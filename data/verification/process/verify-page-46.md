# Verification process log — verify-page-46


## [2026-09-04T19:25:33.171Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 46 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-46.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-46.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-46.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 46` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T19:25:35.106Z] AGENT

I'll start by reading the instructions.


## [2026-09-04T19:25:37.345Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:25:37.360Z] TOOL RESULT

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


## [2026-09-04T19:25:37.504Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-46.txt"
}
```


### [2026-09-04T19:25:37.517Z] TOOL RESULT

```
1	=== PDF page 46 (book page 16) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Al 2 : to grind  (refs POK:28)
4	#1 (parent #0) [Avestan] refs=POK:28 | aša 1, arta 1 : to grind
5	  #2 (parent #1) [Persian] refs=HRN:5; BQT:31 | ârd «آرد» : flour
6	#3 (parent #0) [Sogdian] refs=SOD:59 | `rtk : flower
7	#4 (parent #0) [Greek] refs=AHD; KLN:47 | alein : to grind ; al-euron : wheat flour
8	  #5 (parent #4) [English] refs=None | aleurone
9	
```


## [2026-09-04T19:25:42.379Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-46.json; echo \"=== MATRIX ===\"; cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T19:25:42.425Z] TOOL RESULT

```
{
  "pdf_page": 46,
  "book_page": 16,
  "entries": [
    {
      "root": {
        "name": "Al 2",
        "lang": "Indo-European",
        "refs": "POK:28",
        "gloss": "to grind"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:28",
          "words": [
            {"translit": "aša 1, arta 1", "gloss": "to grind", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:5; BQT:31",
          "words": [
            {"translit": "ârd", "gloss": "flour", "script": "آرد"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:59",
          "words": [
            {"translit": "`rtk", "gloss": "flower", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD; KLN:47",
          "words": [
            {"translit": "alein", "gloss": "to grind", "script": null},
            {"translit": "al-euron", "gloss": "wheat flour", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "aleurone", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== MATRIX ===
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


## [2026-09-04T19:25:44.287Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','HRN','BQT','SOD','AHD','KLN','WLD','IEC','SYN','MON','HUB','BRT','SKT','FSD','WEB','CHEUNG','PHD','NYB','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-04T19:25:46.078Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
CHEUNG null
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root,
```


## [2026-09-04T19:25:53.900Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','HRN','BQT','SOD','AHD','KLN']:\n    print('=====',k)\n    print(json.dumps(d.get(k), ensure_ascii=False, indent=1))\n\""
}
```


### [2026-09-04T19:25:55.485Z] TOOL RESULT

```
===== POK
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
 ],
 "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}
===== HRN
{
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
===== BQT
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt"
 ],
 "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').",
 "covers_etymology": true,
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209",
 "scans": [
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
 ],
 "cites": "page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material"
}
===== SOD
{
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
===== AHD
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
===== KLN
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
```


## [2026-09-04T19:26:01.920Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: al\" POK_full.txt | head -40"
}
```


### [2026-09-04T19:26:01.967Z] TOOL RESULT

```
3858:It seems that Root/ lemma: alca- {more properly ak^i): ek"-: (water, river) derived from 
4144:Root / lemma: aleq- 
4192:Root / lemma: alg"!!- 
4217:Root / lemma: al-1, ol- 
4223:Root/ lemma: al-1, ol-\ "besides; other' derived from Root/ lemma: ala\ interjection. 
4382:Root / lemma: al-2 
4446:clearly alb. shows that from Root / lemma: al-2\ " to grow; to bear; grove' derived Root/ 
4473:Root / lemma: al-4 
4495:Root / lemma: al-5{*hel-) 
4579:Root / lemma: alu-{-d-, -t-) 
5527:Root/ lemma: al-1, ol-\ "besides; other' into *alny-, *any-. 
9043:Root / lemma: al-3 
9102:Root / lemma: alu-, alo- {*halu-) 
25389:clearly alb. shows that from Root/ lemma: al-2\ (to grow; to bear; grove) derived Root/ 
27627:Root/ lemma: er(a)d-{er/a/d-), er(a)6!^-\ "high; to grow' derived from Root/ lemma: al-2\ 
69256:older Latin volpes 'fox', gr. alopex a fox. Root / lemma: alp-, lup- : [a kind of carnivore (fox, 
83350:Root/ lemma: alca- {more properly alcS). ek"-
```


## [2026-09-04T19:26:02.493Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 28\" POK_full.txt | head -20; echo ---; grep -n \"aleuron\\|ἄλευρον\\|aleyron\" POK_full.txt | head"
}
```


### [2026-09-04T19:26:02.555Z] TOOL RESULT

```
4493:Page(s): 28 
4533:Page(s): 28-29 
24006:Page(s): 287 
24067:Page(s): 289-290 
24235:Page(s): 287-289 
26183:Page(s): 281-286 
29133:Page(s): 280-281 
29159:Page(s): 281 
---
```


## [2026-09-04T19:26:04.778Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4470,4580p' POK_full.txt"
}
```


### [2026-09-04T19:26:04.834Z] TOOL RESULT

```
References: WP. I 86 f., WH. I 4, 31 f. 
Page(s): 26-27 

Root / lemma: al-4 
Meaning: "to burn' 

Material: Old Indie alatamu. " fire, blaze, coal ' (also u/mukam'ike'); Latin adoleo^ to 
worship, offer sacrifice, burn a sacrifice; to sacrifice on an altar; in gen., to burn; to smell ', 
adolesco, -ere " flare up (from altars), to grow up, come to maturity, to be heaped up, or 
perhaps to burn ' (ofrom a as in etymological-different adolescere^ to grow up, come to 
maturity, to be heaped up, or perhaps to burn ' to aid, see below *a/-2^ grow'), a/tarel'\re 
altar' (with difficult o ablaut Umbrian uretu^ toward turning to vapor '); 
New Swedish a/a" blaze, flame ' (Johannsson ZfdtPh. 31, 285 following ms. Lithuanian); 
but in question gr. aAaPn av9paK£(; Hes.; view also from Latin a/acer "quick, lively, 
animated', Gothic aljanu. "zeal' etc. was possible as " igneous, quick-tempered ' 
(Johansson aaO.); about Old English selan^ burn ' see *5ic|h-. 

Maybe belongs here gall. MS Alatus, Middle Irish alad^ multicolored, dappled, striped ' 
(if originally 'burnt') = nir. a/ac//? "trout' {alato-). 

Maybe alb. a//e're6 color'. 

References: WP. I 88, WH. I 13, EM. 88. 
Page(s): 28 

Root / lemma: al-5{*hel-) 

Meaning: "to grind' 

Material: Old Indie anu-^ fine, thin, very small ' {*a/-nu-), Hindi and Bengali ata' flour ' 

(below likewise; Kuhn KZ. 30, 355; different Specht Dekl. 125). 

Avestan asa{*arta-) " crushed, ground' (HiJbschmann ZdMG. 38, 428, Spiegel BB. 9, 
178 A. 1). 

Armenian afam " grinds', afaur/{ *alatrio-) " mill ', aleur- " flour ' (in spite of /instead of / 
not borrowed from aAsupov, HiJbschmann Arm. Gr. I 414), aiaxin' servant ', aVf young 
girl ' (Meillet BSL. 37, 72). 



Note: 

The inanimate suffix -ur- : Armenian aiauri{ *alatrio-) " mill ' : UAupioi , oi, lllyrians, UAupia 
, n, lllyria, also'lAAupi^ , n, Adj. 'lAAupiKO? , li, 6v, lllyrian: -kpi, the region or province of 
lllyria, 'lAAupi^O) , speak the lllyrian language, 'IAAupia:-hence Adv. lAAupiaii. 

Gr. ciAe: qAeu) " grinds, crushes ' *, aAsTai AiGoi " millstone, grindstone ', aKz^oo, and 
cxKz^bc, " the milling, the grinding ', aAsTcbv 'mill', aAsTpsuu) "grind', aA£[F]ap, PI. dAEiara 
(stretched from aAsara; Schuize Qunder ep. 225) 'flour' (from it contracted *aAr|Ta called 
out of the new sg. aAr|TOv aAsupov Hes.; aAr|T0-£i5n(; Hippokr., aAnTwv aAsupajv Rhinthon), 
aAeupov (*aA£-Fp-ov) " wheat flour', oXwoc, " flimsy ' ( " pulverized, crushed, ground'), aAi^ 
' miller who grinds the spelt, wheat ' (from it Latin 5//ica 'spelt, or a drink prepared from 
spelt' ds). 



*) Also £Au|JO(; "millet', oAupa "spelt', ouAai, Attic oAai "ground coarse grain' (*oAF-, not 
after J. Schmidt KZ. 32, 382 from *aAF-) would be compatible, perhaps, phonetically (then 
word root would be *el-, *ol-, %/-). 

References: WP. I 89. 
Page(s): 28-29 

Root / lemma: a/p- 

Meaning: "small, weak' 

Material: Old Indie a/pa-, a/paka-smaW, slight, flimsy ' {alpena, alpaV light, fast '); to unite 

heavily in the definition with Lithuanian alpstu, alpau, alpti^ become unconscious ', alpus^ 

weak ', Latvian elpe^ taking air, breath ', alpa' " one time, time, moment in time '. 

apposition also from hom. aAana5v6(; (from Aeschylos Aana5v6(;) 'weak', aAana^w ' 
exhaust, make tired, weaken; drain, empty '. 

Zero grade in (under the influence of lllyrian) Attic Aana^u) ' despoil, pillage', AanaiTU) " 
empty (the body) ' is doubtful because of their to two-syllables root words compared with 
the light ones Old Indie and Lithuanian words; also they suit, as well as to them, added to 
AaTTap6(; " slender, thin, having hollow body ', Aanapa " flank, swell of the body in the hip ', 
KauaQoQ, " cavity, pit ', AanaGoq " sorrel, rumex ' in the meaning colouring ("empty, sunken, 
shrunken '). Quite dubious also alb. (Jokl SBAk. Wien 168, I 48) laps' be tired of, sick of, 
bored with '. 



Maybe in e- grade alb. lepjete' sorrel, rumex ' : gr. AanaGoc;" sorrel, rumex '. 
Maybe Latin lapso -are'to slip, stumble'. 

On account of here Hittite al-pa-an-da- {alpant-) 'ill, weak, small, flimsy'? 
Proto-Altaic: *alpa 

Meaning: unable, sick; being at service, man-at-arms 
Turkic: *alp- 
Mongolian: *alba-n 
Tungus-Manchu: *alba- 
Korean: *arpha- 
Japanese: *apar- 

Comments: Poppe 85, 121 (Turk-Mong.); TMN 2, 110-111. 
Proto-Kartvelian: *valp- 
English meaning: weak 
Georgian: Gur. yalp- 

References: WP. I 92, Couvreur H 106 f., WH. I 786, Hirt Indo Germanic Gr. II, 158. 
Page(s): 33 

Root / lemma: alu-{-d-, -t-)
```


## [2026-09-04T19:26:21.544Z] TOOL CALL #9: Bash

```json
{
 "command": "ls data/verification/ | head -30; echo \"--- tools\"; ls tools/ ; echo \"--- pdf?\"; find . -maxdepth 3 -iname \"*.pdf\" | head"
}
```


### [2026-09-04T19:26:21.608Z] TOOL RESULT

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
process
sources
--- tools
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
--- pdf?
./EtymologicalDictionary-persian-english.pdf
```


## [2026-09-04T19:26:22.826Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK_01 leaf for p.28 (leaf=p+8=36) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==37' POK_01.txt | head -60"
}
```


### [2026-09-04T19:26:26.967Z] TOOL RESULT

```
=== POK_01 leaf for p.28 (leaf=p+8=36) ===
ere  ,heranwachsen^  zu  alö, s.  unter  2.  *al-  , wachsen*^),  altäre  ,Brandaltar^  (mit  schwierigem  o-Ablaut umbr.  uretii  ,ad  adolendum^) ;  nschwed.  ala  ,lodern,  flammen^  (Johannsson ZfdtPh.  31,  285  ff.  m.  Lit.);  aber  zweifelhaft  gr.  dXdßrj'  ävd-Qay.eg  Hes.; Auffassung  auch  von  lat.  alacer^  got.  aljari  n.  ,Eifer'^  usw.  als  , feurig, hitzig^  (Johansson  aaO.)  wäre  möglich;  über  ags.  xlan  ,brennen'^  s.  *aidh-.
Vielleicht  gehört  hierher  gall.  MN  Alatus,  mir.  alad  ,bunt,  scheckig, gestreift^  (wenn  ursprüngl.  ,gebrannt^)  =  nir.  aladh  ,Forelle^  (aläto-).
WP.  I  88,  WH.  I  13,  EM.  88.
5.  ai-  ,mahlen,  zermalmend
Ai.  dhu-  ,fein,  dünn,  sehr  klein'  {^al-niL-),  hiudi  und  bengali  ätä  ,MehF (u.  dgl.;  Kuhn  KZ.  30,  355;  anders  Specht  Dekl.  125).
Av.  asa  (*arta-)  ,gemahlen'  (Hübschmann  ZdMG.  38,  428.  Spiegel  BB. 9,  178  A.  1).
Arm.  alam  ,mahle',  alauri  (*alatno-)  ,Mühle',  aleicr-  ,Mehl'  (trotz  l statt  i  nicht  entlehnt  aus  äXevoov,  Hübschmann  Arm.  Gr.  I  414),  alaxin , Dienerin',  alij  ,junges  Mädchen'  (Meillet  BSL.  37,  72).
29
Gv  die-  :  dXico  ^malile;,  zermalme^ ^);  dlsrai  lld-oi  ^Müblsteine^^  ^XsToq •  und  dl^ög  ;das  Mahlen^,  äXsrcbv  ^Mühle^,  dlergevo)  ^mahle^;,  äXe[J^]aQy  PI. dlEiata  (gedehnt  aus  äUara]  Schulze  Qu.  ep.  225)  ,Mehl^  (daraus  kon- trahiertes '^älfi'ta  rief  den  neuen  sg.  }ilri%ov  ItXevgov  Hes.  hervor;  äXrjTO- siörc  Hippokr.,  äXrjTCJv'  äXsvQcjv  Rhinthon);,  IcXevQOv  (^dXs-J^Q-ov)  ^Weizen- nielil^  dXivög  ^schwach'  (,zerriebenO,  ^Xi^  ;,Speltgraupen^  (daraus  lat. alica  ds.). WF.  I  89.
6,   al-t   alöu-  :  alou-    Farhadjektiv    ^weiß^    glänzend^,    s.   alhlio-    und    Farb- adjektiv el-.
alä  u.  dgl.  ,hallo!^
Ai.  alaläihhavant-)  ^munter  werdend^  (mind.  are,  re  ^du  da!*  vielmehr zu  ari  ,Fvemder^j  Thieme  Der  Fremdling  im  Rigveda  Iff.,  s.  oben  S.  24).
Gr.  dXaXa,  dXaXal  ;,hallO;,  hurraF^,  dXaXrjTÖg,  dXaXrjrvg  ^Schlachtruf^; dXaXdCo)  yStoile  den  Schlachtruf  aus^  (ähnlich  iXeXsv  ^Kriegsruf^  Schmerzens- vai^ j  iXeXi^d)  ^stoße  den  Krieg'sruf  aus^);  lit.  aluoti  ^hallo  schreien'^  (Entleh- nung aus  dem  Deutschen  nicht  nachweisbar)  neben  aliöti  ^durch  Geschrei aufscheuchen^;  aksl.  ole,  bulg.  olele  Interjektion;  z.  B.  Fick  P  356  (nhd. hallo,  holla  sind  dagegen  aus  dem  Imperativ  von  ahd.  halön,  holö
```


## [2026-09-04T19:26:32.269Z] TOOL CALL #11: Bash

```json
{
 "command": "(pdftotext -f 46 -l 46 -layout EtymologicalDictionary-persian-english.pdf - 2>/dev/null | head -60) || echo \"pdftotext missing\""
}
```


## [2026-09-04T19:26:33.679Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN p.5 (leaf=printed+21 => leaf 26) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==27' HRN.txt | head -50"
}
```


### [2026-09-04T19:26:33.949Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-04T19:26:35.572Z] TOOL RESULT

```
=== HRN p.5 (leaf=printed+21 => leaf 26) ===
5 -
gesetzlich unmögliche Etymologie Spiegel' s (Keil-
inschriften 2, 238, Ar. Periode 284) findet sich noch bei
Bechtel, Hauptprobleme, 163.
12. äräm *Ruhe*, ärarmden, arätnis, nu^'0'nN (jüd.-pers.
Bibelübs. ^).
aw. äramayat *er erfreute'; phlv. aramUan, äräni
*Ruhe'.
af/. bei. (18) LW. äräm,
Vergl. räm (No. 604).
\^. ärd 'Mehl'.
\ Käs. ort, ürt, vergl. auch s. v. äsyäh : ör, ä/-, ir,
aw. asa- gemahlen', anasa- (Hübschniann ZDMG.
38, 428); phlv. ärd ^Mehl'.
kurd. är, ärd (Jaba-Justi), ärf, irt (Houtum-
Schindler); af/. öra; bei. ärt n. arf (15); arm. aZ^wr
*Mehr, ahxm 'mahlen* (unsicher, H. No. 7).
14. uren *Elle', äreng^ ärenj,
phlv. äranj (PPGL).
oss. arm-arün *Elle'; sar. yovn 'Ellbogen*; gr. wXsvfj;
lat. ulna.
Vergl. aw. radni- in frara&nidrajö^); phlv. eratn (?);
ai. aratni' 'Elle'.
Die neupersischen Worte werden richtiger mit ä
(bezw. e) zu schreiben sein.
15. äroy (AM. S. 95 Zeile 2), üröq *das Rülpsen , äröytden,
röy,
gr. BQsvyo/Liai 'rülpsen*; lat. ructäre^ ructus 'das
Rülpsen*; lit, raugmi, rugiü 'rülpsen'; ksl. rygayq;
ags. rocetan (Hörn).
Zu arm. orc 'Speichel, Erbrochenes*, orcam erbrechen,
rülpsen* vergl. H. No. 233 und Bartholomae, Studien
n, 134.
16. äri 'fürwahr.
Käs. ore, dre^ drl.
^) Die Endung -ist ist bekanntlich im Afghanischen in der Form
'ist und -ast nicht selten.
*) Bartholomae BB. 17, 111 Anmerkung.
```


## [2026-09-04T19:26:43.421Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i in range(235,252):\n    p=pages[i]\n    # print first 200 chars\n    print('--- leaf',i, repr(p[:160]))\nEOF"
}
```


### [2026-09-04T19:26:46.257Z] TOOL RESULT

```
777
--- leaf 235 'آذرشپ - و "\nمرکق ۳ ۳\n] در شین « بکر شین وسکون نحتانی\nو نون . سمندر را گوند وآن جانورست که در\nآش متکون کردد ۴\n] دار طو س ه نم طای\u200cحطی کون\nواو وسین بی\u200cنقطه بمعنی '
--- leaf 236 'آخر کون نت\nآ داد کش ها یکی کنق. و کون\nبحتانی مجپول و شین قسرشت » آتش پرست را\nکونند ؟ . #\nآذر ۵ ه بفتح رابعم و سکون - میم ,\nزین اسبی را کویندکه نمدزین آن دونیم ب'
--- leaf 237 '7 در هما بون - بن\u200cها . بابساحرهای\nبوده از نسل سام و. خدمت آتشکده صفاهان\nمیکرد وذوالقرنین اورا به بلینای\u200cحکیم دادوبدین\nپیب بلینای را جادوکر میگفتند ۱ .\nاست که بم'
--- leaf 238 'آرا\nآداه بروزن خارا . آرایش. وآرایش\nکننده و آراینده را کویند همچو خن آرا\nو بزمآرا وامی باینمعتی هم هت ممنیآرایم\nکن و بارا .\n9\nو پنجم است از هرماه شمی - و ام فرش'
--- leaf 239 'ت برایو بی اه آرامی\nرة حواشی صفحة .۳\n۵ آرامی_نام قومی از فبایل بدوی سامی ناد سوربه که درجنوب فلسطین در پبرامون\nکوبر ومشرق رود اردن وبحرالمیت میزیستند. اين شبانا'
--- leaf 240 'آرامی - پرایی ۷۲٩\u200f س\nآرامی بکاربردند. بدبنوجه زبان آرام یکه اززبانهای سامی\u200cاست وآموختنش برای\u200cهزدم مأی زبان\nدشوار یست باخط آرامی که الفبابی.ساده بود سراسر کشورها'
--- leaf 241 'مخفف آوداس تکه نام روز بیست و پنجم از هر\nماه شمی باشد ۱- و ممکون ثالث معروف است\nکه له آسیا کرده باشد ۴ - و بمعنی تقصیر هم\nات\nآ رث و له - (۱) بش فوفانی و سکون\nوا'
--- leaf 242 ']دی ح بکر الث و رايع و سکون\nتحتانی ۰ بمعنی ممنوی باشد که در مقابل لفظی\nاست ۰ چه آرش بمعنی «معنی» است ٩\u200f .\nآدع بضم نالث و سکون غین نفطه\nدار , مخفف آروغ است . و آ'
--- leaf 243 'دوع ۰ با غن نقطه دار سس وزن\nفاروق , بادی را گویند که از کلو باسدا برآید ؛\nو بجای غن , فاف نیز گفته آند و عوق فافه\nکردهاند .\nآدون- بر وزن قارون » صفتهای\nخوب و ني'
--- leaf 244 'در دل کسی\u200cجای کند ؛ وباین معلی بازای نفطه\u200cدار\nهم آمده است .\n11 ۱ مه بسکون زای نقطه داره یمعنی\nآرزو و خواهش با ابرام و حرص باشد در جمیع\nامور - ونام جابی ومقامی و'
--- leaf 245 'سب چ ح\nآزا۵ذارو- با دال ابجد بالف کشیده\nو رای فرشت عضوم بواو زده » نوعي از چفندر\nصحرابی است ریخ آنرا «حلیموه کوبند . ضماد\nآن قری و مفاصل را نافع است .\nآراد درخت'
--- leaf 246 'آزدن\nرذن . بازای فارسی » بروزن و معنی\nآزدن بلشد که خلانیدن سوزن وامشالآنست .-\nو استره زنب واژنه وگ اشفا زدن نزدمك\nسکدیگر را کوبند .\n]رده بروزن آمدم .یمعئی رنگهک'
--- leaf 247 'ده\nآ زر نگ - بفتح رأیم بوزن با درنگه .\nبمعلی غم سخت و محنت صعب و رنج و هلا کت\nباشد - وبمعنی خیارسبز هم پنظ آمده است ٩\u200f .\nگت یتح الت وسکون خی تقطمدار»\nدرختان دیگ'
--- leaf 248 'رود 5 با زای هوژ بر وزن ساطور »\nصاحب حرص و آز را کونند که حریص باشد .\nاین لفظ م رکب است حمجو گندور و رنجور -\nو بممنی هوسناله هم گفته\u200cاند ؛ و بر وزن داد کر\nآمده\u200c'
--- leaf 249 '۳ آسا\nآن را « حب الآس » خوانند ۴. کونند عمای\nموسی علیه السلام از چوب آس بوده » ودر مك\nروم درخت آن از جاهای دمگر بزرکتر مشود »\nوشکوفةً آن خوشبوی میباشد » هرک سکه'
--- leaf 250 'آسیابان باشد چه آسیا راآس میگویند .\nآس بری « بکس تالث و فتح بای\nابجد و کسر رای قرشت با عشدید بتحتانی زده .\nمورد صحرابی است و هترین آن رومی\u200cمباشد »\nطبیمت آن کرم '
--- leaf 251 'بمعثی بطانه است - و کنابه\nباشد.\nاسقی » بر وزن راستی » بمعنی آستن\nاست که مخفف آستن (۱) باشد.\n] سقیم » با میم» بروزن و معنی آستین\nاست - و خونی باشد که از جراحت (۲'
```


## [2026-09-04T19:26:51.858Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (240,241,242):\n    print('========== leaf',i)\n    print(pages[i])\nEOF"
}
```


### [2026-09-04T19:26:53.689Z] TOOL RESULT

```
========== leaf 240
آرامی - پرایی ۷۲٩‏ س
آرامی بکاربردند. بدبنوجه زبان آرام یکه اززبانهای سامی‌است وآموختنش برای‌هزدم مأی زبان
دشوار یست باخط آرامی که الفبابی.ساده بود سراسر کشورهای اقولم سامی نژاد را فرا کرفته از
بلحرالروم نایشتکوه (زاگری) وخلیج قاری زبان. بین‌المللی محصسوب حیشد.
هنگامیکه ابرانبان بسرزمین‌های آشور وبابل وآسبای صفیر وسوربه وعصر دست بافتند
باافوامی سروکار پیدا کردند که زبان وخط وسیلهٌ ارتباط دبوان های دولتی هشامثشیان و متصرفات
غربی ابران‌شد. درتوراة , کتاب عزرا باب4 بند۷ آمده: #در روز کار اردشیر اول(هخامنشی) بشلام
21520 ر مهرداد وئبیل [۲20 وباران دیگر آنان مخط آرامی و با ترجمةٌ آرامی نامه‌ای
باردشیر یادشاه ابران نوشتند. »
ازفرائن پیداست که خط میخی برای‌حوائج روزانه بکاردمیرفت" واین‌خط برای کنده کری
اختصاص داشت " اماالفبایآرامی با ۲۴ حرف برای کتابت آسانتر بود . خط سکه‌های محلی دور
حضامنشی و وزنه‌هابی که رویآ نبا خط آرامی نوشنه‌شده وخط بیاری ازمهرهای ابرانبان که ,خطا
آرام یکنده کری‌شده » بخوبی دواج این خطرا درایران میررساند .
کتیبه‌ای «رجيهةٌ آرامگاه داربوش ازنفش رستم بزبان پارسی باستان وبخط آرامی موجود
است وآن‌بنام اردشیر اولاست. یس‌از انقراض سلسلهٌ هخامنشی خطآرامی که در آن‌روز کار هممجا
رخنه بافبه‌بود همچنان راء خودرا پیمود تابجابی رید که چندی پس‌از آن بنام خط پهلوی‌خوانده
شده است. ۱
آار عمدث آرامی- دوبخش ازتوراة بزبانآرامی است: بخشی از کتاب دانیال که درژمان
ااقیوخس‌اییفانوی ۳۵/0205 ۸۱۷۵11:05 (۱۷۵-۱۹ ق.م. ) توشته‌شده وبداتیال تسبت
داده‌شده» دیگر بخثیا ز کتاب عزرا که درحدود فرن سوم ق.م. نوشته شدم همچنین تر گوم
0 (ترجوم - ترجمه) نضبری که بتوراة نوشته‌شده واز فرن‌دوم ق.م. آغا زگردیده است؛
بزمان آرامی است - نیز نلمود (آموزش) بدین زبان است که بخشی از آن‌دا در آغاز قرن چهارم
مبلادی درقلمطین کرد آورده‌اند وبلهجهٌ آرامی غربی است وبخش دبگر درحدود سالهای ۳۹۷ -
4۷ دریابل کردآ وری‌شده وتاقرن پنجم مطالبی‌بدان افزوده‌اند وآن تلمود بابلی نام‌دارد وبزبان
آواعی شرقی است.. «فان ٩ص‏ ۱۵۶ - ۰۱۱ ۶« کتبه‌های پهلوی. هننگ . ترحمهة تگارنده
س ٩۱۵-۰۱۱‏ .
========== leaf 241
مخفف آوداس تکه نام روز بیست و پنجم از هر
ماه شمی باشد ۱- و ممکون ثالث معروف است
که له آسیا کرده باشد ۴ - و بمعنی تقصیر هم
ات
آ رث و له - (۱) بش فوفانی و سکون
واو و فتح لام ء آشی باشد مانندکاچ یکه از آرد
پزند و بیشتی مردم درویش و ففبر خورند وآنرا
جریی «سخینه » گویند .
ومشی آرد توله اس ت که آش کاچی مانند باشد .
]ددم - بنتح رابم و سکون عیم ۰
نام کل آذربون است که نوعی از شقایق وکل
همیشه بهار باشد .
] ذن - بفتح رابم و سکون نون »
,کفگیر سوراخپا دارد وبدلن چیزها صافیکنند.
وکفگیی را نی زکوبند - و نم ولاشی هم
ضت . ؟ *#
]رذهاله - بیای (») بالف کشیده
و فتح لام » بمعنی آرد توله است که آش کاچی
ماتثف باشنه.
آرش
]رده جتح زای حوز , کاحگل را
کوبند . و آن خاکی است که با کاه آمیزند
وگل سازئد و بر دبواز وبام خانه مالند .
آرژه گر - بفتحم کاف فارسی
و سکون رای فرشت . شنصی را کون که کاه
کل عاو...
| دست ع بروزن وارست. بمعنی‌توانت
باشد که ماضی تواشتن است - و مضفف آراست
هم هست که از آراستن باشد . ۴
۲ دسته - مسر وزن وارسته مخفف
آراسته باشف .
دش ٩‏ - بنتح ثاك و سکون شین
شطه دار ۰ نام پهلوانی بوده ابرانی از لشکی
منوچهر و در صنصت تبراندازی عدیل و نظیر
نداشته چنانچه تیری از آمل بمرو انداخته که
قربب بچهل روزه (۳ ) راء است ۰ وکونند آن
تبر مجوف بودماست وآنرا از شبنم پ رکرده‌بود »
و بوفت طلوع آفتاب بجاب مشرق اداخت *-
و نام پسردوم کیقباد هم است که او را «کی‌آرش»
گفتندی ۷ - و یکس ثالث ۸ - بععنی «معنی*
"4
۹ بونکر ۱۱۲ *.
؟ - پپلوی )27 « تاوادبا
۴ - ول : آرستن ۵ اوستا
۱ - از آن خوانند آرش را کمانگیر
که از آمل بمرو انداخت يك نی
و ۱۶۲
شتین چوکاوس با آفرین
2 مزدسنا ۷ ۰
مراد - معشوق » موب :
========== leaf 242
]دی ح بکر الث و رايع و سکون
تحتانی ۰ بمعنی ممنوی باشد که در مقابل لفظی
است ۰ چه آرش بمعنی «معنی» است ٩‏ .
آدع بضم نالث و سکون غین نفطه
دار , مخفف آروغ است . و آن بادی باشد که
با صدا ا زکلو برهیآ مد ۰
]رغاده (۱) - بر وزن مارساده + نام
رودخانه ات .
]دغده ؟- بن الك ( ۲ ) بر وزن
آزرده. بمعنی نخبناك (۳)وخشمگین وقهر آ لود -
و جنگاور باشد - و بفتخ الث حريصي در چپزها
را گویند .
۲۰ ریش «- بنتح اول و ثانی ۰ بر وزت
صم کیش ۷. بوست. بیرخت زرهاباخد وآنرا
دو دازو ها چشم نیزبکار برند .
۱ آآرمان ۴ بر وزن آسمان ۰ بمعنی
جح تب و آرزو - و رنج بردن باشد - و پشیمانی
و آفوی را نیز گویند . *
آمده - بکر میم ۵ . مخفف
وسکون میم بروزن دارنده. بمعنی دریغ‌وافوی
و پشیمانی باشد .
] دهش » بکس میم . مخنف آرامش
)۱ خم ۳ آارغاوه ۰
)4( خم ۳ 0 رنگ دادن.
و
است که ساکن شدن و آساش ‏ فراغت وراحت
کردن باشد .
آدهون - بر وزن ولژگون » زری
را گوند که پیش از کارکردن بکارگر و هزدور
دهند . و معربی «عربون» خواند . 4
| رهیفه » بر وزن نا رسیده . قرار
] دن ه بر وزن فارن . مخفف آرنج
است که بند گاه ساعدوبازو باشد. وبعربی«مرفق»
خوانند ۷ ,
اد نج - بر ون نارنج . بندکگاه
ساعد و بازوست که عرب « مرفق » گوید ۷ - و
بمعنی بازو هم بنظر آعده است که ازمرفق باشد
تا دوش .
]را نگ - باکاف فارسی. بروزن وهعنی
آرنج‌است که مرفی‌داشد - ور نگ ولون (4)را
یز کنته اند - و بمعنی حمانا و پنداری وگمان
بری حم‌آعده است - وونج ومجنت‌را عم گویشدب
و بمعئی مکر و حیله و فررت تیز حستتویمعنی
کونه وروش و طرز حم گفته‌اند چنانکه گویند :
«بدین آرنگ» یعنی بدین (۵) رز و باین دوش
و بدین گونه - و نام میوه‌ای هم مت - وحاکم
ملك را فیز گوشد ِب#
۲۱ ) خم ۳ : غشان.
۳ ت‌ اارغیش
آرمده سکون هیم -
6۵ در اشمار
ه آرمیدن _ ره : آرامدن ۰
براندیشه شد تا چهآ ید بدند
> مزدسنا ۷۹ ۱۹۸ و هی‎ ٩
( قاطع برهان 4 )
```


## [2026-09-04T19:27:14.641Z] TOOL CALL #15: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-04T19:27:14.688Z] TOOL RESULT

```
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
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
```


## [2026-09-04T19:27:21.317Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o bqt241.jpg \"https://archive.org/download/borhan-ghate-v1/page/n241.jpg\" -w \"%{http_code} %{content_type} %{size_download}\\n\""
}
```


### [2026-09-04T19:27:24.740Z] TOOL RESULT

```
200 image/jpeg 515837
```


## [2026-09-04T19:27:27.028Z] TOOL CALL #17: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt241.jpg"
}
```


### [2026-09-04T19:27:27.688Z] TOOL RESULT

```

```


## [2026-09-04T19:27:27.686Z] INPUT

[Image: original 2479x3508, displayed at 1413x2000. Multiply coordinates by 1.75 to map to original image.]


## [2026-09-04T19:28:02.560Z] TOOL CALL #18: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/31.vision.txt <<'EOF'\n[BQT vol.1, printed p. 31 (archive.org borhan-ghate-v1 leaf n241), read from the page image\nby claude-fable-5-1 on 2026-09-04. Running head: آرش   - ۳۱ -]\n\nRight column, top (continuation of the entry آرد, whose headword is at the foot of p. 30):\n«... مخفف آورداد است که نام روز بیست و پنجم از هر ماه شمسی باشد ۱ ــ و بسکون ثالث معروف است\nکه غلهٔ آسیا کرده باشد ۲ ــ و بمعنی تقصیر هم آمده است .»\n\nآردتوله ــ (۱) بضم فوقانی و سکون واو و فتح لام ، آشی باشد مانند کاچی که از آرد پزند و بیشتر\nمردم درویش و فقیر خورند و آنرا بعربی «سخینه» گویند .\nآرددوله ــ با دال ابجد ، بر وزن و معنی آرد توله است که آش کاچی مانند باشد .\nآردم ــ بفتح رابع و سکون میم ، نام گل آذریون است که نوعی از شقایق و گل همیشه بهار باشد .\nآردن ــ بفتح رابع و سکون نون ، ترشی بالا را گویند و آن ظرفی است که مانند کفگیر سوراخها دارد\nو بدان چیزها صاف کنند و کفگیر را نیز گویند ــ و نام ولایتی هم هست .\nآردهاله ــ بهای (۲) بالف کشیده و فتح لام ، بمعنی آرد توله است که آش کاچی مانند باشد.\n\nFootnotes (Mo'in's etymological notes) at the foot of the page:\n۱ ــ صحیح «ارد» بفتح اول است . رك : ارد .\n۲ ــ پهلوی ârt «تاوادیا ۱۵۹ ، بونکر ۱۱۲» .\n۳ ــ و مخفف آوردن .\n۴ ــ رك : آرستن .\n۵ ــ اوستا ərəxsha (درخشنده) «یوستی ۸۹» . وجه اشتقاق آن نامعلوم است «بارتولمه ۳۴۹» .\n[…]\n۵ آرزو ــ پهلوی ârzôk «نیبرگ ۲۸۱» یا ârzûk «اونوالا ۲۹۵»؛ کام، خواهش، مراد ــ معشوق، محبوب .\n۵ آرستن ــ توانستن، یارستن، جرأت، دلیری کردن .\n۵ آرشام ــ Arshâm نام جد داریوش بزرگ شاهنشاه هخامنشی، مرکب از arsha بمعنی خرس و ama\nبمعنی زور، جمعاً خرس نیرو، دارای زور خرس. «بارتولمه ۲۰۴».\n\n[Key point for verification: Mo'in's only etymological note on آرد \"flour\" is «پهلوی ârt»\n(Pahlavi ārt), citing Tavadia p.159 and Bunker p.112. No Avestan or Indo-European form is\ngiven on this page for آرد.]\nEOF\necho written"
}
```


## [2026-09-04T19:28:03.201Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD grep rtk/flour ===\"; grep -n \"flour\" SOD.txt | head -20; echo \"--- entry 59 area\"; grep -n \"^ *59 \\|^59 \" SOD.txt | head"
}
```


### [2026-09-04T19:28:15.318Z] TOOL RESULT

```
written
```


### [2026-09-04T19:28:15.381Z] TOOL RESULT

```
=== SOD grep rtk/flour ===
14058:fertile,  flourishing 
17355:flour 
17479:flour 
17537:flour 
89660:flour     1479,  1498,  1508 
89661:flourishing    992 
--- entry 59 area
7994:59  »8yh    M  =»  »dy,  »8>kw 
17427:59
```


## [2026-09-04T19:28:17.735Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17340,17370p' SOD.txt; echo \"=======\"; sed -n '17470,17545p' SOD.txt"
}
```


### [2026-09-04T19:28:17.815Z] TOOL RESULT

```
STi  33.18;  GMS  1056 

1477  >rsx    C  =*  'rs'ny 

1478  >rt1   M  3 
art  Ortms)  ©in  compd.  conj.  with  pron.  &  art. 

=^ty,  V,  >rty\  rty 
and 
S  W,  BSOAS  1975,  133,  1985,  111;  C2,  9.183 

1479  >rt2  C  ,J 
art   ©ob.  >rty  ?   =^rtk 


flour 

C2,  94  V  21 

1480  >rtJ  =*  »srwc(yy) 

1481  Yt'kCw)  =>  >rtk 

1482  'rt't  rwc   M,  S        (W^j^jj^'^"^^  Jjj 
artat  roc   ©<haruvatdt 

sixth  day  of  the  month 

GMS  86  n  1;  Hen.  Oricntalia.  8,  94;  Magi.  149.10; 
MDiii 

=======

artxwost,  artxust    ©*artwahist   ^Wwxwst  rwc 
Ordibehesht,  third  day  of  the  month 
MDiii  p60;  GMS  392;  Hen.  BSOAS  1965,  251, 
n  58 

1498  >rtk    S  ,/ 
arte   (WkCw))   ©Av.  as  a   =*}rt2,  Jrty3 

flour 

MDii,  >rtkw;  MDiii  p30,  }rtw 

1499  Vtms  =>  ms,  't1,  rtyms 

1500  >rtt  rwc   S  (^-V-W^r*  jJjOjjj^ 
art-roc,  as-roc   =»*rt  rwc,  *s  rwc(yy) 

ninth  day  of  the  month 
MDiii 

1501  Vtw   C  •*i/<j*>«k,l 
artaw   ^rt'w 

faithful 

C2,  54R19,  ob.  V/'hV>\  39V6 

1502  Ytwsp'y    B  =>  'rt'wsp^ 

1503  Ytwspy*    M  =»  >rt,wspy,h 


1504  »rtwy'   C  \ys  ^»r 
arawya   ^rt'wy'Oi) 

righteousness 
C2,40V21 

1505  Ytxwst   M  (,js^  ^l^<f*^  _s<^)jyi^JL4ri>J 
artxwost,  artxust   Ortxwwst)  ©*rta  vahista-, 

>*artavahist>*artxw9st   ^rtywst  rwc, 

Wwxwst  rwc 
Light(//ie  third  element,  a  Manichean  god), 

light 
GMS  392,  422;  Gersh.  Sogd.  Cpds.  410;  Sogdica. 

27.19;  BBB 

1506  Ytxwwst  =*>  'rtxwst 

1507  Vty1   M,  C         -VrrO"  j->)(uy  >^  jJ)u~r,*ij-i<j 

orti    Orlyy,  }rtyh)   ©Knot,  rro   ©in  compd.  with 
pron.   ^>ty,  »PZY,  rty,  TRZY,  }rt\  Bty(y) 

and,  then 

GMS  3,  307A;  BBB;  KG;  MSP;  S  W,  BSOAS 
1983,  41  n  2,  46;  C2,  183,  >rtyswfsy,  >rtysn 

1508  Yty2  C  ^7 
arte  ?  ^n\  >rtk 

flour 

BSTii  827.51;  Bcnv.  Etii  119;  C2,  94V21  pl77 

1509  Ytyp>n   S  oi^jf 
artcwan    ^'rSp'n 

Ardavan 
Anc.  Lett.  3.13
```


## [2026-09-04T19:28:26.268Z] TOOL CALL #21: Bash

```json
{
 "command": "which pdftoppm pdftotext mutool gs python3; python3 -c \"import fitz; print('pymupdf ok')\" 2>&1 | tail -1"
}
```


## [2026-09-04T19:28:27.422Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '1498' in p and 'rtk' in p:\n        print('leaf',i,'printed approx',i-66)\n        print(p[:400])\n        break\nEOF"
}
```


### [2026-09-04T19:28:28.028Z] TOOL RESULT

```
/usr/bin/pdftoppm
/usr/bin/pdftotext
/usr/bin/mutool
/usr/bin/gs
/usr/bin/python3
ModuleNotFoundError: No module named 'fitz'
```


### [2026-09-04T19:28:29.528Z] TOOL RESULT

```
leaf 124 printed approx 58
                                                                                                                   >rw>st>k
 59

                                                                1504 »rtwy'     C                                \ys ^»r
                                            (j^U Ji-u? i^sjX*
       artawya   ^rtwy*                                               arawya     ^rt'wy'
```


## [2026-09-04T19:28:35.292Z] TOOL CALL #23: Bash

```json
{
 "command": "pdftoppm -f 46 -l 46 -r 150 -png EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p46 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p46*"
}
```


### [2026-09-04T19:28:37.080Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 19371 Sep  4 15:28 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p46-046.png
```


## [2026-09-04T19:28:39.344Z] TOOL CALL #24: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p46-046.png"
}
```


### [2026-09-04T19:28:39.367Z] TOOL RESULT

```

```


## [2026-09-04T19:28:50.564Z] TOOL CALL #25: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-04T19:28:50.627Z] TOOL RESULT

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


## [2026-09-04T19:28:55.954Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT asa- ===\"; grep -n \"gemahlen\\|zermahlen\" BRT.txt | head -20"
}
```


### [2026-09-04T19:28:56.004Z] TOOL RESULT

```
=== BRT asa- ===
4374:•  j.  an-aäa-  Adj.  'nicht  gemahlen',  vom Getreide:  aiiaval  asanqm  {yavattqtn)  asta- vat  'ianam  V.  7.35,
6148:•  j.  ^aäa-  Adj.  'gemahlen,  vom  Getreide': gamca  .  .  yaomca  "um  anlfjam  ma'iuea anspgm  V.J. 51;  —  aäavat  'iänam  (yava- nqm)  aitavat  anasanqm  V.  7.35.
6938:Ar.  *rmj-ila-  (IF.  g.  261),  PPfP.  einer  Basis  anf (aj.)  I  i  [ih)  oder  i  'I.  VIL  zu  lett.  smaüs, Vit,  smiflkiis  'fein'  {luSji-  O'l-  —  Pü.;  a^^«- ür/  'nicht  zermahlen'.  —  ■)  Also  nicht  lu Ut  mfrdeö'.  —  >)  S.  noch  PesssoN  Wunclerw. II,  66.
21631:Man  erwartete  *yavärina;  all  Komp.  au«  yma- +*ar3iia-  n.,  eig.  Instrament  zum  Mahlen des  Getreides';  ■.  zn1izJa-undGIrFh./.3ti[. — np. yävar, yär.  — Pfi. :  iur/öt  1  ör/'gemahlenei Getreide'i    erLi    äiyäi  i  fa  datt  '«ine  Hand*
```


## [2026-09-04T19:28:57.739Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN aleurone ===\"; grep -n -i \"^aleurone\\|aleuron\" KLN_1966.txt | head; echo \"=== KLN aleurone 1971 ===\"; grep -n -i \"aleurone\" KLN_1971.txt | head; echo \"=== AHD al- grind ===\"; grep -n -i \"aleuron\\|^al-\\|to grind\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-04T19:28:57.829Z] TOOL RESULT

```
=== KLN aleurone ===
2157:aleurone,  also  aleuron,  n.,  a  proteid  substance found  in  cereals  ( biochem .)  —  Gk.  SXeupov, ‘wheat  flour’,  fr.  aXsiv,  ‘to  grind’,  which  is cogn.  with  Arm.  alam,  ‘I  grind,  pulverize’,  aleur, ‘flour’,  and  prob.  also  with  OI.  anuh  (for  *al- nuh),  ‘thin,  fine’.  Cp.  prec.  word  and  the  first element  in  Aleyrodes.
2168:Aleyrodes,  n.,  a  genus  of  insects  (entomol.)  — ModL.,  fr.  Gk.  iXEupGSi;?,  ‘resembling  tour’, compounded  of  oiXcupov,  ‘wheat  flour,  and -ei.SY)<;,  ‘like’.  See  aleuron  and  -ode,  ‘like’, alezan,  n.,  a  sorrel  horse.  —  Sp.  alazcin  (whence F.  alezan),  ‘sorrel-colored  (horse)’,  fr.  Arab,  al- fiisdn,  ‘the  noble  and  beautiful  horse’, alfa,  n.,  the  esparto  grass.  —  Arab,  halfd’,  rel. to  Mishnaic  Heb.  heleph,  Aram.  hiPphd,  ‘rush, reed’,  from  stem  h-l-p,  ‘to  be  sharp,  cut  through, pierce’.  Cp.  acalephe.
=== KLN aleurone 1971 ===
10868:aleurone, also aleuron, n., a proteid substance 
=== AHD al- grind ===
278:al-'
280:al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
528:in Greek khriein, to anoint: CHRISM, CHRIST, CHRISTEN, (CHRISTIAN); (CHRISTMAS). [Pok. ghréi- 457.] ghreib-. To grip. 1. Germanic *grip- in Old English gripe, grasp, and gripa, handful: crip!. 2. Germanic *gripan in: a. Old English gripan, to grasp: GRIPE; b. Old French gripper, to seize: GRIPPE. 3. Suffixed o-grade form *ghroib-eyo- in Germanic *graipjan in Old English grd- pian, to feel for, grope: GROPE. [Pok. ghreib- 457.] ghrem-. Angry. 1. Germanic *grimmaz in: a. Old English grim(m), fierce, severe: GRIM; b. Old French grimace, a grimace: GRIMACE. 2. Germanic *grum- in Middle Dutch grommen, to mutter angrily, probably akin to Middle English grummen, to grumble: GRUMBLE. 3. Suffixed o-grade form *ghrom-o- in Russian grom, thunder: Po- crom. [Pok. 2. ghrem- 458.] ghrendh-. To grind. 1. Germanic “grindan in Old Eng- lish grindan, to grind: GRIND. 2. Germanic *grinst-, a grinding, in Old English grist, the action of grinding: GRisT. 3. Latin frénum (< frendere, to grind), horse’s bit (on which its teeth grind), bridle: FRENULUM, FRENUM; REFRAIN). 4, Variant form *ghrend- is sometimes but improbably regarded as the root of Greek khondros, granule, groats, hence cartilage: CHONDRO-; HYPOCHON- DRIA, MITOCHONDRION. [Pok. ghren- 459.] ghréu-. To rub, grind. Extension of gher-4. 1. Germanic *greut- in Old English gréot, sand, gravel: GRIT. 2. Ger- manic *grut- in Old English grotan, pieces of hulled grain, groats: GROATS. 3. Germanic “grit- in: a. Old English griit, coarse meal: GRouT; b. Old French gruel, porridge: GRUEL. 4, Germanic *grautaz, coarse, thick (< “coarsely ground”), in: a. Old English gréat, coarse, thick, bulky, large: GREAT; b. Middle Dutch groot, thick: Groat. 5. Germanic *griiw-, to recoil from (< “to be offended, be grated on by”), in Middle Dutch griiwen, to abhor, akin to Middle English grue, horrible: GRUESOME. 6. Variant form *ghrow- in Greek khrés, skin (< “rough surface” ?), hence flesh, complexion, color: RHODOCHRO- SITE. 7. Suffixed variant form *ghré-mn in Greek khréma, skin, complexion, color (semantic development as in 6. above): CHROMA, CHROMATIC, CHROMATO-, CHROME, -CHROME, (CHROMIUM), CHROMO-; ACHRO- Matic. 8. Probably Celtic *graw- in Old French grave, greve, coarse sand, gravel: GRAVEL. 9. Probably Latin *grau-, to touch, graze, in con-gruere, to agree (com-, together; see kom): CONGRUENT. [Pok. 2. ghréu- 460.] ghwer-. Wild beast. 1. Suffixed form *ghwer-o- in Latin ferus, wild: FERAL, FIERCE. 2. Compound *ghwero-okv-, “of wild aspect” (*-ak-, “-looking”; see okw-), in Latin feréx (stem feréc-), fierce: FEROCIOUS. 3. Length- ened-grade form *ghwér- in Greek thér, wild beast: TREACLE; THEROPOD. [Pok. ghuér- 493.] gladh-. Smooth. Suffixed form “gladh-ro- in Latin gla- ber, smooth, bald: GABRO, (GLABELLA), GLABROUS. gleubh-. To cut, cleave. 1. Germanic *k/euban in Old English cléofan, to split, cleave: CLEAVE!. 2. Germanic *klub-, a splitting, in: a. Old English clufu, clove (of garlic): CLOVE*; b. Middle Dutch clove, a cleft: KLOOF. 3. Germanic *k/aubri- in: a. Old Norse kleyfr, easy to split, perhaps akin to Middle English cliver, “expert in seizing,” skillful: CLEVER; b. Old Norse lofi, a cleft, akin to English clevi, “cleft instrument,” clevis: CLEVIS. 4. Zero-grade form *glubh- in Greek gluphein, to carve: GLYPH, GLYPTIC; ANAGLYPH, HIEROGLYPHIC. 5. Suffixed zero-grade form *glubh-md- in Latin glima, husk of grain: GLUME. [Pok. gleubh- 401.] glégh-. Thorn, point. 1. Suffixed form *glégh-i- in Greek glokhis, barb of an arrow: GLOCHIDIUM. 2. Suffixed form *glégh-ya in Greek gléssa, glétta, tongue, hence also language: GLOSS2, (GLOSSARY), GLOTTIS; BUGLOSS, GLOS- SOLALIA, ISOGLOSS, POLYGLOT, PROGLOTTID. [Pok. glégh- 402.] gno-. To know. Contracted from *gnoo-. 1. Variant form *gné- in Germanic *kné(w)- in Old English cndwan, to know: KNOW. 2. Zero-grade form *gno- in: a. Germanic
738:ing (such as millstones). 1. O-grade form *mol- in Ger- manic *mal- in: a. obsolete Dutch malen, to whirl: MAELSTROM; b. Germanic suffixed form *mal-mén- in Old English mealm-, perhaps “crumbling, friable” (only in compounds, as mealmstdn, sandstone): MALM. 2. Full-grade form *mel- in Germanic suffixed form *mel-wa- in Old English melu, flour, meal: MEAL}. 3. Zero-grade form *mJ- in Germanic *mul- in: a. suffixed form *mul-dé in (i) Old English molde, soil: MOLD? (ii) Old Norse *muldhra, to crumble, akin to the probable Scan- dinavian source of MOLDER; b. Middle Dutch mul, dust: MULL2, 4. Full-grade form *mel- in: a. Latin molere, to grind (grain), and its derivative mola, a millstone, mill, coarse meal customarily sprinkled on sacrificial animals: MILL!, MOLAR2, MOLE‘, (MOULIN); IMMOLATE, ORMOLU; b. suffixed form *mel-iyo- in Latin milium, millet: MEAL- IE, MILIUM, MILLET. 5. Suffixed variant form *mal-ni- in Latin malleus, hammer, mallet: MALLEABLE, (MALLET), MALLEUS, MAUL; PALL-MALL. 6. Zero-grade form *mlJ- in Greek mulé, mulos, millstone, mill: AMYLUM, MYLONITE. 7. Possibly extended form “mili- in: a. possibly Greek bliton, blite (a plant that in some varieties has dusty leaves): BLITE; b. Russian blin, pancake: BLINI, BLINTZ. [Pok. 1. mel- 716.]
749:men-2. To project. 1. Suffixed zero-grade form *mn-to- in a western Indo-European word for a projecting body part, variously “chin, jaw, mouth,” in Germanic *mun- thaz in Old English mith mouth: mouTu. 2. Latin mi- nae, projecting points, threats (> mindri, to threaten): MENACE, MINACIOUS; AMENABLE, DEMEAN!, PROME- NADE. 3. Latin -minére, to project, jut, threaten: EMI- NENT, IMMINENT, PROMINENT. 4. Suffixed o-grade form *mon-ti- in Latin méns (stem mont-), mountain: MONS, (MONTAGNARD), MONTANE, MONTE, MONTICULE, MOUNT!, MOUNT?, MOUNTAIN; AMOUNT, ULTRAMONTANE. [Pok. 1. men- 726, 2. menth- 732.] men-3, To remain. Variant suffixed (stative) form *man-é- in Latin manére, to remain: MANOR, MANSE, MANSION, (MENAGE); IMMANENT, PERMANENT, REMAIN. [Pok. 5. men- 729.] men-‘. Small, isolated. 1. Greek manos, rare, sparse: MANOMETER. 2. Suffixed o-grade form *mon-wo- in Greek monos, alone, only, single, sole: MONAD, MONAS- TERY, MONK, MONO-; PSEUDOMONAD. 3. Possibly also suffixed form *men-i-, a small fish, in Old English myne, mynwe, minnow, perhaps the source of Middle English meneu, a small fish: MINNOW. [Pok. 4. men- 728, meni- 731.] mend-. Physical defect, fault. 1. Latin mendum, menda, defect, fault: MENDICANT; AMEND, EMEND, (MEND). 2. Latin mendax, lying, liar: MENDACIOUS. [Pok. mend(a) 729.) mendh-'. To learn. Zero-grade form *mndh- in Greek manthanein (aorist stem math-), to learn: MATHEMAT- ICAL, (MATHEMATICS); CHRESTOMATHY, POLYMATH. [Pok. mendh- 730.] mendh-?. To chew. 1. Latin mandere, to chew: MANDI- BLE, (MANGE), MANGER. 2. Zero-grade form *mndh- in: a. Greek masasthai (< *math-ya-), to chew: MASSETER; b. Greek mastax, mouth, the model for expressive Greek (Doric) mustax, upper lip, mustache: (MOSTACCIOLI), MUSTACHE; Cc. Greek mastikhan, to grind the teeth: MASTICATE. [Pok. 2. menth- 732.] menegh-. Copious. Germanic *managa- in Old English manig, menig, many: MANY. [Pok. men(e)gh- 730.] meng-. To furbish. 1. Latin mango, furbisher, gem pol- isher, swindler: MONGER. 2. Greek manganon, magic
1228:ALERT al-1 ALEURONE al-4 ALEXIA feg-1 ALEXIPHARMIC alek- ALGOLAGNIA  slég- ALIAS al-1 “ ALIBI al-1, kWo- ALIBLE al-3 ALIEN al-1 ALIFORM_ aks- ALIKE fik- ALIMENT al-3 ALIMONY al-3 ALIPHATIC leip- ALIQUOT al-1, kwo- ALL al-5
```


## [2026-09-04T19:29:10.709Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef leaf_of(fn, lineno):\n    txt=open(fn,encoding='utf-8',errors='replace').read()\n    lines=txt.split('\\n')\n    upto='\\n'.join(lines[:lineno])\n    return upto.count('\\f')\nfor fn,ln in [('BRT.txt',6148),('BRT.txt',4374),('KLN_1966.txt',2157)]:\n    print(fn,ln,'leaf',leaf_of(fn,ln))\nEOF\necho \"=== BRT offset info ===\"; python3 -c \"\nimport json;d=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'));print(d['BRT'].get('page_offset'));print(d['BRT'].get('lookup_hint'))\""
}
```


### [2026-09-04T19:29:12.451Z] TOOL RESULT

```
BRT.txt 6148 leaf 163
BRT.txt 4374 leaf 101
KLN_1966.txt 2157 leaf 36
=== BRT offset info ===
Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
```


## [2026-09-04T19:29:16.993Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in (163,101):\n    p=t[i]\n    nums=re.findall(r'^\\s*(\\d{2,4})\\s*$', p, re.M)\n    print('leaf',i,'standalone nums',nums[:10])\n    print(p[:300].replace('\\n',' | '))\n    print('...')\nEOF"
}
```


### [2026-09-04T19:29:18.887Z] TOOL RESULT

```
leaf 163 standalone nums []
,  Stud-  /.  3i4>  West  SEE.  37.  175  (wo auch  lU  Pü.),  DsT.  ZA.  /.  200.  —  'ti  Vgl.  zu aiJAi«-3.  EN.— '»)NA.fli3.ÄfW.  Y^.:  SArmazd u  asavahisl  ki  tan  an  ...  —  '9)  NA,  asäjii. —  »)  VIL  lu  'asa-,  s.  DsT.s  Übersetzung.  — ")  Heilst  das:  "Soll  sie  für  ihn  die  kir
...
leaf 101 standalone nums []
 'kein Beiwohnen  (seitens  eines  Mannes)  habend, ; ohne  Beischlaf' :  tum . .  aH'a  . .  °tis  hunahi ' "gebierst  du  allein  . ,  ohne  Beischlaf?"  V.  ■ iS-io;  31. | Zorn  V.  ^ah;    eig.  'kein  DabeiEcin   habend';' | iSchr.  mit  ä  s.  S  26S.  3  a.—  Pü. :  /Vi  anapar ! ra^oimlh.  ! | • 
...
```


## [2026-09-04T19:29:24.784Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(160,168):\n    nums=re.findall(r'\\b(2\\d\\d|3\\d\\d)\\b', t[i][:400])\n    print(i, nums[:8], '|', t[i][:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T19:29:26.657Z] TOOL RESULT

```
160 [] | auh fus  Yt.13.TT,  —  haoma..  yaorum  (sd.)  äste  V,4.45;  —  ahunm haÜTm^a  
161 ['335', '236'] | mqsdrä  (sd.)  °ia  (Instr.)  yeiä  yä dby  Google 335 'aäa-  A  i  a 'aäa-  Alf
162 [] | maitl{sd.)  tpvrstm  dasvä ,. varfhuya  savö  Sda  °sa  (Instr,)  Aasö  (sd.) fm
163 ['200'] | ,  Stud-  /.  3i4>  West  SEE.  37.  175  (wo auch  lU  Pü.),  DsT.  ZA.  /.  20
164 [] |  weit- aus stärkste':  Aa  druxi  -ta  atahal  FrW. 8.2. SoperL  in  ai.aejak-. 
165 [] | vi  Y. 43. 5 ;  —  tSm  vatmklm  yasä  (sd.)  °sim  Y. 5;. ai;  —  maifyn  siaya
166 ['353'] | ci'iim   nisirtnuyät  ^.14.1;  A.3.J; —  asmanivä  (sd.)  zao^ra  ä>re  a°  fats
167 [] | a-  Adj.  'der  vom  Heiligen'' geschaffen  ist':  vTspaca  däma  . .  ya  'ta (
```


## [2026-09-04T19:29:40.116Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ard/Mehl ===\"; grep -n \"ārd\\|ärd\\|Mehl\" HUB.txt | head -20; echo; echo \"=== PHD ard ===\"; grep -n -i \"flour\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-04T19:29:40.184Z] TOOL RESULT

```
=== HUB ard/Mehl ===
1414:320. Np. plst - nicht pist — heisst *MehI, gerSstetes Mehl'.
3786:Mehl') aber auf schlechter Etymologie beruht.
8445:= zd. xsvasti- ; pist 'Mehl' = skr. pista- ; mahist (ZDM6.

=== PHD ard ===
PHD.txt:172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
PHD.txt:536:pa(č)čēn [pcgn!] copy. *pa(č)čībāg [pcyp k', PWNe- | N *pajiw] *deceptive. ^h : deceit, hypocrisy. *pa(č)čībāy- [pcyp'd-, PWNc-] deceive. pad [PWN, for *pty | M pd, N pa] to, at, in, on. pad- [pt- | M *pd-) fall. padam [pd”m | (IN pandm)] mask for the mouth, worn by a celebrating priest. !Ipádan, pày- (UIN TLWN-tn! < А V ntr; Ptn, pd- | M pd, p’y-, N páyidan] protect, watch, defend. *pádan, pāy- [N TLWN-tn!, etc.] stand, wait. pādāšn [p?td?fn! | M p’d’syn, N pàdàs] reward, retribution. padēx [ptyhw'] flourishing, prosperous. ~ih: prosperity. padéxénidan, padéxén- [ptyhwyn-ytn'] make flourish, prosper. pādēz [p'tyc | M p'dyz, N pāyēz] autumn. pad-góhr [PW Ngwhl] т. jewelled; 2. of good stock, well-born. padifrah [p’tpl’s | M p'dypr?h, N *pādafrāh] punishment, retribution. padir-, ~išn, v. padiriftan. padirag [ptylk' | M pdyrg, N paóira] towards, against, counter-. (6) — madan: come to mect. ~ih: meeting, opposition.
PHD.txt:551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
PHD.txt:1973:flourish, make ~ padéxénidan.
PHD.txt:1974:flourishing padéx; v. prosperous.
PHD_mackenzie.txt:878:   afrosag [)p/wlk l I N - a] a sweetmeat made of flour, butter, and honey.
PHD_mackenzie.txt:1163:ard [KHMA < A qmJ/; )lt l IN....,] flour.
PHD_mackenzie.txt:3906:padex [ptyhw ] flourishing, prosperous.
PHD_mackenzie.txt:3909:padexenidan, padexen- [ptyhwyn-ytn ' ] make flourish, prosper.
PHD_mackenzie.txt:4245:pist [pst' IN ......] browned flour.
PHD_mackenzie.txt:6596:field kisw(iin)zar.                        flour ard; browned ..... pist.
PHD_mackenzie.txt:6597:fierce sturg.                              flourish, make ..... padexenidan.
PHD_mackenzie.txt:6598:fifteen panzdah.                           flourishing padex; v. prosperous.
```


## [2026-09-04T19:29:41.111Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB flour ===\"; grep -n -i \"flour\" NYB_vol2_glossary.txt | head -20; echo \"=== CHEUNG arH/grind ===\"; grep -n -i \"to grind\" CHEUNG.txt | head -20"
}
```


### [2026-09-04T19:29:41.176Z] TOOL RESULT

```
=== NYB flour ===
2069:hur [ŠKL] a strong beverage 9?!. — The whole situation implies that the cup offered to Artaxšēr contained a refresh- ing beverage. In Firdausi’s version of the incident the refreshment was composed of sugar, flour and cold water (šukkar u pist bà äb-i sard). In Kn, the water being missing, we must assume that škl does not mean šukkar, but the ideogr. SKL, Aram škar, šikra (Syr Sakrä) = hur (FrP 5), from Av. (1837) hurd, a sort of fermented alcoholic liquor, probably kou- miss.
3150:pist [pst'] flour, or something pounded or crushed 91.25.26, — NP pist ‘bruised
=== CHEUNG arH/grind ===
5089:*NEIR: Wa. ÖBIX-/60Xt- ‘to grind’, dasn, dasnak ‘grindstone’, Sariq. dex-t ‘to crumble, 
6266:*drauš ? ‘to grind’ 
6271:*NWIR: Bal. drus(i)t/drus- ‘to grind, mill’, NP durust ‘raw, rough, huge’, borrowed 
11433:*HarH ‘to grind (grain)’ 
11435:*AVESTAN: YAv. *ar- ‘to grind’ 
11439:*MIDDLE PERSIAN: BMP ’I- (THNN-) /ar-/ ‘to grind, mill’, BMP "It /ard/ ‘flour’ 
11441:*KHOTANESE: LKh. arr- ‘to grind’ = SGS: 10 
11444:*CHORESMIAN: mjn- ‘to grind’, "rd ‘flour’, ’r@ (Ё) ‘mill-stone’ = Samadi: 115 
11448:ar-, Yzd. är- ‘to grind’, Abz. har/har- ‘id.; to thresh’, NP ard, (? borrowed into) Bal. 
11454:grind’, Yi. yan-/yäg’i- ‘to grind’, Pash. aneyal ‘to grind’, Pash. oró (m. pl.), Sh. 
11462:«PIE *H5elH;- ‘to grind’ = LIV: 277 | Pok.: 28 f. 
18711:*NWIR: Bal. nasit/nas- ‘to grind up, destroy, ruin, defeat’, Kurd. nast (orig. ppp.) 
19267:*AVESTAN: Y Av. pis- ‘to grind’ = Liste: 35 
19278:*CHORESMIAN: (+ *fra-) sPY- ‘to grind’ = Samadi: 199 
22302:*pati-) ps’w- to grind’ || (+ *fra-) m/rs’w- ‘to rub, smooth’. © With regard to Chor. 
29966:‘to grind, rub to powder’, Ishk. avZinj- ‘to express’ || (+ *aua-) Wa. vzom-/vzomd-, 
56682:to grind
```


## [2026-09-04T19:29:46.296Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11425,11475p' CHEUNG.txt"
}
```


### [2026-09-04T19:29:46.342Z] TOOL RESULT

```
166 *HarH 


*REFERENCES: KPF II: 199; Christensen, Contributions I: 66; IIFL II: 538a; Andreev — PeSéereva: 346a; 
EVS: 66b; Abaev, Slovar’ П: 350; WIM I: 72; WIM III: 114; Werba 1997: 165; Steblin-Kamenskij 1999: 
301, 305 


*HarH ‘to grind (grain)’ 

*AVESTAN: YAv. *ar- ‘to grind’ 

Partic.: perf. pass. Ү Ау. aša- ‘ground’ (V 5.52, V 7.35) 

*MIDDLE PERSIAN: BMP ’I- (THNN-) /ar-/ ‘to grind, mill’, BMP "It /ard/ ‘flour’ 
*PARTHIAN: ? yw-’rd’w ‘corn’ (rather the ‘righteous barley’ ?) = DMMPP: 374b 
*KHOTANESE: LKh. arr- ‘to grind’ = SGS: 10 

*SOGDIAN: BSogd. "mo ‘millstone’ (SCE 231), BSogd. "ró'rn'k ‘mill’ (SCE 161) 
*CHORESMIAN: mjn- ‘to grind’, "rd ‘flour’, ’r@ (Ё) ‘mill-stone’ = Samadi: 115 
*BACTRIAN: орбо “Йош? = S-W, Bact.: 181a 

*NWIR: (+ *ä- ?) Kurd. (Kurm.) héran/hér-, Awrom. haráy/hàr-, Bakht. ardan, Gz. 
ar-, Yzd. är- ‘to grind’, Abz. har/har- ‘id.; to thresh’, NP ard, (? borrowed into) Bal. 
art, Kurd. (Kurm.) ar(d), (Sor.) ard, Zaz. ar(di), Abyan. ard (f.), Anar. art, Tal. orda, 
Khuns. art, Gz. art, Gur. árd(1), Siv. агае ‘flour’, Abyan. ar (Ё), Khuns. ar ‘mill’, Gz. 
arun ‘miller’ 

*NEIR: Sh. (Baj.) yan-/yiyd, упа, Sariq. yon-/, yüyj, уйе, Yzgh. yawn-/yüg ‘to 
grind’, Yi. yan-/yäg’i- ‘to grind’, Pash. aneyal ‘to grind’, Pash. oró (m. pl.), Sh. 
(Baj.) yoyj (m.), Bart. yowj, Rosh. yawj, Sariq. yoyj, yowj, Yi. yaré, M. yori ‘flour’, 
? Oss. I. aryng ‘trough in which flour is mixed’ 

*MISC: Orm. hinl-’&k ‘ground, pulverized’, Par. wärun ‘flour’ 

*SANSKRIT: ? ata ‘flour’ (Hi.), Pkt. ata ‘flour’ (Niya) = EWAia I: 108 

«PIE *H5elH;- ‘to grind’ = LIV: 277 | Pok.: 28 f. 

*IE COGNATES: Gr. &A€@, Arm. alam ‘I grind’, etc. 

*REFERENCES: EVP: 12; IIFL I: 397a, 297b; Bailey 1933: 60; Bailey 1936: 338; IIFL II: 272b, 273b; 
Abaev, Slovar’ I: 74 Ё; MacKenzie 1966: 96; EVS: 106a, 119b; WIM I: 342 f.; DKS: 22a; WIM 1I/2: 637 


£; WIM III: 303; ESIJa I: 200 £; Cabolov 2001: 82 f., 436; Lecoq 2002: 572b, 594b, 606a (passim); 
NEVP: 10; Korn 2005: 189, 270 


*Harj ‘to be worth’
```


## [2026-09-04T19:30:01.673Z] TOOL CALL #34: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-42.json | head -120"
}
```


### [2026-09-04T19:30:03.239Z] TOOL RESULT

```
{
    "pdf_page": 42,
    "book_page": 12,
    "verified_by": "claude-fable-5-1",
    "verified_on": "2026-09-04",
    "entries": [
        {
            "entry": 0,
            "root": "Ak, Aq, Aken",
            "verdict": "confirmed",
            "modern_form": "PIE *h\u2082e\u1e31- (trad. *ak-/*ok-) 'sharp, pointed, edged', with the derived n-stem *h\u2082\u00e9\u1e31-mon- 'stone, sky' and the n-formant stem *ak-en- 'stone'",
            "note": "Pokorny I 18-22 heads the entry '2. ak-, ok- \u201ascharf, spitz, kantig\u2018 und \u201aStein\u2018', i.e. exactly Nourai's gloss 'sharp, also a sharp stone'; Walde-Pokorny I 28 has the same lemma 'ak- (z. T. auch \u0101k-) \u201ascharf, spitz, kantig; Stein\u2018'. Nourai's three-part root name reproduces three sources: Klein s.v. 'acrid' writes the base '*ak-, *aq-' (whence 'Ak, Aq'), and Pokorny p.19 has the sub-stem 'aken-' (Av. as\u01ddnga-, OP a\u03b8anga-) (whence 'Aken'). Language label 'Indo-European' correct. TWO CROSS-CUTTING PROBLEMS on this page. (1) The Persian 'weighing' words \u2014 sang/sax 'to weigh', Pahl. saxt, NP sanj\u012bdan, sanje\u0161, saxtan (nodes #4, #5, #7) \u2014 do NOT belong to this root. They are the verb MP saxtan/sanj- 'to weigh', from Old Iranian *\u03b8an\u01f5- 'to pull, draw' (Cheung, EDIV p.392; Abolghasemi FFD p.60; H\u00fcbschmann PSt \u00a7747 already called Horn's remark on sanj\u012bdan 'unklar'). The association with sang 'stone' is a Persian folk etymology helped by the variant sang\u012bdan and by sanje 'balance-weight (a stone)'. (2) Nourai analyses Av./OP asman- as 'as-man = like stone' with a cross-reference to root 'Men 1' \u2014 that is the Borh\u0101n-e Q\u0101te\u02bd explanation ('\u0645\u0639\u0646\u06cc \u062a\u0631\u06a9\u06cc\u0628\u06cc \u0622\u0646 \u0622\u0633\u06cc\u0627 \u0645\u0627\u0646\u0646\u062f \u0627\u0633\u062a', p.42), which Mo\u02bfin's own footnote on that very page flatly rejects: '\u06f4 - \u0627\u06cc\u0646 \u062a\u0648\u062c\u06cc\u0647 \u062f\u0631\u0633\u062a \u0646\u06cc\u0633\u062a' ('this explanation is not correct'). asman- is a plain n-stem *h\u2082\u00e9\u1e31-mon- 'stone > stone vault of heaven', not a compound with a word for 'like'.",
            "sources": [
                "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82e%E1%B8%B1-"
            ],
            "ref_check": [
                {
                    "ref": "POK:18",
                    "status": "supports",
                    "note": "POK_01.txt \u21b5-leaf 25 (printed p.18): '2. ak-, ok- \u201ascharf, spitz, kantig\u2018 und \u201aStein\u2018.' The very first item of the e/o-stems on that page is 'Npers. \u0101s (dehnstufig) \u201aM\u00fchlstein\u2018' \u2014 Pokorny himself puts Persian \u0101s under this root. Entry closes 'WP. I 28 ff., WH. I 6 ff.'"
                },
                {
                    "ref": "KNT:173",
                    "status": "supports",
                    "note": "KNT.txt leaf 195 (running head '173'): 'asan- sb. \u201astone\u2018: pIE *aken- (\u00a79.V, \u00a787, \u00a7155.1), cf. asman-'; and 'asman- sb. \u201asky\u2018: Av. asman-, Skt. \u00e1\u015bman-, Gk. \u1f04\u03ba\u03bc\u03bf\u03bd \u201aanvil\u2018, Lith. akmu\u00f5 \u201astone\u2018, pIE *akmen-/mon-'. Kent's '*aken-' is Nourai's third root name."
                }
            ],
            "nodes": [
                {
                    "id": 1,
                    "lang": "Avestan / Old Persian",
                    "words": "as 1, asan : stone; as-man, as-mana : like stone, sky",
                    "verdict": "plausible",
                    "derivation": "Av. asan- (gen. asn\u014d) 'stone' and asman- 'stone; heaven', OP asman- 'sky' (Bartholomae AiW col. 207; Kent p.173) continue PIE *h\u2082e\u1e31-/*h\u2082\u00e9\u1e31-mon- (Skt. \u00e1\u015bman- 'stone, rock, sky', Gk. \u1f04\u03ba\u03bc\u03c9\u03bd 'anvil', Lith. akmu\u00f5 'stone', OCS kamy with metathesis). The semantic bridge 'stone' > 'sky' is the Indo-Iranian conception of the firmament as a stone vault (Reichelt IF 32, 23 ff., quoted verbatim by both Pokorny and Walde-Pokorny). Nourai's forms and glosses are right, but his morphological analysis is not: 'as-man, as-mana = like stone' treats -man as a separate morph 'like' (his cross-reference '\u261e Men 1'), whereas asman- is an inherited n-stem *h\u2082\u00e9\u1e31-mon- with the ordinary Indo-Iranian -man- suffix; asmana- is simply the derived adjective 'of stone, stony' (Av. asmana-, OP a\u03b8an(g)aina-), not 'like stone'. Kent adds that OP is asman-, 'Not \u0101sman-, despite NPers. \u0101sm\u0101n, which has length of later origin'.",
                    "sources": [
                        "https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D9%85%D8%A7%D9%86",
                        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82e%E1%B8%B1-"
                    ],
                    "ref_check": [
                        {
                            "ref": "POK:19",
                            "status": "supports",
                            "note": "POK_01.txt \u21b5-leaf 27 (printed p.19), section '4. Mit m-Formantien: ak-men-/-mer-': 'Ai. a\u015bman- n. \u201aStein, Himmel\u2018 ... av. asman- \u201aStein, Himmel\u2018 ... gr. \u1f04\u03ba\u03bc\u03c9\u03bd \u201aAmbo\u00df\u2018 ... lit. akmu\u00f5 \u201aStein\u2018.' The following section '5. Mit n-Formantien: aken-' has 'av. as\u01ddnga-, apers. a\u03b8anga- \u201aStein\u2018'."
                        },
                        {
                            "ref": "KLN:18",
                            "status": "supports",
                            "note": "KLN_1966.txt leaf 21 = printed p.18, s.v. 'acrid': '... fr. I.-E. base *ak-, *aq-, \u201asharp, pointed\u2018, whence also ... Gk. \u1f04\u03ba\u03c1\u03bf\u03bd ..., \u1f00\u03ba\u03bc\u03ce\u03bd \u201aan anvil\u2018, OI. a\u015bri\u1e25 \u201aedge\u2018, a\u015bman- \u201astone, rock, sky\u2018, Avestic asman- of s.m., Lith. akmuo \u201astone\u2018 ... OSlav. kamy (a metathesized form) \u201astone\u2018.' Exactly the arrow Nourai draws, and the source of his root-name variant 'Aq'."
                        },
                        {
                            "ref": "KNT",
                            "status": "supports",
                            "note": "KNT.txt leaf 195 (p.173): 'asan- sb. \u201astone\u2018: pIE *aken-'; 'asman- sb. \u201asky\u2018 ... pIE *akmen-/mon-'; also leaf 47 (p.32) 'asan- \u201astone\u2018 with Med. s ... cf. also acc. asm\u0101nam \u201asky\u2018, Av. asman- \u201asky, stone\u2018'."
                        }
                    ],
                    "consulted": [
                        {
                            "src": "BRT",
                            "where": "col. 207 (BRT.txt leaf 147; column number '207' printed on the preceding leaf, and confirmed by Kent's citation 'Bthl. AiW 207' s.v. Asagarta- and by Jeffery FVQ 164 n.5 'Bartholomew, AIW, 207')",
                            "stance": "supports",
                            "note": "'j., g. (, p.) asan-, [asan-tar-], j., p. asman- m. 1) \u201aStein\u2018 ... a) als Amulet ... b) als Waffe, \u201aSchleuderstein, Steingeschoss\u2018'; asman- is cross-referred 's. unter asan-'."
                        },
                        {
                            "src": "WLD",
                            "where": "Bd. I p.28 ff. (WLD_Bd1_pages.txt, section 'Mit m(e)n-Formantien')",
                            "stance": "supports",
                            "note": "'ai. \u00e1\u00e7man- m. \u201aStein, Fels; Himmel\u2018 (zur Vorstellung des Himmels als eines Steingew\u00f6lbes s. Reichelt IF. 32, 23 ff.) ... av. asman- \u201aStein, Himmel\u2018, asmana- \u201asteinern\u2018, ap. asman- \u201aHimmel\u2018 ... ap. a\u03b8an(g)aina- \u201asteinern\u2018.' Note WLD glosses asmana- 'steinern' (of stone), not 'like stone'."
                        },
                        {
                            "src": "SYN",
                            "where": "Buck 1.44 STONE; ROCK, p.52 (SYN.txt leaf 78)",
                            "stance": "supports",
                            "note": "'Skt. a\u00e7man-, a\u00e7an-, Av. asan- (asman- \u201asky\u2018) \u201astone\u2018, adj. Av. asmana-, OPers. a\u03b8a(n)gaina- \u201aof stone\u2018, NPers. sang \u201astone\u2018 ... Grk. \u1f04\u03ba\u03bc\u03c9\u03bd \u201aanvil\u2018 ... Walde-P. 1.28 ff.'"
                        },
                        {
                            "src": "IEC",
                            "where": "Mann s.v. akm\u00f3(n), akmen-",
                            "stance": "supports",
                            "note": "'akm\u00f3(n), akmen- \u201astone, boulder, crag\u2018. WP I, 29, 33' with OCS kamy, Lith. akmuo, Latv. akmens."
                        },
                        {
                            "src": "AHD",
                            "where": "Watkins 1985 s.v. ak-, \u00a73",
                            "stance": "supports",
                            "note": "'Suffixed form *ak-men, stone, sharp stone used as a tool, with metathetic variant *ka-men-'."
                        }
                    ]
                },
                {
                    "id": 2,
                    "lang": "Pahlavi",
                    "words": "\u00e2s : mill, mill stone; \u00e2s-\u00e2p : water mill; v\u00e2t-\u00e2s : wind mill; \u00e2s-m\u00e2n : sky",
                    "verdict": "plausible",
                    "derivation": "Old Iranian *\u0101sa- (lengthened grade *\u0101\u1e31- of the 'stone' root; Pokorny p.18 lists 'Npers. \u0101s (dehnstufig) \u201aM\u00fchlstein\u2018' under ak-) gives Middle Persian \u0101sy\u0101g [\u02beis\u02bek'] 'mill(-stone)' and the compound \u0101sy\u0101b [\u02beis\u02bep] '(water-)mill' = \u0101sy\u0101 + \u0101b 'water' (MacKenzie CPD p.13); \u0101sm\u0101n [\u02beism\u02be\u0101n'] 'sky, heavens' (CPD p.12) continues OP asman- with secondary lengthening of the initial vowel already in Middle Persian. Two of Nourai's four forms are only approximately Pahlavi: the simplex '\u0101s' and the compound 'v\u0101t-\u0101s' (w\u0101d 'wind' + \u0101s) are not in MacKenzie or Nyberg; MP has \u0101sy\u0101g/\u0101sy\u0101b, and the wind-mill compound is attested as New Persian b\u0101d\u0101s (BQT p.39 footnote lists \u0622\u0633\u06cc\u0627\u060c \u0622\u0633\u06cc\u0627\u0628\u060c \u0628\u0627\u062f\u0622\u0633\u060c \u062e\u0631\u0622\u0633\u060c \u062f\u0633\u062a\u0622\u0633\u060c \u067e\u0627\u062f\u0622\u0633). Also, \u0101sm\u0101n does not descend from \u0101s 'mill' but in parallel with it from Av./OP asman-.",
                    "sources": [
                        "https://en.wiktionary.org/wiki/%D8%A2%D8%B3%DB%8C%D8%A7%D8%A8",
                        "https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D9%85%D8%A7%D9%86"
                    ],
                    "ref_check": [
                        {
                            "ref": "BQT:39,42,43",
                            "status": "supports",
                            "note": "BQT_v1_pages.txt leaves 249/252/253 = printed pp.39/42/43. p.39-40 s.v. \u0622\u0633: '\u0622\u0633\u06cc\u0627\u0628\u0627\u0646 \u0628\u0627\u0634\u062f \u0686\u0647 \u0622\u0633\u06cc\u0627 \u0631\u0627 \u0622\u0633 \u0645\u06cc\u06af\u0648\u06cc\u0646\u062f' ('... because \u0101sy\u0101 is called \u0101s'), with Mo\u02bfin's footnote 1: '\u0633\u0627\u0646\u0633\u06a9\u0631\u062a a\u015bman ... \u0627\u0648\u0633\u062a\u0627 asanga \u0648 asan \u0628\u0645\u0639\u0646\u06cc \u0633\u0646\u06af \u00ab\u0628\u0627\u0631\u062a\u0648\u0644\u0645\u0647 \u06f2\u06f0\u06f7\u00bb\u060c \u0622\u0633 \u062f\u0631 \u0644\u063a\u0627\u062a \u0622\u0633\u06cc\u0627 \u0648 \u0622\u0633\u06cc\u0627\u0628 \u0648 \u0628\u0627\u062f\u0622\u0633 \u0648 \u062e\u0631\u0622\u0633 \u0648 \u062f\u0633\u062a\u0622\u0633 \u0648 \u067e\u0627\u062f\u0622\u0633 ...'. p.42 s.v. \u0622\u0633\u0645\u0627\u0646: '\u0645\u0639\u0631\u0648\u0641\u0633\u062a \u0648 \u0628\u0639\u0631\u0628\u06cc \u0633\u0645\u0627 \u0648 \u0641\u0644\u06a9 \u062e\u0648\u0627\u0646\u0646\u062f\u060c \u0648 \u0645\u0639\u0646\u06cc \u062a\u0631\u06a9\u06cc\u0628\u06cc \u0622\u0646 \u0622\u0633\u06cc\u0627 \u0645\u0627\u0646\u0646\u062f \u0627\u0633\u062a ... \u0686\u0647 \u0622\u0633\u06cc\u0627 \u0631\u0627 \u0622\u0633 \u0646\u06cc\u0632 \u06af\u0648\u06cc\u0646\u062f', with Mo\u02bfin's footnote '\u0627\u0648\u0633\u062a\u0627 asan \u0628\u0645\u0639\u0646\u06cc \u0633\u0646\u06af \u00ab\u0628\u0627\u0631\u062a\u0648\u0644\u0645\u0647 \u06f2\u06f0\u06f7 \u0648 \u06f2\u06f2\u06f0\u00bb ... \u0686\u0648\u0646 \u0622\u0633\u0645\u0627\u0646 \u0631\u0627 \u0633\u0646\u06af\u06cc \u067e\u0646\u062f\u0627\u0634\u062a\u0647\u200c\u0627\u0646\u062f ... \u067e\u0647\u0644\u0648\u06cc \u0101sm\u0101n' and the correction '\u06f4 - \u0627\u06cc\u0646 \u062a\u0648\u062c\u06cc\u0647 \u062f\u0631\u0633\u062a \u0646\u06cc\u0633\u062a'. p.43 s.v. \u0622\u0633\u06cc\u0627. So the three cited pages carry exactly the four words of this node."
                        }
                    ],
                    "consulted": [
                        {
                            "src": "PHD",
                            "where": "MacKenzie, CPD pp.12-13",
                            "stance": "partial",
                            "note": "'\u0101sm\u0101n [\u02beism\u02be\u0101n' | = M, N \u0101sm\u0101n] sky, heavens; cal. 27th day'; '\u0101sy\u0101b [\u02beisy\u02bep] (water-)mill. \u0101sy\u0101g [\u02beisy\u02bek' | N \u0101sy\u0101] mill(-stone)'. Supports \u0101s-\u0101b and \u0101s-m\u0101n but has no bare '\u0101s' and no 'w\u0101d-\u0101s'."
                        },
                        {
                            "src": "NYB",
                            "where": "Manual of Pahlavi II (Glossary)",
                            "stance": "silent",
                            "note": "The K\u0101rn\u0101mag glossary attests asm\u0101n only inside phrases (e.g. 'x\u02bbat\u0101i i miy\u0101n i asm\u0101n' s.v. miy\u0101n, 'asm\u0101n \u010dig\u014dn?' s.v. \u010dig\u014dn); no headword entry and no mill word."
                        },
                        {
                            "src": "HRN",
```


## [2026-09-04T19:30:12.865Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 al- mahlen ===\"; grep -n \"mahlen, zermalmen\\|zermalmen\" incoming/WLD/WLD_Bd1_pages.txt | head -10; echo \"=== WLD aleuron ===\"; grep -n \"aXevoov\\|äXevQov\\|alauri\\|aleicr\\|aleur\" incoming/WLD/WLD_Bd1_pages.txt | head -10"
}
```


### [2026-09-04T19:30:12.928Z] TOOL RESULT

```
=== WLD Bd1 al- mahlen ===
8106:5.   al- „mahlen,            zermalmen“.
49061:qHeru- „kauen; zermalmen, mahlen (Mehl und daraus bereitetes)“.
55514:,,zusammendriicken, quetschen", norw. knysia ..zermalmen", ahd. knussen
55519:knussjan s. genu-) „zermalmen", mit a aschw. knusu = nd. knust „driicken,
57029:    fr>n,.zermalmen“ (beide nicht wahrscheinlicher zu g«er- „schwer" durcli
61667:          driiber fahren und es zermalmen, krachend schlagen“ (und andere
61671: mnd. krossen, schwed. kro-ssa, kryssa „zermalmen“; got. krms-tan „knirschen“,
62220:   ghrcndh- ags. grindan ,. zerreiben, zermalmen**, engl. to grind ,,ds.,
63732:   Schw. dial. Jcvadda „in Stiicke sehlagen, zermalmen" nd. quaddcren ds.,
64912:setzen; jedoch got. gakroton ,,zermalmen" (als d-Praes. zu einem g'J.ra „Miihl-
=== WLD aleuron ===
8127:  Arm. alam „malile“, atauri (* alatrio -) ,.Muhle“, aleur „Mehl“ (trotz l statt
```


## [2026-09-04T19:30:14.810Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ===\"; grep -n \"aleuron\\|al-euro\\<\\|alew\\|ale:o\\|alein\" IEC.txt | head -15; echo \"=== SYN flour ===\"; grep -n -i \"flour'\\|FLOUR\\|5.55\\|grind\" SYN.txt | head -25"
}
```


### [2026-09-04T19:30:14.887Z] TOOL RESULT

```
=== IEC ===
12110:olénà, olinà, olənā ‘forearm, elbow, ell" WP I, 156 Per. cf. arang ‘elbow’; Oss. cf. árm-àárin, Dig. cáng-arinà "elt: Gk. oléne, f. ‘elbow’; Alb. llânë, T llërë, f. ‘forearm; eil; Lat. ulna, Fa- liscan olina "elt": Olr. uilen & uilind, f.; Ir. uille, gs: uilleann, f. ‘elbow, forearm, bend’; OBr. elin, Br. élin, ilin, pl. -u, m. ‘elbow’; W elin, pl. au, f. ‘elbow, bend’; Cor. elyn, pl. elynnow, m. id. (and “angle'); Go. aleina, f. "ell: OHG elina, f. ‘elbow’; OFris. elne, OE eln ‘forearm; el’; MHG elline, ellen, elne, len, sf. "ell": ON alin, ọln, pl. alnir & alnar, id.; Sw. aln, pl. -ar, f. id.
=== SYN flour ===
31:LPPPIOV4$94-4050565444 44455555 3 Geqy bis: REE bh puwNUl bUOLL 4 wtkbieesisaeviescibasein een
82:The two most general types are generalization or extension vs. specializa- tion or restriction. Generalization, as in barn etymologically ‘barley-plece’ whence storehouse for any grain or farm produce (now even carbarn), mill originally ‘machine for grinding’ (corn, etc.), and all words of such broad application as do, get, go, thing. Specialization, as in deer (see above), hound, originally any ‘dog’ (like NHG hund), sermon from Lat. sermé ‘dis- course’ specialized in church writings. The history of a given word may show successively a specialization and generalization from a new center, as starve from ‘die’ (as NHG sterben) to ‘die of hunger’ to ‘suffer from hunger’. But this classification is from one point of view only, that of scope. There are many other more specific types of shift within certain associated groups.
842:OE molde ‘loose earth, soil’ (NE mold) = Goth. mulda ‘dust’, Skt. mrd- ‘earth, clay’, fr. root *mel- in Lat. molere, Goth. malan, etc. ‘grind’ (5.56). Walde- P. 2.288. Feist 366.
934:Words for ‘sand’, apart from one widespread but difficult group (Grk., Lat., Gme., Arm.) and some of doubftul origin, come from verbs for ‘grind’, ‘scatter’, ‘blow’, ‘whirl’, with reference to the small particles of sand or their action in the air (hence some overlap- ping in cognate groups with words for ‘dust’). In afew the (sandy) ‘shore’ be- comes ‘sand’.
943:4. Goth. malma = ON malmr ‘ore, metal’, OF mealm in mealmstan ‘malm- stone’, OHG melm ‘dust’, all fr. the root of Goth. malan, Lat. molere, ete. ‘grind’. Walde-P. 2.285. Feist 343.
947:smilts, fr. *smel- beside *mel- in Lith. malti, Goth. malan, etc. ‘grind’. Walde- P. 2.286. 6. ChSL.péstikii, etc., general Slavic : Skt. parisu-, pansuka-, ‘dust’ (1.218). 7. Skt. valuka- (mostly in pl.), prob.
2126:5. Lith. pelenai (pl.), Lett. pelni (pl.), OPruss. pelanne, ChSl. popelii (later pepelti), SCr. pepeo, ete., general Balto- Slavic word, prob. (like Lat. cinis : Grk. ous ‘dust’) : Lat. pulvis ‘dust, pow- der’, pollen ‘fine flour or dust’, Grk. wéXn “fine flour or dust’, etc.; less prob. : ChSI. poléti, paliti ‘blaze, burn’ (1.84). Walde-P. 2.60. Ernout-M. 785.
4240:3. Ir. molt, W. mollt, Br. maout, a gen- eral Celtic word for ‘wether’ and prob. fr. *mel- ‘grind, crush’ (Ir. melim, Lat.
6881:6. ChSl. grystz, SCr. gristi (Boh. hryztt, Pol. gryzé also ‘gnaw’ as mostly Russ. gryzt’) : Lith. grauzti, Arm. krcem ‘onaw’, Grk. Bpixw ‘gnash, grind the teeth’. Walde-P. 1.697 f. Berneker 359.
8034:W. blin, cf. OBr. pl. blinion ‘inert’, Gael. blian ‘lean, insipid’ etym. dub., perh. (fr. IE *mléno- or *mlino-): Skt. mlana- ‘faded, withered, exhausted, languid’, pple. of mla- ‘fade, wither, grow weary’, SCr. mlitav ‘tepid, list- less’, etc. fr. extensions of IE *mel- ‘rub, grind’ (Walde-P. 2.284 ff.). G.S. Lane, Language 13.21 f.
8314:CHAPTER 5 FOOD AND DRINK; COOKING AND UTENSILS 5.11 Eat 5.57 Minn 5.12 Foop 5.61 Mezar 5.13 Drink (vb.) 5.612 Burcurr 5.14 Hunexr (sb.) 5.62 Brrr 5.15 Turrsrt (sb.) 5.63 Sausace 5.16 Suck (vb.) 5.64 Sour, Brots 5.17 Mrx 5.65 VEGETABLES ' 5.21 Cook (vb.) 5.66 Bran ? 5.22 Bor 5.67 Pra 5.23 Roast, Fry 5.68 Onion 5.24 Baxe 5.69 CaBBAGE 5.25 Oven 5.70 Porato 5.26 Por 5.71 Fruir 5.27 Kerrin 5.72 APPLE 5.28 Pan 5.73 PEAR 5.31 Disx 5.74 Pracu 5.32 Prats 5.75 Wie : 5.33 Bown 5.76 Grape 5.34 Pircuer, Jue 5.77 Nur 5.35 Cup 5.78 OLIvE 5.36 Saucer 5.79 Om 5.37 Spoon 5.80 Berry 5.38 Kyire 5.81 Saur 5.39 Fork 5.82 Prpprr 5.41 A Mua, 5.83 VINEGAR 5.42 BReakFast Bi Rdeer ona 5.43 Luncx 585 § 544 Dinner een Base Sucnbn. 5.86 Mixx (sb.) 5.51 Breap 5.87 Minx (vb.) 5.52 Caxn 5.88 CHEESE 5.58 Dover 5.89 Burrer 5.54 Kwrap 5.91 Merap 5.55 Mzau, Frour 5.92 Wine 5.56 Grinp 5.93 Brrr
8636:’ ss C 5 Walde-P, 9 po fine flour’, ete. 6849, «~~ TRout-M. 785. REW
9174:5. Lith. minkyti, Lett. micit : Skt. mac- ‘pound, grind’, perh. OK mengan ‘mix’, etc. (5.17). Walde-P. 2.268.
9177:5.55 MEAL, FLOUR
9180:NG dete ON mjol Lett.  miltz Lat. farina Dan. mel ChSl. maka It, farina Sw. mjél SCr. _ braSno ee farine OE melu Boh. mouka Tun lg ME mele, flour Pol. maka i i ind NE meal, flour Russ. muka Nir si Du. meel Skt. pista- Vv. mn OHG melo Av. iStra- * — blawd MHG mel e Br Bleud NHG mehl
9182:a a ‘grind’ (5.56) or ‘crush’, one Pitom the name of a cereal,
9183:Tk ag Mh ‘grind’ (6.56),
9189:5. ME, NE flour, the same word as flower, came to be used of the flower or finest part of the meal, then especially though not exclusively for the fine meal
9196:5.56 GRIND Grk. ddA Goth. malan Lith. malt NG aGw ON mala Lett. malt Lat. molere Dan. male ChSl.  mléti It. macinare Sw. mala SCr. — mlijeti Fr. moudre OE grindan Boh. = mliti Sp. moler ME _sgrinde Pol. mleé Rum. mdcina NE grind Russ. molot’ Ir. melim Du. —malen Skt. (pis-) Nir. meilimn OHG malan Av. bom ee W. malu MHG maln, malen Br. mala NHG  mahlen
9197:The earliest process of converting grain into meal was ‘crushing’ by pound- ing, whence later the ‘grinding’ between two stones. For the earlier process there is a distinctive group of cognates, namely Grk. rriccw (also ‘winnow’), Lat. pinsere, Skt. pis- (Walde-P. 2.1. Er- nout-M. 770). But such was also the more original force of IE *mel-, which furnishes most of the European words for ‘grind’ and ‘mill’, but shows its earlier sense in Arm. malen ‘pound, bruise’, Skt. mr-, mrd- ‘crush’, Lat. mollis ‘soft’, Toch. A malyw-, B mely- ‘press, tread’ (SSS 454).
9204:2. Grk. adéw, late édybw, NG &dWu : Arm. atam ‘grind’, atauri ‘mill’, aleur, ‘meal’, Skt. anu- ‘fine, thin’. Walde-P. 1.89. Boisacq 43.
9205:3. It. macinare, Rum. mdcina, fr. VLat. *machindre a new denom. of Lat. machina ‘machine’, with specialization to ‘grind’. REW 5206.
9206:4. OE grindan, ME grinde, NE grind : Du. grind, grint ‘gravel, coarse meal’, Lat. frendere ‘crush, bruise, gnash the teeth’, Lith. grendu, gresti ‘rub, scrape’, ete. Walde-P. 1.656 ff. Walde-H. 1.545.
9215:gdm, BEADS ON kvern, mylna Lett.  sudmalas (dzirnavas) ork. ate Dan.  meflle (kvern) ChSI. Zritniivi, zritny NG role, molina Sw. kvarn SCr. mlin (rvanj) Jae ulino OE cweorn, mylen Boh.  mlyn (Zerna) Ite noulin ME mylne, mille (quern) Pol. mlyn (zarna) i. molino 7) NE mill (quern) Russ. mel’/nica oe moar (rignild Du. molen ’ Skt. (pesana-) i brad, ae OHG  muli(n) (quirn) Av. (sudus-) Nir en) MEG mill(e) (btrne) r 1 9 us malin (breo) NHG_ miihle ‘ . . . . ~ “4 9 Mill’ is understood here in the origi- nes z oe to a water-mill(?). nal sense of ‘grist-mill, flour-mill’, not in | Muhl.-Kndz. 3. :
9217:Most of the words for ‘mill’ are deriv- atives of IE *mel- ‘crush, grind’, but in large part through the medium of Latin.
```


## [2026-09-04T19:30:22.749Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8100,8140p' incoming/WLD/WLD_Bd1_pages.txt; echo \"=== nearest page tag ===\"; awk 'NR<=8140 && /\\[pdf page/ {l=$0; n=NR} END{}' incoming/WLD/WLD_Bd1_pages.txt; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd1_pages.txt | awk -F: '$1<8140' | tail -3"
}
```


### [2026-09-04T19:30:24.943Z] TOOL RESULT

```
                                                al-    — alek-                                         89

5.   al- „mahlen,            zermalmen“.
     Gr. dXe-  dXko „mahle, zermalme" 1 ), aXexai Xe&oi „Muhlsteine“, aXexog
                 :




und dXsrog „das Mahlen“, aXerdov „Muhle“, aXstgevco „mahle“, aXe[f\ao, pi.
aXelaxa (mehr gedehnfc aus aXeaxa-, Schulze Qu. ep. 225) „Hehl“ (daraus
kontrahiertes *aXijxa rief den neuen sg. aXyx ov uX.evqov Hes. hervor dXij-
                                                                    '
                                                                                                   ;



xoEidi'jg Hippokr., aXiqxon' aXevgwv Rhinthon), uXevqov (*aXe-fo-ov) „Weizen-
                                      '



mehl“.
  Arm. alam „malile“, atauri (* alatrio -) ,.Muhle“, aleur „Mehl“ (trotz l statt
i nicht entlehnt aus ciXevgov,  Hubsehmann Arm. Gr. 1414).
                                                  <:
  Ai. anu- „fein, diinn, selir klein ( *al-nu -; Fortunatov BB. 6, 216), hindi
und bengali ata „Mehl“ (u. dgl.; Kuhn KZ. 30, 355); npers. anl „Helil“.
  Ay. asa- *<uta -) ,.gemahlen“ (Hubsehmann ZdMG. 3S, 428, Spiegel BB-
                     (

9,   178 A.      1).



ala    u. dgl.   „hallok!“
     Ai. alala(bhamnf-) „munter \verdend‘
=== nearest page tag ===
```


## [2026-09-04T19:30:34.351Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"npers\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | grep -i \"mehl\" | head -10; echo \"---\"; grep -n -A3 -B3 \"hindi\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -30"
}
```


### [2026-09-04T19:30:34.411Z] TOOL RESULT

```
5884:und bengali ata „Mehl“ (u. dgl.; Kuhn KZ. 30, 355); npers. anl „Helil“. 
---
5880-Arm. alam „malile“, atauri (* alatrio -) ,.Muhle“, aleur „Mehl“ (trotz l statt 
5881-i nicht entlehnt aus ciXevgov, Hubsehmann Arm. Gr. 1414). 
5882-
5883:Ai. anu- „fein, diinn, selir klein <: ( *al-nu -; Fortunatov BB. 6, 216), hindi 
5884-und bengali ata „Mehl“ (u. dgl.; Kuhn KZ. 30, 355); npers. anl „Helil“. 
5885-
5886-Ay. asa- ( *<uta -) ,.gemahlen“ (Hubsehmann ZdMG. 3S, 428, Spiegel BB-
```


## [2026-09-04T19:30:41.633Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if '5.   al- „mahlen' in p or '5. al- „mahlen' in p:\n        print('block',i,'of',len(t)); break\nEOF"
}
```


### [2026-09-04T19:30:43.269Z] TOOL RESULT

```
block 97 of 895
```


## [2026-09-04T19:30:47.915Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && for n in 97; do curl -sL -o wld$n.jpg \"https://archive.org/download/in.ernet.dli.2015.70244/page/n$n.jpg\" -w \"%{http_code} %{size_download}\\n\"; done"
}
```


### [2026-09-04T19:30:54.744Z] TOOL RESULT

```
200 674089
```


## [2026-09-04T19:30:57.082Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/wld97.jpg"
}
```


### [2026-09-04T19:30:58.292Z] TOOL RESULT

```

```


## [2026-09-04T19:30:58.289Z] INPUT

[Image: original 1837x2729, displayed at 1346x2000. Multiply coordinates by 1.36 to map to original image.]


## [2026-09-04T19:31:06.068Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index ARD ===\"; grep -n \"^ARD\\|ARD \\|Ard \" incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"=== ARY persian آرد ===\"; grep -n \"آرد\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-04T19:31:06.130Z] TOOL RESULT

```
=== ARY latin index ARD ===
2913:BREME, BARD ARMENIAN) 5+)
3076:OLD NORSE) Sp,  VARD (PAHLAVI) 5
3429:‘REFERENCES be theg BEREM, BARD —(ARMENIAN) gu!
4263:MALLORY & ADAMS: PERD PARD ENGLISH) godt
4268:scl 031 (LION + PARD) LEOPARD) 4 |, 25 slr PARD slots ols)! Glas Sh 2-1
6767:HEARD — (OLD ENGLISH) wf Ki! KRATU., KATHINA
6768:HARD ENGLISH) 5S KHELK ARMENIAN) gs!
6769:HAARD (DANISH) S\asl3 KRATUS (GREER) gli
6770:HARD (SWEDISH) Say HARDUS GOTHIC) S$
6771:BAARD NORWEGIAN) 15$33 OLD SCANDINAVIAN) pS 52h}
=== ARY persian آرد ===
1069:در آثار هومر یونانی آمده است که بردگان زن مسئول انجام کارهای شاق (مثلاً آردکر دن گندم وجو
12227:شباهت دارنسد ولی ظاهراً ایسن واژه‌ها از یک واجریشه‌ی هند و اروپایی دیگر (۳0738817) آرده‌اند
```


## [2026-09-04T19:31:08.217Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD aleurone ===\"; grep -n -i \"aleuron\" FSD_vol1.txt | head -5; echo \"=== WEB aleurone ===\"; grep -n -i \"aleuron\" WEB_vol1.txt | head -5; echo \"=== SKT ===\"; grep -n -i \"aleuron\" SKT.txt | head -5; echo \"=== ISS/DKS arr ===\"; grep -n \"arr- \\|'to grind'\\|to grind\" ISS_alt_DKS.txt | head -10"
}
```


### [2026-09-04T19:31:08.338Z] TOOL RESULT

```
=== FSD aleurone ===
=== WEB aleurone ===
5399:Al-eu-ri/tés, n. [L., from Gr. aleurités, per- taining to aleuron, meal, from alein, to grind.] a genus of cactuslike plants, including the candleberry tree. s
5400:a-lei’/rd-man.-cy, n. (Gr. aleuromanteion, divi- nation by meal; aleuron, meal, and mantera, divination.] a kind of divination by flour or meal.
5401:al-eu-rom/e-tér, n. [Gr. aleuron, meal, and melron, measure.] an instrument for testing the quality of gluten in flour.
5402:à-leū’rö- nat, n. flour made of aleurone. 3
5404:al-et-ron/ic, a. pertaining to or resembling aleurone. x
=== SKT ===
=== ISS/DKS arr ===
414:anühvarremüte jsa "without grasping’, v 124, 4b4; K 53'10"10 akāşțye anihvarrdye büvani gihna, K 63, 78r1 aküstye anahvardye büoaña gihna ‘by aid of bhavana- meditation inconceivable, ungraspable', Manj. 354 anühvarada, = BS agrühya-. See nuhvarr- ‘to grasp’.
763:аай 'flour', Sid. r33rr, Tib. Aye, Sid. 142v1 ara (-r- for -d-), BS saktu-; 2nd component Sid. 143r2 rrüsadá ‘barley flour', п 85:76; 86-87 rüsádá, in phrase n 23'19:2 rrufi jsa adi. Base ar- 'to grind' see ärr- “to grind’, For ‘flour’, the participle a-rta-, -ka-, here āda- (either *arata- or a-rta-), Zor.P., Yayn. art, N.Pers. ard, Pašto бгә masc. plur., Waziri Pašto 4уә ‘dough’, Yidya yărë, yüray ("ürtaka-), Suyni yauyJ, Sarikoli yoyJ, youj, Sangle& wulok, Рагаёй wárun (*àrtana-). O.Ind. affa-, Hindi äjā, Kroraina afa, from *айа- (T. Burrow, BSOAS 35, 1972, 539).
854:агг-, later ár-, participle árrda-, later arda- 'to grind’, Sid. 150v5 йсі jsa ārrāñä ' it is to be ground in water’, BS jala- pista-, Tib. čhu dags-su byas-pa (hthag-ba ‘о grind"); п 71:6, 2 plur. imperative, ganam và bisa bisai arryará 'grind the corn in the house’; participle ш 93:264 árrdá hauska ysálva ' ground dry barberry’; 1 145, 53v5 nauká araña, BS dapaya; 1 175, 93r2 hà nauka атаа. See also āda- ‘flour’, and ñada- ‘small’. Base ar- ' to grind’, pres. *ат-пй-  ürr-, *arnata- ürrda-, to Av. -arana- in yao- arana- ' grinding tool, pestle for grain', Zor.P. gloss yav- artük-arak ('lg), N.Pers. yávar, уйт; M.Parth.T. yw'rd'so ‘grain’, Zor.P. yav-artak ‘all grains’, from yava- ‘grain, barley’ and artā-ka- ‘ground’, Zor.P. artan (THNTWN), Baxtiüri ardan, Yazdi ōrotvūn, Gazi йтйе ‘һе grinds’, Pašto anal, participle Av. afa-, anaša-; Orm, ё1-, hal-, hinl- (*rnya-}, Iškāšmī yunuk, Sanglēčīi yūn-, Šuynt yān-:yūd, participle упуј, Yidya yan-, уйп-:уйруі-, yir-, yür-, Bartangt yex-: yét£, Yazg. yawn-:yug. Second com- ponent in the words for 'water-mill'! *Avata-üraka- 'self-grinding', Waxi xaBürg, Suyni xedárj Yazg. xwayérg, Yidya xirgoh, Yayn. xutanna, Parati xëra ‘mill’, xēra-gir ' mill-stone', and Caucasian lw Сеќеп heri. For ‘small’, Zor.P. xv-artak, Armen. lw xortak, N.Pers. хита, xurdah, Pašto wur, wür (*rta-, IIFL 2:273), see also below ñada- ‘small’ from *ni-arta- or *ui-rta-. From *àrüra- or *arÜra- ‘mill’ derives Maima'i är ‘mill’, N.Pers. às, asya, ахуйо, üsyüb, Zor.P. asyük, asyap ‘mill’, with N.Pers. asyd-sang ' mill-stone', Kurd. ai ‘п’. IE Pok. 28-9 al- ‘to grind’, O.Ind. atta- ‘flour’, no verbal forms (*alió-, see T. Burrow, ВЗОАЗ 35, 1972, 539), Greek Абэ Чо grind’, dAerov ‘mill’, &Acap ‘four’, Armen. alam ' to grind’, aliur, aleur ‘four’, alauri ' mill’,
886:ürgavemstine 'in a mortar, ш 86-9: maksina vasoa uysmä paheraüá, ürgavemitiüe naka küaid ‘with honey (BS mükgikà) clean clay is to be soaked, itis to be pounded in a grinding mortar’, The М8 is dislocated (72, not vā is correct). Here dyadic compound from ar- ‘to grind' and раї- ‘хо pound’, hence *arakaka-paiitina-; for pari- i pis-, note Av. pišant-, pistra- ' flour', Zor.P. pst *pist, N.Pers. pist, Buyni pist ‘mulberry flour’, Sarikoli past, Yazg. рай ‘broken’, Yidya puié 'apple-flour' Munjánt tüi- pušky ' mulberry-Bour'. IE Pok. 796 peis-, O.Ind. pes- ipis-, Greek тгтїстоз, Lat. pinsô, pisare, pistor, pisà ‘mortar’, Lit. paiiyti, O.Slav. piso ‘thrust’.
2398:бада ‘small’, Sid. rsvs hauvi jsa dilakä ñada ' with little, small strength’, BS kincid-vinasita-, 'Tib. mthu čun-zad £am-gyis ¿hun-no; comparative Sid. 19vi dilakai hauta ñadara 'his strength little, smaller’, gloss added to BS, Tib. mthu čhun-no. From *ni-arta- 'ground down' and hence ‘small’, to Zor.P. тік *xvartak, Armen. hw xortak, N.Pers, xurd, xurdah, Makrüni Вајо тї, Sibi Вајаёт hirt', from *hu-artaka-, beside Pašto wur, wór, gem. wura, plur. wa ‘small’, Parāčī yurök ‘small boy’ from *hu-rta- with lost h-. IE Pok. 28-9 al- ‘to grind’, Greek Лё, Armen. alam, above Khotan Saka
2399:ürr- and cognates. O.Ind. ajja- ‘ground swi’. For O.Ind. dnu-, dmivas- ‘small’, see -In-2 -n- (Т. Burrow, BSOAS 35, 1972, 543) and dipa- ‘small’ (against M. Mayrhofer, Dict.) For 'crush' and ‘small’, note aiso O.Ind. ksódati, kşudrd-. See ärr- ‘to grind’.
3210:see also І 167, S3r5 sirausi ‘contentment’ to sira- 'con- tent’, adjective JS гут sirosüdà ‘content’. If durausa is adjective *durauiya-, it connects with Av. düraosa-, Zor.P. dwl'ws *dür-ó£, O.Ind. duroga-, epithet of the sacred drink Ау. haoma-, Zor.P. hóm, O.Ind. sóma-. Veda usage is wider for durüsa-, durdgas-: RV 216 of the libationer domestic Agni fire (not Indra-), the ñdtar-, and S113 of beings who feel oppressed, brought low, being also an-äśġ- 'slow' and an-ugrd- ‘weak’. The three con- texts rust be suited. No agreed meaning has yet emerged. BSOAS зо, 1957, 53-8 listed earlier proposals, all based on compounds, but offered an interpretation by suffix -ausa- like the Khotan Saka -ñş- < -aufa- in parrügka- ' affliction, BS А/еќа-', Z 6:44 avarrüska- (old -й- < -au-) and later ranüska- ' scraped stuff! to base ran- (< rand-). The basic syllable dur- was thought to mean ' pierce, be pungent (of drink), be pained (of persons)’ with Baloéi dàr ' pain”, dóróx ‘il’ (-àx, -ök of permanent quality), so that durosa- of sóma- was the pungent drink called trgmá-, Hurd- ‘sharp’. After hesitating again over a compound of dur- е pungent’ with aus- 'burn, be pungent’ (for Iran. aus- ' to burn’ see s.v. byügàre ' they catch alight’) I prefer now a word dur- with suffix -ausa-, but from the base dau- ‘о press! either ‘ир’, ‘to elate, exhilarate’ ог ' down'!, ‘to depress, afflict' according to context (for dau- see s.v. dii). This dur- is then du- with -r- either verbal increment or nominal suffix beside *daura- in Baloé& dor, as kur- 'neck' in Av. kurit- 'neck-helmet! (see Donum H. S. Nyberg oblatum 1954, 7-12), Oss. D. Rurm, kurmd, I. kürm 'blind', beside *kaura- in Khotan Saka küra- 'bent', Zor.P., N.Pers. kr ‘blind’ апа O.Ind. kora- ‘joint’, Then Iran. *durausa-, O.Ind. durdsa- of the drink is ' exhilarant', but in RV 8:113 durósaso amanmahi ' we thought ourselves to be afflicted'. For a similar use of a base meaning to 'press' to show 'exhilaration', note fior- in Zor.P. fsar-, paffür-, paftir- ' press back", N.Pers. affurdan, affürdan ‘press’, affarah 'expressed juice’, Armen, lw sarak, Arab.-Pers. affara], beside Khotan Saka ssarr- 'to exhilarate’, assuda- dyadic with masta- 'exhilarated, intoxicated’ (base mad-), hasñda- ‘forced forth’ (*fra-fsrta-). With this O.Ind. psar-, parallel to mad-, can be placed (ВЗОАЗ 21, 1958, 543). In Yasna 32714. düraofom saocayat avā 1 see the meaning 'he made pungent the plant (avaA-) so that it was exhilarant'. For this sense of IE её, keuk-, note Vedic sukta- ' vinegar’, Khotan Saka sutta-, Pers. central dialect suta, Parāčī sīt 'sour' and Опа. éukrd- 'sour', Nüristüni "Waigali cukurà ' wine'.
3698:nühvarr- ‘desire, grasp at’, participle nähvarrda-, present stem, Manj. 147 nūhvarāre dharma vira 'they grasp at
3700:jsa "without desire of worship’, Manj. 170 se jsa nühua- rama dharma vira; 3 sing., Z 12793 hà ndhvarrde, ВЗ na virodhayati 'does not oppose' = 'greatly desires'; v 10274 nähvarrde, Tib. lhag-par chags-pa ' greatly desires’; V 93, 1774 maitti vara parruste vara baitti vara nihvarrde vara báysi(std) ' desires' (list of near synonyms); participle ш 49, 19-20 brriye jsa nihvarda ‘grasped by love’ (— BS rüga-), K. 113, 384 órriya jsa nühvarrvai (read: -dai); negative, K 53' 10-10 anihvarrdye, Manj, 317 anühvarrda, parallel to BS agrahya- ' ungraspable'. Base ni-hvar-n- with -rrda- from -rn-ta- (as ürr- 'to grind', ürrda-). Connexion uncertain, nähvarr- and buhurs- attest a base kuar- rather than huar- (see Zoroastrian Problems, ed. 2, 1971, xxvii-viii), since -Л- is found after -i-. Hence Ruar-:kur- in Greek kup- (к©роз, корса) ‘push against, obtain’, as Pindaros, Pythian 1 99 ёукурот) кої EAg *finds and takes', with Oss. D. А' üdrun, k'udrt, Т. Айгул, k'ürd 'push against, strike’, D. dnxuársun, I. dxxürsyn tidem’ (k'uär- < skuar-, хийт- < khuar-).
7496:-ştarr- ‘strew, spread’, see bastarr-, pastarda-.
```


## [2026-09-04T19:31:19.786Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5395,5410p' WEB_vol1.txt; echo \"=== MON ard ===\"; grep -n \"آرد\" MON_part1.txt | head -5; grep -c \"آرد\" MON_part1.txt 2>/dev/null; echo \"=== MON adena ===\"; grep -n \"ârt\\|ārt\" incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -10"
}
```


### [2026-09-04T19:31:19.902Z] TOOL RESULT

```
Alexandrine
erta, watch, f. of erlo, raised aloft ergere, from L. erigere, to raise.] ‘ y arepe guant ready. . brisk; nimble; moving with pro ya Syn.—active, brisk, lively, vigilant, wane _ ful, wide-awake, prompt, ready, biel a-lért, n, 1. a period of vigilance: used pri cipally in the phrase on the alert; as, the wate stood on the alert, PSA 2. an alarm; notice to stand in readines _ as for an air raid. S3 å-lērt’, v.l. to issue an alarm to; to warn, a . ror G arredi as, toe a city. eS a-lért/ly, adv. in an alert manner; pr Aan UA n. briskness; abiere SAA iness, -a’lēs, [L., pl. of -alis.] a suffix used in forming the scientific Latin names of orders of plante ale’tast-ér, n. formerly, an officer appointed and sworn to inspect ale, beer, and bread sold _ within a district; aleconner. a-lé-thi-ol/6-gy, n. [Gr. alétheia, truth, and logos, discourse.] the science or doctrine of truth; the branch of logic that deals with truth, a-leth’6-scdpe, n. (Gr. aléthés, true, and skopein, to view,] an instrument for viewing pictures, producing a stereoscopic effect. Al’e-tris, 2. [L., from Gr. aletris, a grinder of corn, from alelreuein; alein, to grind.] a genus of plants of the lily family. a-lette’ (a-let’), n. [dim. of L. ala, a wing.] the face of the pier of an arch, extending along the edge of the opening; especially, that por- tion between the edge of the opening and the pillar or pilaster used to decorate the arch.
Pp. of
ALETTE A,arch BB, pillars CC, aleties
Al-eu-ri/tés, n. [L., from Gr. aleurités, per- taining to aleuron, meal, from alein, to grind.] a genus of cactuslike plants, including the candleberry tree. s
a-lei’/rd-man.-cy, n. (Gr. aleuromanteion, divi- nation by meal; aleuron, meal, and mantera, divination.] a kind of divination by flour or meal.
al-eu-rom/e-tér, n. [Gr. aleuron, meal, and melron, measure.] an instrument for testing the quality of gluten in flour.
à-leū’rö- nat, n. flour made of aleurone. 3
àleū’röne, n. a protein substance found in small granules in ripening seeds, and forming an outer layer in cereals, :
al-et-ron/ic, a. pertaining to or resembling aleurone. x
AVe-ut, n.; pl. AV@-uts, Aut, 1. a native of the Aleutian Islands and part of Alaska.
2. the language of these natives.
A-leu/tian, a. 1. of the Aleutian Islands.
2. of the Aleuts, their culture, etc.
A-leii/tian, 2. an Aleut.
al’e-vin, n. [Fr. alevin; OFr. alever; L. adlevare, to raise.] a young fish of any kind; especially a young salmon.
=== MON ard ===
1331:شیرینی که از آرد سفید و روغن و قند 
1668:طعامی که شنک آرد. (گیا.) لوله‌هایی در 
2646:آرد؛ 0 (.) نرمه و آس کردةً حیوت) 
2651:بدست آید. آرد گندم؛ آرد جو آرد برنج. 
2652:آرد: ۵ (- آراد] (4) روز پیست و پنجم 
92
=== MON adena ===
```


## [2026-09-04T19:31:22.837Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2640,2660p' MON_part1.txt"
}
```


### [2026-09-04T19:31:22.883Z] TOOL RESULT

```
از شنت ۱ (ص. ۰.) کسی که در 
رشته‌ای از هنرهای زیبا مانند موسیقی» تأتر 
سینماء نقاشی و مانند آن ماهر باشد» هنرمند. 
کسی که در صحنة تأتر» سینما و تلویزیون 
نقشی ایفا کنند» آکتور) هنر يشه. 

آرد؛ 0 (.) نرمه و آس کردةً حیوت) 


آرامگاه 
گردی که از کوبیدن با آسیا کردن غلات 
بدست آید. آرد گندم؛ آرد جو آرد برنج. 
آرد: ۵ (- آراد] (4) روز پیست و پنجم 
از هر ماه شمسی. ضصح.- صحیح «ارد» است. 
اردپیز: 2.012 (افا. امر.) غربال» غربیل. 
اردل: 01 [- اردل ] (ا.) فراشی که مأمور 
فرا خواندن و احضار سپاهیان یا متهمان و 
گناه کاران است؛ اردل. آردل بی‌جوب: 
(کد.) ادرار؛ بول که عرصه رابر شخص 
تنگک کند.
```


## [2026-09-04T19:31:31.016Z] TOOL CALL #46: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T19:31:31.023Z] TOOL RESULT

```


```


## [2026-09-04T19:31:34.759Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%AF",
 "prompt": "Give the full Persian etymology section for آرد (ârd) \"flour\": the Middle Persian form, the Proto-Iranian/Proto-Indo-Iranian/PIE reconstructions, and any cognates listed (Avestan, Sogdian, Khotanese, Greek, Armenian)."
}
```


## [2026-09-04T19:31:36.699Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%84%CE%BB%CE%B5%CF%85%CF%81%CE%BF%CE%BD",
 "prompt": "Give the etymology of ἄλευρον: the verb it derives from, the PIE root reconstruction, cognates, and any English derivatives mentioned."
}
```


### [2026-09-04T19:31:42.304Z] TOOL RESULT

```
# Persian Etymology for آرد (ārd) "Flour"

**Middle Persian Form:** [Book Pahlavi needed] (KHMA /⁠ārd⁠/, "flour")

**Proto-Language Reconstructions:**
- Proto-Iranian: *Hr̥Htáh ("ground up")
- Proto-Indo-Iranian: *Hr̥Htás ("ground up")
- Proto-Indo-European: *h₂l̥h₁-tós ("to grind")

**Cognates Listed:**
The entry identifies related words across several ancient and modern languages:

- Avestan: 𐬀𐬴𐬀 (aṣ̌a, "ground")
- Hindi: आटा (āṭā, "flour")
- Old Armenian: աղամ (ałam, "to grind")
- Ancient Greek: ἀλέω (aléō, "to grind")

This etymology demonstrates "a chain of linguistic descent from Proto-Indo-European through Iranian branches into Persian."
```


### [2026-09-04T19:31:43.484Z] TOOL RESULT

```
# Etymology of ἄλευρον

**Related Verb:** The word derives from the Ancient Greek verb [ἀλέω](/wiki/%E1%BC%80%CE%BB%CE%AD%CF%89#Ancient_Greek "ἀλέω") (ăléō), listed under Related terms.

**PIE Root:** The term originates "From Proto-Indo-European *h₂léh₁wr̥," according to the etymological section.

**Cognates:** Old Armenian អលեւր (alewr) is identified as a cognate word sharing the same ancient origin.

**English Derivatives:** The entry indicates the word descended into English as **aleurone**, a scientific term referring to a protein-rich layer in grain seeds. French and Italian also borrowed this term, maintaining the form **aleurone**.
```


## [2026-09-04T19:31:49.272Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hr%CC%A5Ht%C3%A1h",
 "prompt": "Give the full reconstruction entry: meaning, PIE ancestor, and the list of descendants (Avestan, Middle Persian, Persian, Sogdian, Khotanese, Ossetian, Yaghnobi, Pashto etc.)."
}
```


## [2026-09-04T19:31:49.553Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/aleurone",
 "prompt": "Give the etymology of aleurone: date of coinage, Greek source word and its meaning, and the PIE root cited."
}
```


### [2026-09-04T19:31:54.125Z] TOOL RESULT

```
I apologize, but the web page content provided does not contain any information about the etymology of "aleurone." The page shows only the header, navigation menu, and footer of the Etymonline website—it does not include any dictionary entry or etymological data for specific words.

To find the etymology of "aleurone," you would need to search the Etymonline website directly using their search function.
```


### [2026-09-04T19:31:55.702Z] TOOL RESULT

```
# Proto-Iranian *Hr̥Htáh

## Meaning
This reconstructed term functions as an adjective with two related senses: "ground up" and "flour."

## PIE Ancestor
The word derives from Proto-Indo-European *h₂l̥h₁-tós, itself from the root *h₂elh₁- meaning "to grind."

## Descendants
The term evolved across multiple Iranian language branches:

**Central Iranian:** Younger Avestan 𐬀𐬴𐬀 (aṣ̌a)

**Northeastern Iranian:** Khotanese āḍa; Sogdian ārt(ē); Bactrian ardo; Khwarezmian ard; Yaghnobi arta

**Southeastern Iranian:** Pashto oṛə ("flour")

**Northwestern Iranian:** Baluchi ārt; Kurdish ar/ard; Gilaki ārdə; Mazanderani ārd/ārt; Zazaki ardi/ard

**Southwestern Iranian:** Middle Persian ārd; Persian آرد (ārd); Tajik ord; Bakhtiari ard ("flour")

The descendants demonstrate consistent phonetic evolution across geographic and temporal divisions of the Iranian language family.
```


## [2026-09-04T19:32:06.657Z] TOOL CALL #51: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%AF' --note 'pdf page 46, root Al 2, node #2: Persian ârd \"flour\" etymology (MP ārd, PIr *Hr̥Htáh, PIE *h₂l̥h₁-tós)' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hr%CC%A5Ht%C3%A1h' --note 'pdf page 46, root Al 2, nodes #1/#2/#3: Proto-Iranian *Hr̥Htáh \"ground up, flour\" with descendants Av. aṣ̌a, Sogdian ārt(ē), MP/NP ārd' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E1%BC%84%CE%BB%CE%B5%CF%85%CF%81%CE%BF%CE%BD' --note 'pdf page 46, root Al 2, nodes #4/#5: Greek ἄλευρον \"wheat flour\" < *h₂léh₁wr̥, English derivative aleurone' 2>&1 | tail -3"
}
```


### [2026-09-04T19:32:08.998Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b1ad5eecce3e7550.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f64f7e4e37e5f4c8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/72cc1e4f4587dc79.txt
```


## [2026-09-04T19:32:14.243Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82elh%E2%82%81-",
 "prompt": "Give the root's meaning, the derived terms/reconstructions, and the descendants by branch (Hellenic, Armenian, Indo-Iranian)."
}
```


## [2026-09-04T19:32:17.281Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%80%CE%BB%CE%AD%CF%89",
 "prompt": "Ancient Greek ἀλέω: meaning, etymology (PIE root), principal parts, and whether the infinitive is ἀλεῖν. Also any note about Beekes or the reconstruction."
}
```


### [2026-09-04T19:32:20.211Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂elh₁-

**Root Meaning:**
The reconstructed root means "to grind."

**Derived Terms/Reconstructions:**
- *h₂élh₁-ti ~ h₂l̥h₁-énti (athematic root present)
- *h₂l̥-né-h₁-ti ~ h₂l̥-n-h₁-énti (nasal-infix present)
- *h₂léh₁-wr̥
- *h₂l̥h₁-tós
- *h₂elh₁-won-

**Descendants by Branch:**

**Hellenic:**
Ancient Greek: ἀλέω (aléō)

**Armenian:**
Old Armenian: աղամ (ałam)

**Indo-Iranian:**
Proto-Indo-Iranian: *Hr̥náHti, which evolved into Proto-Iranian forms. Additionally, *Hr̥Htás appears in Proto-Indo-Iranian with further documented descendants.

**Tocharian:**
Tocharian B: alāᵤ ("wether" - a castrated ram)
```


### [2026-09-04T19:32:23.462Z] TOOL RESULT

```
# Ancient Greek ἀλέω

**Meaning:** The verb means "to grind; to bruise; to pound; to mill" and is classified as transitive.

**Etymology:** The word derives from Proto-Indo-European *h₂elh₁- ("to grind"). It shares cognates across Indo-European languages, including Old Armenian ałam, Sanskrit ārtá (flour), Avestan aṣ̌a (ground), and Persian ārd (flour).

**Principal Parts:** The entry shows extensive conjugation tables for both contracted and uncontracted forms across multiple tenses (present, imperfect, aorist, and perfect), with variations for different Greek dialects including Attic, Epic, Ionic, and Koine Greek.

**Infinitive Form:** Yes, the infinitive is ἀλεῖν (contracted form) or ἀλέειν (uncontracted form).

**Additional Notes:** The Wiktionary entry does not reference Beekes or provide etymological commentary beyond the basic PIE reconstruction and cognate listings.
```


## [2026-09-04T19:32:29.245Z] TOOL CALL #54: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82elh%E2%82%81-' --note 'pdf page 46, root Al 2 (= Pokorny 5. al- p.28): PIE *h₂elh₁- \"to grind\", derived stems *h₂léh₁-wr̥ and *h₂l̥h₁-tós' 2>&1 | tail -2\ncd /home/sfmqrb/git/rishe && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E1%BC%80%CE%BB%CE%AD%CF%89' --note 'pdf page 46, root Al 2, node #4: Greek ἀλέω \"to grind\", infinitive ἀλεῖν (= Nourai alein)' 2>&1 | tail -2"
}
```


### [2026-09-04T19:32:32.700Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/479a61f7af960f99.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c70a3a2805f5ef9b.txt
```


## [2026-09-04T19:32:42.522Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ard headword ===\"; grep -n \"^ *[0-9]*\\. *ard\\|ärd\\|ard \" HUB.txt | head -10; echo \"=== NYB 'lt / THNN ===\"; grep -n \"THNN\\|'lt'\\|ārt\\|art'\" NYB_vol2_glossary.txt | head -10; echo \"=== IEC alew/aleu ===\"; grep -n -i \"aleuron\\|alew\\|‘to grind’\\|'to grind'\" IEC.txt | head -15"
}
```


### [2026-09-04T19:32:42.601Z] TOOL RESULT

```
=== HUB ard headword ===
991:224. Np. biSgard und bisgar *Jagd* ist mit Riicksicht
992:auf sikardan jagen' in bi-sgard zu zerlegen und auf
1788:hinzu : np. card pastio', afgh. car pasture*. Dagegen
2415:656. N6ldeke hat Recht, np. zard gelb = ap. ^zarta-
2481:^zarta- und *zartaka- im Neup. zu zard und zarda
2483:zard gelb', zarda *6alle' (bal. LW. zard gelb*, zardd
3242:902. Np. gard *Staub* = phi. vart ^Staub', Yfitk. i. Zar. 68,
3304:gard (so schon Vullers, Radices) abgeleitet werden.
3570:textes du Mainyo-i-Khard p. 11, Mann, ZDMG. 47,
4216:45); sdgird *Schuler = paz. asdgard Min. Gl. 17, arm.
=== NYB 'lt / THNN ===
727:2aš [^5] the independent form of the cas. obl. 3d p. sg. = enel. -$ (g. v.); always preceding the w. to which it belongs; used 1. anaphorically in the interior of a sentence after a part of the sentence which has been placed first for emphasis: andar han Zartuxst | aš hac miyān Gp i hömikän burt || u pat uléh Zartuxšt | aš han i dašn paitištān hac Osan rote burt 5615-1? (Markwart's reading, Cat. 114 n. 1, is a failure); õi (pron.) mar | aš 6 pasčh gàv apāc rānēnīt 485; — not anaphorically: Ot (prep.) fravahr + Zartuxst | aš (viz. the snake) zafar frac zat 4012-13; purr-x"arrahéh i ax" à astómand | aš hac tan xYarrah from his (viz. Zartuxšt's) bodily splendour 377-8; — taking up an encl. -§ at the beginning of the sentence, after a part of the sen- tence which carries a lengthy attribute: api-š hamäk damik i-š apar rāh bit | aš *perävanihit kart 3316-17; — after an ad- verbial phrase beginning the sentence: adak apar pat jamän | aš hanjamanénit mūtak :61° (where aš anticipates mūtak, cf. s. v. -š). — 2. to introduce the apo- dosis (as api-$, adak-i8): after kakar 31?! ; after ka 327. 3319. 341. 565. 5717. 924. after a relative clause 3219, 9824, 100?7— 101?. — Probably identical with MPrthPrs š, written as an independent w. with two dots above (another explanation of this § v. A-H III, Gloss s. v.; ? in a fragmentary context [S] is obscure). Cf am, at, atün, asän.
1004:rarudenc; patron. Prth 1. 28 = Prs 1. 24 bythškn, Gr. v. rırıdıyav; Paikuli = KZS. Arm. lw. bdeašx (Hübschmann, AG 119 sg.). Georg: Armazi bilinguis (Nyberg, Eranos 44, 1946, 228-243; 233 sqq.) bthš, Gr v. nırıadEng also on gems found there (l.c.; v. also Eränsahr 169), Armazi “Aram.” inscr. (Altheim & Stiel, FuF 35, 1961, 172-178) pyihš; native K art'veli patiaxsi, pitiaxši (Hübschmann, Tschen- keli). Syr. lw. ptahšā, ptakša (often faultily vocalized), aftakšā (Hoffmann, Auszüge p. 34 n. 275). Amm. Marc. XXIII, 6: 14 vitaxae (“id est magistri equitum"), Gr. Hesych. Btorač, read Birač. In dealing with its etymology the indigenous form bythš should; as a matter of course, be given preference before any deviating forms in foreign languages. In its oldest form it is, however, found in Arm bdea&r < *bdiaxs: -d- must be secondary (an original d would have given 7) and go back to a f, voiced because of its proximity to the preceding b, which consequently must be the original initial consonant, not p (pt- would have re- mained); this phonetic state is cogently conclusive in favour of an original form "bitiyaxši-. The first element is *bitīya- ‘the second’, NW form of "dvitiya; Av. (963 sg.) bitya-, MPrth. bdyg (Nyberg, l. e. 237 n. 2; Henning, Iranistik 62 n. 2); the second element has been explained by Pagliaro (RSO XII, 1929, 164 sqq.) as *axsi- ‘eye’ (in Av. derivatives, v. also apaxš); *bītīya-axši- ‘the second eye’ of the King, based on the idea, well attested by the classical authors. and well ana- lysed by P., of the King’s officials as his “eyes”. Thus any etymology starting from initial ptt- is peremptorily excluded; pit- for bit- must be due to a secondary development in the borrowing languages. Pagliaro, l.c. 160-168; Eilers IIJ V, 1962, 209 sq. (quotes Armazi pythé, but ignores bihš!); Benveniste, Titres 65; Rundgren, OrSu XII (1963), 1964, 89-98 (oh!); ete.
1705:g0(v)-vieär [gwwe’l] explicit, lucid 8021-25, — gov- from guftan, vicar from vtcārtan (g. v.): "word-explaining'. Paz. gaoguzdr, góguzür, gövazär ete., Skr. v. vibhakta (Mx), suvyakta (ŠGV).
2230:kārt [k’lt'; SKYN?] knife 2220.25, 9621, — Av. (454) !karota-; NP kārd.
3131:pēš [pyš; L'YN!, inser. and Ps. L'YNY] l. adv. before, earlier 97°; first, opp. pas, in a sequence 5718; ~ hac before: 912, 1274, 382, 392, 493, 652°, with a v. n. or an inf. instead of a temporal clause 4618, 5423; ~ ki 81. 1317, ~ hac han-tčit [ZK *D] ka 98% conj. before; dvārtšn 6 ~ to run forwards, opp. dvarišn 6 pas to run backwards 6811; 6 ~ + dar, matan, Sutan, z"àstan, v. these ws.; 6 ~ raft, tacit went, ran ahead, to the front 4918.19; ēn 4 6 — góbam what I am going to say presently 517-8. 541%, — 2. prep. before, regularly followed by the izafat: 7 sül peš <i>» hàn 7 years earlier 40°; þe- fore, in the presence of 23-15, 521, 7021, 9876; for the protection of 49%; without "the izafat HajB:5; 269; referring back to an encl. pron.: api-š Tos — ēstēt and T. will stand before him 1004; — with vbs. of motion, addressing etc., often 6 m: 619, 1015, 1] 15-19, 1316.23, 1510-11, ete, — ~ n&mak, hac ~ némak, v. nēmak; as first element of compounds, v. below. — OP prep. c. acc. patšiyā ‘before’ Beh. IV, 91, according to the last revision of the
3627:310 šāyīt [š?dyt'], cond. 3d p. sg. (nē) &ayit hat 711%, to be able, capable, 1. with a pers. subj.: kad šāyem griftan? when shall we be able to catch him? 75; 8?;-4 martömän šāyēnd ayāftan 887-9; Sūšāns apāk Kai-Xösröi kartan šāyēnd. 8820-22; 908; — 2. with a non-pers. subj.: amäh garān ziyän ... haciš šāyet butan serious harm must necessarily arise for us: from it 191-?; ctš-ē ke ziyān ne haciš Sayist bütan from which no harm could arise 411-12; kū ātaxš haciš nē šāyet vextan that is: the fire cannot break forth from it 95! (gl.); — 2. impers.: it is possible, in varying modal senses: it can, may, might (be), it is proper, suitable, fitting, permis- sible; ‘perhaps it will... .’; it is predestin- ed, necessary, must, ought to, should, passim; the difference between šāyet and tuvan may be illustrated by 719-3; hakar tài 3 rēc griftan ne šāyet, pas hac hin griftam ne tuvdn if he cannot be caught within three days it will be im- possible to catch him; sdéyet ku perhaps 81. 242; ma hakar-am ... nē brihénit estet ku Erän-sahr pat ēv-xvatāyēh be šāyēt vīnā- ristan it is perhaps not predestined for me that I should bring E. together into one kingdom 137-9; šāyet butan ka šāyet butan “it is predestinated to happen when it is predestinated to happen”, it must happen when it must, Fate will necessarily be accomplished 231-? (cf Skr yad bhavisyati tad bhavisyati); kū yam etön névak pat xuatäyeh šāyet kartan that is: so beautiful & bowl must be made for royal persons 6015 (gl.); ānēd x"arisn šāyet x"artan it is permitted to take food here 76%, v. s. v. frayist ; tài Emahčip x"artan ne šāyet during one whole month it was not possible to drink of the water 2017; — if the real subj. is a person the pret. šāytst has regularly impers. construction: asvārān ... hixtan nē šāyist the equestrians could not haul up 153-4 (cf 887-8, above sub 1); ke (indir. obj.) cim 4 han catrang vicārtan šāyist anyone who could solve the problem of this game of chess 11817-18; without
3818:tuvän [twb?n'] 1. adj. mighty, powerful, energetic 559. 6619; subst. what one is able to do, v. s. v. sämänihä. — 2. impers. vb.: it is possible, one can, is able to; the subj. is an encl. pron., or a subst. in the cas. obl., or a form felt as a cas. obl.; construed with an inf., which is generally placed before, less often after ~; pret. ~ būt; a) without a subj.: 6 x¥és kartan nem 9?" ; griftan ne" (ef s. v. Säyistan) ete.; — b) with a logical subj.: man zatan nē ~ I cannot slay him 99%; man zivistan ne ~ 1035-5; api-tan griftan ne ~ 7%; ete.; ka-tan ~ when it will be possible for you 911; šmah xvēš rād ne ~ x"astan 452-3, v. axtäyisneh; aš pād i man... apar daštan ne ~ büt he was not able to „.. 3318-19. 48-8 2-5 vicārtan nē ~ 11912; cand-šan ~ dätan as much as they pos- sibly can 79%; apäc daštan ke ~? 247; martömän ... ayaftan u dānistan ne ~ mankind cannot ... 804-5; 10926-??; duš- man pat dušman hin nē ~ kartani... 414-15, 619-20. Pēc kas vicārtan ne ~ būt 11921. — From Av. (638 sg.) tav-; MPrs twn; Ps. twb?n-; Paz. tuq, tva; NP tuvān, tavān; cf tāyītan and tahé-kar.
4118:vieiirišn [we'lšn'] v. n. 1. as a pred.: has to decide, will decide (the case) 19??. — 2. explanation 118!; 1214. — NP guzārtš. From
4242:vitirtan [wt'ltn'] 1. caus. of vitartan, to cause to pass: dātār han i Zartuxst zx'"arrah tar mätist ārak 6 Zartuxst vitārt the Creator sent Z.’s x“arrah (g. v.) down
4324:1xuar [hw?l] easy, agreeable 10124. — < avāhr, q. v. Cf MPrs n. pr. rwsn?n zw’ryst ‘the most blessed of the Lights’ (A-H I); v. also x%direh and avārthā.
=== IEC alew/aleu ===
```


## [2026-09-04T19:32:44.304Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD loose ===\"; for f in FSD_vol1.txt; do grep -n -i \"aleuro\\|aleurone\\|al-eu\" $f | head -5; done; echo \"=== FSD grep 'aleu' all vols\"; grep -l -i \"aleu\" FSD_vol*.txt; echo \"=== KLN leaf 36 head ===\"; python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[36][:300])\""
}
```


### [2026-09-04T19:32:45.837Z] TOOL RESULT

```
=== FSD loose ===
=== FSD grep 'aleu' all vols
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
FSD_vol1.txt
=== KLN leaf 36 head ===
trength,  power’.  See  Alexander, alcohol,  n.  —  ML.,  fr.  Arab,  al-kohl ,  vulgar  pro¬ nunciation  of  al-kuhl,  fr.  a/-,  the  ,  and  kohl, resp.  kuhl,  ‘antimony  (used  for  painting  the  eye¬ lids)’,  which  is  rel.  to  Heb.  kahal  (Ezek.  23.40), ‘he  painted  the  eyelids  with
```


## [2026-09-04T19:32:54.488Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"WP I, 89\" IEC.txt | head -10; echo \"---\"; grep -n -i \"‘grind’\\|'grind'\\|to grind\" IEC.txt | head -20"
}
```


### [2026-09-04T19:32:54.560Z] TOOL RESULT

```
408:alalos, à ‘babble, hubbub; obstreperous’. WP I, 89 Skt. alalah; Arm. dim. ayayak; Gk. alalë; Li. cf. alasas
424:aleks-, alks- "ward off, protect. WP I, 89. Cf. alkos Skt. raksami; Arm. ayxem ‘bolt, bar; Myc. & Gk. aléxo, alexéo
---
422:aleio “grind, pound, crush'. Cf. aleuro- Hind.Beng. cf. ata, Guj. ato, Romani arno, andro, aro; Per. ard (ambig. “flour”, perhaps to Gk. ártos “bread”. Bois. and Hof. uncertain); Arm. ayam ‘grind’; Gk. aléo, v., aletós, s. Cf. Myc. (queried) aletere-, pl. *millers'
5528:guhremdho, ið (guhrendh-) ‘roar, groan, bark, bellow’. (Isophonic with guhrendh- ‘gnaw, gnash? q. v.). Cf. ghrem- (1) & gurem- Lat. frendo, ére, and frendeo, ere (2) ‘groan’. (From fremo via fremidus by syncope to *frendus'. Ainsworth, 1736); MHG grinden (2) ‘bellow, bark’; E dial. to grind ‘to whine’; cf. Latv. gremzt (2) ‘roar’
6222:cf. khés-imon “self-easement'; pés-imon “act of falling'; pega-imós 'act of departure'; Alb. het-im (inquiry): Li. skait-ymas reading); Ir. maoidh-eamh, gs -imh ‘telling’; áir-eamh, gs -imh ‘counting’; OCS pisimo “letter, writing; jarímü (fyoke', cf. Pol. ko-jarzyé "mont: Li. pie3-imas, ar-imas, grub-imas, &j-imas *design- ing, plowing, roughening, going’ beside grüd- ymas ‘hardening’; sür-ymas ‘saltwater’, etc. -inā, a generalizing extn. See next Gk. khoir-inë (‘musseľ: khoiros); dotiné (Hes: dos); (melíné ‘millet? in relation to *mel- ‘grind’, q. v. may belong here); Alb. lug- inë ((valley': lug 'trough); rreth-inë ('sur- roundings': rreth 'circle"); Lat. farina (:far); rüpina (:rüpes); haed-ina ('goatsflesh': hae- dus); OS cf. stulina ‘stealing’; lugina ‘lying’; OCS ozina ('anguish': ozükü, cf. Lat. angina); globina (‘depth’: globokü); dolina ('valley': dolü *ditch"). A variant occurs in Li. avíena “mutton”, cf. LLat. ovina, id. As an indicator of a female with a male counterpart, cf. Gk. héroiné (*heroine": héros); Lat. reg-ina (:rex); MHG cf. vühsinne (vixen': vuhs). A truncat- ed formula occurs in Go. managei, obl. -ein- ‘multitude’ and OHG hohi, obl. -1n-. See next -Inos, om (-Inios, om), an adjectival formant > a noun-derivative. Skt. a$v-in (:Lat. equinus); Av. peronin *wing- ed'; hámin- ‘summer’; Per. Sirin (sweet: Sir *milk); éübin (^wooden': éüb); pūstīn (‘fur coat: pūst "pelt: Oss. zàr-in ( golden": zàr); Arm. verf-in (final: verð); het-in, id. (fr. *en-pedinos, cf. Li. j-pedin “close behind”; Í-pédinis *successor"); Gk. pheg-inós (*oaken": phégós, cf. Lat. fàgínus of beech’); earinós (‘of spring": éar, cf. Lat. vernus); Lat. marinus, fibr-inus beside nüc-Ínus, màter-nus, ver-nus, etc.; W derw- in, lledr-in, hef-in ('oaken, leath- ern, summer: derw, lledr, haf); Go. fill-eins (‘of skin": fill, cf. Lat. pell-inus); fadr-ein (“pa- ternity, cf. Lat. paternus); OHG bibir-in, fuhs-in; MHG buech-in; ON gull-inn, OE medr-en, etc. “of beaver, fox, beech, gold, mother’; OCS materinü, materiní ‘maternal’; sestrinü, sestrini ‘sisterly’; krův-ínů (“of blood': krúvi, cf. Li. krùvinas ‘bloody’:kraŭjas “blood”). The variant -inios, where it occurs,
10289:málo, io (variant of type mlo, io ‘grind, mill. Cf. also melo, io, id.) Hitt. mallahhi, malliski(mi), v. id.; Umb. mal-, pp: maletu, id.; Per. (ambig.) mālam, id.; Tokh. A malyw-, maly-, B mely-, mäll- ‘crush’; W malu, Br. mala, Cor. mala, pp: melys ‘grind’; Go. OHG malan, id.; ON mala, beside mólva, id.; OCs moljo, iti & Li. malü, málti, Latv. ma]u, malt, id. are of ambig. vocalism (*-À- or *-o-)
10737:(mol- ‘grind’, etc. see mel-, mál-)
10901:grind; Osc. cf. maletu, adj. ‘pulverized, ground’; W malu, Br. mala, Cor. mala, pp: melys ‘grind’; Go. malan, sv. 6, OHG malan, MHG malin & malen, ON mala ‘gring’ beside melja, p.t. malda ‘crush’; OCS moljo, moliti, id.; R molót, inf. id.; Cz. cf. vý-mol ‘milling; Li. malü, málti ‘grind’ beside mole, f. (*erind- ing, < *mal-: MHG muol, pt ON mól, id.); Latv. malu, malt, as Li. Cf. also Du. mul, m. “dust, peatbed'; G Müll, id.; ON moli, n. “fragment; fragments’; molna, intr. ‘crumble’; OE myl.
11377:mulio (1) ‘grind, crush'. Cf. mulos, mio (Arm. variant *mulo). WP II, 285 Arm. myem, v. “press, force? beside myum, id. (fr. *mulümi); Gk. müllo, v. ‘grind’; W (am- big.) cf. mwl, m. ‘chaff from threshing’; OHG muldlen, v. ‘crush, mill’; Icel. mylja, v. ‘crush, pulverise'. Cf. mulos
12933:pisimnos, à ‘ground, pounded, small. Cf. pisio, pistos, etc. Skt. Av. pi&-, v. root ‘grind’; Gk. cf. ptisáne, f. (“pearl barley, barley-gruel, fr. *d-pision-); LLat. pisinnus, adj. ‘tiny’; G Fesen, Vesen, m. ‘spelt; grain-husk'; R pšenò, n. ‘millet; Slo- vene ‘groats’; OPr. cf. som-pisinis (‘coarse bread": Skt. sam-piš-); Skt. cf. pista-pesanah, m. ‘flour, meal
```


## [2026-09-04T19:33:01.155Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '418,428p' IEC.txt"
}
```


### [2026-09-04T19:33:01.203Z] TOOL RESULT

```
‘barley’; Lat. cf. albi-tüdo; Ir. ailbh ‘flock’; W cf. elfed ‘autumn’; Gmc. cf. Alpes (CAlps' — *white mountains' accdg. to Fest. Alemannic p for general Gmc. b)
albhos ‘white’. WP I, 92. Cf. albhis Hitt. alpas (cloud; Gk. alphós; Lat. albus; Umb. alf-; Gaul. albo-; Ir. cf. ailbh ‘flock
aldh-(?) (Most of the evidence is ambigu- ous. For Gk. *álthomai, althaino, álthos — omitted by Bois. and Hof. — see uldh-; íor Holth. the Gk. forms equate with ON aldinn, aldin ‘fruit’. Cf. also uoldh-)
ale$-(?), al$-(?) “sorrow, suffering’. Cf. WP I, 160; II, 423 note. Cf. alg-, sulg-. Oss. älğ (ambig.) “nausea”. (For speculations see Bois: alégo, etc., and WH & EM: neg- ligo, diligo)
aleio “grind, pound, crush'. Cf. aleuro- Hind.Beng. cf. ata, Guj. ato, Romani arno, andro, aro; Per. ard (ambig. “flour”, perhaps to Gk. ártos “bread”. Bois. and Hof. uncertain); Arm. ayam ‘grind’; Gk. aléo, v., aletós, s. Cf. Myc. (queried) aletere-, pl. *millers'
áleið, al- ‘rove, roam’. Cf. aleuos Per. cf. àv-ara, cpd. adj. ‘wandering’; Gk. &lásko, elaíno (Dor.-à-), beside áláomai; Lat. cf. the synthetic cpd. (apparently with an aph- etic px.) p-àlor, palari ‘wander’. Cf. for the px. pono, positum; pars: ars; parco: arx; pudeo (for *po-uideo “look down (?), w. the semantics of R po-zor); Latv. aleties *be rest- less
aleks-, alks- "ward off, protect. WP I, 89. Cf. alkos Skt. raksami; Arm. ayxem ‘bolt, bar; Myc. & Gk. aléxo, alexéo
aleur- (aleuor-) *millings, flour. Cf. aleió Arm. aliwr, aler, -erb; Gk. áleuron, áleiar
aleuos ‘wandering, restless, raving’. Cf. áleið Per. cf. av-ara ‘wandering’; Gk. eleós; Latv. alava ‘restless cow’. (For OCS jalovü "bar. ren’, see iel- in Suppt.)
alonis, see elonis
aleuos "dark: dark substance’. PW I, 159; II, 386; II, 442. Cf. elouos, olouos Hitt. cf. halluwas "deen": Gk. alaós "dark blind, dead": OHG cf. ëlo, gs. élawes ‘yellow’; OCS (ambig.) olovo “lead — metal’; Li. álvas,
```


## [2026-09-04T19:33:11.807Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.merriam-webster.com/dictionary/aleurone",
 "prompt": "What is the definition, etymology, and first known use date of \"aleurone\"?"
}
```


### [2026-09-04T19:33:13.566Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T19:33:16.147Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/aleurone",
 "prompt": "Etymology of English aleurone: source language, coiner if given, date, and meaning."
}
```


### [2026-09-04T19:33:20.159Z] TOOL RESULT

```
# Etymology of Aleurone

Based on the Wiktionary entry, here are the etymological details:

**Source Language:** Ancient Greek

**Date:** 1865/70

**Original Term:** ἄλευρον (áleuron)

**Meaning:** The etymology states the word comes from Ancient Greek meaning "flour, meal." The English term *aleurone* emerged in the late 19th century, adopting this classical root to describe the protein-containing particles found in cereal grains—a scientific term that drew its name from the flour-like appearance of these microscopic structures.
```


## [2026-09-04T19:33:32.420Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[163]\ni=p.find('gemahlen')\nprint(p[max(0,i-600):i+300])\nEOF"
}
```


### [2026-09-04T19:33:34.137Z] TOOL RESULT

```
  466.   OberEctioiie
«Wer  'aia-  Anbang  lu  U  und  lU  mit  No,  16.
KooipA.  — S.  auch  rtaalar- aiair  vaAii/aÄe  als
EN.    —    Pü.:    airäia,  vx  H.  /.  J  erL:    an  i
aitm  vohü;  i.  noch  slav-  mit  No.  6,  —  1)  Nach
dem  eisten  Wort  des  Gebett.  —  ■)  Mit  Heran-
ziebung  des   zweiten  oder  dritten  Worts;    s.
No.   I.
•  j.  3a&i-  in.  'Achsel':  'ifayh  (GD.)  F.^g.
VgL  1«,  axilla,  ahd.  ahsala;  Hbm.  IF.  *  u8. —  PÜ.:  ai  Cin  Aw.-Bacbst),  mit  der  Eil.: eigSn  anäatk  su/l  u  vor  'd.  h.  (das)  mischen Schulter  und  Brost".
•  j.  ^aäa-  Adj.  'gemahlen,  vom  Getreide': gamca  .  .  yaomca  "um  anlfjam  ma'iuea anspgm  V.J. 51;  —  aäavat  'iänam  (yava- nqm)  aitavat  anasanqm  V.  7.35.
KompE.  —  Aus  ir.  *ärla-%  %  3^2,  aSg.  — VgL  np.  äri/'Mehl',  arm.  aiü  'inablen';  Hbm. AGr.  /.  414.  —  Pü.;  artai,  (m  V.  7):  fehlt,
```


## [2026-09-04T19:34:01.368Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -io \"aleu[a-z]*\" FSD_vol1.txt | sort -u -t: -k3 | head -20; echo \"--- alexia context\"; grep -n -i \"alexipharmic\\|Aleurone\\|aleuron\" FSD_vol1.txt | head -3"
}
```


### [2026-09-04T19:34:02.960Z] TOOL RESULT

```
10832:Aleutian
--- alexia context
```


## [2026-09-04T19:34:09.044Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/aleurone' --note 'pdf page 46, root Al 2, node #5: English aleurone < Gk ἄλευρον, dated 1865-70' 2>&1 | tail -2"
}
```


### [2026-09-04T19:34:10.752Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/386eeeca25184683.txt
```


## [2026-09-04T19:34:12.612Z] AGENT

Now writing the verification file.


## [2026-09-04T19:36:50.229Z] TOOL CALL #64: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-46.json",
 "content": "{\n  \"pdf_page\": 46,\n  \"book_page\": 16,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Al 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂elh₁- 'to grind' (Pokorny '5. al- „mahlen, zermalmen“', IEW I 28-29; Watkins/AHD 'al-⁴, to grind, mill'; LIV 277)\",\n      \"note\": \"A short and, for Nourai, unusually clean chart: every one of the five nodes is verifiable, and Nourai's page reference POK:28 is exact — Pokorny's '5. al- „mahlen, zermalmen“' begins in the last third of p.28 and runs onto p.29, and the very words Nourai puts in his boxes (Av. aša [*arta-] 'gemahlen', Gr. ἀλέω 'mahle', ἄλευρον 'Weizenmehl') are Pokorny's own material. 'Al 2' is Nourai's private homonym number, not Pokorny's ('5. al-'); Watkins numbers the same root 'al-⁴'. Root gloss 'to grind' and the language label 'Indo-European' are both right. Modern notation is *h₂elh₁-, with the two derived stems that this chart actually needs: *h₂léh₁-wr̥ (> Gk. ἄλευρον) and the verbal adjective *h₂l̥h₁-tós 'ground' (> Proto-Iranian *Hr̥Htáh > Av. aša-, Sogd. ārt(ē), MP/NP ārd). TWO SMALL DEFECTS, both in the wording rather than in the etymology: (1) the Sogdian box is glossed 'flower', which is a misprint for 'flour' — I checked the 1999 page image itself (pdftoppm p.46), so the error is Nourai's, not the extraction's; Gharib SOD p.59 no.1498 glosses ʾrtk 'flour'. (2) The arrow Avestan → Persian is a language-chain shortcut: NP ārd does not come from Av. aša- (Avestan *rt > š is an Avestan-only change; Persian keeps -rd), but both continue Ir. *ārta-. Nourai partly saves himself by putting 'arta 1' in the same box — that IS Bartholomae's ir. *ārta-, and from *ārta- the Persian form is regular. Independently, Mann (IEC s.v. aleio) flags NP ard as 'ambig.', wondering whether it might belong with Gk. ártos 'bread'; no one else follows him, and Cheung 2007 (*HarH), Bailey DKS and Wiktionary all keep ārd under this root.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82elh%E2%82%81-\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hr%CC%A5Ht%C3%A1h\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:28\",\n          \"status\": \"supports\",\n          \"note\": \"POK_01.txt ↵-leaf 36 (printed p.28, the '29' catchline visible mid-block): '5. al- „mahlen, zermalmen“. Ai. aṇu- „fein, dünn, sehr klein“ (*al-nu-), hindi und bengali āṭā „Mehl“ ... Av. aša (*arta-) „gemahlen“ (Hübschmann ZdMG. 38, 428, Spiegel BB. 9, 178 A. 1). Arm. alam „mahle“, alauri (*alatrio-) „Mühle“, aleur- „Mehl“ ... Gr. ἀλε-: ἀλέω „mahle, zermalme“ ... ἄλευρον (*ἀλε-ϝρ-ον) „Weizenmehl“ ... WP. I 89.' Page number, gloss and three of the five nodes are Pokorny's own text. The POK_full.txt database block for 'Root / lemma: al-5(*hel-) / Meaning: „to grind“' likewise closes with 'References: WP. I 89. Page(s): 28-29'.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"aša 1, arta 1\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Young Avestan aša- is the verbal adjective 'ground (of grain)', attested twice in the Vidēvdād: gaomca … yaomca … aṣ̌əm 'meat … and barley … ground' (V. 5.52 in Bartholomae's numbering) and aṣ̌avat̰ ẏānəm (ẏavanąm) aṣ̌avat̰ anaṣ̌anąm (V. 7.35), beside the negated an-aša- 'unground'. It goes back to PIE *h₂l̥h₁-tós 'ground' > Proto-Indo-Iranian *Hr̥Htás > Proto-Iranian *Hr̥Htáh / *ārta-, the Avestan š being the regular Avestan outcome of the cluster *rt (as in aša- 'truth' < *r̥ta-). So Nourai's two forms are one and the same item seen from two sides — 'aša' is the attested Avestan word, 'arta' is Bartholomae's pre-form 'Aus ir. *ārta-', not a second Avestan lemma; and the gloss should be 'ground' (adjective), not 'to grind' (the Avestan verb is reconstructed *ar-, unattested outside the participle: Cheung, EDIV s.v. *HarH, 'YAv. *ar- „to grind“ … Partic.: perf. pass. YAv. aša- „ground“'). Hence 'plausible' rather than 'confirmed': the etymology is right, the morphological labelling is loose.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hr%CC%A5Ht%C3%A1h\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82elh%E2%82%81-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:28\",\n              \"status\": \"supports\",\n              \"note\": \"POK_01.txt ↵-leaf 36 (printed p.28): 'Av. aša (*arta-) „gemahlen“ (Hübschmann ZdMG. 38, 428. Spiegel BB. 9, 178 A. 1).' Pokorny gives exactly Nourai's pair aša / *arta under this root, but glosses it 'gemahlen' = 'ground', not 'to grind'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"AiW s.v. ²aša- (BRT.txt ↵-leaf 163; col. ≈ 339, the running column number '335' being printed on leaf 161)\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. ²aša- Adj. „gemahlen, vom Getreide“: gaomca .. yaomca .. aṣ̌əm … V. 5.51; — aṣ̌avat̰ ẏānəm (yavanąm) aṣ̌avat̰ anaṣ̌anąm V. 7.35. … Aus ir. *ārta-, § 3⁵², a§g. — Vgl. np. ārd „Mehl“, arm. alam „mahlen“; Hbm. AGr. I 414.' Bartholomae thus draws Nourai's whole left-hand branch himself: Av. aša- < Ir. *ārta-, cf. NP ārd. He also has an-aša- 'nicht gemahlen' (leaf 101, col. ≈ 215) with the same Vidēvdād passage.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"EDIV p.166 s.v. *HarH 'to grind (grain)'\",\n              \"stance\": \"supports\",\n              \"note\": \"'*HarH „to grind (grain)“. AVESTAN: YAv. *ar- „to grind“. Partic.: perf. pass. YAv. aša- „ground“ (V 5.52, V 7.35). … PIE *H₂elH₁- „to grind“ = LIV: 277 | Pok.: 28 f. IE COGNATES: Gr. ἀλέω, Arm. ałam „I grind“.' Cheung's own reference to Pokorny is Nourai's page.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny I 89 (read from the page image, archive.org in.ernet.dli.2015.70244 leaf n97)\",\n              \"stance\": \"supports\",\n              \"note\": \"'5. al- „mahlen, zermalmen“ … Av. aša- (*arta-) „gemahlen“ (Hübschmann ZdMG. 38, 428, Spiegel BB. 9, 178 A. 1).' Same statement as Pokorny 1959, one generation earlier.\"\n            },\n            {\n              \"src\": \"ISS_alt_DKS\",\n              \"where\": \"Bailey, Dictionary of Khotan Saka p.22 s.v. ārr- 'to grind'\",\n              \"stance\": \"supports\",\n              \"note\": \"'Base ar- „to grind“ … Pašto anal, participle Av. aṣ̌a-, anaṣ̌a-; … IE Pok. 28-9 al- „to grind“ … Greek ἀλέω „to grind“ … Armen. ałam „to grind“.' Bailey too pairs Av. aša-/anaša- with Pokorny 28-9.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. al-⁴\",\n              \"stance\": \"partial\",\n              \"note\": \"'al-⁴. To grind, mill. Suffixed form *al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.]' Watkins keeps only the Greek branch; no Iranian material, so silent on the Avestan node itself while confirming the root and its Pokorny page.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"ârd «آرد» : flour\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP آرد ārd 'flour' continues Middle Persian ārd (Book Pahlavi ʾlt, ideogram KHMA < Aram. qmḥ; MacKenzie CPD p.11 'ard … flour'), which continues Old Iranian *ārta- 'ground (stuff)' — the verbal adjective *h₂l̥h₁-tós of the root of this chart. The cluster -rt- is preserved in Southwest Iranian and voiced to -rd in the Middle Persian period (as in *kr̥ta- > kard, *marta- > mard); the initial ā- is the lengthened grade already required by Bartholomae's *ārta-. It is therefore a sister of, not a descendant of, Avestan aša-, whose š is the specifically Avestan reflex of *rt; the arrow is correct only if read from the second word in Nourai's Avestan box, 'arta'. Parallel outcomes across the family: Sogdian ʾrtk / Yaghnobi arta 'flour', Khotanese āḍa, Khwarezmian ʾrd, Bactrian αρδο, Baluchi ārt, Kurdish ar(d), Pashto oṛə, Zazaki ardi. Semantically nothing moved: 'ground' → 'the ground stuff, meal, flour'.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%AF\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hr%CC%A5Ht%C3%A1h\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:5\",\n              \"status\": \"supports\",\n              \"note\": \"HRN.txt ↵-leaf 27 = printed p.5, Horn's numbered entry 13: '13. ārd „Mehl“. Kāš. ort, ürt, vergl. auch s. v. āsyāh: ōr, ār, ir. aw. aša- „gemahlen“, anaša- (Hübschmann ZDMG. 38, 428); phlv. ārd „Mehl“. kurd. ār, ārd (Jaba-Justi), ārt, irt (Houtum-Schindler); afg. ōra; bel. ārt n. art (15); arm. alewr „Mehl“, ałam „mahlen“ (unsicher, H. No. 7).' Precisely Nourai's arrow (Av. aša- → NP ārd), plus the Pahlavi link he omits.\"\n            },\n            {\n              \"ref\": \"BQT:31\",\n              \"status\": \"partial\",\n              \"note\": \"BQT_v1_pages.txt ↵-leaf 241 = printed p.31 (running head 'آرش — ۳۱ —'), read from the page image (archive.org borhan-ghate-v1/page/n241) and saved to data/verification/sources/refs/ocr/BQT/31.vision.txt. The entry آرد runs over from p.30 onto this page: '… و بسکون ثالث معروف است که غلهٔ آسیا کرده باشد ۲' ('with sukūn on the third letter it is the well-known thing, grain that has been milled') — i.e. flour, so the gloss is confirmed. Mo'in's etymological footnote 2 on the same page is only 'پهلوی ârt «تاوادیا ۱۵۹، بونکر ۱۱۲»' (Pahlavi ārt, citing Tavadia 159, Bunker 112). So BQT:31 supports the word and its meaning and adds the Pahlavi antecedent, but says nothing about Avestan or Indo-European: 'partial' with respect to the arrow drawn.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD p.11 s.v. ard (PHD_mackenzie.txt line 1163)\",\n              \"stance\": \"supports\",\n              \"note\": \"'ard [KHMA < A qmḥ; ʾlt | N ~] flour.' The Aramaic ideogram KHMA (qmḥ 'flour') with the phonetic spelling ʾlt = /ārd/, and the New Persian equivalent marked '~' = ārd. This is the Middle Persian stage Nourai's chart skips.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"EDIV p.166 s.v. *HarH\",\n              \"stance\": \"supports\",\n              \"note\": \"'MIDDLE PERSIAN: BMP ʾl- (THNN-) /ar-/ „to grind, mill“, BMP ʾlt /ard/ „flour“ … NWIR: … NP ard, (? borrowed into) Bal. art, Kurd. (Kurm.) ar(d), (Sor.) ard, Zaz. ar(di) … „flour“ … PIE *H₂elH₁- „to grind“ = LIV: 277 | Pok.: 28 f.' Cheung uniquely also attests the Middle Persian verb ar- 'to grind' itself.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny I 89 (page image, archive.org in.ernet.dli.2015.70244 leaf n97)\",\n              \"stance\": \"supports\",\n              \"note\": \"The 1930 text prints '… hindi und bengali āṭā „Mehl“ (u. dgl.; Kuhn KZ. 30, 355); npers. ārd „Mehl“.' — Walde-Pokorny list New Persian ārd under root 5. al- explicitly. (The OCR renders it 'npers. anl „Hehl“'; the page image settles it.) Pokorny 1959 dropped the Persian word, which is why POK:28 alone does not cover this node.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in, Farhang-e Fārsi s.v. آرد (MON_part1.txt line 2646)\",\n              \"stance\": \"supports\",\n              \"note\": \"'آرد … نرمهٔ آس کردهٔ حبوب، گردی که از کوبیدن یا آسیا کردن غلات بدست آید. آرد گندم، آرد جو، آرد برنج.' ('the fine product of milled pulses; the powder obtained by pounding or milling grain'). Confirms the meaning 'flour'; Mo'in's short origin tag is illegible in this OCR, but his footnote in his own Borhān edition (BQT:31) gives Pahlavi ārt.\"\n            },\n            {\n              \"src\": \"ISS_alt_DKS\",\n              \"where\": \"Bailey, DKS p.22 s.vv. āḍa- 'flour', ārr- 'to grind'\",\n              \"stance\": \"supports\",\n              \"note\": \"'For „flour“, the participle a-rta-, -ka-, here āḍa- (either *arata- or a-rta-), Zor.P., Yaγn. art, N.Pers. ard, Pašto ōṛə masc. plur., Waziri Pašto ōṛə „dough“, Yidγa yaṛə … Parāčī wārun (*ārtana-).' Bailey's *arta-ka- is the very formation behind the Sogdian node of this chart, and he lists N.Pers. ard in the same breath.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, IE Comparative Dictionary s.v. aleiō 'grind, pound, crush'\",\n              \"stance\": \"partial\",\n              \"note\": \"'aleiō „grind, pound, crush“. Cf. aleuro-. Hind.Beng. cf. āṭā, Guj. āṭo, Romani arno, andro, aro; Per. ard (ambig. „flour“, perhaps to Gk. ártos „bread“. Bois. and Hof. uncertain); Arm. ałam „grind“; Gk. aléō.' Mann keeps NP ard here but registers a doubt (a possible link to Gk. ártos) that no other source shares.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien (grepped 'ārd', 'ärd', 'Mehl')\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry for ārd; the only 'Mehl' items are no. 320 'Np. pist … „Mehl, geröstetes Mehl“' and passing remarks. Hübschmann's statement on this word is in ZDMG 38, 428 (the article Horn, Pokorny, Walde-Pokorny and Bartholomae all cite), not in the Persische Studien.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II (Glossary)\",\n              \"stance\": \"silent\",\n              \"note\": \"No headword ard/ārt; the glossary covers the Kārnāmag and related texts, whose only flour word is pist [pst'] 'flour, or something pounded or crushed' (p.3150 of NYB_vol2_glossary.txt).\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi (ARY_pages.txt / ARY_latin_index_pages.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"Greps for آرد and for a Latin index entry ARD return only incidental occurrences (e.g. 'آردکردن گندم' in a discussion of Homer); Aryanpur has no headword for آرد.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"`rtk : flower\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The word and the derivation are right; the GLOSS is wrong. Sogdian ʾrtk (Buddhist/Sogdian-script ārtē, also written ʾrtʾk(w), Christian-script ʾrty) means 'FLOUR', not 'flower'. It is the same *arta-ka- 'ground (stuff)' formation as the Persian word — Ir. *ārta- (< PIE *h₂l̥h₁-tós) plus the Sogdian -k(ē) suffix — and survives in Yaghnobi, Sogdian's modern descendant, as art/arta 'flour'. Gharib's dictionary makes the derivation explicit ('©Av. aša'), so the arrow root → Sogdian is exactly what Nourai's own source says. I rendered the 1999 page image itself (pdftoppm -f 46 of EtymologicalDictionary-persian-english.pdf): the printed box really does read '`rtk : flower', so this is Nourai's own typo for 'flour' and NOT an error introduced by this repository's extraction — but the JSON should carry 'flour' if the data are to be published.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hr%CC%A5Ht%C3%A1h\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:59\",\n              \"status\": \"supports\",\n              \"note\": \"SOD_pages.txt ↵-leaf 124, which carries the printed page number '59' in its header — so Nourai's SOD:59 is a page, not an entry number. Entry 1498 on it reads: '1498 ʾrtk  S — artē (ʾrtkw) ©Av. aša  =ʾrt², ʾrty³ — flour — MDii, ʾrtkw; MDiii p30, ʾrtw'. The same page has '1479 ʾrt² C — art ©ob. ʾrty ? =ʾrtk — flour' and '1508 ʾrty² C — artē ? =ʾrt¹, ʾrtk — flour', and '1481 ʾrtʾk(w) => ʾrtk'. Gharib glosses all of them 'flour' and derives them from Avestan aša — Nourai's arrow, with his gloss mistyped.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SOD\",\n              \"where\": \"Gharib, Sogdian Dictionary p.59, entries 1479 / 1481 / 1498 / 1508\",\n              \"stance\": \"supports\",\n              \"note\": \"See the ref_check quotation: 'artē (ʾrtkw) ©Av. aša … flour'. Note that Gharib's own cross-reference is to the Avestan participle, i.e. she treats ʾrtk as the Sogdian continuant of *arta-ka-.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"EDIV p.166 s.v. *HarH, section SOGDIAN\",\n              \"stance\": \"partial\",\n              \"note\": \"Cheung's Sogdian material under this root is 'BSogd. ʾrθ „millstone“ (SCE 231), BSogd. ʾrθʾrnʾk „mill“ (SCE 161)' — he cites the mill words rather than ʾrtk 'flour', but he does list the whole *arta- 'flour' family for the neighbouring languages ('Chor. ʾrd „flour“', 'NP ard'), so nothing here contradicts the node.\"\n            },\n            {\n              \"src\": \"ISS_alt_DKS\",\n              \"where\": \"Bailey, DKS p.22 s.v. āḍa- 'flour'\",\n              \"stance\": \"supports\",\n              \"note\": \"'For „flour“, the participle a-rta-, -ka-, here āḍa- … Zor.P., Yaγn. art, N.Pers. ard …'. Bailey's explicit '-ka-' variant of the participle is the Sogdian ʾrtk, and Yaghnobi art is its living continuation.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"alein : to grind ; al-euron : wheat flour\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek ἀλέω aléō 'I grind, mill, bruise' (Attic contract verb; Nourai's 'alein' is its present infinitive ἀλεῖν, contracted from ἀλέειν) continues PIE *h₂elh₁-, the same root as the Iranian branch, with the laryngeal reflected as Greek -ε-. ἄλευρον áleuron 'wheat flour' (usually plural ἄλευρα; Homer already has the derivative form) is the r/n-heteroclite *h₂léh₁-wr̥ > *ἀλε-ϝρ-ον with the digamma lost between vowels — Pokorny prints the pre-form '*ἀλε-ϝρ-ον' — beside the older ἄλειαρ, pl. ἀλείατα, from the same stem. Nourai's hyphenation 'al-euron' shows he took the analysis from Watkins, whose entry reads 'Suffixed form *al-euro-'. The Armenian cognates ałam 'I grind' and aleur 'flour' show the same pair independently (Hübschmann, Arm. Gr. I 414: not borrowed from Greek, despite the l).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E1%BC%84%CE%BB%CE%B5%CF%85%CF%81%CE%BF%CE%BD\",\n            \"https://en.wiktionary.org/wiki/%E1%BC%80%CE%BB%CE%AD%CF%89\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v.: 'al-⁴, To grind, mill. Suffixed form *al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.]' Both of Nourai's Greek words (as root gloss and as derived noun), the English derivative of node #5, and even his POK:28 page number come straight from this entry. The word-index of the same volume has 'ALEURONE  al-⁴'.\"\n            },\n            {\n              \"ref\": \"KLN:47\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt ↵-leaf 36 (two printed pages per leaf; the leaf opens with the entry 'alcohol' = p.47): 'aleurone, also aleuron, n., a proteid substance found in cereals (biochem.) — Gk. ἄλευρον, „wheat flour“, fr. ἀλεῖν, „to grind“, which is cogn. with Arm. ałam, „I grind, pulverize“, aleur, „flour“, and prob. also with OI. aṇuḥ (for *al-nuḥ), „thin, fine“.' Klein's 'ἄλευρον „wheat flour“' and 'ἀλεῖν „to grind“' are verbatim Nourai's two Greek entries, glosses included — this is where the box was copied from.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW I 28-29 (POK_01.txt ↵-leaf 36)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gr. ἀλε-: ἀλέω „mahle, zermalme“; ἀλέται λίθοι „Mühlsteine“, ἄλετος und ἀλετός „das Mahlen“, ἀλετών „Mühle“, ἀλετρεύω „mahle“, ἄλε[ϝ]αρ, pl. ἀλείατα … „Mehl“ … ἄλευρον (*ἀλε-ϝρ-ον) „Weizenmehl“.' Pokorny's gloss 'Weizenmehl' is Nourai's 'wheat flour' translated.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny I 89 (page image, leaf n97)\",\n              \"stance\": \"supports\",\n              \"note\": \"Identical Greek material, plus the footnote in which Walde rejects Fick's attempt to derive ἀλέω from *mel- 'mahlen': 'ἀλέω nicht nach Fick … als *ml̥- zu *mel- „mahlen“'. So the separation of this root from the well-known *melh₂- 'grind' is deliberate and old.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck, Selected Synonyms §5.56 GRIND, para. 2\",\n              \"stance\": \"supports\",\n              \"note\": \"'Grk. ἀλέω, late ἀλήθω, NG ἀλέθω : Arm. ałam „grind“, alauri „mill“, aleur „meal“, Skt. aṇu- „fine, thin“. Walde-P. 1.89. Boisacq 43.' Buck's §5.55 MEAL, FLOUR table gives Grk. ἄλευρον as the classical word.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.vv. aleiō and aleur- (aleuor-)\",\n              \"stance\": \"supports\",\n              \"note\": \"'aleur- (aleuor-) „millings, flour“. Cf. aleiō. Arm. aliwr, aler, -erb; Gk. áleuron, áleiar.' Mann reconstructs the noun stem separately from the verb, exactly the *h₂léh₁-wr̥ / *h₂elh₁- pair.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Webster's New Twentieth Century Dict., 2nd ed., vol. I s.vv. Aletris, Aleurites, aleuromancy\",\n              \"stance\": \"supports\",\n              \"note\": \"'Al'e-tris, n. [L., from Gr. aletris, a grinder of corn, from aletreuein; alein, to grind.]'; 'Al-eu-ri'tes, n. [L., from Gr. aleurites, pertaining to aleuron, meal, from alein, to grind.]' Webster uses precisely Nourai's citation form 'alein, to grind'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"aleurone\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A 19th-century scientific coinage, not an inherited word: Greek ἄλευρον 'flour' was taken over by plant chemists as the name of the protein granules of the endosperm and its outermost layer, the aleurone layer (German Aleuron, whence English aleurone/aleuron; Wiktionary dates the English form 1865-70). The -e is the ordinary English ending added to a Greek neuter in -ον, as in xanthone, chitone; the meaning was fixed by the resemblance of the granular material to fine flour. Derivatives coined from the same Greek word cluster around it in the older dictionaries: aleuromancy 'divination by flour', aleurometer 'gluten tester', aleuronat 'flour made of aleurone', aleuronic. Nourai gives no reference for this node, but it is exactly the English derivative listed under the root by Watkins ('ALEURONE') and it is the headword under which Klein (KLN:47, cited on the parent node) gives the Greek chain.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/aleurone\",\n            \"https://en.wiktionary.org/wiki/%E1%BC%84%CE%BB%CE%B5%CF%85%CF%81%CE%BF%CE%BD\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai cites no reference on this node. The obvious sources are the two given on its parent: AHD (Watkins) s.v. al-⁴, whose sole English derivative is 'ALEURONE', and KLN:47, whose headword is 'aleurone'. Both were checked and both support the node (see node #4).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966, p.47 s.v. aleurone (KLN_1966.txt ↵-leaf 36)\",\n              \"stance\": \"supports\",\n              \"note\": \"'aleurone, also aleuron, n., a proteid substance found in cereals (biochem.) — Gk. ἄλευρον, „wheat flour“, fr. ἀλεῖν, „to grind“ …'. The following entry, 'Aleyrodes, n., a genus of insects (entomol.) — ModL., fr. Gk. ἀλευρώδης „resembling flour“ …', shows the same Modern-Latin coinage habit.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Webster's New Twentieth Century Dict., 2nd ed., vol. I s.v. aleurone\",\n              \"stance\": \"supports\",\n              \"note\": \"'a-leū'rō-ne, n. a protein substance found in small granules in ripening seeds, and forming an outer layer in cereals'; with 'à-leū'rō-nat, n. flour made of aleurone' and 'al-eu-ron'ic, a. pertaining to or resembling aleurone' — confirming that the word is real English and biochemical, as the chart says.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, root al-⁴ and the English word index\",\n              \"stance\": \"supports\",\n              \"note\": \"'al-⁴, To grind, mill. Suffixed form *al-euro- in Greek aleuron, meal, flour: ALEURONE.'; index entry 'ALEURONE  al-⁴'. Aleurone is the only English reflex Watkins assigns to this root — precisely the shape of Nourai's Greek → English branch.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etymological Dictionary (grepped 'aleuron', 'aleurone')\",\n              \"stance\": \"silent\",\n              \"note\": \"Not in Skeat — expected, since his dictionary is a concise selection of ordinary English words and excludes technical biochemical coinages.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"Funk & Wagnalls New Standard Dictionary vol. I (FSD_vol1.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"The OCR of the A-D volume yields no 'aleuron*' string at all (only 'Aleutian'), so the entry — if present in the printed volume — is lost in this scan; nothing found either way.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-04T19:36:50.260Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-46.json (file state is current in your context — no need to Read it back)
```


## [2026-09-04T19:36:52.717Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-46.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 46"
}
```


### [2026-09-04T19:36:54.661Z] TOOL RESULT

```
JSON OK
nodes verified: 5/5
node verdicts: {'plausible': 1, 'confirmed': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 5, 'partial': 1, 'not_checked': 1}
books consulted: {'supports': 19, 'partial': 3, 'silent': 5} | by book: {'CHEUNG': 3, 'WLD': 3, 'ISS_alt_DKS': 3, 'AHD': 2, 'IEC': 2, 'WEB': 2, 'BRT': 1, 'PHD': 1, 'MON': 1, 'HUB': 1, 'NYB': 1, 'ARY': 1, 'SOD': 1, 'POK': 1, 'SYN': 1, 'KLN': 1, 'SKT': 1, 'FSD': 1}
```


## [2026-09-04T19:36:57.676Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 46 2>&1 | tail -20"
}
```


### [2026-09-04T19:36:59.225Z] TOOL RESULT

```
6 cited URLs, 0 not yet archived
archived 0, failed 0
```


## [2026-09-04T19:37:17.646Z] AGENT

Done. `data/verification/page-46.json` is written and `verify_check.py 46` reports 5/5 nodes, no PROBLEM lines, 6/6 cited URLs archived.

**Page 46 (book p.16) — one entry, root "Al 2" [Indo-European] "to grind", 5 nodes**

- Root: **confirmed** (POK:28 exact — Pokorny "5. al- „mahlen, zermalmen“", IEW I 28-29 = PIE *h₂elh₁-, AHD al-⁴).
- Node verdicts: confirmed 3, plausible 1, transcription_suspect 1.
- Ref checks: supports 5, partial 1, not_checked 1. Books consulted: 18 distinct (supports 19, partial 3, silent 5).

Flagged items:

- **#3 Sogdian `rtk "flower" — transcription_suspect.** The gloss is a typo for **"flour"**. Gharib SOD p.59 no. 1498: "ʾrtk S — artē (ʾrtkw) ©Av. aša — flour". I rendered the 1999 PDF page image itself, so the error is Nourai's own misprint, not this repo's extraction — but the JSON/website should carry "flour". Derivation itself (*arta-ka- from the root, via Av. aša) is exactly what Nourai's cited source says.
- **#1 Avestan "aša 1, arta 1 : to grind" — plausible.** Etymology right, labelling loose: aša- is the verbal *adjective* "ground (of grain)" (Vd. 5.52, 7.35), not a verb "to grind"; and "arta" is not a second Avestan lemma but Bartholomae's pre-form "aus ir. *ārta-".

Other notes worth passing on:

- The **Avestan → Persian arrow is a language-chain shortcut**: NP ārd cannot descend from Av. aša- (Av. *rt > š is Avestan-only); both continue Ir. *ārta-. Nourai partly saves it by putting "arta" in the same box. Node still marked confirmed since Bartholomae (AiW s.v. ²aša-: "Aus ir. *ārta- … Vgl. np. ārd 'Mehl'"), Horn no. 13 (p.5), Walde-Pokorny I 89 ("npers. ārd 'Mehl'", read from the page image — the OCR garbles it), Cheung *HarH, Bailey DKS 22 and Wiktionary all give the same chain.
- **BQT:31 verified from the page image** (archive.org borhan-ghate-v1 leaf n241, running head ۳۱); Mo'in's footnote on آرد is only "پهلوی ârt". Transcription saved to `data/verification/sources/refs/ocr/BQT/31.vision.txt`.
- Only dissenting source found: **Mann (IEC s.v. aleiō)** marks Per. ard "ambig.", floating a link to Gk. ártos "bread"; nobody follows him.
- KLN:47 and AHD are verbatim the source of Nourai's Greek/English boxes ("ἄλευρον 'wheat flour', fr. ἀλεῖν 'to grind'"; Watkins "Suffixed form *al-euro- … : ALEURONE").
