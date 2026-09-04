# Verification process log — verify-page-39


## [2026-09-04T18:48:50.321Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 39 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-39.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-39.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-39.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 39` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T18:48:51.543Z] AGENT

I'll start by reading the instructions.


## [2026-09-04T18:48:53.429Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T18:48:53.445Z] TOOL RESULT

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


## [2026-09-04T18:48:54.271Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-39.txt"
}
```


### [2026-09-04T18:48:54.287Z] TOOL RESULT

```
1	=== PDF page 39 (book page 9) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Aidh, Es 1 : to burn  (refs PRT; KLN; AHD)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:11 | aesmo : heat ; hĕzum : fire wood
5	  #2 (parent #1) [Persian] refs=BQT:2407; HRN:249 | hîzom «هیزم» : firewood ; hîmeh «هیمه» : firewood
6	#3 (parent #0) [Avestan] refs=POK:11; HRN:108; SYN:604 | ištya : dried clay, brick
7	  #4 (parent #3) [Pahlavi] refs=SNS:36 | xišt : clay brick
8	    #5 (parent #4) [Persian] refs=BQT:750; SYN:604 | xešt 1 «خشت ۱» : clay brick
9	#6 (parent #0) [Old Persian] refs=KNT:175 | išti : sun dried brick
10	#7 (parent #0) [Greek] refs=AHD | aithěr : (hot) air
11	  #8 (parent #7) [Arabic] refs=TAD:1 | asîr : ether filling beyond the atmosphere
12	    #9 (parent #8) [Persian] refs=MON:143 | asîr «اثیر» : ether
13	  #10 (parent #7) [Latin] refs=AHD | aethěr, aither : ether beyond earth atmosphere
14	    #11 (parent #10) [French] refs=MON:134 | ether
15	      #12 (parent #11) [Persian] refs=MON:134 | eter «اثر» : ether
16	#13 (parent #0) [Germanic] refs=AHD | ail : fire
17	  #14 (parent #13) [English] refs=None | anneal
18	#15 (parent #0) [Latin] refs=None | asetus : burning heat
19	  #16 (parent #15) [English] refs=None | estuary
20	--- entry 1 ---
21	ROOT Aien -> redirect to Ayer
22	--- entry 2 ---
23	ROOT Aier -> redirect to Ayer
24	--- entry 3 ---
25	ROOT [Indo-European] Aig- : goat, of a goat  (refs POK:6)
26	#1 (parent #0) [Avestan] refs=POK:6; KLN:30 | iza : goat ; izaenem : pertaining to (goat) skin
27	  #2 (parent #1) [Pahlavi] refs=POK:6 | azak : goat
28	    #3 (parent #2) [Persian] refs=POK:6 | azg «ازگ ۲» : goat | NOTE: This word is apparently obsolete
29	#4 (parent #0) [Greek] refs=POK:6; KLN:30 | aigis : goat skin
30	  #5 (parent #4) [English] refs=KLN:30 | aego- : of a goat
31	
```


## [2026-09-04T18:48:58.156Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-39.json | head -200",
 "description": "Read page 39 source JSON"
}
```


### [2026-09-04T18:48:58.194Z] TOOL RESULT

```
{
  "pdf_page": 39,
  "book_page": 9,
  "entries": [
    {
      "root": {
        "name": "Aidh, Es 1",
        "lang": "Indo-European",
        "refs": "PRT; KLN; AHD",
        "gloss": "to burn"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:11",
          "words": [
            {"translit": "aesmo", "gloss": "heat", "script": null},
            {"translit": "hĕzum", "gloss": "fire wood", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2407; HRN:249",
          "words": [
            {"translit": "hîzom", "gloss": "firewood", "script": "هیزم"},
            {"translit": "hîmeh", "gloss": "firewood", "script": "هیمه"}
          ],
          "note": null,
          "quote": {"text": "گر گلست اندیشهٔ تو گلشنی - ور بود خاری تو هیمهٔ گلخنی", "poet": "Molavî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:11; HRN:108; SYN:604",
          "words": [
            {"translit": "ištya", "gloss": "dried clay, brick", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": "SNS:36",
          "words": [
            {"translit": "xišt", "gloss": "clay brick", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:750; SYN:604",
          "words": [
            {"translit": "xešt 1", "gloss": "clay brick", "script": "خشت ۱"}
          ],
          "note": null,
          "quote": {"text": "سر تسلیم من و خشت در میکده ها - مدعی گر نکند فهم سخن گو سر و خشت", "poet": "Hâfez"}
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:175",
          "words": [
            {"translit": "išti", "gloss": "sun dried brick", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "aithěr", "gloss": "(hot) air", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Arabic",
          "refs": "TAD:1",
          "words": [
            {"translit": "asîr", "gloss": "ether filling beyond the atmosphere", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:143",
          "words": [
            {"translit": "asîr", "gloss": "ether", "script": "اثیر"}
          ],
          "note": null,
          "quote": {"text": "همچو آن مستی که پرّد بر اثیر - مه کنارش گیرد و گوید که گیر", "poet": "Molavî"}
        },
        {
          "id": 10,
          "parent": 7,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "aethěr, aither", "gloss": "ether beyond earth atmosphere", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "French",
          "refs": "MON:134",
          "words": [
            {"translit": "ether", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "MON:134",
          "words": [
            {"translit": "eter", "gloss": "ether", "script": "اثر"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "ail", "gloss": "fire", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "anneal", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "asetus", "gloss": "burning heat", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "estuary", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Aien", "redirect": "Ayer"},
      "nodes": []
    },
    {
      "root": {"name": "Aier", "redirect": "Ayer"},
      "nodes": []
    },
```


## [2026-09-04T18:48:59.635Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T18:48:59.689Z] TOOL RESULT

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


## [2026-09-04T18:49:03.050Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-39.json'))\nprint(json.dumps(d['entries'][3],ensure_ascii=False,indent=1))\n\"",
 "description": "Print entry 3 of page 39 JSON"
}
```


### [2026-09-04T18:49:04.586Z] TOOL RESULT

```
{
 "root": {
  "name": "Aig-",
  "lang": "Indo-European",
  "refs": "POK:6",
  "gloss": "goat, of a goat"
 },
 "nodes": [
  {
   "id": 1,
   "parent": 0,
   "lang": "Avestan",
   "refs": "POK:6; KLN:30",
   "words": [
    {
     "translit": "iza",
     "gloss": "goat",
     "script": null
    },
    {
     "translit": "izaenem",
     "gloss": "pertaining to (goat) skin",
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
   "refs": "POK:6",
   "words": [
    {
     "translit": "azak",
     "gloss": "goat",
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
   "refs": "POK:6",
   "words": [
    {
     "translit": "azg",
     "gloss": "goat",
     "script": "ازگ ۲"
    }
   ],
   "note": "This word is apparently obsolete",
   "quote": null
  },
  {
   "id": 4,
   "parent": 0,
   "lang": "Greek",
   "refs": "POK:6; KLN:30",
   "words": [
    {
     "translit": "aigis",
     "gloss": "goat skin",
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
   "refs": "KLN:30",
   "words": [
    {
     "translit": "aego-",
     "gloss": "of a goat",
     "script": null
    }
   ],
   "note": null,
   "quote": null
  }
 ]
}
```


## [2026-09-04T18:49:06.533Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['PRT','KLN','AHD','POK','BQT','HRN','SYN','SNS','KNT','TAD','MON','WLD','IEC','BRT','PHD','NYB','HUB','SKT','LEW','LAT','FSD','WEB','CHEUNG','ARY','FVQ','AFM','PLA']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False))\n\"",
 "description": "Print refs_online entries"
}
```


### [2026-09-04T18:49:08.287Z] TOOL RESULT

```
<persisted-output>
Output too large (42.1KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bkihx5y40.txt

Preview (first 2KB):
PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q=<word>. Entries are alphabetical with numbered sub-senses.", "notes": "RE-SEARCH 2026-09: 8 lending copies on archive.org, none open; HathiTrust search-only; Google no view. Borrow the 1958 copy to match Nourai's pagination."}
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end
...
</persisted-output>
```


## [2026-09-04T18:49:12.930Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','AHD','BQT','HRN','SYN','SNS','KNT','TAD','MON']:\n    v=d.get(k)\n    print('===',k)\n    for f in ['title','kind','local_file','page_offset','lookup_hint','url']:\n        print(' ',f,':',str(v.get(f))[:600])\n\"",
 "description": "Print details of key refs"
}
```


### [2026-09-04T18:49:14.788Z] TOOL RESULT

```
=== POK
  title : J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  kind : archive_djvu
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
  page_offset : POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
  url : https://archive.org/details/indogermanisches01pokouoft
=== AHD
  title : W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)
  kind : archive_djvu+website+archive_restricted
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
  page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
  lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves 
  url : https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only
=== BQT
  title : Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)
  kind : archive_djvu+local_scan_ocr
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/
  page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (
  lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=deh
  url : https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1
=== HRN
  title : P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  kind : archive_djvu
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
  page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
  url : https://archive.org/details/grundrissderneu00horngoog
=== SYN
  title : C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  kind : archive_djvu
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
  page_offset : leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
  url : https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca
=== SNS
  title : Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986
  kind : archive_djvu
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt']
  page_offset : 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
  lookup_hint : grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
  url : https://archive.org/details/VajnameShayest
=== KNT
  title : R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  kind : archive_djvu
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt
  page_offset : leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
  url : https://archive.org/details/oldpers
=== TAD
  title : Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR
  kind : archive_djvu
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt']
  page_offset : 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image
  lookup_hint : Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
  url : https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640
=== MON
  title : Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)
  kind : website+archive_djvu
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
  page_offset : None
  lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded a
  url : https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)
```


## [2026-09-04T18:50:03.022Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full lemma aidh\"; grep -n \"lemma: ai\" POK_full.txt | head -30\necho \"=== POK_full lemma aig\"; grep -n \"lemma: aig\" POK_full.txt | head",
 "description": "Grep Pokorny full for aidh/aig lemmas"
}
```


### [2026-09-04T18:50:03.091Z] TOOL RESULT

```
=== POK_full lemma aidh
2584:Root / lemma: ai-6'^-, Ad^- nasalized /-n-6^-{*av/-6^-) 
2668:Root / lemma: aid- {*avid^ 
2673:Root/ lemma: aig-1, nasalized ing- {* avig-f) 
2705:Root / lemma: aig-2 
2735:from Root/ lemma: aig-2\ "oak (alb. ahu'oak')'. 
2778:Hence Root/ lemma: aig-\ (goat) is identical with Root/ lemma: aig-3\ (to move swiftly, 
2793:Root / lemma: aig- {*avig^ 
2799:From the older root Root / lemma: aig- {* h2evig-)\ "goaf, derived Root/ lemma: ag^h-no-s 
2814:Root / lemma: aig"!!- 
2834:Root / lemma: aik- 
2846:Root/ lemma: ai-2{*avi-2) 
2866:Root / lemma: ai-3, {*hei-, heiua) 
2898:Root / lemma: ai-5 : oi- 
2913:Root / lemma: ai-ra 
2919:Root/ lemma: ai-ra: 'a k. of grass' is a reduced root *a/-trairom which derived also Root/ 
2921:lemma: ai-tro-\ bitter, sharp'. 
2935:Root / lemma: aisk- {*avisk^ 
2963:Root / lemma: ais-1 
2969:The Root / lemma: ais-1 : "to wish for, search for' is a truncated root of ai-ska. The formant 
2971:-ska is a common Germanic suffix added to Root / lemma: ai-2\ "to drive, to overwhelm, 
3013:Root / lemma: ais-2 
3021:The Root / lemma: ais-2\ 'to be in awe, to worship' is a truncated root of ai-ska. The 
3022:formant -ska is a common Germanic suffix added to Root / lemma: ai-3\ "to give' 
3039:Root / lemma: ai-ti-, ai-to- : oi-to- 
3047:Root/ lemma: ai-ti-, ai-to-: oi-to-\ "part, share, allotment, quantity, quota, portion, stake, 
3051:lemma: ai-2\ "to drive, to overwhelm, harm' with the formant -tra. 
3078:Root / lemma: ai-tro- 
3084:Root / lemma: ai-tro- : "bitter, sharp' is a truncated root *ai-tra into the suffixed Root / 
3086:lemma: ai-2\ "to drive, to overwhelm, harm' with the formant -tra. 
3100:Root / lemma: aiu-, aju- 
=== POK_full lemma aig
2673:Root/ lemma: aig-1, nasalized ing- {* avig-f) 
2705:Root / lemma: aig-2 
2735:from Root/ lemma: aig-2\ "oak (alb. ahu'oak')'. 
2778:Hence Root/ lemma: aig-\ (goat) is identical with Root/ lemma: aig-3\ (to move swiftly, 
2793:Root / lemma: aig- {*avig^ 
2799:From the older root Root / lemma: aig- {* h2evig-)\ "goaf, derived Root/ lemma: ag^h-no-s 
2814:Root / lemma: aig"!!- 
8853:tick'. From the older root Root/ lemma: deigh-: "to prick; tick' derived Root/ lemma: aig-\ 
23222:tick'. From the older root Root/ lemma: deigh-: 'to prick; tick' derived Root/ lemma: aig-\ 
43110:From the older root Root/ lemma: aig- {* h2evig-)\ goat', derived Root/ lemma: ag^h-no-s
```


## [2026-09-04T18:50:04.524Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD aidh\"; grep -n -i \"^aidh\" AHD_watkins1985.txt | head\necho \"=== AHD aig\"; grep -n -i \"^aig\" AHD_watkins1985.txt | head\necho \"=== AHD anneal\"; grep -n -i \"anneal\" AHD_watkins1985.txt | head\necho \"=== AHD aestus\"; grep -n -i \"aestus\\|estuary\" AHD_watkins1985.txt | head",
 "description": "Grep AHD Watkins"
}
```


### [2026-09-04T18:50:04.620Z] TOOL RESULT

```
=== AHD aidh
270:aidh-. To burn. 1. Suffixed form *aidh-sto- in: a. Ger- manic *aistaz in Old English dsé, kiln: oast; b. Latin aestas (stem aestat- for earlier *aestotat-), heat, summer: AESTIVAL. 2. Suffixed form *aidh-lo- perhaps in Ger- manic *ail- in Old English dl, fire: ANNEAL. 3. Suffixed form *aidh-i- in Latin aedés, aedis, building, house (<
=== AHD aig
272:aig-. Goat. Greek aigis, goatskin (shield of Athena): AEGIS. [Pok. 3. aig- 13.] .
=== AHD anneal
270:aidh-. To burn. 1. Suffixed form *aidh-sto- in: a. Ger- manic *aistaz in Old English dsé, kiln: oast; b. Latin aestas (stem aestat- for earlier *aestotat-), heat, summer: AESTIVAL. 2. Suffixed form *aidh-lo- perhaps in Ger- manic *ail- in Old English dl, fire: ANNEAL. 3. Suffixed form *aidh-i- in Latin aedés, aedis, building, house (<
1246:ANILE an-! ANILINGUS 4no-, leigh- ANIMA ane ANIMADVERT ane- ANIMAL ane- ANIMATE ane ANIMATO ane- ANIMISM ane- ANIMOSITY ane- ANIMUS ane- ANION ei-1 ANISEIKONIA weik-3 ANKLE ank- ANKYLOSIS ank- ANLAGE an}, legh- ANNALS at- ANNEAL aidh- ANNEX ned- ANNIHILATE ne ANNIVERSARY at-, wer-3 ANNOTATE gno- ANNOUNCE neu-! ANNOY od-2 ANNUAL at ANNUITY at- ANNUL ne ANNULAR 4no- ANNULET 4no- ANNULUS 4no- ANODE sed-2 ANODYNE ed- ANOINT ong¥- ANOMALOUS sem-! ANOMIE nem- ANON ol-no- ANONYMOUS né-men- ANOPHELES obhel- ANORECTIC reg-1 ANOREXIA reg-1 ANORTHITE wrddh- ANOSMIA od-! ANSATE ans- ANSERINE ghans- ANSWER swer-1 ANT mai-1
=== AHD aestus
271:“hearth”): AEDILE; EDIFICE, (EDIFY), MAZAEDIUM. 4. Suffixed form *aidh-stu- in Latin aestus, heat, swell, surge, tide: ESTUARY. 5. Suffixed form *aidh-er- in Greek aithér, air: AETHER, ETHER. [Pok. ai-dh- 11.]
839:parative) form *pro-tero- in Greek proteros, before, former: HYSTERON PROTERON, PROTEROZOIC. VI. Exten- ded forms *prai-, *prei-. 1. Latin prae, before: PRE-; PRETERIT. 2. Suffixed (comparative) form *prei-yos- in Latin prior, former, higher, superior: PRIOR2. 3. Suffixed form *prei-wo- in: a. Latin privus, single, alone (< “standing in front,” “isolated from others”): PRIVATE, PRIVILEGE, PRIVITY, PRIVY; DEPRIVE; b. Latin proprius, one’s own, particular (< pré priv6, in particular, from the ablative of privus, single): PROPER, PROPERTY; APPRO- PRIATE, PROPRIOCEPTION, PROPRIOCEPTOR. 4. Extended form *preis- in: a. suffixed (superlative) form *preis-mo in (i) Latin primus (< *prismus; ablative plural primis), first, foremost: PREMIER, PRIMAL, PRIMARY, PRIMATE, PRIME, PRIMITIVE, PRIMO, PRIMUS; IMPRIMIS, PRIMA FACIE, PRIMAVERA, PRIMEVAL, PRIMIPARA, PRIMOGENI- TOR, PRIMOGENITURE, PRIMORDIAL (ii) Latin compound princeps, “he who takes first place” (-ceps, “-taker”; see kap-), leader, chief, emperor: PRINCE, PRINCIPAL, PRIN- CIPLE; b. suffixed form *preis-tano- in Latin pristinus, former, earlier, original: PRISTINE. VII. Extended form *pres- in compound “*pres-g“u-, “going before” (*gvu-, to go; see gWa-), in Greek presbus, old, old man, elder: PRESBYTER, (PRIEST); PRESBYOPIA. VIII. Extended form *proti in Greek pros, against, toward, near, at: PROS-; PROSOPOPEIA. Other possibly related forms are grouped under per-2, per-3, per-4, per-5, and per-’. [Pok. 2. A. per 810.] per-?. To lead, pass over. A verbal root belonging to the group of per’. I. Full-grade form *per-. 1. Suffixed form *per-tu-s in Germanic “*ferthuz, place for crossing over, ford, in Old Norse fjérdhr, an inlet, estuary: FIRTH, FJORD. 2. Suffixed form *per-ond in Greek peroné, pin of a brooch, buckle (< “that which pierces through”): PERONEAL. II. O-grade form *por-. 1. Germanic *faran, to go, in: a. Old English faran (> Middle English faren), to go on a journey, get along: FARE; WAYFARER, WAY- FARING, (WELFARE); b. Old High German faran, to go, travel: GABERDINE. 2. Suffixed form *por-o-, passage, journey, in Greek poros, journey, passage: PORE”; EMPO- RIUM, POROMERIC. 3. Suffixed (causative) form *por- eyo-, to cause to go, lead, conduct, in Germanic *farjan, to ferry, in Old English ferian, to transport: FERRY. 4. Lengthened-grade form *pdér- in: a. Germanic suffixed form *f6r-ja- in Old English (ge)féra, “fellow-traveler,” companion (ge-, together, with; see kom): FERE; b. Ger- manic suffixed (causative) form *fér-jan in Old High German fuoren, to lead: FUHRER. 5. Possibly suffixed form *por-no-, feather, wing (< “that which carries a bird in flight”), in: a. Germanic *farnd, feather, leaf, in Old English fearn, fern (having feathery fronds): FERN; b. Sanskrit parnam, leaf, feather: PAN2. III. Zero-grade form pr-. 1. Suffixed form *pr-tu-, passage, in: a. Ger- manic *furdu- in Old English ford, shallow place where one may cross a river: FORD; b. Latin portus, harbor (< “passage”): PORT!; IMPORTUNE, OPPORTUNE. 2. Suffixed form *pr-té in Latin porta, gate (> Old French porte, door): PORCH, PORT’, PORTAL, PORTCULLIS, PORTE-CO- CHERE, PORTER®, PORTICO, PORTIERE, PORTULACA. 3. Suffixed (denominative) form *pr-to- in Latin portdre, to carry: PORTS, PORTABLE, PORTAGE, PORTAMENTO, PORTATIVE, PORTER}; COMPORT, DEPORT, EXPORT, IM- PORT, (IMPORTANT), PORTFOLIO, PURPORT, RAPPORT, REPORT, (SPORT), SUPPORT, TRANSPORT. [Pok. 2. B. per 816.]
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
```


## [2026-09-04T18:50:11.352Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2778,2815p' POK_full.txt",
 "description": "Print Pokorny aig- goat entry"
}
```


### [2026-09-04T18:50:11.408Z] TOOL RESULT

```
Hence Root/ lemma: aig-\ (goat) is identical with Root/ lemma: aig-3\ (to move swiftly, 
move violently, swing, vibrate). 

in addition Germanic name of the squirrel: Old High German eihhumo, eihhorn. Middle 
High German e/c/70/77 (Modern High German Eichhorn\N\Vc\ support of E/ic/7e "oak' and 
/yo/77'horn'. Old English acweorna,-wern. Middle Low German ekeren, ekhorn. Old Norse 
Tkorne (lko\6 ablaut or impairment from aik- in addition?). New Norwegian also eikorne. 
Old Swedish ekorne {was based on the concept " flexible, swinging itself from branch to 
branch '; in earliest with one to *uer-, ueuer- ' squirrel, weasel ' the belonging second limb: 
*aik-werna)\ Old Church Slavic igrb, igra^ play ', igrati, perfective v^zigrati^ OKipTciv, hop, 
jump, dance ' (from *bgra, Lithuanian with Berneker422). 

References: WP. Ill, Trautmann 103. 
Page(s): 13-14 

Root / lemma: aig- {*avig^ 
English meaning: goat 
Note: 



From the older root Root / lemma: aig- {* h2evig-)\ "goaf, derived Root/ lemma: ag^h-no-s 
{* heg^h-no-s): lamb' and Root/ lemma: ag-\ "goaf : Root/ lemma: kago-or kogo- -a-: 

"goaf. 

Material: Gr. ai^, - yoq 'nanny goaf, Armenian a/c 'nanny goaf; zero grade Avestan izaena- 

' from leather ' (actually, " from goatskin ' as gr. d\sz\oc„ of the same importance relations 

with *ago- " goat '). 

References: WP. I 8, Specht KZ. 66, 13. 

Page(s): 1 3 

Root / lemma: aig"!!-
```


## [2026-09-04T18:50:12.570Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: ai-dh\\|lemma: aidh\\|lemma: ai-6\" POK_full.txt | head\nsed -n '2584,2670p' POK_full.txt",
 "description": "Print Pokorny aidh entry"
}
```


### [2026-09-04T18:50:12.646Z] TOOL RESULT

```
2584:Root / lemma: ai-6'^-, Ad^- nasalized /-n-6^-{*av/-6^-) 
Root / lemma: ai-6'^-, Ad^- nasalized /-n-6^-{*av/-6^-) 

English meaning: to burn 

Note: 

Common lllyrian -gh->-dh- 

Material: Old Indie inddhe^ inflamed, is aroused ' (pass, idhyate, Perf. Tdhe, part. Perf. 

Pass iddha-h), indhana-m^ lighting '. 

Gr. aiGw " lights, burns ' (aiGopsvoc;), aiGwv, al9oi|j " igneous, sparkling ', i9aiv£a9ai 
0£Pfjaiv£o9ai Hes., hylleisch aiSwaaa aiGouoa " to light up, kindle '; changing by ablaut 
KaK-ien(; Hes. 'ravenously' (W. Schuize KZ. 29, 269 = Kl. Schr. 329). common gr.- lllyrian 
ks- > -ss- 

Maybe alb. (*5ujaaa) ndez^ to light up, kindle '. 



o-Grade:gr. al9o(; m. "fire' (ai96(; "burntly') = Old Indie edha-hxw. "Firewood' = Old 
English ad. Old High German Middle High German eitvc\. " glow, pyre ': zero grade 
probably Norwegian Swedish id^ leuciscus idus ' (a bright carp kind), of Modern High 
German dial, alter leuciscus cephalus' as the " shining '; besides u- stem *ai6!"u- in gall. 
VN Aedui, Old Irish aed^f\re\ also as MN; Latin aedes^ a dwelling of the gods, a 
sanctuary, a temple ', ursprijngl. " the domestic stove ', also aedis= maked. ab\c, saxapa 
Hes. 

From the verbal adjective in -/o- derived probably Latin aestas, - af/s 'yNarm season, 
summer' (from *aisto-tat-, Indo Germanic *afd!"-to-)\ aestus, - Js(from *aiA^-tu-) "heat, 
glow, surf', aestuare " cook, surge, roar '; 

Old Germanic MN Aistomodius {^ with quick-tempered courage '), Old English as/f. "dried 
stove', engl. c»a5/"drying room, drying loft'. 

/"-formants: gr. aiGnp "the upper air' (maked. a5r|), aiGpa "the cheerful sky' (maked. 
a5paia), ai9piO(; "brightly, cheerfully (from the weather)', for what changing by ablaut 
IGapoq 'cheerfully', Old Indie vTdhra-{=vi-idh-ra-) ds. 

A formants: gr. aiGaAr), aiQaKoc, "soot', maked. abakoc;, under acceptance of a 
development from "shining, appearing' " too apparently ' one puts a little bit constrainedly 
here Old English /de/'va\n, pointless, trifling'. Old High German fta/, Modern High German 
e/te/. 

In Indo Germanic *a/i'^-/o- is based Germanic a//- in Old English se/an'burn' to a/n. 
"flame', and in Old English seledrw.. Old Icelandic e/dr{Gen. elds) " fire, flame '. From 
different development-grading Old English aeledare borrowed cymr. aelwyd, bret. oaled^ 
from fire, stove ' (M. Forster Themse 4872). Middle Irish 5e/"lime' could have originated 
from *ai6!"-lo-. However, Germanic and Celtic words could also be formed directly by the 
root 4. 4. a/- with -/osuffix. 

5-formants: e5-stem gr. aiQoc, n. "Glow, fire' = Old Indie edhas-v\. "firewood'. 

Continuing formation: Old Icelandic eisai. {*a/i^-s-dn) "fire', Norwegian "Hearth', Middle 
Low German eset "chimney, fire stove ' (however. Old High German essa' chimney, 
hearth ' see below as-' burn '); Avestan aesma m. "Firewood' {*ai(i!"-s-mo-, cf without s 
Old Indie idhma-hm. ds.); in addition Baltic *a/sm/a\n Lithuanian /es/77e "firewood'; 
Lithuanian a/strat " passion '; Old Czech n/esfejeiiem. PI.) " stove ', later nfstej{m\h n- 
suggestion by wrong decomposition of the connections * \rbn-estejq, \rbn-estejach-b. 



Berneker275) from *a/i^-s-to; in addition zero grades *ki^-s-to-\n slov. /steje, stejeP\. " 
stove hole '; to Johansson IF. 19, 136 also Old Indie istaka^ of burnt bricks ', Avestan 
istya- n. " brick, (baked brick) '. 

Maybe alb. {*/ska) hith^ blight, burning nettle ', {*iskra) h/thra 'nett\e' common a/t>. -k > -th. 

In *//7d'^- goes back: alb. Geg idhune, Tosc idhete "bitter', Tosc /o''/7£V7/77 "bitterness, 
anger, irritation', fydhite, hithraP\. "nettle' (Jokl studies 29). 

Note: 

Alb. and gr. are the only IE languages to preserve the old laryngeal h- . 

References: WP. I 5, WH. 15, 20, 843, Trautmann 3, Schwyzer Gr. Gr. I 347. 

Probably to ai-4. 

Here also belongs aisk-, if originated from akH^-s-k- . 

Page(s): 11-12 

Root / lemma: aid- {*avid^ 
English Meaning: " swell ' 
See also: s. oid-.
```


## [2026-09-04T18:50:29.132Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: ag\" POK_full.txt | head -20",
 "description": "Find Pokorny ag- lemmas"
}
```


### [2026-09-04T18:50:29.178Z] TOOL RESULT

```
1787:Root / lemma: agh-(lo-) 
1793:Root/ lemma: agh-(lo-)\ "disgusting' derived from an extended Root/ lemma: agos-\ " 
1815:Root / lemma: aghl(u)-{*heghel-) 
1831:Root / lemma: agh- {*hegh-) 
1871:Root / lemma: agos- {*hege-) 
1887:Root/ lemma: agro-{egro-?) {*hekrh3Uo) 
1909:Root / lemma: agu(e)sT, aksT 
1935:Root / lemma: agh- 
1951:Root / lemma: agro-s 
1955:Root / lemma: ag- 
2129:Root / lemma: ag'^h-no-s {* Jag^h-no-s) 
2135:It seems that from Root/ lemma: ag-\ 'to lead, *drive cattle' derived Root/ lemma: ag"!!- 
2799:From the older root Root / lemma: aig- {* h2evig-)\ "goaf, derived Root/ lemma: ag^h-no-s 
2800:{* heg^h-no-s): lamb' and Root/ lemma: ag-\ "goaf : Root/ lemma: kago-or kogo- -a-: 
8801:Root / lemma: agher-, aghen-, aghes- (or oghereic) {*daghen) 
8825:From Root/ lemma: d'^eg'^h-: "to burn, *day' derived Root/ lemma: agher-, aghen-, aghes- 
8845:Root / lemma: ag- 
8855:"goaf and Root/ lemma: ag-\ "goaf [common Baltic - lllyrian - alb. de-, da- > zero]. Hence 
8892:Root/ lemma: aier-, aien-\ "day, morning' derived from a reduced Root/ lemma: agher-, 
19998:from Root/ lemma: 6!^eg''h-\ "to burn, *day' derived Root/ lemma: agher-, aghen-, aghes-
```


## [2026-09-04T18:50:31.234Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8845,8875p' POK_full.txt",
 "description": "Print Pokorny ag- goat entry"
}
```


### [2026-09-04T18:50:31.283Z] TOOL RESULT

```
Root / lemma: ag- 

Meaning: goat 

Note: 

Root/ lemma: digh-\ "goaf derived from a zero grade of Root/ lemma: dei§h-\ "to prick; 

tick'. From the older root Root/ lemma: deigh-: "to prick; tick' derived Root/ lemma: aig-\ 

"goaf and Root/ lemma: ag-\ "goaf [common Baltic - lllyrian - alb. de-, da- > zero]. Hence 

the gr. cognate derived from proto lllyrian 



Material: Old Indie aya-/? "he-goaf, aja^ she-goat ', Middle Persian aza/r"goat', npers. azg 
ds.; 

alb. o'/7rgoat' (G. Meyer BB. 8, 186, Pedersen KZ. 36, 320, 335; probably from *adhi, as 
s/7" eye' from asii)\ 

Note: 

Maybe a zero grade in alb. {*aghi) dhV goat ' [the common alb. shift -gh- > -d-], older alb. 
Geg {*aghi) edha'goats, sheep'. 

Lithuanian ozys{* agios) "he-goaf, c»z/ra"goaf. Old Prussian M/c»see"goaf, wosux^he- 
goaf; 

Old Indie ajfna-m "fur, fleece';
```


## [2026-09-04T18:50:34.280Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8875,8895p' POK_full.txt",
 "description": "Print rest of Pokorny ag- goat entry with page"
}
```


### [2026-09-04T18:50:34.334Z] TOOL RESULT

```
Old Indie ajfna-m "fur, fleece'; 

Lithuanian ozinis^ belonging to he-goat ', ozfena^ billy goafs meat '; 

Church Slavic {j)azno {* azbnd) " skin, leather '. 

References: WP. I 38, Trautmann 22. compare also aig-. 
Page(s): 6-7 

Root / lemma: aier-, aien- 

Meaning: day, morning 

Grammatical information: n. 

Note: 

Root/ lemma: aier-, aien-\ "day, morning' derived from a reduced Root/ lemma: agher-, 

aghen-, aghes- (oder oghereic): day'.
```


## [2026-09-04T18:50:45.175Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT izaena\"; grep -n \"izaēna\\|izaena\\|izaēn\" BRT.txt | head -20\necho \"=== BRT iza standalone\"; grep -n \"^iza\\b\\|^iza-\\|^iza \" BRT.txt | head -10\necho \"=== BRT aesma\"; grep -n \"aēsma\\|aesma\" BRT.txt | head -20\necho \"=== BRT istya\"; grep -n \"ištya\\|istya\\|ištiia\" BRT.txt | head -20",
 "description": "Grep Bartholomae for izaena, aesma, istya"
}
```


### [2026-09-04T18:50:45.267Z] TOOL RESULT

```
=== BRT izaena
=== BRT iza standalone
=== BRT aesma
2726:i.  aesma-   m.    'Brennholz',   Flur,    und
13329:•  j.  däityö.aesma-  Adj.  'die  gehörigen Brennhölzer  habend,  daraus  bestehend': aEsmsm  (sd.)  'smam  "  N.  /oj.
13330:vKorapA.  —  Pü. :  'fehlt.  —  ')  AP.  auf  kollekt. AS.  belogen;  s.  aesma-  No.  i.
13351:vKonipA.  —  Pü, :  fehlt,  —  0  Auf  kollelcL  AS. , bezogen?     S,  aesma-  No.   1.  |
18931:mit  fra  'herzutragen,  -bringen  zu  — ' (Akk.):  aesmanqmat  .  .  vasyäi/ (sd.)  .. ratSu^ nmätism /rSnSsayata{'i2.1)  K.3. 5;  5.
19489:•  j.  maesma-  m.  'Harn',  als  rituelles j  Reinigungs-  und  als  Heilmittel  verwendet*';
19493:■  j.  maesman-  n.  'Harn',  als  Rcimgungs- und  Heilmittel'':  Ävam  tanüm  pairi.- yaozdat^Ua  gius'mana  apäca  paiti  avd^a
22152:vaesma-
24858:•  j.  rao^as.caesman-  m.  EN.  eines  der sechs  Genossen  des  SaoSyant  bei  der Auferstehung,  Ralav  des  Karsvar  Art- ta/iT'^:  'mariß  a/aeirS  \'t.  1^3.  128;   iii.
26533:•  j.  staoyah-'*  Adj,  'der  umfangreichere, stärkere,  grössere':  aesmanqmcit . .  vazyäis (sd.)  stais'ca  'yJbls  A.3.^.
27125:—  yd  .  .  rapthwifom  .  .  JrSyasäite  Jra- snälaiibya  xastaäbya  frasnataltbya hüvanalibya  A.  4-  Si  V.  <?  40,  i<y.  19;  — zasta  hl  paoirlm  frasnatayM  V.  8.  40, 16.  T,  —  vasirä  frasna^aytn  massmana gSus  V.  7.  13;  14';  —  taita  . .  hak^nt /rasnahaym  maümana  giul  .  .  halant apS  ß-asnäiayM  V.  7.  74;  —  aSaia  .  . "krii  may^m  (sd.)  avaAanaym  dva  maja /rasnälaym  maesmana  gius  *Hm  apS  V, j6. 13;  —  Med.  in  reflex.  Sinn:  fra  tasta snayaauha  V,  18. 19;  —  tanUm  frasnaya- yanta  \X.io.  laz*;  —  malsma  .  .  yaiibyS (statt  Instr.)  . ,  nasuMala  frasnyänte  van-
28373:j.  maesma  samqn  P.  g:  lies  miutma.s'. •  '}.,  g.  äay-  V.  'wohnen'.    Praes.  1  say-i sy-''>,  xsay''>^,  4  saya-.    —    PPfP.  'Uta-, Inf.  •/(/*,  •iiliy  'xsdi^ne^.
29099:•  j.  ha<)a.aesma-  Adj.  'mit  Brennhob versehen,  Brennholz  darbringend':  akmä- k>m'a  masdayasnanaiii  .  .  'manaiii  kala.- baoioinqm  Vr.  12.  5.
29147:nam  aesmanam  vanJvanqm  .  ,  *tayä  vä  | .,  ä%re  .  .  frabaröil  Y.i&.-Ji;  —  baivari tao'hranam  . .  Aqm.iriita  aitayä  urvarays ya  vaoie  'p3ta  ". .  in  Mischung  mit  der Pflanze,  die  H.  heisst"  V.  14. 4;  —  urvarqm Uqm  alaya  usdatqm  Y.J.  3,  22..1;  62.9.
=== BRT istya
```


## [2026-09-04T18:50:52.748Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2720,2740p' BRT.txt\necho \"=== Ziegel\"; grep -n \"Ziegel\" BRT.txt | head -20\necho \"=== izae variants\"; grep -n -i \"iza[eēsSä]\" BRT.txt | head -20\necho \"=== Leder\"; grep -n \"'aus Leder'\\|aus Leder\" BRT.txt | head -10",
 "description": "Look at Bartholomae aesma and search Ziegel/izaena"
}
```


### [2026-09-04T18:50:52.841Z] TOOL RESULT

```
Sohns   des  ^.,    Sohns   des  .S  . ."  Yt /j.         ^  x,..  ,..__._-_„. ,.        ,.  j._
"5- Lig.  'einiiEMtifi'.
•  g.  aerav-    Adj.    (etwa)    'schimmenid': fiwf'j  ^it^  asnqm  uxsä   (sd.)  agurui  Y,
und  *iSla  könnten  alle  Formen  auch  dem Perfekt  lugewiesen  werden,  S  '62.  —  ')  Them.
—  Ü  Steht  •jf;cäry(sd.)  statt  des  gen.  Inf.,  so lässt  sich  der  Gen.  gäiMiiam  durch  Attraktion erklären;  s.  lu  anujctSf  No.  I.  —  ••)  Hds.  iJti.
—  -■)  Hds.  ii/a.  —  i>)  Hds.  hrn.  —  !)  S  3/S No.  2.    —   S)  Zu   S  37'.    —   *>  Vgl.   Pü.   lu
i.  aesma-   m.    'Brennholz',   Flur,    und
Uiflitized  by  VjOOQ  IC
a?
Sing,  in  kollekt.  Sinn');  'ma  frasaocayähi\     Lavaquellen  enthaltend".    VgL   Bthl.IF.j. V.  *.  7  5 ;  /4-  7 ;  —  a  -man  y'äsamiha  V.  i8.       ■  24-  -  •>  NS.,  S  ^5- »9;  5-z;  — "'«ff  ■■  ^<»"  Y.J.2;  — '«ffJ'Taj«  j.    aezah-    n.    'Verlangen':     "zö    (AS.) baolulmca  Y.^'i,  7.26,  Äi,  22.3;  —  ''ma  J'isatim    aisahe   "sie  (beide)   kamen
(sva.  'nach  dem)  Verlangen  des  verlangen- den" Yt  J5.82'>.
Zum  V.  äs-;  s.  unter  ana-,  —  aL  ihm-  n.  — )  VgL  iKoDstT.  Dbr.  AiS.  185. j-,  g.  'aeä-  V.  'suchen'.  Praes.  3  isa-, a  isa-,  *»Ja-'',  14  b  tfasa-,  aisasa-", 17  (Fut)  aifya-,  30  (Iter.)  aSsaya-;  Perf. iyals-^,  yals-i\  —  PPfP.  isla-,  PFP.  k><7-;
(AD.)  baom  Y.7.2; —  Aa  »i?  bara  'm (AP.)  bansmaca  U.io^;  —  'masca  bam- maca  N.  7/T.;  —  *kava  °ma  (IS.)  Aava bansmana  N.  108-,  — ■  °m>m  aSaya  b^nlsm Y.62.^;   —  yü  °md  (AP.)''  asaya   barat  * V.Ä79;    —    *kva    a/Sqm  (AP.)  ^'mim^    ' paiti.barat    N. /oj;    — ■    cvat    nä    nit?ma 'mähe  patti.barS  ratufri^  "wie  viel  Brenn-    _  .  .
holz  zum  mindesten  darbringend  ist  man  Inf-  <^t^^;  Absol.  'agi?m,  •iünbrn. r.f'  N.106;  —  iat  tä  °ma  (^V.)  yaoz-  i)  '(etwas)  suchen,  suchen  nach  -, dayqn  ar>h>n  V.  7. 28;  ■ — ■  pairi  urvarä-  aufsuchen':  yd  aüm  mainimnö  ahm byasca  varsoäbyasca  'tnaiil^ö  "abseits  von  isimnS  ahm  apa.rao'iayeiU  {sA.)  .  .  dru- Bäumen  und  Sträuchem,  die  Brennholz  jimca  vinasti  V.  7.78;  —  Med.  auch  in sind  (geben)"  V. /6'.  2;  —  Auskam  °m»m  reflex,  Sinn:  vSrrinahe  .  .  yS  vazaite  .  . Y.JI.8; — Auskanqm  ..  'manqm  ,.  nafi-  axsa/hi  {sä.)  xsa/hTm  tsfmnS  \'t  14.  20; tanqm  ..  xraozdvanam  ..  varidvanamY.    ao.  a)  mit  Dat.  comm.:  vlstäspahe  ..
7. 3IJ/5.24,  /.^.  2j3;  —  'manqm  ..husatqm  yö  .  .  asäi  ravö  yaisa*''  .  .  ravö  t'TvaAa A.j.  5';  —  'manqm  yaozdätanqm  Y.t8.  "V.,  der  dem  Asa  ..  Raum  suchte,  .. 19;  22;  —  'mtmi'f  .  .  hüBs  *rat>cas.pai-  'Raxaa  fand"  Yty.gg;  —  äat /rasüspnie ristqm  Y.  62. 10;  —  'mgm^  däityS.aüman  \ .  .  fravalayö  .  .  ap>m  ais^mna^  haväi "Brennholz,  das  aus  den  gehörigen  Brenn-  käcit  näfai  (sd.)  ". .  um  Wasser  zu  suchen hSlzem  besteht"  N.  ioj;   —   aiUm  'mrm  jede  für  .  ."  Yt/_J.66.  b)  ohne  Obj.:
yö  vaoce  *n)ma<,ka  nqma  Yx.14-  55-  balsaz3m  (sd,)  ..  upöisaym  ..yezi  is»mnö
KompA,,  E.  —  Zum  »i.  V,  indhati,  gr.  a:%a.  .  ttSit  vifldaiU  (sd.)   V.  y.36.  2)   'zU    Cf-
Aus  ir.  *ai:ama-,  S5J 1-  8.  —  np.  iiam.  —  langCD  sucheo,   haben  wollen,  begehren,
Pu  :  ^-r«4'.  -    '>  ^f"^"  S.Lg.  mehrmals  angehen':     ^ar^nö  .  .  yat  isat  Jra,?rase
mit   dem  Flur,  des  Attributs  verbunden  vor-  ,,  ,     „  ,~        "        ™
kommt;».  No.  3.  -  ')  llnthem.(?).  -  3)  S.  Y\.ig.$(>;iz;  —  apatat  /raarase  :^ar7n5
=== Ziegel
8060:'  j.  iätya-  n.  'Ziegel,  Backstein':  ava  hi gätüm  barayjti  .  .  "yehe  vä  zarltvahe  vä .  .  pqsnüm  V.  S.  8.
=== izae variants
8456:•  j.  ubdaena-  Adj.  (fem.  °nT-)  'aus  Web- stoff, Zeug':  vastrim  .  .  'tarn  va  Tzaimm Tv7  V.S.a^;  — yesi  avAat  izaätt/  (sd.)  .  . yesi  a»hat  -tfU  V.  7. 14  f.
16538:Vgl  *baHaiyäi    und  AiSaai..    —    Pü.  (dRn.):        SuperL  aus  ÄiSaya-.  —    Pü.;    itlaiMtärOim. itsazeniinU,  pa  bizaSm.  (m  Yt.  7)  erL;    mart  kaS  guß  islll  (*«)  tär  u
17046:*)  Sobm  dtiZasrämvy;  vgL  SBayrAW. /<^0. 2.  62,  76.
30428:•  g.j.'hu-mäyä-,  j.'hu-mayä-(mask.*^a-) Adj.  'segensreich;  gesegnet':  °mälm  i)Wä iilmyazat>m  alatihääm  dadamaidt'aizAeYi segensreichen  setzen  wir  dich  ein,  als  den erfolgreichen  . ."  Y. 41. z;—  yai  hJs  (näml. däman)  'mayaca  liyäca"  äna^amaideVi. 12, 4";  —  'maya  aita  däman  *dähimaide 'maya  clsmaide  'maya  matnyämaide  *yam da^at  ahurS  mazdä  Vr.  72.4'';  —  'maya upar»ha  (sd.)  cllmaide  ahunahe  vairye?u Vr.  12. 2;   —    'maya   nö  buyati
=== Leder
```


## [2026-09-04T18:51:03.360Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"zaEna\\|zaena\\|zaSna\\|Tzae\\|izae\\|iza-\" BRT.txt | head -20\necho \"---- search 'Fell' / 'Ziege'\"\ngrep -n \"'Ziege'\" BRT.txt | head -20",
 "description": "Search Bartholomae for izaena headword and Ziege"
}
```


### [2026-09-04T18:51:03.431Z] TOOL RESULT

```
2749:—  O  Wegen  des  Diphthongen  in  aiza-,  tha-  mich  das   starke  Reich"  Y.^/.4.         3)  mit
4338:•  j.  an-ava'Dhabdamna-  Adj.  'nicht  ein- schlafend': -d^mnS'  zaenauha  Y.57.16".
8681:Vgl.  usvariza-.  —  ')  Vgl,  daiu  HoRH  BB.  //. 259-
11777:•  j.  taiya-,  taiza- 1)  Adj, 'schaif.  j)  m. 'Schärfe'.
12546:j.  daiza-  m.   "Häufen,   Schichten'  von Erde,  Steinen. KompE.  —  Zum  V.  dan-,  —  np,  dcz  "Burg', gr.  «rxoe  'Mauer',   osk.  /eihius  (AP.)   'WafP; ü.  deka-  m.  'Körper'.
17891:KompE.  ~  Zum  V./roi-.  —  Vgl./raiJ-.  — Pü.;  hamfursel,  Sä.:fj-cc/iaii.  —  >)  VgL  zAusdr. Bthl.  1F.  7.  326  mit  Bgm.  IF.  6,  loi;  s. femer  anumatay-,  usdaiza-,  pairi.fräsa-.  — >)  Vgl.  iSl.  IF.  7.  226.
22179:•  j.  vaez-  V.,  nur  mit  nT  'an-,  einstecken', Praes.  3  viza-.
27470:zaenay-
27499:•  j.  zaena-  m.  'Waffe':  vasrfm  . .  ama- vastpmfm  -nam  (GP.)  Yt.  70.  96  ";  96;  — hqm  *'tta  (AP.)"  stmbayalwtm  (sd.)  Yt  i. 27;  —  *tta  (IS.)  haHtma  hutniia  Yt. 10. 141.
27501:•  j.  zaenaDh'an-  Adj,  'wachend,  wach- sam': sraes?m..yd  anavanhabdsmra  'aha (NS.)  nipaili  tnazää  däman  Y.57.  16;  16, F.  20;  —  'K>ha  (NS.)  niJspBj^aJna  (sd.) ya&a  västryS  fsuyqs  V.  13. 46.
27503:•  j.  zaenay-  Adj.  "reg,  eifrig':  yas^a  hi .  .  väam    paifi    'nil   anhat    (näroL  sp£)
27509:•  j.  zaenav-  f.  'Wehrgehänge'*':  yailqm zayanqm  raisWi  .  .  puxaa  'nätti  mat aiana  mat  "irisas  ayj.arfräil  ". .  das  Wehr- gehänge mit  dem  Köcher  sammt  30  eisen- spilzigen  Pfeilen"  V.  14. 9.
27513:•  j.  zaenah'vant- Adj.  'wachsam,  regsam': mCir?m  . .  •narthuntim  Yt  /o.  61 ;  — *'na>3uhant>m     . .    yaka     taxmS    urvpa
29002:von  I  1;  a)  im  jAw.;  zu  a  o):  Aa/  nä a%rava  a%auru>um  k°  *gathäbi!  *parayilt (sd.;  'abeaf)  N.4;  —  ärux!  .  .  ya  k* irista  upa  Jvoräim  upa.dvasaiti  ('arvolat') ..ya  h' irista  upa  Jvani>m  upa.raei;waiti ('inirat')  V.  /O.  i ;  —  avanayeni  ('dcducam') spmSim  mainyüm  h'  raoxsna  *garS  nmäna uspalayeni  ('expellam')  anr>m  mainyBm »rrfata  h-  duiaKha  Yt/p.44;  —  »riza- taina  h'  taSta  saranamim  aoi  taxle ('affundo')  Y.  jo.  17;  —  h'  u^asiara  handva avi  daosastarPtn  k»ndum  V.  i.  18  PUZ. (Verbum  fehlt);  —  neben  einem  blossen Abi.:  haomtm  ytm  nivizaiti  (Sp.  1329  o.) nivandat{sA.)  apoyeiti  ('abscedit!)  [dusmain- yaoi\  pfiana  A'  Yti4.$7.  za\i):  paiti.- p?r)ne  ('oppugno')  atinm  mainyüm  h° nmOna   h'*  . .  h'   daiiihu   V.  jo.  5*';  —
30515:•  j.  hu-zaena-  Adj,  'mit  schönen,  guten Waffen';  mihnm . .  'n^m  . .  vn-Hsravastittum
---- search 'Fell' / 'Ziege'
```


## [2026-09-04T18:51:10.969Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Leder\" BRT.txt | head -20\necho \"=== around istya\"\nsed -n '8050,8070p' BRT.txt",
 "description": "Grep Bartholomae Leder and context of istya"
}
```


### [2026-09-04T18:51:11.033Z] TOOL RESULT

```
8002:*  Adj.  (fem.  "«r-)  'aus  Leder, ledern':  vasfr^m  . .  ubdamsm  'mm  vä  V.  (V, 23;  —  yezi  a^hat  'nif  (liSL)'>  V.J.  14. AbteiL    aus   •£-   oder   *'sä-  'Leder'.  —  Et? Man    vergleicht    gr.  eJ(,    arm.  aic;    s.  lulelit Hbm,  AGr, /.  4'7.  Hatzioakis  IF.  //.  314. — Pu. :  /öi/Fii.  —  O  Mit  t\.S.~~  »)  Man  ver- langte   NSo.,    da   lä  vaitra  APn.  vorausgeht. Vgl.  V,  ;t.   74  f.,  zu  saraaaena-  No.  2. j-,  g.  äy',  Verbalf.;  s.  unter  öi-.
11248:•  j.  (Jaraman-  n.  'Fell,  Leder';  mrätim "ma  "^anjaymte  "sie  ziehen  an  dem  ge- gerbten Leder(strang) "  Yt  17,  12;  — 'manqmca  .  .  *mrätanqm  N.  ^8;  —  'm<i (NP.)"  vatnantö  br3e?nta  {sA.)  frjna  »r^-
=== around istya
istay-  3
baräni   haia    dafvaiifyö   uye    'tilca  (AP.) saokäca  YLj.  26;    —   kahmsi   ..    datam virayqm  'tlm  .  .  gaoyqm  "Um  .  .  asfayam 'tim  Ylä  15—19;   —    ahmäi  asht  (sd.) vahiSä  mahya  'iöis  . .  Mhm  Y.  4G.  18;  — vahistS  °tU  srävl  zara^uitraAs  spitämahyä "das  beste  Gut,  das  man  kemit,  ist  das des  ZSp."  Y.  ^.  1 ;  —  avat  ySsqs  hyat  vi 'lä  (LS.)  vahiSl3m  "nach  dem  verlangend, was  in  eurem  Besitz  das  beste  ist"  Y.  4g. 12;  —  vahiltqm  °tim  . .  yqm  alake  vahis- iaAeVr.'^j.i;  —  yd^rä  vaukSus  inanatihS 'lä  (LS.)  x/a^nm  "wo  das  Reich  im  Besitz des   guten   Sinns  ist"  \.  46.16;    —    kä iJt  vauhius  mazdä  xsdi,rahyä   "til  kä  löi aseis  iwa/lyä  maibyö  ahurä  "Ist  der  Be- sitz deines  guten  Reiches,  o  Mazda/i,  ist der  deiner  Belohnung  für  mich  bestimmt, o  Ah.r'  \.4S.8;    —   a/>e   mä  Ulm    apa- yantilisA.)  bfrix<>qm  häitlm  vatihlui mana~ uhö  Y.J2. 9;    —   tu  vS  mazdä  pagun'Tm ahurä  '•  a!äi  yecS  taibys^ä ''  ärmaiU  döii'ä tnsi  'tsil  xsdhnm  "dnim  sichere  mir  vor allem,  o  MAk.,  die  Herrschaft  über  euren Besitz  zu  und  den  des  Asa  und  den  deinen, o  Arm."  Y.  5/.  2;  benüut  V'yt.dO;  —  Iqm aslTm  dSjSmäsps . .  'tsis  :^ar»na  (sd.)  asä 7vr?nie  Y.j/.  t8.         3)   'Inbesitzb ringen, Inbesitzkommen  von  — ,  Teilhafugwerden': J.wJ  (sd.)  vavAjus  asä  'Um  matiaaAö  Y. 46'.  2.        "/Ä  als  Inf.  sbes.         [Y.44-io: lies  %wil.TäTs;  —  P. /2:  lies  isle,  s.  ags-.'\ KompEU;  Ableit.  (s.  iilavaiit-).  —  XiaaW.afs-; BB,  /J.  54,  T4.  9.  —  Vgl.  goL  aihii,  ahd.  e/ii 'Habe'.    —    Pü.   (meist)i    '//  (Transskr.,   fast immer    in    Aw,-Buchst)J),     etl.    (mehcinals)! j'üs/ai;  Sü.  (meist):  lojcimiA;  (zu  Y.  4S,  53, Vr.):  x'ühün,  {lu  Y,  46.   16);  Ji-äst,  (zu  V.5/. 2):  j'ähit.  —  ')  Mit  /  Yt.  ig.  31,  +Vr.  33.  1 (»o  K  7  ■)  und   im  GS.    —    >)   Stall  oKyis/ä {istöi})  yä  asäi.  taibyüä.     Falsch  BB.  14.  9.  — 1)    S.   auch    lU   iißm    Y,  40.  4   (unter    "^^. No.  6).
•  j.  iStavant-   Adj.   'mit   Besitz-,   Reich- tümern versehen':  yazili  tnBnhjin  ..'vantint
Vt7.5-
AbleiL  aas  'lilay-;  statt  it/ro"  gescbr. O.  —  PQ. niemand,  erl. :  kit  harätmit  (glossirl  lisäHoj gäipandän  dahei,  Npü.:  xixäna  dar.  —  ■)  J  368.
•  j.  iSHe  Inf.  'Herr  zu  sein  über  — Besitz  zu  kommen  von  — ':  jamyqn  i^ra . .  /ravalayö  . .  i°  *vari/ianAqm  paitistaiSe ätaranqm  frala.vax^Si  rayqmca  »farma- »kqmca  "her  (ins  Haus)'>  soUen  sie  kom-
iia-  I  a  378
men,  die  Fr.  . .,  damit  es''  in  Besitz  des Besseren  gelange,  den  Angreifem  wider- stehe, Reichtum  und  Herrlichkeit  weiter -ermehre"  Y.  60.4.
Zum  V.  ais-.  —  Vgl.  iilay.  —  Pii.  (für  /■ vadh')i    an    Mt^oatih  hac  artiivang  ape   rasat.
—  OS.  aiükat  Aa?a  vJsai  Y.  60.  3. j.  iili.mas5  V.  13.  30:  lies  aUi.iii\
'  j.  iätya-  n.  'Ziegel,  Backstein':  ava  hi gätüm  barayjti  .  .  "yehe  vä  zarltvahe  vä .  .  pqsnüm  V.  S.  8.
Vgl.  i^möiilva:  —  Vgl.  ai.  i^lakä-  f.,  np.  xiil.
—  Pii.;  Üi.
•  g-,  j.  isya-  Adj.  (fem.  "yä-)  i)  'erwünscht; begehrenswert':  kä  %wsi  asa  äkä  (sd.) andrang  'yl  Y.4S.%;  —  asahyä  >wj.i  (sd.) aslm  yqm  'yqm  "den Preis ..,  den  begehrens- werten, welchen  . ."  Y.54.r._  2)  von Personen  'lieb,  traut':  b?rfx<iqm  nwi  .  . daldöist  (sd.)  k}krp7m  damaysi  vauhuyäi yqm  Asi  'yqm''>  dälB  x/ayqs  mazdä  ahurB . .  äzdyäi  (sd.)  "den  .  ■  Leib  der  lieben (Jungfrau)  .  .,  welcher  der  Herrscher MAh.  es  gewähre  für  ihr  gutes  Ich  .  . zu  gelangen"  Y.5^.17;  —  hyat  *aS>ia>ihz dngvats  S»äna  °y}ng  avAayS  (sd.)  Y.js, 16.  a)  insbes,  von  'airyaman-  (sd.): il  airySmä  (sd.)  "yö  rafooräi  jatitü  Y.  ^4- 1;  V.  22.9,  19,  20,  a)  mit  'airyamati- (sd.,  auch  fdSt):  mryamamm  'slm  Vr,  2. 10;  usw.;  —  airyamattö  °ye/ie  Vr.  j.8;  usw.
S.  ä.airyiniä.iSyä.  —  PFl'.  lum  V.  ^a/!-.  — ai.  vgL  ffyä-  Adj.  —  Pü.  (lu  ^.48):  x''äl,un, (zu  Y.  Sl)-.  pa  iPäliiSn,  (zu  Y.  54  1.  St.  und zu    2  a  o):    xvähiinth,     (sonst) :    x^äslär.    —
—  ')  '. .  corpus  . .  quam  desiderandam  .  ,' statt  'corpus  . .  desiderandae  (GS.)  quam  .  .'  .
•  j.  (jVa-'*  m.:  sva.  isav-.
KompA.j  Ableit.  (b.  xsvrmijivat>,na-\,  —  gr. «{.  —   ')  Unrichtiges  KZ.  25.  381.
•  j.  iSva.vasman-  n.  'Pfeilflug':  hö  aci'v . .  °sma  apayeiti  .  .  yatcit  vazaite  hvashm "er  alleinholt  denPfeilflug  ein..;  auch  wenn er  guigeschossen  dahinfliegt"  Yt,  14.  20.
"va^man.  n.,  lum  V.  vat-{%  284);  ai.  -uähmau Adj.  —  Npü. :  Willis  u  miiräd  i  xud.
•  j.,  g.  izä-'>  f.  1)  'Stieben,  Eifer",  bes. 'frommer,  Glaub enseifer':  manS  voha  uru- nascä  asiiunqm  n>mascä  yä  ärmaiti/ (sd.) °zäcä  Y.4g.io;  —  mat  vä  padäis  (sd.) yä  frasrütä  (sd.)  -zaya  Y,  50. 8 ;  —  ^vldl- hmnäi  (sd.)  'zäcit  (IS.)  .  .  vahistsm  Y.jr. i;  —  ya%a  'za  (IS.)  viicim  näsima  Y, 70.4.  a)  Plur,  in  Verbindung  väwyaostay- usw.,  Plur.;    °m  yaostayS  fora^tayS  ärma-
```


## [2026-09-04T18:51:24.545Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== HRN leaf 129 (printed 108)\"; awk 'BEGIN{RS=\"\\f\"} NR==130' HRN.txt\necho \"===== HRN leaf 270 (printed 249)\"; awk 'BEGIN{RS=\"\\f\"} NR==271' HRN.txt",
 "description": "Print Horn pages 108 and 249"
}
```


### [2026-09-04T18:51:26.673Z] TOOL RESULT

```
===== HRN leaf 129 (printed 108)
— 108
486. yi^usur 'Schwiegervater.
aw. /asitru' 'Schwiegervater ; ai. imruru-; arm.
skesr]ah\ d. i. 'Mann der Scliwiegermutter (Hübsch-
mann, Xo. 253).
kuvd. /a2ur, xozJ)\ /aur 'Schwiegervater ; afy. s^or;
bei. n. vasarik 'Schwiegervater, vasar\2ä/t *Schwager
(405); wa;K'. yjtrs, sar. (LW.) Xasur.
•Vergl. /Hsrä (No. 487).
487. xusrfi, zesä^ /jisü^ /'es etc. 'Schwiegermutter.
Käs. /asrii',
ai. <;DarrU' 'Schwiegermutter'; arm. akesnr (H. No. 253) ;
lat. socru-s; ksl. soekry.
kuvd. /ost, /esü, yasrü 'Schwiegermutter; af/. ;K''ö4fa ;
bei. V((8sö, vasl, vase (406) ; wa;^. /as, si/n. /as, sar. /,e/.
Vergl. ytisur (No. 486).
488. x^Ht 'Ziegel, Backstein'.
aw. istya- 'Ziegel, Backstein' ; phlv. /ist ; skr. isfakOr-
'Backstein'.
afy. LW. /ßta; bei. ist (168).
489. ^usk 'trocken', /ös« ') 'Ähre', yös, yöslden, yösdniden
(AM. 236 Zeile 3 v. u.), /mkUm,
Kä§. tisk (jendn, husküdSn.
ap. Msia- trocken'; aw. huskd- 'trocken*, aflluiosemnu'
'nicht vertrocknend'; phlv. /<*^Ä;, /usklh^ /ösTnUän
(Bund.)-); ;rösaA; 'Ähre' (Bund.); ai. güska-, güsyati,
skr. gösa-.
kurd. LW. hüsk; afy. vud; oss. /tisk, ba/ussin (311
und Seite 141); bei. husay 'trocknen, austrocknen (160)
(LW?); wa/. vesk,
np, /uskar {/usk ärd, Vullers, 756, vergl. dial. ör,
oben No. 13), arab. LW. x^iskar 'Mehl', phlv. /nsk[a]r
V
(vd. 6 (9) Gl., Say. näsäy. 2, 35). Vergl. de Lagarde,
Semitica 1,41, Nöldeke, ZDMG. 32, 408; de Lagarde
*J Phlv. ;(Osak (Sternbild, Bund.); kurd. t*st, vasi^ krisl; afy. vazai;
bei LW. hösay, d. hösay (100).
2) Vd. 5 (43) (44) steht zwei Mal xösinUan,
===== HRN leaf 270 (printed 249)
- 249 —
4ll3. höm 'Haomastrauch, -pflanze*; vergl. hfun (d-majüH
. -^wo^ *Magierhaoma (eine nicht näher zu bestimmende
^^|j^' Pflanze, AM. 268).
'' aw. haowa-; phlv. hötn; ai. soma-.
bei. vergl. hörn (LW., 99).
V1114. Äe^ jemand, jemals*, mit Negation 'niemand, nichts;
ec (äähn. I, S. 4 Vers 59).
W^ Käs. K. Z. ec,
ap. *(tiva ~r ciy (Salemann, Mel. asiat. IX, 241);
phlv. ec bezw. hec (päz. hec, hSöi),
1115. herhud *Feuerpriester , herkede, hermend, {her *Feuer',
das man daraus erschlossen hat, ist aber bedenklich^).
aw. aeAlrapaiti' ; phlv. ehrpat (Inschriften), lierput,
herpatastän, herputlh bezw. erpat,
1116. lilrek, {^hereh?) 'Bockchen, Zickchen'.
ap. *yö*V7/ra- 'Jährling (Tomas chek, Centralasiat.
Studien II, 766).
si/n. yirk 'ausgewachsenes , männliches Schaaf,
Zuchtwidder.
Wenn die Etymologie richtig ist, so hätten wir
in diesem Worte die einzige neupersische Spur des
aw. yär-, ap. -yära-.
' 1117. hezutn (Is. 30, 88), hezem 'Brennholz*; Mme-).
^c^^ S- i^^i(^\ Käs. Q. K. hezem, ezem,
^ aw. a^sma^^') 'Brennholz'; phlv. esw (nur um-
schreibend), hEzam bezw. ezam (päz. hezam) ; ai. idlimd-.
kurd. ezink (H.-Sch.); minj. czma.
*) FJ hat zwar einen Vers von Emir Muizzi; im Awesta und
Pehlevl kommen ae^ra- oder ehr *Feuer* auch nicht vor.
*j Nicht gehört hierher syr XOPDi tal«»- NDVNi Nnom? Low,
Aramäische Pflanzennamen, 8. 146.
^) Das is in aesma- beruht auf einer 'Verschleppung*, wie in gr.
TTHOfiu., o(i/ur^ etc. (Joh. Schmidt, KZ. 27, 814, Bartholomae, Ar.
Forschungen II, 86).
```


## [2026-09-04T18:51:44.211Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD xist\"; grep -n -i \"xišt\\|xist\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== PHD hezum\"; grep -n -i \"hēzum\\|hezum\\|ēsm\\b\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== PHD azak/goat\"; grep -n -i \"^azag\\|azag \\|'goat'\" PHD.txt PHD_mackenzie.txt | head -20",
 "description": "Grep MacKenzie Pahlavi dictionary"
}
```


### [2026-09-04T18:51:44.296Z] TOOL RESULT

```
=== PHD xist
PHD.txt:24:ALMOST every published list of Pahlavi words contains a number of entries of doubtful nature, the uncertainty lying either in their form, their meaning, or even, occasionally, their very existence. The purpose of this dictionary is to provide the student with a representative vocabulary of Pahlavi in which such uncertain words have been reduced to a minimum and marked. It differs from its predecessors in that the Pahlavi words are given in a phonemic transcription representing, as far as it is deducible from the evidence, the pronunciation they would have had in the third century of our era, the period of the rise of the Sasanian empire. The reasons for this departure from the 'archaistic' tradi- tion of Pahlavi studies I have given elsewhere.! If one reason stands out it is that of practicality, as most corroborative evidence comes from this period.
PHD.txt:161:a- P- | M ?-] privative prefix, un-, Jess, а D] then (generally with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: powerlessness; anarchy. abādyāwand Pf?tyd”wnd | J ?b’dywn<d>] powerless, weak. ~ih: powerlessness, weakness. арар [LW TE < A lwt-h | M?Pg, N (a)bā] with. ~ih Dë kuk) company, assistance. abāgēnīdan, abāģēn- [^P'kyn-ytn!] accompany. a-bahr РРА] portionless, deprived. abām Pf?m | P ?bmyh, N (a)wàm] loan, debt. Abàn PPn! | M'0x, N ~] cal. 8th month; roth day. aband (nd, v. рапа | M ?bnd] erring. “АҺ: error. 'abar [ODM < А дат; bl | M "be, N bar] up; on, over. ~ āmadan: rise (sun). ~ āxistan: rise up. ~ āxrāmīdan: step up. — burdan : undertake. ~ madan: cope with, comprehend. ~ nigeridan: consider. ~ nihumbidan: conceal. ~ niSastan: sit, be enthroned. ~ nišāstan: seat, install. ~ rasidan: come to, upon. ~ rasidan б: attain. tabar Dél higher, superior. ~ag [-g | MP brg] superior. ~agan(ag) [-k’n(k)'] superior. --dar [-t, Zenit | M ?brdr] higher. ~dom [-twm | M ?brdwm] highest. —domih [-twmyh] superiority. abargar [5/21 god, divinity. abarig(àn) ['Bblyk( ny] = abarag. abarig DPryk! | M ?Pryg, J ?Pry] other.
PHD.txt:193:---rēšn(ih) [-Iwsn!, -lwsnyh] Infinite Light. anāhīd р/у | N ndhid] immaculate; a goddess; astr. Venus. an-àáhóg P7 kwok!] undefiled. an-ālūd [?77/wt'] undefiled. a-nāmčištīg m mcftyk!] unspecified. an-ámurzid [?rmwlcyt! | M ?n’mwrz‘yd] merciless. an-āmurzišn [*7”mwicšn!] mercilessness. anār [71 | N ~] pomegranate. anārģēl [777/gy/ | N nārgēl) coconut. an-arzünig [?77/c”nyk!] undeserving, unworthy. an-ast [^n 4 Y T'] non-existent.
PHD.txt:194:~ih : non-existence. ānāst [?n’st'] spoilt, destroyed.
PHD.txt:219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
PHD.txt:223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
PHD.txt:512:nest [LOY T! < А P?yty | M nyst, N ~] is not. ~ih : non-existence. néw [TB < A tb; nyw' | = M, N —] good, brave. ~-ardaxSir [nyw lthsyl | N nard !] backgammon. nézag [nyck! | N néza] lance. nēzūmān, —16 [nycwmn', -yk! | M nyzwm!n] dextrous, skilful. -~th: skill, artistry. nibard [nplt' | N nabard] fight, struggle, battle. ~ag [-k! | N ~a] tried, experienced. nibardīdan, nibard- [npit-ytn! | P nbrd'd] fight, do battle. nibastan, nibay- [SK BHWN-tn! < A У hb; npstn', npd- | M nbst] lie down, sleep. nibāstan, *nibày- [np'stn! | M nb’st, nb y-] lay down. nibég [npyk! | N niwé] writing, scripture, book. nibém [npdm | (P nbdm-)] lying, prostrate. nibištan, nibés- [VK TY BWN-stn! < A yktbwn, У КЬ; npstn' | M nbyšt, nbys-, N —] write. nidan, nay- [YD(B)LWN-tn! < A ydbrwn, V dbr | M nyydn, ny-] lead. nidom [nytwm] least, smallest. nifridag [nplytk' | N nifrid] accursed. nifrin [nplyn' | N <] curse. nigah [nk’s | M пол, N ~] look, attention. ~ dāštan: watch, keep. — kardan: look. ~-darih, —-dári&nih [-d?/(sn)yh | N —dārī] keeping, care. nigān [nk’n' | P ng’n] buried. nigar- [nk’l- | M ng’r-, N ~] draw, design, paint. ~ag [-h! | (M agin, N nigār)] image, picture, diagram. nigástar [nk?s I] guard; protective. nigeridan, niger- [nkyl-ytn! | N nigaridan] look, observe. --išn: observation. ~iSnig : evident, manifest. nigéxtan, nigéz- [nkyhtn!, nkyc-] expound. ~i$n: exposition. nigéz [nkyc] exposition. nigün [nkwn! | N ~] inverted, upside down. ~th: depth, downward direction. ~sar [-s?l | М ngwns’r] downwards. nihadag [nyd’tk' | M ny? dg] foundation. nihādan, nih- [TNH TWN-tn! < А hnht, ~ nht | M пуа, nyh-, N ~] put, place, establish. nihal [nbl | N ~] sapling, self-planted tree. nihān [nyh’n' | N ~] concealment, secrecy. ~ig [-yk! | N ~7] secret. nihang [nsng] small, few.
PHD.txt:570:Srēš [slw$ | M sros, N surūš] the god Obedience; cal. 17th day. ~ig [-yk'] obedient. srū [slwb' | N suri(n)] horn, nail, prong. srub [s/(w)p | N usrub] lead. ~ën [-yn'] leaden. srüdan, sray- [s/wtn', sPd- | M sry-, № sur~] sing, recite, play (an in- strument). ~i$n(ih): singing, recitation. srüwar [siwbw!] horned. srūwēn [slwbyn'] horny. stabr [stpl | M stbr, N sitabr] big, coarse, strong. 7-ih : coarseness; strength, force. stabrag [stpik! | Ar. istabrag] shot silk. stadan, stán- [YNSBWN-tn' < A ynsbwn, V nsb | M ‘std, *stn-, N sit~] take. staft [stpt! | M ‘stpt] hard, firm; harsh, tyrannous; very. stahm [sthm | N sitam] power, oppression. ~ag [-k'] strong, oppressive. ~(ag)ih: oppression. stambag [sthmbk! (-h- < stahm) | M ‘stmbg, N sitamba] oppressive; obstinate. “АҺ: oppression; obstinacy. stān-, v. stadan. star [sil] = stāraģ. stárag [st?/k! | M ‘st?rg, N sitara] star. stard [st!/t!] stunned, stupefied, confounded. ~ih: stupidity, stupefaction. : star-Ošmār, -6šmur [stProfm?l, 2wfmwl] astrologer. starwan [stlwn' | N sit~] barren, childless. stáyIdan (s? dytn! | M гуд, N sit~] = stüdan. Stéy [styk! | N. sitéy] erect. sténdag [styndk!] standing, erect. stér [styl | N sitēr] stater. Stézag [styck! | M ‘styz-, N sitéza] quarrel, strife. sti [sty(y) = Av. sti-] being, existence. Std [stwh! | (P *stwb, N sutdh)] distressed, defeated. ~wih : distress. stör [stwl | P ‘stwr, N sutór] horse, mount; large cattle. «bān [-p’n' | N -bàn] (head) groom. --ģāh [-g’s] stable. *stēš [stw$] the fourth morning after death. stówénidan, stówén- [stwhyn-yin'] defeat, overcome, Stówih, v. sto. stüdan, stāy- [stwtn', st?d- | M ‘stwd, ‘st?y-~~, N sit—] praise. ~išn: praise. ~išnīg : praiseworthy.
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD.txt:1086:brick xišt.
PHD.txt:1836:existence (h)astih, axw(an), sti.
PHD.txt:1837:exists (h)ast.
PHD.txt:2932:non-existence anastih, néstih.
PHD.txt:2933:non-existent anast.
PHD.txt:3457:rise abar āmadan, abar àxistan, ul āmadan.
PHD.txt:3799:stand awištādan, ēstādan, pādan: ~ up āxistan.
PHD_mackenzie.txt:95:form, their meaning, or even, occasionally, their very existence.
PHD_mackenzie.txt:677:  ...... axistan: rise up.
PHD_mackenzie.txt:1061:an-ast ['nA YTI] non-existent.
PHD_mackenzie.txt:1062: ......ih: non-existence.
=== PHD hezum
PHD_mackenzie.txt:2271:izm [CYBA < A Iyb) I N hezum] firewood, fuel. OS1' ~j
=== PHD azak/goat
PHD.txt:380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
PHD.txt:545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
PHD.txt:4629:padir- padiragih padirag padiriftan padirign 12радіѕаг padist- padista(g) padistadan padistán -bed pid paywasag paywiz- paywazag paywāzišn paywand
PHD.txt:4644:frašn frašagirdīg frašagird frašamurw fradāg fradom fradomīh pardag pambagén pambag passaxt passáxtan passox passáz- passāzišn pasen pasēmāl pasēmālīh brin-t bridan™ passazagih passazag past, pist pistag
PHD.txt:5256:nāfag, wazag wabar wābarīgānīh
PHD_mackenzie.txt:1210:a~sazag ['sc)k ] unfitting, unsuitable.
PHD_mackenzie.txt:1537:bazag [bek ' I M bzg, N .....a] sin, evil.
PHD_mackenzie.txt:2497:gazag [gc'k ' ] biting.
PHD_mackenzie.txt:4529:sazag [se'k I N saza] fitting, worthy.
PHD_mackenzie.txt:5293:wAzag [w)ek l ] utterance, saying.
PHD_mackenzie.txt:6981:   nidan, riiyenidan, ziimenidan,         like (pr.) <:iyon, handazag i, hangos-
PHD_mackenzie.txt:8201:tazag                      'y<;to       tarmcnisnih        AUt-"U~~
PHD_mackenzie.txt:8579:                                           paywazag                  \~V",,.,V
PHD_mackenzie.txt:8614:pad-                       -tpV         passazag                  \~W(2)
PHD_mackenzie.txt:8883:sidigar                ~~te1-'        sazag                       ,yO'
PHD_mackenzie.txt:9885:wadwazag             \~t,)'\,.,1   willar                       ~ "',
PHD_mackenzie.txt:10445:gazag                               ,.!'" 4U        guftanl                 \\¥'\~
PHD_mackenzie.txt:12047:hand6zisnih              .AU ~ C\ t't-'      handazag                   \ ~ C2",)U ""
```


## [2026-09-04T18:51:45.933Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT leaf 190 (printed 175)\"; awk 'BEGIN{RS=\"\\f\"} NR==191' KNT.txt | head -60\necho \"=== KNT isti grep\"; grep -n \"išti\\|isti-\" KNT.txt | head -20",
 "description": "Kent Old Persian p.175"
}
```


### [2026-09-04T18:51:48.875Z] TOOL RESULT

```
=== KNT leaf 190 (printed 175)
. Skt. apa, Gk.
and, Lt. ab, Gt. af, Gm. ab, NEng. оў, off, pIE *apo. Used with vb. gaud- and in sbb. apaddna-, apa- niydka-; with suffix in apalara-, apara-.
apataram adv. ‘farther off, far off’; nsn. of
apatara-, which is apa- + comp. -fara- ($82,
5190.111), ef. Gk. adv. ётотіро. DNa 18; DSe 16f; XPb 25; XPh 16.
apaddna- sb. ‘palace’: from apa- + déna- ($147.I) to root *dà-, cf. Skt. apadhá- ‘conceal- ment’, Gk. атоблк ‘storehouse’. For development in later Iranian, with ара- by secondary length- ening (but not OP appa-, cf. $130), see Henning, Trans. Philol. Soc. 1944.110n. apadünam asm. D*Sal; АНЬ. apadàna (852.V) A’Sa 3, 4; A?Ha 5.
apantyüka- sb. ‘great-great-grandfather’: from apa- + niyäka- ‘grandfather’, cf. Lt. ab-avos
OLD PERSIAN
'great-great-grandfather'. §52.1) пет. A’Sa 3.
apara- adj. "later, after’: Av. Skt. apara-, from apa- + comp. -ra- ($32, 419.11). арата пет, XPh 47. aparam asn. as adv. DB 4.37, 42, 48, 68, 70, 87; DSt 10° (not apara-ma, nsm. with enel. abl., DB 4.37, 68, 87—and DSt 10°—as Bthl. AiW 77 suggests, following АКК. $a be-la-a ar-kt-a ‘who shall rule after me’).
apan*ydka-ma — (822,
pi- sb. ‘water’: Av. áp-, NPers. db, Skt. pl. nom. dpas, acc. apás, pIE *йр-, with or without i-extension, which seems to have become 5 in OP ($422). āpišim (= apis-Sim; $41, $130) nsf. DB 1.95f. apiyálsf. DB 1.95. abis (Skt. adbhts, and dat.-abl. Skt. adbhyds, Av. aiwyó, both from *ap- bh-; §75.1V, $130, §188.V, JAOS 62.269-70; see also s.v. abi) ipf. DB 1.86.
apiy adv. ‘thereto, very’: Av. arpi, Skt. ápi, Gk. prep. &t ‘on’, pIE *epi (§44, §191.1). In OP, normally enclitic, but sometimes written sepa- rately; often with dūraiy ‘afar’ (5136): dürai-apty ‘far and wide’ DNa 12; düray-apiy DNa 46; dū- raiy apiy as two words, DSe 11, DZe 6, DE 19, ХРа 9, XPb 18f, ХРе 8, XPd 13, ХР? 13, XPh 10f, XE 18, XV 14, A!Pa 14^, A*He 17f. Prob- ably vafsna[pi]y X Pg 7f (Ву. BSLP 34.1.32-4) with crasis, rather than vadsnd-[cily or vasnà-[di]y (Lg.
9.230); KT's lapli-maiy is eliminated by - -
-€
Cameron’s reading of utämaiy as completely visi- -
ble, DB 4.46 (ef. note ad loc.).
afuvayd, error of writing for aruvdya (855.11); see aruva-.
abiy prep. and prefix ‘to, against, in addition to’: GAv. aibi. LAv. aiwi, Skt. abht; conflux of pIE *mbhi, oHG umbi ‘round about’, and pIE *obhi, oCS ой ‘beside, by’.
(1) Prep. with acc., DB 140, 76, 80, 82, 84; 2.12,17, 73, 88; 3.2, 3, 14, 27, 56, 60, 71, 82; 5.12f, 21, 22^, 28, 26, 28°; DPd 18; DPe 24; DZc 9f, 12; XPg 10.
(2) Prefix with verb jav-, and first element in abicaris, abyapara, perhaps in Abirddus, but prob- ably not the base of abif. — —
abicari& DB 1.64f, word of uncertain form and meaning, probably asn. of s-stem (5185.11), to abi- + root car- ‘move, go’ (Av. caraiti, Skt. cárati, Lt. colit, 8”; $107), giving, in association
with the following gaidam ‘living personal prop- — .
LEXICON
erty’, а meaning ‘pasture lands’, cf. NPers. cáridán ‘to pasture’ (Spiegel, KT, Bthl. AW 89). Cf. also Tm. Lex. 64-5; Gray, JAOS 33.281-8; Hüsing, KZ 48.155-6; Hz. Ар] 51-4.
abiyaparam. adv. ‘later, afterward’, from abiy + aparam (§191.1V). ab*yapara (822, §52.V) A’Sa 4.
Abirüdu- sb. ‘Abiradu’, a village in Elam: first part perhaps abi-.— Abirüdus пэт. DSf 46.
abi$ DB 1.86, probably not adv. ‘thereby’, abi- + adverbial -s, but ipf. of арі- ‘water’ (q.v.): not an error for äpiš nsf. ‘water’ as proposed by König, Кар 70-1.
abyapara see abiyaparam.
-am, enclitic particle extracted by wrong di- vision from pAr. *azham T’, perhaps even in pIE times, and therefore *-om from *ej(h)om; seen in OP tuvam (cf. adam T’), iyam, imam, patisam, cf. Skt. fuvám тубт imám ete.
ama- sb. ‘offensive power’, see ArSdama-.
amaxamaté, DB 4.92, read by KT, and ap- parently corresponding to Elam. ‘were pleased (at the inscription)’ (cf. Wb. KIA 72n, quoting vari- ant interpretations): possibly for ham-axmatá, aor. mid. of ham- + kam- ‘like, love’ (OP Хата- ‘wish’, Skt. vb. kam- ‘love’),
=== KNT isti grep
3880:90 ayd : cáxriyalà : рай$ат : iya : dipiS : hama : ёбаһауа}а : nipištiyā : adā
5155:isti- sb. ‘sun-dried brick’ (5152.11, 5179.11): Av. tštya-, NPers. 110, Skt. istaka-, Medieval Skt. isttka- (König, Burgbau 51-2; Wb. AfOF 7.41; Hz. AMI 3.57-8; W. N. Brown, Lg. 8.13). 2328 nsf. DSf 29.
5609:nipisti- sb. ‘impression’: deriv. of ni- + paid- ($152.11).  [niplisftiya] Isf DB. 4.90 (conj. of Kent, JAOS 62.268).
5617:paié- vb. ‘cut, engrave, adorn’: Av. paésa- ‘adornment’, Skt. pisdtz ‘cuts, adorns’, Gk. токіћоѕ ‘variegated’, OCS pisati ‘to write’, pIE *peik-, cf. Lt. pingit ‘embroiders, paints’ (Wb. AfOF 7.42). Cf. also nipišti-, parsiyd-, Paišiyđwwādā-, pisa-. аріа imf. DSf 54 (§211; cf. Konig, Burgbau 72). [ар #} уа] imf. pass. ($220) DB 4.91 (JAOS 62.268). [pjisia nsf. past pte. pass. ($242.1) DSf 42 (Bv. BSLP 30.1.62; Konig, Burgbau 71; not dista with Hz. Apī 121-5].
```


## [2026-09-04T18:52:05.250Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"išti- sb.\")\nprint(\"charpos\",i)\nprint(\"leaf(0-based ff count before):\", t[:i].count('\\f'))\nEOF",
 "description": "Find Kent leaf for isti-"
}
```


## [2026-09-04T18:52:05.738Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN leaf 628 (printed 604)\"; awk 'BEGIN{RS=\"\\f\"} NR==629' SYN.txt | head -80",
 "description": "Print Buck SYN page 604"
}
```


### [2026-09-04T18:52:08.019Z] TOOL RESULT

```
charpos -1
leaf(0-based ff count before): 231
```


### [2026-09-04T18:52:09.781Z] TOOL RESULT

```
=== SYN leaf 628 (printed 604)
 streu-, etc. Walde-P. 2.638 ff, Ernout-M. 973 f. Grk. ordpviut, o7pavvipt, orpwrviw, NG ozpdvw; Lat. sternere (hence or with ad-, Rum. agterne, OFr. esternir, etc.; a REW 8248, Puscariu 151), and in differ- nt ent use struere ‘pile up, construct’; Ir. sernim, Br. streouz; Goth. straujan, OE stréowian, etc., general Gmc. (also perh. with different extension or by some analogy OE stregdan); SCr.  sterati, prostrijeti, Boh. prostt{ti’ (but ChSI. prostréli, Russ. prostirat', etc. rather ‘stretch out, extend’); Skt. sty-, Av. star-.
2. Lat. spargere ‘strew, scatter, sprinkle’ (> It. spargere, Sp. esparcir), prob. fr. an extension of *sp(h)er- in Grk. ozeipw ‘scatter seed, sow’, Arm. sp%em ‘scatter’, ete. (Walde-P. 2.670 ff.), rather than (as Walde-P. 2.673) more directly to Skt. sphirj-
; ‘roar, crash, burst forth’, ete., which seem to be of imitative origin. Walde- P. lc. Ernout-M. 959 f.
It. stendere, Fr. étendre, Sp. tender, all lit. ‘stretch, stretch out’, fr. Lat. ten- dere ‘stretch’ (9.32) orepds. REW 3083.
It. spandere, Fr. répandre, fr. epds. of Lat. pandere ‘unfold, expand, lay open’ (: patére ‘stand open’, Grk. TET avvupe ‘spread out, apart, open’, etc. Walde-P. 2.18). REW 3030.
Rum. imprdstia, deriv. of prashie ‘a sling’, fr. ChSI. prasta id., orig. then ‘sling, throw’. Cf. Ir. as-srédim (be- low, 3).
3. Ir. sernim, Br. streoui, above, 1.
Ir. assrédim, cpd. of srédim ‘throw’, prob., with unoriginal d-, fr. sréim ‘throw, hurl’, this fr. the root *ster- in
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
sernim ‘strew, Pedersen 2.626.
Nit. spréidhim, fr. ME sprede, NR spread.
NI. leathnuighim, fr. leathan ‘broad wide’. ;
W. taenu, fr. taen ‘a spreading, sprink. ling’, perh. fr. *(s)tagna@ : Br. ster Tiver brook’ (*stagra), Grk. oratw ‘drip’, oa yav ‘drop’, Lat. stagnum ‘pool’, ‘Spread’ in general sense from ‘sprinkle (water) over’. Walde-P. 2.612.
W. chwalu, Br. skuilh (Ir. scdilim et loose, scatter’) : ON skilja ‘divide, sepa- rate’, Lith. skelti ‘split’, ete. (9.27), Walde-P. 2.592.
Br. astenn, fr. Lat. extendere ‘stretch out, extend’. Loth, Mots lat. 165 f.
4. ON breida, Dan. brede ud, Sw. breda ut, OK (ge)br@dan, Du. uilbreeden, OHG, MHG breiten, NHG ausbreiten (in the older languages orig. ‘broaden, make wider’), fr. the words for ‘broad, wide’, ON breidr, OE brad, OHG breit, ete. Walde-P. 2.194. Falk-Torp 100.
OE sprédan, only in epds. tospradan ‘extend, expand’ (wings, fingers, etc.), ge-sprédan ‘extend (the hand)’, ofer- spr@édan ‘cover (a bed)’, ME sprede, NE spread, Du. spreiden, OHG spreiten, MHG, NHG spreiten, fr. an extension of the root *s(p)her- seen in Grk. orelpw ‘sow’, Lat. spargere, etc. (above, 2). Walde-P. 2.671.
5. Lith. igt
```


## [2026-09-04T18:52:16.109Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nfor fn,pat in [('KNT.txt','sun-dried brick'),('SYN.txt','BRICK')]:\n    t=open(fn,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    for i,p in enumerate(pages):\n        if pat in p:\n            print(fn,'leaf',i, repr(p[:120]))\nEOF",
 "description": "Locate leaves for Kent isti and Buck BRICK"
}
```


### [2026-09-04T18:52:17.690Z] TOOL RESULT

```
KNT.txt leaf 166 ' the presence of vašnā Auramazdaha (JAOS 51.196) ; but there is no space for it in tablet a. There is also no room for a'
KNT.txt leaf 197 '�; 4.33; DPe 7; DNa 16; DSe 15; DSm 5°; XPh 14. ima apf. DB 1.21; D$g 3°.\nima nsn. DB 1.27, 72; 2.01; 3.10, 20, 58, 76; '
SYN.txt leaf 659 '%metselen ‘build in stone’, fr. MDu. mets(e), maets(e) ‘mason’: OHG  stein-meizo, NHG steinmetz ‘stonecutter’, fr. a Gal'
```


## [2026-09-04T18:52:25.267Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==198' KNT.txt | head -40",
 "description": "Print Kent leaf 197"
}
```


### [2026-09-04T18:52:26.924Z] TOOL RESULT

```
�; 4.33; DPe 7; DNa 16; DSe 15; DSm 5°; XPh 14. ima apf. DB 1.21; D$g 3°.
ima nsn. DB 1.27, 72; 2.01; 3.10, 20, 58, 76; 4.1, 9, 40, 49, 59; 5.2; DPh 4; ОМ 32; DSf 22; DH 3. ima asn. DB 1.25 bis, 26, 68; 444; DNb If; DSf 10; DS} 2°, 5°; ХРе 10f; XPd 16; XSa 1; Х8е 3°; XV 20; А:Ра 19°; D'Sb3?, 4°. imá apn. DB 432. imaibiš ipn. DNb 48.
Imaniš- sb. ‘Imanish’, name assumed by the Elamite rebel Martiya (§163.V): Elam. um-man- nu-$, АКК. tm-nia-ni-e-Su. — Imani$ пә. (8185.11) DB 2.10; 4.16f; DBF 4.
уат demonst. adj. and pron. ‘this’ ($11, $260.I1I, $265): from * nsf. (perhaps also from *? suffixless пзш.) -+ pronominal -am (q.v.). Decl., $199. Seealso?dà,/ma-. тат pron. пет. DBb 1; DBe 1; DBd 1; DBe 1; РЫ 1; DBg 1; DBh 1; DBi 1; рву 1; DBk1; DN i-v, xv, xvi", xvii, xxix; А?Р 1-4, 8°, 9-21, 22 (written imy*, $51), 23-8, 29°, 30. туат adj. nsf. AmH 5,8 (as Isf., §56.V);
DPd 6; DZe 10; iya (§52.V) DB 4.90; т |
DB 4.91 (written тё, $52. VI).
isuvd- sb. ‘battle-ax’ (Junge, Klio 33.223; Kent, JNES 4.233): etymology unknown (stem- formation $143.IV). Not ‘bowcase’, for ?$uvd-, to Av. ifu- ‘arrow’, Skt. fsu- (ef. for variant views Wb. Grab 41-8). _ iswām asf. DNd 2.
LEXICON
as- vb., see atš-,
isti- sb. ‘sun-dried brick’ (5152.11, 5179.11): Av. tštya-, NPers. 110, Skt. istaka-, Medieval Skt. isttka- (König, Burgbau 51-2; Wb. AfOF 7.41; Hz. AMI 3.57-8; W. N. Brown, Lg. 8.13). 2328 nsf. DSf 29.
ета or lismar\uy asn., of uncertain mean- ing, possibly ‘(gold) inlay’ (Cameron, Persepolis Treasury Tablets 129-30), DSf 51; supplied by Hz. AMI 3.74-5, as a borrowing from Elam. 25- ma-lu (@%ma-lu ‘wood’ Hinz, Orientalia 1950, shortly to appear), or from the lost Akk. original of both; сЁ JAOS 53.21, 56.220. But read rather Idàr|uv with Hinz, see Lex. s.v.
Izalàü- sb. 'Izala', a district in Assyria (86, $107): Elam.?5-$1-la.  Tizaljä nsf. DB 2.58, as re- stored by Wb ZDMG 61.726 (zara Tm. Lex. 74), after the Elam.; but Cameron found all the char- acters visible: 124.
^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
ukdra- adj. ‘having good people or army’: from u- ‘good’ + kāra- ‘people, army’.  uküram asn. for asf. AsH 9 ($52.11).
ucsnav- adj. ‘well satisfied’ ($142): from u- ‘good’ + zšnav- ‘satisfy’ (*wohlgeneigt", Hz. ApI 199-200; ихти ‘well-informed’, Sen 233). u[zina]us nsm. ($188.11, §190.1) DNb 27.
."ucüra- adj. ‘well done, successful’, as sb. nt.
‘good deed’: from u- + cãra-, to root kar- ‘do’ / (809, §122, §123.3), cf. LAv. dard- Hilfsmittel" NPers. батё (Ву. BSLP 30.1.65-6, Gr. $292; cf. Bthl. AiW 584); but Wb. AfOF 7.39-40, Hz. ApI 193-8, take from Ar. car- ‘move’ (Av. éaraitt, Skt. cárati; but Skt. has only sucürá as a woman's name!) ucüramnsn. DS} 4^; DSI 5. ucüram asn. DB 4.76; ucdramaiy DSf 20° (= ucéram-maty, $138.T).
uca$ma, incorrect reading for ст? = саат; see casa-.
^Uja- ^Uvja (83.1) sb. ‘Elam, Susiana’, a province of the Persian Empire ($166.П); also as
175
ethnic, ‘Elamite, Susian’: Elam. hal-tam-ti, Akk. e-lam-mat, ef. MPers. Ни? (Uja distinct from Uvja, wrongly Konig, Burgbau 9-11, and Hz. AMI 3.69-73). See also Ujiya-. (1) ‘Elam’: Ọja пзш. DSe 21°, DSm 7°; XPh 20. Uvja DB 1.14, 2.7, 5.4; DPe 10; DNa 22. Uvjam asm. DB 1.82; 2.12; 4.12, 17; 5.7, 10. {Лау lsm. DSf 46. Uvjaiy DB 1.74f, 75, 77; 2.10, 10f; 4.11, 17; DBe 9f; DBE 5. (2)'Elamite': Uvja nsm. DN iii; A?P 3.
^Ujya- *Uvjiya- (144.11) adj. 'Elamite, Susian’: deriv. of preceding. Uvjiya пет. DB 4.10, 5.5f. Unjiya npm. DB 1.75, 2.12, 5.15. Unjiyd apm. DB 5.11°. Uvjiyaibis ipm. DB 5.10,
ula (for шй, $36.I) conj. ‘and’ (52911-00): Av. ula, Skt. ш, Gk. Hom. -úre ‘like’, pIE *ute (hardly both -@ and - in Aryan, despite Mt. MSLP 19.57-8, MB Gr. 5151). Correlative with preceding -сӣ, DB 1.66f (cf. Gk. тё xai); ша... шб ‘both ... and’
```


## [2026-09-04T18:52:35.138Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    low=p.lower()\n    if 'xist' in low or 'xišt' in low or 'istya' in low or 'ištya' in low or 'brick' in low:\n        print('---- leaf',i)\n        print(p[:200].replace('\\n',' '))\nEOF",
 "description": "Find Buck brick pages"
}
```


### [2026-09-04T18:52:37.043Z] TOOL RESULT

```
---- leaf 13
anic and later ie i ae to-Slavic and from Slavic in Rumanian. But besides ranslation words”. A special use of a familiar foreign word age adopted for the usually corresponding native word. Thus Lat. b
---- leaf 27
Celtic Studies, Ber. Preuss. Akad. Sitzungsberichte der preussischen Akademie der Wissenschaften. Ber. Sichs. Ges. Berichte iiber die Verhandlungen der siichsischen Gesellschaft der Wissen- schaften z
---- leaf 34
led a Proto-IE stage, the forms of which deserve a double asterisk. For example, if the familiar IE *dhe- ‘put’ goes back to an earlier **dhe + a laryngeal, the contraction must have taken place befor
---- leaf 37
L Woops, Forest TREE Woop Stone; Rock Sxy, Heavens Sun - kéapos (olxovpévn, b) kécpos mundus mondo monde mundo lume domun (bith, b, c) domhan (saoghal, b, : bith, b, c) bed 1.53 1.54 Moon STAR LIGHTNI
---- leaf 40
 Grk. doris pas dpa ‘whoever sees the light’ = ‘lives’), hence ‘world’ in sense c, later ‘world’ in all senses, as in the present Slavic lan- guages. 7. Skt. loka- ‘open space, earth, world’ : Lat. la
---- leaf 50
, NHG berg, etc., the most widespread Gmce. word for ‘mountain’ (but ON bjarg ‘rock, precipice’; in Goth. only bazrga- het = dpewh ‘hill country’) : Skt. brhant- ‘high, great’, Av. barazant- ‘high’, b
---- leaf 62
ther by size, or as salt vs. fresh water), and the same word or related group may serve for either or both, or shift its pre- vailing application with changed physi- cal conditions. This is notably th
---- leaf 79
E clif, NE cliff, fr. the same root as ON klifa CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar Digitized by Arya Samaj Foundation Chennai and eGangotri 52 SELECTED INDO-EUROPEAN SYNONYMS 
---- leaf 94
��: OHG wele ‘with- CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar 66 ’ SELECTED INDO-EUROPEAN SYNONYMS ered, weak’ (secondary sense, cf. foll.), Lith. vilgyti ‘moisten’, Lett. valgs, ChS
---- leaf 116
are the usual ones ee atiter. See 2.43, 2.44. The ex- i in the opposite direction also Curs, but less frequently, words for ‘boy’, ‘girl’, and ‘child’ were originally colloquial nicknames, deroga- tor
---- leaf 119
n, KZ 36.331. Bjérk- man, IF 30.266. Norw. jenie (gjente), fem. to Dan. ganie, Sw. dial. gant ‘fool’. Falk-Torp 316. Sw. flicka : ON flik ‘patch, rag’, Sw. fuk ‘flap’, Norw. dial. flicka ‘go about wit
---- leaf 122
ps of cognates pointing to specific words for these rela- tions existing in the parent speech. The most widespread are those which are represented by NE father, mother, son, daughter, brother, sister.
---- leaf 178
r specialized to the bovine animals. Cf. NED s.v. NE stock ‘fund, property’ also used for ‘farm animals’ since 16th cent., hence livestock since end of 18th cent. NED stock, sb. 54, and livestock. 6. 
---- leaf 191
 Collection, Haridwar eee Digitized by Arya Samaj Foundation Chennai and eGangotri 158 SELECTED INDO-EUROPEAN SYNONYMS OE ramm, ME, NE, Du., OHG, MUG ram, prob. : ON ramr ‘strong’, from the ram’s stre
---- leaf 262
ra-, aki Ilyga G eC He lagad il ie , ae ‘fost of the words for ‘eye’ belong to sol, etc. ‘sun’ (1.52). Walde-P. 2.446. a ited group. The others are from | Pedersen 1.62. Stokes 692. an inher! Ir. rosc
---- leaf 265
us ‘cheek’, etc. (4.207). Ir. béoil, NIr. béal, see bel ‘lip’ (4.25). 5. Goth. munps, OE mip, OHG mund, ete., general Gmc., prob. : Lat. mentum ‘chin’, etc. (4.209), rather than : Lat. mandere ‘chew’,
---- leaf 315
 tune ‘underground room’) : Lith. ae i cover’, danga ‘a cover’, IE i lg -. Development fr. ‘covering’ to Ung’ as fertilizer, and also (independ- ently or through ‘dung’) to ‘heap Underground room’, Wa
---- leaf 362
inken ‘limp’ (= ON hinka, etc.) : Skt. khavj- ‘limp’, khafija- ‘lame’, Grk. oxatw ‘limp’, ON skakkr ‘awry, twisted’, IE *(s)keng-. Walde-P. 2.564. Falk- Torp 406. 5. Lith. raigas : Grk. fords ‘crooked
---- leaf 367
an, Pol. pijany, Russ. p’janyj (old mid. pple.? Cf. Meil- 4.99 NAKED, BARE Grk. —-yupvds Goth. nagaps Lith. nuogas NG —-yunv6s, ydupvbs ON —_ nokwidr, noktr; berr Lett. pliks, kails Lat. niidus Dan. n
---- leaf 378
 Falk-Torp 747. 5. Av. raé0wa- etym.? Barth. 1482 f. CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar Digitized by Arya Samaj Foundation Chennai and eGangotri SELECTED INDO-EUROPEAN SYNONYM
---- leaf 381
 LXX) fr. ziyavoy ‘frying-pan’ : OF peccan ‘burn’, etc. Walde-P. 1.717. Boisacq 936. 2. Lat. torrére, lit. ‘make dry’, hence ‘roast’ or ‘bake’ : Grk. répcouat, Goth, gapairsan ‘dry up’, Skt. trs- ‘thi
---- leaf 401
Russ. zauirak ‘breakfast’ or ‘lunch’ (in which case ‘the first meal’ is pervyj zavtrak ‘first breakfast’, or often simply ¢aj ‘tea’), epd. of za ‘at, for’ etc. and jutro ‘morning’ (14.34). Boh. snidan
---- leaf 404
ius Isid. 20.2.15), deriv. of focus ‘hearth’. REW 292. The Sprach- und Sach-Atlas Italiens und der Siidschweiz, Karte 1007 (vol. 5) also gives focaccia (schiacciata) as the heading = NHG Kuchen, Fr. g
---- leaf 417
enten, fr. groen ‘green’. NE vegetables, sb. use of adj. vegetable, fr. OF r. vegetable ‘capable of growing’, Lat. vegetabilis ‘animating, vivifying’, deriv. of vegeiare, iter. of vegére ‘move, quicke
---- leaf 426
erneker 355. Walde-P. 1.646. Pol. winogrono, cpd. of wino ‘wine’, and grono ‘bunch, cluster’, the latter either belonging to the above group (OPol. grozno) or more directly : SCr. grana ‘branch’, etc.
---- leaf 446
ol. rab ‘seam, hem’, Boh. rub ‘wrong side’ of cloth, etc.; cf. SCr. rubaéa, Russ. rubagka ‘shirt’) : Pol. rqbaé, Russ. rubit’ etc. ‘cut, hew’ (out- side root connections?), hence orig. ‘piece cut off’
---- leaf 459
 etc. Walde-P. 1.28 ff. Ernout- M. 8. Walde-H. 1.11. REW 119, 180. 3. Ir. sndthat, NIr. snathad, W. nod- wydd, Br. nadoz, fr. IE *sné- as in words for ‘thread’ (Ir. snathe, etc., 6.38) beside *sné- in
---- leaf 493
rmillae Sw. armband SCr. narukvica, grivna It. braccialeito OE béag Boh.  ndramek Fr. bracelet ME beg Pol. naramiennik, bran- Sp. brazalete, pulsera NE bracelet soletka Rum. brdfaré Du. armband Russ. 
---- leaf 503
� (1.63). Falk-Torp 1045. Feist 435. OE gles ‘glass’ as material (9.74), also as ‘mirror’, and so NE glass (with or without looking-) commonly to the present day (look in the glass). Similarly NG dial
---- leaf 510
 *geu-, as in the fol- lowing. Walde-P. 1.561. Falk-Torp 570, 1500. ON kot (ODan. kod ‘hovel’), OF, ME cot (also cote, NE dovecote, etc.), MLG kot, kote (NHG kot, kote ‘hovel’, Du. kot ‘hovel, sty, ke
---- leaf 513
e’. Walde-P. 1.360. Lett. pagalms, prob. as orig. ‘open space’: ChSl. golt ‘bare’, OHG kalo ‘bald’, etc. Cf. OPol. gola ‘open place’. Mihl.-Endz. 3.27. 6. ChSl. dvort, ete., general Slavic (but Pol. d
---- leaf 520
boden (diele, es- trich) CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar SELECTED INDO-EUROPEAN SYNONYMS lit. ‘wind-eye’, cpd. of the words for ‘wind’ and ‘eye’. Falk-Torp 1383. ON gluggr 
---- leaf 579
iod, and some still, cover both ‘flower’ and ‘blossom’. 1. From *bhis-”, *bhlé-, extension of *bhel- in words for leaf (8.56) and perh. orig. ‘swell’. Walde-P. 2.176 ff. Er- nout-M. 370. Walde-H. 1.51
---- leaf 587
etnik Akad. s.v. CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar Re ee ee ae ee ne a oes li yt he es AGRICULTURE, Dan. Sw. NE Du. NHG ryge réka smoke rooken rauchen carnigr (GrndP>s aly Ka
---- leaf 609
seems extrava- gant (some fifteen in Walde-P.), it is because ‘cut’ is merely a convenient common denominator for the historical uses. From the preceding it is obvious how difficult is the selection a
---- leaf 624
, strive’ esp. in Lat. tendere, ‘extend, lengthen’ dominant in NHG dehnen). Conversely, some one of these notions may be the more original, as in the case of NE stretch (cf. below, 5), or if a word fo
---- leaf 647
��build, erect’, fr. *con-od-ding- (cf. digen ‘firm’) : Lat. fingere ‘mold, fashion’, ete. (9.72). Pedersen 2.505 f, Nr. foirgnighim, cpd. of for- (: Grk. brép) and gni- in do-gnim ‘do, make’. W. adei
---- leaf 658
s orig. ‘something laid across’ : ChSl. préki (*perki) ‘crosswise’. 7. Skt. phalaka- : phal- ‘burst, split’, OHG spalten ‘split’, etc. (9.27), Grk. o¢& Aas ‘footstool, pedestal’, cpad(A)és ‘a kind of 
---- leaf 659
%metselen ‘build in stone’, fr. MDu. mets(e), maets(e) ‘mason’: OHG  stein-meizo, NHG steinmetz ‘stonecutter’, fr. a Gallo- Rom. *matsio = MLat. macio (above, 2). Meyer-Liibke, Wort. u. Sach. 9.67 f. 
---- leaf 660
 brique (OFr. and dial. also ‘piece, fragment’), fr. MDu. bri(c)ke ‘brick’, prob. also ‘piece, fragment’ (cf. MLG bricke ‘disk, plate, piece used in games’) : Du. breken ‘break’, etc. (9.26). REW 1300
---- leaf 661
nd was known to the Greeks and Romans, and spread thence, with brick construction, to northern Eu- rope. The majority of the European words are of Latin origin. Several con- tain the words for ‘lime’ 
---- leaf 676
as OF gler and a part OHG glas) : Ir. glass ‘green, gray blue’, W. glas ‘blue’, Br. glaz ‘green’, ON glesa ‘make shine, adorn’, ME, MLG glaren ‘gleam’, all prob. fr. an s-extension of I *ghel- in colo
---- leaf 691
.246. Falk-Torp 1372. Feist 543. ON hAluir ‘lot, share’ and ‘thing’ : OF hlot (NE lot), etc. Walde-P. 1,493. Falk-Torp 650 f. OE ping ‘judicial assembly, court’, ‘matter before the court’, then any ‘m
---- leaf 692
eneral i) ¥, i ty es-, Weak gi tade *s_. = MoUt-M. 1091, Walde-P, Grk. elut, Aeol. gupe (*esmi), 38g. éazi, NG eya (mid. starting fr. forms like imperf. juny NT), 3sg., pl. evar (fr. a = &eort; vowels
---- leaf 699
xwpe ‘it is agreed, may be done’) > ‘must’. Walde-P. 2.260. NED §.V. mote and must. Franck-v. W. 437. Weigand-H. 242f. Hellquist 678. OE néodab, ME nedeth, NE needs (: OE néad ‘need’, 9.93), also used
---- leaf 710
) some- times, but less commonly ‘difficult’. Sw. svdr formerly ‘heavy’, now only ‘diffi- cult’ (tung ‘heavy’). 5. Lith. sunkus ‘heavy’ (15.81) and ‘difficult’. Lett. grits, orig. and still locally ‘h
---- leaf 721
. an orig. meaning ‘mix’ : Skt. gri-, Grk. xepdvviue ‘mix’, etc. Walde-P. 1.419 f, Falk-Torp 987, 1536. Hell- quist 875, OE styrian, ME slyre (NE stir) : ON lyr ‘tumult’, NHG  stéren ‘disturb’, zrslor
---- leaf 747
iipfen 1. From extensions of IE Walde-P. 2.391 f., 707 f. *(s)lei-dh-, Grk. dAicBavw, OF slidan, ME, NE slide, MHG sliten, Lith. slysti, *(s)lei-. CC-0. In Public Domain. Gurukul Kangri Collection, Ha
---- leaf 749
OHG stincan ‘smell’ (15.21). Walde-P. 2.617. Falk-Torp 1168. Dan. hoppe, Sw. hoppa (ON hoppa ‘hop’) = OE hoppian, NE hop, ete. : CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar Goth. hups,
---- leaf 751
‘dance’ in NT translation, now obs.) : Skt. di- ‘soar, fly’, Grk. dtvéw ‘whirl’, Ir. dian ‘swift’. Walde-P. 1.775. Miihl.-Endz. 1.483. Lett. dancuot, above, 2. 6. ChSl. plesati, SCr. plesati, Russ. pl
---- leaf 791
l. okrut ‘cask’, Boh. krutina ‘knot, cradle’. Berneker 627, Briickner 377 f. Pol. statek, formerly ‘property, equip- ment, implements’ (cf. expressions like NHG fahrzeug, Dan. farigj, etc.), fr. the r
---- leaf 799
. W. hwyl MHG segel, sigel Br. gouel NHG - segel Most of the words for ‘sail’ meant originally ‘piece of cloth’, and several continued to be used in that sense also. This is true also of many colloqui
---- leaf 810
. dréati, Bob. drzeti (Pol. dzierzeé, obs.), Russ. derzat : CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar pOSsESssIO azaite ‘hold, have _ ‘strengthen, make : drh- a4 sxtensions of LB *dh
---- leaf 819
11.24). Pol. ratowaé, cf. rat, rata ‘rescue, help’, loanword fr. NHG retten (above, 4). Brickner 454. Pol. ocalzé, fr. caty ‘safe, whole’ (11.26). 7. Skt. taraya-, ‘cause to cross’ also ‘rescue’, caus
---- leaf 858
’, Aazpets ‘hired servant’, etc. Er- nout-M. 527. Walde-H. 1.771. REW 4931. Fr. voleur, fr. voler ‘steal’ (11.56). Sp. hurtador, fr. hurtar ‘steal’ (11.56). Rum. hot, also ‘robber, rascal’ and prob. o
---- leaf 860
 Lat. usually phrase mituum (ar- gentum, frumentum, etc.) dare lit. ‘give (silver, grain, etc.) loaned’; mituus : mitare ‘change, exchange’ (12.93) Er- nout-M, 648. It. prestare, imprestare, OFr. pres
---- leaf 921
 550. 5. Goth. filhan (also ‘bury’), ON fila : OF befeolan ‘commit, grant’, OHG (i)felahan ‘bury’, ete., perh. fr. an ex- tension ofa *pel- ‘cover’ inferred fr. Lat. Hea OE fell, ON fjall, ete. ‘hide,
---- leaf 947
. Meil- let, Etudes 221. Miklosich 273. SCr. oblik, lik: ChSl. lice ‘face, cheek’, etc. (4.204). Berneker 719 f. Boh. tvar : ChSl. tvort ‘condition, ap- pearance’, tvoriti ‘make’, etc. (9.11). Miklosi
---- leaf 951
ar- gus ‘abundant, copious’, etym.? Er- nout-M. 524. Walde-H. 1.764. REW 4912. NED s.v. 6. Lith. didis, didelis, etym. dub.; pos- sibly through ‘conspicuous’ : Skt. didi- ‘shining’, di- ‘shine’, etc. 
---- leaf 957
- P. 1.62. Pedersen 2.10. 6. Goth. braibs, ON breidr, OE brad, etc., general Gmc.; cf. Goth. us-braidjan ‘spread out’, etc., OHG breta ‘the flat hand’, etym. dub. Walde-P. 2.194. Falk-Torp 100. Feist 
---- leaf 966
 (> ME flatt, NE flat > W. jflat), Dan. jlad, Sw. flat: ChSI. ploskt (*plat-sko- or *plak-sko-?), SCr. plosnat, Boh. plosky (Boh. plochy prob. fr. OHG flah, Ge- bauer 1.441, Vondrak 1.436; otherwise B
---- leaf 982
�tear’, rytt ‘dig’, like that in Lat. rumpere, OE réofan ‘break’, etc. (9.26). Cf. ON rauf ‘hole’ (above, 4). Walde-P. 2.355. CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar wid Digitized 
---- leaf 1001
t’, Grk. b-Gevréy ‘thrive bloom’, ete. Walde-P. 1.679, 1,129. ' 6. ChSI. dovolinti, adj. beside dovitey : ‘suffice’, SCr. dovoljno, Russ. dovol’no i advs., cpds. of do- ‘to’ and second mem- B ber : Ch
---- leaf 1014
 aftuma), OE eftemest, superls. based on Goth. afta beside aftra ‘behind, backwards’, OE eft ‘afterwards’ beside after ‘after’, etc. Feist 12. Goth. spédists (also spédwmists, spé- diza once each), su
---- leaf 1031
d, frail’, t . (tuming) cycle’ of seasons, etc, Cf. Lat. | Grk. yépwy ‘old man’, etc. Walde-P. annus (ménsis) verténs ‘the course of a | 1.599. 14.12 AGE ue Goth. (alds) Lith. améius ; 4 ve ON aldr Le
---- leaf 1056
hen drag on, 3 ’ ae ilgt (Mihl.-Endz. 1.706), fr. ‘gs ‘long’ (12.51). Or commonly phrases wth adv. ilgi ‘long’ and but ‘be’ (ilgi nebija ‘it Was not long’), palikt ‘remain’, etc. But some are differen
---- leaf 1091
r. proljeée, also Boh. podlett ‘early summer, spring’, lit. ‘pre-summer’ (SCr. Ljeto, Boh. leto ‘summer’), Boh. jaro, Pol. obs. jar, jarz, old jaro, Russ.-ChSl. jara : Goth. jer ‘year’, etc. (14.73). 
---- leaf 1105
tc. (above, 2). ON illa pefadr, ila ilmadr, OE fil- stincende, OHG ubilo stinkenti (quot able?, cf. sb. wbile stank, Notker), phrases and epds. with ‘bad’, or ‘foul’ and pples. of the vbs. for ‘smell’
---- leaf 1114
he most nearly generic (in a few cases the selection is doubtful). Words like NE noise (though its use has extended to ee a tne Se eh CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar i Digi
---- leaf 1143
�, Skt a 6 , ‘ni’ ? . ¢rad- ‘cook, bake’ (fr. a - Walde-P. 1.419f. Falk-Torp fa heski, intens. lytéti ‘touch’ in a, Kurschat has pakrutinti ‘touch’ ». and NT) : Lett. laitit ‘stroke’, fr +] ae (perh, 
---- leaf 1168
*§heis- in Goth. US-gaisjan ‘frighten’, Av. zaéSa- ‘horrible’, Walde- P. 1.554. Feist 531. NED sv. ghost. ME, NE spirit, fr. Anglo-Fr, spirit = OF r. esp(e)rit, Fr. esprit (above, 2). 5. Lith. dugia ‘
---- leaf 1173
sti refl. shrases for ‘be troubled, care’, e.g. ne pecesi se = 0b pedrer cor, pecase = (Jagié, Entstehungsgesch. 370). Meillet, Etudes 416. euehev Brickner 406. ing dominant. Russ. zabota, prob. throu
---- leaf 1211
��wrinkle the nose’ : Lith. Septis ‘grin’, Sypsotis ‘smile’ (12.25). Walde-P. 1.364. Stokes 75. NIr. goilim, cf. MIr. gol ‘weeping’, prob. as orig. ‘cry out’ : OE galan ‘sing’, giellan ‘cry out’ (NE y
---- leaf 1244
 ( d DYOb. : krysie gig, fr. kryster ‘coward’, Squeeze, pr ; aie , press, hug’, hence ate hugger’ as an anes * Halk-Torp 587, Dahlerup s.v. c : Only sh coward, NE cowardly (coward (above, BOs, coart, 
---- leaf 1252
t (mostly biblical), epd. of blagi ‘good’ (influence of Grk. ef- in ebxa- pioréew) and *détt : ChSl. déti ‘place, put’, Grk. 7i@nu:, etc. Berneker 178. Similarly Russ. blagodarnost’ (‘thankful- ness’ 
---- leaf 1253
nry 120. Br. leal, fr. OFr. leel (above, 2). Henry 181. 4. Goth. triggws, ON tryggr (Dan. tryg, Sw. trygg ‘safe’), OE getriewe, tréo- we, ME trewe, NE true (now mostly arch. in this sense), OS triuwi,
---- leaf 1254
following group, ef. CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar H. Frisk, “Wahrheit” und “Liige” in den indogermanischen Sprachen (Géte- borgs Hégskolas Arsskrift 1935.3). 1. IE *wéro
---- leaf 1266
ti(s) ‘cease, quit’, OPruss. aulaut ‘die’, etc.; ‘bad’, fr. ‘pliant, yield- ing’. Walde-P. 2.405. Miihl.-Endz. 3.632, 7. ChSL. ziti, SCr. zao, Boh. zly, Pol. ay, Russ. zloj (in SCr. and Russ. now most
---- leaf 1276
e for verbal ‘blame’ culpar, or echar la culpa, lit. ‘lay the fault (blame) on’. 3. Ir. caire = MBr. carez ‘blame’, OW cared, arch. W. caredd ‘sin, crime, fault’ : Lat. carinare ‘abuse, revile’, OF hi
---- leaf 1294
teraeleane seilask (refl.) ‘stretch out the hand, seek Lith skait fi equa Way oa b pe | for, OPruss. seidins (pl.) ‘mind’, ChSl. | + rosy. bocide “hweth. in Skt. cit, cint- sila ‘strength’. et Walde- 
---- leaf 1337
 285. Walde-H. 1.375 f. Rum. indoiald, deriv. of vb. tndoi ‘doubt’, lit. ‘double’, fr. dot ‘two’. Tik- tin 801. 3. Ir. condubart (contubart), fr. *com- di-fo-ber- (but no finite vbl. forms quot- able)
---- leaf 1343
: raccdre ‘roar’ (of the tiger), all of imitative origin. Walde- P, 2.348. Mihl.-Endz. 3.519. Lith. §Saukti, Lett. saukt, prob. : ChSl. sova ‘owl’, Skt. guka- ‘parrot’, fr. an imitative *kau-, beside 
---- leaf 1386
he stift of NHG bleistift (?). 9. Russ. karanda§, fr. Turk. karadas ‘slate’ (cpd. of kara ‘black’ and tas, das ‘stone’), hence doubtless first used of the slate pencil. Lokotsch 1076. _ Digitized by A
---- leaf 1388
s, Fr. vers, OE fers, NE verse, NHG vers, etc., all most commonly applied to poetry (or ‘verses’ in the Bible), but Pol. wiersz reg. word for ‘line’ of prose or poetry. It. riga, fr. OHG (Langob.) rag
---- leaf 1389
ient, fr. OF r. priente, deriv. of Lat. premere ‘press’. 5. Lith. spaudinti, also and orig. ‘press’, beside spausti ‘press’, whence also spausdinti ‘print’ with sb. spaustuvé ‘printing house’. Lett. c
---- leaf 1395
t. patria (> Romance words); Ir. atharde, atharthir (K. Meyer, Contrib. 144); OE federépel, OHG fateruodil, NE fatherland, NHG vater- land, Dan. fedreland, etc. (see - list); Lith. tévyné, Lett. tévij
---- leaf 1411
stamme > Dan. stamme, Sw. stam), orig. ‘stem, stalk, trunk’, OHG stam only in the lit. sense (but ‘tribe, race’ in cpd. liut-stam) : OS stamn ‘stem, race’, OE stefn, stemn ‘trunk, prow’ (in epds. léod
---- leaf 1415
 the Roman emperor and the Persian ‘king of kings’ (19.34). For ‘king’ Lat. réx was adopted, e.g. pnt TorOwv, pre dpayxwv, etc. Theo- phanes (1.472f. DeBoor) notes the crowning of Charlemagne, s7£ tra
---- leaf 1420
specially in the plural (Grk. of yevvator, of etyevets, Lat. nobilés, patricit). : The majority are derived from words for ‘birth, family, estate’, that is, they mean literally ‘of (good) birth’, etc.
---- leaf 1430
ault, Dict. étym. 336. 4. Goth. andbahts, OE ambeht, OHG ambaht (ON only fem. ambdit), fr. Celt. *ambaktos (cf. Gallo-Lat. ambactus ‘slave, vassal’, W. amaeth ‘farmer, plowman’), fr. a epd. of ambi- ‘
---- leaf 1469
phrase with ljuby ‘love’ and déjati ‘put, perform’. Berneker 756. ChSl. bladinica (Supr. for zéprn), SCr. bludnica, Russ. bljudnica, deriv. of ChSl. blqdti ‘ropveta, fornication’, blqdite ‘err, fornic
---- leaf 1494
i and eGangotri WARFARE 1393 OFr. brant. REW 1273. 5. Lith. kalawjas : OPruss. kalabian id., Lat. clava ‘club’, fr. the root in Lith. kalti ‘strike’, etc. (cf. Ir. claideb, above 3). Trautmann, Altpre
---- leaf 1501
reast’ (4.40). Lett. krisu brun’as, gen. pl. of krits ‘breast? and brun’as ‘armor’ (20.31). Mihl.-Endz. 2.293. 6. Russ.-ChSl. briinja (Russ. bronja, Boh. brnént now mostly in the wider sense of ‘body-
---- leaf 1512
tion’), Grk. épboua ‘protect, rescue’, etc. Walde-P. 1.282. Falk-Torp 1369. Feist 551 f. Dan. forsvar, Sw. férsvar, fr. vbs. for- svare, férsvara ‘defend’, cpds. of svare, svara ‘answer’ (18.32). Perh
---- leaf 1527
udicial courts, not necessary). It was the most general word for ‘court’ (as still in Eng- CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar lish) until the introduction of tribunal, after
```


## [2026-09-04T18:52:43.471Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==661' SYN.txt | head -50\necho \"@@@@@@@@@@ leaf 661\"\nawk 'BEGIN{RS=\"\\f\"} NR==662' SYN.txt | head -60",
 "description": "Print Buck brick section"
}
```


### [2026-09-04T18:52:45.131Z] TOOL RESULT

```
 brique (OFr. and dial. also ‘piece, fragment’), fr. MDu. bri(c)ke ‘brick’, prob. also ‘piece, fragment’ (cf. MLG bricke ‘disk, plate, piece used in games’) : Du. breken ‘break’, etc. (9.26). REW
1300. Wartburg 1.522f. NED s.v. brick. Sp. ladrillo, deriv. of Lat. later
(above).
Rum. cdrdmidd, fr. NG xepaptéa ‘tile’, fr. Grk. xepauts ‘roof-tile’ : xépayos ‘clay, pottery, tile’ (9.73). Tiktin 290.
3. Ir. later, fr. Lat. later (above, 2). Vendryes, De hib. voc. 149.
Nir. brice ‘brick, tile’, fr. NE brick (below, 4).
W. priddfaen, cpd. of pridd ‘earth, clay’ (9.73) and maen ‘stone’.
W. bricsen, pl. brics, fr. NE pl. bricks (below, 4). Parry-Williams 104, 138.
Br. brikenn, fr. Fr. brique (above, 2).
4. Goth. skalja ‘roof-tile’ : ON skel, OE sczell, OHG scala ‘shell’, Lith. skala ‘splinter, fragment’, etc., fr. IE *(s)kel- in ON skilja ‘separate’, ete. Walde-P. 2.593. Feist 427.
ON tigl, Dan. tegl, also teglsten (cf. sten ‘stone’), Sw. tegel, tegelsten, OE tigele, ME tyle, tile ‘brick, tile’, NE tle, Du. tegel, tegelsteen, OHG ziagal, MHG ziegel, NHG ziegel, ziegelstein ‘brick, tile’ (NHG also mauerziegel ‘brick’, cf. mauer ‘wall’), all fr. Lat. tégula ‘roof-tile’ : te- gere ‘cover, roof over’. Falk-Torp 1251. NED s.v. tile, sb.}.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
604 SELECTED INDO-EUROPEAN SYNONYMS
ME (late) bryke, brike, NE brick, fr. Fr. brique (above, 2).
Dan. mursten, fr. MLG mirstén, cpd. of mur ‘wall’ and stén ‘stone’, Falk- Torp 741.
Du. baksteen, NHG backstein, epds. of words for ‘bake’ and ‘stone’.
5. Lith. plyia, fr. Pol. ptyta ‘slab’ (be- low, 6). Briickner, S]. Fremdwéorter 119.
Lett. kieg’elis, prob. by assim. fr. tteg’elis (dial.), fr. MLG tegel : MHG, NHG ziegel (above, 4). Mihl.-Endz. 2,390, 4.209.
6. Late ChSIl. plinita, plita (Pol., Ukr. ptyta ‘slab’ > Lith. plyta ‘brick’),
fr. Grk. rAivOos (above, 1), Brij a ) Tlicknoy
SCr. opeka : opeéi ‘burn’, peg ‘bake?
SCr. cigla, Boh. cihla, Pol. cegta, fy MHG, NHG ziegel (above, 4). Brite, ner 57.
Russ. kirpié (SCr. éerpié ‘unbaked brick’), fr. Turk. kerpi¢ ‘unbaked brick’, Berneker 501. Lokotsch 1184,
7. Skt. <slaka-, Av. i&tya-, OPers, astt- (Dar. Sus. f 29), NPers, Zit8t, prob, fr. *idh-s-to- : Skt. tdh-, Grk. at ‘kin- dle’, ete. Walde-P. 1.6, Johansen, IF 19.136.
9.55 MORTAR
Grk. — (wAés, xovia) Goth. Lith. kalkiu glaistas NG Adorn ON Hi Lett. mertelis Lat. _calz aréndtus, mor- Dan. mfrtel ChSl. ....
tarium Sw. murbruk SCr. _malter It. calcina, malta OE ero naye Boh. malta Fy. mortier ME _—morter Pol.  zaprawa wapienna, Sp. argamasa, mezcla, NE mortar ete.
mortero Du. mortel Russ. izvestkovyj rastvor Rum. tencuealé OHGaea.. Skt. (lepa-, sudha-) Ir. aera MHG morter Av. Aner NIr. —_ moirtéal NHG  mértel W. cymrwd Br. priraz
Mortar in the technical sense of a mix- ture of lime and sa
@@@@@@@@@@ leaf 661
nd was known to the Greeks and Romans, and spread thence, with brick construction, to northern Eu- rope. The majority of the European words are of Latin origin. Several con- tain the words for ‘lime’ or ‘sand’ or both. But as mortar was a substitute for clay, previously used for the same purpose, some words for ‘clay, mud’ or the like came to be used also for ‘mor- tar’. Some languages have no single word for ‘mortar’ but make use of ex- pressions meaning lit. ‘mason’s sauce’, ‘lime-cement’, etc.
1. Grk. andés ‘clay’ (9.73), used for clay serving as mortar and then prob. for true mortar, for which also adds
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
nxupwpévos ‘clay mixed with chaff’, IG 27.463.42,
Grk. xovla ‘dust’, also ‘lime, plaster’ (hence xomdw ‘to plaster’, xovtaos ‘plastering, stucco-work’ in building in- scriptions), also ‘mortar’(?); dupoxovla (rare) ‘sand mixed with lime, cement’ (cf. Gupos ‘sand’) : x6us ‘dust, ashes’, Lat. cinis ‘ashes’, ete. Walde-P. 1.392.
NG )éorn ‘mud’ (1.214), also ‘mor- tar’.
2. Lat. calx (h)aréndtus ‘lime mixed with sand, mortar’, also (h)arénatum alone as sb. ‘mortar’, cf. calx ‘lime’ and (h)aréna ‘sand’. ‘
Lat. mortérium ‘a mortar’ in which substances are pounded and crushed, hence also ‘that which is crushed in ®
MIS
‘mortar for puilding’ (> Fr. vortero iD both senses), ; n in Skt. mr- ‘erush,
t see her ‘bruise, crush’, etc.
pro s 1 ON merja
sf ‘dime’. riv. of Lat. calx
r, Lat. maltha ‘a kind of rowed fr. Grk. adn : padOaxdos
mrd- loam’ (9.73). 2.289. Walde-H. 2.17. oe asa (Oat., Port. argamassa),
. argam A of masa ‘mass, dough, mortar, but ent part dub. (relation to Lat. argilla
‘olay’ difficult). na omen ‘mixture’ (5.17), conimen= ly used by the workmen for ‘mortar’.
Rum. tencueala ‘plaster, mortar’, de- riv. of fencut ‘cover with plaster or mor- tar’, fr. NHG tinchen ‘cover with lime, whitewash, plaster’ through Pol. tyn- cowaé, Tiktin 1577.
3. Nix. moirtéal, with dissim. fr. NE mortar (below, 4).
W. cymrwd, etym.? (epd. of cym- ‘to- gether’ and rhwd ‘sediment, rust, dung water’?).
Br. priraz, cpd. of pri ‘clay’ (9.73) and raz ‘lime’,
4. MHG morter, with dissim. Dan.
CELLANEOUS PHYSICAL ACTS, ETC.
Digitized by Arya Samaj Foundation Chennai and eGangotri
605
mértel, Du. mortel, NHG mértel, fr. Lat. mortarium (above, 2) in second sense only.
ME morter, NE mortar (both senses), fr. Fr. mortier (above, 2).
Sw. murbruk, epd. of mur ‘wall’ and -bruk, this prob. the same word as bruk ‘use’. Hellquist 102.
5. Lith. kalkiy glaistas (NSB, s.v. kalkés), lit. ‘lime-cement’. Also Lith. murininko kosé, lit. ‘mason’s pap’, like Pol. zaprawa mularska (below, 6).
Lett. mertelis, fr. NHG miértel (above, 4).
6. Boh. malt
```


## [2026-09-04T18:52:53.296Z] TOOL CALL #28: Bash

```json
{
 "command": "python3 tools/ref_page.py --help 2>&1 | head -40",
 "description": "ref_page.py help"
}
```


### [2026-09-04T18:52:55.113Z] TOOL RESULT

```
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


## [2026-09-04T18:52:57.850Z] TOOL CALL #29: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2407 --image 2>&1 | head -60",
 "description": "Fetch BQT page 2407"
}
```


### [2026-09-04T18:53:06.787Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 490; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2407.png
REF: BQT:2407  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 490  OCR-lang: fas

-۷)- هیگر
مخنث وپشت پایی باشد؛ ودر فارسی های هوز با | لیزگویند از کتان که بیشتر در بلاد هندوستان
حای حطی بدل میشود ۱ - و بلغت پهلوی دلو | بافند۴ - وآهن جفت را نی زکویند وآن آهنی
گرمایه بان را کوبند که بدان آب بر اطراف باشد که زمین را بان شیارکنند۴ .
حمام ریزند وشست‌وشو دهند ودرین‌زمان پدولچه هیشر* « بفتح ارل وشن نقطه دار بر
مشهوراست . وزن قصر, کنگرسحرائی است ودرازی‌آن زیاده
هیزارها - یک اول و ثاك بالف | بريك کزمیشود وشکوفهآن پهن بود ماندبنفشه
کشیده و برای بی‌نقطةٌ زده و میم والف » بلفت | ودر میان شکوفهةٌ آن مانند پنوه چیزی است .
سربانی‌رستنیی باشد کهآ نرابعرپی‌نمناع کویند۳ . | اگر درکوش مردم رود کر گرداند .
اکرزن پیش ازجماع قدری ازآن بخود بر گیرد همیگر - باکان فارسی‌بروزن‌تیسر, اسب
آبستن نشود؛ بسن ی کوبند اين‌لفت رومی‌است.* | کمیت را کوبند یمنی اسب سرخ ی که بسیاهی
ههش - با شين قرشت بروزن و معنی ‏ مایل بود وبال ودم اوسیاه باشد؛ ویکسرکاف هم
هیچ‌است که لاشیء ومعدوم باشد۴ - وبافته‌ای‌را ‏ بنظر آمده است۹ .
۱ - «هیز, مخنث بود . عجدی (مروزی) گوید :
کفتم همی‌چ ه کوبی‌ای هیز کلخنی؟ کفتا که چه شنیدی ای پیر مسجدی؟»
«لفت فری س۳-۱۷۲>. ور4:: صحاح الفرس‌دشهٌ طاعتی.
« هیز. مخنث که مردم حیز گوبند.» «رشیدی» ؛ قی : پیشاوری 5:۸2 (پشت گردن, قنا) (ر43 :
مقدمهٌ کتاب حاضر ص‌نودودو هتن وحاشیهٌ؟۰ درفارسیکابل 0128و 1285 اخته را کوبند. «سعید
نفیسی» و رك : حیز . ۴ - در تحفةً حکیم موّمن « هیزاو ‏ اسم فارسی‌نمناع است.»
ان هیچ (و.م.) :
هن که آمد هن که آید میرود این جهان محنت سرائی بیش لیست
دیگران رفتند و ماهم میرویم کیت کو را منزلی در پیش لیست
احمد جامی ترا بندی دهد آخرت را باش » دنیا هیش لیست.
احمد جام « رشیدی > «فرهنکه نظام».
ای خیش (۸م.) «رشیدی» . 8 - (عر) «هیغر, کحیدر... گیاهی‌است سست.
با آن کنگردشتی‌است که کیاهی باشد با درختی‌است«یگستالی, پاک وکنار.» «تحقة کیم مومن»
«هیشر, عربی» اسم جنس حرشف است وازد بعلی مخصوص بری او» «تحفةً حکیم موْمن» .
٩-«هیگر‏ (بفتح ها وکاف فارسی) اسپ کمیت, ودرداشهٌ سروری بکسرکافاسپ سیاه
که بسرخی زند.» «رشیدی» ور4: سروری, نوروزنامه . تعلیقات م۱۳۹۵ ۰
0 هیزم - بتلفظ قدیم 13621000 (تلفظ کنونی 13120) » اوستا -869838 (هرمه)»
پپلوی68180 ,628۳32 . پازند 70ط1362, هندی باستان - 1080۳06 ۰ منجی 62708 «اسشق
۰ کردی 162:1362186 (هیزم سوخت) , 1162188؛ زازا 6121701 «ژابا س14۳ رل :
هیمه؛ چوب سوخت, چوب برای سوختن, هیمه :
ز حسی دان له از مقلی اگر در خود بدی بایی
زهیزم دان نه از آتش اگر در وی دخان بینی-
«سنائی غزنوی دیوآأن م60۲۷
```


## [2026-09-04T18:53:18.020Z] TOOL CALL #30: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:750 --image 2>&1 | head -70",
 "description": "Fetch BQT page 750"
}
```


### [2026-09-04T18:53:19.843Z] TOOL RESULT

```
no scan of BQT covers printed page 750 (see 'scans' in refs_online.json)
```


## [2026-09-04T18:53:24.643Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('npages',len(pages))\nfor i,p in enumerate(pages):\n    if 'خشت' in p:\n        print('leaf',i,'printed~',i+543)\nEOF",
 "description": "Find خشت in BQT vol2"
}
```


### [2026-09-04T18:53:26.429Z] TOOL RESULT

```
npages 684
leaf 64 printed~ 607
leaf 66 printed~ 609
leaf 79 printed~ 622
leaf 88 printed~ 631
leaf 89 printed~ 632
leaf 144 printed~ 687
leaf 177 printed~ 720
leaf 185 printed~ 728
leaf 186 printed~ 729
leaf 198 printed~ 741
leaf 202 printed~ 745
leaf 208 printed~ 751
leaf 209 printed~ 752
leaf 210 printed~ 753
leaf 213 printed~ 756
leaf 228 printed~ 771
leaf 233 printed~ 776
leaf 292 printed~ 835
leaf 463 printed~ 1006
leaf 465 printed~ 1008
leaf 495 printed~ 1038
leaf 496 printed~ 1039
leaf 543 printed~ 1086
leaf 547 printed~ 1090
leaf 550 printed~ 1093
leaf 594 printed~ 1137
leaf 595 printed~ 1138
leaf 625 printed~ 1168
leaf 647 printed~ 1190
leaf 651 printed~ 1194
```


## [2026-09-04T18:53:29.169Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==208 || NR==209' BQT_v2_pages.txt | head -80",
 "description": "Print BQT vol2 leaves 207-208"
}
```


### [2026-09-04T18:53:31.254Z] TOOL RESULT

```
  ‫جسوردن‬                                                                                                       ‫نله‬
 ‫خساث ‪ -‬بفتح اول وانی وسکون‌کافی»‬                                              ‫همجو خم خسروانی وامثالآن ‪.‬‬
 ‫خس وخاشاك وخاری‌باشد سه گوشه ‪-‬وخارهای‌سه‬                      ‫خسرو چهارم سریر ‪ -‬کناب‬
 ‫کوشهرانیز گوبند که انزدآهون‌دسرازسررامدشمن‬                                    ‫افزتآاب است باعتبار فلك چهارم‬
‫گذارند ودراطراف وجوالب حصار وقلعه ریزتلد‬                     ‫یه است از‬       ‫خسرو خکاونرا‪-‬‬
 ‫وبضم اول مطلق وقت رکاوبند اعم ازصبح وشام‬
                                                                ‫خورشید ‪ -‬ویادشاه مغرب را نیز گوبند ‪. ۱‬‬
‫زته‌اند ‪ -‬وبکر‬
             ‫وغیره ‪ -‬وتأخیرودرنگه رائیگزف‬
                                                               ‫حسر و داد وه رستنی وداروبی باشد‬
  ‫تکرهاکل‬
        ‫آشد‬
          ‫»ل معصفر با‬
                    ‫اول وسکون انی ک‬                            ‫کهآ نرا خولنجان کویند» وبسنی گفته‌اند درختی‬
‫کاجره‌خوانند وتخم| نرراخك‌دانه گوند رسربی‬
                                                             ‫است منسوب بانوشیروان‪ ,‬که‌چوب آن درخت را‬
                  ‫قرطم وحب‌المصفر نامند ® ‪.‬‬                    ‫خالولنجان خواندد‪ .‬وجمعی کودند نبانی‌است که‬
                      ‫خکانان" ‪-‬‬                                 ‫آنرا سفید تاك نامند و بکعرربمیةالبیضاخوانند‬
 ‫ی و تجس بجد ونفتش وجتجوی‬
            ‫بایغ باشد وبعربی استقصا خوالند ‪.‬‬
                                                               ‫و میوآن سرخ میباشد و بخوشة انگور شباهت‬
                                                               ‫‪۳‬‬   ‫داردوندان دوست رادیاغت دهنف» ودراختبارات‬

                                                                                ‫بجای حرف اول جیمآورده است‬
‫تخم کاژیره است و آنرا بعربی حب الصفر‬                         ‫خسرو زریی عطاه کنابه از‬
                                           ‫خوانند ‪.‬‬
                                                                                             ‫آفتاب عالمتاب اسب ‪.‬‬
‫اول وسکون ثانی ومیم»‬    ‫‪ .‬تک‬          ‫خم‬
                                                                ‫خسر و سيار گان = بمعنی خرو‬
                        ‫بمەنی جراحت باشد ‪.‬‬                     ‫که کنابه از آفتاب عالمتاب‬
                                                                                       ‫زرین عطا است‬
‫‪ = ۸‬بفتح‌اول بروزن پرئده »‬           ‫حسنده‬                                                                     ‫باشد ‪. ۴‬‬
                                                               ‫حسرو دشستم لهشت د اشاره به‬
‫حسودن = بروزن کشودن؛ درو کردن‬                                             ‫حضرترسول صلوات‌انه عليه وا لهاست‬
                                                               ‫خسروی ‪ ۴‬س نوعی از شراب عرفی‬
‫حسو و ب«روزن قصور‪ ,‬پدرشوهر ویدر‬
‫زرا کویند‪٩‬‏ ‪ -‬و بمعنی دروهم هست که بربدن‬                     ‫ت‌‌ بروزن علف» گردکان‌باشد که‬                 ‫حف‬

                                ‫غله وعلف باشد ‪.‬‬                                         ‫‪۱‬‬    ‫ف‬   ‫هم کو‬         ‫آترا جوز‬


‫صم اول وفتح دال امحد‪,‬‬
                    ‫ض‬   ‫ص‬     ‫حسوردن‬                                ‫‪۰‬لی است‬
                                                                          ‫حسق = بر وزن شفق ک‬
‫بمعنی خسودن است که بربدن ودرو کردن علف‬                         ‫و دعر دیعصفن‬   ‫تِِ‬           ‫آ نرا‪,‬صفاهاتی گل کاویشه‬


                                     ‫وغله باشّف ‪۰۱‬‬                                                             ‫خوانند ‪.‬‬


                                                                            ‫(‪ )۱‬چك » چش ‪:‬کافشه ‪.‬‬

   ‫‪ ۳‬ك مراد (اختمارات‪,‬دیعی) است ‪ .‬رك‪ :‬ص‌هشتاد وشش‌مقدمه‪.‬‬                            ‫‪۰‬‬   ‫خاور‬     ‫رك‪:‬‬   ‫_‬   ‫‪۱‬‬



           ‫صح نختن‌نمود روی بنظار کان‬                              ‫‪- ۴‬آمد بانگه‌خروس‌موذن میخوارگان‬
  ‫روی_بمشرق نهادخسروسا رگان‪...‬‬                  ‫که بکتف برفکندچادر (ب رگرفت‌جامة) بازارگان‬
      ‫‪ ۵‬منوچپری دامقالی ‪٩ ۵6۱‬‏ ‪.‬‬
                            ‫دانه ‪.‬‬    ‫‪ :‬خك‬    ‫رك‬    ‫_‬    ‫®‬                 ‫بیت‬
                                                                             ‫د‪+‬‬‫(رو‬
                                                                                 ‫‪ ۴‬از ‪:‬خ‬
  ‫‪ _ ۸‬لغتی‌درخز نده (ھ‪.‬م‪(.‬‬             ‫‪.‬‬   ‫_ رك ‪:‬خك‬            ‫‪۷‬‬        ‫‪ - ۱‬مصحف «خدکامار» («‪.‬م‪.).‬‬
                                            ‫خسودن‬       ‫رك ‪:‬‬        ‫‪۶‬‬              ‫‪ ,‬خنوره ‪.‬‬       ‫رك ‪ :‬خر‬        ‫‪-‬‬   ‫©‬

 ‫‪Yg‬‬     ‫~‪m‬‬                                                                                      ‫‪‎‬هرو‬


‫بمعنی‬   ‫‪ -‬بر وزن رسیدن »‬         ‫خسدن‬                      ‫خسوره ه بم اول وفتح رای قرشت؛‬
‫استت که در زیر «ندان ترم کردن‬           ‫خایدن‬              ‫یمضی خور استت که پدر شوحو و پدر زن‬
                                                                                                    ‫يلد‪٩ ‎‬‬




                                                    ‫بیان دهم‬
             ‫در خای نقطه دار باشن نقطه دار مشتمل بر هفتاد و هفت‬

                                               ‫لغت و کنات‬
```


## [2026-09-04T18:53:41.876Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==210' BQT_v2_pages.txt | head -60",
 "description": "Print BQT vol2 leaf 209"
}
```


### [2026-09-04T18:53:43.596Z] TOOL RESULT

```
                                                                                                ‫یوا‬


‫‪٩‬‏ ‪-‬‬    ‫ند‬
         ‫زبان‬
            ‫دانوتن‬
                 ‫که در زیربغل جامه و می‬              ‫باشد ‏‪٩‬وآن‌یز؛ کوچکی‌استکه در میان‌آن‬
             ‫ویمعنیآینه زالو هم‌آمده امتا ‪۰‬‬          ‫بافته بسته باشند‬       ‫شم‬
                                                                             ‫رنیبا‬
                                                                                 ‫بسما‬
                                                                                    ‫ا ری‬
                                                                                       ‫حلقه‌ای از‬
‫ت بکسر دوخای تقطمدار‬     ‫حشت‬       ‫حشت‬
                                                    ‫وانگشت سبابة رادرآن حلقه کرده بجانب خسم‬
                                                     ‫انداز ند‪ - ۴‬ونام نك دوازدهم است از جمله‬
‫وسکون دوشین و تای قرشت » صدای ورق‌کاغذ‬
                                                      ‫و سك کتاب‪ .‬زند پوازند (ی‪۱‬ع)نی‬‫يتك‬ ‫بيس‬
‫ر جامه که نو پوشیده باشند‪.‬‬‫زمهیو‬
                              ‫وصدای جا‬
  ‫شیت‬
    ‫قتحررا‬
         ‫اول وف‬          ‫کهسدر‬
                             ‫بتر‬
                               ‫خش‬                    ‫بك قىم ازجملابیست وبك‌فم‪,‬چه نك بمعنی‬
                                                    ‫قم باشد ‪ - ۴‬و نوعی از حلوا هم هت که‬
                                                     ‫در مشکها و جاها ریزند نابك پارچه وقرص‬
‫پارچة چهار كوشة زبر بغل جامه و زبر جامه‬                                                               ‫دود‬

                             ‫وشلوار باشد ‪. ۸‬‬
                                                    ‫خشت تابه ه بافوقالی بالف کشد‪.‬‬
‫خشت رر د خشت ر رین کنابه‬                            ‫فوتح بای ابجد ‪ .‬کوره و داش خشت یزی را‬
                                                                                                  ‫‪۳۱‬‬
‫جفتلث = مصغر خشت است ‪ -‬وبارچة‬                        ‫خشتامی ‪ -‬بفتح اول بروزن تردامن »‬
‫مربع زیر بغل جامه ومیان تنبان وشلوار را لیز‬           ‫و سم اول نیز درست‬         ‫مادر زن رگاونند‬
       ‫عنته‌اسه‬
              ‫کون وآیینه (‪ )۲‬زائو را مک‬                                                         ‫ات ‪. ۴‬‬

‫کابه از آقاب‬              ‫خشتك رر‬                    ‫حشتچه » بکر اول وفتح جیم‌فارسی‪.‬‬
                               ‫‪۰‬‬   ‫عالمتاب ست‬        ‫ه باشد‬    ‫شر‬ ‫و‌چها‬
                                                                      ‫گه‌ای‬
                                                                          ‫خشتك رگاونند ؛وآن پارچ‬

                               ‫(‪)۲‬اچك‪ .‬چش‪ :‬مئه ‪۰‬‬                 ‫(‪ )۱‬چك ‪ :‬ژند ویاژند ‪.‬‬
  ‫‪ - ۱‬هندی باستانی ‪( 1۵5۲‬یزه) » قی‪ :‬اوستا ‪ -‬ئ‪ » 5۲3‬بارسی‌باستان یز لاتا‪.578‬‬
                                         ‫ص ‪۷٩‬‏ *‪.‬‬        ‫سنا‬      ‫بهلوی] ‪٠ 015۳2‬‏ ارمنی ع ‪yaeth‬‏‬
                                         ‫‪ - ۴‬وقت محر که کلنك تسبه ای ساخته است‬
             ‫هند تا خزران تاخثه است‬       ‫یای‬
                                            ‫ودزرل‬
           ‫است‪...‬‬
                ‫‌شت‬
                  ‫تسته»خ‬
                       ‫خ‌ا‬
                         ‫افته‬
                            ‫نردو کو‬
                                  ‫بل‌ف‬
                                     ‫طم‬                  ‫می سیه‌برففاش تيغ برون‌آخته امت‬
  ‫«منوچهری داحقاتی ‪.*۷4۱‬‬
  ‫ی مزدسنا‬    ‫است‬   ‫یا ‪dãdartiC‬‏‬   ‫‪tãûdartiC‬‏‬   ‫دات‬    ‫دوازدهم اوستا چىىرە‬    ‫نام سك‬   ‫ك‬   ‫‪۳‬‬
```


## [2026-09-04T18:54:04.273Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD grep athir\"; grep -n \"أثير\\|اثير\\|الأثير\" TAD_pages.txt | head -20\necho \"=== TAD leaf0-2\"; awk 'BEGIN{RS=\"\\f\"} NR<=3' TAD_pages.txt | head -60",
 "description": "Grep TAD for athir"
}
```


### [2026-09-04T18:54:05.769Z] TOOL RESULT

```
=== TAD grep athir
143:‫اثير ب‪-‬وناني انه ومطنانه احترق ولمع واهلوعقنددماء أعلىجهة‬
146:‫المحسوسة غاطدة فها ويحتمل أينكون هذا الاثير عل الماذبية أيضأ أما فيعل‬
2958:‫قال ابن الاثير ‪ :‬ان لاخلرمخنار لامها مخمر العقل أي تستره ‪ .‬قلت الخر‬
=== TAD leaf0-2
                                     ‫الف‬
           ‫ياكابىاللبناك‬  ‫‪َ8‬‬
                       ‫نببى‬




       ‫لحتل‬
    ‫‪ -‬اا لدم‬  ‫‪1‬‬             ‫تت‬             ‫‪7‬‬   ‫‪:‬‬
     ‫امون‬
‫ظ‬     ‫‪1‬‬



      ‫هني بنشره وتصحيحه وتعليق <واشيه‬
                            ‫ا‬


           ‫الو مان‬
              ‫دام‬    ‫ده ل‬




                    ‫« طبعة ثانية ‪6‬‬




                    ‫حل '‬

                    ‫ذكرى الذ ممردص‬
 ‫الى الكير بروحه ونكرة‬        ‫الى من حك العلويغاد على الاادب‬

 ‫وقلبه ؛ الى من حب اطق وشرف الحق ولا نخاف فسيبيل المقلومةلاتم‬
                                  ‫والى الصديق الصادق فىكرم انلساانية‬


                  ‫عابلممل ي بنابت اباظ‬
                         ‫اهدي هذا الكتاب‬

               ‫المخلص‬

       ‫امم تيووسبا السسّافى‬
           ‫صاحب مكتية العرب‬                     ‫مصر فى ‪ 737‬أبريل ‪#‬اسرة !ا‬




‫عر خح‪-‬‬
                      ‫مكتية نرجس ]‪21‬م‬
                                                            ‫‪5‬‬         ‫سيور‬




                  ‫زات ‪١١‬‏ ‪/ .‬الانانانالا‬   ‫‪5‬ع‬   ‫أهمره نماط ‪.‬لالد اط‬          ‫‪76‬‬
‫ات ا‬

                                       ‫‪0‬‬
```


## [2026-09-04T18:54:09.702Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'اثير' in p and 'وناني' in p:\n        print('leaf',i)\n        print(p[:1500])\nEOF",
 "description": "Print TAD page containing athir"
}
```


### [2026-09-04T18:54:11.449Z] TOOL RESULT

```
leaf 4
                                                                       ‫‪0‬‬
                ‫لفل ونان قلطء دمع معنأه ولابة الاسقف ورعمته‬            ‫‪١‬‬

                          ‫معناه الذهب الخالص‬    ‫‪ 3‬اوناني‪80210‬‬       ‫‪2‬‬

                                ‫برشيم‪ 6‬معناءالخرير‬   ‫‪1‬ريسم ‪--‬فارمي ‪0‬‬


                              ‫‪ 2‬بق ‪ -‬فارسى « اتريز ‪ 4‬معناه يصب الماء‬


         ‫‪ --‬فارمي وهو فتحة مربعةفيجوفها لسان تعلق بطرف الحزام‬      ‫دم‬

         ‫بلس ‪ -‬بناني ‪5‬هامطذتك معناه كذ"اب وكام وهو من امماء الثشيطان‬
     ‫ابنوس ‪ -‬فاليونانية ومدعاة وهو خشب اسود شديد الصلابة شجره ينبت‬
                          ‫افلهيند فيكون بالطبعاسمههندي‬
‫اثير ب‪-‬وناني انه ومطنانه احترق ولمع واهلوعقنددماء أعلىجهة‬
‫افليجو وأنتاها وألمعما وعندالشعراء الهواء والسماء وافليطعبليعيات بدل على‬
 ‫حالة شديدة الدقة ولكنها غاايلةعفٌيدد بزعمون انها ‪٠‬ننشرة‏ فايلكون والمادة‬
‫المحسوسة غاطدة فها ويحتمل أينكون هذا الاثير عل الماذبية أيضأ أما فيعل‬
 ‫|‬                                    ‫‪30‬‬             ‫تت‬   ‫‪0‬‬
 ‫الكتمياء فبراد بهمواد |ليةتطير وهارامحة ذكية وهى تستحضر بعزل الماء من‬
                                           ‫كمحمول‬
                                                ‫لمض‬
                                                  ‫احوا‬
                                                     ‫الكحول بأاونحاد ال‬
                         ‫معناه يزه الخلق وشر يف‬      ‫‪-‬نابي ‪56‬‬
                                                            ‫أثيل و‬

         
leaf 81
‫افسىه ‪ :‬البرهان يبان الحجة مالنبرهرهة وهي البيضاء‬  ‫سري‬
                                                     ‫أمخش‬
                                                        ‫قال الز‬
 ‫‪ 0‬اري كااشتق السلطان‪.‬هنالسليط لاضاءته ق‪.‬لت‪ :‬السلطان لأفرظامى‬   ‫‏‪١‬‬
‫وهو مشدق م ن «شاط» اناا‬            ‫شولطانا م»عناه المنساط أي ماعن ل‬

  ‫أكعان البيل بق توم ساف ماله أيهرك ‪ .‬قأت ‪5‬‬               ‫قال ابن در ‪1‬‬

‫أي حربة وهو مشتى‬       ‫ليوناني‪ 5018‬كريس وف العبرانية‪ 0‬ع‬              ‫ا‬


                                                  ‫من « رب »‪ 6‬أي راب‬
‫قال ابن الاثير ‪ :‬ان لاخلرمخنار لامها مخمر العقل أي تستره ‪ .‬قلت الخر‬
‫يران أي الخرد ستسيع بغرا‬
                       ‫فز‬‫لآفظرةاضة « وا »© وهوامقتقدياقل م‬
                                                   ‫أي جراء من لومبها الاجر‬

  ‫قندفمىته ‪ :‬الانبرذور ولعلالمتوج معنى لنفلة الانبرذور‬
                                                     ‫مدو‬
                                                       ‫قال اءن خل‬
 ‫قلت انبردور تعرسب ماهر مدنا اللاتتى ومعناه الآهر وهو مشتق من ‪056‬م‪22‬آأ‬

‫أمر بأمر وكان يطلق على أمر الميش وقد أطاقته العامة على المملك وعلى ملك‬
                                                            ‫المموك أيضًا‬
‫راسم‬   ‫قال الطعرى ف تأرضه ‪ :‬ان اسماسكتدر مر كلب من سمأمه هلاى‬

‫عدرة قال ا بالفارسية سندر ‪ .‬قلت ‪ :‬ان اسماسكندر لنظة ونانة معناها ناصر‬
                ‫‪1,‬ك رك‬          ‫ازجل وهو رك من انالك نصر ومن ‪5‬‬

 ‫قال السيوطي فى مزهره ‪ :‬أنجد هو زحطي ‪ .....‬ثمم
```


## [2026-09-04T18:54:21.938Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON_part1 اثیر\"; grep -n \"اثیر\" MON_part1.txt | head -10\necho \"=== MON adena v1 اثیر\"; grep -n \"اثیر\" incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -10\necho \"=== MON adena v1 اتر\"; grep -n \"^اتر\\|اتر (\" incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -10",
 "description": "Grep Moin for athir/eter"
}
```


### [2026-09-04T18:54:22.063Z] TOOL RESULT

```
=== MON_part1 اثیر
6778:نور از آن عبور می‌کند موجود است؛ اثیر. 
7178:اثیر: ده [معر .] (ا.) کر 5 آتش که بالای کر و 
7181:زمين را فرا گرفته است. اتر. چرخ اثیر: کرة 
44407:يا نانوایی؛ ج. تناثیر ( کم.) 
=== MON adena v1 اثیر
6778:نور از آن عبور می‌کند موجود است؛ اثیر. 
7178:اثیر: ده [معر .] (ا.) کر 5 آتش که بالای کر و 
7181:زمين را فرا گرفته است. اتر. چرخ اثیر: کرة 
44407:يا نانوایی؛ ج. تناثیر ( کم.) 
=== MON adena v1 اتر
1957:اترویین: 2017 (.) (بز.) شبه قلیابی 
1960:اتریاد. 0 (ا.) بکك دسته سر باز. 
6768:اتر. ۲ [معر ی و 
6784:اتراق: 5۲ ([تر - او تراق ] (.) توقف جند 
6787:اترج: سور می. تر نج فارسی] (ا.) (گیا.) 
12484:اتری که از تقطیر یکی از استات‌ها بدست 
25645:اتر حل می‌شود. حلال بسیار خوبی است 
93579:اتریطس. طین سجلات: (زه.) گل مسختوم
```


## [2026-09-04T18:54:24.719Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6760,6800p' MON_part1.txt\necho \"-----\"\nsed -n '7170,7190p' MON_part1.txt",
 "description": "Print Moin entries for اتر and اثیر"
}
```


### [2026-09-04T18:54:24.800Z] TOOL RESULT

```
اتحاف: 81 (ع.] (مصم.) تحفه دادن؛ 
هدبه فر ستادن» تحفه فرستادن. 

اتخاد؛ ۱۱۵22ه [غ.] (مسصم.) گرفتن» 
برگرفتن» فرا گرفتن. اتخاذ سند: استناد به 
قول طرف برای قولاندن ادعای خود. 

اتر. ۲ [معر ی و 
تقلید آنان اقوام شیک انز را نهعتهی تال 
و رقیق که قسمت فوقانی کرة ارض را فرا 
گرفته» اطلاق می‌کردند. (فز.) بخار رقیق و 
ماد سیال و سریع التسخیری است که قسمتی 
از فضای هت جو را اشغال کرده و در 
تمام اجسام نافذ است. دانشمندان فیزیکک 
آن را عامل انستقال نسور و حرارت و 
الکتر پسیته دانسته‌اند. دارای هیچ گونه وزنی 
نست و خلاء و همه محط‌های شفاف که 
نور از آن عبور می‌کند موجود است؛ اثیر. 
(شیم.) نمک فرار و سریع التسخبری است 
که از ترکیب وت معدنی یا آلی 
با الکل بدست می‌آید» اترسل. (شیم.) 
ماده‌ای که از گرفتن یک مولکول آب از دو 
مولکلول الکل حاصل شود؛ اتر اکسید. 
اتراق: 5۲ ([تر - او تراق ] (.) توقف جند 
روزه در سفری بجایی. 

اترج: سور می. تر نج فارسی] (ا.) (گیا.) 
ترنج» با 

اتساع: 3 [ع.] (مص‌ل.) فراخ شدن» 
کشاد شدن. (امسص.) فراخیء فراخاء 
کشادگی؛ سعه» وسع 
(مص‌ل.) (بز.) منسط شدن و باز شدن و 
گشوده شدن و حجیم شدن و فراخ شدن 
یکی از اعضاء (مثل معده پا رگ‌هاو با 
روده). نضصرت» نضارت. کثرت مال؛ ملکك. 
مکنت و تروت» وسعت. 

اتساق: بخعهاا» [ع.] (مص‌ل.) راست و 
تمام شدن. فراهم افتان: انتظام یافتن. 
-----
انناعشر: (پز.) اماس و التهاب و تورم 
اثناعشر به علت فونت و یا ضربه به علل 
ااعشری: -]252- موی [ع. ف.] 
دوازده امامی. 

اثنان" «2ووه [ع.] (.) در حالت رفعی. دو» 
دو مرد. روز دوسنه. 

اثیر: ده [معر .] (ا.) کر 5 آتش که بالای کر و 
هوا است» سایلی رقبق و تنکك و بی‌وزن که 
طبق عقبده قدما فضای بالای هوای کرة 
زمين را فرا گرفته است. اتر. چرخ اثیر: کرة 
آتش» فلکك تارنم ]تیا (فد.) به عقیدة 
بی‌وزن و قابل قبض و بسط که فضا را پر 
کرده و در همه اجسام نافذ است؛ اتر. 
ائیم: 2912 [ع.] (ص.) گناهکار؛ تسه کاره 
بر من بزهکار) بزه گر مدنب» مجرم » 
عاصی. دروغفگوی» دروغزن. (اخ.) لقب 
اب وجهل (اخ.) لقب یزد فرد پسر بهرام 
بادشاه ساسانی (در نرد عربت)» نزه کر 
بزهکار.
```


## [2026-09-04T18:54:44.542Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN azg\"; grep -n \"azg\\|azak\" HRN.txt | head -20\necho \"=== HUB azg\"; grep -n \"azg\\|azak\" HUB.txt | head -20\necho \"=== PHD azag/goat\"; grep -n \"azag\\|'goat'\\|goat\\.\" PHD.txt | head -10\necho \"=== NYB azak\"; grep -n \"azak\\|azag\" NYB_vol2_glossary.txt | head -10",
 "description": "Grep for azg/azak in Iranian dictionaries"
}
```


### [2026-09-04T18:54:44.665Z] TOOL RESULT

```
=== HRN azg
1833:aw. bäzu' *Ärm'; phlv. bäzüh^). bazak]masih^) (ZPGl.);
1999:aw. baesaza^ 'Arzenei, Arzt'; phlv. bBsazak (PPGl.),
8574:aw. mazga- 'Gehirn'; phlv. mazg; ai. majjdn- 'Mark*.
8576:(174); bei. mazg (229); sar. muig 'Knochenmark', da-
10208:42. azg (d. i. azak) 'Ziege (PPÖl.).
11010:182. spaxff *verleumderisch', spazgth 'Verleumdung' (Men.,
11012:aw. spazga- (yt. 3, 8, 11, 15), Bedeutung unsicher.
11347:^"VW-yazaklh; vergl. dev]ya8n.
14857:dazgaiiiti- 70,
=== HUB azg
3542:Afgh. nazuk (mit u) bei Raver ty; nazaka, nenzdka f.
7973:'Gehirn' = zd. mazga-, ksl. mozgu, idg. mazg'^ho^.
8119:*) Vgl. auoh i in vazun = vazgun, bSzgun u. s. w. Verkehrt* aus
8854:dagegen kann mayz 'Gehirn' = zd. mazga- nicht auf ap.
8855:^mazya- zuriickgefiihrt werden. Wurde schon ap. mazga-
9552:g) Ap. zg = np. yz: mayz 'Gehirn* = zd. mazga-.
=== PHD azag/goat
256:bayaspānļīh: mission, embassy. ~ig [-yk'] post-(horse). Бах [Pc | N ~] hawk, falcon. bāzā [b’c’y | (N bāzū)] arm. ~banag [-p'nk'] arm-guard, brassard. bazaģ [bck' | М beg, N ~a] sin, evil. —ih: = bazag. bazakkar [bckkl | M bzkr] sinful, sinner. bāzā-zanišnīh [by znfnyh = Av. bázu.jata-] a degree of sin. bazišn [dcšn'] division, part. bazm [bzm | — M, N —] meal, feast. ~-awurd [-zolt! | N ~] a sort of canapé. 1bë [BRA < A br | MP] but; out; ~... (enya), except. ~...enya...né: except... (otherwise)... not. ~ az: without. m 2be [BRA | M P, N bi-] particle with verbs, with 6, of indefinable function. -bed [-pt' | M -byd, N -balilud] suffix, -lord, -master. bēdom [bytwm | M bydwm] furthermost. béganag [byk’nk' | N ~a] strange; stranger. bégar [byk”/ | N ~] corvée, forced labour. béh [byh | N bih] quince. bel [by] | (M. Бу), N ~] spade. bélür [bylwl | M bylwr, N bilür] crystal. bérón [bylwn' | M byrwn, N bérün] outside. bëš [bys] pain, sorrow; harm, hostility. — burdan: bear hostility. bēš-, —i&n, v. bištan. bēšāz [byš(*)z] healing, medicinal. bēšāz(ēn)- [by?z(yn)-, byf?)c(yn)- | M byP?z-] heal, cure. —išnih: healing. bēš-burdār [byšbwlť’[] hostile. bëšidan [bysytn'] = bištan, bēšūmand [byš?*wmnd] sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [byths] viceroy. *bifagàn [bch'n!] medicinal. bim [bym | = M, N ~] fear, terror. ~gén [-kn'] fearful, terrible. ~génih: fearfulness. --6mand [-'wmnd] fearful. *bistag [bstk! | N busta] hazelnut. biš [byf | N —] aconite. bištan, bé&- [bys-in' | M by$t, bys-] hurt, torment. ~išn: harm, torment. bize&k [dešk! | M bzyšk, N pizišk] doctor, physician.
292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
1003:biting (a.) gazag.
1816:evil (n.) ak, anāgīh, bazag(ih), dušīh, petyárag, wad(ag)ih, wat- tarih; onslaught of ~ ébgat(ih), petyāragīh.
1959:fitness sazišn, sazagih; v. suitability.
1960:fitting abāyišnīg, niyābag, passazag, sazāg(wār); be ~ abāyistan, saz-.
2760:measure (n.) handazag, payman(ag); (time, length) hās*r, v. Appendix (vii); grain — griw, kabiz.
=== NYB azak
965:bazak [bck'] misdeed, crime 6817. 73° etc. — MPrthPrs bzg ‘evil, wicked’; Paz. baza, baža, bažaa (SGV); v. Bailey, BSOS VII, 1933, 85.
966:bazak-kar [bckly] evil-doer 1285. - MPrthPrs bzkr; Paz. bažagar (SGV). Cf also s. v. davr.
1141:..ma... 708; pat —-ic cārak...nē... 792; —-ic āštēh 78% (interrogation). 796 (... n& ...); —-ic bazak ... nē... 809; ~-tc ... nē... in no way 34?!.
1448:éraxtan ['dlhtn'] to inflict damage, or loss; (as a legal term) to condemn, to convict: tur éraxt hénd the Turs were condemned, they lost the case 4513; — [pres. črang-: äyözend 6 bazak, marnjēnd gehän, érangénd they are intent upon sin, they destroy the world, they inflict dam-
1975:hazar [LP, with a P resembling the OAram. and Palmyr. forms of it; for Aram ’LP] thousand, — Av. (1796) hazagra- < *ha- zahra-, Skr sahasra-.
2299:kirpak [krpk'] virtue, pious duty (duties) imposed on the faithful by the Zoroastrian religion, or regarded as religiously meri- torious in general: 6419. 6714, 6921, 7924, 8313; opp. vinds 6313-14 etc.; opp. bazak 80°; enumeration of the principal virtues 8319-855; — kür w ~ exercise of virtue 6416 etc. passim; of pious institutions 13°; varz i ~ practicing virtue 66°; pātdāšn 4 ~ reward of virtue 8019, ~ mizd id. 8018; — ~ u ahlāyēh 066197209; m u vēhēh u rästeh 78. — MPrthPrs kyrbg
2555:micak [mck'] taste, flavour 891°. 10022, 10416-20 — Paz. miža; NP mazak.
3689:tacitan [teytn'] to run: api-m cand 4 nem roc pat pušt hamé tacit hom (for tacit-om) almost half a day (he was run after by me =) I ran after him 311? (cf s. v. kar- tan); be tacit pat oš han mat *cautiously (v. s. v. 68) his mother ran to him 48?9, 217.49 5019; pčš tacit ran before, got ahead (of the others) 494-19, — Av. (624) tak-; M Prth tc-; MPrs čz- (S); Paz. 0ajü for tazak (tajäk; Aog. 77); Verbum 169; Ghilain 50. Cf täxtan.
4162:vinäs [wns] sin, passim; ~ u bazak 68". 7419; ~ 2 andar dast u päd sins in which hand and feet are involved 6519-29; opp. kirpak 6313.24, 7925, 810, — NW form, Arm. lw. vnas; MPrs w(y)n’h (S, A-H I); Paz. NP gunäh; Arab. lw. junäh-.
5587:bzg: bazak
```


## [2026-09-04T18:54:53.462Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"42. azg\")\nprint('leaf',t[:i].count('\\f'), 'printed', t[:i].count('\\f')-21)\np=t.split('\\f')[t[:i].count('\\f')]\nprint(p[:1500])\nEOF",
 "description": "Print Horn page with azg"
}
```


### [2026-09-04T18:54:55.146Z] TOOL RESULT

```
leaf 290 printed 269
— 2f)9 —
42. azg (d. i. azak) 'Ziege (PPÖl.).
ai. ajd' *Bock , ajd- 'Ziege' ; lit. osys, lett. aßs *Ziegen-
bock*, ozMi *Ziege'. Dazu wohl auch arm. aic (H. No. 16),
gr. al^ und aw. iza^na- 'aus (Ziegen)fell- (?) , ledern
(vergl. ai. ajina- 'Fell'; wa/. ijWj sar. Jein *Filz ; ksl.
a^rwo Teir) 0-
43. «j? 'Schlange'.
aw. aSi' (vergl. oben unter No. 76). Im Np. nur
in ezdehä erhalten.
B.
44. hag 'Teil, Anteil' (M^n.), arm. LW. hacj 'Anteil, Erbe'.
aw. baya- 'Teil, Anteil' neben häga (oben No. 169).
45. hay 'öott'.
ap. haga- 'Wott'; aw. haya-x ai. hhäffha-; ksl. hogn
'Gott'.
46. hwftan 'schenken', vergl. np. leystdev (oben No. 186).
47. hayf mit Hülsen versehen (Getreidekörner)', ^h-ba/f
(vd. 7 (93)).
aw. ba/ta-, aba/ta- 'mit Hülsen, ohne Hülsen'.
Np. be/te alles, dem die Haut abgezogen ist', ist
nicht belegt^).
Für die Bedeutung 'dreijähriges Kalb' werden im
FR und FJ folgende Verse citirt:
(Metrum: Muzäri').
bäZ'l türä kt säh't tuyür esf cnn 'üqäh
ez gö8^fend"l be/te-ye efftW nrnstV (FJ: yeste) bäd
E;KSiketT
(Metrum: BesTt).
cun^) gurg^ bäs^ kl rind ufted fmyän-% r^me
ci meS-l berri bedendänes dt be/te ve säk
HekTm SözenT.
^) Die übrigens köstUohe Polemik von Bradke^s, Methode S. 174 ff.
geht bezüglich iza^nu- wohl über das Ziel hinaus.
*) Im FR soll der mitgeteilte Vers E;^slketl'8 liierher gehören.
*) Corrigirt statt cfi.
```


## [2026-09-04T18:55:11.932Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN aegis/aego\"; grep -n \"^aego-\\|^aegis\\|^Aegis\" KLN_1966.txt | head\necho \"=== KLN anneal\"; grep -n \"^anneal\" KLN_1966.txt | head\necho \"=== KLN estuary\"; grep -n \"^estuary\\|^estuar\" KLN_1966.txt | head\necho \"=== KLN ether\"; grep -n \"^ether,\" KLN_1966.txt | head",
 "description": "Grep Klein 1966"
}
```


### [2026-09-04T18:55:12.055Z] TOOL RESULT

```
=== KLN aegis/aego
1778:aegis,  egis,  n.,  1)  shield  used  by  Zeus,  later  by Pallas  Athene  (Greek  mythol.) ;  2)  used  figura¬ tively  in  the  sense  of  protection.  —  L.  aegis,  fr. Gk.  <xlyk,  ‘goatskin;  the  skin  shield  of  Zeus’, fr.  all,  gen.  odyo;,  ‘goat’;  see  aego-.  For  this etymology,  suggested  already  by  Herodotus,  see Frisk,  GEW.,  I,  p.  32  s.v.  xtyi;.  Cp.  Aegeus. Cp.  also  Giles.
1779:Aegisthus,  n„  the  lover  of  Clytemnestra,  with whom  he  killed  her  husband  Agamemnon (Greek  mythol.)  —  L.,  fr.  Gk.  AEyioOcx;,  a  word of  uncertain  origin.
1782:aego-,  combining  form  meaning  ‘goat’.  —  Gk. alyo-,  fr.  xiEi,  gen.  xlyoc,  ‘goat’,  which  is  cogn. with  OI.  ajah,  ‘he-goat’,  ajinam,  ‘skin’,  Avestic tzaen'm,  ‘pertaining  to  skin’,  Arm.  aic,  ‘goat’, Lith.  ozys,  ‘he-goat’.  Cp.  the  first  element  in aegicrania.
=== KLN anneal
2842:anneal,  tr.  v.,  to  temper  by  heat;  to  temper.  — ME.  anelen ,  fr.  OE.  anselan,  ‘to  burn,  kindle’, fr.  an,  ‘on  (see  a-  ‘on’),  and  shin,  ‘to  kindle, bum’,  which  is  rel.  to  OE.  al,  ‘fire’,  sled,  ‘fire, firebrand’.  ME.  anelen  and  E.  anneal  were  in¬ fluenced  in  form  by  an  erroneous  association with  OF.  neeler  (whence  F.  nieller),  fr.  VL.  *ni- gelldre,  ‘to  blacken’,  fr.  L.  nigellus,  dimin.  of niger,  ‘black’.
=== KLN estuary
13703:estuary,  n.,  broad  mouth  of  a  river.  — -  L.  aestu- arium,  ‘a  tideplace,  an  estuary’,  fr.  aestus,  ‘heat, fire,  the  ebb  and  flow  of  the  sea,  tide’,  rel.  to aestus,  ‘heat’.  See  estival, esurience,  esuriency,  n.  —  Formed  fr.  next  word with  suff.  -ce,  resp.  -cy.
=== KLN ether
13719:ether,  also  aether,  n.,  i)  the  upper  regions  of space;  2)  (chem.),  a  colorless  liquid  used  as  an anesthetic.  —  L.  aether,  fr.  Gk.  aUHjp,  ‘the upper,  purer  air,  ether’,  which,  together  with
```


## [2026-09-04T18:55:24.483Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '13719,13722p' KLN_1966.txt\necho \"=== leaf/page calc\"\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor key in ['aego-,  combining','aegis,  egis','anneal,  tr.','estuary,  n.','ether,  also  aether']:\n    i=t.find(key)\n    leaf=t[:i].count('\\f')\n    print(key[:12], 'leaf',leaf, 'approx printed', 2*(leaf-12), '-', 2*(leaf-12)+1)\nEOF",
 "description": "Klein ether entry and page estimates"
}
```


### [2026-09-04T18:55:26.296Z] TOOL RESULT

```
ether,  also  aether,  n.,  i)  the  upper  regions  of space;  2)  (chem.),  a  colorless  liquid  used  as  an anesthetic.  —  L.  aether,  fr.  Gk.  aUHjp,  ‘the upper,  purer  air,  ether’,  which,  together  with
aftfpa,  ‘the  clean  sky,  fair  weather’,  derives  fr. a(8-£tv,  ‘to  bum’,  fr.  I.-E.  base  *aidh-,  ‘to  bum’, whence  also  L.  aedes,  ‘a  building,  sanctuary, temple’.  See  edify  and  words  there  referred  to and  cp.  esp.  Aethusa,  Ethiop;  cp.  also  hypae- thral.  As  a  chemical  term,  the  word  aether  was coined  by  August  Sigmund  Frobenius  (in  1730), the  discoverer  of  this  liquid.
ethereal,  adj.  —  Formed  with  adj.  suff.  -al  fr. L.  aethereus,  fr.  Gk.  ai&Epio?,  ‘pertaining  to ether’,  fr.  <xUW]p.  See  prec.  word.
Derivatives:  ethereal-ity,  n.,  ethereat-ize,  tr.  v., ethereal-iz-ation,  n.,  ethereal-ly,  adv.,  ethereal¬ ness,  n.
=== leaf/page calc
aego-,  comb leaf 28 approx printed 32 - 33
aegis,  egis leaf 28 approx printed 32 - 33
anneal,  tr. leaf 53 approx printed 82 - 83
estuary,  n. leaf 296 approx printed 568 - 569
ether,  also leaf 297 approx printed 570 - 571
```


## [2026-09-04T18:55:50.528Z] TOOL CALL #42: Bash

```json
{
 "command": "ls data/ && ls data/extracted | head && find . -maxdepth 3 -iname \"*.pdf\" | head -20",
 "description": "Look for source PDF of Nourai"
}
```


### [2026-09-04T18:55:50.590Z] TOOL RESULT

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
./EtymologicalDictionary-persian-english.pdf
```


## [2026-09-04T18:55:50.632Z] TOOL CALL #43: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T18:55:50.638Z] TOOL RESULT

```


```


## [2026-09-04T18:55:57.032Z] TOOL CALL #44: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p39 && pdftoppm -f 39 -l 39 -r 200 -png EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p39/page && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p39/",
 "description": "Render page 39 of the source PDF"
}
```


### [2026-09-04T18:55:59.440Z] TOOL RESULT

```
total 88
drwxrwxr-x  2 sfmqrb sfmqrb  4096 Sep  4 14:55 .
drwx------ 13 sfmqrb sfmqrb  4096 Sep  4 14:55 ..
-rw-rw-r--  1 sfmqrb sfmqrb 78497 Sep  4 14:55 page-039.png
```


## [2026-09-04T18:56:01.614Z] TOOL CALL #45: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p39/page-039.png"
}
```


### [2026-09-04T18:56:01.961Z] TOOL RESULT

```

```


## [2026-09-04T18:56:01.957Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-04T18:56:19.939Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p39 && pdftoppm -f 39 -l 39 -r 600 -png /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('hi-039.png'); print(im.size)\nw,h=im.size\n# eter box approx at x 0.63-0.78, y 0.42-0.46 of page\nim.crop((int(0.60*w),int(0.415*h),int(0.80*w),int(0.462*h))).save('eter.png')\nim.crop((int(0.55*w),int(0.62*h),int(0.80*w),int(0.68*h))).save('azg.png')\n\"; ls",
 "description": "Crop eter box at high resolution"
}
```


### [2026-09-04T18:56:25.593Z] TOOL RESULT

```
(5100, 6600)
azg.png
eter.png
hi-039.png
page-039.png
```


## [2026-09-04T18:56:28.425Z] TOOL CALL #47: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p39/eter.png"
}
```


### [2026-09-04T18:56:28.441Z] TOOL RESULT

```

```


## [2026-09-04T18:56:36.534Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82eyd%CA%B0-",
 "prompt": "Give the reconstructed root, its meaning, the derived terms listed (especially Avestan, Greek, Latin, Germanic/Old English), and any note on Pokorny page."
}
```


## [2026-09-04T18:56:38.266Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%87%DB%8C%D8%B2%D9%85",
 "prompt": "Give the Persian entry هیزم: etymology (Middle Persian, Avestan, Proto-Iranian, PIE forms cited), meaning, and any references (Hasandust, MacKenzie, Horn)."
}
```


### [2026-09-04T18:56:43.159Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂eydʰ-

**Reconstructed Root:** *h₂eydʰ-

**Meanings:** "to ignite" and "fire"

## Key Derived Terms

**Avestan:** aēsma ("firewood")

**Ancient Greek:** aíthō (αἴθω, "to burn"); aithḗr (αἰθήρ, "ether")

**Latin:** aedēs ("building/temple"); aestās ("summer"); aestus ("heat/tide")

**Proto-Germanic:** *aidaz (ancestor of English terms); *ailą

**Sanskrit:** édhate (एधते, "burns"); édha (एध, "firewood")

## Notable Etymology

The root possibly derives from a compound meaning "to put to fire," combining *h₂ey- ("fire") with the suffix *-dʰ(h₁)- ("to put, set").

## Additional Note

The page references multiple etymological dictionaries including works by Kroonen (Proto-Germanic), Rix (Indo-European Verbs), and De Vaan (Latin and Italic languages), though specific Pokorny page numbers aren't provided in this source.
```


### [2026-09-04T18:56:44.302Z] TOOL RESULT

```
# Persian Entry: هیزم (hēzum/hizom)

## Meaning
The word means "firewood," with a synonym being هیمه (heyme).

## Etymology
According to the Wiktionary source, هیزم derives from Middle Persian 𐭰𐭩𐭡𐭠 (CYBA /⁠ēzm⁠/), which ultimately traces back to Proto-Indo-European *h₂eydʰ- meaning "to burn; fire." The entry also notes a comparison with Talysh ایزم (izəm).

## References
The page cites Hayyim, Sulayman's *New Persian–English dictionary* (1934, Teheran: Librairie-imprimerie Béroukhim, pages V2-1220) as a reference source.

The entry does not provide specific Avestan or Proto-Iranian forms, nor does it reference scholars like Hasandust, MacKenzie, or Horn in the visible content.
```


## [2026-09-04T18:56:47.899Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%B4%D8%AA",
 "prompt": "Give the Persian entry خشت: etymology (Middle Persian, Old Persian, Avestan, Sanskrit forms cited), meaning 'brick', and references."
}
```


## [2026-09-04T18:56:48.246Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/estuary",
 "prompt": "Give the etymology of estuary, including Latin aestuarium and aestus, and the PIE root cited."
}
```


### [2026-09-04T18:56:54.102Z] TOOL RESULT

```
# Etymology of Estuary

**Origin:** The word estuary entered English in the 1530s from Latin *aestuarium*, meaning "a tidal marsh" or "channel inland from the sea."

**Latin Foundation:** The Latin term derives from *aestus*, which signifies "boiling (of the sea), tide, heat."

**PIE Root:** Both Latin terms trace back to the Proto-Indo-European root *\*aidh-*, meaning "to burn." This ancient root also gave rise to the word "edifice," as the etymology notes that the same root underlies multiple words referring to fire and burning across various Indo-European languages.
```


### [2026-09-04T18:56:55.110Z] TOOL RESULT

```
# Persian Entry: خشت

## Etymology

The Persian خشت (xišt/xešt) derives from **Middle Persian** hšt' (/xišt/, "brick"), which came from **Old Persian** 𐎡𐏁𐎫𐎡 (i-š-t-i /išti-/, "sun-dried brick"). Scholars suggest this may have been "borrowed from the BMAC substrate."

Related cognates include:
- **Avestan**: ištiia, išti, and zəmōištuua (meaning brick or clay brick)
- **Sanskrit**: इष्टका (iṣṭakā, "brick")
- **Tocharian B**: iścem ("clay")
- **Pashto**: خښته (xaś̱tah)

## Primary Meanings

1. Adobe or sun-dried brick
2. Tile or slab
3. (Uncommon) A loaf baked for the soul of a deceased person
4. (Zoroastrianism) The twelfth chapter of the Zend

## References

The etymological information cites Alexander Lubotsky (1999) and Rüdiger Schmitt (2018) regarding Indo-Iranian substrate origins and lexical reconstruction (*išta-, *išti- 'brick').
```


## [2026-09-04T18:57:16.307Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B1%E1%BC%B4%CE%BE",
 "prompt": "Ancient Greek αἴξ: give the etymology section verbatim in substance — what origin is proposed (Pre-Greek? Beekes?), what cognates (Armenian ayc, Avestan izaēna-, Sanskrit ajá-) and which PIE reconstruction is given."
}
```


## [2026-09-04T18:57:16.743Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/anneal",
 "prompt": "Give the etymology of anneal: Old English forms, the element meaning 'fire', and the PIE root cited."
}
```


### [2026-09-04T18:57:22.218Z] TOOL RESULT

```
# Etymology of Ancient Greek αἴξ (aíx)

Based on the Wiktionary entry, here's the etymology section:

**Origin proposed:** The word derives from Proto-Hellenic *aíks, which comes from Proto-Indo-European *h₂eyǵ- meaning "goat."

**Cognates listed:**
- Old Armenian այծ (ayc)
- Sanskrit एड (eḍa)
- Albanian dhi

**PIE reconstruction:** The entry states the word comes from "Proto-Indo-European _[*h₂eyǵ-](/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ey%C7%B5- 'Reconstruction:Proto-Indo-European/h₂eyǵ-')_ ('goat')."

**Note on sources:** The etymological information is sourced to Beekes, Robert S. P. (2010), *Etymological Dictionary of Greek*, published by Brill.

The entry does not propose a Pre-Greek origin; rather, it traces the word to established Indo-European ancestry through Proto-Hellenic and Proto-Indo-European reconstructions.
```


### [2026-09-04T18:57:23.125Z] TOOL RESULT

```
# Etymology of Anneal

**Old English Form:**
The word derives from Old English *onælan*, meaning "to set on fire, kindle; inspire, incite."

**Fire Element:**
The element meaning fire is *ælan*, which comes from Proto-Germanic *\*ailan*. Related forms include Old English *æled* "fire, firebrand," Old Norse *eldr*, and Danish *ild* "fire."

**PIE Root:**
The ultimate source is a Proto-Indo-European root meaning "to burn," which also gave rise to the word "ash." The text notes this root as "*as-* 'to burn, glow.'"

**Sense Development:**
By late Old English, the term had already acquired its technical meaning: "to treat by heating and gradually cooling" materials like glass, earthenware, and metals to strengthen them.
```


## [2026-09-04T18:57:34.765Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D8%AB%D9%8A%D8%B1",
 "prompt": "Arabic أثير: is there a sense 'ether/aether' and is it said to be borrowed from Ancient Greek αἰθήρ? Quote the etymology."
}
```


## [2026-09-04T18:57:35.943Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ey%C7%B5-",
 "prompt": "Give the reconstruction *h₂eyǵ- 'goat': its descendants (Greek, Armenian, Avestan, Sanskrit) and any note distinguishing it from *h₂eǵ- 'goat'. Also list what Iranian forms are given if any."
}
```


### [2026-09-04T18:57:39.094Z] TOOL RESULT

```
# Etymology of أثير (Ether)

Yes, the Arabic word أثير does have the sense of "ether" and is indeed said to derive from Ancient Greek.

**Etymology Quote:**
"Phono-semantic matching of Ancient Greek αἰθήρ (aithḗr, 'upper air')."

The entry indicates this is a phono-semantic matching—a linguistic borrowing that adapts both sound and meaning—rather than a direct etymological derivation. The noun أَثِير (ʔaṯīr) is listed as masculine and defined as "air, ether," with its formation traced to the Greek term through this sound-and-meaning correspondence method.
```


### [2026-09-04T18:57:41.700Z] TOOL RESULT

```
# Proto-Indo-European *h₂eyǵ- 'Goat'

## Descendants

**Greek:** Proto-Hellenic *aíks ("goat")

**Armenian:** Old Armenian այծ (ayc)

**Sanskrit:** इज्जल (ijjala)

**Avestan:** 𐬍𐬰𐬀𐬉𐬥𐬀 (īzaēna, "leathern")

## Distinguishing Note

The page lists *h₂eyǵ-* as a homonymic root with two separate etymologies. Etymology 1 denotes the animal (goat), while Etymology 2 denotes "oak." The reconstruction notes for Etymology 2 indicate that "root nouns in Germanic are frequently of unexplained/substrate origin," suggesting these may represent distinct lexical items despite their identical form.

## Iranian Forms

Only one Iranian attestation appears: Avestan īzaēna, which shows a derivative meaning "leathern" rather than a direct animal designation.
```


## [2026-09-04T18:57:49.574Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82e%C7%B5-",
 "prompt": "Is there a Proto-Indo-European root *h₂eǵ- meaning 'goat'? List its descendants, especially Sanskrit ajá-, Lithuanian ožys, and any Iranian (Middle Persian azag, New Persian azg) forms."
}
```


## [2026-09-04T18:57:51.037Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%87%DB%8C%D9%85%D9%87",
 "prompt": "Persian هیمه: meaning and etymology — is it linked to هیزم / Avestan aēsma- / Middle Persian? Quote the etymology section."
}
```


### [2026-09-04T18:57:55.476Z] TOOL RESULT

```
Based on the content provided, I cannot answer your question about the etymology of Persian هیمه or its potential links to هیزم, Avestan aēsma-, or Middle Persian. 

The page shown is for the Mazanderani word **هیمه** (hêma), meaning "firewood," with pronunciation [heːmɐ]. There is **no etymology section** included in this Wiktionary entry. To find the etymological information you're seeking about the Persian cognate, you would need to visit the Persian Wiktionary entry, which is linked on this page.
```


### [2026-09-04T18:57:55.847Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂eǵ- (Goat)

Yes, the Wiktionary article confirms a second etymology for this root meaning "goat."

## Key Descendants

**Sanskrit:** The article lists "अज" (ajá, "driver") under Etymology 1, but for the goat meaning specifically, it documents "अजिन" (ajína, "skin of an animal, esp. goat").

**Lithuanian:** Under the goat etymology, descendants include "ožỹs" (masculine) and "ožkà" (feminine), along with "oženà" (goat-skin).

**Iranian forms:** The article does not mention Middle Persian *azag* or New Persian *azg*. However, it does reference Younger Avestan with a form meaning "wearing a skin," and notes Proto-Iranian descendants.

## Note on Etymology

The article suggests: "The alternation with *h₂eyǵ-* could suggest a substratum loan," indicating uncertainty about whether this root represents genuine Indo-European stock or borrowed material. This dual meaning—both "to drive" and "goat"—across different etymologies suggests these may be distinct roots coincidentally similar in form.
```


## [2026-09-04T18:58:16.957Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### SKT\"; grep -n -i \"^anneal\\|^estuary\\|^ether\\|^aegis\" SKT.txt | head\necho \"### LEW aestus\"; grep -n -i \"aestus\\|aestas\\|aether\" LEW_1910.txt | head -8\necho \"### LAT aestus\"; grep -n -i \"aestus\\|aether\" LAT.txt | head -8\necho \"### IEC aidh\"; grep -n \"aidh\\|aig-\" IEC.txt | head -10\necho \"### HUB xist\"; grep -n \"xišt\\|xist\\|hezum\\|hēzum\" HUB.txt | head -10\necho \"### NYB ezm/xist\"; grep -n -i \"ezm\\|xist\\|xišt\" NYB_vol2_glossary.txt | head -10",
 "description": "Batch grep secondary references"
}
```


### [2026-09-04T18:58:17.078Z] TOOL RESULT

```
### SKT
716:ANNEAl- «#t  pp.  of  ¥4fiirii  lo  turn
6014:Estuary,  mouih  of  n  tidal  riTcr.  (1..) L  trstuarium,  the  same.  *  L.  trituan^^  to »urgc,  foftm  as  the  tide.^I*.  «x/iu,  heal, surge,  title.     (VIDH.)
6017:Ether,  pure  upper  air.  (I...  — Gk.)  L. a//itr.  -  Gk.  al^p,  upper  air;  from  iu t'lt^wing  —  Gk.  a($ttv,  to  glow.    (^IDH.)
21842:Anneal  Perhaps  the  A.  S.  words  should be  pmklan  aud  ^Um^  with  long  dT.  Vet  sec l^'ick,  i.  loo.
### LEW aestus
### LAT aestus
1578:m aedo, non attest 4 , cf.gr.ai 9 w (en latin aestus, aestas) comme caedes
1606:eit "bfichqr", racine represent^e aussi en latin par aestas et aestus.
1746:en revanche, 1 'effort fait depuis Pacuvius pour latiniser aether n’a
1864:aestas, -atls f.; aestus, -us m. Cf. aedes. Aestas semble issu par
1869:1° aestas:-e te. - est pars anni, aestus calor [ temporis\. festus a
1874:3 ° aestus: chaleur brulante, provenant d'une substance enflammee,
1876:quin, si aestus malum est, et aestuare malum sit ? Sen., Ep.117,18.
1879:un liquide bouillant. Aussi aestus a-t-il designe 1 'agitation des flots
### IEC aidh
285:aidher-, aidhros, à “burning, bright; bright- ness’. WP I, 5. Cf. aidho Gk. aithér; aithros; aithra; cf. aithérios, adj.; Sequanian aidrini, adj. ‘bright: Gk. aithrinós “of early morning’; Alem. eter, adj. ‘clever, bright; Li. jedrà ‘measles’. Cf. aidhlos
286:aidhost-, see aidhst-
287:aidhlos, aidholos, om ‘burning; consump- tion’. WP I, 5. Cf. aidhó Oss. ird (adj. 'bright); Myc. (name) Aithalos; Gk. aíthalos, aithále ‘ashes, embers’; Alb. jézull ‘embers; MIr. ael, aol ‘quicklime’ (in mod. Ir. also ‘bright colour); Br. aoled, oaled, Vannic oeled; Cor. olas; OCor. oilet; W ael- wyd (all = *hearth") beside W aeled, m. "Drei: OS éld; OE ål; ON eldr ‘fire’; OE &led, obl. &ld, id.
288:aidhmos, aidhsmos ‘burning’. WP I, 5. Cf. aidho Skt. idhmáh; Av. aesmo; ON eimr; OE am; OHG cf. eimurja: ON eymyrja: OE zemyrie ‘embers’; Li. iesmas, iesme 'firing-charge'
289:aidhō (əidh-) ‘burn’. WP I, 5 Skt. idhé, v.; édhah, m.; Gk. aítho; MHG eiten; cf. Alb. eth *mate bull with heifer fr. *aidhsko
290:aidhos (oidh-) “fuel, fire, heat, passion”. WP . I, 5. Cf. aidho, aidhst- Skt. édhah; Gk. aithos, n., aithós, adj.; MIr.
297:áed, aodh ‘fire’, ide ‘torch’; Br. oaz ‘passion’, aézen ‘vapour’; OHG eit; OE ad Cf. Oss. ird *bright', fr. *aidhlos, *əidhros; Li. jedrà ‘measles’. Cf. also Li. aidinti ‘to tease’. Cf. OCS jadíno ‘burn, burning’.
298:aidhs-, cf. aidho, aidhos, etc. ON eisa; Li. cf. iesme ‘fuelling’; Latv. iesna “Inflammation, cold’. LG cf. aesel ‘charred wick, glowing wick”
299:aidhst- (aidhəst-, əidh-) “heat, burning, furnace, rage'. WP I, 5, cf. aidho, aidhos Av. istyo ‘brick’; Alb. ethe ‘fever’; Lat. aestus; aestas; MIr. áith ‘kiln’; Cor. eth ‘hearth’; eth ‘vapour’; OE ast; Du. eest ‘oast’; Lusatian jest ‘foam, cf. n-e&c ‘fireplace, ovenhole', cf. *en-aidhst-)
302:Gk. cf. krát-aigos, aig-eiros, aig-anée; OHG
### HUB xist
376:wort sein wird. Also existirt ostat gar nicht. Darme-
378:= zd. *aiwistditi-, aber ustad existirt nicht und *aiwi'
1159:urtheilen, existiert ein np. pad 'Schiitzer iiberhaupt
3378:Xocken'. — Syr. ges existirt nicht (Noldeke).
6167:= zd. baresma (np. barsam ist Parsenwort); hezum 'Brennholz
8438:hihist 'Paradies' == zd. vahista-; xist 'ZiegeF, skr. istako-;
9497:Dagegen stammt das h von hast 'ist, existirt', paz.
9512:aresa-, skr. rksa-; xist 'Ziegel', phi. oHst = zd.istya-; xism,
### NYB ezm/xist
78:"YT', "YTY (inser.): ’ITAY it exists, there is 'ZLWN-: "ZL to go
286:a-frac-saci8néh [’pr’c sešnyh] the quality of not passing away, continuance, con- tinued existence (of the family) 597°. — Av. (1554) pasca frasaxtahe mašyehe ‘after mankind has come to an end’, Vd. 1928, is rendered in Phl. by pas hac fräc-sacisneh i martömän, v. sacišneh.
417:heard as such a ''modesty pronoun" = I. — This pron. is, however, obsolete in BP, and the cas. obl. man (q. v.) is regu- larly used as the cas. rect. The Pazandists had lost all tradition regarding the equi- valent of the ideogr., which they trans- literate mechanically aomen (Mx, SGV), when occurring in the texts. It was omitted in most MSS of the FrP (want- ing in Junker’s text), but exists in Codd. P and S, though with misunderstood Ir. equivalents.
431:an-aryan [’n’ry’n] (Prth) non-Aryans HajA: 2. ŠPrth: 5.11, = Prs anörän. anäst ['n'st'] nothingness, that which is vain, worthless: dróv u ~ 83%. 8427. — Paz. anäst, Skr. v. nästikya (Mx), nästika (SGV); anahast ‘non existent’, Skr. v. asat, nāsti; anahasti ‘unreality, extinction’ (SGV, Aog.). From the neg. pref. and (v.s.v. anāvinast) + *hast; anāst < ana- hast with contraction seems to be the older form, anahast to be a recent for- mation.
468:"p: api-š, ”pm’n' or (Ps.) *pmn: api- man, ’pt’n': api-tän, "p$^n! or (Ps.) *pšn: api-ščin: 1. and, introducing and coordi- nating sentences, e.g. andar-rón andar šut api-$ guft 1818-14; coordinating substan- tives if the second subst. is determined by an encl. pron., e. g. zantšn + Ahriman api-š visütakän 8819; also preceded by u: u api-t 6°, u api-š 7822, u api-sdn 79°, etc. — 2. introducing the apodosis after ka 94. 1025, 5225-27, 5418; after cigon 931; after an isolated w. having the character of a protasis: hämöden api-š hàn zan... ayyāt būt all this [to supply: engaging his attention], the remembrance of that woman came upon him 11'!-!*; — taking up the sentence again after a preceding digression: han zan u hàn fradand 1-8... api-man ne özat 1212-3. — Av. (82 sg.) aipi, OP apiy ‘moreover, further’, both encl. and often only emphasizing: OP düraiy apiy (and other spellings) ‘very far’; surviving in Milr -p(?), g. v. Along with it there must have existed a fully stressed form "dpi; id.-europ. "dpi (Gr postp. Ézt, prep. èni), whence the gen- uine Arm. eu ‘and’; it is the counterpart of Gr ču, Lat et (eti-am). This "dpi > Milr ap, in the sense of ‘and’ and in the apodosis, is normally used in the Sassa- nian official language as the bearer of encl. pronouns beginning the sentence, but in fact occasionally occurs alone, as in the Ps. (several instances, v. Gloss.); PR 231.14, 347. 404; PhlY 31! (intro- ducing the apodosis). Apparently it was counted among the archaisms which need- ed explanation, because it was included in the FrP (ch. 24). Paz. has preserved some remnants of the archaic form: awam = api-m SGV VII, 22, awama = api-mān ibd. VI, 47. X, 28. 35; Paz. AV, ed. Antiā, Päz. texts 35818; hawasq = api- gan SGV V, 62, etc.; the Paz. forms reg- ularly occurring may be shortened allegro forms of api-m ete., v.s.v. u. The equi- valents of api-m etc. given by the FrP are wm, wt, wš, which seem to coincide
717:āstišnēh: mēnēi ~ existence at the heav- enly stage of development 3821; gētē m existence at the earthly stage of develop- ment 393-28; pas hac dam pat menči m after the existence of the creation at the heavenly stage (= after the creation had entered upon the heavenly existence) 3871-22; rai ~ ever-lastingness of splen- dour 5918,
819:axistan [hstn'; KDMWM-tn']  dzéz- Phyc-, KDMWN-] to stand up 1418. 3217. 33; apar ~ id. 233-74, passim; apde = to rise from the dead 105'7. — Ps. ^hstny hyc-; MPrs ’zystn ’xyz- (S, A-H I); < ā- + BP vistan [hstn'] x&- [hyc-];
821:MPrth ?a?štn "ayz- (S), cf KZSPrth 1. 9 wyhšt = vixišt, Gr. v. dopunsagev. Verbum 178; Ghilain 61. V. also v2st-üxez.
826:ax" ['hw] existence, life: ~ ti astomand the material, terrestrian world 378. 40! etc., passim. — Av. (106 sqq.) ahu-, anhu-; FrP, Cod. P fol. 7a with the Paz. reading axti and the NP gl. dunyā. Paz. common- ly óx. — Another ax“ v. patvast-axteh.
951:bavišn [YHWWN-šn'] v. n. of bütan: the act of entering into material existence; material existence 109° (opp. vindsišn). — Corresponds exactly to the Arab. philo- sophical term kaun (opp. fasdd), Gr yeveoic. Cf bütak.
```


## [2026-09-04T18:58:38.983Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\nfor ln in (6167,8438,9497,9512):\n    # find char offset of that line\n    off=sum(len(x)+1 for x in lines[:ln-1])\n    leaf=t[:off].count('\\f')\n    print('=== line',ln,'leaf',leaf)\n    print('\\n'.join(lines[ln-6:ln+6]))\n    print()\nEOF",
 "description": "Print Hübschmann contexts"
}
```


### [2026-09-04T18:58:40.634Z] TOOL RESULT

```
=== line 6167 leaf 184
fand statt zur Vermeidung iiberlanger Silben (auf kurzen
Vokal + drei Eonsonanten oder langen Vokal + zwei
Konsonanten, wenn der letzte Konsonant ein Nasal oder
eine Liquida ist) und zwar ist
§ 64. a) u eingeschoben in : phi. paz. barsum aus *barsm
= zd. baresma (np. barsam ist Parsenwort); hezum 'Brennholz
aus *ezm = ap. *aizma- = zd. a^sma- ; ustur 'Kameel' aus
*) Schon bei Ptolem. liandSarcc^ das trotzdem zu zd. &p. spaSa-
*Heer* gehoren wird.
*) Der Vorsohlag von a vor sx aus X8 (z, B. asx^ *roth' = zd.
xsapta-'y asxarh 'Land' = ap. xsa^^'a-) ist; armenisoh.- 175 -
^tistr = zd. ustra- ; vielleicht auch in abr^um *Seide* = phi.

=== line 8438 leaf 246
= np. st und s^:'
a) = s^ : mw6^^ Taust' = zd. rmdU-, arm. msrtfc 'Bundel*
= phi. "^mustik; angust 'Finger, Zehe' = zd. angusta";
ustur 'KameeV = zd. uistra--, pust 'Rucken* = zd. parsfi-,
skr. prstha-; mustan reiben, skr. mrsta-, Wrzl. m&t'g'^\
hihist 'Paradies' == zd. vahista-; xist 'ZiegeF, skr. istako-;
ristan *spinnen, pr. resam, Wrzl. reik^; nivistan 'schreiben*
= ap. nipistanaiy, pr. nuvesam, Wrzl. pdk^ ; histan 'lassen*,
skr. srsta-, Wrzl. serg^ ; hast ^) 'acht* = zd. asta, idg. okHOu ;
biristan 'braten' mit st aus skt von Wrzl. iran. brj und
bri^g = idg. bhrzg, oben p. 27.
b) = st: dost Treund' == ap. daustar-; §ast 'sechzig'

=== line 9497 leaf 275
Shk. 250, Min. Gl. 103 aus Oh (oder dAV) von phi. Ohrmazd
= ap. A{h)uramazda ; doch kann auch hier h vorgeschlagen
sein wie in den obigen Fallen. Denn der Kegel nach
(s. § 96, b) sollte ehrpat zu *erpaty Ohrmazd zu *ormazd (arm.
Ormizd, syr. Hormizd, gr. ' 0()iLuadag u. s.w. BB. 4, 67) werden.
Dagegen stammt das h von hast 'ist, existirt', paz.
hast *there is' Shk. 250, Min. Gl. 101 (neben ast *ist') aus
der 3. p. pi. niittelpers.*Aawrf = pSz. hend Shk. 250, Min. Gl. 102
'■= ap. hantiy (wahrend andrerseits Viand durch Anlehnung
an ast zu and wird), vgl. Horn Nr. 1094; das h von hast
acht' = zd. asta ist von haft *sieben', das h von hastad
achtzig* von haftod *siebzig' genommen.

=== line 9512 leaf 275
xastu *Kern* = xasta JRAS. 1894, p. 458 = asta, zd. ast-
*Knochen'; xaya *Ei* (mit h im Kurd., Afgh. und Bal.) =
paz. xdyay phi. xayak Shk. 254, Min. Gl. 125, gr. aJoV, lat.
Ovum\ xdm roh' (kurd. mit x, bal. mit h) = skr. ama-,
arm. hum; xirs 'Bar, phi. x(i)rs Bdh. 56, 14 und 17, zd.
aresa-, skr. rksa-; xist 'Ziegel', phi. oHst = zd.istya-; xism,
xasm 'Zorn , paz. xasm {xism) Min. Gl. 124, Shk. 254, phi.
xism Gl. and Ind. 68 = zd. aesma-; xEs, ka§. is, xis *Pflug*
= zd. aesa-; xurma 'Battel', paz. xurma Min. Gl. 128,
arm. armav (5. Jhd.).
Hier ist x schon im Phi. vorgeschlagen worden, aber
die Kegel, nach welcher dieser Vorschlag erfolgte, ist
```


## [2026-09-04T18:58:53.353Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['HUB','SNS','IEC','SKT','LAT','WLD','ARY','FSD','WEB','LKT','PLA','AFM','FVQ']:\n    v=d.get(k,{})\n    print(k,'|',v.get('page_offset'),'|',str(v.get('local_file'))[:200])\n\"",
 "description": "Get page offsets for secondary refs"
}
```


### [2026-09-04T18:58:55.064Z] TOOL RESULT

```
HUB | leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
SNS | 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt']
IEC | TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
SKT | leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
LAT | leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt
WLD | Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/da
ARY | printed page = pdf page + 1 | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt']
FSD | vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
WEB | not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt
LKT | leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt
PLA | 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home
AFM | 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt']
FVQ | printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt']
```


## [2026-09-04T18:59:05.232Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### SNS xist\"; grep -n -i \"xist\\|xišt\\|hšt\" SNS.txt SNS_pages.txt | head -10\necho \"### PLA athir\"; grep -n \"أثير\\|aithér\\|aither\\|athir\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -5\necho \"### FVQ athir\"; grep -n \"أثير\" FVQ.txt | head -5\necho \"### AFM athir\"; grep -n \"أثير\" AFM.txt | head -5\necho \"### LKT ather\"; grep -n -i \"aether\\|athir\" LKT.txt | head -5",
 "description": "Check SNS and Arabic loan dictionaries"
}
```


### [2026-09-04T18:59:05.350Z] TOOL RESULT

```
### SNS xist
SNS_pages.txt:1214:              \X/\Y^ ax§z: V (yW y. 178) xist                            :    o T *r*L**li                       - fL          .alfj^^l           :   ahunvad/ahuved-g3h :-oovt*>*^>                                                    '
SNS_pages.txt:15683:xist 36/1                x v 3his xvastan 58/9               xv arsedar mah 71/8         yasn 315/3
SNS.txt:2012:\X/\Y^ ax§z: V (y W y. 178) xist : o T *r*L**li 
SNS.txt:30695:xist 36/1 
### PLA athir
### FVQ athir
### AFM athir
### LKT ather
```


## [2026-09-04T18:59:07.178Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### WLD Bd1 aidh\"; grep -n \"aidh\\|ai-dh\\|aizma\\|istya\\|iṣṭakā\" incoming/WLD/WLD_Bd1_pages.txt | head -20",
 "description": "Grep Walde-Pokorny Bd1"
}
```


### [2026-09-04T18:59:07.237Z] TOOL RESULT

```
### WLD Bd1 aidh
446:idh-s-h zur Wzf. *aidh-).
623:ai-dh- ..brennen, leuchten                            ".
645:                                                                     ai-dh-                                             5
649:Univ. Arsskr. 1894, 98); daneben «-St. *aidhu- in gall.                                            Aedui,       air.   aed
689:  Auf idg. *aidli-lo- oder einer Kreuzung     von aidh- mit *aleto- (: lat. ad-
701:wartenl. Nach Stokes (KZ. 35, 595) ware auch mir. del „lime“ auf *aidh-
716:                                                               *aidh-s-mo -, vgl. ohne s           ai.   idhtna-h      m.
717:„Brennholz“).           *aidh-s-t- in:              lat.       aestds, -iatis „warme Jahreszeit,               Sommer",
746:son IF. 19, 136 auch ai. iila/ca ,.gebrannter Ziegel", av. istya- n. „Ziegel,
751:weisenden Worte vielmehr auf idg. ais-t- von der Wzf. *ai-s- neben *ai-dh-.
755:s-tru   und ctiJcstis f. „Leidenschaft aus aidhsti- mit ft-Einschub. Doch kann
1745:vor Augen“ (np. as /car „klar“; ai. avistya -, av. avisya- „offenkundig“); aksl.
8076:s. *aidh-.   DaB elai{$-)ov „Ol“ als „das brennbare“ benannt sei (Prellwitz 2
9264:bei    *aidh-           „glanzen“         zu bleiben).
9611:Anm. zw. ein mit *ai-dh- „al‘t}co u verwandtes        *is- erwagt; doch
9691:252 zu *aidh- „brennen“): in iihnlicher Bed. lorvugEf ogylgexai (Fick KZ.
23469:                            in-uraidh                  ds.,
52316:av. Zdvistya ,,der eiligste, raseheste, der forderlichste", uzutay- „hervor-
```


## [2026-09-04T18:59:18.499Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '700,760p' incoming/WLD/WLD_Bd1_pages.txt\necho \"=== page calc\"\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (623,716,746,751):\n    off=sum(len(x)+1 for x in lines[:ln-1])\n    leaf=t[:off].count('\\f')+1\n    print('line',ln,'leaf(1-based)',leaf,'printed',leaf-9)\nEOF",
 "description": "Print Walde-Pokorny aidh passage"
}
```


### [2026-09-04T18:59:20.271Z] TOOL RESULT

```
sprechung der brifc. Worte bezeichnet, doch wiirde man cymr. *oelwyd er-
wartenl. Nach Stokes (KZ. 35, 595) ware auch mir. del „lime“ auf *aidh-
lo- zuriickzufiihren.
   -es-St.:      gr.    aWog      n.        = ai. edhas- n. Brennholz. Weiter-
                                           „Glut,      Brand           1'




bildungen:         aisl.   eisa       f.    „Feuer“, norw. „Feuerstatte“, mnd.
                                               (
                                                 *didh-s-on -)
ese     f.   „Esse, Feuerherd" (aber nicht ahd. essa „Esse“ als *idh-tu, s. viel-
mehr         unter as- „brennen“; s. Lit. bei Osthoff PBrB. 13, 398, Falk-Torp
1455,        wozu noch Collitz Praet. 45).
   av.       aesma- m. „Brennholz'‘                        (
                                                               *aidh-s-mo -, vgl. ohne s           ai.   idhtna-h      m.
„Brennholz“).           *aidh-s-t- in:              lat.       aestds, -iatis „warme Jahreszeit,               Sommer",
aestns, -iis „Hitze           und dadurch bewirkte Wallung", aestuarc „infolge Hitze
wallen, brausen", agerm. Aistomodius („mit hitzigem Mute"),         ags. Cist m.
„Ofen“ (engl. oast „Hopfendarre“ ndl. eest „Darre“; vermutlich ahd. gan-
                                                                ),


eista „Feuerfunke“, aisl. gneiste „Funke“ (wenn die Trennung gan-eista zu-
trifft, vgl. Brugmann IF. 6, 102 f., Johansson IF. 19, 136 j; Johansson sieht

im 1. Glied ein zu ghen- „reiben" gehoriges Wort, wie in schwed. mdartl.
snaiksta f. „Funke“, apr. Jcnaistis „brennendes Scheit" ein zu ( s)qen „reiben“
gehoriges, ursprgl. „Reibfeuer“. Fur Jcnaistis ist iibrigens dt. Ursprung zu
erwagen; abg. gnetiti „anzitnden“ am ehesten nach Trautmann BB. 30,
329 f. direkt zu ghen- „reiben“. Ygl. iiber die strittigen Worte die Lit.
bei Johansson aaO., Yf. LEWb. 2 u. niteo Berneker312, Trautmann Apr.
                                                                                                                            -




6                                            aibbro-     —         aiu-,        aiu-



360 f., Falk-Torp u. gnist, Lewy IF. 32, 162), acech. niestcjS (f. pi.) „Ofen“,
spater nistej „Ofen, Feuerstatte, Backofen" (mit w-Yorschlag durch falsche
Zerlegung der Yerbindungen *m,n-estej%, vzn-estejachn, Berneker 275); dazu
schwundstufiges *idhsto- in sloven, isteje, steje pi. „Ofenloch“; nacb Johans-
son IF. 19, 136 auch ai. iila/ca ,.gebrannter Ziegel", av. istya- n. „Ziegel,
Backstein“ (Yoraussetzung ist Schwund von Dentalen vor s im Indischen).
     [Nicht wahrscheinlicher                erwiigen         Uhlenbeck Ai. Wb. 26 und Persson
Beitr. 326 a         —    vgl.   auch 338, 950 — Zuriickfiihrung dieser auf a)idh-s-t                            (

weisenden Worte vielmehr auf idg. ais-t- von der Wzf. *ai-s- neben *ai-dh-.
ai. istaJca nicht zur \Yz. *eis- „heftig bewegen*, Persson zweifelnd.]

     Trautmann GGA. 1911, 252 reiht an: lit. aistrii „Leidenschaft“ aus*aic?7i-
s-tru   und ctiJcstis f. „Leidenschaft aus aidhsti- mit ft-Einschub. Doch kann
                                                    ‘




=== page calc
line 623 leaf(1-based) 13 printed 4
line 716 leaf(1-based) 14 printed 5
line 746 leaf(1-based) 15 printed 6
line 751 leaf(1-based) 15 printed 6
```


## [2026-09-04T18:59:32.313Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### WLD Bd1 leaf 17 (p.8)\"; awk 'BEGIN{RS=\"\\f\"} NR==17' incoming/WLD/WLD_Bd1_pages.txt | head -40\necho \"########## WLD Bd1 leaf 47 (p.38)\"; awk 'BEGIN{RS=\"\\f\"} NR==47' incoming/WLD/WLD_Bd1_pages.txt | head -40",
 "description": "Print Walde-Pokorny pages 8 and 38"
}
```


### [2026-09-04T18:59:34.310Z] TOOL RESULT

```
### WLD Bd1 leaf 17 (p.8)
                       .                                                                                                          ;




8                                                      aik-, ik-   — aig-
rs.uauivog oder iyuayevog (in letzterem Falle aus *ixa ua itsvog) ..yerwundet",          l     l


gr. ar/ut'i ..SpieB"(*aik-sma 1)), apr. mjsmis BratspieB", lit iesmas, jie&nas .                   .



.BratspieB", lett. tesms .jedes zum Halten oder Zusammenhalten dui-chge-
steckte SpieBchen aus Holz oder Eisen, BratspieB                                        (Gdf. *aihnos oder dem
Gr.  genau entsprecliend *aiJc-smos); lat. Ico oder tcio, -ere ..treffen, ver-
wunden", ictus ,.Hieb, StoB wohl auch gr. I'y.zao „nahe (als anstofiend" 2 ))
                                               ",
                                                                                               "
                                                                                                       .




und i’ySrj, tydig Morser (auch tg, ixeg ..den Weinstock schadigende Wiirmer
                                      "
                                                                                                                             ",

woraus tines ds. nach den bedeutungsyerwandten y.vineg, oxvuneg, do'mtg
umgebildet sein konnte? s. Solmsen Beitr. 1 73 f. Anm. 2). S. J. Schmidt Yoc.
I 76, Fick II s 31, I 4 345, Bezzenberger BB. 27, 166, SolmsenBPhW. 1906,
723, Wtf. 172.      Hierher moglicherweise aucb anord, eigin n. „eben her-
vorgesproBter Saatkeim"' („Spitze“), schwed. mdartl. djel m. ds. (Fick 4
III 2) und nd. ine „Grannen, Ahrenspitze“ (Bezzenberger aaO.).
   Ahnliche Bedeutungen zeigen einige der unter aig- „Ziege“ besprochenen
Worte (ksl. jasva apr. eyswo „Wunde“), doch fehlt die Bedeutung „SpieB“
                             ,


dieser     Sippe          daher wil’d aiyju’j lit. iesmas nicht besser nach
########## WLD Bd1 leaf 47 (p.38)
38                                  agen-,   ang         agro-, ogro-



agen-, ang- „GefaS“?
                                                                    ir. aigen
     Gr. dyyog n.„Eimer, Schale“, ayyeTov ( *ayyso-iov) „Gefafi                          ‘,



„Pfanne“ (Pick II 7; iiber das hier
                               4,
                                       nach  Bezzenberger  BB.  4, 321  f. an-
gereihte an. key. ai. aga- „Topf, Krug“  s. aber Zupitza GG.  213).
   Wenn der Yergleich zutrifft, bestiinde ein Nasalverhaltnis wie zwiscben
lat.u-n-da und ai. ndan-.
  Doch konnte (unter Ausschlu.fi von aigen') dyyog und das damit von Uhlen-
beck Ai. Wb. 5 (zw.) verbundene ai. anjali-h m. „die beiden hohl anein-
ander gelegten Hande“ auch auf die neben aiak- „biegen“ liegende Wzf.
ang- (lat. angulus) bezogen werden, wie notwendig das von Schrader KZ.
30, 461       mit dyyog vereinigte ahd. ancha „occipitium, testa“, mhd. nhd. dial.
Anke hingegen „Genick“(s. dariiber Weigand-Hirt). — Ion. gyavov „Schmelz-
tiegel“       ist       nach Solmsen Unters. 46 a 1          als   rgyavov mifiverstandenes           x g-

yavov.


agos- „Fehl, Schuld, Siinde“.
                                                                                                            £

      Ai. agas- n. ds. ablautend             mit   gr. ay os       „sch\vere   Schuld,   Blutschuld‘            ;




ai.    dnagas-, gr. avayrjg „sehuldlos“            ;
                                                       aygg, svaygg „verflucht‘‘, ayiog' [uagog.
Curtius® 170 usw.
   Diese entsehieden ins sittliche Gebiet gewendete Bed. „Schuld, Frevel“
ist vielleicht aus sinnlicherem „Schaden, Wehtun" entwickelt: ags.
```


## [2026-09-04T18:59:40.166Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Ziege\" incoming/WLD/WLD_Bd1_pages.txt | head -20",
 "description": "Grep WLD Bd1 for Ziege"
}
```


### [2026-09-04T18:59:40.223Z] TOOL RESULT

```
746:son IF. 19, 136 auch ai. iila/ca ,.gebrannter Ziegel", av. istya- n. „Ziegel,
962:   Ahnliche Bedeutungen zeigen einige der unter aig- „Ziege“ besprochenen
994:aig- „Ziege“ (yielleicht „Springerin“                              s.   u.).
996:   Gr. aig, -yog „Ziege“, arm. aic ,.Ziege“; tiefstufig (aber Tga/.og ,,zQayog“,
997:iga/.fj „Ziegenfell“ ist ein yersch. "VVort kleinas. Ursprungs, s. Solmsen Beitr.
1000:lich „aus Ziegenleder“     wie gr. al’yeiog ), vgl. die gleichen Bedeutungsyer-
1025:   Wenn das Ziegenwort auf einer verbalen Bedeutung „springen“ beruht
1041:(Uhlenbeck Ai. Wb.                        — Beziehung zu *ago-s „Ziegenbock, Ziege“
1285:    *) Nicht nach Boisacq 1088    ubertragener Gebrauch von aig „Ziege“ nach Art von
1308:   Ygl. noeh das lautahnliehe *aig- „Ziege“ (wenn dies auf der Anschauung
3581: ago-s, agi- „Ziegenbock, Ziege“.
3582:   Ai. ajd-h „Ziegenbock“, ajd „Ziege“, mp. azak „Ziege“, np. asg ds.;
3585:   lit. ozijs „Ziegenbock“, ozka „Ziege“, lett. dzi-s „Ziegenbock‘ apr. loosee                ,
3589: „Ziege“, tvosnx „Ziegenbock“;
3590:   alb. <5/ „Ziege“ (G. Meyer BB. 8, 186, Pedersen KZ. 36, 320, 325; kaum
3591: zu *dik- „Ziege“);
3594:   lit. ofmis „zum Ziegenbock gehorig“, ozxena „Ziegenbockfleisch“;
3693:cymr. gafr „Ziege“ vorausgesetzten, im gr. allerdings nicbt nachweisbaren
9374:„Auftritt, Tritt“ (Persson Beitr. 563; anders u. *aig- „Ziege“); arm. ej
12216:2. er-    „Bock; Tier aus dem Schaf- oder Ziegengeschlecht                       11
```


## [2026-09-04T18:59:45.269Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '994,1030p' incoming/WLD/WLD_Bd1_pages.txt\necho \"###### ago-s\"\nsed -n '3578,3600p' incoming/WLD/WLD_Bd1_pages.txt\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (994,3581):\n    off=sum(len(x)+1 for x in lines[:ln-1])\n    leaf=t[:off].count('\\f')+1\n    print('line',ln,'leaf',leaf,'printed',leaf-9)\nEOF",
 "description": "Print WLD aig- Ziege and ago-s entries"
}
```


### [2026-09-04T18:59:46.946Z] TOOL RESULT

```
aig- „Ziege“ (yielleicht „Springerin“                              s.   u.).

   Gr. aig, -yog „Ziege“, arm. aic ,.Ziege“; tiefstufig (aber Tga/.og ,,zQayog“,
iga/.fj „Ziegenfell“ ist ein yersch. "VVort kleinas. Ursprungs, s. Solmsen Beitr.

2, 141,    Bechtel Lexil. 177 f.) ay. izaena- oder Izaena- „aus Leder“ (eigent-
lich „aus Ziegenleder“     wie gr. al’yeiog ), vgl. die gleichen Bedeutungsyer-
haltnisse bei *ago-              „Bock ‘). :




mann Apr. 296) wegen seines g,     ebenso der mit *aig-; die Formen jegla, jagla erklart
Briickner KZ. 45, 290f. nicht iiberzeugend als Dissimilation aus *jigla.
   *) Fiir einen Wzansatz *aigli- fehlt jede Stiitze   keine solche ist das von Holthausen
                                                                           ;



IF. 20, 316 mit alyjii] verglichene ags. dg-ldc, -Icec n. „Elend, Qual“ ( dgltcca „ Blender
Ungeheuer; Held, Kampfer”), das eigentlich „Lanzenspiel‘, daher „Kampf, Krieg* be-
deutet habe; unter derselben Voraussetzung kann darin entlehntes ir. dg „Kampf*
stecken.
   2
     ) S.
          Solmsen Wtf. 172, Vf. LEWb. 2 374; anders Brugmann IF. 16, 495: mit lat. igitur
zu ki-siyto; nicht iiberzeugend Ehrlich BPhW. 1911, 1574: zu v^e.oiy.xaiviodai „sich iiber-
aus schnell bewegen*.             .
                                                          (aig-?) ing-                                             9


   Wenn das Ziegenwort auf einer verbalen Bedeutung „springen“ beruht
(vgl. das ahnliche *aig- ,.sich heftig bewegen, schwingen, vibrieren“), so
konnte auch gr, I'yvog, I'yviov ,.Fu6spur, Fahrte“, i'yjiaza I'yvta Hes. (-v-              •



###### ago-s
alcel „Leid, Unrecht, Schade“, nfries. akelig, aeklig „horridus, miser, vehe-
 mens“ (Wood AlPh. 27, 59, Fick 4 III 7, Falk-Torp 459 unter igt).

 ago-s, agi- „Ziegenbock, Ziege“.
   Ai. ajd-h „Ziegenbock“, ajd „Ziege“, mp. azak „Ziege“, np. asg ds.;
                                                                                          :

   lit. ozijs „Ziegenbock“, ozka „Ziege“, lett. dzi-s „Ziegenbock‘ apr. loosee                ,



 „Ziege“, tvosnx „Ziegenbock“;
   alb. <5/ „Ziege“ (G. Meyer BB. 8, 186, Pedersen KZ. 36, 320, 325; kaum
 zu *dik- „Ziege“);
   ai. ajina-m „Fell“ (in neuiran. Dialekten idzin, dzein „FiIz“)

   lit. ofmis „zum Ziegenbock gehorig“, ozxena „Ziegenbockfleisch“;
                                      t:
   ksl. (j)asno (*azwio) „Haut, Leder                    .



   Z. B. Uhlenbeck Ai. Wb. 4 (unter Ankniipfung an ay- „treiben“??), Ber-
line 994 leaf 17 printed 8
line 3581 leaf 47 printed 38
```


## [2026-09-04T19:00:01.099Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor w in ['هیزم','خشت','اثیر','ازگ','هیمه']:\n    hits=[i for i,p in enumerate(pages) if w in p]\n    print(w, hits[:12])\nEOF",
 "description": "Grep Aryanpur for headwords"
}
```


### [2026-09-04T19:00:03.806Z] TOOL RESULT

```
هیزم [241, 459]
خشت [21, 22, 26, 39, 40]
اثیر []
ازگ [7, 9, 21, 33, 35, 59, 65, 71, 73, 91, 92, 93]
هیمه []
```


## [2026-09-04T19:00:07.833Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (241,):\n    p=pages[i]\n    # print lines containing هیزم and neighbors\n    L=p.split('\\n')\n    for j,l in enumerate(L):\n        if 'هیزم' in l:\n            print('--- leaf',i,'line',j)\n            print('\\n'.join(L[max(0,j-6):j+7]))\nEOF",
 "description": "Print Aryanpur hizom entry"
}
```


### [2026-09-04T19:00:09.431Z] TOOL RESULT

```
--- leaf 241 line 14
ایسلندی کهن (( 5640/01۸4 0/۵): 815۸ 9 (۳88) هیده
آلمانی کهن (/057014۸ 4/07 ۵70): ۴889۸ 2 (70ه) 347
آلمانی ((050/4): لاد برهان قاطع + ۷۵۰
یادداشت.
۱ چم این واژه در زبان یونانی و ایسلندی کهن و ایرلندی کهن: شمله؛ لو آتش,.
چم این واژه در زبان آلمانی کهن و آلمانی؛ دودکش‌بخاری» بخاری,
۲- واژه‌ی فارسی "هیزم" نیز از همین واجريشه است. ۰
اوستایی (۸۷287۸۷): 7 مشاه
+1118 ش1153 +1۸05 انگلیسی (8(/0/5923): ۸ ,5885
پارسی باستان (۶8781404 010): ۰ 1811۸ نروژی (/078014/): 50
پپلوی (۲1مانتم): 311817 ,8116ن111 هلدی (0076): 7200
کر دی (80/57ا۸): َ 11111 اسلاوی کهن (عاماد تلعقنانه /0):
2 ات سانمگر یت (54/37): 771 811۳71
```


## [2026-09-04T19:00:17.568Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[241][:2200])\nEOF",
 "description": "Print full Aryanpur leaf 241"
}
```


### [2026-09-04T19:00:19.407Z] TOOL RESULT

```
[pdf page 242]
۹ 5
پهلری (۲1الا۸ط): ان ایرلندی کهن (لادلقا ۳ا0): زراد ۱
افغانی (پشتر) (//۸۳07۸):
۸ 2۸8717۸ پسگشت‌ها کیت ی
سانسکریت (8۸۸/97077): زا ۳
18117۸ بقکل۸ 18117 5 (88106) ان
یونانی (086)+ 05 6034 (8316) لاه
ایسلندی کهن (( 5640/01۸4 0/۵): 815۸ 9 (۳88) هیده
آلمانی کهن (/057014۸ 4/07 ۵70): ۴889۸ 2 (70ه) 347
آلمانی ((050/4): لاد برهان قاطع + ۷۵۰
یادداشت.
۱ چم این واژه در زبان یونانی و ایسلندی کهن و ایرلندی کهن: شمله؛ لو آتش,.
چم این واژه در زبان آلمانی کهن و آلمانی؛ دودکش‌بخاری» بخاری,
۲- واژه‌ی فارسی "هیزم" نیز از همین واجريشه است. ۰
اوستایی (۸۷287۸۷): 7 مشاه
+1118 ش1153 +1۸05 انگلیسی (8(/0/5923): ۸ ,5885
پارسی باستان (۶8781404 010): ۰ 1811۸ نروژی (/078014/): 50
پپلوی (۲1مانتم): 311817 ,8116ن111 هلدی (0076): 7200
کر دی (80/57ا۸): َ 11111 اسلاوی کهن (عاماد تلعقنانه /0):
2 ات سانمگر یت (54/37): 771 811۳71
نان لاد 508۸4 ,8199۸7 روسی (۵(۷ا55لا): 01
پونانی (0/888): ۹۱ ۱ لیترانی 8۸1871:77 ,8۸8۸8 :
,۸08 ,11۸1705 لنونی (لني) (47714): 5۸188 ,81نا8
لاتین (/712مل): 015 آلبانی (02(هه ۸+ زا
آلمانی کهن (/08804۸ ۲/۵7 0ا0۵):
نرادن زین
انگلیسی کهن (بدا.ا0/(ظ 010):
```


## [2026-09-04T19:00:30.066Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### MON خشت\"; grep -n \"^خشت\\|خشت:\" MON_part1.txt | head -5\necho \"### WEB anneal/estuary\"; grep -n -i \"^anneal\\|^estuary\\|^ether\\b\" WEB_vol1.txt | head -5\necho \"### FSD anneal\"; grep -n -i \"anneal,\" FSD_vol1.txt | head -3\necho \"### IEC aig goat\"; grep -n \"aig-, \\|aigos\\|aigs\" IEC.txt | head -10",
 "description": "Grep Moin, Webster, Funk, Mann"
}
```


### [2026-09-04T19:00:30.196Z] TOOL RESULT

```
### MON خشت
5313:خشت و آهک و امتال آن بزند) بزاوه» 
26870:بید خشت: ]نا (امر.) و کی که 
37079:خشت بحته» آجر بزرگ. 
50116:چرخشت: 2708 (.) چرخی که با آن 
55466:خشتل: )۷2 [ع.] (مسصم.) فریب دادن» 
### WEB anneal/estuary
36226:ether.
65253:ether or around: also spelled intwine. _ ine/ment, 7. a twisting round; union.
102287:ether by means of cement, mortar, ete., or
109095:ether. x 2 to close tightly and firmly; as, his jaws locked. _
114286:ether 5m of 1S for 'OCEsg Ncon. Uced: fense
### FSD anneal
### IEC aig goat
300:aigilos (or aigilos) (a tree or shrub). Cf. aigos Gk. aígilos; OHG eihhila; G Eichel
301:aigos (or aigos) (a kind of tree). WP I, 10 Myc. cf. aikinoo (queried “part of a chariot);
302:Gk. cf. krát-aigos, aig-eiros, aig-anée; OHG
2965:dhoiĝhos, om, is, iə ‘shape, mould; shaper’. Cf. dheiĝh-. WP I, 833 Skt. dehah, -am “body, mass, person’; dehth ‘rampart; Av. -daeza, in pairi- ‘rampart’; LW in Arm. dez, gs dizi “pile, rick and par- tez ‘paradise’; Tokh. A tseke ‘plastic figure’; tsek-, B tsaik- ‘to shape’; Gk. toikhos “house- wall’; Myc. to(i)ko-, id.; Gothic daigs, OHG teic, OE dag ‘dough, mass: ON deg id., deigr ‘plastic’; Pol. dzieza, Slovak dieZa, Cz. diže ('kneading-trough'. Isophonic with OE dæge *bread-maker'; ON deigja "mad": Finn. LW taika *magic'; taikina *dough'; Li. (perh. by metath.?) žiedas (fring, thimble, blossom’. Semantics obscure). (W dull *form, shape? seems to represent a type *dhoighlio-)
11025:beside maigs, adj. "soft A type moighos, à is represented in Skt. megháh, m. ‘cloud’; Av. maeyo, m. id.; Per. miy, id.; Arm. meg, gs migi, ab. s. migav, s. ‘fog; Go. cf. maihstus "dung Li. maigai, mpl. ‘litter
11805:noigos, à “gentle, fair; gentility, fairness, beauty” OCS něga, f. ‘delight’; R ‘effeminacy’; Srb. ‘cherishing’; Cz. něha ‘gentility, fondness’; Latv. naigs, adj. (3) ‘beautiful
11806:noigh- OE nægan, v. ‘accost, attack’; ge-nāg (hapax) ‘dashing’; Latv. naigs, adj. (1) ‘quick’
18125:suoig- (suoigos, ios) ‘fresh, lively’. (Celtic and Balto-Slav ambig.). See next W hu, adj. ‘bold’; OCS svěží, adj. ‘fresh’; svézZanü “bold, keen’; Latv. svaigs, adj. id. & ‘fresh’; (for the consonantism, cf. OHG be- swihhen, intr. *clear, brighten and Go. swikns, adj. “cleared of crime, innocent")
18126:suoigh- “bend, sway, rush, lunge, topple'. (Gk. ambig. Cf. uoigh-) Gk. (ambig.) oíkhomai, v. “rush, depart, va- nish’; ON sveigja, v. ‘bend’; sveigjast, refl. ‘sway’; Li. svaigstù, svaigti, v. ‘tipple; frolic, fall senseless, faint’; sviegiu, ti, v. (fling, fr. *sueigh- or *suoigh-); svaigùs “intoxica- ting. (Isophones: MHG sweig, sweige, f. ‘drove of cattle; ranch’; sweigen, wv. (tend (cattle); Li. dial. svíegiu, ti smear; punch")
```


## [2026-09-04T19:00:37.705Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### IEC goat\"; grep -n \"goat\" IEC.txt | head -12\necho \"### WEB anneal\"; grep -n -i \"anneal\" WEB_vol1.txt | head -5\necho \"### FSD anneal\"; grep -rn -i \"annealing\\|to anneal\" FSD_vol1.txt | head -3\necho \"### FSD aego\"; grep -n -i \"aego-\\|aegis\" FSD_vol1.txt | head -5",
 "description": "More greps in Mann, Webster, Funk"
}
```


### [2026-09-04T19:00:37.846Z] TOOL RESULT

```
### IEC goat
259:agis, ios (2) 'goat'. Cf. aigis Skt. ajab, adj. (ajáh, m.); Alb. dhí; Li. ožys; Latv. āzis. Cf. with short vowel Skt. ajáh; Gael. agh ‘hind’, and perhaps also Dacian azila (a plant: houndstongue"?)
305:aigis ‘kid, goat. WP I, 8 Skt. cf. aja; Arm. ajc; Phryg. aizi-; Myc. aiki- (for aigi-); Gk. as gs. aigós; EMAlIb. edh; Li. cf. oZys; Latv. azis (fr. a type *agis)
926:bekio *bleat, bray' It. cf. becco ‘billy-goat’; Br. bégia ‘bleat’; Cor. bégy, begya, id. (and "brav Cz. bečet, Pol. beczec, Srb. becati ‘bleat’ beside Slovene békati, id.
1020:bukk- (buks-?) (2) ‘he-goat’. WP II, 189 Skt. bukkah; Oss. bodz, bodzo; Per. buz; Olr. bocc; Ir.boc; W bwch; Latv. buks, bucens, id.
1536:bhorus, uos, uis (1) ‘smal! domestic animal". Cf. bhero Lydian bórus, gs -uos (an unknown animal. Hes.); Alb. cf. berr ‘small domestic animal’; OCS bravi, id.; Cz. brav “sheep? or ‘goat; Slovak ‘pig’ or ‘boar’; Srb. “tan” or 'castrat- ed boar’
1894:bhuĝos, ios, o(n) ‘small animal’. WP II, 189 Av. büzo ‘buck’; Per. buz ‘goat; Oss. bodz, Dig. bodzo, id.; Arm. buc, a-st. lamb; MHG boc, gs bockes ‘he-goat’; ON bokkr, bukkr, id. Finn. LW pukki, id.
2272:dig- ‘goat; goatskin’ Arm. tik (a-st. ‘skin bottle, bagpipes’); Lacon. díza (goat, fr. *digio); OHG zicchi; G Zicke skid?
3924:gebor (gerb-, geb-) (?) jumper, frisky animal Ir. gabhar ‘goat; OBr. gabr (in a cpd.) id: Br. gaur, gavr tnanny-goat'; W gafr, id.; ON cf. kjappi ‘he-goat; EME cf. kipper “salmon”: OCS Zrébe, Zdrébe, n. “foaP; Pol. źrebię, id. (but for Czech hříbě ‘foaľ, see gurebh-)
5717:ĝid- ‘small creature. Cf. WP I, 527. See eidh-, dig- Arm. Cit, gs cti, i-st. ‘small sparrow, tit; Alb. dhí ‘goat’ (ambig. see 8idh-); MHG kiz, kitze ‘buck, kid?; G Kitz ‘fawn in first year’; Kitze *she-cat, kid, fawn’; EME chit (freckle; young person’. Cpds: chit-lark, chit-pease); E dial. chit “eye of potato’; cf. E kit (kitten, fr. Norse?); Du. cf. kittig ‘sprightiy’
5718:eidh- (variant of gid-? Cf. WP I, 527) Gk. cf. ai-gíthalos (orn. *tit'. Cf. auis (1)); Alb. (ambig.) dhí, def. dhija (goat, but cf. gid-); ME kid; Du. kid, kidde ‘pony’; ON kið, gp -a, ja, n. "d: Sw. kid, beside kidling, killing, id. (Eng. kid is prob. of Norse origin, note initial k-)
5922:êhaidos ‘goat, kid’. WP I, 527 Lat. haedus ‘kid’; Rustic Lat. hedus (Yarro); Sabine fedus, faedus; Go. gaits, f. i-st. ‘goat’; MHG geiz; OE gåt; ON geit, id.; Li. cf. žaid- žiù, Zaisti “play? and Skt. jihi-, id. and “jump”. Adj. of type *&haidino- in Lat. haedinus: OHG geizin
6069:in-gimus *one-year-old'. Extns: Skt. himeluh ‘chilly’; Tokh. semál ('goat', lit. *year-old"); Arm. dzmern, gs dzmeran, pl. dzmerunk *win- ter; Gk. khímaros ‘yearling goat; LLat. cf. himeros (sic 'raisins); Ir. geamhar ‘green corn’; Icel. gimbur, pl. gimbrar 'ewe-lamb'; Scots gimmer (‘yearling ewe’, fr. ON); Sw. gimmer, id. WP I, 547
### WEB anneal
7986:nealed, pt., pp.; annealing, ppr. [ME. anelen, onelen; AS. anzlan, onælan, to burn; an, on, on, and ælan, to burn, set on fire; al, æl, fire.]
7988:of rendering less brittle; to temper by a grad- ually diminishing heat. 2. to strengthen and temper (the mind, will, etc.). ieee 3. to heat, as glass or tiles, in order to fix colors; to bake. [Archaic.] ; an-néal/ér, n. one who or that which anneals. an-néal/ing, . the process or art of annealing.
7990:an-nēal’ing pot, a closed pot in which articles to be annealed. are placed to prevent them from being oxidized.
26269:2. an oven for annealing metals. cal/ca-rate, cal/ca-ra-ted, a., [L. calcar, a = spur.] in biology, provided with a spur; as,
83932:nich impressions are printed from various kinds of blocks or plates, as etching, lithography, dry point, offset, etc. graphic tellurium; vanite. the Syn.— picturesque, illustrative, descriptive, pictorial, forcible, vivid. graph/ic-Al-ly, adv. in a graphic manner. graph/ic-Al-ness, z. the condition or quality of being graphic. graph/ic-ness, 7. graphicalness. graph/ics, n.pl. [construed as sing.) 1. the art of making drawings, as in architecture or en- gineering, in accordance with mathematical rules. 2. calculation of stresses, etc. from such drawings. _ graph-i-ol/6-gy, n. (Gr. grapheion, astyle, pen- cil, and -logia, from legein, to speak.] the art of Woe or delineating; also, a treatise on this art, graph’īte, n. [Gr. graphē, a writing, from graphein, to write, draw, and -ife.] one of the forms of carbon: also known as plumbago and black lead. It has an iron-gray color, metallic luster, granular texture, and is soft and unc- tuous to the touch. It is used chiefly in the manufacture of pencils, crucibles, lubricants, electrodes, etc. gra-phit’ic, a. relating to, containing, or de- rived from graphite. graphitic carbon; carbon found in iron or steel which is considered to be graphite. graph i-tīze, v.t.; graphitized, pt., pp.; graphi- hi ang, ppr. 1. to change into graphite by ae or annealing. + to put graphite in or on. graph’i-toid, graph-i-toid’ăl, a. [Gr. graphé,
### FSD anneal
FSD_vol1.txt:17129:gradually  heating  and  gradually  cooling  glass,  metals, or  other  substances  to  reduce  brittleness  and  increase flexibility,  strength,  etc.—  an-nearing*arch",  n.  A   cool- ing-oven for  annealing  glass;  a   leer.—  a.sbox,  n.  A   box  in which  articles  to  be  annealed  are  enclosed  while  in  the  fur- nace.—a.  *co!or,  n.  The  hue  taken  by  steel  in  annealing. —   a.*pot,  n.  An  air-tight  pot  into  which  articles  being annealed  are  put  to  protect  them  from  oxidation.
FSD_vol1.txt:43744:3.  Cookery.  To  make  w*hite,  as  by  taking  off  the  skin, or  by  scalding;  as,  to  blanch  almonds;  also,  to  whiten by  plunging  first  into  hot  and  then  into  cold  water;  as, to  blanch _   meat.  4.  To  w’hiten  (plants)  by  depriving them  of  light,  as  by  banking  up  earth  about  them,  etc. 5.  To  whiten  or  brighten  (metals),  as  by  the  removal of  oxid  by  the  use  of  acids,  by  annealing,  or  by  coating w’ith  tin.  6.  [Rare.]  To  make  excuse  for;  palliate; whitewash.
FSD_vol1.txt:49671:annealing bat
### FSD aego
```


## [2026-09-04T19:00:52.988Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ether",
 "prompt": "Give the etymology of ether/aether: Latin aether, Greek aithēr, the PIE root, and when the chemical/anaesthetic sense arose."
}
```


## [2026-09-04T19:00:53.702Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%C3%A9ther",
 "prompt": "French éther: give the etymology (from Latin aether, from Greek), the date of first attestation and the chemistry sense."
}
```


### [2026-09-04T19:00:58.750Z] TOOL RESULT

```
# French "éther" Etymology and Information

**Etymology:** The word derives from Latin *aethēr* ("upper air, ether"), which came from Ancient Greek *αἰθήρ* (aithḗr, "air; ether").

**Date of First Attestation:** The provided Wiktionary entry does not include a specific date of first attestation for the French term.

**Chemistry Sense:** While the entry confirms that "éther" means "ether" in French, it does not provide a detailed definition of the chemistry sense. The page does list a derived term—"méthyl tert-butyl éther"—which suggests chemical usage, but no explicit chemical definition is given in the source material.
```


### [2026-09-04T19:00:59.186Z] TOOL RESULT

```
# Etymology of Ether

**Linguistic Lineage:**
The word traces back through Latin *aether* and Greek *aithēr*, meaning "the upper pure, bright air; sky, firmament." The Greek term derived from *aithein*, "to burn, shine," which connects to the Proto-Indo-European root *\*aidh-*, meaning "to burn."

**Ancient and Scientific Usage:**
In classical cosmology, ether represented "the element that filled all space beyond the sphere of the moon, constituting the substance of the stars and planets." From the 17th through 19th centuries, scientists adopted it as a theoretical framework for understanding universal forces, though it lacked clearly defined material properties.

**Chemical Discovery:**
The chemical compound received its name around 1730 (English adoption by 1757). Though recognized since the 14th century for its "lightness and lack of color," the substance's anesthetic properties weren't fully established until 1842.

**Scientific Decline:**
The Michelson-Morley experiment (1887) challenged the ether concept, which was ultimately abandoned in the early 20th century following Einstein's Theory of Relativity. Before its dismissal, the term spawned the colloquial usage for "the radio" (1899).
```


## [2026-09-04T19:01:10.195Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82eyd%CA%B0-\" \\\n \"https://en.wiktionary.org/wiki/%D9%87%DB%8C%D8%B2%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%B4%D8%AA\" \\\n \"https://www.etymonline.com/word/estuary\" \\\n \"https://www.etymonline.com/word/anneal\" \\\n \"https://www.etymonline.com/word/ether\" \\\n \"https://en.wiktionary.org/wiki/%CE%B1%E1%BC%B4%CE%BE\" \\\n \"https://en.wiktionary.org/wiki/%D8%A3%D8%AB%D9%8A%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ey%C7%B5-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82e%C7%B5-\" \\\n \"https://en.wiktionary.org/wiki/%C3%A9ther\" ; do\n  timeout 120 python3 tools/fetch_source.py \"$u\" --note \"pdf page 39, roots Aidh/Es 1 and Aig-: verification of ether/estuary/anneal/hizom/xesht/goat chains\" 2>&1 | tail -2\ndone",
 "description": "Archive all web sources used"
}
```


### [2026-09-04T19:01:15.043Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f6f088c1187cbd07.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7c9b24cdb51ecbb0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/362b528ffe88f70e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1098071fd387aeb2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b4276e11bc2f8e2d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/534980109a20e44f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a8e8508383471b55.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ae7c36f81596bf1b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9b626e9c1a5ca337.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5c5ab2ed410b9aa5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/af09a0d54c6d5a2b.txt
```


## [2026-09-04T19:01:19.949Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2005,2020p' SNS.txt\necho \"### BQT v1 ازگ\"\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'ازگ' in p:\n        print('leaf',i)\nEOF",
 "description": "SNS xist entry and BQT azg"
}
```


### [2026-09-04T19:01:21.906Z] TOOL RESULT

```
■fr/T ^ 




x§z :>;t {GNPE. 102)xaSzanuha-haSz ^j 1 ;.^ 
\X/\Y^ ax§z: V (y W y. 178) xist : o T *r*L**li 

.jiil>£-t J -.^l > i. i L :abaz-Sxez§n5nd : jku^^ 

\x/\vJ\ 

■YA tf t-iO'jcwV 'o-l#*< tahySsi 

•f/1t^ ahy5 yfis.n- : *- 
### BQT v1 ازگ
leaf 17
leaf 552
leaf 638
```


## [2026-09-04T19:01:35.421Z] TOOL CALL #76: Bash

```json
{
 "command": "grep -l '\"Es 1\"' data/extracted/batch/*.json | head -5; grep -h -o '\"name\": \"Es[^\"]*\"' data/extracted/batch/*.json | sort -u | head",
 "description": "Find root Es 1 elsewhere in the extracted data"
}
```


### [2026-09-04T19:01:35.511Z] TOOL RESULT

```
data/extracted/batch/page-161.json
"name": "Es 1"
"name": "Es 2, Es-ti"
"name": "Es-ti"
"name": "Esu"
```


## [2026-09-04T19:01:39.007Z] TOOL CALL #77: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-161.json'))\nfor e in d['entries']:\n    r=e['root']\n    if r.get('name','').startswith('Es 1'):\n        print(json.dumps(r,ensure_ascii=False))\n        for n in e['nodes'][:8]:\n            print(n['id'],n['parent'],n['lang'],n['refs'],[ (w['translit'],w['gloss']) for w in n['words']])\n\"",
 "description": "Inspect root Es 1 entry"
}
```


### [2026-09-04T19:01:40.608Z] TOOL RESULT

```
{"name": "Es 1", "redirect": "Aidh"}
```


## [2026-09-04T19:03:13.418Z] TOOL CALL #78: WebSearch

```json
{
 "query": "Persian هیمه hima firewood etymology Middle Persian Avestan aēsma Hasandust"
}
```


### [2026-09-04T19:03:15.233Z] TOOL RESULT

```
Web search results for query: "Persian هیمه hima firewood etymology Middle Persian Avestan aēsma Hasandust"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T19:03:21.687Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"هیمه\" MON_part1.txt MON_part2.txt | head -8",
 "description": "Grep Moin for هیمه"
}
```


### [2026-09-04T19:03:21.745Z] TOOL RESULT

```
MON_part1.txt:26346:بهایم: سعرقناها [ع. بهائم] )1( 3 سهیمه» 
MON_part1.txt:26585:بهیمه: (ع)فس-طده [ع. بهیمه ] (.) چهار با 
MON_part1.txt:53649:حطب: ۸ (ع.] (.) هیزم» هیمه؛ ج. 
MON_part2.txt:27134:هیزم» هیمه. ( گٌیا.) (فره.) قسمت پایین 
MON_part2.txt:92770:هیرم. 1(.) هیمه. چوب خشکد. هیزم 
MON_part2.txt:92801:هیمه فر هنگ فار سی معیر ۳۱۹ 
MON_part2.txt:92807:هیمه: (ظ)۱1012 هیزم.
```


## [2026-09-04T19:09:07.109Z] TOOL CALL #80: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk39.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nAIDH = W + \"Reconstruction:Proto-Indo-European/h%E2%82%82eyd%CA%B0-\"\nAIG  = W + \"Reconstruction:Proto-Indo-European/h%E2%82%82ey%C7%B5-\"\nAG   = W + \"Reconstruction:Proto-Indo-European/h%E2%82%82e%C7%B5-\"\nHIZ  = W + \"%D9%87%DB%8C%D8%B2%D9%85\"\nXST  = W + \"%D8%AE%D8%B4%D8%AA\"\nAIX  = W + \"%CE%B1%E1%BC%B4%CE%BE\"\nATIR = W + \"%D8%A3%D8%AB%D9%8A%D8%B1\"\nETHR = W + \"%C3%A9ther\"\nEO   = \"https://www.etymonline.com/word/\"\n\ndata = {\n \"pdf_page\": 39,\n \"book_page\": 9,\n \"verified_by\": \"claude-fable-5-1\",\n \"verified_on\": \"2026-09-04\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Aidh, Es 1\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *h₂eydʰ- 'to ignite, burn; fire' (Pokorny 11-12 'ai-dh-'; Walde-Pokorny I 4-6; Watkins/AHD 'aidh-')\",\n   \"note\": (\"Root form, language label and gloss 'to burn' are all correct: Pokorny 11-12 gives ai-dh- \"\n     \"'brennen, leuchten' with exactly the material Nourai charts (Av. aēsma-, Av. ištya-, Gk. \"\n     \"aiθήρ, Lat. aestus/aestās, Gmc. *ail- in OE ǣlan). The second root name 'Es 1' is \"\n     \"Nourai's own alias — in his dictionary 'Es 1' is itself a redirect to 'Aidh' (see page-161.json) — \"\n     \"and it conflates *h₂eydʰ- with the separate root *as- / *h₁eus- 'to burn, glow' (Pokorny 68, \"\n     \"Watkins 'as-'), which Pokorny and Watkins keep apart. The conflation is not baseless: Walde-Pokorny I 6 \"\n     \"records Uhlenbeck's and Persson's proposal to trace the *aidh-s-t- words 'vielmehr auf idg. ais-t- von der \"\n     \"Wzf. *ai-s- neben *ai-dh-', and Etymonline still assigns ANNEAL to *as- rather than *aidh-. Two internal \"\n     \"problems on the page: the Avestan/Old Persian box mixes an Avestan word (aēsma-) with a Middle \"\n     \"Persian one (hēzum) and mis-glosses aēsma- as 'heat' (it is 'firewood'); and the last Latin box \"\n     \"prints 'asetus', a misprint for Latin aestus (confirmed on the page image at 600 dpi, so it is Nourai's \"\n     \"error, not an extraction error). The brick branch (Av. ištya-, OP išti-, MP/NP xišt) rests on \"\n     \"Johansson IF 19,136, accepted by Walde-Pokorny, Pokorny, Horn, Hübschmann, Buck and Mann, but modern \"\n     \"Indo-Iranianists (Lubotsky 1999/2001, Schmitt 2018, as cited by Wiktionary) treat Indo-Iranian *išt(i)- \"\n     \"'brick' as a BMAC-substrate loan word, i.e. not a derivative of 'to burn' at all.\"),\n   \"sources\": [AIDH, EO+\"ether\", EO+\"estuary\", EO+\"anneal\"],\n   \"ref_check\": [\n     {\"ref\":\"PRT\",\"status\":\"not_checked\",\"note\":\"Partridge, Origins (1958). refs_online: all archive.org copies are lending-only; no open text, no page number given by Nourai.\"},\n     {\"ref\":\"KLN\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 297 (~p.570) s.v. 'ether, also aether': 'L. aether, fr. Gk. αἰθήρ ... derives fr. αἴθειν, \\\"to burn\\\", fr. I.-E. base *aidh-, \\\"to burn\\\", whence also L. aedes'.\"},\n     {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt l.270-271: 'aidh-. To burn. 1. Suffixed form *aidh-sto- ... b. Latin aestas ...: AESTIVAL. 2. Suffixed form *aidh-lo- perhaps in Germanic *ail- in Old English āl, fire: ANNEAL. ... 4. Suffixed form *aidh-stu- in Latin aestus, heat, swell, surge, tide: ESTUARY. 5. Suffixed form *aidh-er- in Greek aithēr, air: AETHER, ETHER. [Pok. ai-dh- 11.]' — no 'Es'/'as-' material here; Watkins lists as- separately.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\":1,\"lang\":\"Avestan / Old Persian\",\"words\":\"aesmo; hĕzum\",\"verdict\":\"plausible\",\n     \"derivation\":(\"Avestan aēsma- m. is 'firewood', not 'heat': Bartholomae AiW s.v. 'aēsma- m. \\\"Brennholz\\\"', \"\n       \"cited from Y.7.3, V.14.2 etc., from Proto-Iranian *aizma- < *h₂eydʰ-s-mo- (Walde-Pokorny I 5: 'av. \"\n       \"aēsma- m. \\\"Brennholz\\\" (*aidh-s-mo-, vgl. ohne s ai. idhma-ḥ)'); the -s- is the same formant as in \"\n       \"Lat. aestus and Lith. iesmas. The second word, hēzum, is not Avestan or Old Persian at all but Middle \"\n       \"Persian: MacKenzie CPD writes it ēzm (ideogram CYBA), and the h- plus the anaptyctic -u- are late \"\n       \"Iranian developments (Hübschmann, Persische Studien §64a, p.174-5: 'hēzum \\\"Brennholz\\\" aus \"\n       \"*ēzm = ap. *aizma- = zd. aēsma-', the u inserted to avoid an over-long syllable). Old Persian has \"\n       \"no attested *aizma- — the Old Persian label is unsupported.\"),\n     \"sources\":[AIDH, HIZ],\n     \"ref_check\":[{\"ref\":\"POK:11\",\"status\":\"supports\",\"note\":\"Pokorny 11-12 (POK_full.txt 'Root/lemma: ai-dh-', Page(s): 11-12): 'Avestan aesma m. \\\"Firewood\\\" (*aidh-s-mo-, cf without s Old Indic idhma-h m. ds.); in addition Baltic *aismia in Lithuanian iesme \\\"firewood\\\"'. Supports the arrow root->aēsma-; nothing there about a form hēzum being Avestan or Old Persian.\"}],\n     \"consulted\":[\n      {\"src\":\"BRT\",\"where\":\"AiW s.v. aēsma- (BRT.txt l.2726)\",\"stance\":\"supports\",\"note\":\"'i. aesma- m. \\\"Brennholz\\\" ... Zum ai. V. indhati, gr. αἴθω. Aus ir. *aizma-. — np. hīzum.' Gloss is 'firewood', not 'heat'.\"},\n      {\"src\":\"WLD\",\"where\":\"Bd. I p.5 (WLD_Bd1_pages.txt leaf 14)\",\"stance\":\"supports\",\"note\":\"'av. aesma- m. \\\"Brennholz\\\" (*aidh-s-mo-, vgl. ohne s ai. idhma-h m. \\\"Brennholz\\\")'.\"},\n      {\"src\":\"IEC\",\"where\":\"Mann, 'aidhmos, aidhsmos' (IEC.txt l.288)\",\"stance\":\"supports\",\"note\":\"'aidhmos, aidhsmos \\\"burning\\\". WP I,5. Skt. idhmáh; Av. aesmo; ON eimr; OE am; ... Li. iesmas, iesme \\\"firing-charge\\\".' Mann cites the Avestan nominative aesmo, exactly Nourai's spelling.\"},\n      {\"src\":\"PHD\",\"where\":\"MacKenzie CPD s.v. ēzm (PHD_mackenzie.txt l.2271)\",\"stance\":\"partial\",\"note\":\"'ēzm [CYBA < A ...| N hēzum] firewood, fuel' — the Pahlavi form is ēzm; hēzum is given as the New Persian outcome, so the box's language label for hĕzum is wrong.\"},\n      {\"src\":\"AHD\",\"where\":\"Watkins 'aidh-' (AHD_watkins1985.txt l.270)\",\"stance\":\"silent\",\"note\":\"Watkins lists only Germanic, Latin and Greek reflexes under aidh-; no Iranian material.\"}\n     ]\n    },\n    {\n     \"id\":2,\"lang\":\"Persian\",\"words\":\"hîzom «هیزم»; hîmeh «هیمه»\",\"verdict\":\"plausible\",\n     \"derivation\":(\"هیزم hīzom continues MP ēzm/hēzum < Proto-Iranian *aizma- < *h₂eydʰ-s-mo-, the same word as \"\n       \"Av. aēsma-: the diphthong ai > ē, an anaptyctic -u- breaks the final cluster -zm, and a prothetic h- is \"\n       \"added before the initial vowel (Hübschmann PSt §64a p.174-5; the same prothesis as in Pāzand hēzum). \"\n       \"Horn no.1117 (p.249) gives the chain 'hēzum, hēzem \\\"Brennholz\\\"; aw. aēsma-; phlv. ēsm ..., \"\n       \"hēzam bezw. ēzam (pāz. hēzam); ai. idhmá-', with Kurdish ēzing and Munji ēzma. \"\n       \"The second word هیمه hīma 'firewood' is only a synonym: Horn prints it inside the same entry and Mo'in \"\n       \"cross-refers ('رک: هیمه') and glosses هیمه simply as هیزم without an origin tag, but no \"\n       \"source derives hīma from *aizma- phonetically (the -z- would have to disappear without trace), so its \"\n       \"membership in this box is asserted rather than demonstrated. The Molavī line quoted on the chart \"\n       \"('ور بود خاری تو هیمهٔ گلخنی') uses هیمه in the ordinary sense 'firewood for the bath-house furnace'.\"),\n     \"sources\":[HIZ, AIDH],\n     \"ref_check\":[\n      {\"ref\":\"BQT:2407\",\"status\":\"supports\",\"note\":\"Borhan-e Qate' p.2407 (fetched with tools/ref_page.py BQT:2407 -> BQT_v4 pdf p.490), Mo'in's etymological footnote to هیزم: 'هیزم - بتلفظ قدیم hēzum (تلفظ کنونی hīzom)، اوستا aēsma-، پهلوی ēsm, hēzam، پازند hēzum، هندی باستان idhma-، منجی ezma، کردی ēzing ... رک: هیمه'. Exactly the arrow Nourai draws, and it is also the source of his cross-reference to هیمه.\"},\n      {\"ref\":\"HRN:249\",\"status\":\"supports\",\"note\":\"Horn, Grundriss p.249 (HRN.txt leaf 270) no.1117: 'hēzum (Is. 30,88), hēzem \\\"Brennholz\\\"; hīme. aw. aēsma \\\"Brennholz\\\"; phlv. ēsm (nur umschreibend), hēzam bezw. ēzam (päz. hēzam); ai. idhmá-.' Page number cited by Nourai is exactly right.\"}\n     ],\n     \"consulted\":[\n      {\"src\":\"HUB\",\"where\":\"Persische Studien §64a, p.174-5 (HUB.txt leaf 184)\",\"stance\":\"supports\",\"note\":\"'hēzum \\\"Brennholz\\\" aus *ēzm = ap. *aizma- = zd. aēsma-' — given as an example of anaptyctic u.\"},\n      {\"src\":\"MON\",\"where\":\"Farhang-e Fārsī s.v. هیمه (MON_part2.txt l.92807)\",\"stance\":\"partial\",\"note\":\"'هیمه: hīma (ا.) هیزم.' Mo'in defines hīma only as a synonym of hīzum and gives it no origin tag, so the two words are equated in meaning but not etymologically.\"},\n      {\"src\":\"ARY\",\"where\":\"Aryanpur, Farhang-e Rishe-hā, pdf p.242 (printed 243)\",\"stance\":\"supports\",\"note\":\"Footnote 2 to the *aidh- root entry: '۲- واژه‌ی فارسی \\\"هیزم\\\" نیز از همین واجریشه است' ('the Persian word hīzom is also from this same root').\"},\n      {\"src\":\"CHEUNG\",\"where\":\"Etymological Dictionary of the Iranian Verb\",\"stance\":\"silent\",\"note\":\"Nominal stem, not a verb; no entry (Cheung covers verbal roots only).\"}\n     ]\n    },\n    {\n     \"id\":3,\"lang\":\"Avestan\",\"words\":\"ištya\",\"verdict\":\"plausible\",\n     \"derivation\":(\"Avestan ištiia-/ištya- n. 'brick, baked brick' is real and correctly glossed: Bartholomae AiW \"\n       \"'j. ištya- n. \\\"Ziegel, Backstein\\\"', attested at Vīdēvdād 8.8, with the cross-references 'Vgl. ai. \"\n       \"iṣṭakā- f., np. xišt'. The derivation from the burning-root is Johansson's (IF 19,136): *h₂eydʰ-s-t- \"\n       \"'that which is fired' > Indo-Iranian *išt(a)- with zero grade and loss of the dental before -s-, whence \"\n       \"Skt. iṣṭakā- 'burnt brick' and Av. ištya-. Pokorny 11-12 and Buck 604 print it; but Walde-Pokorny I 6 \"\n       \"already brackets Uhlenbeck's and Persson's alternative (*ais-t-), and current Indo-Iranian scholarship \"\n       \"(Lubotsky 1999; Schmitt 2018, cited on Wiktionary s.v. خشت) treats Proto-Indo-Iranian *išta-/*išti- \"\n       \"'brick' as a loan from the BMAC substrate, i.e. not from 'to burn' at all. Hence 'plausible' rather than \"\n       \"'confirmed' for the edge root->ištya.\"),\n     \"sources\":[XST, AIDH],\n     \"ref_check\":[\n      {\"ref\":\"POK:11\",\"status\":\"supports\",\"note\":\"Pokorny 11-12: 'to Johansson IF. 19,136 also Old Indic istaka \\\"of burnt bricks\\\", Avestan istya- n. \\\"brick, (baked brick)\\\"'. The page cited is right, though Pokorny flags the attribution as Johansson's.\"},\n      {\"ref\":\"HRN:108\",\"status\":\"supports\",\"note\":\"Horn p.108 (HRN.txt leaf 129) no.488: 'xšt \\\"Ziegel, Backstein\\\". aw. ištya- \\\"Ziegel, Backstein\\\"; phlv. xist; skr. iṣṭakā- \\\"Backstein\\\".' Exactly the chart's chain.\"},\n      {\"ref\":\"SYN:604\",\"status\":\"supports\",\"note\":\"Buck, Selected Synonyms p.604 (SYN.txt leaf 661), section 9.54 BRICK, para. 7: 'Skt. iṣṭakā-, Av. ištya-, OPers. išti- (Dar. Sus. f 29), NPers. xišt, prob. fr. *idh-s-to- : Skt. idh-, Grk. αἴθω \\\"kindle\\\", etc. Walde-P. 1.6, Johansson IF 19.136.' Nourai's page number is exact.\"}\n     ],\n     \"consulted\":[\n      {\"src\":\"BRT\",\"where\":\"AiW s.v. ištya- (BRT.txt l.8060)\",\"stance\":\"supports\",\"note\":\"'j. ištya- n. \\\"Ziegel, Backstein\\\": ... V.8.8. Vgl. ai. iṣṭakā- f., np. xišt.'\"},\n      {\"src\":\"WLD\",\"where\":\"Bd. I p.6 (WLD_Bd1_pages.txt leaf 15)\",\"stance\":\"partial\",\"note\":\"'nach Johansson IF. 19,136 auch ai. istaka \\\"gebrannter Ziegel\\\", av. istya- n. \\\"Ziegel, Backstein\\\" (Voraussetzung ist Schwund von Dentalen vor s im Indischen). [Nicht wahrscheinlicher erwägen Uhlenbeck ... und Persson ... Zurückführung dieser auf *(a)idh-s-t weisenden Worte vielmehr auf idg. ais-t- von der Wzf. *ai-s- neben *ai-dh-.]' — supports the material but records a rival root.\"},\n      {\"src\":\"IEC\",\"where\":\"Mann, 'aidhst-' (IEC.txt l.299)\",\"stance\":\"supports\",\"note\":\"'aidhst- (aidhəst-, əidh-) \\\"heat, burning, furnace, rage\\\". WP I,5 ... Av. istyo \\\"brick\\\"; Alb. ethe \\\"fever\\\"; Lat. aestus; aestas; MIr. áith \\\"kiln\\\"; ... OE ast; Du. eest \\\"oast\\\"' — groups Av. ištya- and Lat. aestus in one formation, as the chart does.\"},\n      {\"src\":\"AHD\",\"where\":\"Watkins 'aidh-'\",\"stance\":\"silent\",\"note\":\"Watkins lists no Indo-Iranian brick word under aidh-.\"}\n     ]\n    },\n    {\n     \"id\":4,\"lang\":\"Pahlavi\",\"words\":\"xišt\",\"verdict\":\"confirmed\",\n     \"derivation\":(\"Middle Persian xišt 'brick' (Book Pahlavi hšt') continues the Old Iranian word behind Av. ištya-/OP \"\n       \"išti- (Proto-Iranian *išti-/*ištya-). The initial x- is not from the ancestor: Pahlavi develops a prothetic \"\n       \"x- before an original word-initial vowel, and Hübschmann (Persische Studien p.265) lists xišt among exactly \"\n       \"these cases — 'xišt \\\"Ziegel\\\", phl. xist = zd. ištya-; xišm, xašm \\\"Zorn\\\" ... = zd. aēšma-; xēš \"\n       \"\\\"Pflug\\\" = zd. aēša-' — adding 'Hier ist x schon im Phl. vorgeschlagen worden'. Strictly the parent is \"\n       \"not the Avestan word itself (Avestan is not the ancestor of Persian) but its Old Iranian equivalent, best \"\n       \"represented by Old Persian išti- in node 6.\"),\n     \"sources\":[XST],\n     \"ref_check\":[{\"ref\":\"SNS:36\",\"status\":\"supports\",\"note\":\"Tavoosi, Vazhe-name-ye Shayast ne Shayast: the glossary index lists 'xist 36/1' (SNS.txt l.30695; entry text at SNS_pages.txt l.1214, OCR too poor to read in full), i.e. the Pahlavi word xist is registered in this Šāyast nē Šāyast glossary at the place Nourai cites. Whether '36' is the printed page or the text reference chapter/line could not be settled from the OCR.\"}],\n     \"consulted\":[\n      {\"src\":\"PHD\",\"where\":\"MacKenzie CPD s.v. xišt (PHD.txt l.661)\",\"stance\":\"supports\",\"note\":\"'xišt [hšt' | (P hystyg), N ~] brick.'\"},\n      {\"src\":\"HUB\",\"where\":\"Persische Studien p.265 (HUB.txt leaf 275) and p.236 (leaf 246)\",\"stance\":\"supports\",\"note\":\"p.265: 'xišt \\\"Ziegel\\\", phl. xist = zd. ištya- ... Hier ist x schon im Phl. vorgeschlagen worden'; p.236: 'xišt \\\"Ziegel\\\", skr. iṣṭakā-' (under np. št < Iranian št).\"},\n      {\"src\":\"NYB\",\"where\":\"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt)\",\"stance\":\"silent\",\"note\":\"grep for xist/xišt/ēzm returns only unrelated hits (existence, axistan); the word is not in Nyberg's glossary, which covers a limited text corpus.\"},\n      {\"src\":\"HRN\",\"where\":\"Horn p.108 no.488\",\"stance\":\"supports\",\"note\":\"'phlv. xist' cited as the intermediate between Av. ištya- and NP xšt.\"}\n     ]\n    },\n    {\n     \"id\":5,\"lang\":\"Persian\",\"words\":\"xešt 1 «خشت ۱»\",\"verdict\":\"confirmed\",\n     \"derivation\":(\"New Persian خشت xišt/xešt 'sun-dried brick, adobe; slab' is the regular continuation of MP xišt, \"\n       \"with no further change; cognate Pashto خښته xaṣ̱tah, Sanskrit iṣṭakā-. Horn no.488 (p.108) heads the \"\n       \"entry 'xšt \\\"Ziegel, Backstein\\\"' and Buck 604 lists 'NPers. xišt' in the BRICK table. The Hāfez couplet \"\n       \"quoted on the chart ('سر تسلیم من و خشت در میکده‌ها') uses it in the concrete sense 'brick (as a \"\n       \"pillow at the tavern door)'. Nourai's '1' is Mo'in's homonym number, distinguishing it from xešt 'javelin'.\"),\n     \"sources\":[XST],\n     \"ref_check\":[\n      {\"ref\":\"BQT:750\",\"status\":\"supports\",\"note\":\"Borhan-e Qate' vol.2 (BQT_v2_pages.txt leaf 209, printed ~751-752; the خش section opens at the foot of leaf 208, so Nourai's 750 is within the ±2-page uncertainty of the leaf->page mapping). Mo'in's footnote 1 on that page gives the etymology of خشت with Old Indic iṣṭakā-, Avestan ištya-, Old Persian išti-, Pahlavi xišt and an Armenian form — the same chain the chart draws.\"},\n      {\"ref\":\"SYN:604\",\"status\":\"supports\",\"note\":\"Buck p.604 §9.54 BRICK, para. 7: 'Skt. iṣṭakā-, Av. ištya-, OPers. išti- ..., NPers. xišt, prob. fr. *idh-s-to-'.\"}\n     ],\n     \"consulted\":[\n      {\"src\":\"HRN\",\"where\":\"p.108 no.488\",\"stance\":\"supports\",\"note\":\"'xšt \\\"Ziegel, Backstein\\\". aw. ištya-; phlv. xist; skr. iṣṭakā-.'\"},\n      {\"src\":\"HUB\",\"where\":\"p.236 and p.265\",\"stance\":\"supports\",\"note\":\"NP xišt derived from phl. xist = Av. ištya-, with the prothetic x- explained.\"},\n      {\"src\":\"MON\",\"where\":\"Farhang-e Fārsī (MON_part1.txt l.5313, 37079)\",\"stance\":\"partial\",\"note\":\"Mo'in has خشت in compounds ('خشت و آهک', 'خشت پخته، آجر بزرگ') confirming the sense 'brick'; the 2-volume abridgement on disk carries no etymological tag for it.\"},\n      {\"src\":\"BQT\",\"where\":\"vol.2 leaf 209\",\"stance\":\"supports\",\"note\":\"see ref_check.\"}\n     ]\n    },\n    {\n     \"id\":6,\"lang\":\"Old Persian\",\"words\":\"išti\",\"verdict\":\"plausible\",\n     \"derivation\":(\"Old Persian išti- f. 'sun-dried brick' is attested once, in the accusative ištim in Darius' Susa \"\n       \"foundation charter DSf 29 (the passage on how the palace was built of mud brick). Kent's lexicon (p.175) \"\n       \"glosses it exactly as Nourai does. It is the same Old Iranian word as Av. ištya- and the direct ancestor \"\n       \"of MP xišt, so on the chart it should really stand above node 4 rather than beside the Avestan branch. \"\n       \"As with node 3, its attachment to *h₂eydʰ- 'burn' is the Johansson/Pokorny/Buck analysis, now contested \"\n       \"in favour of a BMAC-substrate origin (Lubotsky, Schmitt).\"),\n     \"sources\":[XST],\n     \"ref_check\":[{\"ref\":\"KNT:175\",\"status\":\"supports\",\"note\":\"Kent, Old Persian, Lexicon p.175 (KNT.txt leaf 197, printed numeral '175' visible on the page): 'išti- sb. \\\"sun-dried brick\\\" (§152.II, §179.II): Av. ištya-, NPers. xišt, Skt. iṣṭakā-, Medieval Skt. iṣṭikā- (König, Burgbau 51-2; ...). ištim nsf. DSf 29.' Page number exact.\"}],\n     \"consulted\":[\n      {\"src\":\"SYN\",\"where\":\"Buck p.604 §9.54\",\"stance\":\"supports\",\"note\":\"'OPers. išti- (Dar. Sus. f 29)' — same attestation.\"},\n      {\"src\":\"TLM\",\"where\":\"Tolman, Ancient Persian Lexicon\",\"stance\":\"silent\",\"note\":\"not consulted in detail; Kent supersedes it and gives the same reading.\"},\n      {\"src\":\"BRT\",\"where\":\"AiW s.v. ištya-\",\"stance\":\"partial\",\"note\":\"Bartholomae covers the Avestan word and cites np. xišt but (being an Avestan dictionary of 1904) does not treat the DSf attestation.\"}\n     ]\n    },\n    {\n     \"id\":7,\"lang\":\"Greek\",\"words\":\"aithěr\",\"verdict\":\"confirmed\",\n     \"derivation\":(\"Ancient Greek αἰθήρ (aithḗr), gen. αἰθέρος, 'the upper, purer air; bright sky', already Homeric, \"\n       \"is an -ηρ formation on αἴθω 'I kindle, burn' — i.e. *h₂eydʰ-er-, literally 'the burning/blazing (air)'. \"\n       \"Beside it Greek has αἴθρα 'clear sky' and αἴθριος. Nourai's gloss '(hot) air' matches Pokorny's 'the \"\n       \"upper air'. In Aristotelian physics it becomes the fifth element filling the region above the sublunary \"\n       \"world — the sense that travels on into Arabic and Latin.\"),\n     \"sources\":[EO+\"ether\", AIDH],\n     \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins: 'aidh-. ... 5. Suffixed form *aidh-er- in Greek aithēr, air: AETHER, ETHER.'\"}],\n     \"consulted\":[\n      {\"src\":\"POK\",\"where\":\"Pokorny 11-12\",\"stance\":\"supports\",\"note\":\"'r-formants: gr. αἰθήρ \\\"the upper air\\\" (maked. ἀδη), αἴθρα \\\"the cheerful sky\\\", αἴθριος \\\"brightly, cheerfully (from the weather)\\\"'.\"},\n      {\"src\":\"KLN\",\"where\":\"Klein s.v. ether (leaf 297, ~p.570)\",\"stance\":\"supports\",\"note\":\"'L. aether, fr. Gk. αἰθήρ ... which, together with αἴθρα \\\"the clean sky, fair weather\\\", derives fr. αἴθειν, \\\"to burn\\\", fr. I.-E. base *aidh-'.\"},\n      {\"src\":\"SKT\",\"where\":\"Skeat s.v. Ether (SKT.txt l.6017)\",\"stance\":\"supports\",\"note\":\"'Ether, pure upper air. (L.—Gk.) L. aether. — Gk. αἰθήρ, upper air; from ... Gk. αἴθειν, to glow. (√IDH.)'\"}\n     ]\n    },\n    {\n     \"id\":8,\"lang\":\"Arabic\",\"words\":\"asîr\",\"verdict\":\"confirmed\",\n     \"derivation\":(\"Arabic أَثِير (ʾaṯīr) 'ether, the upper air' is the Greek αἰθήρ taken over by the Baghdad \"\n       \"translators of Aristotle (De caelo, Meteorologica) in the 9th century, for the fifth element above the \"\n       \"sphere of fire; the form is a phono-semantic match, the Greek shape being fitted to the native pattern \"\n       \"faʿīl of the root ʾ-ṯ-r (which independently gives ʾaṯīr 'preferred, noble'). Al-ʿAnaysī's dictionary of \"\n       \"foreign words in Arabic states the Greek origin outright. Nourai's gloss 'ether filling beyond the \"\n       \"atmosphere' is the Aristotelian/scholastic sense.\"),\n     \"sources\":[ATIR],\n     \"ref_check\":[{\"ref\":\"TAD:1\",\"status\":\"supports\",\"note\":\"Tobia al-ʿAnaysī, Tafsīr al-alfāẓ al-dākhila, p.1 (TAD_pages.txt leaf 4, the first page of the alif section): 'اثير - يوناني [aiθήρ] ومعناه احترق ولمع ... وعند الشعراء الهواء والسماء ... يزعمون انها منتشرة في الكون والمادة المحسوسة غاطسة فيها'. Exactly Nourai's arrow and gloss; page number exact.\"}],\n     \"consulted\":[\n      {\"src\":\"KLN\",\"where\":\"Klein s.v. ether\",\"stance\":\"partial\",\"note\":\"Klein traces the European word to Greek but says nothing about the Arabic transmission.\"},\n      {\"src\":\"FVQ\",\"where\":\"Jeffery, Foreign Vocabulary of the Qur'an\",\"stance\":\"silent\",\"note\":\"grep for أثير finds nothing — the word is post-Qur'anic, so Jeffery has no entry.\"},\n      {\"src\":\"PLA\",\"where\":\"Asbaghi, Persische Lehnwörter im Arabischen\",\"stance\":\"silent\",\"note\":\"no entry (grep of the djvu text): the word is a Greek, not a Persian, loan in Arabic — consistent with Nourai's Greek->Arabic arrow.\"},\n      {\"src\":\"AFM\",\"where\":\"Addi Shir, al-Alfāẓ al-Fārisiyya al-muʿarraba\",\"stance\":\"silent\",\"note\":\"no entry; again consistent with a Greek rather than Persian source.\"}\n     ]\n    },\n    {\n     \"id\":9,\"lang\":\"Persian\",\"words\":\"asîr «اثیر»\",\"verdict\":\"confirmed\",\n     \"derivation\":(\"Persian اثیر asīr is the Arabic ʾaṯīr re-borrowed into Persian with the philosophical vocabulary of the \"\n       \"Islamic sciences: 'the sphere of fire above the sphere of air', hence چرخ اثیر 'the fiery sphere'. Persian \"\n       \"keeps the Arabic spelling with ث and pronounces it [asīr]. Mo'in explicitly tags the entry [معر.] \"\n       \"(muʿarrab, i.e. an Arabicized/Arabic-mediated word), which is exactly the Greek > Arabic > Persian \"\n       \"round-trip the chart draws. The Molavī line quoted ('همچو آن مستی که پرّد بر اثیر') uses it in that \"\n       \"cosmological sense.\"),\n     \"sources\":[ATIR],\n     \"ref_check\":[{\"ref\":\"MON:143\",\"status\":\"supports\",\"note\":\"Mo'in, Farhang-e Fārsī s.v. اثیر (checked in the 2-vol Adena abridgement, MON_part1.txt l.7178, since the 6-vol pagination is not mappable online): 'اثیر: [معر.] (ا.) کرهٔ آتش که بالای کرهٔ هوا است، سیالی رقیق و تنک و بی‌وزن ... اتر. چرخ اثیر: کرهٔ آتش، فلک نار'. The tag [معر.] and the cross-reference to اتر are Nourai's claim exactly; the volume/page 143 could not be verified because only the abridged edition is on disk.\"}],\n     \"consulted\":[\n      {\"src\":\"BQT\",\"where\":\"Borhan-e Qate'\",\"stance\":\"silent\",\"note\":\"اثیر is a learned Arabic word; not a headword of the Borhān in the volumes searched.\"},\n      {\"src\":\"MON\",\"where\":\"MON_part1.txt l.7178\",\"stance\":\"supports\",\"note\":\"see ref_check; Mo'in marks it muʿarrab and equates it with اتر.\"},\n      {\"src\":\"RCH\",\"where\":\"Richardson, Persian-Arabic-English Dictionary\",\"stance\":\"silent\",\"note\":\"not searched in detail; the Arabic origin is not in doubt.\"}\n     ]\n    },\n    {\n     \"id\":10,\"lang\":\"Latin\",\"words\":\"aethěr, aither\",\"verdict\":\"confirmed\",\n     \"derivation\":(\"Latin aethēr, -eris m. is a straight borrowing of Greek αἰθήρ (not an inherited cognate), current from \"\n       \"Ennius and Lucretius on for the fiery upper air; Ernout-Meillet note that the attempt made since Pacuvius \"\n       \"to latinise it (with a native equivalent) did not succeed, and it kept a Greek declension. The chart's \"\n       \"second form 'aither' is simply the Greek spelling as used in Latin texts. The arrow Greek -> Latin is \"\n       \"therefore a borrowing, correctly drawn.\"),\n     \"sources\":[EO+\"ether\"],\n     \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 'aidh-' 5: 'Greek aithēr, air: AETHER, ETHER' — the English words come through Latin aether.\"}],\n     \"consulted\":[\n      {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. aether (LAT.txt l.1746)\",\"stance\":\"supports\",\"note\":\"'... en revanche, l'effort fait depuis Pacuvius pour latiniser aether n'a [pas abouti]' — treated as a Greek word in Latin.\"},\n      {\"src\":\"KLN\",\"where\":\"Klein s.v. ether\",\"stance\":\"supports\",\"note\":\"'L. aether, fr. Gk. αἰθήρ'.\"},\n      {\"src\":\"SKT\",\"where\":\"Skeat s.v. Ether\",\"stance\":\"supports\",\"note\":\"'(L. — Gk.) L. aether. — Gk. αἰθήρ'.\"}\n     ]\n    },\n    {\n     \"id\":11,\"lang\":\"French\",\"words\":\"ether\",\"verdict\":\"confirmed\",\n     \"derivation\":(\"French éther continues Latin aether (learned borrowing, attested in the cosmological sense from the \"\n       \"13th-16th c.). The chemical sense that matters for the Persian loan is younger: the volatile liquid was \"\n       \"named aether by August Sigmund Frobenius in 1730, the name passing at once into French éther and English \"\n       \"ether; the anaesthetic use dates from 1842. It is this 18th-19th c. chemical term, not the cosmological \"\n       \"one, that reaches Persian in node 12. The chart gives no gloss for the French box.\"),\n     \"sources\":[ETHR, EO+\"ether\"],\n     \"ref_check\":[{\"ref\":\"MON:134\",\"status\":\"supports\",\"note\":\"Mo'in's entry اتر (MON_part1.txt l.6768) is tagged as a European (French) borrowing and defines it in physics and chemistry terms ('بخار رقیق و مادهٔ سیال و سریع التسخیری ... (شیم.) ماده‌ای که از گرفتن یک مولکول آب از دو مولکول الکل حاصل شود؛ اتر اکسید'), i.e. the French chemical term. Page 134 itself could not be checked (only the abridged 2-vol edition is on disk), but it precedes اثیر (MON:143) alphabetically, as it must.\"}],\n     \"consulted\":[\n      {\"src\":\"KLN\",\"where\":\"Klein s.v. ether\",\"stance\":\"supports\",\"note\":\"'As a chemical term, the word aether was coined by August Sigmund Frobenius (in 1730), the discoverer of this liquid.'\"},\n      {\"src\":\"DEV\",\"where\":\"Devic, Dictionnaire étymologique des mots français d'origine orientale\",\"stance\":\"silent\",\"note\":\"no entry — correctly, since French éther is from Latin/Greek, not from an oriental language.\"}\n     ]\n    },\n    {\n     \"id\":12,\"lang\":\"Persian\",\"words\":\"eter «اثر»\",\"verdict\":\"transcription_suspect\",\n     \"derivation\":(\"The word itself is right: Persian اتر eter is the modern chemistry term borrowed from French éther \"\n       \"(diethyl ether), distinct from the older Arabic-mediated اثیر asīr of node 9, and Mo'in's entry اتر \"\n       \"explicitly cross-refers to اثیر. But the Persian script in the JSON is wrong: the book prints اتر \"\n       \"(alef + tāʾ + rāʾ), which I read directly off the page rendered at 600 dpi from \"\n       \"EtymologicalDictionary-persian-english.pdf p.39; the extraction has «اثر» with thāʾ (three dots) instead \"\n       \"of tāʾ (two dots). اثر would be Arabic aṯār/aṯar 'trace, effect', a different word altogether, and it \"\n       \"contradicts the chart's own transliteration 'eter'. The extracted script should be corrected to اتر.\"),\n     \"sources\":[ETHR],\n     \"ref_check\":[{\"ref\":\"MON:134\",\"status\":\"supports\",\"note\":\"Mo'in s.v. اتر (MON_part1.txt l.6768-6784), a European loan defined in physics and chemistry and ending '؛ اثیر' — the headword is spelled اتر, never اثر, which is independent confirmation that the JSON's «اثر» is a misreading.\"}],\n     \"consulted\":[\n      {\"src\":\"MON\",\"where\":\"MON_part1.txt l.6768\",\"stance\":\"supports\",\"note\":\"headword اتر, chemical/physical senses, cross-reference اثیر.\"},\n      {\"src\":\"BQT\",\"where\":\"Borhan-e Qate'\",\"stance\":\"silent\",\"note\":\"a 20th-century European loan; not in a 17th-century dictionary.\"}\n     ]\n    },\n    {\n     \"id\":13,\"lang\":\"Germanic\",\"words\":\"ail\",\"verdict\":\"plausible\",\n     \"derivation\":(\"'ail' is not an attested word but Watkins' reconstructed Germanic stem *ail-, from a suffixed \"\n       \"*h₂eydʰ-lo-; its attested continuations are Old English āl 'fire, flame' and the verb ǣlan 'to burn, \"\n       \"kindle', plus OE ǣled 'fire, firebrand', Old Norse eldr 'fire', Danish ild. Pokorny 11-12 puts it the same \"\n       \"way: 'In Indo-Germanic *aidh-lo- is based Germanic ail- in Old English ǣlan \\\"burn\\\" to āl \\\"flame\\\", and in \"\n       \"Old English ǣled, Old Icelandic eldr \\\"fire, flame\\\"'. Two reservations: Watkins himself writes 'perhaps' \"\n       \"for this Germanic branch, and Etymonline assigns ǣlan/anneal instead to PIE *as- 'to burn, glow' (the \"\n       \"root Nourai calls 'Es 1' and merges into this same box). The gloss 'fire' is right for āl.\"),\n     \"sources\":[EO+\"anneal\", AIDH],\n     \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 'aidh-' 2: 'Suffixed form *aidh-lo- perhaps in Germanic *ail- in Old English āl, fire: ANNEAL.' The hedge 'perhaps' is Watkins' own.\"}],\n     \"consulted\":[\n      {\"src\":\"POK\",\"where\":\"Pokorny 11-12\",\"stance\":\"supports\",\"note\":\"'In Indo Germanic *aidh-lo- is based Germanic ail- in Old English ǣlan \\\"burn\\\" to āl \\\"flame\\\", and in Old English ǣled ..., Old Icelandic eldr (Gen. elds) \\\"fire, flame\\\".'\"},\n      {\"src\":\"WLD\",\"where\":\"Bd. I p.5-6\",\"stance\":\"supports\",\"note\":\"same material under 'Auf idg. *aidh-lo- oder einer Kreuzung von aidh- mit *aleto-'.\"},\n      {\"src\":\"IEC\",\"where\":\"Mann, 'aidhlos, aidholos' (IEC.txt l.287)\",\"stance\":\"supports\",\"note\":\"'aidhlos, aidholos \\\"burning; consumption\\\". WP I,5 ... OS ēld; OE āl; ON eldr \\\"fire\\\"; OE ǣled, obl. ǣld, id.'\"}\n     ]\n    },\n    {\n     \"id\":14,\"lang\":\"English\",\"words\":\"anneal\",\"verdict\":\"confirmed\",\n     \"derivation\":(\"Old English onǣlan 'to set on fire, kindle' (on- + ǣlan 'to burn', to āl 'fire') > Middle English \"\n       \"anelen > anneal. The technical sense 'temper by heating and slow cooling' is already late Old English \"\n       \"(of glass, tiles and metals). Klein adds that the Middle English and modern form were reshaped under an \"\n       \"erroneous association with Old French neeler (> nieller) 'to blacken', from Vulgar Latin *nigellāre — \"\n       \"which is why the modern word has -nn-. The chart supplies no gloss for the English box.\"),\n     \"sources\":[EO+\"anneal\"],\n     \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"Nourai gives no reference for this node; the parent box carries AHD, and Watkins' aidh- entry ends the branch with 'ANNEAL'.\"}],\n     \"consulted\":[\n      {\"src\":\"KLN\",\"where\":\"Klein s.v. anneal (KLN_1966.txt leaf 53, ~p.82)\",\"stance\":\"supports\",\"note\":\"'ME. anelen, fr. OE. anǣlan, \\\"to burn, kindle\\\", fr. an, \\\"on\\\", and ǣlan, \\\"to kindle, burn\\\", which is rel. to OE. āl, \\\"fire\\\", ǣled, \\\"fire, firebrand\\\". ME. anelen and E. anneal were influenced in form by an erroneous association with OF. neeler ...'\"},\n      {\"src\":\"WEB\",\"where\":\"Webster's New Twentieth Century (WEB_vol1.txt l.7986)\",\"stance\":\"supports\",\"note\":\"'anneal ... [ME. anelen, onelen; AS. anǣlan, onǣlan, to burn; an, on, and ǣlan, to burn, set on fire; āl, ǣl, fire.]'\"},\n      {\"src\":\"SKT\",\"where\":\"Skeat, Supplement (SKT.txt l.21842)\",\"stance\":\"partial\",\"note\":\"'Anneal. Perhaps the A.S. words should be onǣlan and ǣlan with long ǣ ...' — a note on vowel quantity, not on the derivation.\"},\n      {\"src\":\"FSD\",\"where\":\"Funk & Wagnalls (FSD_vol1.txt l.17129)\",\"stance\":\"supports\",\"note\":\"defines annealing as 'gradually heating and gradually cooling glass, metals, or other substances to reduce brittleness'.\"}\n     ]\n    },\n    {\n     \"id\":15,\"lang\":\"Latin\",\"words\":\"asetus\",\"verdict\":\"plausible\",\n     \"derivation\":(\"The Latin word is aestus, -ūs m. 'heat, seething, surge, tide' < *h₂eydʰ-s-tu-, beside aestās \"\n       \"'summer' < *aidh-s-tāt- and aestuāre 'to seethe, boil'. Nourai's gloss 'burning heat' is accurate but the \"\n       \"printed form 'asetus' is a metathesis-misprint for aestus: I checked the page image itself (600 dpi render \"\n       \"of the source PDF, p.39) and the book really prints 'asetus', so this is Nourai's own typo, not an \"\n       \"extraction error — which is why the verdict is 'plausible' rather than 'transcription_suspect'.\"),\n     \"sources\":[EO+\"estuary\", AIDH],\n     \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"Nourai gives no reference for this box; the root box's AHD covers it (Watkins 'aidh-' 4: 'Suffixed form *aidh-stu- in Latin aestus, heat, swell, surge, tide: ESTUARY').\"}],\n     \"consulted\":[\n      {\"src\":\"WLD\",\"where\":\"Bd. I p.5\",\"stance\":\"supports\",\"note\":\"'*aidh-s-t- in: lat. aestās, -ātis \\\"warme Jahreszeit, Sommer\\\", aestus, -ūs \\\"Hitze und dadurch bewirkte Wallung\\\", aestuare \\\"infolge Hitze wallen, brausen\\\"'.\"},\n      {\"src\":\"POK\",\"where\":\"Pokorny 11-12\",\"stance\":\"supports\",\"note\":\"'aestus (from *aidh-tu-) \\\"heat, glow, surf\\\", aestuare \\\"cook, surge, roar\\\"'.\"},\n      {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. aestas/aestus (LAT.txt l.1864 ff.)\",\"stance\":\"supports\",\"note\":\"'aestas, -atis f.; aestus, -us m. Cf. aedes' ... 'aestus: chaleur brûlante, provenant d'une substance enflammée' — the same family as aedes/gr. αἴθω. The headword is aestus; no Latin word 'asetus' exists.\"},\n      {\"src\":\"IEC\",\"where\":\"Mann, 'aidhst-'\",\"stance\":\"supports\",\"note\":\"'Lat. aestus; aestas' listed under the *aidh-s-t- formation.\"}\n     ]\n    },\n    {\n     \"id\":16,\"lang\":\"English\",\"words\":\"estuary\",\"verdict\":\"confirmed\",\n     \"derivation\":(\"Latin aestuārium 'tidal channel, tidal marsh, inlet' (a derivative of aestuāre 'to surge', from \"\n       \"aestus 'boiling of the sea, tide'), borrowed into English in the 1530s as estuary in the sense 'tidal \"\n       \"inlet, mouth of a river where the tide meets the current'. The semantic thread is 'boiling/heat' > \"\n       \"'seething of the sea' > 'tide' > 'tidal channel'. No French intermediary is needed. The chart gives no \"\n       \"gloss for the English box.\"),\n     \"sources\":[EO+\"estuary\"],\n     \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference given by Nourai; Watkins ends the aidh- branch with 'ESTUARY' and the alphabetical index of AHD_watkins1985.txt has 'ESTUARY aidh-'.\"}],\n     \"consulted\":[\n      {\"src\":\"KLN\",\"where\":\"Klein s.v. estuary (KLN_1966.txt leaf 296, ~p.568)\",\"stance\":\"supports\",\"note\":\"'estuary, n., broad mouth of a river. — L. aestuarium, \\\"a tideplace, an estuary\\\", fr. aestus, \\\"heat, fire, the ebb and flow of the sea, tide\\\".'\"},\n      {\"src\":\"SKT\",\"where\":\"Skeat s.v. Estuary (SKT.txt l.6014)\",\"stance\":\"supports\",\"note\":\"'Estuary, mouth of a tidal river. (L.) L. aestuarium ... L. aestuare, to surge, foam as the tide. — L. aestus, heat, surge, tide. (√IDH.)'\"},\n      {\"src\":\"WEB\",\"where\":\"Webster's New Twentieth Century\",\"stance\":\"silent\",\"note\":\"grep of the OCR'd volume did not return a clean 'estuary' headword line (OCR damage); Klein and Skeat cover it.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 3,\n   \"root\": \"Aig-\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *h₂eyǵ- 'goat' (Pokorny 13 '3. aiǵ-'; Walde-Pokorny I 8)\",\n   \"note\": (\"The root name and gloss are right, but the page reference is not, and it exposes a conflation. \"\n     \"Pokorny's aiǵ- 'Ziege' is on p.13 and contains only Gr. αἴξ, Arm. ayc and Av. izaēna- 'of leather'; \"\n     \"the material Nourai puts in the Iranian branch — 'Middle Persian azak \\\"goat\\\", npers. azg' — stands on \"\n     \"pp.6-7 under a DIFFERENT root, aǵ- 'goat' (Skt. ajá-ḥ, Lith. ožys, Alb. dhi, OCS (j)azno 'hide'), \"\n     \"whose entry ends 'References: WP. I 38 ... compare also aig-'. So POK:6 is genuinely where Nourai found \"\n     \"azak/azg, but it is not the page for the root 'Aig-'. Walde-Pokorny keeps the same two entries apart \"\n     \"(aiǵ- I 8, aǵos- I 38, the latter with 'mp. azak \\\"Ziege\\\", np. asg'), and Watkins gives only \"\n     \"'aig-. Goat. Greek aigis, goatskin: AEGIS. [Pok. 3. aig- 13.]' with no Iranian at all. Horn (no.42, \"\n     \"p.269) and Klein (p.30) do unite the two families ('dazu wohl auch arm. aic, gr. αἴξ und aw. izaēna-'), \"\n     \"and Wiktionary observes that the *h₂eǵ-/*h₂eyǵ- alternation 'could suggest a substratum loan', so the \"\n     \"merger is defensible as a hypothesis — but as drawn, with Pahlavi azak descending from Avestan iza, it is \"\n     \"phonologically impossible (Iranian i- cannot become a-). A second, smaller point: the Avestan box's first \"\n     \"word 'iza : goat' is not an attested Avestan noun; only the adjective izaēna- 'leathern' exists.\"),\n   \"sources\": [AIG, AG, AIX],\n   \"ref_check\": [\n    {\"ref\":\"POK:6\",\"status\":\"partial\",\"note\":\"Pokorny pp.6-7 (POK_full.txt 'Root/lemma: ag-', Meaning: goat, Page(s): 6-7): 'Old Indic ajá-ḥ \\\"he-goat\\\", ajā \\\"she-goat\\\", Middle Persian azak \\\"goat\\\", npers. azg ds.; alb. dhi \\\"goat\\\"; Lithuanian ožys ... Church Slavic (j)azno \\\"skin, leather\\\". References: WP. I 38, Trautmann 22. compare also aig-.' It does support the words azak/azg, but under root aǵ-, not under aiǵ- (which is on p.13: 'Gr. αἴξ \\\"nanny goat\\\", Armenian ayc; zero grade Avestan izaena- \\\"from leather\\\"'). So the citation is right for the Iranian words and wrong for the root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\":1,\"lang\":\"Avestan\",\"words\":\"iza; izaenem\",\"verdict\":\"plausible\",\n     \"derivation\":(\"What Avestan actually has is the adjective izaēna- (fem. izaēnī-) 'made of leather, leathern', \"\n       \"acc. sg. n. izaēnəm, attested at Vīdēvdād 6.23 and 7.14 of leather garments; Nourai's 'izaenem' is that \"\n       \"accusative and his gloss 'pertaining to (goat) skin' is accurate. His first word 'iza : goat' is not an \"\n       \"attested Avestan word: Bartholomae derives izaēna- from a noun *iz-/*izā- 'Leder' and marks the etymology \"\n       \"'Et?', comparing Gr. αἴξ and Arm. ayc. The step from 'goat' to 'goat-leather' is the same as in Gr. \"\n       \"αἴγειος 'of a goat' (Pokorny 13: 'zero grade Avestan izaena- \\\"from leather\\\" (actually \\\"from goatskin\\\")'). \"\n       \"Phonologically izaēna- < *iz-aina- with the zero grade of *h₂eyǵ-, which is why Pokorny calls it \"\n       \"'tiefstufig'.\"),\n     \"sources\":[AIG, AIX],\n     \"ref_check\":[\n      {\"ref\":\"POK:6\",\"status\":\"not_found\",\"note\":\"Pokorny pp.6-7 (root aǵ-) does not mention izaēna- at all; the Avestan word is on p.13 under aiǵ-: 'zero grade Avestan izaena- \\\"from leather\\\" (actually \\\"from goatskin\\\" as gr. αἰγέος ...)'. Right material, wrong page.\"},\n      {\"ref\":\"KLN:30\",\"status\":\"supports\",\"note\":\"Klein s.v. aego- (KLN_1966.txt leaf 28, ~p.32; Nourai's 30 is within the ±2-page tolerance of the leaf-to-page formula): 'Gk. αἰγο-, fr. αἴξ, gen. αἰγός, \\\"goat\\\", which is cogn. with OI. ajaḥ, \\\"he-goat\\\", ajinam, \\\"skin\\\", Avestic izaēnəm, \\\"pertaining to skin\\\", Arm. aic, \\\"goat\\\", Lith. ožys, \\\"he-goat\\\".' Klein's 'izaēnəm' and gloss are word-for-word Nourai's second entry.\"}\n     ],\n     \"consulted\":[\n      {\"src\":\"BRT\",\"where\":\"AiW s.v. izaēna- (BRT.txt l.8002)\",\"stance\":\"partial\",\"note\":\"'Adj. (fem. °nī-) \\\"aus Leder, ledern\\\": vāstrəm ... V.6.23; ... V.7.14. Ableit. aus *iz- oder *izā- \\\"Leder\\\". — Et? Man vergleicht gr. αἴξ, arm. aic; s. zuletzt Hübschmann AGr. I 417.' Confirms the adjective and its meaning, but the base noun means 'leather', not 'goat', and Bartholomae leaves the etymology open.\"},\n      {\"src\":\"WLD\",\"where\":\"Bd. I p.8 (WLD_Bd1_pages.txt leaf 17)\",\"stance\":\"supports\",\"note\":\"'aiǵ- \\\"Ziege\\\" ... Gr. αἴξ, -γός \\\"Ziege\\\", arm. aic \\\"Ziege\\\"; tiefstufig ... av. izaena- oder īzaena- \\\"aus Leder\\\" (eigentlich \\\"aus Ziegenleder\\\" wie gr. αἴγειος)'.\"},\n      {\"src\":\"IEC\",\"where\":\"Mann, 'aigis' (IEC.txt l.305)\",\"stance\":\"partial\",\"note\":\"'aigis \\\"kid, goat\\\". WP I,8. Skt. cf. aja; Arm. ajc; Phryg. aizi-; Myc. aiki-; Gk. as gs. aigós; EMAlb. edh; Li. cf. ožys' — Mann too runs the two families together, and lists no Avestan or Iranian form.\"},\n      {\"src\":\"AHD\",\"where\":\"Watkins 'aig-' (AHD_watkins1985.txt l.272)\",\"stance\":\"silent\",\"note\":\"'aig-. Goat. Greek aigis, goatskin (shield of Athena): AEGIS. [Pok. 3. aig- 13.]' — no Iranian material of any kind.\"}\n     ]\n    },\n    {\n     \"id\":2,\"lang\":\"Pahlavi\",\"words\":\"azak\",\"verdict\":\"disputed\",\n     \"derivation\":(\"Middle Persian azag 'goat' is a real word (Pokorny 6-7 'Middle Persian azak \\\"goat\\\"'; Walde-Pokorny \"\n       \"I 38 'mp. azak \\\"Ziege\\\"'), but it does not come from Avestan iza-/izaēna-. It continues Proto-Iranian \"\n       \"*aza-ka-, the -ka- diminutive/individualising suffix on *aza- 'goat', which is *h₂eǵ-o- — the root of \"\n       \"Skt. ajá-ḥ 'he-goat', ajā́ 'she-goat', Lith. ožys, Latv. āzis, Alb. dhi, OCS (j)azno 'hide'. Iranian \"\n       \"i- cannot yield a-, so the arrow iza -> azak is impossible as drawn; Pokorny prints the two roots as \"\n       \"separate entries seven pages apart and only adds 'compare also aig-'. The older comparative tradition \"\n       \"(Horn 1893 no.42; Klein 1966 s.v. aego-) did unite them, and Wiktionary notes that the *h₂eǵ-/*h₂eyǵ- \"\n       \"alternation may point to a shared non-Indo-European source; but on any account azak belongs to the a-root, \"\n       \"not to the ai-root the chart puts it under. MacKenzie's Concise Pahlavi Dictionary does not have azag at \"\n       \"all (its word for 'goat' is buz), so the Middle Persian form rests on the Pahlavi-Pāzand glossary \"\n       \"tradition.\"),\n     \"sources\":[AG, AIG],\n     \"ref_check\":[{\"ref\":\"POK:6\",\"status\":\"partial\",\"note\":\"Pokorny pp.6-7, root aǵ- 'goat': 'Old Indic ajá-ḥ \\\"he-goat\\\", ajā \\\"she-goat\\\", Middle Persian azak \\\"goat\\\", npers. azg ds.' — the page does give azak with this meaning, so it supports the word; it contradicts the chart on the root, since this is Pokorny's aǵ-, not aiǵ- (p.13).\"}],\n     \"consulted\":[\n      {\"src\":\"WLD\",\"where\":\"Bd. I p.38 (WLD_Bd1_pages.txt leaf 47)\",\"stance\":\"contradicts\",\"note\":\"'aǵo-s, aǵi- \\\"Ziegenbock, Ziege\\\". Ai. ajá-ḥ \\\"Ziegenbock\\\", ajā \\\"Ziege\\\", mp. azak \\\"Ziege\\\", np. asg ds.; lit. ožys ...; alb. dhi \\\"Ziege\\\"; ai. ajina-m \\\"Fell\\\" ...; ksl. (j)azno \\\"Haut, Leder\\\".' Walde-Pokorny puts azak under aǵ-, thirty pages away from aiǵ- (I 8).\"},\n      {\"src\":\"PHD\",\"where\":\"MacKenzie, Concise Pahlavi Dictionary\",\"stance\":\"silent\",\"note\":\"no headword azag/azak; MacKenzie's 'goat' is 'buz [AZ < A ʿz; bwc | N ~] goat' (PHD.txt l.256). The word is thus not part of MacKenzie's core Book-Pahlavi vocabulary.\"},\n      {\"src\":\"NYB\",\"where\":\"Nyberg, Manual of Pahlavi II Glossary\",\"stance\":\"silent\",\"note\":\"grep for azak/azag returns only bazak 'misdeed' and similar; no entry.\"},\n      {\"src\":\"HRN\",\"where\":\"Horn no.42, p.269 (HRN.txt leaf 290)\",\"stance\":\"partial\",\"note\":\"'42. azg (d.i. azak) \\\"Ziege\\\" (PPGl.). ai. ajá \\\"Bock\\\", ajā \\\"Ziege\\\"; lit. ožys, lett. āzis \\\"Ziegenbock\\\", ožka \\\"Ziege\\\". Dazu wohl auch arm. aic (H. No.16), gr. αἴξ und aw. izaēna- \\\"aus (Ziegen)fell(?), ledern\\\".' Horn derives azak/azg from the ajá-/ožys family and only tentatively ('wohl auch') attaches αἴξ and izaēna- to it — i.e. the reverse direction of Nourai's arrow.\"},\n      {\"src\":\"KLN\",\"where\":\"Klein s.v. aego- (~p.32)\",\"stance\":\"partial\",\"note\":\"Klein likewise lists OI ajaḥ, Av. izaēnəm, Arm. aic and Lith. ožys as one set of cognates, but names no Iranian azak.\"}\n     ]\n    },\n    {\n     \"id\":3,\"lang\":\"Persian\",\"words\":\"azg «ازگ ۲»\",\"verdict\":\"plausible\",\n     \"derivation\":(\"The step Pahlavi azak > New Persian azg is regular (loss of the final -ak vowel with retention of \"\n       \"the consonant cluster, as in Horn's own equation 'azg (d.i. azak)'), so the immediate arrow is sound; what \"\n       \"is wrong is the root the whole branch hangs from (see node 2). Horn no.42 (p.269) marks the word as known \"\n       \"only from the Pahlavi-Pāzand glossary ('PPGl.'), and Walde-Pokorny I 38 prints it 'np. asg', which is \"\n       \"why Nourai's own note 'This word is apparently obsolete' is correct: azg is a lexicographers' word, not \"\n       \"current New Persian (the living word for 'goat' is بز buz). Mo'in's numbering «ازگ ۲» distinguishes it \"\n       \"from a homonym.\"),\n     \"sources\":[AG],\n     \"ref_check\":[{\"ref\":\"POK:6\",\"status\":\"partial\",\"note\":\"Pokorny pp.6-7 under aǵ-: 'Middle Persian azak \\\"goat\\\", npers. azg ds.' — supports the Pahlavi->Persian step verbatim, but again under root aǵ-, not aiǵ-.\"}],\n     \"consulted\":[\n      {\"src\":\"HRN\",\"where\":\"Horn no.42, p.269\",\"stance\":\"supports\",\"note\":\"'42. azg (d.i. azak) \\\"Ziege\\\" (PPGl.)' — Horn equates the New Persian and Pahlavi forms and gives the Pahlavi-Pāzand glossary as the only source, which corroborates Nourai's 'apparently obsolete'.\"},\n      {\"src\":\"WLD\",\"where\":\"Bd. I p.38\",\"stance\":\"supports\",\"note\":\"'mp. azak \\\"Ziege\\\", np. asg ds.' (Walde-Pokorny's transliteration asg for azg).\"},\n      {\"src\":\"BQT\",\"where\":\"Borhan-e Qate' vol.1 (BQT_v1_pages.txt)\",\"stance\":\"silent\",\"note\":\"a grep for ازگ over the whole volume returns only incidental hits inside other words (leaves 17, 552, 638), none in the alif section where a headword ازگ would stand — consistent with the word being obsolete, though the Persian OCR of this scan is poor.\"},\n      {\"src\":\"MON\",\"where\":\"Farhang-e Fārsī\",\"stance\":\"silent\",\"note\":\"no ازگ headword found in the 2-vol abridgement on disk; Nourai's homonym number '۲' implies the 6-vol edition has one.\"}\n     ]\n    },\n    {\n     \"id\":4,\"lang\":\"Greek\",\"words\":\"aigis\",\"verdict\":\"confirmed\",\n     \"derivation\":(\"Ancient Greek αἰγίς, -ίδος f. 'goatskin; the goatskin shield/aegis of Zeus and Athena' is built with \"\n       \"the -ίς/-ίδος suffix on αἴξ, gen. αἰγός 'goat'; the connection with the goat was already the \"\n       \"ancient explanation (Herodotus 4.189 on the Libyan goatskin aprons). αἴξ itself goes back to Proto-Hellenic \"\n       \"*aíks < *h₂eyǵ-, with Old Armenian այծ (ayc) as the nearest cognate. Nourai's gloss 'goat skin' is exact.\"),\n     \"sources\":[AIX, AIG],\n     \"ref_check\":[\n      {\"ref\":\"POK:6\",\"status\":\"not_found\",\"note\":\"Gr. αἴξ/aigis is not on Pokorny pp.6-7 (root aǵ-); it is on p.13 under aiǵ-: 'Gr. αἴξ, -γός \\\"nanny goat\\\", Armenian ayc \\\"nanny goat\\\"'.\"},\n      {\"ref\":\"KLN:30\",\"status\":\"supports\",\"note\":\"Klein s.v. aegis (KLN_1966.txt leaf 28, ~p.32): 'L. aegis, fr. Gk. αἰγίς, \\\"goatskin; the skin shield of Zeus\\\", fr. αἴξ, gen. αἰγός, \\\"goat\\\"; see aego-. For this etymology, suggested already by Herodotus, see Frisk, GEW., I, p.32 s.v. αἴξ.'\"}\n     ],\n     \"consulted\":[\n      {\"src\":\"POK\",\"where\":\"Pokorny p.13\",\"stance\":\"supports\",\"note\":\"aiǵ- 'goat' with Gr. αἴξ and Arm. ayc as the core evidence.\"},\n      {\"src\":\"WLD\",\"where\":\"Bd. I p.8\",\"stance\":\"supports\",\"note\":\"'Gr. αἴξ, -γός \\\"Ziege\\\", arm. aic \\\"Ziege\\\"'.\"},\n      {\"src\":\"AHD\",\"where\":\"Watkins 'aig-'\",\"stance\":\"supports\",\"note\":\"'aig-. Goat. Greek aigis, goatskin (shield of Athena): AEGIS.'\"},\n      {\"src\":\"IEC\",\"where\":\"Mann, 'aigis' (IEC.txt l.305)\",\"stance\":\"supports\",\"note\":\"'aigis \\\"kid, goat\\\". WP I,8 ... Gk. as gs. aigós'.\"}\n     ]\n    },\n    {\n     \"id\":5,\"lang\":\"English\",\"words\":\"aego-\",\"verdict\":\"confirmed\",\n     \"derivation\":(\"aego- is not an inherited English word but a learned combining form taken straight from the Greek \"\n       \"stem αἰγο- (of αἴξ, gen. αἰγός) and used in scientific Latin/English compounds — aegagrus 'wild goat', \"\n       \"Aegipan, aegicrania (the goat-skull ornament in architecture). Klein's entry, which Nourai cites, defines \"\n       \"it in exactly these terms. So the Greek -> English arrow is a modern learned borrowing rather than a \"\n       \"descent, and Nourai's gloss 'of a goat' is right.\"),\n     \"sources\":[AIX],\n     \"ref_check\":[{\"ref\":\"KLN:30\",\"status\":\"supports\",\"note\":\"Klein (KLN_1966.txt leaf 28, ~p.32): 'aego-, combining form meaning \\\"goat\\\". — Gk. αἰγο-, fr. αἴξ, gen. αἰγός, \\\"goat\\\", which is cogn. with OI. ajaḥ ... Cp. the first element in aegicrania.' Nourai's headword, gloss and reference all match.\"}],\n     \"consulted\":[\n      {\"src\":\"KLN\",\"where\":\"s.v. aego- and aegis\",\"stance\":\"supports\",\"note\":\"see ref_check.\"},\n      {\"src\":\"AHD\",\"where\":\"Watkins 'aig-'\",\"stance\":\"partial\",\"note\":\"Watkins lists only AEGIS as the English derivative of this root; the combining form aego- is not separately entered.\"},\n      {\"src\":\"FSD\",\"where\":\"Funk & Wagnalls (FSD_vol1.txt)\",\"stance\":\"silent\",\"note\":\"grep for 'aego-'/'aegis' in the OCR'd volume 1 returned nothing usable (OCR damage in the front of the A section).\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-39.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk39.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-39.json > /dev/null && echo \"VALID JSON\"",
 "description": "Write page-39 verification JSON"
}
```


### [2026-09-04T19:09:09.650Z] TOOL RESULT

```
ok
VALID JSON
```


## [2026-09-04T19:09:15.449Z] TOOL CALL #81: Bash

```json
{
 "command": "python3 tools/verify_check.py 39",
 "description": "Run verify_check for page 39"
}
```


### [2026-09-04T19:09:17.047Z] TOOL RESULT

```
nodes verified: 21/21
node verdicts: {'plausible': 8, 'confirmed': 11, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'plausible': 2}
ref checks: {'supports': 20, 'not_checked': 3, 'not_found': 2, 'partial': 2}
books consulted: {'supports': 43, 'partial': 12, 'silent': 19, 'contradicts': 1} | by book: {'WLD': 8, 'KLN': 8, 'IEC': 6, 'AHD': 5, 'MON': 5, 'BRT': 4, 'HRN': 4, 'BQT': 4, 'POK': 4, 'SKT': 4, 'PHD': 3, 'HUB': 3, 'NYB': 2, 'LAT': 2, 'WEB': 2, 'FSD': 2, 'ARY': 1, 'CHEUNG': 1, 'SYN': 1, 'TLM': 1, 'FVQ': 1, 'PLA': 1, 'AFM': 1, 'RCH': 1, 'DEV': 1}
```


## [2026-09-04T19:09:31.999Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-39.json` written; `verify_check.py 39` reports 21/21 nodes, no PROBLEM lines.

**Page 39 (book p. 9) — 2 entries (Aien/Aier are redirects, skipped)**

Verdicts: roots 2 plausible; nodes 11 confirmed, 8 plausible, 1 disputed, 1 transcription_suspect.
Ref checks: 20 supports, 2 partial, 2 not_found, 3 not_checked (PRT lending-only; two unreferenced nodes).

Flagged items:
- **transcription_suspect — Aidh, node 12, Persian "eter"**: JSON has «اثر»; the book prints **اتر** (verified on a 600 dpi render of the source PDF p.39, and Mo'in's headword is اتر). اثر would be a different word.
- **disputed — Aig-, node 2, Pahlavi azak**: MP azag/NP azg belong to PIE *h₂eǵ- (Skt. ajá-, Lith. ožys) — Pokorny pp. 6-7 and Walde-Pokorny I 38 — not to *h₂eyǵ- (Gr. αἴξ, Av. izaēna-, Pokorny p. 13). Av. iz- cannot give az-. Nourai's own POK:6 citation is literally the *aǵ-* page, so his root reference points at a different root than his root name.
- Other substantive notes captured in the file: Av. aēsma- means "firewood", not "heat", and hēzum is Middle Persian, not Avestan/Old Persian (node 1); Latin box "asetus" is Nourai's own misprint for **aestus** (confirmed on the page image, so not an extraction error); the whole brick branch (Av. ištya-, OP išti-, MP/NP xišt) rests on Johansson IF 19,136 and is now often treated as a BMAC-substrate loan (Lubotsky, Schmitt) rather than a derivative of "to burn"; "Es 1" is a redirect to "Aidh" in Nourai's own dictionary and conflates *h₂eydʰ- with *as-.
- Nourai's page numbers that check out exactly: POK:11, HRN:108, HRN:249, KNT:175, SYN:604, TAD:1, BQT:2407 (Mo'in's footnote fetched via ref_page.py); KLN:30 and BQT:750 within the leaf→page tolerance; MON:143/134 verified by content in the 2-vol abridgement (6-vol pagination unmappable).
