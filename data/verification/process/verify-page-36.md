# Verification process log — verify-page-36


## [2026-09-04T18:30:39.135Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 36 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-36.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-36.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-36.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 36` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T18:30:40.646Z] AGENT

I'll start by reading the instructions and the relevant files.


## [2026-09-04T18:30:42.778Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T18:30:42.791Z] TOOL RESULT

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


## [2026-09-04T18:30:43.114Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-36.txt"
}
```


### [2026-09-04T18:30:43.131Z] TOOL RESULT

```
1	=== PDF page 36 (book page 6) ===
2	--- entry 0 ---
3	ROOT [Akkadian] Agaru : to hire  (refs KLN)
4	#1 (parent #0) [Syriac] refs=KLN | 
5	  #2 (parent #1) [Arabic] refs=AKD:47; FVQ:49 | a`jara : he hired
6	    #3 (parent #2) [Persian] refs=MON | ejâreh «اجاره» : rent ; ojrat «اجرت» : wage ; ajr «اجر» : reward
7	  #4 (parent #1) [Greek] refs=KLN:74; AHD:453 | angelos : hired messenger ; eu-angelos : messenger of good news ; evangelion : good news
8	    #5 (parent #4) [Persian] refs=MON5:190 | Angelyŭn «انگلیون» : good news, Bible
9	    #6 (parent #4) [Arabic] refs=TAD:5 | enjîl : good news, Bible
10	      #7 (parent #6) [Persian] refs=MON:369 | enjîl «انجیل» : Bible
11	    #8 (parent #4) [English] refs=AHD | angel, Los Angeles, Evangelical
12	--- entry 1 ---
13	ROOT [Sanskrit] Agaruh : aloe wood  (refs KLN:55)
14	#1 (parent #0) [Arabic] refs=KLN:55 | al-oud : the wood, also a stringed musical instrument
15	  #2 (parent #1) [Persian] refs=BQT:1385 | ŭd «عود» : any fragrant wood, also a musical instrument (lute)
16	  #3 (parent #1) [French] refs=PHN:240; KLN:605,914 | luth : lute ; flute : this is influenced by "lute" but is probably from another root
17	    #4 (parent #3) [Persian] refs=MON:2573 | folŭt «فلوت»
18	    #5 (parent #3) [English] refs=AHD:776 | lute, flute
19	  #6 (parent #1) [Hebrew] refs=PRT:13 | alôth : aloe
20	    #7 (parent #6) [Greek] refs=None | 
21	      #8 (parent #7) [Latin] refs=None | 
22	        #9 (parent #8) [English] refs=AHD:36; PHN:36 | aloe
23	
```


## [2026-09-04T18:30:44.539Z] AGENT

I'll read the supporting files.


## [2026-09-04T18:30:46.812Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T18:30:46.851Z] TOOL RESULT

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


## [2026-09-04T18:30:49.481Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['KLN','AKD','FVQ','MON','TAD','AHD','BQT','PHN','PRT','POK','WLD','SYN','IEC','HRN','HUB','SKT','FSD','WEB','AFM','PLA','AFA','LKT','DEV','LAM','DOZ','HJB','AID','ARY','MON5']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False))\n    else: print(k,'MISSING')\n\""
}
```


### [2026-09-04T18:30:51.351Z] TOOL RESULT

```
<persisted-output>
Output too large (41.7KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b8j9bkk6k.txt

Preview (first 2KB):
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)", "local_files": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"], "cites": "page number, continuous across the two volumes (1966–67)"}
...
</persisted-output>
```


## [2026-09-04T18:30:55.996Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['AKD','FVQ','MON','TAD','AHD','BQT','PHN','PRT']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print('===',k, v.get('title'))\n    print(' cites:', v.get('cites'))\n    print(' page_offset:', v.get('page_offset'))\n    print(' local:', v.get('local_files') or v.get('local_file'))\n    print(' hint:', v.get('lookup_hint'))\n\""
}
```


## [2026-09-04T18:30:56.539Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-36.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:6000])\n\""
}
```


### [2026-09-04T18:30:57.850Z] TOOL RESULT

```
=== AKD H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
 cites: None
 page_offset: leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt
 hint: Organised by semantic field; Akkadian words in transliteration with Aramaic/Arabic/Persian loans. grep the word.
=== FVQ Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
 cites: page number of Jeffery, The Foreign Vocabulary of the Qurʾān (1938)
 page_offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves)
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt']
 hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
=== MON Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)
 cites: page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)
 page_offset: None
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
 hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
=== TAD Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR
 cites: None
 page_offset: 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt']
 hint: Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
=== AHD W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)
 cites: page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)
 page_offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
 hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
=== BQT Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)
 cites: page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material
 page_offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
 hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
=== PHN A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866
 cites: None
 page_offset: leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt
 hint: French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.
=== PRT E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958
 cites: None
 page_offset: None
 local: None
 hint: Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q=<word>. Entries are alphabetical with numbered sub-senses.
```


### [2026-09-04T18:30:59.721Z] TOOL RESULT

```
{
 "pdf_page": 36,
 "book_page": 6,
 "entries": [
  {
   "root": {
    "name": "Agaru",
    "lang": "Akkadian",
    "refs": "KLN",
    "gloss": "to hire"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Syriac",
     "refs": "KLN",
     "words": [],
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Arabic",
     "refs": "AKD:47; FVQ:49",
     "words": [
      {
       "translit": "a`jara",
       "gloss": "he hired",
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
     "refs": "MON",
     "words": [
      {
       "translit": "ejâreh",
       "gloss": "rent",
       "script": "اجاره"
      },
      {
       "translit": "ojrat",
       "gloss": "wage",
       "script": "اجرت"
      },
      {
       "translit": "ajr",
       "gloss": "reward",
       "script": "اجر"
      }
     ],
     "note": null,
     "quote": {
      "text": "اینهمه شهد و شکر کز سخنم میریزد - اجر صبریست کزآن شاخ نباتم دادند",
      "poet": "Hâfez"
     }
    },
    {
     "id": 4,
     "parent": 1,
     "lang": "Greek",
     "refs": "KLN:74; AHD:453",
     "words": [
      {
       "translit": "angelos",
       "gloss": "hired messenger",
       "script": null
      },
      {
       "translit": "eu-angelos",
       "gloss": "messenger of good news",
       "script": null
      },
      {
       "translit": "evangelion",
       "gloss": "good news",
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
     "refs": "MON5:190",
     "words": [
      {
       "translit": "Angelyŭn",
       "gloss": "good news, Bible",
       "script": "انگلیون"
      }
     ],
     "note": null,
     "quote": {
      "text": "ولی خط مرا افزون ، کرم کن تا کنم موزون - کلامی همچو انگلیون، به لحنی همچو یوحنّا",
      "poet": "Sohbat Lârî"
     }
    },
    {
     "id": 6,
     "parent": 4,
     "lang": "Arabic",
     "refs": "TAD:5",
     "words": [
      {
       "translit": "enjîl",
       "gloss": "good news, Bible",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 6,
     "lang": "Persian",
     "refs": "MON:369",
     "words": [
      {
       "translit": "enjîl",
       "gloss": "Bible",
       "script": "انجیل"
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 8,
     "parent": 4,
     "lang": "English",
     "refs": "AHD",
     "words": [
      {
       "translit": "angel, Los Angeles, Evangelical",
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
    "name": "Agaruh",
    "lang": "Sanskrit",
    "refs": "KLN:55",
    "gloss": "aloe wood"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Arabic",
     "refs": "KLN:55",
     "words": [
      {
       "translit": "al-oud",
       "gloss": "the wood, also a stringed musical instrument",
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
     "refs": "BQT:1385",
     "words": [
      {
       "translit": "ŭd",
       "gloss": "any fragrant wood, also a musical instrument (lute)",
       "script": "عود"
      }
     ],
     "note": null,
     "quote": {
      "text": "من زمزمهٔ عودم ، تو زمزمه پردازی - من سلسلهٔ موجم، تو سلسله جنبانی",
      "poet": "Rahî Mo`ayyerî"
     }
    },
    {
     "id": 3,
     "parent": 1,
     "lang": "French",
     "refs": "PHN:240; KLN:605,914",
     "words": [
      {
       "translit": "luth",
       "gloss": "lute",
       "script": null
      },
      {
       "translit": "flute",
       "gloss": "this is influenced by \"lute\" but is probably from another root",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "Persian",
     "refs": "MON:2573",
     "words": [
      {
       "translit": "folŭt",
       "gloss": null,
       "script": "فلوت"
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 5,
     "parent": 3,
     "lang": "English",
     "refs": "AHD:776",
     "words": [
      {
       "translit": "lute, flute",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 6,
     "parent": 1,
     "lang": "Hebrew",
     "refs": "PRT:13",
     "words": [
      {
       "translit": "alôth",
       "gloss": "aloe",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 6,
     "lang": "Greek",
     "refs": null,
     "words": [],
     "note": null,
     "quote": null
    },
    {
     "id": 8,
     "parent": 7,
     "lang": "Latin",
     "refs": null,
     "words": [],
     "note": null,
     "quote": null
    },
    {
     "id": 9,
     "parent": 8,
     "lang": "English",
     "refs": "AHD:36; PHN:36",
     "words": [
      {
       "translit": "aloe",
       "gloss": null,
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


## [2026-09-04T18:31:28.660Z] AGENT

Now let me start checking the local reference texts.


## [2026-09-04T18:31:30.390Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN_1966 angel ===\" && grep -n -i \"agaru\" KLN_1966.txt | head -30 && echo \"--- 1971 ---\" && grep -n -i \"agaru\" KLN_1971.txt | head -30",
 "description": "grep KLN for agaru"
}
```


### [2026-09-04T18:31:30.463Z] TOOL RESULT

```
=== KLN_1966 angel ===
2329:alodial,  alodium,  n.  —  See  allodial,  allodium, aloe,  n.  —  L.  aloe,  fr.  Gk.  aX6r),  ‘aloe’,  prob. borrowed  fr.  Heb.  ahaltm,  ahaldth  (pi.),  which are  perhaps  borrowed  fr.  OI.  agaruh,  aguruh, ‘aloewood’,  these  latter  being  prob.  of  Dravid- ian  origin.  Cp.  agalloch. aloetic,  adj.  containing,  or  of  the  nature  of,  aloes ; n.,  an  aloetic  medicine.  —  Formed  with  suff. -etic  fr.  Gk.  aXot],  ‘aloe’.  See  aloe, aloft,  adv.  —  ON.  a  lopt,  ‘in  the  air’,  whence  arose the  meaning  ‘on  high’.  See  a-,  ‘on’,  and  loft, aloin,  n.,  a  bitter  crystalline  substance  (chem.)  — Formed  fr.  aloe  with  chem.  suff.  -in;  so  called because  it  is  obtained  from  the  aloe, aloisiite,  n.,  a  hydrous  subsilicate  of  calcium, ferrum,  magnesium  and  sodium  (mineral.)  , Named  after  Prince  Luigi  (Latinized  into  Aloi- sius)  Amedeo  of  Savoy,  Duke  of  the  Abruzzi. For  the  ending  see  subst.  suff.  -ite. alone,  adj.  —  ME.  al  one ,  ‘all  alone  ,  fr.  al,  all , and  one,  fr.  OE.  an,  ‘one,  alone  .  Cp.  Du.  alleen, MHG.  al-ein,  al-eine,  G.  allein,  ‘alone’,  and  see all  and  one.  Cp.  also  lone, along,  adv.  and  prep.  —  ME.  anlong,  along,  fr.  OE. andlang ,  which  is  compounded  of  and-,  ‘against’, and  lang,  ‘long’.  The  first  element  is  cogn.  with Gk.  avxt,  ‘against’,  L.  ante,  ‘before’ ;  see  ante-, anti-.  For  the  second  element  see  long,  adj. aloof,  adv.  —  Originally  a  nautical  term  formed on  the  analogy  of  Du.  te  loef,  ‘to  windward  . See  loof,  luff.
2753:angary,  n.,  the  right  of  a  warring  nation  to  use or  destroy  the  property  of  neutrals.  F.  an- garie,  fr.  L.  angaria.  See  prec.  word, angel,  n.  —  ME.,  fr.  OF.  angele  (F.  ange),  fr.  L. angelus,  fr.  Gk.  oiyyeXo-,  ‘messenger,  divine messenger,  angel’  (whence  the  verb  dyyeXXetv, ‘to  bear  a  message,  report,  tell’),  which  is  rel.  to dyyapo?,  ‘mounted  courier,  messenger’;  of Persian,  ult.  of  Sem.  origin.  Cp.  Akkad,  agarru, ‘hireling,  hired  laborer’,  fr.  agaru,  to  hire  , which  is  rel.  to  Aram,  agar,  eggdr,  ‘he  hired’, (whence  Arab,  ajara,  of  s.m.),  Heb.  iggereth, Aram.  igglri,  iggartd,  ‘letter’,  prop,  message Cp.  angaria,  the  first  element  in  Ingram  and  the second  element  in  evangel.  The  sense  develop¬ ment  of  Gk.  ayyapo<;,  resp.  6cyyeXo<;,  from  a Sem.  noun  meaning  ‘hireling’,  may  be  illustrated by  the  phases :  ‘hireling,  hired  messenger,  mes¬ senger’.  Gk.  dyyeXoi;  in  the  sense  of  angel ,  is a  loan  translation  of.  Heb.  mat  dkh,  messenger, divine  messenger,  angel’,  fr.  base  l-'-k,  ‘to  send  . Derivatives:  angel-ic,  adj.,  angelica  (q.v.),  angel- ic-al,  adj.,  angel-ic-al-ly,  adv.,  angel-ic-ize,  tr.  v., angel-ize,  tr.  v.
24902:Nagari,  n.,  Devanagari,  —  OI.  nagari  ‘(the  script of)  the  city’,  prob.  of  Dravidian  origin;  cp.  Ta¬ mil  nakar,  ‘house,  palace,  temple,  dwelling, town,  city’,  Telugu  nagaru,  ‘palace’.  Cp.  the  sec¬ ond  element  in  Devanagari. nagor,  n..  a  West  African  antelope.  —  F.,  coined by  the  French  naturalist  Comte  Georges-Louis Leclerc  de  Buffon  (1707-88). nagyagite,  n.,  a  sulAd  of  lead,  gold,  tellurium  and antimony  (mineral.)  —  G.  Nagyagit,  named  in 1 845  by  the  Austrian  mineralogist  Wilhelm  Karl von  Haidinger  (1795-1871)  after  Nagyag  in Hungary  (now  Sacarambu  in  Romania).  The ending  -it  goes  back  to  Gk.  see  subst.
27409:Derivatives:  parget,  n.,  parget(t)-ing,  n. pargo,  n.,  the  porgy.  —  Sp.  pargo,  a  collateral form  of  pagro,  fr.  L.  pagrus,  phagrus,  pagarus, fr.  Gk.  <paypo?,  ‘sea  bream,  braise’,  prob.  iden¬ tical  with  oaypoc ,  ‘whetstone’,  which  is  possibly cogn.  with  Arm.  bark,  ‘sharp,  sour,  bitter’.  Cp. porgy.
--- 1971 ---
12084:are perhaps borrowed fr. OI. agaruh , aguruh, 
158252:town, city’, Telugu nagaru, ‘palace’. Cp. the sec- 
174089:form of pagro , fr. L. pagrus, pkagrus, pagarus,
```


## [2026-09-04T18:31:31.110Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== 1966 ===\" && grep -n \"^angel\" KLN_1966.txt | head -20 && echo \"=== 1971 ===\" && grep -n \"^angel\" KLN_1971.txt | head -20",
 "description": "grep KLN angel"
}
```


### [2026-09-04T18:31:31.180Z] TOOL RESULT

```
=== 1966 ===
2757:angelolatry,  n.,  the  worship  of  angels.  —  Com¬ pounded  of  angelo-  and  Gk.  -XaxpEia,  -Xaxpta,
=== 1971 ===
14827:angel. 
14832:angel, n. — ME., fr. OF. angele (F. ange), fr. L. 
14833:angelus , fr. Gk. <£yyeXoq, ‘messenger, divine 
14855:angel-ize , tr. v. 
15007:angelfish, n. — The name is prob. due to the mis- 
15012:angelic, adj. — F .angilique, fr. L. angelicus , fr. Gk. 
15024:angelo-, combining form meaning ‘angel’. See 
15025:angel. 
15027:angelolatry, n., the worship of angels. — Com- 
99100:angel. — Heb. GabhrVSl , lit. ‘man of God’, fr. 
150884:angel. — Late L., fr. Gk. Mix^X, fr. Heb. 
250528:angelus with a clapper’. Cp. toccata, toccatella,
```


## [2026-09-04T18:31:44.476Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint(\"leaves:\",len(pages))\nfor i,p in enumerate(pages):\n    for pat in ['agaru','ahaldth','agalloch','^lute','flute,  n','luth']:\n        pass\ntargets=['Akkad,  agarru','borrowed  fr.  Heb.  ahaltm','agalloch,','lute,  n.','flute,  n.']\nfor t in targets:\n    for i,p in enumerate(pages):\n        if t in p:\n            print(t,'-> leaf',i,'=> approx printed page', 2*(i-12), 'or', 2*(i-12)+1)\nEOF",
 "description": "Locate KLN leaves"
}
```


### [2026-09-04T18:31:46.487Z] TOOL RESULT

```
leaves: 903
Akkad,  agarru -> leaf 51 => approx printed page 78 or 79
borrowed  fr.  Heb.  ahaltm -> leaf 41 => approx printed page 58 or 59
lute,  n. -> leaf 15 => approx printed page 6 or 7
lute,  n. -> leaf 301 => approx printed page 578 or 579
lute,  n. -> leaf 327 => approx printed page 630 or 631
lute,  n. -> leaf 437 => approx printed page 850 or 851
lute,  n. -> leaf 492 => approx printed page 960 or 961
lute,  n. -> leaf 731 => approx printed page 1438 or 1439
lute,  n. -> leaf 732 => approx printed page 1440 or 1441
flute,  n. -> leaf 327 => approx printed page 630 or 631
```


## [2026-09-04T18:31:56.266Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in [327,492]:\n    p=pages[i]\n    print('===== leaf',i,'=====')\n    print(p[:200].replace('\\n',' '))\n    for m in re.finditer(r'(flute,  n\\.|lute,  n\\.)',p):\n        print('>>>', p[m.start():m.start()+700].replace('\\n',' '))\nEOF",
 "description": "Print KLN flute/lute entries"
}
```


### [2026-09-04T18:31:57.925Z] TOOL RESULT

```
===== leaf 327 =====
ret, fleur-de-lis,  flirt,  Flora,  flora,  floral,  Floreal, Florence,  Florentine,  florescent,  floret,  florid, florin,  flour,  flourish,  millefiori,  Phyllis,  phyllo-. The  meaning  ‘to  bloss
>>> flute,  n.  —  ME.  floute ,  floite,  fr.  OF.  flaiite, fleiite  (F.  flute),  fr.  OProven?.  flaiit,  which  is prob.  a  blend  of  OProven q.flaujol,  ‘flageolet’,  and laid,  ‘lute’.  See  flageolet  and  lute,  ‘a  musical  in¬ strument’.  It .flauto  and  Sp.  flauta  are  OProven?. loan  words.  Cp.  flout. flute,  intr.  v.  —  ME.  flouten,  floiten,  fr.  OF,  flak¬ ier,  fleiiter  (F.  fluter ),  fr.  OF.  flaiite,  fleiite, ‘flute’.  See  flute,  n. Derivatives:  flut-ed,  adj .,  flut-er,  n.,  flut-ing,  n., flut-y,  adj. flutist,  n.  —  A  hybrid  coined  fr.  flute  and  -ist, a  suff.  of  Greek  origin.  Cp.  flautist, flutter,  intr.  v.,  to  flap  the  wings;  tr.  v
>>> flute,  n. Derivatives:  flut-ed,  adj .,  flut-er,  n.,  flut-ing,  n., flut-y,  adj. flutist,  n.  —  A  hybrid  coined  fr.  flute  and  -ist, a  suff.  of  Greek  origin.  Cp.  flautist, flutter,  intr.  v.,  to  flap  the  wings;  tr.  v.,  to  move quickly.  —  ME .floteren,  fr.  OE .floterian,  ‘to  be tossed  by  waves,  to  flutter’,  freq.  of  flotian,  ‘to float’.  See  float,  v. Derivatives:  flutter,  n .,  flutter-er,  n.,  flutter-ing, adj.,  flutter-ing-ly,  adv.,  flutter-y,  adj. fluvial,  adj.,  pertaining  to  a  river.  —  L .  fluvialis, fr.  fluvius,  ‘river’,  which  is  rel.  to  fluere,  ‘to flow’.  See  fluent  and  adj.  suff.  -aL f.uviatic,  adj.,  fluvial.  
===== leaf 492 =====
an instrument’,  and  -ist.  Cp.  lutist. lute,  n.,  a  cohesive  substance.  —  ME.,  fr.  MF. (=  F.)  lut,  fr.  L.  lutum,  ‘mud,  clay’,  which  stands for  *lutom  and  is  rel.  to  -luere  in
>>> lute,  n.,  a  cohesive  substance.  —  ME.,  fr.  MF. (=  F.)  lut,  fr.  L.  lutum,  ‘mud,  clay’,  which  stands for  *lutom  and  is  rel.  to  -luere  in  polluere  (for *por-luere),  ‘to  pollute,  contaminate’,  and  to  lus¬ trum  (for  *lu-strom),  ‘slough,  bog,  morass’.  See pollute  and  cp.  lutetia,  Lutetian. Derivatives:  lute,  tr.  v.,  lut-er,  n.,  lut-ing,  n. lute,  n.,  a  stringed  instrument.  —  ME.,  fr.  OF. lut  (F.  luth),  fr.  OProven?.  laiit,  fr.  Arab,  al- ‘iid  (whence  also  Sp.  laud,  Port,  alaude.  It. liuto),  lit.  ‘the  wood’,  fr.  al-,  ‘the’,  and  ‘ud,  ‘wood’. Cp.  lutanist. Derivative:  lute,  tr.  and  intr.  v. lutccia,  n.  —  A  var.  
>>> lute,  n.,  a  stringed  instrument.  —  ME.,  fr.  OF. lut  (F.  luth),  fr.  OProven?.  laiit,  fr.  Arab,  al- ‘iid  (whence  also  Sp.  laud,  Port,  alaude.  It. liuto),  lit.  ‘the  wood’,  fr.  al-,  ‘the’,  and  ‘ud,  ‘wood’. Cp.  lutanist. Derivative:  lute,  tr.  and  intr.  v. lutccia,  n.  —  A  var.  of  lutetia. lutecium,  n.  —  A  var.  of  lutetium. lutein,  n.,  a  yellow  pigment  ( biochem .)  —  Coined by  Thudichum  from  L.  tuteum  (in  corpus  luteum, ‘egg  yolk’),  neut.  of  luteus,  ‘of  the  color  of  egg yolk,  yellow’  (see  luteous)  and  chem.  suff.  -in. The  pigment  was  so  called  because  it  occurs  in egg  yolk. luteo-,  combining  form  meaning  ‘g
```


## [2026-09-04T18:32:12.727Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('AKD.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('AKD leaves',len(pages))\nfor i,p in enumerate(pages):\n    if re.search(r'ag[aâā]ru|agarru|igru', p, re.I):\n        print('--- leaf',i,'printed ~',i-8)\n        for m in re.finditer(r'ag[aâā]ru|agarru|igru',p,re.I):\n            print('   ', p[max(0,m.start()-250):m.start()+250].replace('\\n',' '))\nEOF",
 "description": "grep AKD Zimmern for agaru"
}
```


## [2026-09-04T18:32:13.817Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ leaf 66 (p.49) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==67' FVQ_pages.txt | head -60",
 "description": "Print FVQ page 49"
}
```


### [2026-09-04T18:32:14.501Z] TOOL RESULT

```
AKD leaves 112
--- leaf 15 printed ~ 7
      gebrauchte  Wort minzör  auf  akk.  massaru  (mnzzaru,  manzaru)  zurückgeht. akk.  purldu,  peredu  eilig  :  >  wohl  arab.-pers.  band  Eilbote  und viell.  auch  spätlat.  veredus  Eilpferd  (s.  hierzu  noch  unten  S.  50).  Zu akk.  ugrii,  agarru  JVIietsklave  :  >  wahrsch.  äyyaQog  Postknecht  (nebst Ableitungen)  s.  u.  S.  47.  akk.  tajjalu  Kundschafter,  von  dälu, tälu  umhergehen  :  ^  viell.  aram.  fajjel  umhergehen. akk.  targumänu,  turgumütm  Dolmetscher  :  >  aram.
```


### [2026-09-04T18:32:16.210Z] TOOL RESULT

```
=== FVQ leaf 66 (p.49) ===
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
```


## [2026-09-04T18:32:21.397Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AKD leaf 55 (printed 47) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==56' AKD.txt",
 "description": "Print AKD page 47"
}
```


### [2026-09-04T18:32:23.172Z] TOOL RESULT

```
=== AKD leaf 55 (printed 47) ===
Harper  ÜI  312).  2)  K.  177,  7  (Harper  V  438).
3)  mahir  im  heutigen  Dialelit  des  Tilr  noch  speziell  :  nordwärts  segelnd.
4)  Falls  nicht  vielmehr  zu  akk.  kirubu  Stück  Land,  gehörig,  s.  oben  S.  40.
      46      
räume  (wohl  in  7  Stufen  übereinander  gedacht)  :  >  wolil  die  7  fabaqät (Stufen)  des  arabischen  Weltbildes.
11.  Familie,  (xesellschaft.
akk.  talimu  (ebenbürtiger)  Bruder  :  >  wohl  aram.  (jüd.-aram.,  christl.- pal.,  saraar.)  tdlima,   auch  viell.  spätliebr.  tälim  (Sir.  7,18).  akk.  te-
niqu  Säugling,  Kind  :  >  viell.  neuhebr.,  aram.  (christl.-jjal.)  t/nöq.
akk.  sutapü  Genosse,  Handelskompagnon  :  >  aram.  Sautäpä, sfdäpa  Genosse  (mit  denom.  Verben)  O  äth.  sidfifc,  mit  denom. Verben).  akk.  kinattu  Genosse  :  ^  aram.  l-dnätd.
akk.  criiu  Bräutigam,  irsüu  Verlobung  :  >»  viell.,  ti'otz  des  .v, hebr.  Fi.  'eres,  aram.  'äras  sich  verloben.  [akk.  hadasSahi  Braut,
selten,  viell.  <;  westsemit.  (hebr.)  hädäsa  eig.  die   neue  (von  der  jungen Frau).]  akk.  susajmiic,  msapinu,  susahlnu  Anführer   od.    ä.  :  >
aram.  sö.sdbmd,  Samdhinä  Brautführer  (>  nordsyr.-arab.  Sabm  dass.).
akk.  lamddu  (eig.  kennen  lernen)  und  idü  (eig.  erkennen)  vom  ge- schlechtlichen Verkehr  gebraucht  :  davon  viell.  beeinflußt  hebr.  jada (NT  und  spätgriech.  yiyvüaxity,  lat.  cognoscere)  in  diesem  Sinne,  ebenso aram.  Iidham,    arab.  'arafa.  akk.  nadänu   geben,    Gabe   :  >■  hebr.
Fl.  ngddnim  Ez.  16,33  Buhlerlohn,  und   viell.  auch  näde  dass.,  ebenda.
akk.  nudunnü  Mitgift  (von  nudanu  geben)  :  ]>■  jüd.-aram.  twdunjä.
akk.  mulugu  Mitgift  :  >  jüd.-aram.  nalög.  Zu  hebr.  moJiar,
aram.  mnhrd,  arab.  mahr  Brautgeld  s.  oben  S.  18  unter  akk.  mdlurH.
akk.  dsidtu  Ehe  (eig.  Weibscliaft)  :  davon  woiil  beeinflußt  neuhebr. "issitt,  ägypt.-aram.   "antiltä.  akk.  siqu  viell.  Verpflichtung  (der
Frau  gegenüber  dem  Manne),  dann  :  >  neuhebr.  ziqd.  akk.  eselni
entlassen  (die  Ehefrau),   sich  scheiden,  usuhha   die  Scheidungssumme  : davon  wohl  beeinflußt  hebr.  'äsühd  entlassen  (von  der  Frau).
akk.  puhni  Versammlung  :  >■  syi'.  imhrd  Gastmahl  (^  wahrsch. arab.  fuhr,  fuhr).  akk.  kvretu  Gastmahl  :  >  wohl  hebr.  kerd  (mit
denom.  Verbum).
akk.  Sa  diu  mhnu  jem.  begrüßen  (eig.  nach  seinem  Wohlbefinden fi'agen)   :'  davon   wohl   beeinflußt  hebr.  m'cd  h-Sdlom,   aram.  Äa'eZ  Sdldmä.
akk.  ummänu,  viell.  auch  iimmatu,  Volk,  Heer  (St.  viell.  'mm)  :
```


## [2026-09-04T18:32:30.693Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('AKD.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'Mietsklave|Postknecht|Mietling|agru|aggaru', p, re.I):\n        print('--- leaf',i)\n        for m in re.finditer(r'Mietsklave|Postknecht|Mietling|agru|aggaru',p,re.I):\n            print('   ...', p[max(0,m.start()-350):m.start()+350].replace('\\n',' '))\nEOF",
 "description": "Search AKD for Mietsklave/Postknecht"
}
```


### [2026-09-04T18:32:32.644Z] TOOL RESULT

```
--- leaf 15
   ... .  3,  17  als  Bez.  einer  Berufsklasse  in  Nineve  gebrauchte  Wort minzör  auf  akk.  massaru  (mnzzaru,  manzaru)  zurückgeht. akk.  purldu,  peredu  eilig  :  >  wohl  arab.-pers.  band  Eilbote  und viell.  auch  spätlat.  veredus  Eilpferd  (s.  hierzu  noch  unten  S.  50).  Zu akk.  ugrii,  agarru  JVIietsklave  :  >  wahrsch.  äyyaQog  Postknecht  (nebst Ableitungen)  s.  u.  S.  47.  akk.  tajjalu  Kundschafter,  von  dälu, tälu  umhergehen  :  ^  viell.  aram.  fajjel  umhergehen. akk.  targumänu,  turgumütm  Dolmetscher  :  >  aram.  targamänä, turgdmänä  O  arab.  targamän,  targuman,  turgumän,  woraus  auch  unser Dragoman);  dazu  neuhebr.  targüm  Übersetzung,  „Targum". 
--- leaf 30
   ... üru  Platterbse  =  hebr.  härül,  aram.  hurlri,  arab. hullar.     S.  dazu  unteu  S.  56. 2)  Die  ausschließliche  Lesung  des  fast  stets  ideogi-aphisch  geschriebenen  "Wortes für  Talent  als  hiltri  ei-soheint  mir  nicht  so  sicher  wie  allgemein  angenommen  wii'd.  "Wohl in  der  Bed.  „Scheibe"  (vgl.  hebr.  hiJckar)  begegnet  gaggaru  einmal  in  den  Amai-nabriefen. 3)  Das  allerdings  nur  als  Name  eines  Gefäßes  nachweisbar  ist.   22       irdenes  Faß,  Krug,  wie  auch  aram.  lignd,  hgettfi  i.  d.  Bed.  Stück  Saatfeld O  arab.  lugnat).  —  Ob  hierzu  auch  hebr.  log  ein  kleines  Maß  für  Flüssig- keiten, svr.  laggatä  Schüssel  und  Maßbezeichnung, 
--- leaf 34
   ... n,  Pfand,  Urkunde  usw.  oben  S.  16  ff., für  solche  aus  dem  Familienrecht,  z.  B.  Mitgift,  Scheidungsgeld  usw., unten  S.  46. 5.  Handwerke  und  Künste. akk.  ummänu,  älter  ummiänu  (Werk)meister  :  ]>•  aram.  'iminiänä (^  späthebr.  ^ommCin).  Zu  jüd.-aram.  sdwaljä  Lehrling,  Geselle s.  oben  S.  16  unter  samallü. akk.  naggaru,  nangarii  Zimmermann  (vieU.  <^  sum.  namga)  :  ^ aram.  naggaru  (mand.  nangurü)  O  arab.  naggär).  akk.  Pael  sidluln überdachen,  bälken,  sidfdu  Bedachung  (spez.  Bed. -Entwicklung  aus sülu  Schatten,  Scliirm)  :  in  Anlehnung  hieran,  aber  mit  gesetzlichem  Laut- 1)  Mit  Ersetzung  des  akk.  sdbätu  ergreifen,  durch 
   ... amilienrecht,  z.  B.  Mitgift,  Scheidungsgeld  usw., unten  S.  46. 5.  Handwerke  und  Künste. akk.  ummänu,  älter  ummiänu  (Werk)meister  :  ]>•  aram.  'iminiänä (^  späthebr.  ^ommCin).  Zu  jüd.-aram.  sdwaljä  Lehrling,  Geselle s.  oben  S.  16  unter  samallü. akk.  naggaru,  nangarii  Zimmermann  (vieU.  <^  sum.  namga)  :  ^ aram.  naggaru  (mand.  nangurü)  O  arab.  naggär).  akk.  Pael  sidluln überdachen,  bälken,  sidfdu  Bedachung  (spez.  Bed. -Entwicklung  aus sülu  Schatten,  Scliirm)  :  in  Anlehnung  hieran,  aber  mit  gesetzlichem  Laut- 1)  Mit  Ersetzung  des  akk.  sdbätu  ergreifen,  durch  das  entsprechende  syr.  'ehad. 2)  Sekundäre  t-Bildung  eines  Sta
--- leaf 56
   ...  Z'w,  Ihn  od.  ä.)  niederfallend  huldigen,  nQogxvvily  : >  aram.  meslfind  arm  (]>  späthebr.  mislrn,  arab.  mislcin,  äth.  meskin;  > ital.  mescliino,  franz.  mesquin,  auch  wohl  deutseh  dial.  nwkenhe  und  t^er- misquiemt).  akk.  sun'qtc,  sinqu  Hungerenot  :  >  viell.  syr.  sajte^ bedürftig  sein,  ssnlqfi  bedürftig. akk.  agru,  agir,  agarni  Mietsklave,  agüru  mieten  :  >  wohl  aram. 'egar  mieten,  "ägJrn  Lohnarbeiter  O  arab.  "agara);  ]>  wahrsch.  auch äyyago?  urspr.  wohl  Mietüng  und  dann  erst  Postknecht.  [akk.  ahdu Sklave,  Knecht,  selten,  <C  westsemit.  (hebr.  'ähed,  'nhd-,  aram.  'ahdä, arab.  'ahd).]  akk.  napi.iiu  Seele,  Leben,  v.
   ... niederfallend  huldigen,  nQogxvvily  : >  aram.  meslfind  arm  (]>  späthebr.  mislrn,  arab.  mislcin,  äth.  meskin;  > ital.  mescliino,  franz.  mesquin,  auch  wohl  deutseh  dial.  nwkenhe  und  t^er- misquiemt).  akk.  sun'qtc,  sinqu  Hungerenot  :  >  viell.  syr.  sajte^ bedürftig  sein,  ssnlqfi  bedürftig. akk.  agru,  agir,  agarni  Mietsklave,  agüru  mieten  :  >  wohl  aram. 'egar  mieten,  "ägJrn  Lohnarbeiter  O  arab.  "agara);  ]>  wahrsch.  auch äyyago?  urspr.  wohl  Mietüng  und  dann  erst  Postknecht.  [akk.  ahdu Sklave,  Knecht,  selten,  <C  westsemit.  (hebr.  'ähed,  'nhd-,  aram.  'ahdä, arab.  'ahd).]  akk.  napi.iiu  Seele,  Leben,  v.  Personen,  bes.  v. 
   ...  deutseh  dial.  nwkenhe  und  t^er- misquiemt).  akk.  sun'qtc,  sinqu  Hungerenot  :  >  viell.  syr.  sajte^ bedürftig  sein,  ssnlqfi  bedürftig. akk.  agru,  agir,  agarni  Mietsklave,  agüru  mieten  :  >  wohl  aram. 'egar  mieten,  "ägJrn  Lohnarbeiter  O  arab.  "agara);  ]>  wahrsch.  auch äyyago?  urspr.  wohl  Mietüng  und  dann  erst  Postknecht.  [akk.  ahdu Sklave,  Knecht,  selten,  <C  westsemit.  (hebr.  'ähed,  'nhd-,  aram.  'ahdä, arab.  'ahd).]  akk.  napi.iiu  Seele,  Leben,  v.  Personen,  bes.  v.  Skla- ven :  davon   wohl  beeinflußt  hebr.  «<yj&s  in  ders.  Bed.  akk.   ilid hJtim  im  Hause  geborener  Sklave  :  davon  wohl  beeinflußt  hebr.  jdl/'d hajit  da
```


## [2026-09-04T18:32:47.183Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD grep إنجيل ===\" && grep -n \"انجيل\\|إنجيل\\|أنجيل\" TAD_pages.txt | head -20 && echo \"=== leaves ===\" && python3 -c \"\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read(); p=t.split('\\f'); print(len(p))\nfor i,x in enumerate(p[:15]): print('LEAF',i,repr(x[:300]))\n\"",
 "description": "grep TAD for injil"
}
```


### [2026-09-04T18:32:49.236Z] TOOL RESULT

```
=== TAD grep إنجيل ===
=== leaves ===
87
LEAF 0 '                                     \u202bالف\u202c\n           \u202bياكابىاللبناك\u202c  \u202b\u202aَ8\u202c\u202c\n                       \u202bنببى\u202c\n\n\n\n\n       \u202bلحتل\u202c\n    \u202b\u202a -\u202cاا لدم\u202c  \u202b\u202a1\u202c\u202c             \u202bتت\u202c             \u202b\u202a7\u202c\u202c   \u202b\u202a:\u202c\u202c\n     \u202bامون\u202c\n\u202bظ\u202c     \u202b\u202a1\u202c\u202c\n\n\n\n      \u202bهني بنشره وتصحيحه وتعليق <واشيه\u202c\n                            \u202bا\u202c\n\n\n    '
LEAF 1 '                    \u202bذكرى الذ ممردص\u202c\n \u202bالى الكير بروحه ونكرة\u202c        \u202bالى من حك العلويغاد على الاادب\u202c\n\n \u202bوقلبه ؛ الى من حب اطق وشرف الحق ولا نخاف فسيبيل المقلومةلاتم\u202c\n                                  \u202bوالى الصديق الصادق فىكرم انلساانية\u202c\n\n\n                  \u202bعابلممل ي بنابت اباظ\u202c\n                   '
LEAF 2 '                                       \u202b\u202a0\u202c\u202c\n\n              \u202bبس الآالبارىء المادل اتقامل\u202c\n  \u202bان ميلا الى معرفة الاصل واجتهادا فياستخراج\u202c\n                                           \u202bسفى\u202c\n                                             \u202bاذىنخلق\u202c\n                                                   \u202bلها\u202c\n  '
LEAF 3 '                                         \u202b(ب)\u202c\n \u202bعلى أن رد الاخيل إلى أصل لفته قد أمعانيداشأوقالي ولقيت منه عنتا شاقا\u202c\n\n  \u202b\u202a85\u202c\u202c\u202bعريةوموقك\u202c\n            \u202bدلا وات نهمش أحرف\u202c\n                            \u202bة\u202c \u202bمش حروو\u202c\n\n\n               \u202bأضله بمارستان وهل جر ا\u202c          \u202bام "ترس وعربة أصابا ا\u202c\n           '
LEAF 4 '                                                                       \u202b\u202a0\u202c\u202c\n                \u202bلفل ونان قلطء دمع معنأه ولابة الاسقف ورعمته\u202c            \u202b\u202a١\u202c\u202c\n\n                          \u202bمعناه الذهب الخالص\u202c    \u202b\u202a 3\u202cاوناني\u202a80210\u202c\u202c       \u202b\u202a2\u202c\u202c\n\n                                \u202bبرشيم\u202a 6\u202cمعناءالخرير\u202c   \u202b\u202a1'
LEAF 5 ' \u202b\u202a--\u202cفينيعي وفيالعبرانية « ارحمان \u202a 6\u202cوهو حيوان في جوف صدفة\u202c       \u202bاراد\u202c\n \u202b|اكتشفه الفينيقيون فيالدهر\u202a "2\u202cالحامس عشرقبل المسيح فصيموا بدمه الاثواب\u202c\n     \u202bالحريرية وأطلقوا الارجوان علىالثوب نفهقترجمه اليونان بلغسهم « برفير»\u202c\n \u202bارخون واركون \u202a -\u202cووناتي ده«اعمة مناه المبتدأ والاول من كل شيء\u202c\n         '
LEAF 6 '\u202bمعاه أخبار تارمحية وقد استعمابا العرب ععى\u202c           \u202bاساطير \u200f بوناني \u202a8\u202c\u202c\n                                                            \u202bخرافات وحكابات\u202c\n                                     \u202bاستبرق \u202a -\u202cفارسي معناه الديباج الغديظ\u202c\n                                   \u202bاسرب \u202a -\u202cفارسي «سيرب» معناه رصاص\u202c\n'
LEAF 7 ' \u202bإرفج \u202a -\u202cتعريب علتهة؛ الجرماني الذيمعناهحر" وهوالسشمعب غرني\u202c\n\u202bجرمانيا الذي دوخ غاليا سنة \u202a 584\u202cومماها داعمه؛ \u202a,\u202cععده\u202a :\u202cفدخل هذا الاسمإلى\u202c\n                                               \u202bبلادنا إبان الهروب الصليبية\u202c\n \u202bمعمخورائط ب يوئاني \u202a 52114\u202cوهو اسملجار حامل الكرة الارضية\u202c        \u202bطلس\u202c\n        '
LEAF 8 '                             \u202b|قنوم ارامية \u202a 9 72\u202cقَدُوما \u202a 4\u202cمعناه الشخص\u202c\n \u202bفي الفارسية ل\u202a2\u202cنكر» وفىاليونانية اله عرببها المرساة والموجل\u202c           \u202bاجر\u202c\n\n \u202bجيل يوناني\u202a#\u202cوألعههدوع (إوتجيليون )معناه خير بشارة وبشرى فرح\u202c\n\u202b(نكليس ) عريها الجرى\u202c\n                   \u202bنقليسوحتكلس \u202a -\u202cيوناني \u202a59\u202cا\u202a600\u202cي» إ'
LEAF 9 '                                    \u202b\u202a5\u202c\u202c\n\n                                 \u202bدرن »\u202a6\u202c\u202c\n\n           \u202bبايا في اللاتينية همهم وهو تضعيف أب مقلوبا أي بايا\u202c\n\u202b(كوين\u202c\n    \u202bل الارض ت\u202c   \u202bكسا\u202c\n                  \u202bنلل\u202c\u202bبأبللى \u200f دعي اسمهابابللان الرب هناك بلب\u202c\n                \u202b« بابيلو » أيباالباله\u202c   \u202bووت\u202c\n   '
LEAF 10 '                                 \u202bم\u202c\u202bميه\u202c\n                                    \u202bم ل\u202c\n\n\n\n\n\u202bوممامدم أي قاس وهو\u202c\n                 \u202bمكب م\u202a6\u202cن\u202a 5008\u202cأي قل د\u202c\n                                   \u202bباروسيرت يوناني ر\u202c\n                                           \u202bتستعمل لنرقة قن الوا وطذعاه\u202c\n\u202bبارون \u202a -\u202cايطاني مه'
LEAF 11 '                                                              \u202bعت ات\u202c\n\n\n \u202bبأميا \u202a -\u202cنبات له قرون تطبخ أصله من أهريكا الحو ببة واسمه هناك هطتترمع\u202c\n \u202bو \u202a40362\u202cدمع وعرنوه ياميا لويتئوه \u202a1\u202cاناء وأطل! أي غاذق إزجة وهو من قصيلة\u202c\n                                                                             '
LEAF 12 '                                 \u202bعت اب\u202c\n\n\n                                \u202bرجيس \u202a -\u202cاسمالسيار لمشئري بالفارسية\u202c\n \u202bايطالي \u202a 35618200\u202cمعناه سثر الباب أصله فارسي « برده (أي \u202a5\u202c\u202c       \u202bرداه\u202c\n\n                                                           \u202bوسجف وغطاء\u202c\n\u202bريد \u202a -\u202cفارسي دن ردن أي دل وهومذكورفي'
LEAF 13 '                                        \u202bك\u202c\n                                        \u202bح \u202a:\u202cو\u202c\n                                           \u202bتبن\u202c\n\n\n      \u202bركي\u202a -\u202cعامية \u200f فارسي « بملكرىوبالكدهف»ها لويعحلثمل أن\u202c\n                          \u202bرميل \u202a -\u202cايطالمي \u202a 11:35\u202cوهو وعاء مستدير من خشب\u202c\n\n\n                '
LEAF 14 '                                  \u202bدوو\u202c\n\n\n\u202bمن « وى » أي رابحة ذكة و\u202a9\u202cستان» وهي أداة\u202c           \u202bيتان \u202a -\u202cفارسي \u202a5\u202c\u202c\n\n                                                    \u202bتدل على ظرف المكان\u202c\n    \u202bعلى \u202a 1\u202cايطالي والودام ج للأءذام وهو تصغير \u202a05\u202cوم أي وزنوقاللانشة\u202c\n\n\u202bبلبنيوس وفي اليونانية هؤام وهو نات '
```


## [2026-09-04T18:33:09.013Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHN leaf 271 (p.240) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==272' PHN.txt | head -50 && echo \"=== grep LUTH ===\" && grep -n \"^LUTH\\|^LUT\\b\\|LUTH,\" PHN.txt | head",
 "description": "Print PHN page 240"
}
```


## [2026-09-04T18:33:09.877Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHN leaf 67 (p.36) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==68' PHN.txt | head -50 && echo \"=== grep ALOES ===\" && grep -n \"ALOES\\|ALO.S\" PHN.txt | head",
 "description": "Print PHN page 36"
}
```


### [2026-09-04T18:33:11.094Z] TOOL RESULT

```
=== PHN leaf 271 (p.240) ===
240 LUT
Louqsor est le nom d'un village de la haute Egypte , qui occupe
une partie de remplacement de l'ancienne Thèbes, sur la droite
du Nil, et renferme de superbes débris de palais, ce qui lui
a valu^sa dénomination. — De ce lieu fut apporté, par l'in-
génieur français Lebas , l'obélisque érigé au milieu de la place
de la Concorde, à Paris, le 3 5 octobre i836. — Remarquez
que, pour le mot Louqsor, la première lettre de l'article al
n'est point représentée. Quelques dictionnaires géographiques
offrent la variante Luxor.
LUTH, s. m. (a.)
jyJI [a/^ou^] le bois en général , et en particulier le bois d'aloès.
Nom d'un instrument de musique à cordes , abandonné depuis
longtemps, — La transcription luth est tellement corrompue,
qu'il paraît assez difficile, au premier coup d'œil, d'y recon-
naître quelque affinité avec le mot oriental; mais on y parvient^
soit à l'aide de l'espagnol laud, soit au moyen du portugais
alaude, dans lequel l'article al figure intégralement. Le même
instrument s'appelle leuto ou liuto chez les Italiens, et lute chez
les Anglais.
=== grep LUTH ===
6791:LUTH, s. m. (a.)
```


### [2026-09-04T18:33:12.828Z] TOOL RESULT

```
=== PHN leaf 67 (p.36) ===
U A MA
vulgairement nommé chicotin (voyez ce mot). — Comparez avec
le persan le grec dXéti et le latin alœ, d'où vient par suite le
mot français. — Aloès est aussi le nom d'un arbre presque
semblable à l'olivier et qui croit dans l'Inde; son bois, qui est
odoriférant, s'appelle â»^ [^oûd] et ^yJI [a^oiU] en arabe.
AMAN, s. m. (a.)
;jUt [liifuln] sécurité, protectim, dérivé de (j^\ [àmin] être en
sûreté, sans crainte. Ce mot nous est devenu familier depuis la
conquête de l'Algérie. Demander l'aman, c'est se soumettre au
vainqueur, en implorant sa clémence ou en réclamant un sauf-
conduit. — Celui qui se met sous la protection de quelqu'un
fi
et qui en jouit s'appelle, en arabe, (j^U^iMt [motw(àmûi], et ce
teroie s'applique surtout, dans les pays musulmans, aux chré-
tiens étrangers qui y vivent sous la foi des traités. — Il faut
bien se garder de confondre aman avec iman. Voyez ce dernier
mot. — Les noms propres arabes Ahin ou Euin et Mahodn, qui
veulent dire constant, fidèle, à qui Ton peut se fier, appartiennent
à la même racine.
AMARRER, V. a. (a.)
jjfi\ [àfnarr] serrer une corde, — Amarre (en arabe, ^1^ marâr)
se dit du cordage qui sert à fixer un navire ou à l'attacher à
un autre bâtiment. — Le terme arabe explique le correspon-
dant français plus exactement que l'expression latine ad mare,
dans laquelle on a cru reconnaître quelque rapport avec amarre.
— En portugais et en espagnol , amarrar veut dire aussi atta-
cher un vaisseau avec des cordages.
=== grep ALOES ===
1598:ALOES, s. m. (p.-a.)
```


## [2026-09-04T18:33:17.346Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==67' PHN.txt | head -40",
 "description": "Print PHN aloes entry start"
}
```


### [2026-09-04T18:33:18.881Z] TOOL RESULT

```
ALO 35
dont le correspondant arabe esiioyjj^ [marboût!] au singulier,
<^t i^èl^yiy^ [marboûdin] au pluriel; car le pluriel (^^1^
[mmrâbil!tn]^ qui diffère du précédent, désigne spécialement,
d après les dictionnaires arabes , des cavaliers armés qui veiUeni
(ttsidûment à la défense au à F extension des frontières , et les faits
attestent que tel fut le principal rôle des Almoravides. — On
altribue aux Almoravides l'introduction en Espagne des mon-
naies appelées harabodtin et marav^di. Voyez ces mots.
ALMOUCANTARAt, s. f. pi. (a.)
oljJaÂiuJi \^almùuqaniarât^ les cintrées, les voûtées, part, passé
fém. plur. du verbe quadrilittère ^iaÂj [gonf'ar] cambrer^ donner
à tme construction la forme d'une arcade ou d'une voûte. Terme
d'astronomie qui désigne les lignes ou petits cercles tracés sur
la sphère parallèlement à l'horizon ; on les appelle aussi cercles
de hauteur. — Almoucantarât , étant déjà au pluriel en arabe,
doit s'écrire sans l'addition d'une s en français, et cette ortho-
graphe est certainement préférable à almicantarat, que l'on
trouve dans les dictionnaires.
ALOES, s. m. (p.-a.)
1^1 [édwâ] Nom d'une plante liliacée, très-commune en Asie
et autres contrées de l'Orient; elle est particulièrement cultivée
dans les jardins, à cause de la beauté de ses fleurs; et ses
feuilles produisent des filaments soyeux qui servent à faire des
cabas, des bourses et autres objets de fantaisie. Le suc amer
qu'elle fournit à la médecine s'appelle également aloès, et il y
en a de diverses qualités dont la meilleure est Valois socotrin,
3.
```


## [2026-09-04T18:33:25.867Z] TOOL CALL #19: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:1385 --image 2>&1 | head -60",
 "description": "Fetch BQT page 1385"
}
```


### [2026-09-04T18:33:34.560Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1385.png
REF: BQT:1385  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 178  OCR-lang: fas

و۱۳۸ فوسج
چهل و هشت صورت فلك که کوبا بآواز بلند | کردد ؛وینی کویند جوبی‌است که آش‌ب رآن‌کار
شخسیرا میطلید ۱ - ودیرآدمی رانیز وین د که نکند وهرچند بشکنند مربع برآید - و چوب
مقعد باشد بزیان عرب - سه گوشه را نیز کوبند که در تمویذهای
عوانان ؟ فلت - بانون‌بالف کشید.. کودکان بررشته کشند تا در خواب رسند ‎٩‏ -
کنایه از سبعةٌ ساره است که زحل و مشتری | وکنایه از صبح دم هم‌هست که دم سبح باشد.
ومریخ وآفتاب وزهرء وطارد ومام باشد. عود سیمین - بستی درم عودالسلیب
عود * - نم اول و سکون نانی (۱) است که کنایه از دم را
ممروق است, رتم موی سبح باشد. ا ط
ی ۱۹ عودملای وا
که‌بجهت بخور عود کنایهازمفیدی‌وسیاهعی 1 ی
سوزاشد . گوبند عود بیخ درختی است که | باشد - سپ شا یر
آرا میکنند و در زبس زمین دفن میکنند " | عودی تخت وا 9
سیر درو پنیداید وودخا ی کردد- ۳۰ | نی از اسان رک
سازی هم‌هت که نوازند ۴ . ۲ و ۳
عود الصلیب - دوابی است‌که را | است ۰
فاوالیا9 گوبند.باهر که‌باشد اززحمت‌صرع ایمن عوسج ۷ - عوسج

(۱) چك :۳ ودال .

۹ < بورطیس حارس * بقار < کاوچران * رامی‌الداء * حاری الثمال * صباح <
حاری‌الماء 7 5076 ال 027۵160 < 8010۷107 «لغت نامه: ثوابت شمارء ۵ از صورتپای
شمالی » . ۲ - جمع عوان ( بفتح‌اول ودوم مشدد ) سخت کیرنده وظالم وزج کننده -
وسرهنگه دیوان سلطان «غیات» .

۴ - (ص) «عودبالشم چوب ... ورباب- وچوبی است که دخان آن بوی خوش دارد >
«منتهی‌الارب» عه اگر (هندی) - رادیوی *< داربوی ۳ 1(۸10#لمانی) «یورداود. خرده‌اوسما .
۳۹و فراسوی 81068 . ۴ - آلت‌طرب دارای ‎٩‏ با»سیم«تفس» .كلم اتگلیسی
6 فرادوی 11110 مأخون از ( المود ) عربی است . تصوبر آلنی موسیقی شبیه بمود برروی
تفش برجستهٌ گلی‌سومری که متعلق بسه هزار سال قبل از میلاه است‌بافی ماندء. «ردورة اسلامی
این آلت موسیقی در نواحی شمال شرقی ظاهر میشود باین صورت که سرآن که جای کوشیهای
ساز است بطرف‌عق بر گشته وکاسة‌آن ازیوست پوشیده شده است ( مجلهٌ روز گاراو چه شماره4:
بعضی از آلات موسیقی شرقی غربی بقلم وانلد .ءلچ) ۰ ۵ -01۷۵[۵6 (ف) :لك ۷
یس٩۸۹‏ ورك : فاوانیا .

‎٩‏ -چوآن‌مود السلیب اسر برطفقل صلیب آویزم اندر حلق عمدا. «خاقانی‌شروانی۲۲».

‏۷ -(عر)*عوسجة کدحرجه ...خاری است,عوسج جمع» «منتهی‌الارب» عوسج‌انواع مخّلف

‏دارد : شت * خوعشه انگور < 62150271122 3۳27008 «نابتی ۰۱۹۸
( 1:09 2۳۵۶ط3 «لك؟ سی؟4۸۲ - دوم ۳ وليك * ۳2126819 «ثابتی ۱۹۸
سوم * دپوخار > 010زا «ثابتی ۰۱۹۸
```


## [2026-09-04T18:33:48.237Z] TOOL CALL #20: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1385.png"
}
```


### [2026-09-04T18:33:48.963Z] TOOL RESULT

```

```


## [2026-09-04T18:33:48.960Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-04T18:34:23.077Z] TOOL CALL #21: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1385.vision.txt <<'EOF'\n[Read from image data/verification/sources/refs/ocr/BQT/1385.png = BQT_v3_picofile.pdf pdf-page 178.\n NOTE: the running-head numeral printed at the top of this page is -۱۳۸۰- (1380), NOT 1385.\n The entry عود with Mo'in's etymological footnotes is on this page.]\n\nHeadwords on the page: عوانان فلک ، عود ، عودالصلیب ، عود سیمین ، عود گلابی ، عودی تخت ، عوسج\n\nعود ۳ ـ بضم اول و سکون ثانی (۱) معروف است، و آن چوبی باشد سیاه رنگ که بجهت بخور\nسوزانند. گویند عود بیخ درختی است که آنرا میکنند و در زیر زمین دفن میکنند تا تغییر در وی\nپدید آید و عود خالص گردد ـ و نام سازی هم هست که نوازند ۴.\n\n--- Mo'in's footnotes at the bottom of the page ---\n\n۳ ـ (عر) «عودبالضم چوب ... و رباب ـ و چوبی است که دخان آن بوی خوش دارد» «منتهی‌الارب» ـ\nاگر (هندی) = رادبوی = داربوی = Aloë (آلمانی) «پورداود، خرده‌اوستا ص۱۳۹ و ۱۴۶» فرانسوی aloés.\n\n۴ ـ آلت طرب دارای ۶ یا ۲۰ سیم «نفس». کلمهٔ انگلیسی lute فرانسوی luth مأخوذ از (العود) عربی\nاست. تصویر آلتی موسیقی شبیه بعود بر روی نقش برجستهٔ گلی سومری که متعلق به سه هزار سال قبل\nاز میلاد است باقی مانده. در دورهٔ اسلامی این آلت موسیقی در نواحی شمال شرقی ظاهر میشود\nباین صورت که سر آن که جای گوشیهای ساز است بطرف عقب برگشته و کاسهٔ آن از پوست پوشیده\nشده است (مجلهٔ روزگار نو ج ه شمارهٔ ۴: بعضی از آلات موسیقی شرقی غربی بقلم واندل ولچ).\n\n۵ ـ pivoine (ف)، «لک ۲ ص۴۸۶» ورک: فاوانیا.\nEOF\necho saved",
 "description": "Save BQT vision transcription"
}
```


## [2026-09-04T18:34:26.144Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt; do echo \"=== $f ===\"; grep -c \"\" $f; done; echo \"--- انجیل ---\"; grep -o -n \".\\{0,180\\}انجیل.\\{0,180\\}\" MON_part1.txt | head -8; echo \"--- انگلیون ---\"; grep -o -n \".\\{0,180\\}انگلیون.\\{0,180\\}\" MON_part1.txt MON_part2.txt | head -5; echo \"--- فلوت ---\"; grep -o -n \".\\{0,180\\}فلوت.\\{0,180\\}\" MON_part1.txt MON_part2.txt | head -5",
 "description": "grep Mo'in for injil, angelyun, flute"
}
```


### [2026-09-04T18:34:30.438Z] TOOL RESULT

```
saved
```


### [2026-09-04T18:34:40.213Z] TOOL RESULT

```
=== MON_part1.txt ===
99339
=== MON_part2.txt ===
94500
--- انجیل ---
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,180}
                            \___exceeds complexity limits


--- انگلیون ---
ugrep: error: error at position 92
\n\x80-\xbf][\x80-\xbf]*){0,180}
   exceeds complexity limits___/


--- فلوت ---
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,180}
                          \___exceeds complexity limits
```


## [2026-09-04T18:34:44.179Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['MON_part1.txt','MON_part2.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for w in ['انجیل','انگلیون','فلوت','اجاره','اجرت']:\n        hits=[m.start() for m in re.finditer(w,t)]\n        print('###',f,w,len(hits))\n        for h in hits[:3]:\n            print('   ...',t[max(0,h-200):h+250].replace('\\n',' '))\nEOF",
 "description": "Search Mo'in text"
}
```


### [2026-09-04T18:34:47.047Z] TOOL RESULT

```
### MON_part1.txt انجیل 6
   ... ه خاطر»  فارغ البال. بی‌دلواپسی؛ مق. مضطرب.  اسوندار: 2011-۲۳ (امر.) (گیا.) درختی  است که در جنگل‌های شمالی ابران وجود  دارد و دارای چوب سختی است. رشه و  بسرگگك‌های آن مسصرف دارویی دارد؛  دمیر آغاجی» انجیلو» انجیلی» انجول» توبی؛  نمی » زوند.   اسه؛ (6-)352 (.) زردی و بژمردگی که بر  روی آدمی با بر گیاه افتد» آسه غله» گر سنة    آساننده؛ آسوده).    آسه زده.  اسه: ()«ة [قس. آیش» آمدن] (.) کشت  و زراعت» زمینی که برای کشت آماده کر ده    فرهنگ فارسی معی
   ...  فارغ البال. بی‌دلواپسی؛ مق. مضطرب.  اسوندار: 2011-۲۳ (امر.) (گیا.) درختی  است که در جنگل‌های شمالی ابران وجود  دارد و دارای چوب سختی است. رشه و  بسرگگك‌های آن مسصرف دارویی دارد؛  دمیر آغاجی» انجیلو» انجیلی» انجول» توبی؛  نمی » زوند.   اسه؛ (6-)352 (.) زردی و بژمردگی که بر  روی آدمی با بر گیاه افتد» آسه غله» گر سنة    آساننده؛ آسوده).    آسه زده.  اسه: ()«ة [قس. آیش» آمدن] (.) کشت  و زراعت» زمینی که برای کشت آماده کر ده    فرهنگ فارسی معین ۴۷    
   ... » چین و  چروک بافتن پوست چهره و بدن (به سب  پبر ی).   انجیدن: 7 ره [ریزه‌ریزه کردن]  (مص‌م.) ریز ریزه کردن» ریزریز کردن.  بیرون کشیدن. استره زدن در ححجامت»  بریدن. آزردن» زخم زدن.   انجیرز ۲[- 201 [- انجیل ] (.) ( یا ۰ درختی  از تبرةٌ گز نه‌ها جزو دستة توت‌ها که بلندیش  تا ۱۲ متر می‌رسد و برخلاف توت یک پایه  است و گل‌های نر و ماده‌اش سر روی بکث    درخت است؛ تین.   انجیر بن: .2 (امر.) درخت انجیر.  ان‌جیرخوار: ۲۳ ([- ان‌جیرخور]  (امر.) (جان.) پرنده
### MON_part1.txt انگلیون 2
   ... ده و کمی محدب و  طسویل است؛ پریشاه‌رخ» سارطلایی؛  انجیرخور.   انجیر دل: 2012۲-0 [- انج ] (مصع.)  (انجیر د» انجبرد؛ خواهد انجیرد» بینجیر »  انجیر نده» انجیر ده) سوراخ کردن» 04  انجیل: ا[[ [معر. شارت < انگلیون]  (اخ.) هر یکث از چهار کتاب دینی مسیحیان)  ج. اناجیل.   انجین: 2101-10 ریزریزه. (افا.) ریز کننده.  انسجوچک: *00هه [- انسجکک] (.)  (گیا.) درختی از تیر؛ گل‌سرخیان که در  ایسران در جنگل‌های خشک فارس و  کو ه‌های بختباری و لرستان وجود دارد. دانة  
   ... ک کردن: 2801-26-0 [ء  انگولکك کردن] با انگشت چیزی را زیر و  ینت دخالت کردن در کاری  (تو أم با با بهم زدن آن).   انگله: (ع-)«-ا0برمه ( ۰) تکمه» دکمه» گوی  گریبان؛ انگل» عر وه.   انگلیو ت ز(اخ.) انجیل؛ انگلیون.  (.) چون مسیحیان شرقی انجیل را در قماش    ابریشمین و ملون می‌پیچیده‌اند» از اینرو آن    ۳    ۳9  نگ 9( تست  مادهة جستتل ۵ لرجی که از درختان تتضوعا  درختان آلو و آلو چه و گو جه خارج می‌شود   و ای   انگور: 208-۳۲ [ آنکره کر کر. دوجیکی ] (.)  (
### MON_part1.txt فلوت 0
### MON_part1.txt اجاره 13
   ... تجاب» بدیرفته» مقبول. اجابت معده:  (بز.) عمل کردن و کار کردن آن.   احاده: (0-)6202 [- احادت» ع. اجادة]  (مص‌م.) نیکو گردانیدن. نیک گرفتن. نیکك  کردن. چیز نیکو آوردن. (اسص.) نیکث  گفتاری. یک کرداری.   اجاره؛ (عیص۲قه [- اجارت. ع. اجارة]  (مص‌ع.) رهانیدن» به فریاد رسیدن» زینهار  دادن. به مر ددادن ِِ چز آن. به مزد  گرفن. اجیر داسته کم  منفعت» مالی که مستأجر به موجر بپردازد.  مزدوری که کسی را می‌دهند. (قف.) تملیت  منافع» عمقدی که به‌موجب آن ۳  مالکث‌م
   ... ینهار  دادن. به مر ددادن ِِ چز آن. به مزد  گرفن. اجیر داسته کم  منفعت» مالی که مستأجر به موجر بپردازد.  مزدوری که کسی را می‌دهند. (قف.) تملیت  منافع» عمقدی که به‌موجب آن ۳  مالکث‌منافع عین فش بر شود  اجاره‌بندی: [-0د9-» [ع. . ف.] (حامص.)  تعیین اجارة یک يا چند مستغل.   اجاره‌بها: 8 [ع. ف.] (فق. حق.) پول  و بهایی که در برابر اجاره کردن جایی به  صاحبت آن می‌بر دازند. مبلغی است که به  ازای استفادة مستأجر از منافع عين مستجره  به موجب می‌بردازند» مال 
   ...  مالی که مستأجر به موجر بپردازد.  مزدوری که کسی را می‌دهند. (قف.) تملیت  منافع» عمقدی که به‌موجب آن ۳  مالکث‌منافع عین فش بر شود  اجاره‌بندی: [-0د9-» [ع. . ف.] (حامص.)  تعیین اجارة یک يا چند مستغل.   اجاره‌بها: 8 [ع. ف.] (فق. حق.) پول  و بهایی که در برابر اجاره کردن جایی به  صاحبت آن می‌بر دازند. مبلغی است که به  ازای استفادة مستأجر از منافع عين مستجره  به موجب می‌بردازند» مال الاجاره» اجرة  السمیء عوض.   اجاره‌نامچه: (م-)مک- 050 [ع. ف.]  (امر. م
### MON_part1.txt اجرت 18
   ... رفن. گزند کردن. همه چیز را بردن.  نزدیکك شدن. با کسی نزدیکی کردن.  نقصان کردن؛ ج. اجحافات.   اجدع: م14« [غ.] (ص.) کسی که بینی وی  را بریده باشند» بریده بینی.   اعضتیت: : 21 [ع.] (.) باداش نیکك» مزده  اجرت. واب. بای مزد. کاب زنان» مهر زن.  (مسصم.) باداش نیک دادن» مزددادن.  اجرجزیل: مزدفراوان» باداش گران.  اچراء: له (ع. ف. اجرا] (مسصم.)  راندن» روا کردن امری. وظیفه و راتبه و  جیره مقرر کردن برای کسی. کسی را وکیل  کردن. امضاء کردن. بکار بردن لفظ و  
   ...  کواکب و غیره. اجسام غیر مرکبه و یا مرکب  از عناصر متساوی الاجزاء مانند: طلاء نقره»  آهن. اجرام چرخ: افلاکث و ستارگان. اجرام  سماوی: سماوی. (فل. نج.) اجرام بسیط.  اجرام مرکب (مرکبه) (شیم.) اجسامی که  اجرت: 013۱ [ع. اجر ة] (.) مزد» مزدکار»  دستمزد» حق‌القدم. کرایه. قیمتی که در  تن می سود   اجری: [[ه [ع. ممال اجر اء] (.) مستمری»  مقرری» جیره» وظیفه و راتبه» جنسی که به  لشکر بان و جز آنان می‌داده‌اند. اجراء» اجرا»  جر ی» جر ۵.    اجز اء  اجزاء: 2123
   ...  حد  در گذشتن. (امص.) نافرمانی» س رکشی»  گردنکشی. ستم ظلم. اف زون‌جویی.  گمراهی» ضلالت.   بعی: : 9:1 [ع.] (ص.) بدکار» بد کار ه.  بغیاز: 0۵۷-۶7 [- فغیاز» بجای بعیاده فغناد |  (۰) بول اندکی که علاوه بر اجرت استاد به  شاگرد دهند؛ شاگردانه. بهای شیر بنی که در  وقت جامة نو پوشیدن بخش کنند؛ بول  شتریتی امژده) وید   بعیض: ۵-ضبهه [ع.] (ص.) دشمن داشته»  دشمن روی.   بفیه. 03 [ع. بغیه ] (ا.) آرزو» خواهش»  دلخواه.   بسفتری: 187-1-]02 (امر.) دفستین؛ افزار  جو
### MON_part2.txt انجیل 1
   ... .) وضع کننده» مقرر  دارنده. سازنده» موجد. آفر بننده» خالق.  آنکه در میان مردم قوانین و احکام پدید  آرد؛ شارع؛ ج. واضعین. واضع چهار (چار)  کتاب: (کد.) حق تعالی که صحف را بر  ابراهیم» تورات را بر موسی؛ انجیل را بر  عبسی و قرآن را بر محمد(ص) نازل ساخته.  (بعضی بجای صحف. زبور داود را نام  بررند.)   واعط: ۷22 [ع۰] (افا.) وعظ کننده» بند  دهنده» اندرزگوی» نصیحتگوه ج. (عربی)  واعظین» وعاظ. ,۱   واعی: [۷3 [ع.] (افا.) نگاهدارنده حافظ.  شنو نده» گوش دهند ه.
### MON_part2.txt انگلیون 1
   ... د.  الثاً فاقد خصوصیت زئولوژیکی هستند  یعنی هورمون‌های مشابه در حیوانات مختلفه  دارای اثرات مشابه هستند. مثلاً آدرنالینی که  از قسمت مغزی غده فوق کلبوی یک  پستاندار گرفته شود با آدرنالینی که از  پاراگانگلیون‌های سک ماهی‌ها بدست آید  دارای خواص فیزیولوژیکی مشابه هستند»  اخیراً برخی از هورمون را بطور مسصنوعی  نیز تهیه کرده‌اند» ارمون.    هور: 52 (.) آواز تند و تيز مانند صدایی  که از طاس برنجی و امثال آن برخیزد. آواز  (بانک) به هوز افتادن (اوفتادن):
### MON_part2.txt فلوت 6
   ... م.) گازی است زرد  رنگ که به وسیلةٌ مواسان و دوار بصورت  مایع در آمده است و بعداً آن را در شدرژزن  مایع سصورت جامد دراورده‌اند. وزن  مخصوص آن ۱/۳۱ و در منهای ۱۸۷  درجه می‌جوشد و تنفس آن خطر ناکك است.  فلوت: 01 (۰.) (مس.) نوعی نی تکمیل  شتلاه که توف ازویاتان است باس ار  در موسیقی عملی نیز بکار برده می‌شود. با  فلوت به سهولت می‌توان صداهای مختلف  را اجرا کرد ولی چون فاقد برده‌های  مسخصوص موسیقی مااست. نواختن  نغمه‌های ایرانی در روی این ساز مشکل  است
   ... امد دراورده‌اند. وزن  مخصوص آن ۱/۳۱ و در منهای ۱۸۷  درجه می‌جوشد و تنفس آن خطر ناکك است.  فلوت: 01 (۰.) (مس.) نوعی نی تکمیل  شتلاه که توف ازویاتان است باس ار  در موسیقی عملی نیز بکار برده می‌شود. با  فلوت به سهولت می‌توان صداهای مختلف  را اجرا کرد ولی چون فاقد برده‌های  مسخصوص موسیقی مااست. نواختن  نغمه‌های ایرانی در روی این ساز مشکل  است.    فلوت: 1 (ا. ) مجموع کشتی‌های جنگی    فررهنگ فارسی معین    ۱۱۳  یک دولت؛ ناو کان (فر ه.)  فلورن: ۵ (.) قطع
   ... ن است باس ار  در موسیقی عملی نیز بکار برده می‌شود. با  فلوت به سهولت می‌توان صداهای مختلف  را اجرا کرد ولی چون فاقد برده‌های  مسخصوص موسیقی مااست. نواختن  نغمه‌های ایرانی در روی این ساز مشکل  است.    فلوت: 1 (ا. ) مجموع کشتی‌های جنگی    فررهنگ فارسی معین    ۱۱۳  یک دولت؛ ناو کان (فر ه.)  فلورن: ۵ (.) قطعه‌ای مسگ وک  (سابقاً از طلا و امروزه از نقره) واحد پول  در هلند. ضح.- این کلمه در فارسی بصورت  «فلور ی» در آمده.  فلوس: تاه (ع.] (.) (گیا.) درختی
### MON_part2.txt اجاره 10
   ...  معانی نیامده» صحیح به جای ارت ات  منقول. قا بای و دعا با حدیئی که  از زمان‌های دیرین از شخصی به شخص  دیگ ثر رسمده باشد.  مانسوم: ۳ (ع.] (ص.) گناهکار 3  بزه کار.  ماجر: 2 02۵ [ع.] (.) (فة.) آانجه که  اجاره شود؛ مکان اجاره‌یی؛ ج. ماجر.  مأجور: ۱ [ع- ۰] (امف.) اجرت گرفته؛  مزد گرفته؟ چ. .مأجورین.  ماخد: مت [ع. ۰ (.) جایی که از آن    نع کر نله مسلکفا: روش. مسج اساس ؛  ِِِ    موخر: ۲ 0( [ع.] (امف.) عقب افتاده.  (۱.) عقب چیزی؛ مق. مقدم. (نظ.) واحدی  ک
   ... حیح به جای ارت ات  منقول. قا بای و دعا با حدیئی که  از زمان‌های دیرین از شخصی به شخص  دیگ ثر رسمده باشد.  مانسوم: ۳ (ع.] (ص.) گناهکار 3  بزه کار.  ماجر: 2 02۵ [ع.] (.) (فة.) آانجه که  اجاره شود؛ مکان اجاره‌یی؛ ج. ماجر.  مأجور: ۱ [ع- ۰] (امف.) اجرت گرفته؛  مزد گرفته؟ چ. .مأجورین.  ماخد: مت [ع. ۰ (.) جایی که از آن    نع کر نله مسلکفا: روش. مسج اساس ؛  ِِِ    موخر: ۲ 0( [ع.] (امف.) عقب افتاده.  (۱.) عقب چیزی؛ مق. مقدم. (نظ.) واحدی  که در عقب عمده قو
   ... ن    مسمل  2 ۷ : 21054 ( ۱.) کلهی شحات: . غم» اندو ه.    مستانه: (ه 1 -۱۸5۱ (ص. ق.) مانند  مستان؛ همجون فسته,  من هناد [ع. ۰ (افا.) و    منتخب. مختص. متألم. مت غمگین.  مستاجر: را [ع. (امف.) آانجه ند  اجاره داده شو د؛ مورد اجاره.   ی ۱۱۲( [ع.) (افا.) اجاره  کننده» اجاره‌دار. خدمتکار» اجیر (غم.) کسی  که ضرب مسکوکات و ساختن نقده‌ها در  ی 33 وا گذار می‌شد (صفویه)؛  ج. مستأجرین.   میستتاضا : ای ۱۱۱05۱۸ [ع. ۰ (امف.) از بیخ  بر کنده. ريشه کنده. (ف.) بی‌
### MON_part2.txt اجرت 17
   ...  می‌رود. در مراتع بهتر زندگی  می‌کند و به اصطلاح در زمین‌های علفی  می‌چرد. غازهای وحشی بصورت دسته‌های  عظیمی در شمال آسیا و اروپا زندگی  می‌کنند و در زمستان بطرف مرکز اروپا و  اسب و گاهی شمال ایران مهاجرت می‌نمایند.  غاز انواع و نژادهای مختلف دارد و برخی از  نچادهایش در صورت توجه و تغذیة نیک تا  ۲ کبلو وزن بیدا می‌کنند. نژادهای مختلف  غاز عبار تند از: غاز پومر و غاز تولوز و غاز  کلموگوری. تخم‌گذاری غاز ماده در اواخر  پیز است و معمولا" وقتی که ۱۲ 
   ...     فر هنک فارسی معین    ۵ ۱  کار بودن.  فعلات: : تانجا (ع.] (. تن  اعمال.  فعلا «: باه [ع.] (ق ق.) از روی فعل» عملا  حالا؛ | کنون.    نعلگی: آ-(۸:۱۸)۵] (حامص.) فعله بودن  مزدوری» کارگری. کارگری بدون اجرت و  مزد. ضح.- در تداول به سکون عین استعمال  شود و آن غلط است.  فعله: ۰ (0-]1۵1۸ [. . فعله | (  یک بار کردن؛ ج. علات.  فعله: (۵-)۱۸۱۸) . فعله | (افا. ۱.)  کنندگان. کار گران؛ : عمله. (  گلکار (مفرد گیرند.)  ‌ دوم استعمال شود و صحیح نیست  (ایضا).  ف
   ...  اهنجاری است. برهای  آن اکثر سفید است ولی در استرالیا گونه‌های  ۱0  تا حدی سفت است و بنابراین چندان مطبوع  و مورد توجه نیست. در فصول سرد این  پرنده از نواحی شمال به طرف مناطق گرم  آفریقا و هندوستان مهاجرت می‌کند و گاهی  هم در زمستان‌ها در نواحی ؛ بحر الرومی باقی  می‌مأند و در کنار رودخانه برای خود لانه  تهیه می‌کند.   قواد: ۵ (ع.] (ص. ۱.) کسی که و اسطة  شهو ترانی دیگران است؛ دیوث» قرمساق.  قواره: (ند. 62۷816) ۲۷5۲3۵ [ع. قوارة] (.)  بارچه‌ای که گر
```


## [2026-09-04T18:35:11.270Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nimport re,os\ndef show(f,pats,ctx=280,limit=2):\n    if not os.path.exists(f): print('MISSING',f); return\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pg=t.split('\\f')\n    for pat in pats:\n        n=0\n        for i,p in enumerate(pg):\n            for m in re.finditer(pat,p,re.I):\n                n+=1\n                if n>limit: break\n                print(f'@@ {os.path.basename(f)} /{pat}/ leaf{i}: '+p[max(0,m.start()-ctx):m.start()+ctx].replace('\\n',' '))\n            if n>limit: break\n        if n==0: print(f'-- {os.path.basename(f)} /{pat}/ : SILENT')\nprint('===== SKT =====')\nshow('SKT.txt',[r'\\bAngel\\b',r'\\bAloes?\\b',r'\\bLute\\b',r'\\bFlute\\b'])\nPY",
 "description": "grep Skeat"
}
```


### [2026-09-04T18:35:13.394Z] TOOL RESULT

```
===== SKT =====
@@ SKT.txt /\bAngel\b/ leaf32: (Gk.)    SeeAnJmal. Anent,  rcRaiding.  (E.)     See  Sven. Aneroid,  dry.  (Gk.)    See  Nereid. Aneurism,  a  tumour  due  to  dilatation. (Gk.)  Gk.  iv^vpvcfta,  a  widening. —Gk. Av;  for  (li-u,  up;  and  tvpvrur,  to  widen, from  (L'piJr,  wide. Anew.  C£.)    See  Now. AngeL  (L.  -  Gk  )     L.  attfrfius.  -  Gk. i£7-y«Aoi,  a  mcisciigcf.     Cf.  Gk.  (Syyn^or,  a ted  courier,  from  O.  Persian.     Dor. rch-anffti,  q.  v.,  tv-an^l-ist,  q.  x. Anger.  (Scand.)  M.E.  artnr^  often with  the  sense  of  vexation,  trouble,  •IceL OHgr^
@@ SKT.txt /\bAngel\b/ leaf606: e. CORRECTIONS   AND   NOTES. [Some  of  the  etymologies  given  io  the  preceding  paces  will  re<ioire  m whcD  the  history  of  the  wordi  treated  of  l>ccomc»  marc  accurately  known, such  corTection&  und  improvements  as  have  hitherto  occurred  to  me. — W.W. I Angel.  The  A.S.  form  ia  tn^I,  from Latin.  Afietwards  altered  by  F.  and  I* influence. Anneal  Perhaps  the  A.  S.  words  should be  pmklan  aud  ^Um^  with  long  dT.  Vet  sec l^'ick,  i.  loo. Baokgammon.  Stmtt  suggests  that. after  all,  this  word  merely  mea
@@ SKT.txt /\bAloes?\b/ leaf274:   Ugioe, lights  ;  from  Ugkii,  light Xii^hten  (1),  to  flash.  Ughtning ;  see Light  (I). Xiigneous,  woody.  (L.)  L.  Ji^Jteus, wooilt'ii.  — L.  ii^rtuM,  wood, Ugn  aloos.  a  kind  of  tree.  (L.a»^Gk.) A   sort  of  translation  of  L.  H^num  aloti, liL   'wood  of  aloes.*      Aloes   is   gen.   of a/<(V.  from  Gk.  dAvf},  aloe.     See  AJO0. Iiigule ;  see  LiogiuiL Liguro.  a  precious  stone.  (L.  *Gk.) L.  Itptrius.^^V. 
@@ SKT.txt /\bAloes?\b/ leaf274: ts  ;  from  Ugkii,  light Xii^hten  (1),  to  flash.  Ughtning ;  see Light  (I). Xiigneous,  woody.  (L.)  L.  Ji^Jteus, wooilt'ii.  — L.  ii^rtuM,  wood, Ugn  aloos.  a  kind  of  tree.  (L.a»^Gk.) A   sort  of  translation  of  L.  H^num  aloti, liL   'wood  of  aloes.*      Aloes   is   gen.   of a/<(V.  from  Gk.  dAvf},  aloe.     See  AJO0. Iiigule ;  see  LiogiuiL Liguro.  a  precious  stone.  (L.  *Gk.) L.  Itptrius.^^V. 
@@ SKT.txt /\bLute\b/ leaf286: a  period  of  tive  ycar&, every  Ave  yeara  a  lustrum  was  per The  orig.  seme  is  *a  porificaliooj /wrr.  allied  to /awarf,  to see  I^ave. lustration,  a  purificatioa (L.)    From  L.  Imtratio.  an L.  lustrtstus,  pp.  of  lus/rart, L.  lujfrum,  an  expiatory  sac Lute  (1),  a   musical    instrai Arab.)  M.E. /«iy.-F. /w/ ^Cotgi F.  luiA.  We  also  find  Prov.  /au/, ; Port  a/auJit  Ual  liuta,  Du. .y.  *' L  mei ^^ lusd ta,Dt 1 LUTE. h.     The  Port,  form  ihewi  the  Arab. I  liDce  «-  is  for  al,  the  Arab.  def. UbV  V</,  wo
@@ SKT.txt /\bLute\b/ leaf286: atioa (L.)    From  L.  Imtratio.  an L.  lustrtstus,  pp.  of  lus/rart, L.  lujfrum,  an  expiatory  sac Lute  (1),  a   musical    instrai Arab.)  M.E. /«iy.-F. /w/ ^Cotgi F.  luiA.  We  also  find  Prov.  /au/, ; Port  a/auJit  Ual  liuta,  Du. .y.  *' L  mei ^^ lusd ta,Dt 1 LUTE. h.     The  Port,  form  ihewi  the  Arab. I  liDce  «-  is  for  al,  the  Arab.  def. UbV  V</,  wood,  timber,  a  KtafT.  stick, of  Uoefi.  lute,  m  harp. I(j).  tkiijdofloaiii.  (F.-L.)    O.F. vf,  loun.*  L.  iutum.  mod.  thit  which }cd  down.  ••X./v/'Y,  to  wa
@@ SKT.txt /\bFlute\b/ leaf174: Plagstone,  a  paving-stooe; see  Fl&ke. Flagellate.  (L.)  From  pp.  of  U fiagtUart^  to  scourge.  ^'L.Jtarelium.  dimin. of Jtagrum,  a  scourge,     {y  nllLAG,') flalL  (F.  - L.)    O.  F.  /«/  (F.  jTMu), a  flail,  scourge. —  L.  fiagellum  (above). Flageolet ;  see  Flute. Flagitloua.  <L.)    h.  Jfagt'/iosHs,  ^hmnc- ful.  V  \^  jiagitium,  a  disf^raceful   act,  ~L. Jta^itare.  to  act  with  rioleooe.     Allied  to Flftgrruit. Flagon :  ace  Fl&ak. Flagrant,  glaring,  as  a  fault.  (F.^L.) O.  F.  ftogrt^t^  pioperly  burning.  —  L
@@ SKT.txt /\bFlute\b/ leaf177: ed  form  of fioMUrtn,  to  dangle,  flap,  sjilnsh  fhr( mire.     Cf.  Swcd.yf<w^f0;  to  flutter. Flounder  (a),  a  fish    (Scaitit)    S ftuiuirtt,  Dan.  Jtyndtr.  \QfA.JIy^t%.    Pt< frcffn  flouuJet-itt^  about ;  see  above, Flour,  Flourish ;  «ec  Floral Flout,  see  Flute. Flow,  to  stream  (£.)    A.  S.  tfL^«4«. Du.  vhiijen  ;  Iccl./PAr,  to  fi<~- ii  rains;  Rnu. //wr/r,  to  float Skt. /Ah,  to  iluac^  swim.    ( yi'UJ  j FLOWER. .)  A.  S.  JUd^  %  flood ;  from reV  +  Pa.  vUtd,  Icel.  Jl^^d, Goth.  jUdus^  %  river,  G. f«e71
```


## [2026-09-04T18:35:16.071Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nimport re,os\ndef show(f,pats,ctx=300,limit=2):\n    if not os.path.exists(f): print('MISSING',f); return\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pg=t.split('\\f')\n    for pat in pats:\n        n=0\n        for i,p in enumerate(pg):\n            for m in re.finditer(pat,p,re.I):\n                n+=1\n                if n>limit: break\n                print(f'@@ {os.path.basename(f)} /{pat}/ leaf{i}: '+p[max(0,m.start()-ctx):m.start()+ctx].replace('\\n',' '))\n            if n>limit: break\n        if n==0: print(f'-- {os.path.basename(f)} /{pat}/ : SILENT')\nprint('===== LKT =====')\nshow('LKT.txt',[r'al-?.?ud',r'\\bLaute\\b',r'agaru',r'Aloe'])\nprint('===== AFA Fraenkel =====')\nshow('AFA.txt',[r'agara|aggara|\\bagir',r'\\bfid\\b|\\b.ud\\b'],limit=1)\nprint('===== AFM Addi Shir =====')\nshow('AFM.txt',[r'عود',r'انجيل'],limit=2)\nPY",
 "description": "grep LKT AFA AFM"
}
```


### [2026-09-04T18:35:17.983Z] TOOL RESULT

```
===== LKT =====
@@ LKT.txt /al-?.?ud/ leaf53:  nannt; in  sie  werden  die  Arekanüsse [s.  hier  Nr.  17]  mit  Kalk  eingewickelt und  so  in  ganz  Südasien  als  Narkotikum, ähnlich  wie  bei  uns  der  Kautabak,  viel benutzt. 319.  Ar.  bittiha: 'Wassermelone',  Demin.  dazu  huttaiha; hieraus  z.  T.  mit,  z.  T.  ohne  ar.  Art. kat.  albudeca,  pg.  aibudega,  pateca,  sp. pg.  badea,  aprov.  albuesca,  npr.  aubieco, frz.  pastlqiie  'Wassermelone'  [dies  trotz Wartbg  FEWb  61  und  288;  das  dort angegebene  mal.  bateka  existiert  wohl kaum],  [DE  74  und  232.  Eguilaz  119. Hobson-Jobson  684/685.    ML  1136. .320.  
@@ LKT.txt /al-?.?ud/ leaf147: rei  als  'tributarius'  erklärt  wird). 1490.  Ar.  mndd: 'Getreidemaß'  [Lammens  Fartlk  Nr.  1242 ; im  'Irak  2  1,  im  Higäz  l'/s  1,  sonst  1,76  1 fassend;  aus  lat.  medium,  gr.  liobiö?, die  beide  semitischen  Ursprungs  sind, vgl.  hebr.  mad  'Maß'];  hieraus  mit  ar. Art.  sp.  almud,  kat.  alrnut,  pg.  almude, frz.  almoude,  almude  'dass.'.  [DE  180. Eguilaz  239.  Devic  DEt  26.  ML  5625. Lammens  Rem.  18. 1491.  Ar.  luuflis: 'ßankrottierer'  [part.  praes.  act.  vom Vb.  falasa  IV  'bankrott  machen',  dies von  ar.  fals,  plr.  fulüs  'Geldstück' gr.  qpöUi
@@ LKT.txt /\bLaute\b/ leaf43: poln. balkon,  6ech.  bulkön.  —  Auf  direkterem Wege,  höchstens  über  tat.  bälahane  ist russ.  balagan  'Marktbude  aus  Brettern, Schaubude'  entstanden.  —  Andere  Ab- leitungen s.  DE  60.  Eguilaz  97.  ZfromPh V,  244;  XXX,  557.  [Gorjajew  9  u.  10. ML  890. 198.  Tat.  balaliiika: 'Laute' ;  hieraus  russ.  h
@@ LKT.txt /\bLaute\b/ leaf44: alalaika,  klr. balabaika,  serb.  balalajka,  öech.  bala- lajka  'russische  Zither  oder  Laute  mit zwei  oder  drei  Saiten' ;  frz.  la  balale'ika, dtsch.  Balalaika.    [Gorjajew  10. 199.  Mongrol.  balamnt: Hieraus  russ.  balamut,  öech.  balanmt, poln.  balamut  'Schwätzer,  Klatsch  er' ; Tum.  balamut  'dumm'.  Dazu  auch  Verba: russ.  balamutit' ,  Cech.  balamutiti,  poln. 
-- LKT.txt /agaru/ : SILENT
@@ LKT.txt /Aloe/ leaf137: lgaiu: 'Erweichende  Salbe'  [aus  gr.  |id\aY|ua mit  Metathesis];  hieraus  sp.  pg.  kat. amalgama,  frz.  amalgame;  engl,  aniaf- gam,  Vb.  amalgamate,  dtsch.  Amalgam, Vb.  amalgamieren;  russ.  amal'gama [und  über  tk.  melhem,  ebenso  tat.]  mal  - han,  bulg.  mehlem,  serb.  meiern  'Saloe'. —  [Devic  DEt  29/30  und  Eguilaz  256/257 geben  andere  unhaltbare  Ableitungen, Lammens  Rem  21/22  spricht  schon Zweifel  daran  aus;  die  hier  gegebene Etymologie  deutetschonGorjajew201  an]. 1379.  Araiii.  itialka: 'König' ;  hieraus  gr.  Md\xo?.  lat.  Malchus ['der  Königlich
@@ LKT.txt /Aloe/ leaf155: daja,  poln.  oda  'Zimmer'. 1585.  Tk.  öd  agagy: 'Wohlriechendes  Holz'  [von  öd  'Galle' vom  Stamme  ol,  ög  'Zorn,  Eifer'  <^ 'Feuer,  brennen'  in  flg.  Bedeutuug, Vämbery  TktEtWb  S.  51,  S.  56,  und  agag 'Baum'  in  genitivischer  Verbindung]; hieraus  rum.  odogacm  'Seifenkraut,  Aloe- holz'. —  [Es  liegt  wohl  schon  im  tk. Grundwort  Kontamination  mit  ar.  'üd, s.  hier  Nr.  2127,  vor.] 1586.  Tk.  odalyk: [Aus  oda  'Zimmer',  s.  hier  Nr.  1581,  und Suffix  lik,  also  wörtlich  'Frauenzimmer' wie  im  Dtsch.]  'Sklavin  der  Harems- damen'; hieraus  in  wesentl
===== AFA Fraenkel =====
-- AFA.txt /agara|aggara|\bagir/ : SILENT
@@ AFA.txt /\bfid\b|\b.ud\b/ leaf13: ls ich dieseiu meinem hochverehrten Lehrer zu danken habe. Von ihm habe ich ilie erste An- regung zu diesen Studieu empfangen, von ihm gelernt, dass der wahre Philologe an Wörtern und Sachen gleiches Interesse nehmen muss, ihm verdanke ich die Kenntuiss iler Methode, uach «ler ich gearbeitet habe. L'ud als ich nicht mehr zu seinen Füssen sitzen durfte, da hat er in einem jahrelangen uuunterbrocheuen Briefwechsel diesem Buche, das er werden sah, stets den wärmsten Autheil ge- widmet; jeden wichtigen Fund durfte ich ihm mittheileu und mich seiner Zustimmung freuen, wie ich umgekehrt durch seine 
===== AFM Addi Shir =====
@@ AFM.txt /عود/ leaf0: لثار. وآذر يون اغة فيه ± ` 096( حيجكى ( زهر القمر )  وقره كز ( العين السوداء )   3( الأرجان ) ,شر 4033( :3( 600390550901017 ا  ارجن وهو الفستق البري وقيل الاوز المر واسمة 6 9 اي لوز الل  ( الترهان القاطع )   590 معرب )6.35 وهو سّحر له ورد 0 به 0  ويطلق 9 على 0 حمر والشاب الخمر والصبغ الأخر ٠وقيل‏ 0 عوده اذا احصارق  تفع لاإننات ܚܟ .ܕܟܕ بالارامية ܐܪܥܘܝܐܝ ܙ( 5 6( و 6 1  اللفظة سنسكر ܝܬ 10 ܐܦܬ نه من 5282 اي احمر ومن 724 وهى اداة  النسة ( القاموس العبرالي الكلداني تأليف جسنيوسء ضن : + ) (4) :   الأوارجة ) 5755 جسات الدخل والخرح يدون 3 )ا 1  مسدنّا من حسابات الديوان   + ( الأرش ) ما 'يدفع بين السلام
@@ AFM.txt /عود/ leaf0:  بالسر ܬܒ وهو  اسود :ܠ جوذة الطيس ٠‏ يقال له ( 039 ححر الولادة ܝ الذسر وحجر  العا ٠١و‏ بالتركية « 1 طاثى وطوشتحل تظائق »© وتيختالاه افع لعسر الولادة  وتعلقة على ܐ( ينع تساقط الاكثر.» “قلت أو ܦܘ ܀ :111 لصبت سواانة يكل  ܨ إما ܠ 1 0  3 ܝܫ الشديدة من شدائد الدنيا تعريب آك وهما عمنى   0 ®+ ,|11 ,)7 5) العود 0 ) ܡܳܐ به . .قال الاصمعي ذهو فارسني  معرب ٠‏ قلت 9 13( الصبزء قال الاب 5 50 0507  قلت : والموثافى في ماخوذ من | ܕ لان 5 اصله من بلاد 0935 0  )ܒܨܢ 210 والفرني 0105 والاتكليزي” 5 موالايطاليالي 31 010   ( الأماج» الغرض وهو في اصله الفارسي نبشان السهم الموضرع على كرمة من  ܨ ومنة اتكردي آما نج   * (
-- AFM.txt /انجيل/ : SILENT
```


## [2026-09-04T18:35:35.488Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nimport re,os\ndef show(f,pats,ctx=320,limit=1):\n    if not os.path.exists(f): print('MISSING',f); return\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pg=t.split('\\f')\n    for pat in pats:\n        n=0\n        for i,p in enumerate(pg):\n            for m in re.finditer(pat,p,re.I):\n                n+=1\n                if n>limit: break\n                print(f'@@ {os.path.basename(f)} /{pat}/ leaf{i}: '+p[max(0,m.start()-ctx):m.start()+ctx].replace('\\n',' '))\n            if n>limit: break\n        if n==0: print(f'-- {os.path.basename(f)} /{pat}/ : SILENT')\nprint('== SKT aloes ==');  show('SKT.txt',[r'Aloes,\\s|Aloes\\.'],limit=2)\nprint('== FSD vol1 ==');  show('FSD_vol1.txt',[r'aloe,? n\\.|\\balo.,? n'],limit=2)\nprint('== WEB ==');  show('WEB_vol1.txt',[r'\\[.*al-?.ud'],limit=3)\nprint('== DEV ==');  show('DEV.txt',[r'ALO.S|LUTH|aloès'],limit=3)\nprint('== HJB ==');  show('HJB.txt',[r'AGALLOCHUM|EAGLE-?WOOD|aguru'],limit=2)\nPY",
 "description": "grep SKT FSD WEB DEV HJB"
}
```


## [2026-09-04T18:35:37.447Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nimport re,os\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npg=t.split('\\f'); print('AFM leaves',len(pg))\nfor i,p in enumerate(pg):\n    if 'العود' in p or 'عود' in p:\n        for m in re.finditer('العود',p):\n            print('@@ leaf',i,':',p[max(0,m.start()-500):m.start()+600].replace('\\n',' '))\nPY",
 "description": "grep AFM pages for al-ud"
}
```


### [2026-09-04T18:35:38.728Z] TOOL RESULT

```
== SKT aloes ==
@@ SKT.txt /Aloes,\s|Aloes\./ leaf274:     lightneu.      So    aIso    Ross.    Ugioe, lights  ;  from  Ugkii,  light Xii^hten  (1),  to  flash.  Ughtning ;  see Light  (I). Xiigneous,  woody.  (L.)  L.  Ji^Jteus, wooilt'ii.  — L.  ii^rtuM,  wood, Ugn  aloos.  a  kind  of  tree.  (L.a»^Gk.) A   sort  of  translation  of  L.  H^num  aloti, liL   'wood  of  aloes.*      Aloes   is   gen.   of a/<(V.  from  Gk.  dAvf},  aloe.     See  AJO0. Iiigule ;  see  LiogiuiL Liguro.  a  precious  stone.  (L.  *Gk.) L.  Itptrius.^^V. 
== FSD vol1 ==
-- FSD_vol1.txt /aloe,? n\.|\balo.,? n/ : SILENT
== WEB ==
@@ WEB_vol1.txt /\[.*al-?.ud/ leaf50: silas, from adversus, pp. of adverlere, to oppose.] 1. misfortune; calamity; affliction; distress; state of unhappiness. Sweet are the uses of adversity. —Shak. 2. an instance of misfortune; a calamity. Syn.—disaster, misfortune, calamity, bad luck, misery, distress. ad-vért’, v.i.; adverted, flr, pp.; adverting, ppr. [L. advertere; ad, to, and vertere, to turn.] to turn the mind or attention; to refer or allude (to something); as, he adverted to what was said, or to a circumstance that occurred. ad-vért’ence, ad-vért’/en-cy, n. [OFr. adver- tence; L. advertentia, from advertens, ppr. of advertere, to turn to.] a direction of the mi
@@ WEB_vol1.txt /\[.*al-?.ud/ leaf282: ra-phist, ca-lig/ra-phist, 7. a callig- rapher. r cal-lig/ra-phy, çå-lig'rå-phy, n. (Gr. kalli- graphia, irom peers pees ne beautiful, and graphein, to write. : he 1. beautiful or expert handwriting. K My calligraphy, a fair hand Fit for a secretary. 2. handwriting. way. to call off; (a) to divert; to summon away; (b) [Colloq.] to cancel a proposed or promised event or function; to revoke; (c) to read aloud from a list or enumeration; as, to call off the names of the eligible candidates. to call on; (a) to visit briefly; (b) to ask (a person) to speak. to call out; (a) to speak aloud; to shout; (b) to challenge, as to a fight; (c) t
@@ WEB_vol1.txt /\[.*al-?.ud/ leaf363: layed by means oi holes and keys: it is made in various keys, and has a range of about 3!/:octaves. clar-i-net/ist, clar-i-net’ tist, n. a person who plays the clarinet. cla-ri/no, n. [It., from L. clarus, clear.] a four-foot organ stop having reed pipes that sound like a trumpet: also written clar- tOn. clar’i-ðn, n. [ME. clarioun; pne perin; LL. clario, a trumpet; L. clarus, clear. 1. a kind of trumpet producing clear, sharp, shrill tones. 2. the sound of a clarion, or a sound like this. [Poetic.] clar/i-6n, a. clear, sharp, and shrill; as, a clarion call. i clar’i-6n, v.t. to announce forcefully or loudly. $ clar”i-6-net’, n. sam
== DEV ==
@@ DEV.txt /ALO.S|LUTH|aloès/ leaf31: KEFO.  C'était  autrefois  le  nom  d'une  monnaie  qui avait  cours  en  France.  En  portugais,  xarajîm,  xerafim,  dé- signe une  monnaie  des  Indes  orientales,  que  Baumgar- ten,  au  commencement  du  xvf  siècle,  appelle  en  latin seraphi.  C'est  l'arabe-persan  j,y»ii  achraji  ^anoneta?  aureae genus,  valons  vn  reaies  hispanicos^?  (Vullers).  Le  mot semble  formé  de  oyit  achraf,  très-illustre,  comme  son synonyme  <^va^î  ahhen,  de  ^3^  akhar,  très-grand.  On  peut voir  sur  le  j^^r^m  l'article  du  Gloss.  de  M.  Dozv,  p.  353, 35A. Si  aigrefin,  monnaie,  vient  de  achraji,  il  ne  serait  pas 
@@ DEV.txt /ALO.S|LUTH|aloès/ leaf33:   oit  Perso ,  i).  '2\(),  2ii0,  édit.  Sniilli.)  Voir  aussi le  curieux  article  Pelirano,  dans  le  Gazophyl.  livg.  Pci'n. DES  MOTS  D  ORIGINE  ORIENTALE.  7 Alboucor.  Li(|iicur  qu'oii  retire  de  l'arbre  de  l'encens, i  Bosc,  Dict.  dliisL  nat.^  C'est  l'arabe  )y^^  al-houkhoûr, encens,  bois  d'aloès,  et  en  (général  parfum  à  brûler.  El- Hous  Bocthor  (^Dlct.  fr.-ar.,  au  mot  encens)  redouble  le  ^ A7/.  En  portugais,  par  la  transformation  si  fréquente  du  ^ kh  en  /",  le  mot  arabe  est  devenu  alhajor,  encens,  parfum. Alcade.  Esp.  «/crt/r/e.  De  l'arabe  ^^UJî  al-qâd'i /^u^e  i^
@@ DEV.txt /ALO.S|LUTH|aloès/ leaf68: e  la  queue  du  Cy- gne; en  arabe,  o:>JI  ar-ridf,  mot  qui  signifie  celui  qui  suit, celui  qui  vient  après.  (Voy.  Rédif,  au  mot  Nizam.  ) 1  5.  Asangue,  la  constellation  de  la  Lyre;  en  arabe, .^^o^î  as-sandj,  qui  est  probablement  une  altération  du  ^qy- sdLXi  3^j^=s^  tcheng ,  harpe,  luth. i6.  Aschémie,  l'étoile  Procyon;  en  arabe,  ^^UJi  ach- clulmi,  le  Syrien,  ^^UJI  <.^yt*«Ji  ach-chtra  ach-cltâml,  Sirius de  Syrie.  (Voy.  Aliémini,  ci-dessus.)  L'e  final  de  aschémie montre  que  le  mot  a  été  fait  sur  le  féminin  <XA-«UiJi  ach- châmia. 17.  Aschère,  Sirius.  C'est  l'arab
== HJB ==
@@ HJB.txt /AGALLOCHUM|EAGLE-?WOOD|aguru/ leaf22: which  would connect  it  with  the  Ophir  trade  of  Solomon,  we  find  no  existing  Western term  traceable  to  that  episode  of  communication  ;  but  the  Greek  and  Roman commerce  of  the  later  centuries  has  left  its  fossils  on  both  sides,  testifying to  the  intercourse  that  once  subsisted.  Agallochum,  carba^us,  camphor, sandal,  musk,  nard,  pepper  (Wire/w,  from  Skt.  pippali,  *long  pepper'),  ginger (^tyyi^pis,  see  under  Ginger),  lac,  costus,  opal,  malabathrum  or  folium  indicum, beryl,  sugar  {adjcxap,  from  Skt.  sarkara,  Prak.  saJdcara),  rice  (Upvia,  but  see  s.v.), were  pro
@@ HJB.txt /AGALLOCHUM|EAGLE-?WOOD|aguru/ leaf26:   less  violent,  of  Oriental  words and  phrases  which  have  put  on  an  English  mask.  Such  are  maund,  fooVs rack,  bearer,  cot,  boy,  belly-band,  Penang-lavjyer,  buckshaw,  goddess  (in  the Malay  r^on,  representing  Malay  gddts,  *a  maiden'),  compound,  college* pheasant,  chopper,  summer-head,*  eagle-wood,  Jocfco^^-copal,  bobbery.  Upper  Roger (used  in  a  correspondence  given  by  Dalrj'mple,  for  Yuva  Raja,  the  '  Young King,'  or  Caesar,  of  Indo-Chinese  monarchies),  Isle-o^-Bats  (for  Allahabad  or Ilahdbdz  as  the  natives  often  call  it),  hobsorirjohson  (see  Preface),  St  JoMs^ The
```


### [2026-09-04T18:35:40.656Z] TOOL RESULT

```
AFM leaves 198
@@ leaf 13 : 83 0 الى 500 937 :ابن 55[ 37 39093 .1.3 ܐܨܦ القاطع : « اكت مكت بكسر الكافين ضرب من !ܐܝܢ بالسر ܬܒ وهو اسود :ܠ جوذة الطيس ٠‏ يقال له ( 039 ححر الولادة ܝ الذسر وحجر العا ٠١و‏ بالتركية « 1 طاثى وطوشتحل تظائق »© وتيختالاه افع لعسر الولادة وتعلقة على ܐ( ينع تساقط الاكثر.» “قلت أو ܦܘ ܀ :111 لصبت سواانة يكل ܨ إما ܠ 1 0 3 ܝܫ الشديدة من شدائد الدنيا تعريب آك وهما عمنى 0 ®+ ,|11 ,)7 5) العود 0 ) ܡܳܐ به . .قال الاصمعي ذهو فارسني معرب ٠‏ قلت 9 13( الصبزء قال الاب 5 50 0507 قلت : والموثافى في ماخوذ من | ܕ لان 5 اصله من بلاد 0935 0 )ܒܨܢ 210 والفرني 0105 والاتكليزي” 5 موالايطاليالي 31 010 ( الأماج» الغرض وهو في اصله الفارسي نبشان السهم الموضرع على كرمة من ܨ ومنة اتكردي آما نج * ( الاإمدان» | على وجه الارض تصحيف 1 دان ومعناه الغدير + (الأمد) يقال ما أمدك 35 5 7 امد ومعناها الزمنان ܢ ' 1 0 والاميض) طعام ܣ من حلم عجل مجلده او مرق السكماج :7 1 ن الدهن معرب خأ ميز ܙܘ ايضا ܐܐܝܟ ܠܐܠ ܐ ܡܝܢ + يكن باللغة الربانية ( )ܠ ܙܕ والأندَروَديّة ) اسم لنوع من السراويل مركب من اندّر اي داخل ومن ور اي
@@ leaf 19 : :9 ` - من 9 3 ظاهر. والاصح انْ 45 3 13 الخمر والنمذ (البدنوز): معرات كه بوذ وهو احتبيث ܝܘ ( البربط ) العود تعريب برت واصل معناه صدر ܐܠ( لاله يشبهة ٠‏ ومنة اليونائي ومجمةامهة * (البربيطاء ) الثياب معرب ܨ ܢܝܐ ومعناها الصدربة وهي ثاب يلسها اللا ناك والنساء * على صدورهم * ( الت ) بعنى الدليل مشتق من ب تو ومعناة الضياء (البَرَنتَ ) السئ الخلق تعريب بَرتني ومعناه الغرور والعجب < * 3 الإبريج ) 45 بها 5 السّمن منها < ابيز واصل ܘܚܐܘ يصب الماء و يطآق على الدلو والسطل وغير ذلك + 5 سفيعة كيرة 512 ان = 7 95 عن اركاء 35 بلاط اللك والمضرب 50 وحطة الرحال اوعن بركرك اي قصر عال ٠او‏ الارجح ܣ 05225 غرض في الهواء على رأس رمح او نوه فارسيتها برجاس ومعناما هدف السهم ܬ اصل اللفظة يونالي 90 0 ( البرجس ( نم او هو الش
@@ leaf 22 : ائينة 1 وبالفرنسة 12 0 ® 8 وبال تكايزنة 6 ܙ باطرمانة 111 ܦܘܪܦܝܪܗ ܕ ܦ ܪܦ ܪ̈ܐ ¦ الريامة وال 3 4 0( 7 بره وده ارق 46 ܒܪܚܐ وهذا يطلق ء 501 63007 5 - وهو ܨ ܫ 7 نك واضل تناه 030 ܥܢ (اليَرَم) علّة وابيض 0 و( البرهرهة) 31 ܟ السيضاء )20 7 3 )< ܨ بره ܚ̈ܝ الراء وظهور الهاء ومعناه احلسن الناعم الحميل » ( اليرهان) ܥܫ والدليل ٠‏ قال الخليل : البرهان ببان !ܥܫ وايضاحها من ܐ ܦ ܩܬ ܛ ܐ &4 او من البرهة لشاته ٠‏ قات 504 بروهآن ا الواضح الظاهر المعاوم (البروّاز) م تحبط بالشيء 1 > كبرواز الصورة تعر يبا برواز 0 السهم والعود ܗ ܨܚ معنى 9 (التروائة ) حاجب املك مركب من ' بر اي باب ومن بان اي حافظ + (اليزد ) 0 ْوَاعْ وهو تمد السيف + ` كل ܝܝ الال للنبات تعريب برز 0 7 3395 الارائي ܒܙܪܐ (الميْرّار) عمنى الأكار ابت بان باويوه راك يف برزيار 79
@@ leaf 28 :  110 1 وهو الذى يقال | 5 53- وطرثوة. وقال 7 ` 2 رمان لهند . وقال بعضهم هو الخبار المندي وهو المعروف عند الاطاء طرثوث رب الأرض ولت ٠‏ الرياح. 10 4 با ܠ « قولغان ܕܨ ¢ وهو نماث 0 الارض أخر 80 ܝ كالورق لللدوفت اط فك ت نبات ܝ ܒ في الاغاب ܨ مه 5[ وهر ايا افع من الإرستهالر لان الدم ْ 3 ّ 0056 ܟܣ 95 3743 9 الاثم وهو مفعول مطلق مصاغ من بالا الذى ܘܫܘ الرفيع ܐܬܶܢ والطويل + (الملهور) تعر يب بالاور 3 لكان الواسع + (المليكج ) شجر في حجم الزيتون 8 قريب الطبع ٠‏ ن الأملج 100 4 الاقطار ܐܬ تعر بب بليله اليم ) من العود اغلظ اصواته او القرار او |( ܟ الغليظ من أوتار |[ ܦܨ معرب بأم وهو : الغليظ من أوتار الآلات (1 ® ( )ܐܗ نمت مسبت رضت ]لسن ص يه 3 )ܕ : 37( الت ١‏ الاصل نعريت 'بنك وهو تضغير 33 ܙܪܫܐܐܘ .ܠ ܝܐܝ !¥ ܩܝܐܼ܇ ( ܐܝܫ ̈ܝ ) ` كنت بق المواضع ܐܨ ܢܬ من المماه واغصانه صلبة وورقه اررق ار ديل ارك نع انكفت ܕܐܝܐ + أصابع ويقال له 9 « بش بارماق وايد 39 » وبالعريّة ذو حمس اوراق وذو س أصابع وليه حب الفقد ْ قيل ان حبَهُ ينفع ن ]عله الاستستاء ܇ (الببعان القاطع ) ( المنحكشت ) فاسي محض وهو القرتقل ٠‏ والق رنمل تعر نب 70.007 1000100010 (النْد) العلّم الكبير والميلة ومن المدش عشرة لاف ومن ܐܢ الفصل او 30 3 09 43 ܥ 73 ند وال
@@ leaf 74 :  دواء يشبة الثوم فارسي ( يط امحيط) ول ܪ 6 من" 0 الكتسة مأخوذة من رأء اي الطيب !ܥ 4 8906 9 راموذ وهو الربان والفاسي مسأخوذ من ܨ ` 3 ودعئاه م 0 البحر فاصله حبثي ` 4116[ ( ܝܢܝܐ ص 3 1 ܒܫ 57 ذ الميكة ) اشر اعالارذونة تسعد للنسل ٠قال‏ في شفاء الغليل : 9 0 ܐܪܝ مغرب ±( “قلت رهي ܐܨ ܢ رمكا بالفارسة ܬܐ ܕܘܫܐ )ܬܐ الفرس وقد سق 1005[ سية والقطيع وما ن ان الفارسي. رمك مأخوذ من ܪܡܟܐ * (الرانج» فارسي حض وهو مر املس كالتعضوض -( المددي عد (الرَأند) شجر طَيَب الرانحة من سجر البادية دقل هو الا ܝܨ¿ ܪܝܐ[ الفار وقد قبل العود الذي ' 9 به في الصحاح : قال الأصيي ورم شِجوا إل كه وإني” ان يكون الرند الا ٠قلت‏ ܢܬܪ فاسي ܕܘܐܘ الطيّب | ارائحة ويطلق على 0 ܀ ܙ
@@ leaf 110 : )< * ¥ الذي لا يعرف ( 9003 عن @9 ومعناه:الفاسق العاهر )ܝ 0 معرب دمن بتقديم النون على اليم ومعناهُ عابد الاصنام ٠‏ وما فرنتكل ( ܩ :¥ ) فيقول اله ܟ ܝܢ ܨܠܡܐ ( اليد ؟ عمنى الاميذ معرب ( ܐܢܫܐ َّ الغليل ܀ وهو سهبد ܐܐ ܕܚܐ ܕܝܬ )ܘ >> 0 1 :> ومن بد لي 5 ( الصهر ؟ 2 بنت الرجل وزوج اخته 4 ܒܒ وهو روح | 3 ( )ܐܟܟ والصوطانة » العود المعوبع تعريب جوكآن ومنة اسريافي ܨܘܠܓܢܐ ( راجع ايضأ فرنتكل ܩ : \ ¥ ) والكردي ܗ : * (الصيدانة ) الغول والسرّئة الخاق ܟ 3 من ܚܐܘ اي أسود ومن دان وهي اداة تدل على 5 ® + (الصيف) ܐ سبيد بر بحذف شطره ܠܥܐ ܖ | ܐܢ 0 سبيد ي أبيض د ومن بر اي فوق ٠‏ وسيب التنسمية ظاجر ܚܝ ܐ 0 27 1:0 0 ܟܙ 19 6 اي 2 ܐܩܢܐ :2 أطلق على كل من يديع أي جنس كان من العطر والعقاقير 07 ا  -‏ 5 396 ومن بانااي صاحب واما 5 فأخوذة من 9 0 0 3 * (الصُؤْبآن) السمين الشديد مركب من ܪܕ أي قوة ومن ع بان اي ذو + ( الضبطر | 98 ) الأسد ܬܨ تعر يب ÷ اي أقوى عله معو ܐܢܒܐ (الصَتَغْطرى ) اف الرجل الشديد والصَيَئْط والصَسَمْطَى ܚܐ فنه
@@ leaf 142 : ال) الة معوجة ܝ تهدم 0 ܟܒ 7 فارسّة فاذا صح ذلك ك1 ادن 1 لشات :0600 +« ( الكلحَة ) كيل معروف لاهل العراق وهى 0 ܝܫܐ 0:00 ܦ والفارسى ܝ ܨ ܟܝܠܐ : لكا ) المطكى فارسيّة كنا 05 (اللازورد) 3 0 ال 1 الطرة معرب ليت ܐ اللجام ) تعريب لكام وهو بالارامسة ܠܓܡܐ ܠܘܓܡܐ وباحدشة 1010 + وبرادفة ܐܐܐܠ 4 (١‏ فرد ܀ \ ) ܕܝܢ 13100 ا 0 صل < 1 ® ܐܪܝܐ من ܥ ܢ ® طلق 3 على الفك ܨ * (اللَج) الياعة الكثيرة ومعظم الماء تعريب 3 وهو اليش البالغ عدده قات العك قر وتلق @) علي كل ما بلغ عدده مائة الف ([35) .27 ܥ وهو ضرب من الطيوب مر 3 ܨ العود ܕ ܐܫܡ والمسك واللادن والكافور
@@ leaf 160 : ل | ܘ | صمت ,3 ܚܝ و3 ( الحاوآت 22 الذى يدق شه الدواء وغاره 2 هاون ܦ 4 ة هاون بالتركة 313 بالكردنة د ( | ܙ ) ܐܕܒ ^ 7 32 هيرون 2 بضصرب °ܝ القصب علو الداخل ̄ܒ 4 زم ر سّليه با لقَطن :رفير 354 + ا ( 00:0 وقمل اسم اداته 0 56 هس وهو الحراث ܒܝܒܗ ® (م 026 © جرمعى 153 ( الوبر) فارسيتة وبر 905 اصغر 7 »× 0:37371 5 10509 9 الرَح) ضرب من الأدوية وهو اصول نبات كالبردي تعريب‎ ١ 0 ( 565 الا الَهُ اعظم من يكون في ܝ ܐ والصحارى 27 171 140000 من امات محتبل ان :536 كته الى النقطة ومنه الكردي تت ` ضرب من الاوتار او العود او ܗ معرب وله بالفارسّة 15 1 ܝܐ ) ٠‏ قات و 3 د تت اللغة اله ܢ بيدي بل ونك بعنى الصدى والصوت ( ! العنب الاسود 3 او هو من توافق 335( ܒܣ ® ܛ الشراب و 053 ܢ ܐܚܝܬ يعنى الكرمة والشراب و يوراه بالونائيّة و نامف بالروممة و7111 ا و 82110 بالروسمة و7110 بالايطاليائة و 5711 بالانتكليزية و ܐ 5 0 9 0 ± جنسيليوس ) ٠‏ ويوافقة ايضاً العتى ]ܐܟ £¿ ܕ ܥܢܒܐ بالاراميّة معدو بده
```


## [2026-09-04T18:35:51.267Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));v=d['AFM'];print(v.get('page_offset'));print(v.get('lookup_hint'));print(v.get('url'))\"",
 "description": "AFM offset"
}
```


### [2026-09-04T18:35:52.715Z] TOOL RESULT

```
198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image
Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)
```


## [2026-09-04T18:35:56.813Z] TOOL CALL #29: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py AFM:5 --image 2>&1 | head -20",
 "description": "Render AFM page 5"
}
```


### [2026-09-04T18:35:58.656Z] TOOL RESULT

```
no scan of AFM covers printed page 5 (see 'scans' in refs_online.json)
```


## [2026-09-04T18:36:04.167Z] TOOL CALL #30: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-04T18:36:04.173Z] TOOL RESULT

```


```


## [2026-09-04T18:36:08.673Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%84%CE%B3%CE%B3%CE%B5%CE%BB%CE%BF%CF%82",
 "prompt": "Give the full etymology section for Ancient Greek ἄγγελος: proposed origins, relation to ἄγγαρος, any Semitic/Akkadian agāru or Iranian source, and cited scholars (Beekes etc.)."
}
```


## [2026-09-04T18:36:09.669Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/angel",
 "prompt": "Full etymology of 'angel' including Greek angelos, angaros, Persian/Semitic origin claims."
}
```


### [2026-09-04T18:36:16.464Z] TOOL RESULT

```
# Etymology of "Angel"

The word "angel" emerged around 1300 from a blend of Old English *engel* and Old French *angele*, both deriving from Late Latin *angelus*. This ultimately traces to Greek *angelos*, meaning "messenger, envoy, one that announces."

## Origin Theories

The Greek root's ultimate source remains uncertain. Scholars have proposed several possibilities:

- **Sanskrit connection**: A comparison to Sanskrit *ajira-* ("swift") has been proposed but "has now been abandoned"
- **Iranian origin**: Some suggest ties to Greek *angaros* ("Persian mounted carrier")
- **Semitic sources**: Klein has suggested Semitic language origins

The Greek term was adopted in Biblical translation to represent the Hebrew *mal'akh* (messenger), from the root meaning "to send."

## Extended Meanings

Beyond its primary spiritual sense, "angel" came to describe "one who is loving, gracious, or lovely" by the 1590s. Medieval English also used the term for a gold coin bearing the image of archangel Michael.

Modern compounds include "angel food cake" (attested 1881) and "angel dust," a street name for phencyclidine (1968).
```


### [2026-09-04T18:36:17.249Z] TOOL RESULT

```
# Etymology of Ancient Greek ἄγγελος

The word ἄγγελος has uncertain origins but shows cognation with Mycenaean Greek 𐀀𐀐𐀫 (a-ke-ro). Scholars propose it as "probably a loanword, likely related to ἄγγᾰρος (ángăros, 'Persian mounted courier')," which itself may derive from Old Persian or another Asian language.

**Semitic hypothesis:** Klein suggests a Semitic source, noting parallels to Aramaic 𐡀𐡍𐡂𐡓𐡕𐡀 ('engirtā, "missive, letter; contract") and Classical Syriac ܐܓܪܬܐ (ˀeggarṯā, "letter, document"), which trace to Akkadian 𒂊𒄈𒌓 (egertu, "inscribed tablet; contract").

**Sanskrit comparisons:** The entry also references Sanskrit अजिर (ajira, "agile, swift"), अञ्जि (añji, "commander, sender"), and अञ्जस् (añjas, "speed, velocity") as potential cognates.

**Religious sense:** The meaning "angel" or "heavenly spirit" in Koine Greek represents "a semantic loan from Biblical Hebrew מַלְאָךְ (malʾāḵ)."

The primary scholarly authority cited is Robert S. P. Beekes' *Etymological Dictionary of Greek* (2010).
```


## [2026-09-04T18:36:21.841Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9%D9%88%D8%AF",
 "prompt": "For the Arabic entry عود (ʿūd): give its etymology and meanings (wood, lute), the root ع و د, and any claim of borrowing from Sanskrit agaru or elsewhere. Also mention the Persian entry if present."
}
```


## [2026-09-04T18:36:22.830Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/aloe",
 "prompt": "Full etymology of 'aloe': Greek aloe, Latin, Hebrew ahalim/ahaloth, Sanskrit agaru, any Dravidian claim."
}
```


### [2026-09-04T18:36:29.330Z] TOOL RESULT

```
# Etymology of Aloe

Based on the Online Etymology Dictionary, the word "aloe" has a complex linguistic journey:

**Primary Origin:**
The term entered English in the late 14th century, referring to "a group of shrubs or herbs with spiky flowers and thick leaves, yielding bitter juice which was used as a purgative drug." It derives from Latin *aloe*, which came from Greek *aloē*, though "its origin is uncertain, probably a loan-word from an Oriental language."

**Secondary Meaning:**
An older English sense described "fragrant resin or heartwood of an East Indian tree" (Old English *alewe*). This usage stemmed from a mistranslation of the Latin/Greek term for the Hebrew word *akhalim*, which "ultimately is perhaps from a Dravidian language."

**Modern Confusion:**
The term was incorrectly applied to the American agave plant in the 1680s due to its similar appearance. To distinguish the original plant, botanists began calling it "aloe vera" (using Latin *vera* meaning "true").

The etymology demonstrates how medical terminology and biblical translation contributed to word meanings evolving across cultures and languages.
```


### [2026-09-04T18:36:30.234Z] TOOL RESULT

```
# عود (ʿūd) - Etymology and Meanings

## Primary Meanings
The Arabic entry عُود (ʿūd) denotes: "wood, timber; stick, rod, pole; branch, twig; stem, stalk; cane, reed; aloe/agarwood; thin strip of wood/veneer; oud (lute); body/build; strength."

## Root and Etymology
The term derives from the Semitic root **ع و د** (ʕ w d). The etymology traces to "عَادَ (ʕāda, to return, turn back)" in reference to wood's flexible nature.

## Instrument Etymology
The oud sense represents a "semantic loan from Middle Persian" rather than Sanskrit. The entry notes connection to Middle Persian *lwt'* (stringed instrument/barbat), which influenced Arabic terminology. The instrument developed distinctive features—smaller curved neck and larger steam-bent wooden belly—differentiating it from the solid-carved Persian barbat.

## Ancient Precedent
Notably, a Ugaritic cognate exists: "𐎓𐎄 (ʿd, lute)" predating later developments by millennia, connected to Sumerian wooden instruments.

## Persian Entry
The Persian عود ('ud) appears as a borrowing from Arabic, denoting both "incense" and "oud/lute" (with synonyms barbat and lut).

**No Sanskrit *agaru* borrowing is mentioned in this entry.**
```


## [2026-09-04T18:36:35.396Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D8%AC%D8%B1",
 "prompt": "Arabic أجر: etymology of the root ء ج ر (ajara 'to hire/reward'), any Akkadian agāru / Aramaic / Syriac source, and the derived nouns أجر ajr, أجرة ujra, إجارة ijāra."
}
```


## [2026-09-04T18:36:37.798Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A5%D9%86%D8%AC%D9%8A%D9%84",
 "prompt": "Arabic إنجيل: full etymology — Greek εὐαγγέλιον, route via Ethiopic/Ge'ez wangel or Syriac ewangeliyon, and any Persian angelyun. Cite scholars named."
}
```


### [2026-09-04T18:36:41.822Z] TOOL RESULT

```
# أجر (Ajr) - Arabic Dictionary Entry

Based on the Wiktionary page, **أجر** (ajr) is a multifaceted Arabic term with several meanings:

## Primary Definitions

**As a Noun:** The word functions as a masculine noun meaning "wages," "salary," "pay," or "hire." It can also mean "reward," "recompense," or "compensation."

**As Verbs:** Multiple verb forms exist:
- Form I (أَجَرَ): "to reward, pay, compensate" or "to hire, rent out"
- Form II (أَجَّرَ): "to rent" or "to hire"

## Etymology

The entry notes it derives from the Semitic root ء ج ر (alif-jīm-rā). The page indicates comparison with Hebrew אגר (agár), suggesting ancient linguistic connections related to gathering or harvesting concepts.

## Linguistic Variations

The term appears across multiple Arabic dialects:
- **Egyptian Arabic**: أجر (wage, salary)
- **South Levantine Arabic**: أجّر (to rent out)

The extensive conjugation tables demonstrate the complexity of Arabic verbal morphology, showing how this root generates numerous grammatical forms across tenses, moods, voices, and persons.
```


### [2026-09-04T18:36:44.193Z] TOOL RESULT

```
# إنجيل (Injīl) - Arabic Dictionary Entry

This Wiktionary entry documents the Arabic word **إنجيل** (ʔinjīl), which means "Gospel" or "evangel."

## Key Information

**Definition:** The term refers to the Gospel in both Christian and Islamic contexts, and can denote the New Testament in Christian usage.

**Etymology:** The word likely derives from Ancient Greek *εὐαγγέλιον* (euangélion), "possibly through Classical Syriac *ܐܘܢܓܠܝܘܢ* (ʾewwangellīōn) or a variant thereof."

**Pronunciation:** /ʔin.d͡ʒiːl/

**Grammatical Details:** It functions as a masculine noun with the plural form **أَنَاجِيل** (ʔanājīl). The entry includes comprehensive declension tables for singular, dual, and plural forms across different grammatical cases.

**Related Terms:** The entry connects this word to other religious texts, including references to the Qur'an, Bible, Torah, and Psalms in Arabic.

**Descendants:** The word has been borrowed into numerous languages, including Turkish, Persian, Malay, Indonesian, Azerbaijani, Bengali, and Japanese.
```


## [2026-09-04T18:36:47.408Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/lute",
 "prompt": "Etymology of English 'lute' (the instrument): Old French lut/leut, Old Provençal laut, Arabic al-'ud 'the wood'. Any mention of Sanskrit?"
}
```


## [2026-09-04T18:36:48.543Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/flute",
 "prompt": "Etymology of 'flute': Old French flaute/fleute, Old Provençal flaut, blend with laut 'lute', and Latin flare theories."
}
```


### [2026-09-04T18:36:51.491Z] TOOL RESULT

```
Based on the etymology page provided, there is **no mention of Sanskrit** in the documented origin of the word "lute."

The etymology traces the word back through: Old French *lut/leut* → Old Provençal *laut* → Arabic *al-'ud* (meaning "the wood"). The page notes that "al" is the definite article in Arabic, making *al-'ud* literally translate to "the wood."

The documented path of transmission shows the word spreading from Arabic into Romance languages (Spanish *laud*, Portuguese *alaude*, Italian *liuto*) and then into Germanic languages (Dutch, German, Danish), but Sanskrit does not appear in this etymology chain.
```


### [2026-09-04T18:36:55.610Z] TOOL RESULT

```
# Etymology of "Flute"

The word "flute" originated in the early 14th century from Old French *flaut* and *fleute*, which came from Old Provençal *flaut*. The Provençal source has uncertain origins, but scholars propose several theories.

**Proposed Origins:**

The term may be imitative in nature, or it could derive from Latin *flare* meaning "to blow." According to etymological research, it may have also been influenced by Provençal *laut*, meaning "lute."

**Historical Development:**

Originally, "flutes were direct, blown straight through a mouthpiece but held away from the player's mouth." The modern transverse flute developed during the 18th century, with earlier styles sometimes called *flûte-a-bec* (French for "flute with a beak"). The modern concert flute's design and key system were refined in 1834 by Theobald Boehm.

**Extended Meanings:**

Beyond the musical instrument, "flute" acquired architectural meaning around 1650 to describe "furrows in a pillar," based on resemblance to a flute's interior. By the 1640s, it also referred to a "tall, slender wine glass."
```


## [2026-09-04T18:36:59.661Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%97%E0%A4%B0%E0%A5%81",
 "prompt": "Sanskrit अगरु / अगुरु agaru, aguru: meaning, etymology (Dravidian?), and descendants (Hebrew, Greek agallochon, Arabic?)."
}
```


## [2026-09-04T18:37:02.087Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%80%CE%BB%CF%8C%CE%B7",
 "prompt": "Ancient Greek ἀλόη: etymology, proposed Semitic/Hebrew ahalot source, Sanskrit aguru, and what Beekes/Chantraine say. Also descendants (Latin aloe)."
}
```


### [2026-09-04T18:37:07.758Z] TOOL RESULT

```
# अगरु (Agaru) - Sanskrit Dictionary Entry

**Definition**: अगरु refers to agarwood, a fragrant resin-wood highly valued in traditional medicine and perfumery.

**Etymology**: The term was borrowed from Dravidian languages. According to the Wiktionary entry, scholars compare it to "Old Tamil 𑀅𑀓𑀺𑀮𑁰 (akil, 'eagle-wood')." The Sanskrit linguist David Shulman notes that the Hebrew term *ahalim* was "probably derived directly from Tamil *akil* rather than from Sanskrit *aguru*," indicating the word's South Indian origins.

**Linguistic Features**:
- Masculine u-stem noun in Sanskrit
- Pronounced /ɐ.ɡɐ.ɾu/ in both Vedic and Classical Sanskrit
- A doublet of अगुरु (aguru)

**Descendants**: The word spread across multiple language families through trade and cultural exchange:
- **Indo-Aryan**: Hindi अगर (agar), Gujarati અગર (agar)
- **Austronesian**: Malay/Indonesian gaharu
- **Sino-Tibetan**: Tibetan ཨ་ག་རུ (a ga ru)
- **Tocharian/Turkic**: Traced through Old Uyghur to Classical Mongolian агар (agar)

The term's journey across Eurasia reflects the historical importance of agarwood trade routes.
```


### [2026-09-04T18:37:08.422Z] TOOL RESULT

```
# Ancient Greek ἀλόη (aloe)

## Etymology

The word ἀλόη originated as "a loanword from an Eastern language." It entered Greek via Aramaic during the 1st century CE, with cognates in Classical Syriac, Christian Palestinian Aramaic, and Classical Mandaic. The ultimate source traces to Old Tamil *akil*, related to modern Tamil *அகில்* (akil, "agarwood").

## Meaning

This Ancient Greek noun refers to the aloe plant, specifically *Aloe vera*.

## Linguistic Features

- **Gender**: Feminine
- **Declension**: First declension
- **Pronunciation**: In 5th-century BCE Attic, /a.ló.ɛː/, evolving to /aˈlo.i/ in later periods

## Descendants

The word spread across multiple language families:
- **Latin**: aloē (producing modern Romance language forms)
- **Aramaic**: Jewish Palestinian, Babylonian, and other varieties
- **Arabic**: أَلْوَة (ʔalwa)
- **Armenian**: հալվե (halve)
- **Georgian**: ალოე (aloe)

The etymological research cited comes from Beekes' *Etymological Dictionary of Greek*.
```


## [2026-09-04T18:37:19.846Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%84%CE%B3%CE%B3%CE%B1%CF%81%CE%BF%CF%82",
 "prompt": "Ancient Greek ἄγγαρος: meaning, etymology — Old Persian / Akkadian agru 'hired man' / Aramaic, and relation to ἄγγελος. Name the scholars cited."
}
```


## [2026-09-04T18:37:21.163Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/agaru",
 "prompt": "Is there an Akkadian entry agāru 'to hire'? Give its meaning, forms (agru 'hired man', igru 'wages') and descendants (Aramaic, Arabic)."
}
```


### [2026-09-04T18:37:25.737Z] TOOL RESULT

```
Based on the web page content provided, I cannot find any information about an Akkadian entry for "agāru" or its related forms and descendants. 

The Wiktionary page shown is for the English word "agaru" (meaning agarwood) and its Japanese romanization. It does not contain etymological information about Akkadian roots or related Semitic language descendants.

To find information about Akkadian "agāru" and its linguistic connections, you would need to consult a specialized etymological dictionary or academic resource focused on Akkadian and comparative Semitic linguistics.
```


### [2026-09-04T18:37:26.262Z] TOOL RESULT

```
# ἄγγαρος: Etymology and Meaning

## Definition
The Ancient Greek word **ἄγγαρος** (ángăros) refers to a "Persian mounted courier, for carrying royal dispatches."

## Etymology
The word's exact origin remains uncertain. Two main theories are proposed:

1. **Akkadian connection**: Possibly from Akkadian *egirtu* ("inscribed tablet; contract"), though the Wiktionary notes this is "not from" the Akkadian term *LU2.ḪUN.GA2* (agru, "hired man").

2. **Old Persian pathway**: More likely from Old Persian *\*angarā* ("missive, letter"), which itself derives from Aramaic *\*'engartā* or *\*'iggartā*, ultimately tracing back to Akkadian *egirtu*.

The entry notes it's "a likely doublet of ἄγγελος (ángelos)" (messenger).

## Scholars Cited
- **Robert S. P. Beekes** (2010) — *Etymological Dictionary of Greek*
- **Jan Tavernier** (2007) — *Iranica in the Achaemenid Period*
```


## [2026-09-04T18:37:39.601Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%90%D7%94%D7%9C%D7%99%D7%9D",
 "prompt": "Hebrew אֲהָלִים / אֲהָלוֹת ('ahalim/'ahalot) 'aloes': meaning, biblical attestations, and etymology (Sanskrit aguru or Dravidian akil?)."
}
```


## [2026-09-04T18:37:41.264Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AC%DB%8C%D9%84",
 "prompt": "Persian انجیل: etymology and meaning. Also check if there is any note about انگلیون / Middle Persian ewangelyon."
}
```


### [2026-09-04T18:37:41.650Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T18:37:47.478Z] TOOL RESULT

```
# Persian انجیل: Etymology and Meaning

## Meaning
In Persian, انجیل (injīl/enjil) refers to "the gospel, the evangel" and in Christian contexts, "the Bible" or "the New Testament."

## Etymology
The word was "Borrowed from Arabic إِنْجِيل (ʔinjīl)." The entry notes this is a "Doublet of انگلیون (angalyūn/angalyun, 'Gospel'), borrowed directly from Syriac, which this Arabic word displaced."

This etymology shows a linguistic competition: the older Syriac-derived form was eventually replaced by the Arabic term that came through the same historical pathway—both ultimately deriving from Ancient Greek euangélion through Syriac intermediary languages.

The complete etymological chain traces back through Classical Syriac ܐܘܢܓܠܝܘܢ and Ancient Greek, with Proto-Indo-European roots.
```


## [2026-09-04T18:37:53.896Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%90%D7%94%D7%9C%D7%95%D7%AA",
 "prompt": "Hebrew אהלות: is there an entry for 'ahalot 'aloes'? Give meaning and etymology."
}
```


### [2026-09-04T18:37:56.818Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T18:38:05.962Z] TOOL CALL #46: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%E1%BC%84%CE%B3%CE%B3%CE%B5%CE%BB%CE%BF%CF%82|page 36 entry 0 node 4: Greek angelos origin (Beekes; Klein's Semitic hypothesis)\" \\\n \"https://www.etymonline.com/word/angel|page 36 entry 0 node 8: English angel chain and origin theories\" \\\n \"https://en.wiktionary.org/wiki/%E1%BC%84%CE%B3%CE%B3%CE%B1%CF%81%CE%BF%CF%82|page 36 entry 0 node 4: Greek angaros, Akkadian egirtu vs agru, Old Persian *angara\" \\\n \"https://en.wiktionary.org/wiki/%D8%A3%D8%AC%D8%B1|page 36 entry 0 nodes 2-3: Arabic root a-j-r ajr/ujra/ijara\" \\\n \"https://en.wiktionary.org/wiki/%D8%A5%D9%86%D8%AC%D9%8A%D9%84|page 36 entry 0 node 6: Arabic injil from Greek euangelion via Syriac\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AC%DB%8C%D9%84|page 36 entry 0 nodes 5,7: Persian enjil from Arabic; angelyun from Syriac\" \\\n \"https://en.wiktionary.org/wiki/%D8%B9%D9%88%D8%AF|page 36 entry 1 nodes 1-2: Arabic ud root '-w-d, Persian ud\" \\\n \"https://www.etymonline.com/word/aloe|page 36 entry 1 nodes 6-9: aloe chain Greek-Latin-English\" \\\n \"https://www.etymonline.com/word/lute|page 36 entry 1 nodes 3,5: lute from Arabic al-ud\" \\\n \"https://www.etymonline.com/word/flute|page 36 entry 1 nodes 3,5: flute origin, blend with lute\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%97%E0%A4%B0%E0%A5%81|page 36 entry 1 root: Sanskrit agaru, Dravidian origin, Shulman on Hebrew ahalim\" \\\n \"https://en.wiktionary.org/wiki/%E1%BC%80%CE%BB%CF%8C%CE%B7|page 36 entry 1 nodes 6-8: Greek aloe from Aramaic, ultimately Old Tamil akil\" \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-04T18:38:11.492Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/134af8b7c9acb748.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e65a1f6d413a75ba.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/64fcae89e4cac1bb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fb17fed0f79dc076.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8a4fc08c9d330eb5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3fbbc8bfd789a59a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0c71acb5fb7f79c0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8caaf509bac4d289.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ee226ab08c87cd91.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b62e0e3c80400a8c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b31794ee92acd0eb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6a97528bdc5ca078.txt
```


## [2026-09-04T18:38:32.838Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nimport re,os\ndef show(f,pats,ctx=300,limit=1):\n    if not os.path.exists(f): print('MISSING',f); return\n    t=open(f,encoding='utf-8',errors='replace').read(); pg=t.split('\\f')\n    for pat in pats:\n        n=0\n        for i,p in enumerate(pg):\n            for m in re.finditer(pat,p,re.I):\n                n+=1\n                if n>limit: break\n                print(f'@@ {os.path.basename(f)} /{pat}/ leaf{i}: '+p[max(0,m.start()-ctx):m.start()+ctx].replace('\\n',' '))\n            if n>limit: break\n        if n==0: print(f'-- {os.path.basename(f)} /{pat}/ : SILENT')\nprint('## POK'); show('POK_full.txt',[r'\\bangelos|ἄγγελος|ang\\^helos',r'\\bal.h.\\b.{0,20}aloe'],limit=1)\nprint('## WLD b3'); show('WLD_band3.txt',[r'angelos'],limit=1)\nprint('## AHD watkins'); show('AHD_watkins1985.txt',[r'\\bangel\\b',r'\\baloe\\b',r'\\blute\\b',r'\\bflute\\b'],limit=1)\nprint('## RCH'); show('RCH.txt',[r'\\bijara|ij[aá]rat',r'\\binjil|inj[ií]l',r'angaly|angely',r\"\\b.[uú]d, Wood|al-'ud\"],limit=1)\nprint('## PHD'); show('PHD_mackenzie.txt',[r'ewangel|wng',r'\\bʾgr|hire'],limit=2)\nprint('## NYB'); show('NYB_vol2_glossary.txt',[r'ewangel|wnglywn'],limit=2)\nprint('## SOD'); show('SOD.txt',[r'wnglywn|ewangel|ʾwnglyw'],limit=2)\nPY",
 "description": "Batch grep POK WLD AHD RCH PHD NYB SOD"
}
```


### [2026-09-04T18:38:37.397Z] TOOL RESULT

```
## POK
-- POK_full.txt /\bangelos|ἄγγελος|ang\^helos/ : SILENT
-- POK_full.txt /\bal.h.\b.{0,20}aloe/ : SILENT
## WLD b3
-- WLD_band3.txt /angelos/ : SILENT
## AHD watkins
@@ AHD_watkins1985.txt /\bangel\b/ leaf32:  anemos, wind: ANEMO-. [Pok. 3. an(9)- 38.] anata. Doorjamb. Latin antae (plural), a pair of pillars on the opposite sides of a door: ANTA. [Pok. anatd- 42.] [angelos. Messenger. Greek noun, akin to Greek anga- ros, mounted courier, both from an unknown Oriental source. 1. Greek angelos, messenger: ANGEL, (ANGELIC), ANGELICA, (ANGELUS); ARCHANGEL, EVANGEL. 2. Greek angaros, mounted courier: ANGARY.] angh-. Tight, painfully constricted, painful. 1. Germanic *ang-, compressed, hard, painful, in Old English ang- nzgl, “painful spike (in the flesh),” corn, excrescence (nzgl, spike; see nogh-): AGN
-- AHD_watkins1985.txt /\baloe\b/ : SILENT
@@ AHD_watkins1985.txt /\blute\b/ leaf66: -, -LYTE, -LYTIC; ANALYSIS, CATALYSIS, DIALYSIS, LYASE, PARALYSIS, TACHYLYTE; b. Latin lués, plague, pestilence (< “dissolution, putre- faction”): LUES; Cc. prefixed form *se-lu- (se-, apart; see s(w)e-) in Latin solvere, to loosen, untie: SOLUBLE, SOLUTE, SOLVE; ABSOLUTE, (ABSOLVE), ASSOIL, CONSO- LUTE, DISSOLVE, RESOLVE. [Pok. 2. Jeu- 681.] leu-2. Dirt; to make dirty. 1. Latin polluere, to pollute (< *por-luere; por- for pr6-, forth, forward; see per’): POLLUTE. 2. Suffixed zero-grade form */u-to- in Latin lutum, mud, mire, clay: LUTE?. [Pok. 1. leu- 681.] léu-1, Stone. Welsh Jlech, flat sto
@@ AHD_watkins1985.txt /\bflute\b/ leaf33: . 1. Germanic suffixed form *uhw-na- in *ufna- in Old English ofen, furnace, oven: OVEN. 2. Suffixed form *auk-sld- in Latin aulla, aula, olla, pot, jar: OLLA. [Pok. aug(h)- 88.] aulo-. Hole, cavity. 1. Metathetic form *alwo- in Latin bat- alvus, the belly, stomach: ALVEOLUuS. 2. Greek aulos, pipe, flute, hollow tube: CAROL, HYDRAULIC. [Pok. au- lo-s 88.] [aurum. Gold. Latin noun with preform *aus-o- probably from a root *aus-. Latin aurum (> French or), gold: AUREATE, AUREOLE, AURIC; AURIFEROUS, DORY?, EYRIR, OR’, ORE, ORIFLAMME, ORIOLE, ORMOLU, OROIDE, OR- PHREY, ORPIMENT.] aus-', To shine. 
## RCH
@@ RCH.txt /\bijara|ij[aá]rat/ leaf461: tqfSzl^  (vi  of  i^t^)  Lifting  with  both  hands, p j\af  tqfdr^  A   thorough-bred,  unbroken  colt.  A   well-paced horse,  (in  ancient  Persian)  Travelling. A   tySr  or  /qi/dr,  (pl.ofjs^*  /q;ir)  Merchants;  vintners, A   tajSrih^  (pi.  of  h jetT  tq;ribat)  Experiments,  proofs. A   tijarat^  Merchandize,  commerce,  as- hdb^itijdraty  Merchants,  v ^JkSjpaftijdratkardan^  To  trade, p   tufdrah^  A   cojt  not  yet  broke  in.* A   tajarl^  (viof  Conversing;  meeting;  agreeing. A   tajartd^  (pi.  ofA}ja^  t^jrid)  Detachments  sent  out. A   iqjdzt^{vi  of  Entreating  earne
@@ RCH.txt /\binjil|inj[ií]l/ leaf944:   bird.  Ecstasied,  enraptured. p   saiyaristdny  A   monastery  built  for  the  sophs. A   sinjarf  (or  sinjafr)y  Cinnabar. A   ^^^....s^sanjisbuyah  (p  i^y;...Sz.isangisbuyah)yC\ncpxeto\l. p   sanjaky  A   flag,  a   banner.  A   cornet.  A   pin.  San- jak  or  sai\}uky  A   waistband. A   sinjildty  A   species  of  spotted  odoriferous  flower. F   sanjahy  A   balance,  scales.  A   pound- weight.  An  equi- poise, or  make-wciglit. 853 A   weighing,  The weighing  or  nice  distinction  of  words,  or  miniite  objects. P   tinjidy  The  jujube«tree. P   sanjidagt,  The  act  of  w
@@ RCH.txt /angaly|angely/ leaf44: t,  or  Eon,  is  said  to  be  an  Egyptian  name  of the  sun  ;   and  for  this  we  have  the  authority  of  the priest  Manetho,  as  quoted  by  Eusebius  anil  Thco- j)hilus.  I   shall  not  dispute  it,  but  only  observe, that  every  thing  relative  to  the  old  Egyptians  is so  strangely  involved  in  hieroglyphic  darkness  and absurdity,  that  we  know  little  which  bears  the  sem- blance of  probability,  with  regard  to  their  history, their  religion,  or  their  language.  The  krihins,  or priests,  it  appears,  had  a   mysterious  character  of their  own  ; 
-- RCH.txt /\b.[uú]d, Wood|al-'ud/ : SILENT
## PHD
@@ PHD_mackenzie.txt /ewangel|wng/ leaf18: pless. delet~-diitag ... (read i"YiAtag) add vafriz ['pl'c I N faraz] acclivity.       ....afson      add M 'pswn.      ""gir         , add useless.       vigoi ['kw,§ I (M »ws, P 'gwc), N a"Yos] embrace, armful. add \R'''YiAtag ['gystk' I P *'gyst, N a"Yi§ta] mixed, defiled. add v.Ahliiwang [' hlyswng] = Ard. delete'Ahriiwang ... for vi.lum ... read vrlum ['lWlll I N -] millet.      v'8.sniid (ag) .,. delete noble.         aswir [PR/LSYA < A prsy'; ...         isnig         add acquainted with.         isUh         add concord.         ayid         read ['Qyq't' I ... for     bahr. .. and bah
@@ PHD_mackenzie.txt /ewangel|wng/ leaf58: g~kAn                                37                           grfyistan ·Il~kln [gwk)n'] details.    -Ig [-yk ' ] detailed; precisely.  gOmez [gwmye I N gimez] bull's urine (as ritual purifier).  g~mez- [gwmye- I N gimez-] urinate.  110n [gwn l I N gun] colour, complexion.   -ag [_kl 1M gwng, N guna] = 1l0n; sort, kind, form.  110r [gwll N -] onager, wild ass.  l10spand [KYNA < A qnyn) ?; gwspnd IN -] (small) cattle, sheep.   --~ihral1 [-eyhlk'] holding the seed of cattle.  110stiin [gwst)n l] cattle-stall, cowshed.  19~A [gwf I = M, N -] ear.  zGo§ [gwi I N -] cal. 14th day.  goAag
@@ PHD_mackenzie.txt /\bʾgr|hire/ leaf77: sh.                       ' miJiig [myc-, myswk/ I N mizii] lentil. mir-, v. murdan. mistan, 'mez- [mstn l , myc- IN mezidan] urinate.  -i~n(ih) : urination. mizag [m(y)ck I N maza] taste.                     '  -dirih [-d'lyh] (sense of) taste.  -omand [-)wmnd] tasty. mizd [m(y)zd IN muzd] reward, hire, pay.  -war [-wbll N -ur] hireling. ·mizne [m(y)znydy] mist, dew. miig [mwk ] shoe:-             ' ·moy-mard [m~!mlt', -gGBRA I N muy] magus. mor [mwl I N -] ant. m('jrd [mwlt' I N -] myrtle. morwarid [mwlw'lyt 1M mwrw)ryd, N -] pearl.                          ' ·mowbed [mgwpt l I N mobad] Mazd
@@ PHD_mackenzie.txt /\bʾgr|hire/ leaf77: iig [myc-, myswk/ I N mizii] lentil. mir-, v. murdan. mistan, 'mez- [mstn l , myc- IN mezidan] urinate.  -i~n(ih) : urination. mizag [m(y)ck I N maza] taste.                     '  -dirih [-d'lyh] (sense of) taste.  -omand [-)wmnd] tasty. mizd [m(y)zd IN muzd] reward, hire, pay.  -war [-wbll N -ur] hireling. ·mizne [m(y)znydy] mist, dew. miig [mwk ] shoe:-             ' ·moy-mard [m~!mlt', -gGBRA I N muy] magus. mor [mwl I N -] ant. m('jrd [mwlt' I N -] myrtle. morwarid [mwlw'lyt 1M mwrw)ryd, N -] pearl.                          ' ·mowbed [mgwpt l I N mobad] Mazdean priest. moy [mwd IN -] hair
## NYB
-- NYB_vol2_glossary.txt /ewangel|wnglywn/ : SILENT
## SOD
@@ SOD.txt /wnglywn|ewangel|ʾwnglyw/ leaf0:  >w/iJtw,  MDii;  >wn%  TSP  7.111;   S  W,  TPS  1994,  48  1907  Ww  ^tJ+Attf    onu   Ownw)   ©*ava-naku   ^'wn'kw,  w-,  xwny   that,  the   BSTBL;  STii  7.1,  9.12;  C2  gloss.;  MSP  p42;  GMS   960n  1,  1423,  1431;  Benv.  Et.  309,  >wnwn>x      "   that  is"   1908  Vnglywn  M,  C  J^l  ewangelyon   ©ob.  -y   Gospel,  Evangelion   GMS  1648,  1221;  BBB;  C2,  55R23,  28   1909  'wntn  M  jjaTo^T  ont/dan,  awantan   thus,  of  such   Sogdica.  21.4;  GMS  210n3,  1609   1910  Nvnw  =*  'wn'w   1911  'wnwn'x  C  ^u  onunax  ?   ^nJx   that  is   C2,  40R  21,  61R  20  p85;  Bcnv.
```


## [2026-09-04T18:38:57.766Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nimport re,os\ndef show(f,pats,ctx=280,limit=1):\n    if not os.path.exists(f): print('MISSING',f); return\n    t=open(f,encoding='utf-8',errors='replace').read(); pg=t.split('\\f')\n    for pat in pats:\n        n=0\n        for i,p in enumerate(pg):\n            for m in re.finditer(pat,p,re.I):\n                n+=1\n                if n>limit: break\n                print(f'@@ {os.path.basename(f)} /{pat}/ leaf{i}: '+p[max(0,m.start()-ctx):m.start()+ctx].replace('\\n',' '))\n            if n>limit: break\n        if n==0: print(f'-- {os.path.basename(f)} /{pat}/ : SILENT')\nprint('## RCH'); show('RCH.txt',[r'ijdrat|ij[aá]rat,',r'\\binj[ií]l,|Injil',r'ajr,\\s|\\bujrat'],limit=2)\nprint('## HJB'); show('HJB.txt',[r'\\bALOES\\b|Aloes,|aguru|agila'],limit=2)\nprint('## ARB jawaliqi'); show('ARB_mo3rb.txt',[r'العود',r'إنجيل|انجيل'],limit=2)\nprint('## PLA asbaghi'); show('incoming/PLA/PLA_pages.txt',[r'\\bʿūd|\\bud\\b.{0,30}Laute|Laute'],limit=2)\nprint('## FSD'); show('FSD_vol3.txt',[r'lute, n|\\blute\\b.{0,60}Arab'],limit=2)\nprint('## WEB'); show('WEB_vol1.txt',[r'al[o0]e, n|Gr\\. alo'],limit=2)\nPY",
 "description": "Batch grep RCH HJB ARB PLA FSD WEB"
}
```


### [2026-09-04T18:39:02.185Z] TOOL RESULT

```
## RCH
@@ RCH.txt /ijdrat|ij[aá]rat,/ leaf461: dr^  A   thorough-bred,  unbroken  colt.  A   well-paced horse,  (in  ancient  Persian)  Travelling. A   tySr  or  /qi/dr,  (pl.ofjs^*  /q;ir)  Merchants;  vintners, A   tajSrih^  (pi.  of  h jetT  tq;ribat)  Experiments,  proofs. A   tijarat^  Merchandize,  commerce,  as- hdb^itijdraty  Merchants,  v ^JkSjpaftijdratkardan^  To  trade, p   tufdrah^  A   cojt  not  yet  broke  in.* A   tajarl^  (viof  Conversing;  meeting;  agreeing. A   tajartd^  (pi.  ofA}ja^  t^jrid)  Detachments  sent  out. A   iqjdzt^{vi  of  Entreating  earnestly  (a  pemn to  do  a
@@ RCH.txt /ijdrat|ij[aá]rat,/ leaf461: n  colt.  A   well-paced horse,  (in  ancient  Persian)  Travelling. A   tySr  or  /qi/dr,  (pl.ofjs^*  /q;ir)  Merchants;  vintners, A   tajSrih^  (pi.  of  h jetT  tq;ribat)  Experiments,  proofs. A   tijarat^  Merchandize,  commerce,  as- hdb^itijdraty  Merchants,  v ^JkSjpaftijdratkardan^  To  trade, p   tufdrah^  A   cojt  not  yet  broke  in.* A   tajarl^  (viof  Conversing;  meeting;  agreeing. A   tajartd^  (pi.  ofA}ja^  t^jrid)  Detachments  sent  out. A   iqjdzt^{vi  of  Entreating  earnestly  (a  pemn to  do  any  thing).  Jj^einanding  payme
@@ RCH.txt /\binj[ií]l,|Injil/ leaf944:  enraptured. p   saiyaristdny  A   monastery  built  for  the  sophs. A   sinjarf  (or  sinjafr)y  Cinnabar. A   ^^^....s^sanjisbuyah  (p  i^y;...Sz.isangisbuyah)yC\ncpxeto\l. p   sanjaky  A   flag,  a   banner.  A   cornet.  A   pin.  San- jak  or  sai\}uky  A   waistband. A   sinjildty  A   species  of  spotted  odoriferous  flower. F   sanjahy  A   balance,  scales.  A   pound- weight.  An  equi- poise, or  make-wciglit. 853 A   weighing,  The weighing  or  nice  distinction  of  words,  or  miniite  objects. P   tinjidy  The  jujube«tree. P   sanjida
@@ RCH.txt /ajr,\s|\bujrat/ leaf122: ning  384  mudds  or  about  768  lbs.  Spaces  of  ground where  such  quantities  may  be  sown.  (pi.  of  ^\f^jirdh)  Lea- thern [)ag8  in  which  travellers  carry  their  provisions.  Spaces or  areas  in  wells,  from  the  mouth  to  the  surface  of  the  water. ACl^^l  ujrat^  Reward,  recompense,  hire,  rent,  wages. A   f{;rady  Bald,  bare.  A   bald  person.  A   barren  field A   smooth  stone.  A   horse  with  very  
@@ RCH.txt /ajr,\s|\bujrat/ leaf745: ins. A   dajajdn  (from  dajja),  Walking  slow.  Creep- ing. Trading.  Loosing  a   veil. A   J   dajdf^.  Dark. A   aswadu)  dujduj.  Extremely  black,  pitchy,  dark. A   dajdajat  (from  q),  Calling  fowls  together by  saying  dajji  dajjt  Being  dark  (the  night). A^J  dajr,  The  plough-tail.  Dajr,  dijr,  dujr,  and  dt^ur, A   Turkish  or  French  bean.  Dq/r,  A   machine  in  which  grain is  put  for  sowing,  having  an  iron  instrument  at  the  bottom  which scatters  it.  Dqjar  (from J^^)^  Being  astonished,  confounded. Being  tum
## HJB
@@ HJB.txt /\bALOES\b|Aloes,|aguru|agila/ leaf69: in Academy,  Sept.  27,  1879,  p.  231. 1589. — "   itemanelanfsettle,  item  ane almarle,  ane  Kist,  ane  sait  burde  .  .  .  ." — Ext.  Records  Burgh  of  Olasgow,  1876, 130. 1878.— "  Sahib,  have  you  looked  in  Mr Morrison's  almirah?" — Life  in  Moftusil, i.  34. ALOES,  s.  The  name  of  aloes  is applied  to  two  entirely  different  sub- stances :  a.  the  drug  prepared  from  the inspissated   bitter  juice  of  the  AloS Socotrina^  Lam.  In  this  meaning  (a) the  name  is  considered  (Hanbury  and Fliickigerj  Pharfnacographi
@@ HJB.txt /\bALOES\b|Aloes,|aguru|agila/ leaf69: 79,  p.  231. 1589. — "   itemanelanfsettle,  item  ane almarle,  ane  Kist,  ane  sait  burde  .  .  .  ." — Ext.  Records  Burgh  of  Olasgow,  1876, 130. 1878.— "  Sahib,  have  you  looked  in  Mr Morrison's  almirah?" — Life  in  Moftusil, i.  34. ALOES,  s.  The  name  of  aloes  is applied  to  two  entirely  different  sub- stances :  a.  the  drug  prepared  from  the inspissated   bitter  juice  of  the  AloS Socotrina^  Lam.  In  this  meaning  (a) the  name  is  considered  (Hanbury  and Fliickigerj  Pharfnacographia^  616)  to  be derived  f
## ARB jawaliqi
@@ ARB_mo3rb.txt /العود/ leaf0: كثير » انظره فى الاسان فى مادة ”” ن ب ج* ومفاتيح العلوم لهذوارزى الكاتب ألى عيد الله تمد ؟  ابن أحمل ن يوسف المتوق سنة /81؟ (ص ٠4‏ عن الطرعة المنير بة) وشفاء الغايل لزراجس (ص 5 م) ٠‏    ياه المر بياث    ”0 غواس ل ولاليت       ١6    يل يأب الألف    بي 3 و فلن 040  0 و” الأ » 5 ٠‏ العود الذى لبعخر يه ه.ذ5أ بوعبيد أله معرب :  )2 0   أ فى حديث ث القساسم م قال : إن الوالى أدنحت أقار , به أمائته  34  0 تحت القَدُوم * الإصافًا ينة؛ 6 حتى ل إلى قلمبا ٠‏   )04  قال ثور: :اغا الإصطفا مخ ة » كالمزرة »| مس بعر مية خحضة ) لين الم أدوالطاء   2    ل يكادان يحتمعان» و إ
@@ ARB_mo3rb.txt /العود/ leaf0: م فعال » والنوث       00(  و هر 5  أصاية ل ولا إل#مرقى مؤة 'فعمل 03  وى مدي ا به 5 ومن يا ١‏ مدوم  5 و والباج 0 المعى واحك اح الباج نضا أقهى ٠0‏ تقول : أجعله  و2 9 2 ء ش ر نرف  بأجأ واحدا ٠‏ أى شيا وأحدا ٠‏ وأقل من تكلم هذه الكلية ان بن عفان ٠‏  م 1 و9)  5 2 اليم وذ“ : أحد أوتار العود الذى العتمرانبا به 5 أحمى” معرب 5 1  03 - -000 > تير :  5 وم : هم مدطة يكامان . وقد ذ كرها الطر اح فقال :  مو ددم || رةس م 24 ١‏  الياتنا 2 م كزرمان أصبيحى  لق  م م5 ا 20  5 و2 بغداد يض 1 أمم أمجمى” كن 34 “صم .و داذ “عطية ٠‏ فكانها  ١ 3١ 7‏  عطية المعن ٠‏  2 39  )000 هنا يح
@@ ARB_mo3rb.txt /إنجيل|انجيل/ leaf0:  تحن العباد »> ٠‏ اظر الاثعقاق (ص*1) /  والمهرة (ج ١‏ ص ع ؟) كلاها لابن ع دريد ٠‏ وانار اللسان » ما ”ع بده  غ2( فى ب « والإبليس > وهوغطأ ٠‏ 4 فىب در آله » ٠.‏  (5) كلة دالثي»» ل نوق و    1  05  ار    ماه  ]أ    ”0 غواس ل جلاليت    وف باب الألف       0    إذا اشخريتة وأظهرته 2 فالإنجيل 2« بر يه م ٠‏ وقبل : هوقو  2 ل « من التجل «2 وهو الأضل ه (3 الإنجيل « امِل لعلوم و    1 5 ا 29 و  ِ 3 الإبزيم 66 : |بزم الممرج ونحوه» فارسى معرب .وقد تكامت بهالعرب ٠‏  2 2 ٍِ_    0-8 واس 2 و سما وار  وغ انلق الى ذا ليان يكل ف ارق فى أسفل المحمل ثم تعض عليها حاقتها»  لق 2   
@@ ARB_mo3rb.txt /إنجيل|انجيل/ leaf0: ابن ع دريد ٠‏ وانار اللسان » ما ”ع بده  غ2( فى ب « والإبليس > وهوغطأ ٠‏ 4 فىب در آله » ٠.‏  (5) كلة دالثي»» ل نوق و    1  05  ار    ماه  ]أ    ”0 غواس ل جلاليت    وف باب الألف       0    إذا اشخريتة وأظهرته 2 فالإنجيل 2« بر يه م ٠‏ وقبل : هوقو  2 ل « من التجل «2 وهو الأضل ه (3 الإنجيل « امِل لعلوم و    1 5 ا 29 و  ِ 3 الإبزيم 66 : |بزم الممرج ونحوه» فارسى معرب .وقد تكامت بهالعرب ٠‏  2 2 ٍِ_    0-8 واس 2 و سما وار  وغ انلق الى ذا ليان يكل ف ارق فى أسفل المحمل ثم تعض عليها حاقتها»  لق 2    ونه ميا بنع 4 ه الال  إولا 0 م ى عن لد أن عر    05 4    "ادق © فاون
## PLA asbaghi
@@ PLA_pages.txt /\bʿūd|\bud\b.{0,30}Laute|Laute/ leaf12:          Plurale,         2.    B.:   asätid,         asätida           von            pers,     ustäd   7.    denominative                Verben,         2.    Be:   tag >         tawwaß        u.      mutawwag   Die    Anpassung            der             persischen            Laute    ans    arabische               Lautinventar       geht         folgendermaßen                       vor       sich:   at;     pers.       & >>ar.                  < z.        B.:     pers.    äbkäri        >>ar.         Sabgari a2:     pers.       a >>ar.                
@@ PLA_pages.txt /\bʿūd|\bud\b.{0,30}Laute|Laute/ leaf14:                                                           XIX  t:   anlautendes      a,    das      nur   als     Rest    des   arabischen   Artikels   verstanden      werden   kann,        z.    B.:   pers.     bil       ar.     abil. u:   auslautendes      1,       z.   B.:   pers.     sarpäyi     >ar.      zarbil. 
## FSD
@@ FSD_vol3.txt /lute, n|\blute\b.{0,60}Arab/ leaf242:  under fbno- INQ [F , < L ortava, f of odaeus, eighth, < octo, eight) — great octave, the octave bcRlnuIng with C be- low the boss clef Hec scale — oe'tavocoup'ler, n. A contrivance attached to tho keyboard of musical In- struments so as to unite each note with Its octave — o.t flute, n. 1. The piccolo 2. An organ-stop — o. -forks, n. pl A pair ot forks tuned to the Interval of the octave — o. species, an arrangement of the tones of an ortave to con- form to some scale o.>Btop, n Bee octave, 1 (4) - short o. ((trganebuiiding), the lowest division of an e
@@ FSD_vol3.txt /lute, n|\blute\b.{0,60}Arab/ leaf645: t, g rfiv'o-lQt, a Hot A Zool Rolled backward from ttie iiiarKliiH uiwm the uudor Hurfare lIlUM under roNVOLUTt. [< L revolpo, pp rep/i/uft4«, aup uk- VOLVB 1 rev'o-lut''od|.- rev'o-luto*niar''Ktned. a Hav- ing odKCB rolled or turned backward or downward, as certain leavcB rev'o-lute, n Math A aolld of revolution KT*o-IU'tlun» vt [Rare.] To revolutlonlae rev^o-lu'Clon, 1 rev-o-hOMian, 2 rfiv'o-lfrahon, n 1. The act or atate of revolving (I ) A motion in n elowd curve around a renter, or a conipleie circuit or apparent cir- cuit made by a body In Much a c
## WEB
@@ WEB_vol1.txt /al[o0]e, n|Gr\. alo/ leaf73: rom all, all, and -od, orig., what fate assigned; hence possessions.] in law, land owned inde- pendently, without any rent, payment in ice etc.; a freehold estate: opposed to eud. Qse, bull, brite, türn, up; cry, myth; cat, machine, ace, church, chord; gem, añge AVE, n. i, aloe; Gr. aloz, the aloe.] a genus of plants of the lily family, native to the southern part of Africa. al’õe, n.; pl. al’des, any plant of the genus Aloe, as Aloe socotrina, one of the species used in med- icine. al’des, n.pl. [construed as sing.] in medicine, a bit- ter, laxative dru
@@ WEB_vol1.txt /al[o0]e, n|Gr\. alo/ leaf73: ; in the air; high above the ground; as, the eagle soars aloft. 2. in nautical language, at the masthead, or on the higher yards or rigging. _ , 3. on the upper part, as of a building. a-loft’, prep. on top of; on the upper surface of. [Obs.] A-l6/gi-An, n. [L. Alogiani, alogii; Gr. alogos; a priv., and logos, word.] in church history, a member of a sect of the second and third centuries, that rejected the Gospel and Reve- lation of St. John. al’6-g6-tr0/phi-a, al-6-got’r6-phy, n. [Gr. alogos; a priv., and logos, reason, and trophé, nourishment, from tre
```


## [2026-09-04T18:39:13.667Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nt=open('HJB.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[69]\ni=p.find('ALOES,  s.')\nprint(p[i:i+2600].replace('\\n',' '))\nPY",
 "description": "Print Hobson-Jobson ALOES"
}
```


### [2026-09-04T18:39:15.235Z] TOOL RESULT

```
ALOES,  s.  The  name  of  aloes  is applied  to  two  entirely  different  sub- stances :  a.  the  drug  prepared  from  the inspissated   bitter  juice  of  the  AloS Socotrina^  Lam.  In  this  meaning  (a) the  name  is  considered  (Hanbury  and Fliickigerj  Pharfnacographia^  616)  to  be derived  from  the  Synac  'ehoai  (in  P. ahodX  b.  Aloes-wood,  the  same  as Eagle-wood.  This  is  x>erhap8  from one  of  the  Indian  forms,  through  the Hebrew  (nL  forms)  ahdlim,  cUckdlim and  ahdldtky  akhdldth.  Neither  Hippo- crates nor  Theophrastus  mentions  aloes, but  Dioscorides  describes  two  kinds  of it  (Mat.  Med.  iii.  3).  "  It  was  probably the  Socotrine  aloes  with  which  the ancients  were  most  familiar.  Eustathius says  the  aloe  was  called  lepd,  from  its excellence  in  preserving  life  (ad.  II. 630).  This  accounts  for  the  powder  of aloes  being  called  Hiera  picra  in  the older  writers  on  Pharmacy."— (JfVan<»« AdamfUj  Names  of  aU  Minerals^  PlantSy and  Animuds  desc.  by  the  Greek  authors^ etc.) (a)c.  A.D.  70.— "The  best  Aloe  (Latin the  same)  is  brought  out  of  India.  .  .  . Much  use  there  is  of  it  in  many  cases,  but principally  to  loosen  the  bellie ;  being  the only  purgative  medicine  that  is  comfo^ble to  the  stomach.  .  .  ."—Pliny,  Bk.  xxvii  (PA. Holland,  ii.  212). (b)  ""HX^e  di  Kol  NiK6di7/ios  ....  ^/wr fiiyfM  fffi6pvrft  KoX  d\6rfs  c^ei  Xirpai iKarhv.^'—John  xix.  39. c.  A.D.  545. — "From  the  remoter  regions, I  speak  of  Tanista  and  other  places,  the imports  to  Taprobane  ar
```


## [2026-09-04T18:39:21.150Z] TOOL CALL #50: Bash

```json
{
 "command": "ls data/ 2>/dev/null | head -20; ls *.pdf data/*.pdf 2>/dev/null | head",
 "description": "Look for source PDF"
}
```


### [2026-09-04T18:39:21.201Z] TOOL RESULT

```
ANOMALIES.md
extracted
EXTRACTION_SPEC.md
research
translations
verification
(eval):1: no matches found: data/*.pdf
```


## [2026-09-04T18:39:23.096Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nimport re\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nfor w in ['عود:','اجر:']:\n    for m in list(re.finditer(w,t))[:3]:\n        print('###',w,':',t[max(0,m.start()-150):m.start()+400].replace('\\n',' '))\nPY",
 "description": "Mo'in ud and ajr entries"
}
```


### [2026-09-04T18:39:25.322Z] TOOL RESULT

```
### عود: : رزندزاده» پسر بسر»  نواده. قبله؛ ج. اسباط.   بع؛ 90 [ع.] (عد. .) هفت.  سبع: ماده [ع.] (ص.) درنده. جانور؟ ج.  سبا.  سبع: ([ع.] (عد. کسری) هفت یکد؛    سعود: 520-0 [ع.] (عد. ا.) هفتاد»    سبعه: (6-)۹202 [ع. سبعه ] (عد. ۱.) هفت.  سیعین: 92018 [غ.] (عد. ۱.) هفتاد» سبعون.  سیق: اوه [ع.] ( آنجه که بر سر آن در  مسابقهٌ اسب دوانی و تیراندازی شرط ندند.  (.) مقداری از کتاب که همه روزه آموخته  شود) ج. اسناق. ضسح.- در فارسی به این  معانی به سگون دوم هم آمده. (مج.) قر آن.  سبفت: ۱ [ع. سبق] (مصل.) پیشی  ضح.- اين مصدر مسجعول است و در زبان  عربی بجای آن «سبق» آ
### عود: :  درخت خرما که    از بررگ دور شده باشد. برگ درخت خرما؛  ‌: سعوف.  سعقص: 2125 [ع.] .( یکی از ترکسات  سعله: (م)هاه» (ع. سعلة] (ا.) (پز.) سعال»  سر فه.  سعود: 5014 [ع.] (مصل.) خوشحت  شدن» یکبخت گردیدن. خجسته گشتن»  سارک شدن.  سعوط: 25 [ع.] (.) (پز.) عطسه آور  (دارو)» معطس.  سعه: (6۵)2 [ع. سعه] (امص.) سعت. سعه  صدر: کشادگی سینه. (کد.) همت عالی» نظر  بلند. (کد.) گشاده دستی» دست و دل باز  بودن. سعه مشرب: آزاد اندیشی» آزاد  فکری.  سعی. ٩2۷‏ [ع.] (سصل.) کوشیدن؛  کوشش کردن. کار کردن» عمل کردن. قصد  کردن» آهنگ کردن. (اسص.) کوشش:  اهتمام. قصد.  ستعیك: 5214
### عود: :  اد59 ٩0‏ [ع. صعوبه] (مص‌ل.)  دشوار شدن کاره مشکل گردیدن) مق.  سهولت» آسانی. (امص.) دشواری» سحتی»  عسرت» مة. سهولت» آسانی. زحمت؛  محنت. در ماندگی.   صعود: 054 [ع.] (مصل.) به بالا رفتن»    پرآمدن. (امص.) بالاروی» عروج؛ ارتقاء؛    صعوه فرهنگ فارسی معیر ۹۸*۰۹    مق. نز ول. (نج.) بر آمدن ستاره بود به شمال  تا عررض او به شمال افزاید. (نج.) صعود و  هبوطء قیاس ستاره است به زمین و آن چنان  است که ستاره را به نطاق نخستین و دوم  هابط خوانند و بر سوم و چهارم صاعد.  صعود تدوبری: (نج.) بودن ک و کب است در  نطاق سوم و چهارم تدویر. صعود حاملی:  (نج.) بودن کوکب
### اجر: : ن. "   احراز: ۳92 [ع.] (مص م.) فراهم آوردن»  جمع کردن. در حرز کردن پناه دادن جای  دادن. دارا شدن» بدست آوردن. تصرف  چیزی که متعلق به عموم باشد. احراز اجر:  گرد آوردن و گرفتن مزد را. احراز مقام  (مقامات): دارا شدن مقام (مقامات).   احراق: و [غ.] (مسص‌م.) سوزانیدن»  زا کردن سر ازع رسانلو سس |  سوزآوری. احراق کواکب (نج.) احتراق  کواکب. احراق لاشه: سوختن جسد میت. .  احرام: سقعه [ع.] (.) ج. 0 و حریم:  احرام: اور ارت [ع. ۰[ (مص‌ل ۳ له حصج  را یک  حرمت شدن, در حرمتی در آمدن که هتکك  آن روا نیست» بعضی چیزهای حلال و مباح  را در هنگام زیارت کعبه و مراسم ح
### اجر: : ه. (گیا.) گیاه صاحب تاج و  اکلیل. چتری» ذواکلیل. تاجدار فلکك:  خورشید.   تاج‌دار: ۱-۲ [معر. ف.] (ص‌مر.) به  منز له افسر بر دار اعدام. م بر سر دار.   تاجر: لها [ع. ] (افا.) بازرگان» سوداگر؛  ج. تجار.   تاجریزی: 21-12 (امر.) (گیاء) گیاهی  است از تبرة بادنجانیان که علفی است و  بعض گونه‌هایش بصورت درختچه‌اند.  برگ‌های آن پهن و گل‌هایش منظم و گل  آذینش گرزن است. میوه‌اش سته می‌باشد؛  انگور روباه» عنب‌العلب.  تاج‌گذاری: آ2022۲-1-.۱ [معر. ف.]  9 آیین | نهادن دیهیم بر سر بادشاهی  نوء جشن تاج گذاردن پادشاهان؛ تتویج»  تاجور: ۱-57 (ص‌مر.) دارای تاج با افس
### اجر: :  د؟ ج‌. تساییر .   تش: ۱۵5 [- تيشه] (.) تيشة درودگری.  تشابه: ۱21200 ل ۰ (مصل.) بهم مانند  بودن به یکدیگر شبیه سودن. (اسص.)  همانندی؛ ج. تشابهات.   تشاجر: ۳۹ [ع. ۰] (مص‌ل.) با هم نزاع  کردن» با هم ستیزیدن» مشاجره کردن.  (امص.) کند » مشاجر ه.   تشارک: ۱۵8:06(ع.) (مصل.) با هم  شر یک کردن. (امص.) انبازی.   تشاعر: 90 [ع.] (مصل.) به شاعری  تظاهر کر دن» خود را شاعر نشان دادن به  تکلف شعر سرودن.   تشاغل: امرقذه۱ [ع.] (سص‌ل.) خود را  مشغول ساختن» خودرابه کاری س رگرم  کردن.   تشاکل: املقه۱ [ع.] (مصل.) مانند هم  شدن» بهم مانستن» هم شکل گشتن. (امص.)  رف
```


## [2026-09-04T18:39:29.174Z] TOOL CALL #52: Bash

```json
{
 "command": "sed -n 1,200p /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-04T18:39:29.239Z] TOOL RESULT

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


## [2026-09-04T18:40:58.310Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nimport re\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if re.search(r'Injil|Ingil|euangelion|evangel',p,re.I):\n        for m in re.finditer(r'Injil|Ingil|euangelion|evangel',p,re.I):\n            print('@@ leaf',i,'p~',i-17,':',p[max(0,m.start()-500):m.start()+500].replace('\\n',' '))\n            break\nPY",
 "description": "grep Jeffery for Injil"
}
```


### [2026-09-04T18:41:00.228Z] TOOL RESULT

```
@@ leaf 188 p~ 171 : FOREIGN VOCABULARY OF THE QUR ? AN 171 Bekri, Mu'jam, 369, 18, we read of how a<J-Dahhak entered a Christian monastery while the monk was reading #ju-*-i j* i^**-, and Ibn Duraid, 103, says that Sifr means " the volume of the Torah or the Injil or what resembles them ", 1 It is clearly a borrowing from Aramaic. 2 The common Heb. "15?? appears in Aram, as N"]9P ; Syr. ];W>- From Aram, it passed on the one hand into Eth. as tl&, and on the other into Arm. as un^fy. As the Arm. word seems to have come from Syr., 3 we may suppose that it was from the same source that the Arabs got the word. J x- *'jA-~> (Safara). Ixxx, 15. ^ i ** Scribes ; plu. of ^^?l *> (used of the heavenly scribes). as-Suyuti, Itq, 321 (Mutaw, 60), tells us that 
@@ leaf 243 p~ 226 : 226 FOREIGN VOCABULARY OF THE QUR ? AN be the equivalent of Taurah. In iii, 2, it is associated with the Taurah and the Injil, and xxv, 1, and ii, 181, make it practically the equivalent of the Qur'an, while in viii, 29, we read, " if ye believe God, he will grant you a Furqan and forgive your evil deeds." In viii, 42, however, where the reference is to the Battle of Badr, " the day of the Furqan, the day when the two hosts met," the meaning seems something quite different. The form of the word would suggest that it was genuine Arabic, a form J^*i from (Jj*, and thus it is taken by the Muslim authorities. Tab. on
@@ leaf 244 p~ 227 : FOREIGN VOCABULARY OP THE QUR'AN 227 text of the Hebrew Scriptures. 1 This, however, is rather difficult, and Margoliouth, Mohammed, 145 (but see ERE, ix, 481 ; x, 538), while inclining to the explanation from D^pIS, refers it, not to the sections of the Pentateuch, but to a book of Sayings of the Jewish Fathers, which Muhammad heard of from the Jews, and which he may have thought of as similar to the Taurah and the Injil. This theory is more probable than that of Hirschfeld, and has in its favour the fact that resemblances have been noted between phrases and ideas in the Qur'an and the well-known fTON ^pIS. 2 It also, however, has its difficulties, and in any case does not explain the use of the word in viii, 42. Linguistically there is a closer equivalence in the Aram. Ip'lS, ]p"113 deliverance or redemption, and Geiger, 56 ff., 3 suggested this as the source of the Arabic word. He would see the primary m
@@ leaf 251 p~ 234 : 234 FOREIGN VOCABULARY OF THE QUR ? AN for the Jews or Injil for the Christians. 1 It thus looks as though the word is not native, but an importation into the language. Marracci, 53, looked for a Jewish origin, suggesting that it was formed under the influence of the Heb. NHpJ? in its late sense of reading, as in Neh. viii, 8, and frequently in the Rabbinic writings. Geiger, 59, supports this view, and Noldeke in 1860, though inclining to & the view that it was a formation from I^J, yet thought 'that it was influenced by the use of X"lpQ. 2 The tend
```


## [2026-09-04T18:41:05.295Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==89||NR==90' FVQ_pages.txt | head -70",
 "description": "Print FVQ p.71-72"
}
```


### [2026-09-04T18:41:07.278Z] TOOL RESULT

```
FOREIGN VOCABULARY OF THE QUR*AN 71
In lix, 23, * j^.* meaning faithful* and in lix, 9, jlsj meaning
certainty, may be genuine Arabic (see Fischer, Glossar, 9a).
3^)* j (Infil).
"in, 2, 43, 58 ; v, 50, 51, 70, 72, 110 ; vii, 156 ; ix, 112 ; xlviii,
29 ; Ivii, 27.
Gospel.
It is used always of the Christian revelation, is particularly asso-
ciated with Jesus, and occurs only in Madinan passages. 2
Some of the early authorities tried to find an Arabic origin for it,
making it a form A^_ *0I from \, but this theory is rejected with
some contempt by the commentators Zam. and Baid. both on general
'*
grounds, and because of al-Hasan's reading Ju I , which clearly is
*r
not an Arabic form. So also the Lexicons LA, xiv, 171 ; TA, viii,
128 ; and al-Jawaliqi, 17 (al-KhafajI, 11), give it as a foreign word
derived from either Hebrew or Syriac (cf. Ibn al-Athlr, Nihdya, iv, 136).
Obviously it is the Gk. tvayytXiov, and both Marracci 3
and Fraenkel 4 have thought that it came directly into Arabic from
the Greek. The probabilities, however, are that it came into Arabic
through one of the other Semitic tongues. The Hebrew origin suggested
by some is too remote. It is true that in the Talmud we find ]Y1 V J ]TIS?
for ]1 v33T)N, 6 but this is merely a transcription of iQjJ^Jol,
and the DTOH nBOl DTP^T! "the Gilyonim and books
of the Minim ", merely reproduces the Syr. .CU.X... The sug-
gestion of a Syr. source is much more hopeful. It is true that .o*.^jo]
is only a transliteration of the Gk. tvayyeXiov, but it was as
commonly used as the pure Syr. ]2j^QD, and may be assumed to
have been in common use among the Christians with whom Muhammad
may have been in contact. Noldeke has pointed out, however, that
1 With which may be compared the Sab. , faithful. Cf. Hommel, Sttdara-
bische Chrest, 121 ; Rossini, GHoswrium, 106.
2 vii, 156, is perhaps an exception, but though the Sura is given as late Meccan,
this verse seems to be Madinan.
3 Prodromus, i, 5, " corrupta Graeca voce."
4 Vocab, 24.
6 Krauss, Griechische und lateinische Lehnworter im Talmud, ii, 21.
72 FOREIGN VOCABULARY OF THE QUR'AN
the Manichaean forms j^JiXjl of Persian origin, 1 and anglion of
Turkish origin, 2 still have the Gk. -LOV ending, and had the Arabic,
like these, been derived from the Syr. we might have expected it also
to preserve the final 0. The shortened form, he points out (Neue
Beitrdge, 47), is to be found in the Eth. <D*}1A> where the long
vowel is almost conclusive evidence of the Arabic word having come
from Abyssinia. 3 Grimme, ZA, xxvi, 164, suggests that it pay have
entered Arabic from the Sabaean, but we have no inscriptional evidence
to support this. It is possible that the word was current in this form in
pre-Islamic days, though as Horovitz, KU, 71, points out, there is some
doubt of the authenticity of the verses in which it is found. 4
<JI (Aya).
Of very frequent occurrence. Cf. ii, 37 ; iii, 9 ; xxxvi, 33.
A sign.
Later it comes to mean a verse of the Qur'an, and then a verse
of a book, but it is doubtful whether it ever means anything more than
sign in the Qur'an, though as Muhammad comes to refer to his preaching
as a sign, the word tends to the later meaning, as e.g. in iii, 5, etc.
It is noteworthy that in spite of the frequency of its occurrence in the
Qur'an it occurs very seldom in the early Meccan passages. 5
The struggles of the early Muslim philologers to explain the word
are interestingly set forth in LA, xviii, 66 ff. The word has no root
in Arabic, and is obviously, as von Kremer noted, 8 a borrowing from
Syr. or Aram. The Heb. DIN (cf. Phon. PX), from a verb !TIK, to
sign or mark, was used quite generally, for signs of the weather (Gen.
i, 14 ; ix, 12), for a military ensign (Numb, ii, 2), for a memorial sign
1 Vullers, Lex, i, 136 ; Salemann, Manichaeische Studien, i, 50 ; BQ, 88, which
latter knows that it is the name of the book of Jesus and the book of Mani fi
<JU v^llS^flJ < ^f' J-^l w i jLoi ollS^ It is curious that Bagh. on iii, 2,
gives /jjJ&| as an attempt to represent the Syriac original.
2 In the phrase uluy anglion bitig, cf. Lo Coq, 8BAW, Berlin, 1909, p. 1204.
```


## [2026-09-04T18:41:13.592Z] AGENT

Now I'll write the verification file.


## [2026-09-04T18:46:03.614Z] TOOL CALL #55: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /home/sfmqrb/git/rishe/data/verification/page-36.json <<'JSONEOF'\n{\n  \"pdf_page\": 36,\n  \"book_page\": 6,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Agaru\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Akkadian agāru 'to hire' (stative agir), with agru / agarru 'hired man, hireling' and igru 'wages'\",\n      \"note\": \"The root box is right: Akkadian agāru 'to hire' is a well-attested verb (CAD A/1 s.v. agāru; Zimmern, Akkadische Fremdwörter, 2nd ed. 1917, p.47). The Semitic left branch of this chart (Akk. > Aram./Syr. > Arab. ʾajara > Persian ejāre/ojrat/ajr) is solidly supported by Nourai's own references and is still the standard account. The Greek right branch is the weak point: Zimmern (1917), Jeffery (1938) and Klein (1966) do connect Greek ἄγγαρος (and through it ἄγγελος) with Akkadian agru 'hireling', but current scholarship (Beekes, EDG 2010; Tavernier, Iranica in the Achaemenid Period 2007, followed by Wiktionary) instead derives ἄγγαρος from Old Persian *angara- 'missive' < Aramaic *ʾiggartā < Akkadian egirtu 'inscribed tablet, letter' — a different Akkadian etymon. Watkins (AHD appendix) simply says 'unknown Oriental source'. One transliteration point: the chart's Arabic verb is printed in the JSON as 'a`jara'; the verb is أَجَرَ ʾajara, root ʾ-j-r with hamza, not ʿayn (Zimmern writes ʾagara, Klein 'Arab. ajara'). Since the chart elsewhere uses the backtick for ʿayn (Mo`ayyerî), this is most likely a hamza/ʿayn confusion introduced somewhere between the print and the JSON.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%E1%BC%84%CE%B3%CE%B3%CE%B5%CE%BB%CE%BF%CF%82\",\n        \"https://en.wiktionary.org/wiki/%E1%BC%84%CE%B3%CE%B3%CE%B1%CF%81%CE%BF%CF%82\",\n        \"https://www.etymonline.com/word/angel\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966.txt \\\\f-leaf 51 (≈ printed p.74-78), s.v. angel: 'of Persian, ult. of Sem. origin. Cp. Akkad, agarru, \\\"hireling, hired laborer\\\", fr. agaru, to hire, which is rel. to Aram. agar, eggār, \\\"he hired\\\", (whence Arab. ajara, of s.m.)'. Klein is exactly Nourai's root box.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Syriac\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Empty pass-through node standing for the Aramaic/Syriac stage. Akkadian agāru 'to hire' was taken over into Imperial Aramaic as ʾgr (ʾăgar 'he hired'), Syriac ܐܓܪ ʾegar 'to hire', with the nouns ܐܓܝܪܐ ʾăgīrā 'hireling, hired labourer' and ܐܓܪܐ ʾagrā 'wage, reward'. The Aramaic forms keep the Akkadian consonant skeleton unchanged (ʾ-g-r); the word is far commoner in Syriac than in Jewish Aramaic, which is why Jeffery makes Syriac specifically the donor to Arabic. Placing Syriac between Akkadian and both Arabic and Greek is therefore right for the Arabic branch and at least defensible for the Greek one.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A3%D8%AC%D8%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 51 s.v. angel: 'fr. agaru, to hire, which is rel. to Aram. agar, eggār, \\\"he hired\\\", (whence Arab. ajara, of s.m.)' — Klein's Aramaic is Nourai's Syriac node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"p.49 (FVQ_pages.txt leaf 66)\", \"stance\": \"supports\", \"note\": \"'From this come on the one hand the Aram. אגר : Syr. ܐܓܝܪܐ a hireling, and thence the denominative verbs אגר and ܐܓܪ, to hire, with corresponding nouns … It would have been from the Aram. that the word passed into Arabic … as the word is of much wider use in Syriac than in Jewish Aramaic, we are probably right in considering it as a borrowing from Syriac.'\"},\n            {\"src\": \"AKD\", \"where\": \"p.47 (AKD.txt leaf 56)\", \"stance\": \"supports\", \"note\": \"'akk. agru, agir, agarru Mietsklave, agāru mieten : > wohl aram. ʾegar mieten, ʾăgīrā Lohnarbeiter (> arab. ʾagara)'.\"},\n            {\"src\": \"AFA\", \"where\": \"grep 'agara|aggara|agir' in AFA.txt\", \"stance\": \"silent\", \"note\": \"Fraenkel's Aramäische Fremdwörter has no entry for this root in the OCR text.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Arabic\",\n          \"words\": \"a`jara\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic أَجَرَ ʾajara 'he hired, he gave wages, he rewarded' (root ʾ-j-r), with the verbal noun أَجْر ʾajr 'wage, reward' and أُجْرَة ʾujra 'hire, rent'. Aramaic/Syriac ʾ-g-r was taken into Arabic in the pre-Islamic period; Aramaic g regularly answers Arabic j (ǧ), so ʾăgar → ʾajara with no other change. Jeffery notes that the Muslim lexicographers took the root for pure Arabic but that the verb أجر 'to receive hire' is obviously denominative from the noun أجر, which betrays the loan. NOTE on the data: the JSON transliteration 'a`jara' has a backtick where a hamza belongs — the verb is ʾajara (ʾ-j-r), not *ʿajara (ʿ-j-r); the chart uses the same backtick for ʿayn elsewhere on the page, so this is very likely a hamza/ʿayn confusion in the transcription rather than Nourai's claim.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A3%D8%AC%D8%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"AKD:47\", \"status\": \"supports\", \"note\": \"AKD.txt \\\\f-leaf 56 = printed p.47: 'akk. agru, agir, agarru Mietsklave, agāru mieten : > wohl aram. ʾegar mieten, ʾăgīrā Lohnarbeiter (> arab. ʾagara); > wahrsch. auch ἄγγαρος urspr. wohl Mietling und dann erst Postknecht.' Zimmern's page is exactly the arrow Nourai draws, and Zimmern too writes the Arabic with the aleph/hamza, not ʿayn.\"},\n            {\"ref\": \"FVQ:49\", \"status\": \"supports\", \"note\": \"FVQ_pages.txt leaf 66 = printed p.49 (heading 'FOREIGN VOCABULARY OF THE QUR'AN 49'), s.v. أجر 'reward, wages': 'Zimmern, Akkad. Fremdw. 47, has pointed out that the ultimate origin of the root in this sense is the Akk. agru, agarru, hired servant … It would have been from the Aram. that the word passed into Arabic, probably at a very early period … we are probably right in considering it as a borrowing from Syriac.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 51, s.v. angel\", \"stance\": \"supports\", \"note\": \"'Aram. agar, eggār, \\\"he hired\\\", (whence Arab. ajara, of s.m.)'.\"},\n            {\"src\": \"RCH\", \"where\": \"RCH.txt leaf 122\", \"stance\": \"supports\", \"note\": \"Richardson lists 'A أجرة ujrat, Reward, recompense, hire, rent, wages' — marked A(rabic), the word and sense the chart gives.\"},\n            {\"src\": \"PLA\", \"where\": \"grep in PLA_pages.txt (Asbaghi, Persische Lehnwörter im Arabischen)\", \"stance\": \"silent\", \"note\": \"Asbaghi does not list أجر — consistent with the word being an Aramaic, not a Persian, loan in Arabic.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"ejâreh «اجاره»; ojrat «اجرت»; ajr «اجر»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are ordinary Arabic loans in New Persian, taken over after the Islamic conquest from the Arabic root ʾ-j-r: إِجَارَة ʾijāra (form-IV verbal noun) → Persian ejāre/ejārat اجاره 'lease, rent'; أُجْرَة ʾujra → Persian ojrat اجرت 'wage, fee' (Persian keeps the Arabic tāʾ marbūṭa as -at in the older pronunciation); أَجْر ʾajr → Persian ajr اجر 'reward, recompense', the sense Ḥāfeẓ uses in the couplet quoted on the chart ('اجر صبری است …'). The native Middle/New Persian word for the same notion is mizd/muzd (MP mizd 'reward, hire, pay', MacKenzie PHD), so these are lexical replacements, not inherited forms. The route Akkadian → Aramaic/Syriac → Arabic → Persian is therefore correct as drawn.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A3%D8%AC%D8%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"partial\", \"note\": \"The 6-vol page is not cited by number so the exact page could not be located, but Mo'in's text (2-vol Adena abridgement, MON_part1.txt) tags all three as Arabic: 'اجاره: [- اجارت، ع. اجارة] (مص‌ع.) … به مزد گرفتن' and 'اجرت: [ع. اجرة] (ا.) مزد، مزدکار، دستمزد … کرایه'. Mo'in confirms the words and their Arabic origin, i.e. the last arrow of the chain.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt s.vv. اجاره، اجرت (2-vol abridgement, no page numbers)\", \"stance\": \"supports\", \"note\": \"'اجاره: [- اجارت. ع. اجارة]' and 'اجرت: [ع. اجرة] (ا.) مزد، مزدکار، دستمزد' — Mo'in's [ع.] tag = Arabic.\"},\n            {\"src\": \"RCH\", \"where\": \"RCH.txt leaf 122 s.v. ujrat\", \"stance\": \"supports\", \"note\": \"'A أجرة ujrat, Reward, recompense, hire, rent, wages' in a Persian-Arabic-English dictionary, marked Arabic.\"},\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt leaf 77 s.v. mizd\", \"stance\": \"partial\", \"note\": \"'mizd [m(y)zd | N muzd] reward, hire, pay. -war [-wbl | N -ur] hireling' — the inherited Iranian word; MacKenzie has no ʾgr-type word, confirming that ajr/ojrat/ejāre are post-conquest Arabic imports.\"},\n            {\"src\": \"HRN\", \"where\": \"grep 'ajr|ijar|uǧrat' in HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss covers only inherited Iranian vocabulary and has no entry — expected for an Arabic loan.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"angelos; eu-angelos; evangelion\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Greek words are of course real: ἄγγελος 'messenger' (Mycenaean a-ke-ro, so attested by the 13th c. BCE), εὐάγγελος 'bringing good news', εὐαγγέλιον originally 'reward given to the bearer of good news', then in the Koine 'good news, gospel'. What is disputed is the arrow. Nourai follows Zimmern (1917), Jeffery (1938) and Klein (1966), who derive Greek ἄγγαρος 'Persian mounted courier' from Akkadian agru/agarru 'hireling' (Klein's semantic ladder 'hireling → hired messenger → messenger'), and then treat ἄγγελος as a doublet of ἄγγαρος; Nourai's gloss 'hired messenger' for angelos is that reconstruction, not an attested Greek sense. Modern scholarship prefers a different Akkadian source: Beekes (EDG 2010) and Tavernier (Iranica in the Achaemenid Period, 2007) derive ἄγγαρος from Old Persian *angara- 'missive, letter' < Aramaic *ʾiggartā / *ʾengartā < Akkadian egirtu 'inscribed tablet, letter', and expressly say it is NOT from agru 'hired man'. Klein himself hedges by citing both etyma (agarru 'hireling' AND Heb. iggereth / Aram. iggartā 'letter') in one breath. Watkins (AHD IE-roots appendix) declines to choose: '[angelos. Messenger. Greek noun, akin to Greek angaros, mounted courier, both from an unknown Oriental source.]'; Skeat says only 'from O. Persian'. So: a Near-Eastern loan — yes, essentially undisputed; from the 'hire' root agāru — a minority, now largely superseded, view. There is also a structural problem with the chart: it hangs Greek off the Syriac node, whereas every version of the Semitic hypothesis routes the word through Persian/Median (ἄγγαρος is a Persian institution — the royal post described by Herodotus 8.98).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E1%BC%84%CE%B3%CE%B3%CE%B5%CE%BB%CE%BF%CF%82\",\n            \"https://en.wiktionary.org/wiki/%E1%BC%84%CE%B3%CE%B3%CE%B1%CF%81%CE%BF%CF%82\",\n            \"https://www.etymonline.com/word/angel\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:74\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 51 (Klein's angel entry; the leaf→page formula puts it at ≈p.74-78, i.e. Nourai's citation): 'Gk. ἄγγελος … which is rel. to ἄγγαρος, \\\"mounted courier, messenger\\\"; of Persian, ult. of Sem. origin. Cp. Akkad, agarru … The sense development of Gk. ἄγγαρος, resp. ἄγγελος, from a Sem. noun meaning \\\"hireling\\\", may be illustrated by the phases: \\\"hireling, hired messenger, messenger\\\".' Klein says precisely what the chart says, including the gloss 'hired messenger'.\"},\n            {\"ref\": \"AHD:453\", \"status\": \"not_checked\", \"note\": \"Nourai's AHD page numbers below 1505 are main-dictionary pages of the 1975/76 New College Edition, which is not open online. The Watkins IE-roots appendix that IS on disk (AHD_watkins1985.txt leaf 32) carries the bracketed non-IE entry '[angelos. Messenger. Greek noun, akin to Greek angaros, mounted courier, both from an unknown Oriental source. 1. Greek angelos, messenger: ANGEL, (ANGELIC), ANGELICA, (ANGELUS); ARCHANGEL, EVANGEL. 2. Greek angaros, mounted courier: ANGARY.]' — the word list matches, the Akkadian etymology does not.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt leaf 32, entry [angelos]\", \"stance\": \"partial\", \"note\": \"'both from an unknown Oriental source' — Watkins accepts an Oriental loan but refuses Nourai's specific Akkadian etymon.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 32 s.v. Angel\", \"stance\": \"contradicts\", \"note\": \"'Angel. (L. - Gk.) L. angelus. - Gk. ἄγγελος, a messenger. Cf. Gk. ἄγγαρος, a [moun]ted courier, from O. Persian.' Skeat makes the source Old Persian, with no Semitic 'hire' word.\"},\n            {\"src\": \"AKD\", \"where\": \"AKD.txt leaf 56 (p.47) and leaf 15 (p.7)\", \"stance\": \"supports\", \"note\": \"Zimmern: 'Zu akk. agru, agarru Mietsklave : > wahrsch. ἄγγαρος Postknecht' and 'wahrsch. auch ἄγγαρος urspr. wohl Mietling und dann erst Postknecht' — the source of Klein's and Nourai's claim; note that Zimmern's Greek word is ἄγγαρος, never ἄγγελος.\"},\n            {\"src\": \"FVQ\", \"where\": \"p.49 n.2 (FVQ_pages.txt leaf 66)\", \"stance\": \"supports\", \"note\": \"Jeffery: 'there can be little doubt that the Gk. ἄγγαρος with ἀγγαρεύειν and ἀγγαρεία came directly from the Akkadian, as indeed Ed. Meyer … had already recognized', arguing against Liddell-Scott's 'borrowing from Persian'.\"},\n            {\"src\": \"POK\", \"where\": \"grep 'angelos' in POK_full.txt\", \"stance\": \"silent\", \"note\": \"Pokorny has no IE root for ἄγγελος — consistent with everyone treating it as a loanword.\"},\n            {\"src\": \"WLD\", \"where\": \"grep 'angelos' in WLD_band3.txt\", \"stance\": \"silent\", \"note\": \"Walde-Pokorny likewise has no entry.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"Angelyŭn «انگلیون»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Persian انگلیون angalyūn 'Gospel' is a real word, used by the Manichaeans (the Ewangelyōn of Mani) and by Persian Christians, and quoted by the chart from Sohbat-e Lārī. Its immediate source is not Greek directly, as the chart's arrow implies, but Syriac ܐܘܢܓܠܝܘܢ ʾewwangelyōn, itself a transliteration of εὐαγγέλιον; the -yūn ending is the tell-tale, since it preserves the Greek/Syriac -ion which the Arabic إنجيل lost. Jeffery expressly cites 'the Manichaean forms انگلیون of Persian origin, and anglion of Turkish origin' as still having 'the Gk. -ιον ending'. The same Syriac form gives Sogdian ʾwnglywn ewangelyon 'Gospel' (Gharib no. 1908), which shows how the word travelled into Iranian: through the Church of the East and the Manichaean church, not through direct contact with Greek. So the node is right about the word and its ultimate Greek etymon, and only its route is loose.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AC%DB%8C%D9%84\"],\n          \"ref_check\": [\n            {\"ref\": \"MON5:190\", \"status\": \"not_checked\", \"note\": \"Volume 5 (اعلام) of Mo'in's six-volume Farhang-e Fārsi is not on disk — only the two-volume Adena abridgement, which has no page correspondence. See the 'consulted' entry for what the abridgement does say.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. انگلیوت/انگلیون\", \"stance\": \"supports\", \"note\": \"'انگلیو[ن]: (اخ.) انجیل؛ انگلیون. (ا.) چون مسیحیان شرقی انجیل را در قماش ابریشمین و ملون می‌پیچیده‌اند، از اینرو …' — Mo'in has the headword with exactly the chart's gloss.\"},\n            {\"src\": \"FVQ\", \"where\": \"p.72 n.1 (FVQ_pages.txt leaf 90)\", \"stance\": \"supports\", \"note\": \"Jeffery: 'the Manichaean forms انگلیون of Persian origin, and anglion of Turkish origin, still have the Gk. -ιον ending' (citing Vullers, Salemann Manichaeische Studien i.50, and BQ 88).\"},\n            {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary no. 1908\", \"stance\": \"supports\", \"note\": \"'1908 ʾwnglywn M, C — ewangelyon — Gospel, Evangelion' — the same Syriac-derived form in Sogdian, showing the Iranian route.\"},\n            {\"src\": \"PHD\", \"where\": \"grep 'ewangel|wnglywn' in PHD_mackenzie.txt\", \"stance\": \"silent\", \"note\": \"MacKenzie's Concise Pahlavi Dictionary (Zoroastrian Book Pahlavi only) has no entry — expected, since the word belongs to Manichaean and Christian Middle Iranian.\"},\n            {\"src\": \"NYB\", \"where\": \"grep 'ewangel|wnglywn' in NYB_vol2_glossary.txt\", \"stance\": \"silent\", \"note\": \"Nyberg's Pahlavi glossary likewise silent.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Arabic\",\n          \"words\": \"enjîl\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Arabic إِنْجِيل ʾinjīl 'Gospel' (Qurʾān iii.2, v.50, lvii.27 etc.) is beyond doubt Greek εὐαγγέλιον, as the chart says; the only question is the intermediary, which the chart's direct Greek→Arabic arrow leaves out. The Muslim philologists' attempt to make it a native form ʾifʿīl from n-j-l is rejected already by Zamakhsharī and Bayḍāwī, and al-Jawāliqī lists it as foreign. Marracci and Fraenkel argued for direct borrowing from Greek; Nöldeke's argument, generally followed, is that the loss of the Greek -ιον ending points to Ethiopic ወንጌል wangēl as the immediate donor (Christian Ethiopia rather than Syria), because the Syriac ʾewwangelyōn and the Manichaean Persian angalyūn both keep the -yōn/-yūn. Wiktionary today gives '(possibly through Classical Syriac ʾewwangellīōn or a variant thereof)'. Either way the node's language label, word and gloss are right and only the transmission line is simplified.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A5%D9%86%D8%AC%D9%8A%D9%84\"],\n          \"ref_check\": [\n            {\"ref\": \"TAD:5\", \"status\": \"supports\", \"note\": \"al-Unaysī, Tafsīr al-alfāẓ al-dākhila, TAD_pages.txt \\\\f-leaf 8 (the following leaf carries the printed numeral ٥, so this is p.4/5 — i.e. Nourai's page within the ±1 the OCR allows): '[إن]جيل يوناني εὐαγγέλιον (إونجيليون) معناه خبر بشارة وبشرى فرح' = 'Injīl: Greek euangelion (ewangeliyūn), meaning good news, glad tidings' — exactly the chart's Greek→Arabic arrow and gloss.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"pp.71-72 s.v. إنجيل (FVQ_pages.txt leaves 89-90)\", \"stance\": \"partial\", \"note\": \"'Obviously it is the Gk. εὐαγγέλιον, and both Marracci and Fraenkel have thought that it came directly into Arabic from the Greek. The probabilities, however, are that it came into Arabic through one of the other Semitic tongues … The shortened form, he [Nöldeke] points out, is to be found in the Eth. ወንጌል where the long vowel is almost conclusive evidence of the Arabic word having come from Abyssinia.' Same origin, different route.\"},\n            {\"src\": \"ARB\", \"where\": \"al-Jawālīqī, al-Muʿarrab (ARB_mo3rb.txt, bāb al-alif)\", \"stance\": \"supports\", \"note\": \"'… فالإنجيل … وقيل: هو … من النجل، وهو الأصل' — al-Jawālīqī records the debate and lists إنجيل among the arabicized (muʿarrab) words, i.e. not native Arabic.\"},\n            {\"src\": \"AFM\", \"where\": \"grep 'انجيل' in AFM_pages.txt\", \"stance\": \"silent\", \"note\": \"Addi Shir's book covers Persian loans only, so the Greek/Syriac word is absent — expected.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 51 s.v. angel\", \"stance\": \"partial\", \"note\": \"Klein covers evangel from εὐαγγέλιον ('Cp. … the second element in evangel') but says nothing about the Arabic.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"enjîl «انجیل»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian انجیل enjīl 'Gospel, the Bible' is a straight borrowing of Arabic إِنْجِيل ʾinjīl, taken over with the rest of the Qurʾānic religious vocabulary after the conquest; the Persian pronunciation simply drops the initial hamza. It is a doublet of the older, Syriac-derived انگلیون angalyūn (node #5), which it displaced. Mo'in marks it explicitly as arabicized-from-angalyūn, so the chart's Greek > Arabic > Persian order for this node is exactly Mo'in's.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AC%DB%8C%D9%84\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:369\", \"status\": \"partial\", \"note\": \"The 6-vol page 369 could not be located (only the unpaginated 2-vol abridgement is on disk), but Mo'in's entry itself is there: MON_part1.txt 'انجیل: [معر. … < انگلیون] (اخ.) هر یک از چهار کتاب دینی مسیحیان؛ ج. اناجیل' — 'arabicized … from angalyūn', which is the chart's claim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. انجیل\", \"stance\": \"supports\", \"note\": \"'[معر. … < انگلیون] (اخ.) هر یک از چهار کتاب دینی مسیحیان؛ ج. اناجیل' — معرّب = arabicized.\"},\n            {\"src\": \"RCH\", \"where\": \"RCH.txt (Persian-Arabic-English)\", \"stance\": \"partial\", \"note\": \"Richardson carries انجیل as an Arabic-marked headword in the Persian dictionary; the OCR of the entry itself is too damaged to quote verbatim.\"},\n            {\"src\": \"BQT\", \"where\": \"grep انجیل in BQT_v1_pages.txt / BQT_v2_pages.txt\", \"stance\": \"silent\", \"note\": \"Borhān-e Qāṭeʿ has no etymological footnote for the word in the volumes on disk.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"angel, Los Angeles, Evangelical\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek ἄγγελος → Late Latin angelus (the Church Latin borrowing, used in the Vulgate to render Hebrew malʾāḵ) → Old French angele/angle, which about 1300 blended with the inherited Old English engel (itself an early Latin loan) to give Middle English, then Modern English, angel. Evangelical is Late Latin evangelicus < Greek εὐαγγελικός, from εὐαγγέλιον; the ecclesiastical sense-history runs through the Vulgate and the Reformation. Los Angeles is Spanish, from the 1781 Spanish foundation 'El Pueblo de Nuestra Señora la Reina de los Ángeles', Spanish ángeles being the same Latin angelus. All three English/Spanish forms therefore do descend from the Greek node as drawn; only the origin of the Greek word itself (node #4) is in dispute.\",\n          \"sources\": [\"https://www.etymonline.com/word/angel\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt leaf 32, bracketed entry '[angelos … 1. Greek angelos, messenger: ANGEL, (ANGELIC), ANGELICA, (ANGELUS); ARCHANGEL, EVANGEL. 2. Greek angaros, mounted courier: ANGARY.]' — the appendix lists ANGEL and EVANGEL under the Greek word exactly as the chart does, but gives the source as 'unknown Oriental', and of course does not treat the place-name Los Angeles.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 51 s.v. angel\", \"stance\": \"supports\", \"note\": \"'angel, n. — ME., fr. OF. angele (F. ange), fr. L. angelus, fr. Gk. ἄγγελος … Cp. angaria, the first element in Ingram and the second element in evangel.'\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 32 and leaf 606 (Corrections)\", \"stance\": \"supports\", \"note\": \"'Angel. (L. - Gk.) L. angelus. - Gk. ἄγγελος, a messenger'; the Corrections add 'The A.S. form is engel, from Latin. Afterwards altered by F. … influence' — the OE/OF blend.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt\", \"stance\": \"supports\", \"note\": \"Webster's Twentieth Century likewise routes angel ME < OF < LL angelus < Gk. angelos.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Agaruh\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Sanskrit अगरु agaru- / अगुरु aguru- 'agarwood, aloeswood (Aquilaria agallocha)' — itself a loan from Dravidian (cf. Old Tamil akil)\",\n      \"note\": \"The root word is real and the gloss is right (the citation form is agaru-/aguru-; the chart's 'Agaruh' is the nominative singular agaruḥ). Two reservations. (1) Sanskrit is not the ultimate source: Klein already writes 'prob. of Dravidian origin', and current work (Burrow-Emeneau; D. Shulman) makes both the Sanskrit word and the Hebrew one borrowings from Old Tamil akil 'eagle-wood'. (2) More seriously, this chart merges two etymologically distinct families under one root. The genuine agaru- family is aguru → Hebrew ʾăhālīm/ʾăhālōt → Greek ἀλόη → Latin aloē → English aloe (plus Greek ἀγάλλοχον, Portuguese aguila, English eagle-wood). The lute family is Arabic al-ʿūd 'the wood', from the native Semitic root ʿ-w-d, → Old Provençal laüt → Old French lut/luth → English lute. Klein — the very reference Nourai cites for the root, KLN:55 — keeps them apart, and so does every modern source consulted. The two Arabic-headed branches of this chart (#1 Arabic al-oud and #6 Hebrew alôth from Arabic) are the errors; the sub-chains hanging off them (#2-#5, #7-#9) are individually sound.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%97%E0%A4%B0%E0%A5%81\",\n        \"https://en.wiktionary.org/wiki/%E1%BC%80%CE%BB%CF%8C%CE%B7\",\n        \"https://www.etymonline.com/word/aloe\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:55\", \"status\": \"partial\", \"note\": \"KLN_1966.txt \\\\f-leaf 41 (≈ printed p.55-58), s.v. aloe: 'L. aloe, fr. Gk. ἀλόη, \\\"aloe\\\", prob. borrowed fr. Heb. ahalim, ahaloth (pl.), which are perhaps borrowed fr. OI. agaruh, aguruh, \\\"aloewood\\\", these latter being prob. of Dravidian origin. Cp. agalloch.' Klein gives the root word and gloss Nourai gives — but he makes it the source of the HEBREW, never of Arabic al-ʿūd, and he flags Dravidian behind the Sanskrit.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"al-oud\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Arabic عُود ʿūd 'wood, stick, branch; aromatic (agar)wood; lute', with the article al-ʿūd, is a native Semitic noun of the root ع و د ʿ-w-d (cf. عَادَ ʿāda 'to return, bend back', of a pliant branch); a Ugaritic cognate ʿd 'lute' is attested more than a millennium before any Indian contact. Sanskrit agaru- cannot give it: there is no source for the ʿayn, the g/r skeleton is lost, and the Arabic word's core sense is 'wood/stick' in general, not 'aloeswood' specifically. Klein, on the page Nourai cites for this arrow (KLN:55, s.v. aloe), routes Sanskrit agaruh to HEBREW, and in his separate lute entry derives al-ʿūd simply from 'al-, \\\"the\\\", and ʿūd, \\\"wood\\\"' with no Indian element; Etymonline, Wiktionary and Skeat agree. There is an old Arab-lexicographic tradition (al-Aṣmaʿī, reported by al-Jawālīqī and Addi Shir) that the incense-wood sense of العود is muʿarrab, i.e. foreign — but the language named there is Persian, not Sanskrit, and it concerns only the aromatic-wood sense. The chart also mis-parses the gloss: 'the wood' is al-ʿūd (article + noun), so 'al-oud' should not itself be treated as a stem. Verdict: the word and its meanings are real, but the derivation from Sanskrit agaru- is rejected by modern scholarship and is not what Nourai's own reference says.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B9%D9%88%D8%AF\",\n            \"https://www.etymonline.com/word/lute\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:55\", \"status\": \"contradicts\", \"note\": \"KLN_1966.txt leaf 41, s.v. aloe: Klein takes Gk. ἀλόη from Heb. ahalim/ahaloth 'which are perhaps borrowed fr. OI. agaruh, aguruh' — Hebrew, not Arabic. And KLN_1966.txt leaf 492, s.v. lute (stringed instrument): 'fr. OProven[çal] laüt, fr. Arab. al-ʿūd …, lit. \\\"the wood\\\", fr. al-, \\\"the\\\", and ʿūd, \\\"wood\\\"' — no Sanskrit anywhere. Klein does not support the arrow Nourai draws from him.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaves 41 and 492\", \"stance\": \"contradicts\", \"note\": \"See ref_check: Klein keeps the aloe family and the ʿūd/lute family separate.\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan p.240 (PHN.txt leaf 271) s.v. LUTH\", \"stance\": \"partial\", \"note\": \"'العود [al-ʿoud] le bois en général, et en particulier le bois d'aloès' — Pihan glosses al-ʿūd as 'wood in general, and in particular aloes-wood', i.e. Arabic wood-word applied to the aromatic wood; he derives nothing from Sanskrit.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, AFM_pages.txt leaf 13 (≈ printed p.5)\", \"stance\": \"partial\", \"note\": \"OCR badly damaged but legible in outline: '… العود … قال الأصمعي فهو فارسي معرَّب … قلت … والفرنسي aloès والانكليزي … والايطالي …' — Addi Shir cites al-Aṣmaʿī that العود is an arabicized PERSIAN word and lines it up with French aloès; a foreign-origin claim, but Persian, not Sanskrit.\"},\n            {\"src\": \"ARB\", \"where\": \"al-Jawālīqī, al-Muʿarrab (ARB_mo3rb.txt, bāb al-alif)\", \"stance\": \"partial\", \"note\": \"'… العود الذي يُتبخَّر به … أبو عبيد أنه معرَّب' and '… أحد أوتار العود … أعجمي معرَّب' — the medieval Arab tradition that the incense-wood ʿūd (and a lute-string name) are foreign; again no Indian etymon is named.\"},\n            {\"src\": \"PLA\", \"where\": \"grep ʿūd in PLA_pages.txt (Asbaghi)\", \"stance\": \"silent\", \"note\": \"Asbaghi does not list عود among Persian loanwords in Arabic.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 286 s.v. Lute (1)\", \"stance\": \"contradicts\", \"note\": \"'The Port. form shews the Arab. [article] since a- is for al, the Arab. def. [article] … ʿūd, wood, timber, a staff, stick, … lute, a harp' — native Arabic wood-word, no Sanskrit.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"ŭd «عود»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian عود ʿud is borrowed from Arabic عُود ʿūd, in both of the senses the chart gives: (a) the aromatic wood burnt as incense (agarwood), and (b) the short-necked lute. The Arabic ʿayn is retained in spelling and in the classical Persian orthography, which is itself proof of the Arabic (not Indian) source. The direction of borrowing is Arabic → Persian for the word, even though the instrument itself descends from the pre-Islamic Persian barbaṭ — hence Mo'in's note that the Islamic-period ʿūd appears in the north-east with a bent-back pegbox and a skin belly. The chart's Arabic → Persian arrow is therefore right; only its parent (node #1) is wrong.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B9%D9%88%D8%AF\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1385\", \"status\": \"supports\", \"note\": \"Rendered with tools/ref_page.py BQT:1385 → BQT_v3_picofile.pdf pdf-page 178; the running head on the image actually reads ۱۳۸۰, so the entry sits on p.1380 rather than 1385 (noted for re-runs). The عود entry is there: 'عود ـ بضم اول و سکون ثانی … معروف است، و آن چوبی باشد سیاه رنگ که بجهت بخور سوزانند … و نام سازی هم هست که نوازند.' Mo'in's footnote 4: 'آلت طرب دارای ۶ یا ۲۰ سیم «نفس». کلمهٔ انگلیسی lute فرانسوی luth مأخوذ از (العود) عربی است.' Footnote 3: '(عر) «عود بالضم چوب … و چوبی است که دخان آن بوی خوش دارد» «منتهی‌الارب» ـ اگر (هندی) = رادبوی = داربوی = Aloë (آلمانی) «پورداود، خرده‌اوستا ص۱۳۹ و ۱۴۶» فرانسوی aloés.' Mo'in tags the word (عر) = Arabic, confirms the two senses, and confirms lute/luth < al-ʿūd; his equation with Hindi اگر 'agar' is a list of foreign equivalents of the substance, not a derivation. Saved verbatim to data/verification/sources/refs/ocr/BQT/1385.vision.txt.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ ed. Mo'in, p.1380 s.v. عود, footnotes 3-4\", \"stance\": \"supports\", \"note\": \"See ref_check — Mo'in marks عود as (عر) Arabic and gives both senses.\"},\n            {\"src\": \"MON\", \"where\": \"grep عود in MON_part1/2.txt\", \"stance\": \"silent\", \"note\": \"The 2-vol Adena abridgement of Farhang-e Fārsi does not carry a usable عود entry in the OCR.\"},\n            {\"src\": \"RCH\", \"where\": \"RCH.txt (Persian-Arabic-English)\", \"stance\": \"partial\", \"note\": \"Richardson has عود ʿūd 'wood, aloes-wood, a lute' marked A(rabic) in the Persian dictionary; the OCR of the line is too corrupt to quote exactly.\"},\n            {\"src\": \"HRN\", \"where\": \"grep 'ud|aloe' in HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss treats only inherited Iranian words; an Arabic loan is not in scope.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"French\",\n          \"words\": \"luth; flute\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"luth: Arabic al-ʿūd was borrowed in the Iberian/Occitan contact zone — Spanish laúd, Portuguese alaúde (which keeps the whole article, the proof of the etymology), Old Provençal laüt — and thence Old French lut, modern French luth; the Arabic ʿayn is lost, al- is reanalysed into the l- of the stem in French/Provençal but preserved intact in Portuguese. This half is certain and is precisely what Pihan p.240 and Klein s.v. lute say. flute: the chart's own hedge is the right answer. French flûte goes back to Old French flaüte/fleüte < Old Provençal flaüt, which is either imitative or from Latin flāre 'to blow'; Klein and Etymonline both treat it as at most a blend or a contamination — Klein: 'OProvenç. flaüt, which is prob. a blend of OProvenç. flaujol, \\\"flageolet\\\", and laüt, \\\"lute\\\"'. So flute shares only the second syllable's shape with lute, by contamination, and is not a descendant of Arabic al-ʿūd. Node verdict takes the weaker of the two words.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/lute\",\n            \"https://www.etymonline.com/word/flute\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"PHN:240\", \"status\": \"supports\", \"note\": \"PHN.txt \\\\f-leaf 271, page header '240 LUT': 'LUTH, s. m. (a.) العود [al-ʿoud] le bois en général, et en particulier le bois d'aloès. Nom d'un instrument de musique à cordes … on y parvient, soit à l'aide de l'espagnol laud, soit au moyen du portugais alaude, dans lequel l'article al figure intégralement.' Pihan's page is exactly the chart's Arabic → French luth arrow.\"},\n            {\"ref\": \"KLN:605,914\", \"status\": \"supports\", \"note\": \"Both entries located and both say what the chart says, though the leaf→page formula puts them slightly higher than Nourai's numbers (the offset drifts across the two volumes). KLN_1966.txt leaf 327 s.v. flute: 'ME. floute, floite, fr. OF. flaüte, fleüte (F. flûte), fr. OProvenç. flaüt, which is prob. a blend of OProvenç. flaujol, \\\"flageolet\\\", and laüt, \\\"lute\\\".' KLN_1966.txt leaf 492 s.v. lute (a stringed instrument): 'ME., fr. OF. lut (F. luth), fr. OProvenç. laüt, fr. Arab. al-ʿūd …, lit. \\\"the wood\\\".'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaves 327 (flute) and 492 (lute)\", \"stance\": \"supports\", \"note\": \"See ref_check; Klein is the source of the chart's own 'probably from another root' hedge on flute.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 286 s.v. Lute (1)\", \"stance\": \"supports\", \"note\": \"'Lute (1), a musical instrument (F. - Arab.) M.E. lute. - F. lut … F. luth. We also find Prov. laut, Port. alaude, Ital. liuto … The Port. form shews the Arab. [article].'\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ ed. Mo'in p.1380 n.4\", \"stance\": \"supports\", \"note\": \"'کلمهٔ انگلیسی lute فرانسوی luth مأخوذ از (العود) عربی است' — 'English lute, French luth are taken from Arabic al-ʿūd'.\"},\n            {\"src\": \"DEV\", \"where\": \"grep 'LUTH|aloès' in DEV.txt\", \"stance\": \"silent\", \"note\": \"Devic's Dictionnaire des mots français d'origine orientale has no separate luth article in the OCR (hits are only incidental uses of 'luth' glossing Persian چنگ).\"},\n            {\"src\": \"LKT\", \"where\": \"grep 'Laute|al-ʿud' in LKT.txt\", \"stance\": \"partial\", \"note\": \"Lokotsch no. 1585 (Turkish öd ağacı) notes 'Es liegt wohl schon im tk. Grundwort Kontamination mit ar. ʿūd, s. hier Nr. 2127, vor' — Lokotsch treats ar. ʿūd as an Arabic word in its own right.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"folŭt «فلوت»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian فلوت folut is a modern European loan, taken from French flûte during the 19th-20th century wave of French technical and musical vocabulary in Persian (like پیانو, ویولن, ارکستر). The French final -e is dropped and the vowel rendered ū; there is no older Persian attestation and no Iranian pedigree. Mo'in's entry describes it purely as an instrument definition, without any Persian etymon: 'نوعی نی تکمیل‌شده … در موسیقی عملی نیز بکار برده می‌شود'. The chart's French → Persian arrow is right.\",\n          \"sources\": [\"https://www.etymonline.com/word/flute\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:2573\", \"status\": \"partial\", \"note\": \"The 6-vol page could not be reached (only the unpaginated Adena abridgement is on disk), but the entry is present there: MON_part2.txt 'فلوت: (مس.) نوعی نی تکمیل‌شده … در موسیقی عملی نیز بکار برده می‌شود. با فلوت به سهولت می‌توان صداهای مختلف را اجرا کرد ولی چون فاقد پرده‌های مخصوص موسیقی ماست، نواختن نغمه‌های ایرانی در روی این ساز مشکل است.' Mo'in gives a Latin-script source form in the head (illegible in OCR); the neighbouring homonym فلوت 'fleet' is explicitly tagged (فر.) = French.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt s.v. فلوت\", \"stance\": \"supports\", \"note\": \"Entry present, defined as the modern transverse flute; the parallel entry فلوت 'a state's warships' is tagged (فر.) French, showing Mo'in's practice for these loans.\"},\n            {\"src\": \"BQT\", \"where\": \"grep فلوت in BQT_v1/v2_pages.txt\", \"stance\": \"silent\", \"note\": \"Borhān-e Qāṭeʿ is a 17th-century dictionary and naturally has no entry for a 19th-century French loan — itself evidence that the word is recent.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"lute, flute\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"lute: Middle English lute/lut, borrowed from Old French lut (mod. luth) in the 14th century, ultimately Arabic al-ʿūd. flute: Middle English floute/floite, from Old French flaüte/fleüte, early 14th century; the modern spelling follows the French. Both English words are unproblematic borrowings from the French node above; the only caveat is inherited from node #3, namely that flute's ancestor is not the Arabic word. Note that the English homonym lute 'clay sealing compound' is unrelated (Latin lutum 'mud'), and Watkins puts that one, and only that one, under the IE root leu- 'dirt' — a useful check that the appendix keeps the two apart.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/lute\",\n            \"https://www.etymonline.com/word/flute\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:776\", \"status\": \"not_checked\", \"note\": \"p.776 is a main-dictionary page of the 1975/76 AHD New College Edition, which is not open online. The Watkins IE-roots appendix that is on disk (AHD_watkins1985.txt leaf 66) contains only LUTE² 'clay' under leu-2 'dirt; to make dirty', i.e. the appendix deliberately excludes the musical lute as a non-IE loan — consistent with, but not a check on, Nourai's page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaves 327, 492\", \"stance\": \"supports\", \"note\": \"'lute, n., a stringed instrument. — ME., fr. OF. lut (F. luth), fr. OProvenç. laüt, fr. Arab. al-ʿūd'; 'flute, n. — ME. floute, floite, fr. OF. flaüte, fleüte (F. flûte)'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 286\", \"stance\": \"supports\", \"note\": \"'Lute (1), a musical instrument (F. - Arab.) M.E. lute.'\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt leaf 66 (root leu-2) and leaf 33 (aulo-)\", \"stance\": \"partial\", \"note\": \"Only LUTE² (< L. lutum 'mud') is in the IE appendix; the instrument is absent because it is a Semitic loan.\"},\n            {\"src\": \"FSD\", \"where\": \"grep 'lute, n' in FSD_vol3.txt\", \"stance\": \"silent\", \"note\": \"Funk & Wagnalls OCR did not yield a readable lute entry (only octave-flute compounds).\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Hebrew\",\n          \"words\": \"alôth\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The word is real: Biblical Hebrew אֲהָלוֹת ʾăhālōt / אֲהָלִים ʾăhālīm 'aloes, aloeswood', at Numbers 24:6, Psalm 45:9, Proverbs 7:17 and Song of Songs 4:14 (the chart's 'alôth' drops the h of ʾăhālōt). But the parent is wrong. These are pre-exilic attestations, centuries before Arabic could have mediated anything, and the Hebrew word has the -h- and the l/h skeleton of the Indian/Dravidian word, not the ʿayn of Arabic ʿūd. Klein — the reference Nourai cites for this whole entry — derives Hebrew ahalim/ahaloth straight from Old Indian agaruh/aguruh; Hobson-Jobson s.v. ALOES says aloes-wood is 'perhaps from one of the Indian forms, through the Hebrew (pl. forms) ahalim, ahalim and ahaloth, akhaloth'; and current work (Shulman, cited by Wiktionary) makes ʾăhālīm a direct borrowing from Old Tamil akil rather than from Sanskrit aguru. In other words this node should hang directly off the root box, not off Arabic al-ʿūd.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%97%E0%A4%B0%E0%A5%81\",\n            \"https://en.wiktionary.org/wiki/%E1%BC%80%CE%BB%CF%8C%CE%B7\",\n            \"https://www.etymonline.com/word/aloe\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"PRT:13\", \"status\": \"not_checked\", \"note\": \"Partridge, Origins (1958) is not in the local library and the archive.org copy (originsshortetym00part) is lending-only, so p.13 could not be read.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 41 s.v. aloe\", \"stance\": \"contradicts\", \"note\": \"'prob. borrowed fr. Heb. ahalim, ahaloth (pl.), which are perhaps borrowed fr. OI. agaruh, aguruh, \\\"aloewood\\\"' — Sanskrit to Hebrew directly, with no Arabic step.\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. ALOES (HJB.txt leaf 69)\", \"stance\": \"contradicts\", \"note\": \"'b. Aloes-wood, the same as Eagle-wood. This is perhaps from one of the Indian forms, through the Hebrew (pl. forms) ahalim, akhalim and ahaloth, akhaloth.' Indian → Hebrew, no Arabic.\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan p.35-36 s.v. ALOES (PHN.txt leaves 67-68)\", \"stance\": \"partial\", \"note\": \"Pihan tags the article '(p.-a.)' Persian-Arabic and starts from الوّة [alwā]; he then says 'Comparez avec le persan le grec ἀλόη et le latin aloe' and notes that the fragrant wood 'sappelle عود [ʿoud] et العود [al-ʿoud] en arabe' — he keeps the aloe word and the ʿūd word as two separate names for the substance.\"},\n            {\"src\": \"FVQ\", \"where\": \"grep 'ahal|aloe' in FVQ_pages.txt\", \"stance\": \"silent\", \"note\": \"Jeffery has no entry (the word is not Qurʾānic).\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Greek\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The unlabelled Greek node stands for ἀλόη 'aloe', first in Dioscorides (Materia Medica iii.3, 1st c. CE) and in John 19:39 (σμύρνης καὶ ἀλόης); the word is absent from Hippocrates and Theophrastus, so it enters Greek only with the Roman-period trade in the drug. Everyone agrees it is an Oriental loan; the disagreement is over the immediate donor. Klein (and Nourai following him at the top of this entry) says 'prob. borrowed fr. Heb. ahalim, ahaloth'; the current treatment (Beekes; Wiktionary) has it enter Greek through Aramaic in the 1st c. CE — cf. Syriac and Christian Palestinian Aramaic cognates — with the ultimate source Old Tamil akil. Either way the node's position between the Semitic word and Latin is right; only 'Hebrew' vs 'Aramaic' as the exact donor is open. Greek -η renders the Semitic feminine plural ending, and the word was declined as a first-declension feminine.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%E1%BC%80%CE%BB%CF%8C%CE%B7\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart gives no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 41 s.v. aloe\", \"stance\": \"supports\", \"note\": \"'L. aloe, fr. Gk. ἀλόη, \\\"aloe\\\", prob. borrowed fr. Heb. ahalim, ahaloth (pl.)'.\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. ALOES (HJB.txt leaf 69)\", \"stance\": \"supports\", \"note\": \"'Neither Hippocrates nor Theophrastus mentions aloes, but Dioscorides describes two kinds of it (Mat. Med. iii.3)'; the drug sense is 'derived from the Syriac ʿelwai (in P. ahwa)'.\"},\n            {\"src\": \"POK\", \"where\": \"grep for an IE root behind ἀλόη in POK_full.txt\", \"stance\": \"silent\", \"note\": \"Pokorny has no entry — as expected for a loanword.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 274 s.v. Lign aloes\", \"stance\": \"supports\", \"note\": \"'A sort of translation of L. lignum aloes, lit. \\\"wood of aloes.\\\" Aloes is gen. of aloe, from Gk. ἀλόη, aloe.'\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Unlabelled node = Latin aloē, -ēs, a straight learned borrowing of Greek ἀλόη retaining the Greek first-declension inflection; it is the form Pliny uses ('The best Aloe is brought out of India', Nat. Hist. xxvii) and the form of the Vulgate at John 19:39, whence it passed into every medieval European pharmacopoeia. Latin also formed the compound lignum aloēs 'aloes-wood', the source of English lign-aloes.\",\n          \"sources\": [\"https://www.etymonline.com/word/aloe\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart gives no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 41 s.v. aloe\", \"stance\": \"supports\", \"note\": \"'aloe, n. — L. aloe, fr. Gk. ἀλόη'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 274\", \"stance\": \"supports\", \"note\": \"'L. lignum aloes, lit. \\\"wood of aloes.\\\" Aloes is gen. of aloe, from Gk. ἀλόη'.\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. ALOES, quotation (a) c. A.D. 70\", \"stance\": \"supports\", \"note\": \"'The best Aloe (Latin the same) is brought out of India' — Pliny, Bk. xxvii, in Philemon Holland's translation.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt leaf 73 s.v. aloe\", \"stance\": \"supports\", \"note\": \"'[… Gr. aloē, the aloe.] a genus of plants of the lily family' — Webster routes the English word through Latin from Greek.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"aloe\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English had alewe/aluwe 'fragrant resin or heartwood of an East Indian tree', borrowed early from Latin aloē; the modern form aloe was re-Latinised in the late 14th century, when the sense shifted to the bitter purgative drug of Aloe socotrina and then to the succulent plant itself (the modern 'aloe vera' label was coined to distinguish the true plant after the name was misapplied to the American agave in the 1680s). The OE sense 'aloeswood' comes from the Vulgate's use of aloē to render Hebrew ʾăhālōt, which is why English inherited both the drug and the incense-wood senses under one word. The chart's Latin → English arrow is correct.\",\n          \"sources\": [\"https://www.etymonline.com/word/aloe\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:36\", \"status\": \"not_checked\", \"note\": \"p.36 of the 1975/76 AHD New College Edition (main dictionary) is not open online; the Watkins IE-roots appendix on disk has no 'aloe' entry, correctly, since the word is a loan.\"},\n            {\"ref\": \"PHN:36\", \"status\": \"partial\", \"note\": \"PHN.txt \\\\f-leaves 67-68, entry beginning 'ALOES, s. m. (p.-a.)' with the running head 'ALO 35' on the preceding page: Pihan starts from الوّة [alwā] and adds 'Comparez avec le persan le grec ἀλόη et le latin aloe, d'où vient par suite le mot français' — he confirms the Greek → Latin → French/English line the chart draws, but makes the ultimate source a Persian/Arabic word, not Hebrew or Sanskrit.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 41 s.v. aloe\", \"stance\": \"supports\", \"note\": \"'aloe, n. — L. aloe, fr. Gk. ἀλόη … Cp. agalloch.'\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt leaf 73\", \"stance\": \"supports\", \"note\": \"'al'oe, n.; pl. al'oes, any plant of the genus Aloe, as Aloe socotrina, one of the species used in medicine' with '[… Gr. aloē, the aloe.]'\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 274 s.v. Lign aloes\", \"stance\": \"supports\", \"note\": \"'Aloes is gen. of aloe, from Gk. ἀλόη, aloe. See Aloe.'\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. ALOES (HJB.txt leaf 69)\", \"stance\": \"supports\", \"note\": \"Distinguishes the two English senses (the drug from Aloe socotrina; aloes-wood = eagle-wood) exactly as the etymology requires.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-36.json > /dev/null && echo \"VALID JSON\"",
 "description": "Write page-36.json"
}
```


### [2026-09-04T18:46:05.875Z] TOOL RESULT

```
VALID JSON
```


## [2026-09-04T18:46:09.870Z] TOOL CALL #56: Bash

```json
{
 "command": "python3 tools/verify_check.py 36",
 "description": "Run verify_check for page 36"
}
```


### [2026-09-04T18:46:11.442Z] TOOL RESULT

```
nodes verified: 17/17
node verdicts: {'confirmed': 10, 'disputed': 3, 'plausible': 4}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 8, 'partial': 5, 'not_checked': 7, 'contradicts': 1}
books consulted: {'supports': 34, 'silent': 17, 'partial': 12, 'contradicts': 5} | by book: {'KLN': 10, 'SKT': 8, 'FVQ': 5, 'MON': 5, 'RCH': 4, 'BQT': 4, 'HJB': 4, 'WEB': 3, 'AKD': 2, 'PLA': 2, 'PHD': 2, 'HRN': 2, 'AHD': 2, 'POK': 2, 'ARB': 2, 'AFM': 2, 'PHN': 2, 'AFA': 1, 'WLD': 1, 'SOD': 1, 'NYB': 1, 'DEV': 1, 'LKT': 1, 'FSD': 1}
```


## [2026-09-04T18:46:29.821Z] AGENT

Page 36 (book p.6) verified — `data/verification/page-36.json` written, `verify_check.py 36` clean (17/17 nodes, no PROBLEM lines).

**Counts** — node verdicts: 10 confirmed, 4 plausible, 3 disputed. Root verdicts: 1 confirmed (Akkadian *agāru*), 1 plausible (Sanskrit *agaru-*). Ref checks: 8 supports, 5 partial, 1 contradicts, 7 not_checked. 24 different books consulted.

**Disputed items**
- *Agaru* / **#4 Greek angelos, eu-angelos, evangelion** — Nourai follows Zimmern (AKD:47), Jeffery (FVQ:49) and Klein (KLN:74), who derive Gk. ἄγγαρος/ἄγγελος from Akk. *agru* "hireling". Beekes (EDG 2010) and Tavernier (2007) instead derive ἄγγαρος from OP *\*angara-* "missive" ← Aram. *ʾiggartā* ← Akk. *egirtu* "letter", explicitly **not** from *agru*; Watkins says only "unknown Oriental source", Skeat "from O. Persian". Also the chart hangs Greek off Syriac, whereas every version of the hypothesis routes it through Persian/Median.
- *Agaruh* / **#1 Arabic al-oud** — Arabic عُود is native Semitic (root ع و د; Ugaritic *ʿd* "lute"), not from Skt. *agaru-*; no source for the ʿayn. Klein on the very page cited (KLN:55) sends *agaruh* to **Hebrew**, and s.v. *lute* derives *al-ʿūd* from *al-* + *ʿūd* "wood". Old Arab tradition (al-Aṣmaʿī, via Jawālīqī and Addi Shir) calls the incense-wood sense *muʿarrab* from **Persian**, never Sanskrit.
- *Agaruh* / **#6 Hebrew alôth** — parent should be the root box, not Arabic: אֲהָלוֹת is pre-exilic (Num 24:6, Prov 7:17, Song 4:14), centuries before Arabic mediation. Klein and Hobson-Jobson both route it Indian → Hebrew; Shulman/Wiktionary now prefer direct Old Tamil *akil*.

**Data note (not flagged as a verdict):** entry 0 node #2 is transcribed `a`jara`; the verb is أَجَرَ *ʾajara* (root ʾ-j-r, hamza). The chart uses the same backtick for ʿayn elsewhere on the page, so this looks like a hamza/ʿayn confusion between print and JSON. Zimmern and Klein both write it with the hamza.

**New artefacts:** `data/verification/sources/refs/ocr/BQT/1385.{png,vision.txt}` (the عود entry with Mo'in's footnotes — note the running head reads **1380**, not 1385; it is BQT_v3 pdf page 178), plus 12 archived web pages under `data/verification/sources/web/`.
