# Verification process log — verify-page-57


## [2026-09-04T22:40:35.681Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 57 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-57.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-57.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-57.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 57` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T22:40:37.685Z] AGENT

I'll start by reading the instructions and the relevant files.


## [2026-09-04T22:40:39.802Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T22:40:39.813Z] TOOL RESULT

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


## [2026-09-04T22:40:40.084Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-57.txt"
}
```


### [2026-09-04T22:40:40.099Z] TOOL RESULT

```
1	=== PDF page 57 (book page 27) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Angh : tight, compressed  (refs POK:42)
4	#1 (parent #0) [Avestan] refs=POK:42 | azaehě : compressed, in need ; ni-az : that which pushes you down, need ☞Nî 1
5	  #2 (parent #1) [Pahlavi] refs=MON:4877 | niyâz : need
6	    #3 (parent #2) [Persian] refs=BQT:2222; MON:4877 | niâz «نياز» : need ; nîâzî «نيازى» : need, dear friend, sweetheart | extra: نيازمند ، نيازومند
7	#4 (parent #0) [Latin] refs=AHD | 
8	  #5 (parent #4) [English] refs=None | anxious, anguish
9	#6 (parent #0) [Germanic] refs=AHD | 
10	  #7 (parent #6) [English] refs=None | anger
11	--- entry 1 ---
12	ROOT [Indo-European] Angwhi : snake  (refs POK:43)
13	#1 (parent #0) [Avestan] refs=POK:44; KLN:86 | aži : snake ; aži-dahâkô : biting snake
14	  #2 (parent #1) [Persian] refs=BQT:116,1339; PLA:5,190; FSF:43 | eždehâk «اژدهاک» : serpent ; eždehâ «اژدها» : serpent, also a spear ; aždar «اژدر» : torpedo | extra: ضحّاک
15	#3 (parent #0) [Latin] refs=AHD | anguis : snake
16	  #4 (parent #3) [English] refs=None | anguine
17	--- entry 2 ---
18	ROOT Ank -> redirect to Ang
19	--- entry 3 ---
20	ROOT Anô -> redirect to An 3
21	--- entry 4 ---
22	ROOT Anôr -> redirect to Nôr
23	--- entry 5 ---
24	ROOT Anq -> redirect to Ang
25	--- entry 6 ---
26	ROOT Ansu -> redirect to An 1
27	--- entry 7 ---
28	ROOT An-teros -> redirect to An 2
29	--- entry 8 ---
30	ROOT Ap 1 -> redirect to Ab 1
31	
```


## [2026-09-04T22:40:42.201Z] AGENT

I'll read the supporting files next.


## [2026-09-04T22:40:45.111Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T22:40:45.158Z] TOOL RESULT

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


## [2026-09-04T22:40:47.245Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','WLD','AHD','KLN','BQT','MON','PLA','FSF','HRN','HUB','PHD','NYB','IEC','SYN','BRT','KNT','CHEUNG','SKT','FSD','WEB','ARY','AFM','FVQ']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False))\n\"",
 "description": "Read refs_online for keys"
}
```


### [2026-09-04T22:40:50.752Z] TOOL RESULT

```
<persisted-output>
Output too large (38.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bxu665ijh.txt

Preview (first 2KB):
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)", "local_files": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_0
...
</persisted-output>
```


## [2026-09-04T22:40:55.883Z] AGENT

Let me look at the source JSON and the key ref metadata.


## [2026-09-04T22:40:57.052Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-57.json | head -200",
 "description": "Read page-57 JSON"
}
```


### [2026-09-04T22:40:58.985Z] TOOL RESULT

```
{
    "pdf_page": 57,
    "book_page": 27,
    "entries": [
        {
            "root": {
                "name": "Angh",
                "lang": "Indo-European",
                "refs": "POK:42",
                "gloss": "tight, compressed"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:42",
                    "words": [
                        {
                            "translit": "azaeh\u011b",
                            "gloss": "compressed, in need",
                            "script": null
                        },
                        {
                            "translit": "ni-az",
                            "gloss": "that which pushes you down, need",
                            "script": null,
                            "see": [
                                "N\u00ee 1"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Pahlavi",
                    "refs": "MON:4877",
                    "words": [
                        {
                            "translit": "niy\u00e2z",
                            "gloss": "need",
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
                    "refs": "BQT:2222; MON:4877",
                    "words": [
                        {
                            "translit": "ni\u00e2z",
                            "gloss": "need",
                            "script": "\u0646\u064a\u0627\u0632"
                        },
                        {
                            "translit": "n\u00ee\u00e2z\u00ee",
                            "gloss": "need, dear friend, sweetheart",
                            "script": "\u0646\u064a\u0627\u0632\u0649"
                        }
                    ],
                    "script_extra": "\u0646\u064a\u0627\u0632\u0645\u0646\u062f \u060c \u0646\u064a\u0627\u0632\u0648\u0645\u0646\u062f",
                    "note": null,
                    "quote": {
                        "text": "\u062f\u0644\u0645 \u062e\u0633\u062a\u0647\u0654 \u0646\u0627\u0632 \u062a\u0648\u0633\u062a \u0627\u06cc \u0646\u064a\u0627\u0632\u06cc - \u06a9\u0647 \u0631\u0648\u0632\u06cc \u0646\u064a\u0627\u0633\u0627\u064a\u06cc \u0627\u0632 \u0646\u0627\u0632 \u0628\u0627\u0632\u06cc",
                        "poet": "Osm\u00e2n Mokht\u00e2r\u00ee"
                    }
                },
                {
                    "id": 4,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "anxious, anguish",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "anger",
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
                "name": "Angwhi",
                "lang": "Indo-European",
                "refs": "POK:43",
                "gloss": "snake"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:44; KLN:86",
                    "words": [
                        {
                            "translit": "a\u017ei",
                            "gloss": "snake",
                            "script": null
                        },
                        {
                            "translit": "a\u017ei-dah\u00e2k\u00f4",
                            "gloss": "biting snake",
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
                    "refs": "BQT:116,1339; PLA:5,190; FSF:43",
                    "words": [
                        {
                            "translit": "e\u017edeh\u00e2k",
                            "gloss": "serpent",
                            "script": "\u0627\u0698\u062f\u0647\u0627\u06a9"
                        },
                        {
                            "translit": "e\u017edeh\u00e2",
                            "gloss": "serpent, also a spear",
                            "script": "\u0627\u0698\u062f\u0647\u0627"
                        },
                        {
                            "translit": "a\u017edar",
                            "gloss": "torpedo",
                            "script": "\u0627\u0698\u062f\u0631"
                        }
                    ],
                    "script_extra": "\u0636\u062d\u0651\u0627\u06a9",
                    "note": null,
                    "quote": {
                        "text": "\u0628\u062c\u0646\u0628\u06cc\u062f \u06af\u0634\u062a\u0627\u0633\u067e \u0627\u0632 \u067e\u06cc\u0634 \u0635\u0641 - \u06cc\u06a9\u06cc \u0628\u0627\u0631\u0647 \u0632\u06cc\u0631 \u0627\u0698\u062f\u0647\u0627\u06cc\u06cc \u0628\u06a9\u0641",
                        "poet": "Ferdows\u00ee"
                    }
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "anguis",
                            "gloss": "snake",
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
```


## [2026-09-04T22:40:59.395Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['BQT','MON','PLA','FSF','AHD','KLN']:\n    e=d.get(k,{})\n    print('===',k)\n    for f in ['kind','url','local_file','local_files','page_offset','lookup_hint','notes','scans']:\n        if f in e: print(' ',f,':',str(e[f])[:900])\n\"",
 "description": "Ref metadata for cited abbrs"
}
```


### [2026-09-04T22:41:01.258Z] TOOL RESULT

```
=== BQT
  kind : archive_djvu+local_scan_ocr
  url : https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verific
  page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017,
  lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only t
  notes : Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only
  scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming
=== MON
  kind : website+archive_djvu
  url : https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
  page_offset : None
  lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
  notes : covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists
=== PLA
  kind : archive_djvu
  url : https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt']
  page_offset : 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
  lookup_hint : HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
  notes : Open full text obtained. Alphabetical Arabic headwords with Persian/MP etyma; OCR fair (German + transliteration), Arabic script mostly garbled. Provenance: a user upload of an in-copyright 1988 Harrassowitz book — grey copy; publisher sells it (harrassowitz-verlag.de).
  scans : [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', 'first_printed': 1, 'last_printed': 300, 'pdf_offset': 0, 'lang': 'deu+ara'}]
=== FSF
  kind : archive_djvu
  url : https://archive.org/details/20220809_20220809_1444
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt']
  page_offset : 484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking
  lookup_hint : grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).
  notes : Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Donya print Nourai used.
=== AHD
  kind : archive_djvu+website+archive_restricted
  url : https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
  page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
  lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
  notes : AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.
=== KLN
  kind : archive_djvu
  url : https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
  local_files : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt']
  page_offset : KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
  notes : Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)
```


## [2026-09-04T22:41:13.611Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-57.json | sed -n '200,300p'",
 "description": "Rest of page 57 JSON"
}
```


## [2026-09-04T22:41:14.780Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: an\" POK_full.txt | head -40; echo \"=== angwhi\"; grep -n -i \"lemma: ang\" POK_full.txt | head",
 "description": "Search Pokorny full for angh roots"
}
```


### [2026-09-04T22:41:15.468Z] TOOL RESULT

```
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "anguine",
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
                "name": "Ank",
                "redirect": "Ang"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "An\u00f4",
                "redirect": "An 3"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "An\u00f4r",
                "redirect": "N\u00f4r"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Anq",
                "redirect": "Ang"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Ansu",
                "redirect": "An 1"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "An-teros",
                "redirect": "An 2"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Ap 1",
                "redirect": "Ab 1"
            },
            "nodes": []
        }
    ]
}
```


### [2026-09-04T22:41:15.526Z] TOOL RESULT

```
1731:From Root/ lemma: ang''(h)i-\ "snake, worm' derived Root/ lemma: ak^'a- {more properly 
3826:From Root/ lemma: ang''(h)i-\ "snake, worm' derived Root/ lemma: ak''a- {more properly 
4769:Root / lemma: anA^er-, ijA^er- 
4796:Root / lemma: anA"^-, aned^- 
4829:Root / lemma: anA'^o- 
4844:Root / lemma: an(9)-3^henah^ 
4850:Root/ lemma: an(a)-3\ to breathe' derived from a reduction of Root/ lemma: anghen-: 
4931:From Root / lemma: an(a)-3\ "to breathe' derived in zero grade Root/ lemma: nas- 
4951:Root/ lemma: anat-{*ang''h-at-) 
5060:Root / lemma: anghen- 
5074:Root / lemma: angh- {*hengh-) 
5169:Root / lemma: ang''(h)i- {* eg'^hi-, og'^i- and egh/-) 
5179:Root/ lemma: ang''(h)i-\ 'snake, worm, *fish' derived from an extended Root/ lemma: 
5266:Root / lemma: ank-1 
5301:Root / lemma: ank-2, ang- 
5417:Root / lemma: an-1{*han- 1) 
5424:Root / lemma: an-1{*han-) : "male or female ancestor' derived from zero grade of Root/ 
5487:Root / lemma: an-2 
5526:It seems Root / lemma: an-2\ "there, on the other side' is a zero grade of the extended 
5539:Root / lemma: an4, anu, and, no 
5616:Root / lemma: ansa, ansi- 
5650:Root/ lemma: ansu-, psu-{*henku-r-\n centum languages) 
5656:Root/ lemma: ansu-, psu- {* henku-r-): ghost, demon, derived from Root/ lemma: ank-2, 
5707:Root / lemma: ans- 
5742:Root / lemma: antro-m 
5756:Root / lemma: ants 
7103:Alb. and Rumanian prove that from Root/ lemma: anat-: (duck) derived Root/ lemma: 
9140:Root / lemma: ano- 
10309:g^era-: "to devour; throat' + zero grade g^fhj/-^ snake, worm, fish' Root/ lemma: ang''(h)i-\ 
29504:Root/ lemma: eff-: "diver' derived from the abbreviated Root/ lemma: anat-: "duck' 
61827:which derived from zero grade of Root/ lemma: an(a)-3\ "to breathe' : Root/ lemma: 
62871:zero grade of Root/ lemma: an(a)-3\ "to breathe'. 
74129:From a zero grade of Root/ lemma: ang''(h)i-\ "snake, worm' derived lllyrian *nsaia'ee\' 
=== angwhi
1731:From Root/ lemma: ang''(h)i-\ "snake, worm' derived Root/ lemma: ak^'a- {more properly 
3826:From Root/ lemma: ang''(h)i-\ "snake, worm' derived Root/ lemma: ak''a- {more properly 
4850:Root/ lemma: an(a)-3\ to breathe' derived from a reduction of Root/ lemma: anghen-: 
5060:Root / lemma: anghen- 
5074:Root / lemma: angh- {*hengh-) 
5169:Root / lemma: ang''(h)i- {* eg'^hi-, og'^i- and egh/-) 
5179:Root/ lemma: ang''(h)i-\ 'snake, worm, *fish' derived from an extended Root/ lemma: 
10309:g^era-: "to devour; throat' + zero grade g^fhj/-^ snake, worm, fish' Root/ lemma: ang''(h)i-\ 
74129:From a zero grade of Root/ lemma: ang''(h)i-\ "snake, worm' derived lllyrian *nsaia'ee\'
```


## [2026-09-04T22:41:18.982Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5060,5270p' POK_full.txt",
 "description": "Pokorny angh- and anghen- entries"
}
```


### [2026-09-04T22:41:19.049Z] TOOL RESULT

```
Root / lemma: anghen- 

Meaning: "smell, odour; person' 

Material: Armenian anjn{ior older *anj). Gen. anjin^ soul, being, person ' = Old Norse angi 

m. " odour, smell '. 

maybe alb. 5/7/ "swell, puff' [common alb. ng > nj\. 

References: Liden Arm. Stud. 38 f., WP. I 58, Meillet Esquisse 77 ff. 

Page(s): 43 

Root / lemma: angh- {*hengh-) 

Meaning: "narrow, *press' 

Material: Verbal: Avestan qzarjhe^io press', lengthened grade Avestan ny-azata^ she 

squeezes herself into her corset ', ny-azayen " to wedge oneself in ' (with a = 5; ved. 

ahema possibly " let us arm = gird on the sword ' is remote to the meaning; anaha RV. 8, 

46, 5 is unclear); 

Maybe zero grade alb. Geg {*anza-) zane'to capture, grasp, press', Tosc ze\ Avestan 

qzarjhe^io press' [common alb. -gh- > -z-]. 

gr. ayxu) " ties up, strangles ', Latin ango^ to press tightly; of the throat, to strangle, 
throttle; in gen., to hurt, distress; of the mind, to torment, make anxious '; 

Old Church Slavic as /■ verb gzg, gz/t/" restrain '; in addition with zero grade very 
probable Old Church Slavic vgzg, vgzat/" bind ' (suggestion that v- is filling hiatus, see 
Meillet MSL. 14, 369, maybe becomes steady through influence from 1////" coil, bind, wind' 
which may also have influenced meaning?). 

anghu-s' narrow ': Old Indie only in amhu-bhedTi. " narrow lacuna ' and in the Abl. Sg. 
n. arhhoh^ crowdedness, quality of tightly packed together, affliction ' (derivative arhhura-^ 
pressed, unhappy '); gr. in apcpriv (see below); Latin in angiportus {* angu-portus) " narrow 
alley, a narrow street '; 

Gothic aggwus " narrow ' (at first from *aggus, as manwus irom *manus, m/ comes from the 
oblique cases). Old Norse gngr, 0ngr, Old English enge. Old Saxon engi. Old High 
German angi, engT narrow ', Middle High German bange Mn. {bi+ Adv. ango). Modern 
High German bange, furthur derivatives with g. Armenian anjuk^ narrow ', mit /rOld 
Church Slavic gzi^-ki, " narrow '. 



Cymr. e(h)ang (*eks-angu-, Indo Germanic *nghu-) " far, wide, extensive ', mcymr. 
eingyaw^ be restricted, be contained in ... ', Old Irish cumcae {*kom-ingia) gl. " 
compression of the throat, suffocation; of the mind, distress, anguish, trouble ', fairsing^ 
far, wide ' ( *for-eks-ingi-), cumung {* kom-ingu-, Indo Germanic *nghu-) " narrow ', ing^. 
{*nghTj " crowdedness, affliction ', from *kom-angio-C)/vc\r. cyfyng, in this way yA7^ (also ing, 
Morris-Jones, Welsh Gr. 110)' narrow ', Middle Breton encq {*angio-) " narrow '. 

Maybe alb. eA?^ "deaf and dumb (*narrowed)' 

anghos-, anghes^ oppression, affliction, crowdedness ': Old Indie amhas-u. " Fear, 
distress, need ' (as well as amhatf-hi.), Avestan c[zah-' badgering, need, captivity ', qzo- 
Jata^ killed by strangulation ': Latin angorm. " compression of the throat, suffocation; of the 
mind, distress, anguish, trouble ', angus-tus' narrow ' (from *anghos-to-s)\ angustiae^ 
narrowness; hence, of space, a strait, narrow place; 'spiritus', shortness of breath; of time, 
shortness; of supplies, shortness, poverty; of circumstances, difficulty, distress; of 
disposition, narrow-mindedness; of reasoning, subtlety '; 

maybe zero grade in alb. {* angus-tus) ngushte' narrow'. 

about Celtic see above; Old Norse angrrw. (maybe originally more neutrally es-stem, Fick^ 
III 12) ' Annoyance, loss, pity, affliction, frustration ', Old Frisian angost. Old High German 
angust. Modern High German Angst {irorr\ *a/7^/7c»5-//- changing the vowel aiter * anghu-); 
Old Church Slavic gzostb " restriction, constriction, limitation, narrowing '; 

Lithuanian ankstas " narrow ' {k- insertion, not guttural change) cannot stand for *an^a]s- 
tas or *anz-tas. 

Words for " nape ' as ' the narrowest place between head and trunk ' ( the idea also 
plays a role " where one strangles one ' in light of this?): gr. Aeolic apcpriv and aucpnv " 
nape ' (after Schuize GGA. 1897, 909 A. 1, as *aYxF-nv substantivization of ^-Adj. *anghu- 
s by means of forms -en-; 

about auxnv see also Schwyzer Gr. Gr. I 296), Gothic hals-agga^ r\a^e\ kir. vjazyP\. 
"Neck', Czech vaz^ neck, nape ' (to v§zatisee above). Old Prussian (as Slavic loanword) 
m'nsus' neck ' (also Armenian i//z' neck, throat, cervix ' with preposition i/-?), see 
Pedersen KZ.38, 311; 39, 402, Vondrak SI. Gr. I 184, Adontz Mel. Boisacq I 10, as well as 
below under augh-, ugh. 

Other formations: gr. ayxovr) " cord, choking, strangling ' (from it Latin ang/na' the 
quinsy, as suffocating '), ayKirip m. " braces, bandage ', ayx'. cjyXoO, ayxoGi " close to ' 



(compare French pres^ close to, near': Latin pressus'a pressing, pressure'), compounds 
ciaaov " nearer, very near ' (*aYX,iov; aaaov hence has changed after jjaaawv = *|jaKiu)v, 
Osthoff MU. 6, 60 ff.); common gr.-lllyrian -ks- > -ss-\ 

bret. concoez^ geode ' {*kom-angeid-\ compare also dial, ancoe^ uvula in the throat '; 
Ernault RC. 7, 314; 19, 314 ff.); Old Church Slavic qzota^ narrowness '. 

Gall. PN Oc/oc/i/ms absents, because Irish ochte^ narrowness, straitness ' does not 
exist. 

Van Windekens (Lexique 5) puts here Tocharian A amgar^ weak, flimsy (?)'. 

References: WP. I. 62 f., WH. I 47. 
Page(s): 42-43 

Root / lemma: ang''(h)i- {* eg'^hi-, og'^i- and egh/-) 

Meaning: "snake, worm, *fish (*hedgehog = snake eater)' 

Note: eg"/?/-, og^hi- and egh/- ds., at least two etymological different, but early the crossed 

kinship whose relations still are often unclear. 

Note: 

Root/ lemma: ang''(h)i-\ 'snake, worm, *fish' derived from an extended Root/ lemma: 

angh- {* hengh^: 'narrow, *press' 

Material: Latin 5/7^^/s = Lithuanian angis{i.). Old Prussian angis^ serpent, snake ' 

(Latvian uodzei. ' snake '), Old Church Slavic *gzh, russ. uz, poln. m/^z' snake ', 

Armenian a^y(Gen. -/) ' snake ' (Meillet Esquisse 154, Dumezil BSL. 39, 100); 

Middle Irish esc-ung^ eel ' (*'water snake ', esc' water ' + *ang"hd), cymr. Ilys-yw-en, PI. - 

yw-od ds. (Pick 11^ 15; to brit. zero grade from z;^ before usee Pedersen KG. I 107). 

In addition with zero grade and voiced-nonaspirated (the latter could be in itself also in 
the Latin and Balto-Slavic) Old High German unc^ snake, adder ', gr. (illyr). apsic; £X£i<; 
Hes. {*ng"'f-). Note: common lllyrian g"'- > b-. 

To these forms with voiced-nonaspirated at first is ippr|P"i £YX£^U(;, MsGupvaToi Hes. 
{* eng"-eri-: to i compare Solmsen Beitr. 1215), where because of r- suffixes are to be 
connected Balto-Slavic *anguria-\n Slavic *ggorbrr\. russ. ug(o)rb, poln. wggorz, Czech 
uhdr, Serb, ugor, sloven, oggr^ eel ', Lithuanian ungurys ds. 

(assim. from *angurys, compare Finnish ankerias). Old Prussian angurgis^ eel ' (Church 
Slavic ^gulja, jgguija ' eel' probably from Latin). Hirt IF. 22, 67 connects these gr. and 



Balto-Slavic eel names to an independent equation (nevertlieiess, compare tlie A-suffix of 
Old High German angaretc, see below). 

Another Indo Germanic equation for " eel ' is perhaps gr. eyxs^u^ f., Latin anguilla (see 
esp. W. Meyer KZ. 28, 163, Johansson KZ. 30, 425, J. Schmidt KZ. 32, 369, Osthoff IF. 4, 
270, 292, Hirt IF. 22, 67, Indo Germanic 619 f.), although the details are still unclear (in the 
Gr. *aYX£^uo(; assimilated etc. to zsxthjoc,, or £ and the pure gutural through the influence 
from £xi<;; in Latin -///a instead of-e//a after the fluctuation in real diminutive under 
determining influence / of anguisl). 

With r- suffix: 

Gr. imPhP"^ eel' 

Maybe in -dz- > ^/ending stem: 

Maybe from Greek lllyrian syxsAuc; " eel ' > alb. ngja/e' eel ' [common Albanian Slavic yx- 
> dz-] lllyrian TN Encheleae^ snake men? ' : Hungarian ango/na'eeV [from native lllyrian 
TN Paeones]. 

In the meaning ' worm, maggot ' and with A-suffix (compare above ijjpnP"^ etc) : Old High 
German angar^ grain maggot' ' engirinc^ larva ', Modern High German Engerling, 
Lithuanian ankstiraT^ maggots, cock chafer grubs, grubs ' (and similar forms, see 
Trautmann Old Prussian 301), Latvian anksteri^ maggots, cock chafer grubs ', Old 
Prussian anxdr/s{\.e. anxtris), however, 'adder' (about the -st- these Baltic forms compare 
MiJhlenbach-Endzelin Lett.-D. Wb. I 71), russ. ug(o)rb ' blister, raised bubble on the skin 
that is filled with pus, fin ' (also " eel', see above), poln. wqgry^ blister, raised bubble on 
the skin ' (Bezzenberger GGA. 1874, 1236, BB. 2, 154; not better about angar, ugorb ders. 
GGA. 1898, 554 f.). 

Nasalized forms: 

Gr. £xi<; m. (f.) "snake', £Xi5va ds. (for *£xi5via, Specht Dekl. 377), Old High German 
egala^ leech, bloodsucking worm ', Danish Norwegian igle^ a parasite sheet worm in the 
viscera of the animals and in the skin and the branchia of the fish '. 

Moreover gr. £xTvoc;, Old High German Old English /g//(lndo Germanic *eghinos). 
Modern High German Igel, actually ' snake eater ', W. Schuize Gnomon 11, 407, 
Lithuanian ezys. Church Slavic yiezi. ' hedgehog (snake eater) '. 



Armenian /z" snake, viper ' can be put as *eg"'h/s\.o ocpic; (Meillet Esquisse 75); 

gr. 6(p\q " snake ' {*og"his)\ cymr. euod {*og"h-) " sineep worms ': Old Indie ahi-, Avestan 
azi- " snake '. 

It is uncertain apposition from Old Saxon egithassa. Middle Low German egidesse. Old 
English (corrupted) at^exe. Old High German egidehsa. Modern High German Eidechse 
mit ewi-, egi-, Indo Germanic *og"'hi-= ocpic; (Zupitza gutturals 99 after Kluge; Falk-Torp 
under 0gle) + Germanic *t^ahsid. Old High German *dehsa^ spindle, newel '. 

Whether in this variety so order is to be brought that *arjg"'hi- and *eghi-, *oghi- (gh) an 
intersection form would have caused *eg"hi-, *og"hi- , remains undecided. Taboo images 
have also probably helped in it. 

References: WP. I 63 ff.. WH. I 48, Specht KZ. 64, 13; 66, 56 f.. Havers Sprachtabu 44 f. 
Page(s): 43-45 

Root / lemma: ank-1 
Meaning: "need, necessity' 
Material: 

In e- grade:
```


## [2026-09-04T22:41:28.770Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 50 51 52 53; do echo \"=== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' POK_01.txt | head -60; done",
 "description": "Print Pokorny leaves 50-53"
}
```


### [2026-09-04T22:41:31.476Z] TOOL RESULT

```
=== leaf 50
 ahema  etwa ,mögen  wir  rüsten^  liegt  in  der  Bed.  ab;  anäha  RV.  8,  46,  5  ist  unklar);
gr.  Uyx(j')  ^schnüre  zusammen,   erdroßle^,  lat.  angö  , beenge,  schnüre  zu^;
aksl.  als  i-Verbum  ozo,  gziti  ,beengen*;  dazu  mit  Tiefstufe  sehr  wahr- scheinlich aksl.  vezo^  vezati  ,binden^  (y-  hiatusfüllender  Vorschlag,  siehe Meillet  MSL.  14,  369,  vielleicht  festgeworden  durch  Einfluß  von  viti , winden',  das  auch  die  Bed.  beeinflußt  haben  mag?).
anghü-s  ^eng^ :  ai.  nur  in  aiahu-hhedl  f.  ,engspaltig*  und  im  Abi.  Sg. n.  amhöh  , Bedrängnis^  (Ableitung  aihhurd-  ,bedrängt,  unglücklich^);  gv.  in d(.icprjv  (s.  u.);  lat.  in  angiportus  (^'-angu-i).)  ,enges  Gäßchen'^;  got.  aggicus ,enge'  (zunächst  aus  *aggus,  w-ie  manwus  aus  *manus]  das  ic  stammt  aus den  obliquen  Kasus),  anord.  ongr,  engr,  ags.  enge,  as.  engl,  ahd.  angi,  engl ,eng^,  mhd.  bange  Adv.  (bi  +  Adv.  ango),  nhd.  bange-^  weitergebildet  mit g:  arm.  anjuk  ,eng*,  mit  k  aksl.  oz^-k^  ,eng*.
Cymr.  e(li)ang  (*eks-angu-,  idg.  '^nghu-)  ,weit,  umfangreich-,  mcymr. eingyaw  ,eingeengt  sein,  enthalten  sein  in  .  .  .',  air.  cumcae  (*kom-ingia) gl.  ,cLngov',  fairsing  ,weit^  {^''for-eks-ingi-),  cumung  (*kom-ingu-^  idg.  *nyhu-) ,eng^,  ing  f.  {^nghi)  , Bedrängnis^,  aus  '^kom-angio-  cymr.  cyfyng,  danach  yng (auch  ing,  Morris-Jones,  Welsh  Gr.  110)  ,eng^,  mbret.  enc(i  (*augio-)  ^eng'.
anghos-,  anghes  ,Beklemmung,  Bedrängnis^:  ai.  dmhas-  n.  ,Angst, Bedrängnis,  Not^  (wie  auch  amhati-h  f.),  av.  qzah-  ,Bed rängung,  Not,  Ge- fangenschaft',  qzö-jata   ,durch   Erdrosselung   getötet*^:    lat.    angor   m.   ,das
43
^Zusammenschnüren  der  Kehle;  Unruhe^  Angst.  Kummer*/  amjus-tus  ,eng-^ faiis  '^■anghos-to-s)]  angiistiae  ^Enge,  Klemme^  Schwierigkeiten^;  über  kel- tisches s.  0.;  anord.  angr  m.  (vielleicht  ursprüngl.  neutraler  esSt.,  Fick* III  12)  ^Verdruß;  Schade^  Betrübnis^;  afries.  angost,  ahd.  angust,  nhd. 'bigst  (aus  *anghos-ti-  nach  *anghu-  umvokalisiert);  aksl.  qzosti)  ^Beengung^; lit.  afikstas  ,eng^  (A:-Einschub^  nicht  Gutturalwechsel)  kann  für  *anz[a]s-tas oder  '^' anz-tas  stehen.
Worte  für  ;,Nacken^  als  ^engste  Stelle  zwischen  Kopf  und  Rumpf'  (spielt .luch  die  Vorstellung  ^wo  man  einen  würgt^  herein?) :  gr.  äol.  Hf-icpriV  und avmv  ^Nacken'^  (nach  Schulze  GGA.  1897^  909  A.  1,  als  ^ayxf-iqv  Substan- tivierung des  w-Adj.  *anghii-s  mittels  des  Formans  -en-]  über  avx'^j'^  s.  auch Schwjzer  Gr.  Gr.  I  296)^  got.  hals-agga  ^Nacken^^  klr.  vjazy  PL  ^Genick^^ cech.  vaz  ^Genick,  Nacken'  (zu  vezati  s.  o.);,  apr.  (als  slav.  L
=== leaf 51
w.)  winsus ,Hals'  (auch  arm.  viz  Jials'  mit  Präp.  v-?),  s.  Pedersen  KZ.  38,  311;  39,  402, Vondräk  Sl.  Gr.  I  184,  Adontz  Mel.  Boisacq  I  10,  sowie  unten  unter  augli-j ugh-.
Andere  Bildungen:  gr.  ayxövr]  ,Strick,  das  Würgen,  Erdrosseln*  (daraus lat.  angina  ,Halsbräune^),  äy-Air^  m.  ,Spange,  Verband^,  ^y^i,  dyxov, ayxö-d-i  ,nahe  bei^  (y^^-  ^^'Z.  ]pres  ,bei^ :  lat.  'pressus),  Komp.  äoGov  ,näher^ i^äyxiov]  ^ooov  ist  daraus  nach  f.ia(Tao)v=  *uax/wy  geneuert.  Osthoff  MU. 6,  60 ff.);  bret.  concoez  ,Druse,  etranguillon^  (*kom-angeid-]  vgl.  auch  dial. ancoe  , Zäpfchen  im  Ilals^;  Ernault  RC.  7,  314;  19,  314ff.);  aksl.  gzota  ,Enge^
Gall.  ON  Octodurus  bleibt  fern,  denn  ein  ir.  ocA^e.,angustia^  existiert  nicht.
Van  Windekens  (Lexique  5)   stellt  hierher  toch.  A  amgär  ,schwach^(?).
WP.  I.  62  f.,  WH.  I  47.
anghen-  ,Duft,  Gei'uch,  Persona
Arm.  aiijii  (für  älteres  *anj),  Gen.  anji'<^  ,Seele,  Wesen,  Person'  =^  anord. angi  m.  ,Duft,  Geruch^
Liden  Arm.  Stud.  38  f.,  WP.  I  58,  Meillet  Esquisse  77  ff.
3ng^(h)i'  ,Schlange,  Wurm-,  eg^hi-,  ogj^hi-  und  eghi-  ds.;  mindestens  zwei etymologisch  verschiedene,  aber  früh  verschränkte  Sippen,  deren  Ver- hältnisse noch  vielfach  unklar  sind.
Lat.  anguis  =  lit.  angis  (f.),  apr.  angis  ,Schlange^  (lett.  üodze  f.  ,Schlange*), aksl.  *gzh,  russ.  uz,  poln.  wqz  ,Schlange'^,  ai-m.  auj  (Gen.  -i)  , Schlange* (Meillet  Esquisse  154,  Dumezil  BSL.  39,  100);  mir.  esc-ung  ,Aal'  (*,Wasäer- schlange',  esc  , Wasser^  +  *ang'":ho),  cymr.  llys-yic-en,  PL  -yio-od  ds.  (Fick II  ^  15;  zum  brit.  Schwunde  von  i^g  vor  m  siehe  Pedersen  KG.  I  107).
44
Dazu  mit  Schwundstufe  und  unaspirierter  Media  (letztere  konnte  an  sich.« auch  im  Lat.  und  Balt.-Slav.  vorliegen)  ahd.  unc  ^Schlange,  Natter^  gr.j (illjr.)  ^ßsLQ'  sxeig  Hes.  (*ng^i-).
Diesen  Formen  mit  Media  zunächst  steht  Yußrjoig'  eVx^^t'g,  Msd-vixvaToil Hes.  (^eng^r^rl- :  zum  i  vgl.  Solmsen  ßeitr.  I  215),  woran  wegen  des  7'-Suffixes  i anzuschließen  sind  balto-slav.  *anguria-  in  slav.  *0(/orb  m.  russ.  i(g(o)n,] poln.  icegorz,  cech.  illiovy  serb.  ügor,  sloven.  ogor  ,Aal',  lit.  ungurys  ds.  (assim. ' aus  *angurijs,  vgl.  finn.  ankerlas),  apr.  angurgis  ,kdX'  (ksl.  (igulja,  jegidja^ ^AaF  wohl  aus  dem  Lat.).  Hirt  IF.  22,  67  verbindet  diese  gr.  und  balt.-^ slav.  Aalnamen  zu  einer  selbständigen  Gleichung  (doch  vgl.  das  ?"-Suffix  r von  ahd.  angar  usw.,  s.  unten).  j
Eine  andere  idg.  Gleichung  für  ^Aal'  ist  vielleicht  gr.  eyxekvg  i.,  lat.  5 anguilla  (s.  bes.  W.  Meyer  KZ.  28,  163,  Johansson  KZ.  30,  425,  J.  Schmidt KZ.  32,  369,  Osthoff  IF.  4,  270,  29j^,  Hirt  IF.  22,  67,  Idg.  619  f.),  wenn- gleich die  Einzelheiten  noch  unklar  sind  (im  Gr.  *äyxeXvog  usw.  zu  iyxs^vog  ' assimiliert,  oder
=== leaf 52
  das  s  und  der  i-eine  Gutt.  durch  Einfluß  von  .e'xig]  im  ^ Lat.  -üla  statt  -ella  nach  dem  Schwanken  in  echten  Deminutiven  unter  1 entscheidendem  Einfluß  des  i  von  anguis7).
In   der  Bed.  ,Wurm,  Made^  und   mit  r-Suffix   (vgl.  oben  üfißr^gig  usw.):; ahd.    angar    ,Kornmade^    eugirinc    ,Larve^,    nhd.    Engerling,   lit.    anksfirai ,Maden,  Engerlinge'  (und  ähnliche  Formen,  s.  Trautmann  Apr.  301),  lett.  ; anksteri   ,Maden,   Engerlinge",   apr.    anxdris   (d.   i.    anxtris)    aber   ,Natter^ (über  das  -st-  dieser  halt.  Formen  vgl.  Mühlenbach-Endzelin  Lett.-D.  Wb.  I  ; 71),  russ.  ug{o)rh  , Hitzblatter,    Finne^    (auch    ,AaP,    s.  oben),   poln.    icagry ,Schweinsfinnen'  (Bezzenberger  GGA.  1874,  1236,  BB.  2,  154;  nicht  besser über  angar,  ugorh  ders.   GGA.  1898,  554 f.).  i
Nasallose  Formen: .    Gr.  exig  m.  (f.)  .Schlange',  Mx^^va   ds.  (für  *ey^idvLa,  Specht  Dekl.  377), ahd.  egala  ,Egel^,  dän.  norw.  igle  ,ein   schmarotzender  Blattwurm   in  den Eingeweiden  der  Tiere  und  in  der  Haut  und  den  Kiemen  der  Fischet
Hierzu  gr.  sxivog,  ahd.  ags.  igll  (idg.  '^eghinos),  nhd.  Igel,  eigentl. ,Schlangenfresser^,  W.  Schulze  Gnomon  11,  407,  lit.  ezys,   ksl.  jeh  Jgel*.
Arm.  iz  ,Schlange,  Viper^  kann  als  *6g'^hls  zu  h'q)ig  gestellt  werden (Meillet  Esquisse  75);
gr.  ocfLg  ,Schlange^  (^og^his):  cymr.  euod  (*og'^h-)  ,Schafwürmer:  ai.aÄi-, av.  azi-  ,Schlange^
Unsicher  ist  Anreihung  von  as.  egithassa,  mnd.  egidesse,  ags.  (verderbt) äpexe,  ahd.  egidehsa,  nhd.  Eidechse  mit  ewi-,  egi-,  idg.  *og]'hl-  =  Ucpig (Zupitza  Gutt.  99  nach  Kluge;  Falk-Torp  u.  0(jle)  +  germ.  ^pahsiö,  ahd. "^dehsa  ,Spindel'.
45
Ol)    in  diese  Mannig-faltig-keit  so  Ordnung  zu  bring-en  sei^  daß  *a7dg]iJä- nd  *eghi-,  '^ogld-   (gh)  eine  Kreuzungsform   *eglihi-^  '^o(ßhl-  liervorgerufeii 1  ••Uten    bleibe  dahingestellt.  Wahrscheinlich  haben   dabei   aucli  Tabu-Vor- stellungen mitgewirkt.
AVP.  I  63 ff.,  WH.  I  48,  Specht  KZ.  64,  13:  ^:>^^,  56  f.,  Ilavers  Sprach- tnbn  44  f.
/.  ank'  ,Zwang,  Notwendigkeit^
Gr.  dvdyyiT]  ,Not wendigkeit,  Zwangt  (gewöhnlich  als  i-edupliziert  ange- sehen),  ion.   ävayxair]   ds.    (von  dvayy.aTog  ,notwendig^,  dvayÄaCcx)  ,zwinge');
air.  ecen  (ec-  aus  *ank-  oder  *n^c-),  mcymr.  anghen^  cymr.  angen,  corn. bret.  anken  ,Not,  Notwendigkeit^,  im  Ir.  auch  ,Gewalttat^
Obwohl  , Zwangt  aus  ,feiudlicher  Bedrängnis,  Verfolgung^  verständlich wäre,  macht  die  gr.-kelt.  Bed. -Üb
=== leaf 53
ereinstimmung  es  doch  fraglich,  ob  das lautlich  übereinstimmende  ahd.  ähta  ,feindliche  Verfolgung^,  nhd.  Achty ags.  öht  (urgerm.  *anxto),  germ.  EN  Äctumerus  (d.  i.  AytuweraZy  1.  Jh. n.  Chr.;  Brugmann  Grdr.  P  382),  womit  ir.  echt  (*anktu-  oder  *nktu-, *e7iktu-)  ,Totschlag'^  zunächst  zu  verbinden  ist  (s.  Falk-Torp  17,  1430), wLirzelhaft  mit  anÄ:-  , Zwangt  (:, bedrängen,  töten^?)  ursprünglich  gleich ist,  oder  zu  *enek-  ,töten^  gehört,  wie  auch  hitt.  hi-in-kdn^  ht-en-kdn (henkan)  ,Tod^
WP.  I  60,  Pedersen  Hittitisch  183  f.,  Hendriksen  Unters.  28,  Benve- niste  Origines  155.
2.  ank-,  ang-  , biegen^;  Nominalstämme  anko-,  onko-;  ankes-;  anku-lo-; anken-,  -on-;  ankoto- ;  ankro-.
Ai.  ancati  (mpers.  ancUan)  und  (tiefstufig)  dcati  ^biegt,  krümmt^,  Partiz. -akna-  (mit  ä-,  ny-,  sam-),  -akta-  (mit  ud-^  ny-)  ,gebogen^;  aidkd-h  m. , Biegung,  Haken,  Biegung  zwischen  Brust  und  Hüfte*^,  ardkas-  n.  ,Biegung, Krümmung^  (=  gr.  to  liyy.og  ,Tal,  Schlucht^,  ar^kasdm  ,Seite,  Weiche'; cwku-  in  aTdküydnt-  ,Krümmungen,  Seiten Avege  suchend.*^;
av.  anku-pdsdmna-  ,mit  Haken,  Spangen  sich  schmückend"^,  ai.  ankucd-h ;Haken,  Angelhaken,  ElefantenstacheP,  aTdkurd-h  ,junger  Sproß,  Schößling (ursprüngl.  Keimspitze,  gebogener  Keim),  Anschwellung^  (=--^  gr.  dyy.vlog ,krumm^,  dt.  Angel,  anord.  öll,  äZZ-, Keimblatt,  Keim^  s.  u.);
av.  aka-  m.  ,Haken,  Zapfen^,  axnah  (ßartholomae  Stud.  2,  101,  Airan. Wb.  359)  ,ZügeF;
gr.  dyy.(bv  ^Bug,  Ellenbogen^  (D.Pl.  dymoi  zu  dyAri  =  dyy.dlri),  iTt-rjy^isv-Ldsg .die  an  den  dyKÖvsg  (Rippen?)  des  Schiffes  befestigten  Bohlen^  (Döderlein, Bechtel   Lexil.   129),   IcyytOLva   ,alles   Gekrümmte^,   UyY.iorQOv  .Angelhaken';
4G
äyycvXog  ^krumm^^   dyxvXi]  ^Riemen*    (=  anord.  ol^  al  ds.),  ^yy.voa  .Anlcei dyAccXfj  .Ellenl)Og-en^  Bucht,  alles  Gekrümmte^;  tö  äy/.og  (s.  o.).
Mit  o:  oyxog  ^Widerhaken^  ==  lat.  uncus  ^g-ekrümmt;  Subst.  Flaken] {oy'/.lvog=  unclnus  Jfaken^  Widerhaken'^);  nngulus  ^Fing-erring^  Pacuvius] von  Festus  514  L.  als  oskisch  bezeichnet^  ungustiis  ^fiistis  uncus'  Paulus ex  Fest.  519,  s.  unten  unter  ang-)]  ^y/,fj'  ywria   Hes. ;
lat.  anciLS  ^qui  aduncum  brachium  habet^_,  ancrae  .convalles.  vallis^ (^Krümmung;  Einbuchtung^  wie  tö  fy/.og  =  germ.   *angra-)]
air.  tcath  ^»Fischhaken^  =  cymr.  angliad  ^Griff,  Hand'  (zu  craf-arn ,Klaue^)  aus  "^cmkato-  =  aksl.  gkoth  ^Haken'^;
gallorom.  ancoi'ago,  ancora(y)iLS  aus  ^miko-räkos  ^Rheinsalm,  Hakenlachs' schwd.  Anke  ^Bodenseeforelle'  (g"^^l-  *cinko-  ^gekrümmt'  und  *7'äko-  ,vorne^ aus  *prökO',  cymr.  o^hag  ;Yor^);
ahd.  angoj    angul   ^Fischhaken^    Stachel'^    aisl.  angi^    ags.   onga   ^S
```


## [2026-09-04T22:41:40.999Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"anghos\\|anghu\\|angh-\\|ang\\\"hi\\|anguis\" WLD_Bd1_pages.txt | head -40",
 "description": "Grep Walde-Pokorny Bd1 for angh"
}
```


### [2026-09-04T22:41:41.079Z] TOOL RESULT

```
5610:angh- (kelt. aueh engh-) „eng, einengen, schntiren“, z. T. auch von seelischer
5673:     *anghos-, *anghes- „Beklemmung, Bedrangnis“                n. „Angst, Be-        :   ai. cuiihas-
5679:(wohl aus * anghos-to-s oder mit altem, aus dem Adj. *anghu- bezogenem
5682:Schade, Betrfibnis“, afries. ongost, ahd. nngast, nhd. Angst (aus *anghos-ti-
5683:nach *anghu- umvokalisiert) aksl. qzostb ,.Beengung“; lit. ankstas „eng“
5727:auch alum oder cdus „Symphytum officinale*' aus *angh-slo-m als „zusammen-
5737:u. take- „schweigen“) ist mit *angh- unvereinbar und hochstens auf eine
5914:(Yf. LEWb. 2 u. anguis), bleibe dahingestellt.                                — DaB *ang*(h)is als „con-
5915:strictor“ (Fick II 4 15;                Fay Transact. Am. Phil. Ass. 41, 37 f.) zu angh- ge-
14951:lat. sanguis als Verbindung des «-St. der Kasus obi. *(j)st n- mit dem nomi-
66404:                       angh- „einengen“ bei Collitz Praet. 80_ wegen des
```


## [2026-09-04T22:41:41.844Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^angh-\\|^angh\\|^ang.*narrow\\|angh- To\" AHD_watkins1985.txt | head -20; echo \"---egwh\"; grep -n \"^angwhi\\|^egwhi\\|^ogwhi\\|angwhi-\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins for angh and angwhi"
}
```


### [2026-09-04T22:41:41.914Z] TOOL RESULT

```
---egwh
1986:OPERA! op-! OPERATE op-! OPERCULUM_ wer-5 OPEROSE op-! OPHIDIAN angwhi- OPHIOLOGY angWhi- OPHITE angWhi- OPHIUCHUS angwhi-, segh- OPHTHALMO- ok¥- OPINE op-2
```


## [2026-09-04T22:41:46.841Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"angh\" AHD_watkins1985.txt | head -30; echo \"=== angwhi lines\"; grep -n \"angwhi\\|angWhi\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD text for angh/angwhi occurrences"
}
```


### [2026-09-04T22:41:46.899Z] TOOL RESULT

```
282:b. Old Norse um/(b), about, around: OMBUDSMAN; c. Old High German umbi, around: UMLAUT. 3. Latin ambi-, around, about: AMBI-. 4. Greek amphi, around, about: AMPHI-. 5. Celtic *ambi (see ag-). [Pok. ambhi 34.] ambhé. Both. 1. Reduced form *bAd in Germanic *b6-, *bé in Old Norse bdthir, both: BOTH. 2. Latin ambé, both: AMBSACE. 3. Greek amphé, both: AMPHOTERIC. [In Pok. ambhi 34.] amer-. Day. Suffixed form “Gmer-d in Greek hémera, day: EPHEMERAL, HEMERALOPIA. [Pok. dmer- 35.] ames-. Blackbird. 1. Suffixed variant form *ams-ol- in Old English dsle, blackbird: ouzEL. 2. Suffixed variant forms *mes-old, *mes-olo- in Latin merula, merulus, merle, blackbird: MERLE, MERLON. [Pok. ames- 35.] [amma. Various nursery words. Latin root. 1. Medieval Latin amma, mother: AMAH. 2. Reduced form *am- in: a. Latin amare, to love: AMATEUR, AMATIVE, AMATORY, AMORETTO, AMOUR; ENAMOR, INAMORATA, PARAMOUR; b. Latin amita, aunt: AUNT; c. Latin amicus, friend: AMICABLE, AMIGO, AMITY; ENEMY, INIMICAL.] an’. On. Extended form *ana. 1. Germanic *ana, ané in: a. Old English an, on, a, on: ON; b. Old Norse 4, in, on: ALOFT; ¢. Old High German ana (> Middle High Ger- man ane), on: ANLAGE; d. Middle Dutch aan, on: ON- SLAUGHT. 2. Greek ana, on, up, at the rate of: ANA?, ANA-. [Pok. 4. an 39.] an?, Demonstrative particle. Suffixed form “*an-tero-, “other (of two)” (compare *al-tero- under al-') in Ger- manic *antharaz in Old English 6ther, other: OTHER. [Pok. 2. an 37.] an-', Old woman, ancestor (nursery word). Latin anus, old woman: ANILE. [Pok. 1. an- 36.] an-2. To pour, draw water. Suffixed form *an-tlo- in Greek antlos, bilge water, bucket: ANTLIA. [In Pok. 1. sem- 901.] andh-. Bloom. Suffixed form *andh-es- in Greek anthos, flower: ANTHEMION, ANTHER, ANTHESIS, ANTHO-, -AN- THOUS; AGAPANTHUS, CHRYSANTHEMUM, DIANTHUS, EX- ANTHEMA, HYDRANTH, (MONANTHOUS), STROPHANTHIN. [Pok. andh- 40.] andho-. Blind, dark. Suffixed variant form *ondh-ro- perhaps in Latin umbra, shadow: UMBEL, UMBRA, UM- BRELLA; ADUMBRATE. [Pok. andho- 41.] ane-. To breathe. Suffixed form *ana-mo- in: a. Latin animus, reason, mind, and anima, soul, spirit, life, breath: ANIMA, ANIMADVERT, ANIMAL, ANIMATE, (ANI- MATO), ANIMISM, ANIMOSITY, ANIMUS; EQUANIMITY, LONGANIMITY, MAGNANIMOUS, PUSILLANIMOUS, UNANI- mous; b. Greek anemos, wind: ANEMO-. [Pok. 3. an(9)- 38.] anata. Doorjamb. Latin antae (plural), a pair of pillars on the opposite sides of a door: ANTA. [Pok. anatd- 42.] [angelos. Messenger. Greek noun, akin to Greek anga- ros, mounted courier, both from an unknown Oriental source. 1. Greek angelos, messenger: ANGEL, (ANGELIC), ANGELICA, (ANGELUS); ARCHANGEL, EVANGEL. 2. Greek angaros, mounted courier: ANGARY.] angh-. Tight, painfully constricted, painful. 1. Germanic *ang-, compressed, hard, painful, in Old English ang- nzgl, “painful spike (in the flesh),” corn, excrescence (nzgl, spike; see nogh-): AGNAIL. 2. Suffixed form *angh-os- in Germanic *angaz in Old Norse angr, sor- row, grief: ANGER. 3. Suffixed form *angh-os-ti- in Ger- manic *angusti- in Old High German angust (> German Angst), anxiety: ANGST. 4. Latin angere, to strangle, draw tight: ANxious. 5. Suffixed form *angh-os-to- in Latin angustus, narrow: ANGUISH. 6. Greek ankhein, to squeeze, embrace: QUINSY. 7. Greek ankhoné, a stran- gling: ANGINA. [Pok. angh- 42.] angvhi-. Snake, eel. 1. Latin anguis, snake: ANGUINE; ANGUILLIFORM. 2. Taboo deformation or separate root *ogvhi- in Greek ophis, snake, serpent: OPHIDIAN, OPHITE; OPHIOLOGY, OPHIUCHUS. 3. Taboo deformation or separate root *eghi- in Greek ekhis, snake, in deriva-
1219:AGIO al-1 AGITATE ag- AGLET ak- AGMINATE ag- AGNAIL angh- AGNATE gene- AGNI egni- _ AGNOMEN no-men- AGNOSIA gnd- AGO ghé- -AGOGUE ag- AGONY ag- AGORA! ger-1 AGORAPHOBIA ger-! AGRAFFE ger-2 AGRAPHA gerbh- AGRAPHIA gerbh- AGRARIAN agro- AGREE gWere-3 AGRESTAL agro- AGRIA agro- AGRICULTURE agfo- AGRIOECOLOGY agro- AGRIOLOGY agro- AGROSTOLOGY agro- AHIMSA ghei-i, ne AHRIMAN men-1
1245:-ANDRY ner-2 ANECDOTE d6- ANELE elaia ANEMO- ane- ANEROID newo- ANESTHESIA au-5 ANEURYSM were-! ANFRACTUOUS bhreg- ANGARY angelos ANGEL angelos ANGELIC angelos ANGELICA angelos ANGELUS angelos ANGER angh- ANGINA angh- ANGLE! = ank- ANGLE? §ank- ANGLE ank- ANGST angh- ANGUILLIFORM ang¥hi- ANGUINE ang¥hi- ANGUISH angh- ANHYDROUS wed-! ANIL nei-
1251:ANVIL pel-6 ANXIOUS angh- ANY oi-no-
2154:QUINATE penkWe QUINCUNX  oi-no-, penkwe QUINDECENNIAL at-, penkWe QUINQUAGENARIAN penkWe QUINQUAGESIMA penkWe QUINQUE- penkWe QUINQUENNIUM at- QUINSY angh-, kwon- QUINT! penkve QUINTAIN penkwe QUINTESSENCE es-, penkwe QUINTET penkwe QUINTILE penkwe QUINTILLION penkwe QUINTUPLE penkwe, plek- QuIP k¥o-
=== angwhi lines
1986:OPERA! op-! OPERATE op-! OPERCULUM_ wer-5 OPEROSE op-! OPHIDIAN angwhi- OPHIOLOGY angWhi- OPHITE angWhi- OPHIUCHUS angwhi-, segh- OPHTHALMO- ok¥- OPINE op-2
```


## [2026-09-04T22:42:01.769Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zaŋh\\|zanh\\|azah\\|qzah\\|ązah\\|ny-āz\\|nyāz\\|ny-az\\|nyaz\" BRT.txt | head -40",
 "description": "Grep Bartholomae for azah/nyaz"
}
```


### [2026-09-04T22:42:01.821Z] TOOL RESULT

```
4380:•  j.  aii-a'haxta-'>  Adj.  'der  nicht  berech- tigt (geeigenschaflet  und  ermächtigt)  ist {etwas  zu  tun)':  yS  anyahe  ^apynnäyüka ^'lä'^  a'^aurufiTttt  paraahacäiti  "wenn einer  eines  andern  Kind  unberechtigt  3'  zu priesterlichem  Dienst  mit  sich  wegfiihrt" N.7;  6;  —  'tö.  .  ahaxts  (sd,)  N.tf;  — haxts . .  'ts  N.  6-,  — yasta  aSlalsam  mazda- yasnanqm  tnyazdavanam  aüanhqm  yat myazdanam  "ts  parabaraiH  nsit  täyul ,  . bavat  .  ,  ainyi}  kasat  .  .  "und  wer  von den  ,  .  M.  etwas  von  den  My.  wegnimmt, auch  ohne  berechtigt  zu  sein,  der  , . ;  aber irgend  ein  andrer  .  ."  N.  6^;  —  yezt^a *aile  ratavö  *'ta*^  *para.iyayanH  "und wenn  die  R.,  weil  (zu  ihrem  Amt)  nicht qualifizirt,  weggehen"  N.  ^o;  —  zaota  (sd.) *-ßS)  parayat  N,  So.
4385:•  j.  an-ahü-  Adj.  'der  keinen  Aha  (sd.) hat';  ahmaofanqm  .  ,  °ahunqm  aratunqm Yt.  /^.  I  o  5 ; — *anaKruA3i?)  ">  arafvS  acisifm duzanhavS  "das  Schlimmste  der  Hölle  ist fiir  den,  der  keinen  A.  und  R.  hat"  P.  14.
4418:•  j.  an-ä'dnixta-  Adj.  i)  'unbelogen,  un- betrogen':     apa    haca    qzanhtbyiS    tnihra
4461:•  ],  an-azah-  Adj.  'der  keiner  Bedrängung ausgesetzt  ist,  keine  Not  kennt";  mi^r^m . ,  yet'ihe  mag'i^anpm  .  .  °zS  Yt-jo.44.
4679:tsin  aiare^  utä  'niyä  bagäA^  lyaty  At^tiy Bh.  4-  ■  2  >  13;  —  "^'"i  vahistsm . .  'iiya^qm yat  anifsanqm  spmtanqtn  YL_j,3;  —  yetii zT  MS  maiysia  .  .  yazayanta  yak:a  'nye yazaiinhe  . .  yazinti  ". .  wie  dae  andern y.  verehrt  werden"  YtÄii;  —  ahe  nars asaofiB  ..  äai  'nyazsqm  asaonqm  Yti.30; i3-  ^Ti  —  airime  gstüm  kl  nUhka^a  .. *par^itar?m  kala  'uyalibyd  mazdayas- f>aiibysY.(}.^y, —  'nye  aaksus /rals.iar^ %ra  Aog.65(?)'';  —  \'.ulä  pärsJ' uls  msdt^ utä  "niyS  dahySve^  Bh. /.  13,  14;  11;  — psrsaiy . .  msdaiy  utä  'niy^uvä  dakyusuvä Bh.  J.  10;  —  ahmäi  nmsnäi  daaäiti  gBu^ca vq^iwa  . .  upa  'nya  (APn.)  sHndayäti  Yt /o,  2  8 ;  —  vätB  , ,  AubaoioitarS  . .  'nyalifyö vstaeihyö  H.2.7;  25,  V.j.ss,  ^,29,  Vyt. 45i  —  ""^  a%ra  frakavB  mä  apakavB  . . maia.cim  'nyqm  (GPn.)  daxstanqm  V,  2. 29;  —  ahtnavaila  (sd.)  gäkanqm  .  . uilavaitTm  hsitlmca  , .  av5  yS  °nya  (näml. gä'^h)  srSvaydii  N.  46.  a)  Plur.  mit folg.  äi  'auch  die  andern' :   tl  mqm  ava%a
5018:•  j.  avaänö-mazah-  Adj.  'was  (noch)  ge tingeren  Pfandwert  hat"':  B3ii  sT  akurs
5160:'  °vanhasca  *"irH~irahe^a  V.44-',  -^  "^rJ- ^/■i7(  g3ui'  . .  "vaitihe  narqm  asaonam  Yt. /^.  10;  ig.6g;  —  'variAe  narqm  asaonqm qzanhe  duzvarHm<ar3tqm  Yt.  JJ.  39;  — ä(a  ^wa  sbayai  'vaifihe  Yt./O.??,  78;  83 —86',  /J.28,  35,  (?.  a;    —    äca    nS    jam-
5594:acht Renoer", Name  cinesGebirgs*>:  ahmat\  j.  »arazah-  n.  'Abend':  yai  uHrSAva ha:a    garayl   fraoxiyqn  .  .    asta    'vants  m»r)neaite  (sd)  -zahva  bisasyät  V.2/.3. fitnkOfö   (sd)    YL  Jp.3.  [Vyt.  IQ:    lies       Et.?   Vgl.  Gdn.  Stud.  /.  51.  —  Vgl.  anzt-hU
5596:gr.  'OtKTT^;!  in  HamaJän.  ',  j.  atazahi-  (n^)  Name  des  im  Westen
5868:asp9r9DÖ.mazah-
5870:•  j.    aspar^nö.mazah-   Adj.    'was    den  |
6311:•  j.  a^-vazah-  Adj.  'das  Aia  fördernd': haomahe  °zar>As  Y.  lO.  i,  8.^,  S.  /.  30,  Yt 20-0,  3.
6319:Zum  V.  Mz-;  ai.  vähas-  n.  (ZDMG.  50.  4*8). —  PU. :  ahtmi  zSyak;  s,  zu  asavazah: —  Vgl. dsavazah;  asakyä  vazdting  und  ai.  ftäsya vähiuä  RV.  8.  6.  2.    Falsch  BB,  15.  11.
6862:■rahe  mazdä  Vr.  14.2;  — yeAh! hltqm  äat yesng  (sd)  paitl  vai)hd  mazdä  'rS  vag'iä Y.  27. 1 5 ;  —  äppm  zazahi  tarn  ys  °rS  mazdä zrayaahal ha'a  z'ouru.kas-lt ha'^ra  Täi?mca dunmqnca  V.5.  15;  isf.'.  60;  —  a'iä  Ml (sd.)  °rB  ma-id\  zard^ustr^m  aoaxsayaUa Y.  /2.  S ;  —  ar>dvlm  . .  yahmya  °rS  mazda ivaiiayal  Yt.  5.85;  —  imat  t!  saahat
7853:Vgl.  gt.  äna,  lat  angö;  s.  auch  qzah-  und No.  I.  —  Pü.:  awialan.  —  «)  Ob  statt  nyas" geschr.?  VgL  S  ^68.  3  a;  s.  aber  np.  niyäz 'Maogel'  bei  Hbm.  AGr.  /.  105,  Weiteres, auch   la    aL    anSha,   IF.  8.  235.    —  »)   VgL
11972:tanumazah-
11975:'tanu-mazah-  n.  'Grösse  des  Leibes':
12000:•    j.    nanu.mazah-    n.    'Pfandwert    des      /'"^«™«^-
12451:•  j.  daenä'vazah-  m.  EN.  eines  Gläubigen : 'zanhs  asaonS  Yt  13. 117.
14511:'etwas  aufschichten,  häufen  auf—'  (Akk.): stirmaoiti  .  .  stanm  (sd.)  . .  ya%a  nar>m aiavarum  "duscä  zanhm  uparSi  naimat nasus  aoi  ava  *^ravlt  ".  .  als  ob  er  auf einen  altersschwachen  Gläubigen  von  oben her  Leichenteile  aufhäufte"  P.  2j.
14892:causa':  ySi  vanhd^ra  framanydnte  (sd.) VJtar».qzahyekeca  'ti ..Y.  6^.  13.  S) 'ge- mäss'(?);  AämS.fyaokna  .  .  bavainti  a^ahe 'ti  pantqm  alahe  °ti  mq'^r>m  asahe  °ti /rasastlm  Y.4-  43.  ^)  ^ur  Bezeichnung
14893:von  Vorgängen  und  Umständen,  die  die Satzhandlung  begleiten  oder  die  Voraus- setzung dazu  bilden,  'bei';  i)  mit  Lok.: ahß  at  'tl  adäkü  .  .  büiricä  kar^hia  . . xrapaitT  (sd.)  hyai  ahmat  aibl  Y.  4°. 1.  i)mitAkk.:  ma  yave  imal  nm3t»m  . . s^annB  /razahlt .  .  n^äkrS.disyehe  (sd.)  'ti a^iila  . .  haxma  Y.6o.j; .  .   manB    rämayeiti  [huxsnßittm  (sd.)
15470:(s.  ebenj.  3)  'von  —  her,  von  Seiten', mit  Abi.:  yat  bavaiti  avi.spaslB {sA.)  sssta . .  aurvd^aiibyB  tb  tbisyanbyB  Yt.  13, 69;  — neben/(7r><  i';  vUarf.qzahyehe{sd.^ca  patli . . pairi  *Aalnyäs!a  vBiynäuyB  aurva%aäbyasca •rB  pifyanbyö  Y.  68. 1 3.  4)  'mittelst;  mit Hilfe  von  — '  (Abi.):  yim  yazata  haomB .  .  anähimt  'rB  barismm  Yt  iO.  88;  88'; —  yüsmaoyB  'rB  karsnazB  hvira  baon  Yt. '.?■  38;  —  y<ii  3s  masyanqm  . .  aoji^B  ,  . nairyayät  'rB  hqm.vtrttBil  yat  dim  uparfha- cat    hqm.variilil  Yt  J(J.  jSf.  5)    'um
15542:'vor—',  neben  parö:  aoa  ..  nS  ..  ntpaya .  .  'ri  dniatat  mahrkai  'ri^  . .  aistnake pars  draomSbyS  Y.  57.  25;  JÄ'.  2  ">,  SrB.j; —  th  (Täxüi.frtrvasay^)  .  .paritasca  pairi- värascä  vUfnte  'ri  mainyaoyät  drujat  Yt. ^J-7ij  71;  —  ya'ka  ..  dadränS  m  'ri iri>yqstätal(sd.)  Aaraite  Y.ip.io.  d)  wie lat  ab  zur  Bezeichnung  des  Anlasses, neben  parff:  viian.qzahyehei^A^ca  paiti  . . 'ri"^  *halnyäsca  vöiynäuyU  aurva- byasla  parö  Y.6S.i$.  e)  'ohne' aufTalliger  Verwendung:  yim  antan  äkitim ramm  frajasäi  (Sp.  goo  o.)  afranhansäl (Sp.ioi  o.)  'ri  xi'udrätV.i6.i6"\  4)  mit Instr.;  i)  'ex  — ',  beim  V.  'zan-  mit  /r 'cognoscere':  yS  aSa  (Sp.  11  u.)  -n'' ariira  frasänaiti    F.5.  2)  pairi  SiS
16046:pazahvant-
16420:PPA.;    Praes.  I  oder  3.    —    Vgl.  ai.  finöüi,   „mä/iyB  (näml.  ralus)  vTsyB  zanhimB  däR-
17243:•  j.  bazah-  n.  'Höhe,  Tiefe':  avervaitya °zas/a  fra%as{a  .  .ya^a  im  z3,  astica  tm zä  avaiti  °z5  yavaiti  /raiiascit  "soviel  an
17807:•  g.  fra-vazah-  Adj.  (auch  fem.)  'vor- wärts fliessend':  apä  .  .  maeiaintii\sd.)cä *hibavaintiBi  'zanhö  (APf.)  Y,  JÄ  3.
18421:•  j.  ßt^a-  m.  i)  'weibliche  Brusf,  Du.:  Aä hl  mailim  nyazata  (sd.)  ya%aea  huk^r^ta 'naya^aca  anhin  niväzäna {sd.)Yl.S-i^7i F-JS'  2)  'Wölbung  der  Brust',  um  die Brustwarze  herum  riÄtft'wOT(bz.Äö>«OT)  'n^m V.Ä53— 54*,  p.  19*.  3)'Buckel,Knoten' (nur  Komp.).
19218:•  j.  nivizan-  Adj.  'anziehend,  reizend,  1 '^'''*  Yt/5. 45,  Geringe  Stelle. gefällig'  ■>:  Äa  hi  maiUm  nyazata  ya^aca  .  ,  j.  nisma-  m.  '(Hineingehen  in  den  Erd- hukfr)ptaßtänayai!aca  anh)rfz3nal^'Q:)  \^o^^^  sva.)  Tiefe':  paoirjm  upa  vmy>m "äe  schnürt  sich  ihre  Taille,  damit  '-^tz  ■  ni>:w>rnöil  .  .  dva  »rssu  -mähe''»  "das Brüste  schöngestaltet  und  damit  sie  gefällig ,  erste  Loch  sollst  du  .  .  zwei  Finger  in seien"  Yt 5.127.  der  Tiefe  ausstechen"  V.o.  6.
19363:•  )•<  E-.  P-  'inä  prohib,  Part  "nicht,  ne,  fi.-^'; drückt  aus,  dass  man  das  Eintreten  der  Sau- aussage nicht  haben  will  mä  tritt  a)  an  die Spitze  des  Satzes  oder  b)  vor  das  Verbum ''. Gilt  die  Aussage  von  mehreren  Nomina, so  wird  m3  wiederholt  (doch  s.  No.  3),  an letzter  Stelle  erscheint  dann  auch  mala (statt  iwa).  i)  mit  Inj.  des  Verbs;  zu  a): iux/ährä  x^ntqm  (sd.)  ma  rß  *du/^xia^rä xsima  Y.  48.  5 ;' —  m  a  S^l  ai  vS  dngvatö mq%rqs!a  güHä  sämatca^^  Y.ji.jS;  — väfva  (sd.)  vtdusl  tnraotu  mS  »vTdva  aipl.- dSbavayatY.31.1-j;  —  mä  »r  ahmt  nmatu mai  ../rfm  vaocata  mqm  ..  V.iy;  — m  3  yave  imat  nmäium  . .  ^artnS  frazahJt /nS' ..  Y.60.  7; —  tnSca  pas!aäa  masda- yasna  tarn  sqm  karaym  mä  äpö  himaygn V.  6'.  a ;  —  mäia  pascaila  mazdayasna vTmshasäf  vTmahayatUa  V,  7.  38*';  —  ma äim  pfnsS  yim  pfrysaki  H.  2. 17;  —  mS m?r?ruainTs  astvaitli  galhä  SrB.  3;  — mä  mqm  . .  Vj^ä»/ VyLfo.j  —  s.  noch zu  6.  zu  b)    am?m  mq^nm   mä  fra-
20165:•  j.  'mazah-  n.  i)  'Grösse,  Umfang' :  _>iaj:& .  .  daxmanqm  avavantpm  'xS  vltsnayäj ya^a  hl  tanus  aahat ". .  (soviel  an  Grösse als  . .  sva)  ein  Stück  so  gross  als  . ."  V. 7.  51.  2)  (etwa)  'Fülle':  'zJ  avahyai  °tS raßmSJiyai  däidl  hauruatä  am>r>tätü  "ge- währe zur  Hilfe  die  Fülle,  zur  Unterstützung die  FüUe  des  H.  und  A."  Y.  5Ä  7.
20169:•  j.  ^mazah-  Adj.:  s.  unter  masyak-.
20173:—  at  fravaxsya  vTspanqm  Htm  "ich  will reden  von  dem,  der  der  grösste  ist  von allen"  Y.  4S-  6;  5?-  8;  —  ahur?m  mazdqm , .  'hm  yazahm  Y.  16.  1;  —  ahurS  mazds yB  'ts  yazatanqm  yB  vahiltB  yazatanqm Yt.  77. 16;  70.  142 ;  —  ätarl . .  'ta  yazata Ny.  j.  4.  b)  in  Verbindung  mit  vaki^ta- imd  sral^ta-:  ya%a  nS  'täsca  vahistasSa sraeitasia  a/ayS  ^nnavante  Y.S2. 3;  —  as/a zadhranqm  'taca  vahiitaca  sralliai^a  N.£^;
20244:}.,  g,  mazyah-,  j.  mazah-'>  Adj.  'der grössere,  gewaltigere',  an  Umfang,  Bedeu- tung usw. :  ya^/a  ahtnat  aiti  'sys  . .  vatthB ,  .  srayd  .  .  ta^  nB  dsyata    Y.  ^5. 14;    — katürim  asavä  va  dngvä  vä  vfranvaiil(sd.) "sys  Y.3i.i-j''>;  —  vrsmie  avat  vTstnta^a *matyasat^'>  Yt  i^.  7  3 ;  —  izyati . .  tavavat (sd.)  ,  .  *°zyasät^  'Vyt.30;  —  'xanham'^ va  ifaram  (sd,)  N.^IJ. Komp.  zu  mtu;  matanl-.  —  u.  vgl.  mäl^ai- Adj.  —  Pü.!  miuO,  {lu  N.):  mid,  —  '»S50. 3.  —  »)  Vgl.  V,  38.  5.  —  1)  Hds,  matdyasfit (mit  Yat.),    Der  Verf.  des  Vjrt.  fand  &1eo  die Verderbnis  in  Vt  13.  72  bereits  vor.  —  4)  Zn Y.  31  mit  der  ErL  luxiamä/ar.
20876:35ra.)  ..cikayatö'F.^c;  —  mitGen.part.: yasca  altailqm  viazdayasnanqm  .  .  nötl *vTsaile  framrüite  aitqm  a  .  .  jasatti  Y. <y.4;N.6j; — *pouru.nar?m  tum  ktnnBsi . .  yas?  tl  . .  iaxsaite  ", .  (eum)  facis qui  . ."  Y.  10. 13;  —  n^armS  .  .  yat  upa- nhacaiii  yS  avatä^  fraxsayeite  ".  .  quod sequitur  (eum)  qui  . ."  Yt/9. 66; —  Cßw ..  nmän^m  da^äM  b>rnimit?m  yas?  %wä .  .  yazaite  ".  .  domum  (eius)  qui  .  ."  Yt. 70,30;  —  Aa  yaoidä  yS  Avqm  anhvqm yaozdäite  ".  .  puriücatio  (eius)  qui  .  .**  V, Y,  ö's.  10;  —  paoiflm  aitassqm ^adknanqm  . .  yS  narym  afavantm  .  . \  kasyanhe  (sd.)  satthäi  da%aiH  "die  erste dieser  Taten  . .  ist  (die  dessen,  der . .  sva.) wenn  man  . ."  V.  75.  a;  3,  5,  7,  8; —  kva i  asti  spa  vohunazgs  (sd.)  däityB^ätuli  . . \yj  naicim  isaiü  hunaranqm  "ubi  est  canis ',  .  aptus?  . .  (apud  cum)  qui  .  .  "  V,  7_j. !  19;  17,  18;  —  aheca  ank^uf  .  .  yasta asti  manahyS  "et  huius  vitae  et  (illius) quae  est . ."  Y. 57.  25;  —  cvathya  *nä  nitt- malibya  hävanailbya  (sd.)  *ratufrisl  *yä (NDm.) . .  '^hÜj^istö  (sd.)  N.  io8\  —  ^a- rata  ..  *ysi.dim  hauhäna  (sd.)  ,  .  "editc  . . (is)  qui  (vestrum)  . .  meritus  est . ."  Y.  8. 2;  —  ya  (NDm.)  ffä^a  ..  *sravayalS  Ma 'ratu/rya  N.  2^;  24; — *kaya  h?nH  mas- yanhs  ai'ja  (sd.)?  *yifi3'*  *aparaya  paiti mastrr^naya  ".  .  (ü)  qui  (sunt)  .  ."  F._jc; *ja3'>;  —  vtspe  mainyava  dama  yai- (NPm.ya  varpnya  ".  .  invisibiles  . .  et  (ii) qui  (sunt)  .  ."  Yt.  70.68;  FrW.  1.2;  — vlspe  kaoma  yatcit  (sd.)  ..yaectt  qzahu dfrttAnAs  .  .  *upa  *d»rfzähu  (sd.)  Y,  70. 17;  —  kä  an-a  as'if.staiti/ (sd.)  ^,!(NSf:) dasa  anyaSsqm  asS.stBitinqm  .  .  an/aiti "quae  sola  ..  precatio  (ea  est)  quae  ,  .?" H.2. 6;  —  AvuHtS  vä  ySUlS  (vä)  yim (ASm.)  vä  ainim  ..layqn  "maximus  (natu) seu    (is)    quem    alium   .  .
21138:frSil  mf  tat  nqma  framrüihi  .  .  y"  asim taurvayeni  vispe  daSva  .  .  y  taurvayeni vispe  yäiavS  yat  mqm  naiHs  taurvayät  YX. j.Sf.;  70.343,  i^sSJ,  75.56;  —  variu- hisca  asayö  (näml.  a/nmimi)  ..  y  nö  ma- ziltäsca  .  .  alayS  3r?navante  Y.  52. 3 ;  — mräili  vals  .  .  y  tl  anhtn  yasta  äp3 FrW.  7.  i;  —  ha  hl  maihitn  nyazata '"haca  hukanpta  fitana  '%aca  atahin nivazana  Yt.  5. 127; — y  nS  änham  (3P.) syit3  mani  .  .  ^a^ravaitls  tanvS  ''hantB (3P.)s' Jiffj!-'?iV  (sd.)  ahäire  . .  jasjniqm  Y. 60.11; — aca  nS jamyat  avaiiihe .  .y  ^wa ^aiwi/ayama  .  .  b3rfymya./aifom  (sd.)  Yt 10.  Tj;  —  .T^ar?ni  .  .  yat  asti  ahurahe mazdii  y  damqn  da^a{ ..peuruca  vokuca
21254:•  j-  yat-£it  Konjn.  i }  konzessiv  'auch  wenn, wenn  schon';  das  Verbum  {'aA-)  ist  weg- gelassen: y  usas/aire  Aimivs(sd.)  *ag»urva- yeiti  Y.57.  29;  29,  Yt /o.  104';  —  mit Praes.:  hs ..  iiva.vasmai^A^  apayeifi  ..y° vazaite  hvastim  YLJ4.20.  a)  im  Nach- satz steht  o)  Hl;  das  Verbum  i^ah-)  ist we^elassen:  y°  vimaSiim  aiAhA  umö tfmcit  mi%rB  kangr>fs3mnS . .  Yt/o.io4f.; 104.  ß)  atH},  mit  Praes.:  y  Avast?m (sd.)  *aiihyäti  y  tanüm  apayäti  atßt  dim nOii  räsayaiU {sd.)  Yt. /o.  zi.  2)  tem- poral; 'als',  mit  Praes.,  im  Nachsatz  steht atai  'da':  y°  mam  tura  (sd.)  pazdayanta aiiii  atitn  tanüm  aguze  .  .  a0i  . .  Yl  sj. 56'';  56.  3)  kondizional  'wenn,  so- fern'; mit  Praes.:  y  *pascaaa  aH'qm raiufrittm  ava.raooayäti  tanüm  *pirydli N.  4"^,  3)  wiederholt  'sei  es  dass  .  . oder  dass';  mit  Praes.:  y  ahi  raihvd .  .  upa  karlvars  yat  ar>sahi  zbayamaki . . y^  ..  Yt.  12,9-37;  —  das  zweite  Mal mit  Tmesis:  y  n^mavAa  väcim  baraiti yat  gai>s{sd.)cii  Yt.  10.  S$.  b)  das  Ver- bum (,'aA-)  ist  weggelassen:  vTspe  haoma upastaomi  y°  barisnuna  gairinam  y'  jaf- nu&a  raonqm  yaicit  azahu  ,  ,  V,  /o.  17.
23215:•  j.  vazah-  n.  1)  'Vorwärtsbringen, Fördern'.         i)  'Gleiten,  Fliessen*.
23300:Mit  Akk.  'sich  kleiden  in  — ,  anziehen, sich  umtun;  anhaben';  Akt.  und  Med.: uai  vaslrä  vanAalu  V,_y.  19'';  ^^<Kcri7««( vastra  va»Aaia  (^S.)  andvl  YL5. 129"; —  spafta  vasträ  zanhaiti  tpaita  (sd.)  Yt 10.  126";  —  yS  vanhaiti  .  .  al^Js/a \frazus5  sanhasSa  .  .  N.92'*;p5;  —  *yffi .vanhinti  hntts^a  paiti-varahasca  ü.gi; I  —  kamn>m  (sd.)  vaste  vanhafum  V.  4. 49; *Y.8^^;  —  anyqmla  sutsm  vatfhsnahe N.52(?);  —  vanhSnS  F.S;  —  asman?m .  ,  yint  maedä  vasle  vaahansm  stfhr- paesanhim  "den  Himmel . .,  den  M.  anhat als  sein  aternengeschmiicktes  Gewand"  Yt. 13.  Z\  —  mainyul  ipjnisis  y7  xraosdtstsng asstis  vaitf  "der  heiligste  Geist,  der  die festesten  Himmel  als  Gewand  trägt"  Y. 30.  5.  Wertlos:  vanhäna  x^aita  raoci :fanvaitT^ia  vsrtsU  Yt  j.  i.
```


## [2026-09-04T22:42:13.003Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7830,7860p' BRT.txt",
 "description": "Bartholomae context around line 7853"
}
```


### [2026-09-04T22:42:13.060Z] TOOL RESULT

```
kommen zu  — '  (Akk.):  vlspü  anhus  ..  air- yatum  vaijS{sA^fräsnvät^.t.\.  a)  'in Berührung  kommen  mit  — ':  yezi  apin- I  näyüks  fräshaväi  "wenn  ein  (saugendes) Kind  (mit  der  menstniirenden  Frau)  in Berührung  kommt"  V. /6'.7*>.  3)  'teil- haftig werden,  sich  teilhaftig  machen',  mit |Gen.;  nSit  dva  nSit  irayS  .  ,  asake  ndil asaya  früsinti  (Konj.)  yß  rßit  .  .  "nicht '  werden  sich  zwei  .  .  des  Asa  noch  der 'Belohnung  teilhaftig  machen  .  ."  P. '  44''^.  4)  'zu  teil  werden':  hyat  nä  fryäi I . .  isvS  (sd.)  daidii  maibyS  . .  tava  rafons ^  fräximmm  (sd.)  hyat  'kwä  xsa'^ra  asät ^kala  frqstä  (3SPrM.)*>  Y.^O-M'
I  ai.  aiyal,  aHoiStnahai'il,  ainiti,  alial.  —  VgL '  »flflj-.  —  Fa.;  rasitOH,  hilan,  matan,  (zu  Yt. I  .  11,  P.):  pursUan;  s.  noch  No.  4-8.  —  ')  Die I  Fonn  i^aintä  ist  verderbt  Man  erwarttte *iisa!/ä  —  s.  aber  sfiahAä  —  oder  *qsiiimifä
ob,Google
36 I  ^sa-
(Praei.  7  +  10).     Unrichtig   KZ,   S3-    4^5- '}  Ausg.  aiaiia,  s.  Var.  —    3}  iSL  Gi>n.  KZ. JO.  514.  —  *)  Aus  ava  +  'ojyii/,  %  s6S.  3.  Pü, : nt . .  api  HosfmtSr,  erL :  aiär  tarlan  iie  titvän.
—  S)  Aus /w+*afcä/;  vgl.  Sjo^  II.  a8.  Pü. : ne  . .  /räi  rdntmlär,  eil. :  pälifris  bavttudak ape  iattan  ne  taväti.  —  *)  Pü.i  ka  afurriäyai fräc  raset,  erl.;  hac  kaitän  ajil  Sylt,  —  7)  zSL
Bthl.  IT-  7.  as8.  —  B)  Falsch  KZ.  jj.  465 ;
s.  noch  No.  g.  IMi.:  ie  S  15  iahrvtr  hac ahräilh  apiklk  framüt.  —  9)  Nicht  sicher; Bthl.  Stud.  i.  96.  frqitä  könnte  statt  Praes.  S auch  /-Aor.  sein.
•  g.  asa-  m.  'Partei',  nur  Du.  von  den beiden  Religio  nsparteien,  der  a^uHschen und  der  daiiA^hea'^ :  ai  vä  vTs^Sng  äyöt jiaiä  ratäm  (sd.)  ahurB  valdä  mazda  aya
°sayä  "so  wende  ich  mich  an  euch  alle als  der  Ratav  der  beiden  Parteien  hier, als  den  (mich)  ÄhM.  kennt"  Y.jJ.a.
>i.  ämia-  m.  —  Pü. :  hac  ö/än  an  raiiin.  — .)  VgL  'rJm...
•  j.  i^sav-  m.  'Schoss,  Zweig*  der  Haoma- pfianze:  ^ävaiitJ  alte  'sai'S  arihin  "wie gross  sollen  die  Zweige  sein?"  N.  to8;  — havamm  (sd.)  . .  yd  'sus  (AP.)  hangmr- vayäti  Y.jo.i.
KompE.  —  ai.  amiäv-  m.;  ■>.  dazu  Roth ZDMG.  jj.  684.  —  l'a-:  l^t.
ß,  '"ifsahitä  Y,  4S.  l:  s.  HS-  mit  No.  i.
•  ]-•  S-  S[sta-  m.  'Hass,  Feindschaft; Feindseligkeit':  %wahya  mazda  °tä  (IS.) urvataAyäisd.)  Y.34.&; — yü  gä^ä  asrü- vayd  *'ta  (IS.)"'  vH  tarff.waiti  v3  tanUm *piryetti  "wer  die  G.  nicht  aufsagt  aus Hass  oder  Trotz,  verwirkt  den  Leib"  N. 41;  —  kS  *tff'^  **J  *iarS.»iaitis' (sd.)  N. 41;  —  cim  aosaaAi  aoSaaukaiti  'Um Uaiti  tanva  Aog.  4S(?);  —  a  f/  dvafsSng (sd)  ..  anale  -tqsca  Y.  44-i4)  —  y^ maiiyä  yaoi  akmsi  .  .  vaAista  . .  SStiim  . . 'tftig  ahtnai  y7  nä  astät  (als  Inf)  daidüä ".  .  Feindschaft  (aber)  dem,  der  uns  zu befeinden  vorhat"  Y.  ^.  18;  —  °ta  ava- spayama  vä  Vyt.  44.  a)  DS.  '/ai  als Id£  sbes.
Ans  ar.  *a«j-lha- ;  ygl,  (Et.  unter  aora- ').  — Pü.;  aiuufih,  (EU  N,  41)  erl,!  ka  gäwit  ku  den ntsi;  [iD  V.  44):  anasi  iat;  Sü.:  nSsäiatvam, anäitiiatvam  'Ungläubigkeit'.  —  >>  Hds.  ifslä.
—  »)  Ganz  Verkehrtes   bei  Dst.  ZA.  r.  309.
•  g.  ^^  Inf."  'zu  befeinden':  asting (sd.)  ahmäi  yf  nä  qr  daidltä  Y.40.18.
Zu  einer  Basis  ar.  '*ans-,  %.  airra-.  —  Vgl.  1 ^Af.  —  Ptt.!  anasak.  —  0  Zu  S  25*.  a  e  e.  I
t^Ö.bug-  363
!•  j.  a^'  V.  'schnüren'.  Praes,  3  aza- (/lyäza-yK         Inf.  qzatthe.
'schnüren'  sva.  'einengen,  bedrängen': s.  Inf.
mit  Kf 'einschnüren,  einzwängen':  ha  hi maiofm  nyäsala  "sie  schnürt  sich  ihre TaiUe"  Ytj.137'*.  a)  'hineinzwängen in  — '  (Akk.):  täst>m  däuru  .  .  stamanim he  aoat  nyszaym  ".  .  ein  zugeschnittenes Stück  Holz..;  in  sein  Maul  sollen  sie  es dann  hineinzwängen"  V, /J.30.
Vgl.  gt.  äna,  lat  angö;  s.  auch  qzah-  und No.  I.  —  Pü.:  awialan.  —  «)  Ob  statt  nyas" geschr.?  VgL  S  ^68.  3  a;  s.  aber  np.  niyäz 'Maogel'  bei  Hbm.  AGr.  /.  105,  Weiteres, auch   la    aL    anSha,   IF.  8.  235.    —  »)   VgL
•  J.  lucaBhe  InC  'zu  bedrängen,  in  Not zu  bringen':  ava^he  narqm  asaonqm  qz° duwarltavarxsam  Yt.  13. 39.
Zum  V.  qs-.  —  Vgl.  qsah:
•  j.  ^ah-  n.  i)  'Ein-,  ZusammenschnU- rung*  der  Kehle,  'Erdrosselung'  (nur Komp.).  3)  'Bedrängung,  Enge,  Not; Gefangenschaft':  mi^nm  .  .  yS  nargm  .  . ipa  'zatshat  .  .  fäyajanhat  baraiti  apa nö  haca  'zaahat  apa  haca  'satihibyö (DP.)'>  harSiS^l.  10,22V,— th  nS 'tahucit hals  %rayente  YL 13. 1 46 ;  Vy  t.  $0;  —  yd  AÜ
frayazaite  . .  kahmaiHt  °zat)Aqm  biwivä Yt.  ry.  41;  —  ravasla  o^idrimla  (sd.)  . . aiaonö  stsil  'eas/a  dtäa'intiUa  . .  drvats stSisY.S.8; — yas/a  ml  ail^m  nanm  "zö <vi  avag>r?pt>m  ravöhu  paiti  uzbäraya£ 'imd  wer  den  .  .,  der  in  Gefangen- schaft verbracht  ist,  wieder  in  Freiheit versetzt"  V.  r<?.  10;  —  haoma  .,  yalcit ■zahu  dirilärihs  Jaininam  *upa  *d?rfzaAu (sd.)  Y.  io.17.  a)  liS.  'zaKAe  als  Inf.
sbes.
KompA.,  E.  —  Zum  V.  qz-.  —  ai.  dniAas-  a.
—  PQ.:    langlA,  Sü.    (lU  Y.  8):    näslihyam.  —
```


## [2026-09-04T22:42:40.194Z] TOOL CALL #16: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/tools/; echo ---; ls /home/sfmqrb/git/rishe/data/ | head -20",
 "description": "List tools"
}
```


### [2026-09-04T22:42:40.243Z] TOOL RESULT

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
---
ANOMALIES.md
extracted
EXTRACTION_SPEC.md
research
translations
verification
```


## [2026-09-04T22:42:42.102Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN niyaz\"; grep -n -i \"niyāz\\|niyaz\\|niyäz\\|niaz\" HRN.txt | head -20; echo \"=== HUB\"; grep -n -i \"niyāz\\|niyaz\\|niyäz\" HUB.txt | head -20; echo \"=== PHD\"; grep -n -i \"niyāz\\|niyaz\\|nyʾc\\|nyaz\" PHD.txt PHD_mackenzie.txt | head -20",
 "description": "Grep Horn, Hübschmann, MacKenzie for niyaz"
}
```


### [2026-09-04T22:42:42.204Z] TOOL RESULT

```
=== HRN niyaz
2170:g. niaz. varak; gel. velg, valk; Käö. valg^ velg\ (vergl.
2525:be (ZPGl.), vergl. arm. LW. ape]niaz,
=== HUB
6330:apeniaz 'bediirfnisslos' = np. be-niyaz; apsparem *ich iiber-
=== PHD
PHD.txt:129:niyāz, —omandih ... add necessity. read niyoxšīdan... по [TSA < A tě |... (not tē”).
PHD.txt:166:~ih: wonder. àb-dàn [^5d?n!] water-holder. abdast ['5dst!] hand-guard. abdom Pfdwm | М ?bdwm] last, final(ly). ~ih: finality, end. abd-sahist [pdshst'] wonderful. abē- [5»(y)- | M ?by-, N bé] without, Jess. ~-bar [-5/] fruitless. ---bé$ [-bys] unharmed. ~-bim [-bym] fearless. ~-bimih: fearlessness. e--boy [-bwd] senseless. ---bēyih : senselessness. —-büd(ih) [-bwt', -bwtyh] deficiency. «=čim [-cym] without reason, cause. abēdān рругп!] of use, wanted. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. ~=-68 [ws] M *by?wš, N béhóf] senseless, unconscious. -~-6Sih : senselessness, unconsciousness. abér [yl] very, much. abē-rāh Payis] e erring. abesar [fysl | M ?bysr, N afsar] crown. abesīhēnīdan, abesihén- [Ashyn-ytn', v. abesihidan] destroy. išn(īh): destruction. abesihidan, abesih- Pžs(y)%-ytn! | M? bysyh-] perish, be destroyed. —išn(ih): destruction, ruin. abespardan Pžļsp?/tn!) = abespurdan. abespurdan, abespār- [’fspwltn', ?psp'l- | M ?byspwrd, ?byspr-, N sipurdan, sipàr-] commit, entrust, consign. ubestag [5(y)s? k!] Avesta, the Mazdean scriptures, abestām [ēst m] = abestān. abestàn [°25/°п!] refuge, support, trust. ābestan Dóystn! | P ?bystn, N abtstan] = ābustan, abé-süd [yý swt'] profitless. “Аһ: profitlessness. a-bëš Буў] harmless; unharmed, invulnerable. ~ih: harmlessness; invulnerability. abē-|-wināh [-cwz?^s | M?bywr? 1] innocent. ~-wizend [-wznd] harmless, invulnerable, safe. abézag Pfyck! | M ?bycg, (N *oëza)] pure, holy. ~th: purity, holiness, abēzār Pye’, ?Буе?1 | N bézdr] free.
PHD.txt:514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
PHD.txt:2823:misery niyaz.
PHD.txt:2900:need astānag, niyāz.
PHD.txt:3193:poverty driyūšīh, niyāzēmandīh, škēhīh.
PHD.txt:4259:want (n.) niyaz.
PHD.txt:5291:wahārīg \ NT 1 wehm -eQU'I wahmān (am A 1 wēhmih MGV \ niyāz CAV wiyābānīh AS Ү” OU \ wiyābānēn- - rr QU wiyābānēnīdan (1183 P r^ ay wiyābānīg 143 ar 12wiyābān: V QUy
PHD.txt:5293:niyàzómand эго ү» VU niyāzūmandīh — ^45? 06 үу о y \ niyābagīh ^ $91 niyābag BOV wüxtan OV \ nihādag 14 vex» \ nay, này, *?way, way Del | уду. wb wāyendag 14» ГСУ \ wayendag 155 TO V git-!, kun-! DAT eh A kirih-t — UY I
PHD_mackenzie.txt:767: ,...,-niyaz [-nyd'c] free from want.
PHD_mackenzie.txt:3812:niyaz [nyd)c I M ny)z, N -] need, want, misery.
PHD_mackenzie.txt:7102:misery niyaz.                                  moving ewarzig.
PHD_mackenzie.txt:7141:mount barag, stor.                             need astiinag, niyaz.
PHD_mackenzie.txt:7144:needy astanag<>mand, driyos, niyaz.    obedience ekanagih.
PHD_mackenzie.txt:7304:poverty driyosih, niyazomandih,                privilege abarmand.
PHD_mackenzie.txt:7908:   -- frazam-perozih.                    want (n.) niyaz.
PHD_mackenzie.txt:10381:niyaz                          ~\                                              -.l!.Y~
PHD_mackenzie.txt:10395:niyazomandih      ~t6~~\                           1-2jadag                       \-'~
PHD_mackenzie.txt:11506:abcniyaz                                   abu, abc-
```


## [2026-09-04T22:43:01.453Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 2160-2180\"; sed -n '2160,2180p' HRN.txt; echo; echo \"=== HRN grep niaz/niyaz variants\"; grep -n \"niäz\\|niâz\\|nijaz\\|nijâz\\|niyâz\" HRN.txt | head; echo \"=== CHEUNG\"; grep -n \"Hanź\\|Hanz\\|niyāz\\|niyaz\\|\\*az \" CHEUNG.txt | head -20",
 "description": "Horn context and Cheung grep"
}
```


### [2026-09-04T22:43:01.531Z] TOOL RESULT

```
=== HRN 2160-2180
rösten'; af;\ writ geröstet', wrat-Sddl 'rösten'; bei.
brijag , brejag 'backen , rösten (39) ; wsi/, waresam,
sar. wirzam.
202. &^r/ 'Schnee.
g. mäz. gel. Ka§. varf^ verf.
aw. vafra- 'Schnee'; phlv. vafr.
kurd. vafr (H.-Sch.), befir, bafer, berf (LW.); af>.
vävra 'Schneeflocke*, Plur. 'Schnee'; bei. LW. harpi
sangl. varf, min], värfa,
203. hery 'Blatt'.
g. niaz. varak; gel. velg, valk; Käö. valg^ velg\ (vergl.
buchär. :^3, Ps. 1, 3).
aw. varekah^ (ZP61.); phlv. varg 'Blatt',
kurd. LW. (?) valg (H.-Sch.), belk, balg (Guranl, Rieu
Catalogue II, 729 a).
204. bevf/er 'Glück'.
SiW.*uparö.kara- {wergl.uparö.kairga-), deLagarde,
Beitr. z. altbaktr. Lex. 71, von Geldner, 3 Yasht 12,
gebilligt.
205. bergustuwän 'Panzer, Pferdepanzer'.
Etwa *uparö,kustapäna'; phlv. vergl. kustak \Seite'.

=== HRN grep niaz/niyaz variants
3983:niäz. javän.
=== CHEUNG
11809:*MIDDLE PERSIAN: (+ *ni-) BMP nyd’c /niyaz/, MMP ny’z ‘want, need, misery’ 
11823:*NWIR: ? NP javazah, Gz. yane ‘mortar’ || (+ *ni-) NP niyaz ‘need’ || (+ *ui-) Khuns. 
35427:nyd'c /niyaz/, 171 
41214:niyaz, 172
```


## [2026-09-04T22:43:10.996Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11780,11845p' CHEUNG.txt",
 "description": "Cheung entry context"
}
```


### [2026-09-04T22:43:11.036Z] TOOL RESULT

```
*NWIR: ? Gz. b-a5 ‘look !’ 

*NEIR: (+ *abi-, *ui- ?) Yghn. yaxs-/yáxsta ‘to be seen, visible’ 

*SANSKRIT: äksi- ‘eye’ (RV+) = EWAia I: 42 

9 The Ir. word *Has- ‘eye’, from which the apparently ancient denomin. *Haxs 
derives, has lost *x by analogy with *us- ‘ear’. 

«PIE *H3ek¥-s- ‘eye’ = LIV: 297 | Pok.: 775 ff. 

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
less suitable for Gz. yane though. || The forms with pref. *ui- may be contaminated 
with *yaid?. 

*NEIR: (+ *apa-) Pash. (aor.) boz-/ (inf.) bötlol ‘to lead away’, Sh. boz-/boxt, Rosh. 
aböz-/abüxt, Bart. aböz-/aböxt ‘to send’ || (+ *upa- ?) Yi. aväz-/aväzd, M. avaz-/ 
avézd ‘to bring (someone), fetch’ || (+ *para-) Pash. pryez-, prez- ‘to take out’ || (+ 
*pari-) Yghn. piráyZ-, paréZ- ‘to run away’ 

*SANSKRIT: aj ‘to drive’ = EWAia I: 50 

Q According to Schmeja 1976: 101ff., the substantive Av. āzi- (m.) ‘greed’, MP /az/ 
(MMP ’’z, BMP ’c, Pth. ’’z, etc. can be equated with Skt. aji- ‘race, battle’, which 15 
the nominal derivative of aj. This is semantically difficult to explain though, perhaps 
via *‘drive’ ?
```


## [2026-09-04T22:43:27.202Z] TOOL CALL #20: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-04T22:43:27.210Z] TOOL RESULT

```


```


## [2026-09-04T22:43:32.043Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7%D8%B2",
 "prompt": "Give the full Persian etymology section for نیاز (niyāz): what Proto-Iranian / Middle Persian forms, which PIE root, and which sources are cited (Cheung, Hasandust, MacKenzie)?"
}
```


## [2026-09-04T22:43:34.191Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82en%C7%B5%CA%B0-",
 "prompt": "Give the reconstruction, meaning, and descendants of this PIE root (h2enghw / h2enǵʰ-), including Latin, Germanic and Indo-Iranian reflexes."
}
```


### [2026-09-04T22:43:42.566Z] TOOL RESULT

```
# Persian Etymology for نیاز (niyāz)

Based on the Wiktionary content provided, the Persian etymology section offers limited detail. It states:

"Cognate with Sogdian [script needed] ('ny'z(h), 'need')."

The article does **not** provide:
- Proto-Iranian reconstructions
- Middle Persian forms
- Proto-Indo-European roots
- Citations to Cheung, Hasandust, MacKenzie, or other scholarly sources

The etymology section only establishes a connection to Sogdian through cognacy, without tracing the word back through intermediate historical stages or reconstructed ancestral languages.
```


### [2026-09-04T22:43:45.758Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂enǵʰ-

## Reconstruction
**\*h₂enǵʰ-** (with alternative form \*h₂emǵʰ-)

## Meanings
The root conveys three related semantic domains:
1. "to constrict, tighten, compress"
2. "narrow, tight"
3. "distressed, anxious"

## Major Descendants

**Latin:**
- *angō* ("I cause pain")
- *angustus* ("narrow, close")
- *ānxius* ("anxious")

**Ancient Greek:**
- *ánkhō* ("I compress, strangle")
- *ankhoû*, *ánkhi* ("near, close")

**Germanic:**
- Proto-Germanic *angustiz* ("narrowness, tightness, anxiety")

**Other branches:**
- Albanian: *angësht*
- Old Armenian: *anjaw*
- Proto-Slavic: *vę̄zàti*

The etymology note indicates that "Hittite ḫamank- 'to tie' suggests" the earlier reconstruction should possibly be *h₂emǵʰ- rather than *h₂enǵʰ-, which affects proposed connections to Proto-Uralic forms.
```


## [2026-09-04T22:43:52.014Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%DA%98%D8%AF%D9%87%D8%A7",
 "prompt": "Give the full etymology for Persian اژدها (aždahā): Middle Persian form, Avestan aži dahāka, Proto-Iranian, PIE root, and any cited sources. Also note any related forms اژدر aždar."
}
```


## [2026-09-04T22:43:54.056Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81%C3%B3g%CA%B7%CA%B0is",
 "prompt": "Give the reconstruction, meaning, descendants (Latin anguis, Avestan aži, Sanskrit ahi, Greek ophis) and any notes on the variant *angʷʰis."
}
```


### [2026-09-04T22:43:59.493Z] TOOL RESULT

```
# Etymology of Persian اژدها (aždahā)

**Middle Persian Origin:**
The word is "inherited from Middle Persian" with two attested forms: Book Pahlavi (ʾcydhʾk' /az(i)dahāg/) and Manichaean Middle Persian (ʾzdhʾg /azdahāg/).

**Avestan Root:**
These derive from Avestan aži.dahāka, meaning "Azhi Dahaka"—"a mythical serpent in Zoroastrianism." The component aži means "snake; dragon."

**Proto-Language Chain:**
- **Proto-Iranian:** *Háǰiš
- **Proto-Indo-Iranian:** *Háǰʰiš  
- **Proto-Indo-European:** *h₁ógʷʰis, *h₃égʷʰis, meaning "snake"

**Related Forms:**
The alternative اژدر (aždar) appears throughout Persian and related languages, representing a shortened variant found in multiple descendant languages including Turkish (ejder) and other regional dialects.

The etymology demonstrates a continuous linguistic lineage spanning millennia, preserving the mythological concept of the dragon across Indo-European language families.
```


### [2026-09-04T22:44:01.653Z] TOOL RESULT

```
# Proto-Indo-European *h₁ógʷʰis

**Reconstruction:** *h₁ógʷʰis (feminine noun)

**Meaning:** Snake; also a mythic serpent or dragon slain by a hero in Indo-European mythology

**Key Descendants:**
- Latin: *anguis* (via Proto-Italic)
- Sanskrit: *ahi* (via Proto-Indo-Iranian *Háǰʰiš*)
- Avestan: *aži* (via Proto-Indo-Iranian)
- Greek: *óphis* (via Proto-Hellenic *ókʷʰis*)
- Armenian: *iž* (via Proto-Armenian)
- Welsh: *euod*, *euon* (via Proto-Celtic)
- Tocharian B: *auk*

**Variant Note:** The page lists alternative reconstructions including *egʷʰi-s* and *ogʷʰi-s*, but does not specifically discuss a variant "*angʷʰis*" as distinct from the main form. The synonym "*h₂éngʷʰis" ("snake") is noted as having "replaced this word in most Western and Central Indo-European dialects."

**Reconstruction Debate:** Beekes proposes *h₃égʷʰis* based on "the absence of reflexes of Brugmann's Law pointing to IE *e*-vocalism."
```


## [2026-09-04T22:44:13.062Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== leaf 55\"; awk 'BEGIN{RS=\"\\f\"} NR==56' KLN_1966.txt | head -80",
 "description": "Klein leaf 55 (p.86)"
}
```


### [2026-09-04T22:44:14.847Z] TOOL RESULT

```
=== leaf 55
dian,  adj.,  pertaining  to  the  forenoon. —  L.  antemeridianus,  ’in  the  forenoon’,  fr.  ante meridiem.  See  next  entry  and  -an. ante  meridiem,  before  noon.  —  L.,  fr.  ante,  ‘be¬ fore’,  and  acc.  of  meridies,  ‘midday,  noon’.  See ante-  and  meridian  and  cp.  post  meridiem, antemundane,  adj.,  existing  or  happening  before the  creation  of  the  world.  —  Formed  fr.  ante- and  mundane.  Cp.  premundane. antenatal,  adj.,  previous  to  birth.  —  Formed  fr. ante-  and  L.  natus,  ‘born’,  pp.  of  ndsci,  ‘to  be born’.  See  natal.
antenati,  n.  pi.,  persons  born  before  a  certain event  (law).  —  Formed  fr.  ante-  and  L.  ndti,  pi. of  natus,  ‘born’.  See  prec.  word, antenna,  n.  —  ModL.,  feeler  or  horn  of  an  in¬ sect',  fr.  L.  antemna,  antenna,  ‘sail  yard’ .which  is of  uncertain  origin.  It  is  perh.  a  contraction  of *an(a)tempna,  ‘that  which  is  stretched,  extend¬ ed',  fr.  l.-E.  base  *temp-,  ‘to  stretch,  extend’.  See temple,  ‘place  of  worship’,  and  cp.  next  word. Derivative:  antenn-al,  adj.
Antennaria,  n.,  a  genus  of  herbs,  plants  of  the thistle  family  (bot.)  —  ModL.,  fr.  antenna;  so called  because  the  pappus  resembles  the  anten¬ nae  of  insects.
antenuptial,  adj.,  prior  to  marriage.  —  Formed
fr.  ante-  and  nuptial.  Cp.  postnuptial, antepenult,  n.  —  Abbreviation  of  next  word, antepenultima,  n.,  the  last  syllable  but  two.  — L.  antepaenultima  (scil.  syllaba).  See  ante-  and penultima.  Derivative:  antepenultim-ate,  adj. anteprandial,  adj.,  before  dinner.  —  Formed  fr. ante-  and  prandial.  Cp.  postprandial, anterior,  adj.  —  L.,  ‘former",  compar.  of  ante, ‘before’.  Cp.  F.  anterieur  and  see  ante-  and  -ior. Derivatives:  anterior-ly,  adv.,  anterior-ness ,  n. anteroom,  n.,  A  hybrid  coined  fr.  L.  ante,  ‘be¬ fore’  (see  ante-),  and  room.  The  word  lit.  means ‘a  room  in  front’.
antetype,  n.,  a  prototype.  —  A  hybrid  coined  fr. L.  ante,  ‘before’  (see  ante-),  and  Gk.  tu7to;,  ‘a
82
blow,  a  stamp’;  see  type.  The  correct  form  is prototype,  in  which  both  elements  are  of  Greek origin.
anth-,  form  of  anti-  before  an  aspirate, anthelion,  n.,  a  kind  of  halo.  —  ModL.,  fr.  Gk. dvflrjXiov,  neut.  of  dvfWjXioc,  ‘opposite  the  sun’, fr.  dhm-  (see  anti-),  and  r}.ioc„  ‘sun’.  See  helio-. anthelmintic,  adj.,  destroying  or  expelling  intest¬ inal  worms.  —  Formed  fr.  Gk.  avxl,  ‘against’ (see  anti-),  and  eXixiv;;,  also  £Xptc;,  gen.  eXpuvxoi;, ‘worm’.  See  helminthic.
anthem,  n.  —  ME.  antefne,  antem,  fr.  OE.  antefn (orig.  identical  in  meaning  with  antiphony),  fr. ML.  antiphona,  fr.  Gk.  avxi^oiva,  neut.  pi.  of avxiqxovo;,  ‘sounding  in  answer  to’,  which  was mistaken  for  fern.  sing.  Sec  antiphon.
Derivative:  anthem,  tr.  v.
Anthemis,  n.,  a  genus  of  plants  of  the  thistle family;  the  camomile  (bot.)  ■ —  ModL.,  fr.  Gk. av9ep.ii;,  ‘a  flower  resembling  the  camomile’, fr.  £v9o<;,  ‘flower’.  See  next  word, anther,  n.,  that  part  of  the  stamen  which  contains the  pollen.  —  F.  anthire,  fr.  ModL.  anthera,  ‘a medicine  extracted  from  flower’,  fr.  Gk.  av- 9i)pa,  fem.  of  av9i]p6<;,  ‘flowery’,  fr.  dv9oc, ‘flower’,  which  is  cogn.  with  OI.  dndhas,  ‘herb’. Cp.  antho-,  Anthus,  -anthus,  antheridium,  Anthyl- lis,  the  first  element  in  antelope,  Anthemis, Anthesterion,  anthology,  Anthrenus,  Anthurium, and  the  second  element  in  Chrysanthemum, clinanthium,  colcothar,  enanthema,  exanthema, hydranth,  isanthous,  perianth,  polyanthus. Anthericum,  n.,  a  genus  of  plants  of  the  lily  family (bot.)  —  ModL.,  fr.  Gk.  avOepixo;,  ‘the  as¬ phodel’,  which  is  rel.  to  av9epi^,  ‘blade’,  aflvjp, ‘chaff,  barb  of  a  weapon’ ;  of  unknown  etymo¬ logy.  Cp.  Anthriscus,  atherine,  atheroma,  and the  first  element  in  Atherosperma. antheridium,  n.,  the  male  organ  in  ferns,  mosses, etc.  —  ModL.,  formed  with  the  Greek  dimin. suff.  -t&iov  fr.  dv9v]p6;,  ’flowery’,  fr.  SvOop, ‘flower’.  See  anther  and  -idium.
Anthesterion,  n.,  name  of  the  8th  month  of  the Attic  calendar  (corresponding  to  the  second half  of  February  and  the  first  half  of  March).  — - Gk.  ’Av9ea-rrlpuov,  lit.  ‘the  month  in  which Avflea-rvjpia,  “the  Feast  of  the  Flowers”,  was celebrated’,  fr.  <5tv9o;,  ‘flower’.  See  anther, antho-,  before  a  vowel  anth-,  combining  form meaning  ‘flower’.  —  Gk.  dv9o-,  <xv9-,  fr.  av9o;, ‘flower’.  See  anther.
anthodium,  n.,  the  head  of  a  composite  plant (bot.)  _  ModL.,  fr.  Gk.  av9d>Sr-,  ‘flowerlike’, which  is  formed  fr.  Sv9o;,  ‘flower’,  with  suff. -tbS-rfi,  ‘like’.  See  anther,  -ode,  ‘like’,  and  tst
-ium.
antholite,  n.,  a  fossil  flower.  —  Lit.  ‘flower  stone’. See  antho-  and  -lite.
anthology,  n.  —  Gk.  dv9oXoja5,  ‘a  flower  gath¬ ering’,  fr.  dv9oX6yo';,  ‘gathering  flowers  ,  fr. Sv9o5,  ‘flower’,  and  XFyeiv,  ‘to  gather’.  See
anther  and  -logy.
83
Derivative:  antholog-ic-al,  adj.,  antholog-ic-al- ly,  adv.,  antholog-ist,  n.,  antholog-ize,  tr.  v. anthophyllite,  n.,  a  magnesium  and  iron  silicate (mineral.)  —  Formed  with  subst.  suff.  -ite  fr. ModL.  anthophyllum,  ‘clove’,  fr.  Gk.  dvftoc, ‘flower’,  and  <puXXov,  ‘leaf’  (see  antho-  and phyllo-);  so  called  in  allusion  to  its  clove-brown color.
Anthoxanthum,  n.,  a  genus  of  grasses  of  the family  Poaceae  (bot.)  —  ModL.,  lit.  ‘the  yellow flower’,  fr.  dvfto;,  ‘flower’,  and  £av96i;,  ‘yellow’.
See  antho-  and  xantho-.
Anthozoa,  n.  pi.,  a  group  of  Coelenterata  (zool.) —  ModL.,  fr.  Gk.  Svflop,  ‘flower’,  and  Cepa,  pi. of  s<iiov,  ‘animal’,  hence  Anthozoa  lit.  means ‘flower  animals’.  See  anther  and  -zoa  and  cp. Zoanthus.  Derivatives:  anthozo-an,  adj.  and  n., antho zo-ic,  adj.,  antho zo-id,  n. anthracene,  n.,  a  hydrocarbon  C14H,0  (chem.)  — Formed  with  suff.  -ene  fr.  Gk.  divflpa!;,  ‘coal’. See  next  word.
anthracite,  n.,  a  kind  of  hard  coal.  —  L.  anthra¬ cites,  ‘a kind  of  bloodstone’,  fr.  Gk.  dv8paxfxY]c, ‘a  gem’,  prop,  subst.  use  of  an  adj.  meaning  ‘re¬ sembling  coal’,  fr.  Sv9pa^,  gen.  Sv9paxoi ;,  ‘coal’. See  anthrax  and  subst.  suff.  -ite.
Derivatives:  anthracite,  tr.  v.,  anthracit-ic,  adj., anthracit-ism,  n.
anthraconite,  n.,  a  coal-black  marble  of  limestone (mineral.)  —  Formed  with  subst.  suff.  -ite  fr. Gk.  dvhpxli,  ‘coal’,  and  xovla,  ‘dust,  ashes; lye,  soap  powder;  lime’.  For  the  first  element see  anthrax.  Gk.  xovia  derives  fr.  xovtp,  ‘dust’, which  is  cogn.  with  L.  cinis,  ‘ashes’;  see  cine¬ rary.
anthracosis,  n.,  coal-miner’s  disease  ( med .)  — Medical  L.  lit.  ‘disease  caused  by  coal’,  formed with  suff.  -osis,  fr.  Gk.  avffpai;,  gen.  avftpaxoc, ‘coal’.  See  anthrax.
anthrax,  n.,  a  malignant  disease  of  cattle  and sheep.  —  L.,  fr.  Gk.  dvftpcc!;,  ‘coal;  carbuncle, malignant  pustule’,  which  is  of  uncertain  origin. Cp.  Arm.  ant'el,  ‘a  glowing  coal’.  —  Coal  is first  mentioned  about  370  B.C.E.  by  Theo¬ phrastus  in  his  treatise  ‘On  Stones’,  under  the name  X19op  4v9paxo<;  (i.e.  ‘coal  stone’). Anthrenus,  n.,  a  genus  of  insects  ( entomol .)  — ModL.,  fr.  Gk.  av9pf)vr),  ‘wild  bee,  hornet’, contraction  of  *iv9o-9p7jvr;  (see  haplology),  lit. ‘flower  bee’.  For  the  first  element  see  antho-. The  second  element  is  rel.  to  TEv9pY]wj,  ‘bee, wasp’,  9pd>va5,  ‘drone’.  See  drone.
Anthriscus,  n.,  a  genus  of  plants  of  the  family  Am- miaceae  (bot.)  —  L.  anthriscus,  ‘the  wild  chervil’, fr.  Gk.  iv&picjxoc,  which  is  possibly  rel.  to  a9f;p, ‘chaff’.  See  Anthericum.
Mthrop-,  form  of  anthropo-  before  a  vowel, •■thropic,  adj.,  pertaining  to  man.  —  Gk.  av- ffpomixdp,  fr.  5v9po)iro.;,  ‘man’.  See  anthropo- and  -ic.
•nthropo-,  before  a  vowel  anthrop-,  combining form  meaning  ‘of  man,  pertaining  to  man’.  —
Gk.  avflpcono-,  dvflpont-,  fr.  av9pc»7TO<;,  ‘man’, which  is  perh.  a  dialectical  variant  of  *avSp- w7toi;,  a  compound  of  avfjp,  gen.  avSpo;, ‘man’,  and  gSiJj,  gen.  coro;,  ‘eye,  face’,  and  lit. means  ‘he  who  has  the  face  of  a  man’.  See andro-  and  -ops  and  cp.  the  second  element  in cynanthropy,  Eoanthropus,  lycanthrope,  mis¬ anthrope,  philanthrope,  Pithecanthropus,  theri- anthropic.
anthropocentric,  adj.,  regarding  man  as  the center.  —  Compounded  of  anthropo-  and  centric, anthropogeography,  n.,  the  study  of  the  geo¬ graphical  distribution  of  man.  —  G.  Anthropo- geographie,  coined  by  the  German  geographer Friedrich  Ratzel  (1844-1904)  in  1882  fr.  anthro¬ po-  and  G.  Geographic,  fr.  L.  gedgraphia  (see geography).
anthropography,  n.,  that  part  of  anthropology which  deals  with  the  physical  characteristics  of the  human  race.  —  Lit.  ‘the  description  of  man’. See  anthropo-  and  -graphy. anthropoid,  adj.,  manlike;  n.,  an  anthropoid  ape.
—  Gk.  avAporroEtSf);,  ‘like  a  man,  resembling a  man’,  compounded  of  avOporrop,  ‘man’,  and -osiSiiq,  ‘like’,  fr.  elSo?,  ‘form,  shape’.  See  an¬ thropo-  and  -oid.
Derivatives:  anthropoid-al,  anthropoid-an,  adjs. anthropolatry,  n.,  the  worship  of  a  human  being.
—  Compounded  of  Gk.  av&poiTro:;,  ‘man’,  and -Xaxpeia,  -Xaxptx,  fr.  Xaxpeia,  ‘hired  labor; worship’.  See  anthropo-  and  -latry.
anthropology,  n.,  the  science  of  the  natural  his¬ tory  of  man.  —  The  word  lit.  means  ’the  science of  man’;  it  is  compounded  of  anthropo-  and  Gk. -Xoyi«,  fr-  -Xoyop,  ‘one  who  speaks  (in  a  cer¬ tain  manner);  one  who  deals  (with  a  certain topic)’.  See  anthropo-  and  -logy.
Derivatives:  anthropolog-ic-al,  adj.,  anthropo- log-ic-al-ly,  adv.,  anthropolog-ist ,  n. anthropometry,  n.,  measurement  of  the  human body.  —  Compounded  of  anthropo-  and  Gk. -(isxptx,  ‘measuring  of’,  fr.  pexpov,  ‘measure’. See  -metry.  Derivatives:  anthropometr-ic,  an- thropometr-ic-al,  adjs.,  anthropometr-ist,  n. anthropomorphic,  adj.,  pertaining  to  or  having the  nature  of  anthropomorphism.  —  Formed with  suff.  -ic  fr.  Gk.  ivflptoTropopqio;,  ‘of  a  hu¬ man  form’.  See  anthropomorphous.
Derivative:  anthropomorphic-al-ly,  adv. anthropomorphism,  n.,  conception  of  God  under a  human  form.  —  Formed  with  suff.  -ism  fr.  Gk. dv9po>7rap.op<fio;,  ‘of  a  human  form’.  See  anthro¬ pomorphous.
anthropomorphist,  n.  —  See  prec.  word  and  -ist. anthromorphi ze,  tr.  and  intr.  v.  —  See  next  word and  -ize.
anthropomorphous,  adj.,  having  the  form  of  a man.  —  Gk.  av9po)7r6fi.opcpoc,  ‘of  a  human form’,  compounded  of  4v9p(orto;,  ‘man’,  and p.op<p7],  ‘form,  shape’.  See  anthropo-  and  mor- pho-.  For  E.  -ous,  as  equivalent  to  Gk.  -04,  see suff.  -ous.
anthropopathy
anutjuii/
84
anthropopathy,  n.,  ascription  of  human  feelings  to God.  —  Gk.  av&pcoTro7ta9£ia,  ‘humanity’,  lit. ‘human  feelings’  fr.  avFpco7xoc,  ‘man’,  and -TxaHeta,  fr.  7xaHeTv,  ‘to  suffer’.  See  anthropo- and  -pathy.
Derivatives:  anthropopath-ic,  adj . , anthropopath- ic-al-ly,  adv.
anthropophagi,  n.  pi.,  cannibals.  —  L.,  pi.  of '  anthropophagus,  fr.  Gk.  avffp<o7xo<paYo<
```


## [2026-09-04T22:44:21.569Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Azhi\\|Dahaka\\|Dahak\\|azhdaha\\|Zohak\\|Zahhak\" KLN_1966.txt KLN_1971.txt | head -20; echo \"=== anguine/anguis\"; grep -n \"^anguine\\|^anguis\\|^anguish\\|^anguilla\" KLN_1966.txt | head",
 "description": "Klein grep for Dahaka and anguine"
}
```


### [2026-09-04T22:44:21.637Z] TOOL RESULT

```
=== anguine/anguis
2792:anguine,  adj.,  pertaining  to  a  serpent.  —  L.  an- guinus,  fr.  anguis,  ‘serpent,  snake’,  which  is  cogn. with  Arm.  auj,  oj,  Lith.  angis,  OPruss.  angis, Lett,  itodze,  Russ,  az,  Pol.  wqz,  and  prob.  also with  01.  ahih,  Avestic  azish,  ‘snake’,  Gk.  'iyiQ, ‘viper’.  See  echidna  and  cp.  Anguidae,  Anguilla, Anguis.  Cp.  also  Ahi,  Encelia,  ask,  ‘water  newt’. For  the  ending  see  suff.  -ine  (representing  L. -inus).
2793:anguineous,  adj.,  serpentlike.  —  L.  anguineus,  fr. anguis,  ‘serpent’ ;  see  prec.  word.  For  E.  -ous,  as equivalent  to  L.  -us,  see  suff.  -ous.
2795:anguish,  n.  —  ME.  anguise,  angoise,  fr.  OF.  an- guisse,  angoisse  (F.  angoisse ),  fr.  L.  angustia  (in classical  Latin  used  mostly  in  the  pi.),  ‘narrow¬ ness,  deficiency’,  fr.  angustus,  ‘narrow  ,  fr.  an- gere,  ‘to  throttle,  torment’.  See  anger  and  words there  referred  to  and  cp.  esp.  angostura. anguish,  tr.  and  intr.  v.  —  OF.  anguissier,  an- goissier  (F.  angoisser),  fr.  anguisse,  angoisse.  See prec.  word.
```


## [2026-09-04T22:44:29.346Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=2795{n+=gsub(/\\f/,\"\")} END{print \"form-feeds before line 2795:\", n}' KLN_1966.txt; echo \"=== leaf tail\"; awk 'BEGIN{RS=\"\\f\"} NR==58' KLN_1966.txt | grep -o \"^\\|[0-9][0-9]\" | head -0; awk 'BEGIN{RS=\"\\f\"} NR==58' KLN_1966.txt | tr ' ' '\\n' | grep -x \"8[0-9]\\|9[0-9]\" | head",
 "description": "Find Klein leaf for anguine"
}
```


### [2026-09-04T22:44:31.373Z] TOOL RESULT

```
form-feeds before line 2795: 52
=== leaf tail
86
87
88
89
```


## [2026-09-04T22:44:36.521Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==53' KLN_1966.txt | tr ' ' '\\n' | grep -x \"[0-9][0-9]\" | head; echo \"--- first words of block\"; awk 'BEGIN{RS=\"\\f\"} NR==53' KLN_1966.txt | head -c 300",
 "description": "Page numbers in Klein block 53"
}
```


### [2026-09-04T22:44:38.452Z] TOOL RESULT

```
77
78
79
87
--- first words of block
 Russ,  ugori,  Pol.  wfgorz),  ‘eel’,  which  all mean  derivatively  ‘the  snakelike  fish’.  It.  an¬ guilla,  F.  anguille,  Sp.  anguila,  Port,  enguia  and prob.  also  OSlav.  qgulja,  fegulja,  ‘eel’,  derive  fr.
L.  anguilla.
anguine,  adj.,  pertaining  to  a  serpent.  —
```


## [2026-09-04T22:44:55.137Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^Ahi,\\|^Ahi \\|Avestic azish\\|Avestic azi\" KLN_1966.txt | head; echo \"=== block 58 content sample\"; awk 'BEGIN{RS=\"\\f\"} NR==58' KLN_1966.txt | head -c 400; echo; echo \"=== block 57 pages\"; awk 'BEGIN{RS=\"\\f\"} NR==57' KLN_1966.txt | tr ' ' '\\n' | grep -x \"[0-9][0-9]\" | head",
 "description": "Klein Ahi entry and block pagination"
}
```


### [2026-09-04T22:44:57.348Z] TOOL RESULT

```
2035:Ahi,  a  serpent  in  Vedic  mythology,  identified with  Vritra.  —  Ol.  ahih,  ‘serpent’,  rel.  to  Avestic azish  and  cogn.  with  Gk.  lyiq,  ‘viper’,  L,  anguis, ‘serpent,  snake’.  See  anguine  and  cp.  echidna, ahoy,  interj.  —  A  natural  sound,  compounded  of the  interjections  a,  ‘ah’,  and  Aoy.Seeah  and  hoy. Ahriman,  n.,  the  spirit  of  evil  in  the  Zoroastrian religion.  —  Gk.  ’ApEqrdvto?  (in  Aristotle)  or ’ApsipLavY]?  (in  Agathias),  fr.  Avestic  ahra  mai- nyu,  ‘the  evil  (lit.  hostile)  spirit’, ahull,  adv.  (naut.)  —  Formed  fr.  a-,  ‘on’,  and hull,  ‘body  of  a  ship’.
=== block 58 content sample
in  1880). antiseptic,  adj.  and  n.  —  Formed  fr.  anti-  and septic.
Derivatives:  antiseptic-al-ly,  adv.,  antiseptic- ism,  n.,  antiseptic-ist,  n.,  antiseptic-ize,  tr.  v. antiserum,  n.  —  A  hybrid  coined  fr.  Gk.  dvxi, ‘against’,  and  L.  serum,  ‘whey’.  See  anti-  and serum.  The  correct  form  would  be  antiorus,  fr. Gk.  dvxi,  ‘against’,  and  opo?,  �
=== block 57 pages
85
```


## [2026-09-04T22:45:21.134Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"abandon,\" \"anger,\" \"ankle,\"; do ln=$(grep -n \"^$w\" KLN_1966.txt | head -1 | cut -d: -f1); blk=$(awk -v L=$ln 'NR<=L{n+=gsub(/\\f/,\"\")} END{print n+1}' KLN_1966.txt); echo \"$w line=$ln block=$blk\"; awk -v B=$blk 'BEGIN{RS=\"\\f\"} NR==B' KLN_1966.txt | tr ' ' '\\n' | grep -x \"[0-9]\\{1,3\\}\" | head -6; echo; done",
 "description": "Klein page calibration"
}
```


### [2026-09-04T22:45:23.574Z] TOOL RESULT

```
abandon, line= block=1

anger, line=2761 block=52
76

ankle, line= block=1
```


## [2026-09-04T22:45:33.273Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} END{print \"blocks:\",NR}' KLN_1966.txt; echo \"--- last block page markers\"; awk 'BEGIN{RS=\"\\f\"} NR>=740 && NR<=760' KLN_1966.txt | tr ' ' '\\n' | grep -x \"1[0-9]\\{3\\}\" | head -20",
 "description": "Klein block count"
}
```


### [2026-09-04T22:45:35.121Z] TOOL RESULT

```
blocks: 903
--- last block page markers
1391
1879
1392
1394
1393
1895
1401
1402
1405
1406
1408
1409
1410
1413
1640
1414
1415
1781
1416
1767
```


## [2026-09-04T22:45:59.914Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=54 && NR<=58' KLN_1966.txt | grep -o \"[a-zA-Z]*[Ss]erpent[a-z]*\\|[Ss]nake\\|Avestic [a-z]*\" | sort | uniq -c | head",
 "description": "Check Klein blocks 54-58 for snake content"
}
```


### [2026-09-04T22:46:02.590Z] TOOL RESULT

```
      1 serpentine
```


## [2026-09-04T22:46:15.774Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v4 pdf page 305 (printed 2222)\"; awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 305\\]/' incoming/BQT/BQT_v4_pages.txt | head -60",
 "description": "BQT vol4 page 2222"
}
```


### [2026-09-04T22:46:17.771Z] TOOL RESULT

```
=== BQT v4 pdf page 305 (printed 2222)
[pdf page 305]
بیابه ۲۲۲
هرچیز هم هست - تاج رآکوش ۴ - وبمعنی‌حاجتمند ماج
1( [چ 1 : زومند هم آمده‌است 6 - خواهش1 -
با یرای فان بای | وافارست وس مرها پزکر 7
نوبت باشد ؛ وباین معنی‌بجای حرف‌اول بای‌ایچ 7 ال
هم‌آمده وگفته شد . - و بمعنی قحط وغلا - وشره وحرص - وبلذت
نیارست ؟ - بنتح اول و رای قرشت خوردن طمام هت و بسنی دوست دبای
وسکون سين بی‌قطه وفوقانی, بعنی شواست‌واز دشمن ؛ و درجای دیگر درست دربراین ؛
دستش لدامد + ودرسخةٌ دیگر درشت در برایرهموار نوشته شدم
نیاز ۴ « بکراول بروزن‌حجاز,حاجت بود ؛ وهيچيك شاهد دامتند ۸ .
‎٩‏ < نیابة (لیابت) (عر) «نوبة بالفتح بار وپاس: نو ب کسرد جمع . بقال : جامت نوبتك
و لیابتك . . ليابة ككتابة بار و پای » * منتهی‌الارپ » - «النائب اسم فاعل و من قام مقام غیره
فی‌امراوعمل کنائب‌القاضی ودائب‌الملك » و عمله‌النيابة . ج نوب ونواب» « اقرب‌الموارد ». فارسی
دانستن اين‌لفت ناشی از لغت فری‌اسدی(س۶۸۸) است : «نیایه, نوبت بود. پوشکو رکفت :
آن به که نیایه را نگه داری کردار تن خویش راکنی فربه.»
۲ -ر4 : آرستن » بارستن . ۴ - پپلوی 81182 ( احتیاج » ضرورت,فقدان).
از اوستا -27- 81 ۹ 2 پیشولد است وريشهٌ 22 بمعنی بستن » فشار آوردن و مجبور کردن ]
( بتن , فداردادن ۰ بزور داخل کردن ) « بارتولمه ۰۶۳۹۲ 2283 ( ضرورت #تنگی» احتیاج)
« بارتولمه ۳۹۲ > رك : نیب رکه س ۱۹۳.
۴ - دگر بوبهای خوش آورد باز که دارند مردم ببوش لیاز -
فردوسی طوصی ۸« شاهنامهٌ بخ جاص ۲۵ ۰
۰ - باین معنی « نیازمند »۰ « لیازومند » و«لیازی» (ه.م.) است .
‎٩‏ - درفرهنگه نظامآمده : « نیاز. . بمعنی‌خواهش کردن, دیازش - نیاز فخر گر کالی:
سروشان را نام يك بتود بیازشهای بی‌اندازه بنمود . >
موْلف نهی‌الادب در فصل « بیان زبادت »گفته (س ۲۲۸ ): « شین نقطه‌دار , چون «نیازش» مزبد
علیه « بیاز» [است ]. فغرجرجانی درمثنوی ویس‌ورامین گوید : سروشان را ...» « لیازش» درلفت
فری. » جهانگیری » رشیدی » برهان قاطع وانجمنآرا نيامدء و درموضع دیگر درنظم وش دیده
نشده وبیت فوق هم درة وس ورامین » مصحح‌آفای مینوی (س۶4) بدین صورت است :
سروشان را بنام نيك بتود فیایشهای پی اندازه بنمود.
و*اپایش» (پهلوی82[18108 بمعنی‌ستایش)(۸.م.) صحیح است. «اسم مصدر بقلم‌نگارنده ص4۳*.
۷ - مجازاً نذری که برای گرفتن مراد و حاجت خود بنام لبی وولی داده شود که بیشتر
بشکل خوراك است « فرهنگه نظام ».۸ - رشید ی کوید : « لیکن بممنی دوست » لیازی
است نه نیاز » (ر4: نیازی)مژلف فرهنگه نظام نود : «ولی‌معنیاول که درسخهة (سحاح الفری)
زد من درست با سین «همله است (همچنین در لخهّآقای طاعتی) » در سغهةٌ جهانگیری با شین
منقوطه بوده » ودرسه دغخةٌ جهانگیری که نزد من‌است » چنین‌است» اسل این‌اقوال ناشی‌از کفتار
آسدی طوسی است : «نیاز » دوست بود . لبیبی گوید :
ایا نیاز بمن ساز ومر مرا مگذار که نا زکردن معمشوق دلگداز بود .>
« لت فري ۱۸۹ ۰
```


## [2026-09-04T22:46:43.224Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v1 grep اژدها\"; grep -n \"اژدها\" BQT_v1_pages.txt | head -10",
 "description": "BQT v1 grep azhdaha"
}
```


### [2026-09-04T22:46:43.272Z] TOOL RESULT

```
=== BQT v1 grep اژدها
2553:۰ -واژدهای نوچاپ نر هنگستان
4475:6 اختیار- اژدها: ۱۳۷۸ شسی.
4476:۵- اژدها- اسحان» ۲٩‏ ۱۳شمسی.
5854:(۱) رك : اژدها و اژدرها در متن,
7786:تاععو۷تاید ۳۱۱۵۵۲60۵ 122۳812 ۸ آمده. فردوسی‌دز شحاك رابنام‌اژدها میخواید:
7787:نهان بود ( جمشد ) چند از دم اژدها ( ناه )
7790:مرآن اژدها (ضحال) را خورش ماختی «ابسناً ص ۳۵ >
7791:و نیز او را «ازدهافش؛؟ و «اژدهایکر» میشواند . لمزدستا ٩۳۱‏ .آسیابان باشد چه آسیا راآس میگویند .
11373:٩‏ - تحریف « ازدماك » . ره : اژدها .
11385:ادها « با کاف‌معنی آخراژدهاست
```


## [2026-09-04T22:46:44.627Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 128 129 130 131 134; do echo \"=== pdf page $p\"; awk -v P=\"[pdf page $p]\" 'BEGIN{RS=\"\\f\"} index($0,P)>0' incoming/BQT/BQT_v3_pages.txt | head -12; done",
 "description": "BQT v3 pages around 1339"
}
```


### [2026-09-04T22:46:46.453Z] TOOL RESULT

```
=== pdf page 128
[pdf page 128]
وج ات

از ‎ci‏ بردن وفایده کردن .

صر و » بنتح اول و سکون ثالی و واوه

‎ae‏ شوکران ۱- و آن بیخی باشد که از

‎oy‏ و تفت آورلد ؛ وبسشی کوبند دوری است

‏بیان
=== pdf page 129
[pdf page 129]
‎oly‏ هفتم
در صاد بی نقطه با لام مشتمل بر چپار ‎ca)‏ کنات

‏صلا ۱ © بقتح اول‌بروزن‌ملا برافروختن
آش را گوینه بجهت سرمای سخت - ۰فربادی
باشد که ‎(lb cpm‏ دادن بدرویشان وقفیران ۴
وچیزی فروختن کتند - و یک اول » درعربی
پربان را گویند .

‏صالاب ۴ ‎den‏ بر وزن کلاب 1
اسطرلاب را کوبند و آن ‎AT‏ باشد که ‎Pot‏
=== pdf page 130
[pdf page 130]
—\rry

وبلاظ دیگر حرمل عربی خوالند » و معرب‌آن
‎Sate‏ دانج است وآن ‎gest‏ از-داب(۱) کوهی
باشد .گرم و ختكك است در سیم » وسفید آن
بهتر است. بولوحیض‌براند ‎LUG ey‏ ومفاصل‌را

ol

صومعه داران فلت
‎ct du‏ . #
=== pdf page 131
[pdf page 131]
‎oly‏ دهم

‏در صاد بی نقطه بایای حطی مشتمل بر دو ‎cal‏ و کنایت
صیقل مس ‎ST‏ ینش ‎ALS‏ از | است ‎wget IG)‏
آقاب‌التابات_ رصقل‌مسیر آفرینش | صیمگان ۱ ‎She‏ فرسی بروزن ‎re‏
‎ST pas jive »‏ ینش م بنظر آمده جان . ام ولایتی است ازملك فاری.

‏0( چك : - است.

‎٩‏ -۱کتون 510۳0260 تلفط کنند .,رآن شپربت بفاری بطول. 4۸ وعرض ۳۰ کیلو
متر » از شمال محدود بخفرومیمند واز مشرق ببلوك جهرم و از جنوب یلو ‎sb‏ وکارزین و از
=== pdf page 134
[pdf page 134]
گفتار شانردهم
از کناب ‎ebb aby‏ در حروف طای بی نقطه با حروف
تبجی مبتنی بر دوازده بیان و محتوی بر بکصد و دفتاد
وشش") لت و کنابت و ‎dy‏ انجام که آنبم ‎is gow‏ است
برشش ‎cd‏ و کنابت که اول ‎BT‏ ظای ‎ded‏ دار باشد)

بیان اول

در طای بی نقطه با الف مشتمل مر سی و له لغت و کنایت
* طاخكگ ه با غای ‎abs‏ دار (ع) بر | اکر ‎ele‏ بررکث ‎(YT‏ بخورند بمیرهد.
وزن آحك » ‎yey‏ از درخت است که آلرا طاق طار ‎Gb‏ - بفتح‌رای بی قطه (4 اوسکون
```


## [2026-09-04T22:47:00.059Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 5854 7786 11373; do blk=$(awk -v L=$L 'NR<=L{n+=gsub(/\\f/,\"\")} END{print n+1}' BQT_v1_pages.txt); echo \"=== line $L in leaf $blk\"; done",
 "description": "Find BQT v1 leaves"
}
```


### [2026-09-04T22:47:02.221Z] TOOL RESULT

```
=== line 5854 in leaf 207
=== line 7786 in leaf 250
=== line 11373 in leaf 328
```


## [2026-09-04T22:47:10.955Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 326 327 328; do echo \"===== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -70; done",
 "description": "BQT v1 leaves 326-328"
}
```


### [2026-09-04T22:47:12.696Z] TOOL RESULT

```
===== leaf 326
از ذست ب رکرفتن
یت و بود گردانیدن باشد .
هوز بالف کشده , نان فطیر را گویند یمن بعنی نافی
که خمیر آن نرسیده باشد .
از دست دهرجستن - بستی از
خر افتادن است که مردن و از عالم رفتن باشد .
از دست رقتن - کناید از بخودی
و بی اختیاری و اضطراب کردن باشد .
ازدست شدن « بسسنی از دست‌رفتن
است که کنابه از بخودی و بی اختباری
و اضطراب کردن باشد .
از دست فز | - بتح فای سنس ,
بمعنی ازدست پزاست که نان فطیر باشد .
ادف - بکر اول و فتح ثالك وسکون
فا . میوهء‌ایت سرخ رنگ و صحراسی و آنرا
بعربی زعرور خوانند ؛ و بفتح اول هم گفته‌اند .
ار دمی بر وزن فمدمی . <سالوری
است غیر معلوم» وبا رای قرشت هم کفته اند .
ازدن » بقثم اول و ثانی و الث
وسکون لون؛ بمعنی رنگ» کردن باشد - وبمعنی
0
و واو 4 صمغ درطات ارجن 3 درخت بادام
را رز گفته‌اند ۳
ارذوی تادی - یی سصغ عریی.
چه ازدو صمغ و تازی عربی را گوبند ,
از ده ت فتح اول ودال ابجد و کسرثانی»
یسعتی رنگه کرده باشد .
۱ رد : آزرمیدخت ۰
ی ناس ۶ .
۵ ازه - (فتح اول) - : ازغ .
۷4
از راستی باشد که هیچ کبمی درآن نباشد .
از دق - با رای فرشت بر وزن ابلق ,
- و در
عربی رنگه کنود را گویند .
ازر گ اند بشه چکیدن ه کنابه
از دقت کردن در فکر و اندیشه باشد .
از رمیدخت » با دال و خای قطه "
دار بر وزن سحر میگفت » نام دخشی پرویزاست
که لشکر بدوبیعت کردند وششماه ملك راندا -
و نم شهری تبز هست که اوبنا کرده است .
ارر نگ بر وژن ید رن , خیار
پادرنگه را گوشد .
از ز بان جستن -کنابدازخطا وسهو
کردن در کفتگو باشد .
از سر با روان شدن» کنابه
از زود روان شدن و بتعجیل رفن باشد .
ازسر ذست « کنابه از گفتن مر قزر
وسختی باشد بیتأمل و فکر - وزود ساختن‌کاری
بی‌اتظار .
ارشکم افتادن - کنابه از مردن
واز عالم دفتن باشد.
از « تج اوز و سکون ثانی و غین
قطه دار . آنجه از شاخهای درخت برند
وییرایش دهند ۴ وآترا بعزبی جلمه گویند .
ارچ - بنتح اول و کون ثالی و کر
تالت و جیم فارسی سا کن » کیاهی اس ت که بر
درخت یجد و آنرا بعربی عشقه خوانند . #
از کات ه با اف فارسی بروزن بمدذات»
عردم بد دل و بد اندرون را گونند .
از کره درفتن - کنابه ازابود وتلف
شدن زر نهد و غره باشد . ٩‏
3
۵ از یل کنا[1۷66۳1 « کل کلاب(۲۱۷۲ » دتایتی»۱۹ *
از دتةکل سرخهاي اصای 8۸۵8685 ازتبر؛ گل سرخیان 80980669 1
دادای میوهُ خوردنی «گ لگلاب 4۲۲۸
ی
===== leaf 327
ما
ارم » جح اول و سکون.تانی و میم »
بنتی فد باشد ‏
ارمل س بر وژن جدول » بمنی بسیار
وکثیرباشد. وصدا وآوازرا یز گومند - وبمعنی
همه و مجبوغ هم آمده است
از ناو با نون و واو بی وزن غرفاو .
نم ناحیه‌ایست از نواحی حمدان .
از ناوه ت شتح اول وواو» سعنی ازناو
است که ناحیهای باشد از نواحی همدان ‏
از فس « بر وزن مذحب . بمعتی رنجش
باشد که از رنجیدن است - و در عربی فربه را
کونند که ضد لاعی باشد .
ار نقش گلور خار دستن .
کتابه از خواری و بی اعتباری باشد .
از ود - باواو بروزنشبگرد » دوابی
است که آنرا بفارسی انده فوقو گویند و بعربی
آژوها:
روغن بجوشانند و برطفل یکه دب سمرکت آمد
بمالند زود بحرکت آبده و جمیم یادها را نافع
است .
ارودری بر وژن سرصری » بلفت
بربری نام درختی است سطبر و خار دار ؛ پوست
آن سرخ و گنده میباشد» در دوایی بکار برند .
ار هر اه ه بفتح های هوز و رای می
نفطه بالف کشیده ۳ اسلی تساه
ماران است ا .
ار ای وزدضر ۱ مخفف زبرا
هد که از رای سلیل است » نی از برای اين
و از این جپت .
اد یز » بر وزن تمیز . بان و فرباد
و اله راگویند .
ار یش « بر وزن کشیش » بمعنی ازو
وازوی باشد. چنانکه کوبند «ازیش بستان» .نی
حندقوقی خوانند . اکی آب آنرا بگیرند و با | ازو بگیر و (۱) ازوی بتان .
بیان دوازدهم
از خ -. فتح اول و ان وسکون ای
قطه دار . دانهای ی از اعنا بر می آبد
ودرد لمیکند ,و بعربی تولول کوبند ۴
ازدر ه با دالابجد پروزن لشکر » سر
علم و رابت راگویند - و هار بزرکه را نیز
گفته اند ؟ .
ازدرها بر وزن لشکرها» بمعنی
)۱( چك : - ازوبگیرو .
٩‏ - تحریف « ازدماك » . ره : اژدها .
۴ رك : #دها
مار بزر کب است که اژدر باشد و های اژدرها.
های چمم یست بلکه جزو کلمه است ؟ -
ومردم شجاع و دلاور و خشمگین را نز گفته‌اند
سویادشاهان ظالم رااکونند عموعاً وضحاه ماراترا
خصوساً -. و بمعنی رات و سرعلم هم آمده
ات ۲ ۱
۴ - ره : ازح ‏
===== leaf 328
اراد
باشد ٩‏ - و کنابه از مردم شجاع و قهرآلود حم
هت - ورایت و سرعلم را نیز گوبند ۴ -
وپادشاه تال و ححاك ماراترا هم گفته‌اند ۴ .
ادها « با کاف‌معنی آخراژدهاست
که نحاك ماران باشد ۴ .
اژدهای فلك - اثارء بشدنین رأی
و ذنب است - و تلی‌را نیز گویندکه ازجلهة
چهل و حشت صورت فلك باشد ٩‏ .
ارم خح اول و سکون انی و غن
نقطه دار , شاخهابی را گویند که از درخت بریده
باشند و بعربی جلمه خوانند٩‏ .
ار کان با کاف‌بروزن دربان ؛ بمعتی
مردم کاهل و باطل و مهمل و بیکار باشد .
باگد شبکه دار که ازیس آن نگاه توان کرد .
۱
ظ
از گهی -باها پروزنک رکدن : بمعنی
از کهان است که کاهل و باطل و مهمل وبیکار
بش
۸ ۰
آز لد - بفتح اول و انی و سکون نون
و دال ایجد . کلی باشد که بر روی خشت بهن
کنند و خشتی دیگر بربالای آن نهند - و گل
و لای ته حوض را نیز گفته اند .
اژ نگ -بر یزن پلنگ , چين پیشانی
وروی و اندام باشد.
اه « بنتح اول و انی , آهك را گویند
و بعربی کلس و نوره خوانند .
‌ و ۲ ۳
ار هان ‏ با ها بر وزن دربان؛ هردم
کاهل و باطل و مهمل و بیکار باشد .
۱
از هی - بروزن الکن ؛ بمعتی اژهان
است که مردم بکار و مهمل و باطل باشد .
۳
از کهان باها بروزن پهلوان ؛. بمنی از بر ع« بر وزن وزیر » بمعنی هوشمند
از کان است که مردم کاهل و باطل و مهمل | و زبرك و عاقل باشد - و مردم پرهیزکار را نیز
و بیکلر باشد . گویند
بیان سیز دهم
اتاات ی وزن وسام اوه بو وغان فرد
باشد , وآن سبب خواب‌باخمار باکاهلی بپجرسد
و بممتی شیه و تظیر و مانند هم آمده است .
اییادون - بارای قرشت بس وزن
فلاطون ؛ بخ کیاهی است کمغلاف تخم آن‌مانند
غلاف بذرالبنج است - و بعض یگوبند بیخ ستبل
حمعا؛ مار گز تده
کنادء دهان اژدهای علم
۳ - مضغف اژی‌دهاك , مُحالك :
۴ مختف اژی‌دهاك , رك: اژدها,
مفرجام هم زو بامث رها .
دمزدبنا ۳۹ ح ۶ *.
۵ - 1(<۲2800. ۱ - ر۵: ازغ
```


## [2026-09-04T22:47:39.488Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ضحاك\\|ضحاک\\|ضحّاک\" incoming/BQT/BQT_v3_pages.txt | head -20",
 "description": "Grep BQT v3 for Zahhak"
}
```


### [2026-09-04T22:47:39.541Z] TOOL RESULT

```
2456:as ‏وخدم ونزدیکان او را‎ cdl ‏ضحاك دست‎
8154:دبگرش ارنواز در ‎Ube‏ ضحاك بود وبعداز کشته
8155:‎Yas‏ ضحاك هردو بفریدون عنتفل شدند.
11393:‏نام مپم-الار ضحاك ‎A‏ اسدی بوده .
19974:کنندء ضحاك بشمار رفته . رك ‎Leg:‏ حماسه ملی‌ابران . نولدکه ‎Ne‏ و رل : مزدیسناص۳۹,
20004:ضحاك را گرفته دربند کرد .
26747:ودخترزاده‌های ضحاك .
27345:مشهور که فردون را بیدا کرد و برس ضحاك
30703:‎ly‏ وسکون میم؛ کلم کرکی که ضحاک ‎ctl‏ و گوبند کردان از آن
43794:پادشاء زادمایست و او مطبخی ضحاكك بود. گوشد
43796:‏را بجهت ‎cle‏ دوشهای ضحاك مرهم سازد و او
47152:وآن قلعه‌ای ‎Soy‏ ضحاك در شهر بابل ساخته
47443:بر آورده ابوان ضحاك دان.
```


## [2026-09-04T22:47:45.077Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 19974 20004 27345; do awk -v L=$L 'NR<=L && /\\[pdf page/ {p=$0} NR==L{print \"line \"L\" -> \"p}' incoming/BQT/BQT_v3_pages.txt; done",
 "description": "Locate pdf pages for Zahhak lines"
}
```


### [2026-09-04T22:47:47.138Z] TOOL RESULT

```
line 19974 -> [pdf page 275]
line 20004 -> [pdf page 276]
line 27345 -> [pdf page 376]
```


## [2026-09-04T22:47:55.691Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 132 133; do echo \"===== pdf page $p\"; awk -v P=\"[pdf page $p]\" 'BEGIN{RS=\"\\f\"} index($0,P)>0' incoming/BQT/BQT_v3_pages.txt | head -60; done",
 "description": "BQT v3 pdf pages 132-133"
}
```


### [2026-09-04T22:47:57.544Z] TOOL RESULT

```
===== pdf page 132
[pdf page 132]
انجام

در ضاد تقطه دار با حروف تیجی مشتمل بر هشت لغت

* ضال ۱ - تخد لام ‎ding‏ شال,
میوه ایستسرخ ‎Ky‏ شبیه ‎lig‏ وآنرابفارسی
کنارخوانندبضمکاف وبعربی ثمرةالدر ۴ خوانند
و درهندوستان ‎je‏ گوبند - وتشدید لام ‎pn‏
‏بمعنی کمراه باشد بض‌کای فارسی ۴ .

‎IgG © chee‏ و جیم بالفکشیده
بجیم دیگر زده » نوعی از صمغ است,وآن‌سفید
میداشد وبجای‌صابون کارفرمایندوجامه وچیزهای

‏دیگر بدان شویند ۴ - و در عربی بعمتی بدی
کردن باشد ‎٩‏ - و بفتح ارل هردرختیر! کوبند
که دد و دام آلثرا پبوشد ۷ - ودر عربی بمعتی
بانگ وفرباد کردن باشد ۵ .۷

‏ضرب - بنتم اول وسکون رای قرشت
و بای ایجد , سیخول راکوبند که خاریشت تیر
اندازباشد ‎whe ie‏ خود را چون‌تیراندازد ۷
- و درعربی بمعنی زدن باشد .

‏# ض (ضاد) - حرف هیجدهم ازالفبای فارسی وحرف پانزدهم از الفبای عربی ‎ee)‏
‏و در ‎ole‏ جمل ‎YT‏ هشتصدگیرند . درفارسی ‎ol‏ حرف ‎ao‏ رآ ترا ماشد «ز» ‎habs‏ کنند .
تلفظ این حرف درعربی از گذاشتن‌پهلوی زبان بپهلوی دندانهای آسیا و دمیدن لفی‌صورت کیرد

‏ورك : لغت نامه .
۱ - (عر) رك: لفت نامه .

‎fruit de lotus= ۴‏ « لك ۷ ص ۳۸۸ »سس

‎۲ ‏ابتی»۱۹‎ » Zyz.spina _ christi= Zyzyphus nummularia
: ‏(گمراهی ) ودرفارسی بتخفیف لام درشمرآمده‎ le ‏اسم فاعل از‎ - ۴

‏بس ز نقش لفظهای مثنوی

‏صورنش ضالست وحادی عمئوی ۰
مولوی « لقت نامه > -

‏۴ - (عر) «منتهی‌الارب» « ‎cad‏ نامه» ۳ ‎ZOMME‏ (فر) «لك ۷ ص 6۳۹۰.
‎٩‏ - (عر) ‎Cue‏ شور وغوغا کردن - ‎KIL‏ و فریاد کردن - ‎Ely‏ و خصومت کردن

‏«منتبی‌الارب» لت نامه

‏۱ - جاح بکر اول (عر) و در تمریف ‎ala oT‏ کل

‏شجرة نسم بهاالباع مثل‌الخروع والقسیب والالب . صاحب برهان ‎LIS‏ « دم » را ‎an poner‏

‏یشم » خوانده است و متوجه کلمةٌ ( به ) نیز شده است « لغت نامه >

‏۷ - (عر) در ‎isl‏ « ضربان » «لنت ‎porc. 6016 = cau‏ (فر) «ل۲ ص۳۹۲
# ضحا لك - پفتح اول و دوم مشدد ؛ رك : ای دهاك .

===== pdf page 133
[pdf page 133]
t=
‏اول و سکون را و عين‎ che ‏ضرع‎
‏می‌هطه (۱) ۰ بمعتی پستان‌است وآن چیزی‌باشد‎
‏از انان ر حیوانات دیگ رکه شیر ازآن دوشند‎
‏کوینه عربی است ۱ - ویفتح اول وثالی هم در‎
. ۴ ‏وضعیف را گوبند‎ AV ‏عریی‎

‎Js! the Pp?‏ و سکون رای فرشت
ومیم ۴ ۰ نام داریی است که آغرا بیونانی‌اسطو-
خودوی کوبند ۴ ۰ وآن شاه اسفرم رومی است.
‎ole‏ سرع را تافع باشد - و در عربی آفروخته
شدن آش - و سخت کرم‌شدن - وبیار کرسته
کردبدن بائد ۵ .

‏۱ -عربی است (رك: یستان) :
آنکه مادر آفربد وضرع وشیر

‏وت

‏صر یج « بر وزن صریم ‎Gus‏ است

‏دربایی وپیشتر در ساحل و کنار ‎bye‏ بابند ‎٩‏ .

‏صاقبوس = با غین ‎ahd‏ دار بر وزن

‏محبوی » خربز#نارسیده را گویند که‌کالك‌باشد ۷

‏- وبعربی مردم‌ضعیف ولاغر را گویند ۸ و کوش"
پمعنی اول هم عربی است.

‏صو‌هر » بنتح ارل ومیم وسکون الی

‏و رای قرشت ‎.)٩(‏ کل بستان افروزاست ‎AT,‏

‏تاج خروی هم میکوند ‎٩‏ .بویدن ‎OT‏ عطه

‏آورد .

‏)2( چك : ورا .

‏تا پدر کروش قرین آن خود مگیر .
مولوی . «لفت ‎Cua‏ .

‏۳ - ضرع ‎Ce)‏ بفتح اول ‎Ty‏ دوم ؛ ‎Olid Ce‏ « متتهی‌الارب » , ضعیف « مهذب

‏الاسماء» « منتخب اللفات » رك : لفت نامه .

‎rf‏ وم اروسکون دوم «لغت نامه».
۵ - ضرم ‎ci)‏ اول و دوم) (عر) سخت گرسنه گردیدن « تاج

‏و رك : اسطوخودوی .

‎۰۳۹۱ pre 5۱060025 < ۴

‏المصاور بهقی» «منتهی‌الارب» - سخت شدن سوزش و حرارت چبزی « منتهی الارب» - افررخته

‎oT ous‏ وشمله زدن ‎oT‏ « منتهی ‎COM‏ . رك : لغت نامه.

‎re aye ٩
```


## [2026-09-04T22:48:09.810Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PLA grep\"; grep -n -i \"azdah\\|aždah\\|ažda\\|Azdahag\\|dahak\\|Dahāk\\|ضحاك\\|Drachen\" incoming/PLA/PLA_pages.txt | head -20",
 "description": "Grep Asbaghi PLA"
}
```


### [2026-09-04T22:48:09.857Z] TOOL RESULT

```
=== PLA grep
721:yes!                  -             afdahäk:                  "ein         bestimmter                       Drache"           aus     dem       pers.       (»>;ı           azdaha
723:          "Drache"                                         mp.     40 ar azi-dahak
724:                                                                         ai-dahak                                       aw. azı-cana
4274:ob)       _           arhbän:             "Drachenwurz,                 Artemisia,          dracunculus"             Ic          mp.9J)pP tarak,
10721:Ol» - dahhäk „ Pachender; Name eines Königs" * — pers. L,.ı aZdahä
10722:        "Drache"         °         a.             gahäka        >>paz.             Dahak       "böser,        demönischer         König"
10726:        Hieraus        zunächst               tk.       asder,           bulg.      / serb.           a2der    7, mand.       asdahak           .
11025:ob.      -       tarhän’ : "dracunculus,                            Drachenwurz,           Tarragon"    'o mp.9p tarak
14140:        Mithras           Geburtstag                und       der       Tag    seines            Sieges       über         Dahak     q.    v.
```


## [2026-09-04T22:48:11.023Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF grep azhdaha\"; grep -n \"اژدها\\|اژدر\\|اژی\" FSF_pages.txt | head -20",
 "description": "Grep FSF for azhdaha"
}
```


### [2026-09-04T22:48:11.072Z] TOOL RESULT

```
=== FSF grep azhdaha
1076:         ‫از ناصر خسرو (دیوان ‪:)۸۴-۳۲‬‬               ‫بسادخترم باید اژدهایی رکاه در کوه‬
1082: ‫نه اسانی نکهام این جهانی‬                                        ‫همی گویدش اژدهاگیر باش‬
1088:          ‫که آن شاه و لشکر بدینسو گذشت‬             ‫می‌آید‪ :‬یعنی‪ :‬یااژدها رابکش یااز پیوند و‬
1303:                   ‫«برانگیختن» (ج‬                     ‫اژدها را حرب ننگ آید که با حربا کند‬
1316:     ‫بسه انبوه تا خیره گردد سرش‬                       ‫اژدها را حرب ننگ آیدکه با حربا کند‬
1711:          ‫دو فرسنگ چون اژدهای دژم‬                        ‫درآویختن و دست به گریبان شدن‪:‬‬
2248:                                                   ‫یکی باره زیر اژدهایی به کف‬
3224: ‫بر آن اژدهافش سپردندشان‬                                              ‫اسن (بهفتح و بهسکون نون)‬
3572: ‫به کوه بزرگ اژدهای سترگ‬
4330:‫تن اژدهارا به دو نیم کرد‬
5872:‫اگراژدهارا بکشد دخترش رابهاو خواهد‬                    ‫(‪)۵-۷-۱۲‬‬
6313:                    ‫ولی دبریت زی‬                         ‫کهگربرمن ایناژدهای بزرگ‬
6434:        ‫‪E‬‬                      ‫‪EE‬‬                       ‫جهان را ازو [اژدها] بود دل پرهراس‬
6752:‫که آن اژدها زشت پتیاره بود‬                       ‫در جهانگیری و برهانگذشته آانزچه ک دهر‬
7508: ‫وگر خیره سوی دم اژدها‬                                      ‫تو اکنون سوی لکشر خویش پوی‬
10488: ‫تن خشندی دیدم از روزگار‬                           ‫بسرستم من از جنگ آن اژدها‬
10885:                                                      ‫که خوشان بدیم از دم اژدها‬
11992:‫بر آن‌گرگ و آن اژدهای سترگ‬                          ‫‏‪١‬۔دستر سی «دست‌رس» (رشیدی» برهان)‪:‬‬
12311:‫ببین این دمآهنج نر اژدها‬                                        ‫هلاک برآوردن هلاک کردن‪:‬‬
12348:                          ‫دمدار (باپیش اول)‬         ‫اسفندیار صفت برای اژدهاست‪ .‬اسفندیار‬
```


## [2026-09-04T22:48:20.872Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && for L in 721 10721; do blk=$(awk -v L=$L 'NR<=L{n+=gsub(/\\f/,\"\")} END{print n+1}' PLA_pages.txt); echo \"line $L -> leaf $blk -> printed $((blk-15))\"; done; echo \"=== leaf for 721\"; awk 'BEGIN{RS=\"\\f\"} NR==20' PLA_pages.txt | sed -n '1,40p'",
 "description": "PLA page mapping"
}
```


### [2026-09-04T22:48:23.047Z] TOOL RESULT

```
line 721 -> leaf 20 -> printed 5
line 10721 -> leaf 205 -> printed 190
=== leaf for 721
’abi&am                                                                                                      5                                                                   abdahäak


     3                              -                                                     -
a             - ’apiäam:                                   "Seide"             -’abrisam                   a.     vv

          5                              -
>,>2\-                         ’abiward:                     eine         Stadt           im       Westen              v.    Marw;         in   der        Provinz           Khorasan


              s                 >     _.7T  Fi                                            >     nu?
Sd,zt                  -            abiwardi:                     Nisba             v.        abiward,


&             utraß:                          "eine              Sorte          von       Zitrusfrüchten"                           aus     pers.      Mg          torang            1   .
          targ.                     Onk.               Inn“,            SYT.         {yet          ;       Iyodi,           mand.     trunga,              hebr.        max          2, dtsch.
         Orange                         "Apfelsine"                                 pers.          >        ar.        >     Sp. >          frz.      3,
         österr.                             Aranzini                 "verzuckerte                         od.     schokoladeüberzogene                            Orangenschalen"
          <                pers. >ar.                              >it.
         Orangeade                                 "Getränk               aus        Orangensaft"                             pers, B> ar. B>- SP.
         Orangerie                                 "Gewächshausanlage"                                           pers.        >      ar.    >       SP.     B>/ frz.             5


 &>>1-                     ”utrußßa:                        nom.          un.        v.       utruß
                                                                                              utrug             "ein        Stück     utrug"          q.     v.        6,


>] - ’utrußgi:                                              "orangenfarben,                                rotgelb"           Nisba v.’utruß .

                      - ”utrugiyya                               Nisba v.                 utruß q. v.

     m;                    >                   x                      7
&>!-                           "atrung                 =    utrug              q.    v.


 a                -        ’atrand                     = utrug             a         v

   “;                 >»      _4ıT                                                                     7
 O>t-                      “atun:              "Backofen"                      pers,           ?
```


## [2026-09-04T22:48:29.761Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && awk 'BEGIN{RS=\"\\f\"} NR==20' PLA_pages.txt | sed -n '40,110p'; echo \"=========== leaf 205\"; awk 'BEGIN{RS=\"\\f\"} NR==205' PLA_pages.txt | sed -n '1,60p'",
 "description": "PLA p.5 and p.190"
}
```


### [2026-09-04T22:48:31.844Z] TOOL RESULT

```
              3                >                                                                                                                                   :         x       -
yes!                  -             afdahäk:                  "ein         bestimmter                       Drache"           aus     dem       pers.       (»>;ı           azdaha
                                                                                                                                                                                             9
          "Drache"                                         mp.     40 ar azi-dahak
                                                                         ai-dahak                                       aw. azı-cana
                                                                                                                            afi-dahä ® ‚ mand.                              asdaha
                                                                                                                                                                            ascahag
          s.               dahhäk                  „



1.       Fraenkel                             s.       v.
2.       Macuch                         Ss.    v.
3.       Fremdwörterbuch                                         s.       v.
4,       ebda.
5.       ebda.
6.       LD.               s.           v.
7.       Steingaß                             s.       v.
8.       Nyberg                         Bd.        II       s.     v.
9,       Macuch                         Ss.    v.

=========== leaf 205
saidaläni                                                                  190                                                          garih

Ya          - saidaläni                  = sandanäni                 q.    v.


ls        - saidalani                   = sandaläni                 q. v.

a=ır-       siga:      "Zeitehe",                  wahrscheinlich                   aus    mp.)         dagar    "wife       of   the    second
        degree"


wr#?-    sin:     China pers.                           ang     &in,       mand.         Sin    (p.ce)


<s“*-     sini:        Nisba            v.    sin, mand.                 finia      3,


                                                                               D



Ol» - dahhäk „ Pachender; Name eines Königs" * — pers. L,.ı aZdahä
        "Drache"         °         a.             gahäka        >>paz.             Dahak       "böser,        demönischer         König"
        arabisiert            in zahhäk
                                     ax e.
                                                                                                                                           8
        Hieraus        zunächst               tk.       asder,           bulg.      / serb.           a2der    7, mand.       asdahak           .


albo1o_           daräbhäna:                  "Münzstätte!"                pers.         9, eigentl.           eine    ar.    pers.      Zu-
        sammensetzung.                   Aus       dem        ar.    <—-       darräb,         nom.     agent.    v.    daraba      „_..
        "schlagen"            + pers.              =L         hane       "Haus".


lo.             darbbäna                = daräbbäna                 q.    v.


e-       darag=               adrig q.            v.


&>-      darra$        = adrig q.                  v.


@&- garig = adriß a. v.

1.   Mackenzie           s.       Vv.
2.   Macuch       s.     v.
3.   ebda.
4.   Wahrmund
           Ss. Vv.
5.   Horn    Np     Etym.           5.       19    Nr.        76.
6.   Nyberg       Bd.        II     s.       v.
7.   Lokotsch          Ss.    v.
8.   Macuch       S.     v.
9.   Wahrmund          s.     v.
```


## [2026-09-04T22:48:47.892Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -5 FSF_pages.txt; echo ...; grep -c \"pdf page\" FSF_pages.txt; echo \"=== find azhdaha headword\"; grep -n \"اژدها\\b\" FSF_pages.txt | head -3; awk 'NR<=3224 && /pdf page/{p=$0} NR==3224{print p}' FSF_pages.txt",
 "description": "FSF page structure"
}
```


### [2026-09-04T22:48:49.884Z] TOOL RESULT

```
   ‫‪۵‬اژهنامکت‬
‫فرهوناکژته‌هایدشوارشاهنامه‬
  SAN    ۹ 75035 7-3
          ۱
  ‎‫ا‬
...
0
=== find azhdaha headword
1076:         ‫از ناصر خسرو (دیوان ‪:)۸۴-۳۲‬‬               ‫بسادخترم باید اژدهایی رکاه در کوه‬
1082: ‫نه اسانی نکهام این جهانی‬                                        ‫همی گویدش اژدهاگیر باش‬
1088:          ‫که آن شاه و لشکر بدینسو گذشت‬             ‫می‌آید‪ :‬یعنی‪ :‬یااژدها رابکش یااز پیوند و‬
```


## [2026-09-04T22:48:54.030Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && blk=$(awk -v L=1082 'NR<=L{n+=gsub(/\\f/,\"\")} END{print n+1}' FSF_pages.txt); echo \"leaf $blk\"; awk -v n=$blk 'BEGIN{RS=\"\\f\"} NR==n' FSF_pages.txt | head -60",
 "description": "FSF leaf with azhdaha"
}
```


### [2026-09-04T22:48:55.967Z] TOOL RESULT

```
leaf 31
 ‫آسودن‬                                       ‫‪۳۷‬‬


           ‫شناسی تکوردار گودرزیان‬                          ‫ز بس انديشه کردن گشت دلتنگ‬

‫بهآسانی و رنج و سودو زیان‬                          ‫رخش بی‌رنگ و پیشانی پرآژنگ‬
 ‫(‪)۵-۵۵-۲۱۸‬‬                                                                         ‫آژیر‬
              ‫ميان بسته دارند پیشم به پای‬         ‫گیری ‪-‬‬     ‫هااحن‪-‬‬ ‫جصح‬‫‪«-۱‬پرهیزکار» (‬
 ‫همیشه به نیکی مرا رهنمای‪.‬‬                        ‫برهان) رشیدی این معنا را با تردید از‬
            ‫از رودکی (نفیسی بیت ‪:)۰۱۲‬‬                                  ‫جهانگیری نقل می‌کند‪:‬‬
      ‫عیال نه‪ .‬زن و فرزند نه» معونت نه‬             ‫اهرن نام از بزرگان روم خواستار دختر‬
‫از اینهمه تنمآسوده بودو آسان بود‬                    ‫قیصر است‪ .‬قیصر می‌گوید برای همسری‬
         ‫از ناصر خسرو (دیوان ‪:)۸۴-۳۲‬‬               ‫بسادخترم باید اژدهایی رکاه در کوه‬
          ‫جای رنج و اندهست این ای پسر‬              ‫سقیلاست نابو د کنی‪ .‬در بیت زیر دوست‬
 ‫جای آسانی و شادی دیگرست‬                           ‫گشتاسب این پیشامد را برای گشتاسب‬
   ‫اگزرفخگرانی (ویس و رامین ‪:)۸۳۲-۲۸‬‬               ‫حکایت می‌کند و از او برای اهرن یاری‬
              ‫نخواهم بی تو یارا زندگانی‬                                           ‫می‌خواهد‪:‬‬

 ‫نه اسانی نکهام این جهانی‬                                        ‫همی گویدش اژدهاگیر باش‬
                                                   ‫گر از خویشی قیصر آژیر باش‬
                                                  ‫‏)‪(OYO-f:-7۶‬‬

         ‫همان راه دریابه یکس‌اله راه‬              ‫باینتو‌های پیش و پس‪.‬‬      ‫امزفهوم بی‬
 ‫جتان یز شد باد در هفت ماه‬                         ‫معنایی کهسه فرهنگ نامبرده داده‌اند بر‬
          ‫که آن شاه و لشکر بدینسو گذشت‬             ‫می‌آید‪ :‬یعنی‪ :‬یااژدها رابکش یااز پیوند و‬
 ‫که از بادکژ آستی‌تر نگشت‬                          ‫خویشی باقیصر «پرهیزگار»باش‪ .‬پرهیز‬
 ‫(‪)۵-۶۵۳-۰۶۲‬‬                                                                ‫کن» دوری جوی‪.‬‬
         ‫از اسدی ( گرشاسب‌نامه ‪:)۷۰۴-۳۰۱‬‬                                        ‫یاو‪:‬‬
                                                                                   ‫هاده‬
                                                                                      ‫مام‬
                                                                                        ‫‪-۲‬‬

    ‫تگوفتی کههر یک عروسیست مست‬                                   ‫ییککی نغز پولاد زنجیر داشت‬
‫نوان و استی‌ها فشانان به دست‬                       ‫نهان کرده از جادو آژیر داشت‬
              ‫‪:)۲۵۳‬‬    ‫وعدان‬
                           ‫یس‬‫دعود‬
                                ‫(مس‬
                                  ‫از‬               ‫(‪)۶-۹۷۱-۷۱۲‬‬


                ‫وهر دامنی فرو ریزد‬
                                 ‫گز‬‫ا‬                                ‫بر زاد فرخ یکی پیر بود‬
 ‫گر آستی‌ی ز طبع بفشانم‬                           ‫کهبرکارها کردن آژیربود‬
                                     ‫آسودن‬         ‫‏(‪٩‬رویز ‪)۹۱۹۳‬‬
                                                             ‫پ‬
                                                                                        ‫آسانی‬
‫(نقیض فرسودن) آگررامفتن» آسایش و‬
                         ‫استراحت کردن‪:‬‬
                                              ‫آسودگی؛ بی‌رنجی (نقیض دشواری» رنج) به‬
                                                         ‫نگاه کنید‪:‬‬     ‫ننی‬
                                                                          ‫ساناوت‬
                                                                               ‫آنآس‬
                                                                                  ‫واه ت‬
```


## [2026-09-04T22:49:02.787Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==37' FSF_pages.txt | head -70",
 "description": "FSF printed page 43"
}
```


### [2026-09-04T22:49:04.397Z] TOOL RESULT

```
‫آکندن‪ .‬آگندن‬


‫آفریننده‪,‬در واژه‌های مرکب جهان‌آفرین»‬                  ‫انزاصر خحسرو (دیوان ‪:)۱۷۲-۲۱‬‬
                            ‫جان‌آفرین‪...‬‬                      ‫گر اهل آفرین نیمی هرگز‬
                            ‫آفریناد آ=فریندا‬   ‫جهان چون کنندی نفرینم؟‬
            ‫وعا‪:‬‬
               ‫آفریند ‪+‬الف آرزومندی د‬           ‫از گفخررگانی (رویاسموین ‪:)۲۴۴-۳۰۵‬‬
              ‫کزان بوم خیزد سپهبد چو تو‬                ‫مرانفرین تو چون آفرینست‬
‫فزون آفریناد ایزد چو تو‬                         ‫کفهتارت بگهوشم شکرینست‬    ‫گ‬
‫(‪-۸‬هرمزد ‪)۷۸۶۱‬‬                                 ‫در بیت زیر فردوسی نفرین رابه معنی‬
                              ‫آفرین خانه‬       ‫رنننجاوخوشی و آفرین رابه معنی‬
        ‫خانة ستایش و نیایش» پرستشگاه‪:‬‬                              ‫خوشی بکار می‌برد‪:‬‬
 ‫از هزار بیت دقیقی در شاهنامه‬                          ‫چنین گفت کاین روز ناپایدار‬
                            ‫(‪۶-۶۶-۸۱)۰‬‬         ‫گهی جزم سازد گهی کارزار‬
‫[لهراسب] به بگلزخین شد بر آن نوبهار‬                     ‫ار‬        ‫ییک ان زمه‬
‫که یزدان پرستان بدان روزگار‬                    ‫به نفرین بود گه گهی بآفرین‬
 ‫خحسانه را داشستندی چان‬          ‫مران‬           ‫(‪)۴-۱۶۲-۴۰۸‬‬

‫که مر مکه راتازیان‌ این زمان‬                   ‫‪-۲‬به معنی آفرینش‪ ,‬آفریدن؛ در بیت زیر‬
‫آن در آفرين خحاه را‬            ‫ببست‬                            ‫رنددن است‪:‬‬
                                                                        ‫ورز‬
                                                                          ‫آاد ف‬
                                                                              ‫مر‬
‫نمانداندرو خویش و بیگانه را‬                    ‫بهرام نوجوان به پروردگار خود منذر‬
                        ‫آفرینش (اسم مصدر)‬                                      ‫گوید‪:‬‬
                  ‫‪-۱‬آفرین و نیایش کردن‪:‬‬                  ‫اگر تاجدارست اگر پهلوان‬
           ‫بزرگان ایران گزفتار اوی‬              ‫به زن‌گیرد آرام مرد حوان‬
 ‫به روی زمین برنهادند روی‬                              ‫همان زو بود دین یزدان به پای‬
               ‫چو از آفرینش بپرداختند‬           ‫جوان را به نیکی بود رهنمای‬
‫نوندی ز ساری برون تاختند‬                                 ‫کنيزک بفرمای تاپنج و شش‬
 ‫(‪)۲-۰۴-۷۹۴‬‬                                     ‫وورشید فش‬
                                                        ‫بیارند با زیب خ‬
                  ‫‪-۲‬اسم مصدر از آفریدن‪:‬‬                  ‫مگر زان یکی دگوزین آیدم‬
            ‫نخست آفرینش خرد را شناس‬            ‫هم انديشة آفرین آيدم‬
‫نگهبان جانست و آن سه پاس‬                        ‫(‪)۷-۳۷۲-۴۵۱‬‬

‫(‪)۱-۴۱-۷۲‬‬                                                      ‫مگر نیز فرزند بینم یکی‬
                             ‫آندن‬
                                ‫آندن‪ .‬ک‬
                                      ‫ک‬        ‫که آرام دل باشدم اندکی‪.‬‬
                        ‫پر کردن‪ .‬انباشتن‪:‬‬      ‫یزدن =‬     ‫فمر ا‬‫آرخ‬ ‫‪-۳‬اسم فاعل م‬
```


## [2026-09-04T22:49:12.108Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {split($0,a,\"\\n\"); print NR\": \"a[1]}' FSF_pages.txt | sed -n '35,60p'",
 "description": "FSF leaf headers 35-60"
}
```


### [2026-09-04T22:49:14.282Z] TOOL RESULT

```
35:      ‫آغالیدن‬                                     ‫‪۳۱‬‬
36:                                                                                      ‫آغشتن‬
37: ‫آکندن‪ .‬آگندن‬
38:                                                                                              ‫آنده‬
39: ‫آن سر‬
40:                                                                                              ‫آنک‬
41:  ‫آوردگاه‬
42:                                          ‫‪۸۳‬‬                                         ‫آوردن‬
43:                                              ‫‪۳۹‬‬
44:            ‫آن بادساری از دل بیرون کن‬
45:               ‫که فر کیان دارد و چنگ شیر‬                       ‫از منوچهری (دیوالن» ‪:)۲۳‬‬
46:                                                                               ‫آهیختن‬
47: ‫آیین‬                                     ‫‪۳۳‬‬
48:                   ‫لر‬
49:    ‫رگژونگ‬
50:                                                                                      ‫ارج‬
51:  ‫آزوند‬
52:                                                ‫‪۳۸‬‬                                             ‫ازار‬
53: ‫ازیرا‬                                             ‫‪۳۹‬‬
54:                                               ‫‪۵۰‬‬                                         ‫آژدها‬
55:  ‫اشنان‬                                          ‫‪۵۱‬‬
56:                                                  ‫‪۲۵‬‬                                          ‫افراختن‬
57: ‫افشاندن‬
58:                                                                                  ‫افکنده‪ .‬افگنده‬
59:            ‫تو گفتی که الماس جان داردی‬                          ‫سوم تیز و تازانه باز آورم‬
60:                                                                                              ‫انجامش‬
```


## [2026-09-04T22:49:18.955Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==54' FSF_pages.txt | head -45",
 "description": "FSF azhdaha entry page"
}
```


### [2026-09-04T22:49:20.757Z] TOOL RESULT

```
                                              ‫‪۵۰‬‬                                         ‫آژدها‬


   ‫بند ‪ ۲۱51705۵‬یوستی بندهش ص ‪:)۳۶‬‬                         ‫ازیرا سرت ز آسمان برتر است‬
                       ‫میدان اسب‌تازی‪:‬‬                 ‫ست‬
                                                        ‫رمور‬
                                                           ‫هآننا‬
                                                               ‫وتوز‬
                                                                  ‫گخم‬
                                                                    ‫کهت‬
          ‫نشانی نهادند بر اسپریس‬                    ‫رتم‪۲۴۲۱‬‬
                                                                                        ‫آژدها‬
 ‫سیاوش نکر د ایچ بکاس‌مکیس‬                                                   ‫کنایه از نیزه‪:‬‬
 ‫(‪)۳-۹۸-۸۶۳۱‬‬
                ‫=یستادن‬
                      ‫استادن (بهکسر اول) ا‬
                                                   ‫یکی باره زیر اژدهایی به کف‬
               ‫ایستادگی و پایداریکردن‪:‬‬              ‫(‪)۶۲۵۸۱‬‬
 ‫در شاهنامه‬      ‫یتقی‬
                    ‫ق بی‬
                       ‫دار‬
                         ‫از هز‬
                                                              ‫و در چند بیت سپس‌تر گوید‪:‬‬
                ‫(‪۶۲۱۹-۱۷۳‬و ‪۳۰۱-۱۵۵6‬‬
       ‫نه استد کس آن پهلوان شاه را‬                            ‫بزد نیزهگشتاسپ بر جوشنش‬
                                                    ‫بخست آن زمان کارزاری تنش‬
‫ستوه آورد شاه خرگاه را‬
                                                                            ‫اول)‬    ‫ر‬
                                                                                    ‫سبه‬
                                                                                      ‫کر (‬
                                                                                         ‫اسپ‬
       ‫همی کشت زیشان همی خوابنید‬
 ‫مر او رانه استاد هر کش بدید‬                                                    ‫چو‬
                                                           ‫بباريد تير از كمان سران‬
                               ‫استام = ستام‬

                        ‫لگام اسب» دهنه‪.‬‬
                                                   ‫به روی اندر آورده کرگ اسپران‬
                                                    ‫)‪(0-441-۳04‬‬
 ‫در شاهنامه‬       ‫قی‬‫یت‬
                     ‫ق بی‬
                        ‫دار‬
                          ‫از هز‬
                                                   ‫(کرگ اسپر و اسپر کرگ یعنی سپری که از‬
                           ‫(‪)۶-۵۷-۰۶۱‬‬
```


## [2026-09-04T22:49:37.566Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 5605-5620\"; sed -n '5605,5615p' incoming/WLD/WLD_Bd1_pages.txt; echo; echo \"=== WLD Bd1 5905-5920\"; sed -n '5900,5920p' incoming/WLD/WLD_Bd1_pages.txt",
 "description": "Walde-Pokorny angh entries"
}
```


### [2026-09-04T22:49:37.628Z] TOOL RESULT

```
=== WLD Bd1 5605-5620

aksl. qgh> „Winkel“ urverwandt ist) „Winkel“? (oder dies zu ango, angustusl
Nicht recht Mar ist das g von lat. ungulus , ungustus s. o.).
     Lit. bei Vf.           LWb. s. v.; dazu Persson Wtf. 421a.

angh- (kelt. aueh engh-) „eng, einengen, schntiren“, z. T. auch von seelischer
    Beklemmung, Angst.
  Verbal av. qzimhe „zu bedrangen, in Not zu bringen“, tiefstufig av.
               :



=== WLD Bd1 5905-5920
                             ;                                                                          .




  Unsicher ist Anreibung von as. egithassa, mnd. egidesse ags. (verderbt)                       ,


apuxe, abd. egidehsa, nhd. Eidechse mit ewi-, egi- — ogig (Zupitza Gutt. 99
nach Kluge; Falk-Torp u.                     ogle).

      Ob in diese Mannigfaltigkeit so Ordnung zu bringen                                        sei,   daB       aiag'i.lii-

und eghi-, oglii- (gh) eine Kreuzungsform eg'ihi-, og*hi- hervorgerufen hiitten
(Yf. LEWb. 2 u. anguis), bleibe dahingestellt.                                — DaB *ang*(h)is als „con-
strictor“ (Fick II 4 15;                Fay Transact. Am. Phil. Ass. 41, 37 f.) zu angh- ge-
hore,    wegen der Gutturalverscbiedenbeit und sacblich zu bestreiten, da
          ist

bei den  kleinen europaischen Sclilangenarten das Tier gewiC nicht vom
Erdriicken der Beute benannt ist.      Aber auch Osthoffs IF. 4, 292 An-
```


## [2026-09-04T22:49:40.419Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT\"; grep -n \"^anger\\|^anguish\\|^anxious\\|^anguine\\|^eel\" SKT.txt | head; echo \"=== NYB glossary niyaz\"; grep -n \"niyāz\\|niyaz\\|ny'z\\|nyʾc\" NYB_vol2_glossary.txt | head; echo \"=== IEC\"; grep -n \"^angh\\|anghos\\|^angṷ\\|anguis\" IEC.txt | head; echo \"=== SYN snake\"; grep -n \"anguis\" SYN.txt | head",
 "description": "Skeat, Nyberg, Mann, Buck greps"
}
```


### [2026-09-04T22:49:40.507Z] TOOL RESULT

```
=== SKT
=== NYB glossary niyaz
=== IEC
544:anghostis, see an2uhəstis
545:anghó, ið “press, squeeze, strain, confine’. WP I, 62. Cf. angho, anguho. (Much of the evidence for these forms is ambiguous) Av. aíigh-; Arm. z-angem, cpd. ‘knead’, ç- angem, cpd. ‘hedge round’; Gk. ánkho; Alb. cf. ang ‘nightmare’; Lat. ango, -ére; Osc. cf. angitust (‘shall demand’ or sim.); MIr. angim, con- ‘protect beside angtha (pp. as adj. "dit. ficult); Ir. cumh-angaim ‘confine’; W angu ‘contain’; OE angian ‘grieve’; OFris. angia ‘fear; MDu. cf. ang. ‘afraid’; Li. (ambig.) éngiu, ti ‘squeeze’ beside angà ‘doorway’, cf. Pol. weg-ar, id. (Li. engti is e-grade, see un- der eng-. Go. ga-aggwjan: MHG engen derive
551:anghros, å ‘raging, bitter; rage, bitterness’ Av. añgra; Tokh. (?) ankāre ‘profligacy’; Olr. égair ‘ferocious ON angr, gs. angrs: Nor. anger: Sw. ånger; Finn.LW ankara ‘severe’
552:anghulos, anghlos, is “angle, corner’. WP I, 61. Cf. ank-, onk-, onk- Skt. ánghrih ‘foot’; Oss. ángurá (ambig.) “fish- hook; Lat. angulus; Umb. anglo-; OHG (ambig.) angul “fish-hook; MHG angel “hinge, fish-hook'; OE angel; ON ongull, pl. onglar; OCS oglü ‘corner’ and com. SI.
560:WP I, 63. Cf. oguhis Lat. anguis, cf. anguilla; Br. anv 'slowworm' (Br. -v- from -guh-, as in devi, v. ‘burn’, from dheguh-, q.v.); OCS oZ 'grass-snake"; R už ‘adder’; Li. angis, f. ‘viper’; cf. anginas “a poisonous serpent’; Latv. odze ‘viper’
564:angho, ið ‘cramp, straiten, force’. WP I, 62. Cf. anghó, anguho (Most of the evidence is ambiguous. For Per. Go. ON and OCS forms, cf. anguho. For Av.Gk.Lat.OlIr. forms see angho)
566:anguhostos, is “narrow; constrained; anxi- ous; strain, anguish’. WP I, 62. Cf. anguhis, os, anguhó, anghó and WP I, 61-63 Av. ásto; n. gs. -áh- ‘oppressor; oppression"; Alb. anksht ‘wild’; Lat. angustus, angustia; OHG angust 'fear'; OFris. angost; Sw; àn- gest; ON angist: OCz. üZest, d: Li. afik3tas; afikStis, f. “narrow; strait beside ankstis, f. “fear”. (For Latv. oksts, oksta and OE ohsta see ankst- below)
570:anĝuhis, anghus “narrow, thin, close, tight’; anĝuhos, is, å ‘clamp, hinge, corner; strait; anguish’ WP I, 61-63. See next Skt. *amhuh (compar: amhīyah), adi. Oss. dim. wngäg; Arm. dim. andzuk; Alb. cf. eng “stupid”; MIr. ang- cpds. 'dire-; Cor. yn; W cf.cpd. cyf-yng (= Mir cumh-ang “narrow, tight); Go. aggwus; OHG enge; ON ongr; OCS dim. gzükü. For the noun reflexes cf. Skt. amhas, amhu; Av. ázo, -áh-; Oss. wng, ungá; Gk. ágkhi, agkhoü ‘near’; Alb. ang ‘bogey’; Lat. angina; Olr. ing ‘strait; OHG enge; MHG ange ‘hinge, fish-hook'; ON ongvar, pl. ‘straits, beside eng, engi, n. ‘meadow’; OCS oza ‘bond’; R üzy, pl.id. beside uzdà ‘bridle’; Li. anga ‘doorway, aper- ture’. (Many of the above forms are of am- biguous background, cf. angh-, angh-. For ON ang, angi ‘fragrance’, see onguh-)
3371:dhuél- ‘languish, expire, gasp’. See dhuol-, dhul-, dhul- OHG twélan; MHG er-, vertwëln ‘expire’; (z-gde in Li. dvylu, dvilti ‘wane, pine’; OE dwolma ‘chaos’; Norw. cf. dolmen ‘faint’ be- side ON dylminn ‘indolent. (Long-grade iso- phone in Li. dvēlē 'spirit). Av. dvar- ‘rush, as demons’ is ambig. Cf. Skt. a-dhvaráh re, ligious ceremony’. Cf. also OHG twala, OS dwala “hesitate?
5679:&eur- (ĝeurið) (1) ‘ailing, sad; mourn, langu- ish’. Cf. &eruos Arm. ciwr, ost ‘lean’; ciwrim ‘languish’; OHG kiur-, cpds. as in kiur-driozon “suffer”; kiur-chundon ‘report bad news’; Ukr. cf. žurba ‘grief’; Zur-lyvyj ‘saď’; za-Zurenyj ‘careworn’; Srb. Zurav ‘puny’; Blg. Züri se, 3s. ‘die out
=== SYN snake
5163:Grk. — b¢us (és) Goth. waurms, nadrs Lith.  gyvaté (angis, Zaltys) NG Sdus, pl5e ON ormr, nadr, snakr Lett. _ éiska Lat. anguis, serpéns, Dan. _ slange, snog ChSl. zmija
5165:1. Grk. égis (NG gid fr. dim. ogl- doy), beside gus, exdva ‘viper’ (less generic than és cf. Aristot. HA 511914 ff.); Lat. anguis; Lith., OPruss. angis; ChSl. *qzt, Pol. waz, Russ. uz; Skt. ahi-, Av. adi-; fr. parallel forms with and without nasal, but phonetic rela- tions in part obscure. Walde-P. 1,63 ff, Emout-M. 52. Walde-H. 1.48,
5432:Lat. cruor ‘blood from a wound, gore’ (as distinguished from generic sanguis; cf. also cruentus ‘bloody’); Ir. cri, NIr. cro, W. craw (obs.), Corn. crow, all used mostly like Lat. cruor; Lith. kraujas, OPruss. craujo, krawia, ChSI. kriivt, etc., the general Balto-Slavic (except Lett.) word for ‘blood’ : Grk. xpéas ‘meat’, Skt. kravis- ‘raw flesh’, Av. zra- ‘raw flesh’, Skt. krira- ‘raw, bloody’, Av. See ‘bloody, fierce’, OF hréaw Taw’, etc.
5437:4. Lat. sanguis (early neut. sanguen) ~inis (> the Romance words), etym.? Connection with Skt. asrk, asnas, ete, (above, 1) too complicated to be con- vincing. Cf. refs. in 1, above.
8052:Boh. unaveny fr. unaviti ‘tire, fatigue’ epd. of naviti id., fr. nati ‘waste aay, languish’ : ChSI. -nytz ‘be sluggish’, Lith. novytt ‘torment, oppress’, apparently from the same root as Lett. nave ‘death’, ete. (4.75). Walde-P. 2.316. Miklosich 218.
16096:wendigkeit ‘necessity’ (through the adj. nolwendig; hence Dan. nédvendig, n¢d- rendighet, Sw. nodvandig, naceaniaag at) : OPrus. nautin (acc. sg.) cess ate tress’, Boh. nytt ‘languish’, wnavite ‘tire (trans.), etc. prob. also ChSI. nqézda, muda, ete. (below, 6). Walde-P. 2.316. Falk-Torp 782f. Weigand-H. 2.312. Feist 372.
28311:Of the more distinctive words, several are connected with adjs. for ‘narrow’ (12.62), whence also others for the stronger ‘anguish’, and some are simply ‘disquietude’.
28331:Br. nec’h = W. nych ‘languishing, pining, consumption’, cf. W. nychtod ‘phthisis’, etym. dub. Stokes 190. Walde-P. 2.85.
28337:anguish’, whence Dan. engstelse, Sw. dngslan), OHG angust, MHG angest, NHG angst : OE ange, OHG angi, engi, NHG eng ‘narrow’. Cf. Lat. anzxietds, etc. (above, 2). Falk-Torp 29. Weigand-H. 1.61.
28651:ME angre, NE anger, fr. ON angr ‘trouble, affliction’ (so also ME angre) : Lat. angor ‘constriction of the throat, anguish, trouble’, Skt. a7thas- ‘distress, need’, ON ongr, OE enge, OHG angi, engi ‘narrow’, etc. Falk-Torp 29. Walde-P. 1.62.
```


## [2026-09-04T22:49:58.033Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5610,5640p' incoming/WLD/WLD_Bd1_pages.txt; echo \"=== page markers around\"; awk 'NR>=5560 && NR<=5620' incoming/WLD/WLD_Bd1_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | head",
 "description": "WLD angh- entry full"
}
```


### [2026-09-04T22:49:59.832Z] TOOL RESULT

```
angh- (kelt. aueh engh-) „eng, einengen, schntiren“, z. T. auch von seelischer
    Beklemmung, Angst.
  Verbal av. qzimhe „zu bedrangen, in Not zu bringen“, tiefstufig av.
               :



ny-azata „sie schntirt sich“, ny-Ctzaysn „sie sollen hineinzwangen“ (zum d
s.   Bartholomae IF.                       8,          235 m. Lit., Altiran. Wb. 362; ved. ahenia etwa
„mogen wir rfisten“ liegt in der Bed. ab; nnaiia RY. 8, 45, 5 ist unklar);
     gr. ay/co „sehntire                       zusammen, erdroBle“, lat. ango „beenge, schntire zu“;
             -Yerbuni ajq, qsiti „beengen“; dazu mit Tiefstufe sehr wahr-
     aksl. als     i


scheinlich aksl. veia, vrzali „binden“ (c- hiatusfiillender Yorsehlag, siehe
Pedersen KZ. 38, 311 39, 437, Meillet Msl. 14, 369, vielleicht festge worden
                                               ;


durch Einflutl von viti „winden“, das aueh die Bed. beeinflufit haben mag?
Das yon Vondrak SI. Gr. I 184 fur idg. Alter des v- ins Feld gefiihrte lit.
vyzti vyzenas ..Bundschuhe flechten“, vyzd „Ba3tschuh“ •wohl zu einer Pala-
talerweiterung von *uei- „-winden“).
  *onghii-s ,,eng“ ai. nur in amhu-bhtcll f. „engspaltig“ und im Abl. sg. n.
                                  :



amhos „Bedrangnis“ (Ableitung amhurd- „bedrangt, ungliicklich") gr. in                                         ;

=== page markers around
```


## [2026-09-04T22:50:09.356Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" incoming/WLD/WLD_Bd1_pages.txt | head -3; blk=$(awk -v L=5610 'NR<=L{n+=gsub(/\\f/,\"\")} END{print n+1}' incoming/WLD/WLD_Bd1_pages.txt); echo \"leaf $blk\"; awk -v n=$blk 'BEGIN{RS=\"\\f\"} NR==n' incoming/WLD/WLD_Bd1_pages.txt | head -3",
 "description": "WLD page location"
}
```


### [2026-09-04T22:50:10.910Z] TOOL RESULT

```
leaf 71
                                                   ;                                                                    ;
```


## [2026-09-04T22:50:19.023Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW ango\"; grep -n \"ango\\b\\|angustus\\|anguis\" LEW_1910.txt | head -8; echo \"=== LAT\"; grep -n \"^ango\\|^anguis\\|^angustus\\|ANGO\\|ANGVIS\" LAT.txt | head -8; echo \"=== SKT anger\"; grep -n -i \"anger, \" SKT.txt | head -5; grep -n -i \"anguish\\|anxious\" SKT.txt | head -5",
 "description": "Latin dicts and Skeat"
}
```


### [2026-09-04T22:50:19.102Z] TOOL RESULT

```
=== LEW ango
480:fango II 243
538:Spanisch aliso I 31 arapende (alt) I 66 baga I 93 bahia I 93 bazo I 98 becerro I 104 bicerra I 104 bicha I 102 brisa I 116 calibre I 141 cerio I 219 chamorro I 143 estario II 585 fango II 243 fieltro I 497 gamo I 322 gargola I 602 gualda I 841 halar I 141 natron II 171 nino, nia II 170 otero I 32
10031:kite I 124 languish for I 263 law I 790 league I 787 learn I 331 leer I 239
10454:ango, angul I 46
11145:scouwon I 187 8c63, scoz I 185 screion, screi I 291 screvon II 500 scrian I 291, I1 498 scriban IT 499 scrint IT 500 scritan I 293 scrodén II 498 scrot IT 498 scrotan II 498 scruton, scrutilon IT 498 skubil I 311 skugin(a) IT 196 sculd(a) II 492 skultirra II 492 scum II 196 scuoh IT 196 scuoppa IT 583 scur ,,schauer, Un- wetter®’ I 190 skir ,,Schauer, Ob- dach*‘ IT 196 skiira IT 196 scurz I 273, 317 scutien I 210, II 400 sctitilon IIT 400 scuwo6, sci IT 196 scuz3zila IT 503 slat I 739 slaf I 739, II 661 slafan I 739 slahan I 743 slah I 759 slango I 248 sléha I 816 sléht I 802 slethha I 802 sléo I 751, 816 sléwa I §16 slidic I 749, 813 slifan I 739, 795, $23 slichan I 802 slimen I 802 slingan I 233, IT 195 slink I 759 slio I 802, II 683 sliofan I 823
=== LAT
3782:ango, -Is, -xl, anctum, -ere: etreindre, oppresser, serrer (la gor-
3788:angor est aegritudo premens, Cic.Tu.4,18; le sens physique est reserve
3795:anguis
3798:angustus: etroit,serre; peut-etre d'un thfeme en -s-, cf. onus/onus tus ;
3804:angustus figure comme premier terme de compos 4 dans angusticlduus,
3809:angor - , toujours au sens moral. Le fem. anxia substantiv 4 est atteste
3821:angustus (avec ses derives); cf.v.h.a .angust "angoisse". Le thfeme en
3823:angustus peut-etre egalement tire de la, cf. le type robustus. L'elar-
=== SKT anger
4636:Daotyl.  ^L.  -  Gk.^ metrical  foot  marked  - a  Anger,  a  dactyl.     See  Toe.
6422:Fear.  ^E.)  M.  E.  /eer,  A.  S.  /ir.  * sudden  peril,  danger,  frar.  Otig.  osed  of the  peril  of  travelling  —A-  S./antw,  to  go, travel.  4"  ^^^^'  /«'''•  honn,  G.  pfoAr^ danger.
8096:Grumble,  to  mnrmnr.  (F.  ••  G.)  F. gt^mmefcr  (Cot)  —  O.  and  prov.  G grummtlin,  to  grumble  ;  fre<]iienl.  ol grummtn^  gfomMtn,  to  grumble  i.Du. grvmtrutt).  Allied  to  G.  gram,  anger, grimmtM,  to  rage:  and  to  £  Orlm.
8114:Sj/.+Icel.  gtitr,  Dan,  giest,  Swcd.  giist, a.  gojf,  Goth,  gasts,  G.  gast ;  L.  fiostis, a  stranger,  also  an  enemy.  (^GHAX.) Allied  lo  Hoatae.
8377:lB»ab.(E.)  M.E-Aiirm.  A.S.y(^dr*7i, itobana^loeL  harmr.  gitct.  Dan. ,  wiath.  Swcd.  hami,  anger,  giicl, 'iw,  £ricf.  KuM.  /mm/,  hlianie ;  ^kl. ,  XoC..  (rora  pnJM.  to  be  weary.  (^ if.)  Der  harm,  verb. pony,  concord.  ^F.  -  U  *  Gk.) ■f.  —  F.  Aanfi«»M.  —  L.  Aar- tk.  ifttovia,  a  joint,  proportimi, ^  Gl  ifi*^,  a  joining.  —  Gk. ftt  iVAK) BMB :  sec  Iron.
243:Abeyance,  expectation,  su&pcnsioo.  (F. ~  L.)  F.  ab/iatiff.  s«»i>ciision.  waiting (Roq.)  —  F.  a ;  and  be'ant,  pres.  pt.  of  O.  P . A'Vr  (F.  lkiyer\  to  gajw,  ejt|tecl  anxiously. ••  I«  eui.  at :  and  badare,  to  £a[)e,
702:angina,  acute  pain.    (L.)     L. pain.  lit  choking.  —L.  oMfftrtf  to anxious,  distressed,    (L.)     L.
789:Anxious.  (L.)    See  Angiulah.
1231:was  also  n&ed),  but  rather  from  Icel.  0gK awe,  fear:  Dan.azv.+AS.  tf;$T,  <>^;  Gom. tj^,  fear,  anguish ;  Irish  ^agfiat^  fcar. terror;  Gk.  ix°'i  anguish,  afmctioa;  L anj;ffr,  choking,  anguish  ;  Skt.  ag^A,  fla 1'he  orig.  sense  ia 'choking.*  (<^  AGU.) See  Anffuiali.     Der.  aw-fuL
5610:Dwindle.  (E.)  The  frequent,  form  of M.  E.  dwintn,  to  dwindle,  A.  S.  dwinan, to  dwindle,  languish.  ^  Icel.  dvima^  dvinA, Swed.  tvina,  to  dwindle,  pine  away.
```


## [2026-09-04T22:50:20.263Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN anger\"; sed -n '2758,2770p' KLN_1966.txt; echo \"=== KLN anxious\"; grep -n \"^anxious\\|^anxiety\" KLN_1966.txt | head -3",
 "description": "Klein anger entry"
}
```


### [2026-09-04T22:50:20.328Z] TOOL RESULT

```
=== KLN anger
fr.  Xa-pela,  ‘hired  labor,  worship’.  See  -latry. angelot,  n.,  1)  a  gold  coin ;  2)  a  sort  of  cheese  made
in  Normandy;  3)  a  musical  instrument.  — OF.,  dimin.  of  angele,  ‘angel’.  See  angel, anger,  n.  —  ME.,  fr.  ON.  angr,  ‘sorrow,  afflic¬ tion’,  rel.  to  ON.  ongr,  OE.  enge,  ‘narrow,  pain¬ ful’,  OS.  engi,  MDu.  enghe,  Du.  eng,  OHG.  an-
gi,  engi,  MHG.  enge,  G.  eng,  Goth,  aggwus, ‘narrow’,  and  cogn.  with  OI.  amhu-,  ‘narrow’, arrihah,  ‘anguish,  need,  anxiety’,  Avestic  qzah-, ‘distress,  oppression’,  Gk.  ayyeiv,  ‘to  squeeze’ (esp.  the  throat),  ‘strangle,  throttle,  hang’, ayyovY),  ‘strangling,  hanging;  rope’,  ivyi, ayyou,  ‘near’  (lit.  ‘narrow’),  anaov  (for  *<5iyy-iov), ‘nearer’,  L.  angere,  ‘to  press  together,  throttle, torment’,  angustus,  ‘narrow’.  Arm.  anjuk,  ‘nar¬ row’,  OSlav.  qzQ,  qziti,  ‘to  narrow,  compress’, qzota,  ‘narrowness’,  'qzosti,  ‘a  narrowing,  nar¬ rowness’,  qziiku,  ‘narrow’,  Lith.  ahkstas,  ‘nar¬ row’,  fr.  I.-E.  base  *angh-,  ‘to  narrow,  com¬ press’  ;  the  corresponding  Celtic  base  is  *engh-, *%gh-,  whence  Bret,  enk ,  ‘narrow’,  Ir.  cumung, ‘narrow’,  Ir.,  W.  ing,  ‘distress’.  Cp.  agnail,  an¬ gina,  anguish,  anxious,  and  the  second  element in  cynanche,  quinsy,  squinancy,  Orobanche. Derivatives:  angr-y,  adj.,  angr-i-ly,  adv.
anger,  tr.  v.  —  ON.  angra,  fr.  angr,  ‘anger’.  See anger,  n.
angina,  n.,  inflammation  of  the  throat;  quinsy.  - — L.  angina,  ‘quinsy’,  prob.  a  loan  word  fr.  Gk. iyyovr),  ‘a  throttling,  strangling,  hanging'.  The form  angina  (instead  of  *aneina)  is  due  to  the influence  of  angere,  ‘to  throttle’.  See  anger, tt.,  and  cp.  words  there  referred  to.
Derivative:  angin-al,  adj.
angio-  before  a  vowel  angi-,  combining  form meaning  ‘covered  by  a  seed  or  blood  vessel’,  as in  angiosperm.  —  Gk.  dyyeio-,  fr.  dyyeTov, ‘vessel’,  fr.  Syyo?,  ‘vessel’,  a  word  of  uncertain origin.  Cp.  the  second  element  in  Hydrangea, sporangium,  synangium.
angiology,  n.,  that  branch  of  anatomy  which deals  with  the  blood  vessels.  —  Compounded of  angio-,  and  Gk.  -Xoyia,  fr.  -Xoyoc,  ‘one  who speaks  (in  a  certain  manner);  one  who  deals (with  a  certain  topic).  See  -logy, angioma,  n.,  a  tumor  consisting  of  dilated  blood vessels  (med.)  —  Medical  L.,  formed  with  suff. -oma  fr.  Gk.  ayysiov,  ‘vessel’.  See  angio-. angiosperm,  n.,  name  of  a  large  class  of  plants which  has  its  seeds  inclosed  in  an  ovary.  — Coined  (in  the  Modern  Latin  form  Angiosper- tnae)  by  Paul  Hermann  in  1690  fr.  Gk.  dyyeiov, ‘vessel,  receptacle’  and  cmeppia,  ‘seed’.  See angio-  and  sperm.
Derivatives :  angiosperm-al,  angiosperm-atous, angiosperm-ic,  angiosperm-ous,  adjs. angle,  n.,  comer.  —  F.,  fr.  L.  angulus,  ‘angle, comer’,  which  is  cogn.  with  Arm.  angiun,  anki- un,  OSlav.  qg(u)lu,  ‘comer’,  OSlav.  qkotu, ‘hook’,  Lith.  anka,  ‘loop’,  OI.  angam,  ‘limb’, angulih,  angurih,  ‘finger,  toe’,  angusfhdh,  ‘big toe,  thumb’,  Avestic  angushta-,  ‘toe,  finger’,  OI. ankah,  ‘hook;  bent’,  ancati,  ‘bends,  curves’,  Gk. a'f/.oc,,  ‘a  bend,  hollow’,  dyxtov,  ‘elbow’,  dyxuXo?, ‘crooked,  curved’,  SyxOpa,  ‘anchor’,  L.  ancus, ‘crooked,  curved’,  OE.  ancleo,  ancleow,  ‘ankle’, OE.  anga,  OHG.  ango,  ‘hook’.  All  these  words derive  fr.  I.-E.  base  *ang-,  resp.  *anq-,  ‘to  bend’. Cp.  angle,  ‘fishhook’,  Angle,  anchor,  ancon, angula,  angular,  ankle,  ankylosis,  and  the  second element  in  triangle.  Cp.  also  the  second  element in  sarangousty.  The  above  I.-E,  words  stand  in gradational  relationship  to  Gk.  oyxo?,  L.  un¬ cus ,  ‘hook’,  Mir.  ecath,  ‘fishhook’;  cp.  Uncaria, unciferous,  uncinal,  uncinate,  uncinus,  uncus, aduncus,  Redunca.
angle,  n.,  a  fishhook.  —  OE.  angel,  fr.  anga, ‘hook’,  rel.  to  ON.  ongull,  OHG.  angul  (MHG., G.  angel),  ‘fishhook’,  and  cogn.  with  L.  ancus, ‘crooked,  curved’,  uncus,  ‘hook’.  See  angle, ‘corner’.
Derivatives:  angle,  tr.  and  intr.  v.,  angl-er,  n., angl-ing,  n.
Angle,  n.,  member  of  a  Teutonic  tribe  that  came  in the  5th  century  from  what  is  now  known  as Schleswig-Holstein  to  Britain  and  conquered  it. —  L.  Anglus,  pi.  Angli,  of  Teut.  origin.  Cp.  OE. Angle,  Engle,  prop,  ‘the  people  coming  from Angul  ( =  ON.  Ongull),  ‘a  hookshaped  district in  Schleswig’,  fr.  angul  (=  ON.  ongull),  ‘fish¬ hook,  angle’,  which  is  rel.  to  anga,  OHG.  ango, ‘hook’.  See  angle,  ‘fishhook’,  and  angle,  ‘comer’, and  cp.  English,  Anglican,  Anglo-Saxon, anglesite,  n.,  a  mineral  containing  lead  sulfate.  — Coined  by  the  French  mineralogist  and  physi¬ cist  Francois  Sulpice  Beudant  in  1832;  so  called by  him  in  allusion  to  the  fact  that  it  was  dis¬ covered  by  Withering  in  Anglesey  (in  1783). For  the  ending  see  subst.  suff.  -ite.
Anglican,  adj.  and  n.  —  ML.  Anglicanus,  fr.  An- glicus,  ‘English’,  fr.  Late  L.  Anglus.  See  Angle and  -an.
=== KLN anxious
3028:anxiety,  n.  —  L.  anxietas,  gen.  -at is,  ‘anguish, anxiety’,  fr.  anxius.  See  next  word  and  -ity. anxious,  adj.  —  L.  anxius,  ‘solicitous,  uneasy’,  fr.
```


## [2026-09-04T22:50:30.554Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3780,3800p' LAT.txt; echo \"=== anguis\"; sed -n '3826,3860p' LAT.txt; echo; grep -n \"anguis\" LAT.txt | head",
 "description": "Ernout-Meillet ango/anguis"
}
```


### [2026-09-04T22:50:30.651Z] TOOL RESULT

```
anglstrw, -I n.: instrument de chirurgie (isid.). Emprunt a ayxi-
CTTpov, rapprochi par 1 'etymologie populaire de ango.
ango, -Is, -xl, anctum, -ere: etreindre, oppresser, serrer (la gor-
ge); Ov. M.9,78, angebar, ceu guttura forcipe pressus. Atteste atoutes
les ipoques; mais anxi et anctus ne figurent que dans les grammairiens.
M.L.4g8b. - Ango se dit du physique et du moral; ce meme double sens
se retrouve dans les substantifs derivis: angor, -oris (m.) rare au
sens de "angine" 3'emploie plutot de 1'oppression morale, de 1'angoisse:
angor est aegritudo premens, Cic.Tu.4,18; le sens physique est reserve
k angina , sans doute fiminin substantivi d'un adj. *anginus, "genus
morbi, eo quod angat, et Graece synanche appellatur" Non.35. L'hypo-
thfese d'un emprunt au gr. afyo\ir\ ne rend pas compte de la forme, et se
heurte k la difference de sens, ay^ovT) signifiant "strangulation"; du
reste, comme on le voit par Nonius, le correspondant grec de angina
c'est cruvaYXtl. L’i de angina est bref, cf. Lucii .864; Ser .Samm.378;59
anguis
c’est a tort que Quicherat a angina . Un adj. *angus (cf. angiportus) n'a
pas subsiste et a ete remplace par:
angustus: etroit,serre; peut-etre d'un thfeme en -s-, cf. onus/onus tus ;
robustus, augustus, uetus/uetustus? D'ou angustia, employe surtout au
pl. angustiae au sens de "d^file" (cf. fauces ), puis au sens moral "gene",
=== anguis
angobatae: sorte. d'automate. Se trouve dans Vltruve 10,7,4. Peut-
etre transcription d'un mot grec non atteste. Cf. toutefois andabata.
anguis, -ls n.(et f. i l'6p.arch.; anguen, - inis n. dans Jul.Val.
anguena f.gloss.): serpent. Mot ancien, amploye dans la 1 . religieuse;
cf.Thes. II S3,49sqq.Apour substituts des adjectifs: serpens (bestiaJ,
uipera, sans doute aussi coluber, colubra ; ou 1’emprunt au gr. draco.
Po^tique; rare en prose (T.L.); un ex. dans Columelle; 40 ex. contre
360 de serpens dans Pline; cf. Thes. II 51,76. Caton et Varron 1 'ignorent
tout en employant anguinus. N'a survecu que dans quelques dialectes
italiens, cf. M.L.463.
Derives: anguiculus m. (Cic.); anguinus (ancien); angueus (Sol.).‘Com¬
posta po6tiques: anguifdr (= ocpi.ou)(OC); -ger; -gena; -nanus, -pes. S'y
rattache sans doute: anguilla (anguila) f.: anguille; M.L.461, dont
la loi Sal. a un adj.derive anguilldricius.
Mot de date indo-europeenne, mais dont les formes ont ete varices
intentionnellement, comme on le voit par les substitutions telles que
serpens on uipera (cf. aussi lupus, aper). La forme anguis est super-
posable 1 v. pruss. ang is "serpent (non venimeux)", lit. angis (acc. angi)
"serpent (venimeux)", pol. waz (gen.wgza); une forme visiblement deviee,
anxdris, designe en vieux prussien le "serpent venimeux". Le traiteraent
g, en face de lat. gu, dans iri. esc-ung "anguille" gen. escongan (litt.
"serpent d^au") en face de lat. anguis indiquerait 1 'aspiree. Mais le
grec offre lesb. l| i( 3 ijp iC * ey^eXuc. MtiOuiivouol Hes., a cote de ext-S,
ocpi,C, eyxeXuC et de a( 3 e(.£* e^ei-S Hes. L'indo-iranien a skr. ahih, a v.angulus
60
azis "serpent", dont 1 1 a est ambigu. L' i de arm. iz (gen. izi) ne peut
guere reposer que sur *e. On ne peut donc restituer un original indo-
europeen. Le flottement |>o:rte sur 1' initiale : e-, o-, an-, et
sur les consonnes *g w , *g h, *gh, les formes de plusieurs langues etant
du reste ambigues. “ La designation de "1'anguille" par un deriv^,
anguilla, de anguis, a son pendant dans v. pruss. angurgis , lit. ungurys,
pol. wegorz, russe ligor', etc.
angulus, -i (anglus dans l'app. Probi) m.: eoin [d'un edifice], angle
(yuwux). — Ancien, technique, usuel. M.L.465. Britt . ong l.
Deriv 4 s: angellus: petit coin, petit angle; angularis (lapisj ; angu¬

3795:anguis
3828:anguis, -ls n.(et f. i l'6p.arch.; anguen, - inis n. dans Jul.Val.
3842:serpens on uipera (cf. aussi lupus, aper). La forme anguis est super-
3847:"serpent d^au") en face de lat. anguis indiquerait 1 'aspiree. Mais le
3856:anguilla, de anguis, a son pendant dans v. pruss. angurgis , lit. ungurys,
5516:se en a fait un aasculin, d'aprbs anguis, draco. M.L.711; irL asf.
5570:p.8 et 36. - Le latin a un non inexpliqu6 de genre ania£, sanguis, ofc
7826:99,1; de IA Gloss. Plac. 8 , 8 , bubinarium n.: sanguis qui mulieribus
14766:r^pandu ou coaguli, flaque de sang", par opposition a sanguis "sang
14769:sanguis/emicat exultans alte spargitque cruorem, etc. Atteste a partir
```


## [2026-09-04T22:50:32.892Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON adena niyaz\"; grep -n \"نیاز\\b\" incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -5; echo \"=== MON_part2\"; grep -n \"نیاز\" MON_part2.txt | head -5; echo \"=== ARY latin index\"; grep -n -i \"NIYAZ\\|ANGH\\|AZDAHA\\|AZHDAHA\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Mo'in and Aryanpur greps"
}
```


### [2026-09-04T22:50:32.970Z] TOOL RESULT

```
=== MON adena niyaz
489:غانی: 0 [ع.] (ص.) بسی‌نیاز. توانگر» 
493:که به سیب حسن خویش بی‌نیاز از زیور 
495:شوهر خود بی‌نیاز باشد. زن جوان پا کدامن با 
4414:بدون نیاز به قصد زایدی بر علم (ایضا). 
4533:فاقه: ()«« (ع. فاقة| (۰.) نیازمندی. فقر 
=== MON_part2
489:غانی: 0 [ع.] (ص.) بسی‌نیاز. توانگر» 
493:که به سیب حسن خویش بی‌نیاز از زیور 
495:شوهر خود بی‌نیاز باشد. زن جوان پا کدامن با 
4414:بدون نیاز به قصد زایدی بر علم (ایضا). 
4533:فاقه: ()«« (ع. فاقة| (۰.) نیازمندی. فقر 
=== ARY latin index
1118:~ thay bangh J A lee thy col od Gace cdl ph 3 4 el gh
2320:OLD HIGH GERMAN) pS gst AZDAHAG, AZ (PAHLAVI) 5 ly
3267:BORST (DUTCH) sola VARANGH, VARAH
3907:“"* VESELU VAHYA, VANGHA
10379:9 ett Rada 4 eels slangh y ws efit
```


## [2026-09-04T22:50:43.821Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && awk 'NR<=2320 && /pdf page/{p=$0} NR==2320{print p}' ARY_latin_index_pages.txt; sed -n '2314,2326p' ARY_latin_index_pages.txt; echo \"=== ARY_pages grep\"; grep -n \"اژدها\\|نیاز\" ARY_pages.txt | head -10",
 "description": "Aryanpur index and pages"
}
```


### [2026-09-04T22:50:46.138Z] TOOL RESULT

```
[pdf page 82]
MACKENZIE: (FROM) 115 SECUS LATIN) og3¥ i
yr igbb oh, SEC, SECEN (LATVIAN) (35) ig) |
SECH HOLD IRISH) Ssh p! |
|
‘OPHIS AZHI-DAHAKA, —(AVESTAN) play! |
ANGUIS (LATIN) 3 AZHI '
OLD HIGH GERMAN) pS gst AZDAHAG, AZ (PAHLAVI) 5 ly
IcIL AML, SANSKRIT) ey Saile
IGEL (GERMAN) glT IZH, AUS ARMENIAN) ga)
IGIL HOLD ENGLISH) oS g3S\ EKHIS, ECHINOS, — (GREEK) by
[pdf page 83]
el | oat
‘REFERENCES beth (OLD CHURCH SLAVIC) oS 53%)
=== ARY_pages grep
341:این پرسش منطقی نیاز به جواب دارد: کاوش‌های باستانشناسی و واژگان غیر هند و اروپایی
1049:خدایان بود. او نیاز انسان‌ها را (همراه با نیایش و قربانی) به خدایان اظهار می‌کرد و آنان در مقابل
1200:بی‌نیاز می‌کند.
1617:معنی این واژه در یونانی؛ نیاز» مشقت.
```


## [2026-09-04T22:50:55.482Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"دهاک\\|دهاك\\|اژد\\|آنگ\\|انگوئیس\\|ophis\\|OPHIS\\|Ophis\" ARY_pages.txt | head -20",
 "description": "ARY main text search"
}
```


### [2026-09-04T22:50:55.534Z] TOOL RESULT

```
1183:از دیرپاز آغاز شده است. مثلاً در زبان انگلیسی صدهاکتاب و مقاله و واژه‌نامه در این باره متتشر شده
1272:واژه‌های همریشه همه دارای معنی همسانی بودند آنگاه می‌توانستیم با اطمینان پیشتر ننیجه بگبریم؟ و
1838:واژه‌ی آنگلیسی 3۸7 یعنی "خوردن" و واژه‌ی هنبت 131811 یعنی "می‌خورم"). ای ای هو
1897:این واژه با واژه‌های آنگاه" و "چشم " همریشه است. بازگشت به؛ نگاه. :
3736:اوستایی (487۸4): ۷۸۸ آنگلیسی کهن (0ل8ال2(/0 ۰:0۵ ,۷/۸۲۸۷
5227:چم آنگلیسی سرواژه‌ی فارسی: 10000
6054:آنگلیسی کهن (4ق3ل8(/02 صان): 1 (۸818) ,128 (۳0788 ,۵6 وهی
7678:9 0۸ آنگلیسی (6(701/827) از لانین) ۳
8938:آنگلیسی کهن (8(/0134 ضا0): رال۸ 1.800 6 ملفاطقلا ,05859
10683:آنگلیسی رس 11007
13358:۲ چم این واژه در هلندی: پر حرفی کردن (جالب این است که در برهان قاطع : نیز [صفحه‌ی ۱۸۷۹] واژدی "۹"
13509:اففانی (پشتو) (/۸۳0/7۸۷): آنگلیسی (7ل5لا8(/0): 15
13747:آنگلیسی کهن (80لا80/0 ۰:00 1408۸ 6 (7۷8) دا هد وا
15988:بلرچی (8۸/6/1): 041 | پسگشت‌ها آنگ ره اد دی
```


## [2026-09-04T22:51:03.066Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/anger",
 "prompt": "Give the full etymology entries for anger (and any linked note on the PIE root *angh-), including Old Norse angr, and the related words anguish/anxious if shown."
}
```


## [2026-09-04T22:51:03.549Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/anguish",
 "prompt": "Give the full etymology for anguish (Old French angoisse, Latin angustia, angere) and any statement of the PIE root."
}
```


### [2026-09-04T22:51:10.775Z] TOOL RESULT

```
# Etymology of Anger

## Anger (Verb)
From c. 1200, meaning "to irritate, annoy, provoke." The word derives from Old Norse *angra* "to grieve, vex, distress," tracing back to Proto-Germanic *\*angaz* and ultimately the Proto-Indo-European root *\*angh-* meaning "tight, painfully constricted, painful." By the late 14th century, the meaning evolved to "excite to wrath, make angry."

## Anger (Noun)
Dating to mid-13th century, initially denoting "hostile attitude, ill will, surliness" and also "distress, suffering; anguish, agony" (now obsolete). It comes from Old Norse *angr* "distress, grief, sorrow, affliction." The sense of "rage, wrath" appeared by the early 14th century. As one source notes, "the expression was transferred to the feelings of resentment naturally aroused in the mind of the person aggrieved" from an original sense of oppression or injury.

## Related Terms
- **Anguish**: Connected through the shared PIE root *\*angh-*
- **Anxious**: Also derived from *\*angh-*, meaning "tight, painfully constricted, painful"
- **Angst**: From German *Angst*, borrowed into English psychology (1944), cognate with anger

The root *\*angh-* appears across Indo-European languages, consistently expressing notions of tightness, constriction, and pain.
```


### [2026-09-04T22:51:10.927Z] TOOL RESULT

```
# Etymology of Anguish

**Old French Origin:**
"From Old French _anguisse, angoisse_ 'choking sensation, distress, anxiety, rage' (12c.)"

**Latin Development:**
The Old French term derived from Latin _angustia_ (plural _angustiae_), meaning "tightness, straitness, narrowness" and figuratively "distress, difficulty." This came from the Latin verb _ang(u)ere_, meaning "to throttle, torment."

**Proto-Indo-European Root:**
The ultimate source is the PIE root *angh-, defined as "tight, painfully constricted, painful." This root also underlies related words like anger, angina, anxiety, and angst, all sharing the core sense of constriction and discomfort.

The semantic evolution traces from physical tightness and choking sensations to psychological states of suffering and distress, reflecting how bodily experiences become metaphors for mental anguish.
```


## [2026-09-04T22:51:16.338Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D9%86%DB%8C%D8%A7%D8%B2",
 "prompt": "Show the Mo'in (فرهنگ معین) dictionary entry for نیاز — including the bracketed origin tag (e.g. [په.] Pahlavi) and all senses."
}
```


## [2026-09-04T22:51:17.985Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%A7%DA%98%D8%AF%D9%87%D8%A7",
 "prompt": "Show the Mo'in (فرهنگ معین) dictionary entry for اژدها — origin tag and senses. Also anything for اژدر."
}
```


### [2026-09-04T22:51:20.814Z] TOOL RESULT

```
# Mo'in Dictionary Entry for نیاز (Niyāz)

**Origin:** [په.] (Pahlavi)

**Part of Speech:** (اِ.) - Noun

**Senses:**

1. "حاجت ، احتیاج" — necessity or requirement; something one lacks and requires

2. "نذری که برای گرفتن مراد و حاجت به کسی یا جایی بدهند" — a votive offering made to fulfill a wish or obtain a need through appeal to someone or at a particular place
```


### [2026-09-04T22:51:23.682Z] TOOL RESULT

```
# Mo'in Dictionary Entry

## اژدها (Azhda)

**Origin Tag:** (اَ دَ) [اَوِس] (امر.)

**Definition:** The entry notes that اژدها is a variant of اژدرها. It refers to "a mythical serpent with a large body that has strong wings and talons, and fire emanates from its mouth."

## اژدر (Azhdar)

The dictionary identifies اژدر as the root form, defining it identically to اژدها—a legendary dragon-like creature with powerful wings, claws, and fire-breathing capabilities.

Both terms represent the Persian mythological concept of a dragon, drawing from ancient Zoroastrian and broader Indo-Iranian legendary traditions.
```


## [2026-09-04T22:51:28.574Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/indoeurop.html",
 "prompt": "Find and quote the entries for the roots \"angh-\" and \"angwhi-\" (or angʷhi-) exactly as given, including their glosses and English derivatives and Pokorny page references."
}
```


### [2026-09-04T22:51:36.353Z] TOOL RESULT

```
# Indo-European Roots: "angh-" and "angwhi-"

## angh-

The entry for **angh-** is present in the document:

> "Tight, painfully constricted, painful. Oldest form _\*ang̑h‑_, becoming _\*angh‑_ in centum languages. Derivatives include [anger](/word/search.html?q=anger), [hangnail](/word/search.html?q=hangnail), and [quinsy.](/word/search.html?q=quinsy.)"

The Pokorny reference is: **\[Pokorny _ang̑h‑_ 42.\]**

## angwhi-

I cannot locate an entry for "angwhi-" or "angʷhi-" in the provided document. The web page content includes entries from **ad-** through **bheudh-**, but no entry for this root appears in that range.
```


## [2026-09-04T22:51:46.887Z] TOOL CALL #65: Bash

```json
{
 "command": "ls data/extracted/ ; find . -maxdepth 3 -iname \"*.pdf\" 2>/dev/null | head; cat tools/ref_page.py | head -40",
 "description": "Look for book PDF"
}
```


### [2026-09-04T22:51:46.954Z] TOOL RESULT

```
batch
NEXT_CHUNK
RETRY.txt
test
./EtymologicalDictionary-persian-english.pdf
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


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
```


## [2026-09-04T22:51:52.333Z] TOOL CALL #66: Bash

```json
{
 "command": "D=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && (pdftoppm -f 57 -l 57 -r 200 -png EtymologicalDictionary-persian-english.pdf $D/p57 2>&1 | head); ls -la $D/p57*",
 "description": "Render PDF page 57"
}
```


### [2026-09-04T22:51:54.820Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 67151 Sep  4 18:51 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p57-057.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1 Sep  4 16:01 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p57.txt
```


## [2026-09-04T22:51:57.241Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p57-057.png"
}
```


### [2026-09-04T22:51:57.578Z] TOOL RESULT

```

```


## [2026-09-04T22:51:57.576Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-04T22:52:20.330Z] TOOL CALL #68: WebSearch

```json
{
 "query": "Persian niyāz \"need\" etymology Avestan ni-āz Cheung *Haz Middle Persian nyʾc"
}
```


## [2026-09-04T22:52:22.312Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7%D8%B2%D9%85%D9%86%D8%AF",
 "prompt": "Etymology of نیازمند — does it give a Middle Persian niyāz and any deeper etymology?"
}
```


### [2026-09-04T22:52:22.325Z] TOOL RESULT

```
Web search results for query: "Persian niyāz "need" etymology Avestan ni-āz Cheung *Haz Middle Persian nyʾc"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T22:52:27.769Z] TOOL RESULT

```
# Etymology of نیازمند

Based on the Wiktionary content provided, the etymology is straightforward but limited in depth:

The word نیازمند comes from **"نِیازْ (niyâz, 'need') +‎ ـمند (mand)"** according to the entry. This shows it's a compound formed from the Persian noun "niyâz" (need) combined with the suffix "-mand."

However, the page does not provide deeper etymological information tracing "niyâz" back to Middle Persian or earlier origins. The entry focuses only on the immediate Persian morphological composition rather than investigating the proto-linguistic roots of the word "need" itself.

To discover whether "niyâz" derives from Middle Persian or has further etymological ancestry, you would need to consult more comprehensive etymological resources or the separate Wiktionary entry for نیاز (niyâz).
```


## [2026-09-04T22:52:43.351Z] TOOL CALL #70: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7%D8%B2|page 57, root Angh, Persian niyaz etymology\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82en%C7%B5%CA%B0-|page 57, root Angh, PIE root reconstruction and descendants\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%DA%98%D8%AF%D9%87%D8%A7|page 57, root Angwhi, Persian azhdaha < MP azdahag < Av. azi-dahaka\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81%C3%B3g%CA%B7%CA%B0is|page 57, root Angwhi, PIE snake root and Avestan azi\" \\\n \"https://www.etymonline.com/word/anger|page 57, root Angh, English anger < ON angr < PIE *angh-\" \\\n \"https://www.etymonline.com/word/anguish|page 57, root Angh, English anguish < OF angoisse < L angustia\" \\\n \"https://vajehyab.com/moein/%D9%86%DB%8C%D8%A7%D8%B2|page 57, root Angh, Mo'in entry for niyaz tagged Pahlavi\" \\\n \"https://vajehyab.com/moein/%D8%A7%DA%98%D8%AF%D9%87%D8%A7|page 57, root Angwhi, Mo'in entry for azhdaha tagged Avestan\" \\\n \"https://ahdictionary.com/word/indoeurop.html|page 57, both roots, AHD Indo-European roots appendix angh-\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7%D8%B2%D9%85%D9%86%D8%AF|page 57, root Angh, niyazmand = niyaz + -mand\" \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-04T22:52:48.282Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0097c36e54f76601.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2bf8785b7aaf20b2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d4227a1ad79eca32.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/09bb3ac136f9ff2d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d2ea84e3d3f2982d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e3d34fc875007895.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0ad446a3da7dfdd6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cdf63c5e3a86ea3e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/24cd7948c66bfb96.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/84656b61666ec396.txt
```


## [2026-09-04T22:52:51.396Z] TOOL CALL #71: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-04T22:52:51.434Z] TOOL RESULT

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


## [2026-09-04T22:54:01.171Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WEB anguine\"; grep -n -i \"anguine\" WEB_vol1.txt | head -3; echo \"=== FSD anguine\"; grep -n -i \"anguine\" FSD_vol1.txt | head -3; echo \"=== HUB azdaha\"; grep -n -i \"aždah\\|azdah\\|ajdah\\|dahâk\\|dahak\" HUB.txt HRN.txt | head -8; echo \"=== NYB nyʾc\"; grep -n \"ny’c\\|nyʾc\\|niyāz\\|niyaz\" NYB_vol2_glossary.txt NYB_vol1.txt | head -5",
 "description": "Webster/F&W anguine, Hübschmann azhdaha, Nyberg niyaz"
}
```


### [2026-09-04T22:54:01.306Z] TOOL RESULT

```
=== WEB anguine
7749:an-guin’é-Al, a. anguineous.
7750:an-guin’é-ous, a. [L. anguineus, from anguis, a snake.] resembling a snake.
40694:con-san/guine (-gwin), a. consanguineous.
=== FSD anguine
8729:cal  affections  of  matter.  D.  Stewart.  marriage:  contrasted  with  consanguine.  2.  Zool,  Hav-
44483:of  blood.—  b. *dlsk,  n.  A   red  blood-corpuscle.  —   blood'- drop",  n.  A   red  terebellold  marine  worm,  especially  Poly- cirrns  eximius  and  Enoplobranchus  sanguineus,  contractile Into  a   blood-like  Bpot,  living  on  muddy  bottoms  and  often on  and  under  oysters.— b. *dust,  n.  Anat.  Microscopic dumb-bell-shaped  bodies  found  In  the  blood-plasma,  whose function  Is  not  known,  but  which  do  not  possess  true  ame- boid motion.  b.'mote}.— b.*eagle,  n.  Horse  Hut.  Tbe cutting  away  of  the  ribs  from  the  spine  and  tearing  the  lungs, liver,  etc.,  out  of  an  enemy’s  body.  Tennyson  The  Dead Prophet  st.  18.—  blood'ed,  a.  1.  Having  blood  of  a   speci- fied character;  as,  fishes  are  cold  •blooded.  2.  Of  a   specified temperament,  character,  or  temper;  as,  hot •blooded  youth;  a cold-blooded  murder.  3.  Having  pure  blood  or  lineage; thoroughbred;  as,  blooded  cattle  —   blood'er,  n.  [Rare.]  A bloodletter.—  b.'feud,  n.  A   feud  between  families  or  clans arising  from  a   violent  crime,  usually  murder  or  a   crime  in- volving dishonor.—  b. 'finch,  n.  A   spermestlne  seed-eating bird  (genus  Lagonosllaa )   having  deep  crimson  as  the  pre- vailing color;  a   Senegal.— b.'flne,  n.  A   fine  anciently paid  by  a   murderer;  blood-wite. —   blood  now"er,  n.  1, Any  red-flowering  plant  of  the  genus  Hzmamhus,  of  the amaryllis  family  (AmarylUdaccx) .   2.  An  ornamental
44502:1.  Any  hiemodoraceous  plant.  2.  The  salad  burnet.  3. The  lesser  centaury.  4.  The  red- veined  dock  ( Rumex sanguineus ).  5.  Bloodroot.—  blue  b.,  blood  of  a   supposed finer  or  purer  kind;  hence,  aristocratic  lineage,  character,  or bearing.— corruption  of  b.  (Late),  an  Immediate  conse- quence of  a   judgment  of  attainder  (in  England)  whereby  the guilty  person  can  neither  receive  nor  transmit  property by  inheritance:  abolished  (except  for  outlawry)  In  1870.
=== HUB azdaha
HUB.txt:5354:*to consecreate, worship', yazesn Vorship', yazdahum *der elfte*
HUB.txt:5356:yak, yax, yazdahum (mit ya- aus e-, s. § 30) und ya- (neben i
HUB.txt:5828:'Eanal, R5hre' H. 1024; nuvazdah neunzehn H. 1048, navad
HUB.txt:5835:Ebenso im Armenischen : Artavazd - zd. asavazdah-^
HUB.txt:7020:Hormizd = ap. a(h)uramazda; azdahd *Drache* = arm.
HUB.txt:7021:aMahak, zd. azis dahako, u. s. w. In alien diesen Fallen
HUB.txt:7620:= zd. x^'aiihar- ; aMaha Drache' = zd. am dahako ; bih gut,
HUB.txt:7969:tnazd; arm. Artavazd = zd. Asavazdah-, gr. '^praovdadrjg
=== NYB nyʾc
```


## [2026-09-04T22:54:12.821Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7015,7025p' HUB.txt; echo \"-----\"; sed -n '7615,7625p' HUB.txt; echo \"=== HRN azhdaha\"; grep -n -i \"aždahā\\|azdaha\\|Drache\" HRN.txt | head -8",
 "description": "Hübschmann context and Horn Drache"
}
```


### [2026-09-04T22:54:12.898Z] TOOL RESULT

```
dami ; landa 'Sklave' = ap. bandaka- ; andam *K5rper, Glied'
= zd. handcLma-^ u. s. w. ; duzd *Dieb' = zd. duzd& *Bose-
wicht*; muzd, muzd *Lohn, Preis' = zd. mlzda, ksl. mtzda,
skr. mtdha'\ miyazd 'Gelage* = zd. myazda-, skr. miyedha-;
nazd *nahe = zd. nazda-, skr. comp. nediyas-] sassanid.
Hormizd = ap. a(h)uramazda; azdahd *Drache* = arm.
aMahak, zd. azis dahako, u. s. w. In alien diesen Fallen
stand im Ap. der Verschlusslaut d.
§ 92. Ap. d hatte nach Vokalen die Geltung als
Spirans J und wurde im Paz. und Np. zu h oder y = i.
a) zu A: diham gebe* = zd. dadqmi^^di^. ipt. dadatuv
-----
Hagmatdna- ') ; Hind = ap. Hindu- Indien ; Hindu Inder
= phi. Hinduk^ arm. Hndik-K Indien', Hnduk Inder Mos.
Kalank. I, 257, u. s. w.
b) im Inlaut: ddh *Sklave = skr. dasa-; mah Mond,
Monat* = ap. mdha-^ skr. mas-, mOsa- ; x^ahar *Schwester
= zd. x^'aiihar- ; aMaha Drache' = zd. am dahako ; bih gut,
besser = Siip.Vahyaz- (data^), arm. veh, skr. vasu-; bahd 'Werth,
skr. vasna- 'Kaufpreis ; bahor Triihling , ap. [&ura')vahara'?,
skr. vasanta-; bahana 'Vorwand', skr. vasana- *Qewand';
bahist, bihist 'Paradies* = zd. vahista-; dih *Dorf\ arm. deh,
ap. dahyth; phi. N(a)rs(e)hz = arm. Narseh, zd. nairydsatlha-.
=== HRN azhdaha
1106:76. ezdehä 'Drache'.
1107:aw. azis dahakö; phlv. aze dahäk, arm. LW. azdahak.
1108:arm. azdahak beweist, dass im Mittelpersischen az-,
```


## [2026-09-04T22:54:23.509Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6320,6340p' HUB.txt; echo \"=== HRN grep niyaz/Mangel/Bedürfnis\"; grep -n -i \"Bedürfnis\\|Bediirfnis\\|niaz\" HRN.txt | head -8; echo \"=== HRN line 3980-3990\"; sed -n '3978,3990p' HRN.txt",
 "description": "Hübschmann apeniaz context, Horn niaz"
}
```


### [2026-09-04T22:54:23.577Z] TOOL RESULT

```
AbarSahr (NSldeke, Alexanderroman 15, s. oben § 22);
Aprvez bei Sebeos = paz. awarvS^, phi. aparvBj Shk.
233, np. Parvez [im "^BarvEz), siehe § 69; Aprsam (Elise)
= np. Abarsdm (Tab. 9); Atrpatakan = np. A^arbaigan
neben AdarbaSegan JKAS. 1894, 440, zu zd. atarepata-^ gr.
'ArQondvrjg'^ Sapuh ^= phi. S(a)hpi(hr, np. Sdpur; Pap =
phi. P(S/? ZDMG. 44, 658 ; apastan Tertrauen' s= phi. apastan;
aparanfan 'Arrnband* = np. abranjan ^), dasUbaranJan ; apa-
ranU *Haus, Palast', ap. apadana-; aparfan-Er Var hoch-
miithig (EliSe p. 12), np. bartan, psiz. awartam'Rochmuth;
apeniaz 'bediirfnisslos' = np. be-niyaz; apsparem *ich iiber-
gebe, vertraue an', np. siparam, paz. awasparam^ phi. ap-
-spar am Shk. 233, PPGl. 78, u. s. w. in zahlreichen Fallen.
Eine Ausnahme bildet nur bob (Sebeos p. 64), das
wohl Teppich* bedeutet und = phi. bop 61. and Ind. 82,
bal. b6p *Matratze, Kissen* ist. Es ist erst bei Sebeos
(7. Jhd.) bezeugt und also jiingeres Lehnwort. Bei Thavrez
(Faustusv. Byz.) = np. Tabriz (Stadt in Persien) ist zu
beachten, dass diese Stadt wohl erst zur Sassanidenzeit ge-
griindet oder namhaft wurde, den Armeniern also erst unter
der sassanidischen Namensform Tatcrez (— phi. '^TaprBd?)
=== HRN grep niyaz/Mangel/Bedürfnis
1956:^\fy^ bäg-ed; vergl. ender wm 'Bedürfniss'^).
2170:g. niaz. varak; gel. velg, valk; Käö. valg^ velg\ (vergl.
2525:be (ZPGl.), vergl. arm. LW. ape]niaz,
7923:wohl bei AM. 237 Zeile 6: 'Also ist das Bedürfniss
10074:Im Neupersischen soll endervä {endenväl 'Bedürfniss*
=== HRN line 3980-3990
SiW.yava- *6etreide'; phlv. jav bezw. yav; ai. yäva-.
knrd, je, jau, yö (H.-Sch.); oss. yau, yäu, yeu *Hirse'
(147); bei. /ö, jav, n. jau 'Gei-ste' (179); si/n. yavoj,
sar. yaugjy yögj, 'MehY (aus ^yavaka^).
429. Jevän, juvän 'Jüngling .
niäz. javän.
aw. ytivan- {yvan-) 'Jüngling; phlv. yuvän (päz.
falsch jüdän)^), arm. LW. yavanak, yovanak 'Junges
eines Vierfüsslers'; ai. yüvan-,
LW. kurd. juvän; afy. javän; bei. javan (111).
430. jösTden *koehen, sieden, jös{pere), jösäk, jösänldtn,
Ka§. vöyösnaä, böyösad (Qohrüd).
ai. yüs-, yüsdn- 'Brühe*.
```


## [2026-09-04T22:54:35.163Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2518,2532p' HRN.txt; echo \"=== HRN 1100-1115 (no.76)\"; sed -n '1100,1115p' HRN.txt",
 "description": "Horn be- entry and no.76"
}
```


### [2026-09-04T22:54:35.254Z] TOOL RESULT

```
246. bihiSt^ behist ^Paradies'.
(äw, mhista- 'bester; phlv. vahist; ai. väsistha-.
LW. kurd. behist.
Die Aussprache behist ist die ursprüngliche ; in bihist
ist der erste Vokal dem zweiten angeglichen.
247. be, ehe 'ohne'.
phlv. ape- (päz. atve-)^ z. B. ape'\htm, ape]vnäs etc.,
be (ZPGl.), vergl. arm. LW. ape]niaz,
kurd. af/. bei. LW. bt- resp. he-.
*) Fr. Müller, WZKM. 5, 186, Anm. vergleicht aw. vahhana'
*Kleid\ was ganz unwahrscheinlich iat.- 57 ~
Eine über das Pehlevi hinausgehende iranische Form
kommt nicht vor ; ape resp. ii12 stehen im PehlevT für
die verschiedensten Praepositionen des Awestatextes,
z. B. für vi {vi)y para^ paiti u. a. m.
=== HRN 1100-1115 (no.76)
ap. hacä; aw. haca; phlv. aj; ai. sdca,
kurd. az, ze, z-; af/. ;'-; bei. a(f, as (1); wa/.,
sar. z- etc.
1) Vgl. Bartholomae, BB. 10, 274.
*) Vergl. aber Bartholomae, Ar. Forsch. I, 119.
^) Bedeutungsübergang etwa: finster — höllisch ~ zornig.- 19 --
76. ezdehä 'Drache'.
aw. azis dahakö; phlv. aze dahäk, arm. LW. azdahak.
arm. azdahak beweist, dass im Mittelpersischen az-,
nicht a/- gesprochen wurde; in jüd.-pers. xmiX ist z
nur ausnahmsweise durch i bezeichnet, während es
sonst durch T ausgedrückt wird *).
aw. azi' 'Schlange'; phlv. az; ai. ähU; arm. ?i'^);
minj. yiz selbst ist sonst im Np. verloren gegangen.
77. esp, esb 'Pferd'.
ap. Aspa[cana-, uv]aspa- fschöne Pferde habend');
```


## [2026-09-04T22:56:10.707Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dahāka\\|dahaka\\|dahäka\\|dahāk\\|aži\\b\" BRT.txt | head -10; echo \"---\"; grep -n \"azi-\\s*m\\.\\|'Schlange'\" BRT.txt | head -10",
 "description": "Bartholomae azi entry"
}
```


### [2026-09-04T22:56:10.796Z] TOOL RESULT

```
6543:1 '3- 47;  49-  «)  sonst  m\K  dahaka-:  'iis
6544:•  j.''as.vandara-')Adj.  dem  reichlich  Lob  ^  ^„-^^yif  daAäks  (Stverz.)  Yti-zg;  usw. gespendet     wird,     vielgepriesen':     uyr?m<     KompA.  —  ai.  ähay-  m.,  mp.  of;  s.  noch  zu kavalTH  ^ar^nJ  .  .  'r^m  Yt.  ig.  9;  45.  1      dahäka-.  —  Pü. :  ai,  erl,:  mär.  —  »  Fü.  (ügt
13059:■  j.  'dahaka-  m.  Bezeichnung  d^A/ischer Geschöpfe:  äal  ahmt  runäne  tayänU  °ksca mürakäca  (sd.)  peurvjar^  varsnäca  Y. II.  d.
13061:m  j.  'dahaka-  Adj.  -?-:  *&>(NS.)  nqma aAmi  Yt  75. 45  (  Vayav  spricht).
13063:•  j.  dahäka*  m.  EN.  eines  sagenhaften i/iMTÖschen  Königs  von  Iran*';  stets  mit aiay-  m.  (sd):  aus  ^risa/a  °ks  bamröis paiti  daitihaove  Ytj.  29;  —  aus  %ritafh 'kö  upa  kvirintim  tüisii^m  Yt/J.  19;  — "hraäaonS  yB  jaitat  aiim  'kjm  'irhafan»m %riJtamfr^6»M  xsias'astm  hatatjrS.yaoxi- flM..dalvlM  *drufim  ..yqm  as.aojasttmqwt *drujim  fraca  kmntai  attrS  mainyui  Y.  p- 8;^ —  '^raSaotß  jania  aisis  'käiV.i.XT, Yt7p.92;  —  aarö  matnyus  aittm  fratfhan- eayat  .  .  aiimca  'k^m  Yt  ig.  46 ;  —  aie 'hritafim  'ka'^l.ig.^Q; — haxoffrayaaxstyö baväki  yaia  aiSii  °kai  ayaJaina  Az.j.
13065:kt. '>  und  Bed.  ?  VgL  'dahaka-, —  np.  lüdalä 'Drache'.  —  1)  Unrichtig  Dsr.  ZA.  /.  86-
---
6536:Vfil.  aiakva-.  —  Pü. :  fehlt. •  j.  azay-  m.  i)  'Schlange',  ein  ^ÄiÄisches Tier:  /<fiws.tara  ya^a  'zayS  xsvoewanhs V.iS.ßs;  —  'Sinam  udarS.>rasanam  .  . °iinam  spakanqm  kahrpunanam  (sd.)  V. 14.%.  a)  Sing,  in  koll.  Sinn:  äat  ahe paityänm  .  .  'zimca  yim  raoioibtn  (sd.) zj'rtM/a..V./.2''; — yai3  '%wä  niHt  aiwi,- Jruzilnti  •iisea  arütuiisca  "damit  dir kein  Arg  antun  können  Schlangen  und  .." YL5, 90.  2)  schlangenähnlichcs  Untier 'Drache,  Ungeheuer'":  'zdis  sairitaAe simahe  vlsS.valpahe  Y.().3o;  —  'zis .  . gäuitava . .  vTraja  Aog.  ~S;  —  'leis  vJlspahe N.  48;  —  ktrasäsps  .  .  yS  jartat  °ilm (sd.)  yim  aspB.garpm  mnganm  ..
```


## [2026-09-04T23:01:25.366Z] TOOL CALL #77: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-57.json",
 "content": "{\n  \"pdf_page\": 57,\n  \"book_page\": 27,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Angh\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂enǵʰ- 'to constrict, tighten; narrow, painfully constricted' (Pokorny angh- 42–43; Watkins/AHD angh- 'tight, painfully constricted, painful')\",\n      \"note\": \"Root form, language label and gloss are all right. Pokorny IEW 42–43 heads the entry 'angh- (kelt. auch engh-) ‚eng, einengen, schnüren‘, z. T. auch von seelischer Beklemmung, Angst' and lists exactly the branches Nourai draws (Avestan verbal forms, Latin ango/angustus, Germanic angr/angust); AHD gives 'angh-. Tight, painfully constricted, painful ... [Pok. ang̑h- 42.]'. Two cross-cutting caveats: (1) the Avestan form printed in the book, 'azaehě', is not a real Avestan word — the PDF page image confirms the book itself prints 'azaehě', so this is Nourai's own corruption (not a scan error) of Av. ǫzaŋhē (Bartholomae AiW 363–4, Pokorny p.42 'ǫzaŋhē'); (2) the ni-āz / niyāz branch is claimed by a different root in current Iranian scholarship: Cheung, Etymological Dictionary of the Iranian Verb (2007) 171–172, files Av. niiāzata / niiāzaiiən and MP/Pth./Sogd./NP niyāz under *Haz 'to drive, lead' (PIE *h₂eǵ-, Skt. aj-, Lat. agō), not under *angh-. Bartholomae, Walde-Pokorny I 62 and Moʼin (following Bartholomae) all support Nourai; Cheung is the dissent.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82en%C7%B5%CA%B0-\",\n        \"https://ahdictionary.com/word/indoeurop.html\",\n        \"https://www.etymonline.com/word/anger\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:42\",\n          \"status\": \"supports\",\n          \"note\": \"POK_01.txt ↵-leaf 50 (printed p.42/43 — the '43' page numeral falls inside this leaf): 'anghos-, anghes ‚Beklemmung, Bedrängnis‘: ai. ámhas- n. ‚Angst, Bedrängnis, Not‘ ..., av. ǫzah- ‚Bedrängung, Not, Gefangenschaft‘ ... lat. angor m. ... angus-tus ‚eng‘ (aus *anghos-to-s); angustiae'; the database text POK_full.txt gives 'Root / lemma: angh- (*hengh-) / Meaning: \\\"narrow, *press\\\" ... References: WP. I. 62 f., WH. I 47. / Page(s): 42-43'. Grep: grep -n 'lemma: angh-' POK_full.txt.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"azaehě; ni-az\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two items. (a) 'azaehě' is a corrupt rendering of Young Avestan ǫzaŋhē, the infinitive of ǫz- 'to lace up, constrict, oppress' (Bartholomae AiW s.v.: 'j. ǫzaŋhe Inf. ‚zu bedrängen, in Not zu bringen‘: avaŋhe narǫm ašaonǫm ǫz° Yt 13.39'), beside the s-stem ǫzah- n. '1) Ein-, Zusammenschnürung der Kehle, Erdrosselung; 2) Bedrängung, Enge, Not; Gefangenschaft' (Yt 10.22, V 16.10, Y 10.17). Phonology: PIE *h₂enǵʰ- > Proto-Iranian *anź- > Av. ǫz- (the nasal is written with the nasalised vowel ǫ before the fricative), the exact match of Lat. angō/angor and Skt. áṃhas-. So Nourai's gloss 'compressed, in need' is right and the arrow root→Avestan is right for this word, but the printed shape is impossible Avestan. (b) 'ni-az' = Av. ǫz- with the preverb ni-, in the lengthened grade *ni-āz-, attested only in finite forms: ni-āzata 'she laces her waist in' (Yt 5.127, of Anāhitā) and ni-āzaiiən 'they shall wedge (it) in' (V 13.30). No Avestan noun *ni-āz- 'need' exists — Nourai's gloss 'that which pushes you down, need' back-projects the Middle Persian abstract. Walde-Pokorny I 62 print exactly this set ('Verbal av. ǫzaŋhe ‚zu bedrängen, in Not zu bringen‘, tiefstufig av. ny-azata ‚sie schnürt sich‘, ny-āzayən ‚sie sollen hineinzwängen‘'), and Bartholomae's own footnote to ǫz- points forward to 'np. niyāz ‚Mangel‘ bei Hbm. AGr. I.105'. THE DISPUTE: Cheung 2007:171–172 removes ni-āz from this root altogether and files it under Proto-Iranian *Haz 'to drive, lead' (< PIE *h₂eǵ-, Skt. aj-, Lat. agō), reading YAv. caus. (+ni-) 'to straiten' (citing De Vaan 2003:34), with MP nydʾc /niyāz/, Pth. nyʼz, Sogd. nyʼz and NP niyāz listed as its nominal continuations. Because the node's second word is assigned to a different root by the current standard work, the node takes the worse verdict.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82en%C7%B5%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:42\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt s.v. angh-: 'Material: Verbal: Avestan ǫzaŋhē “to press”, lengthened grade Avestan ny-azata “she squeezes herself into her corset”, ny-azayen “to wedge oneself in” ... Page(s): 42-43'; the German original (POK_01.txt leaf 50) has 'av. ǫzah- ‚Bedrängung, Not, Gefangenschaft‘'. So p.42 does carry both of Nourai's Avestan items — but in the shapes ǫzaŋhē / ny-āzata, not 'azaehě'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"AiW s.v. ǫz-, ǫzaŋhe, ǫzah- (BRT.txt lines 7853–7862)\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. ǫz- V. ‚schnüren‘. Praes. 3 aza- (nyaza-). Inf. ǫzaŋhe ... mit ni ‚einschnüren, einzwängen‘: hā hī maiδīm nyāzata ‚sie schnürt sich ihre Taille‘ Yt 5.127 ... ‚hineinzwängen in —‘ ... nyāzayən V 13.30. Vgl. gt. āna, lat. angō; s. auch ǫzah- ... s. aber np. niyāz ‚Mangel‘ bei Hbm. AGr. I.105.' Bartholomae both derives the forms from *angh- and connects them with NP niyāz — exactly Nourai's arrow.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 62 s.v. angh-\",\n              \"stance\": \"supports\",\n              \"note\": \"'angh- (kelt. auch engh-) ‚eng, einengen, schnüren‘, z. T. auch von seelischer Beklemmung, Angst. Verbal av. ǫzaŋhe ‚zu bedrängen, in Not zu bringen‘, tiefstufig av. ny-azata ‚sie schnürt sich‘, ny-āzayən ‚sie sollen hineinzwängen‘ (zum ā s. Bartholomae IF. 8, 235 m. Lit., Altiran. Wb. 362)'.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"pp. 171–172 s.v. *Haz 'to drive, lead'\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'*Haz ‚to drive, lead’. AVESTAN: az- ‚to lead’ || ... (+ *ni-) caus. ‚to straiten’ (cf. De Vaan 2003: 34) ... INJ. med. 3sg. YAv. niiazata (Yt 5.127), 3pl. YAv. niiazaiiən (V 13.30). MIDDLE PERSIAN: (+ *ni-) BMP nydʾc /niyaz/, MMP nyʼz ‚want, need, misery’ ... NWIR: (+ *ni-) NP niyaz ‚need’.' Cheung thus takes the very forms Pokorny/Bartholomae use as *angh- evidence and assigns them to PIE *h₂eǵ- 'drive' instead.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. angh-\",\n              \"stance\": \"partial\",\n              \"note\": \"'angh-. Tight, painfully constricted, painful. ... [Pok. angh- 42.]' — confirms the root and its gloss but lists no Indo-Iranian reflexes at all, so it is silent on the Avestan node itself.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"niyâz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian niyāz, Book Pahlavi ⟨nydʾc⟩ = ⟨nyʾc⟩, Manichaean MP and Parthian ⟨nyʼz⟩ 'need, want, misery' (MacKenzie, Concise Pahlavi Dictionary s.v.), with the derivatives niyāzōmand 'needy' and niyāzōmandīh 'poverty' and the negated compound abē-niyāz 'free from want'. Formally it is an Old Iranian action-noun *ni-āza- built to the verb seen in Av. ni-āz-: the preverb ni- + ā of the lengthened grade gives MP niyā- (the glide y is automatic between i and ā), and Old Iranian intervocalic -z- is kept, spelt ⟨c⟩ in Book Pahlavi. Age: Armenian took the compound over in the Arsacid period as apeṛniaz / apeniaz 'without need' = MP abē-niyāz (Hübschmann, Persische Studien §91), which shows the word already existed in Middle Iranian; Sogdian nyʼz 'need' and Christian Sogdian nyʼzʼwt 'needy' show the same formation in the eastern branch. Only the ultimate root attribution is contested (see node 1); that MP niyāz contains ni- + the āz- verb is agreed by everyone, Cheung included.\",\n          \"sources\": [\n            \"https://vajehyab.com/moein/%D9%86%DB%8C%D8%A7%D8%B2\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:4877\",\n              \"status\": \"partial\",\n              \"note\": \"The 6-vol Amir Kabir Moʼin is not online in any form, so p.4877 itself cannot be opened. Moʼin's entry as served by vajehyab.com/moein/نیاز reads '[په.] (اِ.) ۱- حاجت، احتیاج. ۲- نذری که برای گرفتن مراد و حاجت ... دهند' — the origin tag [په.] = Pahlavi is precisely the Pahlavi node Nourai draws, so the content of the citation is right even though the page cannot be verified.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD s.v. niyāz (PHD.txt line 514)\",\n              \"stance\": \"supports\",\n              \"note\": \"'niyāz [nydʾc | M nyʼz, N ~] need, want, misery. ~ōmand [-ʼwmnd | N ~mand] needy. ~ōmandīh: poverty.' Also 'abē-|-niyaz [-nyʼc] free from want.' The Manichaean and New Persian equations are MacKenzie's own.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Persische Studien §91 (HUB.txt line 6330)\",\n              \"stance\": \"supports\",\n              \"note\": \"'apeniaz ‚bedürfnisslos‘ = np. be-niyaz' — the Armenian loan proves an Arsacid-era Middle Persian abē-niyāz, i.e. the Pahlavi stage Nourai's chart requires.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p. 171 s.v. *Haz\",\n              \"stance\": \"partial\",\n              \"note\": \"Gives exactly the same Middle Iranian material ('MIDDLE PERSIAN: (+ *ni-) BMP nydʾc /niyaz/, MMP nyʼz ‚want, need, misery’ ... PARTHIAN: (+ *ni-) nyʼz ... SOGDIAN: CSogd. nyʼzʼwt ‚needing, needy’, MSogd. nyʼz ‚need’') but under a different PIE root.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep -n 'niyāz|niyaz|nyʼc' NYB_vol2_glossary.txt NYB_vol1.txt returns nothing; the word does not occur in the texts Nyberg glosses.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"niâz; nîâzî\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"MP niyāz passes into New Persian unchanged as نیاز niyāz 'need, want', with the derived adjectives نیازمند / نیازومند niyāz(ō)mand 'needy' (= MP niyāzōmand) — exactly the two forms Nourai prints in the box — and the Islamic-era religious sense 'votive offering made to obtain a wish' (Moʼin sense 2; Farhang-e Neẓām, quoted in Moʼin's note to Borhān). The second word نیازی niyāzī 'beloved, sweetheart' is a separate lexicographic item: Asadi Ṭusi's Loghat-e Fors already has «نیاز، دوست بود» with Labībī's line «ایا نیاز بمن ساز و مر مرا مگذار», and Rashīdī corrects him: «لیکن بمعنی دوست، نیازی است نه نیاز» — i.e. in the 'friend/beloved' sense the correct form carries the -ī, which is why Nourai's chart gives 'nîâzî: need, dear friend, sweetheart'; the ʿOsmān Mokhtārī couplet he quotes (دلم خستهٔ ناز توست ای نیازی) uses it in that sense. Semantically the 'sweetheart' sense is the object of one's niyāz, i.e. 'the one one longs for'.\",\n          \"sources\": [\n            \"https://vajehyab.com/moein/%D9%86%DB%8C%D8%A7%D8%B2\",\n            \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7%D8%B2\",\n            \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7%D8%B2%D9%85%D9%86%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:2222\",\n              \"status\": \"supports\",\n              \"note\": \"Checked with the local scan of Borhān-e Qāṭeʿ vol. 4 (BQT_v4_pages.txt, [pdf page 305] = printed 2222). Headword «نیاز بکسر اول بروزن حجاز، حاجت بود»; Moʼin's etymological footnote (n. 3, OCR garbled but legible): 'پهلوی niyāz (احتیاج، ضرورت، فقدان). از اوستا ni-āz ... و ریشهٔ āz بمعنی بستن، فشار آوردن و مجبور کردن (بستن، فشار دادن، بزور داخل کردن) «بارتولمه ۳۹۲» ... ǫzah (ضرورت، تنگی، احتیاج) «بارتولمه ۳۹۲»' — i.e. Pahlavi niyāz from Avestan ni-āz, root āz 'to bind, press, force', citing Bartholomae col. 392: literally Nourai's chain, source and all. The same page carries footnote 5 'باین معنی نیازمند، نیازومند و نیازی (ه.م.) است' (Nourai's script_extra) and footnote 8 with Rashīdī's 'لیکن بمعنی دوست، نیازی است نه نیاز' and Asadi's 'نیاز، دوست بود'.\"\n            },\n            {\n              \"ref\": \"MON:4877\",\n              \"status\": \"partial\",\n              \"note\": \"Same as node 2: the 6-vol Moʼin is not online, so the page cannot be opened; the online Moʼin entry نیاز '[په.] (اِ.) ۱- حاجت، احتیاج' (vajehyab.com/moein/نیاز) supports the content.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 4, printed p. 2222 (scan pdf page 305)\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check: headword نیاز 'need' + Moʼin's footnote deriving it from Pahlavi niyāz < Avestan ni-āz, and the نیازی 'beloved' discussion.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Moʼin, Farhang-e Fārsi s.v. نیاز (via vajehyab)\",\n              \"stance\": \"supports\",\n              \"note\": \"'[په.] (اِ.) ۱- حاجت ، احتیاج. ۲- نذری که برای گرفتن مراد و حاجت به کسی یا جایی دهند' — Pahlavi origin tag, 'need' plus the votive sense.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Grundriss no. 247 'be, ehe ‚ohne‘' (HRN.txt line 2525)\",\n              \"stance\": \"partial\",\n              \"note\": \"Horn has no separate entry for niyāz; he cites it only inside the bē- entry: 'phlv. ape- (pāz. awe-), z. B. ape-ḥīm, ape-vnās etc., be (ZPGl.), vergl. arm. LW. ape-niaz' — which does confirm the Pahlavi→New Persian continuity of the word.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p. 172 s.v. *Haz, NWIR section\",\n              \"stance\": \"partial\",\n              \"note\": \"'(+ *ni-) NP niyaz ‚need’' — the New Persian word and its ni-āz analysis are confirmed, but attached to *Haz 'to drive' rather than to *angh-.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi (ARY_pages.txt / ARY_latin_index_pages.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep of the Persian text and of the Latin index for نیاز / NIYAZ / ANGH returns no root entry; the word is not treated.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box standing for the Latin branch of *h₂enǵʰ-: the verb angō, -ere 'to press tight, throttle; to distress' (the exact match of Gk. ἄγχω and Av. ǫzaŋhē), its nouns angor 'constriction of the throat; anguish' and angina 'quinsy', the adjective anxius (< *angh-s-io-) 'uneasy, solicitous', and the s-stem adjective angustus < *angh-os-to-s 'narrow' with its abstract angustia(e) 'narrowness, straits, distress'. Ernout–Meillet stress that the double sense Nourai needs is Latin-internal: 'Ango se dit du physique et du moral; ce même double sens se retrouve dans les substantifs dérivés'. Both English words in the daughter box come out of this Latin material.\",\n          \"sources\": [\n            \"https://ahdictionary.com/word/indoeurop.html\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v. angh-: '4. Latin angere, to strangle, draw tight: ANXIOUS. 5. Suffixed form *angh-os-to- in Latin angustus, narrow: ANGUISH.' Exactly this node and its English child.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout–Meillet, DELL p. 59 s.vv. ango, angustus\",\n              \"stance\": \"supports\",\n              \"note\": \"'ango, -is, -xi, anctum, -ere: étreindre, oppresser, serrer (la gorge) ... Ango se dit du physique et du moral; ce même double sens se retrouve dans les substantifs dérivés: angor, -oris (m.) ... angor est aegritudo premens, Cic. Tu. 4,18 ... angustus: étroit, serré ... D'où angustia, employé surtout au pl. angustiae ... puis au sens moral ‚gêne‘.'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. anger, n. (KLN_1966.txt)\",\n              \"stance\": \"supports\",\n              \"note\": \"'... L. angere, ‚to press together, throttle, torment’, angustus, ‚narrow’ ... fr. I.-E. base *angh-, ‚to narrow, compress’.'\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 42–43\",\n              \"stance\": \"supports\",\n              \"note\": \"'lat. ango ‚beenge, schnüre zu‘ ... lat. angor m. ... angus-tus ‚eng‘ (aus *anghos-to-s); angustiae ‚Enge, Klemme, Schwierigkeiten‘.'\"\n            },\n            {\n              \"src\": \"LEW\",\n              \"where\": \"Walde–Hofmann index (LEW_1910.txt line 10454)\",\n              \"stance\": \"partial\",\n              \"note\": \"The local file is only the index volume; it lists 'ango, angul I 46', i.e. the entry stands at LEW I 46 (= the 'WH. I 47' Pokorny cites), but the article text itself is not in the local copy.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"anxious, anguish\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Two different routes out of the Latin box. ANXIOUS is a learned 16th/17th-c. borrowing straight from Latin anxius 'solicitous, uneasy' (formed to angere), with English -ous substituted for Latin -us; the noun anxiety likewise from anxietas, -atis. ANGUISH came by the popular route: Latin angustia (classical plural angustiae) 'narrowness, straits' > Old French anguisse, angoisse 'choking sensation, distress, anxiety, rage' (12th c., Modern French angoisse) > Middle English anguise, angoise (c.1200), whence the verb anguish from OF anguissier, angoissier. The semantic path is 'tightness/choking' > 'straits, difficulty' > 'mental torment'.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/anguish\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference of its own; the parent Latin box's AHD citation covers it ('Latin angere ...: ANXIOUS'; '*angh-os-to- in Latin angustus ...: ANGUISH').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. anguish, anxious, anxiety\",\n              \"stance\": \"supports\",\n              \"note\": \"'anguish, n. — ME. anguise, angoise, fr. OF. anguisse, angoisse (F. angoisse), fr. L. angustia ..., ‚narrowness, deficiency’, fr. angustus, ‚narrow’, fr. angere, ‚to throttle, torment’. See anger.' and 'anxious, adj. — L. anxius, ‚solicitous, uneasy’, fr. [angere]'.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etym. Dict. s.vv. Anxious, Angina\",\n              \"stance\": \"supports\",\n              \"note\": \"'Anxious. (L.) See Anguish.' and the angina entry 'L. ... lit. choking. — L. angere, to ... anxious, distressed'.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. angh-, index\",\n              \"stance\": \"supports\",\n              \"note\": \"Index lines: 'ANGUISH angh-', 'ANXIOUS angh-'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Germanic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box for the Germanic branch of *h₂enǵʰ-. The adjective *angwuz 'narrow' (Goth. aggwus, ON ǫngr, OE enge, OS engi, OHG angi/engī, G. eng) continues *anghu-; the s-stem *angaz- (< *anghos-, the same formation as Skt. áṃhas- and Lat. angor) gives ON angr 'grief, affliction'; and *angusti- (< *anghos-ti-, revocalised after *anghu-) gives OHG angust, OFris. angost, German Angst. Nourai's box leads only to English anger, i.e. to the ON angr reflex.\",\n          \"sources\": [\n            \"https://ahdictionary.com/word/indoeurop.html\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v. angh-: '2. Suffixed form *angh-os- in Germanic *angaz in Old Norse angr, sorrow, grief: ANGER. 3. Suffixed form *angh-os-ti- in Germanic *angusti- in Old High German angust (> German Angst), anxiety: ANGST.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. anger, n.\",\n              \"stance\": \"supports\",\n              \"note\": \"'ON. angr ... rel. to ON. ǫngr, OE. enge, ‚narrow, painful’, OS. engi, MDu. enghe, Du. eng, OHG. angi, engi, MHG. enge, G. eng, Goth. aggwus, ‚narrow’ ... fr. I.-E. base *angh-.'\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck, Selected Synonyms 16.42 (anger) and 16.31\",\n              \"stance\": \"supports\",\n              \"note\": \"'ME angre, NE anger, fr. ON angr ‚trouble, affliction’ ... : Lat. angor ‚constriction of the throat, anguish, trouble’, Skt. aṃhas- ‚distress, need’, ON ǫngr, OE enge, OHG angi, engi ‚narrow’, etc.' and 'OHG angust, MHG angest, NHG angst : OE ange, OHG angi, engi ‚narrow’.'\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 43\",\n              \"stance\": \"supports\",\n              \"note\": \"'anord. angr m. ... ‚Verdruß; Schade, Betrübnis‘; afries. angost, ahd. angust, nhd. Angst (aus *anghos-ti- nach *anghu- umvokalisiert)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"anger\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Not a native English word: Middle English angre (n., mid-13c., first 'distress, suffering, affliction'; v. c.1200 'to vex, irritate') is a loan from Old Norse angr 'grief, sorrow, affliction' / angra 'to grieve, vex' taken over in the Danelaw — the same Norse layer as e.g. ill, skin, take. The Proto-Germanic base is *angaz < *anghos-. The modern sense arose by transfer from the injury to the feeling it provokes ('the expression was transferred to the feelings of resentment naturally aroused in the mind of the person aggrieved'), giving 'rage, wrath' by the early 14th c., whence angry.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/anger\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference; the parent Germanic box's AHD citation covers it ('*angh-os- in Germanic *angaz in Old Norse angr, sorrow, grief: ANGER').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. anger, n. and anger, tr. v.\",\n              \"stance\": \"supports\",\n              \"note\": \"'anger, n. — ME., fr. ON. angr, ‚sorrow, affliction’ ... fr. I.-E. base *angh-, ‚to narrow, compress’ ... Derivatives: angr-y, adj.' and 'anger, tr. v. — ON. angra, fr. angr.'\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 16.42\",\n              \"stance\": \"supports\",\n              \"note\": \"'ME angre, NE anger, fr. ON angr ‚trouble, affliction’ (so also ME angre) : Lat. angor ..., Skt. aṃhas- ‚distress, need’ ...'.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. Awe (cross-reference to Anguish)\",\n              \"stance\": \"partial\",\n              \"note\": \"Skeat's own 'anger' headword is not legible in the local OCR; the Awe entry gives the family: 'Goth. agis, fear, anguish ... Gk. ἄχος, anguish, affliction; L. angor, choking, anguish ... See Anguish.'\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Angwhi\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂éngʷʰis 'snake' (Pokorny angʷ(h)i- 43–45; Watkins/AHD angʷhi- 'snake, eel')\",\n      \"note\": \"The root box itself is right: Pokorny 43–45 heads 'angʷ(h)i- ‚Schlange, Wurm‘' and AHD 'angʷhi-. Snake, eel.' What Nourai's single box hides is the split Pokorny states in his own first line: 'egʷhi-, ogʷhi- und eghi- ds.; mindestens zwei etymologisch verschiedene, aber früh verschränkte Sippen, deren Verhältnisse noch vielfach unklar sind.' Current handbooks separate *h₂éngʷʰis (Lat. anguis, Lith. angis, OPruss. angis, OCS *ǫzь, Pol. wąż) from *h₁ógʷʰis / *h₃égʷʰis (Skt. áhi-, Av. aži-, Gk. ὄφις, Arm. iž), which is where the Avestan branch of this chart actually belongs (see node 1). Ernout–Meillet put it bluntly: 'Le flottement porte sur l'initiale: e-, o-, an-, et sur les consonnes *gʷ, *gʰ, *gʷʰ ... On ne peut donc restituer un original indo-européen.' Separately, Walde–Pokorny I 65 reject the once-popular idea that *angʷ(h)is 'snake' is a 'constrictor' derived from the neighbouring root angh- 'to press' — 'ist wegen der Gutturalverschiedenheit und sachlich zu bestreiten' — which matters because Nourai prints Angh and Angwhi side by side on this page.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81%C3%B3g%CA%B7%CA%B0is\",\n        \"https://ahdictionary.com/word/indoeurop.html\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:43\",\n          \"status\": \"supports\",\n          \"note\": \"POK_01.txt leaf 51 (the printed '44' numeral falls in this leaf, so the entry opens on p.43): 'angʷ(h)i- ‚Schlange, Wurm‘, egʷhi-, ogʷhi- und eghi- ds.; mindestens zwei etymologisch verschiedene, aber früh verschränkte Sippen ... Lat. anguis = lit. angis (f.), apr. angis ‚Schlange‘ ...'; POK_full.txt: 'Root / lemma: angʷ(h)i- ... Meaning: “snake, worm, *fish” ... Page(s): 43-45.'\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"aži; aži-dahâkô\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both words are real. Av. aži- (stem ažay-) m. is 'snake' and, by extension, 'dragon, monster' — Bartholomae AiW: 'j. ažay- m. 1) ‚Schlange‘, ein daēvic animal (V 18.65, V 14.5) ... 2) schlangenähnliches Untier ‚Drache, Ungeheuer‘ (Y 9.30 ažiš sairitaʾ, Aog. 78)'; it is the exact cognate of Skt. áhi-, Gk. ὄφις, Arm. iž, Lat. anguis. aži.dahāka- is the three-headed serpent-tyrant of Yt 5.29–35, Yt 9.14, Yt 19.37 and Y 9.8, killed by Θraētaōna; Nourai's shape 'aži-dahâkô' is the Avestan nominative singular ažiš dahākō, the very form used by Horn (Grundriss no. 76 'aw. ažiš dahākō') and Hübschmann ('zd. aži dahākō'). WHY ONLY 'plausible': the arrow from the root box as drawn is phonologically wrong under the modern reconstruction. Av. aži- goes back to Proto-Iranian *Háǰiš < Proto-Indo-Iranian *Háǰʰiš < *h₁ógʷʰis — the NASAL-LESS variant. Pokorny himself puts it there, not under the nasal form: on printed p.44 he writes 'gr. ὄφις ‚Schlange‘ (*ogʷhis): cymr. euod (*ogʷh-): ai. ahi-, av. azi- ‚Schlange‘', i.e. in the *ogʷhi- paragraph, while Latin anguis heads the *angʷhi- paragraph. Klein hedges the same way ('prob. also with OI. ahiḥ, Avestic azish'), and Buck notes the two sets come 'fr. parallel forms with and without nasal, but phonetic relations in part obscure'. So the family relationship is real and old, but 'Avestan aži derives from *angʷhi-' is not what modern sources say. Nourai's gloss 'biting snake' for aži-dahāka- is also only one of several proposals for dahāka-, whose meaning is unsettled (variously 'stinging/harming', 'man-like', or a reflex of the ethnonym Dahā/Dahae).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81%C3%B3g%CA%B7%CA%B0is\",\n            \"https://en.wiktionary.org/wiki/%D8%A7%DA%98%D8%AF%D9%87%D8%A7\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:44\",\n              \"status\": \"supports\",\n              \"note\": \"POK_01.txt leaf 52 (printed p.44, the '45' numeral follows a few lines later): 'gr. ὄφις ‚Schlange‘ (*ogʷhis): cymr. euod (*ogʷh-): ai. ahi-, av. azi- ‚Schlange‘.' The page cited does carry Av. azi- — exactly as Nourai claims — but under the *ogʷhi- variant, not the nasal one.\"\n            },\n            {\n              \"ref\": \"KLN:86\",\n              \"status\": \"partial\",\n              \"note\": \"Klein does say precisely this, s.v. anguine: 'L. anguinus, fr. anguis, ‚serpent, snake’, which is cogn. with Arm. auj, oj, Lith. angis, OPruss. angis, Lett. uodze, Russ. už, Pol. wąż, and prob. also with OI. ahiḥ, Avestic azish, ‚snake’, Gk. ἔχις, ‚viper’', and s.v. Ahi: 'OI. ahiḥ, ‚serpent’, rel. to Avestic azish and cogn. with Gk. ἔχις, L. anguis'. But the page number does not match the copy on disk: in KLN_1966.txt the anguine/anguish entries sit in ↵-leaf 53, whose printed numerals read 77–79 (the calibration leaf = floor(p/2)+12 would put p.86 at leaf 55–58, which is the anth-/anti- material, containing no snake entry). So: content supports, page unconfirmed.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"AiW s.vv. ažay-/aži- and dahāka- (BRT.txt lines 6536, 13063–13065)\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. ažay- m. 1) ‚Schlange‘, ein daēvisches Tier ... 2) schlangenähnliches Untier ‚Drache, Ungeheuer‘'; 'j. dahāka- m. EN. eines sagenhaften daēvischen Königs von Iran; stets mit ažay- m.', with the note 'np. aždahā ‚Drache‘'. Bartholomae also gives 'ai. áhay- m., mp. až'.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 76, p. 19\",\n              \"stance\": \"supports\",\n              \"note\": \"'76. eždehä ‚Drache‘. aw. ažiš dahākō; phlv. aže dahäk, arm. LW. aždahak ... aw. aži- ‚Schlange‘; phlv. až; ai. áhi-; arm. iž.'\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck, Selected Synonyms 3.93 'snake'\",\n              \"stance\": \"partial\",\n              \"note\": \"'Lat. anguis; Lith., OPruss. angis; ChSl. *ǫzь, Pol. wąż, Russ. už; Skt. ahi-, Av. aži-; fr. parallel forms with and without nasal, but phonetic relations in part obscure. Walde-P. 1.63 ff.' — same family, but Buck flags the nasal/non-nasal problem Nourai's single box conceals.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, IE roots of Persian, Latin index p. 82\",\n              \"stance\": \"supports\",\n              \"note\": \"The index page groups under one root: 'AZHI-DAHAKA (AVESTAN), AZHI; AZDAHAG, AZ (PAHLAVI); OPHIS (GREEK), ANGUIS (LATIN), EKHIS, ECHINOS (GREEK), IZH (ARMENIAN), AHI (SANSKRIT), IGEL (GERMAN), IGIL (OLD ENGLISH)' — the same grouping Nourai draws, in a modern Persian IE-roots dictionary.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"eždehâk; eždehâ; aždar\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Iranian aži-dahāka- > Middle Persian až(i)dahāg (Book Pahlavi ʿcydhʿk', Manichaean MP ʿzdhʿg) > New Persian اژدها aždahā, by the regular loss of final MP -g and of the intervocalic stop; the fuller اژدهاک eždehāk preserves the -k and, in Borhān, is glossed as the last sense of اژدها, i.e. ضحاک ماران (Moʼin's footnote: 'مخفف اژی‌دهاک، ضحاک'). Horn (no.76) shows the date: the Armenian loan aždahak proves that the Middle Persian pronunciation was already až-, not aǰ-, in Arsacid/Sasanian times. The Semitic round-trip Nourai marks with ضحّاک in the box is real and runs Persian > Arabic > Persian: Asbaghi (PLA 190) has Arabic ضحّاک ḍaḥḥāk, folk-etymologised as the Arabic active participle 'the laugher / name of a king', from Persian aždahā 'Drache' < aži-dahāka > Pazand Dahāk 'evil, demonic king', 'arabisiert in ẓaḥḥāk'; and PLA 5 has a second, unassimilated Arabic borrowing أزدهاق azdahāq 'a particular dragon' straight from Persian. اژدر aždar is the shortened Persian form, from which Turkish ejder/ejderha and Bulgarian/Serbian ažder were taken (PLA 190); Borhān glosses اژدر as 'مار بزرگ ... و سر علم و رایت'. The modern military sense 'torpedo' (اژدر دریایی) is a 20th-c. Persian coinage on the dragon image, not an old sense. Nourai's extra gloss 'also a spear' for eždehā is Ferdowsi's metaphor and is exactly what Noushin's Shāhnāma glossary records.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%DA%98%D8%AF%D9%87%D8%A7\",\n            \"https://vajehyab.com/moein/%D8%A7%DA%98%D8%AF%D9%87%D8%A7\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:116,1339\",\n              \"status\": \"supports\",\n              \"note\": \"vol. 1: the اژدر / اژدرها / اژدها / اژدهاک cluster stands across ↵-leaves 327–328 of BQT_v1_pages.txt = printed pp. 117–118 (offset printed = leaf − 210), i.e. immediately at Nourai's p.116: 'اژدر ... سر علم و رایت را گویند و مار بزرگ را نیز گفته‌اند'; 'اژدرها ... مار بزرگ است که اژدر باشد ... و مردم شجاع و دلاور ... و پادشاهان ظالم را ... و ضحاک ماران را خصوصاً و بمعنی رایت و سرعلم هم آمده است'; 'اژدهاک با کاف معنی آخر اژدهاست که ضحاک ماران باشد', with Moʼin's footnotes 'مخفف اژی‌دهاک، ضحاک' and 'مخفف اژی‌دهاک، رک: اژدها'. vol. 3 ([pdf page 132] of BQT_v3_pages.txt ≈ printed 1339–1341): the headword 'ضحاّک بفتح اول و دوم مشدد؛ رک: اژی دهاک' — Borhān/Moʼin refer ضحّاک straight back to Avestan aži-dahāka, which is exactly what Nourai's parenthesis ضحّاک asserts.\"\n            },\n            {\n              \"ref\": \"PLA:5,190\",\n              \"status\": \"supports\",\n              \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen, p. 5 (PLA_pages.txt leaf 20, running head 'ʾabišam 5 azdahāk'): 'أزدهاق azdahāk: ‚ein bestimmter Drache‘ aus dem pers. اژدها azdaha ‚Drache‘, mp. aži-dahak, aw. aži-dahā ..., mand. asdahag. s. ḍahḥāk.' p. 190 (leaf 205, running head 'saidalāni 190 ǵariḍ'): 'ضحاك ḍaḥḥāk ‚Lachender; Name eines Königs‘ — pers. اژدها aždahā ‚Drache‘, a. dahāka > paz. Dahāk ‚böser, dämonischer König‘, arabisiert in ẓaḥḥāk. Hieraus zunächst tk. ažder, bulg./serb. ažder, mand. asdahak.' Both of Nourai's PLA pages are dead on, and p.190 even supplies his aždar.\"\n            },\n            {\n              \"ref\": \"FSF:43\",\n              \"status\": \"partial\",\n              \"note\": \"The entry exists and says exactly what Nourai's gloss says, but at a different page in the printing on disk: FSF_pages.txt ↵-leaf 54, running head 'اژدها ۵۰' = printed p. 50, reads 'اژدها — کنایه از نیزه: یکی باره زیر اژدهایی به کف' — i.e. 'a metaphor for the spear', illustrated with the very Ferdowsi line Nourai prints under the Persian box. refs_online notes the scanned copy is not the 1363 Donya printing Nourai used, which explains the 43 vs 50 offset.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 76, p. 19\",\n              \"stance\": \"supports\",\n              \"note\": \"'76. eždehä ‚Drache‘. aw. ažiš dahākō; phlv. aže dahäk, arm. LW. aždahak. arm. aždahak beweist, dass im Mittelpersischen až-, nicht aǰ- gesprochen wurde.' Horn's headword spelling eždehā is Nourai's eždehâ.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien §91 and §92 (HUB.txt lines 7020, 7620)\",\n              \"stance\": \"supports\",\n              \"note\": \"'aždahā ‚Drache‘ = arm. aždahak, zd. ažiš dahākō' and again 'aždahā ‚Drache‘ = zd. aži dahākō' — including the -ō nominative Nourai prints.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Moʼin, Farhang-e Fārsi s.vv. اژدها / اژدر (via vajehyab)\",\n              \"stance\": \"supports\",\n              \"note\": \"اژدها is tagged [اَوِس] = Avestan and referred to اژدرها / اژدر, defined as the winged, taloned, fire-breathing mythical serpent — same origin tag and same senses as the chart.\"\n            },\n            {\n              \"src\": \"FSF\",\n              \"where\": \"Noushin, Vāže-nāmak, printed p. 50 (scan leaf 54)\",\n              \"stance\": \"supports\",\n              \"note\": \"'اژدها — کنایه از نیزه' with 'یکی باره زیر اژدهایی به کف' — the source of Nourai's 'also a spear'.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 1 pp. 117–118; vol. 3 ≈ p. 1339 s.v. ضحّاک\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check above; Moʼin's footnotes derive both اژدهاک and ضحّاک from اژی دهاک.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"anguis\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin anguis (m., f. in early Latin) 'snake' is the direct reflex of the nasal form *h₂éngʷʰis and is exactly superposable on Lith. angis, OPruss. angis, Latv. uodze, OCS *ǫzь, Pol. wąż, Russ. už. It is an old religious/poetic word, largely replaced in prose by serpēns and uīpera (Pliny has it 40× against 360× serpēns); its derivatives are anguinus, anguiculus, and the diminutive-shaped anguilla 'eel' (paralleled by OPruss. angurgis, Lith. ungurys, Pol. węgorz for the same 'snake-fish' idea). It is the only word in this chart that the modern reconstruction actually assigns to *angʷʰi-.\",\n          \"sources\": [\n            \"https://ahdictionary.com/word/indoeurop.html\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt: 'angʷhi-. Snake, eel. 1. Latin anguis, snake: ANGUINE; ANGUILLIFORM. 2. Taboo deformation or separate root *ogʷhi- in Greek ophis, snake, serpent: OPHIDIAN, OPHITE; OPHIOLOGY, OPHIUCHUS. 3. Taboo deformation or separate root *eghi- in Greek ekhis, snake ...' — both the Latin node and its English child, and AHD's own note that the Greek/Indo-Iranian type may be a separate root.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout–Meillet, DELL pp. 59–60 s.v. anguis\",\n              \"stance\": \"supports\",\n              \"note\": \"'anguis, -is n. (et f. à l'ép. arch.): serpent. Mot ancien, employé dans la l. religieuse ... La forme anguis est superposable à v. pruss. angis ‚serpent (non venimeux)‘, lit. angis ‚serpent (venimeux)‘, pol. wąż ... L'indo-iranien a skr. áhiḥ, av. aziš ‚serpent‘, dont l'a est ambigu ... On ne peut donc restituer un original indo-européen.'\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 43\",\n              \"stance\": \"supports\",\n              \"note\": \"'Lat. anguis = lit. angis (f.), apr. angis ‚Schlange‘ (lett. uodze f.), aksl. *ǫzь, russ. už, poln. wąż ‚Schlange‘.'\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, IE Comparative Dictionary s.v. angʷhis (IEC.txt line 560)\",\n              \"stance\": \"supports\",\n              \"note\": \"'WP I, 63. Cf. ogʷhis. Lat. anguis, cf. anguilla; Br. anv ‚slowworm‘; OCS ǫzь ‚grass-snake‘; R už ‚adder‘; Li. angis f. ‚viper‘; Latv. odze ‚viper‘.' Mann too keeps *ogʷhis as a separate lemma.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 3.93\",\n              \"stance\": \"supports\",\n              \"note\": \"Lists Lat. anguis in the 'snake' table beside Lith. angis and ChSl. *ǫzь.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"anguine\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A learned borrowing, not an inherited word: English anguine 'snakelike, pertaining to a serpent' (17th c.) is Latin anguinus, the adjective of anguis, with the Latin -inus ending anglicised as -ine; the parallel anguineous renders anguineus. No French intermediary is needed, and the word has stayed a bookish one. AHD gives ANGUINE (with ANGUILLIFORM) as the English yield of this root through Latin.\",\n          \"sources\": [\n            \"https://ahdictionary.com/word/indoeurop.html\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference; the parent Latin box's AHD citation covers it ('Latin anguis, snake: ANGUINE; ANGUILLIFORM').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. anguine, anguineous\",\n              \"stance\": \"supports\",\n              \"note\": \"'anguine, adj., pertaining to a serpent. — L. anguinus, fr. anguis, ‚serpent, snake’ ... For the ending see suff. -ine (representing L. -inus).' and 'anguineous, adj., serpentlike. — L. anguineus, fr. anguis.'\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Webster's New Twentieth Century Dict. s.vv. anguineal, anguineous\",\n              \"stance\": \"supports\",\n              \"note\": \"'an-guinʹe-al, a. anguineous.' / 'an-guinʹe-ous, a. [L. anguineus, from anguis, a snake.] resembling a snake.'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, index and root entry\",\n              \"stance\": \"supports\",\n              \"note\": \"Index: 'ANGUILLIFORM angʷhi-', 'ANGUINE angʷhi-'.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-04T23:01:25.394Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-57.json (file state is current in your context — no need to Read it back)
```


## [2026-09-04T23:01:30.147Z] TOOL CALL #78: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-57.json > /dev/null && echo \"JSON OK\" && FLAGGED=1 python3 tools/verify_check.py 57",
 "description": "Validate and run verify_check"
}
```


### [2026-09-04T23:01:32.788Z] TOOL RESULT

```
JSON OK
nodes verified: 11/11
node verdicts: {'disputed': 1, 'confirmed': 9, 'plausible': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 8, 'partial': 4, 'not_checked': 3}
books consulted: {'supports': 32, 'contradicts': 1, 'partial': 7, 'silent': 2} | by book: {'KLN': 5, 'SYN': 4, 'CHEUNG': 3, 'AHD': 3, 'HRN': 3, 'POK': 3, 'BRT': 2, 'HUB': 2, 'BQT': 2, 'MON': 2, 'ARY': 2, 'LAT': 2, 'SKT': 2, 'WLD': 1, 'PHD': 1, 'NYB': 1, 'LEW': 1, 'FSF': 1, 'IEC': 1, 'WEB': 1}
FLAG: 57 Angh #1 azaehě; ni-az disputed | Two items. (a) 'azaehě' is a corrupt rendering of Young Avestan ǫzaŋhē, the infinitive of ǫz- 'to lace up, constrict, oppress' (Bartholomae AiW s.v.: 'j. ǫzaŋhe Inf. ‚zu bedrängen, in Not zu bringen‘:
```


## [2026-09-04T23:01:52.384Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-57.json` written; `verify_check.py 57` reports 11/11 nodes, no PROBLEM lines.

**PDF page 57 (book p. 27) — 2 charts, 7 redirects skipped**

- Root verdicts: confirmed 2 (Angh = PIE \*h₂enǵʰ-, POK 42–43; Angwhi = PIE \*h₂éngʷʰis, POK 43–45).
- Node verdicts: confirmed 9, plausible 1, disputed 1.
- Ref checks: supports 8, partial 4, not_checked 3. Books consulted: 20 distinct titles, 42 entries.

Flagged items:
- **Angh, node #1 (Avestan "azaehě; ni-az") — disputed.** "azaehě" is an impossible Avestan form; the PDF page image confirms the *book itself* prints it, so this is Nourai's own corruption of Av. **ǫzaŋhē** (Bartholomae AiW; Pokorny p.42). More seriously, Cheung, *Etym. Dict. of the Iranian Verb* (2007) 171–172 files Av. ni-āzata/ni-āzaiiən and MP/Pth./Sogd./NP *niyāz* under **\*Haz 'to drive'** (PIE \*h₂eǵ-), not under \*angh-. Bartholomae, Walde-Pokorny I 62 and Moʼin (via Bartholomae col. 392, quoted in the Borhān footnote) all back Nourai; Cheung is the modern dissent.
- **Angwhi, node #1 (Avestan aži, aži-dahākō) — plausible.** Pokorny's own p.44 places Av. *azi-* under the nasal-less variant \*ogʷhi- (with Gk. ὄφις, Skt. áhi-), not under \*angʷhi- (Lat. anguis); modern reconstruction: Proto-Iranian \*Háǰiš < \*h₁ógʷʰis. Family relation real, the drawn arrow is not the current one.

Notable ref findings: BQT:2222 is a bullseye (Moʼin's footnote gives Pahlavi *niyāz* < Av. *ni-āz*, root *āz* 'to bind, press', citing Bartholomae 392, plus نیازمند/نیازومند/نیازی). PLA:5 and PLA:190 are exact (Ar. أزدهاق and ضحّاك ← Pers. اژدها, and the source of *aždar* → Turkish *ejder*). BQT:116/1339 confirmed (ضحّاک → "رک: اژی دهاک"). Two page numbers are off in the copies on disk: **KLN:86** (Klein's *anguine*/*Ahi* content is right but sits at ~pp.78–82) and **FSF:43** (the اژدها = "کنایه از نیزه" entry with Nourai's exact Ferdowsi line is at p.50 in the available printing). MON:4877 unverifiable — the 6-vol Moʼin is not online anywhere; online Moʼin tags نیاز `[په.]` (Pahlavi), which matches. All 10 web pages archived via `fetch_source.py`.
