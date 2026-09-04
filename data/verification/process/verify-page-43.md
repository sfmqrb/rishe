# Verification process log — verify-page-43


## [2026-09-04T19:09:52.867Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 43 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-43.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-43.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-43.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 43` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T19:09:54.419Z] AGENT

I'll start by reading the instructions file.


## [2026-09-04T19:09:56.537Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:09:56.552Z] TOOL RESULT

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


## [2026-09-04T19:09:56.768Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-43.txt"
}
```


### [2026-09-04T19:09:56.790Z] TOOL RESULT

```
1	=== PDF page 43 (book page 13) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ak, Aq, Aken : sharp, also a sharp stone  (refs POK:18; KNT:173)  PART 2
4	#1 (parent #0) [Indo-European] refs=POK:541,542 | Ke 1, Kei 3, Ko 1, Koi : sharp, to sharpen
5	  #2 (parent #1) [Avestan] refs=POK:542; SNS:18; IEC:11 | saěni, saěniš, čâna : pointed, sharp or rough objects used for grinding ; asânam : whetstone ; abi-čâna, abhi-čâna : grinding stone | NOTE: Compare with root "Sek"
6	    #3 (parent #2) [Persian] refs=POK:542; BQT:1077,1488; SNS:18; MMF:325 | sâyîdan «ساییدن» : to grind, rub ; fesânîdan «فسانیدن ( افسانیدن )» : to grind, rub ; fsân «فسان ( افسان )» : grinding stone | extra: سای ، ساو ، ساب ، سان ، سوهان
7	  #4 (parent #1) [Old Persian] refs=IEC:11 | asa, asam : whetstone
8	  #5 (parent #1) [Germanic] refs=AHD | hainô : grinding stone
9	    #6 (parent #5) [English] refs=AHD | hone
10	  #7 (parent #1) [Greek] refs=AHD | kônos : sharp pointed, cone
11	    #8 (parent #7) [English] refs=AHD | cone
12	--- entry 1 ---
13	ROOT Aken -> redirect to Ak
14	--- entry 2 ---
15	ROOT [Indo-European] Akos, Âkos : suffix indicating small size  (refs IEC:9)
16	#1 (parent #0) [Pahlavi] refs=MON:2775 | -ak
17	  #2 (parent #1) [Persian] refs=IEC:9; MON:2775 | -ak «ـک» : a suffix indicating small size | extra: مرغک ، کنیزک | NOTE: See "Kak" for another possible root of suffix "-ak"
18	#3 (parent #0) [Sanskrit] refs=IEC:9 | -akah : small
19	--- entry 3 ---
20	ROOT Âkos -> redirect to Akos
21	
```


## [2026-09-04T19:10:01.237Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-43.json && echo \"=====MATRIX=====\" && cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T19:10:01.290Z] TOOL RESULT

```
{
  "pdf_page": 43,
  "book_page": 13,
  "entries": [
    {
      "part": 2,
      "root": {
        "name": "Ak, Aq, Aken",
        "lang": "Indo-European",
        "refs": "POK:18; KNT:173",
        "gloss": "sharp, also a sharp stone"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "POK:541,542",
          "words": [
            {"translit": "Ke 1, Kei 3, Ko 1, Koi", "gloss": "sharp, to sharpen", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "POK:542; SNS:18; IEC:11",
          "words": [
            {"translit": "saěni, saěniš, čâna", "gloss": "pointed, sharp or rough objects used for grinding", "script": null},
            {"translit": "asânam", "gloss": "whetstone", "script": null},
            {"translit": "abi-čâna, abhi-čâna", "gloss": "grinding stone", "script": null}
          ],
          "note": "Compare with root \"Sek\"",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "POK:542; BQT:1077,1488; SNS:18; MMF:325",
          "words": [
            {"translit": "sâyîdan", "gloss": "to grind, rub", "script": "ساییدن"},
            {"translit": "fesânîdan", "gloss": "to grind, rub", "script": "فسانیدن ( افسانیدن )"},
            {"translit": "fsân", "gloss": "grinding stone", "script": "فسان ( افسان )"}
          ],
          "script_extra": "سای ، ساو ، ساب ، سان ، سوهان",
          "note": null,
          "quote": {
            "text": "طبع و دل خنجری و آینه است - رنج و غم صیقلی وافسان است",
            "poet": "Mas`ŭd Sa`d Salmân"
          }
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Old Persian",
          "refs": "IEC:11",
          "words": [
            {"translit": "asa, asam", "gloss": "whetstone", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "hainô", "gloss": "grinding stone", "script": null}
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
            {"translit": "hone", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 1,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "kônos", "gloss": "sharp pointed, cone", "script": null}
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
            {"translit": "cone", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Aken", "redirect": "Ak"},
      "nodes": []
    },
    {
      "root": {
        "name": "Akos, Âkos",
        "lang": "Indo-European",
        "refs": "IEC:9",
        "gloss": "suffix indicating small size"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "MON:2775",
          "words": [
            {"translit": "-ak", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "IEC:9; MON:2775",
          "words": [
            {"translit": "-ak", "gloss": "a suffix indicating small size", "script": "ـک"}
          ],
          "script_extra": "مرغک ، کنیزک",
          "note": "See \"Kak\" for another possible root of suffix \"-ak\"",
          "quote": {
            "text": "از حال نباتی برسیدم به ستوری - یک چند همی بودم چون مرغک بی پر",
            "poet": "Nâserkhosrow"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:9",
          "words": [
            {"translit": "-akah", "gloss": "small", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Âkos", "redirect": "Akos"},
      "nodes": []
    }
  ]
}
=====MATRIX=====
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


## [2026-09-04T19:10:03.458Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','KNT','IEC','AHD','SNS','BQT','MMF','MON','WLD','SYN','HRN','HUB','CHEUNG','PHD','NYB','BRT','KLN','SKT','ARY']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-04T19:10:05.653Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MMF {"title": "K. Khalili, Farhang-e Moshtaqqat-e Masader-e Farsi (Dictionary of Derivatives of the Persian Infinitives), Institute of Cultural Studies and Research 1993", "kind": "login_required", "url": "https://ketabnak.com/book/127793 (vol.1) ; /127795 (vol.2) ; /127796 (vol.4) — free registration for online reading; also tebyan online reader", "lookup_hint": "Not found.", "local_file": null, "pag
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG null
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root,
```


## [2026-09-04T19:10:41.135Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK p18 area (ak-) ===\"\ngrep -n \"scharf, spitz, kantig\" POK_full.txt | head -20\necho \"=== POK kē(i) ===\"\ngrep -n \"schärfen, wetzen\" POK_full.txt | head -20\necho \"=== AHD kō- ===\"\ngrep -n -i \"whetstone\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-04T19:10:41.208Z] TOOL RESULT

```
=== POK p18 area (ak-) ===
=== POK kē(i) ===
=== AHD kō- ===
323:outlaw”), in: a. Old English bannan, to summon, pro- claim, and Old Norse banna, to prohibit, curse: BAN}; b. Old French ban, feudal jurisdiction, summons to military service, proclamation, Old French bandon, power, and Old English gebann, proclamation: BANAL, BANNS; ABANDON; C. Old French banir, to banish: BAN- ISH; d. Late Latin bannus, bannum, proclamation: Ccon- TRABAND; @. Italian bandire, to muster, band together (< “to have been summoned”): BANDIT. 4. Suffixed form *bha-ni in Germanic *b6dni- in Old Norse b6n, prayer, request: BOON!. 5. Suffixed form *bhd-ma in: a. Latin fama, talk, reputation, fame: FAME, FAMOUS; DEFAME, INFAMOUS; b. Greek phémé, saying, speech: EUPHEMISM. 6. Suffixed o-grade form *bhd-nd in Greek phéné, voice, sound, and phénein, to speak: PHONE, -PHONE, PHO- NEME, PHONETIC, PHONO-, -PHONY; ANTHEM, (ANTI- PHON), APHONIA, CACOPHONOUS, EUPHONY, SYMPHONY. 7. Suffixed zero-grade form *bha-to- in Latin fatéri, to acknowledge, admit: CONFESS, PROFESS. 8. Greek blas- phémos, evil-speaking, blasphemous (first element ob- scure): (BLAME), (BLASPHEME), BLASPHEMOUS. [Pok. 2. bha- 105.] bha-bha-. Broad bean. 1. Latin faba, broad bean: FAVA BEAN. 2. Variant form *bha-un- in Germanic *bauné in Old English béan, broad bean, bean of any kind: BEAN. [Pok. bhabhé 106.] bhad-. Good. 1. Germanic (comparative) *batiz6 in Old English betera, better: BETTER. 2. Germanic (superla- tive) *batistaz in Old English bet(e)st, best: BEST. 3. Ger- manic noun *b6¢6 in Old English bét, remedy, aid: BooT?. 4. Germanic verb *batnan, to become better, in Old Norse batna, to improve: BATTEN!. [Pok. bhdd- 106.] bhag-'. To share out, apportion, also to get a share. 1. Greek phagein, to eat (< “to have a share of food”): -PHAGE, -PHAGIA, PHAGO-, -PHAGOUS. 2. Extended form *bhags- in Avestan bakhsh- in Persian bakhshidan, to give: BAKSHEESH, (BUCKSHEE). [Pok. 1. bhag- 107.] bhag-. Sharp. Suffixed form *bhag-ro- in Greek phag- ros, whetstone, also a name for the sea bream: PORGY. [Pok. 2. bhag- 107.] bhaghu-. Arm. Germanic *bdguz in Old English bdg, boh, bough: BouGu. [Pok. bhdghii-s 108.] bhago-. Beech tree. 1. Germanic *b6k6, beech, also “beech staff for carving runes on” (an early Germanic graphic device), in: a. Old English bdc, written docu- ment, composition: BOOK; b. Middle Dutch boek, beech: BUCKWHEAT. 2. Germanic *bdkjdn- in Old English béce, beech: BEECH. [Pok. bhdgo-s 107.] bhar-. Also bhor-. Projection, bristle, point. 1. Suffixed o-grade form *bhor-so- in Germanic *barsaz in Old English bzrs, perch, bass (a fish that has a spiny dorsal fin): BASs!. 2. Suffixed zero-grade form *bhAr-sti- in Germanic *bursti- in Old English byrst (> Middle Eng- lish bristel), bristle: BRISTLE. 3. Extended zero-grade form *bhrs- in: a. Germanic *bur- in Swedish borre, bur, perhaps akin to the Scandinavian source of Middle English burre, bur: BUR}; b. suffixed form *bhrs-dh- in Germanic *bruzd-, point, needle, in Old Norse broddr, spike: BRAD; C. suffixed form *bhrs-ti- in Latin fastig- ium, summit, top, extremity: FASTIGIATE, FASTIGIUM; d. possibly suffixed form *bhrs-tu- in Latin fastus, fasti- dium, disdain (from the notion of prickliness): FASTIDI- ous; e. suffixed form *bhrs-tio- in Russian borshch, cow parsley: BORSCHT. [Pok. bhar- 108.] bhardha. Beard. Possibly related to bhar-. 1. Germanic *bardaz in Old English beard, beard: BEARD. 2. Ger- manic *bard6, beard, also hatchet, broadax (the associ- ation of beard and ax is attested elsewhere in the Indo-European family; both were symbols of patriarchal authority), in Old High German barta, beard, ax: HAL- BERD. 3. Latin barba, beard: BARB!, BARBEL, BARBEL- LATE, BARBER, BARBETTE, BARBICEL, BARBULE; REBARBATIVE. [Pok. bhardhé 110.] bhares-. Also bhars-. Barley. 1. Germanic *barz- in Old
```


## [2026-09-04T19:10:42.368Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC around page 9-11 ===\"\ngrep -n \"akos\\|ākos\\|-akah\\|akah\" IEC.txt | head -30\necho \"=== IEC asan ===\"\ngrep -n \"asan\\b\\|asānam\\|asan-\" IEC.txt | head -30"
}
```


### [2026-09-04T19:10:42.428Z] TOOL RESULT

```
=== IEC around page 9-11 ===
344:-akos, -àkos (diminutive suffix) Skt. -akah, -aka; Per. -ak; Arm. -ak; Alb. -ok; W og: OCS -akü; Li. -okas (in adjj.)
388:aksis, -ó(n) ‘axle, axis, pivot. WP I, 37 Skt. áksah; Myc. akosone (*aksones, pl.); Gk. áxon; Lat. axis, g.p. axium (fLat. axis, as also Gk. áxon are from ago)” — Ainsworth 1736); MIr. ais; OE eax; OHG ahsa; Du. as; LG ass, pl. en OCS ost Li. ašis, gp. aSiü, m. & f.; Latv. ass, gs. ass, gp. asu ‘axle’
964:bol-, bolok- ‘clod; clot, churľ’ Skt. bälah ‘young, minor’; balakah ‘youngster, fool’; Gk. (ambig.) bõlos, bolax ‘clod’; Ir. bálach "chu, clown’
1090:bhak-, bhakolos ‘compact; lump’. Cf. bhakos, bhaK-, bhaks- Gk. cf. óm-phax, -phakos “bunch of sour grapes’, phákelos ‘bunch’; Alb. bake *pot- belly’, bákull ‘tubby’; Lat. (fr. Celt.?) bacci- num: basin (see Dauzat: bassin); Ir. baicle, baclach ‘crowd’; Br. bagol ‘hale, hearty’; W cf. bagad “cluster, crowd", bagwy ‘clump’; Srb. cf. bokast ‘humped’?
1092:bhakos (bhokos?) ‘side, flank’ Arm. bak (‘limb’. Semantics of Go. fera ‘side; limb); OCS bokü (and comm. SI.) ‘flank’; cf. Srb. bokonj ‘side of ship’
1097:63 bhakos, à — bhand- 64
1099:bhakos, å ‘leguminous seed, bean, lentil’. WP II, 131 Av. cf. baxto ‘leguminous’; Gk. phakós ‘lentil’, a-pháke ‘vetch’ beside pháselos, phasiolos (*-Ki-) ‘bean’; Alb. bathé “broad bean’
2577:dumbos, à «thick, plump; mass, lump, tail. WP I, 816 Skt. cf. dumbakah, dim. 'fat-tailed sheep’; Per. dumbe ‘fat on tail of sheep’; Alb. dumé, adj. ‘plump’; OHG zumpfo; MHG zumph(e) ‘penis’; LG tümp ‘pack, crowd'; E tump “hil- lock. Cf. the variants Per. dum ‘tail’; Av.
2644:in Arm. krkin ‘double’, cf. LG twit ‘narrow dividing lane’; E dial. twitton, twit, id.; *-&en-, *-Genes- in Skt. dvi-jánman; Gk. digenés and Lat. bigener, bigeneris; *-gueni- in Skt. dvi- jànih 'bigamous' and ON tví-kveni; *-iug- in Skt. (o-gde) dvyogah; Gk. dí-zux, -zugos & Lat. bi-jugis, -jugus; cf. Latv. div-jugs, s. 'two- in-hand'; *-plos, -plos in Av. bifro; Gk. diploüs, -plóos, -plós; Lat. duplus; Go. tweifls; OHG zwival; OFris. twifil and Du. twijfel; *-ped-, pod-, pd- in Skt. dvi- padah; Av. bib- dəm; Arm. cf. erkot-ani; Gk. di-podēs; Lat. bi-pēs, gs -pedis; cf. OE twi-fete; ON tví- foettr; *-poltos, -pltos in Gk. dí-paltos, di- plásios; Go. -falbs; MHG zwi-valt and ON tví-faldr; *-qusakos (or *-kakhos) in Skt. dvi- khakah, (-$akhah) ‘forked, two-pronged, bi- furcated'; Gk. dípsakos; Per. dū-šāxe and Li. dviSakas; *-rotos, (-rothos) in Lat. birotum, -rota and Li. dvirátis (fr. *rotios)
2760:dhēkos, å, iə “placing, setting, fixture, recep- tacle’. Cf. dheio (2), etc. Skt. dhakah (2) ‘receptacle’; Gk. thékē, id.; Alb. doke ‘custom, habit, duty, task’; Latv. deka ‘adventure, mishap’; Li. cf. deklas ‘case, container
2982:dhokos, ios ‘repository’. Cf. dhekos Skt. dhakah ((2) ‘receptacle’. Equally to dhe- ko-, q. v.); Gk. thókos, m. ‘seat, court, shop’; Latv. dokis 'salt-vat; salmon-trap'. For Li. sf. duo-klé and W dawg see do (4) ‘give’, and cpds.
3271:dhülos, à, io (2) (?) ‘hollow, receptacle’ Gk. cf. thül-ax & -akos ‘bag’; W dill ‘plait, fold" (but dillad, s. “clothes? seems to reflect with *-ū Icel. dula ‘worn piece of cloth’, with *ü); SWG Tüle ‘hollow, dell: Hes. thul- lis = thúlakos.
5118:guakos (or guaKos), ios “empty, vain’. Cf. guag- (2) Oss. (*-à-) qwag, Dig. gäwagä ‘lacking’; Gk. cf. bákëlos ‘eunuch’; Lat. (ambig.) vacuus, va- civus; (LW in) W gwag ‘empty’; Li. gašùs “fop- pist’ beside baslüs ‘lewd’, gašnùs (“dandified?. Cf. also Gk. bákēlos in this sense);
6201:Skt. avikab, -ā ‘ram; ewe’; gudika (pellet: gudah); balika (‘little gir: bala); Arm. matik (‘little finger’: mat); Snik (‘pup’: Sun, cf. Skt. Sunakah, dim. id.); Lat. canticus (‘song’: can- tus); cf. carrüca, beside carrus “little cart’; Bret. moedik (‘little thumb’: moed); OCS cf. otici (*daddy', cf. Gk. átta); potoðici ("little stream’: potokü); etc.; Li. kulikas (little bag’: kule); Sunikas (‘rascaľ’: Suð); cf. Li. avike *ewe-lamb'. For Cz. srnec (‘fallow deer: OCS srini 'roe- buck', see Krn-)
6445:ieunkos (iounk-, iuunk-) ‘young creature, young person'. Cf. ieunos. WP I, 200 Skt. yuvakah, m.; yuvanakabh, adj.; Oss. wånig, onig, iwonig, jonág ‘bullock’; LW in Arm za- vag ‘child’ (Iran.); Lat. juvencus (fyoung, of animals’; s. 'steer); Umb. iuengar, fpl. "ber, fers’; Gaul. iovinco- (in names); MIr. ócc, Ir. óg ‘young’; ‘young person’; W ieuanc; Br. iauank; Cor. yowynk, adj. ‘young’; Go. juggs; OE geong; ON ungr, adj. ‘young’ & com. Gmc. Cz. cf. jun, junák ‘youngster’
6640:kakos, ios ‘foul, filthy’. WP I, 336 and cf. kākstios, kakā Skt. cf. kacakuh ‘wicked, intolerable’ beside kaccarah ‘foul, bad?; Gk. kakós; Alb. i keq, f. e keqe ‘bad’; Lat. cacus ((camp-boy', Dei: Ligurian (in Rumansch) cac, f: caca ‘ugly’; Big. (?) koc ("latrine' fr. kakios?)
6653:kal- (1) (kalt-) ‘slope’. Cf. WP I, 430 and kalt- Skt. cf. katakah 'slope'; Go. wilja-halpei, f. ‘favour’; OHG hald, adj. ‘inclined’; G Halde ‘slope’; Du. cf. hellen, v. ‘tilt’; ON hella *de- cant’; R cf. po-kolét ‘die off”; Li. kaliuos, kal- tis ‘lean’; üZ-kaliu, -kalti ‘lean’; at-kaltis, f. “back of chair; LW in Finn. kaltto, kalteva ‘sloping’
6986:Skt. cf. Camarakah, dim. ‘bee’; Cz. čmel
7213:kiriquaquos, à ʻa cackling bird'. Cf. Kris, krk-, etc. etc. (quiri-). Skt. Cirikakah 'crow'; Alb. cirikoké (jackdaw; warbler', fr. an assimilated *quiriquaqua); Cz. cf. Cirikavka ‘partridge’ beside crkat ‘to chirp’ and Per. Ciryad ('cricket' insect), Li. kirkauti, inf. ‘to shriek’?
7683:korkos (korok-) (2) (demon, monster’. Cf. kark- Scythian cf. kórakos ‘demon’; Alb. cf. kark- in kark-zogé, usu. kaké-zogé *blindworm, slowworm'; Cz. krak *sea-monster'. (Skt. kar- kah, m. ‘crab’ is ambig. Cf. kark-)
7739:kostos, à, is (combings, fibre, grass, tress, bristle’. Cf. kes-, kos-, koso Gk. kóstos 'prickly-leaved spice-plant, burr or thistle’; kostai, pl. ʻa barbed fish'?); cf. Hes. kóstai, fpl. “barley? beside Gk. akosté, id.; kósta, npl. (perh. "linchpins"); Alb. kashtë ‘straw’; Ir. cuise ‘meadow-grass’; ON haddr ‘tress’ beside (e-gde) OE heorde ‘hards of flax’; Pol. cf. kost-rzewa ‘fescue’; Blg. koSC- riàva «timothy-grass'; Cz. cf. kostrbaty 'shag- gy’; koště, n. ‘broom for sweeping’; Li. cf. kastuvas ‘currycomb’. (LW in Lat. costus, costum ‘amōmum hirsutum, zedoary’, fr. Gk.). Here also prob. W. Cor. cos, f. ‘itch’
8539:Kakio (Kakos, us) “jump; jumper; jumping, agile, springy’. Cf. WP I, 334 Oss. sag ‘stag’; Gk. kekío (Doric: -à-) jump’; Li. Sóku, ti and $okiü, -éti “jump, dance’; cf. Sokus ‘agile, springy’; šoktas 'jumping-bar'
8552:Skt. sale, mp. ‘shine’; Cz. sálat, inf. ‘shine, glow’. An uncertain variant in Lat. caleó, ere ‘be hot! is isolated, but see next entry Kaləd- (Kalod-, Kald-) ‘summer, year. (A form limited to Indo-Íran. Lat. equivalent uncertain). Cf. WP I, 429 Skt. Sarád, f. ('autumn'; in pl. 'years); Av. saroóo, m. ‘year’; Oss. sárd ‘summer’; Per. sal ‘year’; Lydian sardis, id. Uncertainly to Lat. calidus (“hot', an adj. extn. of caleo. See Kàl-) (Kalmos, is, variant of type KImos, q. v. Am- big. in OCS slama, R solóma, H szalma; MHG halm, sm. ‘stalk, haulm'; Du. helm, f. ‘bentgrass’; OE healm as MHG) Kam- "do act, toil, languish’. Cf. kam- (1) and cf. WP I, 387. (Gk. ambig.) Skt. Samyami "be active, toil; Gk. (ambig.) kámno, adj: kmetós (Doric -a-) (make; toil; languish’. Two wds? See kam- (1)); Mod. Gk. kámo ‘do’; Lat. cf. (?) camillus, -a “serving youth or maid at sacrifice) beside (?) camena *poetry, song” (speculations in WH:LEW & EM DELL). (Li. kamuoti, v. ‘weary, bother’ indicates *kam-) Kamios, io “peg, crook, yoke-peg, pintle'. See next Skt. Sámyà, f., yuga-Samyám, n. *yoke-peg'; Arm. sami, -vo, -vov ‘pole, rudder, beam’; samik, pl. form “yoke-peg'; Gk. cf. kámax, -akos “stake, pole, shaft ' Kamos, us (1) “with crumpled or broken horn'. Cf. WP I, 386 and Kamios above Skt. śámah ‘hornless’; Lat. camus, camur & camurus ‘with bent horn’; cf. Gallo-Lat. camox ‘chamois’. (For Lat. camur see WP I, 349) Kamos (2) ‘a fish’ W cf. cem-yw, pl. -ywion, m. ‘male salmon’; G cf. Ham-butte ‘halibut: R som “silure, sheat’; Li. šamas, id.; Latv. sams, id.; Finn. LW cf. sampi ‘sturgeon’ (?) (Kan- (1), variant of type kan-, see kanið and cf. kon-. Gk. ambig. Av. san- ‘destroy’; Gk. kaíno, fut. kanó ‘kill’. Ambig. cf. kanið in view of Cz. kon-, etc.) Kan- (2) ‘sing, hum, bark, echo’. Cf. WP I, 351 Tokh. A. kan ‘melody, rhythm’; Gk. cf. ei-
8603:367. Cf. Káuio and káuo Arm. sor ( cave, cavity’. Cf. Arm. nor ‘new’ fr. *neuos; Cor ‘drip, flow’, fr. *steuos, cf. Skt. stavah (drip and W sew ‘juice’. SEM: AEI: § 57); Gk. kóos, m. ‘cavity’; cf. the synthe- tic elements of Gk. kóthon ‘goblet’; kórukos ‘pouch’; also cf. kafar “pit, stone-container in sling’; kúar, gs küatos “hole, eye of needle’, representing various grades of vowel; Lat. cavus, adj. and m. ‘hollow’; cavea ‘cave, den, cage’ beside covum ‘hollow blade of plow- share; heaven’; MIr. cúa, adj. “hollow? beside Ir. cuas, m. (&hollow', fr. *kouost-); Br. kéó, pl. kéwiu (*hollow, cave". But Br. kað, kav “hol- low? is a doublet fr. Lat. like Ir. cabha, id.); W cau, adj. and m., pl. ceuodd ‘hollow’; Cor. cow, pl. -yow, adj. & m., id.; long vowel in Sw. ho, m. ‘trough’; Li. $ovà “hole, hollow, chink’; reduced or zero-grade in OR suji, adj. ‘empty’; R cpds. suje- *vain-'; cf. possibly also Lat. va-cuus, va-civus («empty', fr. *gua-?? but cf. guakos)
8821:kos. (Variants: Kiakos, à, is) Skt. $akha “branch, limb’; Per. Sax “branch, Shoot, horn’; (Oss. xix, Dig. xexä “branch? beside ságoi *dungfork' suggest a doublet of type *qusak-, q.v. for xix, xexá); Arm. çax *heather; shrub; branch' beside caKan (Awge- rian); cak (Kerestedjian) ‘harrow’; OCS soxa ‘stem, stake’; R soxà ‘primitive plow’; Srb. soha ‘prop, stay, forked stick’. The Gothic form hōha ‘plow’; LW in Finn. kuokka ‘hoe’ is of uncertain phonology. Li. šakà ‘branch’; sake ‘fork: šaknis "root represent a variant of type *kak-
9193:Skt. Sunakah ‘pup’; Arm. 8nik, id.; Gk. kuni- kós, adj. *'doggish'; Ir. cf. conach, m. ‘rabies’; Li. Sunikas ‘cur, scoundrel
9303:Kuirokis, os, Kuirikis, os ‘a chirping creature, bird or insect Oss. cf. CirCir, s. (chirp'. Phon. obscure, but onomat.); Arm. cf. šršiwn (^whisper, rustle’, fr. *Kuir(i)kion); Gk. cf. a-sírakos (for *as- sírakos 'long-legged grasshopper’); Alb. cf. cirak, m. (an unnamed bird); OCS svricí and svrísti, m. “cricket insect; Pol. $wierszcz, id.; Slovene cf. (with long vowel) svirati, v. *pipe, whistle’; svirala (“flute, pipe’; Srb. évréim, v. ‘twitter’; Cz. cvrčet, inf. id.; cf. Slovene švrl- juga ‘tufted lark’. Of similar type are the fol- lowing: Latv. svire “swallow, curlew’ or sim. But cf. suir-); Li. Svirk$Ciu, -šti “whizz, whirr, twitter'. See next
9439:lak- (3) “lap up, gulp, gobble’. WP II, 380 Arm. lakem, id.; lak ‘porridge, pap’; W (long- gde) llawg, f. ‘gulp’; OCS loco, lokati ‘lap’; R inf. lokàt, id.; Cz. lokat, id.; lok, m. ‘gulp’; Li. laku, làkti “lap up’; Latv. loku, lakt, id. (pres. tense fr. *lank-); laka ‘swill, mash’. (The composition of Gk. ko-lax, gs -lakos ‘flatterer’ is uncertain)
9448:lakt-, lakot- “rag, scrap, tatter'. Cf. lak- (1) Skt. (dim. type) laktakah ‘rag’; Per. laxt, laxd ‘scrap’; Arm. lať ‘garment, cloth, rag! beside lati ‘scrap’; Li. lákatas ‘rag’: Latv. lakats "ker. chief; cf. also Li. lákStas ‘sheet of paper, quire’
9493:las- (1) “drip; drop’. Cf. lasik-, laK- Skt. cf. lasika ‘saliva’; lasakah (a *resinous tree); Gk. cf. larinós, adj. (fat, fattened', fr. *lasrino-); Lat. laser & lasur, gs -eris, m. ( ‘gum, benzoin’, w. dissimilated consonants, cf. miser); lar-idum, lardum, n. Card. lit. *drip- ping’ as in Eng.); larix, -icis, f. ("larch', lit. *dripping-tree? from resinous exudation). Pa-
=== IEC asan ===
348:aksios (2) “like, equivalent, due, true, valid, right’. WP I, 36. Cf. aksulos Skt. aCChab; Av. a$0; Tokh. cf. asan; Kanic (name of a king at Kültepe) Kunut-ahsu- (cf. $nótos below); Arm. a£; Gk. áxios; MIr. aice, adj. ‘worth’; R cf. -oSij (in xor-ošij *good^). For OCS oxolü see aksulos, and for OCS oxvy see esus
366:aKonos, à, is, io ‘spike, awn’. WP I, 30. Cf. aKnis Skt. asánih; Av. asan; Arm. cf. hesan ^whet- stone', appar, from a type *epi-aKon-; Gk. ákanos, ákaina, cf. also ákon; Lat. cf. agna (*ear of corn', phonology of dignus, segmen, etc); Go. ahana beside OHG agana; Latv. asns ‘bud’; cf. Finn. LW akana ‘husk, glume’
377:akón- ‘stone; whetstone’. WP 1, 30. Cf. akən-, Kön- Skt. asan; asánih; OPer. asa, asan-; Av. asa- nam, acc.; Per. san; Oss. sson, Dig. insoinä; Arm. cf. h-esan (*epi-akKon-?) ‘whetstone’; Gk. akóne, beside ákon, -ontos; Gaul. acaunum, pl. acona (-au- for -o-) *whetstone?
2135:deKo, io ‘find, get; deem, judge’. WP I, 783. Cf. deKs- Av. das- ‘possess’; dasan ‘possession’; Tokh. A täk- ‘decide, judge’; Myc. cf. dekasato (:Gk. edæxato); Gk. dékomai, beside dektós ‘agreeable’; Lat. decet; Umb. Get “is allowed’; Osc. cf. deketasis (title of a judge); cf. dek- manni(s) ‘paying member of a club’; MHG cf. ge-zéchen, OHG gi-zehon ‘arrange’; OE teohhian, v. *determine, judge' beside tióian (for tigóian *bestow"); OCS dešọ, desiti ‘get, find’. A possible long-gde occurs in Skt. dāśāmi, dāśmi & da$nómi ‘worship; bestow’. See next
3678:esános (sanos) “good, due, right, proper, Cf. sános, esnt-; esont-, snt-, sont- (all with radical: *es-, s- "be Hitt. cf. asanc, neut. asan 'true'; Lat. sanus (* good; sound"), cf. san-cio, -cire (*establish, enact’. Cf. cio, cire ‘cal’ and sense of G gut-heissen); cf. also sanates (‘reinstated rebels’, fr. san- *good" — Fest.); W iawn (just, right, proper’, fr. esàn-); Br. écen, d: OHG suona “judgment; reconciliation; suonen ‘judge’; cf. G Sübne and ver-sóhnen; OS sonian, id.; OCS sanü ‘dignity’ beside sanitü (holy: OS gi-sonid). (For OE sona *forth- with’: W hawn ‘brisk’ see són-)
3702:esmnos (esimnos, esniu-) “fine, thin”. Variant of emnos (?), q. v. (A Skt. form of type *asanáh, Prakrit (alleged) sagha implies a prototype *esmnos, found in Romani sano “thin, fine. Gk. eānós, heianós id. are apparently infl. by hénnümi; Cz. Slovak jemny, id. equally indicates a pro- totype emno-, q. v. Semantically related is Skt. anuh, id.)
8573:Kas- (1), (Kasnos) “grey, white; grey or white creature or plant'. WP I, 357 Lat. canus ‘hoary, frosted, white-haired'; Osc. cf. casnar, m. old man'; Gk. cf. also kolo- kasía *hoar-wort'; OHG hasan, adj. ‘grey’ be- side haso, m. ‘hare’; OE hasu, heasu “grey, ashen’ beside hara, wm. ‘hare’; paroxytonic in E haze and in MHG heswe ‘pale’ (LW in Fr. háve, id.), but oxytonic in Scots har “low mist, suspended mist’; ON boss, acc. hosvan, adj. “grey, of wolf; G cf. Hasel, Hásel 'grayling'; Finn. LW harjus,id. Assimilated consonants in Skt. $a$áh “hare? owing to association w. Sasami “jump”; OPr. sasins ‘hare’. Cf. W cei- nach ‘hare’ if for *Kasinaks-
12531:nom as censa ‘due, tithe’ fr. *cesna. The Alb. vowel is ambig.); OHG cf. faso, wm., fasa, wf. obl: fasan- as Gk.; cf. (variant) OCS pasmo, R pàsmo (and com. Sl.) "bank skein’; (LW in Finn. pasma, id. Wrongly associated w. pás ‘belt’ in Cz.); Li. pósmas, id. (LW)
19882:ueikot- (uoiKot-), cf. ueik- Skt. vesatvam, n. ‘tenancy, vassalage' beside (vrddhi) vai$yata, f. “peasant status, peasan- try’; OS wihetha, f. ‘sacramental vessels’
20273:uidh- (1) “counter-, against; opposed; oppo- sition’. Cf. ui- and dhe- Skt. cf. cpds. -vidhami, v. (pay! — esp. 'hom- age’) beside vindhé, mp. ‘be bereft of; Hom. Gk.? hus, (2) ‘thrust, opposition, effort"; Hes. íthur, n. ‘brake’; (Hom. phr. pasan an íthun “with all one's might, but initial ambig. Cf. suidh-); Go. cf. in-widan, v. ‘deny’; OS cf. in-wid, n. (o-st.) ‘mischief; OE in-wid(d), n. id.; OHG in-wit, n. ‘trick’; ON vió ‘against
```


## [2026-09-04T19:10:54.187Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- POK files ---\"; ls -la POK_*.txt\necho \"--- search ak- root ---\"\ngrep -n \"ak̑-\\|ak'-\\|aḱ-\" POK_full.txt | head -20\necho \"--- search kēi ---\"\ngrep -n \"kē(i)\\|kēi-\\|schärfen\" POK_full.txt | head -20"
}
```


### [2026-09-04T19:10:54.278Z] TOOL RESULT

```
--- POK files ---
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
--- search ak- root ---
--- search kēi ---
```


## [2026-09-04T19:10:54.983Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC page markers around line 344 and 377 ===\"\nsed -n '330,395p' IEC.txt"
}
```


### [2026-09-04T19:10:55.033Z] TOOL RESULT

```
=== IEC page markers around line 344 and 377 ===
45
type; (2) durative-freq. of verb type; (3) de- nominative extn. of verb type (1) Gk. outáo, geláo, eráo, damáo, skirtáo; Lat. crepo, seco, tono, veto, domo, sono, frico, all with inf. in -are, pf. in -u1; OS fol- gon; OHG tholon, holon and halon, volgon beside -en in all forms; OCS prijajo (beside prijo, inf. prijati: Skt. prinami: Go. frijon, see below: priià-, vrüzajo, vrükajo, tüpajo; Li. plasnóju, inf.-óti, riaumóju, pléscioju; Latv. bokaju, at. bojaju; (2) sedare, ducare, placare; Go. miton (mitan), hvarbon (hvairban); OCS tékajo, -ati (eko, testi); OCz. vídaju, -ati (vizu, viděti); Li. pa-jaújoju, -oti(jauti) Latv. plūkāju, -āt (plükt); (3) Gk. timáo (timé), ereunáo; Lat. fumare; OHG zilon (:Go. tilon) (zil), faston (fasta), fülön (fül); OCS dymajo, -ati (Lat. fümare)(dymü), düzdajo (düZzdi), kosajo (kosü); Li. ráudoju, -oti (ráuda), vo- Dom (vðlas). See below: *siiā- (sia), skiia-, neuà-, dhuma-, etc.
aios, -es- “metal, bronze, ore. WP I, 4 Skt. áyas; Av. ayáh-; Lat. aes; Umb. ahes- (w. ‘false h); Go. aiz; ON eir; MHG er. (Note: J. Pokorny and others refer this word to Alasia (Ayasia), an ancient name of Cyprus)
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
aKonos, à, is, io ‘spike, awn’. WP I, 30. Cf. aKnis Skt. asánih; Av. asan; Arm. cf. hesan ^whet- stone', appar, from a type *epi-aKon-; Gk. ákanos, ákaina, cf. also ákon; Lat. cf. agna (*ear of corn', phonology of dignus, segmen, etc); Go. ahana beside OHG agana; Latv. asns ‘bud’; cf. Finn. LW akana ‘husk, glume’
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
aksis, -ó(n) ‘axle, axis, pivot. WP I, 37 Skt. áksah; Myc. akosone (*aksones, pl.); Gk. áxon; Lat. axis, g.p. axium (fLat. axis, as also Gk. áxon are from ago)” — Ainsworth 1736); MIr. ais; OE eax; OHG ahsa; Du. as; LG ass, pl. en OCS ost Li. ašis, gp. aSiü, m. & f.; Latv. ass, gs. ass, gp. asu ‘axle’
āKsos (? oKsos) ‘keen, sharp, clear; keen- ness, etc? W awch ‘edge, keenness’; Cz. jas ‘clarity’; cf. the synthetic OCS cpd. jastrebü ‘hawk’, with part of the semantics of Lat. accipiter, id. The Lat. form ascia and It. azza indicate a short vowel. `
akstin-, akstin- ‘point, prickle, dart, shaft, spike, pike, spit’. WP H, 338 Tokh. asce “head, beginning’; Gk. aktin; MIr. aittenn, Ir. aiteann ‘furze’, Gallo-Lat. atinia ‘ulmus gallica; OBr. ethin “rushes'; MW eithyn 'trampium'; W eithin, pl. aith ‘furze’;
' eithen ‘point, prickle’; Cor. eythynen ‘furze’;
30
35
40
45
```


## [2026-09-04T19:11:04.613Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -c 1500 POK_full.txt; echo; echo \"---01---\"; head -c 800 POK_01.txt"
}
```


### [2026-09-04T19:11:04.668Z] TOOL RESULT

```
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 




Anatolian 


Ang. 




Anglian 


AngN 




Anglo-Norman 


Aram.- 


■Iran 


Aramaeo-lranian 


Ash. 




Ashkun 


Ass. 




Assyrian 


Auk. 




Aukshtaitian 


Bactr. 




Bactrian 


Bel. 




Belorussian 


Br. 




British 


Bret. 




Breton 


BVan. 




Bas-Vannetais 


CCI. 




Continental Celtic 


Chak. 




Chakavian 


Chor. 




Chorasmian 


Clb. 




Celtiberian 


Class. 


Skt. 


Classical Sanskrit 


Co. 




Cornish 


Corn. 




Cornouillais 


Dae. 




Dacian 


Dan. 




Danish 


Dard. 




Dardic 


Dzuk. 




Dzukian 


EBI. 




East Baltic 


EGm. 




East Germanic 


EGmRun. 


East-Germanic Runic 


El. 




Elymian 


Elam. 




Elamite 


Elam.- 


Iran. 


Elamo-lranian 



EMoBret. 


Early Modern Breton 


EMolr. 


Early Modern Irish 


EMoW 


Early Modern Welsh 


ESI. 


East Slavic 


Faer. 


Faeroese 


FriRun. 


Frisian Runic 


Gal. 


Galindian 


Gallo-Gk. 


Gallo-Gk. (in Gk. authors) 


Gallo-Lat. 


Gallo-Latin (in Lat. authors) 


Gaul. 


Gaulish 


GaulG 


Gaulish in Greek letters 


GaulL 


Gaulish in Lat. letters 


Go. 


Gothic 


Gr. 


Greek 


Hebr. 


Hebrew 


Hell. 


Hellenistic 


Hi. 


Hindi 


HVan. 


Haut-Vannetais 


IE 


Indo-European 


Mr. 


Indo-lranian 


InsCI. 


Insular Celtic 


Iran. 


Iranian 
---01---
)H
JULIUS  POKORNY
INDOGEEMAmSCHES
ETYMOLOGISCHES
WÖRTERBUCH
I.  BAND
FRANCKE  VERLAG  BERN UND  MÜNCHEN
A.  Francke  AG  Verlag  Bern  •   1959
Alle  Rechte  vorbehalten
Satz  und  Druck:  Adolf  Holzhausens  Nfg.,  Wien
INDOGERMANISCHES   ETYMOLOGISCHES   WÖRTERBUCH
ä  Ausruf  der  Empfindung,  oft  neugeschaffen.
Ai.  ä  Ausruf  der  Besinnung-;
gr.  ä  Ausruf  des  Unwillens,  Schmerzes,  Erstaunens;  Ic,  da  Ausruf  der Verwunderung  und  Klage;  dazu  ä^etv  ^ächzen*";
lat.  äj  äh  Ausruf  des  Schmerzes^  des  Unwillens;
lit.  äj  aä  Ausruf  der  Verwunderung^  des  Tadels  oder  Spottes^,  ä  Aus- ruf der  verwunderten  Frage  (lauter  Neuschöpfungen);
got.  ö  Ausruf  des  Unwillens^  der  Bewunderung;  ahd.  ö  Ausruf  des Schmerzes;  mhd.  ö  Ausruf
```


## [2026-09-04T19:11:06.009Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"whetstone\\|Wetzstein\" POK_full.txt | head -20; echo \"=== count ff ===\"; python3 -c \"\nd=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nprint(len(d.split('\\f')))\nprint(repr(d[:300]))\n\""
}
```


### [2026-09-04T19:11:08.780Z] TOOL RESULT

```
3260:ocoluin, ncymr. hogalen. Middle Breton hygo(u)len, nbret. higolenn' whetstone ' (with the 
3301:ose/oRm. "whetstone', Czech os/nat "awn'. 
3606:deficiency, loss' see WH. I 9), OKOvn ' whetstone ', qkcjov, - ovioq, ' spear ' (for older qkoov, 
10294:Material: Cretan cpaypoq " whetstone ', OKovn, cpo^oc; " pointy heads, pointedheads, 
15555:russ. brus{Qev\. brusa; mostly brusok) "grindstone, whetstone'; russ. etc brusnfka^ 
15821:Old Icelandic brun'edge', whereof it'/yna 'whet', it*/]?/?/ "whetstone'; Old English Middle 
30431:presumably Lithuanian gliaumas^ smooth diminution of the whetstone ', gliaumus^ 
36507:glastu, glasttC caress'. Old Prussian ^/os/o 'whetstone'; 
36522:Lithuanian galandu, gal^sti^ sharpen, carve, cut ', Latvian ^aA/Od/s 'whetstone'. Old 
36530:Maybe alb. glemb^ sharp thorn (smooth, sharp) ' : Old Prussian ^/os/o "whetstone'. 
46582:Old Indie ksnauti^ trails, races, rubs ', ksnotra-n. 'grindstone, whetstone', participle 
51042:whetstone, touchstone, yardstick, criterion ' (= npers. s5/7 'whetstone'); perhaps also Old 
51059:Irish cath); cos, C0//5 "whetstone', also cotes, cautesi. PI. " pointed rock, reef {-au- 
51064:Old Icelandic heini. "whetstone'. Old English han^ boundary stone ', engl. hone 
51065:"whetstone' ( *Rai-n- : Avestan saeni-); Middle High German har^ tools to sharpen the 
54814:Old Icelandic sITkr^ smooth ', s//7r/s/e//7/7 "grindstone, whetstone'. Old High German 
85132:m. "grindstone, whetstone'; Lithuanian /e/r/77e"wellspring, river', //o/ra " estuary'; Latvian 
86053://^/o/ss "whetstone', Latvian truots ds. (Trautmann 326, VasmerS, 133); 
=== count ff ===
1
'List of language abbreviations in tlie lED \n\n\n\nAbbreviation Language name \n\n\nAeq. \n\n\n\n\nAequian \n\n\nAkk. \n\n\n\n\nAkkadian \n\n\nAlan. \n\n\n\n\nAlanian (=Old Ossetic) \n\n\nAlb. \n\n\n\n\nAlbanian \n\n\nAnat. \n\n\n\n\nAnatolian \n\n\nAng. \n\n\n\n\nAnglian \n\n\nAngN \n\n\n\n\nAnglo-Norman \n\n\nAram.- \n\n\n■Iran \n\n\nAramaeo-lranian \n\n\nAsh. \n\n\n\n\nAs'
```


## [2026-09-04T19:11:13.795Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '51010,51090p' POK_full.txt"
}
```


### [2026-09-04T19:11:13.841Z] TOOL RESULT

```
German /7e/s// "violent, forcible '. 

References: WP. I 364 f.; belongs to Rei-gh-, see below. 
Page(s): 542 

Root / lemma: Rei-gh- 
Meaning: quick, hasty 
Material: Old Indie sFghra-^ash, hasty, quick, fast'; 

Old English hTgian^ stretch, make tense, stretch out, spread out, distend, extend, 
hasten, make haste, be in haste, hurry, be quick, bear upon, press upon, lean, support 
oneself, engl. /7/e 'hurry', geminated Norwegian hikka^ sob ', Old Swedish hikka^ gasp, 
have the hiccups ' (onomatopoeic words?); 

russ. sigatb, s/gnutb ' spnng' , wruss. s/gac, s/gnuc' walk, make big steps '; wherefore 
also russ. s/g'a kind offish', as Sa/mto salid, so that Lithuanian sykiseic. and Old Norse 
s/Ttr maybe are borrowed from Russ.. 

References: WP. I 363, Wissmann Nom. postverb. 174, Specht Indo Germanic Dekl. 249; 
See also: belongs to Rei-b'^-, see above. 
Page(s): 542-543 

Root / lemma: Re(i)- : Rd(i)- : RsO)- 

Meaning: to sharpen, whet 

Note: probably further formations from a^- 'sharp' (see 18 ff.) 

Material: Old Indie si-sa-ti{si-sT-t§), sy-at/" sharpens, whets ', participle s/ta- ' sharpened, 

pointed ' (= Latin catus, Old Irish cath), sata- ds., sana- m. (with Middle Indie /7for n) ' 

whetstone, touchstone, yardstick, criterion ' (= npers. s5/7 'whetstone'); perhaps also Old 

Indie S//5 'stone, rock' ( *ka-la)\ 



Avestan 5ae/7/-"cusp, peak, treetop, sharp' (npers. sayad'reM) = Old Norse he/rr, 

Armenian s^r'sharp' {*Rd-ro-), sre/T? "sharpen', sur. Gen. sroy 'sword, knife', sair 
"cutting edge' {*Re-ri-), compound s5//'a^//'"cutting edge', therefrom *sardrem, sadrem^ 
irritate, annoy, itch, anger, tease; arouse, excite, set in motion '; perhaps also sal. Gen. sail 
"flagstone, anvil ' ( *Ra-li-, compare above Old Indie sila); 

gr. Kwvoq m. " cone, a pine-cone, the cone of a helmet, top ' (= Old Indie sana-), 
therefrom kwveiov " hemlock, Conium maculatum ' (after the leaves); 

Latin ca/i/5 (after Varro Sabine) "acutus, sharp witted, shrewd' (= Old Indie si-ta-. Old 
Irish cath); cos, C0//5 "whetstone', also cotes, cautesi. PI. " pointed rock, reef {-au- 
hyperurbanism); catanus' cedar juniper ' is perhaps gall, loanword; 

Old Irish cath^mse' (= Latin catus. Old Indie si-ta-); 

Old Icelandic heini. "whetstone'. Old English han^ boundary stone ', engl. hone 
"whetstone' ( *Rai-n- : Avestan saeni-); Middle High German har^ tools to sharpen the 
scythe ' ( *Re-r-), Middle Low German haren " sharpen, be sharp '. 

References: WP. I 454 f., WH. 1181, 183 f., 190 f. 
Page(s): 541-542 



Root / lemma: Reko- 

Meaning: green grass, green fodder 

Material: Old Indie saka-m. n. " edible herb, vegetables '; 

Lithuanian seRas^ freshly mowed grass, green fodder", Latvian seRs6s., Old Prussian 
schokis "grass' (these at first from *sjaRas, -ya-from -e-1); 

Old Icelandic hat " bumper crop, byproduct' (probably from Germanic *hehdn-). 

References: WP. I 381. 
Page(s): 544 

Root / lemma: Re-ro- 
Meaning: a kind of colour
```


## [2026-09-04T19:11:34.118Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK ak- root ===\"\ngrep -n \"Root / lemma: aR-\\|Root / lemma: aR\" POK_full.txt | head -20\necho \"=== page 18 ===\"\ngrep -n \"^Page(s): 18\\b\\|^Page(s): 18-\\|Page(s): 18 \" POK_full.txt | head"
}
```


### [2026-09-04T19:11:34.184Z] TOOL RESULT

```
=== POK ak- root ===
3242:Root / lemma: aR-, ok- {*hek-) 
3768:Root / lemma: aR-1, aRo- {*hek-) 
3776:From Root / lemma: aR-, oR- {* hek'^-): sharp; stone' derived Root/ lemma: aR-1, aRo- 
3792:Root / lemma: aRru 
=== page 18 ===
3766:Page(s): 18-22
```


## [2026-09-04T19:11:35.754Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT saeni ===\"\ngrep -n \"saēni\\|saeni\\|sāni\" BRT.txt | head -20\necho \"=== BRT asan ===\"\ngrep -n \"asānam\\|asan-\\|asāna\" BRT.txt | head -20\necho \"=== SNS ===\"\ngrep -n -i \"afsān\\|afsan\\|sān\\b\\|asān\" SNS.txt | head -20"
}
```


### [2026-09-04T19:11:35.834Z] TOOL RESULT

```
=== BRT saeni ===
25797:•  j.  saeni.kaofa-  Adj.  '(mit  spitzem,  d.  i.) gerade  aufgerichtetem,  steifem  Höcker' '\ vom  Kamel:  uäräaha  .  .  'Ja  YLr7. 13; —  u/tranqm  .  .  'fanqm  V.  22. 3.
=== BRT asan ===
4698:\)amm  Y.$4.2,  G,  j.6; — yä  {ar?ävi) 'vaiti fratalaili  Y.  Ö5. 3 ;  Yt.  5. 1 5 ;  —  a^tn  vatau- hlm  .  .  hrpsailTm  'vattTm  Y.  3. 14;  Yt /J. I,  7;  —  drvaspqm  . .  'vaitlm  YL9.2;  — fravaiayö  .  .  yä  'vaifli  Yt  13.  29;  —  at töi  atrjm  . .  *asXsttin  'vanhm  Y.j^4;  — tiiirim  .  .  'vant?m  YtÄ4;  —  vatianttm 'vant»m  Yt  21.  i;  —  °vatS  amai  'vatÖ virp^raynäi  'vat^yO.  »rütyi  'vai'iya aiöii  'vai^ya  astdil  'vaüyä  paurvatälo 'vai'i'yB  uparatälö  'va^byä  yazatoAbyö  Vr. g.i,.  b)  sonst;  uströ . ,  b)r?zB  "vä  Yt i.^.  1 2 ;  —  srlra  urusta  'vaiti  (VSf.)  .  . UfTaireY.it^.iB,Vyt22; — srayarfhö  vouru- ka?ahe  'vatö  Yt.<S.46;  —  vasnm..  zaröil ayanhö  frahixt»m  'vatö  \L  10.96;  —  'vat iimäfum  Y.  57. 10;  —  ptiüm . .  yim  aiwatö 'vantim  Vyt.^;  —  'vaitlm  sitiqin  dävöi (sd.)  dr»gvasa  Y.  44. 14.  —  IstJm  . .  pouru.- sarioam  'vaitlm  Y.  65. 1 1 ;  —  hazö  "vat  Y. jj^.  iz;  —  yahmi  maza  'va  (NSn.l')J' '  iiiäälpm  Yt  10. 64  (?) ;  —  *°vata  vaca  F.3  e. AbleiL  —  ai.  dmm-ant-  Adj.;  vgl.  mp.  (PS.) amäz-nnd.  —  ')  %  jg4.  —  •)  Zur  Zusammen- Stellung  von  amai'aaf-  mit  ^'/ri^ravan ,  viri- %rasan-  s.  'amn-  2.-3)  Wenn  richtig,  wohl Neubildung  lum  NSm.  'va  nach  der  n-Dekt.
5024:•  j.  ava.Jasan-  Adj.  "her-,  hinzukommend, gehend  zu  — '  (mit  a  und  Akk):  yasca.. frS.vS  iüsa  (NS.)  haca  daiähaot  °sa  dahyUm ä  Yt/.i?.
5704:Ableit  —  Vll.  Komp.  asan-Jr'garta.  'Stein- höhlen  habend,  bewohnend',  also  eig.  Volks- nanie,  ai.  gärla-  m.  (wozu  MMülles  SBE.  32. 433).  —  ->  JusTi  GIrPh.  3.  455-
5721:Eiß.  Bed.?  Wohl  Komp.  mit  asan-i\.  —  Vgl.  l asa-iaiia-.  —  O  Gaui  Unsicheres  bei  Jusxl . NB.  42,  HoRN  NpEt   165.  '
5724:•  j-t  E-  (.  P-)  asan-iaj«-,  j.,  p.  asman-  m." i)  'Stein':  *ja«s(alsAP.)  äi/i{sd.)  maya  äiti darSii"V.g.  11;  —  'sSnaShia'^ ..  vtHiaeh-a' . .  tBiuxha  (sd.)  V,  6. 5 1,  a)  als  Amulet: °samm  *siyaire.ci^rim  (sd.)  abars  *aAurö.- puirS  (sd.)  Yl;4.59-  b)  als  Waffe, 'Schleuderstein,  Steingeschoss':  Uavasca  . . •sanas(a  . .  (NP.)  fraäaxlaitya  V.  Z7.9;  — karjtS  .  .  vazrö .  .  'sänS  atymSJütä  Yt.  JJ. 72;  /.18;  —  jainti  mqm  ahuna  vairya avavata  snai^isa  ya'^a  'sma  iatS.masa (sd.)  Yt/7.20;  —  'sanS  (als  AP.)  tasia drazimnS  katä-masatiks  Aynti  V,  117.43); —  yahmai  .  .  aurvan/a  *yuxta  vJsa %an/asante  (sd.)  .  .  asUnas/a  (als  AP.) vispeMvia  "dem  .  .  die  Renner  am  ge- schirrten Wagen   ziehen  -  .  und  die  all-
5907:•  j.,  p.  asman-  m.:  s.  unter  asan-.
10024:mit  ava  'hinkommen,  hingehen  zu  -'; a)  mit  Akk.:  ava  tä  aiiya  maya  äia(sd.) Jasöit  V.^,  31;  12,  32;  —  urraraiiqm (stattAkk.)..<ir'a.y(ij,iA/V.((j.i8.  b)mit hyat  m5i  vaahius  AazS  jimat  ma'iaahd  Lok. :  yim  yaz^nte  daitihupatayS  ^anzahi Y,4y.4;  — jamy,V  tS  vat?haot  vavho^  ava. Jan ritc^  Yt.  lO.  S.  S.  noch  m-a.- Y.5P.31;  31';  —   «V  ahmai  jasai  Syap-  jasan-.
10145:dem,  was  das  Rind  liefert;  i) 'Fell,  Haut':  ahurai  a  mS  urva  'Suscit  azya  Y.2g. mä  .  ,  yaia  *'aof  drafsö  (sd.)  .  .  Y.  /o.  1  5  '3>.  a)  neben  'gaya-  (sd.):  nimS  °Sus 14.  2)Tleisch':  pars xh'isca{sd.)  5zBi-\  mmö  gayehe  Y.68.  22;  Vr.  z/.  a;  —  fra tisca'jus  matY.13.%9,;  —  nöii  payS  fsula  .vasayS  ..  yqmca  asnö  ..  spu  ..  zsmS (sd.)  nSii  'Jul  .  .  paiti.baire  V.  7.  77;  —  I .  .  un-arayd  .  .  -Jus  .  .  gayeke  Vl  13. kat  na  .  .  -Jus'  ataifya  (sd.)    aslryeiti  N. '  86.  a)    GS.    mit  tasan-  m.  (sd.,   auch
12160:.  j.,  g.  tasan-  m.  'Büdner,  Schöpfer',  nur'*  g-  *^s  ä  adv.-artige  Verb,  'auf  solche
13692:äsnaila  zbayantsi  'ratca  Yt.  77.  * ;  ■ — ■  nara . .  ya  nasaum  avaJiUta  'ire  asahi  rasan- hqm  (sd.)  V.Ä'.g?;  YX.i4.^l\  —  Wp^r- sahyü  .  .  ari'tii  'raiy'''  paragmatä  "des Persers  Speer  ist  fernhin  gekommen"  D. ff.  4;  —  mit  Abi:  agibyS  'in  voha  as mand  (sd.)  Y.J4.  8.  a)  |  in  Verbindung mit  apiy  (sd.):  ahyäyä  bümiya  'raiapiy  D. 6.3;  X.I.3  (wo  'raiy  apty): —  mit  Aacä und  Abi.:  pSrs<^  marliytr  *'rayapiy''> hacä  pärsS^  kamaram  paliyajatä  D.  6. 4.  2)  Abis,  'von   fem;  fem;    femhin,
16493:•  j.  baevar«.spasan-  Adj.  'der  zehn- tausend Späher,  Wächter  hat',  von  Mikra: mi%rs  .  .  yS  'sanS  (NS,)"'  Yt  to.  24;  — mi^rB  .  .  yS  'sänö  (NS.)"  Yt  10.  60.
20116:•  j,  'masan-  n.  'Grösse,  Eedeutendheit': "sanaca  (IS.)  vatvhanaca  srayanaca  (sd.) V.J.  22,  Yt/p.  sS,  K.i.\z,  H.J.6,  2.  II, *P.  42.  a)  Plur. 'Glosstaten':  li^ra  vö buyäryS  'sänh  (NP.)''  H%ra  vS  zavanif.- sav^(s±)  Ny.j.ii.
20118:•  j.  'masan-  Adj.  'gross,  bedeutend':^ffi>,*? .  ,  'sä/ias^ä  (GS.)  vauhänasiä  srayanascJ (sd.)  carpktnmahi  Y.  3Ä4.
20119:Ableit  aus  'masan-  n.,  durch  Ilaplol.  auä *masanaH-(i)'i;  man  beachte  das  ä  des  GS. and  S  403  I-  —  Pü.:  masiA  'Grösse'. —  ■)  S. auch  ai.  varmirt-,  nämin-  u.  a.  (bei  Wh.  Gr.' S  rijoi);  vll.  hat  sich  der  Typus  schon  im Arischen  ausgebildet
26885:•  j.  spasan-  Adj.  Iiinspähend  (auf  — )';
26999:•  j.  spantö.frasan-  Adj.  'heilige  Fragen stellend,    heilige    Unterredung    führend':
27725:—  ztün-a  '.  ai.  Aiman ,  gr.  x"/^^'  =*^  j-  aln-e  \ ai.  aJttiaa,  gr.  äx/iüit ;  s.  noch  irayan-,  masan-. Dazu  JScHUiDT  Kritik  87.
=== SNS ===
2699:J^'j^^-^^^jJjK^xib^. - . U* UI : afsannj^o- 
4838:•f/lY ^ ( afsan 
33843:afsan 18/19
```


## [2026-09-04T19:11:42.525Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3242,3260p;3760,3800p' POK_full.txt"
}
```


### [2026-09-04T19:11:42.574Z] TOOL RESULT

```
Root / lemma: aR-, ok- {*hek-) 
Meaning: "sharp; stone' 
Material: 1. e/o-and a-St 

Npers. a5(lengthened-grade form) "millstone, grindstone'; gr. OKn "point', lengthened- 
grade form Ionian nKr| aKWKn, £ni5opaTi(;, nK^n Hes., redupl. aKOJKn " point, edge ' (as 
aywyn : ayw); after Kretschmer KZ. 33, 567 and Schwyzer Gr. Gr. I 348 belongs qkouu) 
"hears' as *aK-ou(;- "having sharp ear' here, see, however, 1. keu-; alb. a//7e/e "sharp, 
sour', [common alb. -k> -//?]. 

Latin ace/ie "sharp, cutting, keen. Hence, to taste, biting; to touch, sharp; of sounds, shrill; 
of smells, penetrating; of sight, keen; of emotions, painful; of understanding, quick, 
vigorous, energetic', ac/c/us' sour, acid, tart ', acetum' vinegar'; 

Maybe alb. acarlrost, sharp steel' : Romanian acar' signalman, pointman, switchman, 
pin cushion '. 

with ambr. con voc ar v/7/n 'sharpen the millstone ', cymr. hog/' sharpen', acymr. 
ocoluin, ncymr. hogalen. Middle Breton hygo(u)len, nbret. higolenn' whetstone ' (with the 

See also: S. under *oR-t6u^e\Q\\{\ actually " both points of the hands (without thumb) '. 

zero grades ^- stuck probably in stems kemen-, kernel-, komen-^ stone, skies ', komor- 
" stone hammer ', Rei-, koi-, kd/- " sharpen, whet ', Ru-^ sharp, spit, spear '. 

Page(s): 18-22 

Root / lemma: aR-1, aRo- {*hek-) 



Meaning: to eat' 

Note: 

From Root / lemma: aR-, oR- {* hek'^-): sharp; stone' derived Root/ lemma: aR-1, aRo- 

{*hek-): 'to eat' 

Material: Old Indie as/7a// (inserted Inf. as/'-tum etc.) 'eats, consumes', asanamu. "food', 
asna-h ^ greedy' , lengthened grade asayat/" aWows to dine', prafar-asa-h ^breakiasV; 
Avestan kahrk-asa "chicken eater = vulture' etc.; 

gr. aKuAo(;f. "acorn' (as "food', compare formally Old Indie asi/-5a-/7 "greedy'), cxkoKoq, 
"bite'; 

Old Norse agnn. "bait for fish' ( *aka-n6-), aeja "allow to graze' ( *ahjan). 

References: WP. I 112 f., WH. I 210 f. 
Page(s): 1 8 

Root / lemma: aRru 

Meaning: tear' 

Material: Ved. asruu., later also asram'tear', Avestan asru-n., Lithuanian asara' and 

asarat, Tocharian A akarP\. akrunt ds., compare Old Indie asrayami, Lithuanian asaroju 

"cries'. The relationship to Indo Germanic *dakru'tear' is unsettled, compare Meillet BSL.
```


## [2026-09-04T19:11:44.258Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS page 18 region ===\"\ngrep -n \"\\[pdf page 1[5-9]\\]\\|\\[pdf page 2[0-5]\\]\" SNS_pages.txt | head\necho \"--- afsan context ---\"\nsed -n '4820,4850p' SNS.txt\necho \"=== KNT 173 ===\"\ngrep -n \"asan\\|asa-\\|whetstone\" KNT.txt | head -20"
}
```


### [2026-09-04T19:11:44.332Z] TOOL RESULT

```
=== SNS page 18 region ===
--- afsan context ---
{GNPE. 264) anhu-, ahQ- : t- .^fc<w«£<j*T 5h5g 

•r/To^ 

.>ISjS#» , l&,,*xc±i :xvabar/xv a par: \j»v* 

Ut^.l877)hvapah? :ji( -ra o T ^» xvgpara- : fc. 

.^jB^jix^wari : L {Mir. Man. 11,58) xw'br ijiU 

•TY— TMl— YY/YT ^ .(^jo-y^) 
-tfb* , L^.*j.ys:x v abar Shrraazd: -**£»?«?>*>'*• 

-J^= hu jl ■>!*(*« «>> wU-— Uj:hu-afrin-tar : JfV^aj'K' 
. ^yJ.-iiu c^i-i Lu -tar+ Uj .jirfb- .o^U:5frIn+ v> *. 

: ^ji^o*:^) .•a#;I > * .*j > -b :an-afsudag: 3r»VO*V 

•f/lY ^ ( afsan 

.^tJjtiS «wo.>*:hQxt: >0*v 



61 



Ui^^Li ^l.;l, 


=== KNT 173 ===
339:I. Arsacid Pahlavi was the official language of the Arsacid dynasty of Parthia, which ruled from 250 в.с. to 226 a.p.; it did not die out with the dynasty. It is represented in some bilingual in- scriptions alongside the Sasanian Pahlavi, where it is often called Chaldaeo-Pahlavi or Parthian; by the parchment manuscripts of Auroman; and by certain Manichaean texts from Turfan (IV). It is also called Northwest Pahlavi, and appar- ently was developed from a dialect which was almost or quite identical with that of Media.
340:II. The Sasanian or Southwest Pahlavi was the official language of the Sasanian dynasty, which ruled from 226 А.р. until the Mohammedan conquest in 652. It is known from some rock- inscriptions of the kings in the general region of Persepolis, datable in the 3d and 4th centuries, some being accompanied by a translation into Arsacid Pahlavi or even by a second translation into Greek; from some texts on Egyptian papyri, of about the 8th century; from many religious texts preserved by the Zoroastrians (III); and from some of the Manichaean texts found at Turfan. In mscriptional form it can be observed in legends on coins, seals, and gems, until near the end of the 7th century. It appears to have developed from Old Persian or from a very similar dialect.
341:III. The ‘Book-Pahlavi’ includes the writings preserved by the Zoroastrians of Persia and India, forming a very considerable body of literature divisible into (1) translations of parts of the Avesta, with commentary, (2) texts on other religious subjects, (д) texts on other than religious topics. They represent both Sasanian and Arsa- cid Pahlavi. They are written in an alphabet derived from that of Aramaic, and, like all the early Pahlavi writings and inscriptions, contain an extremely high percentage of Semitic words; but many of these were to be read with the Ira- nian equivalents, even as we write 10 est and say ‘that is’, viz. and say ‘namely’.
343:dialects, including the Arsacid and the Sasanian types, the Sogdian (known also from a trilingual inscription of Kara-Balgassün), and a dialect known as ‘Eastern Iranian’, perhaps a derivative of northeastern Scythian, in which there are texts of the Buddhists of Khotan. The notable peculiarity of these Turfan texts is that they are written in relatively pure Iranian, without the Semitic writings for the words which are to be spoken by the Тташап equivalent.
373:s in asa- from Ё if it means ‘stone’. Sikayawati$, a Median fortress, with s- from
397:asan- ‘stone’, with s from Ё.
588:arasam impf. of pres. stem rasa- (-sa- from *-ske-),
717:taxsacd. in borrowed tacaram DPa 6, ХР], and dacaram DSd 3. (b) c/& in late inscriptions: haga A'Sde 4, for the usual hacá. Xsayarcahyd A'Sa 2 bis, for XSayarsa ete. {ustalcandm A’Sc 5f, for ustasanàm A?Pa 22. Ardaxcasca AVsa for Ат{ах$ага. (с) с and variants: in late Ardaxcasca AVsa, for ArtaxSaca. in late Мита), M'tra, M*$ra (see Lexi- eon), and the Persian personal name Vau-misa DB 2.49 ete. Other variants are explained in the phonology
853:A'Ha 7 imam (asm. for asn. ima) iya; so also : А%а 5 (restored). : АзРа 22f imam ustasaném afaganam (for nom. : iyam ušlašanā adagaind) müm (perhaps for . mana) upd mam kartā. ; A3Pa 26 {уа mam kartā (perhaps for mand kartam). : $67. NEOLOGISMS IN THE LATER INSCRIPTIONS, . that is, after Xerxes, may perhaps be counted аз : errors, though susceptible of explanation. There : are the following, all new formations for the . genitive—presumably after the gen. zšāyaðiyahyā, with which the genitives of the royal name were constantly associated, and gen. Arlazsagahyá:
1101:OP Casa-, from Elam. fu-ía-an, whence also Akk. Su-Sa-an.
1118:thus the pAr. *aratn- aratan- gave Av. dual arana, but OP arašn- and (with extension of the $) arasan- ‘cubit’, in inst. pl. arašaniš (see
1152:asan- "stone! with Med. s, in nom. asd, and
1192:pIE *efuo- ‘horse’, OP asa- in aec. asam and in аѕађата-; OP aspa- (with Med. sp) in waspa-, Aspacanah-, Vistaspa-; Av. aspa-, Skt. бра, Lt. equos.
1222:(with Med. s) asan- ‘stone’, $87. pIE *ghem- in Lith. Zémé ‘earth’, Lt. humus, but
1302:pIE *lekp- ‘cut’, Av. tataša ‘he has created’, Skt. азаб. "they fashion’; in ОР us-tasana- ‘staircase’.
1304:pIE *qek-s-, probably in OP caSa-m ‘eye’, cf. Av. cašman- ‘eye’, Skt. cdksus- ‘eye’ (see Lex. s.v. casa-).
1330:cf. Av. paséa, Skt. pased. The evidence of Sasa- nian Pahlavi shows that this value alone is pho- netic in OP (Bv. Gr. §114), and that the -&- which is seen in some sandhi combinations, be- longs rather to Median: OP kaSevy ‘anyone’ from pIE *q*0s-q*id; manaš-clä] DNb 32 from *menos-
1393:Skt. sindhu-. afa"ga- ‘stone’, Av. asanga-. ba"daka ‘servant’, Phi. bandak, NPers. bándáh. a^lar ‘inside’, Skt. antár, Lt. inter.
1524:*bher- ‘bear’ in bara*tiy ‘they bear’; *bhor- in aršti-bara ‘spear-bearer’; *bhr- in u-bar-tam ‘well uplifted’; *bhór- in asa-büra- ‘horse-borne’, uSa-büri- ‘camel-borne’.
1545:(д) long grade in substantives from the verbal root: asa-bdra-, u$a-büri-; u-céram, bajt-.
```


## [2026-09-04T19:12:01.264Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('KNT.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds',d.count('\\f'))\nlines=d.split('\\n')\nfor i,l in enumerate(lines):\n    if 'asan-' in l and i<1400:\n        print(i,l[:200])\nEOF\necho \"=== look for lexicon page markers ===\"\ngrep -n \"^\\s*17[0-9]\\s*$\" KNT.txt | head -20"
}
```


### [2026-09-04T19:12:03.090Z] TOOL RESULT

```
formfeeds 231
396 asan- ‘stone’, with s from Ё.
1117 thus the pAr. *aratn- aratan- gave Av. dual arana, but OP arašn- and (with extension of the $) arasan- ‘cubit’, in inst. pl. arašaniš (see
1151 asan- "stone! with Med. s, in nom. asd, and
1221 (with Med. s) asan- ‘stone’, $87. pIE *ghem- in Lith. Zémé ‘earth’, Lt. humus, but
=== look for lexicon page markers ===
5047:170
5071:171
5083:172
5118:173
5125:174
5165:175
5173:176
5210:177
5220:178
5259:179
```


## [2026-09-04T19:12:04.604Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5083,5130p' KNT.txt"
}
```


### [2026-09-04T19:12:04.655Z] TOOL RESULT

```
172
аг$Е- sb. ‘spear’ (830): Av. arsti-, Skt. rstt-, pIE *rs-ti- ($152.IIT, $179.IIT), to root in Skt. drsatt rşáli ‘rush, push’. See also ár&tika-, arsti- bara-. ат] nsf. DNa 44.
Grshka- sb. 'spearman': from ar&- ‘spear’ with vriddhi (as in wárttika-, $126), + suffix -ka- ($146.10). ага пет. DNb 44.
arslibara- sb. ‘spear-bearer’: aršti- ‘spear’ + bara- ‘bearer’ ($122, §143.V, §160.Ia). arStbara пзш. DNe 2 (written 59519, $51; the original draft seems to have had ате; on proofread- ing, the $° which was to have replaced the s* was wrongly substituted for the a, and this falsely cor- rected orthography was inscribed on the rock).
‘ava- demonst. adj. and pron. ‘that’ (5260.11, $264): Av. ava-, Skt. gen. du. avós, oCS орй; see also avd, араба, avadà, avapard, avahyarüdiy, pasiva. Decl., $200.
avam asm. DB 1.21, 22, 31, 40, 49, 57, 76, 80, 84, 88; 2.4, 4f, 12, 17, 20, 25, 30, 31, 35, 40f, 46, 50, 51, 55, 61, 84, 87, 94, 97; 3.4, 7, 12, 14, 14f, 17, 27, 38, 45f, 47f, 50, 56f, 58, 62, 67, 82, 85, 89; 4.38, 66 bis; 5.6°, 27; DNa 2; DSe 2; DSf 2°; DSt 2°; рле, 1; DE 3; XPa 2; XPb 3; XPe 2; XPd 2; XPf 2, 28; XPh 2, 37; XE 4; XV 3; А?Ра 2f^; A’H 3; A*Pa 2f. avamsam DB 2.20, 821; 3.31, 85; 5.8. auahya gsm. DB 1.29; 3.70; 4.48f. алапа absm. DSf 81. араш npm. DB 5.15, 31°; DSf 48, 50°, 51, 53, 54. avaiy apm. DB 2.77; 4.69. avaišām gpm. DB 4.51.
avém asf. DSE 27; alva]m-c* (= -ciy, 852.1) DB 5.26; ava as asf. (856.V) XPh 33. [ора npf. DNa 39.
ava nsn. DB 1.20, 447; DNb 10, 11, 20, 22; DSf 42. ava-maiy DSj 4; 051 46. ava-di$ DNa 21; DSe 20°; XPh 19. avaš-ciy (89. VT, $105) DNb 55. ava asn. DB 1.62; DNa 20, 37, 49; DSa 4; DSe 19°, 32°, 34, 44°; DSf 20°; XPa 16; XPb 25; XPf 39, 42; XPg 10; XPh 18, 42. ava-taiy DB 4.76, 79. avas-cty DNb 5f, 57; XPa 20; ХРе 14; ХРЇ 48. арапа absn. DSe 88. avand isn. XPh 49, 51f.
’ava- prefix ‘away, down’: GAv. avd, LAV. ava, Skt. dva; with verbs ar-, *kan-, gam-, jan-, à-jan-, !rad-, sta-, hard-. Cf. JAOS 62.274-5,
avd adv. ‘thus’, correlative to уаба: perhaps isn. of !а0а-, but more probably error for атаба ($52.УТ), by omission of one character, as taken by MB Cr. $59; see also avdkara-. DB 4.51.
OLD PERSIAN
avakanam, see ?kan-.
avdkara- adj. ‘of such sort’: avd ‘thus’ + kara- ‘doer’ (§160.Ia; wrongly Hz. ApI 101-3, who takes -kara- in avükara- and ciyükara- not from kar- ‘do’, but as kara- ‘time’, as in hakaram, q.v.). avakaram nsn. (6259) DNb 6; avdkaram-ca-mary ($109, $133, $135) DNb 2f.
avajam, see vaj-.
avabà adv. ‘thus, then’: LAv араба: 'ava- + adv. suffix -6@ (§191.If), cf. Skt. td-thd. Often ` with preceding or following correlative yaf; see also avabata.
(1) ‘thus: DB 1.24, 38, 63, 67, 70, 75, 78; 2.10, 15, 80; 3.24, 80; 4.8, 11, 13, 16, 19, 21, 24, 27, 29, 36, 39, 54; DBb 4; DBe 4; DBd 2; DBe 4f; DBE 20; DBg 4; DBh 3f; ОВ! 3; ВВ) 3; DPe 20; DNb 18f; DSf 16; DS} 3°; DZe 11, 12; XPf 22, 30 (written ааба, 852.11).  avaéd-dim DNb 17. avabä-diš DB 5.17, 33. avada-Saiy DB 2.30, 50; 3.14. avabd-Sém DB 2.20, 83; 3.57, 85.
(2) ‘then’: DB 142, 56, 90, 96; 2.70; 3.89. avaba-Sém DB 2.27, 36f, 42, 47, 56, 62, 98; 3.8, 19, 40, 47, 68f, 69.
avabasta DB 4.72, uncertain word read by KT; perhaps avatása-là, from атада with abl. -ša (8191.II; as in avadasa) + encl. apm. -tā ($188), ‘thenceforward Шеш (= the sculptures)? So Kent, JAOS 62.272-3, after Tolman’s emendation араб : là ‘thus them’, cf. НКЗ атаба Sa ‘thus stand (as І stand over the rebels)’, and Sen's avabäštā adj. apm. 'thus standing".
avadà (ie. avadá) adv. ‘there, then’: LAv. атаба; from 'ava- + suffix seen in OP «dà (319.1). Usually resumptive of an immediately preceding place-phrase, which is thus made locative (so al- ways in DB except 1.85, 88; 2.24; 3.74; 4.81; 5.24, 28). See also avadasa.
(1) ‘there’: DB 1.85, 88, 92; 2.9, 23, 24, 28, 34, 39, 44f, 54, 59, 66, 96; 3.5, 23, 34f, 44, 61, 66; 4.81; 5.24, 28; XPh 40. avada-Sim (8135) DB 1.59; avadd-Sim DB 3.74; avada-šiš DB 3.52.
(2) ‘then ’: DNa 42.
avadasa adv. ‘from there, from then’: avadd- + abl. -ša (5191.1; ВЫ, AiW 170, with lit.; against his view, Ву. Gr. §325), always after hacd. (1) ‘from there’: DB 1.37; 342, 80; DSf 47. (2) ‘from then’: DSe 47f.
LEXICON
avaparü phrasal adv. ‘along there’: ava asn. + postpos. pard (S191.IV). DB 2.72; 3.792.
avastü- sb. ‘leather’ (König, Klotho 4.45-6): etymology uncertain ($145). avastlälylä] 15. DB 4.89f (JAOS 62.267); hardly стаз уот) as read and restored by KT, which could be only an un- augmented imf. of ava- + stā-. Probably not а reference to the Avesta, as suggested by Wb. ZDMG 61.730.
dvahana- sb. ‘village’ (5166): deriv. (8147.1) of à + vah- ‘dwell’, Av. vah-, Skt. vas-, Gm. Wesen ‘being’. dvahanam DB 2.33; DSf 46.
avahar|da| DB 2.94, see hard-.
avahya- denom. vb. ($217) ‘ask for help’: Av. avahya-, Skt. avasya- in dsm. pres. ріс. avasyaté (RV 1.116.283), to Av. avah- ‘aid’, Skt. dvas- (Jn. JAOS 27.190, MB Gr. §209, Bv. Gr. $193). pali- + avahya- ‘ask for help’: patiydvahyaty ($140.11) Ist sg. imf. mid. DB 1.55.
avahyarddty phrasal adv. (§191.1V) ‘for this reason’: avahyd ($185) gen. of !ava-, + rüdiy ‘on account of’, q.v. For phrasing, cf. Gk. rovrov évexa, robvexa, Lt. huius ret causd; JAOS 35.322-9. DB 1.6f, 51; 4.47, 62; DBa 9f.
asa- sb. ‘horse’ (590, $143.IIT): Med. aspa-, Av. aspa-, Skt. déva-, Lt. equos, pIE *ekyos. See also Asagarta-, asabüra-, aspa-. asam asm. (col- lective, $255) DB 1.87.
Asagarta- sb. ‘Sagartia’, a northwestern prov- ince of the Persian Empire (§29.n2, $81): Elam. ad]. a&-Sa-kar-tt-a, Akk. adj. sa-ga-ar-ta-a-a, Gk. Yayapria. Probably asan- ‘stone’ (with Med. s < pIE Ё; $9.1, 587) + *garta- ‘cave’ (Skt. gdria-), ‘Land of Stone-Cave Dwellers’ ($161.10, §166.1; Bthl. AiW 207, zAiW 119-20); hardly asa- ‘horse’ (with OP s < plE ky, §90) + *garta- ‘wagon’ (Skt. gária-), ‘Land of Horse-drawn Wagons’. See also Asagartiya-. Asagartansm. DPe 15. Asagartam asm. DB 4.23. Asagartaty lsm. DB 2.80f; 4.22; DBg 8f.
Asagartiya- adj. ‘Sagartian’: adj. to preced-
ing (§144.111, $159). Asagarfiya nsm. DB 2.79;
4.20f.
asan- sb. ‘stone’: plE *aken- (§9.V, $87, §155.1), ef. asman-. See also Asagaria-. ай (8124.5, $187) nsm. DSf 40f; but see also under daru-.
173
asabára- sb. ‘horseman’: NPers. suvdr, cf. also Tedesco, ZII 2.40-1; asa- ‘horse’ ($126) + bára- 'earried by, rider’ (§122, $143.V, $159, §160.Ic). See also uvüsabüra-. аѕађбға пет. DNb 41f, 44, 45. asabáraibi$ ipm. DB 22, 71; 3.41, 72.
aspa- sb. ‘horse’, Median for ОР asa- (890), q.v.; in Aspacanah-, uvaspa-, Vistüspa-.
Aspacanah- sb. ‘Aspathines’, bow-bearer of Darius: Elam. a§-ba-za-na, Akk. as-pa-[si-nal, Gk. ‘Aoraftens; aspa- ‘horse’ (59.11, §9.n2, $90) + canah- ‘desire’, Av. -Cinah-, Skt. cénas-; ‘Lover of Horses’ (§161.[a, $168.10). Азрасапа пзш. (156.11, $185.11) DNd 1.
asman- sb. ‘sky’: Av. asman-, Skt. áéman-, Gk. йкроу ‘anvil’, Lith. akmud ‘stone’, pIE *akmen- /mon- (§95, 5155.11); for variant meanings, cf. Reichelt, ТЕ 82.28-57; for lranian ideas of its cre- ation, ef. Bailey, Zoroastrian Problems 120-48. Not dsman-, despite NPers. dsmén, which has length of later origin (Debrunner, IF 52.153, against Bv. Gr. $175). See also asan-, абаја-. asmünam asm. (§67.II, $124.6, $187) DNa 2f; DSe 2f; DSf 2; DSt 2f; DZc 1; DE 3f; XPa 2; XPb 3f; ХРе 2; XPd 3; XPE 2f; XPh 2; XE 4; XV 3; A'Pa 3°; A?He 3. asmanam (853) A?Pa 3.
ašnaiy adv. ‘near’, lsn. of ašna- ‘near’ (Hz. Ap] 98-9), Av. dsna- ‘near’, in loc. dsnaé-ca, asne ‘near’, abl. asna ‘from near’; from pAr. root end- ing in $ or 2 (pIE Ё or ў: Skt. aánóti ‘attains’ and djatt ‘drives’ hardly suit); not *à-zd-na-, pte. to à + *had- ‘herangehen’ (Bthl. AiW 1755; but *had-, which always has prefix d, is only a semantic vari- ation of thad- ‘sit’), cf. Skt. dsanna- as adj. ‘near’ (Bthl. AW 220). Possibly from plE *afijh- ‘choke, throttle’, cf. Lt. атаб, Gk. &yxw, sb. Lt. angor, Av. azah-, Skt. qhas-: *afijh- + pte. -no- (806, §147.1, $191.11I, $243); for semantics, cf. Gk. &yx« adv. ‘near’ (JAOS 62.276-7). Not ‘on the march’, to pAr. root *aé-, Skt. djatt, Lt. agit (Bthl. А 264); nor ‘m friendship’ on the basis of the Elam. kanna ети git (WB; KT); nor ‘at peace’, cf. Av. dxsitd ‘peace’, dx Sta- ‘peaceful’ (Ву. BSLP 31.2.67-9). Elam. kan- recurs as the translation of dausid ‘friend’, but this meaning eliminates only ‘on the march’, since ‘friendship’, ‘peace’, and ‘nearness’ are related ideas. asnaty DB 2.11f; [aSnajiy DB 5.23.
агай adv. “known ОСА: azdà "thus", Phi. ага,
174
Skt. addhá ‘surely’, from pAr. *adzdhà (885); cf. MB Gr. §118. DB 1.32; DNa 43, 45; DNb 50.
tah- vb. ‘be’: Av. ah- Skt. as-, Gk. tert, Lt.
esl, Gt. ist, pIE *es-. See also hafya-, А@їуй- bau$na-. Conj., $208.
amiy ist sg., Av. ahmi, Skt. dsmz, Gk. Lesb. tume, Att. eui, NEng. am (5118.11, $226.1): AmH 9; DB 1.12, 39, 53, 75, 79; 2.10, 15, 80; 3.25, 81; 49, 11, 14°, 17, 19, 22, 25, 27, 30; DBb 5, 7; DBe 8f; DBd 4f, 7; DBe 6, 9; DBE 4f; DBg 7f; DBh 5f, 9; Рві 6, 10; DB} 5; DNa 35; DNb 6f, 7, 8, 1f, 13, 15, 26, 27, 34, 40, 42, 43, 44, 51; Die Т; A? He 18.
азу, Ау. asti, NPers. dst, Skt. ásti (5116, 5228.1): DB 4.46, 51; DNb 54f, 56; DSe 37; XPh 30.
```


## [2026-09-04T19:12:15.271Z] TOOL CALL #18: Bash

```json
{
 "command": "ls tools/ && ls data/ && ls data/extracted | head"
}
```


### [2026-09-04T19:12:15.316Z] TOOL RESULT

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


## [2026-09-04T19:12:17.166Z] TOOL CALL #19: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-04T19:12:17.220Z] TOOL RESULT

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
```


## [2026-09-04T19:12:27.131Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN ===\"\ngrep -n -i \"sâyîdan\\|sajîdan\\|sâjîdan\\|afsân\\|fasân\\|sûhân\\|sûhan\" HRN.txt | head -20\necho \"=== HRN sāyad ===\"\ngrep -n \"sâjad\\|sâjîdan\\|säjad\\|säjidan\\|s.jad\" HRN.txt | head -20\necho \"=== HUB ===\"\ngrep -n -i \"afsân\\|afsan\\|sâjad\\|säjad\\|sûhân\" HUB.txt | head -20\necho \"=== CHEUNG ===\"\ngrep -n -i \"sāy\\|\\*sah\\|afsān\\|sāyīdan\" CHEUNG.txt | head -30"
}
```


### [2026-09-04T19:12:27.216Z] TOOL RESULT

```
=== HRN ===
=== HRN sāyad ===
=== HUB ===
2705:752. Vgl. san und afsan 'Wetzstein'.
6127:afsan 'Wetzstein* = fasan H. 98; afsurdan *frieren' = fu-
6470:afsos *Spott' H. 101 (?), paz. aw(a)sd8; afsandan ausstreuen'
7471:afsan *Wetzstein , afsar 'Krone', pdsux *Antwort\ pasand
=== CHEUNG ===
21308:*saH 325 
21352:*saH ‘to whet, cut’ 
21357:*saHh), v. Lubotsky 2001: 34. = Liste: 62 
21369:‘flat stone, flagstone’, Sariq. sad ‘slate, baking pan’, Yi. sur ‘slate’ (< *saHti- 
21370:‘whetstone’ ?), Sariq. suóy “flat, smooth (surface)’ ( *saH-ta-ka-, with fric. assimil. ?: 
21375:326 *saHh 
21383:9 There are no IE verbal correspondences of Ir. *saH / Skt. sa. A possible variant of 
21384:*saH is *sauH! (q.v.). 
21398:*saHh ‘to teach, instruct’ 
22324:Ó The root *sauH' either reflects a rare ua-stem of *saH (similar to *fiHu, Kellens 
55906:*drau(H)s (s.v.), *saH (s.v.), 
56193:*kart', *saH, *tas, *9uars, 
56928:*danh, *saHh 
58132:*iauc, *mauc’, *saHh 
58393:*saH, *sauH!
```


## [2026-09-04T19:12:28.836Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '21340,21400p' CHEUNG.txt"
}
```


### [2026-09-04T19:12:28.885Z] TOOL RESULT

```
(LW) hrasax, Syr. (LW) prsh’, Arab. (LW) farsax (< NW Ir.) 

«PIE *(s)Kek- ‘to pass, happen’. Ф To be separated from *skek- ‘to jump’, OCS skaco 
(skakati), (?) MWelsh kesgyc shakes, stirs’ ? = LIV: 551 f. | Pok.: 922 f. 

*IE COGNATES: OHG scehan, МНС schehen ‘to run’, OHG gi-skehan, MHG 
geschehen, NHG geschehen ‘to happen, take place’, (?) Olrish scuichid ‘moves; 
passes’ (contaminated with *skek- ?) 

*REFERENCES: EVP: 72; IIFL II: 414; DKS: 430b f.; Steblin-Kamenskij 1999: 338; NEVP: 73 


*saH ‘to whet, cut’ 
*AVESTAN: OAv. si- (sä-) ‘to sharpen, cut’ ?. 0 The verbal root may be non-existent. 
The attested forms can be interpreted differently: siiodum (< *siazd), sazdum (< 


*saHh), v. Lubotsky 2001: 34. = Liste: 62 
Pres. ja-: IMPV. 2р1. OAv. paiti siiodüm (Y 48.7); Aor. s-: ІЧЈ.ЛМРУ. 2р1. OAv. sazdüm (Y 31.18) 


*KHOTANESE: OKh. säta- ‘smooth’ (Z 23.44) 

*NWIR: Bal. sat/say-, sah- ‘to shave’, Kurd. (Kurm.) hasun/has- (ha- < *ham- or sec. 
2), (Sor.) sün/sü- ‘to whet, sharpen’, Gz. sün-/sünt ‘to rub, shave off’, NP sad 
‘smooth, plain; rubbed, worn out’ || (+ kardan ‘to do, make’) ‘to castrate, cut all 
clean away’ || (+ *ham- ?) Kurd. hasan, hasan (m.) ‘whetstone’ 

*NEIR: ? Pash. sūlēdəl ‘to become ground, grated’, Oss. I. sart ‘chisel’, ? Sh. säd (f.) 
‘flat stone, flagstone’, Sariq. sad ‘slate, baking pan’, Yi. sur ‘slate’ (< *saHti- 
‘whetstone’ ?), Sariq. suóy “flat, smooth (surface)’ ( *saH-ta-ka-, with fric. assimil. ?: 
-dy- > -óy- ?), (av- < *a-apa- ?) D. avinsun/avinst ‘to whet; to incite, direct’ || (+ 
*abi- ?) Yi. áfseno, yufseuno ‘whetstone’ || (+ *pati-) Sh. pisen (f.), Rosh. pisen (f.), 


326 *saHh 


Orosh. pison (f.), Sariq. pisan (f.), Yzgh. posan ‘whetstone, hone’ || (+ *ham-) Oss. I. 
yssyn/yssad, D. insun/insad ‘to whet, sharpen’ 

*SANSKRIT: 58 ‘to sharpen, whet? = EWAia П: 627 

9 There are no IE verbal correspondences of Ir. *saH / Skt. sa. A possible variant of 
*saH is *sauH! (q.v.). 

«PIE *KeHs- ‘to sharpen, whet’ = LIV: 319 f. | Pok.: 541 f. 

*IE COGNATES: Lat. cds ‘whetstone’, catus ‘sharp(-minded)’, Olrish cath ‘wise’, 


Arm. sur ‘sharp’, ON hein (f.) ‘whetstone’ 

*REFERENCES: EVP: 67; IIFL II: 245b, 188b; Abaev, Slovar’ I: 85; EVS: 72a, 61b f.; Abaev, Slovar’ II: 
36; DKS: 424a, 290a; WIM 1/1: 82; Abaev, Slovar’ IV: 278; Werba 1997: 320; Cabolov 2001: 426, 424; 
Korn 2005: 110, 313, 381 


*saHh ‘to teach, instruct’
```


## [2026-09-04T19:12:40.134Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\*sauH\" CHEUNG.txt | head -20\necho \"---\"\nawk 'NR>=22280 && NR<=22400' CHEUNG.txt"
}
```


### [2026-09-04T19:12:41.798Z] TOOL RESULT

```
5523:is more likely a "Reimbildung", cf. *sauH!. A.L. points out though that in Vedic 
21384:*saH is *sauH! (q.v.). 
22284:*sauH! ‘to rub, wear, whet’ 
22305:*suHia- of the root *sauH. — Samadi: 187, 25, 161, 172 
22324:Ó The root *sauH' either reflects a rare ua-stem of *saH (similar to *fiHu, Kellens 
22333:*sauH ‘to bulge, swell up, increase’ 
24131:*sauH! ?) 
55872:*sauH 
57659:*sard, *sauH!, Sort" 
58382:*sauH! 
58393:*saH, *sauH! 
---

*REFERENCES: IIFL I: 287a; IIFL II: 246a; EVS: 72b; DKS: 426b. 


*sauH! ‘to rub, wear, whet’ 

*MIDDLE PERSIAN: BMP s'd- /say-/ ‘to rub, wear, tire, tear’ || (+ *ham-) MMP hswd 
(ppp.) ‘whetted’ (Henning 1947: 45) = DMMPP: 186a 

Inf.: BMP swtn /südan/ 

*PARTHIAN: s’w- ‘to crush" > DMMPP: 306a 

Pres.: SUBJ. 150. s’w’n {hapax} 

*KHOTANESE: LKh. sauy- ‘to rub’ = SGS: 134 

*SOGDIAN: (+ *apa-) BSogd. ps’w- ‘to touch’ {hapax} 

Pres.: IND. 3sg. BSogd. ps’wt 

*CHORESMIAN: sw(y)- ‘to clean (the nose)’ || (+ *apa-) Bs’w- ‘to rub off, polish’ || (+ 
*pati-) ps’w- to grind’ || (+ *fra-) m/rs’w- ‘to rub, smooth’. © With regard to Chor. 
sw(y)- ‘to clean (the nose), Samadi (ibid.) cites Skt. svas- ‘to pant, wheeze’, which 
is semantically not compelling. The Chor. form may rather derive from a med. stem 
*suHia- of the root *sauH. — Samadi: 187, 25, 161, 172 

*NWIR: NP sudan/say- ‘to rub, wear, tear’, Kurd. (Kurm.) sö-, su-/sutin, (Sor.) su-, 
Awrom. sawa ‘to rub’, Zaz. sawitis/sawen- ‘to smear, rub’, Nn. sawnäye/sawn- ‘to 
grind’ 

*NEIR: Pash. sulédal ‘to be ground, grated’ (+ *-d-), Sh. (Baj.) säw-/säwd, Rosh. 
sew-/sewt, Bart. stw-/stwd, Yzgh. saw-/sed, (with redupl.) Sariq. sasew-/sasewd, (?) 
Yi. sa-/sovd-, M. söw- ‘to rub, smear, grind’, ? Wa. sbIX-/soXt- ‘to smear, rub’ (with 
sec. -X- ?) 


*sad 341 


*MISC: Orm. say- ‘to rub’ = say-/sayok 

*SANSKRIT: 5а ‘to sharpen, whet > EWAia II: 627 

Ó The root *sauH' either reflects a rare ua-stem of *saH (similar to *fiHu, Kellens 
1984: 162) or, more likely, may have been the result of contamination with 


semantically similar roots: *dauH and *skauH. 
*REFERENCES: IIFL II: 245, 541b; EVS: 75b ff.; DKS: 429a f.; Paul 1998: 312b; Cabolov 1997: 72; Lecoq 
2002: 132; Kiefer 2003: 206 


*sauH ‘to bulge, swell up, increase’ 

*AVESTAN: su- (sáuu-) ‘to bulge, swell up, increase’ = Liste: 63 

Fut.: IND. 3sg. YAv. “saoSiiat® (A 4.6); Partic.: pres. pass. YAv. suiiamna- (Y 55.3, Y 70.4, V 4.2, intens. 
YAv. süsouuista- (Aog 19), fut. saosiiant-; Inf: OAv. süidiiai (Y 44.2, Y 49.3); Caus.: pres. INJ. 2sg. 
OAv. sauuaiiö (Y 51.9), SUBJ. 3sg. YAv. sauuaiiat (Yt 13.129) 

*MIDDLE PERSIAN: MMP swd, swwd, BMP swt /sud/ ‘profit, use, advantage’ 
=> DMMPP: 310a 

*KHOTANESE: (+ *fra-) LKh. hasv- ‘to swell’ 2 SGS: 151 

*BACTRIAN: 0000 ‘plenty’ {hapax} = S-W, Bact.: 224 

*NWIR: Bal. sit", si0/si- ‘to swell’, NP süd ‘ gain, profit’ 

*NEIR: Oss. І. sy-var, D. su-var ‘uterus’ || (+ *fra-) Oss. I. resyjyn/resyd, D. 
reesujun/resud ‘to swell’ 

*MISC: (+ *fra-) Orm. Susuk, sras-"ek ‘to swell’ 

*SANSKRIT: sav’ ‘to swell, to become strong, to increase, to prosper’ (RV+) 
= EWAia II: 623 

«PIE *KeuH;- ‘to bulge, swell up’ = LIV: 339 f. | Pok.: 592 ff. 

*IE COGNATES: Gr. коёо ‘I am pregnant’, Gr. к®но‹ (n.) ‘wave’, Lat. cavus ‘hollow’, 
in-ciéns ‘pregnant’, MWelsh cyw (m.) ‘young animal’, OE Aun (m.) ‘young one’. 
*REFERENCES: IIFL I: 409b; Abaev, Slovar’ II: 380 f.; Abaev, Slovar’ III: 213 f.; DKS: 476; Werba 1997: 
320; Shahbakhsh: s.v. si-; Korn 2005: 91, 314, 385 


*säd ‘to cover, protect, shield’ 

*AVESTAN: Y Av. saóaiianti- (f. ?) ‘long trousers ?’ (N 95) 

*MIDDLE PERSIAN: ВМР c'twl /čādur ‘sheet, veil’ (< late Skt.) || (+ *4-) BMP ’s’dk 
/asayag/ ‘shelter’ 

*SOGDIAN: (+ *а-) CSogd. ’s’dty ‘shielded, protected’ || (+ *pati-) SSogd. pts’6(°) 
‘shield’, CSogd. pts’6 ‘shield’ (Schwartz 1967: 141 f.) 

*NWIR: NP cadur ‘veil’ (< late Skt.) 

*NEIR: (+ *4-) Oss. I. asadyn/aseest, D. asadun/asast ‘to become clouded; to cover the 
seeds of the land before sowing; to plant (beans, peas)’ || (+ *upa-) ? Pash. psunai 
‘ambush’ || (+ *pati-) ? Pash. psöl (m.), psald (obl.) ‘ornament, gold or silver 
jewelry’ 


342 *séand (*skand) 


*SANSKRIT: chad ‘to cover, to conceal’ (RV+), chattra (n.) ‘parasol’ (Br.+) 
= EWAia I: 554 

© The root is exclusively Ir. with no certain IE cognates. The often cited 
comparison to the isolated form OE heteru ‘clothes’ can hardly be used for 
etymological purposes. 

*PIE — => LIV: 546 | Pok.: 919 

*REFERENCES: EVP: 60; Abaev, Slovar’ I: 76; Werba 1997: 185; Lubotsky 2001: 40; NEVP: 66 


*stand (*skand) ‘to break, cleave’
```


## [2026-09-04T19:12:53.497Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN Wetzstein ===\"\ngrep -n -i \"wetzstein\\|reiben\\|schleifen\" HRN.txt | head -30\necho \"=== HUB context ===\"\nsed -n '2695,2715p;6120,6135p;7465,7480p' HUB.txt"
}
```


### [2026-09-04T19:12:53.558Z] TOOL RESULT

```
=== HRN Wetzstein ===
273:schreiben, wie mir die Zeichen gerade in die Feder fliessen,
613:(bezw. e) zu schreiben sein.
1276:98. efsän 'Wetzstein', eusän,^) fesän, vergl. sün,
1279:wa;f. sar. pasän ^Wetzstein'.
1536:127. engeiten antreiben', Praes. engez-em,
1537:phlv. angfytan antreiben', angejet (AV.), vergl.
1781:-) Assa- hätte ich auch No. 77 schreiben müsRon (KZ. 32, 577).— 37 —
2705:schreiben), Metrum: Xeflfi
3059:aw. pistra-; ai. l/'pes- 'zerreiben, zerstampfen {pistä-^
4051:car/^ auch ^Wetzstein (s. v. sunhade),
4087:ai. l/cörf-, corföf^e 'antreiben ; sich beeilen' (Nöldeke,
4596:*) EinmnI im Pehlevivondidäd, aber wohl nur umsohreibend, hur,
5416:606. ränden 'treiben, stossen*, ranis,
6095:(\)8än 'Wetzstein.
6099:'"Wetzstein* erwähnt
6197:S. 261 Vers 304); heraustreiben (Sahn. III, 1797
6201:fernen, heraustreiben (Men., AV.), spö/tUan; arm. LW.
6561:752. Süden 'reiben', Praes. säy-em, sät/lden.
6563:kurd. süin^ sün 'reiben, ein Messer reiben, schärfen'.
6852:siften reiben, kratzen'^) mit aw. aiu)i]siföis, yt. 14, 35
6858:oss. LW. sk'ärun 'treiben, jagen (v. Stackeiberg,
7658:kes, vergl. pö^yötkes (nur umschreibend), arm. LW. ßes.
7761:Vergl. oss. d. tarun, t. farjn, färin 'treiben, jagen,
8258:^) Die Syrer schreiben nach Mitteilung des Herrn Prof. Nöldeke
8312:962. mäliden 'reiben, glätten*, -mal (vergl. destmäV)
8319:reiben, mischen, streichen'; oss. märzin 'fegen* (180).
8546:983. tniiSten 'reiben*.
8551:'reiben*, kratzen, streichen, salben, mahlen' (244).
9099:schreiben, Praes. miw^s-em; nulje, nuwB^) *Wort
9102:ap. ni + [/^pais-, nipistanaiy 'schreiben* 2) — ai.
=== HUB context ===
inf. saxtan (ptc. saxta gewogen ), praes. sanjam {-sanj
Vagend', sanja ^Gewicht*), von letzterem aus ist der
Infinitiv sanjTdan neu gebildet worden.
748. Lies so, sot = phi. sdk. Vgl. die Nachtrage bei
Horn p. 259.
749. Fiir aspvOrakan BB. 4, 39 und 62 ist vaspuhraMn
zu lesen, vgl. ZDMG. 46, 327. So bleibt np. suvdr
= asvdr = phi. ashar (Pahl. Dictionary II, 409), das
direkt dem ap. asabara- (nicht assabdra- !) lautgesetz-
lich entspricht.
752. Vgl. san und afsan 'Wetzstein'.
753. Darmesteter iibersetzt suirya- jetzt durch *banquet'
(Zend-Avesta I, p. 389), schwerlich mit Recht, da
suirya- nach yt. 14, 20 morgentlich, tagend' heisst.
Vgl. meine Casuslehre p. 196.
754. Geiger kommt Etym. und Lautl. des Afgh. Nr. 209
(afgh. s€l/rai 'Loch') wieder auf Darmesteter's Er-
klarung zuriick, die an paz. suld = phi. mrdk oder
sulak Shk. 268, phi. sUlak Gl. and Ind. 166 scheitert.
Zd. ^sufraka- wSre zudem = np. *sufra, zd. ^stiuyrdka-
= np. "^suhrd,
mit Vokal + Doppel konsonant anlauteten. Dies geschah
bei: ustur ^KsuneeY = sutur, zd. ttstra-; asvar *Reiter = .s?/-
var, phi. asbar, ap. asabara-; afroxtan *anzunden, erleuchten,
glanzen' = ftiroxtan, furoy 'Glanz', phi. afrOxtan, zd. aiwi
+ rwJ. Ebenso bei abresum = baresum *Seide', arm. apri-
sum H. 65; fitadan = uftddan 'fallen* H. 92; afzudan zu-
nehmen = fuzudan H. 96; afsar *Ziiger = fisar H. 97;
afsan 'Wetzstein* = fasan H. 98; afsurdan *frieren' = fu-
surdan H. 100; afsos *Spott* — fisds H. 101; afscLndan *aus-
streuen' = fisCtndan H. 102; afgandan Vegwerfen' — figandan
H. 103; aknun = kunUn jetzt'; xastn *blauschwarz' = zd.
axsa^na-; s/jdow/ 'Ruheplatz, Gasthaus*, phi. aspanj^ arm.
ospnjfakan *Wirt'; abranjan 'Armband' = baranjan {dast-
baranjan), arm. aparanjan (s. § 3); azbar oben' — zabar
u. s. w. Dieser Wechsel tritt nicht ein, wenn der erste
der Doppelkonsonanten n ist.
sal Mahr = zd. sareda-; surx Voth* = zd. suxra-,
ap. &uxra'; suxun^ suxan *Wort* aus iran. "^saxvan- = ap.
*&a(h)uvan' von &ah *sprechen, skr. gq^, zd. satlh; sang
*Stein, ap. a&angaina- *steinern ; sard 'kalt' = zd. sareta-;
saya *Schatten' = skr. chdya- (mit ch aus idg. k%) u. s. w.
Vgl. Horn 688 — 765. Ebenso in Zusammensetzungen :
afsan *Wetzstein , afsar 'Krone', pdsux *Antwort\ pasand
'angenehm' (oben p. 41), dsiidan ruhen*, duvSst *zweihundert'
=-• zd. duy^ saite; farsang = phi. frasang naQaaiyyric,
u. s. w.
Im Arm., Phi. und Paz. erscheint hier gleichfalls
stets 5.
Da es nicht wahrscheinlich ist, dass das aus iran. s
entstandene ap. d- schon im altesten Phi. wieder in s iiber-
ging, da vielmehr das im Phi. Paz. und Np. anlautende s
= iran. s ein ap. s voraussetzt, so ergiebt sich, dass hier
```


## [2026-09-04T19:13:00.053Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 98 ===\"; sed -n '1270,1290p' HRN.txt\necho \"=== HRN ~6090 ===\"; sed -n '6085,6105p' HRN.txt\necho \"=== HRN 752 ===\"; sed -n '6555,6580p' HRN.txt"
}
```


### [2026-09-04T19:13:00.126Z] TOOL RESULT

```
=== HRN 98 ===
aw. "^aiwi + \/ snv-, sävaijät 'er wird nützen';
phlv. afzütan^ ofzün^ afzüntk^ afzäyltan, afzäyimtan,
afzäy(i)sn,
97. efsär 'Zügel, Zaum', ßsar.
aw. ^aiwisdra-; phlv. afsdr (Bund.),
syr. talmüd. LW. 1DCN.
98. efsän 'Wetzstein', eusän,^) fesän, vergl. sün,
phlv. afsän (Säy. Näääy. 10, 28); skr. gäna-^) 'Wetz-
stein* + abhi; vergl. B.rm. yesan (H. No. 211).
wa;f. sar. pasän ^Wetzstein'.
99. efser 'Krone'.
aw. ^aiwisara-; phlv. afsar 'Krone' (6ö§t-T Fr.)^).
100. efsurden 'frieren', gefrieren, fusurden^ ßsurden
(Sahn. I, 78 Vers 211).
phlv. afsartan, afsar(i)smh (vd. 19, 12), vergl. arm.
surf, 'Kälte'.
Siehe np. serd (No. 731).
101. efsös 'Spott, Scherz', fisös,
phlv. afsös 'Spott, Scherz'.
Darmesteter's Erklärung, Et. ir. II, 131 aus aw.
*aiwisaoca' ist unhaltbar, da aw. d im Np. nicht zu s
=== HRN ~6090 ===
aw. *särö,dära' ; phlv. sälar, \idQa(jTaöa()av\öaXdvrji^
(Procop. Pers. I, 7, 11 u. ö.), arm. LW. s(dar, spajsalar,
np. serdär (phlv. sardär) ist eine junge Bildung, da
man sonst seryär erwarten müsste.
Vergl. No. 726.
693. sämän 'Ordnung, Grenze; Hausgerät etc.'.
phlv. sämän, bezw. sahmän (z. B. AV. 'boundary-
mark'), arm. LW. sahman o()ocj oQ^o/ndc^ -nQoacayua (de
Lagarde, No. 1934).
Zu ai. [/'gad' etc. (Fr. Müller, WZKM. 5, 262).
(\)8än 'Wetzstein.
Siehe efsan (No. 98) 0.
*) Nachträglich sei hier noch np. sumhäde (goschr. sunb"), Käs.
K. sunbötä, arab. LW. sunbäSaj^ sunhäSat (Bibl.' geogr. arab. IV, 277)
'"Wetzstein* erwähnt
■}\*m^t!/*m.^i— 154 -
694. (2)säii 'Teil, Stück; Art und Weise'; -$an gleich,
ähnlich, -sä.
Die Deutung von aw. sü^ia- (yt. 19, 44) als *Stück'
(Studien, I, 148) hat Geldner BB. XV, 254 wider-
rufon.
=== HRN 752 ===
'Brand'.
751. 8üd 'Nutzen, Vorteil'.
g. sid 'Zinsen*.
aw. [/'saV' 'nützen'; phlv. süt , sütih, sütömand,
sütlnUa/L
bei. sät, Sit (357); sonst allgemein entlehnt.
752. Süden 'reiben', Praes. säy-em, sät/lden.
ai. l/'cd' 'wetzen, schärfen .
kurd. süin^ sün 'reiben, ein Messer reiben, schärfen'.
Die Bedeutung ist im Neupersischen verblasst ;
vergl. aber das Kurdische.
753. sür *Fest, Gelage'. •
aw. süirya- 'Morgenessen* (Darniesteter, Et. ir.
II, 161 und Geldner, KZ. 25, 531 Note 228); phlv.
5/Tr 'Morgenmahl, Mahl'.
bei. LW. slr 'Hochzeit, Verlobung' (241) ; siyn. sur
'Gelage, Hochzeitsfest* (die Bedeutung ist hier noch
mehr als im Np. specialisirt).
754. sTirfii, sülax, ^Nt^lD (Is. 11, 8) 'Loch'.
Darmesteter's Etymologie (Et. ir. I, 62) aus
aw. *siifräka' , phlv. "^sufräk , "^suhräk , ^süräk in
säräk]öniand bezw. süläk]ömand ist unmöglich, da im
Aw. nur suwrä- ('Ring' oder Pfeil') vorkommt (vergl.
oben No. 740).
kurd. LW. särä/; afy. sürai^ LW. süläy.
*) Vergl. bezüglich des Vokals Kas. V. bdslz, bäalzün neben
```


## [2026-09-04T19:13:14.828Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" SNS_pages.txt | head -5\necho \"---\"\ngrep -n \"afsan\\|afsān\" SNS_pages.txt | head\necho \"--- index area ---\"\nsed -n '33835,33850p' SNS.txt"
}
```


### [2026-09-04T19:13:14.909Z] TOOL RESULT

```
---
1657:                                                              If/11**               \~K/\y£           \/\&<S .f      J^'j^^-^^^jJjK^xib^.                                        -    .       U*        UI   :   afsannj^o-
3035:                                                                                                                                                                                                                 •f/lY ^    (   afsan
16483:abSrtar 25/15                   afsan 18/19
--- index area ---


afganSd 228/13 
afganend 228/11 
afganisn 228/15 
afroxtan 21/21 
afrBzend 22/9 
afrOzisn 22/6 
afsan 18/19 
afs3yend 19/2 
afsard 20/3 
afsihSnldartar 19/5 
afsed/apsSd 21/5 
afsed fisted 21/7 
afzar/abzar 17/10 
afzayed 18/1
```


## [2026-09-04T19:13:19.784Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1650,1665p' SNS.txt\necho \"=== 3030 ===\"\nsed -n '3028,3042p' SNS.txt\necho \"=== head of SNS_pages ===\"\nhead -c 400 SNS_pages.txt"
}
```


### [2026-09-04T19:13:19.844Z] TOOL RESULT

```
Y/T** 



j~^j- '/-'*- 



iWii^i*j^ ^j e*^ 



J~ 



=== 3030 ===


-\ 



mOzag +tf , ab§ -*i**b «j^oj->* -*i>\* :ab§mOzag: 4«. 



■A/1^ 'V T +ai* 



*tf< 
=== head of SNS_pages ===
    A
>l»>'i




 O^t'

        /
« *>&
                              Shiraz University Publication




     A GLOSSARY OF
SAYIST NE SAYIST
 A pahlavi persian Glossary
             -




       and Six indexes

         '




                      By

        Mahmood Tavoossi




                 * Z 2 2 7 7 6 O*
U*'^ J^»t ^Sj (jl3T v U». ^jb.1^ ^jjt



 tr-w^-r
```


## [2026-09-04T19:13:30.545Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR==1657' SNS.txt\necho \"=== ref_page usage ===\"\npython3 /home/sfmqrb/git/rishe/tools/ref_page.py --help 2>&1 | head -30"
}
```


### [2026-09-04T19:13:32.048Z] TOOL RESULT

```
=== ref_page usage ===
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


## [2026-09-04T19:13:35.996Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['SNS'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-04T19:13:37.762Z] TOOL RESULT

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
 "title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/VajnameShayest",
 "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"
 ],
 "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image",
 "covers_etymology": true,
 "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."
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


## [2026-09-04T19:13:45.815Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(d))\nfor leaf in (533,534,535):\n    t=d[leaf]\n    print('==== leaf',leaf,'printed ~',leaf+543,'====')\n    print(t[:1800])\nEOF"
}
```


### [2026-09-04T19:13:47.410Z] TOOL RESULT

```
leaves 684
==== leaf 533 printed ~ 1076 ====
                                                                                                  ‫= —‬

      ‫استحکام که از لیف خترامباندودر کشتی و‬                  ‫بون زای قطمدار(‪.)۱‬سازی‬
                                                                                  ‫سار = ک‬
  ‫بز رکه آ را مکار دار ند وگاهی دزدالرا نبزدان‬
                                                         ‫که نوازند مانند چنکه و عود و بربط وطتبور‬
‫بحلق کشند ‪ -‬ورسمان علفی‌را نیز گویندوبعر بی‬              ‫وقىجك و قانون و امثال آن ‪ - ۴‬و سامان سفر‬
                                   ‫شردطه خوانند ‪.‬‬        ‫واستعداد و ساختگی کارها ورونق‌مهم‌را گونند ‪۴‬‬
 ‫سازو اره = بباوراووز»ن‌ومعنی‌ساز گار‬                        ‫کاری‬
                                                                ‫با‬‫‪ -‬وبمعتی ساز گاری وتحمل ‪ -‬و امر ز‬
                            ‫است ‪,‬حنی موافق مزاج‬
                                                         ‫و تحمل باشد ‪ -‬و بمعتی سلاح وادوات جنگه‬
 ‫سازواری‪= ۱‬بروزن ومعنی‌ساز گاری‬                          ‫وخفتان و زره وچارآینه و مانند آن هم‬            ‫ِ‬‫از‬
  ‫باشد بعنی‌موافقت در مزاج و درطبم ودرکارها‪.‬‬              ‫‪ -‬و ضیافت ومهمانیر! نیز گوبند‪ -‬وبمعنی‬
 ‫سارو باز = بروزن چاقو باز رسمان‬                          ‫‪ 7۳‬وحیله وفریب وخدعههم آمده‌است‪-‬وبمعنی‬
 ‫بازراکوبند واوشخصی است که بوبالای ریمان‬                 ‫مثل ومانند وشبه ونظیر باشد ‪ -‬ونقم وفایده را‬
                                                                                             ‫هم مبگویند‪۶ .‬‬
                 ‫رود وبازبهای غیرمکرر کند‪.‬‬
 ‫سازور ‪ = ۷‬بورزن دادکر ؛ ساخته‬                           ‫بنتح‌کان فارسی بر وزن‬       ‫سار گری ‏‬

 ‫و پرداخته و مهیا کرده شده را گوشد‪ -‬وصاحب‬                      ‫مرقکب‬
                                             
==== leaf 534 printed ~ 1077 ====
    ‫= —‬                                                                                       ‫ساسا رکشت‬
‫بدین معنی آن طایفه راکه ایشان بانواع کدبه‬                  ‫با ثالث بالف کشده‬    ‫کشت ت‬      ‫ساسار‬
‫وکدایی و اصناف سوال جواهر و لقود ار رکان‬
                                                          ‫و برای یی قطةٌ زده و کر کاف و سکون شن‬
                                                           ‫و تای قرشت ‪ ۰‬بلغت سربالی تخمی است‌دوابی‬
‫خوانند ‪ ۰ ۴‬و بعضی کویند ساسان چون از بم‬                         ‫که آنرا بعربی بزرالانجره وقریض‌خوانند ‪۰‬‬
‫و خوف خواهر خود با جممی از درویشان سردر‬                   ‫ساسا لیوس ‪ -‬بکسر لاموتحتانی بواو‬
‫نام‌داشت»‬     ‫بود اوئیز ساسان‬     ‫حهان نهاد اورا ری‬
                                                           ‫رسیده وبسین بی‌نقطةٌ زده » بلغت‌سریانی‌انجدابرا‬
‫بابك والی فاری دختر خود را بوی‌داد ‪.‬بسدازآن‬                ‫کوبند ‪ ,‬وآن رستنیی بکاشهد‌صمغ! براحلتیت‬
‫فنردزان‌ساسان بن‌ساسان که نبیره های‌بايك‌بودند‬
                                                          ‫خوانند » ویس کوبند انجدان رومی‌است وآ را‬
‫ملك رافرو گرفتند وایشان راساسانبان‌خوانند؟ ‪.‬‬
                                                           ‫کاشم رومی نیز گوبند و آنهم نوعی از این است‬
‫بارساء‬      ‫بروزن‬   ‫یا تای فرشت‬   ‫‪= ۴‬‬   ‫ساستا‬              ‫لسکن اکنید‌درازتر ازآن عیباشد»وا تراسالیون‬
                     ‫نام دبوی است از تابعانآ هرمن ‪.‬‬
                                                                                    ‫وسیالیوی همگویند‪.‬‬
‫ساسر * دینتم اك‌بروزن لاغر ‪ ۰‬بمعنی‬
                                                           ‫= بروزن آسان ‪٠‬‏ صاحب ترك‬        ‫ساسان‬
‫» قلم ولی‬       ‫سارج است که سار باشف ‪ -‬رضم تال‬
                                                           ‫باشد ‪ -‬و کدا وکدابی کن
==== leaf 535 printed ~ 1078 ====
  ‫سالار‬                                                                                         ‫س‬
                                                                                                ‫باباه‬
                                                                                                    ‫سم‬
          ‫ررشد را لگزوبند ‪.‬‬
                          ‫مپی‬
                            ‫وو‬‫صادق ‪-‬‬
‫ساك ‪ - ۴‬بروزن پاك‪ .‬بمعنی فسخ‌باشد‬                                                     ‫قوت ناه دهف‪.‬‬

 ‫معتی جپل وضمف وفاد رای‬
                      ‫و فخ در لبفت‬                 ‫ساطل ‪ -‬بکر طای‌حطی ‪ ۰‬مفرب‌ساتل‬
 ‫وتسان است ؛ و درطریق اهل تناسخ آن‌است که‬          ‫باشد که شبراز بان‌روشتك‬    ‫است ‪ ۱‬و آن رستنی‬

 ‫روح بدومرتبه فرورودیمنیآزصورت انسانی‌صورت‬        ‫خوانندش ؛ و باين معنی با شین نقطه دار هم‬
                          ‫لباتی چمنآرا گردد‪.‬‬                                            ‫‪.‬‬        ‫آمده ات‬
 ‫سا کنان گر دون = کنابه ازستارها‬                   ‫ساع = بر وزن باغ » جانوری باشد‬
                 ‫‪-‬اکه را لگبوزنند‪.‬‬
                                 ‫مل‬‫وشد‬
                                     ‫با‬                                                     ‫مالند سار ‪.‬‬

 ‫سا کیز ‪ -‬باکافبروزن فالیز ‪ .‬لمد‬                  ‫شراب را‬      ‫ل‬
                                                               ‫یغرا‪٠‬‏‬
                                                                    ‫ساغر ‪ -‬بروزن لا‬
‫رااگویند مطلقاً خواه نمد ثکیه باشد وخواه نغیر‬         ‫از ملك د کن ‪.‬‬      ‫ونام قصه‌ایت‬       ‫کونند ‪- ۴‬‬


                                                   ‫سافوت = با فا بروزن لاهوت »سدایی‬
 ‫سال » بروزن مال » معروفت و آن‬
 ‫حر کت بك دوره آفتاب‌است از فقطة برج حمل‬
```


## [2026-09-04T19:13:57.598Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f in ['BQT_v2_pages.txt']:\n    d=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    for i,t in enumerate(d):\n        if 530<i<545:\n            for w in ['ساییدن','سائیدن','سوهان','سان ','افسان']:\n                if w in t:\n                    print(f,'leaf',i,'printed~',i+543,'has',w)\nEOF\necho \"=== v3 pdf 283 for فسان ===\"\npython3 - <<'EOF'\nd=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('blocks',len(d))\nfor i,t in enumerate(d):\n    if '[pdf page' in t[:60] and ('فسان' in t or 'افسان' in t):\n        print(t[:60].strip().replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T19:13:59.374Z] TOOL RESULT

```
BQT_v2_pages.txt leaf 534 printed~ 1077 has سان 
BQT_v2_pages.txt leaf 535 printed~ 1078 has سان 
BQT_v2_pages.txt leaf 539 printed~ 1082 has سوهان
BQT_v2_pages.txt leaf 539 printed~ 1082 has سان 
BQT_v2_pages.txt leaf 540 printed~ 1083 has سوهان
BQT_v2_pages.txt leaf 541 printed~ 1084 has ساییدن
BQT_v2_pages.txt leaf 542 printed~ 1085 has سان 
BQT_v2_pages.txt leaf 544 printed~ 1087 has سان 
=== v3 pdf 283 for فسان ===
blocks 721
[pdf page 213] یواژ  کوشت ریا رااگویندکه زغن باشد و او شش ما
[pdf page 281] we ‏بیان‎  درحرف فا با سین بی‌نقطه هشتمل بربس
[pdf page 375] کول ۲ زن اس ‎SI‏ = بر وزن و معنی کابل است + ک
```


## [2026-09-04T19:14:07.839Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor leaf in range(533,546):\n    t=d[leaf]\n    lat=re.findall(r'[A-Za-zāīūēōšāčžḡʿâ\\.\\-\\*]{3,}',t)\n    print('leaf',leaf,'printed~',leaf+543,'LATIN:',lat[:40])\nEOF"
}
```


### [2026-09-04T19:14:09.576Z] TOOL RESULT

```
leaf 533 printed~ 1076 LATIN: []
leaf 534 printed~ 1077 LATIN: ['nirt']
leaf 535 printed~ 1078 LATIN: ['sarda', 'daS']
leaf 536 printed~ 1079 LATIN: ['SII']
leaf 537 printed~ 1080 LATIN: ['gecko', 'Lacerta', 'gecko']
leaf 538 printed~ 1081 LATIN: ['airamaS']
leaf 539 printed~ 1082 LATIN: []
leaf 540 printed~ 1083 LATIN: ['...']
leaf 541 printed~ 1084 LATIN: ['...']
leaf 542 printed~ 1085 LATIN: []
leaf 543 printed~ 1086 LATIN: []
leaf 544 printed~ 1087 LATIN: []
leaf 545 printed~ 1088 LATIN: ['savik', 'saev', 'subuk']
```


## [2026-09-04T19:14:19.267Z] TOOL CALL #32: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1488 --image 2>&1 | head -60"
}
```


### [2026-09-04T19:14:25.982Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1488.png
REF: BQT:1488  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 281  OCR-lang: fas

بیان نهم
درحرف فا با سین بی‌نقطه مشتمل بربیست وچهار لفت و کنایت
فا <- بفتح اول وئانی‌بالف کشیده,شهری فای‌است که افسون کر(۱) ورام کننده باشد.#*
است از ملك فاری . فسرد ۴ بنم اول و نانی و سکون‌را
قصار ۱ - بفتم‌اول بروزن مهار «بسمنی | و دال بی‌نقطه . ماضی فسردن است بعنی‌بسته‌شد
افار است. وآن چیزی باشد که ازچرم دوزین | ومنجمد گردید ؛ وبکر اول هم گفته‌اند .
وبر اسر اسبان‌کنند . فسردن ۱ بنم اول بروزن شمردن,
فسان < بفتح اول بروزن زبان » سنکی بمعنی بیته‌شدن ومنجم دگردیدن باشد ؛ وبکسر
باشد که‌کارد وشمشیر بدان تی زکنند ۴ سوافانه | اول هم‌آهده است .
وحکایت را نی ز گویند ۴ . فسرده ۴ یم اول بر وزن شمرده .
فقسافه ۴ - بروزن زمانه . بسمنی‌افانه بمعنی منجمد کردیده و بسته‌شده باشد - وبمعنی
وحکایت بی‌اسل‌باشد - و بمعنی‌شهرت بافتّه شده | دل سرد کردیده و سردشده هم هت بعنی دست
ومشپور نیز آمده است. ودل کسی بکاری فرود - و بمعنی شکاری هم پنظن
فسانیدن - بر وزن رسانیدن » بممنی آمده است ؛ و با اول مکور نی زکویند .
مالیدن و راست کردن 8 - و رام ساختن ‎٩‏ - فسرده پستان - بم اول وکسربای
و افان هگفتن ۷ -و افو ن گری کردن‌باشد ‎.٩‏ | فارسی + کنایه از زنی است که هر کز نزاییده
فسانیده « بر وزن رسانیده . بمعنی و عقیمه باشد - وزن پیررا نیز گفته‌اند .
افسون خوانده‌ورامکرده ۸ - وراست نموده ‎٩‏ - فسرده بیان * جضم اول و فتنح بای
و مالیده باشد ‎٩‏ . ایجد »کنایه از کسی است که سفنان او خنك
فمای بفتح اول و ثانی بالف کشیده | و بیعزه وپوج ویبهوده باشد .
و بتحتانی زده , بممنی افسون‌گر و رام کننده فسرده دل « بم اول .کنایه ازمردم
و فماییدن بمعنی افسون کردن ورام‌نمودن. دل مرده و افرده باشد - وکناید ازمردم سخت
فساینده « بر وزن سراینده . بیمنی | دل و پیمهر هم هست .
(۱) خم۱: افون خواشده .
۱ - مخفف «افیار» (ه.م.), ۴ - رك : افمان, ارسان .مان . کردی 136927
( سنکه چاقو نیز کن ) , 8198 « ژابا س ۸۸۳ ؛
چه‌حاجتی بضان روزرزم توفش‌را ‏ ازآنکه سبنهٌ امدای اوست سنگه.فسان ‏ «فرخی‌سیستانی ۹۲۷۹.
۴ برك: قانه, اقانه ,۴ - مغفف « افانه » (9م.) .8 از : فان (سنگه)
+ بدن ( پوند مصدری ) . ‎٩‏ - ظ.مصحف «فایدن». رك : فای . ۷ - از فان
(افانه) + بدن (پلوند مصدری) ‎ .‏ ۸ - باین‌معتی ظ. مصحف « فایده » . رك : فای .
‎٩‏ - اسم مفعول از «فانیدن» ۰ ۱۶ رك : فردن ۰ ۱۱ مخفف « افردن *
(وم.). ۱۳ -اسم مفعول ازهفردن» .
ات فساییدن درك : فاي.
```


## [2026-09-04T19:14:46.787Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in (539,540,541):\n    print('==== leaf',leaf,'====')\n    print(d[leaf][:2500])\nEOF"
}
```


### [2026-09-04T19:14:48.630Z] TOOL RESULT

```
==== leaf 539 ====
  ‫ساو‬                                                                                                        ‫‪7‬‬


‫سانقه ‪ 1‬د بکر دون و فتح قاف» پر‬                                                                     ‫وامثال آن تکزنند‪.‬‬
‫صباوشان را گوند ‪ ۰‬وآن دوای باشد که بعر نی‬
                                                               ‫سان = روزن کان » بمعنی فارز وروش‬
                                     ‫دم الاخوین خواناد‪.‬‬        ‫م‪-‬طولق سوهانرا لیز‬   ‫وت باشد ‪۱‬‬ ‫امد‬
                                                                                                ‫عرس‬
                                                                                                  ‫و‬
 ‫ساننج ‪ ۷‬ب=فتح الك بورزن نارلج‪,‬‬                                ‫گفته‌اند ‪ ۴‬اعم از چوب‌ساوی واهن وطلا ونقره‬
             ‫وعیف‪.‬‬  ‫ووچك ض‬  ‫مرغکی باشد سياه ک‬                  ‫ساوی ‪ -‬وشبه‌واظیر ومثل‌ومانند راهمکفته‌اند ‪۴‬‬
 ‫ساو ‏ بر وزن کاو » بممنی باج وخراج‬                            ‫‪ -‬و مطلق سلاح جنگه باشد خواه خود پوشند‬
 ‫امت وآن زری‌باشد که یادشاهان‌قوی‌ازیاه‌شاهان‬                  ‫بوشانند ‪ -‬و بمعنی حصه‬                 ‫و خواه برفل واس‬
 ‫هم‬     ‫و رصد‬     ‫و نسمعتی حصه‬   ‫‪-‬‬     ‫‪۸‬‬   ‫بگرد‬   ‫ضعبف‬        ‫همهت چه هرگاه کوبند « سان‬                           ‫وه‬
                                                                                                                   ‫پر‬‫باره‬
                                                                                                                        ‫وب‬
 ‫وطلای خالصی را نیز گوشد‬              ‫‪ -‬وور‬   ‫آمده مت‬          ‫سان کردند » مراد آن باشد که پاره پاره کردند‬
 ‫وبوته‌ای‬     ‫‪۳‬‬   ‫شده باشد ‪۹‬‬   ‫رزه‬     ‫که شکته وبرزه‬           ‫‪ -‬وفانرا گیفزته‌اند‪ .‬وآن مگ باشد که‌کارد‬
 ‫باشد خاردار و سفد رنگ سلندی بك کزوآترا‬                        ‫وشمشیر وغیره بدان تیز کنند ‪ - ۴‬وبمعنی‌سامان‬
 ‫بجای هیمه بوزانند ونیز درمیان کرمپای پیله‬                     ‫و سرانجام و اسباب و والمودن خود را بخوبی‌هم‬
 ‫بهند تاپبله برآن تند ‪ -‬و بممنی مطلق سودن‬                     ‫هست ‪ -‬و عرض لشکر را نکیوزبند ‪ - ۵‬و دام‬
 ‫وسازیدن باشد ‪ -‬وآهنی را یز کون که بدان‬                        ‫فصبه‌است نزدىك بجارىك کار کهآ نم فصبه‌است‬
                        ‫‪.‬‬      ‫قز کنند‬     ‫کارد وشمشر‬                                                         ‫از کادل ‪3 .‬‬

      ‫‪ ( ۷ [025 .‬چطور ‪ .‬چان )‪٩‬‏ ‪( 2۷ 8749 ۰‬بابنطرز)‪.‬اففایی‬                              ‫‪ - ۱‬کردی 
==== leaf 540 ====
       ‫ه‬
       ‫جاه‬
         ‫ا ب‬
           ‫و‬                                                                                                  ‫ساو آهن‬
                   ‫بجهت رشتن را درآ تحاگذار ند ‪.‬‬
                                                                   ‫ساو آ هن ه بروزن کاوآهن » سونش‬
‫» بر وزن لامور ‪ ,‬کوهی است‬               ‫ساهور‬                       ‫وراد آهنی را گویند که ازدم سوهان‌بریزد‪.‬‬
                                                                                                          ‫ی‬
 ‫درمغرب که ممدن سنگی است بهمین‌نام ‪ .‬وآن‬                            ‫ات‬     ‫بروزن کاوه ‪ ۰‬نامبهلوانی‬    ‫ساو ه‪-‬‬

                                                               ‫یه در جنگه رستم ا‬
                                                                               ‫تورانی خوش کاموسکشال ک‬
 ‫کند ؛ و بجای هامیم هم بنظر آمده است‬                               ‫کته شد و اورا ساوه شاه ایز مبگفتند ‪ -‬ونام‬
                                               ‫له اعلم ‪.‬‬
                                                                    ‫شهری است مشهور ومعروف در عراق ‪٩‬‏ گ‪.‬وبند‬
‫ساهو يه ‪ -‬باهابر وزن آموبه ‪ ۰‬نم‬                                    ‫" درباچه‌ای در آنجا بودکه هرسال يك کس را در‬
 ‫عهلم تعبیرمثل‬ ‫رک‬ ‫معبری وتعبیر کنندهای بو‬
                ‫دده‬                                                 ‫آن غرق میکردند تا از سیلان ایمن مي‌بودند‬
 ‫نوظیری نداشته » و بعضی گوبند زنی‌بوده‌است‪.‬‬                         ‫و در شب ولادت سرور کاسات آن دریاچه خشكث‬
                                    ‫ممبره ساهویه تلم ‪.‬‬              ‫شد ‪ -‬و زرخالسی را یز گوبندکه شکسته‌وریزه‬
‫سای = بورزن لای » فاعل سابیدن را‬                                                                ‫‪۲‬‬    ‫باشد ‪۳‬‬    ‫زبره شده‬


  ‫ساو یز = باواو بر وزن کاریز» شخمی ' کوند که ساینده باشد ‪ - ۱‬وامر باین معنی‌هم‬
 ‫هت یعنی بای ‪ - ۷‬و نوعی از فماش لفیس‬                        ‫خوش خلق نيك خو باشد ‪*. ۴‬‬
                                    ‫وطیف هم هت ‪.‬‬
                                               ‫ل‬
                                                                    ‫ساو یس = باناك بتحتانی رسیدموسین‬
 ‫سابیان ‪ ۲‬د آفتاب کیر را گوبند» وآن‬                                ‫وينبة‬    ‫بی نقطة زده» بمعنی چیزی گرانمابه باشد‬

  ‫چیزی باشد مافند چتری که ببراسدرشاهان‬                             ‫محلوح کرده که درجامه گذارند ‪ -‬وجامةٌ پنبه‬

‫لام از تاش آفتاب گردد ‪ -‬و درین‬        ‫ات‬‫مرند‬
                                    
==== leaf 541 ====
  ‫سابه خوش‬                                                                         ‫‪ ۷۱0‬اس‬

‫سابه بر ست د کنابه ازشخصی باشد‬                     ‫ساید = بر وزن اید » بمعنیريم آهن‬
 ‫که ببوسته فق وفجور کوارهای‌ناشاسته کند‪.‬‬             ‫است‪,‬وآن چ رکی باشدکه از آهن بیرون‌آید‪.‬‬
‫سا به زر سی ک=نابه از فق وفجور‬                     ‫سایس پنحم رواق ‪ -‬کنابه از‬
               ‫کوارهای نا شاسته کردن باشد ‪.‬‬        ‫کو کب مریخ است چه او در فلك پنجم‌میباشد؛‬
‫=شم بای ابجد وفتح رای‬
                    ‫سا به بر گ ب‬                   ‫ند که اسب رانگاه‬
                                                                  ‫ویرا‬
                                                                     ‫وسایی در عربی شگخصی‬
‫قرشت وسکون کاف »کیاهی است که چون شتر‬                              ‫دارد وتسمار ومحافظت آ نکند‪.‬‬

‫قدری اآزن بخورد بخواب رود ؛ و با بای فارسی‬           ‫مباشمع»تی‬      ‫زرن‬
                                                                      ‫وب‬‫سایش ‪۱۰‬‬
                                                                                 ‫ساییدن باشد ‪.‬‬
   ‫تهه‬ ‫سک‬ ‫وون‬
            ‫با گ‬ ‫پیر‬
                   ‫سایه پرود ‪-‬ک‬                    ‫سایگی ‏ کون الت کواف بتحتالی‬
 ‫بفراغت وآسودکی برآمده باشد ومحنت ومشقت‬            ‫و یبال شراىخورىرا گونند ‪5 ۴‬‬    ‫‪ ۰‬قدح‬   ‫رسده‬
‫نکشیده باشد ‪ -‬و کیامی هم هت که آنرا‬                            ‫وبمعنی کلاغ نیز بنظر آمده است‪.‬‬
‫از مردم مفت خور‬       ‫کنوابه‬
                           ‫بانخورش کنند ‪-‬‬          ‫سیاوس ‪ -‬بر وزن سالوی‪ ,‬اسبغول را‬
                                        ‫باشد ‪.‬‬     ‫بزر‬   ‫بی‬
                                                          ‫عفرو‬
                                                             ‫مرو‬
                                                               ‫است مع‬        ‫خنمی‬‫تآ‬‫گویند و‬
‫سا به پروران حم (‪ - )۱‬کنابه‬                                                    ‫قطونا خوانند ‪.‬‬
‫از دالهای انکور است که در خم بجهت شراب‬             ‫ساله = بر وزن مابه معروف است ‪- ۳‬‬
                                      ‫انداز ند ‪.‬‬    ‫ابه‬
                                                      ‫و نام دبوی هم بوده است ‪ -‬و جن را فسيز‬
‫سابه پوش = با بای فارسی بروزن‌باده‬                 ‫جوورهم هست ‪-‬‬
                                                              ‫‪۴‬ت‪-‬اوبه از فق‬
                                                                          ‫گونند ک‬
             ‫نوش ‪ ۰‬بمعنی سایبان وشامیانه باشد‪.‬‬
```


## [2026-09-04T19:15:19.743Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== GPL diminutive ===\"\ngrep -n -i \"diminutive\" GPL.txt | head -30"
}
```


### [2026-09-04T19:15:19.817Z] TOOL RESULT

```
=== GPL diminutive ===
64:DrnominativE Nouns. Noun of Unity, 169. Noun denoting Vessel or Receptacle, 170. The Relative Adjective, 170. The Abstract Noun of Quality, 171. The Diminutive, 172. Formation of Feminines from Masculines, 172. Number, 173. The Dual, 173. Regular Plurals, 173. Broken Plurals, 174. The Plural of the Plural, 180. The Declension of Nouns, 180. The Numerals, 181.
172:کدخدا رکتخدا : زرذشت as,‏ > زد ت ریچه ریحه the diminutive suffixes‏ در زج ot, eee‏
937:12), 7. Andak. Adjective اندك‎ ‘little, small, few’; اندکی‎ ‘a little, afew’. Andak is the diminutive of ,اند‎ As an adjective, it may either follow or precede the noun it qualifies. The following are examples of its use: قوت یافت‎ Hle Gail تا‎ ‘till he gained a small stock of strength’; دارم‎ wail کفافی‎ “1 possess scanty means’; آتش‎ اندف‌را‎ ‘a little (or, a small) fire’; بسیاری بود‎ Jue اندکی‎ ‘a little will serve as an indication of a great deal’; اندی جمال به از سیاری مال‎ ‘a little of beauty is better than an abundance of wealth’ ;. eS قناعت‎ با اندکی‎ ‘be contented with a little’.
1792:Note. Diminutives. In a few cases this suffix, annexed to substantives, forms diminutives ; but for such formations the unreduced Phl. suffix -ak (v. 7)) is more commonly employed; e.g. s yes ‘little daughter, little girl’ (from j<55 ‘daughter ’); مردمه‎ ‘manikin, con- temptible man’ (from پسره ز(مردم‎ ‘wretched boy’ (from }....).
1795:Diminutives. These suffixes are added to nouns to form diminutives.
1798:B) st, 2, رچه‎ BRT BRT The ch of the first of these forms is derived from a primitive affix -ach, meaning ‘tending (to), approaching’ (cf. S. Svityach ‘approaching whiteness, whitish ’, from éviti ‘whiteness’). The Phi. kanich- (Persian eS kaniz) ‘ young girl, maiden’ (Z. kanya+ach), may be taken as the type of such diminutive forms, and may account for the initial 7 of the suffixes. To the suffix -ich thus obtained the Phl. superadds the suffix -ak, thus forming ichak, whence the Persian -2ha, -ta, -iza, -izha. Again, by detaching the initial 2 of -icha, Persian forms the suffix -cha. The forms -cha, -tcha, -tja, are applicable to inanimate objects only; -tza and -2zha, to both animate and inanimate objects; e.g. asf ‘a little
2422:e) The Diminutive (220 opel or pees (اسم_‎
2423:§ 155, a. The usual measure of the diminutive, when it is formed from a noun of three letters, is فعیل‎ : e.g. Ese ‘Husain’ from حسن‎ ‘Hasan’. When the noun is qguadriliteral, the diminutive is of the measure فعیعل‎ ; aS مسیجد‎ from مسجد‎ ‘a mosque’, and if guingueliteral the fifth letter is dropped before forming the diminutive; e.g. JS سفر‎ ‘a quince’ makes its diminutive سفیرج‎
2424:b. The feminine terminations ری وحم‎ &c.; the relative termina- tion ری‎ and the dual and plural terminations; are all disregarded in forming the diminutives, but are added to them afterwards; e.g. 9 from قلعه‎ ‘a castle’ ; lope from Say fem. of اسود‎ > black ’; مسیلمه‎ from مسلمع‎ ‘a man’s name’; Speed from بهری‎ ‘belonging to Bagra’ (+23) ; مسیامان‎ eles ‘two Muslims’.
2425:Rem. The Arabic diminutive is not of very common occurrence in Persian.
```


## [2026-09-04T19:15:22.243Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD -ag ===\"\ngrep -n \"murwag\\|kanizag\\|kanīzag\\|-ag \\[\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== PHD afsan ===\"\ngrep -n -i \"afsān\\|afsan\\|whetstone\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"\ngrep -n -i \"afsān\\|afsan\\|whetstone\" NYB_vol2_glossary.txt | head -10\necho \"=== NYB -ak suffix ===\"\ngrep -n -i \"diminutive\" NYB_vol2_glossary.txt NYB_vol1.txt | head -20"
}
```


### [2026-09-04T19:15:22.351Z] TOOL RESULT

```
=== PHD -ag ===
PHD.txt:172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
PHD.txt:424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
PHD.txt:895:auspicious humurwag.
PHD.txt:2123:kanizag; v. daughter,
PHD.txt:2701:maid kanig, kanizag, paristar.
PHD.txt:4853:[138] mese murdir aay’ AV murwag 26 morwārīd -O*6 murwizag _ m» 55 murw wy Ww $6 murwnīš we NV 5G murnjén- 51136 murnjēnīdan 131936 mērd, murd
PHD.txt:5038:nay! kundāgīh kundāg nayestān! kandan kanīg kanīzag xwan-! xwandan! -gen
PHD_mackenzie.txt:1804: -ag [_kl I N -a] wand, arrow shaft.
PHD_mackenzie.txt:2216: --ag [_hi] an Eranian, Aryan.
PHD_mackenzie.txt:2545:  -ag [_kl 1M gwng, N guna] = 1l0n; sort, kind, form.
PHD_mackenzie.txt:2798: -ag [hnd)ck I N andaza] measure, manner; - i: like.
PHD_mackenzie.txt:2953:hu-murwag [hwmwlw)k ] auspicious.
PHD_mackenzie.txt:3074:  --ag [_kl I (P -g), N --a] eternal, perpetual.
PHD_mackenzie.txt:3326: -ag [-hi I N kiiha] saddle.
PHD_mackenzie.txt:3601: -ag [mwhlk I P mwhrg, N -a] bead, vertebra, piece (in backgammon,
PHD_mackenzie.txt:3705: --ag [1zymk ' I N --a] half, side, direction.
PHD_mackenzie.txt:3722: --ag [-k l I N --a] tried, experienced.
PHD_mackenzie.txt:3744: --ag [_kl I (M ng'r, N nigar)] image, picture, diagram.
PHD_mackenzie.txt:3797: -ag [-k ' ] residence, abode.
PHD_mackenzie.txt:4014: --ag [_kl I N "'a] pentad; hand, paw.
=== PHD afsan ===
PHD.txt:172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
PHD.txt:1864:Jable afsān.
PHD.txt:3831:story afsān.
PHD_mackenzie.txt:880:   afsan [)ps'n' I (M "ps)ng). N afsana] story, fable.
PHD_mackenzie.txt:891:   afsandan. afsan- ['#'n-tn l I N -] spread, scatter. sow.
PHD_mackenzie.txt:6530:   speech dus-gowisn; of...... thought             fable afsan.
PHD_mackenzie.txt:7638: soul frawahr, fraward, griw, gyan,     spread afSandan, wistardan.
PHD_mackenzie.txt:7650: sow afsandan, kistan.                 stand awistadan, estiidan, padan; ,.."
PHD_mackenzie.txt:7685:story afsan.                               suffer widiir(i)dan; V. endure.
=== NYB ===
546:Cf NP afsün, ausün ‘charm’, afsä ‘a wizard’, afsäyidan ‘to subdue, esp. by magic’, undoubtedly to be connected with NP sidan säy-, farsūdan farsäy (< *fra-) ‘to rub’, the magic treatment con- sisting of some special rubbing or strok- ing of the sword (< *upa-sü-, v. apa-). However, the corresponding OInd. vb. šā- means ‘to sharpen, to whet’ ($ita- ‘sharp’) a sense also attested in Ir: NP afsän, ausän ‘whetstone’; MPrs hswd = hassüd < *ham-süt "whetted' of a sword (Hen- ning, BSOAS XII, 1947, 45), directly to be compared with OInd (RV) sam-sä- ‘to whet’; thus apa-sütak could simply mean ‘sharpened, whetted’. The parallel epi- thet distak (g. v.) is not quite clear.
=== NYB -ak suffix ===
NYB_vol2_glossary.txt:1477:ēvarz ['dwlc'] review, muster, as a mili- tary term: ~ kartan to review, to muster (an. army) 2014; — [hence ēvarzīk kas probably *a man called up for military service, DkM 750!?]. — Originally ‘com- putation, calculation, account’, ef the following examples: ~ 4 x“atdydn 6 osti- kan the rulers’ calling of their trustees to account DkM 40416; étar *zarvan i (K drang) àivan (< K) andak, ~ züt; änöd dātavār (!) rāst here (in this world) the term of the court is short, and the account swift; there (in heaven) is & righteous *judgment DkM 5481-11; apar hān 4 andar nihvārēh ~ about the items (necessary) in combat FrP 14, heading. In all probability to be connected with NP dvàr(ah) ‘calculation, reckoning; an account-book’ (of which dvārjah, dvarcah ‘a cash-book, a book of receipts and dis- boursments, a diary, or register’ is the diminutive) < *abi-varda- SW form of *abi-varza-; dvdr : ēvarz, cf ēvāc, Evar, évar. (Wrong interpretation by Nyberg, TMK 69 sq., Pagliaro, Iscr. Dura-Europo 592. 595). — From varz-, v. varz, varzitan.
```


## [2026-09-04T19:15:39.709Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== GPL 1785-1800 ===\"; sed -n '1788,1800p' GPL.txt\necho \"=== AHD ko- ===\"; grep -no \"ko-\\. To sharpen[^]]\\{0,400\\}\" AHD_watkins1985.txt | head -5\ngrep -no \"kd-\\. To sharpen[^]]\\{0,400\\}\\|To sharpen, whet[^]]\\{0,400\\}\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-04T19:15:41.549Z] TOOL RESULT

```
=== GPL 1785-1800 ===
(1) Nouns. In the first case, it serves to form substantives ex- pressing, generally, an idea analogous to that of the stem; as چنی‎ ‘the hand with the five fingers’ (from (2) ‘five’); چیه‎ " left-handed’ (from
ده( 9 چشم و وود ‘source, borin,‏ چشمه ‘left’);‏ چپ ‘hand’); sls ‘tooth of a saw’‏ دست handle, haft, handful’ (from‏ jy) daily allowance,‏ ز) ‘relating to the day‏ روزه ‘tooth’); x‏ دندان (from‏
Derivation of Words 135
fast’ (so called because Muhammadans fast in the day, and not in the night) ; کوهه‎ ‘hump, bunch’ (from کوه‎ ‘hill’) ; آستره‎ ‘razor’ (from استر‎ the pres. stem of استردن‎ ‘to shave’); خنده‎ ‘laughing, laughter ’ (from رخند‎ the pres. stem of ز (خندیدن‎ x24 ‘a bat’ (lit. ‘night-flier’, from شب‎ ‘night’+ 42, pres. stem of پریدن‎ ‘to fly’).
Note. Diminutives. In a few cases this suffix, annexed to substantives, forms diminutives ; but for such formations the unreduced Phl. suffix -ak (v. 7)) is more commonly employed; e.g. s yes ‘little daughter, little girl’ (from j<55 ‘daughter ’); مردمه‎ ‘manikin, con- temptible man’ (from پسره ز(مردم‎ ‘wretched boy’ (from }....).
(2) Adjectives. In the second case the suffix forms adjectives ; ۰.2. دو روزه‎ ‘of two days’ (from روز+ 0۳۵0 دو‎ ‘day’); هر روزه‎ ‘of every day, daily, diurnal’; دو ماهه‎ ‘bi-monthly ’ (from ماه + دو‎ ‘month ae B29) دو‎ " double-faced’ (from روی‎ face 2 مر و‎ ot? ‘sufficient for five men’, &c. (from Ee + ۰(مرد‎
7) رت ی‎ >, st, =, ee Sas) and و‎
Diminutives. These suffixes are added to nouns to form diminutives.
a) ™— عم‎ This is the Phl. suffix -ah, noticed in the preceding paragraph. It is applicable to both animate and inanimate objects, and may also be annexed to adjectives; e.g. اسب‎ ‘a little horse, a pony’ (from آسپ‎ horse’); Wil ‘little’ (from اند‎ ‘as much’, &c.); Kale ‘a small dress or gown’ (from sole = Phil. jamak); کودت‎ ‘boy, lad, child’ (Phl. kutak; Z. kutaka ‘little’; cf. S. kshudraka); >,» ‘manikin’ (from 5,0); شیرد ينك‎ ‘sweetish ’ (from شپرین‎ " sweet ’, from shir ‘milk’ +i, v. 17); LoS ‘somewhat warm’ (from ۰ oie warm ’). (Sometimes the suffix is sS ha; e.g. مرککه‎ ‘manikin ’.)
Rem. In recent times the ending -2 is also used; e.g. بنديك‎ ‘a little slave’ (from si: ‘slave’), but this is uncommon.
B) st, 2, رچه‎ BRT BRT The ch of the first of these forms is derived from a primitive affix -ach, meaning ‘tending (to), approaching’ (cf. S. Svityach ‘approaching whiteness, whitish ’, from éviti ‘whiteness’). The Phi. kanich- (Persian eS kaniz) ‘ young girl, maiden’ (Z. kanya+ach), may be taken as the type of such diminutive forms, and may account for the initial 7 of the suffixes. To the suffix -ich thus obtained the Phl. superadds the suffix -ak, thus forming ichak, whence the Persian -2ha, -ta, -iza, -izha. Again, by detaching the initial 2 of -icha, Persian forms the suffix -cha. The forms -cha, -tcha, -tja, are applicable to inanimate objects only; -tza and -2zha, to both animate and inanimate objects; e.g. asf ‘a little
136 A ccidence
garden’ (from باغ‎ ‘garden’); ss#2o ‘small pot or cauldron’ (from دیغ‎ < Phi. deg); درتچه‎ ‘a little door or gate, a wicket’ (from در‎ ‘ door ‘3 spe, SST wy BST ww زه‎ pe ys ‘measles, roscola’ (from سرخ‎ ‘red’); پاکیزه‎ ‘pure, chaste, ieee &c. (from پا‎ ‘ pure’) ; مشکیزه‎ ‘a small (leathern) water-bag’ (from wl.t.).
=== AHD ko- ===
642:To sharpen, whet. Contracted from *koo-. 1. Suffixed extended form “kooi-no- in Germanic *haind in Old English hdn, stone: HONE!. 2. Perhaps Greek kénos, cone, conical object (< “a sharp-pointed object”): CONE. [Pok. Aéi- 541.
```


## [2026-09-04T19:15:50.402Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN hone ===\"; grep -no \"hone, n\\.[^]]\\{0,500\\}\" KLN_1966.txt | head -3\ngrep -no \"hone (n\\.)[^]]\\{0,400\\}\" KLN_1966.txt | head -3\necho \"=== KLN cone ===\"; grep -no \"cone, n\\.[^]]\\{0,500\\}\" KLN_1966.txt | head -3\necho \"=== SKT hone/cone ===\"; grep -no \"HONE[^]]\\{0,300\\}\\|CONE[^]]\\{0,300\\}\" SKT.txt | head -5"
}
```


### [2026-09-04T19:15:51.974Z] TOOL RESULT

```
=== KLN hone ===
=== KLN cone ===
=== SKT hone/cone ===
8788:HONE.
```


## [2026-09-04T19:15:56.074Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8780,8800p' SKT.txt\necho \"=== SKT cone ===\"; grep -n \"^CONE\\|Cone\\b\" SKT.txt | head -5\necho \"=== KLN hone ===\"; grep -n \"hone\" KLN_1966.txt | head -10\necho \"=== KLN kônos ===\"; grep -n \"kônos\\|kōnos\\|kônos\\|xâivoç\\|hän, 'stone'\" KLN_1966.txt | head -10"
}
```


### [2026-09-04T19:15:56.171Z] TOOL RESULT

```
Homicide:  see  Hamaa.
Homily ;  sec  Homogoneoiia.
Hominy,  ma:rc  prepared  for  food.  K  ~ Indiau.)     W.  ludiaii  AHAAmm*^^  pajdi com.
Hommook ;  sec  Hump.
Homoeopathy ;  »ec  Horaogeaeott*
Homogeneous,  of  the  same  b throughout.  <,Gk.)  Engluhed  fron  C (//lo^ctijt.  of  the  same  raoe.*Ck^  i# same  (c&gnate  with  E.  8am«>,  and  y^i a  nice  (cognate  with  E  Klnl  S^  1* AofHO'logouJ,  corrcsponiling,  U- saying,  Xiytiv^  to  aay  ;  ham-, in  sound,  from  Zvvt:~   -  t —
homily.   (L.— ;  "vjVW.*
d^Aja,    a  living    lt„  o    coi!
HONE.
bcmHy.-Glt  ifuXct,  a  throng. j*^f.  like,  same,  together, 8*n3e ;  atiU  IX17.  ttArj,  a .lu  MAiiK,  to  compress,  shut  in. .) irvoTUL^hv      r,\(_)    Englished  from -s  in  feeling  or  con- like;  waeiiy,  aorist of  ««M'x««*'.  u*  kufTer.    See  8*md  And kthoft     And  Ke  Homllr. HOQ)0^   (£.)     AS.    ^Jrt,  a  hone,  (with _     from  d  lo  long  e,  as  iii  d^rin,  bone).
>  led.    Jknn,   SweiL    ^^ ;    Skt    fdna.    a *^'  «oo��  EromjT,  tu  sharpen ;  Gk,  jHlrt-of,
>  eoBT,  poik.    Sec  Coae. Bonest ;  see  Honour.
Ho&ey.  {£.)    Si.K  Auhi.    AS. ^«nr^'.
Dd  Aamir,  I  eel.  hunaug,  Don.  honnhig,
*    kcHing.  G.  homg.      Pet  haps  orig.
UD-lake/  or  like  broken  lice;  cf.  Skt,
I.  i^rsia,  broken  tioe.
boneyoomb.    <El.)    A.  S.  hunigtamb,
\%mttj'^omh-»  where  com6  is  the  usual  £.
Ihowh  the   likeness  to  b  (om^  is
ihcr  CuucafttL
=== SKT cone ===
2797:Canopy ;  sec  Cone.
3698:Coin.  (F.-L.)  M. E. «!>(.- O.K. f«w, a  werJge,  stamp  on  a  coin,  a  coin  (stamped by  means  of  a  wedge)  *L.  cuntum,  ace. of  cumns,  a  wedge.     Allied  to  Cone.
3921:Cone.  (F.  -  L.  -  Gk.) (pMMi.  ~Gk.  »aivos,  a  cone, L.  I'UHtus,  a  we<lgc ;   A.  S. CVK.-\.)
5160:Disease ;  see  Cone.
=== KLN hone ===
97:The  transliteration  for  Semitic  words  contained  in  the  etymologies  of  this  dictionary  is  such that  it  renders  exactly  every  consonant,  vowel  and  diacritical  sign.  It  happens  for  the  first  time that  the  Hebrew  and  Aramaic  words  quoted  in  an  etymological  dictionary  are  transliterated according  to  a  system  which  makes  it  possible  to  retransliterate  these  words  into  their  original characters,  including  all  the  phonetic  signs  particular  to  Hebrew  and  Aramaic.  (See  the  follow¬ ing  Rules  for  Transliteration.)
1162:Derivatives:  abid-ing,  adj.,  abid-ing-ly,  adv. Abies,  n.,  a  genus  of  trees,  the  true  fir  (bot.)  — L.  abies,  ‘silver  fir’,  cogn.  with  Gk.  fiffiv  (acc.), ‘silver  fir’,  ’Affix)),  name  of  Southern  Russia, lit.  ‘a  region  of  firs’.  Cp.  abeto. abietic,  adj.,  pertaining  to  the  crystalline  acid C20H30O2  (chem.)  —  Formed  with  suff.  -ic  fr. L.  abies,  gen.  abietis,  ‘silver  fir’.  See  prec.  word. Abigail,  fem.  PN. ;  in  the  Bible,  the  wife  of  Nabal, later  of  David.  —  Heb.  Abhigayil,  lit.  ‘my  father is  rejoicing’,  fr.  abh,  ‘father’  and  gil,  ‘to  rejoice’. For  the  first  element  see  Aboth.  The  second  ele¬ ment  is  rel.  to  Arab,  jdla,  ‘he  went  round’  and to  Heb.  galdl,  ‘he  rolled,  unfolded’;  see  gelilah. The  use  of  the  name  in  the  sense  of  ‘waiting maid’  is  due  to  the  passage  ini  Sam.  25 : 35,  where Abigail  calls  herself  a  ‘handmaid’, abigeat,  n.,  cattle  stealing  (civil  law).  —  L.  abi- geatus,  fr.  abigeus,  ‘cattle  stealer’,  fr.  abigere, ‘to  drive  away’,  fr.  ab-  and  agere,  ‘to  drive’ ;  see agent.  The  change  of  Latin  d  (in  agere)  to  f  (in  ab¬ igere)  is  due  to  the  Latin  phonetic  law  according to  which  in  the  unaccented  open  radical  syllable of  the  second  element  of  compounds,  original b  becomes  i.  Cp.  accident,  adhibit,  ambiguous, ancipital,  anticipate,  artifice,  comfit,  conceive, consilient,  constitute,  contiguous,  council,  de¬ ceive,  deciduous,  deficient,  delicious,  delitescent, desipient,  destine,  destitute,  difficulty,  disciple, dissilient,  efficient,  elicit,  exhibit,  Illicium,  inci¬ dent,  incipient,  inhibit,  inimical,  institute,  insipid, insipient,  irritate,  ‘to  make  null  and  void’,  navi¬ gate,  obstinate,  Occident,  occiput,  office,  partici¬ pate,  precipice,  prodigal,  proficient,  prohibit,  pros¬ titute,  receive,  recidivist,  resilient,  resipiscence, restitute,  reticent,  substitute,  superficies,  super¬ stition,  supplicate,  transilient. ability,  n.  —  ME.  abilite,  fr.  OF.  ablete,  habilite (F.  habilite),  fr.  L.  habffitatem,  acc.  of  habilitas, ‘aptitude,  ability’,  fr.  habilis,  ‘that  may  be  easily handled  or  managed,  suitable,  fit,  proper’.  See able  and  -ity.
1256:Derivative:  abstersive-ness,  n. abstinence,  n.  —  OF.  (=  F.),  fr.  L.  abstinentia, fr.  abstinens,  gen.  -entis.  See  next  word  and  -ce. abstinent,  adj.  and  n.  —  OF.  (=  F.),  fr.  L.  absti- nentem,  acc.  of  abstinens,  pres.  part,  of  absti¬ nere,  ‘to  refrain  from’.  See  abstain  and  -ent.  The change  of*Latin  e  (in  tenere)  to  i  (in  abs-tinere) is  due  to  the  Latin  phonetic  law  according  to which  in  the  unaccented  open  radical  syllable  of the  second  element  of  compounds,  original  e becomes  i.  Cp.  assiduous,  continent,  continuous.
1321:Derivatives:  accelerat-ed,  adj.,  accelerat-ed-ly, adv.,  acceleration  (q.v.),  accelerat-ive,  adj.,  ac- celerat-or,  n.,  accelerat-ory,  adj. acceleration,  n.  —  L.  accelerated,  gen.  -onis,  ‘a hastening,  acceleration’,  fr.  acceleratus,  pp.  of accelerare.  See  prec.  word  and  -ion. accelerometer,  n.,  an  instrument  for  measuring acceleration.  —  A  hybrid  coined  fr.  L.  accele¬ rate,  ‘to  hasten’,  and  Gk.  pixpov,  ‘measure’.  See accelerate  and  meter,  ‘poetical  rhythm’, accent,  n.  —  F.,  fr.  L.  accentus,  fr.  ad-  and  can- tus,  ‘tone,  melody’.  See  cant  and  cp.  enchant, incantation.  The  change  of  Latin  d  (in  cdntus ) to  €  (in  ac-cintus)  is  due  to  the  Latin  phonetic law  according  to  which  in  the  unaccented  and closed  radical  syllable  of  the  second  element  of compounds,  original  a  becomes  £.  Cp.  concent, precentor,  succentor.  Cp.  also  abject,  accept, adept,  ascend,  biceps,  biennial,  centennial,  coerce, commend,  concept,  confect,  confection,  confess, congress,  conjecture,  consecrate,  defect,  degres¬ sion,  deject,  descend,  discerp,  disperse,  eject,  ex¬ cept,  excerpt,  execrate,  exercise,  forceps,  im- petrate,  incendiary,  incense,  incentive,  incept, incest,  inept,  inerm,  inert,  infect,  inject,  integer.
1378:Derivatives :  accusativ-al,  adj .,  accusative-ly,  adv. accuse,  tr.  v.  —  ME.  acusen,  fr.  OF.  acuser  (F. accuser),  fr.  L.  accusare,  ‘to  accuse’,  fr.  ad-  and causa,  ‘cause,  lawsuit’,  which  stands  for  *caud- ta-,  and  is  rel.  to  cudere,  ‘to  strike,  beat’.  See cause  and  cp.  excuse,  recusant,  recuse.  The change  of  Latin  au  (in  causa)  to  u  (in  ac-cusare) is  due  to  the  Latin  phonetic  law,  according  to which  in  the  unaccented  radical  syllable  of  the second  element  of  compounds,  au  becomes  u. Cp.  conclude ,  exclude,  occlude.
1478:Derivative:  acquiescent-ly,  adv. acquire,  tr.  v.  —  L.  acquirere,  ‘to  seek  in  addition to,  acquire’,  fr.  ad-  and  quaerere,  ‘to  seek, search’.  See  quaere  and  cp.  acquisition,  conquer, conquest,  inquire,  require,  request.  The  change of  Latin  ae  (in  quaerere)  to  i  (in  ac-quirere)  is due  to  the  Latin  phonetic  law  according  to  which in  the  unaccented  and  open  radical  syllable  of the  second  part  of  compounds,  ae  becomes  i.  Cp. -cide,  circumcise,  collide,  concise,  conquistador, decide,  elide,  excide,  excise,  ‘to  cut  out’,  incise, iniquity ,  perquisite,  precise ,  succise .
1514:•wopfcooy,  n.,  the  use  of  the  pictorial  represen¬ tation  of  an  object  as  the  phonetic  sign  of  the initial  sound  or  syllable  with  which  the  name  of that  object  begins.  —  Compounded  of  aero-, Wd^3k.  -pxavla,  fr.  <pcov4),  ‘sound,  voice’.  See
1874:effroi),  fr.  esfreer,  *esfreier.  See  prec.  word, affricate,  n.  ( phonetics ).  —  L.  affricatus,  pp.  of affricare,  ‘to  rub  against’.  See  affricate,  v. affricate,  tr.  v.,  to  rub ;  to  grate  on.  —  L.  affricatus, pp.  of  affricare,  ‘to  rub  against’,  fr.  ad-  and  fri- care,  ‘to  rub’.  See  friction  and  verbal  suff.  -ate. Derivatives:  affricat-ed,  adj.,  affricat-ion,  n., affricat-ive,  adj.
2381:versity.  —  L.  alumnus,  ‘a  nursling,  foster-son, disciple’,  for  *alo-menos ,  prop.  pass.  pres.  part, of  alere,  ‘to  nourish’ ;  see  old  and  cp.  alt.  For the  suff.  *-menos  cp.  Gk.  -pevo?,  the  suff.  of  the med.  and  pass,  part.,  and  L.  fe-mina ,  ‘woman’, lit.  ‘suckling  (woman)’,  and  see  feminine.  Cp. also  the  suffixes  of  the  words  Aeschynomene, calumny,  catechumen,  clement,  column,  ecumen¬ ic,  energumen,  hapax  legomenon,  hegumen, noumenon,  phenomenon,  prolegomenon, alurgite,  n.,  a  purplish  manganese  mica  (mineral.) —  Formed  with  subst.  suff.  -ite  fr.  Gk.  AXonpy/j?, ‘genuine  purple  dye’,  lit.  ‘wrought  in  or  by  the sea’,  which  is  compounded  of  a X?  (fem.),  ‘sea’, and  sp-fov,  ‘work’.  See  halieutic  and  ergon, alushtite,  n.,  a  hydrous  aluminum  silicate  (min¬ eral.)  —  Named  after  Alushta  in  the  Crimea. For  the  ending  see  subst.  suff.  -ite. aluta,  n.,  a  kind  of  soft  leather.  —  L.,  for  alu-ta, lit.  ‘leather  prepared  by  means  of  alum’,  rel.  to alumen,  ‘alum’.  See  alum, alutaceous,  adj.,  resembling  aluta.  —  L.  alutacius, fr.  aluta.  See  prec.  word  and  -aceous. alveolar,  adj.,  pertaining  to  alveoli.  —  Formed with  suff.  -ar  fr.  L.  alveolus.  See  alveolus, alveolate,  adj.,  pitted  with  small  cavities,  as  a honeycomb.  —  L.  alveolatus ,  fr.  alveolus.  See next  word  and  adj.  suff.  -ate. alveolus,  n.,  a  small  cavity.  —  L.  alveolus ,  dimin. of  alveus,  ‘a  hollow,  cavity’,  which  is  rel.  to  al- vus,  ‘belly’,  and  cogn.  with  Gk.  auX6?,  ‘tube, pipe’,  gv-auXo?,  ‘channel,  riverbed’,  auXtov, ‘hollow  way,  defile,  ravine,  glen,  channel,  strait’, OS1.  ullji,  Lith.  aulys,  Lett,  aulis,  ‘beehive’,  lit. ‘a  trunk  hollowed  out’,  OSlav.  ulica,  ‘defile; courtyard’,  Lith.  aulas ,  Lett,  aule,  ‘leg  of  a boot’,  OPruss.  aulis,  ‘shinbone’.  Arm.  ui,  uli, ‘way’,  yli,  ‘pregnant’.  For  the  correspondence of  Gk.  xuXo  ?  and  L.  ah  us,  alveus,  cp.  Gk. veupov,  ‘nerve’,  with  L.  nervus ,  of  s.m.,  and Gk.  7ra0po?,  ‘little,  small’,  with  L.  parvus ,  of  s.m. For  the  ending  see  suff.  -ole.  Cp.  carol,  hy¬ draulic.
2989:Derivative:  antiphlogistic,  n. antiphon,  n.,  a  versicle  sung  responsively.  —  F. antiphone,  fr.  ML.  antiphona,  fr.  Gk.  dvxitpoiva, neut.  pi.  of  dvxicpotvo;,  ‘sounding  in  answer to’,  mistaken  for  fem.  sing.;  fr.  avxi,  ‘over against,  in  response  to’  (see  anti-),  and  (pew;, ‘voice,  sound’ ;  see  phone,  n.  Cp.  anthem,  which is  a  doublet  of  antiphon.
=== KLN kônos ===
```


## [2026-09-04T19:16:10.409Z] TOOL CALL #39: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T19:16:10.415Z] TOOL RESULT

```


```


## [2026-09-04T19:16:15.406Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1eh%E2%82%82-",
 "prompt": "Give the full reconstruction entry: root form, gloss, whether it means \"to sharpen/whet\", and all listed descendants (Sanskrit śāna-, Avestan saēni-, Greek κῶνος, Latin cōs, Germanic *hainō / Old English hān). Quote exactly."
}
```


## [2026-09-04T19:16:16.356Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hone",
 "prompt": "Quote the full etymology of \"hone\" (noun and verb), including the PIE root cited and cognates (Old Norse hein, Sanskrit sana, Greek konos)."
}
```


### [2026-09-04T19:16:17.084Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T19:16:21.917Z] TOOL RESULT

```
# Etymology of "Hone"

## Noun
"Old English _han_ 'a stone, rock, (boundary) stone,' from Proto-Germanic _\*haino_" with origins in PIE _\*ko-_ meaning "to sharpen, whet."

By Middle English (early 14c.), the term acquired its specialized meaning: a fine-grained stone for sharpening tools requiring delicate edges.

## Verb
The verb form emerged in 1788, meaning "rub or sharpen on or as on a hone," derived from the noun. Interestingly, earlier Middle and Old English versions (_hene_ and _hænan_) had a different sense: "cast stones at."

## Note on Cognates
The web page mentions Old Norse _hein_ as a cognate but does not cite Sanskrit _sana_ or Greek _konos_. The content provided contains only the sources explicitly listed in the article.
```


## [2026-09-04T19:16:26.045Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/hone",
 "prompt": "Quote the English noun \"hone\" etymology section in full: Proto-Germanic form, PIE root cited, and cognates listed (Sanskrit, Avestan, Greek, Latin)."
}
```


## [2026-09-04T19:16:28.060Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%E1%BF%B6%CE%BD%CE%BF%CF%82",
 "prompt": "Quote the Ancient Greek κῶνος etymology in full: the PIE root, the meaning(s) of κῶνος, and the cognates listed (Sanskrit śāna, Avestan saēni-, Old English hān, Latin cōs)."
}
```


### [2026-09-04T19:16:31.746Z] TOOL RESULT

```
# Etymology of "Hone" (Noun)

Based on the Wiktionary content provided, here's what the etymology section states:

The entry traces "hone" back through: "From Middle English _hon_ ("whetstone"), from Old English _hān_, from Proto-Germanic _*hainō_" 

The Proto-Indo-European root cited is: "_*ḱeh₃i-_ ("to sharpen")"

However, the document lists only **Ancient Greek and Persian cognates**, not Sanskrit or Avestan:

- Ancient Greek: _κῶνος_ (kônos, "cone")
- Persian: _سان_ (sân, "whetstone")

The article does not provide Sanskrit or Avestan cognates for this particular noun etymology. The PIE root and the specific cognates mentioned are limited to what appears above.
```


### [2026-09-04T19:16:33.862Z] TOOL RESULT

```
# Ancient Greek κῶνος Etymology

Based on the Wiktionary article, here's the etymology information:

**PIE Root:** The word is traditionally derived from Proto-Indo-European *ḱóh₃nos, stemming from the root *ḱeh₃- meaning "to sharpen."

**Meanings of κῶνος:** The article lists six primary definitions:
1. Pine cone
2. Edible seed of a pine tree
3. Pine tree
4. Cone or peak of a helmet
5. Geometric cone
6. Iron pole for piling grain in conical shape

**Cognates Listed:** The etymology section provides these related words:
- Sanskrit śāṇa (whetstone)
- Latin cōs (whetstone)
- Latin catus (clever, sharp)

**Note:** The article does not mention Avestan saēni- or Old English hān as cognates. It does note scholarly debate about whether κῶνος derives from PIE or represents a Pre-Greek borrowing, with support cited from Schwyzer, Furnée, and Beekes for the latter theory.
```


## [2026-09-04T19:16:41.536Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%AF%D9%86",
 "prompt": "Quote the Persian entry سودن: etymology (Middle Persian form, Proto-Iranian root, present stem سای), meanings, and any related terms such as ساییدن, فرسودن."
}
```


## [2026-09-04T19:16:43.367Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D8%A7%D9%86",
 "prompt": "Quote the Persian entry افسان: is there a sense 'whetstone'? Give the etymology (prefix *abi- + root), any Middle Persian form, and related forms فسان, سان."
}
```


### [2026-09-04T19:16:45.477Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T19:16:47.888Z] TOOL RESULT

```
# Persian Entry: سودن (sūdan)

Based on the Wiktionary content provided, here's what we know about this verb:

## Definition
The word **سودن** functions as "a literary form of ساییدن" (sāyīdan/sâyidan), meaning to benefit or profit in literary Persian.

## Pronunciation
The entry shows pronunciations across Persian dialects:
- Classical: /suː.ˈdan/
- Dari (formal): [suː.d̪än]
- Iranian (formal): [suː.d̪æn]
- Tajik: [su.d̪än]

## Verb Structure
The conjugation table reveals:
- **Present stem**: سای (sây) or ساو (sâv)
- **Past stem**: سود (sud)
- **Present participle**: ساینده (sâyandé)
- **Past participle**: سوده (sudé)

## Related Terms
The entry references **ساییدن** as the more common form and mentions **فرسودن** implicitly through the broader verb family structure.

The word represents a classical/literary variant within Persian's rich verbal conjugation system, featuring standard indicative, subjunctive, and imperative moods across all persons and numbers.
```


## [2026-09-04T19:16:51.192Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%A7%DB%8C%DB%8C%D8%AF%D9%86",
 "prompt": "Quote the Persian entry ساییدن in full: etymology (Middle Persian, Proto-Iranian root, PIE root), meanings, and cognates."
}
```


## [2026-09-04T19:16:53.002Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%A7%D9%86",
 "prompt": "Quote the Persian entry سان: is there a sense 'whetstone'? Give its etymology and any cognates (Sanskrit śāṇa, Greek κῶνος, Old English hān)."
}
```


### [2026-09-04T19:16:56.938Z] TOOL RESULT

```
# Persian Entry: ساییدن (sāyīdan)

## Etymology

The word is "inherited from Middle Persian (swtn' /⁠sūdan⁠/, 'to rub'), present stem (sʾd- /⁠sāy-⁠/); regularized from the older infinitive سودن (sūdan / sudan)."

The ultimate origin traces to "Proto-Iranian *sauH- ('to rub'), from Proto-Indo-European *ḱeh₃(i)- ('to sharpen')."

## Meanings

The verb has three primary definitions:
1. "to rub, grind"
2. "to pulverise"
3. "to wear away, erode"

## Cognates

Related words across languages include:
- Central Kurdish سوون (sûn, "to rub; to sharpen")
- Sanskrit शा (śā, "to sharpen")
- Latin catus ("clever")
- English hone
```


### [2026-09-04T19:16:58.425Z] TOOL RESULT

```
# Persian سان (sān) - Whetstone Entry

Yes, the Persian entry includes a whetstone sense.

**Etymology:** The whetstone meaning derives from "Proto-Indo-Iranian [Term?]" according to the source material.

**Cognates:** The document lists "Sanskrit _[शाण](/wiki/%E0%A4%B6%E0%A4%BE%E0%A4%A3#Sanskrit "शाण")_ (śāṇa, 'whetstone')" as a cognate.

The entry does not mention the Greek or Old English terms you referenced. The Wiktionary article only documents the Sanskrit connection under Etymology 2 for the whetstone definition.
```


## [2026-09-04T19:17:05.556Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/-%DA%A9",
 "prompt": "Quote the Persian suffix -ک (-ak) entry: its meaning (diminutive?), etymology (Middle Persian -ag, Proto-Iranian *-aka-, PIE *-kos), and examples."
}
```


## [2026-09-04T19:17:07.045Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-kos",
 "prompt": "Quote the PIE suffix *-kos entry: meaning/function, and descendants including Indo-Iranian *-kas / Sanskrit -ka, and whether a diminutive function is mentioned."
}
```


### [2026-09-04T19:17:07.662Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T19:17:10.980Z] TOOL RESULT

```
# PIE Suffix *-kos Analysis

**Meaning/Function:**
"Creates deadjectival and desubstantival adjectives denoting the characteristic of, typical of, pertaining to."

**Key Descendants:**
- Proto-Indo-Iranian: *-kas (with further descendants listed)
- Sanskrit inherited this through the Indo-Iranian line

**Diminutive Function:**
No diminutive function is mentioned in this entry. The suffix is described solely as creating adjectives with characteristic or pertaining meanings, with no reference to diminutive applications.
```


## [2026-09-04T19:17:14.770Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9#Persian",
 "prompt": "Is there a Persian suffix ک (-ak) entry? Quote its definition (diminutive) and etymology, including any Middle Persian -ag form."
}
```


## [2026-09-04T19:17:15.730Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%95#Sanskrit",
 "prompt": "Is there a Sanskrit suffix -क (-ka / -aka) entry? Quote its definition (diminutive / adjectival) and etymology."
}
```


### [2026-09-04T19:17:18.568Z] TOOL RESULT

```
Based on the Wiktionary page provided, there is no entry for a Persian suffix ک (-ak) with a diminutive definition. The page only documents ک as a letter in various languages including Persian, where it is described as "The twenty-fifth letter of the Persian alphabet, called کاف and written in the Arabic script."

The content does not include any information about a diminutive suffix form or Middle Persian etymology for this character.
```


### [2026-09-04T19:17:21.380Z] TOOL RESULT

```
Based on the content provided, there is **no dedicated entry for a Sanskrit suffix -क (-ka / -ka)** with definitions for diminutive or adjectival use.

The page only covers **क (ka)** as:
1. A Devanagari letter (consonant)
2. An interrogative pronoun ("who," "what," "which")
3. Various nouns (names, soul, sun, fire, happiness, water, etc.)

The etymologies provided trace the pronoun back through Proto-Indo-Aryan, Proto-Indo-Iranian, and Proto-Indo-European, but do not address suffix functions or diminutive/adjectival applications of this character form.
```


## [2026-09-04T19:17:31.561Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index sāy/sān ===\"\ngrep -n -i \"SAYIDAN\\|SAIIDAN\\|SAN\\b\\|AFSAN\\|FASAN\\|SUDAN\" incoming/ARY/ARY_latin_index_pages.txt | head -20\necho \"=== ARY persian ساییدن ===\"\ngrep -n \"ساییدن\\|سائیدن\\|افسان\\|سودن\" incoming/ARY/ARY_pages.txt | head -20"
}
```


### [2026-09-04T19:17:31.623Z] TOOL RESULT

```
=== ARY latin index sāy/sān ===
571:Sy Sacsan glygsl 9 a cuales glandly dod Ha y lead glitih 1 6 ch yry
594:Wace 5h s rey tab gs diay lig ly te San (LYCIANS) lay y (PALAICS)
1037:ape gt ISH ty 5d (U3 S910 J dhe 32.05.94) dy! De dle 99 stingy OLS san
1103:shaw yg SAN!
1649:OSTU, OSLA + ASAN, ASMAN ——(AVESTAN) (gly!
1651:OSBLOK (RUSSIAN) gs, ASAN, ASRI (SANSKRIT) <4 Sie
2306:Mabel 72 pS lg bE bag y gee Bin py chats elicdl » or) gob sluSan sp Ly ajly |
2544:SHKAUT, LATVIAN) (3) 93 NIOSAN, FNEHAN
3929:PRIMAVERA SPANISH) pistol VASAR, VASAN, :(SANSKRIT) cu Site
4054:DVACET CZECH) Sx KSAN ARMENIAN) gs}
4085:BAZEN (BOHEMIAN) san » BIM, BIMGEN, (PAHLAVI) 5 shy
4427:FIMTAN * HINGE-TASAN (ARMENIAN) yo)
6210:BUCK: 676 JESAN:(OLD HIGH GERMAN) pS gas
6307:; dh pp date San SF Lp 4 Sadke Slok5 2203 ae
7107:VAs tabi chy SAN, SPAVATI. ~_—:(SERBIAN) 1g. pe
7641:DOU  (-4L!}(OLD SAXON) ff pS TSAN :(TOKHARIAN A) A 555
7642:DAW — (4Lt}(OLD FRISIAN) oS 5.3 TSAN, TSENE (TOKHARIAN B)B jiu
8282:KIOSAN (OLD PERSIAN) skool 534,
8284:CBOSAN (OLD ENGLISH) pS 535i! (PAHLAVI) 5 3h,
8296:MACKENZIE: KAUSJAN, KIUSAN :(GOTHIC) S
=== ARY persian ساییدن ===
1108:خط نویسی» افسانه‌ها و تاریخ مردم خود را در حافظه‌ی خود جا داده و در بزم‌ها یا مراسم رسمی با
1334:۵ توضیحات افسانه مانند درباره‌ی ریشه‌ی واژه‌ها را باید با شک و تردید فراوان مورد
9995:سان سومان افسان / ۳۳۹
10009:واژه‌های فارسی "ساییدن" و آسودن" و "بسودن" نیز از همین واجریشه‌اند (۳۵۳073790 :542)
```


## [2026-09-04T19:17:33.368Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON part2 suffix ک تصغیر ===\"\ngrep -n \"پسوند\" MON_part2.txt | head -20\necho \"=== MON مرغک ===\"\ngrep -n \"مرغک\\|کنیزک\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-04T19:17:33.449Z] TOOL RESULT

```
=== MON part2 suffix ک تصغیر ===
2901:[«ه«(پس.) پسوند دال بر آغشتگی و 
16694:کا: ۸ ( یس پس.) بصورت پسوند به آخر اسم یا 
21835:گرد» جردا بصورت پیشوند یا پسوند مکان 
29154:گار؛ ۱۳9 - کار» یب.] (سد.) پسوندی است 
29413:گاله: (0)ه2۱ه (ب.) پسوند دال بر تصغیر 
29812:پسوند مکان استعمال شود. (.) هر خانه از 
36870:پسوند در ترکیبات ات ی رک 
55218:پسوند» پساوند. مزید مقدم: پیشونده 
66426:خود اسم مکان است و احتیاج به پسوند 
66428:(پسوند مکان) ملحق کنند. 
70286:مکان است. مع‌هذا در تداول فارسی پسوند 
72692:نا ک: *78 (بس.) پسوندی است که با الحاق 
72696:ضح.- بعضی پنداشته‌اند که این پسوند فقط 
81171:پسوند «ين» به صفت مطلق ملحق نمی‌شود 
81180:کامل دارد و احتیاجی به پسوند «ین» نیست. 
83181:(پس.) بصورت پسوند آید به معنی فوق: 
83220:بصورت پسوند آید به معانی ذیل: دال بر 
83231:پسوند به اسماء عام و یز به اسماء خاص. 
83859:وال: 31 (سد.) پسوندی است به معنی 
83970:رنک» لون. (پس.) بصورت پسوند آید به 
=== MON مرغک ===
MON_part1.txt:4361:طلا. نامی از نام‌های زنان و کنیزکان ترکث. 
MON_part1.txt:59973:مادری. خال بیر» دابی‌بیر. کنیزکی که 
MON_part1.txt:84584:شخش: 808 [- شخیش] (امر.) مرغکی 
MON_part2.txt:4873:مونث فتی. زن جوان. کنیزکك (غم.)؛ ج 
MON_part2.txt:12465:خدمتکار؛ کنیزکك» ج. (به سیاق فارسی) 
MON_part2.txt:27533:کنیزک: -۸۵]2 (ا.مصف.) زن خرد (عم.) 
MON_part2.txt:66620:که کنیزکان را برای فروش بر آن بر آورند.
```


## [2026-09-04T19:17:41.505Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY 9985-10020 ===\"\nsed -n '9985,10020p' incoming/ARY/ARY_pages.txt\necho \"=== ARY pdf page tag ===\"\nawk 'NR<10010 && /pdf page/ {last=$0; ln=NR} END{}' incoming/ARY/ARY_pages.txt\ngrep -n \"pdf page\" incoming/ARY/ARY_pages.txt | awk -F: '$1<10010' | tail -3"
}
```


### [2026-09-04T19:17:43.094Z] TOOL RESULT

```
=== ARY 9985-10020 ===
13 بکاناا بانق21 برهان قاطع + 1.۷۳
یادداشت,
۱ بازگشت به؛ سرد.
۲ واژه‌ی "کالری" (۸1.0778)) نیز از همین واجریشه است.
۳ چم این واژه در زبان ساکسونی کهن: سوختن.
چم این واژه در زبان‌های رومانس و زبان ولزی: گرم) گرما.
چم این واژه در بان ژرمنی: نیم‌گرم» ولرم» ملایم.
چم این واژه در زبان سانسکریت: پائیز,
واه
[pdf page 338]
سان سومان افسان / ۳۳۹
اوسنابی (48724/4): ادا
تخاری 8 (8 [(70727۸-۸): نک ریا پسگشت‌ها 5
سانسکریت (54(/5/7): 81۸1۸85 ,5307۸ 2 ۶0090
پونانی (0520): 05 9 (110(5) 8/7
لانین (7100ا): 678 ,۲05 6 (0305) 00/5
ایتالیایی (مانلم؟): 07 6 (130۷5) +57
ایسلندی کهن (54(/010۸40 :۰۰۰33813۷ 805,08۱ :5( 4 للملا
انگلیی کهن (تکلا8۷0 0ا0): 110 برهان قاطع : ۱۷۶-۷
انگلیسی (ل5لا6(/0): 1102 فرهنگ معین + ۸۱۰
دانمارکی (7ل0۸(۷/5): 118 لفت‌نامه دهخدا : ۱۳۳۶۶
سوئدی (8/80/57): 1
یادداشست:
۱ چم این واژه در زبان یونانی: مخروط درخت کاج.
واژه‌های فارسی "ساییدن" و آسودن" و "بسودن" نیز از همین واجریشه‌اند (۳۵۳073790 :542)
اوستایی (4۲574۸): ۸۸۰ ,۸8522 3۸
پهلوی (بابلهه): 5۸ ساکونی کهن 54000۷0 ۰:00 5831۸8۷
ی با کردی (130/5): 4 باه فریزی گهن (/(۴۴/514 0ا0): 51۸
1۹ " بلرچی (اپل الم , 6 ,ل52 آلمانی کهن (08741۸0 107 01):
افغانی (پشتو) رس 81۷1۸۱۷ ۸رد
تخاری 8 (8 70827۸4۸): 30 آنمانی (08821۸۷): لد انا ان
سانسکربت (8/5877): ی انگلیی کهن (2(/050 ۰:0۵ 8213۸۷
یرنانی 078570): 541 انگلیسی (57/ا8/0): الا ادن
لاتین (712ها): 5۳1۸ دانمارکی (0۸/[574): لول رن
گریکه (00777/0): ادن سوئدی (817570150): 5.۸
ایسلندی کهن (504010704۵7 0ا0): نروژی (/0/0050140: لاهن
=== ARY pdf page tag ===
9930:[pdf page 336]
9961:[pdf page 337]
9994:[pdf page 338]
```


## [2026-09-04T19:18:00.417Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON part2 16690-16710 ===\"\nsed -n '16690,16712p' MON_part2.txt\necho \"=== MON کنیزک ===\"\nsed -n '27530,27537p' MON_part2.txt\necho \"=== ARY suffix ===\"\ngrep -n \"پسوند\\|تصغیر\" incoming/ARY/ARY_pages.txt | head -20"
}
```


### [2026-09-04T19:18:00.497Z] TOOL RESULT

```
=== MON part2 16690-16710 ===
را ۱۳ 
این حرف را بنام کاف و کاف تازی و کات 
عربی خوانند و بصورت: کك: 5 5 کت 
نوسند: درکك» کس کار» مکان» فلک. 
کا: ۸ ( یس پس.) بصورت پسوند به آخر اسم یا 
صفتی که پجای اسم نشیند بلحق گرده و آن 
به معناهای ذیل آید: تصغیر» کوچکی. 
تحبیب» دلسوزی و ترحم. لطافت» ظرافت. 
تحقبر؛ توهین. تقلیل» اندکی. کو تاهی. اسم 
الت سازد: غلطکك (غلتکك). نست و تشبه 
[- 4]: بشتکك. اسم صوت سازد: بدبدک. از 
صفت اسم سازد: روزد کگ: بت سازد: 
نند ک. افادة مکان و جایگاه کند: هت 
معنی همچون و سان و گونه مانند ۳0 
گاه‌افادهٌ معر فه کن (بجای الف‌و لام‌در عر بی). 
کا: 2 [مصر ی قد یم ] .۲ در دین مصر بان 
قدیم به معنی روح جاویدان و همان جفت یا 
غسي کنناء «رکا» برای نعسن نوعی همراد 
مشترک جهت همه افراد بکك دسته بکار 
می ر ژد. در «کا» فردیت و شحصت «مانام و 
دات خدایی دیده می‌شو د. شاهت «کا.ی 
مصری و مثل افلاطونی نمونه جالبی از 
رابطه دين و فلسفه است. همچنین «کا» تا 
=== MON کنیزک ===
پرستار زن» جاریه. برده‌ای که دختر یا زن 


کنیزک: -۸۵]2 (ا.مصف.) زن خرد (عم.) 
دخت رکك. پرستار زن خرد. دخترک با زنکی 
که بر ده باشد. کنیز. 

کنیس: 5 (معر. ارمی؛ آرا. - کنشت] 
=== ARY suffix ===
11104:پسوند ۳۸311 به چم "پاییدن" (هند و اروپایی:-۱۶01 بازگشت به: پاییدن)
13224:۲ پسوند ۰۷030178 (مثلاً در واژه‌ی 0۸71۷030118) نیز از همین واجریشه است.
```


## [2026-09-04T19:18:50.105Z] TOOL CALL #56: Bash

```json
{
 "command": "ls -la && find . -maxdepth 3 -iname \"*.pdf\" -not -path \"./data/verification/*\" | head"
}
```


### [2026-09-04T19:18:50.172Z] TOOL RESULT

```
total 24660
drwxrwxr-x  8 sfmqrb sfmqrb     4096 Sep  4 13:41 .
drwxrwxr-x 20 sfmqrb sfmqrb     4096 Sep  4 14:35 ..
-rw-rw-r--  1 sfmqrb sfmqrb     2209 Aug 22 01:02 CONTRIBUTING.md
drwxrwxr-x  6 sfmqrb sfmqrb     4096 Sep  4 10:26 data
drwxrwxr-x  3 sfmqrb sfmqrb     4096 Aug 22 15:38 docs
-rw-rw-r--  1 sfmqrb sfmqrb  1201179 Aug 22 01:02 EtymologicalDictionary-persian-english.epub
-rw-rw-r--  1 sfmqrb sfmqrb 23984297 Aug 22 01:02 EtymologicalDictionary-persian-english.pdf
drwxrwxr-x  9 sfmqrb sfmqrb     4096 Sep  4 15:16 .git
drwxrwxr-x  3 sfmqrb sfmqrb     4096 Aug 22 01:02 .github
-rw-rw-r--  1 sfmqrb sfmqrb      263 Sep  4 13:41 .gitignore
-rw-rw-r--  1 sfmqrb sfmqrb    12133 Aug 22 15:41 README.fa.md
-rw-rw-r--  1 sfmqrb sfmqrb     8014 Aug 22 15:39 README.md
drwxrwxr-x  3 sfmqrb sfmqrb     4096 Aug 22 18:35 site
drwxrwxr-x  4 sfmqrb sfmqrb     4096 Sep  4 14:35 tools
./EtymologicalDictionary-persian-english.pdf
```


## [2026-09-04T19:18:53.366Z] TOOL CALL #57: Bash

```json
{
 "command": "(pdftotext -f 43 -l 43 -layout EtymologicalDictionary-persian-english.pdf - 2>/dev/null || python3 -c \"print('no pdftotext')\")"
}
```


### [2026-09-04T19:18:55.449Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:18:59.607Z] TOOL CALL #58: Bash

```json
{
 "command": "which pdftotext pdftoppm; pdftotext -f 43 -l 43 -layout EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p43.txt; echo \"exit $?\"; wc -c /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p43.txt"
}
```


### [2026-09-04T19:19:01.232Z] TOOL RESULT

```
/usr/bin/pdftotext
/usr/bin/pdftoppm
exit 0
1 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p43.txt
```


## [2026-09-04T19:19:04.604Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 43 -l 43 -r 200 -png /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf p43 && ls -la p43*"
}
```


### [2026-09-04T19:19:07.040Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 73155 Sep  4 15:19 p43-043.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1 Sep  4 15:19 p43.txt
```


## [2026-09-04T19:19:09.234Z] TOOL CALL #60: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p43-043.png"
}
```


### [2026-09-04T19:19:09.690Z] TOOL RESULT

```

```


## [2026-09-04T19:19:09.687Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-04T19:19:44.478Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 k̑ē(i) ===\"\ngrep -n \"Wetzstein\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20\necho \"=== SYN whetstone/sharp ===\"\ngrep -n -i \"whetstone\" SYN.txt | head -10"
}
```


### [2026-09-04T19:19:44.609Z] TOOL RESULT

```
=== WLD Bd1 k̑ē(i) ===
2097:axovij „ Wetzstein‘ : , dxcov , -vvrog „\YurfspieB“ (fiir alteres axcov, *-ovog nach 
28591:Wetzsteins“ 2 )); 
28598:Lat. cds, cotis „Wetzstein“ (wohl auch cedes, cautes „spitzer Fels, Riff", 
39400:„streicheln, mit der Hand sanft iiberfahren u , pr. glosto „Wetzstein“ (lit. 
39412:galanda, galasti „scharfen, schleifen“, lett. galuods „Wetzstein w , pr. glan- 
51882:mutige", drjyov oi be bt-v, axovyxov Hes., dgyavg „Wetzstein“, xedcoxx at- 
=== SYN whetstone/sharp ===
1620:Lith. uola ‘rock’ (also ‘whetstone’), Lett. wola ‘pebble, egg, rock’ : Lett. velt, Lat. volvere ‘roll’, Lith. apvalus, ON valr ‘round’, etc. (Walde-P. 1.298 ff., without uola). Miihl.-Endz. 4.416.
1628:Skt. gila- ‘stone, rock’ : ¢ita- ‘sharp’, ¢a-, gt- ‘sharpen’, Lat. cds ‘whetstone’, ON hein ‘whetstone’, OF han ‘stone’, ME honne, NE hone ‘whetstone’. Walde-P. 1.454.
6619:Lett. wola (also ‘round stone, pebble’ ; Lith. uola ‘whetstone, rock’) : Lett, velt, Lat. volvere ‘turn’, Lith. apvalus, ON valr ‘round’, etc. (Walde-P. 1.298 ff, without wola). Muhl.-Endz. 4.416,
14128:deriv. of Lat. cos, cotis ‘whetstone’ | (cf. foll.), rather than cognate with it. ae cute). Of. Rum. ascutt ‘whet, | Mithl.-Endz. 2.697. igen fr, *excotire. Tiktin 471. 6. ChSl. nozt, etc., general Slavic :
```


## [2026-09-04T19:19:45.895Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN hone n ===\"\ngrep -no \"hone, n[^|]\\{0,400\\}\" KLN_1966.txt KLN_1971.txt | head -5\necho \"=== KLN cone n ===\"\ngrep -no \"cone, n[^|]\\{0,400\\}\" KLN_1966.txt KLN_1971.txt | head -5"
}
```


### [2026-09-04T19:19:47.557Z] TOOL RESULT

```
=== KLN hone n ===
KLN_1971.txt:16609:hone, n. Cp. anthem, which 
KLN_1971.txt:22818:hone, n., an instrument for helping the deaf 
KLN_1971.txt:67998:hone, n., an instrument placed against the 
KLN_1971.txt:70826:hone, n., a phonographic instrument for 
KLN_1971.txt:86606:hone, n., a free-reed organ stop giving a sweet 
=== KLN cone n ===
KLN_1971.txt:53536:cone, n. — F. cone , fr. L. conus, fr. Gk. xwvot;,
```


## [2026-09-04T19:19:55.558Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD 28580-28610 ===\"; sed -n '28580,28610p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt\necho \"=== KLN cone ===\"; sed -n '53536,53545p' KLN_1971.txt\necho \"=== KLN hone whetstone ===\"; grep -n \"whetstone\" KLN_1971.txt | head -10"
}
```


### [2026-09-04T19:19:55.675Z] TOOL RESULT

```
=== WLD 28580-28610 ===
lat. catus (nach Yarro sabinisch = ) „acutus“, „scharfsinnig, gewitzigt“ (Auf- 
recht KZ. 1 , 472 ff.’, mir. cath „weise“ (Fickl 4 45'). Yielleicht auch gr. 
kotos „Groll, Zorn 1 ' als „*Scharfe“ (Fiek aaO.; nicht besser zu gall. Catu- 
„Kampf‘ £ usw.; Yok. wie in doxog). 

Ai. gana-h „\Vetzstein, Probierstein" (eigentlich mind aus *cana-h, == 
np. san, af'-san, pam, pa-sdn „W etzstein"; dazu vermutlich xcoveiov „coni- 
um maculatum" (s. zur Bed. Vf LEWb. 2 u. cicuta, Lehmann KZ. 41, 394) 
wegen letzterer Entsprechung nicht besser nach Bezzenberger BB. 27,171 
als *i s ahia- zunachst zu ala, s. u.) = gr. y.cbvos „Kegel, Pinienzapfen, Helm- 
spitze, der kegelformige Kreiseh' (urspgl. etwa „von der Gestalt eines 
Wetzsteins“ 2 )); 

Av. saeni-s „Spitze, Wipfel", saeni-kaofa- „mit spitzem, d. i. aufgerich- 
tetem Hocker a (vom Kamel). 

Anord. liein , ags. han „Schleifstein“; 

Lat. cds, cotis „Wetzstein“ (wohl auch cedes, cautes „spitzer Fels, Riff", 
so daB au Hyperurbanismus fur o , s. Vf. LEWb. 2 143 3 ); Curtius 159, 
Fick 1 4 45, 425, III 4 64, Brugmann I 2 353. 

Arm. sur „scharf" ( *ko-ro-s ; davon stem „scharfe“), sur, g. sroy „Schwert, 
Dolch, Messer, Rasiermesser" 4 *, wohl auch sair „Schneide“ ( lce-ri -), Zs. 
sairadir „Schneide“, wovon *sardrem, sadrem „reize, treibe an". (Lit. fiber 
die arm. Worte : Scheftelowitz BB. 28, 284, Pedersen KZ. 39, 407 Liden 
Arm. St. 80 5 ); dazu nach Bugge BB. 32,24 als id g.*kd-la, -li- auch ai. 
gild „Stein, Fels", arm. sal (g. salt) „Steinplatte, AmboB" (vgl. zur Bed. 
gr. dxp,a>v „AmboB“ : ai. acma „Stein“), vermutlich auch anord. hella „flacher 
Stein, Schiefer". Anord. hallr „Stein“, got. hallus „Klippe“. 6 ) 

=== KLN cone ===
cone, n. — F. cone , fr. L. conus, fr. Gk. xwvot;, 
‘pine cone, fir cone, cone; peak’, which is cogn. 
with OI. sanah , ‘whetstone’, L. cos, gen. cotis , 
‘whetstone’, cat us, ‘sharp’, fr. L-E. base *fco(i)-, 
*ke(i)-, ‘sharp, whet; to sharpen, whet’, 

whence also OE. han, ‘stone’, ON. hein, ‘hone’. 
See hone and cp. conarium, Conium. Cp. also 
cade, ‘juniper’. 

=== KLN hone whetstone ===
53538:with OI. sanah , ‘whetstone’, L. cos, gen. cotis , 
53539:‘whetstone’, cat us, ‘sharp’, fr. L-E. base *fco(i)-, 
103002:‘smooth’, OPruss. glosto, ‘whetstone’. Cp. 
115322:hone, n., a whetstone. — ME. hoone, ‘hone’, fr. 
115330:L. cos , gen. cotis, ‘whetstone’, cat us, ‘sharp’, 
163241:novaculite, n., a hard slate used for whetstones 
173284:and axovr], ‘whetstone’, which is rel. to a xyj, 
174091:tical with <paypoc, ‘whetstone’, which is possibly 
221858:to OI. sdnah, ‘whetstone’, Utah, ‘sharpened’, si- 
266530:whetstone, n. — ME. whetston , fr. OE. hwetstan ,
```


## [2026-09-04T19:19:59.801Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '115322,115336p' KLN_1971.txt\necho \"---- 221855 ----\"; sed -n '221850,221865p' KLN_1971.txt"
}
```


### [2026-09-04T19:19:59.899Z] TOOL RESULT

```
hone, n., a whetstone. — ME. hoone, ‘hone’, fr. 
OE. hdn, ‘stone’, rel. to ON. he in, ‘hone’, and 
cogn. with OI. si-sa-ti, ‘sharpens’, sanah, ‘whet- 
stone’, iatah, ‘sharpened, sharp’, iitdh, of s.m., 
Avestic saeni-, ‘pointed; point, top of a tree*, 
ModPers. sayad, ‘rubs’, Arm. sur (for *ko-ro-), 
‘sharp 1 , sur (gen. sroy), ‘sword, knife’, srem, 
‘I sharpen’, Gk. xwvos, ‘pine cone, fir cone’, 
L. cos , gen. cotis, ‘whetstone’, cat us, ‘sharp’, 
Mir. cath, ‘wise, sage’. All these words derive 
fr. I.-E. base *ko(i)-, *ke(i )-, *£*(*>, ‘sharp, 
whet; to sharpen, whet’, whence also possibly 
OI. sikha, ‘top, point; tuft of hair’, sikharah, 
‘pointed; summit’, sekharah , ‘top, summit’. Cp. 
cone and words there referred to. Cp. also sik- 
---- 221855 ----
nity founded by Guru Nanak about the end of 
the 16th cent. • — Hind., lit. ‘disciple’, fr. OI. 
sikfati, ‘studies, learns’, desiderative of sakndti , 
‘is able, is competent’. 

sikhara, sikara, n., a pyramidal tower {India). — 
OI. dkharah, ‘pointed; summit’, rel. to iikha-, 
‘point’, sekharah , ‘top, summit’, and prob. also 
to OI. sdnah, ‘whetstone’, Utah, ‘sharpened’, si- 
sd- ti, ‘sharpens’, and cogn. with Gk. xtovcu;, 
‘pine cone’. See cone. 

Sikhism, n., the tenets of the Sikhs. — Formed fr. 
Sikh with suff. -ism. 

silage, n., fodder packed in a silo. — Aphetic for
```


## [2026-09-04T19:20:20.768Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB -ak suffix ===\"; grep -n \"suffix -ak\\|suff. -ak\\|-ak-\\b\" NYB_vol2_glossary.txt | head -10\necho \"=== NYB kanizak ===\"; grep -n \"kanizak\\|kanicak\\|murvak\" NYB_vol2_glossary.txt | head -5\necho \"=== SBK -ak ===\"; grep -n \"پسوند\\|تصغیر\" SBK.txt | head -10\necho \"=== HRN diminutive ===\"; grep -n -i \"Deminutiv\\|Diminutiv\" HRN.txt HUB.txt | head -10"
}
```


### [2026-09-04T19:20:20.862Z] TOOL RESULT

```
=== NYB -ak suffix ===
3385:sälak [s?lk' ; SNT-k'] adj. of the preceding w. used in composition with a numeral: duxt-é ... 3-— a three year old daughter 14%; dāt + 15-— the age of 15 years 3! etc. ; ka Zartuxšt 7-~ būt 5217-18, 7-~ homänäk about seven years old 26°; — in repe- titions the suff. -ak may be added to the last sal only: hac 10 sal tai 90 ~ 201; — used for sal: hac 7 ~ apäc since seven years 16%; cf. sih-sälak, sih-säleh.
=== NYB kanizak ===
1069:who knew 121°; būt i ka nē būt ... u bavet ka ne bavet ches was a time when he did not exist, and there will be a time when he will not exist 642-3; ö(h) ~, v. ē(h); cf bavisn. — 2. as copula, with a noun, a pron. or a prep. + subst. as its complement, passim: hàn but Vahuman 56%; martom ... hamäk ahēš ... bavēnd willbe immortal 1049-19; kanicak pat giyäk bütàn (YHWWN-t*n'] pl. cas. obl. of the pret. büt used as a subst. ‘he who has been’ 5518, ~. V. bavétün.
1220:dāštan [d'štn'] dār- [YHSNN-; d'1- 217. 281. 10014. 10279], imp. sg. with encl. pron. där:om [YHSNN-m] 6t; opt. 2nd p. sg. dārēš 41!?; pt. dašt = pret. pass. 3d p. sg., construed as an act. form 495-5; to keep, to hold, to sustain, to maintain, to have, 8?! and passim; — with an adj. as a complement of the obj.: Sahpuhr kanicak āžarmīk u garamik däst Š. kept the girl honoured and respected 163-4; 225 ete. passim; the complement some- times comes near to an adv., e. g. véh ~ to keep, handle a th. well 5026-27, and may be replaced by an adv.: én zan garämikihä ddr 1024; 6415; — with an obj. and pat + an adj.: to consider a p. or a th. to be ...: pat margaržān ~ to consider a p. guilty of death 1014-19; 6398-9, 8017, 839-19; pat azateh (cas. obl. sg.) där-om! consider me as a free (wom- an) — release me (from slavery)! 64, v. s. v. Gzat; — pat & ~ ku to be of the opinion that, to think, imagine that 2525, 982-3, 3227 sq. 5012-13, ef NP pindāštan < *pa(t) én daštan; pat ce dārēh how do you regard (the case mentioned in the preceding kū- clause)? 105-$; pat depahr, pat nihän
1760:4. partitive: hac fradandan + han mart kasé anyone of the children of that man 25; hac šmāh xiönän ke hast ke ...? 25” ete.; fratom hac ax" i astomand 53%; xuastom hac z"arisnàn the most delicious of dishes 7413; ete. — 5. in comparison ‘than’: hac apārīk kanicakän āžarmīktar 422; Zarristan ke... zan-ē hac či hucihr- tar nest 259-19; hac tē veh 411; kū-š suk mas būt hac apdrik gāv 492°; more emphatically yuvattar (g. v.) hac hàn + huhömikän homtar 40°’. — 6. causative: hac hàn dušxvār sahist by this he was very much shocked 4?-?; hac hàn 1 devan sārēnišn 3774-25 : causal conj. : hac hàn cigon because 4511; hac han i with a nominal clause 48!. — 7. forming adverbs: hac pas, hac pes, hac be, hac apar (hacapar), hacadar; prepositions: pas hac, peš hac (= patiš hac 368), yuvat hac, bé hac; frame prepositions: hac. . . rād owing to 1525-26; hac .. . bérén 20%; hac . . . yuvatāk 76°. — Av. (1746 sqq.) hacé; OP haca; MPrth ^c, "Z; MPrs 'c, "z; Paz. ez (eži-ca); NP az.
2179:kanicak
2197:kanicak [knyck'], with indef. art. ~-é
=== SBK -ak ===
479:تصغیرکلمات 4 € 1۱۳ > 1۱۱ 
13339:بمعنی ملکه و صاحبه‌مملکت و نیزعلامتی بوده است کهها آنر | ازادات تصغیرميشماريم 
15860:ودر پپلوی مردم را هر دمك بکاف تصغیس نیز میآوردهاند ولی در زبان دری‌این تصغیردیده 
17673:این ادات تصغیر کاه برای تصفیر سنی و گاه برای تصغیر مقامی و گاه منباب 
17674:رحمت ورقت وعطوفتآ بد و گاهی هم در مورد اث تصغیر بکارآورند و در کتب قدیم 
=== HRN diminutive ===
HRN.txt:8075:*) Ein np, Deminutivsuffix -le finde ich nachträglich sehr häufig
HRN.txt:8077:indog. Deminutivsuffix -/o- vergl. Brugmann, Grund-
HRN.txt:8878:sammengezogenes Diminutiv von näm*).
HUB.txt:3140:870. Np. kamzak ist durch das Deminutivsuffix ak von
HUB.txt:8107:Aus jiingerer Zeit muss auch das Deminutivsuffix ^)
HUB.txt:8745:a) im deminutiven Suffix 2) ak, das wohl jungeren
HUB.txt:8753:*) Vgl. bal. -/A;, uk (mit k) als Deminutivsuffix.— 245 —
```


## [2026-09-04T19:20:24.920Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB 3135-3145 ===\"; sed -n '3135,3148p' HUB.txt\necho \"=== HUB 8740-8760 ===\"; sed -n '8738,8760p' HUB.txt\necho \"=== HRN 8070-8082 ===\"; sed -n '8070,8082p' HRN.txt\necho \"=== SBK 17665-17685 ===\"; sed -n '17665,17685p' SBK.txt"
}
```


### [2026-09-04T19:20:25.002Z] TOOL RESULT

```
=== HUB 3135-3145 ===
gelten konnen.- 89 -
und Impt.) = kandol („in the past tenses'') kann
doch nur LW. sein (np. praes. kanam, perf, handam).
Die Differenz zwischen iran. han- und skr. khan ist
noch nicht befriedigend erklart.
870. Np. kamzak ist durch das Deminutivsuffix ak von
kaimz abgeleitet. Phi. kanlSak ware = np. kanlza,
Vgl. Darmesteter, Etud. iran. I, p. 288. Ueber
dial, kine s. Mann, ZDMG. 47, 705.
871. Np. hutdh oder kdtah (nach dem afgh. LW. kdtah) heisst
eigentlich 'kurz* (nicht 'klein*) und ist von np. kddak
*Kind' = phi. kotak *a child, an infant' Gl. and Ind.
201, arm. LW. kotak *der Eleine' (Beiname des armen.
Konigs Xoarov bei Faust us von Byz.) zu trennen.
=== HUB 8740-8760 ===
{ag, ag, ug, ig, tg) siehe Verf. ZDMG. 41, 326 flg. , im
Afghanischen {k, g, ka^ ga etc.) Geiger, Etym. und Lautl.
p. 46; im BaludT {ag-^ ok, uk\ ig, deminut. i, ik, uk) Geiger,
Lautlehre p. 25.
§ 137. In den folgenden Fallen ist suffixales k im
Auslaut weder zu g geworden noch geschwunden, sondem
als k geblieben :
a) im deminutiven Suffix 2) ak, das wohl jungeren
Ursprungs als das allgemeine Pehlevisuffix ak = np. a ist :
mardak 'Mannlein* von mard *Mann', andak wenig' von and
'soviel* etc. (Vullers, Gram. p. 233). Dazu auch juftak
Inseparaber, eigentl. *Parchen , vgl. arm. juxtak ein Paar
*) Z. B. zibaq 'Queoksilber', arm. zibak (geschrieben zipah\ syr.
pD^T (Brockelraann p. 90), ;ii^7 (de Lagarde) = np. ziva — phi.
*zivak,
*) Vgl. bal. -/A;, uk (mit k) als Deminutivsuffix.— 245 —
(Turteltauben), afgh. LW. juftak *das Ausschlagen mit beiden
Hinterbeinen = np. jufta; kddak 'Kind', phi. kotak, arm.
kotak (oben p. 89); r^ak 'Kind' = fihl. retak (siehe p. 244)?,
pusak = pOsak 'Katze' (dial.) H. 322 ? Dieses k bleibt auch
im Plural: hindtwakariy Vullers Wb. II, 1478.
b) in dem Suffix uk:
sabuk leicht', afgh. spuk^ paz. saiuk Min. Gl. 180,
=== HRN 8070-8082 ===
mann, M61. asiat. IX, 235. Bei den damaligen nicht eben bedeutenden
neupersischen Kenntnissen des Verfassers darf man in solchen Fällen
kaum etwas Belangreicheres als Verlesungen (oben etwa statt merdike?)
oder kritiklose Übernahmen von Päzendworten aus West's Glossaren
mutmassen *).
*) Ein np, Deminutivsuffix -le finde ich nachträglich sehr häufig
bei den Bergjuden im Kaukasus. Aus Mi Her 's Glossar habe ich mir— 208 —
indog. Deminutivsuffix -/o- vergl. Brugmann, Grund-
riss II, 186 folg.
930. gile 'Klage .
aw. gerezü" 'Klage', vergl. [/^gar2-, gerezaiti 'klagen';
plilv. garzTtan j garz{i)s7i, gilak (Men.); ai. l^garh-,
garhate 'klagen, anklagen' ^).
=== SBK 17665-17685 ===
اسلیمی شد . و یکی از اسرار ترقی نقشه های قالی و شوش کاشی وسایر سفالها وسرلوحمای کتب که 
دئیا را بخود متوجه کرده است همین ممنی است و اسلیمی‌های قبلاز اسلام چه در ایران وچه در روم 
وچه درهند بسیار ساده ات و این تنوع و داربائی از اش تربیت اسلامی است . 


سبك شناسی 4\4 


این ادات تصغیر کاه برای تصفیر سنی و گاه برای تصغیر مقامی و گاه منباب 
رحمت ورقت وعطوفتآ بد و گاهی هم در مورد اث تصغیر بکارآورند و در کتب قدیم 
بارها لفط (پا کیزه) را که مصفر (باك) است درمورد زنان پال وموّعن آورند چنانکه‌در 
پهلوی ملکه را «پانوی» د«شهر پانوی» که مصفردپان» و«شپرپان» است‌آورده‌اند 


وشرح‌آن گذشت . 
مو لوی فرماید : 
کاف رزخمت کفیشن فی نت جد چو وید طفلکم تحقیر نیست 


در نثر ونظم قد م‌کلمات مصفر از هر باب زیادتراز ادوار بعد معمول بوده است - 
مثال از لیهقی ص سي « در آ تسف رکه بخراسان رفتیم و سوی ری کشیده آمد وسفر
```


## [2026-09-04T19:20:42.214Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cone",
 "prompt": "Quote the full etymology of \"cone\": Greek konos, Latin conus, French cone, and the PIE root and cognates cited (Sanskrit sana, Latin cos, Old English han/hone)."
}
```


## [2026-09-04T19:20:43.860Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%BE%E0%A4%A3",
 "prompt": "Quote the Sanskrit शाण (śāṇa) entry: meaning ('whetstone'), etymology (root शा śā 'to sharpen'), and cognates."
}
```


### [2026-09-04T19:20:47.311Z] TOOL RESULT

```
# Etymology of "Cone"

The word "cone" traces back through multiple linguistic layers:

**Greek Origin:** "konos" meaning "cone, spinning top, pine cone"

**Latin:** "conus" meaning "a cone, peak of a helmet"

**French:** "cone" (16th century)

**Proto-Indo-European Root:** The etymology suggests a PIE root "*ko-" with the meaning "to sharpen," though some scholars consider it possibly a pre-Greek word.

**Related Cognates:** The source document cites "Sanskrit sanah 'whetstone,' Latin catus 'sharp,' Old English han 'stone'" as cognate forms sharing this root connection to sharpening or stones.

The term entered English around the 1560s as a mathematical/geometric term, later expanding to describe pine cones (1560s), volcanic formations (1771), eye structures (1867), and ice cream cones (1909).
```


### [2026-09-04T19:20:51.425Z] TOOL RESULT

```
# Sanskrit शाण (śāṇa)

## Meaning
The Sanskrit entry defines शाण (śāṇa) with three related senses: "whetstone," "touchstone," and "saw."

## Etymology
The word derives from a root meaning to sharpen or hone. The Wiktionary entry notes comparison to Ancient Greek κῶνος (kônos), suggesting possible Indo-European connections.

## Cognates and Descendants
The term has extensive descendant forms across Indo-Aryan languages, including:
- Pali: sāṇa
- Hindi: सान (sān)
- Urdu: سَان (sān)
- Bengali: সান (śan)
- Nepali: सान (sān)
- Punjabi: sāṇ
- Marathi: साण (sāṇ)

These descendants preserve the original meaning relating to grinding or sharpening implements, demonstrating the word's deep roots in South Asian linguistic tradition.
```


## [2026-09-04T19:20:53.484Z] AGENT

Now let me archive all the web sources I used.


## [2026-09-04T19:21:05.646Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://www.etymonline.com/word/hone|page 43, root Ak/Kei: English 'hone' < OE han < PGmc *hainō < PIE *ko- 'to sharpen'\" \\\n \"https://www.etymonline.com/word/cone|page 43, root Ak/Kei: English 'cone' < F cone < L conus < Gk konos; PIE *ko- 'sharpen'; cognates Skt sanah, L catus, OE han\" \\\n \"https://en.wiktionary.org/wiki/hone|page 43, node 5-6: OE han < PGmc *hainō < PIE *keh3i- 'to sharpen'; cognates Gk konos, Persian san 'whetstone'\" \\\n \"https://en.wiktionary.org/wiki/%CE%BA%E1%BF%B6%CE%BD%CE%BF%CF%82|page 43, node 7: Gk konos < PIE *koh3nos from *keh3- 'to sharpen'; cognates Skt sana, L cos, catus; Beekes suspects Pre-Greek\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D8%A7%DB%8C%DB%8C%D8%AF%D9%86|page 43, node 3: NP sayidan < MP sudan, pres. say- < PIr *sauH- < PIE *keh3(i)- 'to sharpen'\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%AF%D9%86|page 43, node 3: NP sudan, present stem say-/sav-, literary form of sayidan\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D8%A7%D9%86|page 43, node 3 extra: NP san 'whetstone', cognate Skt sana\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%BE%E0%A4%A3|page 43, node 2: Skt sana 'whetstone, touchstone', cf. Gk konos - the form Nourai labels Avestan 'cana'\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-kos|page 43, entry 2 root Akos: PIE *-kos is an adjectival suffix, no diminutive function listed\" \\\n ; do\n  url=\"${u%%|*}\"; note=\"${u#*|}\"\n  python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-04T19:21:09.914Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/95e3898830c604ee.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3c5f026b5d601747.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a6db38b45dc421a0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/28fb21577ddb55a1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e50c70fae23aa521.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2d35956609e336f0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3a7a8e8f3a510e87.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e87466f02febdf30.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7ce16198ec0b1351.txt
```


## [2026-09-04T19:21:18.615Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/extracted/batch\npython3 - <<'EOF'\nimport json,glob,os,re\nhits=[]\nfor f in glob.glob('page-*.json'):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e.get('nodes',[]):\n            if n.get('lang') in ('Sanskrit','Avestan'):\n                for w in n.get('words',[]):\n                    t=w.get('translit') or ''\n                    if 'č' in t:\n                        hits.append((f,n['lang'],t,w.get('gloss')))\nprint(len(hits))\nfor h in hits[:60]: print(h)\nEOF"
}
```


### [2026-09-04T19:21:20.153Z] TOOL RESULT

```
98
('page-295.json', 'Avestan', 'čatwârao', 'four')
('page-357.json', 'Sanskrit', 'pra-nača', 'to be finished')
('page-357.json', 'Sanskrit', 'pra-nač', 'absent, absent minded')
('page-456.json', 'Sanskrit', 'čodatî', 'to hurry, propel')
('page-312.json', 'Avestan', 'raočah', 'light')
('page-312.json', 'Avestan', 'raoč-xšaema, raoxšna', 'bright light')
('page-292.json', 'Sanskrit', 'čamati, camati', 'to sip')
('page-498.json', 'Avestan', 'tak, taka, tač', 'to run')
('page-498.json', 'Avestan', 'tačaiti', 'runs')
('page-498.json', 'Avestan', 'ham-tač, ham-tak', 'to throw')
('page-498.json', 'Avestan', 'tačar', 'road')
('page-498.json', 'Avestan', 'tačan', 'haste, hurry')
('page-452.json', 'Sanskrit', 'čadaiti', 'to cover')
('page-452.json', 'Sanskrit', 'čattra', 'cover, umbrella')
('page-420.json', 'Sanskrit', 'račana, rašanâ', 'rope, strap, belt')
('page-267.json', 'Sanskrit', 'šiphâ, čiphâ', 'twig, hair')
('page-437.json', 'Avestan', 'haek 2, hinčaiti, hičaiti', 'flows from')
('page-263.json', 'Avestan', 'čevîšî', 'attend, expect, hope')
('page-342.json', 'Avestan', 'berez-čaxra', 'with fast wheels')
('page-168.json', 'Avestan', 'vîčiča', 'mortar, gypsum')
('page-501.json', 'Avestan', 'thang, â-thax, hanč', 'to pull, also a path, way')
('page-425.json', 'Avestan', 'uruthwara, uruthwan, uruthwasča', 'abdomen, belly')
('page-425.json', 'Avestan', 'ravas-čarât', 'moves in free space (freely)')
('page-419.json', 'Sanskrit', 'rěš, ričate', 'to tear')
('page-284.json', 'Sanskrit', 'Kâča', 'straw')
('page-284.json', 'Sanskrit', 'čvitra', 'white')
('page-285.json', 'Sanskrit', 'kunče', 'bend')
('page-554.json', 'Avestan', 'vi-vačah', 'to speak against')
('page-43.json', 'Avestan', 'saěni, saěniš, čâna', 'pointed, sharp or rough objects used for grinding')
('page-43.json', 'Avestan', 'abi-čâna, abhi-čâna', 'grinding stone')
('page-297.json', 'Avestan', 'kam 1, kam-čit, katama', 'which?')
('page-297.json', 'Avestan', 'č-, čŭ, čî 2', 'how?')
('page-297.json', 'Avestan', 'čiš 2, čiš-ca 2', 'who?')
('page-297.json', 'Avestan', 'čeč', 'whether')
('page-297.json', 'Avestan', 'čaiti, chvant', 'how many?')
('page-297.json', 'Avestan', 'ča-hyâ', 'who, which?')
('page-288.json', 'Avestan', 'ca, ča', 'and')
('page-288.json', 'Avestan', 'čiš-ca 1', 'any, whatever')
('page-288.json', 'Avestan', 'čit 1', None)
('page-388.json', 'Avestan', 'pax, pač, pačaiti', 'to cook')
('page-307.json', 'Avestan', 'raexnah, raix, raik, raič, raeč 2', 'to leave')
('page-307.json', 'Avestan', 'paiti-raeč', 'avoid, leave')
('page-307.json', 'Avestan', 'vi-raeč', 'leave away, run away')
('page-467.json', 'Sanskrit', 'čârah', 'sparrow')
('page-438.json', 'Avestan', 'sčand', 'to break')
('page-438.json', 'Avestan', 'kareman, čareman', 'hide cut off animals')
('page-78.json', 'Avestan', 'bučahin, buxti', 'howl, yell')
('page-484.json', 'Avestan', 'hu-čitra', 'nice faced')
('page-516.json', 'Avestan', 'usča', 'above, overhead, on top')
('page-516.json', 'Sanskrit', 'ucca, učča', 'high, top')
('page-271.json', 'Sanskrit', 'črî', 'bind, mix')
('page-54.json', 'Avestan', 'anhuyat-hača', 'from heart (soul)')
('page-450.json', 'Avestan', 'fra-sčimbana', 'universe, world')
('page-451.json', 'Avestan', 'čitra', 'clarity, face, also race and origin')
('page-451.json', 'Avestan', 'hu-čitra', 'with nice face')
('page-451.json', 'Avestan', 'manuš-čitra', 'with a manly face, or from the race of "Manush"')
('page-451.json', 'Avestan', 'čâyâ, asaya', 'shade')
('page-154.json', 'Avestan', 'hača-adairi', 'from under')
('page-393.json', 'Avestan', 'pairi-čayeiti', 'sort around, divider')
('page-249.json', 'Avestan', 'kakuš, čakuš', 'ax, hammer')
```


## [2026-09-04T19:21:37.813Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ak-, ok-\\|aRk\\|„scharf“\\|ak\\^-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head\necho \"--- find 'scharf, spitz' ---\"\ngrep -n \"scharf, spitz\\|spitz, scharf\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head\necho \"--- around line 2090 (akone) ---\"\nsed -n '2060,2100p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-04T19:21:37.902Z] TOOL RESULT

```
1997:BB. 23, 62). — Lit. asriis, astrus , alit. asztrus , aksl. ostrr, „scharf“ (t Ein- 
2263:ofo? ..AYeinessig 11 ; lett. ass „scharf“ = schwed. ag m. „Sumpfgras, Cladium 
2320:Bedeutungsverschiedenheit „scharf“ und ,, Stein") ; sie wfirden auch die An- 
22397:Uber mit bar- (qar-) anl. Steinbezeichnungen s. u. *ak- „scharf“. 
26925:mit den u. *uk- „scharf“ besprochenen Steinbezeichnungen mit dem Anl. 
28897:hcendig mit Lit.; ahd. hantag „scharf“ zu kevt- „stechen“, wie vielleicht 
29313:78 f. (Charpentier IF. 38, 186 nimmt aind. *guka- „scharf“ als Grundlage von 
32311:„scharf“, ahd. ( h)was , mhd. was(ser ) „scharf, spitzig, heftig, streng“; aisl. 
--- find 'scharf, spitz' ---
1964:ak- (z. T. auch ak-) „scharf, spitz, kantig; Stein“ (altere Lit. z. B. bei Yf. 
7313:*ak- ,,scharf, spitz“, lat. unis, -as usw.; iiber lakon. aixXov „Abendessen“ 
11145:problematisch ist Zusammenhang mit ah- „scharf, spitz“ imit o wie lat. 
22415:qhar- „scharf, spitz". 
25691:*ak- ,.scharf, spitz 1 , iiberzeugt nicht, siehe Zupitza KZ. 36, 60 gegen Daniels- 
32311:„scharf“, ahd. ( h)was , mhd. was(ser ) „scharf, spitzig, heftig, streng“; aisl. 
41708:igld , Nadel", wobei etwa aksl. ostrogh „Pfahlzaun" zu ostn „scharf, spitz"' 
54681:dilra- „mit scharfer Schneide"; gr. floog ,,scharf, spitz", sdoiooa „ich scharfte, 
--- around line 2090 (akone) ---

ai. dqman- m. „Stein, Fels; Himmel“ (zur Yorstellung des Himmels als 
eines Steingewolbes s. Beichelt IF. 32, 23 ff.), acmard- „steinern“ (weisen 
auf einen r-w-St., s. Meillet Ft. 424, Berneker 478), av. asman- „Stein, 
Himmel“, asmana- „steinern“, ap. asman- „Himmel“ f ai. gen. dniali , instr. 
acnd, av. gen. a mo, abl. asnuat nach J. Schmidt Krit. SS f. mit -n- aus 
-mn- und darum nicht unmittelbar den n-Bildungen vergleichbar ; instr. 
pi. ai. agnaih nach den o-St.); av. asongo-gav- „mit Hiinden aus Stein“. 
ap. ada n yaina- „stoinern“ (mit -g- aus dem n. sg. des rjn- St., s. Bartho- 
lomae IF. 2, 269 ; ob auch hier -n- auf -mn- zuriickgeht, ist sehr fraglich, 
und urspriingliches *ak-en-g- weit wahrscheinlicher) ; gr. uyguov „AmboB !! 
ux/uwv 6 ovgarog (s. Reichelt aaO. 26); gall, aumnum „saxum“ (aus *akamno- 
mit friiher Lenierung des m zu w?); lit. asmno , -ehs „Schiirfe“, lett. asmens 
m. „Schneide‘ : , lit. akmud, -ens „Stein“, aksl. kanuj, -cne „Stein“ (Umstellung 
aus *akmy, das durch Anlautdehnung aus *dkmon entstanden sei, erwagt Ber- 
neker 47S wo Lit. iiber andere Erklarungen : von diesen bevorzuge ich die Iler- 
leitung aus einer Basis *akam(on) : *kam(on) wegen gall, accaiuinm und dt. 
Hammer , s. u., vgl. Barth. IF. 2, 270, Hirt Abl. 137 : anord. hamarr „Fels, 



30 


at-, ak- 


Klippe ; Hammer (ursprgl. Steinwerkzeug), as. hatnur, ags. hamor, ahd. hamar, 
nhd. Hammer (vgl. zum r-St. oben ai. acmard-; Lit. bei Zupitza GG. 108); 
mit l statt r reiht Fick III 474 = Falk-Torp 377 an anord. hqmid-gryti n. 
„steiniger Boden, Ansammlung von kleinen runden Steinen unter der Erde“, 
norw. dial, humid „Stein“, mhd. hamel „steile Hohe, Klippe 11 . 1 ) 2 ) 

Hit n-Formantien : 

ai. agdni-h „Pfeilspitze, GeschoB :! (iiber agnail usw. s. o.), gr. axaiva 
„Spitze, Stachel; LangenmaB“ (aber iiber lat. acnna s. Yf. LEWb. 2 8 f.), 
axovij „ Wetzstein‘ : , dxcov , -vvrog „\YurfspieB“ (fiir alteres axcov, *-ovog nach 
den Participien, nicht nach Johansson Beitr. 9f. mit -t- als Nachwirkung 
einer Flexion *ak-r , gen. *a!,-n-t-os ), axovzi^co „schleudre den \VurfspieB“, 
dxavog „Distelart, dorniger Fruchtkopf einiger Pflanzen 11 , axavi&iv „dornige
```


## [2026-09-04T19:22:40.131Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TLM asan ===\"; grep -n \"asan\\|açan\\|aθanga\" TLM.txt | head -10\necho \"=== BRT saeni headword ===\"; grep -n \"saeni-\\|saēni-\\|Spitze, Wipfel\" BRT.txt | head -10\necho \"=== IEC 6195-6205 ===\"; sed -n '6195,6205p' IEC.txt"
}
```


### [2026-09-04T19:22:40.250Z] TOOL RESULT

```
=== TLM asan ===
100:JR  AS  =   Journal  of  Royal  Asiatic  Society Jud.  Pers.  =   Judaic  Persian Kas  =   KasanI
793:3.  0atiy  A[28]rtaxsa0ra  xsaya0i-22)ya  [29]imam4 *  ustasanam a0a”ga[3O]nam6  ma-23)m  upa6  mam  [31]karta
930:3[usta]canam  =   ustasanam,  Foy.
1084:a6a”gaina  or  a0a"gaina,  adj.  of  stone.  Nom.  sg.  m.  a$angaina, Dar.  Pei'S.  C.  ardastana  a$a"gaina.  Acc.  Sg.  f .   a6a"gainam,  Al’t.  Sus. c;  a0a"ganam  for  a$angainam,  Art.  Pers.  a,  b,  3.  YAv.  asanga  (New Pers.  sang,  Horn,  NS,  38,  2).  Cf.  KZ.  39,  69.
1185:avahana,  n.  dwelling  place.  Mom.  sg.  avahanam.  Skt.  vasana. a   -j-  *vah,  to  dwell ,   YAv.  vah,  Skt  .   vas.
1249:ud,  us,  adv.  up,  forth,  e.  g.  udapatata,  Bh.  2.  5,  et  passim;  us- tasana,  Art.  Pers.  1.  3.  Av.  us  (Middle  Pers.  uz,  New  Pers.  zi;  cf. Horn,  Grundr.  d.  neupers.  Etym.  143),  Skt.  ud.
1275:ustasana,  f.  staircase ,   Bauwerk  (IV B),  Treppe  (Bartholomae). AcC.  Sg.  ustasanam,  Al't.  Pers.  a,  b,  3.  imam  ustasanam  a^anganam mam  upa  mam  karta.  Foy  (IvZ,  35,  60)  reads  ustacanam  (=  ustasanam, cf.  xsayarcahya,  Al't.  Sus.  a,  1)  in  Art.  Sus.  C.  imam  +   +   +   +   4.  + canam  tya  a^angainam.  us  (see  ud)  -(-  *tasana,  fr.  "tas,  cut,  fashion , Av.  tas,  Skt.  taks.
1416:taxs  (Pres,  taxsa-,  Bartholomae,  Grunclr.  123),  to  be  active. Foy  regards  the  root  as  a   kompromissbildung  between  *tas  (Skt. taks,  Av.  tas  in  tasan)  and  "tvaxs  (Skt.  tvaks,  Av.  #waxs).
=== BRT saeni headword ===
=== IEC 6195-6205 ===
Skt. gávyam ‘herd’; Lat. tri-noctium; ON eski *ashwood box’; OCS trünije (thorns': trünü ‘thorn’)
-iios (-ios), à, om, adjectival extn. ofa noun- simplex; comparative extn. and agent-extn. Skt. gavyah, śunyah, dantyah, divyah; Per. abri ‘cloudy’; Gk. pátrios, taúreios, dios; Lat. pa- trius, taureus; OE cf. mōdrige “maternal aunt’; ON neytr ‘useful’; OCS divij ‘wild’; Li. cf. vedlýs, karvedys “leader; warrior beside moté&- rius ‘flirt’. For the comparative extn. (-iio-, -iión) cf. Skt. pürniyan; Gk. meízon, meíón; OS bet, leng "better, longer' beside ON neóri "Tower": OCS minij “less”, etc. For the agent- extn. cf. Lat. lüdius ‘actor’; OCS trobij *trum- peter’; Cz. krejčí ‘tailor’; Li. kogeus ‘librarian’ beside vedýs “leader”, etc.
ik- ‘squeal (onomat.)
Gk. cf. issa ‘whoop’; Cz. jikat, jiknout ‘squeal’; Li. vk, -ti, id.
-Ik-, Iks, derivate suffix Gk. cf. ámbix, gs -1ikos (‘spouted cup’, fr. ámb6); Lat. lendix, gs -1cis (' maggot”, fr. lens). Short vowel in Lat. imbrex, cimex (cf. Koim-), sorex, culex, gs -icis, and vier, -icis (cf. uit- beside uoit-)
-ikos, -ikà (1), diminutive extn.
Skt. avikab, -ā ‘ram; ewe’; gudika (pellet: gudah); balika (‘little gir: bala); Arm. matik (‘little finger’: mat); Snik (‘pup’: Sun, cf. Skt. Sunakah, dim. id.); Lat. canticus (‘song’: can- tus); cf. carrüca, beside carrus “little cart’; Bret. moedik (‘little thumb’: moed); OCS cf. otici (*daddy', cf. Gk. átta); potoðici ("little stream’: potokü); etc.; Li. kulikas (little bag’: kule); Sunikas (‘rascaľ’: Suð); cf. Li. avike *ewe-lamb'. For Cz. srnec (‘fallow deer: OCS srini 'roe- buck', see Krn-)
-ikos, -ikā (2) descriptive adj. extn. (often becoming the basis of an agent-noun)
Skt. cf. matrkah; Av. vorozika- (vorozo); Gk. statikós (stásis), kunikós (kuon); Lat. müricus (mūs), canticus (cantus); Osc. tüvtiks, toutico- (touto); Br. groenek (groen); W boneddig (bo-
sa a = -iiom (-iom) — -imos
20
```


## [2026-09-04T19:27:22.668Z] TOOL CALL #73: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /home/sfmqrb/git/rishe/data/verification/page-43.json <<'JSONEOF'\n{\n  \"pdf_page\": 43,\n  \"book_page\": 13,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ak, Aq, Aken\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂eḱ- (Pokorny *ak̑-, ok̑-) 'sharp, pointed; stone'; n-stem *h₂eḱ-en- (Pokorny/Kent *ak̑-en-) 'stone, whetstone' — Nourai's third variant 'Aken'\",\n      \"note\": \"Root box, language label and gloss are all right: Pokorny p.18 heads the lemma 'ak̑-, ok̑- (*hek-)  Meaning: \\\"sharp; stone\\\"' (POK_full.txt line 3242, Page(s): 18-22), i.e. exactly Nourai's 'sharp, also a sharp stone'; the n-stem 'Aken' is Kent's pIE *aken- (OP asan- 'stone') and Walde-Pokorny I 30 'Mit n-Formantien: ai. aśáni-ḥ ..., gr. ἀκόνη \\\"Wetzstein\\\"'. The whole chart hangs on Pokorny's own remark at the head of lemma k̑ē(i)-: 'Note: probably further formations from ak̑- \\\"sharp\\\" (see 18 ff.)', and the ak̑- entry reciprocally lists 'k̑ei-, k̑oi-, k̑ə(i)- \\\"sharpen, whet\\\"' among its zero-grade offshoots — so the root→#1 arrow is Pokorny's, flagged by him as 'probably'. THREE data points on this page are the author's own errors rather than scan errors (checked against the page image, pdftoppm p.43: the book really prints them): (a) node #2 files Sanskrit śāṇa- / abhi-śāṇa- ('čâna', 'abhi-čâna') under the Avestan box — Nourai regularly writes Sanskrit ś as č (cf. 'čvitra' = śvitra, 'črî' = śrī elsewhere in the book) and took the pair straight from Horn no. 98 ('skr. śāna- \\\"Wetzstein\\\" + abhi') and Pokorny 541 ('ai. śāna- m.'); (b) node #4's second Old Persian form 'asam' is not an OP word for stone (Kent's asam is the acc. of asa- 'horse'); it is a misreading of Mann IEC:11 'OPer. asa, asan-'; (c) node #3's 'fsân' is a misprint for fasân/fesân (the Persian script فسان on the same line is correct).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/hone\",\n        \"https://en.wiktionary.org/wiki/%CE%BA%E1%BF%B6%CE%BD%CE%BF%CF%82\",\n        \"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%BE%E0%A4%A3\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:18\", \"status\": \"supports\", \"note\": \"POK_full.txt line 3242 (starling dump of IEW): 'Root / lemma: ak̑-, ok̑- (*hek-) | Meaning: \\\"sharp; stone\\\" ... Page(s): 18-22'. The entry closes: 'zero grades k̑- stuck probably in stems k̑emen-, k̑emel-, k̑omen- \\\"stone, skies\\\", k̑omor- \\\"stone hammer\\\", k̑ei-, k̑oi-, k̑ə(i)- \\\"sharpen, whet\\\", k̑u- \\\"sharp, spit, spear\\\"' — i.e. Pokorny himself subordinates Nourai's node #1 to this root.\"},\n        {\"ref\": \"KNT:173\", \"status\": \"supports\", \"note\": \"KNT.txt lines 5118-5124 (page marker '173' at line 5118, entry straddles the p.172/173 column break): 'asan- sb. \\\"stone\\\": pIE *aken- (§9.V, §87, §155.I), cf. asman-. See also Asagarta-. asā (§124.5, §187) nsm. DSf 40f'. Kent p.173 thus gives precisely the root Nourai calls 'Aken' and the OP word of node #4.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 28 ff. (WLD_Bd1_1930_dli_70244_djvu.txt line 1964) and p. 30 (line 2093)\", \"stance\": \"supports\", \"note\": \"'ak̑- (z. T. auch ak-) \\\"scharf, spitz, kantig; Stein\\\"'; and under 'Mit n-Formantien:' 'ai. aśáni-ḥ \\\"Pfeilspitze, Geschoß\\\", gr. ἄκαινα \\\"Spitze, Stachel\\\", ἀκόνη \\\"Wetzstein\\\"' — the *ak̑-en- stem behind Nourai's 'Aken'.\"},\n        {\"src\": \"IEC\", \"where\": \"p. 11 s.v. akón- (IEC.txt line 377)\", \"stance\": \"supports\", \"note\": \"'akón- \\\"stone; whetstone\\\". WP 1, 30. Cf. akən-, Kōn-  Skt. asan; asánih; OPer. asa, asan-; Av. asa-nam, acc.; Per. san; Oss. ...; Arm. cf. h-esan (*epi-akon-?) \\\"whetstone\\\"; Gk. akóne ...' — Mann keeps 'stone/whetstone' under the a-root and explicitly cross-refers it to Kōn-, exactly the double filiation Nourai draws.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins s.v. kō- (AHD_watkins1985.txt line 642)\", \"stance\": \"supports\", \"note\": \"'kō-. To sharpen, whet. Contracted from *koə-. 1. Suffixed extended form *kōi-no- in Germanic *hainō in Old English hān, stone: HONE¹. 2. Perhaps Greek kōnos, cone, conical object (< \\\"a sharp-pointed object\\\"): CONE. [Pok. k̑ēi- 541.]' — Nourai's AHD-tagged nodes #5-#8 verbatim.\"},\n        {\"src\": \"KLN\", \"where\": \"s.v. hone, n. (KLN_1971.txt line 115322)\", \"stance\": \"supports\", \"note\": \"'hone, n., a whetstone. — ME. hoone ... fr. OE. hān, \\\"stone\\\", rel. to ON. hein ... and cogn. with OI. śiśāti, \\\"sharpens\\\", śāṇaḥ, \\\"whetstone\\\" ... Avestic saēni-, \\\"pointed; point, top of a tree\\\", ModPers. sāyad, \\\"rubs\\\" ... Gk. κῶνος ... L. cōs ... All these words derive fr. I.-E. base *k̑o(i)-, *k̑e(i)-, *k̑ə(i)-.' Klein assembles the whole of Nourai's entry 0 independently.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Indo-European\",\n          \"words\": \"Ke 1, Kei 3, Ko 1, Koi\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Nourai's four citation-forms reproduce Pokorny's homonym-numbered lemma 'k̑ē(i)- : k̑ō(i)- : k̑ə(i)- \\\"to sharpen, whet\\\"' (IEW 541-542); in laryngeal notation *ḱeh₃(i)- ~ *ḱeh₂s- 'to sharpen, whet'. The e-grade *ḱeh₃- underlies Skt. śiśāti/śyati 'sharpens', the o-grade *ḱoh₃-no- Gk. κῶνος and Skt. śāṇa- 'whetstone', the i-extended *ḱoh₃i-no- Gmc. *hainō > OE hān, and the ə-grade Lat. cōs, cotis 'whetstone' and catus 'sharp'. Pokorny derives this lemma from *ak̑- himself ('probably further formations from ak̑- \\\"sharp\\\", see 18 ff.'), which is the only warrant for the root→#1 arrow: the two lemmata are printed separately in IEW, and Watkins/AHD lists kō- as an independent root (referring back only 'Pok. k̑ēi- 541'), so the connection is Pokorny's conjecture, not a consensus reconstruction.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:541,542\", \"status\": \"supports\", \"note\": \"POK_full.txt lines 51031-51068: 'Root / lemma: k̑e(i)- : k̑ō(i)- : k̑ə(i)- | Meaning: to sharpen, whet | Note: probably further formations from ak̑- \\\"sharp\\\" (see 18 ff.) ... References: WP. I 454 f., WH. I 181, 183 f., 190 f. | Page(s): 541-542'. Nourai's two page numbers and the parentage arrow are both exactly here.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"WP I 454 f. (WLD_Bd1 lines 28580-28605)\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny I 454: 'Ai. śāna-ḥ \\\"Wetzstein, Probierstein\\\" ... = np. sān, af-sān, pasān, pa-sān \\\"Wetzstein\\\" ... = gr. κῶνος \\\"Kegel, Pinienzapfen, Helmspitze\\\"; Av. saēni-š \\\"Spitze, Wipfel\\\" ...; Anord. hein, ags. hān \\\"Schleifstein\\\"; Lat. cōs, cotis \\\"Wetzstein\\\"' — the same set of descendants.\"},\n            {\"src\": \"AHD\", \"where\": \"s.v. kō- (AHD_watkins1985.txt line 642)\", \"stance\": \"partial\", \"note\": \"'kō-. To sharpen, whet. Contracted from *koə-. ... [Pok. k̑ēi- 541.]' — same root and gloss, but Watkins lists it as an independent root and does not derive it from ak̑-.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §12.72 area (SYN.txt line 1628)\", \"stance\": \"supports\", \"note\": \"'Skt. śilā- \\\"stone, rock\\\" : śita- \\\"sharp\\\", śā-, śī- \\\"sharpen\\\", Lat. cōs \\\"whetstone\\\", ON hein \\\"whetstone\\\", OE hān \\\"stone\\\", ME honne, NE hone \\\"whetstone\\\". Walde-P. 1.454.'\"},\n            {\"src\": \"CHEUNG\", \"where\": \"p. 325 s.v. *saH\", \"stance\": \"supports\", \"note\": \"Cheung 2007 files the Iranian verb under '«PIE *ḱeHs- \\\"to sharpen, whet\\\" = LIV: 319 f. | Pok.: 541 f.', with IE cognates 'Lat. cōs \\\"whetstone\\\", catus \\\"sharp(-minded)\\\", OIrish cath \\\"wise\\\", Arm. sur \\\"sharp\\\", ON hein (f.) \\\"whetstone\\\"' — the modern (laryngealist) form of Nourai's node.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. cone, n. (KLN_1971.txt line 53536)\", \"stance\": \"supports\", \"note\": \"'... fr. I.-E. base *k̑o(i)-, *k̑e(i)-, \\\"sharp, whet; to sharpen, whet\\\", whence also OE. hān, \\\"stone\\\", ON. hein, \\\"hone\\\"' — Klein's base is letter-for-letter Nourai's 'Ke, Kei, Ko, Koi'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Avestan\",\n          \"words\": \"saěni, saěniš, čâna; asânam; abi-čâna, abhi-čâna\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Only the first word and 'asânam' are Avestan. (i) Av. saēni- (nom. sg. saēniš) 'point, tip, treetop; sharp' is genuine and goes back to *ḱoh₃i-ni-, the exact i-stem match of Gmc *hainō (Pokorny 542: 'Avestan saēni- \\\"cusp, peak, treetop, sharp\\\" ... = Old Norse hein'; Bartholomae AiW has the compound saēni.kaofa- 'with a pointed, i.e. erect hump', of a camel). (ii) 'čâna' and 'abi-čâna, abhi-čâna' are NOT Avestan: they are Sanskrit śāṇa- 'whetstone, touchstone' and abhi-śāṇa- 'grinding stone'; Nourai renders Sanskrit ś as č (cf. his 'čvitra' = śvitra, 'črî' = śrī, 'čiphâ' = śiphā) and lifted the pair from Horn no. 98 ('skr. śāna- \\\"Wetzstein\\\" + abhi') and Pokorny 541 ('ai. śāna- m. \\\"whetstone, touchstone\\\" (= npers. sān)'). The prefix abhi- is itself the giveaway: Avestan has aiwi-, not abhi-. (iii) 'asânam' is the accusative of Av. asan- 'stone' (Bartholomae s.v. asan-/asman- m. 'Stein'), which belongs to the *ak̑-en- stem of the root box, not to *ḱē(i)-; Mann IEC:11 files it under akón- 'stone; whetstone'. So the box is a conflation of Avestan, Sanskrit and two different PIE stems, though every individual form is real and every one of them does descend from the root complex Nourai draws.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%BE%E0%A4%A3\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:542\", \"status\": \"partial\", \"note\": \"POK_full.txt line 51046: 'Avestan saēni- \\\"cusp, peak, treetop, sharp\\\" (npers. sāyad \\\"reibt\\\") = Old Norse hein' — supports saēni-; but the whetstone words on the same page are given by Pokorny (line 51037) as 'Old Indic ... śāna- m. (with Middle Indic ṇ for n) \\\"whetstone, touchstone, yardstick, criterion\\\" (= npers. sān \\\"whetstone\\\")', i.e. Sanskrit, not Avestan, and Pokorny has no Avestan asānam at all under this lemma.\"},\n            {\"ref\": \"SNS:18\", \"status\": \"partial\", \"note\": \"SNS.txt line 33843 (Tavoosi's index): 'afsan 18/19' — the word does stand at p.18 l.19 of the Shāyast nē-shāyast glossary, and Horn no.98 cites the same passage ('phlv. afsān (Šāy. Nēšāy. 10, 28)'). But that form is Pahlavi afsān 'whetstone', evidence for node #3, not for an Avestan headword.\"},\n            {\"ref\": \"IEC:11\", \"status\": \"supports\", \"note\": \"IEC.txt line 377 (page-11 header at line 373 'aknis, os, à — aktros'): 'akón- \\\"stone; whetstone\\\". WP 1, 30 ... Av. asa-nam, acc.; Per. san ...' — Mann's page 11 gives exactly 'asānam' as an Avestan accusative, and the gloss 'whetstone' Nourai attaches to it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"s.v. asan- / asman- (BRT.txt line 5724; AiW col. 207, cited by Kent)\", \"stance\": \"partial\", \"note\": \"Bartholomae: 'asan-, j., p. asman- m. 1) \\\"Stein\\\"' with Vidēvdād and Yašt citations (sling-stone, amulet); he glosses it 'Stein', never 'Wetzstein'. He has no headword čāna; saēni- appears only in the compound 'saēni.kaofa- Adj. \\\"(mit spitzem, d. i.) gerade aufgerichtetem, steifem Höcker\\\"' (BRT.txt line 25797).\"},\n            {\"src\": \"HRN\", \"where\": \"no. 98, p. 24 (HRN.txt line 1276)\", \"stance\": \"contradicts\", \"note\": \"Horn expressly labels the form Sanskrit: 'efsān \\\"Wetzstein\\\", eusān, fesān, vergl. sān, phlv. afsān (Šāy. Nēšāy. 10, 28); skr. śāna- \\\"Wetzstein\\\" + abhi; vergl. arm. yesan.' Nourai's 'abhi-čâna' is this line, mis-shelved in an Avestan box.\"},\n            {\"src\": \"WLD\", \"where\": \"WP I 454 (WLD_Bd1 lines 28584-28592)\", \"stance\": \"contradicts\", \"note\": \"'Ai. śāna-ḥ \\\"Wetzstein, Probierstein\\\" (eigentlich mind. aus *śana-ḥ, = np. sān, af-sān ...)' stands in the Indic paragraph; the Avestan paragraph two lines below gives only 'Av. saēni-š \\\"Spitze, Wipfel\\\", saēni-kaofa-'. Walde-Pokorny keeps the two languages apart.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. hone, n. (KLN_1971.txt line 115325)\", \"stance\": \"supports\", \"note\": \"'... OI. śāṇaḥ, \\\"whetstone\\\" ... Avestic saēni-, \\\"pointed; point, top of a tree\\\"' — same two forms, again with the whetstone word assigned to Old Indic.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"sâyîdan; fesânîdan; fsân\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are real New Persian words with the glosses given, and all three continue the root of node #1 through Iranian. (1) sāyīdan 'to grind, rub' is a secondary infinitive built on the present stem sāy- of MP sūdan / sāy- [swtn' / s'd-] 'to rub, wear' (MacKenzie; Wiktionary: 'inherited from Middle Persian sūdan, present stem sāy-; regularized from the older infinitive سودن'), from Proto-Iranian *sauH- 'to rub, wear, whet' (Cheung 2007: 340), itself a ua-variant of *saH < PIE *ḱeh₂s-/*ḱeh₃(i)-. Pokorny cites the Persian present directly at 542 ('npers. sāyad \\\"reibt\\\"'). The chart's own extra forms سای، ساو (present stems sāy/sāv), سان and سوهان are the same family: NP sān 'whetstone' = Skt. śāṇa- (Pokorny 541 'npers. sān'; WP I 454 'np. sān, af-sān, pasān'). (2) fasān/afsān 'whetstone' < Middle Persian afsān < Old Iranian *abi-sāna- (Horn no. 98: 'phlv. afsān (Šāyast nē-šāyast 10,28); skr. śāna- + abhi'; the Pamir cognates pasān/pisen < *pati-sāna- and Yidgha āfseno < *abi- confirm the prefixal type: Cheung 326). The doublet afsān ~ fasān is the regular New Persian aphaeresis of unstressed initial a- before a consonant cluster (Hübschmann Pers. St. §3: 'afsān \\\"Wetzstein\\\" = fasān H. 98', beside afsurdan = fusurdan, afgandan = figandan). (3) fesānīdan 'to grind, rub' is a denominative made in New Persian from fasān + the infinitive suffix -īdan — Mo'in's footnote in Borhān-e Qāṭeʿ p.1488 says exactly that: 'از: فسان (سنگ) + یدن (پسوند مصدری)' ('from fasān (stone) + -īdan, the infinitive suffix'). NOTE on the data: the printed transliteration 'fsân' is impossible as a Persian word (no initial fs- cluster) and is Nourai's own typo for fasân/fesân — the Persian script فسان (افسان) beside it is correct; this is in the book itself, not an extraction error.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%D8%A7%DB%8C%DB%8C%D8%AF%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%AF%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%B3%D8%A7%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:542\", \"status\": \"supports\", \"note\": \"POK_full.txt line 51046: 'Avestan saēni- ... (npers. sāyad \\\"reibt\\\")' and line 51038 '(= npers. sān \\\"whetstone\\\")' — Pokorny's page 541-542 does carry both the Persian verb and the Persian whetstone noun.\"},\n            {\"ref\": \"BQT:1077\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ vol. 2 (BQT_v2_pages.txt, leaves 539-540, printed pp. ≈1076-1082 — the offset is independently pinned by Aryanpur, who cites 'برهان قاطع: ۱۰۷۶-۷' under the very same headword سان): 'سان ... مطلق سوهان را نیز گفته‌اند ... و فسان را گفته‌اند و آن سنگ باشد که کارد و شمشیر و غیره بدان تیز کنند' ('sān ... also used absolutely for a file (sūhān) ... and they say fasān, which is the stone on which knife and sword are sharpened'), and on the next leaf 'سای ... فاعل ساییدن را گویند که ساینده باشد' ('sāy: the agent of sāyīdan') and 'ساو ... بمعنی مطلق سودن و ساییدن باشد'. Exactly the نode's words and the chart's extra forms سای، ساو، سان، سوهان.\"},\n            {\"ref\": \"BQT:1488\", \"status\": \"supports\", \"note\": \"Fetched with tools/ref_page.py BQT:1488 (vol. 3 pdf p.281; cached at data/verification/sources/refs/ocr/BQT/1488.png|.txt): 'فسان ← بفتح اول بروزن زبان، سنگی باشد که کارد و شمشیر بدان تیز کنند' ('fasān: a stone on which knife and sword are sharpened'), 'فسانیدن ← بر وزن رسانیدن، بمعنی مالیدن و راست کردن' ('fasānīdan: to rub and make straight'), with Moʿin's footnotes 'رك: افسان، ارسان، سان' and '۸ از: فسان (سنگ) + یدن (پسوند مصدری)', plus Farroḵi Sistāni's line 'چه حاجتی بفسان روز رزم تیغ تو را'. Supports both fasān and fasānīdan and Nourai's spelling variant افسان.\"},\n            {\"ref\": \"SNS:18\", \"status\": \"supports\", \"note\": \"SNS.txt line 33843 (index of Tavoosi's Shāyast nē-shāyast glossary): 'afsan 18/19'; the glossary entry itself is at SNS.txt line 1657 (OCR unusable). This is the Pahlavi antecedent afsān that Horn no. 98 also cites from the same text ('Šāy. Nēšāy. 10, 28').\"},\n            {\"ref\": \"MMF:325\", \"status\": \"not_checked\", \"note\": \"Khalili, Farhang-e Moshtaqqāt-e Maṣāder-e Fārsi — refs_online.json marks it 'login_required' (ketabnak.com/book/127793 etc.), no local text and no open copy; could not be consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 98 (p. 24) and no. 752 (p. 165) — HRN.txt lines 1276-1279, 6561-6566\", \"stance\": \"supports\", \"note\": \"no. 98: 'efsān \\\"Wetzstein\\\", eusān, fesān, vergl. sān, phlv. afsān (Šāy. Nēšāy. 10, 28); skr. śāna- \\\"Wetzstein\\\" + abhi; vergl. arm. yesan. — wax. sar. pasān \\\"Wetzstein\\\".'  no. 752: 'sūden \\\"reiben\\\", Praes. sāy-em, sāyīden. ai. √śā- \\\"wetzen, schärfen\\\". kurd. sūin, sūn \\\"reiben, ein Messer reiben, schärfen\\\". Die Bedeutung ist im Neupersischen verblasst.'  Horn also has a cross-entry '(1)sān \\\"Wetzstein\\\". Siehe efsān (No. 98)' (line 6095) with a note on np. sunbāde.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien §3 (p. 41) and Nachträge no. 752 — HUB.txt lines 6127, 7471, 2705\", \"stance\": \"supports\", \"note\": \"'afsān \\\"Wetzstein\\\" = fasān H. 98' in Hübschmann's list of New Persian aphaeresis doublets (beside afzūdan = fuzūdan, afgandan = figandan); 'afsān \\\"Wetzstein\\\", afsar \\\"Krone\\\", pāsux \\\"Antwort\\\" ...'; and at no. 752 (the sūdan entry) 'Vgl. sān und afsān \\\"Wetzstein\\\"'.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary, s.v. afsūtak/apa-sūtak (NYB_vol2_glossary.txt line 546)\", \"stance\": \"supports\", \"note\": \"'Cf NP afsūn ... undoubtedly to be connected with NP sūdan sāy-, farsūdan farsāy (< *fra-) \\\"to rub\\\" ... However, the corresponding OInd. vb. śā- means \\\"to sharpen, to whet\\\" (śita- \\\"sharp\\\"), a sense also attested in Ir.: NP afsān, ausān \\\"whetstone\\\"; MPrs hswd = hassūd < *ham-sūt \\\"whetted\\\" of a sword (Henning, BSOAS XII, 1947, 45), directly to be compared with OInd (RV) sam-śā- \\\"to whet\\\".'\"},\n            {\"src\": \"CHEUNG\", \"where\": \"pp. 325-326 s.v. *saH, p. 340 s.v. *sauH¹\", \"stance\": \"supports\", \"note\": \"*sauH¹ 'to rub, wear, whet': 'BMP s'd- /sāy-/ \\\"to rub, wear\\\" ... Inf.: BMP swtn /sūdan/ ... NP sūdan/sāy- \\\"to rub, wear, tear\\\"'; *saH 'to whet, cut' < 'PIE *ḱeHs- \\\"to sharpen, whet\\\"' with '(+ *abi- ?) Yi. áfseno \\\"whetstone\\\"' and '(+ *pati-) Sh. pisen ... \\\"whetstone, hone\\\"' — the prefixed *abi-sāna- type behind afsān.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p. 5 (PHD.txt line 172; PHD_mackenzie.txt line 880)\", \"stance\": \"partial\", \"note\": \"MacKenzie has 'afsān [ʾpsʾn' | (M ʾpsʾng), N afsāna] story, fable' — i.e. the homonym afsān 'tale', and does NOT list a Pahlavi afsān 'whetstone'; he does list the verb (v. sūdan/sāy-). So the MP whetstone form rests on Horn's Shāyast nē-shāyast citation, not on the Concise Pahlavi Dictionary.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi, p. 339 (ARY_pages.txt lines 9995-10010, pdf page 338)\", \"stance\": \"supports\", \"note\": \"Headword 'سان، سوهان، افسان' with cognates ŚĀNA (Skt.), KŌNOS (Gk.), CŌS (Lat.), HEIN (ON), HĀN (OE), HONE (Eng.), and the note 'واژه‌های فارسی «ساییدن» و «آسودن» و «بسودن» نیز از همین واجریشه‌اند (POK:542)' ('the Persian words sāyīdan, āsūdan and basūdan are from the same root'); his own sources are given as برهان قاطع ۱۰۷۶-۷, فرهنگ معین and لغت‌نامه دهخدا — an independent modern Persian confirmation of Nourai's node and of his BQT page.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Old Persian\",\n          \"words\": \"asa, asam\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Old Persian asan- 'stone' is real: nominative asā, attested once, in Darius' Susa foundation charter DSf 40-41 (the list of building materials). It reflects PIE *h₂eḱ-en- (Kent: 'pIE *aken-'), with s for inherited *ḱ — a Median, not a genuine Old Persian, treatment (native OP would give θ, cf. aθangaina- 'of stone'); the word is therefore a Median loan in the royal inscriptions, and it survives as NP sang 'stone' only through the parallel form asanga-. It belongs to the root box *ak̑-/*ak̑-en-, not to node #1 *ḱē(i)-, and Nourai has hung it on the wrong parent (Mann, his source, files it under akón-, the a-root). Two further problems: 'asam' is not an Old Persian word for stone — Kent's asam is the accusative of asa- 'horse' — and is a misreading of Mann's 'OPer. asa, asan-'; and Kent glosses asan- simply 'stone', the gloss 'whetstone' being Mann's label for the reconstructed stem, not for the Old Persian word.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"IEC:11\", \"status\": \"partial\", \"note\": \"IEC.txt line 377: 'akón- \\\"stone; whetstone\\\". WP 1, 30. Cf. akən-, Kōn-  Skt. asan; asánih; OPer. asa, asan-; Av. asa-nam, acc.; Per. san ...' — Mann gives 'asa, asan-', not 'asa, asam', and files the whole group under the a-root, so IEC:11 supports the word but not the form 'asam' nor the parent Nourai draws.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"Lexicon p. 172/173 (KNT.txt line 5117) and Grammar §87 (line 1152)\", \"stance\": \"partial\", \"note\": \"'asan- sb. \\\"stone\\\": pIE *aken- (§9.V, §87, §155.I), cf. asman-. See also Asagarta-. asā (§124.5, §187) nsm. DSf 40f.' and §87 '(with Med. s) asan- \\\"stone\\\"'. Kent confirms the stem and the nominative asā, glosses it 'stone' (not whetstone), and gives no form 'asam' for it — his asam (line 1192) is 'OP asa- in acc. asam', the word for 'horse' (pIE *eḱwo-).\"},\n            {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon s.v. aθangaina (TLM.txt line 1084)\", \"stance\": \"silent\", \"note\": \"Tolman lists only 'aθangaina, adj. of stone ... YAv. asanga (New Pers. sang, Horn NS 38,2)'; he has no entry asan-/asā, so the OP simplex is not corroborated there.\"},\n            {\"src\": \"BRT\", \"where\": \"s.v. asan-/asman- (BRT.txt line 5724)\", \"stance\": \"supports\", \"note\": \"Bartholomae AiW 207: 'asan-, j., p. asman- m. 1) \\\"Stein\\\"' — the Avestan/Old Persian n-stem exists and means 'stone', which is what Kent's OP asan- continues.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Germanic\",\n          \"words\": \"hainô\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *hainō f. 'whetstone' < PIE *ḱoh₃i-neh₂-, the i-extended o-grade of node #1 — the exact formal match of Avestan saēni- (Pokorny 542: 'Old Icelandic hein \\\"whetstone\\\", Old English hān \\\"boundary stone\\\" ... (*ḱai-n- : Avestan saēni-)'). The regular Germanic outcomes are Old Norse hein 'whetstone', Old English hān 'stone, rock, boundary stone'; PIE *ḱ > Gmc *h by Grimm's Law, *oi > Gmc *ai > OE ā. MHG har 'scythe-sharpening tool' (*ḱē-r-) and MLG haren 'to sharpen' belong to the same nest.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/hone\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 642, s.v. kō-: '1. Suffixed extended form *kōi-no- in Germanic *hainō in Old English hān, stone: HONE¹.' Nourai's Germanic box is this clause; the only difference is his gloss 'grinding stone' where Watkins writes 'stone'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 542 (POK_full.txt line 51064)\", \"stance\": \"supports\", \"note\": \"'Old Icelandic hein \\\"whetstone\\\", Old English hān \\\"boundary stone\\\", engl. hone \\\"whetstone\\\" (*ḱai-n- : Avestan saēni-); Middle High German har \\\"tools to sharpen the scythe\\\" (*ḱē-r-), Middle Low German haren \\\"sharpen, be sharp\\\".'\"},\n            {\"src\": \"WLD\", \"where\": \"WP I 454 (WLD_Bd1 line 28596)\", \"stance\": \"supports\", \"note\": \"'Anord. hein, ags. hān \\\"Schleifstein\\\".'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Hone (SKT.txt line 8788 ff.)\", \"stance\": \"supports\", \"note\": \"'Hone. (E.) A.S. hān, a hone ... + Icel. hein, Swed. hen; Skt. śāna, a whetstone. From √ŚĀ, to sharpen; Gk. κῶνος, a cone. See Cone.' (OCR garbled but legible).\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"hone\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English hān 'a stone, rock, (boundary) stone' > Middle English hoon(e)/hone, with regular OE ā > ME ǭ > ModE /oʊ/ (as in stān > stone, bān > bone). The sense narrowed in early 14c. to 'a fine-grained stone for putting a delicate edge on a blade'; the verb 'to sharpen on a hone' is first recorded 1788 (the older ME hēnen/OE hǣnan 'to pelt with stones' is a separate formation). Straight inheritance from node #5, no borrowing involved.\",\n          \"sources\": [\"https://www.etymonline.com/word/hone\", \"https://en.wiktionary.org/wiki/hone\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 642: '... in Old English hān, stone: HONE¹' — HONE is the English keyword Watkins hangs on the Germanic form, exactly Nourai's arrow #5 → #6.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. hone, n. (KLN_1971.txt line 115322)\", \"stance\": \"supports\", \"note\": \"'hone, n., a whetstone. — ME. hoone, \\\"hone\\\", fr. OE. hān, \\\"stone\\\", rel. to ON. hein, \\\"hone\\\", and cogn. with OI. śiśāti \\\"sharpens\\\", śāṇaḥ \\\"whetstone\\\" ... All these words derive fr. I.-E. base *k̑o(i)-, *k̑e(i)-, *k̑ə(i)-.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Hone (SKT.txt line 8788)\", \"stance\": \"supports\", \"note\": \"Skeat derives E. hone from A.S. hān and refers it to the same root as Cone.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/hone (archived)\", \"stance\": \"supports\", \"note\": \"'Old English hān \\\"a stone, rock, (boundary) stone,\\\" from Proto-Germanic *hainō', PIE root 'to sharpen, whet'; the whetstone sense from early 14c., the verb from 1788.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Greek\",\n          \"words\": \"kônos\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Ancient Greek κῶνος m. 'pine cone; peak of a helmet; spinning top; geometric cone' would be *ḱoh₃-no-, the o-grade thematic noun of node #1 and the exact equation of Sanskrit śāṇa- 'whetstone' (Pokorny 541: 'gr. κῶνος m. \\\"cone, a pine-cone, the cone of a helmet, top\\\" (= Old Indic śāna-)'; the semantic bridge in Walde-Pokorny I 454 is 'ursprüngl. etwa \\\"von der Gestalt eines Wetzsteins\\\"'). Two reservations keep this from 'confirmed': Watkins himself hedges ('Perhaps Greek kōnos'), and Schwyzer, Furnée and Beekes treat κῶνος as a Pre-Greek (substrate) word, which is the position Wiktionary now records. Nourai's gloss 'sharp pointed, cone' is the traditional reading of the semantics, not an attested Greek meaning 'sharp'.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CE%BA%E1%BF%B6%CE%BD%CE%BF%CF%82\", \"https://www.etymonline.com/word/cone\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt line 642: '2. Perhaps Greek kōnos, cone, conical object (< \\\"a sharp-pointed object\\\"): CONE.' Watkins gives Nourai's derivation but marks it 'Perhaps'; Nourai drops the hedge.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 541 (POK_full.txt line 51057)\", \"stance\": \"supports\", \"note\": \"'gr. κῶνος m. \\\"cone, a pine-cone, the cone of a helmet, top\\\" (= Old Indic śāna-), therefrom κώνειον \\\"hemlock, Conium maculatum\\\" (after the leaves)'.\"},\n            {\"src\": \"WLD\", \"where\": \"WP I 454 (WLD_Bd1 lines 28585-28590)\", \"stance\": \"supports\", \"note\": \"'= gr. κῶνος \\\"Kegel, Pinienzapfen, Helmspitze, der kegelförmige Kreisel\\\" (urspgl. etwa \\\"von der Gestalt eines Wetzsteins\\\")'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. cone, n. (KLN_1971.txt line 53536)\", \"stance\": \"supports\", \"note\": \"'Gk. κῶνος, \\\"pine cone, fir cone, cone; peak\\\", which is cogn. with OI. śāṇaḥ \\\"whetstone\\\", L. cōs ... catus \\\"sharp\\\", fr. I.-E. base *k̑o(i)-, *k̑e(i)-.'\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/κῶνος (archived)\", \"stance\": \"partial\", \"note\": \"Gives *ḱóh₃nos < *ḱeh₃- 'to sharpen' with cognates Skt. śāṇa, Lat. cōs, catus, but records the competing view of Schwyzer, Furnée and Beekes that κῶνος is a Pre-Greek borrowing.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"cone\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A learned borrowing, not an inheritance: Greek κῶνος was taken into Latin as cōnus 'cone, peak of a helmet', thence Middle French cône (16th c.), and English cone appears in the 1560s first as the geometer's solid and as 'pine cone', later extended to volcanic cones (1771), the retinal cones (1867) and the ice-cream cone (1909). The chart's arrow #7 → #8 elides the Latin and French stages but is otherwise right; note that English therefore has the same PIE etymon twice, inherited in hone (#6) and borrowed in cone (#8).\",\n          \"sources\": [\"https://www.etymonline.com/word/cone\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 642: '... Greek kōnos, cone, conical object: CONE.' CONE is the English keyword Watkins attaches to the Greek word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. cone, n. (KLN_1971.txt line 53536)\", \"stance\": \"supports\", \"note\": \"'cone, n. — F. cône, fr. L. conus, fr. Gk. κῶνος ... See hone and cp. conarium, Conium.' Klein spells out the F < L < Gk route Nourai's single arrow compresses.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Cone (SKT.txt line 3921)\", \"stance\": \"supports\", \"note\": \"'Cone. (F. — L. — Gk.) ... Gk. κῶνος, a cone ... L. cunus, a wedge' — Skeat's language chain '(F. — L. — Gk.)' is the borrowing route.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/cone (archived)\", \"stance\": \"supports\", \"note\": \"'konos \\\"cone, spinning top, pine cone\\\"' > L. conus > French cone (16c.) > English 1560s; cognates given as 'Sanskrit sanah \\\"whetstone\\\", Latin catus \\\"sharp\\\", Old English han \\\"stone\\\"'.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Akos, Âkos\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *-ko- / *-h₂ko- (Wiktionary Reconstruction:*-kos), a denominal/deadjectival adjective suffix; Indo-Iranian *-ka-, *-aka- with secondary diminutive value\",\n      \"note\": \"The suffix itself is beyond doubt and Nourai's citation is exact — Mann's Indo-European Comparative Dictionary p.9 has the lemma verbatim. What is only 'plausible' is the gloss on the root box. Modern reconstruction (Wiktionary s.v. *-kos, and the standard handbooks) treats PIE *-ko- as an adjective-forming suffix, 'characteristic of, pertaining to'; the diminutive value is a post-PIE development shared by Indo-Iranian, Balto-Slavic, Greek (-ίσκος) and Germanic, not a reconstructible PIE function. Nourai's own cross-reference on the Persian node ('See \\\"Kak\\\" for another possible root of suffix \\\"-ak\\\"') shows he was aware the etymology is contested. A second, purely Iranian caveat runs through both Persian nodes: the Middle Persian suffix -ag/-ak regularly yields New Persian -a (کنیزگ > کنیزه), and Hübschmann concluded that the New Persian diminutive in -ک is 'wohl jüngeren Ursprungs' than that general suffix, so the arrow Pahlavi -ak → Persian -ak is a simplification of a messier history.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-kos\"],\n      \"ref_check\": [\n        {\"ref\": \"IEC:9\", \"status\": \"supports\", \"note\": \"IEC.txt line 344, on the page whose running head (line 331) is '9 akmó(n), akmen- — akmo(n), aḱmen-': '-akos, -ākos (diminutive suffix)  Skt. -akah, -aka; Per. -ak; Arm. -ak; Alb. -ok; W og; OCS -akŭ; Li. -okas (in adjj.)'. Nourai's root name, language label, gloss and both daughter nodes are this one line of Mann.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"IEC\", \"where\": \"p. ~20 s.v. -ikos, -ikā (1) (IEC.txt line 6201)\", \"stance\": \"supports\", \"note\": \"Mann has a parallel lemma '-ikos, -ikā (1), diminutive extn.' with 'Skt. avikaḥ \\\"ram; ewe\\\"; guḍikā (\\\"pellet\\\": guḍaḥ); bālikā (\\\"little girl\\\": bālā) ... cf. Skt. śunakaḥ, dim.' — the k-suffix diminutive is well attested in Indo-Iranian, which is the empirical basis of Nourai's box.\"},\n        {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/-kos (archived)\", \"stance\": \"partial\", \"note\": \"'Creates deadjectival and desubstantival adjectives denoting the characteristic of, typical of, pertaining to'; descendants include Proto-Indo-Iranian *-kas. No diminutive function is listed — i.e. the form is confirmed, the gloss 'suffix indicating small size' is not, for PIE.\"},\n        {\"src\": \"GPL\", \"where\": \"Platts & Ranking, Grammar of the Persian Language, pp. 135-136 (GPL.txt lines 1792-1798)\", \"stance\": \"supports\", \"note\": \"'Diminutives. These suffixes are added to nouns to form diminutives ... the unreduced Phl. suffix -ak ... is more commonly employed; e.g. دخترک \\\"little daughter, little girl\\\" (from دختر) ... کودک \\\"boy, lad, child\\\" (Phl. kutak; Z. kutaka \\\"little\\\"; cf. S. kṣudraka)' — the Sanskrit, Pahlavi and Persian members of Nourai's box, treated together as one diminutive suffix.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"-ak\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Middle Persian suffix is written <ʾk> in Book Pahlavi and <-g> in Manichaean script; MacKenzie transcribes it -ag, older handbooks (and Nourai) -ak. It continues Old Iranian *-aka- (Av. -aka-, OP -aka-) < PIE *-ko-, and is by far the commonest derivational suffix of Middle Persian: dast 'hand' → dastag, kanīz → kanīzag, murw 'bird' → murwag. Its function in MacKenzie's definition is not diminutive but simply derivational — 'suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems' — and its regular New Persian reflex is -a (kanīzag > kanīza, bandag > banda), not -ak; the diminutive value that Nourai's root box asserts is only sporadically visible in Middle Persian itself. So the node's form and ancestry are right, its gloss (inherited from the root box) is a New Persian back-projection.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"MON:2775\", \"status\": \"not_checked\", \"note\": \"Moʿin's six-volume Farhang-e Fārsi is not available in any scan (refs_online.json: 'still no scan of the 6-vol Amir Kabir edition ... The 6-vol set is purchase-only'), so page 2775 itself could not be opened. The only accessible Moʿin is the 2-volume Adena condensation, whose suffix entry is quoted on node #2; it carries no Pahlavi Latin-script etymon, the feature Nourai is citing.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p. 5 s.v. -ag (PHD.txt line 172)\", \"stance\": \"partial\", \"note\": \"'-ag [-k' | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.' The suffix exists and is written -k, but MacKenzie gives its New Persian outcome as -a and assigns it no diminutive value.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. sālak and kanīcak (NYB_vol2_glossary.txt lines 3385, 2197)\", \"stance\": \"supports\", \"note\": \"Nyberg treats -ak as a live Pahlavi suffix ('in repetitions the suff. -ak may be added to the last sāl only'), and glosses kanīcak [knyck'] as the ordinary Pahlavi word for 'girl' — the form that underlies both NP kanīza and NP kanīzak.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §137a, pp. 244-245 (HUB.txt lines 8745-8752)\", \"stance\": \"partial\", \"note\": \"'im deminutiven Suffix -ak, das wohl jüngeren Ursprungs als das allgemeine Pehlevisuffix ak = np. a ist: mardak \\\"Männlein\\\" von mard \\\"Mann\\\", andak \\\"wenig\\\" von and \\\"soviel\\\" etc.' — Hübschmann separates the New Persian diminutive -ak from the general Pahlavi -ak, which is precisely the arrow Nourai draws.\"},\n            {\"src\": \"GPL\", \"where\": \"Platts, Grammar of the Persian Language p. 135 (GPL.txt line 1792)\", \"stance\": \"supports\", \"note\": \"'the unreduced Phl. suffix -ak ... is more commonly employed' for diminutives — Platts derives the Persian diminutive directly from the Pahlavi suffix, as Nourai does.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"-ak\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"New Persian ـک /-ak/ is a productive diminutive: مرغک murġak 'little bird' (from مرغ), کنیزک kanīzak 'young slave-girl' (from کنیز) — both of them the chart's own examples, and both listed as diminutives by Moʿin ('کنیزک: زن خرد' = 'a small woman') and by Hübschmann ('Np. kanīzak ist durch das Deminutivsuffix ak von kanīz abgeleitet'). Moʿin's entry for the suffix opens with exactly Nourai's gloss: it is added to a noun or a substantivised adjective and expresses 'تصغیر، کوچکی' (diminution, smallness), then endearment, delicacy, contempt, and reduction. The reservation is on the route: the ordinary phonetic continuation of MP -ag in New Persian is -a (Phl. kanīčak → np. kanīza, Hübschmann no. 870), so -ak with its k preserved is either the 'unreduced' variant (Platts) or, in Hübschmann's judgement, a younger formation on the same inherited *-aka-; either way Nourai's single arrow Pahlavi -ak → Persian -ak understates the doublet. Nourai's own note 'See \\\"Kak\\\" for another possible root of suffix \\\"-ak\\\"' concedes an alternative.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"IEC:9\", \"status\": \"supports\", \"note\": \"IEC.txt line 344 (page 9): '-akos, -ākos (diminutive suffix)  Skt. -akah, -aka; Per. -ak; Arm. -ak; ...' — Mann lists 'Per. -ak' as the Persian reflex, exactly this node.\"},\n            {\"ref\": \"MON:2775\", \"status\": \"partial\", \"note\": \"The 6-volume edition p.2775 is not obtainable (no scan exists), but the corresponding entry survives in the 2-volume Adena condensation of Moʿin, MON_part2.txt line 16694: 'ک ... (پس.) بصورت پسوند به آخر اسم یا صفتی که بجای اسم نشیند ملحق گردد و آن به معناهای ذیل آید: تصغیر، کوچکی؛ تحبیب، دلسوزی و ترحم؛ لطافت، ظرافت؛ تحقیر، توهین؛ تقلیل، اندکی؛ کوتاهی؛ اسم آلت سازد: غلتک؛ نسبت و تشبیه: پشتک ...' ('ک: joined as a suffix to a noun or to an adjective standing for a noun, with the following senses: diminution, smallness; affection, pity; delicacy; contempt; reduction ...'). Moʿin's first sense is Nourai's gloss word-for-word; what cannot be checked is whether p.2775 also carries the Pahlavi etymon Nourai implies.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Moʿin (2-vol. Adena condensation) s.v. ک and s.v. کنیزک (MON_part2.txt lines 16694, 27533)\", \"stance\": \"supports\", \"note\": \"suffix entry as quoted above; and 'کنیزک: (ا.مصف.) زن خرد. دخترک. پرستار زن خرد' — Moʿin classes کنیزک as an اسم مصغّر (diminutive noun), corroborating the chart's example.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien no. 870, p. 89 (HUB.txt line 3140) and §137a p. 244 (line 8745)\", \"stance\": \"partial\", \"note\": \"'Np. kanīzak ist durch das Deminutivsuffix ak von kanīz abgeleitet. Phl. kanīčak wäre = np. kanīza.' — the diminutive -ak is confirmed, but Hübschmann makes NP kanīzak a New Persian formation, not the direct phonetic descendant of Phl. kanīčak, and calls the whole diminutive -ak 'wohl jüngeren Ursprungs' than the Pahlavi -ak that gives np. -a.\"},\n            {\"src\": \"GPL\", \"where\": \"Platts, Grammar of the Persian Language pp. 135-136 (GPL.txt lines 1792-1795)\", \"stance\": \"supports\", \"note\": \"'Diminutives. These suffixes are added to nouns to form diminutives ... but for such formations the unreduced Phl. suffix -ak ... is more commonly employed; e.g. دخترک \\\"little daughter\\\"'.\"},\n            {\"src\": \"SBK\", \"where\": \"Bahar, Sabk-shenāsi I (SBK.txt lines 17673-17674)\", \"stance\": \"supports\", \"note\": \"'این ادات تصغیر گاه برای تصغیر سنی و گاه برای تصغیر مقامی و گاه من‌باب رحمت و رقت و عطوفت آید و گاهی هم در مورد تحقیر به کار آورند' — Bahar describes the same range of values (age-diminutive, status-diminutive, affection, contempt) that Moʿin lists for ـک.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p. 5 s.v. -ag (PHD.txt line 172)\", \"stance\": \"partial\", \"note\": \"'-ag [-k' | M -g, N -a]' — MacKenzie's stated New Persian reflex is -a, not -ak, which is the reason this node is 'plausible' rather than 'confirmed'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"-akah\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit -aka- (masc. nom. sg. -akaḥ) is the thematic enlargement of the inherited *-ko- suffix (Indo-Iranian *-aka-), and it does form diminutives and hypocoristics beside its adjectival/agentive uses: putrakaḥ 'little son' (putra-), aśvakaḥ 'little horse' (aśva-), śunakaḥ 'puppy' (śvan-), bālikā 'little girl' (bālā). It is the exact formal correspondent of the Iranian -aka- of nodes #1-#2 — the two are sister continuations of one PIE suffix, not one derived from the other, which is how Nourai draws it (both hang directly off the root box). Nourai's gloss 'small' is the diminutive function, correctly identified.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"IEC:9\", \"status\": \"supports\", \"note\": \"IEC.txt line 344 (page 9): '-akos, -ākos (diminutive suffix)  Skt. -akah, -aka; Per. -ak; ...' — Mann's page 9 gives 'Skt. -akah' with precisely the diminutive label Nourai reproduces.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"IEC\", \"where\": \"s.v. -ikos, -ikā (1) 'diminutive extn.' (IEC.txt line 6201)\", \"stance\": \"supports\", \"note\": \"'Skt. avikaḥ, -ā \\\"ram; ewe\\\"; guḍikā (\\\"pellet\\\": guḍaḥ); bālikā (\\\"little girl\\\": bālā) ... cf. Skt. śunakaḥ, dim.' — Mann's own Sanskrit examples of the diminutive k-suffix.\"},\n            {\"src\": \"GPL\", \"where\": \"Platts, Grammar of the Persian Language p. 136 (GPL.txt line 1795)\", \"stance\": \"supports\", \"note\": \"Platts brings the Sanskrit member into the same paradigm when explaining the Persian diminutive: 'کودک \\\"boy, lad, child\\\" (Phl. kutak; Z. kutaka \\\"little\\\"; cf. S. kṣudraka)'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/-kos (archived)\", \"stance\": \"partial\", \"note\": \"Confirms Proto-Indo-Iranian *-kas as the descendant of PIE *-kos, but describes the PIE function as adjectival; the diminutive use of Sanskrit -aka- is therefore an Indo-Iranian innovation on an inherited suffix.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-43.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-04T19:27:24.973Z] TOOL RESULT

```
JSON OK
```


## [2026-09-04T19:27:30.517Z] TOOL CALL #74: Bash

```json
{
 "command": "sed -i 's/Nourai’s نode/Nourai'\"'\"'s node/; s/Nourai'\"'\"'s نode/Nourai'\"'\"'s node/' data/verification/page-43.json && grep -c \"نode\" data/verification/page-43.json; python3 -m json.tool data/verification/page-43.json >/dev/null && echo OK; python3 tools/verify_check.py 43"
}
```


### [2026-09-04T19:27:32.858Z] TOOL RESULT

```
1
OK
nodes verified: 11/11
node verdicts: {'confirmed': 6, 'plausible': 5}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 11, 'partial': 5, 'not_checked': 2}
books consulted: {'supports': 30, 'partial': 10, 'contradicts': 2, 'silent': 1} | by book: {'KLN': 5, 'WLD': 4, 'HUB': 3, 'PHD': 3, 'SKT': 3, 'GPL': 3, 'CHEUNG': 2, 'BRT': 2, 'HRN': 2, 'NYB': 2, 'POK': 2, 'Etymonline': 2, 'Wiktionary': 2, 'AHD': 1, 'SYN': 1, 'ARY': 1, 'KNT': 1, 'TLM': 1, 'MON': 1, 'SBK': 1, 'IEC': 1}
```


## [2026-09-04T19:27:40.691Z] TOOL CALL #75: Bash

```json
{
 "command": "python3 - <<'EOF'\np='data/verification/page-43.json'\ns=open(p,encoding='utf-8').read()\ns=s.replace('نode','node')\nopen(p,'w',encoding='utf-8').write(s)\nEOF\ngrep -c \"نode\" data/verification/page-43.json; python3 -m json.tool data/verification/page-43.json >/dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 43"
}
```


### [2026-09-04T19:27:42.487Z] TOOL RESULT

```
0
JSON OK
nodes verified: 11/11
node verdicts: {'confirmed': 6, 'plausible': 5}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 11, 'partial': 5, 'not_checked': 2}
books consulted: {'supports': 30, 'partial': 10, 'contradicts': 2, 'silent': 1} | by book: {'KLN': 5, 'WLD': 4, 'HUB': 3, 'PHD': 3, 'SKT': 3, 'GPL': 3, 'CHEUNG': 2, 'BRT': 2, 'HRN': 2, 'NYB': 2, 'POK': 2, 'Etymonline': 2, 'Wiktionary': 2, 'AHD': 1, 'SYN': 1, 'ARY': 1, 'KNT': 1, 'TLM': 1, 'MON': 1, 'SBK': 1, 'IEC': 1}
```


## [2026-09-04T19:28:01.982Z] AGENT

Wrote `/home/sfmqrb/git/rishe/data/verification/page-43.json`; `verify_check.py 43` is clean (11/11 nodes, no PROBLEM lines).

**Page 43 (book p.13) — verdict counts**
- Roots: 1 confirmed (`Ak, Aq, Aken`), 1 plausible (`Akos, Âkos`)
- Nodes: 6 confirmed, 5 plausible; 0 disputed, 0 transcription_suspect
- Nourai's own refs: 11 supports, 5 partial, 2 not_checked (MMF:325 login-only; MON:2775 — the 6-vol Moʿin has no scan anywhere)

**Key findings**
- Root chain is Pokorny's own: IEW 541 heads *ḱē(i)- with "probably further formations from *ak̑- (see 18 ff.)", and IEW 18 lists *ḱei-/*ḱoi- among *ak̑-'s offshoots — so Nourai's root→#1 arrow is sourced, not invented. AHD *kō- reproduces nodes #5–#8 verbatim.
- BQT:1077 and BQT:1488 both verified (the latter fetched via `tools/ref_page.py`, cached PNG+OCR); Aryanpur p.339 independently cites "برهان قاطع ۱۰۷۶–۷" for the same headword, which pins the volume-2 page offset.
- Three errors are the **author's own**, not extraction errors (checked against the rendered page image, so `transcription_suspect` does not apply):
  - #2 [Avestan] "čâna / abi-čâna, abhi-čâna" are Sanskrit śāṇa- / abhi-śāṇa-, taken from Horn no.98 and Pokorny 541 (Nourai writes Skt ś as č elsewhere too); "asânam" is Av. asan- 'stone', which belongs to the root box, not to node #1. → node plausible.
  - #4 [Old Persian] "asam" is not an OP word for stone (Kent's asam = acc. of asa- 'horse'); it misreads Mann IEC:11 "OPer. asa, asan-", and Kent glosses asan- 'stone', not 'whetstone'. → node plausible.
  - #3 "fsân" is a misprint for fasân/fesân (the adjacent script فسان is right); node otherwise fully confirmed (Horn 98/752, Hübschmann §137, Nyberg, Cheung *sauH¹, BQT 1488, Wiktionary).
- Entry 2 root is plausible: PIE *-ko- is reconstructed as an *adjectival* suffix; the diminutive value is an Indo-Iranian/Balto-Slavic development. Hübschmann §137a and no.870 further show NP diminutive -ak is not the straight phonetic continuation of MP -ag (which gives NP -a), so both Iranian nodes are plausible rather than confirmed.
- 9 web pages archived via `tools/fetch_source.py`; every cited local lookup is quoted with file/line in `ref_check`/`consulted`.
