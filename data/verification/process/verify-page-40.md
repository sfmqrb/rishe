# Verification process log — verify-page-40


## [2026-09-04T18:56:23.683Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 40 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-40.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-40.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-40.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 40` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T18:56:25.279Z] AGENT

I'll start by reading the instructions.


## [2026-09-04T18:56:27.413Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T18:56:27.426Z] TOOL RESULT

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


## [2026-09-04T18:56:27.585Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-40.txt"
}
```


### [2026-09-04T18:56:27.606Z] TOOL RESULT

```
1	=== PDF page 40 (book page 10) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Aik, Ěik : to possess, own  (refs POK:298; KLN:1106)
4	#1 (parent #0) [Avestan] refs=POK:298; KLN:1106; SYN:771,772 | îs, îše, îšti, âěšâ 1 : wealth, power ; îsvan, išvan : wealthy
5	#2 (parent #0) [Germanic] refs=AHD | aigan : to possess
6	  #3 (parent #2) [English] refs=None | own, owe, ought
7	--- entry 1 ---
8	ROOT [Indo-European] Aios, Ayos : metal  (refs POK:15; KLN:1093)
9	#1 (parent #0) [Avestan] refs=POK:15; KLN:1093 | ayô, ayah, ayanh : metal, bronze
10	  #2 (parent #1) [Pahlavi] refs=BQT:70; HRN:14 | âsîn, âhěn : metal, iron
11	    #3 (parent #2) [Persian] refs=BQT:70; SYN:612 | Âhan «آهن» : iron, anything hard
12	#4 (parent #0) [Latin] refs=AHD:443 | aes : bronze, money ; aera : counters for counting, also an era of time
13	  #5 (parent #4) [English] refs=None | era
14	#6 (parent #0) [Germanic] refs=AHD:925 | 
15	  #7 (parent #6) [English] refs=None | ore
16	
```


## [2026-09-04T18:56:32.388Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-40.json && echo \"=== MATRIX ===\" && cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T18:56:32.434Z] TOOL RESULT

```
{
  "pdf_page": 40,
  "book_page": 10,
  "entries": [
    {
      "root": {
        "name": "Aik, Ěik",
        "lang": "Indo-European",
        "refs": "POK:298; KLN:1106",
        "gloss": "to possess, own"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:298; KLN:1106; SYN:771,772",
          "words": [
            {
              "translit": "îs, îše, îšti, âěšâ 1",
              "gloss": "wealth, power",
              "script": null
            },
            {
              "translit": "îsvan, išvan",
              "gloss": "wealthy",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "aigan",
              "gloss": "to possess",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "own, owe, ought",
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
        "name": "Aios, Ayos",
        "lang": "Indo-European",
        "refs": "POK:15; KLN:1093",
        "gloss": "metal",
        "note": "KLN:1093 claims that this word may have been driven from \"Ayashya\", ancient name of Cyprus, meaning Cyprus metal."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:15; KLN:1093",
          "words": [
            {
              "translit": "ayô, ayah, ayanh",
              "gloss": "metal, bronze",
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
          "refs": "BQT:70; HRN:14",
          "words": [
            {
              "translit": "âsîn, âhěn",
              "gloss": "metal, iron",
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
          "refs": "BQT:70; SYN:612",
          "words": [
            {
              "translit": "Âhan",
              "gloss": "iron, anything hard",
              "script": "آهن"
            }
          ],
          "note": null,
          "quote": {
            "text": "آهن دلان به آه ملایم نمی‌شوند - چون قفل بسته را به نفس وا کند کسی؟",
            "poet": "Sa`eb"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:443",
          "words": [
            {
              "translit": "aes",
              "gloss": "bronze, money",
              "script": null
            },
            {
              "translit": "aera",
              "gloss": "counters for counting, also an era of time",
              "script": null
            }
          ],
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
              "translit": "era",
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
          "refs": "AHD:925",
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
              "translit": "ore",
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
}=== MATRIX ===
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


## [2026-09-04T18:56:39.151Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','KLN','SYN','AHD','BQT','HRN','HUB','BRT','PHD','NYB','WLD','IEC','SKT','LEW','LAT','MON','ARY','FSD','WEB','LKT','FRS','FSF','TLM','AVG','HID','ISS','SOD','CHEUNG','KNT','PEI','NAT','RCH','GPL','SIN','AFM','FVQ']:\n  if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:600])\n\""
}
```


## [2026-09-04T18:56:39.499Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py && echo ---- && ls data/verification/ | head -30"
}
```


### [2026-09-04T18:56:40.824Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs
TLM {"title": "H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Series, 1908", "edition_found": "1908", "kind": "archive_djvu", "url": "https://archive.org/details/ancientpersianle00tolm_0", "identifier": "ancientpersianle00tolm_0 (also in.ernet.dli.2015.90691, ancientpersianl00tolmgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/TLM.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 24 = p.4). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.
AVG {"title": "A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892", "edition_found": "1892", "kind": "archive_djvu", "url": "https://archive.org/details/pt1avestagrammar00jackuoft", "identifier": "pt1avestagrammar00jackuoft (also an-avesta-grammar-in-comparison-with-sanskrit, in.ernet.dli.2015.47742)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AVG.txt", "page_offset": "leaf = printed + 54 (e.g. leaf 61 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/det
HID {"title": "C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883", "edition_found": "1883", "kind": "archive_djvu", "url": "https://archive.org/details/handbuchderalti00bartgoog", "identifier": "handbuchderalti00bartgoog (also handbuchderalti01bartgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HID.txt", "page_offset": "leaf = printed + 13 (e.g. leaf 14 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Grammar by numbered 
ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
PEI {"title": "M. Pei, The Families of Words, New York 1962", "edition_found": "1962 (open copy)", "kind": "archive_djvu", "url": "https://archive.org/details/familiesofwords00inpeim", "identifier": "familiesofwords00inpeim (lending copies: familiesofwords00peim, bwb_FS0-ABP-200)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PEI.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 21 = p.3). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Popular p
NAT {"title": "C. Berlitz, Native Tongues, New York 1982", "edition_found": "2005 Castle Books reprint (open); 1982 original lending-only (nativetongues00berl)", "kind": "archive_djvu", "url": "https://archive.org/details/native-tongues-charles-berlitz-book-sales-ca-1997-3-printing-2005-castle-books-9", "identifier": "native-tongues-charles-berlitz-book-sales-ca-1997-3-printing-2005-castle-books-9", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NAT_2005.txt", "page_offset": "2005 reprint: leaf = printed + 15 (e.g. leaf 17 = p.2); reprint pagination may differ slightly from 1
RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 =
GPL {"title": "J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911", "edition_found": "1911", "kind": "archive_djvu", "url": "https://archive.org/details/grammarofpersian0000plat", "identifier": "grammarofpersian0000plat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt", "page_offset": "leaf = printed + 12 (e.g. leaf 17 = p.5). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Grammar organised by n
SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "loo
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
```


### [2026-09-04T18:56:40.868Z] TOOL RESULT

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
----
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
process
sources
```


## [2026-09-04T18:56:50.307Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==306' POK_01.txt | head -60"
}
```


## [2026-09-04T18:56:50.480Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==23' POK_01.txt | head -80"
}
```


### [2026-09-04T18:56:51.951Z] TOOL RESULT

```
,  wohl  auch  z.  T.  echtem  Gen.;  nach >Ieillet  Slave  comm.^  155,  505  reduktionsstufiges  bsl.  Hz  (?);  s.  auch Eüdzelin  Lett.  Gr.  33,  über  lett.  tz  507.
WH.  I  423  stellt  auch  arm.  Präverb  y-  (z.  B.  y-afnem  ,erhebe  mich' : lat.  ex-orior)  und  die  Präp.  mit  Abi.  i  ,von'  hierher  (unsicher);  ebenso z^veifelhaft  ist  Meillets  (MSL.  18,  409)  Erklärung  der  toch.  A-Postposition -5  ,von  wegen'  aus  *-ks.
Über  verbale  Komposita  in  mehreren  Sprachen,  wie  z.  B.  gr.  i'K-q)eQü), lat.  ef-ferö  ,trage  heraus*,  air.  as-hiur  ,sage'  (*efcs-bJierö)j  gr.  e^-SL[.u,  lat. ex-eö  ,gehe  heraus',  lit.  is-eiti,  aksl.  iz-iti  ds.  usw.,  s.  WH.  I  423  f.
WP.  I  116  f.,  WH.  I  423  ff.,   Trautmann  105,    Schwjzer  Gr.  Gr.  I  326.
cgnis  :  ognis  m.  , Feuer'.
Ai.  agni-h  m.  ,Feuer'  (=  hitt.  Agnisy  Hrozny  ZA.  38,  185,  nach  Laroche, Recherches  sur  les  noms  des  dieux  hittites  119,  von  den  Churritern  über- nommen) ;
lat.  igmsj  -is  m.  ,Feuer,  Flamme,  Licht,  Glut'  (*egnis)'j
lit.  ugriis  f.  (alit.  auch  m.,  Specht  KZ.  59,  278*),  lett.  uguns  m.  f.  ds.; das  i(>  stammt  von  aschwed.  ughn  ,Ofen';
aksl.  ognb  m.  , Feuer'  (* ognis ]  i-St.,  sekundär  20-St.),  öech.  ohefi  (ohnä), russ.  ogöub  {ognjd)]  über  cech.  vyhen  f.  , Rauchloch,  Esse',  skr.  viganj  m. ,Schmiede',  mit  ganz  unklarem  Anlaut,  s.  Meillet  Slave  comm.^  85,  zuletzt J.  Holub  Strucny  slovnik  etym.  jazyka  ceskoslov.  341.
WP.  I  323,  WH.  I  676,   Trautmann  334  f.
ebem,  eheu,  eho  Ausrufe,  meist  unabhängige  Neubildungen. Ved.  aha,  ai.  ahahu,  ahe,  ahö,  liamliö  usw.;
lat.  ehern,  hem  (Schallnachahmung  des  verlegenen  Räusperns),  eheu,  heu (:  äi.  aho)  ,ach,  oh!',  eho  ,lieda!';
nhd.   hem,  hum,  hm  (:  lat.   hem);  vgl.  nhd.  aha,  oho\', für  ai.  ah-,  lat.  eh-  könnte  man  idg.  *egh-  ansetzen. WP.  I  115,  WH.  I  396  und  oben  S.  281  e,  ö.
I.  ei-  ,gehen',  erweitert  ei-dh-,  ei-gh-,  i-tä-  und  i-ä-,  i-e-  :  iö-  :  19-]  Nominal- bildungen i'to-,  oi'UO-,  oi-tO'  und  i-ter,  Gen.  i-ten-os  ,Weg'. Ai.    imi,    kl,    imdh,   ydnti  ,gehen',  av.    aelti,   yeinti,   apers.  aitiy   ,geht', themat.  Med.  ai.  dya-te   usw.  (das  scheinbar   dehnstufige  ai.   äiti,   av.  äiti ,adit'  ist  *ä-a{ti,  mit  Präf.  ä);
294
gr.  hom.  elf.u  ,werde  gehen*,  ei  [
```


### [2026-09-04T18:56:53.465Z] TOOL RESULT

```
  , schändlich  handeln',  ags.  Icwiscie)  n. , Schande,  Vergehen',  Adj.  , schamlos*,  mnd.  eisch  , häßlich,  abscheulich', nnd.  eisk^  aisch  , ekelhaft,  garstig^
WP.  I  7,  Feist  30.
ä(i)gh-  :  igh-  , bedürfen,  begehren'.
Av.  äzi-s  m.  , Begierde',  np.  az  ds.,  av.  äza-§  ni.  , Streben,  Eifer';  ab- lautend av.  izyati  , strebt,  verlangt  nach'  und  Tzä  , Streben,  Eifer,  Erfolg' ai.  ihä  , Verlangen',  ihate  ,st!-ebt  wonach';
gr.  äxrjv  ,(iüvhig'  =  ijxrjveg'  ksvol,  Trrwxot  Hes.  (durch  Anlehnung  an  Worte,
15
mit  (i-privativum  daraus  dsxrjvsg'  TtevrjTsg  Hes.,  und  'äxe^ia  , Mangel,  Armut'), xc£(xvr]xrig'  ^^^'^N  K^^-'  ablautend  txccvccu)  ,beg-elire',  I^«^  , Begierde';
tocli.   A  äkäl,  B  akälk  , Wunsch,  Sehnsucht'.    Anders  Pedersen  Toch,  42.
WP.  I  40,  Van  Windekens  BSL.  41,  55;  unwahrscheinlich  Bartholomae IF.  5,  215.
äik' :  li-  , Spieß;  mit  einer  spitzen  Waffe  treffen'  (:  aigu-  ,Nadel'?).
Gr.  auloL'  al  ycjviai  lov  ßiXovg  lies.,  g'r.  Ursa'  dAÖvxiov  Hes.,  kypr. Uaauevog  oder  Ixiiaiievog  (in  letzterem  Falle  aus  ^'ly.af.iafxsvog)  , verwundet', IT  at/ü^  , Spieß'  (*aik-sma),  apr.  aysmis  , Bratspieß',  lit.  iesmas,  jiesmas Bratspieß',  (Grdf.  *aikmos  oder  dem  Gr.  genau  entsprechend  *'aik-smos)  ] ob  hierzu  apr.  ayculo,  ksl.  igla  usw.  , Nadel',  mit  g  statt  z  (vgl.  S.  18^)? lat.  Icö  (analog'isch  iciö),  -ere  , treffen,  verwunden^,  ictus  ,Hieb,  Stoß',  wohl auch  av.  isavd  , sogleich'  =  gv.  YKzao  ,nahe'  (als  , anstoßend')  und  l'yör], Hyötg  , Mörser'  (auch  f§,  hsg  ,den  Weinstock  schädigende  Würmer', woraus  'iTtsg  ds.  nach  den  bedeutungs verwandten  xvTrcsg,  Gv.viTteg^  O^QiTtsg umgebildet  sein  konnte;  anders  Schwyzer  Gr.  Gr.  I  299.  Hierher  mög- licherweise auch  anord.  eigin  n.  ^eben  hervorgesproßter  Saatkeim^  (,Spitze^), schwed.  mdartl.  äjel  m.  ds.  (Fick"*  III  2)  und  nd.  me  ^Grannen,  Ähren- spitze^  (Bezzenberger  BB.  27^   1G6).
WP.  I  7,  WH.  I  670,  Trautmann  3,  4.
aik-  ,anrufen'^(?).
Gr.  al'AaC,w  xaXst  Hes.,  lett.  aicindt  ^laden,  rufend
Aber  %aXet  kann  für  alycccllsi  ^schmeichelf^  verschrieben   sein,  und  aici- ndt eine  Ableitung  von  ai  ,höre!'    darstellen   (vgl.  vaicat  , fragen^  zu  vai). WP.  I  8,  Mühlenbach-Endzelin  I  12.
aios-  ,MetalF,  u.  zw.  wohl  , Kupfer  (,brandfarbig^ ?),  Bronze^;  im  Arischen auch  ,Eisen^.
Ai.  dyas-  n.,  av.  ayanh-  n.  ,Metall,  Eisen^;
lat.  aes,  g.  aeins]  got.  aiz  (urgerm.  '■^a(i)iz-  =  idg.  *aies-)  ^Erz,  Geld*",  ahd. er  ,Erz^,  anord.  eir  n.  ^IJrz,  Kupfer'^.
Davon  av.  ayahhaena-  ^metallen,  eisern'^,
```


## [2026-09-04T18:57:01.518Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"eignen,  vermögen\\|eignen, vermögen\\|ēik\\|eik-  ,haben\\|aik-  ,haben\" POK_01.txt | head -20"
}
```


### [2026-09-04T18:57:01.566Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:57:03.168Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"isvan\\|išvan\\|îsvan\\|ïsvan\\|aesa\\|īšti\" POK_01.txt | head -20; echo \"--- grep haben eignen\"; grep -n \"haben,  eignen\\|vermögen\" POK_01.txt | head -20"
}
```


### [2026-09-04T18:57:03.238Z] TOOL RESULT

```
1446:Gr.  q)rjy6gy  dor.  g)ay6g  f.  ,Eiche*  (vgl.  Specht  KZ.  66,  59);  lat.  fdgus  f. ,Buche*;  gall.  bägos  in  ON  J5ä^äco?i,  Bägono-]  ahd.  buohha  , Buche*  (bököh-y vgl.  Silva  Bäcenis  ,Harz*  bei  Caesar  und  mlat.  Böcönia  ,Rhön'),  aisl.  bök  f., ags.  böc,  bece  (bökjön-),  dazu  got.  böka  f.  ,Buchstabe',  aisl.  bök,  ags.  5öc, ahd.  buoh  f.  n.  ,Buch*,  ahd.  buohstap  , Buchstabe',  eigentlich  , Buchenstab zum  Einritzen*.
2717:Ai.  didestij   disdti,   deiayati  , zeigt,   weist',   av.  daes-  Aor.  döU-  ;Zeig^ {daesayeiti,    disyeiti,    daedöiU)    ,zeigen ;    jemandem    etwas    zuweisen, sprechen',  Partiz.  ai.  distd-  (=  lat.  dictus) ;  dlsti-h  ,Weisung,  Vorschrift av.   ädiHi-§  , Anweisung,   Lehre'   (=  lat.  dicti-ö,  ags.  tiht  , Anklage',  ahc in-,  bi'Ziht  ds.,  nhd.  Verzicht),  ai.  dis-  f.  , Weisung,  Richtung',  diSä  .Richtum (=r  SUt]  ,Recht',  woraus  wohl  lat.  dicis  causa  ,nur  der  Form  wegen,  zuiä Schein'),  desd-h  ,(Richtung),  Gegend'  =  an.  teigr  s.  unten;
3264:s-Erweiterung   in   ai.  dvisti  .haßt,  feindet  an',  dvistd-   .verhaßt',  dvesa-/^ ra..  dvisas-  n.  .Haß',  av.  dvae§-,  tbaeS-  .anfeinden,  kränken'.  Partiz.  thüta- dva&sah-,   tbaesah-  .Anfeindung',   mpers.  bes  .Leid.   Unheil',  wohl  zu  duis^  "** S.  232.      ^  '^    .,
4098:ai.  e-^ä,  e-§ä,  e-tdt,  av.  aesa-,  aeta-  ,der  da'  (*ei-so,  -to-,  während  arm.  aidsL *äi-to-,  s.  oben;  osk.  umbr.  eiso-,  ero-  dag-egen   aus  dem  Gen.  PL  *ei5ö„^H!
4352:!  .  über^  isvan-  .vermögend',  Isti-  ,Gut,  Reichtum'  (germ.  aihti-)^  aesä-  ,Ver- mögen;  Habe^
4360:av.  aes-  ,(sich)  in  eilige  Bewegung  setzen'  (Präs.  St.  üa-,  isya-,  aesaya-, apers.  aisaya-)^  av.  aesma-  m.  ,Zorn';
4381:etrusk.  aesar  ,Gott',  ital.  *aiso-,  *am-  ds.  sind  fern  zu  halten  und kaum  mit  gr.  legög  gleichzusetzen.
--- grep haben eignen
2131:TV-ird  gewahr^;  frabuidyamnö  ^erwachend';  ai.  boddhdr-  m.  ^Kenner'  (:  gr. ^sv(ri^rjQ--^og  ,frag-eiid');  av.  baoöah-  n.  , Wahrnehmung,  Wahrnehmungs- vermögen^, Adj.  , wahrnehmend^  (:  hom.  d-nev^rjq  ^unerforscht,  unbekannt; unkundig^);  av.  zaeni-hudra-  , eifrig  wachend^  («abg.  Hd-n,  lit.  hudriXs)] av.  haoiöi-  , Wohlgeruch'  (=  ai.  hödlii-  ^vollkommene  Erkenntnis');
3055:Gr.  dqdü}  (*dQCcicü)  , mache,  tue^  Konj.  dgöj,  äol.  3.  PL  ÖQälGi,  Aor.  att. edqaaa,  hom.  öoTjaTrjQ  , Arbeiter,  Diener',  ÖQäfia  , Handlung',  dodvog-  egyov, ngä^ig  .  .  .  övraf-ug  Hes.,  dÖQavi^g  , untätig,  unwirksam,  schwach',  hom. ��XiyodQävecjv  ,nur  wenig  zu  tun  vermögend,  ohnmächtig';  hom.  und  ion. (s.  Bechtel  Lexil.  104)  öquivo)  ,tue';
4348:eik'  ,zu  eigen  haben,  vermögen*.
4352:!  .  über^  isvan-  .vermögend',  Isti-  ,Gut,  Reichtum'  (germ.  aihti-)^  aesä-  ,Ver- mögen;  Habe^
```


## [2026-09-04T18:57:06.229Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4340,4370p' POK_01.txt; echo \"=== which leaf ===\"; awk 'BEGIN{RS=\"\\f\"} /eik.  ,zu  eigen  haben/ {print NR}' POK_01.txt"
}
```


### [2026-09-04T18:57:07.805Z] TOOL RESULT

```
vielleicht  germ.  *aibö  ^Familie,  pagus'^  in  langob.  -aib  (Änt-aib,  Burgund-  J aib),  ahd.  -eiba  (Weter-eiba,  Wingart-eiba)-^  ^.^^
slav.  *iebö  ,futuö^  in  russ,  jebü^  jeti,  skr.  jebem,  jebati  (mit  neugehildetem  "*" Infinitiv),  usw.
WP.  I  198,    Specht  KZ.  59,  121 2,    Schwyzer  Gr.  Gr.  I  722 1   (sieht  in       ; gr.  d-  ein  Präverh  e,  0,  oben  S.  280).  -i
eig-,  olg-  ,laut  jammern,  kläglich  bitten'.
Gr.  olyiTog  ,das  Bejammern,  Erbarmen',  ohrgög  ,kläglich,  erbärmlich, elendiglich',  ohTigo)  (äol.  ohTiQQw)  ,bemitleiden,  heklagen^;
dazu  Verbum  '^eigiö  in  mir.  eigid  ,schreit^,  eigem  f.  , Schrei',  ^o-Bildung in  lachtaid  , stöhnt,  schreit^;
got.  aihtrön  ,sich  erbitten,  erbetteln'  (Denominativ  eines  dem  gr.  ohtQÖg entsprechenden  Nomen  agentis  oder  eher  des  Neutrums  *oiktrom).
WP.  I  105  f.
eik'  ,zu  eigen  haben,  vermögen*.
Ai.  Uej  iste  (i  ursprüngl.  Perfektreduplikation)  ,hat  zu  eigen,  besitzt, beherrscht',  Uvard-  ,ver mögend,  imstande;  m.  Gebieter';  av.  ise  ,ist  Herr
299
»»'
!  .  über^  isvan-  .vermögend',  Isti-  ,Gut,  Reichtum'  (germ.  aihti-)^  aesä-  ,Ver- mögen;  Habe^
Hierzu  got.  ""aigan  (aih,  aigum,  sekund.  Prät.  aihta)  .haben,  besitzen', altn.  e^9^  i^y  eigom,  ätta),  ags.  ägan,  afries.  äga,  asächs.  egan,  ahd.  ei^an ^s  j  Partiz.  *aigana-,  aigina-  in  der  Bedeutung  ,eigen'  und  Substantiv,  n. ^Eigentum'  :  altn.  eiginn  ,eigen(tümlich)',  ags.  ägen  (engl,  oicn),  afries. j(/m;  ein,  asächs.  egan,  ahd.  e^aw  usw.  ds.,  got.  aigin  n.  , Eigentum',  altn. eigin,  ags.  ^^ew  usw.  ds.  Hiervon  abgeleitet  ist  *aiganön  :  anord.  eigna,  -acta ^ueignen';  ags.  ägnian  ,zu  eigen  machen,  besitzen',  weiter  ahd.  eiginen zu  eigen  machen,  aneignen'  usw.
^i-Abstr.  germ.  *aihti  :  got.  aihts  ,Eigentum',  altn.  cett,  ätt  in  der  ab- strakteren Bedeutung  ,(jeschlecht';  auch  , Himmelsgegend';  ags.  ^ht,  ahd. Sht  ,Besitz,  Eigentum^  Vgl.  weiter  altn.  eign  f.  .Eigentum  an  Grund  und Boden'  {"^aig-ni-)]
urgerm.  *aihter  ,Besitzer'  ist  aus  läpp,  äitdr  ds.  zu  erschließen  (:  ai. isitar-  ds.);
nach  Pedersen  Groupement  30  f.  hierher  toch.  B  aik-,  ais-  ,wissen'.
WP.  I  105,  Feist  20.
/.  eis-  ,(sich)  heftig,  ungestüm,  schnell  bewegen;  antreiben  =  anregen,  er- quicken; auch  vom  Entsenden,  Schleudern  von  Geschossen,  Pfeilen*; Nominalbildungen:  isoro-s  ,kräftig,  heilig',  FIN  Wort  (e)isä,  oisä usw.,  ois-mo-  , Ansturm,  Zorn*,  ois-tro-  ,Wut'.
Ai.  i§näti,  isyati  ,setzt  in  Bewegung,  schwingt,  schnellt  (spritzt  aus), treibt  an;  eilt,  drängt  vorwärts',  Bsati  , gleitet'  {esd-  ,eilend',  ha-  ,das  Hin- eilen'), isate  , enteilt'  (Adv.  Isdt  ,annähernd'),  isanat  ,er  trieb  an',  isanyäti ,treibt  an,  regt  an',  isaydti  ,ist  frisch,  rege,  kräftig;  erfrischt,  belebt',  is- f.  ,Erquickung,  Labung'  (auch  in  is-kxti-  ,Heilung'),  isird-  {'.Xaqög,  Isara) ,stark,  regsam';
av.  aes-  ,(sich)  in  eilige  Bewegung  setzen'  (Präs.  St.  üa-,  isya-,  aesaya-, apers.  aisaya-)^  av.  aesma-  m.  ,Zorn';
gr.  dor.  \(XQÖg  (:ai.  isird-),  att.  Isqoq  (f  :  er,  Schwyzer  Gr.  Gr.  I  482), lesb.  ion.  Iqog  (*isros)  ,kräftig,  rüstig';  weiter  gr.  hdcv,  iveo)  (wenn  mit i  zu  lesen,  so  daß  aus  *iav-ao),  -sca  herleitbar)  .entsende,  leere  aus;  gieße aus',  Med.  ,entleere  mich'  (vgl.  ai.  isnäti);  öla),  diofiai  {ölooaTO,  ävwiaTog^ dv-cüiaTLj  ü)LO-9-rjV,  ölg^slq)  ,meine,  komme  mit  meinen  Gedanken  worauf, verfalle  worauf,  bei  Hom.  mit  i  entweder  durch  metr.  Dehnung  aus *d-i:'[(7]-w  oder  aus  *d-t[ö"]iö,  nachhom.  oT^at  (aus  6io[.iaL)]
mit  ablaut.  oi:
olfxa  ,stürmischer  Angriff,  Andrang',  oif^dü)  .stürme  los',  beides  von Raubvösreln,   wie   ved.  esati   auch   vom   Losschießen   des   Raubvogels  auf
300
f
seiu    Nest    (gr.    Grundf.    *ol(T(.ia,    vgl.    av.    ae§ma-);    hierher    auch  ," olavQog  ;Wut   und  die  sie   durch  ihren   Stich  erregende  Bremse^,  nj verwandt   mit   lit.  aisträ   ^heftige    Leidenschaft',    aistrüs    jleidenschaftS (nicht  besser  oben  S.  12);  in  ähnlicher  Bed.  larva^ei'  ögyllsTai-^
ob  gr.  idoi-iai  ,heile';  iargög  ,Arzt'  hierher  gehören,  ist  zweifelhaft- att.  Formen    ohne   Asper    sprechen   eher   gegen   intervok.   -s-  und gegen   anlaut.  ei-;    bei   einem    Kulturwort   wäre   fremder   Ursprung verwunderlich;  Theander  (Eranos  21,  31  ff.)   geht  von  dem  heiligea Id  aus,  was  auch  die  .schwankende  Quantität  des  l  (die  Heilgötter  *ij ^Irjad)  L,  ""Idawr,  'Ii^aojv  m.  usw.,  vielleicht  auch  der  Stammesname  ^Id(Ä\ vgl.  Schwyzer  Gr.  Gr.  I  80,  als  ta-Rufer)  erklären  würde;
lalvo)  ,wärme'  hat  l  und  braucht  trotz  Schwyzer   Gr.  Gr.  I  681/ 700  nicht  dazu  zu  gehören;   s.  oben  S.  11  und  W.  Schulze  Qu.  ep.  381^ nach  Wissmann  Nomina  postverb.  203  soll  ido^at  die  lautsymbolisch' dehnte  Schwundstufe  der  Wz.  eis-  darstellen,  brauchte  also  der  Quantit differenz  wegen  nicht  von  ialvo)  getrennt  zu  werden;  \\
lat.  ira,  Plaut,  eira  (*eisa)  ,Zorn';
vielleicht  hierher   gall.   Isarno-   PN,   isarno-dori  ,ferrei  ostii*,   air. mir.  larann   n.,   cymr.    haiarn   (erfordert   t-),    acorn.    hoern,   bret.   tio"^ , Eisen'  als  das  ,starke  Metall'  im  Gegensatz  zur  weicheren  Bronze;   -l
=== which leaf ===
311
```


## [2026-09-04T18:57:34.651Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\n\" ; python3 -c \"\nimport json;d=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'));print(d['KLN']['page_offset']);print(d['KLN'].get('lookup_hint'))\nprint('---POK---');print(d['POK']['page_offset'])\nprint('---SYN---');print(d['SYN']['page_offset'],d['SYN'].get('lookup_hint'))\nprint('---HRN---');print(d['HRN'].get('lookup_hint'))\nprint('---BQT---');print(d['BQT'].get('page_offset'));print(d['BQT'].get('lookup_hint'))\nprint('---AHD---');print(d['AHD'].get('page_offset'));print(d['AHD'].get('lookup_hint'))\n\""
}
```


### [2026-09-04T18:57:36.409Z] TOOL RESULT

```
leaves 903
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
---POK---
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
---SYN---
leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
---HRN---
Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
---BQT---
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
---AHD---
1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
```


## [2026-09-04T18:57:42.258Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -A12 \"^ayes-\\|^aik-\\|^ai-k\\|^ayos\" AHD_watkins1985.txt | head -60"
}
```


### [2026-09-04T18:57:42.302Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:57:43.024Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aik-\\|ayes-\\|OWN\\.\\|ORE\\b\" AHD_watkins1985.txt | head -40"
}
```


### [2026-09-04T18:57:43.112Z] TOOL RESULT

```
<persisted-output>
Output too large (81.9KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bothz173s.txt

Preview (first 2KB):
172:The Indo-Europeans knew metal and met- allurgy, to judge from the presence of the word ayes- in Sanskrit, Germanic, and Latin. The term designated copper and perhaps bronze. Iron is a latecomer, technologically, and the terms for it vary from dialect to dialect. Latin has ferrum, while the Ger- manic and Celtic term was *isarno-, properly “holy (metal),” doubtless so called because the first iron was derived from small meteor- ites. Gold was known from ancient times, though the names for it vary; ghel-2, prob- ably “yellow (metal),” and aurum (*aus-, Latin aurum), are widespread. Silver was arg-, with various suffixes, doubtless mean- ing “white (metal).”
315:[aurum. Gold. Latin noun with preform *aus-o- probably from a root *aus-. Latin aurum (> French or), gold: AUREATE, AUREOLE, AURIC; AURIFEROUS, DORY?, EYRIR, OR’, ORE, ORIFLAMME, ORIOLE, ORMOLU, OROIDE, OR- PHREY, ORPIMENT.]
317:aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 2. Compound *awi-spek-, “observer of birds” (*spek-, to see; see spek-), in Latin auspex, augur: AuSPICE. II. Possible derivatives are the Indo-European words for egg, *dwyo-, *ayo-. 1.Germanic *ajja(m) in: a. Old English 2g, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2, Latin 6uum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek dion, egg: 00-. [Pok. auei- 86.] awo-. An adult male relative other than one’s father. 1. Latin avus, grandfather: ATAVISM. 2. Latin avunculus, maternal uncle: AVUNCULAR, UNCLE. 3. Latin avia, grandmother: AYAH. [Pok. auo-s 89.] ayer-. Day, morning. 1. Germanic “*airiz in: a. Old Eng- lish &r, before: EARLY, ERE; b. Old Norse dr, before: OR2. 2. Germanic (superlative) *airistaz in Old English rest, earliest: ERST. [Pok. ajer- 12.] ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA.
...
</persisted-output>
```


## [2026-09-04T18:57:47.224Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"ayes-\\. A metal.\\{0,400\\}\" AHD_watkins1985.txt; echo \"===\"; grep -o \"aik-\\.\\{0,400\\}\\|eik-\\.\\{0,400\\}\" AHD_watkins1985.txt | head; echo \"=== own/owe/ought ===\"; grep -o \".\\{200\\}OWE.\\{0,200\\}\" AHD_watkins1985.txt | head"
}
```


### [2026-09-04T18:57:48.933Z] TOOL RESULT

```
ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.] baba-. Root imitative of unarticulated or indistinct speech; also a child’s nursery word for a baby and for various relatives. 1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY. 3. Italian bambo, child, simpleton: BAMBINO. 4. Polish baba (diminutive babka), old woman: BABA, BABK
===
eik-
eik-
eik-
eik-.
eik-.
eik-
eik-
eik-
eik-
aik-
=== own/owe/ought ===
in folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m
English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Ge
-tu- in Latin futirus, “that is to be,” future: FUTURE. IV. Zero-grade form *bhii- (< *bhua-). 1. Germanic *biiram, dweller, especially farmer, in: a. Old English bir, “dwelling space,” bower, room: BOWER}; b. Old English gebir, dweller (ge-, collective prefix; see kom): NEIGHBOR; Cc. Middle Dutch gheboer, ghebuer, peasant: BorR, Boor. 2. Germanic *birjam, dwelling, in Old English byre, stall, hut: B
ge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek te
d form *dé-no- in Latin dénum, gift (> ddndre, to present, forgive): DONATION, DONA- TIVE, DONOR; CONDONE, PARDON. 3. Suffixed form *do-t/i)- in: a. Latin dds (genitive détis), dowry: DOT?, DOWAGER, DOWER, (DOWRY); ENDOW; b. Slavic *datja in Russian dacha, gift: DACHA; C. Russian dat’, to give, in izdat’, to publish: sAMIzDAT. 4. Reduplicated form *di-dé- in Greek didonai, to give: DOSE; ANECDOTE, AN
léd, ember: GLEED. 16. Germanic *gié- in: a. Old English gléwan, to glow: GLow; b. Norwegian dialectal glora, to gleam, stare, akin to the probable source of Middle English gloren, to gleam, stare: GLOWER; C. Old Norse glotta, to smile (scornfully), perhaps akin to the source of GLOAT. 17. Germanic *glé-m- in Old English glém, twilight: GLOAMING. 18. Possibly distantly related is Germanic *glidan, to
glish cwethan, becwethan, to say, speak: BEQUEATH, BEQUEST, QUOTH. [Pok. 2. g¥et- 480.] gvet-3. Intestine. Suffixed o-grade form *gvot-olo- in Latin botulus, intestine, sausage: BOTULINUM, BOTULISM, BOWEL; (BOTULIN). [Pok. gvet- 481.] ghedh-. To ask, pray. 1. Germanic *bidjan, to entreat, in Old English biddan, to ask, pray: BID. 2. Germanic *bidam, entreaty in Old English gebed (ge-, intensive and c
 Basic form *kar- in derivatives referring to things with hard shells. 1. Possi- bly Latin carina, keel of a ship, nutshell: CAREEN, CARINA. 2. Possibly Greek karuon, nut: KARYO-; EU- CARYOTE, GILLYFLOWER, SYNKARYON. 3. Reduplicated form *kar-kr-o dissimilated to Latin cancer, crab: CAN- CER, CANKER, CHANCRE. 4. Suffixed form *kar-k-ino- in Greek karkinos, cancer, crab: CARCINO-, CARCINOMA; (CARCINOG
akin to the Low German source of Middle English cunte, vulva: CUNT. 13. Germanic kird- in Icelandic kiird, to crouch, lie in wait, akin to the Scandinavian source of Middle English couren, to cower: COWER. 14. Possibly Old Norse kiiga, to oppress, akin to the probable source of cow?. [In Pok. géu- 393.] kus-. A kiss. Germanic *kussaz, a kiss, with denominative *kussjan in Old English cyssan, to kiss:
under, up, up from under; see upo), in Old Irish toir, pursuit: Tory. 2. Suffixed o-grade form *rot-d- in Latin rota, wheel: RODEO, ROLL, ROTA, RO- TARY, ROTATE, ROTUND, (ROTUNDA), ROULETTE, ROUND!, ROWEL; BAROUCHE, CONTROL, PRUNE?, ROTIFORM, ROTO- GRAVURE. [Pok. ret(h)- 866.] rét-. Post. O-grade form *rdt- in Germanic *réd- in Old English réd, rod, cross: ROOD. [Pok. rét+ 866.] reu-'. To bellow. 1.
```


## [2026-09-04T18:57:59.312Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"eik-\\. To be master of.\\{0,400\\}\\|aik-\\.\\{0,300\\}\\|eik-\\.\\{0,300\\}\" AHD_watkins1985.txt | head -6; echo \"=== OWN OUGHT ===\"; grep -o \".\\{0,300\\}OWN, OWE.\\{0,120\\}\\|.\\{0,300\\}OWE, OWN.\\{0,120\\}\\|.\\{0,250\\}OUGHT.\\{0,120\\}\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-04T18:58:02.799Z] TOOL RESULT

```
eik-
eik-
eik-
eik-.
eik-.
eik-
=== OWN OUGHT ===
ugrep: error: error at position 249
x80-\xbf][\x80-\xbf]*){0,120}
exceeds complexity limits___/
```


## [2026-09-04T18:58:05.799Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'eik-\\.', t):\n    print(repr(t[m.start()-60:m.start()+420])); print('---')\nprint(\"=== OUGHT ===\")\nfor m in re.finditer(r'OUGHT', t):\n    print(repr(t[m.start()-350:m.start()+120])); print('---')\nEOF"
}
```


### [2026-09-04T18:58:07.517Z] TOOL RESULT

```
'-6 in Middle English teke, tick: TIck?. [Pok. deigh- 187.] deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. I. Variant *deig-. 1. O-grade form doig- in: a. Germanic *taikjan, to show, in Old English t&can, to show, instruct: TEACH; b. Germanic *taiknam in (i) Old English tacen, tacn, sign, mark: TOKEN (ii) Old English tdcnian, to signify: BETO- KEN (iti) Gothic taikns, sign: TETCHY (iv) Old French tache, teche, mark, stai'
---
'finger (< “pointer,” “indicator”): picitT. II. Basic form *deik-. 1. O-grade form *doik- possibly in Germanic *taihw6 in Old English ta, tahe, toe: TOE. 2. Basic form *deik- in Latin dicere, to say, tell: DICTATE, DICTION, DICTUM, DITTO, DITTY; ADDICT, BENEDICTION, CONDI- TION, CONTRADICT, EDICT, FATIDIC, (INDICT), INDITE, INTERDICT, JURIDICAL, JURISDICTION, MALEDICT, PRE- DICT, VALEDICTION, VERDICT, VERIDICAL. 3. Zero-grade form *dik-d- in Latin dicdre, to proclaim: ABDICATE'
---
'tive of meiere, to urinate): MICTURATE. [Pok. meigh- 713.] meik-. To mix. 1. Variant form *meig- in Greek mig- nunai, to mix: AMPHIMIXIS, APOMIXIS, PANMICTIC, PAN- MIXIS. 2. Suffixed zero-grade form *mik-sk- in Latin miscére (past participle mixtus), to mix: MEDDLE, (MED- LEY), (MELANGE), MESTIZO, MISCELLANEOUS, MISCIBLE, MIX, MIXTURE; ADMIX, COMMIX, IMMIX, MISCEGENATION, (PELL-MELL), PROMISCUOUS. 3. Possibly a Germanic form *maisk- in Old English mdsc, macs, mdx, mashed malt'
---
"Macedonia: PIERIAN SPRING. [Pok. pei()- 793.]\npeig-'. Also peik-. To cut, mark (by incision). 1. Alter- nate form *peik- in Germanic *fihala, cutting tool, in Old English fil, file: FILE. 2. Nasalized zero-grade form *pi-n-g- in Latin pingere, to embroider, tattoo, paint, picture: PAINT, PICTOR, PICTURE, PICTURESQUE, PIG- MENT, PIMENTO, PINTO; DEPICT, PICTOGRAPH. 3. Suffixed zero-grade form *pik-ro- in Greek pikros, sharp, bitter: PICRO-. 4. O-grade form *poik- in Greek poiki"
---
", various: POIKILOTHERM. [Pok. 1. peig- 794.]\npeig-?. Also peik-. Evil-minded, hostile. 1. Suffixed zero-grade form *pig-olo- in Germanic *fikala- in Old\nEnglish ficol, treacherous, false: FICKLE. 2. Suffixed o-grade form *poik-os in Germanic *gafaihaz (*ga-, collective prefix; see kom), in Old English gefah, enemy: FOE. 3. Suffixed o-grade form *poik-yos in Germanic *faigjaz in Old English fege, fated to die: FEY. 4. Suf-\npeis-'\nfixed o-grade form *pozk-itd in Germanic *faih"
---
': PLECOPTERAN, PLECTOGNATH. [Pok. plek- 834.] plék-. Also pleik-. To tear. 1. Zero-grade form *pbk- becoming *plak- in Germanic *flahan in Old English fléan, to strip the skin from: FLAY. 2. Suffixed o-grade form “ploik-sk- perhaps in Germanic “flaiskjan, piece of flesh torn off, in Old English flésc, flesh: FLESH. 3. Zero-grade form *plik- in Germanic *flikkja in: a. Old English flicce, side of a hog: FLITCH; b. Germanic ablaut form *flekkja in Old Norse flekkr, piece of ski'
---
'-os- 857.] rei-1, To scratch, tear, cut. I. Extended form ‘reik-. 1. Germanic *rigon- in Italian riga, line (< “something cut out’’): RIGATONI. 2. Suffixed form *rei-md or *reig-sma in Latin rima, crack, cleft, fissure: RIMOSE. 3. Suffixed o-grade form *roik-wo- in Germanic *rai(h)-wa- in Old English raw, réw, a line, row: ROW!. II. Possible extended form *reipp-. Germanic *raipaz, rope, in: a. Old English rap, rope: ROPE; b. compound *stig-raipaz, “‘mount-rope,” in Old Engli'
---
'd English spdca, spoke: SPOKE}. [Pok. 1. sp(hjéi- 981.] (s)peik-. Bird’s name, woodpecker, magpie. 1. Suffixed form *peik-o- in Latin picus, woodpecker: PICARO, (PICKET), (PIKE!), (PIQUE). 2. Suffixed form *peik-d- in Latin pica, magpie: PICA2, PIE2. [Pok. (s)piko- 999.] spek-. To observe. I. Basic form *spek-. 1. Germanic *spehon in: a. Old French espier, to watch: ESPY, SPY; b. Germanic derivative *speh-6n-, watcher, in Old Italian spione, spy: ESPIONAGE. 2. Suffixed form *'
---
'” series, in Old English wicu, wice, week: WEEK. II. Form *weik-. Zero-grade form *wik- in: a. Latin vix (genitive vicis), turn, situ- ation, change: VICAR, (VICARIOUS), VICE; VICISSITUDE; b. Latin vicia, vetch (< “twining plant”): veTCH. [Pok. 4. ueik- 1130.] weik-5, To fight, conquer. 1. Germanic “wik- in Old Norse vigr, able in battle: WIGHT2. 2. Nasalized zero-grade form *wi-n-k- in Latin vincere (past participle victus), to conquer: VANQUISH, VICTOR, VINCIBLE; CONVINCE, '
---
'her” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wlik-u-, wet, in: a. suffixed form *wlik-w-d- in Latin liquare, to dissolve: LIQUATE; b. suffixed form *wlik-w-é- in Latin liquére, to be liquid: LIQUESCENT, LIQUID, LIQUOR; DELIQUESCE, LIQUEFY. 2. Suffixed form *wlik-s- in: a. Latin lixa, lye: LIXIVIATE; b. Latin prélixus, poured forth, stretched out in front, extended (pro-, forth; see per’): PROLIX. [In Pok'
---
=== OUGHT ===
'peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEU'
---
'223.] [dorsum. The back. Latin noun of unknown origin. DORSAL, DORSO-, DORSUM, DOSS, (DOSSAL), DOSSER, DOS- SIER; ENDORSE, INTRADOS, REREDOS.]\ndrem-. To sleep. Suffixed zero-grade form “drm-yo- in Latin dormire, to sleep: DORMANT, DORMER, DORMITORY. [Pok. dré- 226.]\n[dreug-. Dry. Germanic root. 1. Old English driigoth, drigath, dryness, drought: DROUGHT. 2. Suffixed form *drig-iz in Old English dryge, dry: DRY. 3. Suffixed variant form *draug-n- in Old English dréah'
---
'OR, JANUARY, JANUS; b. San- skrit ydnam, way (in Buddhism, “mode of knowledge,” “vehicle”): HiINAYANA, MAHAYANA. [Pok. 1. ei- 293.]\nei-2. Reddish, motley; yew. Suffixed form *ei-wo- in Germanic *iwaz, yew, in Old English iw, yew: yew. [Pok. 3. ei- 297.]\n6ik-. To be master of, possess. 1.Germanic “aigan, to possess, in Old English dgan, to possess: OUGHT!, OWE. 2. Germanic participial form *aiganaz, possessed, owned, in Old English agen, one’s own: own. 3. Germanic p'
---
'TION, GRANDILOQUENCE, INTERLOCUTION, MAGNIL- OQUENT, OBLOQUY, PROLOCUTOR, SOLILOQUY, VENTRILOQUISM. [Pok. tolk¥- 1088.] tong-. To think, feel. 1. Germanic *thank6n in: a. Old English thancian, to thank: THANK; b. Old English thencan, to think: THINK. 2. Germanic *(ga)thauht- (*ga-, collective prefix; see kom) in Old English (ge)- thoht, thought: THOUGHT. 3. Germanic factitive *thunk- Jan in Old English thyncan (third person singular present indicative thyncth), to s'
---
'- URGE, DRAMATURGE, ENDERGONIC, ENDOERGIC, EN- ERGY, ERGOGRAPH, EXERGONIC, EXERGUE, EXOERGIC, GEORGIC, LITURGY, METALLURGY, SURGERY, (SYNERGID), SYNERGISM, THAUMATURGE. II. Zero-grade form *wrg-. 1. Suffixed forms *wrg-yo-, *wrg-to- in Germanic *wurk- Jan, to work, participle *wurhta-, in Old English wyrcan, to work, participle geworht, wrought: WROUGHT. 2. Suf- fixed form *wrg-t- in Germanic *wurhtj6- in Old English wryhta, maker, wright: WRIGHT. III. O-grade form '
---
'deme-1 DONATION d6- DONATIVE d6- DONOR do- poom dhé-1 pooR dhwer- DOPE dub- DORMANT drem- DORMER drem- DORMITORY drem- DORSAL dorsum poRrsO- dorsum pory? aurum DOSE dé-\nposs dorsum DOSSAL dorsum DOSSER dorsum DOSSIER dorsum por? dé-\nDOTE dud- DOUBLE dwo- DOUBLET dwo- DOUBLOON dwo- DOUBLURE dwo- DOUBT dwo- DOUCEUR dik-u- DOUCHE deuk- poucH dheigh- DOUGHTY dheugh- DOUR deru. DOVE! dheu-1 DOWAGER dé- DOWEL dheubh- DOWER do- Down! dhino- pDowN2 dheu-! pown’ dhiino- Dowr'
---
' DRASTIC dere- DRAW dhragh- DRAY dhragh- DREAM dhreugh- DREARY dhreu- DRECK sker-4 DREGS dher-1 DRENCH dhreg- DRIFT dhreibh- DRILL! tere-1 DRINK dhreg- DRIP dhreu- DRIVE dhreibh- DRIVEL dher-! DRIZZLE dhreu- -DROME der-1 DROMEDARY der-1 DROMOND der-1 -DROMOUS der-1\nDRONE! dher-3 DRooP dhreu- DROP dhreu- DROPsY wed-1 DROSHKY dhragh- DRoss_ dher-1 DROUGHT dreug- DROVE? dhrelbh- DROWN dhreg- DROWSE dhreu- DRUID deru DRUPE deru, pekw- DRY dreug- DRYAD deru DUAD dwo- DUA'
---
'mosis wedh- OSPREY awi-, ghend- OsSEOUS ost- OSSICLE ost- OSSIFRAGE bhreg-, ost- OSSIFY ost- OSSUARY ost- OSTENSIBLE ten- OSTEO- ost- OSTEOCLAST kel-1 OSTEOMALACIA mel-1 OSTIARY Os- OSTIUM 6s- OSTMARK aus-! OSTRACIZE ost- OSTRACOD ost-\nPALUDAL\nOSTRICH awi-, trozdo- OsTROGOTH aus-! OTHER an?\nOTIC ous-\nOTO- ous-\nOTTER wed-1 OUBLIETTE lei- oucH2 ned: OUGHT! 6 OUNCE! oi-no- OUNCE? leuk-\nOUR nes-2\nOURS nes-2\noust sta-\nouT ud-\nOUTLAW legh-, ud- OUTRE al-!\nOUZEL ames-\nOVAL'
---
'egu-\nTHIGH teue- THIGMOTAXIS dheigh- THIMBLE teue- THIN ten-\nTHINE tu-\nTHING §tenk-1 THINK tong-\nTHIO- dheu-t THION- dheu-1 THIRD trel-\nTHIRST ters- THIRTEEN trei- THIRTY trel-\nTHIS to-\nTHITHER to- THIXOTROPY dheigh- THOLE tele-\nTHOLE PIN teue- THONG twengh- THOR (s)tene- THORN (s)ter-n- THOROUGH tere-2 THORP treb- THOSE to-\nTHOU! tu-\nTHOUGH to- THOUGHT tong- THOUSAND teue-\nTHRUST treud- THUG (s)teg- THUJA dheu-! THUMB teue- THUNDER (s)tene- THURIBLE dheu-! THURIFER'
---
```


## [2026-09-04T18:58:12.262Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find('ik-. To be master of')\nprint(t[i-10:i+600])\nEOF"
}
```


### [2026-09-04T18:58:14.223Z] TOOL RESULT

```
i- 297.]
6ik-. To be master of, possess. 1.Germanic “aigan, to possess, in Old English dgan, to possess: OUGHT!, OWE. 2. Germanic participial form *aiganaz, possessed, owned, in Old English agen, one’s own: own. 3. Germanic prefixed form *fra-aihtiz, absolute possession, property (*fra-, intensive prefix; see per'), in Middle Low German and Middle Dutch vrecht, vracht, “earnings,” hire for a ship, freight: FRAUGHT, FREIGHT. [Pok. éik- 289.]
eis-1. In words denoting passion. 1. Suffixed form “eis-d- in Latin ira, anger: IRASCIBLE, IRATE, IRE. 2. Suffixed zero-grade form “is-(a)ro-, powerful, holy, in Gre
```


## [2026-09-04T18:58:20.280Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^own, adj\\|^own, tr\\|^owe, tr\\|^ought,\\|^ore, n\" KLN_1966.txt | head -20; echo \"=== leaves ===\"; awk 'BEGIN{RS=\"\\f\"} /^own, adj|^ore, n/ {print NR\": \"substr($0,1,80)}' KLN_1966.txt"
}
```


### [2026-09-04T18:58:22.386Z] TOOL RESULT

```
26753:ought,  aux.  v.,  expressing  duty  or  obligation.  — ME.  aughten,  oughten,  fr.  aughte,  oughte,  ‘own¬ ed,  possessed’,  fr.  OE,  dhte,  of  s.m.,  past  tense of  agan,  ‘to  own,  possess’;  hence  prop,  past tense  of  owe  (q.v.)
26754:ought,  n.  —  An  obsol.  var.  of  aught.
=== leaves ===
```


## [2026-09-04T18:58:24.772Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^own,\\|^owe,\\|^ore,\\|^ora,\\|^oread\" KLN_1966.txt | head -20; echo \"=== ctx around ought line ===\"; sed -n '26740,26775p' KLN_1966.txt"
}
```


### [2026-09-04T18:58:24.847Z] TOOL RESULT

```
26472:ore,  n.,  the  grampus.  —  L.  orca,  ‘a  kind  of  w  hale’, fr.  Gk.  opuya,  acc.  of  opui;,  ‘a  kind  of  whale’;  c for  g  in  L.  orca  is  due  either  to  contamination with  L.  orca  in  the  sense  of  ‘butt,  tun’  (see  ur- ceolate),  or  to  Etruscan  influence.  For  the  deri¬ vation  of  the  Latin  word  from  a  Greek  accusa¬ tive  cp.  Numidia  and  words  there  referred  to. Cp.  next  word  and  Orcinus. orca,  n.,  1)  a  killer  whale;  2)  (cap.)  the  genus consisting  of  the  killer  whale  (zool.)  —  L.,  *a kind  of  whale’.  See  prec.  word.
26525:ore,  n.  — -  ME.  oor,  or,  fr.  OE.  dr,  Sr,  ‘brass’,  rel. to  ON.  eir,  ‘brass,  copper’,  OHG.  er,  ‘brass’, OHG.,  MHG.  erin,  G.  ehern,  ‘brazen’,  Goth. aiz,  ‘bronze’,  and  cogn.  with  OI.  ayah  (gen. dyasah),  Avestic  ayo  (gen.  ayanhd),  L.  aes,  gen.
26527:ore,  n.,  a  Dan.  and  Norw.,  resp.  Swed.  coin, equal  in  value  to  1/100  of  a  krone,  resp.  krona.
26529:oread,  n.,  a  mountain  nymph  ( Greek  mythol.)  — L.  Oreas,  gen.  -adis,  fr.  Gk.  ’Opsta;,  gen.  -<x.8oq, fr.  opo c,  ‘mountain’.  See  oro-,  ‘mountain-’,  and
26826:owe,  tr.  and  intr.  v.  —  ME.  owen,  awen,  fr.  OE. agan,  ‘to  possess,  have,  own,  owe’,  rel.  to  OFris. aga,  ON.  eiga,  Swed.  aga,  OHG.  eigan,  Goth. aigan,  ‘to  possess,  have’,  fr.  I.-E.  base  *aik-,  ‘to own’,  whence  also  OI.  tie,  ‘he  owns’,  tidh , ‘owner,  lord,  ruler’,  tivardfi,  ‘owner,  ruler,  lord, king’,  Avestic  is-,  ‘riches,  fortune’,  isvan-,  ‘well off,  rich’.  Cp.  ought,  aux.  v.,  own,  adj.  and  v., fraught,  freight.  Cp.  also  Ishvara.
26830:own,  adj.  —  ME.  owen,  awen,  fr.  OE.  agen, ‘own’,  lit.  ‘possessed  by’,  prop.  pp.  of  agan,  ‘to possess,  have’;  rel.  to  OS.  egan,  ‘own’,  OFris. egin,  ON.  eiginn,  Dan.,  Swed.  egen,  Du.  eigen, OHG.  eigan,  MHG.,  G.  eigen,  ‘own’,  of  s.m., which  all  are  orig.  pp.s.  and  arc  rel.  to  Goth. aigan,  ‘to  possess,  have’,  dih,  ‘I  possess,  have’. See  owe  and  cp.  own,  v.
26831:own,  tr.  and  intr.  v.  —  ME.  ohnien,  ahnien,  fr.  OE. dgnian,  ‘to  possess,  take  possession  of’,  fr.  agen, ‘own’  (adj.);  rel.  to  ON.  eigna,  ‘to  own’,  Dan. egne,  OHG.  eiginen,  G.  eignen,  of  s.m.  See  own, adj.
=== ctx around ought line ===
Otiorhynchidae,  n.  pi.,  a  family  of  weevils  (ento- mol.)  —  ModL.,  formed  with  suff,  -idae  fr.  Gk. coxiov,  dimin.  of  on?,  gen.  coxo?,  ‘ear’,  and puy/or,  ‘snout,  beak’.  Seeoto-  and  rhyncho-  and cp.  words  there  referred  to. otiose,  adj.,  1)  at  leisure  (archaic);  2)  useless, futile.  —  L.  otiosus,  ‘at  leisure,  at  ease,  idle’,  fr. otium,  ‘leisure,  idleness’,  which  is  of  uncertain origin.  Cp.  negotiate.  For  the  ending  see  suff. -ose.
Derivatives:  otiose-ly,  adv.,  otiose-ness,  n. otiosity,  n.  —  MF.  ociosite,  fr.  Late  L.  otio-
l
sitatem,  acc.  of  otiositas,  fr.  L.  otiosus.  See prec.  word  and  -ity.
Otis,  n.,  a  genus  of  bustards  ( ornithol .)  —  L.  Otis,
‘a  kind  of  bustard’,  fr.  Gk.  cbxl?,  lit.  ‘long¬ eared  bird’,  fr.  oOp,  gen.  tixop,  ‘ear’.  See  oto- and  cp.  the  second  element  in  Haliotis,  Myo- sotis.
otitis,  n.,  inflammation  of  the  ear  (med.)  —  Med¬ ical  L.  otitis,  formed  with  suff.  -itis  fr.  Gk.  o5p, gen.  &Ttbq,  ‘ear’.  See  oto-. oto-,  before  a  vowel  ot-,  combining  form  denoting the  ear  (med.)  —  Gk.  (3xo  ,  ox-,  fr.  o5?,  gen. toxo?  (for  *o-jcjo?,  gen.  *oi3cxxo? ),  ‘ear’,  which is  cogn.  with  L.  auris  (for  *ausis),  ‘ear’,  Goth. auso,  OE.  eare,  ‘ear’.  See  ear,  ‘the  organ  of hearing’,  and  cp.  words  there  referred  to.  Cp. also  otic,  Otis,  Aotus,  diota,  lago-,  microtia, parotic,  parotid,  Plecotus. otocyst,  n.,  the  auditory  organ  of  Mollusca  and Vermes  (zool.)  —  Lit.  ‘otic  cavity’;  coined  by the  French  naturalist  Felix-Henri  de  Lacaze- Duthiers  (1821-1901)  fr.  Gk.  o5?,  gen.  <oxo?, ‘ear’,  and  xonxic,  ‘bladder,  bag,  pouch’.  See oto-  and  cyst.
otolith,  n.,  chalky  matter  in  the  internal  ear  of animals  (zool.)  —  Lit.  ‘ear  stone’ ;  coined  by  the French  anatomist  and  surgeon  Gilbert  Breschet (1784-1843)  in  1836  fr.  Gk.  o5?,  gen.  coxo?,  ‘ear’, and  Xiffo?,  ‘stone’.  See  oto-  and  -lith. otology,  n.,  that  branch  of  medicine  which  deals with  the  ear  and  its  diseases.  —  Compounded  of oto-  and  Gk.  -Xoyla,  fr.  -Xo-yo;,  ‘one  who speaks  (in  a  certain  manner);  one  who  deals (with  a  certain  topic)’.  See  -logy.
Derivatives:  otolog-ic-al,  adj.,  otolog-ist,  n. otoscope,  n.,  an  instrument  for  examining  the  ear. —  Compounded  of  oto-  and  Gk.  -axomov,  fr. oxottciv,  ‘to  look  at,  examine’.  See  -scope, ottava  rima,  a  stanza  of  eight  lines,  with  the  rhyme scheme  abababcc  (pros.)  —  It.,  lit.  ‘octave rhyme’.  See  octave  and  rhyme, otter,  n.,  an  aquatic  carnivorous  mammal.  — ME.  oter,  fr.  OE.  otor,  oter,  rel.  to  ON.  otr, Swed.  utter,  Dan.  odder,  MLG.,  MDu.,  Du. otter,  OHG.  ottar,  MHG.  oter,  otter,  G.  Otter, and  cogn.  with  OI.  udrah,  Avestic  udra,  ‘otter’, Gk.  uSp  5c,  68poc.  ‘water-serpent’,  £vu8pi?,  ‘otter’, L.  lutra  (for  * utra ,  ‘udra,  influenced  in  form  by iutum,  ‘mud,  mire’),  OSlav.  vydra,  Lith.  udra, Lett,  udris,  OPruss.  udro,  ‘otter’,  OIr.  odar, ‘dark -colored,  brown’,  lit.  ‘otter-colored’,  odoir- ne,  ‘otter’,  and  prob.  also  with  Gk.  iiXXo;  (for •flSXo?),  ‘water  snake,  ichneumon’  (with  change of  p  to  X).  All  these  words  derive  fr.  I.-E.  *udr-, ‘water’,  and  lit.  denote  an  aquatic  animal.  I.-E. *udr-  is  an  enlargement  of  base  *ud-,  ‘water’.  See water  and  cp.  hydra,  Lutra,  nutria, otto  cycle,  1)  a  four-stroke  cycle  in  internal- combustion  engines ;  2)  a  kind  of  velocipede.  — Named  after  its  inventor  August  Nikolaus  Otto (1839-91).
Ottoman,  adj.,  Turkish;  n.,  a  Turk.  —  F.  otto¬
man,  fr.  it.  Ottomano,  fr.  ML.  Ottomanus,  fr, Arab.  ‘Uthmdnt,  ‘pertaining  to  ‘ Uthmari ,  fr.
‘  Uthman ,  ‘Osman’,  name  of  the  founder  of  the Ottoman  empire.  Cp.  Osmanli. ottoman,  n.,  a  kind  of  sofa  or  divan.  —  F.  otto- mane,  prop.  fern,  of  ottoman,  ‘Ottoman’,  hence lit.  ‘Ottoman  piece  of  furniture’  (see  prec.  word) ; so  called  because  one  can  rest  on  it  according  to the  Oriental  fashion.
oubliette,  n.,  a  secret  dungeon,  reached  only through  a  trapdoor  from  above.  —  F.,  fr.  MF., fr.  oublier,  ‘to  forget’,  fr.  OF.  oblider,  fr.  VL. ‘oblitdre,  fr.  L.  oblitus,  pp.  of  oblivisci,  ‘to forget’.  See  oblivion  and  -ette. ouch,  also  nouch,  n.,  a  brooch  or  clasp  (archaic). —  ME.  nouche,  fr.  OF.  nosche,  noche,  nouche, ‘jewel,  necklace’,  fr.  ML.  nusca,  fr.  OHG.  nusca, a  word  of  Celtic  origin  (cp.  OIr.  nasc,  ‘a  tie, chain’,  Bret,  nask,  ‘a  rope  to  tie  animals’),  fr, I.-E.  base  ‘ned-,  ‘to  knot,  twist’.  See  net  and  cp. words  there  referred  to.  The  loss  of  the  initial n-  in  ouch  is  due  to  a  misdivision  of  a  nouch  into an  ouch.  For  similar  misdivisions  cp.  adder  and words  there  referred  to.
ought,  aux.  v.,  expressing  duty  or  obligation.  — ME.  aughten,  oughten,  fr.  aughte,  oughte,  ‘own¬ ed,  possessed’,  fr.  OE,  dhte,  of  s.m.,  past  tense of  agan,  ‘to  own,  possess’;  hence  prop,  past tense  of  owe  (q.v.)
ought,  n.  —  An  obsol.  var.  of  aught.
Ouija,  n.,  a  trademark.  —  Coined  fr.  F.  out,. ‘yes’,  and  G.  ja,  ‘yes’.
ounce,  n.,  a  unit  of  weight,  the  twelfth  part  of  a pound  in  troy  and  apothecaries  weight.  —  ME. unce,  ounce,  fr.  OF.  unce  (F.  once),  fr.  L.  itncia, ‘the  twelfth  part  (of  anything) ;  the  twelfth  part of  a  pound,  an  ounce;  the  twelfth  part  of  a  foot, an  inch’.  See  uncia  and  cp.  inch,  which  is  a doublet  of  ounce.  Cp.  also  the  second  element  in quincunx.
ounce,  n.,  snow-leopard,  lynx.  —  ME.  unce,  once, fr.  OF.  (=  F.)  once,  fr.  lonce,  misread  as  I'once, the  initial  /  having  been  taken  for  the  definite article  and  consequently  dropped.  Lonce  goes back  to  VL.  ‘luncia,  from  L.  lyncea,  ‘the  lynx¬ like  animal’,  fern,  of  lynceus,  ‘lynx-like’,  used  as a  noun,  fr.  lynx,  gen.  lyncis,  ‘lynx’.  See  lynx, ouphe,  n.,  an  elf,  sprite.  —  A  var.  of  oaf. our,  pron.  —  ME.  ure,  oure,  fr.  OE.  ure,  ‘of  us, our,  fr.  earlier  user,  gen.  of  us;  ‘us’;  rel.  to  OS. usa,  user,  OFris.  use,  user,  OHG.  unsar,  unser, MHG.,  G.  unser,  Goth,  unsar,  ‘our’.  See  us  and cp.  nostrum.
ourali,  n.  —  A  var.  of  curare, ours,  pron.  —  ME.  ures,  formed  fr.  ure,  ‘our’  (see prec.  word)  with  gen.  suff.  -s.
-ous,  suff.  used  to  form  adjectives  meaning ‘having,  full  of,  abounding  in’ ;  in  chemistry  this suff.  means  ‘having  a  lower  valence  than  is  ex¬ pressed  by  suff.  -ic.  — •  ME.,  fr.  OF.  -ous-,  -eus (F.  -eux),  fr.  L.  -dsus.  See  adj.  suff.  -ose.  In  many cases  E.  -ous  is  equivalent  to  Gk.  -o?  or  L.  -us-
ousel
ovitorm
Cp.  e.g.  arduous ,  fr.  L.  arduus,  E.  pious,  fr.  L. pius,  etc.
ousel,  n.  —  See  ouzel.
oust,  tr.  v.,  to  drive  out,  expel,  eject.  —  AF.  ous¬ ter,  fr.  OF.  oster  (F.  6 ter),  ‘to  take  away’,  fr.  L. obstdre,  ‘to  stand  against,  oppose,  obstruct’,  in VL.  used  also  in  the  sense  ‘to  hinder',  formed fr.  ob,  ‘against’  (see  ob-),  and  stare,  ‘to  stand’. See  stand,  v.,  and  cp.  obstacle.
Derivative:  oust-er,  n.
ouster,  n.,  ejection  from  property,  dispossession (law).  —  AF.  inf.  used  as  noun,  fr.  OF.  oster,  ‘to take  away’.  See  prec.  word.  For  the  subst.  use  of the  infinitive  cp.  attainder  and  words  there  re¬ ferred  to.
out,  adv.  —  ME.  out,  oute,  fr.  OE.  ut,  ute,  rel.  to OS.,  ON.,  OFris.,  Goth,  ut,  Swed.  ut,  Dan.  ud, MDu.  uut,  Du.  uit,  OHG.,  MHG.  mj,  G.  aus,  fr. I.-E.  *ud,  ‘up,  out,  away’,  whence  also  01.  ut, ‘up,  out’,  uttarah,  ‘the  higher,  upper,  latter, later,  northern’,  Avestic  us-,  uz-  (for  *ud-z),  ‘up, out’,  OIr.  pref.  ud-,  od-,  ‘out-’,  L.  usque  (for *us-que),  ‘all  the  way  to,  from  ...  to,  without interruption’,  Gk.  uaxEpo c  (for  *ud-tero-s),  ‘the latter’.  Cp.  about,  but,  uitlander,  utmost,  utter, adj.  and  v.,  and  the  second  element  in  carouse. Cp.  also  hysteron  proteron.  Cp.  also  hubris. Derivatives:  out,  adj.,  n.,  tr.  v.,  and  interj. outcast,  adj.  and  n.  —  ME.,  fr.  pp.  of  out- casten,  fr.  out,  ‘out’,  and  casten,  ‘to  cast’.  See out  and  cast.
outcaste,  n.,  in  India,  a  person  expelled  from  his caste.  —  Formed  fr.  out-  and  caste, outcome,  n.,  result.  —  Scot.,  formed  fr.  out  and come;  introduced  into  English  by  Carlyle, outlander,  n.,  foreigner,  used  esp.  in  the  sense  of ‘not  of  Boer  birth’.  —  Formed  in  imitation  of  S. African  Du.  uitlander,  ‘person  from  a  foreign land’;  see  out,  land  and  agential  suff.  -er  and  cp. uitlander.
outlandish,  adj.,  1)  foreign;  2)  strange.  —  ME. utlandisch,  fr.  OE.  utlendisc,  ‘foreign’.  See  out, land  and  adj.  suff.  -ish.
outlaw,  n.  —  ME.  ullage,  fr.  OE.  utlaga,  fr.  ON. Magi,  ‘an  outlaw’,  lit.  ‘(one  placed)  outside  of the  law’.  See  out  and  law.
Derivatives:  outlaw,  tr.  v.,  outlaw-ry,  n. outline,  n.  —  Coined  by  the  English  diarist  John Evelyn  (1620-1706)  fr.  out  and  line.
Derivatives:  outline,  tr.  v.,  outlin-ed,  adj., outlin-er,  n.
outrage,  n.,  a  violent  injury;  any  serious  violation of  the  law.  — •  ME.,  fr.  OF.  oltrage,  oultrage, outrage,  fr.  VL.  *ultraticum,  fr.  L.  ultra,  ‘be¬ yond’.  See  ulterior  and  -age  and  cp.  outre. Derivative:  outrage,  tr.  v. outrageous,  adj.,  violent,  excessive;  very  offen¬ sive.  —  ME.,  fr.  OF.  oultrageus,  outrageus  (F. outrageux ),  fr.  oultrage,  outrage.  See  prec.  word and  -ous.
Derivatives:  outrageous-ly,  adv.,  outrageous¬ ness,  n.
1104  1105
```


## [2026-09-04T18:58:31.140Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,L in enumerate(leaves):\n    if '\\nore,  n.  — -  ME.  oor' in L or 'ore,  n.  — -  ME.' in L:\n        print('leaf',i); print(L[-300:]); print('=== ore entry ===')\n        j=L.find('ore,  n.  — -')\n        print(L[j:j+700])\n        break\nfor i,L in enumerate(leaves):\n    if '\\nowe,  tr.  and  intr.  v.' in L:\n        print('OWE leaf',i); print(L[-200:])\n        break\nEOF"
}
```


### [2026-09-04T18:58:32.998Z] TOOL RESULT

```
leaf 584
.  aes. For  sense  development  cp.  L.  cuprum,  ‘copper’, fr.  Kiitrpo;,  ancient  name  of  Cyprus  (see  cop¬ per).
ore,  n.,  a  Dan.  and  Norw.,  resp.  Swed.  coin, equal  in  value  to  1/100  of  a  krone,  resp.  krona.
—  Dan.  and  Norw.  ere  or  Swed.  ore,  fr.  L. aureus,  a  gold 
=== ore entry ===
ore,  n.  — -  ME.  oor,  or,  fr.  OE.  dr,  Sr,  ‘brass’,  rel. to  ON.  eir,  ‘brass,  copper’,  OHG.  er,  ‘brass’, OHG.,  MHG.  erin,  G.  ehern,  ‘brazen’,  Goth. aiz,  ‘bronze’,  and  cogn.  with  OI.  ayah  (gen. dyasah),  Avestic  ayo  (gen.  ayanhd),  L.  aes,  gen.
aeris,  ‘brass’,  fr.  I.-E.  *uyos-,  which  is  perh.  a derivative  of  Ayashya,  later  form  of  Alashya, ancient  name  of  Cyprus,  hence  I.-E.  *ayos would  have  meant  orig.  ‘the  Cyprian  metal’. Cp.  aeneous,  aes,  aerarian,  aerugineous,  era,  es¬ teem;  see  Walde-Hofmann,  LEW.,  1, 19  s.v.  aes. For  sense  development  cp.  L.  cuprum,  ‘copper’, fr.  Kiitrpo;,  ancient  name  of  Cyprus  (see  cop
OWE leaf 591
ich  is  rel.  to oxpt;,  ‘peak,  point’,  Homeric  oxptav,  ‘to  make rough  or  rugged’,  dxptxaffxt,  ‘to  be  exasperated’, cogn.  with  L.  ocris,  ‘a  rugged,  stony  mountain’, medi-ocris,  ‘mi
```


## [2026-09-04T18:58:40.677Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(580,594):\n    tail=leaves[i][-120:].replace('\\n',' ')\n    m=re.findall(r'\\b1[01]\\d\\d\\b',leaves[i])\n    print(i, m[-4:] if m else None, '|', tail[-60:])\nEOF"
}
```


### [2026-09-04T18:58:42.606Z] TOOL RESULT

```
580 ['1084', '1085'] | ‘a  sowing, seed'.  See  spore. ootbeca,  n.,  a  case  cont
581 ['1086'] | ontaining  opium;  narcotic;  n.,  a drug  containing  opium
582 ['1088', '1089'] | cian,  n.,  one  who  makes  or  sells  optical  in¬ strumen
583 None | atorio,  ‘oratorical  art’,  fern,  of  drdtdrius, ‘pertaini
584 ['1093'] |  and  Norw.  ere  or  Swed.  ore,  fr.  L. aureus,  a  gold 
585 ['1094', '1095'] |   any  bird  of  the  family  Oriolidae;  2) any  of  variou
586 ['1096'] | ,  n.,  the  Florentine  iris.  —  Prob.  fr.  ML. yreos,  �
587 None |   Gk.  ooyeov, ‘scrotum’.  See  oscheo-. oscheo-,  before  a
588 None | st.  suff.  -ary. ost-,  oste-,  forms  of  osteo-  before  
589 ['1103'] | ?,  gen.  <oxo?, ‘ear’,  and  xonxic,  ‘bladder,  bag,  pouc
590 ['1104', '1105'] | o  cry  £ua  (in  honor  of  Bacchus)’, oven,  n.  —  ME.,  
591 ['1106', '1107'] |  L.  ocris,  ‘a  rugged,  stony  mountain’, medi-ocris,  ‘mi
592 ['1108'] | the  mod¬ em  sense  of  stamen.  See  andro-. Pachystima,  
593 None | , adj.,  pageant-eer,  n.,  pageant-ic,  adj.,  pageant- ry,
```


## [2026-09-04T18:58:47.874Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==636' SYN.txt | head -50"
}
```


## [2026-09-04T18:58:48.640Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=795 && NR<=797' SYN.txt | head -80"
}
```


### [2026-09-04T18:58:49.910Z] TOOL RESULT

```
y rubbing’, epd. of teret’ ‘rub’ (9.31).
9. Skt..nzj-, Av. niz-, above, 1.
Skt. dhdav-, prob. as ‘cleanse, make shine’; dhavala- ‘shining white’, Av.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
580 SELECTED INDO-EUROPEAN SYNONYMS
fra-dav- ‘tub off’, Grk. Oods'... . Aap- mpos, Oodca....Aaumpivac Hesych., etc., 6é ‘shine’ (Hes., Theoc., etc.). Walde-P. 1.835.
Av. sna-, esp. cpd. fra-snd- (quotable
with reference to body, hands, and clothes) : Skt. sna- ‘bathe, Perform t) rite of bathing’, Gri. vixe, Lat 9°
at. ng ‘swim’, etc. Walde-P. 2.692 f. Bae 1628. |
9.37 SWEEP Grk. —_xopiw, calpw Goth. usbaugjan Lith. Sluoiz NG —capdivw, oxouriti ON sopa Lett. mézt (slaucit) Lat. —_verrere Dan. feje ChSl.  pomesti It. Spazzare, scopare Sw. sopa SCr. mes; Fr. balayer OE swapan Boh. mésti Sp. _barrer ME _ swepe, swope Pol. - . zaméatad Rum. mdétura NE sweep Russ. mesti Ir. scOpaim Du. vegen Skt. mrj- NIr.  scuabaim OHG kerren Av. maraz- W. —-ysgubo MHG keren
Br. skuba
Several of the words for ‘sweep’ are derived from those for ‘broom’, one from the word for ‘floor’. In most of the others, so far as there are clear cognates, ‘sweep’ is a specialization of either ‘cleanse, adorn’ or various motions like ‘turn, throw’, etc., applicable to the re- moval of dirt.
1. Grk. xopé (whence xdpnua ‘sweep- ings’ and ‘broom’; cf. also képos*.... Ka\huyrpor, Hesych., vao-xbpos ‘care- taker of a temple’, etc.), etym. dub. Walde-P. 1.462, Boisacq 495 f.
Grk. caipw (cf. cdpyara ‘sweepings’, etc.), later capsw (whence Byz. cdpwrpov, NG 74pwpov‘broom’), NG Tapwve, perh. : atpw ‘drag’, cupderss ‘sweepings’, but root connection dub. Walde-P. 2.530. Boisacq 849,
NG oxovritw, deriv, of cxodra ‘broom’ (9.38).
2. Lat. verrere (> Sp., Port. barrer) : ChSl. vriicha, vréiti ‘thresh’ (fr. ‘drag’, ef. 8.34), perh. Grk, €ppw ‘walk with difficulty, go to destruction, perish’, dial. réppw ‘be exiled’, Walde-P. 1.292.
Ernout-M. 1091.
It. spazzare, fr. Olt. spazzo ‘floor’ (Lat. spatium ‘space’). REW 8121,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
NHG fegen, kehren
It. scopare, fr. late Lat. ScOpare, deriv, of scépa ‘broom’ (9.38). REW 7735,
Fr. balayer, fr. balai ‘broom’ (9.38).
Rum. mdétura, fr. mdturé ‘broom’ (9.38).
3. Ir. scdpaim, NIr. scuabaim, W. ysgubo, Br. skuba, fr. late Lat. ScOpare (above). Vendryes, De hib. voc. 176. Loth, Mots lat. 216.
4. Goth. us-baugjan, prob. fr. caus, of biugan ‘bend’, with specialization from ‘make bend, turn aside’. Cf. ‘sweep’ fr. ‘swing’ in OE swapan, fr. ‘throw’ in Slav. mesti, etc. Feist 529 (with other views). Walde-P. 2.145 (otherwise).
ON sépa (with sdfl ‘broom’), Sw. sopa (older Dan. sobe), prob. fr. a root *sweb- beside *swep- in ChSI. sypati, etc. ‘strew, scatter’ (9
```


### [2026-09-04T18:58:51.619Z] TOOL RESULT

```
aod OHG /floz W.  cludair MHG oléz Br —_radell NHG floss
Many of the words for ‘raft’ are de- rived from the verbs for ‘float’. A few reconnected with verbs for ‘slide, slip’, here, too, doubtless through the notion of float’. Others reflect the construc- tion of rafts of sticks or logs, as ‘fasten- ing together, bundle, pile’, etc.
* Grk, oxeila, fr. fem. (sc. vats) of ee casual, temporary’ with refer- ton, ie light, hastily made construc-
: ‘do offhand, impro-
» Lat, ralis, often in pl. and defined
o
z fastened together’ (rates vocan- tunity, ale uae tiihon aul. Fest, )
lur
Walde-P.
CC-0. In Public Domain
Foundation Chennai and eGangotri
QMOTION, TRANSPORTATION, NAVIGATION 731
SCr. éun, Boh. élun (Pol. czdtno, Russ. éeln, celnok ‘skiff, canoe’), as orig. ‘dug- out’ : Lith. kelmas ‘tree-stump’, Lett. celms ‘stump’, OHG scalm ‘navis’ (Graff 6.491), Norw. skolm ‘pod’, etc., fr. IE *skel- in words for ‘cut, split, ete.’. Walde-P. 2.594. Berneker 167.
Boh. lod’ka, Pol. tédka, (also tédz larger ‘boat’), Russ. lodka : ChSl. ladijz, etc. ‘ship’ (10.81).
7. Skt. ndu- ‘ship, boat’, see 10.81.
Skt. plava- (also ‘raft, float’) : plu- ‘float, swim’ (10.34).
RAFT Lith. _ sielis Lett. pluosts, pluts, stelains ChSle nase SCr.  splav Boh. vor, pli’ Pol. tratwa, plet Russ. plot Skt. udupa- Av. A Bic
It. zaltera (Sp. zata, zatara, but not the usual word), fr. MHG tatze ‘paw’? REW 8599.
Sp., Port. balsa ‘raft’ (also ‘pool’, in Port. also ‘clump of briar bushes’). ‘Raft’ prob. based on the material used in its construction, but the ultimate source of the word is unknown (Iber.?). REW 917.
Rum. pluéd, also ‘cork’, fr. the Slavic, ef. Slov. pluta, SCr. pluto ‘cork’, Russ. plot ‘raft’? (below, 5). Tiktin 1193.
3. Ir. ratth, fr. Lat. ratis (above, 2). RIA Contrib. s.v.
NIr. slaod, also ‘swath, layer or pile, sliding mass’ (Dinneen), hence the meaning of ‘raft’ (in this sense also bathshlaod : bata ‘stick, timber’) = MIr. sldet ‘a slide’ (: OE slidan ‘slide’, etc., 10.42). Walde-P. 2.707f. Macbain 327.
. Gurukul Kangri Collection, Haridwar
Sie
732 SELECTED INDO-EUROPEAN SYNONYMS
W. cludair, also ‘heap, pile’ (Spurrell), hence the meaning ‘raft’ (fr. ‘pile of wood’) : cludo ‘carry, convey’, arch. ‘heap’ (10.61).
Br. radell, razell, see above, 2.
4. ON flott, Dan. flaade (both also ‘fleet’), Sw. jflotte (cf. flotta ‘fleet’), NE float (rare in this sense, NED s.v. 7a), Du. vlot, OHG floz (mostly ‘flux, flow’), MHG vl6dz, NHG floss: ON fijota, OF fléotan ‘float’, ete. (10.34). Falk-Torp 229.
NE raft, arch. (ME) ‘rafter, beam, spar’, fr. ON rapir ‘rafter’, coll. ‘roof, ceiling’. NED s.v.
5. Lith. sielis, Lett. sielains, prob. : Lett. siet ‘bind’. Leskien, Bildung d. Nom. 275. Mihl.-Endz. 3.858.
Lett. pluosis (= Lith. pluostas ‘fer- ry’) : plist ‘overflow’, OE fléotan ‘float’, etc. (above, 4). Miuihl.-Endz. 3.364, 365.
Lett. pluts, fr. ORuss. *pliitz, Russ. plot ‘raft’ (below, 6). Miuhl.-Endz. 3.359.
6. SCr. splav, epd. *sti-plav, of. pla pada ules pected o)
(poet.) ‘navis, linter’ (Rjetnik Akad 10.22) : ploviti ‘float’, ete. ;
Boh. vor, as orig. ‘a binding-togethe, (of logs) : Pol. wér ‘sack, bundle’, Chg] vriivt, Lith. virvé ‘cord’, Lith, verti ‘to thread’, etc. Walde-P. 1.263. Traut. mann 352. Briickner 382, 634,
Pol. tratwa, earlier trafta, fr, early NHG irift ‘a drive of logs’ 
(14th cent, still in local use; cf. Weigand-H, 2.1071 and similar use of NE drive in US.) : treiben ‘drive’. Briickner 575.
Russ. plot, Pol. ptet, Boh. plt’ : Russ, plavat', Pol. ptywaé, Boh. plovati ‘float’, Trautmann 224,
7. Skt. udupa-, also ‘moon’, particu- larly ‘new moon’ (whence the meaning ‘raft, barge’ as a ‘flat, slightly curved boat’?), MIndic for Skt. *rlu-pa-, lit. ‘keeper of the (correct) time’. Wacker- nagel, Altind. Gram. 1.167 (Uhlenbeck 28, but with unconvincing explanation of the meaning ‘raft’).
10.85 OAR Grk. —xéswry, tperpby Goth. .... Lith. irklas NG xourl ON Gr, redt Lett. irkls Lat. rémus (t6nsa) Dan. are ChSI.  veslo It. remo Sw. dra SCr. _veslo Fr. rame, aviron OE Gr, roper Boh. _ veslo Sp. remo ME ore Pol. wiosto Rum. visld, lopaté NE oar Russ. veslo I. rame Du. rem Skt. —_arttra-, kgepani-, nau- NI. ramha OHG ruodar, riemo danda- W. rhwyf MHG_ ruoder, ruodel, rieme Avy. Gc Br. roenv NHG ruder
Many of the words for ‘oar’ belong to an inherited group pointing to IE words for ‘oar’ and ‘row’. Other connections are with words for ‘carry, ride’ or for ‘rod, pole’.
1. IE *era-, *ré-, *rd- in words for ‘oar, rudder, row’ (perh. ultimately con- nected with IE *er- in Skt. 7- ‘move’, Grk. épvie ‘rouse, move’, but this quite uncertain). Walde-P. 1.143f. Ernout-
M. 859. Pedersen 2.591. Stokes 39,
Grk. éperpdy (cf. tpécow ‘row’, épérns ‘rower’); Lat. rémus (> It., Sp. remo, OFr. reime, W. rhwyf, Br. roefv; Fr. rame, back-formation fr. deriv. vb. Tamer ‘row’); Ir. ra@me, NIr. raémha; OE réper (NE rudder), OHG ruodar, MHG ruoder (also ‘rudder’), NHG ruder; Lith. irklas, Lett. irkls, irklis (cf. Lith. irti, Lett. wrt ‘row’); Skt. aritra- (cf. aritar- ‘rower’).
2. Grk.xomn, NG lit. coy, kwmlov, POP: xourl, orig. ‘handle’, hence the ‘handle of
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri > 4
{
LOCOMOTION, T
n ‘draw on’; sie n te., JE *tens- extenslo
) . ‘pull, drag» e ndere ‘stretch’, etc.; or
os ‘shear, crop, cut off’ ; ndere ‘shear,
en stick’?). Walde-P. 1.720,
88
fr, OF r. avirer ‘turn about’ epd. of virer ‘turn, tack’. Gamillscheg
i.
fr, aviron, (ound only 28 x28), change course, Veer,
fii lopatd, also and orig. ‘shovel’, fr. gvie lopata ‘shovel’ (8.24).
Rum. visld, fr. the Slavic, ef. ChSl. reslo, etc. (below, 7).
4, Ir. rame, etc., cf. above, 1.
5, ON ar, Dan. aare, Sw. dra, dr, OE ir, ME ore, NE oar, fr. Gme. *atro- (cf. Finn. loanword airo), without clear out- sideconnections. Walde-P. 1.167. Falk- Torp 7, 1429.
ON redi, prob.: MHG ruote ‘rod, pole’ also ‘oar-shaft, oar’ (NHG rute), OHG ruofa, OF rod ‘rod, pol
e’, etc. Falk-Torp 908 (against connection with OE roper, etc.).
roper, OHG ruodar, above, 1.
7 he OHG riemo, MHG rieme (above a ae pee Late remus ya/+ Lranck-y, W, ‘ oa ind, 1587, pete Wel . Lith, trklas, Lett. irkls,
+ Uns], veslo, etc,
*wegh-slo-) - vehi tide tlo-) : C
above, 1. » Beneral Slavic (fr. l. vozq, voziti, Lat.
ete. (10.66). W. a aritra-, above, | alde-P. 1.250, - kyepani- ox
(also ksepani-, ksipani-,
gitized by Arya Samaj Foundation Chennai and eGangotri
RANSPORTATION, NAVIGATION 733
etc.) : ksip- ‘throw, cast’ (10.25), fr. the ‘throwing motion’ involved in rowing.
Skt. ndaudanda-, ndukddanda- lit. ‘boat-pole’, cpd. of ndu- ‘boat’ and danda- ‘stick, staff’.
10.852. ‘Row’ (vb.). Nearly all the verbs for ‘row’ are connected with the nouns for ‘oar’, mostly those of the widespread group 1 of 10.85—either from their roots or, more commonly, derivatives, compounds, or phrases with them. Thus Grk. épécow; Lat. rém-igere (epd. with agere), VLat. *rémdre (It. remare, Fr. ramer, Sp. remar; Ir. radim (Pedersen 2.591), NIr. rdmhuighim, W. rhyfo, Br. roefivi; ON réa, Dan., Sw. ro, OE rowan, NE row, Du. roeien, OHG ruoderon, NHG rudern; Lith. irti, Lett. art; SCr. veslati (similarly Rum. visli, fr. visld), Boh. veslovatt, Pol. robié wiostem (lit. ‘act with the oar’).
But there are a few of different origin.
NG pop. Adpvw, fr. edabvw ‘drive’ (10.65), which is used for ‘row’ in NT, Mk. 6.48, Jn. 6.19, and so rendered in the other versions (Vulgate, Goth., OH, ChSL1., etc.).
Fr. nager, fr. Lat. ndvigare ‘sail’ (10.36), now commonly ‘swim’ or ‘float’, is also sometimes used for ‘row’, esp. in phrase nager de long ‘row with long strokes’.
It. vogare, Sp. vogar, fr. a Gmc. form like NHG wogen, deriv. of word for ‘wave’ (1.85). REW 9566.
Goth. farjan (for é\atyw ‘row’ in Jn. 6.19; also for wAéw ‘sail’) : OE faran, etc. ‘go’ (10.47).
```


## [2026-09-04T18:58:57.726Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"9\\.67 IRON\\|9\\.67  IRON\\|11\\.4. RICH\\|11\\.41 RICH\\|11\\.42 WEALTH\\|11\\.51 POWER\" SYN.txt | head"
}
```


### [2026-09-04T18:58:57.775Z] TOOL RESULT

```
15459:MISCELLANEOUS PHYSICAL ACTS, ETC. 613 . 9.67 IRON Goth. eisarn Lith. gelezis gldnpos ON isarn, jarn Lett. dzelzs [€p0 Dan. jarn Chl. Zeléso F ferrum Dan. jam SCr. Zeljezo, guozde ferro OE isern, isen, tren Boh.  Zelezo fer ME iren Pol. zalazo hierro NE tron Russ. Zelezo | fer Du. zzer Skt. ayas- jarn OHG  isarn, isan Av. ayah- garann MHG_ isern, isen ‘aan NHG eisen ou n is comparatively late 2. Grk. cidnpos, NG pop. otéepo
19585:11.42 WEALTH, RICHES
```


## [2026-09-04T18:58:59.563Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15459,15480p' SYN.txt | head -40"
}
```


### [2026-09-04T18:58:59.613Z] TOOL RESULT

```
MISCELLANEOUS PHYSICAL ACTS, ETC. 613 . 9.67 IRON Goth. eisarn Lith. gelezis gldnpos ON isarn, jarn Lett. dzelzs [€p0 Dan. jarn Chl. Zeléso F ferrum Dan. jam SCr. Zeljezo, guozde ferro OE isern, isen, tren Boh.  Zelezo fer ME iren Pol. zalazo hierro NE tron Russ. Zelezo | fer Du. zzer Skt. ayas- jarn OHG  isarn, isan Av. ayah- garann MHG_ isern, isen ‘aan NHG eisen ou n is comparatively late 2. Grk. cidnpos, NG pop. otéepo
neut., prob. a loanword, but source un- known. Schrader, Reallex. 1.239.
3. Lat. ferrum (> Romance words), orig. dub., loanword fr. Semitic (?). Schrader, Reallex. 1.240. Ernout-M. 352. Walde-H. 1.486.
4, Lith. gelezis, Lett. dzelzs, OPruss. gelso, ChSl. Zeléso, general Balto-Slavic word, perh. with Grk. xadxés ‘copper, bronze’ as loanwords fr. some common source. Walde-P. 1.629. Schrader, Reallex. 1.236.
SCr. also guozde, deriv. of old gvozd ‘nail’ (9.51), hence orig. ‘nail material’. Berneker 366.
5. Skt. ayas-, Av. ayah-: Lat. aes, etc. See 9.66.
Skt. ¢ydma- ‘black’ is used with ayas- or alone for ‘iron’. Macdonell-Keith 1.31 f.
r 9.68 LEAD an Goths isis Lith.  Svinas plumbum ON bly Lett. _svins Piombo Dan. bly ChSl. olovo plomb Sw. bly SCr. _olovo Plomo OE léad Boh. _olovo plumb ME ede Pol. oléw luaide NE lead Russ. svinec luaidhe Du. —_lood Skt. sisa- Plum OHG blio Av. srva- Ploum MHG bli NHG ble:
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
614
Lead dates from the bronze age in the eastern Mediterranean region and pos- sibly in Britain, but in most of Europe it is contemporaneous with iron. Among the words for ‘lead’ there is a group com- mon to Celtic and Gmc., resting on bor- rowing, and probably the Greek and Latin words are from a common, un- known source. There is some confusion between ‘lead’ and ‘tin’. Schrader, Real- lex. 1.149 ff.
1. Grk. pédvBd0s (with variants pd6d.- Bos, Bddtpos, BodBos), NG pordbBr (also BoXtur), doubtless a loanword, but source unknown. Boisacq 644.
2. Lat. plumbum (> Romance words, also W. plwm, Br. ploum), prob. a loan- word fr. the same source as the Grk. word. Ernout-M. 781.
3. Ir. luaide, NIr. luaidhe; OE léad, ME lede, NE lead, Du. lood (MHG lat, NHG lot ‘lead’ as ‘solder’ or ‘plummet’; so also Dan., Sw. lod, fr. MLG). The Gme. words are prob. borrowed from Celtic, and the latter perh. deriv. of IE
SELECTED INDO-EUROPEAN SYNONYMS
*pleu- in words for ‘flow, float’, ete applied to the quickly melting lead, Walde-P. 2.442. Franck-y. W. 3961, 4. ON bly, Dan., Sw. bh OHG 5) bi (gen. bliwes), MHG bi, NHG yi pointing to a Gmc. *bliwa-, perh. : Lith,
blyvas ‘violet colored’, etc. Walde-p 2.210. Falk-Torp 86. 5. Lith. Svinas, Lett. svins, Russ
svinec, etym. dub. Persson, Beitriige 745 Buga, Kalba ir Senové 262,
OPruss. alwis ‘lead’, Lith. alvas ‘tin’ Lett. alvs, alva ‘tin’, ChSl., SCr., Boh; olovo, Pol. oféw all ‘lead’, but Russ. olovo ‘tin’, orig. a color word (with charac- teristic -wo-suffix) with application to either ‘lead’ or ‘tin’ and subsequent varying distribution in this respect, But root connection dub. (OHG elo ‘yellow’, etc.?). Walde-P. 1.159, 2,449,
6. Skt. stsa- neut. (AV-+, cf. Mac- donell-Keith 2.452), etym.?
Av. srva- neut. (Barth. 1649), NPers, surb, etym.?
```


## [2026-09-04T18:59:00.096Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19580,19620p' SYN.txt"
}
```


### [2026-09-04T18:59:00.161Z] TOOL RESULT

```
Skt. dhana-, in Vedic mostly ‘prize (of contest), stake, booty’, whence also ‘property, wealth’, prob. : dha- ‘set, place’, Grk. ri@nut, ete., ef. Grk. dena ‘deposit of money, pledge’. Uhlenbeck 134. Walde-P. 1.828.
Skt. dravya-, also ‘material, sub- stance’, this perh. as orig. ‘building ma- terial’, fr. dru- ‘wood’. Uhlenbeck 132.
Skt. apnas-, also ‘earnings’ : apas- ‘work’, Lat. opus ‘work’, ops ‘riches, wealth’, Grk. dumvn ‘food’, ete. Walde- P. 1.175. Uhlenbeck 10.
Ay. gaéa- (= OPers. gaiéa-), lit. ‘being, material being, substance’ then ‘house and home’, whence, in general, ‘possessions’ (esp. as ‘worldly posses- sions’), fr. the root *gez- ‘live’ in Av. fiva-, Skt. jiva- ‘alive’ (4.74). Cf. for semantic development Skt. gaya- ‘house, household’. Barth. 476f. Walde-P. 1.668.
Av. 7ti- ‘power, possession, property, wealth’ (Barth. 376) : Goth. azhis, etc., above, 4.
11.42 WEALTH, RICHES
js Goth. bet i 3 Ao gaber Lith. bagotyste diniion A Bibs ON audr, audefi (rik- Lett. bagdtiba ricchezza _domr) ChSl. bogattstvo Tichesse Dan. —rigdom, formue SCr. — bogatstvo riqueza Sw. rikedom, férmégenhet Boh. _ bohatstvi Gere, bogatie on wela, ad Pol. bogactvo Saidbre, somme IE welthe, richesse, wele Russ. bogatstvo veers, maoin ae wealth, riches Skt.  dhana-, vasu-, rat- vit oath OHG sider, ssrnoeen Av. — Saéla-, iSti- tgez wolo, welida, richid MHG Friliccrd bo 8 Notion of « NHG  reichtum, vermégen Versally ee Wealth, riches’ is Sait P ! é ay ee toperty Buished from th ot | property, wealth’, and in fact in primi- Ye used ith ds f at of | tive society any ‘property’ beyond
household goods and a few domestic animals constitutes ‘wealth’. But in the
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
;
772 SELECTED INDO-EUROPEAN SYNONYMS
European languages there are distinc- tive words for ‘wealth’, most of them de- rived from the adjectives for ‘rich’ (11.51; but sometimes conversely ‘rich’ from ‘wealth’); and there are also cer- tain of the words for ‘property’ which are most often used with the implication of ‘wealth’ and so are also entered here in second place, e.g. NHG vermégen.
1. Grk. mAodros (6, but in Byz. de- clined as neut. c-stem, hence) NG pop. pl. mAobrn : rodbs ‘much, many’, mAetos, Att. wAéws ‘full’, ete. Walde-P. 2.64.
NG Bids, see 11.41.
2. Lat. divitiae, fr. dives ‘rich’ (11.51).
Lat. opés : Skt. apnas- ‘property’, etc. (11.41).
It. ricchezza, Fr. richesse, Sp. riqueza, derivs. of It. ricco, etc. ‘rich’ (11.51).
Rum. avere, see 11.41.
Rum. bogatie fr. the Slavic (below, 5).
3. Ir. satdbre, NIr. saidhbhreas and saidhbhreacht, fr. Ir. saidbir ‘rich’ (11.51).
Tr. somme, sb. use of adj. somme ‘rich’ (11.51). Cf. also somaine esp. ‘profits’ (Laws, Gloss. 672).
NI. maoin, fr. Ir. moin, main ‘object of value, treasure’ (11.46).
W. golud : Ir. folad ‘substance’, fr. a epd. of W. gwo-, Ir. fo- (IE *upo-), anda deriv. of the root in Skt. lota- ‘booty’, Goth. laun, OHG lon ‘pay, reward’, etc. (11.78). Walde-P. 2.380. Pedersen 1.54.
W. cyfoeth, also (and orig.) ‘dominion, power’, cf. OCorn. chefuidoc ‘omnipo- tens’: Ir. cwmachte ‘power’, con~iccim ‘ean’, etc. Pedersen 1.124.
Br. pinvidigez, fr. pinvidig ‘rich’ (11.51).
4, Goth. gabei : giban ‘give’ (11.21).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
ON audr (also audasi, epd. with eens ond member deriv. of of ‘excess, multi. tude’), OF éad, OHG in al-dd ‘free Pos- session’ (hence MLat, allodium), OS od ‘possession’ : ON audna ‘fortune, fate’ audinn, OE éaden ‘granted by fate’ Goth. audags ‘naxdpws’, ete, perh, of mythological origin, with reference to the weaving of the goddess of fate, fr, the root in Lith. austi ‘weave’, ON vay ‘piece of cloth’, ete. Walde-P, 1.16 f, Falk-Torp 530. Feist 63.
Dan. formue, Du. vermogen, NHG vermogen, see ‘property’ (11.41).
Sw. férmégenhet, deriv. of Sormégen ‘powerful, wealthy’, fr. MLG vormo- gen(de) pple. of vormogen ‘be able’ = Du. vermogen, etc. ‘be able’ as sb, ‘power, wealth’ (above).
OE wela, ME wele (NE weal), OHG wolo, welo, etc., with deriv. suffix ME welihe (not found in OF), NE wealth, OHG welida: OE wel(l), OHG wola, wela adv. ‘well’, etc.
ME richesse fr. OF r. richesse; then conceived as pl. form in ME, NE riches.
Du. rijkdom (MLG rikedém > late ON rikdémr, Dan. rigdom, Sw. rike- dom), OHG richiduam, rihtuom, MHG richtuom, NHG reichtum, orig. and in the earlier language mostly ‘power, domin- ion’ (OE riceddm only in this sense), fr. OHG richi, OF rice, ON rikr, ete. ‘mighty’, later ‘rich’ (11.51).
5. Lith. bagotysté, Lett. bagatiba, ChSI. bogatisivo, etc., fr. the Baltic and Slavic words for ‘rich’ Lith. bagotas, Lett. bagats, ChSI. bogatii (11.51).
6. Skt. dhana-, vasu-, rai-, Av. tli, see ‘property’ (11.41).
Ay. Saéta-, etym. dub. Barth. 17041.
Digitized by Arya Samaj Foundation Chennai and eGangotri > /
Digitized by Arya Samaj Foundation Chennai and eGangotri
ERCE 773 PROPERTY, COMM pOSSESSION, 11.43 MONEY atts, fathu Lith. pinigat ; a Gor fe, peningar (baugr) ea ite ort ee, aphbess Dan. penge SCr. aoe vet x0 rd Byes 2eenee Boh. abe } pals ges, arger OE feoh, sceatt oh. penize a pean 1 ME mone(ye), fe Pol. pieniqdze rel NE money Russ. den'gi It ce Du. geld Skt. (dhana-) Be nea OHG  scaz, gelt Avs hi) % soni, porale MHG  gelt, schaz i NHG geld vi igen od Cae j,  orchan ord of value in the IE ; names of particular coins, the latter in he chief oa history of the IE- | part derived from the name of the metal riod ae Jes before the introduc- | used, especially ‘silver’. In one group a a money’ based on coinage | ‘money’ is from ‘payment’. 10)
f ; ‘live- cattle (in the old yclessense
wk). This is amply attested for the several peoples by direct references and i; ako reflected in the interchange of tattle’ with ‘property’ or ‘money’ in an inherited IE group and some others (315). Cf. Schrader, Reallex. 1.371 ff., and, especially for Celtic, Vendryes, RC 42.881 ff.
```


## [2026-09-04T18:59:07.711Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"9\\.66\" SYN.txt | head; echo ===; sed -n '15440,15459p' SYN.txt"
}
```


### [2026-09-04T18:59:07.780Z] TOOL RESULT

```
Exit code 1
991:though the root connection is uncertain, the sense ‘rock, stone’ is more widely dis- tributed and prob. earlier. Walde-P. 9.66. Falk-Torp 223.
13511:9.44 9.45 9.46 9.47 9.48 9.49 9.50 9.51 9.52 9.53 9.54 9.55 9.60 9.61 9.62 9.63 9.64 9.65 9.66 9.67 9.68 9.69 9.71 9.72 9.73 9.74. 9.75 9.76 9.81 9.82 9.83 9.84 9.85
15283:1. Grk. xadxets, orig. ‘worker in cop- per’, generalized, already in Hom., to ‘worker in any metal, smith’, deriv. of xadxés ‘copper, bronze’ (9.66).
15307:Skt. lohakdra-, epd. of loha- ‘copper’ (9.66) and -kara- : kr- ‘do, make’.
15426:9.66 COPPER, BRONZE
15464:5. Skt. ayas-, Av. ayah-: Lat. aes, etc. See 9.66.
19630:Lat. aes ‘bronze’ (9.66), hence, since the early coins were of bronze, ‘money’ esp. in the expression aes aliénum ‘another’s money’ = ‘debt’ (11.64).
(eval):1: == not found
```


## [2026-09-04T18:59:09.460Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15426,15458p' SYN.txt"
}
```


### [2026-09-04T18:59:09.513Z] TOOL RESULT

```
9.66 COPPER, BRONZE
Goth. azz Lith. varis, Zalvaris, bronza xarxés i; ON koparr, eir Lett. kapars, vars, bronza xaxbs, HAOX Ply Dan. _ kobber, bronze ChSl. médt
prpodrrfos aan koppar, brons SCr.  mjed, bakar, bronza acs pes OE copor, ar, bres Boh.  méd’, bronz rame, one; adrain ME coper, bras Pol. miedz, bronz, spiz Se cans NE copper, bronze Russ. med’, bronza . ane, arama, bronz Du. _ Koper, brons Bit. «5 lola aaa " umae, credumae OHG = kupfar, ér Vg a umha, pras MHG kupfer, ér NHG  kupfer, erz, bronze
must still be so understood in the Eng- lish Bible and in old references to classi- cal antiquity (cf. NED s.v.). MHG messinc, NHG messing represent a wide- spread Gme. group (OE mesling, NE dial. maslin, cf. NED), whence also the Lith., Lett., Boh., Pol. words for ‘brass’, but of uncertain origin (cf. Schrader, Reallex. 1.269, 2.62). The group Fr. laiton (> Russ. latun’), It. ottone, etc., is also difficult’ (REW 4933). ‘Brass’ is ‘yellow copper’ in Du. geel koper, SCr. Zuta mjed. Grk. dpetxadxos lit. ‘moun- tain copper’ (whence Lat. aurichalcum with spelling after aurwm), an alloy of unknown character, later used for ‘brass’, as in NG.
1. IE *ayes-. Walde-P. 1.4. nout-M. 19. Walde-H. 1.19.
Lat. aes, gen. aeris (cf. aénus, ahénus, fr. *ayes-no-, Umbr. ahesnes ‘shenis’), whence late aerdmen, *aramen (> It. rame, Rum. aramd ‘copper’, OFT. arain, Br. arem, Fr. airain ‘bronze’); Goth. aiz, ON eir, OE ar, OHG ér; Skt. ayas-
Er-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
612 SELECTED INDO-EUROPEAN SYNONYMS
prob. ‘bronze’ in Rigveda (Zimmer, Altind. Leben 51f. Macdonell-Keith 1.31 f.), later ‘iron’, Av. ayah- ‘bronze’ (as shown by epithets ‘yellow, golden’; cf. Geiger, Ostiran. Kultur 148), later fron’ as NPers. dhan.
2. Grk. xaAxés, prob. a loanword and possibly fr. the same source as Lith. gelezis ‘iron’, etc. (9.67). Walde-P. 1.629. Boisacq 1049.
NG pop. umaxipt, like SCr. bakar, fr. Turk. baker ‘copper’. Lokotsch 193. Berneker 40.
3. Lat. aes Cyprium ‘aes from Cy- prus’, like aes Corinthium, aes Cam- panum (cf. vasa Campana ‘vessels of Campanian bronze’, source of It. cam- pana ‘bell’). Hence late Lat. cuprum ‘copper’, whence Fr. cuivre (> Br. kouevr), Sp. cobre, Rum. cupru, and the Gme. words, OE copor (rare), OHG kup- Jar, etc., also W. copr (fr. ME) and Lett. kapars (fr. LG).
4. It. bronzo, whence NG umpoivrtos, Fr. bronze, and similar forms in nearly all the present European languages, orig. disputed, best derived, not fr. Pers. biring ‘copper’ (as REW 1113, etc.), but fr. aes Brundisium. The best bronze mirrors were made at Brundisium (spe- cula Brundisina, Pliny 33.130) and Byz. Bpovrjcvov ‘bronze’ occurs in the works of the alchemists (e.g. Berthelot, Alchi- mistes grecs 376.25). Berthelot, Rey. arch. 1888.295 ff. Wartburg 1.373 says “Aes Brundisium wire sachlich gerecht-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
fertigt, aber lautlich unmoglich” the phonetic difficulty seems less th
that in the deriv. fr. Pers, biring, esp an the o- vowel admittedly unexplaine r,
5. Ir. umae (also crédumae, cpq of cred ‘tin’, Windisch, Wtb. s.v., K. Me er, Contrib. 509, 511), NIr. umha, Ow emid, W. efydd : Ir. om, W. of ‘raw? hence orig. ‘raw ore’, Pedersen 1.166,
6. OF bres (both this and Gr render Lat. aes. Cf. Aelfric, Gram. aes, bres 000e ar), ME bras (> NIr. pras, W pres), NE brass with change of applica. tion, etym.?
OHG aruz(zi), erizee, MHG arze erze, NHG erz ‘raw metal, ore’, now often ‘bronze’, etym. dub. Schrader, Reallex. 1.262. Walde-P. 2.360.
7. Lith. varis, Lett. vars, OPruss war- gien ‘copper’, also Lith. Zalvaris ‘bronze’ (epd. of Zalias ‘green’), perh. loanword from a language of the Finnish group. Schrader, Reallex. 1.262. Miuzhl.-Endz, 4.484,
8. ChSl. médt, ete., general Slavic (SCr. also bakar, see above, 2), etym. dub. Berneker 46. Walde-P. 2.222.
Pol. spiz ‘bronze’, fr. MHG spise ‘food’ and also ‘metal ready for casting’ as in NHG glockenspeise ‘bell-metal’. Briickner 509. Weigand-H. 2.908.
9. Skt. loha-, lohdyasa-, lohitayasa- ‘copper’ (cf. Macdonell-Keith 1.31f.) : loha- ‘red’ beside rohita-, rudhira- ‘red’, etc. Walde-P. 2.358 f.
Skt. ayas-, Av. ayah-, above, 1.
se of iro : cia, long after the period of Il
unity. Most of the words are of obscure _ The only agreement between the different branches of IE is that be- tween Celtic and Gme., which reflects prehistoric borrowing.
1. The Celtic and Gme. group. Walde-P. 1.4. Schrader, Reallex. 1935f. Feist 131. Pokorny, KZ 46,292 ff., 49.126. Walde-H. 1.19 f.
Ir. iarn, NIr. tarann, W. haearn, Br. houarn, fr. a Celt. *tsarnon (cf. Gall. Isarnus, etc.), whence the Gmc. group, Goth. eisarn, ON zsarn (the more com- mon ON jarn by later borrowing fr. Ir. iarn), OB isern, tsen, OF, ME iren, NE iron, OHG isarn, isan, NHG eisen, etc. The Celt. *tsarnon perh. itself of Illyrian origin (there is a similar Illyr. river hame, and the Hallstatt iron finds are
earlier than the Celtic) and : Skt. isira- strong’,
origin
Digitized by Arya Samaj Foundation Chennai and eGangotri
```


## [2026-09-04T18:59:14.342Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==35' HRN.txt"
}
```


### [2026-09-04T18:59:16.145Z] TOOL RESULT

```
13
umgekehrt osk. mo-, umbr. ero- jener' gegenüber ap.
aita-, aw. aesa-, skr. esd-. Die Dehnung des ä ist
speciell mittel-neupersisch.
Darmesteter's Etymologie (aus ap. aniya-) ist
falsch, denn ap. aniya- hätte im Np. kaum etwas
anderes als m oder in werden können. Zudem kommt
das Ideogramm "]; nur durch Nachlässigkeit der
Schreiber für aw. anya- vor; das letztere Wort wird
vielmehr regulär durch ""XDi wiedergegeben. Im
Ya^^nöbi hat sich anya- in Form und Bedeutung sehr
getreu bewahrt; hier findet sich ani mUi am andern
Tage*, any adam ein anderer Mensch', anyokai 'anders-
wo* (Salemann, Mel. asiat. IX, 234); vergl. auch
wa/. sar. yan anders* (Tomaschek, Pämir-Dial. 817).
Daneben ü in np. aöün (neben andün nach edün
gebildet); phlv. a (Stellen bei Hörn, ZDMG. 43, 45
Note 28); bei. s. ä und in Zusammensetzungen (8).
Formen der np. Dialekte, wie Käs. ü, T, tat. ü darf
man nicht vergleichen, da wir es hier auch mit dem
Pronomen der dritten Person zu thun haben können.
In Zusammensetzungen findet sich aber üco {== änja)^
uro (= an räh), üzü {=•- an sän) u. a. m.').
53. mväre Verloren* etc.
ap. *a + i^bar- ; phlv. apar (vd. 5, 33, GL), mand. LW.
INIX 'Verwüstung*, vergl. äpar^ apar(i)sn *Raub*, apartan^
äpurtan plündern', d. i. überall äw^ (Men.).
bei. LW. awar Beute, Raub' (20); arm. LW. aimr
'Raub, Beute*, ayarem 'rauben, plündern* (nach S. Bugge,
Indog. Forsch. I, 454 vielleicht statt ^anar aus gr.
svuQa; aber warum so gekünstelt?).
54. üväz 'Stimme*, äväze, äväzlden,
aw. ai. ä + [/^vac-, s. np. vaj (No. 1072) ; phlv. aväj
bzw. äväc 'Stimme , arm. LW. avaj\ avac,
afr. kurd. bei. LW. avüz,
55. ärverdeti (AM. ; im Reim Sahn. I, 4 Vers 66 ; heutige
>j Mittlerweile auch KZ. 32, 578, No. 3; vergl. auch F. Solmsen ,
KZ. 31, 472.
```


## [2026-09-04T18:59:19.678Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==36' HRN.txt; echo \"=== grep ahan ===\"; grep -n \"āhan\\|ähan\\|äsin\\|äsen\\|äsn\\|asin\" HRN.txt | head -20"
}
```


### [2026-09-04T18:59:21.154Z] TOOL RESULT

```
- 14 -
Aussprache : äivtirden), Praes. äwerem^ är-em^ ätrertden ;
jüd.-pers. Bibelübersetzung: pTI2X neben TIIN.
ap. *^+|/6ar-; päz. äwardan, ätvurdan, äivar-am,
beL (LW. ?) ärag, n. aray, awarta (14).
56. ävey(ten 'hängen, aufhängen', Praes. avez-em^ ät^ezis^
vergl. avenffy ävingän 'hängend'^).
phlv. ave/fan 'hängen , Mit7']avec (Gemme, ZDMG. 18
No. 54 (IV) --- Paris, No. 1349).
oss. d. awinjiü}, t. avinjin 'hängen' (6); kurd. hil]avistw,
hal]avism (H.-Sch.) aufhängen'.
Nöldeke (mündliche Mitteilung) meint, dass sich
eine Anknüpfung an ai. V^vij-, vijdte wohl durch eine
anzunehmende Zwischenbedeutung 'bummeln' vermitteln
lasse. Die von Fr. Müller (WZKM. 5, 184) verglichene
altslavische Wurzel stimmt lautlich nicht zu den
iranischen Formen.
57. ähen 'Eisen'; ähemn 'eisern 2).
Semn. ösün; g. vuhen,
phlv. äsm (z. B. vd. 5, 121), ämtm 'eisern*.
kurd. hasin ^ hesin (Jaba-Justi), üsin (Houtum-
Schindler) 'Eisen ; bei. LW. ahin (18); wa;^- «'^'^ (?)•
Das Verhältniss zu af/. öspana ,, öspma; oss. äfsan
(42); ^iyn, sar. spiu 'Eisen* ist nicht aufgeklärt^). Fr.
Müller (WZKM. 5, 258) denkt für diese Worte an
Zusammenhang mit phlv. spenäk; eine Wurzel ad^-
schneiden* im Altpersischen anzunehmen, liegt jeden-
falls meines Erachtens kein genügender Grund vor.
58. ahen^J^den 'ziehen, herausziehen*, vergl. ahi/Jen
{ahe/ten)^); ahenje^),
*) So (Wörterbücher: ävengän) steht im facsimilirten Text des
Seljuqname, bei Sohefer 76, 7. (Ich verdanke dieses Citat Prof.
Nöldeke.)
^) Nach dem BQ soll äyen eine Nebenform zu np. ähen sein;
Belege fehlen.
^) Schrader, Sprachvergleichung und Urgeschichte*, 286 be-
friedigt nicht; die zweite Auflage ist mir nicht zur Hand.
*) Rück er t zieht ZDMG. 8, 264 vielleicht mit Recht auch np.
ä/tcn hierher; dann vergl. auch yä/ten^ yäzlden,
5) Bei. LW. C?) ähihjag, n. ähenjuy *ßaiid, Gürtel' (U).
=== grep ahan ===
715:vergl. aber näsnä (No. 1019).
734:34(i). äsna 'bekannt', äsnäyt,
735:ap. *ä(x)snäka- 'bekannt'; phlv. äsnäk.- 9 ~
736:34(2). äänä, äsnäh 'Öchwinuner, Schwimmerei', üsnäh^ dsnäiv,
738:vergl. aber aw. asnätar-, skr. äsnäna- (*Bad').
790:ähandS' 'schwellend, strotzend'; vergl. lit. (/awd 'genug,
941:kurd. hasin ^ hesin (Jaba-Justi), üsin (Houtum-
2552:Ob np. hiyähan überhaupt etymologisch ohne Wasser
2712:phlv. pacm (Bund.) ; bei. pädin, n. päsin 'Ziegenbock,
2729:aw. päsna- 'Ferse'; phlv. päsnak*^ ai. pdrsni-,
2732:päsna, sar. pu/nä 'Ferse'.
3652:tiirt, si/n. täsna, täsnagl, yidg. triisna.
4008:433. i^äSt 'Frühstück', cüäte, ca§ti, cääne^ cäsnl, cesiden.
4757:g. däsn.
4758:phlv. dah(i)Sn ; vergl. padäsn (No. 265*'^'').
6955:g. äsnuftmün.
6956:aw. l/^srar-, surunaoiti 'hören'; phlv. vergl. äsnütan,
9987:847. Der Präsensstamm kün- mit dem Infinitiv kerde findet
10135:27. äsn natürlich, eigen (AW.-Komm., Mön.).
10330:aw. dasina- rechts*; ai. daksina-.
```


## [2026-09-04T18:59:45.395Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"āhen\\|ahen\\|āsen\\|asen'\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n \"āsēn\\|asen\\|āhen\\|ʾsyn\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-04T18:59:45.454Z] TOOL RESULT

```
PHD.txt:181:a-gumég Pgwmyk! | M ?gzumyg] unmixed, pure. ~ih: purity. 33? águstan Pkwstn! | M ”gwst] hang up, suspend. 8.45% X wc āhan pA(y)n! ,^s(y)n! | M ?hwn, N ~] iron. ~én ['synyrn!] iron, of iron. ~gar [-kl | N ~] blacksmith. ahang [hng] pull, draught. āhanjīdan [?hncytn!] = āhixtan. ahanüz Phnwe | M *hnwn-c, N haniiz] yet, still. āhen = āhan, q.v. аһа Phyt' | M QYAyd] stain, impurity; confused. ^Àh : pollution; confusion.
PHD.txt:1523:decrease (vt.) kahenidan, kāstan.
PHD_mackenzie.txt:3147:kahenidan, kahen- [k)hyn-ytn l ] decrease, lessen (tr.).
PHD_mackenzie.txt:6350: decrease (vt.) kahenidan, kastan.          desirous kiimagomand.
PHD_mackenzie.txt:6864: immortal ahos, amarg, anos(ag).          inform agahenidan, azdenidan.
PHD_mackenzie.txt:9739:kahen-                               -tUU',      kistarI
PHD_mackenzie.txt:9741:kahenidan                   ,,~t'\)UI'           kistanI
PHD_mackenzie.txt:11749:                               ~      agahenidan.             \\tfJ tW"" Y
PHD_mackenzie.txt:11858:agahen-              -~~           Ardwahist           \~\~"'"
=== NYB ===
686:āsēn ['syn'] iron 1105. — MPrth ”swn; MPrs ”hwn (List 79); Paz. āhin(-sāxt) (Aog.); NP āhan. Ci Benveniste, MSL 23, 1927, 132 sq.; 30, 1930, 60.
687:āsēnēn adj. of iron 2076. 2327, 241; ~-sumb v. sumb.
1946:thas [KZY] early, in the beginning: ~ hac apürik xYarišn before the other food 922; [~-am i pat bun nipišt ku ... pre- viously, in the fundamental chapter, I wrote ... BdA p. 41! (Henning, JRAS 1942, 241, n. 1 not acceptable)]. - NW w., also hasë, adj. hasenak (MPrth hsyng) ; SW ahé, adj. ahénak (MPrs ’hyng): Ny- = berg, Henning Vol. 343—348.
2982:death of A. 1? etc. passim; without hac: ~ i naxcir after the hunt 1418-14; followed by an inf. or the v. n. in -i5n(éh) it stands for a temporal clause: ~ hac matani... 4018; ~ hac be vitirišneh 65117, etc. pas- sim; introducing a full temporal clause: ~. hac hàn i .. . 6zat but 818; ~ hac hàn i ka 174, 965. — Av. (882 sq.) pasca; Milr NW paš (cf pasémanéh), SW pas, v. Tedesco, Dial. 209 sqq. — V. also paséh, pasen.
3257:. rasend the souls of the Righteous reach salvation 8825-26, — SW only: OP pres. rasa- from ar- ‘to move, to go or come toward’ (Av. [183] !ar-);; MPrs. rsydn; Paz. NP rasidan.
3711:tan [tn'] body, passim, stalk of a plant 9524; ~ u jan body and vital spirit 1523. 6422 (the constituents of human physical nature); ~ u jan u hir u xvāstak 4%; kanišn 4 jan u višopišn i ~ the destruc- tion of the vital spirit and the decom- position of the body (= the physical death) 64191; ~o as opposed to the immortal soul, ruvān 6625. 6820, 6927, 7615-17-18; — — also refers to the human individual as a whole, with all its physical and spiritual qualities, cf 65? sqq. 6611. 8414. 8671; har —-E rad hamgöhr fravahr et 4 x"eš paitak it is revealed that every human individual has its own fravahr (g. v.) of the same substance as itself 88°; xueš.— and ~ 4, avēš v. aueš; — ~ i pasen the ultimate form of existence the Universe will be given after the now running eycle of millenia has elapsed, the next world, Eternity; very often ristaxéz (q. v.) u ~ + pasen: 12%, 6411-13, 7118-19, 7610, 8326, 8821, 919; ~ 4 pasén alone 5212-13, 66°. 677. 934. 104%. — Av. (633 sqq.) tanū-; common Ir.
4137:vigräs- [wgl’s-] pres., to rouse a p. from sleep, from the dead: apäc vigräsend 10179; d(h) vigrasend 101°. — Av. (511) lgar-, v. guhräyenitan; MPrth wygr’s ‘to awake’, MPrs ‘to rouse from sleep’; Ver- bum 196; Ghilain 82, 92-93.
5694:’P)be’r: apa-car ’P)fr’h: äfräs »gwst: &kustan ”gynyn: hakanēn »hwn: āsēn "Cog: ārak »ryšnwg: arišn »stw'n: ästavän »stw'nyy: āstavānēh "stwnd: astomand St: āštēh
6331:ähin: āsēn
6976:ähan: āsēn
```


## [2026-09-04T18:59:53.677Z] TOOL CALL #32: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T18:59:53.683Z] TOOL RESULT

```


```


## [2026-09-04T18:59:56.928Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%87%D9%86",
 "prompt": "Give the full Persian etymology section for آهن (āhan) 'iron': Middle Persian form, Proto-Iranian reconstruction, PIE root, cognates, and any cited authorities (Hasandust, MacKenzie, Bailey, Cheung)."
}
```


## [2026-09-04T18:59:59.159Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C3%A9yos",
 "prompt": "Give the full reconstruction, meaning, descendants (Indo-Iranian, Latin, Germanic), and note whether Avestan ayah- and Persian āhan are listed as descendants. Also any note about the Cyprus/Alashiya theory."
}
```


### [2026-09-04T19:00:02.018Z] TOOL RESULT

```
# Persian Etymology of آهن (āhan) 'iron'

Based on the Wiktionary entry provided, here is the available etymological information:

**Middle Persian origin:** The word derives from Middle Persian ʾh(y)n' (āhan), meaning "iron."

**Proto-Iranian reconstruction:** It traces back to Proto-Iranian *Hácwā.

**Limitations of available information:** The webpage does not provide:
- PIE (Proto-Indo-European) root information
- Cognates from related languages
- Citations to scholarly authorities like Hasandust, MacKenzie, Bailey, or Cheung

The entry includes only the basic etymological chain: Modern Persian آهن ← Middle Persian āhan ← Proto-Iranian *Hácwā. For more detailed etymological analysis, including PIE roots and scholarly citations, you would need to consult specialized etymological dictionaries or academic sources beyond this Wiktionary entry.
```


### [2026-09-04T19:00:05.252Z] TOOL RESULT

```
# Proto-Indo-European *h₂éyos

**Full Reconstruction:** *h₂éyos (neuter noun)

**Meaning:** A metal, specifically copper or bronze

**Key Descendants Listed:**
- Proto-Germanic: *aiz
- Proto-Indo-Iranian: *Háyas
- Proto-Italic: *aos

**Important Note:** The page does not list Avestan ayah- or Persian āhan as descendants, nor does it mention the Cyprus/Alashiya theory. The descendants section directs readers to see related entries for "further descendants" but provides no additional specifics beyond the three proto-language forms noted above.

**Linguistic Significance:** The article states: "This shows that the Indo-European language was spoken during a time when copper was used," indicating the word's historical importance for dating the proto-language period.
```


## [2026-09-04T19:00:10.427Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C3%A1cw%C4%81",
 "prompt": "Give the reconstruction, meaning, its Proto-Indo-Iranian/PIE ancestor, all descendants (Persian, Ossetian, Pashto, Khotanese, Avestan etc.) and any references cited."
}
```


## [2026-09-04T19:00:11.522Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/H%C3%A1yas",
 "prompt": "Give the reconstruction, meaning, descendants including Avestan ayah- and any Iranian continuations, and references."
}
```


### [2026-09-04T19:00:17.603Z] TOOL RESULT

```
# Proto-Indo-Iranian *Háyas

**Reconstruction:** *Háyas (neuter as-stem noun)

**Meanings:** 
- A metal
- Copper

**Etymology:** Derived from Proto-Indo-European "*h₂éyos" meaning "copper, bronze"

**Key Descendants:**

- **Sanskrit:** áyas (अयस्) - continuing from Proto-Indo-Aryan *Háyas
- **Avestan:** aiiah (𐬀𐬌𐬌𐬀𐬵) - meaning "metal, iron" - continuing from Proto-Iranian *Háyah

**Reference:**

The entry cites Lubotsky, Alexander (2011), "áyas-" in *The Indo-Aryan Inherited Lexicon* (Indo-European Etymological Dictionary Project), Leiden University, as documented in the Wiktionary reconstruction page last updated August 23, 2026.
```


### [2026-09-04T19:00:18.603Z] TOOL RESULT

```
# Proto-Iranian *Hácwā - Iron

## Reconstruction
**\*Hácwā ~ \*Hcunáh** (masculine noun)

## Meaning
"Iron" or "ironstone"

## Etymology
The word derives from Proto-Indo-Iranian *\*Háćwā ~ \*Hćunás*, which comes from Proto-Indo-European *\*Héḱ-wō ~ \*Hḱ-unés*. It possibly originated from *\*h₂eḱ-* ("sharp") combined with the suffix *\*-w-* and *\*-ō*.

A semantic merger likely occurred with descendants of *\*Hácwr̥* ~ *\*Hcwán* ("ploughshare").

## Major Descendants

**Southeastern Iranian:**
- Pashto: wëspëna, óspëna
- Khotanese: hīśśanä
- Wakhi: išn, yišn

**Northwestern Iranian:**
- Kurdish: asn, hesin, asin
- Baluchi: âsin, âsan

**Southwestern Iranian:**
- Persian: āhan
- Tajik: ohan
- Ossetian: æfsæn (ploughshare, from the merger word)

## References
Cited works include Buyaner (2020), Bailey (1979), Rastorgujeva & Edelʹman (2000), and Morgenstierne (2003) on comparative Iranian etymologies.
```


## [2026-09-04T19:00:27.907Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hīśśan\\|hissana\\|hiśśan\\|hīssan\" ISS_alt_DKS.txt | head -10"
}
```


### [2026-09-04T19:00:27.965Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:00:29.520Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i in range(272,290):\n    L=leaves[i]\n    print('--- leaf',i, 'has آهن' , 'آهن' in L)\nEOF"
}
```


### [2026-09-04T19:00:31.240Z] TOOL RESULT

```
777
--- leaf 272 has آهن False
--- leaf 273 has آهن False
--- leaf 274 has آهن False
--- leaf 275 has آهن True
--- leaf 276 has آهن False
--- leaf 277 has آهن False
--- leaf 278 has آهن False
--- leaf 279 has آهن True
--- leaf 280 has آهن True
--- leaf 281 has آهن True
--- leaf 282 has آهن False
--- leaf 283 has آهن False
--- leaf 284 has آهن True
--- leaf 285 has آهن False
--- leaf 286 has آهن False
--- leaf 287 has آهن False
--- leaf 288 has آهن False
--- leaf 289 has آهن False
```


## [2026-09-04T19:00:33.694Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (279,280,281):\n    print('===== leaf',i,'=====')\n    print(leaves[i][:2500])\nEOF"
}
```


### [2026-09-04T19:00:35.460Z] TOOL RESULT

```
===== leaf 279 =====
اه
۲ هنیا به (۱) - با بای ابجد و نون
و بای حطی وبای بيكك قطةٌ تحتانی بر وزن ۷ -
ات ادن بعتی جاااهوی امه که زوا از
گویند و مربی «تاب» خوانشد .
7 42 - بر وزن نافثه » بععنی آازیده
است که مطلن کشیده باشد اعم از قد کشیده و
شمشیر کنیده و امثال آن ٩‏ - و هارتهای
| هتخت ۲ - بکر ثالث و سکون خای
خن و ای افرشت » یمنی ب رکشید و بر آورد .
]خن ۴ » بروزن دانستن . بمعنی
" کشیدن باشد ۰طلقا اعم از هد کشیدن و شمشبر
از غلاف کشدن - و دست از چیزی کشیدن
و امتال انها ۴ .
باشد مطلقا ؟ .
]هر اهی * - با رای فرشت بر وزن
(۱) چب . چش : آحبیا ۱
رهنمای بیکیهاست .
آ هرمن * - بتتح رای قرئت و میم
بروزن لاف زدن» سمعنی و امن است کمرهنمای
بدیها باشد و بسکون رای فرشت حم کفته اند
که‌بروزنوا کردن باشه۷ . وبسن یکوینهآهرمن
شیطان است چنانکه (۲) بزدان فرشته است و
بضی گویند بزدان دم خداتمای کته آهرمن
نم‌شیطان و این اصح است : وتوبة مسگوشد
که خلی تمه علمت او ارنگی و بهع رسای
شر وفتنه و فاد اوست .
] هرن * - بر وزن باد زن » بععنی
آهرمن است که شبطان باشد .*
]هریهن * - بک رایع و قح میم .
بر وزن ماه ددن بمعنی آهرن است که شیطان
و رهنمای بدیها باشد .
هر یمه * فتح‌هيم » » بمعن ی آهردمن
ست که شیطان و رهنمای بدبها باشد ,3
همند ۸ - بنتح میم و سکون تون
۴ - مرکب از:2 (ییشوند) +-
و آهنجیدن «فاب. ۱ : ۸٩‏ ۶ :
زآهختن نیخ‌ها ازغلاف
وت 2
٩‏ خجسته بی دنام او زردهشت
۲ - رك : بزدان.
کناهکار » عاسی :
۱ چوجنی کسی با کس یکفتگوی
ز پولاد سندائی اننر شتاب
کفش سوختیگربدی آهمند
۴ ره : آهختن. رگ : اهر هررمین-
که آهرمن بدکنش‌را بکشت
دققی ۶ مزدسنا ۱۵۷: ۰۱۷۲ ۱۷۵ *.
ججیزی که سو کند بودی در اوی
کندی » ستی .آهسته کاری فونگف:
شه در صفحةٌ ۷۰
===== leaf 280 =====
ودال ابجد ,کی را گویند که دروغ وید 6
هودم را فریپ دهد ۷ .
آ هی ؟ س بفتح اك و سکون نون »
ممروفست.- وشمشیر و تیغ را نیز آهن گویند .
بمعنی ب رکشیدن باشد مطلفا - و اهر بکشیدن‌هم
را یز گون که فاعل نوشیدن وکشیدن وانداختن
باشد ۴ - وبمعنی عزم واراده - ونضت وابدا-
و انداژهم آمده است .
از مرد سخت جان و سخلی کش نی محنت
کش باشد . ۱
] هنجد ؟ - بنتح جیم و سکون دال
۲ - آدرخش صاعقه » بدی 7
اه
ایجد , یشی یکشد - و ینداژد .
آهنچه - بتج جم ۰ پپناکش
جولاهگانرا گوبند , و آن چوبی است که طول
آن موافق عرش جامه ایست که می بافند و بر
هردو سرآن آهنی صب کرده اند » و آنرا هد
وقت بافند کی بردو کناوجامه بند کنند - وبعنی
گوند رسمانی باشد که جولاهگان در آخرکار
پندند و در سقف خانه بند کنند » و باجیم فارسی
هم کفته اند .
ا هی چخت - بض جیم و سکون 8
تای فرشت . آهنی باشد که زمین را بدان‌شیار
گت .
آ هنحیدن * - بر وزن واگردیدن,
بعمنی توشیدن- و کشیدن باشد. ویمعنی انداختن
هم آمده است ۷ .
آهمندآن دروشگو ظریب . « لت نامه » .
ایا 2515 < دهارله ۱۸۸ > و8268 « تیب که ٩-۱۳۵‏ > اورامانی 25260 «2. اورامان ۱۲۰»
سمتانی 5110 ۰ منکری 21180 , سرخ 8987 , لاسگردی 888 , شهمیرزادی 8580
٩۱۸۱-۷۲. 3‏ * .کلکی 2010 م فریزندی ویرنی » ۵180 , نطنزی 2008 , دك .ص۷۸۵»:
ی دا و ار کف رت
خلقانی «لفت نامد».
۴ - درلمات مرکب : آب‌آهنج » جان آهنج . دم‌آهنج , دودآخنج , گوشتآهنج »
معده آهنج بممنی آهنجنده یمنی بر آورنده , ب رکننده » یرون کنندم و پر کشنده است . رف :
دلت‌نامه ۰ ۴ رك : آهنجیدن. ۵ بهلوی ات2202 « منای ۹٩٩۵‏ * , فذارسی
آهنگه , آهنگیدن » هنجیدن , آهیختن همربثه‌اند . از رسةٌ اوستائی 1308) بمعن ی کشیدن
« بارنولمه ۷۸4 > « تب رکه ۷۰ ذیل ۲۵۳2908) >. ۱ - بر آهنجدن نژ بمحنی
بآوردن » جدا کردن : « پیدا شد که صورت معروف کنند؛ هیولی است ازمجهولی او » ومادت
مطلق اندر وهم آینده نیست مگ رکه نفس یاری عقل ازنخست مراورا بمیانجی سورت ثابت کند:
آنگاه مرصورت را بوهم ازاو برآهنجد وعجپولی ثابت کندش بی آن صورت . » « زاد المسافرین
۷۳-۲ »- نز آهیختن » سل - جذب کردن ؛ و درآ هنجیدن » در کشیدن چنانکه گوشت را به
سیخ « لت نامه * .
بقبه از صفحةٌ ٩٩‏
تأنی : تهور و نیزی کرد و پیش آن لشکر بازشد و هرچه محمد. بن هززن آهستکی فرمود تعجبل
کود . « تارخ سیستان > دفق ۰ حلایمت » مدارا - سکیته » رزات - حلم ؛ بردباری .
آهته -آرم» بی‌شرور - با رفق ومدارا- ترم -آرام - باسکینه . « لفت‌نامه » راد : آهستگی.
===== leaf 281 =====
: آهنخای - باخای هطه دار بر ون
پا برجلی ء کنابه از اسب سرشخ یر زور باشد .
آ هن .دبا - بن رای فرشت » سنگی
کویند چون آب سیر و لعاب دهان ناشتا وخون
کوسفند ماده را بر آن بمالند جابه اش برطرف
شود .
هر گ ‌ بفتح‌رای‌بی نقطه دسکون
کاف فارسی . کنایه از اسب صاحب فوت ویرزود
باشد .
هن سرد کوفتن یکس نون
کنایه از کاری و اراده ای که تتیجه سداشته باشد
و بفعل تباید -
"هی ۱
ساز و آواز باشد ۴ -. و آوازی که در اول
اراده - و توجه - و عزم ‏ و شتاب و تعجیل
را یز گویند - و بمعتی خسید گی طاق ابوان و
امثال آن باشد که باسطلاح بنابان لنکه گونند
سوکنار صفحه وحوض وامثال آن راهم کفته‌انس_
و بمعنی طرز و روش - و قاعده وقانون هم‌آمده "
است - و صفت مردمان وجانوران را نیز کوینه
و ماضی کشیدن باشد بعنی کشید ۴ - و طوبلمو
گفته اید وحرهی «ازح» خوانند وق سقلپوسکان
آ هن گاو- باکاف فارسی بالف کنیده
و بواو زده » بمعنی آهن جفت است , و آن
آهنی باشد که بدان زمین را شبا رکنند . #
آ هفگیدن - مسدر آهنکه است که
بمعنی کشبدن بود مطلفاء خواء آواز باشد وخواه
نیغ و شمشیر و خواء صف عردمان و جانوران
وامثال آنها - و قصدکردن واراده نمودن را نیز
گویند 44
]هذین جان - بممنیآهن جان ات
که کنابه از مردم جفا کش وسختی بین ومخت
اس که کنابه از مردم سخت جان باشد -
وهردم دلاورو بهادر را ق ]هنن شک مگ شق:
آهنین د گه « بنج رای قرئت
وکاف فارسی» اسپ پر زور وصاحب قوت و دلاور
باشد .
آهنین لرسی - بت کان, کنایماز
مندان آهنگری و مسگری و ز رکری باشد .
]هو بر وزن کاهو . جالورست
۶ مناس ۵ ۰ بر : هنگه و آهنجیدن .
۴ ره : لمت‌نامه .
ی ۱۸۶ > .
« لفت‌یامه » :
خر ۰
آهنگری - شفل وعمل آهنگره رگ
```


## [2026-09-04T19:00:47.321Z] TOOL CALL #40: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:70 --image 2>&1 | tail -60"
}
```


### [2026-09-04T19:00:49.089Z] TOOL RESULT

```
no scan of BQT covers printed page 70 (see 'scans' in refs_online.json)
```


## [2026-09-04T19:01:04.945Z] TOOL CALL #41: Bash

```json
{
 "command": "sed -n 1,60p tools/ref_page.py"
}
```


### [2026-09-04T19:01:04.998Z] TOOL RESULT

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


## [2026-09-04T19:01:11.464Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o bqt70.jpg \"https://archive.org/download/borhan-ghate-v1/page/n280_w1600.jpg\" && file bqt70.jpg && ls -la bqt70.jpg"
}
```


### [2026-09-04T19:01:14.623Z] TOOL RESULT

```
bqt70.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
-rw-rw-r-- 1 sfmqrb sfmqrb 532833 Sep  4 15:01 bqt70.jpg
```


## [2026-09-04T19:01:17.901Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt70.jpg')\nw,h=im.size\nprint(w,h)\n# bottom third = footnotes\nim.crop((0,int(h*0.60),w,h)).resize((int(w*0.75),int(h*0.40*0.75))).save('bqt70_bottom.png')\nim.crop((0,0,w,int(h*0.35))).resize((int(w*0.75),int(h*0.35*0.75))).save('bqt70_top.png')\n\""
}
```


### [2026-09-04T19:01:20.421Z] TOOL RESULT

```
2479 3508
```


## [2026-09-04T19:01:22.174Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt70_bottom.png"
}
```


### [2026-09-04T19:01:22.199Z] TOOL RESULT

```

```


## [2026-09-04T19:01:32.292Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt70.jpg'); w,h=im.size\nim.crop((0,int(h*0.42),w,int(h*0.66))).resize((int(w*0.8),int(h*0.24*0.8))).save('bqt70_mid.png')\n\""
}
```


### [2026-09-04T19:01:34.265Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:01:36.650Z] TOOL CALL #46: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt70_mid.png"
}
```


### [2026-09-04T19:01:36.673Z] TOOL RESULT

```

```


## [2026-09-04T19:02:08.420Z] TOOL CALL #47: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/70.vision.txt <<'EOF'\n[BQT vol. 1 (Borhan-e Qate', ed. Mo'in), printed page 70 = archive.org borhan-ghate-v1 leaf n280.\nRead from the page image (https://archive.org/download/borhan-ghate-v1/page/n280_w1600.jpg); OCR of the\nlocal BQT_v1_pages.txt leaf 280 was too poor. Page identified by the running notes\n\"بقیه از صفحهٔ ۶۹\" at the foot of this page and \"بقیه در صفحهٔ ۷۰\" at the foot of the preceding leaf.]\n\nHeadword (col. 2, top of page):\nآهن ـ بفتح الف و سکون نون، معروفست. ـ و شمشیر و تیغ را نیز آهن گویند.\n(\"āhan — with fatḥa on the alif and sukūn on the nūn, [it is] well known [i.e. iron]. — Sword and\nblade are also called āhan.\")\n\nMo'in's etymological footnote no. 2 to آهن (bottom of page 70), verbatim:\n۲ ـ اوستا ـ ayah ، در ترجمه و تفسیر پهلوی âsênên «بارتولمه ۱۵۶»، پهلوی ایضاً asîn «دهارله ۱۸۸»\nو âhên «نیبرگ ۱۳۵ـ۶»، اورامانی âsaen «دك. اورامان ۱۲۰»، سمنانی âsun، سنگسری ahän، سرخهٔ âsân،\nلاسگردی âsân، شهمیرزادی asän «ك. ۲.۱۸۱ـ»، گیلکی âhin، فریزندی و یرنی âhan، نطنزی âhon «دك. ۱. ص۲۸۵».\n\n(= \"Avesta ayah; in the Pahlavi translation and commentary āsēnēn [Bartholomae 156]; Pahlavi likewise\nasīn [Dhalla 188] and āhēn [Nyberg 135-6]; Awromani āsaen; Semnani āsun, Sangesari ahän, Sorkhaʾi āsân,\nLasgerdi āsân, Shahmirzadi asän, Gilaki āhin, Farizandi and Yarani āhan, Natanzi āhon.\")\n\nFootnote 5 on the same page, to آهنجیدن (a different word, \"to pull\"):\n۵ ـ پهلوی âhanzhitan «مناى ۲۶۵»، فارسی آهنگ، آهنگیدن، هنجیدن، آهیختن هم‌ریشه‌اند. از ریشهٔ اوستائی\nthang بمعنی کشیدن «بارتولمه ۷۸۴»، «نیبرگ ۷۰ ذیل frahang».\nEOF\necho saved"
}
```


## [2026-09-04T19:02:08.745Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ayah\\|ayaŋh\\|ayanh\" BRT.txt | head -20"
}
```


### [2026-09-04T19:02:09.893Z] TOOL RESULT

```
saved
```


### [2026-09-04T19:02:09.939Z] TOOL RESULT

```
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
3092:•  g-  ag»nyä-  f.  'melke  Kuh,  Milchkuh': apas&l  vä  agt}c3  vä  mätprqicä  vä  'jrä *drfguäayanh6  vTspBpaitli  avaoÜ'amS  "und euch,  Wasser,  rufen  wir  an  als  die  träch- tigen und  die  Mutter-  und  die  melken Kühe,  die  fiir  den  Armen  sorgen,  die  all- tränkenden"   ^.38.$.
4128:•  j.  a-nhaiSya-  Adj.  'unlauter':  °^lm frafravayahi  tUm  yS  ahurS  maxdä  .  .  aoi zrayS  püitihm  "schwemmst  du  ,  .,  was unlauter  ist,  fort  . .  zum  See  .^.i^' V. 5. 76;
4277:•  j.  an-aiwi.^ratvö.gätav-  Adj.  'der keinen  bestimmt  angewiesenen,  festen  Platz hat':  "'tu'''  (NDm.)  aita  äb^rtta  ^sraosa- vanza**  vlcarayahin  "ohne  festen  Platz sind  die  beiden:  der  Ab.  und  der  Sr.;  sie gehen  auf  und  ab"  N.  717.
4585:•  j,  +antar«.ar98am ''  Adv,  ('zwischen  den Seiten',  sva.)  1) 'innerhalb',  mit  Gen.:  °äjw zrayanhB  V.5.19;  —  ''(am  nmänahe  "V-ff. 33,  Yt./7.6o.  2)  'diesseits':  yas;/  iava masda  kirpnaot  tacar)  *nSit  *tacar>  *'Mm'^ upairi  Avanxsaiüm  "dass  dir  M.  eine Bahn  bereite,  nicht  eine  Bahn  diesseits, (sondern)  Über  dem  Sonnenball"  YL  5, 90.
4698:\)amm  Y.$4.2,  G,  j.6; — yä  {ar?ävi) 'vaiti fratalaili  Y.  Ö5. 3 ;  Yt.  5. 1 5 ;  —  a^tn  vatau- hlm  .  .  hrpsailTm  'vattTm  Y.  3. 14;  Yt /J. I,  7;  —  drvaspqm  . .  'vaitlm  YL9.2;  — fravaiayö  .  .  yä  'vaifli  Yt  13.  29;  —  at töi  atrjm  . .  *asXsttin  'vanhm  Y.j^4;  — tiiirim  .  .  'vant?m  YtÄ4;  —  vatianttm 'vant»m  Yt  21.  i;  —  °vatS  amai  'vatÖ virp^raynäi  'vat^yO.  »rütyi  'vai'iya aiöii  'vai^ya  astdil  'vaüyä  paurvatälo 'vai'i'yB  uparatälö  'va^byä  yazatoAbyö  Vr. g.i,.  b)  sonst;  uströ . ,  b)r?zB  "vä  Yt i.^.  1 2 ;  —  srlra  urusta  'vaiti  (VSf.)  .  . UfTaireY.it^.iB,Vyt22; — srayarfhö  vouru- ka?ahe  'vatö  Yt.<S.46;  —  vasnm..  zaröil ayanhö  frahixt»m  'vatö  \L  10.96;  —  'vat iimäfum  Y.  57. 10;  —  ptiüm . .  yim  aiwatö 'vantim  Vyt.^;  —  'vaitlm  sitiqin  dävöi (sd.)  dr»gvasa  Y.  44. 14.  —  IstJm  . .  pouru.- sarioam  'vaitlm  Y.  65. 1 1 ;  —  hazö  "vat  Y. jj^.  iz;  —  yahmi  maza  'va  (NSn.l')J' '  iiiäälpm  Yt  10. 64  (?) ;  —  *°vata  vaca  F.3  e. AbleiL  —  ai.  dmm-ant-  Adj.;  vgl.  mp.  (PS.) amäz-nnd.  —  ')  %  jg4.  —  •)  Zur  Zusammen- Stellung  von  amai'aaf-  mit  ^'/ri^ravan ,  viri- %rasan-  s.  'amn-  2.-3)  Wenn  richtig,  wohl Neubildung  lum  NSm.  'va  nach  der  n-Dekt.
4714:SuperL  aus  'voni-,  statt  anu'varslUv'  g«sclir., S  aö*.   12,    17.    —    VgL    anu.-.ar}layah'<i.    — >>  Die  Lesung  Ist  nicht  gani  sicher. 'öt:  E
4867:ayanho-zasta-
4868:•  j.  ayanhö.zasta-  Adj.  'mit  nietallenen (eisernen)  Klauen';  varäzahe  ('eines Ebers'; ayüahs^äiahe  'saslahe  Yt.  ro.  70.
4909:•  j.,  g.ayah-n. 'Metall (Eisen)':  asmansm..
5771:—  yai  nsit  sün}  .  .  a3atf/iqm  °tqm  .  . bannhm  (sA.) /rafasqn  V,  6.46;  —  'ti'a (AP.)  gaonaca  *dmi}'iaca  Ytij.  11;  —  yS süne  .  .  'tanqm'-''  (als  Obj.)  ahmarslanqm da',aiti  . .  yaica  alle  'ti  (NP.)  dälshva arSnte  V./3.3f.;  —  "tfin  .  .  *maslrr/nqm F,_y  c ;  —  ayanhaHiäis  kantlU  asdibls  paili
5886:•  j.  aspya-payah-  n.  'Pferdemilch':  dakmd huram  (sd.)  :i^araili  maoB  *°ya»Al>'^  N._J0.
6254:—  syao%ami  razistä  (sd.)  ängvataicä kyai<ä  *'iaotii  yehyäiä  ASmunylsaitl  (sd.) mi^aAyä  yucä  ksi  är»svä  Y.  _jj.  i ;  —  yS vü  xsayqs  adqs  drTtä  ayanhm  urvatsis (sd.)  Vit  huiSntul .  .  ra/nä  jvqs  yS  'savä dr3gvant)m  Y.  46.  5.  a)  Ko-i  it  von Zara^ustra  (s.  2  c  a  und  drTgvaiit- 1  2  a  a) : y!  äyal  •iavanam  divamnsm  (sd.)  hsi  . . *dusji^arä^Sm  (sd.)  . .  ISm  *vi  ahSm  dr>g- vants..dams  «a<tf«/(sd.)  Y.^7.20.  b)  im jAw.:  kat  *sava . .  vanai drvantami  'idva vanat  drußm  °sava  vanat  drvantpm  Yt. I.2S;  —  x^ayamnam  '/avanim  däyata *axsyamn^m  drvant^m  Y.  Ä  5  ;  —  vasB.- x/a'iirB  kyüi  'sava  avasS.xia'^rS  hyäf  drvä Y.S.6;  —  yqm  'lara  ..  asayqm  (sd.) va^  tarn  drva  ^ihva  Vr.  22.2;  —  mt^nm ms  janyh  mä  yim  drvatat  pimanke  mU yim  n^adafnat  'iaoiiat  uvayä  af  asti  (sd.) mskrB  drvataica  'saonai^a  Yt/o.  2;  — pdhqm  %rvB.däianqm  jasaiti  yasla  drvaile yas^a  '/aofieV.  lff.$o;  — yai  azäite^sd.) tsm  ahum  pai'iyaite  yim  "soonam  yesi  nHii azUiie  tun  aAam  pai^yäite  yim  drvatqm V.  /Ä76;  —  drvatqm  ..  urvänS ..'läunqm V.  ig.  30;  —  ga>il  nmätiam  ^mr^yS  asti '/SvaoyB  (DP.)  naSai  drvatqm  Yt,7.4;  — hiiia  para  'saonqm  pa^a  urva/ai/i  iu^a drvatqm  Yt4.4;  —  narqm  vä  'saonqm kanjamanäis  drvatqm  vä  . .  kandvaranäü YLi/,4; — yai  •i'ava  para.iriiyeiä  . . yal drvä  ava.*miryeie  H.2.1  — 19;  7,  8,  10, 15*,  16',  18  {'iaonyäi);  s.  unter  drvatif- 1 1.  2)  sonst,  a)  im  gAwr.  (ausser GHapt):  zara'^usträ  kastl  'lavä  urva^S mazsi  magäi  (sd.)  Y,  46. 14;  —  tSm  (näml. pounicistqm)  . ,  varänl  (sd.)  .  .  yä  försi vTdäl  paüyaFcä  västryaHbyo  (sd.) . .  *°iapnj 'iavabyS  Y.  5J.4;  —  hvs . .  yas^a  vadarS (sd.)  vBizdal  'iauni  Y.^a.io.        a)  spez.
6392:•aäan  jam  Y.Q.  %-!.■,  lO.S,  61.4;  — \ 'siütJ  (GS.).  ji7  as'^/m  siaeiti  ..  "wer  ver- '•yahe'^  ayahe  anai'acnS  V.  JÄ  j  i,  1 2 ;  — '  mag  mittelst  eines  einzigen  Spruchs  alles . . luayanam ..'yaonam  anasaonam  Yt./^.ios.   zu  verkünden?  .  .  Der  ^/abeter.  Wer  das
7153:feuer***':  yqm  xsnBtftn  ränsibyä  (sd.)  da "^wä  ''ira  suxrä  mazdä  ayanhä  xiustä Y.5/.9;  31.3;  —  (a  da  spmta  mainyü ,  ■  '"^ra  vaahäu  vldäitim  (sd.)  ränStiyä  V. 47-  6j  3^-  '9;  —  ahurä  . .  yä  da  airs  (sd.) .  .  %wahya  garima  '%rS  asa.aojaah3  Y. 4J.4;  —  aitSi  'irSm  ahurä  aojSnhvanttm (sd.)  asä  usSmahl  .  .  siöi  rapantl  ci%ra.- avaahim  al  .  .  daibisyant!  .  .  dir^stä.- agnanh)m  Y.34'4-
9279:•  j.  'karata-  m.  'Messer':  ayanhalnäi^ °tsis  azdibti  paiti  ava-ksrii^yät  (sd.)  V. 4-50-  a)  insbes.  als  Waffe,  'Dolch- messer, Dolch':  yallam  zeyanqm  rdiniM ,  .  bityd  'IS  N.!4.(};  ~—  'ts  hufranliar$t5 Yt.  i^.  7  2 ;  —  HaBt  (NP.)  alsqm  hufrayuxta Yt.  10. 40 ;  —  iSavS ..'ta  ..  vazra  Yt. /. 1 8 ; —  'hm  iaranyS.saor^m  /rapixstfm  vTspi,-
9545:•  j.,  g.  kahrp-,  ksr?/-^'^  f.,  n.'>  'das  sieht- ' bare  Äussere  jedes  Wesens  und  Dings, , äussere  Erscheinung,  sichtbare  Gestalt': sraliiqm  at  tSt  'p/m  (AS.)  -^pam  (GP.)  j ävaedayamakl  tnazdä  ahurä  iinä  raota  . . avat  y.ll  hvarS  aväcT  Y._J(*'.  6;  — para avtiiriAe  hü  "^warstö  (sd.)  'pya  (LS.)  Y. ' /p.  8;  —  asmamm  ,  ,  y3  hislaite  ayanhs 'pa  (IS.)  x^amahe  (sd.)  ".  .  mit  der  Er- scheinung von.,  (sva. ..  anzusehen  wie..)'' YL  13.  2.  A)  insbes.  von  lebenden Wesen;  auch  vom  gestalteten  Stoff  selbst 'Leib,  Körper';  i )  von  Menschen  und Göttern:  aj  'psm  (GP.)  utayuitil  dadat ärmaitis  qnmä  (sd.)  Y.jo.  7;  — ■  yd>!a varsnahe  'palie^^  dsus  (sd.)  N.  7o(7;  — paiti  ainii  .  .  'p^m  .  .  gaia/ie  .  .  °ppm  .  . säJiar/  .  .  "Pim  .  .  abmatr/aAe  .  .  'P^m ..jahikayüi  ..  -p.m  Y.//.  30-32;  32;  — avqm  'P^m  yazamaide .  -yqtn . .  k^r^säspahe Yt /?.  61;  Az._J;  —  üjasat . .  viriisra-fitä ..vätahe  'pa  (IS.)  Vt/4-2;  —  mi%nm..
10867:•  j-,  g.  xäusta-  Adj.  'Üüssig*,  spcz.  'brei- flüssig'; a)  vom  Lehm,  sva.  'aufgeweicht': yäiia  nü  ma/yska  *xsvisti  (LS.)  '>  zjtiiS (sd.)  vfsä2'ayänti  V,  3.  3i'>,  b)  vom Metall  (Eisen),  sva.  'geschmolzen',  mit ayah-  n.  Bezeichnung  des  glühenden  Me- tallstroms beim  letzten  Gericht^*:  yqrn xstiütim  rSf\Sibyä  (sd.)  dh  ^!ci,l  iJ^rJ suxrä  .  .  aya»Ää  °tä  Y.  j/,  9;  —  *'lpm^''
12385:knüpfung einer  nominalen  Ergänzung  an dn  vorausgehendes  Substantiv;  l)*J  im Nominativ  (oder  dem  ihm  gleichen  Akku- sativ): yaunä  (sd.)  'yaiy  ''uikakyä  uta 'yaiy  *drayahyä  D.  5.  2 ;  —  sakä  (sd.) 'yaiy  ^tara'drayt^  D.  6.  3;  —  dahyäv<r 'yä  *paruvaiy  ü.ß.z;  —  xsa%''am  'ya* babirauv  Bh.  i.  16;  —  x/a'^'am  .  .  ya^ *vaiariam  'y<^  ''uvaspam  D.  77. vasiy    'ya^    naibam    X.  7.  3.  l)    in
12438:nim  Vr.  7.  3 ;  Yt  2.  i  a,  Vyt  i4-  a)  äai^ nayä  (näml.  ayah)  heisst  der  24.  Monats- tag; °nayä  vavhuyJ  mazdayasnUi^S.i.n; vgL  2. 24,  Y.7(».6.  a)  GS.  mit  a^OTOna- m.  Name  cioer  Gottheit:  äat  hl  (näml. mi^raie)  Aävlfya  ar^e  vasatte  .  .  'nayä mäzdayamSiS  upamaram  (statt  NS.;  Sp. 391  u.)  Yt/0.  ia6.
```


## [2026-09-04T19:02:14.785Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4905,4915p' BRT.txt"
}
```


### [2026-09-04T19:02:14.837Z] TOOL RESULT

```
•  j.  a-yaz9mna-  Adj.  'nicht  betend':  y^ saSte  haurvqm  tarüsca  xsapamm  °«5| ". .  ohne  zu'beten"  V.JÄs;—  mitAkk. 'zu  -':  yüi  °na  am>Ss  sp>nl!"ä\t  nicht  zu den  ASp.  beten"  Vyt  12.
Pü. :  ayastär  (so !,  falsch  H  auo  SBayrAW.  rS72.
•  j.  aya^äna-  n.  Name  eines  landwirt- schaftlichen, anscheinend  beim  Pflügen notwendigen  Geräts:  yaiSatn  zayanqm vastryehe  ßiiyantS  .  .  'iJna  (NP.)  paiti.- dar>zäna  (sd.)  V.  i4- 10.
Et.?  ä  =  ar.  /(i)  oder  jl(*).  —  Pü.;  ^at'a m  dan  i  k.
•  j.,  g.ayah-n. 'Metall (Eisen)':  asmansm..
yS  histaite  . .  'yar)ks  fohrpa  ifaSnake  (sd.) ^t-y-3>  —  vazr»m  ..  zardi/ (sd.)  °yat»ks\ frahioctsm  Yt.  10.  96;  —  /rat3rasy3n?m .  .  *pairis.:^axt>m  (sd.)  'yat>Aafie'^  Y.  11. 7.  a)  'Gerät  aus  Metall  (Eisen)';  hanhui draos^a  *mmataheea  (sd.)  'yaTjheca  (GS.)" V,  5.38.  a)spez.zumKochen, 'Kessel' i>: aum..yim  upairi  Afr^säspn 'yanha  pitsm paiata  . .  iafsatca  As  mairyU  . .  /ras  (sd.) "yaahB  fraiparat  V.^.ii.  a)  im  gAw. vom  glühenden  Metallstrom  beim  letzten Gericht;  auch  mit  :faSna-  und  xsusta-\^ (sd.):  aeSqm  töi  ä  anhat  ya'i^it  'yattkä adänäii  paouruyB  "so  ,dass  er  bei  deinen Heimzahlungen  durch  das  Metall  vor  ihnen den  Vorzug  haben  wird"  Y.^o.  7«'; — yä JBya  (sd.)  s^nghaiti  .  .  x^aims  'yartha  Y. 32.T,  —  yqm  xsnODm  räneidyä  (sd.)  du ,  .  'yanha  xsiista  Y.5/.9.
KompA.,  E. ;  Ableit  —  ai.  ayas-  n.  —  Pü. ; äsia  ■Ei>en',  (zu  \.  g]:  äsh</n  dek  'eiserner Kessel',  (^u  Y.  //):  <islm»i  'silbern',  (lu  Y.  JO): ojv/  'er  j;eht'.  —  •)  Them.  —  ')  Haplol.  statt "ayaahaiilK'i   Dann  them.,  s.  No.  1.  —  J>  S.  Pii.
—  4)  Zuletzt  »St.  JuSTI  Prj.  8S.  241.
•  j.  a-yä-  Adj.  (auch  fem.)  'hin  gehend,
-laufend',  vom  Wasser:  ana  tä  (näml .i/f)  vaioim  (sd.)  yn  (NSf.)  V.j-S-
PQ.irflr«?/(3S.>
```


## [2026-09-04T19:02:30.196Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ahen ===\"; grep -n \"āhen\\|ähen\\|äsin\\|ahan\" HUB.txt | head -20; echo \"=== ARY latin index ===\"; grep -n -i \"AHAN\\|AHEN\" incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-04T19:02:30.285Z] TOOL RESULT

```
=== HUB ahen ===
253:') Oder besser: ahanjidan (wozu auch paz. dhanzidan *to drag*,
254:ahanzd = phi. ahanjak 'attracting* Shk. 227) gehort zu einer Wurzel hanj
785:ban 'Haus' = ap. vahana- (vgl. skr. vasana- 'Wohnen*,
1069:lauten. Das Wort geht iiber paz. vahana = vahdn
1524:353. Fr. Muller, WZKM. 8, 93 verdachtigt phi. patrahan
1525:'Rock' als kiinstliche Form, halt sich an phi. perahan
1529:trahan (aus *patrahan) echt ist. Von Wichtigkeit ist
1531:KitteF (Rosen, Np. Sprachfiihrer p. 49), pwahan,
1532:plrahan *Hemd' (Sal. Shuk. p. 20, Glossarium p. 76)
1533:weist auf phi. pBrahan = ^pairydnhana-; np. pairdhan
1534:(wie die Afghanen sprechen) auf phi. patrahan.
1744:Np. jahan {JihOn) 'Welt' (afgh. LW. jahan, bal. jihon)
2253:bissstiick des Ziigels ; afgh. LW. dahana fem. *the bit
2942:Farrahanns N. pr. bei Hoffmann, Ausziige p. 72) =
3100:wie kurd. dew *Mund* zu ap. dahan, setzt also ein
4701:sah = sah 'KSnig, vgl. sahansah Fird. 13, 226, sahanSahi
4702:14, 13, sahansahan 37, 45 etc., Ispahan — Ispahan, Sifahan
4776:etc., siehe § 3. Daher auch bUmahan 'Erdbeben aus ^bum-
4777:"tnahan = ap. ^bUmima&ana-.
4989:Ind. 29, 68, Bdh. Gl. 124. Ebenso mit a fur i (i, e): ahan 'Eisen* =
=== ARY latin index ===
2:Pahang Richaye 2
1839:AHAND, HAND
2046:JERN NORWEGIAN) 5}3,3 ASIN, AHEN, HAPAHLAVD 5
2047:UZER (DUTCH) ggacke ‘ASENEN, AHAN.
2529:Id ger iebGoby ZAHIAR, ZAHOR, TRAHAN
4295:SPAHEN ~ (GERMAN) glast AAVESTAN) glues!
4652:BUCK!” 1264-1266 FORSCON, FRAHEN, FRAGA
4661:vVAHATI, VAHANA, VAHAYATI, VAHA- (KURDISH) 63
5216:PATTAR, PADDANI (HITTITE) <2 PAHAN (PAHLAVI) 5 hay
10498:BARNHART: (HAMMER) 463 AHANA GOTHIC) S55
14078:MYKE, MYE ——(NORWOIAN).5}4,5 MAHANT nh ue
15246:OY | (12S Lata!” 6 4) Gens aheny
```


## [2026-09-04T19:02:32.165Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ===\"; grep -n \"aios\\|ayos-\\|ayes-\" IEC.txt | head -10; echo \"=== WLD Bd1 ===\"; grep -n \"aios-\\|ai̯os\\|aios\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"=== WLD eik ===\"; grep -n \"eik-\\|aik-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-04T19:02:32.269Z] TOOL RESULT

```
=== IEC ===
257:agouos, ageuos (?) ‘excessive; intense(ly)' (as suffix "Tur Gk. agauós, agaios (but this may be part of the Lat. gaudeo, gavisus); cf. (?) Lat. -iguus (in amb-, ex-, prod-iguus)
322:aiesnos "of bronze, of ore’. Cf. aios Skt. cf, àayasah; Av. ayáhaeno; Lat. aenus, aeneus; Umb. ahesn- (w. “false? h); OE &ren; OHG erin (G ehern, w. ‘false’ h)
332:aios, -es- “metal, bronze, ore. WP I, 4 Skt. áyas; Av. ayáh-; Lat. aes; Umb. ahes- (w. ‘false h); Go. aiz; ON eir; MHG er. (Note: J. Pokorny and others refer this word to Alasia (Ayasia), an ancient name of Cyprus)
735:artaios, see arotàios
1063:. Phryg. cf. bagaios ‘Zeus’; Gk. éphagon (aor.
3869:Li. gagü, eti. Cf. *gagaio in Blg. gagam; Latv. gagaju, id. gagos (gaglis) ‘knob, lump, berry’; as adj. *lumpish, boorish’ Alb. gogël “berry, oakapple'; gogé ‘boorish’; Sw. koka (&clod'. Ambig. cf. gogos); Li. gõgas ‘Jump, hump; withers’; Icel. kaekur, m. (' vice. Mod. -æ- for ON -ce-) gāið (1) ‘croak, caw'. WP I, 526. Cf. gauið, gouo Skt. gāyāmi ‘sing’; cf. G kaien ‘prattle’; keien “blub, weep’; OCS gajọ, ati ‘croak, caw’ gāið (2), see gígāmi gàios, à (1) “raucousness, cawing; jay, mag- pie, or other raucous bird’. WP I, 526. Cf. gaio (1) Skt. gayah ‘song’; Arm. čaj, Lat (jay, with induced palatalism); Lat. gaius, gaia “jay, mag- pie; G (short vowel) Kai ‘prattle’; Norw. Sw. Scots kaja, kaie, kae ‘jackdaw’; E caw; R gaj ‘caw’. Cf. Ukr. Zaj-voronok Clark fr. *gēi-); Pol. ga-wron, Cz. ha-vran ‘raven’ gaios, om (2) ‘pace, gait'. Cf. gígàmi, ghàio. WP I, 526 & 677 Skt. gayah, adj. ‘striding’; Av. gàyom ('pace', also 'yard-measure)); (ambig.) Cz. hej-no, OCz. hajno ‘flock’; (ambig.) cf. Li. góju, son ‘amble, wade’; Latv. (ambig.) gāju Cl went, but Arm. gaci, id. is fr. ghai-, q.v.); cf. also gājums ‘gait, track’; gājējs ‘pedestrian’ galdāið, galdeio ‘bawl, exuit, howl’. Skt. gardāmi, Av. garəd- (1); Alb. (denom.) galdoj ‘exult’; Lat. gallo, are (‘rave���, but poss. denom. of gallus, cf. gagol-); MHG kalzen, kelzen *bawl'; kelz “loud talk’; OFris. kaltia “talk”; Du. kouten chat": kout, s. id.; R. cf. galdét ('brawl', but the phonol. is irregular) galið *shout'. Cf. gald-, galu- Gk. cf. a-gállo ‘glorify’; MHG kallen ‘shout, chatter, sing, croak’; Du. G kallen ‘chatter’; LG kohlen, id.; Tirol. kallen ‘bellow, rut; OE ceallian: ON kalla (“calP', etc.). Cf. also Alb. galé ‘rook’; Br. gal-dü “black sea-bird"; OE -calla *-crier'. (Ambig. or variant in Skt. járe, Av. jar- ‘creak, rustle; call’, cf. &el-) galuó ‘call’. Cf. galið, gald-; galuos, s. Skt. cf. garvah ‘pride’; Br. galv ‘appeal’; W galw ‘call, vocation’; Ir. (?) gailbh ‘squall’;
4556:ghaiios (ghaios) (?) *vigorous, lively, solid, firm. (The evidence is ambig.,, cf. WP I, 528 & 670). Cf. guoiio Gk. khaios ‘staunch, genuine’ (but a-gaios is *elegant); Br. gaé, adj. (gay. LW in Fr. gai); OCz. hojiti sé, v. *multiply', cf. Cz. hojný 'abundant'; Li. gajüs ‘sprightly’. (LG gau ‘dashing, gay’ is from a type *ghau-, cf. Norw. göy ‘fun’. Li. gaivüs ‘lively’ repre- sents *guoiu- apparently, but is entirely ambig. Gaulish gaeso- fstalwart may equate w. Br. gaé ‘gay’) |
4557:ghaisos ‘lance, pole’. WP I, 528 Av. cf. gaesus ‘lancer’; Gk. khaios *shepherd's crook’; Hes. gaiós (Thrac. or Maced. (?) «lance, pole); Celt. LW in Gk. gaisos ‘javelin’; Olr. gaí, gáe, Ir. gai, gaoi ‘spear’; Gallo-Lat. gae- sum; Br. goaó, goaf, gwat; Cor. gew; W gwaew lance, javelin’, w. induced labialism; OHG gër, MHG geér(e); OE gàr; Du. geer “bias, crosscut, gore’; ON geirr ‘spear’, geiri ‘gore, gusset
5100:guag- (1) ‘fluctuate, flag, flounder, waver’. (The evidence is ambig. cf. uag-) Lat. (ambig.) vagus ‘roving, random, un- steady’; vagārī ‘wander, waver, fluctuate’; Hes. bagaios “empty, idle, vain’; OE cwacian ‘wag, shake’: E quake; Li. cf. gõglinti ‘moon around, gawp'; fr. *guag- (?) but cf. also gožiù, góZti ‘rampage, run wild”, fr. *gua$-?, beside (ex- pressive) gvagZdü, -eti “pine away, fail
6159:8huuo (1) *pour, shed, cast, scatter, destroy'. Form of gheu-, q. v. Gk. cf. khúto “was poured'; khümenos, pt.; cf. khudaios ‘poured; vulgar; Li. Züvu, Son ‘perish’
=== WLD Bd1 ===
431:aios- ..Metall" u. zw. wohl (trotz Hirt Idg. 6S5) ..Kupfer (..brandfarbig 11 ?), 
441:292 f. ist idg. aios alte Entlehnung aus AVas(ja ), dem alten Is amen von 
462:Aber Pokorny KZ. 46, 292 wendet das i des kelt. isarnon ein ( *aios 
1398:anas (Theokrit.), ana (Alkaios) „Freund, Geiiebter‘ ! (ibd. 2 )); lat. aceo, 
2057:Lebens); Entscheidungspunkt“ (ay./ugv Adv., axpaios, dy./udCco ), schwed. 
2943:fiihrt Meillet Et. 155 f. auf gen.-ablativisches *aios zuriick (ob = ai. atah 
7234:Ai. udliar (und udhas), gen. wlhndh „Euter“; gr. ol-Oao, -aios (a = ->j) 
23062:cud), xolXog „hohl" (xofdog vgl. xoviXai, d. i. xofdai Alkaios; = alb. dels), 
24767:Xov Alkaios) „abgekratzte Wollflocken; Kissen 11 (die Auffassung von xvacp- 
33222:gewesen seien, iiberzeugt nicht (vgl. auch Prellw. 2 u. fiaios). Unter dieser 
=== WLD eik ===
619:aiq«o- — aik-, 1k- 
669:aik-, Ik- „Spie£S; mit einer spitzen Waffe verwunden, treffen". 
676:einigung mit aik- (so durch J. Schmidt Voc. I 76, Bezzenberger GGa. 1874, 1236, Traut- 
683:aik-, ik- — aig- 
687:gr. ar/ut'i ..SpieB" (*aik-sma 1 )), apr. mjsmis . BratspieB", lit . iesmas, jie&nas 
707:aik-, ib- „anrufen, bittend anrufen“. 
713:(die aber vielmehr zu *seik- „die Hand ausstrecken“ gehoren, vgl. nach 
715:„ein erwiinschter, giinstiger Wind ;< (das aber besser zum selben *seik-, gr. 
806:*) Briickuers Ankniipfung der si. Worte an igla, jegla, jagla .NadeP (s. unter aik- 
893:anord. ikorne (tk- alter Ablaut oder Sehwachung aus aik- im Nebenton?),
```


## [2026-09-04T19:02:42.106Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD aios ===\"; sed -n '425,470p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== HUB 4989 ===\"; sed -n '4980,4995p' HUB.txt"
}
```


### [2026-09-04T19:02:42.168Z] TOOL RESULT

```
=== WLD aios ===
.ijos- — ai-dk- 


anderen Zusanunenhang ; daB auch uter zu ai- gehore, als ai-, ist mir hochst 
fraglich. Aber vgl. Buga, Lietuviu kalbos zodynas S. 27. 

aios- ..Metall" u. zw. wohl (trotz Hirt Idg. 6S5) ..Kupfer (..brandfarbig 11 ?), 
Bronze": im Arischen auch ..Eisen". 

Ai. ayas- n. av. ayanh- n. ..Metall, Eisen": 

lat. aes. g. aeris; got. aiz (urg. a(j)iz- = idg. ajes-) .Erz, Geld ", ahd. cr 
,.Erz ; , anord. eir n. , Erz, Kupfer \ 

Davon av. ciyahhaena- ..metallen, eisern ", lat. acnus ( *aies-no - ), aeneus, 
ags. aren, as. ahd. mhd. erin, nhd. eren ( ehern ). Each Pokorny IvZ. 46, 
292 f. ist idg. aios alte Entlehnung aus AVas(ja ), dem alten Is amen von 
Kypros. 

Hierher hat man bislier meist den keltischen und germ. Eisennamen 
gestellt: 

kelt. *isarno- in gall. Isarnodori gl. ferrei ostii, gall. Isamus , abrit. Iser- 
ninus (Mannernamen), air. iarnn, kymr. haiarn, acorn, hoern; 

got. eisarn , an. isarn (und jam, jam , aus ir. iarn entlehnt? oder boden- 
stiindig aus *Jrarn , alter *isarn , dissimiliert. wo fur ags. Tren, engl. iron , 
ahd. Iran angefiihrt werden kann? s. Koreen Ark. f. nord. fil. IY 110a, 
Falk-Torp 472 und 1491), ahd. Isarn, tsan , mhd. iser, holl. ijzer. Trotz 
der auf blofies n oder r endigenden Formen wie isan, tser, aus denen man 
auf einen idg. r\n- St. is-0r : is-en- geschlossen hat ( Isarno - hatte dann beide 
Suffixe iibereinander geschichtet), ist von einer einzigen urg. Grundform 
isarna- auszugehen; daS diese aus dem Urkelt. entlehnt sei, ist auch kultur- 
geschichtlich wahrscheinlich, da die Kelten friiher als die Germanen zur 
Kenntnis des Eisens und der Eisenbearbeitung gelangten (s. Schrader Sprvgl. 3 
II 86; weitere Lit. bei Yf. LEWb. 2 s. v. aes). 

Aber Pokorny KZ. 46, 292 wendet das i des kelt. isarnon ein ( *aios 
wiirde eine Tiefstufe is- erwarten lassen); wie Much ZfdA. 42, 164 sucht 
er Yerbindung mit dem kelt. Flufinamen Isara , dem ir. Mannsnamen Isa- 
ros, mit gr. ie.oug „kraftig“, ai. isirah ..kraftig, regsam ", is „Erquickung. 
Kraft ", lat. ira ( *eisa ) „Zorn, Heftigkeit 1 , so daB das Eisen von den Kelten 
als das ..starke, kraftige' 4 Metall bezeichnet ware im Gegensatz zur weiclieren 
Bronze. Das i laBt sich jedoch nicht als kelt.. wohl aber als illyr. Entwick- 
lung von ei- begreifen ; der Eisack erweist ja fur Isarcus i, und dieser 
Name war ja illyrisch; seine Ablautstufe ist die von lat. eira, ira. Die 
=== HUB 4989 ===
= skr. rdman-; hum 'Homapflanze' (vgl. hUm bei Mu-
waffaq p. 268, s. Horn Nr. 1113) = paz. hum Min. Gl.
106, zd. haoma-, Vgl. auch Bum *das byzantinische Reich'
(reimt auf bum Fird. I, 403) =' Poi/nT], lat. Roma, — Ausser-
dem ist altes o z\i U geworden in : samur 'Zobel' = parth.
aifuoo (de Lag. G. A. 71, 226), arm. samoir (= phi. ^samor)
und np. kahUd blau = arm. kapoit *dunkelblau (vgl. Horn
Nr. 842).
») Vgl. pSz. xaim Min. Gl. 124, phi. x{a)8m und tism Gl. and
Ind. 29, 68, Bdh. Gl. 124. Ebenso mit a fur i (i, e): ahan 'Eisen* =
phi. aatn (reap. a«g«) s. oben p. 10; mazldan *8augen, schmecken' s. § 17.
*) Dazu ciguna, can *wie*, zaryun etc.— 143 —
§ 313. Ap. au = phi. o kann (vor A, vor Doppelkon-
sonanten etc.) im Neup. verkurzt werden : guhar = gGhar
'Edelstein* ; sutuh = Bui6h Mefatigatus, torpidus, tristis ; kuh
= koh 'Berg'; anduh = andoh *Kummer : htiS = hds 'Ver-
```


## [2026-09-04T19:02:47.295Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Eisen\" HUB.txt | head -20"
}
```


### [2026-09-04T19:02:47.370Z] TOOL RESULT

```
233:57. Die Etymologie von dhan 'Eisen bleibt dunkel. Fiir
4989:Ind. 29, 68, Bdh. Gl. 124. Ebenso mit a fur i (i, e): ahan 'Eisen* =
7517:auch ahan 'Eisen', kurd. hasin u. s. w. (oben p. 10) ; dha
```


## [2026-09-04T19:02:49.918Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '228,248p' HUB.txt; echo \"=== 7510 ===\"; sed -n '7510,7525p' HUB.txt"
}
```


### [2026-09-04T19:02:49.983Z] TOOL RESULT

```
(KZ. 25, 126) Oder wie np. amextan 'mischen und
ksl. rn^siti mischen (s. oben Nr. 51). Skr. vie *durch
Schwingen oder Worfeln aussondern* gehort ebenso
wenig wie skr. vij *eniporschiessen, zuriickfahren, in
Aufregung geraten* hierher.
57. Die Etymologie von dhan 'Eisen bleibt dunkel. Fiir
das Altpersische ware, nach phi. dstn zu urteilen,
etwa *asaina- anzusetzen, wozu auch bal. asin (fehlt
bei Horn), kurd. hasin {— asina-?) stimmen, wahrend
afgh. osptna^ ospana, osset. dfsdn^), pamirdial. spin^)
ein iran. *aspaina-^ resp. *spaina- voraussetzen ? Dass
phi. spenah (fiir zd. spenta 'heilig') hierher gehore, ist
nicht wahrscheinlich.
58. Die Form dheocta/n *herausziehen' (das Schwert aus
der Scheide) gibt Gazophyl. unter *tirar la spada so-
wie Pizzi Chrest. persane p. 150 mit dem Praesens-
stamm ahez. Ich finde sie bei Fird. I, 19, 39: dhext
er zog ab' (das Fell). Sie wird als alt verbiirgt durch
phi. hext *sie zog' (Wasser aus dem Brunnen) BB. 4,
p. 65. Also war hie die Wurzel und dhanjldan miisste
fiir ahinjidan stehen^) wie avangan der Wb. fiir dvin-
=== 7510 ===
= ap. ^^''Id^at- = zd. d^risatem (oben p. 78) ; panjah *funf-
zig* = ap. *panda9^at', zd. pancasatem, skr. pafidagaf-;
gunah *Sunde* = pfiz. gunah Shk. 247, phi. v(i)nad^ Gl. and
Ind. 24:7 ; padaf rah *Vergeltung, Strafe* = pfiz. pddafrdh
Shk. 261, phi. j^a^a/m^, a,ip.*pdtifra9^a', vgl. zd. paitifrasa-;
tih leer*, HhT = phi. tuhtk, vgl. bal. fusay *ausgehen*, skr.
tucchya-; phi. pah *Vieh* Horn p. 287 = zd. pasu-, Vgl.
auch ahan 'Eisen', kurd. hasin u. s. w. (oben p. 10) ; dha
^Gazelle', bal. dsk u. s. w. (oben p. 11). Ueber kdstan, kd-
ham H. 835 und Mh 'Stroh' s. oben p. 86. Also sollte ap.
vi9^- *Haus, Familie = zd. vis- im Np. *bih (= paz. *i?iA,
phi. *yt^) lauten, wie es lautgesetzlich richtig im Balu5i
durch gis *Hausstand' vertretea ist 2).
Wahrend im Armenischen h == mp. np. h fiir ap. ^ in
dahekan und akah erscheint, liegt s vor in vnas 'Schade,
Verlust, Unrecht, Schuld' (5. Jhd.) gegeniiber paz. np.
```


## [2026-09-04T19:03:03.977Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2035,2060p' incoming/ARY/ARY_latin_index_pages.txt; echo \"=== find pdf page tag ===\"; awk 'NR<=2060 && /\\[pdf page/ {l=$0} END{}' incoming/ARY/ARY_latin_index_pages.txt; grep -n \"\\[pdf page\" incoming/ARY/ARY_latin_index_pages.txt | awk -F: '$1<2060' | tail -3"
}
```


### [2026-09-04T19:03:05.757Z] TOOL RESULT

```
ashy 4 Sy
[pdf page 73]
oes | VE
‘ FIKHO. . * AGREEK) ly NAVESTAN) gles 3|
we VAEG-, NIWIXTA-, A-VAEG
REFERENCES beth . PAHLAVI) 5 shy,
POKORNY, ~~~~S~*«MAOAAIL _AVIXTAN, APIXTAN
ry sguiley AWISHTEL —ARGHAND (24) gli
ey foe Kas SANSKRIT) 2, Scaler
08 etn |
JERN __ (SWEDISH) Sai AYAH, AYO- AVESTAN) gle 3
JERN NORWEGIAN) 5}3,3 ASIN, AHEN, HAPAHLAVD 5
UZER (DUTCH) ggacke ‘ASENEN, AHAN.
IARN HOLD IRISH) oS 543 y) HESIN x(KUORDISH) 52,5
_ISARNON CELTIC) (1S) gl ISTRI ‘AFGHANT) gail
ISARNO HGAULISH) JIE AYAS, SANSKRIT) 4 Sila
HAEARN: (OLD WELSH) opS 553 HIERO GREEK) iti,
HOUARN (BRETON) aoe AES, AIS LATIN) ys
HIERO ASPANISH) lied
‘REFERENCES beth AIZ, EISARN GOTHIC) Sa,
“POKORNY ———~—~=~=«89-300, 1S | © «(OLD SCANDINAVIAN) Sigh!
BARNHART: (RON) 544 TSARN, EIR, JARN
MACKENZIE: 6, (IRON) 120 ISARN HOLD SAXON) of J y-S\s
‘BUCK: 613 . OLD HIGH GERMAN) pS galT
ONIONS: (IRON) 485 TSARN, ER
SKEAT: (IRON) 308 EISEN, ERZ GERMAN) glulT
=== find pdf page tag ===
1979:[pdf page 71]
2009:[pdf page 72]
2036:[pdf page 73]
```


## [2026-09-04T19:03:20.659Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN era ===\"; grep -n \"^era, n\" KLN_1966.txt; echo; echo \"=== SKT era/ore/own ===\"; grep -n \"^era\\.\\|^era,\\|^ore,\\|^own,\\|^owe,\\|^ought,\" SKT.txt | head"
}
```


### [2026-09-04T19:03:20.731Z] TOOL RESULT

```
=== KLN era ===

=== SKT era/ore/own ===
19230:owe,  ccrnclude ;  esp.  used  of  closing  the pa  of  the  public-houses,  at  the  sound  of e  drum.  So  also  G.  zap/enstreiih,  the ttoo,  is  lit  '  tap-slrolce ; '  and  Low  G. """■•*,  the  tatioo,  is  lit.  'tnp-shutting.' (^  tap  is  cognate  with  K.  tap ;  and
```


## [2026-09-04T19:03:22.089Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW aes ===\"; grep -n \"aes,\\? -eris\\|aes  \\|aera\" LEW_1910.txt | head -10; echo \"=== LAT aes ===\"; grep -n \"aes\\b\" LAT.txt | head -10"
}
```


### [2026-09-04T19:03:22.166Z] TOOL RESULT

```
=== LEW aes ===
1402:aerazata- I 66
5779:Caballos I 125 *cabros I 8d4 Caeracaies I 157 caeto- I 120 caw, caio I 187/8 Calete, Caletes I 141 *calmis I 249 candetum (gall.- lat.) IT 294 canecosedlon II 511 canta- I 252 KOVTEML, “KAVTEVA, xarvtev I 155 caracalla II 239 Carantus I 1765 karnitu I 276 xdovor (galat.) [276
7010:caech (air.) I 129 caera (air.) I 157 cail (mir.) I 304 caile (air.) I 139 cailech (air.) I 142 catll (mir.) I 140 carmmse (air.) [147 cain (mir.) J 179, IT 330 cainnen (mir.) [201 caint (nir.) I 199 caire (air.) I 169 cairem I 172 caiss (mir.) J 136 caisse (mir.) I 177 caissel (mir.) I 180 cath (air.) IT 400 caithid (mir.) I 855 catthim (mir.) [211 calath, calad (air., mir.) J 14] calb (air.) I 143 Caliaci (air. og.) I 142 camm (air.) I 145, 149 canim (air.) I 154 cano, cana (mir.) IT 423 capall (air., mir.) L125, 853 cap(p) (mir.) [157, 162, 163 carae (air.) 1175, 855 caraum (air.) [175 carcar (air.) I 166 carn (air.) [7, § carna (mir.) I 170 carpat (air.) I 171 carr (air., mir.) LI71, 174 carran (mir.) I 171 casair (nir.) I 128
=== LAT aes ===
1686:"avantageux, favorable", cf.Caes., B.C. I 85,3, qui etiam bona condicione
1753:aera, -ae (era) f.(sans doute pluriel de aes, aeris considere comme
1760:aeranis: v. aes.
1777:aes
1789:laire, A aes: aeruscare: aera undique, i.e, pecunias colligere, P.F.33,
1800:aes (anc. ais), aeris n.: bronze. A. factum "bronze travaille" et a.
1802:forme de la monnaie (cf .per aes et libram ) remplacee par 1 'a. signatum
1804:"monnaie, argent", de IA aerarium "trusor public"; aes alienum "argent
1805:d'autrui, dette", cf.Ulp., Dig.50,16,313,1, aes alienum est quod nos
1806:aliis debemus, aes suum est quod alii nobis debent-, de IA obaeratus,
```


## [2026-09-04T19:03:25.267Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1750,1770p' LAT.txt; echo \"...\"; sed -n '1800,1830p' LAT.txt"
}
```


### [2026-09-04T19:03:25.358Z] TOOL RESULT

```
Panroman, M.L.34O; iri. der, britt. ayr. L'adj. derive aerius, attest^
A partir de Varron d'Atax, Catulle, Lucrbce, et surtout poetique, trans¬
erit le gr. aep(.o£. On a aussi aerinus: d'air, couleur d'air.
aera, -ae (era) f.(sans doute pluriel de aes, aeris considere comme
un f^minin singulier): i° nombre, chiffre (sens qu'avait le n.pl. aera,
cf.Cic.ap.Non., 193,11, soles, si aera singula probasti, summam... non
probare?) 3° "bre" d'ou iri. aer. - Mot de basse ^poque. V.Kubitschek,
Grdr. d. ant iken Zeitrechnung, p.yy; et Sofer, p.116. M.L.341.
aera, -ae f.: ivraie, mauvaise herbe, dans Plin.i8,iss. Emprunt au
gr. oupa.
aeranis: v. aes.
aero, -onis (ero, hero,-onis) m.: panier, corbeille servant A porter
et A monter des materiaux. Terme technique, d£riv 4 sans doute de gr.
cupoq, aei,pu>. Cf. peut-etre aerumna, aerumnula. M.L.2903. Derive: fajero-
nalis.
aerumna, -ae f.: souffrance, ^preuve. Aerumna est ddfini par Cic 4 ron
aegritudo laboriosa, Tu.4,8,18, et qualifi^ de tristissimum uerbum,
Fi.3,35. C'est un terme plus expressif que labor ou dolor.
D 4 riv£s: aerumnula: aerumnulas Plautus refert furcillas quibus reli¬
gatas sarcinas uiatores gerebant... Itaque aerumnae labores onerosos
significant; siue a Graeco sermone deducuntur. Ham oupeiv Graece,
...
aes (anc. ais), aeris n.: bronze. A. factum "bronze travaille" et a.
infectum "quod in massis est"; a. graue "bronze au poids", premibre
forme de la monnaie (cf .per aes et libram ) remplacee par 1 'a. signatum
"bronze estampe". - Ancien, usuel. - Specialise bientot dans le sens
"monnaie, argent", de IA aerarium "trusor public"; aes alienum "argent
d'autrui, dette", cf.Ulp., Dig.50,16,313,1, aes alienum est quod nos
aliis debemus, aes suum est quod alii nobis debent-, de IA obaeratus,
cf .Varr., L.L.7,105 et qerator: debiteur (gl.); aesculor-. amas se r de la
petite monnaie (tardif). Aussi le sens de "bronze" a~t~il finalement
et 6 r 4 serv 6 aux derives aeramen, aeramentum, proprement "objet de bron¬
ze", cf.gr. )(aAxcopa. Aeramen (ardmen ) est demeure dans les 1 . romanes.
M. L.343.
L'ancien adjectif deriv6 est aenus, ahenus, issu de *ayes-no-s, cf.
ombr .ahesnes "ahenis". L'allongement de la seconde voyelle A la suite
de 1 1 amuissement de l's ( aesnos >*aeznos> aenus) a eu pour consequence
le maintien de l'a initial d'ou aenus en face de aes; en latin comme
en ombrien, ceci a ete marque par 1'introduction d'un h purement gra-
phique: ahenus (cf.ahala, etc.); L'etrangete de la forme a frappe les
erudita, cf.Serv.Ae.1, 357 , solutio dicenda est quomodo dicimus aena
( 1 .aera?) et agna. Hoc autem solum huiuscemodi uerbum in Latio inuenitur.
Sons 1 'influence du type en -eus des adjectifs indiquant la matibre,
on a fait a(h) eneus ; cf. t errdneus . La derivation aes \ a(h)enus etait
inintelligible en latin; d'aprbs ferrum | ferreus, etc.,sur le thfeme
aer- du g6nitif a 6te cr6e 1 1 adj. aereus, non atteste avant Varron.
Virgile emploie conjointement la forme ancienne et la forme nouvelle,
Ae. 1,448-449: Aerea cui gradibus surgqbant limina nexaeque | Aere trabes
foribus cardo'stridebat ahenis. De aenus ( aeneus ) derive aendtor ( aenea¬
tor) " joueur de trompette".
Autres deriv 6 s: aeratus: bronze, aerosus " 7 ioXuxaAxoc", aerarius
"concernant le bronze, ou la monnaie, le tresor"; et peut-etre aerdnis"i
qu'on lit dans Isid., Or.13,1,53, ceruinus est color equi, quem uulgo
```


## [2026-09-04T19:03:33.141Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1830,1845p' LAT.txt; echo \"=== KLN era ===\"; grep -n \"aera,  ‘counters\\|era,  n\\.\\|era ,  n\\.\" KLN_1966.txt | head; grep -n \"^era\" KLN_1966.txt | head"
}
```


### [2026-09-04T19:03:33.240Z] TOOL RESULT

```
qu'on lit dans Isid., Or.13,1,53, ceruinus est color equi, quem uulgo
gauranem dicunt. Aeranem idem vulgus uocat, quod in modum sit aereiaesculus - s« -
coloris; mais dans le lib.Gloss. le mot est doune sous la forme aeramen,
cf.Thes.s.u. et Sofer, 31 et suiv. M.L .343 (ae- et *aramen); aeramentum
(v.Lofstedt, Phil. Comm. z. Peregr .Aeth., p. «31); aerugo (avec un doublet
aeruca, -ae): rouille de cuivre, vert-de-gris; cf. ferrugo, lanugo, robigo;
d'ou aeruginosus; les formes romanea remontent a aerugo et aerigo (ce
dernier sana donte d'aprbs robigo), M.L.343. Sur aesculor n ,
v. Samuelsson, Glotta, 6,329.
Composta: ahenobarbus : surnom de la gens Domitia, avec un vocalisme
o au lien de i,etonnant, mais non sana exemple, cf .Primogenia (influence
du type grec en -o?; cf.Stolz-Leumann, Lat. Gr. , p .348 ) . - En outre,
nombreux composes po^tiques en aeri- traduisant pour la plupart des
adjectifs grecs en yakKO-: aericrepdns yakxoxpoxoc; aeripes yahicmovZ;
aerisonus \ixXx6xxvnoC . Cf. aussi pent-etre aestumo, que L.Havet, MSL
6,18, a explique comme un denominatif de *ais -ternos "celui qui coupe
=== KLN era ===
1464:Acnida,  n.,  a  genus  of  plants  of  the  amaranth family.  —  ModL.,  lit.  ‘without  nettles’,  fr.  priv. pref.  a-  and  Gk.  xv(8?),  ‘nettle’,  which  is  rel.  to xvi^siv,  ‘to  scratch’.  See  cnida. acnode,  n.,  point  of  a  curve,  not  connected  with real  points  of  the  curve  (math.)  —  A  hybrid coined  fr.  L.  acus,  ‘needle’  (see  acus),  and  E.  node. Acocanthera,  n.,  a  genus  of  African  plants  (bot.)
6279:camera,  n.,  a  chamber.  —  L.,  ‘vault,  arched  roof, arch’,  fr.  Gk.  xotpdcpa,  which  is  rel.  to  xocp-Tvog (whence  L.  caminus),  ‘furnace’,  and  cogn.  with L.  camur ,  camurus,  ‘curved’,  fr.I.-E.  base  *qam-, *qem-,  ‘to  bend,  vault’.  Cp.  It.,  OProveng., Catal.  camera ,  Sp.  camara,  Port,  camara,  F.  cham- bre,  OHG.  chamara,  OS.  camara,  OSlav.  komora, Lith.  kamara ,  OIr.  camra,  which  all  derive  fr.
7415:Derivatives:  chime,  tr.  and  intr.  v.,  chim-er,  n. chime,  chimb,  n.,  rim  of  a  cask.  —  ME.  chimbe, from  the  stem  of  OE.  cimbing,  ‘joint’,  which  is rel.  to  Du.  kirn,  ‘chime’,  G.  Kimme,  dial.  Swed. kind),  kimbe,  ‘edge’.  These  words  prob.  stand in  gradational  relationship  to  comb.  Cp.  dial. Swed.  kim,  ‘cockscomb’, chimer,  chimere,  n.,  a  robe  worn  by  bishops.  — MF.  chamarre,  samarre,  ‘a  loose  gown’,  fr.  Sp. zamarra,  fr.  Arab,  sammiir,  ‘weasel,  marten’. Cp.  It.  zimarra,  ‘robe;  cassock’,  which  was formed  with  vowel  dissimilation  fr.  Sp.  zamarra. F.  simarre,  ‘robe;  cassock’,  is  a  loan  word  fr.  It. zimarra.  Cp.  cymar,  simar,  zimarra. chimera,  chimaera,  n.,  a  monster  with  lion’s  head, goat’s  body  and  serpent’s  tail  ( Greek  mythol.)  — L.  chimaera,  fr.  Gk.  yluatpa,  ‘a  young  she- goat’,  which  is  rel.  to  xipapap,  ‘a  young  he- goat’,  lit.  ‘one  winter  old’,  fr.  xsip.a,  ‘winter’, which  is  cogn.  with  L.  hie  ms,  ‘winter’,  hibernus, ‘pertaining  to  winter,  wintry’.  See  hibernate  and cp.  chiono-,  the  first  element  in  Chimaphila  and the  second  element  in  Hedychium  and  in  iso- cheime.
7451:—  See  prec.  word  and  agential  suff.  -or. Chiroptera,  n.  pi.,  the  order  of  the  bats  ( zool .)  —
7507:choledocho-,  combining  form  meaning  ‘contain¬ ing  bile’.  —  See  prec.  word, choler,  n.  —  ME.  coler,  colere,  fr.  OF.  colere  (F. colire),  ‘choler,  anger',  fr.  L.  cholera,  fr.  Gk. yoXepa,  'bilious  diarrhea,  cholera’,  fr.  yolrh  also y6Xo c,  ‘gall,  bile’,  which  is  rel.  to  y'k'joc,  ‘greenish- yellow  color’,  yko^eiv,  ‘to  be  green’,  yluicib', ‘greenish-yellow,  pale  green,  green,  fresh’,  and cogn.  with  Avestic  zara-,  ‘gall,  bile’,  L.  fel, OSlav.  zluci,  Russ,  zelc.’,  Lith.  tulzis  (metathesis for  *zultis ),  Lett,  zults,  OE.  gealla,  galla,  ‘gall, bile’,  fr.  I.-E.  base  *ghel-,  *ghel-,  ‘to  shine;  yel¬ low,  yellowish  green,  green’.  See  yellow  and  cp. gall,  ‘bile’.  Cp.  also  next  word,  Chloe,  Chlorella, chlorine,  Chloris,  and  the  second  element  in melancholy,  Chrysochloris,  Echinochloa.  Cp.  also the  second  element  in  bezoar. cholera,  n.  —  L.  cholera,  fr.  Gk.  xoXepa,  ‘bilious diarrhea’,  fr.  yoTcq,  ‘gall,  bile'.  See  prec.  word, choleraic,  adj.,  related  to,  or  resembling,  cholera. —  Formed  from  prec.  word  with  suff.  -ic. choleric,  adj.  —  MF.  (=  F.)  choleriqtie,  fr.  L. cholericus,  fr.  Gk.  yokepixo^,  fr.  ydkipdi,  (see choler  and  -ic) :  first  used  by  Chaucer. Derivatives:  choieric-ly,  adv.,  choieric-ness,  n. cholesterine,  n.,  cholesterol.  —  See  next  word and  chem.  suff.  -ine.
8187:Coleoptera,  n.  pi.,  an  order  of  insects  ( =  Beetles). • —  ModL.,  lit.  'sheath  winged’,  fr.  Gk.  xoXeo- Trrepo?,  fr.  xoXeo?,  ‘sheath’,  and  Trrepov,  ‘wing’.
9179:cordiform,  adj.,  heart-shaped.  —  Compounded of  L.  cor,  gen.  cordis,  ‘heart’  and  forma,  ‘form, shape’.  See  cordate  and  form,  n. cordillera,  n.,  one  of  several  parallel  mountain ranges.  —  Sp.,  fr.  cordilla,  dimin.  of  cuerda, ‘rope,  cord’,  fr.  L.  chorda  (see  cord);  hence  the name  Cordilleras  (pi.)  given  by  the  Spaniards to  the  parallel  ranges  of  the  Andes, cordite,  n.,  a  smokeless  explosive.  —  Formed  fr. cord  with  subst.  suff.  -ite. cordoba,  n.,  the  monetary  unit  of  Nicaragua.  — Sp.  cordoba,  named  after  Francisco  de  Cordoba (died  in  1526).  Cp.  Cordovan, cordon,  n.,  1)  a  guarded  line;  2)  an  honorary  cord or  ribbon.  —  F.,  fr.  corde,  ‘twist,  cord,  cordon, ribbon  (of  an  order)’.  See  cord, cordon  bleu.  —  Orig.  the  blue  ribbon  worn  by  the knights  of  the  Holy  Ghost,  the  highest  order  in France  under  the  Bourbons;  later  used  to  de¬ note  a  distinguished  person  and,  facetiously,  a first-rank  cook.  —  F.,  ‘blue  ribbon’.  See  cordon and  blue.
11260:Dianthera,  n.,  a  genus  of  plants,  the  water  willow (hot.)  —  ModL.,  lit.  ‘having  two  anthers',  fr.
11536:Diptera,  n.  pi.,  an  order  of  insects,  the  flies  ( en - tomol.)  —  ModL.,  fr.  Gk.  Sitrrepa,  neut.  pi.  of SbiTEpo?,  'having  two  wings’,  fr.  Si-  (see  di-, ‘two’)  and  mepiv,  ‘feather,  wing’.  See  ptero- and  cp.  next  word.
13339:Se?),  ‘freckle’,  fr.  ini  (see  epi-)  and  7, >.105, ‘sun’.  See  helio-  and  cp.  words  there  referred  to. Ephemera,  n.,  the  genus  of  the  Ephemerida  (en- tomol.)  —  ModL.,  fr.  Gk.  itpTjuspov,  ‘dayfly’, prop.  neut.  of  iqjrjpepop,  ‘lasting  but  a  day, short-lived’,  used  as  a  noun,  fr.  ini  (see  epi-) and  ■fjpipa,  ‘day’.  See  hemero-. ephemeral,  adj.,  living  only  for  a  day;  short¬ lived,  fleeting.  —  Lit.  meaning  ‘of  one  day’; formed  with  adj.  suff.  -al  fr.  Gk.  iy^iLepoc.  See prec.  word.
13505:era,  n.  —  Late  L.  aera,  ‘era’,  fr.  L.  aera,  ‘coun¬ ters;  items  of  calculation,  money’,  pi.  of  aes, ‘brass’.  See  ore.
13506:eradiate,  intr.  and  tr.  v.,  to  emit  light.  —  Formed fr.  e-  and  radiate.
13507:eradiation,  n.,  emission  of  light.  —  Formed  fr.  e- and  radiation.
13508:eradicable,  adj.  —  See  next  word  and  -able.
13509:eradicate,  tr.  v.,  to  root  out.  —  L.  eradicatus,  pp. of  eradicare,  ‘to  root  out’,  fr.  e-  and  radix,  gen. radicis,  ‘root’.  See  radix  and  verbal  suff.  -ate. Derivatives:  eradicat-ion,  n.,  eradicat-ive,  adj., eradicat-or,  n.
13513:erase,  tr.  v.,  to  rub  out.  —  L.  erasus,  pp.  of  era- dere,  ‘to  scratch  out,  scrape  off’,  fr.  e-  and rdsus,  pp.  of  radere,  ‘to  scrape,  scratch’.  See raze.
22951:eral)  —  Named  after  Mariposa  County  in California.  For  the  ending  see  subst.  sufF.  -ite.
38491:eration,  temperance’,  fr.  temperans,  gen.  -an¬ tis,  pres.  part,  of  temperare.  See  temper  and -ance.
```


## [2026-09-04T19:03:41.290Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT isti/isvan/aesa ===\"; grep -n \"isvan-\\|īšvan\\|'isti-\\|iSti-\\|aesa-  n\\.\\|aeSa-\" BRT.txt | head -20; echo; grep -n \"Reichtum\" BRT.txt | head -20"
}
```


### [2026-09-04T19:03:41.372Z] TOOL RESULT

```
=== BRT isti/isvan/aesa ===
6380:•  j.  aää'uTvaeSa-  m.  EN.  eines  Gläubigen:  •  j-  asam.yei»he.varaza  indekl  m.,  EN. •>iiÄ^  aj^M?  YLy.  116.  leines    Gläubigen:    'za    (als   GS.)'*    nama
7998:•  g,  isvan- Adj,  1) 'verfügend,  Herr  über-' (Gen.):  kasSuic'U  n3  aiilunS  ia^^  (sd.) avAal  'väcJl  Aas  paraol  "ob  man  über weniges,  ob  man  über  vieles  Herr  ist,  man soll . ,"  ¥..^7,4''.  a)  'der  (es)  vermag': hyat  na  fryai  vaEäamnS  °va  daidU  .  . fräxsn^mm  rafirü^  ".  .  Unterstützung,  wie sie  ein  Wissender,  wenn  er  es  vermag, dem  Freund  gewähren  soll"  y.415.14.
10300:hvialia  V.O.33,  /tf.8;  —  hiku  pqsitu  (sd.) °tu  (IS.)  tihayaaa  Y.16.2;  —  nsit  Alm  'tvd (GS.)  vindm  pasvasca  . .  "es  fanden  nicht mehr  Platz  .."  V.2.8;  9.  a)  mit  misvan- Adj,  (sd.,  auch  fdSt.):  misvärum  'tarn  S. 2.^0;  — misvänahe  'tvaie(GS.)^>  S./.30; usw.  2)  sva.  'festbestimmter,  vorge- schriebener, richtiger  Ort  (usw.)';  iva aHahe  nars  'tu^  anhat  ya£  irisis.kasahe ^■,?-^5i  —  y^S  "^'''^  zaota  (sd.)  /r3ya- zititi ..zaotars  "lai-a^  (IS.) .. syae^nöJätfya .  .  paiti.jatfkdit  hävanänö  -taiii'  .  .  N.  Si;
14719:•  j.,  g.  'tkaeSa-  m.  i)  'Lehre'  bes.  auf religiösem  Gebiet,  'Glaubenslehre';  a)  im gAw.  spez.  von  der  Lehre  des  falschen Glaubens  'Irr-,  Afterlehre'":   a^^ä  ahmät
15807:•  j.  paoiryö.t^aeSa-  m-,  Plur,  'die  ersten Lehrer  des  Glaubens'*':  asaunqm  fra- vasinqm  .  .  *fanqm  /ravaltnam  "den  Fr. der  Gläubigen  .  .,  den  Fr.  der  ersten Lehrer"  Y.r.  18.
17785:•  j.  fra-vaeSa-  Adj.  'im  Besitz  von  — , teilhaftig'":  zardiustraAe  .  .  paotrysi  '"•läi paoiryüi  fravaiiiayamnäi .. gqmca  alinua  ..
20538:misvan-  11 86
20550:•  j.  misvan-  Adj.  'die  Gemischten  ent-
20613:Vgl.  mp.  hamislak  'gemischt',  np.  ämestan (wozu  Hbm,  PSt.  8).  —  Vgl.  misvan-.  —  Pü. (zu  Y.  46):  vartmS,  (zu  Y.  33):  kila  i  Si  i kam  mal  Citel  an  i  dräy  keia  i  öi  an  i  apilak, dazn  die  Erl.:  hamhlakän.—  ')  S.  zSt  Bthl.
24785:'raeSa-

7470:•  j.  äsu.aspya-  n.  'Besitz  schneller  Rosse, Reichtum  an  schnellen  Rossen':  'pTm da'jiiiti  mi%rU  Ytjo.3; —  '^wqm  naracit yöi  taxma  Jat'iyhnte  -ptm  YL5.86;  98.
8047:•  j-.  g-  tätay-''  f.  i)  'Vermögen,  Können, Imslandsein,  Kiaff,  mit  Inf.:  Aat  vf  xsa- :^r^m  kn  'trfi'SS.)  iyao>amli  masda ya>ä *vä  ^kaxmi  (sd.)  asä  vokü  manatikä ^mydidyni  (sd.)  "habt  ihr  die  Herrsch- gewalt, habt  ihr  die  Kraft  lu  tun,  o  M., . .,  o  Asa,  o  VM. . .?"  Y. ^4.5.  2)  'Ver- mögen sva.  Habe,  Besitz,  Gut,  Reichtum'; auch  mit  obj.  und  subj.  Gen.:  mä  yave imat  timiliifm  .  ,  /ratahlt  .  .  x^iiiravatti °ti/  mä  j^ä'hravaiti  äsna  frazaintii  Y. 60.7;  —  äps  °tjm  vS  jaidyämi  pauru.- sars'iqm  . .  *frazaintimla  Y.  (fj.  1 1 ;  —  °tlm pourus.x^a'irqm  .  .  ''frazaintim  Y.  68. 1 1 ; —  kahmäi  °tim  .  .  kahmäi  ainistim  .  . baxsiJni  Yt  10.  108— 110;  —  '/Im  jaio- yanla  . .  molu  pas^aSta  . .  'tlm  baon  sivÜla Yt.5.98;  —  dazdi  ahmJk3tn  . .  'lfm  anum v)r?^r(qmnua  Yt.  ici.33;  —  ydi^a  , .  uz-
8057:men,  die  Fr.  . .,  damit  es''  in  Besitz  des Besseren  gelange,  den  Angreifem  wider- stehe, Reichtum  und  Herrlichkeit  weiter -ermehre"  Y.  60.4.
9867:•  j.  gao-8urä-  f.  'Reichtum  an  Rindern' (?) : TtrthrtrjnS  avi  imal  nmänpm  •räbyBijiV. als  IP.)  :^ar»nö  pairi.vsnnavaiti  (sd.)  Yt.
20482:•  g.  mi^ä.rayay-,  j.  *miizä-rayay-"  Adj. (auch  fem.)  'der  grosse  Reichtum«  be- sitzt, schätzereich':  s»rac^d  asi  "roya (ISf.)'* Aaamni!  "SraoiS  .  .  im  Verein   mit  der
24767:«oi/Ä  gäi/  pälixUh  {pa  sh-'iA,    N.  62)  J'arlan^      Et.  und  Bed.?    Vll.  "rc^i^f-manak^  {'n,a»ai-)f. "wie   wird    et   sialthaft   das  Fleisch  (bis  lur       '^°  "'E-  'Aufenthalt  des  Reichtums'? Mtiigung)zue_ssen?"-s)DasPraev  doppelt.       j    raeVa-  Adj.  'reich;  prächtig,  pnmk- und  No.  6,  8.  -  6)  Pü.  (lu  V.  5. 33,  i'jlio): '  ™''  =    AvanxsaStahe  amfiahe  'vahe  Yt  6.
25174:•  j.  rayay-  m.  'Reichtum,  Fracht,  Prunk': yaf  as  ,.ralm{A.S.)'^  rafvastirnff  Yt  ig,  jg;
25396:•  f-  räy-  DO.  'Reichtum':  astm  *d»r>idyäi (sd.)  .  .  räyB  (GS.)  a/f/  vaahht!  gaim mananhB  Y.  43- 1-
```


## [2026-09-04T19:03:52.096Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"•  g\\.  is-\\|•  j\\.,  g\\.  is-\\|•  g\\.  aesa-\\|•  j\\.,  g\\.  aesa-\\|•  j\\.  aesa-\" BRT.txt | head -10; echo \"=== search ise ===\"; grep -n \"'ise\\b\\|ise  '\\|isS  '\" BRT.txt | head -5; echo \"=== aesa ===\"; grep -n \"aesa-  f\\.\\|aesa-  n\\.\" BRT.txt | head"
}
```


### [2026-09-04T19:03:52.179Z] TOOL RESULT

```
=== search ise ===
2761:Z  verlangen,  dass  er  (dem  Freund)  Schutz gewähre"  Y.  7/.  13,  a)  statt  des  praed. Akk.  ein  Adv.:  yimS  avai^a  ktrsnaot yaia  dim  Ual  ahurö  mazäi  "V.  tat  so, wie  es  AhM.  von  ihm  verlangte"  V.  2. 31.  4)  spez.  'zu  hören  verlangen,  hören wollen':  ^J  tsi  asä  yi  asäi gius  ia/.i  (sd.) mraot  is3ntl  tnä  tu  isi  vohB  manaaAl "was  ,  .  kund  getan  hat,  hören  wollen  sie dasdurchdeinenKji/."  Y.4Ö.9.  a)  ohne Ob],":  at  tä  vaxfyj  is?ntd  "ich  will  davon reden  zu  denen,  die  hören  wollen"  Y. _jo.i;  47-6*>;  — yalüä  asnat  yaila  anrät (sd)  isa:iä  Y.  45- 1-  5)  'Jemand  (Akk.) angehen,  sich  an  ihn  wenden,  ihn  bitten': ise  'i/wqm  aAura  mazda  ptrsst  '^wqm  . . Yt  12. 1 ;  —  *yas»  tat  *afivataiti  (sd.) paranlarfm  (sd.)  isöit  N./2;  —  vayö  .  . harn  istmmm  painyätte  ".  .  stellt  sich ein  bei  dem,  der  sich  (an  ihn)  wendet" Yt-/>S3;  —  al  yastim  nsii  na  is7mnS (inpass.Bcd.)9*Jj'i7/(sd.)Y.4ö.6.  a)  mit Inf.:  amslacit  .  .  avaiahe  isinli  masya- kanhs  "die  ^Ienschen  bitten  die  Am.  um Beistand"  Aog.  41.  6)  'Jemand  (Akk.) angehen  (in  feindlichem  Sinn),  angreifen, nachstellen';  avae^amai  ^iff  pantö  yim isfnli    mi^röjiruiS  Yt.  io.45.  7)    'er-
=== aesa ===
```


## [2026-09-04T19:04:01.160Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Herr  über\\|Herr  sein\" BRT.txt | head -10; echo \"=== aesa ===\"; grep -n \"^• *[jg]\\.[, ].*ae[sS]a-\" BRT.txt | head -20"
}
```


### [2026-09-04T19:04:01.243Z] TOOL RESULT

```
2702:aes-V. 'Herr  sein  Über —'.  Praes." —  Inf.  Wie.
2703:*aevö.gava-'>  Adj.  'einhändig:  ya>a\     Nur  Med.  i)'Herr  sein,  verfiigen  über-, paaunö    'vö  afnö-armö  raaAam  *avajia-  zu  rechnen  haben  auf-'  (Gen.)  tistrim.. yänttm  'savavä  ä>t  eis  äUe^'v.33'\         ,isanpm  /iazar»räi  (statt Oen.):  ayapianam ISi.-.  tvai  göii).—  »  Bei  DsT.  'savö;  vU.  ist '"den  T.,  der  über  tausend  Herrlichkeiten das   Wort    mit   dem    zweiten   (-Zeichen   ge-,  verfügt"   YLA49;    —    kat   möi  vrvä    isl Sin''„'t"srenc'isrJnki^nin^^^^^^^  l^hyä-va^ho  "ob  meine  Seele
7998:•  g,  isvan- Adj,  1) 'verfügend,  Herr  über-' (Gen.):  kasSuic'U  n3  aiilunS  ia^^  (sd.) avAal  'väcJl  Aas  paraol  "ob  man  über weniges,  ob  man  über  vieles  Herr  ist,  man soll . ,"  ¥..^7,4''.  a)  'der  (es)  vermag': hyat  na  fryai  vaEäamnS  °va  daidU  .  . fräxsn^mm  rafirü^  ".  .  Unterstützung,  wie sie  ein  Wissender,  wenn  er  es  vermag, dem  Freund  gewähren  soll"  y.415.14.
26405:—  »Zi^  (sd.)  'rayä  ^rtiffaonS  Y.g.y;\t 5-33,  '7-35;  —  ^axnm(sd.)  'nm  V.l. 16;  s;  —  us/avaia(sA.ya  yä  'raYx^iq. 67;  — yasfum  'nm  haplanhnitim  Y.  41.  8, Vr./ff.o,  21.0;  —  kcäia  xä..a  vanhjis.. *ra  vaxiyenteisA.)  vax^a  Yt.8.^2.  a)  mit Gen.  'gebietend,  Herr  über -">:  aus  .  . *rag}uica  vaslrakecaYx,.ig.^^.  Undeut- lich: ^yaoiäni  'ra/ie  F.^g.  Wertlos: '^pu%rqs  .  .  yS   'ra  Vlspa   VyL^ff.
=== aesa ===
3304:•  j.  a-daratö.tkaesa-  Adj.  'der  den  Lehrer nicht  achtet':  vlspe  drrantö  tanu.drujö yS'^ •sd'''  vXspe  'sS'*  yß'>  asnifs'ß'''  "alle  sind ungläubig  und  leibhaftig  mit  der  Dr.  ver- bunden, die  den  Lehrer  nicht  achten;  all die  achten  den  Lehrer  nicht,  die  (ihm) ungehorsam  sind"  \.i(J.i8.
5508:•  j.  ar9nat.£aesa-  Adj,  —  ?—,  von  Miira: miir^m  .  .    'um  vindatspa^tm  hazaara.-
6380:•  j.  aää'uTvaeSa-  m.  EN.  eines  Gläubigen:  •  j-  asam.yei»he.varaza  indekl  m.,  EN. •>iiÄ^  aj^M?  YLy.  116.  leines    Gläubigen:    'za    (als   GS.)'*    nama
6919:•  j.  ahurö.tkaesa-  Adj.  (fem.  'si-)-.  s. unter  ahura.tk'.
8924:•  j.  'kaeS-  V.  'struere';  nur  mit  Praev. Praes.  2  caesa-,  5  .vV/.-",  30  (Iter.)  caS- s-aya-.
12538:•  j.  daesa-  m.  'Zeichen,  Otnea':  pattiHatSe ayanqmca    :^a/nanqm    ayanqmca
13037:•  j.  dasvar-  o.  'Gesundheit',  nur  in  Ver- binduDg  mit  (folg.)  batsaza-  n.  'Heiltum': 'varfca  baisazfmca  V.5. 53;  —  ni  'van nl  baltazim  (näml.  mruyt)  Y.  p.  1 7 ;  71. 1 7, Vr.  20,  I,  Vyt_35; —  ci^nm  'van  baesa- stm  Y.  70. 7;  *FrW.9.  2";—  'varp  (statt AD.)')  baliaza  äfrfnämi  Y.6S.i$;  — *'varii*  (statt  des  Instr.)"  . .  ba^asa  Y. 55.3;  —  'van  (statt  des  Dat.)''  baisa- zäUa  Y.  6S.  2.
13723:•  j.  dürae-urvaesa-"  i)  Adj.  'des  Wende fem  liegt',  vom  Weg:  °s)m  paili  pantqm Vt.i.35.  2)m. 'ferne  (Weges)wende':(7fl/ ti  narqm  fravaz>nti  'i»m  ",  .  zur  fernen Wegeswende"  Vt.  (J.  58.
14719:•  j.,  g.  'tkaeSa-  m.  i)  'Lehre'  bes.  auf religiösem  Gebiet,  'Glaubenslehre';  a)  im gAw.  spez.  von  der  Lehre  des  falschen Glaubens  'Irr-,  Afterlehre'":   a^^ä  ahmät
14808:•  j.  'paesa-  m.  'Schmuck,  Zierrat':  °sa F.  10.
14810:•  j.  'paesa-  i)  Adj.  'aussätzig':  ma  mg aiiayä  zao'hrays  /ranhar?ntu  *mä  *°sa'^ yS  vUiritsJanus". .  ein  Aussätziger,  dessen Person  isolirt  ist"  Yt.5.  92.  2)  ra. 'Aus- satz': ma  ähra  .  ,  'sS  yS  vJt3r7tS.tanu! mäZa.Bm  anyqm  daxstanqm  .  ,  aarahe mainySus  "nicht  .  .  AussaU,  womit  die Isolirung  der  (betroffenen)  Person  ver- bunden ist,  . ."  V,  2.  29.
15653:•  j.  paouru.{raourvaesa-  Adj.  (fem.  °sa-) 'mit  vielen  Ausläufern':  harqm  btrszaitim 'sam  Yt72.  23.
15807:•  j.  paoiryö.t^aeSa-  m-,  Plur,  'die  ersten Lehrer  des  Glaubens'*':  asaunqm  fra- vasinqm  .  .  *fanqm  /ravaltnam  "den  Fr. der  Gläubigen  .  .,  den  Fr.  der  ersten Lehrer"  Y.r.  18.
17785:•  j.  fra-vaeSa-  Adj.  'im  Besitz  von  — , teilhaftig'":  zardiustraAe  .  .  paotrysi  '"•läi paoiryüi  fravaiiiayamnäi .. gqmca  alinua  ..
21503:•  j.  yah-  V.  'sieden'  (intrans.).  Praes.  6 jraesa-'\  2^  jyagsya-.  —  FP[P.  yaäa-i?)».
23470:•  j.  väiti-gaesa-  in.  Name  eines  Gebirgs*>: ; akmal  hala  garayS  fraexsyan  . .  dvadasS  j 'SS  Yt  ig.  2.
24499:•  j.  vispö.paesa-  Adj.  'mit  allem  Schmuck, allerlei  Zieraf :  vä^?Tn  .  .  's^m  zaranalmm Yt.  10.  124.  [Y.  57.  20:  lies  'paislm; s.  -pis-.]
```


## [2026-09-04T19:04:14.322Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ore",
 "prompt": "Give the full etymology of 'ore', including Old English ār/ōra, Proto-Germanic *aiz-, PIE *ayes-, and whether two words merged."
}
```


## [2026-09-04T19:04:14.629Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/era",
 "prompt": "Give the full etymology of 'era': Late Latin aera, Latin aera plural of aes, and the semantic development to 'era'."
}
```


### [2026-09-04T19:04:19.528Z] TOOL RESULT

```
# Etymology of Ore

The word "ore" comes from a merger of two Old English terms. The first, *ora*, meant "unworked metal" and related to *eorþe* ("earth"). The second, *ar*, meant "brass, copper, bronze."

Both traced back through Proto-Germanic. According to the source, *ar* derived from "*ajiz-," which also produced Old Norse *eir* and Gothic *aiz*. These ultimately stemmed from the PIE root "*aus-" meaning "gold."

As the source explains: "The two words were not fully assimilated till 17c.; what emerged has the regular modern form of *ar* but the meaning of *ora*." 

The modern word thus retained the phonetic shape of *ar* while adopting the broader semantic scope of *ora*—referring to metalliferous minerals worth mining rather than just worked metals.
```


### [2026-09-04T19:04:21.109Z] TOOL RESULT

```
# Etymology of "Era"

The word "era" derives from Late Latin *aera* (attested from the 7th century), which scholars believe originated from Latin *aera*, the plural of *aes* meaning "counters used for calculation." The root *aes* itself denoted "brass, copper, money."

## Semantic Development

The chronological application began in 5th-century Spain. The term initially meant "the starting point of an age" in English usage (1716). Its meaning evolved to encompass "system of chronological notation" by the 1640s, and finally "historical period" by 1741—as exemplified by the U.S. *Era of Good Feeling* (1817).

This semantic shift reflects how the Latin concept of *aes* (originally counters for reckoning) transformed into a foundational term for marking and measuring time across civilizations, from ancient Spanish and Chaldean eras to modern historical periodization.
```


## [2026-09-04T19:04:28.601Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/own",
 "prompt": "Give the full etymology of 'own' (adj. and verb), Old English agen, Proto-Germanic *aigana-, and the PIE root cited; also mention owe and ought if given."
}
```


## [2026-09-04T19:04:31.439Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ey%E1%B8%B1-",
 "prompt": "Does this page exist? If so give the reconstruction, meaning 'to own/possess', and its descendants (Proto-Indo-Iranian, Proto-Germanic *aiganą, Avestan, Sanskrit īś-). If it does not exist say so."
}
```


### [2026-09-04T19:04:34.904Z] TOOL RESULT

```
# Etymology of "Own"

## Adjective
The adjective "own" comes from Middle English *ouen*, derived from Old English *agen*, literally meaning "possessed by." This traces back to Proto-Germanic *aiganaz* "possessed, owned," which appears in related Germanic languages like Old Saxon *egan* and German *eigen*. 

The ultimate source is the PIE root *aik-, meaning "be master of, possess," also found in Old English *agan* "to have" (see "owe" below).

## Verb
The verb developed around 1200 from Old English *geagnian*, sharing the root *agan* "to have, to own." This form became obsolete by 1300 but was revived in the early 17th century, partly as a back-formation from *owner*. A secondary sense developed by 1300: "to acknowledge, concede, admit as a fact."

## Related Words

**Owe**: This verb shares the same Old English root *agan*. Originally meaning "to have," its sense shifted in late Old English to "have to repay," eventually yielding the modern meaning of indebtedness.

**Ought**: The past tense form *oughte* (from *agan*) eventually developed into this independent verb expressing obligation.
```


### [2026-09-04T19:04:36.755Z] TOOL RESULT

```
# Response

Yes, this page exists. The reconstruction is **\*h₂eyḱ-**, meaning "to appropriate, possess."

The documented descendants include:

- **Proto-Indo-Iranian**: \*Háyćati
- **Proto-Tocharian**: \*aik- ("to know, recognize")
- **Proto-Italic**: \*aiko-
- **Ossetian**: исын (isyn, "to take")

The page notes that "The _a_- vowels in Tocharian and Germanic could be from a pervasive _o_-grade," which aligns with the Germanic \*aiganą you mentioned. However, the specific Proto-Germanic form is not explicitly listed in the visible content, though it's referenced indirectly through the discussion of Germanic vowel evidence.
```


## [2026-09-04T19:04:43.433Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/aigan%C4%85",
 "prompt": "Give the reconstruction, meaning, etymology (PIE root), and descendants including Gothic aigan, Old English āgan (> own, owe, ought), Old Norse eiga, Old High German eigan."
}
```


## [2026-09-04T19:04:44.101Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/aiz",
 "prompt": "Give the reconstruction, meaning, PIE etymology, and descendants including Old English ār (> ore), Gothic aiz, Old Norse eir, Old High German ēr."
}
```


### [2026-09-04T19:04:48.746Z] TOOL RESULT

```
# Proto-Germanic *aiganą

**Reconstruction:** *aiganą

**Meaning:** "to possess, to own, to have"

**Etymology:** Derived from Proto-Indo-European "*h₂eh₂óyḱe," which comes from the root "*h₂eyḱ-" meaning "ability, possession."

**Key Descendants:**

- **Gothic:** aigan, aihan
- **Old English:** āgan, which evolved into modern English "own" (past participle), "owe" (present), and "ought" (past tense)
- **Old Norse:** eiga, which produced Icelandic, Faroese, and Scandinavian forms like Swedish "äga" and Danish "eje"
- **Old High German:** eigan, leading to modern German "eigen" (own/own)

The verb is classified as irregular and preterite-present, showing extensive conjugational variations across person, number, tense, and mood in its reconstructed forms.
```


### [2026-09-04T19:04:50.570Z] TOOL RESULT

```
# Proto-Germanic *aiz

**Reconstruction:** *aiz (neuter noun)

**Meanings:** "copper, bronze" and "ore"

**PIE Etymology:** Derived from Proto-Indo-European *h₂éyos

**Key Descendants:**

- **Old English:** ār, ǣr → Middle English ore, oure → Modern English ore
- **Gothic:** 𐌰𐌹𐌶 (aiz)
- **Old Norse:** eir → Icelandic eir, Norwegian Nynorsk eir, Swedish ärg, Danish ir
- **Old High German:** ēr → Middle High German er → German ehern (via ērīn derivative)

The term originally functioned as a z-stem but underwent phonological leveling where "the older nominative singular alternant *ajaz > *āz was levelled out in favour of the oblique stem *aiz," causing it to resemble a neuter consonant stem instead.
```


## [2026-09-04T19:05:00.527Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT ore ===\"; grep -n \"ORE,  metal\\|Ore,\\|ORE\\.\" SKT.txt | head -5; echo \"=== SKT OWN ===\"; grep -n \"OWN,\\|OWE,\\|OUGHT,\\|ERA,\" SKT.txt | head -8"
}
```


### [2026-09-04T19:05:00.596Z] TOOL RESULT

```
=== SKT ore ===
1016:ASHORE.
12840:ORE.
18618:STORE.
=== SKT OWN ===
```


## [2026-09-04T19:05:01.938Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG ais ===\"; grep -n \"\\*Hai(a)š\\|Haiš\\|\\*aiš\" CHEUNG.txt | head -10; echo \"=== CHEUNG ahan ===\"; grep -n \"āhan\\|āsēn\" CHEUNG.txt | head -5"
}
```


### [2026-09-04T19:05:02.010Z] TOOL RESULT

```
=== CHEUNG ais ===
=== CHEUNG ahan ===
```


## [2026-09-04T19:05:04.688Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12836,12846p' SKT.txt; echo \"=== own ===\"; grep -n -i \"^Own\\|^Owe\\|^Ought\\|^Era\" SKT.txt | head -10"
}
```


### [2026-09-04T19:05:04.769Z] TOOL RESULT

```
a  track  (below).
L  »riim,  ft  track,  circuit ;
-4(it  >LifIis   -ta  from  <v^'-,  crude f  «v^r  An  offa^  circle.
E;  aec^Krort. B»  l]L»Ck.)    L.  mvJUfim.^
ORE.
Gk.  A/>xi^crpa,  an  orchestra;  which,  in  the Attic  tbcfllrCf  was  a  space  on  which  the chorus  danced.  — Uk.  6pxioftai,  I  tlaucc. Orchis,  a  plant.  (L.  — Gk.)  L.  anhis.^ Gk.  opx^f,  a  testicle,  a  plant  with  roots  of testicular  shape.  Dor.  orchid,  a  false form,    since    tne    gen.    caM    of   ^x"  ^
hp\itM.
Ordain ;  see  Order.
Ordoal;  sec  Deal.
Order.  (F.-L.)    F.  erdtt,  O.  F.  erdine.
—  L.  oniincm,  ace.  of  erdo,  order.  I'cr- hapc  allied  to  Oiigrixi.     Der.  dis-onltr.
=== own ===
4295:eram,  a  gratiag.  — L.  ertUa,
5935:ERASE.
5953:Era.    (I.)    L.   ara.    ait   era,  (weA From  a    tvirtlcular  sciuc  of  tfn*, (for  calculation)*  pi-  ol  'J^.  brw^
5954:Eradicate ;  sec  Badlx.
9088:own ;  ffi^  mpaffiS,
12954:ought.  cE.)    The  pres.  tense  of  A& dgan  \&  it  dh,  really  an  old  pt.  tense ;  h was  formed  the  pt.   t.   dAtt^   M.  £. aughtt,  OH^htig  mod.  £.  aught.
12956:own  (1),  possessed  by  any  one. to  oneself.   (£.)     M.E.  a-^en,  awtn, contracted  to  own  by  loss  of  /.    A.S.  ig^ own,  orig.  pp.  o(  dj^n,   to   possess; Owe  (a^ve).  4*  ^ccT.  ti^it,    Uan.  Svni
12957:own  (2),  to  poMess.  (E.>    M.  E. ahnitnt  aAnen,  ohntn.     A.  S. appropriate,  claim   as   one's    ow verb,  from  A.  S.  45m,  oMm  (al eigyta,  to  claim  as  one's  own  . own.     Der.  own-er.
12959:Own  (1).  Own  (2);  see  Owe.
12960:Own  (3),  to  grant,  allow.  (E,) confused    with  au/m    (j),    yet  of origin.      M.  E    unntn.    I0   yj*M ; UHnan,   to  grant.     The   prcs.  t  b an.  M.  E.  iVl  dM  or  ith  on,  1  own, Icel.  uHHat  to  grant,  pre&.  t.  tk  mm gi-unnan,  G.gvnMtn,  O.  H.  G. grant.
```


## [2026-09-04T19:05:12.157Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"ore (1)\\|Ore, \\|ore,  unwrought\\|unwrought\" SKT.txt | head -5; echo \"=== owe ===\"; grep -n -i \"^Owe\\b\\|Owe (\" SKT.txt | head -5; sed -n '12940,12956p' SKT.txt"
}
```


### [2026-09-04T19:05:12.240Z] TOOL RESULT

```
611:Ambassador,  Embassador.  (1 Low  L.-O.  ILG.)  F.  ambassa,f.'iir  »y. amifas^aiie,  an  cmbass)';  prob.  ''■."-! from  Ilal.  aTi^ajrw/i*.— Low  L (Lex  Salictt) ;  more  correctly  am^  . mission,  scr^'ice.  —  L.  ambaciux,  a  »ervut. emissar)';  Cxsor,  de  Bell.  Gall.  \*i. O.  W.O.  ambaht,  ampahi,  a  servant Goth,  cmdbahti,  a  servant,  p.  The  O. prefix  am',  Goth.  aW-,  is  cognate anU.  Gk.  dyr/.  before,  in  place  of; baht  means  a  sen*ant,  orijj.  '  devoted. Skt.  bkakta,  devoted  :  hhakii^  tervfafc (Origin  of  L.  ambacius  disputed.)
748:AntO-,  prefix,  before,  (L.)  L.  ante,  be* fore.     Allied  to  Anti-,  q.v.
786:t  supposed  to   be  etjuivalent   to  a  Low  L, ^Htoiuhnum  * ;    from    antf.    before,   uid cmtus,  the  eye.     ^  Prob.  the  latter. AnuB,  the  lower  orihce  of  the  bowels. (L.)     L,  a«w.
3607:Co&Bt.  (F.  -  L.)  M.  E.  t6st€.  -  O.  F. costt  (F.  c$U),  a  rib,  slope  of  a  hill,  shore, w  L  casta,  a  rib.
4252:ktira,  Dan.  >»r/,  to  do/c,  Iter  quiet;  Swed. ku/a.  Ik>  dore,  rooM,  Mtttc  to  icit  ^as  binis). LI.  Uoth,  kwairrus,  identic. Oowl  (I).  K  monkb  >ioo<l.  (L.)  M.  £. fQuet^cHMtL  A. S  ii///^.  a  cowl;  cf.  Kcl. kt^jl,  *tfrf.  towL-L  iu^ttHtu.     i^ybKU.)
=== owe ===
19230:owe,  ccrnclude ;  esp.  used  of  closing  the pa  of  the  public-houses,  at  the  sound  of e  drum.  So  also  G.  zap/enstreiih,  the ttoo,  is  lit  '  tap-slrolce ; '  and  Low  G. """■•*,  the  tatioo,  is  lit.  'tnp-shutting.' (^  tap  is  cognate  with  K.  tap ;  and
Oval,  egg  shaped.  (F.  —  L.>  F.  aval Formed  with  suffix  W  ( •«  L.  Wu)  from  L. 9itum,  an  ^g.  •f*  Gk.  ^(jv,  an  egg.  p.  L. 9uum  and  G^iiov  are  from  a  common  lAse AWI,  appearing  in  1  auii,  %  bu&\  «ee Ariarr.     And  we  £k«.     Dw.  r»-ar-y,
I
jao
OVATION.
Low  L.  tntarta,  the  part  of  the  body  in which  eggs  arc  fonnca  in  birds  ;  ovi  forttt, (^-shaped;  ovi-parvus,  (torn  l^cut-/aruig
[:^g- producing  (sec  Parent).
'  Ovation,  a  lesser  Koman  triumph.  (F.«> L.)  P.  oua/icn.^l*  ace.  oua/ionrm,  from cuatiOf  m.  shouting,  exultation  —  L.  euaius^ pp.  of  ouarty  to  shout  4*  G^  aiuv,  to ■hout. Oven.  (E.)    M.  E.<w<«  ( ^avm).    A.S.
[4^".  tyVi+Da.  tn'ifn.  Icet.  o/h^  omn  (also
''^'*  ^^^-  **S^'  ^-  5^>  Goth,  au^fw. (The  common  base  is  l/tlNA.) Over,  above,  across.  (E.)  M.E.  ffudr {=»OTrri.  A.S.  o/ir.  +  Du.  ovtr,  \(x\. y^r, Dan.  ovtr,  Swcd.  o/c^r,  G.  iib^r,  Goth, •i/ar,  Gk.  imip,  L.  S'up<r\  Skt.  upari, above.  The  Aryan  form  is  UPARl,  loca- tive case  of  UPARA.  upper  (Skt.  tt/ara, L.  s-upems,  A.  S.  y/cra).  This  is  a  compa- rative ibnn  from  Aryan  UFA  (Skt.  w/a, near,  on,  under ;  Gk.  vw6^  L.  s-u&,  Goth,  m/, under;  E.  <rve  in  tUjovc).  Closely  allied to  Up.  ^Thc  senses  '  over '  and  '  under  * arc  curiously  mixed.)  ^T  Hence  a  large number  of  compounds  beginning  with  nvr, which  present  no  difficulty.
oft.  often,  frequently.  (E.)  A.S.  9ft\^ whence  M.  £.  ofte,  with  added  -/^  and  lastly ofic-n  with  added  n,  +  Icel.  oft,  \>%Xk.oftt, Swe<l.  o/ta.O.o/fj  Goth.  ufea\  answering  in form  to  Gk.  Oiraror,  highest ;  a  supcrUtive form  allied  to  the  comp.  form  0Vtr.  Ktom the  notion  of  what  is  over  or  axccssive,  we pass  to  that  of  frequency.
Overt,  open,  public  (K,  -  I-.)  OF. ffvtrt  (later  ouvert']^  pp.  of  ovrir  (later Quvrir),  to  open.  The  etymology  is  dis- puted ;  Dicz  suggests  that  ettrir  is  a shortened  form  ofO,  F.  a-ovrir,  a-uvrir (Livre  dcs  Kois),  answering  toProv.a./«/'n>, to  open.  The  latter  can  be  resolved  into L.  adj  dif  op^rire,  where  a</  is  a  mere prefix,  and  dt-ffperirt  is  to  uncover.  Liltxc considers  ovrir  as  put  for  avrtr,  i.e.  !>. 9p<rirty  to  open.  p.  We  may  consider uvtri  as  due  to  confusion  bctwten  Qptritx and  aperirt,  both  difficult  words,  and  prob. related.  Perhaps  a-p^rirt^a^perirf*,  to nncover.  and  »ptrirt»ob-perin*,  to  cover up.  where  -ptrire  is  allied  to  L.  parart,  to prepare,  get  ready.
overture,  a  proposal,  beginning.  (F, — L.)     O.  F.   overture^    latter   ot«verturt,  on opening,  from  <X  F  ovtrt,  open  'above). Oviform,  Oviparous  -,  see  OvoL Ovr0,    to    poBicstj    hcQCc,    to    posteaa
OXUP,
another's  properly,  be  in  debt,  be  oblif^ (£.)  M.E.  <73rff,  awen,  owtm,  orig.  ' pos&ess ' ;  hence  to  be  obliged  to  do^  to in  debt.  A.  S.  ifgiUL,  to  have. (whence  long  0  from  A.  S.  i.  and  t»  ict^ •f-IceU  tiga,  to  possess^  have,  be  booiii own:  Dan.  a'^t  Swed.4^,  O.  H.  G Goth,  aigan,  to  possess..  Allied  toS'Lt to  possess  (VI^*)
ought.  cE.)    The  pres.  tense  of  A& dgan  \&  it  dh,  really  an  old  pt.  tense ;  h was  formed  the  pt.   t.   dAtt^   M.  £. aughtt,  OH^htig  mod.  £.  aught.
owing,  in  phr.  tmnng  /^»dae  Uk  t* cause  of.  (E.)    Orig.  prrs.  pL  of «
own  (1),  possessed  by  any  one. to  oneself.   (£.)     M.E.  a-^en,  awtn, contracted  to  own  by  loss  of  /.    A.S.  ig^ own,  orig.  pp.  o(  dj^n,   to   possess; Owe  (a^ve).  4*  ^ccT.  ti^it,    Uan.  Svni
```


## [2026-09-04T19:05:28.547Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD eik ===\"; grep -n \"eik-\\|zu  eigen  haben\\|eigen  haben\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-04T19:05:28.609Z] TOOL RESULT

```
=== WLD eik ===
713:(die aber vielmehr zu *seik- „die Hand ausstrecken“ gehoren, vgl. nach 
715:„ein erwiinschter, giinstiger Wind ;< (das aber besser zum selben *seik-, gr. 
5368:W orten far „Stange“ von einer Wz. *reik- gestellt (woneben *rSk- in dt. 
6825:eik- — eig-, oig- 
6850:eik- „zu eigen haben, vermogen“. 
8383:tjveiy.a dagegen Praep. ev + Wz. *seik- „langen“, s. d. und Boisacq 251 f. 
9425:aaO.) miiSte daneben ein idg. *ereik- angesetzt werden, welches evident 
9427:fiber die Benennung der „Nisse“ vgl. Wood IF. 18, 23 f. Zu idg. *ereik- 
14255:zur erw. Wz. *ueik-, van Helten ibd. 241 . 
14459:S. die Erweiterungen tteik- ueiy-, ueid-, y e ip- ucib-. vein- (viel-
```


## [2026-09-04T19:05:29.783Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^aes\\b\\|aes,\\? *-eris\\|aes  \" LEW_1910.txt | head -10; echo \"=== find aes ===\"; grep -n \"aes \" LEW_1910.txt | head -20"
}
```


### [2026-09-04T19:05:29.860Z] TOOL RESULT

```
=== find aes ===
374:portatu, portaia, portust II 345 purtiius, purtifile, purditom I 363 purtingus IL 142 purtuvitu, purtu- vies, purdovitu IT 325, 363 purome II 391 pure, porse II 404 puse, puset II 844 pusme II 404 pusnaes IT 335 pustin II 348 pusinaref II 335 posine II 335, 348, 361 putrespe II 845 puze II 844 ranu, randeme I 619 rehte II 424 reper II 430 restef, restatu II 597 revestu II 785 rt II 430 Rubiname II 445 Rufrer II 448 rufru, rufra IT 439, 445, 446, 448 ruseme II 449 sacri-, sakra, sacre IT 460 Sace, Sansio- II 474 salu II 106, 466 saluvom, salvom IT 472 sanes II 476 sarsite II 479 savitu II 483 skale¢eta, scalseto, scalsie I 138 scapla II 489 screhto, screthtor IT 499 seipodruhper II $45 semenies, sehme- nier, sehmeniar, sehemeniar II 512 semu Il 512 sent II 629 seples II 540
6405:parfa, parfaes IT 256
7307:huilliu (air.) IT 207 huisse (air.) I 733 humal (air.) I 664 humil (air. ) IT389 harda (air.) IT 391 sadam (air.) 17193, 215 tarar, -atr (mir.) IT 289 iarfargid (air., mir.) 17725, 824 tarmafoicht (air.) IT 824 war n, tarm- (air.) ,nach* IT 193 darn ,,Hisen‘* IJ 19 carrair, tarraim (mir.) IJ 289 tase (air.) IT 310 abt IT 739 abid (air.) I 103 tcarm (air.) I 716 tec (air.) [716 ar wchét (air.) IT 270 wcht I 716 tchtar (air.) I 686 wd (mir.) ,,Fessel* IT 294 wd (air.) Relativ- partikel J 670 adacht (mir.) I 25 adan (air.) IT 294 adnae (mir.) [725 of (air.) I 103 aw (air.) IT 328 dlach (air.) I 814 alar (air.) IT 328 aulé (air.) IT 316 amb- (air.) ,,um‘ 136 amb (air.) ,, Butter“ II 820 ambed (air.) IT 210 embel (mir.) IT 338 wmbithe (air.) IL787 amoblissvu (mnir.) I 510 wmbliu (air.) IT S14 wmhaes (air.) I 17 imlecan (air.) IT 814 amm-, imme- (air.) I 36
```


## [2026-09-04T19:05:36.034Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l LEW_1910.txt && head -5 LEW_1910.txt && sed -n '6845,6880p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-04T19:05:36.099Z] TOOL RESULT

```
14865 LEW_1910.txt
eae hee ne
ee
Duquesne University:
joe Kt re |
* ee . ¥
punkt, Schlu8werk“ (wfirde, wenn zutretfend, eher zu *id- zu stellen sein). 

Mhd. jan „Reihe, Gang £i , nhd. Jahn „Gang, Reihe gemahten Getreides“, 
schwed. mdartl. an ds. (Schade, Kluge 8 s. v., Liden Arkfnfil. 3, 243). 

eik- „zu eigen haben, vermogen“. 

Eine ausschliefilieh arisch-germ. Wurzel. 

Ai. fse, tste „hat zu eigen, besitzt, beherrscht“, Isnnd „vermogend, m. 
Herrscher“, tsvnrd- „vermogend, imstande; m. Gebieter“; av. is- „Ver- 
mogen, Reichturn“, isvun- „vermogend“, Uti- „Gut, Reichtum“ (germ, aihti-). 

Hierzu got. aigan ( aih , aigum, aihta) ,, haben, besitzen“, altn. eiga (a, 
cigom, dtt(i), ags. ft gun, afr. aga, as. cgnn, ahd. eigan ds. Partic. *aigana -, 
aigina- in der Bedeutung „eigen“ und substantiv. n. „Eigentum“ : altn. 
ekgiun , „eigen(tfimlich;“, ags. Gym (engl. own , afr. eg in, cin, as. cyan, ahd. 
eigan usw. ds. got. aigin n. „Eigentum“, altn. eig in, ags. ugen usvv. ds. 
Hiervon abgeleitet ist *aiganun : altn. eigna, -acla „zueignen“; ags. dgnian 
„zu eigen machen, besitzen“, weiter ahd. eigincn „zu eigen machen, an- 
eignen“ usw. 

G-Abstr. germ. *aihti- : got. ailits „Eigentum“, altn. cet, alt in der ab- 
strakteren Bedeutung „Geschlecht“ ; auch „HimmeIsgegend £I ; ags. celit, ahd. 
eht „Besitz, Eigentum“. S. weiter altn. eign f. „Eigentum an Grund und 
Boden“ (*<iig-ni- Vgl. Fick I 4 113, 177, 346, III 4 1. Falk-Torp 183, 184, 
1453. Feist GEW. 2 14, 15 (wo Aufzahlung anderer, abzulehnender Yer- 
mutungen). 

DaE! ir. irht „Kachkommenschaft, Stamm“ hierzu gehore, ist unwahr- 
scheinlich (Fick III 4 1, Feist aaO). 

eig-, oig- „laut jammern, klaglich bitten 1 '. 

gr. olxxog „das Bejammern, Erbarmen", oixxgd; ,, klaglich, erbiirmlich, 
elendiglich' 1 , oixitgco (aol. olxx(ggm) r bemitleiden, beklagen“ : got. aih/rin
```


## [2026-09-04T19:05:44.700Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%D9%87%D9%86/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for آهن — its definition and any bracketed origin tag such as [په.] (Pahlavi). Also quote the دهخدا (Dehkhoda) entry's etymological note if present."
}
```


### [2026-09-04T19:05:59.281Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T19:06:02.919Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"آهن\" MON_part1.txt | head -5; echo \"--- part2 ---\"; grep -n \"آهن\" MON_part2.txt | head -5; echo \"--- adena v1 ---\"; grep -c \"آهن\" incoming/MON/MON_2vol_Adena_v1_djvu.txt"
}
```


### [2026-09-04T19:06:03.025Z] TOOL RESULT

```
350:(لندن)؛ اشتار (پاریس)» آهنگ (دهلی)۰ آریانا (کابل) و نیز در سالنامه‌های 
809:جوشان: آب معدنی گازدار؛ آب آهن 
1085:اب پاش: *05-.2 (امر.) آلتی آهنی یا حلبی 
1267:برای سخت کردن آهن و آن فرو بردن فلز 
1469:حوضحه‌ای که از چینی يا آهن و مانند آن 
--- part2 ---
1192:آهنگ. خواهشی نهانی که غالا به قصد 
2046:آمر.) در همی از آهن و روی و جز آن که در 
2061:آهنگری و مسگری و غیره. 
2133:بند و زنجیر آهنین که به گیردن و دست 
2680:عم آهنج: 2201 -۰[ع- 4 - غم آهنجنده] 
--- adena v1 ---
409
```


## [2026-09-04T19:06:06.072Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^آهن\\|آهن\\. \\|(آهن)\\|آهن (اِ\" MON_part2.txt | head -20; echo \"===\"; sed -n '2050,2075p' MON_part2.txt"
}
```


### [2026-09-04T19:06:06.160Z] TOOL RESULT

```
1192:آهنگ. خواهشی نهانی که غالا به قصد 
2061:آهنگری و مسگری و غیره. 
12930:آهنگ چیزی کردن. ((مص.) مبانه‌روی. 
19413:آهنگ. شهوت. 
21095:آهنی سر کج و دسته‌دار که فیلبازان بدان فیل 
22855:آهنی سر کج و دسته‌دار که فلبانان بدان فبل 
24956:آهنگران و جز آنان آهن تفته را بدان 
25413:آهنی و نوک تبز دارای دسته‌ای چویین که 
26752:آهنین (عموماً). قلابی که قصابان بر آن 
27163:کنده: (6-)۲۵۸02 (.) کارد گاو آهن. 
27645:آهنین؛ شمو د. 
27916:آهنگری و مسگری. جابی که در آن خشت 
29173:گار: جع (.) استگاه قطار راه آهن. 
29652:آهن جفت» خیش» سیار» فدان. 
30312:آهنین بر دو طرف آن تعبیه کنند و ریسمانی 
31027:آهنی که بدان گوشت را کباب کنند یا نان 
33072:آهن‌دار که سابقا آن را از ارمنستان 
34649:آهنین با سر مدور پهن (که بر دروازه کوبند 
36977:آهن صاف به شکل ۲ يا با که برای محکم 
36985:آهنین: فانه‌ای که از آهن باشد. گوه چویین: 
===
خرخر کردن مذبوح و مخنوق. (.) بانگ 

شتر. بانگ بوز. (اح. از تسا 
منحو سه. 
غار: :۸5« (ع.| (ص.) آمرزگاره 
آمرزنده گناه؛ ج. غفارون. از صفات خدای 
تعالی. 

> [ ات آیکه تن 

مفاک» گودال, حفر ۵. شمشیر آندار. 7 
آهنگری و مسگری و غیره. 
* : ۵۲ [- خفح - خفج - خفچه] (.) 
دسته موی. شاخ راست و نا زکث. 
غفج کر دن: ۰۲( (مص م.) جدا کردن 
شاخه‌های راست و نازک و دسته کردن آنها 
تا سپس در لیف بیچند و در خاک کنند. 
غفجی: -[۰۲« [- غنچی] (حامص.) عمق» 
ژرفا» گودی. 
غفر: ۷ [ع (مص م.) بوشیدن چی را. 


غفران 

آمرزیدن گناه را. 
غفران: حقامر [غ.] (مص‌ل.) بوشیدن کناه
```


## [2026-09-04T19:06:11.566Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%A2%D9%87%D9%86",
 "prompt": "Quote the Mo'in (فرهنگ معین) dictionary entry for آهن verbatim, including any bracketed origin tag such as [په.] or [پهلوی]."
}
```


### [2026-09-04T19:06:15.512Z] TOOL RESULT

```
# Mo'in Dictionary Entry for آهن

According to the Mo'in (فرهنگ معین) dictionary shown on this page, the entry reads:

"(هُ) ( اِ.) آهون ، نقب"

This entry indicates the word آهن with pronunciation guides and related terms, though the full definitions are not elaborated in the displayed content.
```


## [2026-09-04T19:06:21.696Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"آهن\" incoming/MON/MON_2vol_Adena_v1_djvu.txt | grep -n \"فلز\\|عنصر\\|په\\.\" | head -10; echo \"=== alt ===\"; grep -n \"آهن\\s*[.:]\\?\\s*\\[\" incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -10"
}
```


### [2026-09-04T19:06:21.838Z] TOOL RESULT

```
4:1267:برای سخت کردن آهن و آن فرو بردن فلز 
24:5469:دورة فلزات. اين دوره از زمان پیدایش آهن 
149:34025:پیت: ؛آم (۱.) چلیک فلزی (آهنی با حلبی) 
242:61373:آلتی فلزی (معمولاً آهنین) که بر دست 
405:96657:پیدایش فلزات شروع و به دور آهن ختم 
=== alt ===
```


## [2026-09-04T19:06:29.719Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"AYAH\\|AYO-\\|ASIN\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-04T19:06:29.777Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:06:34.846Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"آهن\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY index around 2046 raw ===\"; sed -n '2016,2036p' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-04T19:06:34.903Z] TOOL RESULT

```
294:«شخم» و «آهن) و «جوه و «گاوه و «بز» و «خوکک» نشان می‌دهد که این مردم به کشاورزی هم اشتغال"
345:از دوران آهن تعلق دارد.
555:1300-5108078۸70) را نو آوری کرد. ضمناً آهنگ پیشرفت دانش زبانشناسی و پژوهش درباره
1115:(110178۸0078) شعر عشقی يا رزمی می‌سرودند و در بزم‌ها با صدای آهنگین می‌خواندند..
5311:چم کلی واژه‌های اين فهرست: دمیدن» دم آهنگری» بادکردگی» بادکردن؛ تاول.
14521:چم این واژه در زبان‌های اسلاوی و بالیتک و ژرمنی: پوست گوسفند؛ کیسه‌ی چرمی؛ دء آهنگری,
=== ARY index around 2046 raw ===
(OTHER) 126, ANTARS
ONIONS: (OTHER) 635
SKEAT: (OTHER) 417
AMINDAROV: (OTHER) 264
Pr seb ily
leatloal
Farce th oth shanty Soo 9 Sa 9 A Ng ees! SOILS 22 cal
WACKITWEI, EN-WACKEMAL (AVESTAN) esl
(OLD IRISH) oS 434) UXTA., VAC, A-VAXSH
FDAIM, FOCCUL ‘AWAZ, AVAC (PAHLAVI) 5 3h,
AASANSKRIT) ey Sail
REFERENCES tek] AVEC, VAVacA, VicavaTy, AVOcAM
POKORNY, —~=~=S~S*C«SMSSAALG OPA * GREER) pliy
DELAMARRE: (VOIX) 110 VOX, VOCARE. (LATIN) oa
‘MACKENZIE: (VOICE) 139 VOISER ERENCH) wij aq
BUCK: (VOICE) 1248 OLD SCANDINAVIAN) “Sissel ‘
2) 1 bu dy OMUN :
LATVIAN) (2) 33
leetloal
ashy 4 Sy
[pdf page 73]
```


## [2026-09-04T19:06:44.614Z] TOOL CALL #83: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D9%87%D9%86\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C3%A9yos\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C3%A1cw%C4%81\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/H%C3%A1yas\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ey%E1%B8%B1-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/aigan%C4%85\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/aiz\" \\\n \"https://www.etymonline.com/word/ore\" \\\n \"https://www.etymonline.com/word/era\" \\\n \"https://www.etymonline.com/word/own\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 40 (book p.10), roots Aik/Eik and Aios/Ayos: PIE roots, Av. ayah-, NP ahan, Gmc *aiganan/*aiz, English own/owe/ought/ore/era\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-04T19:06:49.353Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/39f07dcf09a8d1f1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/99b0f5fba39a65e1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e8f82be28cc4ef08.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ff4e32f6c24b44f6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/79c81df14fabefe5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6f63dd109a7a37f5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2b0be329618c727a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/488ffce4690754aa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d9605d573cec2e2c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9cbe127373677147.txt
```


## [2026-09-04T19:06:53.475Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -A12 -i \"Etymology\" 39f07dcf09a8d1f1.txt | head -40"
}
```


### [2026-09-04T19:06:53.529Z] TOOL RESULT

```
84: Etymology 
85-
86- 3.2 
87- Pronunciation 
88-
89- 3.3 
90- Noun 
91-
92- 3.3.1 
93- Derived terms 
94-
95- 3.3.2 
96- Descendants 
--
296: Etymology
297- [ edit ] 
298-
299- From Middle Persian [script needed] ( ʾh(y)n' /⁠āhan⁠/ , “ iron ” ) , from Proto-Iranian *Hácwā .
300-
301- Pronunciation
302- [ edit ] 
303-
304- ( Classical Persian ) IPA ( key ) : /ʔaː.ˈhan/ 
305-
306- ( Dari, formal ) IPA ( key ) : [ʔɑː.ɦän] 
307-
308- ( Dari, formal ) IPA ( key ) : [ʔɑː.ɦän]
```


## [2026-09-04T19:07:06.328Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'\\bORE\\b', t):\n    print(repr(t[m.start()-120:m.start()+60])); print('--')\nprint('=== ERA ===')\nfor m in re.finditer(r'\\bERA\\b', t):\n    print(repr(t[m.start()-100:m.start()+40])); print('--')\nEOF"
}
```


### [2026-09-04T19:07:08.202Z] TOOL RESULT

```
'o- probably from a root *aus-. Latin aurum (> French or), gold: AUREATE, AUREOLE, AURIC; AURIFEROUS, DORY?, EYRIR, OR’, ORE, ORIFLAMME, ORIOLE, ORMOLU, OROIDE, OR- PHREY, ORPIMENT.'
--
'ID ergh- ORDAIN  a\x0cr- ORDEAL dail- ORDER ar- ORDINAL ar- ORDINANCE ar- ORDINARY ar- ORDINATE ar- ORDO ar-\nORDURE ghers- ORE aurum\nORGAN werg- ORGANOLEPTIC (s)lag¥- ORGANON werg- OR'
--
=== ERA ===
'liest: ERST. [Pok. ajer- 12.] ayes-. A metal, copper\x0c or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.] baba-. Root imitat'
--
' gealla, gall: GALL!. 2. Suffixed o-grade form *ghol-& in Greek kholé, bile: CHOLE-, CHOLER, (CHOL- ERA); ACHOLIA, MELANCHOLY. 3. Suffixed f'
--
'tended form *keras-. 1. Greek keras, horn: CARAT, CERASTES, KERATO-; CERATODUS, (CERATOID), CHELIC- ERA, CLADOCERAN, KERATIN, RHINOCEROS, TR'
--
'UIPONDERATE (S)pen-\nEQUISETUM ekwo- EQUITANT ekwo- EQUITATION ekwo- EQUIVALENT wal- EQUIVOCAL wekw- ERA ayes- ERADICATE wrad- ERASE réd-\nERE'
--
```


## [2026-09-04T19:07:47.039Z] AGENT

Now I'll write the verification file.


## [2026-09-04T19:12:09.731Z] TOOL CALL #86: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-40.json <<'JSONEOF'\n{\n  \"pdf_page\": 40,\n  \"book_page\": 10,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Aik, Ěik\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂eyḱ- 'to appropriate, possess, be master of' (Pokorny ēik- 298; Watkins/AHD ēik-)\",\n      \"note\": \"Root, language label and gloss are all right. Pokorny IEW 298-299 heads the entry 'eik- ‚zu eigen haben, vermögen‘'; Walde-Pokorny I 105 adds the important observation that it is 'eine ausschließlich arisch-germ. Wurzel' — i.e. exactly the two branches (Indo-Iranian and Germanic) that Nourai draws, and no others. Watkins (AHD 1985) writes it 'ēik-. To be master of, possess. [Pok. ēik- 289]' (the '289' is a misprint or a scan misreading for 298). Modern Wiktionary reconstructs *h₂eyḱ- 'to appropriate, possess', with the a-vocalism of Germanic and Tocharian explained as a pervasive o-grade; Nourai's double citation form 'Aik, Ěik' reflects exactly this old a-/ē- ablaut notation. One caveat carried into node #1: Nourai's gloss 'wealthy' for Av. isvan- comes from Klein (p.1106 'isvan-, ‘well off, rich’'); Bartholomae AiW glosses isvan- 'verfügend, Herr über-, der (es) vermag' — 'able, having power over', not 'rich'.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ey%E1%B8%B1-\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/aigan%C4%85\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:298\", \"status\": \"supports\", \"note\": \"POK_01.txt ƒƒ-leaf 311 (printed pp. 298-300) carries the entry 'eik- ,zu eigen haben, vermögen‘. Ai. ī́śe, ī́ṣṭe ... ,hat zu eigen, besitzt, beherrscht‘ ... av. iše ,ist Herr über‘, isvan- ,vermögend‘, išti- ,Gut, Reichtum‘ (germ. aihti-), aēšā- ,Vermögen; Habe‘. Hierzu got. *aigan (aih, aigum...) ,haben, besitzen‘'. The page number 298 is right (the entry begins on p.298; the running number 299 falls inside it).\"},\n        {\"ref\": \"KLN:1106\", \"status\": \"supports\", \"note\": \"KLN_1966.txt ƒƒ-leaf 591, which carries the printed page numbers 1106/1107, has s.v. 'owe': 'fr. I.-E. base *aik-, ‘to own’, whence also OI. ī́śe, ‘he owns’, ... Avestic is-, ‘riches, fortune’, isvan-, ‘well off, rich’. Cp. ought, aux. v., own, adj. and v.' — Klein's base *aik- is literally Nourai's root name and gloss.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"Bd. I p. 298-299 (POK_01.txt leaf 311)\", \"stance\": \"supports\", \"note\": \"'eik- ,zu eigen haben, vermögen‘' with the Avestan and Germanic material Nourai charts.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 105 (WLD_Bd1_1930_dli_70244_djvu.txt line 6850)\", \"stance\": \"supports\", \"note\": \"'eik- „zu eigen haben, vermögen“. Eine ausschließlich arisch-germ. Wurzel.' — confirms the root and, incidentally, that no Latin/Greek branch belongs here.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. ēik-\", \"stance\": \"supports\", \"note\": \"'ēik-. To be master of, possess. 1. Germanic *aigan, to possess, in Old English āgan, to possess: OUGHT¹, OWE. 2. Germanic participial form *aiganaz ... OWN.'\"},\n        {\"src\": \"KLN\", \"where\": \"vol. II p. 1106 s.v. owe\", \"stance\": \"supports\", \"note\": \"I.-E. base *aik- 'to own', with OI. ī́śe and Avestic is-, isvan-.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"îs, îše, îšti, âěšâ 1; îsvan, išvan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All four forms are genuine Avestan continuations of PIE *h₂eyḱ-. The verb is Bartholomae's aēš- 'Herr sein über—' (AiW s.v.), a stative middle whose 3sg. is aēšē/išē 'he is master of, disposes of' — formally the Indo-Iranian perfect-stative matching Skt. ī́śe (< reduplicated *h₂e-h₂óyḱ-e), the same formation that Germanic continues in the preterite-present *aih 'I possess'. Nourai's 'îs, îše' are the zero-grade stem īš- and that 3sg. īšē; 'îšti' is the ti-abstract *Híḱ-ti- > Av. išti- f., which Bartholomae glosses '‘Vermögen, Können, Kraft’; ‘Habe, Besitz, Gut, Reichtum’' — the exact equivalent of Gothic aihts and Old English ǣht; 'âěšâ' is the full-grade *h₂oyḱ-eh₂- > Av. aēšā- 'Vermögen, Habe'; 'isvan-' is the van-adjective *Híḱ-uen- 'having power over'. The trailing '1' after 'âěšâ' is not part of the word — it is a stray superscript reference numeral picked up in the transcription. One gloss is loose: Nourai's 'wealthy' for isvan- is Klein's rendering, whereas Bartholomae gives 'verfügend, Herr über-' / 'der (es) vermögt', i.e. 'able, in command of'.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ey%E1%B8%B1-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:298\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 311: 'av. iše ,ist Herr über‘, isvan- ,vermögend‘, išti- ,Gut, Reichtum‘ (germ. aihti-), aēšā- ,Vermögen; Habe‘' — all four of Nourai's words, in his order.\"},\n            {\"ref\": \"KLN:1106\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 591 s.v. owe: 'Avestic is-, ‘riches, fortune’, isvan-, ‘well off, rich’' — the source of Nourai's gloss 'wealth' / 'wealthy'.\"},\n            {\"ref\": \"SYN:771,772\", \"status\": \"supports\", \"note\": \"SYN.txt §11.41 PROPERTY, p.771: 'Av. išti- ‘power, possession, property, wealth’ (Barth. 376) : Goth. aihts, etc., above, 4'; §11.42 WEALTH, RICHES p.772 lists 'Av. šaēta-, išti-' in its table and repeats 'Skt. dhana-, vasu-, rai-, Av. išti, see ‘property’.' Both cited pages really do carry Av. išti- 'wealth'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW s.v. aēš- (BRT.txt line 2702), isvan- (line 7998), išti- (line 8047)\", \"stance\": \"partial\", \"note\": \"'aēš- V. ‘Herr sein über —’ ... Nur Med. 1) ‘Herr sein, verfügen über-’'; 'isvan- Adj. ‘verfügend, Herr über-’ ... ‘der (es) vermögt’'; 'išti- f. 1) ‘Vermögen, Können, Imstandsein, Kraft’ ... 2) ‘Vermögen sva. Habe, Besitz, Gut, Reichtum’.' Forms confirmed; but Bartholomae's isvan- is 'able/in command', not 'wealthy'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 105\", \"stance\": \"supports\", \"note\": \"'av. iš- „Vermögen, Reichtum“, isvan- „vermögend“, išti- „Gut, Reichtum“ (germ. aihti-)'.\"},\n            {\"src\": \"KNT\", \"where\": \"Old Persian lexicon\", \"stance\": \"silent\", \"note\": \"No Old Persian reflex of this root is listed by Kent; the root is attested in Iranian only in Avestan, so the chart's 'Avestan' label is the right one.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §11.41, p. 771\", \"stance\": \"supports\", \"note\": \"Av. išti- 'power, possession, property, wealth', explicitly equated with Goth. aihts.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Germanic\",\n          \"words\": \"aigan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *aiganą 'to possess' is a preterite-present verb: the PIE stative perfect *h₂e-h₂óyḱ-e (the same formation as Skt. ī́śe, Av. išē) was reanalysed in Germanic as a present, whence Gothic aih (1/3sg.), aigum (pl.), with a secondarily built weak preterite aihta. From it: Gothic aigan, Old Norse eiga, Old English āgan, Old Frisian āga, Old Saxon ēgan, Old High German eigan (> German eigen). Grimm's Law gives PIE *-ḱ- > Gmc *-h- in the plural/preterite stem (*aihum, *aihta), while the singular *aih preserves the same consonant; the diphthong ai is the Germanic reflex of the PIE o-grade *h₂oy-.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/aigan%C4%85\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. ēik-: '1. Germanic *aigan, to possess, in Old English āgan, to possess: OUGHT¹, OWE.' Nourai's bare 'AHD' citation (no page) points at the Indo-European Roots appendix, and the appendix does give precisely the form *aigan with the gloss 'to possess'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 299\", \"stance\": \"supports\", \"note\": \"'Hierzu got. *aigan (aih, aigum, sekund. Prät. aihta) ‘haben, besitzen’, altn. eiga, ags. āgan, afries. āga, asāchs. ēgan, ahd. eigan.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 105\", \"stance\": \"supports\", \"note\": \"Same Germanic paradigm, plus the participle *aigana-/aigina- 'eigen' and the abstract *aihti- 'Eigentum'.\"},\n            {\"src\": \"KLN\", \"where\": \"vol. II p. 1106 s.v. owe\", \"stance\": \"supports\", \"note\": \"'rel. to OFris. aga, ON. eiga, Swed. äga, OHG. eigan, Goth. aigan, ‘to possess, have’.'\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Owe (SKT.txt line 12940 ff.)\", \"stance\": \"supports\", \"note\": \"'A.S. āgan, to have ... Icel. eiga, Dan. eje, Swed. äga, O.H.G. eigan, Goth. aigan, to possess. Allied to Skt. īś, to possess.'\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"own, owe, ought\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are Old English āgan and its parts. (a) owe: OE āgan 'to have, possess' > ME owen, awen; the modern sense 'be in debt' is a late-OE/early-ME specialisation from 'to have (something belonging to another)'. (b) own (adj.) is OE āgen, originally the past participle of āgan, 'possessed (by)', ME owen/awen, contracted to own by loss of medial -g-; the verb own is OE (ge)āgnian 'to take possession of', ME ahnien, largely obsolete by 1300 and revived in the early 17th c. partly as a back-formation from owner. (c) ought is the old preterite of āgan, OE āhte 'possessed, owed' > ME aughte, oughte, which detached itself from owe and became an independent modal of obligation. The initial /oː/ in all three is the regular development of OE ā in southern Middle English.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/own\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; the derivation is a standard English-etymology commonplace and is covered by Klein p.1106, Skeat and the AHD appendix cited at the parent node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"vol. II p. 1104-1107 s.vv. ought, owe, own\", \"stance\": \"supports\", \"note\": \"'ought ... fr. OE. āhte ... past tense of āgan, ‘to own, possess’; hence prop. past tense of owe'; 'own, adj. — ME. owen, awen, fr. OE. āgen, ‘own’, lit. ‘possessed by’, prop. pp. of āgan'; 'own, tr. v. — ME. ohnien, ahnien, fr. OE. āgnian'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.vv. Owe / ought / own (SKT.txt lines 12940-12957)\", \"stance\": \"supports\", \"note\": \"'ought. The pres. tense of A.S. āgan is ic āh, really an old pt. tense; hence was formed the pt. t. āhte, M.E. aughte, oughte'; 'own (1) ... A.S. āgen, own, orig. pp. of āgan, to possess'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ēik- and index (ERA/OUGHT entries)\", \"stance\": \"supports\", \"note\": \"OUGHT¹, OWE and OWN are all listed as derivatives of ēik- via Germanic *aigan / *aiganaz.\"},\n            {\"src\": \"Etymonline\", \"where\": \"entry 'own'\", \"stance\": \"supports\", \"note\": \"'from Old English agen ‘one’s own’, literally ‘possessed by’, from Proto-Germanic *aiganaz ... from PIE root *aik- ‘be master of, possess’'; the same entry covers owe and ought.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Aios, Ayos\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂éyos (n., s-stem) 'a metal: copper, bronze' (Pokorny aios- 15; Watkins/AHD ayes-)\",\n      \"note\": \"Root, label and gloss are right; Pokorny's own gloss is more precise — 'Metall, u. zw. wohl ‚Kupfer („brandfarbig“?), Bronze‘; im Arischen auch ‚Eisen‘' — which is exactly the Indo-Iranian 'metal → iron' shift the chart depends on. NOURAI'S ROOT NOTE ('KLN:1093 claims that this word may have been derived from “Ayashya”, ancient name of Cyprus, meaning Cyprus metal') is an accurate report of Klein, who writes s.v. ore: 'fr. I.-E. *ayos-, which is perh. a derivative of Ayashya, later form of Alashya, ancient name of Cyprus, hence I.-E. *ayos would have meant orig. ‘the Cyprian metal’.' The idea is Pokorny's (KZ 46, 292 f.), relayed by Walde-Pokorny I 4 ('idg. aios alte Entlehnung aus Alas(ja), dem alten Namen von Kypros') and by Mann IEC 332 ('J. Pokorny and others refer this word to Alasia (Ayasia), an ancient name of Cyprus'). MODERN SCHOLARSHIP DOES NOT FOLLOW IT: current handbooks and Wiktionary treat *h₂éyos as an inherited PIE s-stem and use it as evidence that PIE was spoken while copper was in use; Pokorny himself already presents the Cyprus derivation as a conjecture, and the chronology (Alashiya is attested only from the 2nd millennium BCE, long after the Indo-Iranian/Italic/Germanic split implied by the cognate set) tells against it. Buck §9.66 and Ernout-Meillet reconstruct it without any Cyprus loan. Nourai reports the claim as Klein's rather than adopting it, which is the correct handling. Separately: the whole Iranian branch of this chart (nodes #2-#3) rests on an equation that modern Iranian scholarship rejects — see node #2.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C3%A9yos\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/H%C3%A1yas\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:15\", \"status\": \"supports\", \"note\": \"POK_01.txt ƒƒ-leaf 23, which carries the printed page number 15: 'aios- ,Metall‘, u. zw. wohl ,Kupfer („brandfarbig“?), Bronze‘; im Arischen auch ,Eisen‘. Ai. áyas- n., av. ayaŋh- n. ,Metall, Eisen‘; lat. aes, g. aeris; got. aiz (urgerm. *a(i)iz- = idg. *aies-) ,Erz, Geld‘, ahd. ēr ,Erz‘, anord. eir n. ,Erz, Kupfer‘.' Watkins independently confirms the page: '[Pok. aios- 15.]'\"},\n        {\"ref\": \"KLN:1093\", \"status\": \"supports\", \"note\": \"KLN_1966.txt ƒƒ-leaf 584, printed page 1093, s.v. 'ore, n.': 'ME. oor, or, fr. OE. ār, ǣr, ‘brass’, rel. to ON. eir, ... Goth. aiz, ‘bronze’, and cogn. with OI. áyah (gen. áyasah), Avestic ayō (gen. ayaŋhō), L. aes, gen. aeris, ‘brass’, fr. I.-E. *ayos-, which is perh. a derivative of Ayashya, later form of Alashya, ancient name of Cyprus, hence I.-E. *ayos would have meant orig. ‘the Cyprian metal’.' Nourai's root note quotes this claim correctly, page and all.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"Bd. I p. 15\", \"stance\": \"supports\", \"note\": \"See the quotation above; Pokorny's entry is the source of the whole cognate set Nourai charts.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 4 (WLD_Bd1_1930_dli_70244_djvu.txt line 431 ff.)\", \"stance\": \"supports\", \"note\": \"'aios- „Metall“ u. zw. wohl „Kupfer („brandfarbig“?), Bronze“: im Arischen auch „Eisen“. Ai. ayas- n., av. ayaŋh- n. „Metall, Eisen“; lat. aes, g. aeris; got. aiz ... Nach Pokorny KZ. 46, 292 f. ist idg. aios alte Entlehnung aus Alas(ja), dem alten Namen von Kypros.'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ayes-\", \"stance\": \"partial\", \"note\": \"'ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.]' — root and gloss confirmed, but Watkins lists only the Latin branch under this root (see node #7).\"},\n        {\"src\": \"IEC\", \"where\": \"Mann col./p. entry 'aios' (IEC.txt line 332)\", \"stance\": \"supports\", \"note\": \"'aios, -es- “metal, bronze, ore”. WP I, 4. Skt. áyas; Av. ayáh-; Lat. aes; Umb. ahes-; Go. aiz; ON eir; MHG er. (Note: J. Pokorny and others refer this word to Alasia (Ayasia), an ancient name of Cyprus)' — independently confirms both the root and that the Cyprus idea is Pokorny's, reported as a note.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck §9.66 COPPER, BRONZE, pp. 611-612\", \"stance\": \"supports\", \"note\": \"'1. IE *ayes-. Walde-P. 1.4. Ernout-M. 19. Walde-H. 1.19. Lat. aes, gen. aeris ...; Goth. aiz, ON eir, OE ār, OHG ēr; Skt. ayas-' — no Cyprus loan is entertained.\"},\n        {\"src\": \"KLN\", \"where\": \"vol. II p. 1093 s.v. ore\", \"stance\": \"supports\", \"note\": \"Full cognate set plus the Alashya/Ayashya conjecture, referred to Walde-Hofmann LEW I 19 s.v. aes.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"ayô, ayah, ayanh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"One word in three case-forms of a neuter s-stem, not three words: Proto-Indo-Iranian *Háyas (= Skt. áyas-) > Avestan nom./acc. sg. ayō, stem ayah-, oblique/derivational stem ayaŋh- (gen. ayaŋhō), where the intervocalic *-s- of the weak cases became -ŋh- by the regular Avestan development *s > h with nasal colouring after a. Bartholomae lemmatises it 'ayah- n. ‘Metall (Eisen)’', with the derivative ayahāēna- 'metallen, eisern'. The gloss 'metal, bronze' is right for the older layer: Buck notes that Av. ayah- must have meant 'bronze' because of its epithets 'yellow, golden', and only later 'iron' — in Gathic Avestan it names the molten metal-stream of the last judgement (Y. 30.7, 32.7, 51.9 ayaŋhā xšustā 'with molten metal').\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/H%C3%A1yas\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C3%A9yos\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:15\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 23 (printed p.15): 'Ai. áyas- n., av. ayaŋh- n. ,Metall, Eisen‘ ... Davon av. ayahāēna- ,metallen, eisern‘.'\"},\n            {\"ref\": \"KLN:1093\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 584 s.v. ore: 'cogn. with OI. áyah (gen. áyasah), Avestic ayō (gen. ayaŋhō), L. aes, gen. aeris' — Klein gives exactly Nourai's two forms ayō and ayaŋh(ō).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW col. 156 s.v. ayah- (BRT.txt line 4909)\", \"stance\": \"supports\", \"note\": \"'j., g. ayah- n. ‘Metall (Eisen)’' with the Gathic passages for the molten-metal ordeal; 'ai. ayas- n.' given as the cognate. Also 'ayahō.zasta- Adj. ‘mit metallenen (eisernen) Klauen’' (line 4868).\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §9.66, p. 612\", \"stance\": \"supports\", \"note\": \"'Av. ayah- ‘bronze’ (as shown by epithets ‘yellow, golden’; cf. Geiger, Ostiran. Kultur 148), later ‘iron’ as NPers. āhan.' Also §9.67 IRON lists 'Av. ayah-'.\"},\n            {\"src\": \"AVG\", \"where\": \"Jackson, Avesta Grammar (s-stem declension)\", \"stance\": \"silent\", \"note\": \"Grepped for ayah-/ayaŋh-; the grammar's paradigm sections do not cite this noun by name, so no confirmation of the individual case-forms from this book.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 4\", \"stance\": \"supports\", \"note\": \"'av. ayaŋh- n. „Metall, Eisen“ ... Davon av. ayahhaena- „metallen, eisern“.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"âsîn, âhěn\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The two Middle Persian forms are real and correctly cited: the Book-Pahlavi spelling is <ʾ(y)n'/ʾs(y)n'>, read āsēn by Nyberg and āhan by MacKenzie, with Manichaean MP ʾhwn confirming the pronunciation with -h-; Nourai's doublet 'āsīn, āhēn' simply records the written vs. spoken form. WHAT IS DISPUTED IS THE ARROW from Avestan ayah-. Nourai follows an old equation that goes back to the Pahlavi Zand: Bartholomae (AiW 156) notes that the Pahlavi translators render Av. ayah- by āsīn 'Eisen' (and āsēn dēg 'iron kettle'), and Mo'in's footnote in Borhan-e Qate' p.70 repeats it — but a Zand translation-equivalent is a lexical gloss, not a sound-law descent. Phonologically ayah- could not give āsīn/āhēn: there is no source for the -s-/-h- or the -ēn. Hübschmann already said so flatly (Persische Studien no. 57, p.10): 'Die Etymologie von āhan ‘Eisen’ bleibt dunkel. Für das Altpersische wäre, nach phl. āsīn zu urteilen, etwa *asaina- anzusetzen' — i.e. an Old Persian *āsa(i)na-, not *ayah-. The modern reconstruction (Bailey, Dictionary of Khotan Saka 1979; Morgenstierne 2003; Rastorgujeva-Edelʹman ESIJa; Buyaner 2020) is Proto-Iranian *Hácwā ~ *Hcunáh 'iron, ironstone' (< PIE *Héḱ-wō, probably to *h₂eḱ- 'sharp'), which yields Khotanese hīśśanä, Pashto ōspəna/wəspəna, Wakhi išn, Kurdish hesin/asin, Baluchi āsin and, in the Southwest, MP āsēn/āhan — Old Persian *θ giving Middle Persian written <s> but spoken h, exactly the alternation Hübschmann documents (āhan : phl. āsīn, cf. panjāh, gunāh). Horn's entry no. 57, which Nourai cites, gives the Pahlavi form but pointedly does NOT derive it from ayah-, and calls the relation to Pashto ōspana / Ossetic æfsæn 'nicht aufgeklärt'.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C3%A1cw%C4%81\",\n            \"https://en.wiktionary.org/wiki/%D8%A2%D9%87%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:70\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol. 1 p.70 = archive.org borhan-ghate-v1 leaf n280 (page identified by the foot-notes 'بقیه در صفحهٔ ۷۰' on the preceding leaf and 'بقیه از صفحهٔ ۶۹' on this one). Mo'in's footnote 2 to آهن, read from the page image and saved to data/verification/sources/refs/ocr/BQT/70.vision.txt: '۲ ـ اوستا ـ ayah، در ترجمه و تفسیر پهلوی âsênên «بارتولمه ۱۵۶»، پهلوی ایضاً asin «دهارله ۱۸۸» و âhên «نیبرگ ۱۳۵ـ۶» ...' — i.e. Avestan ayah, Pahlavi āsīn and āhēn, exactly Nourai's arrow and exactly his two transliterations.\"},\n            {\"ref\": \"HRN:14\", \"status\": \"partial\", \"note\": \"HRN.txt ƒƒ-leaf 36 (printed p.14) no. 57: 'āhen ‘Eisen’; āhenīn ‘eisern’. Semn. ōsūn; g. vuhen. phlv. āsīn (z. B. vd. 5,121), āsīnīn ‘eisern’. kurd. hasin ~ hesin, ūsin ‘Eisen’; bel. LW. ahin.' Horn gives Nourai's Pahlavi forms, but offers NO Avestan etymon at all and adds 'Das Verhältniss zu afgh. ōspana, ōspīna; oss. äfsan ... ist nicht aufgeklärt' — so the page supports the word, not the arrow from ayah-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p. 5 s.v. āhan (PHD.txt line 181)\", \"stance\": \"partial\", \"note\": \"'āhan [ʾ(y)nʹ, ʾs(y)nʹ | M ʾhwn, N ~] iron. ~ēn [ʾsynynʹ] iron, of iron. ~gar blacksmith. ... āhen = āhan, q.v.' — both of Nourai's forms are there, with no etymology given.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, Glossary s.v. āsēn (NYB_vol2_glossary.txt line 686)\", \"stance\": \"partial\", \"note\": \"'āsēn [ʿsynʹ] iron 110⁵. — MPrth ʾswn; MPrs ʾhwn (List 79); Paz. āhin(-sāxt) (Aog.); NP āhan. Cf Benveniste, MSL 23, 1927, 132 sq.; 30, 1930, 60.' Confirms the forms and the line to NP āhan; no Avestan ayah- is invoked.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 57, p. 10 (HUB.txt line 233) and p. 143 (line 4989), p. 148 (line 7517)\", \"stance\": \"contradicts\", \"note\": \"'Die Etymologie von āhan ‘Eisen’ bleibt dunkel. Für das Altpersische wäre, nach phl. āsīn zu urteilen, etwa *asaina- anzusetzen, wozu auch bal. āsin, kurd. hasin (= asina-?) stimmen, während afgh. ōspīna, ospana, osset. āfsān, pamirdial. spin ein iran. *aspaina-, resp. *spaina- voraussetzen?' Elsewhere: 'āhan ‘Eisen’ = phl. āsīn (resp. āsēn)' in the list of Persian h corresponding to Old Persian θ / Pahlavi s. This is a direct rejection of an ayah- etymology.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW col. 156 s.v. ayah-, Pü. section\", \"stance\": \"partial\", \"note\": \"'Pü.: āsīn ‘Eisen’, (zu Y.9): āsēn dēg ‘eiserner Kessel’' — Bartholomae records only that the Pahlavi version TRANSLATES Av. ayah- by āsīn; he asserts no genetic derivation. This is the origin of the equation Mo'in and Nourai repeat.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"Etymological Dictionary of the Iranian Verb\", \"stance\": \"silent\", \"note\": \"Grepped for āhan/āsēn and *aiš; nothing found — the work covers verbs only, and 'iron' is a noun.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"Âhan «آهن»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian آهن āhan 'iron' is the straightforward continuation of the Middle Persian word of node #2: MP āhan/āhēn (Manichaean ʾhwn, Book-Pahlavi <ʾs(y)nʹ>) > early NP āhan, with regular shortening/lowering of the MP -ē- in the final unstressed syllable (āhēn > āhan, exactly as Hübschmann's rule 'mit a für ī (ī, e)' describes), the -h- being the Southwest-Iranian outcome of the same segment written <s> in Book Pahlavi. The extended sense 'anything hard' that Nourai gives is well attested and is the basis of the compounds Borhan-e Qate' lists on the same page (آهن‌دل 'iron-hearted', آهنین جان 'of iron constitution'), and of Sa'eb's line quoted in the chart, آهن دلان به آه ملایم نمی‌شوند. Borhan itself glosses it معروفست 'well known' and adds 'و شمشیر و تیغ را نیز آهن گویند' (sword and blade are also called āhan). The edge #2 → #3 is beyond doubt; what is not is the edge #1 → #2 above it (see node #2), so the word's ultimate ancestor is Proto-Iranian *Hácwā 'iron', not *Háyah.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A2%D9%87%D9%86\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C3%A1cw%C4%81\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:70\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol.1 p.70 (leaf n280) headword: 'آهن ـ بفتح الف و سکون نون، معروفست. ـ و شمشیر و تیغ را نیز آهن گویند' with Mo'in's footnote 2 giving Avestan ayah / Pahlavi āsīn, āhēn and the dialect forms (Semnani āsun, Sangesari ahän, Gilaki āhin, Natanzi āhon). Transcription saved at data/verification/sources/refs/ocr/BQT/70.vision.txt.\"},\n            {\"ref\": \"SYN:612\", \"status\": \"supports\", \"note\": \"SYN.txt §9.66, printed p.612: 'Av. ayah- ‘bronze’ ... later ‘iron’ as NPers. āhan.' Buck's page 612 says precisely what Nourai's chart says (and shares its now-superseded etymology).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Horn no. 57, p. 14\", \"stance\": \"supports\", \"note\": \"'āhen ‘Eisen’; āhenīn ‘eisern’ ... phlv. āsīn' — the NP word and its MP antecedent, with Kurdish hasin/hesin and Baluchi āhin.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien pp. 10, 143, 148\", \"stance\": \"partial\", \"note\": \"Confirms NP āhan = phl. āsīn/āsēn and the vowel development, but rejects any Avestan ayah- source ('bleibt dunkel').\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 1 p. 70 (Mo'in's footnote 2)\", \"stance\": \"supports\", \"note\": \"See ref_check; also gives the Iranian dialect spread āsun / ahän / āsân / asän / āhin / āhan / āhon.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā, entry آهن (ARY_latin_index_pages.txt [pdf page 73] = printed p.74)\", \"stance\": \"supports\", \"note\": \"Groups 'AYAH, AYO- (AVESTAN) / ASIN, AHEN, ASENEN (PAHLAVI) / AHAN (PERSIAN) / HESIN (KURDISH) / AYAS (SANSKRIT) / AES, AIS (LATIN) / AIZ, EISARN (GOTHIC) ...' with REFERENCES: POKORNY, BARNHART (IRON) 544, MACKENZIE (IRON), BUCK 613, ONIONS (IRON) 485, SKEAT (IRON) 308 — an independent modern Persian work that reproduces Nourai's chain exactly (and, like him, follows the older Bartholomae/Buck view).\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, s.v. آهن\", \"stance\": \"silent\", \"note\": \"The local OCR of Mo'in (MON_part1/part2 and the 2-vol Adena scan) does not contain a clean آهن headword entry, and vajehyab's Mo'in lookup returns only the homograph آهُن 'آهون، نقب' (tunnel). Mo'in's own etymological opinion is however available in full through his footnotes to Borhan-e Qate' (BQT:70), quoted above.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p. 5\", \"stance\": \"supports\", \"note\": \"'āhan ... | M ʾhwn, N ~' — the 'N ~' notation means the New Persian form is identical, i.e. NP āhan directly continues the MP word.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"aes; aera\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin aes, gen. aeris 'bronze, copper; money' is the regular Italic reflex of the PIE s-stem *h₂éyos: Proto-Italic *aos > Old Latin ais > classical aes, with the oblique stem *ayes- > *aiez- > aer- by rhotacism (aeris). Its antiquity in Italic is guaranteed by the derived adjective aenus/ahenus < *ayes-no-, matching Umbrian ahesnes and Avestan ayahāēna-. Because early Roman money was reckoned in bronze (aes grave, aes signatum, aes alienum 'debt'), aes came to mean 'money, cash'. The neuter plural aera was used for 'the individual items of a reckoning, counters'; this plural was then reinterpreted as a feminine singular aera 'a number, a figure', and in Late Latin (attested from 5th-c. Spain, whence the 'Spanish Era' dating from 38 BCE) it acquired the sense 'fixed point from which time is reckoned, era'. Both of Nourai's glosses — 'counters for counting' and 'an era of time' — are exactly Ernout-Meillet's two senses.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/era\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:443\", \"status\": \"not_checked\", \"note\": \"Page 443 of the AHD New College Edition is a main-dictionary page (it would be the entry 'era'), not part of the Indo-European Roots appendix; the 1970s AHD scans on archive.org are lending-only and their djvu text returns 401, so the page itself could not be read. The corresponding statement in the appendix IS accessible and agrees: AHD_watkins1985.txt s.v. ayes-: 'Latin aes, bronze, money: AENEOUS, ERA.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.vv. aes and aera (LAT.txt lines 1753, 1800)\", \"stance\": \"supports\", \"note\": \"'aera, -ae (era) f. (sans doute pluriel de aes, aeris considéré comme un féminin singulier): 1° nombre, chiffre (sens qu'avait le n. pl. aera) ... 2° “ère” ... Mot de basse époque'; 'aes (anc. ais), aeris n.: bronze ... Spécialisé bientôt dans le sens “monnaie, argent” ... L'ancien adjectif dérivé est aenus, ahenus, issu de *ayes-no-s, cf. ombr. ahesnes.'\"},\n            {\"src\": \"KLN\", \"where\": \"vol. I, s.v. era (KLN_1966.txt line 13505)\", \"stance\": \"supports\", \"note\": \"'era, n. — Late L. aera, ‘era’, fr. L. aera, ‘counters; items of calculation, money’, pl. of aes, ‘brass’. See ore.' — verbatim Nourai's gloss for aera.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §9.66 p. 611 and §11.43 p. 773\", \"stance\": \"supports\", \"note\": \"'Lat. aes, gen. aeris (cf. aenus, ahenus, fr. *ayes-no-, Umbr. ahesnes)'; and 'Lat. aes ‘bronze’ (9.66), hence, since the early coins were of bronze, ‘money’.'\"},\n            {\"src\": \"LEW\", \"where\": \"Walde LEW (LEW_1910.txt)\", \"stance\": \"silent\", \"note\": \"The local copy is an unusable OCR consisting mostly of the index volume; s.v. aes could not be located. Klein's citation 'see Walde-Hofmann, LEW., 1, 19 s.v. aes' shows this is where the Cyprus conjecture is discussed.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"era\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Borrowed in the early 17th c. from Late Latin aera 'era' (see node #4), itself Latin aera, the plural of aes taken as a feminine singular 'number, counter'. The chronological use starts in Visigothic Spain, where documents are dated by the 'Spanish Era' (era of 38 BCE); English first has it in the sense 'system of chronological notation' (1640s), then 'the starting point of an age' (1716), then 'a historical period' (1741, e.g. the Era of Good Feeling, 1817). No sound change is involved: Latin aera was simply taken over, with the learned pronunciation giving /ˈɪərə/, later /ˈɛrə/ in American English.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/era\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai cites nothing for this node; the parent node's AHD:443 and Klein s.v. era cover the claim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"vol. I s.v. era\", \"stance\": \"supports\", \"note\": \"'era, n. — Late L. aera, ‘era’, fr. L. aera, ‘counters; items of calculation, money’, pl. of aes, ‘brass’.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Era (SKT.txt line 5953)\", \"stance\": \"supports\", \"note\": \"'Era. (L.) L. aera, a fixed era. From a particular sense of aera (for calculation), pl. of aes, brass.' (OCR of this line is damaged but the sense is unambiguous.)\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, index and s.v. ayes-\", \"stance\": \"supports\", \"note\": \"Index: 'ERA ayes-'; entry: 'ayes- ... Latin aes, bronze, money: AENEOUS, ERA.'\"},\n            {\"src\": \"Etymonline\", \"where\": \"entry 'era'\", \"stance\": \"supports\", \"note\": \"'from Late Latin aera ... probably identical with Latin aera ‘counters used for calculation’, plural of aes (genitive aeris) ‘brass, copper, money’.'\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Germanic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box standing for Proto-Germanic *aiz (n.) 'copper, bronze, ore', the regular Germanic reflex of PIE *h₂éyos: the older nominative *ajaz > *āz was levelled out in favour of the oblique stem *aiz-, and Verner-conditioned *s remained z, giving Gothic aiz, Old Norse eir, Old High German ēr, Old English ār/ǣr. Nourai leaves the box wordless because the AHD entry he cites (a main-dictionary page) does not print a Germanic form; the form is supplied identically by Pokorny ('got. aiz, urgerm. *a(i)iz- = idg. *aies-'), Klein and Buck.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/aiz\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:925\", \"status\": \"not_checked\", \"note\": \"Page 925 of the AHD New College Edition would be the main-dictionary entry 'ore'; those 1970s scans on archive.org are lending-only (djvu text 401), so the page could not be read. Note that the accessible Watkins appendix does NOT put English ORE under ayes-: its index reads 'ORE aurum', and the ayes- entry lists only AENEOUS and ERA — so Nourai's Germanic-→-ore branch is probably taken from the body of the dictionary rather than from the root list, and may not be what the appendix says.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 15\", \"stance\": \"supports\", \"note\": \"'got. aiz (urgerm. *a(i)iz- = idg. *aies-) ,Erz, Geld‘, ahd. ēr ,Erz‘, anord. eir n. ,Erz, Kupfer‘.'\"},\n            {\"src\": \"KLN\", \"where\": \"vol. II p. 1093 s.v. ore\", \"stance\": \"supports\", \"note\": \"'rel. to ON. eir, ‘brass, copper’, OHG. ēr, ‘brass’, ... Goth. aiz, ‘bronze’.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §9.66 p. 611\", \"stance\": \"supports\", \"note\": \"'Goth. aiz, ON eir, OE ār, OHG ēr' listed directly under IE *ayes-.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 4\", \"stance\": \"supports\", \"note\": \"Same Germanic set; also ags. ǣren, as./ahd./mhd. ērin, nhd. ehern from *ayes-no-.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"ore\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Modern English ore is the phonetic continuation of Old English ār, ǣr 'brass, copper, bronze' < Proto-Germanic *aiz < PIE *h₂éyos — which is Nourai's arrow, and is what Klein, Pokorny, Buck and Wiktionary give. The complication he does not show is that the modern word is a MERGER: OE ār collided in Middle English with the unrelated OE ōra 'unwrought metal, ore' (related to eorþe 'earth'), the two not being fully assimilated until the 17th c.; the surviving form is the regular development of ār (OE ā > ME ǫː > NE /ɔː/, ME oor, or) but the meaning is ōra's. A second complication is that Nourai's own cited authority points elsewhere: Watkins's AHD appendix indexes 'ORE' under aurum (Latin aurum 'gold', via the Scandinavian coin øre < aureus), not under ayes-, and Etymonline likewise tags Proto-Germanic *ajiz- to PIE *aus- 'gold'. Hence 'plausible' rather than 'confirmed': the form-chain PGmc *aiz > OE ār > ore is standard and well supported, but the node hides a merger and the reference Nourai cites (AHD) classifies the word differently.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/ore\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/aiz\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference is given on this node; the parent's AHD:925 is the relevant one and could not be read (see node #6).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"vol. II p. 1093 s.v. ore, n.\", \"stance\": \"supports\", \"note\": \"'ore, n. — ME. oor, or, fr. OE. ār, ǣr, ‘brass’, rel. to ON. eir ... Goth. aiz, ‘bronze’, and cogn. with OI. áyah, Avestic ayō, L. aes ... fr. I.-E. *ayos-.' Klein makes no mention of a merger with OE ōra.\"},\n            {\"src\": \"Etymonline\", \"where\": \"entry 'ore'\", \"stance\": \"partial\", \"note\": \"'a merger of two words. The first is Old English ora ‘ore, unworked metal’ (related to eorþe ‘earth’) ... The second is Old English ar ‘brass, copper, bronze’, from Proto-Germanic *ajiz- (source also of Old Norse eir, Gothic aiz) ... The two words were not fully assimilated till 17c.; what emerged has the regular modern form of ar but the meaning of ora.' Etymonline refers *ajiz- to PIE *aus- ‘gold’, differing from Klein/Pokorny/Wiktionary.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, index s.v. ORE and entry [aurum]\", \"stance\": \"contradicts\", \"note\": \"Index line: 'ORE aurum'; the aurum entry reads 'Latin aurum (> French or), gold: ... EYRIR, OR¹, ORE, ORIFLAMME ...'. Watkins does not list ORE under ayes-, which is what Nourai's chart implies.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §9.66 p. 611\", \"stance\": \"supports\", \"note\": \"OE ār listed under IE *ayes- alongside Goth. aiz, ON eir, OHG ēr; Buck separately notes 'OE bres ... ME bras' for the unrelated ‘brass’ word.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, s.v. Ore\", \"stance\": \"silent\", \"note\": \"The OCR of SKT.txt at the 'ORE' running head (line 12840) is corrupted — the page prints the Orchestra/Orchis/Order entries and the 'ore' headword itself is unreadable in this scan.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-40.json > /dev/null && echo \"VALID JSON\""
}
```


### [2026-09-04T19:12:11.624Z] TOOL RESULT

```
VALID JSON
```


## [2026-09-04T19:12:15.791Z] TOOL CALL #87: Bash

```json
{
 "command": "python3 tools/verify_check.py 40"
}
```


### [2026-09-04T19:12:17.747Z] TOOL RESULT

```
nodes verified: 10/10
node verdicts: {'confirmed': 8, 'disputed': 1, 'plausible': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'not_checked': 5, 'partial': 1}
books consulted: {'partial': 6, 'supports': 30, 'silent': 6, 'contradicts': 2} | by book: {'KLN': 6, 'SYN': 5, 'WLD': 4, 'SKT': 4, 'BRT': 3, 'AHD': 3, 'Etymonline': 3, 'POK': 2, 'PHD': 2, 'HUB': 2, 'KNT': 1, 'AVG': 1, 'NYB': 1, 'CHEUNG': 1, 'HRN': 1, 'BQT': 1, 'ARY': 1, 'MON': 1, 'LAT': 1, 'LEW': 1}
```


## [2026-09-04T19:12:37.195Z] AGENT

Wrote `/home/sfmqrb/git/rishe/data/verification/page-40.json`; `verify_check.py 40` reports 10/10 nodes, no PROBLEM lines.

**Page 40 (book p. 10) — 2 entries, 10 nodes**

- Root verdicts: 2 confirmed. Node verdicts: 8 confirmed, 1 disputed, 1 plausible.
- Nourai's own refs: 9 supports, 1 partial, 5 not_checked (the 3 unreferenced English nodes plus AHD:443 / AHD:925, which are main-dictionary pages of the 1975 AHD — lending-only on IA; I checked the accessible Watkins appendix instead).
- Books consulted: 20 distinct (POK, WLD, AHD, IEC, SYN, KLN, SKT, LAT, LEW, BRT, KNT, AVG, PHD, NYB, HRN, HUB, CHEUNG, BQT, MON, ARY + Etymonline/Wiktionary): 30 supports, 6 partial, 2 contradicts, 6 silent.

Flagged items:

- **disputed — Aios/Ayos, node #2 [Pahlavi] āsīn, āhēn.** The forms are right (MacKenzie, Nyberg, Horn all have them), but the arrow from Avestan ayah- is a Zand translation-equivalence (Bartholomae AiW 156 "Pü.: āsīn 'Eisen'"), repeated by Mo'in (BQT:70) and Buck (SYN:612), not a sound-law descent. Hübschmann §57 p.10 flatly rejects it ("Die Etymologie von āhan bleibt dunkel … etwa *asaina- anzusetzen"); the modern reconstruction (Bailey DKS, Morgenstierne, ESIJa, Buyaner 2020, Wiktionary) is Proto-Iranian *Hácwā "iron" < PIE *h₂eḱ-, with Khotanese hīśśanä, Pashto ōspəna, Kurdish hesin, Ossetic æfsæn. NP āhan (node #3) is still confirmed off its own parent.
- **plausible — Aios/Ayos, node #7 [English] ore.** The form-chain PGmc *aiz > OE ār > ore is standard (Klein 1093, Pokorny, Buck, Wiktionary), but modern *ore* is a merger of OE ār with unrelated OE ōra, and Nourai's own cited authority disagrees: Watkins's AHD index puts ORE under *aurum*, not *ayes-*.

Other findings worth noting: the root note on entry 1 (Klein's Ayashya/Cyprus origin for *h₂éyos) is quoted accurately from KLN:1093 and traced to Pokorny KZ 46.292 f. via WLD I 4 and Mann IEC 332 — I evaluated it as a minority view current handbooks do not follow. In entry 0 node #1, the trailing "1" after *âěšâ* is a stray reference numeral, not part of the word, and the gloss "wealthy" for Av. *isvan-* is Klein's; Bartholomae gives "able, in command of". New file saved: `data/verification/sources/refs/ocr/BQT/70.vision.txt` (Mo'in's footnote 2 to آهن, read from the archive.org page image since ref_page.py has no scan for BQT vol. 1). Ten web sources archived via `fetch_source.py`.
