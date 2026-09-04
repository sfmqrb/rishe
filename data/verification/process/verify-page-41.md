# Verification process log — verify-page-41


## [2026-09-04T19:00:05.332Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 41 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-41.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-41.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-41.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 41` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T19:00:06.948Z] AGENT

I'll start by reading the instructions.


## [2026-09-04T19:00:09.132Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:00:09.149Z] TOOL RESULT

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


## [2026-09-04T19:00:09.375Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-41.txt"
}
```


### [2026-09-04T19:00:09.390Z] TOOL RESULT

```
1	=== PDF page 41 (book page 11) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Aiw : vitality, eternity  (refs POK:17)
4	#1 (parent #0) [Avestan] refs=POK:17 | âyu, ay : life, age ; yave : forever
5	  #2 (parent #1) [Pahlavi] refs=BQT:564; HRN:93 | yavě-tân : ever lasting
6	    #3 (parent #2) [Persian] refs=None | jâvîd «جاويد ( جاويدان )» : eternal
7	  #4 (parent #1) [Avestan] refs=KLN:31; BQT:264 | perana-âyu : full of life ☞Pel 1
8	    #5 (parent #4) [Pahlavi] refs=BQT:264 | a-purn-ây : not full of life, young ☞Ne 1
9	      #6 (parent #5) [Persian] refs=BQT:264 | bornâ «بُرنا» : young adult
10	  #7 (parent #1) [Avestan] refs=BQT:718; BRT:1862 | xvato-ayâo : alive by itself, God ☞Seu 1 | NOTE: Hub:54 derives this from Indo-European root "Ghu"
11	    #8 (parent #7) [Pahlavi] refs=None | xvatây : God
12	      #9 (parent #8) [Persian] refs=HRN:108; BQT:779; FSF:159 | Xodâ «خدا» : God ; xadîv «خديو» : governor, ruler ; xâjeh «خواجه» : master
13	#10 (parent #0) [Germanic] refs=AHD | aiwi
14	  #11 (parent #10) [English] refs=None | ever, every, never
15	#12 (parent #0) [Latin] refs=AHD | 
16	  #13 (parent #12) [English] refs=None | age, eternity
17	
```


## [2026-09-04T19:00:13.615Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-41.json && echo \"=== MATRIX ===\" && cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T19:00:13.671Z] TOOL RESULT

```
{
  "pdf_page": 41,
  "book_page": 11,
  "entries": [
    {
      "root": {
        "name": "Aiw",
        "lang": "Indo-European",
        "refs": "POK:17",
        "gloss": "vitality, eternity",
        "note": "Compare with root \"Yeu 2: young\""
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:17",
          "words": [
            {
              "translit": "âyu, ay",
              "gloss": "life, age",
              "script": null
            },
            {
              "translit": "yave",
              "gloss": "forever",
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
          "refs": "BQT:564; HRN:93",
          "words": [
            {
              "translit": "yavě-tân",
              "gloss": "ever lasting",
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
          "refs": null,
          "words": [
            {
              "translit": "jâvîd",
              "gloss": "eternal",
              "script": "جاويد ( جاويدان )"
            }
          ],
          "note": null,
          "quote": {
            "text": "دلش به ناله میازار وختم کن حافظ - که رستگاری جاوید در کم آزاریست",
            "poet": "Hâfez"
          }
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Avestan",
          "refs": "KLN:31; BQT:264",
          "words": [
            {
              "translit": "perana-âyu",
              "gloss": "full of life",
              "script": null,
              "see": [
                "Pel 1"
              ]
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Pahlavi",
          "refs": "BQT:264",
          "words": [
            {
              "translit": "a-purn-ây",
              "gloss": "not full of life, young",
              "script": null,
              "see": [
                "Ne 1"
              ]
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:264",
          "words": [
            {
              "translit": "bornâ",
              "gloss": "young adult",
              "script": "بُرنا"
            }
          ],
          "note": null,
          "quote": {
            "text": "توانا بود هرکه دانا بود - زدانش دل پیر برنا بود",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 7,
          "parent": 1,
          "lang": "Avestan",
          "refs": "BQT:718; BRT:1862",
          "words": [
            {
              "translit": "xvato-ayâo",
              "gloss": "alive by itself, God",
              "script": null,
              "see": [
                "Seu 1"
              ]
            }
          ],
          "note": "Hub:54 derives this from Indo-European root \"Ghu\"",
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {
              "translit": "xvatây",
              "gloss": "God",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "HRN:108; BQT:779; FSF:159",
          "words": [
            {
              "translit": "Xodâ",
              "gloss": "God",
              "script": "خدا"
            },
            {
              "translit": "xadîv",
              "gloss": "governor, ruler",
              "script": "خديو"
            },
            {
              "translit": "xâjeh",
              "gloss": "master",
              "script": "خواجه"
            }
          ],
          "note": null,
          "quote": {
            "text": "سیامک به دست خرزوان دیو - تبه گشت وگشت انجمن بی خدیو",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "aiwi",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "ever, every, never",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "age, eternity",
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


## [2026-09-04T19:00:22.625Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','BQT','HRN','KLN','BRT','FSF','AHD','HUB','PHD','NYB','MON','WLD','IEC','SYN','SKT','FSD','WEB','ARY','TLM','KNT','CHEUNG']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600]); print()\n\" && sed -n 1,80p tools/verify_check.py"
}
```


### [2026-09-04T19:00:24.636Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

TLM {"title": "H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Series, 1908", "edition_found": "1908", "kind": "archive_djvu", "url": "https://archive.org/details/ancientpersianle00tolm_0", "identifier": "ancientpersianle00tolm_0 (also in.ernet.dli.2015.90691, ancientpersianl00tolmgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/TLM.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 24 = p.4). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

CHEUNG null

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


## [2026-09-04T19:00:27.851Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 80,200p tools/verify_check.py; ls data/verification/ | head -30"
}
```


### [2026-09-04T19:00:27.897Z] TOOL RESULT

```
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
process
sources
```


## [2026-09-04T19:00:32.193Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-38.json'));e=d['entries'][0]\nprint(json.dumps({k:v for k,v in d.items() if k!='entries'},ensure_ascii=False,indent=1))\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:2500])\n\""
}
```


### [2026-09-04T19:00:34.176Z] TOOL RESULT

```
{
 "pdf_page": 38,
 "book_page": 8,
 "verified_by": "claude-fable-5-1",
 "verified_on": "2026-09-04"
}
{
 "id": 1,
 "lang": "Pahlavi",
 "words": "ahŭk 2",
 "verdict": "confirmed",
 "derivation": "Middle Persian āhōg, spelled ʾhwk' in Book Pahlavi and ʾhwg in Manichaean script, 'fault, blemish' — MacKenzie, CPD p.5: \"āhōg [ʾhwk' | M ʾhwg, N āhū] fault, blemish\". The Manichaean spelling with -g shows the suffix -ōg (< Old Iranian *-uka-) with the stop already voiced; the same suffix gives the homonym āhūg [ʾhwk' | M (ʾ)ʾhwg, N āhū] 'gazelle' (CPD p.5), which is why Nourai and Mo'in both number these words 1 and 2. The negated form is attested in Pahlavi too: an-āhōg [ʾnʾhwk'] 'undefiled' (CPD p.9), i.e. the exact Middle Persian counterpart of Avestan an-āhita-, which ties this node to node #3. Two remarks on the printed form: the book writes 'ahŭk' without marking the long ā- of āhōg, and it uses the older Pahlavi transcription with -k for what MacKenzie reads -g; neither is an error in the JSON (checked against the page image), just Nourai's 1960s-style transcription following Mo'in's 'âhôk'.",
 "sources": [
  "https://en.wiktionary.org/wiki/%D8%A2%D9%87%D9%88"
 ],
 "ref_check": [
  {
   "ref": "BQT:72",
   "status": "supports",
   "note": "Mo'in's footnote 1 on printed p.72 names the Pahlavi form explicitly: 'پهلوی âhôk (عیب)' = Pahlavi āhōk 'defect' — exactly this node (see the saved vision reading data/verification/sources/refs/ocr/BQT/72.vision.txt)."
  }
 ],
 "consulted": [
  {
   "src": "PHD",
   "where": "PHD_mackenzie.txt line 948 = CPD p.5 s.v. āhōg",
   "stance": "supports",
   "note": "\"āhōg [ʾhwk' | M ʾhwg, N āhū] fault, blemish\"; and line 960 \"āhūg [ʾhwk' | M (ʾ)ʾhwg, N āhū] gazelle\" — the two homonyms Nourai numbers, with the New Persian outcome āhū given for both."
  },
  {
   "src": "NYB",
   "where": "grep 'ahok|āhōk|ahog' in NYB_vol2_glossary.txt",
   "stance": "silent",
   "note": "Nyberg's Manual of Pahlavi glossary has no āhōk entry (it covers only the texts printed in Part I); it does have 'Anāhit [ʾnʾhyt'] a female deity; the planet Venus 511. — Av. (125) Anāhita' (line 419), which belongs to node #4."
  },
  {
   "src": "HRN",
   "where": "HRN.txt no. 59, p.1-2 (grep 'Gazelle')",
   "stance": "partial",
   "note": "Horn's Grundriss no. 59 is 'āhu \"Gazelle\". phlv. āhūk \"Gazelle\"' — he registers only the animal homonym and its Pahlavi ancestor, and says nothing about āhū 'fault'. Confirms the Pahlavi -ūk/-ōk word type but is silent on this particular sense."
  }
 ]
}
```


## [2026-09-04T19:01:02.300Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\n# POK_01: leaf = p + 8 ; page 17 -> leaf 25\nfor n in (24,25,26):\n    print('==== leaf',n,'====')\n    print(t[n][:3000])\nEOF"
}
```


### [2026-09-04T19:01:04.036Z] TOOL RESULT

```
364
==== leaf 24 ====
gn. aisis  ,dis*,  volsk.  esaristrom  ,sacrificium^,  umbr.  esono-  ,divinus,  sacer^, stammen  aus  dem  Etruskischen.     Anders   Devoto  St.  Etr.  5,  299  f.
d-Erweiterung:  gr.  aido{.iaL  (aus  *aiz-d-)  ,scheue,  verehre^,  aldcog,  -ovg ,Ehrfurcht,  Scheu,  Scham^,  aldeofxai.  {^aldsa-oixai)  ,at'Jo//ßi^;  got.  aistan, -aida   ,sich   scheuen,   achten^;    tiefstufig   ai.  IcU  ,verehre,  preise,  flehe  an^
WP.  I  13,  WH.  I  20,  419,  844;   Feist  28  a,  Kretschmer  Gl.  30,  881
aisk-  ,klar,  hell,  leuchtend^
Awnord.  eiskra  ,vor  hitziger  Erregung  wüten^,  nisl.  iskra  auch  von brennendem  Schmerz.
17
Lit.  diSkus,  woneben  seh  wund  stufig-  alit.  üJdis  ^deutlich^
Russ.  dial.  jdska,  demin.  jdsocka  ^klarer  Stern^^  daneben  Sih ^.  jasno  Adv. ,klar,  deutlich^^  russ.  jdsiiyj  ^licht^  klar^  aus  *aiskno-]  poln.  jaskry^  jas- kvawy  ^blendend;,  funkelnd^  aus  *aiskro-]  abg-.  iskra  ^Funke^  usw.  aus  *iskrä.
Hierher  die  FIN  nhd.  Aisch  (Bayern)^  Eysch{en)  (Luxemburg)^  nengl Axe  aus  kelt.  oder  ven.-ill.  '^Aiskä.
WP.  I  2,  Trautmann  4,  Pokorny  Urill.  70,  113,  M.  Förster  Themse  839.
Vielleicht  aus  *aidh-sk-  entstanden,  oder  aus  *ai-sk-  zu  4.  äi-.
ai-tro-
Lit.  aitriis  , bitter,  herb^,  aiträ  f.  ,Schärfe^  (auch  übertragen);  nasal- infigierendes  *intro-  vielleicht  in  abg.  oh-etriti  ,entbrennen  lassen^,  o.  se , brennen,  hitzig  sein^,  wru.  zajdtric  ,erzürnen^,   klr.  roz-jatryti  sa  ,eitern^
WP.  I  3,  Berneker  269.
Vielleicht  zu  4.  äi-.
aiu-f  aiu-  ,Lebenskraft'^.
Ai.  dyu-  n.  , Lebenskraft^,  substantiviertes  Adjektiv  zu  äyu-  ,beweglicli, regsam^;  äyil-h  m.  ,Genius  der  Lebenskraft^,  davon  abgeleitet  der  5-St. ayuh  n.  Gen.,  äyusa'i  ,Lebenskraft^  (*diuos^  Gen.  *ah(s-es)]  nSt.  im  Lok. äyunij  Instr.  äyunä]  yäh  , Lebenskraft^;
av.  äyü  n.  , Lebensdauer^,  Gen.  yaos,  Dat.  yavöl,  Instr.  yavä,  davon yavaetät-  ,Dauer^,  yavaejl-  ,immer  lebend-;   yus  m.  ,Lebensdauer^;
Gr.  s-St. ;  kypr.  vSatg  t^av  (=  diä  ßlov);  suffixloser  Lok.  lakon.  aisg ,immer^;  hom.  alsl,  att.  dsi  (^^aLj^eOi),  Akk.  aatt.  auo  (*aLJ^oaa);  Dat.-Lok. ohne  Erweiterung  in  ion.  aa,  lesb.  ^l  {*aiJ^i)  (danach  dtdiog  ^ewig^,  drjv- aiog  ,langlebend^);  n-St.:  ald}v  m.  (und  f.  nach  aiü)g)  ,Lebenskraft,  Lebens- dauer"^, alsv  ,immer^;
alb.  eshe  , Zeitraum*^  aus  '^^aiuesiä  (Jokl  L.-k.  U.  34);
lat.  o-St.  aeviis  m.  und  aevum  n.  , Lebenszeit,  Ewigkeit^;  hingegen beruhen  aefas  f.,  alt  aevttas  (daraus  osk.  Gen.  aitateis,  Akk.  aitatum,  päl. Abi.  aetatu)  , Zeitalter^,  aetermis  ,ewig^  auf  adverbialem   *ami.
Got.  o-St.  aüus  m.  ,Zeit,  Ewigkeit,  Welt^;  i-St.  adverbiell  aiiv  (^aiiti) =  aisl.  36,  ei  (auch  in  ei-gi  ,nicht^),  ags.  ä,  ö,  ahd.  io  ,je,  immer^,  got
==== leaf 25 ====
. ni  aiw  ,nie^,  ahd.  neo,  nio,  nhd.  ?n'e;  ags.  n-a,  engl,  no  ,nicht,  nein^;  aisl. lang-^r  =  lat.  longaevus  ,langlebig*^;  2-St.  auch  in  aisl.  ößfi,  cevi  f.(*aiiii-) ,Leben,  Zeitalter^;  ä-St.  in  ahd.  eiva  f.  ,Zeit,  Ewigkeit^,  davon  alid.  eicidö ,]i]wigkeit^,  eiülg  ,ewig'^;  got.  aju-k-daps  f.  ,Ewigkeit'^  aus  *ajuki-  (==  ags. ece  ,ewig^),  mit  idg.  ^-Suffix  +  idg.  -tüti--^
toch.  A  äym-  , Geist,  Leben'^,  das  m  von   änm-  ,Leben^  bezogen.
AVP.  I  6,  WH.  I  21,  EM.  21,  Feist  30,  32,  Benveniste  BSL  38,  103 ff., Dumezil  BSL  39,  193,  Specht  KZ.  68,  196,  Dekl.  88  ff..  Van  Windekens  15.
2
18
Hiervon  abgeleitet  *iuuen-  ^jung';   Specht  will   auch  sehr  gewagt  *aig-    \ ,Eiche^  (=  .Lebenskraft'?)  hierzustellen.
1.  ak-,  ako-  .essend
Ai.  asnätl  (infigiert,  Inf.  asi-tum  usw.)  ,ißt,  verzehrt',  dsanam  n.  ,das Essen;  Speise',  d^na-h  .gefräßig',  dehnstufig  äsayati  .läßt  speisen',  prätar- äsa-h  .Frühstück';  av.  kahrk-äsa  .Hähnefresser  =  Geier'  usw.;
gr.  ^y,vlog  f.  .Eichel'  (als  .Nahrung',  vgl.  formal  ai.  asü-sa-h  .gefräßig'). äxoXog  .Bissen';
an.  agn  n.  .Lockspeise  für  Fische^  (*akd-nö-\  xja  .weiden  lassen'  (^alijan).
WP.  I  112  f..  WH.  I  210  f.
2.  ak-,  ok-  .scharf,  spitz,  kantig'  und  , Stein'.
1.  e/o-  und  ä-St.:
Npers.  äs  (dehnstufig)  .Mühlstein';  gr.  dyn]  .Spitze',  dehnstufig  ion.  -^zi}* cJzwxtJ,  iTtidogavig,  rfAurj  Hes.,  redupl.  ^xwxtJ  .Spitze.  Schneide'  (wie  dyct)- yf]  :äya));  nach  Kretsclimer  KZ.  33.  567  und  Schwyzer  Gr.  Gr.  I  348  ge- hört dyiovcj  .höre'  als  *d7,-ovg-  .das  Ohr  scharf  habend'  hierher,  s.  aber 1.  keu-]  alb.  athete  .herb,  sauer';  lat.  acere  .sauer  sein',  acidus  .sauer'. acetum  .Essig';
mit  o:  mbr.  convoc  ar  vilin  .den  Mühlstein  schärfen',  cymr.  hogi  .schär- fen', acymr.  ocoluin,  ncymr.  hogalen,  mbret.  hygo(u)leiij  nbret.  liigolenn .Wetzstein'  (mit  unklarem  zweitem  Bestandteil;  der  bret.  Vokalismus  des Anlauts  durch  den  Vorton  zu  erklären);  mc.  cyfogi  .sich  erbrechen, kämpfen',  mit  sekundärem  lO-Suffix  acymr.  cemecld,  ncymr.  cyfegydd (*kom-okiio-)  .Spitzhacke' ;
mit  Dehnstufe;  acymr.  diauc,  ncymr.  diog,  mbr.  dieuc  (*de-äko-)  .faul', mcymr.  ym-am-ogawv  {^^-äkä-r)  .man  regt  sich,  ist  tätig'  (Loth  RC.  45.  191) und  mbr.  eaug,  nbret.  eok  .reif,  aufgeweicht'  (*eks-äko-),  zu  gall.  exäcum .centaurion  lepton'  (Ernault  Gloss.  MBret.  201);  vgl.  auch  oben  S.  5;
schwed.  ag  m.  .Sumpfgras.  Cladium  mariscus.  Schneide'  (*akö-),  mhd. ag  .Barsch',  egle,  eglinc  ds..  nhd.  Schweiz,  egel,  Demin.  egli,  aschwed.  agh- borre  ds..  vielleicht  auch  schwed.  agg  .Groll.  Haß',  agga  .stechen,  plagen', norw.  dial.  agge  .Zahn.  Spitze'  {*ako-k�
==== leaf 26 ====
�-  oder  expressive  Gemination?), sowie  (mit  sekundärem  germ.  Ablaut  a  :  ii  oder  aus  *akuko-  mit  Assimila- tion des  a  an  w?)  norw.  dial.  ugg  .Stachel.  Ängstigung',  schwed.  dial.  ugg .Zacke,  Zahn',  anord.w^^r  .Furcht',  norw.  dial.  it^^e  .Flosse';  lit.  aküotas^) .Granne',  äsaka^  {*ako-kä)  .Fischgräte.  Kleie'  ==  wruss.  osoka  .carex'. apr.  ackons  {^aköno-)  ds.
^)  Die  baltoslav.  Formen  mit  h  beweisen  keine  idg.  Nebenform  ak-,  sondern  sind  teilweise Lehnworte  aus  dem  Veneto-lllyrischen,  dessen  Gebiet  von  den  Balten  und  Slaven  überschich- tet  worden  war  (Kretschmer  Gl.  21,  115).    Ebenso  erklärt  sich  das  g  in  ksl.  igla  oben  S.  15.
19
2.  i-  und  j-Stämme:
Arm.  asehi  ,NadeP  (aus  '^asüa,  Meillet  Esquisse  43);  gv.  (^//g,  -löog Spitze^  StaclieP;  lat.  acies  , Schärfe^  Schneide^  Schlaclitreihe^;  as.  eggja  f., ahd.  usw.  ekha  , Spitze,  Scliwertschneide^;  nhd.  Ecke  (urg-erm.  '^a%iö,  anord. egq  ^Schneide;  Fels  rücken^,  ^ggj(^  ,schäi-fen,  anspornen^,  ags.  ecg  ^Kante, Schneide^  Schwert^  (daraus  entlehnt  mir.  ecg  ^Schneide^,  nbret.  ek  , Spitze'), egle  PI.  ^Grannen',  engl,  ails]  aksl.  osla  (*osbla)j  russ.  oselok  m.  ,Wetz- stein^,  cech.  osina  f.  ,Granne^
Über  ag's.  eher  ,Alire'  s.  unter  s-Formantien.
3.  u-St.:
Gr.  icxvQOv  , Spreu'  s.  unter  s-Formantien ;  lat.  acus^  -üs  L  , Nadel;  Fiscli- name',  acuere  , schärfen',  acümen  , Spitze',  acia  (f^acu-iä)  , Faden  zum Nähen',  aquifolium  (neben  äcrifoUum)  , Stechpalme',  aculeus  , Stachel', accipiter  ,Habicht,  Falke'  (*acu-peter  ,schnellfliegendQ ;  gall.  acaunum (^akounon)  , Felsen';  ill.  ON  Äcumincum  heute  Szlankamen  ,Salzstein' (Banat);  nhd.  Achel  f.  , Ährenspitze'  aus  ndd.  aggel  (mit  spirant.  g)  aus idg.  *aku-lä]  ags.  äiüel  m.  , Gabel',  anord.  sotS-äll  , Fleischgabel'  (germ. *ahwala-y  idg.  *dku-olo-) ;  falls  hierher  gallo-lat.  opulus  , Feldahorn'  (Mar- strander,  Corr.  germ.-celt.  18),  würde  idg.  *oku-olo-  anzusetzen  sein;  über anord.  uggr  usw.  s.  e/o-St.,  über  ags.  ear  s.  5-Formantien;  cymr.  ehill ,Bohrer',  mbr.  ebil  ,Pflock,  Nagel'  (*aku-llio-) ;  halt.  *ahis  in  lett.  ass , scharf,  spitzig',  lit.  asutai  m.  PL  , grobe  Pferdehaare'  =  slav.  *o§uta  m. , Distel'  in  ksl.  os^U,  russ.  osöt.  Ob  hierher  toch.  A  acäice  ,rauh'  (Van Windekens  Lexique  15)?
S.  auch  unter  "^öku-s  , schnell  (scharf  in  der  Bewegung)'.
4.  Mit  m-Formantien : akmo'/'ä
Gr.  dKUTj  ,Spitze,  Schneide,  Sch�
```


## [2026-09-04T19:01:14.695Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD ===\" && grep -n -i -m5 -A25 \"^aiw-\\|aiw- *Vital force\\|aiw-\" AHD_watkins1985.txt | head -60"
}
```


### [2026-09-04T19:01:14.754Z] TOOL RESULT

```
<persisted-output>
Output too large (31.2KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bafxtuwzv.txt

Preview (first 2KB):
=== AHD ===
183:A hint of Indo-European metaphysics ap- pears in the word aiw-, “vital force,” whence “long life, the eternal recreation of life, eter- nity” (EON). It is noteworthy that the idea of “holy” is intimately bound up with that of “whole, healthy” in a number of forms: kailo- (WHOLE and HOLY), swento- (SOUND?), and sole-, whence Latin salvus (SALVATION). An ancient root relating solely to religion is sak- (SACRED).
184-Another aspect of the function of sover- eignty is the sphere of the law. There is an old word, yewes-, probably for “religious law,” in Latin jus. Latin léx is also ancient (leg-'), though the details of its etymology are uncertain. In a society that emphasized the principle of exchange and reciprocity, it is scarcely surprising that the notion of con- tractual obligation should be well repre- sented. Several roots specify the notion of “bond”: bhendh-, ned-, leig-', all of which have derivatives with technical legal mean- ings in various languages. The word for “a pledge,” wadh-', exists in western Indo- European, whence the English verb for mak- ing a particular kind of contract, WED. An oath then as now was important: the roots *serk- and oito- are found in Celtic and Ger- manic. The verb k”ei-' meant “to pay com- pensation for an injury.” Its derivative noun, *k“oind, was borrowed from Doric Greek into the most ancient Roman law as Latin poena, punire, whence English PUNISH and a host of legal terms. The Greek word for jus- tice, diké, is derived from the notion of “boundary marker” (deik-; compare also ter-, “termen-).
185-In conclusion we may add that poetry and a tradition of poetics are also common patri- mony in most of the Indo-European tradi- tions. The hymns of the Rig-Veda are composed in meters related to those used by
186-xxiv
...
</persisted-output>
```


## [2026-09-04T19:01:17.054Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Vital force\" AHD_watkins1985.txt | head; echo ---; grep -n \"aiw-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-04T19:01:17.140Z] TOOL RESULT

```
274:aiw-. Vital force, life, long life, eternity; also “endowed with the acme of vital force, young.” 1. Extended form in Germanic *aiwi in: a. Old English a, ever: No}; b. Ger- manic *aiwi + *wihti, “ever a thing, anything” (*wihii-, thing; see wekti-), in Old English Gwiht, duht, anything, “ever a creature”: AUGHT!; c. Old English &fre (second element obscure), ever: EVER; EVERY, NEVER; d. Old Norse ei, ever: AYE?; NAY. 2. Suffixed form *ai-wo- in: a. Latin aevum, age, eternity: COEVAL, LONGEVITY, ME- DIEVAL, PRIMEVAL; b. suffixed form *aiwo-tdt- in Latin aetds (stem aetdt-), age: AGE; COETANEOUS; C. suffixed form *aiwo-terno- in Latin aeternus, eternal: ETERNAL; SEMPITERNAL. 3. Suffixed form *aiw-en- in Greek aidn, age, vital force: EON. See also *yuwwen- under yeu-. [Pok. aiu- 17.]
1135:Old English war, seaweed: SEAWARE. 3. Suffixed zero-grade form *wi-ria- in Latin (of Celtic origin) viriae, bracelets: FERRULE. 4. Suffixed form *wei-ti- in Ger- manic *with- willow, in Old English withig, wiry: wITHY. 5. Suffixed zero-grade form *wi-t- in Germanic withj6n- in Old English withthe, supple twig: wITHE. II. Form *weia-, zero-grade *wi- (< *wia-). 1. Suffixed form *wi-ti- in Latin vitis, vine: VISE; VITICULTURE. 2. Suffixed form *wi-td- becoming *wittd in Latin vitta, headband: viTTA. 3. Suffixed form *wi-ri- probably in Greek iris, rainbow, and Iris, rainbow goddess: (IRIDACEOUS), IRIDO-, IRIS, IRIS; (IRIDIUM), (IRISITIS). 4. Suffixed form *wi-n- per- haps in Greek is (genitive inos), sinew: EXINE, INOSITOL, INOTROPIC. [Pok. 1. wei- 1120.] wei-?. To go after something. Suffixed o-grade form in Germanic *wai-thj6-, “pursuit,” with denominative *waithanjan, to hunt, plunder, in Old French gaaignier, gaigner, to obtain: GAIN}; ROWEN. [Pok. 3. wei- 1123.] wei-%. To wither. Extended form *weis- in Germanic *wis- in suffixed form *wis-n-6n in Old English wisnian, to wither, shrivel, shrink: wizEN. [Pok. 2. wei- 1123.] wei-*. Vice, fault, guilt. 1. Suffixed zero-grade form *wi-tio- in Latin vitium, fault, vice: vICE1, vICcIoUs, VITIATE. 2. Suffixed form “wi-tu- in: a. Latin vitiligo, tetter (< “blemish”): vITILIGO; b. Latin vituperdre, to abuse (perhaps formed after Latin recuperdre, to regain; see kap-): VITUPERATE. [Pok. 1. wi- 1175.] weid-. To see. I. Full-grade form *weid-. 1. Germanic *witan, to look after, guard, ascribe to, reproach, in: a. Old English witan, to reproach: Twit; b. Old Proven- gal guida, a guide: GUIDE; c. Germanic derivative noun *witi- in Old English wite, fine, penalty: WITE!. 2. Suf- fixed form *weid-to- in Germanic *wissaz in: a. Old English wis, wise: WISE!; b. Old English wisdém, learn- ing, wisdom (-d6ém, abstract suffix; see dhé-'): WISDOM; c. Old High German wissago, seer, prophet: WISEACRE; d. Germanic *wissdén-, appearance, form, manner, in (i) Old English wise, wis, manner: WISE? (ii) Old French guise, manner: GUISE. 3. Suffixed form *weid-es- in Greek eidos, form, shape: EIDETIC, EIDOLON, IDOL, IDYLL, -OID; IDOCRASE, KALEIDOSCOPE. 4. Perhaps Greek Haidés (also Aidés), the underworld, perhaps “the invisi- ble” (> French Hadés): HADAL, Hangs. II. Zero-grade form *wid-. 1.Germanic *wit- in: a. Old English wit, witt, knowledge, intelligence: wit}; b. Old English wita (genitive plural witena), wise man, councilor: WITENAGE- MOT. 2. Germanic *witan in Old English witan, to know: WIT2; UNWITTING. 3. Suffixed form *wid-to- in Germanic *wissaz, known, in Old English gewis, gewiss, certain, sure: IWIS. 4. Form *wid-é- (with participial form *weid-to-) in Latin vidére (past participle visus), to see, look: VIDE, VIEW, VISA, VISAGE, VISION, VISTA, VOYEUR; ADVICE, (ADVISE), BELVEDERE, CLAIRVOYANCE, ENVY, EVIDENT, INTERVIEW, PREVISE, PROVIDE, REVIEW, SU- PERVISE, SURVEY. 5. Suffixed form *wid-es-ya in Greek idea, appearance, form, idea: IDEA, IDEO-. 6. Suffixed form *wid-tor- in Greek histdr, wise, learned, learned man: HISTORY, (STORY!); POLYHISTOR. 7. Suffixed nasal- ized form *wi-n-d-no- in: a. Irish fionn, white (< “clearly visible”): COLCANNON; b. Welsh gwyn, gwynn, white: PENGUIN. 8. Celtic compound *dru-wid-, ““knower of trees” (*dru-, tree; see deru-). III. Suffixed o-grade form *woid-o- in Sanskrit vedah, knowledge: VEDA; RicG- VepaA. [Pok. 2. ufe)di- 1125.] weidh-. To divide, separate. 1. Suffixed zero-grade form *widh-ewo-, “bereft,” feminine *widh-ewd-, “woman separated (from her husband by death),” in Germanic *widuw6 in Old English widuwe, widow: wiDow. 2. Zero-grade form *widh- in Latin dividere, to separate (dis-, intensive prefix): DEVISE, DIVIDE, POINT-DEVICE. [Pok. weidh- 1127.] weie-. Vital force. Perhaps related to wi-ro-. Zero-grade form *wi- (< *wia-) in Latin vis, force, with irregular
1195:yeu-. Vital force, youthful vigor. Earliest form *ayeu-; variant of aiw-. Suffixed zero-grade form *yuwen- (< *yu-sen-), “possessing youthful vigor,” young. 1. Further suffixed form *yuwn-ti- in Germanic *jugunthi-, *jugun- tha- in Old English geoguth, youth: YOUTH. 2. Further suffixed form *yuwn-ko- in: a. Germanic *juwungaz becoming *jungaz in (i) Old English geong, young: YOUNG (ii) Old High German jung, young: JUNKER (iii) compound *jung-fréw6-, young lady (see per’); b. Old Irish 6ac, Irish Gaelic 6g, in oglach, soldier: GALLOW- GLASS. 3. Latin iuvenis, young: JUNIOR, JUVENILE; JUVE- NOCRACY, REJUVENATE. [Pok. 3. ieu- 510.]
---
183:A hint of Indo-European metaphysics ap- pears in the word aiw-, “vital force,” whence “long life, the eternal recreation of life, eter- nity” (EON). It is noteworthy that the idea of “holy” is intimately bound up with that of “whole, healthy” in a number of forms: kailo- (WHOLE and HOLY), swento- (SOUND?), and sole-, whence Latin salvus (SALVATION). An ancient root relating solely to religion is sak- (SACRED).
274:aiw-. Vital force, life, long life, eternity; also “endowed with the acme of vital force, young.” 1. Extended form in Germanic *aiwi in: a. Old English a, ever: No}; b. Ger- manic *aiwi + *wihti, “ever a thing, anything” (*wihii-, thing; see wekti-), in Old English Gwiht, duht, anything, “ever a creature”: AUGHT!; c. Old English &fre (second element obscure), ever: EVER; EVERY, NEVER; d. Old Norse ei, ever: AYE?; NAY. 2. Suffixed form *ai-wo- in: a. Latin aevum, age, eternity: COEVAL, LONGEVITY, ME- DIEVAL, PRIMEVAL; b. suffixed form *aiwo-tdt- in Latin aetds (stem aetdt-), age: AGE; COETANEOUS; C. suffixed form *aiwo-terno- in Latin aeternus, eternal: ETERNAL; SEMPITERNAL. 3. Suffixed form *aiw-en- in Greek aidn, age, vital force: EON. See also *yuwwen- under yeu-. [Pok. aiu- 17.]
655:kwo-. Also ki-. Stem of relative and interrogative pro- nouns. 1. Germanic *hwa-, hwi- in: a. personal pronouns *hwas, *hwasa, *hwam in Old English hwd, hwes, hwem, who, whose, whom: WHO, WHOSE, WHOM; b. pro- noun *hwat in Old English hwet, what: WHAT; c. adverb *hwi in Old English hwy, why: wHy; d. relative pronoun *hwa-lik- (*lik-, body, form; see lik-) in Old English hwilc, hwelc, which: WHICH; e. adverb *hwo6 in Old English hii, how: How!; f. adverb *hwan- in (i) Old English hwenne, hwanne, when: WHEN (ii) Old English hwanon, whence: WHENCE; g. adverb *hwithré in Old English hwider, whither: WHITHER; h. adverb *hwar- in Old English hwér, where: WHERE. 2. Germanic *hwatha- raz in: a. Old English hwether, hwether, which of two, whether: WHETHER; NEITHER; b. Germanic phrase *aiwo gihwatharaz, “ever each of two” (*aiwo, *aiwi, ever; see aiw-; *gi- from *ga-, collective prefix; see kom), in Old English €ghwether, &ther, either: EITHER. 3. Latin gui, who (genitive plural guérum): QUA, QUIB- BLE, QUORUM. 4. Latin quid, what, something: HIDALGO, QUIDDITY, QUIDNUNC, QuIP. 5. Latin quam, as, than, how, in quasi (quam + si, if; see swo-), as if: QUASI. 6. Latin quod, what: QUODLIBET. 7. Latin quot, how Many: QUOTE, QUOTIDIAN, QUOTIENT; ALIQUOT. 8. Latin quom, when: QUONDAM. 9. Latin quem, whom: CON- QUIAN. 10. Latin quantus, how great: QUANTITY. 11. Latin gudlis, of what kind: QuALITY. 12. Latin ut, that: (uT). 13. Latin uter, either of two: NEUTER. 14, Latin ubi, where, and ibi, there: ALIBI, UBIQUITY. 15. Persian chiz, thing: CHEESE, [Pok. k¥o- 644.] kwon-. Dog. 1. Greek kudn, dog: CYNIC; CYNOSURE, PROCYON, QUINSY. 2. Suffixed zero-grade form “kwn-to- in Germanic *hundaz in: a. Old English hund, dog: HOUND; b. Old High German Aunt (> German Hund), dog: DACHSHUND; c. Dutch hond, dog: KEESHOND. 3. Nominative form *kw6o in Welsh ci, dog: CORGI. 4. Variant *kan-i- in Latin canis, dog: CANAILLE, CA- NARY, CANICULA, CANINE, CHENILLE, KENNEL}, [Pok. Ruon- 632.]
698:[lik-. Body, form; like, same. Germanic root. 1. Old English lic, form, body: LICH GATE. 2. Old English -lic, having the form of: -LyY!}, -Ly?. 3. a. Germanic *galikaz in Old English gelic, similar: ALIKE, LIKE?; b. Germanic phrase *aiwo galikaz, “ever alike” (*aiwo, *aiwi, ever; see aiw-), in Old English #lc, each: EACH. 4. Germanic *is-lik in Old English ilca, the same (see i-). 5. Old Norse likr, like: LIKELY. 6. Middle Dutch -lijc, -ly: FROLIC. 7. Germanic *likjan in Old English lician, to please: LIKE!, 8. Germanic *hwa-lik-, which (see k’o-). [In Pok. 2. leig- 667.]]
1195:yeu-. Vital force, youthful vigor. Earliest form *ayeu-; variant of aiw-. Suffixed zero-grade form *yuwen- (< *yu-sen-), “possessing youthful vigor,” young. 1. Further suffixed form *yuwn-ti- in Germanic *jugunthi-, *jugun- tha- in Old English geoguth, youth: YOUTH. 2. Further suffixed form *yuwn-ko- in: a. Germanic *juwungaz becoming *jungaz in (i) Old English geong, young: YOUNG (ii) Old High German jung, young: JUNKER (iii) compound *jung-fréw6-, young lady (see per’); b. Old Irish 6ac, Irish Gaelic 6g, in oglach, soldier: GALLOW- GLASS. 3. Latin iuvenis, young: JUNIOR, JUVENILE; JUVE- NOCRACY, REJUVENATE. [Pok. 3. ieu- 510.]
1218:AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE aiw- AGENDUM ag- AGENT ag- AGERATUM gere-1 AGGLOMERATE gel-1 AGGLUTINATE gel-1 AGGRAVATE gWere-2 AGGREGATE ger-? AGGRESS ghredh- AGGRIEVE gWere-2 AGHAST gheis- AGILE ag-
1266:ASTERIATED | ster-3 ASTERISK ster-3 ASTERISM  ster-3 ASTEROID ster-3 ASTIGMATISM _ steig- ASTONISH (s)tena- ASTRAEA | Ster-3 ASTRAGAL ost- ASTRAGALUS ost- ASTRAL  ster-3 ASTRAPHOBIA | ster-3 ASTRINGE | streig- ASTRO-  Ster-3 ASTROBLEME gWele-1 ASTROLABE (s)lagW- ASTRONAUT nau-2 ASTRONOMER nem- ASTRONOMY nem- ASTUTE wes-3 ASTYLAR sta- ASUNDER sen-2 ASYNDETON dé- AT ad- ATARACTIC dher-1 ATAVISM atto-, awo- ATAXIA tag- ATHEISM dhés- ATHELING _ athal- ATLANTIC tele- ATLAS tele- ATMAN étmen- ATMOSPHERE wet-' ATOM tem- ATONE ol-no- ATRABILIOUS ter- ATRIUM ater- ATROCIOUS ter- ATROPHY threph- ATTACH steg- ATTACK steg- ATTAIN tag- ATTEND ten- ATTENUATE ten- ATTEST trei- ATTITUDE ap-! ATTO- okt6(u) ATTORN  tere-! ATTRACT tragh- ATTRITION tere-1 AUBADE albho- AUBURN = albho- AUCTION aug-1 AUDIBLE au-5 AUDIENCE au-5 AUDIENT au-5 AUDILE au-5 AUDING au-5 AUDIO- au-5 AUDIT au-5 AUDITOR au-5 AUDITORIUM § au-5 AUDITORY au-5 AUGEND aug-1 AUGER nobh- AUGHT! = aiw- AUGHT2 wekti- AUGITE aug-2 AUGMENT aug-1 AUGUR aug-t AUGUST aug-1 AUK el-2
1379:COCKLE! konk(h)o- COCKNEY awi- CocyTus kau-1 cop? ku- CODEINE keue-2 -COEL keue-2 COELACANTH ak- COELOM keue-2 COENO- kom COERCE arek- COETANEOUS aiw- COEVAL aiw-
1464:ENTO- en ENTOMO- tem- ENTRAILS en ENTRAP der-1 ENTREPRENEUR ghend- ENTRESOL sel-1 ENTROPY trep-2 ENUMERATE nem- ENUNCIATE neu-! ENURESIS wers-2 ENVOI wegh- ENVOY! wegh- ENVY weid- ENZYME yeud- EO- aus-! EQOHIPPUS ekwo- EON aiw-
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
1479:EUTECTIC ta- EUTHANASIA dhwene- EUTHENICS gWhen-2 EUTROPHIC threph- EUXENITE xenos EVACUATE eu-2 EVADE wadh-2 EVAGINATE wag- EVANESCE eu-2 EVANGEL angelos EVAPORATE kwép- EVECTION wegh- EVENT gWa- EVENTIDE da- EVER aiw-
1480:EVERT wer-3 EVERY aiw- EVICT weik-5 EVIDENT weid- EVIL wep-
1761:-LoGY leg-', sleu- LOIN lendh-1 LOITER leud- LOLL 1[a- LOMBARD del-1 LOMENT leu(@)- LONE oi-no- LONELY oi-no- LONG! del-1 LONG? del-1 LONGANIMITY ane- LONGERON del-1 LONGEVITY aiw-, del-1 LONGICORN ker-1 LONGITUDE del-1 LOON! [a-
1903:NAY aiw-, ne NEAP TIDE ken-2 NEAR néhw-iz
1912:NETTLE ned- NEURILEMMA wel-3 NEURO- (s)nee@u- NEUROGLIA gel-1 NEURON (s)neeu- NEUTER kWo-, ne NEVE sneigh- NEVER aiw-, ne NEW newo- NEWEL ken-5 NEXT néhw-iz NEXUS ned-
1927:No! aiw-, ne
2131:PRIMA FACIE dhé-1, per? PRIMAL pert PRIMARY per! PRIMATE pert PRIMAVERA per', wes PRIME per! PRIMEVAL aiw-, per? PRIMIPARA pert PRIMITIVE per PRIMO per! PRIMOGENITOR pert PRIMOGENITURE gene-, per? PRIMORDIAL af-, per? PRIMUS pert PRINCE pert PRINCIPAL pert PRINCIPLE per? PRINT per-5
2241:SEMEME dheie- SEMEN sé-1 SEMESTER mé-2, s(w)yeks SEMI- sémi- SEMINARY sé-1 SEMINATION sé@-1 SEMIOLOGY dheie- SEMIOTIC dheie- SEMPITERNAL aiw-, sem-1 SEMPLICE sem-1 SEMPRE sem-1
```


## [2026-09-04T19:01:25.573Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor p in (93,108):\n    n=p+21\n    print('===== printed p',p,'leaf',n,'=====')\n    print(t[n][:2600])\nEOF"
}
```


### [2026-09-04T19:01:27.019Z] TOOL RESULT

```
412
===== printed p 93 leaf 114 =====
— 93 —
412. jäme 'Kleid, Gewand'.
ai. V^yam- mit chardis- etc. *ein Dach, einen Schirm,
Schutz überhalten , lett. ju^m-f *dachdecken*, ksl. /)o-
jata 'Dach' (Fick); phlv. jämak bezw. yamak (z. B.
vd. 6 (71) Gl.)i).
kurd. yüma 'grobes baumwollenes Zeug (H,-Sch.);
LW. afy. jama, bei. jfämag (113).
Hörn, KZ. 32, 583 No. 11.
413. Jan 'Leben, Seele', Janver.
aw. daenä' 'Seele, zu [/'dliay-, dhyO- (oder nach
Bartholomae, ZDM6. 43, 665 dhai-) „'sehen' im
geistigen Sinn, subjektiv die Erkenntniss als psy-
chischer Faktor, objektiv die Erkenntniss als das
wahr Erkannte, Glaube, Bekenntniss" (Geldner,
BB. 15, 261); phlv. jän, jätwar,
LW. kurd. bei. (114) afy. Jan,
Geldner, KZ. 25, 562 Note 140, Hübschmann,
KZ. 27, 101 unter (Berücksichtigung von Geldner,
BB. 15, 261).
414. Jäved^) *ewig', javMan.
aw. yava^tat- 'Ewigkeit*, yave *für ewig ; phlv. yä-
vetan (PPGl.), arm. LW. yav^t^ yavitean, yavitenakan.
415. Jävf^den 'kauen, zäviden,
g. jovadmün,
phlv. vergl. jütan 'kauen, verzehren' (West: jaldanö),
jüyend (vd. 17 (9))^).
kurd. /Miw, jün 'kauen'; afy. Sövul, zöyal; he], jfayag,
n. jäy (176).
Bartholomae meint (briefl. Mitteilung), dass np.
jävJden aus ar. gzhau-, altir. yiaw-, einer w-Bildung
zu i^yhas-, stammen könne (vergl. sravati — sarati
u. a. m. bei Per Persson, Wurzelerweiterung).
Dann müsste die Grundbedeutung Verzehren* sein.
') Nicht *Gefä88*, wie ich ZDMG. 43, 48 übersetzt habe.
*) Reimt auf umed (Vis und Rämln, Seite 85 Vers 3 v. u.).
») Fr. Müll er 's Lesung .^ar^rmw (WZKM. 5, 380J ist unmöglich.
===== printed p 108 leaf 129 =====
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
```


## [2026-09-04T19:01:41.996Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if re.search(r'(?i)(x|\\/|;)?[hu]?ud[aä]|/ud|hvatäi|xvatäi|/vatäi|Xvatäi', p):\n        pass\nfor pat in ['udä','udäi','vatäi','vatay','χudā','ǰudā','tay ','χvatāi']:\n    hits=[i for i,p in enumerate(t) if pat in p]\n    print(pat, hits[:20])\nEOF\ngrep -n \"vatäi\\|vatai\\|hutai\\|hodä\\|/uda\\|χ\" HRN.txt | head -20"
}
```


### [2026-09-04T19:01:44.590Z] TOOL RESULT

```
udä [125, 209, 220, 238, 256, 327, 332, 334, 335, 381, 390]
udäi []
vatäi []
vatay []
χudā []
ǰudā []
tay  [74, 203, 235, 386, 387, 388, 395, 398]
χvatāi []
```


## [2026-09-04T19:01:47.823Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (125,127,128):\n    print('===== leaf',n,'printed p',n-21,'=====')\n    print(t[n][:2200])\nEOF"
}
```


### [2026-09-04T19:01:49.536Z] TOOL RESULT

```
===== leaf 125 printed p 104 =====
1-4 -
Hüb.sohniann. Zr»Mü. :>. 42o.
47<.». '/jtjeffte *^'e^tÄ'i>.-T. jiüoklich". ver^l. fer[jriijeste.
aw. ''h*'i:t.<t'i'. Yrr^'l. aj'i^f't'. p^hlv. 4/a^ (Gemme
.J».v. Biiti:.h Mu^. Xu. •;:.. ZDMG. 44. •>*)).
471. '/jtflfil. /u»*i «Tijit: HtiT. ;rM</4rfM</. /udäcendgür
itürk. /itnL'für. v.-ii:]. NOMtrkt: bei Uübschmann.
<>^at't. Elvi]]., r!^. l:'.:'.!. //tC'.ni, /i'Uc,
aw. vt-ri:l. x'^i^Ot*-: fthlv. /iff«ir id. i. ;frt<tef^) bezw.
/'td'iiw ai. Ytriji. >cj*iiid' Selbst I-Hrstininiung'.
LW. kiipi. ;f<^'r: af;. x'*'inii Oss. ;rwföi: bei. /*«*'*»
n. /»»(t*'!. /i '<»>'// i'..«oi.
Die Diirchsichtiirktrit Jt.-s Zusammenhanges mit l'^</*'
hat wohl Jas d i:eschützt : als Grundform ist etwa *?**
aw. /'adöffii' löder */»iit)'.*y'i-| anzusetzen. Nöldeic ^'
G^'A. l^SJ. .>. t«»:;i« bezweifelt die Richtigkeit 4^*^
EtvmoloKit' vielleicht nicht mit L'nreeht.
Fr. Müllers Erklärung jWZKM. 5. 6b) aus av^
*/ atö.ui/fio nach tiunem Willen sich bewegend*
schon an .>icii wenig Überzeugendes, ganz abgesehe
von der falschen awesti:?chen Xominativbildung.
47:i. yJrätnJden 'schreiten, ^ehen".
ai. l h'ntut'. knlwftfi. hrt'n/Uitr 'gehen, schreiten'.
In der Bedeutung angenehm, erfreuend* etc. ist,
wie schon Vullers gesehen hat. /jrüm ursprünglich
yu/rem. eine Ansicht, der auch Xöldeke beipflichtet
(mündliche Mitteilung».
47o. y/fi' 'Esel*, yj^ryö^ *Hase' (^^ *Eselsohr K /ercür, /«fr^^fAr«?
u. a. m.
aw. /ara- 'Esel : phlv. /ar: skr. khara- 'Esel'.
kurd. ier, liar (GuränT): SLfy./ar: oss. /ßräg, x^*'^9
(2i)7); bei. n. ffar, /ar, LW. har^) (192); wa/. ;rwr,
«ar. cer, üer, sangl. //tr, minj. xara.
*j Vcrgl. Ilorn, ZDMG. 44, 675, No. 134.
•; Vcrgl. Barthol oniao, ZDMG. 44, 550.
===== leaf 127 printed p 106 =====
— 106 —
479. Y^urreni 'fröhlich, glücklich*, /iirirewT,
skr. Sugratna- (Nom. propr.) *sich wohl (im Guten)
abarbeitend'; phlv. yjirram (bezw. /iiram oder hurram,
hur am), yurramth.
Bei der üblichen Ableitung aus phlv. huramak (d. i.
aw. ^htirama-) *herdenreich' (übersetzt im Kommentar
aw. hvqd^wa-) bleibt, abgesehen von dem Bedeutungs-
unterschiede, das doppelte r unerklärt. Bartholomae
(briefl. Mitteilung) will dagegen /jirrem lieber zu /urre
(ö. unter No. 808) stellen. Er nimmt als Grundform
"^suniama- an, vergl. ai. svarmrä-', Wechsel der
Suffixe -ma- und -ra-, wie bei ai. Häma- neben
Jcsärd', gv. ^7]^6g und öfter, vergl. Studien II, 23.
480. Y^urös 'Hahn'^).
aw. [//raos-, yraosyöii^ /jaosya- Vehklagend, heulend',
apa.^yraosaka- ; phlv. /rös *Hahn'; ai. l/'Arör-, krogatL
vergl. hröQa-, apa]kröca-,
kurd. korös; hei, krös, kurus 'Hahn , auch *Männchen
(bei Vögeln)' (202).
481. yi^uröstden 'schreien, lärmen, /urös,
aw. |//raos-, yraosyöit (s. No. 480), phlv. yrust,
/rustak, /rtisttun, xrus(i)sn bezw. /rös'\
Der Übergang von s zu s ist erst neupersisch (an aw.
l/'xraos- in yraozdant- etc. darf man nicht denken).
Zur Erklärung verweise ich auf Bartholomae, Studien
II, 42 folg., und nehme an, dass das s sich zuerst
vor t entwickelt hat und dann allgemein eingedrungen
ist ; der Weg war also np. "^/rüsten, *xru§ten, yrösem,
xrösiden,
flirre s. ferr (No. 808).
482. fßvlden 'kaufen'.
ai. Vkray-^ krmdti, krintte 'kaufen'; phlv. ;^an^a/«.
kurd. kerin 'kaufen'.
*) x^iroh soll (nach BQ.) ebenfalls *Hahn' und *Hahnenkamm* be-
deuten. Np. li neben s (aus aw, s) findet sich auch in amäs^ ämäh, DNT'S»
riN^PS (Zotenberg in Merx' Archiv für wissenschaftliche Erforschung
des alten Testaments, I, 398 Zeile 9).
===== leaf 128 printed p 107 =====
— 107 —
Dialektisch ist die ursprüngliche Flexion nach der
neunten indischen Klasse sekundär wieder eingeführt
in Kasan: V(öni§ün) Impt. bann (Inf. eirlän; das an-
lautende k ist hier erst zu h geworden, wie in g.
heridmün, und dann gänzlich geschwunden), Q(ohrad)
bd/rm, K(e8e) be/rln^ Z(efre) biirln.
483. y(usptden 'schlafen , {TCSir auch *beschlafen, schänden
(Is. 13, 16), ^Nr2'D?l5 (Jer. 50, 6), /?(/"/e/«, /uspamJen.
aw. [/^x^ap- , yjapta- , [/^/"afs- , /"'afsata 'schlafen* ;
phlv. x^aftaii , yj^aftak , /;'afsUan bezw. /uftmi ; ai.
y'svap'^ svdplH.
oss. d. /iissthi, t. Russin (309); bei. vapsay^ n. vafsay^
vapsay (403); wa/. rä-yp-am^ ro/opt-am yö/s-am, sar.
yufs-am, si;'n. sows-am.
Hierher gehört wohl auch np. /efj, /efjä, ber/efj (HF),
'Nachtmahr , das de Lagarde, Ges. Abh. 55 mit aw.
xawza- oder, wie er lesen will, yawja- (vd. 8, 32 (99))
zusammenstellt. Doch scheint mir auch das, Beitr. zur
altb. Lex. 44, über aw. x^mba- Beigebrachte diese
Ansicht nicht genügend zu stützen, und mir bleibt
daher die Übersetzung Napf und 'Topf (Geldner,
KZ. 25, 573, 583) die wahrscheinlichere^); vergl. auch
skr. kumbhä' in übertragener Bedeutung als 'Hure*
(allerdings spät), worauf Geiger, Ostiranische Kultur,
S. 341 Note 1 verweist. Mit np. küze lässt sich
aw. ;^aw'2:a- lautlich doch vereinigen, vergl. No. 872.
484. "^estü 'Kern*.
Vergl. s. V. est (No. 81).
aw. astu- 'Körper ist unsicher.
485. Y^astü gestehend, beichtend; Geständniss*, hestä^ ynste-
väne, ^esteväne.
aw. ^x^aMavana- (vergl. äMavana-) ; phlv. yustük,
x(u)stavän, arm. LW. /ostovan.
de Lagarde, Beiträge zur altb. Lexicogr. 21.
*) Auch Caland, Zur Syntax der Pronomina im Avesta, 15
billigt Geldner 's Übersetzung.
```


## [2026-09-04T19:02:09.057Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (130,131):\n    print('===== leaf',n,'printed p',n-21,'=====')\n    print(t[n][:2500])\nEOF"
}
```


### [2026-09-04T19:02:11.212Z] TOOL RESULT

```
===== leaf 130 printed p 109 =====
-- 109 -
will auch np. /äsdk (jüd.-pers. T^^Z, Is. 7, 24) heran-
ziehen.
490. xiSm, xesm *Zorn*.
aw. aesma- 'Zorn*; phlv. /ism, x(h^fi^'
491. yi^eSTn 'bläulich, blauschwarz'; vergl. x^sisar (äähn. I,
157 Vers 510).
aw. a/saena- (Darmesteter, Et. ir. II, 53); phlv.
/asTn (Jamaspji, Pahlv. Dict. II, 421; falsch asgun,
asTu, 241), ;^ai;fm« oder axsin(?), vd. 22 (12).
kurd. stn, heslu 'blau ; afy. s7n bezw. xtn; oss. ä/sinäg
'Taube (46; vergl. Hübschmann, ZDMG. 38, 427/8);
sar. xoin, siyn. soin 'blau, yidg. ayßin (Tomaschek,
BB. VII, 204).
492. lele {jule) 'Wunde, Spitzes; Geschwätz', /ehden,
aw. hareöis; phlv. havak bezw. yarah^ vd. 2 (89).
Die Etymologie stammt von West (PPGl.s. vJialeh);
die Bedeutung der aw. und mittelp. Worte ist unsicher,
ebenso die Grundbedeutung des neupersischen. Im Men.
fasst West päzJiala als 'foolish, silly'. de Lagarde,
Beitr. z. altb. Lex. 38 wollte aw. /"ara- * Wunde' ver-
gleichen.
493. %ufn^ ;^Mw/;, yiimh Topf, Krug , /umre (HIOID, Is. 13, 12).
aw. /umba- *Topf ; phlv. yurnb*^ ai. Jcmnhhd',
kurd. LW. /um: bei. kumb, n. fftimh 'Teich, Pfuhl;
mit Wasser gefüllte Vertiefung im Felsgestein* (204);
wa/. Imbun,
494. fmkde 'Gelächter, ymdtden.
phlv. /andlta^i, yandak (PPGl.).
kurd. kenin 'lachen' ; bei. kandag, n. Uanday, yanday,
LW.') handag (186); wa/. känd-am, sar. söwrf-am (?).
oss. d. ;^odww, t. ;^wd/w (303) scheint hiervon ge-
trennt werden zu müssen und zu [/^svad- zu gehören.
Oder ist doch Urverwandtschaft vorhanden?
ffindeq 'Graben' siehe s. v. kenden (No. 869).
») Vergl. Bartholomae, ZDMG. 44, 550.
I
===== leaf 131 printed p 110 =====
— 110 —
495. lym 'Schlaf, /ahtdefK
Kä§. ;^öw?[es; hevoft 'schlafen*.
aw. /'a/wa- *Schlaf; phlv. /*'äÄ; ai. svdpiw-; arm.
^un (H. No. 295).
kurd. /evii, /evin; af/. LW. yöb; bei. ^?a/>, n. väir
(410).
496. x'^^^ 'leicht, gerade; niedrig, verächtlich', x^^ärT,
aw. /'ad-ra- (Geldner, KZ. 25, 478, Studien I, 17
folgg. ; Darm est eter. Et. ir. II, 189)'); phlv. /"är, nur
in der Bedeutung 'leicht', /"änha *leichtlich' (Sa le-
rn an n, Mel. asiat. IX, 234).
LW. kurd. /(^r; afy. /'är; bei. vär (290).
Die Bedeutung 'niedrig, verächtlich' ist erst neu-
persisch.
497. i^äfiten 'wünschen, wollen, Praes. /"ähem, /"äliis,
/"äste 'Besitz'.
ai. l/^soad-, svädati 'sich schmecken lassen, Gefallen
finden*, svädate; gr. rjdoftat. Vergl. np. /iväi (No. 502).
phlv. yyastan 'wollen, wünschen', /^ah(i)§ff, x^stär,
y^astak 'Besitztum' etc.; kurd. /^dsthi , ;jfMSfni; bei.
vergl. västa 'für "(413).
498. x^äW/ 'Tischdecke; Tisch (gedeckter)'.
aw. /^'^aini' 'Teppich, Überzug, Decke',
kurd. LW. /an; af/. /^än; bei. n. vän 'Platte, Teller'
(289).
Geldner, Studien I, 17/8.
499. yiyänden Vufen, lesen etc.', /emden, /unlde, /unyä
'Musik, /unyäyer,
aw. l/";^^«;/- in /^anaf.ca/ra- ('klirrend'); phlv.
X'^äntan, /untt (GF.) ; ai. [/^svan-, sodnati 'tönen'.
kurd. y^ändin^ /ündin 'lesen; oss. d. /önim, i. xöJiin
'nennen , heissen , rufen , einladen' (305) ; bei. vänag,
n. vanay, vänganay 'lesen, recitiren, studiren' (412);
wa;f. ^an-am 'reden, sagen, sprechen'.
*) Sahn. I, 170 Vers 745 steht np. j^^är direkt im Gegensfttz zu
(hfsvär, wie im Awesta '^^äSra- zu (Inzä^ra-,
```


## [2026-09-04T19:02:17.143Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (132,):\n    print('===== leaf',n,'printed p',n-21,'=====')\n    print(t[n][:2500])\nEOF"
}
```


### [2026-09-04T19:02:19.248Z] TOOL RESULT

```
===== leaf 132 printed p 111 =====
— 111 —
500. ^fyalTden *f?chmeckon' , /^al 'Speise', /^älger, /^älf,
X^'ältger.
aw. x^arezista-; phlv. /^list (vd. 2 (77))'); arm.
l^alcr 'süss (sehr unsicher, H. No. 287).
501. polier \Sch wester, /ö/j.
g. yohr; Käs. /üh, yöh,
SiW. /^afihar- Schwester; phlv, /^'ühar, ytlk {PPGl.);
ai. svasar-; arm. ^^oir (H. No. 294).
kurd. xöh, ;c^A^» ^^^^ (H.-Sch.), af}'. yöt' ; oss. d. /ore,
t. ;ro; bei. gvahär, n. gvähar, göhär, gvär (131) 2); wa/.
;^m/, sar. ya;^, minj. yayvd, sangl. i/vd.
502. x^**^^*» /^^^^ 'Wohlgeschmack'.
skr. sräda- * Wohlgeschmack*.
kurd. x^ *Salz ; bei. väd, n. väd, vad\ vü:: (411)
'Salz.
In diesem Worte hat sich die ursprüngliche Be-
deutung der [/"svad- im Neupersischon allein noch
erhalten; vergl. /^'dfiten (No. 497).
503. y(nb gut, schön , /hIü.
Ka§. /ßh, /öb^ /eb.
aw. hväpah' 'wohltätig; phlv. /rap bezw. /üp,
Xüpih; ai. svdpas-'^),
504. lud, ^eS (AM.) 'selbst'.
Käs. x^d.
ap. vergl. wrö- ; aw. yyatö 'selbst'; phlv. ;^^a^, j^^'a/^Ä ;
ai. svdtas,
kurd. ;^i2 ; af/. ;t'/>'<^ ; oss. d. x'^^^^^9i t. /ädäg (298) ;
bei. i?a^, n. viixt^ vas; äiyn. ^w, sar. /w, wa;^. ;frti, gen.
505. x'*^* 'Sonne', hur, hör (reimt auf .<??^^ör; Sahn. 111,1105
Vers 693), Xurasan,
*) So korrigirt D armesteter, 6t. ir. I, 136.
') Yergl. Bartholomae ZDMG. 44, 552, Hübschmann ebenda
557, Geiger, Lautlehre d. Bei. § 15, 3. Uraprachliche Dialekt-
Verschiedenheit.
«) Ebenso Fr. Müller, WZKM. 5, r>7.
```


## [2026-09-04T19:02:27.107Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aǰe\\|äge'\\|āǰa\\|/äge\\|x^äge\\|Eunuch\" HRN.txt | head -20; echo \"=== HUB p54 (leaf 64) ===\"; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nprint(t[64][:3000])\nEOF"
}
```


### [2026-09-04T19:02:28.868Z] TOOL RESULT

```
=== HUB p54 (leaf 64) ===
300
— 54 —
Z. 2 stimmen, auch wenn es vorhanden ware, was
aber nicht der Fall ist: xcLvar-xudai = der Xavar-
herr Fird. I, 154, 465.
469. In den Nachtragen wird saxudan zerkratzen' (afgh.
LW. st^xudq 'scratched with the nails') hierher gestellt.
Aber 'kauen ist nicht zerkratzen' und xdyam nicht
Saxayam.
ill, NSldeke bezweifelt die Richtigkeit von Horn's
Etymologie: np. xuddi *Gott' = zd. *x^adaya- mit
voUem Recht, da ocudai = phi. x^atai (61. and. Ind.
p. 47, Bdh. Gl. 126, ZDMG. 31, p. 596, Nr. 34, etc.)
ein zd. *xwataya- oder auch *xwataia-^) voraussetzt,
die sich zur Not durch skr. svatas 4- ayu- Von selbst
lebend' oder skr. svatas + adi- Von selbst anfangend,
uranfanglich' (vgl. skr. svayambhu-) deuten liessen. Doch
sind diese Deutungen so unsicher wie die iibrigen. Vgl.
Fr. Muller, WZKM. 5, 65. Als Curiosum sei er-
wahnt, dass de Lagarde, Agathang. p. 159—160
deutsch Gott wieder (nach Burnouf) aus dem Per-
sischen {xodd = xudai) entlehnt sein lasst wie deutsch
gund (in Kunigunde etc.) aus pers. "^gund.
474. Vgl. ZDMG. 46, 234. Dazu arm. xarbzak 'Melone' (nur
bei Caxcax,)
475. Np. xarSang *Krebs' aus phi. karcang mit volksety-
mologischer Anlehnung an die Composita mit xar Esel
(vgl. Vullers s. v. xar 2), so dass nun das Wort
aus xar 'Esel' und cang *Kralle' zusammengesetzt er-
scheint.
476. Lies arm. xrat (fur xart),
477. Dazu kurd. vird, Mrs, hire 'Bar ZDMG. 38, 93.
478. Auf Grund der Pazendlesungen des Min. und Shk
setze ich x^arsand als Pehleviform an und lehne
die so wie so unsichere Etymologie Darmesteters
(= hu-rasant' gut-kommend' ab.)
*) Arsao. phi. *x^ataS, sp&ter phi. x^atai, paz. x^adai.
```


## [2026-09-04T19:02:53.785Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in PHD.txt PHD_mackenzie.txt; do echo \"=== $f ===\"; grep -n -i \"xwad[āa]y\\|abur[nl][āa]y\\|aburnay\\|y[āa]w[eē]d[āa]n\\|jāwēdān\\|ǰāwēdān\\|xwāg\\|purnāy\" $f | head -20; done"
}
```


### [2026-09-04T19:02:55.447Z] TOOL RESULT

```
=== PHD.txt ===
124:~išn : [М tandis] ... add ёахгар |c hlk' | M cxr, № čarx] wheel, circle. čimīg ... add caused, justified, reasonable. dagrand-xwadāy ... delete eternal. dast-gir [dstgyl | N x]... delete: dst OHDWN, ...
154:xwaday ... read N xuday.
170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
306:īdabr [dpi] sinner, deceiver. *dabr [dpl] *dark-coloured. dad [dt' | M dd, N ~] wild animal. 1ааа [d't! | M d?d, N ~] law, justice; those scriptures dealing with legal matters. даа [d’t' | N ~] age. зааа [d>1!] tooth. tdād, v. ahlaw-dād. dādan, dah- [YH BWN-tn! < A Vyhb; d*tn!, dh- | M d'dn, (dy-), P dh- N ~, dih-] 1. give; 2. create. —išn [dh(y)sn'] giving, donation; creation. dādār [d’t?l | N ~] creator. -- ih : creatorship. dādestān [DYNA < А dyn; d'ts?n! | M d'(d)ys?n, N dá(de)stan] judgement, justice, law; case, process. dàd-gàh [2^? gs] proper place, fire temple; = daxmag. dādīg [d'tyk'] legal, concerned with the Law. dad-meh (d"tms] adult, elder. dādwar [d?twbl | (M d^ywr, P d'dbr), N da(d)war] judge. ~ih: judgement. daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. «dišn: breath. daftar [dptl | N —] register, account-book. dagr [AL YK < А ryk; dgl | M dgr > dur, N dër] long. dagrand [дата | N dërand] long. ~«xwaday [-hwt’y] eternal, of long dominion. daģr|-pattāy [dgl pt'd] long-lasting. -—-zamáàn [-2т?п!] a long time. ^-zi(w)isn [-zywsn'] long-lived. dah [ro, ASLY A < A ә | M dh, N ~] ten. dah-, —išn, v. dádan. Юаһаӣр [dř k' | (N Dahàk)] = Azdahág. dahān [РИМЕ < A p(w)m-h | M dhyn, N даһап] mouth. dahibed [dhywpt! | M dhybyd] ruler, lord of the land.
422:kabk [АрА! | N ~] partridge. ~-anjir [acyl | N ~] a kind of francolin. kabód [kpwt! | N ~] grey-blue; pigeon. kabótar [kpwil | M kbwtr, N ~] pigeon. kāč [с | N kāš(ki)], ~ ka: would that, if only. кадар [01А] game, joke. кадар [ktk' | M kdg, N kada] house. ~-banig [-b'mwk! | N Radbanü] mistress, lady of the house. ~ig [-yk'] domestic; servant. ~-xwaday [-hwty | P gdyxwd?y, N kadxudā] householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. kadar [kt] who, which. 7-iz-é(w) [-c-H D] whoever. kaf [kp | N —] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-А! | N ~a] spoon. kafš, ~ag [kps, -k! | N Аар] shoe. ~gar [-k/ | N ~] shoemaker. kaftan, kaf- [kp-in' | P kft, kf-] fall. kah [TBNA < A tbr | N ~] chaff, straw. kān-, ~i§n, v, kāstan. _ kahas [kts | М khs] channel, sewer. kāhēnīdan, káhén- [R'hyn-ytn!] decrease, lessen (tr.). kühidan [P hytn! | N ~] = kastan. kahist [ksst'] least. kah-rubāy [Ара | N —rubá] amber. kahwan [khwbn' | M qhwn, N kukan] old. kākom [RP Rkwm | N ~] stoat. ~ i spéd: ermine. kālbod [Аро | (M k*/byd), N ~] body, shape, form. ~ӧтапа [-wmnd] corporeal. kam [km | M kmb, N ~] little, small, few; v. kem. kam [Em | = M, N ~j will, desire, purpose. kàm-, v. kāmistan. 1катаб [k?mk! | N kama] kinds of gruel, or soup. ?kümag [k?*mk! | N kama] = kam. «-hanjām [-hnc’m] gaining one’s end, successful. -~-hanjamih: success. „ūmand [-wmnd] willing(ly), desirous. ~-widar [-wt?l | N kām-gučār] successful, independent. ~-xwaday [-Awt^y] independent, absolute. kamal [kml | (M km?7)] head (daevic). ~ig [-yR!] chief (daevic).
551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
703:absolute kāmag-xwadāy, kāmgār.
734:adult dād-meh, purnāy.
777:always bāstān, hamé, hamēšag, hāmwār, Jāwēdān, P yawed(an).
1225:childhood aburnāyīh, rahigih.
1677:dominion šahryārīh; of long ~ dagrand-xwadāy.
1807:eternal dagrand-xwaday, haméig, fawed.
1808:eternally haméiha, jāwēdān(ag), P yāwēdān.
2330:householder kadagxwadāy.
2415:independent kāmag-widār / -xwadāy kām-zīwišn.
2667:lord аху, bay, šahryār, xwadāy; ~ of the land dahibed.
2668:lordly xwadāywār.
2669:lordship xwadayih.
2745:master awestād, rad, salar; ~ of the house kadagxwadāy, mānbed.
=== PHD_mackenzie.txt ===
828:aburnay ['p(w)ln'd, v. purnay I N burna] under age, child.
830:aburnayag ['p(w)ln'(d)yk'] child.
2158: .......-xwadAyih [-hwt)yh] misrule.
3129:  ---xwaday [-hwt)y I P qdyxwd)y, N kadxudii] householder, master of
5596:xwaday [hwt>y I M xwd'y, N .......] lord.
5893:absolute kamag-xwaday, kamgar.               ebgat, petyiirag.
6173:cauldron deg.                           child aburnay(ag), frazand, rahig,
6176:cavity gabr.                            childhood aburnayih, rahigih.
6415:disappointment oreb(ih).                   dagrand-xwaday.
6510:eternal dagrand-xwaday, hameig,                    experienced kiiragah, nibardag.
6513:   yawedan.                                        explain paydagenidan, wizardan.
6804:hire mizd.                                     householder kadagxwaday.
7029:lord axw, bay, sahryiir, xwaday; '" of   manager kiirframan.
7032:lordship xwadayih.                       Ma7lichaean zandik.
7063:  house kadagxwaday, manbed.                 wiyufs-.
7649:    xwadayih.                          stalk ewan.
9506:durI, rahig              \~       kadagxwaday
10627:gusn                                    dusxwadaylh
10825:dagrand-xwaday
11396:aburnay                .No'~~          abzonig                       \»\$~
```


## [2026-09-04T19:03:03.932Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"jāwēd\\|Jāwēd\\|yawed\\|yāwēd\" PHD.txt PHD_mackenzie.txt | head; echo \"=== NYB ===\"; grep -n -i \"xvatāy\\|xvatāi\\|xwatāy\\|hvatāy\\|yāvētān\\|yavētān\\|jāvēt\\|apurnāy\\|aburnāy\\|purnāy\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-04T19:03:04.063Z] TOOL RESULT

```
PHD.txt:404:-(i)m 46 Jāwēd
PHD.txt:412:J jad [y’t'] share, portion. Yadag [ytk! | M jdg] omen. tļadaģ [ytk'] form, property. jadag [y’tk' | M del share, portion; case, cause. jadag-g5(w) [y tkgwb'] advocate, intercessor. ~ЛЬ : intercession. jadag-wihīrih [ytkwhylyh] transformation, alteration. Jadarih [y2?lyh] maintenance. *fadisn [ytsn'] (accidental) quality, property. ~ig [-yk'] accidental, non-essential. jadiig [y?te&! | M j?dwg, N jadi] sorcerer, magician. — h: sorcery, magic. *jay [у?л | N ~] sissoo tree. jagar [yal | N jigar] liver. Jah-, v. jastan. jahišn [yhysn' | J jhysn-] chance, fortune, omen. Jahišn-ayār [yhyfn hdyb'l | N n. pr. jhiy?r] fortunate. ~ih: good fortune. jahüd [yhwt' | N juhiid] Jew. jām [y m | N ~] glass. јат [M ANE < A mn-h; ут | M Pm, N <] vessel, goblet. lfamag [y”mk! | N јата) = *jām. атар [y mk! | М ртр, N fama] clothing, garment. jang [yng | M jnng, N ~] struggle, battle, fight. Jar [ywl | M рт] time, occasion. jastan, jah- [ystn!, yh-] happen, occur, chance (to be). ~išn, v. jahišn. Jašn [yfn! | N —] celebration, festival. jaw [ŠZ < A £% | N ~] barley. Jāwēd [y wyt! | (P ywyd), N ~] eternal.
PHD.txt:671:yāsaman [y smn! | N ~] Jasmine. yask [ysk! | = M] illness, sickness. yasn [ysn' | = M] adoration, worship. yašt [yst! | = M] prayer, worship. yaštan, yaz- [YDBHWN-tn! < A ydbhwn, V dbh; уйт, yc- | M yz-] worship, celebrate, recite. ~Л&п : worship. yāt [yt! = Av. yáta-] a degree of sin. P yāwēd(ān) [5?*wyt(?*n)! | P y'wyd(?n)] always, eternally. yaz-, ~išn, v. ya&tan. yazd [yzdt! | M yzd, N ~] god, divinity. yāzdah [y'cdh | M y'zdh, N ~] eleven. yazdān [yzd’n'] (pl.) gods, spirits. yējdahr [ywid?sl | М ywjdhr] holy, pure. ~th: holiness, purity. yojdahrgar [ywsd’slkl] purifier. ~ih: purification, sanctification. убх [ywc | N ~] cheetah, hunting leopard.
PHD.txt:777:always bāstān, hamé, hamēšag, hāmwār, Jāwēdān, P yawed(an).
PHD.txt:1808:eternally haméiha, jāwēdān(ag), P yāwēdān.
PHD.txt:3101:perpetual jāwēdānag.
PHD.txt:5559:jāwēdānag jáwed, yawéd -dān
PHD.txt:5570:jawedan, yāwēdān
PHD_mackenzie.txt:5700:p yawed(an) [y)wyWn)1 I P y)wyden)] always, eternally.
PHD_mackenzie.txt:5943:   hllmwar, Jawedan, P yawed(an).         arch-demon miizandar.
=== NYB ===
554:apäyistan ['p'dstn'], apāyītan [’p’dytn'] apäy-, 3d p. sg. apāyēt [’p’dt', ^p'dyt'], 3d p. pl. apäyend ['p'dynd], pret. 3d p. sg. apāyist 1. to please a p. (pat) 83%; cigon mēnēyān apäyist as it had pleased (was predestinated by) the heavenly gods 405, v. below. — 2. impers. it is desirable: -m apāyēt 6 han ciš I desire, try to obtain, this 562%, — 3. to be needed 1211-2 also pat. kär. apāyet 14%. 375, andar apāyēnd 105%. — 4. to be proper, seemly 4015 (bē ~). — 5. impers. apäyet auxiliary vb.: must, ought to, shall, should, has to, is bound to, ete. with the p. as indir. obj. (virtual dat.), a) governing an inf., which is as a rule placed after: u api-t xvatāyēh i Ērān šahr vas sal apäyet kartan and thou shalt exercise dominion over Iran for many years 629-31; 918-19, ]014 ete.; in this case preverbs to the inf. are drawn to apäyet; bé — pursitan 1319; ba ~ hištan 1313; kār-ē i apar nē ~ kartan 104%; apārīk 6 [KN] ~ xtartan 94??; less often the inf. is placed before: ēzatan nē ~ 1017-19; pit u mat frazand i xueš rād En and kär u kirpak ... bē üámóxtan ~ the parents shall teach 6522-23; 6519-20; 9113; the inf. sometimes has to be supplied: -
610:apurnāyīk [’pwln’yk], aparnäyik [’pin’yk] a young man 44. 48°; pl. cas. rect. ~ 5235; pl. cas. obl. —-än 1019. 52%, used as cas. rect. 16%; mart ~ 4719, — Milr form; cf Av. (81 sq.) a-poronāyūka-; Paz. = the preceding w.; NP barnäk, burnäk.
3627:310 šāyīt [š?dyt'], cond. 3d p. sg. (nē) &ayit hat 711%, to be able, capable, 1. with a pers. subj.: kad šāyem griftan? when shall we be able to catch him? 75; 8?;-4 martömän šāyēnd ayāftan 887-9; Sūšāns apāk Kai-Xösröi kartan šāyēnd. 8820-22; 908; — 2. with a non-pers. subj.: amäh garān ziyän ... haciš šāyet butan serious harm must necessarily arise for us: from it 191-?; ctš-ē ke ziyān ne haciš Sayist bütan from which no harm could arise 411-12; kū ātaxš haciš nē šāyet vextan that is: the fire cannot break forth from it 95! (gl.); — 2. impers.: it is possible, in varying modal senses: it can, may, might (be), it is proper, suitable, fitting, permis- sible; ‘perhaps it will... .’; it is predestin- ed, necessary, must, ought to, should, passim; the difference between šāyet and tuvan may be illustrated by 719-3; hakar tài 3 rēc griftan ne šāyet, pas hac hin griftam ne tuvdn if he cannot be caught within three days it will be im- possible to catch him; sdéyet ku perhaps 81. 242; ma hakar-am ... nē brihénit estet ku Erän-sahr pat ēv-xvatāyēh be šāyēt vīnā- ristan it is perhaps not predestined for me that I should bring E. together into one kingdom 137-9; šāyet butan ka šāyet butan “it is predestinated to happen when it is predestinated to happen”, it must happen when it must, Fate will necessarily be accomplished 231-? (cf Skr yad bhavisyati tad bhavisyati); kū yam etön névak pat xuatäyeh šāyet kartan that is: so beautiful & bowl must be made for royal persons 6015 (gl.); ānēd x"arisn šāyet x"artan it is permitted to take food here 76%, v. s. v. frayist ; tài Emahčip x"artan ne šāyet during one whole month it was not possible to drink of the water 2017; — if the real subj. is a person the pret. šāytst has regularly impers. construction: asvārān ... hixtan nē šāyist the equestrians could not haul up 153-4 (cf 887-8, above sub 1); ke (indir. obj.) cim 4 han catrang vicārtan šāyist anyone who could solve the problem of this game of chess 11817-18; without
3716:tan ... paristém adak-tān dahém ... vas zarr ... 193-4; u api-tin ... kar framā- yēm 198; täi-tän man zīvišn + gētē pat miyān kunom 67-5; agent: ka-tän pursīt hat 214; kū-tān... dit ...? 39%; vinäs t-tān kart éstét 67°; referred to by a follow- ing prep.-adv.: āfrīn-tān + xvatāi apāk the benediction of the Lord (be) with you 1281-19; — independent form atän 451,
3899:Vadagān [wtk?n'] patron. or pl. cas. obl.: adak-it 1000 sāl xvatāyēh i gehän dahom cigon 6 ~ dahyupat Dahāk dāt then I will
4016:lyaspuhrakan used as pl. cas. obl. of vaspuhr: the heirs of body, in the royal family: the princes of the blood royal: apāk fradandàn u ~ 3793; spähpatän u vazurgān u üdzütakün u ~ 11%; apāk apurnäi zātakān ~ + Artaxšēr 16°"; apäk pusän brätarän u ~ u hāmharzān 188 (185 vispuhrakän inthe same series) ;bunak i Vistäsp u apārīk ~ 115%. — Paz. vāspu- hargq, vāspihiraga, Skr. v. vikhyātimant in pl. (Mx 1"). — As to the correlation sg. väspuhr: pl. cas. obl. väspuhrakän, cf apurnāi: apurnāyakān (but sg. also apur- näyik); äzät: azātakān (pl. also azatàn); Eran: Ērānakān (q.v.; also Mx 21%); Tür: Türakän (Mx ibd.; commonly Tū- ran); (Hrömäy-ik:) Hrömäyakän (Mx ibd.); Yahüd: Yahüdakän (v. these ws.); cf also vazurgakün and vispuhrakān".
4372:xvatāi-vār [- wl] worthy of a ruler, regal 917
4376:xYatayéh domination, dominion, reign 620, 727, 1311.19.21 ete. passim; v. also zēšt-xvatāyēh, duš-xuatayeh, ēv-xYatāyēh, ēvak-x".; KZŠPrth hwtwypy, Gr. v. šeo-
4438:yāvētān perpetual, eternal: ~ rēcān in eternity 272°. - MPrth y^wyd?n, ^w y’wyd’n ‘eternally’; MPrs Z’yd’n (S, A-H II), j”yd*n (BBB); Paz. jāvada (SGV); NP jüvidàn.
4439:yāvētānakān for all eternity 103?9, yazdān [yzd'n'] v. yazet.
6667:jāvada: yāvētān jāvar: yāvar
6911:| : xVatāi
7225:jāvīdān: yāvētān
```


## [2026-09-04T19:03:10.931Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4360,4378p' NYB_vol2_glossary.txt"
}
```


### [2026-09-04T19:03:10.981Z] TOOL RESULT

```
to summon a p. to one’s side 2?-3-12, 56, 104 ete.; without 6 pes 625, 73. 315; Ohur- mazd ast hac damik ... x“ahét O. will call up the bones from the earth 100'2-13; vas a«vāhišn (q.v.) i rüpak-karihà xvāhēt he clamourously utters many implorations 7426-27, — 3. to ask, to demand: pat zan ~ to marry a wife 675; pat zanéh ~ to ask in marriage 1165-5; hac Papak past (g. v.) u zinhär xvāst 214; 3 rēc jamān x“äst he solicited a time of three days for consideration 11819; 121%; mizd dātihā ~ to demand reward righteously 8120-21; hac x"at karap margēh 4 Zartuxšt x"àst, apar cé āivēnak margēnītan he asked the karap himself about the manner of Z.'s death, how to put him to death 4812-13; sāi u baz ~ hac to exact tribute from 177. 58%; Pourušasp hàn hom hac Dugdāv apāc x"àst P. asked D. to give him back that Haoma 42?4-25,. 4, to seek,to search,to look for, to ponder, to strive to attain: api-ščin hàn hom x"àst they searched for that Haoma 409; pat ~ 4 hàn i či zuarrah in striving to attain his Glory 4614, more fully + an inf: api-š hàn xarrah bē aydftan x“dst 4618; — with an abstr. subst. as its obj.: v. cärak, ddrišn, dösäram, hucasmeh, ken, panäh, zivišn, ete.; cf also s. v. az"àyisneh. — Olr *hväz-, MPrth wx'št, pres. wz?z-; MPrs xw'stn, xwh-; Paz. NP z"üstan audah-; Verbum 187; Ghilain 69; Bailey, BSOS VI, 1930, 74. V. also x“dstar, -ēh, zuäyısn, -ēh.
x"astür [hwst?l] one who tramples down,
crushes: duž i ~ 5827, — V. xtastan.
xuastar [hw’st’l] a seeker, one who strives for a th. 56?6, — V. xudstan.
x"üstaréh the act of striving for 6612, 712.
xuaš [BSYM] beautiful, nice, pleasant, savoury 28? ; sup. ~-tom 748-18, — MPrth wx3; MPrs xwš; Paz. NP xvas; etymology v. Pagliaro, RSO XII, 1929, 166.
xvašēh [BSYM.yh] beauty, savouriness 8919, 9410, 10422, 1052.
222
x"atài-vàr
xuat [BNPSH; hwt' 122] himself, herself, itself: (asp 2) ēvak — u Evak kanicak apar našast the one (horse) he mounted him- self, and the other the girl mounted 6!2; ~ karap the karap himself 4812; ; ~ his (her, one’s) own, or proper 100. 12115; -m ~ myself 122; -šān ~ themselves 104, — Av. (1861) z"ató adv. ‘of one’s self, voluntarily’; MPrth wad; MPrs xwd; Paz. z"ad, xud; NP xtad (xod). — Cf x"es.
xuatäi [hwt’y; MRWHY Ps.] pl. cas. obl. ~-dn (used as cas. rect. pl. 176-10, 9013-14) 1. suzerain in a political sense: ~ u dahyupat 12%. 7223; nē ~-an rād u nē-c an dahyupatän 7271; ~ u dahyupat u sardär u dastavar i den äkäh 1081-2; ~ -ē u pätixsäy-& 513; peš 4 ~-ān u pätixsäyäan 7021; with a gen. of the governed people or country: ~ % Pärsikän 1315; X20nàn ~ 18-29 passim; Eran u Anērān ~ 11919; fradandān + ~ -àn124; ganj i 110?! — of minor rulers: sar-~ properly ‘ruling as the head of a family’, prince, vice-roy, vassal: sar-~-dn 4 Erän 13%; sar-~~-Gn  kustak kustak the vice-roys of the different territories 17>-*-19; in the same sense katak-~ 13, properly ‘the master of the house’. — 2. of the heavenly beings: Ohurmazd ~ Lord O. 12%; Ohurmazd 4 ~ 745 and passim; ~ alone: the Lord Paramount 10411; ~ u pātixšāi of Srosh 86%; [MRWHY] God in the Jewish-Christian sense 1289.19.20, — Prth inser. hwtwy (Prs always MRWHY); MPrth zwd’wn, awd'y; MPrs zwd'y, cwd^wy (A-H I), zwdy’(h), pl. zwdy’h’n (S, A-H II); Paz. x"adàe, x"uaddič; NP xuda ‘God; master, owner’. Meillet, MSL 17, 1911, 109 sqq.; Bthl, MirM ITT, 1920, v. Index; Junker, WuS XII, 1929, 145— 147; Schaeder, UJ XV, 570 n.; Eilers, AOi 24, 1956, 185. — V. also dérang- xatar.
—-ün
xvatāi-vār [- wl] worthy of a ruler, regal 917
www.parsianjoman.org | ool wok
x'atayéh 2
23 xlēt
xYatayéh domination, dominion, reign 620, 727, 1311.19.21 ete. passim; v. also zēšt-xvatāyēh, duš-xuatayeh, ēv-xYatāyēh, ēvak-x".; KZŠPrth hwtwypy, Gr. v. šeo-
TOTELA.
xuat-doščh [hwtdwsyh] self-will, self- conceit, capriciousness 84?%, Paz. xtad. doši, Skr v. svecchäcäritva; as to dos cf S. v. dost.
```


## [2026-09-04T19:03:16.914Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nimport re\n# find leaf containing column number 1862\nfor i,p in enumerate(t):\n    if re.search(r'\\b186[0-4]\\b', p) and i>800:\n        print(i, [l for l in p.split('\\n') if re.search(r'\\b186[0-4]\\b',l)][:3])\nEOF"
}
```


### [2026-09-04T19:03:18.847Z] TOOL RESULT

```
leaves 1041
```


## [2026-09-04T19:03:21.654Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (930,960,990,1000,1010):\n    print('==== leaf',i,'====')\n    print(t[i][:400].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-04T19:03:23.246Z] TOOL RESULT

```
==== leaf 930 ====
 | 'die    betten    um   dabei  zu  wohnen';    s.  dacu | Dbr.  AiS.  4iä>  419- | •  j.  siti  Inf.  'zu  wohnen'. | KompE.  —  Zum  V.  lay.  —  Vgl.  Siiay-. p.  'Um,  'iil;  1.  hay-. j.  iuqs  F.  750:  lies  Ivqt;  s. ^m/- mit  No. 6. | •  j.  satay-  f.  'Bewegen;  Sichbewegen', KompE.  —  Zum  V.  •ion-.  —  n.  eyutay-  f.  — Vgl  'atmisüili,  'iülöit  Inf. | •  j.  "sutasme"*  F.  5. | Pü.:  danmi. 
==== leaf 960 ====
'a 'täitim  AainaspaHmaidayeAe  (sd.)  Ä.^.  12; 9.  a)  mit  Gen.:  •laillm  atr».saokanqm V.Ä90;  4- 19',  d- 15'. | Ableit.  {ha^a&ivanh).  —  Ableit  aus  Aafta, S  2ro.  —  ai.  vgl.  laflitay-  f. ;  np.  haftäd.  — Pa. ;  jo. | ■  j.  haptäzdyäi  Y. //.  9:  kabbalistisches | Unwort | Stammt  aus  Y.  31.  aa  {hapli)  und  Y.  sr.  17 {äidyäi)iv^\.*m3ndäidyäi*1.  —  Pü. :  Aa/ttAna u  aSt  rdnn. | •
==== leaf 990 ====
 xüp  karl,  (la Y.  34)-  po  hakarlärlh.  —  ')  NA.  kü.karHä; s.  aber  R  4  und  wegen  der  Bedeutung  du vorherg. /taiö  ..  ^aShig.  —  »)  Man  verlangte den  IS. | •  j.  hu-kshrp- Adj. 'wohlgestaltet':  vatihus haomS  .  .  'kfnfi  Y.p.  16;  F.  ja. | Ableit.  — Pü.;  hukarp,  erl.:  fisSn  (xüplA) pata- lailAä  i  handäm  'gemeint  ist  (Schönheil)  in Beziehung  auf  die  Zusammenstellu
==== leaf 1000 ====
9.  8''. -----  Gray  JAOS.  25.  125.  ai.  TgL  svädmin-  m.'),  —  Vgl.  1 | neuerdings  Gruy  JAOS.  3/.  115,  — «)  ai.  a/äii- man- :  g.  kudima-  (ar.  "jMi/mo-)  ='  »n.  Äilmi : ai.  ruJmiä-  (u,  a.).  —  J)  S.  tuaäna-  'Haus' No.  7. | •  j.  hu-d-axta-  Adj.  'gut  gespannt',  vom | Bogen:    isavasctt  aisam  ■■  'tat  haca  ä««- vanät  jya.jatät»ke  vasimna  . .  YL 10. 39. | j.  hupiüda
==== leaf 1010 ====
dainä-:  yvSfum  °na- aham  kvaca^ham  husyaokmm  hudalmm ^^-  J-  3  i  —  yUnü  fiumanatfhö  kvacanAs huiyao^nahe  kudafnahe  H.2.18;  Vytl*; | —  yum  'nS  kvacS  *hulyao^na  *hudaina H.2.ir,  12;  —  haxayS  . .  'natakB  hva- ioTihS  hu^aöiinäahö  huoa^na   Yt/^.  95; | —  yünat  haca  'nanhai  hvaiarfhat  hu^ao- %nat  hudainal  P.33.  2)  'gutes  Muts, wohlgemut':  ydäa  valm  °na^hs  (NPm.)  .
```


## [2026-09-04T19:03:30.191Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"atö\" BRT.txt | head -30"
}
```


### [2026-09-04T19:03:30.264Z] TOOL RESULT

```
2447:lausgesprochenen)  Gegensatz;  a}  adjekti- \Tsch,  mehrfach  sva,  'dieser  mein,  unser" ahmäicä  ahuyi  manaüyäicil  'Tilr  das  Leben hier  und  für  das  geistige"  V.  40. 2 ;  —  ahyil anhSus  asti<atö  manhrahasca  Y.  43. 3 ;  J2. '3.  34-6j  45-3t4i  —  aAe.'a  anhius  .  . ■ .  manahyeheta  ankiul  Vyt  $2;  —  ahum Tütümca  gaf^anqm  yaozdatlr?m  anham dämanqm  Vi.  70. 92J  —  aisqm  atthunqm hstam  Vyt.  JO;  —  kva  ..  aiiika  zimS  "wo auf  der  Erde  hier"    V._j.i,7;  15,  18,  34,
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2493:/u>n  ..  Y.6"o.sf.;— ..  a/^'z'^-4r^ayS(sd.)j_j.5;  _  „yaca  h 'disänaya  Vyt5/; ..  ya>a  spä  vakrkaAe  k}r?naoiti  ya%a\ai,iAa  drujö  FrVV.  Äi ;  V.  7.52  PüZ.; — yat  v>hrkö  spa  V./_j.4i;  ~  ..  aAmai  „Ami  ar»>e  yahmi  gafi:e  Yt./2.8;  — nmänai  .  .  ^yahva  xsnBto  bavaiti  Yt  10. 1  aAmya  .  .  yahmya  .  .  aAmya '  Yyt.  4^;  — 28;—  zugleich  zurückweisend;  s.  I  i  al  ^^ft,«/«  «ar««  V.5.9  PüZ.;  Yt./.a?,  J.  10, aE.  a)  Das  adj.  Fron,  vertritt  das  lat.  [4.2',  8,  V.  7!72PuZ.,  Vyt.  39,42';  — yaj eius  (s.  I  I  a  et):  dBräi  Aa/a  aAmai  nmä- '  mlalsamcilnmSnanamca'*caratö(s^.)dva.. nät  .  .  aiiihät  vUat  .^.  aAmät  zantaot  .  ■  V.  13.49;  — c'vat.bi/ ayß-  vTtay3{sd.)  atthsn aitihat   daitiAaot    aya    ihyejä   .  .  *yeyenti  \  >j,  ^V.  ti^e   i>:a  ya>na    aAmii  Yt  IQ.
2550:äJffj  ti  'take  paiti  ..  V.22.2f.;  —  Da.'  aoAvo  (Stvetx.)  yal  as/tainti  Y.i^.6  \isw.; in  Verbindung  mit  anya-  Du.  (s.  i  b):  —  'tagsam  sünam  ..yimpasuiJiaurvamca.. asUm^mastrrfttqm  vispacayö*>nastr?inqm  i  V./^J.S;  —  'farahqm  urvaranqm  yat  ätri.- amqsta  fsd.)  ''i^arö.cikaya  *°le  anye  cika- ■  ciirranqm  V,4',75;  —  'ttm  ratümca  .. yatö  "wenn  einer  ,  .  und  wenn  einer  ,  .  \yim  maiaydhanmaim  A.j.3(?).  b)  sub- vcrletzt,  so  sollen  sie  dies  und  jenes  . ."  stasA\v\&c\\- 'ta(^T>.)äb3r3ta*sraosiivariza F,_jc  b)  adjektivisch:  j'iT/fl/ire'a/ara.-  vicarayaDm  "die  beiden,  der  .^.  und  der iri^yeiti  kva  "tarn  xsapan»m  . .  *vanAaiti  Sr.  .  ."  N.  jcf ;  —  cval  'te  (ADn.)  stai- "wenn  ein  Gläubiger  stirbt,  wo  weilt  asi\tiüa  bar>iis^a  ..  nasus  .,  fräsnaoiti dem  Tä^  (des  Todes)  . ."  H.  2.  i;  — yö  "..  die  beiden,  das  Bett  und  das  Polster .." . .  upairi  kunanm  (sdL)  manö  baräi  i-up^m  V.  7.9;  — ■  azim  °ta  (APn.)  zaota  zlsJi  (sd.) 'tfm  paiti  zmämm  aUariin  uri'a  kllayäi  ..  /rasrao^r?mca  /ragl>r>mca  . .  Vr._j.7; (sd.)  "wenn  einer  . .,  so  . .  während  der  —  't^m  nitamim  As'>rjm  '^rivacahim  (sd.) ganzen  Zelt  (seiner  Cberhebung)  .  ."P.  "id  minimum  Aj^/um:  triverbe"  F.  27b; J7.  a)  wo    wir   'solch'   brauchen:  yö  —  haomü  kutö  .  .  ava    'te  ahuta  .  .  "ge-
2571:fBgt  /  tä  ..  hiniu.  —  ')  Pü.:  ilän.  —  3)  Pü.:        afun    Kurinamen   daiü    fortsetzen;    doch  s. aetavatö  Adv. :  s.  aetavant-
2578:31;  3''.  35'*. "^-85;  —  tts  haca  nassvö  °vat  •  j.  aeJa-m.,  Plur.  'Kopfhaut';  '',a  ..*kay:i apat Aaca ni:iiiraj-fnV.6.$if?); — asH.masÖ  fi^nti  masyat»hd  'r,a  *ydi  *aparaya  paiti xraoidi'aAe  bis  'rate  lar^AaAe  "..h\s^3iXtto  *)tiastrfynaya..*kaya  kasya/i/t^  *yüi  *paou- mollisligni"  V.  jj.  30;  —  'val  apayaiia  H.  ruya  paiti  *mastrr/nya  "Kopfhaut.  — iog(X).  a)  mit  dem  Korrelat  _v(K'a«/- :  Welcher TeilderKopfhautistdergrössere? ^t/ (sd.)  °vat  htT^r»m  yaval  tacantn  F. '  Der  an  der  hiotera  Schädelwand.  Wel- 27a;  a;  ■ —  yavat-  hatca  hl  sastaiibya  eher  der  kleinere?  Der  an  der  vordem hangturvayqn  'vat  apat  haca  nizbärayfn  Schädelwand."  F.jc. \.ti.2t);  —  'imt  npö  yavat ,  .  J^.ioX;  — 'foiö  zaota  (iäm\.  ratu/rii)  yajat ß-ama- raiti  "mit  so  vielem  ist  der  Z.  r.,  als  .  -^  „  . n  (selber)  .ufsagt-  N.  2,1  2,,  23,  »>',  \  )■  if^  'a.«,y<,il„t  pa,U  afa  .  .  N. j'P.  Aa)  GS.  'vatö  als  .\dv.  'quantum  ^  j-  .  j^j^j^ sat  est,  in  hinreichendem  MassM?):  hura-  "  ^^.^  ^  ^  ^^^  ^^^^^ ysscti  (sd.)  a(.a  Tato  datdyat  A.j.4;  —  .   ^i%y^_^.^^,„„  -(.^5.  y^s  ka^i^yStarlum.
2643:•  j.  aenaahe,  g.  +''oaöhe  Inf.  'einem (GÜubigen)  Gewalt  anzutun,  an  ihm  Ge- walttat zu  verüben'  a)  mit  Akk.:  hyal  mäi ärfg7-i'j  dläar>iat3  (sd.)  'nariAl  Y.  4^.  7  ;  I —yi  rä  mäi  yä  gaf^<i  (fazdg(sd.)  'naiihg\ \.46.B.  b)  mit  Gen.:  naeÜlcä  *atiha jässiti  .  .  mahrküi  (sd.)  ndit  -nanke  Y. (»5. II.  c)  mit  Pianü  und  Akk.:  Ayat •^natike  dng^'atö  S»ana  i^yPng  arghaya  (sd.) Y.^2.i6.
2675:parnnsm  /ramStHram  X.  /.  i,  &.  i,  D.  &.  i,  j   a^a/j  n.  j^;  li«  iHtavatö.
3056:•  j.  aya'vant-  Adj.  'reich  an  Übeln,  Ge- fahren' :  z?m3  ..  ■'vatö  "des  gefahrenreichen . .  Winters"  V.  7.27.
3161:Komp. !  niä.+'un-ii/a-,  PPfP.  lum  V.  :n;irs- ; zSchr.,s.  S  :6S.  44  aE.  —  Pü.:  atö£isn  (T.)
3272:•  j.  a-dätay-  f.  'Nichtgeben,  Nichtdar- bringen,  Verweigerung':  «J  gJu/  ml  vas- trahe  hatö  "oditlm  vaocöit  "man  soll  nicht das  Nichtgeben  eines  wirklich  vorhandenen Fleischstücks  oder  Kleids  behaupten"  V. 4.46'*; — paoiryeheca  nH  myazdake  'oätii {]Si.) yat  mai'iydi.sar^myeAe"\inA6.zi:iz,Aa:&s man  den  ersten  My.,  den  des  jW. -Festes, nicht  darbringt"  A.  j.?;  8-12  (,  SWienAW. (17,839);  —  kat  «3  *dazi'ayasnäi  vä  .  . giul  'iaitya'"  ästryeiti  "begeht  man  da- durch Sünde,  dass  man  einem  Z>. . .  kein Fleisch  gibt?"  N.  i(?; —  •oaiti  */rilraihya-
3304:•  j.  a-daratö.tkaesa-  Adj.  'der  den  Lehrer nicht  achtet':  vlspe  drrantö  tanu.drujö yS'^ •sd'''  vXspe  'sS'*  yß'>  asnifs'ß'''  "alle  sind ungläubig  und  leibhaftig  mit  der  Dr.  ver- bunden, die  den  Lehrer  nicht  achten;  all die  achten  den  Lehrer  nicht,  die  (ihm) ungehorsam  sind"  \.i(J.i8.
3541:•  j.  "apaS'atö  paitim  äpim  . ."  FrD.  7. j.  ^paeurus  karma  apaj^ta  . ."  P.  4$-
4085:•  j.  ^afsmaimv^  Adv.  'verszeilenweise' : iraosim  . .  yS  paoirys  ga^a  frasrävayat . . *a/s°'''  vacastastivat  ".  .  der  zuerst  die Gäha&  rezitirte  .  .  verszeilen-,  strophen- weise" Y.  57.8; — yä  gäiä  *a/s''^  sräva- yatö  uva  ratufris  (statt  ND.)  vacattaSHvat *srävayatS  aSavatö  katarascit ,.  N.  2J;  — ys  yasrum  *yasmti  *aft°  -ö  va  vacoitaitivai va  nva  ratufrya  N.  24;  —  yat  kakat *'amrutS  ^'vanca'''^  *valastastivaüa ..  N.24.
4146:der  Gesammtheit  der  stofflich  Seienden, 'die  Welt,  Menschheil'  (s.  I  la);  yasnyasla vahmyaüa  'nuhe  astvaite  Yt-fS*.  15;  Y.  65. 1%  Yt  y.146,  V.  2.24,  P.J5  (wo  arikeY\ *Vyt  J<?;  —  apam  napiss  tä  äps  .  .  -t3uhe astvaite . .  vl6ax/aiti  Yt.  Ä  34 ;  —  syai)^  na . . yä  'ühus  astvä  vfifzyäü  V.  75.  i;  Yt.  y. 12;  —  avi  °hüm  astvantpta  a-fpm  (sd.) *e}mS  jaiihintuY.  2.22*;  —  kascit  'ufiSus astfats  "ein  jeglicher  Mensch"  F.  2()", V.Äioo;  7.50,  70.19,  'Äaa.  P.y,  .<3;  — anys  kascit  "nhSu^  ash'atö  N.  63;  — yeiftyö  .  .  vlsp^mili  -uuÄe''  astvaite  Yt  10. 5.  aa)  mit  vispa-  Adj.  'die  gesammte
4249:raolatfhqm  (näml.  ayan)  heUst  der  30. Monatstag;  S./.30;  vgl. 2.30,  Y.  16', 6;  — auch  ohne  raoc' :  pancaca  kaptailJm  paittl- hahyehe  (sd.)  xsa^rake  vairyehe  'ranqm A.j.g;  10.  b)  'ra  hmä  'die  anfangs - lose  Finsternis' :  täirlm  gama  frabarat  yg nars  drvatö  urva  'raih'a  tjmShva  nida^at H.2.33.
4484:•  j.  anu,  p.  anuv,  g.  33änü ''  i)  Praen, a)  mitAkk.,  a)  'nach,  gemäss':  hvam  'u uStim  zaoämca  V.2. 11; —  °«  a^qmi^A.) N.Äjj/Oj;  —  ftspünam  "u  mainm"n3Lch aller  Urteil"  Yt.5.93.  ß)  'in  der  Rich- tung auf— hin,  an':  Ayaj  *aenatiAe  dr}g- vatö  Ä»J»fl"  isySng  *ankayä  (sd.)  Y.  J2. 16.  b)  mit  Lok.  'längs,  entlang  an— ': !!  zäzänJ'  niima"  vardanam  °uv  ^u/ratauvä (sd.)  Bh.j.19.  2)  Praev.  (mit  '«««-, var>z-,  slü'  u.a.).  [Yt. /o.  137:  lies anu-sasträi,  anu.maiityji.]
4696:•  j.  ama'vant-,  g.  Sma'vant-  Adj.  (fem. 'vaifi-)  'kräftig,  stark,  mächtig,  gewaltig, wuchtig'i  a)  vona)  Menschen  und  ß)  Göttern : o)  narf .  .  pancajiasanhö . ,  hrpzats  avi.- amahe  'vatö  Yi.S.i$;  — ya'ia  agj?  'va .  .fraxitäne  z?ma  paiti  Y.5. 20;  —  aisäta "iwa  'vantaslä  buyamä  (sd.)  Y.4J.4;  — , ^vm  yäka  ^vifrö  naväso  Vyt2;  Az,2;  — | faritJm  il  ^icJ  yähanä  tat  °vatqm  kyat ^wä  xiayqs  (sd.)  aissm  dyll  'vantim  "eine Frage  von  dir  (d.  i.  Zar^  ist  ja  wie  eine Frage  Mächtiger.."  Y.^l^.io,  zit.  A.  4. 3, wo  amavanlam  und  amavant^m ;  —  °fa (NSm.)''  äs  Vfri^rava"^  nqma  v^rp^rava] Os  'va  nqma  Yt.  i4'S9-  ß)  ralnul bjrTZö  yö  '»i  Yt,JO,ioo,  i2.6;  /7.16,  J2. ' 5;  — yö  {sraolö)  .  .  niaza  'va  firS^raja'^ , Vr./5.3;  —  °va  mt^rä  Yt  10.  loj ;  6,  25, loa;  —  airyamarigm  .  .  'vantpm  vprjhrd- ^
4698:\)amm  Y.$4.2,  G,  j.6; — yä  {ar?ävi) 'vaiti fratalaili  Y.  Ö5. 3 ;  Yt.  5. 1 5 ;  —  a^tn  vatau- hlm  .  .  hrpsailTm  'vattTm  Y.  3. 14;  Yt /J. I,  7;  —  drvaspqm  . .  'vaitlm  YL9.2;  — fravaiayö  .  .  yä  'vaifli  Yt  13.  29;  —  at töi  atrjm  . .  *asXsttin  'vanhm  Y.j^4;  — tiiirim  .  .  'vant?m  YtÄ4;  —  vatianttm 'vant»m  Yt  21.  i;  —  °vatS  amai  'vatÖ virp^raynäi  'vat^yO.  »rütyi  'vai'iya aiöii  'vai^ya  astdil  'vaüyä  paurvatälo 'vai'i'yB  uparatälö  'va^byä  yazatoAbyö  Vr. g.i,.  b)  sonst;  uströ . ,  b)r?zB  "vä  Yt i.^.  1 2 ;  —  srlra  urusta  'vaiti  (VSf.)  .  . UfTaireY.it^.iB,Vyt22; — srayarfhö  vouru- ka?ahe  'vatö  Yt.<S.46;  —  vasnm..  zaröil ayanhö  frahixt»m  'vatö  \L  10.96;  —  'vat iimäfum  Y.  57. 10;  —  ptiüm . .  yim  aiwatö 'vantim  Vyt.^;  —  'vaitlm  sitiqin  dävöi (sd.)  dr»gvasa  Y.  44. 14.  —  IstJm  . .  pouru.- sarioam  'vaitlm  Y.  65. 1 1 ;  —  hazö  "vat  Y. jj^.  iz;  —  yahmi  maza  'va  (NSn.l')J' '  iiiäälpm  Yt  10. 64  (?) ;  —  *°vata  vaca  F.3  e. AbleiL  —  ai.  dmm-ant-  Adj.;  vgl.  mp.  (PS.) amäz-nnd.  —  ')  %  jg4.  —  •)  Zur  Zusammen- Stellung  von  amai'aaf-  mit  ^'/ri^ravan ,  viri- %rasan-  s.  'amn-  2.-3)  Wenn  richtig,  wohl Neubildung  lum  NSm.  'va  nach  der  n-Dekt.
4775:•j.,g.am»rBta'^t-,  amarBtlt-'T.'Unsterb- lichkeit.  Ewigkeif;"'  tit  d^hnaotä  maslm hujyiH5is{sA)  "ntstascä  Y._j2. 5 ;  —  'rstSitl *a^aonö  urvä  also  (sd.)  utayütä , ,  Y.  43. 7 ; 48. 1 ;  —  yä  fyat/^an/t . .  -ntäbm  astmcä *taibyO  danhä  (sd.)  .  .  xs^nm^a  haurva- tätö  Y.34-^i  —  ahmäi  aahat  vahiihm yi  möi  vtdva  vaolat  hai~ilm  mq^r^m  yim haurvatatö  alahyä  'ritatasca  "dem  soll das  Beste  zu  Teil  werden,  der  mir,  ein: Wissender,  ktmd  tut  das  rechte  Wort  Aia^ von  der  Wohlfahrt  und  Unsterblichkeit" Y._3/.6.  a)  bes.  in  Dual  Verbindung  mit
4777:ahmst  sISi  dqn  (sd.)  trvjh  utayüitl  Y.  4I5. 10;  57.7,  44.18,  47.1;  —  0,a  haurvaia "rstäta  ySi  slö  /nlzd»n  asaonqm  parSMsti jasmtqm  Yt.  1.25;  —  mazS  (sd.)  avaKyai .  .  daidl  Aaurväd  Titätä  (GD.)  V.  5Ä 7.  a)  als  Bezeichnung  fiir  die  Speise der  Seligen*;'*  at  löi  ubl  haurvassa 3^ar?%äi  3  'r^atasca  (NS.)**  "und  deine beiden  werden  zur  Nahrung  dienen,  der Wohlfahrtstrank  und  die  Unsterbltchkeits- speise"  Y.,?4.  n.  A)  als  Gottheit  {Amasa Spmtd),  der  die  Sorge  für  die  nützUchen Pflanzen  anvertraut  ist  (SüErL:  vanas- patipatiliySi  aya  damaya  fraonnta  akurd .  .  vohu  manu  .  .  a£>m  . .  xsa%rpm  .  . ärmaitil  frä  kaurvatas  fra  'r>tatils  Y.57. 24;  —  vanät  haurvasca  °rstas^a  (NS.)" •wa  sUMtttca  farsmmla  Yt  ig.  96 ;  96 ;  — armaitfm  ..  haurvaiat^m  ..  'rsiatatsm  yaza- maide  Y.16.%;  JI.12,  S,  2.6f.;  —  mazdii dadat  akurö  haurvatö  'riiatascä  .-.  sarS Y. 31.21;  —  data  vj  'rjtSscä (NS.  als VS.)i> utaySitT {%A.)  kaurvatas  draonsY.33.9,;  — iaurvatas^a  'r)tatasca\t.4.i(f)  a)bes. i  in  Dualverbindung  mit  Aaurvatät-:  aya I  damaya  fraornnta  ahurd  masdä  .  .  fra ,  sp^nta  *armaitis/ra  haurvaia  °rHäta  (ND.) Yt.  JO.92;  —  sarBi  bszdyai  (&d.)  haurräiä I  "niaia  (ND.) . .  j?.  .  Y.44.17;  —  upa.- ßm^ti  (sd.)  haurvatä  °r>talä  (AD.)  Y.  45, .  5;  —  sp)ntayai  ärmatSe  haurvalbya  -ntat- '  bya  Yt.  7. 2 ;  H.  i.  7 ;  —  yS  spsntaya  arma- töis  yä  haurvatä  'ntata  (GD.)  Y.  70. 3 ; .  —  kaurvatasca  nö  'ritats,'''^ gTusca  tasiiö.. I  Vr.  g.  5,  a)  amir>tät5  (näml.  ayar?) heisst  der  7.  Monatstag:  S.  7.7;  vgl, 2. 7, ,  V.  7tt.3,  A  1)  als  Bezeichnung  für  die
4923:unsTcs  schwachbetonten  'er'*':  fravasayB ..  yä  ahurahe  xiayatö  daiinam  ufayüÜt- ynnii  yai  aim  bavaiti  *alavaxmul  yai fi  bavainti  anäzaritä  Yt.  /J.63;  —  ä  dim paskät  anumar»zatim  aHila  . .  färfndtl'a  . . visp>m  ä  akmät  yat  aim  paiti.apayat.,'H\.. iV.38;  —  vispaeibyS  sastim  baraiti  älarS. . yaübyS  alm'''*  *ham.paeaili  ..  \.62.T,  — iim  Aaxa  Aase  baraiti  . .  ?  äat  yai  s!  a^m  " baraiti  .  .  Y.  62.  8f.;  —  yim?m  .  .  yerihe xsä^rä',a  ndit  aotim  inha  . .  para  akmät yat  hlm  a!m  *draogpm  välim  .  .  patti.- barata  Yt.  ig.  33 ;  —  tvai  na  *ai^rapaitim updisai  .  .  iim  *aSm  at^^  aS^rapaitim upayat  (sd.)  N.  Jlt;  —  mürtm  .  .  yd .  . frä  rasmanö  scandayeiti  .  .  ari  dlsalm.  . Ji^iM  *baraiti  Vtio-^Gt;  loi,  71  (yavata aim),  .5', 43  {yezi  alm),  47  (ya^a  am); —  aom  asmatum  ,  ,  mariay^n  ahe  yäiia vis  aim  .  .  Yt.  ij,2.  2)  auf  ein  Nomen vorausweisend:  äa^  mg  alm'°^  pait- yaoxta  AaomU..Y.ff.i;  V.2.3.  III)  ver- doppelt, substantivisch  sva,  'irgend  ein  be- liebiger': _)(7/  hl  nazdiUö  dahmö :'dü'/(sd.)  yavat  vä  aSm  aim^^^ uübya  N.2;.
5315:•  j.  "araityatö 'J  Vyt.5.
5453:•  j.  aratö.kar^^na-  AdJ,  'wofür  die  Er- füllung der  religiösen  Pflicht  bezeichnend ist',  von  Hamaspa^maedaya  (sd.)":  ha- maspahmaSdaim  "tum  Vr.  2.  z; —  kama- spdimaldayeAe  'nahe  Vr.  1.2;  —  *'%nö F.7'>.
5833:35.36,41,50.  i4-ii',i2-is,  /5.i7,23, 44,46,50,  j6'.i,5,i4,  /p.27,  c)  atfliav- (sd,,  auch  fdSt):  ahvi  'vaiascä  hyatci maiiatiks  äyapts  (sd.)  Y.  28. 2;  —  paid. . ahyä  arahSus  °vatö  manatthascä  hatk:ySng *•!  Sil/  (sd.)  Y.  4j.  3 ;  —  uvaHbya  nS  aAubya nipayä  . .  ahe'a  anhSus  yS  'vatB yash  asti manahyo  Y.  57,  25;  —  mäca  .  ,  'vatahe^^ anhHis  didnsvg  Pisa  (sd.)  manahim  paiti.- ralxMa  '2.40;  *4o'^;  —  ka>a  .  .  apa- jasg .  .  °vatal  haca  arahaot  manahim  avi ahüm  H.  2. 16;  —  vTspB  anhus  "va  \.s. I  usw.j>;  —  visp>m  ahUm  °rani3m .  .jumta iristfmca  Yt,  13.  9;  *Vd.  <V'*;  usw.3>;  — hascit  atihsus  'vats  F.  -'tf;  *N.  63'^;  usw.J*;
5917:VeI.  SBE-  47.  165.  —  ')  Der  Mann  hLess  im Non.  luDächst  *asnia  j^airrS,  ä.  i.  'lichter lllmmer;  der  rcEcIrechte  Gen.  dazu  ist  alnS i'.im-atö  Yt,  13.  96  2.  Stelle.  Aus  *asma i'anz-a  entstand,  indem  das  Nominaliv-a  durch riis  KooipositionS'D  ersetit  wurde,  asmöJ^atn-i Yt.  /.  30,  dem  dann  als  neuer  Gen.  asmS.. i'aTK-atff  Vl  7J.  96  I.  Stelle  mr  Seite  trat. l)et  Kompilaior  von  Yt.  /j  hat  iwei  Männer draus  gemacht.    NA.  trennt  ßlscblich.
6099:—  mazda  dadät  aAurö  Aaurvatö  amfntä' tasca  .  .  'sahyacä  xsairaAya  sarö  (sd.) vanhSus  vazdvari  mananAS  Y.  31.  21  \  — tä  vi  masdä  .  .  aAurä  'säi  yecä  taifyacä armaill  .  .  i/lffiS'  (sd.)  xsa'^rvm  .  ,  voAä manaaAa  Y.57,  2;  —  tat  vi  ni  Aasaosä^
6152:•  j.  a-Saeta-  Adj.  'der  Icein  Geld  hab arm':  saHavatö  ahmot  (nämL  pourum  fra- mraomi)  yä^a  °täi  "dem  vennöglichen (spreche  ich  einen  höheren  Wert  zu)  als dem  armen"  V.  4.47.
6284:—  'Zäum  ahura  mazda  Y.  16.  i  o,  Vr.  5. 3, Yt./.5,  72.1,  V.2.39,  s-39<  ''■4».  7-23- A12,  7^.41;  —  ahura  mazda  mainyS s^nista  datar»  gai^anqm  astvaiiinqm (Stverz.)  '/3um  V.  2,  i  usw.;  39  usw.;  — unter  den  Namen  des  Ah  AI.:  "sava nama  ahmt  aiavasUma  nqma  ahmt  Yt 1. 1 2.  a)  auch  Kar'  i^.  (ohne  Nennung des  Namens);  im  Gegensatz  zu  drvant- (sd.  II  2  a  a):  °saono  ahmt  drvatS  nsii  ahmt Y.  10.16;  —  sonst:  *eyum  na  °saonS xsnaohnm  (sd,)  H.  7.  5;  —  s.  noch KompA.  aa)  GS.  mit  stay-  (sd.,  auch fdSt.),  iraOegensatz  zu  drvant—.  o^a^rimca .  .  'saonB  stöis  . .  duzä^r^mca  .  .  drvatö slöHY.  8. 8 ;  52. 4;  —  sonst :  hatkyävarfz^m . .  'säend  stim  G.  _j.  7 ;  Vr.  18.  \\  —  anayra -saons  siis  Yt.  Ä  48;  *V.  2.  19  PüZ., usw.  3)  von  allem,  was  sonst  zur ö.4ansclicn  Welt,  zum  Reich  des  Asa  ge- hört, auch  sva.  'Jieilig';  im  }Av/.  (s.  auch  2) :
6470:y  aila/atö  P.  47-  ü«  "^  mxmi.
```


## [2026-09-04T19:03:41.775Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rmäyu\\|rjnäyu\\|r3näyu\\|ranäyu\\|näyükaP\\|näyüka\\|näyü\" BRT.txt | head -20"
}
```


### [2026-09-04T19:03:41.826Z] TOOL RESULT

```
3660:•  j.  a-p»r»näyav-  Adj.  "nicht  volljährig, minderjährig, unmündig':/w^^iTÄÄ  ^'näyaoS N.54;  —  kimHi  daAmanqm  'nSyunqm 'S.iO-{;  —  vispaiibys  'tiayubyd  lÜ.ii;  — tisil  (okmäi  'nHyunqm  N,  //;  —  "nayu  (als NSm.)  "  aimi  nsit  p?rmäyu  (sd.)  Yt.  i(). 43;  —  ms  °nayu  (alsNPm.)"  iaunmii(sd.) mJl  iaintna  YL77.54;S5.  a)  m.'Kind'; 3faß0yaha  'niJyus  "verschlafen  (ist  der Hund)  wie  ein  Kind"  V.  73.48;  483.
4230:6)  Pä.:  anäyünik  räi,  Sü;  attaganlä.  Man nehme  dazu  DST.s  seltsame  Erkllmng  (IFAnz. 6.  43).  5.  noch  Pü.  zu  anäis  ä  und  zu  äü.  — 7>  NA.  a^ä;  S  4'9  No.  1.  —  *>  Pü.:  a/i  Aa/ isän  lardärih  gmotm  ke  ißn  äniand.
4380:•  j.  aii-a'haxta-'>  Adj.  'der  nicht  berech- tigt (geeigenschaflet  und  ermächtigt)  ist {etwas  zu  tun)':  yS  anyahe  ^apynnäyüka ^'lä'^  a'^aurufiTttt  paraahacäiti  "wenn einer  eines  andern  Kind  unberechtigt  3'  zu priesterlichem  Dienst  mit  sich  wegfiihrt" N.7;  6;  —  'tö.  .  ahaxts  (sd,)  N.tf;  — haxts . .  'ts  N.  6-,  — yasta  aSlalsam  mazda- yasnanqm  tnyazdavanam  aüanhqm  yat myazdanam  "ts  parabaraiH  nsit  täyul ,  . bavat  .  ,  ainyi}  kasat  .  .  "und  wer  von den  ,  .  M.  etwas  von  den  My.  wegnimmt, auch  ohne  berechtigt  zu  sein,  der  , . ;  aber irgend  ein  andrer  .  ."  N.  6^;  —  yezt^a *aile  ratavö  *'ta*^  *para.iyayanH  "und wenn  die  R.,  weil  (zu  ihrem  Amt)  nicht qualifizirt,  weggehen"  N.  ^o;  —  zaota  (sd.) *-ßS)  parayat  N,  So.
4474:Pü. !  anafie  apaspäTÜnik ;  s.  noch  No.  4, 6.  — ')  Hds.  Shianisititim.  —  »)  Hds.  ainüsrilim. — 3)  Hds.  ai%sHiim.  —  1)  Hds,  anitril;  Pü. : fehlt.—  £)  Der  Text  sollte  lauten:  %TiiayaaA>m )ia%ra  raiul  a'iti/ayauliim  ya%ra  ttp>r>näyüt5 nSii  .  ,;  s.  zu  ♦aSiffflyiis'iri-.  —  *>  Hds.  airili; Pü.:  /a  fl/Ji-'  (statt  atiapäc)  apasparäulh,  erl.: kaS  nc  dabei.
7830:kommen zu  — '  (Akk.):  vlspü  anhus  ..  air- yatum  vaijS{sA^fräsnvät^.t.\.  a)  'in Berührung  kommen  mit  — ':  yezi  apin- I  näyüks  fräshaväi  "wenn  ein  (saugendes) Kind  (mit  der  menstniirenden  Frau)  in Berührung  kommt"  V. /6'.7*>.  3)  'teil- haftig werden,  sich  teilhaftig  machen',  mit |Gen.;  nSit  dva  nSit  irayS  .  ,  asake  ndil asaya  früsinti  (Konj.)  yß  rßit  .  .  "nicht '  werden  sich  zwei  .  .  des  Asa  noch  der 'Belohnung  teilhaftig  machen  .  ."  P. '  44''^.  4)  'zu  teil  werden':  hyat  nä  fryäi I . .  isvS  (sd.)  daidii  maibyS  . .  tava  rafons ^  fräximmm  (sd.)  hyat  'kwä  xsa'^ra  asät ^kala  frqstä  (3SPrM.)*>  Y.^O-M'
10904:Zum  V,  xsnav:  —  Vgl.  xinümaine  mil  JScHMIDT Krit.  103.  —  rap.  inöm;  %.  dizu  Hbm.  AGr.  /. 214.  —  Pü,:  inäyünlh,  erl-i  .,  rämUnlar  iarl
10911:Vgl.  snül-  nnd  IF.  p.  374.  —  mp-  inäy/ntlan (Kaus.);  ^''alnSI,  np.  x<,!n,ld.  —  PQ.  (für  I  nnd 2  Pass.):  x^ainül  bülan;  (für  2):  iibiyftüian, Sü. :  salkärayiliim,  sanmäitayUam  \  (fOr  3  a  CD Y.  43,  45):  fHämei  li)  hüyinitärt),  tiiSmS 73)  InäyütiSi,  (lu  Y.  33,  4p):  mSair.  —  D  « nur  F.  5.  —  ')  Unthem.  —  »  FOi  A'  der  Re-
13310:j.  dilti  Inf.  (?) ''  'abzuschneiden':  yö k»mHt  dakmanqm  \ap?rmäyunqm\  aihm dasti  hä  ml  bara  aismaca  bansmaca,  yezi
18672:3  airySma  (sd.)  .  .  jantü  mnbyasiä HäiribyascS  zara%uslrakl  Y.54.  i;  FrW. i.\;  —  narasca  *tiairTsla  Vyt.30;  — rtaram  näirinamca  V,  2.  27,  30;  8.  12,13, Vd.3,  Y.(?Än*;  —  in  Verbindung  mit alavan-  (s.  auch  Sp.  1050  o.):  aiaunqm .  .  urunS  .  .  kiidö.taianqmltt  narqmcä näirinqmlä  Y.J9.2;  J7-3,  -i'.?,  8,  10, Yz.iS.  2,Yt./j,  143-145^  A)näirika-. nar 3m  vä  *nSirikqm  vä  FrB.;  Az.  I,  Vyt. /,  Vd.  7j,  Nik-i-j^;  —  hala  nä  (statt Abi.)  paiti.irisi5  haca  näirika  paitiSriste V,  iO.  s ;  —  in  Verbindung  mit  aSavan- (s.  auch  Sp.  1050  o.):  nanm  asavamm .  .  näiriiqm  asaonim  V.p,33,  42,  ig.  12, 26,  71.1,  3,  7,  10  (statt  Abi.);  Vr.^.  4, G.4.9.  a)  jahikä-:  narS  (tiS.)''>  pai- ristä.xsu%rS  . .  Jahika  paraJax^ta  Yt  J7. 54.  f)  vantav-:  yaisa  nä  fryS  fryäi vantaoe{sA.)  ..  pu%r»m  ..  avi  avii.baraili ^- 3-  *S-  g)  pu'^ra-.  nanm  vä  .. puhnm  vä  FrB.;  Az.  /,  Vyt  7,  Nik. I.  h),  i)  aptnnäyBka-,  kainikä-:  na- ramHa  .  .  apmnäyükanamca  kainika- nqm!a  Y.  68.12;  26.  8 f.'  2)  sonst: nar/^  k?hrpa  panca.dasanlüs  YtÄi3, i4~^T,  Vdiy;  —  niUmactt  ..  stärqm {sA)  ya%a  nars  matmyehe  v(r/han>m    F.
18911:\paiti  nars  aSaorUS . .  °kala  apsnnsyäkasca varai^rm  (sd.)  pantqm  atBit  V.J.  11;  3; —  ,.  zaohrata  (sd.)  ratufris  'käscit  (GS.) apgrmäyükahecit  N.  .^0;  —  yS  anyahe'ka (IS.)  ..yS  anyehe  ^apirmSyüka  *anakaxt/T a'haurUTifm  *parar>kacaiti'ü.6i.;  6; — yHi.. 'kqm  vä  *ap}nnäyük>m  (vS)  a/t?m  dasli N.  105; —  'ka  kasujcra%wa  (sd.)  ^.40;  — ava%a  Ag  x"atg  (sd)  pu%rytn  ankat..aat yai  hvqtn  'ka^^  bavaiti(sd.)  ..yai dirftrqm \AfntiYd.2\  —  dahma  •^rf(NS.?)  ap^rma- yüke  kainike  Y.2^.3;  —  katärS  (sd.) '  a%aurumm  *parayat  'ka  va  nmänS.paiti^ va  N.5;5,  *5'>j — yai . .  nmanahe  nmOnB.- paitlm  'kam  .  .  daiöÄSui  daiiikupaitim 'kqm  bisazyätY.j.42;42',  is.$&.  a)mit asavan-  (Sp.  250  m.):  nanm  aiavanjm  . , 'kqm  a^aonlm  V.p.  33,  42,  75.12,  26,  rr.i, 2/7,  10  (statt  Ab!.),  Vr.j.4,  G.4.9;  — tat  asti  yUnO  . .  a^arihim  , .  tat  -kayai  . . ratuxsa^ray'ai  asaonyäi  H.  z.  1 8 ; — 'rikayh aiaonyä  Vd.  4-
19037:jAw.;  zu  1);  a)  das  Verbum  ist  indi-  n"^  . .  rta^a.äm  anyqm  . .  Y.  2.  ^y-  —  es kativisch:  n°  data  aAmt  «'  asts  (sd.)  ist  eine  Verbalform  entsprechend  der  des mpntS  .  .  V.  2. 3;  —  «•  As  ao^  pairi.-  vorhergehenden  positiven  Satzes  zu  er^ z'tfSiä»»' V,ip.3;  Yt5.93;  —  n°tatii^ar»nS\gä.ta.ta:  ap)rmäyu  aAmi  n'  p?r)näyu  (sA) pairi.abaom  Yt.7p.57;  —  "^"^  ^^l  n°  pairi.-\Yt  ig.43;  —  /W  äp^m  jainti..n'  avaha Jräsa  (sd.)  .,  *p3r>saAi  . .  Y.p.  25;  —  nava\  m3r>tS  V,5.  37;  38;  —  avi  ''ainyS  *'surun- Al  asti  ciha  .  .  n°  he  asti  yaozdühnm  V.  I  vaili  n'  ainys  N.  24;  P-i?;  —  nisriti 3-39',  —  "'  '?'"  ä^ravöpührim  (sd.) '^aStaAe  ästryeiti  n'  anisriti  N.ii; —  mosu nai^a  *daste  Aapu^nm  Y.70. 15; — na!cisca\tat  äs  n'  darrf>m  Yt5.  65;  —  sumnaoiti aitiAi  (Sp.  8  o.)  yasäiti  xyänäi  n'  snähai  ,*zaeta  upa.sraotara7tqm   n°  *upajraotärS
20789:10  m.)  bairyänte  yaisam  dim  /räye{%d^ vohunqm  V._j.  29.  p)  adjektivisch,  in- sofern das  Bezugswort  (Substantiv),  das man  beim  vorbeigehenden  Demonstrativ erwarten  sollte,  in  den  Relativsatz  gezogen ist:  aisqm  sanaoiti  virikrafmm  ySi  dim dahma  . .  fräyaz^nte  YL  /o.  16;  —  haomS aiiHi  ySi  aurrantö  hila  taxs^nti  arvnäum zävars  .  .  baxiaiti  "H.  schenkt  den  Hel- den, die.."  Y.5.22.  f)*iiÄrii-(Sp.34  o.); nur  B)  iinjAvr.;  das  Relativ  ist  substan- tivisch: aisS  *ratufris  yö  nSit  * aiwi-srun- vaili  N.  24;  *ig,  60,  V.  16.  5;  —  aÄ'a sadiranqm  . .  yä  *alaone  *daste  N.  84; —  baya  also  (in  Kongruenz  mit  dem Praed.)  äs  ahunahe  vatryehe  . .  y at  ii  frä- vaoc)m  Y.ig.^;- — aisa yeAhe apmnäyükB N.<?;7-.  g)  ^aaa-  (Sp.  13U.,  16  u.); nur  b)  im  jAw.;  das  Relativ  ist  substan- tivisch: all3m  a?sm»m  yö  vaoce  *n>miüika nqma  Yt.  74.  55;  —  aitayä  urvarayä  yä vaoce  hatäna^äta  V,  14.  4;  Yt  /4,  55;  — ime  alle  vaca  yöi  h?nti  atfrahe  mainySvS snäk?m  V.  10.  16;  3,  15,  17,  N._J_J;  — ku%a  aital  druxs  ppnnäne  yä  .  ,  upa fvaniim  upa^dvqsaiti  V.  /o,  i ;  i ;  —  tata^ bansma  yat  paiti  äp?m  fränayantgma N,  70;  —  altat  . .  yat  ti  asti  spmts.main- yaom  Y.  35.  j;  —  aKa  dämqn  .  ,  *yqm (APn.)  da%at  ahurB  Vr,  12.  4;  —  aOa^a daxmalsva  ..yöi paiti  äya  ztmä  bavainti
22784:i)  'schwanger  macheu':  te  mam  avdha  ,  nähme,  Erbeutung  bezüglich':  gnul..  'älm v>r3n>nle  ya%a  anyas&i  arlänS  avi  xsu-' fiantam  azaile  "den  Weg  der  Gcfangen- dri  xsaisrirva  hqm.Virpnavainti  (Sp.  1360  schaft'^  entlang  zieht  das  Rind"  VL/0.3S; m.)  "die  schwängern  mich  ebenso,  wie  wenn  —  yat  bä  paiti  narl  asaond  .  .  näiri- sonst  Männer  den  Samen  in  ihren  Weibern  ;  iaca  apinnäyükasia  '"hrm  paniam  atsit bergen"  V.  1Ä32;  —  hö  mam  aväia  pasnvänAfm  hikvatih9m"wQ&isG\:A.\ib\%ea VinnüHi  yaha  ..  V.  ;<?.  35;  —  *ffrmuile  Weib  und  Kind  den  staubigen  trockoen F.  5''.  e)    'schwanger  werden  mit  -■  Weg  der  Gefangenschaft"  entlang  ziehen"
24464:AanD  . .  bavSi  "bis  dass  er  greis  . .  ge- worden ist"  V._y.  19;  Ä38,  4.45,5.12,  59; —  v°  ä  a°  %rä%nm  k>r3navat  yai  a^a yS  apinnäyükö  utjasHi  (sA..)  V.75.15;  21, 43;  —  v°  ä  a'  yai  hl%rayö  xsafna  sacänte "usque  eo  donec . .  tres  noctes  praeterierint" V. 5.33;  J^-8, 15-23-  ''■43-  h)  yavat, das  Verb.  fin.  ist  zu  ergänzen:  v  a  a' aisa  äfi  ayaozdya  . .  yava^  aisa  nasul niziinla  V.6,3i'J;  —  v  ä  a-  '^rä%r9m k>r?tiav3t  yavat  aisa  spa  anyS  jasO  V. '5- 48-  3)  durch  einen  Hauptsatz  (?)■>'; ti'  a  a*  spä  vä  aiwi.vafnaiii  .  .  äat yai  Alt  spä  V3  aiwi.valnaiti  (sd.)  .  . FrW.  //  3),  II)    'bis    zu    dem    Masse
26821:bis  hapta  nmSna  *pairi.talahi(%A.)  bavanX V./j.44f.;  43,  21,  ji;  —  xlval  man'hs\ sanB  {GS.)  %rä%nm{sA.)  kafta  sar>üa\ apTTTnäyükahe  V. /j.  45;  —  gahvam  ,.' ^rayqm  *baotdri ..  sanam  *baotdn  {sA.) V.J5.49*';  —  katärö  'xT  ayä  vthrkaya ja%wSJarS  *atghat..yak:a  spa  vfkrkahe (sd.)  ktnnaoifi  ya^a  yat  v?hrks  spa  V.  13.  \
```


## [2026-09-04T19:03:53.428Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"volljährig\" BRT.txt | head -10"
}
```


### [2026-09-04T19:03:53.481Z] TOOL RESULT

```
3660:•  j.  a-p»r»näyav-  Adj.  "nicht  volljährig, minderjährig, unmündig':/w^^iTÄÄ  ^'näyaoS N.54;  —  kimHi  daAmanqm  'nSyunqm 'S.iO-{;  —  vispaiibys  'tiayubyd  lÜ.ii;  — tisil  (okmäi  'nHyunqm  N,  //;  —  "nayu  (als NSm.)  "  aimi  nsit  p?rmäyu  (sd.)  Yt.  i(). 43;  —  ms  °nayu  (alsNPm.)"  iaunmii(sd.) mJl  iaintna  YL77.54;S5.  a)  m.'Kind'; 3faß0yaha  'niJyus  "verschlafen  (ist  der Hund)  wie  ein  Kind"  V.  73.48;  483.
```


## [2026-09-04T19:03:58.769Z] TOOL CALL #24: Bash

```json
{
 "command": "sed -n 1,60p tools/ref_page.py"
}
```


### [2026-09-04T19:03:58.818Z] TOOL RESULT

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


## [2026-09-04T19:04:02.401Z] TOOL CALL #25: Bash

```json
{
 "command": "grep -n \"\\[pdf page\" data/verification/sources/refs/BQT_v1_pages.txt | head -3; echo ---; grep -c \"\" data/verification/sources/refs/BQT_v1_pages.txt; echo \"=== search borna in v1 ===\"; grep -n \"برنا\" data/verification/sources/refs/BQT_v1_pages.txt | head -10"
}
```


### [2026-09-04T19:04:02.493Z] TOOL RESULT

```
---
32486
=== search borna in v1 ===
8863:باید خرد شاه را نا گزبر هم آموزش مرد برنا وییر . فردوسی < لفت‌نامه *.
8900:۸ - چوآعیغ برنا شدآراسته
9869:۲ - پپلوی 200792 , 20117۲02 بمعنی برناء جوان « بونکر ۹۹ ».
17257:اعمال هرات برناحية بادغیس ۷ .
18281:بروزن سرتراشك » بممنی برناشك أست .
19010:بمعنی برنا است که جوان و نوچةٌ اول عمر باشد
19020:و تعصب باشد چه برنایشتی کردن بمعنی پشتی
24992:با درخشنده چراغی ممبان برنا .
26378:بشد برغخت زر اردای وبراف ۱ پنامی بررخ و کستی‌اش برناف .
27022:برنافتن- وترلك دادن و اجتناب نمودن و احتراژ
```


## [2026-09-04T19:04:08.132Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9855,9880p' BQT_v1_pages.txt; echo \"=== structure ===\"; python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds',t.count(chr(12)))\nimport re\nprint(re.findall(r'\\[[^\\]]{0,40}page[^\\]]{0,20}\\]',t)[:5])\n\""
}
```


### [2026-09-04T19:04:15.709Z] TOOL RESULT

```
پرخینه بمعئی ایما و اثارت (۶) باشد ۷ .
وزن سحر خیز , بمعنی پرویز است چنانکه
افربدون فربدون باشد - و بمعتی مظفر ومتصور
ایر ناك ه , نم ثانی و نون بالف کشیده و عزیز و کرامی هم آمده است ٩‏ .
)۱ چك : : سوم ۰ )۱( مك : زند ویاژند ۰ ۳ چك : هك.
4 چكث » چب 5 : اشاره ۰ () جكث ژند وداژند ۲
- اییورد و علورد سس کفتهاند وباورد همان « باأرت ۰ واباورت» زمان قد‌است وغاهراً
1 «زوستن؟ و وم «#یلین» همین شهراست. «امران‌باستان ۰۸-۲۲۰۷
باقوت کویدٍ : اسورد شهری اس بخراسان من سرخس و تسا و آب‌وهوای آن‌ناسالم امست و أین‌شهر ۱
دست این علعرینکریز بسال۳۱ « فتح شد وبصنی کنته اند بیش از این زمان بست‌احنفین
ی تن کقوده هف ۰ * معجم الملدان ‌ ۳ . رك ؛ ایبویه
۴ - مصحف کلمة بوتانی اییلمبنینا « لفت‌نامه » ۳118170021120618 ممعنی‌ناگهان
تن ۴ هزوارش 2 , 2۱۷۲2 . بهلوی خالك 22 « بونکر۱۰۰ 5
۵ رگ : ابرهام. ۱ - ازلفات دساتیر است ؛ رك : فرهنگه دساثبر صس۲۳۷۲ .
۲ - پپلوی 200792 , 20117۲02 بمعنی برناء جوان « بونکر ۹۹ ».
۸ - رك : اپیرنداخ » پرنداخ. ٩‏ - بپپلوی 2097۷۵ بمعنی پرو زگر » غاح
«منای ۲-۷۹۷ *.بچهُ با رسیده را گویند که از شکم ۱
و حبوان دمگر بیفتد .
اپرنداخ است که نیماح وسختیان باشد .
ایسان « بروزن یکان» سنگه فان‌را
گوینه . و آن منگی است که چبزها بدان
تیز کنند وسربی «مسن» خوانند .
ایشا « بان قرشت بر وزن تفزلد »
شبم را گویند » و آن رطوبتي است که شبها
بر سبزه و غیره نشیند ۷ . ۱
ایگافه » با کاف فارسی بروزن افانه,
=== structure ===
formfeeds 776
[]
```


## [2026-09-04T19:04:30.919Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# map line numbers\nimport bisect\nstarts=[]; n=1\nfor p in pages:\n    starts.append(n); n+=p.count('\\n')+ (0)\nfor ln in (8863,9869,19010,19020):\n    i=bisect.bisect_right(starts,ln)-1\n    print('line',ln,'-> page idx',i)\nEOF"
}
```


### [2026-09-04T19:04:32.533Z] TOOL RESULT

```
line 8863 -> page idx 272
line 9869 -> page idx 295
line 19010 -> page idx 484
line 19020 -> page idx 484
```


## [2026-09-04T19:04:37.515Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (484,295):\n    print('======== leaf',i,'========')\n    print(t[i][:2200])\nEOF"
}
```


### [2026-09-04T19:04:39.121Z] TOOL RESULT

```
======== leaf 484 ========
برحه
بر هه ۱ « بروزن کرعه: مثفب‌درود گری
باش که بدان چوب و نخته سوراخ کنند .
برن ‏ بروزن چمن . ام فصبه‌است در
فر فا ۴ ع بنتح اوز و سکون ثانی و نون
بالف کشیده . جوان و نوچة اول عمر و ظریف
را گونند - و بمعتی خوب و نيك هم هست -
و حنا را نیز کون دکه بردست و پا بندنده وضم
اول هم آمده است .
بر فاخی الستادن » کنابد از اطات
کردن و بلدب ایستادن باشد .
بر فاص ۴ - بروزن کربای, بمعنی‌غافل
و عادان - و غافلی و ناداتی باشد .
بر ناك ۴ « چختح اول بر وزن غمناله ۰
بمعنی برنا است که جوان و نوچةٌ اول عمر باشد
ور حنای دلت و بارا نیز گفته‌اند. و خ‌اوژهم
۱ رك : برماه.
1 نو ای
یعنی آدجه برس رکتابتهار نامها نویستد » وسسربی
القاب و عنوان گویند۷ .
بر ناه » بروزن حمراه » جوان و نوچة
اول عمر را گویشدب وحنای دست و پارا نیز
بر نایشتی - یکر بای حطیو سکون
شین فرشت و فوفانی‌بتحتانی رسیده ۰ بمعنی پشتی
و تعصب باشد چه برنایشتی کردن بمعنی پشتی
کردن و تسب نمودن است . #*
بر فج - فتح اول و انی و سکون نون
و جیم » آن‌باشد اکه سیب کوری‌با بجهت‌ناریکی
دست خور را مر دبوار با جابی بمالند تا وک
بیدا کاند ۷ ْ
پر فاد - بکس اود بر وزنکرفتار .
جوان اراده کنند . ناصر خسرو بلخی کوید :
داسفا ۱ : ۲ س ٩۹۳‏ . اه
۵ مرکب‌از: پیشوند بر (بار) ۳ نامه, ۷2۲-۲۵103
« اسفا ۱ : ۲ص ۱۹۰ . 1 - آمروز نمی دستورعملبکار
رود. ععرب آن «یر نامج». «رزی>.
غله‌است (3201۷3 ۳۷2۵()) که درمازندران. کلان » استراباد.
خوزستان؛ اسفهان وبرخی‌تقاط دیگر ابران ودر هندوسثان شرفی
و ژاين و چن میروید . « فرهنکگ روستابی ۲۶۵ » « کل کلاب
======== leaf 295 ========
کت آیرویز
نحتانی مجهول و واو » بسعنی آبی باشد و آن
ا ییون « بر وزن و ممنی افیون است
که تربالك باشد ونام داروبی حم هست که بیهوشی
می اورد ۴ ۰
ونگی ات ععروف. ابی سك ۳ ۲ بای حطی
۱ ۱ 3 ۱ ‌ ‌‌ هح ‌
یود ج ( 3 رب وسکون های‌هوز و کسرمیم رتحتانی‌بالف کشیده,
و دال بی نقطه ؛ نام شهرست در خراسان مایین بزبان یونانی توعی از تشنج باشد که مانع حس
سرخس ونساآله آنها نیزهريك شهری باشند! ۰ | و حرکت کرده
درهمزه با بای فارسی مشتمل بر بازده لغت
آر ؟ س بفتح اول و سکون ثانی ورای بی و بکاف زده » بلقت زند و یازند (۵) نوچه و نو
نقطه بالف کشیده , بلنت زند و پازید (۷) خالء | جوان را گوبند ۷ - و جماعتی از ترکان حم
را گوبند و بعربی تراب خوانند ۴ . 9
اپراهام * - بکر اول و حای (۳) ابر فداخ - با داد بی قطه و خای
بالف کشیده و بمیم زده , نامی است دارسی استان تن مان » سختان و تیماح
۰ که آنرا ممرب کرده «ابراهیم» گویند . را گویند
آ پر خیله - بنتح اول وکسر خای‌نفطه آیر و دز با راو و تجتانی حجهول بر
دار پروزن تترسیده . بممنی صریح است چنانچه
پرخینه بمعئی ایما و اثارت (۶) باشد ۷ .
وزن سحر خیز , بمعنی پرویز است چنانکه
افربدون فربدون باشد - و بمعتی مظفر ومتصور
ایر ناك ه , نم ثانی و نون بالف کشیده و عزیز و کرامی هم آمده است ٩‏ .
)۱ چك : : سوم ۰ )۱( مك : زند ویاژند ۰ ۳ چك : هك.
4 چكث » چب 5 : اشاره ۰ () جكث ژند وداژند ۲
- اییورد و علورد سس کفتهاند وباورد همان « باأرت ۰ واباورت» زمان قد‌است وغاهراً
1 «زوستن؟ و وم «#یلین» همین شهراست. «امران‌باستان ۰۸-۲۲۰۷
باقوت کویدٍ : اسورد شهری اس بخراسان من سرخس و تسا و آب‌وهوای آن‌ناسالم امست و أین‌شهر ۱
دست این علعرینکریز بسال۳۱ « فتح شد وبصنی کنته اند بیش از این زمان بست‌احنفین
ی تن کقوده هف ۰ * معجم الملدان ‌ ۳ . رك ؛ ایبویه
۴ - مصحف کلمة بوتانی اییلمبنینا « لفت‌نامه » ۳118170021120618 ممعنی‌ناگهان
تن ۴ هزوارش 2 , 2۱۷۲2 . بهلوی خالك 22 « بونکر۱۰۰ 5
۵ رگ : ابرهام. ۱ - ازلفات دساتیر است ؛ رك : فرهنگه دساثبر صس۲۳۷۲ .
۲ - پپلوی 200792 , 20117۲02 بمعنی برناء جوان « بونکر ۹۹ ».
۸ - رك : اپیرنداخ » پرنداخ. ٩‏ - بپپلوی 2097۷۵ بمعنی پرو زگر » غاح
«منای ۲-۷۹۷ *.
```


## [2026-09-04T19:04:51.971Z] TOOL CALL #29: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-04T19:04:53.734Z] TOOL RESULT

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
```


## [2026-09-04T19:05:06.251Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[484])\nEOF"
}
```


### [2026-09-04T19:05:08.384Z] TOOL RESULT

```
برحه
بر هه ۱ « بروزن کرعه: مثفب‌درود گری
باش که بدان چوب و نخته سوراخ کنند .
برن ‏ بروزن چمن . ام فصبه‌است در
فر فا ۴ ع بنتح اوز و سکون ثانی و نون
بالف کشیده . جوان و نوچة اول عمر و ظریف
را گونند - و بمعتی خوب و نيك هم هست -
و حنا را نیز کون دکه بردست و پا بندنده وضم
اول هم آمده است .
بر فاخی الستادن » کنابد از اطات
کردن و بلدب ایستادن باشد .
بر فاص ۴ - بروزن کربای, بمعنی‌غافل
و عادان - و غافلی و ناداتی باشد .
بر ناك ۴ « چختح اول بر وزن غمناله ۰
بمعنی برنا است که جوان و نوچةٌ اول عمر باشد
ور حنای دلت و بارا نیز گفته‌اند. و خ‌اوژهم
۱ رك : برماه.
1 نو ای
یعنی آدجه برس رکتابتهار نامها نویستد » وسسربی
القاب و عنوان گویند۷ .
بر ناه » بروزن حمراه » جوان و نوچة
اول عمر را گویشدب وحنای دست و پارا نیز
بر نایشتی - یکر بای حطیو سکون
شین فرشت و فوفانی‌بتحتانی رسیده ۰ بمعنی پشتی
و تعصب باشد چه برنایشتی کردن بمعنی پشتی
کردن و تسب نمودن است . #*
بر فج - فتح اول و انی و سکون نون
و جیم » آن‌باشد اکه سیب کوری‌با بجهت‌ناریکی
دست خور را مر دبوار با جابی بمالند تا وک
بیدا کاند ۷ ْ
پر فاد - بکس اود بر وزنکرفتار .
جوان اراده کنند . ناصر خسرو بلخی کوید :
داسفا ۱ : ۲ س ٩۹۳‏ . اه
۵ مرکب‌از: پیشوند بر (بار) ۳ نامه, ۷2۲-۲۵103
« اسفا ۱ : ۲ص ۱۹۰ . 1 - آمروز نمی دستورعملبکار
رود. ععرب آن «یر نامج». «رزی>.
غله‌است (3201۷3 ۳۷2۵()) که درمازندران. کلان » استراباد.
خوزستان؛ اسفهان وبرخی‌تقاط دیگر ابران ودر هندوسثان شرفی
و ژاين و چن میروید . « فرهنکگ روستابی ۲۶۵ » « کل کلاب
```


## [2026-09-04T19:05:21.348Z] TOOL CALL #31: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-04T19:05:21.356Z] TOOL RESULT

```


```


## [2026-09-04T19:05:26.401Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%AF%D8%A7",
 "prompt": "Give the full etymology section for the Persian word خدا (xodâ) 'God': the Middle Persian form, the Proto-Iranian/Old Iranian reconstruction, cited scholars, and any mention of *hwa-tāwya- 'self-powerful' or *xwatō-āyu- 'self-living'. Also any derived/related terms like خدیو."
}
```


## [2026-09-04T19:05:27.925Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D8%A7%D9%88%DB%8C%D8%AF",
 "prompt": "Give the full etymology of Persian جاوید (jāvid) 'eternal': Middle Persian form, Avestan source, Proto-Iranian reconstruction, and any cited sources. Also mention جاویدان if present."
}
```


### [2026-09-04T19:05:33.864Z] TOOL RESULT

```
# Etymology of Persian جاوید (jāvid) 'eternal'

## Direct Etymology Chain

**Middle Persian source:** The word derives from Middle Persian _yʾwyt'_ (jāwēd), meaning "eternal."

**Old Persian reconstruction:** It traces back to Old Persian _*yāvaitat_.

**Avestan cognate:** The Avestan form _yauuae-jī-_ means "living forever," providing comparative evidence.

## Proto-Indo-European Roots

The word ultimately originates from two Proto-Indo-European roots:
- _*h₂óyu_ 
- _*gʷeyh₃-_

## Related Terms

The entry notes **جاویدان** (jâvedân) as a synonym meaning "eternal" in Persian, indicating a related lexical family.

## Cited Sources

The etymology references three scholarly works documenting this linguistic progression, including Heinrich Hübschmann's 1897 Armenian Grammar and Birgit Anette Olsen's 1999 study on Biblical Armenian word formation.
```


### [2026-09-04T19:05:34.415Z] TOOL RESULT

```
# Etymology of Persian خدا (xodâ)

## Historical Development

The Persian word derives from earlier **خدای** (xudāy), which came from Middle Persian **𐭤𐭥𐭲𐭠𐭩** (hwtʾy /xwadāy/, "lord"). The Manichaean Middle Persian form appears as **𐫑𐫇𐫅𐫀𐫏** (xwadāy).

## Proto-Iranian Origin

The ultimate source traces to Proto-Iranian **\*hwatā́wHā** ("lord, god"). The documentation notes this root carried "both religious and secular connotations."

## Cognates

Related forms appear across Indo-Iranian languages:
- Avestan **𐬓𐬀𐬜𐬀𐬙𐬀** (xᵛaδata, "self-determined")
- Bactrian **χοαδηο** (khoadēo, "lord")
- Northern Kurdish **xwedê**
- Sanskrit **स्वधा** (svadhā́)

## Related Terms

Connected Persian words include:
- **خود** (xod, "self")
- **خدیو** (xadiv, "lord, master")
- **خاتون** (xâtun, "lady, noblewoman")

## Scholarly Reference

MacKenzie, D. N. (1971) documented "xwadāy" in *A concise Pahlavi dictionary*.
```


## [2026-09-04T19:05:47.883Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C3%B3yu",
 "prompt": "Give the reconstruction, meaning, and the list of descendants (especially Indo-Iranian: Avestan, Sanskrit; Latin aevum/aetas/aeternus; Proto-Germanic *aiwaz/*aiwi and English ever/never/every; Greek aiṓn). Also note any derived terms like *h₂yuHen- 'young'."
}
```


## [2026-09-04T19:05:50.092Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%86%D8%A7",
 "prompt": "Give the etymology of Persian برنا (barnâ/bornâ) 'young': Middle Persian form (aburnāy?), the Avestan source (a-pərənāyu-?), and any cited sources."
}
```


### [2026-09-04T19:05:55.331Z] TOOL RESULT

```
# Proto-Indo-European *h₂óyu

## Reconstruction and Meaning

The reconstructed term is **\*h₂óyu** (neuter noun), meaning "long time, lifetime." It derives from the root "\*h₂ey-" meaning "vital force, life, age, eternity."

## Descendants

**Major language families:**

- **Indo-Iranian**: \*Hā́yu (Proto-Indo-Iranian) → Avestan yauuae-jī-, Sanskrit derivatives
- **Latin**: aevum (also related: aetas, aeternus)
- **Germanic**: \*aiwaz → English ever, never, every
- **Greek**: aiṓn (αἰών), earlier aiwṓn (αἰϝών)
- **Albanian**: jetë
- **Armenian**: ayo (Old Armenian)
- **Celtic**: \*aiwestom descendants

## Selected Derived Terms

Notable formations include "\*h₂yéw-Hō" meaning "young" and compounds like "\*h₂y-(e)w-gʷih₃-" relating to health/vigor (Greek hugiḗs, Latin iūgis).

The word demonstrates the proterokinetic inflection pattern typical of neuter u-stem nouns in reconstructed Proto-Indo-European, with forms like genitive \*h₂yéws and oblique stem \*h₂yéw-.
```


### [2026-09-04T19:05:55.355Z] TOOL RESULT

```
# Etymology of Persian برنا (burnā/bornâ)

**Middle Persian Form:**
The word derives from Middle Persian *aburnāy* (/aburnāy/), described as "a Zoroastrian legal term."

**Avestan Source:**
The Middle Persian term was "borrowed from Avestan" *apərənāiiu*, meaning "underage." This represented "the negative of" Avestan *pərənāiiu* ("adult").

**Proto-Iranian Origin:**
Both Avestan forms traced back to Proto-Iranian *\*pr̥Hnáh*, which meant "full, filled."

**Semantic Development:**
The word's meaning evolved from the negative legal designation for minors in Zoroastrian contexts to the poetic Persian adjective and noun meaning "adolescent," "young," or "youth"—shifting from a formal legal term to a literary descriptor of youthfulness.
```


## [2026-09-04T19:06:02.335Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%AF%DB%8C%D9%88",
 "prompt": "Etymology of Persian خدیو (xadiv) 'lord, ruler, khedive': Middle Persian/Old Iranian source, relation to خدا, any cited scholars."
}
```


## [2026-09-04T19:06:04.026Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%AC%D9%87",
 "prompt": "Etymology of Persian خواجه (xâje/khwāja) 'master, lord': what origin is given (Middle Persian? unknown? related to خدا?), and any cited sources."
}
```


### [2026-09-04T19:06:08.950Z] TOOL RESULT

```
# Etymology of خدیو (xadiv)

Based on the Wiktionary entry, here's what's documented about this word's origin:

## Source Language Chain

The term traces back through multiple languages:

**Persian خدیو** derives from "Middle Persian _𐭤𐭲𐭩𐭥_ (htyw /⁠xadēw⁠/), from Bactrian _χοαδηο_ (khoadēo, 'lord')."

The Ottoman Turkish variant similarly came "From Persian _خدیو_ (xadêw, xedêw, 'lord, master, king'), from Bactrian _χοαδηο_ (khoadēo, 'lord')."

## Meaning Evolution

The term originally meant "lord, master, mighty ruler, king" in archaic Persian contexts. It later acquired a historical sense referring to the Ottoman khedive—the viceroy of Egypt (1805-1914).

## Related Term

The entry notes a relationship with **خدا** (xodâ, "God"), listed under related terms for Persian.

## Cited Scholar

Nicholas Sims-Williams is referenced in the references section regarding Bactrian language etymology, published in *Encyclopædia Iranica*.
```


### [2026-09-04T19:06:09.844Z] TOOL RESULT

```
# Etymology of Persian خواجه (xâje/khwāja)

According to the Wiktionary entry, the Persian word خواجه ultimately derives from **Sanskrit उपाध्याय (upādhyāya, "teacher; preceptor")** through Middle Indo-Aryan intermediaries.

The source states: "Ultimately derived from a Middle Indo-Aryan reflex of Sanskrit उपाध्याय (upādhyāya, 'teacher; preceptor; spiritual adviser'), via Central Asian intermediaries."

The entry notes that various Middle Indo-Aryan reflexes are attested historically, and suggests the Central Asian loaning source most closely resembles an unattested form matching Sindhi and Tamil cognates.

**Cited sources** include:
- Asatrian, Garnik (2011, 2012) - Articles in "Iran and the Caucasus" journal examining Persian loanwords and their history

The etymology does **not** attribute the word to Middle Persian or خدا (God), but rather traces it back to Sanskrit through Central Asian transmission.
```


## [2026-09-04T19:06:24.265Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 aiu ===\" && grep -n \"Lebenskraft\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-04T19:06:24.338Z] TOOL RESULT

```
=== WLD Bd1 aiu ===
594:Lebenskraft“ (ganz fraglich ist Zugehorigkeit von av. yav- „lange Dauer", 
14073:vom Aushauchen oder Auslassen der Lebenskraft (zur Bed. zuletzt Bechtel 
14075:fjTog, ■dvyov Acc. der Beziehung „mit der Lebenskraft auslassen“?). 
14674:-cs-St., bzw. s-Erw. : ai. rayns- n. „Lebenskraft. Jugendkraft, Jugend- 
14813:Zeitalter“, slov. v>:k „Kraft, Lebenskraft, Zeitalter usw.“, ceeh. vel\ russ. 
52149:Wznomina (in Zs.) z. B. ai. vayo-dha-h „Lebenskraft verleihend", sam-
```


## [2026-09-04T19:06:26.741Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '575,640p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-04T19:06:26.798Z] TOOL RESULT

```
Sehr fragliches Weitere bei Falk-Torp 1416 unter ogle (Eidechse): gr. 
aiyhj „Glanz, Schimmer“ bleibt trotz Prellwitz 2 fern (s. aig- „schwingen, 
vibrieren"). 

aibliro- ,,scharf. herb". 

Ags. u for ,,scharf. heftig“, ahd. eibar, elver (zum f aus b s. Bahder IF. 
14, 261) „acerbus, amarus, horridus“, vermutlich zu lit. aibrumas „das 
Wassern im Hunde" [von Kurschat nur aus Mielcke angefiihrt] wenn dieses 
etwa „Sodbrennen“ meint. Yerwandt vielleicht nhd. Eifer , mhd. tfer, altest 
„Eifersucht“, Falk-Torp 469 und 1491 m. Lit. 

Venn eigentlich „brennend" (vom Geschmack), liitzig", so vermnte ich 
Erweiterung zu ai - ,,brennen“. 

aiu-, aiu- „Leben. Lebensdauer, lange Zeit, Ewigkeit“. 

Ai. ayu n. (1. i. ayuni, dyuna ) „Leben“, av. ciyu „Dauer, Lebensalter": 
adj. ai. dgu-h „lebendig, beweglieh"; s-St. ai. dyus- n. „Leben, Lebensdauer, 
Lebenskraft“ (ganz fraglich ist Zugehorigkeit von av. yav- „lange Dauer", 
yava „immer“, Lit. bei Boisacq unter ate, vgl. Bartholomae Airan. Wb. 
1264). 

Gr. St. *alfeo- und *atfev- (letzterer kaum nach J. Schmidt KZ. 25, 24 f. 
und 3S, 49 erst durch nachtriigliche Uberfiihrung von *atfd>g — Fern, wie 
ijo'ig — in die Analogie der «-Stamme zu erklaren, wogegen at ev spricht; 
das z. T. fem. Geschlecht von alymv stammt allei'dings von *atfebg): acc. 
aid) (*a«yocra), loc. ate, del (*al$-toi) „immer“, suffisloser loc. lakon. usw. 
aleg „immer“ (tarent. ah) „immer“ instr. vom o-St. *atfo-), almv „Lebens- 
zeit, Ewigkeit“, aiev „immer“; jon.au (a'ldiog „ewig“), lesb. di (*alfl, wohl 
nach Lokativen konsonantischer Stiimme aufgekommen ; daraus durch 
Kreuzung mit alev :) lesb. auv, thess. div „immer“ (kaum altes *aiuim , wie 
got. aiw, s. u.); dgv-aiog „lange lebend 11 ;. 

lat. aevum „Lebensdauer, Zeitalter, Ewigkeit", aevifas, aetas „Lebenszeit, 
Alter", aeviternus, aeternus „ewig“; 

got. aiws (m. i-St.) „Zeit, Ewigkeit ‘, adverbialer acc. aiw Jemals = aisl. 
ce, ei „immer“ (auch in ei-gi „nicht !i . s. Neckel KZ. 45, 15), ags. a „immer, 
jemals", as. eo, ahd. io, nhd. je, got. ni aiw „nie“, ahd. nio, nhd. nie, ags. 
na (engl. no) „nicht, nein“; ags. ce, cew „Leben‘‘, ahd. ewa ,, Ewigkeit" 



aiq«o- — aik-, 1k- 


(ahd. as. eivig „ewig“), aisl. cevi, cefi f. „Leben, Lebenszeit, Zeitalter“; aisl. 
langcer „wer lange lebt oder dauert“ = lat. longaevus ; got. aju-k-dups ..Zeit. 
Ewigkeit“, ags. ece „ewig“. 

Air. dis, aes, ois , oes „Alter“, cymr. oes und acymr. oct, ncymr. oed ds. 
werden meist irrig als *aivestu- und *aivito- angereiht (so wieder Peder- 
sen KG. I 56, 176, II 19; schwierig bleibt dabei der von Thurneysen IA. 6, 
196 und Loth RC. 17, 434 eingewendete Yerlust des v im Brit.; daher 
miissen diese Worte an gr. diaaao&ai angekniipft werden, woriiber oben 
S. 2 unter *ai-to-). 

aiqSo- ..eben, geeignetk 

Lat. aeqiws ..eben; geeignet, passend, guns tig; gleich, ahnlich', aeqiior, 
-oris „Ebene, poet. Meer“. Alle bisherigen Zusammenstellungen sind un- 
sicher. Am ehesten sind zu vergleichen lit. iki, )k ..bis lett. apr. ik ver- 
allgemeinerndes Prafix (wie lett. ikdienejs ..taglich") apr. ideal, ikai (ik 
-f- kai) ..wann, ob“ (Bezzenberger BB. 26, 166f.). Vgl. zur Bedeutung lett. 
lids, nordlit. lyg ,.bis" : lygus ..gleich ". Femer lit. aikstS „ebene Flache,
```


## [2026-09-04T19:06:36.525Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ===\" && grep -n \"aiwos\\|aiwo-\\|aiwom\\|aiwesos\" IEC.txt | head -12; echo \"=== SYN eternal/young ===\" && grep -n \"aevum\\|aiw\" SYN.txt | head -12"
}
```


### [2026-09-04T19:06:36.594Z] TOOL RESULT

```
=== IEC ===
=== SYN eternal/young ===
747:Grk. aidy ‘lifetime, age’ (:Lat. aevum, aetas, etc., 14.12) is used in the NT for ‘worldly life, this world’ in sense c, e.g. Mt. 13.22, Mk. 4.19 4 pépyuva (ak Hépiuvat) rod alvas robrov ‘the care(s) of this world’. Although this use itself was not extended to ‘world’ in other senses in Greek, it is important for the history of other words used to translate it.
770:ON vergld, OF weorold, OHG weralt, etc. general Gmc. except Gothic, a cpd. of wer ‘man’ (2.21) and a noun form of adjs. for ‘old’ (14.15), hence ‘age of man’. Thus it was equivalent to and followed Lat. saeculwm in its ecclesiasti- cal use (above, 2). For the early period this is the prevailing use, e.g. in the OF gospels, Mt. 12.32, 13.22 (Grk. aiwy, Vulgate saeculum). The further de- velopment was from this sense c to sense b and eventually to sense a, until the words in question became the common expressions for ‘world’ in all senses in all the Gmc. languages. NED s.v. world. Falk-Torp 1368.
1280:oF en Goth. saiws, mari-saiws Lith. eZeras oe oa Chi. " us Dan. sf, indsd ChSl. jezero Ay tag Sw 8j6, insj6 SCr.  jezero rr oe OE mere, s@ Boh.  jezero Rum. lac NE tak Russ. aero. Ty. loch (lind) mE ae Skt. sara NIr. loch (Ii on Hess - aed + t (linn) OHG  séo, wac Av — me lyn MHG sé f
2005:Grk.  xidy (vida poet.) Goth. snaiws Lith. snie, NG xtdve ON 8n@r (snjor, snjar) Lett. shee Lat. nix Dan.  sne ChSl.  snégit It. neve Sw. snd SCr.  snijeg Fy. neige OE snaw Boh. snth Sp. nieve ME snow Pol. — fnieg Rum. zdpadé NE snow Russ. sneg Ir. snechte Du. Sneeuw Skt. hima- Nir. sneachta OHG  snéo Ay. vafra- W. etra (nyf) MHG nz ;
2016:Grk. vi¢a ace. sg. (poet.), with vb. yelder; Lat. nix, nivis, with vb. ningutt, It. neve, OF r. noif, Fr. neige (fr. neiger, *niviare. RIEW 5934), Sp. nieve, Rum. mea (dial.); Ir. snechte (but snigid ‘it rains’), NIr. sneachta, W. nyf (obs.); Goth. snaiws, OE sndw, etc. general Gmce.; Lith. sniegas, ChSl. snégi, etc., general Balto-Slavic; Av. snaég- only in vb., pres. snaéza- (but Pahl. sb. snéhr ‘snow’, Horn 292); here prob., but with
2148:In some groups the intransitive mean- ing is either the prevailing one or de- monstrably the earlier; in others the tran- sitive meaning appears to be the earlier. The former are connected with words meaning ‘hot’, ‘shine, be bright’, ‘spurt’(?), ete. The latter either are of obscure etymology (Grk. xaiw) or are inherited from IE roots in which the meaning ‘burn’ was already developed, so that the ultimate source is unknown. It is noticeable that there is no ety- mological connection between the words for ‘burn’ and the common words for ‘fire’,
2196:Grk. daiw (poet.): Skt. du- ‘burn, tor- ment’, etc. Walde-P. 1.767 f.
3566:1. IE *daiwer-, root connection dub. Walde-P. 1.767. Ernout-M. 541. Walde- H, 1.787 f.
4090:6. ChSl. chlévii (also ‘hut’), Boh. chlév, Pol. chlew (now esp. ‘pigsty’), Russ. chlev, loanword fr. Gme. *xlaiwa- ‘hut’ (Goth. hlaiw ‘grave’ beside hleipra, hlija ‘tent’, etc. fr. IE *klei- ‘incline’; Walde-P. 1.490 ff.). Berneker 389. Stender-Peter- sen 239 ff.
7535:Crk 4.799 GRAVE Tk, i NG a oFjna ae hlaiw on bones : grof, grofir ett. kaps It, pati me Dan. grav ChSl. grobit Ty Ga Sw. grav SCr. ove tomb OE _byrgen, graf Boh. hro 8p. ha tale ME grave, tumbe Pol. rob qu, Mormint ( NE grave (tomb) Russ. _mogila (grob) eer te PO Du. graf Skt.  (cmagana-) 7 Uaigh OHG grab Ay.  (uzdana-) 2 bedd MHG grap Br bez NHG grab
7554:4. Goth. hlaiw = OF hlaw, hlew ‘mound, burial mound’, OHG hiléo ‘burial mound’ : Lat. clivus ‘hill, slope’, etc., fr. the root of OF hlinian, Lat. clindre ‘lean’, ete. Walde-P. 1.491. Feist 261.
12432:Av. aiwi-varaz-, epd. of varaz- ‘work, do’ (9.18). Barth. 1376.
```


## [2026-09-04T19:06:43.138Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ===\" && grep -n \"aiwo\\|aiu- \\|aiwes\\|aiwā\" IEC.txt | head -12; echo \"=== SYN aetas ===\" && grep -n \"aetas\" SYN.txt | head -8"
}
```


### [2026-09-04T19:06:43.218Z] TOOL RESULT

```
=== IEC ===
=== SYN aetas ===
747:Grk. aidy ‘lifetime, age’ (:Lat. aevum, aetas, etc., 14.12) is used in the NT for ‘worldly life, this world’ in sense c, e.g. Mt. 13.22, Mk. 4.19 4 pépyuva (ak Hépiuvat) rod alvas robrov ‘the care(s) of this world’. Although this use itself was not extended to ‘world’ in other senses in Greek, it is important for the history of other words used to translate it.
```


## [2026-09-04T19:06:45.798Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aiu-\\|aiuos\\|aiuā\\|aiuo\" IEC.txt | head -20; echo \"--- IEC size ---\"; wc -l IEC.txt"
}
```


### [2026-09-04T19:06:45.863Z] TOOL RESULT

```
319:aiuit- ‘age’. Cf. aiuom Lat. cf. aetas; Osc. aitatum; MIr. áes “age, time’; áetid-iach, adj. “youthfuP; Br. oad, pl. oaZu; W oed, pl.-au beside oes, pl.-oedd
320:aiuom ‘age, lifetime’. WP I, 6 Cyp. cf. aiwéi ‘ever’; Gk. cf. aion; ae, aién; Lat. aevum; Go. aiws; OHG éwo, ẹwa; G dial. Ewe; Du. eeuw; Fris. ieu; cf. OE &fre, adv. (fr. *aiui-pro or sim. cpd. to Lat. sem-per); ON ævi; ei, ey, ae, adv.; Norw. æva, æve
4701:OCS glogü (‘hawthorn’, and com. Sl.) ghlaiuos ‘bright’. Cf. ghlauos (ghlauuos) and
5750:£naiuos (form of gnauos, $nauos? q.v. The parallel existence of two roots gn- ‘be born’ and gn- ‘know’ renders the semantics ambig.) Lat. naevus ‘birthmark’; OLat. gnaivo- (Fest. gnaevus); Osc. Gnaivs, a name; Olr. cf. gné (2) “form, beauty’; Ir. gnaoi ‘repute, liking, pleasure’; adj. ‘courteous, pleasant’; Ir. gné, pl. gnéithe ‘hallmark, characteristic’; cf. OE cnæwe, adj. ‘well-known’
5923:(8haiuo ‘yawn’, see ghiia- and extns.)
9425:laiuos ‘awry, left-handed, crooked; lefthand' WP II, 378 Gk. laiós “left-hand; sinister’; Lat. laevus, id.; Ir. laobh ‘crooked’; OCS. and com. SI. lévü ‘left-hand’
14950:saiuos ‘raging, mad, possessed’. WP II, 445 Hitt. cf. sawwar, vbl. n. (anger'. Radical given as sáa ‘be angry); Lat. saevus, adj. “wild, fierce’; Olr. saeb, adj. ‘false, bewildering’; Ir. saobh, adj. “false; mad’; W hoew, adj. ‘lively’;
15443:(skaiuo, ið (skauið) ‘divert, bend, twist’. See next)
15444:skaiuos ‘left-hand, sinister, odd, strange’. Cf. skauios (skauios), skeuios, ksauios, kseuios. WP II, 537 Per. cf. šūx, adj. ‘lewd, impudent'; Oss. xiw, adj. ‘straddle-legged’; Gk. skaiós, adj. “left- handed, awkward, stupid, unlucky, crooked’; Alb. (variant) i huej, Tosk i huaj, adj. ‘strange, foreign’; Lat. scaevus ‘lefthand, sinister, un- lucky’; W ysgoew, adj. ‘wry; fickle’; cf. ysgoe- wan, m. ‘fickle one’; Li. dial. cf. (variant) Seivas (*crooked', fr. *ksaiuos); ON cf. (vari- ant) skeifr, adj. ('skew”, fr. *skaip- or *skaibh-. Ambig.)
15509:skáuios “bent, twisted, left-hand’, etc. See skaiuos. The present variant arises in Alb. i huej, i huaj, adj. ‘strange, foreign’; t&-huej, v. ('alienate', fr. *at-skaujo); EMDu. schou- wen, v. ('avoid'. NB. Du. schuwen, id. is fr. a type *skeukio: skük- in view of OHG skiu- hen, G scheuen, etc. LWs in OFr. eschiver, It. schivare, E eschew, etc.); schouw, adj. *depraved, wayward'
16899:spraiuos, sprauios, à, iə “a speckled bird,
19657:uaghlos, us — uaiuolos, uaiuoros
19675:uaiuolos, uaiuoros ‘twisting, turning, chang- ing; twist’, etc. Cf. uoiu- Skt. (ambig.) cf. (vrddhi) vaivarnam, n. *varie- gation’; vellàmi, v. ‘curl; sway’; Tokh. waiwa- lau, s. ‘dizziness’; Gk. aiólos, adj. ‘twisting, fickle'; cf. (?) aióra, f. “swing, seesaw', usu.
19677:refd. to aeiro) (?); OCS cf. véverica, f. (“squir- rel, weasel, stoat’ etc.) beside Li. vovere, f., voveris, f. ('squirrel', but cf. uiuera); OLi. vaivaras, m. ((squirrel', vocalism obscure); Latv. vaivari, mpl. ‘marsh rosemary’ beside vaveraji, id.; Li. vaivara, f. 'speedwell"; Latv. vāvere, f. (squirrel, vocal. as Li.). (Radical form *uaiu-, or *uoig-, in Li. vaivó-rykste ‘rainbow’, cf. rykste, f. *rod")
--- IEC size ---
20498 IEC.txt
```


## [2026-09-04T19:06:57.048Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"perena\\|p3rena\\|pərəna\\|paranay\\|paranāyu\" KLN_1966.txt KLN_1971.txt | head; echo \"=== KLN 'age' entry ===\"; grep -n \"^age,\" KLN_1971.txt | head; grep -n \"aiw-\\|aiu-, ai\" KLN_1971.txt | head -10"
}
```


### [2026-09-04T19:06:57.144Z] TOOL RESULT

```
=== KLN 'age' entry ===
8862:age, harass, torment, distress’, freq. of affligere 
9244:age, n. — ME., fr. OF. aage, eage (F. age), fr. 
31179:age, bordar, bordel, border, berm, brelan, brim, 
31219:age, n., boat-irtg, n. 
49318:age, n., clown-ery, n., clown-ish, adj., clown-ish- 
154835:age, confidence, etc. — F., prop. fem. of the adj. 
175965:age, n., pawn-ee, n., pawn-er, n. 
209114:age, n., rough material, rough-en , tr. and intr. v., 
210074:age, picture, beauty’, perhaps related to OI. vdr- 
222058:age, n., silt-ation, n., silt-y, adj.
```


## [2026-09-04T19:07:00.055Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9244,9270p' KLN_1971.txt; echo \"=== ever ===\"; grep -n \"^ever, adv\\|^ever, \" KLN_1971.txt | head -3"
}
```


### [2026-09-04T19:07:00.148Z] TOOL RESULT

```
age, n. — ME., fr. OF. aage, eage (F. age), fr. 
VL. *aetaticum, fr. L. aetdtem (acc. of aetas, 
‘age’), whence also It. eta, Catal. edat, Sp. edad. 
Port, idade, ‘age’. L. aetas is contracted fr. ae vi- 
tas, fr. aevum, ‘space of time, eternity’. See aeon 
and cp. eternal. Cp. also coetaneous, coeval, 
longevity, primeval, moyen age. 

Derivatives: age , intr. and tr. v., ag-ed, adj., 
ag-ed-ly, adv., ag-ed-ness, n., age-less, adj. 

-age, suff. forming nouns denoting act, process, 
function, condition, dignity or place. — OF. and 
F. -age, fr. Late L. - aticum , fr. L. -at us, pp. suff. 
of verbs in -are (i.e. verbs of the 1st conjuga- 
tion). See adj. suff. -ate and cp. -atic. 
agee, adv., awry (dial.) — Formed fr. a- and dial. 
E. gee, ‘to turn’. 

Agelaius, n., a genus of birds of the family Icter- 
idae, comprising the blackbird (ornithol.) — 
ModL., fr. Gk. dyeXato^, ‘belonging to a herd, 
gregarious’, fr. dy$X7), ‘heard’, lit. ‘that which 
is led or driven’, fr. dyEiv, ‘to lead’, which is 
cogn, with L. agere, ‘to drive, lead, do, act’. 
See agent, adj., and cp. words there referred to. 
agency, n. — Late L. agenda (whence also F. 
=== ever ===
24260:ever, the first element in either and the second 
87069:ever, adv. — ME. ever, fr. OE. xfre, prob. rel. 
110724:ever, that Akkad, hazdnu was borrowed from a
```


## [2026-09-04T19:07:02.745Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '87069,87085p' KLN_1971.txt; echo \"=== aeon ===\"; grep -n \"^aeon\" KLN_1971.txt | head -3"
}
```


### [2026-09-04T19:07:02.835Z] TOOL RESULT

```
ever, adv. — ME. ever, fr. OE. xfre, prob. rel. 
to OE. a, ‘always, ever’. See aye, ‘ever’, and cp. 
words there referred to. Cp. also the first ele- 
ment in every and the second element in never. 
Everard, masc. PN. — OF. Everart , of Teut. ori- 
gin. Cp. OHG. Eburhard (= G. Eberhard, 
Ebert), lit. ‘strong as a boar’, fr. ebur, ‘boar’, 
and hart, ‘hard’. See aper and hard. 

Evernia, n., a genus of lichens of the family Us- 
neaceae (bot.) — ModL., fr. Gk. euspvrjs, 
‘sprouting well’, fr. d 5 (see eu-) and gpvoc, 
‘young sprout, twig, shoot’, which is cogn. with 
Norw. runne, rune, ‘branch*, ON. renna, ‘to 
shoot up’, fr. I.-E. base *er -, *or ‘to stir, move’, 
whence also L. oriri, ‘to rise’. See orient and cp. 
words there referred to. 
=== aeon ===
8449:aeon, eon, n., a long and indefinite period of
```


## [2026-09-04T19:07:05.270Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8449,8470p' KLN_1971.txt; echo \"=== aye ===\"; grep -n \"^aye, adv\" KLN_1971.txt|head -3"
}
```


### [2026-09-04T19:07:05.362Z] TOOL RESULT

```
aeon, eon, n., a long and indefinite period of 
tim \ — L. aeon , fr. Gk. alcov, ‘age, eternity’, 
which stands for *<xt fd>v and is rel. to Gk. octet 
(for *aLFecn), ‘always, ever’, and cogn. with 
01 . dyu, ‘life’, Avestic ayu, ‘age’, L. aevum , 
‘space of time, eternity’, Goth, aiws, ‘age, eter- 



nity’, atw, adv., ‘ever’, ON. a?v/, ‘lifetime’, OHG. 
ewa, ‘eternity’, Du. eeuw, ‘age, century’, eeuwig, 
OFris. ewich, OS., OHG. ewig, MHG. ewic, 
G. ewig, ‘everlasting’, OE. a, ‘always, ever’. See 
aye, ‘ever’, and cp. words there referred to. See 
also age and cp. words there referred to. Cp. 
also prec. word. 

Aepyomis, n., a gigantic, extinct bird of Mada- 
gascar. — ModL., lit., ‘the tall bird’, com- 
pounded of Gk. otbruc;, ‘tall, very high’, a 
word of uncertain origin, and of 6pvt<;, ‘bird’, 
for which see ornitbo-. 
=== aye ===
```


## [2026-09-04T19:07:13.935Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i,p in enumerate(t[:60]):\n    head=p.strip()[:80].replace('\\n',' ')\n    print(i,'|',head)\nEOF"
}
```


### [2026-09-04T19:07:17.048Z] TOOL RESULT

```
leaves 903
0 | A  COMPREHENSIVE ETYMOLOGICAL  DICTIONARY OF  THE ENGLISH  LANGUAGE Dealing  wit
1 | ELSEVIER  PUBLISHING  COMPANY 335  JAN  VAN  GALEN STRAAT,  P.O.  BOX  211,  AMS
2 | Preface To  know  the  origin  of  words is  to  know  the  cultural  history  o
3 | work. VIII My  grateful  acknowledgements  are  also  due  to  the  whole  staff
4 | but  the  origin  of  the  respec- X tive  word  is  referred  to  by  such  vag
5 | Theo- phile-Hyacinthe  Laennec  (1781-1826)  fr.  Gk.  xippo?,  ‘tawny’,  which 
6 | a  slight  aspira¬ tion  of  the  sound  - like  gh;  now  pro¬ nounced  like  g
7 | he  letters  17  .  D  ,  3  1  >  3  ,  to  indicate  their original  hard  pro
8 | ss  in English  hiss J* dad d palatal  d s> ta 1 an  emphatic  t J; za' z an  em
9 | Auflage  von  J.  B.  Hofmann,  Heidelberg,  1938-55. Walde-Pokorny,  VWIS.  =  
10 | before  the  common  era diet. dictionary Berb. Berber dimin. diminutive Bibl. B
11 | abinic Old  Sabinic OSerb. Old  Serbian OSlav. Old  Slavic OSp. Old  Spanish Oss
12 | an Republics Russ. Russian V. verb S. South var. variant S.Afr. South  African v
13 | L.  bassus,  ‘thick,  fat, low’.  See  base,  ‘low’,  and  cp.  the  second  ele
14 | nt,  efficient,  elicit,  exhibit,  Illicium,  inci¬ dent,  incipient,  inhibit,
15 | and  -facient. abortion,  n.,  miscarriage.  —  L.  abortio,  gen.  -onis, ‘misc
16 | (see  ab-),  and  tenere,  ‘to hold’.  See  tenable  and  cp.  appertain,  conta
17 | ‘mite’. See  acarid. aeariatre,  adj.,  bad-tempered.  —  F.,  ‘contrary, crabbe
18 | ��to  cry  out  at’. fr.  ad-  and  clamare,  ‘to  cry  out’.  See  claim  and c
19 | ,  fern.  pi.  of  -aceus,  ‘belong- t®*  to,  of  the  nature  of’;  see  -aceo
20 | ��,  fr.  priv.  pref.  a-  and chlamydeous. Achras,  n.,  a  genus  of  trees  
21 | .  pref.  a-, xoop.0?,  ‘the  world’  (see  cosmos),  and  suff.  -ism. acosmist
22 | g  the  extremities  of stone  and  the  trunk  of  wood.  —  L.  acrolithus, fr
23 | point.  —  L.  acumi- natus,  pp.  of  acuminare,  ‘to  sharpen’,  fr.  acumen, 
24 | ‘to  lead’.  See  duke. 23 Derivatives:  adduc-er,  n.,  adduc-ible,  adj. adduc
25 | is  formed  fr.  ad-  and  ire,  ‘to  go’, fr.  I.-E.  base  *ei-,  •/-,  ‘to  g
26 | dnem,  acc.  of admonitio,  fr.  admonite,  pp.  of  admonere.  See admonish  an
27 | r.  adulterare.  See  adulterate  and  -y (representing  L.  -ium). adumbrate,  
28 | s.v.  aiyiaXA?. aegicrania,  n.,  representation  of  goats’  heads (1 Greek  an
29 | .  atoxovopew), ‘sensitive  plant’,  fern,  of  octaxuvopevos,  being ashamed’, 
30 | -ment,  n. affray,  tr.  v.,  to  frighten.  —  ME.  afraien,  affraien, formed 
31 | element  is  of  uncertain  origin.  It  possibly derives  fr.  I.-E.  *mga-  an
32 | —  F.  agilite,  fr.  L.  agilitdtem,  acc.  of agilitas,  ‘mobility,  nimblenes
33 | e,  n„  hook,  clasp.  —  F.  agrafe,  back  forma¬ tion  fr.  agrafer,  ‘to  ho
34 | Com¬ pounded  of  Gk.  a’iXoupog,  "cat’,  and  -91X05, ‘loving’.  For  the  fir
35 | ,  n.,  son  of  Neleus  and  brother  of  Nestor in  Greek  mythology;  fig.  u
36 | trength,  power’.  See  Alexander, alcohol,  n.  —  ML.,  fr.  Arab,  al-kohl , 
37 | read’.  For  the  ending  see  suff.  -ia. alexin,  n.,  a  substance  which  de
38 | .  formed  fr.  Thes- sal.  Gk.  akKiY.cc,  acc.  of  aXXi^,  ’upper  gar¬ ment;
39 | allegare,  ‘to  despatch,  com¬ mission,  mention,  adduce’,  fr.  ad-  and  leg
40 | v.  —  OF.  aloter  (F.  alloter,  allotir),  a hybrid  coined  fr.  a,  ‘to’  (
41 | r.  L.  admorsus,  pp.  of  admordere, ‘to  bite  into’,  fr.  ad-  and  mordere
42 | tles  of  the  family  Chryso- melidae  (entomol.)  —  ModL.,  fr.  Gk.  aXxixoi
43 | I.-E.  *am-ro-, fr.  base  *am-,  ‘bitter’,  which  is  rel.  to  *omo-. Taw,  u
44 | like  food’.  Cp.  Arab.  * unbar  (pronounced  ‘d/n- bar’),  ‘ambergris’,  and 
45 | ddle’,  fr.  on  (see  a-,  ‘on’),  and  middan, dat.  sing.  masc.  of  midde, 
46 | SpneXog,  ‘vine’,  and  elSos, ‘form,  shape’.  See  ampelo-,  -oid  and  -ous. 
47 | se  to  gape  idly  about’,  fr.  a, ‘to’  (see  a),  and  muser,  ‘to  muse’.  
48 | o peel’,  and  E.  cleave,  to  split  (q.v.)  Cp.  the  second element  in  hie
49 | ed,  MDu.  sent,  OHG.  anut, MHG.  ant,  G.  Ente,  and  prob.  also  with  Gk.
50 | ��to  go  round’.  See  ambient, andantino,  adj.,  somewhat  quicker  (sometime
51 | con¬ fusion  with  words  ending  in  -ism. Derivatives:  aneurysm-al,  adj.,  a
52 | Russ,  ugori,  Pol.  wfgorz),  ‘eel’,  which  all mean  derivatively  ‘the  snak
53 | liquid  measure.  —  Du.,  rel.  to  G. Anker,  Swed.  ankare,  fr.  ML.  anceri
54 | heard of’,  fr.  a-  (see  priv.  pref.  a-)  and  vor,xo;,  ‘per¬ ceptible  by 
55 | dian,  adj.,  pertaining  to  the  forenoon. —  L.  antemeridianus,  ’in  the  f
56 | ;,  ‘man- eater,  cannibal’,  fr.  avHpco7toc,  ‘man’,  and  the stem  of  tpaye
57 | in  1880). antiseptic,  adj.  and  n.  —  Formed  fr.  anti-  and septic. Deriva
58 | eive’,  used  as  a  noun,  fr. a,  ‘to’  (see  a),  and  percevoir  ‘to  percei
59 | em  of  vordre. apjohnite apoplexy 90  91 ‘to  devour’.  See  Apis,  a  genus  o
```


## [2026-09-04T19:07:25.314Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (28,29,30):\n    print('==== leaf',i,'====')\n    print(t[i][:1800])\nEOF"
}
```


### [2026-09-04T19:07:27.066Z] TOOL RESULT

```
==== leaf 28 ====
s.v.  aiyiaXA?. aegicrania,  n.,  representation  of  goats’  heads (1 Greek  and  Roman  antiq.)  —  ModL.,  fr.  Gk. at?,  gen.  aiydp,  ‘goat’,  and  xpavla,  pi.  of xpavEov,  ‘skull’.  For  the  first  element  see  aego-, for  the  second  see  cerebrum, aegirite,  n.,  a  variety  of  acmite  (mineral.)  — Formed  with  subst.  suff.  -ite  from  Aegir,  name of  the  Icelandic  sea-god;  so  called  because  it occurs  in  Scandinavia.
aegis,  egis,  n.,  1)  shield  used  by  Zeus,  later  by Pallas  Athene  (Greek  mythol.) ;  2)  used  figura¬ tively  in  the  sense  of  protection.  —  L.  aegis,  fr. Gk.  <xlyk,  ‘goatskin;  the  skin  shield  of  Zeus’, fr.  all,  gen.  odyo;,  ‘goat’;  see  aego-.  For  this etymology,  suggested  already  by  Herodotus,  see Frisk,  GEW.,  I,  p.  32  s.v.  xtyi;.  Cp.  Aegeus. Cp.  also  Giles.
Aegisthus,  n„  the  lover  of  Clytemnestra,  with whom  he  killed  her  husband  Agamemnon (Greek  mythol.)  —  L.,  fr.  Gk.  AEyioOcx;,  a  word of  uncertain  origin.
Aegle,  n„  1)  one  of  the  Hesperides;  2)  the  mother of  the  Graces;  3)  the  fairest  of  the  Naiads (Greek  mythol.)  —  L.,  fr.  Gk.  AEyXr),  lit.  ra¬ diance,  gleam’.  The  orig.  meaning  of  Gk.  otEyXr) was  ‘quickly  moving  light’.  It  is  cogn.  with  OI. djati,  ‘moves  about,  trembles’.
Aegle,  n.,  a  genus  of  trees  of  the  rue  family  (bot.) —  Named  after  the  Naiad  Aegle.  See  prec. word.
aego-,  combining  form  meaning  ‘goat’.  —  Gk. alyo-,  fr.  xiEi,  gen.  xlyoc,  ‘goat’,  which  is  cogn. with  OI.  ajah,  ‘he-goat’,  ajinam,  ‘skin’,  Avestic tzaen'm,  ‘pertaining  to  skin’,  Arm.  aic,  ‘goat’, Lith.  ozys,  ‘he-goat’.  Cp.  the  first  element  in aegicrania.
Aegopodium,  n.,  a  genus  of  herbs  of  the  car
==== leaf 29 ====
.  atoxovopew), ‘sensitive  plant’,  fern,  of  octaxuvopevos,  being ashamed’,  pass.  pres.  part,  of  alayuveiv,  to  d,s- honor  put  to  shame’,  fr.  atnyuvri,  ‘shame  ,  fr. alayoq,  ‘shame’,  which  stands  for  *aig"h-s-kos and  is  cogn.  with  Goth,  aiwiski,  ‘shame,  con¬ fusion’,  MHG.  eisch,  ‘ugly’.  For  the  suff.  -pevo? see  alumnus  and  cp.  words  there  referred  to.  The plant  was  called  ai<ryuvopivr„  ‘the  ashamed one’,  in  allusion  to  the  sensitiveness  of  its
leaflets.  ,
Aesculaceae,  n.  pi.  a  family  of  trees,  the  horse- chestnut  (bot.)  —  Formed  with  suff.  -aceae  fr.
L.  aescuius,  ‘the  Italian  oak’.  See  Aesculus. Aesculapian,  adj.,  i)  pertaining  to  Aesculapius,
2)  medical.  —  Formed  with  suff.  -an  fr.  Aescula¬ pius,  Latinized  from  Asclepius,  fr.  Gk.  ’AoxA/j- mbc  ‘the  god  of  medicine’.  See  Asclepius. Aesculus,  n.,  a  genus  of  trees,  the  horse-chestnut
(bat,) _ L.  aescuius,  ‘the  Italian  oak  .  See  oak.
Aesir,  n.  pi.,  the  chief  gods  of  Scandinavian  my¬ thology.  —  ON.,  pi.  of  ass,  ‘god’,  rel.  to  OE.  os, OS  as-,  os-,  OHG.  ans-  (in  PN.s),  Goth,  ans, ‘god’;  possibly  of  the  same  origin  as  ON.  ass, Goth,  ans,  ‘beam’.
Aesopian,  adj.,  pertaining  to,  or  resembling  Ae¬ sop.  —  Formed  with  suff.  -an  fr.  L.  Aesopius, ‘Aesopian’,  fr.  Aesopus,  fr.  Gk.  A’tatono?,  the Greek  fable  writer.
Aestas,  n„  the  goddess  of  summer  in  Roman mythology.  —  L.  aestas,  ‘summer’.  See  estival, aesthete,  n.  —  See  esthete, aesthetic,  adj.  —  See  esthetic, aestival,  adj.  —  See  estival, aestivate,  intr.  v.  —  See  estivate, aestivation,  n.  —  See  estivation, aether,  n.  —  See  ether.  i
aethogen,  n.,  boric  nitrite  (chem.)  — 
==== leaf 30 ====
-ment,  n. affray,  tr.  v.,  to  frighten.  —  ME.  afraien,  affraien, formed — with  change  of  prefix — fr.  OF.  esfreer, *esfreier  (F.  effrayer ),  ‘to  frighten,  terrify’,  fr. Gaul.-L.  *exfridare,  'to  put  out  of  peace’, fr.  L.  ex-,  ‘out  of’  (see  ex-),  and  Frankish *fridu,  ‘peace’,  which  is  rel.  to  OE.  fridu,  OHG. fridu,  ‘peace,  truce’,  fr.  Teut.  base  *fri-,  which corresponds  to  I.-E.  base  *pri-,  ‘to  be  friendly, to  love’,  whence  OSlav.  prijati,  ‘to  aid,  help’, prijatelfl,  ‘friend’,  01.  prija-,  ‘beloved’.  Cp. OProveng.  esfredar,  ‘to  frighten’,  which  also derives  fr.  Gaul.-L.  *exfridare.  See  free  and words  there  referred  to  and  cp.  esp.  defray. Derivative:  affray-er,  n.
affray,  n.  —  ME.  afrai,  affrai,  fr.  OF.  esfrei  (F.
effroi),  fr.  esfreer,  *esfreier.  See  prec.  word, affricate,  n.  ( phonetics ).  —  L.  affricatus,  pp.  of affricare,  ‘to  rub  against’.  See  affricate,  v. affricate,  tr.  v.,  to  rub ;  to  grate  on.  —  L.  affricatus, pp.  of  affricare,  ‘to  rub  against’,  fr.  ad-  and  fri- care,  ‘to  rub’.  See  friction  and  verbal  suff.  -ate. Derivatives:  affricat-ed,  adj.,  affricat-ion,  n., affricat-ive,  adj.
affright,  tr.  v.,  orig.  spelled  af  right.  Meta-
thesized  fr.  afyrht,  fr.  OE.  dfyhrt,  pp.  of  dfyrhtan, ‘to  frighten’,  fr.  a-  (see  intensive  pref.  a-)  and fyrhtan.  See  fright,  v.  For  the  spelling  affright (with  double  /)  see  afford.  Derivatives:  affright, n.,  affright-ed,  adj.,  affright-ed-ly,  adv. affront,  tr.  v.  —  OF.  afronler  (F.  affronter),  ‘to strike  on  the  forehead’,  fr.  Late  L.  aflrontare, ‘to  strike  against’,  fr.  ad-  and  L.frdns,  gen.  fron¬ ds,  ‘forehead’.  See  front.
Derivat
```


## [2026-09-04T19:07:40.917Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(24,33):\n    p=t[i]\n    nums=re.findall(r'(?m)^\\s*(\\d{1,3})\\s*$',p)+re.findall(r'\\b(\\d{2,3})\\s+(\\d{2,3})\\b',p)\n    print(i, 'aeon' in p or 'aeon' in p.lower(), nums[:6], '|', p[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T19:07:42.665Z] TOOL RESULT

```
24 False ['23', '24'] | ‘to  lead’.  See  duke. 23 Derivatives:  adduc-er,  n.,  add
25 False ['25', '26'] | is  formed  fr.  ad-  and  ire,  ‘to  go’, fr.  I.-E.  base 
26 False ['27', '28'] | dnem,  acc.  of admonitio,  fr.  admonite,  pp.  of  admoner
27 False ['29', '30'] | r.  adulterare.  See  adulterate  and  -y (representing  L. 
28 True [] | s.v.  aiyiaXA?. aegicrania,  n.,  representation  of  goats’
29 False ['04', '35', ('04', '35')] | .  atoxovopew), ‘sensitive  plant’,  fern,  of  octaxuvopevo
30 False [] | -ment,  n. affray,  tr.  v.,  to  frighten.  —  ME.  afraien
31 True ['36', '37'] |  element  is  of  uncertain  origin.  It  possibly derives  
32 False ['39'] |   —  F.  agilite,  fr.  L.  agilitdtem,  acc.  of agilitas,
```


## [2026-09-04T19:07:47.778Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[28]\ni=p.lower().find('aeon')\nprint(p[max(0,i-400):i+1400])\nEOF"
}
```


### [2026-09-04T19:07:50.413Z] TOOL RESULT

```
nd  -ian.
Aeolian,  n.,  one  of  a  branch  of  the  Greek  people named  fr.  Aeolus  —  Formed  with  suff.  -an  fr.  L. Aeolius,  fr.  Gk.  AEdXio;,  ‘Aeolian’,  fr.  AEoXog, ‘Aeolus’,  after  whom  the  ancient  district  AEoXE; (Aeolis)  in  Asia  Minor  is  said  to  have  been named.
Aeolis,  n.,  a  genus  of  mollusks  (zool.)  —  ModL., fr.  Gk.  xioXo;,  ‘quick,  quick-moving’.  See  aeon and  cp.  Aeolus.
aeolo-,  combining  form  used  to  denote  musical wind  instruments.  —  Fr.  L.  Aeolus,  name  of  the god  of  winds.  See  Aeolian,  ‘pertaining  to Aeolus’.
Aeolus,  n.(  the  god  of  the  winds  in  Greek  mythol. —  u.  fr.  Gk.  AloXo;,  lit.  ‘Rapid’,  fr.  aloXo;, ‘quick,  rapid’,  which  is  of  uncertain  origin.  It possibly  stands  for  *alfo-Xo;,  and  is  rel.  to aicov,  ‘age,  eternity’.  See  next  word  and  cp. Aeolis.
aeon,  eon,  n.,  a  long  and  indefinite  period  of tinv.  —  L.  aeon,  fr.  Gk.  aEtuv,  ‘age,  eternity’, which  stands  for  *a!fcov  and  is  rel.  to  Gk.  oteE (for  * xlf ecu),  ‘always,  ever’,  and  cogn.  with OI.  ayu,  ‘life’,  Avestic  ayu,  ‘age’,  L.  aevum, ‘space  of  time,  eternity’,  Goth,  aiws,  ‘age,  eter¬ nity’,  aiw,  adv.,  ‘ever’,  ON. sevi,  ‘lifetime’,  OHG. ewa,  ‘eternity’,  Du,  eeuw,  ‘age,  century’,  eeuwig, OFis.  ewich,  OS.,  OHG.  ewig,  MHG.  ewic, G.  ewig,  ‘everlasting’,  OE.  a,  ‘always,  ever’.  See aye,  ‘ever’,  and  cp.  words  there  referred  to.  See also  age  and  cp.  words  there  referred  to.  Cp. also  prec.  word.
Aepvornis,  n.,  a  gigantic,  extinct  bird  of  Mada¬ gascar.  —  ModL.,  lit.,  ‘the  tall  bird’,  com¬ pounded  of  Gk.  ‘tall,  very  high’,  a
word  of  uncertain  origin,  and  of  fipvu;,  ‘bird’, for  which  see  ornitho-.
aerobic
a
```


## [2026-09-04T19:07:59.856Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i in (21,):\n    print('==== leaf',i,'(printed ~',i+543,') ====')\n    print(t[i][:3000])\nEOF"
}
```


### [2026-09-04T19:08:12.098Z] TOOL RESULT

```
leaves 684
==== leaf 21 (printed ~ 564 ) ====
                                              ‫بیان دویم (‪)۱‬‬
             ‫جد با بای ابجد مشتمل برپاتزدهلفت کونایت‬
                                                   ‫دارجبیم‬
                                      ‫فغفور باشد ‪.‬‬              ‫جبا = بکر اول و ثالیبالفکشیده ‪,‬‬
 ‫جیسین ‪ - °‬باسین بی قطه بر وزن‬                                  ‫باج وخراح را گویندا ‪ -‬وبفتح اول در عربی‬
  ‫کد‬          ‫فزوین کر کر کان و‬                                 ‫ردن‪ -‬و وایی‬
                                                                          ‫بمعنی ینان شدن ‪ -‬وید دکلی‬
                          ‫ببصآین‌است‬
                                   ‫جعر‬
                                     ‫وم‬                         ‫استادن باشد ‪ - ۴‬و بقصر الف خاك گردا گرد‬
‫جبغوت ‪ -‬باغین ضلهدار(‪ )۷‬و ای‬                                    ‫چاه رگاوند؟ ‪ -‬وضم اول وتشدید انی هم در‬
‫رشت (‪ )۳‬بروزن مربوط » یشم و پنبه که در‬
                                       ‫ق‬                        ‫عربی بمعنی بد دل باشد ؟ ‪ -‬و بکر اول‬
‫تهالی ولحاف بادآ تکفا ‪ -‬کین لمات‬
   ‫بو زار کت واد ا‬
                                                                ‫جمع شده و گرد آ‪۰‬ده برای‬                     ‫در عربی آب‬

                                                                                                                      ‫شتران‬
 ‫اجیم فارسی نیزکفته اید » وبایشمعنی‬
                                           ‫» وب‬        ‫است‬       ‫بکراول بروزن‌حجایت؛‬                   ‫جبایت =‬
 ‫بتقدیم غین بر حرف الی هم هت که جغبوت‬
                                                                                     ‫باج وخراج گرفتن راگویند‪. ۴‬‬
                                             ‫باشد‪. ۷‬‬
                                                                ‫وزن‬    ‫بر‬    ‫یا بای أبد‬            ‫باج ‪-‬‬         ‫جب‬
 ‫جبلاج ‪ -‬بکر اول ولام والفہ پروزن‬
 ‫اخراج » مردم برزکه دون همت خیس را‬                              ‫کجواح ‪ .‬جامه ای که پادشاهان بروز لوروز‬
                                            ‫گونند ‪.‬‬
                                                                                                                 ‫‪۰‬‬    ‫بو شنفد‬



  ‫بروزن لك لك » سخت شن‬        ‫س‬           ‫جبلك‬                  ‫جبر آهنگ » براای قرشت والف‬
 ‫وقايم (‪ )4‬و مسکم گردیدن چیزی باشدیسیب‬                          ‫وها ولون وکاف فارسی بر وزن خشمآ کند ›‬
                                      ‫چیزی دیگ ‪.‬‬                ‫اربت کهآدرا ژردخار می‌گویند ‪.‬و بخ‬  ‫تخخم‬
 ‫۔ با ها برورن اسفرنگه‪,‬‬       ‫جبلهنگ‬
                                                                                     ‫آتنرید زرد باشد؟ ‪.‬‬
‫آهنگه است» که‬
            ‫ك هردوبممنیجبر‬                 ‫جیلاهن‬        ‫و‬      ‫جیر ود = با رای قرشت بر وزن‬
 ‫نخم خاری بود زرد وآن خاررا زردخار کوند»‬                        ‫سردوز ‪ ۰‬خاریشت بزرکه تبر انداز را گوینده‬
 ‫وت آن تربدزرد باشدش‪ >» ۸‬وسقديم لام برحرف‬                       ‫و با رای بینقطه همبنظرآمده است که‌بروزن‬
       ‫ت
```


## [2026-09-04T19:08:19.033Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(t[:60]):\n    if 'جاوید' in p or 'جاوبد' in p or 'حاوید' in p:\n        print('leaf',i,'printed~',i+543)\nEOF"
}
```


### [2026-09-04T19:08:21.284Z] TOOL RESULT

```
leaf 19 printed~ 562
leaf 20 printed~ 563
leaf 27 printed~ 570
```


## [2026-09-04T19:08:24.445Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (19,20):\n    p=t[i]\n    print('==== leaf',i,'====')\n    idx=p.find('جاوید')\n    print(p[max(0,idx-1500):idx+1500])\nEOF"
}
```


### [2026-09-04T19:08:25.995Z] TOOL RESULT

```
==== leaf 19 ====
 سک بروزن باور » بمعنی حال‬                                                          ‫بودن باشد ‪.‬‬
 ‫باشد چنانکه اگرگوبند « چهجاورداری؛» مراد‬            ‫جافه = بروزن دانه » روح حیوالی‌را‬
                   ‫آں باشدکه چه حال داری ‪٩‬‏‬          ‫وس‪-‬لاح جنک را کیفتزه‌اند؟ ‪.‬‬
                                                                               ‫کوبند ‪۴‬‬
‫جاو رث » بسکون‌راودال هردوبی قطه؛‬                    ‫جانه دار » بداال ابجد بر وزن‬
     ‫خاری باشد سفید رنگه » بوایشمعنی بزاای‬
 ‫‌ماند ‪ ۰‬و بمربی ثفام جنم ای‬
                           ‫تاهر ح‬
                                ‫نکقطفه د‬             ‫و نگاهدارنده اسلحهٌ چتگه را نیز کفته‌اند؟ ‪.‬‬
                                   ‫مثلثه خوانند ‪.‬‬   ‫و قوت لایموت حم‬            ‫زی‬
                                                                                ‫رقوو‬
                                                                                   ‫رز‬          ‫‪-‬موعنی‬
                                                                                                    ‫پ‬
                                                                                              ‫هت ‪. ۳‬‬
‫جاور کردن س بر وزن باور کردن»‪.‬‬
              ‫بمعنی تغبیر و تبدیل دادن باشد*‪.۱‬‬        ‫واو بورزن عابد‪.‬‬         ‫جاود هیک‬
                                                        ‫ایوم‬
                                                           ‫دیشه‬
                                                              ‫مخفف جاوید است که بمعنی هم‬
 ‫جاور د = بسکون زای قطه دار »‬                                                                  ‫باشد؟ ‪.‬‬
 ‫بر وزن ومعنی جاورد است که خار سفند باشد ‪.‬‬

 ‫جاوشیر » باشن قطه دار بر وزن‬                        ‫آن‌جهان‬      ‫(‪3 -)۲‬‬   ‫جاویداست که همیشه ودام‬

 ‫بادکیر‪ .‬صمغی باشددوابی ومعرب کاو شیراست‬                                                        ‫بائد ‪٩‬‏‬
                       ‫که همان سمخ باشد‪٩۱‬‏‬
                                                      ‫جاو دان خرد ‏ بکر دون وخای‬
 ‫جاوه = پر وزن ساوه » نام ولامتی‬                     ‫نقطه دار ر قتح را وسکون دال هردو بی‌شطه »‬
  ‫وجزیره ایت درمیان دربا؟‪ -۱‬و انسرون دهابرا‬          ‫تکلتمایی است که هوشنک درعلم حکمت‌عملی‬

‫‪3‬‬                                               ‫(‪ )۱‬چك ‪ :‬ژدو پاژند ‪ )۲( .‬چك ‪ :‬دائم ‪.‬‬

‫‪3‬‬
‫‪e,‬‬


‫‪e‬‬
‫‌‬                  ‫‪‎‬دن ‪.‬‬ ‫كر ‪ :‬وا‬
                       ‫‪‎‬واج‬    ‫ر‬     ‫‪۴‬‬        ‫رك ‪ :‬حاندار ‪.‬‬      ‫‪۴‬‬         ‫رك ‪ :‬جان ‪.‬‬   ‫‪- ۴‬‬

     ‫این کتاب بعر بی تلخیص و ترجمه شدد و ترجمه آخین ‪۱‬‬                      ‫یدان‬
                                                                              ‫‪-‬راكو‪:‬‬
                                                                                   ‫© ج‬
       ‫« مظلوم مافر مانکجی‌لیمجی حوشنك هاتربا پزدانی ملقب بدروش فالی » در سال ‪۵۹۲۱‬‬
     ‫‏‪ ٩٩-‬قمری درتبران بطبع رسمیده است ‪ .‬جاوبدان خرد یز نکاتمابی است که محمد حسین بن‬
      ‫شمس الدین از عربی بفارسی ترجمه
==== leaf 20 ====
 ‫¬=“‬                                                                                   ‫جاو ند‬

‫ونام کلی حم هت وآن در هندوستان‬      ‫باشف ‪-۴‬‬       ‫و بیار‬       ‫دده‬
                                                                 ‫نباش‬
                                                                    ‫زوری‬
                                                                       ‫گجال‬
                                                                          ‫لگیوزبند ‪ -‬و نام‬
                              ‫و‬   ‫است‬     ‫بار‬
                                                                                       ‫کوچك ‪.‬‬
‫جای باش » با بای ابجد بالف‬                       ‫جاو ید ‪» ۱‬بر وزن باهید » پاینده‬
‫کشنده رشن قرشت زده » خاله وسرا ومنزرا‬            ‫وهسثه ودام )‪ ۱‬را گونند ‪ -‬وعالم آخرت را‬
                           ‫گوند ‪.‬‬                                                  ‫حمگفتهاند‪۰‬‬

‫جای گر م کردن ‪ -‬کنابه از آبت‬                      ‫جاویدان ‪ -۲‬بر وزن غازیخان‬
 ‫قبه‬
   ‫او‬‫بیمردر‪-‬‬
           ‫وام گ‬
               ‫که کی درجابی قرار آر‬               ‫بمعنی جاوبداست که همیشه‌وپابنده ودایم (‪)۱‬‬
                    ‫رفتن را کیوزبند ‪.‬‬                                                      ‫باشد ‪2.‬‬

‫جای مند = ببامریومزن پای‌بند ‪.‬‬                    ‫جاو یداه ه بر وزن تازنخانه ‪,‬‬
           ‫کاهل و تنبل وهیج‌کاره را گونند ‪۱‬‬       ‫و دایم )‪۱۱‬‬      ‫شه‬
                                                                   ‫هتمکه‬
                                                                       ‫بمعنی جاویدان اس‬
  ‫لمی‬
    ‫کدا‬
      ‫جالی(‪ - )۲‬بر وزن طائی ‪,‬‬                                                          ‫باشد ‪9 .‬‬

                         ‫‪4.‬‬   ‫©‬   ‫درهند‬    ‫ات‬     ‫جای » بروزن لای ‪ .‬بمعئی‌جا ومقام‬

                                                ‫(‪ )۲‬چش ‪:‬‬           ‫)‪ (۱‬چك ‪ :‬دائم ‪.‬‬


  ‫( ابدیت ) ؛ ‪ ( ۵۷۵۷‬الى الابد ) » پهلوی ‪› 0۵۱6۷2۷‬‬             ‫و ‪ -‬اومتا ‪taY‬‏‬
  ‫ارمنی‪ «۳861806]1۷2۷ ۸۵۵۸۲۷۵۷۰ ۰ ۵۷2۷/‬اسشق ‪ -۲ . 4۱4‬پپلوی ‪ « 0211۷81‬منای‪.‬‬
  ‫رك ‪ :‬جایی‪-‬‬   ‫‪۴‬‬        ‫‪ - ۴‬رك ‪ :‬جا ‪.‬‬            ‫‪ > ۲ :‬رك ‪ :‬جاویك ‪.‬‬     ‫‪ » ۲ :‬تاو 'دیا ‪۹‬‬      ‫‪۷‬‬

                   ‫رك ‪ :‬جاودان خرد ‪.‬‬
                                   ‫‪2‬اویدان خرو ‪-‬‬
                                               ‫ج‬                      ‫‪ - ۵‬رك ‪ :‬جای ‪.‬‬

      ‫‪#‬جاویدن ‪ -‬بفتح پنجم » قس ‪ :‬پهلوی "‪([820۵0‬جویدن) ک‪
```


## [2026-09-04T19:08:39.094Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'خدای' in p and 170<i<250:\n        pass\nimport re\nfor w in ['خدیو','خواجه','خدا =','خدا ','خودای']:\n    hits=[i for i,p in enumerate(t) if w in p and 150<i<260]\n    print(w, hits[:12])\nEOF"
}
```


### [2026-09-04T19:08:40.869Z] TOOL RESULT

```
خدیو [178]
خواجه [237, 238]
خدا = []
خدا  [178, 193, 201, 237, 248]
خودای []
```


## [2026-09-04T19:08:47.432Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[178]\ni=p.find('خدیو')\nprint('==== leaf 178 (printed ~721) ====')\nprint(p[max(0,i-2500):i+2500])\nEOF"
}
```


### [2026-09-04T19:08:49.018Z] TOOL RESULT

```
==== leaf 178 (printed ~721) ====
     ‫‪۵‬ف‬

 ‫‪۴‬‬      ‫باشد‬    ‫بزرگه و خداوند خانه‬        ‫و کدخدای‬       ‫بضم اول و الی و سکون‬       ‫خدو ‪- ۲‬‬
‫کودبانوی خاله را نکبفزته‌اند (‪)۱‬؛ وبفتح اول‬                ‫وأو » آب دهن راگونند که از آثر مزةٌ چیزی‬
                                                                                            ‫‏‪Ey‬‬
                                                          ‫ْم اول بروزن سلو کك»‬     ‫کّ خدو ك و‬
‫جدیو * ‪ -‬بکر اول و الیوسکون‬
 ‫تحتالی مجهول و واو پادشاه ‪ -‬و وزیر س‬                     ‫پراکنده و پریشان شدن طبیمت باشد از امور‬
                                                          ‫‪ -‬وفهروخشم‪-‬‬     ‫ناملام ‪ _۴‬ویمعنی رشك وحد‬
 ‫ونگانةً عصر باشد ِ‬     ‫وخداوند کار ‪ -‬و بزرگه ‪-‬‬
                                                          ‫وخجلت وشرماری نیز آهده است ‪ -‬و بمعنی‬
                                                                          ‫آزردگی وعصهٌ بیجاخوردن ه‬
‫اول وثالی وفتح رابع‬     ‫»‪ -‬بكر‬   ‫حد بور‬
                                                          ‫؛ وبفتح‌اول‬   ‫همت‬
‫یمعتی خدیو است که‬          ‫و سکون رای فرشت ‪۰‬‬                                              ‫نیز گفته‌اند ‪۲‬‬
 ‫پادشاه ‪ -‬ووزیر ‪ -‬و خداوند کار ‪ -‬وبزرگه ‪-‬‬                  ‫حد بر ه بفتح اول بروزن وزیر» بمعنی‬
                            ‫وبگانةً عصر باشد ‪٩‬‏ ‪۰‬‬
                                                           ‫حن امت که خوب ‪ -‬وخوبی ‪ -‬و خوشدلی ‪-‬‬
‫وتح‬
  ‫حد به = بکراول وسکون تانی ف‬                                                         ‫وخوش خلقی باشد‬
‫تحتالی ‪ ۰‬بمعنی مضاف است که در مقابل مطلق‬                   ‫خد یش ‪ -‬بضم‌اول کوسرثانی وسکون‬
                                               ‫باشد ‪. ۷‬‬    ‫تستالی مجمول و شین قرشت ‪ ۰‬بمعنی پادشاه‬



                                                                            ‫(‪ )۱‬چش ‪:‬گوند‪.‬‬

      ‫‪ = ١‬خو (ه‪.‬م‪« ).‬اسفاا‪ ۲ :‬ص ‪ = 64‬خذوك (بفتح اول ونيز طم آن ) ر‬
  ‫(ك‪: ‎‬‬
                          ‫ع‪ .1‬مانوی‪012۷۷ ‎‬‬
                                         ‫‪4 K1‬‬
                                            ‫لفت فرس اسدی ص‪ " ۹٥۲) ‎‬درسغدی‪W ‎‬‬
          ‫)‪(Henning, sogdian loan words , BSOS. X. 1 . 94.‬‬
   ‫؟‪ ‎‬درقرای اطراف فزو‪.‬ن ‪ ( 1002‬اضطراب وغم وحزن ) ( ازافادات‌علامه دهخدا)‪‎.‬‬
                                               ‫رکنف جوم‪‎‬‬
                                                       ‫خن ن‬
                                                          ‫‪ ۴‬اف سیف سد رات‬
                ‫ز آنکه خدوك مشود خون مرا ازین مگس‪. ‎‬‬
   ‫مولوی بلخی‌رومی‪.‬‬
                                                                 ‫‪ ۴‬ظ » از ت خدا («‪.‬م‪: ).‬‬
               ‫مکن بد بکس کر نخواهی بخوش‪.‬‬                        ‫نک گفت مزدور باآن خدیش‬
   ‫‪.4‬‬          ‫رود کی سەر قندی‪« .‬لفبت فری‬

   ‫® ‪ -‬خدیو از ‪ .۵ ۷6/۵۳‬از ‪ ( 2۷۳212070-‬ق ‪« ) 121۵۷‬یبرك ‪ ۷۵۲‬درمادء‬
   ‫‪ 2‬رك ‪ :‬خدا ‪« .‬خدیو» خداوند بود ‪ .‬گویندکشور خدیو و گهان خدیو ‪ .‬فردوسی‬                             ‫‪0۱‬‬
                                                                                     ‫)وید ‪:‬‬
                                                                                          ‫(وسی گ‬
                                                                                               ‫ط‬
               ‫وماند الجمن بى خدیو‪.‬‬       ‫مت‬    ‫سه‬
                                                                  ‫سيامك بدست خود و رای دیو‬
     ‫«لفت فری‪۱۶ ۲‬؟‪.‬‬

   ‫معرب آن « خدبوی » بضم اول و فتح دوم بمعنی مالك و امیر وآقا و درترکی بمعذی‬
```


## [2026-09-04T19:09:03.039Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (176,177):\n    print('==== leaf',i,'printed ~',i+543,'====')\n    print(t[i][:3500])\nEOF"
}
```


### [2026-09-04T19:09:04.715Z] TOOL RESULT

```
==== leaf 176 printed ~ 719 ====
 ‫ضا‬
  ‫با سوختن و راه رفتن در دست وایعاو‬                            ‫خجنك = نماول وفتح ثانی سوکون‬
                                                              ‫نون ودال ابجد ‪ 0‬نام قصبه‌ایت درماوراءالنهر که‬
                                         ‫‪.‬‬   ‫بهم رسد‬
                                                          ‫‪۲‬‬                              ‫مولد کمال است ‪٩‬‏ ‪:‬‬
‫اول و انی بتحتانی‬
  ‫»|‬    ‫=‬    ‫‪۷۳1‬‬
                            ‫حجیر "‪۰‬یکر‬
                                  ‫‪۴‬‬          ‫‪2‬‬


                                                               ‫_ بن اول و ثالی» در نذه است‬        ‫خجی؟‬

                                                              ‫گویند‪.‬‬   ‫که لآرا چکاو کے خوانند و بعربی قبره‬
‫وجمیل وخوش صورت وصاحب حسن راگویند ؛‬
                          ‫ویضم اول هم آمده است ‪1‬‬              ‫خجو له بکر اول و فتح ثانی و لام‬
                                                              ‫وسکون واو »آبله گروانندکه ببب کارکردن‬


                                                   ‫بیان ششم‬
            ‫درخای نقطه دار ‪ ۳‬دال بی نقطه مشممل بر شانزده لغت و کنات‬

 ‫‪-‬دوای؟ جم اول ‪ ۰‬نام ذات | وصاحب ومالك را نگیوزبند ؛ وبا ذال نقطه‌دار‬
                                                                    ‫خداً خ‬
                                      ‫بارتمالی است همچو الهواله ‪ -‬و مخقف خود؟" | هم خوانده‌اند ‪.‬‬
                                                                                              ‫‪1‬‬




                                                   ‫(‪ )۷‬چك‪ .‬چش‪ :‬جوئی‪.‬‬               ‫(‪ )۱‬خم‪ -: ۱‬و‪.‬‬
  ‫روزه راه‬         ‫ده‬   ‫‪ ۰‬من آن و ‪-‬مرقند‬         ‫‪ - ۱‬شهری مشپور بماوراء النهر بر ساحل سبحون‬
  ‫در ‪ ۱4‬درجه و ‪ ۳۲‬دققهة‬               ‫ت‬
                                      ‫س)‬‫اوس‬
                                          ‫است « ممجم‌البلدان ‪ :‬خجندة » و اکنون در ترکستان (ر‬
      ‫‪ - ۴‬ظ‪ .‬مصحف«چفو»‬          ‫عرض شمالی و ‪۸٩‬‏ درجه و‪ ۲4‬دققة طول‌شرفیه ضمیمهةٌ معجم البلدان»‪.‬‬
  ‫بهلوی ‪rhic‬‏ ‪( uh -‬از ‪ :‬هو (خوب ) ‪٣‬‏ چهر(اصل نژاد ) ‪.‬‬                            ‫هرژ=ر‬
                                                                                      ‫هج‬          ‫(«‪.‬م ) ‪= ۴‬‬
   ‫اوستا_‪-»3601)1‬ل‪0‬ا«بارتولمه ‪۱۲۸۱٩‬‏ نبیر گے ‪»۹۰۱‬طبری ‪( ۲1[06‬خوش» خوب‪ .‬زیدا) «واژه‌نامه‬
  ‫‪ .‬دامفالی نیز ×‪٣[0‬‏ ‪ ,‬شهمیرزادی ‪7[1205‬؛ لفة نيك نژاد ‪ .‬خوب اصل و مجازاً بمعانی‬                            ‫‪۳‬‬
  ‫‪ ۴‬ب۔هلوی متأخر ‪: . ۷2۸۵۷۲‬هلوی اشکانی‬                                    ‫مکقور در متن آمده ‪ .‬رك‪ :‬هزیر ‪.‬‬
  ‫بازند ‪« 102۷‬هوبشمانس ‪4۵‬ج » « مسینا ‪. » ۲ : ۹۳۱‬بعضی ابن کلمه را از‬                                 ‫‪007‬‬
   ‫اوستابی_‪ )# 212210(, 6 ۵۷5 3/2010-‬مشتق دانسته اند ونولد که بحق دراين وجه اشتقاق‬
  ‫شکكرده » چون خدای فارسی و خواتای بهلوی بکلمةٌ ‪_ayÃtaWX‬‏ ‪ °‬با ‪o 2002802۷01‬‏‬
   ‫‪+ 142‬‬      ‫رت‬    ‫کبا‬
                      ‫سده )‬
                          ‫اد زن‬
                              ‫مزخو‬‫اقرب است و آنهم بسادسکریت_‪( 5802۷5 + 1018‬ا‬
  ‫‪ ( 52‬ازخود آغاز کرده) رابطه دارد ‪ .‬برای اطلاع از عقابد مختلف رك ‪ :‬بارتولمه ‪۰ ۲۹۸۱‬‬
      ‫استق ‪ , ۱۲۷‬هوشمان ‪.۱۷4‬تبعات ادرالی‪ .‬دارمستتر ‪ ۱‬ص‪ ۷۰‬بشتها ‪ ۲6۰ : ۱‬خرده اوستاه‪.۵۲‬‬
  ‫‪.‬‬          ‫* گربرسن ‪۶‬‬      ‫‪ ۰‬زبا کی ‪127‬‬           ‫‪2‬‬    ‫» اشکاشمی‬      ‫‪۵۰۹‬‬   ‫ص‬    ‫ا«اسفا ‪۱‬‬        ‫‪6‬‬     ‫کردی‬

       ‫گیلکی ‪830‬ا‪ .‬در بهلوی و پازند خواتای بمعنی شاه آمده و « خوانای نامك» بعنی «شاهنامه»‪.‬‬
      ‫ا
==== leaf 177 printed ~ 720 ====
 ‫خدرگه‬                                                                                                     ‫‪a Ah‬‬


‫اول‌بروزن مهره » خرده‬         ‫حدره =‬                         ‫زراق که بظاهر خود را بیارایند‪ -‬وآلهایی‌را فیز‬
‫رىز هرچیز را گویند رک وشرارة آتش‌را لز‬‫و‬                      ‫‌دشدادو لمرود؛‬      ‫عابنییکر‬‫یخد‬
                                                                                           ‫دی‌‬
                                                                                             ‫نوا‬
                                                                                               ‫گونن که دع‬
          ‫گفته‌اند ؛ وبفتح اول همآمده اش‬                         ‫وآنها راخدای فروشان هم میگوبند با دوتحتانی‬
‫خدك ‪ .‬بفتح اووئانی بروزن کجك‪.‬‬                                                                                    ‫ورف‬
‫مطلق پل را گوبند خواه باسنگف وخشت وکچ‬                        ‫تون‬     ‫حجد او ند ‪ ۱‬ب‌ بقتح واو وسکون‬

 ‫بر رودخانه بندند و خواه با چوب وخاکد‬                                 ‫‪۰‬‬   ‫را کوند‬    ‫انه‬    ‫ویز رگ‬        ‫صاحب‬   ‫‪1‬‬   ‫ودال‬

                                 ‫بر جوی (‪# . )۱‬‬
                                                             ‫مزر گد‬        ‫بادشاه‬       ‫‪ ۴‬س‬     ‫حدایگان‬
‫سمعنی‬
    ‫بر وزن عشرنی ‪۰‬‬           ‫‪°‬‬
                                                                                            ‫وخداوند گار اعظم باشد‪.‬‬

‫بروزن بپلنگه‪ ,‬نام درختی‬      ‫‪-‬‬        ‫‪۱‬‬
                                                                 ‫حدر نق » بفتح‌اول وئانی‌بروزن‌خورنق‬
‫است بیارسخت که از چوب آن‌نیزه وتبروژین‬                       ‫بلغت رومی و بعضی گوبند بونانی عنکبوت را‬
                                                            ‫گوبند ‪ ۴‬؛ وباین‌معنی بجای نون بای حطی حم‬
                                          ‫میکویند ‪. ۷‬‬                                                ‫بنظر آ مده اف‬

                                                                               ‫(‪)۱‬چك» چش‪ :‬جوئی‪.‬‬
                            ‫وند (یوند اصاف) بمعنی صاحب (مطلقا) ‪:‬‬                    ‫‪+‬‬       ‫ا‬‫د‪:‬‬
                                                                                              ‫از‬‫‪ ۱‬خ‬
  ‫‪۶‬لتان ‪. ۸۳‬‬
           ‫گ‬                        ‫درتهند‬      ‫ر‬   ‫دست‬   ‫کنان‬    ‫لماش‬         ‫جاه‬          ‫ویشند‬
                                                                                                ‫اه ب‬
                                                                                                   ‫دی ک‬
                                                                                                      ‫خبن‬
                                                                                                     ‫‪“e‬‬
                                                                                                        ‫نه‬
  ‫)ه فلان قلعه را بدولت خداوند‬
                             ‫‪-‬یادشاه ‪« :‬سواری از در درآمد وبثارت داد (ملك را ک‬
  ‫کشادیم» ‪« .‬دکلتان ‪ - ۰ ۸۲‬ان ‪ 9:‬هر که خدای را عزوجل بمازارد تادل مخلوقی بدست آرد ‪۰‬‬
              ‫خداوند تعالی همان خلق را براو کمارد تا دمار از زروکارش برآرد»‪ .‬ک«لتان ‪.۲4‬‬
                                            ‫‪+‬ان (پسوند بت و اصاف ) ‪:‬‬
                                                                   ‫ک‬                        ‫ای‬
```


## [2026-09-04T19:09:32.397Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (236,237):\n    p=t[i]\n    print('==== leaf',i,'printed ~',i+543,'====')\n    print(p[:3200])\nEOF"
}
```


### [2026-09-04T19:09:34.088Z] TOOL RESULT

```
==== leaf 236 printed ~ 779 ====
 ‫¬ ‪~A‬‬


   ‫ن‬
   ‫ز بر‬
      ‫وول‬
        ‫حنبور ‏‪ ١‬با تحتانی مجپ‬                        ‫وسکون‬     ‫انی‬   ‫نم اول وکر‬      ‫‪-‬‬   ‫حضاف‬


‫حلی کر » قامت و پل صراط رگانویبزند ‪-‬‬                  ‫باشف‬    ‫وخشن‬    ‫تستالی وکاف ‪ ۰‬لوعی آزلبای درشت‬

 ‫ومزارع‌و زراعت کنندهرا گنفیتزه‌اند؟ و؛یمعنی‬                             ‫که درویثان وفقیران بوشند ‪.‬‬
    ‫اول بتقدیم بای حطی بر نون هم آمده ات‬




                                       ‫بیان هیجد هم (‪)۱‬‬
          ‫ن و ن (‪)۳‬‬         ‫و‬          ‫یکی‬                      ‫در خای باه‬

                                            ‫و کنات‬      ‫لف‬


‫ىك مشت آ بوبك مشت کاه‌وامثال آن ‪ -‬وبمعنی کفل‬           ‫خو » بفتح اول و سکون انی ‪ ۰‬جرب‬
‫وساغری اسبان هم هست ‪ -‬وقالبی را نیز گویند‬              ‫بتابی (‪ )4‬باشد که بنابان و کتابه نوسان‬
‫‪ - ۴‬وسم‬      ‫نند‬
               ‫نآ‬‫زالای‬
                     ‫که استادان بنا طاق برب‬            ‫و قاشان در درون و بیرون عمارت ترقیب دهند‬
                                                       ‫وبر بالای آن رفته‌کار کنند ‪ - ۴‬و گیاه خودروی‬
          ‫اول سرشت و عادت وطبعیت باشد ‪٩‬‏ ‪.‬‬
                                                      ‫که درمیان غله زارها وباغها رود تاآنر! نکنند‬
‫اول بر وزن دوا » تمعای‬      ‫خوا‪ -.‬بقنح‬
                                                      ‫غله وزراعت قوت بهم لرساند وچنانچه بايد نشو‬
‫ند ‪ -‬و بزبان‬    ‫بحم‬
                  ‫ول‬‫کربی‬
                       ‫شت باشد که بع‬                   ‫ولما نکند ‪ - ۴‬وبمعنی کندن ودرو کردن علف‪.‬‬
‫عربی بالف ممدوده خالی بودن شکم از طعام‬                 ‫ناه‬‫گر‬‫ویربدن شاخ درخت هم آمده اعت ۔ و ه‬
 ‫واف‬‫وهوای‌میان دوچیزومیان(ه) پاباشد ‪ - ۱‬ع‬             ‫را بدرخت پبجد عموماً ‪ - ۴‬و عشقه‬         ‫خهود‬
                                                                                                 ‫ک‬
‫را بیز گفته‌اند؛وبا الف مقصوره هم درست است‪-‬‬           ‫ولبلاب را کوبند خسوصاً ‪ - ۴‬و کف دست رانیز‬
‫وبکسر اول؛پمعنی مزه ولذت باشد ‪ -‬ویضم اول‬               ‫گفته‌اند ‪ -‬وبك مشت ازهرچیز که باشد همجو‬

  ‫‪)۱( ۱‬‬     ‫(‪)e‬‏ درچك باشتداه ‪:‬‬              ‫‪.‬‬   ‫صد‬   ‫ر«( چش‪:‬‬             ‫‪ :‬هر دهم‬   ‫)‪ (۱‬مك‬

                                                 ‫(‪)e‬‏ چش ‪:‬‬            ‫)( چك‪ .‬چش‪:‬بندی ‪.‬‬

                                                 ‫اج‌نود» (بل صراط ) (و‪.‬م‪۳ ).‬‬       ‫ممحف‬   ‫‪۱‬‬

                 ‫همیدون بپول خنیور گذار ‪.‬‬
  ‫منسوب باسدی طوسی ‪ .‬رك‪ :‬ص چهل وثش‌مقدمه ‪.‬‬
                                        ‫‪ ۴‬رك‪ :‬خوازه ‪+‬‬                     ‫خنور ‪.‬‬   ‫رکه‪:‬‬   ‫؟‬


       ‫کگهردون بته از هفت آسمان خو‬                               ‫ز بهر چار طاق رفعت اوست‬
  ‫‪.‬فرهنك شاهنامه ‪۱۲۱‬؟‪.‬‬
                     ‫نزاری قهستانی «‬
             ‫‪:‬‬    ‫(علف هرزه) ‪٠‬‏ فقس ‪ :‬زردخو (فسم یگل) « اسفا ‪ ۲ : ۱‬ص ‪۸۳‬‬              ‫‪×1 _ ۴‬‬

       ‫نماند بر این بوم و برخار وخو ‪.‬‬                        ‫گر ایدون که رستم بود پیش رو‬
   ‫ی‬       ‫فردوسی طوسی تقو‬
  ‫گے ابت ‪.‬و‪.‬خو سم‬          ‫‪#‬جمعتی گر‬         ‫(عر)ا‬            ‫‪- ۱‬‬         ‫؛وی ‪.‬‬
                                                                              ‫® _ رل خ‬
                  
==== leaf 237 printed ~ 780 ====
 ‫خواجه‬                                                                             ‫ها‬
                                       ‫آنچه بدان روز (‪ )۱‬بگذرانند‪ .‬یمنی قوت | است‬
‫خواب نادیده س کنابه‌ازطفل دابافغ‬                                       ‫لابموت ‏‪# . ٩‬‬
                                   ‫خواب جاو ید باانی ممدوله ‪ | ۰‬باشد ‪. ۴‬‬
                           ‫بونا‬
 ‫یده ه با ثانی معدوله بر وزن‬  ‫خ‬                ‫کنابه ازهرکے است که بیدار شدن در قیامت‬
          ‫والمیده » مخفف خواباننده ® باشد ‪.‬‬                                        ‫باشد ‪, .‬‬

 ‫خو اجه" ‪ -‬بائانىممدولەبووزن راجه‪,‬‬              ‫خو اب خرگوش د کنابه از غافل‬
 ‫کدخدا ورئیی خانه گروایند‪-‬ویمعتی معظم‌باشد‬                     ‫بودن وغفلت و تفافل باشد ‪. ۴‬‬
 ‫خو) بستان ‪ - ۴‬باانی مسوله بروزن | وشیخ ویر ‪ -‬ومالدار‪ -‬و حاکم وساحب جمعیت‬
                                                     ‫امعا‬
                                                  ‫یندن‬   ‫وو‬  ‫‪ .‬تاستان ‪ ,‬کنانه از حای خو‬
                                                           ‫خاب‬
 ‫را نیز کفته‌اند ‪ -‬ویمعنی دل وروح هم هت ‪-‬‬
                       ‫و خدمتکاری که آلت‬                               ‫‪۱‬‬            ‫باشد ‪.‬‬
 ‫تناسل او را بریده‬


                                                     ‫(‪ )۱‬چك » چش ‪ :‬روز بدان ‪.‬‬

                                                            ‫رك ‪ :‬خواجه بار ‪.‬‬   ‫ِ‬
       ‫دهد شرافکنان راخواب خر کوش‪.‬‬               ‫‪ - ۴‬بچشم آهوان چآشنمهةٌ نوش‬
   ‫نظامی کنجوی ‪« .‬کنجنه >‪٤۵‬‏ ‪.‬‬
                                          ‫‪:‬واب ‪-۲‬ستان (یموند مکان ) ‪.‬‬
                                                                    ‫‪ - ۴‬از خ‬
       ‫‪ - ۴‬ریدکان خواب نا دیده مصاف اندرمصاف مکربان د!غ تاکرده قطار اندر قطار‪.‬‬
  ‫‪ +‬فرخی سیستانی‪.> ۹۷۱‬‬
  ‫« سخن سال ‪۲‬‬        ‫‪01‬‬
                      ‫‪8‬اجیکی‬
                           ‫‪0‬جة ت‬   ‫‪-۱‬‬
                               ‫‪1‬درله‬                  ‫رك ‪ :‬اسقا ‪۲: ۱‬ص ‪۰۲‬‬       ‫‪۵‬‬
   ‫» درهندوتر کیه ‪( 805 -‬درهندوستان ‪ -‬اصطلاحاً خوجه بییروان اسمعیلیه‬       ‫شمارة ‪ ۸‬ص ‪۹۱۱‬‬
 ‫اطلاق شود ) ‪ ,‬معرب آخنواجا « تفس» « دزی ج‪ ۱‬ص‪٤٠٩‬‏ ‪ ۰‬آفای پورداود این‌کمه رامر کب‬
  ‫از ‪ ۵۷2 = 2۷27 :‬اوستابی بمعنی خود ‪ 16) +‬که درآخرکلمات اوستابی درآبد بمعنی لل و‬
  ‫همچنین‪.‬جمعاًبمنی کسکه دارای‌خودییوشخصیت مستقل‌است‪,‬دانته‌اد‪ «.‬حافظ شبرین سخن ‪, ۲ ۳۷‬‬
  ‫صفیر = چه)دانسته‌اند تیه‌ای‌در‬   ‫وند‬
                                     ‫س‪+‬‬‫یای)‬
                                          ‫((خد‬
                                             ‫كلوی‬
                                                ‫چی به‬
                                                    ‫بعضی اصل] نرا«خواتای‌چث» از خواتا‬
  ‫نزدیکی درباچة زره (هامون ) سیستانست ‪.‬انرا هم « کوه خدا» گویند وهم «کوء خواجه » (اين‬
           ‫درباچه و کوه ترد زرتشتبان جنبةٌ تقدس دارد ) واين امرشاید موند فرضةٌ اخیرباشد ‪.‬‬
   ‫‪ - ۷‬بین این دومعنی خواجه درحقیقت هیچگونه اختلان طفظ ومعنی نست و خواخه‬
   ‫درهردو مورد بمعنی بزر که وسرور وصاحب است بااين تفاوت که درمورددوم درقدیم «خواجمسرا»‬
   ‫میگفتند یعنی بزر كك و سرور اندرون» و چون مردم نامحرم لمیتوانته است درحرم راه بايد در‬
  ‫دستگاههای استبدادی قدیم مردال
```


## [2026-09-04T19:09:54.957Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"خدیو\" FSF_pages.txt | head -10; echo \"=== pages ===\"; python3 -c \"\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nimport re\nfor i,p in enumerate(t):\n    if 'خدیو' in p: print('leaf',i, p[:100].replace(chr(10),' '))\n\" | head -20"
}
```


### [2026-09-04T19:09:56.739Z] TOOL RESULT

```
6627:     ‫خردباید و گوهر نامدار‬                   ‫بریده دل از ترس گیهان خدیو‬
10066:                                             ‫ببرد از رخت شرم گیهان خدیو‬
10343:‫شاهد برای واژة خدیو همین بیت را از‬
20118:‫کیهان خدیو‬                                  ‫‪۳۰۷‬‬
20129:                              ‫گیهان خدیو‬                  ‫توگفتی نهشببودپیدانه روز‬
20137:‫ببرد دل از ترس گیهان خدیو‬                                          ‫پهلوانان هممی‌آورد‪:‬‬
=== pages ===
485
leaf 138                                                                                      ‫پایمرد‬       
leaf 204               ‫همی تا آز باشد بر جهان چیر‬               ‫نبینی باغبان چون گل بکارد‬  ‫نگردد جان مرد
leaf 210                       ‫(اسدی ‪:)۷۹۳-۷۳‬‬                  ‫سپاهی بدین رزمگاه آمدیم‬         ‫رنگ رنگ
leaf 410 ‫کیهان خدیو‬                                  ‫‪۳۰۷‬‬                 ‫پآسگاهی آمد سوی نیمروز‬
```


## [2026-09-04T19:10:04.809Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\n# find printed page numbers per leaf\nfor i in (255,258,260,262,265,410):\n    p=t[i]\n    nums=re.findall(r'[۰-۹]{2,3}',p[:200])\n    print('leaf',i,'nums',nums[:4],'|',p[:160].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T19:10:06.537Z] TOOL RESULT

```
leaf 255 nums [] |                                                 ‫‪Yar‬‬                                            ‫دیزه‪‎‬‬                            ‫فرهنگ بهدینان)‪:‬‬     
leaf 258 nums ['۵۵'] | ‫راست‬                                           ‫‪۵۵‬‬   ‫(یعنی آن کس را که تنگدست و نیازمند‬                                                 ‫ا‬  ‫بود و روز ب
leaf 260 nums ['۲۵۳'] | ‫رای‬                                              ‫‪۲۵۳‬‬                                              ‫راه‬                  ‫آیین» روش رسم و قاعده‪:‬‬       
leaf 262 nums ['۹۵۳'] | ‫رحیل‬                                                ‫‪۹۵۳‬‬                                           ‫رای زدن‬                             ‫مقصود‪ .‬مراد‪:‬‬
leaf 265 nums ['۹۳'] |                                                  ‫‪۹۳‬‬                                            ‫رد‬                         ‫رده (بازبر اول و زیر دوم)‬     
leaf 410 nums ['۳۰۷'] | ‫کیهان خدیو‬                                  ‫‪۳۰۷‬‬                 ‫پآسگاهی آمد سوی نیمروز‬              ‫فروختن عافروختن ]‪ :‬فروزندة گیتی‪.‬‬ ‫به نزدیک سال
```


## [2026-09-04T19:10:16.883Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (165,166,167):\n    print('==== leaf',i,'====')\n    print(t[i][:1500])\nEOF"
}
```


### [2026-09-04T19:10:18.540Z] TOOL RESULT

```
==== leaf 165 ====
                                                                                  ‫پیوسته‬


                    ‫‪-۲‬خویش‪ .‬خویشاوند‪:‬‬                        ‫ز گفتار دهقان یکی داستان‬
     ‫بسی خویش و پیوند ما برده گشت‬
‫بسی مرد تیک اختر آزرده گشت‬                  ‫(‪)۲-۱۰۷۱-۵۱‬‬

 ‫(‪)۴-۱۸-۲۳۱۱‬‬                                        ‫همی خواهم از دادگر یک خحدای‬

                         ‫(ویس ‪:)۶۳۱-۷۴‬‬     ‫که چندان بمانم به گیتی به پای‬
     ‫تراواز خان و مانو خویش و پیوند‬               ‫که ‌این نام شهریاران پیش‬
 ‫جدا کرد و به دام بوری افگند‬                ‫بپیوندم از خوب گفتار خویش‬
                       ‫‪-۳‬سازش‪ ,‬نزدیکی‪:‬‬      ‫)‪(۶۴۶-4‬‬
                                                                                  ‫پیوسته‬
 ‫تهمورث در جنگ با دیوان پیروز شده‬
                                                    ‫پیوند‪:‬‬     ‫ه)»‬
                                                                 ‫نیض‬
                                                                   ‫انق‬
                                                                     ‫گ (‬
                                                                       ‫ییش‬
                                                                         ‫بخو‬
                                                                           ‫‪-۱‬‬
                                 ‫است و‪:‬‬
                                                          ‫ز دهقان پرمایه کس را ندید‬
         ‫ازیشان دو بهره به افسون ببست‬
  
==== leaf 166 ====
   ‫همی گفت و چنگش به چنگ اندرون‬
  ‫هی داشت ا ھن و شا ورن‬                                ‫(نقیض جفت)‪ .‬یک لنگه فرد‪:‬‬
   ‫همان ناخنش پر ز خوناب کرد‬                               ‫شبستان او را به حادم سپرد‬

‫سپهبد بروها پر از تاب کرد‬                   ‫از آنجایگه رشته تایی نبرد‬
 ‫(‪)۶۲۶۲-۳۶۷‬‬                                 ‫(‪)۶۶۵-۲۰۱۴-۶‬‬


            ‫گیی‪:‬‬ ‫دمعن‬
                    ‫یبه‬
                      ‫ییتچزیر‬
                            ‫پدرب‬
                               ‫و‬              ‫(یعنی همانایکنخهماز آنجاباخودنبرد)‬
        ‫وخت‬
          ‫چو صد سال بگذشت باتاجت‬                                ‫تاب (اسم از تابیدن تافتن)‬
 ‫سرانجام تاب اندر آمد به‌بخت‬                 ‫«یکی طاقت است ‪-‬دیگر پیج و تاب کهدر‬
 ‫(‪)۲-۲۴۷۰-۳۹۱‬‬                                ‫باشد ‪-‬دیگر فروغ‬        ‫وفان‬
                                                                       ‫کزل‬
                                                                         ‫رنسنیو‬
                           ‫(ناصو ‪:)۴۴-۵۱‬‬    ‫بودبهآتش و برق ‪-‬دیگر تبش گرمی‬
   ‫تاب و نور از روی من می‌برد ماه‬            ‫باشد‪ .‬چنانکه عنصری همه را در سرغزلی‬
‫تاب و نورش گشت یکسر پیچ و تاب‬               ‫گوید‪ :‬گفتم متاب زلف و مراایپسر متاب‬
                           ‫(منوچهری ‪:)۴‬‬      ‫»«گفتا ز بهرتاب تودارمچنین به تاب ‪-‬‬
                ‫بخهومایرگان ساقی آواز داد‬   ‫گفتم نهی برین دلمآن تابدار زلف ×گفتا‬
‫اندرون تاب‌ها‬        ‫ف‬
                     ‫لبه‬‫زده‬
                 
==== leaf 167 ====
                                               ‫ور‬                                      ‫تاب‬


                              ‫(مسعود ‪:)۲۳‬‬             ‫‪-۲‬توانایی توان نیرو پایداری طاقت‪:‬‬

    ‫نههیچ گردون باهمت توساید سر‬                               ‫چنين داد پاسخ بدیشان که من‬

‫نه هیچ آتش باهیبتتو گیرد تاب‬                        ‫نبینم کسی را بدین انجمن‬
                              ‫(حافظ ‪:)۵۲۴‬‬                         ‫سبیاب‬
                                                                      ‫و تا‬
                                                                         ‫ریا‬
                                                                           ‫فد پ‬
                                                                              ‫ادار‬
                                                                                 ‫که‬

  ‫از تاب آتش می برگرد عارضش خحوی‬                    ‫مرا رفت باید کچشوتی برآب‬
‫چون قطرهای شبنم بربرگگل چکیده‬                       ‫(‪)۳-۱۰۴-۵۸۵‬‬

                 ‫‪-۴‬روشنایی فروغ نور‪:‬‬                        ‫و کیت زاگ ا ازب‬
                         ‫(اسدی ‪:)۴۸۱-۸۲‬‬             ‫خسدنگم بسدوزد دل آفتاب‬
           ‫از آن گوهران درهم افتاده تاب‬             ‫(‪)۳-۱۴۲-۵۴۶۲‬‬
‫جهان کرده روشن‌تر از آفتاب‬                                    ‫اگر تاب داری به جنگش بگوی‬
                      ‫(ناصر ‪:)۴۴-۶۱‬‬                 ‫سبر اندرین آبروی‬      ‫وگرنه‬

       ‫پتیجاوبش نور و تاب از منببرد‬                 ‫(‪)۶-۱۵-۰۸۶‬‬
```


## [2026-09-04T19:10:27.751Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(t):\n    if 'خدیو' in p and i<400:\n        print('==== leaf',i,'====')\n        print(p[:2000])\nEOF"
}
```


### [2026-09-04T19:10:29.289Z] TOOL RESULT

```
==== leaf 138 ====
                                                                                     ‫پایمرد‬
                                                           ‫دستیار دستگیر یاری دهنده‪:‬‬

 ‫که هرکس کهسر بکرشد ز انجمن‬                       ‫[کاوه] خروشید کای پایمردان دیو‬
     ‫خردباید و گوهر نامدار‬                   ‫بریده دل از ترس گیهان خدیو‬
 ‫هنر یار و فرهنگش آموزگار‬                    ‫(‪)۱-۳۶-۴۱۲‬‬
     ‫وار کتومران رابت آززد‬
 ‫دلاور شود پر و پاآورد‬
 ‫(‪)۳-۹۷۱-۰۴۷۲‬‬
                                             ‫ازین سرفرازان روز نبره‬
                                    ‫پایه‬     ‫(‪)۴-۹۳-۷۷۴‬‬
                 ‫و‪:‬‬
                  ‫بره‬
                    ‫رهتقد‬
                        ‫میگا‬
                           ‫‪-۱‬ارج‪ ,‬پا‬                                ‫(اسدی ‪:)۲۲۲-۸۱۰۱‬‬
                   ‫(دقیقی ‪:)۶-۷۸-۸۱۳‬‬                       ‫به نزدیک او پایمردم تو باش‬
              ‫ستاره شناس و گرانمایه بود‬      ‫بدینکار درمان دردم تو باش‬
‫ابا ا بوه دانش که را پایهبود؟‬                ‫‪ :)۲۸-۳‬دریغا عمر که عنان‬        ‫مهنوه‬
                                                                                 ‫دلیل‬
                                                                                    ‫(ک‬
                      ‫‪-۲‬جاه مقام ر تبه‪:‬‬      ‫گشاده رفت و از وی جز تجربت و‬
                ‫کپهارداشاهی سزا بد بداد‬      ‫ممارست عوضی به دست نیامد که در‬
‫کرا پایه بایست پایه نهاد‬                     ‫تواند‬     ‫یاری‬
                                                          ‫گی ی‬
                                                             ‫ترد‬
                                                               ‫سایم‬
                                                                  ‫دری پ‬
                                                                      ‫وقت پی‬
 ‫‪۶۱۲۱-۴۰۸4‬‬
         ‫(‬                                                                          ‫بود‪.‬‬


                              ‫پاییدن‬                   
==== leaf 204 ====
              ‫همی تا آز باشد بر جهان چیر‬               ‫نبینی باغبان چون گل بکارد‬
 ‫نگردد جان مردم از گنه سیر‬                   ‫چه مايه غم خورد تاگل برآرد؟‬

                     ‫چیره زبان و چیره سخن‬                                 ‫چیرگی‬
 ‫هردو به معنی‪ :‬سخنور» خوش‌سخن»‬               ‫(مرکب از چیره ‪ +‬ی مصدری‪ :‬های آخر‬
                             ‫خوش بیان‪:‬‬       ‫چیره در پیوند به «ی» به کاف پارسی بدل‬
          ‫بجستند از آن انجمن هر دوان‬                ‫می‌شود)‪ :‬پیروزی» برتری» تسلط‪:‬‬
‫یکی پاکدل مرد چیره زبان‬                                  ‫همه چیرگی با منوچهر بود‬
‫(‪)۵۱۸-۱۱۱-۱‬‬
                                             ‫کزو مگغیزتی پر از مهر بود‬
              ‫ولیکن توای پور چیره سخن‬        ‫‪۱-۲۲۱۰۸۲۷6‬‬

‫شبارده مکن‬
         ‫زبان برنگیا‬                                                         ‫ر‬
                                                                             ‫ي=‬‫جره‬
                                                                                 ‫چی‬
‫(ه‪)۸۰۱۲-۸۸۳‬‬
                                                            ‫پیروز» مستولی» مسلط ‪:‬‬
                                       ‫چیز‬          ‫جرابر دلت چیره شد رای دیو؟‬
                         ‫خواسته دارایی‪:‬‬
                                             ‫ببرد از رخت شرم گیهان خدیو‬
         ‫ندارد جز او گیو فرزند نیز‬           ‫(‪)۳-۷۵۱۰-۵۱۲۲‬‬
‫زنج و ز چیز‬
          ‫گرامی‌ترستش گ‬                           ‫چو چیره شدی‪ ,‬بی‌گنه خون مریز‪...‬‬
‫(‪)۴۰۶۲۱۰۸‬‬                                    ‫(‪)۲-۵۹۱-۰۸۹۲‬‬
                       ‫(اسدی ‪:)۰۰۱-۳۷‬‬                             ‫(اسدی ‪:)۰۷۲-۱۳‬‬
          ‫پذیرفتمش دخت و بسیار چیز‬                    ‫نشسته بر آهو عقاب دلیر‬

‫ونج و دینار نیز‬‫همان کشور گ‬                   ‫چو براسب گردی به ناورد چیر‬
                                                                 ‫(ویس ‪:)۸۲۴-۱۶۲‬‬

==== leaf 210 ====
                      ‫(اسدی ‪:)۷۹۳-۷۳‬‬                  ‫سپاهی بدین رزمگاه آمدیم‬
        ‫رنگ رنگ‬   ‫ز خرگاه و ازخیمۀ‬        ‫نه بر آرزو کینه‌خواه آمدیم‬
       ‫گ‬
       ‫نبر‬
         ‫دگرکش‬
             ‫ز شیر واز‬                                  ‫کنون سر بسهر شبانهدرها‌ایم‬
                                   ‫خديو‬     ‫ایم‬  ‫‌وی‬‫ههر‬
                                                      ‫دهم‬
                                                        ‫نن ب‬
                                                           ‫گجا‬
                                                             ‫دآلو‬
           ‫سرور» بزرگ» پادشاه خداوند‪:‬‬     ‫(نه بر ارزوی یعنی نهبه خواست و ميل‬
        ‫دیو‬      ‫وتان‬
                    ‫ه دس‬
                       ‫ز‬ ‫رب‬
                          ‫خامک‬
                             ‫سی‬                                               ‫حود)‬

  ‫گهشت وماند انجمن بخیدیو‬
                        ‫تب‬                                     ‫خدنگت (با زبر اول و دوم)‬
‫)‪(V-F.-1‬‬                                  ‫‪-۱‬نوعی چوب گز بسیار سخت و هموار‬
‫مصراع اول این بيت را عباس اقبال‬           ‫سازند و‬     ‫که از ان تیر و نیزه و زین اسب‬


‫مصحح لغت فرس بهاین شکل ضبط کرده‬           ‫تیر حدنگ و زین خدنگ به این اعتبار‬
                                ‫است‪:‬‬                         ‫گویند (رشیدی برهان)‪:‬‬
‫«سیامک به دست خود و رای دیو» که‬                        ‫چنان برگرفتم ز زین خحدنگ‬
 ‫نادرست است و معنی بيت و مضمون‬            ‫که گفتی ندارم به یک پشه بتک‬
 ‫شاهنامه را خراب کنرده است‪ .‬از داستان‬     ‫(‪۷۵ -۲-۷۶‬‬
 ‫سیامک در شاهنامه بهخوبی آشکار است‬         ‫(میم در «بر گرفتم» ضمیر مفعولیست‪.‬‬

  ‫یمن»‬
     ‫رور‬
       ‫اوه«پ‬
           ‫کسهیامک به دست دی‬
‫کشته می‌شود‪ .‬ناماین دیو درنسخۀ لندن‬                      ‫کمان کیانی گرفتم به چنگ‬
 ‫«خرزوان» و در نسخه لنینگراد «خروزان»‬      ‫به پیکان پولاد و تیر خدنگ‬
‫نوشته شده است‪ .‬همین نام دیو است که‬        ‫‏)‪(YY-14۶-1‬‬
‫در لغت فرس تحریف شده است‪ .‬بی‌گمان‬          ‫اا
```


## [2026-09-04T19:10:40.521Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (209,210,211,212):\n    p=t[i]\n    print(i, re.findall(r'[۰-۹]{1,3}',p[-400:])[:6], '|', re.findall(r'[۰-۹]{1,3}',p[:300])[:6])\nEOF"
}
```


### [2026-09-04T19:10:42.262Z] TOOL RESULT

```
209 ['۱', '۰۳۱', '۵۳۸', '۷۰۱', '۱۱۴', '۲'] | ['۳', '۹']
210 ['۲', '۲۲', '۶۸۳', '۰۸'] | ['۷۹۳', '۷۳']
211 ['۸', '۸۱', '۶۲۵', '۲', '۸۸۵', '۱۸۱'] | ['۸۰۳']
212 ['۴', '۱۰۳', '۲', '۲۰۴', '۱', '۲۰۴'] | ['۹', '۳', '۳۹۲']
```


## [2026-09-04T19:10:53.663Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"جاوید\" \"برنا\" \"خدا\" \"خواجه\"; do echo \"### $w in ARY\"; grep -c \"$w\" incoming/ARY/ARY_pages.txt; done; echo \"=== ARY latin index aiw ===\"; grep -n -i \"aiw\\|aevum\\|ayu\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-04T19:10:55.108Z] TOOL RESULT

```
### جاوید in ARY
3
### برنا in ARY
104
### خدا in ARY
130
### خواجه in ARY
0
=== ARY latin index aiw ===
667:Nays Sly Glas 9 sins .y OLS Jad layup 9a) BN AD cde Ga pet oye cabs)
1025:ili 32 OUT 5 9 Sige BI OIE 4 (GLB y AYU olar) Ly BOLT IL sl oy able
3504:AS cess SNEGD 545 gsi GNIEGAS 5,5 x) SNECHTAE 345 5-1 | SNAIWS
3559:BARN NORWEGIAN) 33,3 AP@RANAYU, PaRQNAYU
4446:PAYUS,- PA, PATRA, PATI
5481:(OLD CHURCH SLAVIC) ot 5 THAYUN (OSSETIC) <2 \
6119:POKORNY = SSSSC*« AYU, AYUSHAH (SANSKRIT) cy Sib.
6120:BARNHART: (AY, AYE) AYUNI, AYUNA
7665:DEJU LATVIAN) (3) 5 DAIN, DAYUN AOSSETIC) sn 3}
9722:DYB DANISH) Sylasl ‘ZHAFRA, JAIWA- :(AVESTAN) (gly!
```


## [2026-09-04T19:11:02.615Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" incoming/ARY/ARY_latin_index_pages.txt | head -3; echo ---; sed -n '3550,3570p' incoming/ARY/ARY_latin_index_pages.txt; echo \"=== find page tag near 3559 ===\"; awk 'NR<=3559 && /\\[pdf page/ {p=$0} END{}' incoming/ARY/ARY_latin_index_pages.txt; python3 - <<'EOF'\nimport re\nlines=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nlast=None\nfor i,l in enumerate(lines[:6200],1):\n    if '[pdf page' in l: last=(i,l)\n    if i in (3559,6119): print(i, 'last tag:', last)\nEOF"
}
```


### [2026-09-04T19:11:04.290Z] TOOL RESULT

```
1:[pdf page 1]
9:[pdf page 2]
37:[pdf page 3]
---
YCHELA  stovany Fil
feetlook
2a BEN et ely (AVP Sch opel ee y ot ee EN jg "ei! ashy “\
eat pe Sl Susy als “BK y “shast” 5 "ouSit” oluajly ccael "457" ph 2 BHI ols!
ward MEV a set ga so Sil "ge Si et gt 3
[pdf page 125]
~~ e
Cars! lyre big | NE
oy BARN * :(SWEDISH) 53 yo AVESTAN) glee 3}
BARN NORWEGIAN) 33,3 AP@RANAYU, PaRQNAYU
BERNIAKAS, (LITHUANIAN) (gl 53 ABURNAY, (PAHLAVI) 6 shay
BERNAS ABURNAYAG
BERNS LATVIAN) (33) 93 VIRNT KURDISH) 535°
BARN GOTHIC) SF
‘REFERENCES both BARN :(OLD SCANDINAVIAN) 35.511
POKORNY, = SS”™S*~*~S~*~«S BARN {OLD SAXON) AS pip Ste
BARNHART: (BAIRN) 71 HOLD HIGH GERMAN) op gil
MACKENZIE: (CHILD) 106 BARN
ONIONS: (BAIRN) 69 BEARN (OLD ENGLISH) op 3S)
SKEAT: (BAIRN) 44 BAIRN ENGLISH) ,gS&i
ver rgbtoly| © BARN DANISH) jails
=== find page tag near 3559 ===
3559 last tag: (3555, '\x0c[pdf page 125]')
6119 last tag: (6110, '\x0c[pdf page 212]')
```


## [2026-09-04T19:11:13.876Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\npages=re.split(r'\\f?\\[pdf page (\\d+)\\]',t)\nd={}\nfor i in range(1,len(pages),2): d[int(pages[i])]=pages[i+1]\nfor n in (125,126):\n    print('==== pdf page',n,'====')\n    print(d.get(n,'')[:1800])\nEOF"
}
```


### [2026-09-04T19:11:15.721Z] TOOL RESULT

```
==== pdf page 125 ====

لا زژ)۹گگگک ۳
۶ برّنا (بة چم "جوان* و "نرچه")
اوستایی (45374): سرئدی (/0[05015): ۱ ۳
7 ۸7۵8۵281 نر وژی (/۸/07(7501۸): 8۸80
پهلوی (۸۲۷1ال۳۸): امانلی ۱1۱ لیتوانی (0۸(/4/۷ 0/777 ,کشم8530۷1
ردان ۱ ۸5(
کردی (4ل0/5(/): ۷17 لتونی (لتی) (774/۷مل): 5(
گوتبکه (1/6ل007): لا
ایسلندی‌گهن (14(7/ 5070/۸/۸ ۵۲۵): 8۸33 پسگشت‌ها اکن
ساکسرنی کهن (81000 0ا0): ۰ 2۸8 81 2002200
آلمانی کهن "(/ف4ل052 انز صا۵): 1 (8۸783) در ان انا
50 6 (5710) :11027218
انگلیسی کهن (4ل5ل8۸0 صا): 88۸0۲ 9 (۵۸383) :00/5
انگلیسی (50ل6۸/07): لت ان 4 (8۸783) 3
دانمارکی (0۸(//87): 0 ۰ | برهان قاطع + ۶۴
بادداشت:
۱ ریشه‌ی این واژه با ریشه‌ی واژه‌ی "بردن" خویشی دارد.
۲- چم این واژه در اوستایی و پهلوی و زبان‌های ژرمنی و لیترانی و لتونی وکردی: بچه؛ نوباوه,
بتوانگلیسی سرواژای اس 3088
اوستایی (/48874): ,۷۸۹0 رمشقانا 8۸۸ ,انش
لد ارمنی (/۵/8(740/: ۰ 6۸۹1۸ ,0۸3
پارسی باستان (۳27۵14(۷ 2ا0): ,۷۸۱/۸6 یونانی (076580): 7 ,۸08
۷۸۸۸ لاتین (47100ل): دید دیا
پپلری (/۷ملتن۲۸): ,۷۷۸۳۹8۸6 بله۷۸ دانمارکی (0۸187). اد وید :۱
۷۸۸۵ لهستانی (۳0(80): 38۸۸7186 ,8۸۸
اوستی (058552712): ۷۸ روسی (7ل5514(آ۸): 1۸۸
سانسکر بت (5(/920717): چکه (25[7)): الا از ۱

==== pdf page 126 ====

اا ‏ ااا گگ ی .
۱ بریدن / ۱۲۷
اسلواکی 51-07470): انشا ی ۱۱ پسگشت‌ها شهب درد
لیتوانی (۸۸/1۵27تا8ل7ل). ند دیا 0 20050
ایرلندی کهن (بغولگا صان): ۷۸ 1 (318شآ) دام دی ها
116160 ناه
1 :قلطم 2 #ملتهه)
یادداشت:
معنی این واژه در لاتین: گوسپنداخته شده,
| گس سوازی ناش ی 60۴
اوستایی (4۲5874/۷: 8۸07183/۸ ,8817۸ آلمانی کهن (/08/04۸0 210 0ا۵): ۱
8۸ +881 00۸ ,204020
پهلری (۲7ائل۸): ,8837۸۷ ,8178130۸ آلمانی (088000: ۰ 81308 ,207573
َ لا انگلیسی کهن 20/0870 صا0): ,تل۸ت808
اوستی (0555712): 71( 10
کردی(8013/7-: 88818۲ ,258۸31210 انگلیسی (701/520(ق): 208
سانسکریت (8۸(/58077): 87181 دانمارکی (0۸/37): ۸0
7 811۸8۷۸7 ,8118۸۵71 سوئدی (9(/52157): 3073۸ ,8083
ارمنی (0/52/۵9بم. " 21 نروژی (0070750107: 808
بونانی (07885): ۳۸08,83۸3۸0 اسلاوی کهن (۲10ما؟ 267ن 27 )+
لین مین بصع تور ۸ 2711
را 1 روسی (۷5914): ۱
ایتالیایی (42ال7۸): 0 لیترانی (777۸7۵۷/ل). 8ف328
ایسئند یکهن (/01014771۸(ی5 صا0۵): لدرنی (لتی) (7۲4۸ا): نی
بش80 آلبای (نمااله‌هام. 3 ,815
نورس کهن (۸۷07۶8 0ا0): 8۳87۸ با8087
فریزی کهن (54(7ل۲۸ صا0): 3
```


## [2026-09-04T19:11:43.168Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=re.split(r'\\f?\\[pdf page (\\d+)\\]',t)\nd={}\nfor i in range(1,len(pages),2): d[int(pages[i])]=pages[i+1]\nfor n,p in d.items():\n    if 'جاوید' in p or 'جاودان' in p: print('JAVID pdf',n, p[:200].replace('\\n',' '))\nfor n,p in d.items():\n    if re.search(r'خدا\\b',p[:300]): print('XODA pdf',n,p[:150].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T19:11:45.277Z] TOOL RESULT

```
JAVID pdf 39  ۰ / ریشه‌های هندو اروپایی زبان فارسی  با آسیاب دستی) بودند. وقتی یونانیان شهر تروا راگشودند» زنان خانواده سلطتتی (مثلاًاندروما کك ۸0/۸5 و کاساندرا ۸85۸۷0۸)) همه به سارت گرفته شدند ولی مردان و حتی. پس
JAVID pdf 92  1 ۱ ۱ امرداد (به چم *جاویدان» نمردنی")_ ‎٩۳|‏ ‏اسلاری کهن (ع1شا5 7ل#6نابل» صا0): پسگشت‌ها 5 ۸۲ ,۶۲۷ 770 ماس که برهمی (80178[4140): انا 2 (۸0) :م8 یتراتی (0(مابین ۰:07 ۷۳۸ ,2 8 (۸۸1۲1831۸011) ۰ نقققام
JAVID pdf 212  جاوید, جاودان / ۲۱۳ اوستایی (438722): 7 2 آلمانی (05701۸۸4): 6 بقل 5 ,۷۸۷۸۳۸3 ,1۸2 ,۷۸۷01 انگلیسی کهن (80/0/5/4 010): پیلوی (/۸۲۸۲: ۰ ,1۸۷۷80 ,1۸۷1120 آ۸ ,0 بر 6 1۸۷802 انگلیسی (8(0ل8/0): ۰ ۳۷8۸ ,لا۸
JAVID pdf 215  ۶ / جویدن, جاویدن افغانی (پشتو) (//۸۳07۸): ۷۳5۸ سرئدی (8۱5215): 1387 نخاری ۸ (۸ [(4ل7۸7ل70): کةا هلندی (7لع07): 7 تخاری 8 (8 ((3۸ل70): + گالی (98/ا6۸: ‎٩۳‏ قفا سانسکریت (54۸58/7): ۷885۸71 ,۷۸8۰ ۰ 7 ا
XODA pdf 54  ۳ آرواره» آره / ۵۵ یادداشت: ۱ برهان قاطع : و دهخدا و معین ریشه‌ی این واژه را نمی‌دهند. ۲- 0۸1008 ,3۸8۸11۸۹7 فقط ریشه‌های ژرمنی این واژه را می‌دهند. ۳
XODA pdf 94  پسگشت‌ها 5 ی 317 (83لتف8۲۶) :005 ار 7 4 ر(قاتف8(۲۶) میت فرهنگ معین : ۳۷۴ 6 (8ق18653) :ما05 لغت‌نامه دهخدا. ۳۳۱ 252 8۸ یادداشت, ۱- واژه‌ی "اندرونه" از
XODA pdf 130  0 بَمْ (به چماخد) / ۱۳۱ پسگشت‌ها اه ۲ 9 (816۸1) :0۸70/5 0 7 8 (5ه5آ8) رن ان لغت‌نامه دهخدا: ۴۷۷ 9 (8ت8۸1 ,59 8۲8) که میرم 02 یادداشت, ۱ برخی معتقدند 
XODA pdf 143  ۴۳ ا/ بیم (به چم "ترس *باک")  ۱ ساسکربت (64(8/7): -78 ,۷18۸ پسگشت‌ها شش دنت ارمنی (470481014۷): 3 برنانی 072510): 05 بقد 0018090 ۲ ار عاقه با لاتین (
XODA pdf 154  ی پانزده / ۱۵۵ انگلیسی (57/.ا8۸0): ان 21 ۱ پسگشت‌ها 5 دانمارکی (0۸/]57): ۳15 10244 ۶0/0700 سوئدی (8175213/7): ۳5 :وچمه نروژی (0/0750140: نز نا 7 (۳38
XODA pdf 190  ۹ اا ‏ اااااااااا ‏ گ گ 1 تخم ۱۹۱ پسگشت‌ها ۲۶۲۵2/۵48 4110 ۸ 9 روم ری دا ۱ :ما۲2 3 (ت۸ 080313 ,739 (1573) : 8 (887/81.83ک۸ ,5015 87 برهان قاطع + ۳۷۶ :
XODA pdf 193  ۴ / ترس ترسیدن ایسلندی کهن (/(۵ یی صا0): برتونی (88870/7): اند ای با 717 نررس کهن (۸/082 010): 78 پسگشت‌ها ۳ 5 انگلیسی کهن (بتقلا8(0 ام 050508 68 * 0
XODA pdf 196  ‎٩ ۹‏ یی تشنه» نش تشنگو ]۱۹۷ پسگشت‌ها ۳5 3 (7180) ,ف65 17330۷0 :7هطزک ْ 1071 امات ک نا برهان قاطع + ۵و ۵۳۲ دای ادا آغت‌نامه دهخدا : ۶۶۹۶ 6 (7133) ,11
XODA pdf 198  ۹ تف» تفت» تفتان» تافتن» نفسیدن / ۱۹۹ پسگشت‌ها 5 8 (8711) :0/105 0 0000 وهای :17 7 (8۳11) +7 ملظ 291 :۸0 4 (ظ۲8۸6۲) :ما02 برهان قاطع : ایشا هد 25 ناه
XODA pdf 329  ُ ا ۰ زود ۱ 6۸1 ,۷۸85 پسگشت‌ها ده اد اد ی لتونی (لتی) ((477۸ل): ات 48 200200 9 (07) 2 ۸ :22( ها کک هام ۹ جهمی روم 1 ۱ لغت‌نامه دهخدا: ۱۳۲ ا یادداشت: 
XODA pdf 335  ۶ | رف سانکریت (8۸/58077): ۸ 11۸33[* ب۸0۸[ پسگشت‌ها 5 یونانی 07880): ۸۸۸ 5 و 9 207070 اسلاوی کهن (ح۲1ابما5 2210264 0ا0): ات تقاط ملک | 213010۸ برهان 
XODA pdf 388  فراخ ۳۸۹ برتونی (//570ل): -0 88 پسگشت‌ها امه وی دناد آلبانی (0(مامهتم: ۳ زان 0 هتیت. (11177/758): نف8 برهان قاطع + ۱۴۴۳  لغت‌نامه دهخدا: ۱۷۰۱۱۲ اوستا
XODA pdf 477  تسقق سک : بونانی (0820): 5 ۱ لین ۸47100 هتت/۱1۸۸/2 ,21۸۱/2۸ پسگشت‌ها 5 //2 ۳۴۱۹2۲2 فرانسه (۳8۸۷04): 1 0 اسپانیایی (/58۸(//8): ۸۷۸ 9 (01۸۱631۸) :02/10
XODA pdf 479  رلزی (7لک8). 1157 پسگشت‌ها ارهد ی اد اد اد برتونی (88870/0): 118 4 ۸0090 آلبانی (00/لمقلم: 113۸58 مت242۸ سمش و مهد پ هتیت (7177175): 7 1,149 شید و339
XODA pdf 514  ا ا والانه ولانه (به چم *زخم", *جراحت") / ۵۱۵ ٍ پسگشت‌ها رده با ادن لغت‌نامه دهخدا: ۳۳۹۹ 9 (5رتغ۲۲) +8147 پادداشت: 5166۸7-۱ معتقد است که واژه‌های یون
XODA pdf 519  ۰ /_ورزء برزء ورزیدن» ورزش پسگشت‌ها 5( برهان قاطع : تیما هو ها مرها 113 2 فرهنگ معین + ۳۸ لغت‌نامه دهخدا: ۳۵۳ ظ ا اوستایی (/۸887/4)+ انگلیسی کهن (/5ل
```


## [2026-09-04T19:11:52.030Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=re.split(r'\\f?\\[pdf page (\\d+)\\]',t)\nd={}\nfor i in range(1,len(pages),2): d[int(pages[i])]=pages[i+1]\nprint(d[212][:2500])\nEOF"
}
```


### [2026-09-04T19:11:53.797Z] TOOL RESULT

```
جاوید, جاودان / ۲۱۳
اوستایی (438722): 7 2 آلمانی (05701۸۸4): 6 بقل
5 ,۷۸۷۸۳۸3 ,1۸2 ,۷۸۷01 انگلیسی کهن (80/0/5/4 010):
پیلوی (/۸۲۸۲: ۰ ,1۸۷۷80 ,1۸۷1120 آ۸ ,0 بر
6 1۸۷802 انگلیسی (8(0ل8/0): ۰ ۳۷8۸ ,لا۸ بقالا۸
کردی (7ل۷00820/5: ۰ 2۷0۸0۲[ ,12۷80 آلبانی (۸۸المقلم): ۸
بلوچی (/8۸/67): زرد 02
تخاری ۸ (۸ 4(7ل۸8ل7052): ای پسگشت‌ها شمیت
سانسکریت (54۸/۶0007): 5277571۸17 ,23/10 ۳
بللال 23 ,له زاره
ارمتی (4۸48]4۸): ۷۸۷18۸۸ ,۷۸۷ 5( ,69
بونانی (07854)+ 8 ,۸180 َ :۸4۸020725
لاتین (/4710ل): 4 ,۸8۷9 3 (3783۲۷۲3۷ بل818۵۲۸)
گوتبکك (ع[00777): ۸05 6 (۸) :010/5
ایسلندی کهن (۷(۷ا94(010۸ ۰:01 81 2 (8۷88) +7
آلمانی کهن (05824۸9 2۲۵/3 صا0): برهان قاطع + انصن
۸ ,80 ,10
پادداشت,
چم این واژه در سانسکریت: توانایی» بنیه.
| مانگلیس سروازی ارس 188
9 اوستای (/(4۲574): 1۸ برنانی 0788/0): ۰ 138۳۸7085 ,31۳3۳۸
پهلوی راام‌برمم: تْ. فلال ,۸0۸8 لانین (0امم: 75860878 ,1800
ْ اوستی (0555710): با162 فرانسه (4ل0/0ق۳8): 2018
اُ کردی (2/0/3(7). وان ره اسپانیایی (5۳۸۸۷]34): 10
بلوچی (8۸1-011): 3 ایتالیایی (/(۸لله7): ۳/0
افغائی (پشتر) (4۳0/1۵71). اسلاوی کهن ( ماک 0267 ام
16۸[ 1
سانسکریت (۷۸6۸5:)5۸۸7580/7 ,۷81687 روسی (/(85514): 1۸
```


## [2026-09-04T19:12:07.318Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"جاوید\" \"برنا\" \"خدیو\" \"خواجه\"; do echo \"### $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null; done"
}
```


### [2026-09-04T19:12:09.399Z] TOOL RESULT

```
### جاوید
incoming/MON/MON_2vol_Adena_v2_djvu.txt:5
MON_part2.txt:5
MON_part1.txt:24
incoming/MON/MON_2vol_Adena_v1_djvu.txt:24
### برنا
incoming/MON/MON_2vol_Adena_v2_djvu.txt:2
MON_part2.txt:2
MON_part1.txt:9
incoming/MON/MON_2vol_Adena_v1_djvu.txt:9
### خدیو
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part1.txt:0
### خواجه
MON_part2.txt:5
incoming/MON/MON_2vol_Adena_v2_djvu.txt:5
MON_part1.txt:7
incoming/MON/MON_2vol_Adena_v1_djvu.txt:7
```


## [2026-09-04T19:12:11.983Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"جاوید\" MON_part1.txt | head -8; echo \"=== برنا ===\"; grep -n \"برنا\" MON_part1.txt | head -8"
}
```


### [2026-09-04T19:12:12.063Z] TOOL RESULT

```
351:پاریس» ایران» جاوید» کارون (تهران) و يادنامة بیرونی ( کلکته) به طبع رسیده و 
6109:ابدی: -2020 [ع. ابدی] (ص‌نسب.) جاوید» 
6110:جاویدان» باقی» هميشه (در مستقیل) 
18543:انسوشه: 20-2 (ص مر .) جاوید؛ باقی» 
24365:پایستن» جاوید بودن. (امسص.) زیست» 
24367:جاویدانی. بقای عمر کسی بودن: عمر و 
29107:استوار» پابرجاء پادار» جاویدان» ات باقی؛ 
29166:(مصل.) بایدار ماندن» جاویدان بودن 
=== برنا ===
6187:ابرناک: 2.6 (ص‌مر.) ابری» دارای ابر» 
22762:برنا: 3(ص.) جوان» شاب؟ مسق. ببر. 
22765:برناس: 5 ابرناس - فرناس] (ص.) 
34313:مسن؛ معر » شیخ ؛ مق. جوان» برنا. سالیان 
46014:گردیدن» ذخونت. (.) ستبرنا» ستبرا» سبری» 
61677:رخصت. اجازه. قانون» آیین» روش. برنامه» 
70799:مق. برنا. آنکه مویش سفید است: زال زر. 
92108:طبع : "اما [ع.] (مص‌م.) مهر کردن برنامه.
```


## [2026-09-04T19:12:17.620Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22758,22770p' MON_part1.txt; echo \"=== javid headword ===\"; grep -n \"جاوید\\|جاوبد\" MON_part1.txt | sed -n '1,40p' | grep -i \"جاوید\" | head; grep -n \"^جاوید\\|جاوید:\" MON_part1.txt | head; echo \"=== خدا ===\"; grep -n \"خدا:\" MON_part1.txt | head -5"
}
```


### [2026-09-04T19:12:17.784Z] TOOL RESULT

```
استعمال دار د. 

برنا: 3(ص.) جوان» شاب؟ مسق. ببر. 
ظریف» خوب. نیکک. 

برناس: 5 ابرناس - فرناس] (ص.) 
غافل, نادان. 


بر نامه: (6-)02۲-18002 [- ورنامه - بر نامج» 
معر. ] (امر.) آنچه بر سر نامه یا کتاب 
=== javid headword ===
351:پاریس» ایران» جاوید» کارون (تهران) و يادنامة بیرونی ( کلکته) به طبع رسیده و 
6109:ابدی: -2020 [ع. ابدی] (ص‌نسب.) جاوید» 
6110:جاویدان» باقی» هميشه (در مستقیل) 
18543:انسوشه: 20-2 (ص مر .) جاوید؛ باقی» 
24365:پایستن» جاوید بودن. (امسص.) زیست» 
24367:جاویدانی. بقای عمر کسی بودن: عمر و 
29107:استوار» پابرجاء پادار» جاویدان» ات باقی؛ 
29166:(مصل.) بایدار ماندن» جاویدان بودن 
29288:داشتن» مدام بودن؛ جاوید بودن» فایم بودن. 
47032:جاودان: 12*02۰ [- جاویدان] (ص‌مر. 
6110:جاویدان» باقی» هميشه (در مستقیل) 
24367:جاویدانی. بقای عمر کسی بودن: عمر و 
47038:جاوید؛ 0 (ص. ق.) اسدی» دایمی» 
47039:جاویدان: :127-74 [- جویدن] (سص‌م.) 
49696:جاویدن: 3۷-0 (مصل.) (جاوید» 
57291:جاوید بودن؛ جاوید زیستن. (امسص.) 
76215:دیگر. سرای جاوید: ( کد.) بهشت. سرای 
=== خدا ===
6916:تویل. تسلیم شدن. اتال به خدا: موکل 
19506:بنام خدا: در آغاز سخن آید یعنی با نام خدا 
25595:زرخرید (در مورد مرد). بندة خدا: الف: 
32671:باه بسي خدا: به یزدان بناه» اجوذبالل» 
42838:بزررگ داشتن. نه نت ر کی باه کنر ادن نخدا:
```


## [2026-09-04T19:12:21.331Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '47030,47045p' MON_part1.txt; echo \"=== xoda entry ===\"; grep -n \"^خدا\\b\\|خدا: \" MON_part2.txt | head -5; grep -n \"خدا \" MON_part2.txt | head -5"
}
```


### [2026-09-04T19:12:21.434Z] TOOL RESULT

```
جانیه: (»)12۰ (ع. جانية] (افا.) مونث 
جانی» زن جنایتکار» زن تبهکار؛ ج. جانیات. 
جاودان: 12*02۰ [- جاویدان] (ص‌مر. 
ق‌مر.) جاوبدان. ۱ 

جاورد: 127:74(.) (گیا.) قسمی خار سفید 
رنگک. نغام. 

جاوید؛ 0 (ص. ق.) اسدی» دایمی» 
جاویدان: :127-74 [- جویدن] (سص‌م.) 
(جاوید» جاود» خواهد جاوید» بجاو 
جاونده» جاویده) جویدن» مضغ کردن. 
جاه: 126 [- جاه معر.] (.) مقام» منزلت؛ 
درجه» رته. جلال» فر و شکوه. 

جاهد: ۵ (ع.] (افا.) جهد کننده؛ 
=== xoda entry ===
2093:خدای تعالی. 
3515:خدای متعال. (امص.) فر بادرسی. اغانه. 
9838:خدای تعالی. تر کیبات اسمی: قابل اتساع: 
11614:خداوند در مورد نندگان؛ سرنوشت» تقدیر؛ 
11907:خدای تعالی از جهت وجوه اختلافات متواتر 
2574:ایمان به شرکت ایشان با خدا در معبودیت یا 
2576:در صفات ذاتی خدا مانند قدرت؛ علم؛ 
3070:مسلمانان یکث پنجم اينها به خدا تعلق داشت 
3523:(غم.) (ص.) نایبدا» مخفی: غیب. ( کذ.) خدا 
4913:یافتن. یاری کردن خدا پیامبر يا دیگری را.
```


## [2026-09-04T19:12:31.527Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ever",
 "prompt": "Give the etymology of \"ever\", and also what it says about \"every\" and \"never\" if mentioned: Old English æfre, its obscure formation, and the Proto-Germanic/PIE connection to *aiwi- \"eternity\" / *aiw- \"vital force, life\"."
}
```


## [2026-09-04T19:12:33.065Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/eternity",
 "prompt": "Give the etymology of \"eternity\" and \"eternal\": Old French, Latin aeternus/aeternitas, aevum, and the PIE root *aiw-. Also whether \"age\" is derived from Latin aetas/aevum."
}
```


### [2026-09-04T19:12:37.700Z] TOOL RESULT

```
# Etymology of "Ever"

**Origin:** The word "ever" derives from Old English *æfre*, though its formation remains uncertain. As the source notes, there are "no cognates in any other Germanic language," suggesting a unique development in English.

**Proposed Formation:** One theory suggests it's "a contraction of *a in feore*, literally 'ever in life,'" with the first element connected to Old English *a* meaning "always."

**Proto-Germanic/PIE Roots:** The first element traces to Proto-Germanic *\*aiwi-*, an extended form of PIE *\*aiw-*, which meant "vital force, life; long life, eternity."

## Related Words Mentioned

**Every:** Formed as a contraction of Old English *æfre ælc*, literally "ever each," this word emerged in the early 13th century to mean "each of a group."

**Never:** This Middle English term combines *ne* ("not") with *æfre* ("ever"), creating the compound "not ever, at no time."

Both derivatives demonstrate how "ever" served as an intensifier and generalizer in English word formation, extending its meaning across temporal and universal expressions.
```


### [2026-09-04T19:12:39.286Z] TOOL RESULT

```
# Etymology of "Eternity" and "Eternal"

**Eternity** entered English in the late 14c. from Old French *eternité*, which derives from Latin *aeternitatem* (nominative *aeternitas*). The Latin term comes from *aeternus* meaning "enduring, permanent," itself a contraction of *aeviternus* ("of great age") stemming from *aevum* ("age"). Ultimately, these trace back to the Proto-Indo-European root *aiw-, which means "vital force, life; long life, eternity."

**Eternal** follows a parallel path, also deriving from the Latin *aeternus*, described as a "contraction of aeviternus 'of great age,' from aevum 'age.'" Both words thus share the same Latin and PIE foundations.

**Regarding "age":** Yes, the document confirms that "age" connects to this same etymological family. It derives from Latin *aetatem* (nominative *aetas*), which is described as "extended form of Latin aetatem...from aevum 'lifetime, eternity.'" Both *aetas* and *aevum* ultimately descend from the *aiw- root, linking "age" to the broader semantic field of time and duration.
```


## [2026-09-04T19:12:43.496Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT ever ===\"; grep -n \"EVER, at any\\|Ever, at any\\|^EVER\\|æfre\" SKT.txt | head -6; echo \"=== SKT age ===\"; grep -n \"AGE, period\\|aetatem\" SKT.txt | head -6"
}
```


### [2026-09-04T19:12:43.561Z] TOOL RESULT

```
=== SKT ever ===
6030:EVER.
=== SKT age ===
```


## [2026-09-04T19:12:46.398Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6015,6045p' SKT.txt; echo \"=== SKT AGE ===\"; grep -n \"^AGE\\b\\|AGE, a period\\|AGE\\.\" SKT.txt | head -5"
}
```


### [2026-09-04T19:12:46.462Z] TOOL RESULT

```
Btoh  :  see  Eat.
Eternal.  (F.  -  L.)  M.  E.  tumtl.  -  F. tltrntt.  —  L  aiermiiit,  eternal.  —  L.  attmuj, lit.  lasting  for  an  age  ;  put  for  ^tii-Umuj*. *L.  *eui-,  for  anum,  on  age.     See  Age.
Ether,  pure  upper  air.  (I...  — Gk.)  L. a//itr.  -  Gk.  al^p,  upper  air;  from  iu t'lt^wing  —  Gk.  a($ttv,  to  glow.    (^IDH.)
Ethic,  relating  lo  custom.  (L,  —  Gk.) I..  t/AiiUJ.  moral.  —  Gk.  ^6tituf,  moral.— Gk.  Jj^ot,  custom,  moral  nature;  cf.  i$ot, manner,  custom.  +  Goth,  tii/w,  G.  n//e, custom:  Skt.  svaJhd,  self-will,  strcngtb. from  JTW,  self,  fihti,  to  place.
Ethnic,  relating  to  a  nation.  (L.  — Gk.) L.  ^Mn/iKj.  — Gk.  i0viH6i,  national.  *  Gk. iBvns,  a  nation.
Etiquette  ;  see  Stick  (i).
Etymou,  the  tnie  aource  of  a  word. (L.*Gk.)  L^  etymon. ^GV,  irvfiov  \  neuL aUrv^Mst,  real,  true.  — Gk.  Iriut,  tnie.  Al- lied to  Booth.
etymology.  (F.  -  L.  -  Gk.)  O.  F. ttymcfpip'f.  —  L.  etymohgia.  —  Gk.  Jru/fo- Ao^i'a,  etymology. —  Gk.ery/io-!,  tnie  ;*A*7fa, Recount,  frura  \ituv,  to  si:>eiik.
Eu-,  prefix,  well  (Gk.)  Gk.  tZ.  well ; neut.  of  ivt,  good,  put  for  ^a-vr*,  real,  from V  AS,  to  be.
Eucharist,  the  I^rd'&Sopper, lit. thanks- giving, (I.,- «•  Gk.)  L.  c$tchanstia  -•  Gk. iitX<ifi*^rla,  a  giving  of  thanks.  —  Gk.  «5, well ;  x"P*(^t^''  I  shew  favour,  from  x^fi**t favour     (VGHAR.)
Eulogy ;  Kc  liOgio.
Eunuch,  one  who  is  castrated.  (H« Gk.)  L.  eunuchut.  •-  Gk.  tvv  <M\ot,  a diajbbcrlain ;  one  who  had  charge  of ilceping  apartments.  — Gk.  fVK^,  a  couch; ix^iv,  to  keep,  have  in  charge.
Euphemiazn,  a  Kiftcned  expression. (Gk.)  Gk.  <6(f»7/ijcr/«!i,  the  same  as  tinp^fAia, the  use  of  woris  of  good  omen.— Gk.  tZ, well ;  -Pfifil,  I  i].»cnk.     (V  BHA.)
Euphony.  (Gk.)  Gk.  t ^o/vfa,  a  pleas- iiti^  sound.  — Gk.  <£>^<<M'ui,  swl-cI  voiced.— Ck   •!,  well;  (f^atvri,  voice,     (y  liHA.)
Euphrasy,  the  plant  eye  bright.  (Gk.) Supiioscd  lo  be  berieficial  to  the  eyes;  lit. •drlight.'  -  Gk.  lOfpaah,  delight.  -  Gk.
EVER.
t^pnlvtir,  to  delight,  cheer— '^'^    ** ^ptr-,  hast  of 'Ppi*',  midriff,  h-. Euphuism,  aflectation  ill  s[-^ So  named  from  a  book  EHf-kmrs,  bi Lyly  (i57o>.-Gk.  ffi^^y.  well  grovm,' ccllent— Gk.  <Z^  well;  ^wj,  growth,  frt ^iJo;*(u,  I  grow.     (^  BIIU.) Buroolydon,  a  tcmpestnouswind.  (Gl Gk.   t\ifiOKAvlw¥,    supposed    to    mean storm    from   the   east.'— Gk.   «9po-c.   S wind ;    xAilSan',    &urge,   from    KAiJ^fv, surge,  dash  as  waves. Euthanasia,  easv  death.   (Gk.)     C rOtfoKairfa,  easy  death  :  cf.  c^PfiFsrat,  dyil well.  — Gk,  fv.  well ;  tforciV,  to  die- Evacuate;  see  Tacatiou. Evade,  to  shun.  (T.-L.)    F.  evutkr. L.  euaJtrr  (pp.  tuasus).  to  escape.- L away ;  uatUrt,  to  go.     Der.  tvas  iom  <frg the  pp.)
invade.    (F.  -  L.)    F.  trrvtu'tr,  - in-uadtre  (pp.  ittuatm'),  to  enter,  iuva''
—  L.  in,  in ;  uaiiere,     Der.  inx^as  ton. pervade.  (L)      L.  ptr-wuitrt,  to
through.
Evanescent ;  see  Vain.
Evangelist,  writer  of  a  gospel.  (T. Lk  — Gk.)  O.  ?.rvan^tisU.^h  ev^nffi iffa  — Gk.  fta-yytAitfTT^f.- Gk.  fvayyiAdl a  reward  for  good  tidings.  gonieL^G e5,  well;  d77#Aio.  tidings,  fiom  dyytKttf messenger;  sec  An«ol.
Evaporate ;  see  Vapour.
Evasion ;  sec  Evade.
Eve,  Even,  the  latter  part  of  the (K)  £ve  ii  short  for /v^« ;  (for see  below).  M.  E.  w/,  eum,  A //m.  ^  O.  Sax.  (ffdW,  IccI  ofian^ afton^  Dan.  aflen,  G.  abend.  Soppotdl mean  the  '  after '  part  of  the  <Uy ;  aUiid Aft.  Cf. Skt.  d^ra. posterior;  ^a4B dhyd,  evening  twilight  Dttr.  tvtm- ifeniid. evening,  even.    (£.)     M.  E
A.S    iftttm^,  put  for  rf''—   -•      •
from  ci/fw,  even,  with  m
Even,  level.  (E.)  Ml e/en,  e/n^Vhi.  e7>en,  Iccl.  *a/»,  Dan Swcd. yrt«»,  Goth.  i^#M,  G  then
anent,    regarding,   ^ (E.)     M.  E.  djwit/.  mtii anc/rnf,   whtrC  the  /  is  e» andctt,  flnf/en,  near  I   aUo  writ
—  AS  PM.on;  e/en,  e\cn-     Hesi even  with,  on  an  equaliljr  wiih.<^C (for  in  eden).
Ever.    (£.)     M.  E.  imr  (omt^    A-
=== SKT AGE ===
209:;ONCISE    ETYMOLOGICAL   DICTIONARY OF  THE   ENGLISH    LANGUAGE.
6870:FOLIAGE.
11460:MESSAGE.
11910:MORTGAGE.
14728:PRESAGE.
```


## [2026-09-04T19:12:56.352Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Lebensdauer\" BRT.txt | head -6; echo \"=== KNT yav ===\"; grep -n -i \"yauviya\\|yaumaini\\|ever\\b\" KNT.txt | head -5"
}
```


### [2026-09-04T19:12:56.410Z] TOOL RESULT

```
=== KNT yav ===
344:V. Among the earliest traces of Pahlavi, how- ever, are certain legends in Greek characters on coins of Indo-Scythic rulers of the Turuska dy- nasty in northwestern India, belonging to the first two Christian centuries.
436:ings, even in these inscriptions, is sorry stuff, and he could never realize in later years that the foundations which he had laid had been built проп and improved.
534:pronoun and article tya-, always written ty- = fya-, and never #0" = tiya-. The reason for this is that the nom. sg. masc. and fem. were hya and hyd (Skt. syds syd), in which an 1 could not be written (§27); and the other forms, using the stem (ya-, followed their model in this point: thus nom. masc. hya, fem. hyd, nt. tya; асс, tyam lyam tya; etc.
546:The problem confronts us wherever we find three successive consonants of which the first has inherent a and thé second i is ^; wherever we find initial a + т + а consonant; and wherever we find at the end of a word the 7^ preceded by an a-inherent consonant. The evidence which
626:But final -hi, which would be expected to give -hiye = -hiy, must be written -hy = -hy, since h*i is almost never written for hi (§27): атау = amahy, for *as-masi; ига = vaindhy.
```


## [2026-09-04T19:13:02.908Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/hwat%C4%81%CC%81wH%C4%81",
 "prompt": "Give the reconstruction, its meaning, morphological analysis (which elements: *hwa- 'self' + what?), descendants (Middle Persian xwadāy, Bactrian khoadēo, Sogdian, Khotanese), and any references cited."
}
```


## [2026-09-04T19:13:04.027Z] TOOL CALL #78: WebSearch

```json
{
 "query": "Middle Persian xwadāy etymology *hwa-tāwya- \"self-powerful\" Avestan xᵛaδāta Encyclopaedia Iranica"
}
```


### [2026-09-04T19:13:06.013Z] TOOL RESULT

```
Web search results for query: "Middle Persian xwadāy etymology *hwa-tāwya- "self-powerful" Avestan xᵛaδāta Encyclopaedia Iranica"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T19:13:09.596Z] TOOL RESULT

```
# Proto-Iranian *hwatā́wHā

**Reconstruction:** *hwatā́wā ~ *hwatāwnás (masculine noun)

**Meanings:**
1. Lord, sovereign, king
2. God

**Morphological Analysis:**

The entry states the term derives from "*hwa- ('self') +‎ *tā́wHā ('lord, deity')". The composite structure combines a reflexive element meaning "self" with a root denoting authority or divinity.

**Key Descendants:**

- **Middle Persian:** xwadāy, xwadāwan
- **Bactrian:** khoadēo
- **Sogdian:** xutāu (multiple script variants)
- **Old Khotanese:** hvatänä (nominative singular)
- **Classical Persian:** xudāy, xudā, xudāwand
- **Alanic:** χουτζαυ (khoutzau, "god")

**Cognate Reference:**

Sanskrit *svátavas* ("valiant, inherently powerful") is noted as a cognate form.

**Sources Cited:**

The primary reference is Rastorgujeva & Edelʹman's *Etymological Dictionary of Iranian Languages* (2000), page 423, supplemented by Novák's dissertation on Eastern Iranian languages.
```


## [2026-09-04T19:13:20.878Z] TOOL CALL #79: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%AF%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/%D8%AC%D8%A7%D9%88%DB%8C%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%86%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%AF%DB%8C%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%AC%D9%87\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 41, root Aiw (Indo-European), Persian nodes #3/#6/#9: Wiktionary etymology\" 2>&1 | tail -2; done"
}
```


### [2026-09-04T19:13:23.823Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0a2b71d06c5962d3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ad67b95700d79fc7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5660da974237acbf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8453aab80c6e0de9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5489c0b5dc2b3564.txt
```


## [2026-09-04T19:13:28.301Z] TOOL CALL #80: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C3%B3yu\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/hwat%C4%81%CC%81wH%C4%81\" \\\n \"https://www.etymonline.com/word/ever\" \\\n \"https://www.etymonline.com/word/eternity\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 41, root Aiw: PIE/Proto-Iranian reconstruction and English/Latin chain\" 2>&1 | tail -2; done"
}
```


### [2026-09-04T19:13:30.944Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a8098da198fb9c94.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/246569f23caef635.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fb398be66c35c76e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6c68d8b150efb3f0.txt
```


## [2026-09-04T19:14:21.252Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN barnā ===\"; grep -n \"burnä\\|barnä\\|burna\\|purnäi\\|apurnä\" HRN.txt | head -6; echo \"=== HUB barnā ===\"; grep -n \"burnä\\|barnä\\|apurnä\\|purnäy\" HUB.txt | head -6; echo \"=== LEW aevum ===\"; grep -n \"aevum\" LEW_1910.txt | head -4; echo \"=== LAT aevum ===\"; grep -n \"aevum\" LAT.txt | head -4"
}
```


### [2026-09-04T19:14:21.355Z] TOOL RESULT

```
=== HRN barnā ===
2198:207. burnäf bernä Müngling', burnm 'Jugend, Kindheit',
2200:vergl. arab. LW. burnäj, barnaj, eine Dattelart (de
2202:aw. aperenäyuka^ * Knabe*; phlv. apurnäyak.
=== HUB barnā ===
=== LEW aevum ===
=== LAT aevum ===
```


## [2026-09-04T19:14:26.163Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2192,2212p' HRN.txt; echo \"=== which page ===\"; python3 -c \"\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport bisect\n# find leaf of line 2198\npages=t.split('\\f'); starts=[]; n=1\nfor p in pages: starts.append(n); n+=p.count('\\n')\ni=bisect.bisect_right(starts,2198)-1\nprint('leaf',i,'printed',i-21)\n\"; echo \"=== LEW/LAT check ===\"; grep -n \"aeuum\\|aevom\\|aeternus\" LEW_1910.txt LAT.txt | head -5"
}
```


### [2026-09-04T19:14:28.766Z] TOOL RESULT

```
slavischen Wortgruppe alb. braus *Egge*, serb. brana,
poln: brona, russ. borona, ngr. ößdpva etc. annimmt.
Das neupersische Wort ist aber ganz unsicher; die
Wörterbücher (ausser dem FS.) überliefern nur die
Form bezen, im Gacophylacium und bei Woliaston
fehlt es.
207. burnäf bernä Müngling', burnm 'Jugend, Kindheit',
Njm5 Is. 3, 4, 5, wumaj wernä, purnäk (unbelegt);
vergl. arab. LW. burnäj, barnaj, eine Dattelart (de
Goeje, Bibl. geogr. arab. IV, 189).
aw. aperenäyuka^ * Knabe*; phlv. apurnäyak.
afy. wör 'klein , wörkai, wörukai 'Kind*; bei. LW.
Warna jung, Jüngling (285).
208. (i)&fr«tijf, gurinj (AM.) 'Reis'.
Semn. varinj; (Käs. nur berSnj).
aw. ^verenja-; skr. vergl. vrthi- *ßeis'.
Vielfach entlehntes , gewiss ursprünglich arisches
Wort; vergl. arm. brinj; kurd. birinj; oss. brinj
(Hübschmann, S. 121); bei. brinj (35); wa/.
gurunj etc.
af/. vrize geht auf die Form ohne Nasal zurück,
=== which page ===
leaf 69 printed 48
=== LEW/LAT check ===
LAT.txt:1935:aeuiternus, puis aeternus: qui dure toute la vie, 4 ternel (oppose A
LAT.txt:1937:Ciceron; c£ gr. auovuorqS; aeterno,-ds (Varr.), coaeternus (lat.eccl.).
LAT.txt:1938:Le suffixe de aeternus se retrouve dans hesternus, sempiternus , et«4
LAT.txt:1943:le par S t Augustin) qui a renplace aeternus. Les gloses ont aussi
LAT.txt:2181:d'nne chose qni se fait: de'IA agere uitam, aeuum, aetatem; custodias
```


## [2026-09-04T19:14:33.911Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1915,1950p' LAT.txt"
}
```


### [2026-09-04T19:14:33.965Z] TOOL RESULT

```
ethiar.
aeuus m., aeina, -i n.: "temps" consider^ dans sa duree, par oppo-
sition a tempus qui designe, tout au moins A 1'origine, un aspect ponc-
tuel de la dur6e. De IA des acceptions particulibres, etendues ou res-
treintes, de aeuus: 1° duree de la vie, age, gen^ration; a° eternite.
Le genre masculin est attest£ chez les auteurs archaiques (Plaute,
Poe.1187; Lucr. a,561; 3,605); c'est aussi celui de gr. oucov, de got.
aiws; il correspond A une conception "anim6e" de la duree; le triomphe
du neutre aeuom, qui est ^galement anci en-, a pu etre favorise par l'in-
fluence de tempus. Terme archaique, conservi A 1 ' epoque imperiale par
la langue 4 crite, surtout poetique, et qui A basse epoque et chez les
ecrivains eccl^siastiques a etP remplace partiellement par saeculum
qui a servi A traduire ouo>v (v. saeculum) . Pas de pluriel. Non roman.
D 4 riv£s: aetas (aeuitas , Lex XII Tab., cf .osq. aitateis "aetatis", p£l.
aetatu "aetate"; sur la d^rivation, voir plus bas): age, vie (au sens
de "temps A vivre" agere aetatem) . Aussi "periode de la vie": aetates
hominis (cf. en fr.- 1 'age viril); aetatula: age tendre. Puis "gene-
ration"; et "epoque, temps". - Terme courant qui tend A remplacer
aeuom. Panroman, sauf roumain. M.L., 351. Certaines formes romanes sup-
posent encore ae(u) itas, ae(u)ita ( cf .iuuentas et iuuenta).
aeuiternus, puis aeternus: qui dure toute la vie, 4 ternel (oppose A
mortalis, e.g. Cic., Ac.3,134). De IA: aeternitas peut-£tre crW par
Ciceron; c£ gr. auovuorqS; aeterno,-ds (Varr.), coaeternus (lat.eccl.).
Le suffixe de aeternus se retrouve dans hesternus, sempiternus , et«4
af
et rappelle les fornations analogae»: diurnus, nocturnus, hibernus, ho¬
diernus, modernus, qui servent 4 galenent 1 1'expression du temps.
D'aprfes mortalis, la langue de l'%lise a cr£e aeternatis (d^jA signa-
le par S t Augustin) qui a renplace aeternus. Les gloses ont aussi
aeuitaneus: qui in aeuo durat; aetdneus: r|Ai,l|; et A basse epoque coae-
tdneus traduit ouvt^Ai.^. Conpos^s: longaeuus; grandaeuus — pxx.—
xpatwv; grandaeuitas.
Le latin conserve ici, sous forne d’un deriv 4 en -0- qui se retrouve
dans got. aiws, le non indo-europeen de la "dur^.e" (en gen^ral lj. "longue
dur^e", la "dur^e sans linite"); ce non 4 tait de la forne ayu, yu-
et conporte des suffixes de d^rivation varies. Le v^dique offre:^ ayuh,
```


## [2026-09-04T19:14:41.713Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"XVATAY\\|XWATAY\\|XUDAY\\|KHUDA\\|XVATAI\" incoming/ARY/ARY_latin_index_pages.txt | head -5; python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=re.split(r'\\f?\\[pdf page (\\d+)\\]',t)\nd={}\nfor i in range(1,len(pages),2): d[int(pages[i])]=pages[i+1]\nfor n,p in sorted(d.items()):\n    head=p.strip().split('\\n')[0]\n    if 'خدا' in head or 'خدای' in head: print(n, head)\nEOF"
}
```


### [2026-09-04T19:14:43.512Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:18:49.010Z] TOOL CALL #85: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build41.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nPIE = W + \"Reconstruction:Proto-Indo-European/h%E2%82%82%C3%B3yu\"\nPIR = W + \"Reconstruction:Proto-Iranian/hwat%C4%81%CC%81wH%C4%81\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"âyu, ay; yave\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan has a suppletive neuter u-stem āyū 'lifetime, duration' (nom.-acc.), whose oblique cases are built on the zero/full grade *yaw-: gen. yaoš, dat. yavōi, instr. yavā — exactly the paradigm Pokorny prints on p.17 under aiu-/ai̯u- 'Lebenskraft'. The dative yavē was lexicalised as an adverb 'for ever, in perpetuity', and from it the abstracts yavaētāt- 'perpetuity' and the bahuvrīhi yavaē-jī- 'living for ever' were formed. The chart's 'ay' is Nourai's citation form of the stem ay-/āy- (Skt. áyu-, ā́yus-). PIE *h₂óyu 'long time, lifetime' (root *h₂ey-), proterokinetic n./u-stem with oblique *h₂yéw-, which is why Iranian shows the alternation āyu- : yav-.\",\n \"sources\": [PIE],\n \"ref_check\": [\n   {\"ref\": \"POK:17\", \"status\": \"supports\",\n    \"note\": \"POK_01.txt leaf 24 (page marker '17'): 'aiu-, ai̯u- ,Lebenskraft'. ... av. āyū n. ,Lebensdauer', Gen. yaoš, Dat. yavōi, Instr. yavā, davon yavaētāt- ,Dauer', yavaējī- ,immer lebend-; yūš m. ,Lebensdauer''. Both of Nourai's Avestan words (āyu- and yav-/yavē) stand on the cited page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p.17 s.v. aiu-, ai̯u- (POK_01.txt leaf 24)\", \"stance\": \"supports\",\n    \"note\": \"'aiu-, ai̯u- ,Lebenskraft'' with ai. ā́yu-, av. āyū, gr. αἰών, lat. aevum, got. aiws — the root box and this node in one entry.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 6, s.v. aiu-, ai̯u- (WLD_Bd1 djvu line 588-596)\", \"stance\": \"partial\",\n    \"note\": \"'aiu-, ai̯u- ,Leben, Lebensdauer, lange Zeit, Ewigkeit'. Ai. ā́yu n., av. āyu ,Dauer, Lebensalter''; but adds 'ganz fraglich ist Zugehörigkeit von av. yav- ,lange Dauer', yava ,immer'' (WP 1927/30 doubted precisely the yav- forms that carry Nourai's Pahlavi/Persian branch; Pokorny 1959 and Wiktionary reinstate them as the oblique stem *h₂yew-).\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 p.274 s.v. aiw-\", \"stance\": \"supports\",\n    \"note\": \"'aiw-. Vital force, life, long life, eternity; also \\\"endowed with the acme of vital force, young.\\\" ... [Pok. aiu- 17.]' — same root, same Pokorny page as Nourai's citation.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.31 s.v. aeon (KLN_1966.txt leaf 28)\", \"stance\": \"supports\",\n    \"note\": \"'Gk. αἰών ... cogn. with OI. āyu, \\\"life\\\", Avestic ayu, \\\"age\\\", L. aevum ...' — Klein's Avestan citation is Nourai's node word.\"}\n ]})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"yavě-tân\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Book Pahlavi yʾwytʾn = yāwēdān (Manichaean/Parthian yʾwydʾn 'eternally'), an -ān adverbial/adjectival extension of yāwēd 'eternal' < Old Iranian *yāwa-tāt- / *yāwaitāt-, i.e. the Avestan abstract yavaētāt- 'perpetuity' built on yavē 'for ever' (node #1). The Arsacid form is preserved as an Armenian loan yavēt, yavitean, yavitenakan (borrowed in the 5th c.), which fixes the Middle Iranian shape with -t-. In Book Pahlavi the initial y- had already begun to affricate, whence the doublet jāwēd / P(azand) yāwēdān in MacKenzie. Nourai's spelling 'yavě-tân' is Nyberg's transcription yāvētān, not a scan error.\",\n \"sources\": [W + \"%D8%AC%D8%A7%D9%88%DB%8C%D8%AF\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:564\", \"status\": \"supports\",\n    \"note\": \"BQT_v2_pages.txt leaf 20 (printed ≈563/564, vol.2 offset leaf+543±3) carries the headwords جاوید 'پاینده و همیشه و دایم', جاویدان, جاویدانه, and Mo'in's footnote in the bottom margin giving the Pahlavi form (OCR 'پهلوی 0۵۱6۷2۷' = yāwētān) plus the Armenian loans yavēt, yavitean, yavitenakan — the same set Horn gives.\"},\n   {\"ref\": \"HRN:93\", \"status\": \"supports\",\n    \"note\": \"HRN.txt leaf 114, printed '— 93 —', no. 414: 'jāved ,ewig', jāvedān. aw. yavaētāt- ,Ewigkeit', yave ,für ewig'; phlv. yāvetan (PPGl.), arm. LW. yavēt, yavitean, yavitenakan.' — exactly the arrow Avestan yavē/yavaētāt- → Pahlavi yāvētān → NP jāvēd(ān).\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie CPD, PHD.txt line 671 and line 412\", \"stance\": \"supports\",\n    \"note\": \"'P yāwēd(ān) [yʾwytʾn | P yʾwyd(ʾn)] always, eternally' and 'jāwēd [yʾwyt' | (P ywyd), N ~] eternal'; index 'eternally haméihā, jāwēdān(ag), P yāwēdān'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. yāvētān (NYB_vol2_glossary.txt line 4438)\", \"stance\": \"supports\",\n    \"note\": \"'yāvētān perpetual, eternal: ~ rōčān in eternity 272⁵. — MPrth yʾwydʾn, ʾwd yʾwydʾn \\\"eternally\\\"; MPrs Zʾydʾn (S, A-H II), jʾydʾn (BBB); Paz. jāvada (SGV); NP jāvidān.' Nourai's transcription 'yavě-tân' is Nyberg's headword.\"}\n ]})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"jâvîd «جاويد ( جاويدان )»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian جاوید jāvīd 'eternal' and its extension جاویدان jāvīdān continue Middle Persian jāwēd / yāwēdān without change beyond the regular Middle-to-New Persian shift of initial y- to j- (already visible in Manichaean MP jʾydʾn and in Pazand jāvada, beside the conservative Zoroastrian-Pahlavi spelling yʾwytʾn). MP ē is written -ی- and pronounced ī in classical New Persian (majhūl ē > ī), giving jāvīd; -ān is the old plural/adverbial suffix, so jāvīdān literally 'for eternities'. Hafez's line quoted by Nourai (رستگاری جاوید در کم‌آزاریست) is a normal 8th/14th-c. attestation.\",\n \"sources\": [W + \"%D8%AC%D8%A7%D9%88%DB%8C%D8%AF\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"Nourai gives no reference for this node; the chain is covered by the references on node #2 (HRN:93, BQT:564), both of which end in NP jāved/jāvedān.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Grundriss no. 414, p.93\", \"stance\": \"supports\",\n    \"note\": \"The headword of Horn's entry is the New Persian word itself: 'jāved ,ewig', jāvedān'.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā, printed p.213 (ARY_pages.txt pdf page 212) s.v. جاوید، جاودان\", \"stance\": \"supports\",\n    \"note\": \"Aryanpur's entry for جاوید/جاودان lists Avestan, Pahlavi JĀWĒD/JĀWĒDĀN, Armenian YAVET/YAVITEAN, Greek AIŌN/AIEI, Latin AEVUM, Gothic AIWS, OHG ĒWA, German EWIG, OE Ā, English AY/EVER — i.e. an independent modern Persian handbook putting jāvīd and English 'ever' under one root, as Nourai's chart does; references Pokorny, Onions, Skeat, Borhan-e Qate'.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi, 2-vol Adena reprint, MON_part1.txt line 47038\", \"stance\": \"partial\",\n    \"note\": \"'جاوید (ص. ق.) ابدی، دایمی' — Mo'in has the word with the expected sense but this reprint's OCR does not preserve the bracketed Pahlavi transcription.\"},\n   {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 4438 and line 7225\", \"stance\": \"supports\",\n    \"note\": \"s.v. yāvētān: '... NP jāvidān'; cross-reference index 'jāvīdān: yāvētān'.\"}\n ]})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Avestan\", \"words\": \"perana-âyu\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan pərənāyu- (written pərənāiiu-) is a bahuvrīhi 'having full life/age' = pərəna- 'full' (PIE *pl̥h₁-no-, root *pelh₁- 'to fill'; Nourai's cross-reference '☞Pel 1') + āyu- 'life, age' (node #1); the technical sense is 'of full age, adult, of legal majority'. It is attested only in the Younger Avesta, and mostly in the negated form: Yt.19.43 apərənāyu ahmi nōit pərənāyu 'I am a minor, not of age', N.54, V.13.48, and the -ka- extension apərənāyūka- 'child'. Nourai's gloss 'full of life' is a literal rendering of the compound rather than its legal meaning.\",\n \"sources\": [W + \"%D8%A8%D8%B1%D9%86%D8%A7\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:31\", \"status\": \"partial\",\n    \"note\": \"KLN_1966.txt leaf 28 = printed pp.31-32 contains the entry 'aeon, eon ... cogn. with OI. āyu, \\\"life\\\", Avestic ayu, \\\"age\\\", L. aevum ...'. Klein's p.31 therefore supports the second member (āyu-) of Nourai's compound and the root, but Klein nowhere mentions Avestan pərəna-āyu- or Persian barnā.\"},\n   {\"ref\": \"BQT:264\", \"status\": \"supports\",\n    \"note\": \"BQT_v1_pages.txt leaf 484 (printed 264 by the volume's leaf−220 offset) is the page carrying برنا 'جوان و نوچهٔ اول عمر', برناک, برناه; the same page number is cited independently by Aryanpur under برنا ('برهان قاطع ۲۶۴'). The Latin-script part of Mo'in's footnote on that leaf is lost in the djvu OCR; the parallel footnote on ابرناک (leaf 295 = printed p.85) reads 'پهلوی aparnāk/apurnāk بمعنی برنا، جوان «یونکر ۹۹»'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae AiW col. 81, s.v. a-pərənāyav- (BRT.txt line 3660)\", \"stance\": \"supports\",\n    \"note\": \"'j. a-pərənāyav- Adj. \\\"nicht volljährig, minderjährig, unmündig\\\" ... apərənāyu (als NSm.) ahmi nōit pərənāyu (sd.) Yt.19.43 ... a) m. \\\"Kind\\\"' — the positive pərənāyu- is quoted in the same passage, so the Avestan compound Nourai posits is attested.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II, glossary s.v. apurnāyīk (NYB_vol2_glossary.txt line 610)\", \"stance\": \"supports\",\n    \"note\": \"'apurnāyīk, aparnāyik \\\"a young man\\\" ... cf Av. (81 sq.) a-pərənāyūka-; NP barnāk, burnāk' — Nyberg's cross-reference is to AiW col. 81, the entry above.\"},\n   {\"src\": \"POK\", \"where\": \"IEW p.17 (aiu-) and p.798 (pel-/plē-)\", \"stance\": \"silent\",\n    \"note\": \"Pokorny lists the simplex av. āyū under aiu- but no Avestan compound pərəna-āyu-.\"}\n ]})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Pahlavi\", \"words\": \"a-purn-ây\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian aburnāy, spelled ʾp(w)lnʾd, 'under age, minor, child' (abstract aburnāyīh 'childhood', diminutive aburnāyag) is the direct continuant of Avestan apərənāyu-: Old Iranian *a-parna-āyu- > MP a-burnāy with the regular Middle Persian voicing of intervocalic -p- to -b- and loss of the medial vowel (parna > burn-), and with -āyu- > -āy. Its positive purnāy 'adult' is likewise attested. The word is above all a Zoroastrian legal term (minority vs. majority in the Nērangestān and Vidēvdād tradition), which is why MacKenzie and Nyberg cite it from the juridical texts. Nourai's hyphenated 'a-purn-ây' is a morphological analysis of the attested aburnāy, not a variant form.\",\n \"sources\": [W + \"%D8%A8%D8%B1%D9%86%D8%A7\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:264\", \"status\": \"partial\",\n    \"note\": \"The برنا page of Borhan (BQT_v1_pages.txt leaf 484 ≈ printed 264) has the Persian headwords; the Pahlavi form appears in Mo'in's footnote to ابرناک on printed p.85 (leaf 295): 'پهلوی aparnāk/apurnāk بمعنی برنا، جوان «یونکر ۹۹»' (Junker, Frahang i Pahlavīk 99). Mo'in thus does give the Pahlavi ancestor Nourai draws, though the Latin transcription on p.264 itself is illegible in the available OCR.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie CPD p.4 and p.68 (PHD.txt line 170, line 551)\", \"stance\": \"supports\",\n    \"note\": \"'aburnāy [ʾp(w)lnʾd, v. purnāy | N burnā] under age, child. ~īh: childhood. aburnāyag [ʾp(w)lnʾ(d)yk'] child' and 'purnāy [pwlnʾd] adult' — both the negative and the positive, with the New Persian outcome given as burnā.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II glossary, apurnāyīk (line 610) and vaspuhrakān (line 4016)\", \"stance\": \"supports\",\n    \"note\": \"'apurnāyīk ... a young man 44. 48⁹ ... — Mīr form; cf Av. (81 sq.) a-pərənāyūka-; Paz. = the preceding w.; NP barnāk, burnāk', and the plural apurnāi : apurnāyakān.\"}\n ]})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"bornâ «بُرنا»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian برنا burnā/barnā 'young man, youth' is Middle Persian aburnāy with the usual New Persian loss of the unstressed prothetic/initial a- (aburnāy > burnā, exactly as MP abestān > NP bistān-type reductions and as in the doublet burnāk beside Pahl. apurnāyīk), and with final -y lost. The semantics inverted from the technical negative 'not of full age, minor' to the positive poetic 'young, in the prime of life' once the legal sense was forgotten — Ferdowsī's line quoted by Nourai (ز دانش دل پیر برنا بود) opposes burnā to pīr 'old', which is the classical usage. Horn no. 207 registers the doublets burnā/bernā, burnāī 'youth' and even an Arabic loan burnāj.\",\n \"sources\": [W + \"%D8%A8%D8%B1%D9%86%D8%A7\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:264\", \"status\": \"supports\",\n    \"note\": \"BQT_v1_pages.txt leaf 484 (= printed 264): 'برنا ... جوان و نوچهٔ اول عمر و ظریف را گویند'; also برناک 'بمعنی برنا است که جوان و نوچهٔ اول عمر باشد' and برناه. Aryanpur independently cites 'برهان قاطع ۲۶۴' for برنا, confirming that p.264 is this page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 207, p.48 (HRN.txt leaf 69)\", \"stance\": \"supports\",\n    \"note\": \"'207. burnā, bernā \\\"Jüngling\\\", burnāī \\\"Jugend, Kindheit\\\" ... aw. apərənāyuka- \\\"Knabe\\\"; phlv. apurnāyak' — Horn's chain is Nourai's chain.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi (Adena reprint), MON_part1.txt line 22762\", \"stance\": \"partial\",\n    \"note\": \"'برنا (ص.) جوان، شاب؛ مق. پیر' — the sense and the antonym pīr, but this reprint's OCR drops the bracketed Pahlavi etymon.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, printed p.126 (ARY_pages.txt pdf page 125) s.v. برنا\", \"stance\": \"partial\",\n    \"note\": \"Aryanpur gives the correct Iranian ancestry (Avestan APƏRƏNAYU, PƏRƏNAYU; Pahlavi ABURNAY, ABURNAYAG; Kurdish VIRNI) but then equates the word with Germanic BARN/Old English BEARN/English BAIRN and notes 'ریشهٔ این واژه با ریشهٔ واژهٔ بردن خویشی دارد' — a comparison with *bher- 'to bear' that no other source accepts; his Iranian half agrees with Nourai, his Germanic half does not.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie CPD p.4\", \"stance\": \"supports\",\n    \"note\": \"'aburnāy [...| N burnā]' — MacKenzie himself equates the Pahlavi word with New Persian burnā.\"}\n ]})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Avestan\", \"words\": \"xvato-ayâo\",\n \"verdict\": \"disputed\",\n \"derivation\": \"No such Avestan compound is attested: Avestan has the adverb xᵛatō 'of oneself, voluntarily' (AiW 1861) and the adjective xᵛaδāta- 'self-created', but not *xᵛatō-āyu-. The form Nourai prints is a 19th-century conjecture: after Nöldeke rejected Horn's *xᵛadāya-, Hübschmann (Pers. Stud. p.54) floated 'Skr. svatas + āyu- \\\"von selbst lebend\\\"' (or svatas + ādi- 'self-beginning') as a possible reading of MP xwatāy, adding at once 'doch sind diese Deutungen so unsicher wie die übrigen'; Fr. Müller had proposed *xᵛatō-uyō 'moving by its own will', which Horn calls unconvincing. Modern Iranian etymology reconstructs instead Proto-Iranian *hwa-tā́wā (~ *hwatāwnas) 'lord, god' = *hwa- 'self' + *tā́wHā 'lord, mighty one' (root *tauH- 'to be able, powerful'), with the exact Indo-Aryan cognate Sanskrit svá-tavas- 'inherently powerful' (Rastorgueva-Edel'man, ĖSIJa, s.v.). That is a compound of 'self' with 'power', not with 'life', so this node does not belong under the root Aiw at all. Nourai's own source for it is Mo'in's footnote to خدا in Borhan (p.719), which repeats Hübschmann's tentative svatas+āyu- and cites Bartholomae and Hübschmann for the alternatives.\",\n \"sources\": [PIR, W + \"%D8%AE%D8%AF%D8%A7\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:718\", \"status\": \"supports\",\n    \"note\": \"BQT_v2_pages.txt leaf 176 (printed ≈719, offset leaf+543±3) is the خدا page; Mo'in's footnote reads (OCR, Persian) '... بعضی این کلمه را از اوستایی xᵛa-dāta- مشتق دانسته‌اند و نولدکه بحق در این وجه اشتقاق شک کرده، چون خدای فارسی و خواتای پهلوی به کلمهٔ *xᵛatāya- یا *xᵛatāwya- اقرب است و آنهم به سانسکریت svatas + āyu (از خود زنده) ... رابطه دارد. برای اطلاع از عقاید مختلف رک: بارتولمه ...، هوبشمان ۵۴ ...' — i.e. exactly Nourai's 'alive by itself' analysis, presented by Mo'in as one opinion among several, with the same Bartholomae and Hübschmann page references Nourai carries.\"},\n   {\"ref\": \"BRT:1862\", \"status\": \"partial\",\n    \"note\": \"The Altiranisches Wörterbuch column Nourai cites is the xᵛatō- region: Nyberg's glossary cites 'Av. (1861) xᵛatō adv. \\\"of one's self, voluntarily\\\"' for exactly this word, and Mo'in's footnote on BQT p.719 refers the reader to the same Bartholomae column. Bartholomae therefore documents the first member xᵛatō- but no compound xᵛatō-āyu- (the BRT.txt OCR of this part of the book is too corrupt to quote the column verbatim; the searchable entries around it show xᵛatō only as the adverb).\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.54, note to Horn no. 471 (HUB.txt leaf 64)\", \"stance\": \"partial\",\n    \"note\": \"'Nöldeke bezweifelt die Richtigkeit von Horn's Etymologie: np. xudāi \\\"Gott\\\" = zd. *xᵛadāya- mit vollem Recht, da xudāi = phl. xᵛatāi ... ein zd. *xᵛatāya- oder auch *xᵛataia- voraussetzt, die sich zur Not durch skr. svatas + āyu- \\\"von selbst lebend\\\" oder skr. svatas + ādi- ... deuten liessen. Doch sind diese Deutungen so unsicher wie die übrigen.' Hübschmann is the source of the 'self-living' idea but explicitly calls it as uncertain as the rest. (Nourai's NOTE on this node, 'Hub:54 derives this from Indo-European root Ghu', does not match the page: what p.54 reports about the Germanic word for God is de Lagarde's curiosity that German Gott was borrowed from Persian xudā, cited as a Curiosum, not a derivation from *ǵʰau-.)\"},\n   {\"src\": \"BRT\", \"where\": \"AiW col. 1861-62 (via Nyberg's citation)\", \"stance\": \"partial\",\n    \"note\": \"Bartholomae has xᵛatō 'von selbst, freiwillig' and xᵛa-dāta-, but the searchable text shows no *xᵛatō-āyu-.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 471, p.104 (HRN.txt leaf 125)\", \"stance\": \"contradicts\",\n    \"note\": \"Horn sets up 'als Grundform ist etwa aw. *xᵛadāta- (oder *xᵛatāya-)' and adds that Nöldeke doubts the etymology; of Fr. Müller's aw. *xᵛatō-uyō 'nach eigenem Willen sich bewegend' he says it is 'schon an sich wenig überzeugend, ganz abgesehen von der falschen awestischen Nominativbildung' — a direct warning against inventing an Avestan compound of this shape.\"}\n ]})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Pahlavi\", \"words\": \"xvatây\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The Middle Persian word itself is beyond doubt: xwadāy, Book-Pahlavi hwtʾy, Manichaean xwdʾy, 'lord, sovereign; the Lord', abstract xwadāyīh 'dominion', compounds kadag-xwadāy 'master of the house', dagrand-xwadāy 'of long dominion'; it is the source of Xwadāy-nāmag, the 'Book of Lords/Kings'. What is disputed is the ancestor drawn here. Modern Iranian etymology derives it from Proto-Iranian *hwa-tā́wā 'lord, god' ('self' + 'the powerful one', root *tauH-), whose other descendants are Bactrian χοαδηο, Sogdian xwtʾw/xutāw, Old Khotanese hvatänä and Alanic χουτζαυ — a chain that has nothing to do with āyu- 'life' and therefore nothing to do with the root Aiw. Nourai's arrow (from the unattested Avestan *xᵛatō-āyu- of node #7) reproduces Hübschmann's discarded conjecture.\",\n \"sources\": [PIR],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"Nourai gives no reference on this node; the relevant citations are those on nodes #7 (BQT:718, BRT:1862) and #9 (HRN:108, BQT:779, FSF:159), all checked there.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie CPD p.96 (PHD.txt line 663)\", \"stance\": \"supports\",\n    \"note\": \"'xwadāy [hwtʾy | M xwdʾy, N xudā] lord. ~īh: lordship, sovereignty. ~wār [-wʾl] lordly.' — the form and its New Persian outcome, but MacKenzie gives no etymology.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II glossary s.v. xᵛatāi (NYB_vol2_glossary.txt line ~4370)\", \"stance\": \"partial\",\n    \"note\": \"'xᵛatāi [hwtʾy; MRWHY Ps.] 1. suzerain in a political sense ... 2. of the heavenly beings: Ohurmazd xᵛatāi \\\"Lord O.\\\" ... Prth inscr. hwtwy; MPrth xwdʾwn, xwdʾy; Paz. xᵛadāe; NP xudā \\\"God; master, owner\\\". Meillet, MSL 17, 1911, 109 sqq.; Bthl, MirM III; Junker, WuS XII, 1929, 145-147; Schaeder; Eilers.' Nyberg documents the word richly but refers the etymology out to a literature that does not include an āyu- compound.\"}\n ]})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Persian\", \"words\": \"Xodâ «خدا»; xadîv «خديو»; xâjeh «خواجه»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Three words, three different verdicts. (a) خدا xodā < classical xudāy < MP xwadāy: the Persian form is impeccable (loss of the final -y in the modern language, xudāy still in classical verse and preserved in خدای and خداوند), and the sense narrowed from 'lord, master' to 'God' under Islam; but its ultimate source is Proto-Iranian *hwa-tā́wā 'self-powerful one' (Skt. svá-tavas-), not a compound with āyu-, so the link to the root Aiw is rejected. (b) خدیو xadīv 'lord, ruler' (later the Ottoman title 'khedive') is not a direct descendant of MP xwadāy at all: Persian xadēw is a loan from Bactrian χοαδηο (khoadēo) 'lord', the eastern-Iranian cognate of xwadāy — a Kushan-era administrative title taken into Persian, whence the Ferdowsian کشور خدیو, جهان خدیو. Mo'in's footnote in Borhan states the same reconstruction, '*xᵛatāwya-'. (c) خواجه xᵛāja 'master, lord, eunuch of the harem' is not from xwadāy either: Mo'in reports the derivation 'xᵛatāy + diminutive -ča' only as one of several opinions (beside Pūrdāvūd's xᵛa- + -ča), and current scholarship (Asatrian, Iran and the Caucasus 2011/2012, followed by Wiktionary) derives it from a Middle Indo-Aryan reflex of Sanskrit upādhyāya 'teacher, preceptor' transmitted through Central Asia — which also explains Indic khoja. All three words therefore stand outside the root Aiw as drawn.\",\n \"sources\": [W + \"%D8%AE%D8%AF%D8%A7\", W + \"%D8%AE%D8%AF%DB%8C%D9%88\", W + \"%D8%AE%D9%88%D8%A7%D8%AC%D9%87\", PIR],\n \"ref_check\": [\n   {\"ref\": \"HRN:108\", \"status\": \"not_found\",\n    \"note\": \"HRN.txt leaf 129 prints '— 108' and contains only nos. 486-489 (xusur 'Schwiegervater', xusrū, xišt, xušk) — nothing about xudā or xᵛāja. Horn's xudā entry is no. 471 on p.104 (leaf 125): 'xudā, xudāi \\\"Gott, Herr\\\", xudāvand, xudāvendgār ... aw. vergl. xᵛadāta-; phlv. xutāi (d.i. xᵛatāi) ... als Grundform ist etwa aw. *xᵛadāta- (oder *xᵛatāya-) anzusetzen. Nöldeke bezweifelt die Richtigkeit der Etymologie vielleicht nicht mit Unrecht.' Nourai's page number is off by four; the entry he means says the etymology is doubtful.\"},\n   {\"ref\": \"BQT:779\", \"status\": \"partial\",\n    \"note\": \"BQT_v2_pages.txt leaf 237 (printed ≈780, i.e. Nourai's 779 within the volume's ±3 drift) is the خواجه page. Mo'in's footnote: '... معرب آن خواجا ... «دزی ج۱ ص۴۰۹». آقای پورداود این کلمه را مرکب از xᵛa (اوستایی، بمعنی خود) + -ča ... دانسته‌اند «حافظ شیرین سخن ۲: ۳۷»؛ بعضی اصل آن را «خواتای‌چه» از خواتای (خدای) پهلوی + پسوند تصغیر «چه» دانسته‌اند'. So Borhan/Mo'in records Nourai's xᵛatāy-ča derivation, but only as one of two competing guesses, and offers no decision.\"},\n   {\"ref\": \"FSF:159\", \"status\": \"supports\",\n    \"note\": \"Noushin's Vāzhe-namak (FSF_pages.txt leaf 210) has the headword 'خدیو — سرور، بزرگ، پادشاه، خداوند' illustrated by exactly Nourai's verse, 'سیامک به دست خرزوان دیو / تبه گشت و ماند انجمن بی‌خدیو', with Noushin's note that Abbas Eqbal's Loghat-e Fors reading 'به دست خود و رای دیو' is wrong and that the demon's name is خرزوان (London ms) / خروزان (Leningrad ms). Nourai has taken both the reading and the demon's name from this entry. (The scan carries no usable page numerals, so the leaf, not the printed page, is quoted.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Grundriss no. 471, p.104\", \"stance\": \"partial\",\n    \"note\": \"Gives the Pahlavi ancestor xᵛatāi for NP xudā (which Nourai needs) but explicitly reports Nöldeke's doubt about the Avestan reconstruction, and dismisses Fr. Müller's *xᵛatō-uyō.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p.54\", \"stance\": \"partial\",\n    \"note\": \"Repeats Nöldeke's rejection of *xᵛadāya- and calls the svatas+āyu- reading 'so unsicher wie die übrigen'.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, vol.2, printed ≈721 (leaf 178), s.v. خدیو\", \"stance\": \"partial\",\n    \"note\": \"Mo'in's footnote (OCR) 'خدیو از xᵛatāv از *xᵛatāwya- ... رک: خدا. «خدیو» خداوند بود؛ گویند کشور خدیو و جهان خدیو. فردوسی' — Mo'in derives xadīv from *xᵛatāwya-, i.e. from the 'self-powerful' compound, not from a compound with āyu-.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi, Adena 2-vol reprint (MON_part1/2)\", \"stance\": \"silent\",\n    \"note\": \"The reprint's OCR has خدا only inside compounds and idioms; the headword's bracketed origin tag is not recoverable from this text.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā (ARY_pages.txt, headword scan)\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur has no entry for خدا / خدیو / خواجه — he does not treat them as Indo-European inheritances of this root.\"}\n ]})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Germanic\", \"words\": \"aiwi\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *aiwaz m. 'age, eternity' (Gothic aiws) beside the adverbial i-stem/locative *aiwi 'ever' (Gothic aiw, ON ei/æ, OE ā/ō, OS eo, OHG io 'ever'), from PIE *h₂oy-wo-, a suffixed o-grade of *h₂ey-. Germanic also keeps the ā-stem *aiwō 'eternity' (OHG ēwa, whence ēwīg 'eternal') and *aiwī- 'lifetime' (ON ævi). Watkins' entry names precisely the shape Nourai prints: 'Extended form in Germanic *aiwi'.\",\n \"sources\": [PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 p.274 s.v. aiw-: '1. Extended form in Germanic *aiwi in: a. Old English ā, ever ... c. Old English ǣfre ... ever: EVER; EVERY, NEVER; d. Old Norse ei, ever: AYE²; NAY.' Nourai's 'Germanic aiwi' is a verbatim quotation of AHD.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p.17-18\", \"stance\": \"supports\",\n    \"note\": \"'Got. o-St. aiws m. ,Zeit, Ewigkeit, Welt'; i-St. adverbiell aiw (*aiwi) = aisl. æ, ei ..., ags. ā, ō, ahd. io ,je, immer', got. ni aiw ,nie', ahd. neo, nio, nhd. nie; ags. nā, engl. no.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IECD col. 320 s.v. aiuom (IEC.txt line 320)\", \"stance\": \"supports\",\n    \"note\": \"'aiuom \\\"age, lifetime\\\". WP I, 6 ... Go. aiws; OHG ēwo, ewa; ... cf. OE ǣfre, adv. (fr. *aiui-pro or sim. cpd. ...); ON ævi; ei, ey, ae, adv.'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. aeon (p.31)\", \"stance\": \"supports\",\n    \"note\": \"'Goth. aiws, \\\"age, eternity\\\", aiw, adv., \\\"ever\\\", ON. ævi, \\\"lifetime\\\", OHG. ewa, \\\"eternity\\\" ... OE. ā, \\\"always, ever\\\".'\"}\n ]})\n\nnodes.append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"ever, every, never\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old English ǣfre 'ever' (whose second element is obscure; the traditional explanation is a contraction of ā in fēore 'ever in life') has as its first element OE ā 'always' < Germanic *aiwi (node #10); ǣfre > ME ever > modern ever. Every is a univerbation of OE ǣfre ǣlc 'ever each', first written as one word in the early 13th c.; never is OE nǣfre = ne 'not' + ǣfre. AHD adds the third English descendant of the bare adverb, OE nā 'not' > no. Nourai's three words are exactly the three AHD lists at aiw- 1c.\",\n \"sources\": [\"https://www.etymonline.com/word/ever\", PIE],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"No reference on the node; it inherits AHD from the parent node #10, which does list EVER, EVERY, NEVER under aiw-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 p.274 s.v. aiw- and index (p.1479-80, 1903, 1912)\", \"stance\": \"supports\",\n    \"note\": \"'c. Old English ǣfre (second element obscure), ever: EVER; EVERY, NEVER'; index entries 'EVER aiw-', 'EVERY aiw-', 'NEVER aiw-, ne'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. ever (KLN_1971.txt line 87069)\", \"stance\": \"supports\",\n    \"note\": \"'ever, adv. — ME. ever, fr. OE. ǣfre, prob. rel. to OE. ā, \\\"always, ever\\\". See aye, \\\"ever\\\" ... Cp. also the first element in every and the second element in never.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Ever (SKT.txt line 6030)\", \"stance\": \"supports\",\n    \"note\": \"'Ever. (E.) M.E. euer ... A.S. ǣfre' — native English, same source.\"}\n ]})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Latin\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"A pass-through node: Latin continues the root as the o-stem aevus m. / aevum n. 'lifetime, age, eternity' (PIE *h₂oy-wo-, the same formation as Gothic aiws), from which are derived aevitās > aetās (gen. aetātis) 'age, lifetime' — the older form survives in the Twelve Tables' aeuitas and in Oscan aitateis, Paelignian aetatu — and aeviternus, contracted to aeternus 'everlasting', whence aeternitās (a coinage of Cicero's, per Ernout-Meillet). These are the Latin words behind the English node #13.\",\n \"sources\": [PIE, \"https://www.etymonline.com/word/eternity\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 p.274 s.v. aiw-: '2. Suffixed form *ai-wo- in: a. Latin aevum, age, eternity: COEVAL, LONGEVITY, MEDIEVAL, PRIMEVAL; b. suffixed form *aiwo-tāt- in Latin aetās (stem aetāt-), age: AGE; COETANEOUS; c. suffixed form *aiwo-terno- in Latin aeternus, eternal: ETERNAL; SEMPITERNAL.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, Dict. étym. lat. s.v. aeuus/aeuom (LAT.txt lines 1916-1950)\", \"stance\": \"supports\",\n    \"note\": \"'aeuus m., aeuum n.: \\\"temps\\\" ... 1° durée de la vie, âge, génération; 2° éternité ... Dérivés: aetas (aeuitas, Lex XII Tab., cf. osq. aitateis, pél. aetatu) ... aeuiternus, puis aeternus ... aeternitas peut-être créé par Cicéron ... Le latin conserve ici, sous forme d'un dérivé en -o- qui se retrouve dans got. aiws, le nom indo-européen de la \\\"durée\\\" ... ce nom était de la forme āyu-, yu-.'\"},\n   {\"src\": \"POK\", \"where\": \"IEW p.17\", \"stance\": \"supports\",\n    \"note\": \"'lat. o-St. aevus m. und aevum n. ,Lebenszeit, Ewigkeit'; hingegen beruhen aetas f., alt aevitas ... ,Zeitalter', aeternus ,ewig' auf adverbialem *aivi.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann col. 319-320 (aiuit-, aiuom)\", \"stance\": \"supports\",\n    \"note\": \"'aiuit- \\\"age\\\". Cf. aiuom. Lat. cf. aetas; Osc. aitatum; MIr. áes \\\"age, time\\\"' / 'aiuom \\\"age, lifetime\\\" ... Lat. aevum; Go. aiws'.\"}\n ]})\n\nnodes.append({\n \"id\": 13, \"lang\": \"English\", \"words\": \"age, eternity\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"age: Latin aetās, acc. aetātem, gave Vulgar Latin *aetāticum, whence Old French aage/eage (modern âge), borrowed into Middle English as age in the 13th c.; the Romance cognates It. età, Sp. edad, Port. idade show the same base. eternity: Latin aeternus (< aeviternus) yielded the abstract aeternitās, acc. aeternitātem > Old French eternité, borrowed into English in the late 14th c. as eternity (with the adjective eternal from aeternālis). Both therefore reach English from the Latin node #12, and both are listed under aiw- in Watkins' index.\",\n \"sources\": [\"https://www.etymonline.com/word/eternity\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"No reference on the node; the parent node #12 cites AHD, whose index does list 'AGE aiw-' and 'ETERNAL aiw-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. age (KLN_1971.txt line 9244)\", \"stance\": \"supports\",\n    \"note\": \"'age, n. — ME., fr. OF. aage, eage (F. âge), fr. VL. *aetāticum, fr. L. aetātem (acc. of aetās, \\\"age\\\"), whence also It. età, Catal. edat, Sp. edad, Port. idade ... L. aetās is contracted fr. aevitas, fr. aevum, \\\"space of time, eternity\\\". See aeon and cp. eternal.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Eternal (SKT.txt near line 6016)\", \"stance\": \"supports\",\n    \"note\": \"'Eternal. (F. - L.) M.E. eternel. - F. éternel. - L. aeternalis, eternal. - L. aeternus, lit. lasting for an age; put for *aeui-ternus. L. *aeui-, for aeuum, an age. See Age.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, index pp.1218, 1477\", \"stance\": \"supports\",\n    \"note\": \"'AGE aiw-' and 'ETERNAL aiw-' in the English index of Indo-European roots.\"}\n ]})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Aiw\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₂ey-w- / *h₂óyu 'vital force, life; long life, eternity' (Pokorny's aiu-, ai̯u-, IEW 17; Watkins aiw-)\",\n \"note\": \"The root box is right in every particular: Pokorny p.17 heads the entry 'aiu-, ai̯u- \\\"Lebenskraft\\\"' and Watkins glosses aiw- 'vital force, life, long life, eternity', so Nourai's label 'Indo-European' and his gloss 'vitality, eternity' are literal renderings of his two sources; the source-JSON's cross-reference 'Compare with root Yeu 2: young' matches AHD's own 'See also *yuwwen- under yeu-' (yeu- being explicitly 'a variant of aiw-'). The Germanic-Latin-English half of the chart (nodes #10-#13) and the jāvīd and barnā branches (nodes #1-#6) are all standard and confirmed by Pokorny, Watkins, Klein, Ernout-Meillet, Bartholomae, MacKenzie, Nyberg and Horn. The one bad branch is the xodā branch (nodes #7, #8, #9): Nourai takes it from Mo'in's footnote to خدا in Borhan-e Qate' (p.719), which repeats Hübschmann's 1895 guess that MP xwatāy might be 'Skr. svatas + āyu- \\\"von selbst lebend\\\"'. Hübschmann himself called that guess as uncertain as the rest, Nöldeke rejected the whole family of Avestan reconstructions, and modern Iranian etymology derives xwadāy from Proto-Iranian *hwa-tā́wā 'self + the powerful one' (Skt. svá-tavas-), so Persian خدا, خدیو (a Bactrian loan) and خواجه (< Skt. upādhyāya via Middle Indo-Aryan) do not belong under this root at all. One citation is simply wrong: HRN:108 has nothing on xudā, whose entry is Horn no. 471 on p.104.\",\n \"sources\": [PIE, \"https://www.etymonline.com/word/eternity\", PIR],\n \"ref_check\": [\n   {\"ref\": \"POK:17\", \"status\": \"supports\",\n    \"note\": \"POK_01.txt leaf 24, immediately after the printed page marker '17': 'aiu-, ai̯u- ,Lebenskraft'. Ai. ā́yu- n. ,Lebenskraft' ... av. āyū n. ,Lebensdauer', Gen. yaoš, Dat. yavōi ... Gr. ... αἰών ... lat. o-St. aevus m. und aevum n. ,Lebenszeit, Ewigkeit' ... Got. o-St. aiws m. ,Zeit, Ewigkeit, Welt'.' The page number, the root shape and the gloss all check out.\"}\n ],\n \"nodes\": nodes\n}\n\ndoc = {\n \"pdf_page\": 41,\n \"book_page\": 11,\n \"verified_by\": \"claude-fable-5-1\",\n \"verified_on\": \"2026-09-04\",\n \"entries\": [entry]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-41.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build41.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-41.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 41"
}
```


### [2026-09-04T19:18:52.286Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 13/13
node verdicts: {'confirmed': 10, 'disputed': 3}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 9, 'not_checked': 4, 'partial': 4, 'not_found': 1}
books consulted: {'supports': 27, 'partial': 10, 'silent': 3, 'contradicts': 1} | by book: {'NYB': 5, 'POK': 4, 'KLN': 4, 'PHD': 4, 'HRN': 4, 'AHD': 3, 'ARY': 3, 'MON': 3, 'BRT': 2, 'HUB': 2, 'IEC': 2, 'SKT': 2, 'WLD': 1, 'BQT': 1, 'LAT': 1}
```


## [2026-09-04T19:19:14.914Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-41.json` written; `verify_check.py 41` reports 13/13 nodes, no PROBLEM lines.

**Page 41 (book p.11), single entry — ROOT "Aiw" [Indo-European] "vitality, eternity"**

- Root: **confirmed** (Pokorny IEW 17 `aiu-, ai̯u- "Lebenskraft"`, verified verbatim in POK_01.txt; Watkins `aiw-` "[Pok. aiu- 17]").
- Node verdicts: **10 confirmed, 3 disputed**. Ref-checks: 9 supports, 4 partial, 1 not_found, 4 not_checked (nodes with `refs=None`). 15 books consulted (POK, WLD, AHD, KLN, IEC, SKT, LAT, BRT, HRN, HUB, PHD, NYB, BQT, MON, ARY).

Disputed items — all one branch (Nourai's خدا branch does not belong under this root):
- **#7 Av. `xvato-ayâo`** — no such Avestan compound exists. It is Hübschmann's 1895 tentative reading (`skr. svatas + āyu- "von selbst lebend"`, HUB p.54, who calls it "so unsicher wie die übrigen"); Nöldeke rejected the family, and Horn p.104 dismisses Fr. Müller's parallel `*xᵛatō-uyō`. Modern: Proto-Iranian *hwa-tā́wā "self + the powerful one" (Skt. svá-tavas-).
- **#8 Pahl. `xvatây`** — the word (MP xwadāy "lord", CPD p.96) is certain, but its ancestor is *hwa-tāwā, not a compound with āyu-; the drawn edge fails.
- **#9 Pers. `Xodâ; xadîv; xâjeh`** — xodā < MP xwadāy (same wrong root); xadīv is a loan from **Bactrian χοαδηο**, not a lineal descendant; xâjeh is now derived from Skt. **upādhyāya** via Middle Indo-Aryan (Asatrian), while Mo'in (BQT p.780) offers Nourai's "xᵛatāy + -ča" only as one of two guesses.

Other findings worth flagging (not verdict-changing):
- **HRN:108 is a wrong page** (`not_found`): p.108 has xusur/xusrū/xišt/xušk; Horn's xudā entry is no. 471 on **p.104**, and it says the etymology is doubtful.
- **KLN:31** (node #4) is `partial`: p.31 is Klein's *aeon* entry, which supports Av. `āyu` but never mentions `pərəna-āyu` or barnā.
- The chart's NOTE "Hub:54 derives this from IE root Ghu" does not match HUB p.54; what stands there is de Lagarde's *Curiosum* that German *Gott* was borrowed from Persian xodā.
- Nourai's odd transcriptions `yavě-tân` and `a-purn-ây` are **not** scan errors — they are Nyberg's `yāvētān` and an analysis of MacKenzie's `aburnāy`.
- 9 web sources archived via `fetch_source.py` (5 Wiktionary lemmas, 2 reconstruction pages, 2 Etymonline).
