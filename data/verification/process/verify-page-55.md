# Verification process log — verify-page-55


## [2026-09-04T19:48:58.321Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 55 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-55.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-55.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-55.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 55` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T19:48:59.919Z] AGENT

I'll start by reading the instructions.


## [2026-09-04T19:49:02.038Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:49:02.053Z] TOOL RESULT

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


## [2026-09-04T19:49:02.298Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-55.txt"
}
```


### [2026-09-04T19:49:02.318Z] TOOL RESULT

```
1	=== PDF page 55 (book page 25) ===
2	--- entry 0 ---
3	ROOT [Indo-European] An 3, Anô : on, upon, above, to  (refs POK:39)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:39; KLN:67; KNT:164; DZA:57 | ana : on, upon ; anu, anuv : to, after, along ; anu-i : going along
5	#2 (parent #0) [Germanic] refs=AHD | ana, ano
6	  #3 (parent #2) [English] refs=None | on, upon, unless
7	#4 (parent #0) [Greek] refs=None | ana- : according to, upward, back, again ; ana-luein : to loosen back, analyze ; analogos : speak according to, give analogy
8	  #5 (parent #4) [English] refs=AHD | analysis, analogy, anatomy
9	--- entry 1 ---
10	ROOT An 4 -> redirect to Ne 1
11	--- entry 2 ---
12	ROOT [Arabic] A.n.b, anbar : amber  (refs FVA:286)
13	#1 (parent #0) [Persian] refs=BQT:1382; FVA:286 | anbar «عنبر» : amber
14	#2 (parent #0) [Middle Latin] refs=KLN:60 | 
15	  #3 (parent #2) [English] refs=KLN:60 | amber
16	--- entry 3 ---
17	ROOT anbar -> redirect to A.n.b
18	--- entry 4 ---
19	ROOT [Indo-European] Andho : blind, dark  (refs POK:41)
20	#1 (parent #0) [Avestan] refs=POK:41; SYN:323 | anda, ando : blind
21	#2 (parent #0) [Sogdian] refs=SOD:44 | ʿntʿ : blind
22	#3 (parent #0) [Latin] refs=AHD | umbra : shadow
23	  #4 (parent #3) [English] refs=None | umbrella
24	
```


## [2026-09-04T19:49:05.555Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-55.json",
 "description": "Read page 55 source JSON"
}
```


### [2026-09-04T19:49:05.592Z] TOOL RESULT

```
{
  "pdf_page": 55,
  "book_page": 25,
  "entries": [
    {
      "root": {
        "name": "An 3, Anô",
        "lang": "Indo-European",
        "refs": "POK:39",
        "gloss": "on, upon, above, to"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:39; KLN:67; KNT:164; DZA:57",
          "words": [
            {"translit": "ana", "gloss": "on, upon", "script": null},
            {"translit": "anu, anuv", "gloss": "to, after, along", "script": null},
            {"translit": "anu-i", "gloss": "going along", "script": null}
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
            {"translit": "ana, ano", "gloss": null, "script": null}
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
            {"translit": "on, upon, unless", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": null,
          "words": [
            {"translit": "ana-", "gloss": "according to, upward, back, again", "script": null},
            {"translit": "ana-luein", "gloss": "to loosen back, analyze", "script": null},
            {"translit": "analogos", "gloss": "speak according to, give analogy", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "analysis, analogy, anatomy", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "An 4",
        "redirect": "Ne 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "A.n.b, anbar",
        "lang": "Arabic",
        "refs": "FVA:286",
        "gloss": "amber"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:1382; FVA:286",
          "words": [
            {"translit": "anbar", "gloss": "amber", "script": "عنبر"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Middle Latin",
          "refs": "KLN:60",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "KLN:60",
          "words": [
            {"translit": "amber", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "anbar",
        "redirect": "A.n.b"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Andho",
        "lang": "Indo-European",
        "refs": "POK:41",
        "gloss": "blind, dark"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:41; SYN:323",
          "words": [
            {"translit": "anda, ando", "gloss": "blind", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:44",
          "words": [
            {"translit": "ʿntʿ", "gloss": "blind", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "umbra", "gloss": "shadow", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "umbrella", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-04T19:49:07.249Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T19:49:07.292Z] TOOL RESULT

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


## [2026-09-04T19:49:15.167Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','KLN','KNT','DZA','AHD','FVA','FVQ','BQT','SYN','SOD','WLD','IEC','BRT','HRN','HUB','PHD','NYB','SKT','LEW','LAT','MON','LKT','AFM','PLA','AFA','DEV','PHN','FSD','WEB','SIN','TAD','ARB']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-04T19:49:16.841Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
DZA {"title": "M.T. Rashed Mohassel, Daramadi bar Dastur-e Zaban-e Avestai, Khajeh 1364/1985", "kind": "purchase", "url": "taaghche.com (revised edition ebook)", "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: the 1364 Khajeh edition is not digitised; a revised edition is sold as an ebook on Taaghche."}
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_f
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnair
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = p
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://a
ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; t
```


## [2026-09-04T19:49:17.017Z] TOOL CALL #6: Bash

```json
{
 "command": "grep -n -i -E \"^(FVA|DZA|FVQ|SYN|SOD)\" /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt | head -40; echo ---; grep -n -i -E \"FVA|DZA\" /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt | head -20"
}
```


### [2026-09-04T19:49:17.081Z] TOOL RESULT

```
---
3: TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
9: TABLE IV - Reference Abbreviations (continued ...) 17 BLY 18 BQT 19 BRT 20 BST 21 CEL 22 DEV 23 DMO 24 DOZ 25 DRM 26 DVS 27 DZA 28 EAV 29 ETM 30 FAF 31 FFD H. W. Baily, "Hvatanica II", (Glossary of some Khotanese words with reference to Avestan and Persian words), Bulletin of the School of Oriental and African Studies (BSOAS IX:1937-39) pp 69-78, University of London. M. H. Tabriz! (Borhan), Borhan Qate', ^l»ls ^i&amp;j&gt; Etymological footnotes by Dr. M. MoTn, 4 vol, Amfr Kabrr Press, Tehran 1362 (1983). C. Bartholomae, Altiranisches Worterbuch Zusammen Mit Den Nacharbeiten Und Vorarbeiten, Walter de Gruyter Press, 1979. Paul Horn, "Some Inscriptions on Sassanian Gems", Avesta, Pahlavi and Ancient Persian Studies, First Series, pp 224-263, Bombay Educational Society's Press, 1904. S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, 6 Vol., Sverge Haus Publishers, Milton, Ma, 1997 L. M. Devic, Dictionnaire Etymologique des Mots Francais D'Origin Orientale, Oriental Press 1876. S. NafisT, Par Maktab Ostad, ilx-,1 Zohreh Press, Tehran 1344 (1965). R. Dozy, Verklarende Lisjt der Nederlandsche Woorden, Die Uit Het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch Afkomstig Zijn, Leiden 1867. J. Darmester, Etudes Itaniennes, Paris 1883. P. Davis, Roots - Family History of Familiar Words, McGraw-Hill Book Company 1981. M. T. Rashed Mohassel, Daramadi Bar Dastur ^^jl oki _}f~&gt;* j&gt;. iSJ^&gt;^ Zaban AvestST, Khajeh Press, Tehran 1364 (1985). J. Duchesne-Guillemin, "Etymologies Avestiques", Bulletin of the school of Oriental and African Studies (BSOAS IX: 1937-39) pp 861-869, University of London. M. Abolghasemr, RTsheh ShenasT - Etimologi, Ghoghnoos Press, Tehran 1374 (1995). A. Daneshgar, Farhang A'alam Farsi, Hafez NovTn Press, 1370 (1991). M. Abolghasemr, Fe'lhay FarsT Pari, Ghoghnoos Press, Tehran 1374 (1995). v^«&gt;jls pMel 
12: TABLE IV - Reference Abbreviations (continued...) 32 FIB 33 FNI 34 FRS 35 FSD 36 FSF 37 FVA 38 FVF 39 FVQ 40 FWE 41 FWK 42 GPL 43 HID 44 HJB 45 HRN 46 HUB 47 IEC Pur Davfld, Farhang Iran Bastan, Vol. I, University of Tehran Press 1326 (1947). F. DanaT, Farhang Namhay Irani, Negah Publishers, Tehran 1370 (1991). AsadT Tflsi, Farhang Fors, Kharazmi Press, Tehran 1365 (1986). ^iljjl ^cUj^cLs &gt;^fl&gt;jS Funk and Wagnalla, New Standard Dictionary of the English Language, Funk &amp; Wagnalls Company, New York, 1940. A. H. Noushin, Farhang Shahnameh Ferdowsi, oULS 03I3 - ^-jiy i*La&gt;Li ^^ay Vajheh Namak, Donya Press, Tehran 1363 (1984). S. M. Nahvi, Farhang VSm J-^-i - ^-&gt;jl» j* ^o^ ^gb. 03I3 ^(3 ^S^a,^ Vajhehhay Arabi dar Farsi, Dakhil, TohT Azadi Press 1368 (1989). S. M. A. Emam Shflshtari, ^c ^bj ji ^-"j1* iS^ °j'3 «-fc»j» Farhang Vajhehhay Farsi dar zaban Arabi, Anjoman Asar Melli, No 58, Bahman Press, Tehran, 1347 (1968). A. Jeffrey, The Foreign Vocabulary of the Qur'an, (see VDQ). Oriental Institute, Baroda, Stephen Austin &amp; Sons Press, Great Britain 1938 A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, Warner Books, 1966. R. Dvorak, "Fremdworter im Koran", Doctoral Dissertation, Akademische Buchdruckerei von F. Straub (1884). J.T. Platts and G.S.A. Ranking, A Grammar of the Persian Language, Oxford University Press (1911). B. Bartholomae, Handbuch der Altlranischen Dialekte, Breitkopf &amp;Hartel, Leipzig 1883. H. Yule &amp; A. C. Burnel, Hobson Jobson, A Glossary of Colloqual AngloIndian Words, Oriental Publishers, Delhi 1903-1968. Paul Horn, Grundriss der NeuPersischen Etymology, Verlag von Karl J. Trubner, Strassburg 1893-1974. H. Hubschmann, Persische Studien, Verlag von Karl J. Trubner, Strassburg 1895. Stuart E. Mann, An Indo-European Comparative Dictionary, Helmut Buske Verlag, Hamburg 1987 A-ll
```


## [2026-09-04T19:49:25.008Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','KLN','KNT','AHD','SYN','SOD','IEC','SKT','LEW','LAT','FSD','WEB','BQT']:\n    v=d[k]\n    print('==',k, '| local:', v.get('local_file'), '| offset:', v.get('page_offset'), '| hint:', str(v.get('lookup_hint'))[:300])\n\""
}
```


## [2026-09-04T19:49:25.429Z] TOOL CALL #8: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/tools/ ; echo ---; sed -n 1,60p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-04T19:49:27.198Z] TOOL RESULT

```
== POK | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== KLN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== KNT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== AHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== SYN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== SOD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'] | offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur
== IEC | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== LEW | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt | offset: 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
== LAT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt | offset: leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
== FSD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== WEB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.
== BQT | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
```


### [2026-09-04T19:49:27.239Z] TOOL RESULT

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


## [2026-09-04T19:49:31.380Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Page(s): 39\" POK_full.txt | head -20; echo \"=== 41 ===\"; grep -n \"Page(s): 41\" POK_full.txt | head -20"
}
```


### [2026-09-04T19:49:31.447Z] TOOL RESULT

```
5612:Page(s): 39-40 
31134:Page(s): 392 
31694:Page(s): 390 
31720:Page(s): 399 
32130:Page(s): 393-398 
35603:Page(s): 392-393 
35681:Page(s): 390-391 
35741:Page(s): 399-400 
35768:Page(s): 399 
=== 41 ===
4794:Page(s): 41 
4842:Page(s): 41 
5056:Page(s): 41-42 
36009:Page(s): 412-413 
36085:Page(s): 413-414 
37427:Page(s): 418-419 
37647:Page(s): 419-422 
37931:Page(s): 414-416 
38005:Page(s): 416-417
```


## [2026-09-04T19:49:31.965Z] TOOL CALL #10: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/ | head -30"
}
```


### [2026-09-04T19:49:32.009Z] TOOL RESULT

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
page-46.json
page-47.json
page-48.json
page-49.json
page-52.json
process
sources
```


## [2026-09-04T19:49:34.721Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5580,5625p' POK_full.txt; echo \"=========== 41 area ===========\"; sed -n '4770,4860p' POK_full.txt; echo \"==== 5040-5070 ====\"; sed -n '5040,5075p' POK_full.txt"
}
```


### [2026-09-04T19:49:34.807Z] TOOL RESULT

```
maybe zero grade in alb. {*ana) ne^ on, in '. 

Lithuanian anote, anofm. Gen. " accordingly, according to '; about the first on proto 
Slavic *c»/7 going back to Slavic Slavic vh{n)- ' in, on ' see Brugmann Grdr. 112 2, 828 and 
*en"\n'. 

With zero grade of the first syllable, thus initial sound n: 

Lithuanian nudm. Gen. " from down, from away ' (these where from meaning only 
from the connection with the ablative originated anew), as a Nominal praf. nuo-, as a 
Verbal praf. /7i/- (proklit. abbreviation as in pri-bes\de pne), let. nuom. Gen. ' from', as 
prefix nuo-; 

Old Prussian no, nam. Akk. " on (where), against, about there ', as prefix " after; from 
away ' (see also BezzenbergerKZ. 44, 304); Old Church Slavic nam. Akk. and Lok. ' on 
there; up, on, in ' (in addition aiier pre: pre-db neologism na-db " upside, above, about ' m. 
Akk. and Instr. and proverb); Old Indie na- perhaps in nadhita^ pressed ', see below na-^ 
help '. 

Here presumably Lithuanian -na, -n " in (direction where) ', postal position with verbs of 
the movement, Avestan na-zdyah-. Old Indie nedJyas- " closer '(' * moved near '); root sed- 
" sit '; presumably similarly Gothic nelv. Old High German nah Mn. ' near' as " looking 
near, turned near ' (with root oq "-as 2nd part); see Brugmann Grdr. I|2 2, 798 f., where 
also about the ambiguous Old Indie adhT about, on', ap. adiy^'w! (*-/7dh/or "ed^/; *cA^n). 

maybe alb. {^naH) ngalrom' [common alb. n > /7^ shift] 

About Gothic anaksa6v. " suddenly, straight away ', supposedly to Old Bulgarian 
nag/b " suddenly, abruptly ' (?), s. Feist 42. 

References: WP. I 58 f., WH. I 43 f., 49, 677, Feist 41 a, 373, Trautmann 200. 

Page(s): 39-40 



Root / lemma: ansa, ansi- 

Meaning: noose, snare 

Material: Latin ansa^ clutch, handle, a handle; (hence), occasion, opportunity', ansae 

crepidae' the eyelets on the straps of the shoe soles through which the shoelaces were 

pulled ' = Lithuanian c[sa\. (Akk. ^s^) ' pot handle, loop with the knot apron ' (compare 

=========== 41 area ===========

Meaning: "stem, spike' 

Material: Nur griechisch: aGrip " an ear of corn ', av0£pi^ " stalk point, stalk ', av0£piKO(; " 

Stalk, stem of a plant ', avGepscbv " chin ' as " bearded, shaggy place ', av9piaK0(; ' the 

common chervil ', named after his prickly fruit, avGpnvr), av9pr|5u)v " wasp, forest bee ', 

word outcome after TSvGpnvr) ' corneous '; 

Tav9pr|5u)v " wasp ' (here maybe av9pu)no(; from *av9po-u)no(; " with bearded face = man 

', then " man, person ', GiJntert Heidelberg. SB. 1915, Abh. X?; compare also Schwyzer 

Gr. Gr. I 4264. 



After Kretschmer Gl. 28, 246 from *av5p-u)n6(;, the rough breathing of opaw etc 
figurative?); from also aGapn (*a0apFa), aGnpa ' wheat gruel, Spelt miller ' (von Plin. n. h. 
22, 121 however identified as agypt. word)? 

References: WP. I 45. 
Page(s): 41 

Root / lemma: anA"^-, aned^- 

Meaning: "to grow, bloom, blossom, young woman, young cow ' 

Material: Old Indie andhahu. " Soma plants '; Armenian and^ field '; gr. ayQoc, n. ' flower, 

bloom ', avGsu) ' blossoms ', avGnpoq {*-es-ro-) " blossoming ' etc; alb. ende{*an6'^dn) ' 

blossom, flower', endem^ blossoms ' (efrom present *efrom *an6,^d}\ Tocharian A ant, B 

ante^ open space, area '. 

Middle Irish ainder, aindir^ young woman ', cymr. anner^ young cow ', PI. anneirod, 
(common Celtic -ns-, -nt- > -nn-), acymr. enderic^ a bull-calf; also of the young of other 
animals ', cymr. enderig^ bull, ox ', bret. ounner {Treg. annouar, Vannes annoer) " heifer, 
young cow '; moreover French (l)andierxx\. " fire goat, Aries ', also "poppy' (= ' young girl ', 
compare Italian madona, fantina^'^O'^'^Y), further to Basque andere^ woman', iber. FN 
Andere, Anderca, MN Anderus, maybe Celtic Origin? ( *andero-^ blossoming, young '?). 

According to Schwyzer Gr. Gr. I 339 here gr. av-nvoGs ' came out, bubbled out; ', snsv- 
nvoGs " reside on top of ', KaTsv-nvoGs ' canopied, covered ', etc. 

In spite of the a little bit divergent meaning probably also here with zero grade *i^^: 

Old Indie adhvanru. = Avestan advanm. ' way, road ', for what Old Indie adhvara-h 
religious action (*Soma-) sacrifice, ceremony ' (originally ' course of action, way' - " 
ceremonious way ') from *n6'"uero-, and probably also with suffix ablaut (*n&^uro-) isl. 
gndurrm. " a kind of snow shoe '. 

References: WP. I 45, 67, P. Benoit ZrPh. 44, 3 ff., 69 ff. 
See also: Here belongs probably: and^er-, ij6!^er-. 
Page(s): 40-41 

Root / lemma: anA'^o- 
Meaning: 'blind, dark' 



Material: Old Indie andha-, Avestan anda-^ blind, dark ', gall, andabataxw. " a gladiator 

who fought with a helmet without openings ' (to Celtic loanword Latin battud^ to beat, 

knock '). 

References: WP. I 182, WH. I 46. 

Page(s): 41 

Root / lemma: an(9)-3^henah^ 

Meaning: "to breathe' 

Note: 

Root/ lemma: an(a)-3\ to breathe' derived from a reduction of Root/ lemma: anghen-: 

"smell, odour; person' as in Armenian sat//? (for older *anj). Gen. anjin^ soul, being, person 

': Old Norse ang/m. " odour, smell ' : alb. aA7y"swell, puff' [common alb. ng > nj\. 

Material: Old Indie ^/7/// "breathes' (also thematically anati), anila-h "breath, breeze, wind', 

^/7a-/7 (maybe "breath' or " mouth, nose ', ana-nam^ mouth, muzzle, face ' with Indie 

Vrddhi; "mouth' as "breath, the breathing '); p/a/?///" breathes'; 
==== 5040-5070 ====

Sary-Yugliur: an+t 

Azerbaidzlian: anGut-boGaz 'fljinHHOujeuM' 

Turkmen: ar)k 'red duck' 

Kliakassian: at 

Karaim: anqlt, ankit 'ostrich, vulture, dragon' 

Kumyk: hanqut 



References: WP. I 60, WH. I 44, Trautmann 10. 
Page(s): 41-42 



Root / lemma: anghen- 

Meaning: "smell, odour; person' 

Material: Armenian anjn{ior older *anj). Gen. anjin^ soul, being, person ' = Old Norse angi 

m. " odour, smell '. 

maybe alb. 5/7/ "swell, puff' [common alb. ng > nj\. 

References: Liden Arm. Stud. 38 f., WP. I 58, Meillet Esquisse 77 ff. 

Page(s): 43 

Root / lemma: angh- {*hengh-)
```


## [2026-09-04T19:49:43.605Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5520,5583p' POK_full.txt"
}
```


### [2026-09-04T19:49:43.651Z] TOOL RESULT

```
Church Slavic v-btor-t "second' s. £//-" asunder, apart '. 



Note: 

It seems Root / lemma: an-2\ "there, on the other side' is a zero grade of the extended 
Root/ lemma: al-1, ol-\ "besides; other' into *alny-, *any-. 

Maybe zero grade in alb. {*nyatra) fjeter' other' [common alb. n > nt > /] : Old Indie anyatra 
"somewhere else'. 

Perhaps alb. dial. {* heter) jater, Jeter, alb. [ attribute /e'of + antef\, tjeter' other, second'; 
similar to formation in alb. Geg {*te mel= of milk) /a/77//"milk' where te is the alb. attribute 
particle. Initial alb./ seems to have substituted the old laryngeal form /?-. 

References: WP. I 56, 67, II 337, WH. I 44, Trautmann 10/11, Debrunner REtlE. 3, 1 ff. 
Page(s): 37-38 

Root / lemma: an4, anu, and, no 

Meaning: a preposition ("along a slanted surface, etc.") 

Note: (compare the summary by Brugmann Grdr. I|2 2, 798 f., also about the syntactic). 

Material: Avestan ana. Old pers. a/7a(Proto Aryan * ana or *ana) " about there ' (m. Akk. or 

Instr.), " along, on ' (m. Akk.), Avestan anu. Old pers. anuv^ after, according to; up there ' 

(m. Akk.), " lengthwise, along ' (m. Lok.), also proverb; 

maybe alb. anes "along' 

Old Indie anu^ after (timewise m. Akk., Abl., Gen.), after (order), after there, along, 
behind, according to, with regard to, against ' (m. Akk.), Adv. " on it (auslaut-i/ appears to 
be comparable in Lesbian Thessalian anu beside Attic airo. Against Wackernagels 
explanation from Indo Germanic *enu^ along, according to ' see WH. I 677; to-^see below 
ap-u); Armenian am- in am-barnam ham-barnam^ I raise, uplift ', ham-berem^ I endure ' 
maybe from -an (the h by mixture with a borrowed sound from the Pers. ham- " together '; 

Ionic-Attic ava, ava " on, upwards, along ', Doric Boeotian Arcadian Cypriot av, Lesbian 
Thessalian Arcadian, z. Part Cypriot 6v, isolates Arcadian Cypriot uv (from 6v) ds. (the 
monosyllabic form appears the original and to be extended ava only after Kaia; compare 
Schwyzer Gr. Gr. I 622; it is likely according to Schwyzer Gr. Gr. I 275 6v originated from 
civ; Adv. avu) " upward, up '; 

A Latin remainder appears an-helo^ breathes strongly and with difficulty ' {an + 
*ansld); Umbrian an-, (with e/7"in' become synonymous and with it alternately, hence, en- 
tentu bes\6e.) an-tentu "\r\ter\6\to' , ansen'ato 'observatum', ang/ar^ osc\r\es' {*an-k/a to 
clamo) etc 



Maybe here Old Irish an-dess^ from the south ' etc; 

Gothic ana{v(\. dat. mid Akk.) " on, in, against, because of, about ', Old Norse a Adv. 
and preposition m. dat. and Akk. ' on, in ', m. dat. " on, in, up, by ', m. Akk. " after, up, on, 
against ', Old Saxon an. Old English on. Old High German aua, an. Modern High German 
an{*anaor *and, *ane) preposition m. dat. and Akk. and Instr. ' on, up, in, to, against '; 

maybe zero grade in alb. {*ana) ne^ on, in '. 

Lithuanian anote, anofm. Gen. " accordingly, according to '; about the first on proto 
Slavic *c»/7 going back to Slavic Slavic vh{n)- ' in, on ' see Brugmann Grdr. 112 2, 828 and
```


## [2026-09-04T19:49:44.673Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"umbra\" AHD_watkins1985.txt | head -20; echo \"=== andho ===\"; grep -n -i \"andho\\|an-dho\\|^an-\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-04T19:49:44.729Z] TOOL RESULT

```
282:b. Old Norse um/(b), about, around: OMBUDSMAN; c. Old High German umbi, around: UMLAUT. 3. Latin ambi-, around, about: AMBI-. 4. Greek amphi, around, about: AMPHI-. 5. Celtic *ambi (see ag-). [Pok. ambhi 34.] ambhé. Both. 1. Reduced form *bAd in Germanic *b6-, *bé in Old Norse bdthir, both: BOTH. 2. Latin ambé, both: AMBSACE. 3. Greek amphé, both: AMPHOTERIC. [In Pok. ambhi 34.] amer-. Day. Suffixed form “Gmer-d in Greek hémera, day: EPHEMERAL, HEMERALOPIA. [Pok. dmer- 35.] ames-. Blackbird. 1. Suffixed variant form *ams-ol- in Old English dsle, blackbird: ouzEL. 2. Suffixed variant forms *mes-old, *mes-olo- in Latin merula, merulus, merle, blackbird: MERLE, MERLON. [Pok. ames- 35.] [amma. Various nursery words. Latin root. 1. Medieval Latin amma, mother: AMAH. 2. Reduced form *am- in: a. Latin amare, to love: AMATEUR, AMATIVE, AMATORY, AMORETTO, AMOUR; ENAMOR, INAMORATA, PARAMOUR; b. Latin amita, aunt: AUNT; c. Latin amicus, friend: AMICABLE, AMIGO, AMITY; ENEMY, INIMICAL.] an’. On. Extended form *ana. 1. Germanic *ana, ané in: a. Old English an, on, a, on: ON; b. Old Norse 4, in, on: ALOFT; ¢. Old High German ana (> Middle High Ger- man ane), on: ANLAGE; d. Middle Dutch aan, on: ON- SLAUGHT. 2. Greek ana, on, up, at the rate of: ANA?, ANA-. [Pok. 4. an 39.] an?, Demonstrative particle. Suffixed form “*an-tero-, “other (of two)” (compare *al-tero- under al-') in Ger- manic *antharaz in Old English 6ther, other: OTHER. [Pok. 2. an 37.] an-', Old woman, ancestor (nursery word). Latin anus, old woman: ANILE. [Pok. 1. an- 36.] an-2. To pour, draw water. Suffixed form *an-tlo- in Greek antlos, bilge water, bucket: ANTLIA. [In Pok. 1. sem- 901.] andh-. Bloom. Suffixed form *andh-es- in Greek anthos, flower: ANTHEMION, ANTHER, ANTHESIS, ANTHO-, -AN- THOUS; AGAPANTHUS, CHRYSANTHEMUM, DIANTHUS, EX- ANTHEMA, HYDRANTH, (MONANTHOUS), STROPHANTHIN. [Pok. andh- 40.] andho-. Blind, dark. Suffixed variant form *ondh-ro- perhaps in Latin umbra, shadow: UMBEL, UMBRA, UM- BRELLA; ADUMBRATE. [Pok. andho- 41.] ane-. To breathe. Suffixed form *ana-mo- in: a. Latin animus, reason, mind, and anima, soul, spirit, life, breath: ANIMA, ANIMADVERT, ANIMAL, ANIMATE, (ANI- MATO), ANIMISM, ANIMOSITY, ANIMUS; EQUANIMITY, LONGANIMITY, MAGNANIMOUS, PUSILLANIMOUS, UNANI- mous; b. Greek anemos, wind: ANEMO-. [Pok. 3. an(9)- 38.] anata. Doorjamb. Latin antae (plural), a pair of pillars on the opposite sides of a door: ANTA. [Pok. anatd- 42.] [angelos. Messenger. Greek noun, akin to Greek anga- ros, mounted courier, both from an unknown Oriental source. 1. Greek angelos, messenger: ANGEL, (ANGELIC), ANGELICA, (ANGELUS); ARCHANGEL, EVANGEL. 2. Greek angaros, mounted courier: ANGARY.] angh-. Tight, painfully constricted, painful. 1. Germanic *ang-, compressed, hard, painful, in Old English ang- nzgl, “painful spike (in the flesh),” corn, excrescence (nzgl, spike; see nogh-): AGNAIL. 2. Suffixed form *angh-os- in Germanic *angaz in Old Norse angr, sor- row, grief: ANGER. 3. Suffixed form *angh-os-ti- in Ger- manic *angusti- in Old High German angust (> German Angst), anxiety: ANGST. 4. Latin angere, to strangle, draw tight: ANxious. 5. Suffixed form *angh-os-to- in Latin angustus, narrow: ANGUISH. 6. Greek ankhein, to squeeze, embrace: QUINSY. 7. Greek ankhoné, a stran- gling: ANGINA. [Pok. angh- 42.] angvhi-. Snake, eel. 1. Latin anguis, snake: ANGUINE; ANGUILLIFORM. 2. Taboo deformation or separate root *ogvhi- in Greek ophis, snake, serpent: OPHIDIAN, OPHITE; OPHIOLOGY, OPHIUCHUS. 3. Taboo deformation or separate root *eghi- in Greek ekhis, snake, in deriva-
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
2433:UMBRA andho- UMBRELLA andho- UMLAUT ambhi, kleu-1 uN-l ne
=== andho ===
282:b. Old Norse um/(b), about, around: OMBUDSMAN; c. Old High German umbi, around: UMLAUT. 3. Latin ambi-, around, about: AMBI-. 4. Greek amphi, around, about: AMPHI-. 5. Celtic *ambi (see ag-). [Pok. ambhi 34.] ambhé. Both. 1. Reduced form *bAd in Germanic *b6-, *bé in Old Norse bdthir, both: BOTH. 2. Latin ambé, both: AMBSACE. 3. Greek amphé, both: AMPHOTERIC. [In Pok. ambhi 34.] amer-. Day. Suffixed form “Gmer-d in Greek hémera, day: EPHEMERAL, HEMERALOPIA. [Pok. dmer- 35.] ames-. Blackbird. 1. Suffixed variant form *ams-ol- in Old English dsle, blackbird: ouzEL. 2. Suffixed variant forms *mes-old, *mes-olo- in Latin merula, merulus, merle, blackbird: MERLE, MERLON. [Pok. ames- 35.] [amma. Various nursery words. Latin root. 1. Medieval Latin amma, mother: AMAH. 2. Reduced form *am- in: a. Latin amare, to love: AMATEUR, AMATIVE, AMATORY, AMORETTO, AMOUR; ENAMOR, INAMORATA, PARAMOUR; b. Latin amita, aunt: AUNT; c. Latin amicus, friend: AMICABLE, AMIGO, AMITY; ENEMY, INIMICAL.] an’. On. Extended form *ana. 1. Germanic *ana, ané in: a. Old English an, on, a, on: ON; b. Old Norse 4, in, on: ALOFT; ¢. Old High German ana (> Middle High Ger- man ane), on: ANLAGE; d. Middle Dutch aan, on: ON- SLAUGHT. 2. Greek ana, on, up, at the rate of: ANA?, ANA-. [Pok. 4. an 39.] an?, Demonstrative particle. Suffixed form “*an-tero-, “other (of two)” (compare *al-tero- under al-') in Ger- manic *antharaz in Old English 6ther, other: OTHER. [Pok. 2. an 37.] an-', Old woman, ancestor (nursery word). Latin anus, old woman: ANILE. [Pok. 1. an- 36.] an-2. To pour, draw water. Suffixed form *an-tlo- in Greek antlos, bilge water, bucket: ANTLIA. [In Pok. 1. sem- 901.] andh-. Bloom. Suffixed form *andh-es- in Greek anthos, flower: ANTHEMION, ANTHER, ANTHESIS, ANTHO-, -AN- THOUS; AGAPANTHUS, CHRYSANTHEMUM, DIANTHUS, EX- ANTHEMA, HYDRANTH, (MONANTHOUS), STROPHANTHIN. [Pok. andh- 40.] andho-. Blind, dark. Suffixed variant form *ondh-ro- perhaps in Latin umbra, shadow: UMBEL, UMBRA, UM- BRELLA; ADUMBRATE. [Pok. andho- 41.] ane-. To breathe. Suffixed form *ana-mo- in: a. Latin animus, reason, mind, and anima, soul, spirit, life, breath: ANIMA, ANIMADVERT, ANIMAL, ANIMATE, (ANI- MATO), ANIMISM, ANIMOSITY, ANIMUS; EQUANIMITY, LONGANIMITY, MAGNANIMOUS, PUSILLANIMOUS, UNANI- mous; b. Greek anemos, wind: ANEMO-. [Pok. 3. an(9)- 38.] anata. Doorjamb. Latin antae (plural), a pair of pillars on the opposite sides of a door: ANTA. [Pok. anatd- 42.] [angelos. Messenger. Greek noun, akin to Greek anga- ros, mounted courier, both from an unknown Oriental source. 1. Greek angelos, messenger: ANGEL, (ANGELIC), ANGELICA, (ANGELUS); ARCHANGEL, EVANGEL. 2. Greek angaros, mounted courier: ANGARY.] angh-. Tight, painfully constricted, painful. 1. Germanic *ang-, compressed, hard, painful, in Old English ang- nzgl, “painful spike (in the flesh),” corn, excrescence (nzgl, spike; see nogh-): AGNAIL. 2. Suffixed form *angh-os- in Germanic *angaz in Old Norse angr, sor- row, grief: ANGER. 3. Suffixed form *angh-os-ti- in Ger- manic *angusti- in Old High German angust (> German Angst), anxiety: ANGST. 4. Latin angere, to strangle, draw tight: ANxious. 5. Suffixed form *angh-os-to- in Latin angustus, narrow: ANGUISH. 6. Greek ankhein, to squeeze, embrace: QUINSY. 7. Greek ankhoné, a stran- gling: ANGINA. [Pok. angh- 42.] angvhi-. Snake, eel. 1. Latin anguis, snake: ANGUINE; ANGUILLIFORM. 2. Taboo deformation or separate root *ogvhi- in Greek ophis, snake, serpent: OPHIDIAN, OPHITE; OPHIOLOGY, OPHIUCHUS. 3. Taboo deformation or separate root *eghi- in Greek ekhis, snake, in deriva-
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
1240:AN- ne
2432:UMBEL andho- UMBILICUS nobh- UMBO nobh-
2433:UMBRA andho- UMBRELLA andho- UMLAUT ambhi, kleu-1 uN-l ne
```


## [2026-09-04T19:50:20.079Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KNT anuv ===\"; grep -n \"^anuv\\|anuv\" KNT.txt | head -20; echo \"=== KNT ana ===\"; grep -n \"^ana\\b\\|^ana,\" KNT.txt | head"
}
```


### [2026-09-04T19:50:20.141Z] TOOL RESULT

```
=== KNT anuv ===
1857:wan- їп banuvan-rya-. V. Stem in -vin-: adj. mana’-uvin-.
3053:in their position; for while they normally preceded the noun which they modify, we find also DNb 25f anuv taumaniSaty ‘according to his powers’, and the restored DB 5.27 [та аат :] S[ku]za : пата ‘the chief of them, Skunkha by name’, where the -šīm has no earlier word to which it may be attached, and space does not permit lhyaSdm : тайба |] Slkulza : пата. Cf. also $8111 end.
4127:19 2 : parsàmiy : паа : kama : tya : mar^üya 20 : vinaflayais : naipatimà : ava : Каша : yadi 21 y : vináfayais : naiy : frafiyaiS : martiya : 22 tya : рау : martiyam : (айу :ava : mam : 23 палу : varnavataiy : yátà : uradanám : hadu 24 рат : àxinautiy : martiya : tya : kunau 25 tiy : yad'ivà : abaratiy : anuv : tauman
4143:42 ra : ° uvàsabàra : amiy : fanuvaniya : ufa
4405:rauta : tya : Mudràyaly : danuvatiy : ab
5176:ubanuvaniya- sb. ‘good bowman’: u- ‘good’ + Sanwaniya- ‘bowman’. wudanwaniya nsm. DNb 42.
5473:Sanuvaniya- sb. ‘bowman’: deriv. ($144.IV) of stem in Av. Üanvar/n- ‘bow’, ef. Skt. dhanvan- ‘bow’ (583.11, $114, §155.1V) and Hz. ApI 339.
=== KNT ana ===
```


## [2026-09-04T19:50:21.542Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT anda ===\"; grep -n \"anda-\\|and\\^a\" BRT.txt | head -20; echo; echo \"=== SOD blind ===\"; grep -n -i \"blind\" SOD_pages.txt | head -20"
}
```


### [2026-09-04T19:50:21.598Z] TOOL RESULT

```
=== BRT anda ===
4616:•  j.  anda-  Adj.  'blind':  n^il  ava  zaoi^ra paiti,vlse  yä  mävsya  frattuhannti  'dssca tNPm.)  ..  Yt.5.93.
5819:•  j,  astö.vi'Sätav-  :  °\5tu-  m.  Name  eines Dafva'h  fräksrssts  "hstus  "zirijä  (sd.) ajiairi.ayö  Aog.57;  —  °oütu^  dim  handa- yeiti  vayS  dim  bastsm  nayeiti  V.ß.S;  — 'oUlus  p?sanatti  V.4.^^.
8347:•  j.  upairi,  p,  upariy  i)  Adv,  'supetne'; a)  'oben':  °ri  pusqm  (sd,)  bandayata  Yt. 5.128.  b)  'von  oben  her':  fravasayS .. ya  'ri  ^hamarmat  (sd.)  .  .  bazül  slanda- yeiti  Yt.  13. 31.  2)  ftaen.  mit  Akk.  und Instr.;  a)  'oben  über  — ,  oben  auf—',  mit Akk,  a)  auf  die  Frage  wo?:  asim  .  . yim  °ri  *vis  * rao'jat . .  yim  "ri  k^rysäsps ., pitüm  pacata  Y.p.  11;  — gSuS  kihrpa  ..yim
8357:•  j.  upairLkairya-  Adj.  (fem.  ys^  'des Wirksamkeit  oben  gelegen  ist,  von  oben her  wirkend';  fravasayS . .  °rya  .  .ya  upairi  \ */iamarmäi.,  aur7»^anqm..b3züi  scanda- yeittti  YLy.31.
16676:banda-
16712:bqnaya-'\  —  PPfP.  banta-  (sbes.).  •  j.    (,   p.)   banda-    m.  'Bande,    Fessel':
17127:fravaiayS)..aurvaiianam  uyra  °züs  scanda-  _
17619:—  Uta  bannii  '%3m  vTspä  banmavB  gai- rinqm  Yt/Ä  6;  6';  —  ydäira  vs  aAurS mazdä  '%sm  baxsat  F.  4b;  —  'ha  (IS.) ..  var)da%a  Y,55.3;  —  'dathe'^  vanda- 'häiea  \.68.2.  '%äi  (und  "'hai  s)  als Inf.  sbes.
18648:xräm  aiwi.vamaiti  ".  .  der  sogar  noch aus  dem  neunten  Land*'  eines  faustgrossen Stücks  Fleisch  gewahr  wird"  ytr4-33; 16. 10.  a)  ASn.  °m3m  als  Adv.  'beim neunten  Mal':  yaäsa  t(&a  °m?m''>  handa- riza  V.  8.  78.
19196:•  j.  oi-vanda-  m,  'Fessel,  Fesselimg, Gefangennahme':  haomsm  yim  tüvisaiH (sd.)  'dät  apayeiti  \dusmainyagt,  sd.]  p>Sana kaca  ".  .  entgeht  man  der  Fessel  [des Feindes]  in  der  Schlacht"  Yt/^-s?.
20527:•  i-i  St  P-"  mi^ra-,  p.  "mitra-"'  m.  'Ver- trag, Abmachung,  Konliakt':  "rim  mä janyä  .  .  Mvaya  tT  asti  (Sp.  270  U.)  'rS drvataäa  asaona^a  Yt.  70.  a ;  —  laiti  aSe 'ra  tava  yat  ahurahe  masdsl  äat  mraot ahurS . .:  xsvas. .  vacaAind . .  sasf3.tnaräs . . pasu.mazS  .  .  staorö.mazB  .  .  vlrS.masS  .  . dai}ihu,mazS  V,  4L  2;  —  vacB paoirim  'nm karmaoiti  *zasts.maz3  alät  framansaiti *zastö.masö  atiät  antan  urvaitya^sA.)  /ra- daäiaiti  y.4-Z'i  —  Äaj'  agiO  'rB  aiwi- druxtö  ästäraili  yB  vacalünB  V.  4.5;  — yö  'nm  aiwt.druzaiti  ytm  vaeahimm  V, 4. 1 1 ;  —  s.  noch  Yt  10. 3,  45, 14. 47,  V. 4.  54  unter  A  n.  a)  im  gAw.  'reli- giöse Bindung,  Verpflichtung':  yS . .  drltä ayanUtn  urvätöis  (sd.)  vä  .  .  'rBibyS  vä \.46.  5.  A)  als  Gottheit*';  1)  im  Ap.: mSm  a'ura^maxdä  utä  °'^r<^  bage^  pätuv Ao.  /.  4;  —  J'urJ'mazdä''  ^anahitc^  utä "'trJ'  Am.4''i  i  i'>ra*).  II)  im  jAw. (yazata-) :  kö  'rtm  aiwi.drusaiti  ks  rasnüm paifijrinaxti  Yt  14-  47;  10.  45;  —  äsu.- aspim  dacäiH  'rö  .  .  ysi  'nm  nsit  aiwi.- druUnti  Yt  ro.  3 ;  —  rasnaoSca  paitLsanfam 'raheca  aiwi.drux/3m  (sd.)  V.  4. 54; — yai vä  dim  aiwLdrusaiti  . .  /rasa  upajcanda- yäti  'rB  grantB  upaJbUtB  Uta  nmämm  .  . Yt/0. 18;  19;  —  apa  HB  haca  azaaAat ,  .  'ra  barBis  anädruxtB  Yt  10.  23;  —  t^sa mainyete  dus:^ar3nä  nSit  vlsp?m  aiwi.- druxtse  'rB  vamaitt  apifma  Yt  70.105; — ■  satayus  antan  pitan  pu^rtmla  . .  asti 'rJYLio.  117;  116;  —  tOm  akB  vakUlasia 'ra  ahi  daiAhuby5..tBm  axstöii  anäxitBiita 'ra  xSayehe  dahyunqm  Yt70.  39;  29;  — tbiHahecil  axlnultahe  (sd.)  °ra  (IS.)  mata rämayeiti  huxsnüitlm  paiti  'rahe  , .  xsiiB- taAe^it  albiHahe  (sd.)  °ra  manB  yaozayäti ax/nßitlm  paiti  *raAeYtio.iog— 111;  120; —  'raAe  da&yunam  dai^hupatsU  Y.  /,  1 1 ; 2.  II,  Yt/0. 145,  75.35;  —  äea  nB  jamyät avahyäi  uyrB  aiwi'^Urd  ..'rB  ralva  dai^hu- paitii  Yt  10.  78;  —  'nm  aiwi.dahyüm  . . 'nm  antar».daRyüm  'rtm  ä.daRyäm  . .  Yt 10.  144;  144*;  —  ci>rä  'rahe/rayana  yasj tarn  da^Bm  slaraitt  ..  Yt  iO.  112;  — kaaa   nB   aria  gavai^im    apayst  paskst
22390:'führen,  ziehen,  schleppen':  ^o^a  banda- yeni  ..franrasyänim  Uta  baitsm  vä%aymi Yt.p.  18;  ^yat ..  baslB  atakat  väiayamnS (pass.)  Yt  15.52;  —  z'itansi}  (sd.)  datvS .  .  urvämm  bast?m  väliayeiti  W.ir/.ti).
25955:KompA.  —  Zum  V.  ^sand-,  —  zBed.  vgl.  ai. chanda-  m.  —  PO.  (dRn.):  sahel  (3S.},  Harlan- dlh.—  I)  Hds,  vaür,  aber  unter  den  Wörtern für  J-;  -e  für  -ya,  %  26S.  32.
26446:mit  upa  'zerstören':  /rafa  upa.scanda- yeiii  mürS  .  .  uta  nmamm  Yt.  70.  18;  — upa  anyh  (näml  timanä)  sandayäti  Yt j  10.  28.
27684:•  '].  zanda-  m.  Name  gewisser  Häretiker*': ya'ha  'da{^V.) yatumsnia  m^rmcita gai%a as'ahe  V.7ÄSS; +F.20";  —  'dqmca  (GP.) yätumatqmca  Y.  61.  3.
28803:•  j.  'haosravah-  m.  EN.  eines  irani- schen Königs  aus  der  A'uz'aj'dyiiastie:  arsa airyanqm  dahyunam  xJdhrai  hanktr^mH (sd.)  'va  (NS.)  Yt.5.49.  a)  sonst  mit kavay-:  ayaslam  amahrkim  bavdhi  ydkia kava  *'va  Az.7'>;  *Vyt.2'';  —  haomS .  . him  ja^yal . .  dazdi  mL.ya'ia  aam  banda- yeni  . ,  läirTm  fraarasyämm  . .  uta  bastftn upanayeni  bastsm  kavSi^  'vanhahe^  janäi t>m  kava  'va  .  .  pu%rü  iama  (sd.)  syä- var/anäi  Yti).  i7f.;  /p.77,  93,  ^5.32;  — ahurS  kava  'va  Ytig.yj;  —  uynm  ia- valm  i^amiS  .  .  yat  upa^hacat  kavaltn •vanhitn  Yt /p.  73f.;  S. /.  9;  —  yc^a  as>m uzayeni  ha^a  iavlfis 'vamkahe'^  Yt.  15.  2^ ; Ny.  J.  S ;  —  kavsis  kaosravatihs  ai'aonS  Yt J.?-i3a-

=== SOD blind ===
6975:        ynskryy~                                                             blind
17980:                                                                              blind           ©ob. -y; pi. -/; ob. pi. -ty ^kwr>k
17996:                                                                              blind
18043:         blind-hearted
29187:       10, 218; Frag. Len. 51.1, 17; MSP p53                    blind
29192:8825 sm'yr B, M                                                blind-born
30224:      nightblind                                                   sivkos ©Skt. sivaghosa =»syPkwsh
36786:          blind                                                11371 zp'rtyh =» zp'rty*
37788:(to)bc troubled     365                  blind    1127,5032,5035,8836,          (^)bow    6607
37790:   10740                                 blind-born    8837                     bowl   1767
37791:between the brows    1142                blind-hearted    5041                  bowman     3610
38986:nightblind    9179                      not having eaten      5750           ocean   5304, 8823, 8833, 8834
```


## [2026-09-04T19:50:31.532Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^ *1127 \\| 1127 \" SOD_pages.txt | head; echo \"---5032---\"; grep -n \"5032 \\|5035 \" SOD_pages.txt | head; echo \"--- context around line 6975 ---\"; sed -n '6960,6990p' SOD_pages.txt"
}
```


### [2026-09-04T19:50:31.619Z] TOOL RESULT

```
6971:       VJ 992; GMS 367, 372          r                                 1127 >nt' B                                    j/
---5032---
17977:              (/cOdo                                                     5032 kwr'
17993:                                                                         5035 kwr>k B
--- context around line 6975 ---
                                                                             GcOshow
                                                                             GMS 657; BBB; TSP 7.94; 13iil0; BSTBL; VJ 960;
      anskafe ^ptsk'p-
      splitted                                                                 KG; MSP b67; Frag. Len. 101 Rl; AVS 92
      BBB 542; GMS 968; Sogd. Cpds. 145.3                              1126 'nsystyy M                                        ? <»yLJ
                                                                            ansistc ? © Aw. ham-sisto; hi&wat-        ©pp.
 1114 'nsk'np B                                          (Jl*<jl*r
      anskamb ©<*ham-skamb-              ^sk'np
      world                                                                  BBB  493 ?
                                                                             pressed

       VJ 992; GMS 367, 372          r                                 1127 >nt' B                                    j/
                                                                            and Ond) ©Av. anda\ Khot. hana% Parth. hand\
 1115 'nsk'r- B                       j^.h^id^J'^^^d-^-                        Orm. ond
      anskar Osqr-, }nskr-)       ©<*ham-skar- ©inf.
        ynskryy~                                                             blind

       (to)pick up, (to)coUcct                                               BSTBL, Dhy. 184; GMS 283; Hen. Brahman. 110
       VJ 1037, 1016; GMS 709, 921                                             n 2; Bailey. Prolexis. 384
 1116 >nskr- => 'nsk'r-                                                1128 >nt: B, S
 1117 >nskrt-      B                                                         and ©<hanti ©3pl. prcs. ^'st'nt, xnd, ynt1. xnt
      anskart      ©pt. st.                        ■a_A/^*^" *0-^^*"         GMS 765; AVS 224
       (fo)collcct
                                                                       1129 >nt»c B =* >nt>c
       GMS 860; VJ 1019, 1037; AVS 103                                                                               f-1^ *CT^ "J^
                                                                       1130 »nt>c B
 1118 »nskrt»y B                                                             andac     Ont'c) ©<*ham-taca      ©ob. -y
      anskartc Onskrtk) ©pp.                                                 group, assembly
       picked up                                                             TSP; BSTBL; Frag. Len. Ilc2; GMS 655 n 1
       VJ 1038, 1017                                                   1131 »ntVnt(y) B                                ^-r ^j/
                                                                            andacand(c)
```


## [2026-09-04T19:50:48.391Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\np='SOD_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find index of line containing \"1127 >nt'\"\nfor i,l in enumerate(lines):\n    if \"1127 >nt'\" in l:\n        idx=i; break\nprefix='\\n'.join(lines[:idx])\nleaf=prefix.count('\\f')\nprint('leaf(0-based)',leaf,'-> printed approx',leaf-66)\nimport re\nm=re.findall(r'\\[pdf page (\\d+)\\]', prefix)\nprint('last pdf tag', m[-5:] if m else None)\nEOF"
}
```


## [2026-09-04T19:50:49.714Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor i,l in enumerate(lines):\n    if \"anda-  Adj.  'blind'\" in l:\n        idx=i;break\nprefix='\\n'.join(lines[:idx])\nprint('leaf',prefix.count('\\f'))\nprint(lines[idx-3:idx+3])\nEOF"
}
```


### [2026-09-04T19:50:50.014Z] TOOL RESULT

```
leaf(0-based) 109 -> printed approx 43
last pdf tag None
```


### [2026-09-04T19:50:52.034Z] TOOL RESULT

```
leaf 108
['ai.  anlasthä-  Adj.', '•  j.  antama-  Adj.  i)  \'der  innerste\':  \'ma aiwi.varma  "das  innerste  Kleidungsstück" (d.  i.  das  Hemd)  V.  7.10;  —  \'ma  aiwyi- fthänS  Vd.  /2  \'*.  —  2)  \'der  vertrauteste, intimste\':  *°m3mcit\'\'\'^  sanhs-n  "auch  das vertrauteste  Wort"  F.  j  eJ\'.', "SuperL,  S.  'antara-.  —  ai.  anlama-  Adj.  —  Pü. : aiidarliim,  (zu  Vd.):  ha/diar.  —  ')  zSt.  Bthl. IF.  77,  115.  —  »)  Hds.  x^t>mHi\\  s.  Bthl.  IF. II,  13t.  —  1>  Pü.  erl.:  ligBn  razikä.", "•  j.  anda-  Adj.  'blind':  n^il  ava  zaoi^ra paiti,vlse  yä  mävsya  frattuhannti  'dssca tNPm.)  ..  Yt.5.93.", 'ai.  andhä-  Adj,  —  Falsches  BB.  /.  203.', '•  j.  \'anya  Adv.\'\'  i)  \'andernfalls,  sonst\'; aolS.iarasca  . .  ya^a  aii°  spä..\x0cya1ia  an\' i\'jhrka  "schädlicher  . ,  als  sonst  der  Hund']
```


## [2026-09-04T19:50:58.979Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport json,re\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nprint(d['BRT'].get('page_offset'))\nEOF\necho \"=== KLN amber ===\"; grep -n \"^amber\" KLN_1966.txt | head"
}
```


### [2026-09-04T19:51:00.736Z] TOOL RESULT

```
Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
=== KLN amber ===
2421:amber,  n.  —  ME.,  fr.  OF.  (=  F.)  ambre,  fr.  Arab. 'anbar,  ‘ambergris’.  Cp.  It.  ambra,  Sp.,  Port. ambar,  alambar,  which  all  derive  fr.  Arab,  an- bar.  Cp.  also  amariUo.  Cp.  also  ambrosia  and the  second  element  in  next  word  and  in  Liquid- ambar,  pomander.
2423:ambergris,  adj.  —  F.  ambre  gris,  ‘gray  amber  . For  the  first  word  see  amber.  F.  gris  is  borrowed fr.  Frankish  *gris,  which  is  rel.  to  Du,  grijs,  ‘gray’, OS.,  OHG.,  MHG.  gris,  ‘gray’,  G.  Greis,  ‘old man’,  and  prob.  also  to  OE.  grasg,  ‘gray’.  See grizzle,  ‘gray’,  and  cp.  gray  and  words  there  re¬ ferred  to.
2424:amberite,  n.,  an  explosive.  —  Formed  fr.  amber with  subst.  suff.  -ite;  so  called  because  it  re¬ sembles  amber.
```


## [2026-09-04T19:51:08.022Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor pat in [\"amber,  n.\",\"ana-,  pref\"]:\n    for i,l in enumerate(lines):\n        if l.startswith(pat):\n            print(pat,'leaf',('\\n'.join(lines[:i])).count('\\f'))\n            break\nEOF\necho \"=== KLN ana- ===\"; grep -n \"^ana-,\\|^ana,\\|^an-,\\|^analysis\\|^analogy\\|^anatomy\\|^unless\\|^umbrella\\|^umbra,\" KLN_1966.txt | head -20"
}
```


### [2026-09-04T19:51:09.778Z] TOOL RESULT

```
amber,  n. leaf 43
=== KLN ana- ===
496:anatomy
2583:an-,  a-,  priv.  pref.  —  Gk.  av-,  a-,  ‘not,  without’, rel.  to  ve-,  vr;-,  v-,  of  s.m.  (see  nepenthe),  and cogn.  with  OI.  an-,  a-,  L.  in-,  Goth.,  OE.,  etc. un-,  of  s.m.  See  priv.  pref.  un-.
2584:an-,  form  of  ana-  before  a  vowel.
2585:an-,  assimilated  form  of  ad-  before  n.
2587:ana-,  before  a  vowel  an-,  pref.  meaning:  1)  up, upward;  2)  back,  backward,  against;  3)  again, anew;  4)  exceedingly;  5)  according  to.  —  Gk. ava-,  dtv-,  ‘up  to,  upward,  up,  toward;  exceed¬ ingly;  back,  backward;  against’,  fr.  ava,  ‘up, on,  upon;  throughout;  again’,  rel.  to  avw, ‘above’,  and  cogn.  with  Avestic  ana,  ‘on,  upon’, L.  an-  in  anheldre,  ‘to  pant,  gasp’,  Goth,  ana, OE.  on,  an,  OSlav.  na,  Lith.  mi,  OPruss.  no,  na, ‘on,  upon';  fr.  I.-E.  base  *ano-,  ‘on,  upon, above’.  Cp.  on  and  a-,  ‘on’.  Cp.  also  the  pref. in  anhelafion.
2589:ana,  n.,  collection  of  memorable  sayings  of famous  men.  —  Coined  fr.  -ana,  neut.  pi.  of Latin  adjectives  ending  in  the  masc.  sing,  into -anus;  abstracted  from  the  ending  of  names  like Johnsoniana,  etc.  See  -ana.
5690:umbrella.
40727:umbra,  n.,  shade,  shadow  (of  a  planet).  —  L. umbra,  ‘shade,  shadow’,  of  uncertain  origin.  It is  possibly  cogn.  with  OI.  dndhas-,  ‘darkness’, andhdh,  Avestic  ando,  ‘blind’.  For  the  suff.  -bra in  umbra  cp.  the  suff.  in  L.  tenebrae  (pi.),  ‘dark¬ ness’.  See  Ernout-Meillet,  DELL.,  p.  745  s.v. umbra.  Cp.  Rum.  umbra.  It.  ombra,  F.  ombre, ©Proven?.,  Catal.  ombra,  ‘shade’,  which  all  de¬ rive  fr.  L.  umbra,  and  Catal.,  Sp.,  Port,  sombra, ‘shade’,  which  come  fr.  VL.  subumbrare,  ‘to cast  shade  upon’.  Cp.  umbel,  umber,  ‘the  gray¬ ling’,  umbrage,  umbrella,  umbrette,  adumbrate, adumbration,  penumbra.  Cp.  also  somber,  som¬ brero.
40823:unless,  conj.  —  Fr.  earlier  onlesse,  ontesse  that, i.e.  ‘on  less  that’.  Cp.  F.  a  moins  que,  ‘unless’, lit.  ‘on  less  that’,  and  see  on  and  less, unmeet,  adj.,  not  meet;  unsuitable.  —  ME.  un- mete,  fr.  OE.  unm&te,  ‘not  meet’.  See  priv.  pref. un-  and  meet,  adj.
```


## [2026-09-04T19:51:20.262Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ntargets={2421:'amber',2583:'an- priv',2587:'ana- pref',40727:'umbra',40823:'unless'}\nfor ln,name in targets.items():\n    i=ln-1\n    leaf=('\\n'.join(lines[:i])).count('\\f')\n    print(name,'line',ln,'leaf',leaf,'est printed pages',2*(leaf-12),2*(leaf-12)+1)\nEOF"
}
```


## [2026-09-04T19:51:21.131Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^analysis\\|^analogy,\\|^anatomy,\\|^umbrella,\\|^analyse\\|^analyze\" KLN_1966.txt | head"
}
```


### [2026-09-04T19:51:22.084Z] TOOL RESULT

```
amber line 2421 leaf 43 est printed pages 62 63
an- priv line 2583 leaf 47 est printed pages 70 71
ana- pref line 2587 leaf 47 est printed pages 70 71
umbra line 40727 leaf 887 est printed pages 1750 1751
unless line 40823 leaf 890 est printed pages 1756 1757
```


### [2026-09-04T19:51:22.129Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:51:27.326Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor n in (42,43,44,46,47,48):\n    txt=leaves[n]\n    nums=re.findall(r'^\\s*(\\d{2,4})\\s*$', txt, re.M)\n    print(n, nums[:8], '|', txt.strip()[:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T19:51:28.887Z] TOOL RESULT

```
42 ['58', '59'] | tles  of  the  family  Chryso- melidae  (entomol.)  —  ModL.,  fr.  Gk.  aXxixoi
43 ['60', '61'] | I.-E.  *am-ro-, fr.  base  *am-,  ‘bitter’,  which  is  rel.  to  *omo-. Taw,  u
44 ['62', '63'] | like  food’.  Cp.  Arab.  * unbar  (pronounced  ‘d/n- bar’),  ‘ambergris’,  and 
46 ['66'] | SpneXog,  ‘vine’,  and  elSos, ‘form,  shape’.  See  ampelo-,  -oid  and  -ous. 
47 ['67', '68'] | se  to  gape  idly  about’,  fr.  a, ‘to’  (see  a),  and  muser,  ‘to  muse’.  
48 ['69', '70', '71'] | o peel’,  and  E.  cleave,  to  split  (q.v.)  Cp.  the  second element  in  hie
```


## [2026-09-04T19:51:34.170Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"analysis,\" KLN_1966.txt | head -3; echo ---; grep -n \"anatomy,\" KLN_1966.txt | head -3; echo ---; grep -n \"analogy,\" KLN_1966.txt | head -3; echo ---; grep -n \"umbrella,\" KLN_1966.txt | head -3"
}
```


### [2026-09-04T19:51:34.273Z] TOOL RESULT

```
2637:Derivatives:  analogical  (q.v.),  analog-ist,  n., analog-ist-ic,  adj.,  analogize  (q.v.) analphabetic,  adj.,  not  alphabetic.  —  Formed  fr. privative  pref.  an-  and  alphabetic, analysis,  n.,  separation  of  a  whole  into  its  com¬ ponent  parts.  —  Gk.  dvdXuai?,  ‘a  loosing,  re¬ leasing’,  fr.  dvaX’jEiv,  ‘to  unloose,  release,  set free’,  fr.  dvd,  ‘up,  on,  throughout’  (see  ana-),  and Xueiv,  ‘to  unfasten,  loosen,  slacken’.  See  lysis, analyste,  n.,  a  person  who  analyzes.  —  F.,  formed fr.  analyser,  on  analogy  of  nouns  in  -iste  (E. -ist)  fr.  verbs  in  -iser  (E.  -ize).  See  prec.  word and  cp.  analyze.
23680:metamorphosis,  n.,  change  of  form,  transforma¬ tion.  —  L.,  fr.  Gk.  (jtexapiiptpcooLi;,  ‘transfor¬ mation’,  fr.  [.isxauopcpouv,  ‘to  transform’, which  is  formed  fr.  ptexa  (see  meta-),  and  piop- rpoijv,  ‘to  give  form  to’,  fr.  jj.opcprj ,  ‘form, shape’.  See  morpho-  and  -osis. metanalysis,  n.,  the  analysis  of  words  or  groups of  words  into  elements  contrary  to  their  struc¬ ture,  as  an  adder  for  a  nadder.  —  Coined  by  the Danish  philologist  Otto  Jespersen  (1860-1943) fr.  met-  and  analysis.
23816:microanalysis,  n.,  the  chemical  analysis  of  very small  quantities.  —  ModL.,  compounded  of micro-  and  analysis.
---
2087:alar,  adj.,  1)  pertaining  to  a  wing;  2)  winglike; 3)  in  anatomy,  axillary.  —  L.  alaris,  of  the wing’,  fr.  ala,  ‘wing’.  See  aisle.
2676:anatomic,  anatomical,  adj.  —  F.  anatomique,  fr. L.  anatomicus,  fr.  Gk.  dvxxo {X'.yAz,  ‘relating  to anatomy,  skilled  in  anatomy’,  fr.  dvaxo[ztd. See  next  word  and  -ic,  resp.  also  -al. Derivative:  anatomic-al-ly,  adv. anatomy,  n.  —  F.  anatomie,  fr.  L.  anatomia,  fr. Gk.  dvaxopid,  avaxopd),  ‘dissection’,  which  is related  to  dvaxdpvetv,  ‘to  cut  up’,  fr.  dvd  (see .  ana-)  and  x^veiv  ‘to  cut’.  See  tome  and  cp.
3863:atomy,  n.,  skeleton.  —  From  misdivision  of  ana¬ tomy  into  an  atomy.  See  anatomy, atomy,  n.,  pygmy.  —  L.  atomi  (pi.  of  atomus, ‘atom’),  mistaken  for  a  singular.  See  atom, atone,  intr.  v.  —  Short  for  ‘to  be  at  one’.
---
2636:dvdXoyov,  neut.  of  dvdXoyo;;.  See  prec.  word, analogy,  n.,  similarity.  —  F.  analogic,  fr.  L.  ana- logia,  fr.  Gk.  dvaXoyia,  ‘proportion,  analogy’, fr.  dvdXoyop.  See  analogous  and  -y  (represent¬ ing  Gk.  -ta).
21376:*Xey-cu;),  ‘speech,  diction’,  Xoyo;,  ‘word, speech,  discourse,  account,  thought,  reason’. Alb.  mb-l'ed,  ‘I  gather,  collect,  harvest’.  Cp. alexia,  Alogians,  analects,  analogue,  analogy, apologetic,  apologize,  apologue,  apology,  coil, colleague,  collect,  college,  curiologic,  Decalog, dialect,  dialogue,  diligent,  duologue,  dyslogy, eclectic,  eclogue,  elect,  election,  elegant,  eligible, elite,  epilogue,  eulogy,  florilegium,  intellect,  in¬ telligent,  lectern,  lection,  legal,  legation,  legend, legible,  legion,  legislation,  legitimate,  legume, lesson,  lexicon,  ligneous,  logic,  logos,  monologue, neglect,  negligee,  paralogy,  predilection,  prole¬ gomena,  prologue,  recollect,  religion,  sacrilege, select,  sortilege,  syllogism,  tetralogy,  trilogy.  For the  ending  of  lecture  see  suff.  -ure.
22073:logometric,  adj.,  serving  to  represent  graphically chemical  elements  ( chem .)  —  Compounded  of logo-  and  Gk.  pirpov,  ‘measure’.  See  metric, logos,  n.,  the  divine  Word.  —  Gk.  Xoyop,  ‘word, speech;  word  which  expresses  the  inward thought;  the  thought  itself;  tale,  story;  maxim, proverb,  narrative;  prose;  ratio,  reason ;  rela¬ tion,  proportion,  analogy,  calculation,  reckon¬ ing,  account;  discussion,  deliberation,  dia¬ logue-,  fr.  Xcyciv,  ‘to  pick  out,  choose;  to  speak, declare",  and  cogn.  with  L.  legere,  ‘to  gather, collect;  to  pick  out,  choose;  to  read,  recite’.  See lecture  and  cp.  logic,  logistic,  adj.,  -logue,  -logy, Alogians,  apologue,  curiologic,  Decalog,  dialect. Cp.  also  paralogism,  syllogism, logothete,  n.,  name  of  various  officers  of  the  By¬ zantine  empire.  —  ML.  logotheta,  orig.  ‘an  au¬ ditor  of  accounts’,  fr.  Gk.  XoyoffETr)?,  which  is compounded  ofXoyog,  ‘word,  speech;  account', and  -Derr,!:,  a  derivative  of  Fr,-,  the  stem  of -iDcvai,  ‘to  place,  set,  lay  down'.  See  logo-  and theme.
---
40727:umbra,  n.,  shade,  shadow  (of  a  planet).  —  L. umbra,  ‘shade,  shadow’,  of  uncertain  origin.  It is  possibly  cogn.  with  OI.  dndhas-,  ‘darkness’, andhdh,  Avestic  ando,  ‘blind’.  For  the  suff.  -bra in  umbra  cp.  the  suff.  in  L.  tenebrae  (pi.),  ‘dark¬ ness’.  See  Ernout-Meillet,  DELL.,  p.  745  s.v. umbra.  Cp.  Rum.  umbra.  It.  ombra,  F.  ombre, ©Proven?.,  Catal.  ombra,  ‘shade’,  which  all  de¬ rive  fr.  L.  umbra,  and  Catal.,  Sp.,  Port,  sombra, ‘shade’,  which  come  fr.  VL.  subumbrare,  ‘to cast  shade  upon’.  Cp.  umbel,  umber,  ‘the  gray¬ ling’,  umbrage,  umbrella,  umbrette,  adumbrate, adumbration,  penumbra.  Cp.  also  somber,  som¬ brero.
40731:Derivative:  umbral-ly ,  adv. umbrella,  n.  —  It.  ombrella,  fr.  Late  L.  umbrella, alteration  of  L.  umbella,  ‘a  little  shadow,  sun¬ shade,  umbrella’,  dimin.  of  umbra.  See  umbra and  -ella  and  cp.  umbel.
```


## [2026-09-04T19:51:41.996Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LAT umbra ===\"; grep -n \"^umbra,\" LAT.txt | head -3; echo \"=== LEW umbra ===\"; grep -n \"^umbra\" LEW_1910.txt | head -5; echo \"=== SYN BLIND ===\"; grep -n \"BLIND\" SYN.txt | head -10"
}
```


### [2026-09-04T19:51:42.069Z] TOOL RESULT

```
=== LAT umbra ===
69533:umbra, -ae f.: 1“ ombre, produite par un corps interpos 4 entre
=== LEW umbra ===
=== SYN BLIND ===
5263:4.97 BLIND
8222:4.97 BLIND Grk. —_ rvdAbs Goth. blinds Lith. aklas NG tupr6s, orpaBds ON blindr Lett. akls, neredzigs Lat. caecus Dan. blind ChSl.  slépit It. cieco, orbo Sw. blind SCr.  slijep Fr. aveugle OE blind Boh. — slepy Sp. ciego ME blind Pol. §lepy Rum. orb NE blind Russ.  slepoj Tr. dall, goll Du. blind Skt.  andha- NIr. _caoch, dall OHG blind Av. anda- W. dall MHG blint Br. dall NHG blind
```


## [2026-09-04T19:51:43.039Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SKT ===\"; grep -n \"^AMBER\\|^UMBRELLA\\|^UMBRAGE\\|^ON \\|^UNLESS\\|^ANALYSIS\\|^ANATOMY\" SKT.txt | head"
}
```


### [2026-09-04T19:51:43.093Z] TOOL RESULT

```
=== SKT ===
20408:UMBRAGE.
```


## [2026-09-04T19:51:48.712Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ni=8221\nprint('leaf',('\\n'.join(lines[:i])).count('\\f'), '-> printed', ('\\n'.join(lines[:i])).count('\\f')-24)\nprint('\\n'.join(lines[8221:8240])[:2500])\nEOF"
}
```


## [2026-09-04T19:51:49.247Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '69533,69560p' LAT.txt"
}
```


### [2026-09-04T19:51:50.397Z] TOOL RESULT

```
leaf 365 -> printed 341
4.97 BLIND Grk. —_ rvdAbs Goth. blinds Lith. aklas NG tupr6s, orpaBds ON blindr Lett. akls, neredzigs Lat. caecus Dan. blind ChSl.  slépit It. cieco, orbo Sw. blind SCr.  slijep Fr. aveugle OE blind Boh. — slepy Sp. ciego ME blind Pol. §lepy Rum. orb NE blind Russ.  slepoj Tr. dall, goll Du. blind Skt.  andha- NIr. _caoch, dall OHG blind Av. anda- W. dall MHG blint Br. dall NHG blind
Of the words for ‘blind’ only a few are connected with those for ‘eye’ or ‘see’. Some have come through ‘squinting, one-eyed’, and this was probably the sense of the inherited group, Lat. caecus, etc., (below, 2). Some are from such general notions as ‘mixed, confused’ or ‘bereft’.
1. Grk. rupdés, also of objects ‘dim, obscure’ : ri¢w ‘stupefy with smoke’, Goth. daufs ‘insensible’ (of the heart), ON daufr ‘deaf’ (4.95). Walde-P. 1.840.
NG ozpaBés ‘crooked’ (12.74), also (through ‘squint-eyed’) ‘blind’.
2. Lat. caecus (> It. cieco, Sp. ciego) : Ir. caech ‘one-eyed’, ‘squinting, blind’ (K. Meyer, Contrib. 297), NIr. caoch ‘blind, dim-eyed’ (‘blind’ by influence of Latin?), W. coeg ‘empty, foolish’ (coeg-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
ddall ‘half blind’), Goth. haths ‘one- eyed’, cf. Skt. kekara- ‘squinting’. Walde-P. 1.328. Ernout-M. 128. Walde-H. 1.129.
It. orbo (but also ‘bereft, orphaned’), OFr., Rum. orb, fr. Lat. orbus ‘bereft, deprived’, with late Lat. specialization fr. phrases like orbus lumine, perh. as- sisted by association with orbis in the sense of ‘eye’. Ernout-M. 710. REW 6086.
Fr. aveugle, OIt. avocolo, fr. a late Lat. *ab-oculus, a medical term like and prob. modelled on Byz. aaéuparos ‘blind’. REW 33. Wartburg 1.7.
3. Ir., W., Br. dall, prob. : Goth. dwals ‘silly’, OF dol, OHG tol ‘foolish’, Grk. @odés ‘mud, dirt’ (esp. in water), ford ‘make turbid (of water), con
extension of *dheu- ‘blind’, ON daufr Walde-P. 1.842. 1 seconds media), Ol coll S 1.236.3 gl. ‘luscum but or perh. : Skt. kana ‘per- , Grk. Keddas’ povopian- *kel- ‘prick’ (?). 1,436. Pedersen 1.157. h : Lat. caecus (above, 2). nds, etc., general Gmc., ed, troubled’, cf. Ir. Tupros, etc.) : Goth. blandan ON blanda, OF blandan, OHG trouble’, ChSl. bledq,
rch.;
pos
Walde-P. NIr. caoe ‘ 4, Goth. bli rob. (as ‘confus
¢
p
dall, Grk. ‘ix with’, O blantan ‘O)X;
blesti ‘go astray’, etc. Falk-Torp 82. Feist 100.
Digitized by Arya Samaj Foundation Chennai and eGangotri
```


### [2026-09-04T19:51:50.438Z] TOOL RESULT

```
umbra, -ae f.: 1“ ombre, produite par un corps interpos 4 entre
la lumibre et la terre} a° ombrage, place A 1 'ombre, objet donnant
de 1'ombre: umbrae uocabantur Meptunalibus casae frondeae pro taber¬
naculis, P.F.‘sitf, x, et par suite "asile, protection"} 3 0 ombre, par
opposition au corps qui la produit, d'ou "inage sans consistance,
semblant"} et au pl. umbro* "les ombres" des morts} 4 0 comme le gr.
oxia, personnage non inrit 4 amen 4 par un conrire (comme son ombre)}
5 0 ombre, ombrine, poissons. - Ancien, usuel et classique} panroman,'
sauf espagnol et portugais. M.1.9046,
DArirAs et composAs: umbella et dans les gloses umbrella (refait
sur umbra) : ombrelle (Mart., Jur., cf. Rich, s.u.), M.L.9049} umbrilla:
oxCcnvcx, poisson (GELoss.)}
umbrosus (cl&ss.), M.1.9050} umbraculum: ce qui donne de 1 ’ombre,Orneo
- 1.318 -
ombrage(s), parasol (= <JxCac)j M.L.9047; umbrSticus ; umbrStilis :
qui se passe A 1'ombre, retir£ (par oppos. k forensis , cf.gr.oxia-
Tpocpeay etc.); umbrSticulus (Pl., Tru.6x1)j umbraliter-, figurdment
(S^ Ang.); unbrSticS "en apparence" (Cassiod.); umbro,-Ss: onbrer
(surtout podtique), M.L.9048, avec ses composds: adumbrS , t. des
peintres "esquisser" (cf. OXtaypacpeTv), M.L.308, d'ob adumbrStiS,
adumbrStim-, in-, ob-, prae-, * sub-umbrO M.L.8045; unbrStiO (tardif);
umbrifer (podt.).
Le rapprochement' avec skr. andhdh * av. andO "aveugle" et v^d.
dndhah "obscuritd" est plausible; pour le suffixe, cf.lat .tenebrae.
Qme 5 , - 5 s, - 5 re: etre humide (snrtont podt.).
Formes nominales et d^riv^s: Unor n.: hnmidit d (abstr. et concret),
£ 14 ment liquide; liquide en g^ndral, humeur. - Ancien (Pl.), clas¬
sique, usuel. umidus : liquide, humi de (s'oppose a terrenus)umiditSs
```


## [2026-09-04T19:51:59.684Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in range(360,372):\n    txt=leaves[n]\n    nums=re.findall(r'\\b(\\d{3})\\b', txt[:200])\n    print(n, nums[:6],'|', txt.strip()[:100].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T19:52:01.333Z] TOOL RESULT

```
360 [] | v, plesiv calvo OE aie ee Boh. _lysy, pleSivy, pleSaty chau ME alled, calou Pol. lysy ; ean ek NE ba
361 [] | break, bend, twist’, some from the name of a part affected (as ‘hip’), some prob- ably of imitative 
362 ['564', '406'] | inken ‘limp’ (= ON hinka, etc.) : Skt. khavj- ‘limp’, khafija- ‘lame’, Grk. oxatw ‘limp’, ON skakkr 
363 ['528'] | dible’, prob. (as orig. ‘indistinct’ of sound) fr. the root in susurrus ‘muttering, whisper’, susurr
364 [] | utolo Sw. stum SCr. nijem Be et OE dumb Boh.  némy s, —imudo ME = dumb Pol. — niemy a mut NE dumb Ru
365 ['290', '101'] | l. Ph. 39.290 te 7. Skt. maka- : Lat. mitus, (above, 2). Av. afravaoca-, neg. cpd., second part : fr
366 ['307', '531'] | ‘see’. 6. ChSl. slépi, etc., general Slavic (cf. also vb. ChSI. oslipnati, OBoh. oslniiti ‘make blin
367 [] | an, Pol. pijany, Russ. p’janyj (old mid. pple.? Cf. Meil- 4.99 NAKED, BARE Grk. —-yupvds Goth. nagap
368 ['122'] | nt, tt. nekumane Da! : a nekus ‘evening’ Hitt. Gram. 122 f.). : 9, NG -youuv6s, . ues by associa- ‘ 
369 [] | eed on’ as homely words use The’ gabsti- (perh. : Lat. tergére ‘rub off’, terere ‘rub’, ing’ oF yulg
370 ['559'] | l. pitéti ‘feed’, etc. (5.12). Pedersen 2.559. W. bwyita, fr. bwyd ‘food’ (5.12). Br. dibri, MBr. di
371 [] | rd originally denoting some special kind of food comes to be FOO. d whe special of If *ed- ‘eat’ (5.
```


## [2026-09-04T19:52:22.663Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LKT ambra/anbar ===\"; grep -n -i \"anbar\\|ambra\\|ambergris\\|Ambra\" LKT.txt | head -20"
}
```


### [2026-09-04T19:52:22.717Z] TOOL RESULT

```
=== LKT ambra/anbar ===
237:Auch  tk.  'Pferd  mit  weißen  und  schwar- zen Füßen'.  Hieraus  rum.  abra§  'ge- fleckt, buntscheckig',  tig.  'Unheil  ver- kündend'; im  walachischen  Dialekt iabrai^,  iambra^  'Pferd  mit  weißen Flecken'.
396:78.  Ar.  'anbar:
397:Mit  Assimilation  'ambar  gesprochen; hieraus  it.  ambra,  frz.  ambre,  sp.  pg. ambar,  [mit  ar.  Art.]  alambar,  alambre, rum.  ambrä,  ambru;  engl,  ambre,  ndl. amber,  dtsch.  Amber;  russ.  ambra.  — Aniber  ist  eine  ihrer  Herkunft  nach zweifelhafte,  ilirer  Zusammensetzung nach  unvollständig  bekannte,  sehr  teure, dunkelgraue  Masse,  die  in  früheren Zeiten  in  der  Medizin  hochgeschätzt war,  während  sie  heute  fast  nur  noch zur  Herstellung  von  Parfümen  benutzt wird.  In  rundlichen  oder  kantigen Stücken  auf  dem  Meere  schwimmend oder  am  Strande  angespült,  wird  die Ambra  im  Indischen  Ozean  gefunden und  für  feine  Sorten  je  kg  5000  Mark und  mehr  gezahlt.  Vermutlich  ist  der Amber  die  verhärtete  Kotmasse  des Pottwals  Catodon  macrocephalus  Lac. —  Dazu  engl,  yellow  amber  'Bernstein'. [DE  188/9.  Eguilaz  258.  ML  441. Gorjajew  4.
1614:'Parfüm  aus  Moschus  und  Ambra';  hier- aus sp.  algalia,  pg.  algälia  'dass.';  mlat. galia  muscata,  sp.  pg.  gato  de  algalia [Constancio  Dicc  50  b]  'Zibetkatze,  Vi- verra  civetta  Schreb.'.
1852:b)  Mit  ar.  musk  'Moschus'  [s.  hier Nr.  1701]  wird  ar.  habb  al-niusk  'Hibis- cus  abelmos(  hus  L.' ;  hieraus  sp.  abel- mosco,  pg.  abehnosco,  abelmoscho  [Con- stancio Dicc  4a:  'ambarina'],  frz.  abel- mosc,  abelmosch,  ndl.  abelmosch.  Da  der Duft  ihrer  Blüten  wie  der  von  Ambra und  Moschus  zusammen  ist,  heißt  sie auch  frz.  ambrette,  ndl.  amberbloem  [zu
1853:Ambra,  s.  hier  Nr.  78];  vgl.  DE  51. Dozy  Oost  51.    Devic  DEt  1.
2125:'Röte,  Rotlauf  [vom  Stamme  ahmar 'rot',  aus  dessen  fem.  hamra',  mit  ar. Art.  al-hamra'  'die  Rote'  der  Namen Alhambra  jenes  wunderbaren  maurischen Schlosses  auf  der  Höhe  von  Granada geworden  ist] ;  hieraus  sp.  alfombra, gewöhnlich  alfombrilla  'Masern'  [Dicc Gast  120  a].  —  Vom  gleichen  Stamme ist  sp.  alhamar  'rote  Decke'  [ebenda 123  b].
4167:'Trank'  [Vb.  sariba  'trinken'],  hieraus mlat.  siröpus,  sirüpus,  it.  sciroppo,  si- roppo,  frz.  sirop,  syrop,  prov.  isarop, kat.  aixarop,  sp.  jnrope,  pg.  xarope, enxarope,  rum.  sirop,  sirup;  ndl.  siroop, stroop  [in  Südhmburg  dial.  sroep,  vgL GRM  V,  171],  dtsch.  Sirup,  engl,  syrop, syrup;  russ.  sirop,  serb.  sirup,  äech. syrup,  poln.  syrop.  —  Aus  der  gleich- bedeutenden ar.  Form  surba,  sarba wurde  zur  Bezeichnung  eines  kühlenden Trankes  über  tk.  serbet  'Kühltrank'  it. sorbetto  'süßes  Fruchteis'  [mit  Einwir- kung von  it.  sorbire  'schlürfen'],  frz. Sorbet,  sp.  sorbete,  pg,  sorvete,  rum.  ger- bet 'dicker  Obstsaft';  ndl.  sorbet,  engl. sherbet,  shrub,  dtsch.  Sorbet,  Scherbet 'ein  aus  Wasser,  zerstoßenen  Rosinen, Zucker,  Zitronensaft,  Ambra  und  ähn- lichen Zutaten  gemischter  Kühltrank'. [DE  218  und  417.  Eguilaz  495  und  513. ML  7675  und  7711.
4899:'Musiker'  [part.  praes.  act.  I  des  Vbs. zamara  'pfeifen,  blasen'],  plr.  zamara; hieraus  kat.  sambra,  pg.  snnibra  'nächt- liches Fest  der  Mauren,  Freudengeschrei'. [DE  363/364.    Eguilaz  523/524.
4981:'Abbäs  I.  4 'Äbbäs  Pascha  507 Äbutilon  14 Adamsapfel  19 Ädenia  venenata  20 Adhatoda  1161 Ägypten  1222 Ailantus  glandulosa  1141 ^Zc«Z(J  1021 Alcdntara  1057 .4Zei)^;o  792 Algarve  674 Alhambra  882 Aljarafe  (de  Sevilla)  1840 ^/fco/jo/  1227 Almagra  1349 Amber  78 Amocklaufen  71 Anakonda  74 Antiaris  toxicaria  2136 Antilope  saiga  1774 .4rafta  90 ^rec«  1 7 Argali  96
6950:ambra  78
7314:sac  1781 ^acre  1799 safareig  1767 safata  1753 sap-«  1784 sa^ep  20ül sambra  2191 saraguells  1849
8714:iäbangiü  921 iaba^a  945 iabrci^  9 «öca  927 «ac?e^  922 idhnie  926 iama  923 iambras  9 iamurluc  924 ianicer  954 iasmin  942 iasomie  942 «atac  945 iatagan  944 iaurgiü  960 «awri  960 iavaq  946 iava^a  945 «6Hc  894 ibripm  10 ibri^in  10 «cfef«  900 «edec  948
```


## [2026-09-04T19:52:23.801Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PLA anbar ===\"; grep -n -i \"anbar\\|ʿanbar\\|'anbar\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20; echo \"=== AFM عنبر ===\"; grep -n \"عنبر\" AFM_pages.txt | head -10; echo \"=== TAD عنبر ===\"; grep -n \"عنبر\" TAD_pages.txt | head -10"
}
```


### [2026-09-04T19:52:23.877Z] TOOL RESULT

```
=== PLA anbar ===
1059:pers. ab —> ar. nb 2. B.: ambar > ar. Sanbar 
2366:scheinlich = ’isbäanbar s. ’isbänbar 7 
3045:—mp.>r hanbar ap. hambara 4 syr. fyaatlao 5, 
3049:ol - ”anbar = “anbar s. “anbar . 
3051:ob 21 - ”anbarbäris = ’ambarbäris s. ”’anbarbäris . 
7211:Frau -Zulanbar = Julanbär s. &ulanbär 7, 
7212:Se = Zulanbari: Nisba v. 6 $ulanbar s. Bulanbar. 
12625:u _ süsanbar: "Mentha aquatica, Wasserminze; sismbrium, wilde Thyme, 
12695:ge — sisanbar = süsanbar q. v. . 
13336:„u- Sambar: "Reifen" ägypt., Ar. pers. „e&anbar T mp. Dep Sambar. 
14668:sd - tanbür: "Laute mit langem Griff" pers. ls. tanbar . 
14935:Sanbar 204 Ja ir 
14938:nie _ Canbar: "Amber" pers. 1 m. >o- ambar — ar. Sanbar °, it. 
=== AFM عنبر ===
=== TAD عنبر ===
```


## [2026-09-04T19:52:31.594Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '14925,14960p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; echo \"=== line 1050-1065 ===\"; sed -n '1050,1070p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt"
}
```


### [2026-09-04T19:52:31.655Z] TOOL RESULT

```
3. Mackenzie s. v. 

4. Macuch S. v. 

5. Fremdwörterbuch s. v., Wahrig s. v. 
6. Nyberg Bd. II s. v. 

7. Chista Bd. 10 S. 1191. 


Sanbar 204 Ja ir 


nie _ Canbar: "Amber" pers. 1 m. >o- ambar — ar. Sanbar °, it. 


ambra, frz. ambre, sp., pg. ambar, engl. ambre, dtsch. Amber, russ, 

ambra 3, syr,nyael 4 

ey. - Sanzarüt: "Knochenleim; persischer Augenbalsam" < pers. a, 
anzarüt, mand. Sanzarüt, syr. 63%. 


ao y6c _ © andnäma: "Farman, Vertrag" pers. 5, aus ar. 4s Sand + pers »b 
näme "Buch, Brief" mp. s£ı nämak - 


& 


Jun _ al-gal: "Türschloß" pers. 6 ?. 


\\u£- gabirä: "berauschender Trank" aus pers. &/ Li gobäriyya "staubig" 7, 

=== line 1050-1065 ===
pers. & > ar. 
pers. > ar. 
pers. 8 > ar. 
pers. 2e> ar. 
pers. g B>, ar. 
pers. g ar. 
pers. 13 ar. 
pers. mar. 
ar. bärfuba 
pers. ab —> ar. nb 2. B.: ambar > ar. Sanbar 

pers. a > ar. lL 2. B.: pers. taranfabin — mp. taranguben —> ar. 
taranabil 

pers. h>>ar. bh z. B.: pers. gonäh gonäh > ar. Bunäh 

pers. h/e >ar. E z. B.::pers. barnäme mp. barnämag —> ar. 
barnäm 

pers. hle > ar. q 2. B.: pers. parwäne —T mp. parwänag "> ar. 
farwänaq
```


## [2026-09-04T19:52:40.729Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD ambar ===\"; grep -n -i \"ambar\\|'nbl\\|hambar\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n -i \"ambar\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-04T19:52:40.798Z] TOOL RESULT

```
=== PHD ambar ===
PHD.txt:125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
PHD.txt:191:amāwandīh: power, strength. ambag [’mbk' | N anbajat] a preserve, conserve. ambar [mbl, ?nbl | Аг. ‘праг ambergris. ambarag [?mblk! | N anbara] hairless (animal). Р amburdan [h/^mbwultn! | Р ?mPr-] = hambārīdan. a-menīdār [^mynyt!l] unthinking. āmēxtan, āmēz- Pmyhtn', ?тус- | M *myxtn, ?myz-, N ~] mix. ~išn: mixture; element. āmiz [^myc] side dish, vegetables. āmēxtan, āmēz-, read hammóxtan, hammoóz-. Amurdād [?m(w)rdt' | N murdád] Immortality, the sixth Amahraspand, guardian of plants and food; cal. sth month; 7th day. āmurzīdan, āmurz- [mewlc-ytn! | M?mwrz-yd, N ~) forgive, pity, have mercy on. ~išn: mercy, forgiveness. Р amwaštan [h|mwstn! | P ?mwst] gather, collect. an- Pn- | M ’n-] prevocalic privative prefix, un-, -less. ап [ZK < A zk;?n! | M Ап, N ~] that, he. ~ 1: that of; with a qualifier preceding a noun, equivalent to a following 1 e.g. ап i ahlawàn ruwān = ruwan i ahlawān, the souls of the righteous. -ап [2s! | M An N ~] suffix forming (i) present participles, (ii) adverbs, (iii) plurals. ānāb-, —išn, v. ānāftan. an-ābādān Ppp’ rn'] uncultivated. an-abaxšāwand [m ph} wnd] unrepentant. ~ih: unrepentance. an-abāy Pr’ Pd) unfitting, improper. an-abēdān [”7?5yt?x'] useless, unwanted. ~th: uselessness. anübublag [9 fwhlk' = Av. anüpers0a-] inexpiable, unatonable; the highest degree of sin. an-abzār Pwi] unskilled, incapable. ~th: inability. an-ādān [*77:?x!] insolvent. ^h : insolvency. an-ádüg [tk] incapable. an-afsēnišn [”77?syx$n!] indestructible. ānāftan, ānāb- [77ftn',*775- | M ?w pt, Qn m-)] avert, reject, frustrate. ~išn: avoidance, warding off. anág [77 k! | M >ре} evil. ~th: evil, harm. an-ügàh и: | N ndgah] unaware, unwitting. anüg-kardàr [RU АРД, -kunisn [-kwnšn'] evil-doer, maleficent. anagr Pngl) infinite. ~an [”x! | M?nyr^n] Infinite Light; cal. 30th day.
PHD.txt:296:čābuk [c’Swk! | N ~] agile, nimble; excellent. ~th: agility. čādur [c?twl | N ~] sheet, veil. éagad [ck*t! | (N ¿ahad), J ¿eyad] peak, summit. сабаг [cki] wife (of the second degree). саһ [ол | N ~] pit, well. čahār [ALBA < A?rb‘; ch?l | M с, N ~] four. ~dah [cl’ldh | N ~] fourteen. ~-рау [cb Ip d | N ~ > čārwā] quadruped. čakēk [ckwk | N ~, cakáwak] lark. čakuč [cktwc | N čakuš] hammer. čambar [cmbl | N ~] circle, hoop. čamišn [cmšn! | M cmbyšn (?)] urination; lavatory. ` бапа [спа | = M, N ~] how many, much?; so many, much; some, a few. ~ih: amount, quantity. čandal [cndl | N ~] sandalwood. čandīdan, čand- [cnd-ytn! | (M cn-ystn)] tremble, quake. ~išn: trembling, movement. čang [eng | M bung, N ~] harp. ~-sray [-sPd] harpist. са�� [c7] = Carag. багар [clk' | M erg] pasture, grazing; flock. čārag [c?]k! | N ~a] means, remedy. ~garih [-glyh] ability, savoir faire. Carb [с/р | P crb, N ~] mild, gentle; fatty, oily. ~ih: gentleness; fattiness. ~išn [-sn'] fat, oil. ~і&потапа [-šrwmnd) oleaginous. Carm [с/т | M crm, N ~] skin, hide, leather. čārūģ [c wk! | N čārū] lime, mortar. „ēn [-yn!] limy. Carz [сіх | N ~] bustard. čāšīdan [c'$-ytn!] = čāštan. čašm [A YNE < A ‘ynh; ст | = M, N ~] eye. léaSmag [cfmk! | М cšmg, N ~a] spring, source. tčašmaģ [cfmk!] renowned. čašmaģāh [cšmk?s | M csmg’h] obvious, public, notorious. ~ih: notoriety, condemnation. čašm-arešk [cém ?ly$k!] envious. ^h: envy. čašm-dīd [cšm dyt'] visible, obvious. čāšnīg [c nyk! | M спус, N čāšnī] taste.
PHD.txt:566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
PHD.txt:780:ambergris ambar.
PHD.txt:811:apostle fréstag, paygambar; v. pro- phet. .
PHD.txt:1236:circle čambar.
PHD.txt:1273:collect (vt.) hambaridan, harrēb-, P amwaštan.
PHD.txt:1931:fill āgandan, hambaridan.
PHD.txt:2189:hairless ambarag.
PHD.txt:2308:hoop éambar.
PHD.txt:4577:čarbišn čim čambar čamišn sang!
PHD_mackenzie.txt:1006:ambar ['mhl, )nbll Ar. Canbar] ambergris.
PHD_mackenzie.txt:1007:ambarag ['mblk l I N anbara] hairless (animal).
PHD_mackenzie.txt:1008:P amburdan [hj>mbwltn' I P )mb)r-] = hambaridan.
PHD_mackenzie.txt:1709:   tambar [embll N,...,] circle, hoop.
PHD_mackenzie.txt:2685:hamblridan, hambAr- [hm-, hnb)l-ytn I M hmb)r-, N anbardan] fill,
PHD_mackenzie.txt:4556:sisimbar [sysymbl, -nbll N sisambar] sisymbrium, wild-thyme.
PHD_mackenzie.txt:5946:ambergris ambar.                          archives dewiin.
PHD_mackenzie.txt:6186:circle <:ambar.                             rasidan; - to an end 0 ham madan.
=== NYB ===
1875:hanbārak [hnb’lk'] storehouse, larder 973-8.9.10, . MPrth ’mb’rg; Arm. lw. (h)ambar, Talm. ’mbr’, NP anbār; v. Telegdi 229.
7482:ambarišt: paristätan
```


## [2026-09-04T19:52:42.249Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\np='incoming/BQT/BQT_v3_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('nleaves',len(leaves))\nhits=[i for i,l in enumerate(leaves) if 'عنبر' in l]\nprint('leaves with عنبر:',hits[:40])\nEOF"
}
```


### [2026-09-04T19:52:44.653Z] TOOL RESULT

```
nleaves 721
leaves with عنبر: [23, 124, 169, 175, 191, 208, 261, 325, 358, 534, 535, 618, 643, 672, 677, 689]
```


## [2026-09-04T19:53:01.176Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/ ; echo ---; find . -maxdepth 3 -iname \"*.pdf\" | head -20; echo ---; ls data/extracted | head"
}
```


### [2026-09-04T19:53:01.239Z] TOOL RESULT

```
ANOMALIES.md
extracted
EXTRACTION_SPEC.md
research
translations
verification
---
./EtymologicalDictionary-persian-english.pdf
---
batch
NEXT_CHUNK
RETRY.txt
test
```


## [2026-09-04T19:53:01.594Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,50p' tools/ref_page.py"
}
```


### [2026-09-04T19:53:01.634Z] TOOL RESULT

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
```


## [2026-09-04T19:53:07.144Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; SP=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 55 -l 55 -r 130 -png EtymologicalDictionary-persian-english.pdf $SP/p55 && ls -la $SP/p55*"
}
```


## [2026-09-04T19:53:07.602Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:1382 --image 2>&1 | head -60"
}
```


### [2026-09-04T19:53:09.076Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 55458 Sep  4 15:53 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p55-055.png
```


### [2026-09-04T19:53:15.476Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1382.png
REF: BQT:1382  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 175  OCR-lang: fas

زان هفدهم
در عین بی‌تقطه بانون مشتمل بر بیست ويك لغت و کنایت
عناب - پم اول واثانی مشدد بالف | نومید شدن و لاامید کردیدن باشد ۳
کنیده و یبای ابجد زده » میوه ایست ۱ شبیه عنان برءنان - کنایه از برابری
بسنجد ودر منشجات ومسهلات بکار برند:خوردن | وهمسری کردن باشد ۴ ۰
آن خون راصاف کند- عنان تافتی هکنایه از ءاجز شدن -
و کنایه ازلب ممشوق بآ وروی بر گردانیدن باغد ۴ .
هم هت . ۹ عنان دزدیدن -» کنایه از بازماندن
عناب ر - ۳2 باشد. +
بکر بای ابجد ( ۱ ( ی عنان زنان دفتن کنایه ازتمجیل
و فتح‌تا و سکون رای ۲ وشتاب رفتن باشد .
قرشت (۲) » کنایه از عناپ عنان سب کردن - کدابه از
انگفتان محبوب است. آهته براه رفتن و در کارها تأنی و تأمل نمودن
عنان امل سبلگ شدن سکنابه از | باشد .#۸
() چك: بکریا . (۲) چك : وسکون را .
«وانازناز (فر) «لك۷س4۷۸» << 1۳28۵ از تیره عنابها دارای میوه‌هایی که
بمنوان ملین بکار میرود «کل کلاب ۲۳۰ ورك: ثابتی ۱۹۸؛ ستوده ۰۱۵۸
۲ << عنان امل‌سبك کردیدن :
هم عنان امل سبك کردد هم رکاب اجل کران باشد . آلوری آبیوردی. «بهارعجم».
۴ - ترسم که روزحشر عنان برعنان رود تبیح شیخ وخرفةٌ رند شراب خوار .
« حافظ شیرازی ۱۹۷
۴ - ملك را بوقت عنان تافتن نشاید بدزدی ظفر پافتن .
نظامی کنجوی. «بهار عجم».
8 - دست اجل عنان املهاکند سبك چون استوار کشت رکاب کران تو .
سلمان ساوجی. «بهارعجم» .
# عنبر - بفتح اول وسوم, (عر) از عربی واردفرانوی (8۳18) 2010۳6 «لكص4۹۹*
وانگلیی 7 شده وآن ماده‌است درمثانديك جالوربسیاربز رک دربایی ازجنسجانوری که
درفرهنگهای فارسی «یال» («.م.) با«وال» ضبط شده. قسمی ازین جانور دریایی که حامل ء:برست
در لاتینی ۳212408 و درفرانسوی ۳-26108101 و درانگلیسی 416 و در آلمای
۵1 لامیده میشود. درکتب لغات جدید این کلمات را ماهی عنین » عنیر هاهی, شیرماهی
بقیه در صفحة ۱۳۸۳
( برقان قاطع ۱۷۸
```


## [2026-09-04T19:53:28.094Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p55-055.png"
}
```


### [2026-09-04T19:53:28.123Z] TOOL RESULT

```

```


## [2026-09-04T19:53:44.236Z] TOOL CALL #40: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T19:53:44.244Z] TOOL RESULT

```


```


## [2026-09-04T19:53:47.809Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82en",
 "prompt": "Give the full reconstruction, meaning, and the list of descendants (Avestan, Old Persian, Greek, Germanic/Gothic, Latin) with their forms and glosses. Quote exactly."
}
```


## [2026-09-04T19:53:48.762Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/amber",
 "prompt": "Quote the full etymology of 'amber', including the Medieval Latin and Arabic forms and the ambergris/amber semantic history."
}
```


### [2026-09-04T19:53:53.534Z] TOOL RESULT

```
# Proto-Indo-European *h₂én

**Full Reconstruction:** *h₂én

**Meanings:** 
1. "there, yonder, on the other side"
2. "otherwise"

**Descendants Listed:**

The page does not include Avestan or Old Persian descendants. Here are those documented:

- **Greek:** Ancient Greek ἄν (án)
- **Germanic:** Gothic 𐌰𐌽 (an, "so? now?")
- **Latin:** an
- **Balto-Slavic:** Lithuanian anàs, Old Prussian anga
- **Sanskrit:** अङ्ग (aṅgá, emphatic particle) and अन्त (ánta)
- **Celtiberian:** antos ("end, border")

The page notes the Greek form may derive from this root "or from a reanalysis of οὐ κάν (ou kán) as οὐκ ἄν (ouk án)."
```


### [2026-09-04T19:53:56.197Z] TOOL RESULT

```
# Etymology of Amber

The word "amber" originates from mid-14th century English, deriving from the phrase "ambre grice" meaning "ambergris; perfume made from ambergris." The term came through Old French and Medieval Latin from Arabic *'anbar*, which referred to "ambergris, morbid secretion of sperm-whale intestines used in perfumes and cookery."

**Key semantic development:** Initially, the term designated ambergris specifically. However, in late medieval Europe, the designation expanded to encompass Baltic fossil resins. As documented in the source: "In Europe, the word *amber* was extended to fossil resins from the Baltic (late 13c. in Anglo-Latin; c. 1400 in English)."

The two substances were historically distinguished: "French distinguished the two substances as *ambre gris* and *ambre jaune*" (gray amber and yellow amber respectively). The connection between these meanings may stem from both materials being "found washed up on seashores," though scholars acknowledge the possibility that Baltic amber represents "a different word entirely, of unknown origin."

Notably, the Romans knew Baltic amber as *electrum*, recognizing "its static electricity properties." This ancient term connects etymologically to the modern word "electric," coined in the 1640s to describe substances that attract others when rubbed, like amber.
```


## [2026-09-04T19:54:02.681Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%80%CE%BD%CE%AC",
 "prompt": "Quote the Ancient Greek ἀνά etymology section in full: the PIE reconstruction given, and the cognates listed (Avestan, Old Persian, Gothic, Old English, Old Church Slavonic, Lithuanian)."
}
```


## [2026-09-04T19:54:04.393Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9%D9%86%D8%A8%D8%B1",
 "prompt": "Quote the Arabic عنبر entry: etymology, meanings, and any statement about its origin (Persian, unknown, etc.). Also quote the Persian عنبر section if present."
}
```


### [2026-09-04T19:54:07.835Z] TOOL RESULT

```
# Summary of ἀνά Etymology

The article provides the following PIE reconstruction and cognates:

**PIE Reconstruction:** LIPP reconstructs Proto-Indo-European *áno ("up, over, along").

**Cognates listed:**
- Avestan: 𐬀𐬥𐬀 (ana)
- Latin: an- ("up") in an-hēlō and an-testor
- English: on

The text states: "Cognates include Avestan 𐬀𐬥𐬀 (ana), Latin an- ('up') in an-hēlō ('to gasp'), an-testor ('to call up as a witness'), and English on."

**Note:** The document does not list Old Persian, Gothic, Old English, or Old Church Slavonic cognates for this entry—only Avestan, Latin, and English are mentioned.
```


### [2026-09-04T19:54:09.750Z] TOOL RESULT

```
# Etymology of عنبر (Ambar)

## Arabic Origin

The Arabic term **عَنْبَر** (ʕanbar) has two distinct etymologies:

**Etymology 1 (Ambergris):** "From Middle Persian _ʾmbl_ (ambar, 'ambergris')."

**Etymology 2 (Storeroom):** "From Persian _انبار_ (anbâr)."

## Persian Connection

The document indicates that Arabic borrowed the word from Persian for the "storeroom" sense. The ambergris meaning traces back further to Middle Persian origins, which then passed into Arabic and subsequently into Ottoman Turkish and numerous European languages including English, French, Italian, and Spanish.

The word demonstrates a fascinating linguistic journey from Middle Persian through Arabic into multiple language families across Europe, Asia, and Africa.
```


## [2026-09-04T19:54:16.688Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/umbra",
 "prompt": "Quote the Latin umbra etymology section: the PIE reconstruction, what de Vaan or other sources say, and cognates (Sanskrit andhá-, Avestan anda-, Armenian, etc.)."
}
```


## [2026-09-04T19:54:17.227Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/umbrella",
 "prompt": "Quote the etymology of umbrella in full, including Italian ombrella, Latin umbella and umbra."
}
```


### [2026-09-04T19:54:22.829Z] TOOL RESULT

```
# Etymology of Umbrella

According to the Online Etymology Dictionary, the word "umbrella" originates from Italian *ombrello*, which derives from Late Latin *umbrella*—itself an altered form of Latin *umbella* "sunshade, parasol." The entry notes that this alteration was influenced by *umbra*, which means "shade, shadow." The *umbella* form functioned as a diminutive of *umbra*.

The core lineage traces back through these Romance and Classical Latin terms, all connected to the concept of shade and shadow as their fundamental semantic root.
```


### [2026-09-04T19:54:23.134Z] TOOL RESULT

```
# Latin *umbra* Etymology

Based on the Wiktionary content provided, here's what's documented about the etymology:

## PIE Reconstructions

The entry presents two theories:

1. **First theory**: Connected to Lithuanian *unksna* ("shade"), derived from PIE *\*wnksrā-*, tentatively linked to PIE *\*(H)wenk-* ("to bend"). However, the article notes: "the semantic leaps required to go from 'bend' to 'shade' are large and unlikely."

2. **Second theory**: If from Old Latin *\*omra*, possibly from PIE *\*h₂mr-u-* or *\*h₂mrup-*.

## Cognates Mentioned

The documented cognates include:
- Ancient Greek *ἀμαυρός* (amaurós, "dark")
- Luwian terms meaning "rot" and "rotten"
- Possible Semitic borrowing from root *\*ḥ-m-r* ("be red")

**Note**: The Sanskrit and Avestan cognates you mention are not included in this Wiktionary article's etymology section.
```


## [2026-09-04T19:54:36.710Z] TOOL CALL #47: WebSearch

```json
{
 "query": "de Vaan Etymological Dictionary of Latin umbra \"unksna\" *unksrā etymology"
}
```


## [2026-09-04T19:54:37.269Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/analysis",
 "prompt": "Quote the etymology of 'analysis' including Greek analysis, analyein, ana- and lyein."
}
```


### [2026-09-04T19:54:38.171Z] TOOL RESULT

```
Web search results for query: "de Vaan Etymological Dictionary of Latin umbra "unksna" *unksrā etymology"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T19:54:43.950Z] TOOL RESULT

```
# Etymology of "Analysis"

According to the Online Etymology Dictionary, the word "analysis" originates from Medieval Latin and Greek roots with a fascinating progression of meaning:

**Greek Origins:**
The term derives from Greek *analysis*, which meant "solution of a problem by analysis," literally "a breaking up, a loosening, releasing." This came from *analyein*, meaning "unloose, release, set free; to loose a ship from its moorings," and in Aristotle's usage, "to analyze."

**Component Breakdown:**
The Greek *analyein* breaks down into two elements:
- *ana-*: "up, back, throughout"
- *lysis*: "a loosening," derived from *lyein*, meaning "to unfasten"

The ultimate root traces back to the Proto-Indo-European *\*leu-*, which means "to loosen, divide, cut apart."

**Historical Development:**
The 1580s English sense emphasized "resolution of anything complex into simple elements" (positioned as the opposite of synthesis), while the meaning of "statement presenting results of an analytic process" emerged by the 1660s.
```


## [2026-09-04T19:55:00.019Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD Bd1 'an' preposition ===\"; grep -n \"an, anu, and, no\\|anu, and\\|^an\\b.*Präp\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"=== WLD Bd1 andho ===\"; grep -n \"andho\\|andhá\\|andha-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-04T19:55:00.092Z] TOOL RESULT

```
=== WLD Bd1 'an' preposition ===
=== WLD Bd1 andho ===
3846:Annehmlichkeit“ als *anja = aksl. vonja setzt; nicht melir zu *andhos 
4455:anti, anta — andhos 
11714:also blind kiimpft. urn dessentwillen man idg. *andho- ansetzte (FickH 4 
20720:Prellwitz 2 s. v. m. Lit., auch civdas ' poQeag. vn d Tvggyvcbv Hes. : ai. andha-
```


## [2026-09-04T19:55:01.629Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC ===\"; grep -n \"^ana \\|^ana,\\|^ano \\|^andho\\|^andhos\\|^andh\" IEC.txt | head -15; echo \"=== LEW umbra ===\"; grep -n \"umbra\" LEW_1910.txt | head -8"
}
```


### [2026-09-04T19:55:01.698Z] TOOL RESULT

```
=== IEC ===
517:ana (ono) “on, upon WP I, 57. Cf. ano Skt. (ambig.) a (postp. Here: SE, but EHS otherwise); Av. ana; Tokh. A cf. ana-pár, B ene-pre ‘facing’; Gk. aná; Osc. ana-, an- (a preverb identified usually with Lat. in-); Go. OFris. ana. (For an apophonic relationship with type eni, cf. Gk. eni, en: aná; epí: apó; perí: pará)
520:andhos (1): ondhos, q. v.
521:andhos (2) -es-, andhio “plant, flower. WP I, 67 Skt. ándhas; Arm. cf. onda- (in cpds. 'vege- table"); Gk. ánthos; EM Alb. end, ende *flow- er’. According to FH here belong OFris. an- dul, LG andel *marshgrass'
522:andhos (3), à, us “soul, spirit, rancour’. Cf. ano (1) Tokh. A añčän; Alb. àndé ‘pleasure’; Ir. éad ‘jealousy’; OHG anto ‘zeal, anger; ON ond, gs. andar, pl. -ir “breath, life, soul’; OE anda ‘grudge’
=== LEW umbra ===
8939:tumbr, tumbra I 370
```


## [2026-09-04T19:55:08.863Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^ondhos\" IEC.txt | head; echo \"=== WLD 11700-11725 ===\"; sed -n '11700,11725p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== WLD 4450-4470 ===\"; sed -n '4450,4462p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-04T19:55:08.938Z] TOOL RESULT

```
12169:ondhos (andhos? See andhos ( 1)) ‘dark, dingy, smoky; blind”. (Alleged Irish uinne ‘bling’ in- dicates a type *ondh-; Gaul. anda- ‘blindfold’ indicates a type *andh-. The composition of Gk. ánthrax, -akos, m. ‘coaľ is uncertain). Skt. andháh "dark blind; Hitt. cf. andaras
=== WLD 11700-11725 ===


ondho orghi-, jghi 


ondho- „blind, dunkel"? 

Ai. andhu-, av. anda- „blind, dunkel", vielleicht nacb Bezzenberger BB. 
1, 342 zu lat. umbra „Schatten“ (andere Deutungen von umbra s. bei Yf. 
LEWb. 2 s. v.); dafi mndl. andoren , ahd. (nd.) andorn , mhd. andorv, antom 
„Marrubium“ als ein Ausdruck wie „blinde Nessel“ verwandt sei (Lehmann 
IF. 21. 192), ist hochst fragwiirdig. 

(Gall.-) lat. andabata „ein Gladiator, der mit einem Helm oline Offnungen. 
also blind kiimpft. urn dessentwillen man idg. *andho- ansetzte (FickH 4 
15 zw.). mut! dock wobl das Praefix gall, mule- enthalten. Gr. voftog „un- 
ehelicb. Bastard 11 berechtigt keinesfalls zum Ansatz einer zweisilbigen Wz. 
onodk- oder anodh- (Bezzenberger aaO., Hirt Abl. 131) da „blind = heim- 
lich geboren“ eine lediglich konstruierte Bed.-Yermittlung ist. 

or-, or- ,,reden. rufen“. 

Ai. dryati „preisf‘. lat. oro, -are „causam agere, verbandeln (ebenso osk. 
urust). reden, sprechen, bitten" (kaum Denominativ von os „Mund“, da 
o. urust dann Lehnwort aus dem Lat. sein miiflte, s. Vf. LEWb. 2 548 m. Lit.): 

=== WLD 4450-4470 ===
konnte dies eine nachtragliche Gebrauchsangleichung infolge der Laut- 
ahnlichkeit sein, und idg. °nt(i, -at) „bis“ als „gegeniiber hin, auf die 



anti, anta — andhos 


67 


entgegengesetzte Seite hiniiber“ zu anti gehoren (so Fick III 4 30); auch 
die Worte fur „Ende“ (s. u.) sind ursprgl. das auf der gegenuberliegenden
```


## [2026-09-04T19:55:10.332Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; wc -l LEW_1910.txt; grep -n \"^umb\\|^unc\\|^unda\" LEW_1910.txt | head; echo \"=== FSD amber ===\"; grep -n \"^amber,\" FSD_vol1.txt | head -3"
}
```


### [2026-09-04T19:55:10.406Z] TOOL RESULT

```
14865 LEW_1910.txt
659:unchati II 7382
9008:umb I 36
9935:uncud I 700
11240:unc I 48
=== FSD amber ===
```


## [2026-09-04T19:55:21.840Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('n',len(leaves))\nfor n in (177,178,179,180):\n    print('---- leaf',n,'----')\n    print(leaves[n][:1800])\nEOF"
}
```


### [2026-09-04T19:55:23.752Z] TOOL RESULT

```
n 232
---- leaf 177 ----
this palace, by the favor of Ahuramazda, I after- wards built (to completion).
A’Sa = ARTAXERXES II, Susa А.
1 Qty : Artaxfagà : XS : vazraka : XS : XŠyänām : XŠ : DHyinim : XS : ahyiya : BUyà : Darayavausahya : XShya : риса : D
2 ürayavaufahyü : Artaxšaçāhyā : XShya : puça : Artaxsagahyà : Xšayārcahyā : XShya : риса : XSayarcahya : Dara
3 yavaudahyd : XShyà : puça : Dérayavausahya : Vi Stáspahya : puça : Haxamünesiya : imam : apadina : Dàrayavaus$ : apantyikama : ak
4 unas : ab*yapara : upi : Artazíagüm : n*yàkama :+++-+ : vafná : AM : Ата : щй: Мга : imam : apadüna : adam : аитат :AM:A
5 nah*ta : uid : M'bra : тат: pdtw : hacá : vispā : дазїй : Ша : imam : tya : akundm : má : vijanátu : mà : vinàttayátiy
Nore то A*Sa: Lines 4-5 are restored after the OP
text of А?На and the АКК, version of A’Sa.
TRANSLATION оғ А9: Saith Artaxerxes the Great King, King of Kings, King of Countries, King in this earth, son of Darius the King, of Darius (who was) son of Artaxerxes the King, of Artaxerxes (who was) son of Xerxes the King, of Xerxes (who was) son of Darius the King, of Darius (who was) son of Hystaspes, an Achaemen- ian: This palace Darius my great-great-grand- father built; later under Artaxerxes my grand- father it was burned; by the favor of Ahuramazda, Anaitis, and Mithras, this palace I built. May Ahuramazda, Anaitis, and Mithras protect me from all evil, and that which I have built may they not shatter nor harm.
A'Sb = ARTAXERXES II, Susa В. adam : Artaxšaçā : XS : vazraka : XS XSyani : XS : Darayavaus : XShyà : puça Nore то A'Sb: The XS after XSyana is a ditto-
graphie insertion, to which nothing corresponds in the other two versions.
TRANSLATION ОЕ А290: ... (= А?$а 1, with omissions).
A’Sc = Artaxerxes II, Susa c. 0 Dérayavausahya : XShya : puça : 0 Dérayavausahya 
---- leaf 178 ----
 : hya : Dārayavauš : XS : руё : Haxdmanigiya : Mitra : mam : paluv
Nore то АНЬ: Probably the demonstrative imam stood before apadānam at the beginning, and other
155
phrases of the protective prayer may have stood at the end.
TRANSLATION oF Á?Hb: This palace, of stone in its column(s), Artaxerxes the Great King built, the son of Darius the King, an Áchaemenian. May Mithras protect me ...
A'Hc = Artaxerxes II, HAMADAN C. 1 baga : vazraka : Auramazda :hya : тайа : 2 baganam : һуа :imàm : bümim : ada : 3 һуа : avam : asmánam : ada : hya : martiya 4 m : айа : һуа : &y&tim : ада : martiyahy 5 & : hya : Artaxšaçām : XSm : akunaug : ai 6 vam : parünàm : XSm : aivam : parünàm : 7 framataram : ðātiy : Artaxšaçā : XS : va 8 zraka : XŠ : XSyinim : X8 : DHyünám :XS 9 : ahydya : BUya : adam : Darayavausahy 10 à : XShyà : риса : DarayavauSahya : Artax И Sacahya : XShya : puça : ArtaxSacahy 12 & : XSayarSahy3 : XShya : риса : Хау 13 arsahya : Dàrayavausahyà : XShya : p 14 uça : Dārayavaušahyā : Vištāspahyā : nā 15 ma : puça : Haxämanišiya :ðātiy : Artaxša 16 (à : XS : vagna : Auramazdaha : adam : XS :8 17 hyaya : BUyà : vazrak&yà : düraiy :a 18 piy : amiy : Auramazda : xSagam : manā : frába 19 ra : màm : Auramazda : pátuv : uta : xSaca 20 m : tyamaiy : frábara : матау : vilam TRANSLATION OF A?He: M. 1-7. A great god is Ahuramazda, the great- est of gods, ... (= A!Pa 1-8). 82. 7-15.... (= A'Sa D: I (am) ... (= A'8a 1-2), son of Hystaspes by name, an Achaemenian. §3. 15-20. Saith Artaxerxes the King: By the favor of Ahuramazda I am king in this great carth far and wide; Ahuramazda bestowed the kingdom upon me. Me may Ahuramazda protect, and the kingdom which he bestowed upon me, and my royal house.
A?P = ARTAXERXES ÍT or IIT, PeRSEPOLIS.
: Parsa :
: Мада :
3 iyam : Üvja :
4 iyam : Parf
---- leaf 179 ----
8. This is the Arab. 19. This is the Egyptian. 20. This is the Armenian.
21. This is the Cappadocian. 22. This is the Sardian. 23. This is the Ionian. 24. This is the Scythian across the sea. 25. This is the Skudrian. 26. This is the Petasos-Wearing Ionian. 27. This is the Libyan. 28. This is the Ethiopian. 29. This is the man of Maka. 30. This is the Carian.
A’Pa = ARTAXERXES III, PERSEPOLIS А, B, C, D. 1 Бара : vazraka : Auramazda : hya :' 2 упал : bümàm :adà : һуа :a 8 vam : asmünàm : ada : һуа : marti 4 yam : adi : hya : &yatàm : adi : mart ` 5 ihyà : һуа : mim : Агіахёаса : х$ауз 6 буа, : akunaus : aivam : parüvnàm :
[4
Т xšāyaðiyam : aivam : parüvnüm. 8 : framatàram : Вапу : Artaxsagà : 9 xšāyaðiya : vazraka : xsayaftya 10 :xšāyaðiyanām : хёйуабуа : 11 DHyünàm : xSayafiya : ahyàyà : BUyā : ada 12 m : Ártax faga : хёйуа | 13 буа : puça : Artaxsacd : Darayavau 14 š :xšāyaðiya : puça : Darayavaus : A 15 rtaxéacà : xSaya@iya : puça : ArtaxSa 16 cà : XSayarsa : хїйуайуа : puça : X 17 šayāršā : Dárayavaus : xšāyað 18 iya : puça : Darayavaus : Vistaspa 19 hyà : пата : риса : Vistaspahya : 20 ÁrSàma : пата : puça : Haxàmanisi 21 ya :08tly : ArtaxSacd : xSiyafh 22 ya : imam : ustašanām : aðaganām : ma 23 m : upd : mam : kartā : 0tiy : Arta 24 xSacd : xSayabiya : mam : Auramazda : 25 ша : Міга : baga : pàtuv : uta : ima 26 m : DHyaum : uta : tya : mam : kartā : Notes TO АЗРа: The text is arranged according to the line-divisions of copy a, with faithful representation of all orthographic errors; all four copies have identical orthography, though the line-divisions vary somewhat. 12 The translation of lines 12-20 is intended to show the anacoluthic use of the nominative forms; the passage is obviously intended to convey the same ideas as Аа 1-3. 2 For ир@ тат ‘in my titne’ (h
---- leaf 180 ----
d: LX (units) in weight.
‚.. (= Wb ЕЎ).-
157
INSCRIPTIONS ON SEALS SDa = Darius, SEAL A: adam : Darayavaus XS SDb = Darius, SEAL B: adam : Dàrayavaus
SXa = XERXES, SEAL A: 1 X Sayarsa 2: ХБ : vazraka SXb = XERXES, SEAL B: 1 adam : X Say
2 агба : XS SXc = Xerxes, Seat c: 1 adam : Xšayāršā : XS D mure Sa = SEAL A: 1 Arša 5 yüba 2 ka :n 6 ušna à ата: 7 hyä: ‚4 Adi 8 puça Sb = Sear B: 1 Hadaxaya PNE EE 9 Вадаба, : ...
Sc = SEAL c: Vasdasaka
Sd = белі р: Vahyavisdipaya
Se = SEAL E: 1 ma : Xa 2 га 3 dašyā
Sf = SEALF:lupà 2 Arta 3xSac 44am Notes: Se: For Justi’s reading Xifyáráü, see Lex.
s.v. Xaršadašyā. Sf: There is no word-divider after upd. TRANSLATION. OF THE SEALS:
SDa: I (am) Darius the King.
SDb: I (am) Darius. -
SXa: Xerxes the Great King.
SXb~c: I (am) Xerxes the King.
Sa: Arshaka by name, son of Athiyabaushna.
Sb-e: ???
Sf: Under Artaxerxes.
Vase INSCRIPTIONS.
XVs = XERXES, VASE: XSayar 84 : XS : vazraka AVsa = ARTAXERXES, VASE A:
: Ardaxeakea : XS : vazraka AVsb-d = ARTAXERXES, VASES B, C, D: ArtaxSaca : xSayabiya
TRANSLATION: XVs: Xerxes the Great King. AVsa: Artaxerxes the Great King. -
AVsb-d: Artaxerxes the King.
158
OLD PERSIAN
HISTORICAL APPENDIX |
I. THE ÅCHAEMENIAN DYNASTY
Darius and the other Persian Kings who have left us cuneiform inscriptions composed in Old Persian, all belonged to the Achaemenian line, so called because they were descended from Achaemenes. Full information may be found in PW 1.200-204 s.v. Achaimenidai, and under the names of the individual persons? a complete gene-
alogical table is given by PW facing 1.192. A table of the most important Achaemenians is given here; the names of the kings are in large and small capitals, with the dates of their reigns, and an asterisk marks those Achaemenians who are named in the Old Persian inscripti
```


## [2026-09-04T19:55:28.890Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in (186,187,188):\n    print('---- leaf',n,'----')\n    print(leaves[n][:2500])\nEOF"
}
```


### [2026-09-04T19:55:30.598Z] TOOL RESULT

```
---- leaf 186 ----
� asn. DPd 20; DNa 53; XPh 43, 59; XSc 4°. ata- таш DPd 22; DNa 54; XPh 60. aitä apf. XPh 30, 35.
Ainaira- sb. ‘Ainaira’, a Babylonian, father of Nidintu-Bel; Elam. ha-a-na-a-ra, АКК. a-ni-ri-’, Ainaliralhya gsm. DB 1.77f.
atva- adj. ‘one’ ($150; §204.1): Av. aéva- ‘one’, Gk. Hom. olos, Cypr. orros ‘alone’, pIE *ozyos. ашат, asm. DNa 6, 7; DSe 6°, 6f; DSf 4, 5; DE 8f, 10; XPa 4, 5; XPb 8f, 10; XPe 4, 5; XPd 6, 7; XPf 6, 7; XPh 5,6; XE 9, 10; XV 7, 8; A!Pa 6f°, 8°; A?He 5f, 6; А?Ра 6, 7.
aiš- vb. ‘hasten’, caus. azSaya- ‘send’: Av. aes-, caus. aéaya-, Skt. 15-, caus. esayatz (§117).
fra + aiš- caus. ‘send forth’: Av. fraei-, Skt. .
preg-. frdiSayam ist sg. imf. (§24, §72, 6181, §215) DB 1.82; 2.19, 30, 50, 72f, 82; 3.2, 18, 30, 84; 5.7. frütsaya imf. DB 3.55, 60, 71.
Auliyüra- sb. ‘Autiyara’, a district in Ar- menia: Elam. ha-u-ti-ja-ru-i§, АКК. ú-ti-ņa-a-ri. Auliyàra nsm. DB 2.58f.
Aura- (Le. A*ura-) sb. ‘Lord, God’: Av. ahura-, Skt. dsura- ‘demon’, pIE *esuro- (6148.1). Aurahya Mazdaha gsm. ({36.ГУЬ, $44) XPe 10. Аита ism. DPe 24 (otherwise Bv. BSLP 30.1.70-3, Gr. §179, 8889; ‘downward’, isn. of aura-, zero- grade of avara-, comparative of *ava-, cf. Ау. aora ‘down’). Elsewhere always in cpd. Auramazdah-.
Auramazdāł- sb. ‘Wise Lord, Ahuramazda’, supreme deity of the Zoroastrian religion: Av. пет, ahurd mazda, РМ. óhrmazd, NPers. hormizd; Elam.. u-ra-más-da., Akky u-ra-ma-az-da. ü-ri-mt-
=
-
LEXICON
12-00 a-hu-ru-ma-az-da-’ ete., Gk. 'Opouacdys; in Av., always two words, usually separated in the Gathas and often in reverse order (Kent, Or. Stud. Hon. Pavry 200-8), but in OP always one word except ХРе 10 (844; for Ашт alone, see under Aura-). Cpd. of *ahura- (see Aura-) + *ma(n)dzdhà- with s-suffix (another! view by Pisani, ef. $185.n3); this is cpd. of pIE *menth- (or is the full grade pIE *math-?) seen in Gk. ёшабо› ‘I learned’, + pIE *dh&- ‘put’, see “da- (Pisani, Riv. Stud. Or. 81-2, takes prior element as *mns-, zero-grade to pAr. manas-, after Wacker- nagel-Debrunner, Altind. Gram. 3.282-3): for formation, ef. Skt. érad-dhà- ‘trust’, Lt. crédit. 670, $156.I, 5160.11; decl., $185.IV.
Auramazdà nsm. AmH 7, 10; AsH 5f, 12; DB 1.12, 60; 4.35, 55, 62, 74, 76, 79f; 5.15f; DPd 1, 7, 13, 15f, 23; DPh 8, 9; DNa 1, 31, 51f, 55; DNb 1, 46, 49: DSe 1; DSf 1,8, 14, 57; DSp 1; DSs 1^, 6f; DSt 1?, 7; DZe 1; DE 1; DH 6f, 8; XPa 1, 18, 20; XPb 1, 21; XPc 1, 12, 15; XPd 1, 17; XPf 1, 45, 48; XPg 12; XPh 1, 32, 49f, 52, 57, 60; XSc 4f°; XE 1; XV 1, 25; A!Pa 1°, 22°; A?8
---- leaf 187 ----
t built, unrepaired’; neg. a- + pte. of kar- ‘make’. {akarta] nsf. DSe 47 (conj. of Kent, JAOS 54.43).
azíaina- adj, with kdsaka-, ‘turquois’ (so Bleichsteiner, WZKM 37.103-4, and Konig, Burg- bau 63-4, but considered dubious by Hinz, ZDMG 95.235-6; hardly ‘gray amber’, with Hz. AMI 3.05—7, ApI 232; not ‘hematite’, with Scheil 21.29- 30): Av. arSaéna- ‘dark-colored’, borrowed in Gk. Порто “Atevos ‘Black Sea’ (‘in-hospitable’, by Gk. popular etymology, and euphemistically changed to Еф о), from neg. a- + z&atna-, cf. Av. xSaéta- ‘shining’ (§102, 5147.1). azšaina nsm. DSf 39.
axsata- adj. ‘unhurt, undisturbed’: neg. a- + pte. of xSan- ($102, §242.1), Skt. ksanóti ‘injures’, Gk. ктен, ‘kills’ (otherwise Foy KZ 35.49, Hz. Apl 70-1). azšałā nsf, DPe 23.
aguru- sb. ‘baked brick’ (8158.1). lagurum] asm. DSf 53, supplied by König, Burgbau 52, after a-gur-ru of the АКК. text, ef. NPers. ágür in the same meaning. alg|ura[và] Ism. DB 4.89 (restored by Kent, JAOS 62.267, after König, Klotho 4.45); but read амуй аһа with Cameron.
agriya- adj. ‘topmost, excellent, loyal’: Av. ayrya- ‘first in quality, etc.’, Skt. agriyd- agryd- ‘foremost, principal, etc.’, deriv. ($144.1V) to Av. ayra ‘der erste, oberste; (nt.) Anfang, Spitze’, Skt. dgra- ‘foremost, prominent, best; (nt.) tip, sum- mit, best part’ ($148.I). agriya пет. DB 1.21, as read by Cameron, replacing KT’s ag*r^ ++ (and the restorations thereof: dgar[ia] Wb. ZDMG 61.725, Tm. Vdt. Stud. 1.9, ef. Bthl. WZKM 22.72; ágra"|6a] Jn. Indian Stud. Lanman 255-7; ügr[mata] Konig, RuID 65; ágr[mà] Hz. Арі. 59- 62).
aciy adv. ‘then, at that time’ ($291.1V): Av. ajčit ‘and indeed’, Lt. ecquid (interrog.) ‘anything’, pIE *ed-g*id, see *a- ‘this’ and particle -cty ($105, $130; Ву. BSLP 33.2.152-3; Hz. AMI 4.125-6, 8.41, ApI 55-6; Wb. ЖА 41.319). ХРЇ 21.
Atamaita- sb. ‘Atamaita’, an Elamite rebel: Elam. Atameta (854.I, §76.V; Hüsing ар. Prašek,
166
IMP 2.78.08; König, Кир 78; not Umamaita after the Ummaima of Oppert, Médes 158, based on Rawlmnson’s J-im"im*^, later altered by KT's тт). {[Ajtamacta nsm. DB 5.5.
_ ütar- sb. ‘fire’: Av. diar- dór-, NPers. абат; in Á ciyadiya- and verhaps in Acina- ($152.Г).
atar (i.e. ачат), prep. with ace., ‘within, among’: Av. antara, Skt. antar, Lt. inter, pIE tenter (831). DB 1.21; 2.78; 4.32, 92; XPh 30, 35.
ali-, prefix, ‘beyond, across’: Av. aiti, Skt. dti, Gk. ёт ‘yet, longer’, Lt. et ‘and’, pIE *eti ; with ay-, yam-. Cf. also айту.
abaga- (ie. аба"да-) sb. ‘stone’: Av. asanga-, NPers. säng, 
---- leaf 188 ----
’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadtya- ‘truth’, with late loss of h-, + deriv. of d-baud- ‘be fragrant’, cf. Av. baoót- ‘fra-
OLD PERSIAN
grance’, therefore ‘having the fragrance of the truth’).  <Aé@iydbausinahya gsm. Sa 4-7.
Aéura sb. ‘Assyria (and Syria)’, a province of the Persian Empire ($6, $106.11): Elam. aš- &i-ra, АКК. áš-šur, Gk. 'Аттурв‚ but Aram. абиг. Aéuré nsf. DB 1.14f; 2.7; DPe 11; DNa 26f; DSe 26°; DSm 7°; XPh 22. Aéurayd lsf. (5186) DB 2.58f.
A@uriya- adj. ‘Assyrian’: deriv. to preceding .
($144.1), perhaps with vriddhi in first syllable (8126; Aburiya- ?). A@uriya пет. DN xvii; DSf 32; А?Р 17.
Agina- sb. ‘Acina’, ап Elamite rebel: Elam. ka-iš-ši-na, Akk. a-Si-na. Either borrowed from Elam. (Foy, KZ 37.498); or shortened from an IE name beginning with OP äç- = Av. átar- 007- ‘fire’ ($147.11, §152.1), ef. atoro-dáta- ‘Fire-given or Fire-created’ and other names (Vd. 18.52; Justi, INB 50; Bthl. AiW 324). Agina пет. DB. 1.74, 82: 4.10; DBe 1f. Acinam asm. DB 1.76.
Ld
A ciyádiya- adj. ‘Aciyadiya’, the ninth month, .
Nov.-Dec.: Elam. haššiyatiyaš, АКК. kislimu, Cpd. of átar- ‘Are’ + deriv. of yad- ‘worship’ ($126; $152.D: ‘Fire-Worship Month’. Agiyddiyahya gsm. DB 1.89; 3.18.
ada- adv. ‘then’: GAv. ald, LAv. ада, Skt. .
ба ‘therefore’ cf. Gk. трбе-бє (and -Gev) ^n front of’: pIE *e-dhe, to root in *a- ($76.11; $191.II); see also adakaty. — ada-taiy DNa 48, 45.
adakaiy adv. ‘then’: OP ada- + -kazy, Gk. aly. то ‘somewhere’, pIE *q¥ei, Isn. to int.-indef. stem ($135). DB 2.11, 24; 4.81, 82; DNb 38.
adam pron. “Р: Av. azam, Skt. adm, plE .
*eühom ($109), ef. pIE *ейб in Gk. yo, Lt. ego (8193.1). adam nsm. AmH 5,8; AsH 14; CMa 1; DB 1.1, 10, 12, 39, 52, 54 bis, 56, 59, 60, 62, 63, 64, 66, 67, 68 bis, 70, 72, 73, 75, 18, 82, 83, 86, 89, 91, 95; 23, 5, 6, 10°, 11, 15°, 19, 28, 30, 48, 50, 68, 64, 69, 72, 80, 81, 88; 3.1, 13, 25, 29, 50, 77, 80, 84; 48, 8, 11°, 14, 16, 19, 21, 24, 27, 29, 32, 40, 45, 59, 64, 71, 81, 89; 5.2, 6f, 13, 21°, 23°, 25°; DBa 1, 16; DBb 4, 6; DBe 5; DBd 3, 6; DBe 5, 8; DBf 3f; рве 5; DBh 4f, 8; ОВ: 4, 9; ОВ] 4; DPd 20; DPe 1, 7; DPh 4; DNa 8, 17, 34, 37, 531; DSa 1, 4; DSb 1; DSe; DSd 1°; DSe 7f, 16°, 34, 44°; DSf 5, 18°, 21°; D8g 1, 3°; DSi 1; DSj 1°, 2°. DSk 1, 4; DSm 1°, 6°; DSy 1; DZe 4, 7, 8, 11;
LEXICON
DE 11; DH 3f; XPa 6, 13, 14; XPb 11; XPe 6; XPd 8, 17; XP£ 8, 34f, 36, 39, 41; XPg 9; XPh 6f, 15, 29, 34, 37, 40, 421, 43, 50; ХР] bis; XSe 1°, 3°, 4°, XE 12; XV 9, 23; A!Pa 9°, 21°; D'8b 1°, 4°;
```


## [2026-09-04T19:55:47.075Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor n in range(183,193):\n    L=leaves[n]\n    if 'anuv' in L or 'ana ' in L:\n        for m in re.finditer(r'anuv', L):\n            print('leaf',n, L[max(0,m.start()-300):m.start()+300].replace('\\n',' '))\n            print('...')\nEOF"
}
```


### [2026-09-04T19:55:48.777Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:55:51.959Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor n in range(183,200):\n    L=leaves[n]\n    for m in re.finditer(r'anuv|anu-|\\bana\\b', L):\n        print('leaf',n,'|', L[max(0,m.start()-250):m.start()+350].replace('\\n',' '))\n        print('---')\nEOF"
}
```


### [2026-09-04T19:55:53.674Z] TOOL RESULT

```
leaf 185 | n-. See akarta-, ax áaina-, axsata-, Anümaka-, ayaumani-. * a- demonst. ‘this’: Av. a- as in GAv. gsm. ahé, Skt. a- as in gsm. asyd, Gk. lsn. є 40, Lt. nsn. tod in ecce ‘lo’; pIE *e-. See also aciy, ada-. Decl., $199. anã ism. DPe 8 (not to Av. Skt. ana-, cf. Mt. MSLP 19.49-52); XPa 14 (with Wb. KIA 109, Mt. Gr. $326; translated by АКК. a-ga-’, Elam. hi ‘this’, which refutes interpretation of Bv. Gr. $368, $388, as prep. w. inst. ‘throughout’, Av. ana with ace. ‘along, on’, Gk. дра 'along. ahyāyā lsf, DB 447; DNa 11; DSd 2°; DSe 10; DSf 7, 15; DSg lf; DSi lf, 4; DS} 1°; D8m 5°; D8s If, 3°; DSy
---
leaf 185 | -. Decl., $199. anã ism. DPe 8 (not to Av. Skt. ana-, cf. Mt. MSLP 19.49-52); XPa 14 (with Wb. KIA 109, Mt. Gr. $326; translated by АКК. a-ga-’, Elam. hi ‘this’, which refutes interpretation of Bv. Gr. $368, $388, as prep. w. inst. ‘throughout’, Av. ana with ace. ‘along, on’, Gk. дра 'along. ahyāyā lsf, DB 447; DNa 11; DSd 2°; DSe 10; DSf 7, 15; DSg lf; DSi lf, 4; DS} 1°; D8m 5°; D8s If, 3°; DSy 2; DZb 3; DZc 5f; DE 17; XPa 8f; XPc 7; ХВ 12, 24; XPh 9f; XPj; XV 13; A!Pa 13; РЬ if; Аа 1; Ае 4; A’Sdb 1 (ahyd de, $52.VI) ; A?Ha If; А°Не 9, 16f; А#Ра 11; Wb 6; We 7f; Wd 7. ahiydyd ($27) XPb 17; XP
---
leaf 189 | arly done in the spring (cf. РЕШ. AiW 61). Adukalnaz]Sahya gsm. DB 2.69. an- neg. prefix before vowels, ef. !a- before consonants: Ау. Skt. an-, Gk. &»-, Lt. in-, Gt. un-, pIE *on- (867.1); in Anáhatà-. and ism. to ?a- (q.v.); DPe 8 (not to Av. Skt. ana-); XPa 14 (not prep.). Anàümaka- adj. ‘Anamaka’, tenth month, Dec.-Jan.: Elam. handémakas, АКК. febétu. Cpd. of neg. a- + ndma- ‘name’ (see ndman-) + adj. suffix -ka- ($146.11), possibly with vriddhi (8126; Anámaka- ?): ‘Month of the Nameless (= High- est) God’. Anàmakahya gsm. DB 1.96; 2.26, 56; 3.63. Andhita- sb. ‘Anahita, Anaitis’, a goddess
---
leaf 189 | ++ wms, DB 4.89. атш) (ie. anu) prep. ‘along, according to’: Av. anu with acc., loc., ‘toward, along’, Skt. ánu with acc. ‘after, along’; see also anuSiya-. (1) With inst., DB 1.92; DNb 25 (ef. Lg. 15.176). (2) With gen., DNb 16, 18 ($137, $267.IV ; anu-dim + gen.). anuxiya- adj. as sb. ‘follower, ally’: from anu- (see anw) + adj. suffix -ja- (S80, §144.VI). anusiya nsm. DB 2.95. anusiya npm. DB 1.58; 2.77; 3.49, 51, 74, 90, 91f; 4.82. apa- prefix (§206b) ‘away’: Av
---
leaf 189 | Av. anu with acc., loc., ‘toward, along’, Skt. ánu with acc. ‘after, along’; see also anuSiya-. (1) With inst., DB 1.92; DNb 25 (ef. Lg. 15.176). (2) With gen., DNb 16, 18 ($137, $267.IV ; anu-dim + gen.). anuxiya- adj. as sb. ‘follower, ally’: from anu- (see anw) + adj. suffix -ja- (S80, §144.VI). anusiya nsm. DB 2.95. anusiya npm. DB 1.58; 2.77; 3.49, 51, 74, 90, 91f; 4.82. apa- prefix (§206b) ‘away’: Av
---
leaf 198 | av- ing good posterity’. [апа] nsm. DB 4.83. utava- adj. ‘strong, in health’: u- ‘good’ + deriv. of tav- ‘be strong’ (§122). utava nsm. DB 4.71f (emendation of HK, ApKT 1.63, 2.29, for KT’s detse, with first and third characters very faint; $541). ubanuvaniya- sb. ‘good bowman’: u- ‘good’ + Sanwaniya- ‘bowman’. wudanwaniya nsm. DNb 42. ud prep. and prefix ‘up’, becoming Iran. us- uz- before dentals ($85): Av. us- uz-, Skt. ud, pIE *ud (and *üd in NEng. out, NHG aus): ud with verbal root раф, us- in ustaxand-, u(z)- in uzma- (S84). ира (i.e. upd, cf. 5140.1) prep. and prefix ‘to- ward’: Av. ира
---
```


## [2026-09-04T19:56:09.756Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor n in (188,189,190):\n    print(n, re.findall(r'\\b(1[5-9]\\d)\\b', leaves[n])[:10])\nEOF\necho \"=== BRT anu ===\"; grep -n \"•  j.  anu\\|ap,  anu\\|p,  anuv\\|anu\\.i\\|anv\\.i\" BRT.txt | head -20"
}
```


### [2026-09-04T19:56:11.374Z] TOOL RESULT

```
188 ['191', '152', '152', '191', '193']
189 ['191', '167', '198', '193', '193', '193', '168', '172', '191', '176']
190 ['188', '191', '155', '191']
=== BRT anu ===
4484:•  j.  anu,  p.  anuv,  g.  33änü ''  i)  Praen, a)  mitAkk.,  a)  'nach,  gemäss':  hvam  'u uStim  zaoämca  V.2. 11; —  °«  a^qmi^A.) N.Äjj/Oj;  —  ftspünam  "u  mainm"n3Lch aller  Urteil"  Yt.5.93.  ß)  'in  der  Rich- tung auf— hin,  an':  Ayaj  *aenatiAe  dr}g- vatö  Ä»J»fl"  isySng  *ankayä  (sd.)  Y.  J2. 16.  b)  mit  Lok.  'längs,  entlang  an— ': !!  zäzänJ'  niima"  vardanam  °uv  ^u/ratauvä (sd.)  Bh.j.19.  2)  Praev.  (mit  '«««-, var>z-,  slü'  u.a.).  [Yt. /o.  137:  lies anu-sasträi,  anu.maiityji.]
4486:•  j.  anuxtayae-ira,  -tSe  Inf.  '(und)  im Reden  zu  folgen,  zu  reden  gemäss  — ' (Dat,'>,  Gen.):  ya\a  az3m  Aälayme{sä.) .. zara^usir^m  anumatSe  .  .  "tSe  dalnayai anu.varstSe  .  .  Ytf.  18;  —  haxhya  (sd.)
4499:•  j.  anupöiö'want-  Adj.  (fem.  'waiii-) 'mit  einem  hervortretenden  Reif,  Kranz versehen';  pusain  ('Diadem')  .  .  'waüTm Yt.  5.128.
4504:•  j.  anu-matayae-:vr,  "t^e  Inf,  '(und)  im Denken  zu  folgen,  zu  denken  gemäss  -' (Dat",  Gen.):  ya^a  azsm  /nJcayeiie  {sA) .  .  zara%ustr»m  "ISe  dagnayjt  aiiuxtJe  .  . anu.varHSe  Yt.5.18;  —  haxsaya  (sd.)  .  . frat^ma  .  .  aiähl  dasnayj  'iayaeca  , .  Y.
4509:•  j.  anu-maya-  Adj.  'mäh  machend,  blö- kend', vom  Schaf;  mit  pasaf-:  bis  kapta pasvS  °ya  .  .  nisirinuyHt  V.  14~  16;  — pasius  *g3r>bul  'yiie  V.5. 38;  —  koU. 'pecus  ovillum':  pasiui  °yche  pawm  Y.  2. 24.  A)  als  Subst  'Schaf:  hazanram "yanqm  frSvinuyJl  vtspanqmca  aitaisqm pasvqm  ,.  V./Äyo;  —  saUm  aspanqm.. /lazaanm  gavqm  ba^oarj  "yanqm  Yt  5. 2i;  0.3,  V.i'2.4;  —  niiinmn  staor?m bisazy.lt  "malm  anj5  V.  7. 43;  43;  — 'yanqm  arsnqmV  .22.20.  a)  sva. 'Schaf- fleisch': hazat3nm  gSus  j^anüiiiqm  (sd.) baivan  'yanqm  H.;.s'*.
4538:•  j.  anu.zafan-  Adj.  'längs  des  Mauls, dem  Maul  entlang  gehend';  *usrB.az(t»S hisiinte  "faiiB  takahe  "(die  Rinder)  stehen da  Tränen  vergiessend,  dem  Maul  endang gehenden  Laufs"'*  Yt. /0.38.
```


## [2026-09-04T19:56:24.403Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"anv\\.i\\|anu\\.i\\|anu-i\\|anv,i\\|anu,i\" BRT.txt | head -10; echo \"=== BRT ana praep ===\"; grep -n \"j\\.  ana\\b\\|ana,  p\\.  ana\\|•  j\\.  ana\" BRT.txt | head -10"
}
```


### [2026-09-04T19:56:24.477Z] TOOL RESULT

```
=== BRT ana praep ===
4208:•  j.  ana,  p.  anä  Praen. 'über  — hin';  i)  mit Akk.,  a)  'über—  hin':  yat  vlspanqm  yuxta- nqm  az>m  fratsmsm  "^anjaymi  (sd.)  "</ *car>tqm  yqm  daryyqm  ". .  über  die  lange Rennbahn  hin"  Yt5.so'>.  b)  'entlang, längs';  "a  til  vai'Am{&i..)  ayii  °a  bititn  °a 'iritXm  V.  5.  5.         c)  'auf',  auf  die  Frage
4214:\*  j.  ana',  nur  KompA.:  negirende  Par- tikel 'un-'.
4251:•  j.  anaiKm  Adv.  'in  der  Quere':  cvat. . äps  yat  frätal,car}tayä  .  .  druxi .  .  /ras- naoilit .  .  ^rigäim  nyäpim  navagaim  pait- ySp}m  xsvas^aim  an'  ".  .  drei  Schritte stromabwärts,  neun  stromaufwärts,  sechs quer  über  den  Strom"  V.  tf.40.
4254:•  j.  anaiSyä-  f.  'Bann,  Interdikt':  cvanl>m drajS  zrviln^m  aitiha  z^mS  (%t~,  3  b)  'ya (NS.)^a/  ahmt  .  .  V.6.1;  i.
4256:•  j.  ana  parö  adv.-artigcVerb.  'vordem'(?); &!/  ana  parö  dus.hr?la  (sd.)  aat  ana par3  ma'^^rö  spmtd  S.2i.^(^).
4263:•  j.  anapiäüta-  Adj.  (fem.  'tä-)  'wobei kein  Verschieben,  Versetzen  (von  Worten) stattfindet':  gOkanqm  anapySxoanqm  (sd.)
4273:•  j.  anapyüxSa-  Adj.  (fem.  '"oä-)  'wobei kein  Hineinsprechen,  Einschieben  von Worten  stattfindet':  gil'ianqm  'oanqm anapisatanqmsrävayamnanqm"\oaGi^ils, die  ohne  Einschicbung  und  Versetzung von  Worten  hergesagt  werden"  Y.  7(j.  5; 13.3;  —  tisrB  paoiryS  .  .  'o5  anapUütS Vr.  13.  I,  3;  —  Hsra  paoirya  ,  .  'oa anapisäia  YT.13.2,  3;  3.
4332:•  j.  ana.mana-  Adj.  'der  (entlang,  d.  i.) gemäss  Jemands  Sinn,  Willen  ist,  ergeben, treu':  kahmäi  . .  upatihacaymi  (sd.)  haca.- manäica  'näica  ..  "wem  .,  der  (mir)  treu und  ergeben  ist . .?"  YLj.S,
4333:•  j.  ana-mar9zdika-'>  Adj.  'erbarmungs- los, unbarmherzig':  'in  zT  asti  Aavili mar^zdikäi  (sd.)  Aog.  Jp;  —  aus  'ks Aog.  7^;  79,  So;  —  vayuits  "inÄf  Aog.  77; —  gaoake  .  .  'kahe  Yt  jj.  136".
4354:•  j.  ana-saxta-  Adj.  (fem.  °/ii-)  'der  den Ablauf  der  (bestimmten)  Zeit  noch  nicht erreicht  hat' "' :  yö  näirikam  yqm  a/^'irqm ..'tarn para  xludrä  ai'i frau/wrjzaiti  "wer eine  Kindbetterin,  die  ihre  Zeit  noch  nicht abgewartet  hat,  vordem  beschläft"  V.  i^.  8.
```


## [2026-09-04T19:56:40.933Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON عنبر ===\"; grep -c \"عنبر\" MON_part1.txt MON_part2.txt 2>/dev/null; grep -n \"عنبر\" MON_part1.txt | head -5; echo \"=== AFM anbar latin ===\"; grep -n -i \"anbar\\|عنبر\\|العنبر\" AFM.txt | head -10; echo \"=== AFA ===\"; grep -n -i \"anbar\" AFA.txt | head -5"
}
```


### [2026-09-04T19:56:41.030Z] TOOL RESULT

```
=== MON عنبر ===
MON_part2.txt:19
MON_part1.txt:24
6637:معنبر و خوشبو. 
36396:شمع. تاج عنبر: ( کد.) زلف. تاج فلک: ( کد.) 
83368:شاهبو(ی ): (8-950 (امر.) بوی عنبر» 
83369:عنبر. بوی مشک. 
83735:عنبرین: (کد.) شب تاریکک. شب کاینات: 
=== AFM anbar latin ===
=== AFA ===
```


## [2026-09-04T19:56:42.360Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN anbar ===\"; grep -n -i \"anbar\\|ambar\" HRN.txt | head -10; echo \"=== HUB ===\"; grep -n -i \"anbar\\|ambar\" HUB.txt | head -10; echo \"=== DEV ambre ===\"; grep -n -i \"^AMBRE\\|ambre\" DEV.txt | head -6; echo \"=== PHN ambre ===\"; grep -n -i \"ambre\" PHN.txt | head -6"
}
```


### [2026-09-04T19:56:42.447Z] TOOL RESULT

```
=== HRN anbar ===
358:gegenüber hengäm ; qanbara (S. 227 Zeile 9) gegenüber
1387:anhüstan anhäufen', anhar , anbar(i)sn , anh(ä)rok\pat
1388:(Gemme), arm. LW. awbar, hamhar (davon hambarem),
1389:hambarakapet; ai. sam-r- V^par-.
2927:*) Dazu arm. amparist , ambarisf *unfpomm , gottlos* nach F r.
3303:pa/umpar, d, pexompar; hei, paiyam^ paiyambar (207).
4109:phlv. cambar head-fiUet' (Säy. näSäy. HI, 4).
22243:i hambarakapet 111.
22244:i hambarem 111.
=== HUB ===
4283:gaona- ; zanbar *Sanfte* = arm. zanuar = zd. "^jainibara- ;
6020:in paiyambar Prophet* (arm. patgamavor),
6277:sampurayati 'flillt an'; dazu anbar 'Speicher, phi. anbdr,
6278:arm. ambar\ canbar 'Kreis' (? H. 446); siinbada *Wetzstein*
6432:wara-, np. zanbar\ patvast *Einpfropfen', ap. *patiwasU',
6946:zd. hanJcarayemi; anhastan — anbardan anftillen', pr. an-
6947:baram^ ptc. anbarda repletus*, alt belegt JKAS. 1894, 443:
6948:anbarda puffed. up with pride', skr. sam/;wraya^i *anfullen*;
6993:= paz. vadardj wie audi rd in dem alt bezeugten anbarda^
7696:erhalten in hambar *Speicher nebst Ableitungen (5. Jhd.),
=== DEV ambre ===
235:Abelmosc.  Esj).  abehnosco,  laiin  des  botanistes  ahelmos- chus.  Cette  plante  (malvacëe),  appelée  aussi  ketmie  odoranle , vul^o^airement  ambrette  ou  graine  musquée,  doit  son  nom  à l'odeur  de  musc  qu'exhalent  ses  semences,  dont  la  parfu- merie tire  profit.  C'est  l'arabe  dUm  Jo^  habb  el-misk,  litté- ralement graine  de  musc.
367:de  l'arabe  aIaJ!  al-qohha,  qui,  entre  autres  sens,  a  celui de  petite  chambre,  cabinet,  ainsi  que  le  montre  M.  Lane (jTAc  thousand  and  one  Nights,  I,  281).  Voir  l'intéressant article  de  M.  Dozy,  Gloss.  p.  90,  ()i.  Le  mot  est  employé avec  son  sens  le  plus  ordinaire  dans  ce  passage  de  Niebuhr  : t^Les  derniers  seigneurs  de  Taœs.  .  .  ont  bâli  de  beaux palais  pour  eux  et  leur  postérité,  et  se  sont  contentés  d'un petit  kubhe  pour  leur  servir  d'oratoire  et  de  sépulture  -.  v
499:Ambre.  Esp.  alamhar,  port,  alambre,  ital.  ambra.  De l'arabe  ~aJ^  VmW,  ambre  gris,  nom  qui  est  passé  au  succin ou  ambre  jaune.  Les  formes  qu'on  trouve  dans  la  basse
503:latinité, ^//»/>^//'.  (imharc ,  ambra,  amher,  ambre,  ambriun ,  pa- raissent aussi  confondre  les  deux  substances.  HermoJao Barbaro,  qui  a  publié  au  xv*"  siècle  un  commentaire  sur Dioscoride,  écrit  ambra  ou  ambar  :  ^Aetius,  dit-il,  ambar, nos  succinum  orientalem primi  nominavimm  ^  w
504:Liquidambar,  nom  d'un  arbre  d'Amérique  aussi  nommé baume  d'ambre ,  est  formé  de  ambar  et  de  notre  mot  liquide.
507:'  Dioscoridœ pharmacorum  lihri  VIIl ,  1629,  fol.  h6  verso.  Marcello  Ver- jjilio  dit  aussi  :  «Succinum ,  quod  electrum  veteres,  nostri  ambram  dicunt.?i Ihid.  ïo\.  /j7  recto.  Ces  commentateurs  rangent  sous  la  même  dénomination l'ambre  jaune  et  l'ambre  gris  «quod  pisces  devoraverer».
=== PHN ambre ===
874:de musc, petite fleur qui sent l'ambre; autrement appelée am-
1235:ment réservé dans une chambre à coucher pour y placer un
1590:fém. plur. du verbe quadrilittère ^iaÂj [gonf'ar] cambrer^ donner
1641:AMBRE, s. m. (a.)
1643:dont on fait des électuaires. Il y en a de deux sortes : Yambre
1644:jaune ou succin , et Vambre gris. Ce dernier est particulièrement
```


## [2026-09-04T19:56:50.790Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1641,1665p' PHN.txt"
}
```


### [2026-09-04T19:56:50.832Z] TOOL RESULT

```
AMBRE, s. m. (a.)
jjij^ [^anbar] Substance résineuse, odorante et inflammable,
dont on fait des électuaires. Il y en a de deux sortes : Yambre
jaune ou succin , et Vambre gris. Ce dernier est particulièrement
estimé des Arabes, des Persans et des -Turcs, qui l'emploient
avec le musc et l'aloès dans leurs parfums. — En français, on
dit au figuré, en pariant d'un homme rusé, adroit : il est fin
comme Vambre. — Comparez l'espagnol et le portugais ambar et
alambar (on dit aussi alambre en portugais), l'italien ambra, et
Tançais amber.
AMBRETTE, s. f. (a.)
Mot dérivé de^^AÂ^ ['oniar] ambre, et appliqué à la ketmie,
à cause de son odeur. Celte plante sappelle aussi abebnisc et
Jleur du Grand Seigneur. Les Orientaux recherchent sa graine
et la mangent souvent en prenant leur café, pour lui donner
un goût plus exquis. — Les Portugais écrivent ambreia et am-
barilha.
AMER, ÈRE, adj. (a.)
j^ [mourr] rude, acerbe, désagréable au goût, en parlant d'un38 AMI
fruit, d'une herbe, etc. Au figuré, dmdoureux, triste, affligeant,
— Du superlatif ^1 [àmarr] vient peut-être le latin amarus,
d'où am^r'en français, puis amargo en espagnol et en portugais.
— Amertume, s. f. (en arabe, 'Bj\j^ marârat) se dit, au propre,
de Tàcreté d'un suc, d'un fruit, etc., et, au figuré, de la mau-
vaise humeur, de ^affliction de l'esprit. — C'est à la même
```


## [2026-09-04T19:56:51.394Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^عنبر\\|عنبر (\\|عنبر .\" MON_part1.txt MON_part2.txt | head -20"
}
```


### [2026-09-04T19:56:51.597Z] TOOL RESULT

```
MON_part2.txt:410:مرکب از مشک و عنبر و جز آن به رنگ 
MON_part2.txt:5162:فیل‌ای که از عنبر سازند و بوی خوش دهد. 
MON_part2.txt:29525:حال آنکه عنبر از نوعی پستاندار ماهی شکل 
MON_part2.txt:29557:جوذر (گوذر) به گاو عنبر هم اطلاق شلد ه. 
MON_part2.txt:29565:سازند. گاو عنبر (عنبری): (جان.) عنبرماهی؛ 
MON_part2.txt:43975:بنام عنبر بدست می آورند. . ماهی فاطو س: 
MON_part2.txt:61252:امف.) آنسچه که به عنبر آغشته شده؛ 
MON_part2.txt:72711:عنبر مغشوش (خصوصا). 
MON_part2.txt:81556:از قبیل انواع بالن و عنبر ماهی [کاشالو) و 
MON_part2.txt:90372:اوجی» سوس‌عنبر (فرعا.جما.) نوعی نرشی 
MON_part1.txt:6637:معنبر و خوشبو. 
MON_part1.txt:83369:عنبر. بوی مشک. 
MON_part1.txt:83735:عنبرین: (کد.) شب تاریکک. شب کاینات: 
MON_part1.txt:98670:عنبر: ۲ (.) (جان.) ماده‌ای چرب و 
MON_part1.txt:98672:که از روده با معدة ماهی عنبر گر فته می‌شود. 
MON_part1.txt:98674:قطعات عنبر مستخرج از داخل روده و معدة 
MON_part1.txt:98676:بیشتر (تا ۲۰ کیلوگرم) است. تولید عنبر در 
MON_part1.txt:98677:داخل دستگاه گوارش ماهی عنبر بواسطه 
MON_part1.txt:98681:دستگاه گوارش ماهی عنبر حفظ می‌شود و 
MON_part1.txt:98682:حتی پس از مرگ ماهی عنبر بوی مطبوع
```


## [2026-09-04T19:56:56.026Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '98660,98700p' MON_part1.txt"
}
```


### [2026-09-04T19:56:56.088Z] TOOL RESULT

```
حق تعالی به مصالح امور بندگان» علم محیط 
الهی» علم خدا به نظام وجودی جهان (فرع. 
سج.) عنابت الهی: بخشایش الهی. 
عنایت کردد: 6-7 [ع. ف.] 
(مسص م.) توجه کردن. بخشیدن اهداء 
کردن. 
عنایت‌نامه: (م)دستد» (ع. ف.] (امر.) 
تقد بر نامه. سفارشنامه. 
عنب!: همم (ع.] (() (گی.) انگوره مبوة 
درخت مو. . (گیا.) درخت انگور. 
عنبر: ۲ (.) (جان.) ماده‌ای چرب و 
خوشبو و کدر و خاکستری رنگ و رگه‌دار 
که از روده با معدة ماهی عنبر گر فته می‌شود. 
این ماده در عطرسازی بکار می‌رود. وزن 
قطعات عنبر مستخرج از داخل روده و معدة 
ماهی عنیربين ۵/ ۰ تا ۱۰ کیل و گرم و گاهی 
بیشتر (تا ۲۰ کیلوگرم) است. تولید عنبر در 
داخل دستگاه گوارش ماهی عنبر بواسطه 
ترشحات سیاه رنگ جانور نرم‌تنی بنام ماهی 
مرکب است که مورد تغذیهٌ این حیوان است. 
بوی مطبوع این مادةٌ ساه رنگ در داخل 
دستگاه گوارش ماهی عنبر حفظ می‌شود و 
حتی پس از مرگ ماهی عنبر بوی مطبوع 
عنبر در داخل دستگاه گوارشیش محفوظ 
می‌ماند. تا ماهی عنبر را در دریاهای 
شمال و اطراف ژاپن و گاهی در دریاهای 
مجاور جاوه و سوماترا شکار می‌کنند و پس 
از شکافتن شکمش از داخل معده و روده‌اش 
عنبر را استخراج می‌نمایند و هر قدر ماهی 
مرکب بیشتری مورد تغذيه اين حیوان وافع 
شده باشد مقدار و م9 در داخل 
دستگاه گوارش ماهی عنبر مشتر است» عنبر 


خاکستری» شاه بویی. ضح. - در عضی کتب 
عنبر و مشک را مرادف دانسته‌اند و آن 
اشتاه است زیرا عنبر از داخل دستگاه 
گوارشی ماهی عنبر حاصل می‌شود ولی 
مشک از کيسةٌ مشک آهوی ختن نر [کيسة 
مشک این حیوان را نافه گویند] حاصل 
می‌شود و نیز از غده مشک زای زباد نیز
```


## [2026-09-04T19:57:07.843Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"^Amber\\|Amber, \" SKT.txt | head -5; echo ---; grep -n -i \"^Umbrella\\|Umbrella,\" SKT.txt | head -5; echo ---; grep -n -i \"^On, prep\\|^Unless\\|^Analysis\" SKT.txt | head -5; echo \"=== sample lines ===\"; sed -n '400,410p' SKT.txt"
}
```


### [2026-09-04T19:57:07.942Z] TOOL RESULT

```
613:Amber.   (F.  -  Span.  —  Arab (iw/«^nr.  — F.flwi5«f.— Span.  dmAar.  —  Anfc. 'as^bar  (prcMiounced  'aminxr'],  om!tr';;n*.  a rich  pcrlume.    ^Thc  resinous  .ti so  called  from  a  resemblance  to  .-^^ which  is  really  quite  a  cUffercnt  suM-...in.r. ambergris,  i.e.  gray  amber.    CalM gris  amber  in  Milton,  P.  K.  ii.  344.     ^ F.  gris,  gray,  is  from  O-  H.  G,  /rtx,  ptjf cf.  G.  grtis,  hoary.
2692:camlet,    a    «tuft.     ^Arah )      Formerly fdm^^/.supposedto  be  named  from  coittAin- iiiK  iitmel's  nair.    Really  iVoro  Arab,  kham^ /at,  khamalat,  camlet;  Kicb-  Diet  p.  c'ljs. Camellia.    (Personal   name.)     A   plant named  after  Geo.  Jos.  Kamcl,  a  Moravian Jesuit,   who    dt'&cjibed   the    plants    Ui   the ishuid  of  Liuon. Camelopard :  see  CameL Cameo.  (Ital.)     Ital.  cammeo,  a  cameo, piecious  stune  carved  ic  relief.     Origin  tin* known. Camera.  (L.)     L.  camera,,  a  chamber; hence  camera  odsatra.  a  dork  chamber,  box for  photography  ;  see  Chamber. Camlet ;  see  CameL Camomile ;  .%ec  Chamomile. Camp.  (L.)     We  find  F.  camp  (Cot.)  ; bnt  the  E.  word   was  prob.  taken  directly from  L.  eamfus.  a  field,  ground  held  by  an army.  +  Gk.  w^»o»,  a  garden.
3634:chamber,  room  up  in  the  raficw.
5221:Divan,  a  council-chamber,  sofis.  (Pen.) Pcrs.  diviin,  a  tribunal;  Arab.  dit^'Uiin,% royal  court,  tribunal,  cconcil  of  slate.
5740:Electric.  (L.  -  Gk.l  Coined  from  L. eUetrum,  smber.  which  has  electric  pro- perties.—Gk.  ^Afwrpoi',  amber,  also  shining metal  ;  ullieil  to  i^kittriup^  gleaming,  Skt. arM.  to  shine,     (y  ARX.)
---
20415:umbrella.  (Ital.  — L.)  Ital.  umbrella, 9mbr(t!a,  a  parasol;  riimin.  of  Ital.  ombra, B  sha<]e.  — L.  umbra,  a  shade. Umpire.  (F.  —  L.)  Put  for  numpire^ the  old  form  of  the  word  ;  M.  E.  nompere^ ttotimpert^  also  nouuNrt,  nounfter,  V. Plowman,  B.  v.  ^^l.^O.F.ncmfer*',  later nomf^ir,  peerless,  odd  (Col.)  ;  earliest form  nonper  (Roquefort).  Used,  like  L. impar,  in  the  sense  of  arbitrator  ;  the lit.  sense  is  uncqufil,  odd,  hence  a  third man  called  in  to  arbitrate,  a  'non  peer,'* O.  F,  non,  not ;  O.  F.  per,  pair,  a  peer. See  Won- ;  also  paer-,  under  Par,  %  Tlicrc b  no  doubt  as  to  this  result Un-  (0*  ncg.  prefix.  (E.)  Prefixed  to sbs.,  adjs.,  ana  aovs.  (Distinct  from  im- (a)  below.)  A.S.  ««•,  ncg.  prctix.+  Du. ON',  Icel.  i-,  ii-,  Daii.  u-,  bwcd.  tf-,  Guth. un-,  G.  ttif-,  W.  an-,  L.  im-,  Gk.  iof',  d-, orig.  <tra-.  Zend,  ana-,  Pera.  nd-,  Skt.  an-, p.  The  Aryan  form  seems  lo  have  been ANA;  whence  also  L.  ne^  and  Gk.  in;-, Goth,  ni-,  Ru^.  ne-,  Gael,  neo-,  negative prefixes,  y.  Readily  pfclixed  to  a  large number  of  woniU  ;  a  few  of  these,  such  as uH-couth,  of  which  the  simple  form  it  not Qscdp  will  be  found  below. Un*  (2),  verbal  jirefix,  expressing  the reversal  of  on  action.  (£.)  (3uitc  distinct from  un-  (1)  above ;  only  used  with  verbs Thus  to  UM'lock  -  to  reverse  locking,  lo n   that   which   wns  cl(i:>e«l   by  locking.
---
=== sample lines ===
It  ^ry,  by  coofusion
(Gk.)    Gk.  dffPTfi- ,«-Gk.  oitrtfo^,  I  perceive.
t'  ■  (ig     pain,    dulling
^'  .  and  oiffC^ijrtjrtit.
L    ¥uT  ^'N  far, keTsto. pMt:  ucPaot. reaeftm.     (F.  -  L.)  O.  F. ■  iht  Dtioc  of  A  thing  (oflici- ^  .  to  fix  a  I'rioe.  1*
)i  -jm^^  market,
.lidnvit;  Kc  Faith. we  FUlal Fln&t Plna.
<U)    XVI  eeot-L.
affi'^ert.   to  strike  to  the
^  ;T/r,  to  tlojh.
w  Flnont.
```


## [2026-09-04T19:57:18.534Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/on",
 "prompt": "Quote the etymology of the preposition 'on': Old English on/an, Proto-Germanic *ana, PIE root, and cognates (Dutch aan, German an, Gothic ana, Avestan ana, Greek ana, Latin an-, Old Church Slavonic na, Lithuanian nuo)."
}
```


## [2026-09-04T19:57:21.037Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://www.etymonline.com/word/amber\" \"https://en.wiktionary.org/wiki/%E1%BC%80%CE%BD%CE%AC\" \"https://en.wiktionary.org/wiki/%D8%B9%D9%86%D8%A8%D8%B1\" \"https://en.wiktionary.org/wiki/umbra\" \"https://www.etymonline.com/word/umbrella\" \"https://www.etymonline.com/word/analysis\"; do python3 tools/fetch_source.py \"$u\" --note \"page 55 verification (roots An 3 / A.n.b anbar / Andho)\" 2>&1 | tail -2; done"
}
```


### [2026-09-04T19:57:23.411Z] TOOL RESULT

```
# Etymology of "On"

The preposition "on" traces back through multiple language layers. According to the Online Etymology Dictionary, it derives from "Old English _on_, unstressed variant of _an_ 'in, on, into,' from Proto-Germanic _\*ana_ 'on.'"

The entry identifies the ultimate source as the "PIE root _\*an-_ (1) 'on,'" with cognates appearing across Indo-European languages including Dutch _aan_, German _an_, Gothic _ana_, Avestan _ana_, Greek _ana_, Latin _an-_, Old Church Slavonic _na_, and Lithuanian _nuo_ (meaning "down from").

This widespread presence across ancient language families demonstrates how this fundamental spatial preposition became embedded in European linguistic systems, maintaining relatively consistent form and meaning across millennia.
```


### [2026-09-04T19:57:26.926Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/eadc1673c09dba04.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e5ffd1b21b874c9a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7ed70422760d0caa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a1bd172abbed790c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6ee834d74a0afbaf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/392b86ae0274ba9b.txt
```


## [2026-09-04T19:57:30.060Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://www.etymonline.com/word/on\" --note \"page 55, root An 3: Germanic->English on/upon\" 2>&1 | tail -2"
}
```


## [2026-09-04T19:57:30.910Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/anatomy",
 "prompt": "Quote the etymology of anatomy: Greek anatomia/anatome, anatemnein, ana- 'up' + temnein 'to cut'."
}
```


### [2026-09-04T19:57:31.946Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/89d35cba35ecbde1.txt
```


### [2026-09-04T19:57:37.197Z] TOOL RESULT

```
# Etymology of Anatomy

The word "anatomy" originates from Greek roots meaning "to cut up." Specifically, it derives from late Greek *anatomia*, combining *ana* ("up") and *temnein* ("to cut").

**Key Etymology:**
- **Greek origin:** "dissection," literally "a cutting up"
- **Latin path:** Late Latin *anatomia* 
- **Old French:** *anatomie*

The term entered English in the late 14th century as "study or knowledge of the structure and function of the human body" through dissection. Early related senses included dissection (1540s), mummy (1580s), and skeleton (1590s), before the modern scientific meaning of "the science of the structure of organized bodies" predominated from the 17th century onward.

The word was sometimes misdivided in Middle English as "an atomy" or "a natomy," a common occurrence with words beginning with vowels when preceded by the article "an."
```


## [2026-09-04T19:57:40.262Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://www.etymonline.com/word/anatomy\" --note \"page 55, root An 3: Greek->English anatomy\" 2>&1 | tail -2"
}
```


## [2026-09-04T19:57:42.461Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LKT leaf for entry 78 ===\"; python3 - <<'EOF'\nt=open('LKT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ni=395\nprint('leaf',('\\n'.join(lines[:i])).count('\\f'), '-> printed', ('\\n'.join(lines[:i])).count('\\f')-26)\nEOF\necho \"=== DEV leaf ===\"; python3 - <<'EOF'\nt=open('DEV.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ni=498\nlf=('\\n'.join(lines[:i])).count('\\f')\nprint('leaf',lf)\nEOF"
}
```


### [2026-09-04T19:57:43.177Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9bf62ed775ac53b4.txt
```


### [2026-09-04T19:57:45.757Z] TOOL RESULT

```
=== LKT leaf for entry 78 ===
leaf 33 -> printed 7
=== DEV leaf ===
leaf 57
```


## [2026-09-04T19:58:25.577Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"hana-\\|hana \\+'blind'\\|blind\" ISS_alt_DKS.txt | grep -i \"blind\" | head -10"
}
```


### [2026-09-04T19:58:25.627Z] TOOL RESULT

```
338:аса ‘she sewed’, K 4649 ba khauysa Буйтай и аса u ttu vajsya avijsyadai puraká ñüistya ' she found a small piece of clothandshesewedand wrapped it round her afflicted blind son’. To acana ' thread, BS sitra-'. Base čai-: &i-, with acá from *acitatd and ācana from *ā-čyana-. With č-  z-, M.Pers. T. 'bsyngr, M.Parth. T., "упт ‘tailor’, N.Pers. üdidan, üXadan, asandan 'to sew��; with kai-:ki- in Sogd. Ryn'h ‘sword’, O.Pers. cavérmgs, O.Ind. kinása- 'plough- man’ (TPS 1955, 67-69), adding BS cimara- ‘metal, iron or copper’, to IE Pok. оту (s)&(/t)ai- ‘to cut, pierce’. For ‘thread’ derived from ‘to sew’, note O.Ind. siuyati, syfita, sitira-. For acá, see also paca 'she covered! from *pa(ti)- Catüld, pres. pacan-. See also mejanya- ‘embroidery (CY. N.Pers. Занаћ ' sting (of insect), point (of needle)'.
541:arrá ' bear (animal)', JS 26v4 tlvai arrá slana ‘you being a bear (cared) for him’, BS rksa-. From *riia-, Av. ario (Aog. 79), Zor.P. 'rs or hrs *ars, or hirs, N.Pers. xirs, Oss. DL ars, plur. ärsitä, I. ärsytä, 2nd component hurm-asitd ‘blind bears (a game)’, Wanetsi yiri, Pašto yas, Orm. yirs, уі, Yidya, yarš, Suyni yürf, Sarikolt yur£, yiri, Sangl&éi xars, Parāčī uf, uč; ТЕ Рок. 875, O.Ind. /Rsa-, Greek ёрктоѕ, &pkos.
596:avijsyaca 'not seeing, blind', fem., v 38748 auijsyaca strrīya ‘blind woman’; K 46:37 ttye avijsyace sirriyi jsahera ‘in the womb of that blind woman’.
597:avijsyadai 'blind', masc., JS 31v3-4 avijsyamdü ysadaka dva mürd-pyara 'blind two old parents'; K 4647 püra avijsyadai уй 'the son was born blind’; K 4754 s avijsyade sirka ' the blind child’; Manj. 9 hana avijsyadai satva ' blind, not seeing, being' (dyadic). See vijsds-.
934:Hska-— ásalà 27 ti ‘һе was then about to explain’; п rco-219 и japhaí agfamda hamau ' he was about to confer with him’ (hamau infinitive —Ahamaánd); K 32:38 samai astamdi brraima laidrrai pana ' she was about to weep before the hunter’; =E 2485-6 ttanai astada brraima lümdrrai pana, = K 16:141 tanai üstana (-n-, not -d-) brraima lamdrrai pana; X. 46:39-40 khu si avijsyaca strriva dasamye тайа ааай ysaná ' when the blind woman was about to bear a child in the tenth month’; т plural, rt 46:84-5 mista hve ni jsave u ganamai üstamdamdüm haysá ‘the great man does not come and we were about to despatch his wheat’; 11 112-45 u üglamdamdüai mi hajsimá 'and we began to gather here’, translation AM, n.s., 11, 1964, 3; I 75:234 varat astamdamdá jsaná ' there they were about to strike him’. See noun Zsiana- 'beginning'. Base à with sjan- from histan-, to Av. папи-, frastanvanti, IE Pok. 1004-8 stā-:sta-, with -nu-, See also Zor.P. stan-, statan ' to take’, N.Pers. sitanad, sitadan.
1398:kašš-, has-, kas-, karš- ' fall, come into, fail’, Z 23:99 tra ttádeta kaśśīru ' may you fall into this darkness’; Z 10:11 varata kasfüre bodhi-sambüra hamalà ‘there the bodhi- sambhàra- ' means for bodhi-knowledge' come together"; Sid. r21v3 dyamkyai kasüre 'his sight fails', Tib. mig ldons-śin ' eye becomes blind’; 3 sing. Sid. 14r5 nastá ga kaste "faces go downwards’, Tib. lto sbo-bo dan; K 65, 82ут akşanvā hagtyà па kasaune ' may I not come into the eight calamities (BS айапа-)'; noun Sid. 2r2 biysma Rasane hivi pishalà ' chapter of the failing of urine’, Tib. géin sri-bahi lehu; Sid. 8v3 Бухта katama, Tib. дёп hgag-pa (hgag-ba 'stop") With intrusive -r- only JS 38v3-4 karse bhadrre-kalpya ' migrates into the bhadra- kalpika- world’, parallel BS cyavate. Participle kasfa-, K 64, 81v3 küladva hasta ' fallen into the kilada- ( ?)'; JS asvi ttädeta kastye ysama-famdat vaska “ог the world (= BS loka-) fallen into darkness’; 1 sing. ш 2, 7r4 taña bärmaña kaşfūm ' I have come into this prison’; Ш 5, 11v5 hamtharkaña hasta ‘соте into distress’; Y 32, gas kastin; K 46:47 та tcaimefia kasfe 'I failed in my eye’. From base kas- with -ya-. Elsewhere Iranian kap- “to fall’, Zor.P. kaf-, M.Parth. T. kf-, gf-:hft, gft 'to fall, Аит, М.Регѕ.Т. ghwn *kafvan, *hahuan, N.Pers. kuhan, kuhnah 'old'; Zor.P. Арі, kptn 'to fall’, Balo&t kapag, k'afay, kapta 'fall, happen, bring forth’. Possibly kass-, from kas-y- with =s= < -tr- (as basaka- ' calf") to base kas-, kah- (sce khah-), if *Ras-s- gave kats- > kas- (as O.Ind. vivatsati 'wishes to dwell’, fut. vatsyati to base was- ' dwell").
1444:kärra- ' deaf', Z 5:101 kärra pyyäre ' the deaf hear', = Manj. 415 Айта (lacuna); № 169-1 hand karrá mutd "blind, dumb, deaf’, parallel Pali andAa-, müga-, badhira-; v 146, 71v4 abisüta и kārrä 'tongueless and deaf’; SuvP. 71v3 kāra ройтае ' the deaf may hear’, BS badhiras ca srivanti ; abstract Sid. 126v3 kāraustä, Tib. hon-pa ' deafness’; and 1 143, s2v2 Raraümüa ‘deafness’, BS bādhirya-. From *harna- (adjective of deficiency to *karna- 'ear', as Greek laxlov ‘hip’, laxi&s 'pain in hip’), Av. karana; ‘deaf’, karana- ‘ear’, O.Ind. Rdrna- 'ear', but badhira- ‘deaf’. Sogd. krn, Yayn. kan, Zor.P. kl *karr, N.Pers. karr, kar, M.Pers.T. qr *karr, Pašto Коп, Orm. Абл, Buyni па, Yidya kun-, kun-, Мип]йпї kün'gy.
1508:ceremonial jar; from the talkers( ?) I entered, dying with hunger’ (uncertain). From Айса-, N.Pers. Айс, Айгай, Arab.-Pers. kär, plur. kiwasah, Syriac kws-', Armen. lw kous (secondary, Parthian( ?), -2-), Uigur lw Rüzác, Orm. kuzsli, Para&i kīsarē '"water-jar' IE Pok. 588-92 Reu-, keub-, Greek küfos 'cup', with Айта- from base keu-£-. kuysva 'thrown down’, v 66-8a püraka-m haya suhá bedau, khu тат ni himari pajsa kuysva niysiya, muttà paribhüta и рајха faxdya hvasta. iámysirá-vada pūra du(ra) ‘І am protective of my sons in time of happiness so that they do not become cast down greatly, depressed, beaten, defeated, violently beaten to the ground, lovingly nourished sons, daughters’. From kaus-: kuz- tto throw down, lower’, dyadic with niysiya-, to Orm. nikizyek ‘to throw down, sow, propel’, Pašto kās 'low', küzawul' make to descend’, küzédal ‘то descend', Waxi ki. Hence IE heu-f-. The form kuysvana- is like M.Parth.T. kfwn *kafoan, М.Регь.Т. Алип *kahvan, Zor.P. kahvan, N.Pers. kuhan, huhnah 'old' from kaf- ‘to fall down’. бга 'grapes(?)', п 719-10 drai simga huska kūra 'three imga-measures of küra (grapes ?)'; SDTV 78 kāra äjemüm ‘I bring Айла’ (MT c iii o081,2, omitted from KT v). With Pašto kwar ' wild grapes, Vedic kuvala-, hvdla-, kola- ' ju- jube’. The two occurrences will exclude kāra- as a form of güra- ‘grapes’. The jujube is the ‘thorny’ plant, see s.v. simje, BS badara-, Hence IE Pok. 958 s&heu-:skhu- for needles and thorns of plants and Aüra- from (s)&uvara-, IE shhuuelo-, beside Lit. sRujd ‘бг needles’, Russ. xvojd. kūra ‘crooked, non-existent, false', Sid. 2ovs cvai kurä gesürd hame ' whose neck is crooked’, Tib. mjin-pa yo- bahi nad, SuvO. 24r4 küro, BS abhüta-, K 18:218 küra, BS Divyavadana 448-8 vitatha-, v 117, ббгу Айга hära, BS füphya- "trickery', v 117, 66v1 sfathanu hüragu uysnauranu, BS fathyakara-; Z 574 kuire kümate 'false thoughts', = Мапј. 231 hüra kāme; 1137, 45 v4 vittüla, büvau küra hira "vaitüla-demon, bhüta-ghost and evil things’, BS vittánda, pürtanà Атаа vidhaka (=vetāda-, puttana-, krta, -i-. Compound, Manj. 160 &Aüra-vadáya ‘оп the false раф’. From kau- ‘ќо bend’, kāra- from *&aura- ‘bent’, specialized of blindness in Zor.P. Айг ‘blind’, N.Pres. Айг, Oss. D. kurmä, kurm, I. Rürm, kürmytä. For *blind' Khotan Saka has Лапа-, Av. anda-. O.Ind. kora- 'jeint' is direct from IE Pok. 588-592 keu- 'to bend’. küra- 'membrum virile’, Sid. 19r3 cu mirimjsya se kūri vanvüie, Tib. na-le-éam ni ro-éa-bar mi byed-do “ће marica-pepper does not cause lust’; IV 17: 12-3 ttrauvafá hadà kuri vi u hagidiru hurdm jtye ‘the thirteenth day he fails in the küra- and the inner thigh’; K 34:67 tta ttai kaurka spaliyi = K 25:116 tta tte aga spalira, =K. 17:180 Шова spaltra ' the membrum trembled’ and variant ће limbs trembled’, with &aurka from Ёйта-. From Rüra-, kura-, Nüini kur, Biyabiünaki kür, Zor.P. kyl *ker, N.Pers. kér, kir from *kurya- (as Zor.P. tyl *tër 'butter', Av. tüirya-). IE Pok. 954 (s)eu- ‘to thrust". kürada- ' falsity', v 149, 223 vátco kyi uysanye kürüda vajisdi Ш 'then he who sees the falsity of the self (= BS átman-)'. From küra- with *hada- < *harta- 'effecting'. kurkuma- ‘saffron, crocus’, Sid. 1ov2 kurkum, Tib. gur- kum; Y 185, тобу: kūrkūm, BS kunkuma- (written küküma-), later with -йтп, 1 179, 97v3 kurküm, 1 187,
1928:gurmä ‘a kind of pea’, Sid. r6vr, BS kalaya-, Tib. ce sran (ed. Pekin). From base gau-:gu-, gur- 'round', IE Pok. 393-8 Greek yüpós ‘round’ of a round ‘pea’, form like Oss. D. kurmä, kurm, I. kürm 'blind' beside Zor.P. Абг.
2592:ttára- ‘dark’, ш 25,27b2-3 khu hve ttürd vi гатай hama ni tamu ja пата vajisdi ‘when а man has entered darkness, he sees no thing at all’, BS tad-yathapi пата subhüte puruso ^ndhakara-pravisto na kim cid api patyet, Manj. 76 hana ca rrudà tara na butte 'the blind man who does not understand light (and) darkness; Manj. 59 ttära tta khu siya 'dark as at night’, Z 410 рӣѓси ssavo nármáte ttüru juvg hada 'then he created night, dark, at mid-day’; 7,247193 {аги haryāsu jadt harbistu jándá ' it dispels black darkness, all the ignorance’; Z 2:122 tterd sstue біп dark night’; v 154, 184b2 ttürána ssava-mürd ‘night-time with the dark’; ibid. 18422 Aastamo daju ttüro е best flame, darkness’, From base tam- ‘Бе dark', see ttama-, pátam-, bátam-; *tanÜra-- *türa-; Av. tamah-, tafra-; Zor.P. tar, tarik, tártom; N.Pers. tür, tárih; M.Parth. T. tr, tryg, M. Pers. T. t'r, t'ryg, adjective t'ryu, Sogd. Bud. tr'k, Man. g'ryy, 1'тё, Yayn. tóra; Oss. DI. tar ‘dark, darkness’, D. talingd, І. talyng; Pašto tür, tyára ' darkness’ (from *tan6rya-), Yidya tiro, (пто; Sarikoli turik. Possibly Zor.P. t&rak, N.Pers. tërah, Baloci t£ray may come from *tanÜrya-, but sce also s.v. ttarüna- ' reddish’, with tara-. IE Рок. ro63-4 tem-, O.Ind. tdmas-, támisra-, timird-, Lat. tenebrae.
```


## [2026-09-04T19:58:31.923Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['DEV','LKT','SKT','PHN']: print(k, d[k].get('page_offset'))\n\""
}
```


### [2026-09-04T19:58:33.654Z] TOOL RESULT

```
DEV leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
LKT leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
SKT leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
PHN leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


## [2026-09-04T20:02:16.032Z] TOOL CALL #73: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-55.json",
 "content": "{\n  \"pdf_page\": 55,\n  \"book_page\": 25,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"An 3, Anô\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂en- / *h₂ana (older notation *ano-, *anē) 'on, upon, up along'\",\n      \"note\": \"Pokorny's headword is '4. an, anu, and, no — Bedeutung: eine Präposition (\\\"an einer schrägen Fläche entlang o. dgl.\\\")', pp. 39-40; Watkins/AHD numbers exactly the same root 'an³. On. Extended form *ana … [Pok. 4. an 39.]', which is where Nourai's '3' and the second citation form 'Anô' (= Watkins's *anē) come from. Klein s.v. ana- posits 'I.-E. base *ano-, \\\"on, upon, above\\\"'. So the root, the language label (Indo-European) and the gloss are all correct; the only reservation on the whole entry concerns Old Persian anā (node 1), which Kent rejects as a preposition.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%E1%BC%80%CE%BD%CE%AC\",\n        \"https://www.etymonline.com/word/on\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:39\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt block ending 'Page(s): 39-40': 'Root / lemma: an 4, anu, and, no — Meaning: a preposition (\\\"along a slanted surface, etc.\\\") — Material: Avestan ana, Old pers. ana … \\\"along, on\\\" (m. Akk.), Avestan anu, Old pers. anuv \\\"after, according to; up there\\\" … References: WP. I 58 f., WH. I 43 f., 49, 677'. Exactly the root, gloss and first branch Nourai draws.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"ana : on, upon; anu, anuv : to, after, along; anu-i : going along\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Av. ana and (per Bartholomae) OP anā continue the PIE particle *h₂ana with acc./instr. 'over along, on'; Av. anu / OP anuv (with the Old Persian glide -v written for word-final -u, §, Kent's 'anuv (i.e. anu)') continue the -u extension *h₂enu, matching Skt. ánu 'after, along'. Both are inherited, not borrowed: intervocalic *-n- is stable in Iranian and the *a-vocalism is unchanged, so the Iranian forms are phonetically identical to the reconstructed particle. The third item 'anu-i \\\"going along\\\"' is not a lemma in Bartholomae or Kent; it looks like Nourai's citation form of the preverb anu- with the root ay-/i- 'to go' (cf. Skt. anv-i- 'to follow along', Av. anu + verbs of motion, e.g. anu.zafan- 'going along the muzzle'), i.e. a construction rather than a word — I could not confirm it as such. The one substantive problem is OP anā: Kent (Old Persian, 1950, Lexicon p. 168) parses the two attestations (DPe 8, XPa 14) as the instrumental singular of the demonstrative ²a- 'this' and states they are 'not to Av. Skt. ana-' and 'not prep.'; Bartholomae (AiW) and Pokorny do list 'p. anā' as the preposition. Nourai follows the older (Bartholomae/Pokorny) view.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E1%BC%80%CE%BD%CE%AC\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:39\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt, 'Root / lemma: an 4, anu, and, no' (Page(s): 39-40): 'Avestan ana, Old pers. ana (Proto Aryan *ana or *ānā) \\\"about there\\\" (m. Akk. or Instr.), \\\"along, on\\\" (m. Akk.), Avestan anu, Old pers. anuv \\\"after, according to; up there\\\" (m. Akk.), \\\"lengthwise, along\\\" (m. Lok.), also proverb [= Präverb]'.\"\n            },\n            {\n              \"ref\": \"KLN:67\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt leaf 47 (= printed pp. 67-68, the leaf carries the numerals '67','68'), s.v. ana-: 'Gk. ἀνα-, ἀν-, \\\"up to, upward, up, toward; … back, backward; against\\\", fr. ἀνά … cogn. with Avestic ana, \\\"on, upon\\\", L. an- in anhelāre … fr. I.-E. base *ano-, \\\"on, upon, above\\\".' Klein gives the Avestan form but not the Old Persian.\"\n            },\n            {\n              \"ref\": \"KNT:164\",\n              \"status\": \"partial\",\n              \"note\": \"Kent's Old Persian lexicon does have the words, but on p. 168, not 164 (KNT.txt leaf 189; the neighbouring leaf 187 carries the printed numeral 166, so printed = leaf − 21): 'anuv (i.e. anu) prep. \\\"along, according to\\\": Av. anu with acc., loc., \\\"toward, along\\\", Skt. ánu with acc. \\\"after, along\\\"'. But the same page CONTRADICTS the first word: 'anā ism. to ²a- (q.v.); DPe 8 (not to Av. Skt. ana-); XPa 14 (not prep.)', and s.v. ²a- Kent adds that the Akkadian a-ga-' and Elamite hi 'this' renderings 'refute[] interpretation … as prep. w. inst. \\\"throughout\\\", Av. ana with acc. \\\"along, on\\\", Gk. ἀνά \\\"along\\\"'. Page 164 is the first page of the lexicon (headwords a-, akarta- etc.), so the number is a page or two off as well.\"\n            },\n            {\n              \"ref\": \"DZA:57\",\n              \"status\": \"not_checked\",\n              \"note\": \"Rashed Mohassel, Darāmadi bar Dastur-e Zabān-e Avestāʾi (Khajeh 1364/1985): refs_online.json records no digital copy (kind 'purchase', only a revised e-book on taaghche.com), and it is not in the local library.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"AiW col. ~124, s.v. ana (BRT.txt line 4208)\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. ana, p. anā Praep. \\\"über — hin\\\"; 1) mit Akk. a) \\\"über — hin\\\" … b) \\\"entlang, längs\\\"' — Bartholomae accepts both the Avestan and the Old Persian preposition. And s.v. anu (line 4484): 'j. anu, p. anuv, g. anū: 1) Praep. a) mit Akk. α) \\\"nach, gemäss\\\" … b) mit Lok. \\\"längs, entlang an —\\\" … 2) Praev.'. Exactly Nourai's 'anu, anuv'.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Lexicon p. 168 (KNT.txt leaf 189)\",\n              \"stance\": \"partial\",\n              \"note\": \"confirms OP anuv as a preposition but explicitly denies that OP anā is this word (see ref_check above).\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 39-40 s.v. 4. an, anu, and, no\",\n              \"stance\": \"supports\",\n              \"note\": \"as quoted above; also notes the -ī final that may lie behind Nourai's 'anu-i': 'Adv. \\\"on it\\\" (auslaut -ī appears to be comparable in Lesbian Thessalian [ὀνί] beside Attic ἀνά)'.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, s.v. ana (IEC.txt line 517)\",\n              \"stance\": \"supports\",\n              \"note\": \"'ana (ono) \\\"on, upon\\\" WP I, 57 … Av. ana; … Gk. aná; Osc. ana-, an-; Go. OFris. ana.' Mann lists Avestan but no Old Persian.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Germanic\",\n          \"words\": \"ana, ano\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *ana / *anē 'on' directly continues PIE *h₂ana with no change (Germanic keeps *a as a and *n as n; the root is unstressed and never underwent Verner or the vowel shifts that affect full lexical words). It is attested as Gothic ana (with dat. and acc.) 'on, in, against', Old Norse á, Old Saxon an, Old English on/an, Old High German ana/an > German an, Middle Dutch aan. Nourai's two citation forms 'ana, ano' are the short and lengthened stems (*ana, *anē), i.e. AHD's '*ana, anē'.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/on\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt, s.v. an³: 'an³. On. Extended form *ana. 1. Germanic *ana, anē in: a. Old English an, on, a, on: ON; b. Old Norse á, in, on: ALOFT; c. Old High German ana (> Middle High German ane), on: ANLAGE; d. Middle Dutch aan, on: ONSLAUGHT. 2. Greek ana, on, up, at the rate of: ANA², ANA-. [Pok. 4. an 39.]' — this single entry is the source of both of Nourai's branches (Germanic and Greek) and of the two forms 'ana, ano'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"p. 67 s.v. ana-\",\n              \"stance\": \"supports\",\n              \"note\": \"'cogn. with … Goth. ana, OE. on, an, OSlav. na, Lith. nu, OPruss. no, na, \\\"on, upon\\\"'.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 39-40\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gothic ana (m. dat. mid Akk.) \\\"on, in, against, because of, about\\\", Old Norse á … Old Saxon an, Old English on, Old High German ana, an, Modern High German an (*ana or *anō, *anē) preposition m. dat. and Akk. and Instr.'\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, s.v. ana (IEC.txt line 517)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Go. OFris. ana'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"on, upon, unless\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"OE on (unstressed variant of an) 'in, on, into' < PGmc *ana; ME on > NE on with no further change. 'Upon' is the Middle English univerbation of up + on (13c., on the model of / reinforced by Old Norse upp á), so its second element is this same word. 'Unless' is not the negative prefix un- at all: it is a reshaping of Middle English 'on lesse (that)' 'in a less (case) that', with on- later assimilated to un- by folk-association with the privative prefix; so it too contains the preposition on. All three therefore belong under this root, which is the (slightly startling) point Nourai is making by listing them together.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/on\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"the chart gives this node no reference of its own; it inherits the AHD citation of its parent (Germanic) node, which does list 'Old English an, on, a, on: ON'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt line 40823, s.v. unless (leaf 890 ≈ p. 1756)\",\n              \"stance\": \"supports\",\n              \"note\": \"'unless, conj. — Fr. earlier onlesse, onlesse that, i.e. \\\"on less that\\\". Cp. F. à moins que, \\\"unless\\\", lit. \\\"on less that\\\", and see on and less.' Klein derives unless from on, exactly as the chart implies.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"SKT.txt line 20415, s.v. Un- (1)\",\n              \"stance\": \"partial\",\n              \"note\": \"Skeat treats un- (1) as the negative prefix from A.S. un-, IE *n̥-, i.e. a different word; he does not connect un- to on. This is consistent with Klein: it is only in 'unless' specifically that the un- goes back to on-, not the productive prefix.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. an³\",\n              \"stance\": \"supports\",\n              \"note\": \"'Old English an, on, a, on: ON'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"ana- : according to, upward, back, again; ana-luein : to loosen back, analyze; analogos : speak according to, give analogy\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gk. ἀνά / ἀνα- 'up, on, upon, throughout; back; again' continues *h₂ana unchanged (Attic-Ionic ἀνά, with the dialectal shortened forms Doric-Boeotian ἄν, Lesbian-Thessalian ὄν); it lost its independent prepositional use in Koine but survived as a very productive preverb. ἀναλύειν 'to unloose, release, set free' = ἀνα- 'back, up' + λύειν 'to loosen' (PIE *leu- 'to cut apart'), whence the verbal noun ἀνάλυσις 'a loosing, releasing', which Aristotle used technically for 'analysis'. ἀνάλογος is ἀνά + λόγος in the sense 'ratio, proportion' — so the correct gloss is 'proportionate, conformable, according to due ratio', not the chart's 'speak according to, give analogy'; that gloss reflects the other sense of λόγος ('speech'), and is the one loose spot in an otherwise correct node.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E1%BC%80%CE%BD%CE%AC\",\n            \"https://www.etymonline.com/word/analysis\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"the chart gives the Greek node no reference; its child (English) carries 'AHD', and AHD's an³ entry covers the Greek link ('2. Greek ana, on, up, at the rate of: ANA², ANA-').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"p. 67 s.v. ana- and p. 70 s.v. analysis, analogy\",\n              \"stance\": \"supports\",\n              \"note\": \"s.v. analysis: 'Gk. ἀνάλυσις, \\\"a loosing, releasing\\\", fr. ἀναλύειν, \\\"to unloose, release, set free\\\", fr. ἀνά, \\\"up, on, throughout\\\" (see ana-), and λύειν, \\\"to unfasten, loosen, slacken\\\"'; s.v. analogy: 'F. analogie, fr. L. analogia, fr. Gk. ἀναλογία, \\\"proportion, analogy\\\", fr. ἀνάλογος' — note Klein's gloss 'proportion', confirming the correction above.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 39-40\",\n              \"stance\": \"supports\",\n              \"note\": \"'Ionic-Attic ἀνά, ἀνά \\\"on, upwards, along\\\", Doric Boeotian Arcadian Cypriot ἄν, Lesbian Thessalian Arcadian … ὄν … Adv. ἄνω \\\"upward, up\\\"'.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, s.v. ana\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gk. aná'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"analysis, analogy, anatomy\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are learned borrowings of Greek ἀνα- compounds through Latin and (for two of them) French. ANALYSIS: Gk. ἀνάλυσις > ML. analysis, into English 1580s in the sense 'resolution of a complex whole into simple elements'. ANALOGY: Gk. ἀναλογία > L. analogia > F. analogie > E. analogy (15c.). ANATOMY: Gk. ἀνατομή/ἀνατομία 'a cutting up, dissection' (ἀνά 'up' + τέμνειν 'to cut') > LL. anatomia > OF. anatomie > ME. anatomie (late 14c.), sometimes misdivided as 'an atomy' (whence the obsolete noun atomy 'skeleton'). In each the ἀνα- is Nourai's root; the second elements belong to other roots (*leu-, *leg-, *tem(ə)-).\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/analysis\",\n            \"https://www.etymonline.com/word/anatomy\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"partial\",\n              \"note\": \"AHD_watkins1985.txt s.v. an³ lists only 'ANA², ANA-' as the English reflexes of the Greek branch; ANALYSIS, ANALOGY and ANATOMY are indexed in the same book under leu-¹, leg- and tem- respectively (for their second elements). So AHD supports the ana- element of all three but does not list the three words at an³; the arrow is right, the citation is loose.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt lines 2636-2676 (pp. ~70-71)\",\n              \"stance\": \"supports\",\n              \"note\": \"s.v. anatomy: 'F. anatomie, fr. L. anatomia, fr. Gk. ἀνατομία, ἀνατομή, \\\"dissection\\\", which is related to ἀνατέμνειν, \\\"to cut up\\\", fr. ἀνά (see ana-) and τέμνειν \\\"to cut\\\"'; analysis and analogy as quoted on node 4.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"SKT.txt s.v. Anatomy / Analysis\",\n              \"stance\": \"supports\",\n              \"note\": \"Skeat's concise entries give the same Greek chain (ana- + temnein / ana- + luein).\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"A.n.b, anbar\",\n      \"verdict\": \"disputed\",\n      \"modern_form\": \"Arabic عَنْبَر ʿanbar 'ambergris', itself a loan from Middle Persian ambar (ʾmbl)\",\n      \"note\": \"Three problems with the root box. (1) The consonantal frame is wrong: عنبر is ʿ-n-b-r, a quadriliteral, and it has no Arabic verbal derivation; 'A.n.b' (ʿ-n-b) is the root of عِنَب ʿinab 'grape', an unrelated word. (2) The direction of borrowing is disputed: MacKenzie's Concise Pahlavi Dictionary has Middle Persian 'ambar [ʾmbl, ʾnbl | Ar. ʿanbar] ambergris', and Asbaghi, Persische Lehnwörter im Arabischen (1988) p. 204 lists ʿanbar among Persian loans in Arabic — 'ʿanbar: \\\"Amber\\\" pers. عنبر ← mp. ambar → ar. ʿanbar, it. ambra, frz. ambre, sp., pg. ambar, engl. amber, dtsch. Amber, russ. ambra' — and uses it in his phonology as the standard example of Persian -mb- > Arabic -nb- (p. 24: 'pers. mb → ar. nb, z. B.: ambar > ar. ʿanbar'). Wiktionary follows this. The Persian lexicographic tradition (Borhān-e Qāṭeʿ with Moʿin's note, Moʿin's own Farhang) does mark عنبر as Arabic (ع.), which is what Nourai follows, and no Western Semitist derives it from an Arabic root either — Klein, Skeat, Lokotsch and Devic all simply say 'Arab. ʿanbar' without going behind it. So the safest modern statement is: Arabic ʿanbar, probably itself of Middle Persian origin; the New Persian word is a re-borrowing from Arabic (the ʿayn and the -n- prove Arabic mediation). (3) The gloss is anachronistic: Arabic ʿanbar means 'ambergris', the intestinal secretion of the sperm whale; the 'fossil resin' sense of English amber arose only in late-medieval Europe.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B9%D9%86%D8%A8%D8%B1\",\n        \"https://www.etymonline.com/word/amber\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"FVA:286\",\n          \"status\": \"not_checked\",\n          \"note\": \"S.M. Nahvi, Farhang-e Vāžehā-ye ʿArabi dar Fārsi (dakhil), Tohi/Azadi 1368/1989 — refs_online.json records 'kind: catalog', no digital copy found on archive.org, ketabnak, noorlib or the open web, and the book is not in the local library.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"anbar «عنبر» : amber\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"New Persian عنبر is pronounced ʿanbar (the chart's bare 'anbar' drops the ʿayn) and means 'ambergris' — the grey, waxy sperm-whale secretion used in perfumery — with 'amber' only by the same European confusion. Formally it is an Arabic word in Persian: Persian has no ʿayn of its own, and Persian /mb/ is not written /nb/, so the shape عنبر can only have come back into Persian from Arabic, in the ʿAbbasid period when the Arabic pharmacological and perfumery vocabulary was adopted wholesale. But the Arabic word is very probably itself Middle Persian ambar (Pahlavi ʾmbl/ʾnbl), so the true history is a round trip: MP ambar → Ar. ʿanbar (with the regular Persian -mb- > Arabic -nb- substitution and prothetic ʿayn) → NP ʿanbar. Nourai draws only the second leg, and labels it as an Arabic original. Note also that Persian انبار anbār 'storehouse' (< MP hambār, *ham-bar-) is a completely different word, well documented by Horn and Hübschmann, and must not be confused with this one.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B9%D9%86%D8%A8%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1382\",\n              \"status\": \"supports\",\n              \"note\": \"Fetched with tools/ref_page.py BQT:1382 (vol. 3 PDF page 175; cached at data/verification/sources/refs/ocr/BQT/1382.png/.txt). The entry reads: 'عنبر - بفتح اول و سوم، (عر) از عربی وارد فرانسوی (ambre) و انگلیسی amber شده و آن ماده‌است در مثانهٔ یک جانور بسیار بزرگ دریایی از جنس جانوری که در فرهنگهای فارسی «یال» با «وال» ضبط شده …' — i.e. 'ʿanbar, with fatḥa on the first and third [letters], (Arabic); from Arabic it passed into French (ambre) and English amber; it is a substance in the bladder of a very large sea animal …'. The page number and the content are exactly Nourai's claim, including the Arabic→European route drawn on the right of the chart.\"\n            },\n            {\n              \"ref\": \"FVA:286\",\n              \"status\": \"not_checked\",\n              \"note\": \"no digital copy of Nahvi's Farhang-e Vāžehā-ye ʿArabi dar Fārsi exists (see root-level ref_check).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Moʿin, Farhang-e Fārsi, s.v. عنبر (MON_part1.txt line 98670)\",\n              \"stance\": \"supports\",\n              \"note\": \"'عنبر: [ع.] (جان.) ماده‌ای چرب و خوشبو و کدر و خاکستری رنگ و رگه‌دار که از روده یا معدهٔ ماهی عنبر گرفته می‌شود. این ماده در عطرسازی بکار می‌رود' — Moʿin tags the headword [ع.] 'Arabic' and defines it as the fatty, fragrant, grey substance taken from the gut of the sperm whale, i.e. ambergris, not fossil amber.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD s.v. ambar (PHD_mackenzie.txt line 1006)\",\n              \"stance\": \"partial\",\n              \"note\": \"'ambar [ʾmbl, ʾnbl | Ar. ʿanbar] ambergris' — a Middle Persian word ambar existed with exactly this meaning; MacKenzie cross-refers it to Arabic ʿanbar without committing on direction. Its existence is what makes the Persian-origin case possible.\"\n            },\n            {\n              \"src\": \"PLA\",\n              \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen (1988) p. 204 s.v. ʿanbar\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'ʿanbar: \\\"Amber\\\" pers. عنبر ← mp. ambar → ar. ʿanbar, it. ambra, frz. ambre, sp., pg. ambar, engl. amber, dtsch. Amber, russ. ambra, syr. …' — Asbaghi reverses Nourai's arrow, making Arabic the borrower; and on p. 24 he uses this very word as his textbook example of the sound substitution 'pers. mb → ar. nb, z. B.: ambar > ar. ʿanbar'.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss der neupersischen Etymologie\",\n              \"stance\": \"silent\",\n              \"note\": \"grep for anbar/ambar in HRN.txt returns only anbār 'Speicher' (< anhāstan, hambar-) and hambārakapet — Horn has no entry for ʿanbar 'ambergris', as expected for a book that excludes Arabic loans.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien pp. ~13, 106\",\n              \"stance\": \"silent\",\n              \"note\": \"same result: 'anbar \\\"Speicher\\\", phl. anbār, arm. ambar', 'anbardan anfüllen' — the storehouse word only, no ʿanbar 'ambergris'.\"\n            },\n            {\n              \"src\": \"AFM\",\n              \"where\": \"Addi Shir, al-Alfāẓ al-Fārisiyya al-muʿarraba\",\n              \"stance\": \"silent\",\n              \"note\": \"grep of AFM.txt / AFM_pages.txt for عنبر and 'anbar' returns nothing: Addi Shir does not count ʿanbar among the Persian words arabicized.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Middle Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A pass-through box for the Medieval Latin form. The Arabic word entered Latin Europe with the drug and perfume trade of the crusading and Sicilian period; Medieval Latin has ambar, ambare, ambra, amber, ambre, ambrium (Anglo-Latin from the late 13th c.), and from the Latin/Romance forms come Italian ambra, Spanish/Portuguese ambar, alambar (with the Arabic article agglutinated), Old French ambre. The Arabic -nb- was pronounced and rendered -mb- (Skeat notes the Arabic itself was 'pronounced ʿambar'), and the final -r of ʿanbar is preserved in ambar but lost in the Italian/French forms by Romance apocope of the unstressed syllable plus feminine -a. Latin never had the ʿayn, which simply disappears.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/amber\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:60\",\n              \"status\": \"partial\",\n              \"note\": \"KLN_1966.txt leaf 43 (the leaf carries the printed numerals '60','61'), s.v. amber: 'ME., fr. OF. (= F.) ambre, fr. Arab. ʿanbar, \\\"ambergris\\\". Cp. It. ambra, Sp., Port. ambar, alambar, which all derive fr. Arab. anbar.' The page is right and the Arabic etymon is right, but Klein routes the word through OLD FRENCH, not Medieval Latin; he mentions no Latin stage at all. So this reference does not itself support the 'Middle Latin' box.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"DEV\",\n              \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale, p. 31 s.v. Ambre (DEV.txt leaf 57)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Ambre. Esp. alambar, port. alambre, ital. ambra. De l'arabe ʿanbar, ambre gris, nom qui est passé au succin ou ambre jaune. Les formes qu'on trouve dans la basse latinité, ambar, ambare, ambra, amber, ambre, ambrium, paraissent aussi confondre les deux substances.' Devic explicitly attests the Low/Medieval Latin forms Nourai's empty box stands for.\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch, Etymologisches Wörterbuch … orientalischen Ursprungs, Nr. 78 (p. 7)\",\n              \"stance\": \"partial\",\n              \"note\": \"'78. Ar. ʿanbar: Mit Assimilation ʿambar gesprochen; hieraus it. ambra, frz. ambre, sp. pg. ambar, [mit ar. Art.] alambar, alambre, rum. ambră, ambru; engl. ambre, ndl. amber, dtsch. Amber; russ. ambra.' Lokotsch derives the European words straight from Arabic without a Latin stage, and confirms the ʿanbar > ʿambar assimilation.\"\n            },\n            {\n              \"src\": \"PHN\",\n              \"where\": \"Pihan, Dictionnaire étymologique … s.v. AMBRE\",\n              \"stance\": \"supports\",\n              \"note\": \"'AMBRE, s. m. (a.) عنبر [ʿanbar] Substance résineuse, odorante et inflammable … Il y en a de deux sortes: l'ambre jaune ou succin, et l'ambre gris … Comparez l'espagnol et le portugais ambar et alambar …' — Arabic source, and the two-substance confusion.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"amber\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"First in English mid-14th c. as ambre, in the phrase 'ambre grice' = Old French ambre gris 'grey amber', i.e. ambergris; borrowed from Old French ambre (12c.) / Medieval Latin ambar, ultimately Arabic ʿanbar. The transfer to Baltic fossil resin is a European development (late 13c. in Anglo-Latin, c. 1400 in English), because both substances were picked up washed ashore; French kept the two apart as ambre gris vs. ambre jaune, English did not, and by the 16th c. 'amber' alone meant the resin while 'ambergris' was re-borrowed as a separate word. (The Romans had called the resin electrum, whence 'electric'.)\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/amber\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:60\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt leaf 43 = printed pp. 60-61: 'amber, n. — ME., fr. OF. (= F.) ambre, fr. Arab. ʿanbar, \\\"ambergris\\\". Cp. It. ambra, Sp., Port. ambar, alambar, which all derive fr. Arab. anbar. Cp. also amarillo. Cp. also ambrosia and the second element in next word [ambergris] and in Liquidambar, pomander.' Page and content are exactly as cited.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etym. Dict. s.v. Amber (SKT.txt line 613)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Amber. (F. — Span. — Arab.) … Arab. ʿanbar (pronounced ʿambar), ambergris; a rich perfume. The resinous [substance is] so called from a resemblance to [ambergris], which is really quite a different substance. ambergris, i.e. gray amber … F. gris, gray'. Skeat states the amber/ambergris confusion explicitly.\"\n            },\n            {\n              \"src\": \"DEV\",\n              \"where\": \"Devic s.v. Ambre\",\n              \"stance\": \"supports\",\n              \"note\": \"as quoted on node 2; also 'Liquidambar … est formé de ambar et de notre mot liquide'.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 4,\n      \"root\": \"Andho\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂endʰ-o- (older notation *andho-) 'blind, dark'\",\n      \"note\": \"The root, the label and the gloss are exactly Pokorny's. Its support is narrow, though: Pokorny's whole entry is Indo-Iranian plus one Gaulish word, and Walde-Pokorny prints the lemma with a question mark ('ondho- \\\"blind, dunkel\\\"?'). The Latin branch Nourai adds (node 3) is not in Pokorny at that page and is rejected by current Latin etymology — that is the only serious problem in the entry.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/umbra\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:41\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt: 'Root / lemma: andho- — Meaning: \\\"blind, dark\\\" — Material: Old Indic andha-, Avestan anda- \\\"blind, dark\\\", gall. andabata m. \\\"a gladiator who fought with a helmet without openings\\\" … References: WP. I 182, WH. I 46. Page(s): 41.' Root name, language, gloss and page all match. Note that Latin umbra does NOT appear in this entry.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"anda, ando : blind\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Av. anda- adj. 'blind' (Nourai's second form 'ando' is the nominative singular masculine andō, the regular Avestan outcome of a-stem *-as; Klein cites exactly this shape, 'Avestic andō, \\\"blind\\\"'). It continues PIE *h₂endʰ-o- with the regular Indo-Iranian merger of *e/*o/*a into a and the Iranian deaspiration of *dʰ > d, beside Old Indic andhá- which keeps the aspirate. The word is attested in the Young Avesta, e.g. Yašt 5.93 (Ābān Yašt), of libations offered by the blind. Iranian cognates confirm the etymon: Khotanese hana- 'blind', Parthian hnd, Ormuri ond, and Sogdian ʾntʾ (node 2).\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:41\",\n              \"status\": \"supports\",\n              \"note\": \"'Old Indic andha-, Avestan anda- \\\"blind, dark\\\"' (POK_full.txt s.v. andho-, Page(s): 41).\"\n            },\n            {\n              \"ref\": \"SYN:323\",\n              \"status\": \"supports\",\n              \"note\": \"Buck, Dictionary of Selected Synonyms, §4.97 BLIND (SYN.txt \\\\f-leaf 365; the section falls just before the start of chapter 5, so on the printed pp. 322-323 as cited). The comparative table reads '… Skt. andha- … Av. anda- …' alongside Lat. caecus, Goth. blinds etc.; Buck's discussion assigns Skt./Av. to their own inherited group and does not connect them to Latin.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AiW, s.v. anda- (BRT.txt \\\\f-leaf 108, line 4616)\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. anda- Adj. \\\"blind\\\": nōit̰ ava zaoθra paiti.vīse yā mās̆yā frataṷhannti ˚dąsca (NPm.) … Yt. 5.93.' with the cross-reference 'ai. andhá- Adj.' — Young Avestan adjective, exactly the meaning and the Indic cognate Nourai assumes.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny I 182 s.v. ondho- (WLD_Bd1 djvu line 11714)\",\n              \"stance\": \"supports\",\n              \"note\": \"'ondho- \\\"blind, dunkel\\\"? Ai. andha-, av. anda- \\\"blind, dunkel\\\", vielleicht nach Bezzenberger BB. 1, 342 zu lat. umbra \\\"Schatten\\\" (andere Deutungen von umbra s. bei Vf. LEWb.² s.v.)'. Supports the Indo-Iranian core; note the question mark on the lemma and the 'vielleicht' on umbra.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, IECD s.v. ondhos (IEC.txt line 12169)\",\n              \"stance\": \"supports\",\n              \"note\": \"'ondhos (andhos? See andhos (1)) \\\"dark, dingy, smoky; blind\\\". (Alleged Irish uinne \\\"blind\\\" indicates a type *ondh-; Gaul. anda- \\\"blindfold\\\" indicates a type *andh-.) Skt. andháḥ \\\"dark, blind\\\"'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. umbra (KLN_1966.txt line 40727)\",\n              \"stance\": \"supports\",\n              \"note\": \"cites the Avestan word in Nourai's very spelling: 'OI. ándhas-, \\\"darkness\\\", andháḥ, Avestic andō, \\\"blind\\\"'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sogdian\",\n          \"words\": \"ʿntʿ : blind\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Buddhist Sogdian ʾntʾ, read and (ənd), 'blind' — the Sogdian script writes the initial vowel with aleph, hence the two ʾ of the transliteration (Nourai's typography renders them as raised commas). It is the direct Sogdian outcome of Old Iranian *anda- (< PIE *h₂endʰ-o-): Sogdian preserves the -nd- cluster and the a-vocalism, with the usual reduction of the unstressed final syllable to schwa. Gharib's own entry supplies the Iranian comparanda that show it is inherited rather than borrowed: Av. anda-, Khot. hana, Parth. hnd, Ormuri ond.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:44\",\n              \"status\": \"supports\",\n              \"note\": \"Gharib, Sogdian Dictionary, entry no. 1127 (SOD_pages.txt \\\\f-leaf 109, i.e. printed p. ≈ 43-44, matching Nourai's SOD:44): '1127 ʾntʾ B — and (ənd) © Av. anda-; Khot. hana; Parth. hand; Orm. ond — blind. [refs] BSTBL, Dhy. 184; GMS 283; Hen. Brahman. 110 n 2; Bailey, Prolexis. 384'. Form, language, gloss and the derivation from Avestan anda- are all as drawn.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SOD\",\n              \"where\": \"entry 1127, p. ~44\",\n              \"stance\": \"supports\",\n              \"note\": \"as quoted; Gharib lists the whole Iranian set under this one entry.\"\n            },\n            {\n              \"src\": \"ISS_alt_DKS\",\n              \"where\": \"Bailey, Dictionary of Khotan Saka, s.v. kūra- (ISS_alt_DKS.txt line 1508)\",\n              \"stance\": \"supports\",\n              \"note\": \"'For \\\"blind\\\" Khotan Saka has hana-, Av. anda-.' Bailey confirms the Iranian family (Khot. hana- < *anda-ka-) that the Sogdian form belongs to; cf. also s.v. kārra- 'deaf', 'hana kārrā mūtä \\\"blind, dumb, deaf\\\", parallel Pali andha-, mūga-, badhira-'.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 41 s.v. andho-\",\n              \"stance\": \"silent\",\n              \"note\": \"Pokorny lists only Old Indic, Avestan and Gaulish under this root; Sogdian is not mentioned (Pokorny rarely cites Sogdian).\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"umbra : shadow\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The chart takes Latin umbra 'shade, shadow' from *andho- via a zero/o-grade *(o)ndh-ro- with the instrument/result suffix -rā (cf. tenebrae), so *ondʰ-reh₂ > *omra > umbra. That is Bezzenberger's old proposal, and it survives in the handbooks only as a possibility: Watkins/AHD prints 'Suffixed variant form *ondh-ro- PERHAPS in Latin umbra'; Walde-Pokorny I 182 says 'VIELLEICHT nach Bezzenberger … zu lat. umbra' and points to other explanations; Ernout-Meillet (p. 1318) call it 'plausible'; Klein flatly begins 'L. umbra, \\\"shade, shadow\\\", of uncertain origin. It is POSSIBLY cogn. with OI. ándhas-'. Pokorny's own p. 41 — the page Nourai cites for the root — does not list umbra at all. Current Latin etymology prefers a different origin: de Vaan (and Wiktionary after him) reconstructs Proto-Italic *unksrā, connecting umbra with Lithuanian unksmė / ùnksna 'shade', with the alternative (if from Old Latin *omra) *h₂mr-u- beside Greek ἀμαυρός 'dark'. Semantically the *andho- account is also weak: the Indo-Iranian word means 'blind' of a person, and the step to an inanimate 'shadow' is not paralleled. Nourai's Latin box is therefore an old, minority etymology, not the current one.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/umbra\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt: 'andho-. Blind, dark. Suffixed variant form *ondh-ro- perhaps in Latin umbra, shadow: UMBEL, UMBRA, UMBRELLA; ADUMBRATE. [Pok. andho- 41.]' — Watkins really is Nourai's source for this branch (and for the child node umbrella), hedged with 'perhaps'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 41 s.v. andho-\",\n              \"stance\": \"silent\",\n              \"note\": \"the cited page contains only 'Old Indic andha-, Avestan anda- … gall. andabata …; References: WP. I 182, WH. I 46' — no Latin umbra. Nourai's own root citation does not cover this arrow.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny I 182\",\n              \"stance\": \"partial\",\n              \"note\": \"'vielleicht nach Bezzenberger BB. 1, 342 zu lat. umbra \\\"Schatten\\\" (andere Deutungen von umbra s. bei Vf. LEWb.² s. v.)' — accepted only as a possibility, with an explicit pointer to rival explanations.\"\n            },\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet, DELL p. 1318 (LAT.txt line 69533 ff.) s.v. umbra\",\n              \"stance\": \"partial\",\n              \"note\": \"'Le rapprochement avec skr. andháḥ, av. andō \\\"aveugle\\\" et véd. ándhaḥ \\\"obscurité\\\" est plausible; pour le suffixe, cf. lat. tenebrae.' — 'plausible', not established. The same entry lists the derivatives that matter for node 4: 'umbella et dans les gloses umbrella (refait sur umbra): ombrelle'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. umbra (KLN_1966.txt line 40727, leaf 887 ≈ p. 1750)\",\n              \"stance\": \"partial\",\n              \"note\": \"'L. umbra, \\\"shade, shadow\\\", of uncertain origin. It is possibly cogn. with OI. ándhas-, \\\"darkness\\\", andháḥ, Avestic andō, \\\"blind\\\". For the suff. -bra in umbra cp. the suff. in L. tenebrae. See Ernout-Meillet, DELL., p. 745 s.v. umbra.'\"\n            },\n            {\n              \"src\": \"LEW\",\n              \"where\": \"Walde, LEWb (local file)\",\n              \"stance\": \"silent\",\n              \"note\": \"the local LEW_1910.txt turns out to be only the index volume (entries such as 'umb I 36'); the article s.v. umbra, to which Walde-Pokorny refers for the 'andere Deutungen', is not in the local text.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"umbrella\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin umbella 'sunshade, parasol', the diminutive of umbra, was refashioned in Late Latin/glossary Latin as umbrella under the influence of umbra itself (Ernout-Meillet: 'umbella et dans les gloses umbrella (refait sur umbra)'). Italian took it as ombrella/ombrello, and English borrowed the Italian form c. 1600, at first for a sunshade, the rain sense becoming primary in England in the 18th century. The verdict here is about the Latin→English chain, which is certain; whether Latin umbra in turn belongs to *andho- is the disputed point recorded on node 3.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/umbrella\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"no reference is printed on this node; it inherits the AHD citation of its Latin parent, and AHD s.v. andho- does list UMBRELLA among the English derivatives of umbra.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. umbrella (KLN_1966.txt line 40731)\",\n              \"stance\": \"supports\",\n              \"note\": \"'umbrella, n. — It. ombrella, fr. Late L. umbrella, alteration of L. umbella, \\\"a little shadow, sunshade, umbrella\\\", dimin. of umbra. See umbra and -ella and cp. umbel.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. umbrella (SKT.txt line 20415)\",\n              \"stance\": \"supports\",\n              \"note\": \"'umbrella. (Ital. — L.) Ital. umbrella, ombrella, a parasol; dimin. of Ital. ombra, a shade. — L. umbra, a shade.'\"\n            },\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet p. 1318, derivatives of umbra\",\n              \"stance\": \"supports\",\n              \"note\": \"'umbella et dans les gloses umbrella (refait sur umbra): ombrelle … M.L. 9049'.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-04T20:02:16.060Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-55.json (file state is current in your context — no need to Read it back)
```


## [2026-09-04T20:02:18.491Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-55.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 55"
}
```


### [2026-09-04T20:02:20.855Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'plausible': 2, 'confirmed': 9, 'disputed': 1}
root verdicts: {'confirmed': 2, 'disputed': 1}
ref checks: {'supports': 9, 'partial': 3, 'not_checked': 5}
books consulted: {'supports': 27, 'partial': 7, 'contradicts': 1, 'silent': 6} | by book: {'KLN': 7, 'POK': 5, 'IEC': 4, 'SKT': 4, 'BRT': 2, 'DEV': 2, 'WLD': 2, 'LAT': 2, 'KNT': 1, 'AHD': 1, 'MON': 1, 'PHD': 1, 'PLA': 1, 'HRN': 1, 'HUB': 1, 'AFM': 1, 'LKT': 1, 'PHN': 1, 'SOD': 1, 'ISS_alt_DKS': 1, 'LEW': 1}
```


## [2026-09-04T20:02:40.540Z] AGENT

Wrote `/home/sfmqrb/git/rishe/data/verification/page-55.json`; `verify_check.py 55` reports no PROBLEM lines.

**Page 55 (book p. 25) — 3 non-redirect entries, 12 nodes**
- Node verdicts: 9 confirmed, 2 plausible, 1 disputed
- Root verdicts: 2 confirmed (An 3/Anô, Andho), 1 disputed (A.n.b, anbar)
- Ref checks: 9 supports, 3 partial, 5 not_checked (FVA and DZA have no digital copy anywhere)
- Books consulted: 21 distinct (POK, WLD, AHD, IEC, SYN, KLN, SKT, LAT, LEW, BRT, KNT, PHD, SOD, ISS/Bailey, HRN, HUB, MON, BQT, PLA, AFM, LKT, DEV, PHN). 8 web pages archived via `fetch_source.py`.

Disputed / problem items:
- **ROOT "A.n.b, anbar" (Arabic, amber)** — disputed. (a) the consonantal frame is wrong: عنبر is quadriliteral ʿ-n-b-r; ʿ-n-b is the root of ʿinab 'grape'. (b) Direction reversed by modern scholarship: MacKenzie has MP *ambar* 'ambergris', and Asbaghi PLA p.204 gives "pers. عنبر ← mp. ambar → ar. ʿanbar", using it as his textbook case of pers. -mb- > ar. -nb-; Wiktionary agrees. (c) gloss anachronistic — Arabic ʿanbar = ambergris, not fossil amber.
- **Latin *umbra* under Andho** — disputed. AHD (Nourai's own ref) says "*ondh-ro- **perhaps** in Latin umbra"; Pokorny p.41, the page cited for the root, has no umbra at all; WLD "vielleicht", Ernout-Meillet "plausible", Klein "of uncertain origin". De Vaan/Wiktionary now prefer PIt. *unksrā ~ Lith. ùnksna 'shade'.
- **Node 1 of An 3 (Av./OP ana, anu, anuv, anu-i)** — plausible. Kent (KNT, lexicon p. **168**, not 164) explicitly rejects OP *anā* as this preposition ("not to Av. Skt. ana-", "not prep."), reading it as instr. sg. of the demonstrative; Bartholomae and Pokorny do support it. "anu-i" is not a lemma in BRT or KNT (looks like the preverb anu- + i- 'go', cf. Skt. anv-i-).
- **Persian ʿanbar node** — plausible: BQT:1382 and Mo'in both tag it Arabic (supports Nourai), but the word is really a round trip MP ambar → Ar. ʿanbar → NP عنبر; also unrelated to Persian انبار anbār 'storehouse'.
- Minor: Greek node's gloss for *analogos* ("speak according to") should be "proportionate, according to due ratio"; Klein's KLN:60 routes *amber* via Old French, not the "Middle Latin" box Nourai draws (Devic does attest Low-Latin ambar/ambra/ambrium, so the box itself stands).

No transcription_suspect items: I rendered PDF page 55 and confirmed the book itself prints "A.n.b, anbar" and "`nt`", so the JSON is faithful to the scan.
