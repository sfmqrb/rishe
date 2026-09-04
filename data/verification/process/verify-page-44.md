# Verification process log — verify-page-44


## [2026-09-04T19:13:10.798Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 44 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-44.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-44.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-44.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 44` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T19:13:12.356Z] AGENT

I'll start by reading the instructions file.


## [2026-09-04T19:13:14.758Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:13:14.772Z] TOOL RESULT

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


## [2026-09-04T19:13:14.800Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-44.txt"
}
```


### [2026-09-04T19:13:14.818Z] TOOL RESULT

```
1	=== PDF page 44 (book page 14) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Akru, Dakru : tear, tear drop  (refs POK:23, 179)
4	#1 (parent #0) [Avestan] refs=POK:23; KLN:1578 | asrŭ, asraka : tear
5	  #2 (parent #1) [Pahlavi] refs=None | ars : tear
6	    #3 (parent #2) [Persian] refs=BQT:103; HRN:17 | ars «ارس» : tear ; ašk «اشک» : tear
7	#4 (parent #0) [Germanic] refs=AHD | tahr : tear
8	  #5 (parent #4) [English] refs=None | tear 1
9	--- entry 1 ---
10	ROOT [Indo-European] Akwa : water  (refs POK:23)
11	#1 (parent #0) [Latin] refs=AHD | aqua : water
12	  #2 (parent #1) [Avestan] refs=VFO:15 | arva, arvâ : eagle | NOTE: VFO claims these are cognates of English "eagle" and French "aigle" but does not provide any derivation.
13	    #3 (parent #2) [Pahlavi] refs=BQT:58; MPP:79 | alŭh : eagle
14	      #4 (parent #3) [Persian] refs=MON:85; BQT:58; VFO:15 | âleh «آله ( لِه ، آلغ ، آلوه ، آل )» : eagle
15	  #5 (parent #1) [Latin] refs=KLN:97,494; WEB:569; FSD:779 | aqualius : water (dark) colored bird, eagle
16	    #6 (parent #5) [French] refs=KLN:494 | aigle : eagle
17	      #7 (parent #6) [English] refs=KLN:494 | eagle
18	  #8 (parent #1) [French] refs=KLN:495 | aquarium ; eau : water ; eau de Cologne : water (perfume) of Cologne
19	    #9 (parent #8) [Persian] refs=VOP:14,39 | âkvârîŭm «آکواریوم» : aquarium ; odokolon «ادوکلن ( ادکلن )» : eau de Cologne
20	  #10 (parent #1) [English] refs=AHD | aquarium, aqua, aquatic
21	#11 (parent #0) [Germanic] refs=AHD | ahwjo, aujo : (thing on) water, island
22	  #12 (parent #11) [English] refs=AHD | island
23	
```


## [2026-09-04T19:13:16.513Z] AGENT

I'll read the source JSON and supporting files.


## [2026-09-04T19:13:18.581Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-44.json && echo \"=== MATRIX ===\" && cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T19:13:18.645Z] TOOL RESULT

```
{
  "pdf_page": 44,
  "book_page": 14,
  "entries": [
    {
      "root": {
        "name": "Akru, Dakru",
        "lang": "Indo-European",
        "refs": "POK:23, 179",
        "gloss": "tear, tear drop"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:23; KLN:1578",
          "words": [
            {"translit": "asrŭ, asraka", "gloss": "tear", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "ars", "gloss": "tear", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:103; HRN:17",
          "words": [
            {"translit": "ars", "gloss": "tear", "script": "ارس"},
            {"translit": "ašk", "gloss": "tear", "script": "اشک"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "tahr", "gloss": "tear", "script": null}
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
            {"translit": "tear 1", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Akwa",
        "lang": "Indo-European",
        "refs": "POK:23",
        "gloss": "water"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "aqua", "gloss": "water", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "VFO:15",
          "words": [
            {"translit": "arva, arvâ", "gloss": "eagle", "script": null}
          ],
          "note": "VFO claims these are cognates of English \"eagle\" and French \"aigle\" but does not provide any derivation.",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Pahlavi",
          "refs": "BQT:58; MPP:79",
          "words": [
            {"translit": "alŭh", "gloss": "eagle", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:85; BQT:58; VFO:15",
          "words": [
            {"translit": "âleh", "gloss": "eagle", "script": "آله ( لِه ، آلغ ، آلوه ، آل )"}
          ],
          "note": null,
          "quote": {
            "text": "مَثل دشمنان تو با تو - حیلهٔ کبک و حمله های لِه است",
            "poet": "Farqadî"
          }
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Latin",
          "refs": "KLN:97,494; WEB:569; FSD:779",
          "words": [
            {"translit": "aqualius", "gloss": "water (dark) colored bird, eagle", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": "KLN:494",
          "words": [
            {"translit": "aigle", "gloss": "eagle", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "KLN:494",
          "words": [
            {"translit": "eagle", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 1,
          "lang": "French",
          "refs": "KLN:495",
          "words": [
            {"translit": "aquarium", "gloss": null, "script": null},
            {"translit": "eau", "gloss": "water", "script": null},
            {"translit": "eau de Cologne", "gloss": "water (perfume) of Cologne", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "VOP:14,39",
          "words": [
            {"translit": "âkvârîŭm", "gloss": "aquarium", "script": "آکواریوم"},
            {"translit": "odokolon", "gloss": "eau de Cologne", "script": "ادوکلن ( ادکلن )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 1,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "aquarium, aqua, aquatic", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "ahwjo, aujo", "gloss": "(thing on) water, island", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "island", "gloss": null, "script": null}
          ],
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


## [2026-09-04T19:13:37.767Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','KLN','AHD','BQT','HRN','MON','VFO','MPP','VOP','WEB','FSD','WLD','IEC','SYN','PHD','NYB','HUB','BRT','SKT','LEW','LAT','ARY','CHEUNG']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-04T19:13:38.809Z] TOOL CALL #5: Bash

```json
{
 "command": "grep -n -iE '^(VFO|MPP|VOP)' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt; grep -n -iE 'VFO|MPP|VOP' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt | head -30"
}
```


### [2026-09-04T19:13:39.817Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

VFO null

MPP {"title": "W. B. Henning, 'Mitteliranisch', Handbuch der Orientalistik I.4.1, Leiden 1958 (pp. 20-130)", "edition_found": "1958", "kind": "archive_djvu", "url": "https://archive.org/details/henning-1958-mitteliranisch", "identifier": "henning-1958-mitteliranisch", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/MPP.txt", "page_offset": "leaf = printed - 14 (e.g. leaf 7 = p.21). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's Table IV entry

VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

CHEUNG null
```


### [2026-09-04T19:13:39.862Z] TOOL RESULT

```
3: TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
18: TABLE IV - Reference Abbreviations (continued ...) 64 MMF 65 MON 66 MPP 67 MZF 68 NAT 69 NFI 70 NYB 71 OEW 72 OXF 73 PEI 74 PHD 75 PHN 76 PLA 77 POK 78 PRT 79 RCH K. Khalili, Dictionary of Derivatives of the Persian ^wjls jiLa* ol£ii* &gt;_£^&amp;ji Infinitives or Farhang Moshtaqqat Masader FarsT, Institute of Cultural Studies and Research, Tehran, 1993. M. Mo" in, Farhang FarsT MoT'n, Six volumes, Amir Kabir press 1363 (1984). O^*® ^ ^-a-L!* Honari darbareh Zaban Farsi, Sokhan press, Tehran 1340 (1961). C. Berlitz, Native Tongues, Grosset &amp; Dunlapp Publishers, New York, 1982 F. Jonaydi, Nameh Farhang Iran, ^Ijjl ^»js i*b Bonyad Nayshabfir, Tehran 1368 (1989). Section 4, translated from C.H. Rempis' "Persische Worter im Deutschen," in Mitteilungen, Institut fur Auslands-Beziehungen, Iran-Nummer, 3/4, Stuttgart, 1960, S.229-233. H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1974. J. T. Shipley, The Origins of English Words, The John Hopkins University Press, Baltimore 1984. Jennifer Speake, Oxford Dictionary of Foreign Words and Phrases, Oxford University Press, New York 1997 M. Pei, The Families of Words, Harper &amp; Brothers press, New York 1962. D. N. MacKenzie, A Concise Pahlavi Dictionary. Oxford University press, London 1971. A. P. Pihan, Dictionnaire Etymologique des Motes de la Langue Francaise Derives de L'Arabe, du Persan ou du Turc, Paris 1866. Asya Asbaghi, Persische Lehnworter im Arabischen. Otto Harrassowitz, Wiesbaden 1988 J. Pokorny, Indogermanisches Etymologisches Worterbuck, Two volumes, Francke verlag, Bern 1959. E. Partridge, Origins - A short Etymological Dictionary of Modern English, MacMillan Co., NewYork 1958. J. Richardson, Dictionary, Persian, Arabic and English with Dissertation on the Languages, Literature and Manners of Eastern Nations, Sange-e-Meel Publications, Lahore 1829-1984. A-13 
24: TABLE IV - Reference Abbreviations (continued...) 96 TLM 97 TTS 98 TYL 99 TZF 00 UNV 01 VDQ 02 VFO 03 VGH 04 VIE 05 VOP 06 VSF 07 WEB 08 WLD 09 ZAP 10 ZAW 11 ZFS 12 ZMA F. C. Tolman, Ancient Persian Lexicon, The Vanderbilt Oriental Series, American Book co. 1890-1908. G. Vambery, Etymologisches Worterbuch der Turko-Tatarischen Sprachen, Biblio Verlag, Osnabriick, 1972. W. Taylor, Arabic Words in English, Clarenton Press, London 1933. M. Abolghasemi, Tarikh Mokhtasar Zaban FarsT, ^-d1* oki j^""« ejJjIj Bonyad Andisheh EslamT Press, Tehran, 1373 (1994). J. M. Unvala, King Husrav and His Boy - Pahlavi Text and Glossary, Paul Geuthner publishers, Paris 1963. F. Badreh-t, Vajheh-hay Dakhil dar jl*=w oTjsji J-''2 i^l&amp;ejfj Qoran-e Majid, Translation of A. Jeffrey's book with Comments (see FVQ). Toos Publishers, Tehran 1372 (1993). M. Ahmad Soltam, Vajhgan FarsT dar Zabanhay ^jjl ^k-Sbj _ji ^j1* oT;'? OrupaT, Avay Niir Press, Tehran, 1372 (1993). H. Khadiv Jam, Vajheh Nameh Ghazalhay Hafez, Elmi Press, Tehran, 1371 (1992). £i9b» ^L^Jjc ^Ub OjT^ M. A. Sajjadiyyeh, Vajheh-hay Irani dar ^....JLCil ^bj ji ^IjjI ^la 03I3 Zaban EngelTsT, Bonyad Nayshabur, Tehran 1364 (1985). M. MoshM, Farhang Vajheh-hay Orupayl ^-"j1* j* ^kiJ lS1* °3'3 &gt;-^»j» dar FarsT, Alborz Press, Tehran 1371 (1992). K. Mehravand, Vajheh Sazi dar Zaban FarsT, Rasti press, Tehran 1349 (1970). v^-jl* ok) j4 lSJ1- °3'3 W. Collins, Webster's New Twentieth Century Dictionary of the English Language, second edition 1978. A. Walde, Vergleichendes Worterbuch der Indogermanischen Sprachen, two volumes, Walter de Gruyter &amp; co., Leipzig 1930-1973. H. W. Bailey, Zoroastrian Problems in the Ninth-Century Books, Clarendon press, Oxford 1943-1971. C. Bartholomae, Zum Altlranischen Worterbuch Nacharbeiten and Vorarbeiten, Vorlag von Karl J. Trubner, Strassburg 1906. M. Abolghasemi, Zaban FarsT va Sargozasht An, HTrmand Press, Tehran, 1375 (1996). F. Jonaydi, ZendegT va Mohajerat Aryaian, Bonyad Nayshabur, Tehran, 1374 (1995). A-15
```


## [2026-09-04T19:13:47.832Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 30 31 32; do echo \"=== POK_01 ffpage $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' POK_01.txt | head -80; done"
}
```


### [2026-09-04T19:13:49.486Z] TOOL RESULT

```
=== POK_01 ffpage 30 ===
eu'  aus  *ak-s-nä,  danach  umgebildet  llyvoov  ds.  statt '^äy.vQOv]  gr.  dy.oa-xri  , Gerste^  (;die  grannige^,  Bildung  wie  lat.  onus-tus, venus-tus)]  gr.  7]/Jg'  d^v,  Hes.  TtvQL-T^ycrjg  ,mit  feuriger  Spitze^,  df.i(p]^'/.rjg ,zweischneidig^,  xa^vrjArjg  ,mit  langer  Spitze^  (vielleicht  nur  mit  Dehnung im  Kompositum,  wonach  die  Länge  auch  im  einfachen  fj-Aeg]  doch  liegt dehnstufiges  *äk-  auch  vor  in  ion.  -^x?;*  ^xwx/J,  EniöoQaTig,  axfirj  lies., ?Jxa(5a'  •^vÖQoyyAvTiv  yvvaHa  Hes.,  vgl.  zur  Bed.  d/Mrj  .Höhepunkt  des Lebens^).
Weitergebildet  in  gr.  ö^vg  ,scharf^,  vgl.  zur  Bildung  lit.  tamsus  zu  ai. tämas-,  lit.  tamsä  (dazu  ö^ivi]  ;Egge^  Hes.),  o^og  ,Weinessig^  —  Auch dy,ax!.t€vog  ,gespitzt^  scheint  *dy,-(xyi(T-(X£i>og  zu  sein,  Hirt  IF.  12,  225.
22
Lat.  acus,  -eris  ,Spreu^,  acervus  (*aces-V0's)  ^»Haufe^;  got.  ahs  Gen.  *ahsis n.,  aisl.  ax  n.,  alid.  ahir,  ehir  n.  (germ.  *aJiiz),  aus  dem  PI.  nbd.  ,Ähre' f.,  aber  ags.  ear  (*ahuz),  Dat.  Sg.  nordlmmbr.  cehher,  eher  ds.  (Über  das Nebeneinander  von  i-,  u-  und  s-Stämmen,  z.  T.  schon  idg.^  aber  beson- ders im  Germanischen,  vgl.  Brugmann  Vgl.  Gr.  II  1,  522,  u.  Specht  Idg. Dekl.  152.  Ob  ein  ursprüngl.  idg.  -es-  oder  -is-,  bzw.  -«s-St.  vorliegt,  ist im  Einzelfalle  schwer  zu  entscheiden.  Vgl.  auch  Sievers-Bruuner  Aengl. Gr.  §§  128,  2  u.  288  f.)
ak-sti-
Cymr.  eitliin  m.  PL  ^Stechginster^  {*akstmo-),  daraus  entlehnt  mir.  aittenn ds.  (mit  unklaren  Lautverhältnissen);  lit.  akstis  f.  ,Räucherspieß^  (=  russ. osH  ,Spitze,  Granne^),  äkstinas  m.  ,Stachel,  Ansporn^  =  aksl.  oshm  m. jStacheF;  cech.  osten  ds.
8.  Mit  f-Formantien:
Ai.  apäithä-  m.  (aus  *apa-as-tha)  ^Widerhaken  am  PfeiF;  gr.  dy^rrj ^schroffe  Küste  mit  Brandung;  Landspitze,  Erhöhung*^;  loch.  B  äg-,  ägge- ,Kopf,  Beginn^  (aus  *ak-t-).
oketä  ;Egge,  Gerät  mit  Spitzeir:
Lat.  occa  ,Egge^  aus  *otikä  durch  Umstellung  aus  *okitä  (Hirt  IF.  37, 230)?  Vgl.  das  anders  gebildete  gr.  ö^Ivt]  ,Egge^;  acymr.  ocet,  corn.  ocet^ bret.  oguet:  ahd.  egida,  mhd.  eg{e)de
=== POK_01 ffpage 31 ===
,  ags.  eg{e)de  f.  (nhd.  Egge  geneuert mit  dem  Verbum  eggen  aus  ahd.  egen,  ecken,  urgerm.  *agjan,  das  seiner- seits erst  aus  dem  Subst.  *agidö  rückgebildet  ist);  lit.  akecios,  ekeölos ,Egge^,  apr.  aketes  ,Eggen'^,  das  e  statt  e  stammt  von  dem  Verbum  *a/mö in  lit.  akeju,  aketi,  daneben  akeju,  eketi]  das  anlautende  a-  ist  in  unbe- tonter Stellung  vor  palatalem  Vokal  oft  zu  e  geworden  (Endzelin  Lett. Gr.  36).
Specht  KZ.  62,  210  ff.  (unglaubhaft).
S.  unter  *ok-töu  ,acht^,  eigentlich  ,die  beiden  Spitzen  der  Hände  (ohne Daumen)^
Schwundstufiges  k-  steckt  wahrscheinlich  in  den  Stämmen  keinen-, kemel-,  körnen-,  ,Stein,  HimmeP,  komor-  ,Steinhammer^,  kei-,  köi-,  kdi- ,schärfen,  wetzen^,  ku-  ,spitz,  Spieß*.
WP.  I  28  ff.,  WH.  I  6  ff.,  Specht  DekL  24,  69,  125,  271,  331.
23
akkä  .Mutter'  (Lall wort).
Ai.  akJcä  .Mutter'  (Gramm.),  gr.  'Aa/m  .Amme  der  Demeter'.  axxa> Popanz'.  dyi'Ai^sadaL  .sich  zieren,  sich  dumm  stellen',  lat.  Äcca  Lm^entia Larenmutter,  römische  Flurgottin'  (wohl  etruskisch);  auch  in  kleinasiati- schen Sprachen;  vgl.  läpp.  Madder-akka  .Erdenmutter'.
AVP.  I  34.  WH.  I  5.  Über  toch.  ammaki  s.  unter  am[m)a.
akru  .Träne'.
Ved.  dsru  n..  später  auch  ds7^am  .Träne',  av.  asrn-  n..  lit.  asarä  und äsara  f..  toch.  A  äkäv  PI.  äkrunt  ds..  vgh  ai.  asräyämi,  lit.  äsavoju ,\veine'.  Das  Verhältnis  zu  idg.  "^dakru  .Träne'  ist  ungeklärt.  Vgl.  Meillet BSL.  32.  14L
WP.  I  33.  WH.  I  746.
ak"-  .schädigen'??
Ai.    dka-m    .Leid.    Schmerz',    av.    akö    .böse,    schlecht',     axtis    .Leid. Schmerz.  Krankheit';    gr.   Nomen   *än:aQ,  ^ccTtiög,    davon    rjrtavsZ'    äfcoqei, '^Ttavia'    änoQia,    rjneoonevq    .Betrüger';    Verbalst,    an-   in   dnavi]  .Betrug' (*a'pntä),  redupl.  Präsens  iama)  .schädigen'. Kuiper  Gl.  21.  282  f.
aJc!^ä-  (richtiger  ok'iä) :  ek]i-  .Wasser.  Fluß'.
Lat.  aqua  .Wasser.  Wasserleitung'  (davon  aquilus  .dunkel',  aquila .Adler',  eigentl.  .der  Dunkelfarbige',  aquilö  .Nordwind',  eigentl.  .der  den Himmel  Verdunkelnde')  =  got.  a\va  f.  .Fluß.  Gewässer',  aisl.  o.  ags.  ca. as.  ahd.  aha,  nhd.  Ache  ds.  (germ.  *ahioö,  davon  abgeleitet  *ahioj5,  *aicjö .die  vom  Wasser  Umgebene'  in  aisl.  ey  f.  .Insel.  Aue',  ags.  ieg,  ahd. -ouwa,  -awa,  mhd.  ouwe  f.  .Wasser.  Halbinsel  im  Flusse,  wasserreiches Wiese
=== POK_01 ffpage 32 ===
nland',  nhd.  Aue,  vgl.  afries.  ei-land  .Insel'.  Sca(n)din-avia  Kretsch- mer  Gl.  17,  148  ff.),  russ.  FIN  Oka,  pannon.  ON  Aquincum  .Ofen',  apul. FIN  Aquilö,  ven.  ON  Aquileia  (auch  in  Süddeutscliland);  mit  Ablaut (idg.  e)  dazu  aisl.  kgir  (*eKog)  .Gott  des  Meeres',  ags.  xg-iceard  .Wache' an  der  See',  eagor  .Meer.  Flut'  (der  Anlaut  nach  ea);  vielleicht  hierher ai.  kam  .Wasser',  dak.  PflanzenN  y,oaödi.ia'  Tcoraj-ioysiTcov  .Wassersiedler' (*kYia-dhemn),  poln.  (nordill.)  FIN  Kiua.
Die  Zugehörigkeit  von  hitt.  e-ku-uz-zi  (ekuzi)  .trinkt'.  3.  PL  a-ku-ioa-an-zl, scheint  mir  nicht  unwahrscheinlich.  Hierzu  auch  toch.  AB  yok-tsi  .trinken'. Air.  oiche  .Wasser'  existiert  nicht;  cjmr.  aig  .Meer'  ist  eine  Neubildung zu  eigion  aus  lat.  oceanus.
WP.  I  34f.,  WH.  I  60.  848.  Feist  18 f..  Pedersen  Hittitisch  128.  To- charisch  190.
24  •
I.  al-,  Ol-  Pron.-St.  .darüber  binaus'.  adjektivisch  al-no-s,  ol-no-s.
Lat.  uls  jenseits^  *ulter,  -tra,  -trum  .jenseitig'  (ultrö,  ultra),  Komp. ulterior,  Sup.  ultimiis  =  osk.  ültiumam  .ultimam'^ ;  alat.  ollus  .ille'  (*ol-no-s, vgl.  unten  ir.  ind-oll  und  slav.  "^olni),  jünger  olle,  olll  .tunc'.  olllc  ,i\\i&'^ dehnstufig  ölim  .einst'  (wohl  nach  im,  exim  umgestaltetes  und  mit  ai. par-äri  ,\m  drittletzten  Jahr'  [vgl.  TtSQ-vai]  gleichzusetzendes  *öl{,  Loka- tivadverb, auf  das  auch  die  Glossen  olitana  .vetusta'.  olitinata  .veterata. antiqua'  —  ö  oder  Ö?  —  zurückweisen  können),  umbr.  ulo,  ulu  .illo.  illuc'; durch  Einfluß  von  is,  iste  usw.  wurde  ollus,  olle  zu  ille  umgefärbt.
Slav.  *olni  (idg.  *oln-ei)  =  aksl.  lani,  cech.  loni,  poln.  loni  .im  vorigen Sommer,  im  vorigen  Jahre'  (.in  jenem  Jahr',  vgl.  lat.  olll  .tunc').
Die  Bed.  von  ir.  alltar,  allaid  (s,  unten)  läßt  auch  Verwandtschaft  von ai.  drana-  .fern,  fremd'  (=  av.  auruna-  .wild'?),  äräd  .aus  der  Ferne'. äri  .fern'  als  möglich  erscheinen.  Hierzu  auch  vielleicht  ai.  ori  .Fremder. Fremdling'.  ar(i)yd-  .zum  Fremden  gehörig'  (vgl.  ahd.  eli-lenti  .fremdes Land'),  dann  Subst.  .gastlich.  Herr',  dazu  är{i)ya-  .zu  den  ar{i)yd-  ge- hörig, wirtlich',  daher  VN  .Arier',  äryaka-  .ehrwürdiger  Mann',  aryamdn- n.  .Gastlichkeit',  m.  .Gastfreund';  av.  airyö  (=  ärya),  apers.  äriya  (=  ariya) .arisch',  av.  airyaman  .Gast.  Freund',  npers.  ermän  .Gast',  dazu  der  sarmat. VN  IdXavol  (osset.  *alan),  osset.  ir  .Ossete',  iron  .ossetisch'  (P.  Thieme^). Der  Fremdling  im  Rigveda.  Abb.  f.  d.  Kunde  d.  Morgenl.  XXÜI  2.  1938; Specht  KZ.  68.  42 ff.);  air.  aire  (*ar{os)  und  airech  .Adliger.  Freier'  können zur  Präp.  air-  .vor',  also  .an  erster  Stelle  stehend',  gehören- (Thurneysen ZOP.  20.  354);  der  sagenhafte  ir.  Stammvater  'Eremön  ist  eine  gelehrte Neubildung  zu  'Eriu  .Irland'.    S.  auch  unter  ario-  .Herr.  Gebieter'.
Air.  oll  Adj.  .amplus.  groß,  umfassend',  eigentlich  .über  (das  Gewöhn- liche) hinausgehend'  (formell  =  lat.  ollus,  idg.  ^olnos),  Komp.  {K)uilliu .amplius'.  Adv.  ind-oll  .ultra',  woraus  vielleicht  auch  innonn,  innunn .hinüber'  (mit  Assimilation  unter  Mitwirkung  von  inonn  .derselbe';  Thur- neysen KZ.  4S.  55 f.;  anders  Pedersen  KG.  II  195).
```


## [2026-09-04T19:14:00.846Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==187 || NR==188' POK_01.txt | grep -n -A20 -i 'dakru\\|Träne' | head -60"
}
```


### [2026-09-04T19:14:02.473Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:14:04.763Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'dakru' POK_01.txt POK_full.txt | head -20"
}
```


### [2026-09-04T19:14:04.822Z] TOOL RESULT

```
POK_01.txt:330:Ved.  dsru  n..  später  auch  ds7^am  .Träne',  av.  asrn-  n..  lit.  asarä  und äsara  f..  toch.  A  äkäv  PI.  äkrunt  ds..  vgh  ai.  asräyämi,  lit.  äsavoju ,\veine'.  Das  Verhältnis  zu  idg.  "^dakru  .Träne'  ist  ungeklärt.  Vgl.  Meillet BSL.  32.  14L
POK_01.txt:2587:dakru'  n.  ,Träne'.
POK_01.txt:2589:Idg.  *dakru  ist  wahrscheinlich  aus  ^dralcru  dissimiliert  wegen  ahd, trahan,  as.  PL  trahnl  , Träne',  mnd.  trän  ds.  und  , (durch  Kochen  aus  Fett herausgepreßter  Tropfen:)  Tran',  mhd.  traher  ds.  (-er  wohl  nach  zäher geneuert)  und  arm.  artasuk  , Tränen',  Sg.  artausr  aus  *drakur.
POK_01.txt:2590:Andrerseits  sucht  man  Vermittlung  mit  ai.  dsru,  asra-m  , Träne',  av. asrüazan-  , Tränen  vergießend',  lit.  a§arä,  ä§ara  , Träne',  lett.  asara  ds.; wohl  bloßes  Reimwort,  indem  "^akro-  ,acer,  scharf,  acerbus'  als  Beiwort der  Träne  (, bittere  Tränen')  teilweise  an  Stelle  von  dakru  trat,  wobei  es dessen  w-Flexion  übernahm?  Vgl.  auch  Mühlenbach-Endzelin  I  142  f.;
POK_full.txt:3800:"cries'. The relationship to Indo Germanic *dakru'tear' is unsettled, compare Meillet BSL. 
POK_full.txt:16354:partially used in place of dakru, whereby it took over its ^/-inflection? compare also
```


## [2026-09-04T19:14:07.663Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2578,2600p' POK_01.txt"
}
```


### [2026-09-04T19:14:07.719Z] TOOL RESULT

```
liitt.  te.ihä-  ,sich  fernhalten  von*  (3.  Sg.  Prät.  ti-es-ha-as).
Daneben   mit  i-Vokalismus   (idg.   "^di-s-  als   Erweiterung  zu   c^l-?    Oder- erst  germ.  Neuschöpfung?):
schwed.  dial.  teisa,  tesa  , zerpflücken*,  dän.  dial.  tese  , zupfen  (z.  B.  Wolle)Vi ags.  tcp.san  , zerpflücken',  ahd.  zeisan,  zias  , zausen.  Wolle  zupfen';  ostfries.j hoU.  teiffteren  , reißen',  ags.  tcesel,  ahd.  zeisala  , Kardendistel',  norw.  mdartl,  | test  jWeidenbrand,  Haarlocke',  mit  l  norw.  tlst  , Faser',  tisl  , Gesträuch*,! mit  1  mhd.  zispen  , schleppend  gehen'  (wie  zaspen),  wohl  auch  (?)  ags. teoswian  ,plagen,  verunglimpfen',  teoso  ,Beleidigung,  Betrug,  Bosheit^
Endlich  mit  w-Vokalismüs:  norw.  dial.  tosa  , zerfasern,  zupfen^  auch  | , pfuschen,  langsam  arbeiten',  tose  .hinfällige  Person',  tos  , Fasern,  zerfa- sertes Tauwerk',  tossa  ,streuen,  ausbreiten',  mengl.  tötüsen  , zerzausen*, mnd.  tosen  , reißen,  zerren',  ahd.  zirzüsön  , zerzausen',  mhd.  züsach  , Ge- strüpp', züse  f.  , Gestrüpp,  Haarlocke'  u.  dgl.;  vielleicht  zu  lat.  dümus , Gestrüpp,  dicht  verwachsener  hoher  Strauch'  (*d^s-mo-s)  und  air.  doss jBusch^
179
fjber  die  wenigstens  grundsätzlich  als  Erweiterungen  von  da-  , schneiden, nalteu*  auffaßbaren  Wzln  del-  , spalten',  del-  ,es  worauf  abgesehen  haben', ;*.!-    spalten,  schinden'  s.  unter  eigenem  Stichworte.
\VP.  I  '^63 ff.,  WH.  I  322,  323 f.,  859;  Schwyzer  Gr.  Gr.  I  676.
rffl/uer.  Gen.  daiures  ,der  ßrudei*  des  Gatten,  Schwager^
Ai'  düvdr-,  arm.  taigrj  gr.  därjQ  (*öaiJ^rjg),  lat.  levir  (im  Ausgang  nach ^ir  umgestaltet;  das  l  für  d  wohl  sabinisch),  ahd.  zeilihur,  ags.  täcor ^vermutlich  durch  Kreuzung  mit  einer  Entsprechung  von  lit.  Idigonas Bruder  der  Frau^),  lit.  dievens  (für  *dieve  =  ai.  devdr-)  alter  kons.  Gen. dlevefs),  lett.  dieveris,  aksl.  cZ^vej'b  (z-,  io-  und  kons.  Stamm). WP.  I  '767,  WH.  I  787,  Specht  KZ  ^62,  249  f.,  Trautmann  43.
dakru'  n.  ,Träne'.
Gr.  däyiQv^  ddyiQvov,  ddy.QV(j,a  , Träne';  daraus  entlehnt  altlat.  dacruma, lat.  lacruma,  lacrima  ds.  (mit  sabin.  Z?);  air.  der  n.,  cjmr.  deigr  (kann auf  einen  PI.  *dakri  der  o-Dekl.  zurückgehen),  PL  dagrau,  abret.  dacr-(lon) ,uvidus',  corn.  dagr  , Träne'  (inselkeltisch  *dakromj  siehe  Thurneysen KZ.  48,  66  f.);  germ.  *tdhr-  und  tagr'-  :  got.  tagr  n.  , Träne',  anord.  täo'  n. (aus  *tahr-)j  ags.  tcehher,  tear,  teagor  m.,  ahd.  zalia^'  m.  (nhd.  Zähre  aus dem  PL;  ob  im  Germ,  noch  vom  alten  w-St.  oder  einem  daraus  geneu- erten  o-St.  auszugehen  sei,  ist  fraglich).
Idg.  *dakru  ist  wahrscheinlich  aus  ^dralcru  dissimiliert  wegen  ahd, trahan,  as.  PL  trahnl  , Träne',  mnd.  trän  ds.  und  , (durch  Kochen  aus  Fett herausgepreßter  Tropfen:)  Tran',  mhd.  traher  ds.  (-er  wohl  nach  zäher geneuert)  und  arm.  artasuk  , Tränen',  Sg.  artausr  aus  *drakur.
Andrerseits  sucht  man  Vermittlung  mit  ai.  dsru,  asra-m  , Träne',  av. asrüazan-  , Tränen  vergießend',  lit.  a§arä,  ä§ara  , Träne',  lett.  asara  ds.; wohl  bloßes  Reimwort,  indem  "^akro-  ,acer,  scharf,  acerbus'  als  Beiwort der  Träne  (, bittere  Tränen')  teilweise  an  Stelle  von  dakru  trat,  wobei  es dessen  w-Flexion  übernahm?  Vgl.  auch  Mühlenbach-Endzelin  I  142  f.;
s.  oben  S.  23  unter  akru.
WP.  I  769,  WH.  I  746  f.
däu-,  d9u-,  du-    1.  ,brennen^,  2.  ^verletzen,  quälen,  vernichten,   feindselig^;
unsicher,  ob    in    beiden    Bed.  ursprünglich    identisch   (etwa   teils   als
jbrennender   Schmerz^,  teils  ,durch  Feuer  vernichten,   die   feindlichen
Siedelungen  niederbrennen^?).
Ai.  dunöti  ,brennt  (trans.),    quält^,   dünd-  ,gebrannt,   gequält^,    Pass.   du-
yate  ,brennt^   (intr.),  kaus.  dävayati  ,verbrennt^   (trans.),   dävdi,   (mit  Ab-
12*
180
```


## [2026-09-04T19:14:33.167Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD dakru ===\" && grep -n -i -E 'dakru|dak.ru' AHD_watkins1985.txt | head -20 && echo \"=== AHD akwa ===\" && grep -n -i -E 'ak.*w.*a-|akwa|ak\\^wa' AHD_watkins1985.txt | grep -i -n 'water' | head -20"
}
```


### [2026-09-04T19:14:33.249Z] TOOL RESULT

```
<persisted-output>
Output too large (41.1KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bfy3o8vpv.txt

Preview (first 2KB):
=== AHD dakru ===
358:dakru-. Tear. 1. Germanic *tahr-, *tagr- in: a. Old Eng- lish téar, tehher, tear: TEAR2; b. Middle Low German tran, tear, drop: TRAIN OIL. 2. Suffixed form *dakru-ma in Latin lacrima (Old Latin dacruma), tear: LACHRYMAL. [Pok. dakru- 179.]
1726:LAAGER legh- LABEL leb-! LABELLUM leb-2 LABIAL leb-2 LABILE leb-1 LABIUM leb-2 LABOR leb-1 LABRET leb-2 LABRUM leb-2 Lac! reg-3 LACCOLITH laku- LACERATE |@k- LACHRYMAL dakru- LACINIATE l@k- LACK leg-2 LACROSSE ger-2 LACTATE melg- LACTEAL melg- LACTESCENT melg- LACTO- melg- LADDER Klei- LADE kla-
2349:TEAR? dakru- TECHNICAL teks- TECHNOLOGY teks- TECTONIC teks- TECTRIX (s)teg- TECTUM (s)teg- TEEM! deuk- TEEN? deu-3 TEETER der-1 TEETOTUM teuta- TEGMEN (s)teg- TEGMENTUM (s)teg- TEGULAR (s)teg- TEGUMENT (s)teg- TEIGLACH dheigh- 'TELAMON tele- TELANGIECTASIA ten- TELE- kwel-2 TELEKINESIS kei-3 TELEOLOGY kWel-1 TELEOST kWel-1, ost- TELESCOPE spek- TELEUTOSPORE kwel-1 TELIC kwel-1 TELIUM kwel-1 TELL del-2 TELLURIAN tel- TELLURIC tel- TELLURION tel- TELLURIUM tel- TELLURO- tel- TELO- kwel-1 TELPHER bher-1 TEMERARIOUS teme- TEMERITY teme- TEMPLE! tem- TEMPLE? temp- TEMPLES tem-
2400:TRAIN OIL dakru- TRAIT tragh- TRAITOR d6- TRAJECT yé TRAMMEL macula, trei- TRAMP der-! TRAMPOLINE der-1 TRANCE ei-1 TRANQUIL kweie-2 TRANS- tere-2 TRANSACT ag- TRANSCEND skand- TRANSCRIBE  skribh- TRANSDUCER deuk- TRANSECT sek- TRANSFER bher-1 TRANSFIGURE dheigh- TRANSFIX dhig¥- TRANSFUSE gheu- TRANSGRESS ghredh-
=== AHD akwa ===
7:277:akwa-. Water. 1. Germanic *agwjd becoming *auj6, “thing on the water,” in Old English ig, ieg, island, and
...
</persisted-output>
```


## [2026-09-04T19:14:34.317Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT asru ===\" && grep -n -E 'asru|asrū|asrūazan' BRT.txt | head -20 && echo \"=== BRT eagle/arva ===\" && grep -n -E '\\barva\\b|arəva|ərəzifya|erezifya|Adler' BRT.txt | head -30"
}
```


### [2026-09-04T19:14:34.390Z] TOOL RESULT

```
=== BRT asru ===
2881:mit /fl/>r 'befehlen',  mit  Dat.  der  Person und  folg,  dir.  Rede:  at  tu  möi  nöit  asrustä (sd.)  paifyaoyza  (2SPr.).-  *uziriidyäi  (sd,) V.4.J.I2.
4049:•  j.  a-fra'vao£a-  Adj,  'nicht  sprechend, der  nicht  sprechen  kann,  stumm':  asrut.- gaoiö  vs  'Is  v3  N.  14-
4085:•  j.  ^afsmaimv^  Adv.  'verszeilenweise' : iraosim  . .  yS  paoirys  ga^a  frasrävayat . . *a/s°'''  vacastastivat  ".  .  der  zuerst  die Gäha&  rezitirte  .  .  verszeilen-,  strophen- weise" Y.  57.8; — yä  gäiä  *a/s''^  sräva- yatö  uva  ratufris  (statt  ND.)  vacattaSHvat *srävayatS  aSavatö  katarascit ,.  N.  2J;  — ys  yasrum  *yasmti  *aft°  -ö  va  vacoitaitivai va  nva  ratufrya  N.  24;  —  yat  kakat *'amrutS  ^'vanca'''^  *valastastivaüa ..  N.24.
4300:•  j.  an-aiwi'ätay-,  an-aivi'ätay-"  f.  1) 'NichtStudium,  Unterlassen  des  Studiums'; yS  asrut^aosB  vä  a/ravaocS  vä  neit  lim afum  vääm  *aiwyas  tisit  *paslalta  'viM astryeili  yezi  dal  *öyum.pe  *v3am  *aiwyäs "wuti  ästryäti  "wenn  einer,  weil  er  taub ist  oder  stumm,  auch  nicht  ein  einziges Wort  lesen  kann,  dann  macht  er  sich durch  NichtStudium  nicht  sündig;  wenn er  aber  auch  nur  ein  einziges  Wort  lesen kann,  so  macht  er  sich  durch  NichtStudium sündig"  N.  i4;  — y5  .  .  nSii  aiwyästi  (sd.)
4951:Satzes  'jedoch':  *k!ra  .  .  *a^st»im  fiaiti.- bamt?  antarf  (sd.)  aAuna  *airyamana *Sy^mcit  a°  vilcim  gii^anqm  asrutpm  (sd.) paitiiarS  aratufris  N.  10^.
5548:•  jj  g-  'airyaman-,  g.  airyäman-  m. 'Genosse'  uzw.  priesterlicher,  Angehöriger des  ersten  oder  Priesteratands  (s.  unter 'pistra-),  'Sodale' ;  Sing,  auch  koU.  'Soda- lität',  nur  gAw.:  iJ  yama  kp  x^allus  {%<!.) dätäis  anhat  yp  ,  .  Y.  /fg.  7 ;  —  ahyScH x'aSus  (sd.)  yjsal  ahyä  virizsntm  mat yamnn  . .  Y.J2.1;  —  yf  '^jvaj  masdn asruinm  . .  yazli  (sd.)  apa  K^'aüSuScä  tar>- maitTm  virn^nahyiilä  . .  'yamanascä  . .  Y. 33-4  i  —  y^  asäuia  vahiils  :^aSä  (sd.) vä  al  vä  v>r>iSny3  yämiiä  (IS.  als  Subj.)  '> vil .  .  Y.  JJ.  3;  —  pairl  clausus  'yama- nascä  dadaili  ndii  .  .  i-ir>z5nä  (sd.)  Y.46. I.  A)  Name  einer  Gottheit":  vairya sar)ha  para.äi'd  upa.vasanuha  avi  nmli' mm  yamaini  imat  sanhsis  'yamanäi  J' "A^,  geh  weg,  fahr  hin  ins  Haus  zu  A., das  sollst  du  dem  A.  kund  machen"  V.
5912:asrutvm
5939:hört,  nicht  hörbar':  y3 .  .  pailiitanti  (sd.) anyö  713  hl  da/iml  srutn  glisä  dänSiti *ratufris  'tä  daoniti  {aratufril)  "wenn einer. .,  und  ein  andrer  D.  die  Gäkäs.  fiir ihn  hörbar  vorträgt",  so  ist  er  r.\  wenn er  sie  nicht  hörbar  vorträgt",  ist  er  ar." N.  25.         asruhm  als  Absei,  sbes.
5955:asrutgaosa-
5980:Vgl.  iransa:  —  aL  trusläy-  f.;  mp.  asrusl{at') Adj.  —  Pü.  (lu  j.):  asruil,  (lU  g.):  anigBsJtäi, •tärih.  —  1)  zAusdr.  3.  BtHU  IF.  g.  256.
6200:•  j.  aSaya  Adv.  'wie  es  rechtens  ist,  nach Gebühr;  wie  Recht  und  Brauch  es  ver- langt, rite':  a°  nB paitlJamyatY.y.i^;  — ahunahe  vairyehe  a-  frasrutahe  hävaiia- yäsca  a'  fralBtayä  Y.27.7;  Vr.i2.2';  — a'  daüqmi  3^ar?%3m  myasdim  Y.  7.  i ;  a  ff., 8.1,  Öy.itt.;  —  äat  yczi  li  baraiti  ais- mam  vä  a'  bir>t3m  bar?sma  vS  a°  frastar^ i>m  urvaratn  vä  hattanaipatam  Y.  6-2. 9 ; V.Ä79;  —  1'  äaoqmi  imqm  zaoirqm.. a"  uüdätqm  Y.66.1;  22.  z;  —  urvarqm häftflnaipatam    a°    uzdätqm  Y.  3. 3 ;    22.  i ;
6869:Ikät^  'rynt    masdqm..aat  mr€oH^Xvtxz.,\ jnier  I  1)    "rö  mazda  V.  2.  if.;  usw.;    — j  dim  p9r^sat  sarai^uslrS  -rahe  (statt  Akk.) ' masdi    Nile  i ;    —    wii    mraot  (Stverz-,  [ nnter  1  3)      °rJ    masdä    V.iS.i;  usw.;  — miinm    .  .  y5   gimatte    'rät    mazdai  Yt. ' '''■53;    8.  to',   — frSmraot  °rS  mazda  Y. M.  1; — jiimäi ..paoiryS  maiyänqm  apsnse^ oum    y3     "rö    mazdä    V.  2.  2;  1 ;    —    äat ioxta   *rj  masds  V.  2.  21,  40,  42;  31,  Vr. 3.  3,  Y,  10.  9;  — paiti  sS  aoxta  'rS  mazds A.4.6,  H./.  2,  7,  P.27,  FrW./o.40,  Nik. 2;  —   aite  sl  vä^ . .  "rS  mazdn  främraot zara^ultrai  Y.  7/,  14;  ig.  i,  15;  —  rätayS ..*yqm    °rv  mazdil  xaraisuiträi /ravavaca frä    tara^uitrS  gaiHäiyö  ..  Y,6§.g;  — ja'ia    dim    isat    °rS    mazdh    V.2.32;  — jaia  . .  zaois  mana  yat  °rahe  masdä  Yt. ir).%z;    &35;    —    xmaoi:ra    (sd,    auch fdSt.)   'rahe  masdä  Yt.  7.0,  usw.;  — j;As- maitie  'rahe  mazda  Y._^.  i,  22.4,  23;  — frasasti  °rah*  mazdil  Y.  S.  i;  —  staotala .  .  yat  a^a  'rahe  mazda  Vt.i}.  6;  —  /ava 'ra  mazda  yasrum  . .  vahm>mca  Vr.  21.  a; P._3P;    —    ramasf    ti  'ra    mazda    "hrlsHt pars  anyäis  ääman  Ny,  /.  i ;  Y.6S.X2,  Yt. 7.1,  V.ig.25;    —  fumahl  iyiJmS    *'ra.- wiazdä'"'*    Y.  5>y.  3;    —   yat   zaota    'rsm ma-uiam  yazäiti  N.  70;  Y,  25. 4,  57.  a,  V. 7q.  19,  Vt  6.  4,  77. 18,  Vr.  jj.  I,  i8. 1,  23. 1, G.5.S;usw,;  —  kö  mqm  staoiti  yim  'r^m mazdqm  H.7. 3;    —    'rai  mazdäi  haomq äJoAayamahi  Y.  24- 1 ;  Vr.  //.  16,12.1;  — zbayamahi    JrJnämahi     mqm    ytm     °r>m mazdqm     Yt/2.3(?);    Vyt2.^(;    —    'nm mazdqm    danyo.yas/fmca  (si)    hqm.parl- timca  H-2, 14;    —    ks  itvqm  yim  °rgm mazdqm  . .  mazista  ibaisatiha  tbaisayeiti  V. /iS'.6i*;zitY.(?.8PiiZ.; — mä  zl  ahmt  nmane . .  fnm  i-aocata   mqm  yim  'nm  mazdqm yaia  ..  P.  17;    —    i^a    dim  ^ara-cinasti yim    'nm    mazdqm     .  .    damabyS    Y.  ig. la.        a)  in  Verbindung  mit  andern  Gott- heiten: 'rahe  mazda  . .  varahSus  mananks ..asahe  vahisiahe  .  ,  xia^rahe  vairyehe.. tpmtayB    ärmatöil .  .  haurvatä  amir^täta  , . .  ^ui  urune  gSUs    lalne  .  .  ä^re  °rahe  1 mazda  Y.  70.  z;  /.  if,,  57.24,  Vr.  i/.  16,  j ^-  5-  5«  V.  7p,  1 1 ;  —  -räica  mazdäi  srao- , s.Wa    a^.li    rasnvalta    razilläi   mt^räica Vr.  //.  6;  Y.  4. 2,  Vyt  i4;  —  «Äu  me  'ra , mazda   uäa    üpS  urvar&sca  usia  daine  .  . , VlÄ  29;  23.  a.)  bes.  häufig  mit  den
7562:mit  uPa  'beachten,  (Bitte)  erfüllen'; surunuyä  nS  yasmm  . .  xsnuyä  ns  yasn>m .  .  upa  nS  yasrum  ahlsä  (2SOM-)  "hör auf  unser  Gebet  . .;  lass  dir  unser  Gebet gefaUen,  erfüll  unser  Gebet"  Y.ö'Äg;  Yt. /o.jz  (wo  ahiia^.
8268:—  ■)  iBild.   S.  asrutfin,    iKonstr.  s.   'flA-  I  5.
8612:•  g.  •'uz-iraidyäi''  Inf.  'sich  zu  erheben, sich  aufzumachen':  a/  tS  trisi  nöit  asrultä (sd.)  fairyaoyis  uz'  para  hyai  mH  ü.Jimal suraoüi  ". .  befahlst  du.,:  'Mach  dich  auf, bevor  dass  mein  Sr.  herzukommt'"  Y.^j. 12.  a)  mit  Inf;  uz°  *a:S  sar^anil (sd.)  sJngAaAyJ  V.  43.14.
10323:—  daitya  draona  i^arS  *mafjaile  (sd.) nöil   '^a»qm    asruiti  aslryeili  ti.  30;  30;
11017:—  kava^bya  p^aHbya  x^a^diyäia  varsa V.  tf.  46;  —  zara%ustrMn  atnm  pairi.- yaozdd^snlim  gä^äsca  srävayanttm  Y.g.  1 ; I —  :^ar>nte  vahistS  urunaica  pa%mainyB.- '  timB  Y.Q.  1 6 ;  —  ä"^  urva  c^'aZc'a  . .  daffiä I Y.  46. 11;  —  asrustim  aktmlä  manB  Y. |_J3. 4;  —  »1?  urvä  gJidca  atyä  Y.  2p.  5;
11029:—  laimye  .  ,  uruiiaSca  Yt  i~.  22;  — kaittibyü  . .  xsmatbyaca  Y.  5y.  5 ;  —  haurva- tsts  ,  .  amfr.tälasca  Y.31.  6;  — jyai7u? ,. vasS-itdii^a  Y.5_j.9;  47.6;  —  yaää  hvB arf hat  yl.iyaoianasiäY  .31.16; — akurahya xratSiJ..aiaatca  Y._j2,4; —  yeMi  hatqm ..vanhs .. yärahqmlä ..  Y.2-.\y,  —  as>m  .. manasla  vohü  Y.  28.11;  —  aiaAya  .  . vaahSusca  manat^hs  Y.33.  3;  —  vanhSui manai3hs..syaokana . .  spmtqmia  armaitjm Y.34- 10;  —  Aatiuharyne  . .  hSyUmla  dH- ^nm  Y.ii.\;  —  tä  urvata  ..  :^Uicai> ^miti  Y.30. 11;  —  ;tarff  .  .  gju/cä  urz'a Yt/^S4;  —  masdä  yasrum^a  vahm9m?ä (beide  als  i.  Glied;  Sp.  567  u.)  ..  ^ulca västrpm  Y-33.  7 ;  —  vaahsui  xralüm nat9h3..gSusca*urvq>i»mY.28.\.  a)  in auffdlliger  Stellung:  yS  anhai  asul  . .  hu-
11369:(Sp.  23  u.):  *aevayaäl  aisS  bar3Smd.st)r3iti raiu/ris  "a.\u^  schon  durch  eine  einzige  .." N.  103;  P.  24';  —  *Sy?miit  .  .  vaäm  gä- %attqm  asruhm  (sd.)  N,  103.  b)  beim Kompar. :  vTante  (sd)  avat  vlsmtaeia . *matyaslit  YL7_j.73;  *Vytjo; — in  auf-: fälliger  Stellung:  masyB  i^t.)  va  aAmJt^iJ V.^50'"',  c)  beim  Superl.:  »il^ma^it .  .  stärq/ii  (sd.)  ya%a  /lar/  vayhanim  F. 4^\  —  nit>ma(sd.)^ii  *haoma.haiH^  .  . kazavrayiiyäi  asti  dalvanqm  Y.io.ö;  6';
11398:•  j.  £ina-  Pron.  interrog.  'welcher?  wer?'; i)  als  Fragewort,  an  der  Spitze  des  Satzes: 'ntnt  i^ar>^3m  frabaräi  °ti?m  yaom  Jra- barati  ayatfhaltam  vä  srum  (sd.)  vä "worin  '*  soll  er  das  Essen,  worin  '*  das  Bier bringen?  In  einem  Gefäss  aus  Eisen.." V.  iü.  6.  z)  als  Indefinitum;  a)  im Relativsatz,  enkl.  hinter  dva-  'zwei  be- liebige, irgend  zwei':  münm  .  .  yim dväcina  (ND.)  pihe  (sd.)  halimna  .  . zbayeiti  Yt.  10.  84.  b)  im  negativen Satz,  enkl.  hinter  aeva-  'ne  unus  quidem': yS  asrul^aoso  vä , .  nsit  dim  Hram  "  vääm *aiwyäs  nöit . .  anaivisli  (sd.)  astryeiii  N.  S4.
=== BRT eagle/arva ===
7718:•  j.  9r»zi-fya-  m.  i )  'Adler"  (nur Komp.)  i)  Name  eines  Bergs  oder Gebirgs:    ahmat    haca  garayS  fraoxsyan
7721:•  j.  «rszifyö.parana-  Adj.  'mit  Adler- fedem  besetzt":  isavasca  'na  V.  77.9;  Yt. /0.39,   lOI.
8420:Ableit  aus  *Hpairi,iaena-  Adj.  'was  über  die (Flughöhe  der)  Adler  hinausgeht',  mit  V^Jdhih in  der  2.Silbe,  S  'twa.  1  aE.0  —  inp,  (Pü!) apärien.  —  0  Anders  KZ.  38.  292.
17240:Ar.  'biäsa-  m.  Name  eines  Raubvogels'),  — ai.  bhäsa-  m.  (auch  als  EN.);  mp.  bähai  EN. (=  ai.  ikäsaka-  EN.\  S.  noch  Marquart EranSahr  128.  —  ')  Zn  gr.  ^n;  {eine  Adler- att)  s.  Bthl.  IF.  8.  235.
20369:ai.  mfga-m.  'Waldtier'  (Gazelle),  auch'Vogel'; np.  murf  'Vogel;  Huhn'.  —  Pü. :  mun:  — ')  Nur  für  V,  J.  1  gesichert;  s.  Db».  VglS. /.  129.  —  »)  Wie  Adler,  Geier,  Hubn;  im Gegensatz  zu  iv^-.  ~-  J)  Im  Nebensatz  fehlt das  Verbum ,   etwa  ufia,'iyäya.
24514:•  }.  vispö.biä-  f.  Name  eines  mythischen Baums:  upa  avqm  vanqm  yqm  salnake yä  hiiittiie  maiilm  zrayatths  vpurukasahe yä  kubil'  }r^jwS.Us  yä  vaoce  'bis  (NS.) nqma  yqm  upairi  urvaranqm  vUpanqm taoxma  nilayat  "auf  jenem  Baum  des Adlers,  der  inmitten  des  Sees  V.  steht, der  gute,  kräftige  Heilmittel  birgt,  der  K
25786:•  j.  'saena-  m.  Name  eines  grossen  Raub- vogels, wohl  des  Adlers:  ya'äia  Aau  masa m»rrfll  'nS  Yt.  l4-A^s  —  "/"^  avqm  vartam yqm  •nake..yä  vaoh  vTspS-^i/ (sd.)  aama YL12. 17.
25787:KompE.  —  VgL  'saina-  EN,  —  mp.  sinmun; np.  (Npü.)  änmur^;  ai.  vgL  lyeni-  m.  'Adler, Falke'  (S  po.  1);  s.  dazu  Hbm.  AGt.  /.  499,
```


## [2026-09-04T19:14:41.057Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT Träne ===\" && grep -n -i 'Tr.ne\\b\\|Thräne\\|Trane' BRT.txt | head -20 && echo \"=== BRT arva ===\" && grep -n -E '(^|[^a-zA-Z])arva|aurva' BRT.txt | head -20"
}
```


### [2026-09-04T19:14:41.132Z] TOOL RESULT

```
=== BRT Träne ===
5638:5.120;  —  ustrane ..  yö -snam  ..  mattstem  i_  «,•„_;,_   ,,7,7-,   S  "  18    Vo  z";-    ■
5925:'asrai<-  n.  'Träne';  at.  äirav-  r.,  np.  ars.  — "azan-,  an-  Part,  lum  V.  U3-;  s.Bthl.  1F.  jO. 195.  —  ')  NA.  trennt;  s.  ebd.
27402:''  m.  'Träne, Weinen':  aal  ahe (näml.  haraevahe)  paityar^m  fräk^rmtal anr3  mainyus..  *'k?m^a  ifria'ii3(sd.ya  V. 7.8.
27403:Zum  V.  irasi-.  —  np.  sirisi  'Tropfen,  Träne'. —  Pu.!  irc'a  (in  Avf.-Buchst.).   —    ■)  NA.  sa-
=== BRT arva ===
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
2475:—  dr3gvä..ahya  fyao^anäis  akut  *3  fyqs  a^a^ara(sd.)  aya'^^  ra/u/risN.54;  — _>■« manatfhö  Y.47.5;  —  y^  •■  ^^yi^  zaohng  .tanup^rt^ah^  apa.rao^tmnaAe  (sd)  *a)a- usus  vann^ng {sd.)  Aa/aiteY.4S.4; — yimö\yaurva  *aya'^^'^'>  ralv/ris  Vi. $4.  b)  Das ..  yal  kirgnaot  airihe  x/a'iritoa  .,  Y.^.  4;  j  (subst)  Pron.  dem.  steht  an  Stelle  des  rel.
2497:b)  substantivisch:  *ydhä  *i}is'^^ iiä  varsiaiis  yä  dälä  atihius  paouruyehyä ralüs  ^■ao^anä  razUtä  (sd.)  "velut  (est) secundum  eas  (leges)  . .  quae  (sunt)  leges vitae  prioris"  Y.  33. 1 ;  —  Aaemö  aiibis (ab  Dat)  yöi  aurvantö  Atta  taxüsti
2550:äJffj  ti  'take  paiti  ..  V.22.2f.;  —  Da.'  aoAvo  (Stvetx.)  yal  as/tainti  Y.i^.6  \isw.; in  Verbindung  mit  anya-  Du.  (s.  i  b):  —  'tagsam  sünam  ..yimpasuiJiaurvamca.. asUm^mastrrfttqm  vispacayö*>nastr?inqm  i  V./^J.S;  —  'farahqm  urvaranqm  yat  ätri.- amqsta  fsd.)  ''i^arö.cikaya  *°le  anye  cika- ■  ciirranqm  V,4',75;  —  'ttm  ratümca  .. yatö  "wenn  einer  ,  .  und  wenn  einer  ,  .  \yim  maiaydhanmaim  A.j.3(?).  b)  sub- vcrletzt,  so  sollen  sie  dies  und  jenes  . ."  stasA\v\&c\\- 'ta(^T>.)äb3r3ta*sraosiivariza F,_jc  b)  adjektivisch:  j'iT/fl/ire'a/ara.-  vicarayaDm  "die  beiden,  der  .^.  und  der iri^yeiti  kva  "tarn  xsapan»m  . .  *vanAaiti  Sr.  .  ."  N.  jcf ;  —  cval  'te  (ADn.)  stai- "wenn  ein  Gläubiger  stirbt,  wo  weilt  asi\tiüa  bar>iis^a  ..  nasus  .,  fräsnaoiti dem  Tä^  (des  Todes)  . ."  H.  2.  i;  — yö  "..  die  beiden,  das  Bett  und  das  Polster .." . .  upairi  kunanm  (sdL)  manö  baräi  i-up^m  V.  7.9;  — ■  azim  °ta  (APn.)  zaota  zlsJi  (sd.) 'tfm  paiti  zmämm  aUariin  uri'a  kllayäi  ..  /rasrao^r?mca  /ragl>r>mca  . .  Vr._j.7; (sd.)  "wenn  einer  . .,  so  . .  während  der  —  't^m  nitamim  As'>rjm  '^rivacahim  (sd.) ganzen  Zelt  (seiner  Cberhebung)  .  ."P.  "id  minimum  Aj^/um:  triverbe"  F.  27b; J7.  a)  wo    wir   'solch'   brauchen:  yö  —  haomü  kutö  .  .  ava    'te  ahuta  .  .  "ge-
2686:*zamarigusa    avazat   vXspe   daifa    Yt /<?.       AbleiV  aus  ■arr'OB.u'ajflZw. 'elf;  vgl.  tF,  S  ?/o 81 ;  —  yahmai  . .  aurvantö  . .  v3sa  '^an-  ■     aK  und  IF.  p.  245.  —  Pü. :  yHdahum. }aianie   °va   caxra  (sd.)    Yt  10.136;    —  •  j-    aeväkam    Adv.    'zugleich' (?):    aiv aim  .  .  yß  t0  °ve  säsnä   (sd.)  gäsatä    Y.   narqm  asaonqm  ahunvitim  ga^qm  frasrä- ^9.8;  YtJ7.i9,2i;    —  yö  nö  °v6  at  U  vay'nti  Vd. /2.
3194:•  j.  "ataurvayö  i'ja  ßityant>m  västrlm vasByaanai  intam  hmSnhin^  Yt/0.60.
3368:—  yaisa  ni  d.ltl  . .  ''i^a  nä  >rJedüm  V. 5^-5>35-^'> — yit^ä  iä^aca  dahms  staota yesnya  haurva  daoaiti  '%a  ratu/rii  N. 3~;  —  yd^a  . .  nminopaitlm  paiti  tard.- pi'iw>m  dai'hyat  'ia  astryäH  "als  ob  er
3386:aS-aurvan-
3394:Ableit.  ans  lAaurvan-.  —  ai.  vgl.  äihmvatfä-
3397:•  j.  aihaurvan- '':a^a«r»n-,  äSravan-'' m,  'Priester'  im  Al!g e meinen ,  von  dem, der  Priestetqualität  besitzt  und  priester- liche Funktion  verrichten  kann  und  darf: uUa  nS  zlte  -va  .,  zara^uslrS  YLi_y.94;
3480:mit  avi  'einholen':  yest  ahi  paurva.- nafmät  aal  "lam  avi  nmänaya  (sd.)  yezt paskät  aai  ma'm  avi  apaya^sS.)  Yt.i&.a.
3583:—  ma%rym  spmttm  . .  pmrumca  . .  'r^mca V.  4.45;  45;  —  ahun?m  vairJm  . .  Tim sraoidyehya  (^^  frasrüiti  Y.  5. 14;  — apanmta  tiais^mi&A.)  G.3.T, —  'raheca yamahe  haplanhatdis  Vr.2/.o;  0,4^;  — ranuhlsla  a'A  .  .  hupaurva  (sd.)  vahehiS Ti/"  räsaintü  ¥.52.3;  —  aiwiea  'rim patiia  'rym  apsca  paurvalibya  "und  (man soll)  einen  zweiten  (Rüden)  und  dann noch  einen  weiteren  (zulassen)  und  zwar (soll  man  ihn)  gesondert  von  den  beiden ersten  (halten)"  V.  i^.  48.  3)  '>  der  Zeit nach 'der  spätere,  kUnftige'rja^a  mä  'racil (NPm.)  saoiyanis  stavqn  V.9.  2;  — yastä datrSMg  °rö  .  .  tarS.mqstä  "wer  darum künftighin  (eig.  posterior)^  den  D.  ..  auf- sagen wird"  V.  4:5. 11;  —  huzantSus  paiti •raya  YL  13. 134.  a)  mit  ayan-  n.  'der spätere  Teil  des  Tags,  Nachmittag':  */ra- \aire  ayqn  bavaiiii^A.)  hubar,rS  ..  a',a  "re ayqrt  duWirjm  ". .  dann  am  Nachmittag (kommt)  das  Unglück"  Aog.jJ.  A)  ASn. 'r?m,  'ram  und  IS.  °ra  als  Adv.  'postea, später,  künftig' :  yezi  nairyS  aukat  pasca hl  pourum  (sd.)  paiti.hin£öi^  paitisa  "r^m V.ÄSS;  v,%;  —  \mätyi^hy(r'ramimam dipim  patiparsiltiy  .  ,  BL4.8;6,  15,  ^.y,
3777:gaikaAü  tanusi^ä  Y.^J.  7-       2)  Praev.  (mit 'ak;gam-,  'bar;y/th-,  valn-  usw.).        a)  bei Ellipse  des  Verbums:   "wi?a  aparpm  (sd.) paiica    aparam    apnca  paurvaäbya    V.  75, 48;  —  asäaüä  haiä  van/iSus^il  mananhs vankyuscS   xla>rilt  staotäis  '^Tnifl  ahum staotSibyö  °bT  ux'o/l    '^wüt  uxüSibyS  yasnH %wät  yasnsibyd  "und  um  des  ASa  willen und  des    VM.  und  des   guten  XS.:    Lob- gesänge (häufen  wir)  nunmehr,  o  Ah.^  auf Lobgesänge  und  Sprüche  auf  Sprüche  und Gebete  auf  Gebete"  V.^j,.  10";  —  huxsa- %rSJ»m!li  (sd.)    .  .    xsa'inm    ahmai   hya^ 'bii^  dadsmahica  .  .  Y._Jv5. KompA-i  Ableit. —  aLiiM/,  mp..rai*,  np.a/". —  Vgl.  laii,  aei.  —  Pü. :  afar;  (in Komp.  auch): d/f  und  wepgelassen.  —  ')  S.  lu  aiiaiwülay- No.  I.   —    ')  Man  kann  aus   dem   vorherg. Ahsatzdad3maideetgiaT.Ka.  Gdn.n  Übersetzung GlrPb.   3.  32    ist    mir   unverständlich.     Pä.: släyisn  i  IS  öhrmatd  am  haf  släyi'snän  apar,  Sü. : ilulih    te    a-ämin    slulibhya^    utirflalarä.      — ))  Man  erwartete  die  selbe  Redensart  wie  V.
3896:*)  Die  vom  Beginn  der  Abenddämmerung  bia MiUernaclit  reicht  und  in  zwei  Abscbnille  ler- ßllt:    hü  fräimöMlay  -and  irizaurvaiia..     Vgl.
4081:•  j.  afsman-  n.  'Verazeae  (der  Gä^rJs)'": tiSranqm  kaurvafaoiryanam  . .  haitilca "manaca  (AP.)  '^  vacas^a  vacastastlmla  (sd.) Vr. /J.3; — vfsp?m^a  'man^m{Pi&y  yasa- maide  Y.  Ji.^;  —  aitatca  vacö  .  .  %ri.- afsm»m  (sd.)  . .  kais  Al  'man  (NP.)  ". .  wel- ches sind  seine  (des  AAunaVairya)  Vcrs- zeilen?"  Y,  19.16.
4115:FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g,  1,44,  lt. 10,  Yt//.  19; —  iaÖx  dusda  'ra  mainyö V.  i^,  1 2 ;  —  *'rahe ''  *mainy9us  duzdamanH Y.  Ö/.  2;  V. /p.6;  —  skutara  "ra  mainyö V.  79. 3;  —  "rS  mainyus  pouru.mahrkS (Stveri.)  Yt  10. 97 ;  usw.
4190:•  '].  a-ohvä-,  g.  a-hvä-"  f.  i)  'Antrieb des  Willens,  Schaffensdrang,  Lebenskraft' : pairika  yä  duzyäirya  vlspahe  atiksui  .  . ' faröit pairi'in^misA.)  anhvqm  avaAisiiyät\ (sd.)  Yt.Ä54;  —  ava  m!  3zis  .  .  par5it\ fairrbnpm  (sd.)  arihvqm  ava.d}nnqn  sada- 1 yäfi  (sd.)  V.  i5. 19.  2)  'Antrieb  derl Seele,  innerlicher  — ,  Gemütsdrang,  Ge-j müt'"':  kal..*manS  asti  vT/aymii'tfm{s±) anhvqm  vjmar3zist?m  (sd.)  VL  /.  2 ;  —  ' virtzvatca  (sd.)  mat^  vansvatica  attuAa  j 'W.  62,10;  —  ye  kvam  ankvam  yaozdaite\ humatsilia  .  .  V.  ^.2i^>;  si  *PÜZ.,  lO.  19  I PüZ.;  —  dusx'arpnä  . .  asH5  asti  auuhaya  \ (LS.)  ".  .  ist  unfroh  in  seinem  Gemüt"  j YLJO.105;  —  aibl  ahväha  daxst^m  dilvOi\ (sd.)  Y.5/,9;  —  yatära  vä  dim  paurva frayasäiti  fraor^t  fraxsni  avi  manö  (sd.) zrazdälöii  ar^huyal*^  (oder  avuhyat)  i>  haca ". .  gern  in  sorglichem  Sinn  aus  gläubigem Gemüt"  Yt  /o.  9;  —  fora  vi  räki  am?sä spmtn  yasmmcä  rahmtmcä  firä  mana»hä ..  vaiaahä  ..  syat>^anä  ..  dw^iy«  (IS.) » Y.7/.18.
4241:•  j.  an-aoäa-  Adj.  'dem  kein  Verderben droht,  unsterblich':  aurvantö .  .  mainyus.- ii^ar?^a  'shihs  Yt  70.125.
4698:\)amm  Y.$4.2,  G,  j.6; — yä  {ar?ävi) 'vaiti fratalaili  Y.  Ö5. 3 ;  Yt.  5. 1 5 ;  —  a^tn  vatau- hlm  .  .  hrpsailTm  'vattTm  Y.  3. 14;  Yt /J. I,  7;  —  drvaspqm  . .  'vaitlm  YL9.2;  — fravaiayö  .  .  yä  'vaifli  Yt  13.  29;  —  at töi  atrjm  . .  *asXsttin  'vanhm  Y.j^4;  — tiiirim  .  .  'vant?m  YtÄ4;  —  vatianttm 'vant»m  Yt  21.  i;  —  °vatS  amai  'vatÖ virp^raynäi  'vat^yO.  »rütyi  'vai'iya aiöii  'vai^ya  astdil  'vaüyä  paurvatälo 'vai'i'yB  uparatälö  'va^byä  yazatoAbyö  Vr. g.i,.  b)  sonst;  uströ . ,  b)r?zB  "vä  Yt i.^.  1 2 ;  —  srlra  urusta  'vaiti  (VSf.)  .  . UfTaireY.it^.iB,Vyt22; — srayarfhö  vouru- ka?ahe  'vatö  Yt.<S.46;  —  vasnm..  zaröil ayanhö  frahixt»m  'vatö  \L  10.96;  —  'vat iimäfum  Y.  57. 10;  —  ptiüm . .  yim  aiwatö 'vantim  Vyt.^;  —  'vaitlm  sitiqin  dävöi (sd.)  dr»gvasa  Y.  44. 14.  —  IstJm  . .  pouru.- sarioam  'vaitlm  Y.  65. 1 1 ;  —  hazö  "vat  Y. jj^.  iz;  —  yahmi  maza  'va  (NSn.l')J' '  iiiäälpm  Yt  10. 64  (?) ;  —  *°vata  vaca  F.3  e. AbleiL  —  ai.  dmm-ant-  Adj.;  vgl.  mp.  (PS.) amäz-nnd.  —  ')  %  jg4.  —  •)  Zur  Zusammen- Stellung  von  amai'aaf-  mit  ^'/ri^ravan ,  viri- %rasan-  s.  'amn-  2.-3)  Wenn  richtig,  wohl Neubildung  lum  NSm.  'va  nach  der  n-Dekt.
4752:F.  ff;  —  :^ahe  gayehe  :^airvats{5A^  "sähe Y.5.1,  Yt-Äii.  a)  von  der  Sonne: hvan^ail>m  'hm  raim  aurvat.asp»m  Yt. 6.\,  4,  6; —  hvar>.xsaitahe  'sähe  ra^ahe Yt-ö-o,  Y.22.24J  —  paurva.naemäi  °hhe hä  yaf  aurvat.aspahe  Yt.  10. 1 3.  A)  ins- bes.  von  den  dem  AhuraMazdäh  nächst- stehenden Gottheiten*':  yaia  vahm>m 'iaiibyS  Y.  21.2;  —  -saHi  . .  avarshe  ismti masyäkänAs  Aog.  41.  a)  sonst  in  Ver- bindung mit  spitUa-  Adj.  'heilig',  das  in GHapL'vor-,  sonst  nachsteht:  *vyäX3mca kanjamanimca  (sd.)  yat  as  'sanqm  sp?nta- nqm  banlnvS  *avarihe  as/0  y?mat^m  (sd.)
```


## [2026-09-04T19:14:58.182Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5918,5930p' BRT.txt; echo \"=== PHD āluh / ars ===\"; grep -n -E 'ʾlwh|aluh|āluh|eagle' PHD.txt PHD_mackenzie.txt | head -20; echo \"=== PHD ars ===\"; grep -n -E \"^ars |[^a-z]ars \\[|'ls'|tear\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-04T19:14:58.294Z] TOOL RESULT

```
•  j.  a-svar-  :  'ssr-  n.  'Morgendunis  el, -dämmening':   'sSiri  (LS.)  süirim  ispmnS .»  j.  'a-srata-  Adj.  (fem.  'tä-)  'nicht  ge-
YtÄS9;  —  dulxraiUm  .
•  j.  a-sravayant-  Adj,  'nicht  vortragend, aufsagend,  rezitirend';  a)  mit  Akk.:  yB gaisS  (NS.)  'yS  tiaimpm  yäri.dräjJ  "wer  die G.  ein  halbes  Jahr  lang  nicht  aufsagt" N.  44;  41-45''.  b)  ohne  Obj.  '(die vorgeschriebenen  Gebete)  nicht  sprechend': yS  salte  haurvqm  tarasca  xsapatum  ayo' Z)mns  °yif  amarä  V.  /Ä  5 ;  —  *frasrävüy3 rüiufris  tidit  *'°yS'^  N.  104.
Vgi.airä!'aya/.ffä%ä-.  —  Fä.s  asrülär,  ke  gäsSn ne  sräyit  oder  ya%!l,  Jni  afräi sräyün.  —  ')  Hds. (t\Täv'\  die  Echtheit  der  bds.  I.esune  ist wenigstens  nicht  wahrscheinlich;  dach  &.  Aog- SrTi.
•  j.  *"a-srävayamna-''  Adj.  'was  nicht  auf- gesagt, rezitirt  wird':  'ii3t  paiti  ahuiia^ vairyat  "ohne  dass  der  AhV.  rezitirt  wird" N.  tiS'
Pü. ;  pa  asrSyiJii.  —  •)  So  T ;  Ausg.  äsr'.
•  j.  *asrü.azan- '*  Adj.  'Tränen  (treibend sva.)  vergiessend' :  'z3nS  (NP.)  hilt>nte anuxajand  (sd.)  takahe  Yt.  JO.38.
'asrai<-  n.  'Träne';  at.  äirav-  r.,  np.  ars.  — "azan-,  an-  Part,  lum  V.  U3-;  s.Bthl.  1F.  jO. 195.  —  ')  NA.  trennt;  s.  ebd.
1  Morgendunkel  sich  das  Morgenmahl
suchend"
Yt.  14-  2C
Eig.  'wa
s  bis   2um
=== PHD āluh / ars ===
PHD.txt:189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagómand [k mk’ wmnd] unwilling. a-kanārag ['kr?]k! | M ?qn’rg] unlimited, boundless. ~ih: boundlessness. a-kard Pārt! | (M °gyrd)] not done, undone. Akoman ['kwmn! | М ?qwmn] Evil Thought, an arch-demon, akómand ["£wmnd] evil, harmful. alā [Py] oh! alas! Аар [STLA, STRA < A £t ;?lk! | (М rel side. alálag PPH! | N lala] anemone. ālāy-, v. ālūdan. Aleksandar Piksndl | M *Ixsyndr, N Iskandar] Alexander (of Macedon). almās(t) Pim?s(t') | (M ?rm?s), N almas] steel; diamond. аадар [?/wtk'] defiled, polluted. АҺ: defilement. ālūdan, ālāy- Photn!, *Pd- | (M ?rwd), N ~] defile, pollute. Aluh Plwh | M "If, N ~] eagle. Xum [lum] millet. N~ amā [LNE < A l-nh | М ?*°h, N má] we, us. Amadan, āy- [Y ATWN-tn! < А y twn, V*th | M?mdn,?y-, N ~] come. amahraspand [?mhrsbnd | M (?)mhr’spnd] a Holy Immortal, a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [?m?1-] reckon, calculate. ~išn: reckoning. a-marag [mlk') countless. amaraģān [?mlk’n'] generality, commonalty. ~ig [-yk'] general. ~iha [-yh’] in general, generally. a-marg [mig] deathless, undying. ~ih: deathlessness, immortality. ámárgar [?m’lgl | N ~] reckoner. amāwand [?m'wnd] powerful, strong.
PHD.txt:308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
PHD.txt:398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
PHD.txt:1720:eagle āluh, dalman, humāy.
PHD_mackenzie.txt:984: Iluh [,lwh I M "lwf, N .....,] eagle.
PHD_mackenzie.txt:1854:dalman [d'lmn I N dal(man)] lammergeyer, eagle.
PHD_mackenzie.txt:2951:humay [hwm)y IN ......] a bird of good omen; eagle.
PHD_mackenzie.txt:6464:eagle aluh, dalman, humay.                   endure burdan, pattiidan, widar-
=== PHD ars ===
PHD_mackenzie.txt:1183:ars ['Is I M 'rs, N ---] tear (drop).
```


## [2026-09-04T19:14:58.686Z] TOOL CALL #14: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/ /home/sfmqrb/git/rishe/tools/ 2>/dev/null; ls /home/sfmqrb/git/rishe/data/verification/ | head"
}
```


### [2026-09-04T19:14:58.749Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/:
ANOMALIES.md
extracted
EXTRACTION_SPEC.md
research
translations
verification

/home/sfmqrb/git/rishe/tools/:
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
```


## [2026-09-04T19:15:02.345Z] TOOL CALL #15: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-04T19:15:02.394Z] TOOL RESULT

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


## [2026-09-04T19:15:10.167Z] TOOL CALL #16: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['KLN','BQT','HRN','MON','WEB','FSD','AHD','POK']:\n    print(k, d[k].get('page_offset'), '|', d[k].get('lookup_hint','')[:300]); print()\n\""
}
```


### [2026-09-04T19:15:11.904Z] TOOL RESULT

```
KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d

HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

MON None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe

WEB not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.

FSD vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.

AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru

POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
```


## [2026-09-04T19:15:16.042Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN tear ===\" && grep -n '^tear' KLN_1966.txt | head && echo \"=== KLN eagle ===\" && grep -n '^eagle' KLN_1966.txt | head && echo \"=== KLN aquiline/aqua ===\" && grep -n '^aqu' KLN_1966.txt | head -20 && echo \"=== KLN eau ===\" && grep -n '^eau' KLN_1966.txt | head && echo \"=== KLN island ===\" && grep -n '^island\\|^isle' KLN_1966.txt | head"
}
```


### [2026-09-04T19:15:16.173Z] TOOL RESULT

```
=== KLN tear ===
36356:tears’,  <|'<4Xt<;,  ‘scissors’,  Lith.spd/r'az'(pl.),‘shives  of flax’,  OSlav.  ra-splatiti,  ‘to  cleave,  split’,  MLG. spalden,  OHG.  spaltan,  ‘to  split’,  OI.  sphaiayati , ‘splits',  phalati,  ‘bursts’,  phalah,  ‘plowshare’, prop,  ‘that  which  tears  the  soil’,  OSlav.  plevg, pleti,  ‘to  weed’,  pleveld,  ‘weed’.  Cp.  spoil,  v., despoil,  spoliation.  Cp.  also  Spaiax,  spall,  spelt, sphalerite,  spill,  ‘to  flow’,  spool, spoil,  tr.  and  intr.  v.  —  ME.  spoilen,  fr.  OF.  es- poillier,  fr.  L.  spoliare,  ‘to  strip ;  to  rub,  plunder, pillage,  spoil’.  See  spoil,  n.
38345:tear,  n.,  drop  of  liquid  from  the  eye.  —  ME.  tere, ter,  tear,  fr.  OE.  tear,  contraction  of  teagor,  rel. to  ON.,  OFris.  tar,  OHG.  zah(h)ar,  MHG.  za- her,  G.  Zdhre,  Goth,  tagr,  ‘tear’,  fr.  l.-E.  *dakru- ‘tear’,  whence  also  Gk.  Saxpn,  Stxxpuov, Saxpujza  (whence  OL.  dacruma,  L.  lacruma,  la- crima ),  OIr.  der,  W.  deigr,  Co.  dagr,  OBret.  dacr\ cp. — without  the  initial  dental  sound — OI. dsru,  Avestic  asru,  Toch.  A  akar,  Lith.  asara, Lett,  asara.  Cp.  also  Arm.  artasuk ‘  (pi. ;  the  sing, is  artausr ),  with  change  of  dr-  to  rt-.  See  lachry¬ mal  and  cp.  train  oil.
38347:tear,  tr.  and  intr.  v.,  to  putfapart,  rend.  —  ME. teren,  fr.  OE.  teran,  rel.  to  OS.  terian,  ‘to  con¬ sume’,  far-terian,  ‘to  destroy’,  MLG.,  MDu., Du.  teren,  ‘to  consume’,  OHG.  zeran,  fir-zeran, ‘to  destroy;  to  consume  (whence  MHG.  zern, ver-zern,  G.  zehren,  ver-zehren,  ‘to  consume’), OHG.,  MHG.,  G.  zerren,  ‘to  tear’,  Goth,  dis- tairan,  ga-tairan,  ‘to  tear,  destroy;  to  tear  to pieces’,  fr.  I.-E.  *dere-,  *der-,  ‘to  rend,  divide; to  flay’,  whence  also  OI.  drnati,  ‘cleaves,  bursts’, Gk.  SspE'.v,  ‘to  flay’,  8sp(j.a,  ‘skin’,  Sopa,  ‘skin’ Sapaii;,  ‘tearing,  flaying,  separation’,  OSlav. dero,  dlrati,  ‘to  tear,  flay’,  Lith.  dir  it,  dirti,  ‘to flay’,  Arm.  terem,  ‘I  flay’,  W.,  Co.  Bret,  darn, ‘piece’.  Cp.  also  Toch.  tsar,  ‘a  hand’,  prop,  ‘that which  tugs  or  tears’.  Cp.  derma  and  words  there referred  to.  Cp.  also  darn,  dartars,  Derris,  drab, ‘a  kind  of  cloth’,  drape,  tart,  ‘sour’,  tetter,  trap, ‘clothes’.
=== KLN eagle ===
12531:eaglet,  n.,  a  young  eagle.  —  Formed  fr.  eagle on  analogy  of  F.  aiglette,  dimin.  of  aigle, ‘eagle’.  See  prec.  word  and  -et,  -ette. eaglewood,  n.,  agalloch.  —  Loan  translation  of F.  bois  d'aigle,  fr.  Port,  aguila,  ‘aloewood’,  fr. Gk.  ava>.).o-/_ov,  ‘aloe,  aloewood’ ;  see  agalloch. French  bois  d'aigle  arose  from  a  confusion  of Port,  aguila ,  ‘aloewood’,  with  Port,  aguia,  Sp. aguila,  'eagle'  (see  eagle). eagre,  n.,  a  tidal  wave;  a  bore.  —  Lit.  ‘water borer’,  fr.  OE.  ea,  ‘water’,  and  gar,  ‘spear’.  See aquatic  and  gore,  ‘to  pierce’, ean,  tr.  and  intr.  v.  —  A  var.  of  yean  (q.v.)
=== KLN aquiline/aqua ===
3260:aqua  fortis,  nitric  acid.  —  L.,  ‘strong  water’.  See aquatic  and  fort.
3261:aquamarine,  n.,  a  transparent  bluish-green  variety of  beryl  (mineral.)— U  aqua  marina,  ‘sea  water’, fr.  aqua,  ‘water’,  and  marina,  fern,  of  marinus, ‘of  the  sea’.  See  aqua  and  marine, aqua  regia,  mixture  of  concentrated  nitric  and hydrochloric  acid  (chem.)  —  L.,  lit.  ‘royal water’ ;  so  called  from  its  power  to  dissolve  gold, ‘the  king  of  metals’.  See  aquatic  and  regal, aquarelle,  n.,  a  water  color  painting.  —  F.,  fr.  It. acquerella,  ‘water  color’,  dimin.  of  acqua,  ‘wa¬ ter’,  fr.  L.  aqua.  See  aquatic.
=== KLN eau ===
12564:eau  de  vie,  brandy.  —  F.  eau-de-vie,  lit.  ‘water  of life’,  fr.  L.  aqua,  ‘water’,  de,  ‘from,  away  from’, and  vita,  ‘life’.  See  aquatic,  de-  and  vital.  For sense  development  cp.  aqua  vitae,  usquebaugh and  whisky.
=== KLN island ===
19923:island
19967:island,  n.  —  ME.  Hand,  fr.  OE.  egland,  igland, iegland,  ‘island’,  which  is  compounded  of  eg,  ig, leg,  ‘island’,  and  land,  ‘land’,  and  rel.  to  ON. evland,  OFris.  eiland,  ‘island’.  The  first  element of  these  words  is  rel.  to  OE.  ea,  ‘water,  river’, ON.  d,  ‘river’,  ey,  ‘island’,  Norw.  oy,  Swed.  o, Dan.  0,  ‘island’,  MLG.  oge,  och,  ouwe,  ou,  OHG. aha,  ‘river’,  OHG.  auwia,  ouwa,  MHG.  ouwe, ‘island,  damp  meadow’,  G.  Aue,  Au,  ‘meadow
19970:islet,  n.,  a  very  small  island.  —  MF.  islette  (F. ilette),  dimin.  of  isle,  ‘island’.  See  prec.  word and  -et.
```


## [2026-09-04T19:15:21.355Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- eagle ---\" && grep -n 'aquila' KLN_1966.txt | head -10 && echo \"--- aquatic ---\" && grep -n '^aquatic\\|aquatic,  adj' KLN_1966.txt | head -5"
}
```


### [2026-09-04T19:15:21.431Z] TOOL RESULT

```
--- eagle ---
3268:Derivatives:  aqueous-ly,  adv.,  aqueous-ness,  n. Aquila,  n.,  the  genus  of  eagles  (zool.)  —  L.  aquila, ‘eagle’.  See  aquiline.
3269:Aquilegia,  n.,  a  genus  of  plants,  the  columbine (hot.)  —  ModL.,  called  also  aquileia,  fr.  L.  aqui¬ la,  ‘eagle’.  See  next  word, aquiline,  adj.,  1)  like  an  eagle;  2)  like  an  eagle’s. —  L.  aquilinus,  ‘of,  or  pertaining  to,  the  eagle’, fr.  aquila,  ‘eagle’,  prob.  lit.  ‘the  dark-colored (bird)’,  fern,  of  aquilus,  ‘dark-colored’,  prop, ‘water-colored’,  fr.  aqua,  ‘water  .  See  aquatic and  adj.  suff.  -ine  (representing  L.  -inus)  and  cp. eagle.  For  the  form  of  the  word  cp.  L.  nubilus, ‘cloudy’,  fr.  nubes,  ‘cloud’.
3270:Aquilo,  n„  the  north  wind  (Roman  antiq.)  —  L. aquilo,  ‘north  wind’,  lit.  ‘the  dark  one ,  fr. aquilus,  ‘dark-colored’  [cp.  aquila,  ‘eagle’, prop,  ‘the  dark-colored  (bird)’];  see  prec.  word. For  sense  development  cp.  Gk.  xaixla?,  ‘north east  wind’,  lit.  ‘the  dark  one’,  cogn.  with  L. caecus,  ‘blind’  (see  Caecias). aquose,  adj.,  aqueous.  —  L.  aquosus,  abounding in  water’,  fr.  aqua,  ‘water’.  See  aquatic  and  cp. aqueous.
4419:bar,  n.,  the  maigre  (Sciaena  aquila).  —  F.  bar,  fr. MDu.  ba(e)rse,  which  is  rel.  to  OS.,  MHG.  bars, G.  Barsch  and  E.  barse  (q.v.)
12529:each,  adj.  —  ME.  xlc,  elc,  eche,  fr.  OE.  xlc,  which is  short  for  a-gelic,  ‘ever  alike’,  and  is  rel.  to OFris.  ellik,  elk,  Du.  elk,  OHG.  iogilih,  MHG. iegelich ,  G.jeglich,  ‘each,  every’.  See  aye,  ‘ever’, and  like,  adj.  and  adv.,  and  cp.  ilk. eager,  adj.  —  ME.  eger,  egre,  ‘sharp,  eager’,  fr. AF,  egre,  corresponding  to  OF.  (=  F.)  aigre, ‘sour,  acid;  harsh,  bitter,  rough’,  fr.  L.  acrem, acc.  of  acer,  ‘sharp,  pointed,  piercing;  acute, ardent,  zealous’.  See  acrid  and  cp.  agrito  and the  second  element  in  vinegar.  Cp.  also  ear of  corn.  Derivatives :  eager-ly,  adv.,eager-ness,n. eagle,  n.  —  ME.  egle,  fr.  OF.  egle,  aigle  (F. aigle),  fr.  L.  aquila,  ‘eagle’,  whence  also  It. aquila.  Rum.  acerd.  Proven?,  aigla,  Sp.  aguila, Port,  aguia,  of  s.m.  See  aquiline.
--- aquatic ---
3264:Aquarius,  n.,  a  constellation  and  the  eleventh sign  of  the  zodiac  (astron.)  —  L.,  ‘water  carrier’, prop,  the  adj.  aquarius,  ‘pertaining  to  water’. See  aquatic  and  cp.  prec.  word.  L.  Aquarius  as the  name  of  one  of  the  signs  of  the  zodiac  is  a loan  translation  of  TSpoxoo?,  ‘the  water- pourer’,  the  old  Greek  name  of  this  constellation, aquatic,  adj.  —  F.  aquatique,  fr.  L.  aqudticus, ‘found  in  the  water,  watery’,  fr.  aqua,  ‘water’, which  is  cogn.  with  Goth,  aka,  ‘river,  waters, OHG.  aha,  OFris.  d,  e,  ON.  6,  OE.  ea,  ‘water’, OHG.  auwia,  ouwa,  MHG.  ouwe,  G.  Au,  mead¬ ow  watered  by  a  brook’,  ON.  Asgir,  name  of the  god  of  the  sea,  ON.  ey,  OE.  leg,  ‘island’, Hitt,  akw-anzi,  ‘they  drink’;  cp.  the  Russian river  name  Oka,  and  the  second  element  in Sca(n)din-avia.  See  island  and  cp.  eagre,  tidal wave’,  ewer,  eyot.  Cp.  also  aquacade,  aquatint, aqueduct,  aqueous,  aquiline,  Aquilo,  gouache, Scandinavia.  For  the  ending  see  suff,  -atic. Derivatives:  aquatic-al,  adj.,  aquatic-al-ly,  adv. aquatint,  n.,  a  kind  of  engraving  with  aqua  fortis. —  It.  acquatinta,  fr.  L.  aqua  tincta,  'dyed  water’, fr.  aqua,  ‘water’,  and  tincta,  fern.  pp.  of  tingere, ‘to  dye’.  See  aquatic  and  tinge, aqua  tofana,  a  poisonous  liquid,  probably  of  ar¬
37199:Derivatives:  subaltern-ate,  adj.  and  n.,  subal- tern-ation,  n.,  subaltern-ity,  n. subaquatic,  adj.,  partly  aquatic.  —  Formed  fr.
```


## [2026-09-04T19:15:32.683Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef leafof(path, lineno):\n    txt=open(path, encoding='utf-8', errors='replace').read()\n    lines=txt.split('\\n')\n    upto='\\n'.join(lines[:lineno])\n    return upto.count('\\f')\nfor ln,label in [(3269,'aquiline KLN:?'),(3264,'aquatic'),(12529,'eagle'),(12564,'eau de vie'),(19967,'island'),(38345,'tear n.'),(3260,'aqua fortis')]:\n    l=leafof('KLN_1966.txt',ln)\n    print(label, 'line',ln,'leaf',l,'-> printed pp approx', 2*(l-12), 2*(l-12)+1)\nEOF"
}
```


### [2026-09-04T19:15:34.888Z] TOOL RESULT

```
aquiline KLN:? line 3269 leaf 63 -> printed pp approx 102 103
aquatic line 3264 leaf 62 -> printed pp approx 100 101
eagle line 12529 leaf 269 -> printed pp approx 514 515
eau de vie line 12564 leaf 270 -> printed pp approx 516 517
island line 19967 leaf 442 -> printed pp approx 860 861
tear n. line 38345 leaf 836 -> printed pp approx 1648 1649
aqua fortis line 3260 leaf 62 -> printed pp approx 100 101
```


## [2026-09-04T19:15:46.288Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nimport re\nfor i in [62,63,269,270,442,836,801,802,803]:\n    p=pages[i]\n    nums=re.findall(r'\\b\\d{2,4}\\b', p[:200]+' || '+p[-200:])\n    print(i, repr(p[:90]), '...', repr(p[-90:]))\nEOF"
}
```


### [2026-09-04T19:15:48.082Z] TOOL RESULT

```
62 'ive,  adj.,  approving.  —  F.  approbatif (fem.  approbative),  fr.  L.  approbative,  fr' ... 'er’,  and  ductus,  ‘a  leading’,  fr.  ductus,  pp. of  ducere,  ‘to  lead’.  See  aquati'
63 'c  and  duke  and cp.  the  second  element  in  viaduct,  ventiduct, aqueous,  adj.,  wat' ... '  See  arboreal and  vital.\narbuscle,  n.,  a  dwarf  tree.  —  Late  L.  arbuscula, dimin'
269 'for  measuring  the magnifying  power  of  telescopes.  —  Com¬ pounded  of  dyna-  and  G' ... '  -ly.\nDerivatives:  early,  adj.,  earli-ness,  n. earn,  tr.  v.  —  ME.  ernien,  ernen'
270 ',  fr.  OE.  earnian, ‘to  deserve,  earn’,  rel.  to  OHG.  amen,  arnon, ‘to  reap’,  OE' ... 'dj.,  pertaining  to,  made  of,  or  resem¬ bling,  ivory.  —  Formed  with  suff.  -an  '
442 'ains  in the  hip’,  compounded  of  Gk.  EoxEov,  ‘hipjoint’, and  itXyo ?,  ‘pain’.  See' ... 'ison,  subst.  suff.  of  OF.  origin,  as  in  comparison, orison,  venison.  This  suff.'
836 '.  —  ME.  taxacioun,  fr.  MF.  (=  F.) taxation,  fr.  L.  laxationem,  acc.  of  taxati' ... 'pa-rfa,  ‘rule  of’,  fr.  xpaxog,  ‘strength,  power, rule’.  See  -cracy.\ntechnocrat,  n'
801 'le  jack,  n.,  one  who  climbs  steeples,  chim¬ neys,  etc.,  for  making  repairs.  — ' ... '  (in  a  mortar)’,  OHG. stampfon,  ‘to  stamp  with  the  foot,  beat,  pound’. Cp.  est'
802 'afette,  etape,  staff,  stamp,  stampede, staple,  ‘bar,  wire’,  staple,  ‘commodity’,  ' ... ' (pp.  stratus),  ‘to strew,  stretch  out,  spread  out’.  See  stratum  and cp.  words  '
803 'there  referred,  to. sternutation,  n.,  sneeze,  sneezing.  —  L.  sternuta- tio,  gen. ' ... ' mark’.  See  stick,  v., and  cp.  astigmatism.  Cp.  also  the  second element  in  Pach'
```


## [2026-09-04T19:16:15.084Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nprint('leaves', t.count('\\f')+1)\n\""
}
```


### [2026-09-04T19:16:16.736Z] TOOL RESULT

```
leaves 903
```


## [2026-09-04T19:16:29.536Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i in range(266,272):\n    print('='*20,'leaf',i)\n    print(pages[i][:1200])\nEOF"
}
```


### [2026-09-04T19:16:31.157Z] TOOL RESULT

```
leaves 777
==================== leaf 266
۲ ۰ وا
آلان ِ پروزن‌بالان » ام ولایتی ونم
محله ایست ویسنی کوبند شهرست در ت رکستان
و نام کوهی‌هم هست1" .
لاو بسکون واو, آ تس شمله با را
کوند. و بفتح همزه‌هم درست‌است ۷ .
عندی ام درختی است که ازیخ‌آن دنگه سرخی
حاسل شودمانند رنگه رونای وبدان جامه رنگه
کنند و در دواها نیز بکار آید .
! لا » پروزنکلا»
بمعتی‌اول آل اس تکه
رخف سرنگه باشد .89 ۳
]لاس « یسکون لاوه « بنتح واو» بمعنی دیگدان و
سیخ ی فا 221 جایکه درآن آش روش نکنند - دوپارچشچوب
وانگفت راگونند ۴ رانیز کوبند که اطفال‌بدان‌بازی کنند یکی‌بز رکه
٩‏ ( - قدر سه زجب و دیگر یکوجك بمقدار بك‌فیشه
ختح لام » بمعنی لاله - وس‌های چوب کوچاك نیز میباشد .
ی اند وت ا سا و تن
همزه هم درست است ۴ . 9 آلودگی و عیب - ترداهشی وفسق وفجوروخیات
اک آزد ۱ مر خن آ من
۴ - تاب قپرش تیغ را الماس کرد برق خشمش کوه را آلا کرد
۱ سراح‌آالدین راجی « لفت نامه ».
۴ - مرش لال ( سرخ ) . پهلوی 21226 « بندهشن. یمبشی ۱۹۰۸ ص 4۱۱۷. فارسی نیز
لاله ولاله » طبری طفاغاهظ < واژه نامه۸4۳ ». ۴ بش ازه»۱۲۰ جنس مختلف آلاله
وجود دازد و آلالمهای اصلی شامل ۷۲اه 5ناللات(تلا 210 و جنس های فرعی‌آن وشفایق نعمانی
علانامعا عدمصعمه ر ختایق یچ عتلهانا ونافتهن لت.. . « کل کلاب
۷ ببعد * و رك : فرهنگه روستابی 4۸ :
چون دواتی بسدین است خراسانی وا باز کرده سرالاله بطرف‌چمنا «منوچهری4».
۵ و اران . از رشة 2
==================== leaf 267
کت ۱ آننک
و امٌال اینها باشد 0.٩‏
۲ لر - بروزن لاغر ۰ کقل و رین را
کوند مطلقا ۴ .
۷ ۷ ۱
بمعنی آلراست ک هکفل وسرین باشد مطلناً ۴ .
] ل‌طمفا - برکون ثالت » مهرودگین |
یادشاهان را گوبنده ویضی کویند اين, لفث ترکی .
است ؟ .
۲ لفده * - باغین قطمداربروزن آزرده,
بمعنی قهرآلود وخشمگین - وجنگه آورباشد .
۲ لو زه رن اه نش فاد
است و آن‌سرخی باش که زنان برروی مالند ۰
] فتن - بافاء بروزن ومعن ی آشفتن باشت.
۲ قشته مه پروژن و معتی آخفته ۱ هت
رردیکی و کی ودروش نامراد را نیز گوء بند.
ای او سار ء بل
الطيب را کویند ودردواها بکار برند ۷ - و مصغر
آهرهت ۸
۲ لگو نه سکاف و بروزن‌وععتی
آلفونه است که غازه و سرخی زنان باشد ٩۳‏ .
] ل معصفر « بکر ثالث ۳ نوعی از
ماهی درم دار ۳ 9 را نیز
نته‌اند .
آ مج - بن تلد وسکون نون وجیم»
آلوچه را کویند و آن میومایست ممروف ‏
آ لگ « بروزن آهنکه . کوی بلشد
که در اطراف قلمه‌حا بجهث محاصره و کرفتن
آ نکنند ومورچال همان است- و بسنی دبولربرا
کوبند که بجهت محافظت خود و حواله کماز
پرای قلمه سازند - وجنمی ازمردم را نیز گویند
که مردم. بیرون قلمه جابجا بواسطهٌ کرفتن قلمه
عصسدی: لشت‌نامه ».
۴ التمفا . اللون نمفا » هر پادشاهان ترث که با م رکب سرخ برفرمانها فش میکردد ۰
اين فرامن را منصوصاً « بارليغ التون تمغا * مینامیدند . «جنتابی ۳۱ *. ه‌ لغتی دد
« آرغدء » . رك : آرغده. ۲ -.لفتی درآ لگونه .
==================== leaf 268
آ و فك س بروزن باربند » تلم کوهیست
درهمدان که بالوند شپرت دارد ؟ . «
له » بنتح ثالث‌بروزن لاله ؛ سنبل -
الطیب را کویند و آن داروبی‌است که در دواها
بعربی «عقاب» میگوشد ٩‏ -
آ یز - بروزن‌فالیز» جفته ولگدانداختن
- وخیز کردن و برجستن ستور باشد ۷ .
روم درون‌قلمه بجهت محافت قلمه نعیین(۱)
کننهه .
]لو ۷ سبروزن‌خالو موماست ممروف؟ -
ومخفف آلود نیزباشدکه از آلودکي حست ۴
و داش و کور؛ خشت پزی را نز کویند . *
[ لوده داهی ه مرمدامقید - وفاسق
و فلجر و کتاهکار و عاصی را کویند .
۲ لوس « بروزن ناموی ؛ ناه کردن
بگوشةٌ چشم باشد از روی خشم و نز .
را وقتح دال بی‌نقطه . میومایست زرد رلک شببه نون و فتح دال بی نقطه . اسب و استر جهنده
پزرد لو ودخوی لکد انداز راگویند . ۶
۱ - پهلوی 8100 « بونکر ۵۱ » ۰ شهمیرزادی ألقثا , کیلکی 5218 ( کوجه)
ر0( , طبری لاه (آلوچه) « واژه تایه ۳۱۰ > . ۴ یکی از انواع دسته بادامی ها
که تم علمی آن 1000650162 کناتلنا۳ است «گل کلاب وا ۳
؟ - درکلیات مر کب مانند : کل‌آلو , خواب آلو » یشمالو :
جبله اعل بیت خشم آلو شدند که همه درشیر بز طامم بدند. مثئوی «لفت نامه».
۴ - ر4 : الوند . ۵ رد : آفك .
1 - حمزه اصفهانی در کتاپ الئنببه علی حدوث التصحیف (نسخهٌ خطی ) ومیدانی در کتاب‌السامی
فی‌الاسامی عغابرا به « آله » ترجمه کرده اند وهمچنین ابورسان بیرونی در التفهیم. حکیم‌موژمن
در تحفه کوید : « عقاب بخ
==================== leaf 269
]هاچ » بای بروزن تاراج , خاکی
باش د که تشانتیررا برآن صبکنند چه آماجگاه
جاییرا کوبند که نثانه در آنجا بهند - وبسعنی
تشانةٌ یرهم هست ۱ - و آلتی را نیز گوبند از
آه نکه برزیگران زمین رابدان شیا رکنند ۴ -
و تخت یادشاحانرا کفته‌اند - و يك حسه ازیست
و چهار حصاٌ فرسنگه باشد چه هر فرسنگی سه
عیل است و هر میلی مسافت دو ندا و هر ندائی
بغدر چهار آماج » پس‌فرسنگی‌بیست وچهارآماج
باشد ۴ .
آمار
1هادن » بتح دال و سکون دون .
بمعلی ساختن - و ساخته شدن - و پر و مملو
کردانیدن - ومهیا کردن وستعد نمودن باشد .
] ماه ه پننی‌ساخته و پرداخته ومهبا
کرده باشد ۴ .
۲مار _ ه بروزنآزارهمرشی اس تکه‌آنرا
استقا گوبند - و بمعنی تهابت طلب و تفحص
ونجسی باشد - وبمعنی حساب هم‌هست چهآعاره
گیر محاسب وحساي کیزنده را کول ویدشی
استفصا و تبم‌هم بنظی آعده است٩‏ هه
۱ - باين معتی در دزفولی 6 کاشفری (1 : ۵۳) آماچ را درلغات نکی‌بمعنی
هدف وثشانه آورده وبدیهی‌است که دخیل است ر‌ در کتاب «اللیات‌النوائه والاستشهادات‌الستائه»
ننامده :
چونیر انداختی برروی دشمن
بر کند. نبرتو زآ نان خالد درآماچگاه
جنر رکن کاندر آ ماجش شتی. ممدیدلت‌نلمه».
بر ز کر ب رکنده‌پنداری باماج وکلند
سوزنی* لت نامد».
۴ آماج توازبلخ بود تابپنج آب پرتاب توازبلخ‌بود تابف‌طین. فرخی«لفت‌نامه».
۴ - «امیر (محمدین محمود غزنوی) . . .آواز داد . . . که او را تنپا برند؛ حلجب
کگفت 
==================== leaf 270
آماره مات
] مارم ۱ بروژن و معثی آواره - آموخته است ۵ . #
وییعنی آعار است کهمرض استقا - ونهایت تفحص
.و تس - و ساب - و تشبم باشد ,
]ماس ؟ ‏ بسکون مين ی قطه »
بمعنی ورم باشد که برآمدگی است در انا خواء
با درد باشد خواه بی‌درد .
]ماه ۴ ه پروزن تا گاه . بمعنی آحلي
است که ورم و برآمدگی اعضا باشد .
آهای - بسکون بای حطی . بمعنی‌یر
کته ره اراخته د ومافته و صحه زوسیا
کننده باشد ؟ - و اعر باین معنی هم‌هستیعنی
پرکن و بیارای و مهیا و مستمد نمای ۴ .
| محته. بضم نالت بروزن تايخته , مخفف | شهر مازندران ٩٩‏ است .
کویند ۷ . #
وغین نقطه دار » بممنی نفع و فایده است ۸
و زیده و خلاصهٌ هر چیز را نیز کفته اند ٩‏
و بفتح اك‌هم درست است .
۱ مرک از : آمار۳-ه (یسوند) . رك : آمار . ۴ - آهای و آهاه ومای ؛
طری ۵610189 » « واژه نامه ۱۲۹ », کلکی 2۳0۵6 . ؟ ‏ مخنف آمانده :
نوی کوه رآهای چارآخشیج مسلل کن گوهران درمزیج . نظامی «لفت‌نامه».
کر لزع مونح: ۵ - رگ: آموختن . ۱ - ره : آمدن .
۷ - بارها درشدی بجلس خاصس ‏ گه نوا زن بدی وه رقاس
کا هگنتی شوخی آهدمای که نمودی بعشوه شعده‌ای. امرخ رو*لفت‌نامه».
۵ - بیکی دلو سی رکردد هرغ صد درم مرمرا شود آمرغ. سنائی «لغت‌نامه».
٩‏ - این معانی ظاهراً ازحدسهای مختلفی است که در بیت سنائی زدماند. < لغت‌ناحه *.
۴ - آمل ‏ در پهلوی ۸۱0۵ کرسی طبرستان . این‌تام مأخون است ازنلم فبیلهٌ غیر
ابرانی 
==================== leaf 271
آمله ۲ - ینم ثاكك و قح رابغ » دوائی
است کثیرالتفع وممرب آن «آملج» باشد . گویند
دو درم را از آن کوفه تا دوساعت درآب شیرین
بجوشانند و بمد ازآن ساف کنند و سه‌چپارلویت
درچشم چکانند ۰ سفید یرآ که ۳ بود سود
دارد .
]هن - پنتح الك و نون ۰ نود خومن
هیزم شکافنه(۱) را گوبند سوپشته ویشتوار؛ هیزم
ببتهرا ن رگفته‌اند - و بکسرالث یام مادرحصرت
رمالت یناه علیه السلام است .
آمو . نم تالث و سکون واو , مضفف
آمون‌است وآن رودخانه‌ای باشدمشهور وممروف.
واقم در میان ابران وتوران- وبسنی گوبند دهی
است که این رود خانه موسوم بآن ده است ۳
(۱) چش: شکته . . (۲) چك: ژند ویلژند.
وژمینی خم‌هست میان جیحون وفرأت .
] موت - با فوفانی بروزن لاعوت .
آشیان جانوران شکاربرا کوبند حمیویاز وشاهین
]هو یا - بکر فوفانی و تضانی بالف
کشیده , بلفت زد و پازن() کنیزك و پرستا
وخدمتکار (۳) باشد ۴ .
۲ موختگان ادل » اب ر ارب
صلوات اف علیهم اجمعین (4) را کوبند . *#
| مود پروزن تابود » بعنی بر آحیخت
1 بر آراست - و ماخت کرد .
آمودن بروزن آسودن . بمعنی
ارات .- 1 "آراسته خدن و آم‌ختن -
(4)چك : - اجمعین .
منانات دراطامعلار۳ < تیتی دما ؟ ‏ آعو جحون ؛ در
. لهج پارتی وپپلوی (2722(]) ۲12100 وهمچنین درلهجةٌ یکی خلج‌ونیز فرکمنی. رله : مقاله
6 .۱ .3 در پاپ کتاب ,601870۳8۲ مهم‌مودتده ,۱۷۵۵866 . ۲٩‏ . 8۲۱
40 .و4 ۲۵.3 ۰ ۷۵۲۰۱۵ و عع‌نت:5 عتاهني۸ ۵۶ اعصیداه
```


## [2026-09-04T19:16:43.399Z] TOOL CALL #23: Bash

```json
{
 "command": "python3 tools/ref_page.py --help 2>&1 | head -30"
}
```


### [2026-09-04T19:16:45.010Z] TOOL RESULT

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


## [2026-09-04T19:16:47.495Z] TOOL CALL #24: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:58 --image 2>&1 | tail -60"
}
```


### [2026-09-04T19:16:49.205Z] TOOL RESULT

```
no scan of BQT covers printed page 58 (see 'scans' in refs_online.json)
```


## [2026-09-04T19:16:55.040Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in BQT_v1.txt BQT_alt_v1.txt BQT_dli_part1.txt; do echo \"### $f  $(wc -c <$f) bytes, $(python3 -c \"print(open('$f',encoding='utf-8',errors='replace').read().count(chr(12))+1)\") leaves\"; done"
}
```


### [2026-09-04T19:16:56.884Z] TOOL RESULT

```
### BQT_v1.txt  2620060 bytes, 1 leaves
### BQT_alt_v1.txt  2634275 bytes, 1 leaves
### BQT_dli_part1.txt  139 bytes, 1 leaves
```


## [2026-09-04T19:16:59.194Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'اشك\\|اشک' BQT_v1_pages.txt | head -20"
}
```


### [2026-09-04T19:16:59.250Z] TOOL RESULT

```
357:ابر آن لپجه‌ای‌بوده زبا نزد اقوام پارت » خاندان پادشاهی اشکانیان یکی از آن
360:شده است . کلمه بپلوی بز بان دور اشکانیان و بزبان دور ساسانیان‌اطلاق
365:سر کار آمدن نعستین اشك » سرسلسلهٌ اشکانیان که ازیارت ( < خراسان )
395:از پپلوی دورة اشکانیان (۲۵۰ پیش ازمیلاد نا ۲۲4 پس‌اژ میلاد)
417:تفسیر پپلوی اوستا نا گزیر از روز گاراشکانیان آغاز شده . اماآنجه
443:ساسانی بسه زبان وبسه خط است : پیلوی اشکانی‌با پارتی و پپلوی ساسانی
668:۵ ) که مختص زبان‌شمال ایران-یعنی «اشکانی >- است‌ووجود
744:ملحق میشودواین‌دسته خطوطموجب پیدایشاشکال مختلف پپلویومخصوصا
858:سرد بعصر اشکانی و جود دارد بز بانی که هنوز نامی
956:اشکال اسمی نیز بهمین و جه ازمیان رفته‌اند: لپجٌفارسی بورینگون :
961:زين ز بان از نظر اشکال کلمات بسپولت تشخیص داده میشود (جمم اسماه :
962:آنها؛ضمایر : مننو.اوما» شما» ایشان»و آن»این؛ اشکال‌فعلی»زمان‌حال:
1068:اشکالاتی که بر روایات فوی وارداست:
1101:کوج‌ی هیندوك خوانند.» ۱ یعنی : نار گیل که باشکر خورند» بز بان هندی
1105:از آن ز بان بوده و بلاشك این‌مضاف ومضاف الیه پپلوی است وبارسی آن
1109:در مقابل پپلويك ( پپلوی اشکانی ) اطلاق میشده فردوسی در عنوان
1146:دارتگ » کتاب اشکال‌ما نی بود واندر لغت‌دری همین يك‌نا: دیده(م که
1297:1-)شکشمی بااشکاشمی 01:ظ180] «راشکاشم * (بامیر) که
1381:یافته که صر یحا باشکل کلمات یفنابی - که با آن درعلامت جمع شريك است
1386:0 ( که امرو زاز دن‌رفته) و رم تی بااشکاشمی و سنگلیچی بکدسته‌ر|
```


## [2026-09-04T19:17:06.205Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(311,317):\n    print('='*20,'leaf',i)\n    print(pages[i][:1500])\nEOF"
}
```


### [2026-09-04T19:17:08.283Z] TOOL RESULT

```
==================== leaf 311
آردسهشت
او س باکاف‌فارسی بروزن‌پهلوان,
بمعئی اردجان است و ها ور
سرار ۳ و 4
بر از جداول و اشکال و !
وباکاف تازی‌نام موضعی است
ونام دهی است از ی
ار دم بفتح اول و الك و سکون‌نانی
و میم , نام سوره‌های زر که است از کتاب زند
و یازند )۱( - و بممنی‌کار وهثر خوب هم آهده
ابت - و بممنی آذربون هم هست که نوعی از
افحوان باشد .
اد ذهی « بکس میم و سکون تحتانی»
نام جانورست نامعلوم ؛ و بجای حرف انی زای
نقطه دار هم بنظر آمده است .
ادذن « بنتح اول دثالث و سکون انی
و نون » تلم ولابتی است - و نام رودخاله‌ای هم
حست تزديك بدمشق 8 ؟. گوند رم عیسی‌علبه
السالام را قزر ان رود غانه عست بو کشک و
ثرشی پالا را نیز کفته اد » و باین معنی بضم
اول هم آعده است - و در عربی نام شهرست
بزرکه از نواحی شام . گویند قبر حضرت بمقوب
عو چاه یوسف درآ نجاست ؛ و آورده اند کهمشن
حضرت عقوب بر دوازده فرسنگی اردن بوده »
و در وید الفتلا نم همزه وذال نقطه دار آمده
(۱) چله : ژند باژند .
است وافة اعل . *
اد دون - بروزن پهلران , نلپلدشامی
بوده از نسل کشتاسب ۴ - و ناپولایتی هم‌هست
بسیار وسیم - و مضفف اکردوان هم باشد .
ازذو 4 » بر وزن مرغوله . نلم آشی
است مانشد کاچی و آنرا از آرد عیده پزند .
ار دی .- «نم اول , مخغف اردی بپشت
باشد . و آن نام ماه دوم است ازسال‌شمسی ۴
از ۵ یبهشت * « بن‌اول » بمعنیآتش
است که بعربی نار خوانند . و تام عاه حوم(»)
است از سال شمسی و بودن آفتاب در برح تور
و نام روز سیم از هر ماه شمسی باشد - و نام
فرشته‌ای هم هست که محافظت کوحها کند و
ندييي آمور و مصالح ماه اردی بهشت و روز
اردی‌بهشت تملق بدو دارد » و بتابر فاعدث کلی
که نزد فارسیان مقرر است که چون تام ماه با
نام روز موافق آ ید آنروز راعد کنند وجشن
مازند. دربن ماه ا
==================== leaf 312
بخشایش » بمعنی خیر و خیرات و چیزی در راه
خدا بمردم دادن باشد .
. اددانی معروف است که فقیض
گرانی باشد ۵ - ومردم دروش و فقیر ومستحق
را نیز گونند - و بمعنی ملم بتشدید لام هم
امده اسمت . 4
ار « با زای فارسی بر وزن مخزن»
نوعي از درخت بادام کوهی است: و ثمر آن‌سپار
تلخ می باشد و آن رادر دواها بکار برنه وچوب
آبرا عصاکنند و پوست‌انرا بر‌کمان بیچندا .
باشد ٩‏ ؛ چه ارد بععنی شبیه وحانشف ؟حدداست
و چون این ماه وسط فصل بهار است و نبانات‌در
غات نثو و نما و کلها و رداحن تمام شکنته
و هوا در نهات اعتدال » بنایراین اردی بهشت
خوانند  .‏
اد -بوزن طرز » بستی قیمت و بها
و ارزش باشد ۴ - و قدر و مربه را نیز گویند
- ویمعتی درخت صنویر هم هست - ودرخت انار
- و درخت سرورا نیز گفته‌اند - و در عربی برنج
طعام باشد؟ ۴«
اررانش ۴ - بکس نون بر وزن اددن ذدین - کنایه از جرعةُ
۱ - اشتباه است چنانکه گفته شد . ۴ - پهلوی 2۳21 مشثق ازاوستابی 3۳۵[2
« پارتولمه ۱٩۱‏ « تب رک ۲۲ » وتیز 272 درپهلوی آمده ۶ منای ۲۹۷ : ۲ 4 .
۴ - در عربی ارز در لائیتی ۲۷2۵( . ۴ رگ : فزهنگ دساتیر ص ۲۳۲ ۰
شاهد برای آن بافته تشد . ۵ - بهلوی 2۳2201 (دارای ارزتی) و 2۳28۳16 ( عفت )
« مثای ۲۹۷ : ۲ * . - ۵۵6۲ ۸۳۷۵۵ د یاتی ۰.۱۰ ۸62012
ا2ع5۵06 درختی از کل پروانه‌ها که از آن صمغ عربی گیرند ۶ فرهنگه روستابی ۲ _--
نیز نام دشتی درفاری که آنرا ارزن وارجن وارجنه هم کفته‌اند . این‌البلخی در فارسنامه (ص۱۵)
گوبد : مرغزار دشت ارزن » این مرغزارکه برکنار بحیره ارزن است وببشه است ومعدن شیر »
طول آن ده فرسنگه درعرض مك ۹
۵ اردیهشتگان - جشنی که ابرآنیان‌باستان در روز اردیبهشت (سوم) از ماه
اردیبپشت بریا میکردند . « بشت ۱ : ٩۲‏ « خرده اوسنا ۲۲۰4 « روزشماری
۵۸ * ارزان - دزم
==================== leaf 313
مه موم ما ی > ج با
کل فا
درل مخرفا
اردو
==================== leaf 314
آردو ت
برابر نا
سس ۳ص اس ای دیس ۳۳
سذ الفبای ار دو
۳ کیت لا
2 غ ۹ | کیت عرلا
ف ف‌ ِ؛
ت | نا 98
ات 42
ات 4و
ك 7 ار
۳ ‌ ۰ ۷ ی
ی ژا خر سر
و ۱ ول و ۷ ا(زم ؛ ساح خزطعرر
۸ ۳ اج باه | ارف افن‌را)
۱ ] ح شُرر
۵ ۵ 9
7 مر عب | #وع لا یکرجنت)
رل ۵ 92۳۱ از ء ک زک )
7 بر | -2۳۰۵/0]
8
۶ 7-72"
۳
==================== leaf 315
شراب است - و حبایی را نیز کوبند که بردوی
شراب بهم رسد - و کو کب و ستاره - و شرارةٌ
آش را نز کفته اند .
ارژ نگ ۱ »با زای فارسی بر وزن
و معتی ارشگه امت که نکار خانةٌ حانی نفاش
باشد . گریند اصل این لت باين همتی ارننگه
با ثای مثلثه موده » ثارا با زای فارسی بدل کرده
اند ارژنکه شده ؛ و بسضی گویند نام مانی‌ارژنگگ
بوده است و مانی دعابی است که اورا کرده اند
و لب اوشده است ؛ و جمعی گویند نام قاشی
است غس مانی و او نیز در حنروری مانند مائی
بوده است- و نام دبوی است که در مازسران با
رستم جنکه کرده و رستم اورا بکشت - و نام
پسر زره است و او مکی از بهلوانان توران بود
وطوی اورا بقتل آورد .
ارژفه - با زای فارسی » بر وزن
ومعنی ارجئه باشد که نام دشتی است هشهور در
ی
ارز ین س بانون بروزن سرزمین ۰ نانی
را کوید که از آرد ارزن یخته باشند .
اد ده - بروزن هرزه » کاهگل را گویند
چه ارزه گر کاهگل ساز وکسی باشد که کاهگل
را بجابی(۱) بمالد - و کچ را نیز کویند که
بدان خانه سفید کنند - و نام درختی هم هست»
بسضی کویشد درخت سرو است و بعنی د:
گونند درخت صنوبر است و زفت ازآن گیرند»
"۱ آخم۳: درجایی.
اری
و بمتی دیگر گونند پاين معنی عربی است »
و نی دیکر گفته‌اند (۲) درختیست که چلفوزه
میوه و بار آ درخت اس .
ارز ه گر بقاح اف فارسی بر وزن
درده دره اندایش کر و کچ مالئده را گویشد یعنی
(۳) ک یکه کاهگل و کچ درجابی مالد .
ار زیون « با تحتابی و فوقانی بروزن
عنب کون » نام دختر پادشاه مفرب است که در
حبالهٌ بپرام گور بود .
ازز ده » ۳ وژن فهسده سستی
فیمت کرده و قیمت شده باشد .
ارذ یز ه بر وزن غبخیز , قلمی باشد
و بمرپی رصاص خوانند . کویند اک قدری از
آلرا تنك کرده (44 بر کمر بندند منم احتلام
19-0
ار س - بفتح اول و ثانی و سکون‌سین
می 
==================== leaf 316
لرسانیفون
ارسانقون » با اك بالف کشیده
و نون تحتانی رسیده و فاف مضموم بواو و نون
زده » بلفت‌بونانی زرنبخ زردباشد وآن‌جوهرست
کومتشد یامر ند هر هتکتی که از ان شخورد
یمیید »
ارس بز آن - بکر الث و ضم بای
ابجد , چرك کنج چشم بز کوهی و کار کوهی
را گوند » و آن‌کار ترباك فاروق میکند وا ترا
صرمی تریاق‌الحه خوانند .
ادستن - بفتح‌اول وانی. مضنف آراستن
است - و بمعنی نوانستن هم بنظر آمده است .
ثالث و طای حطی ؛ نام حکیمی ات روعی
شا کرد افلاطون و وزیر اسکندر کبیر بود (۱)
ارسطا - با طای حطی بالف کشیده ,
بلفت روحی بمعی ارسط باشد ۱۹ معلم اول
9
ارسطاطا لس ه با طای بالف کشید,
و کس لام و سکون‌سین بی نقطه . بمعنی‌ارسطا
باشد که مملم ارل است ۴
تحانی و .من . همان ارسطاطالس رن که‌معلم
اول باشد ۴ - و نام شهری که ارسطاطالیی بنام
خود آ ماد کرده بوده است
اس
"بح
(۱) چش : بوده . _
رك: فاب ۰۱۷۷-۱۰۲ ؟ ‏ راد :
هواس
ار سطو » ِِِ و سکون واو »
ارسطاطالیی است
معلم اول‌باشد؟ - 1
زراوند گویتد چه ,
ارسطو لوجیا زراونسد
طوبل است و لوجبا
بمعنی طویل باشد ۵ . ۱
ادسی » بر وزن مسکن » بمه‌نی مجمع
ومجلس و انجمن و محفل باشد .
اد سنگه - بر وزن و هی ارانگ
نت که تکار خانةٌ مائی باشد .
ارش . بفتح اول و ثانی و سکون‌شین
نقط 4 دار » مقداری باشد همین ٩‏ ۰ و آن از سح
انگشت میانن دست‌راست است تاسرانگشت‌میاتن
دست چپ , چون دستها را از هم کشاده دارند ؛
و بضی گویند از سر انگشت میادن دست )٩(‏
باشد امرفق که بند گاه ساعد و بازوست و این
اسح است - و نام شهرست از ولادت شیروان -
و بفتح اول و کسر ثانی بمعنی عاقل و زبرك و :
هوشیار باشد - و بمعنی انجمن هم بنظر آعده
است مت و سکون تانی از حرادگنتان اعد عا
آرنج - و انجمن و مجمم و جمعیت مردم راهم
گفته اند
```


## [2026-09-04T19:17:16.488Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (315,316):\n    print('='*20,'leaf',i)\n    print(pages[i])\nEOF"
}
```


### [2026-09-04T19:17:18.389Z] TOOL RESULT

```
==================== leaf 315
شراب است - و حبایی را نیز کوبند که بردوی
شراب بهم رسد - و کو کب و ستاره - و شرارةٌ
آش را نز کفته اند .
ارژ نگ ۱ »با زای فارسی بر وزن
و معتی ارشگه امت که نکار خانةٌ حانی نفاش
باشد . گریند اصل این لت باين همتی ارننگه
با ثای مثلثه موده » ثارا با زای فارسی بدل کرده
اند ارژنکه شده ؛ و بسضی گویند نام مانی‌ارژنگگ
بوده است و مانی دعابی است که اورا کرده اند
و لب اوشده است ؛ و جمعی گویند نام قاشی
است غس مانی و او نیز در حنروری مانند مائی
بوده است- و نام دبوی است که در مازسران با
رستم جنکه کرده و رستم اورا بکشت - و نام
پسر زره است و او مکی از بهلوانان توران بود
وطوی اورا بقتل آورد .
ارژفه - با زای فارسی » بر وزن
ومعنی ارجئه باشد که نام دشتی است هشهور در
ی
ارز ین س بانون بروزن سرزمین ۰ نانی
را کوید که از آرد ارزن یخته باشند .
اد ده - بروزن هرزه » کاهگل را گویند
چه ارزه گر کاهگل ساز وکسی باشد که کاهگل
را بجابی(۱) بمالد - و کچ را نیز کویند که
بدان خانه سفید کنند - و نام درختی هم هست»
بسضی کویشد درخت سرو است و بعنی د:
گونند درخت صنوبر است و زفت ازآن گیرند»
"۱ آخم۳: درجایی.
اری
و بمتی دیگر گونند پاين معنی عربی است »
و نی دیکر گفته‌اند (۲) درختیست که چلفوزه
میوه و بار آ درخت اس .
ارز ه گر بقاح اف فارسی بر وزن
درده دره اندایش کر و کچ مالئده را گویشد یعنی
(۳) ک یکه کاهگل و کچ درجابی مالد .
ار زیون « با تحتابی و فوقانی بروزن
عنب کون » نام دختر پادشاه مفرب است که در
حبالهٌ بپرام گور بود .
ازز ده » ۳ وژن فهسده سستی
فیمت کرده و قیمت شده باشد .
ارذ یز ه بر وزن غبخیز , قلمی باشد
و بمرپی رصاص خوانند . کویند اک قدری از
آلرا تنك کرده (44 بر کمر بندند منم احتلام
19-0
ار س - بفتح اول و ثانی و سکون‌سین
می نقطه ۰ نام رود خانه است
مشهو رکه از کنار تفلیس وماین
آقربانتان و ازاش می‌کنوو ۴ ت
و بفتح اول وسکون ثانی» احك
و سکون انی تام سرو کوهی
است که بعربی ابهل و عرص
خوانند و نخم و ثمر آلرا جوز
الابپل و ثمرة العرعی کویند 6 .
(۳)اچش: و. رخ ۳: ساخته.
44۶
==================== leaf 316
لرسانیفون
ارسانقون » با اك بالف کشیده
و نون تحتانی رسیده و فاف مضموم بواو و نون
زده » بلفت‌بونانی زرنبخ زردباشد وآن‌جوهرست
کومتشد یامر ند هر هتکتی که از ان شخورد
یمیید »
ارس بز آن - بکر الث و ضم بای
ابجد , چرك کنج چشم بز کوهی و کار کوهی
را گوند » و آن‌کار ترباك فاروق میکند وا ترا
صرمی تریاق‌الحه خوانند .
ادستن - بفتح‌اول وانی. مضنف آراستن
است - و بمعنی نوانستن هم بنظر آمده است .
ثالث و طای حطی ؛ نام حکیمی ات روعی
شا کرد افلاطون و وزیر اسکندر کبیر بود (۱)
ارسطا - با طای حطی بالف کشیده ,
بلفت روحی بمعی ارسط باشد ۱۹ معلم اول
9
ارسطاطا لس ه با طای بالف کشید,
و کس لام و سکون‌سین بی نقطه . بمعنی‌ارسطا
باشد که مملم ارل است ۴
تحانی و .من . همان ارسطاطالس رن که‌معلم
اول باشد ۴ - و نام شهری که ارسطاطالیی بنام
خود آ ماد کرده بوده است
اس
"بح
(۱) چش : بوده . _
رك: فاب ۰۱۷۷-۱۰۲ ؟ ‏ راد :
هواس
ار سطو » ِِِ و سکون واو »
ارسطاطالیی است
معلم اول‌باشد؟ - 1
زراوند گویتد چه ,
ارسطو لوجیا زراونسد
طوبل است و لوجبا
بمعنی طویل باشد ۵ . ۱
ادسی » بر وزن مسکن » بمه‌نی مجمع
ومجلس و انجمن و محفل باشد .
اد سنگه - بر وزن و هی ارانگ
نت که تکار خانةٌ مائی باشد .
ارش . بفتح اول و ثانی و سکون‌شین
نقط 4 دار » مقداری باشد همین ٩‏ ۰ و آن از سح
انگشت میانن دست‌راست است تاسرانگشت‌میاتن
دست چپ , چون دستها را از هم کشاده دارند ؛
و بضی گویند از سر انگشت میادن دست )٩(‏
باشد امرفق که بند گاه ساعد و بازوست و این
اسح است - و نام شهرست از ولادت شیروان -
و بفتح اول و کسر ثانی بمعنی عاقل و زبرك و :
هوشیار باشد - و بمعنی انجمن هم بنظر آعده
است مت و سکون تانی از حرادگنتان اعد عا
آرنج - و انجمن و مجمم و جمعیت مردم راهم
گفته اند - و در عربی دیت و جريمهٌ جراحت
کردن باشد - و بدی افکندن میان مردم و بر
انگیختن جنگ و , بر افروختن آتش را نیز
گونند
۴ - چنین یت .
۴ _ ۸۲۱5016186 ( ۳۲۲-۳۸۵ ق.م).
( برهان قاطع ۱۸ )
```


## [2026-09-04T19:17:43.691Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i in (38,39):\n    print('='*20,'HRN leaf',i,'(printed p.%d)'%(i-21))\n    print(pages[i][:2500])\nEOF"
}
```


### [2026-09-04T19:17:45.409Z] TOOL RESULT

```
leaves 412
==================== HRN leaf 38 (printed p.17)
- 17 —
und Tomaschek (Pamirdialekte, 806) vergleichen
skr. ksäuma- 'gewobene Seide* {^uparaMäuma-),
ehe ohne s. he (No. 247).
66. e'iter 'Stern*.
phlv. a/tar; arm. LW. a/JarK 'Horoskop*.
Zusammenhang mit aw. apa^tara-, apa/^ra ist
unwahrscheinlich (Hübschmann, ZDMG. 38, 428,
Bartholomae, ZDMG. 42, 154).
67. erj.'Wert' (Sahn. I, 2 Vers 16), erjmend.
aw. arejah- 'Preis, Wert'; phlv. arj^ arjniand;
ai. vergl. arghd- 'Preis, Wert'.
oss. ary (31); arm. yargem 'ehren, schätzen' etc.
(Hübschmann No. 210).
gybis ^^^ 'Wert', erzan^ erzänis, erzTden,
Käs. ezü^ azün, ajiyd, ajiyd, mit Ausfall des r, wie
arm. LW. (?) azan (de Lagarde, No. 25).
aw. arejah-, arejaiti; phlv. arj, arjän, arjamk^
arJUan, päz. arzän etc., arm. LW. (?) armn 'gebührend*,
armnij armnavor; ai. drhati 'es ist wert*.
afy. yarz 'Fähigkeit, Wert*.
68. erz'Ti^ 'Blei'.
arm. arcic.
Geldner' s Gleichstellung mit aw. arezazi- (Yt. 13,
45, KZ. 25, 558) ist lautlich unmöglich; ebenso die
Ableitung von aw. erezata-, skr. rajatd-.
Die Heimat des Wortes ist noch durchaus unbekannt.
69. ers 'Thräne*.
mäz. asr; Käs. asl,
aw. asru- Thräne*; phlv. ars; ai. dgru-; lit. aszarä.
kurd. asr (Houtum-Schindler), {stir^ istir^ histir^
Jaba-Justi, sind wegen des t zweifelhaft); bei. als
(431).
Die indog. Urform war nach Bugge (BB. XIV, 72)
*ddJcru-, da auch gr. ödxpv, acymr. dacr, air. dSr, lat.
lacruma, got. tagr, ahd. zahar dazu gehören sollen.
Mindestens ist eine Dialektspaltung anzunehmen; viel-
U o r n , Qrundriss d. neup. Etymologie. 2
==================== HRN leaf 39 (printed p.18)
— 18 —
leicht liegen aber zwei ursprünglich ganz verschiedene
Worte vor.
Hierher gehört auch np. esk 'Thräne* (No. 88).
70. ers 'Elle', eres,
aw. arstya- {ßristya- K 5, Pt 4 in y. 9, 11) 'Elle' (?)^).
bei. haris, har§, harsa *Elle, Länge des Vorderarmes*
(153).
Vergl. türk. arys, oss. d. ItW.arcin (Hübschmann
S. 120).
71. er esk 'Neid, Eifer, resk.
aw. araska- 'Neid') ^) ; phlv. arsk^ rask, arSktn, arsklh,
bei. hirs (156) ist nach Dames und Hübschmann
(ZDM6. 44, 558) arabisches Lehnwort.
72. eryend, eryende 'zornig, gierig (Sahn., Mohl, V, 122),
aw. ereyunf' 'finster' (Bartholomae, Handbuch 220,
Geldner, Drei Yasht 27)^); phlv. argand [argimd ist
wohl nur verschrieben); ai. vergl. räjas-.
73. evff 'Castell, Citadelle'.
phlv. arkpatj nDp'?&* (Talmud) und weitere Formen
bei de Lagarde, Semitica I, 43; vergl. auch Nöldeke,
Tabari-Ubersetzung, 5, 111.
lat. arx, arceo, vergl. gr. doycew; arm. vergl. argel
'Hinderniss', argelum 'abwehren* (H. No. 38).
74. erm 'Arm' (nicht belegt, nur im BQ).
aw. aremö\suta' 'mit dem Arm geschleudert'; ai. irma-
'Arm, Vorderbug'; got. arms.
wa;^. yurm 'Vorderarm*; arm. armukn 'Ellbogen'
(H. No. 45).
eren *Elle' siehe ären (No. 14).
75. ez von, aus' etc., z% z-,
gel. ju köi {r= ez kujä),
ap. hacä; aw. haca; phlv. aj; ai. sdca,
kurd. az, ze, z-; af/. ;'-; bei. a(f, as (1); wa/.,
sar. z- etc.
1) Vgl. Bartholomae, BB. 10, 274.
*) Vergl. aber Bartholomae, Ar. Forsch. I, 119.
^) Bedeutungsübergang etwa: finster — höllisch ~ zornig.
```


## [2026-09-04T19:17:56.707Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- HRN 88 esk ---\" && grep -n '88\\. ' HRN.txt | head -5 && echo && grep -n -B3 -A14 \"^ *88\\.\" HRN.txt | head -40"
}
```


### [2026-09-04T19:17:56.764Z] TOOL RESULT

```
--- HRN 88 esk ---
1197:88. eSk *Thräne .
1818:088. hairdg (ZDMG. 41, 575 Anm. 6) und verweist auf Miller, Ose.
1997:188. hiziSk, bijisk (*bishk) 'Arzt* (Sahn. I, 32 Vers 180,
2062:188. {2)-bed, -bud 'Herr* (Comp.), z. B. sipehbed, möbed,
2826:288. pedrad 'Heil, Lebewohl*.

1194-ai. üstra-,
1195-kurd. LW. (?) hustur^ sutur; bei. hustar etc. (161);
1196-wa/. ü^tür^ siyn. stur, sar. xtiir, LW.(?).
1197:88. eSk *Thräne .
1198-g. sah,
1199-aw. *asraka (vergl. skr. dgra-), *arsaka (Hörn, Indog.
1200-Forsch., II, 136).
1201-afy. ö^a resp. ö/a; wsl/, ya^k, sar. yujck,
1202-Vergl. ers (No. 69).
1203-89. iiSnän Name einer zum Waschen gebrauchten Pflanze,
1204-Herba Alkali (AM. 28; 37 Zeile 2), sunan (DWlfi'IN,
1205-Jer. 2, 22).
1206-arm. LW. ausnan 'Seifenkraut*,
1207-aw. "^aiwis'hnana- (\)^) (de Lagarde, Fers. Stud., 74).
1208-Zu aiwis vergl. indessen unter bes-, bis- (No. 221).
1209-90. eSnOse, isnöse 'das Niesen', senöse, sinöse, sinöse-).
1210-germ. Vhnus bezw. /wws, vergl. ahd. niosan^ mhd.
1211-') Die Awestaform ist von de Lagarde falsch angesetzt, der
--
10185-37. iiiväklh 'Hilfe, Beistand' (AV.), vergl. awäklnitan
10186-'folgen'.
10187-Zu awak, np. ba (oben No. 145).
10188:88. äyafb /Belohnung, Gnadengabe',
10189-aw. ayaptü'.
10190-39. äyöjttan 'vereinigen, zusammenfügen .
10191-aw. *ä+ V^yaoj-, yaojante; ai. ä-\-\^yöJ- Caus.
10192-'befestigen, zusammenfügen*.
10193-40. af/öksuHt ^MetalY (Bund., Men.).
10194-aw. ayöxsustem 'Metall*; g. eyu/sust (H.-Sch.).
10195-41. ä%häy{i)Sn 'Anrufung, Gebet*, päz. azb° (Men.).
10196-Da im Awesta-Kommentar aw. {/^zba-^ zbay^mi durch
10197-jn^innp, jnjinDT'' oder stutan wiedergegeben wird, so
10198-soll Men. H, 64 wohl auch j-v^Jinsr stehen. Ein
10199-phlv. zbayttan giebt es jedenfalls nicht.
10200-4P'® azd 'Kunde' in azd rnat 'er ward gewiss, benachrichtigt,
10201-er erfuhr (Geiger, Yätk. Zar. Anm. 2).
10202-ap. azda- 'Kunde'; aw. azdä-; ai. addhd 'fürwahr,
--
10504-Fehle vT vielleicht noch existirt, wenn es auch sonst
10505-nicht weiter belegt zu sein scheint.
```


## [2026-09-04T19:17:58.111Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- HRN aluh ---\" && grep -n -i 'aluh\\|āluh\\|Adler' HRN.txt | head -20 && echo \"--- HUB ars/esk ---\" && grep -n -i \"ars 'Thr\\|esk\\|asru\" HUB.txt | head -20 && echo \"--- HUB aluh ---\" && grep -n -i 'aluh\\|Adler' HUB.txt | head -20"
}
```


### [2026-09-04T19:17:58.188Z] TOOL RESULT

```
--- HRN aluh ---
800:43. äluh 'Adler'.
803:Dazu gr. ögvig 'Vogel'; ksl. ortlü 'Adler; lit. erilis;
804:got. ara\ corn. bret. er, cymr. eryr 'Adler? Vergl.
1464:oss. d. analuHj aüyalim ^meinen, glauben', t. änqül-
6661:765. sl/inury 'Greif, Adler; N. pr.', vergl. STn\duxt,
6662:aw. saenö mereyö- *Adler' ; phlv. stnmuro, seiw murük
--- HUB ars/esk ---
411:88. Da zd. asru' = skr. rf^rw- im Np. als ars (aus "^asr)
417:gvagrii', iran. ^x^asru-. Vgl. afgh. dm *Thrane' = iran.
418:asru' neben afgh. x^'d^a *Schwiegermutter' = iran.
419:*x^asru-, Geiger, Etym. und Lautl. des Afghanischen
7362:= zd. yaozdad^ra- H. p. 301, asruk = zd. Hdravan- H.
7574:sr in rs: ars 'Thrane* == zd. asm-.
9544:d) Ap. sr = np. rs : ars 'Thrane' = zd. asm- (aber inlautend
9591:hazdr *tausend' — ap. "^hazahra-, skr, sahasru-; sCh',
--- HUB aluh ---
164:43. Zu dluh *Adler vgl. die kurd. Formen hdld etc.
165:ZDMG. 38, 95. Die Bildung von phi. np. aluh ist dunkel,
9439:= surax Xoch* H. 754, oben p. 77; aluh *Adler (oben p. 8);
```


## [2026-09-04T19:18:04.214Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 43 ===\" && sed -n '795,815p' HRN.txt && echo \"=== HUB 43 ===\" && sed -n '158,172p' HUB.txt && echo \"=== HUB 88 ===\" && sed -n '405,425p' HUB.txt"
}
```


### [2026-09-04T19:18:04.276Z] TOOL RESULT

```
=== HRN 43 ===
(fem.) 'Pfuhl, Lehmpfütze'.
Durchaus unsicher, da np. äläy-em dann die se-
kundäre Form und ü ursprünglich sein müsste. Auch
scheint die Grundbedeutung von älüden 'beschmieren*
zu sein, vergl. AM. 35, Zeile 6; 40, 16.
43. äluh 'Adler'.
phlv. äluh (Kärn. 59, Note 2), vergl. arvä (Bund.)
in Zendbuchstaben.
Dazu gr. ögvig 'Vogel'; ksl. ortlü 'Adler; lit. erilis;
got. ara\ corn. bret. er, cymr. eryr 'Adler? Vergl.
Hörn, KZ. 32, 583 No. 14.
FK will des falschen Reimes halber in dem letzten Verse statt ^em
vielmehr gom losen, während FJ danach mit Unrecht die Aussprache
bäf^dem für richtig erklärt.
»j KZ. 32, 579 No. 4 war mir leider Rüokert ZDMO. 8, 286
entgangen.- 11 -
44. äleyten 'springen, ausschlagen (vom Pferde)*, Praes.
alezed^)^ alezende^ alezTden^),
got. laikan springen, hüpfen*, laiks Tanz'; lit. laujytl
*wild umherlaufen (von jungen Pferden, Rindern auf der
Strasse)*; air. löeg 'Kalb*, (bei Feist).
=== HUB 43 ===
dann dlayam auf ein caus. *alavayami zuriickzufuhren.
Phi. lutaJc wird (Gl. and Ind. p. 139) durch nackt* iiber-
setzt, obwohl 'schmutzig' besser passt. Lautlich ist
also gegen eine Zusammenstellung von aludan mit lat.
lutum, lUeSj poUuo^ gr. Xv/ua, air. loth etc. nichts einzu-
wendon. Davon zu trennen^aZJd *unrein Fird. I, 15, 31.
43. Zu dluh *Adler vgl. die kurd. Formen hdld etc.
ZDMG. 38, 95. Die Bildung von phi. np. aluh ist dunkel,
die Zugehorigkeit zu ii^vtg u. s. w. daher nicht sicher.
48. Zur Erklarung von^phl. maiffHy amatan = np. dtnadan
(fiir *gatan u. s. w.) ist auf ap. ha(n)gmata (ptc. perf.)
hinzuweisen, nach dem mit Spiegel ein ap. Inf. ^gma-
tanaiy anzusetzen ist.
51. Wenn die Flexion dmextan mischen, pr. amBzam
(vgl. paz. amexta 'mixture' Shk. p. 248, phi. gumext,
=== HUB 88 ===
wahrt hat.
*) Vgl. auoh phi. stik ip sftk-pistan *with prominent breasts'
(Gl. and Ind. 160).— 15 -
ich glaube, dass st^n^ stenik zu lesen ist (die Pehlevi-
schrift unterscheidet e und i nicht), aber die Bildung
des Wortes bleibt mir trotz skr. sthEmdn- unklar.
88. Da zd. asru' = skr. rf^rw- im Np. als ars (aus "^asr)
vorliegt, ist es nicht wahrscheinlich, dass ein zd. *flf.9-
raka- (nicht *osraA;a-!), dem lautgesetzlich np. "^asra
entspr^che, durch np. ash vertreten wird. Nur konnte
Horn sagen, dass as-k neben ars steht wie x^as neben
xusru *Schwiegerniutter' (auch xasu^ xusu etc.) = skr.
gvagrii', iran. ^x^asru-. Vgl. afgh. dm *Thrane' = iran.
asru' neben afgh. x^'d^a *Schwiegermutter' = iran.
*x^asru-, Geiger, Etym. und Lautl. des Afghanischen
p. 51.
89. Arm. d$nan (nur Elise 156, 11) kann fur osnan ge-
schrieben sein ^) und so dem np. uifndn genau ent-
sprechen, mit dem es auf ap. ^usnctna- = zd. *usnana'
(vgl. zd. uS'Snd Vaschen* und wegen sn fiir sn : ap.
vasna = zd. vasna u. ahnl.) zuriickgehen k5nnte. Ap.
```


## [2026-09-04T19:18:20.734Z] TOOL CALL #33: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-04T19:18:20.742Z] TOOL RESULT

```


```


## [2026-09-04T19:18:24.729Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B4%DA%A9",
 "prompt": "Give the full Persian etymology section for اشک (ašk) \"tear\": Middle Persian and Old Iranian forms, Proto-Iranian/PIE reconstruction, and any cited authorities (Hasandust, Cheung, MacKenzie). Also any mention of ارس (ars)."
}
```


## [2026-09-04T19:18:27.432Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%E1%B8%B1%C3%A1%E1%B8%B1ru",
 "prompt": "Give the reconstruction, meaning, descendants (Germanic, Latin, Greek, Celtic), and the discussion of the relation to Indo-Iranian *aćru / Proto-Indo-European *h₂éḱru."
}
```


### [2026-09-04T19:18:29.461Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T19:18:31.593Z] TOOL RESULT

```
# Persian Etymology for اشک (ašk) "tear"

Based on the Wiktionary entry provided, here is the Persian etymology section:

**Etymology 1 Etymology section states:** "A suffixed form of Proto-Iranian *Hácru, from Proto-Indo-European *h₂éḱru ("tear")."

The entry indicates this word "may have been borrowed from Parthian ʾšk /ašk/ or some other Iranian language."

**Relationship to ارس (ars):** The entry describes اشک and ارس as "doublet" forms, noting that ارس "was inherited and lacks the suffix."

**Comparative forms cited:** The etymology mentions Khotanese āṣka- and Wakhi yašk as cognates.

**Etymology 2:** A separate entry notes اشک functions as "alternative form of ارشک (aršak, 'Arsaces')," described as "a corruption of earlier ارشک."

**Notable limitation:** The provided source does not include citations to Hasandust, Cheung, MacKenzie, or other specific scholarly authorities on Middle Persian or Old Iranian forms.
```


## [2026-09-04T19:18:38.393Z] TOOL CALL #36: WebSearch

```json
{
 "query": "wiktionary Reconstruction Proto-Indo-European dakru tear",
 "allowed_domains": [
  "en.wiktionary.org"
 ]
}
```


## [2026-09-04T19:18:39.801Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%84%D9%87",
 "prompt": "Persian آله — is there an entry meaning \"eagle\"? Give its etymology (Middle Persian āluh, Proto-Iranian, PIE) and any cognates."
}
```


### [2026-09-04T19:18:39.930Z] TOOL RESULT

```
Web search results for query: "wiktionary Reconstruction Proto-Indo-European dakru tear"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T19:18:46.472Z] TOOL RESULT

```
# Persian آله (Âloh) - Eagle Entry

Yes, the entry exists. Under **Etymology 1**, آله means "eagle" (marked as rare).

## Etymology Chain

The word traces back through multiple language stages:

- **Middle Persian**: "āluh" (eagle)
- **Proto-Iranian**: *Hr̥jifyáh
- **Proto-Indo-Iranian**: *Hr̥ȷ́ipyás
- **Proto-Indo-European**: *h₂rǵ-i-pt-ió-s, derived from *h₂erǵ- meaning "white, glittering"

## Cognates

Related words appear across several languages:
- Gilaki: aluğ
- Mazanderani: alle
- Northern Kurdish: eylo/êlo
- Central Kurdish: hello
- Bakhtiari: âlō
- Old Armenian: arcui
- Avestan: ərəzifiia

The entry notes this sense is "rare" in contemporary Persian, with more common synonyms being عقاب ('uqâb) and دال (dâl).
```


## [2026-09-04T19:18:54.629Z] TOOL CALL #38: Bash

```json
{
 "command": "python3 -c \"\nimport urllib.parse\nfor s in ['Reconstruction:Proto-Indo-European/dáḱru','Reconstruction:Proto-Indo-European/h₂éḱru','Reconstruction:Proto-Iranian/Hácru','ارس','Reconstruction:Proto-Indo-European/h₂ekʷeh₂']:\n    print(s, '->', 'https://en.wiktionary.org/wiki/'+urllib.parse.quote(s))\n\""
}
```


### [2026-09-04T19:18:56.527Z] TOOL RESULT

```
Reconstruction:Proto-Indo-European/dáḱru -> https://en.wiktionary.org/wiki/Reconstruction%3AProto-Indo-European/d%C3%A1%E1%B8%B1ru
Reconstruction:Proto-Indo-European/h₂éḱru -> https://en.wiktionary.org/wiki/Reconstruction%3AProto-Indo-European/h%E2%82%82%C3%A9%E1%B8%B1ru
Reconstruction:Proto-Iranian/Hácru -> https://en.wiktionary.org/wiki/Reconstruction%3AProto-Iranian/H%C3%A1cru
ارس -> https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%B3
Reconstruction:Proto-Indo-European/h₂ekʷeh₂ -> https://en.wiktionary.org/wiki/Reconstruction%3AProto-Indo-European/h%E2%82%82ek%CA%B7eh%E2%82%82
```


## [2026-09-04T19:19:00.038Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction%3AProto-Indo-European/d%C3%A1%E1%B8%B1ru",
 "prompt": "Give the reconstruction, gloss, notes on the relation to *h₂éḱru (Indo-Iranian/Baltic 'tear'), and the descendants (Proto-Germanic, Latin, Greek, Celtic, Armenian, Tocharian)."
}
```


## [2026-09-04T19:19:01.441Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction%3AProto-Indo-European/h%E2%82%82ek%CA%B7eh%E2%82%82",
 "prompt": "Give the reconstruction, gloss \"water\", the descendants (Latin aqua, Proto-Germanic *ahwō, Hittite), and any notes on *h₂ekʷ-."
}
```


### [2026-09-04T19:19:06.951Z] TOOL RESULT

```
# Proto-Indo-European *dáḱru (Tear)

## Reconstruction
**\*dáḱru** (neuter noun) = "tear (in the eyes)"

## Relation to *h₂éḱru
The etymology remains uncertain. One hypothesis suggests *dáḱru may derive from an earlier *dh₂éḱru, formed as a compound *dr̥ḱ-h₂éḱru meaning "eye-bitter." Another proposal from Dunkel proposes *h₂éḱru was prefixed with *d, the zero grade of *ád ("to; at").

## Key Descendants

**Proto-Germanic:** *tahrą and *trahnuz (yielding Proto-West Germanic *trahnu, "tear")

**Latin:** Reflected in Old Latin dacruma/dacrima, evolving into Classical Latin lacruma/lacrima

**Ancient Greek:** δάκρυ (dákru)

**Proto-Celtic:** *dakrū (plural or collective form)

**Old Armenian:** արտաւսր (artawsr, "tear")

**Note:** The page indicates Tocharian descendants are not detailed in this entry, though the term belongs to Proto-Indo-European's proterokinetic neuter u-stem noun class.
```


### [2026-09-04T19:19:08.343Z] TOOL RESULT

```
# Proto-Indo-European *h₂ékʷeh₂

**Reconstruction:** *h₂ékʷeh₂ (feminine noun)

**Gloss:** "(flowing) water"

**Key Descendants:**
- Latin: *aqua*
- Proto-Germanic: *ahwō
- Lusitanian: *aqua* ("river")
- Hittite: possibly *akukal(la)* (wash-basin), though the connection remains unclear

**Notes on *h₂ekʷ-:**

The root appears "suspiciously limited to a few western Indo-European branches" and lacks clear external parallels. Proposed etymologies connecting it to *h₂ep-* ("water") or *h₁egʷʰ-* ("drink") have been rejected on phonetic grounds.

Scholars consider the word likely of "onomatopoeic or substrate origin." An alternative theory suggests connection to *h₁eḱ-* ("swiftness"), where semantic development would proceed: "swift" → "river" → "water."

Reconstruction challenges include explaining the *-a* vowel in Italic and Lusitanian forms, and whether the underlying structure was *h₂ekʷ-* or *h₂ek-w-*.
```


## [2026-09-04T19:19:12.294Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/eagle",
 "prompt": "Full etymology of \"eagle\": Old French aigle, Latin aquila, aquilus, and whether it is connected to aqua \"water\"."
}
```


## [2026-09-04T19:19:13.471Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/island",
 "prompt": "Full etymology of \"island\": Old English igland/iegland, PIE root *akwa-, and the -s- from isle/Latin insula."
}
```


### [2026-09-04T19:19:18.382Z] TOOL RESULT

```
# Eagle Etymology

The word "eagle" has a rich linguistic history. It entered English in the mid-14th century from Old French *egle*, which came from Old Provençal *aigla* and ultimately Latin *aquila*, meaning "black eagle."

The Latin root's origin remains debated. Some scholars propose it derives from *aquilus*, meaning "the dark colored" bird. However, etymologist De Vaan suggests an alternative: "It is possible that 'eagle' was derived from *aquilus* 'dark' when this had received its colour meaning."

Interestingly, the color word *aquilus* itself may trace back to Latin *aqua* ("water"), though this connection is disputed.

Before the Romance language influence, English speakers used the native term *erne*, descended from Proto-Germanic *aron-* and the Proto-Indo-European root *or-* meaning "great bird."

The figurative phrase "eagle-eyed" (sharp-sighted) has been documented since around 1600, while the golf term for one-under-par emerged in 1908, so named because it "soars higher" than a birdie.
```


### [2026-09-04T19:19:22.255Z] TOOL RESULT

```
# Etymology of "Island"

The word "island" has a fascinating linguistic journey spanning multiple language families.

## Origin and Development

The modern spelling emerged in the 1590s, though earlier forms like "yland" appeared around 1300. It derives from Old English *igland* or *iegland*, combining *ieg* ("island") with *land*.

The root *ieg* traces back through Proto-Germanic *awjo* ("thing on the water") to the Proto-Indo-European root *akwa-, meaning "water."

## Spelling Evolution

The first syllable's spelling changed in the 16th century "by association with similar but unrelated isle." The second syllable was added to distinguish it from homonyms, particularly Old English *ea* ("water").

Similar formations appear across Germanic languages: Old Frisian *eiland*, Middle Dutch *eyland*, German *Eiland*, and Danish *öland*.

## Historical Usage

In place names, Old English *ieg* often referred to "slightly raised dry ground offering settlement sites in areas surrounded by marsh or subject to flooding," as seen in names like the Isle of Ely.

The term became an adjective in the 1620s, and by 1846, "island universe" was used to translate the German *Weltinsel* when describing solar systems.
```


## [2026-09-04T19:19:30.650Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 akru/dakru ===\" && grep -n -i 'akru\\|dakru' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10 && echo \"=== WLD Bd1 aq^ua ===\" && grep -n 'aqua' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10 && echo \"=== WLD band3 register ===\" && grep -n 'akru\\|dakru' WLD_band3.txt | head"
}
```


### [2026-09-04T19:19:30.735Z] TOOL RESULT

```
=== WLD Bd1 akru/dakru ===
2274:akru 
2331:akru „Trane“. 
2349:Besteht eine Beziehung zu *dakru1 Heringer in "Wiener Sitzber. 125, 
2350:II 35 f. nimmt ein Prafix d- an. Hirfc Abl. 1 37 vereinigt *dakru und 
2351:*o(d)kru unter *odakru. Ygl. Vf. LEWb. 2 406. 
13930:ueng- (s. d.) anzunehmen. Lit. rag tit , vdgti „stehlen" (.Akrumme Wege 
48461:dakru — de-, do- 
48475:dakru n. „Trane“. 
48487:Idg. * dakru ist wahrscheinlich aus *dmkru dissimiliert wegen ahd. tra- 
48503:Beiwort der Trane („bittere Tranen") teilweise an Stelle von dakru trat, 
=== WLD Bd1 aq^ua ===
2387:Lat. aqua „Wasser !t , got. aha , ; Flu6, Gewasser", aisl. q, ae. e«, afries. 
2406:ai. Mm „Wasser“, welches die schwachste Stufe zu lat. aqua darstellen 
3178:eine gall. Entsprechung von lat. aqua voraussetzen). Zur Erklarung der 
27785:ai. kahtsu-). wozu wohl ahd. htiliira „ulige, sordes limi vel aquae 1-- , mhd. 
35504:s. unten II, 141 unter *bhau-); weiter zu cjlieu- auck lat. fu-tis „vas aqua- 
43323:ligur. aquae Bormiae, apr. gorme). 
43344:Vf. IF. 39, 74 f.). [Kelto - ligur. aquae Bormiae und der in Thermenorten 
46620:moetinae, quo trahitur aqua . . . dictus a tollendo", Fest., toliitim „im 
=== WLD band3 register ===
1592:ol . i di knuee norw, 553. brangr 50M. dm fill 583. Frappr S06. inykill 692, krasen norw. disl, 697 buyir Sth, rawr G07, Ibnylla 583. beer ,,Eiakruste” norw. 506. Laysja norw. 583 bra fr 66. re ag 682. he acliw. 504: Lada norw. 672 brava echw. 5D6, keddi 600, 671 brefja G06. af GO. brevets 651. lof 501. treken norw. dinl, #24 bok din. 455. Fy Rai
1686:akrum din. See. shranila: narw. dial. Sree skryda nor. wala)
```


## [2026-09-04T19:19:32.922Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN tear ===\" && grep -n -i \"TEAR (of the eye)\\|4\\.25\\|Thräne\" SYN.txt | head -10 && echo \"=== IEC akru ===\" && grep -n -i 'akru\\|dakru\\|dakr' IEC.txt | head -10 && echo \"=== IEC akwa/aqua ===\" && grep -n -i \"ak\\W*ā\\W*\\|aqua\" IEC.txt | head -8"
}
```


### [2026-09-04T19:19:33.074Z] TOOL RESULT

```
=== SYN tear ===
5932:Ir. béoil, NIr. béal, see bel ‘lip’ (4.25).
5947:4.25 LIP
16522:6. OE onginnan ‘begin’ (14.25), some- times with infin. ‘attempt, try’ and gloss- ing Lat. cénarv.
21681:ChSI. zaklenati, aor. zaklepe (mostly Karakvelw, but zaklepe s¢ = exnreloOn LE 4.25, cf. Jagié, op. cit. 346), orig. for tht sound of closing (a door, etc.) : klepam
21967:Grk. xethos, NG xeldc ‘lip’ (4.25), also ‘edge’ as ‘rim, border’.
21980:NIr. béal, ‘lip, mouth’ (4.25), also ‘edge’.
23759:5. Lith. tusias, Lett. tukSs, disputed, but prob. : ChSl. tigi (renders xevés), Skt. tuccha-, tucchya ‘empty, vain’, Av. tus- in caus. taogsaya- ‘let loose, free’, etc. Miihl.-Endz. 4.256 ff. Trautmann 333. Walde-P. 1.714.
24294:yl 42 14.13 44 4.15 14.16 417 14.18 1419 421 14.22 14.23 14.24 14.25
24302:14.252 Last (vb.)
24454:(tk. épxatos, lit. ‘belonging to the be- ginning’, hence ‘ancient, old’, fr. apx7 ‘beginning’ (14.25).
=== IEC akru ===
367:aKərā, aKru ‘teardrop’. Cf. dakru. WP I, 769 Skt. ásru; Av. asru; Per. ašk; Tokh. A ākär, pl. akrunt; Li. ášara; Latv. asara
380:akris, os “point, tip, edge’; pointed, sharp’. WP I, 28. Cf. okris Skt. (ambig.) asrih (*ak- or *ok-); Hitt. cf. hekur (summit. Vocalism obscure); Gk. ákris; ákros; Lat. cf. acer, gs. ácris; Umb. akru-tu (abl.sg. ‘from the beginning"). Osc. akri-d ‘from the top’; Olr. achar, aicher *bit- ter”; aichre ‘fury’; achaire ‘sharpness’; W egr ‘sharp, sour; OE zhher, ear of corn’: OHG ahar, ahir, n. id. (MHG eher: G Aehre); Pol. (ambig.) ostrze 'knife-edge'. See aKtros
382:aKru ‘teardrop’. See aKora, daKru. WP I, 769
1294:bhi, -bhi (3) ‘by, at”, instr. and (sometimes) loc. indicator as an inflexn. Vedic bhi-, px. (in bhi-sákmi *heal); Hind. bhi ‘also’; Tokh. A.B. pi, -pi “and, indeed, so’; Arm. -b, -v (instr. inflexion); Hitt. -pi (in kwa-pi any. where’, sanna-pi ‘in one place); Gk. -phi, Myc. -pi (in óresphi, thürephi, biejphi, dakru- óphi, iphi, etc.); Go. bi; MHG bi; OE bi, be (and comm. Gmc.)
2046:dakruio, (daKrouo, əuið) ‘weep; drip’. See daKru above Arm. artasuem; Ok, dakrüo; W dagreuo; Cor. dagrewy, dagry; Br. daerawi, darawi; MHG zeheren; OE tearian, id.
2449:(draku “tëar”. See dakru)
18679:-to, -tos, ablative inflexion, variant of -t, q.v. Cf. tō (1) Arm. cf. hast-at (certainly, fr. hast ‘certain’. See paKtos); Hitt. cf. wedan-ta, -da ‘by water”; Osc. pure-to ‘by Drei E. Umb. akru-tu "at the top’; skalce-ta “from a dish"; Go. cf dala-pa ‘below’; (for the variant -tos cf.) Skt. mukha- tas “from the mouth’; Gk. ek-tós, en-tós, adv. “outside, inside’; Alb. jash-t8 ‘outside’; Lat. fundi-tus ‘from the bottom’; peni-tus, in-tus “within”
=== IEC akwa/aqua ===
268:aĝio-, -aĝio- ‘acting, course’. WP I, 35 Cf. Phryg. Sab-ázios ‘Bacchus; Gk. nau- agion, -egion; LLat. aquagium; ON ekja; R mjat-ëž; Cz. drůb-ež
406:aKua (?) “water; running water’ (aqua?). WP I, 34, 35 Skt. river-names in a$va-: -rathā, -parni: (?) Gk. asa-, -assa (in asáminthos, thál-assa. Speculations in Bois. DELG); Go. ahva ‘river’; OE ea; ON ọ (speculations with lit. in Feist: VWGS)
657:aquà, io ‘water’; (aquies, à ^watery) WP L 34 Gk. cf. thálassa (? *dh]- + *aquiə. Cf. dhol-); Lat. aqua; Go. ahva ‘river’; ON á ‘water’; OHG ouwa, auia ‘meadow’; OE éa "water, stream’; Fris. ie “water, ril
5490:guhermos (guhermn, guhermio) *warm, hot; heat. Variant: guhorm-. Cf. guheros, guhor-. WP I, 687. (Indo-Iranian forms fr. *guhorm-) Skt. gharmáh, m.; Av. garomo, adj.; garomus, m.; OPer. garma-; Per. garm, adj.; Oss. qarm, adj.; Tokh. A $árme, adj.; Arm. germ, o-st. adj.; Éermn gs german ‘fever’; Gk. thermós, adj.; thérme, f. s. beside thérma, n.; Alb. zjarr, zjerm, m. ‘fire’; cf. Dac. (?) Germi-sara (a wa- tering-place); OLat. cf. formus, adj. (Fest.); Formiae (a town nr. Naples); Lig. Bormium, Aquae Bormiae (places in Switzerland); Go. cf. warmjan, v. beside *warms (^warm', and com. Gmc.); Li. (Zemaité?) germe (“virgin
6623:kakā (kakk-) ‘excrement’. WP I, 336 Per. kak ‘biscuit’; Gk. káke “evi” beside kákkeé ‘excrement’; Alb. kaké, id.; Lat. cf. caco, are, v.; MIr. cacc, f.; Ir. cac, m.; W cach; Li. kaka
6624:kakāið (kakk-) “void excrement'. WP I, 336. Cf. kakā Gk. kakáo, kakkáo; Lat. caco, are; Mlr. cac- caim; Ir. cacaim; Cor. caca; Li. kakóju, óti, id. (an onomat. term, non-historical in Cz. kakat, G kacken, etc.). Br. kach, s., kacha, v. indicates a prototype *kakk-
6625:kākāið ‘cackle, guffaw, mock? Gk. këkázo ‘revile’; OHG huohon, MHG huo- hen, id. beside huoh, m. id. (Onomat. and am- big. in Gz. kákat ‘cackle’. Cf. quaquaió)
6640:kakos, ios ‘foul, filthy’. WP I, 336 and cf. kākstios, kakā Skt. cf. kacakuh ‘wicked, intolerable’ beside kaccarah ‘foul, bad?; Gk. kakós; Alb. i keq, f. e keqe ‘bad’; Lat. cacus ((camp-boy', Dei: Ligurian (in Rumansch) cac, f: caca ‘ugly’; Big. (?) koc ("latrine' fr. kakios?)
```


## [2026-09-04T19:19:42.935Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### WLD akru ###\" && sed -n '2325,2360p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt && echo \"### WLD aqua ###\" && sed -n '2380,2412p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-04T19:19:42.998Z] TOOL RESULT

```
### WLD akru ###
gr. kelt. ital. *okns und die Worter ffir Eijyc. Ursachcn und ursprfingliche 
Yerteilung der vorliegenden Wechselformen bleiben demnach noch zufinden; 
bei den Ackerbauausdrficken, wie lit. akuotas , ake'ios , wird es leichter, 
an Entlehnung aus dem Westidg. zu glauben (so z. B. Zupitza KZ. 37, 461), 
als bei Begriffen wie aJcsf'/s oder gar akmuo neben ainiuo. 

akru „Trane“. 

Yed. agru, spater auch arm n. „Trane“; av. ar.ru n. „Trane“; lit. usurn 
f. „Trane“. Ygl. ai. agiayumi lit. asaroju „weine". 

Wald e , Etymologisches Worterbuch. I. q 



34 


akka — aqHa- 


Bei einer Grundform *oJcru lieBe sich hom. oxQvoeig hierherffigen (Fick 
I 4 2, 162, de Saussure MSL. 7, 88). 

Besteht eine Beziehung zu *dakru1 Heringer in "Wiener Sitzber. 125, 
II 35 f. nimmt ein Prafix d- an. Hirfc Abl. 1 37 vereinigt *dakru und 
*o(d)kru unter *odakru. Ygl. Vf. LEWb. 2 406. 

akka „Mutter“ (Lallwort). 

Ai. akhu „Mutter“ (Gramm.), gr. Axxcb „Amme der Demeter 11 , axxib 
„eitles Weib oder Schreckgespenst“, axxl^ea&ai „sich dumm stellen, sich 
zieren“, lat. Acca Larentia „Larenmutter“ (z. B. Fick I 4 1). 

aq?- „dunkel, blind"? 

### WLD aqua ###
i(n)k- zurfickgehenden "Worter wieder die Abwesenheit des weshalb Yf. 
LEWb. 2 54 Mischung zweier verschiedener Wzln. *aq w - und *iek- erwagt; 
ist aklas nicht am ehesten als augenleidend“ mit ak'is, lat. oculus zu ver- 
binden, da Gebrechen haufig von dem betroffenen Korperteil benannt sind? 

aqja „Wasser, FluB“ (oder akual fiber lit. Asvd s. Trautmann Bsl. Wb. 72). 

Lat. aqua „Wasser !t , got. aha , ; Flu6, Gewasser", aisl. q, ae. e«, afries. 
a, e, as. ahd. aha f. ,.FluB“, nhd. Ache , russ. FI. -Name Oka (Yasmer brief!.). 
TJber die germ. FluBnamen auf - apa -, ahd. -irffi i, s. u. dp- „Wasser“. 

Hierzu germ. ahvJ, ahcjo f. „Wasser, -land, Aue, Insel“ : aisl. ey, gen. 
eyjar f. „Insel“, nnorw. auch in der Bedeutung „Aue“, ags. ley f. „Insel“, 
ahd. -ouwa, -aim, mhd. ouwc f. „Wasser, Strom, Halbinsel im Flusse, 
wasserreiches Wiesenland", nhd. Aur, mnd. d, aye, dch, omve, on „Insel, 
feuchte Wiese“, holl. landouw (Ealk-Torp 1, 1415). Ygl. Scadin-avia usw. 
(Mfillenhoff ZfdA. 20, 27). Anders fiber -avia, doch kaum zutreffend Prell- 
witz, Bursians Jb. 106, 108 und Wb. 2 unter oap 

Ablaut c : a wird durch aisl. cegcr „Meer, Gott des Meeres" erwiesen 
(Noreen Ltl. 59), hierzu nach J. Lowenthal Ark. f. nord. Phil. 35, 240 auch 
gr. (bxeavogl 



Johansson IP. 2, 20 vergleicht (mit Zustimmung von Foy KZ. 36, 123) 
ai. Mm „Wasser“, welches die schwachste Stufe zu lat. aqua darstellen 
wiirde, doch ist das Wort nach Uhlenbeck Ai. Wb. von Theologen erfunden. 
Ein ar. *asva wird aus ai. dgvavant- (RV. X 97, 7 „wasserig“?) und PluB- 
namen wie aqvaratha , ‘ Yddonyg erschlossen (Academy 1891, II 411; vgl. 
Zupitza Gutt. 60, Pay Am. Journ. Phil. 17, 5). 

ag- „treiben“ (urspriinglichst wohl „mit geschwungenen Armen treiben“),
```


## [2026-09-04T19:19:55.156Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW aquila ===\" && grep -n -i 'aquila' LEW_1910.txt | head -5 && echo \"=== LAT aquila ===\" && grep -n -i 'aquila' LAT.txt | head -5 && echo \"=== SKT eagle/island/tear ===\" && grep -n '^EAGLE\\|^ISLAND\\|^TEAR\\|^eagle\\|^island\\|^tear' SKT.txt | head -10"
}
```


### [2026-09-04T19:19:55.238Z] TOOL RESULT

```
=== LEW aquila ===
=== LAT aquila ===
4590:aqua a son correspondant exact en germanique: got .ahwa "Ttorap.OC",aquila
4608:aquila, -ae c.: i° aigle (oiseau, 4 toile,ou enseigne) cf.fulua...
4618:30,14 aquilo uentus a uehementissimo uolatu ad instar aquilae appel¬
4619:latur). On voit par Festus que les anciens rattachent aquilo k aquila
4633:anciens le rapprochent de aquila, et en font un deriv 4 de aqua (d’aprbs
=== SKT eagle/island/tear ===
```


## [2026-09-04T19:19:57.856Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4585,4650p' LAT.txt"
}
```


### [2026-09-04T19:19:57.910Z] TOOL RESULT

```
terme de droit, synonyme de aquae ductus; aqu(a)e mola (gloss.): u8po-
(auAti, piante.
Les 1. ronanes supposent aussi, M.L.$73 *aqudna, $79 *aquatdria;
cf. aussi 147 adaquari; 4336 inaquare; 3939 exaqudre; en germ. aquae¬
ductus (formes modernes), et aquarium v.h.a. ahhdri .
aqua a son correspondant exact en germanique: got .ahwa "Ttorap.OC",aquila
74
etc. et semble se retrouver en celtique, mais seulement dans des noms
de lien. Le germanique offre, d'autre part, un d 4 rive atteste par
v.h.a.ouwo (ali. mod. Au) "prairie marecageuse, ile",' et le nom propre
S candin-auia ; le derive v.isl .aegir "mer, dieu de la ner", avec un
ancien e initial, donne a penser que l'o de lat. aqua, got. ahwa repre-
senterait un i.-e. * 3 . Si ce mot ne se retrouve pas ailleurs, ce n’est
sans doute pas un hasard: tandis que le nom designant l ,H eau" en tant
que chose est commun a tout le monde indo-europeen (v. sous lat.undo),
les nons de genre essentiellement anime qui designent l'"eau" en tant
qu'etre actif - et divin -, n'ont qu'une faible extension dialectale.
II y a ce mot, commun au latin et au germanique; un autre mot, indo-
iran.souvent employe au pluriel (ved . apah , etc.) comme lat.
aquae, a des correspondants en baltique; cf. annis. - 11 n'est pas
accidentel que le nom germanique du "dieu de la mer" appartienne au
groupe de got.ahwa, lat. aqua designant originairement l'"eau" en tant
qu’etre actif.
aquila, -ae c.: i° aigle (oiseau, 4 toile,ou enseigne) cf.fulua...
auis d , Ovide, F.5,733; 3 ° aigle de mer ou mourine (sorte de raie).
Derives et composes : aquilinus ; aquilifer. Panroman. M.L.583; iri.
aicil. Cf. peut-etre aussi *aquileia : ancolie, M.L.583, et O.Blocb,
Dict.etym.
le nom de 1 '"aigle", le premier des oiseaux, et qui avait un ca-
ractbre religieux, varie d'une langue indo-europeenne a 1 'autre et
resuite partout d 1 arrangements relativement recents.
aquilo, -onis ( et aquilus, cf. Thes. II 376,9sqq. M.L.586 et 587^
m.: aquilon. Le nom complet est aquilo uentus (cf.Nep. Mi.1,5; P.F.
30,14 aquilo uentus a uehementissimo uolatu ad instar aquilae appel¬
latur). On voit par Festus que les anciens rattachent aquilo k aquila
et non k aquilus comme le font les modernes. Ce sont les anciens qui
ont probablement raison; aquilo n'est pas le vent sombre; il est qua-
lifi 4 de clarus par Vg., G.1,460, par opposition a nigerrimus auster
3,378; cf.Thes. II 376,48sqq. L'explicat ion rapportee par Isid., Nat.
rer.(Suet., p.339 Keiff.), aquilo, qui et boreas uocatur, ex alto flans
gelidus atque siccus et sine pluuia, qui non discutit nubes sed strin¬
git, parait avoir 4 t 4 inventee dans sa dernibrte partie pour rattacher
coute que coute aquild a aquilus.
De la: aquilonius; aquilonSlis (aquildnaris ap.Aug.) forme d'aprbs
septentrionalis ; aquilonianus (b.lat.); aquilonigena (Aus.).
Le rapprochement avec un mot baltique, lit. dklas "aveugle", etc.
n'explique gufere la forme et pas du tout le sens.
aquilus, -a, -um adj.: brun noir. Sare; arch. et postclass. Les
anciens le rapprochent de aquila, et en font un deriv 4 de aqua (d’aprbs
nubilus, nubes); ainsi Festus: aquilus color est fuscus et subniger,
a quo aquila dicta esse uidetur... aquilus autem color est ab aqua
nominatus, tam cum antiqui duos omnino naturales nossent, i.e. album
et nigrum, interuenerit autem is quoque, qui ita neutri similis est,
ut tamen ab utroque proprietatem trahat, potissimum ab aqua eum deno¬
minarunt, cuius incertus est color, P.F.30,7. Compose subaquilus (en
jeu de mots avec subuolturius, Pl., Ru. 433). L'explication par aqua
rend mal compte du sens de 1 'adjectif; on ne voit pas pourquoi l'eau
aurait 4 t 4 prise pour designer une couleur tirant sur le noir (Plaute
applique aquilus A une n 4 gresse). Peut-etre 1 rattacher a aquila,
1 'aigle 4 tant 1 'oiseau sombre, aueTOU...(leAavoS. II. $ 353. Les adjec-- 75 “ arbiter,
tifs designant la couleur sont sonvent empruntes a des noms d 1 animaux.
ara, -ae f.(ancienne forme dsa, cf.Macr., Sat.3,9,8, qui cite Varron,
et Serv.auct.Ae.4,919; osq. aasas "arae", ombr.asam-ar "ad aram") et
peut-etre hitt .hassas "foyer": antei (premier sens'sans donte), "foyer
de la divinite" par opposition a focus , cf. 1'expression pro aris et
focis. M.L.586a.
```


## [2026-09-04T19:20:10.183Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD vol2 eagle ===\" && grep -n 'aquila' FSD_vol2.txt | head -8 && echo \"=== WEB vol1 eagle ===\" && grep -n 'aquila' WEB_vol1.txt | head -8"
}
```


### [2026-09-04T19:20:10.261Z] TOOL RESULT

```
=== FSD vol2 eagle ===
=== WEB vol1 eagle ===
10095:lgi, n. [L. aguila, eagle.] in botany, 1s of perennial plants of the crowfoot Ranunculacez), found in the north te zone, and characterized by showy owers ot five-spurred petals: called also (or-lin), a.[L. aguilinus, from aquila,
60693:ēa’gle ray, Myliobatis aquila, a species of ray; any ray of the family Myliobatide.
111263:miai/gre, n. a European food fish, Sciæna aquila.
```


## [2026-09-04T19:20:13.439Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10088,10100p' WEB_vol1.txt && echo \"---- eagle headword ----\" && grep -n \"ea'gle\\|ēa’gle, n\\|eagle, n\" WEB_vol1.txt | head -8"
}
```


### [2026-09-04T19:20:13.525Z] TOOL RESULT

```
am in the form of water; like water;
uid.
fui-la, n. [L., eagle.]
1. in ornithology, a genus of raptorial birds containing the true eagles.
2. in astronomy, a northern constellation in ilky Way, containing about eighty stars ange from first to sixth magnitude and sedly outlining an eagle.
valved capsule. d, a. in heraldry, ornamented with
heads.
lgi, n. [L. aguila, eagle.] in botany, 1s of perennial plants of the crowfoot Ranunculacez), found in the north te zone, and characterized by showy owers ot five-spurred petals: called also (or-lin), a.[L. aguilinus, from aquila,
ike, or belonging to the eagle. an eagle's; said especially of a curved į L. aguilo, the north nh Win bs.]
[L. aqua, water, and parere, Si ogy, Seeing a watery P g to Aquitania,
i one of the divi-
ounaation
tween the Garonne River, the Pyrenees, and the ocean. Japa A-quiv’ér, a. agitated; tremulous; quivering. a-quiv’@r, adv. in an agitated manner; quiv- eringly. A qué, [L.] from which: opposed to ad quem. aq’u0d-cap:si li’tis, n. [L., agua, water, cap- sula, box, and -itis.] in medicine, watery in- flammation of the iris of the eye. Ai-quom/e-tér, n. [L. aqua, water, and metrum,
---- eagle headword ----
```


## [2026-09-04T19:20:20.417Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '60660,60700p' WEB_vol1.txt"
}
```


### [2026-09-04T19:20:20.471Z] TOOL RESULT

```
Chinese antelope, a swift animal, Procapra
gutturosa, inhabiting the dry, arid deserts of
central Asia, Tibet, China, and ‘southern
Siberia. dzig’/ge-tai, n. [Mongolian.] the wild ass of
central Asia, Equus hemionus.
ered individually; each one; as, each did his share; each of them heard the remark. i each other; each the other; as, they despis? each other, that is, each despises the other. J éach/where (-hwār), adv. everywhere. [Obs. €ad/ish, n. eddish. [Obs.] erat éa’g@r, a. [ME. eger, egre; OFr. egre, aigres = acer, acris, sharp, keen.] _ h; im- 1. keenly desiring; wanting very muc Jdiers patient or anxious; ardent; as, the sotdi were eager to engage the enemy. 2. sharp; sour; acid. [Obs.] tac] 3. sharp; keen; biting; severe, {Archaic.
4, brittle; inflexible; not ductile. (Obs. k
Syn.—earnest, fervent, zealous, enthu:
tic, vehement, intense, fervid. éa/gEr, n. same as eagre.
A
lomos; in, to culty. m tre- ective
uron, ig the
h dys- >] the capra Tts O ithern
ass of
eagerly
in an eager manner; zealously.
ger ly, pawns 1. the quality or state of bein, ager ne hi t- 1 ae g eager: Sac s
; ess; Sourness, s. ‘
2. PURO, zeal, ardor, impetuosity, en- F _ impatience. 3 thusioshai), MIME. egle; OFr. egle, aigle; Pr. éa/gle BE
la; L.a ui-
n inf onging o the falcon family, noted for their sharp vision and powerful wings. 2. a represen- tation of the ea-
gle, used as a
or em- , re
ation, etc.; especially, (a) the mili-
d of me Roas eae ©} ue atonal emblem of the United States; (c) the ioe insigne of a colonel in the United States armed forces (captain in the United
Navy). sae PA gold coin of the United States, of the value of ten dollars. y y
4. [E-] the northern constellation Aquila.
5, a lectern, the design of which is an eagle with outstretched wings supporting the desk on which the book rests.
6. in golf, a score of two strokes under par on a hole with a par of more than three.
éa'gle-eyed (-id), a. sharp-sighted as an eagle.
éa/gle gull, a gull with a black back, Larus marinus. 9
ēa’gle hawk, a South American hawk of the genus Morphnus.
éa/gle owl, the great horned owl of Europe, Bubo maximus, or the American Bubo virgin- ianus.
ēa’gle ray, Myliobatis aquila, a species of ray; any ray of the family Myliobatide.
éa/gless, n. a female eagle. [Rare.]
ēa'glestōne, n. a variety of clay ironstone occurring in hollow nodules about the size of a walnut: so called from the ancient notion that the eagle transported them to her nest
_ to facilitate the laying of her eggs.
éa/glet, n. a young eagle.
éa/gle vul’ tire, an eaglelike vulture of western
_ Africa, Ga polisaris angolensis.
éa’gle-wood, n. same as agallochum.
```


## [2026-09-04T19:20:27.891Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt; do echo \"--- $f\"; grep -c 'aquila\\|aquil' $f; done; echo \"=== search eagle entry ===\"; grep -n 'ea.gle' FSD_vol2.txt | head -5"
}
```


### [2026-09-04T19:20:29.507Z] TOOL RESULT

```
--- FSD_vol1.txt
5
--- FSD_vol2.txt
7
--- FSD_vol3.txt
0
--- FSD_vol4.txt
2
=== search eagle entry ===
4278:The  great  Floss,  nlonsr  which  they  wandered  ...  to  bbo  the  rush- ing .sDrinctide,  the  awful  Eagre,  como  up  iilio  a   hungry  monator, George  Eliot  Mill  on  the  Floss  bk.  i,  eh,  5,  p.  17.  (it.  1800.J I   <   AS.  eiigor-,  in  cSgor‘Stredm,  water-stream,  sea.l ea'gleh  1 1   i'gl;  2   e'gl,  n.  1.  A   very  large  diurnal  bird ea'gjv,  Jof  prey  or  f:ilei.)ntrid  bird,  espe- cially of  the  genus  Arptifa,  with  logs  feath- ered to  the  toes,  or  of  tlio  genus  IlaUatelus, with  the  lower  part  of  the  shank  bare  of  j feathers.  ^
4286:and  on  which  money  may  he  bet.  ea'gle-birii"!:.  9, .Arch.  The  pediment  of  a   Greek  temple.  [   <   F.  aigle,  <
4304:ea'glet,  1   i'glet;  2   e'glSt,  re.  A   young  eagle.  t<F.
42310:Hawke,  1   hek;  2 hidt.  Edward,  Lord  (l705-®9/i7l781).  An English  admiral,  who  defeated  the  French  oH  Bcllelsle,  1759. hawk'*ea"gle,  s.  See  under  hawk®,  n.
70755:la-get 'to,  Ha-get'o;  21a-get'o,fi.  [W.Ind.]  Thelacebark-  [Sp.) lag'gar,  1   Itig'ar;  2   Itig'ar,  n.  [India.]  Same  as  LUGGEBf,  n. lag'gard,  1   lag'erd;  21ag'ard.  I- a.  Falling  behind;  slow; lagging;  backward.  II.  fj.  One  who  lags;  a   loiterer,  lag'- gerj.  [<  LAG,  a.]  — lag'gard-Ism,  re.— lag'gard-ly,  acl». lag'gen,llag'en:21a,g'6n,re.  [North.  Eng.  &   Scot.)  l.Theangle formed  by  the  bottom  and  side  of  a   wooden  dish.  2.  The protruding  portion  of  the  staves  at  the  bottom  part  of  a cask  or  hooped  ve.ssel.  3.  The  bottom  hoop,  as  of  a   cask.
```


## [2026-09-04T19:20:33.800Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4278,4290p' FSD_vol2.txt | fold -w 200 | head -40 && python3 -c \"\nt=open('FSD_vol2.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('leaf of line 4278:', '\\n'.join(lines[:4278]).count(chr(12)))\nprint('total leaves', t.count(chr(12))+1)\n\""
}
```


### [2026-09-04T19:20:35.533Z] TOOL RESULT

```
The  great  Floss,  nlonsr  which  they  wandered  ...  to  bbo  the  rush- ing .sDrinctide,  the  awful  Eagre,  como  up  iilio  a   hungry  monator, George  Eliot  Mill  on  the  Floss  bk.  i,  eh
,  5,  p.  17.  (it.  1800.J I   <   AS.  eiigor-,  in  cSgor‘Stredm,  water-stream,  sea.l ea'gleh  1 1   i'gl;  2   e'gl,  n.  1.  A   very  large  diurnal  bird ea'gjv,  Jof  prey  or  f:ilei.)nt
rid  bird,  espe- cially of  the  genus  Arptifa,  with  logs  feath- ered to  the  toes,  or  of  tlio  genus  IlaUatelus, with  the  lower  part  of  the  shank  bare  of  j feathers.  ^
The  goMen  eagle  (Aguila  chrys~ aetus)  rftnges  'tliroughout  northern regions  and  la  of  a   prevailing  dark brown  with  a   cowl  of  lanceolate golden-brown  feathers.  The  bald or  .Amer
ican  eagle  (Halixam  i leucoeephalus)  Is  dark-brown,  with  [ the  hoad,  neck,  and  tail  white  In  If the  adult.  It  is  the  national  emblem  |8 of  the  United  States.  The  Euro-  r pea
n  sea-eagle  is  M.  alMclUa.  L A   gold  coin  of  the  United  |
States,  value  $10,  weight  25S grains:  so  o.aHed  from  the  im- age of  an  eagle  on  the  reverse.
'Fhe  doable-eagle,  half»e., and  quartcr-e.  arc  Kimilar® coins  worth  S20,  S,5,  und  S2.50 respectively.  3,  A   coin  of  base metal  In  circulation  at  the  ac- cession of  Edward  I.  (
1272) .   4.
[E-l  The  constellation  Aqulla.  5.  A   Ilom.an  military  stand- ard bearing  the  imago  of  an  eagle:  also  adopted,  as an  ensign  by  France  under  the  two  empires.
'fhe  .standard  bearer  ot  tho  tenth  lesaon, . . .   ealllnR  ol hia  companions  to  follow  him,  leapad  with  hia  eagle  into  i the  eea.  Li.voard  England  vol.  1,  d-  26.  {k.  C.  1827
,]
6.  /7er.  The  figure  of  the  eagle  either  displayed  ] or  with  w'ings  diaplaj'ed  (perched),  double- headed,  etc.  The eagle  with  the early  heralds held  the  same  po- sition  among bir
ds  as  the  lion among  animals.
7.  A   lectern  hav- ing its  desk  suu- ported  by  an eagle  with  out- stretched wing.s; anj’  article  in  the design  of  which an  eagle  is  prom- inent. 8.  In  the game  of  roulette, a   
spot  additional to  the  36  num- bered spots,  on.  1.  Roman  Eagle  from  Trajan's  column, which  is  the  pic-  2.  Roman  Soidier,  carrying  Standard ture  of  an  eagle  of  his  Legion.
and  on  which  money  may  he  bet.  ea'gle-birii"!:.  9, .Arch.  The  pediment  of  a   Greek  temple.  [   <   F.  aigle,  <
L.  aguila,  orig.  f.  of  aguilus.  dark  .colored.]  e'glet.—  black eagle,  an  eagle  notable  for  its  dark  pluma.ge,  .as  (1)  a   golden eagle,  (2)  in  the  United  States,  a   .young 
 bald  eagle,  or  (3)  the Malayan  eagle  (breoptis  malapcnsis). —   e-A'glc--eyed",  a. Keen-alghted  or  far-seeing,  like  an  eagle,  e, -sigh ted;.—  e.- flighted,  a.  [Poet.]  Flying  li
ke  an  eaglf;;  soaring  aloft.—  e.» gull,  n,  [Local,  U.  S.]  The  great  black-hacked  gull  (Lams marinus).—  e.ihavi)c,n.  1.  A   large .*^outh- American  hawk (germsMorphnns) ;   lis.t
hc  eve-nedeagle^hatck  (M.gutanensis).
2.  An  Australian  sea-e.agle  (X-'roaetus  audax).  -   e-.hawklng,  . ».  [Austral,]  The  act  of  stripping  thewooi  from  a   deadsheep: bushrnen'a  cant, —   E.  of  Brittany,  Eertnmd  Dug
uesclin, constable  of  Prance,  a   noted  warrior.— E.  of  Bivines, ThomasAqulnas.— B.  of  Meaiix,  Jacques  Benigne  Bo-asuet, bishop  of  Meiiux,  orator,  theologian,  and  historian.—  e
.- owl,  n.  One  of  various  large  owls:  ospecliaiy,  the  American great  horned  owl  (Bubo  virginlanus) ,   or  the  European  JS. wazfmas.— e.-ray-jW.  .A  large  myllobatoid  ray,  ospecla
ily
lagle  Key  1:  artistic,  art;  fat,  f:
esrtilOng  Key  S:  art,  ape,  fat,  fare,  fast.
leaf of line 4278: 48
total leaves 774
```


## [2026-09-04T19:20:53.417Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('WEB_vol1.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('leaf of eagle line 60670:', '\\n'.join(lines[:60670]).count(chr(12)))\nprint('leaf of aquila line 10095:', '\\n'.join(lines[:10095]).count(chr(12)))\nprint('total leaves', t.count(chr(12))+1)\n\"\necho \"=== MPP p.79 (leaf 65) ===\"; python3 -c \"\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/MPP.txt',encoding='utf-8',errors='replace').read()\npages=t.split(chr(12))\nprint('leaves',len(pages))\nprint(pages[65][:1800])\n\""
}
```


### [2026-09-04T19:20:55.447Z] TOOL RESULT

```
leaf of eagle line 60670: 601
leaf of aquila line 10095: 116
total leaves 1174
=== MPP p.79 (leaf 65) ===
leaves 140
MITTELIRANISCH
79
Hier ist, neben der im einheimischen Soghdischen sowie im Manichäisch-
Soghdischen aufgegebenen Unterscheidung von 8 und 0 , die Schaffung
zusätzlicher Zeichen (F. W. K. Müller, Sb. P. A. W., 1907, 2Öisq.) zu
beachten, die mit der seinerzeit von den Manichäern für das Westiranische
vorgenommenen Zeichenerfindung (§ 27) merkwürdig parallel geht: *
und / aus k bzw. p durch Veränderung am Buchstabenkopf, f entspre¬
chend manich. 7 (auch der Form nach ähnlich). Die so gewonnene sogh-
disch-syrische Schrift wurde dann weiterhin für das Uigurisch-Türkische
(F.W.K. Müller, Handschriftenreste, II, 107) und, allerdings modifiziert,
für das Neupersische gebraucht. Für das letztere stellt das von F. W. K.
Müller vorgelegte Psalmenbruchstück (Festschrift E. Sachau, 1915,
215-22) das wichtigste Zeugnis dar (vgl. H. H. Schaeder, Ungar. Jbb.,
XV, 570 A. 2; E. Benveniste, J.A., 1938, I, 458-62); dazu ein noch
unveröffentlichtes pharmakologisches Fragment über medizinische Öl-
Arten; Z kommt leider nicht vor, / und 6 werden beide mit Säde wieder¬
gegeben, für y 1 tritt, im Gegensatz zum Soghdischen, ein modifiziertes g
ein.
30. Die ältesten Dokumente des Jüdisch-Persischen
An wirklich mitteliranischem Sprachmaterial haben uns die Juden,
die in späteren Jahrhunderten so viele Sprachen mit ihrer hebräischen
Schrift aufzeichneten, nichts hinterlassen. Aus den bislang nicht veröffent¬
lichten Inschriften von Persepolis darf man schliessen, dass die persischen
Juden zur Sassanidenzeit noch ein Gemisch von Hebräisch und Aramäisch
schrieben; erst einige Zeit nach der arabischen Eroberung begannen sie
sich im Schriftverkehr der persischen Sprache zu bedienen; auf einige
epigraphische Zeugnisse ist schon oben beiläufig hingewiesen (Quilon-
Tafel, § 17; Kabuler Inschrift von 119
```


## [2026-09-04T19:21:08.374Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB ars ===\" && grep -n -E \"^ars |[^a-zA-Z]ars,|'ls'|ars\\b\" NYB_vol2_glossary.txt | head -10 && echo \"=== NYB aluh ===\" && grep -n -i 'aluh\\|eagle' NYB_vol2_glossary.txt | head -10 && echo \"=== ARY ashk ===\" && grep -n 'اشک' incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-04T19:21:08.456Z] TOOL RESULT

```
=== NYB ars ===
18:The second volume of my Manual of Pahlavi appears at quite a long interval: ten years after the first. The main reason has been the extraordinary amount of fundamental linguistic problems presenting themselves within almost every word, each requiring lengthy and painstaking research. My advanced age has also somewhat impaired my efficiency. -
19:The delay, however, has not been without its advantages, I think. During these ten years I have had time to scrutinize the texts to the last letter and to deepen my understanding of them. I have been able to correct mistakes and premature emendations. The long list of corrigenda is an evidence of this.
29:As I have pointed out in the Preface to Volume I, I have written this Manual in English for the benefit of the Parsees in India who as a rule do not understand other European languages. This has not been pure joy for me, since I am not ‘to English born’ and have used German and French as a scholarly medium through- out my life. No doubt this work would have appeared much earlier, had I been able to write it in a language that I master. My outstanding disciple, Mrs. Judy Josephson, born American, has done her best to correct my worst Swedicisms with unfailing energy and a fine sense of nuances. If, much to my regret, my text will jar on some sensitive English ears it is certainly not her fault.
402:ämöxtan [’mwhtn'] āmēc- to teach 6523-25, — Ps. imp. ?mwcy; Paz. āmēxtan āmēž-; NP ämöztan ämöz-. MPrth ?nwatn "mwe- (A-H III, BBB); MPrs hmwatn hmwc-. Verbum 170; Ghilain 63. The etymology commonly given of this vb.: ham-vac- (v. wax$ and vācišnēh, patvdxtan) is by no means formally or semantically as evident as alleged. Formally the analysis ham + mauk- > 1) hammök or > 2) hamok > (h)amok would seem more satis- factory, and semantically the difficulties are not insurmountable: *mauk-, Skr muncati ‘to let loose’, ham-mauk- ‘to give out (knowledge) from oneself’ (Skr sam- muc- ‘to shed tears’). Already in 1936 Bailey derived Sogd. mwck ‘teacher’ from *hamauk, v. Gershevitch, GrMSogd § 397.
420:an-aibigatīk ['nybgtyk] adj. belonging to the period of non-atbigat (q. v.), i.e. the period when the Evil Power had not yet invaded the creation of Ohurmazd: ~ sar the end of this period (v. sar) 38%; ~ 330 sal 330 years before the Onslaught took place 3926, — Cf azbigat, aibigatik.
439:and [’nd] so much, so many: én ~ this much 64°; all this, all these 351. 623. 6572.24; hac én ~ sal apāc since so many years 1674; han ~ dušman all these ene- mies (sg. as with numerals) 249; 10426, 11923; — ~ cand as much (big, large, high, etc.) as: 3119-15, 935. (935 without ~); ~ cand yašt-ē (as much as =) at least some ceremonies 659; — hän <... cand as much (many, long, ete.) as 92°. 997. 10027, 10324-25; 2 ~ dranäi pahnāi cand han i nn hast twice the length (and) breadth of it as it is now 10024-25; 7000 han ~ cand
476:apäc [L'WEIL ; ’p’c] 1. adv. back, back- ward (opp. frāc 25?-*), again: hac 7-salak ~ for seven years 16?5; hac én and (q.v.) sal ~ 1674; — prev. with vbs. of motion, e. g. dmatan, šutan, vastan, ete., and many others, e.g. guftan, gumeatan, etc. — 2. prep. with (= apäk) 42%. — 1. < *apācā instr. adv. from Olr adj. *apdnk-, weak st. apük- and apác, derived from Av. (72) apa, OP apa, cf Skr apdfic- ‘situated be- hind’; MPrth °b’c; Paz. awāž; NP baz. — 2. < *upācā, instr. adv. from Olr adj. *wpünk- derived from Av. (388 sq.) upa, OP upä ‘under, with’; J-Prs ?b?z ‘with’ (common); v. further apäk.
546:Cf NP afsün, ausün ‘charm’, afsä ‘a wizard’, afsäyidan ‘to subdue, esp. by magic’, undoubtedly to be connected with NP sidan säy-, farsūdan farsäy (< *fra-) ‘to rub’, the magic treatment con- sisting of some special rubbing or strok- ing of the sword (< *upa-sü-, v. apa-). However, the corresponding OInd. vb. šā- means ‘to sharpen, to whet’ ($ita- ‘sharp’) a sense also attested in Ir: NP afsän, ausän ‘whetstone’; MPrs hswd = hassüd < *ham-süt "whetted' of a sword (Hen- ning, BSOAS XII, 1947, 45), directly to be compared with OInd (RV) sam-sä- ‘to whet’; thus apa-sütak could simply mean ‘sharpened, whetted’. The parallel epi- thet distak (g. v.) is not quite clear.
554:apäyistan ['p'dstn'], apāyītan [’p’dytn'] apäy-, 3d p. sg. apāyēt [’p’dt', ^p'dyt'], 3d p. pl. apäyend ['p'dynd], pret. 3d p. sg. apāyist 1. to please a p. (pat) 83%; cigon mēnēyān apäyist as it had pleased (was predestinated by) the heavenly gods 405, v. below. — 2. impers. it is desirable: -m apāyēt 6 han ciš I desire, try to obtain, this 562%, — 3. to be needed 1211-2 also pat. kär. apāyet 14%. 375, andar apāyēnd 105%. — 4. to be proper, seemly 4015 (bē ~). — 5. impers. apäyet auxiliary vb.: must, ought to, shall, should, has to, is bound to, ete. with the p. as indir. obj. (virtual dat.), a) governing an inf., which is as a rule placed after: u api-t xvatāyēh i Ērān šahr vas sal apäyet kartan and thou shalt exercise dominion over Iran for many years 629-31; 918-19, ]014 ete.; in this case preverbs to the inf. are drawn to apäyet; bé — pursitan 1319; ba ~ hištan 1313; kār-ē i apar nē ~ kartan 104%; apārīk 6 [KN] ~ xtartan 94??; less often the inf. is placed before: ēzatan nē ~ 1017-19; pit u mat frazand i xueš rād En and kär u kirpak ... bē üámóxtan ~ the parents shall teach 6522-23; 6519-20; 9113; the inf. sometimes has to be supplied: -
645:ars ['ls] tear 9317. — MPrs "rs (Sogd. 2731); NP ars.
=== NYB aluh ===
372:aluh ['lwh] eagle; with indef. art. ~-é [+1] 9%. — MPrs "wf (List 79); NP äluh, < OP "ardufya- < *ardifya-, Av. (354) arazifya-.
3423:sén [syn'] a mythical bird of prey, prob- ably the eagle; séné [syn'y, cas. obl.] murvak, dimin. of sén(é)-murv = NP Simury, 2624: aläi! sēnē-murvak bärak-it woe! thy (dear) Simurg of a courser! — Av. (1548) lsačna-; maray6 sačno Yt. 141; a miraculous eagle nesting in a tree called vispo.biš ‘yielding all sorts of medicines’ Yt. 1217”. NP Simury NW form, s. murv.
3700:tài [D] a) until, b) as long as, as far as: A. prep., local and temporal: ~ [YM? =] rot danbY as far as to the bank of the River P 1:3; — nazd bam until daybreak 53; ~ nun until now 79; ~ sar carm bē haxt stripped his skin up to his head 321-1?; — ka? up to whom (does) Right- eousness (reach)? (— who is the origi- nator of Righteousness ?) 57! ; also govern- ing an inf.: 47M. 779; ~ 3 róc within three days 710; ~ zivandak drahnāt dur- ing the whole lifetime 6514; hac ... ~ from... to: hac pus ~ brat from son to brother, both sons and brothers 221; all men hac 10 säl — 80 sälak from ten to eighty years 20*; passim; — also ~ 6: ~ 6 drayäp 671; ~ 6 3 bar until three times 539-10. =. bē 6 asmün 9218; etc.; — han-tàa, v. this w.; — except(ed): sak ... u dalman ~ apārīk o apāyet xtartan dogs ... and eagles excepted, all the other (animals) may be eaten 9421-22; in frame preposi- tions: bé man ~ an kas nē except myself no one else 157; bē Zartuxšt ~ Z. ex- cepted 9313-14; apar 3 Sap ~ three nights ago 512-3, — B. conj. 1. final: in order that, with pres. ind. passim; with subju.: ~ rasāt 4125-26; m ... bavät 45"; governed by a vb.: framäyet ~ pätifräs . . . kunend
=== ARY ashk ===
1154:در دوران اشکانیان و ساسانیان زبان‌های ایرانی کهن به تدریج تبدبل به زبان‌های ایرانی میانه
2552:ا ۲ ۲ اشکه ارس» سرشک
7509:لینرانی (4(0لفلا بل 7/): آنا1۸ پسگشت‌ها اشکیت را
9655:۱ ۳۳ ساشکریت (7تعهبرهم: 11۸8 دانمارکی (0۸(/870): 0
15170:171 11۸۷۸5 5نآن ساشکریت (7ل8۸(/867): ۰"
```


## [2026-09-04T19:21:24.204Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find pdf page tag before line 2552\nimport re\ntag=None\nfor i,l in enumerate(lines[:2560]):\n    m=re.search(r'\\[pdf page (\\d+)\\]', l)\n    if m: tag=(i,m.group(1))\nprint('nearest tag', tag)\nprint('\\n'.join(lines[2535:2575]))\nEOF"
}
```


### [2026-09-04T19:21:25.740Z] TOOL RESULT

```
nearest tag (2548, '89')
برنانی 0728/0): ۸ ,857۸10808 هلندی (07611). 3 ان
لاتین (4770ما): (13(97۸۷8)8۸8)
گوتبک (0077/0): 18-87[1۷381 ,قلل8771 پسگشت‌ها 55 ق۲۵۲2
ایسلند یکهن (0124/49۷/من5 صا0): 09 70000
1 مبفا#لا57 4 (8725) ی
نورس کهن (۸0758 ص01): وان 6 (878353) :005
آلمانی کهن (0870/۸00 04 صاه): 9 ‎٩71178110‏ ,ل878) 7
577837 بف#ن577 برهان قاطع : ۱۳۷
1 7 بیادداشت:.
۱ واژه‌ی "ستور" هم ازالهمین ريشه است,
۲ معنی این واژه در ارمنی: شخیم.
معنی این واژه در یونانی: سترن» تیرء
معلی این واژه در اکثر زبان‌های ژرمتی: سکان» راهبری کردن؛ راندن.
[pdf page 89]
ا

ا ۲ ۲ اشکه ارس» سرشک

ا اوستایی (4۲587۸4): -ل31٩۸8‏ ,۸8۸۷ انگلیسی کهن (80/05[0 0ا0): ۰۰۰ 784۵8
پهلری (الامتللرم: ۸28 هویم "۰"
کردی (54(ط6): اند ان انگلیسی (لاولاه/(8): 7۸
اففانی (پشتو )(/(4۳01۸). 0 دانمارکی (0۸184): 1
سانسکریت (54(/8877): ,۸81581 ,نکم سرئدی (8801/57): 3

هافتاک۸ ,زا۸058 نروژی (۸/0775014(۷): 710

آرمنی (۸/5/14/7): زد ای اب هلندی (007674): آنففع7
۸۸8 لیتوانی (۵0هلانل 7 ): 3غ۸اقم

یونانی (67858): ,0۸36800 (لا 026 لنرنی (لتی) (71۸4ما): ۸۸۸

۱ اد ایرلدی کهن (#لفللا صام: 258
لاین (/4770): خاانا#کشا ,1۸۲3736۸ ولزی (کل/): 28368
فرانسه (۳۸۵۸/6/1): آر ۱۹ برترنی (872707): اراد زا رد۱۳۹
اسپانیایی (ل5۳۸(/5): ۸ ۱
ایتالیایی ((۸): ۲۸۳8۸ پسگشت‌ها زرد هرادن ردنا
رومانی (۸/۸(/(۷): 13 9 200520
پرتغالي (۳0770001285): ۱ 9 (۲8۸3) اک ین ان
گرتبکه (0077710): 3 ی 7 (5/گه]) :هام05
ایسلند یکهن (010۸۷۵۷ی5 ۵): 11 ماد مت ها
```


## [2026-09-04T19:21:35.827Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'عقاب\\|آله ' incoming/ARY/ARY_pages.txt | head -10; echo \"--- latin index eagle/aquila ---\"; grep -n -i 'AQUILA\\|ASRU\\|ASRAKA' incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-04T19:21:35.893Z] TOOL RESULT

```
662:8 ساکن بودند ولی امر وز اعقاب آنها فقط در بخشی از تاجیکستان باقیمانده‌اند. در
664:مذهبی آن دیار از قرن هفتم تا دهم به زبان آنها نگاشته شده است و اعقاب آنها امروژه در پامیر ۱
668:شمال دریای سیاه برافتاده‌اند. نقط در شمال کوه‌های قفقاز اوست‌ها (0888788) که اعقاب الان‌ها . ,
1900:۸ آله آلوه الوه(به چم*عقاب*)
15590:چم این واژه در زبان یونانی؛ عقاب,
--- latin index eagle/aquila ---
1870:ERDLIS. AQUILA LATIN) eZ
1886:eign Cle GAQUILA 3 544, 0 bib SKEAT 3 ONIONS -t
2507:Sp TEAR, ©. (OLD ENGLISH) 4S 5! ASRAY, ASRU- ——-(AVESTAN) ply!
2511:TAR (SWEDISH) (528 y« ASRU, ASHRU, :(SANSKRIT) cy Ste
6937:SWEHUR, SWIGAR SVASRU, CHVAKURA, CHVAKRU
```


## [2026-09-04T19:21:38.185Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON part1/2 آله ===\" && grep -n 'آله ' MON_part1.txt MON_part2.txt 2>/dev/null | head -5; echo \"=== MON adkolon ===\"; grep -n 'ادکلن\\|آکواریوم' MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10"
}
```


### [2026-09-04T19:21:38.280Z] TOOL RESULT

```
=== MON part1/2 آله ===
MON_part2.txt:41218:له: «۱ [- آله - آلوه ‏ اله| (.) (جان.) 
MON_part1.txt:4506:آله کلو: 1011-(6-)212 [- آلا کلنک ] (امر.) 
MON_part1.txt:65124:شدبدی دارد؛ آله کلو. . ضح. مفرد آن کمتر 
MON_part1.txt:93057:طلیع : آله (ع.] (ص.) (فت.) آنکه از طرف 
=== MON adkolon ===
```


## [2026-09-04T19:21:43.687Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ntag=None\nfor i,l in enumerate(lines[:1901]):\n    m=re.search(r'\\[pdf page (\\d+)\\]', l)\n    if m: tag=(i,m.group(1))\nprint('nearest tag',tag)\nprint('\\n'.join(lines[1890:1935]))\nEOF"
}
```


### [2026-09-04T19:21:45.605Z] TOOL RESULT

```
nearest tag (1898, '67')
کردی (08.01577): ۸0۸77 زج ی
سانسکریت. (8۸4(/5577): ادا 0 3 (۸۸۴) یدام ده ها
یونانی (0865): 7805۸3 10 دزی اه را
۹ ۰ اسلاوي کهن (ع ما5 الع#ناتته صل۵):
ان
یادداشت:
این واژه با واژه‌های آنگاه" و "چشم " همریشه است. بازگشت به؛ نگاه. :
| ملاس سروازه نارس 6۵
[pdf page 67]
۸ آله آلوه الوه(به چم*عقاب*)
اوستایی (//4887): 33۹1321-771۸ ,۸18۷۸ انگلیسی(شاید) (8لا8۸/0): زد 2 نا
پارسی باستان (۳88۶1(۷ 02): ۸8177131۸ اسلاوی کهن(شاید) (10ملا تق#ناتل صان):
پهلوی (۲ماتقهه): 3 ار قته9
کردی (۳082/50): 8910 ,اقلا رلانل11۸ روسی(شاید) (0891400): مهار
سانسکریت (54/5777): رد لینرانی(شاید) (۷لفا#(هتاتنترم. ,قااگ8۸
ارمنی (/۸۸/8۸1۸): ۸17 : کمقم ,قناگعم
یونانی 088810): 05 لتونی (لتی)(شاید) (/77142): ,8038
لانین (۸710ل): هانا٩۸‏ 2038
فرانسه (۸/)[7ظ۳۸): خاعا۸ پروسی کهن(شاید) (/(۲8914 صا0).
اسپانیایی (82۸(/18[4): ه۸ا]ا۸0 دا دی
ایتالیایی (/4۸ل7ل): هاآلا۸6 هتبت(شاید) (177175م): ,گش#هتر
رومانی (0۸/۸71400): دی نان ۱
پرتغالی (۳077007285): ۸۲۸
گوتیکك(شاید) (0077710): ها۸ پسگشت‌ها ادا دی دای ]
ایسلند یکهن (۷14۸۷ 21ات5 00):(شاید) وک ۶۸0205200
ب1۸83 2 (شآگ۸ق,7 (اتابتغ) نقلدانتن مر
آلمانی کهن (شاید) (05704۸/۷ لا صاه): 7 (615ه5) :05
۸0 0 (38ا6هه) +57
آلمانی(شاید) (028//۸): جلف ,۸202.88 برهان قاطع ۵۸
انگلیسی میانه(شاید) (2۸۷01187 4005+ فرهنگ معین + ۳۳۳۱
86
بادداشت:
۱ این واژه با واژه‌ی "راست" همریشه است.
1 ۲- 081008 و 858۸7 فقط تا ریشه‌ی لاتین ۸0111۸ به عقب می‌روند.
۳ 8۸13۲1۸۹7 معتقد است که شاید این واژه با واژه‌ی لاتین ۸011۸(آب) همریشه باشد. ۱
۴ ۳0۴018۷9 فقط واژه‌های ایرانی و ارمنی و یونانی این فهرست را از واجریشه‌ی -3۷80* می‌داند و بقیه را از
واجریشه‌ی -12* می‌داند.
د- 05۸31۸35 بیشتر واژه‌های این فهرست را از واجریشه‌ی -/08* پا -01308* مي‌داند.
پندار نویسنده‌ی کتاب حاضر این است که این واژه‌ها به احتمال زیاد همه از یک واجریشه‌اند ولی برای آگاهی
خواننده» جلر واژه‌های مشکوکك (شاید) آورده است.
[pdf page 68]
نج
آلیز آلیزیدن» آلیختن(به چم *جفتک انداختن») / ۶۹
کردی (015): 85-18571011 ,ل#13ا1 لیتوانی (/(م/ههنا بل 7ال): ,شا
سانسکریت (887۸758:)54۸43777 ب8۸[۸71 کشا
```


## [2026-09-04T19:22:04.121Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '41214,41224p' MON_part2.txt && echo \"=== MON آله eagle in part1 ===\" && grep -n '\\[- آله\\|آلوه' MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-04T19:22:04.203Z] TOOL RESULT

```
له: ۱۵۲ (ص.) از هم باشیده» مضمحل شده. 
حر ده شکسته. 

له: «۱ [- آله - آلوه ‏ اله| (.) (جان.) 
عقاب. 

لهات: :۱:۷ (ع. لهاة] (.) (پز.) زبان 
کوچک را گویند که عبارت از زایده‌ای 
است که از وسط شراع الحنک در عقب 
دهان و اتدای حلق آوبخته است؛ ملاز ه. 
=== MON آله eagle in part1 ===
MON_part1.txt:16467:اله: «ماه [- آله] (ا.) عقاب؛ آله. 
MON_part1.txt:56593:مبوه‌های خشکك شده مانند: توت آلوه 
MON_part2.txt:41218:له: «۱ [- آله - آلوه ‏ اله| (.) (جان.)
```


## [2026-09-04T19:22:10.507Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '^آله\\|آله:' MON_part1.txt | head -10; echo \"---\"; grep -n 'آله' MON_part1.txt | sed -n '1,25p'"
}
```


### [2026-09-04T19:22:10.588Z] TOOL RESULT

```
4506:آله کلو: 1011-(6-)212 [- آلا کلنک ] (امر.) 
4511:آلهه: مطعلة (ع.] (.) ج. اله» خدایان» ارباب» 
4515:آلهه پرست: احه2-. (افا ۰ آنکه چند ین 
97099:آله» آلغ. عقاب آهنین منقار: تير پیگان‌دار. 
---
4257:آلاچق ۳ آله‌چوق ] (.) سراپرده و سایبان دو 
4506:آله کلو: 1011-(6-)212 [- آلا کلنک ] (امر.) 
4511:آلهه: مطعلة (ع.] (.) ج. اله» خدایان» ارباب» 
4515:آلهه پرست: احه2-. (افا ۰ آنکه چند ین 
16467:اله: «ماه [- آله] (ا.) عقاب؛ آله. 
16480:این کلمه را با «آلهه» نباید ۳ 
39793:ترجیع: آلها [ع (مص‌م.) برگردانیدن. 
56979:خسفی: آله« (ع.] (ص.) نسهان» پسنهان؛ 
57340:خلیع: آلهد (ع.] (ص.) خلع شده. پریشان» 
65124:شدبدی دارد؛ آله کلو. . ضح. مفرد آن کمتر 
93057:طلیع : آله (ع.] (ص.) (فت.) آنکه از طرف 
93059:طلیعه: (م)«-آلها (ع. طليعة] (ا.) (نظ. قد.) 
97099:آله» آلغ. عقاب آهنین منقار: تير پیگان‌دار.
```


## [2026-09-04T19:22:14.833Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '97088,97104p' MON_part1.txt"
}
```


### [2026-09-04T19:22:14.881Z] TOOL RESULT

```
عقایین فرهنگ فارسی معین 


در قلل مرتفع آلپ و پیرنه بومی است. 
دیگر عقاب پیگارگک است که در سواحل 
دریا می‌زید و به همین جهت بنام عقاب دریا 
یز موسوم است. دیگر عقاب ملیلاتوس 
لوکوسفالوس که بنام عقاب آمریکایی نیز 
مشهور است (در سال ۲ ۱۸۷ میلادی 
قانونی در دومین کنگرة آمریکا به عنوان 
علامت رسمی دولت آمربکا شناخته شده)؛ 
آله» آلغ. عقاب آهنین منقار: تير پیگان‌دار. 
رشته‌ای که در سوارخ گوش کنند برای 
انداختن حلقه. 

عقایین: (ند. می«ردنده (ع.] تث. 
عقاب در حالت نصبی و جری (ولی در
```


## [2026-09-04T19:22:28.606Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'aquarium' KLN_1966.txt | head -5; echo \"--- eau de Cologne ---\"; grep -n 'Cologne' KLN_1966.txt | head -5; echo \"--- SKT eagle ---\"; grep -n 'aquila\\|Aquila' SKT.txt | head -8; echo \"--- SKT island ---\"; grep -n 'igland\\|iegland\\|island' SKT.txt | head -6; echo \"--- SKT tear ---\"; grep -n 'tagr\\|zahar\\|dakru' SKT.txt | head -8"
}
```


### [2026-09-04T19:22:28.725Z] TOOL RESULT

```
3262:Derivative:  the  hybrid  aquarell-ist,  n. aquarian,  adj.,  pertaining  to  an  aquarium.
3263:Formed  with  suff.  -an  fr.  aquarium, aquarium,  n.  —  L.  aquarium,  neut.  of  the  adjective aquarius,  ‘pertaining  to  water’,  used  as  a  noun. See  aquatic.
13908:ewer,  n„  a  wide-mouthed  water  pitcher.  —  ME., fr.  AF.  ewiere,  ewer,  corresponding  to  OF. aiguiere  (F.  aiguiire),  fr.  OProvenq.  aiguiera, ‘water  vessel’,  fr.  VL.  aquaria,  lit.  ‘pertaining  to, or  containing,  water’  (cp.  L.  vds  aquarium, ‘water  vessel’),  fr.  L.  aqua,  ‘water’.  See  aquatic and  cp.  aquarium.  Cp.  also  sewer, ex,  prep,  meaning  ‘out  of’  and  used  in  various phrases  of  Latin  origin.  See  ist  ex-, ex-  pref.  occurring  in  words  of  Latin  origin  used in  the  senses:  i)  out  of,  from;  2)  upward; 3)  completely,  entirely;  4)  to  remove  from,  de¬ prive  of ;  5)  without ;  6)  former  (said  of  previous holders  of  office  or  dignity).  Before  f  ex-  be¬ comes  ef-\  before  all  voiced  consonants  (as b,  d,  g,  etc.)  ex-  becomes  <?-.  —  L.  ex-,  from  the prep,  ex,  ‘out  of,  from’,  which  is  cogn.  with Gk.  iE„  £*,  ‘out  of’  (see  2nd  ex-).  Arm.  i,  ‘from’, pref.  y-  (as  in  y-arnem,  ‘I  rise’),  Gaul,  ex,  OIr. ess-,  ass-,  OPruss.  esse,  Lith.  it,  OSlav.  is-,  iz- (pref.),  iz  (prep.)  Cp.  extraneous,  strange, ex-  pref.  occurring  in  words  of  Greek  origin  and meaning  ‘out  of’.  —  Gk.  ig,  £x,  ‘out  of’.  The former  is  used  before  vowels  and  is  rendered in  English  by  ex-;  the  latter  appears  before  con¬ sonants  and  is  transliterated  ec-.  For  the  ety¬ mology  of  Gk.  IE,,  see  1st  ex-.  Cp.  ec-,  ecto- and  the  first  element  in  eschatology, ex-,  form  of  exo-  before  a  vowel, exacerbate,  tr.  v.,  to  render  worse,  aggravate.  — L.  exacerbatus,  pp.  of  exacerbare,  ‘to  exasper¬ ate,  irritate,  grieve,  afflict’,  fr.  ist  ex-  and  acer- bare,  ‘to  make  harsh  or  bitter;  to  aggravate’, fr.  acerbus,  ‘harsh  to  the  taste,  bitter;  sour’.  See acerb  and  verbal  pref.  -ate  and  cp.  acerbate, exacerbation,  n.  - —  Late  L.  exacerbatio,  gen. -dnis,  ‘exasperation’,  fr.  L.  exacerbatus,  pp.  of exacerbare.  See  prec.  word  and  -ion. exact,  adj.,  1)  accurate;  2)  precise.  —  L.  exactus, ‘precise,  accurate’,  pp.  of  exigere,  ‘to  demand, require’,  lit.  ‘to  drive  out  or  forth’,  fr.  ist  ex- and  agere,  ‘to  set  in  motion,  drive,  lead;  to  do, act’.  See  agent,  adj.,  and  cp.  act.  Cp.also  assay
29539:polyzoarium,  n.,  a  bryozoan  colony.  —  A  ModL. hybrid  coined  fr.  ModL.  Polyzoa,  a  word  of Greek  origin  (see  prec.  w'ord)  and  the  L.  suff. -driitm,  on  analogy  of  aquarium,  vivarium. polyzoary,  n.,  polyzoarium.  —  A  hybrid  coined fr.  ModL.  Polyzoa  (see  prec.  word)  and  suff. -ary  (representing  L.  -arium). pomace,  n.,  the  crushed  pulp  of  apples.  —  OF. pomaz,  pi.  of  pomat,  ‘cider’,  fr.  pome,  ‘apple’. See  pome.
38702:—  ModL.,  formed  fr.  L.  terra,  ‘earth’  (see  terra), with  suff.  -arium  on  the  analogy  of  aquarium. terrazzo,  n.,  a  kind  of  flooring.  —  It.,  rel.  to  ter- razza,  ‘terrace’.  See  terrace  and  cp.  trass, terrene,  adj.,  earthy,  earthly.  —  L.  terrenus ■  ‘of, or  pertaining  to,  the  earth,  earthy,  earthly  ,  fr. terra.  See  terra  and  -ene.
--- eau de Cologne ---
5362:Bordeaux,  bordeaux,  n.,  claret.  —  From  Bor¬ deaux,  name  of  a  city  and  seaport  in  Southern France;  so  called  because  the  wine  is  shipped from  Bordeaux.  The  name  of  the  city  derives  fr. F.  (la  ville  au)  bordd'eaux,  ‘(the  city  at)  the  edge of  waters’  (see  border  and  Eau  de  Cologne). bordel,  n.,  a  brothel.  —  F.,  fr.  Proven?.,  bordel , ‘brothel’,  fr.  OF.  bordel,  ‘a  poor  hut,  hovel’, dimin.  of  borde,  ‘hut’,  fr.  Frankish  *borda,  ‘hut made  from  planks’,  fr.  *bord,  ‘plank’,  which  is rel.  to  OE.  bord,  ON.  bord,  ‘plank’.  See  board, ‘table,  plank’.
8255:cologne,  n.,  perfumed  liquid.  —  Shortened  fr. eau  de  Cologne,  lit.  ‘water  of  Cologne’,  fr. Cologne,  French  name  of  Koln  in  Germany, orig.  called  Colonia  Agrippina  (‘colony  of Agrippa'),  after  Agrippa,  wife  of  the  Roman emperor  Claudius.  Cp.  Eau  de  Cologne, colon,  n.,  that  part  of  the  larger  intestine,  which extends  from  the  caecum  to  the  rectum  (anal.)
12563:Eau  de  Cologne,  cologne.  —  F.,  lit.  ‘water  of Cologne’.  See  eau  de  vie  and  cologne.
30952:pulldoo,  n.,  the  coot.  —  Fr.  F.  poule  d'eau,  lit. ‘water  hen'.  See  pullet  and  Eau  de  Cologne.
32965:Derivatives:  ripple,  n.,  slight  motion  of  the waves;  wavelet,  rippl-et,  n.,  a  small  ripple. Ripuarian,  adj.,  pertaining  to  the  Franks  settled on  both  sides  of  the  Rhine  near  Cologne.  — Lit.  ‘living  on  the  banks  of  a  river’,  fr.  ML.  ri- pudrius,  the  same  as  L.  riparius.  See  riparian. For  sense  development  cp.  Lithuanian. rise,  intr.  v.  —  ME.  risen,  fr.  OE.  risan,  rel.  to  OS. risan,  ON.  risa,  Goth,  ur-reisan,  ‘to  rise’,  OHG. risan,  ‘to  rise,  flow’,  G.  reisen,  ‘to  travel’  (the original  meaning  was  ‘to  rise  for  a  journey’). These  words  possibly  derive  fr.  I.-E.  base  *rei-, ‘to  move,  flow,  run’,  whence  L.  rivus,  ‘brook, stream’.  See  rival  and  cp.  arise,  raise,  rear. Derivatives:  rise,  n.,  ris-er,  n.,  ris-ing,  adj.  and n.
--- SKT eagle ---
--- SKT island ---
6176:Eyot,  a  little  i  land.  (Scand.>  Also spelt  ait.  eyet,  eyght.  From  M.  E.  /i,  an island  =<  Icel.  ey,  an  island  ;  with  dimin. snfFix  -tt,  as  in  hefm-tt.  ITie  A.  S.  form  is igo^,  igeafS  ;  where  ig  is  cognate  with  IceL ty ;  see  lalaad.
9270:Insular.  (L.)  L.  Mjw/aru,  insular.— L.  insuiA.  an  island.  Prob.  from  L.  in sa/e-in  the  main  sea,  where  saJo  is  abl  of L.  ta/um.  the  main  sea,  cognate  with  t»k. oiKai,  tur^f^  aweli  oi  the  aea.  AUicd  l« Swea
9274:Ulo.  ma  ifil*nd.  {F.-L.)  O.  F.  is/e  (F. /".VJ  — L.  inm/a,  an  island  (ftbove).
11148:Maroon  {3),  to  put  ashore  oa  a  dcMiU island.  (F— Span.  — L—Gk.)  F  *w ftdj.  fugitive,  applied  to  a  lu who  takes  refuge  in  woods  tk: [Hence  E.  maroon,  to  treat  :< cause  to  be  fogitivc."'  A  tl>i Span.  n'marrvH,  wild,  unruly, the  mountain^tops.  — Sp.in.  rima,  m tain-top.  (So  also  Ital.  and  Port.  rimM^ time.)  The  O.  Span,  cima  also  meant sprout,  twig  (Diex).  — L.  tyma,  a  v sprout.  — Gk.  nvita,  anything  swoUcSi wave,  a  yotmg  sprout,  %  Ntgrp  ei. or  a'nitirtvH  was  an  everj-day  phrase  fori fugitive  slave  hidden  io  Uie  monnuinH^ Cuba,  about  a.d.  1846.
13716:Penguin,  Pinguin,  a  bird.  (C a  tract  piinlcd  m  i<;>>8,  we  read  thi Drake  gave  a  certain  island  the  r Penguin  Island  in  1587,  from  the  { found  there.  The  word  appei pen  £iv)'n,  i.  e.  white  head.  If rirst  have  been  given  to  another the  auk  (the  puOin  is  common  in  An since  the  penguin's  head  u  black.
13717:Peninsula.  (L.)    t,.  fent of  land  nearly  an  island.  ~L. almost ;    insuia,  an  uUnJ. ultisnaie,   almost    the    iosl,    last] pen-umbro,  partial  shadow.
--- SKT tear ---
6671:Flagellate.  (L.)  From  pp.  of  U fiagtUart^  to  scourge.  ^'L.Jtarelium.  dimin. of Jtagrum,  a  scourge,     {y  nllLAG,')
10903:nui^lAte,  ■  great  man.  noble.  (F.  — L.) (iM/.^L.  i««4<na//M,  ace.  of  $nagtms, ,  — U  m4jr9HWi  great.    %  Magnate lo  the  a*a  of  L.  M^yfio/  in  1  lungnry Poland. Macnifioent-    (U)     L>.   magnifirtnt', of    mmgmjiffm,     lit.    doing     grrat ^lffa«d.  — 1-.  ntagrtt",  lor  wrajf- Tgreat ;  -/can.  (ot/uiens,  doing,  from r.  to  do. ;WgnUy.  (F.-L.)  M.  F.  «^H/>f^M.- tgftffitr.^  L.  magmjUare,  lit.  to  make *  L.     jwa^tti*,    lor    w/^mmj,    grcfti  ; r,  for  fjuert,  to  do.
```


## [2026-09-04T19:22:36.128Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'Eagle\\.' SKT.txt | head -5; echo \"---\"; grep -n -i 'Tear (2)\\|Tear,\\|Tear (1)' SKT.txt | head -5; echo \"--- island ---\"; grep -n -i 'Island\\.' SKT.txt | head -5"
}
```


### [2026-09-04T19:22:36.212Z] TOOL RESULT

```
850:Aquiline,  like  an  eaRle.  (F.  -  L.)  F. aquilin  ;  hence  nez  aqaHin,  '  a  no^e  like  an eagle;*  Cot  «  L.  aquilmus,  adj.  from ff^uJla,  on  eagle.
---
9818:bat*  a  tittle  taoe.  thong.  (F.->L.) )mhft.  ••  O  P.  ia€*U  ■  lace ;  dimin. a  lice  ;  see  above. rate,  to  tear.  (L.)  From  pp.  of T«nf,  to  tear.  —  L.  later^  mangled, •  Gk-  Aa««/rui,  lorn  :  Aan\  a  rent ; »(*i,  to  tear,  W  WR.MC) oarato.  1 1 . )  From  pp.  of  L.  di-tac- o  Ceir  avnn'Icr.
9819:nyixuLl,  laacrinial.  pertaining  to [L.1  Tbe»pe!Iin(;/dMrv/rta/i>  bad. w^-tfu,  better  itictwmt,  /airrma^  a O.  L.  da^rtMUt   a   tear,      Coj^nate
16029:Bevere.  (K.-L.)  O.  F.  rrvtrtr  (F. r^jjrtr),  to  reverence.  —  L.  rtuereri,  to icvcre,  slaniJ  in  awe  of.  — L.  n-,  again; uertri,  lo  tear,  feci  awe,  allied  to  E. Wary.  ■  Der.  rtvtfxmtt  F.  reveretut,  L. ttu(r£ntia.
19257:train-oil.  (Du. ;  andF.  -  L.  -  Gk.) For  oil,  sec  Oil  Formerly  tranepylt  or (rant.  —  O.  Du. /ra^«,  •  traync-oyle  made of  the  fat  of  whales;  also  a  tcnr.  liquor pressed  out  by  the  tire;'  Mexhniu.  Tlie orifi-  sense  IS  Mcar;'  then  tlrops  forced  out in  boiling  blubber,  &c.  Mod.  Du.  traan, a  lear,  G.  trixhnt.  The  G-  trihtte  is  really a  pi  form  M.  H.  G.  traAfrt/,u\.  oitrahen,  j a  tear,  closely  allied  to  M.  H.  G.  MA/r(pDt for  eaAa-*)t  a  tear.    Similarly,  Du.  traan  \
19259:is  allied  to  Dan.  taar,  a  tear,  and  (0  C tear  \aI»ovc).
--- island ---
849:eubaqueouB,  under  water.  (L.)  L  w*, nnder ;  a'/ua,  water.  And  see  Ait,  Ejrot, Island.
9270:Insular.  (L.)  L.  Mjw/aru,  insular.— L.  insuiA.  an  island.  Prob.  from  L.  in sa/e-in  the  main  sea,  where  saJo  is  abl  of L.  ta/um.  the  main  sea,  cognate  with  t»k. oiKai,  tur^f^  aweli  oi  the  aea.  AUicd  l« Swea
11148:Maroon  {3),  to  put  ashore  oa  a  dcMiU island.  (F— Span.  — L—Gk.)  F  *w ftdj.  fugitive,  applied  to  a  lu who  takes  refuge  in  woods  tk: [Hence  E.  maroon,  to  treat  :< cause  to  be  fogitivc."'  A  tl>i Span.  n'marrvH,  wild,  unruly, the  mountain^tops.  — Sp.in.  rima,  m tain-top.  (So  also  Ital.  and  Port.  rimM^ time.)  The  O.  Span,  cima  also  meant sprout,  twig  (Diex).  — L.  tyma,  a  v sprout.  — Gk.  nvita,  anything  swoUcSi wave,  a  yotmg  sprout,  %  Ntgrp  ei. or  a'nitirtvH  was  an  everj-day  phrase  fori fugitive  slave  hidden  io  Uie  monnuinH^ Cuba,  about  a.d.  1846.
13717:Peninsula.  (L.)    t,.  fent of  land  nearly  an  island.  ~L. almost ;    insuia,  an  uUnJ. ultisnaie,   almost    the    iosl,    last] pen-umbro,  partial  shadow.
```


## [2026-09-04T19:22:49.129Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%AF%DA%A9%D9%84%D9%86",
 "prompt": "Persian ادکلن — give the etymology (source language, French eau de Cologne?), pronunciation and meaning. If the page does not exist, say so."
}
```


## [2026-09-04T19:22:50.481Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/aquarium",
 "prompt": "Etymology of \"aquarium\": date of coinage, Latin aquarium/aquarius, and relation to aqua. Also anything about \"eau\" and \"eau de Cologne\" if mentioned."
}
```


### [2026-09-04T19:22:53.308Z] TOOL RESULT

```
# Persian: ادکلن (odkolon)

**Etymology:** This word was borrowed from French *eau de Cologne*, which literally translates to "cologne water."

**Pronunciation:** In Iranian Persian (formal), it's pronounced as [ʔod̪.kʰo.lón], with alternate pronunciations including [ʔo.d̪e.kʰo.lón] and [ʔo.d̪o.kʰo.lón].

**Meaning:** The term refers to cologne or a man's perfume, commonly used in Iran.
```


### [2026-09-04T19:22:56.207Z] TOOL RESULT

```
# Etymology of "Aquarium"

**Date of Coinage:**
The word entered English in 1830, initially meaning "artificial pond in a garden for growing aquatic plants." The modern sense of "vessel of glass filled with water in which living aquatic animals are kept indoors" emerged by 1853.

**Latin Origins:**
The term derives from the Latin adjective *aquarius*, meaning "pertaining to water." As a noun, *aquarius* meant "water-carrier." This traces back to Latin *aqua* (water), which originates from the Proto-Indo-European root *akwa- (water).

**Historical Context:**
The Victorian enthusiasm for indoor aquariums began with Philip Henry Gosse's 1854 book "The Aquarium." An earlier proposed name was "marine vivarium." In Latin, *aquarium* originally referred to "drinking place for cattle."

**Note on "Eau":**
The provided content does not mention "eau," "eau de Cologne," or related French water terminology, so no information on those topics is available from this source.
```


## [2026-09-04T19:23:05.206Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tear",
 "prompt": "Etymology of \"tear (n.1)\" fluid from the eye: Old English tear, teagor, Proto-Germanic *takhr-/*tagr-, PIE *dakru-, and the cognates (Latin lacrima, Greek dakryma, Old Irish der, Sanskrit acru, Avestan asru)."
}
```


## [2026-09-04T19:23:06.234Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%B3",
 "prompt": "Persian ارس (ars) — is there a sense \"tear\"? Give its etymology: Middle Persian ars, Proto-Iranian *Hácru, PIE *h₂éḱru, and any Avestan form cited."
}
```


### [2026-09-04T19:23:10.069Z] TOOL RESULT

```
# Etymology of "Tear" (The Fluid)

The word "tear" (referring to the fluid from the eye) has ancient roots. It originates from Old English *tear* or *teor*, tracing back through Proto-Germanic *tahr-* and *tagr-* to the Proto-Indo-European root *dakru-*.

This same root appears across many languages: Latin *lacrima*, Greek *dakryma*, Old Irish *der*, and Welsh *deigr*. The term initially referred not just to tears but also to "drop" and "nectar" more broadly.

The figurative sense of "tears" meaning "grief" or "sorrow" emerged by the mid-14th century. Common phrases like "in tears" (meaning weeping) appeared around the 1550s, while "tear gas" entered usage around 1917.
```


### [2026-09-04T19:23:11.972Z] TOOL RESULT

```
# Persian ارس (ars) — "Tear" Etymology

Yes, the word has this sense. According to the Wiktionary entry, the archaic Persian noun **ارس** (ars) means "tear," with the synonym listed as اشک (ašk).

## Etymology Chain

The documented etymology traces back through these stages:

1. **Middle Persian**: ʾrs /ars/ ("tear")
2. **Proto-Iranian**: *Hácru ("tear")
3. **Proto-Indo-Iranian**: *Háćru ("tear")
4. **Proto-Indo-European**: *h₂éḱru ("tear")

The entry does not cite a specific Avestan form in the provided content, though the etymological reconstruction references Proto-Iranian as an intermediate stage in the word's development across these ancient language families.
```


## [2026-09-04T19:23:18.857Z] TOOL CALL #68: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A7%D8%B4%DA%A9' --note 'page 44, root Akru/Dakru, node #3: Persian ashk etymology (PIr *Hacru, PIE *h2ekru), doublet of ars' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%B3' --note 'page 44, root Akru/Dakru, node #3: Persian ars \"tear\" < MP ars < PIr *Hacru' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction%3AProto-Indo-European/d%C3%A1%E1%B8%B1ru' --note 'page 44, root Akru/Dakru: PIE *dakru and its disputed relation to *h2ekru' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/tear' --note 'page 44, root Akru/Dakru, nodes #4-#5: Gmc *tahr-/*tagr- > OE tear' 2>&1 | tail -3"
}
```


### [2026-09-04T19:23:21.533Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/14694908e666d3b3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4c015f9ec66fabea.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/94a382d5f45a1a7f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2d9a52ce95203851.txt
```


## [2026-09-04T19:23:31.584Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A2%D9%84%D9%87' --note 'page 44, root Akwa, node #4: Persian aleh/aluh \"eagle\" < MP aluh < PIr *Hrjifyah < PIE *h2rg-i-pt-ios' 2>&1 | tail -2\ncd /home/sfmqrb/git/rishe && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction%3AProto-Indo-European/h%E2%82%82ek%CA%B7eh%E2%82%82' --note 'page 44, root Akwa: PIE *h2ekweh2 \"water\" > Lat aqua, PGmc *ahwo' 2>&1 | tail -2\ncd /home/sfmqrb/git/rishe && python3 tools/fetch_source.py 'https://www.etymonline.com/word/eagle' --note 'page 44, root Akwa, nodes #5-#7: eagle < OF aigle < L aquila, aquilus/aqua link disputed (de Vaan)' 2>&1 | tail -2\ncd /home/sfmqrb/git/rishe && python3 tools/fetch_source.py 'https://www.etymonline.com/word/island' --note 'page 44, root Akwa, nodes #11-#12: OE igland < PGmc *awjo \"thing on the water\" < *akwa-' 2>&1 | tail -2\ncd /home/sfmqrb/git/rishe && python3 tools/fetch_source.py 'https://www.etymonline.com/word/aquarium' --note 'page 44, root Akwa, nodes #8-#10: aquarium 1830 from L aquarium/aquarius' 2>&1 | tail -2\ncd /home/sfmqrb/git/rishe && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A7%D8%AF%DA%A9%D9%84%D9%86' --note 'page 44, root Akwa, node #9: Persian odkolon < French eau de Cologne' 2>&1 | tail -2"
}
```


### [2026-09-04T19:23:34.922Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ab30a1ac2d842443.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/57e658ca27c18c1b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f6dc263affbb2aea.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6e512d74dddc9a0e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6788c547de391431.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f39ca93497ea06b0.txt
```


## [2026-09-04T19:23:41.931Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '277p' AHD_watkins1985.txt && echo \"=== LEW aqua ===\" && grep -n '^aqua\\|aqua,' LEW_1910.txt | head -5 && echo \"=== SYN tear section ===\" && grep -n 'Av. asru\\|asru-\\|ašk\\|ask ‘tear' SYN.txt | head -8 && echo \"=== SYN island/water ===\" && grep -n 'ISLAND' SYN.txt | head -4"
}
```


### [2026-09-04T19:23:42.038Z] TOOL RESULT

```
akwa-. Water. 1. Germanic *agwjd becoming *auj6, “thing on the water,” in Old English ig, ieg, island, and
=== LEW aqua ===
=== SYN tear section ===
8194:TS oF THE BUD AR suet ‘dumb’, and ‘blind’. 6. ChSl. glucht, etc., general Slavic, words £08 a: Falk-Torp 179. outside connections? Berneker 308, 309. rate? Fie kurtinas, Lett. kurls, Briickner 145 (unconvincing). 5, Lith. 1 Jriinit ‘having a mutilated urn”) (of. also Russ. kur-guzyj 7. Skt. badhira- : Ir. bodar (above, 3). eat oF n08e" Uke. kur-nosyj ‘snub- Av. karana- (so NPers. kar ‘deaf’), see tailed’, ‘deaf’ ighort- ob. also Av. karana- ‘deaf’, | above, 5 and Barth., IF 3.169. nosed’), PF tghort-eared’, all with com- Av. asrut-gao8a-, lit. ‘having unhearing Skt. kara of mutilated and presumably | ears’ (cpd. of a- privative with sru- ‘paler ‘out’. Mil. -Fndz. 2.323. | ‘hear’ and gaoga- ‘ear’). Barth. 223. fr. UE Berneker 6 4.96 DUMB ‘ Goth. dumbs, baufs Lith. nebylys, beZadis Grk. a ori ON  dumbr Lett. méms NG oie Dan. stum ChSl. némit Lat. muto, mutolo Sw. stum SCr. nijem Be et OE dumb Boh.  némy s, —imudo ME = dumb Pol. — niemy a mut NE dumb Russ. nemoj it * amlabar, balb Du. stom Skt.  miika- Nir. balbh OHG _ stum (tumb) Av. afravaota- W. mud MHG stum (tump) Br. = mud NHG  stumm
28531:Grk.  daxpu Goth. tagr Lith. aSara NG daxpu ON lar Lett. asara Lat. lacrima Dan.  aare ChSl. _ sliza It. lacrima Sw. tdr SCr. — suza Ir. larme OE téar, teagor Boh. © slza Sp. ldgrima ME tere Pol. iza Rum.  lacrimdé NE tear Russ. — sleza Tr. dér Du. traan Skt. acru-, baspa- Nir. deor OHG zahar, trahan Av. asru- W. deigryn MHG zaher, trahen
28536:(NHG zdhre, poet.), with gramm. change Goth. tagr, OE teagor, also OHG trahan, drahan, MUG trahen (and traher by con- fusion with zaher), NHG trdne, OS pl. trahni, Du. traan; Lith. asara, Lett. asara, Skt. agru-, Av. asru- (in asril- azan- ‘shedding tears’), Toch. akar.
=== SYN island/water ===
1100:. THE PHYSICAL WORLD IN ITS LARGER ASPECTS 29 1.25 ISLAND a j Gothis csc Lith. sala Grk. fies land Lett. sal NG de one Zi page ChSl. tok ostrovit
```


## [2026-09-04T19:23:45.135Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28528,28545p' SYN.txt | fold -w 180 | head -40"
}
```


### [2026-09-04T19:23:45.197Z] TOOL RESULT

```
8. Skt., Av. rud- (but Av. rud- ‘moan’ of cattle and daevic beings, Barth 1492), above, 1. :
Av. garaz- (‘moan, bemoan’, Osset, yarzun ‘groan’; Barth. 516) : Skt. garh- ‘blame, reproach’, OHG klagon, NHG klagen ‘complain’, etc., fr. a guttural ex- tension o
f the root in W. galw ‘ery out, call’, ete. Walde-P. 1.539,
16.38 TEAR (sb.)
Grk.  daxpu Goth. tagr Lith. aSara NG daxpu ON lar Lett. asara Lat. lacrima Dan.  aare ChSl. _ sliza It. lacrima Sw. tdr SCr. — suza Ir. larme OE téar, teagor Boh. © slza Sp. l
dgrima ME tere Pol. iza Rum.  lacrimdé NE tear Russ. — sleza Tr. dér Du. traan Skt. acru-, baspa- Nir. deor OHG zahar, trahan Av. asru- W. deigryn MHG zaher, trahen
Br. daeraouenn NHG _tréne (zéhre)
The usual words for ‘tear’, except the Slavic, belong to a group which, while showing some peculiar variations, points clearly to the existence of a distinctive TE word for ‘
tear’.
1.IE *dakru-, also *draku- and *alru-, relations variously explained. Walde-P. 1.769. Walde-H. 1.746. Er- nout-M. 516. Pedersen 1.124. Falk- Torp 1239.
Grk. daxpu, pl. daxpva, whence new sg. daxpvov; OLat. dacruma, Lat. lacruma, lacrima (> Romance words); Ir. dar, NIr. deor, déar, W. (old) deigr, pl. dagrau, OBr. dacr, Br. daer,
 pl. daerou, new sgs. W. deigryn, Br. daeraouenn; ON ‘ar, OE téar, OHG zahar, etc.
(NHG zdhre, poet.), with gramm. change Goth. tagr, OE teagor, also OHG trahan, drahan, MUG trahen (and traher by con- fusion with zaher), NHG trdne, OS pl. trahni, Du. traan; Lith.
 asara, Lett. asara, Skt. agru-, Av. asru- (in asril- azan- ‘shedding tears’), Toch. akar.
2. ChSl. sliza, etc., general Slavic, etym.? Briickner 316 compares Grk. Atw ‘hiccough, sob’, Ir. slucim ‘swallow ; MHG slucken ‘swallow’, etc. (Walde-P. 2.711). ,
3. Skt. baspa- (also ‘steam’), prob:
? MiIndic form of *varsman- : Ur$- ie sb. varsa- (1.75). Tedesco, Languag
22.184 ff.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
{EMPERAMENTAL, MORAL, AESTHETIC NOTIONS
Digitized by Arya Samaj Foundation Chennai and eGangotri
1131
16.389 GROAN (vb.)
```


## [2026-09-04T19:23:57.227Z] TOOL CALL #72: Bash

```json
{
 "command": "ls data/extracted/ && find . -maxdepth 3 -iname '*.pdf' 2>/dev/null | head -20"
}
```


### [2026-09-04T19:23:57.278Z] TOOL RESULT

```
batch
NEXT_CHUNK
RETRY.txt
test
./EtymologicalDictionary-persian-english.pdf
```


## [2026-09-04T19:24:00.714Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb && (pdftotext -f 44 -l 44 -layout EtymologicalDictionary-persian-english.pdf - 2>/dev/null | head -80) || echo \"pdftotext unavailable\""
}
```


### [2026-09-04T19:24:02.450Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:24:04.499Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb && which pdftotext pdftoppm; ls -la EtymologicalDictionary-persian-english.pdf"
}
```


### [2026-09-04T19:24:06.396Z] TOOL RESULT

```
Exit code 2
/usr/bin/pdftotext
/usr/bin/pdftoppm
ls: cannot access 'EtymologicalDictionary-persian-english.pdf': No such file or directory
```


## [2026-09-04T19:24:10.879Z] TOOL CALL #75: Bash

```json
{
 "command": "ls -la *.pdf && pdftoppm -f 44 -l 44 -r 150 -png EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p44 && ls /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-04T19:24:12.774Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 23984297 Aug 22 01:02 EtymologicalDictionary-persian-english.pdf
add101.py
afm_p8-008.png
afm_p9-009.png
AGENT_INSTRUCTIONS.md
agent_registry.tsv
apply_p31.py
aryhdr_200.png
aryhdr_300.png
aryhdr_450.png
ary_index.log
bibliography_raw.txt
bqt_282.jpg
bqt3_p1-001.png
bqt3_p300-300.png
bqt4_p1-001.png
bqt4_p300-300.png
bqt5_p1-001.png
bqt5_p150-150.png
bqt70_bottom.png
bqt70.jpg
bqt70_mid.png
bqt70_top.png
build34.py
build41.py
buzina.html
charts
cheung.pdf
cheung.txt
chunks.txt
crop_abu.png
crop_ml.png
crop_names.png
ctx
ctx.py
cup_iss.html
djvu.sh
dom.html
dom_path.html
epub
eshia.html
ffd-001.png
ffd-002.png
ffd-003.png
ffd8-008.png
ffd.html
ffd_test-030.pgm
ffd_test_out2.txt
ffd_test_out.txt
findings_A.json
findings_B.json
findings_C.json
findings_D.json
gb2.txt
gb_kgw.html
gbs_ahd.html
gbs_cel.html
gbs_iss.html
gbs_prt.html
gbs_wld2.html
gbs_wld.html
gb.txt
gb_zaw.html
hd
hdr_200.png
hdr_300.png
ht2.html
ht_burhan-i+qati.html
ht_burhan+qati+muin.html
ht_farhang-i+farsi+mu%27in.html
ht_farhang-i+farsi+muin.html
ht.html
ht_test
ia.sh
irn-001.png
irn-002.png
irn-003.png
irn-004.png
irn12-012.png
jstor.html
kgw_150.html
kgw_161.html
kgw_268.html
kgw_55.html
kgw_site.html
kn107170.html
kn59626.html
leaf.py
merge.py
mk35.py
mk39.py
modelcmp
mon
next_chunks.py
nl.html
nls.html
ocr_all.log
ocr_all.sh
ocr_books.log
ocr_BQT_v3
ocr_kill.sh
ocr_one.sh
off_ffd-040.png
off_irn-100.png
off_irn-101.png
off_vie-100.png
old.html
old_template.html
p33-033.png
p33hi-033.png
p33.txt
p35-035.png
p38-038.png
p39
p43-043.png
p43.txt
p44-044.png
pagemap.log
pagemap_v3.log
pageoff.py
paginate.py
pg
pico3.html
pico.html
psearch.py
pt_coo.31924026891675.html
pt_coo.31924027949522.html
pt_mdp.39015066210397.html
pt_mdp.39015066210405.html
pt_uc1.b3827767.html
pt_uc1.b3827768.html
q
queue_opus10.txt
queue.txt
rc
ref_counts.txt
refs
refs_online.json
refs_online_persian.json
refs_online_western.json
shot_path.png
shot_roots.png
SOURCE_MATRIX.md
test.html
test_path.html
upd.py
work
write_101_345.py
z_abu-033.png
z_borr-033.png
```


## [2026-09-04T19:24:16.235Z] TOOL CALL #76: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p44-044.png"
}
```


### [2026-09-04T19:24:16.264Z] TOOL RESULT

```

```


## [2026-09-04T19:25:12.302Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -s -L -o bqt_v1_n315.jpg \"https://archive.org/download/borhan-ghate-v1/page/n315_w1400.jpg\" --max-time 60 && file bqt_v1_n315.jpg && ls -la bqt_v1_n315.jpg"
}
```


### [2026-09-04T19:25:15.629Z] TOOL RESULT

```
bqt_v1_n315.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
-rw-rw-r-- 1 sfmqrb sfmqrb 541820 Sep  4 15:25 bqt_v1_n315.jpg
```


## [2026-09-04T19:25:19.139Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt_v1_n315.jpg')\nw,h=im.size\nim.crop((0,int(h*0.55),int(w*0.55),h)).resize((int(w*0.55*0.8),int(h*0.45*0.8))).save('bqt_v1_n315_crop.png')\nprint(im.size)\n\" 2>&1 | tail -3"
}
```


### [2026-09-04T19:25:21.193Z] TOOL RESULT

```
(2479, 3508)
```


## [2026-09-04T19:25:24.517Z] TOOL CALL #79: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt_v1_n315_crop.png"
}
```


### [2026-09-04T19:25:24.547Z] TOOL RESULT

```

```


## [2026-09-04T19:25:36.330Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt_v1_n315.jpg'); w,h=im.size\nim.crop((0,int(h*0.70),w,int(h*0.88))).save('bqt_fn.png')\nim.crop((0,0,w,int(h*0.09))).save('bqt_hdr.png')\n\""
}
```


### [2026-09-04T19:25:38.413Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:25:40.685Z] TOOL CALL #81: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt_fn.png"
}
```


### [2026-09-04T19:25:40.825Z] TOOL RESULT

```

```


## [2026-09-04T19:25:40.823Z] INPUT

[Image: original 2479x632, displayed at 2000x510. Multiply coordinates by 1.24 to map to original image.]


## [2026-09-04T19:25:54.878Z] TOOL CALL #82: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt_hdr.png"
}
```


### [2026-09-04T19:25:54.941Z] TOOL RESULT

```

```


## [2026-09-04T19:25:54.939Z] INPUT

[Image: original 2479x315, displayed at 2000x254. Multiply coordinates by 1.24 to map to original image.]


## [2026-09-04T19:25:58.252Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt_v1_n315.jpg'); w,h=im.size\nim.crop((0,int(h*0.07),w,int(h*0.16))).save('bqt_hdr2.png')\n\""
}
```


### [2026-09-04T19:26:01.187Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:26:03.643Z] TOOL CALL #84: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt_hdr2.png"
}
```


### [2026-09-04T19:26:03.726Z] TOOL RESULT

```

```


## [2026-09-04T19:26:03.724Z] INPUT

[Image: original 2479x316, displayed at 2000x255. Multiply coordinates by 1.24 to map to original image.]


## [2026-09-04T19:26:10.354Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -s -L -o bqt_v1_n268.jpg \"https://archive.org/download/borhan-ghate-v1/page/n268_w1400.jpg\" --max-time 60 && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt_v1_n268.jpg'); w,h=im.size\nprint(im.size)\nim.crop((0,int(h*0.05),w,int(h*0.14))).save('bqt58_hdr.png')\nim.crop((0,int(h*0.62),w,int(h*0.90))).save('bqt58_fn.png')\n\""
}
```


### [2026-09-04T19:26:13.806Z] TOOL RESULT

```
(2479, 3508)
```


## [2026-09-04T19:26:16.170Z] TOOL CALL #86: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt58_fn.png"
}
```


### [2026-09-04T19:26:16.384Z] TOOL RESULT

```

```


## [2026-09-04T19:26:16.381Z] INPUT

[Image: original 2479x983, displayed at 2000x793. Multiply coordinates by 1.24 to map to original image.]


## [2026-09-04T19:26:36.740Z] TOOL CALL #87: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt58_hdr.png"
}
```


### [2026-09-04T19:26:36.813Z] TOOL RESULT

```

```


## [2026-09-04T19:26:36.811Z] INPUT

[Image: original 2479x316, displayed at 2000x255. Multiply coordinates by 1.24 to map to original image.]


## [2026-09-04T19:27:07.324Z] TOOL CALL #88: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT\ncat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/58.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, vol. 1, printed p. 58 (archive.org borhan-ghate-v1, leaf n268;\nrunning head \"— ۵۸ —\", right head \"آلو\"). Read from the page image by claude-fable-5-1, 2026-09-04.]\n\nBody (entry آله, right column, upper part of page — quoted in Mo'in's footnote 6):\n«له بالول مقسوم مرغی باشد نی مخلب که بر کوههای بلند آشیانه کند و بغایت قوی و بزرگ\nبود و آنرا آله نیز خواندند و بتازی عقاب گویند. حکیم فرقدی راست:\n    مثل دشمنان تو با تو        حیلهٔ کبک و حمله های له است.»\n\nMo'in's footnote (note 6, on آله / له \"eagle\"):\n«در همهٔ فرهنگها آله بمعنی عقاب آمده و در بسیاری از لهجه های کنونی ایران نیز چنین است\nچنانکه «هلو» در کردی و «اله» در مازندرانی و «آلغ» در گیلکی. در کارنامهٔ اردشیر بابکان\n(۱۴ : ۱۲) āluh بمعنی عقاب بکار رفته است و نیز در بندهش (۱۴ : ۲۳) arvâ بمعنی عقاب\nآمده «فلاباس ۲۹۶-۹۸»، در طبری alleh، مازندرانی کنونی allē و alē «واژه نامه ۴۸».»\n\n(Earlier on the same page, footnote 6 of the آله entry also refers to Hamza Isfahani's\nal-Tanbih ʿalā ḥudūth al-taṣḥīf and Maydani's al-Sāmī fi'l-asāmī translating عقاب by آله,\nand to Biruni's al-Tafhīm.)\nEOF\ncat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/103.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, vol. 1, printed p. 103 (archive.org borhan-ghate-v1, leaf n315;\nrunning head \"— ۱۰۳ —\"). Read from the page image by claude-fable-5-1, 2026-09-04.]\n\nEntry (right column, bottom):\n«ارس ـ بفتح اول و ثانی و سکون سین بی نقطه، نام رودخانه است مشهور که از کنار تفلیس و\nمیان آذربایجان و ارمنستان می‌گذرد ۳ ـ و بفتح اول و سکون ثانی، اشک چشم را گویند ۴ ـ و\nبضم اول و سکون ثانی نام سرو کوهی است که بعربی ابهل و عرعر خوانند و تخم و ثمر آنرا\nجوز الابهل و ثمرة العرعر گویند ۵.»\n\nMo'in's footnotes on that page:\n«۳ ـ آنرا در قدیم Erask و یونانیان Araxe میگفتند. «۱۰ ب ۲۵۸۹».»\n«۴ ـ اوستا asrû, asrav (اشك) «بارتولمه ۲۲۲»، پهلوی ars، «بندهش ۹۰»، «اوست ۲۰»،\nطبری asli، مازندرانی کنونی ari و hasri «واژه نامه ۵۰۹».»\nEOF\necho saved; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/"
}
```


### [2026-09-04T19:27:07.435Z] TOOL RESULT

```
saved
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1225.png
1225.txt
1225.vision.txt
1357.png
1357.txt
1385.png
1385.txt
1385.vision.txt
1455.png
1455.txt
1488.png
1488.txt
1803.png
1803.txt
2407.png
2407.txt
58.vision.txt
70.vision.txt
72.vision.txt
```


## [2026-09-04T19:27:13.257Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'aqua' LEW_1910.txt | head -6; echo \"=== SYN 1.31 WATER ===\"; grep -n '1\\.31 WATER' SYN.txt | head -3"
}
```


### [2026-09-04T19:27:13.325Z] TOOL RESULT

```
=== SYN 1.31 WATER ===
1220:1.31 WATER
```


## [2026-09-04T19:27:16.620Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1100,1120p' SYN.txt | fold -w 180 | head -25; echo \"======= water =======\"; sed -n '1220,1240p' SYN.txt | fold -w 180 | head -20; echo \"== LEW size/sanity ==\"; head -c 300 LEW_1910.txt"
}
```


### [2026-09-04T19:27:16.701Z] TOOL RESULT

```
. THE PHYSICAL WORLD IN ITS LARGER ASPECTS 29 1.25 ISLAND a j Gothis csc Lith. sala Grk. fies land Lett. sal NG de one Zi page ChSl. tok ostrovit
Lat.  isula
SCr. _ otok, ostrvo
} Sw. 6
ae tee OE 1g, tgland, éaland Boh. _ ostrov ae isla ME tland, vee ' = poe wyspa
‘ , NE island (isle uss. ostrov Rum. nel (ostrov) ae aon ( oe ae Nir. oiledn (inis) OHG sila Av. — dvaépa- W. ynys MHG tinsel Br. enez NHG  insel
Words for ‘island’ reflect its relation to the water, as ‘floating’, ‘water-land’, ‘flowed around’, etc.
1. Grk. vijoos, Dor. vaoos, prob. : vaxw ‘swim’, Lat. nare ‘swim’, Skt. snd- ‘bathe’, etc. Walde-P. 2.692. Brug- mann, Grd. 2.1.541. Solmsen, Beitrage 244.
2. Lat. msula (> Romance words, but Rum. insuld neolog.), etym. disputed, but perh. best taken as fem. of an adj. *en-salos ‘in the sea’ (like Grk. é-d1os) : salum ‘sea’ (
or : sal, salis ‘salt’, but its use for ‘sea’ seems to be only poet.). Walde-P. 2.452. Walde-H. 1.707. The view that insula and Grk. vfjcos belong together, reflecting some
 Aegean word (Ernout-M. 491; Skok, Glotta 25.217 ff.), has no substantial support.
Rum. ostrov (formerly the usual word, but now displaced by insula, except lo- cally), fr. Slavic, ChSI. ostrovi, etc. (be- low, 6).
3. Ir. inis (NIr. mostly in place names), Gael. innis, W. ynys, Br. enez, fr. a Celtic *inissi, this perh. (Strachan, quoted by Machain s.v. innis) fr. *eni- ae eee in’ (the wate
r), fr. *sta- stand’, like other cpds. in -s{o- -sti- (Walde-P. 2.604). Pie Teoma agg sa rest Bidrag 120). y Marstrander, _ 4. ON ey, eyland, Dan. ¢, Sw. 6, OF %, gland, ME ilan
d, NE island (with Spelling influenced by isle), Du. eiland also MHG oune ‘water, island’ (NHG
aue ‘meadow’), fr. a fem. deriv. (in part + land) of the word seen in Goth. ahwa ‘river’, OE éa ‘water, river’, Lat. aqua ‘water’, etc. Walde-P. 1.34. Simi- larly 
OE éaland directly fr. éa.
ME, NE isle, fr. OF r. isle; OHG Zsila fr. Lat. trsula in its spoken form, MHG, NHG insel with restored n.
5. Lith., Lett. sala : Lith. salti ‘flow’, atsala ‘pool of stagnant water’, etc. Perh. for *apz-sala, like Lett. sawle for pasaule ‘world’ in certain phrases, and so �
�flowed around’ like ChSl. ostrovit. So Mihl.-Endz. 3.664.
6. ChSI. otoku (cf. Jagié, Entstehungs- gesch. 374), SCr. otok, fr. *obu-tokt, epd. of obi ‘around’ and the root of festz, teka, Lith. tektt ‘flow, run’, etc. Walde-P. - 
1.715 ff. Miklosich 347 f.
ChSl. ostrovit, etc., general Slavic, fr. *obi-strovt, cpd. of ob% ‘around’ and the root of struja ‘stream’, Grk. pew ‘flow’, etc. Walde-P. 2.703. Miklosich 318. Briick
ner 385.
Pol. wyspa (which has displaced the older ostréw except in place names) = Boh. vyspa ‘sandbank, small island’, fr. vy- ‘out’ and the root of ChSl. stipa, suti, iter. sypat
======= water =======
1.31 WATER
Grk.  bdwp Goth. wats Lith. vanduo NG vepd ON vain Lett. adens Lat. aqua Dan. vand ChSl.  voda It. acqua Sw. vatten SCr.  voda Fr. eau OE weler Boh.  voda Sp. agua ME water Pol. _v
oda am apd aa water Russ. voda
usce u water Skt. jala-, Gp-, udan- put ae cee wazzar ; Abie ate :
B wfr HG ee lee
Br. dour NEG - carer ge ee
C-0. In Public Domain. Gurukul Kangri Collection, Haridwar
: e
| Digitized by Arya Samaj Foundation Chennai and eGangotri _ | \
oO
—_S ~~ Biotized by Arya Samaj Foundation Chennai and eGangotri
THE PHYSICAL WORLD IN ITS LARGER ASPECTS 35
The words for ‘water’, with few ex- belong to certain widespread nates, one of these reflect- ing what was clearly the general IE word for ‘water’, and three others also re
flecting I words for ‘water’ , but per- haps in some more special application, such as ‘running water’ or ‘rain water’. Many words belonging to these groups appear in o
ther lists, as under ‘sea’, “vave’, ‘river’, ‘rain’.
1. IE *wedor, *wodor, *uden-, a typi- cal r/n stem neuter, with gradation of the root syllable, fr. root *wed- in Skt. ud- ‘wet, flow’. Some forms with nasal in root syllable (
intrusion from verb forms with nasal infix, or anticipation of n of stem). Walde-P. 1.252 ff. Er- nout-M. 1124.
Grk. téwp; Umbr. utur (Lat. unda ‘wave’); Ir. usce, NIr. uisce (Gael. wesge- beatha ‘water of life’ > NE whiskey); the Gme. group, Goth. waté, OF weter, etc.; Lith. vandu
o, Lett. uidens, OPruss. wundan, unds; ChSl. voda, ete. general Slavic; Skt. wdan-; Hitt. watar, gen. we- tenas; Alb. wé.
2. IE *akva- or *akwa-. Walde-P. 1.34f. Ernout-M. 64. Walde-H. 1.60. Feist 18 f. Lat. aqua with its Romance derivatives. Elsewhere mostly of ‘run- ning water’ in words for ‘r
== LEW size/sanity ==
eae hee ne
ee
Duquesne University:
joe Kt re |
* ee . ¥
c
'DOGERMANISCHE BIBLIOTHEK
-ZWEITE REIHE: WORTERBUCHER
____ Digitized by the Internet Archive in 2023 with funding from No Sponsor — re
mi https://archive.org/details/lateinischesetymO ) any * ; - % MANY ioe hie vel
AN
~ LATEINISCHES
```


## [2026-09-04T19:28:14.712Z] AGENT

Now let me write the verification file.


## [2026-09-04T19:33:37.821Z] TOOL CALL #91: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/write44.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_ASK   = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B4%DA%A9\"\nW_ARS   = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%B3\"\nW_DAKRU = \"https://en.wiktionary.org/wiki/Reconstruction%3AProto-Indo-European/d%C3%A1%E1%B8%B1ru\"\nE_TEAR  = \"https://www.etymonline.com/word/tear\"\nW_ALEH  = \"https://en.wiktionary.org/wiki/%D8%A2%D9%84%D9%87\"\nW_AKWA  = \"https://en.wiktionary.org/wiki/Reconstruction%3AProto-Indo-European/h%E2%82%82ek%CA%B7eh%E2%82%82\"\nE_EAGLE = \"https://www.etymonline.com/word/eagle\"\nE_ISL   = \"https://www.etymonline.com/word/island\"\nE_AQU   = \"https://www.etymonline.com/word/aquarium\"\nW_ODK   = \"https://en.wiktionary.org/wiki/%D8%A7%D8%AF%DA%A9%D9%84%D9%86\"\n\ndoc = {\n \"pdf_page\": 44,\n \"book_page\": 14,\n \"verified_by\": \"claude-fable-5-1\",\n \"verified_on\": \"2026-09-04\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Akru, Dakru\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *h₂éḱru 'tear' (Indo-Iranian/Baltic/Tocharian) beside PIE *dáḱru 'tear' (Greek, Italic, Celtic, Germanic, Armenian)\",\n   \"note\": \"Both reconstructions are real and both glosses are right, but Pokorny prints them as TWO separate lemmas — 'akru ‚Träne‘' on p.23 and 'dakrú n. ‚Träne‘' on p.179 — and says explicitly of the pair: 'Das Verhältnis zu idg. *dakru ‚Träne‘ ist ungeklärt' (POK_01.txt \\\\f-page 31, printed p.23) and, under dakru, 'Andrerseits sucht man Vermittlung mit ai. áśru ... wohl bloßes Reimwort ... s. oben S. 23 unter akru' (\\\\f-page 187 area, printed p.179). Nourai's single box 'Akru, Dakru' therefore states as settled what Pokorny leaves open. He is not alone: Buck 16.38 lists 'IE *dakru-, also *draku- and *aḱru-, relations variously explained', and Aryanpur (ARY, printed p.90) puts Av. asrū-, Skt. áśru, Gk. dákru, Lat. lacrima and Eng. tear in one family. Modern Wiktionary keeps the two apart and calls the link 'uncertain', citing Dunkel's *d (zero grade of *ád) prefixed to *h₂éḱru, or a compound *dr̥ḱ-h₂éḱru 'eye-bitter'. Verdict 'plausible' rather than 'confirmed' only because of the merge; every individual word in the chart belongs to one branch or the other. Note also that the two halves of the chart are consistent: the Iranian/Persian branch hangs off *akru, the Germanic/English branch off *dakru.\",\n   \"ref_check\": [\n    {\"ref\": \"POK:23\", \"status\": \"supports\", \"note\": \"POK_01.txt \\\\f-page 31 (printed p.23): 'akru ‚Träne‘. Ved. ásru n., später auch ásram ‚Träne‘, av. asru- n., lit. asarà und ásara f., toch. A ākär Pl. ākrunt ds. ... Das Verhältnis zu idg. *dakru ‚Träne‘ ist ungeklärt. WP. I 33.' Exactly the root Nourai gives, with the caveat he omits.\"},\n    {\"ref\": \"POK:179\", \"status\": \"supports\", \"note\": \"POK_01.txt, printed p.179: 'dakrú n. ‚Träne‘. Gr. dákru, dákruon ...; daraus entlehnt altlat. dacruma, lat. lacruma, lacrima ...; germ. *tāhr- und tagr-: got. tagr n. ‚Träne‘, anord. tár ..., ags. tæhher, tear, teagor m., ahd. zahar. WP. I 769.' Supports the 'Dakru' half of the box and the Germanic branch.\"}\n   ],\n   \"sources\": [W_DAKRU, E_TEAR],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"asrŭ, asraka\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Avestan asrū- n. 'tear' is genuine and well attested — Bartholomae, AiW s.v. (BRT.txt line 5925): \\\"'asrū- n. 'Träne'; ai. āśrav-, np. ars\\\" — and appears in the compound asrū.azan- 'shedding tears' (Yt. 10.38). It continues Proto-Iranian *Hácru < PIE *h₂éḱru, with Indo-Iranian *ć > Iranian s before the following r. The SECOND form, 'asraka', is not an attested Avestan word: it is Horn's starred reconstruction, coined to explain NP ašk — Horn, Grundriss no. 88 (HRN.txt printed p.21): 'ešk ‚Thräne‘ ... aw. *asraka (vergl. skr. áśra-), *arsaka (Horn, Indog. Forsch. II, 136).' Hübschmann rejects it (see node #3). So the node is right for asrū-, over-stated for asraka.\",\n     \"ref_check\": [\n      {\"ref\": \"POK:23\", \"status\": \"supports\", \"note\": \"POK_01.txt printed p.23 under 'akru': 'av. asru- n.' — the Avestan form and its attachment to the root are Pokorny's own.\"},\n      {\"ref\": \"KLN:1578\", \"status\": \"supports\", \"note\": \"Klein s.v. 'tear, n., drop of liquid from the eye' (KLN_1966.txt line 38345): '... fr. I.-E. *dakru- ‚tear‘ ... cp. — without the initial dental sound — OI. ásru, Avestic asru, Toch. A akar, Lith. asara, Lett. asara.' Content is exactly Nourai's claim. Caveat: in the archive.org scan of the 1966-67 two-volume edition this entry sits on \\\\f-leaf 836 ≈ printed p.1648, not p.1578; the leaf→page formula for that scan drifts upward (aquiline +6, eagle +21, tear +71), so Nourai's number is probably the book's and the scan's is the drifting one.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW s.v. asrū- (BRT.txt line 5925; Mo'in cites the column as 222)\", \"stance\": \"supports\", \"note\": \"\\\"'asrū- n. 'Träne'; ai. āśrav-, np. ars\\\" — Bartholomae himself draws the Av. asrū- → NP ars line; no 'asraka' is listed.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 69, printed p.17 and no. 88, p.21\", \"stance\": \"partial\", \"note\": \"no. 69 'ers ‚Thräne‘ ... aw. asru- ‚Thräne‘; phlv. ars; ai. áśru-; lit. aszarà'; but 'asraka' appears only as Horn's starred *asraka at no. 88.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. aKərā, aKru\", \"stance\": \"supports\", \"note\": \"'aKərā, aKru ‚teardrop‘. Cf. dakru. WP I, 769. Skt. ásru; Av. asru; Per. ašk; Tokh. A ākär ...' — Mann puts Av. asru and NP ašk under the same reconstruction.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 16.38 TEAR (sb.)\", \"stance\": \"supports\", \"note\": \"'Skt. açru-, Av. asru- (in asrū-azan- ‚shedding tears‘), Toch. akar' listed under 'IE *dakru-, also *draku- and *aḱru-'.\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 33 (WLD_Bd1 line 2331)\", \"stance\": \"supports\", \"note\": \"'akru ‚Träne‘. Ved. açru ... av. aṣru n. ‚Träne‘; lit. ašara f. ... Besteht eine Beziehung zu *dakru? Heringer ... nimmt ein Präfix d- an.'\"}\n     ],\n     \"sources\": [W_ASK]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"ars\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian ars 'tear', written <ʾLS> in Book Pahlavi and <ʾrs> in Manichaean script, is the regular reflex of Old Iranian *asru-: the Iranian cluster -sr- metathesises to -rs- in Middle/New Persian (Hübschmann, Pers. Stud. p.171/p.220: 'ap. sr = np. rs: ars ‚Thräne‘ = zd. asru-'), and the final -u of the u-stem is lost. It is attested in the Bundahišn (Mo'in cites Bd. 90) and in the texts glossed by Nyberg (93¹⁷).\",\n     \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; checked independently against MacKenzie and Nyberg (see 'consulted').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. ars (PHD_mackenzie.txt line 1183)\", \"stance\": \"supports\", \"note\": \"\\\"ars ['ls | M 'rs, N ~] tear (drop).\\\" — the Book-Pahlavi spelling, the Manichaean spelling, and 'N ~' meaning the New Persian form is identical.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary) s.v. ars\", \"stance\": \"supports\", \"note\": \"\\\"ars ['ls] tear 93¹⁷. — MPrs 'rs (Sogd. 273¹); NP ars.\\\"\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien, sound-change lists (HUB.txt lines 7574, 9544)\", \"stance\": \"supports\", \"note\": \"'sr in rs: ars ‚Thrane‘ = zd. asru-' and 'Ap. sr = np. rs: ars ‚Thrane‘ = zd. asru-' — the exact phonetic rule that turns *asru into ars.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in vol.1 p.103, Mo'in's footnote 4\", \"stance\": \"supports\", \"note\": \"«اوستا asrû, asrav (اشك) «بارتولمه ۲۲۲»، پهلوی ars، «بندهش ۹۰»» — Mo'in gives precisely Av. asrū > Pahl. ars.\"}\n     ],\n     \"sources\": [W_ARS]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"ars «ارس»; ašk «اشک»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"NP ars «ارس» (now archaic/poetic) is the direct continuation of MP ars, itself < Av. asrū- < PIr *Hácru < PIE *h₂éḱru; Borhan-e Qate' p.103 defines it «و بفتح اول و سکون ثانی، اشک چشم را گویند» ('with a on the first and sukun on the second it means the tear of the eye'). The ordinary modern word ašk «اشک» is a DOUBLET, not a straight descendant of ars: it goes back to a k-suffixed *Hácru-ka- (Khotanese āṣka-, Wakhi yašk point the same way) and may have entered Persian from Parthian ʾšk /ašk/ rather than developing inside the south-western dialect, where *-sr- gave -rs-. Horn (no. 88) derived it from a reconstructed Av. *asraka; Hübschmann §88 explicitly objects: 'Da zd. asru- = skr. áśru- im Np. als ars (aus *asr) vorliegt, ist es nicht wahrscheinlich, dass ein zd. *asraka-, dem lautgesetzlich np. *asra entspräche, durch np. ašk vertreten wird', proposing instead as-k beside ars on the model of xʷas beside xusrū 'mother-in-law'. So the arrow Pahlavi ars → NP ašk is too simple, though both words are certainly from the same root.\",\n     \"ref_check\": [\n      {\"ref\": \"BQT:103\", \"status\": \"supports\", \"note\": \"Read from the page image (archive.org borhan-ghate-v1 leaf n315; running head '— ۱۰۳ —'), transcription saved to data/verification/sources/refs/ocr/BQT/103.vision.txt. Entry: «ارس ... و بفتح اول و سکون ثانی، اشک چشم را گویند»; Mo'in's footnote 4: «اوستا asrû, asrav (اشك) «بارتولمه ۲۲۲»، پهلوی ars، «بندهش ۹۰»، طبری asli، مازندرانی کنونی ari و hasri». The page number, the words, both glosses and the Avestan→Pahlavi→Persian chain are all exactly as Nourai has them.\"},\n      {\"ref\": \"HRN:17\", \"status\": \"supports\", \"note\": \"HRN.txt \\\\f-leaf 38 = printed p.17, entry no. 69: 'ers ‚Thräne‘. mäz. asr; Käs. asl, aw. asru- ‚Thräne‘; phlv. ars; ai. áśru-; lit. aszarà ... Die indog. Urform war nach Bugge *dakru-, da auch gr. dákru, acymr. dacr, air. dér, lat. lacruma, got. tagr, ahd. zahar dazu gehören sollen. Mindestens ist eine Dialektspaltung anzunehmen; vielleicht liegen aber zwei ursprünglich ganz verschiedene Worte vor.' Overleaf (p.18): 'Hierher gehört auch np. ešk ‚Thräne‘ (No. 88).' Horn supports both Persian words AND, incidentally, states the akru/dakru question Nourai's root box glosses over.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HUB\", \"where\": \"Persische Studien §88 (HUB.txt line 411)\", \"stance\": \"contradicts\", \"note\": \"'Da zd. asru- = skr. áśru- im Np. als ars (aus *asr) vorliegt, ist es nicht wahrscheinlich, dass ein zd. *asraka- ... durch np. ašk vertreten wird' — rejects the Avestan *asraka > ašk route drawn in the chart.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. aKərā, aKru\", \"stance\": \"supports\", \"note\": \"lists 'Per. ašk' directly under the *aKru reconstruction.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt pdf page 89 = printed p.90, entry اشک، ارس، سرشک\", \"stance\": \"supports\", \"note\": \"Aryanpur's family list for اشک/ارس runs Avestan ASRŪ- / Pahlavi ARS / Sanskrit AŚRU, AŚRAM / Greek DAKRU / Latin LACRIMA, DACRIMA / OE TEAR / NE TEAR — the same merged akru+dakru family as Nourai's box.\"},\n      {\"src\": \"MON\", \"where\": \"vajehyab/Mo'in (not reachable offline); local MON_part1/2 have no اشک headword page\", \"stance\": \"silent\", \"note\": \"the two-volume Adena text of Mo'in on disk does not carry the اشک entry with its bracketed origin tag; Mo'in's etymology is however quoted verbatim in his BQT footnote above.\"}\n     ],\n     \"sources\": [W_ASK, W_ARS]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Germanic\",\n     \"words\": \"tahr\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *tahrą (beside *tagrą) 'tear' is the regular Germanic outcome of PIE *dáḱru: Grimm's law turns *d- into *t- and the palatal *ḱ into *h (before the *-r- also *g by Verner/analogy), whence Gothic tagr, Old Norse tár, OHG zahar (NHG Zähre), OE tēar/teagor. Nourai's 'tahr' is Watkins's *tahr- exactly.\",\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 358: 'dakru-. Tear. 1. Germanic *tahr-, *tagr- in: a. Old English téar, tehher, tear: TEAR²; b. Middle Low German tran ...; 2. Suffixed form *dakru-ma in Latin lacrima (Old Latin dacruma). [Pok. dakru- 179.]' — verbatim Nourai's node, and it is also the source of his 'POK:179'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"printed p.179 s.v. dakrú\", \"stance\": \"supports\", \"note\": \"'germ. *tāhr- und tagr-: got. tagr n. ‚Träne‘, anord. tár n. (aus *tahr-), ags. tæhher, tear, teagor m., ahd. zahar m.'\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 769 (WLD_Bd1 line 48475 ff.)\", \"stance\": \"supports\", \"note\": \"same Germanic set under 'dakru n. ‚Träne‘'; adds 'Idg. *dakru ist wahrscheinlich aus *drakru dissimiliert'.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. tear, n.\", \"stance\": \"supports\", \"note\": \"'OE. tear, contraction of teagor, rel. to ON., OFris. tar, OHG. zah(h)ar, MHG. zaher, G. Zähre, Goth. tagr, ‚tear‘, fr. I.-E. *dakru-'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 16.38\", \"stance\": \"supports\", \"note\": \"'ON tár, OE téar, OHG zahar, etc. ... with gramm. change Goth. tagr, OE teagor'.\"}\n     ],\n     \"sources\": [E_TEAR, W_DAKRU]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"tear 1\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"OE tēar (a contraction of the older teagor, itself < PGmc *tagrą) > ME tere, ter > NE tear (the noun, 'tear 1' as against the homograph 'tear 2' = to rend, from an unrelated PIE *der- 'flay'). No borrowing is involved; the word is inherited straight down the Germanic line from *tahr-/*tagr-.\",\n     \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; checked against Klein, Skeat, Buck and Etymonline (see 'consulted').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. tear, n. and tear, tr. and intr. v.\", \"stance\": \"supports\", \"note\": \"Klein separates exactly the two homographs Nourai's 'tear 1' presupposes: 'tear, n., drop of liquid from the eye. — ME. tere, ter, tear, fr. OE. tear, contraction of teagor' vs 'tear, tr. and intr. v., to put apart, rend ... fr. I.-E. *dere-'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 16.38\", \"stance\": \"supports\", \"note\": \"'OE téar, teagor / ME tere / NE tear' in the descent column.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. train-oil (SKT.txt line 19257-59)\", \"stance\": \"supports\", \"note\": \"'Mod. Du. traan, a tear, G. trähne ... is allied to Dan. taar, a tear, and to E. tear' — same Germanic family.\"},\n      {\"src\": \"web\", \"where\": \"etymonline s.v. tear (n.1)\", \"stance\": \"supports\", \"note\": \"'from Old English tear ... from Proto-Germanic *tahr-, *tagr-, from PIE root *dakru-'.\"}\n     ],\n     \"sources\": [E_TEAR]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Akwa\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₂ékʷeh₂ '(flowing) water' (Pokorny's akʷā-, 'richtiger okʷā-': ekʷ-)\",\n   \"note\": \"The root box is right; the trouble on this page is the EAGLE branch. Nourai hangs Av. 'arva' → Pahl. āluh → NP āleh, and Lat. 'aqualius' → Fr. aigle → Eng. eagle, on *akʷā- 'water'. Two independent problems: (a) 'arva' is not Avestan at all — it is the Pāzand/Middle-Persian form arvā of Bundahišn 14:23, which Mo'in cites in his own footnote at BQT p.58 and which Horn no. 43 quotes as 'arvā (Bund.) in Zendbuchstaben'; Bartholomae's AiW has no such word, Avestan for 'eagle' being ərəzifya- or saēna-. Nyberg derives Pahl. āluh from OP *ardūfya- < *ardifya- = Av. ərəzifya-, and Wiktionary from PIr *Hr̥jifyáh < PIE *h₂rǵ-i-pt-ió-s 'white/swift-flying' — i.e. the Iranian eagle-word has nothing to do with 'water'. (b) The Latin word is not 'aqualius' (no such Latin form exists); it is aquila 'eagle', fem. of aquilus 'dark-coloured'. The step aquilus < aqua is a Roman folk etymology reported by Festus ('aquilus autem color est ab aqua nominatus') and is rejected by Ernout-Meillet, LAT s.v. aquilus: 'L'explication par aqua rend mal compte du sens de l'adjectif; on ne voit pas pourquoi l'eau aurait été prise pour désigner une couleur tirant sur le noir'; de Vaan and Etymonline likewise call it uncertain. Pokorny p.23 does report it ('davon aquilus ‚dunkel‘, aquila ‚Adler‘, eigentl. ‚der Dunkelfarbige‘'), which is presumably where Nourai took it from, so the branch is old-fashioned rather than invented. Aryanpur (ARY p.68) records the same split: 'PARTRIDGE holds this word may be cognate with Latin AQUA (water)', while 'ONIONS and SKEAT go back only to the Latin root AQUILA' and Pokorny takes the Iranian, Armenian and Greek words from *er-/*or- 'eagle, large bird'. The water branches proper (Latin aqua, French eau/eau de Cologne, English aquarium/aquatic, Germanic *ahwjō → island) are all sound.\",\n   \"ref_check\": [\n    {\"ref\": \"POK:23\", \"status\": \"supports\", \"note\": \"POK_01.txt \\\\f-page 31 (printed p.23): 'akʷā- (richtiger okʷā-): ekʷ- ‚Wasser, Fluß‘. Lat. aqua ‚Wasser, Wasserleitung‘ (davon aquilus ‚dunkel‘, aquila ‚Adler‘, eigentl. ‚der Dunkelfarbige‘, aquilō ‚Nordwind‘) = got. aƕa f. ‚Fluß, Gewässer‘, aisl. á, ags. ēa, as. ahd. aha ... (germ. *ahwō, davon abgeleitet *ahwjō, *awjō ‚die vom Wasser Umgebene‘ in aisl. ey f. ‚Insel, Aue‘, ags. īeg, ahd. -ouwa ...), vgl. afries. ei-land ‚Insel‘.' This one page underwrites the root, the Latin node, the eagle claim AND the Germanic 'island' node.\"}\n   ],\n   \"sources\": [W_AKWA],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Latin\",\n     \"words\": \"aqua\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin aqua 'water' is the standard Italic reflex of PIE *h₂ékʷeh₂, cognate with Gothic aƕa 'river', OE ēa, OHG aha, and (probably) the Lusitanian river-word aqua. The root is 'suspiciously limited to a few western Indo-European branches' (Wiktionary), and Ernout-Meillet stress that it named water as an active, divine being rather than water as a substance (that is *wódr̥, Lat. unda).\",\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 277: 'akwa-. Water. 1. Germanic *agwjō becoming *aujō, ‚thing on the water‘, in Old English ig, ieg, island ...' — Watkins's root entry, headed by Latin aqua.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"printed p.23 s.v. akʷā-\", \"stance\": \"supports\", \"note\": \"'Lat. aqua ‚Wasser, Wasserleitung‘ ... = got. aƕa f. ‚Fluß, Gewässer‘.'\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 34 (WLD_Bd1 line 2387)\", \"stance\": \"supports\", \"note\": \"'aqʷā ‚Wasser, Fluß‘. Lat. aqua ‚Wasser‘, got. aha ‚Fluß, Gewässer‘, aisl. ǿ, ae. ēa, afries. ā, e, as. ahd. aha f. ‚Fluß‘, nhd. Ache, russ. Fl.-Name Oka.'\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. aqua (LAT.txt line 4590 ff.)\", \"stance\": \"supports\", \"note\": \"'aqua a son correspondant exact en germanique: got. ahwa ... Le germanique offre d'autre part un dérivé attesté par v.h.a. ouwo (all. mod. Au) ‚prairie marécageuse, île‘, et le nom propre Scandin-auia.'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 1.31 WATER\", \"stance\": \"supports\", \"note\": \"'2. IE *akva- or *akwa-. Walde-P. 1.34 f. ... Lat. aqua with its Romance derivatives. Elsewhere mostly of ‚running water‘.'\"},\n      {\"src\": \"LEW\", \"where\": \"LEW_1910.txt\", \"stance\": \"silent\", \"note\": \"the local OCR of Walde's Lateinisches etymologisches Wörterbuch (1910) is unusable — a grep for 'aqua' and 'aquila' returns nothing at all; used LAT (Ernout-Meillet) instead.\"}\n     ],\n     \"sources\": [W_AKWA]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Avestan\",\n     \"words\": \"arva, arvâ\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Two things go wrong here. (i) The language label: arvā is not Avestan. It is a Pāzand form written in Avestan characters in the Middle-Persian Bundahišn — Horn no. 43 (HRN.txt printed p.10): 'āluh ‚Adler‘. phlv. āluh (Kārn. 59, Note 2), vergl. arvā (Bund.) in Zendbuchstaben'; Mo'in says the same at BQT p.58: «و نیز در بندهش (۱۴:۲۳) arvâ بمعنی عقاب آمده». Bartholomae's Altiranisches Wörterbuch has no arva-; the real Avestan words for 'eagle' are ərəzifya- (col. 354) and saēna-. (ii) The edge: as drawn the node descends from Latin aqua, which is impossible in both direction and family — an Iranian word cannot come out of Latin, and even as a shorthand for 'same root as' the connection fails, since Pahl. āluh/arvā goes back to PIr *Hr̥jifyáh < PIE *h₂rǵ-i-pt-ió-s (from *h₂erǵ- 'white, glittering', cf. Skt. r̥jipyá-, Gk. αἰγυπιός), not to *h₂ékʷeh₂ 'water'. Nourai's own NOTE concedes that his source VFO 'does not provide any derivation'.\",\n     \"ref_check\": [\n      {\"ref\": \"VFO:15\", \"status\": \"not_checked\", \"note\": \"VFO = M. Ahmad Soltani, Vaj̱hgan-e Farsi dar Zabanha-ye Orupa'i, Tehran 1372/1993. refs_online.json has no record for VFO at all (value null) and no scan or copy exists in the local library or online; unverifiable. Nourai's own chart note already flags that VFO asserts the cognacy without any derivation.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, searched for arva-/aurva-/'Adler'\", \"stance\": \"contradicts\", \"note\": \"no headword arva- 'eagle' exists; Bartholomae's eagle-words are 'ərəzi-fya- m. ‚Adler‘' (BRT.txt line 7718) and 'saēna- m. Name eines grossen Raubvogels, wohl des Adlers' (line 25786).\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss no. 43, printed p.10\", \"stance\": \"partial\", \"note\": \"gives the form ('vergl. arvā (Bund.) in Zendbuchstaben') but labels it Bundahišn, i.e. Middle Persian in Avestan script, and connects āluh not with aqua but with 'gr. ὄρνις ‚Vogel‘; ksl. orĭlŭ ‚Adler‘; lit. erelis; got. ara; cymr. eryr'.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.1 p.58, Mo'in's footnote 6\", \"stance\": \"partial\", \"note\": \"confirms the word and its source text — «در کارنامهٔ اردشیر بابکان (۱۴ : ۱۲) āluh بمعنی عقاب بکار رفته است و نیز در بندهش (۱۴ : ۲۳) arvâ بمعنی عقاب آمده» — but places it in a Pahlavi text, not in the Avesta, and offers no link to 'water'.\"},\n      {\"src\": \"web\", \"where\": \"Wiktionary s.v. Persian آله\", \"stance\": \"contradicts\", \"note\": \"MP āluh < Proto-Iranian *Hr̥jifyáh < PII *Hr̥ǳipyás < PIE *h₂rǵ-i-pt-ió-s (: *h₂erǵ- 'white, glittering'), cognate Avestan ərəzifiia, Old Armenian arcui — no relation to *h₂ekʷeh₂.\"}\n     ],\n     \"sources\": [W_ALEH]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"alŭh\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The word itself is impeccable: Middle Persian āluh <ʾlwh>, Manichaean <ʾlwf>, 'eagle', attested in the Kārnāmag ī Ardašīr ī Pābagān 14:12 and in the Bundahišn (as Pāzand arvā). What is wrong is the parentage. Nyberg derives it 'MPrs ʾawf (List 79); NP āluh, < OP *ardūfya- < *ardifya-, Av. ərəzifya-' — that is, from Old Iranian *r̥difya- 'eagle' with the regular Middle Persian development *rd > l and loss of the palatal glide, giving āluh; Wiktionary's PIr *Hr̥jifyáh is the same reconstruction. Descent from Latin aqua via an 'Avestan arva' (as the chart draws it) has no support anywhere; Hübschmann §43 says only 'die Bildung von phl. np. āluh ist dunkel'.\",\n     \"ref_check\": [\n      {\"ref\": \"BQT:58\", \"status\": \"supports\", \"note\": \"Read from the page image (archive.org borhan-ghate-v1 leaf n268; running head '— ۵۸ —'), transcription saved to data/verification/sources/refs/ocr/BQT/58.vision.txt. Mo'in, fn. 6: «در همهٔ فرهنگها آله بمعنی عقاب آمده ... در کارنامهٔ اردشیر بابکان (۱۴ : ۱۲) āluh بمعنی عقاب بکار رفته است». Supports the Pahlavi word and its gloss (not the parentage).\"},\n      {\"ref\": \"MPP:79\", \"status\": \"not_found\", \"note\": \"MPP = Henning, 'Mitteliranisch' (HdO I.4.1, 1958). MPP.txt \\\\f-leaf 65, which carries the printed page number '79' at the head, is §29-30 on the Sogdian-Syriac script and the oldest Judeo-Persian documents — nothing about āluh or eagles. The citation is probably meant for Henning's other work, the 'List of Middle-Persian and Parthian words' (Nourai's LST), since Nyberg's āluh entry cites exactly 'MPrs ʾawf (List 79)'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. āluh (PHD.txt line 189; English index line 1720)\", \"stance\": \"supports\", \"note\": \"'Āluh [ʾlwh | M ʾlf, N ~] eagle'; the index reads 'eagle āluh, dalman, humāy'. Word and gloss confirmed.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. aluh\", \"stance\": \"contradicts\", \"note\": \"'aluh [ʾlwh] eagle ... — MPrs ʾawf (List 79); NP āluh, < OP *ardūfya- < *ardifya-, Av. (354) arəzifya-.' A completely different etymology from Nourai's water-root.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien §43 (HUB.txt line 164)\", \"stance\": \"partial\", \"note\": \"'Zu āluh ‚Adler‘ vgl. die kurd. Formen hālā etc. ... Die Bildung von phl. np. aluh ist dunkel, die Zugehörigkeit zu ὄρνις u.s.w. daher nicht sicher.' Sceptical of Horn's bird-root too, but never entertains 'water'.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt pdf page 67 = printed p.68, entry آله، آلوه، الوه\", \"stance\": \"partial\", \"note\": \"lists Avestan ərəzifya-, Old Persian *ard(u)fya-, Pahlavi ĀLUH, Armenian ARCUI, Latin AQUILA, French AIGLE and cites 'برهان قاطع ۵۸' (the same BQT page Nourai cites); footnote 3 records 'PARTRIDGE holds this word may be cognate with the Latin word AQUILA/AQUA (water)' as one scholar's opinion, while footnote 4 has Pokorny take the Iranian, Armenian and Greek forms from *er-/*or- instead.\"}\n     ],\n     \"sources\": [W_ALEH]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Persian\",\n     \"words\": \"âleh «آله ( لِه ، آلغ ، آلوه ، آل )»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The edge Pahlavi āluh → New Persian āleh/āloh is correct and regular: MP āluh loses the final -h in pronunciation and the -u- is lowered, giving āleh, with the by-forms leh (aphaeresis of the initial ā-), āloš/āloh, ālɣ (Gilaki) and āl. Borhan-e Qate' p.58 defines it «مرغی ... که بر کوههای بلند آشیانه کند ... و بتازی عقاب گویند» and cites the very verse of Farqadī that Nourai reproduces. The word is now rare, عقاب and دال having replaced it. Only the ultimate ancestry drawn upstream (Latin aqua) is wrong — see nodes #2 and #3.\",\n     \"ref_check\": [\n      {\"ref\": \"MON:85\", \"status\": \"partial\", \"note\": \"Mo'in's Farhang-e Farsi does carry the word: MON_part1.txt line 97099, under عقاب, glosses 'آله، آلغ. عقاب آهنین منقار', and MON_part2.txt line 41218 has 'له: [= آله = آلوه = اله] (جان.) عقاب', MON_part1.txt line 16467 'اله: [= آله] عقاب، آله'. Nourai's four by-forms له / آلغ / آلوه / آل are exactly Mo'in's. The local two-volume Adena text of Mo'in carries no page markers, so the specific page 85 could not be confirmed.\"},\n      {\"ref\": \"BQT:58\", \"status\": \"supports\", \"note\": \"Page image read directly (see data/verification/sources/refs/ocr/BQT/58.vision.txt): the entry and Mo'in's footnote 6 give آله = عقاب, the dialect forms 'هلو' (Kurdish), 'اله' (Mazandarani), 'آلغ' (Gilaki), Tabari alleh, modern Mazandarani allē/alē — and the Farqadī couplet «مثل دشمنان تو با تو / حیلهٔ کبک و حمله های له است», i.e. exactly the quotation printed in this chart node.\"},\n      {\"ref\": \"VFO:15\", \"status\": \"not_checked\", \"note\": \"no copy of Ahmad Soltani's Vaj̱hgan-e Farsi dar Zabanha-ye Orupa'i exists in the local library or online (refs_online.json record is null).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"MON_part1 line 97099 (s.v. عقاب) and MON_part2 line 41218 (s.v. له)\", \"stance\": \"supports\", \"note\": \"'له: [= آله = آلوه = اله] (جان.) عقاب.' — Mo'in's chain of by-forms matches Nourai's parenthesis exactly.\"},\n      {\"src\": \"BQT\", \"where\": \"vol.1 p.58\", \"stance\": \"supports\", \"note\": \"see ref_check above; the definition, the dialect forms and the Farqadī verse.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss no. 43, printed p.10\", \"stance\": \"supports\", \"note\": \"'āluh ‚Adler‘. phlv. āluh (Kārn. 59, Note 2)' — Horn lemmatises the New Persian word and derives it from the Pahlavi one, exactly this edge.\"},\n      {\"src\": \"web\", \"where\": \"Wiktionary s.v. آله (Etymology 1)\", \"stance\": \"supports\", \"note\": \"'آله (āloh) eagle (rare) — from Middle Persian āluh'; cognates Gilaki aluɣ, Mazandarani alle, N. Kurdish eylo/êlo, Bakhtiari ālō.\"}\n     ],\n     \"sources\": [W_ALEH]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Latin\",\n     \"words\": \"aqualius\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"There is no Latin word 'aqualius'. What Nourai means — his own gloss 'water (dark) colored bird, eagle' is a paraphrase of Klein's wording — is aquila 'eagle', explained by the Romans as the feminine of aquilus 'dark-coloured', itself supposedly 'water-coloured' from aqua. Klein (KLN:97, s.v. aquiline) states it in just those terms: 'L. aquilinus ... fr. aquila, ‚eagle‘, prob. lit. ‚the dark-colored (bird)‘, fem. of aquilus, ‚dark-colored‘, prop. ‚water-colored‘, fr. aqua, ‚water‘'; Funk & Wagnalls (FSD:779) has '< F. aigle, < L. aquila, orig. f. of aquilus, dark-colored'. But the aqua-etymology goes back to Festus ('aquilus autem color est ab aqua nominatus') and modern Latinists reject it: Ernout-Meillet, s.v. aquilus, 'L'explication par aqua rend mal compte du sens de l'adjectif; on ne voit pas pourquoi l'eau aurait été prise pour désigner une couleur tirant sur le noir', and s.v. aquila, 'le nom de l'aigle ... varie d'une langue indo-européenne à l'autre et résulte partout d'arrangements relativement récents'. De Vaan reverses the direction (aquilus 'dark' may itself be from aquila). Disputed both for the impossible form and for the aqua > aquilus step.\",\n     \"ref_check\": [\n      {\"ref\": \"KLN:97\", \"status\": \"supports\", \"note\": \"Klein s.v. aquiline (KLN_1966.txt line 3269, \\\\f-leaf 63): 'L. aquilinus ... fr. aquila, ‚eagle‘, prob. lit. ‚the dark-colored (bird)‘, fem. of aquilus, ‚dark-colored‘, prop. ‚water-colored‘, fr. aqua, ‚water‘. See aquatic ... and cp. eagle.' Note that Klein's form is aquilus/aquila, never 'aqualius'.\"},\n      {\"ref\": \"KLN:494\", \"status\": \"supports\", \"note\": \"Klein s.v. eagle (KLN_1966.txt line 12529, \\\\f-leaf 269): 'ME. egle, fr. OF. egle, aigle (F. aigle), fr. L. aquila, ‚eagle‘ ... See aquiline.'\"},\n      {\"ref\": \"WEB:569\", \"status\": \"supports\", \"note\": \"Webster's New Twentieth Century, 2nd ed., s.v. eagle (WEB_vol1.txt line ~60670, \\\\f-leaf 601, which maps to printed p.569): '[ME. egle; OFr. egle, aigle; ... L. aqui[la]]'. The 'Aquila / aquiline / Aquilo' cluster earlier in the volume adds 'L. aquilinus, from aquila'.\"},\n      {\"ref\": \"FSD:779\", \"status\": \"supports\", \"note\": \"Funk & Wagnalls New Standard, vol. II, s.v. eagle (FSD_vol2.txt line 4286, \\\\f-leaf 48 → printed p.779): '[ < F. aigle, < L. aquila, orig. f. of aquilus, dark-colored.]' — exactly Nourai's gloss, and the page number checks out.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. aquila and aquilus (LAT.txt lines 4608, 4633)\", \"stance\": \"contradicts\", \"note\": \"aquila: 'résulte partout d'arrangements relativement récents' (no root etymology); aquilus: 'Les anciens le rapprochent de aquila, et en font un dérivé de aqua (d'après nubilus, nubes); ainsi Festus ... L'explication par aqua rend mal compte du sens de l'adjectif.'\"},\n      {\"src\": \"POK\", \"where\": \"printed p.23 s.v. akʷā-\", \"stance\": \"supports\", \"note\": \"'Lat. aqua ... (davon aquilus ‚dunkel‘, aquila ‚Adler‘, eigentl. ‚der Dunkelfarbige‘, aquilō ‚Nordwind‘)' — Pokorny does place aquila under the water-root, which is presumably Nourai's warrant.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. aquiline and s.v. subaqueous (SKT.txt lines 850, 849)\", \"stance\": \"partial\", \"note\": \"'Aquiline, like an eagle. (F.-L.) F. aquilin ... L. aquilinus, adj. from aquila, an eagle' — Skeat stops at Latin aquila and does not connect it to aqua (Aryanpur's fn. 2 says the same of Skeat and Onions).\"},\n      {\"src\": \"web\", \"where\": \"etymonline s.v. eagle\", \"stance\": \"partial\", \"note\": \"'Some scholars propose it derives from aquilus, ‚the dark colored‘ bird ... The color word aquilus itself may trace back to Latin aqua, though this connection is disputed'; quotes de Vaan reversing the derivation.\"}\n     ],\n     \"sources\": [E_EAGLE]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"French\",\n     \"words\": \"aigle\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"French aigle 'eagle' does come from Latin aquila, but not by inherited descent — the regular Old French outcome of aquila would have been *aille; the attested OF egle/aigle is a borrowing (13th c.) of Old Occitan/Provençal aigla, which shows the southern treatment of intervocalic -qu- as -g-. Cf. It. aquila, Sp. águila, Port. águia, Rum. aceră, all from aquila. Klein's entry names the Provençal link.\",\n     \"ref_check\": [\n      {\"ref\": \"KLN:494\", \"status\": \"supports\", \"note\": \"Klein s.v. eagle: 'ME. egle, fr. OF. egle, aigle (F. aigle), fr. L. aquila, ‚eagle‘, whence also It. aquila, Rum. aceră, Provenç. aigla, Sp. aguila, Port. aguia, of s.m.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. II p.779 s.v. eagle\", \"stance\": \"supports\", \"note\": \"'[ < F. aigle, < L. aquila ]' — the same Latin > French > English chain.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's 2nd ed. p.569 s.v. eagle\", \"stance\": \"supports\", \"note\": \"'[ME. egle; OFr. egle, aigle; Pr. [aigla]; L. aqui[la]]'.\"},\n      {\"src\": \"web\", \"where\": \"etymonline s.v. eagle\", \"stance\": \"supports\", \"note\": \"'from Old French egle, from Old Provençal aigla, from Latin aquila' — explicitly the Occitan mediation.\"}\n     ],\n     \"sources\": [E_EAGLE]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"English\",\n     \"words\": \"eagle\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Borrowed in the mid-14th century from Old French egle/aigle, replacing the inherited native OE earn 'erne' (< PGmc *aran-, PIE *h₃er- 'large bird'). ME egle > NE eagle, with the modern -ea- spelling reflecting the ME long open ē. The word entered heraldic and then coin usage (the US ten-dollar 'eagle'); the golf sense is 1908.\",\n     \"ref_check\": [\n      {\"ref\": \"KLN:494\", \"status\": \"supports\", \"note\": \"Klein s.v. eagle: 'ME. egle, fr. OF. egle, aigle (F. aigle), fr. L. aquila.' — exactly the arrow drawn.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. aquiline (SKT.txt line 850)\", \"stance\": \"supports\", \"note\": \"'F. aquilin ... L. aquilinus, adj. from aquila, an eagle' — Skeat's eagle-family stops at Latin aquila.\"},\n      {\"src\": \"FSD\", \"where\": \"vol. II p.779 s.v. eagle\", \"stance\": \"supports\", \"note\": \"'[ < F. aigle, < L. aquila, orig. f. of aquilus, dark-colored.]'\"},\n      {\"src\": \"web\", \"where\": \"etymonline s.v. eagle\", \"stance\": \"supports\", \"note\": \"'mid-14c., from Old French egle ... Native term was erne.'\"}\n     ],\n     \"sources\": [E_EAGLE]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"French\",\n     \"words\": \"aquarium; eau : water; eau de Cologne : water (perfume) of Cologne\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"eau is the regular French descendant of Latin aqua: aqua > Vulgar Latin *awa > Old French ewe/eve (11th c.) > eaue > eau, the modern spelling fossilising a diphthongisation that is no longer pronounced ([o]). eau de Cologne, coined at Cologne in 1709 by Giovanni Maria Farina, is literally 'water of Cologne', the city name going back to Colonia (Agrippina). But 'aquarium' is NOT a French word inherited from aqua: Klein files it as 'L. aquarium, neut. of the adjective aquarius, ‚pertaining to water‘, used as a noun', and the modern sense was coined in English in 1830 (P. H. Gosse's 1854 book The Aquarium popularised it); French acquired aquarium as a learned borrowing of the same Latin word. Hence 'plausible': two of the three words are exactly right, the third is misfiled as French.\",\n     \"ref_check\": [\n      {\"ref\": \"KLN:495\", \"status\": \"supports\", \"note\": \"Klein (KLN_1966.txt line 12563, \\\\f-leaf 270, the leaf immediately after 'eagle' at KLN:494): 'Eau de Cologne, cologne. — F., lit. ‚water of Cologne‘. See eau de vie and cologne', and line 12564 'eau de vie, brandy. — F. eau-de-vie, lit. ‚water of life‘, fr. L. aqua, ‚water‘ ... See aquatic'. Supports 'eau' and 'eau de Cologne'; but Klein's own 'aquarium' entry (line 3263) labels it Latin, not French.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. aquarium, cologne, ewer\", \"stance\": \"partial\", \"note\": \"'aquarium, n. — L. aquarium, neut. of the adjective aquarius'; 'cologne ... Shortened fr. eau de Cologne, lit. ‚water of Cologne‘, fr. Cologne, French name of Köln in Germany, orig. called Colonia Agrippina'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. aqua\", \"stance\": \"supports\", \"note\": \"lists the Romance and learned derivatives of aqua, incl. 'aquarium v.h.a. ahhāri' — confirming aquarium as a Latin, not a native French, formation.\"},\n      {\"src\": \"web\", \"where\": \"etymonline s.v. aquarium\", \"stance\": \"partial\", \"note\": \"'1830, ‚artificial pond ...‘, from Latin aquarium ‚drinking place for cattle‘, noun use of neuter of adjective aquarius ‚pertaining to water‘' — an English coinage, not French.\"}\n     ],\n     \"sources\": [E_AQU]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"Persian\",\n     \"words\": \"âkvârîŭm «آکواریوم»; odokolon «ادوکلن ( ادکلن )»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Both are 20th-century European loans into Persian, and the chart's French source is right for the second and effectively right for the first. ادکلن odkolon / odokolon is French eau de Cologne taken over as a single unanalysed word, the French [o də kɔlɔɲ] being rendered ʾod(o/e)-kolon with the Persian stress on the last syllable; the variant ادوکلن spells the -o- of 'de' out. آکواریوم ākvāriy(y)om reproduces French/English aquarium letter by letter (qu > کو), i.e. ultimately Latin aquarium; it is a technical borrowing of the aquarium-keeping era, not a native formation.\",\n     \"ref_check\": [\n      {\"ref\": \"VOP:14,39\", \"status\": \"not_checked\", \"note\": \"VOP = Mahshid Moshiri, Farhang-e Vazheha-ye Orupāyi dar Farsi, Alborz 1371/1992. refs_online.json records kind 'none': searched archive.org, ketabnak, noorlib and the open web with no result; obtainable second-hand only. Not verifiable.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"web\", \"where\": \"Wiktionary s.v. Persian ادکلن\", \"stance\": \"supports\", \"note\": \"'Borrowed from French eau de Cologne, literally ‚cologne water‘'; pronunciations [ʔod̮kolon], [ʔod̮ekolon], [ʔod̮okolon] — the last is Nourai's odokolon.\"},\n      {\"src\": \"MON\", \"where\": \"MON_part1/part2 and the Adena two-volume text, searched for ادکلن and آکواریوم\", \"stance\": \"silent\", \"note\": \"neither word occurs; Mo'in's foreign-vocabulary volume (vol. 4), which is where such loans are treated, is not part of the local corpus.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (1062 AH)\", \"stance\": \"silent\", \"note\": \"a 17th-century dictionary; it cannot contain 19th-/20th-century European loans, so its silence is expected rather than evidence.\"}\n     ],\n     \"sources\": [W_ODK, E_AQU]\n    },\n    {\n     \"id\": 10,\n     \"lang\": \"English\",\n     \"words\": \"aquarium, aqua, aquatic\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All three are learned Latinisms rather than inherited words: aqua is Latin aqua used directly (in pharmacy from the 15th c., e.g. aqua fortis, aqua vitae); aquatic is from French aquatique < Latin aquāticus 'found in the water'; aquarium is the neuter of Latin aquarius pressed into service in 1830 for a garden pond and by 1853 for a glass tank. Since Latin aqua < PIE *h₂ékʷeh₂, the arrow from the Latin node is correct.\",\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. akwa-: the root entry lists Latin aqua as the source of the English aqua-words (index entries AQUARIUM/AQUATIC → akwa-).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. aquatic, aquarium, aqua fortis\", \"stance\": \"supports\", \"note\": \"'aquatic, adj. — F. aquatique, fr. L. aquāticus, ‚found in the water, watery‘, fr. aqua, ‚water‘, which is cogn. with Goth. aƕa ... ON ey, OE īeg, ‚island‘, Hitt. akw-anzi, ‚they drink‘.'\"},\n      {\"src\": \"web\", \"where\": \"etymonline s.v. aquarium\", \"stance\": \"supports\", \"note\": \"'from Latin aquarium ... from aqua ‚water‘, from PIE root *akwa- ‚water‘.'\"}\n     ],\n     \"sources\": [E_AQU]\n    },\n    {\n     \"id\": 11,\n     \"lang\": \"Germanic\",\n     \"words\": \"ahwjo, aujo\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *ahwō 'river, water' (= Latin aqua, Gothic aƕa) forms a feminine derivative *ahwjō 'the one surrounded by water', which loses the -h- before the glide to give *awjō/*aujō; hence ON ey 'island', OE īeg/īg, OHG -ouwa/ouwe (NHG Aue 'water-meadow'), and the compound *awjaland > OFris. eiland, Du. eiland, Ger. Eiland. Nourai's two spellings ahwjo / aujo are the two stages of exactly this development (Watkins writes them *agwjō > *aujō).\",\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 277: 'akwa-. Water. 1. Germanic *agwjō becoming *aujō, ‚thing on the water‘, in Old English ig, ieg, island ...' — including Nourai's gloss '(thing on) water, island' word for word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"printed p.23 s.v. akʷā-\", \"stance\": \"supports\", \"note\": \"'germ. *ahwō, davon abgeleitet *ahwjō, *awjō ‚die vom Wasser Umgebene‘ in aisl. ey f. ‚Insel, Aue‘, ags. īeg, ahd. -ouwa, -awa, mhd. ouwe f.'\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 34\", \"stance\": \"supports\", \"note\": \"'Hierzu germ. ahwī, ahwjō f. ‚Wasser, -land, Aue, Insel‘: aisl. ey ... ags. īeg f. ‚Insel‘ ... nhd. Aue.'\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. aquatic and island\", \"stance\": \"supports\", \"note\": \"'OHG. auwia, ouwa, MHG. ouwe, G. Au, ‚meadow watered by a brook‘ ... ON. ey, OE. īeg, ‚island‘.'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 1.25 ISLAND\", \"stance\": \"supports\", \"note\": \"'ON ey, eyland ... OE īg, īgland ... fr. a fem. deriv. (in part + land) of the word seen in Goth. ahwa ‚river‘, OE ēa ‚water, river‘, Lat. aqua ‚water‘. Walde-P. 1.34.'\"}\n     ],\n     \"sources\": [E_ISL, W_AKWA]\n    },\n    {\n     \"id\": 12,\n     \"lang\": \"English\",\n     \"words\": \"island\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"OE īgland/īegland = īeg 'island' (< PGmc *awjō < *ahwjō, from *ahwō 'water' = Latin aqua) + land; ME iland, yland (c.1300); the -s- is a false learned insertion of the 1590s, by association with the etymologically unrelated isle (OF isle < Latin īnsula). In English place-names īeg often denotes slightly raised dry ground in marshland (Isle of Ely). So the derivation from the water-root is right, and only the modern spelling is a red herring — worth stating, since a chart like this could be read as deriving the -s- from Latin too.\",\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. akwa-: 'Germanic *agwjō becoming *aujō, ‚thing on the water‘, in Old English ig, ieg, island' — Watkins lists ISLAND under this root.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. island (KLN_1966.txt line 19967)\", \"stance\": \"supports\", \"note\": \"'ME. iland, fr. OE. egland, igland, iegland ... compounded of eg, ig, ieg, ‚island‘, and land ... The first element ... is rel. to OE. ea, ‚water, river‘, ON. á, ‚river‘, ey, ‚island‘ ... OHG. aha, ‚river‘.'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 1.25 ISLAND\", \"stance\": \"supports\", \"note\": \"'OE īg, īgland, ME iland, NE island (with spelling influenced by isle)' — explicitly notes the intrusive s.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Eyot and s.v. subaqueous (SKT.txt lines 6176, 849)\", \"stance\": \"supports\", \"note\": \"'Eyot, a little island ... The A.S. form is īgoð, īgeað; where īg is cognate with Icel. ey; see Island', and under subaqueous 'And see Ait, Eyot, Island' — Skeat too files island under the aqua family.\"},\n      {\"src\": \"web\", \"where\": \"etymonline s.v. island\", \"stance\": \"supports\", \"note\": \"'from Old English igland, iegland ... from Proto-Germanic *awjo ‚thing on the water‘, from PIE root *akwa- ‚water‘ ... spelling modified 16c. by association with similar but unrelated isle.'\"}\n     ],\n     \"sources\": [E_ISL]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-44.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/write44.py && python3 -m json.tool data/verification/page-44.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-04T19:33:41.452Z] TOOL RESULT

```
written
JSON OK
```


## [2026-09-04T19:33:46.046Z] TOOL CALL #92: Bash

```json
{
 "command": "python3 tools/verify_check.py 44; echo \"exit=$?\""
}
```


### [2026-09-04T19:33:47.797Z] TOOL RESULT

```
nodes verified: 17/17
node verdicts: {'plausible': 3, 'confirmed': 11, 'disputed': 3}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'supports': 18, 'not_checked': 5, 'not_found': 1, 'partial': 1}
books consulted: {'supports': 46, 'partial': 9, 'contradicts': 5, 'silent': 4} | by book: {'web': 10, 'SYN': 6, 'KLN': 6, 'WLD': 4, 'BQT': 4, 'POK': 4, 'SKT': 4, 'HRN': 3, 'HUB': 3, 'MON': 3, 'LAT': 3, 'BRT': 2, 'IEC': 2, 'PHD': 2, 'NYB': 2, 'ARY': 2, 'FSD': 2, 'LEW': 1, 'WEB': 1}
exit=0
```


## [2026-09-04T19:34:04.973Z] AGENT

Done. `data/verification/page-44.json` written; `verify_check.py 44` exits 0 with no PROBLEM lines.

**Page 44 (book p.14) — 2 entries, 17 nodes**
- Roots: 1 confirmed (Akwa), 1 plausible (Akru, Dakru)
- Nodes: 11 confirmed, 3 plausible, 3 disputed
- Ref checks: 18 supports, 1 partial, 1 not_found, 5 not_checked. Books consulted: POK, WLD, AHD, IEC, SYN, KLN, SKT, LAT, LEW, BRT, PHD, NYB, HRN, HUB, BQT, MON, ARY, FSD, WEB + web.

**Disputed / flagged**
- *Akwa* #2 Avestan "arva, arvâ" (eagle) — not Avestan: it is the Pāzand form arvā of Bundahišn 14:23 (Mo'in's own footnote at BQT p.58; Horn no.43 "arvā (Bund.) in Zendbuchstaben"). Bartholomae has no such word; and it cannot descend from Latin aqua as drawn.
- *Akwa* #3 Pahlavi āluh — word real (PHD, NYB, Kārnāmag 14:12) but Nyberg derives it "< OP *ardūfya- < *ardifya-, Av. ərəzifya-" and Wiktionary from PIE *h₂rǵ-i-pt-ió-s; nothing to do with *h₂ekʷeh₂ "water".
- *Akwa* #5 Latin "aqualius" — no such Latin word; the book means aquila / aquilus (Nourai's gloss copies Klein). The aqua > aquilus step is Festus' folk etymology, rejected by Ernout-Meillet and doubted by de Vaan (Pokorny p.23 still prints it, which is presumably Nourai's warrant).
- Plausible: root box merges POK's two separate lemmas akru (p.23) / dakru (p.179), whose relation POK calls "ungeklärt"; #1 "asraka" is Horn's unattested *asraka, rejected by Hübschmann §88; #3 ašk is a doublet of ars (suffixed *Hácru-ka-, possibly a Parthian loan), not a descendant of MP ars; Akwa #8 "aquarium" is Latin/ModL, not French.
- MPP:79 (Henning, *Mitteliranisch*) is about Sogdian-Syriac script, not āluh — the citation is probably meant for Henning's *List* p.79 (which Nyberg cites for MPrs ʾawf). VFO and VOP have no copy anywhere.
- BQT:58 and BQT:103 were read from the archive.org page images (page numbers verified in the running heads); transcriptions saved to `data/verification/sources/refs/ocr/BQT/58.vision.txt` and `103.vision.txt`. 10 web pages archived via `fetch_source.py`.
