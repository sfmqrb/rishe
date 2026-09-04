# Verification process log — verify-page-50


## [2026-09-04T19:35:16.608Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 50 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-50.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-50.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-50.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 50` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T19:35:18.270Z] AGENT

I'll start by reading the instructions file.


## [2026-09-04T19:35:20.447Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:35:20.470Z] TOOL RESULT

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


## [2026-09-04T19:35:20.690Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-50.txt"
}
```


### [2026-09-04T19:35:20.715Z] TOOL RESULT

```
1	=== PDF page 50 (book page 20) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Algwh : worth, value  (refs POK:32)
4	#1 (parent #0) [Avestan] refs=POK:32; SYN:826 | arej, arejah : value ; arejat-aspa : (with) valuable horses ☞Ekwos ; varejah, varecah : value
5	  #2 (parent #1) [Persian] refs=BQT:97,98,102,2265; HRN:241; MON:199, 4999 | arj «ارج» : value ; rzân «ارزان» : valuable, also worthless ; Arjâsp «ارجاسب» : "owner of valuable horses", a male name ; varj «ورج» : value | extra: ارجمند ، ارز ، ارزیدن ؛ ارزش ؛ ورجمند ، ورجاوند
6	#3 (parent #0) [Old Persian] refs=SOD:90 | arjana : valuable
7	  #4 (parent #3) [Sogdian] refs=SOD:90,95 | `yžn : valuable
8	#5 (parent #0) [Greek] refs=POK:32 | alphein : to gain, profit
9	--- entry 1 ---
10	ROOT A.l.h -> redirect to Layh
11	--- entry 2 ---
12	ROOT [Indo-European] Alu : bitter, also used in words related to intoxication, magic and sorcery.  (refs KLN:46; AHD:1506; POK:33)
13	#1 (parent #0) [Latin] refs=OEW:84; KLN:46 | Alŭmen : alum, a bitter salt of aluminum
14	  #2 (parent #1) [French] refs=AHD | aluminium
15	    #3 (parent #2) [Persian] refs=VOP:18 | âlŭmîniyom «آلومینیم» | extra: آلمینیم
16	  #4 (parent #1) [English] refs=OEW:84; KLN:57 | ale ; alum ; alumina ; aluminum ; aluminium
17	--- entry 3 ---
18	ROOT [Sanskrit] Amalaka, Âmlak : emblic tree  (refs KLN:513)
19	#1 (parent #0) [Persian] refs=BQT:61; MON:90 | âmoleh «آمُلَه» : emblic tree | extra: آمُلَج
20	  #2 (parent #1) [Arabic] refs=KLN:513 | amlaj
21	    #3 (parent #2) [Middle Latin] refs=None | emblica
22	      #4 (parent #3) [English] refs=KLN:513 | emblic : a tree
23	
```


## [2026-09-04T19:35:22.418Z] AGENT

I'll read the supporting files first.


## [2026-09-04T19:35:24.598Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T19:35:24.637Z] TOOL RESULT

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


## [2026-09-04T19:35:25.773Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json",
 "description": "Read refs online json"
}
```


### [2026-09-04T19:35:25.813Z] TOOL RESULT

```
<persisted-output>
Output too large (107.1KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b0t9frzur.txt

Preview (first 2KB):
{
 "BQT": {
  "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
  "kind": "archive_djvu+local_scan_ocr",
  "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
...
</persisted-output>
```


## [2026-09-04T19:35:31.379Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','SYN','BQT','HRN','MON','SOD','KLN','AHD','OEW','VOP','IEC','WLD','PHD','NYB','HUB','FVQ','SKT','LKT','ARY']:\n    v=d.get(k)\n    print('=====',k)\n    if v is None: print('MISSING'); continue\n    for kk,vv in v.items():\n        print(' ',kk,':',str(vv)[:600])\n\""
}
```


## [2026-09-04T19:35:31.857Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-50.json | head -300"
}
```


### [2026-09-04T19:35:33.230Z] TOOL RESULT

```
===== POK
  title : J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  edition_found : 1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers
  kind : archive_djvu
  url : https://archive.org/details/indogermanisches01pokouoft
  identifier : indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
  page_offset : POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
  notes : Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)
  local_files : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt']
  cites : page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)
===== SYN
  title : C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  edition_found : 1949 (reprint scans, same pagination in all printings)
  kind : archive_djvu
  url : https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca
  identifier : a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
  page_offset : leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
  notes : Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl.
  cites : page number of Buck, A Dictionary of Selected Synonyms (1949)
===== BQT
  title : Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)
  kind : archive_djvu+local_scan_ocr
  url : https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1
  lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=deh
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/
  page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (
  covers_etymology : True
  notes : Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text file
  scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmq
  cites : page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material
===== HRN
  title : P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  edition_found : 1893 (Google scan, Univ. Michigan)
  kind : archive_djvu
  url : https://archive.org/details/grundrissderneu00horngoog
  identifier : grundrissderneu00horngoog
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
  page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
  notes : OCR of German Fraktur-free text is decent; Persian script is not OCRed.
  cites : page number of Horn, Grundriss der neupersischen Etymologie (1893); entries are also numbered
===== MON
  title : Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)
  kind : website+archive_djvu
  url : https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)
  lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded a
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
  page_offset : None
  covers_etymology : True
  notes : covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on
  cites : page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)
===== SOD
  title : Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  kind : archive_djvu
  url : https://archive.org/details/SogdianDictionary
  lookup_hint : Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/Sog
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt']
  page_offset : printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
  covers_etymology : True
  notes : OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.
  cites : entry number / page in Gharib's Sogdian dictionary
===== KLN
  title : E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  edition_found : 1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)
  kind : archive_djvu
  url : https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein
  identifier : a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
  page_offset : KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
  notes : Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)
  local_files : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt']
  cites : page number, continuous across the two volumes (1966–67)
===== AHD
  title : W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)
  edition_found : Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)
  kind : archive_djvu+website+archive_restricted
  url : https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only
  identifier : watkins-american-heritage-dictionary-of-indo-european-roots-1985
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
  page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
  lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves 
  notes : AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.
  cites : page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)
===== OEW
  title : J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984
  edition_found : 1984 (lending-only)
  kind : archive_restricted
  url : https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view
  identifier : originsofenglish00jose (also originsofenglish0000ship)
  local_file : None
  page_offset : None
  lookup_hint : Borrow via IA lending (djvu.txt returns 401/403). Entries are IE roots in alphabetical order; use IA's in-book search: https://archive.org/details/originsofenglish00jose?q=<root>
  notes : RE-SEARCH 2026-09: borrowable only (Internet Archive lending, 1 hr / 14 days with a free account).
===== VOP
  title : Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992
  kind : none
  url : None
  lookup_hint : Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).
  local_file : None
  page_offset : None
  covers_etymology : True
  notes : RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only.
===== IEC
  title : S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  edition_found : 1984-1987 (complete, cols./pp. 1-1682)
  kind : archive_djvu
  url : https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987
  identifier : mann-an-indo-european-comparative-dictionary-1984-1987
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
  page_offset : TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
  notes : 
  cites : column/page number of Mann, An Indo-European Comparative Dictionary (1984–87)
===== WLD
  title : A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32
  edition_found : ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online
  kind : archive_djvu
  url : https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)
  identifier : in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sou
  page_offset : Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
  lookup_hint : Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
  notes : Tried IA (several queries), Google Books API (quota exceeded / not full view), HathiTrust (blocks automated access, 403). Band 2 (1927) is US public domain; Band 1 (1930) became US PD in 2026, so HathiTrust full view may exist - check manually at https://catalog.hathitrust.org/Search/Home?lookfor=walde+pokorny+vergleichendes. || UPDATE 2026-09: Bände I and II obtained in full from the Digital Library of India scans on archive.org (open, OCR layer in the _text.pdf).
  cites : volume (WLD1 / WLD2) and page of Walde–Pokorny
===== PHD
  title : D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  edition_found : 1971 (open scan; plus PDF on parsianjoman.org)
  kind : archive_djvu
  url : https://archive.org/details/a-concise-pahlavi-dictionary
  identifier : a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
  page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
  notes : 
  cites : page number of MacKenzie, A Concise Pahlavi Dictionary (1971)
===== NYB
  title : H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  edition_found : 1964 (Part I texts) and 1974 (Part II glossary)
  kind : archive_djvu
  url : https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg
  identifier : a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
  page_offset : Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
  notes :  local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt (Part II, pp. 1-286); /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt (Part I, plain djvu.txt)
  local_files : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt']
  cites : page number of Nyberg, A Manual of Pahlavi, Part II Glossary (1974)
===== HUB
  title : H. Hübschmann, Persische Studien, Strassburg 1895
  edition_found : 1895 (Google scan)
  kind : archive_djvu
  url : https://archive.org/details/persischestudie00hbgoog
  identifier : persischestudie00hbgoog (duplicate: persischestudie01hbgoog)
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
  page_offset : leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
  notes : Built from djvu.xml (no hocr); OCR quality moderate.
  cites : page number of Hübschmann, Persische Studien (1895)
===== FVQ
  title : Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
  kind : archive_djvu
  url : https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)
  lookup_hint : Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt']
  page_offset : printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves)
  covers_etymology : True
  notes : Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.
  cites : page number of Jeffery, The Foreign Vocabulary of the Qurʾān (1938)
===== SKT
  title : W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)
  edition_found : 1911 'new and corrected impression' (Google scan)
  kind : archive_djvu
  url : https://archive.org/details/aconciseetymolo01skeagoog
  identifier : aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
  page_offset : leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
  notes : Nourai says '1882-1967'; the 1967 Oxford reprint reproduces the 1911 rewritten edition, so the 1911 scan is the right pagination.
  cites : page number of Skeat, Concise Etymological Dictionary
===== LKT
  title : K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  edition_found : 1927
  kind : archive_djvu
  url : https://archive.org/details/etymologische00lokoguat
  identifier : etymologische00lokoguat
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt
  page_offset : leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
  notes : 
  cites : entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)
===== ARY
  title : Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.
  kind : local_scan_ocr
  url : 
  lookup_hint : Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt']
  page_offset : printed page = pdf page + 1
  scans : [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf', 'first_printed': 1, 'last_printed': 546, 'pdf_offset': -1, 'lang': 'fas+eng', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt'}]
  notes : Image-only PDF provided by the owner (2026-09-04). Use as an additional modern source alongside Wiktionary/Cheung/Hasandust when judging Persian arrows; cite as ARY:<page>. | full OCR text fas+eng (headwords in Persian and Latin caps), printed = pdf+1 | Latin-only OCR (cleaner for transliterated headwords, root names, Pokorny numbers)
```


### [2026-09-04T19:35:35.229Z] TOOL RESULT

```
{
    "pdf_page": 50,
    "book_page": 20,
    "entries": [
        {
            "root": {
                "name": "Algwh",
                "lang": "Indo-European",
                "refs": "POK:32",
                "gloss": "worth, value"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:32; SYN:826",
                    "words": [
                        {
                            "translit": "arej, arejah",
                            "gloss": "value",
                            "script": null
                        },
                        {
                            "translit": "arejat-aspa",
                            "gloss": "(with) valuable horses",
                            "script": null,
                            "see": [
                                "Ekwos"
                            ]
                        },
                        {
                            "translit": "varejah, varecah",
                            "gloss": "value",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "BQT:97,98,102,2265; HRN:241; MON:199, 4999",
                    "words": [
                        {
                            "translit": "arj",
                            "gloss": "value",
                            "script": "\u0627\u0631\u062c"
                        },
                        {
                            "translit": "rz\u00e2n",
                            "gloss": "valuable, also worthless",
                            "script": "\u0627\u0631\u0632\u0627\u0646"
                        },
                        {
                            "translit": "Arj\u00e2sp",
                            "gloss": "\"owner of valuable horses\", a male name",
                            "script": "\u0627\u0631\u062c\u0627\u0633\u0628"
                        },
                        {
                            "translit": "varj",
                            "gloss": "value",
                            "script": "\u0648\u0631\u062c"
                        }
                    ],
                    "script_extra": "\u0627\u0631\u062c\u0645\u0646\u062f \u060c \u0627\u0631\u0632 \u060c \u0627\u0631\u0632\u06cc\u062f\u0646 \u061b \u0627\u0631\u0632\u0634 \u061b \u0648\u0631\u062c\u0645\u0646\u062f \u060c \u0648\u0631\u062c\u0627\u0648\u0646\u062f",
                    "note": null,
                    "quote": {
                        "text": "\u0646\u0647 \u062a\u0646\u0647\u0627 \u0634\u0647 \u0648 \u062e\u0633\u0631\u0648 \u06a9\u0634\u0648\u0631 \u0627\u0633\u062a - \u06a9\u0647 \u0634\u0627\u0647 \u0627\u0633\u062a \u0648 \u0628\u0627 \u0648\u0631\u062c \u067e\u06cc\u063a\u0645\u0628\u0631 \u0627\u0633\u062a",
                        "poet": "Ferdows\u00ee"
                    }
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Old Persian",
                    "refs": "SOD:90",
                    "words": [
                        {
                            "translit": "arjana",
                            "gloss": "valuable",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "Sogdian",
                    "refs": "SOD:90,95",
                    "words": [
                        {
                            "translit": "`y\u017en",
                            "gloss": "valuable",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "POK:32",
                    "words": [
                        {
                            "translit": "alphein",
                            "gloss": "to gain, profit",
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
                "name": "A.l.h",
                "redirect": "Layh"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Alu",
                "lang": "Indo-European",
                "refs": "KLN:46; AHD:1506; POK:33",
                "gloss": "bitter, also used in words related to intoxication, magic and sorcery."
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "OEW:84; KLN:46",
                    "words": [
                        {
                            "translit": "Al\u016dmen",
                            "gloss": "alum, a bitter salt of aluminum",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "French",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "aluminium",
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
                    "refs": "VOP:18",
                    "words": [
                        {
                            "translit": "\u00e2l\u016dm\u00eeniyom",
                            "gloss": null,
                            "script": "\u0622\u0644\u0648\u0645\u06cc\u0646\u06cc\u0645"
                        }
                    ],
                    "script_extra": "\u0622\u0644\u0645\u06cc\u0646\u06cc\u0645",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 1,
                    "lang": "English",
                    "refs": "OEW:84; KLN:57",
                    "words": [
                        {
                            "translit": "ale",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "alum",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "alumina",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "aluminum",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "aluminium",
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
                "name": "Amalaka, \u00c2mlak",
                "lang": "Sanskrit",
                "refs": "KLN:513",
                "gloss": "emblic tree"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Persian",
                    "refs": "BQT:61; MON:90",
                    "words": [
                        {
                            "translit": "\u00e2moleh",
                            "gloss": "emblic tree",
                            "script": "\u0622\u0645\u064f\u0644\u064e\u0647"
                        }
                    ],
                    "script_extra": "\u0622\u0645\u064f\u0644\u064e\u062c",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Arabic",
                    "refs": "KLN:513",
                    "words": [
                        {
                            "translit": "amlaj",
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
                    "lang": "Middle Latin",
                    "refs": null,
                    "words": [
                        {
                            "translit": "emblica",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "English",
                    "refs": "KLN:513",
                    "words": [
                        {
                            "translit": "emblic",
                            "gloss": "a tree",
                            "script": null
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


## [2026-09-04T19:35:38.218Z] TOOL CALL #7: Bash

```json
{
 "command": "ls data/verification/ | head -30 && echo \"---\" && sed -n 1,200p tools/verify_check.py"
}
```


### [2026-09-04T19:35:38.271Z] TOOL RESULT

```
page-101.json
page-126.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
page-44.json
page-45.json
process
sources
---
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


## [2026-09-04T19:35:44.516Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: alg\" POK_full.txt | head; echo \"=== POK_full block\"; awk '/Root \\/ lemma: al[gG]/{f=1} f{print} f&&/Page\\(s\\)/{exit}' POK_full.txt | head -60"
}
```


## [2026-09-04T19:35:45.049Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==41' POK_01.txt | head -80"
}
```


### [2026-09-04T19:35:46.156Z] TOOL RESULT

```
4192:Root / lemma: alg"!!- 
=== POK_full block
Root / lemma: alg"!!- 

Meaning: 'to earn, price, value, *precious bright metal' 

Material: Old Indie arhati^ is worth, earns, is obliged, debit, ', argha-h^ value, validity, price 

' (=osset. 5/y ' price, value '), Avestan arejaiti' is worth, amounts for value ' (npers. 

arzTdan^ earn '), arajah-{es- stem) n. " value, price '. 

maybe alb. {*arhati) argaV worker, serf', argetoj' entertain, reward, please, become lazy 
', argome^ barren, unproductive'. 

Gr. ctAcpn 'acquisition, purchase ' = Lithuanian a/ga, Old Prussian Gen. Sg. a/gas' wage 
', gr. aAcpavu), aAcpsTv " profit, earn ' (aAcpsTv = Old Indie arhati, but by the more complete 
present aAcpavu) in the validity embedded as an Aorist), aA(p£aipoiO(; " cattle earned '. Note: 
common lllyrian g"- > b-. 

An additional form on voiced-nonaspirated is Old Indie arjatT acquires, earns, fetches 



References: WP. I 91. 
Page(s): 32-33
```


### [2026-09-04T19:35:48.276Z] TOOL RESULT

```
 1916,  IX  10);  dl'/X  TiSTCOidwq  Hom. ; iclyiifxog  ,stark,  kräftig;  von  Waffen:  wehrbar,  zum  Kampfe  tauglich^;
ags.  ealgian  ,schützen,  verteidigen^  (*algöjan)]  got.  alhs  (f.,  kons.  St.) ,TempeP,  ags.  ealh^  as.  alah  m.  ds.,  urnord.-run.  aluh  , Amulett^  (?),  alit. elkas,  alkas  m.  ,heiliger  Hain,  Stelle  auf  einem  Hügel,  wo  man  früher Opfer  verrichtet  hat^,  lett.  elks  m.  ,Götze^  (die  germ.  und  halt.  Worte  ur- sprüngl.  ,heiliger,  abgeschlossener  oder  der  Nutznießung  entzogener  Hain^);
toch.  B  aläsk  ,beseitigen^
S.  die  ähnliche  Wz.  areq-  ,verschließen,  schützend
WP.  I  89  f.
algh-  ,Frost,  Kälte'.
Lat.    algor   ,Frost,    Kälte',    algeö,  -ere   ,frieren',    algidus    ,kalt'    gehören
nach   Liden,   Studien  z.  ai.   und   vgl.   Sprachgesch.   QQ^  zu   aisl.   Gen.  Sg.
elgiar,  nisl.  elgur  m.  ,Schneegestöber  mit  starkem  Frost,  halbgeschmolzener
Schnee'.  Germ.  s-St.  *alnz-  deckt  sich   mit   dem  lat.  algor,  idg.  *alghes-.
WP.  I  91,  WH.  I  29.    Vgl.  Petersson  Ar.  u.  Arm.  Stud.  126.
alg}fh-  ,verdienen,  Gegenwert'.
Ai.  ärhati  ,ist  wert,  verdient,  ist  verpflichtet,  soll',  arghd-h  ,Wert, Geltung,  Preis'  (=  osset.  ary  ,Preis,  Wert'),  av.  ardjaiti  ,ist  wert,  kommt
in    Wert    o-leich^    (npers.    arzldan    .verdienen'),    ar^jah-    (e.s-St.)    n.    ,Wei-t,
rrei:j'.
Gr.  «Aojj;,  yEi'u^erb'^  =  lit.    algä,  apr.    Gen.    Sg.    älgas    ^Lolin*^^    äXcpccvo),
alwsTy  ,einbring-en;  verdienen^  (dlcfsTv  =  ai.  drhati,  aber  durch  das  vollere Prc'is.  dlcpdyd)  in  die  Geltang  als  Aoi'ist  gedrängt)^  dXcpsalßotog  \,Kinder einbringend^
Eine  Nebenform  auf  unaspii-ierte  Media  ist  ai.  arjati  ^erwirbt^  verdient, schafft  herber.
WP.  I  91.
a/p-  ,klein,  schAvach*?
Ai.  dl'pct-,  alpaka-  ^klein,  gering^  (alpena^  alpät  , leicht,  schnell*);  schwer in  der  Bedeutung  zu  vereinen  mit  lit.  alpstü,  alpaü^  alpti  ^ohnmächtig werden^,  alpüs  ^schwach^^  lett.  elpe  Jjuftschöpfen^  Atemzug*^,  alpä  ^Mal, Zeitpunkt^
Anreilmng  auch  von  hom.  dXaTT.advog  (bei  Aeschylos  Xaitaövog)  ^schwach'^, aXana^ü)  ;,leere  aus^  erschöpfe^^  att.  XaTtcct^u)  ^plündere^,  XaTtazTO)  ^leere (den  Leib)  aus^  ist  bedenklich  wegen  ihrer  zweisilbigen  Wzf.  gegenüber der  leichten  der  ai.  und  lit.  Worte;  auch  stehen  sie^  sowie  die  ihnen  an- gereihten XaTtagög  ^schmächtige  dünn^  offenen  Leib  habend^^  Xarrdoa ^Flanke;,  Dünnung  des  Leibes  an  der  Hüfte^;,  X&7ia^og  ;,Aushöhlunge
```


## [2026-09-04T19:36:01.382Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK leaf 40 (p.32) tail\"; awk 'BEGIN{RS=\"\\f\"} NR==40' POK_01.txt | tail -20; echo; echo \"=== SYN leaf 850 (p.826)\"; awk 'BEGIN{RS=\"\\f\"} NR==851' SYN.txt | head -60"
}
```


## [2026-09-04T19:36:02.495Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD grep arzn/aryn\"; grep -n -i \"valuable\" SOD.txt | head -40"
}
```


### [2026-09-04T19:36:02.943Z] TOOL RESULT

```
=== POK leaf 40 (p.32) tail
  nachweisbar,  trotz  Specht  Dekl.  114, da  bett.  ali-  ,weiß^  sehr  unsicher  scheint  (Couvreur  H  149  f.,  Friedrich IF.  58,  94)  und  gr.  dllcpalog,  ällcpaTa,  äh^  anders  zu  erklären  sind.
Hierher  aber  wohl  (als  ,bellgelbe  Pflanze^)  hisp.-lat.  ala  ,inula,  Alant^ (Isid.),  span.-portug.  ala  ds.,  dazu  mit  -r^^Suffix  abd.  alaoit  ds.,  damit etymologisch  identisch  der  Fiscbname  abd.  ahmt  (jünger  alant),  as.  alund ,Weißfisch,  Alant'^  =  (mit  gramm.  Wechsel)  aisl.  -qlunn  ,ein  Fisch^,  idg. Grundform  "^al-nt-l^al-ont-.  Die  ursprüngliche  Bedeutung  von  al-  ist  wohl ,weiß,  glänzend^,  daher  dann  auch  ,bellgelV  usw.
Eine  genaue  Trennung  der  Bedeutungen  von  al-  und  el-  ist  nicht  immer möglich,  weshalb  Specht  (Idg.  Dekl.  59,  160)  beide  Stämme  für  ursprüng- lich identisch  erklärt,  also  al-  als  tl-  auf  el-  zurückführt,  womit  er  ferner (aaO.  114)  die  Farbwurzel  ar-  (s.  unten  areg-),  er-  identifiziert.
WP.  I  92  ff.,  WH.  I  26  f.
aldh-  ,Tvoo;'.
Altn.  alda  f.  , Welle,  Feindschaft^;  norw.  dial.  olda  f.  ,Trog^;  schwed.  dial. älla  ,längliche  Vertiefung^  Vgl.  ags.  ealdop.  aldot,  aldaht  ,Trog,  Bottich^, nbd.   bair.  alden  , Ackerfurche^.
32  t
Dcazu  baltoslav.  *aldiiä-  in  ksl.  ladiji,  ahdiji  f.  ^Kahn^^  lit.  aldijä,  eldijä f.  ^Flußkahn^,  auch  lit.  eldijeU  ^Räucherpfanne^
Norw.  lodje  ^russisches  Fahrzeug'^,  schwed.  lodja,  mnd.  lod{d)ie,  loddige sind  aus  russ.  lod'bjd  (=  asl.  ladiji)  entlehnt.  Falk-Torp  652  (s.  auch  789 unter  *olde).
WP.  I  92,  WH.  I  35,  Trautmann  6.
aleq-  ^abwehren,  schützen^,  vermutlich  eigentlich  ^abschließen  und  dadurch schützend
Ai.  rdksati  ,hütet,  schirmt,  bewahrt^,  arm.  aracel  ,weiden,  hüten^  (Pisani KZ.  68,  157),  gv.  dXe^co  ,wehre  ab,  schirme^  (so-Präsens;  raksati  wegen dieser  Obereinstimmung  nicht  wahrscheinlicher  zur  gleichbed.  Wz.  areq-), "AleY-TiOQ,  ^ Als'ATQVibv  epische  Eigennamen,  die  nach  dem  Bekanntwerden des  Hahns  auch  zur  Bezeichnung  dieses  streitbaren  Tieres  verwendet  wurden (Fick  est.  9,  169,  Kretschmer  KZ.  33,  559 ff.,  Boisacq  1091  f.);  älaUslv ,abwehren^,  äXytad'ca  , wehre  ab,  helfe^,  äh/,(xQ  ,Schutz,  Schutzwehr,  Hilfe^, ertal^ig  ,Schutz,  Brustwehr,  bes.  Zinnen  der  Mauern;  Hilfe^  (*aAx-2rt-g), äX%ri  ,  Ab  wehr,  Hilfe^  und  , Stärke,  Kraft^  (letztere  Bed.,  obwohl  an  sich aus  ,energischer  Abwehr^  verständlich,  vielleicht  durch  Zusammenfließen  mit einem  anderen,  dem  mpers.  avh  , Arbeit,  Anstrengung,  Mühe^  entsprechenden Worte,  s.  Bartholomae  Heidelbg.  SB. 

=== SYN leaf 850 (p.826)
oor’ (below). Miihl.-Endz. 2085 f.
lett. mazlurigs, cpd. of maz ‘little’ and turigs ‘wealthy’ (11.51).
6. ChSl. ubogti, nebogtt, SCr. ubog, Boh, Mg Pol. ubogi, Russ. ubogyj, neg. epds. beside bogati% ‘rich’
ae ti] rich’, etc. ; ChSl. nist renders Grk. rrwxés more quently than ubogit, mostly as sb.
*  FTaybs
Digitized by Arya Samaj Foundation Chennai and eGangotri
SION PROPERTY, COMMERCE 733
‘poor person, beggar’ (Jagié, Entsteh- ungsgesch. 408; and so Russ. niscij mostly ‘beggar’), fr. *nistyo- or *niskyo-, precise analysis uncertain but based on a form cognate with Skt ni- ‘down’, ChSl. nizi ‘down’, etc: Zubaty, KZ 31.58 ff. Meillet, Etudes 2.380f. End- zelin, Z. sl. Ph. 13.78.
SCr. siromagan, cf. late (Serb.-)ChSl. siromacht, siraki ‘poor’, fr. ChSl. szrz ‘orphaned’ (2.75).
Boh. chudy = Pol. chudy ‘lean, wretched’, SCr. hud, Russ. chudoj ‘evil, bad’ (Russ. also ‘lean’), ChSl. chudi ‘small, insignificant’, etc. perh. : Skt. ksud- ‘crush, pound’, ksudra- ‘small’. Walde-P. 1.502. Berneker 405.
Pol. biedny, Russ. bednyj (= Boh. bidny, SCr. bijedan ‘wretched, miser- able’, ChSl. bédintt ‘maimed’) : ChSl. béda ‘necessity’, béditt ‘compel’, etc. Berneker 54. Walde-P. 2.185 f.
7. Skt. daridra-, lit. ‘wandering about, roving’, hence ‘poor’ and as sb. ‘beggar’ : daridra- intens. to dra- ‘run’. Walde-P. 1.795. Ublenbeck 121.
Skt. nir-dhana, neg. cpd. of dhana- ‘property, wealth’ (11.41).
Av. drigu-, driyu-, etym.? Walde-P. 1.821. Barth. 777 f.
Av. aSaéta-, neg. cpd. of Saéta- ‘wealth’ (11.42).
11.53 BEGGAR
Sartdvos, haxonépns Get bidagwa Lith. elgeta, ubagas pats N skal a olmusu- Lett. nabags, diedelnieks tant maor is ag Dane” tigger Scr ‘proafil matdigo, mendigane  ‘S¥- —‘téggare Boh. Zebra ; rae : 8 wedla Pol. zebrak : bee ‘begging’) te begger(e) Russ. nistij caro E beggar Skt. bhikgu-, daridra-, Hone” Du. —_bedelaar yacaka- Kerbara OHG  betalari Av ;
MHG betelere NHG betiler
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
784 SELECTED INDO-EUROPEAN SYNONYMS
?
The majority of the words for ‘beggar are from verbs for ‘ask for’ (18.35). But several are in origin opprobrious epithets (like NE bum), based in part upon certain physical or mental defects.
1. Grk. rrwxés : ret ‘timid, fearful, cowering’, rrwoow ‘cower, cringe’, rrjc0w “cower, crouch’, (these: zirrw ‘fall’, mérrwxa, etc.). Walde-P. 2.19. Boi- sacq 823.
NG fnridvos, fr. {nr ‘seek, ask for’ (11.31, 18.35).
NG dtaxonépns, fr. dtaxovd ‘serve’ (formerly also ‘beg’, now draxovebw), fr. dtaxovos ‘servant, deacon’.
2. Lat. mendicus (> Sp. mendigo), prob. orig. ‘defective, unsound’ : men- dum and menda ‘physical defect, fault’, W. man ‘spot, mark (on the body)’, Skt. minda- ‘physical defe
```


### [2026-09-04T19:36:02.990Z] TOOL RESULT

```
=== SOD grep arzn/aryn
22692:valuable,  worthy 
95071:valuable    2274
```


## [2026-09-04T19:36:11.925Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22660,22710p' SOD.txt; echo \"=== pages file\"; grep -n \"valuable\" SOD_pages.txt | head -20"
}
```


### [2026-09-04T19:36:12.001Z] TOOL RESULT

```
2269  'ywznkyS  =»  'ywznk'yS 

2270  }ywz(y)  C  to  tifcy 
ayoze   ©pi.  -/    =»}ywst-,  *ywz 

tempest 

BSTii  908.12;  C2,  40R 12 

2271  >yy    M  (A*  «J>-\$» 
ay   ©voc. 

hey 

Hen.  Tales.  478.9,  10 

2272  >yz-    B  o*J'{J*J<o±~<jt 
iz   ©<yaza   =*yz- 

0o)worship,  (fo)sacrifice 
SCE  248;  GMS  206a 

2273  >yzn   S  klJ&ix^jJ 
ezan   ^'yzn,  {yjn 

worthy,  reliable 
MDii  pl42  n9;  MDiii 

2274  >yzn    C  4s^li  <jiui  jjl 
ezan   ©<OP  arjana   ©pi.  -/   ^yzn,  *yJn» 

'yscWy 
valuable,  worthy 


J*J->'  ^ 


GMS  290;  STii  6.47,  34;  C2  gloss. 

2275  'yzndy  C 
ezande   Oyjndy,  }yznty)   =>>yznty 
worthy 
STii  2.19,  23;  GMS  290,  810;  -ty,  STi  59.19 

2276  >yznty   B 
ezande   =^Jyzndy 
worthy 

BSTBL,  Vim.  44;  GMS  290 

=== pages file
10377:     valuable, worthy                                                  thanksgiving
39801:ultra-miraculous      9681               unobtained       5709                    valuable     2274
```


## [2026-09-04T19:36:13.051Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"11.87\\|11.88\\|11.86\\|PRICE\\|DEAR\\b\" SYN.txt | head -30; echo \"=== arejah\"; grep -n \"ar.jah\\|arejah\\|arəjah\" SYN.txt | head"
}
```


### [2026-09-04T19:36:13.129Z] TOOL RESULT

```
11162:5. Lith. brangenybé ‘a valuable’ and ‘jewel’ (cf. NSB s.v.), deriv. of brangus ‘dear, costly’ (11.88). Also brangus akmuo ‘costly stone’.
11163:Lett. dargums, fr. ddrgs ‘dear, costly’ (11.88).
11164:1 (6. es G iaqormment ( G kleinot NH : i Keinood, eee (in general), 6. SCr. dragulj, Boh. drahokor (ef. Heinod, © ‘a “ae cpd. of klein in | kdmen ‘stone’), Russ. dragocennost’, fr. ep (MHG) “a ance elegant, fine’ ChSI. dragi, etc. ‘dear, costly’ (11.88). ? lier ae clene, NE clean) and (0HG Kleint 0) Lad (Pras possession’ 7. Skt. ratna- (also ‘treasure, goods’), OHG “id; aes ‘a ad ‘possession’, perh. fr. *rgtno- : Ir. rét ‘thing’ (*rentu). ), OS p (Lat. ue ‘eiches’ Hence Lith. | Walde-P. 2.374. Uhlenbeck 243. OB éad, ee but not in NSB), Skt. mani-, esp. ‘pearl’, etym.? Leinolas . 2.295. inh Pol, klejnot. Walde-P. 2.295 6.73 RING (For Finger)
18740:11.86 Srorz, SHOP
18741:11.87 Pricr
18742:11.88 Dear (=Costly, Expensive) 11.89 CHmap
19508:Goth. (ga)lausjan, OHG lésen, MHG lesen, NHG lésen (but now mostly in secondary applications), fr. Goth. laus ‘empty, vain’, OHG lds ‘free’, these fr, the root of Goth. kusan in Sraliusan ‘lose’ (11.88), etc.
20780:ee ON lawn, Dan. Ign, Sw. in, OB lean, Du. loon, OHG, MHG lin, NHG lohn, all in older periods most- ly reward’, prob. : Ir. log, hiag ‘price, renard’ (11.87), Lat. lucrum ‘gain, prof- it (11.78), Grk. Xela ‘booty’, etc. Walde- P2379, Falk-Torp 681. Feist 325.
20791:5. Lith., Lett. alga (OPruss. gen. sg. dlgas) : Grk. ad¢q ‘produce, gain’, Skt. argha-, Av. arajah- ‘value, price’ (11.87), Skt. arh-, Av. araj- ‘be worth’. Walde- Je ile
20872:W. gwerthu, Br. gwerza ‘sell’, fr. W. gwerth ‘value, price, sale’, Br. gwerz ‘sale’, prob. : Goth. wairhb, OHG werd, ete. ‘value, price’ (11.87), Lat. vertere ‘turn’, etc. Walde-P. 1.275. Pedersen 2.526.
20927:Lith. prekiauti, fr. preké ‘wares, mer- chandise’ (formerly ‘trade’ and ‘price’: see 11.87), this also : pirkti ‘buy’.
20999:11.86 STORE, SHOP
21013:It. negozio ‘trade, business’, also ‘place of business, shop’, fr. Lat. nego- tiwm ‘business, affair’ (cf. negotiart ‘trade’, 11.88).
21043:the th nch along 11.87 PRICE oth. wairp, andawairpt Lith. kaina
21064:11.88 DEAR (= Costly, Expensive)
21080:derivatives of It. costo, ete. ‘cost? (11.72), as It., Sp. costoso, OF r. costeus (> ME costouse > W. costus), Fr. cotteux, NE costly, NHG kostbar, etc. 1. Grk. zodvredjs, cpd. of zodb ‘much’ and last member fr. rédos ‘tax, toll, duty’ (11.69). Grk. riptos, fr. riuy ‘price’ (11.87). NG dxpiBés, fr. class. Grk. axpifis ‘exact, precise, accurate’ then (fr. ‘exact in money matters’) ‘parsimonious, stin- gy’ and hence ‘dear’ (as SCr. skup, be- low). 2. Lat. carus (> It., Sp. caro, Fr. cher) ‘dear’ = ‘beloved’ (16.28) and ‘ex- pensive’ (Plaut. in both senses). Rum. scump, fr. Slavic, cf. Bulg. ska- pu, etc. below, 6. 3. Ir. logmar, epd. of log ‘price’ and mar, mor ‘great’.
21113:7. Skt. mahargha-, epd. of maha- ‘large, great’ and argha- ‘price’ (11.87).
21114:Skt. bahumilya-, cpd. of bahu- ‘much, many’ and milya- ‘price’ (11.87).
21123:Grk. etwvos, epd. of ed- and aves ‘price’ (11.87).
21135:NIr. saor, orig. ‘free’ (19.44). The sense ‘cheap’ is prob. acquired by con- trast with daor ‘enslaved, captive’ and ‘dear, expensive’ (11.88). The sense ‘free’ lent itself readily to ‘cheap’ (cf. W. rhad).
21138:4. ON adyrr, OF undéor, ME undere, OHG untiuri, MAG untiure, neg. cpds. of ON djyrr, etc., ‘dear, expensive’ (11.88).
21141:bargain, trade, or market’, with OR ceap, ME chepe, Du. koop ‘trade (= sale or purchase), market, bargain, etc.’ : Or céapian, etc., ‘trade’ (11.88). NED BY cheap sb. Cf. the It. and Fr. locutio: above, 2.
22996:OHG winkil, MHG, NHG winkel (cf. OE wincel in place names; (Du. winkel ‘shop’ fr. ‘corner’, 11.87) : OHG winchan ‘move sideways, stagger, nod’, OE win- cian ‘close the eyes, wink, nod’, wince ‘a winch’, Lith. vengét ‘shun, avoid’, vingis ‘bend, crook’, etc., all fr. common notion of ‘bend, turn’. Walde-P. 1.260. Wei- gand-H. 2.1269.
28110:16.28 DEAR Grk. gles Goth. liufs Lith.  mielas NG &yamnrés (pos) ON ljafr, kerr Lett. mil’ Lat. cdrus Dan. kar, elsket ChSl.  viizljublenii, Ljubi It. caro Sw. kar, alskad SCr. mio, drag Fr. cher OE léof, déore Boh. drahy, mily Sp. caro ME _sleve, dére Pol. luby, mity Rum. drag NE dear Russ. mil, dorog Ir. dil, coim, inmain Du. lief Skt. priya- NIr. — dilis, ionmhain OHG  liob Av. — frya-, frida- W. annwyl, cu, hoff MHG liep Br. _ ker, kaez NHG lieb, tener
28111:The majority of words for ‘dear’ Se ‘beloved’) are connected with words for ‘love’ and have been included in the dis- cussion of the latter (16.26). The others, including some in which the earlier sense was ‘dear’ = ‘valuable, ex- pensive’ (11.88), are:
28125:OE déore, ME dére, NE dear, also ‘precious, expensive’ (cf. 11.88) in OF and ME often ‘glorious, noble’ : ON dyrr ‘precious, noble’, OHG tiure ‘glori- ous, excellent, valuable’, NHG teuer ‘dear’ (in both senses), outside connec- tion dub. Falk-Torp 172. Weigand-H. 2.1040 fi.
28884:tis ot Scarcity’) : ON dgrr, OHG ON Seat expensive’ (11.88).
=== arejah
20791:5. Lith., Lett. alga (OPruss. gen. sg. dlgas) : Grk. ad¢q ‘produce, gain’, Skt. argha-, Av. arajah- ‘value, price’ (11.87), Skt. arh-, Av. araj- ‘be worth’. Walde- Je ile
21044:ork tint (vos Hom.) Be vero ‘ Lett. cena XC rip Dan. pris Ch&l. céna Lat pretium Sw. pris SCr.  cijena tt prezzo OE weorp Boh. cena LA ME _sopris, worth Pol. cena Sp. precio NE price Russ. cena Rum. pret Du. = prijs Skt.  vasna-(Ved.), milya-, 1 (69 OHG werd argha- Nir. lwach MHG wert, pris Av. arajah-, paraska- My ay NHG preis ia
```


## [2026-09-04T19:36:27.710Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '2274' in p and 'valuable' in p:\n        print('leaf',i,'printed approx',i-66)\n        print(p[:1500])\n        break\nEOF\necho \"=== SYN leaf for 11.87\"\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport sys\nfor i,p in enumerate(pages):\n    if '11.87 PRICE' in p or 'alga (OPruss' in p:\n        print('leaf',i)\n        print(p[:400])\n        print('---')\nEOF"
}
```


### [2026-09-04T19:36:29.658Z] TOOL RESULT

```
leaf 155 printed approx 89
                                                                                                                         90

 'ywt'cCh)

 2262 »ywt'c(h) S                               lfjib&                 GMS 290; STii 6.47, 34; C2 gloss.
      ew-tac ^yw^c                                                2275 'yzndy
                                                                       worthy C
      alone
                                                                        ezande    Oyjndy, }yznty) =>>yznty
      GMS 1127; TSP 13.10, 3.122; SCE 125; Tales.
        486.20; STi 86.4                                               STii 2.19, 23; GMS 290, 810; -ty, STi 59.19
 2263 >yw wsyy S                                            l^-   2276 >yznty B
                                                                       worthy
      ew-wise ? =^*ws-                                                 ezande =^Jyzndy                               J*J->' ^
      alone
      Sogdica. 249; GMS 1317                                            BSTBL, Vim. 44; GMS 290
 2264 'ywz- =» *ywz                                               2277 'yznty =» >yzndy
 2265 'ywznk**' B, S         ^-*.:: jj)dj^ <Ji* <-u;1*a ijyr^t    2278 >yzt M, C                    <^J jLOU-^ <u'V *ssf
                                                                       izd ((yzt) ©ob. -y, -tty
      ewzang Oywznkh) =*zng                                            public place, street, square
      like, same, s
=== SYN leaf for 11.87
leaf 884

MBE, NE pay : vb. pay (11.65).
MHG solt, NHG sold, fr. It. soldo (above, 2).
5. Lith., Lett. alga (OPruss. gen. sg. dlgas) : Grk. ad¢q ‘produce, gain’, Skt. argha-, Av. arajah- ‘value, price’ (11.87), Skt. arh-, Av. araj- ‘be worth’. Walde- Je ile
6. ChSl. mizda, Boh. mada, above, 1.
SCr. plaéa, Boh. plat, Pol. placa, Russ. plata : SCr. platiti, etc. ‘pay’ (11.65).
Russ. Zalovan’e : zalovat’ ‘gra
---
leaf 893
)bod (ODan. *bdd > ME bothe, NE booth), Dan. bod, NHG bude ‘booth, stall’, locally ‘shop’ : ON bia ‘dwell, prepare’,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
ae biian ‘dwell’, etc. Falk-Torp go, eigand-H. 1.308. NED s.v. booth,
Dan., Sw. buttk, fr. Fr. boutique.
Dan. forretning, lit. ‘business’, algo ‘place of business, shop’ (cf. Dahlerup s.v. 5), fr. forrette ‘perform, dischar
---
```


## [2026-09-04T19:36:40.089Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'arajah-, paraska' in p or ('11.87' in p and 'PRICE' in p):\n        print('=== leaf',i)\n        print(p[:2500])\nEOF"
}
```


### [2026-09-04T19:36:41.795Z] TOOL RESULT

```
=== leaf 893
)bod (ODan. *bdd > ME bothe, NE booth), Dan. bod, NHG bude ‘booth, stall’, locally ‘shop’ : ON bia ‘dwell, prepare’,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
ae biian ‘dwell’, etc. Falk-Torp go, eigand-H. 1.308. NED s.v. booth,
Dan., Sw. buttk, fr. Fr. boutique.
Dan. forretning, lit. ‘business’, algo ‘place of business, shop’ (cf. Dahlerup s.v. 5), fr. forrette ‘perform, discharge execute’. : teveanury’ Le 21-1) : OF seypen re
’ SO Maks scypen ‘cattle- shed’, OHG scopf ‘porch, vestibule’, NED s.v. shop, sb.
NE store (U.S. and colonial = shop) lit. (so Brit. usually) ‘supply, store of goods (of any sort)’, fr. OFr. estor: estorer ‘build, establish, furnish, store’, Lat. instauradre. NED s.v.
Although store definitely replaced shop in this sense (shop only as workshop, blacksmith’s shop, etc.) and was the only term so used in my boyhood, the vb. shop, go shopping remained usual, and recently the sb. shop has been coming back, esp. for the more fashionable shops in the cities.
Du. winkel, orig. (MDu.) ‘corner’ = NHG winkel, etc. ‘corner’ (12.76).
NHG laden, MHG lade, laden rarely in this sense, mostly ‘thick board, plank, window-shutter’, etc., prob. : NHG latte, NE lath, etc. ‘lath’. Weigand-H. 2.5. Kluge-G. 340.
Local equivalents of laden are bude ‘booth’, gewélbe ‘vault’, and more com- monly geschdft ‘business’. Kretschmer, Wortgeogr. 315.
5. Lith. krautuvé, also ‘storehouse’, fr. krauju, krauti ‘heap up, hoard’.
Lett. parduotava, fr. parduot ‘sell’ (11.82).
6. SCr. duéan, Bulg. djukjani, etc.» fr. Turk. dukjan, Arab. dukkan id. Lokotsch 542. Berneker 237. ;
Boh. krdm, fr. MHG kram, NHG kram ‘retail (trade), small (retail) shop, stall, stand’, orig. dub. Walde-P. 1.591. Weigand-H. 1.1135. Berneker 606.
pOSSESSIO
teaylt? = Boh. sklep ee. sklep ‘(burial)
Digitized by Arya Samaj Foundation Chennai and eGangotri
N, PROPERTY, COMMERCE 825
‘bench’, Pol. fawa ‘bench, stand, stall in ° a market’, etc. Berneker 695.
Russ. magazin, fr. Fr. magasin
‘Ol. iyault, ¢? etc a ( bove 2)
- oryP¥» ¢ » dim. of lava | (@ as eat Ee oh. lava, lavka 7. Skt. vipana-, Gpana-, see 11.85.
the th nch along 11.87 PRICE oth. wairp, andawairpt Lith. kaina
ork tint (vos Hom.) Be vero ‘ Lett. cena XC rip Dan. pris Ch&l. céna Lat pretium Sw. pris SCr.  cijena tt prezzo OE weorp Boh. cena LA ME _sopris, worth Pol. cena Sp. precio NE price Russ. c
=== leaf 894
ena Rum. pret Du. = prijs Skt.  vasna-(Ved.), milya-, 1 (69 OHG werd argha- Nir. lwach MHG wert, pris Av. arajah-, paraska- My ay NHG preis ia
The ‘price’ of an article is at least as- sumed to be its ‘value’, and many of the words for ‘price’ are such as were used also for ‘worth, value’ in general. Sev- eral of these and some of the others in- volve the notion of ‘return’ or ‘recom- pense’. The spread of Lat. pretiwm has fumished a more distinctive word to most of the western European languages.
1, Grk. dvos (reg. word for ‘price’ in Hom.) : Skt. vasna-m ‘price’? (RV, AV), * venum ‘sale’, etc. (11.81, Grk. dvéo- iat),
Grk, Tih, also ‘worth, honor, reward, Penlty ‘tla ‘estimate, value, honor’, mwa ‘pay’, ete. (11.65). | eee mostly ‘worth, value’, also Wie a a , Brice’ :aktos ‘of like - ee, (y) ) lt. ‘Weighing as much’,
*@yo ‘lead’, but also ‘draw
town the ntog 2 Weigh’. Walde-P. 1.36,
Rum. pret; ;
i 7 - pret; OF r.
ML 2, ME ee [> W. pris], NE price _~8n., Sw. pris] Du.
ae NHG preis), orale, as
” “Scompense’ neut, of an
adj. *pretios fr. the IE prep. *preti, *proti in Skt. prati ‘against, back’, ChSl. protivi ‘towards’, ete. (these fr. IE *per, pro, ete. and so ultimately connected with Grk. répynue ‘sell’, Lith. pirktz ‘buy’, etc., 11.81; but this remote formal con- nection is without bearing upon the se- mantic development). Walde-P. 2.38. Ernout-M. 808. REW 6746. Falk- Torp 850.
3. Ir. lig, liag (also ‘value’), NIr. luach (also ‘value, cost’): W. golud ‘riches’ (11.42), Goth. laun, etc. ‘wages’ (11.78), etc. Walde-P. 2.380. Pedersen 1.54.
4. Goth. wairp (and andawair pi [and- wair pi cod. Arg.], epd. of and [a]- ‘against, in return’) = ON verd, OE weorb, ME worth, OHG werd, MHG wert ‘worth, value, price’ (NE worth, NHG wert, etc.), beside adjs. Goth. wairps, ON verdr ‘worth, worthy’, etc., perh. : Ir. frith-, MW guwrth, W. wrth ‘against’, fr. the root in Lat. vertere ‘turn’, Goth. wairpan, etc. ‘become’. Walde-P. 1.275. Falk- Torp 1403.
Dan., Sw., ME pris, NE price, etc., above, 2.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
——— oo
826 SELECTED INDO-EUROPEAN SYNONYMS
5. Lith. kaina, ChSI. céna, etc., gen- eral Slavic (Russ. cena > Lett. cena) : Av. kaéna- ‘revenge, punishment’, Grk. mow? ‘retribution, penalty’, IE *k”oina-, fr. the root in Grk. ziw ‘estimate, honor’, tiuy, etc. (above, 1). Walde-P. 1.509. Berneker 124.
Lith. kaina is now the accepted word for ‘price’, whence vb. kainoti ‘cost’ in kiek kainoja ‘how much does it cost?’, et
```


## [2026-09-04T19:36:46.218Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[894]\ni=p.find('826 SELECTED')\nprint(p[i:i+2200])\nEOF"
}
```


### [2026-09-04T19:36:48.348Z] TOOL RESULT

```
826 SELECTED INDO-EUROPEAN SYNONYMS
5. Lith. kaina, ChSI. céna, etc., gen- eral Slavic (Russ. cena > Lett. cena) : Av. kaéna- ‘revenge, punishment’, Grk. mow? ‘retribution, penalty’, IE *k”oina-, fr. the root in Grk. ziw ‘estimate, honor’, tiuy, etc. (above, 1). Walde-P. 1.509. Berneker 124.
Lith. kaina is now the accepted word for ‘price’, whence vb. kainoti ‘cost’ in kiek kainoja ‘how much does it cost?’, etc. Cf. NSB and Hermann, Lit.- deutsches Gespriichsb. 144. Lalis and Kurschat have preké or prekia for ‘price’, but this is now ‘wares’ like Lett.
11.88 DEAR (= Costly, Expensive)
Grk. — xodvreAts, Teptos Goth. galaufs NG axptBés ON dyrr Lat. carus Dan. dyr
It. caro Sw. dyr Fr. cher OE déore Sp. caro ME dere Rum. scump NE dear Tr. logmar Du. duur Nir. daor OHG tiurt W. drud MH
```


## [2026-09-04T19:36:53.298Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"paraska\\|argha-\" SYN.txt | head -20"
}
```


### [2026-09-04T19:36:53.350Z] TOOL RESULT

```
16180:. ddelrer, Tperet), fp podoba in podoba jestii (Supr. 6e?, mpkee: etc.), orig. po-doba ‘what is timely. suitable’ : doba ‘point of time, time’ (not quotable in ChSI., but SCr., Boh, ete., 14.11), Goth. gadaban ‘be suitable’ etc. Similarly Russ. na-doba, whence nadobno or shortened nado impers, ‘it ig necessary’ and the weaker nado(bno) by. Berneker 203 f. SCr. treba, Pol. irzeba (impers.), Boh, | treba jest, all orig. sb. ‘need? : Ch], potréba ‘need’, vb. trébovati, 3sg., tré. bueti% ‘needs’ (9.93). SCr. mora ‘must’ (also Slov.) : more= moze ‘can’ (> r, Leskien SCr, Gram. p. 105, Vondrak, Slav. Gram. p. 459) = ChSI. mozett ‘can’ (9.95). Development fr. ‘can’ > ‘must’ (like ‘may’ > ‘must? | in Gme., above, 4) and differentiated form, spreading fr. Slov. and Croat. ter- | ritory. Rjeénik Akad. 7.1f. Miklosich / 199. Berneker 2.67. Boh. must, Pol. musi, fr. NHG muss. Brickner 348 f. Stender-Petersen 318, Pol. powinienes, usual expression for ‘ought’, fr. adj. powinien ‘obliged’ (:wina ‘fault, guilt’, 16.76) with vb. ‘to be’. SCr. ima, Boh. md, Pol. ma, Russ. imejet ‘has’, all used sometimes like NE has to, most commonly the Boh. md (or mél jest, mél by). | 7. Skt. arhati ‘deserves, may’, some- ! times ‘ought’, beside argha- ‘worth, price’ : Av. arajaiti ‘is worth’, Grk. a\¢7 ‘produce, gain’, 4\¢avw ‘bring in, yield’. Walde-P. 1.91. But in Indo-Iranian the notion of ob- ligation or necessity is commonly ex- pressed by the gerundives or modal forms of particular verbs.
20791:5. Lith., Lett. alga (OPruss. gen. sg. dlgas) : Grk. ad¢q ‘produce, gain’, Skt. argha-, Av. arajah- ‘value, price’ (11.87), Skt. arh-, Av. araj- ‘be worth’. Walde- Je ile
21044:ork tint (vos Hom.) Be vero ‘ Lett. cena XC rip Dan. pris Ch&l. céna Lat pretium Sw. pris SCr.  cijena tt prezzo OE weorp Boh. cena LA ME _sopris, worth Pol. cena Sp. precio NE price Russ. cena Rum. pret Du. = prijs Skt.  vasna-(Ved.), milya-, 1 (69 OHG werd argha- Nir. lwach MHG wert, pris Av. arajah-, paraska- My ay NHG preis ia
21074:Skt. argha-, Av. arafah- (NPers. arz ‘price’) : Skt. arh-, Av. araj- ‘be Worth’ Lith., Lett. alga ‘wages’ (11.78). Walde. P. 1.91. Barth. 192.
21075:Av. paraska-, prob. (*prt-ska-) : Skt, a-prata- ‘without recompense’, and Lat, pretium, etc. (above, 2). Walde-P. 2.38, Barth. 896.
21078:Russ. dorogoj Skt. mahdargha-, bahumi- lya-, etc.
21113:7. Skt. mahargha-, epd. of maha- ‘large, great’ and argha- ‘price’ (11.87).
25641:TIME 1007 14.66 14.67 14.68 THURSDAY FRIDAY SATURDAY gapparov mopcanely oaBBarov Gr “co Acés tutpa "Agpodlrns jyutpa. Kpévov : wapacKkeun ‘ xo rT dies Veneris praia Iat. oe ‘nla feria a feria sabbatum easy venerdi 1 ele vendredi aan pr 4 viernes fi 1eves Lerne sdbado z ‘oui vinert simbdta HL quinta feira sexta Seira sabado Po dardain din diden satharn It dardaoin aoine satharn aM dydd iaw dydd gwener dydd sadwrn hr diziow digwener disadorn Goth “Se paraskaiwe, fruma sabbaté sabbato dags ON orsdagr Srjadagr laugardagr, pvattdagr Nicel. fimtudagur Séstudagur laugardagur Dan. forsdag fredag Igrdag Sy,  torsdag fredag lordag 0E  punresdeeg Srigedeg seter(n)dag ME thursday friday saterday NE thursday friday saturday Du.  dondersdag vrijdag zalerdag OHG donarestag Sriatag sambaztag, sunniinadband MHG donerstac, pfinztac vri(e)tac sameztac, sunnabent NHG donnerstag freitag samstag, sonnabend Lith. Ketvirtadienis (Getvergas) penktadienis (pétnycia) SeStadienis (subata) Lett. celurdiena piektdiena sestdiena a telurlttieis peliiki, pelinica sobota, sabota a ‘hey petak subota Pol, She Pe patek sobota Russ as e piqtek sobota : 9 pjatnica subbota
25658:in Goth., and there are a few in West and North Gme. amid the usual planetary names. Goth. sabbato (mostly unin. flected but also with w- and i-stem forms) with and without dags = Grk. c4BBaroy Or juépa caBBarwy (but independently of the Grk. variation), pis dagis afarsab- baté = ris yds caBBarwy (Mk. 16.2), Srumin sabbatd = xpirn caBBarov (Mi. 16.9), fruma sabbatd = rpoc&BBaroy (Mk. 15.42), beside the borrowed paraskaiwé = mapacxevn (Mt. 27.62, Mk. 15.42),
```


## [2026-09-04T19:37:03.543Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT arej\"; grep -n \"arəj\\|ar.jah\\|arjat\\|Ar.jat\" BRT.txt | head -30; echo; echo \"=== BRT leaf 192+? offset\"; grep -n \"page_offset\" /dev/null"
}
```


## [2026-09-04T19:37:04.228Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\np=pages[241+21]\nprint(p[:3000])\nEOF"
}
```


### [2026-09-04T19:37:05.329Z] TOOL RESULT

```
=== BRT arej
3094:•  j.  a)Ta-  1)  Adj.  (fem.  °rä-)  'der  erste, obierste',  nach  Zeit,  Rang  usw.:  narrjahe ..  yö  vasaite  sarsayamnö  (sd.)  °rqm  usai- am  uSatik^M  \x.i4ao.  a)  n.  'Anfang, das  Oberste,  Spitze':  °ra,  °r>m  F.  7.
5401:Komp.!  a«™™.+fl0.-.  I  ♦  j   arajahvant-  m.  EN.  eines  Gläubigem
7902:sehr,  tarn':    m3   tl  (nämL  kaomahe)    nJre (sd.)    .  .    '"isa    raivanto    ar»jahe    Y,  10. '7-         3)  'ebenso,  gleicher  Weise,  item', mit  Ellipse  des  Verbums^:  vasS /raxitäiteisA.)  aiwi.gäme  '^a  hama Winter;  ebenso  (kann  er  es  tun)  im  Som-
19226:•  j.  nire  Inf.  'hinabzusinken,  -sickern':  ma tl  njre  *z»me  paiti  i^ia  ra!vants  arjjaht "dass  nur  von  dir,  dem  . .,  nichts  auf den  Boden  hinabsickert"  Y.jo.  17.
20168:KompE.  —  Zum  ai.  V.  mämkaU  'er  gibt hin'(?).  —  Eig.  'was  man  drauf  gibt';  Gdn. Stud.  /.  95.  —  Pa.:  masäk.  —  1)  Nicht  'Wert' übeibaupt;  das  ist  arijah-,

=== BRT leaf 192+? offset
```


### [2026-09-04T19:37:07.075Z] TOOL RESULT

```
412
— 241 -
Nicht hierher gehören die Suffixe -var in seriär
löwenhaft' (Sahn. I, 253 Vers 166) oder in selvär
(No. 789) u. a. m.
Das Suffix -awer (z. B. np. jengäwer) ist erst neu-
persisch.
1074. wäriin unglücklich, elend, schlecht*, tcärilne^).
phlv. apärün, aparumh.
Zusammengesetzt aus apa und phlv. rün (das 'Seite,
Richtung zu bedeuten scheint), also eigentlich 'ab-
seits ; vergl. phlv. frarün.
1075. valäne, velane (so im Gazophylacium S. 389)
'Wunde*.
skr. rrand' Wunde* , wozu doch gewiss auch lat.
volmts^) gehört.
1076. veyiMür^ vu/sür 'Prophet' ).
phlv. va/sivar (Denkart); de Lagarde, Ges. Abh.
164 nimmt als Grundform aw. "^va/sahara- an (vergl.
va/sem möi asqsatj vd. 19, 15).
1077. vefif 'Grösse, Würde'.
aw. *tmrecah- in asvaredah-, varei^afihvanf- 'glanz-
reich, prangend*; phlv. varc bezw. varj, varcömamJ
bezw. varjömand (vergl. Salemann, Mel. asiat. IX,
235 Note 35); ai. vdrcas- 'Glanz.
Den von Salemann a. a. 0. citirten FirdüsT-Vers
konnte mir Herr Dr. Landauer nicht nachweisen.
H Häufig mit wazün in den Handschriften verwechselt. Dieses,
sowie wäzüue ist sicher aus bäzyüne (Öähn. I, 197 Vers 1220) ent-
standen, rergl. cün etc. s. v. yün (No. 946).
2) tJber dieses Wort vergl. 0. Hoffmann, BB. XVIir, 291,292.
') In unserem Texte des äähnSme ist in den im FJ angeführten,
von de Lagarde erwähnten Versen ve-^mr durch peiyewber ersetzt
(I, 6 Vers 95); in der Strassburger Handschrift des Ferheng stehen
sie auf Fol. 162 und lauten folgendermassen :
hegnftär-l re/sür-t /ud räh^jöl
d%l ez ieregihä hedln Wf söi
Aus Firdüsl's jQsuf und Zulei;^ä wird ebendaselbst die folgende
Strophe citirt:
bt(/ö ei ;(%reilmend ez in der sü/un
qtyäse zt ve/8ür-i dädär^ hm.
Auch SF hat einen Belcgvors für das Wort.
Uorn, UruDdrUs d. neup. Etyniolugfie. 1(>
```


## [2026-09-04T19:37:24.694Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\n# find leaf containing arjjah-/arijah headword\nfor i,p in enumerate(pages):\n    if 'ar»jah' in p or 'arjjah' in p or 'arijah-' in p:\n        print('leaf',i, p[:200].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-04T19:37:26.352Z] TOOL RESULT

```
leaves 1041
leaf 229 vd  darrja  akarsta  saaa  ..  '6a  i'amiti  .. ila  sadayäj  ya^  "Sa  ..  pdo?m  vamaite'^.yä  darrja  apu'^ ra  *a?i(i  V.J.24.  3)  Es 2.24;  —  fitfii  mi  'oa  *affAäJJ^m  ''^f» .  dient  dazu, 
leaf 605 nd  damit  sie  gefällig ,  erste  Loch  sollst  du  .  .  zwei  Finger  in seien"  Yt 5.127.  der  Tiefe  ausstechen"  V.o.  6. | AbleiL  aus  'm-vaza.  m.  'attraclioii'");   ai.  ni-       Ableit.  a
leaf 642 � 3)  Pü.j  Aaiar  me/i  har  an  oil  vaslrai,  mit  der Erl.:  orL     Vgl.  N. /o. | •  j.  masyö.xra&wä-  f  'grössere  Einsicht^: talla  yä  kasujcratus  ''hmqm  nöit paitiimti "wenn(?)  wer  gerin
```


## [2026-09-04T19:37:35.678Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages[:80]):\n    nums=re.findall(r'\\b(1?\\d{2,3})\\b',p[:300])\n    head=p.strip().split('\\n')[0][:80]\n    print(i,'|',head,'|',nums[:5])\nEOF"
}
```


### [2026-09-04T19:37:37.423Z] TOOL RESULT

```
0 | Google | []
1 | l | []
2 | e | []
3 | e | []
4 | e | []
5 | e | []
6 | e | []
7 | e | []
8 | e | []
9 | e | ['1904']
10 | gle | []
11 | gle | []
12 | 1-19  lV.50-68 | ['19', '50', '68', '69', '74']
13 | Inschriften  Woit  flir  Wort  oder  mit  ganz  genug- | []
14 | roeo    kn | []
15 | üpften, | []
16 | haben   sich   als   tri^erische    erwiesen:    Geldners   'Awesta'    ist | ['1853', '1858']
17 | 147,  Z.  14 ff.)  von  am>sa  sp»nta  bis  jasaiti  (=  Y.  Ä3f.); wo  es  nöti | ['147', '14']
18 | . | ['24', '27', '15', '30', '18']
19 | Vr. S  (151  :Y.  24.1. 7  (181 :  V.  34.  2. B|2i   :V.2j.3. 9  (25)-27  :  V. | ['151', '24', '181', '34', '25']
20 | Y.  75. 8. | ['75', '27', '10', '30', '11']
21 | .  1.  S.2.27. | ['27', '19', '11', '14', '17']
22 | 6. 43  ■■\i.S.A7- | ['43', '46', '47', '43', '50']
23 | .  60. 4. | ['60', '48', '53', '56', '61']
24 | 3- | ['77', '18', '37', '34', '34']
25 | :  V.  6  1,  4- | ['12', '38', '13', '22', '23']
26 | 30  133   ;V.>.38. | ['30', '133', '38', '31', '125']
27 | ;  V. /*.  34,  37,  40,  43. | ['34', '37', '40', '43', '46']
28 | . | ['33', '14', '29', '52', '39']
29 | ist  der  Etymologie  etwas  mehr  Raum  gegönnt worden.     Im  Übrigen  bemerk | []
30 | V       r,  hr      s       z       S      l       k       h       :^ [Ap.]      | []
31 | nd  'Stämme',  Unter  'Verbesserungen'  habe  ich  alle  Fehler  verzeichnet, di | []
32 | Leipzig  1888. (^BfiKLENEccbaiologie:  Die  Verwandtschaft  der  jBdisch-chriitl | ['1888', '1885']
33 | �«-Fragment ;  s.  S.  IX.  lO  L | ['1895']
34 | s  Wörterbuch  der  Albanischen  Sprache.     Strassburg  1891. LMkves  GrEL:  H | ['1891', '1901', '1902']
35 | e  d'apris  le  Maidfisme  h  la  lumiire  des  croyances  paralUles  dans | []
36 | ti t(us).  |  air.:  altirisch. | []
37 | .,  iran.:  iranisch. | []
38 | ii  genannt | []
39 | d. | ['426', '241']
40 | ';  —  w I  nH  aiäAili  i'lse  jamyät  as>mca  ..  asista  tä airihat  Aa'a  vi | ['52', '147', '26', '62', '52']
41 | aya dalnaya  . .  Y,  57. 24;  —  , .  parö  jbi^anbyö .  .  alsqm  tbifyaniqm   | ['57', '24', '11', '75']
42 | ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  . | ['13', '13', '14', '18', '32']
43 | at  öyä  (ISf.)  «>/f  (sd.):  hvö avatahabdgnti  (sd..)  /ramar?nl>m  (sd.)  ag | ['52']
44 | ä  vakrkaAe  k}r?naoiti  ya%a\ai,iAa  drujö  FrVV.  Äi ;  V.  7.52  PüZ.; — yat  | ['52', '10', '28']
45 | H-/°)steckl.Dochs.B(;M,GrGr.3244-    V.  1^.  14;  —  in  Kongruenz  mit  dem  P | ['14']
46 | ^S'^'   '■  3'*-    ~     ^'    "'^''    "■"    beginnt    der | ['50']
47 | visch:  kochersoll  man  niederschlagen,  den  Kessel usia  ahmni  (usw.,  Y.4J- | []
48 | a-,°ö(J  a^ia  yä  kaine  aetakmut  puir-at  *mi- tivisch  angeschlossenem  Nome | []
49 | ,  aetthnuyav- Adj.  (»«h  fem.)  schul-  ,-„,„  Lehir  beiuchen?  Ein  Jah,  la | []
50 | aahe,  g.  +''oaöhe  Inf.  'einem (GÜubigen)  Gewalt  anzutun,  an  ihm  Ge- wal | ['46']
51 | 4s. | ['74']
52 | 1,2a.  Z)   'können, | []
53 | bara  'm (AP.)  bansmaca  U.io^;  —  'masca  bam- maca  N.  7/T.;  —  *kava  °ma | ['108', '62']
54 | sd.) paranlarfm  (sd.)  isöit  N./2;  —  vayö  .  . harn  istmmm  painyätte  ".  | []
55 | Fü. :  |  Y,  und  P.  mit  /rS):  fraatfiiaa ,  (lu  V.  mit nüTräan,  Sü.:  td | ['16']
56 | ,  9.40, 48;  —  ä^ravaium  yaoida^o  ,  .  'so  nä yö  yaoid.1>ryS  V.<).  37—  | ['40', '48', '37', '39', '40']
57 | *frast)r?nte  ya'^a "wer   so   gut   er   kann   das   B.   bereite^ wie  .  ." | ['103', '35', '36']
58 | —    tf/  'jitum  Ä>t-  '■  j  ■  '-'"■:'•'-  'J-  "H-  »"»  ..  -  ■ | ['33', '37']
59 | PÖ.:  öi,  Sü,:  ialam.  DST. ZA.  r.  328  meint:  "siaolä  aojäi  'j'ai  force | ['328', '13', '13']
60 | �  'jönghval Y.4!j.i6. | []
61 | 128;   129—132*, | ['128', '129', '132', '146']
62 | ��^^  ^   _   „  Vgi.  SBE.  4y.  13.     Er  war  der | ['13', '19', '10']
63 | Y./J.-i    - | []
64 | farl aesmtm  N.  /OJ, | ['10', '11', '37']
65 | jrya-  Adj.  (fem.  ya-)  'der  erste' an  Qualität  (usw.):  nit»n>m  .  .  maö | ['41', '43', '37', '37']
66 | gestellten  Sinn  besänftigt  er durch  M."  Yt. /o.  log, | []
67 | ��  a-Jyätay-  £  'Nichtleben':  hyat  ti him  mainya  )asa:t>m  (sd.)  paourvJm | []
68 | ) V.  7.3.         a)  anreihend  'und,  und  auch': | ['22']
69 | h  unten  an- ziehen . .,  wenn  (von  unten)  nach  oben  . ." N.53.  2)    'vo | ['53', '22']
70 | ir^m  k>r3ttaoiti   *sasiB.- | ['60', '20', '32', '23']
71 | ,  nSbisl.  —  O  ^30!.  4; i*  steht  V.  9. 39.  18.  27,  +Yt.  Tl.  8. | ['30', '39', '18', '27']
72 | ltä  °ia asimäl  .  .  7-Tmruyff  ya'iä  . .  vydmrvi/J  .  . sarairus/ro  Y.i2. | []
73 | Y.  JO.  15; — 'runqmca  paitl.ajqinm (sd.)..^;/  *iyeyqm  düräi  as^.TsS(sd.)   | ['15', '42', '17', '46']
74 | ti  V.j.ig;  Vyt. ^5(1*).  43'>  —  °ra  (ava.  'bei  ihm')  anät frajasaiti  ba | ['43', '46', '16']
75 | ��  VgL  äat.  —  Pü,:  clän.  —  ')  Wo ntä  (is,  —  »»  wo  m/iatä  (VS.)  vo | ['26']
76 | akt  mit iyaohnäis  apayantaAei^  "der  die  Worte . .,  aber  in  seinem  Hande | ['77', '19']
77 | ku  man apagayihi  mä  bavät  erläutert;  s.  noch  jUay- No.  1, | []
78 | " nichtung  der  I^benskraft"  YL/5.44.         1Y.65.11. | ['44', '65', '11', '55', '518']
79 | .  4.45;  45;  —  ahun?m  vairJm  . .  Tim sraoidyehya  (^^  frasrüiti  Y.  5. 1 | ['45', '45', '14', '52']
```


## [2026-09-04T19:37:44.943Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"var.cah\\|varcah\\|var.canhvant\\|varjjah\" BRT.txt | head -20; echo \"=== jat.aspa\"; grep -n \"jai.aspa\\|jat.aspa\\|jaj.aspa\\|Arjjata\\|arjjat\" BRT.txt | head -20"
}
```


### [2026-09-04T19:37:45.013Z] TOOL RESULT

```
6548:•  j.  as-varacah-  Adj.  'der  grosse  Kraft,  j  eines    Gebrechens    od.    dgl.:    paitistatse Tatkraft  besitzt':  frar^rase  tarS  'ia  Yt.  19.  yaskaAe  .  .  makrkahe  .  .  'hvaAe  V.  20.  3. 57,58;    —    Vö    yai:a    kava    usa    Az.2;,     Vgl.  o-'-««..  -  Pü.:  fehlt.
10608:49.6;  —  vavlßui  'iüm  ('Wille')  maiiar?hs yä  xsTOvlla  (sd.)  Y.  28.  \\  —  ahya  .  . a.Asi%lfi  (sd.)  ni . .  'tos  (AP.,  'Absichten') .  .  äadat  *var>cahTca  Y._92,i4;  —  yS  .  . %wahmT  'tS  (LS.,  'Ratechluss')  apSrnsm nana  (sd.)  atihat  Y.  4Ä4;  —  dulsastis
11026:—  xratüs  ..  *var3cahTcä  y.j2. 14; — fra gaosävara  sispiit.na  .  ,  minuca  Yt.  77.  10;
=== jat.aspa
25166:•  j.  ranjat.aspa-  Adj.  (fem.  -/ä-)  'der die  Rosse  flink  laufen  lässt':  uiänhfm  .  . TTOlm  'pqm  G.5.  5.
```


## [2026-09-04T19:37:52.919Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"hyaona\\|hySona\\|hyaon\" BRT.txt | head -20; echo \"=== Wert\"; grep -n \"'Wert\\|,Wert\\|Wert'\" BRT.txt | head -20"
}
```


### [2026-09-04T19:37:53.000Z] TOOL RESULT

```
5412:•  j.  araja^aspa-  m.  EN.  eines  Hyaona- Fürsten":  mairyehe  hyaonahe  "pake  \'tf/. 30;  —  drfantptn^a  'piin  Yt.5.  109;  — tum  yazata    vandar^mainis  (sd.)    'ps  Vt.
13109:—  izitu/  nämä"  'Ayätts  a%uräyi^  Bh.2, 10.  11)  im  Atw.:  Uta  at^m  nijanäni RyaonXnqm  'hyunqm  pancasayriäi  .  .  Yt j?.  3 1 ;  —  Uta  azmt  fraourvaisayeni  kumaya (sd.)  *väri'ikanatn  hyaonya  (sd.)  haca 'itihävBiOß.  statt  AblS.)  Ytp.si  \~ydka aztm  nijanäni  tüiryanqm  'hyunqm  panca- saynäi  . .  Yl  5.  54;  /,?-'i43'.  V.J.  42  PüZ., 5. 38PÜZ.;  —  airyanqm*  'Ryunqm*  .. sairimanqm'  'hyunqm'  . .  säininqm'  'hyu- nqm' ..  dählnqm'  'hyunqm''  ..  Dlspanqm* 'hyunqm*  Yt  i^.  i43ff.;  —  kä'ia  airyi' -irihävö  huyäiryh  bat'inti  Yt  8.  36;  56, 58 j;  —  nsit  .  .  airyä  'itihävö  (als  AP.) Art/ (sd.)  hyäi  hama  Yt  8.  56;  —  mi^rtm .  .  huiayamm  atryäbyö  'i^hubyB  Yt.  fo.4;
28958:—  mibints  ('detractus')  h' .  .damabyS  Y.  8. 6; — aptm  tasa/ii['cTaüXi'^)..zrayaahat  h'.. ^■5-  'S!  — yi  ^P^  utbar^nte  ('efferontur') . .  zrayatshat  h'  Yt.  y.  65;  —  aat  aps  ava.- ^arwi/«  ('afFeruntur')  trayaaAata  h'  vouru- kasät  Yt.  A  47;  —  attavat  apat  h'  niiba- ray>n  ('extrahant')  V.  6',  29;  31,  7.34,  Y. ^5- 6;  —  US  h*  a^bys  nmanalibyö  baraysn ('efferant')  .  .  atrtmca  .  .  V.  5. 40 ;  —  apa HS  h  qzanhat  . .  müra  barüs  ('efferas') Yt.  JO.  23;  23;  —  apa.barani  {'auferam') uva  ^Mmca  tarsnpmca  A'  mazdii  dämabyS Wt.g.  10;  10',  5.26,  tp.32,  93;  —  nsit .. apaitibusti  h'  viisbySpara.baraitiy.l3./^o; 10,  II,  N.j^;  —  yö  atnm  sairchyat  h' daitlm  gatüm  avi  ava.baraiti  Ctransfeif ) V.  S.  83;  84-95";  —  fraourralsaymi ('convertam')  humaya  (sd.)  .  .  hyaonya  h daiiihävs  Yt.5. 31;  —  kii>a  nasul  apa- yasäne  ('depellam'J  h'  *ava^hi^  vTsal  V.
30435:•  j.  'hu'mäyä-,  "hu'mayä-  f.  EN.  einer Tochter  Vl/täspas:  tarn  yazata  ..  visiäipS .  .  dazdi  ml  .  .  ya'ha  .  .  uta  azfm fraourvaaayeni  'maya  (IS.)  *värioJianqm (sd.)  hyaonya  haca  daiAAävs  ".  .  und dass  ich  wieder  heimbringe  sammt  der H.  die  V..."  Ytp.  29ff.'>;  —  'mayä (GS.)  aSaonyi  Yt/J.  139.
=== Wert
5129:•  j.  a-var»tä-f.  'Wertgegenstand,  Besitz- tum': siaritasca  g3tus  any5sia  bfrfxiia^sA.) °tä  Yt  //.  7 ;  —  yesi  rn'it  iavan  .  .  pas^m staoräca  aw^qm  hl  'Iqm  altahmifi  naire frabi!ray?n  V.5.39;  ig.id;  —  zur5.bir»ta ,'iä  F.:.'0;  —  Ptspanqm  *°tanqm  saiiavai-
5393:asp  karf  i  sp7i  . .  /fl  humSnik  1  asfi  i  sy.U:      .  j,  ar«Jah-  n.  'Wert,  Preis';  Dur  AS.  'i:
5411:•  j.  ar»Ja-  i )  Adj.  'wertvoll' :  ms  U  (haomä) nire  *z7me  paiti  Ha  ra^'ants  'jahe  \.io. 17.         2)  m.  'Wert'  (nur  Abieil.)
20168:KompE.  —  Zum  ai.  V.  mämkaU  'er  gibt hin'(?).  —  Eig.  'was  man  drauf  gibt';  Gdn. Stud.  /.  95.  —  Pa.:  masäk.  —  1)  Nicht  'Wert' übeibaupt;  das  ist  arijah-,
21799:•  j.  'yöiäta-  Adj.  'der  jUngste':  yS  aläi hnjyqstimB  (sd.)  hvSiitü  vä  'US  ifii) ".,  gleichviel  ob  es  der  älteste  oder  jüngste ist"  N.j;  —  'tS  %waxsitä  kvBistS  (sd.) *paiti!a%rai  F.  4  t.  a)  'der  geringste' an  Rang  und  Wert'';  pas^id  *g?r3hd  'take "das  Junge  von  einem  Stück  geringsten Kleinviehs"  A,^.  3.
30402:Wert':  yS  .  .  upairi  'r>m  manS  barät  .  .  ■""»«""«  dat>rän?m  Hfmca  manB  hOx/fmca yat  hl  *man3  ^ahe  patti  bar3i  . .  yät  hl  ^"'"'^  hvaHt«nca  lyao-htam  Vr.  2.  5;  usw.; *mafas*aht\paiü-\  ava  barait'e  pascaäa . .  "  ™  Gegensatz  zu  äumaia-.  yupa  'ta "wer  seinen  Sinn  höher  als  seinen  Wert  ■  ■  .'*»^«  ■ ;  ^'"'"'«  b<foB.varsta,  vlspa trägt«,  ..;  wenn  er  aber  seinen  Sinn  ihm  y"^"^«  ■■ 'i^'^'' -■ '^"^''"''^  «*'-' '*'«'^-- entsprechend  trägt,  . .  und  wenn  er  seinen  1  ^f  ^''t^^  :?"  '="*"'■  .  ^]  ""  ,!'°S-  ""'' Sinn  darunter  trägt,  dann  ,.  P.jjf.  Plur.  Name  des  ersten  der  drei  Vorräume
```


## [2026-09-04T19:38:09.186Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport bisect\n# map line numbers to leaves\noff=0\nstarts=[]\nfor p in pages:\n    starts.append(off)\n    off+=p.count('\\n')+1\nfor ln in (5393,5411,5412,6548,10608):\n    i=bisect.bisect_right(starts,ln-1)-1\n    print('line',ln,'-> leaf',i)\n# print head of leaves\nfor i in (95,96,97,110,111):\n    pass\nEOF\necho \"=== leaf around 5393\""
}
```


## [2026-09-04T19:38:10.307Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"varcas\\|várcas\\|vdrcas\" POK_full.txt IEC.txt WLD_band3.txt 2>/dev/null | head -20"
}
```


### [2026-09-04T19:38:10.810Z] TOOL RESULT

```
line 5393 -> leaf 134
line 5411 -> leaf 135
line 5412 -> leaf 135
line 6548 -> leaf 172
line 10608 -> leaf 308
=== leaf around 5393
```


### [2026-09-04T19:38:10.850Z] TOOL RESULT

```
IEC.txt:19959:uelk- “pull, tug, jerk’. Cf. suelk-. WP I, 306 Skt. ambig. várcas, n. (1) “energy”; beside val- kah, am. s. ‘bark of tree, scale of fish’; Gk. ambig. hélko, fut: helküso, v. “pull, drag"; Ir. cf. feilc, pl. -eanna, s. ‘tremor’; OCS and com. Sl. vléko, vléSti, v. “pull, drag, draw’; Cz. cf. also viek, m. “pulP; vlecka, f. dim. ‘train of skirt, trai; Li. velkü, vilkti, v. as SL; zero- gde in vilkiu, vilketi, v. tr. ‘wear — clothes’; cf. also velke, f. ‘pulling strap, bolt’; velkamas, adj. towing-'; Latv. velku, vilkt, v. “pull, drag, téar'; velce, f. *drag-hook'. Extn. in velkme, f. *draught
```


## [2026-09-04T19:38:42.565Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^alum\\|^alumen\\|^alumin\\|^ale,\\|^ale \\|^emblic\" KLN_1966.txt | head -20"
}
```


### [2026-09-04T19:38:42.620Z] TOOL RESULT

```
2145:ale,  n.  —  OE.  ealo,  alo,  rel.  to  ON.  67,  and  cogn. with  L.  alumen,  ‘alum’,  fr.  I.-E.  base  *alu-, ‘bitter’.  OPruss.  alu,  ‘mead’,  Lith.  aids,  OSlav, old,  ‘beer’,  are  Teut.  loan  words.  Cp.  alum, alumina,  aluta,  alutaceous. aleatory,  adj.,  depending  on  chance.  L.  dlea- tdrius,  ‘pertaining  to  a  gamester’,  fr.  alea,  ‘die, game  of  hazard’,  prob.  meaning  orig.  ‘mere chance',  and  derived  fr.  Gk.  iXsoq,  a  collateral form  of  vjXeo^,  ‘wandering  in  mind,  distraught, foolish’.  See  Aleochara  and  the  adj.  suffixes  -ate and  -ory.
2333:alumnus
2374:alum,  n.  —  OF.  alum  (whence  F.  alun),  fr.  L. alumen,  ‘alum’,  lit.  ‘bitter  salt’,  cogn.  with  Gk. aXuSoLjiot;,  ‘bitter’,  OE.  ealo,  alo,  ‘ale’,  ON. 61,  of  s.m.  See  ale  and  cp.  alumina,  aluta,  alu- taceous.
2376:alumen,  gen.  aluminis.  See  alum, aluminite,  n.,  a  hydrous  aluminum  sulfate  (mi¬ neral.)  —  Formed  with  subst.  suff.  -ite  fr. aluminum.
2377:aluminium,  n.  —  The  same  as  aluminum  (q.v.) alumino-,  before  a  vowel  alumin-,  combining  form for  aluminum.
2378:aluminum,  also  aluminium,  n.  —  ModL.,  coined by  the  English  chemist  Sir  Humphrey  Davy (1778-1829)  fr.  L.  alumen,  ‘alum’.  He  gave  the new  element  the  name  aluminum,  but  changed it  later  to  aluminium.  See  alum  and  cp.  the second  element  in  duralumin, alumnus,  n.,  pupil;  graduate  of  a  college  or  uni-
```


## [2026-09-04T19:38:43.300Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[41][:60])\np=pages[41]\ni=p.find('alu')\nprint(p[:4000])\nEOF"
}
```


### [2026-09-04T19:38:45.083Z] TOOL RESULT

```
 Grube'^ Xdrta&og  ;,Sauerampfer^  als  ßoTdvrj  'AevcuTtArf
 Grube'^ Xdrta&og  ;,Sauerampfer^  als  ßoTdvrj  'AevcuTtArf  in  der  Bedeutungsfärbung (^ausleeren,  eingefallen^)  doch  erheblich  ab.  Ganz  fragwürdig  auch  alb. (Jokl  SBAk.  Wien  168^  I  48)  laps  ^bin  müde,  überdrüssig^
Ob  hierher  hett.  al-pa-an-da-  (alpant-)  ^krank,  schwach'^?
WP.  I  92,  Couvreur  H  106 f.,  WH.  I  786,  Hirt  Idg.  Gv.  11,  158.
älu-,  älo-  ^bittere  Pflanze?^
Ai.  ähl-Ij,  älukdm-  ^hulbus,  radix  globosa  esculenta^;  lat.  äliim^  älium Jvnoblauch^,  osk.  *allö  aus  *aUä  wohl  als  Grundlage  von  gr.  dXXäq  ,Wurst^; lat.  älum  oder  alus  ^Symphytum  officinale  L.,  Beinwell,  Wallwurz^  eine  um ihrer  Wurzel  willen  geschätzte  Pflanze  (vielleicht  gall.  Wort?  s.  Thesaurus).
WP.  I  90  f.,  WH.  I  30,  33.  Wohl  zum  Folgenden.
alu-  (-d-,  -t')  ,bitter,  Bier,  Alaun^
Gr.  dXvd(p)ip,ov'  Ttiv.QÖv  Ttagä  2(b(pQ0vi  Hes,,  aXuöf-ialveiv'  [TtiycQaivsLv?] lies.  (s.  aber  zur  Bed.  Herwerden  Lex.  Graec.  suppl.  45);  lat.  alüta ,Alaunleder^  und  alämen  ,Alaun^  sind  einfach  Erweiterungen  von  *alii-. Die  Wurzel  erscheint  in  Nordeuropa  mit  der  Bedeutung  ,Bier,  Met' (zu  der  Bedeutungsdifferenz  vergleiche  ksl.  kvas^  , Alaun,  Bier^);  an.  gl n.  ,Bier,   Trinkgelage^,   gldi-   n.    .Trinkgelage'    (*alupra-),    ags.   ealu(d)  n.
3
34
f
,Bier',  as.  in    alo-fat,  mlid.   in   al-schaf  /rrinkg-efäß';  daraus  entlehnt  api alu    n.    ;,Met^,    lit.    alvs    (m.    geworden    wie    medfis  =  preuß.    meddo   n.;1 J.  Schmidt  Pluralbild.   180),  ksl.  oh   (m.  geworden  wie  medi,)  ß'ier'.   Aus' dem  Germ,  ist  auch  iinn.  olnt  ,Bier^  entlehnt. WP.  I  91,  WH.  I  34.
amhhi,   mbhi  ,um-herum,   zu    beiden    Seiten^,  auch   amhhö{u)   Du.  ,beide und  ähnliche  auf  -hhl,  -hho-  ausgehende  Formen. Arm.  amlolj   ^vollständig,   unversehrt^   (zu    oij  .gesund^),   gr.  ^iicpi  ,um' (cc(.i(pl-g  ,zu  beiden  Seiten',  mit  demselben  Adverbial-s  wie  z.  B.  ^'i//,  )uy,oi- cpig,  s.  Brugmann    Grdr.  IP  2,  737);   lat.  amh-   (vor  Vokal,  z.  B.  amhigö), am-,  an-  (vor  Kons.,  z.  B.  amputö,  amiciö  aus  *aw[6i]yacio)    untrennbares Präfix  ,herum,  um,  ringsum*^,  alat.  auch  Präp.  am  ,circum^  m.  Akk.  (ambi- im  Sinne  von  ,beide^,  den  auch   anceps  zeigt,   ist   dagegen   späte  Bildung zu  amhö),  umbr.  amh-  (amholtu),  a-  (ci-ferum  ,circumferre^),  an-  {an-ferener ,circumferendi^),   osk.    amvianniid   ,circuitu,    Umweg^,    amnüd   ,circuitu, causä^  (kaum  *-amh-heno-  :  venia,   sondern  720-Ableitung,   s.  v.  Planta  II  32, 623);    mit    -e7'-Erweiterung    nach   j9?'ae^e?--eö,    intereö   (s.  v.  Planta  II  455, WH.  I  36),  umbr.  ampretu,  ambretnto  ,ambito,  ambiunto^,  vielleicht  auch  i! osk.  amfret   ,ambiunt^   (eher  nach    Schulze   KZ.  45,  182=  Kl.  Sehr.  468  ^ in  *am-ferent  ,circumferurit,  TtSQiayovOi'  zu  zerlegen;    keine   lat.  Spur  der gleichen  -er-Erweiterung  in  amfräctiis  , umgebogen^,  das  vielmehr  aus  am- fräctus)-  über  den  ON  Amiiernum  s.
```


## [2026-09-04T19:38:56.351Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"emblic\\|amlaj\\|myrobalan\" KLN_1966.txt | head -20; echo \"=== 1971\"; grep -n -i \"emblic\" KLN_1971.txt | head"
}
```


### [2026-09-04T19:38:56.414Z] TOOL RESULT

```
4307:Derivatives:  balance,  tr.  v.,  balanc-ed,  adj., balanc-er,  n.,  balanc-ing,  adj. balaniferous,  adj.,  acom-bearing.  —  Compound¬ ed  of  L.  balanus,  ‘acorn’,  and  L .ferre,  ‘to  bear, carry’.  See  balano-  and  -ferous. balano-,  before  a  vowel  balan-,  combining  form meaning  ‘acorn’.  —  Gk.  (JaXavo-,  (3aXav-,  fr. (3aXavo;,  ‘acorn’,  which  is  cogn.  with  L.  gldns, gen.  glandis,  ‘acorn’.  See  gland  and  cp.  the second  element  in  myrobalan. balanoid,  adj.,  acorn-shaped. —  Compounded  of balan-  and  Gk.  -osiSt^,  ‘like’,  fr.  elSop,  ‘form, shape’.  See  -oid.
12932:ML.  imbladare,ir.  im-  (see  im-,‘in’)  and  blada,'X\ic yield  of  a  land’,  fr.  Frankish  *blad-  (whence  also F.  ble,  ‘wheat,  com’),  which  is  rel.  to  OE.  blxd, ‘flower,  fruit,  harvest’.  See  blade  and  -ment. emblic,  n.,  name  of  an  East  Indian  tree.  —  ML. emblica,  fr.  amleg,  Egyptian  pronunciation  of Arab,  amlaj,  fr.  Pers.  amleh,  ultimately  fr.  OI. dmlak,  whence  also  Malay  malaka,  ‘emblic’, which  latter,  according  to  Malay  tradition,  ap¬ pears  also  in  the  name  of  the  peninsula  Malakka. See  Devic’s  Supplement  to  I.ittre’s  Dictionary. P-33-
16218:Derivatives:  glamo(u)r,  tr.  v.,  g!amo(u)r-ous, adj.,  glamo(u)r-ous-ly,  adv.,  glamo(u)r-y,  adj. glance,  intr.  and  tr.  v.,  to  glide  off  obliquely;  to flash;  to  look  quickly.  —  ME.  glacen,  fr.  OF. glacier,  ‘to  slip,  slide’,  fr.  glace,  ‘ice’ ;  see  glacier. The  word  glance  was  prob.  influenced  both  in form  and  meaning  by  ME.  glenten,  ‘to  shine’ (see  glint).  Cp.  glissade.  Cp.  also  next  word. Derivative:  glance,  n.,  a  gliding  off  obliquely; a  flashing;  a  quick  look, glance,  n.,  a  lustrous  metallic  sulfide  (mineral.)  — Du.  glans,  ‘brightness,  luster’.  See  next  word, glance,  tr.  v.,  to  polish  (metal).  —  Prob.  fr.  Du. glanzen,  ‘to  gleam,  polish’,  fr.  MDu.  glansen, ‘to  gleam’,  fr.  glans,  ‘brightness’,  fr.  MHG.  glanz (whence  G.  Glanz),  fr.  Late  OHG.  glanz,  of  s.m., fr.  OHG.  glanz,  adj.,  ‘bright’,  which  is  rel.  to ME.  glenten,  ‘to  shine’.  See  glint, gland,  n.  —  F.  glande ,  fr.  L.  glandem,  acc.  of glans,  ‘acorn’  (used  in  the  sense  of  L.  glandula, ‘gland’,  dimin.  of  glans),  which  is  cogn.  with Gk.  pdXavog,  Arm.  kaiin  (gen.  kalnoy),  OSlav. zelgdi,  ‘acorn’,  Lith.  gile,  Lett,  (d)zile,  OPruss. gile,  ‘oak;  gland’.  Cp.  next  word  and  the  second element  in  Euglandina  and  in  Juglans.  Cp.  also the  first  element  in  balaniferous  and  the  second element  in  myrobalan.  Cp.  also  valonia. Derivatives :  glandi-ferous,  adj.,  glandi-form,  adj. glanders,  n.  pi.,  a  contagious  disease  of  horses, mules,  etc.,  characterized  by  the  swelling  of  the glands  beneath  the  lower  jaw.  —  OF.  glandres (pi.),  fr.  L.  glandulae  (pi.),  ‘glands  of  the  throat'. See  glandule.
24858:myrobalan,  n.,  the  dried  astringent  fruit  of  vari¬ ous  tropical  trees.  —  F.,  fr.  L.  myrobalanum,  fr. Gk.  ixupoflaXxvov,  ‘balsam  made  from  a  palm nut’,  which  is  compounded  of  p.upov,  ‘sweet juice,  sweet  oil,  unguent,  balsam  ,  and  ,jxXxvgp, ‘acorn,  nut’.  For  the  first  element  see  smear  and cp.  Myristica  and  the  first  element  in  next  word, for  the  second  clement  see  balano-.
35643:smatter,  intr.  v.,  to  talk  with  a  superficial  knowl¬ edge.  —  ME.  smateren,  ‘to  make  a  noise’,  of imitative  origin.  Cp.  Swed.  smattra ,  ‘to  crackle’. Derivatives:  smatter-er,  n.,  smatter-ing,  n.  and adj.,  smatter-ing-ly,  adv.,  smatter-y,  adj. smear,  n.  —  ME.  smere,  fr.  OE.  smeoru,  smeru, ‘fat,  grease’,  rel.  to  OS.,  OHG.  smero,  ON. smjor,  smdr,  Dan.  smer,  Swed.  smor,  MDu. smere,  Du.  smeer,  MHG.  smer,  G.  Schmer, ‘grease,  fat’,  Goth,  smairpr,  ‘fatness’,  fr.  I.-E. *smeru-,  ‘grease’,  whence  also  Gk.  piupov,  ‘un¬ guent,  balsam’,  ptupt^av,  opL'jpi^Etv,  ‘to  rub  with ointment’  (but  not  crpujpu;,  ‘emery’,  see  emery), Toch.  B.  $mare,  ‘smooth’,  OIr.  smi(u)r,  ‘mar¬ row’,  W.  mer,  of  s.m.,  and  perh.  also  Lith. smdrsas,  ‘fat’.  Cp.  Myristica,  Amyris,  and  the first  element  in  myrobalan,  Myroxylon.  Cp.  also medulla.
38661:Terminalia,  n.  pi.,  an  ancient  Roman  festival  held on  the  23rd  of  February  (Roman  antiq.)  —  L., lit.  ‘festival  in  honor  of  Terminus,  ‘god  of  the boundaries’,  fr.  Terminus.  See  Terminus. Terminalia,  n.,  a  genus  of  plants  of  the  myrobalan family  (bot.)  —  ModL.,  fr.  L.  terminalis,  ‘per¬ taining  to  the  end’  (see  terminal  and  1st  -ia  and cp.  prec.  word);  so  called  from  the  leaves  at  the end  of  the  branches.
=== 1971
80689:EMBLIC 
80992:emblic, n., name of an East Indian tree. — ML. 
80993:emblica , fr. dmleg, Egyptian pronunciation of 
81007:amlak, whence also Malay malaka , ‘emblic\
```


## [2026-09-04T19:38:58.073Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport bisect\noff=0; starts=[]\nfor p in pages:\n    starts.append(off); off+=p.count('\\n')+1\nfor ln in (2145,2374,2376,2377,2378):\n    i=bisect.bisect_right(starts,ln-1)-1\n    print('line',ln,'leaf',i)\nEOF"
}
```


### [2026-09-04T19:38:59.855Z] TOOL RESULT

```
line 2145 leaf 35
line 2374 leaf 41
line 2376 leaf 41
line 2377 leaf 41
line 2378 leaf 41
```


## [2026-09-04T19:39:13.152Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport bisect\noff=0; starts=[]\nfor p in pages:\n    starts.append(off); off+=p.count('\\n')+1\nfor ln in (12932,):\n    i=bisect.bisect_right(starts,ln-1)-1\n    print('line',ln,'leaf',i)\n    print(pages[i][:300])\nprint('--- leaf35 head'); print(pages[35][:200])\nprint('--- leaf41 head'); print(pages[41][:200])\nEOF"
}
```


## [2026-09-04T19:39:14.021Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'آمله' in p or 'آملج' in p:\n        print('leaf',i,'~printed',i-210)\nEOF"
}
```


### [2026-09-04T19:39:14.838Z] TOOL RESULT

```
line 12932 leaf 273
he  ending  see  subst.  suff.  -ite.
Edentata,  n.  pi.,  a  group  of  placental  mammals including  the  armadillo,  sloth,  anteater,  etc. (zoo!.)  —  ModL.,  neut.  pi.  of  L.  edentatus, ‘toothless’,  pp.  of  edentare,  ‘to  render  tooth¬ less’,  fr.  e-  and  dens,  gen.  dentis,  ‘tooth’
--- leaf35 head
,  n.,  son  of  Neleus  and  brother  of  Nestor in  Greek  mythology;  fig.  used  in  the  sense  of  an avenging  spirit.  —  Gk.  ’  AXacrrap,  lit .  ‘wanderer’, a  derivative  of  dXao&ai,  ‘to
--- leaf41 head
r.  L.  admorsus,  pp.  of  admordere, ‘to  bite  into’,  fr.  ad-  and  mordere,  ‘to  bite’.  See mordant.
aimng,  also  algum,  n.,  a  tree  mentioned  in  the
Bible,  prob.  the  sandalwood  (the
```


### [2026-09-04T19:39:16.816Z] TOOL RESULT

```
leaves 777
leaf 271 ~printed 61
leaf 380 ~printed 170
```


## [2026-09-04T19:39:27.354Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(266,278):\n    nums=re.findall(r'(?m)^\\s*(\\d{3})\\s*$',pages[i])\n    nums2=re.findall(r'\\b(5[01]\\d)\\b',pages[i])\n    first=pages[i].strip().split('\\n')[0][:50]\n    print(i,nums,nums2[:6],'|',first)\nEOF"
}
```


### [2026-09-04T19:39:31.400Z] TOOL RESULT

```
266 ['487'] [] | the  stem  of  L.  dux,  gen.  duds, ‘leader’.  Se
267 ['488', '489', '490', '491'] [] | re  referred  to.
268 [] [] | icatid,  ‘a  doubling’,  fr.  duplicatus,  pp.  of
269 [] [] | for  measuring  the magnifying  power  of  telesco
270 ['497'] [] | ,  fr.  OE.  earnian, ‘to  deserve,  earn’,  rel. 
271 [] [] | fr.  L. eburneus,  ‘of  ivory’,  fr.  ebur,  ‘ivor
272 [] [] | deals  with  animals  and  plants  in  relation  t
273 ['501', '502', '503'] ['501', '502', '503'] | he  ending  see  subst.  suff.  -ite.
274 ['504', '505'] ['504', '505'] | ?,  ‘an  absolute  master  or  ruler’.  See
275 [] [] | h. A  ok  at,  B  okt.  Arm.  ut‘  (for  *optd ), 
276 ['506', '507'] ['506', '507'] | ��uplifted,  ex¬ alted’  (used  as  pp.  of  effer
277 ['508'] ['508'] | h’,  and  yapi?, ‘grace,  delight’.  The  first  e
```


## [2026-09-04T19:39:38.895Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '80660,80700p' KLN_1971.txt; echo \"...\"; sed -n '80980,81015p' KLN_1971.txt"
}
```


### [2026-09-04T19:39:38.973Z] TOOL RESULT

```
Derivative: elope-ment , n. 
elops, n., 1) formerly, a sea fish; 2) {cap.) a genus 
of fishes, the chiro {ichthyol.) — ModL., fr. Gk. 
£Xo^, a var. of gXXotp. See ellops. 
eloquence, n. — F. Eloquence, fr. L. eloquentia , 
‘eloquence’, fr. eloquins, gen. -entis. See next 
word and -ce. 

eloquent, adj., fluent, forceful. — F. eloquent, fr. 
L. eloquentem, acc. of eloquins, pres, part of 
iloqui, ‘to speak out, pronounce’, fr. e- and 
loqui, ‘to speak’. See loquacious and -ent and cp. 
elocution. 

Derivatives: eloquent-ly, adv., eloquent-ness, n. 
Elsa, fem. PN. — G., dimin. of Elisabet , fr. Late 
L. Elisabeth. See Elizabeth, 
else, adj. — ME. elles, fr. OE. elks, neut. gen. 
of adj., used as an adv. in the sense of ‘other- 
wise’, rel. to Goth, aljis , ‘other’, OHG. eli-lenti, 
el-lenti, OS. eli-lendi , OE. el-lende , ‘in a foreign 




243 



EMBLIC 



land’, MHG. ellende , G. elend, ‘unfortunate, 
wretched’, ON. elja, ‘rival’ (fem.), lit. ‘the 
other’, and to the first element in OHG. Eli- 
sti33o (whence G. Elsafi, ‘Alsace’), ‘inhabit- 
ant of the other bank of the Rhine’, and cogn. 
with Toch. A alya-k, B alye-k, ‘somebody else’, 
Gk. &XXoc, (for *<£Xao<;), L. alius. Arm. ail, OIr. aile, 
W., Co. aile, ‘other’. All these words derive fr. 
...
blemat-ic-al, adjs., emblemat-ic-al-ly , adv., em- 
blematic-al-ness, n., emblem-at-ist , n., emblem- 
atize, tr. v. 

emblement, n., usually in the pi.: emblements, 
crop; profits of a crop (law). — OF. emblae - 
ment, emblavement, ‘land sown with wheat’, fr. 
emblaer (F. emblaver ), ‘to sow with wheat’, fr. 
ML. imbladare, fr. im- (see im-,‘in’) and6Wa,‘the 
yield of a land’, fr. Frankish *bldd- (whence also 
F. ble, ‘wheat, com’), which is rel. to OE. bleed \ 
‘flower, fruit, harvest’. See blade and -ment. 
emblic, n., name of an East Indian tree. — ML. 
emblica , fr. dmleg, Egyptian pronunciation of 




EMBODY 



244 



Arab, amlaj, fr. Pers. amleh, ultimately fr. OI. 
amlak, whence also Malay malaka , ‘emblic\ 
which latter, according to Malay tradition, ap- 
pears also in the name of the peninsula Malakka. 
See Devic’s Supplement to Littre’s Dictionary. 
P.33. 

embody, tr. and intr. v. — Formed fr. era- and 
body.
```


## [2026-09-04T19:39:55.223Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[271]\nimport re\ni=p.find('آمله')\nprint(p[max(0,i-1500):i+1500])\nEOF"
}
```


### [2026-09-04T19:39:56.881Z] TOOL RESULT

```
آمله ۲ - ینم ثاكك و قح رابغ » دوائی
است کثیرالتفع وممرب آن «آملج» باشد . گویند
دو درم را از آن کوفه تا دوساعت درآب شیرین
بجوشانند و بمد ازآن ساف کنند و سه‌چپارلویت
درچشم چکانند ۰ سفید یرآ که ۳ بود سود
دارد .
]هن - پنتح الك و نون ۰ نود خومن
هیزم شکافنه(۱) را گوبند سوپشته ویشتوار؛ هیزم
ببتهرا ن رگفته‌اند - و بکسرالث یام مادرحصرت
رمالت یناه علیه السلام است .
آمو . نم تالث و سکون واو , مضفف
آمون‌است وآن رودخانه‌ای باشدمشهور وممروف.
واقم در میان ابران وتوران- وبسنی گوبند دهی
است که این رود خانه موسوم بآن ده است ۳
(۱) چش: شکته . . (۲) چك: ژند ویلژند.
وژمینی خم‌هست میان جیحون وفرأت .
] موت - با فوفانی بروزن لاعوت .
آشیان جانوران شکاربرا کوبند حمیویاز وشاهین
]هو یا - بکر فوفانی و تضانی بالف
کشیده , بلفت زد و پازن() کنیزك و پرستا
وخدمتکار (۳) باشد ۴ .
۲ موختگان ادل » اب ر ارب
صلوات اف علیهم اجمعین (4) را کوبند . *#
| مود پروزن تابود » بعنی بر آحیخت
1 بر آراست - و ماخت کرد .
آمودن بروزن آسودن . بمعنی
ارات .- 1 "آراسته خدن و آم‌ختن -
(4)چك : - اجمعین .
منانات دراطامعلار۳ < تیتی دما ؟ ‏ آعو جحون ؛ در
. لهج پارتی وپپلوی (2722(]) ۲12100 وهمچنین درلهجةٌ یکی خلج‌ونیز فرکمنی. رله : مقاله
6 .۱ .3 در پاپ کتاب ,601870۳8۲ مهم‌مودتده ,۱۷۵۵866 . ۲٩‏ . 8۲۱
40 .و4 ۲۵.3 ۰ ۷۵۲۰۱۵ و عع‌نت:5 عتاهني۸ ۵۶ اعصیداهز ۳۱۵۲۵۲۵ عصعل
۴ - برقلهٌ فاف بخت واقبال 7 آموت عقاب دولت شت . منجيك
و الموت را م رکب از آله بممنی عقاب وموت مخطف آموت بمعتی آشیان دادتة اند .
«لفت نامه» رثك : آله . ۴ . حزوارش , قنا۸6 . بیعنی پرستار ۰ نیز 80010048
نوی بدهش ۷۰ . آسوری ۸۳۱۷ < دلیتزش ص ۷۲-۷۷
آموختی - از رشةٌ »3 . در پهلوی 8۳610 « نی ر
```


## [2026-09-04T19:40:06.971Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(300,320):\n    p=pages[i]\n    hits=[w for w in ['ارج','ارزان','ارجاسب','ارزیدن','ارزش'] if w in p]\n    print(i,'~printed',i-210,hits)\nEOF"
}
```


### [2026-09-04T19:40:08.857Z] TOOL RESULT

```
300 ~printed 90 []
301 ~printed 91 []
302 ~printed 92 []
303 ~printed 93 ['ارزش']
304 ~printed 94 []
305 ~printed 95 []
306 ~printed 96 []
307 ~printed 97 ['ارج']
308 ~printed 98 ['ارج']
309 ~printed 99 []
310 ~printed 100 []
311 ~printed 101 []
312 ~printed 102 ['ارج', 'ارزان', 'ارزش']
313 ~printed 103 []
314 ~printed 104 []
315 ~printed 105 ['ارج']
316 ~printed 106 []
317 ~printed 107 []
318 ~printed 108 []
319 ~printed 109 ['ارج']
```


## [2026-09-04T19:40:13.224Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (307,308,312):\n    print('===== leaf',i,'printed ~',i-210)\n    print(pages[i][:2600])\nEOF"
}
```


### [2026-09-04T19:40:14.739Z] TOOL RESULT

```
===== leaf 307 printed ~ 97
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
===== leaf 308 printed ~ 98
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
===== leaf 312 printed ~ 102
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
```


## [2026-09-04T19:40:42.030Z] TOOL CALL #37: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nprint(json.dumps(d['BQT']['scans'],ensure_ascii=False,indent=1))\nprint(d['BQT']['page_offset'])\n\""
}
```


### [2026-09-04T19:40:43.728Z] TOOL RESULT

```
[
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
]
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
```


## [2026-09-04T19:40:48.884Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor p in pages:\n    if '[pdf page 348]' in p[:60] or '[pdf page 349]' in p[:60]:\n        print(p[:3000])\n        print('#########')\nEOF"
}
```


### [2026-09-04T19:40:50.740Z] TOOL RESULT

```
553
[pdf page 348]
تفه ورج
وآقتاب پرست باشد۱ » وبستی کویند کلی است ور آیج؟ (۱) - بروزن تدریج, پردد
سرخ رنگه ۴ . چون آفتاب بسمت رای رسد | ایست شبیه به تیپو ولیکن ازتیه و کوچکتر است
بشکفد وآنر| خبازی ونان کلاغ خوانند. ویسی | و آلرا بعربی سلوی و سمانی 9 و بفارسی کر
دیگر کوبند کیاهی‌است که پیوسته درآب‌میباشد | و بترکی بلدرچین گوبند - و بمعنی آستان در
وبهرطرف که آقتاب کردد بر کهای‌آنهم‌میگردد | خانه۹ هم بنظرآمده امت .
- وکل یلوفررا نیز کفته اند۴ ‎ -‏ وکلی‌هم‌هت ورج - بفتح اول وسکون ثالی وجیم »
که آبراکل آفتاب پرست میگوبند .# بممنی قدرومرتبه وبزرگی وشأُن وشوکت باشد۷
(نه چش : ورتیخ
۱ - زیرا که همیشه روی بآفتاب دارد « رشیدی ».
۴ - بعض افام‌آن سرخ رنگه است :
تو تاجور ملك شرف بادی وامدات برآتش غم سوخته باشند چو ورتاج-
سوزلی سمرقندی « رشیدی » « فرهنکه نظام».
۴ - رك : پثیرك . این بیت منصور شیرازی را شاهدآورده‌اند :
شکفت در چمن آسمان به رگوشه هزار لاله سیراب و غنچهٌ غناج
کشاده دیدة بینا ستاره چون‌ا ر کی درآب‌رفته کل‌آفتاب چون ورتاج. «رشیدی».
۴ ورتج « صعاح‌الفری» « فرهنکه نظام > وردیج (ه.م.) * ورده ( رگ : وردیج).
« ورتیج » سمانه باشد . زینبی گوید :
آید از باغ بی سرود و بازیج دستك بکراغه می‌برآرد ورتیج (۱)»
« لت فری س ‎۰۹۸-٩۷‏
‏این بیت بنام لبیبی در صحاح‌الفری چنین‌آهده :
از باغ بی سرود بازیج رشك گواعه می‌برآرد ورتیج . (یادداشت آقای طامتی).
8 - رك : سمانه , سمانی. - این اشتباه ازآنجا ناشی شد ه که درمعنی«ورتیج»
: *سمانه» نوشته‌اند » وسمانه را «ستانه » (ه.م.) [ * آستاه ] خوانده‌اند ۱
۷ «ارج (ه.م ) * فرج (ه.م.) ؛ درپهلوی ۰۷۵۳6 دراوستا- ۰۷8۲90810 درماسکریت
5 مبمعنی لیروی حیانی و قوت . و غ۷2۳30811۷8 در اوستا صفت است به‌عنی دیرومشد
و قوی « بارتولمه ۱۳۹۷ *گاه در ادبیات پارسی بجای «فر» (ه.م ) و «خوره» (۸م ) كلمة «ورج»
را بهمان مفهوم بکار برده‌اند. مولف فرائداللوك (که مماسرانايك ازيك من جهان پپلوان[ ۹*۰۷-
بقیه در حاشیةٌ صفحه بمد
ورلج - رك : ورتیج :
دل ز عشفت سحر مطلق میکند همچو ورتج حق بلقلق میکند .
آنوری آبیوردی « صحاح‌الفری » ( پادداشت آقای طاعتی ).
بیه از حاشیة مفحهٌ قبل :
که‌آفتا ب کردد اولیز آن سوکردد . وروی درآفتاب دارد » ودرعراق وخولستان آلرا تولهخوانند.
وآفتاب پرست دی زکوبند » منجيك گفت :
مثال بنده وآن تو جانا | چو فرص آفتاب وی رکه ورتاج .> « طاعتی >
ر4 : پثیرك.

#########
[pdf page 349]
ات ی نها
-وبمعنی کندن وبر کندن - وبممنی سخت هم ٍ است - وبکراول وفتح نانی» دام کیاهی اس ت که
هت که دربرابرست است» وبکراول هم‌آهده | آارا اکرتر کی‌خوانند؟ *.
۱ - جپانگیری این بیت ابواصر احمد رافمی را برای این معتی شاهدآورده :
سرافرازان دولت را بفر ایزدی یاور ستمکاران ملت را پورج حیدری قاهر.
ولی شك نیست که همان معنی اول است ( رك : ح۷ صفحهٌ قبل) ؛ اما «ارج» بمعنی کندن آمده
و رشیدی برای‌آن شاهدی ازسوزنی آورده است » وتبدبل «۱» به «و» در فارسی متداول است.
۳۲ - باین هعنی مصحف «وج» (و.م.) است . ر4 : اگر.
بفیه از حاشیة صفحةٌ قبل
۷ بوده.) نود ( دخهةٌ خطی متملق بکتابغانٌ ملی ملك ) : « و طایقه‌ای را از بندگان
بمنایت لطف اختیار فرمود (حق تعالی ) و بسعادت عقل ممتاز کرد . و ابشان را بفرالهی بیاراست
و به ورج پادشاهی ( ۳ فرکیانی) مزین کردانید . پس بانبیاه مرسل که ممتاز خلایق بودند وحی
فرستاد بتوسط ماشکه »و آن پیغام آسمت بین دکان خوش » و بملوك عادل ورج داد ۰ و آن فری
آمت آلهی و نوری است ربانی که از اشمة عالم غیب فیضان کند » وفروغی اس ت که از پرتو لوایح
ایزدی لمعان زند و درسينةٌ لوك مقام سازد و ازسینه برجبین سرابت کند ».تا بقوت فیض آن بر
عالمیان مهترشود و بمدد تابش آن بر جهالیان غلبه کیرد ...> ابن‌سینا در دانشنامةٌ علای ( بخش
آلهی . مصحح نگارنده چاپ انجمنآثار ملی ۱۳۳۱ ص ۱*۹ - ۱۱۶ ) کوید : 3 ... و ابشان را
( ممقولات را ) بخوشی ولذت برسو مشغولی است , زبراکه هرکز روی از برسو بفروسونکنند,
وخودی خویش را وقف کرده‌اند بر نظارة ورج » بعنی شکوهمندی برین و بریافت خوشی‌مهین.>
سعدالدین وراوینی‌در مرزبان نامه ( چاپ دوم تهران ص ۱۹ ) آرد: « نداش د که پادشاهان برکزیدة
آفرید کار و پروردةٌ پرورد گاراند » و آنجا که مواهب ازلی قسمت کردند [ و ] ولابت ورج الهی
(< فرایزدی) بغرج رفت . اول همای سلطنت سایه بر پیغامبراث افکند , پس برپادشاهان ؛ پس
بر مردم دالا ...* فردوسی در داهنامه کویو :
ز مهرش جهان را بود ورج وف زخشمش بجوشد بتن در جگر ...
نه تنهاشه و خسرو کشورست که شاه است وبا ورج پیذمبراست.
ملك چون ورا دید با ورج وف که‌آبرا نه اندازه بود وثه هر....
ابن‌البلغی کوبد ( فارسنامه چاپ اروپا ص ۳۷ ) : « جمشید کفت برسبیل خطبه که ایزد تعالی
ورج و بهاه ما تمام گردانید وتأبید ارزانی داغت .> زرتشت بهرام پژدو درداردا وبرافنامه»گوید :
زشاهان فر وخره,جم‌فزون داشت . بهرکاری‌خرد را رهنمون داشت.
ز لور مینوانی باقت بهره زفر وورج شد چون‌شیدشهره.
رل : حکمت اشراق بقلم نگارنده س ۲۹-۲۸ ؛ دانشتامةٌ علائی » الهی ( مصحح نگارنده ) ص
۱۱۳-۹ (حاشیه) . ورك : ورج بقلم نگارنده . پاچ : ۱ ۰۳۰-۲۸
«ورجمند» (ه.م.) از ورج بهمین همنی ترکیب پافته .
« ورجاوند > (۸.م.) نیز ا زكلمهٌ «ورج» مر کب است . ر4 : ورج بقلم نگارنده . مجلةٌ
بغما ۱:۳ص ۰۳-۲۸ وآن عنوان یکی از موعودان زرتشتی امت.
1 : بقیةٌ حاشیه درصقحةٌ مد
(برهای قاطع ۳۸۹)

#########
```


## [2026-09-04T19:41:16.169Z] TOOL CALL #39: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-04T19:41:16.176Z] TOOL RESULT

```


```


## [2026-09-04T19:41:18.591Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON && for f in MON_2vol_Adena_v1_djvu.txt MON_2vol_Adena_v2_djvu.txt; do echo \"=== $f\"; grep -n \"ارجاسب\\|ارجاسپ\" $f | head -5; done; echo \"=== part1/2\"; cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" MON_part1.txt MON_part2.txt; grep -n \"ارجاسب\\|ارجاسپ\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-04T19:41:20.286Z] TOOL RESULT

```
=== MON_2vol_Adena_v1_djvu.txt
=== MON_2vol_Adena_v2_djvu.txt
=== part1/2
MON_part2.txt:94500
MON_part1.txt:99339
```


## [2026-09-04T19:41:24.814Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 800 MON_part1.txt; echo; echo \"=== grep arj\"; grep -n \"ارج\" MON_part1.txt | head -5; echo \"=== amleh\"; grep -n \"آمله\\|آملج\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -8"
}
```


### [2026-09-04T19:41:24.914Z] TOOL RESULT

```
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
و ده ها وی مزا موی ماما میو و موه ومد موه اش اما موم م میا شا ولمم 


معین, محمد» ۱۳۵۰۰۱۲۹۱ 
فرهنگ معین / محمد معین. -- تهران: آدنا: کتا�
=== grep arj
190:در مهر ماه ۷ به عنوان راستاد ممتحن خارجی» دانشگاه بنجاب 
1407:شسته شدن آن. خارج شدن منی» جاری 
1734:خارج سازند. 
4015:وسط شکسته و بصورت زاویه بسوی خارج 
4338:قبفت خارجی عضو ساسی زن؛ فرج) 
=== amleh
```


## [2026-09-04T19:41:35.579Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%AC",
 "prompt": "Give the full Persian entry: etymology of ارج (arj), including Middle Persian and Avestan/Proto-Iranian ancestors and any cited sources. Also any Persian ارز/ارزان mentioned."
}
```


## [2026-09-04T19:41:36.698Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%88%D8%B1%D8%AC",
 "prompt": "Give the full Persian entry for ورج (varj): etymology, meaning, Middle Persian and Avestan ancestors, cited sources."
}
```


### [2026-09-04T19:41:39.392Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T19:41:40.203Z] TOOL RESULT

```
I cannot provide the requested information based on the webpage content supplied. The page shown is from English Wiktionary and contains only a brief Arabic entry for **اُرْجُ** (urju), identified as the "second-person masculine singular imperative" form of the verb **رَجَا** (rajā).

The page does not include:
- A Persian entry for ارج
- Etymology information for Persian ارج
- Middle Persian or Avestan/Proto-Iranian ancestors
- Any sources cited for historical linguistic information
- References to ارز/ارزان

To obtain comprehensive Persian etymological information, you would need to consult the Persian Wiktionary (fa.wiktionary.org) or specialized etymological dictionaries covering Persian and Indo-European languages.
```


## [2026-09-04T19:41:44.429Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%B2%D8%A7%D9%86",
 "prompt": "Full Persian entry for ارزان: etymology (Middle Persian, Avestan, Proto-Iranian, PIE root), meanings, and cited references."
}
```


## [2026-09-04T19:41:45.099Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hardzah",
 "prompt": "Does this page exist? If so give the reconstruction, meaning, PIE root, and descendants."
}
```


### [2026-09-04T19:41:49.468Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T19:41:50.909Z] TOOL RESULT

```
# Word Entry: ارزان (arzān)

## Primary Meaning
The Persian adjective **ارزان** means "cheap" or "inexpensive," with the antonym being گران (gerân, "expensive").

## Etymology
This word has deep linguistic roots. It derives "from [Middle Persian] (ʾlcʾn /⁠arzān⁠/), meaning 'valuable, worthy'" and traces back through Proto-Iranian and Proto-Indo-Iranian origins. The term is cognate with related words in Parthian, Talysh, and Northern Kurdish, as well as borrowings in Old Armenian and Classical Syriac.

## Linguistic Reach
The word has spread across numerous languages as a descendant from Persian, including Pashto, Baluchi, Khalaj, Hindustani (Hindi/Urdu), Kyrgyz, Kazakh, Uyghur, and Uzbek variants. This demonstrates the significant historical influence of Persian vocabulary across Central and South Asian languages.

## Usage Example
A classical citation appears in Rumi's *Masnavi* (c. 1260): the phrase describes someone who "sold himself for **cheap**" despite their inherent worth.
```


## [2026-09-04T19:41:55.942Z] TOOL CALL #46: Bash

```json
{
 "command": "for w in \"%D8%A7%D8%B1%D8%B2%D8%A7%D9%86\" \"%D8%A7%D8%B1%D8%AC%D9%85%D9%86%D8%AF\" \"%D8%A7%D8%B1%D8%B2%DB%8C%D8%AF%D9%86\"; do echo \"=========== $w\"; curl -s \"https://en.wiktionary.org/w/index.php?title=$w&action=raw\" | head -60; done"
}
```


### [2026-09-04T19:41:59.405Z] TOOL RESULT

```
=========== %D8%A7%D8%B1%D8%B2%D8%A7%D9%86
{{also|ارزاں}}
==Baluchi==

===Adjective===
{{head|bal|adjective|tr=arzán}}

# [[cheap]]
# [[inexpensive]]

==Gawar-Bati==

===Etymology===
{{bor+|gwt|ps|ارزان}}, {{der|gwt|fa|ارزان}}. 

===Adjective===
{{head|gwt|adjective|g=|tr=arzān}}

# [[cheap]], [[inexpensive]]
# [[worthless]], [[insignificant]]

==Khalaj==

===Adjective===
{{head|klj|adjective|head=اَرزان|tr=arzân ''or'' ərzân}}

# {{spelling of|klj|Arabic|[[arzân]], [[ərzân]]|t=[[cheap]]}}

==Pashto==

===Etymology===
{{etymon|ps|id=cheap|:bor|fa-cls:اَرْزَان<id:cheap>}}
{{bor+|ps|fa-cls|اَرْزَان||cheap}}.

===Pronunciation===
* {{IPA|ps|/ar.zɑn/|[äɾ.zɑ́n]}}

===Adjective===
{{ps-adj|tr=arzān}}

# [[cheap]]

====Declension====
{{ps-decl-adj-m-consonant|ارزان|arzān}}

====See also====
* {{l|ps|ارزانه|tr=arzāna}}

==Persian==

===Etymology===
{{etymon|fa|id=cheap|:der|iir-pro:*Hárǰʰati<id:be worth>}}
From {{inh|fa|pal|tr=ʾlcʾn|ts=arzān|sc=Phlv}}, {{m|pal|𐫀𐫡𐫉𐫀𐫗|t=valuable, worthy|ts=arzān}}, from {{m|pal|tr=ʾlc|ts=arz|t=worth, value|sc=Phlv}} + {{m|pal|tr=-ʾn|ts=-ān|sc=Phlv}}, from {{der|fa|ira-pro|*Hárǰ-}}, from {{der|fa|iir-pro|[[*Hárǰʰati|*Hárǰʰ-]]|t=to be worth}}. Cognate with {{cog|xpr|𐫀𐫡𐫋𐫀𐫗|t=worthy|ts=aržān}}, {{cog|tly|ارژون|tr=erjon}}, {{cog|kmr|erzan}} and the following Iranian borrowings: {{cog|xcl|արժան||worthy; cheap}}, {{cog|syc|ܐܪܙܢ|tr=ʾarzān|t=cheap}}.

===Pronunciation===
{{fa-IPA|ar`zān}}
* {{audio|fa|LL-Q9168 (fas)-Afsham23-ارزان.wav|a=Iran}}

===Adjective===
{{fa-regional|ارزان|ارزان|арзон}}
{{fa-adj|tr=arzân|c=+}}
=========== %D8%A7%D8%B1%D8%AC%D9%85%D9%86%D8%AF
==Persian==

===Etymology===
Related to {{m|fa|ارزیدن|tr=arzidan|t=to cost, be of value}}. Ultimately from {{cog|ine-pro|*h₂elgʷʰ-||to cost, have value}}.{{root|fa|ine-pro|*h₂elgʷʰ-}}

===Pronunciation===
{{fa-IPA|arju`mand}}

===Adjective===
{{fa-regional|ارجمند|ارجمند|арҷуманд}}
{{fa-adj|tr=arjomand|c=+}}

# [[precious]], [[valuable]]
# [[honorable]], [[venerable]], [[esteemed]]
#* {{RQ:fa:Masnavi|I|3472|چینیان صد رنگ از شه خواستند<br>پس خزینه باز کرد آن '''ارجمند'''|čîniyân sad rang az ša xwastand<br>pas xazîna bâz kard ân '''arjumand'''|The Chinese requested the King to give them a hundred colours:<br>then that '''excellent''' (king) opened the treasury.}}

==Urdu==

===Etymology===
From {{bor|ur|fa-cls|ارجمند|tr=arjumand|t=precious, valuable}}

===Adjective===
{{ur-adj|tr=arjmaṉd|hi=अर्जमंद}}

# [[exalted]]=========== %D8%A7%D8%B1%D8%B2%DB%8C%D8%AF%D9%86
==Persian==

===Etymology===
From {{inh|fa|ira-pro|*Hárǰati}}, from {{inh|fa|iir-pro|*Hárǰʰati}}, from {{inh|fa|ine-pro|*h₂elgʷʰ-}}.

===Pronunciation===
{{fa-IPA|arzī`dan}}

===Verb===
{{fa-regional|ارزیدن|ارزیدن|арзидан}}
{{fa-verb|tr=arzidan|prstem=ارز|tr2=arz}}

# to [[cost]]
# to [[be]] [[worth]]
# to [[be]] of [[value]]
# to [[have]] [[worth]]

====Conjugation====
{{fa-conj|ارزید|arzid|ارز|arz}}

====Descendants====
* {{desc|chg||ts=ärzimäk|bor=1}}
** {{desc|uz|arzimoq}}
** {{desc|ug|ئەرزىمەك}}
* {{desc|kk|арзу|bor=1}}
```


## [2026-09-04T19:42:06.548Z] TOOL CALL #47: Bash

```json
{
 "command": "curl -s \"https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/h%E2%82%82elg%CA%B7%CA%B0-&action=raw\" | head -60; echo \"===== PIr Harjati\"; curl -s \"https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Iranian/H%C3%A1r%C7%A7ati&action=raw\" | head -60"
}
```


## [2026-09-04T19:42:08.155Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"\\*Harz\\|arzidan\\|arəj\\|arz-\\|HARJ\\|Harj\" CHEUNG.txt | head -20"
}
```


### [2026-09-04T19:42:08.487Z] TOOL RESULT

```
{{reconstruction}}
==Proto-Indo-European==
{{etymon|ine-pro|id=cost|pos=root}}

===Root===
{{ine-root}}<ref>{{R:ine:LIV|page=263-4}}</ref><ref>{{R:ine:Mallory:2006|274}}</ref>

# to [[cost]], have value, be worth

====Derived terms====
* {{l|ine-pro||*h₂élgʷʰ-e-ti|pos=root thematic}}
** {{desc|iir-pro|*Hárǰʰati}} {{see desc}}
* {{l|ine-pro||*h₂élgʷʰ-t ~ *h₂l̥gʷʰ-ént|pos=athematic root aorist}}
** {{desc|grk-pro}}
*** {{desc|grc|ἦλφον}}
**** {{desc|grc|ἀλφάνω|der=1}}
* {{l|ine-pro||*h₂elgʷʰ-ós}}
** {{desc|iir-pro|*Hargʰás|t=price}} {{see desc}}
* {{l|ine-pro||*h₂elgʷʰ-éh₂}}<ref>{{R:ine:EIEC|head=*h₂elgʷʰo/eh{{sub|a}}|page=484}}</ref>
** {{desc|ine-bsl-pro|*algā́ˀ}} {{see desc}}
** {{desc|grk-pro}}
*** {{desc|grc|ἀλφή|unc=1|qq=probably an independent formation}}
* {{l|ine-pro||*h₂l̥gʷʰ-}}
** {{desc|ine-ana-pro}}
*** {{desc|hit|der=1|𒄬𒆪𒂊𒌍𒊬|tr=ḫal-ku-e-eš-šar|ts=ḫalkuēššar|t=supplies (for festivals)}}

====Descendants====
* {{desc|iir-pro|}}
** {{desc|sa|अर्ह्}} {{see desc}}

===References===
{{reflist}}

===Further reading===
* {{R:ine:IEW|volume=I|32}}===== PIr Harjati
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Not Found</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1114 cp1114, Varnish XID 902849478<br>Upstream caches: cp1114 int<br>Error: 404, Not Found at Fri, 04 Sep 2026 19:42:08 GMT<br><details><summary>Sensitive client information</summary>IP address: 206.172.78.33</details></code></p>
</div>
</html>
```


### [2026-09-04T19:42:08.527Z] TOOL RESULT

```
5153:Abyan. dasta/darz-, Anar. wer-mi-dest/ (impv.) wer-ders, Isfah. dasdän/därz-, Delij. 
5154:ba-darzi, Gz. dastmün/darzón-, Kafr. destemün/derzön-, Qohr. dasta/darz-, Sede 
5155:dastén/dazan-, Siv. derz-, dirz-/dist, Tr. dasta/darz- ‘to sew’, NP darzan ‘needle’ 
5164:polarz-/palisé-, M. polörz- ‘to wrap up (a bundle) || (+ *ni-) Sh. nióuyj ‘woollen yarn 
5510:which see *harz. 
8127:BMP glc- /garz-/ ‘to weep, lament’? (LW) || (+ *upa-) MMP ’bgrysn ‘moaning, 
9403:*harz ‘to let go, release’ 
9427:*harz 133 
9445:(Sor.) hestin/hel- ‘to permit, allow’, Zaz. estis/erzen- ‘to throw’, Abz. hasta/harz-, 
11474:*Harj ‘to be worth’ 
11482:*MIDDLE PERSIAN: BMP ’Ic- /arz-/ ‘to be worth’, MMP rein MMP. rein ‘worthy’ 
11499:*NWIR: NP arzidan/arz-, Gz. aZ-/aZà-, Khuns. erz-, Meim. a-h-arzo/a-h-arz-, Qohr. 
11500:harza/harz- ‘to be worth’, Isfah. arzän/ärz- ‘to cost? (LW), ? Sorkh. b-arsind-/ 
12009:developments of the root *Hmarz ‘to rub, wipe’ (e.g. ВМР mlc- /marz-/ ‘to 
12420:*NWIR: NP mälidan/mäl- ‘to rub, polish; to chafe, box the ears’, Bal. marzit/marz- 
12460:gwamel-, mäl-, marz-; Korn 2005: 97, 317, 404 
17803:*NWIR: Bal. marzit/marz- ‘to absolve, forgive, bless, encourage, support’ || (+ *a-) 
17976:*SOGDIAN: MSogd. (’)ms (inch.) ‘to plough’ (or < *Hmarz ?, cf. Bal. marz- ‘to 
20456:it is due to the influence of Pers. larzidan ‘to shake, tremble’ (*rarz) ? An IE 
20657:*MIDDLE PERSIAN: BMP llc- /larz-/ ‘to shake, tremble’, MMP mz ‘(fever’s)
```


## [2026-09-04T19:42:13.840Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11470,11520p' CHEUNG.txt"
}
```


### [2026-09-04T19:42:13.905Z] TOOL RESULT

```
£; WIM III: 303; ESIJa I: 200 £; Cabolov 2001: 82 f., 436; Lecoq 2002: 572b, 594b, 606a (passim); 
NEVP: 10; Korn 2005: 189, 270 


*Harj ‘to be worth’ 


*AVESTAN: arj- ‘to be worth’ — Liste: 10 
Pres. them.: IND. 3sg. YAv. arajaiti (H 1.5 f., H 1.8, H 1.10, etc.), INJ. 35р. arojat (Y 50.10, Y 64.6, Yt 
5.109, etc. 


*MIDDLE PERSIAN: BMP ’Ic- /arz-/ ‘to be worth’, MMP rein MMP. rein ‘worthy’ 
Pres.: IND. 3sg. BMP ’Icyt /arzed/ 


*SOGDIAN: SSogd. ’yrznw, MSogd. ‘yjn ‘worthy’, SSogd. ’ry, BSogd. ’ry, MSogd. 
ту ‘value, price’ 


*HasH 167 


sy с 


*CHORESMIAN: "Z- ‘to be worth’, (denomin.) m/Z’ny- ‘to estimate, value, negotiate 
about the price’ > Samadi: 267 f. 

*NWIR: NP arzidan/arz-, Gz. aZ-/aZà-, Khuns. erz-, Meim. a-h-arzo/a-h-arz-, Qohr. 
harza/harz- ‘to be worth’, Isfah. arzän/ärz- ‘to cost? (LW), ? Sorkh. b-arsind-/ 
ersinaen- ‘to buy’, NP arz ‘price, value’ 

*SANSKRIT: arh ‘to earn, be worth’ (RV+), arghä- (m.) ‘worth, value, price’ (RV+) 
c EWAia I: 114, 124 

«PIE *H;elg""- ‘to be worth, value, earn’ = LIV: 263 | Pok.: 32 f. 

*IE COGNATES: Hitt. /halkuessar/ (ritual) performance’, Gr. Agave ‘to bring in 
as profit’, (aor.) Gr. &Agetv ‘to earn, to obtain’, Lith. alga (Ё) ‘salary, pay’ 
*REFERENCES: Christensen, Contributions П: 113; Lambton 1938: 40a; WIM I: 68; Werba 1997: 334 f.; 
ESIJa Г: 218 f.; Lecoq 2002: 647a 


*Наг ‘to be envious’ 

*AVESTAN: Y Av. ars- ‘to be envious’, YAv. araska- (m.) ‘envy’ (Y 9.5, Yt 15.16, Yt 
19.33) = Liste: 10 

Partic.: pres. ja- Y Av. arasiiant- (Y 52.2)
```


## [2026-09-04T19:42:26.113Z] TOOL CALL #50: Bash

```json
{
 "command": "echo \"=== varcas\"; curl -s \"https://en.wiktionary.org/w/index.php?title=%E0%A4%B5%E0%A4%B0%E0%A5%8D%E0%A4%9A%E0%A4%B8%E0%A5%8D&action=raw\" | head -40; echo; echo \"=== emblic\"; curl -s \"https://en.wiktionary.org/w/index.php?title=emblic&action=raw\" | head -40; echo; echo \"=== amalaka\"; curl -s \"https://en.wiktionary.org/w/index.php?title=%E0%A4%86%E0%A4%AE%E0%A4%B2%E0%A4%95&action=raw\" | head -40"
}
```


### [2026-09-04T19:42:28.496Z] TOOL RESULT

```
=== varcas
==Sanskrit==

===Alternative scripts===
{{sa-alt}}

===Etymology===
{{dercat|sa|inc-pro|inh=1}}
From {{inh|sa|iir-pro|*wárčas||t=splendour, brilliance; vital power, energy}}. Cognate with {{cog|ae|𐬬𐬀𐬭𐬆𐬗𐬀𐬵|t=vital power; splendour, brilliance}}, {{cog|pal|𐫇𐫡𐫝|ts=warz|t=miraculous power}}.

===Pronunciation===
{{sa-IPA|a=1}}

===Noun===
{{sa-noun|n|tr=várcas}}

# [[energy]], [[might]], [[vital]] [[power]]
# [[brilliance]], [[splendour]], [[light]], [[lustre]]
#* {{Q|sa||RV|3|22|2|quote=अग्ने॒ यत् ते॑ दि॒वि '''वर्चः॑''' पृथि॒व्यां यद् ओष॑धीष्व् अ॒प्स्व् आ य॑जत्र ।<br>येना॒न्तरि॑क्षम् उ॒र्व् आ॑त॒तन्थ॑ त्वे॒षः स भा॒नुर् अ॑र्ण॒वो नृ॒चक्षाः॑ ॥|trans=That '''light''' of yours in heaven and earth, O Agni, in plants, O Holy One, and in the waters,<br>With which you have spread wide the air's mid-region; bright is that splendour, wavy, man-beholding.}}
#* {{Q|sa||RV|10|112|3|quote=हरि॑त्वता॒ '''वर्च॑सा॒''' सूर्य॑स्य॒ श्रेष्ठै॑ रू॒पैस् त॒न्वं॑ स्पर्शयस्व ।<br>अ॒स्माभि॑र् इन्द्र॒ सखि॑भिर् हुवा॒नः स॑ध्रीची॒नो मा॑दयस्वा नि॒षद्य॑ ॥|trans=Deck out thy body with the fairest colours, with golden '''splendour''' of the Sun adorn it.<br>O Indra, turn thee hitherward invited by us thy friends; be seated and be joyful.}}
# [[glory]]
#* {{Q|sa||RV|10|18|9|quote=धनु॒र् हस्ता॑द् आ॒ददा॑नो मृ॒तस्या॒स्मे क्ष॒त्राय॒ '''वर्च॑से॒''' बला॑य ।<br>अत्रै॒व त्वम् इ॒ह व॒यं सु॒वीरा॒ विश्वाः॒ स्पृधो॑ अ॒भिमा॑तीर् जयेम ॥|trans=From the hand of the deceased one I take the bow to be carried, that it may be our power and might and '''glory'''.<br>There you are, there; and here with noble heroes may we overcome all enemies that fight against us.}}

====Declension====
{{sa-decl-noun-n|várcas}}

===Proper noun===
{{sa-propn|m}}

# name of a son of [[w:Chandra|Chandra]]

====Declension====
{{sa-decl-noun-m|varcas}}

====Related terms====
* {{l|sa|वर्चस्य}}
* {{l|sa|वर्चस}}
* {{l|sa|वर्चस्वत्}}

===References===
* {{R:MW|924|col=1}}
=== emblic
==English==
[[File:Nellikai.jpg|thumb|right|{{lang|en|emblic}}|upright=1.15]]

===Etymology===
From {{der|en|la-med|emblicus}}, from {{der|en|ar|أَمْلَج}}, from {{der|en|sa|आमलक}}. {{doublet|en|amla}}.

===Noun===
{{en-noun}}

# The [[fruit]] of {{taxlink|Emblica officinalis|species}} (now {{taxfmt|Phyllanthus emblica|species}}, the [[Indian gooseberry]], once used as a remedy against [[dysentery]])

====Synonyms====
* {{sense|''Emblica officinalis''}} [[amla]], [[Indian gooseberry]]

====Derived terms====
* {{vern|emblic myrobalan}}

===Anagrams===
* {{anagrams|en|a=bceilm|limbec}}

{{C|en|Malpighiales order plants}}
=== amalaka
==Sanskrit==
{{rfc|sa}}

===Noun===
{{sa-noun}}

# {{vern|emblic myrobalan}}, Emblica Officinalis Gaertn.
# the fruit of the Emblic Myrobalan MBh. Suṡr. ChUp. &c.
# another plant, Gendarussa Vulgaris

====Descendants====
* {{desc|te|ఆమలకము}}

===References===
* {{R:MW|146|col=3}}

{{C|sa|Malpighiales order plants}}
```


## [2026-09-04T19:42:39.211Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in AFM.txt TAD.txt LKT.txt HJB.txt AID.txt FVQ.txt SKT.txt AFA.txt DEV.txt; do echo \"=== $f\"; grep -n -i \"amlaj\\|emblic\\|amla\\b\\|املج\\|آمله\" $f | head -6; done"
}
```


## [2026-09-04T19:42:39.794Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && grep -n -i \"amlaǧ\\|amlag\\|amlaj\\|Amla\" PLA_asbaghi_1988_ia_djvu.txt | head -10"
}
```


### [2026-09-04T19:42:40.846Z] TOOL RESULT

```
=== AFM.txt
=== TAD.txt
=== LKT.txt
1252:479.  Tk.  damla:
1253:'Tropfen'  [Stamm  dam  'tröpfeln',  s.  hier Nr.  478],  auch  'SchlaganfaU' ;  hieraus rum.  dambla,  damla  'dass.',  damblagiü; bulg.  damla  'dass.'.
2485:'Laus',  Einheitsnomen  kamla;  hieraus it.  (dial.  Venedig)  cdmola,  siz.  camula
3875:'Sand',  Einheitsnomeu  ramla  'Sandflä- che, Bett  eines  Wildbaches';  hieraus  sp. kat.  rambla  'dass.,  Allee';  La  Ramhla die  Hauptstraße  in  Barcelona,  die  dem Laufe  eines  Wildbaches  folgt,  der  die Stadt  durchschnitt.  [DE  329.  Eguilaz 478.    ML  7030.
4897:hieraus  mit  ar.  Art.  sp.  acemila,  Abltg. azemilero  'Maultiertreiber',  pg.  azemola, kat.  asemhla  'Lasttier'.  Aus  ar.  zammäl 'Treiber'  wurde  mit  Imäla  [ä  >  e/  i)g. azemel  'Maultiertreiber'.  Zur  gleichen Wurzel  gehört  ar.  zamla.  'Familie  und Hausgerät  eines  Häuptlings';  hieraus pg.  nzemel  'Lager,  Zeltstadt',  frz.  zniala, srnala  'dass.  (in  Algerien)'.  [DE  33. Devic  DEt  209.    Eguilaz  22/23.
=== HJB.txt
1856:AMBABBEH,  s.  Dekh.  Hind,  and Mahr.  ambdrd,  ambdri  [Skt.  amla-ydt- ikd],  the  plant  Hibiscus  canndbinus, affording  a  useful  fibre.
5607:GAYOLAQXJE,  s.  Kayu=='^^'ood; in  Malay.  Laka  is  given  in  Craw- furd's  Malay  Diet,  as  "name  of  a red  wood  used  as  incense,  Myridica iners,**  In  his  Descr.  Did.  he  calls  it the  ^^Tanarius  major;  a  tree  with  a red-coloured  wood,  a  native  of  Sumatra, used  in  dyeing  and  in  pharmacy.  It is  an  article  of  consiaerable  native trade,  and  is  chiefly  exported  to China"  (p.  204).  [The  word,  accord- ing to  Mr.  Skeat,  is  probably  kayu, *wood,'  lakh,  *red  dye  ^  (see  LAC),  but the  combined  form  is  not  in  Klinkert, nor  are  these  trees  in  Ridley's  plant list.  He  gives  Ldka-laka  or  Malafca  as the  name  of  the  phyUanthus  emblica.]
13792:MALACCA,  n.p.  The  city  which gives  its  name  to  the  Peninsula  and the  Straits  of  Malacca,  and  which  was the  seat  of  a  considerable  Malay  mon- archy till  its  capture  by  the  Portuguese under  D'Alboquerque  in  1511.  One naturally  supposes  some  etymological connection  between  Malay  emd  Malacca. And  such  a  connection  is  put  forward by  De  Barros  and  D'Alboquerque  (see below,  and  also  under  MALAY).  The latter  also  mentions  an  alternative suggestion  for  the  ori^n  of  the  name of  tne  city,  which  evidently  refers  to the  Ar.  muldkdtj  *a  meeting.'  This last,  though  it  appears  also  in  the Sijara  MaUiytL^  may  oe  totally  rejected. Crawfurd  is  positive  that  the  place was  called  from  the  word  malaka,  the Malay  name  of  the  Phyllanthus  emUtca^ or  emblic  Myrobalan  (q.v.),  "a  tree said  to  be  abundant  in  that  locality  "  ; and  this,  it  will  }ye  seen  below,  is  given by  Cjfodinho  de  Eredia  as  the  ety- mology. Malaka  again  seems  to  be  a corruption  of  the  Skt.  amlaJca^  from a/mla,  *  acid,*  [Mr.  Skeat  writes : "There  can  be  no  doubt  that  Craw- furd is  right,  and  that  the  place  was named  from  the  tree.  The  suggested connection  between  Malayu  and  Ma- laka appears  impossible  to  me,  and, I  think  would  do  so  to  any  one  ac- quaintea  with  the  laws  of  the  language. 1  have  seen  the  Maldka  tree  myself and  eaten  its  fruit.  Ridley  in  his Botanical  Lists  has  laka-laka  and  ma- laka which  he  identifies  as  Phyllanthris emhlioay  L.  and  P.  pectinatua  Hooker (Euj^lwrbia^^eae).  The  two  species  are haraly  distinct,  but  the  latter  is  the commoner  form.  The  fact  is  that  the place,  as  is  so  often  the  case  among the  Malays,  must  have  taken  its  name from  the  Sungei  Malaka^  or  Malaka River.'*]
15262:It  is  not  quite  clear  how  the  term myrohalariy  in  this  sense,  came  into  use. For  the  people  of  India  do  not  seem  to have  any  smgle  name  denoting  these fruits  or  drugs  as  a  group  ;  nor  do  the Arabic  dictionaries  a^ord  one  either (but  see  further  on).  Mv/^o/SdXayos  is spoken  of  by  some  ancient  authors, e,g,  Aristotle,  Dioscorides  and  Pliny, but  it  was  applied  by  them  to  one  or more  fruits*  entirely  unconnected  with the  subjects  of  this  article.  This  name had  probably  been  preserved  in  the laboratories,  and  was  applied  by  some «arly  translator  of  the  Arabic  writers on  Materia  Medica  to  these  Indian products.  Though  we  have  said  that (so  far  as  we  can  discover)  the  diction- aries afford  no  word  with  the  compre- hensive sense  of  Myrohcdan^  it  is probable  that  the  physicians  had  such a  word,  and  Gkrcia  de  Orta,  who  is trustworthjr,  says  explicitly  that  the Arab  practitioners  whom  he  had  con- sulted applied  to  the  whole  class  the name  delegi,  a  word  which  we  cannot identify,  unless  it  ori^nated  in  a clerical  error  for  aUleat^  i.e.  ihlilaj. The  last  word  may  perhaps  be  taken as  covering  all  myrobalans ;  for  accord- ing to  tne  Qlossarv  to  Rhazes  at Leyden  (quoted  by  Dozy,  Suppt,  i.  43) it  applies  to  the  Kdbultj  the  yellow^ and  tne  black  (or  Indian]^  whilst  the EmbHc  is  also  called  Ihlilaj  amlaj.
15264:"  HuUla  (Myrobalan). Bvlda  (BeUerick  ditto). Amla  (Emblica  Phyllanthus)."
15267:(1)  The  EmbUe  myrobalan;  which  is the  dried  astringent  fruit  of  the Anwuldy  dntold  of  Hind.,  the  Emblica officinalis  of  Ckiertner  (Phyllanthus Emblica,  L.,  N.  O.  Euphorbiacea/). The  Persian  name  of  this  is  dmlah^ but,    as    the    Arabic    amlaj   suggests
=== AID.txt
542:Aonla..  [Corruption  of  the  Hindi anold.]  The  myrobolan  tree,  phyl- lanthus  emblica.
5084:Omlah.  See  Amla.
=== FVQ.txt
=== SKT.txt
=== AFA.txt
=== DEV.txt
793:Myrobalanorum  species  sunt  qninque  bonorum  : Citrinus,  Kebukis,  Bellericus,  Emblicus,  Indus.
795:Citrini  coleram  purgent,  hebulus  atque Bellericus  fleuma  pellunt,  quels  emblicus  —  (?)
796:On  trouvera  plus  loin  l'étymologie  arabe  de  kebulus  = hebulus  et  de  emblicus.
1248:final;  on  sait  qu'il  rendent  souvent  cette  lettre  par  un  ^ (Ij  ou  g  dur,  ce  dont  on  peut  voir  un  exemple  plus  loin  au mot  Emblic.  11  est  vrai  qu'on  trouve  en  vieux  français cschas,  cscaSy  bas  lat.  scacatus;  mais  la  forme  actuelle  écliec ou  eschec  est  encore  plus  ancienne  et  remonte  au  xf  siècle. Quant  à  songer  à  l'arabe  ^^  cheikh  comme  employé pour  chah,  Va  de  eschas,  xaque,  scacco,  etc.  ne  le  permet  pas.
1260:Emblic,  Emblique,  Amblique.  Terme  de  droguerie;  es- pèce de  myrobolan.  Latin  du  moyen  âge  emblmis  (voy. Chebule),  ^emblica  Arabes  embelgi  vocant7^  dit  Jean Bauhin,  d'après  Garcias  [Histor,  plantariun  univers.).  C'est en  effet  l'arabe  ^\  amleclj,  qui  est  le  persan  »X^)  amleh, venant  lui-même  du  sanscrit  âmlak.  J^^\  amleclj  est  dans Razi.  (Trait.  111,  ch.  xxviii,  folio  à']  recto  du  man.  déjà cité.)  La  forme  sanscrite  est  restée  dans  le  malais  iiJu«  7na- lâka,  emblic  officinal,  lequel,  d'après  les  traditions  ma- laises, a  donné  son  nom  à  la  presqu'île  de  Malacca"^.
2699:Amblique,  voy.  Emblic.
```


### [2026-09-04T19:42:40.887Z] TOOL RESULT

```
856:mp. armav —>ar. amrüd, amlaß "Birne" 
2969:er - ”amlaß: "Myrobabni Emblici; Fruchtschalen v. Phyllanthus Emblica" 
13582:&-)e& - Siramlaf: "Myrobalane" (Frucht) < pers. Uli $irämle ®, syr. 
19499:or hamla$: "ruhig gehen".
```


## [2026-09-04T19:42:51.502Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && sed -n '2960,2985p' PLA_asbaghi_1988_ia_djvu.txt; echo \"=== find page\"; python3 - <<'EOF'\nt=open('PLA_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'amla' in p and 'Emblic' in p:\n        print('leaf',i); print(p[:1200]); break\nEOF"
}
```


## [2026-09-04T19:42:52.850Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('DEV.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport bisect\noff=0; starts=[]\nfor p in pages:\n    starts.append(off); off+=p.count('\\n')+1\ni=bisect.bisect_right(starts,1259)-1\nprint('leaf',i)\nprint(pages[i][:400])\nprint('...')\nprint(pages[i][-400:])\nEOF"
}
```


### [2026-09-04T19:42:53.534Z] TOOL RESULT

```
vei- ämis: "rohes Fleisch in Essig eingelegt; Kalbaspik" aus pers. 
je hämiz 7 mp. 90 xamiz "eingemachtes Fleisch" 8, 
Ar. a Amis T pers. ef amie I mp. „p ämek "Mixtur, Mischung", syr. 
yı, aram.y»X. 


; 
er - ”amlaß: "Myrobabni Emblici; Fruchtschalen v. Phyllanthus Emblica" 
pers. LT ämle 11 <TImp. 232 ambag 12 


za - ’umluß: "Dattelkern" —T mp. ım> armavy "Datteln" . 


ar - amüya: "heiliger Trank mit Rauschwirkung, Oxus" pers. 14 wahr- 
scheinlich aus dem mp. «vr hom <aw. homikan . 


1. al-Marda® s. v., Muhit s. v. 
2. Fremdwörterbuch s. Vv. 

3. al-Marfa“ s. v. 

4. Löw s. v. 
=== find page
leaf 40
’ ambarbäris                                                                       26                                                           ämüya


sb              ei _ ” ambarbaris:                          "Berberis,             Berberitze"                pers.
          Berberitze                <         pers.         > ar.            >> lat.       2     wahrscheinlich                aus     dem    pers.
              o>,,£           parparrize                  "mit        kleinen       Blättern"            od.         ew_22 Borparrize
           "mit        vielen         kleinen               Blättern".,             syr.        wol.


O»1-            ’immidan:               "Wasser             der       Oberfläche           der        Erde;         sehr    salziges     Wasser"      3
           wahrscheinlich                      eine         pers.-ar.             Zusammensetzung                    aus    pers.     -! ab
           u.    ar. c3>=             maCdani               mit       reg.       ass.     v.    b zu m "Mineralwasser".


yet -            ”amrüt:            "Birne"               pers.        io         pers.        »»»ı     amrod         Me        ai
```


### [2026-09-04T19:42:55.374Z] TOOL RESULT

```
leaf 127
ion  arabe,  marque  du  nominatif  des  noms  indéter-
'  Voy.  Defrémery,  Mém.  d'hist.  orient,  p.  2  35.  Le  savant  professeur  cite un  passage  du  Voyage  de  Chapelle  et  de  Bachaumont,  ({ui  montre  qu'au XVII*  siècle  chicane  se  disait  du  jeu  du  mail  :  «Nous  y  arrivâmes  à  travers mille  boules  de  mail  :  car  on  joue  là,  le  long  dos  chemins,  à  la  chicane.
...
aité  d'arithmétique du  xvif  siècle  :  ç^La  dernière  figure,  qui  s'appelle  nulle ou  zéro,  ne  vaut  rien. . .  En  autre  langage,  elle  s'appelle chifre;  toutefois  ce  mot  abusivement  prins  en  françois signifie  toutes  les  figures  et  l'art  d'arithmétique  ^.  •)•>
Zéro  est  une  autre  forme  du  même  mot -àao  sifr,  que  les anciens  traités  de  calcul  écrits  en  lati
```


## [2026-09-04T19:43:05.624Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('DEV.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'Emblic, Emblique' in p:\n        print('leaf',i)\n        nums=re.findall(r'(?m)^\\s*(\\d{1,3})\\s*$',p)\n        print('page nums found:',nums)\n        j=p.find('Emblic, Emblique')\n        print(p[max(0,j-600):j+900])\nEOF"
}
```


### [2026-09-04T19:43:07.405Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:43:10.912Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('DEV.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'Emblic' in p and 'amleh' in p:\n        print('leaf',i)\n        nums=re.findall(r'(?m)^\\s*(\\d{1,3})\\s*$',p)\n        print('nums',nums)\n        print(p[:1500])\nEOF"
}
```


### [2026-09-04T19:43:12.570Z] TOOL RESULT

```
leaves 326
leaf 141
nums []
recueilli ce  terme  est  trop  récent  pour  qu'on  en  puisse  rien  con- clure sur  la  nationalité  du  mot^.
Elixir.  Esp.  et  portug.  elixir,  ital.  clisire.  (j'est  l'arabe wufc^iJÎ  el-ikslr,  terme  par  lequel  les  alchimistes  désignent la  pierre  philosophale,  la  matière  solide  ou  liquide  qui doit  servir  à  la  transmutation  des  métaux,  la  poudre  de projection  :  «In  ipsis  pulveribus  qui  a  philosophis  vocantur elixir.  w  (^Opus  mirabile  de  Mercurio  ad  ejus  Jîxationem^.^  On
'   Lillré,  Dict.
-  Journ.  asiat.  mal  1866,  p.  3aa.  On  peut  voir  aussi  Dozy,  Gloss.  p.  269.
^  L'auteur,  Alkulioubi,  est  mort  en  i()r)().
*  Dans  le  man.  lat.  n"  7 1  /17,  ancien  fonds,  de  la  Bibl.  nat.  p.  1 8  verso.  Le môme  volume  contient  un  traité  intitulé  Elixiris  composilin  vera ;  il  semble linduit  de  Tliébreu  et  commence  par  ces  mots  :  rln  nomine  Adonay.')
DES  MOTS  D'ORIGINE  ORIENTALE.  109
Iroiivo  aussi  nlexir,  c^medicina  alcliymice  praeparala??  (Ru- land,  Led'ic.  alchcm.)^  xir,  yxir  ai  y  sir.
Le  mot  arabe  lui-même  n'est  autre  chose  que  la  trans- cription du  grec  ^vpov,  sec,  médicament  sec.  On  a  objecté^ contre  cette  origine  que  les  Arabes  transcrivent  le  ?  par JuM  sk  et  non  par  ^jf^  ks;  mais  il  existe  d'autres  exemples de  cette  dernière  transcription  ks  ou  qs,  et  M.  Defrémery en  a  cité  trois^:  ^^^luwJb  hoqsls^  buis  =  ^arv^os;  I^U
```


## [2026-09-04T19:43:18.729Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%A2%D9%85%D9%84%D9%87",
 "prompt": "What does Mo'in's dictionary (فرهنگ معین) say for آمله? Give the entry text including any origin tag."
}
```


## [2026-09-04T19:43:20.143Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/indoeurop.html",
 "prompt": "Find the Indo-European root entries \"alu-\" and \"algwh-\" (or h2elgwh). Quote the full text of each root entry, including derivatives listed."
}
```


### [2026-09-04T19:43:20.596Z] TOOL RESULT

```
The server returned HTTP 500 Internal Server Error.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T19:43:27.359Z] TOOL RESULT

```
# Indo-European Root Entries

## alu-

**Full entry text:**

"In words related to sorcery, magic, possession, and intoxication. Suffixed form _\*alu-t‑_. [ale](/word/search.html?q=ale), from Old English _ealu_, from Germanic _\*aluth‑_."

The root connects to the word "ale" through Germanic linguistic development.

## algwh- (or h2elgwh)

This root entry does not appear in the provided document. The appendix content shown includes roots from "ad-" through "bheuə-," but does not extend to entries beginning with "algwh-" or similar variations. To locate this root, you would need to access a different section of the Indo-European roots appendix.
```


## [2026-09-04T19:43:34.033Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^alu-\\|^alu\\b\\|alu-\" AHD_watkins1985.txt | head -10; echo \"===\"; grep -n -i \"alumen\\|aluminum\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-04T19:43:34.088Z] TOOL RESULT

```
280:al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
606:small hollow: HAUGH; e. Dutch holster, holster, (< “that which covers”): HOLSTER. 2. Suffixed Germanic form *hulfti- in Medieval Latin hultia, protective covering: HOUSING?. 3. Suffixed form *kl-to- in Latin occultus (see III. 5. below). 4. Extended form *kld (< *kl-) in Latin clam, in secret: CLANDESTINE. 5. Suffixed variant form *kal-up-yo- in Greek kaluptein, to cover, conceal: Ca- LYPSO, CALYPTRA; APOCALYPSE, EUCALYPTUS. III. Full-grade form *kel-. 1. Germanic *helmaz, “‘protec- tive covering,” in: a. Old English helm, protection, cover- ing: HELM?; b. Frankish *helm, helmet, akin to the source of Middle English helmet, helmet: HELMET. 2. Latin occulere (part participle occultus; see Il. 4. above), to cover over (ob-, over; see epi): OCCULT. 3. Suf- fixed form *kel-os- in Latin color, color, hue (< “that which covers”): COLOR. 4. Suffixed form *kel-nd in Latin cella, storeroom, chamber: CELL, CELLA, CELLAR, CELLARER; (RATHSKELLER). 5. Suffixed form *kel-yo- in Latin cilium, lower eyelid: CILIUM, SEEL; SUPERCILIOUS, (SUPERCILIUM). IV. Lengthened-grade form *kél-d- in Latin céldre, to hide: CONCEAL. See extension klep-. [Pok. 4. kel- 553.] kel-3. To drive, set in swift motion. Hypothetical base of various loosely connected derivatives. 1. Extended form *kelt- or *keldh- possibly in Germanic *haldan, to drive flocks, keep or pasture cattle, in: a. Old English healdan, to hold, retain: HOLD!; b. Old High German haltan, to stop, hold back: HALT!; c. Middle Dutch houden, to hold: AVAST. 2. Suffixed form*kel-es- in: a. Latin celer, swift: CELERITY; ACCELERATE; b. possibly further suffixed form *keles-ri- in Latin celeber, (of a place) much fre- quented, hence famous: CELEBRATE, CELEBRITY. 3. Suf- fixed zero-grade form *kl-on- in Greek klonos, turmoil, agitation: CLONUS. [Pok. 5. kel- 548.] kel-4. To lean, tilt. Germanic *halthjan in Old English hieldan, to tilt: HEEL2. [Pok. 2. kel- 552.] kel-5. Gray, black, dark. Suffixed form *kel-omb(h)- in Latin columba, dove, pigeon: COLUMBA, COLUMBARIUM, COLUMBINE, CULVER. [Pok. 4. kel- 547.] kel-*, To be prominent; hill. 1. Zero-grade form *k/- in: a. suffixed Germanic form hul-ni- in Old English hyll, hill: HILL; b. suffixed Germanic form *hul-ma- in Old Norse holmr, islet in a bay, meadow: HOLM. 2. Suffixed form *kel-d- in Latin excellere, to raise up, elevate, also to be eminent (ex-, up out of; see eghs): EXCEL. 3. O-grade form *kol- in: a. Greek kolophén, summit: COLOPHON; b. suffixed form *kol(u)men- in Latin culmen, top, summit: CULMINATE; C. extended and suffixed form *kolumna in Latin columna, a projecting object, column: COLONEL, COLONNADE, COLUMN. [Pok. 1. kel- 544.] kel-7. To prick. Germanic *hulin- in Old English holen, holly (from its spiny leaves): HOLLY. [Pok. 2. kel- 545.] kel-®. To deceive, trick. Extended form *kelu-, variant *kalu-, in: a. Latin calvi, to deceive, trick: CALUMNY, CHALLENGE; b. Latin cavilla (< *calvilla), a jeering: CAVIL. [Pok. Rél- 551.] kelb-. To help. Germanic *helpan in Old English helpan, to help: HELP. [Pok. kelb- 554.] kele-1. Warm. Variant *klé-, contracted from *kleo-. 1. Suffixed variant form *k/é-wo- in Germanic *hléwaz in Old English hléo, hléow, covering, protection (as from cold): LEE. 2. Suffixed zero-grade form *kip-é- in: a. Lat- in calére, to be warm: CALENTURE, CHAFE; DECALES- CENCE, NONCHALANT, RECALESCENCE; Db. Latin derivative adjective calidus, warm (> French chaud, warm): CALDRON, CAUDLE, (CHOWDER); CHAUDFROID, SCALD'. 3, Suffixed zero-grade form *fl-os- in Latin calor, heat: CALORIC, CALORIE; CALORECEPTOR, CALO- RIFIC, CALORIMETER, CALORIMETRY. [Pok. 1. kel- 551.] kele-2. To shout. I. Variant form *kld- (< *klaa-). 1. Ger- manic Aljé- in Old English hléwan, to roar, low: Low?. 2. Suffixed form *k/d-mé- in Latin clamare, to call, cry out: CLAIM, CLAMANT, CLAMOR; ACCLAIM, DECLAIM, EXCLAIM, PROCLAIM, RECLAIM. II. O-grade form *kob-.
1227:ALB albho- ALBEDO albho- ALBESCENT albho- ALBINO albho- ALBITE albho- ALBUM albho- ALBUMEN albho- ALBURNUM _albho- ALDER el-2 ALDERMAN al-3 ALE alu-
===
```


## [2026-09-04T19:43:34.650Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in SKT.txt FSD_vol1.txt WEB_vol1.txt; do echo \"=== $f\"; grep -n -i \"^ALUM\\|^ALE\\b\\|alumen\" $f | head -8; done"
}
```


### [2026-09-04T19:43:36.418Z] TOOL RESULT

```
=== SKT.txt
526:Ale.  (E.)  M.  E.  a/f,-  A.  S,  /«/«.+ led.,  S  wed,  and  Dan.  «/;  Lilhnon.  ahu; KoM.  oi\  olevina.
9577:ale,    to   mix   tof^ether  confosedlr.
=== FSD_vol1.txt
11478:ale,  1   61;  2   al,  n.  1.  A   beverage;  made  from  a   fermented  Men  mn
11497:ale,  bread,  etc.,  bolled.- bush.  2.  The  sign  of  an  Inn.- tor  of  ales  and  ale-measures.—
11510:ale  brewed,  originally  for  audit  day.  In  certain  En- glish colleges.—  bitter  ale,  an  ale  made  of  hops,  strong  and somewhat  bitter.— Burton  ale  [Eng.],  ale  brewed  at  Bur- ton-on-Trcnt,  the  water  of  which  place  is  excellent  for  brew- ing; hence,  by  extension,  an  ale  of  superior  body  and  of great  strength.—  butter  or  buttered  ale,  an  ale  contain- ing no  hops  or  other  bitter  element,  but  flavored  with  sugar, butter,  and  spice.—  cuckoo  ale,  ale  reserved  for  spring  use, at  the  time  when  the  cuckoo’s  notes  are  first  heard  —   four
11513:ale  [Eng.],  beer  sold  at  lourpence  a   quart;  small  beer.—  al'era,  1   al'em;  2   al'Sm,  n.  [Turk.]  A   flag  or  standard; hocking  ale,  the  ale  brewed  and  drunk  at  hocking.  sometimes,  the  standard  crescent  on  a   mosque;  as,  the See  hocking.— mace  ale,  an  ale  sweetened  and  flavored  imperial  alem.  Iv,  26.
11554:ale'*sll"ver,  n.  See  under  ale.
12992:aluminum  Key  S:  art,  ape,  fat,  fare,  fast,  what,  all;  m6,  get,  prey,  fern;  htt,  ice;  I   =   e;  i   =   e;  go,  not,  or,  won,  wolf,  do,
13139:Alum-root  ( Heuchera americana).
13191:C.  L.  Bloxam  Chemistry,  Aluminium  p.  303.  [p.  b.  co.  1890.] [OF.  (F.  alun),  <   L.  alumen.)  aHomf;  al'lnmt;  al'- lumet;  al-u'ment;  al'ymt.—  al'um -bath",  n.  A   bath  for preventing  the  frilling  'of  films  on  photographic  plates,  or blistering  of  papers,  composed  of  a   saturated  solution  of potassium  or  chrome  alum;  used  also  In  the  carbon  and other  processes  where  bichromate  of  potassium  is  employed as  a   sensitizing  agent,  to  remove  the  yellow  color.— a.* cake",  n.  A   solid  mixture  of  aluminum  sulfate  and  silica, formed  by  the  action  of  sulfuric  acid  on  roasted  clay.—  a.* earth,  n.  Geol.  A   soft  variety  of  alum  'shale,  generally  bi- tuminous— a. sflower,  n.  Powdered  burnt  alum.— a.* glass,  n.  Alum  crystallized.—  a. *rock,  rz.  Same  as  alu- nite.— a.sroot,  n.  A   low  herb  of  the  genus  Heuchera  of the  saxifrage  family,  espe- cially H.  americana,  or  Its astringent  root.  a.s bloom  J.— a.  s   cvk  1st, shale,  or  slate,  a   clayey, generally  carbonaceous  rock containing  marcasite  and yielding  alum  as  a   decom- position pr  oduct.—  a.» stone,  n.  Same  as  alu- NiTE.-a.  whey,  whey made  from  milk  coagulated with  alum.—  burnt  or  dried a.,  the  white  powder  left after  the  extraction  from alum  of  the  water  of  crys- tallization.— concentrated or  patent  a.,  aluminum sulfate  (All (SO Os)  made  by crystallization  from  alum- cake.— Iron  a.,  a   double sulfate  of  Iron  and  potas- sium that  occurs  native  and Is  then  called  halotrlchlte. a.sfeathcr].— Roman  a., a   potash-alum  prepared fromalunlte,  originally  prob- ably In  Italy:  highly  val- ued by  dyers,  owing  to  Its freedom  from  Iron,  roche a.J;  rock  a.t.— saccha- rine a.,  a   composition  of  alum,  rose-water,  and  albumen, cooked  and  allowed  to  harden  by  cooling.
=== WEB_vol1.txt
5303:Ale-ma/ni-An, a. pertaining to Aleman, a Spartan lyric poet of the seventh century B. C., or to his verse.
5304:Ale-mé/né, n. [L.; Gr. Alkméné.] in Greek mythology. the mother of Hercules: see Amphitryon.
5355:ale. a-lec/i-thal, a. [Gr. a priv., and lekithos, yolk.]
5357:Ale’con-nér, n. [ale and con, to know or see. |
5369:ale’hoof, n. [ME. alehoofe, a corruption of haihove; hai, a hedge, and hoofe, ivy; AS. hofe, ivy.] ground ivy.
5371:ale knight, a drinking companion. [Obs.]
5391:ale; dote n. [Gr. a priv., and lepis (lepido- a t a oe A RR £6 tis), scale.| any fish whose skin is not scaly.
5412:Ale’wife, n.; pl. ale’wives, a fish, Clupea ver- nalis, of the herring family, found in the ocean and in some lakes and streams.
```


## [2026-09-04T19:43:52.314Z] TOOL CALL #61: Bash

```json
{
 "command": "for u in alum aluminum ale; do echo \"############ $u\"; curl -s -A \"Mozilla/5.0\" \"https://www.etymonline.com/word/$u\" | python3 -c \"\nimport sys,re,html\nt=sys.stdin.read()\nt=re.sub(r'<script.*?</script>','',t,flags=re.S)\nt=re.sub(r'<style.*?</style>','',t,flags=re.S)\nt=re.sub(r'<[^>]+>',' ',t)\nt=html.unescape(t)\nt=re.sub(r'\\s+',' ',t)\ni=t.find('$u')\nprint(t[:60])\nimport sys\n\" ; done"
}
```


### [2026-09-04T19:43:55.168Z] TOOL RESULT

```
############ alum
 Alum - Etymology, Origin & Meaning Search Log in Columns Fo
############ aluminum
 Aluminum - Etymology, Origin & Meaning Search Log in Column
############ ale
 Ale - Etymology, Origin & Meaning Search Log in Columns For
```


## [2026-09-04T19:43:58.564Z] TOOL CALL #62: Bash

```json
{
 "command": "for u in alum aluminum ale; do echo \"############ $u\"; curl -s -A \"Mozilla/5.0\" \"https://www.etymonline.com/word/$u\" | python3 -c \"\nimport sys,re,html\nt=sys.stdin.read()\nt=re.sub(r'<script.*?</script>','',t,flags=re.S)\nt=re.sub(r'<style.*?</style>','',t,flags=re.S)\nt=re.sub(r'<[^>]+>',' ',t)\nt=html.unescape(t); t=re.sub(r'\\s+',' ',t)\nprint(t[200:2600])\n\"; echo; done"
}
```


### [2026-09-04T19:44:00.646Z] TOOL RESULT

```
############ alum
 Origin and history of alum alum (n.) "whitish mineral salt used as an astringent, dye, etc.," late 14c., from Old French alum , alun , from Latin alumen "alum," also "the alum plant," from Proto-Italic *alu- "bitter substance" literally "bitter salt," cognate with Greek aludoimos "bitter" and perhaps with English ale and some Balto-Slavic words for "beer" (such as Lithuanian alus). The plant's medicinal use on wounds was known to Pliny. also from late 14c. Entries linking to alum ale (n.) "intoxicating liquor made by malt fermentation," Old English ealu "ale, beer," from Proto-Germanic *aluth- (source also of Old Saxon alo , Old Norse öl ), which is of uncertain origin. Perhaps from a PIE root meaning "bitter" (source also of Latin alumen "alum"), or from PIE *alu-t "ale," from root *alu- , which has connotations of "sorcery, magic, possession, and intoxication" [Watkins]. The word was borrowed from Germanic into Lithuanian ( alus ) and Old Church Slavonic ( olu ). In the fifteenth century, and until the seventeenth, ale stood for the unhopped fermented malt liquor which had long been the native drink of these islands. Beer was the hopped malt liquor introduced from the Low Countries in the fifteenth century and popular first of all in the towns. By the eighteenth century, however, all malt liquor was hopped and there had been a silent mutation in the meaning of the two terms. For a time the terms became synonymous, in fact, but local habits of nomenclature still continued to perpetuate what had been a real difference: 'beer' was the malt liquor which tended to be found in towns, 'ale' was the term in general use in the country districts. [Peter Mathias, "The Brewing Industry in England," Cambridge University Press, 1959] Meaning "festival or merry-meeting at which much ale was drunk" was in Old English (see bridal ). aluminum (n.) by 1812, from alumina , alumine , the name given by French chemists late 18c. to aluminum oxide, from Latin alumen "alum" (see alum ). Sir Humphry Davy, working to isolate it, called it alumium (1808), later he used aluminum (by 1812), which remains the U.S. word. The form aluminium , the modern preferred British word, was proposed by January 1811 in an account of Davy's published experiments written by William Hyde Wollaston (discoverer of palladium and rhodium) and printed in The Critical Review: Potassium, acting upon alumine 

############ aluminum
ads. Origin and history of aluminum aluminum (n.) by 1812, from alumina , alumine , the name given by French chemists late 18c. to aluminum oxide, from Latin alumen "alum" (see alum ). Sir Humphry Davy, working to isolate it, called it alumium (1808), later he used aluminum (by 1812), which remains the U.S. word. The form aluminium , the modern preferred British word, was proposed by January 1811 in an account of Davy's published experiments written by William Hyde Wollaston (discoverer of palladium and rhodium) and printed in The Critical Review: Potassium, acting upon alumine and glucine, produces pyrophoric substances of a dark grey colour, which burnt, throwing off brilliant sparks, and leaving behind alkali and earth, and which, when thrown into water, decomposed it with great violence. The result of this experiment is not wholly decisive as to the existence of what might be called aluminium and glucinium . It better harmonizes with the other metallic element names ( sodium , potassium ). Aluminium, for so we shall take the liberty of writing the word, in preference to aluminum, which has a less classical sound. [Quarterly Review, September 1812] Aluminum foil attested by 1859; popularized in food packaging from c. 1950. also from 1812 Entries linking to aluminum alum (n.) "whitish mineral salt used as an astringent, dye, etc.," late 14c., from Old French alum , alun , from Latin alumen "alum," also "the alum plant," from Proto-Italic *alu- "bitter substance" literally "bitter salt," cognate with Greek aludoimos "bitter" and perhaps with English ale and some Balto-Slavic words for "beer" (such as Lithuanian alus). The plant's medicinal use on wounds was known to Pliny. potassium (n.) metallic element, 1807, coined by English chemist Sir Humphry Davy from Modern Latin potassa , Latinized form of potash (q.v.). Davy first isolated it from potash. The chemical symbol K is from Latin kalium "potash," from Arabic al-qaliy "the ashes, burnt ashes" (see alkali ). Related: Potassic . sodium aluminium sial See All Related Words (5) Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads. More to explore turquoise "Chemically it is a hydrated phosphate of aluminum and copper" [Flood].... topaz In modern science, fluo-silicate of aluminum. As a color name from 1908.... metal an undecomposable elementary substance ha

############ ale
Origin and history of ale ale (n.) "intoxicating liquor made by malt fermentation," Old English ealu "ale, beer," from Proto-Germanic *aluth- (source also of Old Saxon alo , Old Norse öl ), which is of uncertain origin. Perhaps from a PIE root meaning "bitter" (source also of Latin alumen "alum"), or from PIE *alu-t "ale," from root *alu- , which has connotations of "sorcery, magic, possession, and intoxication" [Watkins]. The word was borrowed from Germanic into Lithuanian ( alus ) and Old Church Slavonic ( olu ). In the fifteenth century, and until the seventeenth, ale stood for the unhopped fermented malt liquor which had long been the native drink of these islands. Beer was the hopped malt liquor introduced from the Low Countries in the fifteenth century and popular first of all in the towns. By the eighteenth century, however, all malt liquor was hopped and there had been a silent mutation in the meaning of the two terms. For a time the terms became synonymous, in fact, but local habits of nomenclature still continued to perpetuate what had been a real difference: 'beer' was the malt liquor which tended to be found in towns, 'ale' was the term in general use in the country districts. [Peter Mathias, "The Brewing Industry in England," Cambridge University Press, 1959] Meaning "festival or merry-meeting at which much ale was drunk" was in Old English (see bridal ). Entries linking to ale bridal (adj.) "belonging to a bride or a wedding," c. 1200, transferred use of the noun bridal "wedding feast," from Old English brydealo "marriage feast," from bryd ealu , literally "bride ale" (see bride + ale ). The second element later was confused with suffix -al (1), especially after c. 1600. Compare scot-ale under scot (n.), provincial lamb-ale "a country feast at lamb-shearing," and Middle English scythe-ale (mid-13c.) "drinking celebration for mowers, as compensation for a particular job." Fitzedward Hall ("Modern English," 1873) noted it as a curious etymology for "a word now suggestive of no beverage less luculent than champagne or sparkling moselle." Bridal-suite is attested by 1857. ale-conner (n.) "one who tests the quality of ale," late 13c. as a surname, from ale + conner , from Old English cunnere "examiner, inspector," agent noun from cunnan "to know, know how" (see can (v.1)). alehouse alewife alum beer See All Related Words (6) Advertisement Want to re
```


## [2026-09-04T19:44:19.331Z] TOOL CALL #63: Bash

```json
{
 "command": "curl -s -A \"Mozilla/5.0\" \"https://vajehyab.com/?q=%D8%A2%D9%85%D9%84%D9%87&d=moein\" -o /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/vy1.html -w \"%{http_code}\\n\"; head -c 300 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/vy1.html"
}
```


### [2026-09-04T19:44:21.325Z] TOOL RESULT

```
200
<!doctype html>
<html lang="fa">
  <head>
    <meta charset="UTF-8" />
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="Vajehyab" />
    <link rel="preload" as="font" type="font/woff2" crossorigin="" href="/assets/fonts/estedad/Estedad-FD.woff2" />
```


## [2026-09-04T19:44:22.464Z] TOOL CALL #64: Bash

```json
{
 "command": "curl -s -A \"Mozilla/5.0\" \"https://abadis.ir/fatofa/%D8%A2%D9%85%D9%84%D9%87/\" -o /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/ab1.html -w \"%{http_code}\\n\"; python3 -c \"\nimport re,html\nt=open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/ab1.html',encoding='utf-8',errors='replace').read()\nt=re.sub(r'<script.*?</script>','',t,flags=re.S); t=re.sub(r'<style.*?</style>','',t,flags=re.S)\nt=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t); t=re.sub(r'\\s+',' ',t)\nprint(t[:3000])\n\""
}
```


### [2026-09-04T19:44:27.163Z] TOOL RESULT

```
301
 دیکشنری مترجم بپرس rd دیکشنری آبادیس آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. لینک ها حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. © 2006-2026 abadis.ir
```


## [2026-09-04T19:44:34.555Z] TOOL CALL #65: Bash

```json
{
 "command": "for w in \"%D8%A2%D9%85%D9%84%D9%87\" \"%D8%A7%D8%B1%D8%AC\" \"%D9%88%D8%B1%D8%AC\"; do echo \"########## $w\"; curl -sL -A \"Mozilla/5.0\" \"https://abadis.ir/fatofa/$w/\" | python3 -c \"\nimport sys,re,html\nt=sys.stdin.read()\nt=re.sub(r'<script.*?</script>','',t,flags=re.S); t=re.sub(r'<style.*?</style>','',t,flags=re.S)\nt=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t); t=re.sub(r'\\s+',' ',t)\ni=t.find('فرهنگ معین')\nprint(t[i-100:i+900] if i>0 else t[:1200])\n\"; echo; done"
}
```


### [2026-09-04T19:44:42.666Z] TOOL RESULT

```
########## %D8%A2%D9%85%D9%84%D9%87
شنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. لینک ها حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. © 2006-2026 abadis.ir 

########## %D8%A7%D8%B1%D8%AC
 وا قدر مقدار پایه پایگاه حد منزلت اندازه مقام اعتبار احترام . قصبه ایست از ولایت فیروز کوه طبرستان فرهنگ معین ( اَ ) (اِ. ) ارز، ارزش ، رتبه ، مقام . فرهنگ عمید ۱. ارزش، بها: کسی را که فام است و دستش تهی ست / به هر جای بی ارج و بی فرهی ست (فردوسی: ۶/۵۴۰ ). ۲. احترام، قدر. گویش مازنی /arj/ ارزش – بها مترادف ها value (اسم) مقدار، ارزش، قیمت، فرجه، بها، قدر، ارج supereminence (اسم) رفعت، علو مقام، ابر پایگی، ارج پیشنهاد کاربران ارج بمعنی ارزش از یک ریشه پیش هند و اروپایی است با همین معنی که در نمودار زیر نشان داده شده است. مقام " ارج ":ارزش. " مرج ":شرط. " مرج دانستنیها ":شرط دانستنیها. مرجها:شرطها. شرایط. ارج گذاری و بها دادن به خود ودیگران یا واژگان دیگران قاف انداختن به دیگران است. برابرواژه ها🇮🇷 ∆ ارج، ارزش، بها، تایی، سنج ∆ ارز = بها، ارج، سنج ∆ ارزش = سنجه، بها ∆ هم ارز = برابر، همتا ∆ کم ارزش = ارزان، کم بها ∆ بی ارزش = ناچیز، بی بها، نیارزش، رایگان ( مفت ) ∆ با ارزش = ارزشی، بهادار، ارجمند، ارزشمند، سپندا، زرین، پرگهر تو ای آرش کمانگیر کمان را بگیر بزن بر سر هر ترک نادان و پیر کم

########## %D9%88%D8%B1%D8%AC
 تا بقوت فیض آن بر عالمیان مهتر شود و بمدد تابش آن بر جهانیان غلبه گیرد... ) وج دارویی است اگر ترکی فرهنگ معین (وَ ) [ په . ] (اِ. ) ارزش ، ارج . فرهنگ عمید ارج، ارزش. دانشنامه عمومی ورج (وبگاه). ورج ( به انگلیسی: The Verge ) یک وبگاه روزنامه نگاری فناوری و شبکه رسانه ای آمریکایی مدیریت شده توسط وکس مدیا است. این شبکه اخبار، داستان های طولانی، کتاب های راهنما، بررسی وسایل و پادکست ها را منتشر می کند. این وبگاه از چوروس، سکوی اختصاصی وکس مدیا برای انتشار اخبار و مطالب، استفاده می کند. سردبیر این وبگاه نیلای پاتل، ویرایشگر اجرایی آن دیتر بون و کارگردان ویرایشی آن هلن هاولاک است. ورج در ۱ نوامبر ۲۰۱۱ به راه افتاد. این وبگاه پنج جایزه ویبی را در سال ۲۰۱۲ برنده شد. وبگاه رسمی wiki: ورج (وبگاه) این نوشته برگرفته از سایت ویکی پدیا می باشد، اگر نادرست یا توهین آمیز است، لطفا گزارش دهید: گزارش تخلف پیشنهاد کاربران ورج بمعنی مقام ، ارزش و مرتبه از یک ریشه پیش هند و اروپایی است بمعنی ارزش، مسیر اشتقاق آن در نمودار زیر نشان داده شده. از همین ریشه واژه های دیگری به فارسی رسیده مانند، ارزش، ارج، ارز
```


## [2026-09-04T19:44:55.343Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"arziden\\|arz '\\|arg '\\|arÄ\\|arg\\b\\|arzÄn\\|arzan\" HRN.txt | head -20; echo \"=== HUB\"; grep -n \"arz\\|arg \" HUB.txt | head -20"
}
```


### [2026-09-04T19:44:55.402Z] TOOL RESULT

```
1051:afy. yarz 'Fähigkeit, Wert*.
1443:^) Phlv. andarg ist Unsinn.
2130:aw. [/^varz- 'schaffen, tun'; phlv. varz 'Feldarbeit'
2172:aw. varekah^ (ZP61.); phlv. varg 'Blatt',
2236:(137); wa;K. vurk, siyn. varg, sar. barka,
2257:mäz. bazarg.
2268:ap. vazarka- gross*; phlv. vajarg (Bund., zu lesen
2269:vazarg), vacurg (Men., zu lesen vaziirg),
2873:pouru.mahrku' mit pnrmarg wiedergiebt, so hat er
2875:falls hätte er rasmarg übersetzen müssen.
3965:(Vullers) belegt wird, ist in unseren Texten arg ent-
4910:darg, af/. lärya gleichzusetzen ist, wie noch Geiger
7396:Kas. karg, kerk (s. v. mi(ry).
7888:Käs. var, varg, mrg\ mäz. vurg.— 203 —
7891:kurd. varg *Wolf'; afy. lüg] oss. d. beräyj t. biräy
8483:') Käs. K. dagegen kargühl *Ente*.
8489:No. 75); arm. LW. warg 'Wiese', syr. LW. n:i*1D 'Wiese'.
8499:aw. mahrkor 'Tod*; phlv. marg\cirjan^ marißh 'Tod';
8501:kurd. merk 'Tod'; bei. mark; oss. d. t. marg *Gift'
10364:70. döSak 'Freund* (vd. 1 (20)), dösak\marz 'Päderastie
=== HUB
313:liche Name fiir *Blei' ist surb, Urspriinglich gilt arzzz
314:fiir beide Metalle, indem man zwischen weissem arztz
315:= 'Zinn' und schwarzem arziz — 'Blei' unterschied.^)
316:Auch die Armenier nennen Blei schwarzes ardic, Im
851:von barzan noch vollkommen dunkel.
948:fehlt. — Dazu auch afgh. LW. buzarg *a saint, an elder,
2172:farzcLna (= phi. frazdnak) ; maltdan (von mard- aus
2173:marz) neben mitstan (von mrz) u. s. w. Oder sind auch
3255:906 ****• Das Parsenwort (!) garzmdn ^Himmel' = paz. garod^-
3583:Hierzu arm. navf 'Erdharz, Erdpech, ErdSl* (5. Jhd.),
3838:132***»- Lies phi. maikaparztrij arm. maSkaperdan (mit s fUr s),
4173:abresum *Seide', aatar 'Stern', arj, arz *Werth*, arzls 'Zinn,
4287:= arm. dehpet (EliSe) = zd. danhupaiti- ; marzban *Mark-
4288:graf, phi. marzpdn, arm. marzpan; mobad == syr. NtCSIQ
4393:arm. varz, phi. vazr^ zd. vazra-; guraz *Eber' (neben Baraz
4407:muy- in muyanandarzbad (Hoffmann, Ausziige p. 50), phi.
4550:havar *Glaube ; derjak 'Schneider, np. darzT ; kerp 'Form' =
4618:*Tiefe* zu bqjsah-); mOlfdan reiben', phi. -^tnarz, zd. marez-;
4935:arm. few, zd. ka^na-; xasln *blau8chwarz' = zd. axsa^na-;
5259:iiber , birOdar *Bruder\ barda *Gefangener , barz Teldarbeit',
```


## [2026-09-04T19:45:01.830Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4160,4190p' HUB.txt; echo \"=== leaf\"; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f'); import bisect\noff=0; starts=[]\nfor p in pages: starts.append(off); off+=p.count('\\n')+1\ni=bisect.bisect_right(starts,4172)-1\nprint('leaf',i,'printed',i-10)\nEOF"
}
```


### [2026-09-04T19:45:03.420Z] TOOL RESULT

```
g, p und b, 6 und j gerade in den alten Handschriften nicht
unterscheidet, theils weil die noch in den ersten Anfangen
steckende persische Philologie die nOthigen Vorarbeiten
(kritische Texte, Glossarien, Foniiensammlungen , Unter-
suchungen iiber die Reime der Dichter, die heutigen Dialekte
u. s. w.), von einigen wenigen sehr dankenswerthen abge-
sehen, noch nicht geliefert hat.
*) Ueber den Unterschied zwischen Iranisch-Persisoh und Indisch-
Persisch vgl. Blochmann, JASB. XXXVII, 1, 34-38.Kapitel 1: ap. a.
§ L Ap. a (= idg. a, e, o, ^, j^ u. s. w.) bleibt im
Np. als a, z. B. banda *Sklave, Diener =^ ap. handaka-,
§ 2. Im Anlaut erhielt sich a im Mittelpersischen,
ebenso im Neup. vor Doppelkonsonanten: ahr 'Wolke*,
abresum *Seide', aatar 'Stern', arj, arz *Werth*, arzls 'Zinn,
Blei\ ars *Thrane*, asp Tferd', ast *ist', angust Tinger ')
u. s. w., wahrend anlautendes a vor einfachen Konsonanten
im Neup. niir in einsilbigen (mp. ein-, ap. zweisilbigen)
Wortern blieb: am *ich bin = ap. amiy; az *aus', paz. az,
phi. a6 = ap. haca, sonst aber (in mp. Zwei- oder Mehr-
silblern) abfiel^):
be- *ohne* in Komp. = paz. awe-, phi. ape-, arm. ape-,
api^; beza, veza Vein' = paz. awUa Shk. 235, phi. apejak
oder opecak?; burna 'Jiingling' = paz. awarnai Shk. 238,
phi. apurnai, apurnayak, zd. aperendyu-, aperenayuka- ;
baxtar^)=^fsiz, awaxtar, phi. apaxtar, zd. apaxtara- *nord-
^) Yon diesem a ist das vorgeschlagene a (abiii 'Augenbraue*
= skr. bhru') zu unterschoiden.
*) Ueber afrOxtan = furoxtatt, afzudau = fuzudan u. s. w.
siehe unten.
') Naoh Vullers = 1) Weston, 2) Osten, aber (nach N61-
deke^s Mittheilung) beiMasHdl, hitab at tanhlh ed.de Goeje p. 31
=== leaf
leaf 126 printed 116
```


## [2026-09-04T19:45:10.137Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD\"; grep -n \"^arz\\|^arž\\|^warz\\|^warc\\|^arzān\\|^arzan\" PHD.txt | head -20; echo \"=== NYB\"; grep -n \"^arz\\|^warz\\|^warc\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-04T19:45:10.204Z] TOOL RESULT

```
=== PHD
216:arzómand I2 āsūdan
217:arzómand [le wmnd | (N arjumand)] valuable, worthy. ~ih: value, worth. Arzür []zwl] a demon; a mountain at the mouth of hell. a-sag [?s?*k! | M *s?g] innumerable, countless. азап Pon! | N ~] at rest, easy, peaceful. “АП: rest, ease, peace. a-sar Dell endless. āsāy-, ~išn, v. āsūdan. a-sazāģ ["sc? k!] unfitting, unsuitable. a-sazisn|ig Dscfn-yk'] imperishable, permanent. ~ih: imperishability, permanence. a-sēj [Psyc] free from danger.
608:warz- 88 waxsig
609:warz-, —išn, v. warzidan.
610:warzag [ic k! | (N zvarzāw)] ploughing (ox).
611:warzāwand [wle'wnd | M wrewynd] having miraculous power, powerful.
612:warz-büm [wlcbwm] cultivated land.
613:warzidan, warz- [wlc-ytn' | N ~] work, act, practise; till; beget. ~išn: work, tillage.
614:warzigar [wlcykl | M zorzygr, N barzigar] worker, peasant.
=== NYB
6375:arzani: aržanik arzmand: aržomand ārzū: aržok
6376:arza: arž
7010:arzàn: aržānīk
```


## [2026-09-04T19:45:19.198Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"arž\" NYB_vol2_glossary.txt | head -20; echo \"=== warz in NYB\"; grep -n \"warč\\|warz \\|warz,\" NYB_vol2_glossary.txt | head -10; echo \"=== PHD warz noun\"; grep -n \"warz \\[\" PHD.txt PHD_mackenzie.txt | head"
}
```


### [2026-09-04T19:45:19.267Z] TOOL RESULT

```
505:lapar [’pl; MDM, v. 2apar] adj. situated above, lying above: évak ~, apäk dit, v.s.v. žapāk (2); — heavenly, often in compounds: apar-apükeh etc., v. below; comp. ~-tar [’pltl] higher 5426, 581°, highest 1097; sup. ~-tom highest 415. 102°; v. also apartaréh; — adv. empha- sizing an adj.: highly, extremely: apar- aržānīk, v. aržānīk. — Av. (393) upara-, adv. upara (instr.), uparam; MPrth ’br adj. and adv. (MHC), comp. ’brdr, sup. ’brdwm; Ps. ?pldl; Paz. awartar, awardar (SGV); NP bar ‘height, top, summit’, bartar ‘higher’. ?apar [MDM, erroneous reading of OAram QDM] 1. adv. above: (3 päs) i-m guft ~ of which I spoke above 65°; či nümak" cé hac ~ nipišt" éstat the inscription that had been written here above P2:3, cf hacapar; — prev. over, on, upon, up, or simply expressing the initiation of the action, with varying vbs., cf esp. (@)ma- tan, burtan, grätan, raftan, rasitan ; follow- ed by enclitics: apar-p-im ravišn I must needs ascend 4076, v.s.v. -p(i); — refer- ring back to an encl. pron.: api-š Vidrafš . ~ mšast and V. got on it (the horse) 25W5; cē-t avdom margéh ~ raset for at the end Death will come upon thee 726-7; (martömän) tāi-šān āmēcišn ~ nē barend as long as one does not impart instruction to them 801. — 2. prep. a) local: over, on, on to, down on: Krisäsp ~ én damik raset K. is roaming all over this earth 3318; ~ giyāk on the spot 3", 102; ~ ki Zartuxst bé dahém where we shall deposit Z. 3957; ~ pad ēstāt rose to his feet 1821; asp ... — rahy vartét harness the horse! 5418-14; srišk ~ srišk drop after drop 214
654:aržanik
664:arž ['le'] value, merit 674. — Av. (192) arajah-; Paz. arža (SGV); NP arj, arz.
665:aržānīk [’le’nyk] worthy 119°; apar-~ exceedingly worthy 924, v.s. v. 'apar. — Paz. arzani; derived from arž through the intermediate adj. aržān ‘worthy’, Ps. len; MPrth ?r2n (S); MPrs 'rz'n (A-H II); Arm. lw. aréan ‘worth(y)’, also
667:aržānīk
671:aržānīkēnītan [~-ynytn'] to consider a p. worthy, governing a subordinated clause without an introducing particle, 5318 in a very complicated passage 5317-21, which only seems possible to understand on the following suppositions: a) kū-t bahr hac man bé burt l. 19 is not a gloss, as I have marked it, but is governed by anak tč bavat l. 17 ‘it shall be unhappy for thee that thou hast bereft ...'; b) the clause kē ... aržānīkēnīt hom 1.17-19 is loosely attached to tē l.17; c) for MNW-t L<y> (MS very clearly MNWtl) read MNW kw) LY» = kē tē man, to man being the exact counterpart of LK ^NH = tč an (v. žan) 1. 19 and both signifying ‘thou and I’; d) YBLWN-m l. 18 and 20, and HWH'-m 1. 19, are the Ist. p. pl. coinciding with the Ist p. sg.; e) there is a wordplay between *š = dé ‘food’ l. 18 and ’$ = as (demonic) eye’ 1. 20 (as burtan 'to have a vision', v. 'aš; bahr ‘ministry’, v. this w.). Text: anàk tč bavat, marak, ke t(0» man fratom hac ax" i astomand andar Rdg u Notar hac bahr barišneh āš barom frac aržānīkēnīt hom, kū-t bakr hac man bē burt. niin-ip tē an pat apar-barišneh aš barom u et bavēt kū-t dušcašmiha al zänak nikēram i-t nest ‘unhappy shall it be for thee, little scoundrel, (that thou) — as thou and I first of all men in the material world between Räg and Notar have been found worthy of earning food by perfor- mance of ministry — that thou hast bereft me of the ministry. Now thou and I shall be enraptured in an ecstatic vision, and then it will happen that I shall see thee evil-minded in another house that is not thine’. The passage is the immediate continuation of the incident related in 537-15, Zsprm XII, 7 epitomizes 5316-21 as follows: dwlyslwb BR’ L zltwšt gwpt' "VK cygwnt pltwm HWH'-m b’hl wlweyk BR’ ’pknd HWH'-m ZK tw "NH KR?
673:aržok ['lewk'] desire, lust 65’, 664. — Paz. ārzū; MPrth ’wrjwg (A-H III, MHC), "wrwg (MHC); MPrs ’wrzwg; NP ārzū.
674:aržomand [’le’wmnd] worthy, dignified 311. 4715; precious, excellent, comp. —-tar 879. — Paz. arzmand (Mx), arzamand (SGV); NP arjmand.
726:taš ['š] eye, of demonic beings 3118; ~ burtan to carry one’s eye (sight) far away = to have a vision of distant and hidden things 51-53, of the. pre-Zoro- astrian seers, v. also apar-barišneh and ef s. v. aržānīkēnītan.
729:v.s. v. aržānīkēnītan. — NP ä$ ‘meat, soup, broth'; cannot be identified with
895:bahr [b’hl] lot, share, portion 692°. 9019.11; (the part played by the priest in the service =) ministry 5319-1? (v.s. v. arzä- nikénitan), a synonym of yazisn (q. v.); this sense is confirmed by Zsprm XII, 6: Pourusäsp bahr o öi hilāi ke-š patiš aržānīkēh ‘P. shall leave the bahr to the one who has the qualification for it’, corresponding to (Pourusäsp...) yazišn 6 yastärän *hārēfūt (v. hareftan), with the gl. kū 6 yazāt kē apāyet yaštan 5314-15; — happiness, prosperity: tan ~ bodily beauty 22%, — Av. (923) baxadra-; Ps bhly; MPrth bhr ’*ate’; MPrs bhr (A-H I), h’mbhr "having the same share’ (A-H II); Paz. bahar, Skr. v. vibhäga and samrddhi; NP barx. [It would be tempt- ing to connect (čan) bahr with Skr bhadra- ‘beautiful, happy’; phonetically there is no difficulty, cf Skr mudrā: muhr ‘seal’ ; Av. baóra- is attested in hu-baóra- (1828) ‘happy’; thus Bailey in A. M., N.S. IT: 1, 1952, 32].
927:barišnēh det. v. n. of burtan: the act of carrying or bringing: & gobišn ~ this "saying-bringing" = such a message conveyed to me (by a mysterious voice) 3812-18; bahr ~ performance of sacer- dotal ministry 53%, v. aržanikenitan and bahr. ~ V. also apar-barišneh and frot- barišnčh.
1220:dāštan [d'štn'] dār- [YHSNN-; d'1- 217. 281. 10014. 10279], imp. sg. with encl. pron. där:om [YHSNN-m] 6t; opt. 2nd p. sg. dārēš 41!?; pt. dašt = pret. pass. 3d p. sg., construed as an act. form 495-5; to keep, to hold, to sustain, to maintain, to have, 8?! and passim; — with an adj. as a complement of the obj.: Sahpuhr kanicak āžarmīk u garamik däst Š. kept the girl honoured and respected 163-4; 225 ete. passim; the complement some- times comes near to an adv., e. g. véh ~ to keep, handle a th. well 5026-27, and may be replaced by an adv.: én zan garämikihä ddr 1024; 6415; — with an obj. and pat + an adj.: to consider a p. or a th. to be ...: pat margaržān ~ to consider a p. guilty of death 1014-19; 6398-9, 8017, 839-19; pat azateh (cas. obl. sg.) där-om! consider me as a free (wom- an) — release me (from slavery)! 64, v. s. v. Gzat; — pat & ~ ku to be of the opinion that, to think, imagine that 2525, 982-3, 3227 sq. 5012-13, ef NP pindāštan < *pa(t) én daštan; pat ce dārēh how do you regard (the case mentioned in the preceding kū- clause)? 105-$; pat depahr, pat nihän
1385:duš-cašmiha in, the state of being evil- minded 53%, v.s. v. aržānīkēnītan.
1426:3.8 [the figure l; -’y, -y, -yh] the enel. indef. art.: tigr-é [-1] 339; duxt-ē [BRTH- ^y] 14%; gad-ē [gt'-”y] one stroke with the mace 312°, 4 ēvak-ē [HD-wk!-y] one fourth 998; vāt-ē [-1] 4 hubod 73°; hec ctš-ē [-l] nö 16%; har kas-ē PYS-1] 10018; and cand yašt-ē [-1] 651°; pat har 40 sal hac zan-ē u mart-é frazand-é [al -ē's spelt -1] zāyēt every forthieth year a child is born of a woman and a man (= of one couple) 8622-23; 6 artestäreh for 6 artēštār-ē 4517. — Identical with ?e; MPrs ‘yw placed after its subst.; Paz. -é, NP -é. — The spelling [-1] is sometimes erroneously used for other suffixes -é: mēd4-1 = mode cas. obl. 72??; har marg- arzanik+-1 = -aržānīkē for the abstr. -arzanikéh 10199.
1582:fražām [ple’m] end 804. 81!; pat ~ lastly, in the end 645.721, 7212-5; ~~ pērē- zēh the final victory 77?” sq. — From the preceding vb.; Paz. farjam, faržam; NP farjam.
1709:griftar [glpt’]] a p. who "catches”, i.e. incurs, liability: 1. ku pat dat 1 dévan ~ né bavé lest thou shouldst be subject to the law of the demons 6916-17; [ruvan pat ménoyan pat kunišn aržānīkēh ~ kunénd in the heavenly world they (the gods) call the soul to account according to the value of her deeds Mx ch. 382-6 (~ kunénd = girénd 65°, v. griftan)]. — 2. condemned to (šahrē-karān, v. s. v. kar) 92; prisoner: ~ kartan to imprison, to capture 615; [more general, to catch hold of: api-§ — kunēt u apāc 6 rah i yazdān āvarēt Mx ch. 1525]. — Cf NP gér?ftàr; v. also a-griftär.
2127:kart ēstēt, cigön Dahäk u Frāsyāp u Väman [thus Cod. DH; TD w’tn', Paz. vätan, perhaps for Väöarjä the father of Vaman, Tab. I, 530 init.] u apārīk hac én āivēnak marg-aržānān, pātifrās [+ Paz. vama, probably a misspelt Vaman] 10 ātvēnak-ic vitārēnd ‘those who have in- stituted their own *laws for mankind, as D. and F. and V. and other death deserving men of that kind, will undergo ten sorts of punishment’. For the whole passage cf Phl Vd ad 75? (p. 279).
2445:opp.) druvandän kē né pat ~ druvand būt ésténd evil men who have become evil, though not by deadly sins 101. — V. aržānāk.
2446:marg-aržānīkē [~-yk+1] deadly sin 101, — Cf the spelling mlgle’n'+1 = marg-arzané(h) in the commentary to Vd. 73? (p. 27799).
=== warz in NYB
3767:*Tavvak [twpk'] a town 11616, — Cat. 94; Schwarz, Iran II, 66 sgg.; Yäqüt 1,890sg.; Arab Tawwaj, Gr Toxn, Tadxn; as to -wp- for -v- cf s. v. āstavān.
4790:Schwarz, Iran = Paul Schwarz, Iran im Mittelalter nach den arabischen Geographen. 9 Bde, 1896-1969. In einem Band Hildesheim-New York 1969 + Ergánzungsband 1970. 4
6414:awarč: apärik
=== PHD warz noun
PHD.txt:323:2ēraxtan, ёгапј- Pylhtn', *ylnc- | M ‘yrxt, ( yrnz-)] fight, dispute. éraxtür [y/At? 1] warrior. ēr-kaš ['dik£ | M *yrkš] (hands under the armpits in respectful) salutation, greeting. 1ërmán [?y/mx! | (MÉÁry! mwn), N ~] friend; а god. — ih: friendship. 23ër-man(ag) ['dim?n(k)'] humble. ēr-menišnīh [dimyninyh] humility. ér-tan ['ditn!'] humble. ~ih: humility. ērwār [D yleo?1] befitting a hero. ērwāraģ [*dlw?Ik! | J ?rw’rh] jaw, cheek. ésm ['ysm] = ézm. esp", v. sp”. éstádan, ést- [YKOYMWN-tn! < A ygym, У gum; ?sttn!, *zost- tn! | M ‘yst-’dn, N ~] stand; be, continue (as auxiliary of the perfect con- tinuous tense). ~išn: permanence, lasting, dwelling. ēš Pys | N xéf] plough. efm, v. $n. &(w) [z; HD < A hd | M ‘yw, N -ēļ a, one. éwan [*dwn') stalk, trunk. ēwān ['dw?n!] bridle. éwar ру! | J ?yf?r] certain(ly), assured(ly). éwarz [dwlc] movement. éwarzidan, éwarz- ['dwlc-ytn!] move, travel. éwarzig ['dwlcyk!] moving. 1&wáüz [?уш?с] word, utterance. tēwāz [?уш?с] sole, only. ~ig [-yk'] particular, individual. čw-bār Duech?) once. ē(w)-čand D у(то)спа] some, a few. éwén Pdwyn' | M *ywyn, (N àyin)] manner, custom, form, propriety. pad —: properly. léwénag ['dwynk! | M *ywyng] = ëwën ; v. ёё-. Ў *éwénag [?*dwynk! | (N āyīna)] mirror. Set (ъд) yn k éw-kard(ag) ['ywkrt(k)', -kltk'] united, joined. ē(w)-mēg D»(zo)mtok!] wearing (only) one shoe. éw-sün Pywsn' | (N yak-sān)] uniform, (a)like. ^ Ah : uniformity, likeness. éw-tüg Pywt?k' | М ‘yw 12, (N yaktà)] alone, single, individual. éz-, v. yaz-. —išn [уст] worship. ézm [CY BA < A syb | N hëzum] firewood, fuel. ged Zm4
PHD.txt:607:~išn: conquest, destruction. wanigarih [4W BDN-, wny-klyh] waste. wany [A(W)BDN' < APbdn | M wny] lost, destroyed. wany(b)ūdīh [4WBDN'butyh, -YHWWNtyh | M wny(b)wdyh] destruction, ruination. iwar [wl | M wr, N bar] breast. *war [w/] lake. Zwar [wl] oath, ordeal. ‘war [wl] shelter, enclosure. war-, v. waridan. warāy [wl”g | J bry] crow. waran [win'] desire, lust. warān [wi’n'] ram. wārān [w’Pn' | M wrn, N bārān] rain. waranig [wlnyk'] greedy. ~ih: greed, lust. waranig [wL nyk! | N bārānī) rain(y). warāz [wl”c | N gurāz] boar. war-čašm [wicfm] with eye(s) in the breast. ward-, v. 'waštan. lwardag [witk! | M wrdg, N barda] captive, prisoner. ~ih: captivity. *warda$ [witk'] on heat (female animal). ~ih: heat. *wardānāģ (wi? mk! | N gardana] (roasting) spit. wardénidan, wardén- [wityn-ytn! | (N gardànidan)] cause to turn; change, alter. wardišn [witšn! | M wrdyšn, N дака] turning, change, metamorphosis. ~ig [-y%!] transient, changeable. ~(ig)ih : transience, mutability. wardyün [wltywn! | P wrdywn, N gardiin] vehicle, carriage, chariot. warg [wlg | N barg] leaf. wārīdan, wār- [w?l-ytn' | M w’r-yst, N bàáridan] rain. warišn [wilsn'] conduct, behaviour. lwarm [wlm | N barm] memory. — kardan: learn by heart, memorize. *warm [wim | N barm] pool, reservoir. wārom [w’lwm] mind. warómand [wl’wmnd] doubtful. ih: doubt. warr [LBWS Y A < A lbw?] wool; garment. warrag [КММА < ?; wlk! | M wrg, N barra] lamb, ram; astr. Aries. wars [wils] hair. lwarz [wle | M wrz, N barz] work, agriculture. *warz [wic | М wrc/z] miracle, miraculous power. *warz [wlz | N gurz] club, mace.
PHD_mackenzie.txt:5217:lwarz [wlc I M wrz, N harz] work, agriculture.
PHD_mackenzie.txt:5218:lIwarz [wlc I M wrc/z] miracle, miraculous power.
PHD_mackenzie.txt:5219:3warz [wlz I N gurz] club, mace.
```


## [2026-09-04T19:45:33.341Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f'); import bisect\noff=0; starts=[]\nfor p in pages: starts.append(off); off+=p.count('\\n')+1\nfor ln in (664,674,611):\n    i=bisect.bisect_right(starts,ln-1)-1\n    print('line',ln,'leaf',i,'printed',i-8)\nEOF\necho \"=== KNT arjana\"; grep -n -i \"arjana\\|arja\" KNT.txt | head -10\necho \"=== IEC algwh\"; grep -n \"^alg\\|algʷ\\|alg\\\"\" IEC.txt | head -5\necho \"=== WLD Bd1 p91\"; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\np=pages[99]  # printed = leaf(1-based) - 9 -> printed 91 = leaf 100 (1-based) = index 99\nprint(p[:2500])\nEOF"
}
```


### [2026-09-04T19:45:35.333Z] TOOL RESULT

```
line 664 leaf 38 printed 30
line 674 leaf 39 printed 31
line 611 leaf 36 printed 28
=== KNT arjana
601:Adequate cognates lacking: arjanam, barmiš. §35. OLD PERSIAN ar BEFORE у AND v. In this
1807:Expressing concretes: arja-na-, fem. stü-nà-, fem. hai-nà-.
3072:I. The enclitic pronouns are attached to the first word of their sentence or clause or phrase, even though this be шй ‘and’: DB 1.25 Aura- mazdü-maty upastém frabara ‘Ahuramazda bore me aid’; РР} 8 tya-mary Auramazdà frübara ‘(the kingdom) which Ahuramazda conferred upon me’; DPh 9f тат Auramazdà pütuy utä-maiy ийат ‘me may Ahuramazda protect, and my royal house’. But the phrase vašnā Auramazdaha does not count in fixing the position of an enclitic: DB 1.13f vaina Auramazdàha адат-&ат х$йуабтуа Gham ‘by the favor of Ahuramazda I was king of them’; except in two partly restored passages, see under IIT. An enclitic in a dependent clause is sometimes attached to wd preceding a conjunc- tion or relative: DB 4.781 utd-tazy yàvà tauma ahatiy ‘and as long as strength shall be unto thee’; XPa 15 ша-тату tya рий akunaus ‘and what my father built’, but also XPa 19f шй tya-maiy pica kartam ‘and what was built by my father’; DNb 28f yabd-maiy tya kartam vatnühy ‘when thou shalt see what was built by me’. An attributive en- clitic genitive normally precedes the word which it modifies (cf. §309); but the meaning sometimes governs the position, as in Аа 3 apan?yüka-ma ‘my grandfather’s grandfather’, A*Sa 4 [n*yd|kama (for -am-ma, §138.1) ‘my grandfather’, both with am for -miy = -maiy (852.D. The abl. -ma is found only in hacd-ma ‘from me’, standing any- where in its clause. These formulations are vio- lated in three heavily restored passages, but the available space and the other versions favor these restorations: DSf 20 [ava исйтатату ( = -am-maty) akunaus} ‘that he made successful for me’; DSf 28 [hacd-cily ditradasa [arjanam-sary abariya) from afar its ornamentation was brought’; DNb 54f tya partalm-taty as]fiy ‘what is eommunicated to thee’ (this restoration is highly conjectural).
3955:2 hadá : Капа: Sa|kàm KT; Аоба : karla : Sa(kà Hinz; pasüva : hadja : Мата Kent. * (афту : Saka Kent, for Hinz's [abiy : avā (quoting Wb. for avd). ?* tyaiy : zauda|m Oppert. ? pa[sava : ya6à : adam : abna}ty Hinz (quoting Wb. for pasáva : ya6à). !* * ava[rasam : азд : hada : karja Hinz. ** ... бау : av]àjanam KT; Sak(á : avjajanam Tm. Lex.; разбза : adam :] Sak[a : vasiy :]
5059:arjana- sb. ‘ornamentation’, as shown by АКК. : si-im-ma-nu-u ‘decoration’ (§84, §126, 8147.1): for meaning, see JAOS 51.208, 53.13, 53.19, Schaeder, Arch. Anz. 47.272-4, against Hz.’s ‘lime- stone’ (AMI 3.52-3) and ‘building material’ (ApI 88-93). Cf. Av. pres. arga- ‘be worth’, Skt. árhati, and Ars. РЫ, arzün, NPers. arzün, Av. arojah- ‘worth, value’, Skt. argha-. — arjanam nsn. DSI 41f; arjanam-Sary DSf 23°.
=== IEC algwh
432:algà (?) “a rambling plant’. See alga Lat. (ambig.) alga ‘seaweed’; Li. alga speed. well
433:algeið (?al8-) ‘suffer’. Cf. ale-, sulĝ-. Gk. (ambig.) aigéo; Lat. algeo; Fris. alkje ‘whine, shout
434:alguhos, à “profit, wealth, value, wage’. WP I, 92 Skt. argháh; Av. arojo; Per. arz, arj; Oss. ar£, pl. ärğtä; Hitt. (queried) halkw-essar "offer. ing'?; Myc. cf. name Aqato- (*Alqwhastos = Alphéstos); Gk. alphé; Li. algà. (The form of W elw, pl.- oedd “profit, goods’ is obscure. Perh. a crossing of *alguh- and *selu, q. v.)
435:alga ^a rambling plant, tangle’. Cf. WP I, 153, and alga above Per. raz ‘vine’; Lat. (ambig.) alga; G Alche *short-stemmed vetch or sim. plant’; OCS loza ‘vine’
=== WLD Bd1 p91
895
                                             alu-   — alg“h-                                    91


      Hochst unsicher.     Wenn osk. *allo- als Lehnwort aus dem Lat. gelten
       konnte al(i)um wegen des starken Geruchs als *an-slo- zu *an-
diirfte,
„hauchen, atmen“ gehoren. S. nock Yf. LEWb. 2 26.


alu- „bitter, Bier, Alaun“.
  Gr. dlvd(o)i/uov‘ tuxqov naoa Xdxpqovi Hes., dlvdjualveiv [my.oalvuv ? Hes.
                                                                            '
                                                                                            j




(s. aber zur Bed. Heerwerden Lex. Graec. suppl. 45), lat. aliita „Alaun-
leder“ beruht formell auf einem Verbum *aluio „behandle mit Alaun“ (Ost-
hoff IF. 20, 181 ff., Thurneysen IP. 21, 175), vielleicht aucb aliimen „Alaun“,
wenn dieses nicbt einfach Erweiterung von *alu- ist.
      Die Wurzel erscheint          in    Nordeuropa mit der Bedeutung „Bier, Met“
(zu der Bedeutungsdifferenz vergleiehe ksl. Jcvasz „Alaun, Bier“);                      altn. ol n.

,,Bier,    Trinkgelage“, qldr n. „Trinkgelage“ (* alupra ), ags. ealop ealo n.,     ,
                                                                                                as.

in alo-fat,    mhd. in nl-schaf „TrinkgefaB“.
   Apr. alu n. „Met“, lit. alas (m. geworden wie mediis     preuB. meddo        —
ntr. J. Schmidt, Pluralbild. 180), ksl. oh (m. geworden wie medi) „Bier“.
Aus dem lit. ist finn. olut „Bier“ entlehnt (anders Kuhn KZ. 35, 313).                          Da
germ. bait. si. neben einem Dentalstamm ein vokalisch schlieBender Stamm
alu- auftritt, andrerseits ein auslautender Dental abfallen muBte, schlieBt
J. Schmidt aaO., daB wir es mit einem Dentalstamm zu tun haben, der
durch falsche Analogie in die M-Deklination gedrungen ist. Zum Sach-
lichen vgl. Schrader, Reallexikon 2                 1   42 f.   Kuhn aaO.   Naeh Senn Lehnw.
Studien 47 sind die        bsl. u.        finn.   Worter germ. Lw.


algh- „Frost, Kalte“.
   Lat. algor „Frost, Kalte“; algeo, ere „frieren“; algidus „kalt“ gehort nach
Liden, Studien z. ai. und vgl. Sprachgesch. 66 zu aisl. gen. sg. elgiar, nisi.
elgtir m. „Schneegestober, das von einer Seite her lange fortdauert und
von starkem Frost begleitet ist, halbgeschmolzener Schnee, deep pools of
half-melted ice“.    Germ. s-Stamm             deckt sicli mit lat. algor, idg.
*alghes-.   Altere unrichtige Zusammenstellungen mit lat. algor usw. von
 Liden aaO. zuriickgewiesen.


 a
```


## [2026-09-04T19:45:56.487Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[100][:2000])\nEOF"
}
```


## [2026-09-04T19:45:57.519Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[160]\nprint(p[:1800])\nEOF"
}
```


### [2026-09-04T19:45:58.016Z] TOOL RESULT

```
92                                             aldh-     — albho-
aldh- „Trog; Welle".
     Altn. ahla f. „Welle, Wellental"; norw. dial, olda f. „Trog“; sehwed. dial.
                                                                                            11
alia „langlicke Yertiefung".                Ygl. ags. ealdop, cddot , aldaht „Trog, Bottich                      .



Bair, alclen „Ackerfurche“.
  Zu vergleiehen ist ksl. Jadija, ahdija f. „Kahn“ (daraus lit. eldija f.
„Flu£lkahn“ nach Mikkola IA. 21, 86, auch lit. eldijUle „Raucherpfanne“).
  Ygl. Liden Blandade sprakhist. bidrag I 2ff. (u. Holthausen Anglia Beibl.
15, 71).       Hier wird lat. alv(e)us (aus *aldhouoti) hinzugestellt, was lautlich
nicbt iiberzeugend      ist (vgl. u. mdo-s). Weitere Beziehung zu alo aX&aivco.                    ,


ganz abzulehnen.                S. Yf.   LEWb. 2 30f.
      Norw. lodje „russisches Fahrzeug", scbwed. lodja. mnd. lod(d)ie, loddige
ist    aus russ. lodbja (= asl. ladija ) entlebnt. Falk-Torp 652 (s. auch 789
          r
unter olde ’).


alp- „klein“.
      Ai. (tlpa-,   (dpalca- „klein, gering"               (   alplna , a Ip at „leicht, schnell“);         lit.

                                    ohnmachtig werden“, rtJpnas „schwach“.
alpstii, alpau , atpti „verschmachten,
      Anreihung auch von hom. aXanadvog (bei Aeschylos anadvog) „schwach“,       7.


dlana^co „leere aus, ersehopfe", att. Xand'po „plundere‘‘, Xanaixco „leere
(den Leib) aus“ ist bedenklich wegen ihrer zweisilbigen Wzform gegen-
tiber der leichten der ai. und lit. Worte; auch stehn sie, sowie die ihnen
anzureihenden Ian aoog „schraachtig, diinn, offenen Leib habend“, Xanaoa
„Flanke, Dimming des Leibes an der Hufte“, Xdnu&og „Aushohlung, Grube“,
Xana&og „Sauerampfer“                  y.evconxrf' in der Bedeutungsfarbung
                                         als „fioxav7]
(„ausleeren, eingefallen") doch erheblich ab. Ganz fragwiirdig auch alb.
(Jokl SBAk. Wien lb 8, I 48) Vaps „bin miid
```


### [2026-09-04T19:45:59.635Z] TOOL RESULT

```
                                                                                                                               cyw (yw

 95

                                                                                GMS 1571, 1580; BBB 545
 2387 'spwrn'k M                                                  JJf
      ospurne                                                             2401 cyjn M                               j.jj U^li
      complete, perfect                                                        worthy©<*arjyan~; Av. ar9ja-y Parth. arzan\ MP
                                                                               ezan
      GMS 99.513, 982                                                            arzdn ^yzn, }yzn, 'yscWy
 2388 'spwrnk'rky'h M                                             JUT
      ospurn-karakya                                                            GMS 155, 383; BBB p93
      perfection                                                          2402 'yjn'wyCy) M                                    ^<J<}J
      Hen. AM 1952, 206.17                                                     ezanawe
                                                                               value, price
 2389 'spwrnw        M                                       SwT<J^r
                                                                               GMS 290, 1082
       ospurnu =>pwn*
       completely
                                                                          2403 'yjndy    M =» >yzndy, 'yznty
       GMS 513;BBBf53
                                                                          2404 (ym M =4 >ym\ >ym(,), Y-1
2390 'spwrny'k M                           U^-t <JLT                      2405 (ymy6 M
```


## [2026-09-04T19:46:08.491Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[99][2400:5200])\nEOF"
}
```


### [2026-09-04T19:46:10.287Z] TOOL RESULT

```
s-.   Altere unrichtige Zusammenstellungen mit lat. algor usw. von
 Liden aaO. zuriickgewiesen.


 algSh- „verdienen, Gegenwert“.
      Ai. arjiati „ist wert, verdient, ist verpflichtet, soil", arghd-h „Wert, Gel-
tung, Preis“       (= osset. ary „Preis, Wert“), av. arojaiti „ist wert, kommt an
 Wert gleich" (npers. arzidan „verdienen“), arojah- (es-St.) n. „Wert, Preis“.
       Gr. d/.cft'j „Erwerb“   =   lit.   alga, apr. gen. sg. idgas „Lohn", dlcfdrm, dig sir
 „einbringen, verdienen" ( dlrpeiv           =    ai. drhati, aber durch das vollere    Praes. dl-
 <fdvco in die Geltung als Aorist gedrangt), dlgpEoifloiog „Rinder einbringend".
      de SaussureMem. 277 A, 2, Froehde BB. 3, 12, Fick I 4 5, 170, 356.
      Arm. yargem chre, schatze" (Hiibschmann Arm. Gr. 1 477) muB wegen
                       ,




 seines r iranisches Lehnwort sein (Pedersen KZ. 36, 76).                       Lit. elgiuos, elgtis
 „sich betragen" wird          wegen der groBen Bedeutungsverschiedenheit besser
 ferngehalten    (s. Leskien Abl. 362):

       Eine Kebenform auf Media ist ai. arjati „erwirbt, verdient, schafft herbei".
```


## [2026-09-04T19:46:20.598Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF\"; grep -n \"ارجاسپ\\|ارجاسب\\|ورج\" FSF.txt | head -10; echo \"=== FRS\"; grep -n \"ارج\\|ورج\" FRS.txt | head -10; echo \"=== ARY latin\"; grep -n -i \"ARJ\\|ARZ\\|ALUM\\|AMLA\" incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-04T19:46:20.694Z] TOOL RESULT

```
=== FSF
975:ارجاسب به اسفندیار که به‌صورت 
1491:جاماسپ» هنگام جنگ ارجاسپ با 
3736:(ارجاسب به سپاهیان خود گوید: هر کس 
7048:(ارجاسپ به سپاهیان خود گوید: هر کس 
8767:در جنگ گشتاسپ با ارجاسپ. زریر به 
8769:ارجاسپ به سپاهیان خود می‌گوید هر 
10645:ارجاسپ به گشتاسپ نامه نوشته و او را هدید 
13800:فرشیدورد در جنگ با ارجاسپ زخم 
14105:در داستان جنگ کستاسیت با ارجاسپ. 
14107:ارجاسپ: 
=== FRS
40:بی‌مانند بگانه دوست ارجند آقای اقبال است که تخضص و تبخر شخصی 
52:مخدوم گر امی‌ودوست عز یز ارجند حطرت آقای | قا سید عبدالر حیم خاخالی 
599:لعف ومساعدتهای گرانبهای صدیق فاضل ارجند آ قای سعید نقیسی 
962:شنا کر باشد درآپ . . ۲ س :ز آب ارجو آتش بترسد رواست . ع ون 
1330:(ست اشدس ید۹ نودر قبا و بت ارجا 
1684:چهار گوهرم اندر چهارجای مدام۸ 
2061:کرد پر کار چرخ مر کز بست شبه مم جان شد و بلورجمست ۲] 
3323:غارج* 
3324:خیوح باشد و غارجی صبوحی ۳ شا کربخاری ۱ گوید: 
3325:خوشا نبید " غارجی با دوستان يك دله 
=== ARY latin
298:BARZ (guy! BHURIA 4 Sle (e0lé1 uw 8) BHERGO colyy I y 22 Gofly Se
2205:ERG, ARKA, (SANSKRIT) 2 Sit ARJ (PAHLAVI) 53h,
2217:ARZ, ARZESH, ARZIDAN Gaz zt oti yl Gy! (PERSIAN) gu jb
2221:‘REFERENCES cathy ARZ, ARZIDAN, (PAHLAVI) 5
2222:POKORNY: 32-33 ARZISHN
2232:ARZIZ (pid o Ki g sass 5" al'A a) jay! (PERSIAN) upd
2236:ARKWI (TOKHARIAN B) B 555 ARZIZ, ARZIZEN (PAHLAVI) 6 ky
2240:ARJUNAH, (SANSKRIT) cy Suite
3030:PARKUS HITTITE) esa BARJR, BERJ. — (ARMENIAN) «5!
3081:‘WARZA «(OLD SCANDINAVIAN), AS Ele!
3082:WARZE (GERMAN) glalT VARTA
3411:FOIA gens antic BARBARZYNCA (POLISH) gt)
3453:BERJ, BARJR (ARMENIAN) gs)
4950:FARJAN PEL, PURD, PIRD, PIR
5546:BARNHART: (TERROR) 1127 ‘TARJATI, TRASATI, TRASA-
6748:OLD CHURCH SLACIC) 25 5 3%! KARCANG, KARZANG
7138:vay sebi iby SWARZ.
7813:DARH- SANSKRIT) Gy Sikes DARZ PAHLAVD 65 hy,
7828:seal gt IG chlo 9% 4 DARZIG Gsr5ly hy Obj 22-1
9905:FELCH GAELIC) SIE SPARZ, SPURZ PAHLAVI) 5 ay
```


## [2026-09-04T19:46:25.680Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nimport re\nt=open('ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport bisect\noff=0; starts=[]\nfor p in pages: starts.append(off); off+=p.count('\\n')+1\ni=bisect.bisect_right(starts,2216)-1\nprint('leaf idx',i)\nprint(pages[i][:2500])\nEOF"
}
```


### [2026-09-04T19:46:27.221Z] TOOL RESULT

```
leaf idx 75
[pdf page 76]
oa
WI szssyzl
: OBLAKO ARUSSIAN) «5+,
REFERENCES beth OBLAK (CZECH) Sx
= =
BARNHART: (NEBULA) 697 OBLAK SLOVAK) Sle
MACKENZIE: (CLOUD) 167 AMBRIA, CELTIC) ( gS) gh
BUCK: 3s AMBRA (GAULISH) iS
v4 igbi ob, AMIR, AMYR- WELSH) 69
ethos
Ge Desks Shabs 2 Js ctl eet
BY (A pel slay, pe Uae aly ol Gd9d Es hey AS y BUT hak 22-1
. sel ole
ub tt WA get
OJENBRYN DANISH) jails BRAVAT HAVESTAN) glrs\
OGONBRYN (SWEDISH) (5.8 yp BRUG, BRUK (PAHLAVI) 5 hy
OYENBRYN NORWEGIAN) 559 3 BHROH, BHRUS :(SANSKRIT) <2 Sie
OLD CHURCH SLAVIC) oS 59%! OPaRYS GREEK) gliy
BRUVI OLD SCANDINAVIAN) 2455-he!
BRWI POLISH) long) BRUN, BRA
BROV RUSSIAN) .g3 {OLD HIGH GERMAN) oS giell
oBotr CZECH) Sy BRUs, BRAWAs 7
OBRVA SERBIAN) «ype AUGENBRAVE, ° (GERMAN) st
OBRY (BOHEMIAN) goa BRAVE
oBoct SLOVAK) S11 BRU, {OLD ENGLISH) 46S:
BRUVIS LITHUANIAN) gi s-3 OFARBRU-
BRAUD (OLD IRISH) pS 5) EYEBROW, BROW :(ENGLISH) Si
```


## [2026-09-04T19:46:33.391Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nt=open('ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'ARZ, ARZESH' in p or 'ARZIDAN' in p:\n        print('=== leaf',i, p.strip().split('\\n')[0])\n        print(p[:2500])\n        break\nEOF"
}
```


### [2026-09-04T19:46:35.127Z] TOOL RESULT

```
=== leaf 78 [pdf page 79]
[pdf page 79]
Oj egtisleisl | Ae
REFERENCES beth ERG ARMENIAN) «gs!
————-———— ~~
‘POKORNY: 340 ERC HOLD IRISH) op 543 2h
DELAMARRE: _ _ (HONORER) 255 ARKU- HITTITE) usa
as we . sgb¥ oy
. Jetlool
: 39.70 ge) OS 290319 al
Pe lanl pF GH p! O05 22 03s cal
ARZ, ARZESH, ARZIDAN Gaz zt oti yl Gy! (PERSIAN) gu jb
WORTH ge ald 5039 pe uel Sil a
*ALGwHA, *ALGUH, *ALGwOS (INDO-EUROPEAN) ,gilig,! y xh
AREJAITI, AREJAH :(AVESTAN) .g 5!
‘REFERENCES cathy ARZ, ARZIDAN, (PAHLAVI) 5
POKORNY: 32-33 ARZISHN
DELAMARRE: (VALEUR) 199 ARG OSSETIC) iu s\
MACKENZIE: u ALPHE, ALPHEIN (GREEK) lig
BUCK: 828.826 ALGA LITHUANIAN) (lh
ner sgbG day ALGA LATVIAN) (3) 3.3
ALGAS — «(OLD PRUSSIAN) iS gn.
leethoa
sesh hig, O45 92 051s cal ow
apased AWS eta 9 ia 9 ADSM slabs 22051) cel
Ww
ARZIZ (pid o Ki g sass 5" al'A a) jay! (PERSIAN) upd
*AREG., *ARG-, *ARGU., *RGHI- (INDO-EUROPEAN) igilag,} 9
ARKYANT, —-(TOKHARIAN A) A 55 QRQZATA- AVESTAN) gloss)
ARKI ARDATA- (OLD PERSIAN) skal +s,
ARKWI (TOKHARIAN B) B 555 ARZIZ, ARZIZEN (PAHLAVI) 6 ky
```


## [2026-09-04T19:46:46.230Z] TOOL CALL #77: Bash

```json
{
 "command": "echo \"=== amlaj ar\"; curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%A3%D9%85%D9%84%D8%AC&action=raw\" | head -40; echo; echo \"=== fa aluminium\"; curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%A2%D9%84%D9%88%D9%85%DB%8C%D9%86%DB%8C%D9%88%D9%85&action=raw\" | head -30; echo; echo \"=== alumen la\"; curl -s \"https://en.wiktionary.org/w/index.php?title=alumen&action=raw\" | head -40"
}
```


### [2026-09-04T19:46:48.805Z] TOOL RESULT

```
=== amlaj ar
==Arabic==
[[File:Amla (Gujarati- આમળા) (4938449876).jpg|thumb|right|{{lang|ar|أَمْلَج}}|upright=1.15]]
{{wp|ar:+ (نبات)}}

===Alternative forms===
* {{alter|ar|أَمْلِيج|أَمْلِيك}}

===Etymology 1===
Via {{bor|ar|pal|-}} (from which {{cog|fa-cls|آمله|tr=âmula}}) from {{der|ar|sa|आमलक}}, {{m|sa|आमलकी}} of this meaning.

====Pronunciation====
{{ar-pr|أَمْلَج}}

====Noun====
{{ar-noun|أَمْلَج|m}}

# [[tree]] or [[fruit]] of {{taxfmt|Phyllanthus emblica|species}}, {{vern|emblic myrobalan}} or [[emblic]]
#: {{holonyms|ar|إِطْرِيفَل}}
#: {{coordinate terms|ar|إهليلج|alt1=هَلِيلَج|بَلِيلَج}}
#* {{quote-book|ar|author=ar:{{w|Avicenna|ابن سينا}}<t:Avicenna>|title=ar:القانون في الطب<t:{{w|The Canon of Medicine|Canon Medicinae}}>|year=1025|passage=إن السك الأصلي هو الصيني المتخذ من '''الأملج''' والآن لما عز ذلك فقد يتخذونه من العفص والبلح على نحو عمل الرامك. الطبع: الساذج منه حار في الأولى يابس في الثانية وللطيب حار يابس في الثالثة.|translation=The original ''[[سك#Arabic|sukk]]'' is Chinese and is made from '''emblic''' and when that is hard to get then they take oak gall and dates prepared like ''[[رامك#Arabic|rāmik]]''. Its nature: The simple form of it is hot in the first grade, dry in the second grade and as for the scent hot and dry in the third grade.}}

=====Declension=====
{{ar-decl-noun|أَمْلَجٌ}}

=====Descendants=====
* {{desc|roa-oca|amblic|emblich|alt2=emblichs|bor=1}}<!--doi:10.1515/zrph.2004.120.2.282-->
* {{desc|bor=1|la-med|emblicus|emblica|emleg}}
** {{desc|roa-oca|ambliçi|bor=1}}
** {{desc|en|emblic|bor=1}}
** {{desc|fr|emblique|bor=1}}
** {{desc|it|emblico|bor=1}}
** {{desc|es|emblico|bor=1}}
* {{desc|mxi|اُمِيلْيُو|bor=1}}<!--{{R:ar:Karbstein:2002|page=63}}, form emblio not found in Covarrubias archive.org/details/tesorodelalengua00covauoft/page/222 s.v. mirabolanos-->

===Etymology 2===

====Pronunciation====
{{ar-pr|أُمْلُج}}

====Proper noun====

=== fa aluminium
{{also|الومينيوم}}
==Persian==
{{wp|fa:}}

===Alternative forms===
* {{alt|fa|آلومینیم|tr=âluminiyom, âlominiyom}}

===Noun===
{{fa-noun|tr=âluminiyom, âlominiyom}}

# [[aluminium]]

{{C|fa|Chemical elements}}
=== alumen la
{{also|alúmen}}
==Latin==

===Etymology===
{{etymon|la|id=alum|:af|ine-pro:*h₂elut-<id:beer>|-men<id:nominal>|tree=1}}
{{lit|bitter (salt)}}, from {{suffix|la|ine-pro:*h₂elut-|-men}}.<ref>{{R:itc:EDL|36|alūmen, -inis}}</ref> See also {{cog|ang|ealu|t=ale, beer}} and {{cog|grc|ἀλύδοιμος|t=bitter}}.

===Pronunciation===
* {{la-IPA|eccl=yes|alūmen}}

===Noun===
{{la-noun|alūmen<3>}}

# [[alum]]

====Declension====
{{la-ndecl|alūmen<3>}}

====Derived terms====
{{col|la
|alūminātus
|alūminōsus
|alūta
}}

====Descendants====
{{top2}}
* Italo-Romance:
** {{desc|it|allume}}
* Northern Gallo-Romance:
** {{desc|fro|alum|alts=1}} {{see desc}}
* Southern Gallo-Romance:
** {{desc|ca|alum}}
* Ibero-Romance:
** {{desc|es|alumbre}}
{{bottom}}

===References===
* {{R:la:L&S}}
* {{R:la:du Cange}}
```


## [2026-09-04T19:46:56.632Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/arjasp",
 "prompt": "What does the article say about Arjāsp: its Avestan form, etymology, meaning, and the character in the Shahnameh?"
}
```


### [2026-09-04T19:47:04.106Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T19:47:07.613Z] TOOL CALL #79: Bash

```json
{
 "command": "curl -s -A \"Mozilla/5.0 (X11; Linux x86_64)\" \"https://www.iranicaonline.org/articles/arjasp\" | python3 -c \"\nimport sys,re,html\nt=sys.stdin.read()\nt=re.sub(r'<script.*?</script>','',t,flags=re.S); t=re.sub(r'<style.*?</style>','',t,flags=re.S)\nt=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t); t=re.sub(r'\\s+',' ',t)\ni=t.find('ARJĀSP')\nprint(t[i:i+2000] if i>0 else t[:1500])\n\""
}
```


### [2026-09-04T19:47:09.488Z] TOOL RESULT

```
 Just a moment... Enable JavaScript and cookies to continue
```


## [2026-09-04T19:47:14.037Z] TOOL CALL #80: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Arjasp",
 "prompt": "What is the Avestan form and etymology of the name Arjasp, and who is he in the Shahnameh / Zoroastrian tradition?"
}
```


### [2026-09-04T19:47:20.589Z] TOOL RESULT

```
# Arjasp: Name and Significance

## Avestan Etymology

The Avestan form of Arjasp is **Arәĵaṭ.aspa**, which derives from the word "aspa" meaning horse. Different scholars recorded variations of the name, including "Kharzāsp" and "Hazarāsf," considered corruptions of the Middle Persian rendering.

## Role in Zoroastrian Tradition

In the Avesta, Arjasp appears as "a leader of the _Xyaona,_ a tribe" hostile to Zoroastrianism and its royal protector Goshtasp. Later Middle Persian texts elaborate on religious conflicts where he killed key figures but ultimately faced defeat.

## Shahnameh Portrayal

The epic reimagines him significantly: he becomes "a leader of the Turanians instead of the _Xyaonas_" and is made the son of Shavāsp and brother of the prominent Turanian king Afrasiab. His story culminates when Esfandiār storms his castle Rōyēn Diž, frees his sisters, and kills Arjasp and his brothers.
```


## [2026-09-04T19:47:32.103Z] TOOL CALL #81: Bash

```json
{
 "command": "head -40 tools/fetch_source.py"
}
```


### [2026-09-04T19:47:32.140Z] TOOL RESULT

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


## [2026-09-04T19:47:41.280Z] TOOL CALL #82: Bash

```json
{
 "command": "set -e\nF=tools/fetch_source.py\npython3 $F 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂elgʷʰ-' --note 'page 50, root Algwh: PIE *h2elgwh- \"to cost, have value\"; LIV 263-4, IEW I 32; Greek ἦλφον/ἀλφάνω/ἀλφή'\npython3 $F 'https://en.wiktionary.org/wiki/ارزیدن' --note 'page 50, entry Algwh node 2: NP arzidan < PIr *Harjati < PIE *h2elgwh-'\npython3 $F 'https://en.wiktionary.org/wiki/ارزان' --note 'page 50, entry Algwh node 2: NP arzan < MP arzan \"valuable, worthy\"'\npython3 $F 'https://en.wiktionary.org/wiki/ارجمند' --note 'page 50, entry Algwh node 2: NP arjmand from *h2elgwh-'\npython3 $F 'https://en.wiktionary.org/wiki/वर्चस्' --note 'page 50, entry Algwh node 1/2: Skt varcas \"splendour, vital power\" = Av. varəcah-, MP warz — separate root from arəj- \"value\"'\npython3 $F 'https://www.ahdictionary.com/word/indoeurop.html' --note 'page 50: AHD IE roots appendix, roots algwh- and alu-'\necho done"
}
```


### [2026-09-04T19:47:48.025Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0180d09c6db6728a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/92d40c322d14cc99.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2eb358f49f7bcb31.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/600f16f47244d14f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/05fec99e845609cd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3735d75498a331a4.txt
done
```


## [2026-09-04T19:47:59.730Z] TOOL CALL #83: Bash

```json
{
 "command": "set -e\nF=tools/fetch_source.py\npython3 $F 'https://www.etymonline.com/word/alum' --note 'page 50, root Alu node 1: Latin alumen \"bitter salt\", Proto-Italic *alu-'\npython3 $F 'https://www.etymonline.com/word/aluminum' --note 'page 50, root Alu nodes 2/4: alumine French late 18c; Davy coined alumium 1808 / aluminum 1812; aluminium proposed 1811'\npython3 $F 'https://www.etymonline.com/word/ale' --note 'page 50, root Alu node 4: OE ealu < PGmc *aluth-, uncertain; PIE *alu-'\npython3 $F 'https://en.wiktionary.org/wiki/alumen' --note 'page 50, root Alu node 1: Latin alumen < PIE *h2elut- + -men, de Vaan EDL 36'\npython3 $F 'https://en.wiktionary.org/wiki/آلومینیوم' --note 'page 50, root Alu node 3: Persian aluminium, alt form آلومینیم'\npython3 $F 'https://en.wiktionary.org/wiki/أملج' --note 'page 50, root Amalaka node 2: Arabic amlaj via Middle Persian from Sanskrit amalaka; descendants ML emblicus > English emblic'\npython3 $F 'https://en.wiktionary.org/wiki/emblic' --note 'page 50, root Amalaka node 4: English emblic < Medieval Latin emblicus < Arabic amlaj < Sanskrit amalaka'\npython3 $F 'https://en.wiktionary.org/wiki/आमलक' --note 'page 50, root Amalaka: Sanskrit amalaka \"emblic myrobalan\", MW 146.3'\npython3 $F 'https://en.wikipedia.org/wiki/Arjasp' --note 'page 50, entry Algwh node 2: Arjasp = Av. Arəjat.aspa, Xyaona leader, Shahnameh figure'\npython3 $F 'https://abadis.ir/fatofa/ورج/' --note 'page 50, entry Algwh node 2: Mo`in on ورج \"[pahlavi] ارزش، ارج\"'\npython3 $F 'https://abadis.ir/fatofa/ارج/' --note 'page 50, entry Algwh node 2: Mo`in on ارج \"ارز، ارزش، رتبه، مقام\"'\necho done"
}
```


### [2026-09-04T19:48:21.421Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/91b6fc0fd4f0f01f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6f92d548e95ae367.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6c6a5158eaba02a6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fdff142ace5d9cef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ac90df5dce5dd574.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ea81ad5c854e981d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c3e478b4dc78d0bf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fb7cd39df826316c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2baae0e3ffbe4077.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4bfbc2b2125206a0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d7a89c6bca4eccad.txt
done
```


## [2026-09-04T19:48:26.156Z] TOOL CALL #84: Bash

```json
{
 "command": "cd data/verification/sources/web && for f in 91b6fc0fd4f0f01f 3735d75498a331a4 d7a89c6bca4eccad 2baae0e3ffbe4077; do echo \"=== $f\"; wc -c $f.txt; head -c 400 $f.txt; echo; done; echo \"=== index tail\"; tail -17 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d['status'], d['bytes'], d['url'][:80])\n\""
}
```


### [2026-09-04T19:48:28.357Z] TOOL RESULT

```
=== 91b6fc0fd4f0f01f
8276 91b6fc0fd4f0f01f.txt
URL: https://www.etymonline.com/word/alum
FETCHED: 2026-09-04T19:48:01Z
STATUS: 200
TITLE: Alum - Etymology, Origin & Meaning

Alum - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of alum 

 alum (n.) 

 "whiti
=== 3735d75498a331a4
526313 3735d75498a331a4.txt
URL: https://www.ahdictionary.com/word/indoeurop.html
FETCHED: 2026-09-04T19:47:47Z
STATUS: 200
TITLE: Appendix I - Indo-European Roots

Appendix I - Indo-European Roots 

 HOW TO USE THE DICTIONARY
 To look up an entry in The American Heritage Dictionary of the English Language, use the search window above. For best results, after typing in the word, click on the “Search” button instead of us
=== d7a89c6bca4eccad
11298 d7a89c6bca4eccad.txt
URL: https://abadis.ir/fatofa/ارج/
FETCHED: 2026-09-04T19:48:21Z
STATUS: 200
TITLE: ارج - معنی در دیکشنری آبادیس

ارج - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 ارج
 /~arj/

 مترادف ارج : ارزش، ارز، بها، مقدار، نرخ، اعتبار، پایگاه، پایه، حشمت، شان، قدر، مرتب�
=== 2baae0e3ffbe4077
15843 2baae0e3ffbe4077.txt
URL: https://en.wikipedia.org/wiki/Arjasp
FETCHED: 2026-09-04T19:48:05Z
STATUS: 200
TITLE: Arjasp - Wikipedia

Arjasp - Wikipedia 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Contents 
 Current events 
 Random article 
 About Wikipedia 
 Contact us 

 Contribute

 Help 
 Learn to edit 
 Community portal 
 Recent changes 
 Upload file 
 Special p
=== index tail
200 3978 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂elgʷʰ-
200 8007 https://en.wiktionary.org/wiki/ارزیدن
200 8779 https://en.wiktionary.org/wiki/ارزان
200 3756 https://en.wiktionary.org/wiki/ارجمند
200 7669 https://en.wiktionary.org/wiki/वर्चस्
200 509063 https://www.ahdictionary.com/word/indoeurop.html
200 8139 https://www.etymonline.com/word/alum
200 6788 https://www.etymonline.com/word/aluminum
200 6537 https://www.etymonline.com/word/ale
200 4211 https://en.wiktionary.org/wiki/alumen
200 2133 https://en.wiktionary.org/wiki/آلومینیوم
200 4990 https://en.wiktionary.org/wiki/أملج
200 2613 https://en.wiktionary.org/wiki/emblic
200 2664 https://en.wiktionary.org/wiki/आमलक
200 15584 https://en.wikipedia.org/wiki/Arjasp
200 7425 https://abadis.ir/fatofa/ورج/
200 6541 https://abadis.ir/fatofa/ارج/
```


## [2026-09-04T19:48:32.326Z] TOOL CALL #85: Bash

```json
{
 "command": "cd data/verification/sources/web && grep -o \"algwh-[^|]\\{0,200\\}\" 3735d75498a331a4.txt | head -3; echo \"---\"; grep -o \"alu- *\\n\\?[^|]\\{0,300\\}\" 3735d75498a331a4.txt | head -3; grep -n \"sorcery, magic\" 3735d75498a331a4.txt | head -3"
}
```


### [2026-09-04T19:48:35.502Z] TOOL RESULT

```
---
ugrep: error: error at position 318
][\x80-\xbf]|\xf4[\x80-\x8f][\x80-\xbf][\x80-\xbf]){0,300}
                             exceeds complexity limits___/


236:In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t‑ . ale , from Old English ealu , from Germanic *aluth‑ . [Pokorny alu‑ 33.]
```


## [2026-09-04T19:48:37.887Z] TOOL CALL #86: Bash

```json
{
 "command": "cd data/verification/sources/web && sed -n '230,240p' 3735d75498a331a4.txt; echo \"=== algwh\"; grep -n -i \"algwh\\|be worth\" 3735d75498a331a4.txt | head -5"
}
```


### [2026-09-04T19:48:37.956Z] TOOL RESULT

```
 abele , alb , albedo , albescent , albino , albite , album , albumen , aubade , auburn ; daub , from Latin albus , white.

[Pokorny albho‑ 30.]

 ‌ ‌ alu- 

In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t‑ . ale , from Old English ealu , from Germanic *aluth‑ . [Pokorny alu‑ 33.]

 ‌ ‌ ambhi 

Also m̥bhi .
=== algwh
```


## [2026-09-04T19:49:59.005Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW\"; grep -n \"alumen\\|aluta\" LEW_1910.txt | head -5; echo \"=== LAT\"; grep -n \"alumen\\|alūmen\" LAT.txt | head -5; echo \"=== KNT page\"; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f'); import bisect\noff=0; starts=[]\nfor p in pages: starts.append(off); off+=p.count('\\n')+1\ni=bisect.bisect_right(starts,5058)-1\nprint('leaf',i, pages[i].strip()[:120])\nEOF"
}
```


## [2026-09-04T19:49:59.791Z] TOOL CALL #88: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=aluminum",
 "prompt": "Quote the etymology given for \"aluminum\" and for \"aluminium\" and \"alumina\" in this dictionary entry."
}
```


### [2026-09-04T19:50:00.906Z] TOOL RESULT

```
=== LEW
=== LAT
3093:alumen,-inis n.: alun. Non atteste avant Claudius Quadrig. Panroman,
3103:aluta: v. alumen.
=== KNT page
leaf 182 he field of historical romance. See also PW 3A.710-2, s.v. Smerdis.
III. Tae HELPERS or DARIUS
The names of the six Pers
```


### [2026-09-04T19:50:05.079Z] TOOL RESULT

```
# Etymology of Aluminum

Based on the dictionary entry provided, the etymology given is:

"[ALUMIN(A) + -(I)UM.]"

This indicates the word derives from the root "alumin(a)" combined with the suffix "-(i)um."

The entry does not provide separate etymologies for "aluminium" or "alumina"—only for "aluminum" itself. Those related terms are referenced through the root form but are not individually defined or traced in this dictionary page.
```


## [2026-09-04T19:50:08.650Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3090,3105p' LAT.txt; echo \"=== KNT leaf for arjana headword\"; python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if \"arjana- sb.\" in p:\n        print('leaf',i)\n        nums=re.findall(r'(?m)^\\s*(\\d{2,3})\\s*$',p)\n        print('nums',nums)\n        print(p[:200])\nEOF"
}
```


### [2026-09-04T19:50:10.325Z] TOOL RESULT

```
ce genre a de grandes chances de n'etre ni indo-europeen ni derive de
quelque mot italique herite de 1 1 indo-europeen.
•
alumen,-inis n.: alun. Non atteste avant Claudius Quadrig. Panroman,
sauf roumain. M.L.389 et germ.: ags. alifne; celt. : iri. ailim, gall.
elyf. Cf. bitumen, et comme celui-ci sans doute mot etranger.
Derives: aluminarius, -i; aluminatus (ex-), -minosus. Peut-etre faut-il
y rattacher: aluta, -ae f.: cuir assoupli avec 1'alun, peau souple
(d^ji dans Caton?). M.L.390, d'ou alutdcius, -a, -um.
Le seul terme qui se laisse rapprocher est un mot grec Occidental:
aXu8(o) t,[xov • 7UKpov Tcxpa Suxppovi., Hes.
Terme technique d'origine obscure.
alumnus: v. alo.
aluta: v. alumen.
alutiae, -arum?, mot obscur (iberique?) qui figure dans un seul
passage de Pline, 34,157 in aurariis metallis, quae alutias (alutia
=== KNT leaf for arjana headword
leaf 192
nums []
-, GAv. angra-, LAv. apra- ‘hostile, enemy’, to рАт. root *ans-, seen in Av. qsta- ‘hate, enmity’; ef. also Av. (nom.) avrd mainyus ‘evil spirit, Ahriman’ (Bthl. AiW 189); not to Skt. art- ‘en- emy’ (
```


## [2026-09-04T19:50:19.517Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(186,196):\n    nums=re.findall(r'(?m)^\\s*(\\d{2,3})\\s*$',pages[i])\n    print(i,nums[:6],'|',pages[i].strip()[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T19:50:21.076Z] TOOL RESULT

```
186 ['165'] | � asn. DPd 20; DNa 53; XPh 43, 59; XSc 4°. ata- таш DPd 22; 
187 ['166'] | t built, unrepaired’; neg. a- + pte. of kar- ‘make’. {akarta
188 [] | ’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadt
189 ['167', '168'] | n., asn.); AÁuramazdü, АМ; ava (nsn.); avdkaram, avükaramca-
190 [] | . Skt. apa, Gk. and, Lt. ab, Gt. af, Gm. ab, NEng. оў, off, 
191 ['169', '170'] | formed like Gk. &exero to root *segh-, ёттєтө to root *pet- 
192 [] | -, GAv. angra-, LAv. apra- ‘hostile, enemy’, to рАт. root *a
193 ['171'] | t’). - LEXICON ч. Атах$аса- sb. ‘Artaxerxes’ (Т, son of Xerx
194 ['172'] | пат. AsH 1, 5; DB 1.4f; DBa 6; DSf 13; XPf 19, 20; A’Pa 20 (
195 ['173'] | 's avabäštā adj. apm. 'thus standing". avadà (ie. avadá) adv
```


## [2026-09-04T19:50:29.286Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('PHD.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f'); import bisect\noff=0; starts=[]\nfor p in pages: starts.append(off); off+=p.count('\\n')+1\nfor ln in (217,607,611):\n    i=bisect.bisect_right(starts,ln-1)-1\n    print('line',ln,'leaf',i,'printed',i-21)\nEOF\necho \"=== PHD arz noun\"; grep -n \"^arz \\[\\|arz \\[\\?lc\\|arzān\\|arzōmand\" PHD.txt | head -5; grep -n \"arz \\[\" PHD_mackenzie.txt | head -5"
}
```


### [2026-09-04T19:50:31.117Z] TOOL RESULT

```
line 217 leaf 28 printed 7
line 607 leaf 86 printed 65
line 611 leaf 86 printed 65
=== PHD arz noun
1502:death marg(īh), ēš, widerišn(īh), P murd; moment of — gyān kandan; deserving — margarzān; risk —, fight to ~ anēš xwardan.
4190:value (n.) arz, arzānīgih, arzišn, arzómandih, wahág.
4356:worthiness arzānīgīh, sahīgīh, sazā- gih, sazišn, šāyendagīh.
4358:worthy arzān(īg), arzómand, sahig, sazāg(wār), šāyendag; be — saz-, šāyistan.
4847:mazgit mizné may magas padīr-! padīrišnī padiriftant magind makog 1-2mar marg margomand margarzān margīh
1190:arz [KSP' < A ksp; 'Ic I N ~] worth, value.
1729:   tarz [elz IN,...,] bustard.
1904:darz [dIe I N --] seam.
2123:    .....,-arz [-)lc] worthless.
2753:P hAmharz [h(')mhlc I P h'mhyrz] adjutant, attendant.
```


## [2026-09-04T19:50:43.844Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (38,39):\n    print('leaf',i,'|',pages[i].strip()[:100].replace('\\n',' '))\n    print('   tail:',pages[i].strip()[-80:].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T19:50:45.888Z] TOOL RESULT

```
leaf 38 | 2, — FrP 21 gives as equivalents of the ideogr.: ’pwltn = appurtan, pres. ’pwlyt = ap- pure, 'pwlym 
   tail: 81. arišk ['lyšk'] envy 66°. 691. 8419; bé-~ 454, — Av. (187) araska-; MPrs *ryš
leaf 39 | k (A-H I); Paz. ar(a)šk; NP rask. ariškēh enviousness 8421. arišn [lšn'] cubit: šah-— royal cubit, a
   tail:  the 3d day of the month; MPrs ’rdywh<yst> Sogd. 2771; NP ardi- (urdi-)bihišt. C
```


## [2026-09-04T19:56:22.151Z] TOOL CALL #93: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk50.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\ndata = {\n \"pdf_page\": 50,\n \"book_page\": 20,\n \"verified_by\": \"claude-fable-5-1\",\n \"verified_on\": \"2026-09-04\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Algwh\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₂elgʷʰ- 'to be worth, cost, earn' (Pokorny algʷh- 'verdienen, Gegenwert', IEW I 32-33)\",\n   \"note\": \"Root, language label and gloss are all correct and are exactly what Nourai's cited page says: Pokorny I 32-33 heads the entry 'algᵂh- ‚verdienen, Gegenwert‘' with Skt. árhati / arghá-, Av. arəjaiti / arəjah-, NPers. arzīdan, Gk. ἀλφή / ἀλφεῖν, Lith. algà; the same entry stands in Walde-Pokorny I 91 and Watkins 1985 ('algwh-. To earn, be worth. [Pok. algvh- 32.]'; the root was dropped from the current online AHD appendix). LIV² 263-4 and Cheung 2007 s.v. *Harj reconstruct the same root. THE ONE REAL PROBLEM ON THIS CHART is the varj / varəcah- material hung under this root: Av. varəcah- 'vital power, splendour' (Skt. várcas-, MP warč, NP varj, varjāvand) belongs to a different etymon, as Nourai's own cited sources (Horn 241 and Mo'in's footnote in Borhan-e Qate' 2265, which cites Bartholomae col. 1367) both say.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂elgʷʰ-\",\n    \"https://www.ahdictionary.com/word/indoeurop.html\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:32\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt \\\\f-leaf 40-41 (printed pp.32-33, leaf = p+8): headword 'alg\\\\u1d42h- ,verdienen, Gegenwert'. Ai. ärhati ... av. arəjaiti ,ist wert, kommt in Wert gleich' (npers. arzīdan ,verdienen'), arəjah- (es-St.) n. ,Wert, Preis'. Gr. ἀλφή ,Erwerb' = lit. algà ... ἀλφάνω, ἀλφεῖν ,einbringen; verdienen'. WP. I 91.' Exactly the root, gloss and members Nourai draws.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.91 (WLD_Bd1_pages.txt leaf 100)\", \"stance\": \"supports\",\n     \"note\": \"'algᵂh- ‚verdienen, Gegenwert“. Ai. arhati ... av. arəjaiti ... arəjah- (es-St.) n. ‚Wert, Preis“. Gr. ἀλφή ‚Erwerb“ = lit. alga ...' — the source Pokorny 32 abridges.\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, root list s.v. algwh-\", \"stance\": \"supports\",\n     \"note\": \"'algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.]' — same root name and gloss; note the online (2011) AHD appendix no longer carries this root.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. alguhos (IEC.txt line 434)\", \"stance\": \"supports\",\n     \"note\": \"'alguhos, ā “profit, wealth, value, wage”. WP I, 92 Skt. argháh; Av. arəjo; Per. arz, arj; Oss. arɣ; Hitt. halkwessar; Gk. alphē; Li. algà.' Mann lists Persian arz, arj under the root, exactly as Nourai does.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 11.87 PRICE, p.826 (SYN.txt leaf 894)\", \"stance\": \"supports\",\n     \"note\": \"'Skt. argha-, Av. arəjah- (NPers. arz ‘price’) : Skt. arh-, Av. arəj- ‘be worth’ Lith., Lett. alga ‘wages’. Walde-P. 1.91. Barth. 192.'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *Harj 'to be worth'\", \"stance\": \"supports\",\n     \"note\": \"'*Harj ‘to be worth’ ... «PIE *H₂elgʷʰ- ‘to be worth, value, earn’ = LIV: 263 | Pok.: 32 f.' with Av. arəj-, MP arz-, Sogd. ʾyzn, NP arzīdan, Skt. arh-/arghá-.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur p.80 (pdf 79) s.v. ARZ, ARZESH, ARZIDAN\", \"stance\": \"supports\",\n     \"note\": \"Independent modern Persian handbook: 'ARZ, ARZESH, ARZIDAN (PERSIAN) — WORTH — *ALGwHA, *ALGUH, *ALGwOS (INDO-EUROPEAN); AREJAITI, AREJAH (AVESTAN); ARZ, ARZIDAN, ARZISHN (PAHLAVI); ARG (OSSETIC); ALPHE, ALPHEIN (GREEK); ALGA (LITHUANIAN) ... REFERENCES POKORNY: 32-33 ... BUCK: 828, 826.' Same root, same members, same Pokorny page.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"arej, arejah : value ; arejat-aspa : (with) valuable horses ; varejah, varecah : value\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Av. arəj- 'to be worth' (3sg. pres. arəjaiti, Vidēvdād/Hāđōxt) and the es-stem arəjah- n. 'worth, price' continue PIE *h₂elgʷʰ- with the regular Indo-Iranian outcome *Harjʰ- > Iranian *Harǧ- (Skt. cognates árhati, arghá-); Bartholomae AiW gives 'arəjah- n. ‘Wert, Preis’' and 'arəja- 1) Adj. ‘wertvoll’'. Arəjaṱ.aspa- is a bahuvrīhi 'whose horses are of worth' (arəjaṱ, 3sg. injunctive of the same verb, + aspa- 'horse'), the name of a Hyaona (Chionite) prince and enemy of Vištāspa in Yt. 5.109, 9.30 and 17.50 — Nourai's 'owner of valuable horses' is a fair rendering. BUT varəjah-/varəcah- does NOT belong here: Av. varəcah- (Skt. várcas-, PIIr *wárčas-) means 'vital power, energy; splendour', and Bartholomae's only Avestan compound of it, as-varəcah-, is glossed 'der grosse Kraft, Tatkraft besitzt' (Yt. 19.57-58, of Fraŋrasyan), not 'value'. Nourai has merged two etyma that merely look alike in New Persian (arj ~ varj).\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂elgʷʰ-\",\n      \"https://en.wiktionary.org/wiki/वर्चस्\",\n      \"https://en.wikipedia.org/wiki/Arjasp\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"POK:32\", \"status\": \"partial\",\n       \"note\": \"POK_01.txt leaf 40-41 (pp.32-33) has 'av. arəjaiti ... arəjah- (es-St.) n. ‚Wert, Preis“' — supports arəj/arəjah. Pokorny says nothing about Arəjaṱ.aspa- and nothing about varəcah-, which he treats nowhere under this root.\"},\n      {\"ref\": \"SYN:826\", \"status\": \"supports\",\n       \"note\": \"Buck p.826 (SYN.txt leaf 894), §11.87 PRICE §7: 'Skt. argha-, Av. arəjah- (NPers. arz ‘price’) : Skt. arh-, Av. arəj- ‘be worth’ ... Walde-P. 1.91. Barth. 192.' The table on the same section lists 'Av. arəjah-, paraska-' as the Avestan words for 'price'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch cols. ~191-195 (BRT.txt \\\\f-leaves 134-135)\", \"stance\": \"partial\",\n       \"note\": \"'arəjah- n. ‘Wert, Preis’'; 'arəja- 1) Adj. ‘wertvoll’ ... 2) m. ‘Wert’'; 'arəjaṱ.aspa- m. EN. eines Hyaona-Fürsten' (Yt. 9.30, Yt. 5.109) — supports the first two words. But at leaf 172 Bartholomae has 'as-varəcah- Adj. ‘der grosse Kraft, Tatkraft besitzt’', i.e. varəcah- = 'power', not 'value' — contradicts the third.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *Harj\", \"stance\": \"partial\",\n       \"note\": \"'*AVESTAN: arj- ‘to be worth’ — Liste: 10. Pres. them.: IND. 3sg. YAv. arəjaiti (H 1.5 f., H 1.8, H 1.10), INJ. 3sg. arəjaṱ (Y 50.10, Y 64.6, Yt 5.109)'. No varəcah- anywhere in the entry.\"},\n      {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. algwh-\", \"stance\": \"silent\",\n       \"note\": \"Watkins lists only Sanskrit arhati under the root; no Avestan forms are cited, so nothing bears on varəcah-.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"arj «ارج» ; rzân «ارزان» ; Arjâsp «ارجاسب» ; varj «ورج»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"arj / arz: Av. arəjah- n. 'worth' > MP arž / arz [ʾLCʾ] 'value, merit' (Nyberg: 'arž ... Av. (192) arəjah-; Paz. arža; NP arj, arz'; MacKenzie: 'arz ... worth, value') > NP arz and, with the regular NP ž/j doublet of MP ž, arj; Hübschmann PS §2 lists 'arj, arz ‚Werth“' together as showing initial a- kept before a consonant cluster. Derivatives: MP arzōmand > NP arjmand/arjumand (MacKenzie p.12; Nyberg 'aržōmand ... NP arjmand'), MP arzān(īg) 'worthy, valuable' > NP arzān, which in NP shifted 'worth its price' > 'affordable' > 'cheap' (hence Nourai's 'valuable, also worthless'); NP arzīdan, arziš < MP arz-. NOTE the JSON transliteration 'rzân' is a scan slip: the script ارزان and the book both read arzān. Arjāsp ارجاسپ = Av. Arəjaṱ.aspa- (Hyaona king) via MP Arzāsp; in the Šāhnāma he is turned into a Turanian king killed by Esfandiyār at Rōyīn-diž, and Borhan-e Qateʽ (p.97-98) gives just that story. varj ورج: DISPUTED as drawn. Horn no.1077 (p.241) derives NP verč/varj from 'aw. *varəcah- ... phlv. varč bezw. varj, varčōmand bezw. varjōmand; ai. várcas- ‚Glanz“', and Mo'in's own footnote at BQT 2265 says the same, citing Bartholomae col. 1367; MacKenzie has ²warz 'miracle, miraculous power' and warzāwand 'having miraculous power' = NP ورجاوند varjāvand. So varj, varjmand, varjāvand belong with far(r)/xwarrah 'divine glory', not with arj 'value' — even though Mo'in's Farhang-e Fārsī glosses ورج simply as '[په.] ارزش، ارج', which is what Nourai followed. The Ferdowsī line quoted on the chart ('نه تنها شه و خسرو کشور است / که شاه است و با ورج پیغمبر است') is printed verbatim in Mo'in's BQT footnote among the passages showing varj = 'divine glory'.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/ارزان\",\n      \"https://en.wiktionary.org/wiki/ارزیدن\",\n      \"https://en.wiktionary.org/wiki/ارجمند\",\n      \"https://en.wiktionary.org/wiki/वर्चस्\",\n      \"https://abadis.ir/fatofa/ورج/\",\n      \"https://abadis.ir/fatofa/ارج/\",\n      \"https://en.wikipedia.org/wiki/Arjasp\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:97\", \"status\": \"supports\",\n       \"note\": \"BQT_v1_pages.txt \\\\f-leaf 307 (printed p.97): 'ارج - بفتح اول و سکون ثانی و جیم بمعنی قدر و قیمت و مرتبه و حد و اندازه باشد ... و بمعنی قیمت و بها و ارزش هم هست', and immediately below 'ارجاسپ ... نام پسر فراسیاب است که در توران پادشاهی میکرد و در رویینه دژ مسکن داشت', with Mo'in's footnote giving the Avestan form Arəjaṱ.aspa.\"},\n      {\"ref\": \"BQT:98\", \"status\": \"supports\",\n       \"note\": \"BQT_v1_pages.txt leaf 308 (printed p.98): continuation of ارجاسپ (Esfandiyār storms Rōyīn-diž and kills him) and the entry ارجمند 'بمعنی عزیز و گرامی و صاحب قدر ... چه ارج بمعنی قدر و مرتبه و مند بمعنی صاحب و خداوند است', with Mo'in's footnote '«بارتولمه ۱۹۱»' (Bartholomae col. 191 = arəj-/arəjah-).\"},\n      {\"ref\": \"BQT:102\", \"status\": \"supports\",\n       \"note\": \"BQT_v1_pages.txt leaf 312 (printed p.102): 'ارز - بوزن طرز ، بمعنی قیمت و بها و ارزش باشد' with Mo'in's footnote 'پهلوی arz مشتق از اوستایی arəj «بارتولمه ۱۹۱»', and the footnote to ارزان: 'در پهلوی arzān (با ارزش، قیمتی)' with dialect forms arzān/arzānī.\"},\n      {\"ref\": \"BQT:2265\", \"status\": \"contradicts\",\n       \"note\": \"vol. 4 pdf p.348 = printed p.2265: the headword 'ورج ... بمعنی قدر و مرتبه و بزرگی و شأن و شوکت باشد' carries Mo'in's footnote 7: 'در پهلوی warč در اوستا varəcah- در سانسکریت ... بمعنی نیروی حیاتی و قوت، و varəcaŋhvant- در اوستا صفت است بمعنی نیرومند و قوی «بارتولمه ۱۳۶۷»، گاه در ادبیات پارسی بجای «فر» و «خوره» کلمهٔ «ورج» را بهمان مفهوم بکار برده‌اند'. The very page Nourai cites derives varj from a DIFFERENT Avestan word (varəcah- 'vital power', Bartholomae col. 1367), not from arəjah-. Nourai's Ferdowsī شاهد is one of the lines quoted in that footnote.\"},\n      {\"ref\": \"HRN:241\", \"status\": \"contradicts\",\n       \"note\": \"HRN.txt \\\\f-leaf 262 = printed p.241, entry 1077: 'verč ‚Grösse, Würde“. aw. *varəcah- in asvarədah-, varəcaŋhvant- ‚glanzreich, prangend“; phlv. varč bezw. varj, varčōmand bezw. varjōmand ...; ai. várcas- ‚Glanz“.' Horn's p.241 is about varj only, and derives it from varəcah-, i.e. it does not support putting varj under 'value'.\"},\n      {\"ref\": \"MON:199\", \"status\": \"not_checked\",\n       \"note\": \"Mo'in's six-volume Farhang-e Fārsī is not scanned online and the local files are only the two-volume Adena abridgement (unusable OCR). Substitute checked: abadis.ir's Mo'in text s.v. ارج = '(اَ) (اِ.) ارز، ارزش، رتبه، مقام' — consistent with the gloss.\"},\n      {\"ref\": \"MON:4999\", \"status\": \"not_checked\",\n       \"note\": \"MON vol. 5 (اعلام / proper names, where Arjāsp would stand) has no scan anywhere and vajehyab/abadis carry no Mo'in proper-name entries.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p.116 §2 (HUB.txt leaf 126)\", \"stance\": \"supports\",\n       \"note\": \"'Im Anlaut erhielt sich a im Mittelpersischen, ebenso im Neup. vor Doppelkonsonanten: abr ‘Wolke’, abrešum ‘Seide’, astar ‘Stern’, arj, arz ‚Werth“, arzīz ‘Zinn, Blei’ ...' — Hübschmann treats arj and arz as the same inherited word 'Werth'.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (Glossary) p.~31 s.v. arž\", \"stance\": \"supports\",\n       \"note\": \"'arž [ʾLCʾ] value, merit 67⁴. — Av. (192) arəjah-; Paz. arža (SGV); NP arj, arz.' Also 'aržānīk ... derived from arž through the intermediate adj. aržān ‘worthy’ ... Arm. lw. aržan' and 'aržōmand ... NP arjmand'.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p.12 s.v. arzōmand, s.v. arz; p.88 s.v. ²warz, warzāwand\", \"stance\": \"partial\",\n       \"note\": \"'arz [KSPʹ < A ksp; ʾIc | N ~] worth, value'; 'arzōmand [ʾIcʹwmnd | (N arjumand)] valuable, worthy' — supports arj/arz/arjmand. But 'warz [wlc | M wrc/z] miracle, miraculous power' and 'warzāwand [wlcʹwnd | M wrcwynd] having miraculous power, powerful' (= NP ورجاوند) are a separate lemma from arz — contradicts varj under this root.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *Harj\", \"stance\": \"supports\",\n       \"note\": \"'*MIDDLE PERSIAN: BMP ʾIc- /arz-/ ‘to be worth’ ... *NWIR: NP arzīdan/arz-, ... NP arz ‘price, value’'.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur p.80 (pdf 79)\", \"stance\": \"supports\",\n       \"note\": \"'ARZ, ARZESH, ARZIDAN (PERSIAN) ... ARZ, ARZIDAN, ARZISHN (PAHLAVI) ... AREJAITI, AREJAH (AVESTAN) ... *ALGwH- (INDO-EUROPEAN)'. No varj in the entry.\"},\n      {\"src\": \"MON\", \"where\": \"abadis.ir, فرهنگ معین s.v. ورج\", \"stance\": \"partial\",\n       \"note\": \"'فرهنگ معین (وَ) [په.] (اِ.) ارزش، ارج.' — Mo'in's lexicon gives varj the gloss Nourai gives it and tags it Pahlavi, but supplies no Avestan etymon; his etymological footnote in Borhan (2265) puts it under varəcah-.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Old Persian\",\n     \"words\": \"arjana : valuable\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"OP arjana- is genuinely attested — but only in Darius's Susa foundation charter DSf (arjanam DSf 41f, arjanam-šaiy DSf 23), and Kent glosses it 'ornamentation', a sense fixed by the Akkadian version's simmanû 'decoration'. Formally it is a -na- derivative of the root arj- 'be worth' (Kent's own comparanda: 'Cf. Av. pres. arəja- ‘be worth’, Skt. árhati, and Ars. Phl. arzān, NPers. arzān, Av. arəjah- ‘worth, value’, Skt. argha-'), i.e. 'the precious/valuable (material)'. So the word, the language label and the root are right; Nourai's bare gloss 'valuable' is the etymological rather than the attested meaning.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"SOD:90\", \"status\": \"supports\",\n       \"note\": \"SOD_pages.txt \\\\f-leaf 155, printed p.90, entry 2274: 'ʾyzn C / ezan ©<OP arjana ©pl. -ī ... valuable, worthy'. Gharib herself writes the Old Persian form arjana with exactly Nourai's gloss.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p.170 s.v. arjana-\", \"stance\": \"partial\",\n       \"note\": \"'arjana- sb. ‘ornamentation’, as shown by AKK.: si-im-ma-nu-u ‘decoration’ ... against Hz.’s ‘limestone’ ... Cf. Av. pres. arəja- ‘be worth’, Skt. árhati, and Ars. Phl. arzān, NPers. arzān, Av. arəjah- ‘worth, value’, Skt. argha-. — arjanam nsn. DSf 41f; arjanam-šaiy DSf 23.' Same root, different attested gloss.\"},\n      {\"src\": \"BRT\", \"where\": \"AiW (BRT.txt leaves 134-135)\", \"stance\": \"silent\",\n       \"note\": \"Bartholomae's Old Persian section has no arjana- headword in the searchable OCR; the word is treated in Kent and in the Susa-charter literature.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *Harj\", \"stance\": \"silent\",\n       \"note\": \"Cheung lists Avestan, MP, Sogdian, Choresmian, NW-Iranian and Sanskrit forms but no Old Persian nominal derivative.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Sogdian\",\n     \"words\": \"`yžn : valuable\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Sogdian ʾyzn / ʾyjn (Christian and Manichaean scripts), read ēzan, 'worthy, valuable'; Gharib's dictionary has it twice, at no. 2274 (p.90) and no. 2401 (p.95). The form goes back to Iranian *arǧ-āna- / *arǧiyana-: Sogdian lost the r of the *ar- cluster and fronted the vowel, giving ʾy- for older *ʾarz- (contrast the still-transparent Sogdian doublet ʾyrznw and Parthian aržān, MP arzān, all 'worthy'). Nourai's arrow makes it descend from OP arjana-, which is Gharib's note on p.90 ('©<OP arjana'); but on p.95 the same author reconstructs '*arǧyan-; Av. arəja-, Parth. arzān, MP arzān', i.e. an inherited East-Iranian cognate rather than a borrowing from Old Persian — which is what Cheung and modern Sogdian scholarship assume. Hence plausible: right word, right root, but the OP→Sogdian edge is a sister relation, not descent.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"SOD:90\", \"status\": \"supports\",\n       \"note\": \"SOD_pages.txt leaf 155, printed p.90, no. 2274: 'ʾyzn C ezan ©<OP arjana ©pl. -ī ... valuable, worthy. GMS 290; STii 6.47, 34; C2 gloss.'\"},\n      {\"ref\": \"SOD:95\", \"status\": \"supports\",\n       \"note\": \"SOD_pages.txt leaf 160, printed p.95, no. 2401: 'ʾyjn M ezan / worthy ©<*arǧyan-; Av. arəja-, Parth. arzān, MP arzān ... GMS 155, 383; BBB p93'; and no. 2402 'ʾyjnʾawe(č) value, price'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *Harj, *SOGDIAN section\", \"stance\": \"supports\",\n       \"note\": \"'*SOGDIAN: SSogd. ʾyrznw, MSogd. ʾyjn ‘worthy’, SSogd. ʾarγ, BSogd. ʾarγ, MSogd. ʾarγ ‘value, price’' — the same word, placed directly under the root, not under Old Persian.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent p.170 s.v. arjana-\", \"stance\": \"partial\",\n       \"note\": \"Confirms OP arjana- exists and belongs to the same root, but says nothing about Sogdian taking it over.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Greek\",\n     \"words\": \"alphein : to gain, profit\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Gk. ἀλφεῖν is the (thematic) aorist infinitive of the defective verb ἀλφάνω 'to bring in, fetch (a price), earn', Homeric and Herodotean (e.g. of slaves ‘fetching’ a price). It continues the PIE root aorist *h₂élgʷʰ-t (Gk. ἦλφον), to which the nasal present ἀλφάνω was built secondarily — hence Pokorny's remark that ἀλφεῖν corresponds to Skt. árhati but was pushed into aorist function by the fuller present. Beside it stands the noun ἀλφή 'gain, produce' (= Lith. algà, OPruss. gen. ālgas 'wage'). The node hangs directly off the root, correctly: Greek did not take it from Iranian.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂elgʷʰ-\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"POK:32\", \"status\": \"supports\",\n       \"note\": \"POK_01.txt leaf 41 (printed p.33): 'Gr. ἀλφή ‚Erwerb“ = lit. algà, apr. Gen. Sg. ālgas ‚Lohn“, ἀλφάνω, ἀλφεῖν ‚einbringen; verdienen“ (ἀλφεῖν = ai. árhati, aber durch das vollere Präs. ἀλφάνω in die Geltung als Aorist gedrängt), ἀλφεσίβοιος ‚Rinder einbringend“.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.91\", \"stance\": \"supports\",\n       \"note\": \"'Gr. ἀλφή ‚Erwerb“ = lit. alga, apr. gen. sg. ālgas ‚Lohn“, ἀλφάνω, ἀλφεῖν ‚einbringen, verdienen“'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 11.78 WAGES, p.818 (SYN.txt leaf 884)\", \"stance\": \"supports\",\n       \"note\": \"'Lith., Lett. alga (OPruss. gen. sg. ālgas) : Grk. ἀλφή ‘produce, gain’, Skt. argha-, Av. arəjah- ‘value, price’ (11.87), Skt. arh-, Av. arəj- ‘be worth’.'\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. alguhos\", \"stance\": \"supports\",\n       \"note\": \"'... Gk. alphē; Li. algà' listed with Skt. arghá-, Av. arəjo, Per. arz, arj.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Alu\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *alu- (*alu-d-, *alu-t-) 'bitter; ale, beer; alum'\",\n   \"note\": \"Both halves of Nourai's gloss are quotations from his two cited sources. Pokorny I 33-34 heads the entry 'alu- (-d-, -t-) ‚bitter, Bier, Alaun“' (so does Walde-Pokorny I 91); Watkins/AHD heads it 'alu-. In words related to sorcery, magic, possession, and intoxication', so the chart's 'bitter, also used in words related to intoxication, magic and sorcery' is a faithful merger. Caveat for the whole entry: the connection of Latin alūmen to this root is only 'perhaps' in the modern literature — Ernout-Meillet call alūmen a 'terme technique d'origine obscure', and Watkins's current appendix lists only ale under alu-, dropping alum entirely.\",\n   \"sources\": [\n    \"https://www.ahdictionary.com/word/indoeurop.html\",\n    \"https://www.etymonline.com/word/ale\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:33\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt \\\\f-leaf 41 (printed pp.33-34): 'alu- (-d-, -t-) ‚bitter, Bier, Alaun“. Gr. ἀλυδ(φ)οιμον· πικρόν ... Hes.; lat. alūta ‚Alaunleder“ und alūmen ‚Alaun“ sind einfach Erweiterungen von *alū-. Die Wurzel erscheint in Nordeuropa mit der Bedeutung ‚Bier, Met“ ... ags. ealu(d) n. ‚Bier“ ...'\"},\n    {\"ref\": \"KLN:46\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt \\\\f-leaf 35 (printed p.46) s.v. ale: 'OE. ealo, alo, rel. to ON. öl, and cogn. with L. alumen, ‘alum’, fr. I.-E. base *alu-, ‘bitter’. OPruss. alu, ‘mead’, Lith. alús, OSlav. olu, ‘beer’, are Teut. loan words. Cp. alum, alumina, aluta, alutaceous.' Exactly the root name and gloss Nourai gives.\"},\n    {\"ref\": \"AHD:1506\", \"status\": \"supports\",\n     \"note\": \"The 1975/76 New College appendix is not open online, but the identical root stands in Watkins 1985 (AHD_watkins1985.txt) and in the current online appendix: 'alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t-. ale, from Old English ealu, from Germanic *aluth-. [Pokorny alu- 33.]' — the second half of Nourai's gloss is a verbatim borrowing from it. Note AHD lists no alum/alumen under the root.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.91\", \"stance\": \"partial\",\n     \"note\": \"'alu- ‚bitter, Bier, Alaun“ ... lat. alūta ‚Alaunleder“ beruht formell auf einem Verbum *aluio ..., vielleicht auch alūmen ‚Alaun“, wenn dieses nicht einfach Erweiterung von *alu- ist.' Walde-Pokorny hedge on alūmen ('vielleicht'), which Pokorny 1959 later stated flatly.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. alumen (LAT.txt line 3093)\", \"stance\": \"contradicts\",\n     \"note\": \"'alumen,-inis n.: alun. Non attesté avant Claudius Quadrig. ... Le seul terme qui se laisse rapprocher est un mot grec occidental: ἀλυδ(ο)ιμον· πικρόν ... Terme technique d'origine obscure.' Ernout-Meillet decline to put alūmen in an IE root at all.\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. alu-\", \"stance\": \"partial\",\n     \"note\": \"'alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.]' — supports the second gloss and 'ale', but no 'bitter' and no alum.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Latin\",\n     \"words\": \"Alŭmen : alum, a bitter salt of aluminum\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Lat. alūmen, gen. alūminis n. 'alum' (first attested in Claudius Quadrigarius, 1st c. BCE; Pliny NH describes its medicinal use on wounds) is analysed as an -men noun on the stem *alū- 'bitter', so literally 'the bitter (stuff)', with the parallel derivative alūta 'alum-tanned leather'. The only close comparandum is the Sicilian Greek gloss ἀλυδοιμον· πικρόν (Sophron, in Hesychius), plus the Germanic/Balto-Slavic 'ale/beer' words. De Vaan's Etymological Dictionary of Latin (p.36) analyses it as *h₂elut- + -men, i.e. from the same stem as ale. Nourai's chart is therefore in line with Pokorny and Klein, but Ernout-Meillet call the word 'd'origine obscure', so this is a probable rather than a proven derivation. (The chart's macron placement 'Alŭmen' should be alūmen with long ū.) The gloss 'a bitter salt of aluminum' is anachronistic wording for a Latin word but factually describes potash alum, KAl(SO₄)₂.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/alum\",\n      \"https://en.wiktionary.org/wiki/alumen\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"OEW:84\", \"status\": \"not_checked\",\n       \"note\": \"Shipley, The Origins of English Words (1984), is lending-only on the Internet Archive (djvu.txt returns 401) and there is no other full-text copy; page 84 could not be read.\"},\n      {\"ref\": \"KLN:46\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 35 (p.46) s.v. ale cross-refers to L. alumen 'alum' from I.-E. *alu- 'bitter'; the fuller statement is at leaf 41 (pp.57-58) s.v. alum: 'OF. alum (whence F. alun), fr. L. alumen, ‘alum’, lit. ‘bitter salt’, cogn. with Gk. ἀλυδοιμός, ‘bitter’, OE. ealo, alo, ‘ale’, ON. öl, of s.m.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"p.33\", \"stance\": \"supports\",\n       \"note\": \"'lat. alūta ‚Alaunleder“ und alūmen ‚Alaun“ sind einfach Erweiterungen von *alū-.'\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. alumen\", \"stance\": \"contradicts\",\n       \"note\": \"'Terme technique d'origine obscure' — no IE root assigned; only the Hesychian ἀλυδ(ο)ιμον is compared.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.91\", \"stance\": \"partial\",\n       \"note\": \"'vielleicht auch alūmen ‚Alaun“, wenn dieses nicht einfach Erweiterung von *alu- ist.'\"},\n      {\"src\": \"KLN\", \"where\": \"1966 ed. pp.57-58 s.v. alum\", \"stance\": \"supports\",\n       \"note\": \"'fr. L. alumen, ‘alum’, lit. ‘bitter salt’.'\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"French\",\n     \"words\": \"aluminium\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The French link is real but mislabelled. What French actually contributed is alumine (Guyton de Morveau / the Lavoisier nomenclature, late 1780s-90s), the chemists' name for the earth Al₂O₃, itself formed on Lat. alumen; English took it as alumina. The element name was then coined in English by Humphry Davy — alumium 1808, then aluminum by 1812 — and the -ium variant aluminium was proposed in January 1811 in W. H. Wollaston's account of Davy's experiments and endorsed by the Quarterly Review (1812) as having 'a more classical sound'; French, like most European languages, adopted aluminium from there. So Lat. alumen > Fr. alumine > (Eng./ModL) aluminium > Fr. aluminium is the real chain, and modern French aluminium is a legitimate immediate source for the Persian word below — but 'French aluminium' as a direct derivative of Latin alumen, with no English step, is not what the sources say.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/aluminum\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\",\n       \"note\": \"The AHD entry for aluminum gives only '[ALUMIN(A) + -(I)UM.]' (checked at ahdictionary.com/word/search.html?q=aluminum); it derives the element name from alumina, and the IE appendix root alu- lists no alum/aluminium derivatives at all. It does not say the word is French.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"1966 ed. p.58 s.v. aluminum / aluminium\", \"stance\": \"contradicts\",\n       \"note\": \"'aluminum, also aluminium, n. — ModL., coined by the English chemist Sir Humphrey Davy (1778-1829) fr. L. alumen, ‘alum’. He gave the new element the name aluminum, but changed it later to aluminium.' Klein makes it an English/ModL coinage, not French.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. alum / aluminium\", \"stance\": \"partial\",\n       \"note\": \"FSD_vol1.txt gives alum '[OF. (F. alun), < L. alumen]' and cites 'C. L. Bloxam, Chemistry, Aluminium p.303' — the Romance route for alum, no French origin for the element name.\"},\n      {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. aluminum\", \"stance\": \"partial\",\n       \"note\": \"'[ALUMIN(A) + -(I)UM.]'\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"âlŭmîniyom «آلومینیم»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Persian آلومینیوم / آلومینیم ālūmīniy(u/o)m is a 20th-century scientific loan taken with French phonetics (ālūmīnyom, not English ə-lü-mi-nəm), which fits the general route by which chemical and technical vocabulary entered Persian — through French, the teaching language of the Dār al-Fonūn and of Iranian science until the mid-20th century. Wiktionary records exactly the two spellings the chart has: آلومینیوم with the alternative آلومینیم (āluminiyom). The route Latin alumen > French > Persian is therefore right; only the intermediate English/ModL coining step is missing (see node 2).\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/آلومینیوم\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"VOP:18\", \"status\": \"not_checked\",\n       \"note\": \"Moshiri, Farhang-e Vāžehā-ye Orūpāʾī dar Fārsī (Alborz 1371/1992) has no scan anywhere (re-searched archive.org, ketabnak, noorlib, Google Books, 2026-09); page 18 could not be read.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"vajehyab / abadis (فرهنگ معین)\", \"stance\": \"silent\",\n       \"note\": \"Neither vajehyab (HTTP 500 on the direct entry URL, JS-only SPA) nor abadis returned a Mo'in entry for آلومینیم; Mo'in's foreign-compounds volume (vol. 4) is not online.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin headword index\", \"stance\": \"silent\",\n       \"note\": \"grep of ARY_latin_index_pages.txt for ALUM/ALUMIN returns nothing — Aryanpur covers only inherited Indo-European vocabulary, not modern loans.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"ale ; alum ; alumina ; aluminum ; aluminium\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Four of the five words are correctly from Latin alūmen: alum (late 14c.) via Old French alum/alun; alumina, ModL. from alumen (on French alumine); aluminum (Davy, by 1812) and aluminium (proposed 1811) from alumina + -(i)um. But ALE cannot descend from Latin alūmen as the chart draws it: OE ealu/alu continues Proto-Germanic *aluþ- (ON öl, OS alo), a sister formation to alūmen from the same PIE stem *alu-t-/*alu-, and the Lithuanian alús and OCS olu ‘beer’ are Germanic loans, not cognates. Klein's own entry, which Nourai cites, says precisely that ale is 'cogn. with L. alumen' — cognate, not derived. So the node's parent is wrong for one of its five words.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/ale\",\n      \"https://www.etymonline.com/word/alum\",\n      \"https://www.etymonline.com/word/aluminum\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"OEW:84\", \"status\": \"not_checked\",\n       \"note\": \"Shipley 1984 is Internet-Archive lending-only; no full text available.\"},\n      {\"ref\": \"KLN:57\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt \\\\f-leaf 41 carries printed pp.57-58 with 'alum, n. — OF. alum (whence F. alun), fr. L. alumen'; 'alumina, n. ... fr. L. alumen, gen. aluminis'; 'aluminium, n. — The same as aluminum'; 'aluminum, also aluminium, n. — ModL., coined by the English chemist Sir Humphrey Davy ... fr. L. alumen'. All four alum-words on the cited page; ale is on p.46 and is called a cognate, not a descendant.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Ale\", \"stance\": \"contradicts\",\n       \"note\": \"'Ale. (E.) M.E. ale; A.S. ealu. + Icel., Swed. and Dan. öl; Lithuanian alus; Russ. ol', olovina.' Skeat marks ale '(E.)' = native English, with no Latin source.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. alum\", \"stance\": \"supports\",\n       \"note\": \"'[OF. (F. alun), < L. alumen.]' — the Old French intermediary for alum which the chart omits.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, ale-entries\", \"stance\": \"silent\",\n       \"note\": \"The scanned volume's ale/alum region gives only sense definitions in the OCR; no etymology recoverable.\"},\n      {\"src\": \"KLN\", \"where\": \"1966 ed. p.46 s.v. ale\", \"stance\": \"contradicts\",\n       \"note\": \"'ale, n. — OE. ealo, alo, rel. to ON. öl, and cogn. with L. alumen' — explicitly a cognate of alumen, not a derivative.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 3,\n   \"root\": \"Amalaka, Âmlak\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Sanskrit āmalaka- / āmalakī- (आमलक) 'emblic myrobalan, Phyllanthus emblica (Emblica officinalis)'\",\n   \"note\": \"The Sanskrit word is real and means what the chart says (Monier-Williams 146.3; attested MBh., Suśruta, Chāndogya Up.). Āmlaka is the by-form Klein prints as 'OI. āmlak'; both go with āmla- 'sour, acid' (the fruit is the sour Indian gooseberry), and the Malay name malaka of the same tree — from which the city and Straits of Malacca are named — is the same word. Nourai's whole four-step chain Sanskrit > Persian > Arabic > Medieval Latin > English is precisely Klein's entry and, behind it, Devic's; Wiktionary and Asbaghi agree.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/आमलक\",\n    \"https://en.wiktionary.org/wiki/emblic\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"KLN:513\", \"status\": \"partial\",\n     \"note\": \"Content supports fully — KLN_1966.txt \\\\f-leaf 273 s.v. emblic: 'ML. emblica, fr. āmleg, Egyptian pronunciation of Arab. amlaj, fr. Pers. amleh, ultimately fr. OI. āmlak, whence also Malay malaka, ‘emblic’ ... See Devic's Supplement to Littré's Dictionary. p.33.' The PAGE NUMBER does not match: leaf 273 of the 1966 two-volume scan carries printed pp.501-503 (leaf 266 = p.487, leaf 277 = p.508), and in the 1971 one-volume edition the entry is on pp.243-244. Nourai's '513' is off by about ten pages in either printing.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. MYROBALAN and s.v. MALACCA\", \"stance\": \"supports\",\n     \"note\": \"'(1) The Emblic myrobalan; which is the dried astringent fruit of the ānwalā, āmlā of Hind., the Emblica officinalis of Gaertner (Phyllanthus Emblica, L.) ... The Persian name of this is āmlah, but, as the Arabic amlaj suggests ...'; and s.v. Malacca: 'Malaka again seems to be a corruption of the Skt. amlaka, from amla, ‘acid’.'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck\", \"stance\": \"silent\",\n     \"note\": \"Buck's concept list has no section for this tree; grep of SYN.txt for emblic/amla returns nothing.\"},\n    {\"src\": \"AID\", \"where\": \"Whitworth, Anglo-Indian Dictionary s.v. Aonla\", \"stance\": \"supports\",\n     \"note\": \"'Aonla. [Corruption of the Hindi anola.] The myrobolan tree, phyllanthus emblica.'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Persian\",\n     \"words\": \"âmoleh «آمُلَه» : emblic tree\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Skt. āmalaka-/āmalakī- reached Persian with the usual Middle Indic-to-Iranian syncope of the medial vowel and loss of the final -ka: āmalaka- > *āmlak > MP *āmlag > NP آمله āmla/āmola, with the regular MP -ag > NP -a(h) outcome. The word entered Persian as a materia-medica term (the fruit is one of the three myrobalans of the compound tri-phalā, Arabic إطریفل). Asbaghi reconstructs the Middle Persian stage explicitly. The chart's extra spelling آمُلَج is the back-borrowed Arabicised form (muʿarrab) of the same word, which is exactly how Borhan-e Qateʽ presents it.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/أملج\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:61\", \"status\": \"supports\",\n       \"note\": \"BQT_v1_pages.txt \\\\f-leaf 271 (printed p.61): 'آمله ... دوائی است کثیرالنفع و معرب آن «آملج» باشد' — 'a very beneficial drug; its Arabicised form is āmlaj', with instructions for boiling it and dropping it in the eye. Supports both the Persian headword and the Persian→Arabic direction of node 2.\"},\n      {\"ref\": \"MON:90\", \"status\": \"not_checked\",\n       \"note\": \"The six-volume Mo'in is not online; abadis.ir returns no فرهنگ معین section for آمله and the local two-volume Adena abridgement's OCR is unusable for this headword.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, p.26\", \"stance\": \"supports\",\n       \"note\": \"'ʾamlaǧ: ‚Myrobalani Emblici; Fruchtschalen v. Phyllanthus Emblica“ pers. آمله āmle < mp. ambag' — Asbaghi's whole book is a list of Persian loanwords in Arabic, so this is a direct statement that Persian āmle is the source of Arabic ʾamlaǧ.\"},\n      {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. emblic\", \"stance\": \"supports\",\n       \"note\": \"'... fr. Arab. amlaj, fr. Pers. amleh, ultimately fr. OI. āmlak.'\"},\n      {\"src\": \"HJB\", \"where\": \"s.v. MYROBALAN\", \"stance\": \"supports\",\n       \"note\": \"'The Persian name of this is āmlah, but, as the Arabic amlaj suggests ...'\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Arabic\",\n     \"words\": \"amlaj\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic أَمْلَج ʾamlaj, the emblic myrobalan, is a Persian loan of the Sasanian/early-Abbasid medical vocabulary: Pers. āmla(g) was taken over with the final velar rendered as ج j (the regular Arabic substitution for Persian -g, cf. پهلوی barg > Ar. barj-type renderings) and fitted to the ʾafʿal pattern. It is standard in the Arabic pharmacopoeia — Ibn Sīnā, al-Qānūn fī l-ṭibb (1025) discusses الأملج as the base of Chinese sukk. Variants أملیج / أملیک are recorded. This is a one-way Indian>Persian>Arabic transfer, not a Persian>Arabic>Persian round trip, although Persian then re-borrowed the Arabicised آملج alongside its own آمله (the chart's 'extra' spelling).\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/أملج\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:513\", \"status\": \"partial\",\n       \"note\": \"KLN_1966.txt leaf 273 s.v. emblic states the step exactly: 'fr. āmleg, Egyptian pronunciation of Arab. amlaj, fr. Pers. amleh'. Only the page number is off (the entry sits on printed pp.501-503 of the 1966 edition, pp.243-244 of the 1971 one-volume edition).\"}\n      ],\n     \"consulted\": [\n      {\"src\": \"PLA\", \"where\": \"Asbaghi p.26 s.v. ʾamlaǧ\", \"stance\": \"supports\",\n       \"note\": \"Listed as a Persian loanword in Arabic: 'ʾamlaǧ ... pers. āmle'. Asbaghi also has šīrāmlaǧ < pers. شیرآمله, with a Syriac parallel.\"},\n      {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale, s.v. Emblic (p.~109)\", \"stance\": \"supports\",\n       \"note\": \"'C'est en effet l'arabe أملج amledj, qui est le persan آمله amleh, venant lui-même du sanscrit âmlak. أملج amledj est dans Razi (Trait. III, ch. xxviii).' Devic is the very source Klein refers to.\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾan\", \"stance\": \"silent\",\n       \"note\": \"grep of FVQ.txt/FVQ_pages.txt for amlaj/emblic returns nothing — the word is not Qurʾānic, so Jeffery does not treat it.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-Fārisiyya al-Muʿarraba\", \"stance\": \"silent\",\n       \"note\": \"grep of AFM.txt for أملج / amlaj returns nothing in the OCR (the file's Arabic layer is patchy).\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Middle Latin\",\n     \"words\": \"emblica\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Medieval Latin emblica / emblicus is the Latin translators' form of Arabic amlaj, taken not from Classical Arabic but from an Egyptian-Arabic pronunciation āmleg (Klein), whence the -g- appears as -c- and a prothetic e- develops before the cluster; the word entered Latin through the 11th-13th-century translations of Arabic materia medica (al-Rāzī's Continens, Avicenna's Canon) made in Salerno, Toledo and southern Italy, alongside the other myrobalans chebulus, bellericus, indus. Old Occitan amblic/emblich and Old Spanish ambliçi are parallel Romance takes on the Arabic word.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/أملج\",\n      \"https://en.wiktionary.org/wiki/emblic\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no reference in the book; the claim is however covered by Klein KLN:513 on the adjacent nodes ('ML. emblica, fr. āmleg, Egyptian pronunciation of Arab. amlaj').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"DEV\", \"where\": \"Devic s.v. Emblic\", \"stance\": \"supports\",\n       \"note\": \"'Latin du moyen âge emblicus (voy. Chebule), “emblica Arabes embelgi vocant” dit Jean Bauhin, d'après Garcias (Histor. plantarum univers.).' Devic also prints the medieval mnemonic 'Myrobalanorum species sunt quinque bonorum: Citrinus, Kebulus, Bellericus, Emblicus, Indus.'\"},\n      {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. emblic\", \"stance\": \"supports\",\n       \"note\": \"'ML. emblica, fr. āmleg, Egyptian pronunciation of Arab. amlaj.'\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs\", \"stance\": \"silent\",\n       \"note\": \"grep of LKT.txt for amlaj/emblic returns only unrelated -amla- strings (damla, kamla, ramla); Lokotsch has no entry for this drug name.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"emblic : a tree\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English emblic (also emblic myrobalan) is taken straight from the Medieval Latin drug name emblica/emblicus of the apothecaries, and denotes Phyllanthus emblica (formerly Emblica officinalis), the Indian gooseberry, whose dried astringent fruit was used against dysentery; French emblique, Italian emblico and Spanish emblico are the same borrowing. The English word therefore carries a chain Sanskrit āmalaka- > Persian āmla > Arabic amlaj > ML emblica > English emblic, exactly as the chart draws it.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/emblic\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:513\", \"status\": \"partial\",\n       \"note\": \"KLN_1966.txt leaf 273: 'emblic, n., name of an East Indian tree. — ML. emblica, fr. āmleg ... See Devic's Supplement to Littré's Dictionary. p.33.' Content exactly as drawn; the page number 513 does not match the 1966 pagination (pp.501-503 on that leaf) nor the 1971 one (pp.243-244).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\",\n       \"note\": \"grep of SKT.txt for emblic returns nothing — the word is too rare for Skeat's concise list.\"},\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. MYROBALAN\", \"stance\": \"supports\",\n       \"note\": \"Treats 'the Emblic myrobalan' as the English drug name of Emblica officinalis and traces the Arabic amlaj / Persian āmlah behind it.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls\", \"stance\": \"silent\",\n       \"note\": \"grep of the four FSD volumes for 'emblic' returns nothing usable in the OCR.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-50.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=1)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk50.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-50.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 50"
}
```


### [2026-09-04T19:56:24.282Z] TOOL RESULT

```
written
JSON OK
nodes verified: 13/13
node verdicts: {'disputed': 3, 'plausible': 5, 'confirmed': 5}
root verdicts: {'confirmed': 3}
ref checks: {'partial': 4, 'supports': 11, 'contradicts': 2, 'not_checked': 7}
books consulted: {'partial': 9, 'silent': 11, 'supports': 19, 'contradicts': 4} | by book: {'KLN': 5, 'CHEUNG': 4, 'FSD': 3, 'BRT': 2, 'AHD': 2, 'ARY': 2, 'MON': 2, 'KNT': 2, 'WLD': 2, 'SKT': 2, 'PLA': 2, 'HJB': 2, 'DEV': 2, 'HUB': 1, 'NYB': 1, 'PHD': 1, 'SYN': 1, 'IEC': 1, 'POK': 1, 'LAT': 1, 'WEB': 1, 'FVQ': 1, 'AFM': 1, 'LKT': 1}
```


## [2026-09-04T19:56:48.667Z] AGENT

Wrote `/home/sfmqrb/git/rishe/data/verification/page-50.json`; `verify_check.py 50` reports 13/13 nodes, no PROBLEM lines.

**Page 50 (book p. 20) — 3 non-redirect entries, 13 nodes**

- Root verdicts: 3 confirmed (Algwh, Alu, Amalaka).
- Node verdicts: 5 confirmed, 5 plausible, 3 disputed.
- Ref checks: 11 supports, 4 partial, 2 contradicts, 7 not_checked (OEW and VOP have no accessible copy; Mo'in's 6-vol MON is not scanned).
- Books consulted: POK, WLD I, AHD/Watkins, IEC, SYN, BRT, KNT, PHD, NYB, HRN, HUB, CHEUNG, SOD, BQT vols 1+4, ARY, KLN, SKT, FSD, WEB, LAT, DEV, PLA, HJB, AID, LKT, FVQ, AFM. 17 web pages archived via `fetch_source.py`.

Disputed items:
- **Algwh #1 (Avestan) — varejah/varecah "value"**: Av. varəcah- is 'vital power, splendour' (= Skt. várcas-, MP warč); Bartholomae's as-varəcah- = 'der grosse Kraft besitzt'. Different etymon.
- **Algwh #2 (Persian) — varj «ورج»**: both of Nourai's own cited pages contradict him — Horn 241 (no. 1077) derives verč/varj from Av. varəcah-/Skt. várcas- 'Glanz', and Mo'in's footnote at BQT 2265 does the same citing Bartholomae 1367; MacKenzie has ²warz 'miraculous power' and warzāwand = NP ورجاوند. arj/arz/arzān/Arjāsp on the same node are all solidly confirmed (Nyberg p.31, Hübschmann p.116, BQT 97/98/102).
- **Alu #4 (English) — ale**: cannot descend from Latin alūmen as drawn; OE ealu < PGmc *aluþ-, a sister formation. Klein's own cited entry says "cogn. with L. alumen". The other four words (alum, alumina, aluminum, aluminium) are correct.

Other notable findings (recorded, not flagged as disputed):
- JSON translit `rzân` for «ارزان» is a scan slip for *arzân*.
- **Alu #2 "French aluminium"**: Klein — "ModL., coined by the English chemist Sir Humphry Davy"; French contributed *alumine*, not the element name. Graded plausible since Persian did take it from French.
- **KLN:513** (Amalaka root and nodes 2/4) is a page-number miss: Klein's *emblic* entry is on pp. 501-503 of the 1966 two-volume edition (pp. 243-244 in the 1971 one-volume). Its content supports Nourai's chain verbatim, including "fr. Pers. amleh".
- **Algwh #3 (Old Persian arjana)**: real (DSf 23, 41f) but Kent glosses it 'ornamentation'; #4 Sogdian ʾyžn is genuine, though Gharib's own p.95 makes it a cognate (*arǰyan-), not a loan from Old Persian.
