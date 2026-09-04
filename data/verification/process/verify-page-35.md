# Verification process log — verify-page-35


## [2026-09-04T18:30:34.033Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 35 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-35.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-35.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-35.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 35` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T18:30:35.654Z] AGENT

I'll start by reading the instructions and the relevant files.


## [2026-09-04T18:30:37.787Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T18:30:37.798Z] TOOL RESULT

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


## [2026-09-04T18:30:38.022Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-35.txt"
}
```


### [2026-09-04T18:30:38.032Z] TOOL RESULT

```
1	=== PDF page 35 (book page 5) ===
2	--- entry 0 ---
3	ROOT [Hebrew] Âdhâmah : earth, red soil  (refs KLN:21; AHD:14)
4	#1 (parent #0) [Hebrew] refs=KLN:21 | Âdam, Âdâm : made from red soil (earth), man
5	  #2 (parent #1) [Arabic] refs=VDQ:106; FVQ:51 | Âdam
6	    #3 (parent #2) [Latin] refs=None | 
7	      #4 (parent #3) [English] refs=KLN:21; AHD:14 | Adam ; Adams : a common family name. | NOTE: Name of a gum manufacturer.
8	        #5 (parent #4) [Persian] refs=None | âdâms «آدامس» : chewing gum
9	  #6 (parent #1) [Persian] refs=MON5:12 | Âdam «آدم» | extra: آدمک ، آدمیزاد
10	--- entry 1 ---
11	ROOT [Indo-European] Ag, Agros : to drive; pasture (where cattle is driven)  (refs POK:4)
12	#1 (parent #0) [Avestan] refs=KLN:37; POK:4; PLA:194 | az : to drive ; azaiti : drives ; tara-âz, tara-âzu : balance driver, scale ☞Tel
13	  #2 (parent #1) [Persian] refs=BQT:480; PLA:194 | tarâz «تراز ، طراز» : level, balanced, well shaped ; tarâzu «ترازو» : balance, scale
14	#3 (parent #0) [Avestan] refs=POK:4; KLN:37 | ajras : pasture ; aštrâ 1 : whip ; ašaya : of both wings?
15	  #4 (parent #3) [Pahlavi] refs=SNS:35 | aštr, aštar : whip
16	    #5 (parent #4) [Persian] refs=SNS:35 | aštar «آشتَر ٢» : whip (obsolete) | NOTE: This word was not found in MON or BQT
17	#6 (parent #0) [Greek] refs=AHD | agein : to drive ; stratos-agein : leading the army, strategy ☞Ster 1
18	  #7 (parent #6) [French] refs=AHD:1273 | strategie
19	    #8 (parent #7) [Persian] refs=MON:246 | esterâtežî «استراتژی»
20	    #9 (parent #7) [English] refs=None | strategy
21	  #10 (parent #6) [English] refs=None | agony, agriculture
22	#11 (parent #0) [Latin] refs=AHD | agere : to drive ; agĕns : acting agent ; ag-sla : wing ; ambractus : envoy
23	  #12 (parent #11) [French] refs=None | agence, agent
24	    #13 (parent #12) [Persian] refs=VOP:10 | âžâns «آژانس» : agency ; âžân «آژان» : agent, policeman
25	  #14 (parent #11) [English] refs=None | act, acre, exact, -gate, navigate ; agent, agency ; axle, axis, ambassador, embassy
26	
```


## [2026-09-04T18:30:39.434Z] AGENT

I'll start by reading the supporting files and source JSON.


## [2026-09-04T18:30:42.185Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T18:30:42.222Z] TOOL RESULT

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


## [2026-09-04T18:30:43.378Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-35.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:6000])\n\"",
 "description": "Read page 35 JSON"
}
```


### [2026-09-04T18:30:46.654Z] TOOL RESULT

```
{
 "pdf_page": 35,
 "book_page": 5,
 "entries": [
  {
   "root": {
    "name": "Âdhâmah",
    "lang": "Hebrew",
    "refs": "KLN:21; AHD:14",
    "gloss": "earth, red soil"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Hebrew",
     "refs": "KLN:21",
     "words": [
      {
       "translit": "Âdam, Âdâm",
       "gloss": "made from red soil (earth), man",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Arabic",
     "refs": "VDQ:106; FVQ:51",
     "words": [
      {
       "translit": "Âdam",
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
     "lang": "Latin",
     "refs": null,
     "words": [],
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "English",
     "refs": "KLN:21; AHD:14",
     "words": [
      {
       "translit": "Adam",
       "gloss": null,
       "script": null
      },
      {
       "translit": "Adams",
       "gloss": "a common family name.",
       "script": null
      }
     ],
     "note": "Name of a gum manufacturer.",
     "quote": null
    },
    {
     "id": 5,
     "parent": 4,
     "lang": "Persian",
     "refs": null,
     "words": [
      {
       "translit": "âdâms",
       "gloss": "chewing gum",
       "script": "آدامس"
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 6,
     "parent": 1,
     "lang": "Persian",
     "refs": "MON5:12",
     "words": [
      {
       "translit": "Âdam",
       "gloss": null,
       "script": "آدم"
      }
     ],
     "script_extra": "آدمک ، آدمیزاد",
     "note": null,
     "quote": {
      "text": "آدمی در عالم خاکی نمی آید بدست - عالمی دیگر بباید ساخت وز نو آدمی",
      "poet": "Hâfez"
     }
    }
   ]
  },
  {
   "root": {
    "name": "Ag, Agros",
    "lang": "Indo-European",
    "refs": "POK:4",
    "gloss": "to drive; pasture (where cattle is driven)"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan",
     "refs": "KLN:37; POK:4; PLA:194",
     "words": [
      {
       "translit": "az",
       "gloss": "to drive",
       "script": null
      },
      {
       "translit": "azaiti",
       "gloss": "drives",
       "script": null
      },
      {
       "translit": "tara-âz, tara-âzu",
       "gloss": "balance driver, scale",
       "script": null,
       "see": [
        "Tel"
       ]
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Persian",
     "refs": "BQT:480; PLA:194",
     "words": [
      {
       "translit": "tarâz",
       "gloss": "level, balanced, well shaped",
       "script": "تراز ، طراز"
      },
      {
       "translit": "tarâzu",
       "gloss": "balance, scale",
       "script": "ترازو"
      }
     ],
     "note": null,
     "quote": {
      "text": "یاد باد آن شب که آن شمسهٔ خوبان تراز - به طرب داشت مرا تا بگه بانگِ نماز",
      "poet": "Farrokhî"
     }
    },
    {
     "id": 3,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:4; KLN:37",
     "words": [
      {
       "translit": "ajras",
       "gloss": "pasture",
       "script": null
      },
      {
       "translit": "aštrâ 1",
       "gloss": "whip",
       "script": null
      },
      {
       "translit": "ašaya",
       "gloss": "of both wings?",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "Pahlavi",
     "refs": "SNS:35",
     "words": [
      {
       "translit": "aštr, aštar",
       "gloss": "whip",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 5,
     "parent": 4,
     "lang": "Persian",
     "refs": "SNS:35",
     "words": [
      {
       "translit": "aštar",
       "gloss": "whip (obsolete)",
       "script": "آشتَر ٢"
      }
     ],
     "note": "This word was not found in MON or BQT",
     "quote": null
    },
    {
     "id": 6,
     "parent": 0,
     "lang": "Greek",
     "refs": "AHD",
     "words": [
      {
       "translit": "agein",
       "gloss": "to drive",
       "script": null
      },
      {
       "translit": "stratos-agein",
       "gloss": "leading the army, strategy",
       "script": null,
       "see": [
        "Ster 1"
       ]
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 6,
     "lang": "French",
     "refs": "AHD:1273",
     "words": [
      {
       "translit": "strategie",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 8,
     "parent": 7,
     "lang": "Persian",
     "refs": "MON:246",
     "words": [
      {
       "translit": "esterâtežî",
       "gloss": null,
       "script": "استراتژی"
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 9,
     "parent": 7,
     "lang": "English",
     "refs": null,
     "words": [
      {
       "translit": "strategy",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 10,
     "parent": 6,
     "lang": "English",
     "refs": null,
     "words": [
      {
       "translit": "agony, agriculture",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 11,
     "parent": 0,
     "lang": "Latin",
     "refs": "AHD",
     "words": [
      {
       "translit": "agere",
       "gloss": "to drive",
       "script": null
      },
      {
       "translit": "agĕns",
       "gloss": "acting agent",
       "script": null
      },
      {
       "translit": "ag-sla",
       "gloss": "wing",
       "script": null
      },
      {
       "translit": "ambractus",
       "gloss": "envoy",
       "script": null
      }
     ],
     "note": null,
     "quote":
```


## [2026-09-04T18:30:50.055Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -30 && echo \"---TOOLS---\" && sed -n 1,80p tools/verify_check.py",
 "description": "List verification dir and check script"
}
```


### [2026-09-04T18:30:50.106Z] TOOL RESULT

```
page-101.json
page-126.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
process
sources
---TOOLS---
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
```


## [2026-09-04T18:30:52.548Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['KLN','AHD','VDQ','FVQ','MON','POK','PLA','BQT','SNS']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"",
 "description": "Check refs_online entries"
}
```


### [2026-09-04T18:30:54.359Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaSc
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
```


## [2026-09-04T18:30:58.244Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-33.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3500])\n\"",
 "description": "Look at example verification file"
}
```


### [2026-09-04T18:31:00.339Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Ab 2",
 "verdict": "confirmed",
 "modern_form": "Proto-Semitic *ʾab- / *ʾabw- 'father'",
 "note": "The root box is right: Proto-Semitic *ʔabw- 'father' (Akk. abum, Ugar. ʾabu, Heb. ʾāḇ, Aram. ʾabbā, Arab. ʾab, Geʿez ʾab), an old nursery word, ultimately Proto-Afroasiatic; Klein s.v. Aboth says exactly this ('of uncertain origin, possibly traceable to *ab(a), a child's word for father'). Nourai's '2' is his homograph number (Ab 1 = water). Two branches of the chart are problematic and both hang on Arabic kunya-compounds in node #3: (a) the gibbon branch — Persian بوزینه is an inherited Iranian word (Wiktionary: inherited from Proto-Iranian, cf. Pashto bīzo; attested as būzīna, pl. būzīnagān already in the early NP Qurʾān commentary per Hübschmann, and lent onward to Old East Slavic obezĭjána and Old Turkic béčin) and French gibbon is of unknown origin, so the whole Arabic abū-zīnā > būzīne > bojīna > gibbon chain collapses; (b) the borage branch — Arabic abū ʿaraq 'father of sweat' as the source of Med.Lat. borrāgō is supported by Klein, AHD, Lokotsch no. 13 and Pihan, but rejected by Skeat, Webster and the OED/Etymonline in favour of Lat. borra/burra 'rough hair', so it is a live scholarly split, not a settled fact. Two printed-book errors (not extraction errors — checked against the page scan at 600 dpi): 'borrâco' in node #8 is a misprint for borrāgō, and 'Jaob' in node #16 for Joab. The JSON's «آبو» in node #2 IS an extraction artefact: the book prints أَبو (alef+hamza+fatha), read by OCR as alef-madda.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/%CA%BEab-",
  "https://en.wiktionary.org/wiki/%D8%A3%D8%A8"
 ],
 "ref_check": [
  {
   "ref": "FVQ:44",
   "status": "partial",
   "note": "FVQ_pages.txt leaf 62 = printed p. 44: the page is Jeffery's article on أبابيل and the opening of إبراهيم; it mentions the word for father only in passing ('deriving it from أبو = father and أبيل = lamentation'). Jeffery has no article on the Semitic root *ʾab as such, so p. 44 supports the names branch (below) rather than the root box."
  },
  {
   "ref": "KLN:6",
   "status": "supports",
   "note": "KLN_1966.txt \\f-leaf 15 (= printed p. 6, matches the leaf≈floor(p/2)+12 rule) s.v. 'Aboth, also Abot': 'Heb. Abhōth, pl. of ābh, \"father\", rel. to Aram. ābh (absolute state), abbā (emphatic state), Ugar. ʾb, Arab. ab, Ethiop. ab, \"father\"; of uncertain origin, possibly traceable to *ab(a), a child's word for father. Cp. the first element in Abraham, Abner, Absalom, Abigail, and the second element in Joab, Moab, Barabbas… Cp. also borage.' This one page is the source of almost the whole chart."
  }
 ],
 "nodes": [
  {
   "id": 1,
   "lang": "Arabic",
   "words": "ab, abŭ, a.b.v",
   "verdict": "confirmed",
   "derivation": "Arabic أَبٌ ʾab-un 'father' continues Proto-Semitic *ʔabw- directly; the third radical wāw survives in the construct/nominative أَبُو ʾabū (acc. أَبَا ʾabā, gen. أَبِي ʾabī) — the 'six nouns' (al-asmāʾ al-sitta) declension — and in the plural آبَاء ʾābāʾ and the nisba أَبَوِيّ ʾabawī. Nourai's 'a.b.v' is his notation for the root ء ب و (ʾ-b-w), with v = wāw; that is exactly the root under which Wiktionary and the Arabic lexica file the word. ʾabū is the element that opens a kunya (Abū ʿAlī) and, by the same idiom, hundreds of Arabic plant- and animal-names ('father of X').",
   "sources": [
    "https://en.wiktionary.org/wiki/%D8%A3%D8%A8",
    "https://en.wiktionary.org/wik
```


## [2026-09-04T18:31:01.726Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['KLN','AHD','POK','FVQ','PLA','BQT','MON','SNS','VDQ']:\n    v=d.get(k) or {}\n    print(k,'| local:',v.get('local_file'),'| offset:',v.get('page_offset'))\n\"",
 "description": "Get page offsets"
}
```


### [2026-09-04T18:31:03.657Z] TOOL RESULT

```
KLN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
AHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
POK | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
FVQ | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] | offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves)
PLA | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] | offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
BQT | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
MON | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None
SNS | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt'] | offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
VDQ | local: None | offset: None
```


## [2026-09-04T18:31:07.427Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 21 22 23; do echo \"=== KLN_1966 leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | head -60; done",
 "description": "KLN leaves around p.21"
}
```


### [2026-09-04T18:31:09.280Z] TOOL RESULT

```
<persisted-output>
Output too large (36.5KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b9pl362hx.txt

Preview (first 2KB):
=== KLN_1966 leaf 21 ===
.  pref.  a-, xoop.0?,  ‘the  world’  (see  cosmos),  and  suff.  -ism. acosmist,  n.,  one  who  believes  in  acosmism.
See  prec.  word  and  -ist.
Derivative:  acosmist-ical,  adj. acotyledon,  n„  a  plant  without  cotyledons  (bot) —  See  priv.  pref.  a-  and  cotyledon, acotyledonous,  adj.,  having  no  cotyledons.  — Formed  fr.  acotyledon  with  suff,  -ous. acouchy,  n.,  a  species  of  agouti.  —  F.  acouchi, of  Tupi  origin.
acoumeter,  n.,  an  instrument  for  measuring  the sense  of  hearing  —  Compounded  of  the  stem of  Gk.  dxoustv,  ‘to  hear’,  and  licxpov,  ‘meas¬ ure’.  See  acoustic  and  meter,  ‘poetical  rhythm  . -acousia,  -acousis,  combining  forms  meaning ‘hearing’.  —  Fr.  Gk.  dxooaic,  hearing ,  fr. axouEiv,  ‘to  hear’.  See  acoustic, acoustic,  adj.  —  F.  acoustique,  fr.  Gk.axouoxtxo^, pertaining  to  hearing’,  fr.  axoucrxi;,  ‘heard, audible’,  verbal  adj.  of  dxoueiv,  ‘to  hear’,  which stands  for  *dxou<n.Etv,  and  is  prob.  formed  fr. copul.  pref.  d-(sce  acolyte)  and  I.-E.  base  *(s)qeu-, *(s)qeu-,  ‘to  look  at,  observe,  perceive’,  whence also  xoeIv,  ‘to  mark,  perceive,  hear’,  Goth. hausjan,  OE.  hyran,  ‘to  hear".  See  hear  and  cp. show.  Some  scholars  explain  Gk.  dxoueiv  as standing  for  *ax-ouo-iEiv,  ‘to  have  a  sharp ear’,  fr.  I.-E.  base  *ak-,  ‘sharp’  and  *ous,  ‘ear’; see  acrid  and  ear.  See  Frisk,  GEW.,  I,  57-58. Derivatives:  acoustic-al,  adj.,  acoustic-al-ly, •dv.,  acoust-ics,  n.
■cquaint,  tr.  v.  —  ME.  acointen,  fr.  OF.  acoin- Her,  acointer,  fr.  Late  L.  aecognitare,  ‘to  make
known,  to  acquaint’, fr.  L.  accognitus,' acquainted with’,  fr.  ad-  and  cognitus,  pp.  of  cognoscere, ‘to  know’.  See  cognition  and  cp.  quaint. Derivatives:  acquaintance  (q.v.),  acquaint-ed, adj.,  acquaint-ed-ness,  n. acquaintance,  n.  —  OF.  acointance,  fr.  acointier.
...
</persisted-output>
```


## [2026-09-04T18:31:09.411Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"adamah\\|ădhāmāh\\|adhamah\" KLN_1966.txt | head -20; echo \"--- AHD ---\"; grep -n -i \"adam\\b\\|dhghem\\|Adamah\" AHD_watkins1985.txt | head -20",
 "description": "Grep adamah in KLN and AHD"
}
```


### [2026-09-04T18:31:09.489Z] TOOL RESULT

```
--- AHD ---
137:A word for the earth can be reconstructed as dhghem- (*dheghom). Other terms of lesser distribution designated forest or uncul- tivated land, like kaito- and welt- (wILD). Swampy or boggy terrain was apparently also familiar, from the evidence of the roots sel-es-, pele-', and *mdno-. But since none of these runs through the whole family, it would not be justifiable to infer anything from them regarding the terrain of a hypo- thetical original homeland of the Indo- Europeans.
150:Man and Society. For man himself, a number of terms were employed, with differ- ent nuances of meaning. The general terms for “man” and “woman” are wi-ro- (VIRILE) and *g”end- from g’en- (GYNECOLOGY). For man as a human being, the oldest word was apparently *manu- (man-'), as preserved in English MAN and in Slavic and Sanskrit. In other dialects we find interesting metaphori- cal expressions, which attest a set of religious concepts opposing the gods as immortal and celestial to mankind as mortal and terres- trial. Man is either *mortos, “mortal” (mer-2, “to die’), or *dhghomyo-, ‘“‘earthling”’ (dhghem-, “earth”).
287:ar-. Also are-. To fit together. I. Basic form *are-. 1. Suf- fixed form *ar(g)-mo- in: a. Germanic armaz in Old English earm, arm: ARM}; b. Latin arma, tools, arms: ARM?2, ARMADA, ARMADILLO, ARMATURE, ARMOIRE, ARMY; ALARM, DISARM; C. Latin armus, upper arm: ARMILLARY SPHERE. 2. Suffixed form *ar(e)-smo- in Greek harmos, joint, shoulder: HARMONY. 3. Suffixed form *ar()-ti- in: a. Latin ars (stem art-), art, skill, craft: ART!, ARTEL, ARTISAN, ARTIST; INERT, (INERTIA); b. fur- ther suffixed form ‘*ar()-ti-o- in Greek artios, fitting, even: ARTIODACTYL. 4, Suffixed form *ar()-tu- in Latin artus, joint: ARTICLE. 5. Suffixed form *ar()-to- in Latin artus, tight: COARCTATE. 6. Suffixed form “*ar(e)-dhro- in Greek arthron, joint: ARTHRO-; ANARTHROUS, DIAR- THROSIS, ENARTHROSIS, SYNARTHROSIS. 7. Suffixed (su- perlative) form *ar(g)-isto- in Greek aristos, best: ARISTOCRACY. II. Possibly suffixed variant form (or separate root) *dr-dh-. 1. Latin drdé, order (originally a row of threads in a loom): ORDAIN, ORDER, ORDINAL, ORDINANCE, ORDINARY, ORDINATE, ORDO; COORDINA- TION, INORDINATE, SUBORDINATE. 2. Latin drdiri, to begin to weave: EXORDIUM, PRIMORDIAL. 3. Latin or- ndre, to adorn: ORNAMENT, ORNATE; ADORN, SUBORN. III. Variant or separate root *ré- (< *reo-). 1. Latin réri (past participle ratus), to consider, confirm, ratify: RATE!, RATIO, REASON; (ARRAIGN). 2. Suffixed form ré-dh- in: a. Germanic *rédan in (i) Old English rédan, to advise: READ, REDE (ii) Old English réden, condition: HATRED, KINDRED; b. Germanic *rédaz in (i) Old High German rat (> German Rat), counsel: BUNDESRAT, RATHSKELLER (ii) Old English rédels(e), opinion, riddle: RIDDLE?. 3. Zero-grade form *ra- in Germanic *radam, number (see dekm). IV. Variant (or separate root) *ri-. 1. Suffixed form *ri-tu- in Latin ritus, rite, custom, usage: RITE. 2. Suffixed form *(a)ri-dhmo- in Greek arithmos, number, amount: ARITHMETIC, LOGARITHM. [Pok. 1. ar- 55.]
362:DECENT. 2. Suffixed (causative) o-grade form *dok-eye- in: a. Latin docére, to teach (< “to cause to accept”): DOCENT, DOCILE, DOCTOR, DOCTRINE, DOCUMENT; b. Greek dokein, to appear, seem, think (< “to cause to accept or be accepted”): DOGMA, (DOGMATIC); DOCETISM, DOXOLOGY, HETERODOX, ORTHODOX, PARADOX. 3. Suf- fixed form *dek-es- in: a. Latin decus, grace, ornament: (DECOR), DECORATE; b. Latin decor, seemliness, elegance, beauty: DECOROUS. 4. Suffixed form *dek-no- in Latin dignus, worthy, deserving, fitting: DAINTY, DEIGN, DIG- NITY; CONDIGN, DIGNIFY, DISDAIN, INDIGN, INDIGNANT, INDIGNATION. 5. Reduplicated form *di-dk-ske- in Latin discere, to learn: DISCIPLE, (DISCIPLINE). 6. Greek dekh- esthai, to accept: PANDECT, SYNECDOCHE. 7. Greek dok- os, beam, support: DIPLODOCUS. [Pok. 1. dek- 189.] dek-2. Referring to such things as a fringe, lock of hair, horsetail. 1. Suffixed o-grade form *dok-lo- in Germanic *taglaz in Old English teg(e)l, tail: TAIL!. 2. Perhaps Germanic *tag- in: a. Swedish tagg, prickle, akin to the Scandinavian source of Middle English tagge, pendent piece: TAG!; b. Middle High German zacke, nail (> German Zacken, point): SHAKO; Cc. Old French tache, fastening, nail: TACHE, TACK!. [Pok. 2. dek- 191.] dekm. Ten. I. Basic form *dekm. 1. Germanic *tehun in: a. Old English tien, ten: TEN; b. Old Norse an, ten (see oktd(u)). 2. Latin decem, ten: DECEMBER, DECEMVIR, DECI-, DECIMAL, DECIMATE, DECUPLE, DICKER, DIME; (DECENARY), DECENNIUM, DECUSSATE, DOZEN, DUODECI- MAL, OCTODECIMO, SEXTODECIMO. 3. Irregular Latin distributive dani, by tens, ten each (formed by analogy with néni, nine each): (DENARIUS), DENARY, (DENIER?). 4. Greek deka, ten: DEAN, DECA-, DECADE, (DECANAL), (DOYEN); DECAGON, DODECAGON. II. Extended form *“dekmt- in Germanic *-tig in Old English -tg, ten (see dwo-). III. Ordinal number *dekmto- in Germanic *te- guntha- in Old English teogotha, téotha, tenth: TENTH, (TITHE). IV. Suffixed zero-grade form *-dkm-ta, reduced to -kmtd, and lengthened o-grade form *-dk6m-ta, re- duced to *-kontd. 1. Latin -gintd, ten times: NONAGE- NARIAN, OCTOGENARIAN, SEPTUAGINT, SEXAGENARY. 2. Greek *-konta, ten times: PENTECOST. V. Suffixed zero-grade form *dkm-tom, hundred, reduced to kmtom. 1. Germanic *hundam, hundred, in Old English hundred, hundred (-red, from Germanic *radam, number; see ar-): HUNDRED. 2. Germanic *thiis-hundi, “swollen hundred,” thousand (see teue-). 3. Latin centum, hundred: CENT, CENTAL, CENTAVO, (CENTENARIAN), CENTENARY, CEN- TESIMAL, CENTI-, CENTIME, (CENTNER), CENTUM, CEN- TURY; CENTENNIAL, PER CENT, QUATROCENTO, SEICENTO, (SEN!), (SEN2), (SENITI), SEXCENTENARY, TRE- CENTO. 4. Greek hekaton, a hundred (? dissimilated from *hem-katon, one hundred; see sem-'): HECATOMB, HECTO-. 5. Avestan satam, hundred: SATEM. See also compound root wikmti. [Pok. dekm 191.] deks-. Right (opposite left); hence, with an eastward orientation, south. Suffixed form *deks(i)-tero- in Latin dexter, right, on the right side: DESTRIER, DEXTER, DEXTERITY, DEXTRO-; AMBIDEXTROUS. Compare ner-'. [In Pok. 1. dek- 189.] del-'. Long. Probably extended and suffixed zero-grade form *dlon-gho-. 1.Germanic *langaz, long, in: a. Old English lang, long, long (comparative lengra): LINGER, LoNG!; b. Old High German lang (> German Jang), long: LANGLAUF; C. Old English denominative langian, to grow longer, yearn for: LONG?; d. Latin compound Lon- gobardus, Langobardus (with Germanic ethnic name *Bardi): LOMBARD. 2. Germanic abstract noun */lang- ithé in: a. Old English lengthu, length: LENGTH; b. West Germanic */angitinaz, lengthening of day, in Old English lengten, lencten, spring, Lent: Lent; ¢. Dutch lenghe, linghe, “long one,” akin to the Low German source of Middle English lenge, ling, ling: LING}. 3. Latin longus (> French long), long: LONGERON, LONGITUDE; ELOIGN, ELONGATE, LONGEVITY, LUNGE, OBLONG, PROLONG, PUR-
364:LOIN. 4. Possibly suffixed variant *dlo-gho- in Greek dolikhos, long: DOLICHOCEPHALIC, DOLICHOCRANIAL. [Pok. 5. del- 196.] del-2. To recount, count. 1. Germanic *taljan in Old English tellan, to count, recount: TELL. 2. Germanic *tal6é in: a. Old English talu, story: TALE; b. Middle Dutch dle, speech, language: TAAL. 3. Old English denominative talian, to tell, relate, probably akin to the source of Middle English talken, to talk: TALK. 4. Per- haps Greek dolos, ruse, snare: DOLERITE. [Pok. 1. del- 193.] del-3. To split, carve, cut. 1. Suffixed form *del-to- in Germanic *teldam, “thing spread out,” in Old English teld, awning, tent: TILT?. 2. Germanic extended form *telg- in Old English telgor, telgra, twig, branch: TILLER’. 3. Perhaps o-grade form *dol-é- in Latin dolére, to suffer (? < “to be beaten”): DOLE?, DOLOR; CONDOLE, INDO- LENT. 4. Suffixed o-grade form *dold-dhraé in Latin dolabra, a heavy chopping tool (< doldre, to chisel, hew): DOLABRIFORM. [Pok. 3. del- 194.] del-*. To drip. Perhaps suffixed (stative) o-grade form *dol- in Germanic *talgaz in Middle Low German falg, talch, tallow (< “dripping fat”), perhaps akin to the source of Middle English talow, tallow: TALLOw. [Pok. 4. del- 196.] deme-'. Also dem-. House, household. 1. Suffixed re- duced o-grade form *dom-o-, dom-u-, house, in: a. Latin domus, house: DOME, DOMESTIC, DOMICILE; MAJOR- DOMO; b. suffixed form *dom-o-no- in Latin dominus, master of a household (feminine domina > Old French dame, lady): DAME, DAN?, DANGER, DoM, DOMAIN, DOMI- NATE, DOMINICAL, DOMINIE, DOMINION, DOMINO}, (DOM- INO2), DUENNA, DUNGEON; (MADAM), MADAME, MADEMOISELLE, MADONNA, PREDOMINATE. 2. Com- pound *dems-pot-, “house-master” (*-pot-, powerful; see poti-), in Greek despotés, master, lord: DESPOT. 3. Root form *dem()-, to build (possibly a separate root), in: a. Germanic *timram in Old English timber, building material, lumber: TIMBER; b. Germanic *tumfté in Old Norse topt, homestead: Torr. [Pok. dem- 198.] deme-2. To constrain, force, especially to break in (horses). 1. Suffixed o-grade form *dom-o- in Germanic *tamaz in Old English tam, domesticated: TAME. 2. O-grade form *doma- in Latin domdre, to tame, sub- due: DAUNT; INDOMITABLE. 3. Zero-grade form *dmo- in Greek daman, to tame (> adamas, unconquerable): ADAMANT, DIAMOND. [Pok. (dema-), doma- 199.] denk-. To bite. 1. Germanic *tanhuz in Old English toh, tenacious, sticky (< “holding fast”): TOUGH. 2. Germanic *tanguz in Old English tang(e), tong(e), pincers, tongs: TONGS. 3. Germanic *tang- in Old Norse tangi, a point, sting, akin to the Scandinavian source of Middle English tonge, tange, point, tang: TANG!. 4, Germanic *teng- in Old High German zinko, spike, prong: z1Nc. [Pok. denk- 201.) dens-'. To use mental force. Reduplicated and suffixed zero-grade form *di-dns-sko- in Greek didaskein, to teach: pipactic. [Pok. 1. dens- 201.] dens-2. Dense, thick. 1. Suffixed form *dens-o- or *dns-o- in Latin dénsus, thick: DENSE; CONDENSE. 2. Suffixed zero-grade form *dns-u- in Greek dasus, hairy, shaggy: DASYURE. [Pok. 2. dens- 202.] dent-. Tooth. (Originally participle of ed- in the earlier meaning “to bite.”) 1. O-grade form *dont- in Germanic *tanthuz in Old English toth, tooth: TOOTH. 2. Zero-grade form *dné- perhaps in Germanic *tunth-sk- in Old English tisc, tix, canine tooth: TUSK. 3. Full-grade form *dent- in Latin déns (stem dent-), tooth: DENTAL, DENTATE, DENTI-, DENTICLE; (BIDEN- TATE), DANDELION, EDENTATE, INDENT!, (INDENTURE), TRIDENT. 4. O-grade variant form *(o)dont- in Greek odén, odous, tooth: -ODON, -ODONT, ODONTO-; CERATO- Dus. [In Pok. ed- 287.] deph-. To stamp. 1. Suffixed form *deph-s-ter- in Greek
382:blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
818:ANTIPODES, APODAL, APPOGGIATURA, APUS, CALIBER, LYCOPODIUM, MONOPODIUM, OCTOPUS, PELECYPOD, PHALAROPE, PLATYPUS, PODAGRA, PODIATRY, PODOPHYL- LIN, POLYP, POLYPOD, SYMPODIUM; b. Russian pod, un- der: PODZOL. 8. Suffixed form *ped-ya in Greek peza, foot: TRAPEZIUM. 9. Suffixed form *ped-o- in: a. Greek pedon, ground, soil: PEDO-!; PARALLELEPIPED; b. San- skrit padam, footstep, foot, and pat (> Hindi paisd), foot: PAISA, PICE, PIE’, PUG3; c. Middle Persian pdi, leg, foot: PAJAMAS, TEAPOY; d. lengthened-grade form *pédo- in (i) Greek pédon, rudder, steering oar: PILOT (ii) Greek pédan, to leap: DIAPEDEsIs. 10. Suffixed form *ped-i- in Greek pedilon, sandal: CYPRIPEDIUM. II. Verbal root *ped-, to stumble, fall. 1. Germanic *fetén in Old English fetian, feccean, to bring back: FETCH!. 2. Latin *ped- in: a. suffixed (comparative) form *ped-yos in Latin péor, worse (< “stumbling”): PEJORATION; IMPAIR; b. suffixed (superlative) form *ped-samo- in Latin pessimus, worst: PESSIMISM; C. suffixed form *ped-ko- in Latin peccdre, to stumble, sin: PECCABLE, PECCADILLO, PECCANT; IMPEC- CABLE. [Pok. 2. péd- 790.]
1270:AUSPICE awi-, spek- AUSTERE saus- AUTACOID y@k- AUTARCHY arkhein AUTARKY arek- AUTHOR aug-! AUTHORIZE aug-! AUTOBAHN g*hen-* AUTOCHTHON dhghem- AUTOECIOUS weik-1 AUTOGIRO géu- AUTOMATIC men-1 AUTONOMOUS nem-
1313:BOLD bhel-2 BOLE! bhel-2 BOLL bhel-2 BOLLIX bhel-2 BOLOMETER gW¥ele-1 BOLSHEVIK bel- BOLSTER bhelgh- BOLT! bheld- BOMB bamb- BOMBARD bamb- BONANZA deu-2 BONBON deu-2 BOND bhendh- BONDAGE bheue- BONHOMIE deu-2, dhghem- BONITO deu-2 BONNE deu-2 BONNYCLABBER band- BONTEBOK bhugo- BONUS deu-2 BOOBY baba- BOODLE bheue- BOOK bhago-
1323:BREEKS brak- BREEZE bhreu-2 BREGMA mregh-m(n)o- BREMSSTRAHLUNG | ster-2 BREW bhreu-2 BREWIS bhreu-2 BRIAR! wer-3 BRIDE? bherek- BRIDEGROOM dhghem- BRIDGE! bhri- BRIDLE bherek- BRIEF mregh-u- BRIGHT bherag- BRIM bhrem-2 BRIMSTONE gWher- BRINDLED gWher- BRING bher-!
1342:CENTROBARIC gWere-2 CENTUM dekm CENTURY dekm CEPHALIC ghebh-el- CEPHALO- ghebh-el- -CEPHALOUS ghebh-el- CERAMIC ker-4 CERASTES ker-! CERATODUS dent-, ker-1 CERATOID ker-! CEREAL ker-3 CEREBELLUM ker-1 CEREBRUM ker-1 CERES ker-3 CERTAIN krei- CERVINE ker-1 CERVIX ker-1 CESSION ked- CESSPOOL spirare cEsTus! kent- CEsTUS? kae-id- CHAETA ghait- CHAETOGNATH genu-2, ghait- CHAFE dhé-1, kele-1 CHAFER gep(h)- CHAFF! gep(h)- CHAIR sed-1 CHALAZA gheled- CHALAZION gheled- CHALCID ghelegh- CHALCOCITE ghelegh- CHALCOPYRITE ghelegh- CHALCOsIS ghelegh- CHALICE kal-1 CHALLENGE kel-8 CHALONE ghé- CHAMAEPHYTE dhghem- CHAMBER kamer- CHAMELEON dhghem- CHAMFER bhreg- CHAMFRON kaput CHAMOMILE dhghem-, mélon CHANCE kad- CHANCEL carcer CHANCELLOR carcer CHANCRE kar-1 CHANGE skamb- CHANT kan-
1357:CHOLE- ghel-2 CHOLER ghel-2 CHOLERA ghel-2 CHOLESTEROL ster-1 CHOLINERGIC werg- CHOLLA g(e)u-lo- CHONDRO- ghrendh- CHONDROMALACIA mel-1 CHOOSE geus- CHORAGUS_§ ag-, gher-1 CHORAL gher-1 CHORALE gher-1 CHORD? ghere- -CHORE ghé- CHORIC gher-1 CHORION ghere- CHORISTER gher-! CHOROGRAPHY ghé- CHORUS gher-1 CHOWDER kele-1 CHRESARD gher-5 CHRESTOMATHY gher-5, mendh-1 CHRISM ghréi- Curist ghréi- CHRISTEN ghréi- CHRISTIAN ghréi- CuRIsTMas ghréi- CHROMA ghréu- CHROMATIC ghréu- CHROMATO- ghréu- -CHROME ghréu- CHROMIUM ghréu- CHROMO- ghréu- CHROMONEMA (s)né- CHRONAXY ag- CHRYSANTHEMUM § andh- CHTHONIC dhghem- CHUFA swei-! CHUKAR kau-! CHUKKER kwel-1 CHURCH keue-? CHURL karlaz CHUTE kad-
1485:EXAMINE ag- EXAMPLE em- EXANTHEMA andh- EXARCH arkhein EXCALIBUR kal-3 EXCAVATE keue-2 EXCEED ked- EXCEL kel-6 EXCEPT kap- EXCERPT kerp- EXCISE? kae-id- EXCITE kei-3 EXCLAIM kela-2 EXCLUDE kleu-3 EXCORIATE sker-1 EXCREMENT krei- EXCRESCENCE ker-3 EXCURSION kers-2 EXECRATE Sak- EXECUTE sekw-1 EXEDRA sed-1 EXEGESIS sag- EXEMPLARY em- EXEMPLIFY em- EXEMPLUM em- EXEMPT em- EXERCISE arek- EXERGONIC werg- EXERGUE werg- EXERT ser-3 EXFOLIATE bhel-3 EXHAUST aus-2 EXHIBIT ghabh- EXHILARATE sel-2 EXHORT gher-5 EXHUME dhghem- EXIGENT ag-
1560:GEODE gé GEODESY da- GEOMETRY mé-2 GEOPONIC (s)pen- GEORGIC gé, werg- GERANIUM gera-2 GERENT gerere GERIATRICS gera-1 GERM gene- GERMAN? gena- GERMANDER deru, dhghem- GERMANE gene- GERMINAL gene- GERMINATE gene- GERONTO- gera-1 GERUND gerere GEST gerere GESTALT stel- GESTATION gerere GESTICULATE gerere GESTURE gerere GET ghend- GEYSER gheu- GHAT gher-4 GHOST gheis- GIDDY gheu(e)- Girt ghabh- GILD! ghel-2 GILL! ghel-una GILLS ghai- GILLYFLOWER bhel-3, kar-1 GILT2 ghel-3 GIMMAL yem- GINGERLY gene- GIRASOL sawel- GIRD gher-1 GIRDLE gher-1 GIRTH gher-1 GIST yé-
1638:HOMAGE dhghem- HOMBRE dhghem- HOME tkei-
1639:HOMEO- sem-! HOMICIDE dhghem- HOMILY sem-1 HOMINID dhghem- HOMO! dhghem- HOMO- sem-1 HOMOIOUSIAN eS- HOMOLOGOUS leg-1 HOMOLOGRAPHIC sem-1 HOMOLOSINE PROJECTION HOMONYMOUS nO-men- HOMUNCULUS dhghem- HONE! k6-
1658:HUM kem-3 HUMAN dhghem- HUMANE dhghem- HUMBLE dhghem- HUMECTANT wegw- HUMERUS omeso- HUMID wegw- HUMILIATE dhghem- HUMILITY dhghem- HUMOR wegw- HUMUS dhghem- HUNDRED dekm HUNGER kenk-2 HUNKER keu-2 HURDLE kert- HUSBAND bheue- HUSSAR kers-2 HUSTINGS tenk-1 HUT (s)keu- HYATHODE sed-2 HYDATHODE wed-1 HYDATID wed-1 Hypra_ wed-! HYDRANT wed-! HYDRANTH andh- HYDRAULIC aulo- HYDRO- wed-1 HYDROCEPHALUS ghebh-el- HYDROMEL melit- HYDROUS wed-1 Hyprus_ wed-! HYENA sil- HYGEIA gWei- HYGIENE gWej- HYGRO- wegw- HYLOZOISM _hulé HYMEN  syil- HYMNODY wed-2 HYOSCINE si- HYPER- uper HYPERBOLA gWele-1 HYPERBOLE gWelg-1 HYPERBOREAN gWere-1 HYPERKINESIA kei-3 HYPERPNEA pneu- HYPHA webh- HYPNAGOGIC ag- HYPNO- swep-! Hypnos swep-! HYPNOSIS swep-1 HYPNOTIC swep-1 HYPO- upo HYPOCHONDRIA ghrendh- HYPOCORISM ker-3 HYPOGEAL gé HYPOPHYSIS bheue- HYPOPNEA pneu- HYPOSTASIS sta- HYPOSTYLE sta- HYPOTAXIS tag- HYPOTENUSE ten- HYPOTHERMIA gWher- HYPOTHESIS dhé-1 HYPROCRISY krei- HYPSO- upo HYSTERESIS ud- HYSTERIC udero- HYSTERO- udero- HYSTERON PROTERON per!, ud-
1678:INERTIA ar- INEXORABLE 6r- INFAMOUS bha-2 INFANT bha-2 INFANTRY bha-2 INFARCT bhrekw- INFECT dhé-1 INFELICITY dhé&(i)- INFER_ bher-1 INFERIOR ndher- INFERNAL ndher- INFERNO ndher- INFEST dhers- INFEUDATION peku- INFIDEL bheidh- INFIRM dher-2 INFIRMARY dher-2 INFIX dhigw- INFLAME bhel-1 INFLATE bhié-2 INFLICT  bhiig- INFLUENCE bhieu- INFLUENZA bhleu- INFRA- ndher- INFRACT bhreg- INFRANGIBLE bhreg- INFRINGE bhreg- INFUSE gheu- INGENIOUS gene- INGENUOUS gene- INGEST gerere INGRATE gWere-3 INGRATIATE gWere-3 INGRESsS ghredh- INGUINAL engW- INGURGITATE gWere-4 INHABIT ghabh- INHERE ghais- INHERIT ghé- INHIBIT ghabh- INHUME dhghem- INIMICAL amma INITIAL ej-1 INITIATE ei-1 INJECT yé- INJUNCTION yeug- INJURY yewes- INK kéu-
1791:MADAM deme-! MADAME deme-1 MADDER! modhro- MADEMOISELLE deme-1 MADONNA deme-1 MADREPORE miater- MADURO ma-1 MAELSTROM mele-, sreu- MAENAD men-! MAESTOSO meg- MAESTRO meg-
1970:OLLA aukw- 2 OLLA PODRIDA pU-2 OMBRE dhghem-
```


## [2026-09-04T18:31:16.319Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=21 && NR<=25 {print \"@@@LEAF \"NR-1; print}' KLN_1966.txt | grep -n -i -A3 -B1 \"adam\" | head -60",
 "description": "Find Adam in KLN leaves 20-24"
}
```


### [2026-09-04T18:31:18.967Z] TOOL RESULT

```
100-actin-
101:adamant
102-20
103-certain  etymology.  It  denoted  perh.  orig.  a water  god  and  derives  fr.  axxf),  ‘promontory; beach  seashore’  (whence  also  axxcao;,  ‘on  the shore’),  which  is  of  uncertain  origin.  It  possibly derives  fr.  I.-E.  base  *ak-,  ‘sharp,  pointed’.  See acrid  and  cp.  prec.  word, actin-,  form  of  actino-  before  a  vowel, actinic,  adj.,  pertaining  to  actinism.  —  See  next word  and  -ic.
104-actinism,  n.,  property  of  ultraviolet  rays  of  caus¬ ing  chemical  change.  —  Formed  with  suff. -ism  fr.  Gk.  axxf;,  gen.  axxivo;,  ‘ray,  ra¬ diance’.  See  actino-.
--
142-adalid,  n. ,  leader,  guide.  — Sp.,  fr .  Arab.  ad-dalfl\it. ‘the  leader’,  fr.  ad-,  assimilated  form  of  al-,  ‘the’, and  daltl,  ‘leader’,  fr.  ddlla,  ‘he  showed  the  way, he  lead’.
143:Adam,  n., name  of  the  first  man  (Bible);  in  a  figur¬ ative  sense  it  is  used  to  denote  'human  nature, frailty’.  —  Heb.  Addm,  lit.  ‘man’,  usually  with the  def.  art.,  ha-addm,  ‘the  man’,  prop,  ‘the  one formed  from  addmdh  (i.e.  the  ground)’.  See  Gen. 2:7,  ‘The  Lord  God  formed  man  of  dust  from the  ground’.  For  the  connection  between  Heb. addmdh,  ‘ground,  earth’,  and  addm,  ‘man’,  cp. L.  homo,  ‘man’,  humdnus,  ‘human’,  which  are rel.  to  humus,  ‘earth,  ground,  soil ,  and  Gk. emx&ovioi,  ‘earthly  ones,  men’,  fr.  •/S+ow, ‘earth’. Derivatives:  Adam-ic,  Adam-ic-al,  adjs.,  Adam- ic-al-ly,  adv.,  Adam-ite,  n.,  Adam-it-ism,  n., Adam-it-ic,  Adam-it-ic-al,  adjs. adamant,  n.,  a  very  hard  stone;  adj.,  very  hard, unyielding.  —  ME.,  ‘diamond,  magnet’,  fr.  OF. adamant,  oblique  case,  fr.  L.  adamantem,  acc.  of adamds  (whence  the  OF.  nom.  adamas),  fr.  Gk. aSapa;,  ‘adamant,  the  hardest  metal,  diamond’, lit.  ‘unconquerable’,  fr.  d-  (see  priv.  pref.  a-)  and the  verb  8apav,  ‘to  tame’.  See  tame  and  cp.  dia¬ mond;  cp.  also  the  second  element  in  Hippodamia. The  sense  of  ‘load  stone,  magnet’,  arose  from  a confusion  with  L.  adamare,  ‘to  love  passionately’ .
144:adamantean
145-adept
146:adamantean,  adj.,  hard  as  adamant.  —  Formed with  suff.  -an  fr.  L.  adamanteus ,  fr.  adamds.  See prec.  word.
147:adamantine,  adj.,  1)  made  of  adamant;  2)  like adamant ;  very  hard.  —  L.  adamantinus,  fr.  Gk; aSaiiavnvot;,  fr.  ASApag.  See  adamant  and  adj. suff.  -ine.
148:adamite,  n.,  a  hydrous  zinc  arsenate  (mineral.)  — Named  after  the  mineralogist  M.  Adam.  For the  ending  see  subst.  suff.  -ite.
149:Adam’s  apple,  the  thyroid  cartilage.  —  A  name due  to  the  inexact  translation  of  Heb.  lappiiai 1 haaddm ,  lit.  ‘man’s  projection  (in  the  neck)’,  fr. tappOalf,  ‘anything  swollen  or  protruding; apple’,  from  the  base  of  tdphah,  ‘it  swelled’.  The rendering  of  this  Hebrew  term  by  ‘Adam’s apple’  is  due  to  two  popular  beliefs:  1)  that  the forbidden  fruit  eaten  by  Adam  was  an  apple; 2)  that  a  piece  of  this  apple  stuck  in  Adam’s throat.
150-adangle,  adj.,  dangling.  —  Coined  by  Robert Browning  (1812-89)  ft-  pref.  a-,  ‘on’,  and
151-dangle.
152-adapt,  tr.  v.  —  F.  adapter ,  fr.  L.  adaptare,  ‘to  fit, adjust,  adapt’,  fr.  ad-  and  aptare,  ‘to  fit’,  fr. aptus,  ‘fit’.  See  apt  and  cp.  adept.
```


## [2026-09-04T18:31:33.040Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=66 && NR<=70 {print \"@@@LEAF \"NR-1\" (printed p.\"NR-1-17\")\"; print}' FVQ_pages.txt | head -80",
 "description": "FVQ printed page 51 area"
}
```


### [2026-09-04T18:31:34.667Z] TOOL RESULT

```
@@@LEAF 65 (printed p.48)
48 FOREIGN VOCABULARY OP THE QUR J AN
more than " the adversary ", and particularly in the ecclesiastical
writers he becomes the chief of the hosts of evil. It is in this sense that
xli I appears in the Qur'an, so we are doubly justified in looking
for a Christian origin for the word.
One theory is that it came through the Syriac, the * being taken
as the genitive particle, 1 a phenomenon for which there are perhaps
other examples, e.g. mi^j for 8ia<f)covd? (ZA, xxiv, 51), ^uJ for
SiKaarri? (ZDMG, 1, 620)\ jUa? j for 8v<rVTpLa(tivyrr,ZweiGedichte,
i, 119 n.). The difficulty is that the normal translation of 6
is ] t rO^s), the accuser or calumniator, both in the Peshitta (cf. Matt, iv)
and in the ecclesiastical literature. There is a form *QDQ^jO, a trans-
literation of &a/3oAoy, but PSw, 874, quotes this only as a dictionary
word from BB. There is apparently no occurrence of the word in the
old Arabic literature, 2 so it was possibly a word introduced by
Muhammad himself. If we could assume that some such form as
.fnnV^>>% W as colloquially used among the Aramaic-speaking Christians
with whom Muhammad came in contact, the above explanation might
hold, though one would have to assume that the j had been dropped
by his informants. The alternative is that it came into Arabic directly
from the Greek, and was used by the Arabic-speaking Christians
associated with the Byzantine Church. 3
Grimme, ZA, xxvi, 164, suggested that it might have come from
8. Arabia, perhaps influenced by the Eth. -^-flA-ft. This, however,
is apparently a rare word in Eth., the usual translation for &a/3oAoy
being rt/8/TJ, though sometimes PV} is used (James iv, 7 ; 1 Pet. v,
8, etc.). Moreover, even if there were anything in Grimme's theory
that this was the form that crossed over into Arabia, his further
supposition that the ^jf was taken to bo the S. Arabian H --- (* w
very far fetched.
1 So Horovitz, A'6 T , 87. Mingana, Syriac Influence, 89, thinks rather that it
was the fault of some early scribe or copyist who mistook the initial Dal for an Alif.
2 The verses in Ibn Hisham, 318 and 516, noted by Horovitz, are from the period
of the Hijra and so doubtless influenced by Muhammad's usage. They would seem
fatal, however, to Mingana's theory.
3 Kiinstlinger, " Die Herkunft des Wortes Iblia im Kuran," in Rocznik Orjen-
tolistyczny, vi (1928), proposes the somewhat far-fetched theory that Iblis is derived
from the Jewish Belial by deliberate transformation.
@@@LEAF 66 (printed p.49)
FOREIGN VOCABULARY OF THE QUR^AN 49
Of common occurrence.
He ward, wages.
, *
Besides the noun and its plu. Jj^l there occur also the verbal
<" %
forms >- 1 and >.
The Muslim savants have no suspicion that the word is not pure
$
Arabic, though as a matter of fact the verb ^>-| to receive hire, is
obviously denominative.
Zimmern, Aklcad. Fremd.w, 47, 1 has pointed out that the ultimate
origin of the root in this sense is the Akk. agru, agarru, hired servant.
From this come on the one hand the Aram. NT3N : Syr. lr*Mj> a
hireling, and thence the denominative verbs 13K and ^J , to hire,
with corresponding nouns H3N and IrM, hire ; and on the other hand
(apparently from a popular pronunciation *<Mjgaru) the Gk. <zyyap09
a courier. 2
It would liave boon from the Aram, that the word passed into
Arabic, probably at a very early period, and as the word is of much
wider use in Syriac tluin in Jewish Aramaic, 3 we are probably right
in considering it as a borrowing from Syriac.
(Ahbdr).
v, 48, 68 ; ix, 31, 34.
Plu. of !_>-< ur '^ a Jewish Doctor of the Law.
The Commentators knew that it was a technical Jewish title and
quote as an example of its use Ka'b al-Ahbar, 4 the well-known convert
1 Cf. also Jensen in ZA, vii, 214, 215.
2 Even the latest edition of Liddell and Scott persists in repeating the statement
in Stephaiiua' Thesaurus, that it is a borrowing from Persian. It is, of course, possible
that the word may be found in the OPera. vocabulary, but if so it was a loan-word
there from the Akkadian, and there can be little doubt that the Gk. ayyapo? with
dyyape'ueii/ and dyyapeta came directly from the Akkadian, as indeed Ed. Meyer
(Geschichte de.s Altertkurns, iii, 67) had already recognized.
3 For its occurrence in Aramaic incantations, see Montgomery, Aramaic Incanta-
tion Texts from Nippur ', Glossary, p. 281 ; and for the Elephantine papyri see Cowley,
Aramaic Papyri, p. 178 (No. 69, 1. 12).
4 The plu. form jL-i is explained by a verse in Ibn Hi sham, 659, where we learn
of 0110 whoso full namo was Ka'b b. al-Ashraf Sayyid al-Afcbar.
@@@LEAF 67 (printed p.50)
```


## [2026-09-04T18:31:40.735Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==69 {print}' FVQ_pages.txt | head -50",
 "description": "FVQ printed p.51"
}
```


### [2026-09-04T18:31:42.475Z] TOOL RESULT

```
FOREIGN VOCABULARY OF THE QUR^AN 51
The origin of course is the Heb. DHK, and there is no reason why
the name should not have come directly from the Jews, 1 though there
was a tradition that the word came from Syriac. 2 The name occurs
in the Safaite inscriptions (Horovitz, KU, 85), and was known to
the poet 'Adi b. Zaid, so it was doubtless familiar, along with the
creation story, to Muhammad's contemporaries.
^, ol (tdritt)
Ls-Z *
xix, 57 ; xxi, 85.
Idrls,
He is one of the Prophets casually mentioned in the QurVtn,
where all the information we have about him is (i) that he was a man
of truth (xix, 57) ; (ii) that God raised him to a kt place on high '*
ULjp l>Lx^ aLi*3 j (xix, 58) ; and (iii) that being steadfast and
* " *
patient he entered God's mercy (xxi, 85).
The Muslim authorities are agreed that he is *7-j\>-\, i.e. ^130,
the Biblical Knoch, 3 a theory derived not only from the facts
enumerated above, but from the idea that his nanio <j*^ j^ I is derived
from <^J^ to study both Jewish and Christian legend attributing
to Enoch the mastery of occult wisdom. 4 The fallacy of this derivation
was, however, pointed out by some of the philologers, as Zam. on
xix, 57, shows, and that the name was of foreign origin was recognized
by al-Jawallqi, Mu'armb, 8 ; Qdtnus, i, 215 ; which makes it the more
strange that some Western scholars such as Sprenger, Lvben, ii, 33G, 5
and Eickmann, Awgdologie, 26, have considered it to be a pure Arabic
word.
1 Ibn Qutaiba, Ma'arif, 180 (Kg. cd.) notes a variant reading ^|Jb| which may
represent a Jewish pronunciation.
2 Sycz, Eigennamen, 18.
<l Tha'labI, Qisa*, 34.
4 "[3H of course means to instruct, to initiate (of. viL-) and may have suggested
the connection with ^jj. For the derivation see Tha'labI, loo. cit. ; Ibn Qutaiba,
Ma'arif, 8. Finkel, MW f xxii, 181, derives it from i5So>peaxo?, the 7th antediluvian
King of Berossus, but this is very far-fetched.
5 Ho seems to base this on the occurrence of the name Abu Idris, but see Horovitz,
KU 9 88.
```


## [2026-09-04T18:31:46.430Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==68 {print}' FVQ_pages.txt | tail -30",
 "description": "FVQ p.50 tail"
}
```


### [2026-09-04T18:31:48.881Z] TOOL RESULT

```
used in the Rabbinic writings as a title of honour, e.g. Mish. Sanh. 60 ^
D'HSn V33 *")&< 13n ]'~\7m nQ,"asAaronwasaDoct6rsowere
his sons Doctors." 1 Geiger's theory has been accepted by von Kremer,
Ideen, 226 n., and Fraenkel, Vocab, 23, and is doubtless correct, though
Griinbaum, ZDMG, xxxix, 582, thinks that in coming into Arabic
it was not uninfluenced by the Ar. j\>-, jfr>\ J^>- Mingana,
Syriac Influence, 87, suggests that the word is of Syriac origin (see also
Cheikho, Nasrdniya, 191), but this is unlikely. The word was evidently
quite well known in pre-Islamic Arabia, 2 and thus known to Muhammad
from his contact with Jewish communities. It was borrowed in the
form of the singular and given can Arabic plural.
*3I (Adam)
ii, 29-35 ; iii, 30, 52 ; v, 30 ; vii, 10, 18, 25-33, 171 ; xvii, 63, 72 ;
xviii, 48 ; xix, 59 ; xx, 114-119 ; xxxvi, 60.
Adam.
It is used always as an individual name and never as the Heb.
f-~
and Phon. DIN for man in general, though the use of O I ^i in
Sura, vii, approaches this usage (Noldeke-Schwally, i, 242). It is one of
the few Biblical names which the early philologers such as al-Jawaliqi
(Mua'rrab, 8) claimed as of Arabic origin. There are various theories
as to the derivation of the name, which may be seen in Raghib,
Mufraddt, 12, and in the Commentaries, but all of them are quite
hopeless. Some authorities recognized this and Zam. and Baid., on
ii, 29, admit that it is a foreign word
1 Hirschfeld, Reitrage, 51, translates by " Schriffcgelehrte " (cf. the N.T.
Syr. I******), and takes it as opposed to the ^"IXH D37.
2 It occurs in the old poetry, cf. Horovitz, KU, 63, and Ibn Hiaham, 351, 354, uses
the word familiarly as well known ; cf. also Wenstnck, Jodfn tc 71/r/rfina, 65 ; Horovitz,
JPA T , 197, 198.
```


## [2026-09-04T18:31:56.395Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==13 {print}' POK_01.txt | head -70",
 "description": "Pokorny page 4"
}
```


### [2026-09-04T18:31:57.894Z] TOOL RESULT

```
,  Fracht',  Hes.  djyava  ,Speichen', (XTQccT-riyög  (s.  u.).  Über  dor.  dyov  (ai.  äjam)  ,ich  trieb'  s.  jedoch  Schwyzer Gr.  Gr.  I  654,  4.
0-St. :  ved.  ajd-li  ^Treiben;  Zug;  Treiber^,  gT.  äyog  ^Führer^  Heerführer',
atoav-Qyöc,    att.-ion.   oxQaxiqyög   ;,Heerführer^;  Xo^äyög  (ursprüngl.    dorisch)
xA-iiführer    eines   loxog',    lat.  pröd-igus   _,verschwendend^    (von   pröd-igere),
ahiga  ,chamaepit7S^  (^propter  abortus^  voq  ah-igere  =  äftäyo),  ai.  apa-djati
;abigitO.
iO-St.:  ir.  aige  ^Wettlauf'^  ai.  in  prtanäjyam  ^WettkampF.
agmn,  agmos:  ai.  djman-  n.  ,Bahn,  Zug*^;  djma-h  ds.  (aber  über  jman, parl-jman-,  pftliu-jman- ,  jma-yä-  s.  ghpem-  ^Erde^):  lat.  agmen  ;Zug_,  dahin- ziehende Schar^  (Neubildg.  nach  agö  für  *ammen),  exämen  ^ausziehender Bienenschwarm,,  Schwärm^;  , Zünglein  an  der  Waage*",  dann  ^Prüfung^  (aus *agsmen),  ammentum  (^ agmen- to-m)  ,der  in  Schlingenform  etwa  in  der Mitte  des  Wurfspießes  befestigte  Wurfriemen';  vielleicht  (Schw.  Gr.  Gr.  I 492^*^)  mit  o-Abtönung  gr.  ^yaog  , Ackerfurche,  Bahn  von  Himmelskörpern; Schwade  beim  Mähend
io-St. :  ai.  ajird-  , rasch,  behende^  (aber  lat.  agilis  , beweglich,  behende^ ist  junge  Neubildung);  gr.  äyeXTj  ,Herde, ,  Schar^,    lat.  agolum,   Hirtenstab'.
Gr.  äyö)v  ,Wettlauf,  Wettkampf^;  ^yvia  ,Straße^  (Part.  Perf.),  woraus über  jüngeres  ^äyeia  lat.  agea^  lak.  kret.  ätol.  dyvsio  ,£ühre,  bringe^,  ep. ion.  äyivsixevai,  hyiveo)  ds.  (:  dyvso)  und  ^'/a>,  wie  öql-vcü  gegenüber  l)Q-vv-fiL und  (bg-öfXTjy,  also  von  einer  auf-  i  endigenden  Wurzelform;  vgl.  Schwyzer Gr.  Gr.  I  694,  696).  Über  'fiysf.iiov  s.  Schwyzer  Gr.  Gr.  I  522'^  und  unter  säg-.
Lat.  remex,  remigäre,  remigium,  lltigäre  ,lite  agei'e'  und  andere  Verba auf  -{i)gäre.  —  Vermutlich  lat.  indigites  ,die  einheimischen  Gottheiten  und Heroen'  (indigitäre  ,eine  Gottheit  anrufen',  indigitämenta  , Anrufungs- formeln'), als  ^end(p)-aget-  ,die  Einheimischen'.
Bedeutungsentwicklung  zu  ,wägen'  (aus  ,in  Schwingung  bringen')  in  lat. exagium  , Wägen,  Gewicht',  exigere  u.  a.  , abwägen,  abmessen',  exäctus ,genau  zugewogen',  exiguus  ,knapp  (zugewogen)',  exllis  (*ex-ag-slis)  , dürftig', exämen  (s.  o.),  aglna  ,die  Schere  an  der  Waage'  (Bildung  wie  z.  B.  coqmna), gr.  äyeiv  auch  ,wiegen'  (mit  Akk.  des  Gewichts),  ^^log  (aus  *ä'Ä,Tiog,  auf Grund  eines  *ag-ü-s  , Gewicht',  eigentlich:)  , von  entsprechendem  Gewicht', daher  ,wert,  würdig',  dwa^tog  , gleich  wertig'.
Vgl.  noch  WH.  I  9,  10,  24  über  acnua,  actus  quadrätus  ,ein  Feldmaß von  120  Fuß  im  Geviert',  und  actütum  ,sogleich',  agäsö  ,Pferdeknecht',  agö, -önis  ,der  das  Opfertier  tötende  Priester'  (von  agei-e  in  d
```


## [2026-09-04T18:32:04.448Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==12 {print}' POK_01.txt | tail -30; echo \"=== leaf14 (p.5) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==14 {print}' POK_01.txt | head -40",
 "description": "Pokorny p.3 tail and p.5"
}
```


### [2026-09-04T18:32:06.178Z] TOOL RESULT

```
n  Toch.  64^).    Über  gv.  ä^rjQ  s.  unter  andh-.
WP.  I  45,  Feist  61a,  anders  WH.  I   14.
ad(u)-,  ad-TO-   ,Wasserlau£'.
Avest.  aöu  , Wasserlauf,  Bach,  Kanal',  ven.-ill.  FIN  Ad(cl)ua  (zum  Po), *Adulia':>Attel  (zur  Donau  in  Bayern),  Mons  Adulas  ,St.  Gottbard^  (wohl nach  den  dort  entspringenden  Flüssen  benannt),  der  oberösterr.  FIN  *Adra -^Attersee,  Attergau,  FIN  Adrana>  Eder  (Hessen),  vielleicht  auch  der ON  Adria  in  Venetien  (danach  das  mare  Adriaticum),  der  sizil.  FIN  ^Adgavög und  der  ven.-ill.  Name  der  Oder  OvL-adovag]  ferner  der  lett.  FIN  Adula. Vasmer  ZslPh.  8,  114  f.,  Pokorny  Urill.  4,  70,  93,  109,  124.
ag-  jtreiben'  (eigentlich  wohl  ,mit  geschwungenen  Armen  treiben'),  , schwingen', in  Bewegung  setzen,  führend  Ursprünglich  auf  den  Präsensstamm  be- schränkt.
agö:  ai.  djati  ,treibt',  av.  azaiti  ^treibt,  führt  weg*,  arm.  acem  , führe, bringe^;  gr.  Uyuj  ,führe^  (Aor.  }}yayov,  ^^^a  [sind  jung),  lat.  agö  ^treibe^  führe, verhandle^  (Pf.  egl  mit  Ablautneuerung),  osk.  Imper.  actud  =  umbr.  aitu ,agito',  osk.  acum  ^agere^,  air.  ad-aig  {*aget)  ,adigit',  acymr.  agit,  hegit, jünger  eyt  {*agiti),  daneben  die  starke  Flexion  in  cymr.  corn.  bret.  a  (*aget) ,geht^;  ^Prät.  air.  ro-da-acht  ,trleb  sie  forf^,  cymr.  aeth  (*ag-t)  ,iit^  usw., s.  Pedersen  KG.  II  451  ff.,  air.  äin  ^Treiben,  Spiel^  (aus  *agms),  gallo-rom. *and-agnis  ,großer  Schritt^,  frz.  andain  , Schwade,  Sensenhieb',  afrz.  ,Weit- schritt^,  anord.  aka  , fahren*"  (Prät.  ök  wie  ai.  Gramm,  äja)]  ags.  ac  ,aber, sondern'  (wörtl.  ,geh!^  wie  lat.  age)]   toch.  B  ak-,  AB  äk-  , reisen,  führend
fo-Partiz.:  ä/,T6g,  lat.  actus,  kelt.  *amb{i)-aktos  eigentlich  , herumge- sandter (:  air.  imm-aig)  Bote,  Diener'  in  gall.  (-lat.)  amhactus  , Dienstmann, Höriger^,  cymr.  amaeth  ,servus  arans'  (aus  dem  Kelt.  stammt  got.  andhalits, ahd.  ambaht  , Diener^,  woraus  die  Sippe  von  nhd.  Amt).
Als  idg.  Instrumentalnomen  auf  -trä  hierher  ai.  asträ  ,Stachel  zum Viehantreiben^,  av.  asträ  ,Peitsche,  Geißel'.
Dehnstufenbildungen:  ai.  äji-h  m.  f.  ,Wettlauf,  Kampf,  mir:  äg  (Gen. äga,  w-St.)  ,Kampf^,  äga,  aige  ,Führer'  (vgl.  auch  gall.  PN  Ago-märus =  air.  dgmar  , kriegerisch'';  Com-ägius),  lat.  nur  in  Kompositis:  amhägeSj -um  ,Umgang,  Umlauf;  Irrgang;  Winkelzüge'  (kons.  St.  wie  ai.  dj-E  ,zu treiben'  =  lat.  agi  Inf.  Pass.,  und  wie  ai.  aj-  in  prtanäj-  ,in  den  Kampf ziehend',  jedoch  mit  Dehnung  in  der  Komposition),  indäges  und  indägo, -inis  ,das  Aufspüren  (und  ins  Garn  Treiben)  des  Wildes',  co-ägulum  .ge- ronnene Milch',  ai.  samäja-h  ,Versammlung,  Gesellschaft',  gr.  dywyög  , füh- rend, leitend',  dycayi^  ,Führung,  Leitung
=== leaf14 (p.5) ===
er  Bed.  ,opfern'), agönium  , Opferfest'  u.  dgl.
Hierher  vielleicht  gall.  exacum  ,centaurion  lepton'  falls  für  *exagum (=  "^exago-  ,purgierend')  verschrieben.  Aber  besser  zu  ^ak-  , scharf,  spitz', s.  dort.
6
Ferner  gehören  hierher:
ages-,   aks  .  .  .  /Drehpunkt:)  Aclise  —  Achsel^:
Ai.  dksa-h  .Achsel  gr.  lIEo)v  ds.,  6f>-«?«  ,Wagen^  (Gl.  12,217;  KZ.  4C; 217 f.);  lat.  axis  ^Achse^  =  lit.  asu,  apr.  assls^  aksl.  os^  f.  ds.;  ahd.  ahsa^ nhd.  Achse,  ags.  e«x  ds.;  an.  qxull  (aus  urg.  *alisulaz)  ,Achse^;  mir.  ais .Achse'  {*aksi-lä  in  cjmr.  echel  f.  .Achse^  hret.  aliel).
Lat.  äZct  .Achsel^  woraus  die  üblichere  Bedeutung  .Flügel';  aus  *agsla (vgl.  Demin.  axilln  .Achselhöhle')  ==  an.  qxl,  ags.  eaxl,  ahd.  ahsala,  nhd. Achsel,  woneben  dehnstufig  nil.  oksel  ds..  und  ohne  Z-Formantien:  ahd. uochisa,  mhd.  uohse,  iiehse  und  ahd.  uochsana,  ags.  öaJ7i  .Achselhöhle',  an. öst  f..  ös^r  m.  .Halsgrube',  ags.  öcusta,  öxta  m..  engl,  oxter  .Achselhöhle'; av.  asaya  Gen.  Du.  .der  beiden  Achseln',  arm.  anut''  .Achselgrube'  (zu- nächst aus   *asnut^).
ag-rä  .Hetze.  Jagd',  ag-ro-s  .treibend,  hetzend':
ai.  in  ghase-ajra-  .zum  Verzehren  antreibend.  Eßlust  erregend',  av. (yehr-kam)  azrö-daiölm  .die  Jagd  machende,  auf  Beute  ausgehende  (Wölfin)': gr.  äyga,  ion.  Hygr]  .Jagd.  Fang',  nävayqoo,  .alles  fangend,  fassend',  x^sa/^a .Fleischzange'.  rcvQdyoa  .Feuerzange'.  TtoSdyga  .Fußfalle'.  MeXiocygog  ur- sprüngl.  Bezeichnung  eines  .Dämons,  der  als  hitziges  Fieber  die  Glieder ergreift' ('?).  äygsvg  .Jäger',  dygsvu)  .erjage,  fange';  aber  dygew  .nehme' nach  Schwyzer  Gr.  Gr.  I  727^  aus  "^ä-ygo-]  ir.  är  n.  .Niederlage'  {*agron), cjmr.  aer  .Schlacht.  Kampf  {*agra),  eigentlich  .Hetze',  acorn.  hair  .clades'. abret.  airou  Fl.  .strages'.  gall.  VN  Veragri  .die  ge wältigen  Kämpfer'.
ag-rO'S  .Feld,  Flur'  (zu  *-agö  wie  Triften  treiben,  also  ursprünglich  .Ort. wo  das  Vieh  hinausgetrieben  wird.  Weide').
Ai.  djra-h  .Fläche.  Flur.  Gefilde'  (ohne  Beziehung  auf  Ackerbau).  g\\ dygög  .Feld.  Land'  (im  Gegensatz  zur  Stadt),  lat.  umbr.  ager  .Feld',  got. (usw.)  akrs,  ahd.  ackar,  ahhar,  nhd.  Acker  (Acker  und  ags.  cecer  auch ein  bestimmtes  Landmaß.  .soviel  ein  Gespann  Ochsen  an  einem  Tage pflügen  kann'),  arm.  art  .Acker'  (mit  rätselhaftem  t  über  *atgr-,  *atr-, s.  Pedersen  KZ.  39.  352;  davon  artak's  .hinaus'.  Präfix  arta-  .aus').
Ai.  ajriya-  .in  der  Ebene  befindlich'  =  gr.  äygiog  .auf  dem  Felde,  im Freien  wachsend  oder  lebend,  wild';  dygövsgog  .wild  lebend',  lat.  agrestis .lä
```


## [2026-09-04T18:32:33.072Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN tarazu ===\"; grep -n -i \"tarâzû\\|tarazu\\|tarāzū\\|taraz\" HRN.txt | head -20; echo \"=== HUB ===\"; grep -n -i \"tarazu\\|tarāzū\\|taraz\" HUB.txt | head -20",
 "description": "Grep tarazu in Horn/Hübschmann"
}
```


### [2026-09-04T18:32:33.141Z] TOOL RESULT

```
=== HRN tarazu ===
=== HUB ===
```


## [2026-09-04T18:32:33.590Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==209' incoming/PLA/PLA_pages.txt | head -60",
 "description": "PLA printed p.194"
}
```


### [2026-09-04T18:32:35.352Z] TOOL RESULT

```
tabaristän                                                                     194                                                       tirazdärän


ol.              -       tabaristän? : Landschaft                             in    Nordpersien           ı    mand.           tabaristan         ®,


Sh-            tabari:               "aus     Tiberias             od.    Tabaristan"             °.,


on        -    tabas:            eine        Stadt       in    Khorasan -


Ol             - tabasän:                   Dual    v.     tabas,         zwei          Städte     in    Khorasan             4,

     a                     7.                                                                    Fo              r   5
a         - taba$i:                  "eine        Heilpflanze" <                    Pers. a             tabafi           ”.


o-         tabag:     "Holzplatte",                           nach       Dehhodä          eine     arabisierte                Form       v.   pers.2,0
              =.  6
          tabük     .


apmb- tabanga:                          "Pistole"             = tabänfa q. v.

ENG            aßgan:           "in der Pfanne                 braten"             s.    tägin 7,

(rel - oo
       taräbis:                             Pl.    v. or» 5 tarbüs                  q. v.

Gelb - taräbiS:                             Pl. v. ab tarbüf                       q. v.

Jelb - tar&bil:                             Pl.    v..Jı) garbäl                   q. v.

ab             - taräbina:                   Pl. v.ubb tarhän q. v. 8,

lb.            tiraz:            "Stickerei,               Rand,         Saum!             pers.        ;|x taräz             m.              Dr taraz.

               .t                    =                                                                                               “         2 ee.
Olls;Lb - tiräzdäran:                                 "Futteral               der Waage" pers.                       olbyals              tarazudäran
              mp.           gi        r tarazük            "Balance,               Gleichgewicht"                    air.          *taraä=      skr.
          tula           + aw.        az "zugeben"                 tk.             terazi,       serb.,       kl.        russ,       terezy.



1.       LD.        s.    v.
2.       Macuch           Ss.    v.
3.       Wahrmund               s.    v.,     LD.     S.      v.
4.       al-Mu°arrab                  Ss.    V.
5.       LD.        s.    v.
6.       ebda.
7. Wahrmund
      s. v., Muhit s. v.
8.       LD.        s.    v.
9.       Wahrmund               s.    v..     Addai        Scher         s.    v.
```


## [2026-09-04T18:32:46.847Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ترازو\" BQT_v1_pages.txt | head -20",
 "description": "Grep tarazu in BQT v1"
}
```


### [2026-09-04T18:32:46.897Z] TOOL RESULT

```
12017:و رای فرشت » بیونانی‌ترازورا گوبند ۴ وسربی
12048:ترازوی آفتاب است چه امطی بمعنی ترازو ولاب
12835:بونالی است بمعنی نرازوی آفتاب چه اصطرترازو
23100:باشد که در يك که ترازو نهند نا با کفهٌ دمگر
23568:ترازو هم آ هده است .
26312:و کفة ترازو را هم گفته‌اند - و بکسر اول و فتح
26326:ثانی مشدد بر وزن چله. کفهٌ ترازو را گوند -
27158:پیاهو - با های هوز بر وزن ترازو .
28235:و کیان ترازو ماشدی است که بدان بار سنجند »
29232:هت که از ترازو آخر تراش اس تکه تراشیده شده و[ نجه‌ازتراش
29240:۳ ترازو بانشانه نجوه‌ی
29241:ترازو چشمه‌داشتن ۰ کنابه از
32164:و ثیر عساری و چوب ی که هردو پلةً ترازو از آن
```


## [2026-09-04T18:32:49.272Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=30 && NR<=31 {print \"@@@LEAF \"NR-1; print}' KLN_1966.txt | grep -n -i -B2 -A4 \"^act,\\|act, \\|agent\\|I.-E.  base  \\*ag-\\|base \\*ag\" | head -50",
 "description": "Klein leaf ~29-30"
}
```


### [2026-09-04T18:32:51.023Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:32:54.540Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# find leaf containing line 29232 content\nimport re\nfor i,p in enumerate(pages):\n    if 'ترازو چشمه' in p or 'تراش اس' in p:\n        print('LEAF',i)\n        print(p[:3000])\n        break\nEOF",
 "description": "Find BQT tarazu page"
}
```


### [2026-09-04T18:32:56.381Z] TOOL RESULT

```
LEAF 112
مقدمه صد وچبار
و« دری ؛ لت پارسی باستانی > و« زند (جان) بزبان فرس قدیم > یاد
شكده است.. :
است» وپیداست که فرمس مصحف < قومس > معرب < کومش» پهلوی ۱
است -
ح - پهلوی ۴ - برهان بخشی ازلغات پپلویرابنام « زند وبازند»
آورده است ۰۴ و بغشیر1 بنام « پپلوی > یاد کرده است مانند : تبراست
بیعنی سیصد » و بخش اعظم لفات مأخوذ از پپلوی را - که بیشتر نها
دینی است - بدون تعبین اينکه از چه زبان است » نقل کرده و شرح داده
است ؛ مانند : اردش ؛ |بخشت (ابعشست)» بر سم» تنافور (تنا پوهر )» وچر »
وچر گر وجز آن.
و نیز لفات ذیل رابنام«پپلوی» یاد کرده است: پرویز بمعنی ماهی ۰۴
دوخ چکاد یمعنی اصلم ( ذیل : چکاد )» زردشت بزرک ؛ زروان بزرگ ؛
زرهون ٩‏ ۰ شنگ بیز بمعنی زنجبیل » کیر بمعنی خفتان جنگ » ماه بمعنی
شهر و مملکت » هامرز بمعنی برخیز *هانی بمعنی بنشین * هر بمعنی کننده
و فاعل » هوش بىعنی مرگ » هیز بمعنی دلو گرمابه بان ۱ .
ذیل « تارخ > کوید : « بزبان پپلوی » نامآزربت تراش است . »
درصورتیکه « تارح > عبری است بمعنی تنپل و نام پدر ابراهیم است ۷ .
«- حاعتحوف۴, رك؛ اوتممذ0:0۷ 6 ]۵ منوهماهایت ۸ ,۲2۱۷۵2۵ . [
تا 55 , 12 ۰ و 1931 فحهم . عطقطاعمة:۴ اه وامانوین
۲ - در ذیل «پهلوی» کوید : « زبان شپری باشد وهثسوب بپپلوان وزبان فارسی هم
هست . » رك: ی هفت‌همن‌هقدمه. ۳- رك: ص‌دوازده هسن حقدمه. 4 اپروج
[32027۷6 درپپلوی بمعنی پیروز کر است . رك : اپرویز و پرویز . ۵ - مولف هر سه
کلمه اخیررا پپلوی ونام ابراهيم پیغمبر دانشه است درصورتبکه پپلوی زردشت " 272۲0806
است. ۶ نیب رک ۲۵4» وزرتشت پیامبر ابرانی‌را با ابراهیم پیامبرکلدانی خلط کرده‌اند « مزدینا
۹۸-۹۹,۹۲-۳ > وزروان در پهلوی 2.1۳۷3۳ بالا26۳۷2 بمعنی زمان و در اوستا در ردیف
دیگر ايزدان آمده وبعدها در آبین زروانی پروردگار بزرکه موجد مزدا و اهریمن شمرده شده
اس رگ
,44 ۰2۵0۵۵۵02206 معل259221٩‏ وع1۱ ونا۵؟ ۲۲۵۵ نا ۸.06
0 . 149 00 :
خرده اوستا . بور داود ص۹-۹۳. > - ره : هربك از لغات مذ کور درمتن
برهان و حواشی آن . ۷ - فاموی کتاب مقدس : تارح . ۰
( برهان اطع . سیز دهم )
```


## [2026-09-04T18:33:04.168Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(700,716):\n    p=pages[i]\n    if 'ترازو' in p or 'تراز' in p:\n        print('=== LEAF',i,'===')\n        print(p[:1800])\nEOF",
 "description": "BQT v1 leaves 700-715"
}
```


### [2026-09-04T18:33:06.036Z] TOOL RESULT

```
=== LEAF 705 ===
پاخته بائد پس کیرد - و کنابه از مردم ملوث
ومردار و فاسق حم هست۷ .
فا بفتح اول بر وزن سرا ؛ دبوار
ودیوارفلعه وکاروان سرا - وسدی و دیواربرا لیز
کفته‌اند که دریش جزی یکفند؟ و دیواری
که باکاهگل و کلابه استوار کرده باشند - وبنم
اول تو کیبی باشد از لفظ « تو» و « را > که در
معحاورات و کتابت واو را می اندازند - و بمعنی
خود را هم هت .
تراب بفتح اول بروزن شراب» ترشح
وراوبدن و کم کم چکیدن آب و شراب وروغن
وامثالآن باشد از کوزه و سبو و معك و مانئد
آن؟ - و بمحنی حیله و زبان آوری هم بنظر
آمده است.و بضم اول بزبان عربی‌خاكشرا گویند.
ترا یل بروزن و ممنی تراود است که
تراز
میکند ومی‌ترآوده چچه در فارسی‌با بواو وبرعکس
تبدیل مي‌بابند؟ .
تر الیدن « بر وزن و حعنی تراوبدن
وترشح کردن باشد مطلفا اعما زب وشراب‌ودوغن
وامثالآن از ظرونه .
اشتهار دارد. و ترندنکش نیز گوند , و بعربی
جرجیر خوانند .
قر اج - منم اول بر وزن وعمنی دراج
است» وآن پرنده‌ای باشد صحرایب یکهآنرا شکار
8[ وخورند؟ ۰
قراار ‏ بر وزن نماز » رشتة ریسمان
خام را کوبند - و نام درخت صنویر هم هست
و نام شهری است در تر کستان که منسوب است
۴ - صف دشمن ترا ناستد بیش
بخل همه چنان تراید ازآن روی
۹ رك : دراج .
حدودالمالم . فهرست؟.
بقبه از صفْحٌ 1۷۸
ور همه آهنین ترا باشد. شهید بلخی.
«لت فرس ۱4*.
۵ رك : ثراو ندن:
کآب‌چنان ازسفال نوبترابد(ثرابد. دهخدا).
خروانی. «لفت فری۲۲*.
پونانی 166۵0 .استی 48118 (یسر بجه) . فارسی : ثر ء تازه . پپلوی ۰12۲۲ *صسیشال ۱8:»»
ازهمین ربثه است ترانهةٌ فارسی ( جوان خوش روی و دویرتی و سرود ) و تولة نارسی (بمسك)
وتوره (شغال) دیتتا اص ۱۷۱ ب ٩۷۲‏ , گوراای ۲ ( خبی » 9 گورالی ۷۵ ۰ , فر یز ندی
وبرنی ونطنزری 4۲ « دك . ٩ص‏ ۳ ,: سمنانی و سنگری و لاسکردی و شهمیرزادی ۹:۹9
سرخة #۲) «ثك. ۲س ۰۱۹۳ دزفولی هم 8۲ (خیس ؛ مرطوب). ر که: ترانه. نوره , توله.
=== LEAF 706 ===
ی
تر اژوی دد - کنابه از آقاب
تراش - بقتح اول بروزن نواش " طمع
و نوقع وتراشده شده را گویند؟ -
تر ارو!۱ ه معروف است ؛ ون آلتي
باشد که‌چیز هارا
ندان وزن
برج حیز آن‌هم گراشه" هت تج ایل ورابع : یمی
هت که از ترازو آخر تراش اس تکه تراشیده شده و[ نجه‌ازتراش
۱ جبلة دوازده برح | برآمده باشد. وهلال واری ازخریزه وهندوانعزا
. فلکی است۳ ویر | نیز کوشده *
و عدالت رانیز گویند قر ۷2 بفت‌اول‌بروزن هلاه بسنی
ساب و ی عراز ور | چا وشکاف باشد- وآوازیراگوبندکه ازشکتن
با شکافته شدن چیزی بگوش رسد - و صدای
رعد را نز گفته اند ؛ وطراق ععرب‌آنت ۰
۰ ۳۹ است ۰
۳ ترازو بانشانه نجوه‌ی
ترازو چشمه‌داشتن ۰ کنابه از
زبادتی وسنگینی بك یل نرازوست ازیلهُ دیگر.
تر ارزو شدن « کنابه از برابرشدن
دو عنیم باشد با هم درشجاعت وزور .
ترادوی پو لاد سنحان - کنبه
از نیزه وسنان مبارزان است .
تر ا نه۲ بر وزن بهانه . جوان‌خوش
صورت وشاهدنر ونازه وصاحب جمال را گویند-
و باسطلاح اهل نقمه صنیفی است که آن سد
کوشه داشته «اشد هر کدام سارزی : ۹ نی
ود: گری كٍِ_۳ ویکی دیگر تلا وتارلا - ودرلفت
نقش‌وصوت ودوییتی وسرود ونفمه‌را خوانند۵ -
۱ - پهلوی 12۳220 , ابرانی باستان 12۲2201 ۵ - 2270 - ۵۲2 ۰ : 2۳2) ۵
از سانسکریت 24آلا) , ۷۷2) و22 ۰ از۰22 سانسکریت: 4 (راهنمابی کردن » راندن» پیش-
بردن.) » «نببکک ۰۲۲۳ . رگ : مزنا . ۴ _- خوارژمی : ترلزك سح موی : حیزان .
برح‌هفتم از بروح دوازده گاند « گاه شماری ص ۰۷۰۳ . ۴ اوستا تافقنا * ( نراشدن
بربدن) «بارنولمه 486 . رك : نراشیدن . کب اوه رای :هن (قتتت):
سر گنلک 3-2 ۱ - اسم صوت است . اصدی‌آرد: ترااء, طراق
بود. خسروی گوید :
«لفت فرسی ۲۹۵ .
۷ - از رمثة اوستایی ۸۷۲1108] بمعنی خرد» نر و تازه (رك : تر» توره * توله) «فاب
۱ ص ۷ سسنا۱ صس ۱۷۱ ؟. ۸ دوهی (حوان خوشروی» دو ستی و صشف)؛
هر نسفته دری دری می‌سفت هرترانه ترانه‌ای میگفت فرخی سیستانی.
۵ تراشیدن - بفتح اول و ششم » ار : ترانی - بدن (مصدری ) . پهلوی 2511102)
«سشدهش ۱۷۳ ,(. بر گت ۶ , مفدی 251 ( بر ددن ( «گونیو ۳۵ ۰ ۰ گورانی 2-10(
+ کردی ۰۰۱۹۷ گیلکی 02-1۵250128 , ط
```


## [2026-09-04T18:33:18.430Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(26,34):\n    p=pages[i]\n    if 'agent' in p.lower() or 'I.-E.  base  *ag' in p:\n        print('=== LEAF',i,'===')\n        import re\n        for m in re.finditer(r'ag(ent|enda|ere|-)', p):\n            pass\n        print(p[:200])\n        # print snippets around 'agent'\n        for kw in ['act,  n','agent,','agenda','agriculture','agony','ambassador','axle','strategy']:\n            j=p.find(kw)\n            if j>=0: print('---',kw,'---'); print(p[j:j+700])\nEOF",
 "description": "Klein act/agent entries"
}
```


### [2026-09-04T18:33:20.330Z] TOOL RESULT

```
=== LEAF 26 ===
dnem,  acc.  of admonitio,  fr.  admonite,  pp.  of  admonere.  See admonish  and  -ion.
Derivatives:  admonition-er,  n. admonitor,  n.  —  L„  fr.  admonitus,  pp.  of  admo¬ nere.  See  admonish  a
=== LEAF 31 ===
 element  is  of  uncertain  origin.  It  possibly derives  fr.  I.-E.  *mga-  and  is  rel.  to  Gk.  usyx;, ‘great,  large’;  see  mega-.  The  second  element  is cogn.  with  ON.  stinga,  OE.  st
--- agent, ---
agent,  adj.,  and  cp.  words  there  referred  to. agency,  n.  —  Late  L.  agenda  (whence  also  F. agence),  fr.  L.  agens,  gen.  agentis,  pres,  part  of agere.  See  agent,  adj.  and  n.,  and  -cy. agenda,  n.  —  L.,  ‘things  to  be  done’,  neut.  pi.
37
of  agendus,  the  gerundive  of  agere.  See  agent. For  the  use  of  other  Latin  gerundives  or  their derivatives  in  English  cp.  addendum,  Amanda, Amartdus,  avisandum,  corrigendum,  credenda, deodand,  dividend,  girandole,  habendum,  hacien¬ da,  horrendous,  launder,  legend,  memorandum, minuend,  Miranda,  multiplicand,  ordinand,  pre¬ bend,  propaganda,  pudendum,  radicand,  redden¬ dum,  referendum,  re
--- agenda ---
agenda  (whence  also  F. agence),  fr.  L.  agens,  gen.  agentis,  pres,  part  of agere.  See  agent,  adj.  and  n.,  and  -cy. agenda,  n.  —  L.,  ‘things  to  be  done’,  neut.  pi.
37
of  agendus,  the  gerundive  of  agere.  See  agent. For  the  use  of  other  Latin  gerundives  or  their derivatives  in  English  cp.  addendum,  Amanda, Amartdus,  avisandum,  corrigendum,  credenda, deodand,  dividend,  girandole,  habendum,  hacien¬ da,  horrendous,  launder,  legend,  memorandum, minuend,  Miranda,  multiplicand,  ordinand,  pre¬ bend,  propaganda,  pudendum,  radicand,  redden¬ dum,  referendum,  repetend,  reprimand,  reverend, subtrahend,  tremendous.
agent,  adj.  —  L.  ag
--- agriculture ---
agriculture,  agrio-, agro-,  agronomy,  Agrostis,  Agyieus,  aisle,  ala, ambages,  ambagious,  ambassador,  ambiguous, ament,  anagogy,  antagonist,  apagoge,  assay, Auriga,  axilla,  axiom,  axis,  axle,  cache,  chora- gus,  clarigation,  coact,  coagulate,  cogent,  cogi¬ tate,  demagogic,  deuteragonist,  embassy,  epact, essay,  exact,  examen,  exigent,  exiguous,  exility, indagate,  intransigent,  isagoge,  paragoge,  para- gonite,  pedagogue,  pilgrim,  prodigal,  protago¬ nist,  react,  redact,  remex,  stavesacre,  strategy, synagogue,  transact,  tritagonist,  and  the  second element  in  castigate,  clarigation,  fastigiate,  fu¬ migate,  fustigate,  levigate,  litigate,  mi
--- agony ---
agony’,  Aycoyd?,  ‘leader’,  aywyfj, ‘a  carrying  away,  a  leading’,  OI.  ajati,  ‘drives’, ajirah,  ‘moving,  active’,  Avestic  aza'ti,  ‘drives’, Toch.  A  dk-,  B  &k-,  ‘to  travel,  lead’,  Arm.  acem, ‘1  lead,  bring",  ON.  aka,  ‘to  drive’.  Cp.  agent, n.  Cp.  also  abigeat,  acorn,  acre,  act,  action,  acti¬ vate,  actor,  actress,  actuate,  Agelaius,  agenda, agile,  agitate,  agminate,  -agogue,  agonist,  ago¬ nize,  agony,  agrarian,  agrestic,  agriculture,  agrio-, agro-,  agronomy,  Agrostis,  Agyieus,  aisle,  ala, ambages,  ambagious,  ambassador,  ambiguous, ament,  anagogy,  antagonist,  apagoge,  assay, Auriga,  axilla,  axiom,  axis,  axle,  cache,  chora- g
--- ambassador ---
ambassador,  ambiguous, ament,  anagogy,  antagonist,  apagoge,  assay, Auriga,  axilla,  axiom,  axis,  axle,  cache,  chora- gus,  clarigation,  coact,  coagulate,  cogent,  cogi¬ tate,  demagogic,  deuteragonist,  embassy,  epact, essay,  exact,  examen,  exigent,  exiguous,  exility, indagate,  intransigent,  isagoge,  paragoge,  para- gonite,  pedagogue,  pilgrim,  prodigal,  protago¬ nist,  react,  redact,  remex,  stavesacre,  strategy, synagogue,  transact,  tritagonist,  and  the  second element  in  castigate,  clarigation,  fastigiate,  fu¬ migate,  fustigate,  levigate,  litigate,  mitigate,  na¬ vigate,  objurgate,  purge,  variegate, agent,  n.  —  F.,  in  the  sense  of  ‘act
--- axle ---
axle,  cache,  chora- gus,  clarigation,  coact,  coagulate,  cogent,  cogi¬ tate,  demagogic,  deuteragonist,  embassy,  epact, essay,  exact,  examen,  exigent,  exiguous,  exility, indagate,  intransigent,  isagoge,  paragoge,  para- gonite,  pedagogue,  pilgrim,  prodigal,  protago¬ nist,  react,  redact,  remex,  stavesacre,  strategy, synagogue,  transact,  tritagonist,  and  the  second element  in  castigate,  clarigation,  fastigiate,  fu¬ migate,  fustigate,  levigate,  litigate,  mitigate,  na¬ vigate,  objurgate,  purge,  variegate, agent,  n.  —  F.,  in  the  sense  of  ‘acting  force’,  fr. ML.  agens,  in  the  sense  of  ‘acting  person’,  fr. It.  agente;  both  these  word
--- strategy ---
strategy, synagogue,  transact,  tritagonist,  and  the  second element  in  castigate,  clarigation,  fastigiate,  fu¬ migate,  fustigate,  levigate,  litigate,  mitigate,  na¬ vigate,  objurgate,  purge,  variegate, agent,  n.  —  F.,  in  the  sense  of  ‘acting  force’,  fr. ML.  agens,  in  the  sense  of  ‘acting  person’,  fr. It.  agente;  both  these  words  derive  fr.  L.  agens, gen.  agentis,  pres.  part,  of  agere.  See  agent,  adj. agential,  adj.  —  Formed  fr.  agency  with  suff. -ial.
Ageratum,  n.,  a  genus  of  plants  of  the  thistle family  (bot.)  —  ModL.  ageratum,  fr.  Gk.  ayfj- pxxov,  neut.  of  ayf,paToc,  ‘ageless,  everlasting’, fr.  d-  (see  priv.  p
=== LEAF 32 ===
  —  F.  agilite,  fr.  L.  agilitdtem,  acc.  of agilitas,  ‘mobility,  nimbleness,  quickness  ,  fr. agilis.  See  prec.  word  and  -ity. agio,  n.,  the  discount  paid  to  exchange  one  cur¬ r
--- agent, ---
agent,  adj., and  verbal  suff.  -ate  and  cp.  cogitate. Derivatives',  agitat-ed,  adj.,  agitat-ed-ly,  adv., agitation  (q.v.)
agitation,  n.  —  F.,  fr.  L.  agitatidnem,  acc.  of  agi- tatio,  ‘motion,  agitation’,  fr.  agitatus,  pp.  of agitare.  See  agitate  and  -ion.
Derivative:  agitation-al,  adj. agitato,  adj.  agitated  ( musical  direction).  —  It., pp.  of  agitare,  fr.  L.  agitare.  See  agitate, agitator,  n.  —  L.,  fr.  agitatus,  pp.  of  agitare.  See agitate  and  agential  suff.  -or.
Agkistrodon,  n.,  a  genus  of  pit  vipers  (zool.) ModL.,  compounded  of  Gk.  dyxwxpov,  ‘fish¬ hook’,  and  oSdiv,  gen.  680VT09,  ‘tooth’.  The first  element  is  re
--- agony ---
agony’,  fr.  ML.  agonizdre,  fr. Gk.  dyuv^soflat,  ‘to  contend  for  a  prize,  to struggle’,  fr.  dycliv  ’assembly;  contest  in  the games'.  See  agony  and  -ize.
Derivatives:  agoniz-er,  n.,  agoniz-ing,  adj.,  ag- oniz-ing-ly,  adv.
agonothete,  n.,  leader  of  the  public  games  in  an¬ cient  Greece.  —  Gk.  dyivvofiixr;?,  ‘judge  of  the contest’,  formed  fr.  dyolv,  ‘contest’,  and  the
aikmite
agony
stem  of  Tt-ftsvat,,  'to  put,  place  .  See  agony  and theme.
agony,  n.,  extreme  pain.  —  OF.  (=  F.)  agonie, fr.  Eccles.  L.  agonia ,  fr.  Gk.  aytovla,  ‘struggle’, orig.  ‘struggle  for  victory  in  the  games’,  fr.  aytov, ‘assembly,  contest  in  the 
=== LEAF 33 ===
e,  n„  hook,  clasp.  —  F.  agrafe,  back  forma¬ tion  fr.  agrafer,  ‘to  hook,  fasten’,  fr.  d,  to (see  a),  and  OF.  grafer,  ‘to  fasten  with  a  hook’, fr.  grafe,  ‘hook’,  fr.  OHG.  k
--- agent, ---
agent,  adj. agynary,  adj.,  having  no  female  organs  (bot.)  — Formed  fr.  priv.  pref.  a-,  Gk.  yjvr;,  ’woman’ (see  gyneco-),  and  adj.  suff.  -ary. ah,  interj.  —  Of  imitative  origin, aha,  interj.  —  Of  imitative  origin.
Ahabah  Rabbah,  the  second  of  two  benedictions preceding  the  Shema  in  the  morning  prayer (Jewish  liturgy).  —  Heb.  ahabhdh  rabbd h,  lit. with  great  love’  (so  called  from  the  two  first words  of  the  text  of  the  benediction).  Ahabhdh, l°ve’,  derives  fr.  ahabh,  ‘he  loved’,  which  is  rel. to  Aram,  ahabh,  ‘he  loved’,  and  possibly  also to  Arab,  habba,  ‘he  was  moved’.  Rabbdh  is  fem.
rabh.  'great’  (whence  M
--- agriculture ---
agriculture.  - Formed  with  suff.  -an  fr.  L.  agrarius,  ‘pertaining to  land’,  fr.  ager,  gen.  agri,  ‘field,  land’,  which is  rel.  to  Umbr.  ager  and  cogn.  with  Gk.  xypo;, ‘field’,  Goth,  akrs,  OE.  tecer,  ‘field’.  See  acre and  agent  and  cp.  agriculture.  Cp.  also  acorn, agrestic,  agrio-,  agro-,  Agrostis  and  the  second element  in  onager.
Derivative:  agrarian,  n.
agree,  intr.  v.  —  ME.  agreen,  fr.  OF.  agreer  (F. agreer ),  ‘to  receive  with  favor’,  fr.  a  (F.  a),  ‘to’ (see  a),  and  gre  (F.  gre),  ‘will,  pleasure’,  fr.  L. gratum,  neut.  of  the  adjective  grams,  ‘acceptable, pleasing,  agreeable,  grateful’,  used  as  a  noun.  S
```


## [2026-09-04T18:33:30.519Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"aštar\\|astar\\|ashtar\\|aštr\" SNS.txt | head -20; echo \"=== pages ===\"; grep -n -i \"aštar\\|aštr\" SNS_pages.txt | head",
 "description": "Grep astar in SNS"
}
```


### [2026-09-04T18:33:30.589Z] TOOL RESULT

```
3569:. j^li '4-tfj'- 'j* 1 ' :astar/astr: >w»* 
3954:/W$ \\/kS*r\tt<S >(*+*») xarwastar : LI, 45) 
4560:.(*+**) hamastarlr^Wi^. 1774) hamaSstar-, *« 
6471:SstarSd/astarbrSd: yw-^jij***^ ^u^ i^ 
6473:.-i-ilj"^^^" jibrlt + >i-T=astar ji ^S> ^•jl, l > 1 C-»|l 
7175:.jii>*: xvastar: N V#*y 
7176:t?/Y<>^ .(jji.y^) x v astar :V 
9363:: jzk(AiWb. 862) aojah- :j' pairi. aojastara-:^- 
10706:!.P$ •(/Kk'fc. 1573)sastar- : i^tf-** sastar-:* 5 " 
16410:• 6/ir^.> J-K-j-.jijb.^jUiij-dastartar: Vj**>e>u-»o 
17207:-iiiS'l^.1^^,^ , 4^ ^jfauS Ijfl'ob^ :yastar3n: *•*-*» itJO* 
18110:daolastara-, daosatara- : £« 
28378:sastar- 174/2 
29017:vlsastaraa- 287/9 
29041:sastar- 174/2 
29374:pairi.aojastara- 144/8 
29571:daosastara- , daosatara 
30782:x v astar 101/4 
30812:yastaran 316/1 
33723:astar 35/17 
=== pages ===
```


## [2026-09-04T18:33:31.835Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT astra ===\"; grep -n \"aštrā\\|aštra\\|astra-\" BRT.txt | head -20; echo \"=== BRT asaya ===\"; grep -n \"ašaya\\|asaya\" BRT.txt | head -10",
 "description": "Bartholomae astra"
}
```


### [2026-09-04T18:33:31.913Z] TOOL RESULT

```
=== BRT astra ===
4290:•  j.  an-aiwLvastra-  Adj.  'unbekleidet':! <Äa  nara  . .  mayna  . .  'ra  (ND.)  V.  Ä  10.
8330:•  j.  ratu/ris  canmanqmca  pasu.vastra- nqmca  "upajaeäaätnÜä '* "  fraoiritarst n'almät  N-i«?'*.
9604:•  j.  kastra-  n.  'Spaten':  °r^m  paiü/.hjtyzim
11941:•  j.,  g.  tanü-  f.,  m.'*,  g.  tanuS-'*  n.  Xeib' 1)  der  Menschen  (und  menschenähnlich gedachten  Götter);  auch  sva.  'Person', wobei  die  obliquen  Ka^us  auch  im  Sinn von  ihn'  usw.,  sowie  -  mit  oder  ohne  Ava-, hava-  —  in  reflexiver  Bedeutung^*  im  Sinn von  'sich,  mich'  usw.  gebraucht  werden: ya  anrS  mainyui  frak?rfntat  avi  imqm 'nüm  yam  masyänqm  V.  20.3;  5;  s.  noch lu  aj  —  ks , .  a%r3  tafitus  äärayat  'naot haca  maiyehe  V.  20. 1 ;  —  yasca  .  .  dax- manam  avavantim  mazS  vXkänayat  yaha hl  'nui  anhal  V.  7. 5 1 ;  —  {yai)  *may'iain 'nUm**  aiwyästam  (sd.)  "irlris  .  .  N.  p5; *95^>  —  '*'"'  panna  (sd)  °nBm  aiwi.- si/ais  YX.  14. ^5 i  —  yaf  kl  'nus  hiskvi Aiynvi  (sd.)  pqsnu  bavai  V.5.31;  —  &«.- ayarpm..  'nüm  frasnayayania  Yt/0.  laz; 133;  —  US  'nüm  snayaita  us  *vasirä  V. J.  54;  —  "^ris  frasnaiti  •nunqm  . .  vastra- nam  V. /2.  a;  —  hakmt  aps  hvqm  'nüm pairi yaozdai^ita  V.  (),3i;  31",  ä  36,  37, 39,  Vd./5,  ig*,  20; —  Ja/  vlspam  kvam 'nüm  ayaozdata  k>r>naoiti  V,  ■¥.40;  — yal fU  zasta  nöie  frasnäta  aai  vJspam  hvqm 'nüm  ayaozdata  ik?n>»aoiti  Y.S.40; — yffi Aqm.nasüm  paitiäristfm  °nüm  yaozdai%yqn V.g.i;  —  iia  iristahe  'nüm  avaMsta  .. isaaa  (sd.)  ml  yaoldaitim  V,  Ä  100;   —
14505:zananqm  upäzSit  V.4.11;  11,  2.30;  — ■yff  zpmS  lis'rö  karsA /rakarayeiti  H.  lOi; 7o;(?),  loo'i?).  [Vgl.  noch  SnYNo.  i, zu  %ri^.Aastra-  \md  "hh'^x^is/s.]
14708:•  j.  ^SriS-hastra-'*  n.  'Versammlung  von dreien':  yä  bii.hastrim  sravayeiä  . .  *rsm
15871:*pasu.vastra-
15876:•  j.  'pasu.vastra-  n.  TCleid  aus  Tier-, /spez.i  Schaffell':  carimanam  'ranamca N.  >8;  8v,  —  'rahe  F.^b.
15878:•  j.  'pasu.vastra-  n.  "Viehstall';  az3m  . .
23152:•  j.  'vastra-  n.  'Kleid,  Gewand,  Kleidungs- stück': bawraitti  'rä  vatahüta  arydvT  Yt 5.  129;  —  spaSa  'rä  var^hatti  spaita Yljo.  136;  —  ?rf%ahm  zaranim  . . 'rSsca ktSh  bämanivä  Yt  i"],  14;  zit.  F.  5  (wo vüHrät  vaca  k°)\  —  'nm  . .  ubdanum V3  Izaimm  vä  V.  <?.  23;  —  sr%nm  'nm st»hrpa^aah»m  Vd.  20;20;  —  yänhuya- nam  ..  °ranam  Vd.2;  *I2;  —  hanhus :far^aheca  -rahe-a  V.  5, 38;  —  aSä :^ar»hi  ofaratu  a^ä  'rä  varahatu  V. 3.  19;  —  avalm  3?ar3h>mca  'rpmcij  Y. 5S-3i  z;  — yii0  x^arpia  jrOiS  'raV.^.S^i S7i  58,  Vyt45;  —  i^an^aliiyB  ..'ralibyS .  ,  astayanta  V,  J.  j8;  —  gave  x^arsham gave  'rtm'^  Y.  10.20;  —  mä  gSui  mS °rahe  hatS  aoäitlm  (sd.)   vag^sii  V.  4.46;
23156:•  j.  »vastra-  n.  'Fresse,  Maul,  Rachen': azSis  vilapahe  'r?m  N.  48.
24312:•  j.  virö.vastra-  n.  'Männerkleid':  avaval aipi  ya%a  Byum  'nm  ", .  (als  ein  Männer- kleid sva.)  als  das  Gewand  eines  Mannes" V.  8. 35.
29673:enüassen':  "anya.tkaliais^)  näirika pairi      "='"'  Etymologie  bringt  Dst.  ZA.  /.  «3- xsudra  fraipharTsaiW^  Nik.  7.  •  j.hastra- n. 'Versammlung' uzw.  solcher,
=== BRT asaya ===
2732:(AD.)  baom  Y.7.2; —  Aa  »i?  bara  'm (AP.)  bansmaca  U.io^;  —  'masca  bam- maca  N.  7/T.;  —  *kava  °ma  (IS.)  Aava bansmana  N.  108-,  — ■  °m>m  aSaya  b^nlsm Y.62.^;   —  yü  °md  (AP.)''  asaya   barat  * V.Ä79;    —    *kva    a/Sqm  (AP.)  ^'mim^    ' paiti.barat    N. /oj;    — ■    cvat    nä    nit?ma 'mähe  patti.barS  ratufri^  "wie  viel  Brenn-    _  .  .
3508:•  j.  apa-j-zära-  m.  'Abfluss,  {Wasser)ab- zwejgung'  a)  des  VouruAasa:  srayä  vouru.- kasaya  .  .  yeäke  . .  Aazannm  -ranam  . . kasal  aSsqm  °ranqm  c(&war>.sat»m  ayan.- baranqm..*arihas(a  me  *afi:aAka  Spö 'rö *vt)asaiti  vispJis  aoi  karsvqn  Y.  65.  4  £; —  aija  käu  'rö  bvat  zrayanAs  vouru.- kaiahe  vairil  yH  Aaosravä  nqma  Yt  ig. 56;  —  zrayauhs  vouru.kasahe  ,  .  vTspJ rairi/  a^araiti  vlsp}sca..nimraoi!  vlspSsca srlr!  'äire (AP.)'> \i.8.i,f>;~ katiht kaüht •,lire(XS.)  Ytj.ioi.  b)  der  Ratfka:\ tipa  guoim  'r>m  ra»hayh  Yt/5. 27,  j
3775:•  g-  C  j-)  aibi,  j.  aiwi  (aivi)''*,  p.  abiy 1)  Praen.  II  a)  mit  Akk.  bei  Veiben  der Bewegung;  a)  'ad,  zu  -  hin,  zu,  gegen  - hin':  Aauv  ksrJ' parärasJ'  'biy  vistaspam Bh.  j.  1;  D.  5.3;  —  nadPlabaira"  ..  'biy b-litrum  a/iyavt^  Bh.2.1;  J.14,  5.4;  — iJra*  . ,  hacUmi^  hamtii''iy(^  abavJ'  'biy avatn..astyavt^{sA.)  Bh.y.s;  13,  /.ii,i6% 5.  s;  —  'biy  bubirum  yd^ä  naiy  upilyatn (sd.)  Bh.  j.  19;  —  *adakiy  aham  asnaiy (sd.)  aham  "biy  *uva/am  Bh.  2.4;  —  _fra- vartil  agarbayata  utä  anayatä  "biy  mäm Bh.  2. 13;  J4,  /,  17,  5. 1,  4;  —  pasävc^ adam  käram  . .  fräisayant  'biy  viHäspam Bh.j.  i;  —  yuviyam  (sd)  ii^tanaiy  kacä . .  °biy  drayJ'  /)-«*  . .  D,  i'].y,  3,  Bh.j. 4.  ß)  'adversus,  contra,  gegen' :  pasäva'' kUra^  .,  'biy  avam  ..  aHyazia"  Bh.  1. 18;  — Aauv  karam  fraisaya'^  kari^uvatim . .  'biy avam  Bh.^.9 ;  3, 9, 1 1.||  b) mitLok. 'über, inBetreff  von  -';  /:>rasayai{%^)  'bl  ^Tu.lÄa
3867:•  j.aiwri.vaeSayanta-  Adj.  'der  zugewiesen werden  soll,  wird,  dedicandus':  haoma  . . asiiya  aiwi.vaioayamna  asaya  'la  ". .  qui dedicantur  .  .  dedicabuntur"  Y\.f).$.
4301:*asaya  *arpdusa  . .  nSiS  *°vis(i^  ästrydii vaHmaini  *asaya  (sd.)  x'a/na  vd  'vtsti astryeiti  N.  15.  2)  'Nichtlesen,  Nicht- vorlescn ,  Verweigerung  des  liturgischen Lesens':  yS  baoyö  (sd.)  aelahmSt  paräiti nöit pascalia  "Wistlm  ästryanti  (statt  Sing.) ". .  dann  macht  er  sich  durch  Verweige- rung des  (Liturgie-)  Lesens  nicht  sündig" N.4.
4305:•  j.  an-a'bdäta-  Adj.  'nicht  (mit  dem Hemd)  bekleidet':  bansma  asaya  frastar)- t^m  asaya  aiwyJst^fn  'few"  Vyt.  23.
4881:j,  ayayTi  N.  15%  lies  asaya;  %.  asä-,
5450:Zum  V.  'ar-.  —  VgL  aUy  und  S  ^Sg.  4  C mit  No.  —  Pü.:  larsäiäsJh.  ~~  0  Hds.  ä  rii-' lim;  5.  aber  Pii,  und  iSt.  Y.  60.  3,  wo  oioö- w^  xsnülasla  asayasra  . ,  paili.uiiilayasfa.
5693:asaya-
6071:'sa  (ab  Subj.)^  naptyoisä  . .  türaAya  uxjSn  a  a:  aevö  panlä  yS  'sähe  Y,  72.  1 1 ;  — (sd.)  Y.  4Ö.  1 3 ;  —  y7  xidknm  .  .  'iä .  ratus  . .  'sähe  *dasayat  paniqta  Vyt  42 ; /radähai  (sd.)  aspp/fsata  Y.ji.  161  — 1 — 'sähe  faiti  pantqm  ti/ahi  päi/i  mq^rynt %wahmät  äkras^a  manaahascä  yayä  syao- !  V.  ^  43  (s.  ob.) ;  —  sva.  'Stätte,  wo  das %anaU  °hm  %raosiä  (sd)  \.46.J;  — ,  j^sa  heittüxh  ist' :  haoa  nJ  ß-aounauayät/i vanh^us  :^aasus  i^aaatä  (sd.)  vaahius  'sähe  paiti  panlqm  drujg  vaiim^la  asmi- •/fli/J..  Y.J5.  5.  a)  GS.  mit /«ä- 'der  nqm  (sd.)  "waim  wird  uns  (die  Rinder) Pfad  des  ASa,  der  Wahrheit,  des  beUigen  !  zurUckführcn  zum  Pfad  des  Asa  . ."  Yt Rechts'   (s.  I  3  b  a):    dr^gvafö  .  .    *"Ji/j  70. 86.  ß)  GS.  mit  bir^  (sd.):  hnja
```


## [2026-09-04T18:33:40.658Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3565,3575p' SNS.txt; echo \"=== SNS idx ===\"; sed -n '33720,33726p' SNS.txt",
 "description": "SNS astar entry"
}
```


### [2026-09-04T18:33:40.779Z] TOOL RESULT

```
.f/Tr^ -Y?/YY^ \\/\iJ{A£M>. 204)arstat- : L~ 
•Y*/YY<^ Ij5 jbil j>iI <lj3 jtLil:astad, it: vw^wn)-" 

. j^li '4-tfj'- 'j* 1 ' :astar/astr: >w»* 
• TW/ir^ WiW' 263)astr3- : fc. 
. jj/ J**c 1j ^t^i I* : altar burdan : m°iv>** >kx>" 

-Y1/ir J -o^J** J^ 


=== SNS idx ===



astar 35/17 
astar burdan 35/19 
a-tarsagah 27/14 
a-tavanlg 27/17
```


## [2026-09-04T18:33:41.375Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Peitsche\" BRT.txt | head -10; echo \"=== asaya- ===\"; sed -n '5690,5700p' BRT.txt",
 "description": "Bartholomae Peitsche + asaya"
}
```


### [2026-09-04T18:33:41.440Z] TOOL RESULT

```
4888:•  j.  ayarv.dräjah-  n.  Dauer  eines  Tages': *;irr  vä  äzaili  (sd.)  'jS  vä  vaslryll  (sd.) "(so)  soll  man  ihm  (als  Strafe)  drei  (mit der  Peitsche)  diktiren  oder  einen  Tag  lang Feldarbeit"  N.  42,  *43  '>,  6g,  83,  loff;  6g.
5959:G.  anslässt"',  wird  er  ur,"  N.joj.  j  der  Peitsche"  P.p.         b)  kat  aaahe  paiti
6488:•  j.  aätra-Dhäd-  Adj.  'mit  der  Peitsche lenkend':  mi^rnn  .  .  °»Aäojm  amavanUm .  .  ra>aestq//i  Ytio.  112.
6492:•  j.  alträ-    f.    'Geisel,    Peitsche,    Knute':  narü  xsa^ra  xsaymU  "va  ni'jäiu.pifu  VL yat  b>r3z»m   barat   'ra  väam  "wenn  laut  1/7.  7;  5.130.
6493:die  Peitsche  knaÜt'  Yt,  /o.  1 1 3 ;  —  j«/ . . , ,  j.  as.bazav-  Adj.  'mit  tUchtigen,  starken 'rä  kakvqn  (sd)  Vtio.113;    —   Ja/  -4?  Vorderbeinen,  -schenkein':    uströ .  .   'zSus iyimai)  zaya  frabanm^  aum  y5  ahurö  .  .    (fjs.)  aii.kaüß  Vt  14- 12. suwram   (sd.)  .  .    'ramca  '>   zaramo.paisim  I      Kpü.;  läMib  biryär  zur  az-ar  bäsuvän. V.2.6;-»^Ä0,™)  .,y«/(sdL)  -ra,^  .    -    ^.t,„,.   ^dj.    (auch    fem.)    'rid, V.2  10.  .)    inb»    dit    pntsteihcht   ,^iai\A   bringsnd':  /r.valml .  .    ,4    ■Is
6504:'Stocic,  £ub'  und  ahd.  i-^öAi  'Peitsche'  usw.  j-  '^''''  (Nerbalf.):  s.  qs-.
9608:von  der  Peitsche:  yat  btrizam  barä£ aitra  väcim  aspanqmca  srifa  xsu/sqn aitra  kahvqn  Yt.  iO.  113.
10188:•  j.  gav-äza-  m.  'Gerät  zum  Antreiben des  Viehs',  Du.  'die  beiden  Geräte  z.  A, d.  V.',  d.  i,  'Stachel  und  Peitsche':  yalsqm
10191:•  j.  gav-äzista-'*  Adj.  'der  das  Vieh  am besten  antreibt,  womit  man  das  Vieh  am besten  antreiben  kann':  'zistaQiD.)  ffava:;J (sd.)  "Stachel  und  Peitsche,  womit  man das  Vieh  am  besten  antreibt"  V.  ;4. 10.    1
10955:•  j.  x^vaewayataäträ-  Adj.  (mask.  *ra-) 'der  die  Peitsche  kreisen  lässt,  schwingt': xsähra  . .  'ra  (APn.)  "Reiche,  wo  man die  Peitsche  schwingt"  Yt.5. 130.
=== asaya- ===
dby  Google
207
asaocant-
asaya-
«o8
Taten  hat,  des  Tun  richtig  isf:  na/r«|  glänzenden  Schleudersteine  (fahren»*)"  Yt asaone  ari.manatiha  (sd.) .  ."äwa  Y,  ig.  1 7. '  lo.  136.         2)  'Himmel'  (als  aus  Stein  ge-
Pn.:   täit  tumin.  ~   i)  NA.  ohne  Trennung.  ■  formt):   'smamm  J^amanbm  .  .  paoiryö.-
j.,  g.  as:  t.  »3-  {astu),  asl-  (*as<'a),  tah-.        ^dähm   (sd.)  ..  gaü'ilm  £ag>yayä  sisis  \t.
•   j.  a-8ao<Sant-    Adj.     'nichtflaminend':|7-4;  ^.79.35;   —    ima   -ima  (ob  AP.?)
'cantat  paiti  ä>rat  "ohne  dass  das  Feuer '/'^•"'O'«  damqn{ärae',ayam<iii)Yr.ii.2^);
flammt"  N.5<V".   '  | — fravalayn  ..  yti ..  vfaJäraym  'smamm
```


## [2026-09-04T18:33:53.858Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD ==\"; grep -n -i \"whip\\|aštar\\|astar\" PHD_mackenzie.txt | head -20; echo \"== NYB ==\"; grep -n -i \"aštar\\|whip\\|Peitsche\" NYB_vol2_glossary.txt | head -15",
 "description": "MacKenzie/Nyberg astar"
}
```


### [2026-09-04T18:33:53.937Z] TOOL RESULT

```
== PHD ==
1242:astar ['st'/l M 'st'r] sin.
1243:AstArenidan, astAren- ['selyn-ytn ] cause to sin.
1285:astar ['Itl] whip.
1934:dastar [d'ft'l] keeper, preserver.
2028: dosastar [dwlst1] west.
3257:kastar [kst'l] destroyer, wrongdoer.
3259:kastar [k'st)l] diminisher.
3496:mastarg [mstlg I (M mstgrg)] skull.
3675:nastaran [nstln l I N --] dog-rose, sweet briar.
3745:nigastar [11k' st' I] guard; protective.
3868:osastar ['wsstl] east.
4038:paristar [plst'll N parastar] maidservant.
4354:rastarih [lst'lyh] escape.
4510:sastar [s'st'll P s'st'r] commander; tyrant.
4973:tlzAna~ [t'c'nk I N taz(y)lina] whip.
5237:wastar [wstl = Av. wastra-] clothing, garment.
5238:wastar [wst'll N bistiir] wilful, obstinate; over-confident.
5240:wastar [w)stl] pasture, fodder.
5241:wastarag [wstlg] = wastar.
5242:wastaryoi [w)stlywf = Av. wiistryo./fuyant-] husbandman.
== NYB ==
5465:yama-: yam (&-)yaog-: &yuxtan (api-)yaog-: api-yuxtan yaoz-: āyēz-: yod- yašta-: yašt-fravahr yaštar-: yastar yašti-: yašt
```


## [2026-09-04T18:34:00.300Z] TOOL CALL #29: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-04T18:34:00.316Z] TOOL RESULT

```


```


## [2026-09-04T18:34:01.444Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== NYB astar ==\"; grep -n \"astar\" NYB_vol2_glossary.txt | head -20; echo \"== BQT ashtar ==\"; grep -n \"آشتر\" BQT_v1_pages.txt | head -10; echo \"== MON ashtar ==\"; grep -n \"آشتر\" MON_part1.txt MON_part2.txt | head -5",
 "description": "Nyberg astar and BQT/MON ashtar"
}
```


### [2026-09-04T18:34:01.532Z] TOOL RESULT

```
== NYB astar ==
622:ärästär restorer, pl. cas. obl. —-än 1105, arastarčh: apāc ~ restoration 111".
708:ästär [^st!]] sin 6911-14, — From Av. (1597 Sq.) à + star-; MPrthPrs ^s?r; Paz. astar.
2559:*mih(a)rg [mytlg; Vd. 21? mtlg] cloud, the sphere of the clouds 21”. — Existing in the sphere called in Av. mäna-, v.s. v. mänenak. -g is to be explained in the same way as in andarg, vastarg, vistarg, vazurg: the suff. -ka- was added directly to the stem (cf arišk, husk) and -k- voiced by contact with the preceding -r-; -tl- is no doubt the archaistic spelling -0r- for Milr -hr.; original form consequently *miür-ka > mihrg and then perhaps with secondary vowel miharg, cf *vazrka- > vazurg ete. Possibly derived from M36ra-, cf Yt. 109! where he is praised as the giver of rain; not identical with MTL? (for Prth MTR’) varan, FrP 1.
3264:rastar one who escapes: ~ kartan to bring about an escape, to rescue, to deliver 1135-6, — NP rastär.
3407:sastar [s'st?]] ruler, tyrant, of infidel (non-mazdayasnian) sovereigns, pl. cas. obl. ~-dn 614. — In this sense probably borrowed from Av. (1573) sāstar-; M Prth s?st?r ‘master, lord’ (A-H III, BBB).
4018:vastarg [wstlg] clothes 41?-4-? [472° read vistarg]. — Av. (1385) vastra- ‘clothing’ ; inser. SM 1. 50 wstlg; Paz. vastarg, vastrg ; Mand. lw. bastirga.
4211:vistarg [wstlg] bed coverlet 47%. — < OIr *vi-star-ka-, v. the next w. and cf vastarg; Ps. wstly, NP bistar ‘bed, mat- tress’; Talm. lw. bystrq?, Telegdi 235.
4326:x"arg [hwlg] consuming, of the fire: —-ē ātaxš 92°, with the same ending -é as in menöye, v. meno. — < *xvarka-, cf vastarg, vistarg, vitarg, vazurg, etc. Cf MPrth xwryndg or waryndg.
4356:x"astan [hwstn'] to trample pat ‘pad under the feet 271; pt pass. x%ast pat trained, practised in the use of 2617, 2911, — Av. (1875) xvah- ‘to drive, to press’, (1874) x%asta- ‘thrashed’. V. also x¥astar.
4363:xuastar [hw’st’l] a seeker, one who strives for a th. 56?6, — V. xudstan.
4421:yaštār [yšt'l] worshipper, he to whom it belongs to perform religious service 5314; patiš (= pat den) varzitar u ~ bütan 6311-12 cf den yaštan (v. above). — Av. (1280) yastar-.
5331:sastar-: sastar
5424:varšni-: gušn vastra-: vastarg vastra-: vastr
5465:yama-: yam (&-)yaog-: &yuxtan (api-)yaog-: api-yuxtan yaoz-: āyēz-: yod- yašta-: yašt-fravahr yaštar-: yastar yašti-: yašt
6385:astar: ~
6865:vastarg: ~
== BQT ashtar ==
== MON ashtar ==
MON_part2.txt:92720:۱ ند ۷). در هیچ حای اوستا «آشتر شتی»
```


## [2026-09-04T18:34:08.429Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82e%C7%B5-",
 "prompt": "Give the reconstructed root, its meaning, and the list of descendants especially Proto-Indo-Iranian, Avestan, Greek, Latin forms. Also list derived terms like *h₂éǵros."
}
```


## [2026-09-04T18:34:09.549Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D8%B1%D8%A7%D8%B2%D9%88",
 "prompt": "What is the etymology given for Persian ترازو (tarāzu)? Quote it including Middle Persian form and any Proto-Iranian reconstruction and cited authorities."
}
```


### [2026-09-04T18:34:15.579Z] TOOL RESULT

```
# Etymology of Persian ترازو (tarāzu)

Based on the Wiktionary entry, the Persian term derives from Middle Persian with this progression:

**Middle Persian form:** tlʾcwk' (/tarāzūg/)

**Origin:** The word was borrowed from Avestan tara.azu. The entry states: "borrowed from Avestan 𐬙𐬀𐬭𐬀.𐬀𐬰𐬎 (tara.azu)"

**Related cognates:** Sanskrit तुला (tulā) is listed as a comparable form, along with Iranian borrowings in Old Armenian (տարազուկ - tarazuk) and Udi (таьраьзуькӏ - täräzüḳ).

The entry does not provide a Proto-Iranian reconstruction, only tracing the word back to Avestan as the ultimate source through the Middle Persian intermediary.
```


### [2026-09-04T18:34:15.973Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂eǵ-

## Reconstructed Root and Meaning

The root **\*h₂eǵ-** has two distinct etymologies:

1. **"to drive"** (imperfective) - the primary meaning
2. **"goat"** - a secondary meaning with possible substratum loan origins

## Key Descendants

**Proto-Indo-Iranian:**
- Sanskrit: ईजते (ī́jate, "to drive"); अज (ajá, "driver"); अजिन (ajína, "goat-skin")
- Avestan forms including hunting and skin-related terms

**Ancient Greek:**
- ᾰ̓γός (ăgós, "leader")
- ἄγρα (ắgrā, "hunt")

**Latin:**
- āctus ("driven/acted") and related forms
- (co)āgulum (coagulation-related)
- actor ("one who drives/acts")

**Baltic-Slavic:**
- Lithuanian: ožỹs (goat); oženà (goat-skin)
- Old Prussian: wosux (goat)
- Slavic: azь and derivatives

## Notable Derived Terms

"\*h₂éǵ-ros" means "field, pasturage," while "\*h₂eǵ-ro-" relates to "hunt" or "slaughter," showing semantic extensions from the root concept of driving.
```


## [2026-09-04T18:34:21.358Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B7%D8%B1%D8%A7%D8%B2",
 "prompt": "Give the etymologies for Arabic طراز (ṭirāz) and for Persian طراز/تراز. What language is it borrowed from and what is the original meaning?"
}
```


## [2026-09-04T18:34:22.365Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/strategy",
 "prompt": "Give the full etymology of 'strategy', including Greek strategia, strategos (stratos + agein), French strategie, and dates."
}
```


### [2026-09-04T18:34:27.484Z] TOOL RESULT

```
# Etymologies of طراز

## Arabic طِرَاز (ṭirāz)

The Wiktionary entry provides two etymologies:

**Etymology 1:** This form references "طَرْز (ṭarz)" without elaborating on its origin.

**Etymology 2:** Described as an "occupational noun" derived from طَرْز (ṭarz), referring to an embroiderer.

The entry does not explicitly state the ultimate origin of the Arabic word.

## Persian طراز (terâz/tarâz)

According to the entry, this is an "Arabic respelling of a word which is originally a Persian loan into Arabic." This indicates the word's journey: it originated in Persian, was borrowed into Arabic, and the Persian form represents the original source language.

**Primary meaning:** The Persian etymology section indicates it relates to embroidery, with "alternative spelling of تراز (terâz, 'embroidery, embroidered ornament')."

**Secondary meaning:** As a proper noun, طراز refers to Taraz/Talas, a historic city in Kazakhstan renowned in classical Persian literature.

The entry confirms Persian as the original language, with the word subsequently adopted and reshaped in Arabic.
```


### [2026-09-04T18:34:28.463Z] TOOL RESULT

```
# Etymology of Strategy

**Strategy** entered English in 1810, deriving from the French *stratégie* (16th century) and the Latinized Greek *stratēgia*, meaning "office or command of a general."

The Greek term *stratēgia* combines two elements:

1. **Strategos** ("general, commander of an army"): composed of *stratos* ("army, troop") and *agos* ("leader")

2. **Stratos** etymologically means "that which is spread out," tracing back to the Proto-Indo-European root *str-to- and *stere- ("to spread")

3. **Agos** derives from *agein* ("to lead"), connected to the PIE root *ag- ("to drive, draw out or forth, move")

The word initially referred exclusively to "the art of a general, the science of war," but by 1833 it came to denote specific instances of strategic planning. Its application broadened to non-military contexts by 1887, reflecting the expansion of strategic thinking beyond purely martial domains.
```


## [2026-09-04T18:34:36.182Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%AF%D8%A7%D9%85%D8%B3",
 "prompt": "What etymology does Wiktionary give for Persian آدامس (âdâms) 'chewing gum'? Quote it."
}
```


## [2026-09-04T18:34:36.614Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Adam",
 "prompt": "Give the full etymology of the name Adam: Hebrew adam, adamah, Greek/Latin transmission, and any related notes."
}
```


### [2026-09-04T18:34:39.488Z] TOOL RESULT

```
According to Wiktionary, the etymology is as follows:

"Borrowed from English _Adams_, a historical American brand of chewing-gum, named after its inventor Thomas Adams."

The word entered Persian through a branded product name that became genericized to refer to chewing gum generally.
```


### [2026-09-04T18:34:48.135Z] TOOL RESULT

```
# Etymology of Adam

**Hebrew Origin:**
The name Adam comes from Hebrew *adam*, meaning "man," with the literal sense of "(the one formed from the) ground." This derives from Hebrew *adamah*, meaning "ground."

**Comparative Language Evidence:**
The etymology parallels Latin terms: *homo* ("man"), *humanus* ("human"), and *humus* ("earth, ground, soil"). These cognates across language families suggest a shared Indo-European root relating to earthlings or those formed from soil.

**Semantic Development:**
Beyond its original meaning, Adam acquired secondary associations in Christian tradition. The name came to signify "the evil inherent in human nature (as a consequence of Adam's fall)" and other qualities linked to the biblical figure, including nakedness and gardening.

**Related Expressions:**
The colloquial phrase "Adam's ale" for water dates to the 1640s. The idiom "not know (someone) from Adam"—meaning complete unfamiliarity—appears by 1784, with elaborations like "from Adam's off ox" by 1880.

**Name Derivatives:**
The Middle English pet form was *Addy*, which survives in the surname Addison, while older diminutive forms like *Adkin* and *Adcock* persist in various surnames.
```


## [2026-09-04T18:34:57.605Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && grep -n -i \"^VOP\\|^VDQ\\|^SNS\\|^MON\\|^AHD\" bibliography_raw.txt | head -20; echo \"---\"; grep -n -i \"VOP\" bibliography_raw.txt | head -5",
 "description": "Bibliography VOP VDQ"
}
```


### [2026-09-04T18:34:57.671Z] TOOL RESULT

```
---
3: TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
24: TABLE IV - Reference Abbreviations (continued...) 96 TLM 97 TTS 98 TYL 99 TZF 00 UNV 01 VDQ 02 VFO 03 VGH 04 VIE 05 VOP 06 VSF 07 WEB 08 WLD 09 ZAP 10 ZAW 11 ZFS 12 ZMA F. C. Tolman, Ancient Persian Lexicon, The Vanderbilt Oriental Series, American Book co. 1890-1908. G. Vambery, Etymologisches Worterbuch der Turko-Tatarischen Sprachen, Biblio Verlag, Osnabriick, 1972. W. Taylor, Arabic Words in English, Clarenton Press, London 1933. M. Abolghasemi, Tarikh Mokhtasar Zaban FarsT, ^-d1* oki j^""« ejJjIj Bonyad Andisheh EslamT Press, Tehran, 1373 (1994). J. M. Unvala, King Husrav and His Boy - Pahlavi Text and Glossary, Paul Geuthner publishers, Paris 1963. F. Badreh-t, Vajheh-hay Dakhil dar jl*=w oTjsji J-''2 i^l&amp;ejfj Qoran-e Majid, Translation of A. Jeffrey's book with Comments (see FVQ). Toos Publishers, Tehran 1372 (1993). M. Ahmad Soltam, Vajhgan FarsT dar Zabanhay ^jjl ^k-Sbj _ji ^j1* oT;'? OrupaT, Avay Niir Press, Tehran, 1372 (1993). H. Khadiv Jam, Vajheh Nameh Ghazalhay Hafez, Elmi Press, Tehran, 1371 (1992). £i9b» ^L^Jjc ^Ub OjT^ M. A. Sajjadiyyeh, Vajheh-hay Irani dar ^....JLCil ^bj ji ^IjjI ^la 03I3 Zaban EngelTsT, Bonyad Nayshabur, Tehran 1364 (1985). M. MoshM, Farhang Vajheh-hay Orupayl ^-"j1* j* ^kiJ lS1* °3'3 &gt;-^»j» dar FarsT, Alborz Press, Tehran 1371 (1992). K. Mehravand, Vajheh Sazi dar Zaban FarsT, Rasti press, Tehran 1349 (1970). v^-jl* ok) j4 lSJ1- °3'3 W. Collins, Webster's New Twentieth Century Dictionary of the English Language, second edition 1978. A. Walde, Vergleichendes Worterbuch der Indogermanischen Sprachen, two volumes, Walter de Gruyter &amp; co., Leipzig 1930-1973. H. W. Bailey, Zoroastrian Problems in the Ninth-Century Books, Clarendon press, Oxford 1943-1971. C. Bartholomae, Zum Altlranischen Worterbuch Nacharbeiten and Vorarbeiten, Vorlag von Karl J. Trubner, Strassburg 1906. M. Abolghasemi, Zaban FarsT va Sargozasht An, HTrmand Press, Tehran, 1375 (1996). F. Jonaydi, ZendegT va Mohajerat Aryaian, Bonyad Nayshabur, Tehran, 1374 (1995). A-15
```


## [2026-09-04T18:34:59.354Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find('ag-. To drive')\nif i<0:\n    import re\n    m=re.search(r'\\bag-\\.', t)\n    i=m.start() if m else -1\nprint(t[i:i+2500])\nEOF",
 "description": "AHD Watkins ag- root"
}
```


### [2026-09-04T18:35:00.906Z] TOOL RESULT

```
ag-. To drive. 1. Latin agere, to do, act, drive, conduct, lead: ACT, AGENDUM, AGENT, AGILE, AGITATE; (ALLEGE), AMBAGE, AMBIGUOUS, (ASSAY), (CACHE), COAGULUM, COGENT, ESSAY, EXACT, (EXAMINE), (EXIGENT), FUMI- GATE, INTRANSIGENT, LEVIGATE, LITIGATE, NAVIGATE, OBJURGATE, PRODIGAL, RETROACTIVE, SQUAT, TRANS- act. 2. Greek agein, to drive, lead: -AGOGUE, AGONY; ANAGOGE, (ANTAGONIZE), CHORAGUS, DEMAGOGUE, EPACT, GLUCAGON, HYPNAGOGIC, MYSTAGOGUE, PEDA- GOGUE, PROTAGONIST, STRATAGEM, SYNAGOGUE. 3. Suf- fixed form *ag-to- in Celtic *amb(i)-ag-to-, “one sent around” (*ambi, around; see ambhi), in Latin ambactus, servant (> Medieval Latin ambactia, office): AMBASSA- DOR, EMBASSAGE, (EMBASSY). 4. Suffixed form *ag-men- in Latin agmen, a train, a moving forward, a marching column, group: AGMINATE. 5. Suffixed form *ag-ti-, “weighing” (Greek agein, “to lead,” has a sense “to weigh”), whence adjective *ag-ty-o-, “weighty,” in Greek axios, worth, worthy, of like value, weighing as much: AXIOM; AXIOLOGY, CHRONAXY. 6. Possibly suffixed form *ag-ro-, driving, pursuing, grabbing, in Greek agra, a seizing: PELLAGRA, PODAGRA. Derivative agro-. [Pok. ag- 4]
ag-es-. Fault, guilt. Possibly Old English acan, to ache (perhaps < “to cause mental pain”): ACHE. [Pok. agos- 8.]
agh-1. To be depressed, be afraid. 1. Suffixed form *agh-lo- in Old English egian, eglian, to trouble, afflict: AIL. 2. Suffixed form *agh-es- in Old Norse agi, fright- ened: AWE. [Pok. agh- 7.]
agh-?. A day (considered as a span of time). Germanic *dagaz (with initial d- of obscure origin), day, in: a. Old English deg, day: DAY; (DAISY), TODAY; b. Old English denominative dagian, to dawn: DAWN. [Pok. agher- 7.]
agro-. Field. Derivative of ag-, “to drive” (< “place to which cattle are driven”). 1.Germanic *akraz in Old English zxcer, field, acre: ACRE. 2. Latin ager (genitive agri), district, property, field: AGRARIAN, AGRESTAL; AGRICULTURE, PEREGRINE, (PILGRIM). 3. Greek agros, field, and agrios, wild: AGRIA, AGRO-; AGRIOECOLOGY, AGRIOLOGY, AGROSTOLOGY, ONAGER, STAVESACRE. [In Pok. ag- 4.]
agwesi. Ax. Germanic *akwesi, *akusj6- in Old English zx, ax: AX. [Pok. agu(e)si 9.]
agwh-no-. Lamb. Germanic *aun- in verb *aunén in Old English éanian, to bring forth young: YEAN. [Pok. ag¥h-- no-s 9.]
ai-1, To give, allot. 1. Suffixed form “ai-t-yd in Greek aitia, cause, responsibility: ETIOLOGY. 2. Suffixed form *ai-td- in Greek diaitan, to decide, lead one’s life: DIET!. [Pok. 3. ai- 10.]
ai-2, An utterance. Suffixed for
```


## [2026-09-04T18:35:15.824Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find('aks-.')\nprint(t[i:i+600])\nEOF",
 "description": "Watkins aks- root"
}
```


### [2026-09-04T18:35:17.703Z] TOOL RESULT

```
aks-. Axis. 1. Suffixed form *aks-lo- in Old Norse éxull, axle: AXLE. 2. Suffixed form *aks-i- in: a. Latin axis, axle, pivot: axis; b. Latin diminutive axilla, armpit (< “axis point of the arm and shoulder”): AXILLA. 3. Suf- fixed form *aks-ld- in Latin dla (< *axla), wing, upper arm (see axilla in 2. b. for semantic transition): AISLE, ALA, ALAR, ALARY, ALATE, ALULA; ALIFORM. 4, Suffixed form *aks-on- in Greek ax6n, axis: AKON; MONAXON. [In Pok. ag- 4.]
akwa-. Water. 1. Germanic *agwjd becoming *auj6, “thing on the water,” in Old English ig, ieg, island, and
al-'
igland, iegland (land, land;
```


## [2026-09-04T18:35:17.753Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON esteratezi ==\"; grep -n \"استراتژ\" MON_part1.txt MON_part2.txt | head -5; echo \"== MON azhans ==\"; grep -n \"آژانس\" MON_part1.txt MON_part2.txt | head -5; echo \"== MON adam ==\"; grep -c \"آدم\" MON_part1.txt MON_part2.txt",
 "description": "Grep MON for loanwords"
}
```


### [2026-09-04T18:35:17.931Z] TOOL RESULT

```
== MON esteratezi ==
MON_part1.txt:11745:استراتژی: 2 (.) فن ادارة 
== MON azhans ==
MON_part2.txt:79358:ملی؛ سنا). آژانس (فره.) 
MON_part1.txt:2993:کارهایی را انجام دهد آژانس معاملات. 
MON_part1.txt:55401:آژانس» خبر گزاری پارس. 
== MON adam ==
MON_part2.txt:62
MON_part1.txt:100
```


## [2026-09-04T18:35:22.476Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11742,11750p' MON_part1.txt; echo \"== azhans ==\"; sed -n '2990,2996p' MON_part1.txt",
 "description": "MON esteratezi and azhans entries"
}
```


### [2026-09-04T18:35:22.560Z] TOOL RESULT

```
استر: ۲ [- ستر؛ مربوط به اسب قس. 
قاطر ] (.) (جان.) قاطر . 

استراتژی: 2 (.) فن ادارة 
عملیات جنگی؛ دانش رهبری عملیات 
نظامی؛ سوق الجیش. 

استراتوسفر: ۲ گنت (.) (همو.) 
طبقه‌ای از جو (اتسمفر) که فوق ۱۰ ۷ ۱۲ 
== azhans ==

ازانس: عصققة (ا.) نمایندگی» کارگزاری» 
بنگاهی که به نمایندگی موسات دیگر 
کارهایی را انجام دهد آژانس معاملات. 
خبرگزاری. 

اژزفنداک: 1 (- آزفنداک] ).(
```


## [2026-09-04T18:35:38.893Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN razu ==\"; grep -n -i \"razu\\|râzû\\|tarâz\" HRN.txt | head -10; echo \"== HUB razu ==\"; grep -n -i \"razu\\|râzû\\|tirâz\" HUB.txt | head -10; echo \"== CHEUNG az ==\"; grep -n \"^\\*Haz\\|\\*Haz \" CHEUNG.txt | head -10; echo \"== LKT terazi ==\"; grep -n -i \"terazi\\|terezy\\|tarâzû\" LKT.txt | head -10",
 "description": "Horn/Hübschmann/Cheung/Lokotsch"
}
```


### [2026-09-04T18:35:39.000Z] TOOL RESULT

```
== HRN razu ==
5452:Geldner hatte KZ. 24, 387 Note 2 aw. razura-
== HUB razu ==
== CHEUNG az ==
11745:*Haz 171 
11797:*Haz ‘to drive, lead’ 
28026:*yan / Skt. van ‘to win’ and *Haz / aj ‘to drive’ (cf. Skt. aji- m. ‘contest, race’). 
55860:*bar, *Haz (s.v.), *Huad 
55897:*garH? (s.v.), *Haz (s.v.), 
55997:*Haz (s.v.), *(H)uac (s.v.), 
56757:*garH' (sv.), *Haz (s.v.), 
57046:*Haz, *Huad, *naiH' , *rai9' 
== LKT terazi ==
4564:'Wage',  tk.  ebenso  terazi ;  hieraus  serb. teresije,  klruss.  terezy,  russ.  tereza ' Wase' ; rum.  tirizie,  terezie  'Wagscliale'.  [Löbel EITAP  94.    Mikl  SlEtWb  354  a.
```


## [2026-09-04T18:35:42.407Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4556,4570p' LKT.txt; echo \"=== CHEUNG ===\"; sed -n '11790,11830p' CHEUNG.txt",
 "description": "Lokotsch terazi entry, Cheung *Haz"
}
```


### [2026-09-04T18:35:42.476Z] TOOL RESULT

```
'Entfernen,  beseitigen',  dazu  subst.  Intin. tarh  'Abzug';  hieraus  it.  prov.  tara, frz.  tare,  sp.  pg.  <a>-a,  rum.  dar«;  dtsch. Tara,  engl,  tare;  russ.  tara  'Abzug  vom Bruttogewicht',  also  'Verpackungsge- wicht'. [Zur  Lautgestaltung  beachte man,  daß  das  ar.  tarh  fast  wie  farak gesprochen  wird;  Ableitung  von  fürah scheint  daher  zweifelhaft,  vgl.  RUSKÄ in  Isl  XII,  234-/235.]  Hierhin  gehört auch  it.  tarocco,  dtsch.  Tarock  'ein  Kar- tenspiel'. [DE  313.  Eguilaz  304.  ML 8568.    GrSVociSic  247.
2025.  Ar.  turahsakun:
'Wilde  Zichorie';  hieraus  la*.  taraxacum 'Löwenzahn,  Leontodon  laraxacum',  frz. taraxacon;  eng),  taraxacum.  [Devic  DEt 216/il7.    Lammens  Rem  235.
2Ui6.  Tk.  tarak: 'Kamm'  [vom  Stamme  tal,  tar  'groß, geräumig  >  erweitern,  ausstreuen',  c'ag. tarak  'Kamm',  eigentlich  'Zerstreuer', Vämbery  TktEtWb  S.  162,  Nr.  176  II]; hieraus  rum.  tarac,  arac  'Reben-  und Weinpfahr,  därac  'Wollkratze,  Krempel'.
2027.  Kas.-tat.  tarakau: 'Schabe';   hieraus  russ.  tarukan,  cech. tarakan  'dass.',    vielleicht  auch  poln. karuczan.     [Gorjajew  360.     Mikl  SiEt Wl)  347  a.
2028.  Ar,  taran^nbin:
'Flüssige  pers.  Manna'  [aus  pers.  türiin- gubin:  tär  'feucht,  irisch'  Hoin  NpEt S.  85,  Nr.  382  und  änguhin  'Honig'  eben- da 8.29,  Nr.  124];  hieraus  sp.  terenia- bin,  frz.  tireniabin  \teremabin  in  Roma- nia  XXXV,  409;  s.  Behrens  Beilr  264] 'dass.',  fiz.  tringibin.  [DE  350.  Devic DEt  219/220.  Eguilaz  505.  Lammens Rem  239.
2029.  Pers.  täräzQ:
'Wage',  tk.  ebenso  terazi ;  hieraus  serb. teresije,  klruss.  terezy,  russ.  tereza ' Wase' ; rum.  tirizie,  terezie  'Wagscliale'.  [Löbel EITAP  94.    Mikl  SlEtWb  354  a.
Ar.  Urb.]
160
2030.  Ar.  tarb:
'ümenlum,  Netz',  d.  h.  Faltungen  (Dupli- katuren)  des  Bauchfells  (Peritonium)  der Wirbeltiere,  also  auch  beim  Menschen [aus  pers.  därb  'tetf  Horn  NpEt  ö.  97, Nr.  43ö];  hieraus  nilat.  der  Anatomen zirbits,  it.  zirbo,  sp.  pg.  zirbo,  zerbo 'Leibesnetz',  unmittelbar  mit  Metathesis it,  tn'ppn,  frz.  tripe,  prov.  kat.  sp.  pg. tripj  'Eingeweide,  Kaidaunen',  it.  (dial. Piemont  bis  Neapel)  tripa  'Bauch'. [HArHebrAn  247/250.    ML  8703.
2031.  Ar.  tarbüs:
'Roter  Fez'  [Dozy  Vetem  220,  250,  289 ; aus  tk.  ter  'Schweiß'  und  pers.  püs, Präsensstamm  püsidän  'bedecken',  s.  hier Nr.  1625,  also  'Schweifskappe'] ;  hieraus frz.  tarbouch,  dlsch.  Tarbusch,  engl,  tar- boosh,  tarbouche.
=== CHEUNG ===

*IE COGNATES: Gr. 800€, OCS oči (du. tantum) ‘eyes’, Lat. oculus (m.), Lith. akis 
‘eye’, etc. 

*REFERENCES: WIM II/2: 642; Werba 1999: 615; Rastorgueva -Edel’man 2000: 281 f. 


*Haz ‘to drive, lead’ 

*AVESTAN: az- ‘to lead’ || (+ *aua-) ‘to lead down, chase away’ || (+ *para-) ‘to 
carry, take away’ || (+ *ni-) caus. ‘to straiten’ (cf. De Vaan 2003: 34) = Liste: 10 
Pres. them.: IND. 3sg. YAv. azaiti, med. 35р. YAv. azaite (Yt 10.38, V 5.37), med. 3d. ҮАУ. *azöide (V 
3.11), 3р1. YAv. parazenti (Yt 13.68), INJ. 3sg. YAv. auuazat ‘chased away’ (Yt 19.81, Hoffmann 1968: 
283, fn. 4), 3р1. ҮАУ. azon (Yt 13.37), SUBJ. 1sg. YAv. azani (Yt 5.34, Yt 9.14, Yt 9.30, etc.), 3sg. YAv. 
"azaiti (Fr.), med. 3sg. YAv. azaite (V 18.76), 3pl. ? OAv. aza0a (Y 50.7, Y 64.3), OPT. 3sg. Y Av. para 
... aZoit (V 18.12), med. 35р. azaéta (V 18.68); Partic.: pres. med. Y Av. azamna- (Yt 10.86); Caus.: pres. 
IND. 35р. Y Av. azaiiaiti (Vn 13, Vn 15; De Vaan 2003, 1.с.), INJ. med. 35р. YAv. niiazata (Yt 5.127), 
3pl. YAv. niiazaiion (V 13.30) 

*MIDDLE PERSIAN: (+ *ni-) BMP nyd’c /niyaz/, MMP ny’z ‘want, need, misery’ 
(LW) > DMMPP: 48b 


172 *Hgar 


*PARTHIAN: (+ *ni-) ny’z ‘want, need, misery’ = DMMPP: 48b 

*KHOTANESE: hays- ‘to drive, send’ (with sec. h- ?) = SGS: 148 

*SOGDIAN: (+ *ni-) CSogd. ny’z’wt ‘needing, needy’, MSogd. ny’z ‘need’ (GMS: 
§1060) 

*NWIR: ? NP javazah, Gz. yane ‘mortar’ || (+ *ni-) NP niyaz ‘need’ || (+ *ui-) Khuns. 
vis(s)/viz- (inch. ?) ‘to seek; [+ va] ‘to find’, Abyan., Abz. yösta/yüz-, Anar. usse/ 
(y)uz-, Ard. viyoste/viyoz-, Fariz. -juz-, Gz. yuz-/yus(s)-, Nn. yusse/yuz-, Tr. vósta/ 
vöz-, Varz. ose/oz-, Yar. -just-/-juz- ‘to find’, Qohr. vüsta/vüz- ‘to find, obtain’, 
Natan. -just/-juz-, Meim. bem-vi:ft/a-vi:z- ‘to discover; to find’. 0 NP javazah is 
from *jaua-a(n)za-ka-, on which see Tafazzoli ("do vazah-i parti az diraxt-i аѕшӣ" [= 
Two Parthian words from the "Draxt-i-Asuri"], unpubl.). Differently, Hasandoust 
2001-2002: 36: *iaya-baja- ‘barley breaker’ (see *baj). The reconstruction would be
```


## [2026-09-04T18:35:52.911Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT act ==\"; grep -n -o -i \"Act, a deed.\\{0,320\\}\" SKT.txt | head -3; echo \"== SKT strategy ==\"; grep -n -o -i \"Strategy.\\{0,300\\}\" SKT.txt | head -3; echo \"== SKT acre ==\"; grep -n -o -i \"Acre, a field.\\{0,250\\}\" SKT.txt | head -2",
 "description": "Skeat act/strategy/acre"
}
```


## [2026-09-04T18:35:54.131Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ترازو\" incoming/ARY/ARY_pages.txt | head -5; echo \"== ARY latin ==\"; grep -n -i \"TARAZU\\|TARAZ\" incoming/ARY/ARY_latin_index_pages.txt | head -5",
 "description": "Aryanpur tarazu"
}
```


### [2026-09-04T18:35:54.626Z] TOOL RESULT

```
== SKT act ==
== SKT strategy ==
== SKT acre ==
```


### [2026-09-04T18:35:54.688Z] TOOL RESULT

```
== ARY latin ==
```


## [2026-09-04T18:35:58.294Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -i \"STRATEGY.\\{0,250\\}\" SKT.txt | head -3; echo \"---ACT---\"; grep -n -o -i \"\\bACT\\b, .\\{0,250\\}\" SKT.txt | head -3; echo \"---AGENT---\"; grep -n -o -i \"AGENT.\\{0,250\\}\" SKT.txt | head -3",
 "description": "Skeat retry"
}
```


## [2026-09-04T18:35:59.547Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la incoming/ARY/ 2>/dev/null | head; wc -l incoming/ARY/ARY_pages.txt 2>/dev/null; grep -c \"تراز\" incoming/ARY/ARY_pages.txt 2>/dev/null",
 "description": "Check ARY files"
}
```


### [2026-09-04T18:36:00.002Z] TOOL RESULT

```
---ACT---
84:act,  agiu,
107:Act,  such  mere  derivatives  as
5388:act,  a  dial Gk.  ^p6of.   I  perform.     (V  DAR.) dramatit  (from  S^/iar-):  &c.
---AGENT---
422:AGENT.  s
616:Agent.
1535:agent
```


### [2026-09-04T18:36:00.062Z] TOOL RESULT

```
total 9460
drwxrwxr-x  3 sfmqrb sfmqrb    4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb    4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 8102112 Sep  4 14:06 ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  586473 Sep  4 14:06 ARY_latin_index_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  960497 Sep  4 14:06 ARY_pages.txt
drwxrwxr-x  2 sfmqrb sfmqrb   20480 Sep  4 13:30 ARY_pages.txt.pages
16204 incoming/ARY/ARY_pages.txt
0
```


## [2026-09-04T18:36:04.286Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '420,424p;614,620p' SKT.txt; echo \"=== FSD strategy ===\"; grep -n -o -i \"strategy.\\{0,300\\}\" FSD_vol4.txt | head -3",
 "description": "Skeat context and FSD strategy"
}
```


### [2026-09-04T18:36:06.714Z] TOOL RESULT

```
b.
^^.  oi  arrrtiy
AGENT.  s
AflVlght :  >ee  Fright. A£f^nt :  see  Front. Afloat.  (E.)     foTotiJioat, Afbot.  (E,)     Vox  on  foot. Afore.  (E.)    Voton/art;  K.S.om/»ran» afore. AlVaia   (F.  -  L.  aw*/  Tent.)     Pp.   of
AA-eeh.  (E.)  For  Qnfrtih  or  pffrtsh ; see  Anew.
Ambi .  Amb-,  prefix.  (L.)  L  av^ about :  cf.  Gk.  ^pi^i,  on  both  sides,  whenci E.  pre6x  amphi'..  KeUted  to  L.  awAti Gk.  QM^.  both.
Ambient,  going  about  (L.)  See  Ittai> orant.
AmbisuoujB.  (L.)    See  Agent.
Ambition.  (F.-L.)    Sec  Itinerant
Amble.  (F.-L.)    M.E. *»/«*/!•«  -1*1. F. ambltr,  to  go  at  an  easy  pncc.—  I tart,  to  walk.     %  Perhaps  for  d- to  go  about;  from  amb-,  aboot ,  ..u.  •• , to  go,  appearing  in  Gk.  0alrtir,  to  go  ;  ttc Ambi-  and  Base  (3).
ambulance,  a  moveable  hospital.  <f. —  L.)  F.  ambuUfice, — L.  amimianti- foim  of  prcs.  jiart.  of  atithul<tre.
ambulation,  a  walking  about From  L.  ambulatio.  a  walking  abont, ambiuatus.  pp.  cA  atni-ulart.
=== FSD strategy ===
23985:Strategy
23990:strategy Zaracoza,  furnished  a   point  of  union  for  two  ereat  roads, and  was  consequently  of  atrateote  importance WFP  Napieb  WartnlAcPernn«u/a\ol  i,  bk  i,p  48  [a  abI [<  Gr  slratSgikos.K  stratSQOs,  see  stratagem  ]   stra-teg'- 1-caU  —   strategic  line  (Af/i ),  a   line  the  ma
23990:strategy  —   s   point,  a   location that  aCords  a   vantage-ground  against  a   foe,  as  a   mountain- pass,  or  an  eminence  commanding  a   waterway  —   stra- tcg'l-cal-ly,  adv  —   stra-teglcs,  n   The  art  or  science  of strategy  [in  strategy
```


## [2026-09-04T18:36:18.807Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"آژان\" MON_part1.txt | head -5; echo \"== FSD stratagem ==\"; grep -n -o -i \"stratagem.\\{0,300\\}\" FSD_vol4.txt | head -2",
 "description": "MON azhan, FSD stratagem"
}
```


## [2026-09-04T18:36:20.125Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%AF%D9%85",
 "prompt": "Give the etymology sections for Arabic آدم (ʾādam) and Persian آدم (âdam). Which language is Persian âdam borrowed from? What does Arabic ʾādam derive from (Hebrew? Aramaic? Syriac?)"
}
```


### [2026-09-04T18:36:20.364Z] TOOL RESULT

```
2163:آژان» مه پلیس. 
2988:آژان؛ (.) ن‌ماینده» کارگزار (کم.) 
2993:کارهایی را انجام دهد آژانس معاملات. 
32624:آژان» عسس » مسحتسب. اداره تاش 
55401:آژانس» خبر گزاری پارس. 
== FSD stratagem ==
8615:stratagems sharks,  rt  To  fish  for  sharks,  as,  to  go  sharking sharks,  n   A   plagiostomous  selachian,  havung  lateral gill-opemngs  Sharks  are  mostly  of  the  high  seas,  and are  found  mainly  within  the  tropics  Some  pelagic  species attain  a   great  size,  and  many  are  armed  with
23971:stratagems collectiv'ely  [<F  stTalaQhme,<lj  #tfra- iegema,  <   Gr  stratigema,  <   strategos,  general,  <   stratos, army,  +   lead  1   Syn®  see  artifice  chicanery,  plot
```


### [2026-09-04T18:36:25.642Z] TOOL RESULT

```
# Etymology of آدم (Adam)

## Arabic Etymology

According to the Wiktionary entry, Arabic آدَم (ʔādam) is described as "Terminology of the religious sphere borrowed from Hebrew אָדָם (āḏā́m, 'man, person')."

## Persian Etymology

Persian آدم (âdam) is "Borrowed from Arabic آدَم (ʔādam), borrowed from Biblical Hebrew אָדָם (āḏā́m), from Proto-Semitic *ʔadam-."

**Which language is Persian borrowed from?**
Persian آدم is borrowed from **Arabic**, which itself borrowed from Biblical Hebrew.

**What does Arabic derive from?**
Arabic ʔādam derives from **Biblical Hebrew** (אָדָם), ultimately tracing back to Proto-Semitic *ʔadam-. The entry specifies the Hebrew origin, not Aramaic or Syriac.
```


## [2026-09-04T18:36:43.120Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON adams ==\"; grep -n \"آدامس\" MON_part1.txt MON_part2.txt | head -3; echo \"== BQT adams ==\"; grep -n \"آدامس\" BQT_v1_pages.txt | head -3; echo \"== MON taraz ==\"; grep -n \"^تراز\\|تراز:\" MON_part1.txt | head -5; echo \"== WEB adams gum ==\"; grep -n -o -i \"chewing gum.\\{0,150\\}\" WEB_vol1.txt | head -3",
 "description": "MON/BQT adams, taraz"
}
```


## [2026-09-04T18:36:43.915Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/agent",
 "prompt": "Give the etymology of 'agent', 'agency', and the PIE root *ag- entry, including Latin agere and its English descendants."
}
```


### [2026-09-04T18:36:45.024Z] TOOL RESULT

```
== MON adams ==
== BQT adams ==
== MON taraz ==
7703:احتراز: 22 [ع.] (مسص‌ل.) برهیز 
32588:ترازو» کفه. 
39504:تراز: ۰۵2 (.) رشتة رسمان خام. 
39506:تراز: ۱۵22 () (گیا.) صنوبر. 
39508:تراز: 2 ([-<- طراز» معز. |( ریشت؛ 
== WEB adams gum ==
32178:chewing gum.
85446:chewing gum. , acaroid gum or gum acaroides; a gum given off by certain species of Xanthorrhæa. gum ammoniac; ammoniac, a natural gum resin. ' gum anime or animi
113547:chewing gum, incense, etc. Bar- bary mastic is obtained from the Pistacia at- lantica, which grows in the north of Africa and the Levant.
```


### [2026-09-04T18:36:51.732Z] TOOL RESULT

```
# Etymology of Agent, Agency, and *ag-

## Agent (noun)
Appearing in late 15c., "agent" derives from Latin *agentem* (nominative *agens*), meaning "effective, powerful." This comes from the verb *agere*, which meant "to set in motion, drive forward; to do, perform; keep in movement." The word's meanings evolved: by the 1550s it referred to "any natural force or substance which produces a phenomenon," and by the 1590s it denoted a "deputy, representative." The spy sense emerged around 1916.

## Agency
While not detailed separately in the provided content, "agency" appears as a related entry, deriving from the same Latin root and denoting the action or work of an agent.

## PIE Root *ag-
The ultimate source is the Proto-Indo-European root *ag-, which meant "to drive, draw out or forth, move." This foundational root generated Latin *agere* and its numerous English descendants through various Romance language intermediaries.

## Latin *agere* Descendants
Beyond "agent," English inherited multiple related terms from *agere*'s agent nouns: *motor* ("mover"), *factor* ("doer, maker"), and *procurator* ("manager, agent"). Each reflects different applications of the core concept of action and motion embedded in this ancient root.
```


## [2026-09-04T18:36:57.718Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ترازو:\" MON_part1.txt | head -5; sed -n '39504,39530p' MON_part1.txt",
 "description": "MON taraz/tarazu entries"
}
```


### [2026-09-04T18:36:57.799Z] TOOL RESULT

```
39549:ترازو: ۰25 (.) (فز.) آلتی که برای 
50639:ترازو: سوراخ دو سر شاهین ترازو که 
80565:درهم) یک کسپلوگرم. سنک ترازو: 
تراز: ۰۵2 (.) رشتة رسمان خام. 

تراز: ۱۵22 () (گیا.) صنوبر. 

تراز: 2 ([-<- طراز» معز. |( ریشت؛ 
آرایش. ن_قش و نگار پارچه. زردوزی 
پارچه. 

تراز: 52 () (بناء معم.) آلتی است که به 
توسط آن پستی و بلندی سطحی را معلوم 
کنند و آن انواغ مختلف دارد. تراز آابی: 
(فره.) عبارت است از لوله‌ای فلزی که دو 
سر آن شیشه‌یی و دارای مایع رنگین است و 
آن را بر روی سه پایه قفرار دهند و 
چوب‌های دیکری در مقابل نگاه می‌دار ند و 
یننده (ترازکننده) سطح مایع را در دو شیشه 
با نقاط هم‌سطح و هم‌ترازی روی چوب‌ها 
نشان نماید تا بدان وسیله اختلاف ار تفاع دو 
نقطه را بسدست آورند. این تراز در 
نسقشه‌برداری و راهسازی و غیره مورد 
استفاده دارد. تراز هوایی: (فر.) آلتی که 
تن ای بوون نع ب لت ار آن 


استفاده کنند و عبارت است از یک لوله 
شیشه‌پی سربسته که در آن مایع رنگینی 
ريخته‌اند به اندازه‌ای که کاملا بر شود و
```


## [2026-09-04T18:37:08.944Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%90%D7%93%D7%9E%D7%94",
 "prompt": "Give the Hebrew entry אדמה (adamah): meaning and etymology, including relation to אדם (adam) 'man' and אדם 'red'. Quote the etymology."
}
```


## [2026-09-04T18:37:09.313Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ambassador",
 "prompt": "Give the etymology of 'ambassador' and 'embassy', including Latin/Gaulish ambactus and the PIE root."
}
```


### [2026-09-04T18:37:14.849Z] TOOL RESULT

```
# Hebrew Entry: אדמה (adamah)

## Meaning
According to the Wiktionary entry, אדמה (adamá) is "a feminine noun meaning earth, soil, or land."

## Etymology
The provided content does not explicitly state an etymology connecting אדמה to אדם (adam, meaning "man") or to אדם (meaning "red"). 

However, the entry does indicate that אדמה belongs to the Semitic root א־ד־ם (ʾ-d-m), which governs "9 terms" in Hebrew. The declension table shows the word follows the Hebrew pattern קְטָלָה.

The entry notes synonyms including ארץ (érets) and קרקע (karká), and lists derived terms such as תפוח אדמה (tapúakh adamá, "potato").

**Note:** The etymological relationship you're asking about—connecting אדמה to אדם (man) and the color red—is not addressed in this particular Wiktionary entry, so I cannot provide a quote supporting that connection from the source material.
```


### [2026-09-04T18:37:16.038Z] TOOL RESULT

```
# Etymology of Ambassador and Embassy

**Ambassador** (late 14c.) comes from Old French *embassator*, deriving from Provençal or Old Spanish sources. The term traces back to Latin *ambactus* meaning "a servant, vassal," which originated from Celtic *amb(i)actos* signifying "a messenger, servant."

**Embassy** (1570s) follows a similar path, coming from French *embassee* through Italian *ambasciata*, ultimately from Gaulish *ambactos* meaning "dependant, vassal."

Both words share the same ultimate roots: the PIE *\*ambhi-* ("around") combined with *\*ag-* ("to drive, draw out or forth, move"). As the dictionary notes, *ambactos* literally means "one going around," reflecting this etymological composition of movement and agency combined.

Interestingly, the United States distinguished between ambassadors and ministers until 1893, with ministers representing the state rather than the sovereign.
```


## [2026-09-04T18:37:17.876Z] AGENT

Now let me archive all the URLs I used.


## [2026-09-04T18:37:22.064Z] TOOL CALL #56: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂eǵ-\" \\\n \"https://en.wiktionary.org/wiki/ترازو\" \\\n \"https://en.wiktionary.org/wiki/طراز\" \\\n \"https://www.etymonline.com/word/strategy\" \\\n \"https://en.wiktionary.org/wiki/آدامس\" \\\n \"https://www.etymonline.com/word/Adam\" \\\n \"https://en.wiktionary.org/wiki/آدم\" \\\n \"https://www.etymonline.com/word/agent\" \\\n \"https://en.wiktionary.org/wiki/אדמה\" \\\n \"https://www.etymonline.com/word/ambassador\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 35 verification (roots Adhamah, Ag/Agros)\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-04T18:37:26.483Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c66eb6fbbf324c5e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c3147513546e91f4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1e562e240ab10bca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5a524583a77da29f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7708e55cd1682e0a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e398863648798a00.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/80d612295da16dc5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b17ba14d39f25d8c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d8c4c4dd92564248.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bbf1206f1395eb5f.txt
```


## [2026-09-04T18:37:34.687Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FSD Adam ==\"; grep -n -o -i \"Adam,\\{0,1\\} n\\..\\{0,200\\}\\|Ad'am.\\{0,200\\}\" FSD_vol1.txt | head -3; echo \"== WEB Adam ==\"; grep -n -o -i \"Adam\\b.\\{0,200\\}\" WEB_vol1.txt | head -4; echo \"== AFA adam ==\"; grep -n -o -i \"\\bAdam\\b.\\{0,120\\}\" AFA.txt | head -3",
 "description": "FSD/WEB/AFA Adam"
}
```


### [2026-09-04T18:37:36.600Z] TOOL RESULT

```
== FSD Adam ==
7220:Ad'am-and'Eve",  n.  1.  The  puttyroot  (Aplectrum hlemalc),  a   low  North- American  orchid.  2.  A   British orchid  ( Orchis  maculata).—  Adam’s  ale  [Colloq.],  water.— Adam's  apple.  1.  See  po
7259:Ad'am-ite,  I   ad'am-ait;  2   iid'am-It,  a.  Descended in  the  female;  barrenness.  [<  Gr.  a-  priv.  -f-  kyesis,  1*  A   movement  executed  less  slowly  than  adagio  2.  A   from  Adam;  human
7261:Ad'am-It-Ism,  n. Med.  1.  Means  of  preventing  conception.  2.  Drugs  for  an  adaQl°  march.  II.  n.  1.  A   degree  of  time  quicker  than  The  principles  or  practise  of  the  sect  of  Adami
== WEB Adam ==
2642:Adam's ale; water.
2643:Adam's apple; (a) the thyroid cartilage, the prominent part in the front of the throat, particularly in males: so called from the superstition that it was caused by the for- bidden apple sticking in Adam'
2644:Adam's needle; the Yucca filamentosa, or bear grass.
2645:Adam, 18th-c. British architects.] relating to a style of English furniture and architecture with straight lines and ornamentation of garlands,
== AFA adam ==
7869:Adam geflocbten** (aas |^ Gen 2, SSabge-
```


## [2026-09-04T18:38:02.753Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== RCH whip ==\"; grep -n -o -i \"astar.\\{0,120\\}whip.\\{0,80\\}\\|whip.\\{0,60\\}\" RCH.txt | head -8; echo \"== FRS ==\"; grep -n \"آشتر\" FRS_pages.txt FSF_pages.txt 2>/dev/null | head -5",
 "description": "Richardson whip, FRS/FSF ashtar"
}
```


### [2026-09-04T18:38:07.158Z] TOOL RESULT

```
== RCH whip ==
ugrep: error: error at position 128
x80-\xbf][\x80-\xbf]*){0,60}
                            \___exceeds complexity limits


== FRS ==
```


## [2026-09-04T18:38:09.429Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"a whip\" RCH.txt | head -8",
 "description": "Richardson whip"
}
```


### [2026-09-04T18:38:09.511Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:38:12.463Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"whip\" RCH.txt; grep -n \"whip\" RCH.txt | head -5; echo \"--- astar ---\"; grep -n \"ashtar\\|āshtar\" RCH.txt | head -5",
 "description": "Richardson grep whip"
}
```


### [2026-09-04T18:38:12.566Z] TOOL RESULT

```
51
2394:other with  whips.  Drinking  the  entire  contents  of  a   cup.
2733:a   whip,  &c.).  Pouring*  out  water,  by  inclining  the  vessel  in which  it  is  contained.  Tmpowering  or  sending  one  to  demand or  exact  a   debt  from  another.  Squinting,  or  causing  to  squint.
7049:Alp1y-a!  aazcdfy  (pi.  o{]ffya  aaiot)  Scourges,  whips.
7617:A   aibahty^  The  dawn.  A   whipping-post.
8258:de&ced(booka).  Having  no brother-germain.  (Ri^)with. out  a   whip  or  iwhch.
--- astar ---
14837:p   cu^b  bashty  The  main  beam  of  a   house, p   bashtaraky  A   starling  or  stare.
16918:p   bishtdlam  (or  bishtdm)y  A   parasite, p bishtar  or  bashatry  The  archangel  Michael  (who  they, say  has  the  distribution  of  riches  to  mankind).  A   cloud, p jiJLJ  bushtary  Pimples,  pustules ;   the  thrush, p   bashtaraghy  Melilot.  A   herb  with  which  they  tinge the  body.  Part  of  a   cluster  of  grapes  or  dates, p   C/jIJLj  bushturky  A   cup,  a   drinking-vessel.
16919:F   bushturamy  A   pimple,  pustule.  Small-pox,  ineasles. p   sjiJL)  bashtarahy  A   thorny  shrub.  A   dish  composed  of  sesame- flour,  and  dates.
24188:F jitJ  Tashtar  (or  Tashtl)^  Michael  the  archangel, p   (ashtany  A   kite.  A   large  axe.
85190:AjjiS^  mashtary  Halved,  divided  in  two.
```


## [2026-09-04T18:38:40.903Z] TOOL CALL #61: Bash

```json
{
 "command": "ls data/ ; ls tools/ | head -40; find . -maxdepth 3 -iname \"*.pdf\" 2>/dev/null | head",
 "description": "Look for book PDF and tools"
}
```


### [2026-09-04T18:38:40.997Z] TOOL RESULT

```
ANOMALIES.md
extracted
EXTRACTION_SPEC.md
research
translations
verification
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
./EtymologicalDictionary-persian-english.pdf
```


## [2026-09-04T18:38:44.090Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 -c \"\nimport subprocess\n\" ; pdftotext -layout -f 35 -l 35 EtymologicalDictionary-persian-english.pdf - 2>/dev/null | head -60",
 "description": "Extract raw text of page 35"
}
```


### [2026-09-04T18:38:45.921Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:38:48.908Z] TOOL CALL #63: Bash

```json
{
 "command": "which pdftotext pdftoppm mutool; python3 -c \"import fitz; print('pymupdf ok')\" 2>&1 | tail -1",
 "description": "Check pdf tools"
}
```


### [2026-09-04T18:38:50.765Z] TOOL RESULT

```
/usr/bin/pdftotext
/usr/bin/pdftoppm
/usr/bin/mutool
ModuleNotFoundError: No module named 'fitz'
```


## [2026-09-04T18:38:55.559Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -r 200 -f 35 -l 35 -png /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf p35 && ls -la p35*",
 "description": "Render page 35 to PNG"
}
```


### [2026-09-04T18:38:58.024Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 86486 Sep  4 14:38 p35-035.png
```


## [2026-09-04T18:39:00.280Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p35-035.png"
}
```


### [2026-09-04T18:39:00.841Z] TOOL RESULT

```

```


## [2026-09-04T18:39:00.838Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-04T18:39:11.457Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"tarö.azu\\|tara\\.azu\\|taraazu\\|tar>\\.azu\\|tarö\\.az\" BRT.txt | head; grep -n \"Wage'\" BRT.txt | head -5",
 "description": "Bartholomae tara.azu"
}
```


### [2026-09-04T18:39:11.525Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:39:15.037Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"tarö\\|tar3\\.\\|tar?\\.\" BRT.txt | head -10; echo \"---\"; grep -n \"Wagschale\\|Waage\\|Wage\" BRT.txt | head -8",
 "description": "Bartholomae balance"
}
```


### [2026-09-04T18:39:15.099Z] TOOL RESULT

```
2464:yat  baväma  aiwi.vanyn  dänavö  . .  ahmi gal'ie  piianähu  Yt.5.73;  —  ahmäi  J/ri- n?nti .  ./ravalayö  buyiil  ahmi  nmäne  giusia va^wa  ..  ". .  dem  . . ;  in  dessen  Hause  . ." V't.  jj-sif.;  Y..;j.6  (s.  2  2  aa);  —  auch bei  Beziehung  auf  das  Subjekt  des  Satzes: (ya^a)nar>m ..  asavamm*jas?nSfm  ahmya nmjne  .  .  paiti  taröpi^wim  dai'i^yät  "als ob  er  einen  Gläubigen,  der  in  sein  (zu ihm  ins)  Haus  kommt  .  ."  V.y.aa;  — naSca  ,  .  *hö  nl  ahmat  haca  gätaot  isaetci fraiütöip  nöit  apaiiitöit(%A.)'B.23.  b)  sub- stantivisch: adä  (sd.)  ta^a  guti  p>r9- sat  as>m  .  .  ahmäi  asä  (als  Subj.)  ,  ■  paitl.- mravat  Y.ag.ii.;  30.t,  46.8,  13;  —  uz- valoayat  zara^ustrS  annm  mainyUm  .  . paiti  ahmäi  adavata  .  .  aarS  mainyus  .  .
2477:y^  . .  möi  gas'^iä  dazdl  *amaiiklmit  akyä  \  myazdS  . .  äisy.ll  kl  anhe  ava{  mlid^m  A. maä%rilfrö^StY.46.Z\'—yatäröpaurvö^3.(il.;  — yastal  mihdgm  haiuftt? nöit däitX äire  . .  paitiJiaraiti  ahmäi  atars  ä/rJnat  .  .  kä  tsm  ahyä  *maeHis(sA.)  ar»hatY.44. V.1S.26;  YLIJ.51; — y ahmäi  xlnstö  ba-\  i^.  b)  .\Sn.,  f.  mit  Äaca  sva. 'dadurch': vaili  mi^rä  ahmäi  Jasaiti  avaiäke  YLIO.  yezi  mit  spä  ..  maeyevä  . .  pai'jyäite  ahmat 84;  87,  Y.GS.w*;  — yöi  nsil  ahm  main-  haca  irisyät  "sonst  konnte  der  Hund  in  . . yantä  aiibyö  dair?  (sd)  voka  as  manö  Y.  \  geraten,  dadurch  könnte  er  Schaden  neh- 34-&]  9.  2&  10,  45-ii  — yaisqm  ..  mazdä  \iata"  V,/_j.37;  —  ahmat  haca  /«>nj  (sd) ..  vatghö  vai'ja  alsqm  ..  Yt.i6.%; — ^J  sayiJ/A' Nik.  7;  *2; — yesi  tat  paiti  irisjati syao^anä  yä  vacatihä  yä  yasnJ  .  .  ae^qm  '  aiähal  hala  iyae>n!i7ar3za  (sd.)  .  ,  V./_?. töi..}hmä  pourutimäil  äasl?(sd.}Y.j4-^,''  38-  2)  vorausweisend;  i)  adjektivisch ■ —  yöi  *aite  . .  *gä'kä  nSit  *srävayänti  . .  I  auf  direkte  Rede  oder  Zitat:  vahiütsm  . . assqm  fyaohamm\ia'\  .  .  N, 25;  —  ySt  ..'igänii  ..  vir^zyat  öyä  (ISf.)  «>/f  (sd.):  hvö avatahabdgnti  (sd..)  /ramar?nl>m  (sd.)  ag-  *pt3  asahyä  mazdlY.4y.2;~aya  antar?.- £qm  nöit  aita^qm  ratufris  ..  N.52;  ^j\  uxti  (sd.) :  nöit  nS  mana  (usw.,  Y..^5.z) —  yahmät  kakmäicit  nalmaruim  vätS  ä'^rö  Y.ig.i$.  —  a)  mit  ergänzendem  Relativ: baoiolm  vibaraiti  (sd.)  ahmll  kahmäiHt  aya  aibigara  (LS.  als  Instr.)  aya  aibijary- nalmanqm..\.8.&o.  a)  Die  Beziehung  ta{d.^.)  yä  amfsanqm  sp^ntanqm..:  gave ist  ungenau:  ^yJ  räakaytn  (sd.)  sravaahä  rto5j/(usw.,Y._j5.4)  Vr.J2.i.  a)  substan- vahistät  iyadkanäl  mantärü  aeibyö  mazäi  tivisch  und  adjektivisch  auf  eine  erläuternde akä  (sd)  mraot  "qua  alienant  doc-  oder  ergänzende  nominale  Beifügung:  «7.5- trina  . .,  üs  .  ."  (statt  qui  ..  iis  ,  .)  Y.32.  yacä  i^agtuL  yäsat  ahyi  Virßzin3m..ahyä .. 1 2'*^  Anhang  zu  II  I  1,  2.     a)  An   ahurahya  uruasimai^A.)  mazda  Y.j2.i ;  2S.
2801:Irrlehrer,  der  . ."  \.g,$i{.;  —  yavat  °fa *gaintii  upankacaili  (sd.)  V.  7.  56;  — yavat  'sa  ilß  bySrixfi  (sd.)  .  ,  frabavai \.i4.\y,  — yavat  -lö  spä  anya{sA.) )asö V./5.48,  a)mitrelativischemAnschIuss: "jS  zT  asti  baslazyö.t3mö  .  .yal  *mahnm.- sppni»m.baei'azyd  (sd.)  V.  7.44;  —  '/a  bi~ paitisiana  (sd.)  y3  kaine  V.  75. 19;  19;  — vXsp»m  ä  ahmst.,  yat  -ia  yö  apsntinyBkB uxjasnf  (sd.)  "bis  es,  das  Kind  . ,"  V.  75. 15;  —  'sa  yS  *ar?mBiidd'a.W3.  2)  auf ein  Relativum  als  dessen  Korrelat,  sub- stantivisch: ci'at  dra)ö  avaMUlüt  '^a  yö näirikaya  . .  !^ar>^3tn  frabamt  V.  /J.  4 1 ; —  °sö  .  .  aitayä  vihrkayh  (sd.)  Jq'^-wS.' tarö  *at3kat  . .  ya^a  spä  vtkrkake  k»r?- naoiti  V.  y .  4 1 ;  — "/?  ratufris  *yö  jayara N.if};  24,  60;  —  'sa  yetjhe  apirinSyükö ^•9i  7;  —  °^'''  zaoiranqm  tnaziltaca  . . yiJ  *naire  asaone  *daste  N.^4.  III)  In
3370:gleichen, gleichfalls,  gleicherweise,  item': Aaomö  uxsyeiti  stavans  "ia  na  yö  dim staoili  nri^rajqstarö  bavaiti  "Ä.  wächst, wenn  er  gepriesen  wird;  desgleichen  wird der  Manu,  der  ihn  preist,  siegreicher"  Y. JO.6;  —  caili  nil  aSrahe  pasz'ö  (sd.)  *i "hra  barlti  catafirS .."'^a  dva  °~ia  %ryam
4828:mit  frS^''^  i)  'hervorgehen,  -Ireten': aiiihe  haxayB  fräyente  astva(.»r>take  Yt. ■'5-9SJ  — yü'ia  .,  hvanxsaet^m  tarasca harqtn..fraca  iii/i  aiwica  vazaite  ava^a  . . Yt  /0.118.  2)  'vorwärts,  weiter  gehen': fräyantö  tarö  pilüm  ..yim  cinvats  Vyt. 42.  a)  &oiysX  mA  ß-a^a: /rain /raysiii^ irUtim  uzbaröti  äpö  V.6.2T,  — /ra/a  fra- yaniu  n  maoö  (sA)  Y. /O.  14,  ig;  19;  — /rasa  /raya  (aSIA.)!'  vahisDm  a  ahüm binjayanti  (sd.)  ie  ..  V,  7.52;  —  vgl.  Inf. Jrayäi.  3)  'einhergehen'  iyio? paiti  mit Akk.):  yat  ÖS  paiii  ml  asava  frayaf^  .  . aismssastö  .  .  V.J.  i ;  —  äat  liama  yh paiti  frayat^^  tä paiii, .Yi.  lOjiJ).  4)  'be- gehen', mit  Akk.,  a)  einen  Weg:  kaf  tä pa>ä  (sd.)  Jrayqn^  pasvqm  vil  staorqm va  narqm  vä  Y.S.iy,  ii^23,  3.  15;  — likrava  paoirlm  aHa  pa%ä/rayanlu{s\.3Xl Sing.)  V.  Ä19.  b)  eine  Tat:  (aili  tä ^ao^aa  varsta  , .  fralta^''^  apati(a{&i.) anuzvars/a  . .  V.i^.i.
4954:•vat  ki'ari  utuiti  F.^b;  Yt /( 'vam  uiam  G-5.5;  —  haca  'vatbyS  stjnbyö aoi  sam  Yt5.85,  132  (wo  *°vd'J>yö);  — nihmacii  'vailqm  sfärqm  .  .  y.43.;  — hvan  °va  (IS.)  pai:a  .  .  ma  °va  pa^a  .  . starö  'va  pä^a  yHnti  Yt.  /j.  16;  —  "vaiti/ia niüs  "vaiiiha  pairikaya  pattistätayaSca  .  . Y.16.8;  —  Aaca  *'vaMitt  drujat  V.  J*?, 12;  —  "vai  tmidim  parS.ainli  aauAe "den  Lohn  dort  für  die  künftige  Welt" V.p.44;  —  ym  mä  hau  nä  °z-i
7024:ff(rai>/(Stverz.)  «^«röMasi/J  V.2, 1  f.,  usw.;'eines  koordiniiten  Satzes  an  das  Voraus- Y.p.z.s,  16,  7J.2,  V.j&ai,  H.  2.ii,Nik.  2, 1  gehende 'und';  die  zeitliche  Folge  tritt  min- yyt.8,22;  —  ä3tar3..kd  avalia..vl.l>arat..}'  dest  sehr  zurück;  a)  eines  Hauptsatzes:  tarn a°  aoxta  ahurö  mazdä  V.  2.42;  40,  Yt  5.  ^yatata  haofyauA^  .  ,  ä'  Alm  jaloyal  Yt. 9°>  95!  —  ahmäi  fradaisaSm  dainqm  .  .  ij.2^{.;  5.18,  5.17,  /j.40;  —  vagiipmnsm ä°  hl  mraont  .  .  visanha  mg  yima  .  .  ä'\  *apa  karsayjn  Jainis  .  .  ä°  tä  .  .  hazö ml  alm  paityaoxta  yimS  .  ,  ä"  h!  mraom  '  nivamay?n  (sd.)  Yt.  /5.80;  —  J  tat  han- .  .  ä'  mE  aem  paityaoxta  .  .  ä"  kl  saya  [jamarum  paiti.jasat .  .  ahurö  mazdä  .  .  ä° "       ■    "    "  ahurff  riazdfv.  2.21  f.;—  ,iat{s.  8}
7170:^fiti'"'Tir~  zL'^'"'  ""^  ""'  ^  '^'  ■"el"-|.  j.+ät9r»-tarö.naema-'>m. 'die  über  das
7178:•  j.  atar3.mar»zana-'>  m.  'Vorrichtung,  ^^hrieben  werden:  aat  hlnama /radai-:iyä das  Feuer  (von  der  Asche)  zu  re.nigen' :  j, j^_^^,^„  (,d.)  ya  .'.  -d^hyäm  v.l  .  .  V. ■«^  F.  7.  ^  /.Vgz
7261:ya().         b)   eines  Nebensatzes:  yöi  nmäna kam.barSfnahi  (sd.)  .  ,  ätrsmca  .  ,  W  pas- ciota  ahe  nmänake  spä  vä  nä  va  in%yäi iüia  .  .  "wenn  wir  . ,  und  es  stirbt  dann . ., wie..?"  V.5.39;  Vd./();   —  yS  itarö  .. mpaidyeinte    .  .    ä'    ae^am    naram    afvS irtiyat    cvat  ..  V.5.27.'         3)  'lur    An- knüpfung eines  adversativen  Satzes  'aber; sondern;  vielmehr;  gleichwohl':  i'äa  main- yäe  dus^artnä^  .  .  ä°  azitn  manya  Yt.  10. 105  c;  —   nöii  .  .  vjspa  yazatinhö  .  .  ä' ..  aevd  zarä^usürä  Yt.  ij.  ig;  5,  55  aSt^^ ti-S3<  V-io.S,  ig.  5;  —  iä  fravasayS  . . acjifta     h^nti    .  .    yi    .  .    saosyantqm    ä° ai^alsqm  Jravasayö  (sd.)    .  .    Yt.  1^,  17; N,  I02;  — -  nahänazdiStö  ä'  havatam (sd.)  N.  i^;  p,  6-];    —    äs    zaotars  (sd.) kairim  ar^hath.ä'  AävanänS  {vä.m\.  kairim auAat)  yal .  .  N.  ■J2;  yS—yO,  66';  —  apa. •  •  y^  pora  ahmat  hiit?nta  .  .  3*  W  nürqm fratoHnü  Yt.ij.53f.;  $6,  5S;  —  aai{%'.Z) yakmai  xstiüts  Öavaiti  mihrS  ahmäi  jasaiti avairiie  ü.'  yahmäi  ßistS  bavatH  . .  ahmäi frasciruiayeiti  nmätamca  ..  YL/0.87, yeiihe  x^akrä^ia  nsU  aoüin  änAa  . .  para tthmat  yat    , .    ä°  yal    . .    ",  .  bevor  . aber  als  .  ."  Yt./().33f.; — yaj  Ae pu%, usjaysi^e  .  .  ikalsB  anyS  .  .  ä°    anyS  .  . \.g.io;    —  tar5.d»nanB  (sd.,  näml.  urva- rayä  ar^han)  .  .   ä'   vp?ma  agis.drajaT3h& N.90;  —  navajcsaparim  ..  aiwi^äme  ä' hama  mäzdräjakim  V.J.  42;  N,  4Ö,  4~>5'i; —  nsil    ahmi  nmäne  *sanaile  ä%rava  . ä'  .  ,  sayänie  dahakäca  "nicht  werden  . geboren  - .,   sondern    es    sollen   geboren werden  . ."  Y.  //.  6 ;  —  hau  .  .  yO  .  .  varg- thfca  Aqm.rüzayeiti .  .  a'ia  dim  upa-taala^ ydii  . .  raesayacä  (sd.)  , .  ä°  yat  . .  van- iäsca    *hqm.räzayaaha   .  .   äat    (s.   7)    .  . fascaSa  apa.bardi!  ". .  vielmehr  wenn  du dir  die  Haare    ordnest  . .,   so  sollst  du dann  .  ."  V.iy.z-i,;    —    a%>m  vTspanqm damanqm    nipäta    ahmt    .  .    ä"    ('gleich- wohl') mä  nSil  masyäka  .  .  ya'^nte  Yt  10. 54.        a)  bes.  mit  a)  folgendem  _j'iii  oder ye:i,  ß)  vorausgehendem  yezi  "wenn  aber, wenn  jedoch",  kondiz.:  a)  *yujyaslil  haca *nmänät  .  ,  ä'  yal  h!  aoxte  .  .   d^a  *hil *xiayete  ..  haxtSii  (sd.)  N.<Vf.;  V.7.3; all  (s.  8)  yS  . .  upairi  hunanm  (sd.)  mc iarät  .  .  ä°  yat  .  .  paiti  barJt  äaj  (s.  2) yal  .  .  ara  baraite  "wer  .  .  aber  wenn  er ■ .  und   wenn   er   ■  ."   P.j7f.;
---
2034:und  an  Ursprünglichkeit  des  Lautbestands,  der  Formbezeichnung  und  der  Satz- fUgung  den  Hymnen  des  ^gveda  durchaus  die  Wage  halten,  stehen  Machwerke traurigster  Art  zur  Seite,  deren  Verfasser  auf  Schritt  und  Tritt  verraten,  dass  sie sich  einer  ihnen  fremden  —  weil  längst  abgestorbenen  —  Sprache  bedienen,  in der  sie  nur  ganz  stümperhafte  Kenntnisse  besitzen.  Als  Stücke  solcher  Art,  in deren  Benutzung  für  irgend  einen  Teil  der  Grammatik  dem  Sprachvergleicher  die grösste  Vorsicht  anempfohlen  sei,  bezeichne  ich  in  erster  Reihe:  Yt.  2,  j,  4,  Vyt,  Az,, Nik.,  Vd.,  FrW.  2,  8,  g,  FrB.,  FrD.  5,  6,  7,  FrG.,  FrBy.,  Sl.  8.  zz  Z.,  in  zweiter:  Yt. //,  12,  1$,  18,  V.  S2.  Auch  andern  alten  Teilen  sind  nicht  selten  minderwertige Zutaten  ein-  oder  angeßigt,  die  sich  zumeist  schon  durch  die  mangelhafte  Syntax deuthch  als  solche  zu  erkennen  geben;  z.  B.  in  Yt  /,  V.  10, 11,  13  usw.".
2949:ai.  uij'äti  'er  hält  nieder'.  —  i)  Närol.  anf  der Wage.  Es  handelt  sich  um  das  Abwägen  der Gut-  und  Übeltaten  beim  letzten  Gericht;  vgl. Bnn,.  ZDMG.  35.  157,  jo,  701,    Hörn  BB,
2952:•  j.  aom  Adv.  'dort',  mit  Gen.":  hUtaite a'  väiahe  miirahe  .  .  hasaanm  .  .  "es befinden  sich  dort  im  Wagen  des  M.  . . tausend  .  ."  Vt/o.  128;   129—132*,
3098:Komp.  mit  LS.  im  i.  Glied  0,  eig.  'des  Wagen an  der  Spitie  geht'.  —  ")  Vgl.  ai.  a^te',
5724:•  j-t  E-  (.  P-)  asan-iaj«-,  j.,  p.  asman-  m." i)  'Stein':  *ja«s(alsAP.)  äi/i{sd.)  maya  äiti darSii"V.g.  11;  —  'sSnaShia'^ ..  vtHiaeh-a' . .  tBiuxha  (sd.)  V,  6. 5 1,  a)  als  Amulet: °samm  *siyaire.ci^rim  (sd.)  abars  *aAurö.- puirS  (sd.)  Yl;4.59-  b)  als  Waffe, 'Schleuderstein,  Steingeschoss':  Uavasca  . . •sanas(a  . .  (NP.)  fraäaxlaitya  V.  Z7.9;  — karjtS  .  .  vazrö .  .  'sänS  atymSJütä  Yt.  JJ. 72;  /.18;  —  jainti  mqm  ahuna  vairya avavata  snai^isa  ya'^a  'sma  iatS.masa (sd.)  Yt/7.20;  —  'sanS  (als  AP.)  tasia drazimnS  katä-masatiks  Aynti  V,  117.43); —  yahmai  .  .  aurvan/a  *yuxta  vJsa %an/asante  (sd.)  .  .  asUnas/a  (als  AP.) vispeMvia  "dem  .  .  die  Renner  am  ge- schirrten Wagen   ziehen  -  .  und  die  all-
7811:•  j.  axna.h-  n, 'Zügel':  'nä  dralaite  välahe ".  .  hält  die  Züge!  des  Wagens"  Vt.  5. 1 1 .
9930:KompA.  —  fli.  gada-  f.,  mp.  gas  (geschr.  dt); s.  noch  Osthoff  Par.  143.  —  ")  Im  Gegens. va  vazra-,  womit  gehauen  wuide.  Vgl.  Vt 10.  131  f.,  wonach  sich  in  ;1/f%ras  Wagen  1000 gaiä-  belinden,  aber  nur  ^in  zaim-.  Anders Galt,  OK,  445 ,  der  auf  die  Grundbedealnng von  saina.  lu  viel  Gewicht  legi.
10465:hsm  casmainJ  (sd.)  hSngrabatn^''''  Y. _ji.8.  3)  'aufnehmen  (in  sich)': /ra/(7- rsmcit  . .  Aavartpm  (sd.)  .  .  yd  qsits  *Aan- gSuri'ayeie''*'^  Y.10.2.  4)  'in  seiner  Ge- walt haben,  halten',  sva.  'lenken',  den Wagen:  yeAke  viis»m  hangr^vnäiti  .  .  Yt. io.  68,  143.
```


## [2026-09-04T18:39:21.522Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\.azu\\|azu-\\|azu'\" BRT.txt | head -8",
 "description": "Bartholomae azu"
}
```


### [2026-09-04T18:39:21.573Z] TOOL RESULT

```
7063:;u  dem  Zwecke' sva, 'darum,  dazu':  yS  ä°
12197:•  j.  t9m  Adv.  'darum,  de^ialb,  dazu', znrtickweiseod:  raoxhom  k>r3navShi  dä- mahva  ttmat  uxTra  yai  ahi  garö  d^r^m (sd.)  "Licht  sollst  du  schaffen  .  .,  dazu geh  auf;  .  ."  V.27,5.
21077:setzen  sva.  zur  Verwendung  bringen':  yezt "Siris  *Aa^rän^S  yätayante . . yezi  äal  (^ris) nBii  *halir>'iiuff  yäiayanli  "wenn  sie  drei {Bansman-Zvitigt)  zugleich  zur  Verwen- dung bringen  .  ."  N.  tyii''';  —  yai  'irü *hairäkafibis  ''yiltayeinti  ,  .  yesi  äat  %ris nöit  [är/V]  *Aa^räkagiHs  yatayänti  N. t??'"'.  b)  'betreiben,  sich  befassen mit  — ,  sich  beöeissigen' :  tum  ts  datrihävi tiipahi  yi  hub>r>inm  yätayeiti  (statt  Plur.) mi%rahe  "du  schirmst  dann  die  iJinder, wenn  sie  sich  der  guten  Pflege  des  M. befleissigen"  Yt. /o.  78.  3)  3SPfA.  mit zurückweisendem  tai  (Sp.  616  u.)  'es  ist dazu  gekommen  sva.  man  hat  es  dazu gebracht,  es  reicht  dazu'"':  dätaca pas3us  *gjr>bu} . .  yai  tatyayata  navättat yayata  hurayäscit  .  ,  ".  ,  wenn  es  dazu reicht;  oder  aber,  wenn  es  nicht  dazu reicht,  .  ."  A..j.3">;  4*,  5".
22043:mit  frä  i)  'herausfinden  sva.  aus- erlesen': aßm  tsi  äis  *paouruyi  fravSividi (iSPrM.)'"'  "ich  ward  dazu'"  von  dir  zu Anfang  auserlesen"  Y.  44-ii.  2)  'er- langen': sps  dasta  nS  tftn  yänffn  y5  yüsmat Pars  fi-avistS  ".  .  den  Gunstbeweis,  wie er  früher  von  euch  erlangt  ward"  Y. 68.21.  a.)  Kaus.  'erlangen  lassen,  teil- haftig machen';  zardkusfrahe  .  .  paoiryai ß-ava^äi  (sd.)  ,  .  fraval}tQyamnäi  .  . gamcä  ahmla  .  .  Yt  r?.  88.
```


## [2026-09-04T18:39:24.986Z] AGENT

Now I'll write the verification file.


## [2026-09-04T18:45:00.908Z] TOOL CALL #69: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk35.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PIE   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82e%C7%B5-\"\nW_TARAZU= \"https://en.wiktionary.org/wiki/%D8%AA%D8%B1%D8%A7%D8%B2%D9%88\"\nW_TIRAZ = \"https://en.wiktionary.org/wiki/%D8%B7%D8%B1%D8%A7%D8%B2\"\nE_STRAT = \"https://www.etymonline.com/word/strategy\"\nW_ADAMS = \"https://en.wiktionary.org/wiki/%D8%A2%D8%AF%D8%A7%D9%85%D8%B3\"\nE_ADAM  = \"https://www.etymonline.com/word/Adam\"\nW_ADAM  = \"https://en.wiktionary.org/wiki/%D8%A2%D8%AF%D9%85\"\nE_AGENT = \"https://www.etymonline.com/word/agent\"\nW_ADAMAH= \"https://en.wiktionary.org/wiki/%D7%90%D7%93%D7%9E%D7%94\"\nE_AMB   = \"https://www.etymonline.com/word/ambassador\"\n\nKLN21 = (\"KLN_1966.txt \\\\f-leaf 22 (= printed pp. 20-21, running heads 'adamant | 20' / \"\n         \"'adamantean | adept') s.v. 'Adam': \\\"Heb. Adam, lit. 'man', usually with the def. art., \"\n         \"ha-adam, 'the man', prop. 'the one formed from adamah (i.e. the ground)'. See Gen. 2:7 ... \"\n         \"For the connection between Heb. adamah, 'ground, earth', and adam, 'man', cp. L. homo, \"\n         \"'man', humanus, 'human', which are rel. to humus, 'earth, ground, soil'.\\\"\")\n\nKLN37 = (\"KLN_1966.txt \\\\f-leaf 31 (the printed numeral '37' stands in the middle of the leaf) \"\n         \"s.v. 'agent, adj.': I.-E. base *ag-, 'to drive, lead', whence Gk. agein, 'to lead', \"\n         \"'OI. ajati, \\\"drives\\\", ajirah, \\\"moving, active\\\", Avestic aza'ti [= azaiti], \\\"drives\\\", \"\n         \"Toch. A ak-, B ak-, \\\"to travel, lead\\\", Arm. acem, ON. aka'; the 'Cp.' list runs \"\n         \"'acorn, acre, act, ... agenda, agile, agitate, -agogue, agony, agrarian, agriculture, \"\n         \"agro-, ... aisle, ala, ambages, ambassador, ... axilla, axiom, axis, axle, ... embassy, \"\n         \"exact, examen, exigent, ... navigate, ... strategy, synagogue, transact'.\")\n\nPOK4 = (\"POK_01.txt \\\\f-leaf 13 = printed p. 4 (leaf = p + 8): headword \\\"ag-  ,treiben' \"\n        \"(eigentlich wohl ,mit geschwungenen Armen treiben'), ,schwingen', in Bewegung setzen, \"\n        \"fuehren\\\"; \\\"ago: ai. ajati ,treibt', av. azaiti ,treibt, fuehrt weg'\\\"; and at the foot of \"\n        \"the same page \\\"Als idg. Instrumentalnomen auf -tra hierher ai. astra ,Stachel zum \"\n        \"Viehantreiben', av. astra ,Peitsche, Geissel'\\\". p. 6 of the same article has \"\n        \"\\\"ag-ro-s ,Feld, Flur' (zu *ago wie Triften treiben, also urspruenglich ,Ort, wo das Vieh \"\n        \"hinausgetrieben wird, Weide')\\\" and \\\"av. asaya Gen. Du. ,der beiden Achseln'\\\".\")\n\ndata = {\n \"pdf_page\": 35,\n \"book_page\": 5,\n \"verified_by\": \"claude-fable-5-1\",\n \"verified_on\": \"2026-09-04\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Âdhâmah\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Biblical Hebrew אֲדָמָה ʾăḏāmāh 'ground, earth, (red) soil', from the Semitic root ʾ-d-m (cf. אָדֹם ʾāḏōm 'red')\",\n   \"note\": (\"The root box is right in every part: the language label (Hebrew), the form and the gloss. \"\n            \"Klein's article on 'Adam' (KLN:21, the page Nourai cites) is in fact the source of essentially \"\n            \"the whole chart, including the Latin homo : humus parallel. Two structural problems in the tree, \"\n            \"both about the ROUTE rather than the ultimate origin: (a) node #3 [Latin] is drawn as a child of \"\n            \"the Arabic node, i.e. Latin Adam is made a loan from Arabic — chronologically impossible; Latin \"\n            \"Adam comes from the Greek Ἀδάμ of the Septuagint/NT and the Vulgate, itself straight from Hebrew, \"\n            \"some four centuries before Arabic Ādam is attested. (b) node #6 [Persian] آدم is drawn straight \"\n            \"from Hebrew, but Persian took it from Arabic آدم after the conquest (Wiktionary: 'Borrowed from \"\n            \"Arabic آدَم (ʔādam), borrowed from Biblical Hebrew אָדָם'), which is exactly the Arabic node #2 \"\n            \"already on the chart. The 'Adams > آدامس' branch, which looks like a joke, is genuine: Persian \"\n            \"آدامس is the brand name of Thomas Adams' New York chewing gum. Checked against the 200-dpi render \"\n            \"of pdf page 35: the JSON reproduces the printed boxes faithfully, so nothing here is an \"\n            \"extraction error.\"),\n   \"sources\": [E_ADAM, W_ADAM, W_ADAMAH],\n   \"ref_check\": [\n     {\"ref\": \"KLN:21\", \"status\": \"supports\", \"note\": KLN21},\n     {\"ref\": \"AHD:14\", \"status\": \"not_checked\",\n      \"note\": (\"Nourai's AHD page numbers below 1500 are pages of the main dictionary text of the 1975/76 \"\n               \"American Heritage Dictionary, New College Edition, which is not open online; p. 14 falls in \"\n               \"the 'ad-' range, so the entry 'Adam' is the plausible target. The local AHD file \"\n               \"(AHD_watkins1985.txt) is only Watkins' Indo-European Roots appendix and has no Semitic \"\n               \"material; its root dhghem- 'earth' does carry the same Latin homo/humus/'earthling' idea \"\n               \"Klein invokes for adam : adamah.\")}\n   ],\n   \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"leaf 22 = p. 21 s.v. Adam\", \"stance\": \"supports\",\n      \"note\": \"\\\"prop. 'the one formed from adamah (i.e. the ground)'\\\" — Klein states the root box exactly.\"},\n     {\"src\": \"Etymonline\", \"where\": \"entry 'Adam'\", \"stance\": \"supports\",\n      \"note\": \"\\\"from Hebrew adam 'man', literally '(the one formed from the) ground' (Hebrew adamah 'ground')\\\".\"},\n     {\"src\": \"Wiktionary\", \"where\": \"אדמה\", \"stance\": \"partial\",\n      \"note\": \"Gives אֲדָמָה as a feminine noun 'earth, soil, land' under the Semitic root א־ד־ם, but the page does not itself spell out the adam : adamah : adom link.\"}\n   ],\n   \"nodes\": [\n    {\"id\": 1, \"lang\": \"Hebrew\", \"words\": \"Âdam, Âdâm\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Biblical Hebrew אָדָם ʾāḏām 'man, mankind', normally with the article הָאָדָם hā-ʾāḏām \"\n                    \"'the man', is the same ʾ-d-m root as אֲדָמָה ʾăḏāmāh 'ground'; the etymology is given \"\n                    \"inside the text itself at Gen. 2:7, wa-yyīṣer YHWH ʾĕlōhīm ʾeṯ-hā-ʾāḏām ʿāp̄ār min-hā-\"\n                    \"ʾăḏāmāh 'the LORD God formed the man of dust from the ground'. The colour sense 'red' \"\n                    \"(ʾāḏōm 'red', dām 'blood') belongs to the same root and gives the 'red soil' of Nourai's \"\n                    \"gloss. The pattern is exactly the Latin homo : humus one that Klein and Watkins cite for \"\n                    \"PIE *dʰǵʰem- 'earth' > *(dʰ)ǵʰm-on- 'earthling'.\"),\n     \"sources\": [E_ADAM, W_ADAM],\n     \"ref_check\": [{\"ref\": \"KLN:21\", \"status\": \"supports\", \"note\": KLN21}],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"leaf 22 = p. 21 s.v. Adam\", \"stance\": \"supports\",\n        \"note\": \"\\\"Heb. Adam, lit. 'man' ... prop. 'the one formed from adamah (i.e. the ground)'.\\\"\"},\n       {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt leaf 69 = printed p. 51 (printed = leaf − 17)\", \"stance\": \"supports\",\n        \"note\": \"Jeffery, closing the article آدم: \\\"The origin of course is the Heb. אדם, and there is no reason why the name should not have come directly from the Jews.\\\"\"},\n       {\"src\": \"Etymonline\", \"where\": \"entry 'Adam'\", \"stance\": \"supports\",\n        \"note\": \"Same derivation, plus the note that Hebrew adam is 'man' in the generic sense.\"}\n     ]},\n\n    {\"id\": 2, \"lang\": \"Arabic\", \"words\": \"Âdam\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Arabic آدَم ʾĀdam is a religious-register borrowing of Hebrew אָדָם, reaching Arabia \"\n                    \"before Islam: Jeffery notes that the name 'occurs in the Safaitic inscriptions' and 'was \"\n                    \"known to the poet ʿAdī b. Zayd', so it was familiar to Muhammad's contemporaries along \"\n                    \"with the creation story; it then entered the Qurʾān (II.29-35, III.30, VII.10-33 etc.). \"\n                    \"Phonetically the Hebrew qāmeṣ-ʾālep̄ was rendered with madda, ʾā-, giving آدم; unlike \"\n                    \"Hebrew it is only ever a personal name in Arabic, never 'man' in general. Early Arab \"\n                    \"philologists (al-Jawālīqī, Muʿarrab 8) tried to make it native, but al-Zamakhsharī and \"\n                    \"al-Bayḍāwī on II.29 already 'admit that it is a foreign word'.\"),\n     \"sources\": [W_ADAM],\n     \"ref_check\": [\n       {\"ref\": \"FVQ:51\", \"status\": \"supports\",\n        \"note\": (\"FVQ_pages.txt leaf 68-69 = printed pp. 50-51 (printed = leaf − 17), article \\\"آدم (Adam)\\\": \"\n                 \"\\\"It is used always as an individual name and never as the Heb. and Phoen. אדם for man in \"\n                 \"general ... There are various theories as to the derivation of the name ... but all of them \"\n                 \"are quite hopeless ... Zam. and Baid., on ii, 29, admit that it is a foreign word\\\", and on \"\n                 \"p. 51 \\\"The origin of course is the Heb. אדם, and there is no reason why the name should not \"\n                 \"have come directly from the Jews, though there was a tradition that the word came from \"\n                 \"Syriac.\\\" This is precisely Nourai's Hebrew → Arabic arrow.\")},\n       {\"ref\": \"VDQ:106\", \"status\": \"not_checked\",\n        \"note\": (\"VDQ = Badreh'i's Persian translation of Jeffery's FVQ (Toos, Tehran 1372/1993). \"\n                 \"refs_online.json lists it only as a noorlib page-image viewer \"\n                 \"(noorlib.ir/book/view/12868), which is JavaScript-driven and not fetchable; there is no \"\n                 \"local copy. Since VDQ is a translation of FVQ, the checked FVQ:51 covers the same claim.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"FVQ\", \"where\": \"pp. 50-51 s.v. آدم\", \"stance\": \"supports\", \"note\": \"See ref_check: 'The origin of course is the Heb. אדם'.\"},\n       {\"src\": \"Wiktionary\", \"where\": \"آدم, Arabic section\", \"stance\": \"supports\",\n        \"note\": \"\\\"Terminology of the religious sphere borrowed from Hebrew אָדָם (āḏā́m, 'man, person').\\\"\"},\n       {\"src\": \"KLN\", \"where\": \"leaf 22 = p. 21\", \"stance\": \"silent\",\n        \"note\": \"Klein treats only the Hebrew and English sides of the name; he says nothing about Arabic آدم.\"}\n     ]},\n\n    {\"id\": 3, \"lang\": \"Latin\", \"words\": \"\",\n     \"verdict\": \"disputed\",\n     \"derivation\": (\"An empty pass-through box: Latin Adam, the indeclinable biblical name. The word itself \"\n                    \"is real — it is the form of the Vulgate (Gen. 2-5, Rom. 5:14) — but the arrow drawn into \"\n                    \"it is wrong. Latin got the name from the Greek Ἀδάμ of the Septuagint (3rd-2nd c. BCE) \"\n                    \"and of the New Testament, which transliterated Hebrew אָדָם directly; the Vetus Latina \"\n                    \"and then Jerome (c. 400 CE) simply kept the Greek spelling. Arabic آدَم, Nourai's drawn \"\n                    \"parent, is first attested in the Safaitic/pre-Islamic period and became a written \"\n                    \"language word only in the 7th c. CE, i.e. centuries after Latin Adam was in use, and no \"\n                    \"modern authority routes any European form of the name through Arabic. The correct chain \"\n                    \"is Hebrew (#1) → Greek Ἀδάμ → Latin Adam → English.\"),\n     \"sources\": [E_ADAM, W_ADAM],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box; there is nothing to check.\"}],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"leaf 22 = p. 21 s.v. Adam\", \"stance\": \"contradicts\",\n        \"note\": \"Klein derives English Adam straight from 'Heb. Adam' with no Arabic and no Latin intermediary in the etymology line.\"},\n       {\"src\": \"Etymonline\", \"where\": \"entry 'Adam'\", \"stance\": \"contradicts\",\n        \"note\": \"\\\"masc. proper name, in Old Testament the name of the first man, from Hebrew adam 'man'\\\" — again no Arabic link.\"},\n       {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt, 'Adam's ale / Adam's apple / Adam's needle' group\", \"stance\": \"silent\",\n        \"note\": \"Webster lists the English Adam- compounds but gives no transmission route, so it neither supports nor refutes the Arabic → Latin arrow.\"}\n     ]},\n\n    {\"id\": 4, \"lang\": \"English\", \"words\": \"Adam; Adams\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"English Adam is the biblical name taken over unchanged from Latin/Greek Adam (so the \"\n                    \"Latin → English arrow itself is right; it is the Arabic → Latin arrow above it that \"\n                    \"fails). Adams is the ordinary English patronymic surname, Middle English Adam + genitival \"\n                    \"-s 'son of Adam' (beside Adamson, Adkins, Adcock from the pet form Ad(d)y); Klein records \"\n                    \"the same name-stock on this page (Adamite, adamite 'named after the mineralogist M. \"\n                    \"Adam'). Nourai's NOTE 'Name of a gum manufacturer' is correct and is the point of the \"\n                    \"branch: Thomas Adams (1818-1905) of New York, who from 1869-71 turned Mexican chicle \"\n                    \"into 'Adams New York Gum', the first mass-marketed chewing gum.\"),\n     \"sources\": [E_ADAM, W_ADAMS],\n     \"ref_check\": [\n       {\"ref\": \"KLN:21\", \"status\": \"partial\",\n        \"note\": (\"KLN_1966.txt leaf 22 = p. 21 gives 'Adam' (from Heb. Adam), 'Adam-ite', 'adamite ... named \"\n                 \"after the mineralogist M. Adam' and 'Adam's apple', so the page supports the English name; \"\n                 \"it says nothing about the surname Adams or about the gum manufacturer, and it derives the \"\n                 \"English name from Hebrew, not from Arabic via Latin.\")},\n       {\"ref\": \"AHD:14\", \"status\": \"not_checked\",\n        \"note\": \"1975/76 AHD main-dictionary page, not open online (see the root-level ref_check); only Watkins' root appendix is on disk.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"leaf 22 = p. 21\", \"stance\": \"partial\", \"note\": \"Has Adam, Adamite, adamite, Adam's apple; no 'Adams'.\"},\n       {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt lines 7220-7261, 'Ad'am-and-Eve', 'Adam's ale', 'Ad'am-ite'\", \"stance\": \"partial\",\n        \"note\": \"Funk & Wagnalls has the Adam- word family ('Adam's ale [Colloq.], water'), but no surname or gum entry.\"},\n       {\"src\": \"Etymonline\", \"where\": \"entry 'Adam'\", \"stance\": \"supports\",\n        \"note\": \"\\\"The Middle English pet form was Addy, whence surnames Addison, Adkin(s), Adcock\\\" — the same name-stock the surname Adams belongs to.\"}\n     ]},\n\n    {\"id\": 5, \"lang\": \"Persian\", \"words\": \"âdâms «آدامس»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian آدامس ādāms 'chewing gum' is a genericised trademark: the Adams Chewing Gum \"\n                    \"Company's product reached Iran in the first half of the 20th century and the brand name \"\n                    \"on the packet became the common noun, exactly as ژیلت for a razor or ریمل for mascara. \"\n                    \"Wiktionary: 'Borrowed from English Adams, a historical American brand of chewing-gum, \"\n                    \"named after its inventor Thomas Adams.' The Persian form keeps the English stress-pattern \"\n                    \"and adds no ending; final -s is simply the English genitival -s of the surname. So the \"\n                    \"surname → Persian noun step is right, and it is the only link on this branch that no one \"\n                    \"disputes.\"),\n     \"sources\": [W_ADAMS],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai cites no reference for this box.\"}],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"grep 'آدامس' in MON_part1.txt / MON_part2.txt\", \"stance\": \"silent\",\n        \"note\": \"Not a single hit: Mo'in's Farhang-e Farsi (1963) does not carry the word, which is unsurprising for a mid-century trade name.\"},\n       {\"src\": \"BQT\", \"where\": \"grep 'آدامس' in BQT_v1_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"No hit; Borhan-e Qateʿ is a 17th-c. dictionary and could not have it.\"},\n       {\"src\": \"Wiktionary\", \"where\": \"آدامس\", \"stance\": \"supports\",\n        \"note\": \"\\\"Borrowed from English Adams, a historical American brand of chewing-gum, named after its inventor Thomas Adams.\\\"\"}\n     ]},\n\n    {\"id\": 6, \"lang\": \"Persian\", \"words\": \"Âdam «آدم» (extra: آدمک ، آدمیزاد)\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"Persian آدم ādam 'Adam; man, human being' is genuinely of Hebrew origin, so Nourai's box \"\n                    \"is substantively right, but the arrow skips a link: Persian borrowed the word from \"\n                    \"Arabic آدَم after the Islamic conquest, not from Hebrew directly — Wiktionary states \"\n                    \"'Borrowed from Arabic آدَم (ʔādam), borrowed from Biblical Hebrew אָדָם (āḏā́m), from \"\n                    \"Proto-Semitic *ʔadam-', and the Arabic node #2 is already drawn one box above. The \"\n                    \"Arabic-mediated route explains the meaning: in Persian, as in Qurʾānic Arabic, آدم is \"\n                    \"both the proper name and (unlike Classical Arabic) a common noun 'person', whence the \"\n                    \"diminutive آدمک ādamak 'little man, puppet, figurine' with the Persian diminutive suffix \"\n                    \"-ak, and آدمیزاد ādamīzād 'human being, lit. Adam-born' with the Persian nisba -ī plus \"\n                    \"زاد zād 'born' (< MP zād, past stem of zādan) — both hybrid Arabic-stem + Persian-affix \"\n                    \"formations that can only have been made after the word was already naturalised in \"\n                    \"Persian. The Ḥāfeẓ line quoted in the box (آدمی در عالم خاکی نمی‌آید به دست) plays on \"\n                    \"exactly the ādam 'man' / خاکی 'of earth' pair that motivates the Hebrew etymology.\"),\n     \"sources\": [W_ADAM],\n     \"ref_check\": [\n       {\"ref\": \"MON5:12\", \"status\": \"not_checked\",\n        \"note\": (\"Moʿin vol. 5 = the first aʿlām (proper names) volume; p. 12 is where آدم would fall \"\n                 \"alphabetically, so the citation is entirely plausible, but only Moʿin's lexicon volumes \"\n                 \"(1-3) are on disk as MON_part1/part2 — the aʿlām volumes are not, and vajehyab/abadis serve \"\n                 \"the lexicon text only. Grepping آدم in the local Moʿin text returns 100+ hits in the \"\n                 \"lexicon volumes (آدم، آدمک، آدمیزاد are all lemmatised there), which corroborates the word \"\n                 \"but not the cited page.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_part2.txt, grep آدم (100 + 62 hits)\", \"stance\": \"partial\",\n        \"note\": \"Moʿin's lexicon carries آدم and its derivatives, but the accessible volumes give no etymological footnote for it.\"},\n       {\"src\": \"Wiktionary\", \"where\": \"آدم, Persian section\", \"stance\": \"partial\",\n        \"note\": \"\\\"Borrowed from Arabic آدَم (ʔādam), borrowed from Biblical Hebrew אָדָם\\\" — same ultimate source as Nourai, but one link (Arabic) that his arrow bypasses.\"},\n       {\"src\": \"FVQ\", \"where\": \"pp. 50-51\", \"stance\": \"supports\",\n        \"note\": \"Establishes the Arabic stage that Persian must have gone through: the name was current in Arabic, in the Qurʾān, before Persian could take it.\"}\n     ]}\n   ]\n  },\n\n  {\n   \"entry\": 1,\n   \"root\": \"Ag, Agros\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₂eǵ- 'to drive, lead' (Pokorny aǵ- 4), with the derivative *h₂éǵ-ro- 'field, pasturage'\",\n   \"note\": (\"Root box, language label and both glosses are exactly Pokorny's, and Nourai's page number is \"\n            \"right on the nose: IEW p. 4 opens \\\"aǵ- ,treiben' ... ,schwingen', in Bewegung setzen, führen\\\", \"\n            \"and p. 6 of the same article has \\\"aǵ-ro-s ,Feld, Flur' (zu *aǵō wie Triften treiben, also \"\n            \"ursprünglich ,Ort, wo das Vieh hinausgetrieben wird, Weide')\\\" — i.e. literally Nourai's \"\n            \"'pasture (where cattle is driven)'. In laryngeal notation the root is *h₂eǵ-. The chart is \"\n            \"unusually accurate; the reservations are all local. (a) In node #3 'ajras' is Sanskrit ájra-, \"\n            \"not Avestan — Pokorny lists it as 'Ai.' (Altindisch); the two other words in that box, aštrā- \"\n            \"and ašaya, are Avestan. (b) 'ašaya : of both wings?' is Bartholomae's/Pokorny's genitive dual \"\n            \"'der beiden Achseln' ('of the two shoulders'), the 'wing' sense belonging to Latin āla < *aksla. \"\n            \"(c) 'ambractus' in node #11 is a misprint in the book (confirmed on the 200-dpi render of pdf \"\n            \"p. 35, so not an extraction error) for ambactus, which is moreover Gaulish/Celtic, borrowed \"\n            \"into Latin. (d) Watkins/AHD splits the 'axle, axis, āla' material off as a separate root aks-, \"\n            \"though he flags it '[In Pok. ag- 4]', so Nourai's grouping follows Pokorny, not AHD. \"\n            \"The Iranian branch — Av. az-/azaiti, tara.azu > MP tarāzūg > NP tarāzū — is the strongest part \"\n            \"of the chart and is independently confirmed by Asbaghi, Moʿin's footnote in Borhān-e Qāṭeʿ and \"\n            \"Wiktionary.\"),\n   \"sources\": [W_PIE, W_TARAZU],\n   \"ref_check\": [{\"ref\": \"POK:4\", \"status\": \"supports\", \"note\": POK4}],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"POK_01.txt leaf 13-15 = printed pp. 4-6\", \"stance\": \"supports\", \"note\": POK4},\n     {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. 'ag-' and 'agro-'\", \"stance\": \"supports\",\n      \"note\": \"\\\"ag-. To drive. 1. Latin agere ... 2. Greek agein, to drive, lead ... [Pok. ag- 4]\\\"; \\\"agro-. Field. Derivative of ag-, 'to drive' (< 'place to which cattle are driven'). [In Pok. ag- 4.]\\\" — the same two-part root box Nourai draws.\"},\n     {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 35 ff. (the pre-1959 version of the same article, referenced by Pokorny's own 'WP. I 35' back-references)\", \"stance\": \"supports\",\n      \"note\": \"Pokorny's IEW article is the revision of Walde-Pokorny I; the local WLD volumes are Bd. 1-3 with heavy OCR noise and the aǵ- article could not be located by grep, so the support is indirect, through Pokorny's own citation.\"},\n     {\"src\": \"KLN\", \"where\": \"leaf 31 = p. 37 s.v. agent, adj.\", \"stance\": \"supports\",\n      \"note\": \"\\\"I.-E. base *ag-, 'to drive, lead'\\\" with the Avestan, Sanskrit, Greek, Latin, Armenian, Tocharian and Norse cognates.\"}\n   ],\n   \"nodes\": [\n    {\"id\": 1, \"lang\": \"Avestan\", \"words\": \"az; azaiti; tara-âz, tara-âzu\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Avestan az- 'to drive, lead' is the plain thematic present of PIE *h₂eǵ-: 3sg. YAv. \"\n                    \"azaiti (Yt 10.38 etc.), exactly matching Skt. ájati and Gk. ἄγει, Lat. agit. Cheung \"\n                    \"reconstructs Proto-Iranian *Haz 'to drive, lead' for it. The compound tara.azu- is \"\n                    \"'that which drives/carries across' — tarō/tara- 'across, beyond' (PIE *terh₂-, cf. Skt. \"\n                    \"tiráḥ, Lat. trāns) + the -u- stem of az-, i.e. the beam that swings the load over: hence \"\n                    \"'balance, scales'. Nourai's gloss 'balance driver, scale' is a literal rendering of that \"\n                    \"compound. It is this word, not the simple verb, that carries the Persian branch: \"\n                    \"Av. tara.azu > MP tarāzūg > NP tarāzū.\"),\n     \"sources\": [W_PIE, W_TARAZU],\n     \"ref_check\": [\n       {\"ref\": \"POK:4\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 13 = p. 4: \\\"agō: ai. ajati ,treibt', av. azaiti ,treibt, führt weg', arm. acem ,führe, bringe'; gr. ἄγω ,führe', lat. agō ,treibe, führe'\\\" — Nourai's az/azaiti verbatim.\"},\n       {\"ref\": \"KLN:37\", \"status\": \"supports\", \"note\": KLN37 + \" Klein's cognate list explicitly includes \\\"Avestic aza'ti, 'drives'\\\".\"},\n       {\"ref\": \"PLA:194\", \"status\": \"supports\",\n        \"note\": (\"PLA_pages.txt leaf 209 = printed p. 194 (printed = 1-based leaf − 15), running heads \"\n                 \"'tabaristān | ṭirāzdārān'. Under طرازداران ṭirāzdārān Asbaghi writes: \\\"'Futteral der \"\n                 \"Waage' pers. ترازودران tarāzudārān, mp. tarāzūk 'Balance, Gleichgewicht', air. *tarāz- = \"\n                 \"skr. tulā + aw. az 'zugeben' [read: 'ziehen/treiben'], tk. terazi, serb., kl.russ. \"\n                 \"terezy.\\\" Asbaghi thus derives the whole tarāzū family from Avestan az-, which is exactly \"\n                 \"Nourai's arrow.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"BRT.txt, grep for 'tarō.azu' / '.azu'\", \"stance\": \"not_found\",\n        \"note\": \"Bartholomae's AiW does have the compound, but the OCR of this copy is too corrupt to locate it by grep (all diacritics are mangled); BRT is however clear on the base verb and on aštrā- (see node #3).\"},\n       {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt lines 11797 ff., s.v. *Haz\", \"stance\": \"supports\",\n        \"note\": \"\\\"*Haz 'to drive, lead'. AVESTAN: az- 'to lead' ... Pres. them.: IND. 3sg. YAv. azaiti\\\" — the Proto-Iranian etymon of Nourai's az/azaiti. Cheung's New-Iranian list does not, however, include tarāzū.\"},\n       {\"src\": \"PLA\", \"where\": \"p. 194\", \"stance\": \"supports\", \"note\": \"See ref_check: 'mp. tarāzūk ... aw. az'.\"},\n       {\"src\": \"Wiktionary\", \"where\": \"ترازو\", \"stance\": \"supports\",\n        \"note\": \"Middle Persian tlʾcwk' /tarāzūg/ 'borrowed from Avestan 𐬙𐬀𐬭𐬀.𐬀𐬰𐬎 (tara.azu)' — Nourai's tara-âzu is a real, cited Avestan lemma.\"}\n     ]},\n\n    {\"id\": 2, \"lang\": \"Persian\", \"words\": \"tarâz «تراز ، طراز»; tarâzu «ترازو»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Avestan tara.azu- 'balance' gave Middle Persian tarāzūg (Book Pahlavi tlʾcwk'), with the \"\n                    \"regular MP -ūg suffix on the -u- stem; loss of the final -g in the 9th-10th c. gives \"\n                    \"New Persian ترازو tarāzū 'balance, scales'. The shorter تراز tarāz is the same stem \"\n                    \"without the -ū(g), used for 'level, evenness, plumb' and hence 'well-proportioned, \"\n                    \"well-shaped' — Moʿin lists تراز as a builder's tool, 'آلتی است که به توسط آن پستی و \"\n                    \"بلندی سطحی را معلوم کنند' ('an instrument by which the unevenness of a surface is \"\n                    \"determined'). The second spelling طراز in Nourai's box is the Arabic re-spelling: \"\n                    \"Persian tarāz was borrowed into Arabic as ṭirāz with emphatic ṭ (Arabic having no \"\n                    \"native /t/ + /r/ + long ā pattern for this word), in the sense 'embroidered border, \"\n                    \"ornamental band, the royal-workshop textile', and came back into Persian in that \"\n                    \"spelling; Moʿin marks his تراز 3 as '[= طراز، معرّب]', i.e. explicitly an Arabicised \"\n                    \"doublet. The word travelled on from Persian to Ottoman Turkish terazi and thence to \"\n                    \"Serbian teresije, Ukrainian terezy, Russian tereza, Romanian terezie.\"),\n     \"sources\": [W_TARAZU, W_TIRAZ],\n     \"ref_check\": [\n       {\"ref\": \"BQT:480\", \"status\": \"supports\",\n        \"note\": (\"BQT_v1_pages.txt leaf 706 = printed p. 480 (the preceding leaf carries the continuation \"\n                 \"note 'بقیه از صفحهٔ ۴۷۸'). The entry ترازو is there, and Moʿin's etymological footnote 1 \"\n                 \"reads: 'پهلوی tarāzūk، ایرانی باستان *tarāzu-… از سانسکریت tulā… از aj سانسکریت \"\n                 \"(راهنمایی کردن، راندن، پیش‌بردن)' — 'Pahlavi tarāzūk, Old Iranian *tarāzu-, cf. Sanskrit \"\n                 \"tulā, from Sanskrit aj- (to lead, to drive, to push forward)'. That is Nourai's arrow, \"\n                 \"root and all.\")},\n       {\"ref\": \"PLA:194\", \"status\": \"supports\",\n        \"note\": \"PLA_pages.txt leaf 209 = p. 194: \\\"طراز ṭirāz: 'Stickerei, Rand, Saum' pers. طراز tarāz bzw. تراز taraz\\\" and, under ṭirāzdārān, \\\"mp. tarāzūk 'Balance, Gleichgewicht' ... aw. az\\\". Asbaghi confirms both the تراز/طراز identity and the Avestan az- etymology.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"vol. 1 leaf 706 = p. 480, s.v. ترازو with Moʿin's footnote\", \"stance\": \"supports\", \"note\": \"See ref_check — 'پهلوی tarāzūk، ایرانی باستان *tarāzu-'.\"},\n       {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 39504-39549: four homographs تراز plus ترازو\", \"stance\": \"supports\",\n        \"note\": \"تراز 4 '(بنا، معم.) آلتی است که به توسط آن پستی و بلندی سطحی را معلوم کنند' = Nourai's 'level'; تراز 3 '[= طراز، معرّب] ریشت، آرایش، نقش و نگار پارچه، زردوزی پارچه' = the Arabicised ornament sense; ترازو '(فز.) آلتی که …' = 'balance'.\"},\n       {\"src\": \"HRN\", \"where\": \"grep 'tarâz', 'razu' in HRN.txt\", \"stance\": \"silent\",\n        \"note\": \"Horn's Grundriss has no article on tarāzū under any of the spellings tried (tarâzû, tarazu, taraz); the only 'razu' hit is aw. razura-, unrelated.\"},\n       {\"src\": \"HUB\", \"where\": \"grep 'tarâz', 'tirâz', 'razu' in HUB.txt\", \"stance\": \"silent\", \"note\": \"No hit; Hübschmann's Persische Studien does not treat the word.\"},\n       {\"src\": \"LKT\", \"where\": \"LKT.txt no. 2029\", \"stance\": \"supports\",\n        \"note\": \"\\\"2029. Pers. tārāzū: 'Wage', tk. ebenso terazi; hieraus serb. teresije, klruss. terezy, russ. tereza 'Waage'; rum. tirizie, terezie 'Wagschale'.\\\" Lokotsch confirms Persian as the source but says nothing about the Avestan prehistory.\"},\n       {\"src\": \"Wiktionary\", \"where\": \"ترازو and طراز\", \"stance\": \"supports\",\n        \"note\": \"ترازو: 'from Middle Persian tlʾcwk' (tarāzūg), borrowed from Avestan tara.azu'; طراز (Persian): 'Arabic respelling of a word which is originally a Persian loan into Arabic'.\"}\n     ]},\n\n    {\"id\": 3, \"lang\": \"Avestan\", \"words\": \"ajras; aštrâ 1; ašaya\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"All three words really belong to PIE *h₂eǵ- as Pokorny sets it out on pp. 4-6, but the \"\n                    \"box mixes languages and one gloss is off. (i) 'ajras' is Vedic Sanskrit ájra- 'plain, \"\n                    \"field, open country' — Pokorny p. 6 files it as 'Ai. ájra-ḥ ,Fläche, Flur, Gefilde'' \"\n                    \"under aǵ-ro-s, beside Gk. ἀγρός and Lat. ager; it is not an Avestan word (the Avestan \"\n                    \"member of that group is azra- in azrō.daiδīm 'going after prey', Yt 14). So the language \"\n                    \"label is wrong for this word. (ii) aštrā- 'whip, goad' IS Avestan and is the \"\n                    \"instrument-noun in *-trā of the root: Pokorny p. 4, 'Als idg. Instrumentalnomen auf \"\n                    \"-trā hierher ai. aṣṭrā ,Stachel zum Viehantreiben', av. aštrā ,Peitsche, Geißel''. \"\n                    \"Nourai's '1' is his homograph number. (iii) ašaya is Avestan, but it is the genitive \"\n                    \"DUAL of aša- 'shoulder, armpit' — Pokorny p. 6, 'av. ašaya Gen. Du. ,der beiden \"\n                    \"Achseln'' — under the extension aǵes-/aks- 'axle, shoulder'; the '(wings?)' gloss \"\n                    \"belongs to its Latin cognate āla < *aksla, whose 'wing' sense is secondary to \"\n                    \"'shoulder'.\"),\n     \"sources\": [W_PIE],\n     \"ref_check\": [\n       {\"ref\": \"POK:4\", \"status\": \"partial\",\n        \"note\": (\"POK_01.txt leaf 13 = p. 4 has aštrā ('av. aštrā ,Peitsche, Geißel''), but ajra- and ašaya \"\n                 \"are two pages further on, leaf 15 = p. 6 ('Ai. ájra-ḥ ,Fläche, Flur, Gefilde''; 'av. ašaya \"\n                 \"Gen. Du. ,der beiden Achseln''). So the cited page supports one of the three words \"\n                 \"directly and the other two only through the continuation of the same article — and it \"\n                 \"flatly labels ájra- as Old Indic, not Avestan.\")},\n       {\"ref\": \"KLN:37\", \"status\": \"partial\",\n        \"note\": KLN37 + \" Klein's list has none of aštrā, ajra- or ašaya; it supports the root and the verb, not this box.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"leaf 13-15 = pp. 4-6\", \"stance\": \"partial\", \"note\": \"See ref_check: supports aštrā and ašaya, contradicts the 'Avestan' label on ajras.\"},\n       {\"src\": \"BRT\", \"where\": \"BRT.txt line 6492\", \"stance\": \"supports\",\n        \"note\": \"\\\"j. aštrā- f. 'Geisel, Peitsche, Knute'\\\" with the Yašt 10.113 attestation (yat bərəzəm barat aštrā vācim 'when the whip cracks loud'); Bartholomae also has aštrā-δāt- 'guiding with the whip' (Yt 10.112) and x'aēwayat.aštrā- 'who makes the whip whirl' (Yt 5.130).\"},\n       {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. 'agro-' and 'aks-'\", \"stance\": \"partial\",\n        \"note\": \"Watkins keeps agro- 'field' as a derivative of ag- but gives only the Germanic/Latin/Greek members; his aks- 'Axis' (with 'Latin āla (< *axla), wing, upper arm') is marked '[In Pok. ag- 4]', confirming Pokorny's grouping of the ašaya/āla material under this root.\"}\n     ]},\n\n    {\"id\": 4, \"lang\": \"Pahlavi\", \"words\": \"aštr, aštar\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Middle Persian astar/aštar 'whip' (Book Pahlavi spelling ʾštl) continues Avestan \"\n                    \"aštrā- directly: the Old Iranian instrument-noun *aš-trā- loses its final vowel in the \"\n                    \"Middle Persian collapse of inflection, and the resulting cluster -štr is resolved by an \"\n                    \"anaptyctic vowel, giving astar — the same development as in Av. vastra- 'garment' > MP \"\n                    \"wastar, Av. sāstar- > MP sāstar. MacKenzie's Concise Pahlavi Dictionary lists it \"\n                    \"separately from the homograph astar 'sin' (< Av. ā + star-). The Šāyast nē Šāyast, the \"\n                    \"text Nourai's source SNS glosses, uses both astar and the phrase astar burdan '(to) \"\n                    \"carry/apply the whip' in its penance passages, which is where a whip-word naturally \"\n                    \"belongs in Zoroastrian legal literature.\"),\n     \"sources\": [W_PIE],\n     \"ref_check\": [\n       {\"ref\": \"SNS:35\", \"status\": \"supports\",\n        \"note\": (\"SNS.txt line 3569 carries the glossary lemma 'astar/astr:' with its Persian gloss, \"\n                 \"immediately followed at line 3570 by the Avestan etymon and Bartholomae reference \"\n                 \"'aštrā- (AiW 263)'; the book's back index (SNS.txt lines 33723-33724) reads 'astar 35/17' \"\n                 \"and 'astar burdan 35/19', i.e. page 35, lines 17 and 19 — precisely Nourai's SNS:35.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt line 1285\", \"stance\": \"supports\",\n        \"note\": \"\\\"astar ['štl] whip\\\" — MacKenzie's Concise Pahlavi Dictionary has the word, distinct from line 1242 \\\"astar ['st'/l M 'st'r] sin\\\".\"},\n       {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt, grep 'astar'\", \"stance\": \"silent\",\n        \"note\": \"Nyberg's Manual of Pahlavi glossary has āstār 'sin' (< Av. ā + star-), sāstar, wastarg, rastar etc., but no astar 'whip' — the word simply does not occur in the texts he glosses.\"},\n       {\"src\": \"BRT\", \"where\": \"BRT.txt line 6492\", \"stance\": \"supports\", \"note\": \"Supplies the Avestan aštrā- 'Peitsche' this Pahlavi form continues.\"}\n     ]},\n\n    {\"id\": 5, \"lang\": \"Persian\", \"words\": \"aštar «آشتَر ٢»\",\n     \"verdict\": \"unverified\",\n     \"derivation\": (\"If it existed, New Persian āštar 'whip' would be the regular continuation of MP astar \"\n                    \"(node #4) — MP -st- is normally kept in NP, and the initial ā- of the chart's «آشتَر» \"\n                    \"would be the usual prothetic/lengthened treatment of a word-initial cluster, as in \"\n                    \"استر, اشتر. But no independent evidence for it could be found. Nourai's own NOTE \"\n                    \"concedes 'This word was not found in MON or BQT', and that is confirmed here: grepping \"\n                    \"آشتر in BQT_v1_pages.txt returns nothing, and Richardson's Persian-Arabic-English \"\n                    \"dictionary (RCH), which is generous with obsolete words, has no āštar/aštar 'whip' \"\n                    \"either (its 'whip' hits are all Arabic). SNS:35, the only citation, is a glossary of \"\n                    \"the Pahlavi Šāyast nē Šāyast — its Persian column is Tavoosi's modern rendering of the \"\n                    \"Pahlavi lemma, not evidence of an independent New Persian word. So the box looks like a \"\n                    \"New-Persian entry manufactured out of a Pahlavi glossary's translation line. The \"\n                    \"standard NP words for 'whip' are تازیانه tāziyāna (< MP tāzānag, PHD line 4973) and \"\n                    \"شلاق.\"),\n     \"sources\": [],\n     \"ref_check\": [\n       {\"ref\": \"SNS:35\", \"status\": \"partial\",\n        \"note\": (\"SNS.txt line 3569 'astar/astr:' + index 'astar 35/17' confirms that page 35 of Tavoosi's \"\n                 \"glossary has the word — but as a PAHLAVI lemma of the Šāyast nē Šāyast with a modern \"\n                 \"Persian gloss beside it, which is not the same as attesting a New Persian آشتر. The same \"\n                 \"citation therefore supports node #4 and only half-supports node #5.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"grep 'آشتر' in BQT_v1_pages.txt (vol. 1 covers آ–ت)\", \"stance\": \"silent\",\n        \"note\": \"No occurrence — independently confirming Nourai's own note.\"},\n       {\"src\": \"MON\", \"where\": \"grep 'آشتر' in MON_part1.txt / MON_part2.txt\", \"stance\": \"silent\",\n        \"note\": \"One hit only, in MON_part2 line 92720, and it is a discussion of an Avestan phrase ('در هیچ جای اوستا «آشتر شتی»…'), not a Persian headword.\"},\n       {\"src\": \"RCH\", \"where\": \"Richardson, grep 'whip' (51 hits) and 'ashtar'\", \"stance\": \"silent\",\n        \"note\": \"None of Richardson's 'whip' entries is āštar; the ashtar-shaped hits are unrelated words (Tashtar 'archangel Michael', bashtar etc.).\"},\n       {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt line 4973\", \"stance\": \"partial\",\n        \"note\": \"\\\"tāzānag [t'c'nk | N tāz(y)āna] whip\\\" — MacKenzie's own cross-reference shows that the word that actually survived into New Persian for 'whip' is tāziyāna, not astar.\"}\n     ]},\n\n    {\"id\": 6, \"lang\": \"Greek\", \"words\": \"agein; stratos-agein\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Greek ἄγειν ágein 'to lead, drive' is the direct thematic present of *h₂eǵ- (Pokorny \"\n                    \"p. 4: 'gr. ἄγω ,führe''), the exact counterpart of Lat. agō and Av. azaiti. Nourai's \"\n                    \"'stratos-agein' is his shorthand for the compound: στρατός stratós 'army' (literally \"\n                    \"'that which is spread out', PIE *sterh₃- — hence his cross-reference ☞Ster 1) + the \"\n                    \"agent noun ἀγός agós 'leader' from ágein, giving στρατηγός stratēgós 'general', \"\n                    \"whence the abstract στρατηγία stratēgía 'the office/art of a general'. Pokorny prints \"\n                    \"στρατηγός on p. 4 itself, in the list of o-stem derivatives (ἀγός ,Führer, \"\n                    \"Heerführer'; ἀτταν-ἀγός, att.-ion. στρατηγός ,Heerführer').\"),\n     \"sources\": [E_STRAT, W_PIE],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"AHD_watkins1985.txt s.v. ag-: \\\"2. Greek agein, to drive, lead: -AGOGUE, AGONY; ANAGOGE, (ANTAGONIZE), CHORAGUS, DEMAGOGUE, EPACT, GLUCAGON, HYPNAGOGIC, MYSTAGOGUE, PEDAGOGUE, PROTAGONIST, STRATAGEM, SYNAGOGUE.\\\" Nourai cites AHD with no page, and the appendix root entry says exactly this.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"leaf 13 = p. 4\", \"stance\": \"supports\",\n        \"note\": \"\\\"gr. ἄγω ,führe'\\\" and, in the o-stem list at the head of the page, \\\"ἀγός ,Führer, Heerführer'; … στρατηγός\\\".\"},\n       {\"src\": \"KLN\", \"where\": \"leaf 31 = p. 37 s.v. agent, adj.\", \"stance\": \"supports\",\n        \"note\": \"Klein's 'Cp.' list under the base *ag- includes 'strategy' and 'synagogue' as well as Gk. ἄγειν itself.\"},\n       {\"src\": \"Etymonline\", \"where\": \"entry 'strategy'\", \"stance\": \"supports\",\n        \"note\": \"\\\"Greek strategia 'office or command of a general', from strategos 'general, commander of an army', from stratos 'army' … + agos 'leader', from agein 'to lead' (PIE root *ag-).\\\"\"}\n     ]},\n\n    {\"id\": 7, \"lang\": \"French\", \"words\": \"strategie\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"French stratégie, a learned 16th-century formation on Latinised Greek stratēgia; the \"\n                    \"Greek η is rendered é and the Greek -ia becomes the French learned suffix -ie (as in \"\n                    \"philosophie, théologie). It stayed a term of ancient history until the professional \"\n                    \"military literature of the later 18th century (Joly de Maizeroy, 1771, is usually \"\n                    \"credited with the modern technical sense), and that revived French word is the one \"\n                    \"that spread to the rest of Europe.\"),\n     \"sources\": [E_STRAT],\n     \"ref_check\": [\n       {\"ref\": \"AHD:1273\", \"status\": \"not_checked\",\n        \"note\": \"A page of the main text of the 1975/76 AHD New College Edition (the 'st-' range fits p. 1273 well), which is not open online; only Watkins' root appendix is on disk, and there STRATAGEM/STRATEGY appear in the ag- word list without a French stage being spelled out.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"Etymonline\", \"where\": \"entry 'strategy'\", \"stance\": \"supports\",\n        \"note\": \"\\\"1810, from French stratégie (18c.) and directly from Greek strategia\\\"; the French word is dated 16c. in the entry's own citation of stratégie.\"},\n       {\"src\": \"FSD\", \"where\": \"FSD_vol4.txt line 23971 s.v. stratagem\", \"stance\": \"supports\",\n        \"note\": \"\\\"[<F stratagème, <L stratēgema, <Gr stratēgēma, <strategos, general, <stratos, army, + [agein] lead]\\\" — Funk & Wagnalls routes the family through French exactly as the chart does.\"},\n       {\"src\": \"KLN\", \"where\": \"leaf 31 = p. 37\", \"stance\": \"partial\", \"note\": \"Klein lists 'strategy' among the *ag- descendants but the detail of the French stage is in his own s.v. strategy, not on this page.\"}\n     ]},\n\n    {\"id\": 8, \"lang\": \"Persian\", \"words\": \"esterâtežî «استراتژی»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian استراتژی esterātežī is a 20th-century borrowing of French stratégie, and the \"\n                    \"French route is written into the shape of the word: the ژ /ʒ/ can only come from French \"\n                    \"-gie /ʒi/ (English strategy would have given *esterātejī with ج /dʒ/), and the \"\n                    \"prothetic ا- before the initial cluster st- is the regular Persian treatment of \"\n                    \"European s+consonant onsets (استکان, اسپانیا, استاندارد). Moʿin's entry tags it as a \"\n                    \"European loan and glosses it 'فن ادارهٔ عملیات جنگی؛ دانش رهبری عملیات نظامی؛ سوق \"\n                    \"الجیش' — 'the art of directing operations of war; the science of leading military \"\n                    \"operations', i.e. the modern French technical sense, not the ancient Greek one.\"),\n     \"sources\": [E_STRAT],\n     \"ref_check\": [\n       {\"ref\": \"MON:246\", \"status\": \"supports\",\n        \"note\": (\"MON_part1.txt line 11745: 'استراتژی: [fr.] (اِ.) فن ادارهٔ عملیات جنگی؛ دانش رهبری عملیات \"\n                 \"نظامی؛ سوق الجیش.' The entry stands between استر 'mule' and استراتوسفر, i.e. in the \"\n                 \"الف-س-ت run of vol. 1, which is where p. 246 falls; the source-language tag is present \"\n                 \"(rendered '2' by the OCR, the same glyph that OCRs as '2'/'فر.' on the other French loans \"\n                 \"on the page, e.g. آژانس).\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"MON_part1.txt line 11745\", \"stance\": \"supports\", \"note\": \"See ref_check — Moʿin has the word, tagged as a European (French) loan, with the modern military gloss.\"},\n       {\"src\": \"Etymonline\", \"where\": \"entry 'strategy'\", \"stance\": \"supports\",\n        \"note\": \"Confirms that it was the French word, in its post-1770s military sense, that was internationally borrowed — matching the Persian gloss.\"},\n       {\"src\": \"BQT\", \"where\": \"grep استراتژی in BQT_v1_pages.txt\", \"stance\": \"silent\", \"note\": \"Absent, as expected for a 17th-century dictionary.\"}\n     ]},\n\n    {\"id\": 9, \"lang\": \"English\", \"words\": \"strategy\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"English strategy, 1810, from French stratégie and directly from the Latinised Greek \"\n                    \"stratēgia; strategic follows in 1825 from French stratégique. The sense 'plan for \"\n                    \"achieving an aim' (1833 for a particular instance) and its extension outside war \"\n                    \"(by 1887) are English developments. Nourai's French → English arrow is therefore right, \"\n                    \"and the older doublet stratagem had already come the same way in the 15th century \"\n                    \"(F. stratagème < L. stratēgēma < Gk. στρατήγημα).\"),\n     \"sources\": [E_STRAT],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box.\"}],\n     \"consulted\": [\n       {\"src\": \"Etymonline\", \"where\": \"entry 'strategy'\", \"stance\": \"supports\",\n        \"note\": \"\\\"1810, from French stratégie (18c.) and directly from Greek strategia 'office or command of a general' … by 1833 … by 1887 in non-military contexts.\\\"\"},\n       {\"src\": \"FSD\", \"where\": \"FSD_vol4.txt lines 23971, 23985-23990\", \"stance\": \"supports\",\n        \"note\": \"\\\"strategy … [< Gr stratēgikos, < stratēgos, see stratagem]\\\" and, under stratagem, the F–L–Gk chain quoted at node #7.\"},\n       {\"src\": \"KLN\", \"where\": \"leaf 31 = p. 37\", \"stance\": \"supports\", \"note\": \"'strategy' stands in Klein's list of English words traced to the base *ag-.\"}\n     ]},\n\n    {\"id\": 10, \"lang\": \"English\", \"words\": \"agony, agriculture\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"Both words do go back to *h₂eǵ-, but only one of them goes through the Greek node they \"\n                    \"are drawn under. AGONY: Gk. ἀγών agṓn 'assembly, contest in the games' (an -ōn \"\n                    \"derivative of ágein, 'the gathering that is led together') > ἀγωνία agōnía 'struggle \"\n                    \"for victory' > Eccles. Lat. agōnia (used of Christ's agony in the garden, Luke 22:44) \"\n                    \"> Old French agonie > Middle English agony — so this branch is correctly under Greek. \"\n                    \"AGRICULTURE, on the other hand, is Latin, not Greek: L. agrī cultūra 'cultivation of \"\n                    \"the field', from ager (gen. agrī) 'field' < *h₂éǵ-ro-, borrowed into French and thence \"\n                    \"into English (1590s). Its place on the chart should be under the Latin node #11 (or \"\n                    \"under the 'Agros' half of the root box) rather than under Greek ágein; Watkins files it \"\n                    \"under the separate derivative root agro-, and Klein's list distinguishes 'agrarian, \"\n                    \"agriculture' (via ager) from 'agony' (via ἀγών). Hence 'plausible' rather than \"\n                    \"'confirmed': right root, wrong branch for one of the two words.\"),\n     \"sources\": [W_PIE],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box; the parent Greek box cites AHD.\"}],\n     \"consulted\": [\n       {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. 'ag-' and 'agro-'\", \"stance\": \"partial\",\n        \"note\": \"AGONY is listed under ag- 2 (Greek agein); AGRICULTURE is listed under the separate entry 'agro-. Field. Derivative of ag-… 2. Latin ager … AGRARIAN, AGRESTAL; AGRICULTURE, PEREGRINE, (PILGRIM)', i.e. under Latin, not Greek.\"},\n       {\"src\": \"KLN\", \"where\": \"leaf 31 = p. 37 (agent, adj.) and leaf 33 (agrarian)\", \"stance\": \"partial\",\n        \"note\": \"Klein s.v. agrarian: \\\"fr. L. agrarius … fr. ager, gen. agri, 'field, land', which is rel. to Umbr. ager and cogn. with Gk. ἀγρός, Goth. akrs, OE. æcer, 'field'. See acre and agent and cp. agriculture.\\\" — agriculture reaches English through Latin ager, not through Greek agein.\"},\n       {\"src\": \"POK\", \"where\": \"leaf 13-15 = pp. 4-6\", \"stance\": \"supports\",\n        \"note\": \"p. 4 'gr. ἀγών ,Wettlauf, Wettkampf''; p. 6 'aǵ-ro-s ,Feld, Flur' … lat. umbr. ager ,Feld'' — both words in the article, on two different branches.\"}\n     ]},\n\n    {\"id\": 11, \"lang\": \"Latin\", \"words\": \"agere; agĕns; ag-sla; ambractus\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"agere 'to drive, do, act' is the Latin thematic present of *h₂eǵ- (perfect ēgī with \"\n                    \"analogical lengthened grade, ppp. āctus), and agēns, gen. agentis is its present \"\n                    \"participle, whence the noun 'agent'; both are impeccable, and Pokorny p. 4 has \\\"lat. \"\n                    \"agō ,treibe, führe, verhandle'\\\". The other two entries need qualification. (i) 'ag-sla' \"\n                    \"is Nourai's way of writing the preform of Latin āla 'wing', i.e. *ag-s-lā > *axla > āla \"\n                    \"with compensatory lengthening — Pokorny p. 6, \\\"Lat. āla ,Achsel', woraus die üblichere \"\n                    \"Bedeutung ,Flügel'; aus *agsla (vgl. Demin. axilla ,Achselhöhle')\\\", so the form and the \"\n                    \"'wing' gloss are Pokorny's, although the original sense is 'shoulder/armpit' and \"\n                    \"Watkins detaches the whole group as a separate root aks- (flagged '[In Pok. ag- 4]'). \"\n                    \"(ii) 'ambractus : envoy' is a misprint for ambactus — verified against the 200-dpi \"\n                    \"render of pdf p. 35, so the error is the book's, not the extraction's — and the word is \"\n                    \"not really Latin but Gaulish: Celtic *ambi-ag-to- 'one sent around', taken into Latin \"\n                    \"as ambactus 'vassal, retainer' (Ennius, Caesar BG 6.15) and into Germanic as Goth. \"\n                    \"andbahts, OHG ambaht 'servant', whence German Amt; Med. Lat. ambactia 'office' is the \"\n                    \"source of ambassador/embassy. Its gloss is 'servant, retainer', not 'envoy' — 'envoy' \"\n                    \"is the later Romance development.\"),\n     \"sources\": [E_AMB, E_AGENT, W_PIE],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": (\"AHD_watkins1985.txt s.v. ag-: \\\"1. Latin agere, to do, act, drive, conduct, lead: ACT, \"\n                 \"AGENDUM, AGENT, AGILE, AGITATE … 3. Suffixed form *ag-to- in Celtic *amb(i)-ag-to-, 'one \"\n                 \"sent around' (*ambi, around; see ambhi), in Latin ambactus, servant (> Medieval Latin \"\n                 \"ambactia, office): AMBASSADOR, EMBASSAGE, (EMBASSY).\\\" Watkins gives Nourai's agere, agens \"\n                 \"and ambactus — and spells the last one without the -r-, confirming the misprint. For \"\n                 \"'ag-sla' Watkins uses his separate entry aks-: \\\"3. Suffixed form *aks-lā- in Latin āla \"\n                 \"(< *axla), wing, upper arm … [In Pok. ag- 4.]\\\"\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"leaf 13-15 = pp. 4-6\", \"stance\": \"supports\",\n        \"note\": \"p. 4: \\\"lat. agō ,treibe, führe, verhandle' (Pf. ēgī)\\\" and \\\"kelt. *amb(i)-aktos eigentlich ,herumgesandter Bote, Diener' in gall.(-lat.) ambactus ,Dienstmann, Höriger'\\\"; p. 6: \\\"Lat. āla ,Achsel', woraus die üblichere Bedeutung ,Flügel'; aus *agsla\\\".\"},\n       {\"src\": \"KLN\", \"where\": \"leaf 31 = p. 37\", \"stance\": \"supports\",\n        \"note\": \"Klein's list under the base *ag- contains 'ala, ambages, ambassador, … axilla, axis, axle, … embassy', i.e. all four of Nourai's Latin items.\"},\n       {\"src\": \"Etymonline\", \"where\": \"entry 'ambassador'\", \"stance\": \"supports\",\n        \"note\": \"\\\"from Latin ambactus 'a servant, vassal', from Celtic amb(i)actos 'a messenger, servant' … PIE *ambhi- 'around' + *ag- 'to drive, draw out or forth, move'\\\" — Celtic, and with the sense 'servant'.\"},\n       {\"src\": \"LEW\", \"where\": \"LEW_1910.txt (Walde, Lat. etym. Wb.)\", \"stance\": \"silent\",\n        \"note\": \"The local Walde OCR could not be searched reliably for agō/ambactus (heavily corrupted running text); Pokorny's own 'WH. I 9, 10, 24' back-references on p. 4 stand in for it.\"}\n     ]},\n\n    {\"id\": 12, \"lang\": \"French\", \"words\": \"agence, agent\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"French agent is Latin agentem (acc. of agēns) taken over as a learned word, and agence \"\n                    \"comes from Medieval/Late Latin agentia, an abstract in -ia built on the same \"\n                    \"participle; Klein notes the two side by side: 'agency, n. — Late L. agentia (whence also \"\n                    \"F. agence), fr. L. agens, gen. agentis, pres. part. of agere' and 'agent, n. — F., in \"\n                    \"the sense of \\\"acting force\\\", fr. ML. agens … fr. It. agente'. The French sense \"\n                    \"'commercial/administrative office' for agence, and 'official, functionary' for agent \"\n                    \"(hence agent de police), are 17th-19th c. French developments, and they are the senses \"\n                    \"that Persian borrowed.\"),\n     \"sources\": [E_AGENT],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box.\"}],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"leaf 31 = p. 37, s.vv. agency, agent\", \"stance\": \"supports\",\n        \"note\": \"\\\"agency, n. — Late L. agentia (whence also F. agence), fr. L. agens, gen. agentis, pres. part. of agere\\\"; \\\"agent, n. — F., in the sense of 'acting force', fr. ML. agens, in the sense of 'acting person', fr. It. agente; both these words derive fr. L. agens.\\\"\"},\n       {\"src\": \"Etymonline\", \"where\": \"entry 'agent'\", \"stance\": \"supports\",\n        \"note\": \"\\\"from Latin agentem (nominative agens) 'effective, powerful', … from agere 'to set in motion, drive forward; to do, perform' … 'deputy, representative' 1590s.\\\"\"},\n       {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. ag-\", \"stance\": \"supports\", \"note\": \"AGENT and AGENDUM listed under Latin agere.\"}\n     ]},\n\n    {\"id\": 13, \"lang\": \"Persian\", \"words\": \"âžâns «آژانس»; âžân «آژان»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Both are French loans of the Qajar/Pahlavi period, and again the ژ /ʒ/ gives the source \"\n                    \"away: French agence /aʒɑ̃s/ > Persian آژانس āžāns 'agency, bureau, news agency', and \"\n                    \"French agent (de police) /aʒɑ̃/ > Persian آژان āžān 'policeman, constable'. The French \"\n                    \"nasal vowel /ɑ̃/ is rendered as ā + n in آژان and as ā + ns in آژانس, so the two Persian \"\n                    \"words preserve the difference between the French noun and the French agent-noun. آژان \"\n                    \"in the 'policeman' sense is now archaic, replaced by پاسبان and then مأمور پلیس, while \"\n                    \"آژانس is fully alive (آژانس مسافرتی, خبرگزاری/آژانس خبری).\"),\n     \"sources\": [E_AGENT],\n     \"ref_check\": [\n       {\"ref\": \"VOP:10\", \"status\": \"not_checked\",\n        \"note\": (\"VOP = M. Moshiri, Farhang-e Vāžehā-ye Orupāʾi dar Fārsi (Dictionary of European Words in \"\n                 \"Persian), Alborz Press, Tehran 1371/1992 (bibliography_raw.txt, Table IV no. 05). It is \"\n                 \"not in the local reference library and is not on archive.org, so the cited page could not \"\n                 \"be read; its subject-matter, however, is precisely European loanwords in Persian, which \"\n                 \"makes it the right kind of authority for this box, and Moʿin independently gives the same \"\n                 \"French source (see consulted).\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 2988-2993 and 2163; also 32624, 55401\", \"stance\": \"supports\",\n        \"note\": \"'آژانس: [agence] (اِ.) نمایندگی، کارگزاری، بنگاهی که به نمایندگی مؤسسات دیگر کارهایی را انجام دهد؛ آژانس معاملات؛ خبرگزاری' — the OCR preserves the Latin-script French etymon; and 'آژان: (اِ.) نماینده، کارگزار' with 'آژان، مه پلیس' and 'آژان، عسس، محتسب' for the policeman sense.\"},\n       {\"src\": \"Etymonline\", \"where\": \"entry 'agent'\", \"stance\": \"supports\", \"note\": \"Supplies the Latin > French chain that feeds the Persian forms.\"},\n       {\"src\": \"BQT\", \"where\": \"grep آژانس / آژان in BQT_v1_pages.txt\", \"stance\": \"silent\", \"note\": \"Absent, as expected for a pre-modern dictionary.\"}\n     ]},\n\n    {\"id\": 14, \"lang\": \"English\", \"words\": \"act, acre, exact, -gate, navigate; agent, agency; axle, axis, ambassador, embassy\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"A summary box, and every item in it is standard. Via Latin agere: ACT (< āctus, ppp.), \"\n                    \"EXACT (< exigere 'to drive out, weigh out, measure' > exāctus), the combining form \"\n                    \"-GATE in NAVIGATE (nāvis + agere), FUMIGATE, LITIGATE, MITIGATE, CASTIGATE etc. — the \"\n                    \"-igāre verbs are compounds of agere with vowel weakening a > i in the unstressed medial \"\n                    \"syllable; AGENT and AGENCY via French from agēns/agentia (node #12). Via *h₂éǵ-ro-: \"\n                    \"ACRE, inherited through Germanic *akraz > OE æcer 'field', not borrowed. Via the \"\n                    \"'shoulder/axle' extension: AXIS (< L. axis), AXLE (< ON ǫxull / OE eax, Gmc. *ahsulaz). \"\n                    \"Via Gaulish ambactus: AMBASSADOR (14c., through Old French/Provençal from Med. Lat. \"\n                    \"ambactia) and EMBASSY (1570s, through Italian ambasciata). Klein's 'Cp.' list on the \"\n                    \"very page Nourai cites for the Avestan node (p. 37) contains acre, act, agency, agenda, \"\n                    \"agent, ambassador, axilla, axis, axle, embassy, exact and navigate — the whole box in \"\n                    \"one line.\"),\n     \"sources\": [E_AGENT, E_AMB, W_PIE],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box; the parent Latin box cites AHD.\"}],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"leaf 31 = p. 37 s.v. agent, adj.\", \"stance\": \"supports\", \"note\": KLN37},\n       {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.vv. ag-, agro-, aks-\", \"stance\": \"supports\",\n        \"note\": \"ag- gives ACT, AGENT, EXACT, NAVIGATE, FUMIGATE, LITIGATE, TRANSACT and (via ambactus) AMBASSADOR, EMBASSAGE, EMBASSY; agro- gives ACRE, AGRARIAN, AGRICULTURE; aks- gives AXLE, AXIS, AXILLA, ALA, AISLE — the last group flagged '[In Pok. ag- 4]'.\"},\n       {\"src\": \"Etymonline\", \"where\": \"entries 'agent' and 'ambassador'\", \"stance\": \"supports\",\n        \"note\": \"\\\"ambassador … from Latin ambactus 'a servant, vassal', from Celtic amb(i)actos\\\"; \\\"embassy (1570s) … from Italian ambasciata … from Gaulish ambactos\\\".\"},\n       {\"src\": \"FSD\", \"where\": \"FSD_vol4.txt s.v. stratagem/strategy\", \"stance\": \"partial\",\n        \"note\": \"Covers only the strategy family of this root, but does so through the same Greek/Latin/French route.\"}\n     ]}\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-35.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk35.py && python3 -m json.tool data/verification/page-35.json > /dev/null && echo \"JSON OK\"",
 "description": "Write page-35.json"
}
```


### [2026-09-04T18:45:03.080Z] TOOL RESULT

```
written
JSON OK
```


## [2026-09-04T18:45:07.517Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 tools/verify_check.py 35",
 "description": "Run verify_check for page 35"
}
```


### [2026-09-04T18:45:09.206Z] TOOL RESULT

```
nodes verified: 20/20
node verdicts: {'confirmed': 14, 'disputed': 1, 'plausible': 4, 'unverified': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 11, 'not_checked': 11, 'partial': 4}
books consulted: {'supports': 40, 'silent': 13, 'contradicts': 2, 'partial': 11, 'not_found': 1} | by book: {'KLN': 11, 'Etymonline': 11, 'MON': 6, 'Wiktionary': 5, 'BQT': 5, 'FSD': 4, 'POK': 4, 'AHD': 4, 'FVQ': 3, 'BRT': 3, 'PHD': 2, 'WEB': 1, 'CHEUNG': 1, 'PLA': 1, 'HRN': 1, 'HUB': 1, 'LKT': 1, 'NYB': 1, 'RCH': 1, 'LEW': 1}
```


## [2026-09-04T18:45:12.705Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | grep -i \"35\\|error\\|missing\" | head -20",
 "description": "Verify archived sources"
}
```


### [2026-09-04T18:45:18.621Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:45:20.921Z] TOOL CALL #72: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | tail -20",
 "description": "Full archive check output"
}
```


### [2026-09-04T18:45:24.277Z] TOOL RESULT

```
182 cited URLs, 21 not yet archived
archived 21, failed 0
```


## [2026-09-04T18:45:41.888Z] AGENT

Done. `data/verification/page-35.json` written; `verify_check.py 35` reports 20/20 nodes, no PROBLEM lines.

**Page 35 (book p. 5), 2 entries, 20 nodes**
- Root verdicts: confirmed 2 (Hebrew *ʾădāmāh*; PIE *ag-/agros* = Pokorny p. 4 verbatim, incl. "Ort, wo das Vieh hinausgetrieben wird").
- Node verdicts: confirmed 14, plausible 4, disputed 1, unverified 1.
- Ref checks: 11 supports, 4 partial, 11 not_checked (AHD main-dictionary pages, VDQ noorlib, VOP, MON vol. 5 — none of these are on disk/online).

Flagged items:
- **disputed** — Âdhâmah, node #3 [Latin] (empty box): Latin *Adam* is drawn as a borrowing from Arabic آدم. Impossible chronologically; Latin has it from Septuagint/NT Greek Ἀδάμ via the Vulgate, straight from Hebrew.
- **unverified** — Ag, node #5 [Persian] *aštar* «آشتَر»: absent from BQT, MON (Nourai's own note) and also from Richardson; the sole citation SNS:35 is a Pahlavi glossary whose Persian column is a modern gloss. NP "whip" is تازیانه (MacKenzie: *tāzānag* > N *tāz(y)āna*).
- **plausible** — Âdhâmah #6 Persian آدم: right ultimate source, but borrowed via Arabic (the chart's own node #2), not straight from Hebrew.
- **plausible** — Ag #3 [Avestan]: "ajras" is Vedic *ájra-* (Pokorny p. 6 marks it "Ai."), not Avestan; "ašaya : of both wings?" is gen. dual "of the two shoulders".
- **plausible** — Ag #10: *agriculture* belongs under Latin *ager*, not under Greek *agein*.
- **plausible** — Ag #11: "ambractus" is a printed-book misprint for *ambactus* (confirmed on the 200-dpi page render, so not an extraction error), and the word is Gaulish, glossed "servant/vassal", not Latin "envoy".

Strongest confirmation: the Iranian branch Av. *tara.azu* → MP *tarāzūg* → NP ترازو, independently supported by Asbaghi PLA p. 194 ("mp. tarāzūk 'Balance' … aw. az"), Moʿin's footnote in Borhān-e Qāṭeʿ p. 480 ("پهلوی tarāzūk، ایرانی باستان *tarāzu-… از aj سانسکریت") and Wiktionary — Nourai's BQT:480 and PLA:194 page numbers are both exact.
