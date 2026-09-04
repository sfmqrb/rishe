# Verification process log — verify-page-52


## [2026-09-04T19:39:07.761Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 52 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-52.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-52.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-52.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 52` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T19:39:09.254Z] AGENT

I'll start by reading the instructions and the target materials.


## [2026-09-04T19:39:11.454Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:39:11.478Z] TOOL RESULT

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


## [2026-09-04T19:39:11.673Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-52.txt"
}
```


### [2026-09-04T19:39:11.696Z] TOOL RESULT

```
1	=== PDF page 52 (book page 22) ===
2	--- entry 0 ---
3	ROOT Ambhô -> redirect to Ambhi
4	--- entry 1 ---
5	ROOT Ambhô-bhor -> redirect to Ambhi
6	--- entry 2 ---
7	ROOT Ambhô-Bhor -> redirect to Bher 1
8	--- entry 3 ---
9	ROOT Ambhor -> redirect to Ambhi
10	--- entry 4 ---
11	ROOT Amîr -> redirect to A'.m.r
12	--- entry 5 ---
13	ROOT Âmlak -> redirect to Amalaka
14	--- entry 6 ---
15	ROOT [Semitic] A`.m.m : to join, unite  (refs KLN:62)
16	#1 (parent #0) [Arabic] refs=KLN:62 | amm 1 : a great crowd ; amm 2 : father's brother ; ammah : father's sister
17	  #2 (parent #1) [Persian] refs=FVA:285; SAP:442 | amŭ «عمو» : uncle ; âm «عام» : public | extra: عمّه ؛ عموم ، عوام ، تعميم
18	#3 (parent #0) [Hebrew] refs=KLN:62 | am : people ; im : with, together ; Immânŭ-ĕl : God is with us ☞Layh
19	  #4 (parent #3) [French] refs=None | 
20	    #5 (parent #4) [Persian] refs=None | Âmânoel «آمانوئل» : "God is with us" | extra: امانوئل
21	  #6 (parent #3) [English] refs=KLN:515 | Emmanuel, Immanuel
22	--- entry 7 ---
23	ROOT [Semitic] A.m.n : to trust  (refs KLN:61)
24	#1 (parent #0) [Arabic] refs=KLN:61 | a.m.n : to trust ; amin : trustworthy ; îmân : belief
25	  #2 (parent #1) [Persian] refs=FVA:34,35 | amn «امن» : safe ; amânat «امانت» : trusteeship, consignment, deposit ; îmân «ایمان» : (religious) belief, trust ; âmen «آمین» : truly, certainly, accept it (prayer) | extra: امنیّت ، ایمن ، مأمن ، تأمین ؛ مؤمن ؛ امان ، مأمون ، آمینه | NOTE: personal names from this root
26	#3 (parent #0) [Hebrew] refs=KLN:61 | a.m.n : to be trustworthy ; âmen : truly, certainly
27	  #4 (parent #3) [Greek] refs=KLN:61 | amĕn
28	    #5 (parent #4) [Latin] refs=KLN:61 | âmĕn
29	      #6 (parent #5) [English] refs=KLN:61 | Amen : verily
30	
```


## [2026-09-04T19:39:15.705Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-52.json | head -200"
}
```


### [2026-09-04T19:39:15.811Z] TOOL RESULT

```
{
  "pdf_page": 52,
  "book_page": 22,
  "entries": [
    {
      "root": {
        "name": "Ambhô",
        "redirect": "Ambhi"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ambhô-bhor",
        "redirect": "Ambhi"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ambhô-Bhor",
        "redirect": "Bher 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ambhor",
        "redirect": "Ambhi"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Amîr",
        "redirect": "A'.m.r"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Âmlak",
        "redirect": "Amalaka"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "A`.m.m",
        "lang": "Semitic",
        "refs": "KLN:62",
        "gloss": "to join, unite"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:62",
          "words": [
            {
              "translit": "amm 1",
              "gloss": "a great crowd",
              "script": null
            },
            {
              "translit": "amm 2",
              "gloss": "father's brother",
              "script": null
            },
            {
              "translit": "ammah",
              "gloss": "father's sister",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:285; SAP:442",
          "words": [
            {
              "translit": "amŭ",
              "gloss": "uncle",
              "script": "عمو"
            },
            {
              "translit": "âm",
              "gloss": "public",
              "script": "عام"
            }
          ],
          "script_extra": "عمّه ؛ عموم ، عوام ، تعميم",
          "note": null,
          "quote": {
            "text": "محرم راز دل شیدای خود - کس نمی بینم ز خاص و عام را",
            "poet": "Hâfez"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:62",
          "words": [
            {
              "translit": "am",
              "gloss": "people",
              "script": null
            },
            {
              "translit": "im",
              "gloss": "with, together",
              "script": null
            },
            {
              "translit": "Immânŭ-ĕl",
              "gloss": "God is with us",
              "script": null,
              "see": [
                "Layh"
              ]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": null,
          "words": [
            {
              "translit": "Âmânoel",
              "gloss": "\"God is with us\"",
              "script": "آمانوئل"
            }
          ],
          "script_extra": "امانوئل",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:515",
          "words": [
            {
              "translit": "Emmanuel, Immanuel",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "A.m.n",
        "lang": "Semitic",
        "refs": "KLN:61",
        "gloss": "to trust"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:61",
          "words": [
            {
              "translit": "a.m.n",
              "gloss": "to trust",
              "script": null
            },
            {
              "translit": "amin",
              "gloss": "trustworthy",
              "script": null
```


## [2026-09-04T19:39:16.564Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T19:39:16.597Z] TOOL RESULT

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


## [2026-09-04T19:39:20.758Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-52.json'))\nprint(json.dumps(d['entries'][7],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-04T19:39:22.534Z] TOOL RESULT

```
{
 "root": {
  "name": "A.m.n",
  "lang": "Semitic",
  "refs": "KLN:61",
  "gloss": "to trust"
 },
 "nodes": [
  {
   "id": 1,
   "parent": 0,
   "lang": "Arabic",
   "refs": "KLN:61",
   "words": [
    {
     "translit": "a.m.n",
     "gloss": "to trust",
     "script": null
    },
    {
     "translit": "amin",
     "gloss": "trustworthy",
     "script": null
    },
    {
     "translit": "îmân",
     "gloss": "belief",
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  },
  {
   "id": 2,
   "parent": 1,
   "lang": "Persian",
   "refs": "FVA:34,35",
   "words": [
    {
     "translit": "amn",
     "gloss": "safe",
     "script": "امن"
    },
    {
     "translit": "amânat",
     "gloss": "trusteeship, consignment, deposit",
     "script": "امانت"
    },
    {
     "translit": "îmân",
     "gloss": "(religious) belief, trust",
     "script": "ایمان"
    },
    {
     "translit": "âmen",
     "gloss": "truly, certainly, accept it (prayer)",
     "script": "آمین"
    }
   ],
   "script_extra": "امنیّت ، ایمن ، مأمن ، تأمین ؛ مؤمن ؛ امان ، مأمون ، آمینه",
   "note": "personal names from this root",
   "quote": {
    "text": "میکند حافظ دعایی بشنو و آمین بگو - روزی ما باد لعل شکّر افشان شما",
    "poet": "Hâfez"
   }
  },
  {
   "id": 3,
   "parent": 0,
   "lang": "Hebrew",
   "refs": "KLN:61",
   "words": [
    {
     "translit": "a.m.n",
     "gloss": "to be trustworthy",
     "script": null
    },
    {
     "translit": "âmen",
     "gloss": "truly, certainly",
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  },
  {
   "id": 4,
   "parent": 3,
   "lang": "Greek",
   "refs": "KLN:61",
   "words": [
    {
     "translit": "amĕn",
     "gloss": null,
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
   "lang": "Latin",
   "refs": "KLN:61",
   "words": [
    {
     "translit": "âmĕn",
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
   "lang": "English",
   "refs": "KLN:61",
   "words": [
    {
     "translit": "Amen",
     "gloss": "verily",
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  }
 ]
}
```


## [2026-09-04T19:39:22.860Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && grep -n -iE '^(FVA|SAP|KLN)|FVA|SAP' bibliography_raw.txt | head -40; echo ---; python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['KLN','FVA','SAP']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-04T19:39:24.573Z] TOOL RESULT

```
3: TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
12: TABLE IV - Reference Abbreviations (continued...) 32 FIB 33 FNI 34 FRS 35 FSD 36 FSF 37 FVA 38 FVF 39 FVQ 40 FWE 41 FWK 42 GPL 43 HID 44 HJB 45 HRN 46 HUB 47 IEC Pur Davfld, Farhang Iran Bastan, Vol. I, University of Tehran Press 1326 (1947). F. DanaT, Farhang Namhay Irani, Negah Publishers, Tehran 1370 (1991). AsadT Tflsi, Farhang Fors, Kharazmi Press, Tehran 1365 (1986). ^iljjl ^cUj^cLs &gt;^fl&gt;jS Funk and Wagnalla, New Standard Dictionary of the English Language, Funk &amp; Wagnalls Company, New York, 1940. A. H. Noushin, Farhang Shahnameh Ferdowsi, oULS 03I3 - ^-jiy i*La&gt;Li ^^ay Vajheh Namak, Donya Press, Tehran 1363 (1984). S. M. Nahvi, Farhang VSm J-^-i - ^-&gt;jl» j* ^o^ ^gb. 03I3 ^(3 ^S^a,^ Vajhehhay Arabi dar Farsi, Dakhil, TohT Azadi Press 1368 (1989). S. M. A. Emam Shflshtari, ^c ^bj ji ^-"j1* iS^ °j'3 «-fc»j» Farhang Vajhehhay Farsi dar zaban Arabi, Anjoman Asar Melli, No 58, Bahman Press, Tehran, 1347 (1968). A. Jeffrey, The Foreign Vocabulary of the Qur'an, (see VDQ). Oriental Institute, Baroda, Stephen Austin &amp; Sons Press, Great Britain 1938 A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, Warner Books, 1966. R. Dvorak, "Fremdworter im Koran", Doctoral Dissertation, Akademische Buchdruckerei von F. Straub (1884). J.T. Platts and G.S.A. Ranking, A Grammar of the Persian Language, Oxford University Press (1911). B. Bartholomae, Handbuch der Altlranischen Dialekte, Breitkopf &amp;Hartel, Leipzig 1883. H. Yule &amp; A. C. Burnel, Hobson Jobson, A Glossary of Colloqual AngloIndian Words, Oriental Publishers, Delhi 1903-1968. Paul Horn, Grundriss der NeuPersischen Etymology, Verlag von Karl J. Trubner, Strassburg 1893-1974. H. Hubschmann, Persische Studien, Verlag von Karl J. Trubner, Strassburg 1895. Stuart E. Mann, An Indo-European Comparative Dictionary, Helmut Buske Verlag, Hamburg 1987 A-ll 
21: TABLE IV - Reference Abbreviations (continued...) 80 ROE 81 SAP 82 SBK 83 SDQ 84 SHP 85 SIN 86 SKT 87 SLW 88 SNB 89 SNS 90 SOD 91 SOG 92 SOR 93 SPG 94 SYN 95 TAD R. Caliborne, The Roots of English, A Reader's Hanbook of Word Origins, Anchor Books, New York, 1989. A. Sayyah, Farhang Sayyah, Arabic - Persian Dictionary, ^}~&gt; «^a&gt;Js Three volumes, Translation of the Arabic "Al-Monjed" Dictionary, Eslam Publications, Tehran 1368 (1989). M. T. Bahar, Sabk ShenasT - Tarikh Tatawor Nasr Farsi, ^Ls ._£_&gt; Vol I, Tehran 1321 (1942). A. Siddiqi, Studien uber die Persischen Fremdworter im Klassischen Arabisch, Vandenhoeck &amp; Ruprecht, Gottingen 1919. J. T. Shipley, Dictionary of Word Origins, Philosophical Library press, New York 1945. G. Laufer, Sino-Iranica, Chinese Contributions to the History of Civilization in Ancient Iran, Field museum of natural History, publication 201, Anthropological Series, Vol XV, No. 3, Chicago 1919. W. W. Skeat, A Concise Etymological Dictionary of the English Language, Clarenden press, Oxford 1882-1967. W. B. Henning, "Sogdian Loan-words in New Persian", Bulletin of the School of Oriental and African Studies (BSOAS XT939-42) pp 93-106, University of London H. Kowsar, Sang Nebeshteh-ha Sokhan Miguyand, *ujj£~«&gt; Military Public Relations, Iranian Military Press, Tehran (1960's). M. Tavoosi, A Glossary of Shayast Ne Shayast, Shiraz University publications, 1986. B. Ghanb, Sogdian - Persian - English Dictionary, Farhangan Press, Tehran, 1374 (1995). jLw ^uu oV ijij ^imI^I - ^wjli - 
---
KLN {
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
FVA {
 "title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989",
 "kind": "catalog",
 "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)",
 "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": true,
 "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."
}
SAP {
 "title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989",
 "kind": "purchase",
 "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample",
 "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": false,
 "notes": "RE-SEARCH 2026-09: purchase only. Google Books no-view records 4yQPAQAAMAAJ (1977), NoplAAAAMAAJ (1985), HcGipwAACAAJ (2001)."
}
```


## [2026-09-04T19:39:29.693Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^amen,\" KLN_1966.txt KLN_1971.txt; echo ===; grep -n -i \"Immanuel\\|Emmanuel\" KLN_1966.txt KLN_1971.txt | head -20"
}
```


### [2026-09-04T19:39:29.748Z] TOOL RESULT

```
Exit code 1
KLN_1971.txt:13028:amen, interj., n., adv. and tr. v. — OE., fr. Eccles. 
KLN_1971.txt:271345:amen, at the end for 'a'mana' read 'a'mana' . 
(eval):1: == not found
```


## [2026-09-04T19:39:30.371Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==43||NR==44||NR==42' KLN_1966.txt | head -120"
}
```


### [2026-09-04T19:39:32.838Z] TOOL RESULT

```
<persisted-output>
Output too large (34.7KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b3qri90bd.txt

Preview (first 2KB):
r.  L.  admorsus,  pp.  of  admordere, ‘to  bite  into’,  fr.  ad-  and  mordere,  ‘to  bite’.  See mordant.
aimng,  also  algum,  n.,  a  tree  mentioned  in  the
Bible,  prob.  the  sandalwood  (the  first  form  oc¬ curs  I  Kings  10:11-12,  the  second  11  Chron. 2:7  and  9:10-11).  —  Heb.  almuggtm,  resp.  al- gummfm  (pi.).  The  singular  of  these  words  must be  almdgh,  resp.  algdm,  so  that  the  forms almug  and  algum  are  incorrect.  They  should  be replaced  by  almog,  resp.  algom. alnage,  n.,  measurement  by  the  ell.  —  OF.  aul- nage  (F.  aunage),  fr.  aulne,  ‘ell’,  fr.  Frankish *alina,  prop,  ‘forearm’,  which  is  rel.  to  OHG. elina,  OE.  eln,  ‘ell’.  See  ell  and  -age.
Derivative:  alnag-er.  n.
Alnus,  n.,  a  genus  of  plants;  the  alder  (hot.)  — L.  alnus,  cogn.  with  ON.  obi,  OE.  alor,  ‘alder’. See  alder.
alodial,  alodium,  n.  —  See  allodial,  allodium, aloe,  n.  —  L.  aloe,  fr.  Gk.  aX6r),  ‘aloe’,  prob. borrowed  fr.  Heb.  ahaltm,  ahaldth  (pi.),  which are  perhaps  borrowed  fr.  OI.  agaruh,  aguruh, ‘aloewood’,  these  latter  being  prob.  of  Dravid- ian  origin.  Cp.  agalloch. aloetic,  adj.  containing,  or  of  the  nature  of,  aloes ; n.,  an  aloetic  medicine.  —  Formed  with  suff. -etic  fr.  Gk.  aXot],  ‘aloe’.  See  aloe, aloft,  adv.  —  ON.  a  lopt,  ‘in  the  air’,  whence  arose the  meaning  ‘on  high’.  See  a-,  ‘on’,  and  loft, aloin,  n.,  a  bitter  crystalline  substance  (chem.)  — Formed  fr.  aloe  with  chem.  suff.  -in;  so  called because  it  is  obtained  from  the  aloe, aloisiite,  n.,  a  hydrous  subsilicate  of  calcium, ferrum,  magnesium  and  sodium  (mineral.)  , Named  after  Prince  Luigi  (Latinized  into  Aloi- sius)  Amedeo  of  Savoy,  Duke  of  the  Abruzzi. For  the  ending  see  subst.  suff.  -ite. alone,  adj.  —  ME.  al  one ,  ‘all  alone  ,  fr.  al,  all , and  one,  fr.  OE.  an,  ‘one,  alone  .  Cp.  Du.  alleen, MHG.  al
...
</persisted-output>
```


## [2026-09-04T19:39:39.284Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"amen,\" KLN_1966.txt | head -20; echo \"=== ff index\"; python3 - <<'EOF'\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=p.split('\\f')\nfor i,pg in enumerate(pages):\n    if 'amen,' in pg and 'ament' in pg:\n        print('leaf',i)\nEOF"
}
```


### [2026-09-04T19:39:41.314Z] TOOL RESULT

```
1925:agent,  adj.  —  L.  agens,  gen.  agentis,  pres.  part, of  agere,  ‘to  set  in  motion,  drive,  lead,  conduct, guide,  govern ;  to  do,  act’,  whence  agmen,  ‘army, troop,  band,  multitude’,  lit.  that  which  is  lead’, fr.  I.-E.  base  *ag-,  ‘to  drive,  lead,  act,  do’,  whence also  Gk.  dyeiv,  ‘to  lead,  guide,  drive,  carry off’,  dytveiv,  ‘to  lead,  bring’,  aycov,  ‘assembly, contest  in  the  games’,  xycovtx,  ‘struggle  for  vic¬ tory,  anguish,  agony’,  Aycoyd?,  ‘leader’,  aywyfj, ‘a  carrying  away,  a  leading’,  OI.  ajati,  ‘drives’, ajirah,  ‘moving,  active’,  Avestic  aza'ti,  ‘drives’, Toch.  A  dk-,  B  &k-,  ‘to  travel,  lead’,  Arm.  acem, ‘1  lead,  bring",  ON.  aka,  ‘to  drive’.  Cp.  agent, n.  Cp.  also  abigeat,  acorn,  acre,  act,  action,  acti¬ vate,  actor,  actress,  actuate,  Agelaius,  agenda, agile,  agitate,  agminate,  -agogue,  agonist,  ago¬ nize,  agony,  agrarian,  agrestic,  agriculture,  agrio-, agro-,  agronomy,  Agrostis,  Agyieus,  aisle,  ala, ambages,  ambagious,  ambassador,  ambiguous, ament,  anagogy,  antagonist,  apagoge,  assay, Auriga,  axilla,  axiom,  axis,  axle,  cache,  chora- gus,  clarigation,  coact,  coagulate,  cogent,  cogi¬ tate,  demagogic,  deuteragonist,  embassy,  epact, essay,  exact,  examen,  exigent,  exiguous,  exility, indagate,  intransigent,  isagoge,  paragoge,  para- gonite,  pedagogue,  pilgrim,  prodigal,  protago¬ nist,  react,  redact,  remex,  stavesacre,  strategy, synagogue,  transact,  tritagonist,  and  the  second element  in  castigate,  clarigation,  fastigiate,  fu¬ migate,  fustigate,  levigate,  litigate,  mitigate,  na¬ vigate,  objurgate,  purge,  variegate, agent,  n.  —  F.,  in  the  sense  of  ‘acting  force’,  fr. ML.  agens,  in  the  sense  of  ‘acting  person’,  fr. It.  agente;  both  these  words  derive  fr.  L.  agens, gen.  agentis,  pres.  part,  of  agere.  See  agent,  adj. agential,  adj.  —  Formed  fr.  agency  with  suff. -ial.
2191:Alhagi,  n.,  a  genus  of  plants  of  the  pea  family (bot.)  —  ModL.,  fr.  Arab,  al-haj,  ‘the  camel’s thorn’,  which  is  rel.  to  Talmudic  Heb.  heghd, Aram,  heghd,  heghethd,  Syr.  hagh*thd,  of  s.m. The  primary  meaning  of  these  nouns  is  ‘thorns forming  a  hedge’,  from  the  Semitic  base  h-y-g, h-w-g,  ‘to  surround,  hedge,  fence  in’.  See H.L.  Fleischer  in  his  Contributions  to  Jacob Levy’sNeuhebraischesundChaldaischesWorter- buch  fiber  die  Taimudim  und  Midraschim,  1, p.556,  and  Immanuel  Low,  Aramaische  Pflan- zennamen,  Leipzig,  1881,  pp.  145-47.
2337:alpenstock,  n.,  a  long  iron-pointed  staff  used  for climbing  mountains.  —  G.,  lit.  ‘Alp  stick’,  com¬ pounded  of  Alpen,  ‘the  Alps’,  and  Stock,  ‘stick’. See  alp,  ‘a  high  mountain’,  and  stock, alpha,  n.,  name  of  the  1st  letter  of  the  Greek  al¬ phabet.  —  L.,  fr.  Gk.  diXtpot,  fr.  Hcb.-Phoen. dleph;  see  aleph.  The  final  a  was  added  because a  Greek  word  cannot  end  with  a  9;  cp.  beta, gamma,  delta,  eta,  theta,  iota,  kappa,  lambda, sigma.  See  Theodor  Noldeke,  Die  semitischen Buchstabennamen,  in  Beitrage  zur  semitischen Sprachwissenschaft,  Strassburg,  1904,  PP-  '34 and  135,  and  Eduard  Schwyzer,  Griechische Grammatik,  Munchen,  1939,  I,  140  y. alphabet,  n.  —  L.  alphabetum,  compounded  of Gk.  &X<pa  and  (iTjxx,  names  of  the  first  two letters  of  the  Greek  alphabet.  See  alpha  and beta.
2450:ambush,  n.  —  OF.  embusche  (F.  embuche),  back formation  fr.  embuscher.  See  prec.  word, arnbushment,  n.  —  OF.  embuschement,  fr.  em¬ buscher.  See  ambush,  v.,  and  -ment. ameen, n,,  official,  inspector  (Anglo-Ind.)  — Hind. amin,  fr.  Arab,  amtn,  lit.  ‘trustworthy’,  fr.  amina, ‘he  was  steady,  firm,  trustworthy’  (whence  A'ma- na,  ‘he  believed’);  rel.  to  Heb.  amen,  ‘verily, truly’.  See  amen.
2455:amellus,  n.,  name  of  a  flower.  —  L.,  ‘the  purple Italian  starwort',  a  word  of  Gaulish  origin  (see G.-D.Dottin,  La  langue  gauloise,  p.226).  The derivation  of  this  word  from  the  river  name Mella,  as  suggested  by  Servius  in  his  commen¬ tary  on  Virgil  4,  271,  is  folk  etymology, amen,  interj.,  n.,  adv.  and  tr.  v.  —  OE.,  fr.  Eccles. L.  amen,  fr.  Eccles.  Gk.  ap.7)v,  fr.  Heb.  amen, ‘verily,  truly,  certainly’,  from  stem  a-m-n,  ‘to  be trustworthy,  confirm,  support’,  whence  also aman,  ‘he  supported,  nourished’,  heemln,  ‘be believed’,  emundh,  ‘firmness,  fidelity’,  umndm , omndm,  ‘verily,  truly,  emith  (for  *ementh),  sta¬ bility,  truth’.  Cp.  the  related  Syr.  ammin,  ‘strong, enduring’,  Aram,  hemanuthd,  Syr.  haymanuthd, ‘faithfulness,  truth’,  Arab,  dmina,  ‘he  was  safe’.
2508:Amomum,  n.,  a  genus  of  plants  of  the  ginger  fa¬ mily  ( bot .)  —  L.  amomum ,  ‘a  spice  plant’,  fr. Gk.  apcopov,  which  is  of  Sem.  origin.  Cp.  Mish- naic  Heb.  hdm&m,  of  s.m.,  and  Syr.  hamamd, Arab,  hamdma,  ‘a  spice  plant’,  which  prob.  de¬ rive  from  stem  i h-m-m,  ‘to  be  warm  .  See  Imma¬ nuel  Low.  Aramaische  Pflanzennamen,  Leipsic,
5115:blame,  tr.  v.  —  ME.  blamen,  fr.  OF.  blasmer  (F. blamer),  fr.  VL.  blastemare,  ‘to  blame’,  which  is formed — prob.  under  the  influence  of  L.  aesti-
5368:bore,  tr.  and  intr.  v.,  to  pierce.  —  ME.  borien,  fr. OE.  borian,  rel.  to  ON.  bora,  Swed.  borra,  Dan. bore,  OS.,  OHG.  boron,  MDu.,  Du.  boren, MHG.  born,  G.  bohren,  fr.  I.-E.  base  •bher-,  ‘to cut  with  a  sharp  point;  to  bore,  pierce’,  whence also  Arm.  beran,  ‘mouth’  (prop,  ‘opening’),  Gk. (papaco,  <pap6ca,  ‘I  plow*,  epapo?,  ‘plow  ,  ipapay^, ‘cleft,  chasm’,  pdpuyS,  ‘throat,  chasm,  gulf’,  L. ferire,  ‘to  strike,  smite’,  forare,  ‘to  bore,  pierce’, OSlav.  barjg,  brati  (for  *bor-ti),  ‘to  strike,  fight’, Lith.  bdras,  Lett,  bars,  ‘swath’,  Lith.  burna, ‘mouth’,  Russ,  borona,  ‘harrow’,  Mir.  bern, berna,  ‘cleft,  opening’.  Alb.  brims,  ‘hole’.  Cp. bark,  ‘rind  of  a  tree’,  barranca,  barrow,  ‘castrated boar',  board,  ‘table,  plank’,  board,  ‘side  of  a ship’,  Boris,  brackish,  broom,  burin,  foralite, foramen,  interfere,  perforate,  pharynx,  and  the second  element  in  Dukhobors.
7926:clin-,  form  of  clino-  before  a  vowel, clinamen,  n.,  inclination;  bias.  —  L.  clinamen, fr.  -clinare, ‘to bend,  turn’,  which  iscogn.  with  Gk. xXfveiv,  ‘to  cause  to  slope,  bend’.  See  clinical, clinandrium,  n.,  a  cavity  in  the  top  of  the  column of  certain  orchids,  in  which  the  anther  rests ( bot .)  —  ModL.,  compounded  of  Gk.  xXfvrj, ‘bed’,  and  avr;p,  gen.  xvSpo?,  ‘man’,  used  in  its modern  botanic  sense  ‘stamen’.  Sec  clinical  and andro-.
7932:clinical,  adj.  - —  Formed  with  adj.  suff.  -al  fr.  L. clinicus,  fr.  Gk.  xXmx6s,  ‘a  physician  who  at¬ tends  patients  in  their  beds’,  from  the  adjectiva xXIvixo?,  ‘pertaining  to  a  bed’,  fr.  xXfvtr),  ‘bed’, which  is  rel.  to  xXtueiv,  ‘to  cause  to  slope,  slant, incline’,  xXlptoc,  ‘inclination,  slope,  region’,  xXt- |xa£,  ‘ladder’,  xXtpaxTrip,  ‘rung  of  a  ladder’, xXTt6<;,  xXecru?,  ‘slope,  hillside’,  fr.  I.-E.  base *klei-,  ‘to  incline,  lean’,  whence  also  L.  -clinare (with  the  exception  of  the  pp.  clinatus,  occur¬ ring  only  in  compounds),  ‘to  bend,  turn’,  clivus, ‘slope,  hill’,  clitellae  (dimin.  of  *clitra,  for *kleitrd),  ‘a  packsaddle’,  Umbr.  kletram  (acc.), ‘litter,  bier’,  OI.  srayati,  ‘leans’,  sritah,  ‘leaning’, Lith.  slyti,  ‘to  slope’,  slieti,  ‘to  lean’,  slaitas, ‘declivity,’  sleivas,  ‘bandy-legged’,  Ofr.  cloin, ‘crooked,  wrong’,  Mir.  clithar,  ‘hedge’,  W. dedren,  ‘enclosure’,  Mir.  cle,  W.  cledd,  Co. cledh,  Bret,  kleiz,  ‘left’,  lit.  ‘slanting,  oblique’, Mir.  fo-chla ,  W.  go-gledd,  ‘north’,  lit.  ‘left’  (for sense  development  cp.  Heb.  semdl,  Arab. sham'dl,  shimdl,  ‘left;  north’),  Arm.  learn  (gen. leriri),  ‘mountain’,  Goth,  hlaiw,  ‘grave,  tomb’, OE.  hlxw,  hlaw,  ‘mound,  hill;  cave’,  OE.  hlinian, ‘to  lean’.  See  lean,  ‘to  incline’,  and  cp.  words there  referred  to.  Cp  also  acclivity,  aclinic,  anti¬ clinal,  clement,  client,  climacterium,  climate, climax,  clinamen,  clino-,  clitellum,  clition,  clivus, declension,  decline,  declivity,  diclinous,  enclitic, heteroclite,  incline,  isoclinic,  microcline,  mono- clinal,  pericline,  recline,  synclinal,  triclinium. I.-E.  base  *klei-  is  an  enlargement  of  base  *kel-, for  the  derivatives  of  which  see  heel,  ‘to  lean’ Derivative:  clinical-ly,  adv clink,  intr.  and  tr  v.  —  Prob.  fr.  MDu.  clinken (Du.  klinken),  ‘to  sound,  tinkle’,  which  is  rel.  to MLG.  klingen[  whence  ON.  klingia,  Dan .klinge, Swed.  klinga],  OHG.klingan,MHG.,G.klingen, ‘to  sound,  tinkle’;  of  imitative  origin.  Clink  is related  to  clank;  for  the  thinning  of  a  to  i  cp. click  and  clack.  Cp.  dough.
8913:contaminate,  tr.  v.,  to  render  impure.  —  L.  con- tdminatus,  pp.  of  contamindre,  ‘to  bring  into contact,  mingle,  blend  together;  to  defile,  stain, contaminate’,  fr.  *contamen,  gen.  *contdminis, ‘contagion’,  which  stands  for  *con-tag-s-men and  is  formed  fr.  con-  and  *tag-,  the  stem  of  tan-
10049:Cycas,  n.,  a  genus  of  trees  (hot.)  —  ModL.,  fr. Gk.  x'ixac,  erroneously  written  for  xoixap, acc.  pi.  of  x6l5,  ‘the  doom  palm’,  which  is  a foreign  word  of  unknown  origin, cycl-,  form  of  cyclo-  before  a  vowel, cyclamen,  n.  —  ML.  and  ModL.,  fr.  Gk.  xuxXa- pTvop,  fr.  x'ixXop,  ‘circle’.  See  cycle.
10591:Derivative:  defamatori-ly ,  adv. defame,  tr.  v.,  to  calumniate,  asperse.  —  ME. defamen,  diffamen,  fr.  OF.  diffamer,  fr.  L.  diffa¬ mare,  ‘to  spread  an  evil  report,  defame’,  fr. dis-  and  fdma,  ‘report,  rumor’.  See  fame. Derivatives:  defam-ed,  adj.,  defam-er,  n.  de- fam-ing-ly,  adv.
12474:duramen,  n.,  the  hard  wood  in  the  center  of  the tree  trunk,  the  heartwood  ibot.)  —  L.  duramen, ‘hardness;  a  hardened  vinebranch’,  from  the stem  of  durare,  ‘to  harden’.  See  dure,  v.,  and -men.
12477:dure,  adj.,  hard;  severe  (archaic).  —  F.  dur,  fern. dure,  fr.  L.  durus,  'hard,  rough,  rude’,  prob. dissimilated  fr.  *dru-ros,  for  *dreu-ros,  and  lit. meaning  ‘as  hard  as  wood’,  fr.  I.-E.  base  *de- rew(o)-,  *drew(o)-,  *dru-,  ‘tree,  wood’,  whence also  Gk.  Spue,  ‘oak,  tree’,  86pu,  ‘stem,  tree,  beam, shaft  of  a  spear,  spear’,  OI.  dru-,  ‘wood,  wooden vessel',  ddru,  ‘wood’,  OE.  treo,  treow,  ‘tree, wood’.  See  tree  and  cp.  words  there  referred  to. Cp.  also  dour,  durable,  durain,  duralumin,  dura mater,  duramen,  durance,  duration,  duress,  dur¬ ing,  endure,  indurate,  obdurate,  perdure. dure,  intr.  v.,  to  last  (obsol.  or  poetic).  —  F.  durer, fr.  L.  durare,  ‘to  harden;  to  continue,  last’,  fr. durus,  ‘hard’.  See  dure,  adj. duress,  n.,  1)  imprisonment;  2)  compulsion.  — ME.  duresse,  fr,  obsol.  F.  duresse,  fr.  L.  duritia, ‘hardness,  severity,  austerity’,  fr.  durus.  See dure,  adj.,  and  -ess. durgah,  n.  —  See  dargah.
12540:Derivatives:  early,  adj.,  earli-ness,  n. earn,  tr.  v.  —  ME.  ernien,  ernen,  fr.  OE.  earnian, ‘to  deserve,  earn’,  rel.  to  OHG.  amen,  arnon, ‘to  reap’,  OE.  ern,  OHG.  aran,  arn,  G.  Ernte, ‘harvest’,  Goth,  asans,  ‘harvest,  summer’,  ON. bnn  (for  *aznu),  ‘work  in  the  field’,  and  cogn. with  OSlav.  jeseni,  Russ,  osen’,  OPruss.  assanis, ‘autumn’.
13710:etamine,  n.,  a  dress  fabric  of  cotton,  worsted  or silk.  —  F.  etamine,  fr.  OF.  estamine,  fr.  VL. *staminea,  fern,  of  the  Latin  adj.  stamineus, ‘made  of  threads’,  fr.  stamen,  gen.  staminis ‘warp  in  the  upright  loom,  thread’.  See  stamen. 6tape,  n.,  1)  a  halting  place  for  troops;  2)  a  day’s march.  —  F.,  ‘stage  of  journey,  halting  place, distance  between  two  halting  places’,  fr.  OF. estaple,  fr.  MDu.  staple,  ‘storehouse’.  See  staple, etat,  n.,  state.  —  F.,  fr.  L.  status,  prop,  ‘mode  of standing’.  See  state  and  cp.  words  there  re¬ ferred  to.
13910:essay,  examen,  examine,  exigent,  exiguous, exility.
13915:Derivatives:  exalt-ation,  n.,  exalt-ed,  adj., exalted-ly,  adv.,  exalted-ness,  n.,  exalt-er,  n. exam,  n.  —  Colloq.  abbreviation  of  examination, examen,  n.,  examination.  —  L.  examen.  See examine.
14846:flam,  n.,  sham,  trick.  —  Shortened  fr.  flimflam, flam,  n.,  a  drumbeat.  —  Of  imitative  origin, flambe,  adj.,  decorated  by  irregularly  splashed glaze.  —  F.,  pp.  of  flamber,  ‘to  singe,  blaze’,  fr. OF.  flambe,  ‘flame’,  which  is  a  back  formation fr.  flamble.  See  next  word, flambeau,  n.,  a  large  torch.  —  F.,  fr.  OF.  flamble, ‘flame’,  fr.  L.  flammula,  ‘a  little  flame’,  dimin.  of flamma,  ‘flame’.  See  flame, n.,  and  cp.  prec.  word, flamboyance,  flamboyancy.  n.  —  Formed  from next  word  with  suff.  -ce,  resp.  -cy. flamboyant,  adj.,  characterized  by  flamelike tracery  (archil.)  —  F.,  pres.  part,  of  flamboyer, ‘to  flame’,  fr.  OF.  flambe.  See  flambe  and  -ant. Derivative:  flamboyant-ly,  adv. flame,  n.  —  ME.  flamme,  fr.  OF.  flame,  flamme (F.  flamme),  fr.  L.  flamma,  ‘blaze,  flame’,  which stands  for  *flagma  and  is  rel.  to  flagrare,  ‘to blaze,  glow,  bum’.  See  flagrant  and  cp.  words, there  referred  to.  Cp.  also  dimmer  and  the  se¬ cond  element  in  oriflamme. flame,  intr.  v.  —  ME.  flamen ,  fr.  OF.  flamer,  ‘to flame'  (whence  F.  flammer,  ‘to  singe’),  fr.  L. flammare,  ‘to  flame’,  fr.  flamma.  See  flame,  n. Derivatives:  flam-ed,  adj .,  flam-er,  n.,  flam-ing, adj.,  flam-ing-ly ,  adv.,  flam-y,  adj. flamen,  n.,  a  priest  devoted  to  the  service  of  one particular  deity  (Roman  mythol.)  —  L.  flamen, which  prob.  stands  for  *bhladmen,  and  is  cogn. with  Goth,  biotan,  ‘to  worship’,  ON.  biota,  OE. blotan,  OHG.  bluo3an,  ‘to  sacrifice’, flamenco,  n.,  dancing  style  of  the  gypsies  of  An¬ dalusia.  —  Sp.,  ‘Flemish;  gypsy’,  fr.  MDu. Flaming .  See  Fleming.
=== ff index
leaf 31
leaf 44
leaf 169
leaf 215
leaf 328
leaf 345
leaf 470
leaf 572
leaf 668
leaf 732
leaf 798
leaf 831
```


## [2026-09-04T19:39:54.494Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (44,45):\n    print('======== LEAF',i)\n    print(p[i][:6000])\nEOF"
}
```


### [2026-09-04T19:39:56.280Z] TOOL RESULT

```
======== LEAF 44
like  food’.  Cp.  Arab.  * unbar  (pronounced  ‘d/n- bar’),  ‘ambergris’,  and  see  amber.  See  also nectar.
Derivatives:  ambrosi-ac,  adj.,  ambrosial,  adj. (q.v.),  ambrosi-an,  ambrosi-ate,  adjs. ambrosial,  adj.  —  Coined  by  Milton  fr.  L.  am¬ brosius,  fr.  Gk.  dp(3p6crio<;.  See  ambrosia  and  adj. suff.  -ai.
ambry,  n.,  cupboard;  closet  (archaic).  —  ME.  al- mary,  aumbry,  fr.  OF.  almarie,  armarie  (F.  ar- moire),  ‘cupboard’,  fr.  L.  armarium,  ‘closet, chest’,  lit.  ‘a  place  where  arms  are  kept’,  fr.  arma, gen.  armorum,  ‘arms;  tools,  instruments,  uten¬ sils’.  Cp.  It.  and  Sp.  armario,  OProveng.  armari, and  see  arm,  ‘weapon’,  armory, ambsace,  n.,  double  aces.  —  OF.  ambes  as,  fr.  L. ambas,  fern.  acc.  of  ambo,  ‘both’,  and  L.  as, ‘unity,  unit’.  See  ambi-  and  ace. ambulance,  n.  — -  F.,  fr.  earlier  hopital  ambulant lit.  ‘a  walking  hospital’,  fr.  L.  ambulans  gen. -antis.  See  next  word  and  -ce. ambulant,  adj.  —  L.  ambulans,  gen.  -antis,  pres, part,  of  ambulare.  See  next  word  and  -ant. ambulate,  intr.  v.,  to  move  about,  walk.  —  L. ambulat-(um),  pp.  stem  of  ambulare,  ‘to  go about,  walk’.  See  amble  and  verbal  suff.  -ate and  cp.  circumambulate,  perambulate, ambulation,  n.  —  L.  ambulatio,  gen.  -onis,  fr.  am- bulat-(um),  pp.  stem  of  ambulare.  See  prec. word  and  -ion.
ambulatory,  adj.  —  L.  ambulatbrius,  ‘movable’, fr.  ambu!at-(um)  pp.  stem  of  ambulare.  See  am¬ bulate  and  adj.  suff.  -ory. ambulatory,  n.  —  ML.  ambulatorium,  a  noun formed  fr.  L.  ambulatbrius,  ‘movable’.  See  prec. word  and  subst.  suff.  -ory. am  bury,  n.  —  See  anbury, ambuscade,  n.,  ambush.  —  F.  embuscade,  Galli¬ cized  fr.  It.  imboscata  (under  the  influence  of OF.  embuscher),  lit.  ‘a  hiding  in  the  bush’,  fr. imboscare,  fr.  ML.  imboscare,  ‘to  lie  in  the  bush’. See  next  word  and  -ade.
Derivatives:  ambuscade,  tr.  and  intr.  v.,  am- buscad-er,  n.
ambush,  tr.  v.  —  OF.  embuscher  (F.  embucher ),  fr. ML.  imboscare,  ‘to  lie  in  the  bush’,  fr.  im-,  ‘in, within’,  and  boscus,  ‘bush’.  See  bush,  ‘shrub’, and  cp.  prec.  word.  Cp.  also  boscage,  bosky. Derivatives:  ambush,  n.  (q.v.),  ambush-er,  n., arnbushment  (q.v.)
ambush,  n.  —  OF.  embusche  (F.  embuche),  back formation  fr.  embuscher.  See  prec.  word, arnbushment,  n.  —  OF.  embuschement,  fr.  em¬ buscher.  See  ambush,  v.,  and  -ment. ameen, n,,  official,  inspector  (Anglo-Ind.)  — Hind. amin,  fr.  Arab,  amtn,  lit.  ‘trustworthy’,  fr.  amina, ‘he  was  steady,  firm,  trustworthy’  (whence  A'ma- na,  ‘he  believed’);  rel.  to  Heb.  amen,  ‘verily, truly’.  See  amen.
ameer,  amir,  n.,  a  Mohammedan  ruler.  —  Arab. amtr,  ‘commander,  prince’,  fr.  amara,  ‘he  com¬ manded'.  See  emir.
Ameiurus,  n.,  a  genus  of  catfishes  ( ichthyol .)  — ModL.,  formed  fr.  priv.  pref.  a-  and  Gk.  ;j.eiou- po?,  ‘curtailed’,  which  is  compounded  of  the stem  of  psitov,  ‘smaller,  less’,  and  oops,  ‘tail’. See  meiosis  and  uro-,  ‘tail-’, amelcorn,  n.  —  G.  Amelkorn,  compounded  of Amel,  ‘starch’,  and  Korn,  ‘grain’ .  Thefirst  element derives  fr.  L.  amylum,  fr.  Gk.  a^tuXov,  ‘starch’ ; see  amyl.  The  second  element  is  rel.  to  E.  corn, ‘grain’  (q.v.)  Cp.  emmer.
Amelia,  fern.  PN.  —  A  Teutonic  name  lit.  mean¬ ing  ‘laborious’.  Cp.  ON.  ama,  ‘to  trouble’,  and Amal,  name  of  the  ruling  family  of  the  Ostro¬ goths.  The  name  was  confused  later  with  the name  of  the  Roman  gens  Aemilia  (see  Emily). ameliorate,  tr.  v.,  to  make  better;  intr.  v.,  to  be¬ come  better.  —  Formed  with  verbal  suff.  -ate fr.  F.  ameliorer,  which  is  refashioned  after  L. melior,  ‘better’,  fr.  OF.  ameillorer,  fr.  OF.  meil- lor  (whence  F.  meilleur),  ‘better’,  fr.  L.  melio- rem,  acc.  of  melior,  ‘better’.  See  meliorate. Derivatives:  amelioration  (q.v.),  amelior-at-ive, adj.,  amelior-at-or ,  n.
amelioration,  n.,  betterment,  improvement.  —  F. amelioration,  fr.  ameliorer.  See  prec.  word  and -ion.
amellus,  n.,  name  of  a  flower.  —  L.,  ‘the  purple Italian  starwort',  a  word  of  Gaulish  origin  (see G.-D.Dottin,  La  langue  gauloise,  p.226).  The derivation  of  this  word  from  the  river  name Mella,  as  suggested  by  Servius  in  his  commen¬ tary  on  Virgil  4,  271,  is  folk  etymology, amen,  interj.,  n.,  adv.  and  tr.  v.  —  OE.,  fr.  Eccles. L.  amen,  fr.  Eccles.  Gk.  ap.7)v,  fr.  Heb.  amen, ‘verily,  truly,  certainly’,  from  stem  a-m-n,  ‘to  be trustworthy,  confirm,  support’,  whence  also aman,  ‘he  supported,  nourished’,  heemln,  ‘be believed’,  emundh,  ‘firmness,  fidelity’,  umndm , omndm,  ‘verily,  truly,  emith  (for  *ementh),  sta¬ bility,  truth’.  Cp.  the  related  Syr.  ammin,  ‘strong, enduring’,  Aram,  hemanuthd,  Syr.  haymanuthd, ‘faithfulness,  truth’,  Arab,  dmina,  ‘he  was  safe’.
amenable
amnic
62
63
amuna,  ‘he  was  faithful’,  d'mana,  ‘he  believed’, amtn,  ‘faithful’.  Cp.  ameen.  Cp.  also  mammon, amenable,  adj.,  answerable;  willing;  submissive. —  Formed  with  suff.  -able  fr.  F.  amener,  ‘to lead,  or  bring  up,  to’,  fr.  a,  ‘to’  (see  a),  and mener,  ‘to  lead’,  fr.  VL.  minare,  ‘to  drive  (ani¬ mals)  by  shouting’,  fr.  L.  minari,  ‘to  threaten’. The  orig.  meaning  of  L.  minari  has  survived  in Rum.  mana,  ‘to  threaten’.  See  menace  and  -able. Derivatives :  amenabil-ity,  n.,  amenable-ness,  n., amenabl-y,  adv.
amend,  tr.  and  intr.  v. — OF.  (=  F.)  amender ,  fr.  L. emendare,  ‘to  correct,  emend’,  with  change  of suff.  (cp.  the  same  change  of  suff.  in  It.  ammen- dare  and  OProven?.  amendar);  fr.  e-,  ‘out  of’ (see  e-)  and  menda,  'defect,  blemish’,  which  is cogn.  with  OI.  mindi,  ‘physical  blemish
======== LEAF 45
ddle’,  fr.  on  (see  a-,  ‘on’),  and  middan, dat.  sing.  masc.  of  midde,  adj.  See  mid  and  cp. amidst.
amide,  amid,  n.,  a  compound  obtained  by  re¬ placing  one  hydrogen  atom  in  ammonia  by  an element  or  radical  (chem.)  —  F.  amide,  coined by  the  French  chemist  Charles-Adolphe  Wurtz ( 1 8 1 7-84)  from  the  first  syllable  of  ammonia  and suff.  -ide,  -id.
amidin,  amidine,  n.,  solution  of  starch  in  hot water  (chem.)  —  Formed  fr.  F.  amidon,  ‘starch’, fr.  ML.  amidum,  fr.  L.  amylum,  fr.  Gk.  aguiXov, ‘starch’.  See  amyl,  ‘starch’,  and  chem.  suff. -ine,  -in.
amido-,  combining  form  meaning  ‘containing the  radical  NH,  and  an  acid  radical’  (chem.)  — Fr.  amide.
amidogen,  n.,  the  hypothetical  univalent  radical NH2  (chem.)  —  Coined  fr.  amido-  and  -gen. amidst,  prep.  —  Formed  with  excrescent  -t  fr. ME.  amiddes  (which  was  formed  with  adv.  gen. suff.  -s  fr.  amidde,  see  amid,  prep.)  For  the  -t cp.  against,  amongst,  betwixt,  whilst. amine,  amin,  n.,  a  compound  obtained  by  re¬ placing  hydrogen  atoms  of  ammonia  by  hydro¬ carbon  radicals  (chem.)  —  Coined  from  the  first syllable  of  ammonia  and  chem.  suff.  -ine.  Cp. amide  and  vitamin.  Cp.  also  imine. amino-,  combining  form  meaning  ‘pertaining  to, or  containing,  the  radical  NH2’  (chem.)  —  See prec.  word  and  cp.  deaminate. amir,  n.  —  See  ameer.
amiss,  adv.  and  adj.  —  Formed  fr.  a-,  ‘on’,  and miss,  ‘failure’.
amity,  n.,  friendship.  —  F.  amilie,  fr.  OF.  amistie, fr.  VL.  *amicitatem,  acc.  of  *amicitas,  corre¬ sponding  to  L.  amicitia,  ‘friendship’,  fr.  amicus, ‘friend’,  which  is  rel.  to  amare,  ‘to  love’.  See amative  and  cp.  enmity.
ammeter,  n.,  an  instrument  for  measuring  the strength  of  electric  currents.  —  Shortened  fr. ampere-meter.  See  ampere  and  meter,  ‘poetical rhythm’.
Ammi,  n.,  a  genus  of  plants  (hot.)  —  L.  ammi,  fr. Gk.  fr.  Aram,  ammithd,  a  secondary  form of  hammithd,  of  s.m.
ammo-,  combining  form  meaning  ‘sand’,  as  in ammophilous.  —  Gk.  aggo-,  fr.  figifrog,  ‘sand’, a  blend  of  fip.alk>c;,  ‘sand’,  and  tj'xp.p.oi;,  ‘sand’ ; which  are  both  cogn.  with  E.  sand  (q.v.) ammonal,  n.,  a  high  explosive  obtained  by  a  com¬
bination  of  ammonium  nitrate  and  aluminum. —  Formed  fr.  ammonia  and  the  first  two  letters in  aluminum.
ammonia,  n.  —  Contraction  of  sal  ammoniac,  fr. L.  sal  ammoniacum,  ‘ammoniac  salt’.  See  next word.
ammoniac,  adj.  and  n.  —  F.,  fr.  L.  ammoniacum, fr.  Gk.  afj.[i(ovtax6v,  ‘a  resinous  gum’,  prob. fr.  orig.  ’Apjxsviaxov,  ‘Armenian’,  through  the intermediate  form  apgioviaxov,  occurring  in  the works  of  ancient  authors  beside  ap.|icovtax6v; so  called  because  first  found  in  Armenia.  See Pauly-Wissova,  Real-Encyclopadie  der  klas- sischen  Altertumswissenschaft,  I,  1861. Derivative:  ammoniac-al,  adj. ammonite,  n.,  a  cephalopod  mollusk  allied  to  the nautilus  (paleontol.)  —  Formed  with  subst.  suff. -ite  fr.  L.  cornu  Ammonis,  ‘the  horn  of  (Zeus) Ammon;  so  called  from  its  shape,  which  re¬ sembles  a  ram’s  horn  (Zeus  Ammon  was  rep¬ resented  with  ram’s  horns), ammonium,  n.,  a  basic  radical,  NH4  (chem)  — ModL.,  fr.  ammonia  (q.v.) ammophilous,  adj.,  sand-loving  (zool.  and  hot.) — -  Compounded  of  ammo-  and  Gk.  iplXog, ‘loving’.  See  -philous.
ammotherapy,  n.,  treatment  by  means  of  sand baths.  —  Compounded  of  ammo-  and  -therapy, ammunition,  n.  —  F.  amunition,  a  dialectal  form for  munition  (see  munition).  Amunition  arose through  a  misdivision  of  la  munition  ivAoTamu- nition.
amnemonic,  adj.,  characterized  by  loss  of  me¬ mory.  —  Formed  fr.  priv.  pref.  a-  and  Gk. pvir)|i.ov!.x6p,  ‘pertaining  to  memory’.  See  mne¬ monic.
amnesia,  n.,  loss  of  memory  ( psychiatry ).  — Medical  L.,  fr.  Gk.  ap.v7)crla,  ‘forgetfulness’,  fr. a-  (see  priv.  pref.  a-)  and  (jLvfjmop,  ‘pertaining to  memory’,  which  is  rel.  to  gtvaopat,  ‘I  remem¬ ber’,  fr.  I.-E.  base  *men-,  ‘to  think,  remember’. See  mind  and  cp.  next  word.  Cp.  also  anam¬ nesis,  paramnesia.  For  the  ending  see  suff.  -ia. amnesty,  n.,  general  pardon.  —  F.  amnestie,  fr. L.  amnestia,  fr.  Gk.  apvTjaTta,  ‘forgetfulness, fr.  a-  (see  priv.  pref.  a-)  and  ptvrjcmp,  ‘remem¬ brance’,  which  is  rel.  to  pivaopm,  ‘I  remember’. See  prec.  word.
amnic,  adj.,  pertaining  to  a  river.  —  L.  amnicus, fr.  amnis,  ‘river’,  which  stands  for  *ab-nis  and is  cogn.  with  OIr.  abann,  ab,  W.  afon,  ‘river’,  fr. I.-E.  base  *ab-,  a  collateral  form  of  base  *ap-, ‘water,  river’,  whence  OI.  dpah,  apah,  Avestic af-sh,  ‘water’,  Gk.  ‘Atria,  a  name  of  the  Pelo¬ ponnesus  fso  called  because  surrounded  by water),  Mecraxtrla,  ‘Messapia’,  a  part  of  Magna Graecia  in  Lower  Italy  comprising  Apulia  and Calabria,  lit.  ‘the  country  between  two  waters', L.  Ap-ulia,  ‘Apulia’,  lit.  ‘region  abounding  in waters’,  Lith.  upe,  Lett,  upe,  ‘water’,  OPruss. ape,  ‘a  small  river’,  apus,  ‘spring,  fountain, well’,  and  prob.  also  Toch.  AB  ap-,  ‘river’.  Cp.
amnion
64
65
ampin  mcaici
the  first  element  in  abdest,  abkari,  Apsaras  and the  second  element  in  doab  and  in  Messapian. For  the  ending  of  amnic  see  suff.  -ic. amnion,  n.,  the  membrane  enclosing  the  embryos of  mammals,  birds  and  reptiles.  —  Gk.  dpvlov,
‘a  bowl  in  which  the  blood  of  victims  was caught;  membrane  round  foetus’,  rel.  to  dpaa- 8-ou,  ‘to  draw,  gather’,  dpv],  prop,  ap.ii)  (whence L.  hama),  ‘bucket’,  and  cogn.  with  Lith.  semiu, semli,  ‘to  draw’,  samtis ,  ‘scoop,  ladle’.  These words  prob.  derive  fr.  I.-E.  base  *sem~,  one, together’,  whence  also  Gk.  Spa,
```


## [2026-09-04T19:40:10.422Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nt=p[44]\nprint(len(t))\nprint(t[5500:])\nEOF"
}
```


### [2026-09-04T19:40:12.061Z] TOOL RESULT

```
11666
g.  meaning  of  L.  minari  has  survived  in Rum.  mana,  ‘to  threaten’.  See  menace  and  -able. Derivatives :  amenabil-ity,  n.,  amenable-ness,  n., amenabl-y,  adv.
amend,  tr.  and  intr.  v. — OF.  (=  F.)  amender ,  fr.  L. emendare,  ‘to  correct,  emend’,  with  change  of suff.  (cp.  the  same  change  of  suff.  in  It.  ammen- dare  and  OProven?.  amendar);  fr.  e-,  ‘out  of’ (see  e-)  and  menda,  'defect,  blemish’,  which  is cogn.  with  OI.  mindi,  ‘physical  blemish’  (for *manda,  influenced  in  form  by  OI.  nindd, ‘blame’),  OIr.  mennar ,  ‘stain,  blemish’,  mind, ‘sign,  mark’,  W.  mann  of  s.m.  Cp.  emend,  mend, mendacious,  mendicant.
amendment,  n.  —  OF.  (=  F.)  amendement,  fr. amender.  See  prec.  word  and  -ment. amends,  n.  —  ME.  amendes,  fr.  OF.  amendes,  pi.
of  amende ,  fr.  amender,  ‘to  amend’.  See  amend, amenity,  n.,  pleasantness;  attractiveness.  —  F. amende,  fr.  L.  amoenitatem ,  acc.  of  amoenitas, ‘delightfulness,  loveliness’,  fr.  amoenus,  ‘pleas¬ ant,  delightful,  lovely’,  which  is  rel.  to  amare, ‘to  love’.  See  amative  and  -ity. ament,  catkin.  —  L.  ammentum,  less  correctly amentum,  ‘strap,  thong’,  so  called  because  of  its resemblance  to  a  strap.  Ammentum  stands  for *ag-mentum,  and  prop,  means  ‘something  to lead  with’,  fr.  agere,  ‘to  lead’.  See  agent  and -ment.
Derivatives:  ament-aceous,  ament-al,  adjs. amentiferous,  adj.,  bearing  aments.  ■ —  See  ament and  -ferous.
amerce,  tr.  v.,  i)  orig.,  to  fine;  2)  to  punish. — ME.  amercen,  ‘to  fine’,  fr.  AF.  amercier,  fr.  OF. a  merci  (F.  a  merci),  ‘at  somebody’s  mercy’. OF.  a  derives  fr.  L.  ad,  ‘to’;  see  ad-.  For  F. merci  see  mercy.
Derivatives:  amerce-able,  amerci-able,  adjs., amerce-ment,  n.
America,  n.  —  Named  after  Americas  Vespitcius (Amerigo  Vespucci),  an  Italian  merchant  (1451- 1512).  The  name  America  was  first  used  by  the German  cartographer  Martin  Waldseemiiller (in  1507).
Derivatives:  Americ-an,  adj.  and  n.,  Americ-an- ism,  n.,  Americ-an-ize,  v.,  Americ-an-iz-ation,  n. americium,  n.,  name  of  a  radioactive  element (chem.)  —  ModL.,  named  m  1946  by  its  dis¬ coverer  Glenn  Theodore  Seaborg  (1912-  ) after  the  2  Americas.  For  the  ending  see  suff. -ium.
Amerind,  n.,  an  American  Indian  or  Eskimo.  — Abbreviation  of  American  Indian ;  coined  by Major  John  Wesley  Powell  (1834-1902),  di¬ rector  of  the  bureau  of  American  Ethnology.
Derivatives:  Amerindi-an,  n.  and  adj.,  Amerind- ic,  adj.
amethyst,  n.,  violet  quartz,  used  n  jewelry.  — ME.  ametist,  fr.  OF.  ametiste  (F.  amethyste),  fr. L.  amethystus,  fr.  Gk.  agiHuaroi;,  ‘remedy against  drunkenness’,  prop,  an  adjective  mean¬ ing  ‘not  intoxicating’,  fr.  a-,  ‘not’  (see  priv.  pref. a-),  and  ucbuetv,  ‘to  be  drunken’  (whence pi&ua!4,  ‘drunkenness’),  fr.  pifhj,  ‘wine’;  see mead,  ‘an  intoxicating  drink’,  and  cp.  methyl. The  stone  amethyst  owes  its  name  to  its  sup¬ posed  power  of  preventing  drunkenness, amethystine,  adj.  —  L.  amethyst inus,  fr.  ame¬ thystus.  See  prec.  word  and  adj.  suff.  -ine  (re¬ presenting  L.  -inus).
AMG.  —  Abbreviation  of  Allied  Military  Govern¬ ment.
AMGOT.  —  Abbreviation  of  Allied  Military Government  of  Occupied  Territory.
Amhaarez,  n.,  an  ignoramus.  —  Heb.  ‘am  had- retz,  ‘the  people  of  the  land’.  Heb.  'am,  ‘people’, derives  fr.  base  ‘- m-m ,  ‘to  join,  be  united’, whence  also  ‘am,  ‘kinsman’,  'im,  ‘with’.  Cp.  the rel.  Aram.-Syr.  ‘ammd,  ‘people’,  Ugar. ‘/n, ‘clan’, Arab,  ‘amm,  ‘a  great  crowd’,  ammah,  ‘rabble’, ‘dmma,  ‘it  comprised,  included’,  ‘amm,  ‘father’s brother’,  ‘ dmma *,  ‘father’s  sister’,  Aram,  'im, Syr.  ‘am,  Ugar.  'm,  Arab.  ma‘a,  dial,  ‘am, ‘with’.  Cp.  the  first  element  in  Emmanuel  and the  second  element  in  Jeroboam.  Heb.  eretz, ‘earth’,  is  rel.  to  Aram.  dra‘,ar‘d,  Ugar.  Vy,  Arab. ard,  Akkad,  irfitu,  ‘earth’.  Cp.  Eretz  Yisrael. amiable,  adj.  — OF.  (=  F.),  fr.  Late  L.  amicabilis, ‘friendly’,  fr.  L.  amicus,  ‘friend’.  F.  amiable  was influenced  in  form  by  aimable,  ‘lovely’,  fr.  L. amdbilis,  fr.  amare,  ‘to  love’.  See  amicable. Derivatives:  amiabil-ity,  n.,  amiable-ness,  n., amiabl-y,  adv.
amianthus,  n.,  name  of  a  kind  of  asbestos.  L. amiantus,  fr.  Gk.  afnavrcw;  (scil.  ALiV,-),  lit. ‘undefiled  (stone)’,  fr.  <4-  (see  priv.  pref.  a-),  and piavTo^,  ‘stained,  defiled’,  verbal  adj.  of  tuodvetv, ‘to  stain,  defile’ ;  see  miasma.  The  spelling  th  (for t)  is  prob.  due  to  the  influence  of  Gk.
‘flower’.
Derivatives:  amianth-ine,  amianth-oid,  amianth- oid-al,  adjs.
amicable,  adj.,  friendly.  —  L.  amicabilis,  friend¬ ly’,  fr.  amicus,  ‘friend’,  fr.  amare,  ‘to  love’.  See amative  and  cp.  amiable,  which  is  a  doublet  of amicable.  Cp.  also  enemy,  inimical.  For  sense development  cp.  Gk.  <plXo c„  ‘friend’,  from  the base  of  cptXeiv,  ‘to  love’,  and  Heb.  ohfbh, ‘friend’,  which  is  prop.  part,  of  ahdbh,  ‘he loved’.
Derivatives:  amicabil-ity,  n.,  amicable-ness,  n., amicabl-y,  adv.
amice,  n.,  vestment  worn  by  the  celebrant  at Mass.  —  ME.  amyse,  fr.  OF.  amis,  amit,  fr.  L. amictus,  ‘mantle,  cloak’,  fr.  amictus  pp.  of amicid,  amicire,  ‘to  wrap,  throw  around’,  which is  contracted  from  *am-jacid,  fr.  pref.  ambi-  and
jacid,  ‘I  throw’.  See  ambi-  and  jet,  ‘to  spirt  forth’, amice,  n.,  hood,  headdress.  —  ME.  amisse,  fr. OF.  aumuce  (F.  aumusse),  fr.  VL.  almucia, which  is  formed  fr.  Arab,  al-,  ‘the’,  and  miis- taqah,  fr.  Pers.  mushtd,  ‘fur  cloak’.  Cp.  Sp.  al- mucio,  OProveriQ.  almussa,  MDu.  almutse,  later mutse,  muts,  Du.  muts,  ‘cap’,  MHG.  mutze, miitze,  G.  Mutze,  ‘cap’,  which  all  derive  fr.  VL. almucia.  Cp.  also  almuce,  mozzetta,  mutch.  For sense  development  cp.  cap. amid,  prep.  —  ME.  amidde,  fr.  OE.  on  middan, ‘in  the  mi
```


## [2026-09-04T19:40:25.682Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(255,290):\n    if 'Emmanuel' in p[i] or 'Immanuel,' in p[i]:\n        print('LEAF',i)\n        for m in re.finditer(r'.{200}Emmanuel.{500}',p[i],re.S):\n            print(m.group(0)); print('---')\nEOF"
}
```


### [2026-09-04T19:40:27.479Z] TOOL RESULT

```
LEAF 275
’).  Cp.  Elohim.  Cp.  also  the  first element  in  the  PN.s  Eleazar,  Eliezer,  Elihu, Elijah,  Elishah,  Elizabeth,  and  the  second  ele¬ ment  in  Babel,  bethel  and  in  the  PN.s  Daniel, Emmanuel,  Ezekiel,  Gabriel,  Gamaliel,  Ishmael, Israel,  Joel,  Michael,  Nathaniel,  Raphael, Samuel.
-el,  suff.,  as  in  hovel.  —  OE.  -el,  -eta,  -ele.  Cp. -le,  suff.  representing  OE.  -el,  -ela,  -ele.
-el,  dimin.  suff.  of  French  origin.  —  1)  OF.  -el (F.  - eau ),  fr.  L.  -el/us  (as  in  tunnel)’,  OF.  -ele, -elle  (F.  -eile),  fr.  L.  -ella  (as  in  chapel).  See  -le, suff.  of  French  origin.
-el,  suff.  representing  OF.,  F.  -el,  fr.  L.  -alis,  as in  vowel  (
---
LEAF 280
h,  let out,  emit’,  fr.  e-  and  mittere,  ‘to  send’.  See  mis¬ sion.
Emma,  fern.  PN.  —  G.,  fr.  Erma,  contracted from  names  beginning  with  Erm-  (e.g.  Ermen- trud,  q.v.)  Cp.  Irma.
Emmanuel,  masc.  PN.  —  Gk.  ’Efj.[zavour]A,  fr. Heb.  'Immanuel,  lit.  ‘God  is  with  us’.  See  Im¬ manuel.
emmenic,  adj.,  capable  of  menstruation  (med.) Formed  with  suff.  -ic  fr.  Gk.  iiLiirya,  ‘the  men¬ ses’,  fr.  ev  (see  2nd  en-),  and  p.r)v,  gen.  wrybe, ‘month’.  See  meno-,  and  cp.  catamenia, emmenology,  n.,  that  part  of  medicine  which treats  of  menstruation.  —  Compounded  of  Gk. spipnrjva,  ‘the  menses’,  and  -Xoyia,  fr.  -Aoyop, one  who  speaks  (in  a 
---
LEAF 287
.)  —  G.  Entropie,  formed  on  analogy  of  G. Energie,  ‘energy’,  fr.  2nd  en-  and  Tp07rf),  ‘a  turn¬ ing,  turn,  change’,  first  used  in  1850  by  the German  physicist  Rudolf  Julius  Emmanuel Clausius  (1822-88).  See  trope  and  -y  (represent¬ ing  Gk.  -Ea).
entrust,  intrust,  tr.  v.  —  Formed  fr.  ist  en-  (resp. in-,  ‘in’)  and  trust.
entry,  n.  —  F.  entree,  prop.  fern.  pp.  of  entrer, ‘to  enter’,  fr.  L.  intrare.  Cp.  It.  entrata  (fem.  pp. of  entrare ),  OProveng.  intrada  (fem.  pp.  of  in- trar),  Sp.  entrada  (fem.  pp.  of  entrar)  and  see enter.  Cp.  also  entree.
entwine,  tr.  v.  —  Formed  fr.  ist  en-  and  twine, entwist,  tr.  v.  —  F
---
```


## [2026-09-04T19:40:33.463Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nt=p[280]\nprint(re.findall(r'\\n\\s*\\d{3}\\s*\\n', t))\n# print running head numbers\nprint([l for l in t.split('\\n') if re.fullmatch(r'\\s*\\d{3}\\s*', l)])\ni=t.find('Emmanuel,  masc')\nprint(t[max(0,i-3000):i+200])\nEOF"
}
```


### [2026-09-04T19:40:35.792Z] TOOL RESULT

```
[]
[]
owel  emet-,  combining  form meaning  1)  vomiting;  2)  emetic  (med.)  —  Fr. Gk.  Spcexot;,  ‘vomiting’.  See  emetic, emeute,  n.,  a  riot.  —  F.,  ‘riot’,  fr.  VL.  *exmorita, fern.  pp.  of  *exmovere,  ‘to  set  in  motion’,  used as  a  noun,  fr.  1st  ex-  and  movere,  ‘to  move’. See  move.
-emia,  -aemia,  suff.  denoting  a  certain,  usually diseased,  condition  of  the  blood,  as  in  hydremia, leukemia  (med.)  —  Gk.  -atpia,  fr.  aljra,  gen. aEptocrot ;,  ‘blood’.  See  hemal  and  -ia. emiction,  n.,  urination.  —  Formed  fr.  e-  and mictus,  pp.  of  mingere,  ‘to  make  water’.  See micturition.
emigrant,  adj.  —  L.  emigrans,  gen.  -antis,  pres, part,  of  emigrare.  See  next  word  and  -ant. Derivative:  emigrant,  n.
emigrate,  intr.  v.  —  L.  emigrants,  pp.  of  emi- grare,  ‘to  move  away,  remove,  emigrate’,  fr.  e- and  migrare,  ‘to  move,  migrate’.  See  migrate. Derivatives:  emigration  (q.v.),  emigrat-ive,  emi- grat-ory,  adjs.
emigration,  n.  —  Late  L.  emigrdtid,  gen.  -onis, fr.  L.  emigratus,  pp.  of  emigrare.  See  prec.  word and  -ion.
emigre,  n.,  an  emigrant;  specif.,  a  person  com¬ pelled  to  leave  France  during  the  French  Re¬ volution.  —  F.,  pp.  of  emigrer,  ‘to  emigrate’,  fr. L.  emigrare.  See  emigrate.
Emil,  Emile,  masc.  PN.  —  G.  Emil,  fr.  F.  £mile, fr.  L.  Aemilius,  name  of  a  Roman  gens,  fr.  ae- mulus,  ‘imitating,  rivaling’,  fr.  aemuldrl,  ‘to strive  to  equal’.  See  emulate  and  cp.  Emilia. Emilia,  Emily,  fern.  PN.  —  F.  imilie,  fr.  L.  Ae- milia,  fern,  of  Aemilius.  See  prec.  word, eminence,  n.  —  L.  eminentia,  ‘prominence,  emi¬ nence’,  fr.  e  mine  ns,  gen.  -ends.  See  next  word and  -ce.
i
1
eminent,  adj.,  1)  high;  2)  exalted.  —  L.  eminens, gen.  -entis,  pres.  part,  of  eminere,  ‘to  stand  out, project;  to  be  eminent’,  fr.  e-  and  I.-E.  base *men-,  ‘to  stand  out,  project’.  See  mount,  ‘hill, mountain’  and  -ent  and  cp.  imminent,  prominent. Derivative:  eminent-ly,  adv. emir,  n.,  1)  an  Arabian  prince;  2)  a  title  given Mohammed’s  descendants  through  his  daughter Fatima.  —  Arab,  amtr,  ‘commander’,  fr.  amara, ‘he  commanded’.  See  amoraim  and  cp.  ameer, admiral,  omrah.
emissary,  n.  and  adj.  —  L.  emissarius,  ‘one  sent out’,  fr.  emissus,  pp.  of  emittere.  See  emit  and -ary.
emission,  n.  —  L.  emissio,  gen.  -onis,  ‘a  sending out’,  fr.  emissus,  pp.  of  emittere.  See  emit  and -ion.
emissive,  adj.  —  Formed  with  suff.  -ive  fr.  L. emissus,  pp.  of  emittere.  See  next  word. Derivative:  emissiv-ity,  n. emit,  tr.  v.,  1)  to  send  out;  2)  to  utter;  3)  to  is¬ sue.  —  L.  emittere,  ‘to  send  out,  send  forth,  let out,  emit’,  fr.  e-  and  mittere,  ‘to  send’.  See  mis¬ sion.
Emma,  fern.  PN.  —  G.,  fr.  Erma,  contracted from  names  beginning  with  Erm-  (e.g.  Ermen- trud,  q.v.)  Cp.  Irma.
Emmanuel,  masc.  PN.  —  Gk.  ’Efj.[zavour]A,  fr. Heb.  'Immanuel,  lit.  ‘God  is  with  us’.  See  Im¬ manuel.
emmenic,  adj.,  capable  of  menstruation  (med.) Formed  with  suff.  -ic  fr.  Gk.
```


## [2026-09-04T19:40:43.573Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(272,286):\n    nums=re.findall(r'(?<![\\d.,])\\b(5\\d\\d|4\\d\\d)\\b(?![\\d])', p[i])\n    print(i, nums[:8])\nEOF"
}
```


### [2026-09-04T19:40:45.436Z] TOOL RESULT

```
272 []
273 ['501', '502', '503']
274 ['504', '505']
275 []
276 ['506', '507']
277 ['508']
278 ['510']
279 ['512', '513']
280 []
281 ['516', '517']
282 ['518', '519']
283 ['520', '521']
284 ['522', '523']
285 ['524', '525']
```


## [2026-09-04T19:40:50.324Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,t in enumerate(p):\n    m=re.search(r'Immanuel,\\s+masc.{0,400}', t, re.S)\n    if m:\n        print('LEAF',i, re.findall(r'(?<![\\d.,])\\b(7\\d\\d|8\\d\\d)\\b',t)[:6))\nEOF"
}
```


### [2026-09-04T19:40:51.946Z] TOOL RESULT

```
Exit code 1
  File "<stdin>", line 6
    print('LEAF',i, re.findall(r'(?<![\d.,])\b(7\d\d|8\d\d)\b',t)[:6))
                                                                    ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
```


## [2026-09-04T19:40:55.685Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,t in enumerate(p):\n    m=re.search(r'Immanuel,\\s+masc.{0,400}', t, re.S)\n    if m:\n        print('LEAF',i, re.findall(r'(?<![\\d.,])\\b(\\d{3,4})\\b',t)[:8])\n        print(m.group(0))\nEOF\ngrep -n -o \"Immanuel,  masc.\\{0,300\\}\" KLN_1971.txt 2>/dev/null | head"
}
```


### [2026-09-04T19:40:57.476Z] TOOL RESULT

```
LEAF 415 ['772', '773']
Immanuel,  masc.  PN.  —  Heb.  ' Immanuel,  lit. ‘God  (is)  with  us’.  This  name  is  compounded of  ‘immdnu,  ‘with  us’  (which  is  formed  fr.  ‘im, ‘with’,  with  the  pronominal  suff.  of  the  1st person  pi.),  and  El,  ‘God’.  Heb.  'im  derives  fr. stem  ‘-m-m,  ‘to  join,  be  united’,  whence  also 'am,  ‘people’.  See  Amhaarez.  For  the  second element  in  the  name  Immanuel  see  El.  Cp
```


## [2026-09-04T19:41:12.210Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT amen\"; grep -n -o \"amen,.\\{0,300\\}\" SKT.txt | head -5; echo \"== SKT Amen alt\"; grep -n -i -o \"Amen\\b.\\{0,250\\}\" SKT.txt | head -5; echo \"== FSD amen\"; for f in FSD_vol1.txt FSD_vol2.txt; do echo \"--$f\"; grep -n -i -o \"a-men.\\{0,200\\}\\|Heb\\. amen.\\{0,200\\}\" $f | head -4; done; echo \"== WEB amen\"; grep -n -i -o \"amen[,;].\\{0,250\\}\" WEB_vol1.txt | head -5"
}
```


## [2026-09-04T19:41:14.056Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FVQ amin/iman\"; grep -n -i -o \"\\bamin\\b.\\{0,200\\}\\|\\biman\\b.\\{0,200\\}\\|amana.\\{0,150\\}\" FVQ.txt | head -12; echo \"== FVQ umma\"; grep -n -i -o \"umma[t]*\\b.\\{0,180\\}\" FVQ.txt | head -8"
}
```


### [2026-09-04T19:41:14.073Z] TOOL RESULT

```
== SKT amen
449:amen,  the  tongac of  a  balance,  put  for  txapmn  • :  cf.  exigere, lo  weigh  out.  — L.  ex,  out;  agere.  to  drive.
6579:amen,  • L  jUamentiim,  thin  thread.  —  Low  h./ilartt to  wind  thread.  — L.yf/iiM.
6686:amen,  Flamingo ;  see  Fl Flange ;  see  below Flank,  the  side.  (F.-L.)     F.MSSZ the  'weak'  part  of  the  body.  — L.  0ae soft ;  with  inserted  n  as  in  jangi', iocu/aforem  ;  see  Flaooid.  %  Cf.  G. softnc-s  :  also,  the  side.
7379:amen,  a  game  (above). sec  Baokgammon.
10226:amen,  an  alleviatioQ ; here  used  in  the  orig.  Knse  of '  that  which mivcs.'  —  L.  Uuarr,  to  raise.  —  L.  /ntii, light.
== SKT Amen alt
449:amen,  the  tongac of  a  balance,  put  for  txapmn  • :  cf.  exigere, lo  weigh  out.  — L.  ex,  out;  agere.  to  drive.
760:amen  of  a flower.  (Gk.)  From  Gk.  uHJ^p^'t,  bloom- ing. -  Gk  aftfcrf,  to  bloom ;  d*^or,  a  young bwi  or  sprouL
6579:amen,  • L  jUamentiim,  thin  thread.  —  Low  h./ilartt to  wind  thread.  — L.yf/iiM.
6677:amen.  (L.)  L.  Jtamen  a  priest  of Rome.  Prob^  foxJlAg-mtn  •,  be  who  boms the  sacrifice.
6686:amen,  Flamingo ;  see  Fl Flange ;  see  below Flank,  the  side.  (F.-L.)     F.MSSZ the  'weak'  part  of  the  body.  — L.  0ae soft ;  with  inserted  n  as  in  jangi', iocu/aforem  ;  see  Flaooid.  %  Cf.  G. softnc-s  :  also,  the  side.
== FSD amen
--FSD_vol1.txt
7424:a-mentjla-dtt'a-mentorad'i-td-ment:  2ft-dlt'a-m6nt or  Sd'i-ta-ment,  n.  [Rare.]  1.  A   thing  added;  addition.  2. PhvstoL  Chcm.  Alexin.  [<  L.addo.add.)  ad-dlt'1-mcnt}. —   Syn4  see  addendum; 
7424:a-men'ta-ry,a.
7591:a-ment,  la-dlt'a-mentorad'i-to-ment;  2   fi-dlt'a-mfint or  fid'i-ta-mfint,  n.  [Rare.)  1.  A   thing  added;  addition.  2. Physiol.  Chan.  Alexin.  (<  L.aeWo.add-l  ad-dlt'l-mcntt.
7592:a-men'ta-ry,a. Add'ltcs,  1   ad'aits;  2   fid'Its,  n.  pi.  Same  as  Ad,  3. ad-dl'tlon,  1   a-dish'an;  2   ji-dTsh'on,  n.  1.  The  act  of
--FSD_vol2.txt
3761:a-men'te,  ads.  [It.] Bu-ran'!,  i.  du-ran';  S   dii-ran',  Augustin  ('“/ulTSS-n/i 1862),  a   Spanish  lihrarLan  and  author;  Ballad  Peelry.  2. riii'mu':  2   dii"r;in',  Carolus  (V-ilS37-»/i8ll9
8798:a-ment  or -mant;  2 en-fran'chi«-ment,  n.  1.  The  act  of  enfranchising,  or the  state  of  being  enfranchised;  admission  to  citizen- ship, including  political  freedom  anti  civil  capacity;  
14505:a-mentt.—  ex- cru'cl-a-tor,  n.  A   torturer;  tormentor.
15252:a-mentf. Sjm;  see  propitiation;  sacbieiob.— ex''pI-a'’tlon-al,  a. Pertaining  to,  of  the  nature  ot,  or  for  the  purpose  of  expia- tion: as,  expiailojial  work.
== WEB amen
4988:amen; OFr. amer, esmer; L. estimare, z to estimate.] i
6537:amen; Gr. amén; Heb. dmén, truly, certainly]
6539:Amen, the faithful
6541:amen; an expres- sion of formal assent, concurrence, or con- viction.
6586:Amen, lit., hidden one, and Rā, sun.] the ancient Egyp- tian sun god: also spelled Amon-Ra.
```


### [2026-09-04T19:41:15.796Z] TOOL RESULT

```
== FVQ amin/iman
== FVQ umma
4520:umma).
```


## [2026-09-04T19:41:26.288Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WEB context\"; sed -n '6530,6545p' WEB_vol1.txt; echo \"== WEB Immanuel/Emmanuel\"; grep -n -i -o \"Immanuel.\\{0,200\\}\\|Emmanuel.\\{0,200\\}\" WEB_vol1.txt | head -6"
}
```


### [2026-09-04T19:41:27.936Z] TOOL RESULT

```
== WEB context
a-m6l/i6-ra-ble (-y6-), a. capable of better- ment.
a-mél’id-rint, x. a thing that ameliorates.
a-mél/id-rate, v.t.; ameliorated, pt., pp.; amel- iorating, ppr. [L. amelioratus, pp. of ameli- orare, to make better; ad, to, and meliorare, from melior, better.] to make better; to im- prove; to meliorate.
a-mél/io-rate, v.i. to grow better or less severe.
a-mél-i6-ra/tion, n. a making or becoming better; improvement.
a-mél/io-ra:tive, a. tending to produce im- provement.
a-mél’i6-ra-t6r, n. ameliorates.
a’men/ (also i/men’), n. [L. amen; Gr. amén; Heb. dmén, truly, certainly]
1. [A-] a term used in Scripture to denote Christ.
These things saith the Amen, the faithful
and true witness. —Rev. iii. 14.
2. a speaking or writing of amen; an expres- sion of formal assent, concurrence, or con- viction.
3. the conclusion, in word or act; the end.
4/men/, inlerj. so be it: used as an expression of hearty assent or formal confession of faith; also, as the formal conclusion of prayers, etc.
a’men/, adv. truly; verily. z
a’/men/, v.t. to assent to or concur in; to sanc- „tion; to say_amen to; to conclude.
== WEB Immanuel/Emmanuel
63678:Immanuel (God with us). be em-mir’ble, v.i. to work in marble; to deco- rate with or turn into marble. Baty em-men/a-gogue (-gog), n. [Fr. emmenagogue, Gr. emména, menses, neut. pl. of pene
103238:Immanuel Kant (1724-1804), or to his going through ETA, me i eidoscope; who are still represented by the mikado. works and doctrines; resembling or conform- ka-lei-d6-scop/ic-Al, z ES kä-mi-kä’zē, n. [Japan.,
```


## [2026-09-04T19:41:29.223Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FVQ_pages amin\"; grep -n -i -o \"am[iī]n.\\{0,150\\}\" FVQ_pages.txt | head -8; echo \"== AFM عم\"; grep -n -o \"عم[ّو].\\{0,80\\}\" AFM.txt | head -5; echo \"== AFA amin\"; grep -n -i -o \"\\bAmin\\b.\\{0,150\\}\\|amana.\\{0,120\\}\" AFA.txt | head -6; echo \"== LKT amin\"; grep -n -i -o \"am[iî]n.\\{0,180\\}\" LKT.txt | head -6"
}
```


### [2026-09-04T19:41:31.044Z] TOOL RESULT

```
== FVQ_pages amin
416:amination of the question reveals even further and more
990:amine
1082:amine the words which the philologers class as Indian,^
1378:amination of the words which as-Suyuti's authorities place in the
1588:amination of the Lexicons, however, shows that there is
4326:amined by Horovitz,
4341:amination of the word itself.
4747:amination of the word, Frewdw, 110, has confirmed the suspicion
== AFM عم
240:عمور. وكان الفرس اذا ارادوا نسمية © 
389:عمّل بالذهب او ثاب + ܨ صفاق 
3151:عموا ان فيها 1 81 مستا 
3424:عمون 3 شل انلزن على المغيبات رهي تعريب زيركاه 
3529:عمّيدة:هي فارسيّة .وم يأت بدليل على 
== AFA amin
== LKT amin
367:aminiert,  wobei  sich folgende  Wörter  ergaben :  rum.  amanet, emanet  'Pfand,  Sicherheit';  bulg.  serb. amanet  'Pfand',  russ.  amanat  'Geisel'. [Sain  46.  Devic  DEt  30.  La
371:amin  ,  serb.  aminati, klruss.  amin,  dagegen  cech.  poln.  amen [besonders  in  der  Redensart :  jak  amen w  pacierzu  '(sicher)  wie  das  Amen  im Gebete'].  [Gorjajew  4.  Mi
531:amination  mit  germ.  Hafen  oder Volksetymologie  anzunehmen  ist].  Russ. awarija,  bulg.  serb.  awarija,  Cech.  ava- rie 'Seeschaden'.  [DE  217.  Dozy  Oost 22/23.  Devic  DEt  
599:amin';  hieraus  rum.  bageacä,  bajacä 'Dachfenster,  Fensterluke'.
665:aminationen ähnlich  bedeutender  Wörter  und  unter volksetymologischen  Einflüssen  it.  bar- ■bucane  'Brustwehr  mit  Schießscharten, Stützmauer',  prov.  barbacana,  frz.  bar- ba
742:amineen',  dem Sparlo  ähnlich  und  wie  dieser  gebraucht. [Devic  DEt  29.  Lammens  Rem  21. ML  1401.
```


## [2026-09-04T19:41:35.411Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '355,378p' LKT.txt"
}
```


### [2026-09-04T19:41:35.462Z] TOOL RESULT

```
61.  Tk.  altyn:
'Gold'  [Stamm  al  'rot',  s.  hier  Nr.  48], auch  altun.  Hieraus  bulg.  altzn  'dass.', serb.  alduiii-  in  Zusammensetzungen 'Gold-',  russ.  altgn,  früher  '3-,  jetzt 15-Kopekenstück'  [man  beachte  die  Ent- wertung der  ursprünglichen  Bedeutung!], klruss.  altyyi  '3-Kopekenstück'.  —  Aus dem  tk.  Deminutiv  altyngiß-  wurde  rum. alfingic  'Kapuzinerkresse,  Tropaeolum malus'  [wohl  wegen  der  roten  Blüten]. [Gorjajew  3.    Bern  SlEtWb  27/28.
62.  Pers.  alüca:
'Pflaume'  [Berge  DPersFr  39,  Deminutiv von  ala  'dass.'] ;  hieraus  russ.  alyca, hjöa  'dass.',  wohl  über  einen  tat  arischen Dialekt.    [Gorjajew  3/4.
63.  Tk.  alys-weris: [Verbalsubstantive  von  al-  'nehmen, d.  h.  kaufen',  u.  wer-  'geben,  d.  h.  ver- kaufen'] 'Handel';  hieraus  rum.  ali^veri^ 'dass.,  Verkauf.  [Sain  46.  MSOÖ  II, 122/3.
64.  Ar.  aiumä :
'Aber',  tk.  emma  'dass.'.  Hieraus  rum. ama,  ma  'was!  wirklich!';  bulg.  am,  ami 'sondern,  aber',  serb.  am<x  'allein,  aber'. [Bern  SlEtWb  28.
I'ers.  ämäilä.]
6
65.  Perä.  ämädä:
Part.  pfct.  des  Vbs.  ämiidän  'kommen' (Horn  NpEt  S.  11,  Nr.  48],  also  'gekom- men'. Über  das  tk.  wurde  rum.  aman- dea  'fertig,  schnell'.
66.  Ar.  aniän:
'Gnade,  Gunst',  ebenso  tk.  Hieraus rum.  aman  'Gnade,  Verzeihung',  mit dem  ar.  Art.  aliman  'Not,  Elend'.  Frz. aman  in  der  Redensart  demander  T atnan 'um  Schutz  bitten'.  —  Die  ar.  Form imäna,  tk.  emanet  'Sicherheil'  wurde mit  amän  kontaminiert,  wobei  sich folgende  Wörter  ergaben :  rum.  amanet, emanet  'Pfand,  Sicherheit';  bulg.  serb. amanet  'Pfand',  russ.  amanat  'Geisel'. [Sain  46.  Devic  DEt  30.  Lammens Rem  22.  Bern  SIEtWb  28.  Gorjajew  4.
67.  Ar.  'amära :
'Strick'.  Davon  it.  alamari  plr.  'Rock- verschnürungen',  sp.  alamar  'mit  Schnü- ren verzierte  Knöpfe  zum  Schmucke od.  zum  Gebrauch'  [Dicc  Gast  101a], pg.  alnmar  'Schnüre  od.  Spangen  aus Seiden-,  Gold-  od.  Silberfäden  zur  Zierde am  Anzüge'  [Gonstancio  Dicc  42  b].  — Die  Etymologie  ist  m.  E.  zweifelhaft; vielleicht  ist  besser  liamäla  als  Grdwt. zu  nehmen ;  das  vulg.  ar.  Wort  'amära selbst  aus  herber,  amrär  'Schnur'.  [ML 397.  DE  54/6.  Caix,  Studi  di  etimologia italiana  e  romanza.  Firenze  1878. S.  145.
68.  Hebr.  amen:
'Wahrlich,  gewiß,  sicher'.  Hieraus  gr. b.\xr\v,  lat.  amen;  in  alle  europäischen Sprachen  übergegangen;  mit  diesem Wort  endigen  die  Jüdischen  und  christ- lichen Gebete.  Beachte  besonders  die Formen:  russ.  amin  ,  serb.  aminati, klruss.  amin,  dagegen  cech.  poln.  amen [besonders  in  der  Redensart :  jak  amen w  pacierzu  '(sicher)  wie  das  Amen  im Gebete'].  [Gorjajew  4.  Mikl  SIEtWb  3. Karlowicz  415.
69.  Ar.  ainlr:
a)  Vom  Vb.  amara  'befehlen',  also: 'Befehlshaber,  Fürst'.  In  der  vulg.  Form emlr  in  alle  europäischen  Sprachen  als Fremdwort  übergegangen,  bemerke  be- sonders ndl.  emier.  —  Mit  ar-rahl 'Transport',  d.  h.  die  Transportflotte,  die dem  Verkehr  u.  der  Verbindung  zwischen Andalusien  u.  Nordafrika  diente,  wurde amir  verbunden  zu  amlr  ar-rahl,  dem Titel  für  den  Befehlshaber  dieser  Flotte. Hieraus  ergeben  sich  aus  der  Verkür- zung der  Form:  pg.  amiralh,  prov. amiralhs,  atnirat,  afrz.  amiri,  nfrz. amiral  [u.  mit  falscher  etymologischer Beziehung  zu  lat.  admirari]  admiral, rum.  amiral,  it.  ammiraglio  [u.  wie  im
sp.  pg.  mit  Verkennung  des  ar.  Stammes am  ...  als  ar.  Artikel]  almiraglio,  sp. pg.  almirante  [mit  volksetymologischer Umbildung  gemäß  dem  lat.  partic.  praes.], afrz.  aumirant,  prov.  amiran,  it.  almi- rante.  Die  Bedeutung  ist  überall  'Ober- befehlshaber der  Flotte'.  Ebenso  mhd. admirät  [als  Titel  des  Kalifen],  dtsch. Admiral,  ndl.  admiraal,  engl,  admiral. —  Daß  die  Worte  aus  amlr-al-bahr 'Befehlshaber  der  See,  des  Meeres'  ent- standen sein  sollen,  scheint  wenig  wahr- scheinlich, wenn  auch  ein  solcher  Weg- fall des  arab.  Wortes  hahr  an  und  für sich  möglich  ist,  vgl.  z.  B.  Denebola  [s. hier  Nr.  482],  Abdul  [wurde  bei  einem tk.  Schüler,  der  'Abd-ul-hädl  hieß,  stets als  Name  gebucht].  Dem  Wunsche  von ML  423  nach  einer  Geschichte  der  Form u.  Bedeutung  dieses  Wortes  muß  zuge- stimmt werden.  Nur  zum  Teil  ist  dieser Wunsch  durch  Christoph  Gebhardt,  Das arabische  Etymon  einiger  romanischer Wörter.  Programm  des  Slädt.  Gymna- siums mit  Realschule  zu  Greiz.  1912. S.  6 — 19  erfüllt  worden.  Der  Verfasser stellt  als  neues  Etymon  für  die  verschie- denen Formen  der  Gruppe  Admiral  ar. amir  awival  'erster  Emir,  Oberemir' auf,  leider  ohne  diese  Zusammenstellung in  arabischen  Schriftstellern  belegen  zu können.  Den  Formen  prov.  amiran, amirant,  sp.  pg.  it.  almirante  wird  [a. a.  0.  S.  15]  der  Ausdruck  anUr-amlrän 'Emir  der  Emire'  zugrunde  gelegt,  doch scheint  die  pers.-ar.  hybride  Form  in dieser  Gestalt  nicht  bestanden  zu  haben, auch  scheint  die  notwendige  Abkürzung zu  amiran  zu  merkwürdig  zu  sein  [na- türlich nach  pers.  u.  arab.  Sprachge- brauche ist  nur  die  Verkürzung  mir- mlrän].  Orientalische  Entlehnungen lassen  sich  nicht  ohne  weiteres  nur  mit Beachtung  der  romanischen  Lautgesetze verfolgen,  wie  im  Vorwort  allgemein bemerkt  wurde.  [Devic  DEt  31/32. Lammens  Rem  23/24.  DE  165.  Dozy Oost  5/6.  Kluge  7.  Rom  Forsch  IV, 368.
b)  Mit  pers.  zädäl  'geboren,  Sohn' [Horn  NpEt  S.  143,  Nr.  645]  entstand pers.  ämirzädä  od.  verkürzt  tnirzä,  wört- lich 'Fürstensohn'.  Nachgesetzt,  be- zeichnet das  Wort  einen  'Prinzen  von Geblüt',  z.  B.  ßäsid  tnirzä  'Prinz  R.'. Vorgesetzt,  ist  das  Wort  der  Titel  eines gebildeten,  besonders  eines  schreibkun- digen Mannes;  am  bekanntesten  ist Bodenstedts  JVIIRZA  SCHAFFT,  pers. mirzä  säfi'.  —  Russ.  mirza,  murza 'tatarischer  Großwürdenträger',  vielleicl  it auch  mit  gerade  gegenteiliger  Bedeutung
7
[Ar.  anirah.
nmrza  'Schmutzfink,  Aschenbrödel'.  — Rum.  )H jr^;ac 'TatarenhäupUing'.  [Löbel EITAP  64.
```


## [2026-09-04T19:41:54.257Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"امانوئل\" \"آمین\" \"امانت\" \"عمو\" ; do echo \"=== $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt BQT_v1.txt BQT_v2.txt RCH.txt 2>/dev/null; done"
}
```


### [2026-09-04T19:41:55.965Z] TOOL RESULT

```
=== امانوئل
RCH.txt:0
BQT_v2.txt:0
BQT_v1.txt:0
MON_part2.txt:0
MON_part1.txt:0
=== آمین
RCH.txt:0
BQT_v2.txt:0
BQT_v1.txt:4
MON_part2.txt:3
MON_part1.txt:5
=== امانت
RCH.txt:0
BQT_v2.txt:1
BQT_v1.txt:3
MON_part2.txt:6
MON_part1.txt:12
=== عمو
RCH.txt:0
BQT_v2.txt:122
BQT_v1.txt:112
MON_part1.txt:388
MON_part2.txt:528
```


## [2026-09-04T19:42:00.532Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON1 آمین\"; grep -n -o \".\\{80\\}آمین.\\{200\\}\" MON_part1.txt | head -6; echo \"=== MON2 آمین\"; grep -n -o \".\\{80\\}آمین.\\{200\\}\" MON_part2.txt | head -6"
}
```


### [2026-09-04T19:42:00.611Z] TOOL RESULT

```
=== MON1 آمین
=== MON2 آمین
```


## [2026-09-04T19:42:03.446Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['MON_part1.txt','MON_part2.txt','BQT_v1.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    print('=====',f)\n    for m in re.finditer('آمین',t):\n        print(repr(t[max(0,m.start()-120):m.start()+200]))\n        print('---')\nEOF"
}
```


### [2026-09-04T19:42:05.196Z] TOOL RESULT

```
===== MON_part1.txt
'وج و ك آیده نوش آمیغ» غم آمیغ» \nگوهر آمیغ \n\nآمیفه: 1 )2 ی آمیغدن) آمیزش. \nمباشرت مجامعت» ارف تا (ص.) \nآمیخته» مخلو ط. \n\nآمین : و21 [ع. عبر.| کلمه\u200cای است که بس \nاز دعا گویند به معنی بر آورد! بپذیر! اجابت \nکن! \n\nآن: 1 (ضم.) ضمیر اشاره؛» برای دور) مق. \nاين؛ ج. برای اشخاص ,«آنان» و برای اشیا و \nجانوران «آنها. آن زمان» آن و'
---
'(شمالی» جنوبی) تقسیم کند. \nاسستوار: 05-0-6۲ [- ستوار] (ص\u200cمر.) \nبرقرار» پابدار» ثابت» بای بر جا. محکم؛ \n0 4 سحت. معتمد») آمین. (حامص.) \nاستواری» محکمی. (نظ.) درجه\u200cای است در \nنظام ایران» میان گروهبان و افسریار و دو \nمرحله دارد: استوار دوم و استوار یکم) معین \nتایب. \nاستوار داشتن: ۰-0280 (مصم.) بر قرار \nداشتن» محکم ساختن» '
---
'کشور وی اقامت نماید صادر می\u200cشود؛ \nاعتبار نامه (سیاسی). \nاستوان: 05-0-50 [- ستوان] (ص\u200cمر.) \nاستو ار » محکم؛ متین. معتمد» آمین. مضوط. \nاستوانه: (0-)0500۷5088 [ - مع اسطوانه» قس. \nستون] (.) ستون: ستون راست ( استوانه \nقائمه) (التفهیم). (هت.) حجمی است که در \nدو سر آن دو دایره موازی یکدیگر باشد. \n(مکد.) استوانه\u200cای است که در '
---
'[(ع] (مسصم.) آرزو دادن \n\n\nتأمین: مرها [غ.] (مص م .) ایمن کردن» \nآرام دادن بی\u200cبیم کر دن. امین کردن» حفظ \nکردن» امن کردن: آمین گفتن دعای کسی را \n(عم.) (امص.) ایمنی؛ ج. تا مات تأْمین آتبه \n( آننده): اندوخته برای زندگانی آینده نهادن \nو پیش\u200cبینی برای معاش آتیه. تأمین عبور و \nمرور: منظم ساختن خط سیر وسایل نقلیه \nبرای جل وگیر'
---
'ن. \n\nتوام: (-.«0ا)سه #ها [ع.] (ص. .) کودکی \nکه با کودک دیگر در یکت هنکام زاییده \nشده باشد؛ همزاد؛ دوقلو. تد. توآمان \nت وآمین؛ ج. توائم. جفت (زن و شوهر). دو \nچیز همراه. \n\nتوآمان: (-.0)1007۷- ۵20 ۱۵ [ع.] (ص. .) \nتئنبه توام. دو همزاد. دو همراه» دو قر بن. \nتوبان: مت [- تتبان \u200f تمان] (.) شلوار. \nتنکه. شلوار کو تاه کشت یگیرا'
---
===== MON_part2.txt
' و \nشک وا زود هت غان ایک ات \nنژادهای مهم مرغ\u200cهای آمریکایی عبار تند از. \nتژاد بلیموت را کك» براهماء جاوه. و باندوت. \nمرغ آمین: فر شته\u200cای است که در هوا پرواز \nکند و همیشه آمین گوید و هر دعایی که به \nآمینش رسد مستجاب شود. مرغ ار پینگتون: \n(جاذ.) از ناادهای خوب و تخمی مرغ\u200cهای \nانگلستان است. تنومند و برواری است \nپاهایش پر ن'
---
'آمریکایی عبار تند از. \nتژاد بلیموت را کك» براهماء جاوه. و باندوت. \nمرغ آمین: فر شته\u200cای است که در هوا پرواز \nکند و همیشه آمین گوید و هر دعایی که به \nآمینش رسد مستجاب شود. مرغ ار پینگتون: \n(جاذ.) از ناادهای خوب و تخمی مرغ\u200cهای \nانگلستان است. تنومند و برواری است \nپاهایش پر ندارد. سفید و سیاه و زرد آن \nدیده شده است. مرغ الب'
---
'بلیموت را کك» براهماء جاوه. و باندوت. \nمرغ آمین: فر شته\u200cای است که در هوا پرواز \nکند و همیشه آمین گوید و هر دعایی که به \nآمینش رسد مستجاب شود. مرغ ار پینگتون: \n(جاذ.) از ناادهای خوب و تخمی مرغ\u200cهای \nانگلستان است. تنومند و برواری است \nپاهایش پر ندارد. سفید و سیاه و زرد آن \nدیده شده است. مرغ البر فلد: (جان.) یکی از \nنژادها'
---
===== BQT_v1.txt
' بقابای مناره \nبامر قاگت که ساخته شده است. ۶ داثرة الممارف اسلام ». آبینة اسکندری در حقیقت ۶ آأبينة \nاسکندریه» است بعنی آمینه\u200cا یکه بر فرازمثاره ش شهراسکندربه صب کرده بودنشو بعدها بمناست آنکه \nشاد نهادن\u200cشپراسکتدریه 1 آبرا باسکندر مقدونی نسست میدادند» آ بیشهرا نیز بدواهماب\u200cدادند : \n\nآیینهُ سکندر جام جم است بنگر تا برتو '
---
'ل برست: - ومودم دلیر وصاحب قوت \nوقوی\u200cبازو را نیز کفتهانم.: \n\nاستو ار ۱ بم اول بروزن خشکوار \nبمعنی محکم و عضبوط باشد - و آمین و متمد \nوامادی\u200cرا نیز کوبند - وبمعنی باورهم حست\u200cچه \nاستوار داشتن بمعنی باورداشتن است . \n\nاستوان ۲ - بن اولو تالث بروزن \nپلبلان » بسعنی استوار است که محکم و مضبوط \nواهمین ومعتمد باشد. \n\nاستو\u200cذان؟ '
---
'اسب را کویند - و مردم \nمعتمد واعتمادی را ند کنته انه ۴ - و بمعنی \nآسثانه (۱) خانه ی افو اس \n\nاوستان بروزن دوستان » مردم آمین \nو هعتمد باشد ۴ - و بم\u200cنی ساخت و براق زین \nولجام اسب و آمتانٌ خانه عم هست 9 . \n\nآوستیم- با فوفانی بتحتایی کشيده\u200cوبيم \n\nزده ۰ آستن جامه راگونند - و بمشی خون \nباق کی و \n\nآو\u200cسو « نم اول بروز نک وکوء'
---
' آینه و تیغ وامثال \nو بضم اون وفتح اول وبابای فارسی هم احده\u200cاست - \n\nبز ۵ ییدان ۴ « بکر اول ۰ یمنی یال \nکردن زنگه از روی آمینه و ئیغ و امتال آزد \n\nبر دودن \u200c بروزن بربودن ۰ بمعئی \nبزدابیدن است که پاك کردن و جلا دادن زنگه \nباشد از دوی آبینه و تیغ و غیره . \n\nزد اه بروزن\u200cصفراه بلفت زسوپازند(۷) \nتخم زراعت را کوند ۵ مطلفاً بع'
---
```


## [2026-09-04T19:42:14.164Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nt2=open('MON_part2.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['امانت:','ایمان:','امن:','امین:','عمو:','عام:','عمه:','عموم:','عوام:']:\n    for name,txt in [('p1',t),('p2',t2)]:\n        for m in re.finditer(re.escape(pat),txt):\n            print(name,pat,repr(txt[m.start():m.start()+230]))\n            print('--')\nEOF"
}
```


### [2026-09-04T19:42:22.250Z] TOOL RESULT

```
p1 امانت: 'امانت: اهمقهه [ع. امانة] (مصل.) امین \nنودن. (اسص.) راستی» درستکاری؛ مس . \nخیانت. استواری. (.) مال يا چیزی که به \nزنهار» ودیمه. سته ممهور که به ستخانه \nدهند تا آن را به مقصدی برساند. (تفس.) \nتکالیفی که خدای تعالی برای خلق تعیین \nکر'
--
p1 امانت: 'امانت: (حق.) تصرف امین در \nمالی که نزد او به امانت گذاشته شده در \nجهتی مخالف مقصود امان تگذار. \n\n\n هچ\u200e \n\n\n"۴۹ \n\n\nخیست: ۲۵۷۳۵۱۵۵۷۰۸ [ع. خيبة] (مصل.) \nناامید گردیدن. زیانکار شدن. ناسپاس \nگشتنء کافر شدن. (امص.) نا کامی ناامیدی. \nزیان'
--
p2 امانت: 'امانت: آنکه لایق باشد امانتی \nبدو سیر ند. ( کد.) آدم ابو البشر. ضح. اشاره \nاست به آيةٌ ذیل: انا عرضنا الامانة علی \nالسموات و الارض و الجبال؛ فابین ان \nیحملنها و اشفقن منها و حملها الانسان» انه \nکان ظلوماً جهولا. قابل امتداد: امتدا'
--
p1 ایمان: 'ایمان: 2۳0 [غ.] 1( ج. یمین ؛ سو گندهاء \nسو گندان: ابمان مغلظه. " \nاینمان: ۱ [ع.] (مسصم .) گروبدن» \nعقده ی ایمن کر دن؛ بی\u200cبیم داشتن. باور \nشتن. (امص .) گروش» باورداشب» اعتقاد؛ \n1 ك_ کلمة «اشهد ان\u200cلالهالااللّه» را بر \nزبان راندن. \nا'
--
p1 ایمان: 'ایمان: 2« ((سص.) چایش» \nچاییدن. \n\nچاییدن: «:14-«تة [- چائیدن - چاهیدن| \n(مصل.) (چایید؛ چاید» خواهد چایید؛ ۰ \nچاییده» چایش» چایمان) سرما خوردن» \nناخوش شدن به سبب سرماخور دگی. \nچپ؛: 0 [- چب] (.) سار ایسر؛ مق. \nراست. (ص. ق.) ناراست» '
--
p2 ایمان: 'ایمان: ( کد.) کلمهٌ شهادت. (مس.) علامتی که \nدر طرت چپ حامل روی یکی از خطوط \nقرار می\u200cگیرد و کارش معین کردن اسم نوتی \nکه در روی همان خط وا \nموسیقی سه نوع کلید بکار می\u200cرود که یکی \nنوت «فا» و دیگر نوت «و» و سومی نوت \n«سل» را معرفی می\u200c'
--
p2 ایمان: 'ایمان: ( کد.) حجرالا سود. \n\n\nمحکک \nمجحک زرین: (کد.) سنگی که طلا را بدان \nامتحان کننك: ( کذد.) حجرالا سود. \nمسحکک: :0۳ ۱ع.] (افا.) خارش \nآورنده. (بز.) دوایی که در تماس با پوست \nبدن تولید خارش کند مانند کبیکج و گزنه. \n: ۱۱۱0۵016۵00 '
--
p1 امن: 'امن: 2 [ع.] (افا.) بسی\u200cبیم) سی\u200cخوف» \nایمن» به زینهار» در امن و امان» ج. امنون» \nامنین. \nآمنه (0-)210202 [- امنه] (ا.) پشته هیزم» \nبشتوارة هیزم» توده خرمن هیزم شکافته \nتس اتاصة (.) اشتان مرغان شکاری \nمانند باز ر عقاب» آشیانه. \nآموخ'
--
p1 امن: 'امن: 220 [ع.] (مص\u200cل.) بی بیم بودن ایمن \nشدن. (امص.) بی\u200cبیمی» بی\u200cترسی. اطمینان» \nآرامش قلب؛ مق. خوف. راحت» آساش. \n(ص.) در فارسی گاه به جای وصف «آمن» \nیعنی آرام و آسوده بکار رود. (تص.) جهان \nلایتغیری که حقبقت وجود در آنجا تحقق \nمی\u200cب'
--
p1 امن: 'امن: (0۳۷۰) ر2۳]20120 (۰) (مت.) لحنی \nاز موسیقی قدیم تقریبا مطابق بحر هزج \nاورانیو ۵ 3000 (1.) (شیم.) جسم بسیط \nفلری به علامت اختصاری () ) وزن \nمسخصوص آن */۱۸ و آن را از اوران \n\n\n۳۱۴ فرهنگ فارسی معین اورد \n\n\nضعیف رادیوا کتیو می\u200cبا'
--
p1 امن: 'امن: صحمصق-۲۰ [ < با کدامان] (مص\u200cمر.) \nپاک با کجامه» عفیف» با عفاف» خشکك \nدامن. \n\nپاکرای: ۳-8 آف. ع.] (ص\u200cمسر.) آنکه \nاند یشه\u200cای با ک دارد» صاحب رآی پا کث» \nبا کیزه رآی؛ دانا. \n\nپا کرو: («م)۳۷- [- پاکرونده] (افا. \nص\u200cمر.) پارساء عفی'
--
p1 امن: 'امن: ۱20۲ (ص مر.) آنکه دامنش \nمرطوب گردیده. ( کد.) فاسق؛ فاجر. عاصی» \nکار \n\nتر دد. ۵ (ع ۰] (مص\u200cل.) امد و شد \nکردن. دو دل شدن دو دله گردیدن. شکم \nراندن» اسهال گرفتن. (امص.) آمد و شد» \nرفت ۵ اف دو دلی. شکم روش» اسهال» \nج. تر ددات. \n'
--
p1 امن: 'امن: «مصقعه۱ [ع.] (مصل.) صامن \nیکدیگر شدن. \n\nتصحبه: (۵-)2رن2ها [ع. تضحه ] (مص م.) \nقربانی کردن گوسفند» شتر \nکدن \n\nتضرر: 1-2۳0 اع. (مص\u200cل.) زبان دیدن \nزیان بردن» ضرر کشیدن» خسران بردن. \n\n\nگر ند دیدن. \n\n\nتصرع: 3223۳۳0 [ع.] (مسصل.) خو'
--
p1 امن: 'امن: 325000 [ع.] (مسصل.) به راست \nگشتن» به سمت راست قرار گرفتن؛ مق \n)اس \nتیال" (- طبان)] (.) دیگ س رکشادة \nبز رگ دیگک بهن» باتبل. \nلیب 0 (ص.) س رگشته, مدهوش» حبران. \n3 (.) عشوه» فربب. دفع» رد سجن \nی وقتگذرانی ببهوده. شوخی» \nرشحند.'
--
p1 امن: 'امن: 20 [ع.] (عد. ترتسی» ص.) \nهشتم» هشتمین » امام تأمن. \n\nانوی: (07۷)] ۵3100۷ [ع.] (ص\u200cنسد.) منسوتب \nیه ثانبی» دومی» دو مسن. \n\n\n0۱۰ \n\n\nفرهنگ فارسی معین \n\n\nثانی \n\n\nثانی: آمةه (ع.] (افا. ثنی» عد. ترتیبی.) \nدوم» دویم. . جفت. ۳ \n\nثانیا'
--
p1 امن: 'امن: 2« [ - دامان] (.) دامان. دامن \nخورشید: (کد.) آسمان چهارم. روشنایی \nخورشید. دامن عمر: (کد.) اواخر عمر»پایان \nزندگانی. دامن قیامت: (کد.) روز قیامت؛ \nرستاخیز. دامن باغی گرفتن: (کد.) خلوت \nو گوشه\u200cنشین شدن. دامن به دندان \nگرقن: ( '
--
p1 امن: 'امن: دال بر سل \nشخص يا شی بر شخص يا شی دیگر است و \nآن از افزودن تر به صفت عادی نلاشت اند: \nبدتر. ب - صفت عالی: دال بر تفضیل \nشخص با شی بر همه افرادی که در آن \nصفت مشترکند» می\u200cباشد. نشانه آن رین \nاست که به صفت عادی پیوندد (با ین که'
--
p1 امن: 'امن: معصقد [ع.] (افا.) کسی که عهده\u200cدار \nغرامت کردد» بد یر فتار» یایندان» کفیل؛ ج. \nضوامن» ضمناء (غم.)» ضامنین. ضامن آهو: \nلقب امام رضاء نزد عوام» لیکن ضمانت از \n\n\n۱.۰۴ فرهنگ فارسی معیر ضایر \n\n\nآهو مسوب به علی بن حسین(ع) است \nمدیون'
--
p1 امن: 'امن: \nگوشة دامن. طرف کلاه: گوشهةٌ کلاه» کلاه \nگوشه. کنار» پایان چیزی. منتهی و پایان هر \nچیز؛ انتها. (نج.) برج سرطان. (ف.) کلیچة \nکم رکه برای آرایش بندند؛ کمربند. \n(مص\u200cم.) بر یکدیگر نهادن پلک\u200cها را؛ چشم \nبرهم زدن. برگردانیدن چیزی ر'
--
p2 امن: 'امن: ۵ (ع.] (افا.) بنهان شونده؛ \nبو شیده شو نده. \n\nکام ناکام \nخوای ناچار ناگز ی لته. \n\nکامنولث: 2700-۷615 [نر وت عمومی ] \n(امر.) (سیا.) مشترکث المنافع؛ مسجموعة \nکشورهای مرکب از بریتانیا و مستملکات \nسایق و کنونی آن که تشکیل یک واحد'
--
p2 امن: 'امن: \nگل سیکلمه» قعلامنیس آذریون, اذریون؛ \nاذریونه؛ ذهبیه» بنجة مریم. گل نورور: \n(گیا.) گیاهی است از تیرة پامچال\u200cها که بای \nاست و دارای ب رگک\u200cهای نرم و با ضخامت \nاست. گل\u200cهایش که در اوایل بهار ظاهر \nمی\u200cشو ند به شکل دسته\u200cهابی در انت'
--
p2 امن: 'امن: 0۱۵ [ع ۰] (.) جای امن جای \nسلامت» پناهگاه. مأمن رضا: جای امن و \nخشنودی. مشهد رصوی. \nمومن: ۱00 [ع.] (افا.) کسی که به خدا \nو رسول ایمان آورده: دارندة ایمان؛ با \nری ری ات ای \nمامور: ۱۱۲( [ع-] (امف.) فررمان داده؛ امر \nکرده شده. ک'
--
p2 امن: 'امن: \nزمینی که باران سطح آن را خراشیده باشد. \nقسمت فرودین کوه که آب از آن جاری \n9 ۳ . امراش» مر وش. \n\nمرشح: ۱0 [ع. ۳ (امف.) ترست شده. \nبتدر یج پروروده و آماده کشته برای کاری؛ \nتج مر شحین. \n\nمرشح: 0۱0۵۹۹۵ ۳2 (افاء) ترست کنندة \nفرزن'
--
p2 امن: 'امن: 03-20 آف. ع.] (.) جایی که امنست \nدر آن نست؛ اشفته» بر اشوب. \n\nناامید؛ 4نسهقه [- نااومید] (ص.) آنکه \nامید ندارد ماأٌیوس؛ مق. امیدوار. درمانده» \nسجاره. (عم.) محروم» بی\u200cنصیب (له.) \nناامیدی: :72-۰00 (حامص.) باون \nدر ماندگی» سجارگ'
--
p2 امن: 'امن: (- هامون] (.) زمین هموار» \nدشت. (فر ه.) سطح مستوی. \nهاموار: 21-۲ [- هموار ] (ص.) آنجه \nپستی و بلندی ندارد» مستوی» مسطح. (ق.) \nدایماء ببوسته) همیشه. \nهامون: ۸ (- هامن ] (.) ز مین و سیع \nهموار» دشت. صحرای بی\u200cدرخت» قاع. \nجای بست'
--
p1 امین: 'امین: 2-0« (۱.) شاشء بول. \n\nچانه: (م-)««ق (۰.) (جان.) استخوان زنخ» \nفک اسفل» دقن. \n\nجانه: (0-)602) (.) گلولة خمر شده؛ \nچونه. \n\nجانه: (620:)0 (۱.) سخن منئور؛ مق. چامه. \nجانه زدن: 22020 (مصل.) سیار سخن \nگفتن در هنگام خرید برای کم کر'
--
p1 امین: 'امین: 10 (ص نسد. آمر.) جراگاه» \nعلفرار. کاه» علف. \n\nچرانسیدن: (ند. -.۵-2010201066۲ [- \nچراندن] (مصم.) (چرانید» چراند» خواهد \nچرانبد» بجران جراننده» چرانیده) علف \nخورانیدن به حیوانات» گردش دادن \nحبوانات علفخوار در علفزارها تا جرا ک'
--
p2 امین: 'امین: ۸ ا(معر .] (.) ج\u200c. 4 ور \nضح.- «ایز ن تصرف فارسی زبانان عربی\u200cدان \nاست که جمع لفظ فارسی را بطور عربی \nآورده\u200cاند.» (غیاث. آنند.) ولی در عربی هم \nسستعمل است (المنجد). \nنرانج: ۳۹ آقس. فد رنحکد. \nدرفنجک. برفنجکک] (.) سنگینی که در '
--
p2 امین: 'امین: مأصقآ۷ (.) (بز.) ماده\u200cای که به \nمقدار سیار کم وجودش برای رشد و نمو و \nنگهداری و اعمال و اعضای بدن ضروری \nاست و فقدانش موجب بروز اختلالات \nمخصوص می\u200cگردد» چون بدن قادر به تهیه و \nساختن ویتامین نیست» علیهذا بایستی از \nخارج : ضم'
--
p2 امین: 'امین: «آسة" (.) وزنی است برابر بیست \nو پنج استار. ضح.اين سینا در قانون هامین را \nمعادل پنج استار و بیست درهم و چهار اوبو \n(ابولو) آورده (فرنظا.) \n\nهان: 20« [قس. کر.] (صت.) کلم تنسه است \nو آن برای موارد یل بکار رود: الف -برای \nآ گا'
--
p1 عمو: 'عمو: 2۳-5 [ع. قس. خالو] برادر پدر؛ عم \nافدر. گاه برای توهین به شخص گویند: «برو \nعمو!) به عم (عموی) خود خطاب کنند. به \nدم عامی یا به دوستان نزدیکك خود خطاب \nعمود: ۰704 (ع.] (.) ستون» چوب؛ خیمه. \nگرز. شاهین ترازو. رئیس قوم» مهتر. آل'
--
p1 عام: 'عام: (دس.) اسم جنس) مق. اسم خاص؛ علم. \nاسم فاعل: (دس.) اسمی است مشتق از فعل \nکه بر کنندة کاری با دارندة حالتی دلالت \nکند؛ صفت فاعلی. اسم فاعل از فعل امر (یا \nراشه فعل) با بساوند «نده» ساخته می\u200cشود. \nاسم مشتق مشتق: (دس.) اسمی که از'
--
p1 عام: 'عام: 22اه [ع۰] (سصم.) خورانیدن» \nطعام دادن» خورش دادن. اطعام مساکین: \nتهی\u200cدستان را طعام دادن. \n\nاطعمه: (6-)6102 21 [ع. اطمعة] .( ج. \nطعام؛ خورش\u200cها» خوردنی\u200cها» خوراک\u200cها." \nاطمفاء" ۱۶اه [ع. ف. اطمفا] (سص م.) \nفر ونشاندن» خاموش کردن»'
--
p1 عام: 'عام: 20 [ع. ِ\u200c. ۰ نعم؛ چاربابان؛ \nستوران. \n\nانعام: ات [ع. 8 (مص م ۰ نعمت دادن» \nیکی کردن» دهش کردن» بخشیدن. (امص.) \nدهش عطاء احسان. (.) آانجه که زاید بر \n\n\nحق اصلی به عنوان پاداش به کسی دهند؛ \nبخشش؟ ج. . انعامات. \n\nان\u200cعدام: 9( [ع.'
--
p1 عام: 'عام: ات [ع. 8 (مص م ۰ نعمت دادن» \nیکی کردن» دهش کردن» بخشیدن. (امص.) \nدهش عطاء احسان. (.) آانجه که زاید بر \n\n\nحق اصلی به عنوان پاداش به کسی دهند؛ \nبخشش؟ ج. . انعامات. \n\nان\u200cعدام: 9( [ع. ۰] (مسص\u200cل.) معدوم \n\nشدن» نیست شدن, نابود گشتن'
--
p1 عام: 'عام: بدبرابی عمومی. \nانجمن عام؛ مق. بار خاص. با رگاه سراير ده. \nبار: ۱(2.) دفعه» مرتبه» نویت: یک باره ده \n۳۱ \n\nبار: (پس.) پسوند مکان. به معنی ساحل و \nکنار؛ هندوبار» در یابار. گاه این سوند زاید \nباشد: جویبار (- جوی)» رودبار (- رود)'
--
p1 عام: 'عام: همه افراد» افراد \nبرگز بده و افراد عادی. (فل. منط.) امری که \nسبت به امر دیگر محدودتر و کم وسعت\u200cتر \nباشد» مانند انسان به حبوان که انسان خاص \nاست و حبوان عام. مال متعلق به شاه؛ مق. \nخرجی. خاص و خرجی: مخصوص و ممتاز \nو متعارفی و '
--
p1 عام: 'عام: راهی که \nمردم از آن عبور کنند. \n\nشارف؛: 94 [ع.] (ص.) کسی که بزودی \nشریف گردد. قدیم» کهن) ج. شرف» \nشرّف» شروف و شرف. (غم.) \n\nشار ق: 8570 [ع.] (افا.) تابان: تابنده» \nدرخشان. 0( افتاب. \n\nشارلاتان؛ 12120 (ص.) حقه\u200cباز» متقلب. \nشار'
--
p1 عام: 'عام: سهها (ع.] (.) خوردنی» خوراکك؛ \nج. اطعمه. طعام و شراب: خوردنی و \nآشامیدنی. نان و نت \n\nطعمان: ۰50 [ع.] (مسص\u200cعم.) نیزه زدن با \nیکدیگر \n\n\nطعم. رم 2 [ع.] () شبرینی و تلخی و \n\n\nشوری و ترشی و نمکینی و مانند آنها در \nخوردنی و نوشیدنی'
--
p1 عام: 'عام: ()2 [ع.] (افا.) همه را فرا گیرنده؛ \nعموم را فرا رسنده. (ا.) تمام (هر چه باشد.) \nهمگان» همه مردم؟ مق. خاص. مردم جاهل» \nنادان) مق. خاص. [- عامی] غبر سید؛ مسق. \nسید علوی. \n\nعسسام پسند: تن [ع. ف. <- \nعامپسندیده] (ص\u200cمف.) آنچه مقبو'
--
p1 عام: 'عام: (منط.) \nبل 239 \nحقیقت شود. عرض لازم: (منط.) عرضی \nاست که انفکاک آن از معروض خود محال \nباشد» مانند نویسندگی بالقوه برای انسان» در \nمقابل عرض مفارق که انفکاک آن از \nزایل شود یا بالقوه زوال آن به سرعت باشد \nو با بطوری کندی و بط '
--
p2 عام: 'عام: (دس.) ه رگاه فعل دلالت بر وجود \nو قوع مطلق کند و بر کار و عمل مخصوصی \nدلالت نداشته باشد فعل عام با فعل ربطی \nتارقف اضر قعل قاس زو \nفعلی است که صرف آن مطابق قیاس باشد؛ \nمق. سماعی. و آن بر دو تسم است: تام \nغیر تام. فعل قیاسی تا'
--
p2 عام: 'عام: کشتاری که در آن بر مرد و \nزن و بزرگ و کوچک و دوست و دشمن \nابقاء نکنند» کشتار عام. قتل عمد(ی): (حق.) \nقتلی که در عمل و قصد هر دو عمد باشد و \nآن هنگامی است که عاقل بالغی آهنگ \nکشتن به وسیله\u200cای که غالبا به آن قتل واقع \nگردد» کند'
--
p2 عام: 'عام: (ف.) هیولای اولای عالم \nاست که قابل تبدیل به صور و اشکال \nمختلف می\u200cباشد. ضح.- اگر در حرکات و \nتبدلات عالم خارج و جهان جسمانی \nبنگریم» مشاهده خواهیم که کرد که گاه \nتحولات حاصله در نوع واحد از موالید \nاست چنانگه نهالی بر اثر تب'
--
p2 عام: 'عام: (فل.) فیض \nمنبسط حق است» چنانکه گویند وجود عام \nمقابل با جمیع وجودات می\u200cباشد که بواسط \nنسب احدیت پدید امده\u200cاند (فرع. سج.) \nوجود عام سدیهی: (فل.) همان معنای \nمصدری انتزاعی و مفهوم اعتباری است که \nمابه\u200cالاشتراکث میان تمام اشیاه'
--
p2 عام: 'عام: (فق.) وقفی است که مقصود از \n\n\nان امور خر به است و مخصوص دسته و \n\n\nطبقه\u200cای معین نیست. مانند: وقف بر فقرا و بر \nطلاب و مدارس و مساجد) مق. وقت \nخاص. غطهة وقف: (فق.) متولیان و ادارات \nاوقاف موظف هستند که همواره نسبت به \nموقوفات چ'
--
p1 عمه: 'عمه: (6-)6102 21 [ع. اطمعة] .( ج. \nطعام؛ خورش\u200cها» خوردنی\u200cها» خوراک\u200cها." \nاطمفاء" ۱۶اه [ع. ف. اطمفا] (سص م.) \nفر ونشاندن» خاموش کردن» فرو کشتن آتش \nو چراغ» اطفاء نايرة شهوات. \n\nاطفائیه: (0-)02-۱7۰» [ع.] (ص\u200cنسب. امر.) \nاداره\u200cای که و'
--
p1 عمه: 'عمه: (0-)۱۵۵2 [- طعمه ) (۰) خوردنی» \nخوراکك» غذا؛ ج. طعم. تیولی که از محل \nخالصه\u200cهای دیوان می\u200cدادند. (دورة پیش از \nسلجوقیان). \n\nطعن: ها [ع.] (مص\u200cم.) نیزه زدن. عیب \nکسی را گفتن» سرزنش کردن» ملامت \nکردن. کنایه زدن» کنایه گفتن. (امسص'
--
p1 عمه: 'عمه: ()مسصد [ع. عمه ] (.) خواهر پدر. \nعمی: قدد [ع.] (امص.) کوری» نایینائی. \n(تص.) مرتبهةً حقبقة الحقائق است» چه آنکه \nاگر وجود به شرط لحاظ شود مرتبةٌ احدیت \nو جمع الجمع و حقیقة الحقائق و عمی نامند \nکه تمام اسما و صفات مستهلک در آن'
--
p2 عمه: 'عمه: (ه-)همحصهقه [ع. . ناعمه ] (افا. ص.) \nمونث ناعم. نرم و لین. دختر نیکو زندگانی \nو نیکو خورش. درختی که برگک آن نرم \nو و \n\nناعی: 71« (ع. (افا.) آنکه خبر مرگث کسی \nرا آورد؛ خبر مرک دهنده. خر ید دهنده. \nناغوش: ۵( (۱.) سر به ات فرو '
--
p2 عمه: 'عمه: (م)مسسنه [ع. نسغمه ] (.) اواز \nخوش, آهنگ. (م.) توالی یک رشته \nاصوات موسیقی با امتدادهای مختلف که از \nشنیدن مجموع آنها لذتی درک شود. اساس \nو پايةٌ موسیقی بر نغمه نهاده شده و میزان \nتأثر آن خوبی و بدی نغمه را نشان می\u200cدهد. \nضح.-'
--
p2 عموم: 'عموم: : 1012111 [ع. ۰[ (امة ) غمزرده» \nغتخیا ۳ اندوهگین)؛ مق. مسرورء شاد \nخو شحال. ج.- مغمومین. \n\nمغناطیس: و۲ (.) (شیم.) ا کسید \nطبیعی مفناطیسی آهن را گویند که خاصیت \nجذب براده\u200cهای آهن را دارد و فرمولش \n۳ مسیي\u200cاشد. زک ساه و وزن \n\n'
--
p1 عوام: 'عوام: 2( عامه) مق \nخواص. ضسح.- در تداول چ. عام گیرند. \nضح.- در فارسی گاه بحای مفرد (عام) آید. \nعوام\u200cالناس. \n\nعسوامفسسریب: 2.10 [ع. ف \nعوام\u200cفریبنده] (ص\u200cفا.) آنکه عوام را شرت \nآنکه مردم را گول زند. \n\nعرام\u200cفنهم: 2-7 [ع.] (ص\u200cمر.) آنچه'
--
p2 عوام: 'عوام: خطایی که \nعوام در تلفظ کلمه یا معنیی مر تکب شوند؛ \n\n\nفرهنگ فارسی معین تس \n\n\nمثلاً تعینات به معنی شخصی که تعبین \nگردیده باشد به طرفی يا کاری. غلط مشهور: \n(اد.) کلمه\u200cای که از لحاظ لغت و دستور زبان \nغلط ولی سیار رایج و متداول ا'
--
p2 عوام: 'عوام: (تص.) استبدال \nمتاغ اخروی باقی به حطام دنیوی فانی (فرع. \n\n\nکیمیااثر: :هت [معر. ع.] (ص\u200cمر.) هر \nچیز که قلب ماهبت اشیا کند همچون اکسیر. \nکنهتا کر ۷-۲ [معر. ف.] (ص\u200cفا.) آنکه \nفلرات ناقص را به فلزات کاملتر تبدیل کند. \nمکار» حبله'
--
```


## [2026-09-04T19:42:42.753Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN\"; grep -n -i -o \"\\bamānat\\b.\\{0,120\\}\\|\\bamu\\b.\\{0,120\\}\\|'amm.\\{0,100\\}\" HRN.txt | head -5; echo \"(HRN count amin)\"; grep -c -i \"amin\" HRN.txt; echo \"== HUB\"; grep -n -i -o \"\\bamān.\\{0,120\\}\" HUB.txt | head -5; echo \"== ARY latin\"; grep -n -i -o \"AMEN.\\{0,120\\}\\|AMM.\\{0,100\\}\" incoming/ARY/ARY_latin_index_pages.txt | head -6; echo \"== BQT عمو headword\"; python3 -c \"\nimport re\nt=open('BQT_v2.txt',encoding='utf-8',errors='replace').read()\nfor m in list(re.finditer('عمو',t))[:4]: print(repr(t[m.start()-60:m.start()+120]))\n\""
}
```


## [2026-09-04T19:42:42.880Z] TOOL CALL #27: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py; echo ====; sed -n '1,40p' tools/verify_check.py"
}
```


### [2026-09-04T19:42:44.543Z] TOOL RESULT

```
== HRN
4823:'Amme (vd. 15 (29) (Gl.); ai. [XrfA^-, dlidyaü
4824:'Amme, Erzieher etc. (H. No. 78).
(HRN count amin)
6
== HUB
== ARY latin
1426:AMENITAN
1713:AMEN (RUSSIAN) yoy E’SMAN KURDISH) 53,
1714:AMEN (CZECH) Sx ASMAN AAFGHAND (24) glii)
1715:AMEN (BULGARIAN) ¢5 ji, ASHMAN, (SANSKRIT) 2, Suite
1720:AMMARR
1722:AMMER) 463 HOMER — (OLD FRISIAN) 4S 53.3
== BQT عمو headword
'دی \nومشهدی) . \nمکی\u200cنژاد(فخرالدین)» رئیس بانك ملی رشت (لفات معمول در اراك (سلطانآ باد)» \nکرمانشاه وبروجرد). \nوحدت (صادق) ۰ رس سایق دفتر اداری تیپ مستقل کرمانشاه ( لغات تعمل \nدر کرما'
'لغت و کنایت \n\n\nجر = بفتح اول و سکون انی » هر \nشکافی\u200cرا کویندعمومآوزمدنشکافتهرا خصوصاً ۱ _ \nو با تشدید ثانی در عربی بمعنی کشبدن و اخذ \nکردن باشد یعنی بچاپلوسی و شیرین زبانی از \nکی چ'
'ن روز هم خرداد تام دارد \nمنابر قاعدءٌ کله\u200cای که تزد فارسان معمول است \n\n\nبر افتاد از بیم بر وی جشن . \nسهیلی « لفت فرس ** >. \n\n\n۴ اوستا . 735۳08 , بهلوی 25107[ با ۷25100 ( جشن ) « اس'
'\nگذارد ۰ \n\nجند ره = بروزن\u200cپنجره. هرچوب گند: \nناتراشیده باشد عموما و دو چوب بقدرنیم کز که \n\n\nبجهت کوفتن و هموار ساختن رخوت پوشیدلی \n\n\n)۱ چك :توالنگی. \n\n\n(۷) خم ۱ \n\n\nور رار رز ون 2 د'
```


### [2026-09-04T19:42:44.579Z] TOOL RESULT

```
Exit code 1
#!/usr/bin/env python3
"""Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
"""
import sys, os, json, hashlib, re, html, time, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "data", "verification", "sources", "web")
INDEX = os.path.join(WEB, "index.jsonl")
UA = "rishe-verification/1.0 (+https://github.com/sfmqrb/rishe; etymology source archiving)"


def html_to_text(s):
    s = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</tr>|</h[1-6]>", "\n", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    return s.strip()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    note = ""
    if "--note" in sys.argv:
        note = sys.argv[sys.argv.index("--note") + 1]
        args = [a for a in args if a != note]
    if not args:
        print(__doc__); return 2
    url = args[0]
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]
    # IRI -> URI: percent-encode non-ASCII path/query characters so urllib accepts them
    parts = urllib.parse.urlsplit(url)
(eval):1: === not found
```


## [2026-09-04T19:42:48.218Z] TOOL CALL #28: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-04T19:42:48.256Z] TOOL RESULT

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


## [2026-09-04T19:43:00.307Z] TOOL CALL #29: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/amen\" \\\n \"https://www.etymonline.com/word/amen\" \\\n \"https://en.wiktionary.org/wiki/%D8%B9%D9%85%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%D8%B9%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D8%B9%D8%A7%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D9%85%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D9%85%DB%8C%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%85%D8%A7%D9%86%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%D8%A3%D9%85%D9%8A%D9%86\" \\\n \"https://en.wiktionary.org/wiki/Immanuel\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 52, roots A'.m.m / A.m.n — Semitic root, Arabic/Persian/Hebrew/English nodes\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-04T19:43:08.048Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b96d897a633c2072.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/da70ede2c8128c5f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f1ab2352328995b1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/416ebeaa01da7cf8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/58871eaeebab7247.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/75b710798002813b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/564d0d4b70abef85.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ce06a540b19cce1e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e8fe7d9edb626aeb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/716cb31c45066f7e.txt
```


## [2026-09-04T19:43:10.650Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"===== amen wikt\"; grep -n -A4 -i \"Etymology\" b96d897a633c2072.txt | head -60"
}
```


### [2026-09-04T19:43:10.696Z] TOOL RESULT

```
===== amen wikt
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
117: Etymology 
118-
119- 3.2 
120- Pronunciation 
121-
--
134: Etymology 1 
135-
136- 4.1.1 
137- Pronunciation 
138-
--
146: Etymology 2 
147-
148- 4.2.1 
149- Pronunciation 
150-
--
166: Etymology 
167-
168- 5.2 
169- Pronunciation 
170-
--
180: Etymology 
181-
182- 6.2 
183- Pronunciation 
184-
--
203: Etymology 
204-
205- 7.2 
206- Pronunciation 
207-
--
220: Etymology 
221-
222- 8.2 
223- Pronunciation 
224-
--
251: Etymology 
252-
253- 10.2 
254- Pronunciation 
255-
--
276: Etymology 
277-
278- 12.2 
279- Interjection 
280-
--
```


## [2026-09-04T19:43:13.986Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i -o \"Ancient Greek.\\{0,300\\}\\|Late Latin.\\{0,250\\}\\|Hebrew .\\{0,250\\}\" b96d897a633c2072.txt | head -12; echo \"==== ETYMONLINE amen\"; grep -n -i -o \"amen.\\{0,400\\}\" da70ede2c8128c5f.txt | sed -n '1,8p'"
}
```


### [2026-09-04T19:43:15.516Z] TOOL RESULT

```
746:Hebrew אָמֵן bor. 
753:Ancient Greek ἀμήν ( amḗn ) , from Biblical Hebrew אָמֵן ( ʾāmēn , “ certainly, verily ” ) (cognate with Arabic آمِينَ ( ʔāmīna ) , Classical Syriac ܐܡܝܢ ( ʾāmên ) ).
877:Ancient Greek: ἀμήν ( amḗn ) 
1023:Ancient Greek: ἀμήν ( amḗn ) 
1244:Ancient Greek ἀμήν ( amḗn ) , from Hebrew אמן ( amén , “ certainly, truly ” ) .
1463:Ancient Greek ἀμήν ( amḗn ) , from Biblical Hebrew אמן ( amén , “ certainly, truly ” ) .
1510:Ancient Greek ἀμήν ( amḗn ) , from Biblical Hebrew אָמֵן ( ʾāmēn , “ certainly, truly ” ) .
1543:Ancient Greek ἀμήν ( amḗn ) , from Biblical Hebrew אָמֵן ( ʾāmēn , “ certainly, truly ” ) .
1603:Ancient Greek ἀμήν ( amḗn ) , from Hebrew אמן .
1682:Ancient Greek ἀμήν ( amḗn ) , from Biblical Hebrew אָמֵן ( ʾāmēn , “ certainly, truly ” ) .
1745:Hebrew אָמֵן . Cognate with Arabic آمِين ( ʔāmīn ) , Aramaic אַמִין ( ʾamīn ) , Classical Syriac ܐܰܡܺܝܢ ( ʾamīn ) .
1758:Late Latin , Medieval Latin , Ecclesiastical Latin ; Christianity ) 
==== ETYMONLINE amen
1:amen
4:Amen - Etymology, Origin & Meaning
6:Amen - Etymology, Origin & Meaning 
21:amen 
23:amen (interj.) 
25:amen , from Ecclesiastical Greek amen , from Hebrew amen "truth," used adverbially as an expression of agreement (as in Deuteronomy xxvii.26, I Kings i.36), from Semitic root a-m-n "to be trustworthy, confirm, support."
27:Amen corner is attested from 1860.
35:amen...
```


## [2026-09-04T19:43:21.437Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '740,760p' b96d897a633c2072.txt; echo \"======= عمو Persian\"; grep -n -i -o \"Etymology.\\{0,60\\}\\|Borrowed from.\\{0,250\\}\\|From Arabic.\\{0,250\\}\\|Persian\\b.\\{0,120\\}\" f1ab2352328995b1.txt | head -20"
}
```


### [2026-09-04T19:43:23.207Z] TOOL RESULT

```
 " Amen " in an 1845 translation of the Sermon on the Mount by Owen Jones 
 Etymology
 [ edit ] 

 Etymology tree

 Biblical Hebrew אָמֵן bor. 
 Koine Greek ᾱ̓μήν ( āmḗn ) bor. 
 Ecclesiastical Latin āmēn der. 
 Old English āmen 
 Middle English amen 
 English amen 

 Inherited from Middle English amen , from Old English āmen , from Ecclesiastical Latin āmēn , from Ancient Greek ἀμήν ( amḗn ) , from Biblical Hebrew אָמֵן ( ʾāmēn , “ certainly, verily ” ) (cognate with Arabic آمِينَ ( ʔāmīna ) , Classical Syriac ܐܡܝܢ ( ʾāmên ) ).

 In Old English, it was used only at the end of the Gospels; elsewhere, it was translated as sōþlīċe ! ( “ truly, indeed! ” ) , swā hit is ( “ so it is ” ) , and sīe ! ( “ [so] be it! ” ) .

 Pronunciation
 [ edit ] 

 ( Received Pronunciation ) IPA ( key ) : /(ˌ)ɑːˈmɛn/ , ( uncommon, chiefly for strong agreement ) /(ˌ)eɪˈmɛn/ 
======= عمو Persian
62:Etymology 
74:Persian 
76:Persian subsection 
79:Etymology 
102:Etymology 
183:Etymology
186:Etymology tree
223:Persian
226:Persian Wikipedia has an article on: عمو 
230:Etymology
238:Persian ) IPA ( key ) : /ʔa.ˈmoː/ 
280:Persian
290:Persian , Iran ) paternal uncle 
392:Persian dialectal kinship terms
394:Persian dialectal kinship terms
400:Persian
534:Persian dialectal kinship terms
536:Persian dialectal kinship terms
662:Etymology
665:Etymology tree
```


## [2026-09-04T19:43:25.829Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '180,245p' f1ab2352328995b1.txt"
}
```


### [2026-09-04T19:43:25.869Z] TOOL RESULT

```
 Egyptian Arabic
 [ edit ] 

 Etymology
 [ edit ] 

 Etymology tree

 Arabic عَن ( ʕan ) 

 Arabic مَا ( mā ) 

 Arabic عَمّ ( ʕamm ) 
 Egyptian Arabic عمّ ( ʕamm ) 

 Egyptian Arabic -ـو ( -u ) 

 Egyptian Arabic عمو 

 From عمّ ( ʕamm ) + -ـو ( -u ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ʕammu/ 

 Noun
 [ edit ] 

 عمو • ( ʕammu )  m ( feminine عمتو ( ʕammitu ) ) 

 endearing form of عم ( ʕamm , “ uncle ” ) : uncley 

 possisive form of عم ( ʕamm , “ uncle ” ) : his uncle
 alternative spelling of عمه 

 ( informal ) Term of address to older male strangers 

 Usage notes
 [ edit ] 

 As a term of address, it is used very often by children, and less often by teenagers.

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: عمو 

 Wikipedia fa 

 Etymology
 [ edit ] 

 From عم ( amm , “ uncle ” ) +‎ ـو ( -u  / -o , diminutive suffix ) . Compare Tajik амак ( amak ) , formed from the same root with a different diminutive suffix.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔa.ˈmoː/ 

 ( Dari, formal ) IPA ( key ) : [ʔä.moː] 

 ( Dari, formal ) IPA ( key ) : [ʔä.moː] 
 ( Kabuli ) IPA ( key ) : [ʔä.moː] 

 ( Hazaragi ) IPA ( key ) : [ʔä.mʊː]
```


## [2026-09-04T19:43:31.030Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== عم\"; grep -n -i -o \"From the root.\\{0,200\\}\\|ع م م.\\{0,200\\}\\|Semitic.\\{0,250\\}\\|paternal uncle.\\{0,120\\}\" 416ebeaa01da7cf8.txt | head -14; echo; echo \"=== عام\"; grep -n -i -o \"Etymology.\\{0,40\\}\\|From .\\{0,220\\}\" 58871eaeebab7247.txt | sed -n '1,25p'"
}
```


### [2026-09-04T19:43:32.746Z] TOOL RESULT

```
=== عم
294:ع م م ( ʕ m m ) 
1471:paternal uncle ” ) 
1791:paternal uncle ( “ brother of one's father ” ) 
1808:paternal uncle ” ) .
1820:paternal uncle 
1898:ع م م 
1909:paternal uncle ( father's brother ) 
1946:ع م م 
1992:ع م م 

=== عام
62:Etymology 1 
77:Etymology 2 
92:Etymology 3 
112:Etymology 1 
121:Etymology 2 
133:Etymology 3 
147:Etymology 1 
156:Etymology 2 
176:Etymology 
269:From Wiktionary, the free dictionary
274:Etymology 1
283:from Old South Arabian 𐩲𐩣 ( ʿm /⁠*ʿām⁠/ , “ year ” ) . Compare Ge'ez ዓም ( ʿam , “ year ” ) .
473:Etymology 2
482:from the active participle of عَمَّ ( ʕamma , “ to be general , to be common , to prevail ” ) (cognate to Hebrew עַם ( am , “ nation ” ) and עֲמָמִי ( 'amamí , “ public ” ) ). Contamination from Parthian 𐫍𐫀𐫖 ( hʾm /⁠hām-⁠/ , 
725:Etymology 3
1014:etymology. Notes on the Persian and Arabic lexico
1014:from a Parthian **hām ( “ winter; year ” ) , a word he seemingly made up, since no descendant of Proto-Iranian *jimáh ( “ winter ” )  could come close.
1023:Etymology 1
1032:from Arabic عَام ( ʕām ) .
1047:Etymology 2
1056:from Arabic عَامَ ( ʕāma ) .
1145:Etymology 3
1154:from Arabic عَامّ ( ʕāmm ) .
1182:Etymology 1
1185:from Arabic عَام ( ʕām ) .
```


## [2026-09-04T19:43:40.208Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 75b710798002813b:ایمان 564d0d4b70abef85:آمین ce06a540b19cce1e:امانت e8fe7d9edb626aeb:أمين; do n=${f%%:*}; w=${f##*:}; echo \"===== $w\"; grep -n -i -o \"Etymology.\\{0,30\\}\\|from .\\{0,200\\}\\|From .\\{0,200\\}\\|Borrowed.\\{0,200\\}\" $n.txt | sed -n '1,22p'; done"
}
```


### [2026-09-04T19:43:41.795Z] TOOL RESULT

```
===== ایمان
62:Etymology 
76:Etymology 
96:Etymology 
119:Etymology 
142:Etymology 
238:From Wiktionary, the free dictionary
245:Etymology
248:Etymology tree
255:Borrowed from Classical Persian اِیمَان ( īmān ) , borrowed from Arabic إِيمَان ( ʔīmān ) , from آمَنَ ( ʔāmana ) . Compare Old Hindi इमांन ( imā̃n ) .
274:Etymology
277:Etymology tree
283:Borrowed from Arabic إِيمَان ( ʔīmān ) , from آمَنَ ( ʔāmana ) .
331:Etymology
334:Etymology tree
340:Borrowed from Arabic إِيمَان ( ʔīmān ) , from آمَنَ ( ʔāmana ) .
401:from Arabic 
441:Etymology
444:Etymology tree
452:from Old Punjabi اِیمان ( īymān ) , borrowed from Classical Persian اِیمَان ( īmān ) , borrowed from Arabic إِيمَان ( ʔīmān ) , from آمَنَ ( ʔāmana ) .
521:from Arabic 
537:Etymology
540:Etymology tree
===== آمین
62:Etymology 
76:Etymology 
151:From Wiktionary, the free dictionary
158:Etymology
161:Etymology tree
175:Borrowed from Arabic آمِينَ ( ʔāmīna ) , borrowed from Classical Syriac ܐܰܡܺܝܢ ( ʾāmēn ) or Aramaic אַמִין ( ʾāmēn ) .
192:Etymology
195:Etymology tree
209:Borrowed from Arabic آمِينَ ( ʔāmīna ) , borrowed from Classical Syriac ܐܰܡܺܝܢ ( ʾāmēn ) or Aramaic אַמִין ( ʾāmēn ) .
272:from " https://en.wiktionary.org/w/index.php?title=آمین&oldid=92030779 "
274:from Arabic 
275:from Classical Syriac 
276:from the Arabic root ء م ن 
277:from Aramaic 
278:from the Biblical Hebrew root א־מ־ן 
279:from Biblical Hebrew 
280:from Koine Greek 
281:borrowed from Arabic 
284:from Classical Syriac 
285:from the Arabic root ء م ن 
286:from Koine Greek 
287:from Arabic 
===== امانت
70:Etymology 
81:Etymology 
101:Etymology 
112:Etymology 
132:Etymology 
146:Etymology 
231:From Wiktionary, the free dictionary
246:Etymology
249:Borrowed from Pashto امانت or Urdu امانت , from Persian امانت , ultimately from Arabic أَمَانَة ( ʔamāna ) .
261:Etymology
264:Borrowed from Arabic أَمَانَة ( ʔamāna , “ trust, reliability; deposit ” ) . 
326:Etymology
329:Borrowed from Arabic أَمَانَة ( ʔamāna ) . 
341:Etymology
344:Etymology tree
350:Borrowed from Arabic أَمَانَة ( ʔamāna ) , from أَمُنَ ( ʔamuna ) .
434:Etymology
437:Borrowed from Classical Persian امانت ( amānat ) , from Arabic أَمَانَة ( ʔamāna ) .
456:Etymology
459:Etymology tree
466:Borrowed from Classical Persian اَمَانَت ( amānat ) , borrowed from Arabic أَمَانَة ( ʔamāna ) , from أَمُنَ ( ʔamuna ) .
536:from the Arabic root ء م ن (0 c, 8 e) 
===== أمين
62:Etymology 1 
95:Etymology 2 
170:From Wiktionary, the free dictionary
183:Etymology 1
710:Etymology 2
725:from " https://en.wiktionary.org/w/index.php?title=أمين&oldid=88976922 "
```


## [2026-09-04T19:44:09.815Z] TOOL CALL #36: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D7%A2%D6%B7%D7%9D\" --note \"page 52, root A'.m.m: Hebrew 'am 'people'\" | tail -1; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D7%A2%D6%B4%D7%9E%D6%BC%D6%B8%D7%A0%D7%95%D6%BC%D7%90%D6%B5%D7%9C\" --note \"page 52, root A'.m.m: Hebrew Immanuel\" | tail -1"
}
```


## [2026-09-04T19:44:11.407Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FVQ amin/aman\"; grep -n -i -o \".\\{60\\}\\bAm[iī]n\\b.\\{0,160\\}\" FVQ_pages.txt | head -8; echo \"== FVQ iman\"; grep -n -i -o \".\\{40\\}\\b[Iī]m[aā]n\\b.\\{0,160\\}\" FVQ_pages.txt | head -6"
}
```


### [2026-09-04T19:44:12.343Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/64ac72685954b530.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9de79576c342c2af.txt
```


### [2026-09-04T19:44:14.300Z] TOOL RESULT

```
== FVQ amin/aman
== FVQ iman
```


## [2026-09-04T19:44:19.812Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== עם\"; grep -n -i -o \"Etymology.\\{0,25\\}\\|From .\\{0,220\\}\\|root .\\{0,150\\}\\|Proto-Semitic.\\{0,200\\}\" 64ac72685954b530.txt | head -14; echo \"=== Immanuel heb\"; grep -n -i -o \"From .\\{0,250\\}\\|God is with us.\\{0,120\\}\" 9de79576c342c2af.txt | head -8; echo \"=== Immanuel en\"; grep -n -i -o \"From .\\{0,250\\}\\|Hebrew.\\{0,200\\}\" 716cb31c45066f7e.txt | head -8"
}
```


### [2026-09-04T19:44:21.336Z] TOOL RESULT

```
=== עם
=== Immanuel heb
=== Immanuel en
261:From Wiktionary, the free dictionary
274:From Hebrew עִמָּנוּאֵל ( ʿimanuʾél ) , from עִמָּנוּ אֵל ( ʿimánu ʾél , literally “ God is with us ” ) .
295:from Hebrew : alternative form of Emmanuel .
389:from Hebrew , more popular as Emanuel 
404:from Hebrew 
444:from Biblical Hebrew עִמָּנוּאֵל ( imanu'él , literally “ God is with us ” ) . [ 1 ] 
464:from Biblical Hebrew , rare in this form. Short forms: Immo , Manu 
1122:from the Digital and Population Data Services Agency of Finland.
```


## [2026-09-04T19:44:27.784Z] TOOL CALL #39: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D7%A2%D7%9D\" --note \"page 52, root A'.m.m: Hebrew 'am 'people' / 'im 'with'\" | tail -1"
}
```


### [2026-09-04T19:44:30.049Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9e232c37d6dceaed.txt
```


## [2026-09-04T19:44:32.927Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i -o \"Proto-Semitic.\\{0,200\\}\\|Etymology 1.\\{0,20\\}\\|From .\\{0,220\\}\\|Hebrew.\\{0,150\\}\" 9e232c37d6dceaed.txt | sed -n '1,20p'"
}
```


### [2026-09-04T19:44:34.654Z] TOOL RESULT

```
71:Hebrew 
73:Hebrew subsection 
76:Etymology 1 
126:Etymology 1 
221:From Wiktionary, the free dictionary
248:Hebrew
251:Etymology 1
280:Hebrew pausal form עָם ) [pattern: קֶטֶל ] 
283:from under the burdens of the Egyptians. 
453:from Babylon unto Jerusalem. 
470:from the otherwise archaic preposition אֵת, אֶת־ ( et, et- , “ to, with ” ) (not to be confused with the direct object marker את ( et ) , which is still in use). The traditional, more regular forms are still in use, but only 
589:Etymology 1
609:from Hebrew עַם ( am , “ nation ” ) 
628:from " https://en.wiktionary.org/w/index.php?title=עם&oldid=90051463 "
635:Hebrew terms belonging to the root ע־מ־ם 
636:Hebrew terms with IPA pronunciation 
637:Hebrew/am 
638:Hebrew/am/1 syllable 
639:Hebrew/im 
640:Hebrew/im/1 syllable
```


## [2026-09-04T19:44:39.177Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '248,300p' 9e232c37d6dceaed.txt | head -40; echo \"....\"; grep -n -B2 -A6 \"Etymology 2\" 9e232c37d6dceaed.txt | head -40"
}
```


### [2026-09-04T19:44:39.228Z] TOOL RESULT

```
 Hebrew
 [ edit ] 

 Etymology 1
 [ edit ] 

 Root 

 ע־מ־ם ( ʿ-m-m ) 

 3 terms 

 Compare with Arabic عَامّ ( ʕāmm , “ general, public ” ) , Arabic عَمّ ( ʕamm , “ paternal uncle ” ) , Aramaic עַמָּא , and Egyptian ꜥꜣm ( “ an Asian, a member of Semitic tribes ” ) .

 Pronunciation
 [ edit ] 

 ( reconstructed Biblical ) IPA ( key ) : /ʕam/ , [ʕam] 

 ( Tiberian ) IPA ( key ) : /ʕam/ , [ʕaːm] 

 ( Modern Israeli ) IPA ( key ) : /am/ 

 ( Yemenite ) IPA ( key ) : /ʕam/ , [ʕæm] 

 Rhymes: -am 

 Rhymes: -im 

 Noun
 [ edit ] 

 עַם • ( am )  m ( plural indefinite עַמִּים , singular construct עַם־ , plural construct עַמֵּי־ , Biblical Hebrew pausal form עָם ) [pattern: קֶטֶל ] 

 A nation , a people .
 Tanach , Exodus 6:7 , with translation of the King James Version : וְלָקַחְתִּי אֶתְכֶם לִי לְ עָם וְ הָיִיתִי לָכֶם לֵאלֹקִים וִידַעְתֶּם כִּי אֲנִי ה׳ אֱלֹקֵיכֶם הַ מּוֹצִיא אֶתְכֶם מִתַּחַת סִבְלוֹת מִצְרָיִם׃ And I will take you to me for a people , and I will be to you a God: and ye shall know that I am the Lord your God, which bringeth you out from under the burdens of the Egyptians. 

 Usage notes
 [ edit ] 

....
98-
99- 2.2 
100: Etymology 2 
101-
102- 2.2.1 
103- Pronunciation 
104-
105- 2.2.2 
106- Preposition 
--
133-
134- 3.2 
135: Etymology 2 
136-
137- 3.2.1 
138- Pronunciation 
139-
140- 3.2.2 
141- Noun 
--
405- H5971 in Strong, James ( 1979 ), Strong’s Exhaustive Concordance to the Bible 
406-
407: Etymology 2
408- [ edit ] 
409-
410- Cognate with Ugaritic 𐎓𐎎 ( ʿm ) and, via metathesis, Arabic مَعَ ( maʕa ) and Ugaritic 𐎎𐎓 ( mʿ ) .
411-
412- Pronunciation
413- [ edit ] 
--
604- ( Northeastern ) dative of עס ( es ) : to it 
605-
606: Etymology 2
607- [ edit ] 
608-
609- Borrowed from Hebrew עַם ( am , “ nation ” ) 
610-
611- Pronunciation
612- [ edit ]
```


## [2026-09-04T19:44:54.344Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AFA amen\"; grep -n -i -o \".\\{40\\}amen.\\{0,120\\}\" AFA.txt | grep -i -v \"amentl\\|argument\\|moment\" | head -6; echo \"== PLA\"; grep -n -i -o \"\\bamān.\\{0,120\\}\\|\\bʾamm.\\{0,100\\}\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -5; echo \"== SKT Amen entry\"; grep -n -i -o \".\\{60\\}Heb\\..\\{0,200\\}\" SKT.txt | grep -i \"amen\\|truth\\|verily\" | head -5; echo \"== AFM أمن\"; grep -c \"امين\\|أمين\" AFM.txt"
}
```


### [2026-09-04T19:44:56.267Z] TOOL RESULT

```
== AFA amen
1146:egangen ist. Bei einem fremden Werkzeugnamen
2010:isabür und Herat (äJ.^^d) nach Arabien kamen, so
2013:e einem nicht sehr seltenen Stoffe den Namen gegeben
2461:in solches Eügelchen führt aramäischen Namen
2478:ägt zunächst einen t.*chten arabischen Namen äo.
2601:em persisciieu und einem aramiii.scheu Namen be-
== PLA
ugrep: error: error at position 70
|Ā)n(?:[^\n\x80-\xbf][\x80-\xbf]*){0,120}|\(?:b|B)ʾamm(?:[^\n\x80-\xbf][\x80-
                               mismatched ( )___/


== SKT Amen entry
19660:al.* llcb.  tvmmitn,  pi.  of  tSm^  perfectioo, truth.  —  Heb.  root  fdmam.  to  b*  perfect
== AFM أمن
2
```


## [2026-09-04T19:45:15.691Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -c 64ac72685954b530.txt 9de79576c342c2af.txt e8fe7d9edb626aeb.txt; echo \"== أمين etym1\"; sed -n '183,215p' e8fe7d9edb626aeb.txt"
}
```


### [2026-09-04T19:45:15.733Z] TOOL RESULT

```
  144 64ac72685954b530.txt
  192 9de79576c342c2af.txt
10823 e8fe7d9edb626aeb.txt
11159 total
== أمين etym1
 Etymology 1
 [ edit ] 

 Related to أَمِنَ ( ʔamina , “ to be safe ” ) , أَمُنَ ( ʔamuna , “ to be faithful ” ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ʔa.miːn/ 

 Rhymes: -iːn 

 Adjective
 [ edit ] 

 أَمِين • ( ʔamīn ) ( masculine plural أُمَنَاء ( ʔumanāʔ ) ) 

 reliable , trustworthy , loyal , responsible 

 upright , honest 

 faithful , true , truthful , authentic , honest , sincere , trusty , dependable 

 safe , secure 
 609–632 CE , Qur'an , 95:3 : وَهَٰذَا ٱلۡبَلَدِ ٱلۡأَمِينِ wahāḏā l-baladi l-ʔamīni and this secure city ˹of Mecca˺! 

 innocuous , harmless 

 ( defined ) The archangel Gabriel 
 Synonyms: جِبْرِيل ( jibrīl ) , جِبْرَائِيل ( jibrāʔīl ) 
 609–632 CE , Qur'an , 26:193 : نَزَلَ بِهِ ٱلرُّوحُ ٱلۡأَمِينُ nazala bihi r-rūḥu l-ʔamīnu which the trustworthy spirit ˹Gabriel˺ brought down 

 2018 , “ مضحي من وراء حجاب ”, أحمد الفتلاوي (Aḥmad al-Fatlāwi) (music)‎ [1] : وَلَمَّا دَنَا الْمَوْتُ لِلْمُصْطَفَىٰ / وَعِنْدَ الرَّحِيلِ يَنَالُ الْمُنَىٰ / أَتَاهُ الْأَمِينُ بِمِسْكِ الْخِتَامْ / أَلَا فَلْتُبَلِّغْ جَمِيعَ الْأَنَامِ / حُشُودٌ تَرَاءَتْ بِأَرْضِ الْغَدِيرِ walammā danā l-mawtu lilmuṣṭafā / waʕinda r-raḥīli yanālu l-munā / ʔatāhu al-ʔamīnu bimiski l-ḵitām / ʔalā faltuballiḡ jamīʕa l-ʔanāmi / ḥušūdun tarāʔat biʔarḍi l-ḡadīri And when death drew closer to the Chosen one (Prophet Muhammad) / And during the departure he receives the will (of God) / The Trustworthy has come to him with the sweet conclusion / You shall report (it) to all creatures / Crowds witnessing in the land of Ghadeer
```


## [2026-09-04T19:48:16.899Z] TOOL CALL #44: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /home/sfmqrb/git/rishe/data/verification/page-52.json <<'JSON'\n{\n  \"pdf_page\": 52,\n  \"book_page\": 22,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 6,\n      \"root\": \"A`.m.m\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Proto-Semitic root *ʿ-m-m 'to join, be united; to be general/common'\",\n      \"note\": \"Nourai's root box reproduces Klein almost word for word. KLN_1966 p.62 s.v. 'Amhaarez': \\\"Heb. 'am, 'people', derives fr. base '-m-m, 'to join, be united', whence also 'am, 'kinsman', 'im, 'with'. Cp. the rel. Aram.-Syr. 'ammā, 'people', Ugar. 'm, 'clan', Arab. 'amm, 'a great crowd', ammah, 'rabble', 'āmma, 'it comprised, included', 'amm, 'father's brother', 'ammah, 'father's sister'.\\\" Wiktionary independently files Hebrew עַם / עִם under the root ע־מ־ם and compares Arabic عَامّ and عَمّ. The one caveat is that the root is Semitic (Afro-Asiatic), NOT Indo-European; Nourai's language label 'Semitic' is correct and Pokorny/Walde-Pokorny/Watkins are rightly silent. The 'French → Persian' branch for the name Emmanuel (nodes #4-#5) is Nourai's own reconstruction, carries no reference, and compresses the real route (Hebrew → Septuagint/NT Greek → Latin → French); it is plausible but undocumented.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D7%A2%D7%9D\",\n        \"https://en.wiktionary.org/wiki/%D8%B9%D8%A7%D9%85\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:62\", \"status\": \"supports\", \"note\": \"KLN_1966.txt form-feed leaf 44 (= printed pp. 62-63), s.v. Amhaarez: \\\"Heb. 'am, 'people', derives fr. base '-m-m, 'to join, be united', whence also 'am, 'kinsman', 'im, 'with'.\\\" Klein's cross-reference s.v. Immanuel (leaf 415, pp. 772-773) repeats: \\\"Heb. 'im derives fr. stem '-m-m, 'to join, be united', whence also 'am, 'people'. See Amhaarez.\\\" Exactly Nourai's root gloss.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"amm 1; amm 2; ammah\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic عَمّ ʿamm (root ʿ-m-m) is a geminate noun: (1) ʿamm 'a great crowd, the generality of people', beside the denominal verb عَمَّ ʿamma 'it comprised, included, was general' and the active participle عَامّ ʿāmm 'general, common, public'; (2) ʿamm 'father's brother, paternal uncle', with the feminine عَمَّة ʿammah 'father's sister'. The kinship sense is the older Semitic one ('clan-member, kinsman' > 'paternal kinsman'), directly matched by Ugaritic ʿm 'clan', Hebrew ʿam 'people, kinsman' and Aramaic-Syriac ʿammā 'people'; the abstract 'be general, comprise' sense is an Arabic-internal development from the same 'be joined together' notion. Nourai's split of amm 1 / amm 2 is Klein's own presentation.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B9%D9%85\",\n            \"https://en.wiktionary.org/wiki/%D8%B9%D8%A7%D9%85\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:62\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 44 (pp. 62-63) s.v. Amhaarez lists precisely \\\"Arab. 'amm, 'a great crowd', ammah, 'rabble', 'āmma, 'it comprised, included', 'amm, 'father's brother', 'ammah, 'father's sister'\\\" under base ʿ-m-m. Klein's 'ammah 'rabble'' and 'ʿammah 'father's sister'' are two separate items; Nourai kept only the second.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 44 = pp. 62-63, s.v. Amhaarez\", \"stance\": \"supports\", \"note\": \"\\\"Arab. 'amm, 'a great crowd' … 'amm, 'father's brother', 'ammah, 'father's sister'\\\" — all three of Nourai's Arabic items.\"},\n            {\"src\": \"FVQ\", \"where\": \"FVQ.txt / FVQ_pages.txt, greps for amin, iman, umma\", \"stance\": \"silent\", \"note\": \"Jeffery's Foreign Vocabulary of the Qurʾān has no entry for ʿamm / ʿāmm — expected, since ʿ-m-m is native Arabic, not a loan.\"},\n            {\"src\": \"AFM\", \"where\": \"AFM.txt, grep 'عمّ'\", \"stance\": \"silent\", \"note\": \"Addi Shir lists only unrelated forms (عمور, عمّيدة …); ʿamm is not treated as an Arabicised Persian word, correctly.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt nos. 61-69 (the ar. am-/ʿam- block)\", \"stance\": \"silent\", \"note\": \"Lokotsch has Ar. ammā (no. 64), amān (no. 66), ʿamāra (no. 67), amīr (no. 69) but no entry for ʿamm 'uncle/crowd' — no European loan to record.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"amŭ «عمو»; âm «عام»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both are Arabic loans into New Persian of the Islamic period. (a) عمو amū/amō 'paternal uncle' = Arabic عَمّ ʿamm plus the Persian hypocoristic/diminutive suffix ـو -ū/-ō (Classical Persian /ʔa.ˈmoː/, modern amu), the same formation as Tajik амак amak with a different diminutive suffix and parallel to Egyptian Arabic ʿammu; it displaced no native word entirely — Persian keeps خالو xālū 'maternal uncle' on exactly the same pattern (Arabic خال xāl + -ū), which Moʿin cites as the comparandum. (b) عام ām 'public, general' is Arabic عَامّ ʿāmm, the active participle of عَمَّ ʿamma; Persian regularly degeminates the final -mm in pronunciation. Nourai's script_extra عمّه (ʿammah 'paternal aunt'), عموم (ʿumūm 'generality'), عوام (ʿawāmm 'the common people'), تعميم (taʿmīm 'generalisation') are all further ʿ-m-m loans, each confirmed by Moʿin as [ع.].\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B9%D9%85%D9%88\",\n            \"https://en.wiktionary.org/wiki/%D8%B9%D8%A7%D9%85\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVA:285\", \"status\": \"not_checked\", \"note\": \"S. M. Nahvi, Farhang-e Vāzhehā-ye ʿArabi dar Fārsi (Dakhil), 1368/1989 — refs_online.json records no digital copy on any permitted platform (catalogue record OL2012991M only). Not accessible.\"},\n            {\"ref\": \"SAP:442\", \"status\": \"not_checked\", \"note\": \"Sayyāh, Farhang-e Sayyāh (Persian translation of al-Munjid), 3 vols 1368/1989 — purchase-only (fidibo.com/book/142427 etc.); no readable copy.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt s.vv. عمو، عمه، عام، عوام\", \"stance\": \"supports\", \"note\": \"\\\"عمو: [ع. قس. خالو] برادر پدر؛ عم پدر\\\" (Arabic, cf. xālū, 'father's brother'); \\\"عمه: [ع. عمه] (ا.) خواهر پدر\\\"; \\\"عام: [ع.] (افا.) همه را فرا گیرنده؛ عموم را فرا رسنده … همگان، همه مردم؛ مق. خاص\\\"; \\\"عوام: ج. عامه؛ مق. خواص\\\". Moʿin marks every one of them [ع.] = Arabic.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v1.txt / BQT_v2.txt, grep عمو\", \"stance\": \"silent\", \"note\": \"Borhān-e Qāṭeʿ has no headword عمو — the 122/112 hits are the adverb عموماً inside other articles. Expected: Borhān is a dictionary of Persian (non-Arabic) vocabulary.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt, greps for amu/amānat/'amm\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss covers inherited Iranian etyma only; the only 'Amme' hits are the German gloss 'Amme, Erzieher' at nos. cited from the Vidēvdād. No entry for the Arabic loan.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt, grep amān/amm\", \"stance\": \"silent\", \"note\": \"Hübschmann's Persische Studien likewise ignores Arabic loanwords of this class.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_latin_index_pages.txt, grep AMM/AMEN\", \"stance\": \"silent\", \"note\": \"Aryanpur's dictionary of Indo-European roots of Persian has no entry — correct, the word is Semitic.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Hebrew\",\n          \"words\": \"am; im; Immânŭ-ĕl\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Hebrew עַם ʿam 'people, nation; kinsman' is a qeṭel-pattern geminate noun from the root ע־מ־ם ʿ-m-m 'to join, be united' (pl. ʿammīm, constr. ʿam-); the preposition עִם ʿim 'with, together' is the same base in a prepositional use, cognate with Ugaritic ʿm and, by metathesis, with Arabic مَعَ maʿa and Ugaritic mʿ. The theophoric name עִמָּנוּאֵל ʿImmānū-ʾĒl (Isaiah 7:14, 8:8) is transparently עִמָּנוּ ʿimmānū 'with us' (ʿim + the 1 pl. pronominal suffix -nū, with gemination of the m) + אֵל ʾĒl 'God' — hence 'God is with us'. Nourai's cross-reference ☞Layh is to his own root box for Semitic ʾ-l/Ilāh 'God', the second element of the name.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D7%A2%D7%9D\",\n            \"https://en.wiktionary.org/wiki/Immanuel\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:62\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 44 (pp. 62-63) s.v. Amhaarez: \\\"Heb. 'am had-retz, 'the people of the land'. Heb. 'am, 'people', derives fr. base '-m-m, 'to join, be united', whence also 'am, 'kinsman', 'im, 'with' … Cp. the first element in Emmanuel and the second element in Jeroboam.\\\" Klein's own cross-entry (leaf 415, pp. 772-773) s.v. Immanuel: \\\"This name is compounded of 'immānu, 'with us' (which is formed fr. 'im, 'with', with the pronominal suff. of the 1st person pl.), and El, 'God'.\\\" All three of Nourai's Hebrew items, in Klein's order.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaves 44 and 415 (pp. 62-63, 772-773)\", \"stance\": \"supports\", \"note\": \"See ref_check: ʿam, ʿim and ʿImmānūʾēl are all derived from stem ʿ-m-m.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt no. 68 s.v. 'Hebr. amen'\", \"stance\": \"silent\", \"note\": \"Lokotsch treats Hebrew amen but has no entry for ʿam / ʿim — no European loan to record for this node.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 63678\", \"stance\": \"supports\", \"note\": \"Webster's glosses the name as \\\"Immanuel (God with us)\\\", matching the Hebrew analysis.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Empty pass-through box standing for French Emmanuel (masc. PN, well attested from the Middle Ages, e.g. Emmanuel de Savoie). Its real route is Hebrew ʿImmānūʾēl → Septuagint/NT Greek Ἐμμανουήλ (Matthew 1:23, with prothetic e- and doubled -mm- rendering the Hebrew geminate) → Ecclesiastical Latin Emmanuel → Old French/French Emmanuel; Nourai's arrow Hebrew → French compresses the Greek and Latin stages that his own parallel chart for A.m.n spells out. The box carries no reference of its own.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Immanuel\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 280 (pp. 514-515) s.v. Emmanuel\", \"stance\": \"partial\", \"note\": \"\\\"Emmanuel, masc. PN. — Gk. Ἐμμανουήλ, fr. Heb. 'Immanuel, lit. 'God is with us'. See Immanuel.\\\" Klein inserts Greek between Hebrew and the modern European forms, which Nourai's Hebrew → French arrow omits.\"},\n            {\"src\": \"PHN\", \"where\": \"PHN.txt (Pihan, French words from Arabic/Persian/Turkish)\", \"stance\": \"silent\", \"note\": \"Pihan covers French orientalisms of Arabic/Persian/Turkish origin, not Biblical Hebrew personal names — no entry.\"},\n            {\"src\": \"DEV\", \"where\": \"DEV.txt (Devic)\", \"stance\": \"silent\", \"note\": \"Likewise no entry for the personal name Emmanuel.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"Âmânoel «آمانوئل»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Persian امانوئل Emānuʾel / Amānoʾel is the Biblical name Emmanuel taken over as a modern given name and as the rendering of Isaiah 7:14 in Persian Bible translations. A French (or wider European) route is likely for the modern personal-name use — the -وئل -uʾel spelling reflects a European Emmanuel/Emanuel rather than the Arabic-Christian form عمانوئيل ʿImmānūʾīl, which preserves the ʿayin — but Nourai gives no reference and no dated attestation, and Moʿin's Farhang has no entry for the name (grep of MON_part1/part2 for امانوئل: 0 hits), so the French mediation is an assumption rather than a documented fact. Note also that the headword is printed «آمانوئل» with initial آ- while Nourai's own extra field gives the ordinary spelling امانوئل; the آ- form is not standard Persian and may be a scan artefact.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Immanuel\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt, MON_part2.txt, grep امانوئل\", \"stance\": \"silent\", \"note\": \"0 hits; Moʿin's Farhang-e Fārsi does not carry the name.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v1.txt, BQT_v2.txt, grep امانوئل\", \"stance\": \"silent\", \"note\": \"0 hits.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_latin_index_pages.txt\", \"stance\": \"silent\", \"note\": \"No entry — the name is not Indo-European in origin.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"Emmanuel, Immanuel\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English has both forms: Immanuel is the direct transliteration of Hebrew עִמָּנוּאֵל ʿImmānūʾēl used in English Bibles at Isaiah 7:14, while Emmanuel is the form that came through Koine Greek Ἐμμανουήλ (Matthew 1:23) and Ecclesiastical Latin Emmanuel, where the initial ʿayin was lost and the vowel written e-. Both entered English as Biblical names in the Wycliffite and Tyndale/AV translations and became given names from the Reformation onward.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Immanuel\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:515\", \"status\": \"supports\", \"note\": \"Page number verified: KLN_1966.txt leaf 280 lies between leaf 279 (running numbers 512, 513) and leaf 281 (516, 517), i.e. printed pp. 514-515. It reads \\\"Emmanuel, masc. PN. — Gk. Ἐμμανουήλ, fr. Heb. 'Immanuel, lit. 'God is with us'. See Immanuel.\\\" — Nourai's KLN:515 is correct.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 280 (pp. 514-515) and leaf 415 (pp. 772-773)\", \"stance\": \"supports\", \"note\": \"Both the Emmanuel and the Immanuel entries; the latter refers the root back to Amhaarez, closing Nourai's circle.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 63678\", \"stance\": \"supports\", \"note\": \"\\\"Immanuel (God with us)\\\".\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt, greps for Emmanuel/Immanuel\", \"stance\": \"silent\", \"note\": \"Skeat's Concise has no personal-name entries of this kind.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 7,\n      \"root\": \"A.m.n\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Proto-Semitic root *ʾ-m-n 'to be firm, trustworthy; to confirm, support'\",\n      \"note\": \"Root box, language label and gloss are all right and match both of the standard short statements: Klein (KLN p.61 s.v. amen) \\\"from stem a-m-n, 'to be trustworthy, confirm, support'\\\", and Etymonline s.v. amen \\\"from Semitic root a-m-n 'to be trustworthy, confirm, support'\\\". Note the root is Semitic, so Pokorny/Walde-Pokorny/Watkins have nothing (correctly). The one refinement modern scholarship adds concerns node #2: Persian آمین is not an internal Arabic derivative of ʾ-m-n but a liturgical loan that reached Arabic from Syriac/Aramaic (ultimately Hebrew); Moʿin marks it [ع. عبر.] 'Arabic, Hebrew', which is the same correction. This does not affect the root itself. Nourai's transliteration 'âmen' for «آمین» is his rendering of the Semitic prototype; the Persian word is āmīn.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/amen\",\n        \"https://www.etymonline.com/word/amen\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:61\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 44 — the amen entry stands immediately before the running-head block \\\"amenable | amnic | 62 | 63\\\", i.e. on printed p.61: \\\"amen, interj., n., adv. and tr. v. — OE., fr. Eccles. L. amen, fr. Eccles. Gk. ἀμήν, fr. Heb. amen, 'verily, truly, certainly', from stem a-m-n, 'to be trustworthy, confirm, support', whence also aman, 'he supported, nourished', heemīn, 'he believed', emunāh, 'firmness, fidelity' … Cp. the related Syr. ammīn, 'strong, enduring', Aram. hemanuthā, Syr. haymanuthā, 'faithfulness, truth', Arab. āmina, 'he was safe' [continues p.62] amuna, 'he was faithful', ā'mana, 'he believed', amīn, 'faithful'.\\\" Nourai's page number and gloss are exact.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"a.m.n; amin; îmân\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic root ء م ن ʾ-m-n: أَمِنَ ʾamina 'he was safe', أَمُنَ ʾamuna 'he was faithful, trustworthy', whence the adjective أَمِين ʾamīn 'trustworthy, reliable, faithful' (Qurʾān 95:3 al-balad al-ʾamīn 'the secure city'; al-rūḥ al-ʾamīn 'the trustworthy spirit' = Gabriel, 26:193) and the noun أَمَانَة ʾamāna 'trust, deposit'. The IVth-form verb آمَنَ ʾāmana 'he believed, gave credence (bi- to)' yields the verbal noun إِيمَان ʾīmān 'faith, belief' (*ʾiʾmān > ʾīmān by regular contraction of hamza + i). Nourai's 'a.m.n : to trust' is the root, correctly with initial hamza (not ʿayin — contrast the ʿ-m-m root of the previous chart).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A3%D9%85%D9%8A%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D9%85%D8%A7%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:61\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 44, s.v. amen (p.61 continuing onto p.62): \\\"Arab. āmina, 'he was safe', amuna, 'he was faithful', ā'mana, 'he believed', amīn, 'faithful'. Cp. ameen.\\\" Klein's separate entry ameen (same leaf, p.61) adds: \\\"Hind. amīn, fr. Arab. amīn, lit. 'trustworthy', fr. amina, 'he was steady, firm, trustworthy' (whence ā'mana, 'he believed'); rel. to Heb. amen, 'verily, truly'.\\\"\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 44, s.vv. ameen and amen (p.61)\", \"stance\": \"supports\", \"note\": \"See ref_check — Klein gives amina, amuna, āʾmana, amīn under the same stem as Hebrew amen.\"},\n            {\"src\": \"FVQ\", \"where\": \"FVQ.txt / FVQ_pages.txt, greps amin, iman, amana\", \"stance\": \"silent\", \"note\": \"Jeffery has no entry: ʾ-m-n words in the Qurʾān are treated as native Arabic, not foreign vocabulary (only the interjection āmīn, which is not Qurʾānic, is a loan).\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt no. 66 s.v. 'Ar. amān'\", \"stance\": \"supports\", \"note\": \"\\\"Ar. amān: 'Gnade, Gunst' … Die ar. Form imāna, tk. emanet 'Sicherheit' wurde mit amān kontaminiert, wobei sich folgende Wörter ergaben: rum. amanet, emanet 'Pfand, Sicherheit'; bulg. serb. amanet 'Pfand', russ. amanat 'Geisel'.\\\" — the same root, with its Balkan/Turkish loan history.\"},\n            {\"src\": \"AFM\", \"where\": \"AFM.txt, grep امين/أمين\", \"stance\": \"silent\", \"note\": \"Addi Shir does not list ʾamīn among Arabicised Persian words — correct, the root is Arabic.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"amn «امن»; amânat «امانت»; îmân «ایمان»; âmen «آمین»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Three of the four are straightforward Arabic loans into New Persian, all marked [ع.] by Moʿin: امن amn 'safety, secure' = Arabic verbal noun أَمْن; امانت amānat = Arabic أَمَانَة ʾamāna 'trust, deposit' (Persian keeps the Arabic tāʾ marbūṭa as -t in the free form, as regularly in Persian Arabisms: امانة > امانت); ایمان īmān = Arabic إِيمَان, the IVth-form verbal noun of آمَنَ, borrowed with the religious sense 'faith' and passed on from Persian to Urdu/Punjabi/Pashto (Wiktionary: 'Borrowed from Classical Persian اِیمَان (īmān), borrowed from Arabic إِيمَان (ʔīmān), from آمَنَ (ʔāmana)'). The fourth, آمین āmīn 'amen', is where the chart is only partly right: it is Arabic آمِينَ ʾāmīna, but that Arabic word is itself a liturgical borrowing from Classical Syriac ܐܰܡܺܝܢ / Aramaic אַמִין (ultimately Biblical Hebrew אָמֵן), not an inherited Arabic derivative of ʾ-m-n — Moʿin marks it exactly so, [ع. عبر.] 'Arabic, Hebrew'. So this word reaches Persian by the Hebrew branch of Nourai's own chart (node #3) via Syriac and Arabic, not by the Arabic branch, and the node as drawn conflates the two. Nourai's transliteration 'âmen' also misrepresents the Persian pronunciation āmīn. The script_extra items امنیّت، ایمن، مأمن، تأمین، مؤمن، امان، مأمون، آمینه are all further regular ʾ-m-n loans (Moʿin: تأمین [ع.] 'ایمن کردن'; مأمن [ع.] 'جای امن'; مؤمن [ع.] 'دارندهٔ ایمان').\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D9%85%D8%A7%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%A2%D9%85%DB%8C%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%85%D8%A7%D9%86%D8%AA\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVA:34,35\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e Vāzhehā-ye ʿArabi dar Fārsi (Dakhil), 1368/1989: refs_online.json records no digital copy on any permitted platform (catalogue record OL2012991M only, 582 pp). Not accessible; re-searched 2026-09 per the notes field.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt s.vv. امن، امانت، ایمان، آمین; MON_part2.txt s.vv. مأمن، مؤمن\", \"stance\": \"partial\", \"note\": \"\\\"امن: [ع.] (مص‌ل.) بی‌بیم بودن، ایمن شدن\\\"; \\\"امانت: [ع. امانة] (مص‌ل.) امین بودن … مال یا چیزی که به زنهار، ودیعه\\\"; \\\"ایمان: [ع.] (مص م.) گرویدن … باور داشتن\\\" — all straight Arabic, supporting Nourai. But \\\"آمین: [ع. عبر.] کلمه‌ای است که پس از دعا گویند به معنی برآورد! بپذیر! اجابت کن!\\\" — Moʿin's double tag ع. عبر. (Arabic, Hebrew) shows this one is a Hebrew word transmitted through Arabic, not an Arabic ʾ-m-n derivative.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v1.txt, BQT_v2.txt, greps آمین، امانت\", \"stance\": \"silent\", \"note\": \"The few hits are OCR noise (آمین read for آیینه/امین inside unrelated articles, e.g. s.v. استوار 'محکم و مضبوط … آمین و معتمد'); Borhān-e Qāṭeʿ carries no headword for these Arabic loans.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt, greps amān/amānat/amin\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss treats only inherited Iranian etyma; no entry.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt, grep amān\", \"stance\": \"silent\", \"note\": \"Hübschmann likewise silent on Arabic loans of this class.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt nos. 66 and 68\", \"stance\": \"supports\", \"note\": \"No. 66 documents Ar. amān / imāna > Turkish emanet 'Sicherheit' > Romanian amanet, Russian amanat — i.e. the amānat family; no. 68 documents Hebr. amen > Gk ἀμήν > Lat. amen 'in alle europäischen Sprachen übergegangen', which is the route behind Persian آمین as well.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_latin_index_pages.txt, grep AMEN\", \"stance\": \"silent\", \"note\": \"Only unrelated headwords (AMEN listed as the Russian/Czech/Bulgarian word beside āsmān entries); Aryanpur has no Indo-European etymology for these, as expected.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Hebrew\",\n          \"words\": \"a.m.n; âmen\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Hebrew root א־מ־ן ʾ-m-n 'to be firm, faithful, trustworthy': qal אָמַן ʾāman 'he supported, nourished', hiphʿil הֶאֱמִין heʾĕmīn 'he believed', nouns אֱמוּנָה ʾĕmūnāh 'firmness, fidelity' and אֱמֶת ʾĕmeṯ (< *ʾementh) 'truth, stability'. The adverbial אָמֵן ʾāmēn 'verily, truly, certainly' is a frozen affirmative used to ratify an oath or curse (Deuteronomy 27:15-26, 1 Kings 1:36) and to close a doxology (Psalms 41:14). Cognates: Syriac ammīn 'strong, enduring', Aramaic/Syriac (h)aymānūṯā 'faithfulness'.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/amen\",\n            \"https://www.etymonline.com/word/amen\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:61\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 44 (p.61) s.v. amen: \\\"fr. Heb. amen, 'verily, truly, certainly', from stem a-m-n, 'to be trustworthy, confirm, support', whence also aman, 'he supported, nourished', heemīn, 'he believed', emunāh, 'firmness, fidelity', umnām, omnām, 'verily, truly', emith (for *ementh), 'stability, truth'.\\\" Exactly Nourai's two Hebrew items.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 44, p.61 s.v. amen\", \"stance\": \"supports\", \"note\": \"See ref_check.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt no. 68\", \"stance\": \"supports\", \"note\": \"\\\"Hebr. amen: 'Wahrlich, gewiß, sicher'. Hieraus gr. ἀμήν, lat. amen; in alle europäischen Sprachen übergegangen; mit diesem Wort endigen die jüdischen und christlichen Gebete.\\\"\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 6537\", \"stance\": \"supports\", \"note\": \"\\\"a'men (also ä'men'), n. [L. amen; Gr. amén; Heb. āmén, truly, certainly]\\\".\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"amĕn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Koine/Ecclesiastical Greek ἀμήν amḗn is an unadapted transliteration of Hebrew אָמֵן, taken over untranslated by the Septuagint translators (3rd-2nd c. BCE) where the Hebrew ratifying formula stood, and then used throughout the New Testament (notably the Gospel formula ἀμὴν λέγω ὑμῖν). Greek η renders the Hebrew ṣērê /ē/; the word is indeclinable and keeps no Greek ending, which is itself the mark of a liturgical borrowing rather than a naturalised loan.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/amen\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:61\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 44 (p.61) s.v. amen: \\\"OE., fr. Eccles. L. amen, fr. Eccles. Gk. ἀμήν, fr. Heb. amen\\\" — the Greek link is explicitly Ecclesiastical Greek from Hebrew, as drawn.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 44, p.61\", \"stance\": \"supports\", \"note\": \"\\\"fr. Eccles. Gk. ἀμήν, fr. Heb. amen\\\".\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt no. 68\", \"stance\": \"supports\", \"note\": \"\\\"Hieraus gr. ἀμήν, lat. amen\\\".\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 6537\", \"stance\": \"supports\", \"note\": \"\\\"[L. amen; Gr. amén; Heb. āmén]\\\" — the same Hebrew > Greek > Latin order.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"âmĕn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ecclesiastical/Late Latin āmēn, taken from the Greek of the Septuagint and New Testament in the Old Latin and Vulgate versions (Jerome kept the Hebrew word untranslated); like the Greek it is indeclinable and stays outside the Latin nominal system. Latin then carried it into every Western liturgy and thence into all the Romance and Germanic languages.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/amen\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:61\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 44 (p.61): \\\"OE., fr. Eccles. L. amen, fr. Eccles. Gk. ἀμήν\\\" — the Greek → Latin arrow as drawn.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 44, p.61\", \"stance\": \"supports\", \"note\": \"\\\"fr. Eccles. L. amen\\\".\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt no. 68\", \"stance\": \"supports\", \"note\": \"\\\"Hieraus gr. ἀμήν, lat. amen; in alle europäischen Sprachen übergegangen.\\\"\"},\n            {\"src\": \"LEW\", \"where\": \"LEW_1910.txt (Walde, Lat. etym. Wb.)\", \"stance\": \"silent\", \"note\": \"Walde's Latin etymological dictionary treats inherited Latin vocabulary and has no entry for the ecclesiastical loan amen.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"Amen : verily\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English āmen, borrowed with Christianity from Ecclesiastical Latin āmēn; in Old English it was used only at the close of the Gospels, the affirmative elsewhere being rendered sōþlīċe 'truly' or swā hit is 'so it is'. Middle English amen > modern English amen, still indeclinable, with the two competing pronunciations /ɑːˈmɛn/ (Latinate, older) and /eɪˈmɛn/ (the Great-Vowel-Shift reading of the spelling, favoured in nonconformist and gospel usage). Nourai's gloss 'verily' is the Hebrew adverbial sense preserved throughout.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/amen\",\n            \"https://www.etymonline.com/word/amen\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:61\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 44 (p.61) s.v. amen: \\\"amen, interj., n., adv. and tr. v. — OE., fr. Eccles. L. amen, fr. Eccles. Gk. ἀμήν, fr. Heb. amen, 'verily, truly, certainly'.\\\" Nourai's whole chain and his English gloss come straight from this line.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 44, p.61 s.v. amen\", \"stance\": \"supports\", \"note\": \"See ref_check.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt lines 6537-6545\", \"stance\": \"supports\", \"note\": \"\\\"a'men (also ä'men'), n. [L. amen; Gr. amén; Heb. āmén, truly, certainly] … 4'men', adv. truly; verily.\\\" — including Nourai's exact gloss 'verily'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt, greps for 'amen'\", \"stance\": \"silent\", \"note\": \"No usable entry: every hit is OCR debris from flamen / filament / backgammon; Skeat's Concise appears not to carry the word (or the scan lost it).\"},\n            {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt, FSD_vol2.txt, greps for a-men / Heb. amen\", \"stance\": \"silent\", \"note\": \"The Funk & Wagnalls scan is too badly OCR'd around 'a-men' (hits are additament, enfranchisement, excruciator) to locate the entry.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt no. 68\", \"stance\": \"supports\", \"note\": \"\\\"in alle europäischen Sprachen übergegangen\\\" — English included.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSON\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-52.json > /dev/null && echo \"JSON OK\"; python3 /home/sfmqrb/git/rishe/tools/verify_check.py 52"
}
```


### [2026-09-04T19:48:19.716Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'confirmed': 9, 'plausible': 3}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 8, 'not_checked': 5}
books consulted: {'supports': 20, 'silent': 23, 'partial': 2} | by book: {'KLN': 9, 'LKT': 8, 'WEB': 5, 'MON': 3, 'BQT': 3, 'ARY': 3, 'FVQ': 2, 'AFM': 2, 'HRN': 2, 'HUB': 2, 'SKT': 2, 'PHN': 1, 'DEV': 1, 'LEW': 1, 'FSD': 1}
```


## [2026-09-04T19:48:37.048Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-52.json` written; `verify_check.py 52` reports 12/12 nodes, no PROBLEM lines.

**Page 52 (book p. 22)** — 6 entries are redirects (skipped); 2 real charts verified.

- Root verdicts: 2 confirmed (Semitic *ʿ-m-m "to join, unite"; Semitic *ʾ-m-n "to trust").
- Node verdicts: 9 confirmed, 3 plausible, 0 disputed, 0 unverified, 0 transcription_suspect.
- Ref checks: 8 `supports` (all KLN), 5 `not_checked` (FVA, SAP have no digital copy; two nodes carry no refs at all).
- Books consulted: 15 distinct (KLN, LKT, WEB, MON, BQT, ARY, FVQ, AFM, HRN, HUB, SKT, PHN, DEV, LEW, FSD); 11 web pages archived via `fetch_source.py`.

Key findings:
- Nourai's KLN page numbers are exact. KLN:62 = Klein s.v. *Amhaarez* (leaf 44) which lists literally every Arabic and Hebrew item of chart 6; KLN:61 = s.v. *amen* (same leaf, before the 62/63 running head); KLN:515 = s.v. *Emmanuel* (leaf 280, verified as pp. 514–515 by the neighbouring page numbers).
- `plausible` items (no disputed ones):
  - **A.m.n #2, Persian آمین** — the only substantive correction: Nourai hangs it under the *Arabic* branch, but Arabic آمِينَ is itself a liturgical loan from Syriac/Aramaic ← Hebrew אָמֵן, so the word reaches Persian by the *Hebrew* branch of his own chart. Moʿin independently tags it «[ع. عبر.]» (Arabic, Hebrew). His transliteration "âmen" also misstates the Persian pronunciation āmīn. The other three words on that node (امن، امانت، ایمان) are straight Arabic loans and fully confirmed.
  - **Aʿ.m.m #4, French (empty box)** — unreferenced; Hebrew → French skips the Greek and Latin stages Klein supplies.
  - **Aʿ.m.m #5, Persian آمانوئل** — unreferenced; French mediation is likely but undocumented, and the printed «آمانوئل» with initial آ- is non-standard (his own extra field gives امانوئل), possibly a scan artefact — noted in the derivation rather than flagged.
- Pokorny/Walde-Pokorny/Watkins/Aryanpur are correctly silent: both roots are Semitic, not IE.
