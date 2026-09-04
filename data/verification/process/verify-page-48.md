# Verification process log — verify-page-48


## [2026-09-04T19:29:49.913Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 48 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-48.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-48.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-48.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 48` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T19:29:51.552Z] AGENT

I'll start by reading the instructions and the relevant files.


## [2026-09-04T19:29:53.635Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:29:53.649Z] TOOL RESULT

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


## [2026-09-04T19:29:53.703Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-48.txt"
}
```


### [2026-09-04T19:29:53.725Z] TOOL RESULT

```
1	=== PDF page 48 (book page 18) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Al 4, Âlĕiô, Âleŭos : to wander, roam, rove  (refs POK:27; AHD:1505; IEC:14)
4	#1 (parent #0) [Persian] refs=IEC:14 | âvâreh «آواره» : homeless, wanderer, exiled | extra: آوار
5	#2 (parent #0) [Latin] refs=AHD:1505 | ulâre : to wander ; amb-ulâre : to walk around ☞Ambhi ; ex-ul : wandering outside, exile ☞Ei
6	  #3 (parent #2) [English] refs=AHD | alley, preamble, ambulate, exile
7	--- entry 1 ---
8	ROOT Âlĕiô -> redirect to Al 4
9	
```


## [2026-09-04T19:29:57.173Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-48.json",
 "description": "Read page 48 JSON"
}
```


### [2026-09-04T19:29:57.211Z] TOOL RESULT

```
{
  "pdf_page": 48,
  "book_page": 18,
  "entries": [
    {
      "root": {
        "name": "Al 4, Âlĕiô, Âleŭos",
        "lang": "Indo-European",
        "refs": "POK:27; AHD:1505; IEC:14",
        "gloss": "to wander, roam, rove"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:14",
          "words": [
            {"translit": "âvâreh", "gloss": "homeless, wanderer, exiled", "script": "آواره"}
          ],
          "script_extra": "آوار",
          "note": null,
          "quote": {
            "text": "هوای کوی تو از سر نمی رود ما را - غریب را دل آواره در وطن باشد",
            "poet": "Hâfez"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1505",
          "words": [
            {"translit": "ulâre", "gloss": "to wander", "script": null},
            {"translit": "amb-ulâre", "gloss": "to walk around", "script": null, "see": ["Ambhi"]},
            {"translit": "ex-ul", "gloss": "wandering outside, exile", "script": null, "see": ["Ei"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "alley, preamble, ambulate, exile", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Âlĕiô",
        "redirect": "Al 4"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-04T19:29:58.920Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T19:29:58.963Z] TOOL RESULT

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


## [2026-09-04T19:30:15.765Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','AHD','IEC','WLD','KLN','SKT','LEW','LAT','SYN','HRN','HUB','MON','BQT','ARY','CHEUNG','PHD','FSD','WEB','ETYMONLINE']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:600]);print()\n\"",
 "description": "Inspect refs_online entries"
}
```


## [2026-09-04T19:30:16.702Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -30 && echo --- && cat tools/verify_check.py | head -60",
 "description": "List verification dir and check script"
}
```


### [2026-09-04T19:30:17.585Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
```


### [2026-09-04T19:30:17.632Z] TOOL RESULT

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
```


## [2026-09-04T19:30:23.461Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==36' POK_01.txt | head -80",
 "description": "Print Pokorny page 27"
}
```


## [2026-09-04T19:30:23.957Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"ambulate\\|to wander\" AHD_watkins1985.txt | head -40",
 "description": "Grep Watkins for wander"
}
```


### [2026-09-04T19:30:25.224Z] TOOL RESULT

```
chse.  heile';  aschwed.  alda .fruchttragende  Eiche',  aisl.  aldin  .Baumfrucht,  bes.  eßbare  (Ecker.  Eichel)'.
WP.  I  86  f..  WH.  I  4.  31  f.
3.  äl-  .planlos  umherschweifen,  irren;   auch  geistig  irre  sein'.
Gr.  üXi]  .das  Umherschweifen'.  äXdo(.iccL  (hom.  Pf.  dX(xXr]iiaL),  äXalvco .schweife  umher' ^).  äXrjrrjg  .Bettler'.  dXrjTSvw  .schweife  bettelnd  umber'. tlXioQ  .vergeblich'  (Spiritus  asper  freilich  noch  unerklärt,  s.  Boisacq  44. auch  gegen  die  Annahme  von  anl.  j^-);  von  einer  Basis  aiu-,  aleu-  gr. dXvü)  .bin  außer  mir'-).  äXvcjacü  ds.  (Hom.;   Fut.  äXv^si   Hippokr.).   äXvKT]
')  äXaC(t}v  .Aufschneider,  Prahler'  (eigentlich  herumziehender  Gaukler,  Marktschreier), stammt  nach  Bonfante  (BSL.  37,  77)  aus  dem  thrak.  VN  'AkaCövsg.
*)  dlv(üj  dXviü)  aus  *äXvjiü)  vergleichen  Schulze  Qu.  ep.  310  f.,  Lagercrantz  Z.  gr. Lautg.  89  mit  ai.  ro^ati,  ru^yati  , aufgebracht  sein,  zürnen',  das  aber  von  Uhlenbeck  Ai. Wb.  256  richtiger  zu  lit.  rustas  »unfreundlich'  gestellt  wird.
28  •
jUnruhe;,  Beängstigung^,  äXvaig  (von  äUco)  ;Angst',  Ixlvg,  -vog  (Flut.)  ^niüßi- ges  Herumtreiben,  Langeweile^;  mit  dem  Begriffe  ^umherirren,  um  einer gefährlichen  Stelle  oder  Sache  nicht  zu  nahe  zu  kommen'^,  auch  dlsvoixai, dXeojxai  ,vermeide^,  dlva/^o)  (*aXvy,-(J'Aa),  vgl.  Aor.  ijlv^a)  ,entkomme^,  dXv- ayiccLüj  ^vermeide,  fliehe'^,  dXssiva)  ds.,  dXecxjXrj  , Abwehr^  (*dXeJ^ajXrj  Bildung wie  cpsLÖcoXrj).
Mit  ä- :  '^Xdaxo)  ,irre  umher*,  i]Xaivix)  ,bin  wahnsinnig^.  Med.  ,schweife umher^,  '^Xef.iazog  (dor.  äXsfia-vog  Theokr.)  ,töricht,  eitel^,  '^Xi^iog  ,nichtig, vergeblich,  töricht^,  '^Xsög  ,verwirrt,  betört;  verwirrend'^,  (daneben  die  äol. Entsprechung  äXXog  eines  *dXi.og  in:)  hom.  äXXa  cpQOvewv  ,cpQSvag  rjXeog^ , betäubt,  bewußtlos*"  (aus  dor.  *aXE6g  stammt  lat.  älea  ,blindes  Glück, Würfet).
Lat.  amhulö  ,spaziere^  (umbr.  amholtu*  ,ambulato^) ;  (lat.  alüchior  ,rede gedankenlos  ins  Blaue  hinein,  bin  geistesabwesend^  ist  wohl  aus  dXvu) unter  formaler  Anlehnung  an  väticinor  entlehnt).
Dazu  lett.  aluot,  aluoties  ,umherirreu,  sich  verirren^,  mit  ä  lett.  äVa ,halb  verrückter  Mensch^,  äVuoties  ,sich  närrisch  gebärdend
Toch.  AB  äl-  ,trennen,  entfernen^.
WP.  I  87  f.,  WH.  I  33,  38,  EM.  43  (stellt  amhulö  zu  gr.  ^Xavvcü,  St.  el-).
4.  ai-  ,brennen^
Ai.  alätam  n.  , Feuerbrand,  Kohle^  (auch  lUmuJcam  ,Brand'^) ;  lat.  adoleö ,verbrenne  (bes.  Opfer)',  adolescö,  -ere  ,auflodern  (von  Altären)^  (0  aus a,  wie  im  etymologisch  verschiedenen  adolesc
```


### [2026-09-04T19:30:25.261Z] TOOL RESULT

```
280:al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
458:ers-'. To be in motion. 1. Variant form *rés- in Germanic *rés- in Old Norse rds, rushing: RACE?. 2. Form ers-d- in Latin errdre, to wander: ERR, ERRATIC, ERRATUM, ERRO- NEOUS, ERROR; ABERRATION. [Pok. 2. ere-s- 336.]
834:*pld-ru- in Germanic *fléruz, floor, in Old English flor, floor: FLOOR; b. suffixed form *p/d-no- in Latin planus, flat, level, even, plain, clear: LLANO, PIANO?, PLAIN, PLANARIAN, PLANE!, PLANE2, PLANE, PLANISH, PLANO-, PLANULA; AIRPLANE, EXPLAIN. 4. Suffixed zero-grade form *pb-ma in Latin palma (< *palama), palm of the hand: PALM!, PALM2. 5. Possibly extended variant form *plan- in: a. Greek planasthai, to wander (< “to spread out”): PLANET; APLANATIC; b. possibly Germanic *flan- in Old Norse flana, to wander aimlessly, akin to the Germanic source of French fléner, to walk the streets idly: FLANEUR. 6. Suffixed zero-grade form *pl-dh- in Greek plassein (< *plath-yein), to mold, “spread out”: -PLASIA, PLASMA, -PLAST, PLASTER, PLASTIC, PLASTID, -PLASTY; DYSPLASIA, METAPLASM, (TOXOPLASMA). 7. O-grade form *pols- in: a. Russian polyi, open: POLYN- Ya; b. Slavic polje, broad flat land, field, in Polish Polak, Pole: PoLACK, POLKA. See also extensions plak-' and plat-. [Pok. pels- 805.] pele-%, Citadel, fortified high place. Greek polis, city: POLICE, (POLICY!), POLIS, POLITIC, (POLITY); ACROPOLIS, COSMOPOLITE, MEGALOPOLIS, METROPOLIS, NECROPOLIS, POLICLINIC, PROPOLIS. [In Pok. 1. pel- 798.] pelis-. Also pels-. Rock, cliff. Germanic *felzam, rock, in Old Norse fjall, fell, rock, barren plateau: FJELD. [Pok. peli-s- 807.] pen-. Swamp. Suffixed o-grade form *pon-yo- in Ger- manic *fanjam, swamp, marsh, in Old English fenn, marsh: FEN. [Pok. 2. pen- 807.] penkve. Five. I. Basic form *penke. 1. Assimilated form *pempe in Germanic *fimf in: a. Old English fif, five: FIVE; b. Old High German finf, funf, five: FIN2. 2. Ger- manic compound “*fimftehun, fifteen (*tehun, ten; see dekm), in: a. Old English fifténe, fifteen: FIFTEEN; b. Old Norse fimmtdn, fifteen: FEMTO-. 3. Assimilated form *kvenke in: a. Latin quinque, five: CINQUAIN, CINQUE, QUINQUE-; CINQUEFOIL, QUINCUNX; b. Latin distributive quini, five each: KENO, QUINATE; C. Latin compound quindecim, fifteen (decem, ten; see dekm): QUINDECENNIAL. 4. Greek pente, five: PENTA-, PENTAD; PENTACLE, PENTADACTYL, PENTAGON, PENTAMETER, PENTARCHY, PENTASTICH, PENTATEUCH, PENTATHLON. 5. Sanskrit pavica, five: PUNCH’; PACHISI. II. Compound *penke-(d)konta, “five tens,” fifty (*-(d)konta, group of ten; see dekm). 1. Latin quinqudginta, fifty: QUINQUA- GENARIAN, QUINQUAGESIMA. 2. Greek pentékonta, fifty: Pentecost. III. Ordinal adjective *penk-to-. 1. Ger- manic “fimftdn- in Old English fifta, fifth: FIFTH. 2. Latin quintus (< *quinc-tos), feminine quinta, fifth: QUINT!, QUINTAIN, QUINTET, QUINTILE; QUINTESSENCE, QUINTILLION, QUINTUPLE. IV. Suffixed form *penkv-ro- in Germanic *fingwraz, finger (< “one of five”), in Old English finger, finger: FINGER. V. Suffixed reduced zero-grade form *pnk-sti- in Germanic *fii(nh)stiz in: a. Old English fyst, fist: Fist; b. Dutch vuist, fist: FOIST. [Pok. penkve 808, pnksti- 839.] pent-. To tread, go. 1. Germanic *finthan, to come upon, discover, in Old English findan, to find: FIND. 2. Suffixed o-grade form *pont-i- in: a. Latin pdns (stem pont-), bridge (earliest meaning, “way, passage,” preserved in the priestly title pontifex, “he who prepares the way”; -fex, maker; see dhé-1): PONS, PONTIFEX, PONTIFF, PON- TINE, PONTOON, PUNT}; (TRANSPONTINE); b. Russian put’, path, way, in sputnik, fellow traveler: SPUTNIK. 3. Zero-grade form *pnt- in Greek patein, to tread, walk: PERIPATETIC. 4. Suffixed zero-grade form *pnt-o- in Iranian *path-, probably borrowed (? via Scythian) into Germanic as *patha-, way, path, in: a. Old English peth, path: paTH; b. Middle Dutch pad, way, path: FOOTPAD. [Pok. pent- 808.] per’. Base of prepositions and preverbs with the basic meanings of “forward,” “through,” and a wide range of extended senses such as “in front of,” “before,” “early,” “first,” “chief,” “toward,” “against,” “near,” “at,”
1144:*wn-to- in Germanic *wundaz in Old English wund, a wound: WOUND!. 2. Suffixed o-grade form *won-yo- in Germanic *wanja-, a swelling, in Old English wen(n), wen{n), wen: WENI. [In Pok. 1. ué- 1108.] wendh-. To turn, wind, weave. 1. Germanic *windan, to wind, in: a. Old English windan, to wind: WIND2; b. Old Norse vinda, to wind: WINDLASS. 2. Germanic causative *wandjan in: a. Old English wendan, to turn to: WEND; b. Dutch wenden, to turn: WENTLETRAP. 3. Germanic *wandr6n, to roam about, in: a. Old English wandrian, to wander: WANDER; b. German wandern, to wander: WANDERLUST. 4. Germanic *wanduz in Old Norse véndr, a supple twig: WAND. 5. Germanic *wandljaz, “wan- derer,” perhaps in Latin Vandalus, a Vandal: VANDAL. [Pok. 1. uwendh- 1148.] weng-. To bend, curve. 1. Germanic *wink- in Old Eng- lish wincian, to close the eyes (< “to bend down the eyelids”): WINK. 2. Germanic *winkja in Old English wince, a reel, roller: WINCH. 3. Germanic *winkil- in Old English -wincel, spiral shell: PERIWINKLE!. 4, Germanic *wankil-, *wankul- in: a. Old English wencel, youth, maid (< “inconstant one’): WENCH; b. Old English wancol, inconstant, unsteady: wonky. 5. Germanic *wankj- in: a. Old French gauchir, to turn aside: GAUCHE; b. Anglo-Norman *wencir, to turn aside, avoid (> Middle English wincen, to kick): w1NcE. [Pok. we-n-g- 1148.] wep-. Bad, evil. From earlier *awep-. Suffixed zero-grade form *up-elo- in Germanic *ubilaz, evil, in Old English yfel, evil: EVIL. [wépnam. Weapon. Germanic root. 1. Old English wé- P(e)n, weapon: WEAPON. 2. Old Norse vapn (plural vdpn), weapon: WAPENTAKE.] wer-', High raised spot. 1. Suffixed form *wer-d- in Germanic *wartén- in Old English wearte, wart: WART. 2. Possibly Germanic *war- in obsolete Swedish var- bulde, “pus swelling” (bulde, swelling; see bhel-2), akin to the source of WARBLE2. 3. Latin varius (genitive plural variérum), spotty, speckled, changeable: (VAIR), VARIE- GATE, (VARIETY), VARIOLA, VARIORUM, VARIOUS, VARY; (MINIVER). 4. Latin varix, varicose vein: VARIX. 5. Suf- fixed and extended zero-grade form *wrsu-ko- in Latin verriica, a wart: VERRUCA. [Pok. 2. wer- 1151, 2. ud- 1108.] wer-2. To raise, lift, hold suspended. Earlier form *ower-. 1. Basic form *awer- in Greek aeirein, to raise, and Greek artéria, windpipe, artery: AORTA, ARSIS, ARTERIO-, ARTERIOLE, ARTERY. 2. Possibly referred to this root (obscure basic form *dwer-) is Greek aér (> Latin aer > Italian aria), air: AERIAL AERO-, AIR, ARIA, MALARIA. 3. Related to Greek aér, air, is Greek aura (< zero-grade form *aur-), breath, vapor: AURA. [Pok. 1. wer- 1151.] wer-3, Conventional base of various Indo-European roots; to turn, bend. I. Root *wert-, to turn, wind. 1. Germanic *werth- in: a. Germanic variant *warth- in (i) Old Eng- lish -weard, toward (< “turned toward”): -WARD (ii) Germanic *inwarth, inward (*in, in; see en), in Old English inweard, inward: INWARD; b. perhaps Germanic derivative *werthaz, “toward, opposite,” hence “equiv- alent, worth,” in Old English weorth, worth, valuable, and derivative noun weorth, wierth, value: WORTH}; STALWART. 2. Germanic *werthan, to become (< “to turn into”), in Old English weorthan, to befall: worTH?. 3. Zero-grade form *wrt- in Germanic *wurth- in Old English wyrd, fate, destiny (< “that which befalls one”): WEIRD. 4, Latin vertere, to turn, with its frequentative versare, to turn, and passive versari, to stay, behave (< “to move around a place, frequent”): VERSATILE, VERSE}, VERSION, VERSUS, VERTEBRA, VERTEX, VERTIGO, VOR- TEX; ADVERSE, ANNIVERSARY, AVERT, BOULEVERSE- MENT, CONTROVERSY, (CONVERSE!), CONVERT, DEXTRORSE, DIVERT, EVERT, (EXTROVERSION), EXTRO- VERT, INTRORSE, INTROVERT, INVERT, MALVERSATION, OBVERT, PERVERT, PROSE, RETRORSE, REVERT, SINIS-
1237:AMBLYOPIA mel-1 AMBROSIA mer-2 AMBSACE ambho AMBULATE al-2 AMBUSCADE busk- AMBUSH busk- AMELIORATE mel-4 AMENABLE men-2 AMEND mend- AMENORRHEA mé-2 AMENT! = ap-1 AMENT2 men-1 AMETHYST medhu- AMIANTHUS mai-2 AMICABLE amma AMICE yé-
```


## [2026-09-04T19:30:35.631Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 21 22 23; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' IEC.txt | head -60; done",
 "description": "Print Mann IEC leaves 21-23"
}
```


### [2026-09-04T19:30:37.228Z] TOOL RESULT

```
=== leaf 21 ===
. áyas; Av. ayáh-; Lat. aes; Umb. ahes- (w. ‘false h); Go. aiz; ON eir; MHG er. (Note: J. Pokorny and others refer this word to Alasia (Ayasia), an ancient name of Cyprus)
ak “but, and” Lat. ac; W ac; OE ah
-ăk, -åkis, an adverbial extension Arm. cf. er-aki “trebly'; Gk. is-ákis ‘equally’; OCS inače ‘otherwise’; Cz. jin-ak, id.; Latv. péc-ak ‘afterwards’, labaki, labāk; cf. also trij-acis «three, at cards’.
akeros, akros, akrnos (a tree) ‘maple’, or sim. WP I, 28 Vedic akráb; Gk. ákarna "laurel; Lat. acer; OHG ahorn: Danish zr
akolos, akilos, aklos “point, spike, sting’. Cf. aKil-, aKul- OHG (ambig.) agal- in agal-stra (G. Elster); Li. aklys; Latv. aklis, beside akles, ak]i
akino ‘urge, incite’ W egni; ON egna; Li. akinu, akinti
akinos, à “berry; (?) shoot Lat. acinus; W egin; Li. akyna; cf. Cz. jeény ‘of barley
akl- (?) “ice? Alb. akull; ON éi- in él-kaldr
9 akmó(n), akmen- — akmo(n), aKmen-
akmó(n), akmen- ‘stone, boulder, crag’. WP I, 29, 33. Cf. aKmo(n)
OCS kamy, gs. kamene; Srb. kam, kamen; Li. akmuo, eps Latv. akmens
aknis (?) *point, tip'. Cf. aKnis
-akos, -àkos (diminutive suffix) Skt. -akah, -aka; Per. -ak; Arm. -ak; Alb. -ok; W og: OCS -akü; Li. -okas (in adjj.)
akotos (?okótos) ‘barb, spike’. Cf. aKotos. WP I, 32, 33 ` k Tokh. B. cf. akwatse (ambig.) ‘sharp, violent’; Li. akuotas; Latv. akots
akris, os “sharp; point. Cf. aKris. WP I, 28, 33 Arm. akir (i-stem and o-stem); Ir. acar, acaire
aksios, io (1) 'axe' Gk. cf. axine; Lat. ascia (The phonology of Go. aqizi, OE zx, eax, and æces, OHG ackus, acchus ‘axe’ is obscure); Li. jakšis, jekšis (LW, or IE?)
aksios (2) “like, equivalent, due, true, valid, right’. WP I, 36. Cf. aksulos Skt. aCChab; Av. a$0; Tokh. cf. asan; Kanic (name of a king at Kültepe) Kunut-ahsu- (cf. $nótos below); Arm. a£; Gk. áxios; MIr. aice, adj. ‘worth’; R cf. -oSij (in xor-ošij *good^). For OCS oxolü see aksulos, and for OCS oxvy see esus
akskis, os (?) “chip, splinter. Cf. ak-, aK-, skiio Lat. cf. assis, LLat. axis “board”, and popular Lat. asser beside ascla, astla, astula; W asg; Srb. (?) o$ce *window-pane' and o&cela, f. ‘chip’, but these may be cpds. with px. o-
aksos, ios, akslà (?) “die, dice’. Cf. akskis Skt. aksáh; cf. Lat. ala
akstin-, aKstin- “dart, shaft, spike, pike'. Cf. aKstin-, aKtis. WP IT, 338 Skt. cf. aktüh (1); Tokh. cf. asce “head, begin- ning’; Gk. aktin; Ir. aiteann, gs. aitinn ‘gorse’; W eithin, pl. aith; OCS astínü; Li. ãkstinas ‘goad’, beside akstis, akštis ‘spit, lance’; Latv. aste ‘tail’
aksulos, aksəlos (oks-?) ‘bold, proud’. Cf. aksios (2). Arm. ağoy ‘able’; MIr. ocol, occol (for *acol, *accol? ‘bold, vehement": OCS oxolü, Srb. ohol ‘prouď’; cf. OCz. ochle ‘honour, worship’ or sim.)
20
25
30
35
40
45
10
akus ‘point’. Cf. aKus. WP I, 31, 33 Av. akus; Lat. acus
aKa ‘keenness, sharpness’. WP I, 32. Cf. akis Av. asa; Gk. ake
akeio ‘sharpen; be sharp’. WP I, 32 Gk. cf. akázo; Lat. aceo; OE eggian; ON eggja Å
aker- (9), aKor- (?) (a fish) ‘perch’. Cf. oKris Li. aSerys; Latv. asaris. (See Hellquist: SEO: abborre)
akokà, aKokà, io ‘thorn, spike’. WP I, 32 Gk. akokë Lat. (Pliny) acacia; R osóka ‘sedge’; Li. aSsakà ‘fishbone’; Latv. asaka
aKolos, see aKilos, aKulos
aKonos, à, is, io ‘spike, awn’. WP I, 30. Cf. aKnis Skt. asánih; Av. asan; Arm. cf. hesan ^whet- stone', appar, from a type *epi-aKon-; Gk. ákano
=== leaf 22 ===
s, ákaina, cf. also ákon; Lat. cf. agna (*ear of corn', phonology of dignus, segmen, etc); Go. ahana beside OHG agana; Latv. asns ‘bud’; cf. Finn. LW akana ‘husk, glume’
aKərā, aKru ‘teardrop’. Cf. dakru. WP I, 769 Skt. ásru; Av. asru; Per. ašk; Tokh. A ākär, pl. akrunt; Li. ášara; Latv. asara
akii- “point, tip’. Cf. akis, etc. Lat. aciës; OCS osije
akilos, aKolos, à, us “point, barb; whetstone’. WP I, 29. Cf. aKulos, oK- Arm. aseyn; W agalen; OHG ahil; G Achel, Agle, Aile; WG Agel; LG ailen, pl. ‘awns’; OE egl ‘awn; claw’; OCS osla, osíla ‘awn’. Cf. OBr. ocol- (for *acol-?) ‘whetstone’
akis, aki- ‘point, tip’. WP I, 32. Cf. aKus Gk. akis; áke; Lat. acies; MIr. aicce ‘little needle’; W cf. egfaen ‘haw’; Br. ék “point, spike’; ON ax; egg, pl.-jar; OHG egga, ecka; OE ecg; R osí ‘tips of fur beside OCS osije “ear of corn’; Srb. osje ‘awns’
aKmā, is, os ‘point, pimple’ Gk. akmé; OE ome ‘rash’
akKmo(n), aKmen- ‘crag, boulder’. WP I, 29, 33 Skt. a$man; Av. asman; Gk. ákmon; Li. aš- muo, -efis ‘cutting-edge’; Latv. asmens, id. (Gk. ákmon is ambiguous, see akmo(n))
11 aknis, os, à — aktros, aKstros, à 12
aknis, os, a ‘tip, point, awn’. WP I, 30. See akonis Vedic a$nah ‘stone’; Lat. agna (‘ear of com", Fest. For *acna, cf. -g- for -c- in segmen, signum, dignus, etc.); ON ogn, pl. agnar, agnir (sg. fr. *aknüs); cf. egna ‘provoke’; OE ægnan, pl.; Li. (Zemaità) a£nis ‘cutting-edge’; Latv. asns ‘shoot, sprout
aknu-mi ‘cheer up, be spirited’ Skt. (ambig.) a$nomi (2) “enjoy” (cf. eK-); Arm. c-asnum ‘flare up, be angry) (*eKs-aKnumi); Go. cf. aha, ahjan “mind, to think', ahma ‘spirit’
akoka, see aKəkå
akón- ‘stone; whetstone’. WP 1, 30. Cf. akən-, Kön- Skt. asan; asánih; OPer. asa, asan-; Av. asa- nam, acc.; Per. san; Oss. sson, Dig. insoinä; Arm. cf. h-esan (*epi-akKon-?) ‘whetstone’; Gk. akóne, beside ákon, -ontos; Gaul. acaunum, pl. acona (-au- for -o-) *whetstone?
aKos, -es- ‘barb, tip, point, spot. WP I, 30 Av. aso, n. ‘place’; Lat. acus, -eris ‘chaff; Go. ahs; Sw. ax; Latv. cf. ass, adj. ‘sharp’. Cf. aKus, aKis
aKotos ‘barb, prickle’. WP I, 32, 33. Cf. ako- tos, aKutos Tokh. B (ambig.) akwatse ‘sharp, violent; Lat. cf. cos, cotis; Slovene osát ‘thistle’; Cz. oset ‘prickle’; R osot ‘thistle’? (fr. akutos); Li. aëuote 'esparto-grass'
akris, os “point, tip, edge’; pointed, sharp’. WP I, 28. Cf. okris Skt. (ambig.) asrih (*ak- or *ok-); Hitt. cf. hekur (summit. Vocalism obscure); Gk. ákris; ákros; Lat. cf. acer, gs. ácris; Umb. akru-tu (abl.sg. ‘from the beginning"). Osc. akri-d ‘from the top’; Olr. achar, aicher *bit- ter”; aichre ‘fury’; achaire ‘sharpness’; W egr ‘sharp, sour; OE zhher, ear of corn’: OHG ahar, ahir, n. id. (MHG eher: G Aehre); Pol. (ambig.) ostrze 'knife-edge'. See aKtros
akris, os “keen, swift. WP I, 28. See akris Lat. áàcer; OBr. ar-ocrion, adj. pl. ‘fierce’ (but see óK-); OCS cf. jastr-ebü (a cpd. = “hawk?)
aKru ‘teardrop’. See aKora, daKru. WP I, 769
aksilà, io (axle; shoulder. WP I, 37 Lat. ala ‘wing’, axilla ‘armpit; MIr. aicell
20
25
‘axle’; Gael. aiseal, id. (but Olr. achsal “arm- pit is a Latin LW), W echel; Br. ael; Cor. eghel, id., OHG ahsala; OS ahsla; OE eaxl; ON oxl ‘shoulder’ beside ON oxull ‘axle’; Finn. LW akseli, id.
aksinà 'awn, husk’ W eisin, ‘bran, husks’; Cz. osina ‘barb, awn’
aksis, -ó(n) ‘axle, axis, pivot. WP I, 37 Skt. áksah; Myc. akosone (*aksones, pl.); Gk. áxon; Lat. axis, g.p. axium (fLat. axis, as also Gk. áxon are from ago)” — Ainsworth 1736); MIr. ais; OE eax; OHG ahsa; Du. as; LG ass
=== leaf 23 ===
, pl. en OCS ost Li. ašis, gp. aSiü, m. & f.; Latv. ass, gs. ass, gp. asu ‘axle’
āKsos (? oKsos) ‘keen, sharp, clear; keen- ness, etc? W awch ‘edge, keenness’; Cz. jas ‘clarity’; cf. the synthetic OCS cpd. jastrebü ‘hawk’, with part of the semantics of Lat. accipiter, id. The Lat. form ascia and It. azza indicate a short vowel. `
akstin-, akstin- ‘point, prickle, dart, shaft, spike, pike, spit’. WP H, 338 Tokh. asce “head, beginning’; Gk. aktin; MIr. aittenn, Ir. aiteann ‘furze’, Gallo-Lat. atinia ‘ulmus gallica; OBr. ethin “rushes'; MW eithyn 'trampium'; W eithin, pl. aith ‘furze’;
' eithen ‘point, prickle’; Cor. eythynen ‘furze’;
30
35
40
45
eythen ‘prickle’; MHG este, obl. esten 'foot- hil’; OCS ostínü ‘spike, goad'; OCzech osten ‘goad’, Cz. ‘sting, prickle’; Li. ákstinas ‘goad’ beside akstis, akštis ‘spit, lance’; Latv. aste ‘tail
akstros, see aKtros
aktis “point, prickle, shaft, WP I, 443. Cf. aKstin-, aKtros Gk. aktís beside aktin; Alb. i athët ‘sharp, tart; W aeth, pl. eith; R osti 'awn'; Cz. ost, Slovene ost ‘sting, prickle’; ‘Srb. osti, pl. beside ostve ‘harpoon’; Ukr. osti ‘fishbone’; Latv. aste Cal fr. *aktiə). For R osot, see aKutos
aktós, pp. see ago Lat. actus; Umb. aht-; cf. Lat. actor: Gk. áktor; W aeth "he has gone"; (Ir. acht ‘law’ is a LW fr. Lat.)
aktros, aKstros, à “sharp; sharpness, point. WP I, 28. Cf. aKris
13 aKulos, ios, à — alouos 14
Skt. astra (*goad', fr. *aKtrio); Av. astra; Tokh. astar, astare and astre ‘clear, bright"; OCS ostrü ‘sharp’; ostrije ‘cutting-edge’; OCz. ostrev (fr. *-üs ‘barbed pole’); Li. aštrūs “se- vere’; Latv. astrs ‘horsehair
aKulos, ios, à ‘barb, awl’. WP I, 29. Cf. aKi- los, aKus Skt. a$ula 'vitex alata; Gk. ákulos “holm acorn'; Alb. éhull, éfull ‘icicle’; Lat. aculeus; cf. nov-acula (see ksneu-); W ebill *gimlet'; OBr. epill; Br. ebil ‘peg, pin’; OE awel, awel, awol; cf. ON -áll (in sóó-áll "book: (Icel. alur ‘awl is ambiguous, see gl) For OCS osla, see akilos
áKus ‘sharp; point. WP I, 33. Cf. óK- and cpds. of aK- above Av. (ambig.) asus (see oK-); Oss. cf. äfsän *plowshare', áfsáinag ('iron'. Cpds. áfsán-, id. Omitted from Abaev: IESOJa, I); Hes. ekés; Alb. eh ‘cutting-edge’; Lat. acus; OE agu (?) See Kluge EWDS, 17: Elster); Slovene ostva ‘harpoon’; Srb. ostve, ostava
aKutos ‘barb, spike, bristle’. Cf. aKtis, aKó- tos . Lat. cf. acütus (fr. acuére); OCS osütü; R osot; Cz. oset ‘briar, thistle; barb’
aKua (?) “water; running water’ (aqua?). WP I, 34, 35 Skt. river-names in a$va-: -rathā, -parni: (?) Gk. asa-, -assa (in asáminthos, thál-assa. Speculations in Bois. DELG); Go. ahva ‘river’; OE ea; ON ọ (speculations with lit. in Feist: VWGS)
al- ‘wander, go’. Cf. al-eió Gk. aláomai; LLat. alare (or alar) "bunt, cpd. in amb-ulàre, simplex in OFr. aler. (The LL wd. is given by Servius, 4th.cent. AD in the form aiator “hunter”) h
alalos, à ‘babble, hubbub; obstreperous’. WP I, 89 Skt. alalah; Arm. dim. ayayak; Gk. alalë; Li. cf. alasas
albhedis ‘swan’. WP I, 93. Cf. albhos OHG albizz; ON álpt, elptr; OE ielfetu; G Eibs; OCS lebedi
albhis “white; white substance, white corr. WP I, 92. Cf. albhos Gk. álphi, álphiton *barley-flour; Alb. elb
15
20
25
30
35
40
45
‘barley’; Lat. cf. albi-tüdo; Ir. ailbh ‘flock’; W cf. elfed ‘autumn’; Gmc. cf. Alpes (CAlps' — *white mountains' accdg. to Fest. Alemannic p for general Gmc. b)
albhos ‘white’. WP I, 92. Cf. albhis Hitt. alpas (cloud; Gk. alphós; Lat. albus; Umb. alf-; Gaul. albo-; Ir. cf. ailbh ‘flock
aldh-(?) (Most
```


## [2026-09-04T19:30:44.775Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==23' IEC.txt | tail -40; echo \"=== leaf 24 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==24' IEC.txt | head -50",
 "description": "Print IEC leaves 23-24 fully"
}
```


### [2026-09-04T19:30:46.588Z] TOOL RESULT

```
, pl. en OCS ost Li. ašis, gp. aSiü, m. & f.; Latv. ass, gs. ass, gp. asu ‘axle’
āKsos (? oKsos) ‘keen, sharp, clear; keen- ness, etc? W awch ‘edge, keenness’; Cz. jas ‘clarity’; cf. the synthetic OCS cpd. jastrebü ‘hawk’, with part of the semantics of Lat. accipiter, id. The Lat. form ascia and It. azza indicate a short vowel. `
akstin-, akstin- ‘point, prickle, dart, shaft, spike, pike, spit’. WP H, 338 Tokh. asce “head, beginning’; Gk. aktin; MIr. aittenn, Ir. aiteann ‘furze’, Gallo-Lat. atinia ‘ulmus gallica; OBr. ethin “rushes'; MW eithyn 'trampium'; W eithin, pl. aith ‘furze’;
' eithen ‘point, prickle’; Cor. eythynen ‘furze’;
30
35
40
45
eythen ‘prickle’; MHG este, obl. esten 'foot- hil’; OCS ostínü ‘spike, goad'; OCzech osten ‘goad’, Cz. ‘sting, prickle’; Li. ákstinas ‘goad’ beside akstis, akštis ‘spit, lance’; Latv. aste ‘tail
akstros, see aKtros
aktis “point, prickle, shaft, WP I, 443. Cf. aKstin-, aKtros Gk. aktís beside aktin; Alb. i athët ‘sharp, tart; W aeth, pl. eith; R osti 'awn'; Cz. ost, Slovene ost ‘sting, prickle’; ‘Srb. osti, pl. beside ostve ‘harpoon’; Ukr. osti ‘fishbone’; Latv. aste Cal fr. *aktiə). For R osot, see aKutos
aktós, pp. see ago Lat. actus; Umb. aht-; cf. Lat. actor: Gk. áktor; W aeth "he has gone"; (Ir. acht ‘law’ is a LW fr. Lat.)
aktros, aKstros, à “sharp; sharpness, point. WP I, 28. Cf. aKris
13 aKulos, ios, à — alouos 14
Skt. astra (*goad', fr. *aKtrio); Av. astra; Tokh. astar, astare and astre ‘clear, bright"; OCS ostrü ‘sharp’; ostrije ‘cutting-edge’; OCz. ostrev (fr. *-üs ‘barbed pole’); Li. aštrūs “se- vere’; Latv. astrs ‘horsehair
aKulos, ios, à ‘barb, awl’. WP I, 29. Cf. aKi- los, aKus Skt. a$ula 'vitex alata; Gk. ákulos “holm acorn'; Alb. éhull, éfull ‘icicle’; Lat. aculeus; cf. nov-acula (see ksneu-); W ebill *gimlet'; OBr. epill; Br. ebil ‘peg, pin’; OE awel, awel, awol; cf. ON -áll (in sóó-áll "book: (Icel. alur ‘awl is ambiguous, see gl) For OCS osla, see akilos
áKus ‘sharp; point. WP I, 33. Cf. óK- and cpds. of aK- above Av. (ambig.) asus (see oK-); Oss. cf. äfsän *plowshare', áfsáinag ('iron'. Cpds. áfsán-, id. Omitted from Abaev: IESOJa, I); Hes. ekés; Alb. eh ‘cutting-edge’; Lat. acus; OE agu (?) See Kluge EWDS, 17: Elster); Slovene ostva ‘harpoon’; Srb. ostve, ostava
aKutos ‘barb, spike, bristle’. Cf. aKtis, aKó- tos . Lat. cf. acütus (fr. acuére); OCS osütü; R osot; Cz. oset ‘briar, thistle; barb’
aKua (?) “water; running water’ (aqua?). WP I, 34, 35 Skt. river-names in a$va-: -rathā, -parni: (?) Gk. asa-, -assa (in asáminthos, thál-assa. Speculations in Bois. DELG); Go. ahva ‘river’; OE ea; ON ọ (speculations with lit. in Feist: VWGS)
al- ‘wander, go’. Cf. al-eió Gk. aláomai; LLat. alare (or alar) "bunt, cpd. in amb-ulàre, simplex in OFr. aler. (The LL wd. is given by Servius, 4th.cent. AD in the form aiator “hunter”) h
alalos, à ‘babble, hubbub; obstreperous’. WP I, 89 Skt. alalah; Arm. dim. ayayak; Gk. alalë; Li. cf. alasas
albhedis ‘swan’. WP I, 93. Cf. albhos OHG albizz; ON álpt, elptr; OE ielfetu; G Eibs; OCS lebedi
albhis “white; white substance, white corr. WP I, 92. Cf. albhos Gk. álphi, álphiton *barley-flour; Alb. elb
15
20
25
30
35
40
45
‘barley’; Lat. cf. albi-tüdo; Ir. ailbh ‘flock’; W cf. elfed ‘autumn’; Gmc. cf. Alpes (CAlps' — *white mountains' accdg. to Fest. Alemannic p for general Gmc. b)
albhos ‘white’. WP I, 92. Cf. albhis Hitt. alpas (cloud; Gk. alphós; Lat. albus; Umb. alf-; Gaul. albo-; Ir. cf. ailbh ‘flock
aldh-(?) (Most
=== leaf 24 ===
 of the evidence is ambigu- ous. For Gk. *álthomai, althaino, álthos — omitted by Bois. and Hof. — see uldh-; íor Holth. the Gk. forms equate with ON aldinn, aldin ‘fruit’. Cf. also uoldh-)
ale$-(?), al$-(?) “sorrow, suffering’. Cf. WP I, 160; II, 423 note. Cf. alg-, sulg-. Oss. älğ (ambig.) “nausea”. (For speculations see Bois: alégo, etc., and WH & EM: neg- ligo, diligo)
aleio “grind, pound, crush'. Cf. aleuro- Hind.Beng. cf. ata, Guj. ato, Romani arno, andro, aro; Per. ard (ambig. “flour”, perhaps to Gk. ártos “bread”. Bois. and Hof. uncertain); Arm. ayam ‘grind’; Gk. aléo, v., aletós, s. Cf. Myc. (queried) aletere-, pl. *millers'
áleið, al- ‘rove, roam’. Cf. aleuos Per. cf. àv-ara, cpd. adj. ‘wandering’; Gk. &lásko, elaíno (Dor.-à-), beside áláomai; Lat. cf. the synthetic cpd. (apparently with an aph- etic px.) p-àlor, palari ‘wander’. Cf. for the px. pono, positum; pars: ars; parco: arx; pudeo (for *po-uideo “look down (?), w. the semantics of R po-zor); Latv. aleties *be rest- less
aleks-, alks- "ward off, protect. WP I, 89. Cf. alkos Skt. raksami; Arm. ayxem ‘bolt, bar; Myc. & Gk. aléxo, alexéo
aleur- (aleuor-) *millings, flour. Cf. aleió Arm. aliwr, aler, -erb; Gk. áleuron, áleiar
aleuos ‘wandering, restless, raving’. Cf. áleið Per. cf. av-ara ‘wandering’; Gk. eleós; Latv. alava ‘restless cow’. (For OCS jalovü "bar. ren’, see iel- in Suppt.)
alonis, see elonis
aleuos "dark: dark substance’. PW I, 159; II, 386; II, 442. Cf. elouos, olouos Hitt. cf. halluwas "deen": Gk. alaós "dark blind, dead": OHG cf. ëlo, gs. élawes ‘yellow’; OCS (ambig.) olovo “lead — metal’; Li. álvas,
 
15 algà — ald 16
id.; Latv. alvs, alva ‘tin’. (A possible cpd. in Lat. palleo, pallidus, fr. *p-alu- is uncertain)
algà (?) “a rambling plant’. See alga Lat. (ambig.) alga ‘seaweed’; Li. alga speed. well
algeið (?al8-) ‘suffer’. Cf. ale-, sulĝ-. Gk. (ambig.) aigéo; Lat. algeo; Fris. alkje ‘whine, shout
alguhos, à “profit, wealth, value, wage’. WP I, 92 Skt. argháh; Av. arojo; Per. arz, arj; Oss. ar£, pl. ärğtä; Hitt. (queried) halkw-essar "offer. ing'?; Myc. cf. name Aqato- (*Alqwhastos = Alphéstos); Gk. alphé; Li. algà. (The form of W elw, pl.- oedd “profit, goods’ is obscure. Perh. a crossing of *alguh- and *selu, q. v.)
alga ^a rambling plant, tangle’. Cf. WP I, 153, and alga above Per. raz ‘vine’; Lat. (ambig.) alga; G Alche *short-stemmed vetch or sim. plant’; OCS loza ‘vine’
aliksa (Slavonic type-variant of al?sos, ios, q.v.)
alitós ‘reared, grown; growth’. WP I, 86. See alo Lat. alitus; ON eldr ‘grown old
alio “but, yet'. WP I, 85. Cf. alios Arm. ajl; Gk. allá; Go. alja; ON ella; Cz. Pol. cf. ale (*a-alio)
alio-alio- "each other, one another'. WP I, 85. Cf. alios Arm. cf. ajlajla-ser “of different kinds”; aj-
lajlem "alter": Gk. allelous; MIr. alaile, araile ‘the alternative’; OBr. leill, id.; W lall, pl.
lleill, beside arali, pl. ereill
alio-ĝen, -gn- "of other origin, foreign’. Cf. alios Arm. ajlazan; Gk. cf. allogenës; Lat. alienus (loss of -g- as in maior. WH untenable); Go. aljakuns. For the zero-grade of the second element in Arm. and Go. cf. Gk. neo-gnós and Lat. privi-gnus, W gan, cf. also ail-enu “be born again”
alios "other WP I, 85 Tokh. cf. alàn ‘otherwise’; Arm. ajl; Gk. ál- los; Lat. alius: Osc. allo-; MIr. aile, aili-; Ir. eile beside all; Gaul. allo- beside alla "else, where’; W a
```


## [2026-09-04T19:31:07.805Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HRN\"; grep -n \"âvâre\\|avâre\\|āvāra\\|avara\\|âvârä\\|awâra\\|awāra\" HRN.txt | head -20; echo \"### HUB\"; grep -n \"avara\\|āvāra\\|avâre\\|awara\" HUB.txt | head -20; echo \"### CHEUNG\"; grep -n -i \"āwāra\\|avāra\\|avara\" CHEUNG.txt | head -20; echo \"### PHD\"; grep -n -i \"wʾlk\\|āwārag\\|awarag\\|ʾwʾlk\" PHD.txt PHD_mackenzie.txt | head -20",
 "description": "Grep Iranian refs for avara"
}
```


### [2026-09-04T19:31:07.889Z] TOOL RESULT

```
### HRN
1576:ap. *avaranga- oder wohl besser '^abiranga- (vergl.
5067:Erklärung von np. dwar 'Mauer aus ap. '^didavara-
5871:egel', echt zavara\ bei. zaray (417).
7164:Die Bedeutung von aw. fravara- ist unsicher (wie
7166:setzt ein ^fravarana- mit gleicher oder ähnlicher Be-
10533:gadavara-).
14641:gaSavara- 1073.
20114:I zavara 664.
### HUB
114:aus avarad *bringt* halten), wenn das Wort nicht are
2276:599. Besser *daidavara- (Fe&tungBmsiuer*)^) Sils *daigavara-
2986:823. Xp. farrar deckt sich lautlich ganz mit zd. fravara-^
4266:tavor (wie lus-avor etc.), ap. ^databara- (= ^datawara-) ;
5033:bereta-j skr. bhrta- (dazu Uvurdafiy avaram = aram 'bringe') ;
5958:*Karazm Si\xs*karaztn = zd. kavarasmD (gen. sg.), Darme-
5979:patina testacea = arm. skavarak ^Schiisser; np. fordiydn
6011:ganjur (skr. ganjavara-), dastUr = paz. dastur,
7980:Firdusi (fur *Karazm) = zd. kavarasmo (gen. sg.), Dar-
### CHEUNG
9418:Klein 1988: 412, fn. 53. The hapax form "avaharda is very similar to avarada 
19399:forms to Gr. niAvaraı (intr.) ‘approaches’, on account of its formal similarity. 
21158:*OLD PERSIAN: (+ *aua-) avarad- ‘to leave, abandon’. Ф See most recently R. Schmitt 
21161:Pres. them.: INJ. 2sg. avarada <a-v-r-d> (DNa 60) 
34014:avarad-, 322 
54383:riAvaraı, 294 
### PHD
```


## [2026-09-04T19:31:10.012Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### MON_part1\"; grep -n \"آواره\" MON_part1.txt | head -10; echo \"### MON_part2\"; grep -n \"آواره\" MON_part2.txt | head -10; echo \"### BQT_v1\"; grep -n \"آواره\" BQT_v1.txt BQT_alt_v1.txt | head -10; echo \"### ARY\"; grep -n \"آواره\" incoming/ARY/ARY_pages.txt | head -10; echo \"### ARY latin\"; grep -n -i \"avare\\|AVAREH\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Grep Persian dictionaries for آواره"
}
```


### [2026-09-04T19:31:10.146Z] TOOL RESULT

```
### MON_part1
5161:اوار؛ 1 ([- آواره] (ص.) از خانمان و 
5171:آوارگسی: 2۷2728 (حامص. آواره) 
5175:آواره: ()2:2 (- آوار] (ص.) از وطسن 
48107:دادن. (مصل.) آواره شدن؛ جلاء وطن. 
55252:بی‌خانمان» آواره.‎ 
60183:خانه و خاندان خود آواره شده؛ بی‌خانمان» 
60184:آواره» سرگردان؛ خانه بد و ش. 
77296:متحیر. آواره» دربدر. 
77317:حیران. آواره؛ درندر. 
90783:ضال: (731)1 [ع.] رافا.) گمراه؛» ببر ۵. آواره؛ 
### MON_part2
26448:کم‌بخت» بیدولت. آواره» س رگشته. کافر» 
87366:رن ۵۶9 : هرزه گرد» آواره» بیجا و 
89570:جا قرار نگیرد» آواره» سرگردان. آنکه هر 
### BQT_v1
BQT_v1.txt:15586:] مارم ۱ بروژن و معثی آواره - آموخته است ۵ . # 
BQT_v1.txt:16150:آواد » بر وزن ناچار . مخذف آواره 
BQT_v1.txt:16164:حساپ کننده و محاسب را آواره گیر گوشد ‏ 
BQT_v1.txt:16184:.رکه اولز . ۴ .. * آمار » آهاره » آواره » آمازد : اوارجه . 
BQT_v1.txt:16185:۴ ودفتر حساب : بی‌دیرنمانده است که مك ملعانرا آرند بدیوان نوآواره و دفتر 
BQT_v1.txt:28492:۵ رك , ص: به . ۱ ول : آوا . ۷ - رک : آواره وآهار . 
BQT_v1.txt:28493:۸ رد۵ : آواره و آمار . ۸ رك : اوار  .‏ *9 رك : وام . ٩‏ رگ : فلم. 
BQT_v1.txt:50542:باشد کسی را از جابی ودفع تمودن - و آواره 
BQT_alt_v1.txt:12597:آساده ت بروزن آواره ۰ بمعئی حساب 
BQT_alt_v1.txt:14187:آماره ۲ « بروزن و ممثی آواره - 
### ARY
### ARY latin
```


## [2026-09-04T19:31:14.559Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5150,5185p' MON_part1.txt",
 "description": "Print Mo'in context for آوار/آواره"
}
```


### [2026-09-04T19:31:14.609Z] TOOL RESULT

```
آوا: 3 [- آواز] (ا.) آواز» بانگه» ضوت: 
(مت.) آواز . صبت» شهرت. عقیده» رأی. 
آوای سرد: گفتار زشت. 

اواخ: »2:2 [- آوخ] (صت.) آوخ. (.) آوای 


نرم» صوت خفی. قسمت» نصیب 


اوار؛ 1 ([- آواره] (ص.) از خانمان و 
وطن به دور افتاده» در به در. خراب؛ ویران؛ 
برافتاده. (ا.) هرج و مرج» بی‌نطمی» فساد. 
آزار» رنج. غارت» چپاول. 

آوار؛ ۲(.) گرد و غبار و خاکك. آنجه به 
سب افتادن دیوار و سقف فرو ربزد از 
خاک و نگ آجر و گچ و غیره. 

آوار: 15 [- - آور ] (.) یقین» آور. 
آوارگسی: 2۷2728 (حامص. آواره) 
بسی‌خانمانی» بسی‌منزلی» دورافستادگی از 
خانمان. سرگردانی؛ بر یشانی. 

آواره: ()2:2 (- آوار] (ص.) از وطسن 
دور افتاده» در به در. گم گردیده» بی‌نام و 
نشان . گر بخته. برا کنده» بر شان» متفرق. (.) 


ظلم یج آزار. 


آواز فرهنگ فارسی معین 1۷
```


## [2026-09-04T19:31:15.507Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"آواره\" BQT_v1_pages.txt | head -20; echo \"---- dli\"; grep -n \"آواره\" BQT_dli_part1.txt | head -20",
 "description": "Grep BQT pages for آواره"
}
```


### [2026-09-04T19:31:15.576Z] TOOL RESULT

```
8728:] مارم ۱ بروژن و معثی آواره - آموخته است ۵ . #
8972:آواد » بر وزن ناچار . مخذف آواره
8981:حساپ کننده و محاسب را آواره گیر گوشد ‏
8991:.رکه اولز . ۴ .. * آمار » آهاره » آواره » آمازد : اوارجه .
8992:۴ ودفتر حساب : بی‌دیرنمانده است که مك ملعانرا آرند بدیوان نوآواره و دفتر
14742:۵ رك , ص: به . ۱ ول : آوا . ۷ - رک : آواره وآهار .
14743:۸ رد۵ : آواره و آمار . ۸ رك : اوار  .‏ *9 رك : وام . ٩‏ رگ : فلم.
25021:باشد کسی را از جابی ودفع تمودن - و آواره
---- dli
```


## [2026-09-04T19:31:29.990Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW ambulo\"; grep -n \"ambulo\\|ambulare\\|ambulō\" LEW_1910.txt | head -20; echo \"=== LEW exsul\"; grep -n \"exsul\\|exul\" LEW_1910.txt | head -20; echo \"=== LAT ambulo\"; grep -n \"ambulō\\|ambulo,\\|ambulare\" LAT.txt | head -20; echo \"=== LAT exsul\"; grep -n \"exsul\\|exul,\" LAT.txt | head -20",
 "description": "Grep Latin etymological dictionaries"
}
```


### [2026-09-04T19:31:30.087Z] TOOL RESULT

```
=== LEW ambulo
=== LEW exsul
=== LAT ambulo
2035:ambulare?'. Ager est premier terme de compose dans agricola, etc.,
3184:udles, ambegni,ambedo, ambiguus, ambio, ambulo, anburbiales, ambustus;
3284:ambulo, -as, -&ul, -atum, -are: compos 4 ayant pour premier terne
15912:et aaee: dealbo M.L.3488a, deambulo, deauro (M.L.3489), derelinquo
=== LAT exsul
19744:exui, exsul, -lis c.: exile. Ancien, usuel; iri.esui.
19751:rati atque impii quos leges exsilio affici uolunt, exsules sunt, etiamsi
19754:sianus de Pl., Tri.535. Mais si on lit exsul dans les ass., les inscrip-
25502:et effuse animus exsultat, tum illa laetitia gestiens uel nimia dici
31954:3 *joie, gait<?: - dicitur exsultatio quaedam animi gaudio efferuentior
45894:ans Lucr.3,141 hic exsultat enim pauor ac metus. Le genre animi du
47031:ab Argis iam dudum exsulo ". D'oi repudiS,-ds : rejeter, rApndier
59139:Pour exsul, r. ce mot.
64133:-torris dans extorris (= exsul) adj. avec vocalisme o ancien dans
```


## [2026-09-04T19:31:31.560Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN alley\"; grep -n \"^alley\\|alley, n\\|amble, \\|ambulate\\|preamble\" KLN_1966.txt | head -20; echo \"=== KLN exile\"; grep -n \"exile,\" KLN_1966.txt | head -10; echo \"=== SKT\"; grep -n -i \"^ALLEY\\|ALLEY, \\|AMBLE\\|EXILE\" SKT.txt | head -20",
 "description": "Grep Klein and Skeat"
}
```


### [2026-09-04T19:31:31.659Z] TOOL RESULT

```
=== KLN alley
2269:alley,  n.,  a  narrow  passage.  —  OF.  alee  (F.  allee), ‘a  going,  passage’,  prop.  fem.  pp.  of  OF.  aler (F.  alter),  ‘to  go’,  fr.  L.  ambuldre,  ‘to  go,  walk’. See  amble  and  cp.  purlieu.
2437:amble,  intr.  v.,  to  go  at  an  easy  gait.  —  ME.,  fr. OF.  ambler,  fr.  L.  ambulare,  ‘to  go  about,  walk’, which  prob.  stands  for  *amb-al-are,  fr.  amb- (see  amb-)  and  I.-E.  base  *61-,  ‘to  go’,  whence also  Gk.  & M,  ‘ceaseless  roaming’,  aXac&aa, aXatvav,  ‘to  wander  about’,  aXy]-rr)<;,  ‘beggar’, Lett,  aluot,  ‘to  wander  about’,  L.  aliicinari,  ‘to wander  in  mind’.  See  hallucinate  and  cp.  am¬ bulance,  ambulate,  funambulist,  noctambulism, somnambulism.  Cp.  also  Alastor,  aleatory,  Aleo- chara,  alley,  ‘a  narrow  passage’,  exile,  purlieu. Derivatives:  amble,  n.,  amble-ing,  adj. amble,  n.,  an  easy  gait.  —  ME.,  fr.  F.  amble,  fr.
2438:OF.  ambler.  See  amble,  v. ambly-,  combining  form  meaning  ‘blunt’.  —  Gk. dmfiXu-,  fr.  dtupXu;,  ‘dull,  blunt,  dim’,  which prob.  stands  for  *i-\x>.-bc,  and  is  rel.  to  paXa- x6g,  soft’.  See  malaco-  and  cp.  amalgam,  Amal- thea.
2446:ambry,  n.,  cupboard;  closet  (archaic).  —  ME.  al- mary,  aumbry,  fr.  OF.  almarie,  armarie  (F.  ar- moire),  ‘cupboard’,  fr.  L.  armarium,  ‘closet, chest’,  lit.  ‘a  place  where  arms  are  kept’,  fr.  arma, gen.  armorum,  ‘arms;  tools,  instruments,  uten¬ sils’.  Cp.  It.  and  Sp.  armario,  OProveng.  armari, and  see  arm,  ‘weapon’,  armory, ambsace,  n.,  double  aces.  —  OF.  ambes  as,  fr.  L. ambas,  fern.  acc.  of  ambo,  ‘both’,  and  L.  as, ‘unity,  unit’.  See  ambi-  and  ace. ambulance,  n.  — -  F.,  fr.  earlier  hopital  ambulant lit.  ‘a  walking  hospital’,  fr.  L.  ambulans  gen. -antis.  See  next  word  and  -ce. ambulant,  adj.  —  L.  ambulans,  gen.  -antis,  pres, part,  of  ambulare.  See  next  word  and  -ant. ambulate,  intr.  v.,  to  move  about,  walk.  —  L. ambulat-(um),  pp.  stem  of  ambulare,  ‘to  go about,  walk’.  See  amble  and  verbal  suff.  -ate and  cp.  circumambulate,  perambulate, ambulation,  n.  —  L.  ambulatio,  gen.  -onis,  fr.  am- bulat-(um),  pp.  stem  of  ambulare.  See  prec. word  and  -ion.
5527:Bramah  press.  —  Named  after  its  inventor,  the English  mechanician  Joseph  Bramah, bramble,  n.  —  ME.  brembil,  fr.  OE.  brxmbel, brembel,  fr.  earlier  brxmel,  bremel  (the  second
5656:brim,  n.  —  ME.  brimme,  brim,  rel.  to  ON.  barmr, MHG.  brem,  ‘bordering  edging’.  Late  MHG. verbremen,  G.  verbrdmen,  ‘to  border,  edge’, OHG.  bramberi,  MHG.  bramber,  G.  Brom- heere,  ‘bramble,  blackberry’,  OE.  brom,  ‘broom’. All  these  words  are  derivatives  of  I.-E.  base *bhre-m-,  ‘edge,  point;  to  bore,  pierce’,  an  en¬ largement  of  base  *bher-,  of  s.m.,  whence  berm, board,  ‘table’,  board  ‘side  of  a  ship’,  bramble, broom.
5721:broom,  n.  —  ME.  brome,  fr.  OE,  brom,  rel.  to  Du. braam,  ‘blackberry’,  OHG.  brdma,  bramo,  MHG. brume,  ‘broom  (the  plant)’,  OHG.  brdmberi, MHG.  bramber,  G.  Brombeere,  ‘blackberry’; fr.  I.-E.  base  *bher-,  ‘point,  edge;  to  cut  with  a sharp  point,  to  bore,  pierce’.  See  bore,  ‘to  pierce’, and  cp.  bramble,  bream,  v.,  brim.  For  the  sense development  of  broom  cp.  brush,  scrub. Derivatives:  broom,  tr.  v.,  broom-er,  n.,  broom- y,  adj.
7719:circum-,  pref.  meaning  ‘around,  all  around, about’.  —  L.,  ‘around,  about’,  lit.  ‘in  a  circle’, adv.  acc.  of  circus,  ‘ring’.  See  circus, circumambience,  circumambiency,  n.  —  Formed fr.  next  word  with  suff.  -ce,  resp.  -cy. circumambient,  adj.,  going  round,  surrounding. —  Compounded  of  circum-,  and  ambient, circumambulate,  tr.  and  intr.  v.  —  L.  circum- ambulatus,  pp.  of  circumambuldre,  ‘to  walk around’,  fr.  circum-  and  ambulare,  ‘to  walk’. See  ambulate,  amble.
14219:extraterritorial,  adj.,  exterritorial.  —  Formed  fr. extra-  and  territorial.  Cp.  exterritorial. Derivative:  extraterritorial-ity,  n. extravagance,  extravagancy,  n.  —  F.  extra¬ vagance,  fr.  extravagant.  See  next  word  and  -ce, resp.  -cy,  and  cp.  extravaganza, extravagant,  adj.,  prodigal,  wasteful.,  n.,  an extravagant  person.  —  F.,  fr.  ML.  extravagan- tem,  acc.  of  extravagans,  pres.  part,  of  extrd- vagari,  ‘to  wander  outside  (the  limits)’,  fr. extra-  and  L.  vagari,  ‘to  wander,  ramble,  roam about'.  See  vagary  and  -ant.
14846:flam,  n.,  sham,  trick.  —  Shortened  fr.  flimflam, flam,  n.,  a  drumbeat.  —  Of  imitative  origin, flambe,  adj.,  decorated  by  irregularly  splashed glaze.  —  F.,  pp.  of  flamber,  ‘to  singe,  blaze’,  fr. OF.  flambe,  ‘flame’,  which  is  a  back  formation fr.  flamble.  See  next  word, flambeau,  n.,  a  large  torch.  —  F.,  fr.  OF.  flamble, ‘flame’,  fr.  L.  flammula,  ‘a  little  flame’,  dimin.  of flamma,  ‘flame’.  See  flame, n.,  and  cp.  prec.  word, flamboyance,  flamboyancy.  n.  —  Formed  from next  word  with  suff.  -ce,  resp.  -cy. flamboyant,  adj.,  characterized  by  flamelike tracery  (archil.)  —  F.,  pres.  part,  of  flamboyer, ‘to  flame’,  fr.  OF.  flambe.  See  flambe  and  -ant. Derivative:  flamboyant-ly,  adv. flame,  n.  —  ME.  flamme,  fr.  OF.  flame,  flamme (F.  flamme),  fr.  L.  flamma,  ‘blaze,  flame’,  which stands  for  *flagma  and  is  rel.  to  flagrare,  ‘to blaze,  glow,  bum’.  See  flagrant  and  cp.  words, there  referred  to.  Cp.  also  dimmer  and  the  se¬ cond  element  in  oriflamme. flame,  intr.  v.  —  ME.  flamen ,  fr.  OF.  flamer,  ‘to flame'  (whence  F.  flammer,  ‘to  singe’),  fr.  L. flammare,  ‘to  flame’,  fr.  flamma.  See  flame,  n. Derivatives:  flam-ed,  adj .,  flam-er,  n.,  flam-ing, adj.,  flam-ing-ly ,  adv.,  flam-y,  adj. flamen,  n.,  a  priest  devoted  to  the  service  of  one particular  deity  (Roman  mythol.)  —  L.  flamen, which  prob.  stands  for  *bhladmen,  and  is  cogn. with  Goth,  biotan,  ‘to  worship’,  ON.  biota,  OE. blotan,  OHG.  bluo3an,  ‘to  sacrifice’, flamenco,  n.,  dancing  style  of  the  gypsies  of  An¬ dalusia.  —  Sp.,  ‘Flemish;  gypsy’,  fr.  MDu. Flaming .  See  Fleming.
15313:frambesia,  framboesia,  n.,  the  yaws,  a  tropical skin  disease.  —  Medical  L.,  fr.  F.  framboise, ‘raspberry’,  fr.  Frankish  *brambasi,  which  is rel.  to  Du.  braambezie,  ‘blackberry’.  See bramble,  berry  and  -ia.  F.  framboise  was  in¬ fluenced  in  form  by  F.  fraise,  ‘strawberry’, frame,  tr.  and  intr.  v.  —  ME.  framien,  framen, ‘to  be  profitable;  to  frame’,  fr.  OE.  framian,  ‘to avail,  be  profitable’,  fr.  OE.  fram,  ‘vigorous, bold’,  orig.  ‘going  forward’,  ft.  fram,  ‘forward; from’,  which  is  rel.  to  OE.  forma,  Goth,  fruma, ‘first’,  OE.  fremman,  ‘to  further’.  See  from  and cp.  foremost  and  words  there  referred  to. Derivatives:  frame,  n.,  frame-less,  adj.,  fram-er, n.,  fram-ing,  n.
15747:gamble,  intr.  and  tr.  v.  —  Dial.  ME.  gammlen, gamblen,  fr.  ME.  gamenen,  fr.  OE.  gamenian, ‘to  play’,  fr.  gamen,  'sport,  game,  amusement’. See  game,  n.
15748:Derivatives:  gamble,  n.,  gambl-er,  n.,  gamble- some,  adj.,  gantbl-ing,  n.
15750:Derivative:  gambol,  intr.  v. gambroon,  n.,  a  twilled  cloth.  —  Fr.  Gambroon, Gombroon,  now  Bandar  Abbas,  name  of  a  town on  the  Persian  Gulf.  Cp.  gombroon, game,  n,,  sport,  play.  —  ME.  gamen,  game,  fr. OE.  gamen,  ‘sport,  game,  amusement’,  rel.  to OFris.  game,  OS.,  ON.,  OHG.  gaman,  Dan. gamen,  Swed.  gamman,  ‘merriment’.  Cp.  gamble, gammon,  ‘backgammon’.
26568:oriflamme,  n.,  the  ancient  battle  standard  of  the kings  of  France,  the  banner  of  St.  Denis;  any standard.  —  ME.  oriftamble,  fr.  MF.  oriflamble, oriflambe ,  oriflamme,  fr.  OF.,  fr.  ML.  aurea flamma,  lit.  ‘golden  flame’,  fr.  L.  aurum,  ‘gold’, and  flamma,  ‘flame’.  See  aureate  and  flame, origan,  n.,  marjoram.  —  ME.  origane,  fr.  OF. origane,  origan  (F.  origan ),  fr.  L.  origanum.  See next  word.
28066:perambulate,  tr.  v.,  to  walk  through  or  over.  — L.  perambuldtus,  pp.  of  perambuiare,  ‘to  ramble through,  go  through’,  fr.  per-  and  ambuldre,  ‘to walk,  go’.  See  amble  and  verbal  suff.  -ate. Derivatives:  perambulation  (q.v.),  perambulator (q.v.),  perambulat-ory,  adj.  and  n. perambulation,  n.  —  ME.  perambulacion,  fr.  ML. perambulatio,  gen.  -dnis,  fr.  L.  perambuldtus,  pp. of  perambuiare.  See  prec.  word  and  -ion. perambulator,  n.,  1)  one  who  perambulates  (ar¬ chaic)  ;  2)  an  odometer;  3)  a  baby  carriage.  — ML.,  ‘one  who  perambulates’,  fr.  L.  perambuld¬ tus,  pp.  of  perambuiare.  See  perambulate  and agential  suff.  -or.
29938:preamble,  n.,  introduction.  —  ME.,fr.  MF.  (=  F.) preambule,  fr.  ML.  praeambulum,  prop.  neut. adj.  used  as  a  noun  fr.  Late  L.  praeambulus, ‘walking  before’,  fr.  praeambuldre,  ‘to  walk  be¬ fore’,  fr.  L.  prae-  (see  pre-)  and  ambulare,  ‘to walk’.  See  amble  and  cp.  preambulate.
29939:preambulate,  intr.  v.,  to  make  a  preamble.  — Late  L.  praeambulat-(um),  pp.  stem  of  praeam¬ buldre.  See  prec.  word  and  verbal  suff.  -ate. Derivatives:  preambulat-ion,  n., preambulat-ory, adj.
31074:Derivative:  purl-er,  n.,  a  throw,  spill, purlieu,  n.,  part  of  a  forest,  separated  from  it  after the  perambulation  of  its  boundaries  (Hist,  of Law).  —  ME.  purlewe,  fr.  AF.  puralee,  ‘peram¬ bulation’,  fr.  OF.  puraler,  ‘to  go  through,  per¬ ambulate’,  fr.  pur-  (see  pur-)  and  aler,  ‘to  go'. See  alley.  Purlieu  was  influenced  in  form  by  OF. (=  F.)  lieu,  ‘place’  (see  lieu). purlin,  n.,  a  timber  resting  on  the  principal  rafter and  supporting  the  common  rafters.  —  Of  un¬ certain  origin.
31606:ramble,  intr.  v.  —  Prob.  a  var.  of  ME.  romblen, freq.  of  ME.  romen,  ‘to  roam’.  See  roam.  The -b-  is  intrusive.  Cp.  grumble.
=== KLN exile
2437:amble,  intr.  v.,  to  go  at  an  easy  gait.  —  ME.,  fr. OF.  ambler,  fr.  L.  ambulare,  ‘to  go  about,  walk’, which  prob.  stands  for  *amb-al-are,  fr.  amb- (see  amb-)  and  I.-E.  base  *61-,  ‘to  go’,  whence also  Gk.  & M,  ‘ceaseless  roaming’,  aXac&aa, aXatvav,  ‘to  wander  about’,  aXy]-rr)<;,  ‘beggar’, Lett,  aluot,  ‘to  wander  about’,  L.  aliicinari,  ‘to wander  in  mind’.  See  hallucinate  and  cp.  am¬ bulance,  ambulate,  funambulist,  noctambulism, somnambulism.  Cp.  also  Alastor,  aleatory,  Aleo- chara,  alley,  ‘a  narrow  passage’,  exile,  purlieu. Derivatives:  amble,  n.,  amble-ing,  adj. amble,  n.,  an  easy  gait.  —  ME.,  fr.  F.  amble,  fr.
14043:Derivatives:  exiguous-ly,  adv.,  exiguous-ness,  n. exilarch,  n.,  head  of  the  Jewish  exiles  in  Baby¬ lonia  ( Jewish  hist.)  —  A  hybrid  coined  fr.  L. exilium,  ‘exile’,  and  Gk.  (£px<k,  ‘leader,  chief, ruler’.  See  next  word  and  -arch, exile,  n.,  banishment.  —  ME.,  fr.  OF.  (=  F.), exit,  fr.  L.  exilium,  exsilium,  ‘banishment,  exile’, fr.  exul,  exsul,  ‘a  banished  person,  wanderer’, which  is  of  uncertain  origin.  It  possibly  stands for  *eks-al-s  and  is  formed  fr.  1st  ex-  and  I.-E. base  *il-,  ‘to  wander  about’,  whence  also  Gk. aXaa&ou,  ‘to  wander  about’,  L.  al-ucinbri,  ‘to wander  in  mind’  (see  hallucinate).  The  spelling exsul,  exsilium  is  due  to  a  confusion  with  L. solum,  ‘soil’,  from  which  the  ancients  derived exilium  and  exul,  but  with  which  these  words have  nothing  in  common.  Nor  is  there  any connection  between  L.  exilium  and  exsilire,  ‘to spring  forth’.
14044:exile,  n.,  a  banished  person.  —  Fr.  prec.  word, exile,  tr.  v.,  to  banish.  —  OF.  exilier  (F.  exiler), fr.  L.  exiliare,  exsiliare,  fr.  exilium,  exsilium.  See exile,  ‘banishment’.
14045:exilian,  exilic,  adj.,  pertaining  to  the  exile  of  the Jews  in  Babylonia,  —  Formed  with  suff.  -ian, resp.  -ic,  fr.  L.  exilium.  See  exile,  ‘banishment’, exility,  n.,  slenderness.  —  L.  exilitas,  ‘smallness, thinness,  meagemess,  slenderness’,  fr.  extlis, ‘small,  thin,  meager,  slender’,  which  prob. stands  for  *ex-bg-slis  and  is  rel.  to  exiguus, ‘small,  scanty,  petty’.  See  exiguous  and  -ity. eximious,  adj.,  choice,  excellent.  —  L.  eximius , ‘select,  choice’,  lit.  ‘taken  out’,  fr.  eximere,  ‘to take  out,  take  away’,  fr.  ist  ex-  and  emere,  ‘to take,  buy’.  See  exempt,  v.  For  E.  -ous,  as equivalent  to  L.  -us,  see  suff.  -ous.
14912:Derivatives:  flexible-ness,  n .,  flexibl-y,  adv. flexile,  adj.,  flexible.  —  L.  flexilis,  ‘pliant, flexible’,  fr.  flexus,  pp.  of  flectere.  See  flex and  -ile.
15733:galumph,  intr.  v.,  to  prance  about  in  a  self-satis¬ fied  manner.  —  Coined  by  Lewis  Carrol  (pen- name  for  Charles  Lutwidge  Dodgson),  as  the blend  of  gallop  and  triumph, galuth,  n.,  the  Diaspora  ( Jewish  history).  —  Heb. galiith,  ‘exile’,  fr.  galih,  ‘he  uncovered,  removed ; he  departed ;  he  went  into  exile,  was  deported’, whence  also  Heb.  goldh,  ‘exile,  exiles’,  gillaydn, ‘tablet’.  Cp.  Aram.  glld,  ‘he  revealed,  uncover¬ ed;  he  departed,  went  into  exile’,  Arab,  jdla, ‘he  made  clear,  revealed,  disclosed;  he  ousted, removed;  he  went  away,  departed,  left’,  ajld, ‘emigrated’,  Ethiop.  taglegala,  ‘he  was  led  into exile’,  which  are  related  to  Heb.  galdh.  Cp.  also golah.
16403:gola,  n.,  a  storehouse  for  grain . — H  ind .  gold,  prop, ‘a  round  house’,  fr.  gol,  ‘round’;  so  called  from the  usual  form  of  such  storehouses, golah,  n„  Diaspora,  galuth  (Jewish  hist.)  —  Heb. goldh,  ‘exile;  exiles’,  fr.  gold’1,  ‘he  uncovered, removed;  he  departed;  he  went  into  exile,  was deported’.  See  galuth.
33542:salient,  adj.,  1)  projecting;  2)  conspicuous.  —  L. saliens,  gen.  -ends,  pres.  part,  of  satire,  ‘to  leap, spring',  which  is  cogn.  with  Gk.  a XXeaflm,  of s.m.,  aXux,  ‘a  leap,  spring’,  Toch.  A  sal-,  ‘to jump’,  Mir.  saltraim,  ‘I  trample’,  and  prob. also  with  OI.  ucchalati  (for  *ud-sa1ati),  ‘rises quickly’.  Cp.  Altica,  assault,  consilient,  desul¬ tory,  dissiiient,  exile,  exult,  halma,  insult,  resi¬ lient,  result,  salacious,  Salian,  ‘pertaining  to  the Salii’,  sally,  saltant,  saltarello,  saltation,  salti- grade,  saltimbanco,  saltire,  saltus,  saute,  somer¬ sault,  subsultory,  transilient,  tressiiate.  For  the ending  see  suff.  -ent.
=== SKT
618:Amble.  (F.-L.)    M.E. *»/«*/!•«  -1*1. F. ambltr,  to  go  at  an  easy  pncc.—  I tart,  to  walk.     %  Perhaps  for  d- to  go  about;  from  amb-,  aboot ,  ..u.  •• , to  go,  appearing  in  Gk.  0alrtir,  to  go  ;  ttc Ambi-  and  Base  (3).
1363:Ban,  n  proclamation.  (E.)  Chiefly  in the  pi.  banms  (of  marriage).  M.  K.  ban. A.  S.  gtbatfH,  a  proclamatioD  (the  pnrBx gt-  making  no  diRcrencc).  Cf.  A.  S.  dban^ nan,  to  summon,  onler  out.  -f'  l^u-  ban^ cxcommunicilion :  haMnen,io  exile;  Icel. and  Swed.  bann,  Dan.  band,  O.  H.  G.  ban, a  ban  ;  Ice),  and  Swed.  banna^  to  chide, Ban.  bandt,  to  curse.  Cf.  l^fama,  a  ra* mour.     (yiillA.)
2706:shamble,  to  walk  awkwardly.  (Du.— F.*  iLal.^L.)  T>ix.sehantp€Uft,  to  stumble, trip,  also  to  decamp.  — U.  F.  /ctcamptr,  to decamp;  as  above.
7335:Galley,  a  low  built  ship.   (F  ^ ga/t'ie.  —  O.  F.  golie ;  Low  L  ga/rm.  a Orig   nnknomi.
7378:gamble.    (F..>     A   late   word,  put gttmm  U  or  gam  U,  a  frequent  form  w has  taken  the  place  of  M.  F..  gamenn play  at  games.  —  A.  S.  gamenian,  to at  gamis ;  from  gamcn,  a  game.
7653:%  kite  (b!tt)) :  see  Qlids. I,  a  glowing  coal ;  see  Glow. ,    wnging,    (E.)      A.  S.   ^tV^, jojr,  miilh,   mnsic+Iccl.  ^, Swcd.  dial  gly,  mockery, vmlley.  i.C.)    Gael,  and r,  a  valley,  glen, ^lublc.  tDu)     Du. lo   slide  •• •way.     .VlLied    to
8090:G-rowl,  to  gramble.  (Du.)  Du.  gra//en, to  gnimblc.  +  G.  gtvUtn,  to  ramble  ;  Gk. fpv.wi^uv,  to  grunt,  ipii,  grunting.  Allied to  Oruiuble.
10110:IgBte*  10  eooslgs  to  exile.  (L.) pp.  of  L.  r»-%«iT,  to  send  away.
12015:mump,  to  mamble,  nlk,  beg.  (D«.) A  mumper  was  a  cant  term  Cot  ^\k^jgu.<*
12020:Du.  memptn,  to  mump,  cheat  (Scwcl)  ;  cf. tnommiUn,  mompeltn^  to  mamble  tHex- liain).  Tlius  mump  is  merely  jlq  emphntic form  of  mun,  O.  Da.  mommtn^  to  say mum,  also  to  mask.  Cf.  Goth,  bi-mamfy'an^ to  deride :  likewise  of  imitmtlve  origin.
13749:Itlate :  see  Amble.
16160:Roam.  (E.)  M.E.  romeH\  also  rumen (Laynmon).  Allied  to  A.  S.  dnimaH,  to S|)rcad  out  (usually  explained  to  lift  up^  ; prov.  E.  ramt,  ratm,  ratvm^  to  stretch, •prcnd  about,  roam,  ramble.  Cf.  A.  S. rSmigan  (sense  doubtful).  We  also  find O.  Du.  nimen,  to  strctdi,  Du-  ranutt,  to aim.  plan,  0.  Sax.  rdmSn,  to  aim  at,  O. Fries  ramia,  to  ftrivc  after,  O.  H.G. niWn,  to  strive  after.  Orig.  to  stretch out  aflcr,  strive  after,  aim  at;  hence  to iprcad,  roam,  ramble.  The  particuUr Knse  was  prob.  innucnccU  by  confusion with  M.  £.  Rome-rtnncrt,  a  runner  to Kome,  pilgrim;  cf.  lul.  Komep,  one  who goes  to  Rome,  a  pil^im.
16161:ramble.  (E.)  FrequtAtative  of  M.  £. ramcM,  prov.  E.  raine,  to  spiead  abroad, Sprawl;  hence,  to  gad  about.  The  b  is excrescent,  and  rambU  is  for  prov.  £, rammU,  to  ramble  (Whitby  Glosiuiry).
16501:Um.  Spin.  BxrM  means '  bramble/
16502:^om  BiK^ue  sartna,  a  bramble ;
16677:Bculk.  (.Scand.)    M.  E. /jf-w/*m.  —  Dan. skulke,  to  sciilk.  slink  ;  Swed.  skolka,  to  play the  truant.     Allied  to  Icel.  tkolla,  to  scutk, keep  aloof,  and  skjSl,  shelter,  cover  (above). Scrabble;  see  Sliarp. Scraggy ;  see  Shrink. Scramble,      Sorap,      Scrape ;     see Sharp.
17045:scramble.  (E.)  Nasalised  form  ol prov.  E.  jcradtU,  to  scramble,  allied  to S(raffit,  to  scramble,  scrapple,  to  grub about ;  frequentative*  of  Krapt^  prov.  E. scrap,  (o  scrape.
17739:exile,  banishment.  (F.  —  L.)  O.  F exil,  '  an  exile,  banishment ;  *  Cot.  —  L. txiltHm,  \jc\Xkt  txsiiium^  banishment —1>. txsui,  a  banished  man.  one  driven  from  his native  soil.  — L.  cr,  out  of;  solum  soil, ground  labovc).  %  But  now  geii.  ilcr  from L.  soiiff^  to  leap,  luii.
17800:t.  Somerset.  (F*. -Ital.- •jauft.  '  a  sobresault  or  sum* active  trick  in  tumbling;' nua/Ztf.— Ital.  sopra,  above, cap,  -•  I.  supra<t  above,  over ; of  saltMj,  a  leap,  from  pp.  of ;  sc'c  Salient. St,  PTic  who  walks  in  his i  Coined  (with  sufBx  -u/«L. wriTr.  as  in  6apt-ist)  from  L. ■rp,  and  amhuiart^  to  walk. pnd  see  Amble.
18700:strlplinfiT*  (£•)    A  double  dlmin.  from ttrip;  hence  a   tad  as  thin  ai  a  strips  a growing  lad  not  yet  filled  out. Strive ;  ».«  Stride. Stroke,  (I )  and  (a)  ;  see  Strike. Stroll,   to  wander.    (Scand.)     Formerly ttrauU.  strvyU.     (A  contracted  form,  as  if lot ttrugU*.)  Ftcquetitatjveof Dan.^/fT-^, to  stroll.  Swed.   stryla,  to  stroke,  also  to ramble.  Allied  to  StrUce:  c£  M.  E.jtn'Js£m, to  go,  proceed,  waiidcr.
```


## [2026-09-04T19:31:43.262Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LAT ambulo 3280-3300\"; sed -n '3280,3300p' LAT.txt; echo \"=== LAT exsul 19740-19775\"; sed -n '19740,19775p' LAT.txt",
 "description": "Print Ernout-Meillet entries"
}
```


### [2026-09-04T19:31:43.335Z] TOOL RESULT

```
=== LAT ambulo 3280-3300
ambubala (- (e) la) -ae f.: chicoree sanvage (Cels.Plin.). Autre nom
de 1 ' intubus (intuba). Ainsi appelee sans doute par mauvais jeu de49
amicio
mota: intubus intibus rapproch 4 de tibia et par 11 de ambubaia.
ambulo, -as, -&ul, -atum, -are: compos 4 ayant pour premier terne
le preverbe anb-, et glosd, eorrectement au point de vue dtymologique,
Ttep itoxtw ou circumeo. Le sena premier 4 tait "aller autour, faire un
tour", d'ou "se promener", encore frequemment attest 4 depuis Plaute,
cf. Thes. I i873,59sqq. Dana la langue familifere, 1 l‘aquelle le verbe
appartient specialenent (malgrd 1'emploi assez fr 4 quent qu*en fait
Cic., cf. Thes. III 1870; la podsie dpique l' 4 vite absolument peut-etre
en raison du cr 4 tique qu'il forme le plus souvent), s'emploie comme
synonyme de e 5 , gradior, uado avec le sens de "marcher (au pas)",
"cheminer", "aller", et s'oppose 1 sto, sedeo, curro, cf. Geli.16,18,14.
Usite dans la 1. juridique (cf.. la formule in ius ambula ), militaire
et medicale (Thes. I i874,»isqq.). Se dit quelquefois d'objets inanimes,
cf. Cat., Agr.1,3, mare aut amnis, qua naues ambulant. Fr 4 quent 1 basse
4 poque, notamment dans la langue de 1 'iglise (Itala, Vulg.), au sens
physique et moral: a. in "marcher dans la voie de", a. in deo. - Bien
repr 4 sent 4 dans les 1 . romaoes, M.L.413.
D 4 riv 4 s et compos 4 s: ambulus , conservi comme second terme de compose
=== LAT exsul 19740-19775
Vocalisne -o- a noter au second terme d'un compose; cf. meditullium
et peut-etre sobrius. Clest le type illustre par gr. mxepeC, amxopec;
I^ea, cpucni^ooc.
extra; extrinsecus: v. ex.
exui, exsul, -lis c.: exile. Ancien, usuel; iri.esui.
D 4 riv 4 s: exulS (-lor Lact.,Hyg .), -as: etre exild, et ses d^rivds
tardifs exuldtio,-tor,-tus‘, ex(sJilium: exii. M.L.3016; v.h.‘a. ihsili',
d'ou exilio, -as (depuis Ir^n.), M.L.3oi5; exilica causa, quae aduersus
' exulem agitur, P.F.71,6.; ex(s)ularis, Apul.; exuldtlcius, exilia-
t ictus .
ExfsJul est mis en rapport par les Latins avec solum: omnes scele¬
rati atque impii quos leges exsilio affici uolunt, exsules sunt, etiamsi
solum non mutarint, Cic., Parad.4,3,31; cf. aussi 1 'expression consacree
exilii causa solum uertere. De IA la graphie exolatum dans 1 'Aabro-
sianus de Pl., Tri.535. Mais si on lit exsul dans les ass., les inscrip-
tions ne connaissent que la graphie exui, exilium. Cf. extorris, extor-
rdneus, extermino. Doit plutot se rattacher A la racine verbale qu'on
a dans amb-ulo-, v. ce aot.
exuS, -uls, -ul, -utum, -uere; d^vetir, d^pouiller; exutus "d£-
pouill£". M.L.3iioa. Sens propre et figure. Ancien et usuel.
exuuiae f.pl.(surtout po^tique): d 4 pouille d'un animal, vieille
peau du serpent; veteaents enlev^s par quelqu'un, cf. Pl., Men.191,
induuiae tuae atque uxoris exuuiae, paf suite "d^pouilles d'un enneai":
Vg.,Ae. 3,375 [ Hector .] exuuias indutus Achilli. Exuuiae est. forad
comae rel(lJiquiae; le second u doit noter un phonfeae de transition
entre u et i voyelle: ci.fluuius en face de -fluus.
A exulS s'oppose: induo "revetir", proprement "aettre sur soi"; avec
le prdfixe ind-, cf. endo, indu d'o 4 par analogie de indutus, coup^
in-dutus ; exdutae (l. -tiae?): exuuiae P.F.70,4. S'emploie 4 galeaent
au m^dio-passif induor, indutus-, forae pronominale se induere "se
mettre dedans"; se induere in laqueum, Plaute Cas.113, et par suite
"se transformer en": cum se nux plurima siluis induet in florem, Vg.,
G.1,188. Sans rapport etymologiqne avec ev8u<u, evBuxoC malgr 4 l*ho-
monymie et la synonyaie. Mais le verbe grec a pu influer sur les eaplois
qui ont ^t£ faits de induS.- 369
exuo
```


## [2026-09-04T19:31:44.942Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY آوار\"; grep -n \"آوار\" incoming/ARY/ARY_pages.txt | head -20; echo \"=== SYN wander\"; grep -n -i \"aláomai\\/\\|alaomai\\|ambulare\" SYN.txt | head -20",
 "description": "Grep Aryanpur and Buck"
}
```


### [2026-09-04T19:31:45.017Z] TOOL RESULT

```
=== ARY آوار
=== SYN wander
17527:Lat. ambulare ‘walk’ (10.45), used col- loquially for ‘go’ in Plautus (quo ambulas tu, bene ambula) and regularly in late Latin. Hence Fr. aller, Rum. umbla. REW 412. Wartburg 1.86f.
```


## [2026-09-04T19:31:51.903Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3300,3320p' LAT.txt; echo \"=== SYN ctx\"; sed -n '17515,17535p' SYN.txt; echo \"=== LEW ambul\"; grep -n \"ambul\" LEW_1910.txt | head -20",
 "description": "More Latin sources"
}
```


### [2026-09-04T19:31:51.989Z] TOOL RESULT

```
D 4 riv 4 s et compos 4 s: ambulus , conservi comme second terme de compose
dans fun-anbulus ; ambulatio: promenade (abstr. et concr.) ambulatiun¬
cula (Cic.); ambulator,-trix,-torius (M.L.413), -tura f. "amble" (V 4 g.
Chir.
trad.
ex-, in-, ob-, red-ambulo rarement attestds.
anb-ulare est un verbe duratif en -a- pr 4 c 4 d 4 de preverbe, comme
oc-cupare. L'ombrien a une forme verbale sans le suffixe -a- dans
om b-oltu "ambulatS" et le latin a alacer (v. ce mot). La forme radicale
*el- apparait en second terme de compos 4 : ex-ul. Hors de 1'italique
une racine *el- "aller" est attestde en celtique (m.gall. ei "qu'11
aille" 'etc.j cf. Pedersen, Vergi. Gr. II 353). On a en outre rapproch 4
gr.aXaop.ca, lette aluot "errer"y dont les sens sont trop differents,
et, mieux, le groupe^de gr. eXauvw, eXaoai,, avec les formes 41 argies
hom. t^XuGov, ion.-att. r|X 0 ov (thfemes *e l-u-, *e l-u-dhe-, *el-dhe~) , peut-
etre arm .eli "je suis monte, je suis sorti".
amellus, -1 (anello, -ae) f.: amelle, |ieXCcpuXXov. Attest 4 depuis
Yirgile. Etym.pop. dans Serv., G.4,378, Mella fluuius Galliae est, iuxta
quen haec herba plurima nascitur, unde et amella dicitur.
amentum: alunen scissum (Theod.Prisc.). Sans explication.
ames, -itis m.: perche; perche k oiseleur; manche d'outil, levier.
=== SYN ctx
*gxem-. Girk. Baivw “go, walk’; Lat.
Walde-P.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
694 SELECTED INDO-EUROPEAN SYNONYMS
venire ‘come’ (> the Romance words) ; Goth. giman, OE cuman, etc., general Gme. for ‘come’; Skt., Av., OPers. gam- ‘go, come’ (Skt. gacchati, Av. fasaiti, sko- presents like Grk. Bacxw; Av. Jam- without prefix mostly ‘come’; also Av., OPers. a-jam- ‘come’, whence NPers. amadan ‘come’); Toch. kém-, kum-, etc. ‘come’ (SSS 428 f.).
*gra-. Grk. aor. &8nv, Dor. é8av; Skt. aor. agam, pres. jigali; Av. aor. gat; Lett. gaju ‘went’ (pret. to zet).
3. Grk. gow ‘creep, crawl’ (10.41), in many dialects simply ‘go’. Buck, Grk. Dial. 333.
NG pop. waw, fr. Grk. dr-ayw ‘lead, bring (up, under)’, intr. ‘go slowly away, retire, withdraw’ (of an army, etc.), in NT simply ‘go away’. Hence also NG anyaivw new pres. to aor. m#ya = old imperf. dajyov.
Grk. Baivw, in NG only in epds., pralyw ‘go in’, Byalyw ‘go out’, fr. EuBalvw, eBaivo.
4, Lat. tre, Sp. ir, etc., above, 1.
Lat. cédere, perf. cesst (mostly ‘go away’, but ‘go’ in cpds., perh. fr. *ce-zd- with weak grade of *sed- in ChSI. choditi, etc. (below, 8). Walde-P. 2.486. Walde- H. 1.198. Ernout-M. 168 f.
Lat. vadere ‘go rapidly, rush, ad- vance’, in late Lat. simply ‘go’ (e.g. fre- quently in Peregrinatio) : Lat. vadum ‘ford’, ON vada ‘wade, rush’, OHG watan ‘wade’, OH wadan ‘go, advance’ (NE wade). Hence the present forms like It. vado, va, Fr. vais, Sp. voy, Rum. 3sg. va, etc. Walde-P. 1.217. Ernout-M. 1069. REW 9117.
Lat. ambulare ‘walk’ (10.45), used col- loquially for ‘go’ in Plautus (quo ambulas tu, bene ambula) and regularly in late Latin. Hence Fr. aller, Rum. umbla. REW 412. Wartburg 1.86f.
It. andare, Sp. andar (latter mostly ‘walk’), much disputed. Apparently fr.
CC-O. In Public Domain. Gurukul Kangri Collection, Haridwar
a VLat. *ambitare (: Lat. ambire « i around’, sb. ambitus), but in late Lat texts there is no trace of such a form Bee side the common ambuldre; hence one suspects some, not precisely explained, re. formation of the latter. REW 409, 419.
Rum. merge, fr. Lat. mergere ‘sink plunge’ (10.33). Semantic development, perh. ‘sink’ > ‘disappear’ > ‘withdraw’ (cf. ‘Alb. mérgonj ‘withdraw’) > ‘go away’ > ‘go’ (so Puscariu 1058), but may be simply fr. the pop. use of mer- gere for impetuous going, like NE plunge into the woods, into the crowd, ete. Cf. immersit sese in ganeum ‘plunged into a gaming-house’, ete, (Plaut.), and zmmargebam in a Roman epitaph from Bulgaria. RIEW 5525.
5. Ir. tiagu, NIv. t@ighim : Grk. orel- xw ‘stride, advance, walk’ (in Lesb. dial. ‘go’), Goth. steigan, -steigan used for various cpds. of Grk. Balyw, ON sliga, OE, OHG stéigan, all used for ‘go, go up, go down’, Lett. steigt ‘hasten’, etc. Walde-P. 2.614.—Ir. imperat. eirg, fut. -rega, Nir. raghaidh, etc., etym. dis- puted. Walde-P. 2.364 (: rigim ‘stretch out’). Pedersen 2.648, Thurneysen, Gram. 473. (: Grk. épxopnat ‘come’ 10.48).—Ir. pret. luid : Grk. eboopat, #dvOov (10.48). Walde-P. 2.417. Pedersen 2.378.—NIr. pret. chuaidh, Ir. perf. do- cuaid, perh. *dicom-vad- : Lat. vddere (above, 4). Pedersen 2.648.—Ir. inf. dul, etym.? (Pedersen l.c. : Alb. ddlé ‘go out, sprout’).
W. myned, Br. mont, monet, Corn. mones : ChSl. minqti ‘pass’ (of time), Lat. medre ‘wander, go’, IE *mei-. Walde-P. 2.241. Pedersen 2,454.—The finite indicative Britannic forms chiefly fr. the root *ag- (in Lat. agere, etc.), ©. (only 3sg. forms quoted) W. pres. @ (OW agit), imperf. ai, perf. aeth; Br. pres- a, imperf. ae, pret. eaz. Pedersen 2.358, ? eas) e 451 £, (Walde-P. 1.35).—W. subj. (3s6-)
oTION; © Br. fut. y-elo : Ir. ad- ’ either fr. IE *pel- e’, or fr. *el- in Grk.
Et , Walde-P. 1.156. Peder- avr 9 Thurneysen, Gram. 95 n 2.3 ‘ ON ganga, OE gan-
=== LEW ambul
13009:bamba I 477 bambals, bambuls, bambdé I 111
```


## [2026-09-04T19:32:09.935Z] TOOL CALL #20: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-04T19:32:09.942Z] TOOL RESULT

```


```


## [2026-09-04T19:32:13.951Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%88%D8%A7%D8%B1%D9%87",
 "prompt": "Give the full Persian entry for آواره: etymology, meaning, any Middle Persian or Proto-Iranian antecedent, and any cited sources (Hasandust, Cheung, MacKenzie). Also any Turkish/Ottoman borrowing sections."
}
```


## [2026-09-04T19:32:15.475Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ambulo",
 "prompt": "Give the Latin entry for ambulō: full etymology, the PIE root(s) cited, and any mention of de Vaan, Ernout-Meillet, or alternative derivations (*h1el- vs *h2el-)."
}
```


### [2026-09-04T19:32:21.002Z] TOOL RESULT

```
# Persian Entry: آواره (âvâre)

## Etymology
The word is formed from آوار (āwār / âvâr) plus the suffix ـه (-a / -e). The etymology section notes it is "missing or incomplete" and invites contributions.

## Meanings
The noun has nine documented senses:

1. Account-book; computation
2. Certainty, assuredness
3. Lost, annihilated
4. Ruined; scattered
5. Destitute of name or character
6. An exile, outcast, vagabond, vagrant
7. Iron filings
8. Oppression, injustice
9. Bane, ruin, desolation

## Pronunciation
Multiple regional variants are documented:
- Classical Persian: /ʔaː.waː.ˈra/
- Iranian Persian (formal): [ʔɒː.vɒː.ɹé]
- Dari (formal): [ʔɑː.wɑː.ɾá]
- Tajik (formal): [ʔɔ.vɔ.ɾá]

## Historical Sources
The cited reference is **Steingass, Francis Joseph (1892)**, *A Comprehensive Persian–English Dictionary*, London: Routledge & K. Paul.

## Note
No Middle Persian or Proto-Iranian antecedents are provided in this Wiktionary entry. Turkish/Ottoman borrowing information appears in the "Descendants" section rather than separate entries.
```


### [2026-09-04T19:32:21.082Z] TOOL RESULT

```
# Latin Entry for ambulō

## Etymology

The word derives from the combination of _ambi-_ ("around") plus _\*alō_ ("to wander"), tracing back through Proto-Italic _\*alō_ to Proto-Indo-European _\*h₂elh₂-_ ("to wander").

## PIE Root

The primary PIE root cited is **_\*h₂elh₂-_**, with the prefix _ambi-_ deriving from PIE _\*h₂m̥bʰí_.

## Scholarly References

The page cites **Michiel de Vaan's** _Etymological Dictionary of Latin and the other Italic Languages_ (2008), which provides etymological analysis on page 38. However, the document does not mention Ernout-Meillet or discuss alternative derivations such as _\*h1el-_ versus _\*h2el-_.

## Definition

The verb means "to traverse, travel" or "to walk," with synonyms including _deambulō_, _vādō_, and _gradior_.
```


## [2026-09-04T19:32:28.594Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/exsul",
 "prompt": "Latin exsul/exul: full etymology, PIE root cited, de Vaan's view, and descendants (English exile, French exil)."
}
```


## [2026-09-04T19:32:29.989Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82elh%E2%82%82-",
 "prompt": "Give the reconstruction entry: meaning, derived terms and descendants by language (Greek, Latin, Iranian/Persian, Baltic, Tocharian), and references."
}
```


### [2026-09-04T19:32:33.832Z] TOOL RESULT

```
# Etymology of "exsul"

The Latin word **exsul** (meaning "exile" or "wanderer") has uncertain origins, with scholars proposing several theories:

**Proposed etymologies:**
- From Proto-Indo-European *sel- ("to spring"), related to the Latin verb *saliō*
- From Proto-Indo-European *h₂el- ("to wander")
- From the Latin *solum* ("ground/soil")

The entry notes that the exact derivation remains unknown, listing these as "suggestions" rather than confirmed sources.

**Related terms** include *praesul* and *cōnsul*, which share structural similarities.

**Descendants** include the Italian word *esule*, demonstrating how this Latin root evolved into Romance languages. The term entered English and French as "exile" and "exil" respectively, though the Wiktionary entry itself focuses primarily on the Latin form and its immediate Latin-derived terms (*exsilium* and *exsulō*).
```


### [2026-09-04T19:32:36.635Z] TOOL RESULT

```
# Proto-Indo-European Root: *h₂elh₂-

## Meaning
The reconstructed root means "to wander, roam" and is classified as an imperfective verb.

## Derived Terms by Language

**Greek (Hellenic)**
- Ancient Greek: ἀλάομαι (aláomai) – "to wander, roam"
- Ancient Greek: ἀλύω (alúō) – "to wander in mind, to roam"
- Ancient Greek: ἄλη (álē) – "wandering"

**Latin (Italic)**
- Latin: alucinor
- Appears in compound form ambulō

**Iranian**
- Sanskrit: अट् (aṭ) – "to wander" (tentative connection)

**Baltic**
- Latvian: alot, aloties, āļa, āļoties

**Tocharian**
- Tocharian A & B: āl- ("to keep away, check, restrain")

**Armenian**
- Old Armenian: աղամող (ałamoł)

## References
Sources include Helmut Rix's *Lexikon der indogermanischen Verben* (2001), Robert Beekes' *Etymological Dictionary of Greek* (2010), and Xavier Delamarre's *Dictionnaire de la langue gauloise* (2003).
```


## [2026-09-04T19:32:41.796Z] TOOL CALL #25: WebSearch

```json
{
 "query": "ریشه واژه آواره حسن‌دوست فرهنگ ریشه‌شناختی آوار"
}
```


## [2026-09-04T19:32:42.090Z] TOOL CALL #26: WebSearch

```json
{
 "query": "Persian \"āvāra\" etymology \"wanderer\" Middle Persian \"āwārag\" homeless"
}
```


### [2026-09-04T19:32:43.555Z] TOOL RESULT

```
Web search results for query: "ریشه واژه آواره حسن‌دوست فرهنگ ریشه‌شناختی آوار"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T19:32:44.877Z] TOOL RESULT

```
Web search results for query: "Persian "āvāra" etymology "wanderer" Middle Persian "āwārag" homeless"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T19:32:51.500Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%88%D8%A7%D8%B1",
 "prompt": "Persian آوار: all etymology sections and senses (ruin/debris; wanderer), any Middle Persian, Armenian or Turkic origin proposals, and cited references."
}
```


## [2026-09-04T19:32:52.556Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/avare",
 "prompt": "Give the full etymology entry for Turkish \"avare\": Persian source form, its analysis (prefix/root), and earliest attestation."
}
```


### [2026-09-04T19:32:56.991Z] TOOL RESULT

```
I apologize, but the web page content provided contains only the header, navigation, and footer of the Nişanyan Sözlük (Nişanyan Dictionary) website. It does not include the actual etymology entry for the Turkish word "avare."

To provide you with the full etymology including the Persian source form, morphological analysis, and earliest attestation, I would need access to the actual dictionary entry page for "avare," which is not present in the content shared.

I recommend visiting the dictionary directly at nişanyan.com and searching for "avare" to retrieve the complete etymological information you're seeking.
```


### [2026-09-04T19:32:57.856Z] TOOL RESULT

```
# آوار (āwār) - Persian Dictionary Entry

## Meanings
According to Wiktionary, this Persian noun has three definitions:

1. **Debris** - physical remains or fragments
2. **Injustice/Iniquity** - unfairness or moral wrongdoing
3. **Alternative form** of آواره (āwāra), meaning wanderer or vagrant

## Etymology
The word likely descends from Old Persian roots. The entry notes: "Perhaps from Old Persian _\*awa-bar-_ ("to take away") or _\*ā-bar-_."

A cognate appears in Old Armenian (աւար/awar), traced through Parthian (ʾwʾr), both meaning "loot, spoils."

## Pronunciation
The term is pronounced differently across Persian dialects:
- Classical: /ʔaː.ˈwaːr/
- Iranian formal: [ʔɒː.vɒ́ːɹ]
- Tajik: [ʔɔ.vɔ́ɾ]

The entry was last updated in August 2026 and is categorized as a Persian lemma and noun.
```


## [2026-09-04T19:33:10.387Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN awar\"; grep -n \"awâr\\|âwâr\\|awar '\\|awära\\|âwâra\" HRN.txt | head -20; echo \"=== HUB awar\"; grep -n \"awâr\\|âwâr\\|awar\\b\" HUB.txt | head -20; echo \"=== PHD awarag\"; grep -n \"ʾwbʾl\\|awbār\\|āwār\\|awār\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -20",
 "description": "Grep Horn, Hübschmann, MacKenzie for awar"
}
```


### [2026-09-04T19:33:10.473Z] TOOL RESULT

```
=== HRN awar
14695:ei-awära 4Ö2.
=== HUB awar
795:gehort nicht zu upa + [/^var, sondern ist = paz. vawar
796:credibly, belief*, Shk. 272, phi. vawar (geschrieben
1847:machung (West, PT. I, 29), paz. x^awar 'compassio-
4842:bar, abar 'auf, iiber == paz. awar, phi. apar^\ ap.
6016:Daneben var in d€Lvar *Richter = paz. dawar, phi.
6397:a) = np. b in : abr * Wolke' = paz. awar Shk. 233, zd,
6852:geschwunden in davar *Richter' = paz. dawar Min. Gl. 60,
=== PHD awarag
PHD.txt:336:frawār [plw'l | N farwār(a)] bastion.
PHD.txt:339:*frawārdan, frawār- [plw’l-tn'] present, serve (food).
PHD.txt:564:sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-s?1] stony place. sanj-, v. saxtan. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) danger, trouble. --ómand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
PHD.txt:3202:prayer namāz, niyāyišn; ahunawār, āfrīnagān, hūmāst.
PHD.txt:3212:present frawārdan.
PHD.txt:4681:frawahr - PO o parwāngāh 595 ep o parwanagih ^5 e» Ф parwanag 13 ? o frawār, parwāl M o frawār-, parwāl- ANN CH parwālišn e» O frawārdan wed > оу franàm- - PO v franāmišn Irv’ > vo parwāz о» ro franāftan мү оу \ o Farrobag Yo (read pin-) Farróbag | 23 » a) piring E N a palang 3 М оз рагпарап w as» QJ palangmusk VU re N) Q) parwand E R Фу parwand- - 9 i a parron Ў оу frogih- -45?o frogihistan Us 4» оу frog Po parrwar N М P
```


## [2026-09-04T19:33:12.215Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%D9%88%D8%A7%D8%B1%D9%87/",
 "prompt": "Show the dictionary entries for آواره from لغت‌نامه دهخدا and فرهنگ فارسی معین, including any bracketed etymology tags."
}
```


### [2026-09-04T19:33:16.419Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T19:33:24.504Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D5%A1%D6%82%D5%A1%D6%80",
 "prompt": "Old Armenian աւար (awar): etymology, the Iranian (Parthian/Middle Persian) source form cited, meaning, and references."
}
```


## [2026-09-04T19:33:25.640Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.vajehyab.com/dehkhoda/%D8%A2%D9%88%D8%A7%D8%B1%D9%87",
 "prompt": "Show the Dehkhoda entry for آواره: definitions and any etymological note or cross-reference to آوار."
}
```


### [2026-09-04T19:33:30.479Z] TOOL RESULT

```
# Old Armenian աւար (awar)

**Meaning:** This Old Armenian noun refers to "loot, spoils, booty; plunder, pillage, sacking."

**Etymology:** The word is "an Iranian borrowing" with cognates including Parthian ʾwʾr, Middle Persian ʾdʾly ("booty, plunder"), and Pashto avār ("plunder, spoil, prey, booty, pillage"). These derive ultimately from Proto-Iranian *HwarH- meaning "to pluck, tear out; to rob, plunder."

**Descendants:** The term evolved into modern Armenian ավար (avar) and influenced Old Georgian ავარი (avari) and იავარი (iavari), which subsequently passed into Mingrelian as ნავარი (navari).

The entry includes detailed declension tables showing three grammatical patterns (i-a, o, and i types) across singular and plural forms, along with multiple derived terms and classical references.
```


### [2026-09-04T19:33:30.898Z] TOOL RESULT

```
# Dehkhoda Dictionary Entry for آواره

According to the Dehkhoda dictionary shown, **آواره** (āvāre) has the following definition:

"دفتر حساب" (a ledger or accounting book) where scattered financial records of the administrative office are recorded.

**Etymological Note:** The entry indicates a connection to **آوار** (āvār), suggesting that آواره is a related or derived form. The definition specifies it as "دفتری که حسابهای پراکنده ٔ دیوانی در آن نویسند" — a register in which dispersed governmental accounts were written.

The dictionary supports this definition with a verse attributed to Moezzī that references the word in a historical administrative context.
```


## [2026-09-04T19:33:52.375Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG HwarH / awar\"; grep -n \"HwarH\\|\\*Har-\\|āwārag\\|āwāra\" CHEUNG.txt | head -20; echo \"=== CHEUNG 'to wander'\"; grep -n -i \"to wander\" CHEUNG.txt | head -20",
 "description": "Grep Cheung for relevant roots"
}
```


### [2026-09-04T19:33:52.446Z] TOOL RESULT

```
=== CHEUNG HwarH / awar
=== CHEUNG 'to wander'
2823:*bramH ? ‘to wander, roam’ 
2825:*AVESTAN: YAv. bräs- ‘to wander, roam ?’ © The interpretation of hapax ҮАУ. 
7688:*NWIR: Kurd. (Kurm.) garin/gar-, (Sor.) garan/garé- ‘to wander, go (round), roam’, 
14343:*SOGDIAN: BSogd. y B, CSogd. y’b, MSogd. y'B ‘to wander, travel, rove’, CSogd. 
19881:*NWIR: NP pöyidan/pöy- ‘to wander; to run; to trot’, NP püd, Nn. puy ‘woof, weft’, 
58294:to wander
```


## [2026-09-04T19:33:58.309Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"آوار\\|آواره\" BQT_v1_pages.txt | head -30",
 "description": "Find آوار in BQT vol 1 pages file"
}
```


### [2026-09-04T19:33:58.371Z] TOOL RESULT

```
8728:] مارم ۱ بروژن و معثی آواره - آموخته است ۵ . #
8972:آواد » بر وزن ناچار . مخذف آواره
8981:حساپ کننده و محاسب را آواره گیر گوشد ‏
8991:.رکه اولز . ۴ .. * آمار » آهاره » آواره » آمازد : اوارجه .
8992:۴ ودفتر حساب : بی‌دیرنمانده است که مك ملعانرا آرند بدیوان نوآواره و دفتر
9003:آوارجه - رکه : آورجه .عمتی هم هست معنی بیاور - و بمنی صاحب و
9008:| ور چ4 - بنتح‌جیم» بمعنی‌آوارجه ۴
14742:۵ رك , ص: به . ۱ ول : آوا . ۷ - رک : آواره وآهار .
14743:۸ رد۵ : آواره و آمار . ۸ رك : اوار  .‏ *9 رك : وام . ٩‏ رگ : فلم.
19807:لستك بت بر وزن سمل سزرآوار وکافی-
25021:باشد کسی را از جابی ودفع تمودن - و آواره
```


## [2026-09-04T19:34:02.707Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8960,9010p' BQT_v1_pages.txt; echo \"=== page tag ===\"; awk 'NR<=8972 && /\\[pdf page/ {t=$0; n=NR} END{}' BQT_v1_pages.txt; grep -n \"\\[pdf page\" BQT_v1_pages.txt | awk -F: '$1<8972' | tail -3",
 "description": "Print BQT آوار entry with page tag"
}
```


### [2026-09-04T19:34:04.512Z] TOOL RESULT

```
]و اذه گشتن - بسنیم آوازکفتن
است که بممنی شهرت گرفتن ر سمر گردیدن
ا وخ « بفتح ثاك و سکون خای قطه
دار. بمعنی آواخ است که آه واضوس - وفشمت
آو بروزن واو . آب را کوبند چه
در فارسی واو ببا و برعکس تبدیل می‌باید ۷ .
و « با تاك بالف کشیده . مخفف
آواز باشد لهذا هزار دستان را هزار آوا تسیز
گومشد .
] و اخه بسکون خای‌نقطه دار » بمعنی
آوخ قت که ماو بای نی فقوت نی مق اف
وضمت و اصیب را نیز گوبند .
آواد » بر وزن ناچار . مخذف آواره
است که از خان و مان دور افتاده باشد - وبمعنی
آزار و مشم هم آمده است - و حسب و حساب
را یز گوبند ۴ - وبمعنی خراب هم آمده است
که شض آباد باشد . ۶
[ و اده ‏ ختح رای فرشت. نابود شده
و کم کردیده و پراکنده و پریثان گشته و می‌نلم
و نشان و از وطن دور افتاده و سرکردان شده
را گوبند و ترجمة حساب نیز هست ۴ ؛ چه
حساپ کننده و محاسب را آواره گیر گوشد ‏
وبنمنی خراب هم هست که درمقابل آباد است -
وظلم و سنم و آزار رالیز کوبند - و بمعنی‌تحفیق
وبفین هم آمده است 6 - وآهن رزه را گویند
و صیب باشد .
!ود » بوزن باور.بمعنی درست‌وتحقیق
وین باخد - وبسعتی فك حفنم ببزهنت کهفاكك
زحل باشد ۸ و آورنده را نیز گویند وامرباین
٩‏ رکه . آب : کی توا که همچو ماغ چتار ‏ بزید فوطه در ميا آو.
صنائمی با لطفی « لفت‌نامه ».
.رکه اولز . ۴ .. * آمار » آهاره » آواره » آمازد : اوارجه .
۴ ودفتر حساب : بی‌دیرنمانده است که مك ملعانرا آرند بدیوان نوآواره و دفتر
ممزی « لفت نامه » . ۵ ره : آور .
۰ - ازريشة اوستالی ۷86۷۵ (کفتن): سانسکریت 651466 2۷2,۷۵ بق۷2 ۷۵
پارسی‌میانه ]۱16 «بارنولمه ۱۳۳۲: پهلوی 8۷8 «اونوالا ۳۲4». ۷9 اوستائی و۷26 ساسکریت
و [۷2 و ۷۵[2 پهلوی و ۷۵۶ لائینی و ۷۵1۲ فرانه و ۷۵366 انگلیسی وبلژ , باج » باز »
واج » واژ , آواز » آوا , جزه فرم کواژ وکواژه (نکوهش) ازاین‌ماده است . فخرده اوستا ۸۳»
طبری ۷2 < واژه‌نامه ۱ » زباکی 2۷۷22 «کربرسن ۷4. ۲ ام کت لز: آواز +-
ه پسوند بت . ۸ - این بت ابوشمیب را برای این‌منی شاهدآ وردماند : .
اکردیده بگردون بر کمارد زسهمش پاره پاره کردد آور
گذنته از اینکه شاهد دمگری برای این‌مدعا نیست ؛کلمه دراین بیت ظاهراً حمان‌ممنی
شینا وقطعا میدهد < لفت نامه » . "
آوارجه - رکه : آورجه .عمتی هم هست معنی بیاور - و بمنی صاحب و
خداوند نز گفته‌اند وقت ی که بالفظی م کب شود
همچو جنکه‌آور و دلاور و زورآور و مانند
آن - ویمشی کربه و زشت و بد قیافه هم بنظر
آمده است ۱ - و مخی‌ژشت و بدرا نیز گویند.
| ور چ4 - بنتح‌جیم» بمعنی‌آوارجه ۴
است که دفتر حسابهای پراگنده (۱) باشد .
آودذده بر وزن ناورد ۰ عمروف ات
=== page tag ===
```


## [2026-09-04T19:34:15.156Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -5 BQT_v1_pages.txt | cat -A | head -5 | cut -c1-200; echo ---; grep -n -m3 \"pdf page\\|^=== \\|\\[page\" BQT_v1_pages.txt | head",
 "description": "Inspect BQT pages file format"
}
```


### [2026-09-04T19:34:15.219Z] TOOL RESULT

```
^LM-[M-1 M-[M-5 M-[M-1! M-[M-1$
7 M-YM-^EM-YM-^HM-YM-^E M-[M-3 M-YM-^DM-XM-'M-YM-^E$
M-YM-^E M-[M-1 0 M-YM-^H M-XM-7M-YM-^B M-XM-5M-YM-^AM-XM-1M-XM-1M-XM-1M-YM-^FM-[M-^LM-XM-'M-XM-9M-XM-/M-XM-1M-[M-^LM-XM-1M-YM-^EM-XM-'M-XM-1M-YM-^HM-[M-^L$
M-[M-0 M-[M-1 "M-[M-3$
M-[M-3$
---
```


## [2026-09-04T19:34:21.912Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=8972{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before line 8972:\", n}' BQT_v1_pages.txt; python3 - <<'EOF'\np=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\n# find index of page containing 'مخذف آواره'\nfor i,pg in enumerate(p):\n    if 'مخذف آواره' in pg or 'مخفف آواره' in pg:\n        print('page index',i)\n        print(pg[:200])\nEOF",
 "description": "Locate BQT page index"
}
```


### [2026-09-04T19:34:23.676Z] TOOL RESULT

```
formfeeds before line 8972: 275
page index 275
که هکلم سوراخ کردن نمل اسب و استر ومانند
آن از سل بیفند .
آواد - بسکون زای‌قطه دار.عمروف
است کد مدا و ندا و بانگه بلند باشد - وبمعنی
شهره شدن و سم کشتن عم آمده است .
آو اد گشتن بممنی شهره شدن
و مشهور
```


## [2026-09-04T19:34:28.425Z] TOOL CALL #38: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['IEC'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\"",
 "description": "Read BQT/IEC/MON refs_online details"
}
```


### [2026-09-04T19:34:30.063Z] TOOL RESULT

```
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
{
 "title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87",
 "edition_found": "1984-1987 (complete, cols./pp. 1-1682)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987",
 "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt",
 "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.",
 "notes": "",
 "cites": "column/page number of Mann, An Indo-European Comparative Dictionary (1984–87)"
}
{
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
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
```


## [2026-09-04T19:34:37.507Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/alley",
 "prompt": "Full etymology of \"alley\" (narrow passage): Old French alee, aler, Latin ambulare — quote the chain and dates."
}
```


## [2026-09-04T19:34:38.913Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/exile",
 "prompt": "Full etymology of \"exile\" (noun and verb): Old French, Latin exilium/exsul, and what it says about the origin of exsul (root al- \"to wander\" or salire)."
}
```


### [2026-09-04T19:34:43.121Z] TOOL RESULT

```
# Etymology Chain for "Alley"

The word "alley" traces back through this lineage:

**Old French (13c.):** "alee" — meaning "a path, passage, way, corridor," derived from the feminine form of "ale," the past participle of "aler" meaning "to go."

**Latin (uncertain origin):** The Old French "aler" possibly stems from Latin "ambulare" meaning "to walk." According to the source, this connection "might be a contraction of Latin ambulare 'to walk'" or alternatively derive from Gallo-Roman sources.

**Timeline:** The English noun "alley" appears in mid-14c. usage, referring to "passage in a house; open passage between buildings; walkway in a garden." By around 1500, it was applied to "long narrow enclosure for playing at bowls, skittles, etc."

The etymological path demonstrates how a Latin verb of motion evolved through Old French into the English term for a narrow urban passage.
```


### [2026-09-04T19:34:45.108Z] TOOL RESULT

```
# Etymology of "Exile"

## Noun (c. 1300)
The noun derives from Old French *exil/essil*, tracing back to Latin *exilium* meaning "banishment; place of exile." It also refers to "a banished person," from Latin *exsul*.

## Verb (c. 1300)
The verb originates from Old French *essillier* ("exile, banish, expel"), stemming from Late Latin *exilare/exsilare*, which comes from the noun *exilium*.

## Origin of "Exsul"
Scholars propose multiple etymologies for the Latin *exsul* root:

- **Wandering theory**: The second element may derive from the PIE root *\*al-* meaning "to wander," connecting to Greek *alaomai*.

- **Removal theory**: It could stem from *\*ex-sulere* ("to take out"), relating to the root *\*selh-* ("to take"), similar to *consul*.

- **Walking/driving theories**: Alternative origins link it to *amb-ulare* ("to walk") or *\*helh-* ("to drive").

An ancient folk etymology incorrectly attributed the second element to Latin *solum* ("soil").
```


## [2026-09-04T19:34:57.635Z] TOOL CALL #41: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A2%D9%88%D8%A7%D8%B1%D9%87' --note 'page 48, root Al 4, Persian node avareh: Wiktionary derives آواره from آوار + -ه, no PIE *al- root' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A2%D9%88%D8%A7%D8%B1' --note 'page 48, root Al 4: Wiktionary آوار from OPers *awa-bar-/*a-bar-, cf. Parthian ʾwʾr, Old Armenian awar' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D5%A1%D6%82%D5%A1%D6%80' --note 'page 48: Old Armenian awar \"loot\" < Iranian, Parthian ʾwʾr, Proto-Iranian *HwarH-' 2>&1 | tail -20",
 "description": "Archive Persian-side URLs"
}
```


### [2026-09-04T19:35:00.108Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/671f8a98de672f0d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/16227354160a952b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9c58dcee3191ba0b.txt
```


## [2026-09-04T19:35:03.682Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/ambulo' --note 'page 48, Latin node: ambulo < ambi- + *alo < PIE *h2elh2- (de Vaan 2008 p.38)' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/exsul' --note 'page 48, Latin node: exsul of uncertain origin, one proposal *h2el- \"to wander\"' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82elh%E2%82%82-' --note 'page 48, root box: PIE *h2elh2- \"to wander, roam\", LIV/Beekes; no Iranian descendant' ; python3 tools/fetch_source.py 'https://www.etymonline.com/word/alley' --note 'page 48, English node: alley < OFr alee < aler < L ambulare' ; python3 tools/fetch_source.py 'https://www.etymonline.com/word/exile' --note 'page 48, English node: exile < L exilium < exsul; competing roots *al- wander / *selh- / *helh-' ; python3 tools/fetch_source.py 'https://www.vajehyab.com/dehkhoda/%D8%A2%D9%88%D8%A7%D8%B1%D9%87' --note 'page 48, Persian node: Dehkhoda آواره, links to آوار' 2>&1 | tail -25",
 "description": "Archive remaining URLs"
}
```


### [2026-09-04T19:35:05.542Z] TOOL RESULT

```
python3: can't open file '/home/sfmqrb/tools/fetch_source.py': [Errno 2] No such file or directory
python3: can't open file '/home/sfmqrb/tools/fetch_source.py': [Errno 2] No such file or directory
python3: can't open file '/home/sfmqrb/tools/fetch_source.py': [Errno 2] No such file or directory
python3: can't open file '/home/sfmqrb/tools/fetch_source.py': [Errno 2] No such file or directory
python3: can't open file '/home/sfmqrb/tools/fetch_source.py': [Errno 2] No such file or directory
python3: can't open file '/home/sfmqrb/tools/fetch_source.py': [Errno 2] No such file or directory
```


## [2026-09-04T19:35:11.883Z] TOOL CALL #43: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/ambulo' --note 'page 48, Latin node: ambulo < ambi- + *alo < PIE *h2elh2- (de Vaan 2008 p.38)' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/exsul' --note 'page 48, Latin node: exsul of uncertain origin, one proposal *h2el- \"to wander\"' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82elh%E2%82%82-' --note 'page 48, root box: PIE *h2elh2- \"to wander, roam\", LIV/Beekes; no Iranian descendant' ; python3 tools/fetch_source.py 'https://www.etymonline.com/word/alley' --note 'page 48, English node: alley < OFr alee < aler < L ambulare' ; python3 tools/fetch_source.py 'https://www.etymonline.com/word/exile' --note 'page 48, English node: exile < L exilium < exsul; competing roots *al- wander / *selh- / *helh-' ; python3 tools/fetch_source.py 'https://www.vajehyab.com/dehkhoda/%D8%A2%D9%88%D8%A7%D8%B1%D9%87' --note 'page 48, Persian node: Dehkhoda آواره, links to آوار' 2>&1 | tail -25",
 "description": "Archive remaining URLs (correct cwd)"
}
```


## [2026-09-04T19:35:13.438Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"planlos umherschweifen\\|planlos\" WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "Grep Walde-Pokorny Band 1 for the root"
}
```


### [2026-09-04T19:35:15.247Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/aff53b571fba8aa8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/660989c4113fc221.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d2b28f6b3e6f30da.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b205b68f254a6d88.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/22cf154d59d8331b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d1f381017731dd5e.txt
```


### [2026-09-04T19:35:15.291Z] TOOL RESULT

```
5788:3. al- „planlos umherschweifen, irren; auch geistig irre sein“. 
10145:; : ambio) s. dl- „planlos umherschwcifen u . — Alb prjtr „drehe um, kehre 
10935:mit lat. (ilea ist triigerisch ; s. dariiber u. al- ,,planlos umherschw r eifen“) : 
45465:lings, planlos, aufs Geratewohl“ (Loc. *temesi „im dunkeln [tappend] 44 ,
```


## [2026-09-04T19:35:18.019Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '5788,5820p' WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Print Walde-Pokorny al- entry"
}
```


### [2026-09-04T19:35:18.070Z] TOOL RESULT

```
3. al- „planlos umherschweifen, irren; auch geistig irre sein“. 

Gr. dXt] „das Umherschweifen 41 , aXaoficu (hom. Pf. aXaXrjpai), dXaivm 
„schweife umher 441 ), aXyzyg „Bettler“, aXyzevco „sehweife bettelnd umher“ 
dXiog „vergeblich“, uXiom „vereitle“ („vergeblich“ aus dem Begriffe des 
Planlosen, s. unten yXepazog, t)Xl&iog-, Spiritus asper freilich noch unerkliirt, 
s. Boisacq 44, auch gegen die Annahme von anl. j:-) ; von einer Basis 

1 ) Dazu auch a/.a^cor „ Aufschneider, Piahler 11 (eigentlich heruniziehender Gaukler, 

Marktschreier 14 ) nach Boisacq 40 (von Prellwitz 2 22 zur Interjektion *ald gezogen 14 ). 



88 


al- 


*alu *aleu- gr . aXvco „bin auBer mir“ 2 ), akvaaco ds. (Horn.; Fut. alv&i 
Hippokr.), aXvy.i] „Unruhe, Beangstigung“, dkvy.rem (Pf. akalvy.Trjfj.ai Horn.), 
dkvy.Ta£(o „bin in Angst“, dkvaig (von akvm) „Angst“, dkva/iog „Bangigkeit“, 
dkvg, - vo g (Pint.) „mfiBiges Herumtreiben, Langweile" (s. auch Persson 
Beitr. 739 gegen Hirt Abl. § 510); mit dem Begriffe „umherirren, um einer 
gefahrlichen Stelle oder Sache nicht zu nahe zu kommen“ auch dkevo/jat, 
akeouai „vermeide“ (nachhom. auch aktiv dkevco „wende ab“), jon. akh] 
„das Vermeiden, Schutz", AXvaxm (*akvx-oxco, vgl. Aor. ijkv£a) „entkomme“, 
akvoy.d£co „vermeide, fliehe“, aksslvco ds., ahmoi) „Abwehr“ (*dkefcoh] 
Bildung wie cpetdmh)). Mit a-: ijkaoy.i o „irre umlier“, fj?.aoxd£m „ds., ver- 
meide“ (Horn.), fjkaivm „bin wahnsinnig“, Med. „schweife umher“, fjke/jaTog 
(dor. ukefiaxog Theokr.) „toricht, eiiel“, ijki&iog „nichtig, vergeblich, toricht“, 
yksog „verwirrt, betdrt ; verwirrend" (daneben die aol. Entsprechung ukkog
```


## [2026-09-04T19:35:22.235Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '5820,5850p' WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Print more of WP al- entry"
}
```


### [2026-09-04T19:35:22.291Z] TOOL RESULT

```
yksog „verwirrt, betdrt ; verwirrend" (daneben die aol. Entsprechung ukkog 
eines *akiog, vgl. ygvaiog neben yovaeog, in :) hom. dkka cpQovemv „cpQEva? 
ijkeog „betaubt, bewu8tlos“ (Pick II 390, wonach auch der Yok. >)ki II. 15, 128 
Ionisierung eines aol. dike . Vgl. fiber die gr. Worte zuletzt Bechtel Lexil. 
32 f., 157 f. (aus dor. *<lkeog stammt lat. idea „blindes Glfick, \Vfirfel“, das nicht 
besser von Prellwitz BB. 20, 303 besonders urverwandt aufgefaBt wird). 

Dazu lett. ahidt, aludties ,.umherirren, sich verirren" (Fick BB. 2, 264), 
mit a lett. cil’a „halb verriickter Mensch“, dVuoties „sich narrisch gebarden“ 
(Prellwitz 1 113, 2 172). 

Aber lat. anibulo „spaziere“ ist nach Samuelsson Glotta 6, 252 ff. Demi- 
nutiv zu ambio (umbr. amboltu scheint nicht „ambulato“ zu bedeuten). Lat. 
alucinor „rede gedankenlos ins Blaue hinein, bin geistesabwesend“ ist wohl 
aus dkvy.rj, dkvoaco unter formaler Anlehnung an vaticinor entlehnt (s. Yf. 
LE Wb. 2 29). liber ai. dlakam „vergeblich, umsonst“ s. Uhlenbeck IF. 25, 143. 

4. al- „brennen“. 

Lat. adoleo „verbrenne (bes. Opfer)“, udolesco, -ere „auflodern (von Al- 
taren)“ (o aus a, wie im etymologisch verschiedenen adolescere ,,heran- 
wachsen“ zu alo, s. unter *al- „nahren“), altare „Brandaltar“ (umbr. uretu 
„adoleto?“); ai. alatam „Feuerbrand, Kohle“ (auch uhnukam „Brand“?); 
nschwed ala „lodern, flammen“ (Johansson ZfdtPh. 31, 285ff 2 ) m. Lit.); 
ganz zweifelhaft gr. dka^rj • uv&gay.eg Hes. (Petersson IF. 34, 241). S. noch 
Yf. LEWb. 2 12, 22; Auffassung auch von lat. alaccr, got. aljan „Eifer“ usw. 
als „feurig, hitzig'' (Johansson aaO.) ist ganz fraglich ; fiber ags. celan „brennen“ 
s. *aidh-. DaB elai{$-)ov „Ol“ als „das brennbare“ benannt sei (Prellwitz 2 
s. v.; Urverwandtschaft von arm. eid, g. iuhy ,,01“ damit ist durch Peder- 
sen KZ. 39, 402 nicht erwiesen), ist an sich ganz unwahrscheinlich, auch 
weicht der Yokal ab.
```


## [2026-09-04T19:35:54.946Z] TOOL CALL #47: Bash

```json
{
 "command": "ls data/ && ls data/extracted | head",
 "description": "Check for page images of the book"
}
```


### [2026-09-04T19:35:54.990Z] TOOL RESULT

```
ANOMALIES.md
extracted
EXTRACTION_SPEC.md
research
translations
verification
batch
NEXT_CHUNK
RETRY.txt
test
```


## [2026-09-04T19:35:58.244Z] TOOL CALL #48: Bash

```json
{
 "command": "sed -n '60,140p' tools/verify_check.py",
 "description": "Read rest of verify_check.py"
}
```


### [2026-09-04T19:35:58.300Z] TOOL RESULT

```
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


## [2026-09-04T19:38:27.375Z] TOOL CALL #49: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-48.json",
 "content": "{\n  \"pdf_page\": 48,\n  \"book_page\": 18,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Al 4, Âlĕiô, Âleŭos\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂elh₂- 'to wander, roam' (= Pokorny '3. āl- planlos umherschweifen, irren', IEW 27; Watkins/AHD al-² 'to wander')\",\n      \"note\": \"The root box is right on all three counts. Pokorny IEW p.27 has '3. āl- „planlos umherschweifen, irren; auch geistig irre sein“' with Gk. ἄλη, ἀλάομαι, ἀλαίνω, ἀλήτης, Lett. aluot, Toch. AB āl-, and explicitly 'von einer Basis alu-, aleu-' — which is where Nourai's second and third headword forms come from: they are S. E. Mann's headwords 'áleiō' (OCR'd 'áleiđ') 'rove, roam' and 'aleuos' 'wandering, restless, raving' on IEC p.14, not Nourai's own inventions. 'Al 4' is Nourai's own numbering (Pokorny numbers this root 3. āl-, AHD numbers it al-²). Modern reconstruction with laryngeals is *h₂elh₂- (LIV² 264, Beekes EDG s.v. ἀλάομαι). Two cross-cutting caveats, developed at the nodes: (a) the attachment of Latin ambulāre/exsul to this root has been contested since Walde-Pokorny I 88 (1930), though Pokorny 1959, Watkins and de Vaan 2008 all accept it; (b) NO Iranian reflex of *h₂elh₂- is recognised by any modern Iranist — the Persian branch of this chart rests on a single line in Mann.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82elh%E2%82%82-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:27\", \"status\": \"supports\", \"note\": \"POK_01.txt ff-page 36 (= printed p.27, offset leaf = p+8): '3. āl- „planlos umherschweifen, irren; auch geistig irre sein“. Gr. ἄλη „das Umherschweifen“, ἀλάομαι … ἀλήτης „Bettler“ … Dazu lett. aluot, aluoties „umherirren, sich verirren“ … Toch. AB āl- … WP. I 87 f., WH. I 33, 38'. Page and gloss are exactly Nourai's.\"},\n        {\"ref\": \"AHD:1505\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 280: 'al-2, To wander. 1. Latin ambulāre, to go about, walk (ambi-, around; see ambhi): ALLEY¹, AMBULATE; FUNAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.]' — the appendix page 1505 of the 1975 New College ed. is the 'al-' opening page; content matches.\"},\n        {\"ref\": \"IEC:14\", \"status\": \"supports\", \"note\": \"IEC.txt ff-leaf 24 (printed p.14): 'áleiō, al- „rove, roam“. Cf. aleuos — Per. cf. àv-ara, cpd. adj. „wandering“; Gk. ἀλάσκω, ἐλαίνω, beside ἀλάομαι; Lat. cf. … p-ālor, pālāri „wander“; Latv. aleties „be restless“' and, immediately below, 'aleuos „wandering, restless, raving“. Cf. áleiō — Per. cf. av-ara „wandering“; Gk. eleós; Latv. alava'. Both of Nourai's extra root names and his Persian branch come from this one page.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"IEW p.27 (POK_01.txt ff-page 36)\", \"stance\": \"supports\", \"note\": \"'3. āl- „planlos umherschweifen, irren“'; footnote 'WP. I 87 f., WH. I 33, 38, EM. 43 (stellt ambulō zu gr. ἐλαύνω, St. el-)' — Pokorny himself flags the Latin disagreement.\"},\n        {\"src\": \"WLD\", \"where\": \"WP I 87-88 (WLD_Bd1 djvu line 5788)\", \"stance\": \"partial\", \"note\": \"'3. al- „planlos umherschweifen, irren; auch geistig irre sein“' — same root, same gloss, but with 'Aber lat. ambulo „spaziere“ ist nach Samuelsson Glotta 6, 252 ff. Deminutiv zu ambio', i.e. Walde-Pokorny 1930 keeps the root and rejects the Latin members that Nourai attaches to it.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins, IE Roots appendix s.v. al-²\", \"stance\": \"supports\", \"note\": \"'al-2, To wander … [Pok. 3. al- 27.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann p.14 s.vv. al-, áleiō, aleuos\", \"stance\": \"supports\", \"note\": \"'al- „wander, go“. Cf. al-eiō — Gk. aláomai; LLat. alare (or alar) „hunt“, cpd. in amb-ulāre, simplex in OFr. aler.'\"},\n        {\"src\": \"Wiktionary/LIV\", \"where\": \"Reconstruction:Proto-Indo-European/h₂elh₂-\", \"stance\": \"supports\", \"note\": \"'*h₂elh₂- to wander, roam' (imperfective), refs Rix LIV² 2001, Beekes EDG 2010; descendants Gk. ἀλάομαι/ἀλύω/ἄλη, Lat. alucinor and ambulō, Latv. aloties, Toch. AB āl-. No Iranian descendant is listed.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"âvâreh «آواره» (also آوار)\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"NP آواره āvāre 'driven from home, wanderer, exile' is transparently آوار āvār + the Persian nominal/adjectival ending ـه -a(h) (so Wiktionary, Dehkhoda and Mo'in, who all cross-reference the two words: Borhan-e Qateʿ 'آوار … مخفف آواره است که از خان و مان دور افتاده باشد'). The chart's arrow presupposes an Old Iranian *ava-ara- 'wandering away' = preverb *ava- 'away, down' + a verbal noun *ara- from *h₂elh₂-; PIE *l does regularly become Indo-Iranian r, so this is not phonetically impossible, and it is exactly Mann's analysis ('Per. cf. àv-ara, cpd. adj. „wandering“', IEC 14). But no Iranian language attests any verb from *h₂elh₂-: Cheung's Etymological Dictionary of the Iranian Verb (2007) has no such root (grep for 'to wander' returns only *bramH, *gar-, *wyāb-, *pauy-), and Wiktionary's *h₂elh₂- page lists no Iranian descendant at all. The base آوار is meanwhile well attested in the concrete senses 'debris of a collapsed building, ruin' and 'plunder, oppression' and has an exact Iranian pedigree outside Persian — Parthian ʾwʾr, MP ʾwʾl, Pashto avār 'plunder, booty', borrowed into Old Armenian as աւար awar 'loot, spoils' — pointing to Old Iranian *awa-bar- 'to carry off' (Wiktionary) or *HwarH- 'to tear away, plunder' (Wiktionary s.v. awar), with the semantic path 'plundered, laid waste, scattered' → 'ruined, dispersed' → 'driven from home, vagrant'. On that account āvāre has nothing to do with 'wander' etymologically and the arrow is wrong. Verdict: disputed — the derivation rests on Mann alone, and the mainstream Iranian evidence points to the *bar-/*HwarH- 'carry off, plunder' family.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A2%D9%88%D8%A7%D8%B1%D9%87\",\n            \"https://en.wiktionary.org/wiki/%D8%A2%D9%88%D8%A7%D8%B1\",\n            \"https://en.wiktionary.org/wiki/%D5%A1%D6%82%D5%A1%D6%80\",\n            \"https://www.vajehyab.com/dehkhoda/%D8%A2%D9%88%D8%A7%D8%B1%D9%87\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82elh%E2%82%82-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:14\", \"status\": \"supports\", \"note\": \"IEC.txt ff-leaf 24 (printed p.14): 'áleiō, al- „rove, roam“ … Per. cf. àv-ara, cpd. adj. „wandering“' and 'aleuos „wandering, restless, raving“ … Per. cf. av-ara „wandering“'. Mann does say what Nourai's arrow says (note his hedging 'cf.' and that he cites no Middle Iranian form); the page number is right.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"vol. 1 p.65 (BQT_v1_pages.txt ff-leaf 275; printed ≈ leaf−210)\", \"stance\": \"partial\", \"note\": \"'آوار، بر وزن ناچار. مخفف آواره است که از خان و مان دور افتاده باشد - و بمعنی آزار و ستم هم آمده است - و حسب و حساب را نیز گویند - و بمعنی خراب هم آمده است که ضد آباد باشد' and 'آواره … نابود شده و گم گردیده و پراکنده و پریشان گشته و بی‌نام و نشان و از وطن دور افتاده و سرگردان شده را گویند'. Word and gloss confirmed; Moʿin's numbered footnotes on this page concern آواز (Av. vac-) and آور, not آواره — no etymology is offered for it.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.vv. آوار / آوارگی / آواره (MON_part1.txt lines 5161-5180)\", \"stance\": \"partial\", \"note\": \"'آوار۱ [- آواره] (ص.) از خانمان و وطن به دور افتاده، در به در. خراب، ویران، برافتاده' / 'آواره [- آوار] (ص.) از وطن دور افتاده، در به در …'. Moʿin derives آواره from آوار (and vice versa) and gives NO origin tag — no [په.] Pahlavi tag, no IE root.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss der neupers. Etymologie — grep 'âwâr/awâra' in HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn has no entry for āvār/āvāra (only the unrelated string 'ei-awära' in the index, p.462); the word is not treated.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien — grep 'awâr/âwâr' in HUB.txt\", \"stance\": \"silent\", \"note\": \"Hübschmann has no entry for āvār/āvāra; hits are only for paz. awar 'auf, über' (= phl. apar) and Pazand dawar, abr, unrelated.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb (2007), grep 'āwāra', 'HwarH', 'to wander'\", \"stance\": \"silent\", \"note\": \"No root that would yield āvāra; the verbs glossed 'to wander, roam' are *bramH, *gar-, *wyāb-, *pauy- — none from *h₂elh₂-. Cheung's silence is the strongest single argument against the arrow.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary — grep 'āwār', 'awārag'\", \"stance\": \"silent\", \"note\": \"No Middle Persian *āwārag is recorded (only frawār 'bastion', frawārdan 'to serve food'), so the chart's Persian word has no attested MP ancestor in MacKenzie.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi — grep 'آوار' in ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"No hit for آوار/آواره in the OCR of the Persian headword file (nor for 'avare' in the Latin index); Aryanpur does not list this word among Persian words of IE root — or the OCR failed on it.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.vv. آواره, آوار, աւար\", \"stance\": \"contradicts\", \"note\": \"آواره is analysed as 'آوار + ـه'; آوار as 'perhaps from Old Persian *awa-bar- „to take away“ or *ā-bar-', cognate Parthian ʾwʾr, MP ʾwʾl 'booty, plunder', Pashto avār; Old Armenian աւար awar 'loot, spoils' is 'an Iranian borrowing … ultimately from Proto-Iranian *HwarH- „to pluck, tear out; to rob, plunder“'. No *h₂elh₂- anywhere.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Latin\",\n          \"words\": \"ulâre; amb-ulâre; ex-ul\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin never had a free-standing verb *ulāre: the form Nourai prints as a Latin word is the abstracted second member of ambulāre, and its -u- is merely the composition/reduction vowel of *amb-al-ā- (Klein s.v. amble: 'L. ambulāre … which prob. stands for *amb-al-āre'). ambulāre 'to go about, walk' is attested from Plautus on (in ius ambulā; quo ambulās tu), with an Umbrian cognate amboltu, and is derived by Pokorny (IEW 27), Watkins (AHD al-²) and de Vaan (EDL 2008: 38, followed by Wiktionary) from *h₂m̥bʰi 'around' + *h₂elh₂- 'to wander' → Proto-Italic *ambi-alā-; it displaced īre in colloquial and late Latin and gave OFr aler, Fr. aller, Rum. umbla (Buck 10.47, REW 412). exsul/exul 'a banished man' = ex- 'out' + the same *-al-/-ul- element ('wandering outside' → 'exile'), whence exsilium 'banishment'. The reservations: Walde-Pokorny I 88 (1930) removes ambulō from this root ('Aber lat. ambulo „spaziere“ ist nach Samuelsson Glotta 6, 252 ff. Deminutiv zu ambio'); Ernout-Meillet (1951, s.v. ambulō) prefer a root *el- 'aller' (Gk. ἐλαύνω, Celtic ei) and say of ἀλάομαι/Latv. aluot that 'les sens sont trop différents'; Klein calls exsul 'of uncertain origin', and Wiktionary lists *selh₂- 'to take' (cf. cōnsul, praesul) and *h₁elh₂- 'to drive' as live rivals. Since the current standard Latin etymological dictionary (de Vaan) does take ambulō to *h₂elh₂-, the arrow is defensible; the unattested Latin headword 'ulâre' and the genuinely open question of exsul keep it at plausible rather than confirmed.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/ambulo\",\n            \"https://en.wiktionary.org/wiki/exsul\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1505\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 280 s.v. al-²: '1. Latin ambulāre, to go about, walk (ambi-, around; see ambhi) … 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs)'. Watkins supports both Latin words, but gives no simplex 'ulāre' — that form is Nourai's own back-formation.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW p.27 (POK_01.txt ff-page 36)\", \"stance\": \"supports\", \"note\": \"'Lat. ambulō „spaziere“ (umbr. amboltu „ambulato“)' listed under 3. āl-, with the caveat 'EM. 43 (stellt ambulō zu gr. ἐλαύνω, St. el-)'. Pokorny does not mention exsul here.\"},\n            {\"src\": \"WLD\", \"where\": \"WP I 88 (WLD_Bd1 djvu lines 5830-5832)\", \"stance\": \"contradicts\", \"note\": \"'Aber lat. ambulo „spaziere“ ist nach Samuelsson Glotta 6, 252 ff. Deminutiv zu ambio (umbr. amboltu scheint nicht „ambulato“ zu bedeuten).' Walde-Pokorny 1930 excludes exactly the words this node contains.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.vv. ambulō (p.28) and exsul (p.209)\", \"stance\": \"partial\", \"note\": \"s.v. ambulō: 'La forme radicale *el- apparaît en second terme de composé: ex-ul … On a en outre rapproché gr. ἀλάομαι, lette aluot „errer“, dont les sens sont trop différents, et, mieux, le groupe de gr. ἐλαύνω'. s.v. exsul: 'Doit plutôt se rattacher à la racine verbale qu'on a dans amb-ulo-.' Ernout-Meillet thus confirm the ambulāre ≍ exsul link (Nourai's grouping) but assign both to *el- 'to go', not to āl- 'to wander'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.vv. amble and exile (KLN_1966.txt lines 2437, 14043)\", \"stance\": \"partial\", \"note\": \"amble: 'fr. L. ambulare … which prob. stands for *amb-al-are, fr. amb- and I.-E. base *al-, „to go“, whence also Gk. ἄλη … Lett. aluot' — supports. exile: 'fr. exul, exsul, „a banished person, wanderer“, which is of uncertain origin. It possibly stands for *eks-al-s and is formed fr. ex- and I.-E. base *al-, „to wander about“' — supports only tentatively.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §10.47 'go' (SYN.txt line 17527)\", \"stance\": \"silent\", \"note\": \"'Lat. ambulare „walk“ (10.45), used colloquially for „go“ in Plautus (quo ambulas tu, bene ambula) and regularly in late Latin. Hence Fr. aller, Rum. umbla. REW 412.' Confirms the Latin word and its Romance fate; gives no IE root.\"},\n            {\"src\": \"Wiktionary/de Vaan\", \"where\": \"en.wiktionary.org s.vv. ambulo, exsul\", \"stance\": \"partial\", \"note\": \"ambulō 'from ambi- + *alō „to wander“, from PIE *h₂elh₂-', citing de Vaan EDL (2008) p.38 — supports. exsul: 'uncertain', with *selh₂- (as in cōnsul), *h₂el- 'to wander' and *h₁elh₂- 'to drive' all listed as proposals.\"},\n            {\"src\": \"LEW\", \"where\": \"Walde LEWb 2nd ed. 1910 (LEW_1910.txt)\", \"stance\": \"silent\", \"note\": \"grep 'ambul' / 'exsul' / 'exul' returns no entry — the local scan is defective/indexed only for these letters, so Walde-Hofmann could not be read directly.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"alley, preamble, ambulate, exile\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All four are Latin-mediated and the chain is uncontroversial. ALLEY: L ambulāre > Gallo-Romance *alāre (Mann, IEC 14, notes the Late Latin simplex alāre in Servius, 4th c. AD) > OFr aler 'to go', whose fem. past participle alee 'a going, passage, corridor' (13th c.) gave ME aley, mid-14th c. 'passage in a house, walk in a garden', and c.1500 'long narrow enclosure for bowls'. PREAMBLE: LL praeambulus 'walking before' (prae- + ambulāre) > ML praeambulum, neuter adj. used as a noun > MF preambule > ME preamble (late 14th c.). AMBULATE: a 16th-c. learned formation directly on ambulāt-, the pp. stem of ambulāre (compare perambulate, circumambulate, funambulist). EXILE: L exsilium/exilium 'banishment' (from exsul) > OFr exil/essil > ME exil, c.1300, first 'banishment' then 'the banished person'; the verb from OFr essillier < LL ex(s)iliāre. The English forms therefore descend from node #2 exactly as drawn; whatever doubt attaches to the Latin words' PIE root does not touch this edge.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/alley\",\n            \"https://www.etymonline.com/word/exile\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 280 s.v. al-² lists precisely 'ALLEY¹, AMBULATE; FUNAMBULIST, PREAMBLE' under Latin ambulāre and 'EXILE' under Latin exsul; the reverse index (line 1237) has 'AMBULATE al-2'. Nourai's page-less 'AHD' citation is accurate.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.vv. alley, ambulate, preamble, exile (KLN_1966.txt lines 2269, 2437, 29938, 14043)\", \"stance\": \"supports\", \"note\": \"alley: 'OF. alee (F. allée), „a going, passage“, prop. fem. pp. of OF. aler (F. aller), „to go“, fr. L. ambulāre'. ambulate: 'L. ambulāt-(um), pp. stem of ambulāre'. preamble: 'fr. ML. praeambulum … fr. Late L. praeambulus, „walking before“, fr. praeambulāre'. exile: 'fr. L. exilium, exsilium … fr. exul, exsul'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.vv. Amble and exile (SKT.txt lines 618, 17739)\", \"stance\": \"partial\", \"note\": \"Amble: 'M.E. amblen, F. ambler, to go at an easy pace — L. ambulare, to walk. ¶ Perhaps for amb- about + [root] to go' — supports the Latin chain. exile: 'O.F. exil … L. exilium, better exsilium, banishment — L. exsul, a banished man, one driven from his native soil. — L. ex, out of; solum, soil ¶ But now gen. der. from L. salio, to leap' — i.e. Skeat backs neither of the modern proposals and repeats the ancient solum folk-etymology.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/alley and /word/exile\", \"stance\": \"supports\", \"note\": \"alley: 'from Old French alee (13c.) „a path, passage, way, corridor“, … fem. of ale, past participle of aler „to go“, which might be a contraction of Latin ambulare „to walk“'. exile (n.): 'c.1300, from Old French exil/essil, from Latin exilium „banishment; place of exile“, from exsul „banished person“', with '*al- „to wander“ (cf. Greek alaomai)' given as one of the proposed sources of exsul.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-04T19:38:27.409Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-48.json (file state is current in your context — no need to Read it back)
```


## [2026-09-04T19:38:30.133Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-48.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 48",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-04T19:38:32.046Z] TOOL RESULT

```
JSON OK
nodes verified: 3/3
node verdicts: {'disputed': 1, 'plausible': 1, 'confirmed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 3}
books consulted: {'partial': 6, 'silent': 7, 'contradicts': 2, 'supports': 3} | by book: {'KLN': 2, 'BQT': 1, 'MON': 1, 'HRN': 1, 'HUB': 1, 'CHEUNG': 1, 'PHD': 1, 'ARY': 1, 'Wiktionary': 1, 'POK': 1, 'WLD': 1, 'LAT': 1, 'SYN': 1, 'Wiktionary/de Vaan': 1, 'LEW': 1, 'SKT': 1, 'Etymonline': 1}
```


## [2026-09-04T19:38:50.111Z] AGENT

Written `/home/sfmqrb/git/rishe/data/verification/page-48.json`; `verify_check.py 48` runs clean (3/3 nodes, no PROBLEM lines).

**Page 48 (book p. 18) — 1 real entry (entry 1 is a redirect, skipped)**

- Root verdicts: confirmed 1
- Node verdicts: confirmed 1, plausible 1, disputed 1
- Nourai's own refs checked: POK:27, AHD:1505, IEC:14, AHD — all 4 `supports` (all read in the local texts and quoted)
- Other books consulted: 17 lookups — supports 3, partial 6, contradicts 2, silent 7 (POK, WLD, AHD, IEC, LAT, LEW, KLN, SKT, SYN, HRN, HUB, CHEUNG, PHD, BQT, MON, ARY, Wiktionary/de Vaan, Etymonline). 9 web pages archived via `fetch_source.py`.

Root "Al 4, Âlĕiô, Âleŭos" = Pokorny "3. āl- planlos umherschweifen" (IEW 27) = Watkins al-² = PIE *h₂elh₂-; confirmed. The extra names Âlĕiô/Âleŭos are Mann's headwords áleiō / aleuos on IEC p.14, not Nourai's coinages.

Flagged items:
- **disputed — #1 Persian âvâreh آواره**: the arrow rests solely on Mann IEC 14 ("Per. cf. av-ara, cpd. adj. 'wandering'"). No Iranist recognises any Iranian reflex of *h₂elh₂- — Cheung 2007 has no such verb, Wiktionary's *h₂elh₂- page lists no Iranian descendant, Horn/Hübschmann/MacKenzie are silent. The base آوار 'debris, ruin; plunder' has an independent pedigree (Parthian ʾwʾr, MP ʾwʾl, Pashto avār, borrowed as Old Armenian աւար awar 'loot'), pointing to OIr. *awa-bar- 'carry off' / PIr. *HwarH- 'plunder'; Borhan-e Qateʿ (v.1 p.65) and Moʿin both derive آواره simply from آوار and give no etymology.

Other note worth relaying: node #2 (Latin) is only **plausible** — Nourai prints a Latin headword *ulâre* that never existed as a free verb (it is the second member of amb-ulāre, with the composition vowel), and exsul's root is genuinely open (Klein "of uncertain origin"; Wiktionary lists *selh₂-/*h₁elh₂- as rivals). Walde-Pokorny I 88 explicitly excludes ambulō from this root ("Deminutiv zu ambio") and Ernout-Meillet prefer *el- (Gk ἐλαύνω); de Vaan 2008 p.38, Pokorny 1959 and Watkins do support *h₂elh₂-, so the arrow stands but with a live dissent.
