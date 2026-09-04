# Verification process log — verify-page-53


## [2026-09-04T19:47:46.008Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 53 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-53.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-53.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-53.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 53` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T19:47:47.626Z] AGENT

I'll start by reading the instructions.


## [2026-09-04T19:47:49.740Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:47:49.754Z] TOOL RESULT

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


## [2026-09-04T19:47:49.774Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-53.txt"
}
```


### [2026-09-04T19:47:49.795Z] TOOL RESULT

```
1	=== PDF page 53 (book page 23) ===
2	--- entry 0 ---
3	ROOT [Pahlavi] Âmon : full, filled with  (refs SNS:6)
4	#1 (parent #0) [Persian] refs=SNS:6; BQT:61; MON:91 | âmŭdan «آمودن» : to fill with, mix with ; gohar-âmŭd «گوهرآمود» : filled with gems | extra: آمو ، آمون
5	#2 (parent #0) [Pahlavi] refs=SNS:6 | abr-âmŭn : "filled with clouds", cloudy ☞Nebh
6	  #3 (parent #2) [Persian] refs=SNS:6 | abr-âmŭn «ابرآمون» : cloudy | NOTE: This word is apparently obsolete.
7	--- entry 1 ---
8	ROOT [Arabic] A'.m.r : to command  (refs KLN:26; FVA:33)
9	#1 (parent #0) [Persian] refs=FVA:33; MON | amr «امر» : order ; mîrzâ «میرزا» : Nobel born ☞Gene 1 ; ammâreh «امّاره» : commanding, demanding ; ma'mŭr «مأمور» : agent (one who has orders) ; emârat «إمارت» : kingdom, state | extra: امور ، اوامر ، امیر ، أمرا ، آمر ؛ مأموریت ؛ امارات
10	#2 (parent #0) [Arabic] refs=KLN:26; FSD:38 | Amîr-al-bahr : commander of sea ; Amîr-ar-rahl : commander of transportation
11	  #3 (parent #2) [Late Latin] refs=FSD:38; KLN:26 | amiralis, admiralis : sea commander | NOTE: "bahr" or "rahl" has been dropped.
12	    #4 (parent #3) [Old French] refs=FSD:38 | amiral : sea commander
13	      #5 (parent #4) [English] refs=AHD | admiral
14	        #6 (parent #5) [Persian] refs=MON:36 | âdmîrâl «آدمیرال» : admiral
15	
```


## [2026-09-04T19:47:53.689Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-53.json && echo \"=== MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-04T19:47:53.857Z] TOOL RESULT

```
{
  "pdf_page": 53,
  "book_page": 23,
  "entries": [
    {
      "root": {
        "name": "Âmon",
        "lang": "Pahlavi",
        "refs": "SNS:6",
        "gloss": "full, filled with"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "SNS:6; BQT:61; MON:91",
          "words": [
            {
              "translit": "âmŭdan",
              "gloss": "to fill with, mix with",
              "script": "آمودن"
            },
            {
              "translit": "gohar-âmŭd",
              "gloss": "filled with gems",
              "script": "گوهرآمود"
            }
          ],
          "script_extra": "آمو ، آمون",
          "note": null,
          "quote": {
            "text": "هم زبانشان ز فحش آموده - هم درونشان به خبث آلوده",
            "poet": "Sanâî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "SNS:6",
          "words": [
            {
              "translit": "abr-âmŭn",
              "gloss": "\"filled with clouds\", cloudy",
              "script": null,
              "see": [
                "Nebh"
              ]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "SNS:6",
          "words": [
            {
              "translit": "abr-âmŭn",
              "gloss": "cloudy",
              "script": "ابرآمون"
            }
          ],
          "script_extra": null,
          "note": "This word is apparently obsolete.",
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "A'.m.r",
        "lang": "Arabic",
        "refs": "KLN:26; FVA:33",
        "gloss": "to command",
        "also": {
          "name": "Amîr",
          "gloss": "commander"
        }
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "FVA:33; MON",
          "words": [
            {
              "translit": "amr",
              "gloss": "order",
              "script": "امر"
            },
            {
              "translit": "mîrzâ",
              "gloss": "Nobel born",
              "script": "میرزا",
              "see": [
                "Gene 1"
              ]
            },
            {
              "translit": "ammâreh",
              "gloss": "commanding, demanding",
              "script": "امّاره"
            },
            {
              "translit": "ma'mŭr",
              "gloss": "agent (one who has orders)",
              "script": "مأمور"
            },
            {
              "translit": "emârat",
              "gloss": "kingdom, state",
              "script": "إمارت"
            }
          ],
          "script_extra": "امور ، اوامر ، امیر ، أمرا ، آمر ؛ مأموریت ؛ امارات",
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:26; FSD:38",
          "words": [
            {
              "translit": "Amîr-al-bahr",
              "gloss": "commander of sea",
              "script": null
            },
            {
              "translit": "Amîr-ar-rahl",
              "gloss": "commander of transportation",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Late Latin",
          "refs": "FSD:38; KLN:26",
          "words": [
            {
              "translit": "amiralis, admiralis",
              "gloss": "sea commander",
              "script": null
            }
          ],
          "script_extra": null,
          "note": "\"bahr\" or \"rahl\" has been dropped.",
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Old French",
          "refs": "FSD:38",
          "words": [
            {
              "translit": "amiral",
              "gloss": "sea commander",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "admiral",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:36",
          "words": [
            {
              "translit": "âdmîrâl",
              "gloss": "admiral",
              "script": "آدمیرال"
            }
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


## [2026-09-04T19:47:56.506Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['SNS','BQT','MON','KLN','FVA','FSD','AHD','HRN','HUB','PHD','NYB','POK','WLD','SKT','WEB','FVQ','AFM','PLA','LKT','ARY','IEC','SYN','CHEUNG','BRT','KNT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False))\n\""
}
```


### [2026-09-04T19:47:58.083Z] TOOL RESULT

```
<persisted-output>
Output too large (39.9KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bhlx7c2jy.txt

Preview (first 2KB):
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image", "covers_etymology": true, "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."}
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Ka
...
</persisted-output>
```


## [2026-09-04T19:48:05.083Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['FVA','FSD','KLN','MON','BQT','AHD','SNS']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print('==',k,v.get('title'))\n    print('  offset:',v.get('page_offset'))\n    print('  local:',v.get('local_file'))\n    print('  hint:',str(v.get('lookup_hint'))[:400])\n\" ; echo \"=== BIB FVA ===\"; grep -n -i 'FVA' bibliography_raw.txt | head -20"
}
```


### [2026-09-04T19:48:06.873Z] TOOL RESULT

```
== FVA S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989
  offset: None
  local: None
  hint: Searched archive.org, ketabnak, noorlib, web: no digital copy found.
== FSD Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)
  offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
  hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== KLN E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
  hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== MON Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)
  offset: None
  local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
  hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab
== BQT Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)
  offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
  local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
  hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metada
== AHD W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)
  offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
  hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.
== SNS Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986
  offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
  local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt']
  hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
=== BIB FVA ===
3: TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
12: TABLE IV - Reference Abbreviations (continued...) 32 FIB 33 FNI 34 FRS 35 FSD 36 FSF 37 FVA 38 FVF 39 FVQ 40 FWE 41 FWK 42 GPL 43 HID 44 HJB 45 HRN 46 HUB 47 IEC Pur Davfld, Farhang Iran Bastan, Vol. I, University of Tehran Press 1326 (1947). F. DanaT, Farhang Namhay Irani, Negah Publishers, Tehran 1370 (1991). AsadT Tflsi, Farhang Fors, Kharazmi Press, Tehran 1365 (1986). ^iljjl ^cUj^cLs &gt;^fl&gt;jS Funk and Wagnalla, New Standard Dictionary of the English Language, Funk &amp; Wagnalls Company, New York, 1940. A. H. Noushin, Farhang Shahnameh Ferdowsi, oULS 03I3 - ^-jiy i*La&gt;Li ^^ay Vajheh Namak, Donya Press, Tehran 1363 (1984). S. M. Nahvi, Farhang VSm J-^-i - ^-&gt;jl» j* ^o^ ^gb. 03I3 ^(3 ^S^a,^ Vajhehhay Arabi dar Farsi, Dakhil, TohT Azadi Press 1368 (1989). S. M. A. Emam Shflshtari, ^c ^bj ji ^-"j1* iS^ °j'3 «-fc»j» Farhang Vajhehhay Farsi dar zaban Arabi, Anjoman Asar Melli, No 58, Bahman Press, Tehran, 1347 (1968). A. Jeffrey, The Foreign Vocabulary of the Qur'an, (see VDQ). Oriental Institute, Baroda, Stephen Austin &amp; Sons Press, Great Britain 1938 A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, Warner Books, 1966. R. Dvorak, "Fremdworter im Koran", Doctoral Dissertation, Akademische Buchdruckerei von F. Straub (1884). J.T. Platts and G.S.A. Ranking, A Grammar of the Persian Language, Oxford University Press (1911). B. Bartholomae, Handbuch der Altlranischen Dialekte, Breitkopf &amp;Hartel, Leipzig 1883. H. Yule &amp; A. C. Burnel, Hobson Jobson, A Glossary of Colloqual AngloIndian Words, Oriental Publishers, Delhi 1903-1968. Paul Horn, Grundriss der NeuPersischen Etymology, Verlag von Karl J. Trubner, Strassburg 1893-1974. H. Hubschmann, Persische Studien, Verlag von Karl J. Trubner, Strassburg 1895. Stuart E. Mann, An Indo-European Comparative Dictionary, Helmut Buske Verlag, Hamburg 1987 A-ll
```


## [2026-09-04T19:48:38.076Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS amon/amun ===\"; grep -n -i -E 'am[uūō]n|āmōn|abr-' SNS.txt | head -40; echo \"=== SNS_pages leaf for abr ===\"; grep -n -i 'abr' SNS_pages.txt | head -30"
}
```


### [2026-09-04T19:48:38.143Z] TOOL RESULT

```
=== SNS amon/amun ===
1967:: lJ i** abr-amOn t ^-JS^ j .aj^T^Uji. U *** .a-i^JT^l^L L«** 
=== SNS_pages leaf for abr ===
1149:                                                                                                                                               :     i**    abr-amOn                   t   ^-JS^ j       .aj^T^Uji. U *** .a-i^JT^l^L L«**
1319:1o                                          is* '*U«0*V : abrninftiu
7442:                                                                   t»m*> _!>«*                     •fiJbgaljJ,!^^ rj^wr ,5^. :stabra2f/stavrak:
15844:                                                         spandmad gah 176/14               stabrajr/stavrak 178
16501:abr/avr 11/7                    afzOnlgiha 18/4
16503:abramOn 11/10                   afzQn 17/19
```


## [2026-09-04T19:48:41.016Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG maH ===\"; grep -n -i -E 'āmūdan|amudan|paymūdan|paymudan' CHEUNG.txt | head -30; echo \"=== HRN ===\"; grep -n -i -E 'āmūdan|amuden|āmūd|amud' HRN.txt | head -30; echo \"=== PHD ===\"; grep -n -i -E '^āmu|āmuxt|āmad|hamōy|āmēz' PHD.txt PHD_mackenzie.txt | head -30"
}
```


### [2026-09-04T19:48:41.096Z] TOOL RESULT

```
=== CHEUNG maH ===
=== HRN ===
=== PHD ===
PHD.txt:161:a- P- | M ?-] privative prefix, un-, Jess, а D] then (generally with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: powerlessness; anarchy. abādyāwand Pf?tyd”wnd | J ?b’dywn<d>] powerless, weak. ~ih: powerlessness, weakness. арар [LW TE < A lwt-h | M?Pg, N (a)bā] with. ~ih Dë kuk) company, assistance. abāgēnīdan, abāģēn- [^P'kyn-ytn!] accompany. a-bahr РРА] portionless, deprived. abām Pf?m | P ?bmyh, N (a)wàm] loan, debt. Abàn PPn! | M'0x, N ~] cal. 8th month; roth day. aband (nd, v. рапа | M ?bnd] erring. “АҺ: error. 'abar [ODM < А дат; bl | M "be, N bar] up; on, over. ~ āmadan: rise (sun). ~ āxistan: rise up. ~ āxrāmīdan: step up. — burdan : undertake. ~ madan: cope with, comprehend. ~ nigeridan: consider. ~ nihumbidan: conceal. ~ niSastan: sit, be enthroned. ~ nišāstan: seat, install. ~ rasidan: come to, upon. ~ rasidan б: attain. tabar Dél higher, superior. ~ag [-g | MP brg] superior. ~agan(ag) [-k’n(k)'] superior. --dar [-t, Zenit | M ?brdr] higher. ~dom [-twm | M ?brdwm] highest. —domih [-twmyh] superiority. abargar [5/21 god, divinity. abarig(àn) ['Bblyk( ny] = abarag. abarig DPryk! | M ?Pryg, J ?Pry] other.
PHD.txt:191:amāwandīh: power, strength. ambag [’mbk' | N anbajat] a preserve, conserve. ambar [mbl, ?nbl | Аг. ‘праг ambergris. ambarag [?mblk! | N anbara] hairless (animal). Р amburdan [h/^mbwultn! | Р ?mPr-] = hambārīdan. a-menīdār [^mynyt!l] unthinking. āmēxtan, āmēz- Pmyhtn', ?тус- | M *myxtn, ?myz-, N ~] mix. ~išn: mixture; element. āmiz [^myc] side dish, vegetables. āmēxtan, āmēz-, read hammóxtan, hammoóz-. Amurdād [?m(w)rdt' | N murdád] Immortality, the sixth Amahraspand, guardian of plants and food; cal. sth month; 7th day. āmurzīdan, āmurz- [mewlc-ytn! | M?mwrz-yd, N ~) forgive, pity, have mercy on. ~išn: mercy, forgiveness. Р amwaštan [h|mwstn! | P ?mwst] gather, collect. an- Pn- | M ’n-] prevocalic privative prefix, un-, -less. ап [ZK < A zk;?n! | M Ап, N ~] that, he. ~ 1: that of; with a qualifier preceding a noun, equivalent to a following 1 e.g. ап i ahlawàn ruwān = ruwan i ahlawān, the souls of the righteous. -ап [2s! | M An N ~] suffix forming (i) present participles, (ii) adverbs, (iii) plurals. ānāb-, —išn, v. ānāftan. an-ābādān Ppp’ rn'] uncultivated. an-abaxšāwand [m ph} wnd] unrepentant. ~ih: unrepentance. an-abāy Pr’ Pd) unfitting, improper. an-abēdān [”7?5yt?x'] useless, unwanted. ~th: uselessness. anübublag [9 fwhlk' = Av. anüpers0a-] inexpiable, unatonable; the highest degree of sin. an-abzār Pwi] unskilled, incapable. ~th: inability. an-ādān [*77:?x!] insolvent. ^h : insolvency. an-ádüg [tk] incapable. an-afsēnišn [”77?syx$n!] indestructible. ānāftan, ānāb- [77ftn',*775- | M ?w pt, Qn m-)] avert, reject, frustrate. ~išn: avoidance, warding off. anág [77 k! | M >ре} evil. ~th: evil, harm. an-ügàh и: | N ndgah] unaware, unwitting. anüg-kardàr [RU АРД, -kunisn [-kwnšn'] evil-doer, maleficent. anagr Pngl) infinite. ~an [”x! | M?nyr^n] Infinite Light; cal. 30th day.
PHD.txt:380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
PHD.txt:392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
PHD.txt:599:u- [AP- < А р | M'w-] = ud (when followed by a suffixed pronoun, e.g. u-š). ud [W < А w | M ?wd, N u] and. udrag (^wdlk! = Av. udra-] otter. ul (LALA < А I-*P | M ?wl] up(wards). ~ āmadan: rise, ~ih: upward direction. ul-āmadān [LALA YATWNPn!',*wl?mt?n") astr. ascendant. *ul-drafš, v. xurdrus. ummēd Pwmyt! | N ~] hope. ~war [-w?/ | N ~] hopeful. Urdwahišt Pertwhst'] = Ardwahist. Urišlīm Pwlyštym | N ~] Jerusalem. urmód Pwlmwt! | (N amród)] pear. *uruspar Pwlwspl = Av. uru0Bar-] intestines, womb; core, essence. urwahm(an) [wig hm(n') | M ?wrw’hm-] joyful. ~ЛЬ : joy, pleasure, delight. urwar Pwlwl | M ?wrwr] plant(s), vegetable.
PHD.txt:859:ascendant ul-āmadān.
PHD.txt:1282:come āmadan, madan; awar!;
PHD.txt:1747:element āmēzišn, rastag, záhag.
PHD.txt:1775:enter andar āmadan | šudan.
PHD.txt:2831:mixing, mixture āmēzišn, gumēzišn, gumēzag(īh), gumēg.
PHD.txt:3457:rise abar āmadan, abar àxistan, ul āmadan.
PHD.txt:5543:dādwar Sy тех dādwarīh xD у мехо Чачап, gādan 19545 āy-! - ot āmadan! VV Wrens jādūgīh AD SAMA jādūg VS MAT jādag-gūwīh A yr SU jadag-gow — SP 5tex5 jadag (EI EI dādmeh +36 ONS dādestān w^ FO) Per
```


## [2026-09-04T19:48:48.699Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'abr-amOn' in p or 'abramOn' in p or 'abr/avr' in p:\n        print('LEAF',i, repr(p[:300]))\n        print('---')\nEOF"
}
```


### [2026-09-04T19:48:50.507Z] TOOL RESULT

```
LEAF 19 '                                            .       tfUJcu^UftiLttU                                                                                                                            --v L^c--,U»-U*jl\n\n\n\n      \\\\/\\6*S -T/IY^ -t-r/fiiS                            (e**.*-Ui)-an                 '
---
LEAF 239 '                                                   U^bo\'j   i$}kl <***•& e-j^\n "\n\n                                                            ahravtar/ahlavtar 5/12   an-ahOg 56/8\n,i   <\\   I.   Tm 25/2          afganSd 228/13\n                                                            ahriman/ahrra'
---
```


## [2026-09-04T19:48:51.217Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== CHEUNG maH ==\"; grep -n -E '\\*maH|\\bmaH1|to measure' CHEUNG.txt | head -20; echo \"== CHEUNG paymu ==\"; grep -n -i 'paymu' CHEUNG.txt | head; echo \"== HRN amudan ==\"; grep -n -i -E 'am[uū]dan|amuten|āmāy' HRN.txt | head -20; echo \"== HUB ==\"; grep -n -i -E 'am[uū]dan|āmūd' HUB.txt | head -20"
}
```


### [2026-09-04T19:48:51.317Z] TOOL RESULT

```
== CHEUNG maH ==
10609:wm’t, s.v. *maH?) 
16225:*CHORESMIAN: ? kcy- ‘to throw (away), put on, to; to dictate’, knd- ‘to measure, 
16898:*maH! ‘to measure’ 
16900:*AVESTAN: mä- (mi-) ‘to measure’ || (+ *ä-) ‘to be ready’ || (+ *fra-) ‘to allow, 
16908:*maHl 255 
16922:stem), BMP ptm’d- /paymäy-/ ‘to measure’ || (+ *pari-) ? MMP prm’y- ‘to 
16933:*PARTHIAN: (+ *pati-) pdm'd- (pret. stem) ‘to measure (against)’ || (+ *pari-) prm’y- 
16945:*KHOTANESE: (+ *apa- ?) LKh. pim- ‘to measure’ (SVK I: 72 f.) = SGS: 83 f. 
16959:256 *maHl 
16984:(Sor.) péw-, Awrom. pimay/pim-, Gz. pääm-/päämä, Khuns. p&im- ‘to measure, 
16994:|| (+ *pati-) Pash. pyamal ‘to measure (as liquids, grain, etc.)’ = pem-/pem(d) (cf. 
16995:Sims-Williams, apud NEVP: 63), Wa. patm(a)y-/patmat- ‘to measure’ || (+ *fra-) 
17005:*SANSKRIT: та ‘to measure’ (RV+) = EWAia П: 341 
17007:«PIE *meH_- ‘to measure’ => LIV: 424 f. | Pok.: 703 f. 
17013:*IE COGNATES: Lat. metior ‘I measure (out), Toch. A me-, B mai- ‘to measure’, 
17025:*maH? ‘to be, become’ 
17046:*mata- or (secondarily formed) *mänta-. It is uncertain whether *maH? can be traced 
18037:Derived from *maH! ‘to measure’. 
25508:*NWIR: NP sanjidan ‘to measure; reflect; compare, put in balance’, (LW) NP linj- ‘to 
55200:*kas', *maH' (s.v.), *sac? 
== CHEUNG paymu ==
== HRN amudan ==
== HUB ==
```


## [2026-09-04T19:48:57.634Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16890,16960p' CHEUNG.txt; echo \"...\"; sed -n '17000,17030p' CHEUNG.txt"
}
```


### [2026-09-04T19:48:57.702Z] TOOL RESULT

```
*IE COGNATES: OCS того (mošti), Lith. mae (magéti) ‘I want, like’, Goth. mag ‘is 


able to, can’, Engl. may, etc. 
*REFERENCES: DKS: 327a; Werba 1997: 434. 


*maH! ‘to measure’ 

*AVESTAN: mä- (mi-) ‘to measure’ || (+ *ä-) ‘to be ready’ || (+ *fra-) ‘to allow, 
permit’ — Liste: 44 

Pres. athem. red.: IND./SUBJ. 2pl. OAv. framima0a (Y 32.4); Caus.: pres. SUBJ. med. 3pl. ҮАУ. 
amaiiante (V 7.36), OPT. med. 3р1. YAv. amaiiaiianta (V 7.37); Partic.: perf. pass. YAv. ämäta- (Yt 
10.122, V 7.39) 


*maHl 255 


*OLD PERSIAN: (+ *fra-) framä- ‘to order, direct’. © The old etymology of OP amata- 
‘noble’ <a-m-a-t-a> (DB 1.7), <a-m-a-ta-> (DBa 11), i.e. an old past participle of 
*à-maH! (cf. Kent: 201b), is best to be discarded, on which see also EWAia I: 95. 
Incidentally, the OP form may be continued in MMP sr-’m’dg’n (pl.) ‘distinguished, 
prominent’ (sr ‘head’), cf. DMMPP: 308b. = Kent: 201b 

MED.; Pres. ja-: impf. IND. 35р. framayata <f-r-a-m-a-y-t-a> (XPg 5); Partic.: perf. pass. (NAsg. n.) 
framatam <[f]-[r]-[m]-a-t-m> (DSf 56) 

*MIDDLE PERSIAN: (+ *4-) MMP *’m’dg ‘prepared, ready’ || (+ *(ä-Juz-) BMP 
'(w)zm'd- /uzmay-/, /azmay-/ (?) ‘to prove, test, try’ || (+ *pati-) MMP pym’d (pret. 
stem), BMP ptm’d- /paymäy-/ ‘to measure’ || (+ *pari-) ? MMP prm’y- ‘to 
contemplate, consider’ || (+ *fra-) MMP prm’y-, BMP plm’(d)y- ‘to order, 
command’ || (+ *ni-) MMP nm’y- ‘to show’ || + *ui-) ? MMP gwm’y- ‘to suffer, 
endure’ (diff. root ?, cf. Skt. ámiva- (Ё) ‘suffering, illness") > DMMPP: 36b, 289b, 
279a, 156a, 243a f., 167a 

(+ *(a-)uz-) Pres.: IND. 3sg. ВМР ’wzm’(d)t /uzmayéd/; Inf: BMP ’wzmwtn /uzmüdan/; Partic.: perf. 
pass. ВМР ’wzmwt /uzmüd/ || (+ *pati-) Pres.: IND. 3р1. BMP ptm’dynd /paymayénd/; Partic.: perf. pass. 
MMP pym’d || (+ *pari-) Pres.: IND. 3sg. MMP prm’yd; Perf. pass.: perf. pass. MMP prm’d || (+ *fra-) 
Pres.: IND. 1sg. BMP plm’ym /framayem/, 3sg. MMP prm’yd, etc. || (+ *ni-) Pres.: IND. 3sg. MMP 
Dm vd nm’yyd, SUBJ. 15р. MMP nm’y’n, IMPV. Zeg. MMP nm y; Partic.: perf. pass. MMP nmwd 
*PARTHIAN: (+ *pati-) pdm'd- (pret. stem) ‘to measure (against)’ || (+ *pari-) prm’y- 
‘to contemplate, consider, believe’ || (+ *fra-) frm’y- ‘to order’ || (+ *ni-) nm’y- ‘to 
show’ || (+ *ui-) wm’y- ‘to experience, endure’ (diff. root ?, cf. Skt. amiva- (Е) 
‘suffering, illness’) — Ghilain: 86 f. | DMMPP: 269b, 279a, 156a, 243a, 342b 

(+ *pati-) Partic.: perf. pass. pdm'd, pdm’dg; Inf.: pdm’dn || (+ *pari-) Pres.: IND. 1sg. prm’y’m, 2sg. 
“prm’yh, 3sg. prm’yd, 3р1. “prm’ynd, SUBJ. 2sg. prm’y’h, 3sg. prm’y’h; Partic.: perf. pass. prm'd || (+ 
*fra-) Pres.: IND. 3sg. prm’yd, SUBJ. 3sg. frm’y’h, IMPV. 25р. frm’y; Partic.: perf. pass. frm’d; Inf.: 
prm’dn || (+ *ni-) Pres.: IND. 3sg. nm’yd, 3р1. "nm’ynd, nm’yynd, SUBJ. 1sg. nm’y’n, IMPV. 2pl. 
nm vd Partic.: perf. pass. nm’d; Inf.: nm’d || (+ *ui-) Pres.: IND. 3pl. wm’yynd {unpubl.}; Partic.: perf. 
pass. wm’d 

*KHOTANESE: (+ *apa- ?) LKh. pim- ‘to measure’ (SVK I: 72 f.) = SGS: 83 f. 
*SOGDIAN: (+ *api-ä-) ? SSogd. py’m-, CSogd. py’m- ‘to heal, cure’, CSogd. pyms- 
(pass./inch.) ‘to be healed’ || (+ *a-) BSogd. ’’m’-, CSogd. ’m’- ‘to prepare’ || (+ 
*uz-) SSogd. zm’, CSogd. zm’y ‘to tempt’ || (+ *pati-) BSogd. ptm’k, ptm’’k, 
ptm’ky, CSogd. ptm’q ‘measure’, BSogd. ptm’t’y ‘measured, frugal’ || (+ *pari-) 
CSogd. prm'qycq ‘experience’, BSogd. m’ny-prm’t’y ‘thought, intention’ || (+ *fra-) 
SSogd. prm’y, BSogd. prm’(’)y, CSogd. frm’y, MSogd. frm’y ‘to command, say’, || 
(+ *ni-) SSogd. nm’y, CSogd. nm’y, MSogd. nm’y ‘to judge’. Ф Also attested 15 the 
nominal deverbative, BSogd. ’’m’n ‘power, authority’ (Vim 140), which is perhaps 
secondary: it does not agree with the assumed verbal forms in meaning, BSogd. 
”m’-, CSogd. ’m’-). It seems to be formed after the noun, CSogd., MSogd. frm’n 
(corresponding to SSogd. prm’y, etc.). 


256 *maHl 

...
Sh. (Baj.) rimi(y)-/rimöd, Rosh. rimay-/rimüd, Bart. rimiy-, rimay-/rimöd, Sarig. 
rimey-/rimud, Yzgh. Xamay-, Wa. rom(o)y-/romot- ‘to command, order; to send’ 
*MISC: (+ *uz-) Orm. izmaw-, wuzmaw~ék ‘to try, test? = ázmaw-/ázmawók (etc.) || 
(+ *pari-) Arm. (LW) parmayel ‘to test’ 

*SANSKRIT: та ‘to measure’ (RV+) = EWAia П: 341 

«PIE *meH_- ‘to measure’ => LIV: 424 f. | Pok.: 703 f. 


*maié (mac) ? 257 


*IE COGNATES: Lat. metior ‘I measure (out), Toch. A me-, B mai- ‘to measure’, 


Goth. mel ‘time, hour’, OHG mal ‘moment’, Russ. méra ‘measure’, etc. 

*REFERENCES: IIFL I: 388b; Christensen, Contributions I: 70, 168; Christensen, Contributions II: 59, 116, 
160; IIFL II: 537a; Abrahamian 1936: 113; Lambton 1938: 78a; Abaev, Slovar’ I: 49; Andreev — 
PeSéereva: 251b; MacKenzie 1966: 104, 94; Abaev, Slovar’ П: 199 Ё; EVS: 62, 67b; WIM I: 71; WIM 
II/1: 80 f., 85; Asatrian — Livshits: 82; Cabolov 1997: 72; Werba 1997: 310 Ё; Steblin-Kamenskij 1999: 
281, 301; Cheung 2002: 209; Lecoq 2002: Kiefer 2003: 192 


*maH? ‘to be, become’ 

*KHOTANESE: (+ *fra-) hämä- ‘to be, become’ = SGS: 152 

*SOGDIAN: SSogd. m’t, CSogd. m’t (pret. stem) ‘to be’ || (+ *a-) SSogd. "m- ‘to 
come to’ || (+ *ui-) SSogd. wm’-, BSogd. wm’- ‘to be(come)’ (supplet. past stem of
```


## [2026-09-04T19:48:59.484Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN grep amu ==\"; grep -n -E 'āmū|amū|amud|āmud' HRN.txt | head -30; echo \"== HRN gohar ==\"; grep -n -i 'gauhar\\|gohar' HRN.txt | head -10; echo \"== HUB amu ==\"; grep -n -E 'āmū|amū|amud' HUB.txt | head -20"
}
```


### [2026-09-04T19:48:59.575Z] TOOL RESULT

```
== HRN grep amu ==
== HRN gohar ==
== HUB amu ==
9787:LW. namud 'index, guide, show*, namuddr~ 273 -
```


## [2026-09-04T19:49:26.306Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16960,17000p' CHEUNG.txt; echo \"=== HRN sample ===\"; head -c 600 HRN.txt; echo; echo \"=== HRN lines with 'füllen' ===\"; grep -n -i 'füllen\\|fullen' HRN.txt | head -20"
}
```


### [2026-09-04T19:49:26.387Z] TOOL RESULT

```
(+ *api-ä-) Pres.: SUBJ. 159. SSogd. py’m’n, POT.-SUBJ. 15р. tr. SSogd. py’mtw Куп п, IMPV. 2pl. 
SSogd. py mó; Fut.: IND. 3sg. CSogd. py’mtq’; Pret.: tr. IND. 3sg. SSogd. py’mtw ó rt; Inch.: pres. OPT. 
3sg. CSogd. pymsy; Partic.: pres. MSogd. py’mnyy, perf. pass. SSogd. py mt °, CSogd. *py’m’tyt (pl.), 
CSogd. (f.) “py’m’c ‘cured’ || (+ *4-) Partic.: perf. pass. BSogd. ’’m’t’y, CSogd. "mit, CSogd. ’m’c (Е) 
‘ready, prepared’ || (+ *uz-) Pres.: IND. 3pl. CSogd. zm’ynt, Perf.: tr. IND. 3sg. SSogd. хт? ö’rt, Partic.: 
perf. pass. CSogd. zm’yty ‘tempted’ || (+ *fra-) Well attested: Pres.: IND. 2sg. SSogd. prm’y, CSogd. 
frmy, 3sg. BSogd. prm "yt, dur. 35р. SSogd. prm’ytskwn, CSogd. frmytg, etc. || (+ *ni-) Pres.: IND. 15р. 
dur. CSogd. nm’ymsqn; Impf.: IND. 3sg. MSogd. nym’y; Fut.: IND. 1sg. CSogd. nm’yngq’; Inf.: SSogd. 
prnm’y 

*CHORESMIAN: (+ *pati-) рсту- “о weigh, measure’ || (+ *fra-) sm’- ‘to order, turn 
(into). © Samadi apparently reconstructs on the basis of the subj. forms a stem 
Sm'h-, which she derives from *fra-mä-h(a)-. This can be discarded, not only 
because an intervocalic *h has regularly disappeared in Chor., but also because the 
appearance of -h- in the subj. seems to be intrusive in origin, viz. probably from the 
subj. (3sg.) y’h’c of y- ‘to be’ (s.v. *Hah). = Samadi: 142, 153, 195 

*BACTRIAN: (+ *fra-) ọpopa- ‘to order, command’ = S-W, Bact.: 230b 

*NWIR: (+ *4-) NP ämädan/amäy- ‘to prepare’ || (+ *a- + *uz-) NP azmüdan/azmay- 
‘to try, test, prove, tempt’, NP 4zmudan/azmay-, Gz. uzn-/uznä ‘to try, test, prove, 
tempt’ || (+ *pati-) NP paymüdan/paymäy-, Kurd. (Kurm.) pivin/piv-, payvin, pivan, 
(Sor.) péw-, Awrom. pimay/pim-, Gz. pääm-/päämä, Khuns. p&im- ‘to measure, 
traverse’ || (+ *pari-) NP parmäsidan ‘to know’ || (+ *fra-) NP farmudan/farmay- ‘to 
order, command; [in polite address] to say’, Awrom. farmaway/farmaw- ‘to order, 
deign’, Fariz. bäfärmä ‘order !’, Gil. (Rsht.) farmoestoen/farmaj-, Ham. färmayän/ 
färmon-, Jow. ba-farma:niya, Sang. -farmij-/farmoen-, Shamerz. -farmim-/farmam-, 
Sorkh. -farm-/farma- ‘to order’, NP farman ‘order, command, decree’, Tal. hamue 
‘to order, command’ || (+ *ni-) NP nimäy-/nimüdan ‘to appear, show’, Kurd. (Sor.) 
niwen-, Awrom. nimana, (sec. caus.) Gz. numn-/numnä ‘to show’ 

*NEIR: (+ *a-) Oss. I. amajyn/amad, D. amajun/amad ‘to build up (a wall, logs, etc.) 
|| (+ *pati-) Pash. pyamal ‘to measure (as liquids, grain, etc.)’ = pem-/pem(d) (cf. 
Sims-Williams, apud NEVP: 63), Wa. patm(a)y-/patmat- ‘to measure’ || (+ *fra-) 
Yghn. farmóy-/farmóyta ‘to order, command, wish’, Ishk. ferma(y)-, Sangl. farmé-, 
Sh. (Baj.) rimi(y)-/rimöd, Rosh. rimay-/rimüd, Bart. rimiy-, rimay-/rimöd, Sarig. 
rimey-/rimud, Yzgh. Xamay-, Wa. ram(a)y-/ramat- ‘to command, order; to send’ || (+ 
*ni-) Oss. I. nymajyn/nymad, D. nimajun/nimad ‘to count, value, esteem; to read’, 
Sh. (Baj.) rimi(y)-/rimöd, Rosh. rimay-/rimüd, Bart. rimiy-, rimay-/rimöd, Sarig. 
=== HRN sample ===
Google
This is a digital copy of a book that was prcscrvod for gcncrations on library shclvcs bcforc it was carcfully scannod by Google as pari of a projcct
to make the world's books discoverablc online.
It has survived long enough for the Copyright to expire and the book to enter the public domain. A public domain book is one that was never subject
to Copyright or whose legal Copyright term has expired. Whether a book is in the public domain may vary country to country. Public domain books
are our gateways to the past, representing a wealth of history, cultuie and knowledge that's often diffi
=== HRN lines with 'füllen' ===
788:41. ägenden 'anfüllen', ägenis^ ägm 'voll'.
1304:einfüllen, auffüllen zu sein, vergl. AM. 82 Zeile 1 *in
1305:die Harnröhre einführen, einfüllen , 145 Zeile 3 v. u.
1306:'in die Nase einführen, einfüllen* u. ö. (mit und ohne
1310:Die Bedeutung auffüllen findet sich dagegen noch in
1311:htm efgenden 'das Fundament auffüllen, den Grund
1317:Efgenden 'einfüllen, auffüllen' wird zu np. ägenden
1384:111. enhästen^) 'anfüllen, anhäufen', Praes. enbär-em,
1569:132. öbäSten anfüllen; verschlingen (d. i. sich anfüllen)*
1572:ap. *6l^;a -f l/'^)ar- (vergl. skr. avapürna") anfüllen';
6127:knüpfung an l^par- ausfüllen* besser.
```


## [2026-09-04T19:49:26.718Z] TOOL CALL #13: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-04T19:49:26.765Z] TOOL RESULT

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


## [2026-09-04T19:49:37.259Z] TOOL CALL #14: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-04T19:49:37.267Z] TOOL RESULT

```


```


## [2026-09-04T19:49:39.268Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SNS.txt around 1967 ==\"; sed -n '1955,1985p' SNS.txt; echo \"== SNS scans entry ==\"; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['SNS'].get('scans'),ensure_ascii=False,indent=1))\""
}
```


### [2026-09-04T19:49:40.899Z] TOOL RESULT

```
== SNS.txt around 1967 ==

: \****> I* tjax" .^^^j/i Uiftfc.l56)ayagh- i I*- 

\Y-\fi/\&£ {GIrPh. 14) hesin, hasin sj^ *j*1 
fjJV^W -J->o* T : ahandil (>*-+) : i^cfjj^ "*V 

•j^**' 'j** 1 s ahunavar-ahuvar i 

■6/11** ft 



: lJ i** abr-amOn t ^-JS^ j .aj^T^Uji. U *** .a-i^JT^l^L L«** 

h'rayn :^k {AiWb . 1809) hamina- , hami: fc» 
W/1A --S (ij6.y~»J hamln :L {Mir. Man. I. 39) 

*S *J o= ^U^* jl ^ r U >j , .^j.oU.^: ax v /ah v : t^ 
.•<?/]„ 3 -b-f-X/? <* UiM>- 106.) aghu-.ahu- : fc- 

i i/ia ^ -tr-t/yr ^ 

j**,. ^L l** : ax v I astCraand : jXT^i*^ »*>* 
(•j^o*** •«&) tf**> : ast5mand + -U -j/^j ax v : ^iU-* 



.jjuU.*,^: havind/havand i 



== SNS scans entry ==
null
```


## [2026-09-04T19:49:48.714Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nprint('NPAGES',len(p))\nfor i in (17,18,19,20):\n    print('=========== LEAF',i)\n    print(p[i][:1800])\nEOF"
}
```


### [2026-09-04T19:49:50.174Z] TOOL RESULT

```
NPAGES 243
=========== LEAF 17
                                              LiJ ttaayU 4*L ify                                                                                     <[ZJ C^-*U i-Ls^lj




     ^U.jL-^j^j^^^lMku^ff^o^j^'^^* axtarlg **V"                           1                             ^T^UjIj^^o^) ^L^yk- lyT^^T^I^^jj .c-l^^l^ a-(f)




        .   (li-Nj^ j5^l^*L i/a W c^*L.t                     r U/)    .   jji^ fv«jLi (.ty.)                                                  ^ii,^ L-jioi^^cUbUwift                    hat      yt^u*       i




                                                                                                        3 1 jjS .   uU ««v^
                                                                                                                       .           ,j*«« *-
                                                                                                                                              "   ^Ul « Ia « iSfhi j J   s3ti- ^yS-i-hati- 1-

                                                                                                        The Religious Ceremonies and Customs'-^ •^— J-^t                                  x




                                                                                                        _^_a_l/^r^ -?/\o£ of the Persees, by Modi P. 266
                                                                                                                                                                                   •   tT-rf-n
      Caiman-          jl   ^U f£**fyAiWb                    .    310.( o ^) axs-      |




\-                                                                                                      (TO ^lirVt&tS^'-^L.&i.Jj&jijijL .Jj'j^'obhaxt V**-*                      
=========== LEAF 18
                                                                                         'J')
                                                                                                                                                                                                                                                          V
                                                                                                                                                                                            f
                                                                                                                                                                                                Ui c-,1: *-L*3lj

                                        •
                                            Ji/\r            £    \r-\\/\*s -^U <f~jb^ p>r^\^

                                                                                                                                           t>i*0' : *&      .   c*#iU i |.Uilj- i^^u                      pas-iz, ^HR, yz                           •>&      O**o»
                                       .^il .y-jJu                LjL .j^ftl .:ahrav/ahlav                                  ytW
     asavay            1*   asSg            *j'^ j-ati* iSf^H oy* j J *3'.j cw' isW** « •=—' »^-i-s


                                                                                                                                            •
                                                                                                                                                tfiMHifMi*                    1     ahraglh/ahlaylh/ahraylh                                    :     -<o -*&*_y
 6       (M.F.        .rtavan 
=========== LEAF 19
                                            .       tfUJcu^UftiLttU                                                                                                                            --v L^c--,U»-U*jl



      \\/\6*S -T/IY^ -t-r/fiiS                            (e**.*-Ui)-an                         +   (   u I**   .
                                                                                                                    ^^           |



                                                                                                                                                                                                                                                    •rri
                                                                                                                                           •
                                                                                                                                               M-IV/T^ ham                            :L(4tl/b.           1773)sam :Lham-               :    4_ui    *   fc*,



     -ah§xt cJuaU ahania, ahan5ldan                                                 :   ^ a-hag5                        i
                                                                                                                                **•


     1Y/1Y^             r-'^l^)-isn+ (Pers. Stud. 10)
                       (,,*-.                            *-*-*'                                                                                                               ,
                                                                                                                                                                                  tf Ujbiloo=-S .          jJ^i
=========== LEAF 20
                                                                                                                                                                                           j




                                       bjA^UtebtjIj                                                                                                        r
                                                                                                                                                               Urf.«~rik*b*ilj



                                                                                                       ^ A   j'-vcj)       hvfls-               *(»* ** 16 Jh***j) hvanta-                                               :   &•

                                                                                 fr/T ^                 \/A* f ->>>-.; ha vafid :V(Kapadia                                                 'WV^)(TI
     r
         iT U-b                                                                                                                                                                                               •   r«/iT -^


                                                                                                       .^) .0.»># d Uhrj         ^      .oaI-: ^aiiU <iS*!>*                          :h5vandlh: -*u*W>
                                                                                                                                                                                           VA^                    (*Uo'>                    6
           x§z :>;t    {GNPE. 102)xaSzanuha-haSz                              ^j ;.^     1




              \X/\Y^ ax§z: V (yW y. 178) xist                            :    o T *r*L**li
```


## [2026-09-04T19:50:01.470Z] TOOL CALL #17: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%85%D9%88%D8%AF%D9%86",
 "prompt": "Give the full Persian entry for آمودن (āmūdan): etymology, Middle Persian antecedent, present stem, meanings, and any related-terms/derived-terms sections. Quote the etymology verbatim."
}
```


## [2026-09-04T19:50:02.257Z] TOOL CALL #18: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/admiral",
 "prompt": "Quote the full etymology entry for 'admiral' verbatim, including the Arabic amir al-bahr discussion and the -d- explanation."
}
```


### [2026-09-04T19:50:03.445Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T19:50:08.388Z] TOOL RESULT

```
# Etymology of Admiral

The entry states that "admiral" comes from Old French *amiral* and medieval Arabic *amir* meaning "military commander." The word originally referred to Saracen commanders before shifting to naval officers by the 15c.

Regarding the Arabic origin, the text notes: "As *amīr* is constantly followed by *-al-* in all such titles, *amīr-al-* was naturally assumed by Christian writers as a substantive word."

On the unetymological *-d-*, the entry explains: "The unetymological *-d-* probably is from influence of Latin *ad-mirabilis*" (relating to the word "admire").

The Romance language forms show confusion with Arabic: "Italian form *almiraglio*, Spanish *almirante* are from confusion with Arabic words in *al-*."
```


## [2026-09-04T19:50:10.910Z] TOOL CALL #19: WebSearch

```json
{
 "query": "آمودن āmūdan Persian etymology \"to fill\" Middle Persian"
}
```


### [2026-09-04T19:50:12.459Z] TOOL RESULT

```
Web search results for query: "آمودن āmūdan Persian etymology "to fill" Middle Persian"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T19:50:13.558Z] TOOL CALL #20: Bash

```json
{
 "command": "curl -s -L -o /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/sns_n19.jpg \"https://archive.org/download/VajnameShayest/page/n19_w1200.jpg\" -w '%{http_code} %{content_type} %{size_download}\\n'"
}
```


### [2026-09-04T19:50:18.381Z] TOOL RESULT

```
200 image/jpeg 122906
```


## [2026-09-04T19:50:21.615Z] TOOL CALL #21: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/sns_n19.jpg"
}
```


### [2026-09-04T19:50:21.633Z] TOOL RESULT

```

```


## [2026-09-04T19:50:23.201Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%85%D8%A7%D8%AF%D9%86",
 "prompt": "Full entry for Persian آمادن / آماده — etymology, Middle Persian form, Proto-Iranian root. Quote verbatim."
}
```


### [2026-09-04T19:50:30.060Z] TOOL RESULT

```
# Persian آمادن (āmādan)

## Etymology 1: "To Prepare"

The word derives from **Proto-Iranian *āmaH-**, composed of *ā-* + *maH-* ("to measure"). This traces back through Proto-Indo-Iranian *maH-* to Proto-Indo-European *h₂éd* ("at") + *meh₁-* ("to measure").

Related terms include the adjective آماده (âmâde, "ready") and cognates across Indo-European languages: Avestan āmāta-, Sanskrit माति (māti, "measure, knowledge"), and Ancient Greek μῆτις (mêtis, "skill, counsel, plan").

## Etymology 2: Dialectal "To Come"

The entry notes this etymology requires completion. It identifies this as a **dialectal form of آمدن (âmadan, "to come")** used in Herati speech (Western Dari).

## Pronunciation Note

The word is pronounced /ʔaː.maː.ˈdan/ in Classical Persian, with regional variations across Dari, Iranian, and Tajik dialects.
```


## [2026-09-04T19:51:00.079Z] TOOL CALL #23: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/SNS && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/SNS/6.vision.txt <<'EOF'\n[SNS = Tavoosi, Vazhe-name-ye Shayast ne Shayast, printed p. 6 = archive.org VajnameShayest leaf n19 (right-hand page of the image, numbered ۶); transcribed from the page image by hand, 2026-09-04]\n\n<pahlavi> [درمتن ۱۱ ...]  āmōn :  آمون، پر، مملو، لبالب (پر لبالب) در فرهنگ\nجهانگیری آمده. «آمو (و آمون) بمعنی پر کرده بود» و آمود و آموده نیز بهمین\nمعنی است. سنایی: هم زبانشان ز فحش آموده. هم درونشان به خبث آلوده.\nهمه با پایهای آلوده. همه با مغزهای آموده. و ترکیب: abr-āmōn یعنی:\nپر ابر، ابری. ک ۱۰/۲\n\n(same page, other entries: hām-bun-iz «حتی‌کمی، کمترین اندازه‌ای»؛\nham- : sam (AiWb. 1773) ham ...؛ hāmīn : هامین، تابستان ...؛\naxᵛ/ahᵛ : هستی، حیات، زندگی ...؛ axᵛ ī astōmand : جهان مادی، وجود جسمانی ...؛\naxᵛān/ahvān : هستی‌ها، زندگی‌ها، جهان‌ها)\n\n[facing page 7 has: āhanjišn, āhanžā/āhanjīdan, hāvišt, hāvištān, xānag,\nāhēn/āhan, āhandil, ahunavar-ahuvar, hāvind/hāvand]\nEOF\necho written"
}
```


## [2026-09-04T19:51:01.284Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BQT v1 آمودن ==\"; grep -n 'آمودن\\|آموده\\|گوهرآمود\\|آمون' BQT_v1_pages.txt | head -20; echo \"== MON part1 ==\"; grep -n 'آمودن\\|گوهرآمود\\|آمون' MON_part1.txt MON_part2.txt | head -20"
}
```


### [2026-09-04T19:51:01.945Z] TOOL RESULT

```
written
```


### [2026-09-04T19:51:02.014Z] TOOL RESULT

```
== BQT v1 آمودن ==
8778:آمون‌است وآن رودخانه‌ای باشدمشهور وممروف.
8792:آمودن بروزن آسودن . بمعنی
8814:او بلخ بود بنا دهاد . » ۱ - منظرر شهری بمازسران است .آموده ۰ 7۳۳
8817:آموده ۴ « پروزن آسوده » لمل و
8831:آمون ‌ ب‌وذن حامون ؛ زودست که
8839:۲ مو یه - بنتح تحنانی ؛ بمعنی آمون
8854:۱ - چواز رودآمونگذشت آنسپاه برآعد هیاهو زماهی‌بماه . هانفی «لفت‌نامه*.
8855:۷ رکه : آمو. ۸ - رکه : آمودن.
18781:است که اطراف و پیرآمون دهان باشد ۷ .
24704:پیرآمون کسی
25107:«اسشق ۳۰4 و «ینیری واره» مر کیت از : هنیری دیشو ند ( پیرآمون ) - واره لژمستر ۷۵۲
31051:۳3 دثب و آمودن‌باش وتن‌زن, نن‌زده(۳) خاموش
32126:تبری انداخت» آن کیرش کار اب آمون؟ افتاد
== MON part1 ==
MON_part1.txt:4609:امادن؛ 2102-7 [قس. آمودن] (مسصع.) 
MON_part1.txt:4799:آمودن: 2۳01-27 [قس. آمادن] (مسصم.) 
MON_part1.txt:4831:آمونیاک: (ا.) ( سیم .) گازی است 
MON_part1.txt:4842:ترکسات آمونباک مسجموعه بنام 
MON_part1.txt:4843:آمونیوم دارای خواصی شبه به خواص 
MON_part1.txt:4845:آمونیاک» کلرور آمونیوم با نوشادر است که 
MON_part1.txt:28149:بقایای فسیل شد؛ گونه‌ای از آمونیت‌ها را از 
MON_part1.txt:44840:مجاورت آمونیاک و کرینات و پتاس ایجاد 
MON_part1.txt:66472:بارو. بیرآمون شهر گرداگرد. روده. آنجه 
MON_part1.txt:81404:و آمونیم همه سولفورها غیرمحلول‌اند. 
MON_part2.txt:7344:فسفات سدیم و پتاسیم و آمونیم در آب 
MON_part2.txt:7349:آمونيااک هر دو حل می‌شود. 
MON_part2.txt:13379:اسیدهای مختلف و گاز آمونیاک همراه 
MON_part2.txt:30300:ببرآمون دایره. اجزای 1 ِِ از : دقمقه 
MON_part2.txt:50230:ایشان می پرداختند. مآمون به سال ۲۱۸ ه.ق 
MON_part2.txt:69418:اجساد مستحجر شدهة آمونت‌ها که در 
MON_part2.txt:79543:پتاسیم و آمونیوم که در آب حل می‌شوند 
MON_part2.txt:79548:کربنات‌های سدیم و پتاسیم و آمونیوم 
MON_part2.txt:82168:سولفور آمونیوم ۹0۷۲1۳(۲ رسوب سیاه 
MON_part2.txt:82176:سولفات مضاعف نیکل و آمونیوم
```


## [2026-09-04T19:51:09.920Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nimport re\nfor i,pg in enumerate(p):\n    if 'آمودن' in pg and 'آموده' in pg:\n        print('LEAF',i)\n        print(pg[:2500])\n        print('==========')\nEOF"
}
```


## [2026-09-04T19:51:10.148Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4790,4835p' MON_part1.txt; echo \"---- amadan ----\"; sed -n '4600,4625p' MON_part1.txt"
}
```


### [2026-09-04T19:51:12.001Z] TOOL RESULT

```
LEAF 272
آموده ۰ 7۳۳
و آ یخته‌شدن - وساختن و ساخته گردانبدن٩‏ ۹
و پر کردن و مملو ساختن باشد .
آموده ۴ « پروزن آسوده » لمل و
مروارید و امثال آن را گوبند. که در رشته کشیده
شده باشد - ویمعنی‌پر کرده ومملوساخته‌هم‌هست-
و آراسته و بسراسته را یز کوبند. وترجمه‌لفظی
است که در عربی«مندرج خواند» .#
۱ ]موز گار ۴ ‌ باکاف فارسی. آموزنده
و آموزاننده را کویند که معلم و استاد باشد .
| هو سئی - بسکون‌ین بی‌نقطم و کس
نون و تحتانی ساکن » دو زن با بیشتر که يك
شوهر داشته باشند عربك مردیگررا «آموستی»
بائد ۴ ,
آمولن * - بنتح لام و سکون نون .
بونانی نگاسته را گونند که از آن بالوده و
آ هار پز ند .
آمون ‌ ب‌وذن حامون ؛ زودست که
ب رکنار خوارزم گنرد ؛ و میان تر کستان و
خراسان واقم است ۱ - و بمعنی پر و مملو و
لالب و لبریز هم هست .
موی ۰۲ بسکون بای حطی , دام
شهریست بر کذلر جیحون و جیحون منسوب‌باآن
شهراست - و بمعنی پر کردن و عملو ساختن -
و امر باین ععنی - و فاعل هم آعده است ۸ .
۲ مو یه - بنتح تحنانی ؛ بمعنی آمون
است و آن رووخانه ای باشد مشهور ۷ .
۱ هه .» بروزن نامه ۰ یمعی دوات
نوسندکی باشد ٩‏ - و توده و پشتٌ هیزمرا نیز
کنته اند ۷۰. «
آمیز ۷۱ بروزن کاریز» بمعنیآميزش
و مباشرت و جماع باشد - و امیختن دو چیز
با زباده بهم را نیز گوبند؟۹.
.* کرانمایه سیاهی داشت فرمود  باستقبال شهزاده بآمود. قضرالدین ابوالعملی < لفت‌نامه‎ - ٩
۳ ره : آعودن ۳ ۷ بهلوی 327( (آمو ز گاری طر م20۵2 ۱
د ما۲۹ : ۰۲ . ۴ در لت فری (س۲۳ه) بل « وسنی » آمده : « زني باشد
که برسر زن خواهند. » و در لهج کنابادی ۷۵5 , ۷851 بدینمعنی است ولی د: گیلکی
کتونی 2۷۵81 گوند . صور میرودکه کلمةٌ مسحف « آوسنی * است .
8 - 2001100 , 10۷0105 - 8 بوبانی آردی که بادست ( نه‌آسیا) نهیه شده باشد
« فرهنکه بونانی - انگلیی . لدل واسکات ۸٩‏ 4.
۱ - چواز رودآمونگذشت آنسپاه برآعد هیاهو زماهی‌بماه . هانفی «لفت‌نامه*.
۷ رکه : آمو. ۸ - رکه : آمودن.
٩‏ - ای ترا تبك آمه. نی خامه لوح‌نمليم نختهُ نرد است. طرطری «لغت‌نامه».
۶- رکه : آحنه , وشاید مکی از این دوحصحف دبگری است «لفت نامه* .
۱ ۱ - عمریثه آمیغ. پهلوی وارمنی 20016 ( غذای چاشنی‌زده «راکو» ) «اونوالا۰۳۰۳
م رکب از: 016-2 , بونانی ۲01802 ( آعیخته ). لانینی10350072 و 101560۳2 آمیختن.
رط۳ در کلمات‌م رکب گاه بممنی [میز نده باشد چون : حردم آهیز : و گله نمی آعخته
چون : شهد آمبز . « لت نامه »
۵ آموزش - پهلوی علاکنت8200۵2 « منای ۲۹۵ : ۲ » , عملآموختن ؛ تعلیم :
باید خرد شاه را نا گزبر هم آموزش مرد برنا وییر . فردوسی < لفت‌نامه *.
» آمیخته - پپلوی 27067181 « منای۲:۲۹۵ بمعنی درهم کرده: مخلوط»ممزوح:
تلخی وشیر نش آمیخته است ‏ کی‌نخورد نوش وشکر بآپبون . . رودکی < لفت‌نامه *.
==========
```


### [2026-09-04T19:51:12.057Z] TOOL RESULT

```
تس اتاصة (.) اشتان مرغان شکاری 
مانند باز ر عقاب» آشیانه. 
آموختگار: 20010 (ص‌فا.) معتاد به» 
چشته خور» سته‌خوار. 
اموختن: محا-ستنعة ( آموخت» آموزده 
خواهد اموخت. ساموزء آموزنده. آموخته. 
آموزش). (مصل.) فرا گرفتن» یاد گرفن» 
تعلم. (مسصم.) فرا یاد دادن تعلیم» 
آموزاندن. 
آمودن: 2۳01-27 [قس. آمادن] (مسصم.) 
آمیختن» درهم کردن. . ترصیع» در نشاندن 
چنانکه گوهری را در انگشتری. به سلکك 
درآوردن؛ به نخ کشیدن گوهرها و مهره‌ها. 
آراستن» زشت کردن. سهیا کردن» آماده 
کردن. (مصل.) آميخته شدن. آراسته شدن. 
امو زانیدن: مدلآصعتاهة [- آموزاندن < 
قس. آموختن] (مسصم ِ( تسعلیم دادن 
آموختن. 
آمسوزش: 27024 (اسص. آموزیدن و 
آموختن) عمل آموختن» یاد دادن. تعلیم) 
مق. ترییت» پرورش. 
آموزشگاه: 2.0 (امر.) مدرسه (فره.) 
آمتو ره : 1-.8 (ص‌نسس..) منصوب به 
آموزش. تعلیمی» تعلیماتی. طالب علم؛ 
دوسند ز آموختن. 
آموزگار: ۲-(30102)6 (ص‌شغد.) آنکه 
آموزد» آنکه باد دهد» معلم آموزنده. (فر.) 
معلم مدرسةٌ ابتدایسی. سامح اندرزگوی. 
راهنما؛ هادی. شاک د) مت 
آموز رنده: (6-)202-2002 را آمو حتن» 


۳ فرهنگ فارسی معين 1 


آموزیدن) آنکه به دیگری آموزده آنکه 
تعلیم دهد معلم. آنکه از دیگری آموزد» 
آمو ۵ 27010107 [معر .] (ا.) نشاسته» نشا. 
امون: 2 (ص.) بر » مملو» لبالب. 


آمونیاک: (ا.) ( سیم .) گازی است 


بی‌رنگ با بوی تند و طعم حاد و اشکث آور 
است و در آب حل می‌شوده آن یکی از 
---- amadan ----


آمادگی: 20028036-1 (حامص. آماده) آماده 


آمادن 


بودن. (.) تهیه» بسیج» ساز) استعداد. 
امادن؛ 2102-7 [قس. آمودن] (مسصع.) 
ساختن» سیجدن) آماده کر دن. سر کتودن؛ 
فهلی کرداندن هقی لها شدن. آماده 
شدن. 

آماده: (۵-) 2015-1۸ (امقش. آمادن) حاضر» 
مهیا؛ مستعد. (بناء) گچی روانتر از بوم. (ور.) 
هنکام شروع مسابقه» داور بس از د کر 
«بجای خود) ( آماده» گو ید و سیس با شلبکت 
تير یا دمیدن در سوت مساقه رو 
می‌شو د. . که بجای آماده «حاضر؛ گویند. 
آماده نودن: مهبا بودن» مستعد بودن. 

آمار؛ ۲ (- آماره - امار - اماره] (.) 
حساب؛ شمار. استقصاء پی‌جویی» تتبع. 
علمی که موضوع آن طبقه‌بندی علمی وقایم 
اجتماعی است ۴ مبنای آن محاسیبه و شان
```


## [2026-09-04T19:51:38.864Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD abr / amon ==\"; grep -n -o -E \"abr \\[[^]]*\\][^.]*\\.|āmōn[^.]*\\.|amōn\" PHD.txt PHD_mackenzie.txt | head -20; echo \"== NYB ==\"; grep -n -i -E \"abr-āmōn|āmōn|'mwn\" NYB_vol2_glossary.txt | head -20; echo \"== PHD grep abr line ==\"; grep -n -c 'abr' PHD.txt"
}
```


### [2026-09-04T19:51:38.941Z] TOOL RESULT

```
== PHD abr / amon ==
PHD.txt:230:abr [bpl | N ~] tiger.
PHD.txt:306:abr [dpi] sinner, deceiver.
PHD.txt:306:abr [dpl] *dark-coloured.
PHD.txt:376:abr [gpl, gwbl | M gbr, N ? gór] hollow, cavity, womb.
PHD.txt:570:abr [stpl | M stbr, N sitabr] big, coarse, strong.
PHD_mackenzie.txt:813:abr [lbl, 'pl I N -] cloud.
PHD_mackenzie.txt:1449:abr [bpl IN ......] tiger.
PHD_mackenzie.txt:1809:abr [dpl] sinner, deceiver.
PHD_mackenzie.txt:1810:abr [dpl] ·dark-coloured.
PHD_mackenzie.txt:2411:abr [gpl, gwbll M gbr, N ? gar] hollow, cavity, womb.
PHD_mackenzie.txt:4656:abr [stpl' M <stbr, Nsitabr] big, coarse, strong.
== NYB ==
3117:pērāmēn [pyl'mwn', pylmwn'] 1. adv. all about 3923, 935, 9623. 9817, 2. prep. round about, with the izafat, 119. 8722, 8912; referring back to an encl. pron.: 7 déh 4-4 ~ nisast hend 471°, api-š ... girtak (g. v.) ~ xtarrah āyēt and all around it, 9218-19, — < *pari-yāma-van-, derived from "pari-ydma- < pari — + Av. (1262) yam-, cf s. v. päyam-.
== PHD grep abr line ==
42
```


## [2026-09-04T19:51:40.000Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN admiral ===\"; grep -n -i '^admiral' KLN_1966.txt KLN_1971.txt | head; echo \"=== KLN emir/amir ===\"; grep -n -i '^emir\\|^amir\\|^ameer' KLN_1966.txt | head"
}
```


### [2026-09-04T19:51:40.079Z] TOOL RESULT

```
=== KLN admiral ===
KLN_1971.txt:7666:admiral, n. — OF. amiral, amiralt (F. amiral), 
KLN_1971.txt:7677:admiralty, n. — ME., fr. OF. admiralte (whence 
KLN_1971.txt:81309:admiral, omrah. 
=== KLN emir/amir ===
2451:ameer,  amir,  n.,  a  Mohammedan  ruler.  —  Arab. amtr,  ‘commander,  prince’,  fr.  amara,  ‘he  com¬ manded'.  See  emir.
```


## [2026-09-04T19:51:46.909Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7660,7690p' KLN_1971.txt; echo \"=== KLN emir ===\"; grep -n -i '^emir' KLN_1971.txt KLN_1966.txt | head"
}
```


### [2026-09-04T19:51:47.004Z] TOOL RESULT

```
admirable, adj. — F., fr. L. admirdbilis, fr. ad- 
mirdri, ‘to admire*. See admire and -able and 
cp. MirabeL 

Derivatives: admirable, n., admirabl-y, adv. 
admiral, n. — OF. amiral, amiralt (F. amiral), 
prob. shortened fr. Arab, amtr-ar-rahl, ‘com- 
mander of transport, officer commanding a 
(transport) fleet’, whence also Port, amiralhs , 
amirat , It. ammiraglio (It. almiraglio and It., Sp. 
and Port, almirante arose from a confusion of 
am-, the beginning of the word amfr, with the 
Arab. art. al-\ It., Sp. and Port, almirante were 
transformed after the pres. part. suff. -ante, 
fr. L. -antem; see -ant); influenced in form by 
L. admirdri, ‘to admire*. See ameer, amir, 
admiralty, n. — ME., fr. OF. admiralte (whence 
MF. amiralte , F. amiraute). See admiral and 
-ty. 

admiration, n. — F., fr. L. admirdtionem, acc. of 
admirdtid, ‘a wondering at, admiration’, fr. ad- 
mirate , pp. of admirdri See admire and -ation. 
admirative, adj. — F. admiratif (fem. admirative ), 
fr. Late L. admirative, fr. admirate, pp. of ad- 
mirdri. See next word and -ative. 
admire, tr. and intr. v. — F. admirer, fr. L. ad- 
mirdri, ‘to wonder at’, fr. ad- and mirdri ; ‘to 
wonder*, fr. mire , ‘marvellous’, whence also 

=== KLN emir ===
KLN_1971.txt:81305:emir, n., 1) an Arabian prince; 2) a title given
```


## [2026-09-04T19:51:47.907Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'amiralis\\|amiral\\b\\|admirallus\\|amiratus' FSD_vol1.txt | head -20"
}
```


### [2026-09-04T19:51:47.967Z] TOOL RESULT

```
7816:4.  (1)  A   papilionid  butterfly;  as,  the  red  admiral  (   Va- nessa atalanta );  the  white  admiral  (Limenitis  Camilla). (2)  A   richly  colored  cone-shell  (Conus  ammiralis).  5y. A   Saracen  emir,  prince,  or  commander.  fOF.,  <LL.  ad- miralis,  amiralis,  <   Ar.  amir^aUbahr,  <   amir,  com- mander, +   of,  the,  +   bahr,  sea.]  —   admiral  of  the  fleet, a   title  of  honor  given  to  a   few  British  admirals.— a.  of  the red,  a.  of  flic  white,  a.  of  the  blue,  three  grades  formerly existing  In  the  British  navy:  so  called  from  the  colors  of  the flags  denoting  them.—  ad'mi-ral*shell",  n.  Conch.  Same as  admiral,  4   (2). —   Iand«3.,  n.  [Eng.]  An  admiral  whose duties  do  not  require  that  he  should  go  to  sea.—  Lord  High A.,  an  officer  formerly  In  supreme  charge  of  British  naval affairs.— rear *a,  n.  See  under  rear,  n.—  to  tap  the  a. LVaiif.).  to  tap  and  steal  from  casks  of  liquor  by  means  of a   gimlet  and  straw.—  vlce*a.»  n.  See  under  vice-,  prefix.
```


## [2026-09-04T19:52:02.035Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor f,ln in (('KLN_1971.txt',7666),('KLN_1966.txt',2451),('FSD_vol1.txt',7816)):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    off=sum(len(x)+1 for x in lines[:ln-1])\n    leaf=t[:off].count('\\f')\n    print(f,'line',ln,'-> leaf',leaf)\nEOF"
}
```


## [2026-09-04T19:52:03.374Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/admiral",
 "prompt": "Quote the English etymology section for 'admiral' verbatim, including the Arabic amīr al-… discussion, the Medieval Latin forms, and any note about which Arabic phrase is or is not the source."
}
```


### [2026-09-04T19:52:04.156Z] TOOL RESULT

```
KLN_1971.txt line 7666 -> leaf 0
KLN_1966.txt line 2451 -> leaf 44
FSD_vol1.txt line 7816 -> leaf 78
```


### [2026-09-04T19:52:09.980Z] TOOL RESULT

```
# Etymology of "Admiral"

According to Wiktionary, the English word "admiral" derives from Middle English and Old French *admiral*, ultimately from Arabic *أَمِير* (ʔamīr, "commander").

The etymology section notes that the ending is "frequently but mistakenly folk etymologized" from the Arabic article *ال* (al-), particularly in phrases like *أَمِير اَلبَحْر* (ʔamīr al-baḥr, "commander of the sea") or *أَمِير الْمُؤْمِنِين* (ʔamīr al-muʔminīn, "Commander of the Believers").

However, the source indicates it "seems instead to have been borrowed from modification of only the first term" in *أَمِير الْأُمَرَاء* (ʔamīr al-ʔumarāʔ, "emir of emirs, commander-in-chief"), as used for important commanders in Norman Sicily during the mid-12th century. The Medieval Latin forms include *admiralis*, *admirallus*, and *admiralius*.
```


## [2026-09-04T19:52:23.379Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (24,25,26):\n    seg=t[i]\n    print('LEAF',i,'admiral' in seg, seg[:200].replace('\\n',' '))\n    if 'admiral' in seg:\n        j=seg.find('admiral'); print('   ...',seg[max(0,j-200):j+700].replace('\\n',' '))\nEOF"
}
```


## [2026-09-04T19:52:25.011Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D9%85%D9%8A%D8%B1",
 "prompt": "Arabic أمير (ʔamīr): etymology, root, meanings, derived/related terms, and descendants (especially Persian, Latin, English). Quote the etymology verbatim."
}
```


### [2026-09-04T19:52:25.073Z] TOOL RESULT

```
LEAF 24 False ‘to  lead’.  See  duke. 23 Derivatives:  adduc-er,  n.,  adduc-ible,  adj. adducent,  adj.,  drawing  together  (said  of  mus¬ cles)  ;  the  opposite  of  abducent  ( anat .)  —  L.  ad- ditcens,  g
LEAF 25 True is  formed  fr.  ad-  and  ire,  ‘to  go’, fr.  I.-E.  base  *ei-,  •/-,  ‘to  go’,  whence  also  L. iter,  'a  journey.’  See  itinerate  and  cp.  aditus. Aditi,  n.,  the  endless  heaven,  mother
   ...   prec.  word and  -trix. admirable,  adj.  —  F.,  fr.  L.  admirdbilis,  fr.  ad¬ mirari,  ‘to  admire’.  See  admire  and  -able  and cp.  Mirabel. Derivatives:  admirable,  n.,  admirabl-y,  adv. admiral,  n.  —  OF.  amiral,  amiralt  <F.  amiral), prob.  shortened  fr.  Arab,  amtr-ar-rahl,  ‘com¬ mander  of  transport,  officer  commanding  a (transport)  fleet',  whence  also  Port,  amiralhs, amiral,  It.  ammiraglio  (.It.  almiraglio  and  It.,  Sp. and  Port,  almirante  arose  from  a  confusion  of am-,  the  beginning  of  the  word  amir,  with  the Arab.  art.  a!-;  It.,  Sp.  and  Port,  almirante  were transformed  after  the  pres.  part.  suff.  -ante, fr.  L.  -antem;  see  -ant);  influenced  in  form  by L.  admirari,  ‘to  admire’.  See  ameer,  amir, admiralty,  n.  —  ME.,  fr.  OF.  admiralte  (whence MF.  amiralte,  F.  amiraute).  See  admiral  and -ty. adm
LEAF 26 False dnem,  acc.  of admonitio,  fr.  admonite,  pp.  of  admonere.  See admonish  and  -ion. Derivatives:  admonition-er,  n. admonitor,  n.  —  L„  fr.  admonitus,  pp.  of  admo¬ nere.  See  admonish  a
```


### [2026-09-04T19:52:31.181Z] TOOL RESULT

```
# أمير (Amir) - Etymology and Meanings

## Etymology
According to the Wiktionary entry, the word originates from the Arabic root ء م ر (ʔ m r), with the following description:

"From ء م ر (ʔ m r), meaning to command, to order."

The etymological references provide additional context that this term originated in hunting, referring to "the leader of the hunting party who would give orders and commands."

## Primary Meanings
In Modern Standard Arabic, أمير functions as a masculine noun with two main definitions:
- Prince
- Commander

The feminine form is أميرة (amīra), and the plural is أمراء (umarāʔ).

## Notable Descendants
The word has traveled extensively into other languages, particularly:
- **Persian**: امیر (amir)
- **English**: amir
- **Ottoman Turkish**: evolved into "emir"
- **Romance Languages**: Through Medieval Latin "amiralis," it became Spanish "almirante" and Italian "ammiraglio" (admiral)

This linguistic journey demonstrates how the Arabic term for authority spread across Mediterranean and European languages through historical contact and trade.
```


## [2026-09-04T19:52:41.720Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in LKT.txt PHN.txt DEV.txt LAM.txt SKT.txt WEB_vol1.txt DOZ.txt; do echo \"##### $f\"; grep -n -i -m4 'amiral\\|admiral\\|emir\\b' $f | head -6; done"
}
```


## [2026-09-04T19:52:43.518Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%B1%D8%B2%D8%A7",
 "prompt": "Persian میرزا (mirzā): etymology (amīr + zāda?), meanings, history of usage. Quote the etymology verbatim."
}
```


### [2026-09-04T19:52:44.570Z] TOOL RESULT

```
##### LKT.txt
373:a)  Vom  Vb.  amara  'befehlen',  also: 'Befehlshaber,  Fürst'.  In  der  vulg.  Form emlr  in  alle  europäischen  Sprachen  als Fremdwort  übergegangen,  bemerke  be- sonders ndl.  emier.  —  Mit  ar-rahl 'Transport',  d.  h.  die  Transportflotte,  die dem  Verkehr  u.  der  Verbindung  zwischen Andalusien  u.  Nordafrika  diente,  wurde amir  verbunden  zu  amlr  ar-rahl,  dem Titel  für  den  Befehlshaber  dieser  Flotte. Hieraus  ergeben  sich  aus  der  Verkür- zung der  Form:  pg.  amiralh,  prov. amiralhs,  atnirat,  afrz.  amiri,  nfrz. amiral  [u.  mit  falscher  etymologischer Beziehung  zu  lat.  admirari]  admiral, rum.  amiral,  it.  ammiraglio  [u.  wie  im
374:sp.  pg.  mit  Verkennung  des  ar.  Stammes am  ...  als  ar.  Artikel]  almiraglio,  sp. pg.  almirante  [mit  volksetymologischer Umbildung  gemäß  dem  lat.  partic.  praes.], afrz.  aumirant,  prov.  amiran,  it.  almi- rante.  Die  Bedeutung  ist  überall  'Ober- befehlshaber der  Flotte'.  Ebenso  mhd. admirät  [als  Titel  des  Kalifen],  dtsch. Admiral,  ndl.  admiraal,  engl,  admiral. —  Daß  die  Worte  aus  amlr-al-bahr 'Befehlshaber  der  See,  des  Meeres'  ent- standen sein  sollen,  scheint  wenig  wahr- scheinlich, wenn  auch  ein  solcher  Weg- fall des  arab.  Wortes  hahr  an  und  für sich  möglich  ist,  vgl.  z.  B.  Denebola  [s. hier  Nr.  482],  Abdul  [wurde  bei  einem tk.  Schüler,  der  'Abd-ul-hädl  hieß,  stets als  Name  gebucht].  Dem  Wunsche  von ML  423  nach  einer  Geschichte  der  Form u.  Bedeutung  dieses  Wortes  muß  zuge- stimmt werden.  Nur  zum  Teil  ist  dieser Wunsch  durch  Christoph  Gebhardt,  Das arabische  Etymon  einiger  romanischer Wörter.  Programm  des  Slädt.  Gymna- siums mit  Realschule  zu  Greiz.  1912. S.  6 — 19  erfüllt  worden.  Der  Verfasser stellt  als  neues  Etymon  für  die  verschie- denen Formen  der  Gruppe  Admiral  ar. amir  awival  'erster  Emir,  Oberemir' auf,  leider  ohne  diese  Zusammenstellung in  arabischen  Schriftstellern  belegen  zu können.  Den  Formen  prov.  amiran, amirant,  sp.  pg.  it.  almirante  wird  [a. a.  0.  S.  15]  der  Ausdruck  anUr-amlrän 'Emir  der  Emire'  zugrunde  gelegt,  doch scheint  die  pers.-ar.  hybride  Form  in dieser  Gestalt  nicht  bestanden  zu  haben, auch  scheint  die  notwendige  Abkürzung zu  amiran  zu  merkwürdig  zu  sein  [na- türlich nach  pers.  u.  arab.  Sprachge- brauche ist  nur  die  Verkürzung  mir- mlrän].  Orientalische  Entlehnungen lassen  sich  nicht  ohne  weiteres  nur  mit Beachtung  der  romanischen  Lautgesetze verfolgen,  wie  im  Vorwort  allgemein bemerkt  wurde.  [Devic  DEt  31/32. Lammens  Rem  23/24.  DE  165.  Dozy Oost  5/6.  Kluge  7.  Rom  Forsch  IV, 368.
1319:'Eisen'  [vom  Stamme  tarn,  tem,  Um  'ver- sammelt, fest'  Vämbery  TktEtWb  S.  166, Nr.  17911];  hieraus  bulg.  serb.  demir 'Eisen,  eisern'.  —  Die  ältere  noch  im Öagataischen  lebendige  Form  timur kommt  im  N.  pr.  Timur-Leng  >  TA- MERLAN  vor.
2633:Kasmir  ist  eine  Stadt  und  ein  größeres Gebiet  im  nordwestlichen  Indien,  wo Schals  in  vorzüghcher  Qualität  her- gestellt wurden.  Hieraus  engl,  cashmere, ndl.  cachemir,  dtsch.  Kaschmir  (früher Kasimir);  it.  casimiro,  sp.  casimiro,  pg. Casimir a,  frz.  cachemire;  russ.  kazmir, kasemir,  poln.  kazmirek,  cech.  kazimir. [Bern  SlEtWb  496.
##### PHN.txt
830:puissant Emir qui jouit, parmi les Arabes de l'Afrique
1668:AMIRAL, 8. m. (a.)
1670:mander. — Pour obtenir amiral, il est nécessaire de placer
1676:dant de quoi? Il est évident que le mot amiral est un terme
##### DEV.txt
506:Amiral.  Aucun  étymologiste  ne  doute  que  ce  ne  soit  là le  mot  arabe  •A^î  amïr,  commandant,  émir.  Mais  la  termi- naison al  a  paru  d'autant  plus  embarrassante  qu'on  la  re- trouve dans  le  portugais  amiralh,  l'italien  almiragUo,  am- miraglio,  et  sous  d'autres  formes  dans  l'ancien  espagnol ahnirage,  l'espagnol  moderne  almirante,  le  bas  latin  admi- ralius,  admirallus,  amiraldus,  admiratus,  amirarius,  ami- randus ,  admirandiis ,  admirantius ,  amireda,  amirœus,  etc. Engelmann  avait  supposé  que  le  «/final  était  l'article  pré- cédant un  mot  tombé  depuis,  par  exemple  ^  bahr,  mer: amir-al-bahr,  commandant  de  la  mer,  serait  devenu  amir- al tout  court '^.  Cette  explication,  au  moins  quant  au  mot bahr,  ne  semble  guère  admissible,  vu  qu'on  a  de  nombreux exemples  du  Roman  d'Alexandre,  du  Roman  de  Rou,  de Garin,  cVAiibery^,  qui  prouvent  ([uamiraut,  amirant,  amiratz,
772:celle-la  ou  d'autres  ])arcilles  se  trouvent  dans  des  mots  de nos  langues  dont  l'origine  arabe  est  hors  de  doute.  (  Voy.  par exemple  Amiral.)  Quant  à  supposer  que  la  fin  du  mot  re- présente le  persan  AjLâ».  hhâneh,  maison,  je  n'y  vois  aucune vraisemblance.
1261:Emir.  Transcription  de  l'arabe  vjyoî  emlr  ou  am~u%  chef; le  même  mot  qui  a  donné  amiral.  Dans  certains  pays  mu- sulmans, on  dit  niir;  et  de  là  vient  le  mirza  i)*^*,  hls  d'é- mir, monsieur,  des  Persans.
1748:pour  5:>î)  jjyf>\  cmlr-zâdeh ,  fils  d'émir.  Emir  est  arabe,  zâdeh est  persane  De  ce  dernier  mot  et  de  »U  chah,  roi,  est formé  le  titre  de  chahzaihh,  fds  de  roi,  donné  à  l'héritier présomptif  du  trône ,  chez  les  Turcs.
##### LAM.txt
1070:et peut-être amiral.
1737:Amiral. Il y a longtemps qu'on a reconnu dans la
1755:sens bien différent de celui de notre amiral moderne: «xxiiij, Amii'aux, che-
1761:en a im lyii porte le titre d'Emir Bahr; il a sous sa garde tous les bateaux ;
##### SKT.txt
373:Admiral.  (F.-Arab.)  M.E. more  often  amiraLm^O.  F.  amiral, also  amirt\  cf.  Low  L.  admu prince,  chief.* Arab,  amlr^  a  pri Elmir.  The  suffix  is  due  to  Arab.] amir-ai-baJir,  pnncc  of  ihc  sea.
5803:EMIR,
20842:vice-gerent.  (F.  —  L.)  F,  vicegermt, a  deputy;  Cot.  —  I*  uici,  in  place  of; gertni',  stem  of  pres.  pt.  oinrtre.  to  carry un,  rule ;  see  Oesture.  %  So  also  viie- admiral,  vitt-roy  (from  F.  rci,  L.  rtgem, Iting),  vite-regai,
23690:ww  iM**  talmud,  targnm. tO:  alkali,  alkoran,  arrack,  attar J  aximutb,  carob-tree,  elixir,  emir, iC^ra,  hookah  t.hooka),  noudah I,  jerboa,  koran,  Mahometan  (Mo- \n\  moonshte,  moslem,  muezzin, idir,  otto,  rack  (5),  rayah,  T>'Ot. ulam),  sheik^  sherbet,  shmb  i^i\ oh,  loraiacura,  vUiet  (^iner). fam  Creek  from  Arabic :  naphtha,
##### WEB_vol1.txt
3206:ad/mi-ral, n. [ME. admiral, admiralle: OFr. admiral; from Ar. amir al, ruler of; sp. in- fluenced by admirable.)
3208:2. a naval officer of the highest rank or of a specified high rank. In the United States Navy, there are four grades of admiral, in order of rank. Admiral of the Fleet. full admiral, vice-admiral, and rear-admiral-
3209:3. the ship which carries the admiral: the flagship; also, the principal ship of a fleet of merchantmen, of yachts, or of fishing vessels.
3210:4. a name given to two species of butterflies: Vanessa atalanta, or red admiral, and Limenitis camilla, or white admiral.
##### DOZ.txt
324:amir (ook emir uitgesproken), bevelhebber y van den
341:amiralh en het Fr. amir al ontstaan. De redenen, die
352:dan voegde men achter amiraly of hoe het woord in
896:is van bedoe (in het litemir Arab. bedwon), open veld
```


### [2026-09-04T19:52:49.604Z] TOOL RESULT

```
# Etymology of Persian میرزا (mirzā)

According to the Wiktionary entry, the word derives from an earlier form. Here's the verbatim etymology:

"From earlier _میرزاد_ (mirzâd), compound of _میر_ (mir, 'master') and the suffix _ـزاد، ـزاده_ (-zâd, -zâde, 'child of, son of'), from _زادن_ (zâdan, 'to bear')."

**Summary:** The term combines "mir" (meaning master or prince) with a suffix denoting offspring or descent (-zâd/-zâde), literally translating to something like "child/son of a master." This compound structure reflects its historical use as a noble or administrative title in Persian-speaking regions.
```


## [2026-09-04T19:53:03.072Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON آدمیرال ==\"; grep -n 'آدمیرال\\|ادمیرال' MON_part1.txt MON_part2.txt | head; echo \"== MON امر/اماره/مامور/امارت ==\"; grep -n -m2 '^امر:\\|^امر\\b' MON_part1.txt | head; grep -n 'اماره:\\|امّاره\\|مأمور:\\|امارت:\\|^امیر' MON_part1.txt | head -20"
}
```


### [2026-09-04T19:53:03.216Z] TOOL RESULT

```
== MON آدمیرال ==
MON_part1.txt:2396:ادمیرال: 21 امیر البحر» دریا سالاره 
MON_part1.txt:4880:امیرالبحرء دریاسالار. آدمیرال. 
== MON امر/اماره/مامور/امارت ==
2279:امر» یایان کار» آخرالامر. 
4744:امرانه: (0-)20۵-]2176 (ق‌مر.) مانند اهر ان 
4880:امیرالبحرء دریاسالار. آدمیرال. 
11124:امیرالجیش. ضح اسپهبدان (- اسپاهبذان) 
16553:امارت: اصقحه [ع. امارة] (مصل.) امبر 
16557:اماره: (م-)هتقه [ع.] (ا.) نشان» نشانه» 
16559:اماره: (مصقههه زع. امارة] (ص.) بسیار 
16636:امیر دٍ شا لت اعد رص.) (سیا) 
16763:امیر؛ امیران» فرماندهان» مبران» سرداران. 
16942:امیر: 2 [ع. - مبر] (ص. .) کسی که 
16947:امیر کییر: 2.6۳2۲ [ع.] (امسر.) امیر 
35207:امیر از غذای او خورد تا اکر سمی در آن 
37284:امیر کردن به امارت گماردن. (امسص.) 
37285:امیر ی. 
40645:امیرالمو‌منین دانند؛ مق. تشیع. اهمل سنن: 
45182:امیر تومان: (نظ. قد.) فرماندهة ۱۰۰۰۰ 
55659:امیر. بزرگ قوم. 
58336:امیر ») ۳ 
58787:امیر دادء مر داد. 
60162:امیران. کاخ شاهی» قصر سلطنتی. دیوان عام. 
60905:امیرالبحری. در باسالاری. 
94505:امیر. رأی عالی: رأی اقب و صایب. فرمان
```


## [2026-09-04T19:53:05.356Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AFM amir ==\"; grep -n 'أمير\\|امير' AFM.txt | head -5; echo \"== PLA ==\"; grep -n -i 'amir\\|amīr' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -5; echo \"== FVQ amr ==\"; grep -n -i \"amara\\|'amr\\|amīr\" FVQ.txt | head -8; echo \"== RCH amudan ==\"; grep -n -i 'amudan\\|amuda\\|amun' RCH.txt | head -10"
}
```


### [2026-09-04T19:53:05.454Z] TOOL RESULT

```
== AFM amir ==
3988:3 من رجليه وبديه ل بعشرة مسامير ديععلى 4 من مأحكل كسرى 
4573:التكاليف الاميرية واعفاه عن جميع الوضائع بحيث اله لا يكون عرضة التحكدير 
4935:أمير ياكل الالو سر ويطعم ضيئة خيز الشعير 
5550:بالروممة وكافورى بالتركتة امير بالارامسة و 20111013 بالايطاليانة 
== PLA ==
3007:amirabür 27 ambiq 
3009:Pi _ ”amiräbür: "Stallmeister" aus dem ar. „-ı ’amir + pers. _.>' 
3014:ob! - ’amirbäris = ’ambarbäris s. ’ambarbäris . 
8797:pP - hamir: "Sauerteig" pers. 9, 
8800:Zu? - bamirdi: "Pastetenbäcker" ?. 
== FVQ amr ==
10301:period, as we see from the Mu'allaqa of 'Amr b. Kulthum, 1. 112. 
== RCH amudan ==
324:as  formerly  observed,  seem  to  have  been  merely feudatoiy  kingdoms  of  the  old  Persian  empire.— Alexander  the  Great  divided  the  Eastern  pro- vinces of  Persia  amongst  the  princes  to  whose families  they  had  originally  belonged.  On  this occasion  they  received  a   banner  from  the  hands  of Jje  conqueror,  paid  homage,  and  engaged  to lu^intain  a   certain  number  of  troops,  upon  a   foot- ing the  author  of  the  Tarlkh-i  Muntakliab) gon*ewhat  resembling  the  military  vassals  of  the Otf^itian  empire,  called  Smjacs  and  Timurs.  These prjpces  are  called  by  the  Muhammadan  writers ^jj//7/iM72\iawy//‘(kingsofthc  nations);  and  are  by as  a   particular  dynasty,  between the  Jaayiiuians  and  the  Ashkaniuns,  commonly called  f   Arsacides  by  Europeans.  They  strictly perfrA'med,  it  is  added,  tlieir  feudal  engagements trJ  Alexander;  but  on  his  death,  as  the  Grecian commanders  seized  upon  the  Western  kingdoms, they  also  assumed  an  independency  in  their  re- spective provinces.  This  account  seems  highly probable  ;   as  the  successors  of  Alexander,  accord- ing both  to  the  Eastern  and  Western  writers,  soon lost  all  sovereignty  to  the  eastward  of  the  Tigris.®* The  Tubba,  or  king  of  Arabia  Felix,  was  the acknowledged  paramount  sovereign  in  very  old times  of  a   number  of  tribes.  Alost  of  the  provinces of  Arabia  on  the  Persian  gulph,  with  those  stretch- ing towards  Babylonia,  held  of  the  Persian  kings of  the  Sassanian  dynasty;  who  often  appointed feudatory  princes  on  the  death  or  misconduct  of their  predecessors.  The  Caliph  Almamun  gave Khurasan,  which  he  himself  held  as  a   feudal sovereignty  under  his  father  Harun  APrashld,  to  )
443:The  Tartars,  in  the  circumstance  of  private  war, resembled,  in  many  particulars,  the  old  Arabians ; in  some  they  differed.  The  whole  history  of Abu’lghazI  Khan  is  filled  with  theiiiccssantwars  of the  various  tribes.  The  domestic  slavery  of  the men  was,  indeed,  seldom  adopted :   they  either massacred  them,  or  sent  them  into  distant  exile  ; but  the  women  were  made  ca})tives.  Abu’lghazl mentions  particularly,  when  the  princes  of  the tribe  of  Amunak,  about  the  year  1504,  defeated the  posterity  of  Rurga  SidtJin,  one  of  the  descen- dants of  Changiz  Khan,  that  they  put  to  death  all the  males  of  that  house,  but  their  wives  and daughters  they  kept  as  slaves.  When  they  spared their  prisoners,  and  either  set  them  at  liberty,  or
822:P.  Iv.  Some  combats  with  llie  DTws  have  been  slightly mentioned  (p.  xlvii.)  ;   previous  to  which,  great  preparations were  made  by  the  heroes  to  arm  themselves  with  spells,  as  a defence  against  their  enchantments;  accompanied  with  cere- monies differing  little  from  those  afterwards  practised  by  our European  knights,  when  setting  out  to  engage  with  necroman- cers or  giants.  See  Dictionary  dhiramun, — A   duel  in
4818:«   arghamunly  (A’^yi^Mi)  Wild  tansy.
10170:namudatif  To  provide,  to  be  careful.  tilfU  na-gSh,  Unawares.
10874:G   amamuny  (AVe/aor)  Slone-parsley.  Ginger.
11244::kA  amunoy  (fut.  ya~munu)  He  was  trust-worthy.
14748:repay.  jV  ba$min4m  Taftag.Wtw4*v  WwAAr survive.  Todewit,  to  cease.  To  Jie  separated, namudany  To  shew  again;  toezplain,  to  clear  op. ydftany  To  resume,  fli?,  (in  comp.  part,  nf Playing ;   a   player :   as  jb  $hatraf{;^baz^  A   chess-player,
16678:v.5^^  namudafiy  To  profess  physic,
18182:p   ^y)  bukalam  (or  bukalamun)^  The  chameleon.  A
```


## [2026-09-04T19:53:13.217Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- 2385-2400\"; sed -n '2385,2400p' MON_part1.txt; echo \"--- 16548-16565\"; sed -n '16548,16566p' MON_part1.txt; echo \"--- 16938,16950\"; sed -n '16938,16952p' MON_part1.txt; echo \"--- 4875,4885\"; sed -n '4875,4885p' MON_part1.txt"
}
```


### [2026-09-04T19:53:13.352Z] TOOL RESULT

```
--- 2385-2400

آدمکش: 2.4 [ع. ف.] (افا.) کشنده 

آدم قاتل انسان؛ آدمی‌کش. 

ادهیتا؛ 2012۳-1۶6 [ع.] (مسص جه.) آدم 

بودن» انسان بودن. به فضایل انسانی آراسته 

بودن. 

ادمیرال: 21 امیر البحر» دریا سالاره 
امبرال. 

آدمیزاد: 0-]2012001 [ - آدمیزاده] (ص مر .) 

--- 16548-16565


نشان‌ها. 
امارات: :7272 [ع.] ج اماره (امارت) 
ولایت‌ها. فر مانفرمایی‌ها» سرداری‌ها. 
امارت: اصقحه [ع. امارة] (مصل.) امبر 
شدن. (امص.) فرمانروایی. فرماندهی» 
سرداری. (.) ولابت» حوزة زیر فرمان امیر؛ 
ج. امارات. 
اماره: (م-)هتقه [ع.] (ا.) نشان» نشانه» 
علامت» ج. امارات. 
اماره: (مصقههه زع. امارة] (ص.) بسیار 
امر کننده» اغوا کننده به شرء برانگیزاننده به 
بدی. خواهش‌های نفسانی که آمر اعمال 
شیطانی است. 
اما کن: ۲ [ع.] 0( ج. امکنه» جج. 
مکان) جاهاء جای‌ها» سرژمین‌ها. اماکن 
عمومی: جاهای همگانی مانند مسحد»ه 
کاروانسرا و غیره. 
--- 16938,16950

امیدوار: 0.7 (ص مر .) آرزومند. متوفع» 
منتظر ؛ مق. ناامید» نو مید. 

امیر: 2 [ع. - مبر] (ص. .) کسی که 
فرمانروا بر قومی باشد؛ بادشاه. درجه‌ای 
پایین‌تر از بادشاه. حاکم. فرمانده ساه» 
سر دار » سیهسالار ) ج. امراء (امرا). 

امیر کییر: 2.6۳2۲ [ع.] (امسر.) امیر 
بزرگك. ضح. در عهد قاجاریه عنوان 
ارجمندی بود که به بعضی از صاحب‌منصبان 
عالی قدر داده شده. 

امیل: ا 2 [ع.] (رص تفض..) گرانندهر 
--- 4875,4885
و خیز با زنان داشتن. الفت گرفتن باء انس 
گرفتن با. پیوستن (چنانکه رودی به رود 
دیگر یا به دریا). 

ات ال 301121 [ع. امیرالس حر] (ا.) 
امیرالبحرء دریاسالار. آدمیرال. 

ام 7 زر د. آمیزیدن؛ قس. آمیغ ] 
آمیزش» مخلوط کردن. معاشرت. مباشرت» 
0 آمیغ. . (افا.) در بعضی کلمات مررکب 
سه معنی «آمیزنده) ات مردم آمیز»
```


## [2026-09-04T19:53:15.218Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON مأمور ==\"; grep -n 'مأمور' MON_part1.txt MON_part2.txt | head -6; echo \"== BQT امر/امیر (v1) ==\"; grep -n 'امیر:\\|^امر ' BQT_v1_pages.txt | head -5"
}
```


### [2026-09-04T19:53:15.311Z] TOOL RESULT

```
== MON مأمور ==
MON_part1.txt:1269:آبدار: 20-۳ (افا.) مأموری که موظف بود 
MON_part1.txt:1273:خادمی که مأمور تهیهٌ چای و قهوه و قلبان 
MON_part1.txt:2085:اه تش‌نشان: صقکه-.2 (افا. امر.) مأموری که 
MON_part1.txt:2104:مجموع دستگاه و مأموران فرو نشاندن 
MON_part1.txt:2565:مأمور کردن: بیاراست بر میمنه گیو و طوس 
MON_part1.txt:2655:اردل: 01 [- اردل ] (ا.) فراشی که مأمور 
== BQT امر/امیر (v1) ==
13759:امر ود ۴ ع با دال » بر وژن و عمنی
18469:امر بر وا رسیدن و برسیدن باشد یمنی واری
19880:امر بردادن باشد نی بدهش .
```


## [2026-09-04T19:53:47.842Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FRS ==\"; grep -n 'آمود\\|آمون' FRS.txt FRS_pages.txt | head -10; echo \"== FSF ==\"; grep -n 'آمود\\|آمون\\|گهرآمود' FSF.txt | head -10; echo \"== FFD ==\"; grep -n 'آمودن\\|آمود' incoming/FFD/FFD_pages.txt | head -10; echo \"== ARY ==\"; grep -n 'آمودن\\|آمون' incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-04T19:53:47.952Z] TOOL RESULT

```
== FRS ==
== FSF ==
== FFD ==
== ARY ==
```


## [2026-09-04T19:53:49.449Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%85%D9%88%D8%AF",
 "prompt": "Any Persian entry for آمود / آمودن / آموده? Give etymology and meaning verbatim if present."
}
```


### [2026-09-04T19:53:54.260Z] TOOL RESULT

```
# Response

The webpage provided is an English Wiktionary entry for آمود. While it mentions that a Persian version exists (shown in the language links at the top: "فارسی"), **the actual content of the Persian entry is not included** in the document you've shared.

The page only contains:
- A **Tashelhit** section (noting it's "Arabic spelling of amud")
- An **Urdu** section with etymology and meaning

To answer your question about the Persian entry for آمود/آمودن/آموده, you would need to visit the Persian Wiktionary directly, as that information is not present in this particular page content.
```


## [2026-09-04T19:53:59.081Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in FRS_pages.txt FSF.txt incoming/FFD/FFD_pages.txt incoming/ARY/ARY_pages.txt; do echo \"## $f size=$(stat -c%s $f)\"; grep -c 'آ' $f; grep -n -m3 'آمو' $f | cut -c1-150; done"
}
```


### [2026-09-04T19:54:00.821Z] TOOL RESULT

```
## FRS_pages.txt size=1613053
2641
5950:‫از سم آموارن_ و کوزنان شیار کرد ]‬
8443:                                         ‫آمو همی گرازد کردن همی فرازد‬
9658: ‫‪ : ۵ - ۳‬دخش ابتدا کردن بود ‪.‬‬       ‫آغالش کسی باد بر دهد و بد آموزی کند ‪.‬�
## FSF.txt size=1152733
4005
1954:*آموزگار = پرورنده 
1956:شکست اندر آمد به آموزگار 
2904:اهریمن به ضحاک می‌آموزد که پدر را 
## incoming/FFD/FFD_pages.txt size=170624
631
434:هن آموختن َوهل: بسیار آموختن
758:آموخت < فارسی میانه 270871 + ایرانی باستان 3-2۵0-1۵*. برای 3و 1۵ >
764:آموز < فارسی میانه 38162 < ایرانی باستان 2 + 3-۵06*. برای 2 آرای. در
## incoming/ARY/ARY_pages.txt size=960497
2167
398:در سده‌های شانزدهم و هفدهم میلادی که طی آن آموزش زبانهای خارجی رونق گرفته بود»
993:فلسفی و آمور فراجهانی نداشت. در اسطوره‌های ژرمن‌ها و سلت‌ها و یونانیان و رومیا�
3553:سلمان فارسی حفر " کندک" (خندق) را به آنها آموخت.
```


## [2026-09-04T19:54:15.510Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D9%85%D8%B1",
 "prompt": "Arabic أمر: give the verb أَمَرَ (ʔamara) 'to command' and the noun أَمْر (ʔamr) 'order, command' — etymology, root ء م ر, meanings, and descendants into Persian/Ottoman Turkish. Quote verbatim."
}
```


## [2026-09-04T19:54:17.043Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%A3%D9%85%D9%88%D8%B1",
 "prompt": "Entries for مأمور in Arabic and Persian: etymology (passive participle of أمر?), meanings ('official, agent, one who is ordered'). Quote verbatim."
}
```


### [2026-09-04T19:54:21.710Z] TOOL RESULT

```
# Arabic أمر: Verb and Noun Overview

## Verb: أَمَرَ (ʔamara)

**Etymology & Root:** From Semitic root ء م ر (ʔ m r), cognate to Hebrew אמר (amár, "to say")

**Primary Meanings:**
- "to order, to command, to bid, to instruct"
- "to commission, to charge, to entrust"

## Noun: أَمْر (ʔamr)

**Meanings:**
- "order, command, instruction"
- "ordinance, decree"
- "power, authority"
- "matter, affair, concern"
- (Grammar) "imperative"
- (Computing) "command" or "instruction"

**Plural:** أَوَامِر (ʔawāmir) or أُمُور (ʔumūr)

## Notable Descendants

The term spread to neighboring languages:
- **Persian:** امر (amr)
- **Ottoman Turkish:** امر (emir) → Modern Turkish: emir
- **Urdu:** اَمْر (amr)
- **Swahili:** amri

The root remains productive across Semitic and influenced languages, particularly in administrative and command contexts.
```


### [2026-09-04T19:54:22.077Z] TOOL RESULT

```
# مأمور (ma'mur) - Entry Summary

## Etymology
The word derives from a passive participle form. In Arabic, it comes from the "passive participle of _أَمَرَ_ (ʔamara, 'to order, to command')." Persian borrowed this term directly from Arabic.

## Meanings

**Arabic definitions:**
- "officer, bailiff"
- "subject"
- "magistrate"

**Persian definitions:**
- "official, officer, delegate, functionary, agent" (as a noun)
- "ordered, commanded, commissioned, appointed" (as an adjective)

**Ottoman Turkish definition:**
- "officer, official, agent, somebody charged with an office"

The term spread across multiple languages through Ottoman Turkish, eventually entering Albanian, Armenian, Bulgarian, Romanian, and other languages in the region.
```


## [2026-09-04T19:54:29.774Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.vajehyab.com/dehkhoda/%D8%A2%D9%85%D9%88%D8%AF%D9%86",
 "prompt": "Dehkhoda entry for آمودن: meanings, cited verses, and any etymological note (Pahlavi form). Quote verbatim in Persian."
}
```


## [2026-09-04T19:54:30.999Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/maH-",
 "prompt": "Proto-Iranian *maH- 'to measure': reconstruction, derived terms with preverbs (ā-, pati-, fra-, ni-), and descendants. Quote verbatim."
}
```


### [2026-09-04T19:54:33.128Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T19:54:35.735Z] TOOL RESULT

```
# معنی آمودن (Dehkhoda Dictionary)

According to the Dehkhoda Dictionary entry, **آمودن** carries several meanings:

1. **Mixing/Blending**: "آمیختن . درهم کردن . آمیخته شدن" (to mix, combine, or be mixed together)

2. **Inlaying/Setting**: Placing jewels or gems into settings, as exemplified by the cited verse from Nezami.

3. **Stringing**: "بتار و به نخ کشیدن گوهرها و مهره ها" (threading pearls and beads on thread/string)

4. **Adorning/Ornamenting**: "آراسته شدن" and "زینت کردن" (to be decorated, to embellish)

5. **Preparing/Readying**: "مهیا، معد، آماده کردن" (to prepare or make ready)

6. **Filling**: "پر کردن . مملو ساختن" (to fill or make full)

The dictionary notes that the infinitive forms are **آمودم** and **آمای**, with **آزمایش** serving as both a noun infinitive and secondary infinitive form.
```


## [2026-09-04T19:54:55.769Z] TOOL CALL #48: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/admiral|page 53, root A'.m.r, admiral chain: OF amiral < Arabic amir; unetymological -d- from L. admirabilis\" \\\n \"https://en.wiktionary.org/wiki/admiral|page 53, root A'.m.r, node 3-5: Medieval Latin admiralis/admirallus, rejection of amir al-bahr as source\" \\\n \"https://en.wiktionary.org/wiki/%D8%A3%D9%85%D9%8A%D8%B1|page 53, root A'.m.r: Arabic amir 'commander' from root ' m r, descendants\" \\\n \"https://en.wiktionary.org/wiki/%D8%A3%D9%85%D8%B1|page 53, root A'.m.r: Arabic amara/amr, root ء م ر, Persian amr\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%A3%D9%85%D9%88%D8%B1|page 53, node 1: ma'mur passive participle of amara, Persian 'official, agent'\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%B1%D8%B2%D8%A7|page 53, node 1: mirza < mirzad = mir + -zada\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D9%85%D8%A7%D8%AF%D9%86|page 53, root Amon: Persian amadan < Proto-Iranian *a-maH- 'to measure/prepare'\" \\\n \"https://www.vajehyab.com/dehkhoda/%D8%A2%D9%85%D9%88%D8%AF%D9%86|page 53, node 1: Dehkhoda s.v. amudan 'to fill, set gems, adorn', present stem amay-\" \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done"
}
```


### [2026-09-04T19:54:59.559Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5c5fd5f304537f2a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f0d815fa678ed6c8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dcefbff6778872a7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bb26bea750b22982.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cd6621f2be5b61ac.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a3c23b64ec382782.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ccf34abd57cf4727.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/645cb2c72d2e887e.txt
```


## [2026-09-04T19:55:05.610Z] TOOL CALL #49: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://archive.org/details/VajnameShayest/page/n19\" --note \"page 53, root Amon: SNS (Tavoosi, Vazhe-name-ye Shayast ne Shayast) printed p.6, entry amon 'full' and abr-amon; page image read directly, transcription saved to refs/ocr/SNS/6.vision.txt\" 2>&1 | tail -2; echo ====; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-04T19:55:10.614Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/bfc924c42d74e37f.txt
(eval):1: === not found
```


## [2026-09-04T19:55:12.689Z] TOOL CALL #50: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-04T19:55:12.731Z] TOOL RESULT

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


## [2026-09-04T19:55:29.826Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== RCH amir ==\"; grep -n -o -i '.\\{0,90\\}amir,\\? \\(A\\|a\\) *\\(prince\\|commander\\|lord\\).\\{0,90\\}' RCH.txt | head -6; echo \"== RCH amr ==\"; grep -n -o -i '.\\{0,60\\}amr, *A *\\(command\\|order\\).\\{0,80\\}' RCH.txt | head -4; echo \"== RCH mirza ==\"; grep -n -o -i '.\\{0,60\\}mirza.\\{0,120\\}' RCH.txt | head -4; echo \"== AHD_watkins admiral ==\"; grep -n -i 'admiral' AHD_watkins1985.txt | head -3; echo \"== PHN amiral ctx ==\"; sed -n '1666,1700p' PHN.txt"
}
```


## [2026-09-04T19:55:31.134Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=admiral",
 "prompt": "Give the American Heritage Dictionary entry for 'admiral', especially the etymology bracket in full, verbatim."
}
```


### [2026-09-04T19:55:39.153Z] TOOL RESULT

```
== RCH amir ==
ugrep: error: error at position 114
ce|commander|lord)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,90}
                         exceeds complexity limits___/


== RCH amr ==
ugrep: error: error at position 101
rder)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,80}
            exceeds complexity limits___/


== RCH mirza ==
ugrep: error: error at position 83
bf][\x80-\xbf]*){0,120}
                       \___exceeds complexity limits


== AHD_watkins admiral ==
== PHN amiral ctx ==
racine arabe qu'il convient de rapporter le substantif myrbhb.
Voyez ce mot.
AMIRAL, 8. m. (a.)
j^ [àmirj commandant, chef, émir, dérivé de^l [àmar] corn-
mander. — Pour obtenir amiral, il est nécessaire de placer
l'article al à la suite du mot amir; mais par quelle bizarrerie
a-t-on mis l'article en second lieu, quand, pour les autres mots
empruntés à l'arabe , tels que alcôve, algarade, etc. , cet article
est toujours en tête du mot? On aurait bien pu dire, par ana-
logie, aUnâr (j^k^^l), le commandant en chef, mais comman-
dant de quoi? Il est évident que le mot amiral est un terme
tronqué, dont le sens n'a été fixé que par convention, puisque,
d'après les règles de la syntaxe arabe, il représente seulement
chef de — En arabe, tout mot suivi de l'article exige
un complément. On dit, par exemple, (jâ^A^jJuti [àmir aU
djouyoûch^ chef on commandant des troupes, ^j*Juêy^\jjuJi [àmtr
almoàminin, dont on a fait, par corruption, miramoun] cont-
mandant des croyants. Gomme le mot amiral ne se dit que du
grand officier des armées navales, l'expression j-^t jxa\ [àmir
alhnh'r], chef de la mer, est celle qu'on aurait peut-^tre dti con-ANIS 39
server dans notre langue, car le second mot est nécessaire pour
déterminer le sens du premier. — Les Espagnols et les Por-
tugais ont adopté almirante, les Italiens écrivent ammiragUo, et
les Anglais admirai, toutes variantes plus ou moins éloignées
du correspondant arabe. — L'équivalent d'amtral, en turc, est
cAPiTAN-PAGHA. Voycz ce mot.
AMOME,s. m. (a.)
Ul^ [A'omiifmi] Fruit d'une plante du genre des balisiers; drogue
qui entre dans la thériaque; arbuste solané, plante odorifé-
rante, originaire d'Asie. — Le mot arabe paratt se rattacher
au radical a»- [ÀWmm] chaleur excessive, et, "par extension,
saveur chaude des épices. On lit dans la Flore de Virgile, rédigée
par M. Fée pour la collection des classiques latins de Lemaire,
que le grec Afjtcûfiov est évidemment tiré de son homonyme
Ul^ [h'tttnâmâ] , les Arabes ayant été les premiers à faire con-
```


### [2026-09-04T19:55:45.949Z] TOOL RESULT

```
# American Heritage Dictionary Entry for "Admiral"

The entry defines admiral across five meanings, including a fleet commander, flag officer, specific naval ranks, colorful butterflies, and archaic usage for a flagship.

The etymology bracket states:

"[Middle English *amiral, admiral*, Muslim military commander, emir, admiral, ultimately (partly via Old French *amiral*) from Medieval Latin *admīrālis*, alteration (influenced by *admīrārī*, to wonder at, admire) of *amīrālis*, ultimately (possibly via Medieval Greek *ameras, amerad-*) from Arabic *'amīr*, commander; see **ʾmr** [in the Appendix of Semitic roots] + Latin *-ālis*, noun suffix. Alternatively, both Old French *amiral* and Medieval Latin *amīrālis* ultimately from Arabic *'amīr-al-'ālī*, the high commander (*'amīr* + *al*, the + *'ālī*, high; see **ʿly** [in the Appendix of Semitic roots]).]"

This traces the word's origins through Middle English, Old French, Medieval Latin, and ultimately to Arabic roots meaning "commander."
```


## [2026-09-04T19:55:55.206Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'A commander, prince\\|amiru\\|mirza,' RCH.txt | head -8; echo \"---\"; grep -n -i 'amudan\\|To fill, to stuff\\|amuda' RCH.txt | head -8"
}
```


### [2026-09-04T19:55:55.285Z] TOOL RESULT

```
11330:A amir  (or  mir),  A   commander,  governor,  emperor, chief,  leader,  lord,  prince.  ^^\ The  amiru’l  umara,  prince of  prinCes,  a   viceroy  or  governor  of  a   great  province.  This  was a   title  adopted  by  the  ministers,  or  rather  the  tyrants,  of  the KhalTfs  of  Baghdad,  in  the  decline  of  their  empire.  It  was  an oflice  of  vast  dignity,  and  was  enjoyed  by  ii||uiy  sovereigns  of powerful  independent  dominions ;   particularly  by  the  Hamadan and  Buyan  princes;  some  of  whom,  whilst  Amlru’l  umaras, were  at  the  same  time  kings  of  Persia  and  other  extensive  dis- tricts. The  first  AinTru’l  umara,  I   bn  Rayik  (of  the  Hamadan family),  prince  of  Basrah  and  Wasit,  was  raised  to  that  dignity, acording  to  the  (history  of  the  Muslims)  in  the
67302:Kumarly,  A   kind  of  wood  so  called  from  j\^  Kumar  or Kamirun,  (Cape  Comorin)  in  India.
96695:namirUy  Explanation,  interpretation,  commentary.
---
10170:namudatif  To  provide,  to  be  careful.  tilfU  na-gSh,  Unawares.
14748:repay.  jV  ba$min4m  Taftag.Wtw4*v  WwAAr survive.  Todewit,  to  cease.  To  Jie  separated, namudany  To  shew  again;  toezplain,  to  clear  op. ydftany  To  resume,  fli?,  (in  comp.  part,  nf Playing ;   a   player :   as  jb  $hatraf{;^baz^  A   chess-player,
16678:v.5^^  namudafiy  To  profess  physic,
20155:p   i>\^  pas-nihddy  A   treasure,  a   store,  a   reserve, p   J   ^   pesA  namudauy  To  hesitate,  demur,
25918:A   takumy  (II  of  Distributing,  dividing,  scattering. Giving  to  be  divided.  Division  in  arithmetic, sm^ijam^y  An  assessment  of  land.  A   rent-roll,  p taksim  namudanyTo  distribute,  to  allot.,
29429:namudany  To  sift,  bolt,  jdmn-t'  kh^dby  Bed-clothes.
37623:namudariy  To  abase  one’s  self.
37947:kVusKi  namudanj  To  display  excellence  or  benignity.
```


## [2026-09-04T19:55:56.248Z] TOOL CALL #54: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://ahdictionary.com/word/search.html?q=admiral\" --note \"page 53, root A'.m.r node 5: AHD etymology of 'admiral' (Nourai cites AHD for this node)\" 2>&1 | tail -1"
}
```


### [2026-09-04T19:55:59.102Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7f3ed97e2300b559.txt
```


## [2026-09-04T19:56:46.257Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== abr-amun ==\"; grep -n 'ابرآمون\\|ابر آمون' MON_part1.txt MON_part2.txt BQT_v1_pages.txt FSF.txt FRS_pages.txt 2>/dev/null | head; echo \"(none = silent)\"; echo \"== BQT leaf 271/272 header check ==\"; python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (270,271,272):\n    print('LEAF',i,repr(t[i][:120]))\n\""
}
```


### [2026-09-04T19:56:47.997Z] TOOL RESULT

```
== abr-amun ==
(none = silent)
== BQT leaf 271/272 header check ==
LEAF 270 'آماره مات\n] مارم ۱ بروژن و معثی آواره - آموخته است ۵ . #\nوییعنی آعار است کهمرض استقا - ونهایت تفحص\n.و تس - و ساب - و تشب'
LEAF 271 'آمله ۲ - ینم ثاكك و قح رابغ » دوائی\nاست کثیرالتفع وممرب آن «آملج» باشد . گویند\nدو درم را از آن کوفه تا دوساعت درآب شیرین'
LEAF 272 'آموده ۰ 7۳۳\nو آ یخته\u200cشدن - وساختن و ساخته گردانبدن٩\u200f ۹\nو پر کردن و مملو ساختن باشد .\nآموده ۴ « پروزن آسوده » لمل و\nمروار'
```


## [2026-09-04T20:00:19.393Z] TOOL CALL #56: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /home/sfmqrb/git/rishe/data/verification/page-53.json <<'JSONEOF'\n{\n  \"pdf_page\": 53,\n  \"book_page\": 23,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Âmon\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"MP/early NP āmōn ~ āmūn (آمون) 'full, brimful' — a deverbal of *ā-maH- 'to measure out, prepare', not an independent root\",\n      \"note\": \"Nourai's citation is exact: SNS (Tavoosi, Vāzhe-nāme-ye Šāyast nē Šāyast) p. 6 has the lemma 'āmōn : آمون، پر، مملو، لبالب … و ترکیب: abr-āmōn یعنی: پر ابر، ابری. ک ۱۰/۲', i.e. āmōn 'full, filled, brimful' and the compound abr-āmōn 'full of cloud, cloudy' at Šāyast nē Šāyast 10.2 — and it quotes exactly the Sanāʾi couplet the JSON records ('هم زبانشان ز فحش آموده / هم درونشان به خبث آلوده'). Two caveats keep this from 'confirmed'. (a) Āmōn is not a root: it is a nominal/adjectival derivative of the Old Iranian verb *ā-maH- 'to measure out, prepare' (Cheung 2007: 255-256 s.v. *maH¹), the same verb that yields NP āmūdan/āmāy- and āmādan/āmāde. Nourai's arrows therefore run backwards — āmūdan does not come from āmōn; both come from *ā-maH-. (b) Tavoosi himself documents the free-standing āmōn not from a Pahlavi text but from the New Persian Farhang-e Jahāngīrī ('آمو (و آمون) بمعنی پر کرده بود'); in the Pahlavi corpus only the compound abr-āmōn is attested. MacKenzie's Concise Pahlavi Dictionary and Nyberg's glossary have no āmōn at all (Nyberg's only -mōn word here is pērāmōn < *pari-yāma-van-, a different root).\",\n      \"sources\": [\n        \"https://archive.org/details/VajnameShayest/page/n19\",\n        \"https://en.wiktionary.org/wiki/%D8%A2%D9%85%D8%A7%D8%AF%D9%86\",\n        \"https://www.vajehyab.com/dehkhoda/%D8%A2%D9%85%D9%88%D8%AF%D9%86\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"SNS:6\",\n          \"status\": \"supports\",\n          \"note\": \"Read from the page image (archive.org/details/VajnameShayest leaf n19 = printed p. ۶; transcription saved to data/verification/sources/refs/ocr/SNS/6.vision.txt). Entry: 'āmōn : آمون، پر، مملو، لبالب (پر لبالب) در فرهنگ جهانگیری آمده. «آمو (و آمون) بمعنی پر کرده بود» و آمود و آموده نیز بهمین معنی است. سنایی: هم زبانشان ز فحش آموده. هم درونشان به خبث آلوده … و ترکیب: abr-āmōn یعنی: پر ابر، ابری. ک ۱۰/۲'. Exactly Nourai's gloss and exactly his three boxes.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"âmŭdan; gohar-âmŭd\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP آمودن āmūdan (past stem āmūd-, present stem آمای āmāy-) 'to fill, to mix, to set/string gems, to adorn, to make ready' continues Old Iranian *ā-maH- (preverb *ā- + *maH¹ 'to measure, measure out'), the same formation as paymūdan/paymāy- (*pati-maH-), āzmūdan/āzmāy- (*ā-uz-maH-), farmūdan/farmāy- (*fra-maH-) and nomūdan/nomāy- (*ni-maH-); the -ūd- of the past stem beside -āy- of the present is the regular Middle Persian ablaut of this class (BMP ptmʾd- /paymāy-/ ~ inf. ʾwzmwtn /uzmūdan/, Cheung 2007: 255f.). The doublet آمادن āmādan / آماده āmāde 'ready' preserves the ā-vocalism of the same verb, and Moʿin explicitly cross-references the two ('آمودن … [قس. آمادن]'). Semantically: 'prepare, arrange' → 'set in place, inlay (a gem in a ring), string (pearls on a thread)' → 'stuff, fill, deck out' — the whole range is spelled out in Dehkhoda and in Borhān-e Qāṭeʿ ('و پر کردن و مملو ساختن باشد'). گوهرآمود gohar-āmūd is gohar 'gem, jewel' (MP gōhr) + the bare past stem āmūd used adjectivally, 'gem-filled, gem-studded' — the very sense Moʿin gives the verb ('ترصیع، در نشاندن چنانکه گوهری را در انگشتری'). Both words are real and correctly glossed; what is wrong is the direction of Nourai's arrow: āmūdan is not derived from the noun āmōn, the noun is derived from the verb stem.\",\n          \"sources\": [\n            \"https://www.vajehyab.com/dehkhoda/%D8%A2%D9%85%D9%88%D8%AF%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%A2%D9%85%D8%A7%D8%AF%D9%86\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"SNS:6\",\n              \"status\": \"supports\",\n              \"note\": \"SNS p.6 (image, leaf n19): 'و آمود و آموده نیز بهمین معنی است' — Tavoosi expressly links āmūd/āmūde to āmōn 'full', and cites the Sanāʾi verse with آموده that the JSON records.\"\n            },\n            {\n              \"ref\": \"BQT:61\",\n              \"status\": \"supports\",\n              \"note\": \"BQT_v1_pages.txt leaf 272 (printed p. 61-62; head-word آموده, offset printed ≈ leaf−210): 'آمودن بروزن آسودن . بمعنی … و آمیخته‌شدن و ساختن و ساخته گردانیدن و پر کردن و مملو ساختن باشد'; and 'آموده «بروزن آسوده» لعل و مروارید و امثال آن را گویند که در رشته کشیده شده باشد، و بمعنی پر کرده و مملو ساخته هم هست، و آراسته و پیراسته را نیز گویند'. Same leaf also has 'آمون … و بمعنی پر و مملو و لبالب و لبریز هم هست' and 'آمو … و بمعنی پر کردن و مملو ساختن'. Moʿin's footnotes there read 'رک: آمودن'.\"\n            },\n            {\n              \"ref\": \"MON:91\",\n              \"status\": \"supports\",\n              \"note\": \"MON_part1.txt l.4799: 'آمودن: ĀMŪDAN [قس. آمادن] (مص‌متعدی) آمیختن، درهم کردن. ترصیع، در نشاندن چنانکه گوهری را در انگشتری. به سلک درآوردن؛ به نخ کشیدن گوهرها و مهره‌ها. آراستن، زینت کردن. مهیا کردن، آماده کردن.' — 'setting a gem in a ring' is exactly gohar-āmūd. (Page number not checkable: the OCR of Moʿin carries no printed page numbers, but آمودن does fall in the آم- run of vol. 1, consistent with p. 91.)\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"vol. 1 s.v. آمودن (MON_part1.txt l.4799) and s.v. آمون (l.4831)\",\n              \"stance\": \"supports\",\n              \"note\": \"'آمون: (ص.) پر، مملو، لبالب' — Moʿin lemmatises āmūn as an adjective 'full, brimful', and آمودن with '[قس. آمادن]', tying the verb to āmādan rather than to āmūn.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 1 leaf 272 = printed pp. 61-62, s.vv. آمودن / آموده / آمون / آمو\",\n              \"stance\": \"supports\",\n              \"note\": \"'و پر کردن و مملو ساختن باشد' for آمودن; 'بمعنی پر و مملو و لبالب و لبریز' for آمون.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p. 255-256 s.v. *maH¹ 'to measure' (CHEUNG.txt ll. 16898-17013)\",\n              \"stance\": \"partial\",\n              \"note\": \"'*NWIR: (+ *ā-) NP āmādan/āmāy- \\\"to prepare\\\"' and MMP ʾmʾdg 'prepared, ready', BSogd. ʾʾmʾ- 'to prepare'; PIE *meH₁- (LIV 424f., Pok. 703f.). Cheung lists the ā-form āmādan but not āmūdan; the -ūd-/-āy- pair of āmūdan is the same stem type he gives for uzmūdan/āzmāy- and paymūdan/paymāy-.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"grepped HRN.txt for āmūd/amud/āmāy — no hit (Horn's no. 41 āgenden 'anfüllen' is a different verb)\",\n              \"stance\": \"silent\",\n              \"note\": \"Horn has no article on āmūdan.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"grepped HUB.txt for āmū-/amud — no hit\",\n              \"stance\": \"silent\",\n              \"note\": \"Hübschmann's Persische Studien does not treat the word.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, s.vv. āmēxtan/āmēz-, āmurzīdan, hammōxtan (PHD.txt l.191, l.392)\",\n              \"stance\": \"silent\",\n              \"note\": \"No MP *āmūdan or āmōn in MacKenzie; the ām- entries are āmēxtan 'mix', āmurzīdan 'forgive', hammōxtan 'teach'.\"\n            },\n            {\n              \"src\": \"Dehkhoda (vajehyab)\",\n              \"where\": \"https://www.vajehyab.com/dehkhoda/آمودن\",\n              \"stance\": \"supports\",\n              \"note\": \"'آمیختن. درهم کردن… بتار و به نخ کشیدن گوهرها و مهره‌ها… آراسته شدن… مهیا، معد، آماده کردن… پر کردن. مملو ساختن'; present stem given as آمای.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"abr-âmŭn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Book Pahlavi abr-āmōn is a bahuvrīhi-type compound of abr 'cloud' (MP ʾp̄l/lbl, MacKenzie s.v. abr; NP ابر abr, from Ir. *abra-, PIE *nebʰ-os — hence Nourai's cross-reference '☞Nebh') + āmōn 'full', literally 'cloud-full' = 'overcast, cloudy'. It is attested in the Pahlavi Šāyast nē Šāyast (Tavoosi's glossary cites it at 10.2; his index also lists 'abramōn 11/10'), which is the whole basis of Nourai's root box. Morphologically āmōn continues *ā-māna-, a -mān-/-mōn- noun to the verb *ā-maH- 'to measure out, prepare, fill' (cf. frāmān/farmān < *fra-māna- 'command' to *fra-maH-, and the same -ōn spelling in MP hāmōn > NP hāmūn).\",\n          \"sources\": [\n            \"https://archive.org/details/VajnameShayest/page/n19\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"SNS:6\",\n              \"status\": \"supports\",\n              \"note\": \"SNS p.6 (image, leaf n19; transcription in refs/ocr/SNS/6.vision.txt): '… و ترکیب: abr-āmōn یعنی: پر ابر، ابری. ک ۱۰/۲' — 'the compound abr-āmōn, i.e. full of cloud, cloudy', with the text reference Šāyast nē Šāyast 10.2. This is verbatim Nourai's node.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, PHD_mackenzie.txt l.813 s.v. abr\",\n              \"stance\": \"partial\",\n              \"note\": \"'abr [lbl, ʾpl | N ~] cloud.' — confirms the first member; MacKenzie has no compound abr-āmōn and no āmōn (the word is confined to Šāyast nē Šāyast).\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg vol. II glossary, grepped for āmōn / ʾmwn\",\n              \"stance\": \"silent\",\n              \"note\": \"No āmōn or abr-āmōn; the only comparable form is 'pērāmōn [pylʾmwnʼ] … < *pari-yāma-van-', from Av. yam-, a different root.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"abr-âmŭn\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The New Persian box is the phonetically expected continuation of MP abr-āmōn: MP ō regularly gives NP ū (hāmōn > hāmūn, ammōn-type nouns), so abr-āmōn > ابرآمون abr-āmūn 'cloudy'. Nourai's own NOTE that the word is 'apparently obsolete' is, if anything, understated: no Persian dictionary I could check lemmatises ابرآمون — it is absent from Borhān-e Qāṭeʿ vol. 1, from Moʿin, from Asadi's Loghat-e Fors and from Nūshin's Šāhnāme glossary — although the simplex آمون 'full, brimful' is in both Borhān-e Qāṭeʿ and Moʿin. The node is therefore best read as Nourai transliterating the Pahlavi compound into Persian script rather than citing a living Persian word.\",\n          \"sources\": [\n            \"https://archive.org/details/VajnameShayest/page/n19\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"SNS:6\",\n              \"status\": \"partial\",\n              \"note\": \"SNS p.6 gives abr-āmōn as a Pahlavi compound of the Šāyast nē Šāyast text and glosses it 'پر ابر، ابری' in Persian; it does not claim a New Persian word ابرآمون. The Persian gloss 'ابری' is Tavoosi's translation, which is presumably what Nourai turned into a separate Persian node.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"BQT_v1_pages.txt, grepped ابرآمون / ابر آمون\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry ابرآمون; vol. 1 leaf 272 has only the simplex آمون 'پر و مملو و لبالب و لبریز'.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"MON_part1.txt / MON_part2.txt, grepped ابرآمون\",\n              \"stance\": \"silent\",\n              \"note\": \"Moʿin has آمون '(ص.) پر، مملو، لبالب' (l.4831) but no compound ابرآمون; the آمون- hits in Moʿin are otherwise chemical (آمونیاک، آمونیوم).\"\n            },\n            {\n              \"src\": \"FSF\",\n              \"where\": \"Nūshin, Farhang-e Šāhnāme (FSF.txt), grepped آمود/آمون\",\n              \"stance\": \"silent\",\n              \"note\": \"No hit — the word is not in the Šāhnāme vocabulary Nūshin treats.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"A'.m.r\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Arabic root ء م ر (ʾ-m-r), verb أَمَرَ ʾamara 'to order, command'; nomen agentis أَمِير ʾamīr 'commander, prince'\",\n      \"note\": \"The root box, its language label and its gloss are all right, and so is the sub-box 'Amîr : commander': Klein p.26 s.v. 'ameer, amir' gives 'Arab. amīr, \\\"commander, prince\\\", fr. amara, \\\"he commanded\\\"'. Wiktionary derives أَمَرَ from the Semitic root ʾ-m-r, cognate with Hebrew אמר ʾāmar 'to say'. The cross-cutting problem on this page is node #2: Nourai (following Funk & Wagnalls and Klein) makes the European word start from a full Arabic phrase, amīr al-baḥr or amīr ar-raḥl. Modern scholarship rejects both particular phrases. Lokotsch already wrote in 1927 that deriving the group from amīr-al-baḥr 'scheint wenig wahrscheinlich', and Devic 1876 said the same; the AHD, the OED and Wiktionary now take Medieval Latin amīrālis as amīr + Latin -ālis, or as a shortening of any of the many amīr al-X titles (above all amīr al-umarāʾ, the title borne by commanders in Norman Sicily in the mid-12th c.), not of amīr al-baḥr specifically. Two smaller data problems: 'mîrzâ : Nobel born' is a slip for 'Noble born', and 'emârat «إمارت»' mixes the Arabic إمارة with the Persian امارت — the Persian spelling has no hamza.\"\n      ,\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%A3%D9%85%D8%B1\",\n        \"https://en.wiktionary.org/wiki/%D8%A3%D9%85%D9%8A%D8%B1\",\n        \"https://www.etymonline.com/word/admiral\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"KLN:26\",\n          \"status\": \"supports\",\n          \"note\": \"KLN_1966.txt leaf 25 (= printed pp. 25-26) carries 'admiral'; KLN_1966.txt l.2451 s.v. 'ameer, amir, n., a Mohammedan ruler. — Arab. amīr, \\\"commander, prince\\\", fr. amara, \\\"he commanded\\\". See emir.' Klein thus supports the root ʾ-m-r 'to command' and the derivative amīr 'commander' exactly as the root box states.\"\n        },\n        {\n          \"ref\": \"FVA:33\",\n          \"status\": \"not_checked\",\n          \"note\": \"FVA = S. M. Nahvi, Farhang-e Vāzhehā-ye ʿArabi dar Fārsi (Dakhil), Tehran 1368/1989. refs_online.json records: 'Searched archive.org, ketabnak, noorlib, web: no digital copy found.' Not accessible.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"amr; mîrzâ; ammâreh; ma'mŭr; emârat\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"All five are Arabic-root material taken into Persian after the 7th-c. conquest, and all five do belong to ʾ-m-r, but they belong to it in different ways. (a) امر amr = Ar. أَمْر ʾamr, the maṣdar/noun of ʾamara, 'order, command; matter, affair' (pl. أوامر ʾawāmir, أمور ʾumūr — both in Nourai's script_extra); borrowed unchanged. (b) امّاره ammāre = Ar. أمّارة ʾammāra, the feminine of the intensive faʿʿāl pattern, 'much-commanding, urging', best known from Qurʾān 12:53 al-nafs al-ʾammāra bi-l-sūʾ 'the soul that incites to evil' — Moʿin glosses it precisely so: 'بسیار امر کننده، اغوا کننده به شرّ'. (c) مأمور maʾmūr is the mafʿūl (passive participle) of ʾamara, 'one who is ordered'; in Persian and Ottoman it specialised to 'official, agent, functionary' (whence مأموریت maʾmūriyyat 'mission'). (d) امارت imārat = Ar. إمارة ʾimāra, the abstract of ʾamīr, 'command, governorship, emirate' (pl. امارات imārāt); Moʿin: '[ع. امارة] … فرمانروایی، فرماندهی، سرداری. ولایت، حوزهٔ زیر فرمان امیر'. Nourai's gloss 'kingdom, state' is loose — 'emirate, governorship' is the sense — and his script «إمارت» is a hybrid: Arabic writes إمارة, Persian امارت. (e) میرزا mīrzā is NOT a direct Arabic form: it is a Persian compound of the shortened Arabic loan میر mīr (< amīr, with aphaeresis of the unstressed initial vowel, already medieval — Richardson lists 'amir (or mir), a commander, governor … prince') plus the Persian patronymic ـزاده -zāda 'born of' (< zādan < Ir. *zā- < PIE *ǵenh₁-, which is why Nourai's chart sends the reader to 'Gene 1'); earlier میرزاد mīrzād 'son of an amīr'. Its gloss should read 'Noble born', not 'Nobel born'.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A3%D9%85%D8%B1\",\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%A3%D9%85%D9%88%D8%B1\",\n            \"https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%B1%D8%B2%D8%A7\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"FVA:33\",\n              \"status\": \"not_checked\",\n              \"note\": \"No digital copy of Nahvi's Farhang-e Vāzhehā-ye ʿArabi dar Fārsi exists (refs_online.json: 'Searched archive.org, ketabnak, noorlib, web: no digital copy found').\"\n            },\n            {\n              \"ref\": \"MON\",\n              \"status\": \"supports\",\n              \"note\": \"MON_part1.txt l.16553 'امارت: IMĀRAT [ع. امارة] (مص‌ل.) امیر شدن. (امص.) فرمانروایی، فرماندهی، سرداری. (اِ.) ولایت، حوزهٔ زیر فرمان امیر؛ ج. امارات'; l.16559 'اماره: [ع. امارة] (ص.) بسیار امر کننده، اغوا کننده به شرّ، برانگیزاننده به بدی'; l.16942 'امیر: [ع. ← میر] (ص.اِ.) کسی که فرمانروا بر قومی باشد… ج. امراء (امرا)'. Moʿin tags every one of them [ع.] = Arabic, as Nourai's arrow requires.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"vol. 1, s.vv. امارت / اماره / امیر (MON_part1.txt ll. 16553, 16559, 16942)\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check. Moʿin's '[ع. ← میر]' at امیر also documents the mīr ~ amīr doublet that underlies میرزا.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 p. ~64, s.v. 'ameer, amir' (KLN_1966.txt l.2451)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Arab. amīr, \\\"commander, prince\\\", fr. amara, \\\"he commanded\\\".'\"\n            },\n            {\n              \"src\": \"RCH\",\n              \"where\": \"Richardson-Johnson, s.v. amir (RCH.txt l.11330)\",\n              \"stance\": \"supports\",\n              \"note\": \"'amir (or mir), A commander, governor, emperor, chief, leader, lord, prince. … The amiru'l umara, prince of princes, a viceroy or governor of a great province' — documents both the mīr shortening (basis of mīrzā) and the amīr al-umarāʾ title.\"\n            },\n            {\n              \"src\": \"DEV\",\n              \"where\": \"Devic 1876, s.v. Emir (DEV.txt l.1261) and l.1748\",\n              \"stance\": \"supports\",\n              \"note\": \"'Emir. Transcription de l'arabe emîr ou amîr, chef… Dans certains pays musulmans, on dit mir; et de là vient le mirza, fils d'émir, monsieur, des Persans' and 'pour emîr-zâdeh, fils d'émir. Emir est arabe, zâdeh est persane' — exactly Nourai's mīrzā analysis, including the Persian half.\"\n            },\n            {\n              \"src\": \"PLA\",\n              \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen (PLA_asbaghi_1988_ia_djvu.txt l.3009)\",\n              \"stance\": \"silent\",\n              \"note\": \"Asbaghi lists only hybrids built ON the Arabic word, e.g. 'ʾamirābūr: \\\"Stallmeister\\\" aus dem ar. ʾamir + pers. …' — i.e. amīr is treated as Arabic, not as a Persian loan into Arabic. Nothing contradicting the direction of Nourai's arrow.\"\n            },\n            {\n              \"src\": \"AFM\",\n              \"where\": \"Addi Shir, Kitāb al-alfāẓ al-fārisiyya al-muʿarraba (AFM.txt), grepped أمير\",\n              \"stance\": \"silent\",\n              \"note\": \"Addi Shir does not list أمير among Persian words arabicised — again consistent with amīr being native Arabic.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Arabic\",\n          \"words\": \"Amîr-al-bahr; Amîr-ar-rahl\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Both phrases are genuine Arabic: أمير البحر ʾamīr al-baḥr 'commander of the sea' (a real Fatimid/Sicilian naval title, still the Persian gloss of 'admiral' — Moʿin s.v. امیرال: '[ع. امیرالبحر] امیرالبحر، دریاسالار. آدمیرال'), and أمير الرحل ʾamīr ar-raḥl 'commander of the transport (fleet)', the title Klein assigns to the officer of the convoy fleet plying between al-Andalus and North Africa. What is disputed is that either phrase is the etymon of Latin amiralis. Nourai's two references disagree with each other (FSD:38 gives amīr-al-baḥr, KLN:26 gives amīr-ar-raḥl), and modern scholarship rejects both. Lokotsch (LKT, s.v. amir) already judged 'Daß die Worte aus amīr-al-baḥr \\\"Befehlshaber der See\\\" entstanden sein sollen, scheint wenig wahrscheinlich'; Devic (1876) called Engelmann's amīr-al-baḥr proposal 'guère admissible' because the Old French forms amiraut, amirant, amiratz show no trace of a dropped noun. The AHD, the OED and Wiktionary now derive Medieval Latin amīrālis from Arabic ʾamīr plus the Latin noun-forming suffix -ālis, or from the constant sequence amīr al- in titles generally — amīr al-umarāʾ 'emir of emirs', the style of the great commanders of Norman Sicily in the mid-12th c., being the usual candidate. Nourai's node is therefore a real Arabic phrase but a superseded etymology.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/admiral\",\n            \"https://www.etymonline.com/word/admiral\",\n            \"https://ahdictionary.com/word/search.html?q=admiral\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:26\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt leaf 25 (printed pp.25-26) s.v. admiral: 'OF. amiral, amiralt (F. amiral), prob. shortened fr. Arab. amīr-ar-rahl, \\\"commander of transport, officer commanding a (transport) fleet\\\" … influenced in form by L. admirari, \\\"to admire\\\". See ameer, amir.' Klein says exactly what Nourai's Amîr-ar-rahl box says (note Klein's own hedge, 'prob.').\"\n            },\n            {\n              \"ref\": \"FSD:38\",\n              \"status\": \"supports\",\n              \"note\": \"FSD_vol1.txt leaf 78 (printed p. ≈ 37-38 with the recorded vol.1 leaf-to-page drift) s.v. admiral: '[OF., <LL. admiralis, amiralis, < Ar. amir-al-bahr, < amir, commander, + al, the, + bahr, sea.]' — verbatim Nourai's Amîr-al-bahr box, and also the source of his Late Latin node.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch 1927, s.v. amir (LKT.txt ll. 373-374)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'Mit ar-rahl \\\"Transport\\\" … wurde amir verbunden zu amīr ar-rahl, dem Titel für den Befehlshaber dieser Flotte' — but then: 'Daß die Worte aus amīr-al-bahr \\\"Befehlshaber der See, des Meeres\\\" entstanden sein sollen, scheint wenig wahrscheinlich.' Lokotsch also reviews and rejects Gebhardt's amīr auwal 'erster Emir'.\"\n            },\n            {\n              \"src\": \"DEV\",\n              \"where\": \"Devic 1876, s.v. Amiral (DEV.txt l.506)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'Engelmann avait supposé que l'al final était l'article précédant un mot tombé depuis, par exemple bahr, mer: amir-al-bahr … Cette explication, au moins quant au mot bahr, ne semble guère admissible, vu qu'on a de nombreux exemples … qui prouvent qu'amiraut, amirant, amiratz [existed]'.\"\n            },\n            {\n              \"src\": \"PHN\",\n              \"where\": \"Pihan, s.v. AMIRAL (PHN.txt l.1668, printed pp. 38-39)\",\n              \"stance\": \"partial\",\n              \"note\": \"Pihan derives amiral from amir 'commandant, chef, émir, dérivé de amar commander' and observes that the truncated amīr al- needs a complement, suggesting amīr al-baḥr is the phrase 'qu'on aurait peut-être dû conserver' — i.e. he treats amīr al-baḥr as the sense-restoring gloss, not as a demonstrated etymon.\"\n            },\n            {\n              \"src\": \"DOZ\",\n              \"where\": \"Dozy, Oosterlingen, s.v. amiral (DOZ.txt ll. 324-352)\",\n              \"stance\": \"partial\",\n              \"note\": \"Dozy starts from 'amir (ook emir uitgesproken), bevelhebber' and discusses how the -al was appended, again without settling on baḥr.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Moʿin vol. 1 s.v. امیرال (MON_part1.txt l.4880)\",\n              \"stance\": \"supports\",\n              \"note\": \"'[ع. امیرالبحر] (اِ.) امیرالبحر، دریاسالار. آدمیرال' — confirms amīr al-baḥr as a live Arabic/Persian naval title, whatever its role in the European etymology.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Late Latin\",\n          \"words\": \"amiralis, admiralis\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The forms are real: Latin texts of the 11th-13th c. show amīrālis, admīrālis, admirallus, admiralius, admiratus, amiratus, amiraldus for a Muslim (later any) commander, and from the 12th c. specifically a naval one. Two corrections to the node. (i) The language label should be Medieval Latin, not Late Latin: these are Norman-Sicilian and crusader-chancery coinages of the 11th-13th c., not Latin of the 3rd-6th c.; Funk & Wagnalls' abbreviation 'LL.', which Nourai copied, is F&W's habitual cover-term for post-classical Latin. (ii) The NOTE '\\\"bahr\\\" or \\\"rahl\\\" has been dropped' is the disputed part (see node #2): the mainstream account today makes -ālis the Latin adjective/noun suffix -ālis attached to amīr, so nothing was 'dropped'. The ad- is secondary throughout: it comes from contamination with Latin admīrārī 'to wonder at, admire' (whence also admirabilis), a change already visible in the Latin forms and reinforced in Middle English.\",\n          \"sources\": [\n            \"https://ahdictionary.com/word/search.html?q=admiral\",\n            \"https://en.wiktionary.org/wiki/admiral\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"FSD:38\",\n              \"status\": \"supports\",\n              \"note\": \"FSD_vol1.txt leaf 78 s.v. admiral: '[OF., <LL. admiralis, amiralis, < Ar. amir-al-bahr …]' — the exact forms and the exact 'LL.' label Nourai reproduces.\"\n            },\n            {\n              \"ref\": \"KLN:26\",\n              \"status\": \"partial\",\n              \"note\": \"Klein's admiral entry (KLN_1966.txt leaf 25) goes straight from Arabic to Old French and does not cite a Latin intermediary at all; he only mentions L. admirari as the source of the -d-. So Klein supports the -d- but not the Late Latin node.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"American Heritage Dictionary online, s.v. admiral\",\n              \"stance\": \"partial\",\n              \"note\": \"'ultimately (partly via Old French amiral) from Medieval Latin admīrālis, alteration (influenced by admīrārī, to wonder at, admire) of amīrālis, ultimately (possibly via Medieval Greek ameras, amerad-) from Arabic ʿamīr, commander … + Latin -ālis, noun suffix.' Confirms the Latin stage and the -d- explanation, but labels it Medieval (not Late) Latin and analyses -al as Latin -ālis.\"\n            },\n            {\n              \"src\": \"DEV\",\n              \"where\": \"Devic, s.v. Amiral (DEV.txt l.506)\",\n              \"stance\": \"supports\",\n              \"note\": \"Lists 'le bas latin admiralius, admirallus, amiraldus, admiratus, amirarius, amirandus, admirandus, admirantius, amireda, amiræus' — a far richer set of Latin forms than the two Nourai gives.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, s.v. Admiral (SKT.txt l.373)\",\n              \"stance\": \"partial\",\n              \"note\": \"'M.E. more often amiral … O.F. amiral … cf. Low L. admi[ralis] … Arab. amīr, a prince … The suffix is due to Arab. amir-al-bahr, prince of the sea' — Skeat keeps a Low Latin stage but sides with baḥr, as Funk & Wagnalls do.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Old French\",\n          \"words\": \"amiral\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old French amiral (also amirail, amirant, amiraut, amiratz, 12th c.) 'Saracen commander; any military commander', taken from the Medieval Latin/Norman-Sicilian amīrālis of node #3 (or directly from the Arabic title in Sicily and the crusader Levant); it is the form behind Old Provençal amiralhs, Portuguese amiralh, Italian ammiraglio, and — with the Arabic article misread into the word — Italian almiraglio, Spanish/Portuguese almirante (remodelled on the Latin present-participle suffix -antem). The 'sea commander' sense is a Mediterranean specialisation of the 12th-13th c.: in the earliest French epic use (Roman d'Alexandre, Roman de Rou) amirant is still simply a Saracen lord.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/admiral\",\n            \"https://en.wiktionary.org/wiki/admiral\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"FSD:38\",\n              \"status\": \"supports\",\n              \"note\": \"FSD_vol1.txt leaf 78 s.v. admiral: '[OF., <LL. admiralis, amiralis …]' — Funk & Wagnalls route the English word through Old French exactly as this node does.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 leaf 25, s.v. admiral\",\n              \"stance\": \"supports\",\n              \"note\": \"'OF. amiral, amiralt (F. amiral) … whence also Port. amiralhs, It. ammiraglio (It. almiraglio and It., Sp. and Port. almirante arose from a confusion of am-, the beginning of the word amīr, with the Arab. art. al-).'\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch, s.v. amir (LKT.txt l.373-374)\",\n              \"stance\": \"supports\",\n              \"note\": \"'pg. amiralh, prov. amiralhs, amirat, afrz. amiré, nfrz. amiral [u. mit falscher etymologischer Beziehung zu lat. admirari] admiral … Die Bedeutung ist überall \\\"Oberbefehlshaber der Flotte\\\".'\"\n            },\n            {\n              \"src\": \"PHN\",\n              \"where\": \"Pihan, s.v. AMIRAL (PHN.txt l.1668)\",\n              \"stance\": \"supports\",\n              \"note\": \"Treats French amiral as the direct continuation of the Arabic title, noting 'les Anglais admiral' among the variants.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"admiral\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle English amiral / admiral (13th c.), from Old French amiral; the 'commander of a fleet' sense is settled in English by the 15th c. (Lord High Admiral, admiral of the fleet). The unetymological -d- is not from Arabic or French but from the pull of Latin admīrārī 'to wonder at' / admīrābilis — Klein, Skeat, Lokotsch, Etymonline and the AHD all say so — helped by the pattern of ad- prefixed Latinate words entering English through law-French. The butterfly names (red admiral, white admiral) are a 17th-c. transfer, probably itself an alteration of 'admirable'.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/admiral\",\n            \"https://ahdictionary.com/word/search.html?q=admiral\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Nourai cites 'AHD' without a page, i.e. the dictionary entry, not the IE-root appendix (the local AHD_watkins1985.txt contains only the root appendix and has no 'admiral'). Checked online: AHD s.v. admiral, '[Middle English amiral, admiral, Muslim military commander, emir, admiral, ultimately (partly via Old French amiral) from Medieval Latin admīrālis, alteration (influenced by admīrārī, to wonder at, admire) of amīrālis … from Arabic ʿamīr, commander … + Latin -ālis, noun suffix.]' — supports the English node and its Old French parent.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Webster's New Twentieth Century, s.v. admiral (WEB_vol1.txt l.3206)\",\n              \"stance\": \"supports\",\n              \"note\": \"'[ME. admiral, admiralle; OFr. admiral; from Ar. amir al, ruler of; sp. influenced by admirable.]' — note that Webster too takes the -d- as spelling influence from admirable.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, s.v. Admiral (SKT.txt l.373)\",\n              \"stance\": \"supports\",\n              \"note\": \"'M.E. more often amiral … O.F. amiral' — confirms the ME form without the d as the older one.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"Funk & Wagnalls vol. 1 leaf 78 (printed p. ≈ 38), s.v. admiral\",\n              \"stance\": \"supports\",\n              \"note\": \"Definitions 1-5 include '5. A Saracen emir, prince, or commander', the original English sense, alongside the naval ranks.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"âdmîrâl\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"آدمیرال ādmīrāl is a modern (19th-20th c.) European loan into Persian, taken with the -d- and therefore from English admiral or Russian адмирал rather than from French amiral (which lost the d) — so Nourai's arrow from the English node is defensible. Moʿin lemmatises it in vol. 1 as ادمیرال and glosses it with the native calque: 'امیرالبحر، دریاسالار، امیرال'. It is thus a round trip: the Arabic ʾamīr that Persian had borrowed in the 7th c. comes back, thirteen centuries later, in Latin-Romance-English dress, and Persian immediately re-glossed it with the Arabic phrase amīr al-baḥr that it had never lost. Persian also uses the calque دریاسالار daryā-sālār for the rank.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/admiral\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:36\",\n              \"status\": \"supports\",\n              \"note\": \"MON_part1.txt l.2396, in the آد- run of vol. 1 (consistent with p. 36; the OCR carries no printed page numbers): 'ادمیرال: ĀDMĪRĀL امیرالبحر، دریاسالار، امیرال.' Moʿin's entry immediately precedes آدمیزاد, i.e. it sits exactly where Nourai's page reference puts it.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"vol. 1 s.v. ادمیرال (l.2396) and s.v. امیرال (l.4880)\",\n              \"stance\": \"supports\",\n              \"note\": \"'امیرال: [ع. امیرالبحر] (اِ.) امیرالبحر، دریاسالار. آدمیرال' — Moʿin's cross-reference shows the two Persian shapes of the word (the Europeanised آدمیرال and the Arabicising امیرال) side by side.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhān-e Qāṭeʿ vol. 1, grepped آدمیرال / ادمیرال\",\n              \"stance\": \"silent\",\n              \"note\": \"Absent, as expected: Borhān-e Qāṭeʿ is a 17th-c. dictionary and cannot contain a 19th-c. European loan.\"\n            },\n            {\n              \"src\": \"RCH\",\n              \"where\": \"Richardson-Johnson 1829 (RCH.txt), grepped admiral/ādmīrāl as a Persian headword\",\n              \"stance\": \"silent\",\n              \"note\": \"No Persian entry — again consistent with a post-1829 borrowing.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-53.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-04T20:00:21.646Z] TOOL RESULT

```
JSON OK
```


## [2026-09-04T20:00:23.594Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb && python3 tools/verify_check.py 53"
}
```


### [2026-09-04T20:00:25.489Z] TOOL RESULT

```
Exit code 2
python3: can't open file '/home/sfmqrb/tools/verify_check.py': [Errno 2] No such file or directory
```


## [2026-09-04T20:00:27.942Z] TOOL CALL #58: Bash

```json
{
 "command": "python3 /home/sfmqrb/git/rishe/tools/verify_check.py 53"
}
```


### [2026-09-04T20:00:29.613Z] TOOL RESULT

```
nodes verified: 9/9
node verdicts: {'plausible': 4, 'confirmed': 4, 'disputed': 1}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'supports': 11, 'partial': 2, 'not_checked': 1}
books consulted: {'supports': 16, 'partial': 6, 'silent': 11, 'contradicts': 2} | by book: {'MON': 5, 'BQT': 3, 'DEV': 3, 'PHD': 2, 'KLN': 2, 'RCH': 2, 'LKT': 2, 'PHN': 2, 'SKT': 2, 'CHEUNG': 1, 'HRN': 1, 'HUB': 1, 'Dehkhoda (vajehyab)': 1, 'NYB': 1, 'FSF': 1, 'PLA': 1, 'AFM': 1, 'DOZ': 1, 'AHD': 1, 'WEB': 1, 'FSD': 1}
```


## [2026-09-04T20:00:46.313Z] AGENT

Written `/home/sfmqrb/git/rishe/data/verification/page-53.json`; `verify_check.py 53` reports 9/9 nodes, no PROBLEM lines.

**Page 53 (book p. 23) — 2 entries, 9 nodes**
- Node verdicts: 4 confirmed, 4 plausible, 1 disputed. Root verdicts: 1 confirmed (Arabic ʾ-m-r), 1 plausible (Pahlavi Âmon).
- Ref checks: 11 supports, 2 partial, 1 not_checked (FVA — no digital copy exists). Consulted 21 books/sources: 16 supports, 6 partial, 11 silent, 2 contradicts.

Key findings:
- **SNS:6 checked from the page image** (archive.org VajnameShayest leaf n19 = printed p. ۶); it supports Nourai's whole first chart verbatim, including the Sanāʾi couplet in the JSON. Transcription saved to `data/verification/sources/refs/ocr/SNS/6.vision.txt`.
- **disputed — A'.m.r #2 `Amîr-al-bahr; Amîr-ar-rahl`**: both phrases are real Arabic, but as the etymon of Lat. amiralis both are rejected today (AHD/OED/Wiktionary: amīr + Lat. -ālis, or amīr al-umarāʾ in Norman Sicily). Lokotsch 1927 and Devic 1876 already called amīr-al-baḥr "wenig wahrscheinlich" / "guère admissible". Nourai's own two refs contradict each other (FSD:38 = baḥr, KLN:26 = raḥl).
- **plausible — root Âmon**: real word, but not a root — āmōn is a deverbal of PIr *ā-maH- 'measure out, prepare' (Cheung 255f.), so the arrows to āmūdan run backwards; Tavoosi documents the simplex only from Farhang-e Jahāngīrī, and MacKenzie/Nyberg have no āmōn.
- **plausible — #1 `âmŭdan; gohar-âmŭd`** (words fine, arrow direction wrong); **#3 `abr-âmŭn` Persian** (no dictionary lemmatises ابرآمون — BQT, MON, FRS, FSF all silent; only the simplex آمون is Persian); **#3 Late Latin `amiralis`** (should be *Medieval* Latin, and the "bahr/rahl dropped" note is the disputed part); **A'.m.r #1** (میرزا is a Persian compound mīr + -zāda, not a direct Arabic derivative; «إمارت» is a hybrid spelling — Arabic إمارة / Persian امارت; gloss "Nobel born" is for "Noble born").
- No `transcription_suspect` items; the JSON matches the chart.
