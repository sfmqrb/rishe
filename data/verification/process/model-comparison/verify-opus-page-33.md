# Verification process log — model-comparison/verify-opus-page-33


## [2026-09-04T18:07:11.018Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 33 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-33.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-33.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (all files listed in the source matrix exist there). ONE DEVIATION from the instructions: this is a model-comparison run, so write your output to /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus/page-33.json instead of data/verification/, do NOT read or copy any existing file under /home/sfmqrb/git/rishe/data/verification/page-*.json, and check coverage with `VERIFY_DIR=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus python3 /home/sfmqrb/git/rishe/tools/verify_check.py 33` (the script now honours VERIFY_DIR). Everything else as instructed (modern web sources archived with tools/fetch_source.py, Nourai's citations checked in the local reference texts, every relevant book consulted per the source matrix). Reply with the short summary described in the instructions.


## [2026-09-04T18:07:15.468Z] AGENT

I'll start by reading the instructions.


## [2026-09-04T18:07:17.619Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T18:07:17.636Z] TOOL RESULT

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


## [2026-09-04T18:07:17.917Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-33.txt"
}
```


### [2026-09-04T18:07:17.933Z] TOOL RESULT

```
1	=== PDF page 33 (book page 3) ===
2	--- entry 0 ---
3	ROOT [Semitic] Ab 2 : father  (refs FVQ:44; KLN:6)
4	#1 (parent #0) [Arabic] refs=FVQ:44; FVA:25; LKT:44 | ab, abŭ, a.b.v : father
5	  #2 (parent #1) [Persian] refs=FVA:25; MON | abŭ «آبو ( ابوی )» : father | extra: ابوعلی سینا ، ابوالفضل ، ابوالقاسم ، ابوالحسن ، ابوالفتح ، بوالهوس
6	  #3 (parent #1) [Arabic] refs=FVQ:44; FVA:25; LKT:44; AHD:152 | abŭ-zînâ : "father of whoredom" referring to gibbons ☞Z.n.y ; abŭ-araq : "father of sweat", a spicy plant used in medicine ☞A.r.q
7	    #4 (parent #3) [Persian] refs=MON:602; FVA:180 | bŭzîneh «بوزینه ( بوزنه )» : gibbon
8	      #5 (parent #4) [Hindustani] refs=PRT:253 | bojîna
9	        #6 (parent #5) [French] refs=KLN:655 |  | NOTE: This monkey was taken to France from India in the 18th century.
10	          #7 (parent #6) [English] refs=KLN:655 | gibbon
11	    #8 (parent #3) [Middle Latin] refs=AHD:152 | borrâco
12	      #9 (parent #8) [Old French] refs=AHD:152 | borrace, bourrache
13	        #10 (parent #9) [English] refs=AHD:152 | borage : a spicy salad seasoning
14	#11 (parent #0) [Hebrew] refs=KLN:6 | abh : father
15	  #12 (parent #11) [English] refs=KLN:6 | Abot
16	  #13 (parent #11) [Hebrew] refs=FVQ:44; KLN:6 | Abh-raham : father of the multitude (Abraham) ; Abh-ram : high father (Abram) ; Abh-ner : my father is light (Abner) ☞N.w.r ; Ab-šalom : father is peace (Absalom) ☞S.l.m ; Abh-igayil : father is rejoicing (Abigail) ; Yo-abh : the Lord is his father (Joab)
17	    #14 (parent #13) [Arabic] refs=FVQ:44 | Abrahim : Abraham
18	      #15 (parent #14) [Persian] refs=None | Ebrâhîm «ابراهیم»
19	    #16 (parent #13) [English] refs=KLN; AHD | Abraham, Abram, Abner, Absalom, Abigail, Jaob
20	
```


## [2026-09-04T18:07:22.386Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T18:07:22.467Z] TOOL RESULT

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


## [2026-09-04T18:07:22.593Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-33.json | head -200",
 "description": "Read page 33 JSON"
}
```


### [2026-09-04T18:07:24.367Z] TOOL RESULT

```
{
    "pdf_page": 33,
    "book_page": 3,
    "entries": [
        {
            "root": {
                "name": "Ab 2",
                "lang": "Semitic",
                "refs": "FVQ:44; KLN:6",
                "gloss": "father"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Arabic",
                    "refs": "FVQ:44; FVA:25; LKT:44",
                    "words": [
                        {
                            "translit": "ab, ab\u016d, a.b.v",
                            "gloss": "father",
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
                    "refs": "FVA:25; MON",
                    "words": [
                        {
                            "translit": "ab\u016d",
                            "gloss": "father",
                            "script": "\u0622\u0628\u0648 ( \u0627\u0628\u0648\u06cc )"
                        }
                    ],
                    "script_extra": "\u0627\u0628\u0648\u0639\u0644\u06cc \u0633\u06cc\u0646\u0627 \u060c \u0627\u0628\u0648\u0627\u0644\u0641\u0636\u0644 \u060c \u0627\u0628\u0648\u0627\u0644\u0642\u0627\u0633\u0645 \u060c \u0627\u0628\u0648\u0627\u0644\u062d\u0633\u0646 \u060c \u0627\u0628\u0648\u0627\u0644\u0641\u062a\u062d \u060c \u0628\u0648\u0627\u0644\u0647\u0648\u0633",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 1,
                    "lang": "Arabic",
                    "refs": "FVQ:44; FVA:25; LKT:44; AHD:152",
                    "words": [
                        {
                            "translit": "ab\u016d-z\u00een\u00e2",
                            "gloss": "\"father of whoredom\" referring to gibbons",
                            "script": null,
                            "see": [
                                "Z.n.y"
                            ]
                        },
                        {
                            "translit": "ab\u016d-araq",
                            "gloss": "\"father of sweat\", a spicy plant used in medicine",
                            "script": null,
                            "see": [
                                "A.r.q"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "Persian",
                    "refs": "MON:602; FVA:180",
                    "words": [
                        {
                            "translit": "b\u016dz\u00eeneh",
                            "gloss": "gibbon",
                            "script": "\u0628\u0648\u0632\u06cc\u0646\u0647 ( \u0628\u0648\u0632\u0646\u0647 )"
                        }
                    ],
                    "note": null,
                    "quote": {
                        "text": "\u0686\u0648\u0646 \u062f\u0644 \u0628\u0648\u0632\u06cc\u0646\u0647 \u06af\u0631\u062f\u062f \u0622\u0646 \u062f\u0644\u0634 - \u0627\u0632 \u062f\u0644 \u0628\u0648\u0632\u06cc\u0646\u0647 \u0634\u062f \u062e\u0648\u0627\u0631 \u0622\u0646 \u06af\u0644\u0634",
                        "poet": "Molav\u00ee"
                    }
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "Hindustani",
                    "refs": "PRT:253",
                    "words": [
                        {
                            "translit": "boj\u00eena",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 5,
                    "lang": "French",
                    "refs": "KLN:655",
                    "words": [],
                    "note": "This monkey was taken to France from India in the 18th century.",
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "English",
                    "refs": "KLN:655",
                    "words": [
                        {
                            "translit": "gibbon",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 3,
                    "lang": "Middle Latin",
                    "refs": "AHD:152",
                    "words": [
                        {
                            "translit": "borr\u00e2co",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 8,
                    "lang": "Old French",
                    "refs": "AHD:152",
                    "words": [
                        {
                            "translit": "borrace, bourrache",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 10,
                    "parent": 9,
                    "lang": "English",
                    "refs": "AHD:152",
                    "words": [
                        {
                            "translit": "borage",
                            "gloss": "a spicy salad seasoning",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 0,
                    "lang": "Hebrew",
                    "refs": "KLN:6",
                    "words": [
                        {
                            "translit": "abh",
                            "gloss": "father",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 12,
                    "parent": 11,
                    "lang": "English",
                    "refs": "KLN:6",
                    "words": [
                        {
                            "translit": "Abot",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
```


## [2026-09-04T18:07:29.183Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && grep -inE '^(FVA|PRT|FVQ|KLN|LKT|MON|AHD)\\b|FVA|PRT' bibliography_raw.txt | head -40",
 "description": "Grep bibliography for abbreviations"
}
```


### [2026-09-04T18:07:29.235Z] TOOL RESULT

```
3: TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
12: TABLE IV - Reference Abbreviations (continued...) 32 FIB 33 FNI 34 FRS 35 FSD 36 FSF 37 FVA 38 FVF 39 FVQ 40 FWE 41 FWK 42 GPL 43 HID 44 HJB 45 HRN 46 HUB 47 IEC Pur Davfld, Farhang Iran Bastan, Vol. I, University of Tehran Press 1326 (1947). F. DanaT, Farhang Namhay Irani, Negah Publishers, Tehran 1370 (1991). AsadT Tflsi, Farhang Fors, Kharazmi Press, Tehran 1365 (1986). ^iljjl ^cUj^cLs &gt;^fl&gt;jS Funk and Wagnalla, New Standard Dictionary of the English Language, Funk &amp; Wagnalls Company, New York, 1940. A. H. Noushin, Farhang Shahnameh Ferdowsi, oULS 03I3 - ^-jiy i*La&gt;Li ^^ay Vajheh Namak, Donya Press, Tehran 1363 (1984). S. M. Nahvi, Farhang VSm J-^-i - ^-&gt;jl» j* ^o^ ^gb. 03I3 ^(3 ^S^a,^ Vajhehhay Arabi dar Farsi, Dakhil, TohT Azadi Press 1368 (1989). S. M. A. Emam Shflshtari, ^c ^bj ji ^-"j1* iS^ °j'3 «-fc»j» Farhang Vajhehhay Farsi dar zaban Arabi, Anjoman Asar Melli, No 58, Bahman Press, Tehran, 1347 (1968). A. Jeffrey, The Foreign Vocabulary of the Qur'an, (see VDQ). Oriental Institute, Baroda, Stephen Austin &amp; Sons Press, Great Britain 1938 A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, Warner Books, 1966. R. Dvorak, "Fremdworter im Koran", Doctoral Dissertation, Akademische Buchdruckerei von F. Straub (1884). J.T. Platts and G.S.A. Ranking, A Grammar of the Persian Language, Oxford University Press (1911). B. Bartholomae, Handbuch der Altlranischen Dialekte, Breitkopf &amp;Hartel, Leipzig 1883. H. Yule &amp; A. C. Burnel, Hobson Jobson, A Glossary of Colloqual AngloIndian Words, Oriental Publishers, Delhi 1903-1968. Paul Horn, Grundriss der NeuPersischen Etymology, Verlag von Karl J. Trubner, Strassburg 1893-1974. H. Hubschmann, Persische Studien, Verlag von Karl J. Trubner, Strassburg 1895. Stuart E. Mann, An Indo-European Comparative Dictionary, Helmut Buske Verlag, Hamburg 1987 A-ll 
18: TABLE IV - Reference Abbreviations (continued ...) 64 MMF 65 MON 66 MPP 67 MZF 68 NAT 69 NFI 70 NYB 71 OEW 72 OXF 73 PEI 74 PHD 75 PHN 76 PLA 77 POK 78 PRT 79 RCH K. Khalili, Dictionary of Derivatives of the Persian ^wjls jiLa* ol£ii* &gt;_£^&amp;ji Infinitives or Farhang Moshtaqqat Masader FarsT, Institute of Cultural Studies and Research, Tehran, 1993. M. Mo" in, Farhang FarsT MoT'n, Six volumes, Amir Kabir press 1363 (1984). O^*® ^ ^-a-L!* Honari darbareh Zaban Farsi, Sokhan press, Tehran 1340 (1961). C. Berlitz, Native Tongues, Grosset &amp; Dunlapp Publishers, New York, 1982 F. Jonaydi, Nameh Farhang Iran, ^Ijjl ^»js i*b Bonyad Nayshabfir, Tehran 1368 (1989). Section 4, translated from C.H. Rempis' "Persische Worter im Deutschen," in Mitteilungen, Institut fur Auslands-Beziehungen, Iran-Nummer, 3/4, Stuttgart, 1960, S.229-233. H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1974. J. T. Shipley, The Origins of English Words, The John Hopkins University Press, Baltimore 1984. Jennifer Speake, Oxford Dictionary of Foreign Words and Phrases, Oxford University Press, New York 1997 M. Pei, The Families of Words, Harper &amp; Brothers press, New York 1962. D. N. MacKenzie, A Concise Pahlavi Dictionary. Oxford University press, London 1971. A. P. Pihan, Dictionnaire Etymologique des Motes de la Langue Francaise Derives de L'Arabe, du Persan ou du Turc, Paris 1866. Asya Asbaghi, Persische Lehnworter im Arabischen. Otto Harrassowitz, Wiesbaden 1988 J. Pokorny, Indogermanisches Etymologisches Worterbuck, Two volumes, Francke verlag, Bern 1959. E. Partridge, Origins - A short Etymological Dictionary of Modern English, MacMillan Co., NewYork 1958. J. Richardson, Dictionary, Persian, Arabic and English with Dissertation on the Languages, Literature and Manners of Eastern Nations, Sange-e-Meel Publications, Lahore 1829-1984. A-13
```


## [2026-09-04T18:07:32.116Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['FVQ','KLN','LKT','MON','AHD','PRT','FVA','SKT','FSD','WEB','HJB','AID','DEV','PHN','AFM','PLA','AFA','TAD','BQT','ARY','RCH']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-04T18:07:34.325Z] TOOL RESULT

```
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lo
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 =
```


## [2026-09-04T18:07:58.515Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo ---; python3 -c \"\nimport json;d=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nprint(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['FVQ'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['AHD'],ensure_ascii=False,indent=1))\n\"",
 "description": "List refs dir and inspect KLN/FVQ/AHD metadata"
}
```


### [2026-09-04T18:08:00.317Z] TOOL RESULT

```
AFA.txt
AFM_alt.txt
AFM_pages.txt
AFM.pdf
AFM.txt
AHD_watkins1985.txt
AHM.txt
AID.txt
AIN.txt
AKD.txt
ARB_abdulraheem.txt
ARB_mo3rb.txt
ARP.txt
AVG.txt
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
BRT.txt
BST.txt
CHEUNG.txt
DEV.txt
DOZ.txt
DRM.txt
EAV_studies.txt
FRS_pages.txt
FRS.txt
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
FSF_pages.txt
FSF.txt
FVQ_pages.txt
FVQ.txt
GPL.txt
HENNING_selected_papers.txt
HID.txt
HJB.txt
HRN.txt
HUB.txt
IEC.txt
incoming
ISS_alt_DKS.txt
KFL.txt
KLN_1966.txt
KLN_1971.txt
KNT.txt
LAM.txt
LAT.txt
LEW_1910.txt
LKT.txt
LST.txt
MON_part1.txt
MON_part2.txt
MPP.txt
NAT_2005.txt
---
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
{
 "title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)",
 "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"
 ],
 "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)",
 "covers_etymology": true,
 "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.",
 "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (1938)"
}
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
 "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
}
```


## [2026-09-04T18:08:05.562Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=14 && NR<=17 {print \"=== leaf \" NR-1 \" ===\"; print}' KLN_1966.txt | head -200",
 "description": "Print KLN leaves around p.6"
}
```


### [2026-09-04T18:08:07.528Z] TOOL RESULT

```
<persisted-output>
Output too large (48.2KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b9wpvfj29.txt

Preview (first 2KB):
=== leaf 13 ===
  L.  bassus,  ‘thick,  fat, low’.  See  base,  ‘low’,  and  cp.  the  second  element in  bouillabaisse.
Derivatives :  abas-ed ,  adj.,  abas-ed-ly,  adv.,  abas- ed-ness,  n.,  abase- ment,  n. abash,  tr.  v.,to  confuse;  to  put  to  shame.  —  ME. abassen,  abaissen,  abashen,  fr.  OF.  esbahiss-, pres.  part,  stem  of  esbahir,  ‘to  astonish’,  com¬ pounded  of  pref.  es-  (fr.  L.  ex\  see  1st  ex-)  and a  derivative  of  OF.  baer  (F.  bayer ),  ‘to  gape’, the  change  of  conjugation  (-ir  for  -er)  being prob.  due  to  the  influence  of  the  OF.  adj.  batf.
abasia
abiogenesis
‘astonished’.  The  OF.  verb  baer  derives  fr.  VL. batare,  ‘to  gape,  yawn’.  See  bay,  ‘part  in  the wall’,  and  cp.  words  there  referred  to. Derivatives:  abash-less,  adj.,  abash-less-ly,  adv., abash-ment,  n.
abasia,  n.,  inability  to  walk  ( med .)  —  Medical  L., formed  fr.  priv.  pref.  a-  and  Gk.  Bam?,  ‘stepping, step;  base’,  from  the  stem  of  flaivsiv,  ‘to  go’. See  base,  n.,  and  -ia.
abate,  tr.  and  intr.  v.  —  ME.  abaten,  fr.  OF.  abatre, abattre  (F.  abattre),  ‘to  beat  down’,  fr.  VL.  *ab- balere  (whence  also  It.  abbattere,  Sp.  abatir ), fr.  ab-  and  batere  (L.  battuere),  ‘to  beat,  strike’. See  batter,  ‘to  beat,  strike’,  and  cp.  abatis,  abat¬ toir,  bate,  ‘to  reduce’.
Derivative:  abate-ment,  n. abatis,  n.,  a  defense  made  of  felled  trees  (m/7.)  — F.,  ‘things  thrown  down’,  fr.  abattre,  ‘to  beat down,  throw  down’.  See  prec.  word  and  cp. abattoir.
abattoir,  n.,  a  slaughterhouse.  —  F.,  fr.  abattre, ‘to  beat  down’.  See  abate.  The  subst.  suff.  -oir corresponds  to  L.  -orium,  whence  E.  -ory. abb,  n.,  the  yarn  for  the  woof.  —  OE.  aweb,  ab. See  a-,  ‘on’,  and  web.
abba,  n.,  title  of  honor.  —  L.,  fr.  Gk.  fr.
...
</persisted-output>
```


## [2026-09-04T18:08:12.347Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -E \"^(abba|abbot|aboth|abot|abraham|abram|abner|absalom|abigail|joab|gibbon|borage)[,.]\" KLN_1966.txt | head -30; echo \"=== 1971 ===\"; grep -n -i -E \"^(abba|aboth|abraham|abner|absalom|abigail|joab|gibbon|borage)[,.]\" KLN_1971.txt | head -30",
 "description": "Grep KLN for headwords"
}
```


### [2026-09-04T18:08:12.427Z] TOOL RESULT

```
1137:abba,  n.,  title  of  honor.  —  L.,  fr.  Gk.  fr.
1190:Abner,  n.,  masc.  PN.;  in  the  Bible,  commander of  Saul.  —  Heb.  Abhnir,  lit.  ‘my  father  is  light’, fr.  abh,  ‘father’,  and  ner,  ‘light’;  cp.  the  Baby¬
1217:Abraham,  masc.  PN. ;  in  the  Bible,  the  first  of  the patriarchs  and  father  of  the  Hebrew  nation.
1219:Abram,  masc.  PN.;  in  the  Bible,  former  name  of Abraham.  —  Heb.  Abhrdm,  compounded  of abh,  ‘father’,  and  ram,  ‘high,  exalted’,  which  is prop.  part,  of  rum,  ‘to  be  high,  to  be  exalted  . For  the  first  element  see  Aboth  and  cp.  Abra¬ ham.  From  the  second  element  derive  ramd>', ‘height’  (prop.  fem.  part,  of  rum),  romdm,  ‘ex¬ tolling,  praise;  song  of  praise’,  mardm,  ‘height’, tlrumdh,  ‘contribution,  offering  (for  sacred use)’,  lit.  ‘something  lifted  up,  something  sep¬ arated’.  Cp.  Aram.-Syr.  ram,  ‘was  high’,  Arab. rdma  prop,  ‘he  rose',  hence  ‘he  strove  for’,  and, in  Zanzibar  and  Oman,  ‘he  was  able  to’.  Cp. the  second  element  in  Hiram.
1236:Absalom,  masc.  PN. ;  in  the  Bible,  King  David  s son;  fig.  a  favorite  son.  —  Heb.  Abhshaldm,  lit. ‘father  is  peace’,  fr.  abh,  ‘father’,  and  shaldm, ‘peace’.  See  Aboth  and  shalom. abscess,  n„  a  swelling  in  body  tissues  (med.).  — L.  abscessus,  ‘a  going  away,  departure,  abscess  , fr.  abcedere,  ‘to  go  away’,  fr.  abs-,  ab-,  ‘away from,  from’,  and  cedere,  ‘to  go’.  See  ab-  and cede  and  cp.  cease.
16112:gibbon,  n.,  a  small,  long-armed  ape.  —  F.,  a  name of  Indian  origin  brought  to  Europe  by  the Marquis  Joseph-Frangois  Dupleix  (1697-1763), governor-general  of  the  French  possessions  in India  (1742-54).
20305:Joab,  1)  masc.  PN. ;  2)  in  the  Bible,  the  chief  cap¬ tain  of  David’s  army.  —  Late  L.  Joab,  fr.  Gk. ’lojafi,  fr.  Heb.  Yd'dbh ,  lit.  ‘the  Lord  is  (his) father’.  For  the  first  element  cp.  the  PN’s  Joel, John,  Jonathan,  Joshua,  for  the  second  see Aboth  and  cp.  words  there  referred  to.
=== 1971 ===
4072:abba, n., title of honor. — L., fr. Gk. dpfla, fr. 
4287:Abigail, fem. PN. ; in the Bible, the wife of Nabal, 
4480:Abner, n., masc. PN.; in the Bible, commander 
4484:Aboth, for the second see Menorah. 
4612:Aboth, also Abot,n., 1) the Mishnah treatise also 
4656:Abraham, masc. PN. ; in the Bible , the first of the 
4665:Abraham. — Heb. Abhrdm, compounded of 
4771:Absalom, masc. PN. ; in the Bible, King David’s 
31878:borage, n., a blue-flowered plant used in salads. 
102420:gibbon, n., a small, long-armed ape. — F., a name 
129029:Joab, 1) masc. PN.; 2) in the Bible , the chief cap-
```


## [2026-09-04T18:08:16.127Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4270,4300p;4470,4500p;4600,4640p;4650,4700p;4765,4790p' KLN_1971.txt",
 "description": "Print KLN 1971 Ab- entries"
}
```


### [2026-09-04T18:08:16.206Z] TOOL RESULT

```
abhorrent, adj. — L. abhorrens, gen. -ends, pres, 
part, of abhorrere , ‘to shrink away from’. See 
abhor and -ent. 

Derivative: abhorrent-ly , adv. 
abide, intr. and tr. v. — OE. abidan, formed fr. 
intensive pref. a- and bidan, ‘to remain, await’. 
See bide. 

Derivatives: abid-ing, adj., abid-ing-ly , adv. 
Abies, n., a genus of trees, the true fir {hot) — 
L. abies, ‘silver fir’, cogn. with Gk. < 3 t( 3 t.v (acc.), 
‘silver fir’, * A Pixy;, name of Southern Russia, 
lit. ‘a region of firs’. Cp. abeto. 
abietic, adj., pertaining to the crystalline acid 
C 20 H 30 O 2 (chem.) — Formed with suff. -ic fr. 
L. abies, gen. abietis , ‘silver fir’. See prec. word. 
Abigail, fem. PN. ; in the Bible, the wife of Nabal, 
later of David. — Heb. Abhigdyil, lit. ‘my father 
is rejoicing’, fr. abk, ‘father’ and gil, ‘to rejoice*. 
For the first element see Aboth. The second ele- 
ment is rel. to Arab, jdla, ‘he went round’ and 
to Heb. gdldl, ‘he rolled, unfolded’ ; see gelilah. 
The use of the name in the sense of ‘waiting 
maid’ is due to the passage in I Sam. 25 : 35, where 
Abigail calls herself a ‘handmaid’. 



abigeat, n., cattle stealing {civil law). — L. abi- 
geatus, fr. abigeus , ‘cattle stealer’, fr. abigere , 
See lave and -ion. 

Derivative: ablution-ary, adj. 
abnegate, tr. v., to deny, give up. — L. abnegatus , 
pp. of abnegdre, ‘to refuse, deny’, fr. ab- and 
negare, ‘to say no, deny’. See negate, 
abnegation, n. — L. abnegatio , gen. -dnis, ‘re- 
fusal, denial’, fr. L. abnegatus, pp. of abnegdre. 
See prec. word and negation. 

Abner, n., masc. PN.; in the Bible, commander 
of Saul. — Heb. AbhnSr, lit. ‘my father is light’, 
fr. abh, ‘father’, and ner, ‘light’; cp. the Baby- 
lonian PN. Abunuri. For the first element see 
Aboth, for the second see Menorah. 
abnormal, adj. — A blend of L. abnormis and 
ML. anormalis, this latter itself being a blend 
of L. anomalus and normalis. See anomalous and 
norm and cp. anormal. 

Derivatives: abnormal-ity, n., abnormal-ly, adv., 
abnormal-ness, n. 

abnormity, n. — L. abnormitds, formed with suff. 
-itas fr. abnormis. See prec. word and -ity. 
aboard, adv. and prep. — Formed fr. a-, ‘on’, 
and board. 

Abobra, n., a genus of plants of the gourd family 
(hot.) — ModL., fr. Port, abobora , abobra, 
‘gourd’, fr. L. apopores , apoperes (see Isidorus, 
abortion’, fr. abortus , pp. of aboriri. See abort, v. 
abortifacient, adj. and n., (anything) producing 
abortion. — See prec. word and -facient. 
abortion, n., miscarriage. — L. abort id, gen. -onis, 
‘miscarriage, abortion’, fr. abortus , pp. of abo- 
riri. See abort, v., and -ion. 

Derivatives: abortion-al , adj., abortionist , n. 
abortive, adj., 1) bom prematurely; 2) unsuccess- 
ful. — L. abortivus , ‘pertaining to miscarriage’, 
fr. abortus, pp. of aboriri . See abort, v., and -ive. 
Derivatives: abortive-ly , adj., abort ive-ness, n. 
Aboth, also Abot,n., 1) the Mishnah treatise also 
called Pirke Aboth or The Ethics of the Fathers', 
2) name of the first benediction of the Shemoneh 
Esreh ( Jewish liturgy). — Heb. Abhoth , pi. of 
dbh, ‘father’, rel. to Aram, dbh (absolute state), 



abbd (emphatic state), Ugar. 'b, Arab, ab , 
Ethiop. ab, ‘father’ ; of uncertain origin, possibly 
traceable to *ab(a ), a child’s word for father. 
Cp. the first element in Abraham, Abner, Absa- 
lom, Abigail, and the second element in Joab, 
Moab, Barabbas. Cp. also abbot and words 
there referred to. Cp. also borage, 
abound, intr. v. — ME. abounden , fr. OF. (— F.) 
abonder , fr. L. abundare, ‘to overflow; to a- 
bound’, fr. ab- and unda, ‘wave’. See undate and 
cp. redound, surround. Derivatives: abound-er, 
n., abound- ing , adj., abound-ing-ly, adv. 
about, adv. — ME. abuten, abouten , aboute , fr. 
OE. abutan, onbutan, ‘on the outside of’, formed 
fr. a-, ‘on’, and butan, ‘outside’, which itself is 
formed fr. be, ‘by’, and utan, ‘outside’, fr. ut, 
‘out’. See by and out and cp. but. 

Derivative: about . oren. 

above, adv. — ME. aboven ; fr. OE. abufan , form- 
its name. See abraxas. 

abrade, tr. v., to scrape off. — L. abradere, ‘to 
scrape off’, fr. ab-, and rddere, ‘to scrape off, 
to shave’. See raze and cp. abrase. 

Abraham, masc. PN. ; in the Bible , the first of the 
patriarchs and father of the Hebrew nation. — 
Heb. Abhrahdm, lit. ‘father of the multitude’, 
compounded of dbh, ‘father’, and *rdhdm , 
‘multitude’, which is rel. to Arab, ruhdm, of 
s.m.; see Gen. 17:5. See Aboth and cp. next 
word. 

Abram, masc. PN. ; in the Bible , former name of 
Abraham. — Heb. Abhrdm, compounded of 
dbh, ‘father’, and ram, ‘high, exalted’, which is 
prop. part, of rum, ‘to be high, to be exalted’. 
For the first element see Aboth and cp. Abra- 
ham. From the second element derive ramd h , 
‘height’ (prop. fem. part, of rum), romdm , ‘ex- 
tolling, praise; song of praise’, mdrSm, ‘height’, 
t l rumd h , ‘contribution, offering (for sacred 
use)’. Lit. ‘something lifted up, something sep- 
arated’. Cp. Aram.-Syr. ram , ‘was high’, Arab. 
rdma prop, ‘he rose’, hence ‘he strove for’, and, 
in Zanzibar and Oman, ‘he was able to’. Cp. 
the second element in Hiram. 

Abramis, n., a genus of fishes ( ichthyol .) — ModL., 
fr. Gk. d( 3 pap,ig, ‘bream’, fr. Egyptian rem, 
‘fish’. 

abranchiate, adj., having no gills. — Formed fr. 
priv. pref. a- and branchiate. 

Derivative: abranchiate , n. 
abrase, tr. v., to abrade. — L. abrasus, pp. of 
abradere, ‘to scrape off’. See abrade, 
abrasion, n. — Formed with suff. -ion fr. L. 
abrasus , pp. of abradere. See prec. word, 
abrasive, adj. and n. — Formed with suff. -ive 
fr. L. abrasus, pp. of abradere. See abrade, 
abraxas, n., a mystical word used as a charm. — 
Gk. ’Appa^ag, according to Irenaeus (in Adver- 
sus haereses I, c. 23 and 24) a word formed from 
the Greek letters a, ( 3 , p, a, £, a, a, whose numer- 
ical value amounts to 365 (a = 1, |J — 2, 
p = 100, a = I, £ = 60, a = i, a = 200), cor- 
responding to the number of aeons in Basil idian 
gnosticism and to the number of days in a year. 
ruptness, n. 

Abrus. n., a genus of plants of the pea family 
{bot.) — ModL., for *Habrus, fr. Gk. d( 3 p 6 g, 
‘graceful, delicate’. See habro-. 

Absalom, masc. PN. ; in the Bible, King David’s 
son; fig. a favorite son. — Heb. AbhshalSm, lit. 
‘father is peace’, fr. abh , ‘father’, and shdldm , 
‘peace’. See Aboth and shalom. 
abscess, n., a swelling in body tissues {med.). — 
L. abscessus, ‘a going away, departure, abscess’, 
fr. abcedere , ‘to go away’, fr. abs-, ab-, ‘away 
from, from’, and cedere , ‘to go’. See ab- and 
cede and cp. cease. 

Derivative: abscess-ed, adj. 
abscind, tr. v., to cut off {obsol.) — L. abscindere , 
‘to cut off’, fr. ab- and scindere , perf. scidi, pp. 
scissus (for *scid-tos), ‘to cut, split’. See shed, 
and cp. abscissa, rescind, 
abscissa, n. (math.) — L. {lined) abscissa, lit, ‘(a 
line) cut off’, fem. pp. of abscindere , ‘to tear 
away; to cut off’. (The abscissa of a point P is 
the portion of the x axis cut off by the line 
drawn through P parallel to the y axis.) See
```


## [2026-09-04T18:08:26.855Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '31875,31895p' KLN_1971.txt; echo \"=== 1966 borage/gibbon ===\"; grep -n -i \"borage\" KLN_1966.txt | head; echo ---; sed -n '16108,16120p' KLN_1966.txt",
 "description": "Print Klein borage and gibbon"
}
```


### [2026-09-04T18:08:26.951Z] TOOL RESULT

```
burro); so called in allusion to the red com- 
plexion of intoxicated people, 
boracic, adj., boric. — See borax and -ic. 
borage, n., a blue-flowered plant used in salads. 
— ME., fr. OF. borrace (cp. its variant burage 
and F. bourrache)y fr. ML. borrdgdy ult. fr. 
Arab, abt l drak, lit. ‘father of sweat’, so called 
by the Arab physicians because of its sudorific 
effect. See abbot andc p. arrack, 
boraginaceous, adj. — Formed with suff. -aceous 
fr. ML. borrdgo, gen. bo r rag inis. See prec. word, 
borate, n., salt of boric acid (cheni.) — See boron 
and chem. suff. -ate. 

borax, n., a white crystalline salt used as a flux 
and an antiseptic. — F., fr. Arab, bauraq 
(VArab. bdraq), fr. Pers. bur ah. 
bordage, n., the tenure of a border {Feudal sys- 
tem). — ML. borddgium. See next word and -age. 
bordar, n., tenant {Feudal system). — ML. bor- 
ddrius, fr. borda, ‘cottage’, fr. OF. borde, which 
=== 1966 borage/gibbon ===
1209:Derivatives:  abortion-al,  adj.,  abortion-ist ,  n. abortive,  adj.,  I)  born  prematurely;  2)  unsuccess¬ ful.  —  L.  abortivus,  ‘pertaining  to  miscarriage’, fr.  abortus,  pp.  of  aboriri.  See  abort,  v.,  and  -ive. Derivatives:  abortive-ly,  adj.,  abortive-ness,  n. Aboth,  also  Abot,n.,  i)the  Mishnah  treatise  also called  Pirke  Aboth  or  The  Ethics  of  the  Fathers  ', 2)  name  of  the  first  benediction  of  the  Shemoneh Esreh  ( Jewish  liturgy).  —  Heb.  Abhdth,  pi.  of abh,  ‘father’,  rel.  to  Aram,  abh  (absolute  state), abbd  (emphatic  state),  Ugar.  ’b,  Arab,  ab, Ethiop.  ab,  ‘father’ ;  of  uncertain  origin,  possibly traceable  to  *ab(a),  a  child’s  word  for  father. Cp.  the  first  element  in  Abraham,  Abner,  Absa¬ lom,  Abigail,  and  the  second  element  in  Joab, Moab,  Barabbas.  Cp.  also  abbot  and  words there  referred  to.  Cp.  also  borage, abound,  intr.  v.  —  ME.  abounden,  fr.  OF,  (=  F.) abonder,  fr.  L.  abundare,  ‘to  overflow;  to  a- bound’,  fr.  ab-  and  unda,  ‘wave’.  See  undate  and cp.  redound,  surround.  Derivatives:  abound-er, n.,  abound-ing,  adj.,  abound-ing-ly,  adv. about,  adv.  —  ME.  abuten,  abouten,  about e,  fr. OE.  abutan,  onbutan,  ‘on  the  outside  of’,  formed fr.  a-,  ‘on’,  and  butan,  ‘outside’,  which  itself  is formed  fr.  be,  ‘by’,  and  iitan,  ‘outside’,  fr.  ut, ‘out’.  See  by  and  out  and  cp.  but.
2234:Alkanna,  n.,  a  genus  of  plants  of  the  borage family  (bot.)  —  ModL.,  fr.  Sp.  alcana,  fr.  Arab. al-hinnd',  fr.  al-,  ‘the’,  and  hinnd',  ‘henna’.  See henna.
2693:Anchusa,  n.,  a  genus  of  plants  of  the  borage  fa¬ mily.  —  L.  anchusa ,  fr.  Gk.  avy/jorca,  ‘alkanet’, which  is  of  uncertain  origin, anchylose,  n.  —  See  ankylose. anchylosis,  n.  —  See  ankylosis, anchylotic,  adj.  — -  See  ankylotic. ancient,  adj.,  old.  —  F.  ancien,  fr.  VL.  *antianus, ‘former’,  fr.  ante,  ‘before’ ;  see  ante-.  The  -t  in ancient  is  excrescent  and  is  due  to  a  confusion of  the  ending  of  F.  ancien  with  -ent,  the  English equivalent  of  L.  -ens  (gen.  -entis),  the  pres.  part, sulf.  of  the  II-IV.  Latin  conjugations.  Cp.  pag¬ eant,  peasant,  pheasant,  tyrant.
3484:Amebia,  n.,  a  genus  of  plants  of  the  borage family  (bot.) — Arab,  arnabtya *,  name  of  a  plant, lit.  ‘hare  plant’,  fr.  drnab,  ‘hare’,  which  is  rel. to  Heb.  arnebheth,  Arm.  arnabhtd,  Syr.  ar- nlbhA,  Ugar.  'nhb.  Akkad,  annabu,  ‘hare’.
3492:Derivatives:  arous-al,  n.,  arous-er,  n. a  rovescio,  a  musical  direction  indicating  imita¬ tion  by  contrary  motion.  —  It.,  lit.  ‘upside down’,  fr.  a  (fr.  L.  ad),  ‘to’,  and  rovescio,  ‘re¬ verse,  wrong  side’,  fr.  L.  reversus,  ‘turned  back’, pp.  of  revertere.  See  ad-  and  revert, arpeggio,  n.,  the  playing  of  the  notes  of  a  chord in  rapid  succession  instead  of  simultaneously; a  chord  on  which  the  notes  are  so  played (mus.)  —  It.,  fr.  arpeggiare,  ‘to  play  upon  the harp',  fr.  arpa,  ‘harp’.  See  harp, arpent,  n.,  an  old  French  land  measure.  —  F., fr.  VL.  *arependis,  alteration  of  L.  arepennis, a  Gaulish  word  of  uncertain  origin, arquebus,  n.  —  See  harquebus, arrack,  in  the  East,  a  strong  alcoholic  drink  made from  rice  or  molasses.  —  Fr.  Arab,  ‘araq,  ‘sweat, juice  of  fruit’.  Cp.  rack,  ‘arrack’,  and  borage, arraign,  tr.  v.,  to  call  to  account;  to  bring  before a  law  court.  —  ME.  areinen,  fr.  AF.  areiner, fr.  OF.  araisnier,  aresnier  (F.  arraisonner),  fr. VL.  *arrationare,  fr.  ad-  and  *rationdre,  ‘to reason’,  fr.  L.  ratio,  ‘reckoning,  calculation; reason’.  See  reason  and  cp.  deraign. Derivatives:  arraign,  n.,  arraign-er,  n.,  arraign¬ ment  (q.v.)
3654:Derivatives:  aspers-ed,  adj.,  aspers-er,  n.,  aspers- ive,  adj.,  aspers-ive-ly,  adv. aspersion,  n.  —  L.  aspersio,  gen.  -dnis,  fr.  asper¬ sus,  pp.  of  aspergere.  See  prec.  word  and  -ion. Asperuga,  n,,  a  genus  of  plants  of  the  borage
5360:Borachio,  n.,  name  of  a  drunkard  in  Shakespeare’s Much  Ado  About  Nothing.  —  Sp.  borracho, 'drunk,  intoxicated’,  fr.  L.  burrus,  ‘red’  (see burro);  so  called  in  allusion  to  the  red  com¬ plexion  of  intoxicated  people, boracic,  adj.,  boric.  —  See  borax  and  -ie. borage,  n.,  a  blue-flowered  plant  used  in  salads. —  ME.,  fr.  OF.  borrace  (cp.  its  variant  burage and  F.  bourrache),  fr.  ML.  borrago,  ult.  fr. Arab,  abu  ‘ arak ,  lit.  ‘father  of  sweat’,  so  called by  the  Arab  physicians  because  of  its  sudorific effect.  See  abbot  andc  p.  arrack, boraginaceous,  adj.  —  Formed  with  suff.  -aceous fr.  ML.  borrago,  gen.  borrdginis.  See  prec.  word, borate,  n.,  salt  of  boric  acid  ( chem .)  —  See  boron and  chem.  suff.  -ate.
5384:borrow,  tr.  and  intr.  v.  —  ME.  borwen,  fr.  OE. borgian,  ‘to  lend;  to  borrow’,  fr.  borg,  ‘pledge, security',  rel.  to  ON.  borga ,  ‘to  become  bail  for, to  guarantee’,  MDu.  borghen,  ‘to  protect,  guar¬ antee’,  OHG.  boragen,  borgen,  ‘to  beware  of; to  spare;  to  remit  a  debt',  G.  borgen,  ‘to  bor¬ row;  to  lend’,  biirgen,  ‘to  become  bail  for,  to guarantee’,  OE.  beorgan,  OHG.  bergan,  ‘to  hide, save’.  See  bury.
7038:Cerinthe,  n.,  a  genus  of  plants  of  the  borage family  ( bot .)  — -  ModL.,  fr.  L.  cerintha,  cerinthe, ‘the  waxflower’,  fr.  Gk.  xyjoivIJo:,  ‘beebread’, which  was  prob.  formed  fr.  xvjpoc,  ‘wax’,  with suff.  -ivho;.  See  cere,  n.
8336:comforter,  n.  —  OF.  conforteor,  fr.  conforter.  See comfort,  v.,  and  agential  suff.  -er. comfrey,  n.,  a  plant  of  the  borage  family  —  ME. confine,  cumfirie,  fr.  OF.  confirie,  fr.  con-  (see con-)  and  firie,  ‘liver’  (=  F  .foie),  which  prob. derives  fr.  L.  ( iecur )  ficatum,  ‘liver  (of  a  goose) fattened  with  figs’,  neut.  pp.  of fiedre,  ‘to  fatten with  figs’,  fr.  ficus,  ‘fig’;  see  fig.  The  plant  was so  called  because  of  its  congealing  properties, comic,  adj.  —  L.  comicus,  fr.  Gk.  x(0fxtx6i;,  ‘per¬ taining  to  comedy’,  fr.  xtop.0?,  ‘comic  chorus’. See  comedy  and  -ic.
---
Derivatives:  giant,  adj.,  giant-ess,  n.,  giantism (q.v.),  giant-like,  adj.
giantism,  n.,  pathological  condition  characterized by  abnormal  tallness  (med.)  —  A  hybrid  formed from  prec.  word  with  -ism,  a  suff.  of  Greek  ori¬ gin.  The  correct  form  is  gigantism  (q.v.) giaour,  n.,  a  term  applied  by  the  Turks  to  all  non- Mohammedans.  —  Turk,  giaur,  ‘infidel’,  fr. Pers.  gaur,  a  variant  of  gabr,  ‘fireworshipper’. See  Gheber.
gib,  n.,  a  tomcat.  —  From  Gib,  pet  form  of  the name  Gilbert.
gib,  n.,  a  hook.  —  Of  uncertain  origin, gibbar,  n.,  a  finback  whale  ( obsol .)  —  F.,  fr.  Arab. jabbdr,  ‘giant,  tyrant’,  which  is  rel.  to  Heb.  gibbdr, ‘strong,  mighty;  mighty  man,  hero’.  See  Gabriel, gibber,  intr.  v.,  to  speak  unintelligibly.  —  Of  imi¬ tative  origin.  Cp.  jabber, gibberish,  n.,  unintelligible  talk.  —  Formed  from prec.  word  with  adj.  suff.  -ish. gibbet,  n.,  gallows.  —  ME.  gibet,  fr.  OF.  (=  F.) gibet,  ‘gallows;  a  bent  stick’,  dimin.  of  OF. gibe,  ‘staff,  stick’,  which  is  perh.  of  Teut.  origin; see  Bloch-Wartburg,  DELF.,  p.281  s.v.  gibet. Cp.  jib,  ‘the  projecting  arm  of  a  crane’. Derivative:  gibbet,  tr.  v.
gibbon,  n.,  a  small,  long-armed  ape.  —  F.,  a  name of  Indian  origin  brought  to  Europe  by  the Marquis  Joseph-Frangois  Dupleix  (1697-1763), governor-general  of  the  French  possessions  in India  (1742-54).
gibbose,  adj.,  gibbous.  —  See  gibbous, gibbosity,  n.  —  F.  gibbosite.  See  next  word  and -ity.
gibbous,  adj.  —  L.  gibbosus,  ‘humpbacked’,  fr. gibbus,  ‘hump’,  which  is  of  uncertain  origin.  It
is  possibly  a  loan  word  fr.  Heb.  gibbin,  ‘hump¬ backed’;  see  Heinrich  Lewy,  Die  semitischen Fremdworter  im  Griechischen,  p.  71.  —  lieb. gibben  is  rel.  to  Heb.  gabhndn,  ‘peak,  sum¬ mit’,  Talmudic  Heb.  gabhnun,  ‘humpbacked’, Mishnaic  Heb.  gabhfn,  Aram.-Syr.  gebhiad,  ‘eye¬ brow’,  Arab,  jabtn,  ‘side  of  the  forehead’. Derivatives:  gibbous-ly,  adv.,  gibbous-ness,  n.
gibe,  jibe,  intr.  v.,  to  sneer.  —  Prob.  rel.  to  Du. gijbelen,  ‘to  sneer’,  and  possibly  also  to  ON. geip,  ‘idle  talk’,  geipa,  ‘to  talk  nonsense’. Derivatives :  gibe,  jibe,  n.,  gib-ing-ly,  adv.
giblets,  n.  pi.,  edible  internal  parts  of  poultry.  — ME.  gibelet,  fr.  OF.  gibelet,  ‘game’  (whence  F. gibelotte,  ‘ragout,  stew’),  formed  fr.  *giberet, dimin.  of  OF.  (=  F.)  gibier,  ‘game’,  a  var.  of OF.  gibiez,  fr.  Frankish  *gabaiti,  ‘the  act  of hunting  with  falcons’,  which  is  rel.  to  OHG. bei^an,  ‘to  fly  a  falcon’,  lit.  ‘to  cause  to  bite’ (whence  MHG.  gebeiye  =  Frankish  *gabaiti) fr.  61330/1,  ‘to  bite’.  See  bite.
Gibraltar,  n.,  name  of  the  Rock  at  the  western entrance  to  the  Mediterranean.  —  Fr.  Arab. jabal  (in  vulgar  pronunciation  jebel)  al  Tdriq, ‘mount  of  Tariq’,  named  after  Tariq,  the  Mos¬ lem  invader  of  Spain  who  landed  there  in  71 1. See  javali  and  cp.  Bible.
gibraltar,  n.,  American  name  of  a  hard  (‘rocky’) candy.  —  Named  after  the  fortress  Gibraltar. See  prec.  word.
gibus,  n.,  an  opera  hat.  —  F.,  named  after  its  in¬ ventor,  a  Parisian  hatmaker,  who  lived  in  the 1st  half  of  the  19th  century,
```


## [2026-09-04T18:08:42.024Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['LKT','MON','BQT','HRN','HUB','ARY']:\n  print(k, json.dumps(d[k],ensure_ascii=False,indent=1)[:1500]); print('---')\n\"",
 "description": "Inspect LKT/MON/BQT metadata"
}
```


## [2026-09-04T18:08:42.922Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==62' FVQ_pages.txt",
 "description": "Print FVQ printed page 44"
}
```


### [2026-09-04T18:08:44.104Z] TOOL RESULT

```
LKT {
 "title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927",
 "edition_found": "1927",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/etymologische00lokoguat",
 "identifier": "etymologische00lokoguat",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt",
 "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.",
 "notes": "",
 "cites": "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"
}
---
MON {
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
  "/home/sfmqrb/git/rishe/data/ver
---
BQT {
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={
---
HRN {
 "title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893",
 "edition_found": "1893 (Google scan, Univ. Michigan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/grundrissderneu00horngoog",
 "identifier": "grundrissderneu00horngoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.",
 "notes": "OCR of German Fraktur-free text is decent; Persian script is not OCRed.",
 "cites": "page number of Horn, Grundriss der neupersischen Etymologie (1893); entries are also numbered"
}
---
HUB {
 "title": "H. Hübschmann, Persische Studien, Strassburg 1895",
 "edition_found": "1895 (Google scan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/persischestudie00hbgoog",
 "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt",
 "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.",
 "notes": "Built from djvu.xml (no hocr); OCR quality moderate.",
 "cites": "page number of Hübschmann, Persische Studien (1895)"
}
---
ARY {
 "title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.",
 "kind": "local_scan_ocr",
 "url": "",
 "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"
 ],
 "page_offset": "printed page = pdf page + 1",
 "scans": [
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf",
   "first_printed": 1,
   "last_printed": 546,
   "pdf_offset": -1,
   "lang": "fas+eng",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"
  }
 ],
 "notes": "Image-only PDF provided by the owner (2026-09-04). Use as an additional modern source alongside Wiktionary/Cheung/Hasandust when judging Persian arrows; cite as ARY:<page>. | full OCR text fas+eng (headwords in Persian and Latin 
---
```


### [2026-09-04T18:08:46.359Z] TOOL RESULT

```
44 FOREIGN VOCABULARY OF THE QUR'lN
Burton, Pilgrimage, ii, 175, quotes a Major Price as suggesting
that the word has nothing to do with the birds but is another calamity
in addition, the name being derived from 4x 1 a vesicle. Sprengel
indeed as early as 1794 (see Opitz, Die Medizin im Koran, p. 76), had
suggested a connection of the word with smallpox, deriving it from
^,1 ^father and JA> 1 = lamentation, and stating that the f Persians
^ \^
use the word A^JO I for smallpox. This theory has some support in the
tradition that it was smallpox which destroyed Abrahams army, 1
but it is difficult to see how the word could be of Pers. origin for it
occurs in Pers. only as a borrowing from Arabic, and doubtless from
this passage.
Carra de Vaux, Penseurs, iii, 398, has a suggestion that it is of
Persian origin, and would take the J^y' '- as a s taken reading
for .JA y j = babylonian arrows, which caused the destruction of
the army. The suggestion is ingenious, but hardly convincing, as we
seem to know nothing elsewhere of these JAI y jv.
Apparently the word occurs nowhere in the early literature outside
the Qur'an, unless we admit the genuineness of Umayya's line
5 s S
lj^.JU \jji+* ijXi J>fcj # J^M (W^ a r"' vj*- (Frag. 4,
1. 3, in Schulthess' ed.), where it also means crowds. If it is to be taken
as an Arabic word it may possibly be a case of & U * I A^ j> , especially
in view of the expression quoted from al-Akhfash JAi 1 1 C-4i 1 O*W.
The probability, however, seems in favour of its being of foreign
origin, as Cheikho, Nasrdniya, 471, notes, though its origin is so far
unknown.
/fr*-Jbl J I (Ibrahim).
r* ' *
Occurs some 69 times, cf. ii, 118 ; iii, 30 ; xlii, 11, etc.
Abraham.
1 8cc Sprcnger, Life, 35.
```


## [2026-09-04T18:08:51.664Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==63' FVQ_pages.txt",
 "description": "Print FVQ p.45"
}
```


### [2026-09-04T18:08:53.599Z] TOOL RESULT

```
FOREIGN VOCABULARY OF THE QUB'AN 45
It is always used of the Biblical Patriarch and thus is ultimately
derived from Heb. QmSX. If the name had come direct from the
Heb. we should have expected the form *U^ I, and as a matter of
fact the Muslim philologers themselves recognized that the Qur'anic
form was not satisfactory, for we hear of attempts to alter the form, 1
and an-N,wawI, Taklhlb, 126, gives variant forms *Uj;i ; (%*' J*J 5
and pjtl j\. Moreover we learn from as-Suyutl, Muzhir,
i, 138, and al-Jawallql, 8, that some early authorities recognized it as a
foreign borrowing, al-Marwardi, indeed, informing us that in Syriac
it means /%A>-jiJ (Nawawl, 127), which is not far from the Rabbinic
derivations.
The form p*A\ J\ cannot be evidenced earlier than the Qur'an,
for the verses of Umayya (ed. Schulthess, xxix, 9), in which it occurs,
are not genuine, and Horovitz, KU, 86, 87, rightly doubts the authen-
ticity of the occurrences of the name in the Uxd al-(!hdba and such
works. The form would thus seem to be due to Muhammad himself,
but the immediate source is not easy to determine. The common
Syr. form is ^Sooi-jDJ which is obviously the source of both the Eth.
JMICyjF 1 and the Arm. |J ^mi^mir 2 A marginal reading in Luke i, 55,
in the Palestinian Syriac Lectionary of the Gospels reads J>QjiOl^ul,
but Schulthoss, Lex, 2, rightly takes this as due to a scribe who was
familiar with the Arabic. 3
Lidzbarski, Johanwsbuch, 73, 4 compares the Mandacan DTIX12,
which shortened form is also found as iDOlja[j] in the Christian
Palestinian version of Luke xiii, 16 (Schulthess, Lex, 2), and may be
compared with the +\*J, mentioned in Ibn Hisham, 352, 1. 18, and
the Brahain b. Buriaj whom Horovitz, AT/, 87, quotes from the Safii
inscriptions. The final vowel, however, is missing here. Brockelmann,
1 Sprenger, Leben, i, 06; Sycz, Eigetinamen, 21 ; Margoliouth in MW, xv, 342.
2 Hubschmann, Arm. Gramm, i, 290.
3 The forms *lQjkC7l]^] and SO^O1^1 found in Bar Hebraeus are also
probably of Arabic origin.
4 See also Ephemerw, ii, 44, n. 1.
```


## [2026-09-04T18:09:02.529Z] TOOL CALL #15: Bash

```json
{
 "command": "ls; echo ---; ls data | head -30; echo ---; find . -maxdepth 3 -iname \"*.pdf\" 2>/dev/null | head -20",
 "description": "Look for source PDF"
}
```


### [2026-09-04T18:09:02.598Z] TOOL RESULT

```
CONTRIBUTING.md
data
docs
EtymologicalDictionary-persian-english.epub
EtymologicalDictionary-persian-english.pdf
README.fa.md
README.md
site
tools
---
ANOMALIES.md
extracted
EXTRACTION_SPEC.md
research
translations
verification
---
./EtymologicalDictionary-persian-english.pdf
```


## [2026-09-04T18:09:07.648Z] TOOL CALL #16: Bash

```json
{
 "command": "(pdftotext -f 33 -l 33 -layout EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p33.txt && cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p33.txt) 2>&1 | head -80",
 "description": "Extract PDF page 33 text"
}
```


### [2026-09-04T18:09:09.659Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:09:12.584Z] TOOL CALL #17: Bash

```json
{
 "command": "which pdftotext pdftoppm python3; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p33.txt 2>&1; wc -c /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p33.txt 2>&1",
 "description": "Check pdf tools"
}
```


### [2026-09-04T18:09:12.635Z] TOOL RESULT

```
/usr/bin/pdftotext
/usr/bin/pdftoppm
/usr/bin/python3
-rw-rw-r-- 1 sfmqrb sfmqrb 1 Sep  4 14:09 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p33.txt
1 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p33.txt
```


## [2026-09-04T18:09:16.312Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 33 -l 33 -r 200 -png /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf p33 && ls -la p33*",
 "description": "Render PDF page 33 to PNG"
}
```


### [2026-09-04T18:09:18.392Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 75015 Sep  4 14:09 p33-033.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1 Sep  4 14:09 p33.txt
```


## [2026-09-04T18:09:20.257Z] TOOL CALL #19: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p33-033.png"
}
```


### [2026-09-04T18:09:20.627Z] TOOL RESULT

```

```


## [2026-09-04T18:09:20.625Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-04T18:09:35.839Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 33 -l 33 -r 600 -png /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf p33hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('p33hi-033.png'); print(im.size)\nw,h=im.size\n# Middle Latin box approx x 460-590/1545, y 805-890/2000 in displayed coords -> fraction\nim.crop((int(0.27*w),int(0.39*h),int(0.60*w),int(0.45*h))).save('crop_ml.png')\nim.crop((int(0.42*w),int(0.60*h),int(0.80*w),int(0.66*h))).save('crop_names.png')\n\"; ls crop_*",
 "description": "Crop regions of interest at high res"
}
```


### [2026-09-04T18:09:40.287Z] TOOL RESULT

```
(5100, 6600)
crop_ml.png
crop_names.png
```


## [2026-09-04T18:09:42.415Z] TOOL CALL #21: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_ml.png"
}
```


### [2026-09-04T18:09:42.430Z] TOOL RESULT

```

```


## [2026-09-04T18:09:54.809Z] TOOL CALL #22: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_names.png"
}
```


### [2026-09-04T18:09:54.828Z] TOOL RESULT

```

```


## [2026-09-04T18:09:58.643Z] TOOL CALL #23: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/extracted/batch/page-33.json'))\nfor n in d['entries'][0]['nodes']:\n    if n['id']>=13: print(json.dumps(n,ensure_ascii=False))\n\"",
 "description": "Print JSON nodes 13-16"
}
```


### [2026-09-04T18:10:00.398Z] TOOL RESULT

```
{"id": 13, "parent": 11, "lang": "Hebrew", "refs": "FVQ:44; KLN:6", "words": [{"translit": "Abh-raham", "gloss": "father of the multitude (Abraham)", "script": null}, {"translit": "Abh-ram", "gloss": "high father (Abram)", "script": null}, {"translit": "Abh-ner", "gloss": "my father is light (Abner)", "script": null, "see": ["N.w.r"]}, {"translit": "Ab-šalom", "gloss": "father is peace (Absalom)", "script": null, "see": ["S.l.m"]}, {"translit": "Abh-igayil", "gloss": "father is rejoicing (Abigail)", "script": null}, {"translit": "Yo-abh", "gloss": "the Lord is his father (Joab)", "script": null}], "note": null, "quote": null}
{"id": 14, "parent": 13, "lang": "Arabic", "refs": "FVQ:44", "words": [{"translit": "Abrahim", "gloss": "Abraham", "script": null}], "note": null, "quote": null}
{"id": 15, "parent": 14, "lang": "Persian", "refs": null, "words": [{"translit": "Ebrâhîm", "gloss": null, "script": "ابراهیم"}], "note": null, "quote": {"text": "بت شکستی گیرم ابراهیم وار - کو بت تن را فدا کردن به نار", "poet": "Molavî"}}
{"id": 16, "parent": 13, "lang": "English", "refs": "KLN; AHD", "words": [{"translit": "Abraham, Abram, Abner, Absalom, Abigail, Jaob", "gloss": null, "script": null}], "note": null, "quote": null}
```


## [2026-09-04T18:10:30.969Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN buzine ==\"; grep -n -i -E \"buz[iî]n|bôz|bûzîn|bűz\" HRN.txt | head -20; echo \"== HUB ==\"; grep -n -i -E \"buz[iî]n|bûzîn\" HUB.txt | head -20; echo \"== PHD ==\"; grep -n -i -E \"b(o|ō|u|ū)z(i|ī)n\" PHD.txt PHD_mackenzie.txt | head; echo \"== NYB ==\"; grep -n -i -E \"b(o|ō|u|ū)z(i|ī)n\" NYB_vol2_glossary.txt | head; echo \"== HJB gibbon/monkey ==\"; grep -n -i -E \"^gibbon|bojina|bandar\" HJB.txt | head",
 "description": "Grep Iranian refs for buzine"
}
```


### [2026-09-04T18:10:31.081Z] TOOL RESULT

```
== HRN buzine ==
== HUB ==
3066:dafur buztna, buzina etc. gebraucht.
9718:p. 87, Nr. 842 — 845. Np. buzina (im pi. huzinagan) schon
== PHD ==
== NYB ==
== HJB gibbon/monkey ==
1460:32  5. — Apollo  Bunder.  Mr.  S.  M.  Edwardes  {History  of  Bombay^  Town and  Island^  Census  Report^  1901,  p.  17)  derives  this  name  from *  Pallav  Bandar,' '  the  Harbour  of  Clustering  Shoots.'
2120:Gate.'  The  name  is  said  to  be  a corruption,  and  probably  is  so,  but of  what  it  is  a  corruption  is  not  clear. The  quotations  given  afford  different suggestions,  and  Dr  Wilson's  dictum is  entitled  to  respect,  though  we  do not  know  what  pdlawd  here  means. Sir  G.  Birdwood  writes  that  it  used to  be  said  in  Bombay,  that  ApoUo- bandar  was  a  corr.  of  pa^io-bandar, because  the  pier  was  the  place  where the  boats  used  to  land  pahoa  fish. But  we  know  of  no  fish  so  called ; it  is  however  possible  that  the  paUa or  SaJble-fuiK  ^Hilsa)  is  meant,  which is  so  called  m  Bombay,  as  well  as in  Sind  [The  A^  (ii.  338)  speaks of  ^a  kind  of  fish  callea  vcdwah  which comes  up  into  the  Inaus  from  the sea,  unnvalled  for  its  fine  and  ez- Quisite  flavour,"  which  is  the  Hilsa.] On  the  other  hand  we  may  observe that  there  was  at  Calcutta  in  1748 a  freuuented  tavern  called  the  Apollo (see  Longy  p.  11).  And  it  is  not  im- possible that  a  house  of  the  same name  may  have  given  its  title  to  the Bombay  street  and  wharf.  But  Sir Michael  Westropp's  quotation  below shows  that  PaUo  was  at  least  the native  representation  of  the  name more  than  150  years  ago.  We  may add  that  a  native  told  Mr  W.  G. Pedder,  of  the  Bom1)ay  C.S.,  from whom  we  have  it,  tliat  the  name was  due  to  the  site  having  been  the place  where  the  "po/i"  cake,  eaten at  the  Holi  festival,  was  baked.  And so  we  leave  the  matter.
2122:1847.— "A.  littie  after  sunset,  on  2nd Jan.  1848,  I  left  my  domicile  in  Ambrolie, and  drove  to  the  Ptiawi  bandar,  which reoeiTes  from  our  aooommodatiye  country- men the  more  classical  name  of  Apollo  pier." —  WiUo%,  Lands  of  the  Bible,  p.  4.
2698:BANDAREE,
2712:1548. — ".  .  .  .  certain  duties  collected from  the  bandarys  who  draw  the  toddy {sura)  from  the  aldeas.  .  .  ." — S,  Batelho, Tambo,  203.
2713:1644.— "The  people  ...  are  all  Chris- tians, or  at  least  the  g^reater  part  of  them consisting  of  artizans,  carpenters,  c/umdaris (this  word  is  manifestly  a  mistranscription  of bandaris),  whose  business  is  to  gather  nuts from  the  coco-palms,  and  eoriimbis  (see KOONBEE)  who  till  the  ground.  .  .  ."— BocarrOf  MS.
2715:„  ".  .  .  besides  60  Field-pieces  ready in  their  Carriages  upon  occasion  to  attend the  Militia  and  Bandarines." — Ibid,  66.
2716:c.  1760.—"  There  is  also  on  the  island  kept up  a  sort  of  militia,  composed  of  the  land- tillers,  and  bandarees,  whose  living  depends chiefly  on  the  cultivation  of  the  coco-nut trees."— G^/wc,  i.  46.
2718:1810. — "Her  husband  came  home,  laden with  toddy  for  distilling.  He  is  a  bandari or  toddy-gatherer."— i/aria  Gi-aham,  26.
2734:BANDEL, 'n.p.  The  name  of  the old  Portucuese  settlement  in  Bengal about  a  mile  above  Hoogly,  where  there still  exists  a  monastery,  said  to  be  the oldest  church  in  Bengal  (see  Imp. Gaseteer).  The  name  is  a  Port,  corrup- tion of  bandar,  *  the  wharf ' ;  and  in this  shape  the  word  was  applied  among the  Portuguese  to  a  variety  of  places. Thus  in  Correa,  under  1641-42,  we find  mention  of  a  port  in  the  Red Sea,  near  the  mouth,  called  Bandel dos  Malemos  0  of  the  Pilots ').  Chitta- gong  is  calleci  Bandel  de  Chaiigao  (e.g. m  Bocarro,  p.  444),  corresponding  to Bandar  Chdtgdm  in  the  Autobiog.  of Jahangir  {Elliot,  vi.  326).  [In  the Diarjr  of  Sir  T.  Roe  (see  below)  it  is applied  to  (Gombroon],  and  in  the following  passage  the  original  no  doubt runs  Bandar-i-Hvghll  or  Hngll-Bandar,
```


## [2026-09-04T18:10:32.426Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LKT leaf 70 (p.44) ==\"; awk 'BEGIN{RS=\"\\f\"} NR==71' LKT.txt | head -60",
 "description": "Print Lokotsch p.44"
}
```


### [2026-09-04T18:10:34.045Z] TOOL RESULT

```
== LKT leaf 70 (p.44) ==
n';  hieraus  mit  ar. Art.  sp.  adufe  'dass.',  pg.  adufe  'Schellen- trommel', arfi</"fc'8Vo  [Constancio  Dicc26c]. Wie  die  Kastagnette  arabischer  Herkunft. [DE  50.
538.  Ar.  dnfifa:
'Platte',  vulg.  Form  des  kl.  ar.  daffa; hieraus  mit  ar.  Art.  sp.  pg.  adufa  bei einer  Miihle  die  'Platte,  die  man  in  die Mündung  der  Wasserzuleitung  stellt, damit  das  Wasser  nicht  zur  Mühle  ge- langt'.  [DE  48/50.
539.  Ar.  dahän:
'Rauch',  duhän  sariba  'rauchen',  ebenso tk. ;  hieraus  bulg.  serb.  duhan  'Rauch- tabak', poln.  duchan,  klruss.  dochan, Cech.  dohan  'dass.'.
540.  Tk.  düjme:
'Knopf  [vom  Stamme  tok  >  ttij,  tilj 'binden,  befestigen',  s.  hier  Nr.  528] ; hieraus  hul^.dugme  'dass.,  Knoten',  serb. dugme  'Knopf.    [Bern  SlEtWb  233.
541.  Mal.  düjoug:
[Pijn  113]  'Seekuh,  Halicore  Dujong'  im Indischen  Ozean  [über  sie  vgl.  besonders 0.  Finsch,  Der  Dujong.  Zoologisch- ethnologische Skizze  einer  untergehenden Sirene.  Hamburg  1901.  Sammlung  ge- meinverständlicher wissenschaftlicher
Vorträge.  NF  XV,  359],  auch  H.  taber- naculi  im  Roten  Meere,  H.  austrahs  in Australien,  mit  dem  amerikanischen Manati  [nianatee]  verwandt;  hieraus  frz. dugong,  dougong;  dtsch.  Dugong.  [Devic DEt  1U6/107.  MMM  18.  JAOS  XVH, 135/137.
542.  Ar.  dnkkäu:
'Laden';  \k. ebenso  dükjan;  hieraus  rum. dughiana  'Kramladen';  bulg.  dukan 'Laden',  djukjan  'Werkstätte',  serb.  du- can  'Laden,  Werkstatt',  doganja  'Kauf- mannsladen", russ.  duhan  'Schenke, Bude',  duhanscik.  —  Im  westlichen Afrika  und  Spanien  sprach  man  mit Imäla:  dokkin;  hieiaus  mit  ar.  Art.  sp. adoquin  'viereckige  Steinplatte',  meist als  Pflaster  verwandt,  fig.  'Tölpel'  [zu der  Bedeutungswandlung  vgl.  frz.  tete carrie].  [Gorjajew  99.  Bern  SlEtWb 237.    DE  46/47.
543.  Ar.  düläb:
'Wasserrad,  Bewässerungsmaschine' ; hieraus  vielleicht  sp.  alep  'Mühlrad'. [Eguilaz  151.
544.  Pers.  dulbänd:
'Turban'  [aus  pers.  dil  'Herz'  Horn NpEt  S.  127,  Nr.  571  und  band,  Präsens- stamm von  bästän  'binden'  ebenda  S.  50, Nr. 219;  also  'herzentzückend'];  hieraus l  um.^M^pan'Musseline,  Kopftuch  daraus', tulhent  'Brautschleier',  turban  'Turban', bulg.  serb.  turban,  russ.  tjtirban;  afrz. tolleban,  frz.  turban,  it.  twhante,  sp.  pg. torbante  'Turban';  ndl.  tulband,  engl. turban,  dtsch.  Turban.  —  Aus  demselben Grundwort  ist  der  Name  der  Pflanze Tulipa  Gesneriana  entstanden;  i.  J.  1554 sah  sie  der  kaiserliche  Gesandte  BUS- BECK in  Adrianopel  und  nannte  die  weit offen  stehenden  Blumen  nach  ihrer  Ähn- lichkeit mit  dem  tk.-pers.  Worte  für 'Turban'  [die  Perser  und  Türken  nennen die  Tulpe  übrigens  nicht  so,  sondern peTS.lälä,  tk.lale]:  rv\m.  tuliiyan  [=  la- lea],  it.  tulijxino,  frz.  tulipe,  sp.  pg.  tu- lipa, tulipan;  dtsch.  Tulpe,  ndl.  ftclp, engl,  tulip;  russ.  tjul'pan,  öech.  poln. tulipan.  —  Ableitg.  sp.  torbandalo 'Hammerfisch'.  [ML  8974.  MWiD 11.5/116.
545.  Tk.  dutnan:
'Rauch'  [aus  pers.  düd,  düdmän  Horn NpEt  S.  129,  Nr.  579];  hieraus  bulg. poln.  russ.  tunian  'Nebel',  bulg.  fzma 'dass.'.    [Gorjajew  380.
546.  Tk.  düuibelek:
Auch  tiimbelek  'eine  Art  kleiner  Kupfer- trommel in  Halbkugelform'  [Kelekian Kämüs  417b  mit  ."Abbildung];  hieraus rum.  timbelechiü  'Zimbel,  Schallbecken', timbeleg  in.
Tk.  dilmen.]
44
547.  Tk.  dümeu:
'Steuerruder  [aus  it.  timone];  hieraus bulp.  serb.  dumen,  klruss.  denien  'dass.'. [Bern  SlEtWl)  i2öy.
548.  Tk.  dur-:
Durma  subst.  Intiiiiliv  zu  dtirmak  'blei- ben, stehen'  [vom  Stamme  tw  'vorne, oben,  stellen,  stehen'  Vämbery  TklEtWh S.  184,  Nr.  11)711];  hieraus  serb.  durma 'unaufhörlich'  [wohl  vom  negativen  tk. Stamme  dur-ma-  'nicht  stehen'].  [Bern SlEtWb  239.
549.  Ar.  dürawä: 'Getreidesplitter,  Spreu,  die  beim  Worfeln des  Getreides  abstiebenden  Hülsen'; hieraus  Ober  *dräwa,  *dröwa  die  roma- nischen Formen  sp.  it.di-oga,  irz.drogue; engl,  drugs,  dtsch.  Droge.  [Zahlreiche andere  Ableitungen  sind  vor  allem  be- deutungsgeschichthch  unhaltbar,  so  aus pers.  därü  'Arznei'  Horn  NpEt  S.  116, Nr.  523:  pehl.  därük;  aus  lat.  irochiscus, gr.  TpoxiöKO^  'Pille,  Seifenkugel';  aus ndl.  droog  'trocken';  aus  slav.  doi-gz 'teuer'  Bern  SlEtWb  213;  vgl.  vor  allem BAIST  in  ZffrzSpr  XXXII,  298/39 1.| [Kluge  98.  KLUYVER  in  ZfdWf  XI,  7/10. SEYBOLD  in  ZfdWf  X,  218f.  ZfdU  XV, 335.
550.  Mal.  düri:
'Stachel,  Dorn'  [Pijn  112];  hieraus  dü- rlan  'ein  Baum  Ostindiens,  Durio  zibe- thinus  L.',  der  veegen  seiner  melonen- artigen Früchte,  die  eine  mit  Stacheln versehen
```


## [2026-09-04T18:10:39.974Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E \"^ *4[3-6]\\. \" LKT.txt | head; echo \"=== context ===\"; grep -n -B2 -A12 \"^ *44\\. \" LKT.txt | head -60",
 "description": "Find Lokotsch entry 44"
}
```


### [2026-09-04T18:10:40.030Z] TOOL RESULT

```
313:43.  Ar.  'akar:
315:44.  Ar.  'akida: 'Rosenkonserve,  Bonbon',  plr.  'akiVid; hieraus  tk.  akyde  sekeri  'Karamel),  Ger- stenzucker' [Kelökian  Kämos  855]  od. kurz  akede  [A.  Hindoglu,  Dictionnaire Turc-Fran(;ais.  Vienne  1838.  S.  329]. Wohl  aus  dieser  Form  rum.  acadea, acadele  'dass.'.
316:45.  Ar.  'akika:
318:46.  Ar.  'äkir  karhä :
=== context ===
313-43.  Ar.  'akar:
314-'Grundbesitz,  Immobilien',  plr.  'akärät  ; ebenso  tk.  (A.  Hindoglu,  üictionnaire Türe  FranQais.  Vienne  1838.  S.  328b] al-arat.  Hieraus  rum.  acaret,  acarefuri 'Liegenschaften'.    [Sain  46.
315:44.  Ar.  'akida: 'Rosenkonserve,  Bonbon',  plr.  'akiVid; hieraus  tk.  akyde  sekeri  'Karamel),  Ger- stenzucker' [Kelökian  Kämos  855]  od. kurz  akede  [A.  Hindoglu,  Dictionnaire Turc-Fran(;ais.  Vienne  1838.  S.  329]. Wohl  aus  dieser  Form  rum.  acadea, acadele  'dass.'.
316-45.  Ar.  'akika:
317-'Cornalin',  ein  Edelstein,  der  nach  IBN BAITAR  [gest.  1248  n.  Chr.  in  Damas- kus] den  Blutlauf  im  Körper  aufhält; daraus  sp.  alaqueca,  pg.  laqueca  mit der  heutigen  Bedeutung:  'rot  gefleckter u.  gesprenkelter  Marmor',  wie  er  sich besonders  in  Südamerika  in  kleinen Stücken  findet  [Dicc  Gast  102b;  Con- stancio  Dicc  648a].    [DE  56.
318-46.  Ar.  'äkir  karhä :
319-[Aus  syr.  'akar  kärhä  ZDUG  XLVI,  258] eine  Kamillenart  Anthemis  pyrethrum; über  das  tk.  wurde  hieraus  wohl  runi. cärcü,  cäräu  'echter  Bertram,  Speichel- wurzel'.
320-47.  Ar.  'akrab:
321-'Skorpion'.  Hieraus  sp.  alacran  'dass.' [mit  ar.  Art.  und  Änderung  des  Schluß  b in  einen  anderen  Konsonanten,  vgl. dazu  z.  B.  Calatayud  aus  ar.  KaVat Ajjüh  'Hiobsburg';  Zocodover  (Baedeker, Spanien  u.  Portugal.*  Leipzig  1912. S.  135),  Hauptplatz  in  Toledo,  aus  ar. sük  ad-dawib  'Tiermarkl'] ;  pg.  alacral, alacräo,  lacräo  'dass.'.    [DE  53.
322-48.  Tk.  al:
323-[Vambery  TklEtWb  S.  11 ,  Nr.  10:  al 'rot,  golden,  gelblich']  'hochrot';  hieraus russ.  alyj,  aloj,  bulg.  serb.  al  'rot'.  [Gor- jajew 3.  Bern  SlEtWb  28.
324-49.  Tk.  alacnk:
325-Auch  alaöyk  [nicht  osmanisch]  'Filz- zelt, Rindenjurte'.  Hieraus  russ.  laöuga 'elende  Hütte',  altruss.  alaäuga.  [Bern SlEtWb  682.
326-50.  Tk.  alaga:
327-[Kelekian  Kämos  31]  'gestreifte)',  bunter BaumwoUstofi'  [auch  ins  Ar.  überge- gangen, vgl.  SBKAW  Wien  CHI,  189:  'ge- streifter Stoff  aus  Baumwolle  u.  Seide']; hieraus  rum.  alagea  'feiner  gedruckter Kattun'.
```


## [2026-09-04T18:10:46.143Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LKT abu 'arak / borretsch ==\"; grep -n -i -E \"borretsch|borrago|bourrache|abu.{0,3}'?arak|abu.{0,3}'?araq\" LKT.txt | head -10; echo \"== LKT gibbon ==\"; grep -n -i \"gibbon\" LKT.txt | head",
 "description": "Grep Lokotsch for borage/gibbon"
}
```


## [2026-09-04T18:10:47.459Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HUB 3060-3070 ==\"; sed -n '3060,3072p' HUB.txt; echo \"== HUB 9710-9725 ==\"; sed -n '9710,9726p' HUB.txt",
 "description": "Print Hübschmann buzina context"
}
```


### [2026-09-04T18:10:47.968Z] TOOL RESULT

```
== LKT abu 'arak / borretsch ==
5765:besehein  j.  2210 Beteigetize  St.  695 Betel  2149 betucht  j.  267 Betuchter  j.  267 Betuecliter  j.  267 Bezoar  1605 Bisam  293 ii/Mse  1647 Boback  181 ß��c/i^r  j.  180 Bombasin  16 17 Bonze  331 Borax  356 Boretsch  13 Borretsch  13 £os  j.  184  a Bronze  1657 Burnus  365 Burrich  13 5?<sa  376 Buxkin  324
6380:bouracan  250 i  bournotcs  365 1  bourrache  13 j  boutargue  274 i  bouza  376 j  brodequin  1856 !  bronce  1657 I  bronze  1657 I  brouhaha  256
7425:halascius  151 balsatnum  293 bambagium  1617 Barabbas  220 ftarca  2148 harracanus  250 basilica  (vena)  262 bezoar  1605 birrus  365 bisamutn  293 bombacium  1617 borrago  13 bronzium  1657 brundisinum  Caes)  1657 brunitius  1657 buccina  347 burgns  362 burrus  365
== LKT gibbon ==
```


### [2026-09-04T18:10:48.012Z] TOOL RESULT

```
== HUB 3060-3070 ==
Wort sowohl Lehnwort wie Originalwort sein.
842. Vgl. modern asp i kdtbud *Grausehimmer, Kosen,
Np. Sprachftihrer p. 38.
Hier fehlt np. kaM 'Affe JRAS. 1894, p. 480 = phi.
hapik, arm. LW. kapik, skr. Icapi-. Das Wort ist
in alter Zeit aus dem Indischen entlehnt. Jetzt wird
dafur buztna, buzina etc. gebraucht.
845. Lies afgh. kon (fem. kana *taub'). Vgl. Idg. Forsch.
Ill, 169, Anm.
848. Man erwartet karg, das in den Dialekten (vgl. ZDMG.
32, 535 ; 38, 80) mit kark etc. wechselt. Dazu kas.
karged4n *Nest' (von Menschen gemacht) Shuk. p. 55.
850. Die Bedeutung von zd. kerema- ist ganz unsicher.
== HUB 9710-9725 ==
ZDMG. 36, 73.
p. 78, Nr. 759. Vgl. sayum 'der dritte' Muwaffaq 128, 7; 263,
11 n. 8. w.
p. 79, Nr. 782. Vgl. WZKM. 8, 276.
p. 82, Nr. 800. Np. mdrisBba belegt v. Stackelberg, ZDMG.
48, 494.
p. 83, Nr. 808. Vgl. syr. HIID (in Ardasir-xurrah) ZDMG.
43, 397, Z. 1 (vor 544 p. Chr.).
p. 87, Nr. 842 — 845. Np. buzina (im pi. huzinagan) schon
im alten Korancommentar, JRAS. 1894, 449.
p. 87, Nr. 861. Np. kal (wo vorkommend?) = ka6al *calvus*
= zd. kaurva-, lat. calvus, Geiger, Idg. F.
IV, Anz. 23. Lat. calvus (aus *calovos) zu
skr. kulva-- (in atikulva-) Solmsen, Stndien
zur lat. Lautgesch. p. 136. Idg. Grundform
also klvO'.
p. 89 unten. Hierher np. kahar *hellbraun* (Polak, Persien
```


## [2026-09-04T18:10:57.905Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -A14 \"^ *13\\. \" LKT.txt | head -40",
 "description": "Read Lokotsch entry 13"
}
```


### [2026-09-04T18:10:57.956Z] TOOL RESULT

```
247:13.  Ar.  abü  rag':
248-'Vater  des  Schweißes',  hieraus  lat.  bor- rago,  eine  Pflanze,  die  durch  die  ar. Medizin  im  Mittelalter  verbreitet  wurde. Die  romanischen  Formen  sind:  it.  bor- race,  borragine,  borrana;  prov.  borrage; sp.  borraja ;  pg.  borragem ;  frz.  hourrache. Auch  germanisch,  z.  B.  engl,  borage, dtsch.  Burrich,  Bor( rjetsch.  Wohl  über das  Ngr.  entstand  rum.  boranjä  'dass.'. Trotz  ML  1412  scheint  diese  Ableitung noch  immer  die  beste  und  wenig  an- fechtbar zu  sein.    [Kluge  64.
249-14.  Ar.  abü  tilün:
250-[Vgl.  Ihn  Sinä,  Kitäb  al-känün  fi't-tibb. Romae.  In  typographia  Medicea  1593. S.  137]  'eine  Zierpflanze'  aus  der  Familie der  Malvaceen:  Abutilon  indicum.  Hier- aus frz.  abutilon  'dass.',  nämlich  abutilon striS  Abutilon  striatum  Diks.  (Sida  striata Hort.)  und  abutilon  itendard  A.  vexilla- rium  Ed.  Morrea  (S.  vexillaria  Hort.). [Devic  DEt  3.    Lammens  Rem  3.
251-15.  Pers.  acär:
252-'Sauer',  hieraus  malay.  a£ar  [Pijn  237] in  der  Bedeutung  'Eingemachtes,  pickles' und  ebenso  in  allen  Eingeborenen- sprachen Indiens;  daher  angloind.  achar 'dass.';  frz.  achars  'Obst  od.  Gemüse, das  in  Essig  eingemacht  ist',  ein  im indischen  Archipel,  auf  Mauritius  usw. sehr  beliebtes  Gericht.  [Devic  DEt  3/4. Hobson-Jobson  3.
253-16.  Ar.  'äda:
254-'Sitte,  Gebrauch',  ebenso  Ik.  adet  'dass.'; hieraus  rum.  adet  'Brauch,  Sitte,  Regel', früher  'Steuer'.    [Sain  46.
255-17.  Malayälam  adakka:
256-[Aus  arfa/ 'enge  Anordnung  einer  Traube' und  kay  'Nuß'].  Hieraus  pg.  areca, angloind.  Areca,  worunter  man  allge- mein den  Samen  od.  die  Nuß  der  Palme, Areca  catechu  L.,  versteht.  [Hobson- Jobson  35.
257-18.  Ar.  'adäla:
258-[Aus  ar.  'adl  'Gerechtigkeit']  'Gerichts- barkeit', in  vulgärer  Aussprache  'adälet, woraus  über  das  Hind.  das  angloind. adawlut  'Gerichtshof  wurde.  —  Aus- führlich in  Hobson-Jobson  4/6.
259-19.  Hebr.  Ädäm:
260-'Mensch',  dann  N.  pr.  für  den  Stamm- vater des  Menschengeschlechtes  [vgl. assyr.  admu  'Kind,  bes.  junges  Kind' Del  HWB  25  b],  daraus  bei  den  Ana- tomen des  Mittelalters  hebr.  iappü"h ha-ädäm,  wörtlich  'Apfel  des  Mannes', zur  Bezeichnung  des  Vorsprungs  am Kehlkopf  des  Mannes  [gr.  irpöXoßo;]. Da  er  nur  am  Halse  des  Mannes  zu sehen  ist,  ist  der  Name  treffend  ge- wählt, dann  aber  durch  mißverständ- liche Übersetzung  zu  Pomum  Adami 'Adamsapfel'  geworden  und  die  bekannte Fabel  entstanden,  daß  Adam  den  ihm hingereichten  Apfel  nicht  ganz  habe verschlucken  können.  Ii. morso d'Adamo, frz.  morceau  d' Adam,  pomme  d'Adatn. Engl.  Ada7n's  apple,  schwed.  adanis aepple,  dän.  adams  üble,  ndl.  adanis  appel. Poln.  jabiko  Adamowe,  ßech.  Adamavo jahlko.  Im  Angloind.  ist  Adanis  apple die  Frucht  von  Mimusops  Elengi  L., im  It.  joomo  d'Adamo  [od.  pomo  di  para- diso]  eine  Orangenart,  Citrus  decumana. [Kluge  6.  Hobson-Jobson  4.  HArllebr- An  164.
261-20.  Ar.  'adan ;
```


## [2026-09-04T18:11:17.549Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('LKT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if re.search(r'^\\s*13\\.\\s+Ar\\.\\s+ab', l, re.M):\n        print(\"leaf(0-based)\",i,\"printed ~\",i-26)\n        print(l[-300:])\nEOF",
 "description": "Locate Lokotsch entry 13 page"
}
```


## [2026-09-04T18:11:18.527Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN Affe ==\"; grep -n -i \"affe\" HRN.txt | head -20",
 "description": "Grep Horn for Affe (monkey)"
}
```


### [2026-09-04T18:11:19.161Z] TOOL RESULT

```
leaf(0-based) 28 printed ~ 2
s  zu sehen  ist,  ist  der  Name  treffend  ge- wählt, dann  aber  durch  mißverständ- liche Übersetzung  zu  Pomum  Adami 'Adamsapfel'  geworden  und  die  bekannte Fabel  entstanden,  daß  Adam  den  ihm hingereichten  Apfel  nicht  ganz  habe verschlucken  können.  Ii. morso d'Adamo, frz.  morce
```


### [2026-09-04T18:11:19.209Z] TOOL RESULT

```
== HRN Affe ==
776:39. äfvtden ^schaffen, Praes. afrin-em, afrUegär (AM.);
777:afrtn 1) 'schaffend' 2) 'Lob', vergl. nefnn 'Fluch'.
779:äfritan 'schaffen', afrm 'Lob', nafrm 'Fluch' (AV.);
781:Die Bedeutung 'schaffen' geht nicht über das Pehlevl
2130:aw. [/^varz- 'schaffen, tun'; phlv. varz 'Feldarbeit'
2987:313. pi^fnurden, pezmurden 'erschlaffen, verblühein', pilOTi:!
4623:(302) ; sar. ydtid *Hut, hohe Mütze aus Schaffell'.
4669:*J Bedeutet auch bei Firdüsi 'fleissig, rechtschaffen* wie im
4709:'setzen, machen, schaffen ; phlv. dätan; ai. l^dhä-,
5930:Etwa urspr. 'WafFenarsenar wie auch HNIliNDN (Jer.
6395:732. siristen 'niisclien, vermengen; schaffen, bilden, sirls
6467:schaffen ?
7289:stimmen, das zweifelnd zu gr. xuvvog 'klaffend*, /dog
9866:zu schaffen; doch ist es bisher auch noch nicht
9955:trans. 'raffen, fortraffen, niederstürzen', vergl. Bar-
10481:84. frnrün recht, rechtschaffen , frürümh, sehr häufig.
10685:122. karlnttan 'schneiden; schaffen (von Anröniainyuä)',
10687:aw. iXAar^-, kerentaiti 'schneiden; schaffen'; ai.
11333:230. tf{i)HÜtan 'verunstalten, übel schaffen , v(i)sütak, Men.
11359:236. «äl 'Waffe', AW.-Komm.
```


## [2026-09-04T18:11:27.936Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON بوزینه ==\"; grep -n -o -E \".{80}بوزینه.{120}\" MON_part1.txt | head -8; echo \"== MON بوزنه ==\"; grep -c \"بوزنه\" MON_part1.txt; echo \"== BQT v1 بوزینه ==\"; grep -n -o -E \".{60}بوزینه.{140}\" BQT_v1_pages.txt | head -6; echo \"== BQT v2 ==\"; grep -c \"بوزینه\" BQT_v2_pages.txt",
 "description": "Grep Mo'in and Borhan for buzine"
}
```


### [2026-09-04T18:11:28.036Z] TOOL RESULT

```
== MON بوزینه ==
== MON بوزنه ==
2
== BQT v1 بوزینه ==
== BQT v2 ==
3
```


## [2026-09-04T18:11:31.013Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON بوزنه ==\"; grep -n -o -E \".{100}بوزنه.{160}\" MON_part1.txt; echo; echo \"== BQT v2 بوزینه ==\"; grep -n -o -E \".{100}بوزینه.{160}\" BQT_v2_pages.txt",
 "description": "Show contexts"
}
```


### [2026-09-04T18:11:31.090Z] TOOL RESULT

```
== MON بوزنه ==

== BQT v2 بوزینه ==
```


## [2026-09-04T18:11:35.413Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f,w in [('MON_part1.txt','بوزنه'),('MON_part1.txt','بوزين'),('MON_part1.txt','بوزی'),('BQT_v2_pages.txt','بوزینه'),('BQT_v2_pages.txt','بوزنه')]:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    idxs=[m.start() for m in re.finditer(w,t)]\n    print('###',f,w,len(idxs))\n    for i in idxs[:4]:\n        print(repr(t[max(0,i-200):i+250]))\n        print('--')\nEOF",
 "description": "Python search for buzine in Mo'in and Borhan"
}
```


### [2026-09-04T18:11:37.300Z] TOOL RESULT

```
### MON_part1.txt بوزنه 2
'وز: (۱2۷2)۲0۷2 (.) (جاد.) زنبور سیاه. \nبوز: 2 (ص.) اسب تندرو؛ اسب جلد. \nمرد تیزهوشء» صاحب ادرا کت مق. کودن. \nبوزه: (-)۳۳22 (.) شرابی که از آرد برنج و \nارزن و جو سازند. \n\nبورینه: (6-)۱1212 [- بوزینا - بوزنه - \nبوزنینه ] (.) (جاذ.) میمون. \n\nبوژ: (02۳2)00۷ (.) گرداب. \n\nبوزنه: (م-)هم002 (۱.) شکو فه و هار درخت \nکه هنوز نشگفته باشدء کم. \n\nبوس: ۰" [- بوسه] (ا.) (حامص.) گٌاه در \nترکیب به معنی «بوسی» آید: پابوس. (افاء) \nگاه در ترکیب به معنی («یوسنده) آید:'
--
'لد. \nمرد تیزهوشء» صاحب ادرا کت مق. کودن. \nبوزه: (-)۳۳22 (.) شرابی که از آرد برنج و \nارزن و جو سازند. \n\nبورینه: (6-)۱1212 [- بوزینا - بوزنه - \nبوزنینه ] (.) (جاذ.) میمون. \n\nبوژ: (02۳2)00۷ (.) گرداب. \n\nبوزنه: (م-)هم002 (۱.) شکو فه و هار درخت \nکه هنوز نشگفته باشدء کم. \n\nبوس: ۰" [- بوسه] (ا.) (حامص.) گٌاه در \nترکیب به معنی «بوسی» آید: پابوس. (افاء) \nگاه در ترکیب به معنی («یوسنده) آید: \nآستان\u200cبوس. بوسه و کنار: بوسیدن و در \nآغوش کشیدن. \n\n\nبوستان: 0۷-۲ '
--
### MON_part1.txt بوزين 0
### MON_part1.txt بوزی 5
'درخت. \n\nبوز: (۱2۷2)۲0۷2 (.) (جاد.) زنبور سیاه. \nبوز: 2 (ص.) اسب تندرو؛ اسب جلد. \nمرد تیزهوشء» صاحب ادرا کت مق. کودن. \nبوزه: (-)۳۳22 (.) شرابی که از آرد برنج و \nارزن و جو سازند. \n\nبورینه: (6-)۱1212 [- بوزینا - بوزنه - \nبوزنینه ] (.) (جاذ.) میمون. \n\nبوژ: (02۳2)00۷ (.) گرداب. \n\nبوزنه: (م-)هم002 (۱.) شکو فه و هار درخت \nکه هنوز نشگفته باشدء کم. \n\nبوس: ۰" [- بوسه] (ا.) (حامص.) گٌاه در \nترکیب به معنی «بوسی» آید: پابوس. (افاء) \nگاه در ترکیب به معنی («یوس'
--
'انکه سک به پای صاحب خود.) (کن.) \nتنییه کسی به وسیله دشنام» کتکث یا جر یمه. \nپوزه: (0-)ع۳م [- پوز] (.) پیرامون دهان» \nگرداگرد دهن حبوانات. جانه. \nپوریدد. ۳۱2-0 آفس. بورس ] (مص\u200cل.) \n(بوزبد» بوزد» خواهد بوزید» سوزه بوزنده» \nبوزیده. پوزش) زدودن» راندن» برطرف \n\n\nکردن(۲). معذرت خواستن» عذر خواستن. \nپوساندن: 19-1( [- بوسانیدن] \nسوسان» بو ساننده» بوسان» بوسانده). \nیوسانیدن: مج موه عنام [- بوساندن| \nپسوسانید» بسپوسان» پوساننده» پوسان» \nبوسانیده). سوسیدن د'
--
'ود.) (کن.) \nتنییه کسی به وسیله دشنام» کتکث یا جر یمه. \nپوزه: (0-)ع۳م [- پوز] (.) پیرامون دهان» \nگرداگرد دهن حبوانات. جانه. \nپوریدد. ۳۱2-0 آفس. بورس ] (مص\u200cل.) \n(بوزبد» بوزد» خواهد بوزید» سوزه بوزنده» \nبوزیده. پوزش) زدودن» راندن» برطرف \n\n\nکردن(۲). معذرت خواستن» عذر خواستن. \nپوساندن: 19-1( [- بوسانیدن] \nسوسان» بو ساننده» بوسان» بوسانده). \nیوسانیدن: مج موه عنام [- بوساندن| \nپسوسانید» بسپوسان» پوساننده» پوسان» \nبوسانیده). سوسیدن داشتن» بوسیده کردن» \nت'
--
'(اخ.) \nشادی: 120-7 (حامص.) خوشحالی؛ \nشادمانی» مسرت. به سلامتی (به هنگام \nنوشیدن باده به یاد عزیزی یا دوستی گویند). \n(احح, نت.) فرح. شادی ستاره: (ا<. نح.) \nفرح کوکب (مقدمه التفهیم ص قسط). (ا.) \nمیمون» بوزینه. \n\nشادیانه: (م»)د«-01: (امر.) آنچه که از \nروی شادی باشد. (ص.) شاد» شادمان. (.) \nعیش؛ طرب. \n\nشاد یجه: (201«)0: (امر») بالا پوش» \nلحاف. \n\nشاد: (352)2 [ع.] (افا.) نادر» کمیاب. \n\nشار: 27 (- شهر» قس. شارستان] شهر» \nمدینه. کشور» مملکت: ایران\u200cشار (- '
--
### BQT_v2_pages.txt بوزینه 3
'اروانك باشد که پرنده\u200cاست شبیه\u202c         \u202bافزاری باشد که بدان پنبه دانه ازینبه جدا کنند\u202c\n                                   \u202bبمرغ خانگی \u202a.\u202c\u202c     \u202bوواه از\u202c \u202bخواء آزرا اآزهن ماخته باشند خ\u202c\n \u202bچلوین سبروزن بوزینه\u202a ,\u202cبمعنی\u200cچوینك\u202c                                                           \u202bچوب \u202a.۷\u202c\u202c\n \u202bاست کهروپاکهسرخ \u202a -\u202cو لقب بهرام چویین \u202a-\u202c\u202c                   \u202bجو فلت بابای فارسی ولام » بورزن\u202c\n\n\n              \u202b\u202a.\u202c\u202c   \u202bچش \u202a :\u202cسوج\u202c   \u202b(\u202a)۲\u202c\u202c         \u202b(\u202a )۱'
--
'دور دنه \u202a ۰ ۷\u202cبا زای فارسی وتحتانی\u200cبر\u202c\n                                    \u202b\u202a. _ ۵\u202c\u202c\n                                                            \u202bمز مار خوانند \u202a - ۳\u202cوبا ثانی\u200cمجهول دو ژاننده را\u202c\n\u202bوزن بوزینه\u202a ,\u202cبمعنی\u200cدوزنه است که یش جانوران\u202c                                                           \u202bکویتت \u202a۴\u202c\u202c\n                                     \u202bگز نده باشد \u202a۰\u202c\u202c\n                                                             \u202bدودخ؟ = معروف است و آن'
--
' بروزن شفتالو\u202a,\u202c\u202c                       \u202b\u202a -\u202cو بمعنی بسیار همآمده است کهعربان کثیر\u202c\n                                                                                                    \u202bخوانند \u202a. ۴\u202c\u202c\n\u202bبوزینه راگوبند \u202a .\u202cو آن نوعی از میمون باشد\u202a-\u202c\u202c\n                                                           \u202bنون وبایاسعد\u202a:\u202c\u202c   \u202bعم اول وسکون\u202c             \u202bس۔\u202c\n\u202bو بزیبان هندی نام درختی است که کل و ب رکه\u202c\n                          \u202bنآرا ددوراها بکار برن'
--
### BQT_v2_pages.txt بوزنه 0
```


## [2026-09-04T18:11:51.418Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,glob\nfor f in ['incoming/ARY/ARY_pages.txt','incoming/ARY/ARY_latin_index_pages.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for w in ['بوزینه','بوزین','میمون']:\n        idxs=[m.start() for m in re.finditer(w,t)]\n        print('###',f,w,len(idxs))\n        for i in idxs[:3]:\n            print(repr(t[max(0,i-150):i+200]));print('--')\nEOF",
 "description": "Grep Aryanpur for buzine"
}
```


### [2026-09-04T18:11:53.831Z] TOOL RESULT

```
### incoming/ARY/ARY_pages.txt بوزینه 0
### incoming/ARY/ARY_pages.txt بوزین 0
### incoming/ARY/ARY_pages.txt میمون 0
### incoming/ARY/ARY_latin_index_pages.txt بوزینه 0
### incoming/ARY/ARY_latin_index_pages.txt بوزین 0
### incoming/ARY/ARY_latin_index_pages.txt میمون 0
```


## [2026-09-04T18:11:59.427Z] TOOL CALL #36: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T18:11:59.437Z] TOOL RESULT

```


```


## [2026-09-04T18:12:03.454Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%B2%DB%8C%D9%86%D9%87",
 "prompt": "Give the full Persian entry for بوزینه: etymology (any Middle Persian / Proto-Iranian ancestor, any cited scholars such as Hasandust or Cheung), meaning, and any mention of Arabic abu zina."
}
```


## [2026-09-04T18:12:04.542Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/borage",
 "prompt": "Full etymology of \"borage\" — all proposed origins including Arabic abu araq and Latin burra."
}
```


### [2026-09-04T18:12:09.184Z] TOOL RESULT

```
# Persian Entry for بوزینه

**Word:** بوزینه (būzīna / buzine)

**Meaning:** Monkey; ape

**Etymology:** The entry indicates the word is "inherited from Proto-Iranian" but does not specify the exact Proto-Iranian form (marked as "[Term?]"). It notes comparison with Pashto بيزو (bízo, "monkey"). The term was "anciently borrowed into Old East Slavic обезьꙗ́на (obezĭjána)" and likely into Old Turkic 𐰋𐰃𐰲𐰃𐰤 (béčin, "monkey").

**Scholars:** The entry does not cite Hasandust, Cheung, or other specific scholars regarding etymology.

**Arabic Connection:** The entry contains no mention of Arabic "abu zina" or any Arabic etymological connection.

**Synonyms:** میمون (meymun), کپی (kapi)

**Citation:** The word appears in Rumi's 13th-century Masnavi-ye-Ma'navi with the meaning "ape."
```


### [2026-09-04T18:12:10.440Z] TOOL RESULT

```
# Borage Etymology

According to the Online Etymology Dictionary, borage entered English in the mid-13th century from Anglo-French *burage* and Old French *borage*, ultimately deriving from Medieval Latin *borrago*.

## Competing Theories

**Arabic Origin (Folk Etymology):**
Folk etymologists proposed the word came from Arabic *abu arak*, meaning "the father of sweat," allegedly named by Arab physicians for its diaphoretic effects. However, modern scholars largely reject this explanation.

**Latin Origin (Preferred):**
The Oxford English Dictionary and other sources favor a Latin derivation, suggesting the word traces to Latin *borra*, which refers to "rough hair, short wool," describing the plant's hairy foliage texture.

The term spread across European languages, appearing as Spanish *boraja*, Italian *borraggine*, and German *Boretsch*. The plant itself is a blue-flowered herb traditionally used in salads and culinary applications.
```


## [2026-09-04T18:12:23.706Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/gibbon",
 "prompt": "Full etymology of \"gibbon\" — the French source, Dupleix, any Indian/Hindi word proposed."
}
```


## [2026-09-04T18:12:24.736Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/gibbon",
 "prompt": "Full etymology of English \"gibbon\" (the ape) — French source, any Indic/Bengali/Hindi origin proposed, any mention of Persian buzine or Arabic."
}
```


### [2026-09-04T18:12:29.507Z] TOOL RESULT

```
# Etymology of "Gibbon"

## Origin and Development

The term "gibbon" entered English in 1770 from French *gibbon* (18th century). According to the etymology source, the French word's origin is uncertain: it is "supposedly from a word in the French colonies of India but not found in any language there."

## Key Historical Figure

The word was introduced to Europe through **Marquis Joseph-François Dupleix** (1697-1763), who served as "French governor general in India 1742-54" and brought these long-armed apes from the East Indies to Europe.

## No Confirmed Indian Source

Notably, despite the word's apparent connection to India, etymological research has not identified a corresponding term in any actual Indian language or dialect that would explain the French borrowing.

## Surname Connection

Interestingly, the surname "Gibbon" has a separate European origin, deriving from "Old French *Giboin*, from Frankish *\*Geba-win* 'gift-friend,'" or potentially from diminutives of the name Gilbert.
```


### [2026-09-04T18:12:30.793Z] TOOL RESULT

```
# Etymology of "Gibbon"

Based on the Wiktionary entry, here's the documented etymological path:

**English Origin:** The word "gibbon" came through a "reborrowing from French," involving folk etymology. The ultimate source traces to a Northern Aslian language, with the Batek language showing *kəboɲ* as a cognate.

**French Origin:** French acquired the term when it was "brought to Europe from French India by Joseph François Dupleix," again through folk etymology connected to an Aslian root.

**No Indic/Persian/Arabic Origins Found:** The provided text contains no mention of Bengali, Hindi, Persian *buzine*, or Arabic etymological connections. The only languages cited as sources are the Aslian language family (specifically Batek) from Southeast Asia. The "folk etymology" references suggest the word's path became obscured through cultural transmission, but no alternative Indic or Middle Eastern origins are documented in this source.
```


## [2026-09-04T18:12:38.286Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=borage",
 "prompt": "Give the American Heritage Dictionary entry for \"borage\", especially its etymology line in full."
}
```


## [2026-09-04T18:12:39.600Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/%CA%BEab-",
 "prompt": "Give the Proto-Semitic reconstruction for 'father': the form, meaning, and the descendants listed (Arabic, Hebrew, Aramaic, Akkadian, Ge'ez, Ugaritic)."
}
```


### [2026-09-04T18:12:42.080Z] TOOL RESULT

```
# Borage Entry from American Heritage Dictionary

**Definition:** Borage is "an annual bristly herb (Borago officinalis) native to the Mediterranean region, having blue or purplish star-shaped flowers, edible leaves and stems, and seeds containing oil used as a dietary supplement."

**Etymology:** The word traces back through Middle English and Old French *bourage* to Medieval Latin *borāgō*, likely deriving from Arabic *bū'araq*. The Arabic root combines *'abū* (father, source) and *'araq* (sweat), reflecting the plant's historical use as a sudorific agent.
```


### [2026-09-04T18:12:44.291Z] TOOL RESULT

```
# Proto-Semitic Reconstruction for "Father"

**Form:** *ʔabw- (masculine noun)

**Meaning:** "father"

**Key Descendants:**

- **Arabic:** أَب (ʔab)
- **Hebrew:** אָב (av)
- **Aramaic:** אַבָּא (ʾabā')
- **Akkadian:** abum
- **Ge'ez:** አብ (ʾäb)
- **Ugaritic:** 𐎀𐎁 (ʾabu)

The entry notes that this term derives from Proto-Afroasiatic and is "ultimately an onomatopoeic nursery word," with cognates appearing across multiple language families including Egyptian, Proto-Berber, and Hausa.
```


## [2026-09-04T18:12:52.973Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D8%A8",
 "prompt": "Give the Arabic entry أب: etymology (Proto-Semitic), the root, the construct/nominative forms ab, abū, abī, and any note on the root ء ب و."
}
```


## [2026-09-04T18:12:55.050Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A5%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9%85",
 "prompt": "Give the Arabic entry إبراهيم: etymology — from Hebrew or Syriac? any mention of Syriac ʾAḇrāhām, Greek Abraam, and the Persian descendant."
}
```


### [2026-09-04T18:12:57.599Z] TOOL RESULT

```
# Arabic Entry: أب (Father)

**Etymology:** Inherited from Proto-Semitic *ʔabw- ("father")

**Root:** ء ب و (ʔ b w) — contains 7 related terms

**Key Forms:**
- Nominative singular: أَبٌ (ʔabun)
- Construct singular: أَبُو (ʔabū)
- Genitive singular: أَبٍ (ʔabin)

**Root Note:** The entry indicates this word "belongs to the root ء ب و" and traces back through Proto-Semitic origins, showing cognation with Hebrew אָב (áv, meaning father).
```


### [2026-09-04T18:12:59.468Z] TOOL RESULT

```
# Etymology of إبراهيم

Based on the Wiktionary entry, the etymology states: "Borrowed from Aramaic אַבְרָהָם (ʾaḇrāhām)."

The page does not mention Syriac, Greek, or Persian as direct sources for the Arabic term. However, it does show an etymology tree indicating the word was borrowed from **Aramaic**, with Biblical Hebrew אַבְרָהָם also listed in the chain.

Regarding Persian descendants, the entry lists Classical Persian as a descendant language that received the word from Arabic: "Classical Persian: ابراهیم (ibrāhīm)."

The entry does not provide information about Greek "Abraam" or discuss Syriac ʾAḇrāhām as separate etymological sources for the Arabic form.
```


## [2026-09-04T18:13:07.751Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Abraham",
 "prompt": "Give the etymology of the English name Abraham: Hebrew Aḇrāhām, the Genesis 17:5 folk etymology 'father of a multitude', what modern scholars say (e.g. that it is a dialectal variant of Abram, or contains Aramaic/Arabic ruhām), and the Greek/Latin route."
}
```


## [2026-09-04T18:13:11.689Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nfor w in ['بوالهوس','ابوی','ابوعلی','ابوالفضل']:\n    idxs=[m.start() for m in re.finditer(w,t)]\n    print('###',w,len(idxs))\n    for i in idxs[:2]:\n        print(repr(t[max(0,i-150):i+200]));print('--')\n# Abu entry\nfor m in list(re.finditer(r'ابو[:\\s]',t))[:5]:\n    i=m.start(); print('ABU>',repr(t[max(0,i-100):i+250]))\nEOF",
 "description": "Grep Mo'in for abu / bulhavas"
}
```


### [2026-09-04T18:13:13.609Z] TOOL RESULT

```
# Etymology of Abraham

**Hebrew Origin:**
The name comes from Biblical Hebrew אַבְרָהָם ('aḇrāhām). According to Genesis 17:4–5, it was glossed as "father of" (אַב, aḇ) + "multitude of" (הֲמוֹן, hăˈmōn), yielding the folk etymology "father of many nations."

**Modern Scholarly Interpretations:**
Thomas L. Thompson suggests the original meaning was actually "Father is exalted," noting that Genesis's interpretation may reflect forgotten etymology due to the name's age. Alternatively, scholars propose Abraham represents a dialectal variant of Abram, or contains elements from Aramaic or Arabic ruhām.

**Classical Route:**
The name traveled through Ancient Greek (Ἀβρᾱᾱ́μ, Abrāā́m), then into Late Latin (Ābrahām), and subsequently into Old English and other European languages, establishing the form used in modern English.
```


### [2026-09-04T18:13:15.306Z] TOOL RESULT

```
### بوالهوس 0
### ابوی 8
' زمان به \nرنگی نماید. جانوری است شبیه به چلپاسه. \n(کد.) مردمی که هر ساعت خود را به رنگی \n\n\nباب به همه \n\n\nبیارایند. (کد.) دنیا. سنگ پشت. مرغی \nاست؛. \n\nابوی: 202۷ [ع.] (ص\u200cنست.) منسوت به ات \nپدری. (عم.) در تداول» فارسیان این کلمه را \nبه معنی پدر بکار برند و ابوی من» ابوی تو \nابوی او گویند و بدین معنی در بعضی \nنوشته\u200cها هم بکار رفته است. \n\nابوین: و202۷ '
--
'بیارایند. (کد.) دنیا. سنگ پشت. مرغی \nاست؛. \n\nابوی: 202۷ [ع.] (ص\u200cنست.) منسوت به ات \nپدری. (عم.) در تداول» فارسیان این کلمه را \nبه معنی پدر بکار برند و ابوی من» ابوی تو \nابوی او گویند و بدین معنی در بعضی \nنوشته\u200cها هم بکار رفته است. \n\nابوین: و202۷ [ع. - ابوان] (.) تئنبة اب» \nوالدین» بدر و مادر. \n\nابه: (-)«دن2 [تر .] (ا.) طایفه و ایلی از ترکث. \nابهام: '
--
### ابوعلی 1
'. امر.) نگهدارندة \nاسب و اموال» نگهبان. \nبنوت: 020۷۷26 [ع. . بو 8] (امص.) پسر \nسر خواندگی. اضافه نوت: 7 ۲ \nپسر یا نوه بنام پدر یا جد: محمود سبکتکین» \nابوعلی سینا. \nبنوره: (00-۷21266 [قس. بنلاد؛ بنیاد] \n\n\n۳۹۰ \n(امر.) بنای عمارت و دیوار؛ نناد؛ بنلاد. \nبنوه: (00۳۷2)6 [- بنو] (۱.) خرمن غله و کاه \n۴۱ غیر ۵. \n\nنوی: ]9202۷ [ع.] (ص\u200cنسب.) منسوب به \nابن؛ پسر'
--
### ابوالفضل 1
'ب بازماندگی \nاز مدآ باشد. \n\nدام: 00 (هند.] (ا.) سکه\u200cای مسین در \nهندوستان که نخستین بار در زمان شیر شاه و \nجانشینانش از سلسلةٌ سوری ضرب شد. بنابه \nقول ابوالفضل بن مبارکك ۲۹۰ دام یکث \nمهر و ۴۰ دام یکث روپیه بود. \n\nداماد: 0 (.) مردی که تازه جشن \nعروسی وی برپا شود مرد تازه زن گرفته. \nشوهر دختر شخص. شوهر خواهش شخص. \nدامادی: ا 07 (حامص.) ازدواج» \nزناشویی'
--
ABU> '\nجزیرةٌ موریس روید. چوب آن سیاه» \nسخت» سنگین و گرانبها است. \n\nآبو: 5 [- آبی] (.) (گی.) نیلوفر آبی. \nابو: 20 [- آبی ] (ص. ا.) برادر مادر» خال» \n\n\nآب\u200cورز: 20-7 (افا.) آب\u200cباز» ها که \nغواص. ملاح. \n\nآب\u200cورنگ: 2-0-68 (امسر.) (نسق.) \nرنگ\u200cهای خشکك شده و رنگ\u200cهای آمیخته \nبا آب و مواد چسبنده» که به وسیلةٌ قلم موی \nمخصوص به روی کاغذ یا پارچة ابریشمی \nکشند» آب ر'
ABU> 'نهند و در هوا چرخانند تا مشتعل \nتر دا آتش چرخان» آتش سرخ\u200cکن. \n\nزک شمن ۰ «0701127:-.2 (مص\u200cل.) مشتعل \nابو وه آتش در آن افتاده \nباشد. .(عم.) خشمگین شدن» فغضبا ک \nگردیدن. \nآتشگون: 5-0 (ص\u200cمر.) به رنگ رن \nآتشفام» آتش رنگه آذرگون. \nاتشگیره: (0-)72]و-.2 (امر .) آنچه با 1 \nآتش افروزند (مانند پنبه» خار» هیزم)؛ آ نکن \nافروزنه. چخماق. \nاتشبناک: ...2 (رص مر .) '
ABU> ' مسلاه (ع. .] (ص.) گنک گنک لاج \n(در تازی 7 آن بکماء و جمعش بکم \nاست.) \nابل: 200 (ا.) (تد. عم.) مخفف ابو القاسم و \nاب والفضل و مانند آنها (قس. . بلقاسم و \nبلفضل در نوشته\u200cهای پیشینیان و در تداول \nعوام امل مخفف ام\u200cالبنین و جز آن). (تد. \n۳ نره» احلیل» کیر. \nابل: ۱ [ع.] (ا.) نامی است جمله شتران \nراء اشتران مش از دوه (جمع بی\u200cمفر د با اسم \nجنس به اعتبار و'
ABU> 'ه\u200cها» بنیان\u200cها» اصل\u200cهاء \n\n\nقواعد. صیغه\u200cها (درصرف). ابنیه تاربخی \nبناهای عتیق» ساختمان\u200cهای تار بخی. \nابو: 0 [ع.] (از اسماء سته) (.) اب» بدر» \nضح.- در عربی درحالت رفعی این کلمه را \nنصورت رانو» و در حالت نصبی «اتا» و در \nحالت جری «ابی, گویند و غالباً در آغاز \nکنيةٌ مردان در آبد مانند راین» و گاه در آغاز \nبعضی اسم\u200cهای جنس. فارسی زانان رعابت \nحالت\u200cهای س'
ABU> 'ی. \n\nبابک: ۱2۳-۴ [مصف. باب] (.) پدر (به \nتحبیب). \n\nبابل: ۵1 (.) مغرب؛ مق. خراسان به \nمعنی مشر ق. \n\nبابو: 205 رقس. باب] (.) پدر بابا. بزرگ \nقلندران و درویشان. به معنی بابا که در اوایل \nاسماء برای شفقت با مجرد تلقیب افزایند و \nگویند. \n\nبابونه: (۵-)02ا0ق0 | بایونج؛ معر.] (.) \n\n\n۳۳۴ \n\n\nفرهنگ فارسی معین بایی \n\n\n(گیا.) گیاهی از تیرة مرکبیان که پایا است و'
```


## [2026-09-04T18:13:32.389Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('p33hi-033.png'); w,h=im.size\nim.crop((int(0.55*w),int(0.135*h),int(0.80*w),int(0.185*h))).resize((int(0.25*w*1.5),int(0.05*h*1.5))).save('crop_abu.png')\n\"",
 "description": "Crop Persian abu box"
}
```


### [2026-09-04T18:13:34.535Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:13:36.527Z] TOOL CALL #48: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_abu.png"
}
```


### [2026-09-04T18:13:36.546Z] TOOL RESULT

```

```


## [2026-09-04T18:13:57.305Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in SKT.txt FSD_vol1.txt FSD_vol2.txt WEB_vol1.txt; do echo \"=== $f borage ===\"; grep -n -i -m2 -E \"borage\" $f | cut -c1-600; echo \"=== $f gibbon ===\"; grep -n -i -m2 -E \"gibbon\" $f | cut -c1-600; done",
 "description": "Grep English dictionaries for borage and gibbon"
}
```


### [2026-09-04T18:13:59.120Z] TOOL RESULT

```
=== SKT.txt borage ===
2091:Borate.  (F.  — I^wL,)  Fonnerly  iv»r- ^f».  —  y.  Ifourraihe.  —  Low  L.  terraginem^ ace.  of  hcrrago,  borage ;  prob.  named  from iU  roughnesa.  Pcrfaaps  from  Low  L.  hprra, htma,  rotigfa  hatr  (whence  F.  iomrrt,  Ital. ^rrtt);  ice  BurL
=== SKT.txt gibbon ===
=== FSD_vol1.txt borage ===
15555:»   na-ca-hu!'te*vrood",  1   a'na-ka-hwl't5-wud';  2   S'nfi-ea- nwrte-wood*,  n.  [Sp  Am.)  The  wood  or  a   Mexican  tree ICordtn  bolssler f)  of  the  borage  family  (Borapinacex).  In great  repute  about  I860,  especially  among  the  Germans,  as a   specific  for  consumption.
15655:away  (Ehretia  elliplica),  a   tree  of  the  borage  family  (Bo-  k.n„hl,h  ..  .   .   .
=== FSD_vol1.txt gibbon ===
10061:Gibbon  Rome  vol.  i,  ch.  2,  p.  103.  W.  a   c.  1880.]
12215:Gibbon  Home  vol.  i,  p.  245.  [j.  a.  a.  18S0.] (2)  Connection  of  families  by  marriage.
=== FSD_vol2.txt borage ===
4861:echT-tIn,  1   eU'i-tln;  3   ec'l-tln,«.  A   colorless,  crystalline,  dex-  A   Scottish  naval  architect;  constructed  United  States  lake trorotatory  compound  (C  aaHsaO  s)  contained  In  dita-bark.  fleets  In  the  War  of  1812;  builder  of  Turkish  navy-yard  In Ech'I-um,  lek'i-Tjm:26e'l-Qm,  re.  iJof,  A   large  genus  of  hairy  1831. herbs  or  half-shrubs  of  the  borage  family  of  the  Old  World,  Eck'hardt,  1   ek'hSrt;  2   ek'hart.  Faithful.  [G.]  Folklore.  A with  one-sided  clusters  of  bluish  flowers.  E.  vulgare,  the  venerable  old  man  who 
5757:Eh'ren-herg,  1   S’ren-berg;  2   e'r6n-b6rg,  Christian  C«ott« fried  (V'iol795-®/2!l876).  A   German  naturalist  and  mlero- seoplst:  explored  In  Egypt,  Arabia,  and  Syria  -with  Hum- boldt in  Ural  and  Altai  mountains. Eh"reni“brelt'steln,lg*r6n-brait'dht<iln;2§-’r6n-br!t'shtln.n. A   town  and  fortress  in  Rhine  province,  on  the  Rliine;  be- sieged seven  times  (1631-1793).  [Ger.,  honor’s  broad  .stone.] Bh-re'ti-a,  1   e-rl'ti-a  or -ghi-s;  2   e-rg'ti-a  or  -shl-a,  ».  Bot.  A considerable  genus  of  cMcfly  tropical  trees  or  slirubs  of  
=== FSD_vol2.txt gibbon ===
5363:Education  (L.  educere,  to  lead  or  draw  out)  is  the  system- atic development  and  cultivation  of  the  mind  and  other natural  powers.  "Education  Is  the  harmonious  develop- ment of  all  our  faculties.  It  begins  In  the  nursery,  and  goes on  at  school,  but  does  not  end  there.  It  continues  through life,  whetherwe  will  or  not. . . .   ‘   Every  person,’  says  Gibbon, ‘has  two  cducatlom,  one  which  he  receives  from  others,  and one,  more  important,  which  he  gives  himself.”’  John  Lub- bock The  Use  of  Life  ch.  vli,  p.  111.
8403:Gibbons  vs.  Oadenia  vol.  vi.  p.  J3.  [l.  b.  is  co.  1S58.1 Ilf.  t.  To  seize  or  acquire  wrongfully.  [<  OF.  e
=== WEB_vol1.txt borage ===
7207:a-na/qua, n. (Sp. Am.] a small tree of the borage family, with hard, close-grained wood, found in Texas and Mexico. Also spelled anagua,
22100:bor/Age (biir’), n. [ME. borage, burage; LL. borrago, borago, from borra, the hair of beasts.] a plant of the genus Borago, used medicinally for its soothing and perspiratory properties and sometimes used in salads: written also burridge.
=== WEB_vol1.txt gibbon ===
8537:an’thrō-poid, a. [anthropo-, and Gr. eidos, resembling.] resembling a human being: ap- plied especially to the most highly developed apes, as the gorilla, orangutan, gibbon, and chimpanzee.
11703:right ascension; in astronomy, the are of the equator intercepted between the first point of Aries and that point of the equator which comes to the meridian with the sun or star. relating to ascension; as- cending or rising up. 2 ascensional difference; in astronomy, the dif- ference between the right and oblique ascen- sion of the same point on the surface of the sphere. ae as:cen/sive, a. 1. rising. 2. causing to rise. i; $ 3. in grammar. intensive; increasing the force; augmentative. [Rare.] ascent’, n. [L. ascensus, from ascendere, to ascend. ] > ; 1. the act of rising; rise; a mou
```


## [2026-09-04T18:14:13.424Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WEB gib ==\"; grep -n -m4 -E \"^gib\" WEB_vol1.txt | cut -c1-400; echo \"== HJB gibbon/hoolock ==\"; grep -n -i -m4 -E \"gibbon|hoolock\" HJB.txt | cut -c1-500; echo \"== AID ==\"; grep -n -i -m4 -E \"gibbon|monkey|bandar\" AID.txt | cut -c1-400; echo \"== DEV bourrache/gibbon ==\"; grep -n -i -m4 -E \"bourrache|gibbon\" DEV.txt | cut -c1-400; echo \"== PHN ==\"; grep -n -i -m4 -E \"bourrache|gibbon\" PHN.txt | cut -c1-400",
 "description": "Grep Anglo-Indian and French Arabism dictionaries"
}
```


### [2026-09-04T18:14:13.524Z] TOOL RESULT

```
== WEB gib ==
81719:gib, 1. [short for Gilbert, used as a proper name
102123:gibben, to kick back; OFr. regiber, to wince, kick; prob. of Scand. origin]
== HJB gibbon/hoolock ==
11275:HOOLnCK,s.  Benf.hulakl  The word  is  not  in  the  Diets.,  [hut  it  is possibly  connected  with  ulUk,  Skt. uLahiy  <  an  owl,'  both  bird  and  animal taking  their  name  from  their  wailiiig note].  The  black  gibbon  {Hylobatts hoolaokyJerd.;  [Blanford,  Mami)udia,5'\^ not  unfrequently  tamed  on  our  £. frontier,  and  from  its  gentle  engaging ways,  and  plaintive  cries,  often  becom> ing  a  great  pet.  In  the  forests  of  the Kasia  Hills,  when  there  was  
11281:1884.—"  He  then  .  .  .  describes  a  gibbon he  had  (not  an  historian  nor  a  book,  but  a specimen  of  Hylobates  hooluck)  who  must have  been  wholly  delightful.  T^s  engaging anthropoid  used  to  pnt  his  arm  through Mr.  Stemdale's,  was  extremely  dean  in  his habits  (*  which,'  says  Mr.  Stemdale  thought- fully and  truthfully,  *  cannot  be  said  of  all the  monkey  tribe  ),  and  would  not  go  to sleep  without  a  pillow.  Of  course  he  died of  c
13436:1884.— "Less  interesting  personally  than the  gibbon,  but  an  animal  of  very  developed social  instincts,  is  SemnopUhecus  eniettus, otherwise  the  Bengal  langur.  (He)  fights for  his  wives  according  to  a  custom  not unheard  of  in  other  cases;  but  what  is peculiar  to  him  is  that  the  vanquished  males <^receive  charge  of  all  the  young  ones  of their  own  sex,  with  whom  they  retire  to some  neighbouring  jungle.'  Schoolmasters and  private  tuto
13918:which  some  apprehend  to  be  a  cor- ruption of  the  word  Mandarin^  a  title of  distinction  among  the  Chinese  "  (H. of  Sumatra,  2nd  el  285).  Ritter adopts  the  etymology  from  mandar, apparently  after  A.  W.  Schlegel  * llie  true  etymon  ifl  pointed  out  in Notes  and  Queries  in  China  and  Japan, iii.  12,  and  by  one  of  the  present writers  in  Ocean  Highways  for  Sept. 1872,  p,  186.  Several  of  the  quota- tions beloiJir  will  show  that  the  ea
== AID ==
1146:Bhuiyd.  The  name  of  an  aboriginal tribe  of  Chutid  jfdgpur,  now  semi- Hinduised  and  numerous  in  Bengal and  Behar.  Their  favourite  god  is Hanuman,  and  they  are  supposed  to be  the  race  described  as  monkeys  in the  Rdmdyana.  They  are  cultivators and  labourers.
1335:Bunder.  [A  corruption  of  the  Hindu- stdni  bandar .]  A   harbour,  a   landing- place  ;   also  a   port  town  ;   and  in Bengal  also  a   market.
3543:Kdtkari.  [Mardfhi.]  An  aboriginal tribe  found  in  the  Konkan.  They have«a  tradition  that  they  are  de- scended from  the  wild  tribe— called in  the  legend  monkeys — which  Rdma took  as  allies  in  his  expedition  against
3544:Ceylon.  It  is  perhaps  in  accord- ance with  this  that  they  say  the brown-faced  monkey  has  a   human soul,  and  that  they  will  not  cat  it, though  they  do  eat  other  monkeys, and  almost  all  other  animals  except the  cow.  The  Kdtkaris  are  a   small, hardy  race,  of  dark  complexion  and with  very  low  foreheads.  The  men wear  slicndis  like  the  Hindus,  but
== DEV bourrache/gibbon ==
== PHN ==
10312:Bourrache, s. f. compose, (a.) 74
```


## [2026-09-04T18:14:21.021Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==106' PHN.txt | head -40",
 "description": "Print Pihan page 74"
}
```


### [2026-09-04T18:14:23.236Z] TOOL RESULT

```
76 BOU
BOURAGAN,s. m. (a.)
UV' [^rra^ati] Espèce de vêtement Doir, très-grossiér. Le
kouracan est une sorte de camelot d*un grain plus gros que le
camelot ordinaire. — G*est de l'arabe que les Espagnols et les
Portugais ont tiré harragana, subst. fém., et les Italiens bara-
coHo, mot écrit avec une seule r et employé au masculin comme
son correspondant français.
BOURNOUS,s. m. (a.)
if^ji [houmous] Ce mot , qui désignait , dans lorigine , le bmmet
pamiH porté par les religieux musulmans au commencement
de Tislamisme^ et spécialement le capuchon attaché à un vête-
ments se dit aujourdliui du wumteam de lowe, sans manches et à
cnfndion. que les Arabes ^ et surtout ceux de TAfrique septen-
trionale « ont coutume de mettre par-dessus leurs autres vête-
ments. Les boumous d*été sont de couleur blancbe , et ceux
d^biver de couleur foncée et en laine beaucoup plus épaisse. —
Depuis i830s fusage des boumous sW introduit en France,
avec plusieurs modifications, pour servir à la toilette d'hiver
des deux sexes, — Les Espagnole et les Portugais écrivent «/-
htmo:. mot qui représente a^si^x exactement le correspondant
ambe, préc^nlê toutefois de Fartide aL
ROIRRACHE. s. t composa, {k.)
>? [ M>iî ] (HUir^) j .î«Vw ] phr. ^jH [ rmirU' ] dir U smeur. Plante
ori|^iviiir^ du l^nant^ et dont rôl^mologie arabe suffit pour
imliquer la \ertu sudorilique; «mi Temploie principalement
d,^ns lt>s tivauo< jMvtomK^^. — r^^iu|virpi aussi Pespagnol
\
```


## [2026-09-04T18:14:33.684Z] TOOL CALL #52: WebSearch

```json
{
 "query": "\"أبو زنة\" قرد معنى تسمية القرد بأبو زنة"
}
```


### [2026-09-04T18:14:35.702Z] TOOL RESULT

```
Web search results for query: ""أبو زنة" قرد معنى تسمية القرد بأبو زنة"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T18:14:36.286Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['AFM_pages.txt','TAD_pages.txt','AFA.txt','incoming/PLA/PLA_pages.txt']:\n    try: t=open(f,encoding='utf-8',errors='replace').read()\n    except Exception as e: print(f,e); continue\n    for w in ['بوزينه','بوزينة','أبو زنا','ابو زنا','بوزنه']:\n        n=len(re.findall(w,t))\n        if n: \n            i=t.find(w); print('###',f,w,n,repr(t[max(0,i-200):i+250]))\n    print(f,'done')\nEOF",
 "description": "Grep Arabic loan dictionaries"
}
```


### [2026-09-04T18:14:37.979Z] TOOL RESULT

```
### AFM_pages.txt بوزينه 1 'ن\nا ܨ ܫ ܐ\n± (المَهَو) الميث المقدم امام البيوت وكاس = ܙ فارستتة مهو وهو يطلق\nعلى الغرفة والسرادق وقصر الماك وغير ذلك\n* (المهئّانة ) 80:60 الخفيفة الروح تعريب بهتانه وهو نوع من الةرود\nيقال له بالتركية بوزينه\n١\u200f الباب) وهو معروف فارسية يآ وه حتت بالاراميّة والرايّة وددة بالمراجة\nواعل منة < 5 ححط» اي باب العين ويوافقة اللاتيني هالتمنام\n(1اأمنام) والترى يك ٠\u200f والظاهر الّهُ من ܒܝܒܐ مشتق اسم بابل ܒܒ ܐܝܠ\nي باب الله او ܒܒ حمل اي باب ييل وهو اسم إله عند ا'
AFM_pages.txt done
TAD_pages.txt done
AFA.txt done
incoming/PLA/PLA_pages.txt done
```


## [2026-09-04T18:14:50.083Z] TOOL CALL #54: Bash

```json
{
 "command": "timeout 60 curl -sG 'https://ia800207.us.archive.org/fulltext/inside.php' --data-urlencode 'item_id=originsshortetym00part' --data-urlencode 'doc=originsshortetym00part' --data-urlencode 'path=/27/items/originsshortetym00part' --data-urlencode 'q=gibbon' | head -c 1500; echo; echo \"=== try generic ===\"; timeout 60 curl -s 'https://api.archivelab.org/books/originsshortetym00part/searchinside?q=gibbon' | head -c 800",
 "description": "Try archive.org search inside Partridge"
}
```


### [2026-09-04T18:16:52.321Z] TOOL RESULT

```
=== try generic ===
```


## [2026-09-04T18:17:00.520Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,l in enumerate(leaves):\n    if 'Aboth,  also  Abot' in l or 'Aboth, also Abot' in l:\n        print('Aboth leaf(0-based)',i)\n    if re.search(r'gibbon,  n\\.,  a  small', l):\n        print('gibbon leaf',i)\n    if 'borage,  n.,  a  blue' in l:\n        print('borage leaf',i)\nEOF",
 "description": "Find leaf numbers in Klein 1966"
}
```


### [2026-09-04T18:17:02.410Z] TOOL RESULT

```
Aboth leaf(0-based) 15
borage leaf 109
gibbon leaf 354
```


## [2026-09-04T18:17:11.118Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i in (15,109,354):\n    l=leaves[i]\n    nums=re.findall(r'(?<![\\d.])\\b(\\d{1,4})\\b(?!\\d)', l)\n    print(i, 'first/last lines:', repr(l[:120]), '...', repr(l[-120:]))\nEOF",
 "description": "Inspect leaf boundaries for page numbers"
}
```


### [2026-09-04T18:17:12.879Z] TOOL RESULT

```
15 first/last lines: '  and  -facient. abortion,  n.,  miscarriage.  —  L.  abortio,  gen.  -onis, ‘miscarriage,  abortion’,  fr.  abortus,  p' ... '.  *abstenire,  corresponding  to  L. abstinere,  ‘to  abstain’,  which  is  formed  fr.  abs, ab,  ‘away  from,  from’ '
109 first/last lines: '  ME.  bond,  a var.  of  band.  See  band,  ‘a  tie’,  and  cp.  the  first element  in  bonspiel.\nDerivatives:  bond, ' ... 'dge;  side  of  a  ship’,  which  is  orig. identical  with  *bord,  ‘plank’.  See  board,  ‘side  of a  ship’,  and  cp'
354 first/last lines: ' by  the English  poet  William  Wordsworth  (1770-1850). giant,  n.  —  ME.  geant,  fr.  OF.  geant  (F.  geant), fr. ' ... 'gimel ,  rel.  to  gamdl,  ‘camel’ (whence  Gk.  xdcjj.Y)Xo5,  L.  camelus,  ‘camel’);  so called  in  allusion  to  the'
```


## [2026-09-04T18:17:39.678Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef show(f,words,n=2,ctx=(150,220)):\n    try: t=open(f,encoding='utf-8',errors='replace').read()\n    except Exception as e: print('ERR',f,e); return\n    for w in words:\n        idxs=[m.start() for m in re.finditer(re.escape(w),t)]\n        print('###',f,w,len(idxs))\n        for i in idxs[:n]:\n            print(repr(t[max(0,i-ctx[0]):i+ctx[1]]));print('--')\nshow('BQT_v1_pages.txt',['ابراهیم','ابو '])\nshow('MON_part1.txt',['ابراهیم'])\nshow('AFA.txt',[\"Vater\",'ab '],n=1)\nEOF",
 "description": "Grep Borhan/Moin for Ebrahim"
}
```


## [2026-09-04T18:17:41.215Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FSD Aboth ==\"; grep -n -i -m3 \"aboth\" FSD_vol1.txt | cut -c1-400; echo \"== WEB Aboth ==\"; grep -n -i -m3 \"aboth\" WEB_vol1.txt | cut -c1-400; echo \"== GPL monkey ==\"; grep -n -i -m3 -E \"bojina|monkey\" GPL.txt | cut -c1-300",
 "description": "Grep Funk/Webster for Aboth"
}
```


### [2026-09-04T18:17:41.414Z] TOOL RESULT

```
### BQT_v1_pages.txt ابراهیم 27
'ه دزمردم بذال معجمه مشهور شده غلط است . بزاء\nحصجمه صحیح باشد.» واين قول خطاست ۰\nوموّ لف مجبل التواریخ و القصص رد : چون جبرئیل علیه السلام\nکیش بیاورد وابراهیم قر بان کرد...»\nموّلف «موّ بدا لفضلاء > گوید ۷ :«استوده» بالضم با واو فارسی استه؛\nنيك آوردن و نيك آمده.وماندگی گر فته. > وجای دیگی گویها : < استوه»\nمانده شده\u200cو افسرده و تنگ آمده وملول.» و بدیهی است که « استوده >\nب'
--
'کات 45 هنن بدان\nرجوع کر ده| ند همان شاه\u200cکار روز [ باد یست.\nدر ین صورت میتران اولین لغت نویسان زبان\u200cتازی را بمصداق واقعی\nاین کلمه ازهری وابن درید وابو ابراهیم فارابی و صاحب بن\u200cعباد و جوهری\x0cشصت وهفت فرهنگهای پارسی\nوابن\u200cفارس دانس تکه\u200cهمه\u200cاز سر زمین ایر ان\u200cبررخاسته\u200cاند ومیتوان بجرأت گفت\nکه لغت\u200cنویسی ز بان\u200cتازی ازاختراعات وابداعات ایرانیا نست.\nدر بارة ز بانپای ایرانی قدیمت'
--
### BQT_v1_pages.txt ابو  23
' دوستان ازمن درخواست کردند که این کتاب را\nبپارسی ترجمه کن. ققیر اجابت کرده ترجمه کردم در جمادی\u200cالاول سنه\u200cائنین\nوغشر بن و خمسمائه 4\nتاریخ بخارا ترجبهٌ ابو نصراحمد بن محمدبن نصر القباوی از تاریخ\nابوبکر محید بن جعفر نرشخی ( تلخیس محمد بن زفر بن عمر)\nبتصحیح مدرس رضوی. نشریهً کتابفروشی سناتی . تپر ان (بدون\nتاریخ) ص۲ .\n۰ ۱3۵6 اه بماندمه۷0 (ع:ع:۳۵ ۲56 , 1661۳2۷ . ۸\nْ ۰ - 164'
--
'اند از قبیل :\nهیر نظمی ۰ ابوالمعانی ۰ شاعر ( مطلق )۰ استاد (مطلن).\nهیر غرودی » منلا حیدری » دودبادی » لطیفی » میر ذ! قلی پیگ»\nمنز ه هندی » مطهر الدیی ابو الحطیر وغره وغره .\nدر چپار "ماه قبل بخاطرم رسید که لغات گرد آوردة انگلیس\u200cها را\nدر هند وفرانه ها زا در آسیای صفی بالفت نامه شموری تطبیق کنم\nو همن\u200cکار را کردم . معلوم شد که تمام آن لغت\u200cها بی هیچ تصرف و تحقیقی\nین دانی ا'
--
### MON_part1.txt ابراهیم 2
' تا مکه \n۸ میل باشد. متمتع باید از میقاتگاه احرام \nگیرد و به مکه رود و چون خانه\u200cهای مکه بیند \n«تلبیه, گوید و به مکه رود و هفت بار طواف \nکند و در مقام ابراهیم دو رکعت نماز بجا \nآرد و سعی بین صفا و مروه کند» سپس سر \nبتراشد و محل شود. آنگاه در روز تروبه \nنماز ظهر و نماز عصر به عرفات گزارد و تا \nهنگام غروب بدانجا بماند» سپس به مشعر \nشود و شب آنجا اقامت کند و بامداد به منی'
--
'ند تا \nدیری بماند و متلاشی نگردد. \n\nحننود: متامه! [ع.] (ص.) مهریان؛ با \nشفقت \n\n\nحنیف: ۱2 [ع.] (ص.) راست؛ مستقیم. \n\n\nات در دین» راست کیش. آنکه در فلت \nابراهیم باشد» متمسکک به دین اسلام؛ ج. \nحنفاء. \n\nحنین: ۱20 [ع.] (مص\u200cل.) بانگ کردن از \nشادی با حزن. زاری» ناله» شدت رف \nشفقت» اشتباق. \n\nحواء: "8 ( یف حوا] (ص.) موّنث \nاحوی؛ زن گندمگون. (اخ.) از اعلام زنان \nاست. \n\nحصوادث: 0'
--
### AFA.txt Vater 0
### AFA.txt ab  128
'mente sie geleitet haben. Ein schönes Zeug-\nniss dessen , was von den alten Sprachgelehrten auf diesem\nGebiete geleistet worden ist, bietet der Mu^arrab des Ga-\nwuliki ^) , dessen Hauptautoritaten nicht über das 4. Jahrh.\nder Hegra hinabgehen. Gawäliki selbst scheint nur wenig\nzu den Sammlungen Früherer beigetragen zu haben , im\nGegentheil findet sich manches von dem '
--
```


### [2026-09-04T18:17:41.505Z] TOOL RESULT

```
== FSD Aboth ==
== WEB Aboth ==
== GPL monkey ==
```


## [2026-09-04T18:17:48.816Z] TOOL CALL #59: Bash

```json
{
 "command": "head -40 tools/fetch_source.py",
 "description": "Inspect fetch_source.py usage"
}
```


### [2026-09-04T18:17:48.851Z] TOOL RESULT

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


## [2026-09-04T18:17:59.583Z] TOOL CALL #60: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%B2%DB%8C%D9%86%D9%87|page 33, root Ab 2, node 4: Persian buzine etymology (Proto-Iranian, not Arabic)\" \\\n \"https://www.etymonline.com/word/borage|page 33, root Ab 2, nodes 8-10: borage, Arabic abu arak vs Latin borra\" \\\n \"https://www.etymonline.com/word/gibbon|page 33, root Ab 2, nodes 5-7: gibbon, French, no Indian word found\" \\\n \"https://en.wiktionary.org/wiki/gibbon|page 33, root Ab 2, node 7: gibbon, Aslian etymology\" \\\n \"https://www.ahdictionary.com/word/search.html?q=borage|page 33, root Ab 2, node 8: AHD borage < ML boragō < Arabic bu araq\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/%CA%BEab-|page 33, root box Ab 2: Proto-Semitic *ab- father\" \\\n \"https://en.wiktionary.org/wiki/%D8%A3%D8%A8|page 33, node 1: Arabic ab/abu, root '-b-w\" \\\n \"https://en.wiktionary.org/wiki/%D8%A5%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9%85|page 33, nodes 14-15: Arabic Ibrahim < Aramaic, Persian descendant\" \\\n \"https://en.wiktionary.org/wiki/Abraham|page 33, node 13/16: Abraham, Genesis 17:5 folk etymology\" \\\n ; do url=\"${u%%|*}\"; note=\"${u##*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\"; done 2>&1 | tail -30",
 "description": "Archive web sources"
}
```


### [2026-09-04T18:18:01.942Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a79258c7fe012fe6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7132c6e9ee680f10.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5480297bf52b0bbb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5b69fb503d4db1b7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/343f0d6122563b9e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7191e2277240767c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c2b4c1fb59b8f19a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3ef8647d4ccc22af.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8d97f7dfbd80795d.txt
```


## [2026-09-04T18:18:06.071Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && tail -9 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d.get('status'), d.get('bytes'), d.get('title','')[:60], d['url'][:80])\n\"",
 "description": "Check archive index entries"
}
```


### [2026-09-04T18:18:07.741Z] TOOL RESULT

```
200 3581 ابهت - Wiktionary, the free dictionary https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D9%87%D8%AA
200 6246 Arrack - Etymology, Origin & Meaning https://www.etymonline.com/word/arrack
200 4726 American Heritage Dictionary Entry: gibbon https://www.ahdictionary.com/word/search.html?q=gibbon
200 4932 Reconstruction:Proto-Semitic/ʔabw- - Wiktionary, the free di https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/%CA%BEab-
200 9154 Reconstruction:Proto-Indo-European/h₂ep- - Wiktionary, the f https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ep-
200 5798 Reconstruction:Proto-Iranian/Hā́fš - Wiktionary, the free di https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C4%81%CC%81f%C5%A1
200 5732 أبه - Wiktionary, the free dictionary https://en.wiktionary.org/wiki/%D8%A3%D8%A8%D9%87
200 5394 بهاء - Wiktionary, the free dictionary https://en.wiktionary.org/wiki/بهاء
200 292 معنی ابهت | فرهنگ انتشارات معین | واژه یاب https://vajehyab.com/moein/ابهت
```


## [2026-09-04T18:18:14.630Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 -c \"\nimport json\nwant=['a79258c7fe012fe6','7132c6e9ee680f10','5480297bf52b0bbb','5b69fb503d4db1b7','343f0d6122563b9e','7191e2277240767c','c2b4c1fb59b8f19a','3ef8647d4ccc22af','8d97f7dfbd80795d']\nfor l in open('index.jsonl'):\n    d=json.loads(l)\n    if any(w in d.get('file','') for w in want): print(d.get('status'),d.get('bytes'),repr(d.get('title',''))[:60],d['url'][:70])\n\"",
 "description": "Verify my archived URLs in index"
}
```


### [2026-09-04T18:18:16.490Z] TOOL RESULT

```
200 9350 'gibbon - Wiktionary, the free dictionary' https://en.wiktionary.org/wiki/gibbon
200 5890 'Gibbon - Etymology, Origin & Meaning' https://www.etymonline.com/word/gibbon
200 6078 'Borage - Etymology, Origin & Meaning' https://www.etymonline.com/word/borage
200 48897 'Abraham - Wiktionary, the free dictionary' https://en.wiktionary.org/wiki/Abraham
200 20030 'أب - Wiktionary, the free dictionary' https://en.wiktionary.org/wiki/%D8%A3%D8%A8
200 5332 'إبراهيم - Wiktionary, the free dictionary' https://en.wiktionary.org/wiki/%D8%A5%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9
200 4566 'American Heritage Dictionary Entry: borage' https://www.ahdictionary.com/word/search.html?q=borage
200 3623 'بوزینه - Wiktionary, the free dictionary' https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%B2%DB%8C%D9%86%D9%87
200 4932 'Reconstruction:Proto-Semitic/ʔabw- - Wiktionary, the free d https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/%CA%BEab-
```


## [2026-09-04T18:18:20.930Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,60p' 5480297bf52b0bbb.txt | grep -n -A6 -i \"etymolog\"; echo \"=== gibbon wikt ===\"; grep -n -i -A8 \"Etymology\" 5b69fb503d4db1b7.txt | head -40",
 "description": "Read archived Wiktionary texts"
}
```


### [2026-09-04T18:18:20.986Z] TOOL RESULT

```
4:TITLE: Gibbon - Etymology, Origin & Meaning
5-
6:Gibbon - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
=== gibbon wikt ===
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
--
94: Etymology 
95-
96- 2.2 
97- Pronunciation 
98-
99- 2.3 
100- Noun 
101-
102- 3 
--
108: Etymology 
109-
110- 3.2 
111- Pronunciation 
112-
113- 3.3 
114- Noun 
115-
116- 3.4 
--
220: Etymology
221- [ edit ] 
222-
223: Reborrowing from French gibbon , folk etymology (compare English Gibbon ) [ 1 ] ultimately from a Northern Aslian language (compare Batek kəboɲ ). [ 2 ] 
224-
225- Pronunciation
226- [ edit ] 
227-
228- IPA ( key ) : /ˈɡɪbən/ , /ɡɪˈbɑn/ 
229-
```


## [2026-09-04T18:18:25.231Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i -B2 -A10 \"Proto-Iranian\" a79258c7fe012fe6.txt | head -30; echo \"=== etymonline borage ===\"; grep -n -i -A6 \"borrago\\|abu arak\\|borra\" 7132c6e9ee680f10.txt | head -30",
 "description": "Read archived buzine and borage texts"
}
```


### [2026-09-04T18:18:25.286Z] TOOL RESULT

```
146- [ edit ] 
147-
148: Inherited from Proto-Iranian [Term?] ; compare Pashto بيزو ( bízo , “ monkey ” ) . Anciently borrowed into Old East Slavic обезьꙗ́на ( obezĭjána ) whence Russian обезья́на ( obezʹjána , “ monkey, ape ” ) , and likely into Old Turkic 𐰋𐰃𐰲𐰃𐰤 ( béčin , “ monkey ” ) .
149-
150- Pronunciation
151- [ edit ] 
152-
153- ( Classical Persian ) IPA ( key ) : /buː.ziː.ˈna/ 
154-
155- ( Dari, formal ) IPA ( key ) : [buː.ziː.ná] 
156-
157- ( Dari, formal ) IPA ( key ) : [buː.ziː.ná] 
158- ( Kabuli ) IPA ( key ) : [buː.ziː.ná] 
--
207- Retrieved from " https://en.wiktionary.org/w/index.php?title=بوزینه&oldid=88426308 "
208-
209: Categories : Persian terms inherited from Proto-Iranian 
210: Persian terms derived from Proto-Iranian 
211- Persian terms with IPA pronunciation 
212- Rhymes:Persian/a 
213- Rhymes:Persian/a/3 syllables 
214- Persian lemmas 
215- Persian nouns 
216- Persian terms with quotations 
217-
218: Hidden categories: Proto-Iranian term requests 
219- Old Turkic terms with non-redundant manual transliterations 
220- Pages with entries 
221- Pages with 1 entry 
222-
=== etymonline borage ===
25: blue-flowered plant used in salads, etc., mid-13c., from Anglo-French burage , Old French borage (13c., Modern French bourrache ), from Medieval Latin borrago , which also is the source of Spanish boraja , Italian borraggine , German Boretsch .
26-
27: The Medieval Latin word was held by folk-etymology to be from Arabic abu arak , literally "the father of sweat," supposedly so called by Arab physicians for its effect on humans. But OED and other sources find it rather to be from Latin borra "rough hair, short wool," in reference to the texture of the foliage. Related: Boraginaceous .
28- also from mid-13c. 
29-
30- Entries linking to borage 
31-
32- orach (n.) 
33-
```


## [2026-09-04T18:19:01.297Z] AGENT

Now I'll write the verification file.


## [2026-09-04T18:19:03.214Z] TOOL CALL #65: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus && echo ok",
 "description": "Create output dir"
}
```


### [2026-09-04T18:19:03.253Z] TOOL RESULT

```
ok
```


## [2026-09-04T18:23:01.225Z] TOOL CALL #66: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus/page-33.json",
 "content": "{\n  \"pdf_page\": 33,\n  \"book_page\": 3,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ab 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Proto-Semitic *ʾab- / *ʾabw- 'father'\",\n      \"note\": \"The root box is right: Proto-Semitic *ʔabw- 'father' (Akk. abum, Ugar. ʾabu, Heb. ʾāḇ, Aram. ʾabbā, Arab. ʾab, Geʿez ʾab), an old nursery word, ultimately Proto-Afroasiatic; Klein s.v. Aboth says exactly this ('of uncertain origin, possibly traceable to *ab(a), a child's word for father'). Nourai's '2' is his homograph number (Ab 1 = water). Two branches of the chart are problematic and both hang on Arabic kunya-compounds in node #3: (a) the gibbon branch — Persian بوزینه is an inherited Iranian word (Wiktionary: inherited from Proto-Iranian, cf. Pashto bīzo; attested as būzīna, pl. būzīnagān already in the early NP Qurʾān commentary per Hübschmann, and lent onward to Old East Slavic obezĭjána and Old Turkic béčin) and French gibbon is of unknown origin, so the whole Arabic abū-zīnā > būzīne > bojīna > gibbon chain collapses; (b) the borage branch — Arabic abū ʿaraq 'father of sweat' as the source of Med.Lat. borrāgō is supported by Klein, AHD, Lokotsch no. 13 and Pihan, but rejected by Skeat, Webster and the OED/Etymonline in favour of Lat. borra/burra 'rough hair', so it is a live scholarly split, not a settled fact. Two printed-book errors (not extraction errors — checked against the page scan at 600 dpi): 'borrâco' in node #8 is a misprint for borrāgō, and 'Jaob' in node #16 for Joab. The JSON's «آبو» in node #2 IS an extraction artefact: the book prints أَبو (alef+hamza+fatha), read by OCR as alef-madda.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/%CA%BEab-\",\n        \"https://en.wiktionary.org/wiki/%D8%A3%D8%A8\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"FVQ:44\", \"status\": \"partial\", \"note\": \"FVQ_pages.txt leaf 62 = printed p. 44: the page is Jeffery's article on أبابيل and the opening of إبراهيم; it mentions the word for father only in passing ('deriving it from أبو = father and أبيل = lamentation'). Jeffery has no article on the Semitic root *ʾab as such, so p. 44 supports the names branch (below) rather than the root box.\"},\n        {\"ref\": \"KLN:6\", \"status\": \"supports\", \"note\": \"KLN_1966.txt \\\\f-leaf 15 (= printed p. 6, matches the leaf≈floor(p/2)+12 rule) s.v. 'Aboth, also Abot': 'Heb. Abhōth, pl. of ābh, \\\"father\\\", rel. to Aram. ābh (absolute state), abbā (emphatic state), Ugar. ʾb, Arab. ab, Ethiop. ab, \\\"father\\\"; of uncertain origin, possibly traceable to *ab(a), a child's word for father. Cp. the first element in Abraham, Abner, Absalom, Abigail, and the second element in Joab, Moab, Barabbas… Cp. also borage.' This one page is the source of almost the whole chart.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"ab, abŭ, a.b.v\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic أَبٌ ʾab-un 'father' continues Proto-Semitic *ʔabw- directly; the third radical wāw survives in the construct/nominative أَبُو ʾabū (acc. أَبَا ʾabā, gen. أَبِي ʾabī) — the 'six nouns' (al-asmāʾ al-sitta) declension — and in the plural آبَاء ʾābāʾ and the nisba أَبَوِيّ ʾabawī. Nourai's 'a.b.v' is his notation for the root ء ب و (ʾ-b-w), with v = wāw; that is exactly the root under which Wiktionary and the Arabic lexica file the word. ʾabū is the element that opens a kunya (Abū ʿAlī) and, by the same idiom, hundreds of Arabic plant- and animal-names ('father of X').\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A3%D8%A8\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/%CA%BEab-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVQ:44\", \"status\": \"partial\", \"note\": \"FVQ_pages.txt leaf 62 (printed p. 44): Jeffery cites 'أبو = father' only inside Sprengel's rejected etymology of أبابيل; the page carries no article on ab/abū itself.\"},\n            {\"ref\": \"FVA:25\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e Vāzhehā-ye ʿArabi dar Fārsi (1368/1989) — refs_online.json records no digital copy on any permitted platform (re-searched 2026-09), and there is none in the local library.\"},\n            {\"ref\": \"LKT:44\", \"status\": \"not_found\", \"note\": \"Checked both readings of the citation. LKT.txt \\\\f-leaf 71 = printed p. 44 (the leaf ends with the folio '44') and holds entries 547-550 (Tk. dümen, dur-, Ar. dūrawā, Mal. dūri) — nothing Semitic-ab. Lokotsch entry no. 44 is 'Ar. ʿaqīda: Rosenkonserve, Bonbon'. The relevant Lokotsch entry is no. 13 (printed p. 2-3), 'Ar. abū raqʿ [ʿaraq]: Vater des Schweißes'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p. 6 (leaf 15) s.v. Aboth\", \"stance\": \"supports\", \"note\": \"'…rel. to Aram. ābh…, Arab. ab, Ethiop. ab, \\\"father\\\"'.\"},\n            {\"src\": \"FVQ\", \"where\": \"p. 44 (leaf 62)\", \"stance\": \"partial\", \"note\": \"mentions أبو 'father' only inside a rejected etymology of أبابيل.\"},\n            {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen\", \"stance\": \"silent\", \"note\": \"grep 'Vater' returns nothing; Fraenkel treats Aramaic loans into Arabic, and ab is inherited, not borrowed, so his silence is expected and consistent.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 13 (p. 2-3), no. 14\", \"stance\": \"supports\", \"note\": \"Lokotsch's headwords 'Ar. abū raqʿ' and 'Ar. abū ṭilūn' show abū as the productive first element of Arabic plant names, exactly Nourai's point.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"abŭ «آبو ( ابوی )»\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The derivation is right — Persian ابو abu is a straight Arabic loan, taken over with the kunya formula after the Islamic conquest and productive in Persian names from the 10th c. on: ابوعلی سینا, ابوالفضل, ابوالقاسم, ابوالحسن, ابوالفتح, with the colloquial contraction ابوال- > بوال- in بوالهوس bu'l-hawas 'capricious, given to whims' (Moʿin files this under بل 'مخفف ابوالقاسم و ابوالفضل و مانند آنها'). The nisba form ابوی abavī 'paternal' is used in Persian (but not in Arabic) as a polite word for 'my father'. What is wrong is the Persian script in the JSON: the printed page (checked at 600 dpi) has أَبو — alef with hamza and fatḥa — which the OCR turned into «آبو» with alef madda. آبو is a different Persian word entirely (Moʿin: آبو = نیلوفر آبی 'water lily'), so the JSON headword should read «ابو ( ابوی )».\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A3%D8%A8\"],\n          \"ref_check\": [\n            {\"ref\": \"FVA:25\", \"status\": \"not_checked\", \"note\": \"Nahvi 1368/1989: no digital copy anywhere (refs_online.json, re-searched 2026-09).\"},\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"MON_part1.txt (Adena 2-vol abridgement of Farhang-e Fārsi), s.v. ابو: 'ابو [ع.] (از اسماء ستّه) (اِ.) اب، پدر… در عربی در حالت رفعی این کلمه را به صورت «ابو» و در حالت نصبی «ابا» و در حالت جرّی «ابی» گویند و غالباً در آغاز کنیهٔ مردان در آید'; and s.v. ابوی: 'ابوی [ع.] (ص نسبی) منسوب به اب، پدری. در تداول فارسیان این کلمه را به معنی پدر بکار برند و ابویِ من، ابویِ تو، ابویِ او گویند'. Both the headword and the parenthesised variant of the chart are Moʿin's, tagged [ع.] = Arabic.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt s.vv. ابو, ابوی, بل\", \"stance\": \"supports\", \"note\": \"'[ع.] … غالباً در آغاز کنیهٔ مردان در آید'; 'بل: مخفف ابوالقاسم و ابوالفضل… قس. بلقاسم و بلفضل' — the بوال-/بل- contraction of the chart's بوالهوس.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt / BQT_v2_pages.txt\", \"stance\": \"silent\", \"note\": \"grep 'ابو ' returns only running text of Moʿin's preface (e.g. 'ابو نصر احمد بن محمد', 'ابو ابراهیم فارابی'); Borhān-e Qāṭeʿ is a dictionary of Persian words and carries no headword for the Arabic kunya element.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"no entry — Horn covers inherited Iranian vocabulary, not Arabic loans.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien\", \"stance\": \"silent\", \"note\": \"no entry, same reason.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur's dictionary is of Indo-European roots in Persian; no ابو entry.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"abŭ-zînâ; abŭ-araq\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Both words are Arabic kunya-compounds of ʾabū 'father of' (node #1). أبو عرق abū ʿaraq 'father of sweat' (root ع ر ق ʿ-r-q, cf. ʿaraq 'sweat, distilled juice' > arrack) is genuinely attested as the Arab physicians' name for borage, from its diaphoretic use, and is the etymon Klein, the AHD, Lokotsch (no. 13) and Pihan give for Med.Lat. borrāgō — that word is plausible (see node #8 for the dispute over whether Latin really took it). أبو زنا abū zinā 'father of fornication' (root ز ن ي, whence zinā 'illicit intercourse') as an Arabic name for the gibbon is the weak half: no Arabic lexicon consulted here lists it, and it is invoked only to explain Persian بوزینه, which is not an Arabic loan at all (node #4). Phonetically the derivation also fails: abū zinā would give Persian *abu-zenā, not būzīna with -īn-. Addi Shir, writing in Arabic, actually treats بوزینه as a foreign (Turkish/Persian) word for a monkey, not as Arabic.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/borage\",\n            \"https://www.ahdictionary.com/word/search.html?q=borage\",\n            \"https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%B2%DB%8C%D9%86%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVQ:44\", \"status\": \"not_found\", \"note\": \"FVQ_pages.txt leaf 62 (printed p. 44) has no abū-zīnā and no abū-ʿaraq; Jeffery's book covers only Qurʾānic vocabulary and neither compound is Qurʾānic.\"},\n            {\"ref\": \"FVA:25\", \"status\": \"not_checked\", \"note\": \"Nahvi 1368/1989 not digitised.\"},\n            {\"ref\": \"LKT:44\", \"status\": \"not_found\", \"note\": \"LKT.txt leaf 71 = printed p. 44 = entries 547-550 (Tk. dümen, dur-, Ar. dūrawā, Mal. dūri); entry no. 44 is Ar. ʿaqīda. But Lokotsch no. 13 (p. 2-3) is exactly Nourai's claim for the borage half: 'Ar. abū raqʿ [read ʿaraq]: \\\"Vater des Schweißes\\\", hieraus lat. borrago, eine Pflanze, die durch die ar. Medizin im Mittelalter verbreitet wurde… Trotz ML 1412 scheint diese Ableitung noch immer die beste und wenig anfechtbar zu sein.' Nothing anywhere in Lokotsch for abū zinā.\"},\n            {\"ref\": \"AHD:152\", \"status\": \"supports\", \"note\": \"Nourai's page 152 of the 1975/76 New College Edition is the 'borage' entry (not open online); the current AHD online entry says: borage < Middle English/Old French bourage < Medieval Latin borāgō, 'probably from Arabic bū ʿaraq, from ʾabū ʿaraq, father of sweat'. So AHD supports abū-ʿaraq; it says nothing about abū-zīnā.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p. ~187 (leaf 109) s.v. borage\", \"stance\": \"partial\", \"note\": \"'…fr. ML. borrāgō, ult. fr. Arab. abū ʿarak, lit. \\\"father of sweat\\\", so called by the Arab physicians because of its sudorific effect' — supports abū-ʿaraq only; Klein's gibbon entry (p. 655) makes no Arabic claim.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 13, printed p. 2-3\", \"stance\": \"partial\", \"note\": \"supports abū ʿaraq > borrago; silent on abū zinā.\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan p. 76 s.v. BOURRACHE\", \"stance\": \"partial\", \"note\": \"'BOURRACHE, s. f. composé, (a.) [abū] (père) … [ʿaraq] dire la sueur. Plante originaire du Levant, et dont l'étymologie arabe suffit pour indiquer la vertu sudorifique' — supports the abū-ʿaraq half.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, AFM_pages.txt s.v. (المهنّانة)\", \"stance\": \"contradicts\", \"note\": \"'(المهنّانة) الخفيفة الروح تعريب بهتانه وهو نوع من القرود يقال له بالتركية بوزينه' — Addi Shir treats būzīna as the Turkish (i.e. Turco-Persian) word for a kind of monkey, not as an Arabic abū-compound.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Borage\", \"stance\": \"contradicts\", \"note\": \"'Low L. borraginem… prob. named from its roughness. Perhaps from Low L. borra, burra, rough hair' — no Arabic at all.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, vol. 1 s.v. borage\", \"stance\": \"contradicts\", \"note\": \"'[ME. borage, burage; LL. borrago, borago, from borra, the hair of beasts.]'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"bŭzîneh «بوزینه ( بوزنه )»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The word and its meaning are right — NP بوزینه būzīna 'monkey, ape' (variants بوزینا, بوزنه, بوزنینه), quoted by Nourai from Rumi — but the Arabic parent is not. Modern Iranian etymology takes būzīna as inherited from Proto-Iranian, cognate with Pashto بيزو bīzo 'monkey'; Hübschmann already notes that it is the current NP replacement for the older Indic loan kabī/kapī (< Pahl. kapīk, Skt. kapi-) and that it is attested 'schon im alten Korancommentar' (the 10th-11th c. NP Tafsīr, pl. būzīnagān), i.e. before any large-scale Arabic influence on the vocabulary of fauna. Its own descendants run the other way: it was lent into Old East Slavic обезьꙗ́на obezĭjána (whence Russian обезьяна 'monkey') and probably into Old Turkic béčin. Formally, Arabic abū zinā could only have given *abuzenā; the -īna(g) of būzīna is an Iranian suffix. Moʿin, who tags every Arabic loan [ع.], gives بوزینه no origin tag at all.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%B2%DB%8C%D9%86%D9%87\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:602\", \"status\": \"partial\", \"note\": \"The 6-vol Farhang-e Fārsi p. 602 (vol. 1, ب) is the بوزینه entry; the local Adena 2-vol abridgement (MON_part1.txt) has it as 'بوزینه: būzīna [= بوزینا - بوزنه - بوزنینه] (اِ.) (جاند.) میمون' — headword, both spellings of the chart and the gloss 'monkey' are Moʿin's, so the word is confirmed, but Moʿin gives NO [ع.] Arabic tag, i.e. he does not support Nourai's Arabic source.\"},\n            {\"ref\": \"FVA:180\", \"status\": \"not_checked\", \"note\": \"Nahvi 1368/1989 not digitised.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. بوزینه\", \"stance\": \"partial\", \"note\": \"'بوزینه … (جاند.) میمون' with variants بوزینا/بوزنه/بوزنینه; no Arabic origin tag.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien, note to Horn nos. 842-845 and p. 87 addenda\", \"stance\": \"contradicts\", \"note\": \"'Hier fehlt np. kabī \\\"Affe\\\" … = phl. kapik, arm. LW. kapik, skr. kapi-. Das Wort ist in alter Zeit aus dem Indischen entlehnt. Jetzt wird dafür būzīna, buzina etc. gebraucht'; and 'Np. buzina (im pl. buzinagan) schon im alten Korancommentar, JRAS. 1894, 449.' Hübschmann treats būzīna as the ordinary Persian word, early attested, with no hint of Arabic.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"grep 'Affe' and 'buzin' return nothing — Horn omits the word (which is precisely what Hübschmann's 'Hier fehlt' remark corrects).\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt\", \"stance\": \"partial\", \"note\": \"بوزینه occurs as a defining gloss inside other entries ('… بوزینه را گویند و آن نوعی از میمون باشد'), i.e. Borhān-e Qāṭeʿ treats it as a plain Persian word; no etymological footnote by Moʿin claiming Arabic.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"no بوزینه entry in Aryanpur's Indo-European-roots dictionary.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir s.v. (المهنّانة)\", \"stance\": \"contradicts\", \"note\": \"calls بوزینه the Turkish word for a kind of monkey.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Hindustani\",\n          \"words\": \"bojîna\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"No Hindustani (Urdu/Hindi) word bojīna 'ape' can be documented. The ordinary Hindustani words are bandar and, for the langur, lāṅgūr; the Indian gibbon (Hylobates hoolock) is called hūlak/hoolock, which is what Hobson-Jobson records as the Indian name Europeans actually met in Bengal and Assam ('HOOLOCK, s. Beng. hulak. The word is not in the Dicts.'). The OED's verdict on the supposed Indian source of gibbon is blunt — 'supposedly from a word in the French colonies of India but not found in any language there'. Nourai's bojīna looks like a link invented to bridge Persian būzīne (itself the wrong parent, node #4) to French gibbon; his only authority for it is Partridge, whose Origins is a popular etymological dictionary, not a source on Indic lexicon.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/gibbon\",\n            \"https://en.wiktionary.org/wiki/gibbon\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"PRT:253\", \"status\": \"not_checked\", \"note\": \"Partridge, Origins (1958), p. 253 — refs_online.json lists only lending-restricted archive.org copies (originsshortetym00part etc.); the full-text 'search inside' endpoint returned nothing for a query on 'gibbon'. No local text.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. HOOLOCK\", \"stance\": \"contradicts\", \"note\": \"'HOOLOCK, s. Beng. hulak… The black gibbon (Hylobates hoolock, Jerd.)… The word is not in the Dicts.' — the Anglo-Indian record for the Indian gibbon is hoolock, not bojīna, and Hobson-Jobson has no bojīna entry at all.\"},\n            {\"src\": \"AID\", \"where\": \"Whitworth, An Anglo-Indian Dictionary\", \"stance\": \"silent\", \"note\": \"grep 'bojina' and 'gibbon' return nothing.\"},\n            {\"src\": \"GPL\", \"where\": \"Platts & Ranking, A Grammar of the Persian Language\", \"stance\": \"silent\", \"note\": \"grep 'bojina'/'monkey' returns nothing.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Empty pass-through node standing for French gibbon (18th c.). The chart's own NOTE — 'This monkey was taken to France from India in the 18th century' — is accurate and is Klein's: the animal and its name were brought to Europe by Joseph-François Dupleix (1697-1763), governor-general of the French possessions in India 1742-54, and the word first appears in French zoological writing (Buffon) in the 1760s. What is not supported is the arrow from Hindustani bojīna: the OED/Etymonline record the French word as of uncertain origin, 'supposedly from a word in the French colonies of India but not found in any language there', and the current Wiktionary proposal derives it, through folk etymology on the French surname Gibbon, from a Northern Aslian language of the Malay peninsula (cf. Batek kəboɲ) — i.e. from the gibbon's actual habitat rather than from India at all.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/gibbon\",\n            \"https://en.wiktionary.org/wiki/gibbon\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:655\", \"status\": \"partial\", \"note\": \"KLN_1966.txt leaf 354 (printed p. ~655, between 'giant' and 'gimel') s.v. gibbon: 'F., a name of Indian origin brought to Europe by the Marquis Joseph-François Dupleix (1697-1763), governor-general of the French possessions in India (1742-54).' Klein supports the French mediation and the Dupleix note verbatim, but says only 'of Indian origin' — he gives no Indian, Persian or Arabic word, so he does not support the bojīna/būzīne/abū-zīnā chain.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p. 655 s.v. gibbon\", \"stance\": \"partial\", \"note\": \"'a name of Indian origin brought to Europe by… Dupleix' — the source of Nourai's note, but with no etymon.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale\", \"stance\": \"silent\", \"note\": \"grep 'gibbon' returns nothing — Devic does not count gibbon among French words of oriental origin.\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan, Dictionnaire étymologique… dérivés de l'arabe, du persan ou du turc\", \"stance\": \"silent\", \"note\": \"grep 'gibbon' returns nothing — Pihan does not list gibbon as an Arabic/Persian/Turkish loan in French, although he does list bourrache.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch\", \"stance\": \"silent\", \"note\": \"grep 'gibbon' returns nothing in the whole dictionary of European words of oriental origin.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"gibbon\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English gibbon is a straight borrowing of French gibbon, first recorded in English in 1770 as a name for the long-armed apes (Hylobates) that Dupleix's specimens had made known in Paris; no phonetic change beyond the English stress and /dʒ/. The link French > English is uncontroversial; only what stands behind French is unknown (node #6).\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/gibbon\",\n            \"https://en.wiktionary.org/wiki/gibbon\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:655\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 354 s.v. gibbon: 'n., a small, long-armed ape. — F., a name of Indian origin…' — Klein's 'F.' is exactly the French > English step of this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p. 655 s.v. gibbon\", \"stance\": \"supports\", \"note\": \"derives the English word from French.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\", \"note\": \"grep 'gibbon' returns nothing; Skeat's Concise omits the word.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard, vols 1-2\", \"stance\": \"silent\", \"note\": \"grep 'gibbon' returns only the historian Edward Gibbon in quotations; the ape headword is not in the OCR'd portion.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century vol. 1\", \"stance\": \"silent\", \"note\": \"'gibbon' occurs only inside the definition of 'anthropoid'; no headword in the OCR'd volume.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Middle Latin\",\n          \"words\": \"borrâco\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Medieval Latin plant name is borrāgō, gen. borrāginis (whence It. borragine, borrana, Sp. borraja, Pg. borragem, Prov. borrage, Ger. Boretsch/Burrich). 'borrâco' is a misprint in Nourai's own printed page — I read the book scan at 600 dpi and it really does print 'borrâco', so this is the author's error, not the JSON extraction's. On the derivation itself scholarship is split. FOR the Arabic source: Klein ('ult. fr. Arab. abū ʿarak, lit. \\\"father of sweat\\\", so called by the Arab physicians because of its sudorific effect'), the AHD ('probably from Arabic bū ʿaraq, from ʾabū ʿaraq'), Lokotsch no. 13 ('hieraus lat. borrago… Trotz ML 1412 scheint diese Ableitung noch immer die beste'), and Pihan p. 76; the route is Arabic medical botany > Salernitan/Latin herbals of the 11th-13th c. > Romance. AGAINST: Skeat, Webster, and the OED (followed by Etymonline), which take borrāgō from Latin borra/burra 'rough hair, coarse wool' + -āgō (a common Latin plant-name suffix, cf. plantāgō, farrāgō), from the plant's famously bristly leaves — a formation that explains the -āgō suffix, which the Arabic etymology does not. Note that the Latin-borra account also weakens Klein's own cross-reference from arrack.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/borage\",\n            \"https://www.ahdictionary.com/word/search.html?q=borage\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:152\", \"status\": \"supports\", \"note\": \"p. 152 of the 1975/76 New College Edition is the 'borage' entry (that edition is lending-only); the current AHD online entry reads 'Middle English borage, from Old French bourage, from Medieval Latin borāgō, probably from Arabic bū ʿaraq, from ʾabū ʿaraq, father of sweat', i.e. AHD does give Nourai's Arabic > Medieval Latin arrow. AHD prints borāgō, not 'borrâco'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p. ~187 (leaf 109) s.v. borage\", \"stance\": \"supports\", \"note\": \"'fr. ML. borrāgō, ult. fr. Arab. abū ʿarak, lit. \\\"father of sweat\\\"'.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 13 (p. 2-3)\", \"stance\": \"supports\", \"note\": \"'Ar. abū raqʿ: \\\"Vater des Schweißes\\\", hieraus lat. borrago… Trotz ML 1412 scheint diese Ableitung noch immer die beste und wenig anfechtbar zu sein' — Lokotsch is explicitly arguing against Meyer-Lübke REW 1412 (the burra etymology).\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan p. 76 s.v. BOURRACHE\", \"stance\": \"supports\", \"note\": \"'l'étymologie arabe suffit pour indiquer la vertu sudorifique'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Borate [Borage]\", \"stance\": \"contradicts\", \"note\": \"'Low L. borraginem, acc. of borrago, borage; prob. named from its roughness. Perhaps from Low L. borra, burra, rough hair (whence F. bourre, Ital. borra)'.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century vol. 1 s.v. borage\", \"stance\": \"contradicts\", \"note\": \"'[ME. borage, burage; LL. borrago, borago, from borra, the hair of beasts.]'\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Old French\",\n          \"words\": \"borrace, bourrache\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Med.Lat. borrāgō, acc. borrāginem, gave Old French borrache/borrace (13th c.), with the regular Gallo-Romance treatment of intervocalic -g- before a front vowel and the loss of the final syllable; the doublet with -rr- and the variant burage are both recorded. The modern French form is bourrache, with -ou- for the tonic o. Klein gives precisely 'OF. borrace (cp. its variant burage and F. bourrache)', so both of the chart's forms are documented — although Lokotsch assigns borrace to Italian rather than Old French, so the pair may conflate an Italian and a French form.\",\n          \"sources\": [\"https://www.etymonline.com/word/borage\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:152\", \"status\": \"supports\", \"note\": \"the AHD borage entry gives 'from Old French bourage' (online ed.; the 1975/76 p. 152 print entry gives Old French bourache/bourrache), i.e. the Med.Lat. > Old French step of this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p. ~187 s.v. borage\", \"stance\": \"supports\", \"note\": \"'ME., fr. OF. borrace (cp. its variant burage and F. bourrache), fr. ML. borrāgō'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Borage\", \"stance\": \"supports\", \"note\": \"'F. bourrache. — Low L. borraginem' — same chain, different ultimate source.\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan p. 76\", \"stance\": \"supports\", \"note\": \"French bourrache treated as the descendant of the Latin/Arabic name.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 13\", \"stance\": \"partial\", \"note\": \"'Die romanischen Formen sind: it. borrace, borragine, borrana; prov. borrage; sp. borraja; pg. borragem; frz. bourrache' — Lokotsch lists borrace as Italian, not Old French.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"borage\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle English borage/burage, borrowed from Anglo-French burage / Old French borage (mid-13th c.), naming Borago officinalis, the bristly blue-flowered Mediterranean herb whose young leaves (with a cucumber taste) go into salads and cool drinks — Nourai's gloss 'a spicy salad seasoning' is a fair rendering of Klein's 'a blue-flowered plant used in salads'. The English word's own history is not in doubt; only the ultimate source behind Medieval Latin is (node #8).\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/borage\",\n            \"https://www.ahdictionary.com/word/search.html?q=borage\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:152\", \"status\": \"supports\", \"note\": \"AHD's borage entry (p. 152 of the 1975/76 ed.; text as in the current online entry) begins 'Middle English borage, from Old French bourage', exactly the Old French > English step, and defines it as the annual bristly herb Borago officinalis with edible leaves and stems.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p. ~187 s.v. borage\", \"stance\": \"supports\", \"note\": \"'borage, n., a blue-flowered plant used in salads. — ME., fr. OF. borrace'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Borage\", \"stance\": \"supports\", \"note\": \"English from French, Low Latin borraginem.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century vol. 1 s.v. borage\", \"stance\": \"supports\", \"note\": \"'a plant of the genus Borago, used medicinally for its soothing and perspiratory properties and sometimes used in salads: written also burridge' — note that Webster keeps the sudorific sense that motivated the Arabic etymology while rejecting that etymology.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard vols 1-2\", \"stance\": \"silent\", \"note\": \"'borage' occurs only in family names ('of the borage family, Boraginaceae') under anaqua, Ehretia, Echium; no separate headword in the OCR'd text.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Hebrew\",\n          \"words\": \"abh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Biblical Hebrew אָב ʾāḇ 'father' (Nourai's 'abh' is the older transliteration with spirantised bēṯ, ʾāḇ) continues Proto-Semitic *ʾabw- with loss of the third radical in the free form; the wāw resurfaces in the construct plural אֲבוֹת ʾăḇōṯ and in ʾăḇī- in compound names. It is the exact cognate of Arabic ab (node #1) and Aramaic ʾabbā, not a borrowing from it — so the chart's two branches from the root box are correctly drawn as sisters.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/%CA%BEab-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:6\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 15 = printed p. 6 s.v. Aboth: 'Heb. Abhōth, pl. of ābh, \\\"father\\\", rel. to Aram. ābh (absolute state), abbā (emphatic state), Ugar. ʾb, Arab. ab, Ethiop. ab, \\\"father\\\"' — Klein's 'ābh' is Nourai's 'abh' letter for letter.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p. 6 s.v. Aboth\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n            {\"src\": \"FVQ\", \"where\": \"p. 44-45\", \"stance\": \"silent\", \"note\": \"Jeffery treats only the Qurʾānic إبراهيم here; he has no article on Hebrew ʾāḇ.\"},\n            {\"src\": \"AFA\", \"where\": \"Fraenkel\", \"stance\": \"silent\", \"note\": \"no entry; the word is inherited in both Hebrew and Arabic, not an Aramaic loan.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"Abot\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Abot / Aboth is the Hebrew plural אָבוֹת ʾăḇōṯ 'fathers' taken over unchanged as the title of the Mishnah tractate Pirqē ʾĀḇōṯ 'Chapters of the Fathers' (the Ethics of the Fathers) and, in the liturgy, of the first benediction of the ʿAmīdā. The construct plural preserves the original third radical (*ʾabaw-āt > ʾăḇōṯ), which is why the plural, not the singular, is the form English received. Nourai's spelling 'Abot' is Klein's own alternative spelling.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"KLN:6\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 15 (printed p. 6): 'Aboth, also Abot, n., 1) the Mishnah treatise also called Pirke Aboth or The Ethics of the Fathers; 2) name of the first benediction of the Shemoneh Esreh (Jewish liturgy). — Heb. Abhōth, pl. of ābh, \\\"father\\\"' — headword, alternative spelling and derivation from abh are all exactly the chart's.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p. 6 s.v. Aboth\", \"stance\": \"supports\", \"note\": \"as quoted; Klein is the only one of the English dictionaries here that carries the word.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard vol. 1\", \"stance\": \"silent\", \"note\": \"grep 'aboth' returns nothing.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century vol. 1\", \"stance\": \"silent\", \"note\": \"grep 'aboth' returns nothing.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Hebrew\",\n          \"words\": \"Abh-raham; Abh-ram; Abh-ner; Ab-šalom; Abh-igayil; Yo-abh\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"All six are genuine Hebrew names built on ʾāḇ 'father', five with ʾāḇ first and one (Joab) with it second, and Klein's p. 6-7 entries give Nourai's glosses almost word for word. אַבְנֵר ʾAḇnēr 'my father is light' = ʾăḇī + nēr 'lamp, light' (Klein compares the Babylonian PN Abunuri) — confirmed. אַבְשָׁלוֹם ʾAḇšālōm 'father is peace' = ʾāḇ + šālōm — confirmed. אֲבִיגַיִל ʾĂḇīgayil 'my father is rejoicing' = ʾăḇī + gīl 'to rejoice' — confirmed. אַבְרָם ʾAḇrām = ʾāḇ + rām 'high, exalted' (participle of rūm), so properly 'the father is exalted' rather than Nourai's 'high father' — a word-order quibble, not an error of substance. יוֹאָב Yōʾāḇ 'YHWH is (his) father', with Yō- the shortened theophoric of YHWH as in Joel, Jonathan, Joshua — confirmed. The one problem word is אַבְרָהָם ʾAḇrāhām: 'father of the multitude' is the explanation Genesis 17:5 itself supplies (ʾaḇ hămōn gōyim), and Klein follows it by positing *rāhām 'multitude' (comparing Arabic ruhām); modern scholarship generally treats that as a folk etymology attached to an already-old name and takes ʾAḇrāhām as a dialectal/expanded byform of ʾAḇrām ('the father is exalted'), the -h- being an Aramaic-style secondary expansion rather than a 'multitude' morpheme. Hence 'plausible' for the node as a whole.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Abraham\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:6\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaves 15-16 (printed pp. 6-7): 'Abner… Heb. Abhnēr, lit. \\\"my father is light\\\", fr. abh, \\\"father\\\", and nēr, \\\"light\\\"'; 'Absalom… Heb. Abhshālōm, lit. \\\"father is peace\\\"'; 'Abigail… Heb. Abhigáyil, lit. \\\"my father is rejoicing\\\"'; 'Abram… compounded of ābh, \\\"father\\\", and rām, \\\"high, exalted\\\"'; 'Abraham… Heb. Abhrāhām, lit. \\\"father of the multitude\\\", compounded of ābh, \\\"father\\\", and *rāhām, \\\"multitude\\\", which is rel. to Arab. ruhām, of s.m.; see Gen. 17:5'; 'Joab… fr. Heb. Yōʾāḇ, lit. \\\"the Lord is (his) father\\\"'. Every gloss on the chart is Klein's.\"},\n            {\"ref\": \"FVQ:44\", \"status\": \"supports\", \"note\": \"FVQ_pages.txt leaves 62-63 (printed pp. 44-45), s.v. إبراهيم: 'It is always used of the Biblical Patriarch and thus is ultimately derived from Heb. אברהם' — Jeffery affirms the Hebrew name behind the Arabic one that this node feeds.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 pp. 6-7 and p. ~840 s.v. Joab\", \"stance\": \"supports\", \"note\": \"all six names, as quoted.\"},\n            {\"src\": \"FVQ\", \"where\": \"pp. 44-45\", \"stance\": \"supports\", \"note\": \"Hebrew אברהם as the ultimate source of the Qurʾānic name.\"},\n            {\"src\": \"AHD\", \"where\": \"Wiktionary s.v. Abraham (for the modern consensus)\", \"stance\": \"partial\", \"note\": \"Genesis 17:4-5 glosses the name as ʾaḇ + hămōn 'father of many nations'; modern scholars (e.g. Thompson) read it as 'the father is exalted', the biblical gloss being a forgotten-etymology folk explanation, or as a dialectal variant of Abram.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Arabic\",\n          \"words\": \"Abrahim\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Arabic name is إِبْرَاهِيم Ibrāhīm (Nourai's 'Abrahim' is a loose transliteration; the Qurʾānic form has initial i- and -āhīm). It does go back to Hebrew ʾAḇrāhām, but not directly, and Nourai's single arrow flattens the step that Jeffery — the very reference he cites — spends the page arguing: a direct Hebrew borrowing would have produced *Abrāhām, and the Arabic vocalisation with -īm points to the Syriac/Christian-Aramaic ʾAḇrāhām as the immediate source, the same form that gave Geʿez ʾAbrəhām and Armenian Abraham. Wiktionary likewise files إبراهيم as 'borrowed from Aramaic אַבְרָהָם', with Biblical Hebrew behind that. The word entered Arabic in the pre-Islamic Christian/Jewish milieu of the Ḥijāz and is Qurʾānic (some 69 occurrences), and the Muslim philologists themselves (as-Suyūṭī, al-Jawālīqī) already classed it as a foreign word.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A5%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9%85\"],\n          \"ref_check\": [\n            {\"ref\": \"FVQ:44\", \"status\": \"partial\", \"note\": \"FVQ_pages.txt leaves 62-63 (printed pp. 44-45): the entry إبراهيم begins on p. 44 and continues 'ultimately derived from Heb. אברהם. If the name had come direct from the Heb. we should have expected the form *Abrāhām… we learn from as-Suyūṭī, Muzhir, i, 138, and al-Jawālīqī, 8, that some early authorities recognized it as a foreign borrowing… The common Syr. form is ʾAḇrāhām which is obviously the source of both the Eth. and the Arm.' So Jeffery supports the Hebrew ultimate origin but explicitly denies the direct Hebrew > Arabic route Nourai's arrow draws.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"pp. 44-45\", \"stance\": \"partial\", \"note\": \"as quoted — Hebrew ultimately, Syriac/Aramaic immediately.\"},\n            {\"src\": \"KLN\", \"where\": \"1966 p. 6 s.v. Abraham\", \"stance\": \"silent\", \"note\": \"Klein treats only the Hebrew and the European forms; he does not mention the Arabic name.\"},\n            {\"src\": \"TAD\", \"where\": \"al-Unaysi, Tafsīr al-alfāẓ al-dakhīla\", \"stance\": \"silent\", \"note\": \"grep of the Arabic headword list returns no إبراهيم entry.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Persian\",\n          \"words\": \"Ebrâhîm «ابراهیم»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian ابراهیم is the Arabic Qurʾānic name taken over unchanged in spelling after the conquest and read in Persian phonology as Ebrāhīm (Classical Persian Ibrāhīm), Arabic i- being realised as e- in New Persian; Wiktionary lists Classical Persian ابراهیم explicitly as a descendant of Arabic إبراهيم. It is a common Persian given name from the earliest Islamic-Persian literature on, and Nourai's Rumi couplet (بت شکستی گیرم ابراهیم‌وار / کو بت تن را فدا کردن به نار) is the standard literary allusion to Abraham the idol-breaker thrown into Nimrod's fire.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A5%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9%85\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives this node no reference of his own; nothing to check.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt\", \"stance\": \"silent\", \"note\": \"the Adena 2-vol abridgement of Farhang-e Fārsi covers the lexicon only; ابراهیم appears solely in running definitions (مقام ابراهیم, ملت ابراهیم), since proper names are in vols 5-6 (Aʿlām) of the 6-vol edition, which is not digitised.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt\", \"stance\": \"silent\", \"note\": \"ابراهیم occurs 27 times but only in Moʿin's introduction and in citations (e.g. 'ابو ابراهیم فارابی'); Borhān-e Qāṭeʿ has no headword for the personal name.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"English\",\n          \"words\": \"Abraham, Abram, Abner, Absalom, Abigail, Jaob\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All six English names reached English from Hebrew through the Greek of the Septuagint/New Testament and Late Latin of the Vulgate (Gk. Ἀβραάμ, Ἀβεννήρ, Ἀβεσσαλώμ, Ἀβιγαία, Ἰωάβ > Late L. Ābrahām, Abner, Absalom, Abigail, Joab), and were spread as given names by the Bible and, from the 16th c., by Puritan naming practice; Abigail additionally became a common noun 'lady's maid' after 1 Sam. 25:25, where she calls herself a handmaid. 'Jaob' is a misprint for Joab in the printed book itself (verified on the 600 dpi page scan), not an extraction error; the same name is spelled correctly as 'Joab' in the parent node #13.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Abraham\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaves 15-16 and leaf ~430 carry all six as English headwords with Hebrew etymologies: 'Abraham, masc. PN.; in the Bible, the first of the patriarchs…', 'Abram…', 'Abner, n., masc. PN.…', 'Absalom…', 'Abigail, fem. PN.…', 'Joab, 1) masc. PN.; 2) in the Bible, the chief captain of David's army. — Late L. Joab, fr. Gk. Ἰωάβ, fr. Heb. Yōʾāḇ'. Klein's Joab entry also supplies the Greek/Late Latin route this node needs.\"},\n            {\"ref\": \"AHD\", \"status\": \"not_checked\", \"note\": \"Nourai gives no page; the 1975/76 New College Edition is lending-only, and biographical/biblical entries are not in the Watkins IE-roots appendix that is available locally (AHD_watkins1985.txt).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 pp. 6-7, s.v. Joab\", \"stance\": \"supports\", \"note\": \"as quoted; 'Late L. Joab, fr. Gk. Ἰωάβ, fr. Heb. Yōʾāḇ' gives the transmission route.\"},\n            {\"src\": \"AHD\", \"where\": \"Wiktionary s.v. Abraham (standing in for the AHD entry)\", \"stance\": \"supports\", \"note\": \"'Ancient Greek Ἀβρᾱά̄μ… then into Late Latin Ābrahām, and subsequently into Old English and other European languages'.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard\", \"stance\": \"silent\", \"note\": \"grep 'Aboth'/biblical name etymologies returns nothing usable in the OCR'd volumes.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-04T18:23:01.256Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus/page-33.json (file state is current in your context — no need to Read it back)
```


## [2026-09-04T18:23:06.399Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 -m json.tool /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus/page-33.json > /dev/null && echo \"JSON OK\" && VERIFY_DIR=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus python3 tools/verify_check.py 33",
 "description": "Validate JSON and run coverage check"
}
```


### [2026-09-04T18:23:08.882Z] TOOL RESULT

```
JSON OK
nodes verified: 16/16
node verdicts: {'confirmed': 8, 'transcription_suspect': 1, 'disputed': 4, 'plausible': 3}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 4, 'not_checked': 7, 'not_found': 3, 'supports': 11}
books consulted: {'supports': 19, 'partial': 10, 'silent': 25, 'contradicts': 8} | by book: {'KLN': 12, 'LKT': 5, 'SKT': 5, 'WEB': 5, 'FVQ': 4, 'PHN': 4, 'FSD': 4, 'MON': 3, 'BQT': 3, 'AFA': 2, 'HRN': 2, 'HUB': 2, 'ARY': 2, 'AFM': 2, 'AHD': 2, 'HJB': 1, 'AID': 1, 'GPL': 1, 'DEV': 1, 'TAD': 1}
```


## [2026-09-04T18:23:26.719Z] AGENT

Done. Output: `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus/page-33.json` (valid JSON; verify_check: 16/16 nodes).

**PDF page 33 (book p. 3) — one entry, root "Ab 2" [Semitic] "father"**

Root: confirmed (Proto-Semitic \*ʾabw-; Klein p. 6 s.v. *Aboth* is verbatim the chart).
Node verdicts: 8 confirmed, 3 plausible, 4 disputed, 1 transcription_suspect.
Ref checks: 11 supports, 4 partial, 3 not_found, 7 not_checked (FVA and PRT have no digital copy anywhere).
Books consulted: 20 titles, 62 lookups (19 supports / 10 partial / 25 silent / 8 contradicts). 9 web pages archived via `fetch_source.py`.

- **disputed — #3 Arabic `abŭ-zînâ` "father of whoredom"**: unattested as an Arabic name for the gibbon; invented only to feed Persian بوزینه. (Its sibling `abŭ-araq` is fine.)
- **disputed — #4 Persian `bŭzîneh`**: inherited Proto-Iranian (cf. Pashto bīzo), attested pl. *būzīnagān* in the old NP Qurʾān commentary (Hübschmann), lent *out* to Old East Slavic *obezĭjána* / Old Turkic *béčin*; Moʿin gives it no [ع.] tag.
- **disputed — #5 Hindustani `bojîna`**: no such word; the Indian gibbon is Beng. *hūlak* (Hobson-Jobson); OED: "not found in any language there".
- **disputed — #6 French (gibbon)**: French word of unknown origin (Wiktionary: N. Aslian, cf. Batek *kəboɲ*); Klein only says "of Indian origin, brought by Dupleix" — Nourai's note is right, his arrow isn't.
- **transcription_suspect — #2 Persian «آبو»**: the book prints أَبو (600 dpi check); OCR read alef+hamza as alef-madda. آبو is a different word ("water lily" in Moʿin). Should be «ابو ( ابوی )».
- Two misprints are in the **printed book**, not the extraction (both verified on the scan): `borrâco` (#8) for Med. Lat. *borrāgō*, and `Jaob` (#16) for Joab.
- #8 rated *plausible*, not disputed: Arabic *abū ʿaraq* → *borrāgō* is backed by Klein, AHD (still, online), Lokotsch no. 13, Pihan p. 76, but rejected by Skeat, Webster and OED/Etymonline in favour of Lat. *borra* "rough hair" + -āgō.
- #14 Arabic Ibrāhīm rated *plausible*: Jeffery (the cited ref, FVQ:44-45) explicitly denies a direct Hebrew→Arabic route — the immediate source is Syriac ʾAḇrāhām.
