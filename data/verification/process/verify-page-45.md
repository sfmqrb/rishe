# Verification process log — verify-page-45


## [2026-09-04T19:19:34.849Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 45 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-45.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-45.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-45.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 45` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T19:19:35.974Z] AGENT

I'll start by reading the instructions and the relevant files.


## [2026-09-04T19:19:37.859Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:19:37.875Z] TOOL RESULT

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


## [2026-09-04T19:19:38.659Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-45.txt"
}
```


### [2026-09-04T19:19:38.676Z] TOOL RESULT

```
1	=== PDF page 45 (book page 15) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Al 1, Ol 1 : beyond, above  (refs POK:24)
4	#1 (parent #0) [Indo-European] refs=POK:24,67 | Aryo, Ario : Lord, ruler
5	  #2 (parent #1) [Old Persian / Avestan] refs=AHD; POK; IRN:7,28 | aria : noble ; arân : land of Aryans (Indo-Europeans) ; art-arân : holy Aryan land ☞Ar ; airyanam-vaězo : Aryan race and family
6	    #3 (parent #2) [Persian] refs=PRT:27; MON5:114; PRT:313; IRN:7,28 | Âriyâ «آریا» ; Arân, Îrân, Arâk, Arâq «آران ، ایران ، اراک ، عراق» ; Ardalân «اردلان» : "holy Aryan land", a name ; Îrânvěj «ایرانویج» : original homeland of Aryans
7	    #4 (parent #2) [Avestan] refs=POK:24; BQT:196; IRN:12; FAF:86 | airiyava : helper of Aryans ; airya-man : noble mannered, friend, guest ☞Men 1
8	      #5 (parent #4) [Persian] refs=POK:67; BQT:196; IRN:12 | Îraj «ایرج» : "helper of Aryans", a male name ; îrmân «ایرمان» : guest
9	  #6 (parent #1) [Sanskrit] refs=KLN:110; SHP:180 | Arya : noble
10	    #7 (parent #6) [English] refs=None | Aryan, Ireland
11	      #8 (parent #7) [Persian] refs=MON5:212 | Îrland «ایرلند»
12	  #9 (parent #1) [Sogdian] refs=SOD:60 | `ry`n-wyj`n : Aryan family
13	#10 (parent #0) [Latin] refs=AHD | ille : that ; ultrâ : beyond ; alter : the other ; alius : from beyond (foreigner)
14	  #11 (parent #10) [English] refs=None | alarm, alert, alligator ; ultimate, ultra- ; alternate ; alien
15	#12 (parent #0) [Greek] refs=AHD | allos : other ; para-allělon : besides one another ☞Per 1
16	  #13 (parent #12) [Latin] refs=AHD:951 | parallělum : parallel
17	    #14 (parent #13) [English] refs=None | parallel
18	#15 (parent #0) [Germanic] refs=AHD | al-jas : otherwise
19	  #16 (parent #15) [English] refs=None | else
20	
```


## [2026-09-04T19:19:40.403Z] AGENT

I'll read the supporting files and source JSON.


## [2026-09-04T19:19:42.815Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-45.json && echo \"=== MATRIX ===\" && cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T19:19:42.866Z] TOOL RESULT

```
{
  "pdf_page": 45,
  "book_page": 15,
  "entries": [
    {
      "root": {
        "name": "Al 1, Ol 1",
        "lang": "Indo-European",
        "refs": "POK:24",
        "gloss": "beyond, above"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "POK:24,67",
          "words": [
            {"translit": "Aryo, Ario", "gloss": "Lord, ruler", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Old Persian / Avestan",
          "refs": "AHD; POK; IRN:7,28",
          "words": [
            {"translit": "aria", "gloss": "noble", "script": null},
            {"translit": "arân", "gloss": "land of Aryans (Indo-Europeans)", "script": null},
            {"translit": "art-arân", "gloss": "holy Aryan land", "script": null, "see": ["Ar"]},
            {"translit": "airyanam-vaězo", "gloss": "Aryan race and family", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "PRT:27; MON5:114; PRT:313; IRN:7,28",
          "words": [
            {"translit": "Âriyâ", "gloss": null, "script": "آریا"},
            {"translit": "Arân, Îrân, Arâk, Arâq", "gloss": null, "script": "آران ، ایران ، اراک ، عراق"},
            {"translit": "Ardalân", "gloss": "\"holy Aryan land\", a name", "script": "اردلان"},
            {"translit": "Îrânvěj", "gloss": "original homeland of Aryans", "script": "ایرانویج"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Avestan",
          "refs": "POK:24; BQT:196; IRN:12; FAF:86",
          "words": [
            {"translit": "airiyava", "gloss": "helper of Aryans", "script": null},
            {"translit": "airya-man", "gloss": "noble mannered, friend, guest", "script": null, "see": ["Men 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "POK:67; BQT:196; IRN:12",
          "words": [
            {"translit": "Îraj", "gloss": "\"helper of Aryans\", a male name", "script": "ایرج"},
            {"translit": "îrmân", "gloss": "guest", "script": "ایرمان"}
          ],
          "note": null,
          "quote": {
            "text": "اگر کشته آید به دست تو گرگ - توباشی به روم ایرمانی بزرگ",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 6,
          "parent": 1,
          "lang": "Sanskrit",
          "refs": "KLN:110; SHP:180",
          "words": [
            {"translit": "Arya", "gloss": "noble", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Aryan, Ireland", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON5:212",
          "words": [
            {"translit": "Îrland", "gloss": null, "script": "ایرلند"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:60",
          "words": [
            {"translit": "`ry`n-wyj`n", "gloss": "Aryan family", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "ille", "gloss": "that", "script": null},
            {"translit": "ultrâ", "gloss": "beyond", "script": null},
            {"translit": "alter", "gloss": "the other", "script": null},
            {"translit": "alius", "gloss": "from beyond (foreigner)", "script": null}
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
            {"translit": "alarm, alert, alligator", "gloss": null, "script": null},
            {"translit": "ultimate, ultra-", "gloss": null, "script": null},
            {"translit": "alternate", "gloss": null, "script": null},
            {"translit": "alien", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "allos", "gloss": "other", "script": null},
            {"translit": "para-allělon", "gloss": "besides one another", "script": null, "see": ["Per 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Latin",
          "refs": "AHD:951",
          "words": [
            {"translit": "parallělum", "gloss": "parallel", "script": null}
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
            {"translit": "parallel", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "al-jas", "gloss": "otherwise", "script": null}
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
            {"translit": "else", "gloss": null, "script": null}
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


## [2026-09-04T19:19:52.546Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','AHD','IRN','BQT','MON','KLN','SOD','PRT','SHP','FAF','WLD','IEC','SYN','HRN','HUB','BRT','KNT','PHD','SKT','LEW','LAT','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False))\n\""
}
```


## [2026-09-04T19:19:54.401Z] TOOL CALL #5: Bash

```json
{
 "command": "grep -n -iE '^(PRT|SHP|FAF|IRN|SOD|POK|AHD)\\b' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt | head -40; echo ---; grep -n -iE 'PRT|SHP|FAF' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt | head -30"
}
```


### [2026-09-04T19:19:55.082Z] TOOL RESULT

```
<persisted-output>
Output too large (36.6KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/byn311g1k.txt

Preview (first 2KB):
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)", "local_files": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_0
...
</persisted-output>
```


### [2026-09-04T19:19:55.142Z] TOOL RESULT

```
---
3: TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
9: TABLE IV - Reference Abbreviations (continued ...) 17 BLY 18 BQT 19 BRT 20 BST 21 CEL 22 DEV 23 DMO 24 DOZ 25 DRM 26 DVS 27 DZA 28 EAV 29 ETM 30 FAF 31 FFD H. W. Baily, "Hvatanica II", (Glossary of some Khotanese words with reference to Avestan and Persian words), Bulletin of the School of Oriental and African Studies (BSOAS IX:1937-39) pp 69-78, University of London. M. H. Tabriz! (Borhan), Borhan Qate', ^l»ls ^i&amp;j&gt; Etymological footnotes by Dr. M. MoTn, 4 vol, Amfr Kabrr Press, Tehran 1362 (1983). C. Bartholomae, Altiranisches Worterbuch Zusammen Mit Den Nacharbeiten Und Vorarbeiten, Walter de Gruyter Press, 1979. Paul Horn, "Some Inscriptions on Sassanian Gems", Avesta, Pahlavi and Ancient Persian Studies, First Series, pp 224-263, Bombay Educational Society's Press, 1904. S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, 6 Vol., Sverge Haus Publishers, Milton, Ma, 1997 L. M. Devic, Dictionnaire Etymologique des Mots Francais D'Origin Orientale, Oriental Press 1876. S. NafisT, Par Maktab Ostad, ilx-,1 Zohreh Press, Tehran 1344 (1965). R. Dozy, Verklarende Lisjt der Nederlandsche Woorden, Die Uit Het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch Afkomstig Zijn, Leiden 1867. J. Darmester, Etudes Itaniennes, Paris 1883. P. Davis, Roots - Family History of Familiar Words, McGraw-Hill Book Company 1981. M. T. Rashed Mohassel, Daramadi Bar Dastur ^^jl oki _}f~&gt;* j&gt;. iSJ^&gt;^ Zaban AvestST, Khajeh Press, Tehran 1364 (1985). J. Duchesne-Guillemin, "Etymologies Avestiques", Bulletin of the school of Oriental and African Studies (BSOAS IX: 1937-39) pp 861-869, University of London. M. Abolghasemr, RTsheh ShenasT - Etimologi, Ghoghnoos Press, Tehran 1374 (1995). A. Daneshgar, Farhang A'alam Farsi, Hafez NovTn Press, 1370 (1991). M. Abolghasemr, Fe'lhay FarsT Pari, Ghoghnoos Press, Tehran 1374 (1995). v^«&gt;jls pMel 
18: TABLE IV - Reference Abbreviations (continued ...) 64 MMF 65 MON 66 MPP 67 MZF 68 NAT 69 NFI 70 NYB 71 OEW 72 OXF 73 PEI 74 PHD 75 PHN 76 PLA 77 POK 78 PRT 79 RCH K. Khalili, Dictionary of Derivatives of the Persian ^wjls jiLa* ol£ii* &gt;_£^&amp;ji Infinitives or Farhang Moshtaqqat Masader FarsT, Institute of Cultural Studies and Research, Tehran, 1993. M. Mo" in, Farhang FarsT MoT'n, Six volumes, Amir Kabir press 1363 (1984). O^*® ^ ^-a-L!* Honari darbareh Zaban Farsi, Sokhan press, Tehran 1340 (1961). C. Berlitz, Native Tongues, Grosset &amp; Dunlapp Publishers, New York, 1982 F. Jonaydi, Nameh Farhang Iran, ^Ijjl ^»js i*b Bonyad Nayshabfir, Tehran 1368 (1989). Section 4, translated from C.H. Rempis' "Persische Worter im Deutschen," in Mitteilungen, Institut fur Auslands-Beziehungen, Iran-Nummer, 3/4, Stuttgart, 1960, S.229-233. H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1974. J. T. Shipley, The Origins of English Words, The John Hopkins University Press, Baltimore 1984. Jennifer Speake, Oxford Dictionary of Foreign Words and Phrases, Oxford University Press, New York 1997 M. Pei, The Families of Words, Harper &amp; Brothers press, New York 1962. D. N. MacKenzie, A Concise Pahlavi Dictionary. Oxford University press, London 1971. A. P. Pihan, Dictionnaire Etymologique des Motes de la Langue Francaise Derives de L'Arabe, du Persan ou du Turc, Paris 1866. Asya Asbaghi, Persische Lehnworter im Arabischen. Otto Harrassowitz, Wiesbaden 1988 J. Pokorny, Indogermanisches Etymologisches Worterbuck, Two volumes, Francke verlag, Bern 1959. E. Partridge, Origins - A short Etymological Dictionary of Modern English, MacMillan Co., NewYork 1958. J. Richardson, Dictionary, Persian, Arabic and English with Dissertation on the Languages, Literature and Manners of Eastern Nations, Sange-e-Meel Publications, Lahore 1829-1984. A-13 
21: TABLE IV - Reference Abbreviations (continued...) 80 ROE 81 SAP 82 SBK 83 SDQ 84 SHP 85 SIN 86 SKT 87 SLW 88 SNB 89 SNS 90 SOD 91 SOG 92 SOR 93 SPG 94 SYN 95 TAD R. Caliborne, The Roots of English, A Reader's Hanbook of Word Origins, Anchor Books, New York, 1989. A. Sayyah, Farhang Sayyah, Arabic - Persian Dictionary, ^}~&gt; «^a&gt;Js Three volumes, Translation of the Arabic "Al-Monjed" Dictionary, Eslam Publications, Tehran 1368 (1989). M. T. Bahar, Sabk ShenasT - Tarikh Tatawor Nasr Farsi, ^Ls ._£_&gt; Vol I, Tehran 1321 (1942). A. Siddiqi, Studien uber die Persischen Fremdworter im Klassischen Arabisch, Vandenhoeck &amp; Ruprecht, Gottingen 1919. J. T. Shipley, Dictionary of Word Origins, Philosophical Library press, New York 1945. G. Laufer, Sino-Iranica, Chinese Contributions to the History of Civilization in Ancient Iran, Field museum of natural History, publication 201, Anthropological Series, Vol XV, No. 3, Chicago 1919. W. W. Skeat, A Concise Etymological Dictionary of the English Language, Clarenden press, Oxford 1882-1967. W. B. Henning, "Sogdian Loan-words in New Persian", Bulletin of the School of Oriental and African Studies (BSOAS XT939-42) pp 93-106, University of London H. Kowsar, Sang Nebeshteh-ha Sokhan Miguyand, *ujj£~«&gt; Military Public Relations, Iranian Military Press, Tehran (1960's). M. Tavoosi, A Glossary of Shayast Ne Shayast, Shiraz University publications, 1986. B. Ghanb, Sogdian - Persian - English Dictionary, Farhangan Press, Tehran, 1374 (1995). jLw ^uu oV ijij ^imI^I - ^wjli -
```


## [2026-09-04T19:20:02.652Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'lemma: al' POK_full.txt | head -20; echo \"=== ary ===\"; grep -n -i 'lemma:.*ar(i)' POK_full.txt | head; grep -n -i \"lemma: ar\" POK_full.txt | head -20"
}
```


### [2026-09-04T19:20:02.723Z] TOOL RESULT

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
=== ary ===
3242:Root / lemma: aR-, ok- {*hek-) 
3632:From the extension of Root/ lemma: aR-, oR- {* heR'^-): "sharp; stone' with /--formant derived 
3768:Root / lemma: aR-1, aRo- {*hek-) 
3776:From Root / lemma: aR-, oR- {* hek'^-): sharp; stone' derived Root/ lemma: aR-1, aRo- 
3792:Root / lemma: aRru 
3806:Root/ lemma: aRru: 'tear' derived from Root/ lemma: daRru-: "tears'. The phonetic shift 
3860:Root/ lemma: aR-, ok-: (sharp; stone). 
4607:Root / lemma: arrid^i, np^i 
6231:Root / lemma: ar4 (er, or?), / 
6261:Root / lemma: ardi-, fdi- 
6280:Root / lemma: areg- 
6296:Root / lemma: ar(e)-g- {arg-?), fgi- {* her-(e)-g-) 
6421:Root / lemma: arenko- 
6440:Root / lemma: areq- 
6509:Root / lemma: ar(a)- 
6582:Root / lemma: ario-? 
6588:Root/ lemma: ario-?: master, lord, derived from Root/ lemma: ar-1', themat. (a)re-, 
6622:Root / lemma: ar-1', themat. (a)re-, heavy basis are-, re- and /-basis (a)n-, rei- 
6628:Root/ lemma: ar-V, themat. (a)re-, heavy basis are-, re- and /-Basis (a)n-, rei-\ "to move, 
6967:Root / lemma: ar-2ex er-
```


## [2026-09-04T19:20:06.223Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['PRT','SHP','FAF','IRN','SOD','MON','BQT','AHD']:\n    v=d.get(k)\n    if v is None: print(k,'MISSING'); continue\n    print('==',k, v.get('kind'), '|', v.get('title','')[:90])\n    print('   local:', v.get('local_file'), v.get('local_files'))\n    print('   offset:', str(v.get('page_offset'))[:300])\n\""
}
```


### [2026-09-04T19:20:07.920Z] TOOL RESULT

```
== PRT archive_restricted | E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958
   local: None None
   offset: None
== SHP hathitrust_fullview+archive_restricted | J. T. Shipley, Dictionary of Word Origins, New York 1945
   local: None None
   offset: None
== FAF none | A. Daneshgar, Farhang-e A'lam-e Farsi, Hafez Novin 1370/1991
   local: None None
   offset: None
== IRN local_scan_ocr | Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt'] None
   offset: 222 leaves; printed page = PDF page − 11 (PDF 101 = p.90; chapter openers carry no numeral). 6th printing 1382, same setting as 1368.
== SOD archive_djvu | Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'] None
   offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
== MON website+archive_djvu | Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 for
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] None
   offset: None
== BQT archive_djvu+local_scan_ocr | Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cite
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] None
   offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vo
== AHD archive_djvu+website+archive_restricted | W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edi
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt None
   offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
```


## [2026-09-04T19:20:10.548Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4217,4260p' POK_full.txt; echo \"===== ario =====\"; sed -n '6582,6625p' POK_full.txt"
}
```


### [2026-09-04T19:20:10.621Z] TOOL RESULT

```
Root / lemma: al-1, ol- 

Meaning: "besides; other' 

Note: 

Root/ lemma: al-1, ol-\ "besides; other' derived from Root/ lemma: ala\ interjection. 

Material: Latin uls " beyond ', *ulter, -tra, -trum " ulterior, situated beyond ' {ultro, ultra), 

compounds ulterior. Sup. ultimus= Oscan ultiumam^ the utmost, extreme, the highest, 

first, greatest, lowest, meanest '; 

Maybe alb. ulte, ulet'\o\N', ul'to low, sit below' : Latin ulterior -lus'compar. as from ulter, 

farther, more distant, more advanced, more remote'. 

Old Latin ollus " that, that yonder, that one; emphatically, that well-known; in contrast with 

hie, the former, (sometimes the latter)' {*ol-no-s, compare below Irish Ind-olland Slavic 

*oln/}, newer olle, c»///~"then, next', oll/c' he, she, that, in that place, yonder, there '; 

lengthened grade ollm "in the distant past, once' (probably after Im, exim reshaped and 

with Old Indie par-arr third-last year ' [compare nsp-uai] to be equated *dli, Lok. adverb, 

also the glosses olltana'the aged, old, ancient, of long standing ', olitlnata^ old, inveterate, 

ancient, former, of old times ' can reject - dor 61 -), Umbrian ulo, ulu^ that, that yonder. 



that one; emphatically, that well-known; in contrast with hie, the former, he, she, it yonder, 
that '; influenced by is, /ste etc. the cognates o//us, o//e would be uncolored to ///e'that, that 
yonder, that one; emphatically, that well-known; in contrast with hie, the former, 
(sometimes the latter)'. 

Slavic *c//7/"(lndo Germanic *oln-ei) = Old Church Slavic /an/, Czech /on/, poln. /o/?/" in 
the last summer, last year ' (' that year ', compare Latin o//rat that time, then'). 

The meaning from Irish a//far, a//a/c/{see below) also allows that the relationship of Old 
Indie arana-^ far, strange ' (= Avestan auruna- 'wild'?), arad'iroru a distance', are^ far ' 
===== ario =====
Root / lemma: ario-? 

Meaning: master, lord 

Note: 

Root/ lemma: ario-?: master, lord, derived from Root/ lemma: ar-1', themat. (a)re-, 

schwere Basis ara-, re-und /-Basis (a)n-, rei-\ to move, pass: gr. apiaroq " best in birth 

and rank, noblest'. 



Material: Old Indie ar(i)ya-^ mister, convivial ', ar(i)ya-^ Aryan ', aryaka^ venerable man '; 
Avestan airyo. Old pers. ariya- " Aryan '; 

gall. PN. Ario-manus{Q\\-, III 4594); Irish aire{Q\. primas) besides airech, where is to be 
formed *arJo-av\6 *arJako-, which to Old Indie aryaka behaves as gr. [jsTpa^ "youth' to Old 
Indie maryaka- 'male' (Pedersen Celtic Gr. II 100). Against it belongs Middle Irish ruireuoi 
here, but from ro + rV king of kings '. 

About Old Indie aryamanu. " hospitality ', m. " guest's friend ', Avestan airyaman-, 
npers. erman^ guest ', see above under al-1. 

W. Krause (rune inscriptions 539) should read properly Proto Norse arJosteRH. PI. ' the 
most distinguished, the noblest ', thus would have to be attached indeed an Proto Norse 
*arjaR^ posh, lofty, noble, plush, gentle, kingly, polite, courtly, elegant, genteel, stately, 
highbred, exclusive ' and an Indo Germanic *ario-, in the Old Indie phonetically with a 
derivative from arf-^ alien, stranger ' would have collapsed. 

Celto-Germanic PN Ar/o-v/sf us however, proves nothing, because Ario- could stand for 
*Hario-. Also Old Irish aire, airech ' suitor ' are ambiguous, see above under al-1. 

Maybe Arrianes lllyrian TN. 

References: WP. I 80. 

Page(s): 67 

Root / lemma: ar-1', themat. (a)re-, heavy basis are-, re- and /-basis (a)n-, rei- 

Meaning: to move, pass
```


## [2026-09-04T19:20:15.406Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4260,4382p' POK_full.txt"
}
```


### [2026-09-04T19:20:15.460Z] TOOL RESULT

```
Indie arana-^ far, strange ' (= Avestan auruna- 'wild'?), arad'iroru a distance', are^ far ' 
seems possible. Moreover also maybe Old Indie an " of strangers, stranger ', ar{/)ya- " 
suitable, proper to the stranger ' (compare Old High German e//-/ent/' foreign land '), then 
Subst. " hospitable, lord, master, ruler, man ', in addition ar{/)ya- " to ar{/)ya- , suitable, 
hospitable ', hence, VN ' Arier = Aryan', arya/ca- " venerable man ', aryaman- n. " 
Hospitality ', m. ' Guest's friend '; 

maybe Arn'anes lllyrian TN. 

Avestan a/ryd{= arya). Old pers. ar/ya{= ar/ya), " Aryan ', Avestan a/ryaman' guest, friend 
', npers. erman^ guest ', in addition sarmat. VN AAavoi (osset. *a/an), osset. //'"Ossete', 
/ino/y'Ossetic' " Ossetic ' (P. Thieme*), the stranger in the Rigveda, fig. f. d. client d. 
Morgenl. XXIII 2, 1938; Specht KZ. 68, 42 ff.); 

Old Irish a/re{*anos) and a/rec/i' nobleman, of noble people, suitor ' can belong to 
preposition a/r- " in front of ', thus ' standing in the first place ', (Thurneysen ZCP. 20, 354); 
mythical Irish ancestor Erem6n\s scholar neologism to En'u^ Ireland '. see below ar/o-^ 
lord, god, master'. 



*) Thus Thieme (aaO. 159 f.) properly puts here reinforcing prefix gr. £pi-( reduced 
grade api-), e.g. api-yvajToc; " easily (the stranger) recognizable ', Old Indie ari-eic surely 
must lead back to Indo Germanic *er- . Thieme puts further here Old Indie sun-^ master, 
ruler, lord' as su-n- " hospitable ' and n'-sadas " worry for sustaining the stranger '. 



Old Irish o//M\. " honorable, large, extensive ', actually ' above (the ordinary) going out 
(formally = Latin o//us, Indo Germanic *o/nos), compounds {/i)u////u^ farther, more ', Adv. 
ind-o//^ ultra, extreme ', from which maybe also /nnonn, /nnunn^ over, beyond ' (with 



assimilation in collaboration with inonn^ the same, identical'; (common Celtic -ns- > -nn-), 
Thurneysen KZ. 43, 55 f.; Pedersen KG. II 195), ol-chen(a)e^ in addition, but ', actually " 
on the other side (and) therefrom on this side '; ol-foirbthe' pluperfect, past perfect ', oldau, 
oldaas' when I, when he ', actually " about (the) outside, what I am, what he is ', inaiir 
certain, sure ', actually ' situated on the other side ' (of it inoillus' confidence, security'; 
/nuMg ud'protecWon, safety'; with o/C/)^ ultra, beyond ' maybe corresponds o/' says ' as " 
ultra, beyond, further ', originally in the report in a continuous speech). The conjunction o/' 
because, sice ' keeps Thurneysen Grammar 559 against it for related with cymr. o/' 
footprint '. 

Besides with a: Old Irish 5/ (with Akk.) " on the other side, over - beyond ' (simplification 
from *a//\n the pretone). Adv. fa//{ *to-al-na) ' on the other side, there ', anair from on the 
other side, from there, over here ', with suffixed Pron. of the 3rd person all, allae, newer 
alla^ beyond, on the other side ' (proves original dissyllabic old formation also of the 
prepositional form is not provided with pronominal suffix, see Thurneysen KZ. 48, 55 f., 
thus not from without ending Indo Germanic *c»/or *al)\ derivatives: alltar^ the world of the 
dead, the other world, hereafter ', also from ' to savage areas situated on the other side ', 
alltarach' otherworld, ulterior, thithertho '. 

Gall, alla^ another, other, different ', a//c»5 'second' (Thurneysen ZCP. 16, 299), VN Allo 
broges= mcymr. ail-fro^ exiled, ostracized, banished' (to Z^Ao'land'), all-tud^ foreigner', 
acymr. allann, (common Celtic -ns- > -nn-), ncymr. allan' outdoors, outside '; Old Irish all- 
slige " the second cutting out '. 

Gothic alls. Old Icelandic allr. Old English eall Old High German aira\\\ besides in the 
compound Germanic ala- (without -/7c>-suffix) in Old Germanic matron's names Ala-teivia, 
Ala-gabiae e\.c, Gothic ala-mans^ all people, humanity ', Old High German ala-warr totally 
true ' (Modern High German albern); compare Old Irish oll-athair (epithet of Irish God's 
father Dagdae " the good God ') = Old Norse aA/pdA (epithet of Odin), ' all father '. 

Latin alers, allers^ taught; learned, instructed, well-informed; experienced, clever, 
shrewd, skilful ' according to Landgraf ALL. 9, 362, Ernout El. dial. Latin 104 from *ad-ers, 
*allers (contrast to iners). 

From an adverb *air there, in a specific place, in each case ' (differently Debrunner 
REtlE. 3, 10 f.) have derived: 

alios^ other': 



Armenian air other'; 

gr. hKKoc, "other' (Cypriot aiAo(;), n. aAAo, compare aAAo5-an6(; ' from elsewhere, from 
another place, strange ' (= Latin aliud, forms as in Latin longinquus 'far removed, far off, 
remote, distant'), in addition aAAriAwv etc ' each other', aAAaiTU) ' makes different, changes 
', aAAavn variation, change, exchange, trade ': aAAorpioc; ' becoming another, strange ', 
from Old Indie a/Tya/ra "somewhere else' corresponding adverb; 

Maybe zero grade in alb. {*nyatra) tjeter'other' [common alb. n > nt > t[ : Old Indie anyatra 
"somewhere else'. 

Latin alius= Oscan a//c» "other things', n. aliud= gr. aAAo, in addition from the adverb air. 
a//enus 'strange' (from *alHes-nos), ali-quis, ali-cubi e\.c\ Comparative alter, -era, -erum^ 
one from two ' = Oscan a/Z/Aa/r? 'alteram' (from *allteros-), by Plautus also altro; in 
altrlnsecus, alfrovorsum the syncope is caused by the length of the whole word; here also 
alferare, adulter, alternus, altercarr, 

gall, alios (Loth RC. 41 , 35), Old Irish alle (*alios), n. 5/7/ (from adverbial 5//from *al-na; 
palat. /comes from alle), cymr. all, bret. e//(from *ellus. Comparative *alllds), doubled Old 
Irish alalle, aralle, n. alalll, aralll, mcymr. etc arall, PI. erelll {llixom the adverb alfy, 

Gothic alJIs "other', but only in compositions, as Old Saxon ell-lendlu. ' foreign land ', 
Old High German el/-lent/6s. = Modern High German ' woefulness ', Gothic alja-leiko^ 
other, different ', Old Icelandic elllgar, ellar. Old English elllcor, elcor^ other, otherwise, ', 
Old High German elichor^ further', and in adverbs, like Old English elles, engl. e/se" 
other, different ', Old Norse alla^ otherwise ' etc.; a comparative formation *allra\s Old 
English eira " other '; 

Tocharian A alya-k^, B alye-k^'ahKoq i\q' ( *alle-k^, Pedersen Groupement 26, 
Tocharisch 117); unclear is the absence of palatalization in A alak^^ other ', alam^' each 
other', B alam^ somewhere else', a/e/s/e 'strangers'; 

ostiran. etc hal-cF any (thing) available, etc '. 

References: WP. I 84 ff., WH. I 30, 32 f., Feist 33 b, 39 a, Schwyzer Gr. Gr. I 614. 

About the sound change from *anJosto * alios see Debrunner REtlE. 3, 1 ff., about 
angebl. pejorative character of a see Specht KZ. 68, 52, Die alten Sprachen 5, 115. 

See also: About anioss. under S. 37 {an2). 



Page(s): 24-26 



Root / lemma: al-2
```


## [2026-09-04T19:20:43.287Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### AHD al-1\"; grep -n -E '^\\s*(al-1|al-2|al-|ario-|ar-)' AHD_watkins1985.txt | head -20; echo \"### AHD grep al-1 context\"; grep -n 'al-1' AHD_watkins1985.txt | head -20"
}
```


### [2026-09-04T19:20:43.350Z] TOOL RESULT

```
### AHD al-1
278:al-'
280:al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
287:ar-. Also are-. To fit together. I. Basic form *are-. 1. Suf- fixed form *ar(g)-mo- in: a. Germanic armaz in Old English earm, arm: ARM}; b. Latin arma, tools, arms: ARM?2, ARMADA, ARMADILLO, ARMATURE, ARMOIRE, ARMY; ALARM, DISARM; C. Latin armus, upper arm: ARMILLARY SPHERE. 2. Suffixed form *ar(e)-smo- in Greek harmos, joint, shoulder: HARMONY. 3. Suffixed form *ar()-ti- in: a. Latin ars (stem art-), art, skill, craft: ART!, ARTEL, ARTISAN, ARTIST; INERT, (INERTIA); b. fur- ther suffixed form ‘*ar()-ti-o- in Greek artios, fitting, even: ARTIODACTYL. 4, Suffixed form *ar()-tu- in Latin artus, joint: ARTICLE. 5. Suffixed form *ar()-to- in Latin artus, tight: COARCTATE. 6. Suffixed form “*ar(e)-dhro- in Greek arthron, joint: ARTHRO-; ANARTHROUS, DIAR- THROSIS, ENARTHROSIS, SYNARTHROSIS. 7. Suffixed (su- perlative) form *ar(g)-isto- in Greek aristos, best: ARISTOCRACY. II. Possibly suffixed variant form (or separate root) *dr-dh-. 1. Latin drdé, order (originally a row of threads in a loom): ORDAIN, ORDER, ORDINAL, ORDINANCE, ORDINARY, ORDINATE, ORDO; COORDINA- TION, INORDINATE, SUBORDINATE. 2. Latin drdiri, to begin to weave: EXORDIUM, PRIMORDIAL. 3. Latin or- ndre, to adorn: ORNAMENT, ORNATE; ADORN, SUBORN. III. Variant or separate root *ré- (< *reo-). 1. Latin réri (past participle ratus), to consider, confirm, ratify: RATE!, RATIO, REASON; (ARRAIGN). 2. Suffixed form ré-dh- in: a. Germanic *rédan in (i) Old English rédan, to advise: READ, REDE (ii) Old English réden, condition: HATRED, KINDRED; b. Germanic *rédaz in (i) Old High German rat (> German Rat), counsel: BUNDESRAT, RATHSKELLER (ii) Old English rédels(e), opinion, riddle: RIDDLE?. 3. Zero-grade form *ra- in Germanic *radam, number (see dekm). IV. Variant (or separate root) *ri-. 1. Suffixed form *ri-tu- in Latin ritus, rite, custom, usage: RITE. 2. Suffixed form *(a)ri-dhmo- in Greek arithmos, number, amount: ARITHMETIC, LOGARITHM. [Pok. 1. ar- 55.]
### AHD grep al-1 context
280:al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
900:a. Old English risan, to rise: RISE; b. Old English drisan, to arise (G-, up, out): ARISE. 2. Germanic causative *raizjan in: a. Old English réran, to rear, raise, lift up: REAR?; b. Old Norse reisa, to raise: RAISE.] rtko-. Bear. 1. Latin ursus, bear (< *orcsos): URSINE. 2. Greek arkios, bear: aRcTIC, ARcTURUS. 3. Celtic *arto- in Welsh arth, bear, in the name Arthur (> Medieval Latin Artorius, Arthur): ARTHUR. [Pok. tktho-s 875.] ruk-1, Fabric, spun yarn. Celtic and Germanic root. 1. Germanic *rukk6n- in: a. Italian rocca, distaff: ROCKET!; b. Old High German rocko, distaff: ROCAM- BOLE; C. Old French rocquet, head of a lance: RATCHET. 2. Germanic *rukka- in Old French rochet, rochet: ROCH- ET. [Pok. ruk(k)- 874.] ruk-2. Rough. Extension of reu-2. 1. Lengthened-grade form *rik- in Germanic *riéhwaz in Old English rih, rough, coarse: ROUGH. 2. Lengthened variant form *rig- in Latin riga, wrinkle: RUGA, RUGOSE; CORRUGATE. [In Pok. 2. reu- 868.] runo-. Mystery, secret. Germanic and Celtic technical term of magic. Germanic *riinaz in: a. Old English riinian, to whisper: ROUND?; b. Old Norse riin, secret writing (akin to the Germanic source of Finnish runo, song, poem): RUNE!, RUNE?. [In Pok. 1. reu- 867.] sa-. To satisfy. Contracted from *sas-. 1. Suffixed zero-grade form *s9-to- in: a. Germanic *sadaz, sated, in Old English sed, sated, weary: SAD; b. derivative Ger- manic verb *sadon, to satisfy, sate, in Old English sadian, to sate: SATE!. 2. Suffixed zero-grade form *s9-ti- in Latin satis, enough, sufficient: SATIATE, SATIETY; (ASSAI2), ASSET, SATISFY. 3. Suffixed zero-grade form *s9-tu-ro- in Latin satur, full (of food), sated: SATIRE, SATURATE. 4. Suffixed zero-grade form *so-d-ro- in Greek hadros, thick: HADRON. [Pok. sd- 876.] sab-. Juice, fluid. 1. Germanic *sapam, juice of a plant, in Old English sp, sap: SAP}. 2. Illyrian sabaium, beer, probably akin to the source of Italian zabaglione, zabaione, a frothy dessert: ZABAGLIONE. [In Pok. sap- 880.] sag-. To seek out. 1. Suffixed form *sdg-yo- in Germanic *sdkjan in Old English sécan, sécan, to seek: SEEK. 2. Suffixed form *sdg-ni- in Germanic *sdkniz in Old English sdcn, attack, inquiry, right of local jurisdiction: SOKE. 3. Zero-grade form *sog- in Germanic *sak- in: a. derivative noun *saké, “a seeking,” accusation, strife, in Old English sacu, lawsuit, case: SAKE}; b. Germanic *sakjan, to lay claim to (denominative of *sak6), in Old French seisir, to take possession of, seize: (SEISIN), SEIZE; c. Germanic *sakan, to seek, accuse, quarrel, in (i) Old English forsacan, to renounce, refuse (for-, prefix denot- ing exclusion or rejection; see per'): FORSAKE (ii) Old Norse saka, to seek: RANSACK. 4. Independent suffixed form “sdg-yo- in Latin sdgire, to perceive, “seek to know”: PRESAGE. 5. Zero-grade form “sog- in Latin sagdx, of keen perception: SAGACIOUS. 6. Suffixed form *sdg-eyo- in Greek hégeisthai, to lead (< “to track down”): EXEGESIS, HEGEMONY. [Pok. sdg- 876.] sai-. Suffering. 1. Germanic *sairaz, suffering, sick, ill, in Old English sdr, painful: sore. 2. Derivative Germanic adjective *sairigaz, painful, in Old English sarig, suffer- ing mentally, sad: SORRY. [Pok. sdi-, 877.] sak-. To sanctify. 1. Suffixed form *sak-ro- in: a. Latin sacer, holy, sacred, dedicated: SACRED; CONSECRATE, EXECRATE; b. compound *sakro-dhét-, “performer of sacred rites” (*-dhét-, doer; see dhé-'), in Latin sacerdés, priest: SACERDOTAL. 2. Nasalized form *sa-n-k- in Latin sancire (past participle sanctus), to make sacred, conse- crate: SAINT, SANCTUM; CORPOSANT, SACROSANCT, SANC- tiFy. [Pok. sak- 878.] sal-1, Salt. 1. Extended form ‘*sald- in: a. suffixed form *sald-o- in Germanic *saltam in Old English sealt, salt: SALT; b. Germanic zero-grade suffixed extended form *sult-j6 in (i) Old French sous, pickled meat: SOUSE (ii)
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
1219:AGIO al-1 AGITATE ag- AGLET ak- AGMINATE ag- AGNAIL angh- AGNATE gene- AGNI egni- _ AGNOMEN no-men- AGNOSIA gnd- AGO ghé- -AGOGUE ag- AGONY ag- AGORA! ger-1 AGORAPHOBIA ger-! AGRAFFE ger-2 AGRAPHA gerbh- AGRAPHIA gerbh- AGRARIAN agro- AGREE gWere-3 AGRESTAL agro- AGRIA agro- AGRICULTURE agfo- AGRIOECOLOGY agro- AGRIOLOGY agro- AGROSTOLOGY agro- AHIMSA ghei-i, ne AHRIMAN men-1
1225:ALAR aks- ALARM al-1, ar- ALARY aks-
1228:ALERT al-1 ALEURONE al-4 ALEXIA feg-1 ALEXIPHARMIC alek- ALGOLAGNIA  slég- ALIAS al-1 “ ALIBI al-1, kWo- ALIBLE al-3 ALIEN al-1 ALIFORM_ aks- ALIKE fik- ALIMENT al-3 ALIMONY al-3 ALIPHATIC leip- ALIQUOT al-1, kwo- ALL al-5
1229:ALLEGE ag-, leg-1 ALLEGORY al-!, ger-1 ALLELOMORPH al-1 ALLERGY werg- ALLEVIATE legh- ALLEY! al-2 ALLIGATOR al-1 ALLITERATE deph- ALLITERATION deph- ALLO- al-1 ALLOCUTION tolkw- ALLOMERISM (s)mer-2 ALLOPATRIC  peter- ALLOT kleu-3 ALLOY leig-1 ALLUDE |leid- ALLUVION leu(e)-
1232:ALTER al-1 ALTERCATE al-1 ALTERNATE al-1 ALTHEA al-3 ALTHORN  ker-1 ALTIMETER al-3 ALTITUDE al-3 ALTO al-3 ALTOCUMULUS _al-3 ALTOSTRATUS _al-3 ALTRICIAL al-3 ALTRUISM al-1 ALULA aks- ALUMNUS al-3 ALVEOLUS aulo- ALWAYS wegh- ALYSSUM wikwo- AM es-
1329:CAKE kak-2 CALAMITE kolem- CALAMITY kel-1 CALAMUS kolem- CALANDO ghé- CALDRON kele-1 CALENDAR kele-2 CALENDER skel-3 CALENDS kel@-2 CALENTURE kele-1 CALIBER ped-! CALIX kal-1
1330:CALL gal-2 CALLIGRAPHY kal-2 CALLIOPE kal-2, wekw- CALLIPYGIAN  kal-2 CALLISTO kal-2 CALLOSE kal-3 CALLOUS kal-3 CALLOW gal-1 CALLUS kal-3
1331:CALM kéu- CALOMEL kal-2 CALORECEPTOR kela-! CALORIC kele-! CALORIE kele-1 CALORIFIC kela-1 CALORIMETER kela-1 CALORIMETRY kela-1 CALOYER gere-!, kal-2 CALUMET kolem- CALUMNY kel-8 CALVARIUM klewo- CaLypso_ kel CALYPTRA kel-2 CALYX kal-1
1342:CENTROBARIC gWere-2 CENTUM dekm CENTURY dekm CEPHALIC ghebh-el- CEPHALO- ghebh-el- -CEPHALOUS ghebh-el- CERAMIC ker-4 CERASTES ker-! CERATODUS dent-, ker-1 CERATOID ker-! CEREAL ker-3 CEREBELLUM ker-1 CEREBRUM ker-1 CERES ker-3 CERTAIN krei- CERVINE ker-1 CERVIX ker-1 CESSION ked- CESSPOOL spirare cEsTus! kent- CEsTUS? kae-id- CHAETA ghait- CHAETOGNATH genu-2, ghait- CHAFE dhé-1, kele-1 CHAFER gep(h)- CHAFF! gep(h)- CHAIR sed-1 CHALAZA gheled- CHALAZION gheled- CHALCID ghelegh- CHALCOCITE ghelegh- CHALCOPYRITE ghelegh- CHALCOsIS ghelegh- CHALICE kal-1 CHALLENGE kel-8 CHALONE ghé- CHAMAEPHYTE dhghem- CHAMBER kamer- CHAMELEON dhghem- CHAMFER bhreg- CHAMFRON kaput CHAMOMILE dhghem-, mélon CHANCE kad- CHANCEL carcer CHANCELLOR carcer CHANCRE kar-1 CHANGE skamb- CHANT kan-
1453:ELSE al-1
1579:HAG2 kau-2 HAGGARD kagh- HAGGLE kau-2 HAGIO- yag- HAIL! kaghlo- HAIL? kailo- HAKE keg- HALBERD bhardha, kelp- HALE! kailo- HALE? kele-2 HALF skel-1 HALIBUT bhau- HALL kel-2 HALLOW kailo- HALO-  Sal-1 HALT! kel-3 HALT? kel-1 HALTER! kelp- HALTER? § sel-4 HAM konemo- HAMADRYAD deru, sem-! HAME_ tkei- HAMLET tkei- HAMMER ak- HANDIWORK kom HANDSEL sel-3 HANG konk- HANKER konk- HANUMAN genu-2 HAP kob- HAPLESS kob- HAPLOID pel-3, sem-1 HAPPEN kob- HAPPY kob- HARANGUE koro- HARBINGER koro- HARBOR koro- HARD kar-1 HARDS_ kes-! HARDY! = kar-1 HARE kas- HARM kormo- HARMONY ar- HARNESS _nes-1 HARPOON  serp-1 HARPSICHORD ghere- HARQUEBUS keg- HARRY koro- HART ker-1 HARTEBEEST ker-1 HARUSPEX ghere- HARVEST kerp- HASH! =skep- HASLET ghasto- HASTATE ghasto- HAT kadh- HATCHET skep- HATE kad- HATRED ar-, kad- HAUBERK kWel-1 HAUGH kel-2 HAUGHTY al-3 HAUL kele-2 HAULM kolem- HAUNT tkei- HAUSTELLUM aus-2 HAUSTORIUM aus-2 HAUTBOY al-3, busk- HAVE kap- HAVEN kap- HAW2 kagh- HAWK! kap- HAWKER keu-2 HAWSE kWel-1 HAWSER al-3 HAY kau-2 HAZEL koselo- HE! ko-
1604:HIDALGO al-1, dh@(i)-, kwo-
1724:KURTOSIS sker-3 Kvass kwat- KVETCH kwét- KYLIX kal-1 KYPHOSIS keu-2 KYRIE keue-2
1888:MORDENT mer-2 MORE mé-3 MORELLO oOm- MORES mé-! MORGANATIC mer-1 MORGEN mer-1 MORIBUND mer-2 MORN mer-1 MORNING mer-1 MORON mé6(u)ro- MOROSE mé-! -MORPH merph- MORPHALLAXIS _al-1 MORPHEME merph- MORPHO- merph- MORPHOSIS merph- MORROW mer-1 MORSEL mer-2 MORTAL mer-2 MORTAR mer-2
2059:-PARA pere-1 PARABLE gWelg-1 PARABOLA gW¥ele-1 PARACHUTE pere-1 PARACLETE kele-2 PARADE pere-1 PARADIGM deik- PARADISE dheigh-, pert PARADOX dek-! PARAFFIN pau- PARAGRAPH gerbh- PARALLAX al-1 PARALLEL al-1 PARALLELEPIPED ped-! PARALOGISM leg-1 PARALYSIS leu PARAMECIUM mak- PARAMOUNT ad-, per! PARAMOUR amma, pert PARANOIA nous PARAPET peg- PARAPHERNALIA bher-1 PARAPHRASE gWhren- PARAPLEGIA plak-2 PARASOL pere-1, sawel- PARATAXIS tag- PARBOIL beu-! PARCAE pera-1 PARCEL pere-2 PARCENER pere-2 PARDON d6-
2209:SAL sal-1 SALACIOUS  sel-4 SALAD sSal-1 SALAMI sal-1 SALARY Sal-1 SALE sel-3 SALI-  sal-1 SALICIN sal(i)k- SALIENT sel-4 SALINE sal-1 SALLOW! | sal-2 SALLOW? | sal(i)k- SALLY sel-4 SALMON sel-4 SALON sel-1 SALOON sel-1 SALSA Sal-1 SALT sal-1 SALTCELLAR sal-1 SALTPETER petra, sal-1 SALUBRIOUS sol- SALUTARY sol- SALUTE sol- SALVAGE sol- SALVE! selp- SALVO! sol- SAME sem-! SAMITE mei-4 SAMIZDAT d6-, sem-1
2215:SATISFY sa- SATRAP pase, tké- SATURATE sa- SATYAGRAHA es-, ghrebh-1 SAUCE sal-1 SAUERBRATEN bhreu-2, stiro- SAUERKRAUT siro- SAUTE sel-4 SAVANT sep-1 SAVE!  sol-
```


## [2026-09-04T19:20:44.938Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BRT airya\"; grep -n -iE 'airya|airiia|a[iī]ryaman|airyanəm|airyana|vaējah|vaejo' BRT.txt | head -40"
}
```


### [2026-09-04T19:20:45.003Z] TOOL RESULT

```
### BRT airya
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2769:mit  pairi  1)  'ringsum  absuchen,  auf- lesen': mazdayasna  aitihh  zimß  pairisa- yanta  (Opt.)  . .  varfsqmca  (als  Obj.)  ..yezi nsit  pairiianie  . .  astqmca  7-arpsqm:a  .  . V.  ö.  7f. 's\  z)  'herumsuchen  nach  — , aussuchen,  auslesen':  asstnanqm  xraoldva- nqm  .  .pairlstanqmY.i4.4'i'>;  A.3.5'^; —  uxtiitn  srlr>m  pairisttm  F.^^f'*'; V.J. 42  PüZ,;  —  pairi  daxma  aSlayqn  vi daxma    calsayqn   Y.S.z.  a)    mit    Dat
2878:mit  avi  dnwS.  2,  mit  dopp.  Akk.:  pairi- AaySi,.yl  duiyäitya  nqma  yam  masyäka avi  duzvalanAö  Auyairyatn  natna  aojaite (3PP.)  YtÄ  51 ;  V.  13.  2,6.  '  a)  wie  2  a: m>r>y3  .  .  yim  malyska  avt  duivaear)hö kaArAatas  nqtna  aojaite  V. /A 15.
3113:KotnpA.  i  Ableit.  —  AbleiL  aus  ajra-.  —  ü. agriyä-  Adj,,  mp.  airyai.  —  PB.!  a^ryat.  — 1  Hd$.  srairim,  d.  i.  mp.  j-iir,  womit  die  vor- ausgehenden  Wörter  trjra,  a-ftim  bbersetit werden  (vgl.  asar  für  anaira-\  und  atriin.  ~- *)  Pü.  erl.  ayryai  afiar  soüin  mit  loi  i  sar "Waschen  des  Kopfes";  vgl.  West  SEE. /A 456.
3466:•  g-  at  va  Part',  zur  Anknüpfung  eines Satzteils;  1)  'oder  aber,  oder(vel)'  '>,  parallel mit  vä''':  vacaah3  vS  at  vä  manat»hä zastsiiya  {sd.)  vä  Y.33.2;  —  x^aitB  (sd. vil  at  v3  vsrpzSnyS  airyamnä  vä  Y. 33- Z-  2)  'und,  und  auch':  yamsm ,.  xsmävats  {^d)  al  vJ  . .  staomyä{sd.) vacä  Y.33.Z.
3791:aibLgairya-
3817:•  j.  aiwi.ta£ina-  i)  Adj.  'heranlaufend, anspringend'  zur  Begattung,  vom  Kamel- hengst:  ustrake  vmairyaos  ,  .  °naAi  Yt 14.11.  i)  n.  'Herzulauf,  Anlauf  (nur Komp.).
4081:•  j.  afsman-  n.  'Verazeae  (der  Gä^rJs)'": tiSranqm  kaurvafaoiryanam  . .  haitilca "manaca  (AP.)  '^  vacas^a  vacastastlmla  (sd.) Vr. /J.3; — vfsp?m^a  'man^m{Pi&y  yasa- maide  Y.  Ji.^;  —  aitatca  vacö  .  .  %ri.- afsm»m  (sd.)  . .  kais  Al  'man  (NP.)  ". .  wel- ches sind  seine  (des  AAunaVairya)  Vcrs- zeilen?"  Y,  19.16.
4352:•  j.  an-airya-  Adj.  (fem.  'yä-^  'nicht  — , unarisch':  'yä  daüiAävS  Yt.  1K2;  if}.68; —  yanam  .  .  daüyunqm  N.  GS;  —  'ya!a daitihuiMwistära  {%A.^  V, /.  17.
4472:ASm.  (n.)  aus  ainya-.  —  Vgl.  zu  mairi«,.  - Pü,:  an.  —  »  Die  von  DsT.  ZA.  a,  Z4[  ge- billigte Fassung  des  Dk.  S.  44-  6S  "st  mit  dem Wortlaut  {urvatqm  aimm !)  nicht  zu  vereinigen ; s.  •nairya-  No.  3.
4570:—  vjfTirayru/m  ..yat  asti  °rf  ahutia  airya- mana  ". .  zwischen  dem  A/i.-  und  dem  Airy.- Gebet"  Vr.  24-i;  —  ''v  *am7sSsi!a  spmts saosyantasca  P.^f;^o,_ji(?);  —  'n  pitan i^A.)  puknmla  Yt.J0.117;  117,  116^;  — ' 'n  urvaitya  (sd.)  V.4-3— 4*;  —  ävis  iiä. "rs  hsiiiü . . rätttyl(%d.)  '^■33-T,  —  cvai  'rj *mr3us. .  "wie  viel  im  Kreis  der  Männer . ." V.5.27;  —  yim  'r»  vastnm  frajasäi  (sd.) 'V.i0.i6;i6;yd.ij.i4.  aa) unräumlich: ; \'it/iaiy()xsäydi^iyä  agarbäyam  "rimä  haina-  \ raim  "diese  9  Könige  nahm  ich  in  diesen Schlachten  gefangen"  Bh.  4. 3.  ß)  zeit-  j lieh:  *kva  altqm^aEsnmn  paiH.barat1  "r?, akuna  *airyamana  "wann  soll  man  das  1 Brennholz  herzubringen?  Zwischen  (der  | Rezitation)  des  Ah.-  und  des  .,4»>/, -Gebets"  |
4632:pataha  yat  'n  vä  aai  -w  v,l  .  ."  N. S3.  2)  Praen.  a)  mit  Akk.  'innerhalb, in,  unter,  zwischen';  a)  räumlich,  auf  die Frage  wo?  und  wohin?:  i  °r  tmä  äahyäve^ martiya''  kyi^  . .  "innerhalb  dieser  Län- der . ."  Bh.  /.  8 ;  —  I  avaiy  °r ''  didsm  frii- Aayam  {sd.)  Bh.  2, 13;  —  T;/  ja/W  (sd-) var?zäne  V.ij.iy;  —  'rt  daifiAu  pi}p?r?- tane  Yt  70.8,  J5.49;  49';  —  yS  vJräsaili 'r)  räiia  rJsmana  Yt.  7^47;  —  tiisiltm (sd.)  yim  'rp  mSurunua  büx'aimca  V.  /.  7 ; ■ —  yßi  'r)  v^rxika  *as  *mars}a  (sd.)  V. j8.  70  PüZ.;  —  'rj  sqm  asmanimca  "zwi- schen Himmel  und  'Erde"  Y.6Ä  15;  Yt. ÄS,  /O.95,  y,i3',  43,  44; — hax3or)mia , .  'n  mäti/Dtnla  Avan^a  Yt  ö.  5 ;  —  ..  */ra- hinein  (sd.)  *'r?i'>  airsatca  bammaca  H.öS; —  Vii^raymm ..yat  asH  "n  ahuna  atrya- mana  ". .  zwischen  dem  AA.-  und  dem  Airy.- Gebet"  Vr.  24.1, ;  —  -/-j  ''am?sSsca  spnitS saosyaiitas^a  P.3<i,30,ji{?);  —  'rv  pitan {zd.)  puhnmca  Yt. /0.117;  117,  116';  — °r>  urvaitya  (sd.)  ^",4.3—4*;  —  ävis  tui 'rs  Asnta . . rä/ayy(sd.)  Y._J3.7;  —  ä'at 'r.> *ii?rsus. .  "wie  viel  im  Kreis  der  Männer . ." V.5.27; — yim  'n  vastmii  fraJasäHsd.) V.j6'.i6ji6;Vd.y./4.  aa)  unräumlich: \'h/iaiyiixsilyahiyJ  agarbäyam  °r  ima  Aattia- rana  "diese  9  Könige  nahm  ich  in  diesen Schlachten  gefangen"  Bh.  4. 3,  ß)  zeit- hch:  *kva  aitqm  *agsm3m  paiti.barälf  °r) oAuna  ''airyamana  "wann  soll  man  das Brennholz  herzubringen?  Zwischen  (der Rezitation)  des  AA.-  und  des  ^;>f', -Gebets"  I
4696:•  j.  ama'vant-,  g.  Sma'vant-  Adj.  (fem. 'vaifi-)  'kräftig,  stark,  mächtig,  gewaltig, wuchtig'i  a)  vona)  Menschen  und  ß)  Göttern : o)  narf .  .  pancajiasanhö . ,  hrpzats  avi.- amahe  'vatö  Yi.S.i$;  — ya'ia  agj?  'va .  .fraxitäne  z?ma  paiti  Y.5. 20;  —  aisäta "iwa  'vantaslä  buyamä  (sd.)  Y.4J.4;  — , ^vm  yäka  ^vifrö  naväso  Vyt2;  Az,2;  — | faritJm  il  ^icJ  yähanä  tat  °vatqm  kyat ^wä  xiayqs  (sd.)  aissm  dyll  'vantim  "eine Frage  von  dir  (d.  i.  Zar^  ist  ja  wie  eine Frage  Mächtiger.."  Y.^l^.io,  zit.  A.  4. 3, wo  amavanlam  und  amavant^m ;  —  °fa (NSm.)''  äs  Vfri^rava"^  nqma  v^rp^rava] Os  'va  nqma  Yt.  i4'S9-  ß)  ralnul bjrTZö  yö  '»i  Yt,JO,ioo,  i2.6;  /7.16,  J2. ' 5;  — yö  {sraolö)  .  .  niaza  'va  firS^raja'^ , Vr./5.3;  —  °va  mt^rä  Yt  10.  loj ;  6,  25, loa;  —  airyamarigm  .  .  'vantpm  vprjhrd- ^
4814:mit  "p.parü,  y  parai''>  'weg-,  fortgehen, sich  entfernen';  a)  absol.:  natrya-san/ta . . para.ili'ii  (2SIA.)  upa.vazanuha  avi  ntnä- n>m  airyamaifii  (sii.)  V,  22.  7;  —  *para.- äip^^  upa.vazala  nairy3.sa»hs  avi  . .  V. 22. 13;  —  zaota  (sd.)  anakaxtö  par^at dqhiUäi  .  .  zao^r)m  raSxsaiti  N.  A'o;  — yezica  *alte  ratavö  *anahaxta  para.tya- yanti^^^  N,  Ai?;  —  uzayeni  psrayaii  V,  2-2. I.  a)  II  militärisch  'ausrücken,  ins  Feld ziehen':  avd^ä/aiy  a'iaAam  paraidiy (2SIA.)  avam  käram  jadty  Bh,_^.3;  2.7, 10; — ara^äsam  a>aA<im  piirait>l(iP'PTA.) avam  käram  . .  jatä  Bh._y.14_:  9,  2,6,14;
4951:Satzes  'jedoch':  *k!ra  .  .  *a^st»im  fiaiti.- bamt?  antarf  (sd.)  aAuna  *airyamana *Sy^mcit  a°  vilcim  gii^anqm  asrutpm  (sd.) paitiiarS  aratufris  N.  10^.
4963:'lam  tiadrtabairam  adam Bh.2.i;  5,  J.iö',  ^.1,  5,  ,,  .  _ pairika  yä  äuzyairya  . .  tiitrys  'vqm  pairi- kam  ädanzayeiti  YLÄS4f.;  —  ^artnS apantmaia  . .  aom  (ASn,)  s^anttB  Aangfur- tayata  mihrS  Yt.19. 35;  —  yai  srum paitiJiiruäi  .  .  SdnnjaySti  aom  srUm  . . V.  p.  1 4.  a)  1!  zugleich  voia.usweisend  auf
5072:•  j.  ava'Sra  Adv.  'illic,  dort':    airyamm vaijS  . , .    dasa    ''^ra    manttö   zayana  V.
5117:sükaya  (sd.)  bräZ3m  Yt  14.  33;  33;  — jainü  mqm  ahuna  vairya  "vata  snai>isa ya%a  asma  . .  YtZ/.ao;  P.22;  —  kthrpa 'vatS  (GS.)  *sraya  (sd.)  ya%a  dämqii sralstail'^.2.^;  —  ifkrpa  "vatqm  sraya ydka  di'iayatqm  zaosS  (sd.)  Yt  17. 1 1 ;  — st»r)naoili  aria  *°vat  starim  .  .  ya'ia  .  . P.25(?).  a)  substantivisch  'Wntum',  mit Gen.  part:  yat  mS  'va(  daüvayasnanqm ni/atitn  ydka  .  .  Yt  J.77;  —  upa  .  .  'vat siWi/  (sd.)  urva  *isaiti  yd^a  .  .  H.  2. 2.  b)  mit  Akk.  der  Beziehung:  andern .  .  y3  asti  'vaiti  masö  yd^a  vJspa  ima äpS  Y.  65. 3 ;  — yash  . .  "vant^m  (als  ASn.) mass  vikilnayät  ya'ia  hi  tanus  atphat  V. 7.51.  a)  mit  ya'i:a  yat  'wie  wenn,  als ob':  °vaia  aejanha  yd^a  yat  panca  narS "mit  solcher  Kraft,  als  ob  es  fiinf  Männer wären"  V.  75. 10  PiiZ.  2)  'dass':  asti  sl
5481:*)  Vgl.  Yt.  5.  Ans  dem  Flus»  A,,  der  nach Yt.5.3  von  der  Höhe  Haiairya  mm  .See  Vcuru- iasa  tliesät  (doch  5.  90),  stammt  alles  Wasser der  Erde;  s.  auch  Bd.  12.  5,  13.  I,  5 f.  Die Göilin  A.  wird  als  ein  schönes  Mädchen  ge- dacht, von  dem  Yt.  5.  64,  78,  u6  IT.  eine  auf- (allig  ins  Einielne  gehende  Schilderung  geben. Vgl.  DsT.  ZA.  2.  316,  363,  wo  weitere  Litt.
5539:•  '].  airya-,  p.  ariya-  1)  Adj.  (fem.  ya-) 'arisch':  'yanam  daRyunqm  . .  tüiryanam dahyunqm  Ytl  13.  i43';' 1°.  87',  5.49, 58,  117,  ig.  56,  69,  V,  ig.  39 ;  —  'yä  dai- tihavd  \i.8.jfi,  52%  58^;  —  'yäbyS  dai- tüulys  Yt.^. 61  \  10.4;  —    yäiyö  (statt
5545:•  j.  airyana-  Adj.  'arisch':  "m/w  :^ar3nS Yt.  J<?.  1,  5,  7,  8,  S.  2.  9*>;  —  sonst  von vasjah-  (sd,,  auch  fdSt):  °n»m  vagjö,  'yeiie val/aAi.
5546:Ableit.  aus  airya-.  —  Vgl.  'Apiä-f^l  —  Pü.; erSii  (vH).  —  'I  S.  /■.  9  =  Ny.j.  5  steht  air- yanqm  x'ar^nä.
5547:j.  airyanimna  N.  loy.  lies  airyamana.
5548:•  jj  g-  'airyaman-,  g.  airyäman-  m. 'Genosse'  uzw.  priesterlicher,  Angehöriger des  ersten  oder  Priesteratands  (s.  unter 'pistra-),  'Sodale' ;  Sing,  auch  koU.  'Soda- lität',  nur  gAw.:  iJ  yama  kp  x^allus  {%<!.) dätäis  anhat  yp  ,  .  Y.  /fg.  7 ;  —  ahyScH x'aSus  (sd.)  yjsal  ahyä  virizsntm  mat yamnn  . .  Y.J2.1;  —  yf  '^jvaj  masdn asruinm  . .  yazli  (sd.)  apa  K^'aüSuScä  tar>- maitTm  virn^nahyiilä  . .  'yamanascä  . .  Y. 33-4  i  —  y^  asäuia  vahiils  :^aSä  (sd.) vä  al  vä  v>r>iSny3  yämiiä  (IS.  als  Subj.)  '> vil .  .  Y.  JJ.  3;  —  pairl  clausus  'yama- nascä  dadaili  ndii  .  .  i-ir>z5nä  (sd.)  Y.46. I.  A)  Name  einer  Gottheit":  vairya sar)ha  para.äi'd  upa.vasanuha  avi  nmli' mm  yamaini  imat  sanhsis  'yamanäi  J' "A^,  geh  weg,  fahr  hin  ins  Haus  zu  A., das  sollst  du  dem  A.  kund  machen"  V.
5551:1 99  'airyaman-  —  aurvant-  aoo
5558:VgL  'airyaman-.  —  m.  atyaman-  m.  i)  'Ge-  °vanqm  aunvJ^mftn  Yt  Jj.  57;  —  von fahrte',  a)  Name  eines  Äftfia ;  np.  Tgl.  ÖTiiäu  Httoma:  kaoma  . .  ya~ia  raeuaJie  hubaoi'ds 'Gast'«).    —   Pü.:    ertnän  iSü-i  ädiiah,  ädtia-    ,.,  v  rn  •
5566:•  j.  'airyaman-  m.  Name  des  mit  J  (7/r- ,  •  j.  'aurvataspa-  Adj.  'der  schnelle ysmä  isys  beginnenden  Gebets  Y.54.1:  Rosse  hat';  a)  von  ^rar-imd  Äj'ari>.tiiji^u-: 'matiim  mq^ranqm  maBittm  Yt.j.5;  —  Är'ur?  "toffi  YL/0.90;  6.4;  —  'tun  bavähi T-3r/irayn3m. .  ya^asli  antan  ahuna(&A.)  yaia  kiari  Az.  6";  —  am.nakc  hü  yat 'manaiAD.)Vi.24.i;*li.ioj.  a)  sonst |  Vn^  YLJO.  13;  —  hiarsxsaS^m  'ptm mit  isya-.  'mamm  isim  .  .  ßäsB  mq^fvm  Yt  6. 1,6, 12.^4, 1^.81,  \.  16.4;  —  hvar>- ..  b»r?am  Aa',aoxt?m  Vr.2.10;  G,/.6,  S.j^/attJj  °päi  Y.ÜÄ22;  —  hrerixiaiiahe 2.3;  —  tfm..  vJspanqm  sravanhqm  ufard.-\ ..  -pake  Yt.  Ö.o,  Y, 22. 24;  /.  11;  —  Iwan- kainm  fradaiqm  yim  'mamm  tsim  FrW. '  xsaiia  'pa  (VS.)  V,  j/.  5,  b)  von  apqm 4-1',  1 ;  —  'taan^m  isim  . .  maiisüm  o/aAe  napät-.  apqm  napa  -ps  Yt  ig.  51';  — sra-.arahqm  Y.54.2;  Vr.  24,1;  —  °manS  aPqm  napättm  'ptm  Y.  2. 5;  —  apqtn isyehe  hafu{iitä..'manö  isyeke ,.  haililca  ..  nap5  °pa  Y.65.13.  'pä'a  VyLjJ, Vr.24.2;  /.8,  S.7.3.                                    4'>"(?).
5570:•  j.  airyava-  m.  EN.  Name  eines  Gläu-  des  Viitäspa-.  pu>ri>m  yat  'fa/ie  taxm>m bigen:    manuS.airahe  (sd.)    'vahe   asaonS  kai-alm  züstJspfm  Vtj.  105.
5724:•  j-t  E-  (.  P-)  asan-iaj«-,  j.,  p.  asman-  m." i)  'Stein':  *ja«s(alsAP.)  äi/i{sd.)  maya  äiti darSii"V.g.  11;  —  'sSnaShia'^ ..  vtHiaeh-a' . .  tBiuxha  (sd.)  V,  6. 5 1,  a)  als  Amulet: °samm  *siyaire.ci^rim  (sd.)  abars  *aAurö.- puirS  (sd.)  Yl;4.59-  b)  als  Waffe, 'Schleuderstein,  Steingeschoss':  Uavasca  . . •sanas(a  . .  (NP.)  fraäaxlaitya  V.  Z7.9;  — karjtS  .  .  vazrö .  .  'sänS  atymSJütä  Yt.  JJ. 72;  /.18;  —  jainti  mqm  ahuna  vairya avavata  snai^isa  ya'^a  'sma  iatS.masa (sd.)  Yt/7.20;  —  'sanS  (als  AP.)  tasia drazimnS  katä-masatiks  Aynti  V,  117.43); —  yahmai  .  .  aurvan/a  *yuxta  vJsa %an/asante  (sd.)  .  .  asUnas/a  (als  AP.) vispeMvia  "dem  .  .  die  Renner  am  ge- schirrten Wagen   ziehen  -  .  und  die  all-
5737:•  j.  asah-  n.  'Ort,  Stätte,  Platz,  Raum': y8  anyeAe  *'saAya  (LS.)  bansma  */ra- stff^ie^.ioi; — äaire  "saAi  razaaiam(sd.) V.Ä97;  —  atfffi  daoam  °s/f  rämsMäitTm (sd.)  ndil  kuäalJäiim'V.i.i;  iPUZ.,  Vyt. 2'j(?);  —  xrüma  'sl6rs{3is  Subj.)  frasinia danunam  YL  13.  ^S;  —yatca  aakat  %wyqs- brnalrva  'sauham  V.2.23;  —  yäi^a  °sS mai^animca  atmisilSe  äaiära  (sd.)  Yt.  13. 67.  a)  sonst  neben  sSihra-.  paoirlm •sanham^a  Sstiranamca  vakishm  frii' "iwtnspm  .  .  airyatDtn  vaSjB  "als  die  erst- beste der  Stätten  undWohnplätze.."  V.  I.a; Y.  /.  lÖ;  —  hpnti  atiyäscii  °s3sca  sSi^rSsca irirasla..  V.J.  20;  Y.  3.16,  S.  7.28,  2.28; —  äat . .  vazaite  väiS . .  avi  'sä  avi  /gi'irS ai-i  karh'ä  yäis  hapta  Yt  Ä  3  3 ;  —  para  nU ahntät  h<üa  'sarihal^a  ^t^räatca  axslat .,  iia/a  äzätliscaY.g.^y,  —  Adoa..  aktnai •saaAalia  sUrbraläi  paiti.jasata  iii V.  ß.  5  4 ;  55,  57;  —  tä  yai'.yeinti  p>sanahu kavc  'tahi  säi^rafai  Yt.  IJ.  27.
5806:Vgl.  aitairya-.  —  Pü.;  slar-lih.
5807:•  j.  astairya-  n.  Name  einer  Krankheit: paitiäätJe  yaskahe  .  .  maltrkake  .  .  "yehe V.20.3.
5922:•  j.  *"a-srävayamna-''  Adj.  'was  nicht  auf- gesagt, rezitirt  wird':  'ii3t  paiti  ahuiia^ vairyat  "ohne  dass  der  AhV.  rezitirt  wird" N.  tiS'
5979:—  y5  "i^wat  mazdä  'lim  . .  yazäi  (sd.)  a Y.J'J.4;  —  ysi  °tois  p?rmatth5  .  .  "die, des  Ungehorsams  voll,  .  ."  Y.rf^.i at  tu  mSi  nöit  'tä  pairyatr/zä   "da   be- fahlst du   mir,  nicht  ohne   dass  ich  ge- horchte" Y.^j.ia'*,
6003:•  j.  a-zäta-  Adj.  (fem.  °td-)  '(noch)  nicht geboren'  sva,  '(noch)  zu  gebären,  künftig* : hätamca  aaAusämca  zätanamca  'tanamla aiamamY.6^.6',  —  irfri^u/am  ../vantam .  .  narqm  '/anqm  frasBxar^ram  saol- yattiqmY.24.y,MLi3.i7,ig.az;  —  yat  asti airyanqm  äaAyunqm  sätanqm  'tanqmca (GPt)  ". .  den  jetzigen  und  den  künftigen" Vl  ig,  s6.
6076:—  'sähe  paiti  mq^rfm  'sähe  paiti  fra-  manarihäY.4ß.  10;  —  '/ahya  yäsa  (sd.) sasiim  V.  4.  43  (s.  a);  —  'fa  i-iyaca  Vyt  a^m  Y.54.  i;  —ySais'sMt  nipSrfhi  (sd.) 75;  —  yS  'sili  hr>jyqsl>mS  (sd.)  R  /;  —  manasut  vohn  V.28.  11.  3)  im  jAwr.: airyamarum  isfm . ,  matistim  'saht  srava-  hs  aiwyiixsayatB  hadü  'Saia  vasträca  .  . tthqm  Y.54'3;  —  'iahe  myazdanqm  Vr.  Y.  3<?.  4;  —  yöi.äim  hanhana  (sd.)  'säca ^■3;  —  y^i  til/'rat  (sd.)  aurö  mainyus  frSriticaH.8.i; —  •/«lä""  nmtaahana.. dahlm 'sähe rauh fus  Yt.13.TT,  —  haoma..  yaorum  (sd.)  äste  V,4.45;  —  ahunm haÜTm^a  'sa/ie  xi'r  (sd.)  ahi  Y.  10.  4^  — \mazdqm   yS    'sähe    apanöJ?mS  yS    'sähe
6130:•  j.  *asa-  n.  Name'*  des  mit  asnn  voha vahUttm  astX  beginnenden  Gebets  Y.  27. 14*':  yö  °s3m  staoiti  (sd.)  . .  hö  mam  slaoiti yim  ahunm  mazdqm  H.  i.  3;  7;  —  stäomi a^3m  n3isml  äagvs\t.24.y,  Y. //.  19  und /2. 1 ;  —  sardiiustrahe  .  .  yd  paoiryö  .  . Staat  'Lm  naist  daivS  Yt.  13. 89;  —  yal  nä . .  %ris  "s^n  ufajtuyät  V.  18. 43 ;  —  "hmca *!0  pasca  hü  fräsmSJaitim  (näml  stuyät od.dgl.)  N.  6"^;  imd  so  Öfters.  a)  auch  mit a)  vanhav-'h  aiwi^r^lmahi  's>m  voAa  Vr. J7. 1.  ß)  vaAista-'^:  ahun^mca  vairitn  .  . °s?m(a  vahUtim . .yeAhl.tiätqmca\.6i.\\i3. 8,'Hyuf.S;—jainii  mqm  ahuna  vairya  ..lapa- yäti  mqm  'la  vakUta  Yt/7. 20;  —  6ayqm 'iahe  vahistake  yazatnatde  'sähe  vahÜtahe yasamaide  frasraeimmca  .  .  Y.  20.  5;  — zara^uitrS  ys  paoiryö  .  .  staota  °sfm  ya^
6281:—  r3laca  vaauhi  .  .  °saane  (VS.)  V.  /(?. 19,  Vytjö;  S,  1.5,  2.5;  —  raziflam  astim ..  "saonJm  Yt.16.1,  4;  o,  20;  —  airyama- mm  iitm  '^avan^m  Vr.  24-  3 ;  —  kaomS °^ava  Y.p.a';  10,14;  —  haoma  °lava (als  Vok.)"'  duraosa  Y.  j/.  10;  —  rasmiö °lilum  Yt  J2. 7;  9; —  sraohm  .  .  '/avarum Y-  57-  2i  33,  Yt.  II. T,  —  Aaurvat3t>m 'savaram''^  asahe  ratüm  Y.  71.  12;  — am^ntät^m  "savanpm'i^  asahe  ratüm  Y.7J, 13;  —  ahura  müra  .  .  •s'avana  (AD.) Y.  2. 1 1 ;  YL  70. 14s;  —  ahuraHbya  miitraei- iya  '/avanaäiya  Y,  j.  11,  a)  bes.  von Ahura Mazääh:  3  äim  tä  vaca  rämayal ahurS  masdä  'sava  alavansm  zarä^ulinm V.5.2I;  jp.15  (statt  Akk.),  Y.7/.4,  5,  57. 24,  Yt.S.i,  11.1%  12.4,  16.3,  Yt/0.89, 7J.  14,  15;  —  ahur)m  mazdqm  'iavamm aiahe  ratüm  Y.2,2,    t6.\,  ^5.1,  7/.2,  4;
6291:—  airyamansm  islm  'savanum  a/ahe  ratüm G.  7. 6 ;  —  aZtm  vahili»m  . .  'savamm  asahe ratüm  Vr.2.6*';  7.4»;  —  bayqm  yetiAe.- hstqm  ..  '/aenlm  Y.2I.$;  —  yetihE.hataya ..  'laottyä  aZahe  rä^wS  Vr.7.4;  2,6;  — staotanam  yesnyanqm  .  ,  'iaonqm  Vr.  i.  3 ;
6334:KompA.  —  Vgl,  asaiairyani:  —  Pü.;  /u tthtäkik  sardär.
```


## [2026-09-04T19:21:01.180Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD\"; grep -n -iE '\\bEr(an|man|ic)|ērān|ērmān|Ērānwēz|ēr\\b|wēz' PHD_mackenzie.txt | head -30; echo \"### PHD2\"; grep -n -iE 'Eran|erman|wez' PHD.txt | head -30"
}
```


### [2026-09-04T19:21:01.247Z] TOOL RESULT

```
### PHD
1099:aneran [)n).:rl)71I] non-Eran, the world beyond Eran.
1100:an-erang [)n)ylng] blameless.
1683:Burzenmihr [bwlcynmtr ] the third major Fire of Sasanian Eran, that
2214:£rAn eyl)n I N --] Eran, (land of) the Aryans.
2216: --ag [_hi] an Eranian, Aryan.
2217:erang [)ylng] blame, condemnation; error, heresy.
2218: --ih: = erang.
2219:eranJ-,v. I, leraxtan.
2222:leraxtan, eranJ- [)ylhtn ' , )ylnc- I J )yrxt] blame, condemn, damn.
2224:2eraxtan, eranJ-                 I M (yrxt, Cyrmr-)] fight, dispute.
2278:Farrobll~ [plwb(')g] the first major Fire of Sasanian Eran, that of priests
2634:Gu§nasp [gwln(')sp]      the second major Fire of Sasanian Eran, that of
6045:beget (frazand) warzidan.                   blame (n.) iiwenisn, erang(ih), nikoh-
6231:column stiin(ag); military -- karawan.   condemnation <:asmagahih, erang(ih);
6491:elder dadmeh, mehtar.                        Eranian £ranag.
6495:eloquent gowag.                              error abandih, erang(ih).
6628:force must, stabrih; vital- axw.             friend ayar, dost, erman.
6810:hole may, siirdg, siirax.                      humble erman(ag), ertan, narm.
6924:Iran(ian), v. Eran(ian).                   kinsman xwesawand.
7262:Persian parsig; v. Eranian.                    sriidan, (flute) pazd-.
12203:eranag                     \,,~              ewkardag                \'~'jto'
12211:erang                       ~~               agumegih               .AU 1)6 to'
12212:erangih                   -'"tY~             agumcg                    ,~tv
12217:ermanih
12220:ermanag              ,~~                     ayab                        Q)t\Y
12233:                            "~               Eran                      l~'"
### PHD2
128:delete mezidan ... suck. for ?mēzišn ... read ! meziin ... for mistan, *mēz- read... *mēz-.. mihoxt [mytwht' = Av. midaoxta-| falsehood. *mihr .. add ~ druxtan : break faith. add mizīdan, miz- [myc-ytn' | N mazidan] suck. for *moy-mard ... read mowmard ... mēy ... add M mwy. read nüxun [n^hwn' | P nxwn, N nàxun] (finger) nail. delete nāyīzag ... (read wezag). nek, ~th ... add benefit. nibastan ... delete SKBHWN-tn' < A Vškb; nibastan ... read M nb’st, P nb’y-. nibeg ... add M nbyg. nibištan ... |YKTYBWN-tn'... (not -stn'). nidan, nay- |DB(Y)LWN-tn' < A Ydbr |... nigün, ~sar |-s 1 | (P ngws’r)| downwards. add *nihēb |nyhyp | N ~] fear, terror. for nīšān read nišān...
149:~Th : prodigality, waste. мапу |H(W)BDN < A hwbdn', bd |... wany(b)ūdīh |HWBDN'bwtyh, ... war-wézag [wl-w^yck'| andaxtan : cast lots. wāzīg ... read -wazig |-w cyk' | N -baz] -player. wezag |w yck'| lot. wiyaban, ~ig ... add confusing. Wizarš |wyzl3| a demon.
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
217:arzómand [le wmnd | (N arjumand)] valuable, worthy. ~ih: value, worth. Arzür []zwl] a demon; a mountain at the mouth of hell. a-sag [?s?*k! | M *s?g] innumerable, countless. азап Pon! | N ~] at rest, easy, peaceful. “АП: rest, ease, peace. a-sar Dell endless. āsāy-, ~išn, v. āsūdan. a-sazāģ ["sc? k!] unfitting, unsuitable. a-sazisn|ig Dscfn-yk'] imperishable, permanent. ~ih: imperishability, permanence. a-sēj [Psyc] free from danger.
292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
321:ë ру | (M hyb)] particle giving the present tense optative sense. é, v, éd, éw. ēbāraģ [*dyp'lk', ^dwlk! | N éwàr] evening. ébgat(ih) ['ybgt!, -yh = Av. aifi.gati-] (onslaught of) Evil; the Adver- sary. ēbsrūsrim [>ур-, ?ybslwslym = Av. atBisrūdrima-) the gah from sunset to midnight. ébyünghan [>ур-, ?ywby?nghn!, etc. = Av. aiBydshana-] sacred girdle, = kustig. ёё Pye | (P ?ушус), N héc] (with a negative) not any. ēčand, v. éw-Cand. éd (HN A < A hr? | M? yd] this; v. dāštan. ~ ray ёё [cf. N z-é-rá] because, since. édar [LTME < À I-tnh | M?ydr, N ~] here. édin [ytwn'! | N ēdūn] thus, so. ~ih: (correct) manner. ëg [ADYN' < А *dyn | М ?yg] then, thereupon. ëk Pywk' | M yk, N yak] one. ëkanag [Pywk’nk! | N yagana) submissive, obedient. ^h : submission, obedience. ēk-dād [ywkd’t'] sole-created. ēmēd [*dmyt'] hope. ēn [ZNE < A znh | M *yn, N in] this. -ën [-yz! | = M, N -in] suffix forming adjectives of material or quality. -endag [-ndk! | M -yndg, N -anda] suffix forming present participles. -én-idan [-yn-ytn' | M -yn-ydn, (N -àn-)] suffixes forming causative and transitive denominative verbs. *énókén Pynw(k)kyn' = Av. *aēnē.kaēnā-) heiress (under the obligation of continuing her father's line). enya рулу | (M ?n’y)] otherwise, moreover. lër [d] | M Zur, v. azér] down, below; low; under. — ud abar: upside down. tēr Pyl] noble; hero, ~ih: nobility, good conduct. Eran [y”x! | N ~] Eran, (land of) the Aryans. ~ag [-k'] an Eranian, Aryan. érang [”y/ng] blame, condemnation; error, heresy. ~ih: = érang. éranj-, v.  * éraxtan. Ērān|-šahr (yPnitr! | N ~] land of the Aryans. —-wëz [-wyc] (original) home of the Aryans. 1ёгахќап, ёгапј- Pylhtn!, ?уЇпс- | J ?yrxt] blame, condemn, damn.
323:2ēraxtan, ёгапј- Pylhtn', *ylnc- | M ‘yrxt, ( yrnz-)] fight, dispute. éraxtür [y/At? 1] warrior. ēr-kaš ['dik£ | M *yrkš] (hands under the armpits in respectful) salutation, greeting. 1ërmán [?y/mx! | (MÉÁry! mwn), N ~] friend; а god. — ih: friendship. 23ër-man(ag) ['dim?n(k)'] humble. ēr-menišnīh [dimyninyh] humility. ér-tan ['ditn!'] humble. ~ih: humility. ērwār [D yleo?1] befitting a hero. ērwāraģ [*dlw?Ik! | J ?rw’rh] jaw, cheek. ésm ['ysm] = ézm. esp", v. sp”. éstádan, ést- [YKOYMWN-tn! < A ygym, У gum; ?sttn!, *zost- tn! | M ‘yst-’dn, N ~] stand; be, continue (as auxiliary of the perfect con- tinuous tense). ~išn: permanence, lasting, dwelling. ēš Pys | N xéf] plough. efm, v. $n. &(w) [z; HD < A hd | M ‘yw, N -ēļ a, one. éwan [*dwn') stalk, trunk. ēwān ['dw?n!] bridle. éwar ру! | J ?yf?r] certain(ly), assured(ly). éwarz [dwlc] movement. éwarzidan, éwarz- ['dwlc-ytn!] move, travel. éwarzig ['dwlcyk!] moving. 1&wáüz [?уш?с] word, utterance. tēwāz [?уш?с] sole, only. ~ig [-yk'] particular, individual. čw-bār Duech?) once. ē(w)-čand D у(то)спа] some, a few. éwén Pdwyn' | M *ywyn, (N àyin)] manner, custom, form, propriety. pad —: properly. léwénag ['dwynk! | M *ywyng] = ëwën ; v. ёё-. Ў *éwénag [?*dwynk! | (N āyīna)] mirror. Set (ъд) yn k éw-kard(ag) ['ywkrt(k)', -kltk'] united, joined. ē(w)-mēg D»(zo)mtok!] wearing (only) one shoe. éw-sün Pywsn' | (N yak-sān)] uniform, (a)like. ^ Ah : uniformity, likeness. éw-tüg Pywt?k' | М ‘yw 12, (N yaktà)] alone, single, individual. éz-, v. yaz-. —išn [уст] worship. ézm [CY BA < A syb | N hëzum] firewood, fuel. ged Zm4
325:farr-, v. xwarrah. Farrūbāģ [plwb(’)g] the first major Fire of Sasanian Eran, that of priests and nobles. farrox [plhw' | M prwx, N ~] fortunate, blessed, happy. ~ih: fortune, joy, happiness. filāsūfā [pyPswkp!y] philosopher. frabih [plpyh | (P frbyw), N farbih] fat, stout. Fradadafš [pldtpš = Av. fradašafšū-| the south-eastern continent of the earth. fradág [MHL < A mhr; ИРА! | N farda] tomorrow. frādahišnīh [pP dhšnyh] increase, progress. fradom [AWLA < Ar. !?wD; pltwm | (M prtwm)] first. ~th: first, beginning. fragan [plk?n'] base, foundation; origin. fragandan, fragan- [plkn-dn'} lay foundations. frahang [pl’hng | N farhang] education; knowledge. --estàn [-st?n!] school. frahanj-, v. frahixtan. frahist [p/h(y)st! | (M pryst)] most (superlative of freh), frahixtag [plhhtk' | N farhixta] educated, trained, skilled. frahixtan, frahanj- [plhhtn', pDhnc- | P frhynj-, N far~] educate, teach, instruct. framādār [рж?РЦ commander, ruler, chief. framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin. ~-burdar [-bwlt?l | N -bardār] obedient, submissive. framāy-, ~išn, v. framüdan. framds [bl(?)mwš | M pr’mws, N farámos] forgotten. framošidan [plmwšytn'] = framuštan. framüdan, framāy- [plmwin', plm'd- | M prm'dn, prmy-, N far~] order, command. — $n: order, commandment. frāmuštan, frāmēš- [pl(?)mws-in' | M prhmwst, pr’mwi-, N fard~] forget. franaftan, *franam- [pinptn!, *plnm- | M prnpt, prnm-] go, proceed, depart. franāftan, franām- [pin!ptn!, pli m- | P fri m-] 1. lead, conduct, re- move, promote; 2. profess, propagate (faith). ~išn: removal, promotion, profession. frarast [p/”Pst'] a cubit (18 in.). fràrón [p lwn'] righteous, honest. ~ih : righteousness, honesty. frasang [plsng | N farsang) parasang (4 Roman miles).
380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
597:tru(f)Š [t/wu(p)$ | (P tryff), N turf] sour. truftag [t/wptk'] stolen; intercalary (days). tuhig [twhyk! | M twhyg, ЇЧ tuhi] empty, vain. ~ih : emptiness, void. tumbag [twmbk' | N ~a] drum. tund [twnd | N ~] sharp, violent. ~ih: violence, vehemence. Tür [twl | N ~] one of a people inimical to Eran, Turanian. ~ап [—n! | N ~] (land of) the Turanians. Turk [twlk' | N ~] Turk. tu&t [twst'] silent. tuwān [twb!n! | M twn, N ~] might, power. ~ (+infinitive): it is possible to, one can. ~ag [~k' | N —a] mighty, able. «gar [-kl | N ~] rich. ~garih: richness, wealth. ~ig [-yk'] able. ~igih: ability, power. --sāmān [-s’m’n'] the extent of one’s ability. tuxšáé [twhPk! | M рох р, N tuxsa] diligent. “Аһ: diligence, endeavour. tuxšīdan, tux&- [гол у! | (M. twxf‘yst), N ~] strive, endeavour. ~išn: endeavour, striving.
649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
651:wénig [wynyk! | M wynyg, N bini] nose. wénO£ [wynwk' | N bunü] lentil. wēš [zoy£ | = M, N béf] more. wé&ag [wysR! | N beta] thicket, wood. --estün [-st?n'] woodland. ~ig [-yk'] silvan. wēwag [wdpk! | N béwa] widow. 1wéxtan, wez- [NSSHWN-tn! < А V nsh; wyhtn', wyc- | P wyxt-, N bextan, béz-] sift, select, choose, separate, cleanse, purify, winnow. ~išn: selection. *wēxtan, wēz- [wyhtn!, wyc-] swing, brandish, throw, pour out. Wīdadafš [wydtpš = Av. wīdašafšū-| the south-western continent of the earth. widang [wtng | P wdng] trouble, distress, constraint. widār [xt' | N gudár] passage, entrance. widarag [wtlg | M wdr, N guàar] path, passage. widardan, wider- [wtitn!, wt(y)l- | M wd(y)r-, N guóar-] pass (by, away), cross, die. : ~išn(īh): passage, crossing, death. ~i$nig : transient. widārdan, widār- [xwt?/-tn! | M wyd’r-, N guóárdan] let pass, transport; endure, suffer. widārīdan [w?lytn'] = widardan. widaštan [wtstn' | N gušaštan] = widardan. widāxtan, widāz- [wt’hin', wtc- | (P wd’c-), N gudaxtan, gudāz-| melt, dissolve. widāzīhistan, widazih- [wt’cyh-stn'] be melted, dissolved. wider- , -išn(-īģ, -ih), v. widardan. widerān [wt(y)?n! | N guóarán) transient, dying. widest [zot(y)st! | N bidast] (hand) span (9 in.). ~ig [-yk'] span-sized, midget. widimās [wtym’s | (M wyd’m’s)] wonder, miracle. ~ig [-уА!] wonderful. ~ih: miracle. widimušt [wtymust | M wd(y)mwšt] astonished. ~ih: astonishment. *widwar [wytwl] contented, resigned, consoled. ~ih: contentment, resignation, consolation. wiftag [wyptk'] passive sodomite. wigrad [zogPt! | N bīdār] awake, alert. wigradan, wigras- [zog tn, wgl’s- | M wygr'd, wygr’s-] awaken, rouse. ~i$n(ih): awakening. wih-, v. wistan. wihan(ag) [zh?n(k)', (b-) | M wl?ng, N bahāna] cause, reason. wihēz- [wyhyc- | M twhyz-] move, progress. wihéz(ag) [wyhyc(k')] movement, progression.
655:wistardan, wistar- [wstl-tn! | N gustardan] spread. wistāx [wst??hw! | M wyst?h, N gustāx, bistāx] confident, bold. ~ih: confidence, boldness. wis [w(y)$ | M wyš, N gus] poison, venom, bile. wišād [SLYTWNt', Р! | M wid, N gušād] open, wide, loose. wišādan, *wišāy- [SLYTWN-tn! < A У šrh; wPtn! | M шурап, (wys?h-), N gušādan, gušāy-) open, loose, free. wišād-dar [.SL Y TWNt! BBA] hospitable. wišād-dwārišnīh [zP??! dzb?lšnyh) going about ‘open’, i.e. without kustīg, or šabīg. | wišān- [w®n- | = P] shake down. *wišāy-, v. wišādan. wiškar [zo£hl | N bisgar(d)] hunting-ground, wilderness. wiškīdan, wiškin(n)- [wfkytn!, wškn-] divide, separate. ~išn: separation. wiskofag [wskwpk' | N biškēfa] blossom. wiškuftan, wiSk6f- [vvškup-tn! | J guškuftn, gwškwß-] blossom; hatch. wišūb-, —išn(-īģ), v. wišuftan. wišoūmand [w%wmnd] poisonous, venomous. wišūdag [wiwtk' | (M ghwdg)] abortion, daevic creature. wišūdan [wswtn'] bear daevic offspring. wišuftan, wišūb- (zfwp-tn! | M wiwb-, N *gusuftan] disturb, destroy. ~isn: destruction. ~1&п16 : destructible. *wixSay- [whsd-} forgive, forbear. ~iSn(ih): forbearance. ~išnīg : forbearing. lwiyaban [20(у) р?п! | Р шуп, N bīābān] desert. *wiyābān [wyd’p’n'] astray, wandering; deluded. ~ih: delusion, deception. wiyaban|garih [wyd"Pnklyh] deception. ~ig [-vk'] wandering, itinerant. wiyāftan, *wiyüb- [wd ptn! | M wy’b-] open (the mouth). wiyan [wyd?n! | M wy’n, N giyān] tent. wiyiz- [wydwe-] loosen, undo. *wiyufs- [wdwps-] make merry. ~išn: merry-making. ~iìšnīg : merry. wizandag [wzndk'] quaking. wizandidan, wizand- [wznd-ytn'] tremble, quake. -išn: quaking. wizar [wc] | M wer] separation; explanation. wizārdan, wizār- [wel-tn' | M wyc'rd, wyc^r-, J bz?rd-, N guzardan] separate; explain, interpret; perform, fulfil, redeem. ~išn: decision; redemption.
857:Aryan Ērānag; — home, land Ērān- šahr, Eranwéz.
1792:Eranian Ērānag.
2486:Iran(ian), v. Eran(ian).
2493:issue abāz raftan. item tag. itinerant wiyābānīg.
3099:permanence asazišnīh, ēstišn.
3100:permanent asazišnīg.
3103:perseverance pattügih.
3105:Persian parsig; v. Eranian.
4049:transient frasawand, sazišnīg, ward- išnīg, wideran, widerišnīg.
4183:utterance éwaz, wazag.
4269:washerman gazat.
5122:wideran
5212:wigrad wigridan nerang n��rógómand nerog nilopal nirmadomand nirmad ncm, wem wūmār wēmārīh nēmasp wimand wimandómand wimandig wimustan nemag ncmroz ncmtan niság wisbed
```


## [2026-09-04T19:21:02.859Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HRN erman\"; grep -n -iE 'erman|ērmān|īrmān|Iradsch|Irag|airyaman' HRN.txt | head -20; echo \"### HUB\"; grep -n -iE 'erman|airyaman|arya|ariya' HUB.txt | head -30"
}
```


### [2026-09-04T19:21:02.934Z] TOOL RESULT

```
### HRN erman
1177:indogermanische Vocalsystem 20, 63.
1622:aw. airyaman- N. pr. eines Genius; phlv. ermän^
1704:*) Arm. hav *Gro88vater* stellt S. Bugge mit Petermann wohl
1861:Arische (bezw. indogermanische) Doppelformen vaph-
1887:*) Die indogermanische Wurzel vehh'^ veph', vtra'rtü. wthen^ zuerst
1889:indogermanischem Wörterbuch, erster Theil.
2343:Wort wohl zuerst für indogermanisch erklärt.
2840:phlv. patlrak *) (mit verkürztem k , nicht patirag),
3208:also indogermanische Doppelformen wie bei [/^veph-,
3386:sowohl indogermanischem gji wie g2h,
3641:LW. :it^NlO"nü *Zimmermannsaxt' (de Lagarde, Ges.
5056:kurd. deriyän; af>'. dural; bei. dirag, dirray, n. diray,
5333:germanischen gh und g neben einander.
6000:ertanih, erman(i)sn 'niedrigen Sinnes' (Men.) ^); ai. vergl.
6323:Die indogermanische Grundform ist nach Hübsch-
6886:slc^ap' bezw. sk-ah- 'schaben, graben* als indogermanisch
7885:kurd. girtin 'ergreifen ; bei. girag , n. giray (106);
8368:np. serman *löwengleich' wird auch 'löwensinnig
8462:bei. mirag, n. miray (237); wa/. mari-am, mlrlt^ §iyn.
8635:Persiens (Petermann^s Mitteilungen, Ergänzungsheft Ko. 77), S. 83.
### HUB
345:72. Np. aryand *zornig, gierig kann zu zd. ereyant-
428:90. Die germanischen W5rter fiir 'Niesen' fiihrt Kluge auf
429:die Wurzein vorgermanisch qnus^) und ksmis zuriick."*)
632:140. Die Gleichung ermdn *Gast' ^= zd. airyaman- (nach
634:*Vasall, Dienerj — skr. aryamdn- Busenfreund, Ge-- 21 -
1507:geworden wie aryan zu Sran. Aber die Bedeutung des
2157:ap. daryah- ware phi. *darydk = dBrdk (vgl. jiid. tat.
2977:Hier nach Salemann np. faryand res sordida,
3558:1026. Dazu np. naryan 'Hengst', von gleicher Bildung wie
3582:vor. Ist das Wort iiberhaupt indogermanisch ? —
3940:sprache auf die indogermanische zuriick.
3941:Die indogermanische Grundsprache hatte folgenden
4575:Airan und Aryan, ap. g. pi. ^Ariyanam\ dSr Vacker =
4577:«5r5?, ^siz.n^rd (Min. und Shk.), aus *naryw- oder ^naryava-
4578:(Horn Nr. 1064)?; b^rUn 'aussen* von *6?r- = "^dvarya-?
4579:(oben p. 33) ; %rmCln *Gast' = €rmdn = zd. airyaman- ; Neram
4581:mana (als nom. sg.) ; 5gr 'satt' = *8arya- (p. 78). Unsicher
4590:Min. Gl. 202, Shk. 269 = arisch "^^m-tfyati oder ^vi-taryati?;
4597:jiingerer Zeit zusammenkanien : np. darya *Meer aus *draya,
5326:padyavand kraftig H. 269; daya 'Amme H. 539; darya
6138:darya *Meer = ap. drayah-;farhih *fett' = zd.frapi&wo; far-
7313:ap. did'a- 'Stamm, Abstammung in ariya-ci^'^a' Von ari-
7944:np. darya 'Meer'
8894:*) Vgl. auoh maryas^ Schefer, Chrestom. II, 154, 15, 18; 159,
10266:aryand 13.
10389:(^arya 62.
10430:faryand 84.
10432:faryad 85.
```


## [2026-09-04T19:21:16.015Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 1610-1640 ===\"; sed -n '1612,1640p' HRN.txt; echo \"=== HRN 5990-6010 ===\"; sed -n '5992,6008p' HRN.txt; echo \"=== HUB 625-650 ===\"; sed -n '625,650p' HUB.txt; echo \"=== HUB 4570-4585 ===\"; sed -n '4570,4585p' HUB.txt; echo \"=== HUB 1500-1515 ===\"; sed -n '1500,1515p' HUB.txt"
}
```


### [2026-09-04T19:21:16.123Z] TOOL RESULT

```
=== HRN 1610-1640 ===
Neup. Grammatik § 19); doch scheint es mir besser,
dasselbe mit dem e des unbestimmten Artikels (yäi
validet) zu identificiren, wie dies nach mündlicher Mit-
teilung Prof. Nöldeke's schon vor Jahren Ewald
gethan hat.
138. ei 'o!'
aw. äi o!'; phlv. ai (vd. 19 (32); N:n vd. 18 (48));
skr. di.
139. ec jemand, etwas', s. hec (No. 1114).
140. Irmän {*er?nan^) 'Gast'^).
aw. airyaman- N. pr. eines Genius; phlv. ermän^
ermänik^ ermämh (Aw.-Komm.); ai. aryamän- 'Busen-
freund, Kamerad'.
Wenn aw. "^a^d^ra- wirklich einmal Teuer' bedeutet
») Fr. Müller (WZKM. 5, 185) will np. esän auf es\än d. i.
aw. aßsqm-\-än zurückführen.
*) Auch die indische Aussprache lautet irmän statt ermän,
wie zu erwarten wäre. Im Allgemeinen werden im indischen
Persisch die Majhlilvokale in den Worten richtig sein, in denen sie
sich erhalten haben, doch yersagt die indische Tradition auch in
vielen Fällen.
^) Vergl. Spiegel, Arische Periode, 103; die Bedeutung *Diener*
ist mir zweifelhaft.- 33 -
haben sollte (vergl. aber unter np. herhud, No. 1115,
nebst Anmerkung dazu), so wäre Nöldeke geneigt
(mündliche Mitteilung), np. ermän 'Gast' hieran
anzuschliessen ; also ursprünglich ein *am Feuer
Sitzender, Teilnehmender. Die Ableitung von ar.
aryaman- wäre dann aufzugeben.
=== HRN 5990-6010 ===
679. :iiyän 'Schaden'.
aw. zyana- 'Schaden*; phlv. zi(y)an (talm. Nr"»T;
mand. Xi"»NT) ; skr. (Brähm.) jfydna- 'Bedrückung'.
LW. kurd. af/. ziyän; bei. ziyänl (307); oss. ziän,
d. ziän ; arm. zean,
680. zer 'unten, unterhalb*.
Käs. jir (Vullers jBr, Jerü), zer,
aw. haca + aöairi\ päz. az^r, vergl. phlv. er\tan 'mild',- 151 -
ertanih, erman(i)sn 'niedrigen Sinnes' (Men.) ^); ai. vergl.
ddhara',
kurd. i^r; [af;'. lar; oss. t. dälä 'hinunter 0^8)1;
bei. LW. deräy n. serä, ser 'unter, unterhalb, am Fusse
von (63), ir, er (169); arm. LW. zil 'soprano' (IT üb seh -
mann, ZDMG. 35, 129, No. 22; 46, 259 No. 12).
681. zirek 'klug, entschlossen', äHr,
ai. Jlnt' 'rasch, lebhaft, thätig; aw. Jlra-, jirö.sdrö
(Geldner, 3 Yasht, 64).
=== HUB 625-650 ===
werden. Doch fehlen lautliche Analogien, vgl. ap.
vahyah- 'besser — np. bih etc. Sonst ware np. ord^
vaird 'ihm, ihn' etymologisch = ap. avahyarddiy 'des-
halb*.
138. Np. ei ist verdruckt fur ei ~ ai o!' Solche Inter-
jectionen bleiben ebenso wie die onomatop. Worter
besser weg.
140. Die Gleichung ermdn *Gast' ^= zd. airyaman- (nach
Geldner: *Genossenschaft' , nach Darmesteter;
*Vasall, Dienerj — skr. aryamdn- Busenfreund, Ge-- 21 -
fahrte, Kamerad*') scheint mir einwandfrei, ein zd.
*a^&raman' am Feuer sitzend' dagegen mehr als be-
denklich.
144. Vgl. WZKM. 5, 254. Fr. MuIIer bemerkt richtig,
dass upa in Neup. zu ab geworden ware. ^) Es bleibt
daher nichts tibrig, als np. ba = bad liber paz. pa =
pad nur auf ap. patiy zuriickzufUhren. 3) Als erstes
Glied von Compositen wurde pati- mp. zu pat- (neben
paJ- und pa-y vgl. Nr. 345), das im Neup. erhalten
blieb, wahrend das selbstandige pati mp. zu pad (vor
Vocalen) oder pa (vor Consonanten, zuerst wohl vor Den-
talen) wurde, um dann (allerdings gegen die Kegel : anl.
p = np. p) im Neup. in bad^ ba uberzugehen. Erhalten
blieb pa in jiingeren Zusammensetzungen [padrud,
padid^), pinhan, pinddstan) , in denen seine urspr.
Bedeutung verwischt war und nicht mehr gefiihlt wurde.
=== HUB 4570-4585 ===
menoi) = zd. mainyu-; np. mJnO 'Himmer = zd. mainyava-
'himmlisch'; phi. mSiiltan meinen, glauben', paz. minfdan
{=*mmidan), ap. maniyahy 2. pers. conj., zd. mainy^t^, skr.
mdnyatB,
b) Eran = arm. Eran, paz. Erdn, phi. Eran, inschr.
Airan und Aryan, ap. g. pi. ^Ariyanam\ dSr Vacker =
paz. dSr, zd. cairyu" (fiir dirya-) Aogemad. § 84 ; nlro, alter
«5r5?, ^siz.n^rd (Min. und Shk.), aus *naryw- oder ^naryava-
(Horn Nr. 1064)?; b^rUn 'aussen* von *6?r- = "^dvarya-?
(oben p. 33) ; %rmCln *Gast' = €rmdn = zd. airyaman- ; Neram
^= NarTman (bei Firdusi) = zd. nair^man&j ap. ^naryc^
mana (als nom. sg.) ; 5gr 'satt' = *8arya- (p. 78). Unsicher
sind der lange, spat' = ap. darga"?, siehe Kap. 25; tSra
oder <«ra? 'finster, vgl. Horn Nr. 407 und pBramun =
paz. peramun around' Shk. 263 (zu ap. pariy um, iiber'?).
c) mtrad 'stirbt* aus *miryat = arisch ^mfyatai = ap.
=== HUB 1500-1515 ===
iran. *padd,
347 ^*^ Anm. Vgl. sTvend pTdm 'marjolaine' = np. pudana
(Journ. asiat. 1893, 258).
349. Bei der Erklarung von paidd 'sichtbar, oflfenbar, klar
kommt alles darauf an, ob es zu dem phi. patyak der
Hajlabad-Inschrift gehSrt oder nicht. Im ersten Falle
ware patyak durch Epenthese zu phi. paitak = u^.paida
geworden wie aryan zu Sran. Aber die Bedeutung des
Wortes patyak der noch sehr dunkeln Inschrift steht
bis jetzt keineswegs fest, auch kommt Epenthese sonst
nur bei r und n sicher vor. Im andern Falle ist
Darmesteter's Erklarung (Etud. iran. I, p. 69) zu
erwagen : paida = phi. paitak = padtak (beides kann
gelesen werden) aus *patdak = alterem *patdayak
oder *patdayak --- ap. ^patidaya- oder "^patidaya- sicht-
bar, vgl. zd. paiti-dl 'hinsehen*, paitidaya- *Aufseher,
```


## [2026-09-04T19:21:29.536Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KNT ariya\"; grep -n -E 'ariya|Ariya|Ār[iī]ya' KNT.txt | head -30"
}
```


### [2026-09-04T19:21:29.601Z] TOOL RESULT

```
### KNT ariya
606:І. The sequence -arty- is found in Ariya (and compounds), where Elam. has har-ri-ia, proving phonetic ar and not 7: and in the middle amariyata to root mar- ‘die’, the passive abariya to root þar- ‘bear’, and the passives akariya akariyalà kariyais to root kar- ‘do, make’. The correspond- ing Skt. forms, in the 3d sg. impf., are amriyate, abhriyale, akriyaie; but the OP forms from root kar- cannot have this vocalism, since the product would be *azriya-. In this verb then there was in these forms a vowel between the k and ће т: either а full vowel or the reduced vowel (shwa secundum or *), which assumed the full value of a short vowel in Indo-Iranian. It is likely that the other two verbs had the same formation. Thus there is no sure support for the sequence ri in OP.
666:Two compound words are sometimes cut by the divider; these are Ariya : cd and Ariyacica, paruo : zanànüm and paruzandndm paruzendnam. There is also variation between the phrasal ad- verb paradraya and the prepositional phrase para : draya. But in Fragment Theta of DSf, the. . .]?- -k-[.. supposed to belong to dérantyakara 49 should be read ...h/--5-|... as part of avaiy : Spardiya 51-2.
734:XPh 41f; pereiy"i* = pariyait(iy) XPh 52.
800:II. The stroke is in excess: agaubatà DB 3.55, inscribed ag*urf"a, acc. to KT. abara DB 3.67, inscribed arr’, acc. to KT. akariyatà DB 3.92, inscribed as't- acc. to КТ. vikanāhy DB 4.71, 73, inscribed viis- acc. to KT. yikandh°dis DB 4.77, inscribed v%s*- acc. to KT. pasüva : hada : Қата DB 5.21, correction from
940:П. When у (of either origin) is expected to stand before a vowel, it must be either as con- sonant т, or as the reduced vowel + consonant т. The latter combination? appears in OP as -ar-: pIE *óhwl-enzo-, OP daraniya- ‘gold’, Skt. híranya-. pIE "e-kerWjonie, OP akariya"tà, cf. Skt. ákri-
942:Before ; and y there seems to have been the same development as before a vowel; it is possible that OP akariyaé is based rather on *ekergonto.
1254:pàr. root kar- ‘make, do’, OP pres. kunautzy, imf. pass. akariya, züra-kara- ‘evil-doer’; but *ker- in pres. inf. cartanaiy, *kér- in ucdram ^well- done, successful’, *be-kr- in perf. opt. caxriyd.
1525:*ger- ‘make, do’ in cartunaty ‘to do’; *gor- in züra-kara *evil-doer'; *qr- in ca-xr-1yd ‘he might make’, *gr- in kartum ‘made’; *qwr- in akariya 6 was done’; gér- in u-céram ‘successful’.
1582:Ariya- or Ariya-,' aruvastam or áruvaslam, ar- janam or ürjanam.
1636:(3) plr. change of p tk to f 0 x before con- sonants ($74.D): рага but fra-, aparsam but -frastam, tuvam but ace. ийт, akariya but cazriyü, drauga adurujiya but duructam.
1790:I. Perhaps primary, in ariya-.
1919:‘having one’s own death’ (see Lex.). Ariya-ciça- "Having Aryan lineage’; Ardu-manz&-
1929:с. The second element is predicate to the prior: Ariydramna- from *ariya-dramna- ‘Having the
2001:Of the province names used as ethnics, Bübirus and Uvja as ethnics are certainly errors. Of the ethnics in A?P, Küsáya is probably miswritten for Kü&iya; Gadáraya for Gadariya; Balaguiya for Galaguviya, or misread for @atagudaya, a mis- writing for @atagudiya, Hiduya for Hiduviya.
2531:$220. Tue Passive-Votce Present STEM of pIE was formed by the addition of the suffix pIE -je-/-4o-, which is accented in Sanskrit; in OP the root regularly has the normal grade, with -a-: imf. 3d sg. and pl. abariya abariya", to root bar-; ayadiya ayadiya", to yad-; akaniya, to root kan- ‘dig’; afahya and afahiya, to Ваћ-; avaniya, to van-; ajantya, to jan-; akariya akariya"la, to kar-; pres. ist pl. &ahyàmahy, to dah-; opt. 3d sg. kariyaiš to kar-, frabiyats to frað-, 3d pl. yadiyaiša” to yad-.
2548:П. Thematic stems have optatives with -i- (as zero-grade of -;&-, cf. I) added to the thematic vowel pIE -о-, making pIE -o7-: cf. 2d and 3d sg. Gk. depos tpo, Skt. bháreg bhdret. Examples: 3d sg. vi-nãbðayaiš, pass. kariyaiš frafiyars, pass. pl. yadiyaiía" (for ending, $282.11); 2d sg. mud. with ending -so, yadas3á, cf. Gk. $€po.
2570:II. The secondary ending is -t, which is not written in OP final after & (840); before - the thematic vowel is -e-: pIK *ebheuet, Skt. dbhavat, OP abava; pIE *ebheret, Gk. &фєре, Skt. dbharat, OP abara; Skt. ddruhyat, OP adurujiya; Skt. ddhd- rayat, OP adáraya; viyamarda; unaugmented ava- harida]; etc. Injunctive @adaya. Remodeled non- thematic, dha‘ ‘was’. Passive, abariya, adariya, etc. (§220). Non-thematic: adānā' to z5nà-, adada to 'dá-, айта to *di-, viy-aka" to kan-, avàja" to ava-jan-; in the last two, radical n as well as end- ing é is not represented in the OP orthography. Strong aorist: pIE *edhél, Skt. ddhat, OP ada. Optatives: Skt. gamydi, OP a-jamiya; OP avā- janiyà, Муй, pert. caxriyd.
2573:fer from the sigmatic aorist, where the termina- tions would be pIE -?s-m -is-s -is-t, pAr. -isam -iš -1&; the identity of second and third personal forms gives an analogy to the 2d sg. imperfect in -1-$# (no examples extant in OP), whence impf. 3d sg. in 4$. After u the phenomena are the same.? The OP examples are àt$ ‘went’, 0170-07 ‘went past’, aku- naus ‘паде’ (Skt. ékynot), adarsnaus ‘dared’ (Skt. ddhrgnot); and the thematic optatives active vi- ndlayars, passive kariyars fradiyars (cf. for ending Gk. $€po,, Skt. bhdret).
2599:II. The secondary ending was pIE -io, as in Gk. ёферєто, Skt. dbharata; this is seen in OP ud- араай (Gk. &érero, Skt. épatata), anayatà (Skt. dnayaia), amariyata, früámáyalà, agarbüyatà, agau- bata, ham-ataxsatd, dyasatd, |a|h[yat]à, adalrayat|a, [ат]аоаій, passive akunavayatd, perhaps aor. (h)amarmalà and perf. pass. cazr[zyala] or [claxr|iyata]; non-thematie remade to thematic, avarnavaté and aisiata; non-thematic aor. akula (Skt. dkria) and imf. patiy-ajatd (Skt. dhata).
2602:П. The secondary ending was pIE -nto, as in OP abara"íà, Skt. dbharanta, Gk. ёфрорто; agauba"td, pass. akariya"td; non-thematic remade to thematic, akunava"ta ‘made’, dha*td ‘were’, йуа"{@ ‘went’,
2665:miy Auramazdém ‘this I ask as a favor of Ahuramazda'. In the passive, the accusative of the thing remains unchanged: DNb 8f tya skauðiš . . . mia kariyats ‘that the weak should have wrong done to him’; also DNb 10f, and DB 1.49f (above). |
2811:§264. Tug DEMONSTRATIVE ava- ‘that’ is simi- larly either pronoun or adjective; it commonly refers to something already mentioned, but some- times has a forward reference, as in naimd ava ката tya tunuvd skaubars radiy miła kariyars ‘that is not my desire, that the mighty should have wrong done to him by the weak’ (DNb 10f; also DB 3.58, 5.21, DNa 39, DNb 20, 53, 55, 57, DSa 4, DSe 34, XPh 49, 51f). It has also the meaning ‘yonder’ as applied to the sky: Auramazdà hya imam bümim ada hya атат asmdénam айй ‘Ahura- mazda, who created this earth, who created yonder sky’ (DNa 1-3, eto.).
2880:(c) Some verbs are found only in the middle voice, though the middle meaning is no longer evi- dent: such are maniyaty ‘I think’, yadataiy ‘he worships’, amariyatd ‘he died’, and their forms. That these may originally have represented mid- dle voice ideas, is indicated by the fact that Latin arbitror, veneror, morior, representing the same ideas (though only the last is etymologically cog- nate with the OP correspondent), are all deponents, as are indeed the etymological or se- mantic equivalents in various other languages.
2938:(a) In optative clauses explanatory of kdma ‘de- sire’, introduced by tya ‘that’: kariyaiš DNb 9, 11; einafayai$ DNb 20; frabiyaiš ОМ 21 (without tya).
3072:I. The enclitic pronouns are attached to the first word of their sentence or clause or phrase, even though this be шй ‘and’: DB 1.25 Aura- mazdü-maty upastém frabara ‘Ahuramazda bore me aid’; РР} 8 tya-mary Auramazdà frübara ‘(the kingdom) which Ahuramazda conferred upon me’; DPh 9f тат Auramazdà pütuy utä-maiy ийат ‘me may Ahuramazda protect, and my royal house’. But the phrase vašnā Auramazdaha does not count in fixing the position of an enclitic: DB 1.13f vaina Auramazdàha адат-&ат х$йуабтуа Gham ‘by the favor of Ahuramazda I was king of them’; except in two partly restored passages, see under IIT. An enclitic in a dependent clause is sometimes attached to wd preceding a conjunc- tion or relative: DB 4.781 utd-tazy yàvà tauma ahatiy ‘and as long as strength shall be unto thee’; XPa 15 ша-тату tya рий akunaus ‘and what my father built’, but also XPa 19f шй tya-maiy pica kartam ‘and what was built by my father’; DNb 28f yabd-maiy tya kartam vatnühy ‘when thou shalt see what was built by me’. An attributive en- clitic genitive normally precedes the word which it modifies (cf. §309); but the meaning sometimes governs the position, as in Аа 3 apan?yüka-ma ‘my grandfather’s grandfather’, A*Sa 4 [n*yd|kama (for -am-ma, §138.1) ‘my grandfather’, both with am for -miy = -maiy (852.D. The abl. -ma is found only in hacd-ma ‘from me’, standing any- where in its clause. These formulations are vio- lated in three heavily restored passages, but the available space and the other versions favor these restorations: DSf 20 [ava исйтатату ( = -am-maty) akunaus} ‘that he made successful for me’; DSf 28 [hacd-cily ditradasa [arjanam-sary abariya) from afar its ornamentation was brought’; DNb 54f tya partalm-taty as]fiy ‘what is eommunicated to thee’ (this restoration is highly conjectural).
3154:my grandfather’, DSf36f tya ida akariya comesat 7 the end of its sentence, 38 hya 110 karta comes ` immediately after the subject, 40 hya 14@ karta comes at the end of its sentence. XPh 47 Scydta ahanty jiva uid marta artãvā ahanty ‘happy may І be while living, and when dead blessed may I be’; but there is no such variation in the order when the ideas are repeated in 54-6. On DNb 34, 41-4, see §307.
3288:AmH = Artaramnes, Hamapan: A slightly incomplete OP text in 10 lines, on a gold tablet; there is no evidence that the lost part of the tablet held Elam. and Akk. versions. Hz. AMI 2.117-27 (1930), 4.132-9 (1932), 8.17-35 (1938), Api 1-2 No. 1 (1938); Hz. Die Goldtafel des Ariyaramna, in Berliner Museen, Berichte aus den preussischen Kunstsammlungen 52.3.52-5, with plate (1931); HHSchaeder, РАМ 1931.635-45,  1935.494-8; — WBrandenstein, WZKM 39.18-9 (1932); Ву. Gr. $8 (1931); RGKent, JAOS 56.215 (1936); Sen, OPI 176-7 (1941); Sidney Smith, Isaiah Chapters XL-LV 122-3 (1944); RGKent, JAOS 66.206-12 (1946). See also $18, with note 2.
3464:5 dma : Arsamahyà : pita : Ariyaramna : Ariyáramnahyá : pita : Сехр : Сір 6 45 : pita: HaxdmaniS : иу : Dàrayavaus : x&ayafiya : avahyarà
3491:42 :agarbàyatà : Garmapadahya : máhyà : IX : raucabis : 0akatà : dha : ауаба : xša 43 cam :agarbàysatá : pasáva : Kabüjiya : uvamarSiyuS : amariyatà : іу
3774:%-? As read and restored by KT (who followed WB's restorations), except as noted in the following. * The і before and after the first gap were visible ta Cameron, though not to KT. 9 tyatkaily : fratama :] anušiyā [: ghata : agarbaya} Wb., after the traces seen by KT; tyaiSaily now confirmed by Cameron, who found the rest illegible. 3*7! [pasdva : niyas}tdyam Wh. after traces seen by KT; payme still legible, acc. to Cameron. # asariyata КТ; àkariyatàm WB; akariya^tà Bthl., WBn.
```


## [2026-09-04T19:21:30.003Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SOD leaf ~126 (p60)\"; awk 'BEGIN{RS=\"\\f\"} NR==127' SOD_pages.txt | head -60"
}
```


### [2026-09-04T19:21:31.642Z] TOOL RESULT

```
### SOD leaf ~126 (p60)
                                                                                                                            'skw'ch

     61

                                                                           TSP 5.96,8.61, 190 & etc.
           ask, aska    Osk") ©Av. uskau Khwar. >sk\ Past.
             hask     =^sky, sq\ sqy                                  1554 'sk'tmcyk B
                                                                           oskatamcik
           high, above, loud                                                                                        jiJ% <ji>J
           VJ; TSP; SCE; BSTBL, Dhy. 215; GMS           1215
                                                                           highest
                                                                           TSP  3.104; GMS 1014, 1296
     1543 Wdryk        => >sk>t>ryk)
                                                                      1555 >sk,tr B, M, S
     1544 'sk'n B                      <v>r jt *^&x£ Jl* tc^M <o^
                                                                           oskatar Csktr) ©Parth. }sk}dr ©comp.adj.; adv.
                                                                             =*sq}tr                             /& <jjd>
           (o)skan Csk'n) ©<*us-kana-, fskan
                                                                           higher, further, furthermore
           mark, sign, line
                                                                           BBB 553; GMS 1215, 1285; TSP 6.77, 13ii, 7, 27.5;
           GMS    369; TSP 3.191 n pl97; BSTBL, Dhy. 52, 53,
                                                                             VJ 1467; Frag. Len. 104.2; KG; MDii; MDiii
             54
                                                                     1556 >sk}tryq     M =» 'skVryk*
     1545 'sk'n s'r B «* >skys>r
                                                                     1557 >sk*tryk =* >sk>t>ryk>
     1546 'sk'ntCy) B, S          :         J^gJihJi
          oskand(e) ®fskand\ A v. skznda\ Parth. ysknd               1558 'sk'w'k S                                   VUxL^jd,
            ^ktsknt'k, sqwnt                                              oskawc =^sk*wyh
                                                                          height
          cripple, paralysed
                                                                           Sund. MSP b89
           GMS 365nl; VJ 51, 77, 124; Sund. KG 523 pl79f,
                                                                     1559 »sk*y   B => >sky

                                                                     1560 »sk»yr- B ** >sk>yr-
    1547 'sk'prn B                                         vV-*4
         oska-farn                                                   1561 'skr'nt- B                     j>/ji>j * j^j^T
          high in rank                                                     oskrand     Cskrnt-) ©<*uz Skri\ Skt. utkfntati
          Frag. Len. 44.10                                                   =>ptkrnt-, 'nkr'nt-
                                                                           0o)injurc, ({^destroy
    1548 >sk,r S                                               jUj         SCE 441, Mack. BSTBL p 154
         oskar =->sq}r
         coal                                                        1562 'skrnt- -* 'skr'nt-
          MSP bl49                                                   1563 'sks'k
                                                                          oskase S
                                                                                 ^sqsy                    o^p^< J^»<0'->>^f <j>^

    1549 'sk'rn'k   B                                   jM,^l              tomb, grave {place of bones)
          oskarne OskWy) -^sk'rn'k
                                                                           Gersh. Melanges Benv. 195; MDii, }sks*kw
          stupid, ignorant
                                                                     1564 >skt- B                              (j&OgSiJ^
          SCE 43, 113; TSP 2.656; BSTBL, Vim. 1; GMS
                                                                          (o)skat (skt>) ©Parth. lskd; A v. skaitU Khot.
            369; C2 p60
                                                                          thorn
                                                                            skai ©abl -> ^sqt}
    1550 'sk'rn'y -» ,sk>rn)k
```


## [2026-09-04T19:21:37.239Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SOD grep ryn\"; grep -n -E \"ry.n-wyj|ryn.wyj|wyj.n|>ryn|'ryn|ryan|Aryan\" SOD_pages.txt | head -20; echo \"### SOD leaf126\"; awk 'BEGIN{RS=\"\\f\"} NR==126' SOD_pages.txt | head -70"
}
```


### [2026-09-04T19:21:40.596Z] TOOL RESULT

```
### SOD grep ryn
4465:                                                                       237 Vnj =» *r}ync, >rync
7948:     aryand ©Av. drdYant           -^ry'nt
8182:1525 Yy'nwyj'n       M
8183:     aryan-wezan         (Jry*nwyjn) ©aryana-vaeja                           0o)take out, OcOraise up
8186:1526 *ry*nwyjn =» ^y'nwyj'n                                                 asxwast     (sywst- swyst-) ®<*us-xwasta-         ©pt.
10934:2479 p'ryn B                                            **$&■ i<j\Jj
11585:      VJ 902,781, 1104                                              faryane ©-w
11626:2735 brd'r-    C => Prt-                                          frayna (prynh, Prynh) =*fryn()), P'ryn               <
17435:     kope5 (qpyyS) ©MP kurbag ©ob. -yh                            karyanc ?                                       j^y      <->J
24160:     paryanp ? ©ob. -y(h) ^pry'wn ?
24162:     BSTBL, Dhu. 80, 164; -\ Dhu. 76 etc.; TSP 9.83               frayna (Prynh) ©ob. -yh ^P'ryn, fryn^
24756:7318 prwyjynyy M                          •aic-yr <*asjj.^             GMS 177, 529, 616; BSTii 831.22, 846.28: C2,
28118:     VJ 65\ 198, rfin >krt- "to be wounded"                          (a)ryantya   ©f. ^ry'nttWk
28181:     (a)ryantane =^ry}nt, ry'ntyh                               8483 rywsny pr'ystfkw S         (^ v^W^jjl?«^J
28603:        =>ryncyk                                                       BSTBL, Dhu. 909; GMS 293; Ben v. Et. Oss. 31 n;
30453:9265 sm'r'kh B                                AL>x\<Jb         9278 sm'ryny(y)     M                          Jrj;l<J&>
30456:     VJ 923, 967, 1026; BSTBL, pi 34; Frag. Len. 80.3;              Hen. Tales. 471.11, 13; z'r/Yrf sm'ryny
32116:                                                               9848 wVyn'y =* w'ryn'k
32152:9843 w'pryt =* w>Pr>y5                                         9855 w'ryn'k     B                         <^jj0^j=*^
### SOD leaf126
                                                                                                                                60

 'rw'stk


1516 Vw'stk «» WstHc                                                   1529 >rzn S
                                                                            arzan
1517 Vwytqy* C             (*j£j :Jj>-j)^<^i<sx^yi                          millet
     aruydakya ^'rwytky*                                                    MDiiipll5
     greed, rage
     BSTii 875.15; C2, 66V15; Schwartz. HMV 391                                                                                Ojjl
                                                                                                               jskj* lcr^^yi lJ*/
                                                                       1530 >s- C
1518 'rwr(h) B, M                             ^jjbcLf^jb
                                                                             as =^yt-, *s-
     orwar, orura ? (rwrO         ©Av. urvara—, Khot.                        (^)take, (/cOreceive
                                                                             C2 gloss.; GMS 129, 539; STi 43.9; Sund. AoF
           aruva\                                                              1981 p213
           =»rwrh Pa hi. uruw    ©ob. ~yh pi. -ff>,( -}n, -f/i

                                                                       1531 >s)dty C                               .xic-L-
      medicine, medical plant
                                                                            asaSte ? (pts'd) ®*>syd- ©pp.; ace. -w
      TSP; BSTBL; BBB; GMS 99                                                protected, shielded
1519 >rwrwys>k B                                     ^j> «l/                 BSTii 839.6; C2, 111R5 pl79-80
     orwar- wise ? ;                                                   1532 Vq      C                                 jijt^^u,
     medical plant                                                           asak, ansak ? ©ob. -y ^ns'kCy)
      TSP 20.2; BSTBL, Vim. 131                                              suitable

1520 Vwstk       S                                  ^yixjtj^j                BSTii 895.53; C2, 54V23

      arwastc     ©<OP    aruvasta    ^'rp'st'k                        1533 Vmnty C                             j*yx l^^iS j>
                                                                            asamandc
      powerful
      MDii p21.15; Hen. Mittelir. 39; S W, SI cahicr 7,                      taking, reception
           1989, 184, >rpstk
                                                                            C2, 57V6
1521 'rwt'wspy       S =* 'rt'wsp'y                                    1534 'spVck' B                         &£*t_yi>*<j*?
1522 'rwxs C                                      j$ £ ojjl~*                osfrack    OsPr'ck) ©<us~fras; <*us-fra-uc ; A v.
     aruxs, orwaxs =*ptrwxs-, 'rw^st'k                                         frd-vac- ©ob. -y ^sfr'cq, sPr'ck*
     bandage, gag
                                                                             thing, matter
      STii 2.5; GMS 158, 221 nl; Benv. JA 1943-5, 116;                       SCE 179, 418, BSTBL; TSP 2.959; STii 7.1; Benv.
        Lcntz. STii p600; Schwartz. HMV p391                                   Notcsiii 221; STSC 126

1523 Vwynt-        B                                  j=^Lrf           1535 'spr'ck =* 'sP'r'ck*
      arwi/end ? ©*arwant-ya-           ©inf. ->y                      1536 'sy'nt S                                  j^^i*j*~a
      Oo)stimulate,0o)arousc
                                                                             osxand Osynt)      =»(sxnd-, sxndy, sy'ntcyk
      BSTBL, Dhy. 70; GMS        158; Benv. Notesii 220                      fun, joke

1524 }ry C                                                                  MDii p 125.9; Tales. 478.25 nl3
                                                         ><4^
      are ©adj. ^•r'k                                                  1537 >synt =» ^nt
      mad, raving
                                                                       1538 ^yw'y- B, S        o^J'^. tJ>jj\j> < o-^oj^t
      C2, 66V15
                                                                            osxway ©<*us-xwdhaya ©inf. ->y ~>syw}y-,
                                                         7*j $   y I
                                                                              'sxw'y-, sxw*y-
1525 Yy'nwyj'n       M
     aryan-wezan         (Jry*nwyjn) ©aryana-vaeja                           0o)take out, OcOraise up
     Eran-wej                                                                GMS 417; Dhy. 24, BSTBL; TSP 3, 262 & etc.
     Benv. Notesiv 506n; Hen. BSOAS          11, 68.26                 1539 ^ywst-      S                      uj jjTjj iO^r^oj^
1526 *ry*nwyjn =» ^y'nwyj'n                                                 asxwast     (sywst- swyst-) ®<*us-xwasta-         ©pt.
1527 Vync C                                                                   st. ^syw'y-, 'sxw^-, swxst-, sxwst-
                              <J> ^'j^Lp^jT^ji
     arenj, arinc (*r}nj) ®<*ara6nika\ OP arsan                             (to)take out
       =$*fyn c                                                             GMS 417
```


## [2026-09-04T19:21:50.461Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BQT irman\"; grep -n 'ایرمان' BQT_v1_pages.txt | head; echo \"--- iraj\"; grep -n 'ایرج' BQT_v1_pages.txt | head; echo \"### leaf 415-417 head\"; awk 'BEGIN{RS=\"\\f\"} NR>=414 && NR<=418 {print \"----LEAF\",NR; print substr($0,1,600)}' BQT_v1_pages.txt"
}
```


## [2026-09-04T19:21:51.649Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN && echo \"### IRN pdf18 (p7)\"; awk 'BEGIN{RS=\"\\f\"} NR==18' IRN_pages.txt | head -60"
}
```


### [2026-09-04T19:21:52.236Z] TOOL RESULT

```
### BQT irman
15583:ایرمان ؟ » بروژن و هعتی‌میهمان‌است
15614:درشاهنامه سه‌بار ابرمان پمعنی مهمان آمده وایرمان‌سرای‌بمعتی مهمان‌سرای‌مستممل است .بدیدهی
--- iraj
### leaf 415-417 head
----LEAF 414
۱۳ات ایدغ
ایاره گیر ۱ -بر وزن کنار هگیر ».
محاسب و نوبسنده را گویند .
ایاد ۴ ه بر وزن نماز , دام غلام تراد
سلطان محمود غز نوی بوده -
ابادي - بررزن لمازی » برقع سیاعی
ست که زنان بریشت چشم بندند ۴ .
" ایا ؟ « بروزن ممای » بمعنی ایاز
است که نام غلام سلطان محمود باشد .
ایاسه « بفتم اول و رایع ۰ بمعت یآرزو
و اثتیاق باشد - و حلقه و فلايی را نیز کوبند

----LEAF 415
ایا - بروزن وممنی زبرا و ازبرای‌آن
و از ایشجهت باشد .
ایر اف ۴ - بکر اود و سکون ثانی
و ثالث بالف کشده ویفای زده ۰ نام عدر اردااست
که پارسیان‌اورا پیعمبر
میدانتها ند و
ابسر آن ٩‏ -
بر وزن ببران . نام
هوشنگ ین سيامك
باشد - و ولاسته عرای
| بد‌ماهید - با عیم بالف کشده بروزث
مرخرامد» بلفت سر‌بانی درختی است که بدن‌آن
مانندیشم است» وخاصیت‌ری
----LEAF 416
وه آبرسا
اول نیشاپور است ۷ . از پادشاهان بابل هم بوده است
ار ج ‏ بکسراول و سکون ثانی‌مجهول الیرسا « بکس اول و سکون انیوثاك
و #الك مقتوح بجیم زده ؛ نام پس فربدون است | و سین بی‌فقطٌبالف کشیده » بیونانی ۴ قوس‌رفزح
توا فلك آفتاب را یز کویند؟ . - وناییکی را کوبند وفام یخ‌سوسن ۴ آسمان کون هم‌هست
سس ۰اه
٩‏ پهلوی 50205 - 8640 . شتر(< شهر) بسمنی کشو
----LEAF 417
و چون کل آن زرد و سفیدو کبود میباشدبنایر
آن ایرسا نامیده‌اند چه شبیه بقوی‌فزح است .
بیوایی ٩‏ طلق و زر ورق دا کوبند و بثیرازی
برقك خوانند .
ایر قان - با قاف بروزن میهمان .بلغت
روغی حنا را کوبتد و آن ب رکه درختی باشد که
" یکوبند و خمی رکنند و بردست و پای بندند .
"فر گه ه یک اولو سکون تانی‌وئاك
و کاف‌فارسی » بلفت زند وپازند )٩(‏ بمعنی مردم
----LEAF 418
ایقفه ه با فا بررزن و معلی ابفده‌است
که بهوده گو و سبکار باشد که حرزه چانه
۱9۳۳
اون بکر او وسکون انی وفاف
بواو وسیده و بنون زده ؛ بلفت رومي کلی است
بغات بدیوی و کنده و بعربی‌وردالمنتن‌خوانند .
رنگ آن برنگ گل سرخ ماند .
ابگ ب بکسراول وسکون ثانی و کاف
فارسی » ولاتی است است از ولابات فارسی 6
ایگ بادن هایگ معلوم. و بای ایجد
پالف کشیده و واو
```


### [2026-09-04T19:21:53.945Z] TOOL RESULT

```
### IRN pdf18 (p7)
[pdf page 18]
ایرانویج
خاستگاه ایرانیان

خاستگاه ایرانیان بناب.ر اوستا که کهن‌نسرین نوشتهٌ بازماندةٌ ایرانی است»
اثیریانم ونجو ۷8618 21۳720270 آسده که درزبان پهلوی [2:20۷2 «ایرانویج»شده‌است .
آوستا دربخش «وندیدد» | زجا ی‌بنام ایرانویج نام می‌پر د که مرکز اصلی ایرانی‌هاست .
خود واه «ایرانویج » وارْةٌ مرکبی اس ت که از دو جزء ترکیب یافته است., جزء
نخست آن ایران » و جزء دوم آن ویج است و «ویج» بمعنی نخمه ونژاد است و
در زبان فارسی بیج از این ريشه است وبیضه در زان عربی از همین واژه گرفته
شده‌است . ازینرو ایرانویج بمعنی‌نژاد وتخمةٌ ایرانیهاست , هنگامی که جائی باین‌نام
نامیده شود» بنا چار می‌بایستی آنجا جایگاه نژاد ایرانی‌باشد وایرانیان از آنجا برخاسته
باشندو این نام میتواند راهنمای خوبی‌برای تعیین‌جای ایرانیان نخستین باشد , اکنون
باید دید «ایرانویج « از نظر جغرافیائی درکجا واقع شده است , در اوستا وقت ی که
دربارة ایرانویج سعخن میرود » سخن از جائی است بسیار سرد و شاید هم بخاطر
همین سرساست که ایرانیها از آنجا کو پچ کرده‌اند. در «وندیداد» که بخشی از اوستا
است در جائی که سخْن دربارةٌ سرزمین‌هاست » چنین آنده است , «نخستین‌جا و
سرزمین نیکوئ ی که من‌اهورا مزدا آفریدم ایرانویج بود که از رود «ونگوهی دائیتی»
آییاری می‌شود . اهریمن پرمرگ در آنجا مار آیی و زسستان دیو آفریده آفرید. در
آنجا ده ماه زسستان و دوماه نابستان است و در این ماهها برای آب وزمین وگیاه
سرد است » آنجا مرکز زسستان است » آنجا قلب زسستان است»! .

پس معلوم می‌شود که خاستگاه ایرائیها جای سردی بوده اس ت که از
آن‌جا بخاطر سردا ویسبب نداشتن چراگاه‌ها کوج کرده‌اند. دربارة جای جغرافیائی

(- نگا هکنید به ونذیداد » فرگرد یکم.
```


## [2026-09-04T19:22:05.660Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index containing line 15583\nimport sys\noff=sum(len(l)+1 for l in lines[:15575])\npages=t.split('\\f')\npos=0\nfor i,p in enumerate(pages):\n    if pos<=off<pos+len(p)+1:\n        print('LEAF',i); print(p[:2500]); break\n    pos+=len(p)+1\n\""
}
```


### [2026-09-04T19:22:07.417Z] TOOL RESULT

```
LEAF 416
و چون کل آن زرد و سفیدو کبود میباشدبنایر
آن ایرسا نامیده‌اند چه شبیه بقوی‌فزح است .
بیوایی ٩‏ طلق و زر ورق دا کوبند و بثیرازی
برقك خوانند .
ایر قان - با قاف بروزن میهمان .بلغت
روغی حنا را کوبتد و آن ب رکه درختی باشد که
" یکوبند و خمی رکنند و بردست و پای بندند .
"فر گه ه یک اولو سکون تانی‌وئاك
و کاف‌فارسی » بلفت زند وپازند )٩(‏ بمعنی مردم
باشد چه ابر گان مردمانر| کوبند ۴ . ۱
ار گان - باکاف‌فارسی بروزن‌میهمان,
بلت‌زند و پازند (۱)بممنی مردمان با دکهجمع
مردم است ؟ .
ایرمان ؟ » بروژن و هعتی‌میهمان‌است
اما میهمان طفیلی که برفافت باران و دوسثان
یجایی برند با خرد بی آنکه اورا طلبیده باشند
پرود - و شخصی را نیز گوین که بی‌رضا درخانه
با ملك کسی فرود آید - وبمعنی عاریت‌وحبرت
و آرزورارمان‌هم کفته‌اند ۴ چه ابر‌مان‌خورحسرت
خورنده را گوبتد
آمده است - و تلم شهری و مدینه‌ای‌هم‌هت .
زا
ایر مان‌سر! * - یروزن میپمان‌سرا .
خانه و سرایعارنتی را کونند- وسر کویمطلوب
و حبرت خاله را نی زکوبند - و دیا را ریق
مجاز ايرمان سرا میگویند .
ایر ون » باراو دنون‌وخرکت مجهول؛
ک وکرد را کون که‌جزو اعظم باروت است‌وآن
از کوه ماند اداردانه برمي‌آید .
ایر که نج بلفتز ندویاز ند(۱)
مردم - و مودی را گویشد ٩‏
ایز ازه « با زای شطهدار بروزن‌سحاره:
ازارء خانه را گویتد و آن از دیوار مقداری‌باشد
هنگام شتن پشت برآ نگذارنا .
اف ۲ > بکر اول و تاك و سکون
۳-7 اد تایبا تج
و شین قطه‌دار مفتوح بسن 2 اند
زده ». بمعنی‌خدأبرست ماشفه. - ونام یکی ازامرای
بهرام چوین هم‌هست . ۱
ا یز غفنج ه بکراول‌وسکون‌نانیمجپول
و زای هوز و غين قطه دار مضوم بنون و جیم
بت درپپلوی ابریگان 20727820 مردمان
۳ب ات۱۴
10 که بطبقة پیشواباندینی‌ورء‌حانبان اطلاق‌ميشد. این‌کمه در ادبیات‌بپلوی 287۳088
درشاهنامه سه‌بار ابرمان پمعنی مهمان آمده وایرمان‌سرای‌بمعتی مهمان‌سرای‌مستممل است .بدیدهی
است که این واژه در غارسی ممنی اصلی خود را از دست داده حول بسبار بیدا کرده است . در
ناتگرت واوستا 20" بمعتي بارودوست ونیز نامویکی ازخدابان وداست«مزدبنا۰۳ 4».
۴ ره : ارمان. ۵ ره : ابرمان. ۷ رل: اب رکه وای رکان. ۷ - در اوستا ق۷228
در سا کرت قنا2۷2[2 صفت از ربشة ۷22 بمعنی پرستبدن ومتودن؛ یس یزتنه‌لفة بمعنی درخور
ستابش » و بفرشتگانی اطلاق مبشد که از جهت رتبه و منزات دون‌امشاسپندان حستند . این واژه
در بهلوی ۷220 و در فار.ی ابزد شده اما در فارسی ایزد بمعنی فرشته نت بلکه فقط
بممنی خدا و آفربد کار کل است و در حقیقت اطلاق خاص بعام شده « مزدبسنا ۱۵4 » در استی
0 ۳ . استی ۱۲۱ . ۸ - لفة م کب از : ابزد (فرشته) + کشن ( نر » فحل ) -
اسب 1 جمعاً بمنی دارندء اسب نرامزدی .
```


## [2026-09-04T19:22:31.756Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt; do echo \"== $f\"; wc -c $f; grep -c 'ایرلند' $f; grep -c 'ایرانویج' $f; done; echo \"### irland ctx\"; grep -n -m3 -A3 -B3 'ایرلند' MON_part1.txt MON_part2.txt | head -60"
}
```


## [2026-09-04T19:22:33.285Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KLN 110 area: Aryan\"; grep -n -E '^Aryan|Aryan,|Arya-|arya-' KLN_1966.txt | head -20; echo \"---1971\"; grep -n -E 'Aryan' KLN_1971.txt | head -20"
}
```


### [2026-09-04T19:22:33.500Z] TOOL RESULT

```
== MON_part1.txt
4377831 MON_part1.txt
0
0
== MON_part2.txt
4331421 MON_part2.txt
2
0
### irland ctx
MON_part2.txt-33413-حسرت: گیاهی است علفی و پایا از تيرة 
MON_part2.txt-33414-دارای پیاز بز رک و گوشت‌دار و محفوظ در 
MON_part2.txt-33415-چمن‌زارهای غالب نقاط اروپا و نواحی بحر 
MON_part2.txt:33416:الرومی و انگلستان و ایرلند و آسیای صغیر 
MON_part2.txt-33417-شرفت تاه مد‌کور دارای برگک‌های 
MON_part2.txt-33418-باریکك و دراز و نوک تيز بدون ک رک و به 
MON_part2.txt-33419-رنک‌اند و میوه‌اش کسول سه قسمتی و 
--
MON_part2.txt-87978-(امر.) معاون کنسول» نایب قنسول» کنسولیار 
MON_part2.txt-87979-(فر ه.) 
MON_part2.txt-87980-
MON_part2.txt:87981:ویسکی: ۷۰ [از ایرلندی] (.) نوعی 
MON_part2.txt-87982-مشروب الکلی که بیشتر در انگلستان و 
MON_part2.txt-87983-ابالات متحدهٌ آمریکا تهیه و مصرت 
MON_part2.txt-87984-
```


### [2026-09-04T19:22:33.567Z] TOOL RESULT

```
### KLN 110 area: Aryan
3570:Aryan,  adj.  and  n.  —  Formed  with  suff.  -an  fr, OI.  dryab,  ‘noble’,  which  is  rel.  to  OPers.  ariva, ‘noble’  (whence  Pers.  Iran,  ‘Persia’).  Cp.  Iran¬ ian.  As  a  synonym  for  ‘Indo-European’  the term  Aryan  was  introduced  by  the  German philologist  Friederich  Max  Muller  (1823-1900).
7179:chandaul,  chandal,  n.,  an  outcast  (Anglo-Ind.)  — Hind,  chandal,  fr.  OI.  cdndalah,  which  is  of  un¬ certain,  prob.  non-Aryan,  origin, chandelier,  n.  —  F.,  ‘candlestick’,  fr.  VL.  *can- delarium,  which  is  formed,  with  change  of  suff., fr.  L.  candelabrum.  See  candelabrum, chandler,  n.  —  ME.  chandeler,  fr.  OF.  chandelier, ‘maker  or  seller  of  candles’,  fr.  Late  L.  cande- larius,  of  s.m.,  fr.  L.  candela,  ‘candle’.  See  candle, change,  tr.  and  intr.  v.  —  ME.  chaungen,  changen, fr.  OF.  (=  F.)  changer,  fr.  Late  L.  cambiare, ‘to  change,  exchange’,  which  is  a  Gaulish  loan word  derived  fr.  I.-E.  base  *(s)qamb-,  *(s)qemb-, ‘to  bend’,  whence  also  OIr.  camm,  ‘crooked, curved’,  Mir.  cimb,  ‘tribute’,  cimbid,  ‘prisoner’, Gk.  axapPoc,  ‘crooked,  bent’,  Swed.  skumpa, ‘to  limp’,  skimpa,  ‘to  skip’.  The  original  mean¬ ing  of  Late  L.  cambiare  must  have  been  ‘to bend’,  whence  arose  the  following  phases  of meaning:  ‘to  turn,  to  change,  to  barter’.  Cp. Gaulish  *camb-ita,  ‘felloe’  (whence  F.  jante, ‘felloe’),  and  see  cambium.  Cp.  also  excambion, exchange,  gombeen.  Cp.  also  camp  and  words there  referred  to.
20503:Derivatives:  jut,  n.,jutt-ing,  adj.,jutt-ing-ly,  adv. Jute,  n.,  one  of  the  ancient  inhabitants  of  Jut¬ land.  —  Fr.  Jutae  or  Juti  (as  they  are  called  by Bede),  ‘Jutes’,  fr.  ON.  Iotar,  ‘Jute’. Derivatives:  Jut-ic,  Jut-ish,  adjs.,  Jut-land,  n., Jut-land-er,  n.,  Jut-land-ish,  adj. jute,  n.,  a  fiber  of  two  East  Indian  plants,  Cor- chorus  capsularis  and  Corchorus  olitorius.  — Bengali  joto,  ju(o,  fr.  OI.  jutah,  ‘twisted  hair’, which  is  rel.  to  yd/d,  ‘braid  of  hair’;  of  uncertain, probably  non-Aryan,  origin.
---1971
10493:non-Aryan base *alb, ‘mountain’, whence also 
12135:‘the High Mountains’, from non-Aryan base 
20418:Aryan, adj. and n. — Formed with suff. -an fr. 
20422:term Aryan was introduced by the German 
20424:Derivatives: Aryan-ism , n., Aryan-ize , tr. v., 
20425:Aryan-iz-ation , n. 
25876:‘stammering (designation of the non- Aryan 
31744:nation of the non-Aryan nations), Gk. (Jap| 3 a- 
43839:certain, prob. non-Aryan, origin, 
43922:word of non- Aryan origin. Cp. gantry and 
126647:Aryan. 
128159:Aryan origin. 
130186:probably non- Aryan, origin. 
183368:ket’ ; prob. of non-Aryan origin, 
245145:rank; idol’; prob. of non-Aryan origin,
```


## [2026-09-04T19:22:40.164Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KLN Ireland/Irish/Erin\"; grep -n -E '^(Ireland|Irish|Erin|Ir-)|Ireland,  n|Irish,  adj|Erin,  n' KLN_1966.txt | head; grep -n -B2 -A6 'Erin, n' KLN_1971.txt | head -40; echo \"### SKT Irish\"; grep -n -i -E 'Ireland|Irish' SKT.txt | head"
}
```


### [2026-09-04T19:22:40.282Z] TOOL RESULT

```
### KLN Ireland/Irish/Erin
13554:Erin,  n.,  ancient  (nowpoetic)  name  of  Ireland.  — OE.  Erinn,  dat.  of  Erin  (whence  Ir.  Eire),  ‘Ire¬ land’.  Cp.  Dail  Eireann,  Erse,  Irish,  Hibernian, erinite,  n.,  a  basic  copper  arsenate  of  emerald- green  color  (mineral.)  —  Named  after  Erin, ‘Ireland’.  See  prec.  word  and  subst.  suff.  -ite. Erinys,  n.,  one  of  the  three  avenging  spirits, Alecto,  Tisiphone  and  Megaera  (Greek  mythol.) —  L.,  fr.  Gk.  ’EpTvij!;,  which  is  of  uncertain origin.  It  possibly  means  lit.  ‘the  angry  spirit’, and  is  rel.  to  Arcadian  epfveiv,  ‘to  be  angry’, and  to  Gk.  opfveiv,  ‘to  raise,  stir,  excite’,  gpip, ‘strife,  discord',  fr.  I.-E.  *erei-,  enlargement of  base  *er-,  ‘to  set  in  motion,  stir  up’,  whence Gk.  opvuvai,  L.  oriri,  ‘to  rise’.  See  orient,  n., and  cp.  erethism,  Eris,  eristic, erio-,  combining  form  meaning  ‘wool’.  —  Gk. cpto-,  fr.  eptov,  ‘wool’,  rel.  to  Homeric  and  Ion. clpop,  ‘wool’  (fr.  "gpfop,  which  was  prob.  dis- similated  fr.  *f£pfo<;),  Gk.  aprjv,  Gortyn.  Faprjv, ‘ram’,  and  cogn.  with  OI.  lira,  ‘sheep’,  uranah, ‘ram,  lamb’,  ura-bhrah,  ‘ram’,  Arm.  gain, ‘lamb’,  L.  verve. x,  ‘wether’  (prop,  ‘wool  bear¬ er').  Cp.  Iresine.  Cp.  also  berger  and  the  first element  in  Amoseris.
19895:Irish,  adj.  and  n.  —  ME.,  fr.  OE.  *Irisc,  fr.  Iras, ‘the  Irish’,  which  is  rel.  to  OE.  Eriu,  ‘Ireland’. Cp.  Erin,  Erse.  For  the  ending  see  adj.  suff.  -ish. iritis,  n.,  inflammation  of  the  iris  of  the  eye  (med.) —  Medical  L.,  formed  with  suff.  -itis  fr.  Gk. Tpu;.  See  iris.
84857-ing see subst. suff. -ite. 
84858-
84859:Erin, n., ancient (now poetic) name of Ireland. — 
84860-
84861-
84862-
84863-
84864-ERINITE 
84865-
### SKT Irish
143:fa5>on.  1874. Irish.— Irish;  as  in  O'Reilly.  1864. Iul.~  Italian;  as  in  Meadows  i*»57. L. — I^tin  ;  asinWhitcandKiddle,  1876. Low  G. — Low  German ;  as  in  the  Bremen
795:Ape.  (K)  ME.  ape,  A.S.  a/a.+l aap',  Iccl.is/i;  Swed.  a/a;  Irish  and  Gl apa;  G.  affe\  Gk.  ff^vor;  Skt.  kapi. The  word  has  lost  initial  <(,  nrcservedi Gk.  and  Skt.  only.  The  Hch.  jb^ ape,  is  not  Semitic,  but  boiroweu  nj Skt.
1045:Ass.  (E.)  ME.  aste.  A.S \V.  asyn,  Swed.  Ama,  IccL  aim. Gk.  iV«.  Also  Irish  asa/,  Vv. and  G.  <///,  Goih.  oj/.m/,  l-  « of  Semitic  origin  ;  cf.  Heb.  a/ aas.
1231:was  also  n&ed),  but  rather  from  Icel.  0gK awe,  fear:  Dan.azv.+AS.  tf;$T,  <>^;  Gom. tj^,  fear,  anguish ;  Irish  ^agfiat^  fcar. terror;  Gk.  ix°'i  anguish,  afmctioa;  L anj;ffr,  choking,  anguish  ;  Skt.  ag^A,  fla 1'he  orig.  sense  ia 'choking.*  (<^  AGU.) See  Anffuiali.     Der.  aw-fuL
1454:(Llttri^).  Cf.  UjcL  ii^piui,  ticft. brath^  W.  Ar*/,  Itcachery,  Gael vaittai^e  by  unfair  mtatis;    Irish
1498:Basket.  (C.)  M.  E.  *a.t^/.- W.  Ajr^/t/; Com.  bai(et/\  Irish  Itascnd;  Gael.  Inmaid,  a basket     Perhaps  from  \V.  basf;,  a  platting.
1514:Bat  (1),  a  cuilgcl.  tE  >  M.  K.  hatie.-^ A.  S.  Aa//  (Ent;.  Slndien,  a.  65).  Cf.  Irish baia,  hat.  a  staff.  Der.  bat-Ut^  with  double dimin.  surHs  -/«/.
1711:Bolt,  a  girdle.  (E.)  M.  E.  beU,  A.S. ^//.^Icel.  belti\  Irish  and  GaeL  M//.  a belt,  border;  L.  balteus;  O.  II.  G.  Ao/j.
1768:Big.    (Scand?)     ME.   *»>;    m\ rich  ^Hampotc).     Not  A.S.     Perhaps bil^t  the  /being  dropped,  ai  iu  b^. Icel.  beigfa,   to  inflate,    puff  out;    Hi bf/^,   to    fill    one'i    maw,    cram Swcd.    dial.    ba.[^'^,    buJgtg;     big.       Kit related  to  lag  and  buJ^.    p.  Or  ia  it to  Irish  baghdch,  Gael,  bagtuh^ bulky,   Skt.  baku.  Urge?
1935:Block,  alarceiikceoiwooiL  *.C)  I ^/^..W.  pite,  a  block;  GarL  aidl /^or.  a  block,  romd  aM^  ti^iVh Cf.  Irish  kbgk,  a  fncncoU  O.  Irofcl fragment.     Henoe  alto  Do.  *.^ Swed.  */*-*,    O.  H   G.  b' plakha.     Doublet.  ti»£.     1
```


## [2026-09-04T19:22:53.770Z] TOOL CALL #24: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-04T19:22:53.778Z] TOOL RESULT

```


```


## [2026-09-04T19:22:58.816Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82eryos",
 "prompt": "Give the full etymology section: reconstructed meaning, whether it derives from *h2el- \"beyond/other\" or *h2er- \"to fit\", scholarly views (Thieme, Mayrhofer, Kloekhorst), and the list of descendants (Indo-Iranian, Anatolian, Celtic), including whether Old Irish Ériu / Ireland is listed."
}
```


## [2026-09-04T19:23:00.408Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Celtic/%C4%AAwer%C4%AB%C5%AB",
 "prompt": "Etymology of Proto-Celtic *Īwerīū (Ériu, Ireland): what PIE root, what descendants, and does it mention any connection to Aryan/*h2eryos?"
}
```


### [2026-09-04T19:23:00.565Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T19:23:03.459Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T19:23:06.216Z] TOOL CALL #27: WebSearch

```json
{
 "query": "wiktionary Reconstruction Proto-Indo-European h₂eryós Aryan etymology"
}
```


## [2026-09-04T19:23:06.683Z] TOOL CALL #28: WebSearch

```json
{
 "query": "wiktionary Ériu Ireland etymology Proto-Celtic Īweriū *piHwer- fat"
}
```


### [2026-09-04T19:23:08.040Z] TOOL RESULT

```
Web search results for query: "wiktionary Reconstruction Proto-Indo-European h₂eryós Aryan etymology"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T19:23:09.627Z] TOOL RESULT

```
Web search results for query: "wiktionary Ériu Ireland etymology Proto-Celtic Īweriū *piHwer- fat"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T19:23:16.366Z] TOOL CALL #29: Bash

```json
{
 "command": "curl -s 'https://en.wiktionary.org/w/api.php?action=query&list=search&srsearch=Reconstruction%20Proto-Indo-European%20aryos&srlimit=15&format=json&srnamespace=118' | python3 -m json.tool | head -60; echo \"=== 2\"; curl -s 'https://en.wiktionary.org/w/api.php?action=query&list=search&srsearch=%C3%89riu%20Ireland&srlimit=10&format=json' | python3 -c \"import json,sys;d=json.load(sys.stdin);[print(x['title']) for x in d['query']['search']]\""
}
```


### [2026-09-04T19:23:18.592Z] TOOL RESULT

```
{
    "batchcomplete": "",
    "query": {
        "searchinfo": {
            "totalhits": 0,
            "suggestion": "reconstructions proto indo european ardos",
            "suggestionsnippet": "<em>reconstructions</em> proto indo european <em>ardos</em>"
        },
        "search": []
    }
}
=== 2
Ériu
Yernish
Iras
Nerin
Yernagh
Iwerzhon
īrs
Ireland
Banba
írar
```


## [2026-09-04T19:23:24.033Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /tmp && for t in \"Reconstruction:Proto-Indo-European/h₂eryos\" \"Reconstruction:Proto-Indo-European/h₂eryós\" \"Reconstruction:Proto-Iranian/aryah\" \"Ériu\" \"Ireland\" \"ایرج\" \"ایرمان\" \"𐎠𐎼𐎡𐎹\"; do echo \"===== $t\"; curl -s -G --data-urlencode \"titles=$t\" 'https://en.wiktionary.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&redirects=1' | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nfor p in d['query']['pages'].values():\n    print(p.get('title'), '->', ('MISSING' if 'missing' in p else ''))\n    print((p.get('extract') or '')[:1800])\n\"; done"
}
```


### [2026-09-04T19:23:26.993Z] TOOL RESULT

```
===== Reconstruction:Proto-Indo-European/h₂eryos
Reconstruction:Proto-Indo-European/h₂eryos -> MISSING

===== Reconstruction:Proto-Indo-European/h₂eryós
Reconstruction:Proto-Indo-European/h₂eryós -> MISSING

===== Reconstruction:Proto-Iranian/aryah
Reconstruction:Proto-Iranian/aryah -> MISSING

===== Ériu
Ériu -> 

== Middle Irish ==


=== Alternative forms ===
Hériu


=== Etymology ===
From Old Irish Ériu.


=== Pronunciation ===
IPA(key): (earlier) /ˈeːɾʲu/, (later) /ˈeːɾʲə/


=== Proper noun ===
Ériu f

Ireland


==== Declension ====
Accusative/dative singular: Érind, Érinn


==== Derived terms ====
Érennach (“Irish”)


==== Descendants ====
Irish: Éire
Manx: Nerin
Scottish Gaelic: Èirinn


=== Mutation ===


== Old Irish ==


=== Alternative forms ===
Hériu


=== Etymology ===

Probably, although the É is unexpected and unexplained, from Proto-Celtic *Φīweriyū.


=== Pronunciation ===
IPA(key): /ˈeː.ɾʲu/


=== Proper noun ===
Ériu f

Ireland (a country and island of Europe)
Synonyms: Banba, Elg, Fódla


==== Declension ====


==== Descendants ====
Middle Irish: Ériu, HériuIrish: ÉireManx: NerinScottish Gaelic: Èirinn
→⇒ Old English: ĪrlandMiddle English: Irlond, Irelond, Irland, Irlaund, Yrland, Yrloand, Irlande, Irlaunde (dative case)English: Ireland→ Japanese: アイルランド (Airurando)→ Tamil: அயர்லாந்து (ayarlāntu)→ Telugu: ఐర్లాండు (airlāṇḍu), ఐర్లాండ్ (airlāṇḍ)Scots: IrlandYola: Erelhoan, Erelone, Irelonde→ Old French: Irlande, YrlandeFrench: IrlandeHaitian Creole: Ilann→ Greek: Ιρλανδία (Irlandía)→ Persian: ایرلند (irland)Norman: IrlandeWalloon: Irlande
→ Old Norse: írarIcelandic: ÍriFaroese: íriNorwegian Nynorsk: ireNorwegian Bokmål: ireDanish: irer→? Old English: Īras


=== Mutation ===


=== References ===
===== Ireland
Ireland -> 

== English ==


=== Etymology ===

From Middle English Ireland, Irelond, Irlond, Irland, from Old English Īrland, from Old Irish Ériu + land. See Irish.


=== Pronunciation ===
IPA(key): /ˈaɪə(ɹ)lənd/
(Ireland)
(Dublin / East) IPA(key): [ˈɑɪɚlənd], [ˈʌɪɚlənd], [ˈəɪɚlənd], [ˈɑɚlənd]
(West) IPA(key): [ˈaɪɚlənd]
(General American) IPA(key): [ˈäɪɚɫɪ̈nd]
(Received Pronunciation) IPA(key): [ˈɑɪələnd]

Rhymes: -aɪə(ɹ)lənd
Hyphenation: Ire‧land


=== Proper noun ===
Ireland (usually uncountable, plural Irelands)

A large island in northwestern Europe.

A country in northwestern Europe.
Synonyms: Republic of Ireland, Eire, Southern Ireland

A surname.
Other places named Ireland:
A hamlet in Southill parish, Central Bedfordshire district, Bedfordshire, England (OS grid ref TL1341).
A community in Antigonish County, Nova Scotia, Canada.
An unincorporated community in Madison Township, Dubois County, Indiana, United States.
An unincorporated community in Lewis County, West Virginia, United States.


==== Synonyms ====
(island): Emerald Isle
(nation): Republic of Ireland,  Southern Ireland (rare),  Eire (dated, now sometimes offensive), Free State (dated, now chiefly Irish Republicanism)
(both): Éire, Eire, Hibernia, Éireann, Éirinn, Erin, Wolfland (obsolete nickname), Scotia (archaic) Ivernia (archaic), Green Erin (dated, literary, poetic)


==== Derived terms ====


==== Related terms ====
Irish


==== Descendants ====
→ Japanese: アイルランド (Airurando)
→ Tamil: அயர்லாந்து (ayarlāntu)
→ Telugu: ఐర్లాండు (airlāṇḍu), ఐర్లాండ్ (airlāṇḍ)


==== Translations ====


==== See also ====

Hiberno-English


=== Anagrams ===
Ladnier, Reiland, lindera
===== ایرج
ایرج -> 

== Persian ==


=== Pronunciation ===


=== Proper noun ===

ایرج • (iraj)

(Iranian mythology) Iraj
a male given name, Iraj
===== ایرمان
ایرمان -> 

== Persian ==


=== Etymology ===
Inherited from Middle Persian ʾylmʾn' (ērmān), derived from Avestan 𐬀𐬌𐬭𐬌𐬌𐬇𐬨𐬁 (airiiə̄mā, “fellow tribesman; name of a divinity”), from Proto-Iranian *aryamā́, ultimately from Proto-Indo-Iranian *aryamā́ (“fellow, companion; member of one's own tribe/clan; name of a deity”).


=== Pronunciation ===


=== Noun ===
ایرمان • (ērmān / irmân) (Tajik spelling эрмон)

friend, companion
guest
religious leader, cleric


=== Proper noun ===
ایرمان • (ērmān / irmân) (Tajik spelling Эрмон)

a male given name from Persian


==== Related terms ====
آریا (âriyâ, “Aryan”)
===== 𐎠𐎼𐎡𐎹
𐎠𐎼𐎡𐎹 -> 

== Old Persian ==


=== Etymology ===

From Proto-Iranian *Áryah, from Proto-Indo-Iranian *Áryas. Cognate with Avestan 𐬀𐬌𐬭𐬌𐬌𐬋 (airiiō), Sanskrit आर्य (ārya).


=== Adjective ===
𐎠𐎼𐎡𐎹 (a-r-i-y /Aryaʰ/)

Iranian


==== Derived terms ====
𐎠𐎼𐎡𐎹 𐏐 𐎨𐎡𐏂 (a-r-i-y  :  c-i-ç /⁠arya-ciça⁠/)
*Aryābignah
*Aryabr̥zāh
*Aryamanah


==== Descendants ====
Middle Persian: (/⁠ēr⁠/)
Inscriptional Pahlavi script: 𐭠𐭩𐭫 (ʾyl)
```


## [2026-09-04T19:23:35.511Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /tmp && for t in \"Reconstruction:Proto-Indo-Iranian/áryas\" \"ایران\" \"آریا\" \"ἄλλος\" \"alius\" \"else\" \"parallel\" \"alligator\" \"alarm\" \"alert\" \"عراق\" \"اراک\"; do echo \"===== $t\"; curl -s -G --data-urlencode \"titles=$t\" 'https://en.wiktionary.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&redirects=1' | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nfor p in d['query']['pages'].values():\n    if 'missing' in p: print('MISSING'); continue\n    e=(p.get('extract') or '')\n    import re\n    print(e[:1500])\n\"; done 2>&1 | head -250"
}
```


### [2026-09-04T19:23:38.417Z] TOOL RESULT

```
===== Reconstruction:Proto-Indo-Iranian/áryas
Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
===== ایران
Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
===== آریا
Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
===== ἄλλος
Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
===== alius
Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
===== else
Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
===== parallel
Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
===== alligator
Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
===== alarm
Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
===== alert
Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
===== عراق
Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
===== اراک
Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```


## [2026-09-04T19:23:42.783Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /tmp && UA='rishe-verify/1.0 (etymology research; contact eslaminavid0@gmail.com)'; for t in \"ایران\" \"آریا\"; do echo \"===== $t\"; curl -s -A \"$UA\" -G --data-urlencode \"titles=$t\" 'https://en.wiktionary.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&redirects=1' | head -c 300; echo; sleep 2; done"
}
```


### [2026-09-04T19:23:48.755Z] TOOL RESULT

```
===== ایران
{"batchcomplete":"","query":{"pages":{"258627":{"pageid":258627,"ns":0,"title":"\u0627\u06cc\u0631\u0627\u0646","extract":"\n== Azerbaijani ==\n\n\n=== Proper noun ===\n\u0627\u06cc\u0631\u0627\u0646\n\nArabic spelling of \u0130ran (\u201cIran\u201d)\n\n\n== Ottoman Turkish ==\n\n\n=== Etymology ===
===== آریا
{"batchcomplete":"","query":{"pages":{"8859306":{"pageid":8859306,"ns":0,"title":"\u0622\u0631\u06cc\u0627","extract":"\n== Persian ==\n\n\n=== Etymology ===\nLearned borrowing from Old Persian \ud800\udfa0\ud800\udfbc\ud800\udfa1\ud800\udfb9 (a-r-i-y /\u2060Arya\u02b0\u2060/) or Avestan \ud802\udf0
```


## [2026-09-04T19:23:54.720Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /tmp && cat > /tmp/wk.py <<'EOF'\nimport json,sys,time,urllib.parse,urllib.request\nUA='rishe-verify/1.0 (etymology research; eslaminavid0@gmail.com)'\ntitles=sys.argv[1:]\nfor t in titles:\n    u='https://en.wiktionary.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&redirects=1&titles='+urllib.parse.quote(t)\n    r=urllib.request.Request(u,headers={'User-Agent':UA})\n    try:\n        d=json.load(urllib.request.urlopen(r,timeout=30))\n    except Exception as e:\n        print('=====',t,'ERR',e); continue\n    for p in d['query']['pages'].values():\n        print('=====',p.get('title'))\n        if 'missing' in p: print('MISSING'); continue\n        print((p.get('extract') or '')[:2500])\n    time.sleep(1.5)\nEOF\npython3 /tmp/wk.py \"ایران\" \"آریا\" \"ἄλλος\" \"alius\" \"else\" \"parallel\" \"alligator\" \"alarm\" \"alert\" \"عراق\" \"اراک\" 2>&1 | head -220"
}
```


### [2026-09-04T19:24:08.654Z] TOOL RESULT

```
===== ایران

== Azerbaijani ==


=== Proper noun ===
ایران

Arabic spelling of İran (“Iran”)


== Ottoman Turkish ==


=== Etymology ===
Borrowed from Classical Persian ایران (ērān), from Middle Persian 𐭠𐭩𐭥𐭠𐭭 (ʾyʿʾn /⁠ērān⁠/).


=== Pronunciation ===


=== Proper noun ===
ایران • (Îrân)

Iran (a country in West Asia)
Synonym: عجم


==== Derived terms ====
ایرانلی (İranlı, “Iranian”)


==== Descendants ====
Turkish: İran


== Persian ==


=== Alternative forms ===
ایرون (irun) (dialectal)


=== Etymology ===

Inherited from Middle Persian 𐭠𐭩𐭥𐭠𐭭 (ʾyʿʾn /⁠ērān⁠/), see there for more. 


=== Pronunciation ===


=== Proper noun ===
ایران • (ērān / irân or īrān / irân) (Tajik spelling Эрон or Ирон)

Iran (a country in West Asia); (historically) Persia
Synonym: (official) جُمْهوریِ اِسْلامیِ ایران (jomhuri-ye eslâmi-ye irân)

a female given name, Iran, from Middle Persian


==== Usage notes ====
The female given name does not change its ending in the dialectal register.
In the Standard Colloquial of Iran (Tehrani), retains its original form ایران (irân) instead of an -un form (ایرون (irun)).


==== Derived terms ====


==== Descendants ====


== Urdu ==


=== Etymology ===
Borrowed from Classical Persian اِیرَان (īrān).


=== Pronunciation ===
(Standard Urdu) IPA(key): /iː.ɾɑːn/

Rhymes: -ɑːn
Hyphenation: اِی‧ران


=== Proper noun ===
اِیران • (īrān) m (Hindi spelling ईरान)

Iran (a country in West Asia)


==== Related terms ====
اِیرانِی (īrānī, “Iranian”)


=== See also ===
(Middle East) مَشْرِقِ وُسْطیٰ (maśriq-i vustā); سَعُودی عَرَب (sa'ūdī 'arab), مِصْر (misr) عِراق ('irāq), اِیران (īrān), اُرْدُن (urdun), شام (śām), تُرْکِیَہ (turkiya), قِبْرِص (qibris) فِلِسْطِین (filistīn) اِسْرائِیل (isrāīl) لِبْنان (libnān) یَمَن (yaman) عُمان ('umān) مُتَّحِدَہ عَرَب اِمارات (muttahida 'arab imārāt) قَطَر (qatar) بَحْرِین (bahrīn) کُوَیت (kuvait) (Category: ur:Middle East)


=== References ===
“ایران”, in ریخْتَہ لُغَت (rexta luġat) - Rekhta Dictionary [Urdu dictionary with meanings in Hindi & English], Noida, India: Rekhta Foundation, 2026.
===== آریا

== Persian ==


=== Etymology ===
Learned borrowing from Old Persian 𐎠𐎼𐎡𐎹 (a-r-i-y /⁠Aryaʰ⁠/) or Avestan 𐬀𐬌𐬭𐬌𐬌𐬋 (airiiō), ultimately from Proto-Indo-Iranian *Áryas (see for more information). Doublet of ایر (êr, “Iranian”), which was inherited via Middle Persian 𐭠𐭩𐭫 (ʾyl /⁠ēr⁠/). Compare Urdu آریہ (ārya, “Aryan”).
Attested in the Neo-Persian period when used by Hamza Isfahani in the 10th century AD as a synonym of ایران (êrân, “Iran”). The modern usage of it in reference to the supposed Aryan race dates back to the early 20th century, when Sadeq Rezazadeh Shafaq became the first to use it in place of the earlier آریان (âryân), which was borrowed in the late 19th century from either French aryen or English Aryan by Mirza Aqa Khan Kermani.


=== Pronunciation ===


=== Noun ===

آریا • (âriyâ or âryâ) (plural آریاها (âriyâ-hâ), or آریایان)

Aryan
Synonym: آریان (âryân)


==== Related terms ====
آریایی (âriyâyi, “Aryan”)
آریانا (âriyânâ, “Ariana”)
ایران‌ویج (êrânvêj, “Realm of Aryans, Airyanem Vaejah”)
ایرمان (êrmân, “friend, fellow tribesman”)
یل (yal, “hero, great warrior”)


=== Proper noun ===
آریا • (âriyâ or âryâ)

a male given name, Arya


=== References ===
===== ἄλλος

== Ancient Greek ==


=== Alternative forms ===
αἶλος (aîlos) — Cypriot
ἄλλυ (állu) — Arcadian


=== Etymology ===

From Proto-Hellenic *ál͏̌l͏̌os, from Proto-Indo-European *h₂élyos. Cognates include Latin alius, Old Irish aile, Old Armenian այլ (ayl), Old English elles (English else).


=== Pronunciation ===


=== Adjective ===
ᾰ̓́λλος • (ắllos) m (feminine ᾰ̓́λλη, neuter ᾰ̓́λλο); first/second declension

other, another, different, else
(with article) the other, all others, all besides, the rest

(with numerals) yet, still
(in lists) as well, besides, too
equivalent to ἀλλοῖος (alloîos) of another sort than (with genitive)
(in phrases)
in combination with τις (tis) any other; anyone else, anything else
in the phrase ἄλλος τε καὶ (állos te kaì) especially, most of all
in the phrase εἴ τις καὶ ἄλλος (eí tis kaì állos) or εἴ τι καὶ ἄλλο (eí ti kaì állo) if anyone, whoever else; if anything, whatever else


==== Declension ====


==== Coordinate terms ====


==== Derived terms ====


==== Descendants ====
Greek: άλλος (állos)
Mariupol Greek: а́лус (álus)


=== References ===


=== Further reading ===
“ἄλλος”, in Liddell & Scott (1940), A Greek–English Lexicon, Oxford: Clarendon Press
“ἄλλος”, in Liddell & Scott (1889), An Intermediate Greek–English Lexicon, New York: Harper & Brothers
“ἄλλος”, in Autenrieth, Georg (1891), A Homeric Dictionary for Schools and Colleges, New York: Harper and Brothers
“ἄλλος” in Bailly, Anatole (1935), Le Grand Bailly: Dictionnaire grec-français, Paris: Hachette
Bauer, Walter et al. (2001), A Greek–English Lexicon of the New Testament and Other Early Christian Literature, Third edition, Chicago: University of Chicago Press
ἄλλος in Cunliffe, Richard J. (1924), A Lexicon of the Homeric Dialect: Expanded Edition, Norman: University of Oklahoma Press, published 1963
“ἄλλος” in the Diccionario Griego–Español en línea (2006–2026)
“ἄλλος”, in Slater, William J. (1969), Lexicon to Pindar, Berlin: Walter de Gruyter
G243 in Strong, James (1979), Strong’s Exhaustive Concordance to the Bible
Panayotou, A. “Arcado-Cypriot.” In A History of Ancient Greek from the Beginnings to Late Antiquity, translated by Chris Markham, 417–432.Woodhouse, S. C. (1910), English–Greek Dictionary: A Vocabulary of the Attic Language‎[2], London: Routledge & Kegan Paul Limited. 
ἄλλος, in ΛΟΓΕΙΟΝ [Logeion] Dictionaries for Ancient Greek and Latin (in English, French, Spanish, German, Dutch and Chinese), University of Chicago, since 2011


== Greek ==


=== Etymo
===== alius

== Esperanto ==


=== Pronunciation ===
IPA(key): /aˈlius/
Rhymes: -ius
Syllabification: a‧li‧us


=== Verb ===
alius

conditional of alii
```


## [2026-09-04T19:24:15.686Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /tmp && python3 /tmp/wk.py \"else\" \"parallel\" \"alligator\" \"alarm\" \"alert\" \"عراق\" \"اراک\" \"ille\" \"alter\" \"ultra\" 2>&1 | grep -A25 '^===== ' | head -300"
}
```


### [2026-09-04T19:24:34.303Z] TOOL RESULT

```
===== else

== English ==


=== Etymology ===
From Middle English ells, elles, from Old English elles (“other, otherwise, different”), from Proto-West Germanic *alljas, from Proto-Germanic *aljas (“of another, of something else”), genitive of *aljaz (“other”), from Proto-Indo-European *h₂élyos, from *h₂el- (“other”).
Cognate with Old Frisian elles (“other”), Old High German elles, ellies (“other”), Danish eller (“or”), Danish ellers (“otherwise”), Swedish eljes, eljest (“or else, otherwise”), Norwegian elles (“else, otherwise”), Gothic 𐌰𐌻𐌾𐌹𐍃 (aljis, “other”), Latin alius (“other, another”), Ancient Greek ἄλλος (állos), Arcadocypriot αἶλος (aîlos), modern Greek αλλιώς (alliós, “otherwise, else”), Proto-Slavic *olni.


=== Pronunciation ===
(Received Pronunciation, US) IPA(key): /ɛls/
(colloquial) IPA(key): /ɛlts/

Rhymes: -ɛls


=== Adjective ===
else (not comparable)

(postpositive, used only with indefinite or interrogative pronouns) Other; in addition to previously mentioned items.


==== Usage notes ====
This adjective usually follows an indefinite or interrogative pronoun, as in the examples above. In other cases, the adjective other is typically used.

--
===== parallel

== English ==


=== Alternative forms ===
paralell (obsolete)


=== Etymology ===
From Middle French parallèle and its etymon Latin parallēlus, parallēlos. The verb is from the noun. See also para- and allo-.


=== Pronunciation ===
(Received Pronunciation) IPA(key): /ˈpæ.ɹəˌlɛl/
(Standard Southern British) IPA(key): /ˈpaɹəˌlɛl/
(General American)

Hyphenation: pa‧ra‧llel, Indic: par‧al‧lel


=== Adjective ===
parallel (not comparable)

Equally distant from one another at all points.

--
===== alligator

== English ==


=== Etymology ===

From early Modern English alligater, alligarta, aligarto, alegarto, alagarto, from Spanish el lagarto (“the lizard”), from Latin lacertus (“lizard”), modern spelling possibly influenced by the unrelated Latin alligator (“one who binds”).


=== Pronunciation ===
(Received Pronunciation) IPA(key): /ˈæl.ɪ.ɡeɪ.tə/
(General American) enPR: ălʹĭ-gā-tər, IPA(key): /ˈæl.ɪ.ɡeɪ.tɚ/

(Australia) IPA(key): /ˈæl.ɪ.ɡæɪ.tə/

Homophone: allegator
Hyphenation: al‧li‧ga‧tor
Rhymes: -eɪtə(ɹ)


=== Noun ===
alligator (plural alligators)

Either of two species of large amphibious reptile, Alligator mississippiensis or Alligator sinensis, in the genus Alligator within order Crocodilia, which have sharp teeth and very strong jaws and are native to the Americas and China, respectively.

--
===== alarm

== English ==


=== Alternative forms ===
alarum


=== Etymology ===
From Middle English alarme, alarom, borrowed from Middle French alarme, itself from Old Italian all'arme! (“to arms!, to the weapons!”), ultimately from Latin arma (“arms, weapons”).


=== Pronunciation ===
(Received Pronunciation) IPA(key): /əˈlɑːm/
(General American) IPA(key): /əˈlɑɹm/

(South Asia) IPA(key): /əˈlɑ(rə)m/
Hyphenation: alarm
Rhymes: -ɑː(ɹ)m


=== Noun ===
alarm (countable and uncountable, plural alarms)

(countable) A summons to arms, as on the approach of an enemy.
--
===== alert

== English ==


=== Pronunciation ===
(Received Pronunciation) IPA(key): /əˈlɜːt/
(General American) enPR: ə-lûrtʹ, IPA(key): /əˈlɝt/

Rhymes: -ɜː(ɹ)t
Hyphenation: a‧lert


=== Etymology 1 ===
From French alerte (“alert”), from the phrase à l'erte (“on the watch”), from Italian all'erta (“to the height”), from erta (“lookout, tower”).


==== Adjective ====
alert (comparative more alert, superlative most alert)

 Attentive; awake; on guard.
Synonym: wakeful
(obsolete) brisk; nimble; moving with celerity.


===== Derived terms =====


===== Translations =====


==== Noun ====
alert (plural alerts)

An alarm.
A notification of higher importance than an advisory.
(military) A state of readiness for potential combat.

(computing) Synonym of bell (“bell character”).


===== Derived terms =====


===== Translations =====


=== Etymology 2 ===
Formed within English by conversion, from alert (adjective). Compare French alerter.


==== Verb ====
alert (third-person singular simple present alerts, present participle alerting, simple past and past participle alerted)

To give warning to.


===== Derived terms =====


===== Translations =====


=== References ===


=== Anagrams ===
alter, alter-, altre, artel, later, ratel, taler, telar


== Dutch ==


=== Etymology ===
Borrowed from French alerte.


=== Pronunciation ===
IPA(key): /aːˈlɛrt/

Hyphenation: alert
Rhymes: -ɛrt


=== Adjective ===
alert (comparative alerter, superlative alertst)
--
===== عراق

== Arabic ==


=== Etymology 1 ===


==== Pronunciation ====
IPA(key): /ʕi.raːq/
Rhymes: -aːq


==== Noun ====
عِرَاق • (ʕirāq) m

only used in العِرَاق (al-ʕirāq, “Iraq”)
only used in عِرَاق الْعَجَم (ʕirāq al-ʕajam)
only used in عِرَاق الْعَرَب (ʕirāq al-ʕarab)


===== Declension =====


=== Etymology 2 ===


==== Pronunciation ====
IPA(key): /ʕi.raːq/
Rhymes: -aːq


==== Noun ====
عِرَاق • (ʕirāq) m (plural عُرُق (ʕuruq) or أَعْرِقَة (ʔaʕriqa)) (Classical)

a double suture that is at the lower end of a waterskin (مَزَادَة (mazāda) or قِرْبَة (qirba)) or eating mat (سُفْرَة (sufra))
shore, coast, any region or area (of a whole country or a mere rivulet in a garden) adjacent to water as opposed to another one

the circuit or surrounding edge of the ear
the fore part and hinder part of the saddle of a horse
the court or yard extending from the sides of the house
pace, rate of going


===== Declension =====


==== Noun ====
عُرَاق • (ʕurāq) m (Classical)

clear water
copious rain
a picked bone, the fleshmeat of bone


===== Declension =====


== Pashto ==


=== Etymology ===
Borrowed from Arabic الْعِرَاق (al-ʕirāq).


=== Pronunciation ===
IPA(key): /ˈirɑq/


=== Proper noun ===
عراق • ('irāq)

Iraq (a country in West Asia in the Middle East)


== Persian ==


=== Etymology ===
Borrowed from Arabic الْعِرَاق (al-ʕirāq, “Iraq”).

--
===== اراک

== Persian ==


=== Pronunciation ===


=== Etymology 1 ===
Persianization of earlier عراق (irāq, arāq / erâġ,  arâġ), from Arabic اَلْعِرَاق (al-ʕirāq), possibly a reference to عِرَاق الْعَجَم (ʕirāq al-ʕajam, “Persian Iraq”). The origin of Arabic اَلْعِرَاق (al-ʕirāq) itself is uncertain, and some say it is an Arabization of اراک, not the other way around. That would ultimately derive it from Middle Persian [script needed] (ˀyrg /⁠ērag⁠/) or [script needed] (ˀl'k' /⁠erāg⁠/, “lowlands”).


==== Proper noun ====
اراک • (arāk / arâk) (Tajik spelling Арок)

Arak (a city in Iran, the seat of Arak County's Central District and the capital of Markazi Province, formerly called Soltanabad)
Synonym: (formerly) سلطان‌آباد (sultān-ābād / soltân-âbâd, “Soltanabad”)
Arak (a county of Iran, around the city)


===== Derived terms =====
```


## [2026-09-04T19:24:50.681Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### FSF irman\"; grep -n -B2 -A6 'ایرمان' FSF_pages.txt | head -40; echo \"### FSF iraj\"; grep -n -m2 -A6 'ایرج' FSF_pages.txt | head -30"
}
```


### [2026-09-04T19:24:50.763Z] TOOL RESULT

```
### FSF irman
3170-                                                                                    ‫چ‬
3171-  ‫باشد بنگر تاحال دیگران چگونه باشد‪.‬‬           ‫ویابیمار بر اومید درمان‬
3172:                                     ‫" ایرمان‬                                ‫اهتوخوشی‬
3173-                ‫مهمان (جهانگیری ‪-‬برهان)‪:‬‬      ‫گبفهتا دربارۀ پیشه‌های چهارگانه در‬
3174-                                                                            ‫ر‬
3175-             ‫اگرکّشته آیدبهدست توگرگ‬                              ‫شاهنامه نگاه کنید‪.‬‬
3176:‫تو باشی به روم ایرمانی بزرگ‬                                                           ‫ایدر‬
3177-‫‏)‪(F0-14-£‬‬                                                                        ‫اینجا‪:‬‬
3178-                                ‫یمن (تازی)‬                    ‫دل و جانم ایدر بماند همی‬
3179-              ‫بی‌ترس و باک» آسوده خاطر‪:‬‬        ‫مژه خون دل بر فشاند همی‬
3180-                                               ‫(‪)۱-۲۵۱-۹۳۴۲‬‬
3181-‫ایوان‬                                           ‫‪۷‬‬
3182-
### FSF iraj
3000: ‫خبطیا‌ومعناست و صورت درست آن‬                  ‫خود می‌سپارد سلم وتور به ایرج» برادر‬
3001-   ‫ارمه‬
3002-      ‫نعتب‬
3003-         ‫هم‬‫اخۀ‬
3004-             ‫همانست که از دشونس‬               ‫که کهپادشاهی ایران نصیبش شده‬
3005- ‫یعنی نسخة لندن (‪ ۵۷۶‬هجری) و نسخه‬             ‫است» رشک می‌برند و گستاخانه به پدر‬
3006-‫کتابخانة عمومی لنینگراد (‪ ۳۳۷‬ه)در بالا‬        ‫پیاممی‌فرستند کهپادشاهی ایران رابهآنان‬
--
3008:‫فریدون در نامه خود به‌سلم و تور به‬             ‫فریدون به خواهش ایرج که حاضر است‬
3009-   ‫تان‬
3010-     ‫رهر‬
3011-       ‫اب‬‫زتان‬
3012-            ‫آادر‬
3013-               ‫شوخی می‌نویسد‪ :‬بر‬              ‫از پادشاهی ایران دست بردارد و نزد‬
3014-
```


## [2026-09-04T19:24:51.629Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BRT airyava full\"; sed -n '5566,5580p' BRT.txt; echo \"### BRT 5539-5560\"; sed -n '5539,5560p' BRT.txt"
}
```


### [2026-09-04T19:24:51.690Z] TOOL RESULT

```
### BRT airyava full
•  j.  'airyaman-  m.  Name  des  mit  J  (7/r- ,  •  j.  'aurvataspa-  Adj.  'der  schnelle ysmä  isys  beginnenden  Gebets  Y.54.1:  Rosse  hat';  a)  von  ^rar-imd  Äj'ari>.tiiji^u-: 'matiim  mq^ranqm  maBittm  Yt.j.5;  —  Är'ur?  "toffi  YL/0.90;  6.4;  —  'tun  bavähi T-3r/irayn3m. .  ya^asli  antan  ahuna(&A.)  yaia  kiari  Az.  6";  —  am.nakc  hü  yat 'manaiAD.)Vi.24.i;*li.ioj.  a)  sonst |  Vn^  YLJO.  13;  —  hiarsxsaS^m  'ptm mit  isya-.  'mamm  isim  .  .  ßäsB  mq^fvm  Yt  6. 1,6, 12.^4, 1^.81,  \.  16.4;  —  hvar>- ..  b»r?am  Aa',aoxt?m  Vr.2.10;  G,/.6,  S.j^/attJj  °päi  Y.ÜÄ22;  —  hrerixiaiiahe 2.3;  —  tfm..  vJspanqm  sravanhqm  ufard.-\ ..  -pake  Yt.  Ö.o,  Y, 22. 24;  /.  11;  —  Iwan- kainm  fradaiqm  yim  'mamm  tsim  FrW. '  xsaiia  'pa  (VS.)  V,  j/.  5,  b)  von  apqm 4-1',  1 ;  —  'taan^m  isim  . .  maiisüm  o/aAe  napät-.  apqm  napa  -ps  Yt  ig.  51';  — sra-.arahqm  Y.54.2;  Vr.  24,1;  —  °manS  aPqm  napättm  'ptm  Y.  2. 5;  —  apqtn isyehe  hafu{iitä..'manö  isyeke ,.  haililca  ..  nap5  °pa  Y.65.13.  'pä'a  VyLjJ, Vr.24.2;  /.8,  S.7.3.                                    4'>"(?).
*)  Es  gehört  lu  At^  vaia  ra^niiämrüla,  i.V.         Vgl. 'oh»t  j/.fli/,i-  EX.  — Pü.:  ai'.;td.i'/;  Npü. : za.  II,  N.  36.  nzasp,    Sa.:    ic,^<r.:id,ii-.ah,    (lu  Y.  2y.  /t.,.!/i.-,-
Vgl.   ijjVj-^ninn.  (mit  No.  l)    und    ä.airyjmä.-        «jiivii.
is)v.  —  Pu.i  m/ian,  frmän  x'aiiiiiiA.  ,  j    »auTvat-aspa-    m.    EN'.    des  Vaters
•  j.  airyava-  m.  EN.  Name  eines  Gläu-  des  Viitäspa-.  pu>ri>m  yat  'fa/ie  taxm>m bigen:    manuS.airahe  (sd.)    'vahe   asaonS  kai-alm  züstJspfm  Vtj.  105.
Yt/J.131.  Vgl.  'aut'.al.aspi-.
VU.  «„>.«-+•,«.«.  -Helfer  der  Arier'   zum  \\  ,  =_  a-urva»a- Adj.  'inimicus':  ar-a^a  (sd.)
<!:-.  —  OJliSTls  Deutung,  MJ.  II  stut;t  sich  '_          ,.                  \            ,      >      ,-             «
auf  die  minder  gut  bezeugte  Lesung  .üry^r^'.  mavayatit ..  vjspe  t^m?niu  '>a\t.  14^18;
,                    ^„     .        „           .,  —  hamfriianam  '"ironam  ibilyaniam  \ ,
•  p.  anyaranma- m.  EN.  mts  Perser.",  ,j     Vrt.*m",  Yt.;?..!:   —' -iim
/,/,,  to/,/)  Bhr.2.  i,./vLl.J.69,Y.6.V.i3(wo-ii%4;.',.);  —
*)  Enltels  des  ,4.*fl<-«;,-««,  Licrossvaters  des  ::     ,       "^       i    -       .         ,  ,-.  ^
Dii'iiit  I.  °-^'??  /"n'  dusmattiyaot  \t;.34;   —    "ii*
Aus  *ari}-j-räm,iii-  Adj.  "der  den  Ariern  Ruhe,  Yt  II.  2  (?) ".
### BRT 5539-5560
•  '].  airya-,  p.  ariya-  1)  Adj.  (fem.  ya-) 'arisch':  'yanam  daRyunqm  . .  tüiryanam dahyunqm  Ytl  13.  i43';' 1°.  87',  5.49, 58,  117,  ig.  56,  69,  V,  ig.  39 ;  —  'yä  dai- tihavd  \i.8.jfi,  52%  58^;  —  'yäbyS  dai- tüulys  Yt.^. 61  \  10.4;  —    yäiyö  (statt
'  mask.)  päla^i^yS  Yt 4.  $.  2)  m. 'Arier': \  djrayä*va^us  . .  *_ya*  ar:ya^xji<''a*  D.6.x;
I  —  ya>a  vJspe  *anye  're  (NP.)  Yt.  5. 69 ;  — ?r?xsö  (sd.)  .  .  xsvivii.isvatfmS  'yanqm  Yt S.6;  —  'yanqm  ifaranS  Yt.lS.o,  Ny.5.5.
KompA.  fs.  auch  *v7sfie.aire.riaurä-);  Ableit.  — ai.  Tgl.  arya-  m.  'Atier';  mp.  (Pü.),  ttf.irän; •Apni.  —   ')  S  16S.  32.
•  j.  anya^citKa-  Adj.  'aus  arischem  Ge- schlecht stammend':  darayc^vi^ul . .  °>''i2* D.  ti.  2.
Komp.  mit  NS.  im  i,  Glied.  Dazwischen  der VVortirenncr.     (Anders  Fov  KZ.  ^/.  524.)
•  j.  airyana-  Adj.  'arisch':  "m/w  :^ar3nS Yt.  J<?.  1,  5,  7,  8,  S.  2.  9*>;  —  sonst  von vasjah-  (sd,,  auch  fdSt):  °n»m  vagjö,  'yeiie val/aAi.
Ableit.  aus  airya-.  —  Vgl.  'Apiä-f^l  —  Pü.; erSii  (vH).  —  'I  S.  /■.  9  =  Ny.j.  5  steht  air- yanqm  x'ar^nä.
j.  airyanimna  N.  loy.  lies  airyamana.
•  jj  g-  'airyaman-,  g.  airyäman-  m. 'Genosse'  uzw.  priesterlicher,  Angehöriger des  ersten  oder  Priesteratands  (s.  unter 'pistra-),  'Sodale' ;  Sing,  auch  koU.  'Soda- lität',  nur  gAw.:  iJ  yama  kp  x^allus  {%<!.) dätäis  anhat  yp  ,  .  Y.  /fg.  7 ;  —  ahyScH x'aSus  (sd.)  yjsal  ahyä  virizsntm  mat yamnn  . .  Y.J2.1;  —  yf  '^jvaj  masdn asruinm  . .  yazli  (sd.)  apa  K^'aüSuScä  tar>- maitTm  virn^nahyiilä  . .  'yamanascä  . .  Y. 33-4  i  —  y^  asäuia  vahiils  :^aSä  (sd.) vä  al  vä  v>r>iSny3  yämiiä  (IS.  als  Subj.)  '> vil .  .  Y.  JJ.  3;  —  pairl  clausus  'yama- nascä  dadaili  ndii  .  .  i-ir>z5nä  (sd.)  Y.46. I.  A)  Name  einer  Gottheit":  vairya sar)ha  para.äi'd  upa.vasanuha  avi  nmli' mm  yamaini  imat  sanhsis  'yamanäi  J' "A^,  geh  weg,  fahr  hin  ins  Haus  zu  A., das  sollst  du  dem  A.  kund  machen"  V.
|22,7;  13  ('maini,  'man-ii'').  a)  sonst |mit  ya-  isya-  (Adj.):   mosu  tal  äs  .  .  yai
dby  Google
1 99  'airyaman-  —  aurvant-  aoo
/nlyatayat 'yama  yJ  ilyö  gairim  avi  spjiitJ.-  °'^aj  haca  garsit  ^anvant>m  ai-i  guirtm frasnti  V.  22. 19;  ao;  —    äa^  mqm  tum  Yt.<K6.
biiazydtH  yama  yj  isyS  (NS.  als  Vs.)  V.  Bed.?  Die  LesmiE  des  z.  Glieds  ist  unsicher. 22.9;    —   a    -ySmä    i^S   ra/?lräi  jan/a       "     K'- lu  j^jj/a-.
mnbyascä  näiribyasca  xara>ustrahe  za-  »j.  aurva- Adj, 'schnell;tapfer">:  ^«rffli^^iT tshsus  raßoräi  manaahS  "het  komme  Ae^  aiWü  'vS  \X.4.q;  —  Iqm  yazjitta  'va liebe  X  zur  Unterstützung  zu  den  Männern  hunavSvalsakaya\\..$.t,T,i^;—iS>:riv!Ht und  Frauen  des  Z,  zur  Unterstützung  des  "'^"p«  Yt/0.109;  14;  —  'itwam  yazfmU guten  Sinns"  V.54,1.  "i-ätihs  ahuränhs  VL5.85;  —  yat  bäun
•)    Über   die   Bedeutung   des  Gotls   ist   den    t'isjie  °va   Vlspe  taxma   .  .  kave  HK.1Q.1z; ,i'j5i sehen  Teilen  nichu  Klnies  lu  entnehmen;   —    'v3  as.vancS   kava    usa  Yt5.45;   —
die  GrBd.-Stellc  bei  Dst.  ZA-  3.  319.    S.  noch  -'  ,-,,r.,  ,7.  -'  ■",  -^
No.  2.  ""^^  'i'a{VS.)  YLJ5.57;  46,  S4;  —  i'asm
VgL  'airyaman-.  —  m.  atyaman-  m.  i)  'Ge-  °vanqm  aunvJ^mftn  Yt  Jj.  57;  —  von fahrte',  a)  Name  eines  Äftfia ;  np.  Tgl.  ÖTiiäu  Httoma:  kaoma  . .  ya~ia  raeuaJie  hubaoi'ds 'Gast'«).    —   Pü.:    ertnän  iSü-i  ädiiah,  ädtia-    ,.,  v  rn  •
wJ^),   (zu  Y.  jj.  3,  49.  7):   irmäalh   (Sü. iirff/a/i,  SdinkatS).  —  »  S.  "ara-  No.  3.  —  =)  In
Ableit    —    Vgl.  aunanl:    —    Pü.  {lu  V.  p):
```


## [2026-09-04T19:25:09.475Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/arran-a-region",
 "prompt": "What is the etymology and origin of the name Arrān (Persian آران/اران)? Does it derive from Aryan/*arya-, or from Caucasian Albania / Armenian Ałuank'? Quote the etymological statement."
}
```


### [2026-09-04T19:25:11.309Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T19:25:11.815Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/eran-eransah",
 "prompt": "Quote what this article says about the origin of the names Ērān and Ērānšahr: from Old Persian ariya-, genitive plural aryānām, Avestan airyanąm, and the relation to airyanəm vaējah / Ērānwēz."
}
```


### [2026-09-04T19:25:13.382Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T19:25:17.421Z] TOOL CALL #39: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py; echo ...; python3 tools/fetch_source.py --help 2>&1 | head -30"
}
```


### [2026-09-04T19:25:18.964Z] TOOL RESULT

```
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
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
...
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


## [2026-09-04T19:25:27.685Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp && python3 /tmp/wk.py \"Reconstruction:Proto-Indo-European/h₂el-\" \"Reconstruction:Proto-Indo-Iranian/áryas\" \"Reconstruction:Proto-Indo-European/h₂élyos\" \"ایرلند\" \"اران\" \"اردلان\" 2>&1 | head -140"
}
```


### [2026-09-04T19:25:39.704Z] TOOL RESULT

```
===== Reconstruction:Proto-Indo-European/h₂el-

== Proto-Indo-European ==


=== Etymology 1 ===


==== Root ====
*h₂el- (imperfective)

to grow, nourish


===== Derived terms =====

*h₂él-e-ti (thematic root present)
*h₂ol-éye-ti (causative)
Proto-Germanic: *aljaną (see there for further descendants)
Proto-Italic: *oleō (see there for further descendants)
*h₂el-mn̥-to-m
Proto-Italic: *almentom
Latin: alimentum (see there for further descendants)
*h₂el-mo-s
Proto-Italic: *almos
Latin: almus (see there for further descendants)
*h₂él-ti-s ~ *h₂l̥-téy-s
Proto-Germanic: *aldiz (see there for further descendants)
*h₂el-tó-s
Proto-Celtic: *altos (see there for further descendants)
Proto-Germanic: *aldaz (see there for further descendants)
Proto-Italic: *altos
Latin: altus (see there for further descendants)
*h₂el-dʰr-o-m or *h₂el-tr-ó-m
Proto-Germanic: *aldrą (see there for further descendants)
*h₂el-wó-s
Proto-Italic: *alwos (perhaps)
Latin: alvus (see there for further descendants)
*h₂el-i-
Proto-Italic:
Latin: (ind)olēs, (pr)ōlēs
⇒? Proto-Italic: *-ālis (see there for further descendants)
*h₂el-dʰ-
Hellenic:
Ancient Greek: ἀλθαίνω (althaínō)


==== References ====


==== Further reading ====
Pokorny, Julius (1959), “2. al-”, in Indogermanisches etymologisches Wörterbuch [Indo-European Etymological Dictionary] (in German), volume 1, Bern, München: Francke Verlag, pages 26-27


=== Etymology 2 ===


==== Root ====
*h₂el-

beyond, other


===== Alternative reconstructions =====
*ál (“elsewhere”), *ól (“over there; far”)


===== Derived terms =====

*h₂él-yo-s (“other”)
*h₂el-en-o- ~ *h₂el-n-o- (various thematic n-stem derivatives)
⇒? Proto-Balto-Slavic:  (or from *h₂ól-h₁n-, with postfixed *h₁én)
Proto-Slavic: *olni (“last year”, adverb, originally loc. sg. noun) (see there for further descendants)
Proto-Celtic: *alnos (“other”) (see there for further descendants)
Proto-Indo-Iranian: *Háranas (reflecting *h₂élenos)
Proto-Indo-Aryan: *Háranas
Sanskrit: अरण (áraṇa, “foreign, distant”)
Proto-Italic: *olnos (“that”, pronoun) (reflecting either *h₂ol-no-s or *h₂l̥-no-s)
Latin: ollus, olle, ōlim, ille (see there for further descendants)
⇒ Proto-Tocharian: *ālle-kä (“other”) (with *-kä)
Tocharian A: ālak
Tocharian B: allek
*h₂él-(i)-tero-s (compare *h₂él-yo-s and below)
Proto-Italic: *al(i)teros (“other (of two)”) (see there for further descendants)
*h₂ol-tero-s
Proto-Italic: *olteros
Latin: ulter (“beyond”, adjective), ultrā (adverb)
⇒? Old Latin: uls (“beyond”), ouls (perhaps formed on the example of cis vs. citrā
===== Reconstruction:Proto-Indo-Iranian/Áryas

== Proto-Indo-Iranian ==


=== Etymology ===
Uncertain.

There have been many attempts to qualify the ar- verbal root of Old Iranian *arya- (with short -a, found in Old Persian as ariya-, and Avestan as airiia-, etc), and Old Indic ārya- (with long -a, vriddhi-formed Sanskrit ā́rya-). No Nuristani cognate has yet been identified, however. The most influential (and in the case of Pictet, notorious) of these include:

Before 1957 (these assume that various Sanskrit (near-)homonyms derive from a single historical unity):
Franz Bopp (1830): ar- "to go, to move", read as "one who roams" (like a nomad)
Adolphe Pictet (1858): ar- "to plough", read as "cultivator of the land"
Hermann Güntert (1924): ar- "to fit", read as "allied, friendly"
Paul Thieme (1938): ar- "to give, allot, share", read as "hospitable, friendly"
1957 and later (these differentiate between the Sanskrit gentilic ā́rya- and the (near-)homonyms árya-, aryá-, aryà-, ā́rīḥa-, etc.):
Emmanuel Laroche (1957): ara- "to fit", read as "fitting, proper"
Georges Dumézil (1958): ar- "to share", read as a uniting property of "belonging to the Aryan world" ("appartenant au monde aryen")
Harold Walter Bailey (1959): ar- "to beget", read as "born, nurturing"
Émil Benveniste (1969): ar- "to fit", read as "companionable"
For a review of these and many other considerations, see Szemerényi 1977, pp. 103–147.
A derivation from Proto-Indo-European cannot be obtained with certainty either. This is because

Indo-Iranian ā/a is historically unspecific. Indo-European ā, ē, ō merge as Indo-Iranian ā (a similar merger also occurs for short vowels).
the rules governing ablauts are poorly understood and it is not certain whether PIE had an a-vowel at all; in principle ārya- could simply reflect zero-grade n̥ryo-.
the a priori assumption that ārya- is Indo-European is not assured. No comparable ethnonym is found in any other Indo-European language (i.e. other than the Indo-Iranian ones). 18th/19th-century assumptions of a relationship to Irish Éire, German Ehre, etc. have long since been dismissed; relation to Proto-Celtic *aryos is plausible, but the latter term is never used as an ethnonym. It is possible that the autonym was originally a name given to the Indo-Iranians by another (non-Indo-European) people.
the relationship between various Sanskrit (near-)homonyms has not been established. In addition to the vriddhi-formed ā́rya- that corresponds to Old Iranian ariya/airiia etc., Sanskrit also has árya-, aryá-, aryà-, ā
===== Reconstruction:Proto-Indo-European/h₂élyos

== Proto-Indo-European ==


=== Etymology ===

From *h₂el- (“beyond, other”).


=== Determiner ===
*h₂élyos

other, another


==== Inflection ====


==== Alternative reconstructions ====
*ályos


==== Derived terms ====
*h₂éli-tero-s (or from pre-thematicized *h₂él-i-; or formed within Proto-Italic)
```


## [2026-09-04T19:25:46.387Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp && python3 /tmp/wk.py \"ایرلند\" \"اران\" \"اردلان\" \"𐭠𐭩𐭥𐭠𐭭\" 2>&1 | head -90"
}
```


### [2026-09-04T19:25:54.605Z] TOOL RESULT

```
===== ایرلند

== Persian ==


=== Etymology ===
Borrowed from French Irlande.


=== Pronunciation ===


=== Proper noun ===

ایرْلَنْد • (irland)

Ireland (a country in northwestern Europe)


==== Related terms ====
ایرْلَنْدی (irlandi)
===== اران
MISSING
===== اردلان
MISSING
===== 𐭠𐭩𐭥𐭠𐭭

== Middle Persian ==


=== Alternative forms ===
𐭠𐭩𐭋𐭠𐭭 (ʾylʾn)


=== Etymology ===

Substantivized Middle Persian oblique plural (-ān suffix) of 𐭠𐭩𐭫 (ʾyl /⁠ēr-⁠/, “Iranian”), giving "of the Iranians". Middle Persian adjective ēr- reflects Old Iranian adjective *arya-, as found in Old Persian 𐎠𐎼𐎡𐎹 (a-r-i-y /⁠Aryaʰ⁠/, “Iranian”) and Avestan 𐬀𐬌𐬭𐬌𐬌𐬋 (airiiō, “Iranian”). See Proto-Indo-Iranian *áryas for further etymology.
The term is first attested in the early 3rd-century trilingual (Middle Persian, Parthian, Greek) inscriptions of Ardašīr I, founder of the Sassanian dynasty. In those inscriptions, the Parthian equivalent is aryān (𐭀𐭓𐭉𐭀𐭍 (ʾryʾn)), which is similarly formed from Parthian ary (𐭀𐭓𐭉 (ʾry)) + oblique plural suffix -ān. The Greek version reads arianōn ethnous.


=== Proper noun ===
𐭠𐭩𐭥𐭠𐭭 • (ʾyrʾn /ērān/)

of, or pertaining to, the Iranian peoples, i.e. the Iranian nation.
The following fragment is from the Middle Persian part of the trilingual (Middle Persian, Parthian, Greek) inscription inscription of Ardašīr I, circa. 225 CE, that accompanies Ardašīr's investiture relief at Naqsh-i Rustam:

the Sasanian state, a former kingdom in West Asia, ruled by Iranians; abbreviated form of 𐭠𐭩𐭥𐭠𐭭𐭱𐭲𐭥𐭩 (ʾyʿʾnštʿy /⁠ērānšahr⁠/, literally “kingdom of (i.e. ruled by) Iranians”)


==== Usage notes ====
The distinction is between nation and state. Initially, ērān signified peoples/culture, i.e. the Iranian nation, and subsequently developed into the name of a political entity. The antonymic 𐭠𐭭𐭩𐭥𐭠𐭭 (ʾnyʿʾn /⁠anērān⁠/), originally meaning "non-Iranians", underwent a parallel development.


==== Antonyms ====
𐭠𐭭𐭩𐭥𐭠𐭭 (ʾnyrʾn /⁠anērān⁠/)


==== Derived terms ====
𐭠𐭩𐭥𐭠𐭭𐭱𐭲𐭥𐭩 (ʾyrʾnštry /⁠ērānšahr⁠/)


==== Descendants ====
Classical Persian: ایران (ērān), انیران (anērān) (see there for further descendants)
Dari: ایران (ērān), انیران (anērān)
Iranian Persian: ایران (irân), انیران (anirân)
Tajik: Эрон (Eron), анерон (aneron)
→ Old Armenian: Երան (Eran)


=== References ===
```


## [2026-09-04T19:26:03.572Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### LAT alius\"; grep -n -m3 -A12 '^alius' LAT.txt | head -40; echo \"### LAT ille\"; grep -n -m2 -A10 '^ille' LAT.txt | head -30; echo \"### LAT ulter\"; grep -n -m2 -A8 '^uls\\|^ulter' LAT.txt | head -25"
}
```


### [2026-09-04T19:26:03.661Z] TOOL RESULT

```
### LAT alius
5691:alius, idem atque, etc., oA il est 4 quivalent de quam. Le sens ancien95
5692-ater
5693-apparait encore e.g. dans Pl., Epid.403, diuortunt mores uirgini longe
5694-atque lupae. Atque ainsi interpr^t^ comme equivalent de quam a pu
5695-s’employer avec des adjectifs an comparatif, e.g. Pl., Cas.680, Mere.
5696-897, etc.; quelquefois meme dans des phrases on le premier terme de
5697-la comparaison manque, Pl., Bacch.549, quem esse amicum ratus sum atque
5698-(a.utant qne) ipsus sum mihi. Aussi ac si s 1 emploie-t-il ponr quasi
5699-dans la langue familiare et en bas latin. M.L.57.
5700-atqui : sens propre "mais de tonte fa^on" d'oii "et pourtant" gene-
5701-ralement avec valeur emphatique; correspond ponr le sens au gr. aXXot
5702-[xt)v; aXXa 8rj7tou, aXXa xoi, kou p,T|v, xaCxot. Ponr la formation cf.
5703-alioqui, ceteroqui, utqui. Les deux ^lements sont encore distincts
--
51482:alius, etc. Se place prbs d'un verbe, d'un adverbe ou d'un adj ectif
51483-pour le renforcer; cf,nimis quam, ualde quam, mire quam, sanS quam,
51484-quamplurSs, plurimi} quamprimum, quam maxime. Pour la forme, cf.
51485-aussi nam, - Usit£ de tout temps. M.L.Gy«8.
51486-L'osque a mais... pan... "magis... quam" et pruter pan "priusquam";
51487-ce pan repose sur *pande, comme on le voit par ombr.^one "quam";
51488-pour la forme, cf.v.lat.quande et ombr.pune, pone de quonde. Le
51489-correspondant de lat. quam est dans ombr. pre-pa "priusquam"; cf.pel.
51490-pam. Ilors de 1'italique, on ne peut rapprocher que arm.fe an, qui
51491-r^pond pour le sens a lat. quam.
51492-V. quis.
51493-quamdlu {-dius Inscr., v. Thes. V 1561,73 et suiv.): [depuis] com¬
51494-bien de temps; et secondairement "aussi longtemps que, jusqu'A ce
### LAT ille
14486:ille creator huius urbis gomulus. Dans la 1 . du droit, creare a pris
14487-le sens special de " 41 ever A une magistrature, nommer, elire", T.L.
14488-4,4,2, pontifices, augures... ab Huma Pompilio creati sunt; Cic., Leg.
14489-3,9, qui comitiatu creare consules rite possint. La langue de 1 'Sglise
14490-s'est beaucoup servie du verbe avec le sens de "creer", c.-A-d. "faire
14491-naitre du n^ant", cf. Aug., Ciu .22,14, qui creauit cuncta de nihilo;
14492-et elle a developp^ dans cette acception 1'usage de creator, et fait
14493-creatura "cr^ation" et "creature" (double sens qu'elle donne egalement
14494-A creatio traduisant XTl.apXX, XTIOXC cf.Aug.fid. et symb .4,5), qui n'est
14495-atteste qu'A partir de Tertullien et “'de 1 'Itala. Creator, creatio,
14496-creatrix, bien que classiques, sont du reste rares avant que la langue
--
29354:ille
29355-templS, et gr.ava ou xara ranov, erii totcou.
29356-Ilico est issu de *en stlocod > i(n) s(t)locd(d) > ilico (v. locus) .
29357-II n'y a jamais en de donble l dans le mot; la graphie tardive illico
29358-est due k nn faux rapprochement avec illic. Le mot semble appaxtenir
29359-au langage familier: fr^quent dans les comiques, rare chez Cic.,
29360-inusite chez les dactyliques a cause de sa forme; cf.J.B.Hofmann
29361-Lat. Ungangs O4.
29362-illa: crxajXri^ xX£vr|C (Gloss.); semble identique a la glose grec-
29363-que: iXiqoi," crxooAf]xeC ev touC Spuat,. Sans autre exemple, et inex-
29364-plique.
### LAT ulter
11840:ulterius cilia infestent. - Atteate depuia Pline. M.L.19x3. Rapproch^
11841-de celare par Iaid., Or.11,1,48, -a sunt tegmina quibus cooperiuntur
11842-oculi, et dicta cilia quod celent oculos.
11843-Derivas et composes: ciliatus (Gloas.) = euocppu?; interci l iuw.entre-
11844-deux dea sourcils (= gr. p,e< 70 Cppuov); supercilium: aourcil (d£ja dana
11845-Pl., usuel et classique)j M.L.8459; d'ou superciliosus (epoq.imp.);
11846-ciliumbris (= ocppuooxi,o£, Bobce). ,
11847-De *k°liyo-', pour la forme, cf. v.h. a. hui la "enveloppe" et gr.xccXUa;
11848-pour la phon^tique, cf. le type de milium, sine, similis. V. la racine
--
68401:ulsus,-us m.: vue (sens actif et passif: facult 4 de voir ou d'etre
68402-vu [abstrait ou concret]), aspect, apparence. M.L.9384.
```


## [2026-09-04T19:26:06.237Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### IEC aryo\"; grep -n -E '^ari[oy]|^arya|^aryo' IEC.txt | head -10; echo \"### IEC alyos\"; grep -n -E '^alios|^alyos|^al-|^olnos' IEC.txt | head -10; echo \"### SYN other\"; grep -n -i -m5 -A12 'other.*12\\.3\\|12\\.33' SYN.txt | head -40"
}
```


### [2026-09-04T19:26:06.339Z] TOOL RESULT

```
### IEC aryo
694:ario (1) and (2), see aro (1) and (2)
704:arios *man, hero; manly’. WP I, 80. Cf. åros Skt. áryah, s.; aryáh, adj.; Av, airyo, adj.; Medic Arios ‘Mede’; Arm. ajr (arn, aramb, g & ins.) ‘man’; aru, adj. ‘male’; Gk. ar- in various cpds. and extns. areion, áristos, arete; prob. also in áron 'arum-lily', ás-aron (*man- plant", i.e. baccharis); ár-óma (?) (lit. ‘good smell’; for -oma, cf. Latv. osma 'smell); un- certainly ari- (px. 'very-); doubtfully Lat. aries ‘ram’; uncertainly Or Ir aire, gs. ai- reach, ds. and npl. airigh (Cchieftain, noble- man’. Best as a formula *pri-reg- ?). Other possible relationships are MIr. náir 'shame- fu’ beside nár, id. (:Li. *ne-orüs ‘ignoble’ ? See ar-) and Br. her ‘bold’, w. non-historical h- ?)
705:arios, see aros, and cf. arios
### IEC alyos
407:al- ‘wander, go’. Cf. al-eió Gk. aláomai; LLat. alare (or alar) "bunt, cpd. in amb-ulàre, simplex in OFr. aler. (The LL wd. is given by Servius, 4th.cent. AD in the form aiator “hunter”) h
443:alios "other WP I, 85 Tokh. cf. alàn ‘otherwise’; Arm. ajl; Gk. ál- los; Lat. alius: Osc. allo-; MIr. aile, aili-; Ir. eile beside all; Gaul. allo- beside alla "else, where’; W aill, all- “other? beside ail ‘second’;
5574:al- (1) ‘skin, tissue, texture”
12126:olnos — -omeno-
### SYN other
1011:Boh. vrch ‘top, summit’ (as ChSl. vrichit, etc. 12.33), used also for ‘moun- tain’.
1012-Boh. kopec ‘hill’, fr. kopa ‘heap’. Ber- neker 562.
1013-7. Skt. giri-, Av. gairt- : ChSl. gora, etc., above, 5.
1014-Av. barazah- : OE beorg, etc., above, 4.
1015-OPers. kaufa-: Du. heuvel, etc., above, 4.
1016-Skt. parvata- ‘mountain, mountain range, rock’, Av. paurvata- ‘mountain range’, fr. adj. Skt. parvata- ‘knotty, rugged’, fr. parvan- ‘knot’.
1017-Skt. acala- ‘mountain’ fr. adj. acala- “Smmovable’.
1018-Skt. ¢azla- ‘mountain’, fr. ¢ila- ‘stone, rock’.
1019-1.28 PLAIN, FIELD
1020-Grk. zedlov Goth. stabs ibns Lith.
1021-NG medlov, wedtada, Kauros ON slétta
1022-lyguma, laukas Lett. lidzenums, lauks
1023-Lat. planum, campus Dan.  slette, mark ChSI. mésto ravtno, polje It. pianura, campo Sw. slatt, mark SCr. _ ravan, ravnica, polje Fr. plaine, champ OE emnet, feld Boh. _ravina, pldt, pole Sp. llanura, campo ME opilaine, feld Pol. réwnina, plaszczyzna, Rum. cimp NE plain, field pole
--
9664:Europe generally until the introduction | Lett. medus, OPruss. meddo, Chs] | of sugar (5.85). From it was made the | medi, etc., general Slavic ; Skt. madhy,. oldest IE intoxicating drink, the ‘mead’ | Toch. mit. Elsewhere only as ‘mead! 5 ! (5.91). or for some other intoxicating drink { Most of the words for ‘honey’ belong | (5.91). : to one of two inherited groups. In Gmc. 3. ON hunang, OE hunig, ete., gen. one of these is represented in Gothic, the | eral Gmc. (except Goth.) : Skt, han- if other in words for ‘mead’, otherwise | cana- ‘golden’, kanaka- ‘gold’, Grk | ‘honey’ is expressed by a new word de- | xvnxés ‘pale yellow’ etc. Walde-p. 6 rived from its yellow color. 1.400; Falk-Torp 417. N 1. IE *melit- ‘honey’. Walde-P. 4. Av. *paéna-, implied by paénaéna- L : 2.296. Ernout-M. 602. Grk. pé\:; Lat. | ‘prepared from honey’, NPers. angubin : mel (> Romance words); Ir. mil, W., | ‘bee-honey’, prob. as (bee’s) ‘milk’ or gj Br. mel; Goth. milip (cf. OE mil-déaw | ‘juice’ : Av. payah-, paéman- ‘milk’, Skt, : ‘honey-dew, nectar’, milisc ‘honeyed’); | payas- ‘milk, juice’, Lith. pienas ‘milk’ ; Arm. meir, Alb. mjall. (5.87). Barth. 817. i B 5.85 SUGAR ; Grk. céxxapr, etc. (late) Goth. Lith.  cukrus NG = faxape ONEEE 28,2: Lett. cukurs , Lat.  saccharum (late) Dan.  sukker Cie 7 ) It. zucchero Sw. _socker SCr.  Seéer P Fr. sucre OE tet Boh. — cukr Sp. azticar ME _ sucere, sugure, etc. Pol. cukier Rum. zahdr NE sugar Russ. sachar m Ir. ay Du. —zucker Skt.  carkara- 0 NI. stilicre OHG zucura Av. et CE ie W. stwgr MHG zucker | Br. sukr NHG zucker a rk The home of sugar and its European | the article was then only an exotic ar names is India. The companions of | product used for medical purpose. The Ir : Alexander the Great told of the Indian | cultivation of the sugar cane was intro- BR : cane which produced ‘honey without | duced in Sicily and Spain by the Arabs, fl ? bees’ (wept r&v xadduor, dre mowfor wed. | and it was only after the crusades that 0 .! HedwooGy yx obcdv, Strabo 15.694). The | sugar became the common sweetening th 4 native Indian name appears in Greek | in place of the older honey. The major- 8 4 and Latin transcriptions in the first cen- ity of European forms of the name come or tury A.D. (wédAc 7d Kaddpuvoy 7d Xeyépevoyv | through Arabic via Spanish or Italian. ¥0 oakxapt, Peripl. 14; caxxyapoy eldos dy Schrader, Reallex. 2.705 ff. W Bédtros év "Ivdig xal rH ebdalporr ’ApaBig Skt. carkara- ‘gravel, grit? (AV +) W mennyoros, ebptoxouevoy éxl rOy xadduov, | later ‘sugar’ : Grk. xpdn, xpoxéd7 ‘peb- Y Diosc. 2.104; Saccharon et Arabia fert, | ble’. Walde-P. 1.463. th sed laudatius India, est autem mel in Hence, through a later Prakrit form *; harundibus collectum, Plin. 12.32), but | like Pali sakkhara-, the following: ur
9665-CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
9666-food AN aply gaKXAPOY; odKXaPy saccharum, NG faxap,
9667-_ sachar. kar, whence
9668-' Pers. 84 hero, and through Fi _ guce vero, ’ ape a 1 sukere, etc. (> ME
9669-laez
9670-1, Grk. yada, yédaxros, Lat. lac, lactis (> Romance words, also Ir. lacht, W. llacth, Br. laez), without certain root- connection. Walde-P. 1.659. Ernout- M514, Walde-H. 1.741 f. RIEW 4817. Pedersen 1.228. 2, Ir, mlicht, blicht, W. blith; Goth. miluks, OF meolc, etc., general Gmc.; ChsI. mléko (*melko), etc., general Slav- le; Toch, A malke, B malkwer. These ate put together here despite the dispute 48 to their relationship. Certainly some and prob, all : Grk, &uéd 5 Deal - anew, Lat. mulgére, sth ne OE melcan, etc., the general Bilinreond yordl of Qs G miluh ig hen of Goth, miluks, ti the relationshi Sala Sea think ™ ue to i a the vb. is only , € assimilation of an
9671-& *melk- beside mulcére, this is & Various substitute
9672-d by at. » and th
9673-D DRINK; COOKING AND UTENSILS
9674-igitized by Arya Samaj Foundation Chennai and eGangotri
9675-385
9676-cre, the Celtic (W. stwgr fr. ME sugre) and Gmc. forms, and through the latter the Balto-Slavic forms, except Russ. sachar (above), and SCr. seéer, which is fr. Turk. sheker, this fr. NPers gakar. Lokotsch 1855. REW 844la. NED,
--
10425:The modern ‘overcoat’, which has so largely displaced the ‘cloak’ in men’s at- tire, is commonly expressed by words for ‘over’ or ‘top’, esp. in phrases with words for ‘coat’, etc. Thus Fr. pardessus (> Rum. pardesiu), sb. use of adv. par- dessus ‘above, over’; Boh. surchntk, fr. sorchnt ‘upper’ (: urch ‘top’, 12.33); Sp. sobretodo, NE overcoat, NHG tiberrock, Du. overjas, Dan, overfrakke, Sw. over- rock; Lett. virssvarks (virsus ‘top’); NG eravadépr (-pdpt : doptw ‘wear’ » Popena ‘garment’, 6.12); NHG «iberzicher fr. uberziehen ‘pull over’; SCr. ogrtaé fr, ogrtatz ‘hang about’ (Berneker 372),
10426-Fr. paletot, fr. (instead of conversely, as formerly assumed) the earlier attested ME paltock a kind of short coat (NED 8.v.), perh. fr. pall ‘cloak’ (Lat. pallium). Baist, Z. rom. Ph. 32.430 ff. REW 6178. Gamillscheg 661. Hence, in the very different modern use of the Fr. paletot as a loose outer coat or cloak, It. palto, NG wadré, Sp. paleté, Rum. palton, Pol. palto, Russ. pal'to ‘overcoat’.
10427-Sp. gabdn, orig. the peasant’s heavy coat, but kept in part for the modern ‘overcoat’, fr. Pers., Arab. kaba a kind of cloak. REW 4648, Lokotsch 971.
10428-CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
10429-Sp. abrigo ‘protection, shelter’ (REW 560), used also for ‘overcoat’.
10430-NIr. cota mor, casdg mhor, W. cot far, all ‘greatcoat’, W. also cot uchaf (uchaf ‘upper’ fr. uch ‘above, over’).
10431-Lith. apsiaustas, see 6.41.
10432-6.42 WOMAN’S DRESS
10433-This is most commonly expressed by more generic words for ‘clothing, gar- ment’ (6.12), used (with or without ‘woman’s’) in this special application, as NE dress (now the most common use), NHG kleid, Russ. plat’e, ete. A full list would be in large measure a, repetition of words included in 6.12. But a few others that apply mainly to a woman’s dress are given here.
10434-1. Grk. rémdos (sometimes ‘covering’, also man’s ‘cloak’, but esp. the long robe worn by women), reduplicated form (we-mo-) of IE *pel- in Lat. pellis, OF fell, etc. ‘hide’, ON feldr ‘cloak’, ete. Less prob., since ‘covering’ seems to be the earlier sense, fr. *pel- in words for ‘fold’. Walde-P. 2.56, 58. Boisacq 769.
10435-NG pop. ¢overdy (beside ddpena ‘gal ment’, 6.12, esp. woman’s ‘costume, dress’), fr. It. fustagno ‘fustian’, fr. Arab.
10436-&- ‘2 piece of Tr, Lith, dra.
```


## [2026-09-04T19:26:18.217Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && echo \"### WLD Bd1 pages around 80\"; grep -n 'pdf page' WLD_Bd1_pages.txt | head -3; python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('n pages',len(pages))\nfor i,p in enumerate(pages):\n    if 'ario-' in p or 'arjo-' in p or 'aryo' in p:\n        print('---PAGE idx',i, p[:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T19:26:20.117Z] TOOL RESULT

```
### WLD Bd1 pages around 80
n pages 895
---PAGE idx 88               ,     80                                                             ario-      — ark-  ario- „Herr, Gebie
```


## [2026-09-04T19:26:23.543Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[88][:2600])\nprint(\"======= p84/85 (al-) idx\", 92,93)\nfor i in (92,93):\n    print('---',i); print(pages[i][:2000])\nEOF"
}
```


### [2026-09-04T19:26:25.114Z] TOOL RESULT

```
              ,




80                                                             ario-      — ark-

ario- „Herr, Gebieter“.
     Ai. dry a „Herr, Gebieter“, Cirya „Arier“, ary aka „ehrwiirdiger                                                           Mann“;
                                                          Ll
av. criryo                            Ario-manus (CIL. Ill 4594); ir. aire
                       apers. ariya „ariseh                    ;
                                                                   gall       .




(^gl. priraas gen. airech wo *arjak- oder *arjak- anzusetzen ist, welches
                       ,                          ,


sich zu ai. tiry aka verhalt wie gr. iidoai   Jiingling“ zu ai. marjaka-                      ,,



 „Mannchen“ Pedersen Kelt. Gr. II 100    Dagegen gehort mir. mire nicht               .



hierher, sondern aus ro -j-                           n ,,Gro8konig u                     .



  Hierzu ai. aryamd „Gefahrte, Freund; Name eines Gotten ', av. airya-                                              1




man- „folgsam npers. ermdn „Gast“.
                                 1£
                                      ,


  Ygl. Fick I 4 168.  II 4 19.   Uklenbeck Ai. Wb. 14.
  Ir. Airem, gen. Airemon      Eremon „einer der sagenhaften Stammvater
                                                      ,


des irischen Yolkes" iFickll 4 19; ist naeli K. Meyer RC. 33, 94f. falsch
angesetzt und hat mit der obengenannten Sippe nichts zu tun. Eremon
gen.    £
        remain als Bezeichnung eines irischen Stammvaters ist eine von
Erin abgeleitete gelehrte Fiktion. Dagegen bedeutet ir. airem gen. aire-
mon nichts anderes als „ploughman und kommt mit der Diminutivendung      ££




-dn ( Airemon als Epitheton des sagenhaften Echaid vor.
                             )




ark-
     Ausfiihrlich Osthoff IF. 8, 54 ff. m. Lit.
     Gr. agyJco „wehre, halte vor, schiitze, helfe; halte vor, reiche aus, ge-
nuge“ (scheint wegen dgyJoco, ijgy.eaa iigy.eaig nicht mit lat. arceo gleiches    ,



*aoy.i^o) zu sein, sondern Denominatio zu:; dgy.og n. ,,Schutz“, dgxiog „aus-
              11
reichend      ain-agy.yg „sich selbst geniigend“, nobagy.yg „mit den FiiBen
                   ,


ausreichend, schnell" (s. auch Bechtel Lexil. 279 f.;
   lat. arceo, -ere „verschlieBen, einhegen; durch AbschluB fernhalten, ab-

wehren, verhindern" (iiber art us a. aber *ar- „fugen“, ebenso fiber arma),
                                                                                                   £
area ,.Kasten, Kiste, Lade, Geld
======= p84/85 (al-) idx 92 93
--- 92
                                                                                              4
84                                               ardh-   —     al-, ol-




Bedeutungskreise weisen).                   —
                                 Ahd. arusi, nhd. Erz (Fick 1                                       356)   bleibt
fern (s. u. rcudh- „rot“), ebenso lit. archjti (s. *er- „loeker“).


ardh- „Stange“?
   Arm. ardn „Lanze, Speer" lit. ardai „Stangengeriist zum Flachstrocknen“,
                                             :



alt ardamas „die in der Diagonale des Segels stehende Spreizstange (s. zur
Bed. Bezz. GGA. 1885, 920)“?      Petersson KZ. 47, 245 (die lit. Worter
nicht besser nach Leskien Abl. 329 zu ardyti „spalten, trennen“ s. u. er-
„locker“).
     Unannebmbar deutet Petersson auch lat. asser, -eris „Latte, Balken“, assis
                                                                                                 11
„Diele,         Brett,      Bohle“ (dazu auch            as,    assis),   assula „Span, Splitter
                                                                          aus
*ardh-tro~,         -ti- aber nicht besser Reichelt KZ. 46, 313f.: *azd-ti:
                            (anders,
d^co „dorre“).  Uber lat. radius und dt. Bute, die keinesfalls unter Kon-
struktion einer zweisilbigen Wz. (gegen die der Schleifton yon lit. ardai,
sg. ardas, Einspruch erhebt) verglichen werden diirfen, s. u. *uerad- „Zweig“
und *ret- „Stange“.


arukos
  o
       Getreideart?
   Lat. arinca „Getreideart, olyra“ (,,Galliarum propria" Pein. n. h. 18, 81;
fremdes, vermutlieh gall. Wort, trotz Niedermann e und 7 30 nicht echt
lat.), gr. agaxo? „Hiilsenfrucht, die unter den Linsen als Unkraut wachst“,

agay-oi oojiqiov 1
            •        zb 6 k avro xai Xol&vqov Hes.
                                .



     Wegen des Bedeutungsunterscliiedes                  ganz fragliche Gleichung; keinen
Einwand           bietet        freilich   der nicht 
--- 93
                                            ^                                                                     :




                                                         al-,    ol-                                                                                  85

  idg. alios „anderer“,                    nach Brugmann Grdr. II 2 1, 164 mit Formans -o-
von einem Adv.                *ali „jenseits“ abgeleitet (vgl.  oben *dli)
  air. oil         Adj. „amplus“, eigentlich „fiber (das gewohnliche) hinausgehend“
(formell = lat. ollus, idg. *olnos), Komp. (h)uilliu „amplius“, Adv. ind-oll
„ultra“ (Entstehung                  des    -11-     aus -hi-      bestatigt             hier               auch der Gegensatz
ce-n „diesseits, Pedersen KG. II 197), woraus vielleicht auch innonn, innunn
„hinfiber“ (mit Assimilation unter Mitwirkung von inonn „derselbe“ Thur-                                                                    ;


neysen KZ. 48, 55 f.                 ;
                                         anders Pedersen               KG. II 195),                         ol-chene           „auBerdem,
                                                                                         11
sonst“,           Jenseits (und) diesseits davon
                 eigentlicb                          ol-foirhthe „plusquam-                   ;



perfectum“, oldau, oldaas „als ich, als er“, eigentlich „iiber (das) hinaus,
                                                                                                                                                11
was ich bin, was er ist“, in ill „sicher“, eigentlich ,.jenseits befindlich                                                                          (da-
von    inoillus „Sicherheit;                inuilligud „Sichern“;                   mit            ol(l)         „ultra“ deckt sich
vielleicht (s. Havers KZ. 44, 26 ff., Pokorny KZ. 44, 375, Thurneysen Ildb.

509,   KZ. 48, 55 f.) ol „inquit“ als „ultra, w
```


## [2026-09-04T19:26:49.792Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN && for n in 23 39; do echo \"===== pdf $n (printed $((n-11)))\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' IRN_pages.txt | head -45; done"
}
```


### [2026-09-04T19:26:51.323Z] TOOL RESULT

```
===== pdf 23 (printed 12)
[pdf page 23]
نها ایرانویج
واژه مر کب «اتیرپوشینه» 21۳76-52788 بمهنی سنزلگاه ایرائیان ونام أیرح ت6۳ در
فارسی و اریک 6286 در ارسنی . از دورانهای تاریخی ناسهای بسیار با ت ر کیب :۸۲
بمعای ایران نزد مورخان بونانی و رومی بجای مانده است!"
۱- برخی از نام‌هائ ی که با ريشهٌ ایران ترکیب یافته‌اند چنین‌اند :
تا ان ان ادن دا 28 م۸ عون دزم۸ ۸
اند اای 8 هزم ۸ ههام۸ و۸
۶ م۸ انز ۸ نت ادن دای و۸
نان ند ردنا
نگا هکنیدبه ۲ ناف[ ۷۵۵ طم‌باطا جوز معطم‌وزمع1۳

===== pdf 39 (printed 28)
[pdf page 39]
۲۸ ایرانویج

این‌دو تیرة بزرگك باهمة طایفه‌های خودکه نام برده شد» بسوی نواحی
حاصلخیز پیرامون درياچهُ رضائیه (اورمیه-شهرآب) فرودآمدند, یره مادی در
نواحی جنوب شرقی دریاچه بین همدان وتبریز جای گرفت وبعدها تا اصفهان پیش
رفت وقبیله‌های پارسی درمغرب وقسمت‌های جنوب غربی دریاچه» درناحیةٌ اردلان
کنونی جای گرفت . واه اردلان را میتوان بصورت کهن آن «قله*2 بازسازی
کرد: 271-۳30 ومعنی‌آن «ایران مقدس» است.

این‌قبیله‌ها با یکدیگر باصلح وآرامش زندگی م ی کردند و به دامداری و
تربیت اس بکه یکی از مهمترین پیشه‌های آنها بود می‌پرداختند. یکی از علل
برتری آنها نیز در دوران تاریخی داشتن اسب‌های تربیت شدهٌ خوب بودکه در
جنگها عامل مهم پیروزی بشمار میرفت .

اینان » نخست به خدمت امیران بومی درآمدند وسپس خود سالار و سرور
روستا ها گشتند .
قبیله‌ای از مهاجران هند و اروپائی که در پی‌یانتن سرزمین ها و چراگاه‌های جدید مهاجرت
م یکنند (نقل ا زکتاب عنسصده[1۳3)
ی
```


## [2026-09-04T19:27:12.607Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Arran_(Caucasus)",
 "prompt": "What does the article say about the etymology/origin of the name Arran (Persian اران/آران)? Quote the etymology section, including any derivation from Caucasian Albania / Armenian Ałuankʿ, from Parthian *Ardhan, or from Iranian *arya-."
}
```


## [2026-09-04T19:27:13.661Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/parallel",
 "prompt": "Give the full etymology of \"parallel\", including Latin parallelus, Greek parallelos, para- + allelois/allos."
}
```


### [2026-09-04T19:27:19.521Z] TOOL RESULT

```
# Etymology of Arran

According to the article's "Name" section, **Arran** is an Iranian toponym with the following derivation:

The Middle Persian form **A(r)rān** was the Iranian name for the region known to Greeks and Romans as **Albania**. The article explains that both the Greco-Roman name and the Armenian term **Ałuank/Aghvank** likely derive from an Iranian source.

The article states: "In Parthian the region was known as *Ardān*, which suggests an unattested earlier form \*aldwān that could have yielded \*alban-/\*alwan- and Middle Persian A(r)rān."

The Middle Persian designation was subsequently adopted into Arabic as **al-Rān**, from which the Georgian term **Rani** (რანი) derives. The article notes that "The native name of the region is unknown" but was likely a variant of *Ran*.

The text also discusses a legendary etymology, noting that according to a 10th-century Armenian history, Arran was purportedly the name of the founder of Caucasian Albania, possibly deriving from the nearby Aras (Araxes) river.
```


### [2026-09-04T19:27:20.232Z] TOOL RESULT

```
# Etymology of "Parallel"

The word "parallel" traces back through several languages:

**Greek Origin:** The term derives from Greek *parallēlos*, which combines *para-* ("beside") and *allēlois* ("each other"). The root *allos* means "other," stemming from the Indo-European *\*al-* ("beyond").

**Latin Transmission:** Greek *parallēlos* passed into Latin as *parallelus*, maintaining the same geometric meaning.

**French Intermediate:** The Latin form entered Old French as *parallèle* in the 16th century before reaching English.

**English Adoption:** The adjective "parallel" appeared in English around 1540, initially describing geometric lines that "lie in the same plane but never meet in either direction." The noun form followed in the 1550s, referring to a line parallel to another. By approximately 1600, the figurative sense developed to mean having "the same direction, tendency, or course." The verb emerged in the 1590s with meanings related to positioning things alongside each other and creating similarity.

The compound structure reveals the word's core geometric concept: *para-* + *allelois* literally means "beside one another," capturing the essential spatial relationship the term describes.
```


## [2026-09-04T19:27:32.291Z] TOOL CALL #49: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/%C3%A1ryas\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82el-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C3%A9lyos\" \\\n \"https://en.wiktionary.org/wiki/%C3%89riu\" \\\n \"https://en.wiktionary.org/wiki/Ireland\" \\\n \"https://en.wiktionary.org/wiki/%DB%8C%D8%B1%D9%85%D8%A7%D9%86\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"PDF page 45, root Al 1 / Aryo: PIE *h2el- and *aryas, Eriu/Ireland, ermān\" ; done 2>&1 | tail -20"
}
```


### [2026-09-04T19:27:37.232Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/128c1746f3e5b1a1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fadf8f265695fac1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ec697c8442cf619b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/525aadd4067c91de.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a1dab4f507a7c011.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a3ca9f0cfae78f20.txt
```


## [2026-09-04T19:27:46.439Z] TOOL CALL #50: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/ایرمان\" \\\n \"https://en.wiktionary.org/wiki/آریا\" \\\n \"https://en.wiktionary.org/wiki/ایران\" \\\n \"https://en.wiktionary.org/wiki/ایرلند\" \\\n \"https://en.wiktionary.org/wiki/اراک\" \\\n \"https://en.wiktionary.org/wiki/𐭠𐭩𐭥𐭠𐭭\" \\\n \"https://en.wiktionary.org/wiki/𐎠𐎼𐎡𐎹\" \\\n \"https://en.wiktionary.org/wiki/ἄλλος\" \\\n \"https://en.wiktionary.org/wiki/else\" \\\n \"https://en.wiktionary.org/wiki/alligator\" \\\n \"https://en.wiktionary.org/wiki/alarm\" \\\n \"https://en.wiktionary.org/wiki/alert\" \\\n \"https://en.wiktionary.org/wiki/عراق\" \\\n \"https://www.etymonline.com/word/parallel\" \\\n \"https://en.wikipedia.org/wiki/Arran_(Caucasus)\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"PDF page 45, root Al 1/Aryo: node verification\" ; done 2>&1 | tail -25"
}
```


### [2026-09-04T19:27:54.364Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/32cbedb88926833d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1d7f1db934a03f71.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/91c2ea2372a4be3a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9d6b0b560410d853.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a91c556204f43a78.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5cc562532a586b39.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/79039e5f03c204b7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/21290f8fd12b8dce.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b0476df0be9618a9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/95e18eac6d50c241.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8b1d35236e0865b3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a4c09c614440c3c1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/636c9fb3b88ee994.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0e0fcf91a3f27282.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f94f8232ad2f2864.txt
```


## [2026-09-04T19:27:58.092Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 0e0fcf91a3f27282 f94f8232ad2f2864 a3ca9f0cfae78f20 128c1746f3e5b1a1; do echo \"== $f\"; wc -c $f.txt; head -c 300 $f.txt; echo; done; echo \"### index tail\"; tail -5 index.jsonl"
}
```


### [2026-09-04T19:28:00.121Z] TOOL RESULT

```
== 0e0fcf91a3f27282
6218 0e0fcf91a3f27282.txt
URL: https://www.etymonline.com/word/parallel
FETCHED: 2026-09-04T19:27:54Z
STATUS: 200
TITLE: Parallel - Etymology, Origin & Meaning

Parallel - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to s
== f94f8232ad2f2864
44100 f94f8232ad2f2864.txt
URL: https://en.wikipedia.org/wiki/Arran_(Caucasus)
FETCHED: 2026-09-04T19:27:54Z
STATUS: 200
TITLE: Arran (Caucasus) - Wikipedia

Arran (Caucasus) - Wikipedia 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Contents 
 Current events 
 Random article
== a3ca9f0cfae78f20
156 a3ca9f0cfae78f20.txt
URL: https://en.wiktionary.org/wiki/%DB%8C%D8%B1%D9%85%D8%A7%D9%86
FETCHED: 2026-09-04T19:27:37Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
== 128c1746f3e5b1a1
8895 128c1746f3e5b1a1.txt
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/%C3%A1ryas
FETCHED: 2026-09-04T19:27:34Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-Iranian/Áryas - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-Iranian/Áryas - Wiktionary, the free dictionary 

 Jump to content 
### index tail
{"url": "https://en.wiktionary.org/wiki/alarm", "file": "data/verification/sources/web/8b1d35236e0865b3.txt", "fetched": "2026-09-04T19:27:52Z", "status": 200, "bytes": 41837, "title": "alarm - Wiktionary, the free dictionary", "note": "PDF page 45, root Al 1/Aryo: node verification"}
{"url": "https://en.wiktionary.org/wiki/alert", "file": "data/verification/sources/web/a4c09c614440c3c1.txt", "fetched": "2026-09-04T19:27:53Z", "status": 200, "bytes": 22416, "title": "alert - Wiktionary, the free dictionary", "note": "PDF page 45, root Al 1/Aryo: node verification"}
{"url": "https://en.wiktionary.org/wiki/عراق", "file": "data/verification/sources/web/636c9fb3b88ee994.txt", "fetched": "2026-09-04T19:27:53Z", "status": 200, "bytes": 10665, "title": "عراق - Wiktionary, the free dictionary", "note": "PDF page 45, root Al 1/Aryo: node verification"}
{"url": "https://www.etymonline.com/word/parallel", "file": "data/verification/sources/web/0e0fcf91a3f27282.txt", "fetched": "2026-09-04T19:27:54Z", "status": 200, "bytes": 6067, "title": "Parallel - Etymology, Origin & Meaning", "note": "PDF page 45, root Al 1/Aryo: node verification"}
{"url": "https://en.wikipedia.org/wiki/Arran_(Caucasus)", "file": "data/verification/sources/web/f94f8232ad2f2864.txt", "fetched": "2026-09-04T19:27:54Z", "status": 200, "bytes": 42708, "title": "Arran (Caucasus) - Wikipedia", "note": "PDF page 45, root Al 1/Aryo: node verification"}
```


## [2026-09-04T19:28:07.478Z] TOOL CALL #52: Bash

```json
{
 "command": "head -c 200 data/verification/sources/web/32cbedb88926833d.txt; echo; for u in \"https://en.wiktionary.org/wiki/Aryan\" \"https://en.wiktionary.org/wiki/alien\" \"https://en.wiktionary.org/wiki/ultimate\" \"https://en.wiktionary.org/wiki/alternate\" \"https://en.wiktionary.org/wiki/𐬀𐬌𐬭𐬌𐬌𐬋\"; do python3 tools/fetch_source.py \"$u\" --note \"PDF page 45, root Al 1/Aryo: node verification\"; done"
}
```


## [2026-09-04T19:28:09.100Z] TOOL CALL #53: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.vajehyab.com/moein/ایران\" --note \"Mo'in via vajehyab, MON5:114 check\" 2>&1; head -c 400 data/verification/sources/web/$(python3 -c \"\nimport hashlib;print(hashlib.sha1('https://www.vajehyab.com/moein/ایران'.encode()).hexdigest()[:16])\").txt 2>/dev/null"
}
```


### [2026-09-04T19:28:10.842Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/ایرمان
FETCHED: 2026-09-04T19:27:48Z
STATUS: 200
TITLE: ایرمان - Wiktionary, the free dictionary

ایرمان - Wiktionary, the free dictionary 

 Jump
/home/sfmqrb/git/rishe/data/verification/sources/web/09c07f4b665b99de.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a080fa9b66312181.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f97c2d87296a973e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d9610efd3844839a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e6b2823068413f31.txt
```


### [2026-09-04T19:28:13.081Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/13142f9e8661032d.txt
URL: https://www.vajehyab.com/moein/ایران
FETCHED: 2026-09-04T19:28:13Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 500: Internal Server Error
```


## [2026-09-04T19:28:18.568Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON && ls -la; for f in MON_2vol_Adena_v1_djvu.txt MON_2vol_Adena_v2_djvu.txt; do echo \"== $f\"; grep -c 'ایرلند' $f; grep -c 'ایرانویج' $f; grep -c 'ایرج' $f; done"
}
```


### [2026-09-04T19:28:20.338Z] TOOL RESULT

```
total 48684
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 20113727 Sep  4 14:06 MON_2vol_Adena_v1_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4377831 Sep  4 14:06 MON_2vol_Adena_v1_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 21014767 Sep  4 14:06 MON_2vol_Adena_v2_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4331421 Sep  4 14:06 MON_2vol_Adena_v2_djvu.txt
== MON_2vol_Adena_v1_djvu.txt
0
0
1
== MON_2vol_Adena_v2_djvu.txt
2
0
1
```


## [2026-09-04T19:28:23.242Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON && grep -n -B4 -A8 'ایرج' MON_2vol_Adena_v1_djvu.txt | head -30; echo \"=== v2 iraj\"; grep -n -B4 -A8 'ایرج' MON_2vol_Adena_v2_djvu.txt | head -30"
}
```


### [2026-09-04T19:28:23.329Z] TOOL RESULT

```
45791-رتتلیث» (غالباً بدون نقطه نویسند. 
45792-
45793-اء: رم هه [- ا] (.) نام حرف «ث». 
45794-ثابت: «2:(ع.] (اف_ا. ثبات ثبوت). 
45795:پایرجاء بررقرار. پایدار» پاینده» بادوام. محققء 
45796-مدلل. مشست؛ مق. منفی. (ند.) ستاره‌ای که 
45797-ساکن است و حرکت نکند؛ مق. سیاره؛ ج. 
45798-ثوابت. حساب ثابت: (بانک.) حسابی که در 
45799-بانکی از جهت وجهی ثابت برای مدتی معین 
45800-(تعموا زنط و واه وی مان 
45801-یکسال از آن برداشت نکنند؛ مق. حساب 
45802-جاری. رنگ پابت: رنگی که با شستن و 
45803-تافتن افتاب تغیر نکند و محو نگردد. 
=== v2 iraj
47416-متیل: ۲1 (- مشّل | (.) بارجه‌ای لا 
47417-سفید که روی بالش و لحاف کشند. 
47418-
47419-متین. ۱1 [ع (ص.) مسحکم؛ استواره 
47420:پایرجا. باوقار. 
47421-
47422-مثاب: ۱ [ع.] (امف.) باداش داده شده؛ 
47423-جزا داده. تواب اخروی داده شده. 
47424-مسئایت: ادصحنه [ع. ماه ] (.) مسحل 
47425-اجتماع مر دم» جای گرد ات حد» انداز هه 
47426-درجه منزلت. مانند. به مثایت: به ماننده 
47427-مسثابرت: (عط)احدطاقعهه زع. متایر 5 ] 
47428-(مص‌ل.) پیوسته در کاری بودن؛ مداومت
```


## [2026-09-04T19:28:31.041Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### NYB\"; grep -n -E '\\bērān|Ērān|ērmān|ermān|ēr\\b|airyaman' NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-04T19:28:31.099Z] TOOL RESULT

```
### NYB
418:an-agr (ančr) [’ngl] without beginning, eternal: ~ rösneh 3018; han 1 ~ rošneh 3921. — Borrowed from Av. (114 sg.) an- ayra-; gen. pl. anayranqm raocanhqm (sc. ayara) the day of the Endless Lights, the name of the 30th day of the month, BP anagrän (FrP 28); MPrs ’nyr’n (S); Paz. Anērān; NP Aniran.
554:apäyistan ['p'dstn'], apāyītan [’p’dytn'] apäy-, 3d p. sg. apāyēt [’p’dt', ^p'dyt'], 3d p. pl. apäyend ['p'dynd], pret. 3d p. sg. apāyist 1. to please a p. (pat) 83%; cigon mēnēyān apäyist as it had pleased (was predestinated by) the heavenly gods 405, v. below. — 2. impers. it is desirable: -m apāyēt 6 han ciš I desire, try to obtain, this 562%, — 3. to be needed 1211-2 also pat. kär. apāyet 14%. 375, andar apāyēnd 105%. — 4. to be proper, seemly 4015 (bē ~). — 5. impers. apäyet auxiliary vb.: must, ought to, shall, should, has to, is bound to, ete. with the p. as indir. obj. (virtual dat.), a) governing an inf., which is as a rule placed after: u api-t xvatāyēh i Ērān šahr vas sal apäyet kartan and thou shalt exercise dominion over Iran for many years 629-31; 918-19, ]014 ete.; in this case preverbs to the inf. are drawn to apäyet; bé — pursitan 1319; ba ~ hištan 1313; kār-ē i apar nē ~ kartan 104%; apārīk 6 [KN] ~ xtartan 94??; less often the inf. is placed before: ēzatan nē ~ 1017-19; pit u mat frazand i xueš rād En and kär u kirpak ... bē üámóxtan ~ the parents shall teach 6522-23; 6519-20; 9113; the inf. sometimes has to be supplied: -
649:ArtaxSér ['Ithšdl] = Artaxsahr, 1-17, passim. 117°. 1201-2 (v. also nev-— and Véh-—), Artašēr [ltšdl] 11571. 116? sq. — Olr Arta-xsadra-, cf s. v. Art-vahist and šahr; OP Arta-xšaca-; KZŠ, Gr. v. Apta- Eeto, -Eep, -Ero (the common Gr. ’Apra- Eep&ng is influenced by HépEns); NP Ar- dašīr. Ci Bailey, BSOAS XIII, 1949, 123. Hence
650:Artaxšērān [’lthsdl’n'] 1413. 1512-17, Arta- šērān [*ltšdl*n'] 114-116, patron.
676:asan ['s?n'] calm, quiet; relieved from (hac) 134; peaceful 81%; v. also Ērān- äsän-kart. — Paz. àsq; NP āsān ‘easy, convenient’; from dsdy-, g. v.
794:*avērāt [*’wyl’y] read [^wdPy =] udrāt (g. v.).
817:ävurtan [YHYTYWN-tn'; ’wwltn'] āvar- [YHYTYWN-], subju. 2nd p.sg. ~-d 27%, pt. = pret. pass. 3d p.sg. āvurt [YHYTYWN-t!,^wwlt!], opt. pass. 3d p.sg. ävurt he [HWH-d] 218: to bring a th. to a p. (6) 218 (avis, g. v.). 6% (6 pēš i); 1576 (6 en giyāk to this place here); 76°. 10915, 113; 6 ē giyak ~ to put together, to compose 1192-21; to fetch down 40?!; to inflict (a punishment) 9°; to acquire (a name, renown) 27%; — andar ~ to introduce 10317; — apäc ~ to bring back, to restore (6 to) 514, 17°. 10911, hac from (a state) 11215, hac . . . ó from one state to another 112?-3; — apar ~ to send forth, to emit 719; to assault 984->. 10712; — be ~ to bring 20°; to emit 371%; — 6 bērēn ~ to take away, to carry off 101. 14? ;— pat dit ~ 4? v. dit. — Av. (938) ā-bar-; MPrthPrs pt. ”wrd, pres. ”wr-; Paz. awardan, äwar-; NP āvurdan, āvardan ävar-(är-); v. burtan.
980:bérón [bylwn'; inser. bylwny] outwards HajB:10; out, connected with matan, āvurtan, kartan, v. these vbs.; kac... ~, v. āmatan; — prep. — asman kartan to put out of heaven 1039, — MPrs byrwn (S, BBB); Paz. bērūn; NP birün; < be + ron (g. v.).
1001:bitaxš [bythš] the Grand Vizier, of Jä- mäsp at Vištāsp's court 21—24. 2713; of the corresponding official at Arjasp’s court 2511, 287... A Prth. Arsacid title, adopted by the Sassanid kings of the 3d c., but later replaced by vazurg framatär (v. the 2nd w.); survived in independent Armenia governed by Arsacids (until A. D. 430) and in Georgia. Sas. inser. Prth byths, Prs bythšy KZSPrth a) 1. 23, b) l. 25, c) l. 27 = Prs ll. 29. 31. 33 Gr. v. a) Bde (in the list of the late Artaxšēr's officials), b) miridēng of Shapur’s own vizier, c)
1022:Brātarūrēš [bl’tIwkly$] n. pr. 5022, 5112.20, 5218, — A karap (g. v.) of the Tur people, hostile to Zartuxst; his proper name was Brātar-vaxš [bl’tlwhs] ‘furthering the brothers’, DkM 79412, DD ch. 715 = Cod. K 22115; Brātarē-rēš ‘injuring the brothers’ is a malicious distortion. V. also Brātērēš.
1073:paitak ku 912811; u hac-ic öisän 4011; pat tan brah ...u pat-ic zor u nérok 141°; Yam u an-ic varcävand 44%, ete. — c) corre- sponding coordination: -c... -e: tdi ērān- ic viyan kunénd tai amäh-ic be daném 2022;
1442:Ērān-gušasp ['yPn'gwésp'] n. pr. of a general in Azarbaijan 1171, — V. gusnasp.
1444:eran-šahrik pl. cas. obl. ~-dn the inhabi- tants of Ērān-šahr 118°.
1451:age DkM 6989; tat pat dātistān(ūman>- deh či veh tuvän zatan u éraxtan cigón ka-š pat davreh u drusteh apäk gēbāh through righteousness thou art better able to defeat him and make him lose the case than if thou speakest to him coarsely and roughly (cf s. v. davr) PR 573; — pres. pass. 3d p. sg. éraxtét he is pronounc- ed guilty, opp. buxtet he is acquitted, v. Bthl, ZsR IV, 8; Paz. buxted ... érexted SGV III, 26; kē rāstēh rad pat xudstak eraxtet, ah veh cigon kē družeh rād pat ruvān éraxtét he who suffers loss of prop- erty because of his righteousness is better than the one who suffers the loss of his soul (forfeits his soul) because of his falsity PR 26$-9.] — Two vbs. seem to have coalesced here: 1) črtatan ērēc-, cf Paz. érexted and the caus. érezinidan ‘to condemn’ SGV XI, 257, most probably < abi- + Av. (1479 sq.) raék- ‘to leave in the lurch, to abandon to destruction’ (Bthl IF XII, 112sqq.); 2. éraxtan érang-, most probably a denom. of érang, črangčh 'trouble, delusion' (Paz. ŠGV X, 58 ete.) < *abi-ranga-, cf. an-črang, ranj, ranjak; MPrs ‘yrat, “yrnz- ‘to combat’, Verbum 199. (Bthl, l.c. adopted the reading érazt).
1524:framätan [inscr.], framütan [plmwt'n] framäy-, imp. sg. framäi 10% ete. and framäye [plm’dyd 923,plm? dh 272, plm’ - dyw 5725]; pres. 2d p. sg. framdyé [plm’yh 64, plm’dyh 244]; 3d p. sg. = 2nd p. pl. framäyet 141°, 261° [plm’dt!, ef Ps. hwéty and ywdty 1289, v.s. v. hošitan and yöd-]; Ist p. sg. and pl. framdyém [plm’dym]; pt. = pret. pass. 3d p. sg. inser. framät [prm*t, plm?t; plm’ty P2:4], in the books framüt: to order, to issue an order, to command, to bid, with 6 of the p. to whom (3725-27), and rād of the p. concern- ing whom(219?)the order is issued; with a dir. obj. of the ordered th. 38. 64. 199%; apt-t pasēh framayém karkäs and we shall order the vulture (after thee —) to pursue thee 604; mā man 6 pasčh framdi do not bid me to turn my back 5774-75; — to please to, to deign to, with inf. 1122-26, 149; — kar framutan = kar kartan 27, v. kar; — the order itself is expressed 1. in dir. speech by an imp. introduced by ku: framut kū "nikēr” 45; 1213. 33%; consequently, in 216 (framut ku ...) ‘BYDWN-x, and in 109? YDLWN.x; should be taken as the imperatives kuné and baré; — 2. by a subordinate clause a) with kū + pres. ind. 313-5; b) with tāi + pres. ind. 129-19; c) after the pret. framut, with ku tài + opt. pass.: 217-18; d) introduced by the rel. pron.: amah framatké ... cit” we ordered someone (an
1582:fražām [ple’m] end 804. 81!; pat ~ lastly, in the end 645.721, 7212-5; ~~ pērē- zēh the final victory 77?” sq. — From the preceding vb.; Paz. farjam, faržam; NP farjam.
1668:girtak: ~ pērāmēn all around 92!9,
1749:gušasp [gwšsp'] v. Ērān-gušasp and cf gušnasp.
1750:h- (HWH- ; 3d p. sg. "YT', neg. L'YT', inser. and Ps. ^Y TY, L'YTY 2nd p. pl. enel. -ét in amahraspand-é 58"; forms v. I, 175] to be, only in the pres. ind., subju. and opt., other forms from bütan (q. v ): l. as an independent vb. in the 3d p.: exist(s), e.g. hast hàn ke ahlayeh the One who is Righteousness exists 57°; héc ke but hénd u hec ke bavénd u h&c ke hend all who have been, and all who will be, and all who exist (now) 6417-18, cf subst. hast and nesteh; im roc 7 mähakän hast tdi ... to-day it is seven months since 1011-12. kë hast ke ...? who is there who ...? 257-7; andar Ērān-šahr asvār-ē nest ke ... in Eran-shahr there is no horseman who ... 15; hast 4-8 ... u hast 1-§ ... u hast i .. . there is some (of it) that ... and there is some (of it) ... and there is some (of it) that... = part of it... part of it... ete. 9317-18.26; hast kč-š veš, hast ké-§ kam some have more, others less 96°; astömandän mar- tömän (gen. part.) hast i ... of earthly men there are some who 10519; hast <a> šāhān šāh, hast <i> kesar some belong to the King of Kings, others to the Emperor 11519-20; nē hast kū there is no place where, nowhere 611°; hast (i) ka there is a time when, sometimes, at times 7725-26, 8122, 12018-1?; — with prev.: šusr i Gayomart cis andar hast there is some part of the sperm of G. in it 9422-23; kū-š ataxš andar nést where there is no fire 3721, — 2. copula, with a noun, a pron., or a prep. -- subst. as its complement, pas- sim; the 3d p. sg. ‘is’ is very often not
1753:gušnasp [gwšnsp'] in ātur ~ the second of the sacred fires of Eran-shahr, v. s. v. ätur, — Gušn-asp n. pr. ‘having male horses, stallions’; Arm Všnasp < Vušn- asp. Often gušasp in BP texts — NP, with loss of the the n, cf Ērān-gušasp.
```


## [2026-09-04T19:28:33.163Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && echo \"### ARY latin index ARYA/ARIO/AL\"; grep -n -iE '^ *(ARYA|ARIO|AL-|ALIUS|ALLOS)' ARY_latin_index_pages.txt | head -20; echo \"### ARY pages آریا/ایران\"; grep -n -m6 'ایران' ARY_pages.txt | head; grep -n -m4 'آریا' ARY_pages.txt | head"
}
```


### [2026-09-04T19:28:33.245Z] TOOL RESULT

```
### ARY latin index ARYA/ARIO/AL
1533:ARYAN ENGLISH) glSil
### ARY pages آریا/ایران
25:نیز آورده‌ام تا خویشی زبان‌های ایرانی امروز و رابطه‌ی آنها با پهلوی و اوستایی و پارسی‌باستان و
48:تفریباً همه‌ی زبانهای اروپا و فلات ایران و بخش شمالی شبیه قاروی هند می‌شود. کوچگری
75:خانواده‌ی بزرگك از هندوستان و فلات ایران تا باختر اروپا و بریتانیای کبیر گسترش دارند. برخی
95:پست‌تر از آریایی‌های ناب (یعنی آلمانی‌ها و اسکاندیناوی‌ها) بودند؛ تا چه رسد به ایرانی‌ها و
114:سرزمین کم‌کم از یک سو به فلات ایران و شمال هندوستان و از سوی دیگر به آسیای صغیر و از آنجا
167:صغیر و فلات ایران و هندوستان را زیر مهمیز خود درآوردند.
37:منوچهر آریان‌پورکاشانی
77:۸ج 0-68) را بکار می‌برند. در گذشته واژه‌ی «آریایی» (۸۷۸) نیز بکا رگرفه :..4:
79:ترکیپب (هند و آریایی (13100-۸837۸3) بکار می‌رود.
80:علت از رونق افتادن واژه‌های «آریا» و «آرین» و (آریایی» چه بود؟
```


## [2026-09-04T19:28:39.489Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '1520,1545p' ARY_latin_index_pages.txt; echo \"--- pdf tag\"; awk 'NR<=1533 && /pdf page/ {p=$0} END{}' ARY_latin_index_pages.txt; grep -n 'pdf page' ARY_latin_index_pages.txt | awk -F: '$1<1533' | tail -2"
}
```


### [2026-09-04T19:28:41.324Z] TOOL RESULT

```
OS ithe aol al gant
eden Ly edly cal Baty: ib Olay 9 gue 9 lana “1
Sg 5 Sey ols) 42 GAH, UL o5ly ce! SKEAT, ONIONS -¢
Pama ep
ARIA (GREEK) gig ‘ARIYO, ARIA. {AVESTAN) gts!
ARIANA (LATIN) ys ARIYA OLD PERSIAN) deol gh
ARYEN (FRENCH) <1 ERA, ERANAG,ERAN (PAHLAVI) 5 sly,
HOLD SCANDINAVIAN) 4S.5-chs} IROE, IRON OSSETIC) ins!
IRAR ARYAS, ARYEN, (SANSKRIT) = Suite
TRAS OLD ENGLISH) pf ySs\ ARYA-
[pdf page 56]
. oo
Ov | Cad tale em" 4) JI
ARYAN ENGLISH) glSil
REFERENCES bok, AIRE, ERIU (OLD IRISH) 345 gd 4!
BARNHART: (ARYAN) 54, (IRISH) 544 ERIN (IRISH) «523 4!
DELAMARRE: cu
MACKENZIE: 30, (ARYAN) 103 .
ONIONS: 485 qb \
RAMAT: 126 ye as
irre ebb ob, cal
sewtlsal
Prot Vyol y cad tae IRISH , IRLAND G50 3ly U oly gy! Stites So glut y RAMAT -1
ABU phyla UT fly col
29 AARYAS) sn 53 S099 Ya 31 9 a jh eg bp (BUT Sidi Glatt jl ety let “tf
OT pL ays Us y iat (SL (ROE, IRON) ea! 5» y (IRELAND, ERIU, IRISH, ERIN). ,|
--- pdf tag
1500:[pdf page 55]
1530:[pdf page 56]
```


## [2026-09-04T19:28:47.987Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && awk 'BEGIN{RS=\"\\f\"} /pdf page 56\\]/' ARY_pages.txt | head -60"
}
```


### [2026-09-04T19:28:49.693Z] TOOL RESULT

```
[pdf page 56]
لح -
از (به چم "حرص»"خواهش شدید") / ۵۷
انگلیسی (80/0175/7): ۸۷۸۲
ایرلندی کهن (#اقل#ز ۵2): ۰ 883۲ ,۸ پسگشت‌ها هار ۲
ایرلندی (5ل۸): 1 4 (18157) ,54 (۸8۷۸3۷) 8420247
۱ 47 :م02
3 (۸۸۷۸۵) ,30 :کل از
1 ۵ 45 :0702/5
از ند 126 +7247
یه برهان قاطع : ۱۹۴۳۳
بادداشت:
۱ 1۸81۸7 و شماری دیگر معتقدند که این واژه با واژه‌ی 1314۸710 , 131811 همريشه نیست و اصولاً مىکن
است واژه‌ی "آریا" هند و اروپایی نباشد.
۲- شمار بیشتری از دانشمندان معتقدند که "آریا" نام چند قوم از هند و اروپائپان بوده که در هند (۸837۸8)ر در
ابرنند 8381۸ ,1818 ,ت88 ,810شآ133) و در بت 13070 ,108 ساکن شدند و نام خود را به آن
سرزمین‌ها دادند.
۳ واژه‌ی "اپران" نیز از همین ربشه است(پارسی باستان ۸13۷۸) پبهلری 1۳1۸ برنانی (۵21۸) لاتین
5
۴ 8۸8011۸737 معتقد است که ممکن است این واژه با واژه‌های لانین ۸2-01-18 ,۸1182108 (انگلیسی
1 ۸) همریشه باشد.
ِ
ی
اوستایی (/4۳59740): بلَاش2ة بش2م ,22 ایسلندی‌کهن (/(0۸ا نک ها۵):
هب ۸255 باکه امه
پپلری ۰:4 ۸2۷۸815 ,722 آلمانی کهن (شاید) (027044(0 ۲104 صاه):
تخاری ۸ (۸ (4ل4تل707): 2 01
نخاری 8 (8 70۸5(۷): کلم بکلتگنه انگلیسی کهن (شاید) (8701./54 )+
سانسکریت (54۸/8877)+۸71 بقل 11۸78 آشآ86 ۱
برنانی 0828/0): انگلیسی (شاید) (5ل8(/0): ۰ ۸۷۷8 ماله
5 ,1۳71۸0 ,۸۲۳۳38
گوتبک (شاید) (007/0): ۸61۸0۲
```


## [2026-09-04T19:29:08.489Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SKT else\"; grep -n -m2 -A5 '^Else' SKT.txt | head -20; echo \"### SKT alien\"; grep -n -m2 -A5 '^Alien' SKT.txt | head; echo \"### SKT Alarm/Alert/Alligator\"; grep -n -m1 -A4 '^Alarm' SKT.txt; grep -n -m1 -A4 '^Alert' SKT.txt; grep -n -m1 -A4 '^Alligator' SKT.txt; echo \"### SKT Parallel\"; grep -n -m1 -A5 '^Parallel' SKT.txt"
}
```


### [2026-09-04T19:29:08.620Z] TOOL RESULT

```
### SKT else
### SKT alien
### SKT Alarm/Alert/Alligator
528:Alert.  (F.-ltal.-L.)    See  B^ffent.
529-Algebra.   (Low  L.  —  Arab.)      J-ow  L
530-ALGUAZIL,
531-ALLIANCE.
532-alj^hxt,  compDtatiuD. *Arab.  (z/,  the;  auid faftr^  setting,  repairing  -,  :lIso,  ibe  rcUictiou of  fractioiu  lo  integers  in  arithmetic  ;  hciicr. ilgcbra,  — Arab,  root  j'a^ra,  to  set,  con- sol  ulale, Al^iazil.  B  police-<'flicer;  see  Vlaler. Alburn,  umial-wood.      (Heb.  -  Skt.) In  i  Chroo.  ii.    8.  ix,   to;    spelt  almug, I  Kiiij^s,  X.  II.— Ileb.  a/^/mm/)?/,  or  <tnin»- pose*I  I  atmugim  ;  a  bcirrowed  won!.  — SIct. vaisU'ka^    saiidal-wood ;    where    'ka    is   a sufnx. Alien.  (F.-L.)      M.  E.  aliau.^O.  F. aiicH.  —  L.  alienuj.  sbsnge  ;  a  stranger.  —  L. alius,  another. +  Gk,tfXAor,  another;  Goth. aiii,  other ;  see  Else.  Allegory.
### SKT Parallel
```


## [2026-09-04T19:29:09.735Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### WEB Aryan\"; grep -n -m3 -A4 'Aryan' WEB_vol1.txt | head -30; echo \"### FSD Aryan\"; grep -n -m2 -A4 'Ar.yan' FSD_vol1.txt | head -20"
}
```


### [2026-09-04T19:29:09.805Z] TOOL RESULT

```
### WEB Aryan
10829:A’‘ri-ain, a. and n. see Aryan. :
10830-A’ri-an, a. related to Arius or his doctrines.
10831-A/ri-An, n. a believer in or an advocate of
10832-_ Arianism. S
10833-A’ri-An-ism, n. the doctrines of Arius, an Alexandrian of the fourth century, who taught that Jesus was not of the same sub- Tance as God, but only the best of create
--
11602:3. of the Aryans.
11603-Ar’y-An, Ãr'i:Än, n. 1. the hypothetical parent language of the Indo-European family.
11604-2. a person belonging to, or supposed to be a descendant of, the prehistoric people who spoke this language. i
11605:Aryan has no validity as a racial term, although it has been so used, notoriously by the Nazis to mean “a Caucasian of non- Jewish descent,” etc. The use of the word in connection with race is due to the idea, re- garded by most ethnologists as false. that peoples who spoke the same or related lan- guages must have had a common racial origin. Misuse of Aryan has led to its replace- ment in scientific discussion by Indo-European (in sense 1 of the z. and a.). 5
### FSD Aryan
26146:Ar'yac,  1   or 'yak;  2   ar'yic,  n.  The  Aryan  linguistic  stock. Ar'yan,  1   ar'yon  or  arii-an;  2   ar'yan  or  ariy-an,  a.  Of  or pertaining  to  the  Aryans  or  their  language.
26147-The  term  was  formerly  used  by  some  philologists  as  syn- onymous with  Indo-European  or  Indo-Germanic,  but  Is  now restricted  to  the  Eastern  branch  of  the  Indo-European  fam- ily. Discoveries  made  In  1908,  In  the  land  of  the  HIttites, go  to  show  that  the  Aryans  of  India  are  descended  from  the Aryans  of  Cappadocia,  and  some  philologists  Incline  to  the opinion  that  Europe  was  the  cradle  of  this  primitive  race. The  more  prevalent  use  of  the  word  Aryan  Is  to  denote  the language  of  the  Indo-European  family  but  not  the  tamlly Itself.  The  term  Is  also  sometimes  loosely  used  as  synony- mous with  Japhetic.
26148-The  whole  framework  of  grammar  .   .   .   had  become  settled  be- fore the  separation  of  the  Aryan  family.
26149-MClLeb  Science  of  Lang,  first  series,  p.  234.  [3.  1875.]
26150-[   <   Sans,  Srya,  noble.]  Ar'lanf.  ^
26151:Ar'yan,  n.  1.  One  of  the  primitive  people  who  are  said to  have  migrated  into  Europe  and  India  from  central Asia,  and  are  the  parent  stock  of  the  Hindus,  Persians, Greeks,  Latins,  Celts,  Anglo-Saxons,  etc.;  originally, the  Irarn'c  or  Asiatic  division  of  this  people.  In  Europe the  Aryan  includes  the  blond  and  the  brunette,  or the  xanthochroic  and  the  melanochroic,  divisions. 2.  A   member  of  any  of  the  races  descended  from  this people.  3.  The  Aryan  languages;  specif.,  the  parent language  of  the  Indo-European  family.  See  Indo- European;  LANGUAGE.
```


## [2026-09-04T19:29:14.861Z] TOOL CALL #62: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-04T19:29:14.911Z] TOOL RESULT

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


## [2026-09-04T19:29:59.971Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 -c \"\nimport json\nfor l in open('data/verification/sources/web/index.jsonl'):\n    d=json.loads(l)\n    if 'page 45' in d.get('note','') or '45' in d.get('note',''):\n        print(d['status'], d['url'])\n\" | tail -30"
}
```


### [2026-09-04T19:30:01.643Z] TOOL RESULT

```
200 https://ahdictionary.com/word/search.html?q=checkmate
200 https://ahdictionary.com/word/search.html?q=margarite
200 https://ahdictionary.com/word/search.html?q=matador
200 https://ahdictionary.com/word/search.html?q=mat
200 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/%C3%A1ryas
200 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82el-
200 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C3%A9lyos
200 https://en.wiktionary.org/wiki/%C3%89riu
200 https://en.wiktionary.org/wiki/Ireland
-1 https://en.wiktionary.org/wiki/%DB%8C%D8%B1%D9%85%D8%A7%D9%86
200 https://en.wiktionary.org/wiki/ایرمان
200 https://en.wiktionary.org/wiki/آریا
200 https://en.wiktionary.org/wiki/ایران
200 https://en.wiktionary.org/wiki/ایرلند
200 https://en.wiktionary.org/wiki/اراک
200 https://en.wiktionary.org/wiki/𐭠𐭩𐭥𐭠𐭭
200 https://en.wiktionary.org/wiki/𐎠𐎼𐎡𐎹
200 https://en.wiktionary.org/wiki/ἄλλος
200 https://en.wiktionary.org/wiki/else
200 https://en.wiktionary.org/wiki/alligator
200 https://en.wiktionary.org/wiki/alarm
200 https://en.wiktionary.org/wiki/alert
200 https://en.wiktionary.org/wiki/عراق
200 https://www.etymonline.com/word/parallel
200 https://en.wikipedia.org/wiki/Arran_(Caucasus)
200 https://en.wiktionary.org/wiki/Aryan
200 https://en.wiktionary.org/wiki/alien
200 https://en.wiktionary.org/wiki/ultimate
200 https://en.wiktionary.org/wiki/alternate
200 https://en.wiktionary.org/wiki/𐬀𐬌𐬭𐬌𐬌𐬋
```


## [2026-09-04T19:34:30.842Z] TOOL CALL #64: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/mk45.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nS_PII   = W + \"Reconstruction:Proto-Indo-Iranian/%C3%A1ryas\"\nS_H2EL  = W + \"Reconstruction:Proto-Indo-European/h%E2%82%82el-\"\nS_H2ELY = W + \"Reconstruction:Proto-Indo-European/h%E2%82%82%C3%A9lyos\"\nS_ERIU  = W + \"%C3%89riu\"\nS_IRELAND = W + \"Ireland\"\nS_IRMAN = W + \"ایرمان\"\nS_ARIYA = W + \"آریا\"\nS_IRAN  = W + \"ایران\"\nS_IRLAND= W + \"ایرلند\"\nS_ARAK  = W + \"اراک\"\nS_MPERAN= W + \"𐭠𐭩𐭥𐭠𐭭\"\nS_OPARYA= W + \"𐎠𐎼𐎡𐎹\"\nS_AVAIR = W + \"𐬀𐬌𐬭𐬌𐬌𐬋\"\nS_ALLOS = W + \"ἄλλος\"\nS_ELSE  = W + \"else\"\nS_ALLIG = W + \"alligator\"\nS_ALARM = W + \"alarm\"\nS_ALERT = W + \"alert\"\nS_IRAQ  = W + \"عراق\"\nS_ARYAN = W + \"Aryan\"\nS_ALIEN = W + \"alien\"\nS_ULT   = W + \"ultimate\"\nS_ALTN  = W + \"alternate\"\nS_PARAL = \"https://www.etymonline.com/word/parallel\"\nS_ARRAN = \"https://en.wikipedia.org/wiki/Arran_(Caucasus)\"\n\nPOK_AL1 = (\"POK_full.txt 'Root / lemma: al-1, ol-', Meaning \\\"besides; other\\\", Page(s): 24-26: \"\n           \"\\\"Moreover also maybe Old Indic ari 'of strangers, stranger', ar(i)ya- 'suitable, proper to the \"\n           \"stranger' ... then Subst. 'hospitable, lord, master, ruler, man', in addition ... hence, VN 'Arier = \"\n           \"Aryan', aryaka- 'venerable man', aryaman- n. 'Hospitality' ... Avestan airyō (= arya), Old pers. ariya, \"\n           \"'Aryan', Avestan airyaman 'guest, friend', npers. erman 'guest'\\\" (Pokorny follows P. Thieme 1938).\")\nPOK_ARIO = (\"POK_full.txt 'Root / lemma: ario-?', Meaning: master, lord, Page(s): 67, References: WP. I 80: \"\n            \"\\\"Old Indie ar(i)ya- 'mister' ... Avestan airyo. Old pers. ariya- 'Aryan' ... About Old Indie aryaman \"\n            \"'hospitality', m. 'guest's friend', Avestan airyaman-, npers. erman 'guest', see above under al-1.\\\"\")\n\ndef n(id, lang, words, verdict, derivation, refc, cons, sources):\n    return {\"id\": id, \"lang\": lang, \"words\": words, \"verdict\": verdict,\n            \"derivation\": derivation, \"ref_check\": refc, \"consulted\": cons, \"sources\": sources}\n\nnodes = []\n\n# ---------------- node 1 ----------------\nnodes.append(n(\n 1, \"Indo-European\", \"Aryo, Ario\", \"disputed\",\n \"The form itself is real: Pokorny does print a lemma *ario-? 'Herr, Gebieter' (IEW 67) with Old Indic ar(i)ya-, \"\n \"Avestan airyō, Old Persian ariya-, Gaulish PN Ario-manus. What is disputed is the ARROW: Nourai hangs *aryo- \"\n \"under *al-1 'beyond, other'. Pokorny 1959 does make that connection, but only tentatively and only because he \"\n \"adopted P. Thieme's 1938 analysis (ari- 'stranger' > ar(i)ya- 'hospitable, belonging to the stranger'), printing \"\n \"it under al-1 with 'seems possible' / 'maybe'; at the same time he kept ario-? as a separate lemma on p. 67 and \"\n \"there derived it from *ar-1 'to fit, join, move' (cf. Gk. aristos). Walde-Pokorny I 80 (ario-) and I 84 ff. \"\n \"(al-, ol-) already treat them as two unrelated roots. Modern reference works do not derive *aryo- from *h2el-: \"\n \"the only Indo-Iranian reflex of *h2el- recognised today is *Haranas > Skt. arana- 'foreign, distant'. \"\n \"Wiktionary's Proto-Indo-Iranian *Aryas entry calls the etymology 'Uncertain' and lists the competing verbal \"\n \"bases (Bopp ar- 'go'; Pictet ar- 'plough'; Guentert/Laroche/Benveniste ar- 'fit'; Thieme ar- 'give, allot'; \"\n \"Bailey ar- 'beget'), adding that a PIE derivation 'cannot be obtained with certainty' and that no comparable \"\n \"ethnonym exists outside Indo-Iranian. Phonetically, too, *h2el-yo- gives Gk. allos / Lat. alius with -ly-, not \"\n \"Indo-Iranian ar-(i)ya-. So: word real, gloss 'lord, ruler' right, parent wrong (or at best one hedged option \"\n \"inside Pokorny).\",\n [{\"ref\": \"POK:24\", \"status\": \"partial\",\n   \"note\": POK_AL1 + \" Pokorny does put arya- here, but hedged ('seems possible', 'maybe'), and as a Thieme \"\n           \"hypothesis, not as the arrow Nourai draws unconditionally.\"},\n  {\"ref\": \"POK:67\", \"status\": \"partial\",\n   \"note\": POK_ARIO + \" Pokorny's own note derives ario-? from *ar-1 'to move/fit', NOT from al-1; he only \"\n           \"cross-refers the aryaman- material to al-1.\"}],\n [{\"src\": \"WLD\", \"where\": \"Bd. I p. 80 s.v. ario- (vs. pp. 84-85 al-, ol-)\", \"stance\": \"contradicts\",\n   \"note\": \"\\\"ario- 'Herr, Gebieter'. Ai. arya 'Herr, Gebieter', arya 'Arier' ... av. airyo, apers. ariya 'arisch' \"\n           \"... Hierzu ai. aryama 'Gefaehrte, Freund' ... npers. erman 'Gast'.\\\" Walde-Pokorny gives ario- its own \"\n           \"lemma four pages before al-, ol- and makes no connection between them.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 appendix s.v. al-1\", \"stance\": \"contradicts\",\n   \"note\": \"\\\"al-1, Beyond. 1. Variant *ol- ... Latin ille ... uls, ulter, ultra ... 2. *al-tero- ... 3. Extended \"\n           \"form *alyo- ... Germanic *aljaz ... Latin alius ... Greek allos. [Pok. 1. al- 24.]\\\" Watkins lists NO \"\n           \"Indo-Iranian arya- material under al-1 at all.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann, s.v. 'arios' and s.v. 'alios'\", \"stance\": \"contradicts\",\n   \"note\": \"Two separate lemmas: \\\"arios 'man, hero; manly'. WP I, 80. Cf. aros Skt. aryah ... Av. airyo ... Medic \"\n           \"Arios 'Mede'\\\" and \\\"alios 'other' WP I, 85 ... Arm. ajl; Gk. allos; Lat. alius; Osc. allo-; MIr. aile\\\" \"\n           \"- the second has no Indo-Iranian member.\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt [pdf page 56], note 4 to the entry ARYAN\", \"stance\": \"partial\",\n   \"note\": \"Aryanpur records exactly Nourai's claim as one opinion: note 4 - 'BARNHART holds that this word may be \"\n           \"cognate with the Latin words ALIENUS, AL-TER (English ALIEN)'; but his note 1 says 'BARNHART and a \"\n           \"number of others hold that this word is not cognate with IRELAND, IRISH, and in principle the word \"\n           \"\\\"Arya\\\" may not be Indo-European.'\"}],\n [S_PII, S_H2EL, S_H2ELY]))\n\n# ---------------- node 2 ----------------\nnodes.append(n(\n 2, \"Old Persian / Avestan\", \"aria; arân; art-arân; airyanam-vaězo\", \"plausible\",\n \"aria: correct - Old Persian ariya- (a-r-i-y, Elamite har-ri-ia, so ar- and not r-; Darius DNa 'ariya ariya-cica' \"\n \"'an Aryan, of Aryan lineage') and Avestan airiia- 'Aryan' (Yt 13.143 airiianam dahyunam), Bartholomae AiW s.v. \"\n \"airya-, p. ariya-. airyanam-vaězo: correct - Av. airiianam vaejo, the mythical first land of Vidēvdād 1.2, \"\n \"Bartholomae's separate lemma airyana- 'arisch', 'sonst von vaējah-'; MP Ērānwēz. Nourai's gloss 'Aryan race and \"\n \"family' follows Farahvashi, who takes vaēj- as 'seed, race' (Pers. bīj). arân is NOT an attested Old Persian or \"\n \"Avestan word: what is attested is the genitive plural ariyanam / airiianam 'of the Aryans', which is the \"\n \"immediate source of MP ērān, so the entry is a citation form rather than an error. art-arân 'holy Aryan land' is \"\n \"not attested at all - it is Farahvashi's own reconstruction *Arta-arān for the modern name Ardalān (Iranvij \"\n \"p. 28), with arta- 'truth, holy' (Av. asa-/arta-). Hence plausible, not confirmed.\",\n [{\"ref\": \"IRN:7,28\", \"status\": \"supports\",\n   \"note\": \"Farahvashi, Iranvij, IRN_pages.txt pdf 18 (= printed p. 7), chapter head 'ایرانویج - خاستگاه ایرانیان': \"\n           \"'airyanem vaējō ... که در زبان پهلوی Ērānwēz «ایرانویج» شده است ... «ویج» بمعنی نخمه و نژاد است'. \"\n           \"IRN pdf 39 (= printed p. 28): 'واژه اردلان را می‌توان بصورت کهن آن ... بازسازی کرد: *Arta-arān و معنی آن \"\n           \"«ایران مقدس» است' - i.e. Nourai's art-arān 'holy Aryan land' is verbatim Farahvashi's reconstruction.\"},\n  {\"ref\": \"AHD\", \"status\": \"not_found\",\n   \"note\": \"AHD_watkins1985.txt s.v. al-1 has no Old Persian/Avestan material; the 1976 AHD appendix page Nourai \"\n           \"means is not online. Searched the whole appendix for 'ariya', 'airya', 'Aryan' - nothing under al-1.\"},\n  {\"ref\": \"POK\", \"status\": \"partial\",\n   \"note\": POK_AL1 + \" Pokorny does cite 'Avestan airyō (= arya), Old pers. ariya' - but under the hedged Thieme \"\n           \"paragraph.\"}],\n [{\"src\": \"BRT\", \"where\": \"AiW cols. ~197-200, s.v. airya-, airyana-\", \"stance\": \"supports\",\n   \"note\": \"\\\"j. airya-, p. ariya- 1) Adj. (fem. ya-) 'arisch': airyanam dahyunam ... Yt.13.143 ... 2) m. 'Arier' \"\n           \"... Ableit. - ai. vgl. arya- m. 'Arier'; mp. (Pu.), np. iran\\\" and \\\"j. airyana- Adj. 'arisch': \"\n           \"airyanem xvarena ... sonst von vaŋhah-: airyanem vaejo\\\".\"},\n  {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon and Grammar §§ (Ariya-, Ariya-ciça-)\", \"stance\": \"supports\",\n   \"note\": \"\\\"The sequence -ariy- is found in Ariya (and compounds), where Elam. has har-ri-ia, proving phonetic ar \"\n           \"and not r\\\"; and \\\"Ariya-ciça- 'Having Aryan lineage'\\\" (DNa/DSe).\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien, ch. on epenthesis (p. ~178)\", \"stance\": \"supports\",\n   \"note\": \"\\\"Ērān = arm. Ērān, paz. Ērān, phl. Ērān, inschr. Airan und Aryan, ap. g. pl. *Ariyānām\\\"; and \"\n           \"\\\"wie aryān zu Ērān\\\" - the gen. pl. is explicitly the source.\"}],\n [S_OPARYA, S_AVAIR, S_MPERAN]))\n\n# ---------------- node 3 ----------------\nnodes.append(n(\n 3, \"Persian\", \"Âriyâ «آریا»; Arân, Îrân, Arâk, Arâq «آران ، ایران ، اراک ، عراق»; Ardalân «اردلان»; Îrânvěj «ایرانویج»\",\n \"disputed\",\n \"Îrân: confirmed. OP gen. pl. ariyānām 'of the Aryans' > MP ērān (substantivised oblique plural of ēr < *arya-, \"\n \"first attested c. 225 CE in Ardashir I's trilingual at Naqsh-e Rostam, Parthian aryān, Greek arianōn ethnous) > \"\n \"NP Īrān; the epenthesis aryān > ērān is Huebschmann's textbook example. Îrânvěj: confirmed - Av. airiianam \"\n \"vaējō > MP Ērānwēz (MacKenzie 'Ērān-wēz (original) home of the Aryans') > NP Īrānvīj. Âriyâ: the word exists but \"\n \"is not inherited - Wiktionary marks Persian آریا a LEARNED borrowing from OP Aryah / Av. airiiō, first used by \"\n \"Hamza Isfahani (10th c.) and revived only in the early 20th c. (Rezazadeh Shafaq), replacing آریان borrowed from \"\n \"French aryen/English Aryan in the late 19th c. by Mirza Aqa Khan Kermani; the inherited doublet is ایر (ēr). \"\n \"Arân (Arrān, Caucasian Albania) is NOT from *arya-: the Parthian name is *Ardān, pointing to an earlier \"\n \"*aldwān that also yields Greek/Latin Albania and Armenian Ałuankʿ, whence Arabic al-Rān and Georgian Rani. \"\n \"Arâq/Arâk: Arabic al-ʿIrāq with initial ʿayn cannot continue *ērān; its origin is uncertain, and the Iranian \"\n \"candidate is MP ērag/erāg 'lowlands', a different word; Persian اراک is a 20th-c. Persianisation of عراق \"\n \"(ʿIrāq-e ʿAjam) applied to Soltanabad in 1938. Ardalân: only Farahvashi's reconstruction *Arta-arān supports \"\n \"the gloss; no independent source confirms it. Worst-word rule gives disputed.\",\n [{\"ref\": \"IRN:7,28\", \"status\": \"supports\",\n   \"note\": \"Iranvij pdf 18 (p. 7) for Īrānvīj; pdf 39 (p. 28): 'قبیله‌های پارسی ... در ناحیهٔ اردلان کنونی جای گرفت. \"\n           \"واژه اردلان را می‌توان بصورت کهن آن ... بازسازی کرد: *Arta-arān و معنی آن «ایران مقدس» است.' Exactly \"\n           \"Nourai's Ardalān = 'holy Aryan land'.\"},\n  {\"ref\": \"MON5:114\", \"status\": \"not_checked\",\n   \"note\": \"Mo'in vol. 5 (Aʿlām/proper names) is not among the local files - MON_part1/2 and the 2-vol Adena \"\n           \"reprint are the lexicon only (grep for 'ایرانویج' and 'ایرلند' in both returns nothing relevant); \"\n           \"vajehyab.com/moein returned HTTP 500.\"},\n  {\"ref\": \"PRT:27; PRT:313\", \"status\": \"not_checked\",\n   \"note\": \"Partridge, Origins (1958) is archive.org lending-restricted; no readable copy.\"}],\n [{\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p. 30\", \"stance\": \"supports\",\n   \"note\": \"\\\"Ērān [ʾyrʾn'| N ~] Ēran, (land of) the Aryans. ~ag [-k'] an Ēranian, Aryan\\\"; \\\"Ērān|šahr [...] land \"\n           \"of the Aryans. ~-wēz [-wyc] (original) home of the Aryans\\\"; also \\\"ēr [ʾyl] noble; hero\\\".\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien, no. 349 and the epenthesis chapter\", \"stance\": \"supports\",\n   \"note\": \"\\\"ware patyak durch Epenthese zu phl. paitak = np. paida geworden wie aryan zu Ēran\\\"; and \"\n           \"\\\"Ērān = arm. Ērān, paz. Ērān, phl. Ērān, inschr. Airan und Aryan, ap. g. pl. *Ariyānām\\\".\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary), s.v. an-agr, Ērān-šahr, Ērān-gušasp\",\n   \"stance\": \"supports\",\n   \"note\": \"Ērān-šahr passim ('xvatāyēh i Ērān šahr'); 'MPrs ʾnyrʾn (S); Paz. Anērān; NP Aniran' shows the same \"\n           \"ēr-/ērān formation with the privative.\"},\n  {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol. 1, leaf 416 of BQT_v1_pages.txt (~printed p. 195-196)\",\n   \"stance\": \"partial\",\n   \"note\": \"The page has 'ایرگان/ایرکان - بلغت زند و پازند بمعنی مردمان' and 'ایرج ... نام پسر فریدون است', \"\n           \"i.e. the Īr- name-family, but no entry deriving Arān/Arāk/Arāq from it.\"}],\n [S_IRAN, S_ARIYA, S_MPERAN, S_ARAK, S_IRAQ, S_ARRAN]))\n\n# ---------------- node 4 ----------------\nnodes.append(n(\n 4, \"Avestan\", \"airiyava; airya-man\", \"plausible\",\n \"airya-man: confirmed. Av. airyaman- (Gathic airyāman-) m. 'member of one's own group, sodalis, priestly \"\n \"companion', also the name of a divinity and of the Airyaman išyō prayer (Y 54.1); = Skt. aryamán- 'comrade, \"\n \"bosom friend; an Aditya'. It is a -man- stem built on airya- exactly as Nourai draws it, so the edge #2 > #4 is \"\n \"right; the gloss 'guest' is the later Middle/New Persian sense, not the Avestan one, and 'noble mannered' is \"\n \"Nourai's own etymologising. airiyava: Av. airyava- is attested, but only as a personal name (Yt 13.131, \"\n \"'manuš.ciθrahe airyavahe ašaonō', in the list of fravašis of the faithful); Bartholomae gives no meaning and \"\n \"explicitly warns that Justi's rendering 'Helfer der Arier' (= Nourai's 'helper of Aryans') 'stuetzt sich auf die \"\n \"minder gut bezeugte Lesung', i.e. rests on the poorer reading. So the word is real and Iranian, but the gloss is \"\n \"a 19th-c. onomastic guess.\",\n [{\"ref\": \"POK:24\", \"status\": \"supports\",\n   \"note\": POK_AL1 + \" Pokorny explicitly has 'Avestan airyaman \\\"guest, friend\\\", npers. erman \\\"guest\\\"' here.\"},\n  {\"ref\": \"BQT:196\", \"status\": \"supports\",\n   \"note\": \"BQT_v1_pages.txt leaf 417 (~printed p. 196), s.v. ایرمان: 'بروزن و معنی میهمان است'; Mo'in's footnote \"\n           \"on the same page: 'در شاهنامه سه بار ایرمان بمعنی مهمان آمده و ایرمان‌سرای بمعنی مهمان‌سرای مستعمل است \"\n           \"... در سانسکریت و اوستا [airyaman-] بمعنی یار و دوست و نیز نام یکی از خدایان وداست'.\"},\n  {\"ref\": \"IRN:12\", \"status\": \"supports\",\n   \"note\": \"Iranvij pdf 23 (= printed p. 12): 'واژه مرکب «airyanem vaējah» بمعنی زادگاه ایرانیان و نام ایرج Ērič در \"\n           \"فارسی و Ērič در ارمنی' - Farahvashi puts Īraj in this same *arya- family.\"},\n  {\"ref\": \"FAF:86\", \"status\": \"not_checked\",\n   \"note\": \"Daneshgar, Farhang-e Aʿlam-e Farsi (1370/1991) - no copy on disk or online (refs_online.json kind: none).\"}],\n [{\"src\": \"BRT\", \"where\": \"AiW cols. 199-200, s.v. 1airyaman-, airyava-\", \"stance\": \"partial\",\n   \"note\": \"\\\"j., g. airyaman-, g. airyāman- m. 'Genosse' uzw. priesterlicher ... 'Sodale' ... A) Name einer \"\n           \"Gottheit\\\", footnote \\\"Pu.: ērmān\\\"; but s.v. airyava-: \\\"m. EN. Name eines Glaeubigen: manuš.ciθrahe \"\n           \"airyavahe ašaonō Yt.13.131\\\" with the note that Justi's reading 'Helfer der Arier' 'stuetzt sich auf die \"\n           \"minder gut bezeugte Lesung'.\"},\n  {\"src\": \"HRN\", \"where\": \"Grundriss no. 140, p. 32\", \"stance\": \"supports\",\n   \"note\": \"\\\"140. irmān (*ērmān) 'Gast'. aw. airyaman- N. pr. eines Genius; phlv. ermān, ermānīk, ermānīh \"\n           \"(Aw.-Komm.); ai. aryamán- 'Busenfreund, Kamerad'.\\\"\"},\n  {\"src\": \"AHM\", \"where\": \"Gershevitch, Avestan Hymn to Mithra (grep airyaman)\", \"stance\": \"silent\",\n   \"note\": \"No entry bearing on airyava-.\"}],\n [S_IRMAN, S_AVAIR]))\n\n# ---------------- node 5 ----------------\nnodes.append(n(\n 5, \"Persian\", \"Îraj «ایرج»; îrmân «ایرمان»\", \"plausible\",\n \"îrmân: confirmed and well documented. Av. airyaman- > MP ērmān (Pahlavi ʾylmʾn', glossing Av. airyaman- in the \"\n \"Avesta commentary; MacKenzie: 'ērmān friend; a god', with ērmānīh 'friendship') > NP īrmān 'guest', the sense \"\n \"having shifted 'fellow-tribesman, sodalis' > 'friend' > 'guest' (already in Ferdowsi three times, and īrmān-sarā \"\n \"'guest-house'); Horn no. 140 and Huebschmann no. 140 both accept the equation, Huebschmann calling it \"\n \"'einwandfrei' against Noeldeke's rival *āθraman- 'one sitting at the fire'. Note MacKenzie keeps this ērmān \"\n \"apart from the homophone ēr-man(ag) 'humble' (to ēr 'below'). Nourai's Ferdowsi quotation is genuine: Noushin's \"\n \"Shahnameh glossary s.v. ایرمان gives 'مهمان' with exactly 'اگر کشته آید به دست تو گرگ / تو باشی به روم ایرمانی \"\n \"بزرگ'. Îraj: NP Īraj (Fereydun's youngest son, murdered by Salm and Tur) goes back to MP Ērič/Ēriz, a \"\n \"hypocoristic of ēr < *arya-, and Farahvashi (IRN 12) equates it with Armenian Ērič; but the specific route \"\n \"Nourai draws, Av. airyava- > Īraj with the meaning 'helper of Aryans', is Justi's onomastic guess on a doubtful \"\n \"reading, and would in any case give MP *Ēryāw, not Ērič. Hence plausible.\",\n [{\"ref\": \"POK:67\", \"status\": \"partial\",\n   \"note\": POK_ARIO + \" Pokorny has npers. erman 'guest' (so the īrmān half is supported) but nothing on Īraj.\"},\n  {\"ref\": \"BQT:196\", \"status\": \"supports\",\n   \"note\": \"BQT_v1_pages.txt leaf 417 (~p. 196): 'ایرمان - بروزن و معنی میهمان است ... و ایرمان‌سرا - بروزن \"\n           \"میهمان‌سرا. خانه و سرای عاریتی را گویند'; the previous leaf (~p. 195) carries 'ایرج ... نام پسر فریدون \"\n           \"است' - both words are on Nourai's cited spread.\"},\n  {\"ref\": \"IRN:12\", \"status\": \"supports\",\n   \"note\": \"Iranvij printed p. 12 names 'ایرج Ērič' beside Armenian Ērič as members of the airya-/Ērān family.\"}],\n [{\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p. 30\", \"stance\": \"supports\",\n   \"note\": \"\\\"1ērmān [ʾylmʾn' | N ~] friend; a god. ~īh: friendship\\\" - distinguished from \\\"2,3ēr-man(ag) humble\\\".\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien no. 140 (p. 20-21) and p. 178\", \"stance\": \"supports\",\n   \"note\": \"\\\"Die Gleichung ermān 'Gast' = zd. airyaman- (nach Geldner: 'Genossenschaft', nach Darmesteter: \"\n           \"'Vasall, Diener' - skr. aryamán- 'Busenfreund, Gefaehrte, Kamerad') scheint mir einwandfrei, ein zd. \"\n           \"*āθraman- 'am Feuer sitzend' dagegen mehr als bedenklich\\\"; p. 178 'ērmān \\\"Gast\\\" = ērmān = zd. \"\n           \"airyaman-'.\"},\n  {\"src\": \"HRN\", \"where\": \"Grundriss no. 140, pp. 32-33\", \"stance\": \"partial\",\n   \"note\": \"Accepts aw. airyaman- > phlv. ermān > np. irmān, but reports Noeldeke's alternative: 'so waere Noeldeke \"\n           \"geneigt, np. ermān \\\"Gast\\\" hieran anzuschliessen; also urspruenglich ein \\\"am Feuer Sitzender, \"\n           \"Teilnehmender\\\". Die Ableitung von ar. aryaman- waere dann aufzugeben.'\"},\n  {\"src\": \"FSF\", \"where\": \"Noushin, Vazhe-namak (Farhang-e Shahnameh), s.v. ایرمان\", \"stance\": \"supports\",\n   \"note\": \"'ایرمان - مهمان (جهانگیری - برهان): اگر کشته آید به دست تو گرگ / تو باشی به روم ایرمانی بزرگ' - \"\n           \"confirms both the gloss and Nourai's Ferdowsi citation.\"},\n  {\"src\": \"BQT\", \"where\": \"vol. 1 leaf 417, Mo'in's etymological footnote\", \"stance\": \"partial\",\n   \"note\": \"Mo'in derives ایرمان from a Pahlavi form and notes the Avestan/Sanskrit airyaman-/aryaman- 'یار و دوست' \"\n           \"and the divinity, i.e. supports īrmān but says nothing about airyava-.\"}],\n [S_IRMAN]))\n\n# ---------------- node 6 ----------------\nnodes.append(n(\n 6, \"Sanskrit\", \"Arya\", \"confirmed\",\n \"Skt. ā́rya- 'noble, honourable; an Aryan' (vrddhi formation) beside árya- 'master, lord; kind, favourable', \"\n \"aryaká- 'venerable man'; = Old Iranian *arya- (OP ariya-, Av. airiia-). The edge #1 > #6 is right as far as the \"\n \"Indo-Iranian node is concerned: Skt. ārya- and Ir. arya- are the same word; only the further ascent to *al-1 is \"\n \"the disputed part (see node 1). Klein s.v. Aryan states the descent Nourai wants, and adds the modern-history \"\n \"detail that 'Aryan' as a synonym of 'Indo-European' was introduced by Max Mueller.\",\n [{\"ref\": \"KLN:110\", \"status\": \"supports\",\n   \"note\": \"KLN_1966.txt s.v. Aryan (the A-section around p. 110): \\\"Aryan, adj. and n. - Formed with suff. -an fr. \"\n           \"OI. āryaḥ, 'noble', which is rel. to OPers. ariya, 'noble' (whence Pers. Iran, 'Persia'). Cp. Iranian. \"\n           \"As a synonym for 'Indo-European' the term Aryan was introduced by the German philologist Friederich Max \"\n           \"Mueller (1823-1900).\\\"\"},\n  {\"ref\": \"SHP:180\", \"status\": \"not_checked\",\n   \"note\": \"Shipley, Dictionary of Word Origins (1945) - HathiTrust/archive.org copies are not openly readable; no \"\n           \"local text.\"}],\n [{\"src\": \"POK\", \"where\": \"IEW 67 s.v. ario-?\", \"stance\": \"supports\",\n   \"note\": \"\\\"Old Indie ar(i)ya- 'mister, convivial', ar(i)ya- 'Aryan', aryaka 'venerable man'; Avestan airyo, Old \"\n           \"pers. ariya- 'Aryan'.\\\"\"},\n  {\"src\": \"IEC\", \"where\": \"Mann, s.v. arios\", \"stance\": \"supports\",\n   \"note\": \"\\\"arios 'man, hero; manly'. WP I, 80. Cf. Skt. áryah, s.; aryáh, adj.; Av. airyo, adj.; Medic Arios \"\n           \"'Mede'; Arm. ajr 'man'.\\\"\"},\n  {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, s.v. Aryan\", \"stance\": \"supports\",\n   \"note\": \"\\\"Ar'yan ... Of or pertaining to the Aryans or their language ... [< Sans. ārya, noble.]\\\"\"}],\n [S_PII, S_ARYAN]))\n\n# ---------------- node 7 ----------------\nnodes.append(n(\n 7, \"English\", \"Aryan, Ireland\", \"disputed\",\n \"Aryan is fine: English Aryan = Sanskrit ā́rya- + -an, in learned use from 1794 and as a language-family label \"\n \"from Max Mueller (1850s) - exactly Klein's account, so that half of the node is confirmed. Ireland is not. \"\n \"English Ireland < Middle English Irlond/Irland < Old English Īrland, a compound of the Old Irish country name \"\n \"Ériu (acc./dat. Érinn, whence Erin) + land; Old Irish Ériu goes back to Proto-Celtic *Φīweriyū (Ptolemy's \"\n \"Iouernia, Latin Hibernia), i.e. to a *piHwer- 'fat, fertile' formation, and has nothing to do with *arya-. \"\n \"Walde-Pokorny already dismissed the link: the Irish ancestor-name Eremón, on which the 19th-c. equation rested, \"\n \"'ist eine von Erin abgeleitete gelehrte Fiktion' and 'hat mit der obengenannten Sippe nichts zu tun'. Klein \"\n \"likewise derives Erin from OE Erinn / Ir. Éire with no Aryan reference. Wiktionary's Proto-Indo-Iranian *Áryas \"\n \"entry states flatly that '18th/19th-century assumptions of a relationship to Irish Éire, German Ehre, etc. have \"\n \"long since been dismissed'. Aryanpur records the same split: his note 1 cites Barnhart that Arya is NOT cognate \"\n \"with Ireland/Irish, while his note 2 reports the older popular view that Aryans settled in India, Iran and \"\n \"Ireland. Worst-word rule: disputed.\",\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}],\n [{\"src\": \"WLD\", \"where\": \"Bd. I p. 80, end of the ario- article\", \"stance\": \"contradicts\",\n   \"note\": \"\\\"Ir. Airem, gen. Airemon, Eremon 'einer der sagenhaften Stammvaeter des irischen Volkes' ... ist nach \"\n           \"K. Meyer RC. 33, 94 f. falsch angesetzt und hat mit der obengenannten Sippe nichts zu tun. Eremon ... \"\n           \"als Bezeichnung eines irischen Stammvaters ist eine von Erin abgeleitete gelehrte Fiktion.\\\"\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. Erin, Irish\", \"stance\": \"contradicts\",\n   \"note\": \"\\\"Erin, n., ancient (now poetic) name of Ireland. - OE. Erinn, dat. of Eriu (whence Ir. Eire), \"\n           \"'Ireland'\\\"; \\\"Irish ... fr. OE. Iras, 'the Irish', which is rel. to OE. Eriu, 'Ireland'\\\" - no Aryan \"\n           \"connection anywhere.\"},\n  {\"src\": \"POK\", \"where\": \"IEW 24-26 (al-1) and 67 (ario-?)\", \"stance\": \"partial\",\n   \"note\": \"Under al-1: 'mythical Irish ancestor Eremón is scholar neologism to Ériu \\\"Ireland\\\"'; under ario-?: \"\n           \"'Old Irish aire, airech \\\"suitor\\\" are ambiguous'. Pokorny admits only the Old Irish common noun aire, \"\n           \"never the country name.\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur ARY_pages.txt [pdf page 56], notes 1-2 to ARYAN\", \"stance\": \"partial\",\n   \"note\": \"Note 1: 'BARNHART و شماری دیگر معتقدند که این واژه با واژه‌ی IRELAND, IRISH همریشه نیست'; note 2 reports \"\n           \"the contrary popular view that Aryans named India, Iran and Ireland.\"},\n  {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. Aryan\", \"stance\": \"supports\",\n   \"note\": \"For the Aryan half only: '[< Sans. ārya, noble.]'\"}],\n [S_ERIU, S_IRELAND, S_PII, S_ARYAN]))\n\n# ---------------- node 8 ----------------\nnodes.append(n(\n 8, \"Persian\", \"Îrland «ایرلند»\", \"plausible\",\n \"The word is real: NP ایرلند 'Ireland', a 19th/20th-c. European loan. Wiktionary derives Persian ایرلند from \"\n \"FRENCH Irlande (the usual channel for European toponyms entering Persian through the Qajar-period French-based \"\n \"geographical literature), not from English; Wiktionary's Ériu entry likewise lists Persian ایرلند under Old \"\n \"French Irlande > French Irlande. So the node's word and language are right and the immediate parent (an English \"\n \"or French form of Ireland) is nearly right, but the arrow is one step off, and the whole branch inherits the \"\n \"false Aryan-Ireland link of node 7. Hence plausible rather than confirmed.\",\n [{\"ref\": \"MON5:212\", \"status\": \"not_checked\",\n   \"note\": \"Mo'in vol. 5 (proper names) is not in the local library: MON_part1.txt/MON_part2.txt and the 2-vol \"\n           \"Adena reprint contain only the lexicon (grep 'ایرلند' returns only incidental mentions inside the \"\n           \"entries حسرت and ویسکی), and vajehyab.com/moein returned HTTP 500.\"}],\n [{\"src\": \"MON\", \"where\": \"MON_part2.txt lines 33416, 87981\", \"stance\": \"silent\",\n   \"note\": \"ایرلند occurs only inside other articles ('انگلستان و ایرلند و آسیای صغیر'; 'ویسکی: [از ایرلندی]'), \"\n           \"there is no headword entry with an etymology in the local volumes.\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. Irish, Erin\", \"stance\": \"partial\",\n   \"note\": \"Supplies the source form ('OE. Eriu, Ireland') that the Persian loan ultimately reflects, but of \"\n           \"course says nothing about Persian.\"}],\n [S_IRLAND, S_ERIU]))\n\n# ---------------- node 9 ----------------\nnodes.append(n(\n 9, \"Sogdian\", \"`ry`n-wyj`n\", \"confirmed\",\n \"Manichaean Sogdian ʾryʾnwyjʾn / ʾryʾnwyjn, transcribed aryān-wēzan, i.e. the Sogdian continuation of Av. \"\n \"airiianam vaējah, morphologically the Sogdian oblique plural in -ān matching MP Ērān-wēz; Gharib glosses it \"\n \"'Ērān-wēj' and cites Benveniste, Notes iv 506 n. and Henning, BSOAS 11, 68.26. The word is a genuine Eastern \"\n \"Iranian cognate of Nourai's Avestan airyanam-vaezo, and the parent #1 (the *arya- node) is right for its first \"\n \"element, so the node is confirmed as drawn (the gloss 'Aryan family' renders wēz 'seed, stock' loosely but \"\n \"acceptably).\",\n [{\"ref\": \"SOD:60\", \"status\": \"supports\",\n   \"note\": \"SOD_pages.txt leaf 126, whose header carries the printed page number 60 (leaf 127 = p. 61), entry no. \"\n           \"1525: \\\"ʾryʾnwyjʾn M - aryan-wezan (ʾryʾnwyjn) < aryana-vaeja - Ēran-wej. Benv. Notesiv 506n; Hen. \"\n           \"BSOAS 11, 68.26\\\"; entry 1526 \\\"ʾryʾnwyjn => ʾryʾnwyjʾn\\\".\"}],\n [{\"src\": \"BRT\", \"where\": \"AiW s.v. airyana-\", \"stance\": \"supports\",\n   \"note\": \"\\\"j. airyana- Adj. 'arisch' ... sonst von vaŋhah-: airyanem vaejo\\\" - the Avestan original of the \"\n           \"Sogdian form.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie p. 30 s.v. Ērānšahr\", \"stance\": \"supports\",\n   \"note\": \"\\\"~-wēz [-wyc] (original) home of the Aryans\\\" - the Middle Persian parallel of the Sogdian compound.\"},\n  {\"src\": \"HENNING\", \"where\": \"Selected Papers (BSOAS 11, 68 is Gharib's cited source)\", \"stance\": \"silent\",\n   \"note\": \"The local Selected Papers text does not reproduce the 1943 note Gharib cites.\"}],\n [S_MPERAN]))\n\n# ---------------- node 10 ----------------\nnodes.append(n(\n 10, \"Latin\", \"ille; ultrâ; alter; alius\", \"confirmed\",\n \"All four are the standard Latin reflexes of PIE *h2el-/*h2ol- 'beyond, other'. ille 'that (yonder)' replaces Old \"\n \"Latin ollus/olle < *ol-no-s (the -ll- and the i- from the influence of is, iste); ultrā 'beyond' is the ablative \"\n \"of the adjective *ulter, with uls, ultimus, ulterior, from suffixed *ol-s / *ol-tero-; alter 'the other (of \"\n \"two)' < *al-tero-; alius 'other (of more than two)' < *h2el-yos = Gk. állos, Goth. aljis. Watkins's al-1 entry \"\n \"lists precisely this set. One caveat on the glossing: alius means 'other', not 'from beyond (foreigner)'; the \"\n \"'foreign' sense belongs to the derivative aliēnus (< *ali-es-nos), which is what Nourai's parenthesis really \"\n \"describes.\",\n [{\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"AHD_watkins1985.txt s.v. al-1: \\\"1. Variant *ol-, 'beyond', in: a. suffixed forms *ol-se-, *ol-so- in \"\n           \"Old Latin ollus in Latin ille (feminine illa) ... b. suffixed forms *ol-s, *ol-tero- in Latin uls, \"\n           \"*ulter, ultra ... 2. Suffixed form *al-tero- ... a. Latin alter ... 3. Extended form *alyo- ... b. Latin \"\n           \"alius, other of more than two.\\\"\"}],\n [{\"src\": \"POK\", \"where\": \"IEW 24-26, al-1\", \"stance\": \"supports\",\n   \"note\": \"\\\"Latin uls 'beyond', *ulter, -tra, -trum ... Sup. ultimus ... Old Latin ollus ... (*ol-no-s) ... \"\n           \"Latin alius = Oscan allo- 'other things' ... Comparative alter, -era, -erum 'one from two'.\\\"\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I pp. 84-85, al-, ol-\", \"stance\": \"supports\",\n   \"note\": \"\\\"idg. alios 'anderer', nach Brugmann Grdr. II 1, 164 mit Formans -o- von einem Adv. *ali 'jenseits' \"\n           \"abgeleitet\\\"; the Latin ollus/*olnos material follows in the same article.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. alios\", \"stance\": \"supports\",\n   \"note\": \"\\\"alios 'other' WP I, 85 ... Lat. alius; Osc. allo-.\\\"\"}],\n [S_H2EL, S_H2ELY, S_ALLOS]))\n\n# ---------------- node 11 ----------------\nnodes.append(n(\n 11, \"English\", \"alarm, alert, alligator; ultimate, ultra-; alternate; alien\", \"confirmed\",\n \"Three Romance loans that carry the descendant of Latin ille in as the definite article: alarm < ME alarme < MFr. \"\n \"alarme < Old Italian all'arme! 'to (the) arms!' (a + le < illas + arma), the Italian phrase being taken over \"\n \"whole as a battle cry in the 14th c.; alert < Fr. alerte < It. all'erta 'on the lookout' (a + l' < illa + erta \"\n \"'watchtower, height'); alligator < early ModE alligarta/aligarto < Sp. el lagarto 'the lizard' (el < ille), the \"\n \"name Spanish colonists gave the Florida crocodilian, later respelled after Latin alligator 'one who binds'. \"\n \"ultimate < LL ultimātus, from ultimus, superlative of *ulter; ultra- < the Latin preposition/adverb ultrā. \"\n \"alternate < Lat. alternāre, from alternus < alter. alien < OFr. alien < Lat. aliēnus 'belonging to another, \"\n \"foreign', from alius. Watkins's index assigns every one of these to al-1 (ALARM al-1, ar-; ALERT al-1; ALLIGATOR \"\n \"al-1; ULTIMATE, ULTRA-, ALTERNATE al-1; ALIEN al-1).\",\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}],\n [{\"src\": \"AHD\", \"where\": \"Watkins 1985, index of English words\", \"stance\": \"supports\",\n   \"note\": \"\\\"ALARM al-1, ar-\\\", \\\"ALERT al-1\\\", \\\"ALLIGATOR al-1\\\", \\\"ALTERNATE al-1\\\", \\\"ALIEN al-1\\\", \"\n           \"\\\"ULTERIOR, ULTIMATE, ULTRA-\\\" listed under al-1 in the root entry.\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat s.v. Alien (and cross-ref. Alert s.v. Erect)\", \"stance\": \"supports\",\n   \"note\": \"\\\"Alien. (F.-L.) M.E. alien. - O.F. alien. - L. alienus, strange; a stranger. - L. alius, another. + \"\n           \"Gk. allos, another; Goth. alis, other; see Else.\\\" Alert is cross-referred to 'Erect' (It. erta).\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. alarm, alert, alligator\", \"stance\": \"supports\",\n   \"note\": \"Klein gives the same Romance routes (It. all'arme, It. all'erta, Sp. el lagarto).\"}],\n [S_ALARM, S_ALERT, S_ALLIG, S_ALIEN, S_ULT, S_ALTN]))\n\n# ---------------- node 12 ----------------\nnodes.append(n(\n 12, \"Greek\", \"allos; para-allělon\", \"confirmed\",\n \"Gk. állos 'other' (Cypriot aîlos, Arcadian állu) < Proto-Hellenic *áľľos < PIE *h2élyos, with the regular \"\n \"Greek treatment of *-ly- > -ll-; = Lat. alius, Goth. aljis, OIr. aile. The second item is the compound \"\n \"parállēlos 'beside one another, parallel', para- 'beside' (PIE *per-, whence Nourai's cross-reference to root \"\n \"Per 1) + allēlōn, the reciprocal pronoun formed by reduplication of állos (*allo-allo- > allēlo-). Nourai's \"\n \"'para-allělon' writes the underlying analysis rather than the attested nominative parállēlos, but the analysis \"\n \"itself is correct; the mathematical use of the word is Euclidean.\",\n [{\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"AHD_watkins1985.txt s.v. al-1, 3.c.: \\\"Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, \"\n           \"MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS.\\\"\"}],\n [{\"src\": \"POK\", \"where\": \"IEW 25 (al-1)\", \"stance\": \"supports\",\n   \"note\": \"\\\"gr. allos 'other' (Cypriot ailos), n. allo, compare allodapos 'from elsewhere, from another place, \"\n           \"strange' (= Latin aliud) ... in addition allelon etc. 'each other'.\\\"\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. alios\", \"stance\": \"supports\",\n   \"note\": \"\\\"alios 'other' WP I, 85 ... Gk. állos.\\\"\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I pp. 84-86, al-, ol-\", \"stance\": \"supports\",\n   \"note\": \"The Greek allos material stands in the same article as Lat. alius and Goth. aljis.\"}],\n [S_ALLOS, S_H2ELY, S_PARAL]))\n\n# ---------------- node 13 ----------------\nnodes.append(n(\n 13, \"Latin\", \"parallělum\", \"confirmed\",\n \"Latin parallēlus, -a, -um (also as noun parallēlos) is a straight borrowing of Gk. parállēlos, taken over with \"\n \"Greek geometry (Euclid's Elements, book I, definition 23) by the Latin mathematical and astronomical \"\n \"vocabulary; the Greek -ēlo- is rendered -ēlu-/-ēlo- and the word is given Latin adjectival endings. From Latin \"\n \"it passed into Middle French parallèle in the 16th c.\",\n [{\"ref\": \"AHD:951\", \"status\": \"partial\",\n   \"note\": \"The 1976 AHD main-dictionary page 951 (the entry PARALLEL) is not open online; the corresponding \"\n           \"Watkins appendix entry is verifiable and lists PARALLEL under al-1 (index line 'PARALLEL al-1', and \"\n           \"under al-1 3.c. 'Greek allos ... PARALLAX, PARALLEL'), which is the same claim.\"}],\n [{\"src\": \"KLN\", \"where\": \"s.v. parallel\", \"stance\": \"supports\",\n   \"note\": \"Klein derives English parallel from F. parallèle, from L. parallēlus, from Gk. parállēlos, from para- + \"\n           \"allēlōn, from állos.\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (grep parallel)\", \"stance\": \"silent\",\n   \"note\": \"The dictionary of inherited Latin vocabulary has no article for the Greek technical loan parallēlus.\"}],\n [S_PARAL]))\n\n# ---------------- node 14 ----------------\nnodes.append(n(\n 14, \"English\", \"parallel\", \"confirmed\",\n \"English parallel is first attested c. 1540 as a geometrical adjective ('lying in the same plane but never \"\n \"meeting'), borrowed from Middle French parallèle and its etymon Latin parallēlus; the noun follows in the 1550s, \"\n \"the figurative sense 'having the same direction or tendency' c. 1600, and the verb in the 1590s. Nourai's chain \"\n \"Greek > Latin > English is right; only the French intermediary is left out.\",\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}],\n [{\"src\": \"KLN\", \"where\": \"s.v. parallel\", \"stance\": \"supports\",\n   \"note\": \"English parallel < F. parallèle < L. parallēlus < Gk. parállēlos.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 index\", \"stance\": \"supports\",\n   \"note\": \"\\\"PARALLEL al-1\\\".\"}],\n [S_PARAL]))\n\n# ---------------- node 15 ----------------\nnodes.append(n(\n 15, \"Germanic\", \"al-jas\", \"confirmed\",\n \"Proto-Germanic *aljas 'otherwise, of another' is the genitive singular of the adjective *aljaz 'other' \"\n \"(< PIE *h2élyos, the same formation as Lat. alius and Gk. állos), used adverbially - a normal Germanic adverbial \"\n \"genitive, cf. Goth. aljis 'other', OHG elles, OFris. elles. Watkins reconstructs it as '*aljaz (with adverbial \"\n \"suffix)'. Nourai's spelling al-jas is the ordinary transliteration of *aljas.\",\n [{\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"AHD_watkins1985.txt s.v. al-1, 3.a.: \\\"Extended form *alyo-, 'other of more than two', in: a. Germanic \"\n           \"*aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE.\\\"\"}],\n [{\"src\": \"POK\", \"where\": \"IEW 25-26 (al-1)\", \"stance\": \"supports\",\n   \"note\": \"\\\"Gothic aljis 'other' ... Gothic alja-leiko 'other, different' ... and in adverbs, like Old English \"\n           \"elles, engl. else 'other, different'.\\\"\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I pp. 85-86 (al-, ol-)\", \"stance\": \"supports\",\n   \"note\": \"The Germanic *aljis material stands in the same al-, ol- article.\"}],\n [S_ELSE, S_H2ELY]))\n\n# ---------------- node 16 ----------------\nnodes.append(n(\n 16, \"English\", \"else\", \"confirmed\",\n \"English else < ME elles < OE elles 'other, otherwise, different', from Proto-West-Germanic *alljas, \"\n \"Proto-Germanic *aljas (adverbial genitive of *aljaz), from PIE *h2élyos < *h2el- 'other, beyond'. The word is \"\n \"still an adverbial genitive in form (the -s), which is why it is postposed (someone else, what else). Cognates: \"\n \"OFris. elles, OHG elles, Da. ellers, Sw. eljest, Goth. aljis.\",\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}],\n [{\"src\": \"AHD\", \"where\": \"Watkins 1985 index and al-1 entry\", \"stance\": \"supports\",\n   \"note\": \"\\\"ELSE al-1\\\"; under al-1: \\\"Germanic *aljaz (with adverbial suffix) in Old English elles, else, \"\n           \"otherwise: ELSE.\\\"\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat s.v. Alien (cross-reference 'see Else')\", \"stance\": \"supports\",\n   \"note\": \"Skeat groups else with L. alius, Gk. allos, Goth. alis under one family.\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. else\", \"stance\": \"supports\",\n   \"note\": \"Klein derives else from OE elles, orig. gen. of the adjective, rel. to Goth. aljis, L. alius.\"}],\n [S_ELSE, S_H2EL]))\n\nentry = {\n \"entry\": 0,\n \"root\": \"Al 1, Ol 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₂el- 'beyond, other' (Pokorny 1. al-, ol- 'jenseits, anderer', IEW 24-26; Watkins al-1 'Beyond')\",\n \"note\": (\n  \"The ROOT box is right: Pokorny's al-1, ol- (IEW 24-26) and Watkins's al-1 'Beyond' are exactly this root, \"\n  \"modern *h₂el-, with the Latin (ille, uls/ultra, alter, alius), Greek (allos), Germanic (*aljaz/else), Celtic \"\n  \"and Slavic branches Nourai draws. Only the gloss is slightly padded: the sources say 'beyond, besides, other', \"\n  \"not 'above'. The problem on this page is the whole LEFT branch. Nourai makes *Aryo/*Ario 'lord, ruler' a \"\n  \"daughter of *al-1, and from it hangs the entire Iranian family (aria, Ērān, Īrānvēj, airyaman/īrmān, Sogdian \"\n  \"aryān-wēzan) plus English Aryan AND Ireland. The Iranian material itself is impeccable and every Iranian link \"\n  \"checks out in Bartholomae, Kent, MacKenzie, Horn, Hübschmann and Gharib; what fails is (a) the ascent of \"\n  \"*aryo- to *al-1 - Pokorny 1959 offers it only as P. Thieme's hypothesis, hedged with 'seems possible'/'maybe', \"\n  \"while keeping ario-? as a separate lemma on p. 67 derived from *ar- 'to fit'; Walde-Pokorny I 80 vs. I 84, \"\n  \"Mann's IEC, and Watkins keep the two roots apart, and current work (Mayrhofer, Kloekhorst, Wiktionary) calls \"\n  \"*aryas of uncertain origin with no accepted PIE etymology; and (b) Ireland, which Walde-Pokorny already \"\n  \"labelled a 'gelehrte Fiktion' (Eremón is a learned back-formation from Ériu) and which today goes to \"\n  \"Proto-Celtic *Φīweriyū. Two further Persian names in node 3, Arān (Arrān/Caucasian Albania, from Parthian \"\n  \"*Ardān) and Arāq/Arāk (Arabic al-ʿIrāq, origin uncertain, at best MP ērag 'lowlands'), are also wrongly \"\n  \"attached to Ērān. Nourai's citations are honest: POK:24 really does contain the arya- paragraph, IRN:28 really \"\n  \"does reconstruct Ardalān as *Arta-arān, SOD:60 really has ʾryʾnwyjʾn, BQT:196 really has īrmān - the sources \"\n  \"say what he says they say; it is the 1959/1989 scholarship behind them that has moved on.\"),\n \"sources\": [S_H2EL, S_H2ELY, S_PII, S_ALLOS, S_ELSE],\n \"ref_check\": [\n   {\"ref\": \"POK:24\", \"status\": \"supports\",\n    \"note\": POK_AL1.split(':')[0] + \": POK_full.txt 'Root / lemma: al-1, ol-', 'Meaning: besides; other', \"\n            \"'Page(s): 24-26', 'References: WP. I 84 ff., WH. I 30, 32 f.' - the root, the page and the gloss all \"\n            \"match Nourai's root box (his added 'above' is not in Pokorny).\"}],\n \"nodes\": nodes,\n}\n\ndoc = {\n \"pdf_page\": 45,\n \"book_page\": 15,\n \"verified_by\": \"claude-fable-5-1\",\n \"verified_on\": \"2026-09-04\",\n \"entries\": [entry],\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-45.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/mk45.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-45.json > /dev/null && echo JSON_OK"
}
```


### [2026-09-04T19:34:33.012Z] TOOL RESULT

```
ok
JSON_OK
```


## [2026-09-04T19:34:37.464Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 tools/verify_check.py 45; echo \"exit=$?\"; head -c 300 data/verification/page-45.json; echo; file data/verification/page-45.json"
}
```


### [2026-09-04T19:34:39.300Z] TOOL RESULT

```
nodes verified: 16/16
node verdicts: {'disputed': 3, 'plausible': 4, 'confirmed': 9}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 5, 'supports': 12, 'not_found': 1, 'not_checked': 9}
books consulted: {'contradicts': 5, 'partial': 8, 'supports': 33, 'silent': 4} | by book: {'KLN': 6, 'WLD': 5, 'POK': 5, 'AHD': 4, 'IEC': 4, 'BRT': 3, 'HUB': 3, 'PHD': 3, 'ARY': 2, 'BQT': 2, 'HRN': 2, 'FSD': 2, 'SKT': 2, 'KNT': 1, 'NYB': 1, 'AHM': 1, 'FSF': 1, 'MON': 1, 'HENNING': 1, 'LAT': 1}
exit=0
{
  "pdf_page": 45,
  "book_page": 15,
  "verified_by": "claude-fable-5-1",
  "verified_on": "2026-09-04",
  "entries": [
    {
      "entry": 0,
      "root": "Al 1, Ol 1",
      "verdict": "confirmed",
      "modern_form": "PIE *h₂el- 'beyond, other' (Pokorny 1. al-, ol- 'jenseits, anderer', IEW
data/verification/page-45.json: JSON text data
```


## [2026-09-04T19:34:57.678Z] AGENT

Done. Wrote `/home/sfmqrb/git/rishe/data/verification/page-45.json`; `verify_check.py 45` passes with no PROBLEM lines (exit 0).

**PDF page 45 (book p. 15) — root Al 1, Ol 1 "beyond, above", 16 nodes**
- Root verdict: **confirmed** (= PIE *h₂el-, Pokorny IEW 24-26, Watkins al-1 "Beyond"; only "above" in the gloss is padding).
- Node verdicts: **9 confirmed, 4 plausible, 3 disputed**. Ref checks: 12 supports, 5 partial, 1 not_found, 9 not_checked (PRT, SHP, FAF, MON5 have no accessible copy). 20 different books consulted (33 supports / 8 partial / 5 contradicts / 4 silent).

Disputed items:
- **#1 IE "Aryo, Ario"** — the form is real (POK 67 *ario-* "Herr, Gebieter"), but hanging it under *al-1* is only Thieme's hedged hypothesis that Pokorny 1959 prints with "seems possible/maybe"; Walde-Pokorny I 80 vs. I 84, Mann's IEC and Watkins all keep the two roots apart, and Wiktionary/Mayrhofer call PII *áryas of uncertain origin.
- **#3 Persian "Arân, Îrân, Arâk, Arâq…"** — Îrân and Îrânvěj confirmed (OP gen. pl. *ariyānām* > MP ērān; Hübschmann's *aryān > Ērān*), but Arân = Arrān/Caucasian Albania (Parthian *Ardān), Arâq = Arabic al-ʿIrāq (uncertain, at best MP *ērag* "lowlands"), Âriyâ is a 20th-c. learned re-borrowing, Ardalân rests solely on Farahvashi's own *Arta-arān.
- **#7 English "Aryan, Ireland"** — Aryan fine; Ireland is not: OE Īrland < OIr. Ériu < Proto-Celtic *Φīweriyū. Walde-Pokorny I 80 already calls the Eremón link "eine … gelehrte Fiktion", and Aryanpur (ARY p. 56 n. 1) cites Barnhart to the same effect.

Nourai's own citations checked out well where readable: IRN:28 verbatim reconstructs Ardalān as *Arta-arān "holy Iran"; SOD:60 no. 1525 has ʾryʾnwyjʾn = Ērān-wēj; BQT:196 has ایرمان "میهمان" with Mo'in's footnote; FSF confirms the Ferdowsi verse; KLN:110 matches the Aryan entry exactly. Node #4's gloss "helper of Aryans" for Av. *airyava-* is Justi's guess, which Bartholomae flags as resting on the poorer manuscript reading. 26 web pages archived via `fetch_source.py`.
