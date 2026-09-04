# Verification process log — verify-page-49


## [2026-09-04T19:34:31.252Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 49 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-49.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-49.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-49.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 49` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T19:34:32.934Z] AGENT

I'll start by reading the instructions file.


## [2026-09-04T19:34:35.074Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:34:35.088Z] TOOL RESULT

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


## [2026-09-04T19:34:35.757Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-49.txt"
}
```


### [2026-09-04T19:34:35.789Z] TOOL RESULT

```
1	=== PDF page 49 (book page 19) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Alek : to ward off, protect  (refs POK:32)
4	#1 (parent #0) [Greek] refs=AHD:1506; KLN:47,856 | alexein : to protect ; alex-andros : protector of men ☞Ner 1
5	  #2 (parent #1) [Arabic] refs=MON5:144 | Eskandar
6	    #3 (parent #2) [Persian] refs=MON5:144 | Eskandar «اسکندر»
7	  #4 (parent #1) [Latin] refs=KLN:47 | Alexander
8	    #5 (parent #4) [French] refs=MON5:144 | Alexandre
9	      #6 (parent #5) [Persian] refs=MON5:173 | Alexândr «الکساندر» | extra: آلکساندر
10	    #7 (parent #4) [English] refs=None | Alexander
11	#8 (parent #0) [Sanskrit] refs=POK:32; KLN:47,856 | lâkšâ, rakšâ : 100,000 soldiers, also a large group of insects, insects ; lâk, râk : tree resin leaking after being attacked by a swarm of insects | NOTE: AHD and OEW:333 derive these words from the root "Reg: to dye".
12	  #9 (parent #8) [Persian] refs=KLN:856; BQT:1900 | lak «لَک» : hundred thousand (soldiers) | NOTE: See "Reg: to dye" for another possible root.
13	    #10 (parent #9) [Arabic] refs=AFM:141; FVF:613 | lajj : a large group of people, also the deepest point of sea.
14	      #11 (parent #10) [Persian] refs=MON:3569 | lojjeh «لُجّه» : the deepest point of sea | NOTE: See "Reg: to dye" for another possible root.
15	  #12 (parent #8) [Persian] refs=KLN:856; BQT:1878 | lâk «لاک» : red resin, lacquer | NOTE: See "Reg: to dye" for another possible root.
16	    #13 (parent #12) [Portuguese] refs=None | 
17	      #14 (parent #13) [French] refs=None | 
18	        #15 (parent #14) [English] refs=SKT:281 | lacquer ; Shellac
19	--- entry 1 ---
20	ROOT Âleŭos -> redirect to Al 4
21	
```


## [2026-09-04T19:34:38.979Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-49.json",
 "description": "Read page-49 source JSON"
}
```


### [2026-09-04T19:34:39.016Z] TOOL RESULT

```
{
  "pdf_page": 49,
  "book_page": 19,
  "entries": [
    {
      "root": {
        "name": "Alek",
        "lang": "Indo-European",
        "refs": "POK:32",
        "gloss": "to ward off, protect"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1506; KLN:47,856",
          "words": [
            {"translit": "alexein", "gloss": "to protect", "script": null},
            {"translit": "alex-andros", "gloss": "protector of men", "script": null, "see": ["Ner 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "MON5:144",
          "words": [
            {"translit": "Eskandar", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON5:144",
          "words": [
            {"translit": "Eskandar", "gloss": null, "script": "اسکندر"}
          ],
          "note": null,
          "quote": {"text": "آیینهٔ سکندر جام میست بنگر - تا بر تو عرضه دارد احوال ملک دارا", "poet": "Hâfez"}
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Latin",
          "refs": "KLN:47",
          "words": [
            {"translit": "Alexander", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": "MON5:144",
          "words": [
            {"translit": "Alexandre", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON5:173",
          "words": [
            {"translit": "Alexândr", "gloss": null, "script": "الکساندر"}
          ],
          "script_extra": "آلکساندر",
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Alexander", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:32; KLN:47,856",
          "words": [
            {"translit": "lâkšâ, rakšâ", "gloss": "100,000 soldiers, also a large group of insects, insects", "script": null},
            {"translit": "lâk, râk", "gloss": "tree resin leaking after being attacked by a swarm of insects", "script": null}
          ],
          "note": "AHD and OEW:333 derive these words from the root \"Reg: to dye\".",
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "KLN:856; BQT:1900",
          "words": [
            {"translit": "lak", "gloss": "hundred thousand (soldiers)", "script": "لَک"}
          ],
          "note": "See \"Reg: to dye\" for another possible root.",
          "quote": {"text": "درآن نه سایر ماند و نه طایر از بر خاک - دو لک ز لشکر او شد به زیر خاک نهان", "poet": "Onsorî"}
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Arabic",
          "refs": "AFM:141; FVF:613",
          "words": [
            {"translit": "lajj", "gloss": "a large group of people, also the deepest point of sea.", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON:3569",
          "words": [
            {"translit": "lojjeh", "gloss": "the deepest point of sea", "script": "لُجّه"}
          ],
          "note": "See \"Reg: to dye\" for another possible root.",
          "quote": {"text": "کشتی هرکه در این لُجّهٔ خونخوار افتاد - نشنیدیم که دیگر به کران می آید", "poet": "Sa`dî"}
        },
        {
          "id": 12,
          "parent": 8,
          "lang": "Persian",
          "refs": "KLN:856; BQT:1878",
          "words": [
            {"translit": "lâk", "gloss": "red resin, lacquer", "script": "لاک"}
          ],
          "note": "See \"Reg: to dye\" for another possible root.",
          "quote": {"text": "همی گفت و پیچید بر خشک خاک - زخون دلش خاک همرنگ لاک", "poet": "Onsorî"}
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Portuguese",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": "SKT:281",
          "words": [
            {"translit": "lacquer", "gloss": null, "script": null},
            {"translit": "Shellac", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Âleŭos", "redirect": "Al 4"},
      "nodes": []
    }
  ]
}
```


## [2026-09-04T19:34:40.859Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T19:34:40.931Z] TOOL RESULT

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


## [2026-09-04T19:34:50.767Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','AHD','KLN','MON','BQT','AFM','FVQ','FVF','SKT','OEW','LKT','HJB','DEV','PHN','SIN','AID','FSD','WEB','WLD','IEC','SYN','PLA','TAD','ARB','RCH','ARY','MON5']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:600]); print()\n    else: print(k,'MISSING'); print()\n\""
}
```


## [2026-09-04T19:34:50.917Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-04T19:34:53.532Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view", "identifier": "originsofenglish00jose (also originsofenglish0000ship)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are 

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "loo

AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lo

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "lo

RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 =

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

MON5 MISSING
```


### [2026-09-04T19:34:53.571Z] TOOL RESULT

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


## [2026-09-04T19:35:00.442Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==40||NR==41' POK_01.txt | head -80"
}
```


## [2026-09-04T19:35:01.258Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"alek-\" POK_full.txt | head -20; echo ---; grep -n \"alek\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-04T19:35:02.046Z] TOOL RESULT

```
  nachweisbar,  trotz  Specht  Dekl.  114, da  bett.  ali-  ,weiß^  sehr  unsicher  scheint  (Couvreur  H  149  f.,  Friedrich IF.  58,  94)  und  gr.  dllcpalog,  ällcpaTa,  äh^  anders  zu  erklären  sind.
Hierher  aber  wohl  (als  ,bellgelbe  Pflanze^)  hisp.-lat.  ala  ,inula,  Alant^ (Isid.),  span.-portug.  ala  ds.,  dazu  mit  -r^^Suffix  abd.  alaoit  ds.,  damit etymologisch  identisch  der  Fiscbname  abd.  ahmt  (jünger  alant),  as.  alund ,Weißfisch,  Alant'^  =  (mit  gramm.  Wechsel)  aisl.  -qlunn  ,ein  Fisch^,  idg. Grundform  "^al-nt-l^al-ont-.  Die  ursprüngliche  Bedeutung  von  al-  ist  wohl ,weiß,  glänzend^,  daher  dann  auch  ,bellgelV  usw.
Eine  genaue  Trennung  der  Bedeutungen  von  al-  und  el-  ist  nicht  immer möglich,  weshalb  Specht  (Idg.  Dekl.  59,  160)  beide  Stämme  für  ursprüng- lich identisch  erklärt,  also  al-  als  tl-  auf  el-  zurückführt,  womit  er  ferner (aaO.  114)  die  Farbwurzel  ar-  (s.  unten  areg-),  er-  identifiziert.
WP.  I  92  ff.,  WH.  I  26  f.
aldh-  ,Tvoo;'.
Altn.  alda  f.  , Welle,  Feindschaft^;  norw.  dial.  olda  f.  ,Trog^;  schwed.  dial. älla  ,längliche  Vertiefung^  Vgl.  ags.  ealdop.  aldot,  aldaht  ,Trog,  Bottich^, nbd.   bair.  alden  , Ackerfurche^.
32  t
Dcazu  baltoslav.  *aldiiä-  in  ksl.  ladiji,  ahdiji  f.  ^Kahn^^  lit.  aldijä,  eldijä f.  ^Flußkahn^,  auch  lit.  eldijeU  ^Räucherpfanne^
Norw.  lodje  ^russisches  Fahrzeug'^,  schwed.  lodja,  mnd.  lod{d)ie,  loddige sind  aus  russ.  lod'bjd  (=  asl.  ladiji)  entlehnt.  Falk-Torp  652  (s.  auch  789 unter  *olde).
WP.  I  92,  WH.  I  35,  Trautmann  6.
aleq-  ^abwehren,  schützen^,  vermutlich  eigentlich  ^abschließen  und  dadurch schützend
Ai.  rdksati  ,hütet,  schirmt,  bewahrt^,  arm.  aracel  ,weiden,  hüten^  (Pisani KZ.  68,  157),  gv.  dXe^co  ,wehre  ab,  schirme^  (so-Präsens;  raksati  wegen dieser  Obereinstimmung  nicht  wahrscheinlicher  zur  gleichbed.  Wz.  areq-), "AleY-TiOQ,  ^ Als'ATQVibv  epische  Eigennamen,  die  nach  dem  Bekanntwerden des  Hahns  auch  zur  Bezeichnung  dieses  streitbaren  Tieres  verwendet  wurden (Fick  est.  9,  169,  Kretschmer  KZ.  33,  559 ff.,  Boisacq  1091  f.);  älaUslv ,abwehren^,  äXytad'ca  , wehre  ab,  helfe^,  äh/,(xQ  ,Schutz,  Schutzwehr,  Hilfe^, ertal^ig  ,Schutz,  Brustwehr,  bes.  Zinnen  der  Mauern;  Hilfe^  (*aAx-2rt-g), äX%ri  ,  Ab  wehr,  Hilfe^  und  , Stärke,  Kraft^  (letztere  Bed.,  obwohl  an  sich aus  ,energischer  Abwehr^  verständlich,  vielleicht  durch  Zusammenfließen  mit einem  anderen,  dem  mpers.  avh  , Arbeit,  Anstrengung,  Mühe^  entsprechenden Worte,  s.  Bartholomae  Heidelbg.  SB. 
 1916,  IX  10);  dl'/X  TiSTCOidwq  Hom. ; iclyiifxog  ,stark,  kräftig;  von  Waffen:  wehrbar,  zum  Kampfe  tauglich^;
ags.  ealgian  ,schützen,  verteidigen^  (*algöjan)]  got.  alhs  (f.,  kons.  St.) ,TempeP,  ags.  ealh^  as.  alah  m.  ds.,  urnord.-run.  aluh  , Amulett^  (?),  alit. elkas,  alkas  m.  ,heiliger  Hain,  Stelle  auf  einem  Hügel,  wo  man  früher Opfer  verrichtet  hat^,  lett.  elks  m.  ,Götze^  (die  germ.  und  halt.  Worte  ur- sprüngl.  ,heiliger,  abgeschlossener  oder  der  Nutznießung  entzogener  Hain^);
toch.  B  aläsk  ,beseitigen^
S.  die  ähnliche  Wz.  areq-  ,verschließen,  schützend
WP.  I  89  f.
algh-  ,Frost,  Kälte'.
Lat.    algor   ,Frost,    Kälte',    algeö,  -ere   ,frieren',    algidus    ,kalt'    gehören
nach   Liden,   Studien  z.  ai.   und   vgl.   Sprachgesch.   QQ^  zu   aisl.   Gen.  Sg.
elgiar,  nisl.  elgur  m.  ,Schneegestöber  mit  starkem  Frost,  halbgeschmolzener
Schnee'.  Germ.  s-St.  *alnz-  deckt  sich   mit   dem  lat.  algor,  idg.  *alghes-.
WP.  I  91,  WH.  I  29.    Vgl.  Petersson  Ar.  u.  Arm.  Stud.  126.
alg}fh-  ,verdienen,  Gegenwert'.
Ai.  ärhati  ,ist  wert,  verdient,  ist  verpflichtet,  soll',  arghd-h  ,Wert, Geltung,  Preis'  (=  osset.  ary  ,Preis,  Wert'),  av.  ardjaiti  ,ist  wert,  kommt
in    Wert    o-leich^    (npers.    arzldan    .verdienen'),    ar^jah-    (e.s-St.)    n.    ,Wei-t,
rrei:j'.
Gr.  «Aojj;,  yEi'u^erb'^  =  lit.    algä,  apr.    Gen.    Sg.    älgas    ^Lolin*^^    äXcpccvo),
alwsTy  ,einbring-en;  verdienen^  (dlcfsTv  =  ai.  drhati,  aber  durch  das  vollere Prc'is.  dlcpdyd)  in  die  Geltang  als  Aoi'ist  gedrängt)^  dXcpsalßotog  \,Kinder einbringend^
Eine  Nebenform  auf  unaspii-ierte  Media  ist  ai.  arjati  ^erwirbt^  verdient, schafft  herber.
WP.  I  91.
a/p-  ,klein,  schAvach*?
Ai.  dl'pct-,  alpaka-  ^klein,  gering^  (alpena^  alpät  , leicht,  schnell*);  schwer in  der  Bedeutung  zu  vereinen  mit  lit.  alpstü,  alpaü^  alpti  ^ohnmächtig werden^,  alpüs  ^schwach^^  lett.  elpe  Jjuftschöpfen^  Atemzug*^,  alpä  ^Mal, Zeitpunkt^
Anreilmng  auch  von  hom.  dXaTT.advog  (bei  Aeschylos  Xaitaövog)  ^schwach'^, aXana^ü)  ;,leere  aus^  erschöpfe^^  att.  XaTtcct^u)  ^plündere^,  XaTtazTO)  ^leere (den  Leib)  aus^  ist  bedenklich  wegen  ihrer  zweisilbigen  Wzf.  gegenüber der  leichten  der  ai.  und  lit.  Worte;  auch  stehen  sie^  sowie  die  ihnen  an- gereihten XaTtagög  ^schmächtige  dünn^  offenen  Leib  habend^^  Xarrdoa ^Flanke;,  Dünnung  des  Leibes  an  der  Hüfte^;,  X&7ia^og  ;,Aushöhlunge
```


### [2026-09-04T19:35:02.108Z] TOOL RESULT

```
---
280:al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
1228:ALERT al-1 ALEURONE al-4 ALEXIA feg-1 ALEXIPHARMIC alek- ALGOLAGNIA  slég- ALIAS al-1 “ ALIBI al-1, kWo- ALIBLE al-3 ALIEN al-1 ALIFORM_ aks- ALIKE fik- ALIMENT al-3 ALIMONY al-3 ALIPHATIC leip- ALIQUOT al-1, kwo- ALL al-5
1242:ANA- an! ANABAENA gWa- ANABAPTIST g¥ébh-1 ANABIOSIS gWei- ANACOLUTHON sem-! ANACRUSIS kreue-2 ANADEM dé- ANADIPLOSIS dwo- ANADROMOUS der-1 ANAGLYPH gleubh- ANAGOGE ag- ANALCIME = alek- ANALECTS leg-1 ANALEPTIC (s)lag¥- ANALOGOUS leg-! ANALYSIS leu-1 ANAMNESIS men-1 ANAPEST peu- ANAPHORA bher-? ANARTHROUS ar- ANASARCA twerk- ANASTOMOSIS ste-men- ANASTROPHE  streb(h)- ANATHEMA dhé-1 ANATOMY tem- ANCESTOR ked- ANCHOR ank- ANCHORITE ghé- ANCIENT! ant- ANCILLARY kWel-1 ANCON ank-
```


## [2026-09-04T19:35:25.601Z] TOOL CALL #9: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['KLN','SKT','AFM','MON','BQT','POK']:\n    print(k, d[k].get('page_offset'), '|', d[k].get('lookup_hint'))\n    print()\n\""
}
```


## [2026-09-04T19:35:26.567Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"alexein\\|Alexandros\\|Alexander\" KLN_1966.txt | head -20"
}
```


### [2026-09-04T19:35:27.561Z] TOOL RESULT

```
KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

SKT leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.

AFM 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').

MON None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).

BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)

POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
```


### [2026-09-04T19:35:27.609Z] TOOL RESULT

```
73:athetosis,  n.,  affection  of  the  nervous  system  marked  by  involuntary  movements  of  the  fingers  and  toes (med.)  —  Medical  L.,  coined  by  the  American  nerve  specialist  William  Alexander  Hammond  (1828- 1900)  in  1871  fr.  Gk.  affcTO?,  ‘not  fixed’,  and  suff.  -osis.  See  prec.  word, aureomycin,  n.,  an  antibiotic  drug  resembling  penicillin  (med.)  —  A  hybrid  coined  fr.  L.  aureus,  ‘golden’ (so  called  from  its  color),  Gk.  puxr)<;,  ‘fungus’,  and  chem.  suff.  -in;  see  aureate  and  myco-.  The  correct form  would  be  chrysomycin,  in  which  both  elements  are  of  Greek  origin  (see  chryso-  and  cp.  Aureo- basidium).
2129:Alcestis,  n.,  wife  of  Admetus,  one  of  the  Argo¬ nauts  ;  she  offered  her  life  for  her  husband  but was  rescued  from  the  lower  world  by  Heracles (Greek  mythol.)  —  L.  Alcestis,  fr.  Gk.  ’'AXxy)<m;, lit.  ‘valiant,  courageous’,  fr.  d Xxtj,  ‘protection, help,  strength,  power,  courage’.  See  Alexander, alchemist,  n.  —  OF.  alqemiste  (F.  alchimiste),  fr. alqemie.  See  alchemy  and  -ist.
2136:Alcmene,  n.,  the  mother  of  Hercules  ( Greek mythol.)  —  L„  fr.  Gk.  ’AXxp.f)VTr),  lit.  ’the  strong one’,  fr.  aXxf),  ’strength,  power’.  See  Alexander, alcohol,  n.  —  ML.,  fr.  Arab,  al-kohl ,  vulgar  pro¬ nunciation  of  al-kuhl,  fr.  a/-,  the  ,  and  kohl, resp.  kuhl,  ‘antimony  (used  for  painting  the  eye¬ lids)’,  which  is  rel.  to  Heb.  kahal  (Ezek.  23.40), ‘he  painted  the  eyelids  with  antimony’,  Aram.- Syr.  kfhal,  Ethiop.  kahala,  of  s.m.,  Aram. kuhld,  Ethiop.  kuhel,  ‘antimony’.  (Akkad,  guhlu, ‘antimony’,  is  prob.  a  WSem.  loan  word.)Its  mod¬ em  sense  (‘highly  rectified  spirits’)  is  due  to  the analogy  of  the  fineness  of  this  powder.  Cp.  kohl. Derivatives:  alcohol-ic,  adj.,  alcohol-ic-ally , adv.,  alcohol-ism ,  n.,  alcohol-ize ,  tr.  v. alcoholometer,  n.,  an  instrument  for  measuring the  alcoholic  strength  of  liquids.  —  A  hybrid coined  fr.  alcohol  and  Gk.  pixpov,  ‘measure’. See  meter,  ‘poetical  rhythm  .
2147:fight’.  The  first  element  lit.  means  ‘warder  off, fighter’,  and  is  rel.  to  diX^etv,  ‘to  ward,  drive or  keep  off’,  4X4v)TY)p,  ‘fighter’,  4Xxxf)p,  of s.m.  See  Alexander  and  cp.  the  first  element  in next  word  and  the  second  element  in  hippalec- tryon.  For  the  second  element  in  alectryomachy see  -machy.
2158:alevin,  n.,  a  young  fish.  —  F.,  ‘fry,  young  fish’, fr.  OF.  alevain,  fr.  VL.  *allevdmen,  fr.  L.  alle- vdre,  ‘to  lift  up,  lighten,  alleviate’,  in  VL.  also ‘to  bring  up,  rear’,  fr.  ad-  and  levare,  ‘to  raise, lift  up’.  See  lever  and  cp.  elevate.  The  French form  alevin  (fr.  OF.  alevain)  is  due  to  the  change of  suff.  -ain  (fr.  L.  -amen)  to  suff.  -in  (fr.  L.  -inus). Alexander,  masc.  PN.  —  L.  Alexander,  fr.  Gk. ’AXl^otvSpoi;,  lit., ‘defender  of  men’,  fr.  d&iijeiv, ‘to  ward  off,  keep  off,  turn  away,  defend,  pro¬ tect,  and  avfjp,  gen.  avSpO!;,  ‘man’.  ’AXeijeiv  is desiderative  of  (xXexeiv,  ‘to  ward  off’,  which  is related  to  aXxir),  ‘protection,  help,  strength, power,  courage’,  #Xxi|jlo9,  ‘strong’,  and  cogn. with  OI.  raksati,  ‘protects’,  OE.  ealgian,  ‘to  de¬ fend’,  and  possibly  also  with  OE.  ealh,  OS. alah,  Goth,  alhs,  ‘temple’,  OLith.  elkas,  alkas, ‘sacred  wood’,  Lett,  elks,  ‘idol’.  Cp.  Alcmene, alexin,  alexipharmic,  Alexis,  Alexius,  Alcestis, analcite.  Cp.  also  lac,  ‘one  hundred  thousand’. For  the  2nd  element  in  Alexander  see  andro-. alexanders,  the  meadow  parsnip.  —  Lit.  ‘the flower  of  Alexander  (the  Great)’;  so  called  for its  brilliant  color  suggesting  royalty. Alexandrine,  n.,  a  verse  of  six  iambic  feet,  having the  caesura  after  the  third.  —  F.  alexandrin;  so called  because  first  used  by  the  French  poet Alexandre  de  Paris  (de  Bernai)  in  a  poem  on Alexander  the  Great,  dating  from  the  13th  cent, alexandrite,  n.,  a  dark  green  variety  of  chryso- beryl  (mineral.)  —  Named  after  Alexander  II of  Russia.  For  the  ending  see  subst.  suff.  -ite. alexia,  n.,  inability  to  read  (med.)  —  Medical  L., formed  fr.  priv.  pref.  a-  and  Gk.  ‘speech’, from  the  stem  of  XsyEiv,  to  tell,  say,  speak’ (see  lexicon),  but  confused  in  meaning  with  L. legere,  ‘to  read’.  For  the  ending  see  suff.  -ia. alexin,  n.,  a  substance  which  destroys  bacteria (immunology).  — Coined  by  the  German  bacteri¬ ologist  Hans  Buchner  (1850-1902)  in  1888,  fr. Gk.  (xXeEeiv,  ‘to  ward  off.  keep  off.  protect’. See  Alexander  and  chem.  suff.  -in. alexipharmic,  adj.  counteracting  poison,  anti¬ dotal.  —  Gk.  dtXE^i^aptxaxoi;,  ‘acting  as  an  anti¬ dote’,  fr.  aXs^eiv,  ‘to  ward  off,  keep  off,  pro¬ tect’,  and  tpappiaxov,  ‘drug,  poison’.  See  Al¬ exander,  pharmacy  and  -ic.
2161:See  Alexander  and  pyretic.
2164:ward  off,  keep  off,  protect’.  See  Alexander  and
2628:Derivatives:  anagrarnmat-ic,  anagrammat-ic-al , adjs.,  anagrammat-i-cal-ly ,  SLdv.,anagrammatism (q.v.),  anagrammat-ist, n.,  anagrammatize  (q.v.) anagrammatism,  n.,  the  making  of  anagrams.  — ModL.  anagrammatismus,  fr.  Gk.  avaypappa- xiop. 6?.  See  anagram  and  -ism. anagrammatize,  tr.  v.,  to  make  an  anagram  of; intr.  v„  to  make  anagrams.  —  Gk.  dvaypaupia- TtyEtv.  See  anagram  and  -ize. anal,  adj.,  pertaining  to,  or  connected  with,  the anus.  See  anus  and  adj.  suff.  -al. analcite,  n.,  a  white  zeolite  (mineral.)  —  Formed with  subst.  suff.  -ite  fr.  Gk.  dvaXx-fc,  ‘weak, feeble’,  fr.  dv-  (see  priv.  pref.  an-)  and  dXxr), ‘protection,  help,  strength’;  so  called  in  allusion to  the  weak  electricity  it  acquires  when  rubbed. Gk.  dXxfj  is  rel.  to  dXsxE'.v,  ‘to  ward  off’, whence  the  desiderative  verb  dXl'Eiv,  ‘to  ward off,  keep  off,  turn  away,  defend,  protect’.  See Alexander.
2713:andro-,  before  a  vowel  andr-,  combining  form meaning  ‘man’.  —  Gk.  avSpo-,  avSp-,  fr.  avfjp, gen.  avSpfS?,  ‘man’,  which  is  cogn.  with  OI. ndram  (acc.),  ‘man’,  naryah,  ‘virile’,  Arm.  ayr, gen.-dat.  arn,  ‘man’,  Alb.  n'er,  ‘man’,  Umbr. nerus  (pi.  acc.),  ‘men’,  Sabine-L.  Nerd,  PN.,  lit. ‘strong’,  W.  ner,  ‘hero’,  OIr.  nert,  W.,  Co.  nerth, ‘virility’.  Cp.  Andrew,  Andrias,  andron,  dandy, ‘a  fop’,  and  the  second  element  in  Alexander, Ardhanari,  Dianira,  Leander,  philander,  sundari. Cp.  also  the  first  element  in  anthropo-. androcracy,  n.,  rule  or  supremacy  of  men.  — Compounded  of  andro-  and  -xpaxla,  fr.  xpdxoc;, ‘strength,  power,  rule’.  See  -cracy. androecium,  n.,  the  stamens  of  a  flower  taken collectively  (hot.)  ■ —  ModL.,  compounded  of andro-  and  Gk.  oExtov,  dimin.  of  olxog,  ‘house’. See  economy.
2970:anticlerical,  adj.  —  Formed  fr.  anti-  and  clerical Derivative:  anticlerical-ism,  n. anticlimax,  n.,  the  opposite  of  climax  (rhet.)  — Coined  by  Alexander  Pope  (1688-1744)  fr.  anti- and  climax.
3830:athetosis,  n.,  affection  of  the  nervous  system marked  by  involuntary  movements  of  the  fingers and  toes  (med.)  —  Medical  L.,  coined  by  the American  nerve  specialist  William  Alexander Hammond  (1828-1900)  in  1871  fr.  Gk.  dBsxos, ‘not  fixed’,  and  suff.  -osis.  See  prec.  word.
4693:bel,  n.,  a  unit  for  determining  in  logarithms  the ratios  of  power.  —  From  the  name  of  Alexander Graham  Bel l  (1847-1922),  the  inventor  of  the telephone.
5768:Bucephalus,  n.,  name  of  Alexander  the  Great’s favorite  horse.  —  Gk.  Boux^aXo;,  lit.  ‘oxhead’, fr.  poo;,  gen.  poo;,  ‘ox’,  and  xctpotXy;,  ‘head’.  See
6718:casuistry,  n.,  the  resolving  of  questions  of  right and  wrong.  —  Coined  by  the  English  poet Alexander  Pope  (1688-1744)  fr.  casuist  and suff.  -ry.
10761:demarcation,  n.  —  F.  demarcation,  fr.  Sp.  demar- cacion,  fr.  demarcar,  ‘to  mark  out  the  boun¬ dary",  fr.  de-  and  marcar,  ‘to  mark’,  fr.  marca, ’mark’,  fr.  MHG.  marke.  See  mark,  ‘sign’,  and -ation.  The  word  was  first  used  of  the  linea  de demarcacion  (‘demarcation  line’)  established  in 1493  by  Pope  Alexander  VI,  in  order  to  divide the  New  World  between  the  Spaniards  and  the Portuguese.
11221:Derivatives:  diadem,  tr.  v.,  diadem-ed,  adj. diadoche,  n.,  succession.  —  Gk.  SiaSox?),  ‘succes¬ sion’,  rel.  to  81x80/0;,  ‘succeeding,  successor’, in  gradational  relationship  to  SiaSE/ea&ai,  ‘to succeed’,  lit.  ‘to  receive  one  from  another’,  fr. Sid  (see  dia-)  and  Sbyeabou,  ‘to  take,  accept, receive’,  fr.  I.-E.  base  *dek-,  *dok-,  ‘to  take,  re¬ ceive,  accept ;  acceptable,  becoming,  good’, whence  also  L.  decere,  ‘to  be  seemly  or  fitting’. See  decent  and  cp.  words  there  referred  to. Diadochi,  n.pl.,  the  successors  of  Alexander  the Great;  hence  also  successors  (in  general).  — ModL.  Diadochi,  fr.  Gk.  SidSo/oi,  pi.  of  8id- 80x0;,  successor’.  See  prec.  word, diadochokinesia,  diadochokinesis,  n.,  the  normal
13687:esthetics,  aesthetics,  n.  —  G.  Asthetik,  coined by  A.  G.  Alexander  Baumgarten  (1714-62)  about 1750  fr.  Gk.  ocEaflTj-n.xAp,  ‘perceptive’  (see  prec. word),  to  denote  that  branch  of  science  which deals  with  beauty.
14442:feteful,  adj.  —  Coined  by  the  English  poet Alexander  Pope  (1688-1744)  fr.  fete  and  -fid. Derivatives:  fateful-ly,  adv.,  fateful-ness,  n. father,  n.  —  ME.  fader,  fr.  OE.  fader,  rel.  to  OS. fadar,  ON.  fadir,  Dan.,  Swed.  fader,  OFris. feder,  Du.  vader,  OHG .  fater,  MHG.,  G.  voter, Goth,  fadar  (occurring  only  6nce),  and  cogn. with  OI.  pitar-,  Toch.  A  pacar,  B  pacer.  Arm. hayr,  Gk.  narf)p,  L.  pater,  OIr.  athir,  ‘father’. All  these  words  are  traceable  to  pa,  a  child’s word  for  ‘father’.  Cp.  pater,  ‘father’.  Cp.  also expatriate,  impetrate,  Jupiter,  padre,  parricide, patriarch,  Patrician,  patrimony,  patron,  pattern, p6re,  perpetrate,  repair,  ‘to  resort’,  repatriate. Derivatives:  father,  tr.  v.,  father-hood,  n.,  father- land  (q.v.),  father-less,  adj.,  father-ly,  adj., father-li-ness,n.
14662:logist  Albrecht  von  Haller  (1708-77)  and  adopt¬ ed  by  Alexander  Schmidt  (1831-94)  about  1870. fibrinogen,  n.,  a  protein  in  the  blood,  which  pro¬ duces  fibrin  (biochem.)  —  A  hybrid  coined  by Alexander  Schmidt  (see  prec.  word)  fr.  fibrin and  Gk.  -yevl)?,  ‘bom  of,  produced  by’.  See  -gen. Derivatives:  fibrinogen-ic,  fibrinogen-ous,  adjs. fibroid,  adj.  and  n.  —  A  hybrid  coined  fr.  L.fibra (see  fiber)  and  Gk.  ‘like’,  fr.  sTSo?,  ‘form,
15798:Gardenia,  n„  genus  of  trees  and  shrubs.  — - ModL.,  named  after  the  American  botanist Alexander  Garden  ( 1 730-9 1 )■  For  the  ending  see suff.  -ia.
```


## [2026-09-04T19:35:33.758Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^lac,\\|^lac\\b\\|lakh\\|shellac\\|shell-lac\" KLN_1966.txt | head -20"
}
```


### [2026-09-04T19:35:33.822Z] TOOL RESULT

```
4308:balas,  n.,  a  variety  of  spinel  ruby.  —  F.  balais, fr.  Arab,  balakhsh,  fr.  Balakhshdn,  fr.  Pers. Badhakhshin,  name  of  a  region  in  Central  Asia (near  Samarkand),  where  this  variety  of  spinel ruby  is  found.
9741:crore,  n.,  ten  million  rupees,  i.e.  one  hundred lakhs  (Anglo-Indian),  —  Hind,  karor,  rel.  to Prakrit  krodi,  fr.  OI.  kdtih,  ‘end’,  which  is  prob. a  Dravidian  loan  word.
17052:hakim,  n.,  in  Mohammedan  countries,  a  judge, ruler.  —  Arab,  hakim,  prop.  part,  of  hakuma, ‘he  was  wise’.  See  hakeem, halakah,  also  halachah,  n.,  oral  law;  rule  pre¬ scribed  by  oral  law  (Jewish  religion).  —  Mish- naic  Hebrew  hdlakhdh,  ‘rule,  practice,  tradition’, lit.  ‘something  to  go  by’,  fr.  Heb.  halakh,  ‘he went’,  which  is  rel.  to  Aram,  halakh,  hakh,  hal- lekh,  ‘he  went’,  Akkad,  alaku,  ‘to  go’,  Arab. hdlaka  (used  euphemistically),  ‘he  perished’, Heb.  hilekh,  ‘traveler’,  hdlikhd1',  ‘a  going’,  mo-
20947:Derivative:  labyrinthical-ly,  adv. labyrinthitis,  n.,  inflammation  of  the  labyrinth (med.)  —  Medical  L.,  formed  fr.  L.  labyrinthus (see  labyrinth)  with  suff.  -itis. lac, lakh,  n.,  1)  one  hundred  thousand;  2)  a  great number.  —  Pers.  lak,  fr.  Hind,  lakh,  ult.  fr.  OI. Idkfa,  ‘one  hundred  thousand’,  prop,  ‘sign, mark’,  rel.  to  Uksati,  laksayati,  ‘marks,  charac¬ terizes,  defines’,  and  prob.  also  to  rdkyd,  ‘pro¬ tection,  deliverance,  preservation,  observation’, rak$ati,  ‘protects,  delivers,  preserves,  observes’, and  cogn.  with  Gk.  dXi'Eiv,  aX£xsiv,  ‘to  ward off.  See  Alexander  and  cp.  Lakshmi. lac,  n.,  a  red  resinous  substance.  —  Pers.  lak,  fr. Hind,  lakh,  fr.  OI.  lakfa,  lit.  ‘one  hundred thousand’  (see  prec.  word),  a  name  given  to  the insects  Cocca  ilicis,  in  allusion  to  their  great number.  Their  name  is  used  also  to  denote  the resin  of  the  Quercus  cocci/era,  which  flows  from this  tree  in  consequence  of  the  sting  of  these insects.  Cp.  lacquer  and  the  second  element  in shellac.  Cp.  also  the  second  element  in  Phyto¬ lacca.
20974:lacquer,  lacker,  n.,  a  kind  of  varnish.  —  MF. lacre,  fr.  Port,  lacre,  ‘sealing  wax’,  fr.  laca,  ‘gum lac',  which  derives  fr.  Hind,  lakh,  ‘lac’,  fr.  OI. lak.;b,  See  lac,  ‘a  resinous  substance'. Derivatives:  lacquer,  tr.  v.,  lacquer-er,  n.,  lac- quer-ing,  n.
20985:lac,  gen.  lactis,  ‘milk’.  See  lacteal,  adj. lactometer,  n.,  an  instrument  for  measuring  the purity  of  milk.  —  A  hybrid  coined  fr.  L.  lac, gen.  lactis,  ‘milk’,  and  Gk.  pcrpov,  ‘measure’. See  lacteal,  adj.,  and  meter,  ‘poetical  rhythm’. The  correct  form  is  galactometer  (q.v.),  in which  both  elements  are  of  Greek  origin, lactose,  n.,  sugar  of  milk  (chem.)  —  Coined  by the  French  chemist  Marcclin-Picrrc-Eugene Berthelot  (1827-1907)  fr.  L.  lac,  gen.  lactis, ‘milk’  (see  lacteal,  adj.),  and  subst.  suff.  -ose. lacuna,  n.,  a  gap.  —  L.  lacuna,  ‘ditch,  pit,  pool, pond,  hole,  hollow,  cavity’,  dimin.  of  lacus,  ‘ba¬ sin,  tank,  tub,  a  large  reservoir  for  water,  lake’. See  lake,  ‘pool’,  and  cp.  lagoon.
21027:lakh
21031:lakh,  n.  —  See  lac,  ‘one  hundred  thousand  (ru¬ pees)’.
28718:Phytolacca,  n.,  a  genus  of  plants,  the  pokeweed (bot.)  —  A  ModL.  hybrid  coined  fr.  Gk.  9UT0V, ‘plant’  and  ModL.  lacca,  fr.  Hind.  lakh.  See phyto-  and  lac,  ‘a  resinous  substance’. Phytolaccaceae,  n.  pi.,  the  pokeweed  family  (bot.)
33900:scale,  n.,  a  weighing  instrument.  —  ME.  scale,  fr. ON.  skal,  ‘shell,  dish,  scale  of  a  balance’ (whence  Dan.  and  Swed.  skal,  ‘scale  of  a  bal¬ ance’,  Dan.  skaal,  Swed.  skal,  ‘drinking  cup, bowl’),  which  is  rel.  to  OE.  scalu,  OS.  skala, OHG.  scala,  MHG.  schdle,  G.  Schale,  ‘drinking cup,  bowl;  shell,  scale  of  a  balance’,  MLG. schale,  MDu.  scale,  Du.  schaal,  ‘drinking  cup, bowl,  scale  of  a  balance’;  fr.  Teut.  *skelo-, which — according  to  Paulus  Diaconus — orig. denoted  ‘a  drinking  cup  made  from  a  skull’; fr.  I.-E.  base  *(s)qel-,  ‘to  cut,  cleave,  split’  (so called  in  allusion  to  the  skull  as  separated  from the  other  bones  of  the  head).  See  Kluge- Mitzka, EWDS.,  p.  633  s.v.  Schale.  See  shelf,  ‘slab  of wood’,  and  cp.  words  there  referred  to.  Cp.  also scale  of  fish  and  skull.  Cp.  also  scall,  scallop, scalp,  school  of  fishes,  shale,  shell,  shellac,  shield, shoal,  ‘crowd’,  skill.  Cp.  also  Scylla.
34948:shellac,  n.  and  tr.  v.  —  A  compound  of  shell  and lac,  ‘a  red  resinous  substance’ ;  loan  translation of  F.  tuque  en  ecailles,  lit.  ‘lac  in  plates’, sbelta,  n.,  secret  slang  of  Irish  tinkers.  —  Of  un¬ known  origin.
```


## [2026-09-04T19:35:35.163Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==301' SKT.txt | grep -n -i \"lac\\|lack\" | head -30; echo \"=== leaf 300/302\"; awk 'BEGIN{RS=\"\\f\"} NR==300' SKT.txt | head -5"
}
```


### [2026-09-04T19:35:38.199Z] TOOL RESULT

```
1:  as  Spaa,  dtsmajar, to  dismay,  ttrriiy.  The  O.  F.  dtsmaytr was  early  supplanted  by  esmayer  in  the tame  sense,  which  only  rtiffercd  in  substi- tuting the  prefix  cs-  ^L,  ex'\  fcr  du-  <L. dis').  The  latter  part  {'tnayer)  ol  these woids  ib  from  O.  H.  G  magan  (.G.  mtf£^, to  have  power,  Le  able.  Hence  dtjmaytr and  esmayer,  at  first  io  the  intrans.  sense to  lack  power,  faint,  be  di&conraged,  but afterwards,  actively,  to  discourage.  Cf. \is\.  tmaffjrt  (.put  for  ^wwi^rY*),  lolosc courage,  also  to  dismay  (l-Eono).
=== leaf 300/302
keimtticus.  —  Gk.  fuiQi)-
posed   (o  Icam.  belonging  to
\  esp.  to  mathematics.  —  Gk.
em  of  ttii9rffia,  a  lesson.  *  Gk.
Ifetnre  of  fioffiayity,  to  leara.
```


## [2026-09-04T19:35:50.171Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'lac, lakh' in p or ('lacquer,  lacker' in p):\n        print('leaf',i)\n    if 'Alexander,  masc.  PN' in p:\n        print('Alexander leaf',i)\nEOF"
}
```


## [2026-09-04T19:35:50.663Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"^LAC\\|lac,\\|Lacquer\\|LACKER\" SKT.txt | head -20"
}
```


### [2026-09-04T19:35:51.938Z] TOOL RESULT

```
Alexander leaf 36
leaf 460
leaf 461
```


### [2026-09-04T19:35:51.989Z] TOOL RESULT

```
1857:Black.  (E.)  M.  E.  blak.  A.  S-^ blac,  +  Icel.  blakkr.  dark.  Cf.  Do. to  bum,  scorch.  Perhaps  orig.  *«:( and  thus  connected  with  the  idea  of tense  light;  cf.  L.  yKri^narr,  to  bum; BUnk,  Bleak.  Blank.
3571:lack.
9428:Japan,  a  name  given  to  cer- lacquered  work.  (Japan.)  > the  country.     Der./12/aM,  verb,  im  pu.iw
9809:lac;  put  for  raA/d,  lac.  ••  Skt. yp.  of  roAj't  to  dye,  colonr.  redden  ; .  rm^ffOt  colonr,  paint-  Der.  gitm- f-iae.
9837:Laconic,  brief  and  pithy.  (L.  *  Gk.) L.  LaionicHs,  Laconian.  ~  Gk.  Aacaifunir^ Lacooian.*  Gk.  AtUarv.a  Lacoai&n,  Spartan. These  men  wee  celcbrBtcd  for  their  brief and  pithy  locution.
9838:Lacquer;  see  Loo  (i)-
9839:Lacteal.  relRting  to  milk.  (L.)  From L.  lactt-us,  milky.  ••  L.  Ifut-^  stem  of  lac^ milk,  -^  Gk.  ToAturr-,  stem  of  70^0,  milk* Root  unknown.
9840:lettuce,  a  succulent  plant.  (F.  *  L.) M.  E.  Utut€.  >  O.  F.  laictuce*^  laitMU*^ not  recorded,  old  form  of  iautut  iCot.), mod.  F.  iaitue,  lettuce.  ••  L  /ar/aif^a,  lettuce: named  from  its  juiciness. —  L.  Uct-,  stem  of lac,  milk.
9863:La^,  late,  sluggish.  (C)  W.  /fi^.  slack. Ioo%,  sluggish;  Com.  lac,  1oo»e,  remiss. -f L  laxus^  lax ;  see  Lax,  Lansoid.
10438:liken,  to  compare.  (Scaod.)  U. Hkntm,  to  liken  ;  bat  Uie  tnic transitive,  viz.  to  be  like.  — Swed. to  re>emble.  (1)  to  liken,  from Din.  it^Ht,  the  same,  from  Ug. Iiilac,  a  shrub.  (Span.  — Ti Span.  /t7d^.«-TuTk.  iftla^,  a  Ula£.2 Ul^\  liianj,  liiang,  of  which  the  pfO| sen-e  is  indigo*planL  Tne  tittiisl  /cUfl for  ff,  and  the  abore  form&  arc  frqin  a blue,  whence  nilak,  blnct»h.  The  pl| is  named  from  the  blucish  Cil^  «• Aowere  in  some  Tarietics. LUy.  a  planL  Cl-'Ok 't  A.&ldtf. L.  ///iWfli.—Ck.  h€ipiOr,  1  lily. Xiimb  (i).  a  member,  braitcb (E.)  M  K.lim.  A.S.  A'M.*f  t Dan.  Sued.  Um,
10507:LitmtiB,  a  kind  of  dye.  (I>n)  Corrupted from  Du.  lakntots,  a  blue  dye-stuff  a-Du. lak^  lac:  moes,  pulp,  -f"  G-  l^lif'ims,  lit- mus ;  bom  lathy  lac,  mus^  pulp.    .Sec  Lao.
23087:lace— lasso.
23647:French  from   PortHguese  fro. from  Sanskrit :  lacquer  flacker)
```


## [2026-09-04T19:36:06.401Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9800,9815p' SKT.txt; echo \"=== leaf:\"; python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'put  for  raA/d' in p or 'Lacquer;  see' in p:\n        print('leaf',i); print(repr(p[:300]))\nEOF"
}
```


### [2026-09-04T19:36:07.912Z] TOOL RESULT

```
labiate.  (L.)     A  botnnical  lerm.  *  L. hh  urn,  a  Up:  with  suffix  aft  (L.  -o/aa). Laboratory ;  see  Labour. Iiabotir.  toil.    (F.  -  L)     M.  E.  /a/wir. —  O.  F.  /a/>citr  (later  /a/ri*r).-L.  lahcrtfHt ace  of  /0i^r,  /ii^M,  toil.     Allied  to  rvdur, itivnpth.     (v^RABU.) bwabotiP.  (F.  -  L.  I  with  t^prtJU,)
Coined  by  prefiring  E.  ir-  («*r1  *» ia^tmr,  a  word  of  K.  origin  (•bow,
elaborate.  (Ui     I.-  riahoratm,  pp tlahorart,  lo  labour  greatly.  —  I-  /. greatly;    Uhcf-art,  to  work,  froia labour.
laboratory.    (L.^      Formerly /»f7  (Blount  r.  *  O.  F.  f/it/vm/MWj Formed   from  L.  tiatternim^  pp. ni'T,  to  cUtiOfate,  work  oat,
laborioua.  (F.  -  L)  M.  E  ' ritms.  •  F.  hbontux.  —  L..  4i»rt toilsome.  — L^  /isAfln-,  crude  £atm  i^i la  boor.
LABURNUM.
atiee.  (I.)    h,  Mmrmtm, ^  xvi.  l8.  fcthApi^a/&urrtum, rinth.  a.  muc.  /F.  -  L.  -  Gk.) rintkt.  ••  L.  Iaf>yrinthHS.  •  Gk.Xa- r.  «  mue.  a  pUce  full  of  Unes  or
Pet  for  kafvpt»9oti    Irom  Ktxfpn, >iQi/pa,  ft  lane. (1),  a  rninuttft  substance.  (Pert.—
Pen.  /ai«  /«>,  gum-Uc,  whence t  lake  is  obtained  for  dyeing.  —  Skt.
lac;  put  for  raA/d,  lac.  ••  Skt. yp.  of  roAj't  to  dye,  colonr.  redden  ; .  rm^ffOt  colonr,  paint-  Der.  gitm- f-iae.
tiar,  looker,  a  sort  of  vamith.  (F. -Pctv-Skt.)  F.  lacn  (Cot.V- errv.  icatini^'Wax.  — Port,  laca,  gum- en  la^,  gum  lac  (above).
I  (}),  a  crimsoD  colour.   (F.  — Pen.
K  iaque  i.Cot. )  —  Pers.  idk,  lake. Zai,  gain-lac  (above). \j\  %  hundred   thouMind.  (Hind.*
Imni  iai  <  alw  t4Mh),  a  lac  -  bkt. ft   hundred    thou&and;    appatently Cemce  to  the  number  of  lac-insccti It ;  see  I*ao  ( i ).
.  a  cord,  lic.   (F.-L)     M.  E.  iai, 0.  F. /ar,  /o^i,  a,  snare,  noose. —  L. -,  a  ncoic,  ariare,  knot.     Allied  to T,  to  allnre;  <f.  E.  tlicit,  dt light. t>.  a  noose.  (Spnn.  —  L.)
EL  lu):  mod.  bpan  toio,
=== leaf:
leaf 258
'    (The  a  is  long.)\naloor&n;  thesame  word  with  ibe  Ah dcf.  art.  a/  (the >  proAjced. Kythe;  see  Oia  (i).\nIiab«l :  see  I<ap  (i). I«abial.  (L.)     l^tt  L.  laHatu,  perlaio- ing  (o  the  lips.  *  L.  /ahum,  the  lip.     See Z#ap  it).  Lip.\nlabellum.  a  pendolons  petal.  (L.'
leaf 259
' These  men  wee  celcbrBtcd  for  their  brief and  pithy  locution.\nLacquer;  see  Loo  (i)-\nLacteal.  relRting  to  milk.  (L.)  From L.  lactt-us,  milky.  ••  L.  Ifut-^  stem  of  lac^ milk,  -^  Gk.  ToAturr-,  stem  of  70^0,  milk* Root  unknown.\nlettuce,  a  succulent  plant.  (F.  *  L.) '
```


## [2026-09-04T19:36:34.255Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM leaf ~141+8=149 ===\"; python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i in (147,148,149,150,151):\n    print('---leaf',i,'---')\n    print(pages[i][:1500])\nEOF"
}
```


## [2026-09-04T19:36:35.527Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HJB lakh/lac ===\"; grep -n -i \"LAKH\\|LAC, LACQUER\\|^LAC\" HJB.txt | head; echo \"=== LKT ===\"; grep -n -i \"lakh\\|Lack\\b\\|laca\\|lacca\" LKT.txt | head -20"
}
```


### [2026-09-04T19:36:35.998Z] TOOL RESULT

```
=== AFM leaf ~141+8=149 ===
198
---leaf 147 ---
ܕ 311 تب
( الأست) كامة فارسية اسم للبن ومنة التكردي ,)ܝܝ و ܡܣܬܐ بالسريايّة
الدارحة
(ل) ل قيل فارسي ° ( يط الحيط) والصواب !2 تري
0 المس) النحاس 7
+ ܢ الغلام اسن 85 والوحه 39 00 7 5 امن ܘܟ 0
~ ÷
( !]ܚܝ ) فاسي خض وهو 3 الكف ومنة - بالتركة » 2
0 نوع من اطيب :9 فاسي ܕܫܐ ܐܘ ام ام اللرذان ܠܝ الفرس ]
سمعوا بام جرذان وهي كع صفراء قالوا ܐ جاغوا:« اين موثمان» ( اقرب
ܬܕܐܙܒ) ܕܐܐ ܐ نه
( | هد ) اللقاح 09 وقيل 00 ( 3 .قال في شفاء الغليل 1 `
عق الباذجان معرب
(اللان) 3 مان ܕܬܕ كل عار مانع
(الأملم) دواء ٠‏ وهو ܳܨ ܚܨ ينبت في الهند معرب 11
(النج) منك ك وهو حب اذا أكل < 1 وغير عمَلهُ
1 ܨ ܐܥܘ معرب" ܐܥ وهو ܬܐ )ܒܐ ܐܝܕܒ واضاا
مسه
( | ܐ̈ܫܢܟ ) آلة 2 ܨ 007 ` }1 ܝ اي اناما د
مق ٠‏ وقال ܐ دص :1م 00 0 39
< من 00 وهذه 0 0 ` الواسطة .
ايخ ] ܡܝܓܢܝܩܐ ܐܥ ® ٠و‏ ثممل ان يكون اصل اتكلمة فارسا ` 31
الام مأعذة ع مهنيد يك كا سبى اقول مةئ لك له 001
اساوب ܗ ܐܗܨܢ أو ܚ 5 5 الارتفاع الى فوق وكان
اسم ܬ 06 !]£ ماء £ ويضعون فيه دق 20:03 3 ܢ
2 ان ܣ واحدة فواحدة من الإناء وذلك لا نهم كانوا يطمقون £ الاناء متجتونا
---leaf 148 ---
< 3:(+ 3 3
يضعون عليه قليلا من اللح ٠‏ فبقدر ما كان يذوب الملح كان الماجنون يخاو ܬܨ تلك
الاحجار الدقيقة الى الخارج
مانيذ ) الجرية: بقيتها مأخوذة من مأرنيده اي 01
+ 0 5144 ܨܢ منش )3 10 الهّة ويوافقفة ܨ 1165
والانتكليزي 11170 ܕܐ ريق 14 اي فكر ونأ ܨ
0 )ܕܐ )381 05 7 موتر اي‎ ١
ܢ‎ 491 3
1 2 ܝ الغنى مأخوذ من معيكار اي دأ به العظمة
1 الخاتم فارسي 59 فعا وقالوا مهرَ
ܫ 0 الور ܟ واصل 1 0 حافظ |
7 0 0 6 90 49577 35 610 والعاؤقة
جان) عد الفرس مركب من 3309 331
06 (3061 ܚܚ اول الشماء 0 نقدم عند ܨ 3 0:3 0-3 بق في ܡ
وهو اليوم السادس عشر من شهر « ܝܢ * وذلك عند نزول ܐܚܨ ا >
للفرس عيدان كبيران ررك 795 56 0 7 5( 5 أن الله
580 فرش فيه 000 9 ܗ يع الأجسام 77 للارواح ܐܨ 105
6 0 الازك واكم م كانوا يترون فيه على جميع الرعايا وال بايا
فيقدمون خم الطعام ܝܢ ب قوم الى 0 11 42 7 ني ذلك اليوم ٠‏
فل كارا لنجاتهم ܦ 4 4 من ظلم ܡܓܢ 31 4:83 01 سئة : ܐ 0
اردشير بن بابك وضع ܝ هذا ܟ .0 رأسه تأجة 31 الذي كان 0750 مثل
الشمس ٠‏ وسن على خلفائه من الملوك ان يعقدوا في ذلك اليوم نفسه التاج على روس
اولادهم ويطلوا أجساءهم بدهن البان٠وكان‏ اأوابذة في المهرجان يدخاون على الماوك
كل ` حاملين 4 ج .ܗܘ ܝܐ 50:4 ܐܝܝ ܐܝܢ والعنب الابيض
1 ܫ 0 في ذلك اليوم من تلك الاثار ودهن 250
00 البان :03 عليه ماء الورد سلم حى م 00 منْ جميع الأوجاع 26
---leaf 149 ---
د < 35
3010 رةه كامت النساء 3 1011 لعة فيها ܐܠܝ تمر يبب هر رهي
خرزة لوا ` كاون المرجان
ܢ مره
# ( مضل ) 5 5 مركب من مه اي كبير وسالي لي .مسن
1 ܨܝ § البأورة تعريب مما وهو حجر شه 5 وقيل هر ܐܐ تبه
ملو ول يوان فقيه الفرس ܠ المجوس 3:5( وججعة
ܨ
( لوم ) ببى الشبع فارسي تكلموا 4 0:27 ܨ
(ليَة) فشر بشىء من ܇ الأدرية ܣ من ܐܝ اي الخير 1:0 يبه اي
ܝ
( الميبحتج » العنب المطبوخ مركب من تمي )1١(‏ اي <> ومن إبخته اي مطبوخ
وهو عسبل العنب ١‏ كن الاطباء يغلونة مرة ثانية »= والعسل
4 فشحة مجبهة همده 18 رلم اليل قل كلمن انام 1ه
ܨܐܘ واضبطرابه عند السباق٠وقيل‏ هو من الوَدْن لان الل رون فيه «بحبط
الجيط ‏ ܢܘܛ رأبي ان الميدان ܠܚܢ الاصل وهر مركب من ,مي اي الشراب ومن
:0 وهى : الأدوات ܐܛ تاحق الاسماء ܐ¿ على 5 13 £ اول الام
5 3 5 .يشر بون فيه امن ثم اطلتوم على الفسيعة المدء اسان
واعب الخيل ٠‏ وهر مردان بالتركية والكردبة
(( ܨ » الطعام والحوان عليه الطعام ٠‏ قيل ܐܬܐܬ مشتقّة من ܘ ععنى اعطاه
دعي فاعلة ܬܶܢ مفعولة لان الماك ]ܪܬܐ للنامن اي اعطاهم اياها , «وقيل من ماد كيد
اذا تحرك ( اقرب الموارد ) انها | معربة عن ܚܬܪܘ وهو خبز المسميذ با لفارسة 1
܀ لإن صاحب البيت اذا ܐܘ ضيف ܪܟ له من خْبز ܢܒ ܐܰܢ على الموان وأطلقت
5 * بالفارسة على الموان والذي يخدم ( 55 المانيدة 7450("
)١‏ وشرب الفاريي مي 0 0 4 اي سك واامونالي 40¡ أي
1
ܝ
---leaf 150 ---
_ 4¿ ܙ -
وا لندة 80( 3 اما فرتكل 5 ان اللاندة تعريب 1 `
(ص: ܥ )
6( بالياء 9 بهمزة ܓ 5( فيها الماء والمثقب ويقال
2 وصفها ابن السكيت والفراء وابو حاتم ٠‏ وفي التهذيب عن ابن الاعرابي : ويقال
اللمازاب 3 0 يتقديم الراء المهمة وتاخيرها ونقله الليث وجساعة ( اقرب
الوارد» :قات ان ܐܠ ܐܢ ܨ ܝܢ من ܘܬ اي بول ومن آب اي ماء ܕܝܙܝ النسمية
ظاهر (راجع ` لكل :4 )
ܣ 10 ® 099 2 من مي اق شراب بم الى"
.܀
ܗܐ
9
١‏ ابابا 6 فول الذي 'يككل به فارسيّة ميل ` = ܟ اله
معرب عن اليونافي «</نم٠‏ فالفارمي ايضاً ܨܕ ܝ عن اليونافى وملة ايضاً
ܡܝܠܐ بالارامسية .وما الم للمسافة فهو تعر يب 00 509 (© ܘܐ
بالارامية
*« (المثاء) عق جوقر الزجاج تريب الفارسي مثا وير به 4 الفرني 0081
والايطا ليالي 56 ܙ 1܀] اذى مرمئ السيةء+ة فأخرذ 9 ن الادائي ° ܠܡܐܢܐ والارائي
4 4 مالحوذ من اليوالي ܬܨ(
( ® نات له ورق سُدِيهِ بورق الكر رم البري تعر بيب 8596
باب النون
± 7
» ( الا نوب) ما بين الكعبين م الل اي ܝ النبات ما بين عقدتنه
ويستعار كن ܥܕܝ وسيب ل لر ܟܝܢ ܚ ܨܝ || ܀ ^ له . ܘ ,ܝܝ ܐܟ ܢܬ
المسداة 90 4 :3 ويطاق ايأ على ܐܳܝܰܐܺܝܢ الاناء واللولى ٠‏ والا تنب 0477
---leaf 151 ---
ܢ ܀ © | ܝܝܚ
لغتان فيه ٠‏ والظاهر ان الافظة ارامية الاصل ذعي ܐܢܒܘܒܐ باللغة البابليَة
ܕ ܐܝܟ ܨܐܬ و > دنه حدم ܐܬܐ .ܕ % ܨܝ ܨ ܝܨ 811 )ܙ(
ومعئاها الأننوبة والمزمار ܨ ܐ من ܢܒܒ اي صرخ وتخ ٠‏ .وان ܒܝܒܐ
و ܒܘܒܝܐ اى المجرى والة: ناة 885 | ܗ ܐܐ ܨ ]711 (راجع كلمة
ندب في هذا ܐܐܝ “راجع @ فرئكل ص 7١:‏ )
ܨ عر شجرة 0 و يم عاد ܐܒ وتفاحي مكلك انع
(الأنار) فارسي محض اي 21( واصل 0 المت ومنسة الارائئ”
ܐܡܒܪܐ ܙ !ܚܐ او عشمار بالتركة والكردنة 87 ܐܕ 27 000 متنا 101
اواليو الي بومتومن؟ 9 ܬܘ
ܪ الذي يد 90 صوف تعر يس الإريده أي غير روز
ومنه ܢܒܪܢܢܢܐ بالارامسة
( التبهرج ) الدرهم ازيف الردي تعر يبب ܘ واصل ܫܐ د
( |( ;| ) 7 اسود وابيض واصلة اغلظ من الاصبع يتفرع كثيرا معرب
كدان .ܕܠܐ لغة فيه ومنة السر بالى ܐܓܕܢܐ
# ( الجر والتخر) الاصل والمسب تعريب ܐ¿(
1 وقال فلك 1 ل
عن اليوناللي »ܕ«
53( 5 تمر يت نكل وهو 3088 دقار ف) 305
اي ولده
( النخ ) بساط طولة 7 من عرضه معرب 3
( ||[ 1 0 ننس 4:0 مأخوذ .0 6 وهو ا من ܐܕ 3 ܚܬܐ ومن
0 3 صاحب
0010( 0 هراس ܬܐܘ ܇ : 10801:11 1 56200020
110001 ,12ع0116ه 111011023[211111/
.5 11116 ,011 ه11
```


### [2026-09-04T19:36:36.054Z] TOOL RESULT

```
=== HJB lakh/lac ===
2584:c.  1350.— "The  mountains  of  Badakhshan have  given  their  name  to  the  Badakhshi  ruby, vulgarly  called  oZ-Balakhsh.  "—Ibn  Batuta,
3377:BENGAL,  n.p.  The  region  of  the Gan^  Delta  and  the  dmricts  im- mediately above  it;  but  often  in English  use  with  a  wide  application to  the  whole  territory  ^msoned  by the  Bengal  army.  This  name  does not  appear,  so  far  as  we  have  been able  to  learn,  in  any  Mahommedan or  Western  writing  before  the  latter part  of  the  13th  century.  In  the. earlier  part  of  that  centurv  the Mahommedan  writers  generally  call the  province  Lakhnaotiy  cSter  the  chief city,  but  we  have  also  the  old  form Bang^  from  the  indigenous  Vanga. Already y  however,  in  the  11th  century we  have  it  as  VangcUam  on  the  Inscrip- tion of  the  flreat  Tanjore  Pagoda. This  is  the  olaest  occurrence  that  we can  cite.
3380:c.  1260.— *<  Muhammad  Bakhtiy^r  .  .  . returned  to  Beh^.  Great  fear  of  him  pre- vaUed  in  the  minds  of  the  infidels  of  the territories  of  Lakhnauti,  Behar,  Bang, and  Kj&mTiip.'*—Tabaidt'i-Ndnrit  in  Elliot, ii.  807.
3929:totftt,  *a  well,'  which  comes  near  the Guzerati  forms  mentioned  below.  A great  and  deep  rectangular  well  (or tank  dug  down  to  the  springs^  fur- nished with  a  descent  to  the  water by  means  of  long  fli^rhts  of  steps,  and generally  with  landings  and  logme where  travellers  may  rest  in  the shade.  This  kind  of  structure,  almost peculiar  to  Western  and  Central  India, though  occasionally  met  with  in Nortnem  India  also,  is  a  favourite object  of  private  native  munificence, And  thougn  chiefly  beneath  the  level of  the  ground,  is  often  made  the subject  of  most  effective  architecture. Some  of  the  finest  specimens  are  in Guzerat,  where  other  forms  of  the word  appear  to  be  woo  and  wdin.  One of  the  most  splendid  of  these  structures is  that  at  Asarwa  in  the  suburbs  of Ahmedabad.  known  as  the  Well  of Dhai  (or  *the  Nurse '^  Harur,  built  in 1485  by  a  lady  of  tne  household  of Sultan  Mohammed  Bi^ara  (that  famous *  Prince  of  Cambay  celebrated  by BuUer — see  under  CAMBAYX  at  a cost  of  3  lakhs  of  rupees.  There is  an  elaborate  model  of  a  great Guzerati  hdoU  in  the  Indian  Museum at  S.  Kensington.
5607:GAYOLAQXJE,  s.  Kayu=='^^'ood; in  Malay.  Laka  is  given  in  Craw- furd's  Malay  Diet,  as  "name  of  a red  wood  used  as  incense,  Myridica iners,**  In  his  Descr.  Did.  he  calls  it the  ^^Tanarius  major;  a  tree  with  a red-coloured  wood,  a  native  of  Sumatra, used  in  dyeing  and  in  pharmacy.  It is  an  article  of  consiaerable  native trade,  and  is  chiefly  exported  to China"  (p.  204).  [The  word,  accord- ing to  Mr.  Skeat,  is  probably  kayu, *wood,'  lakh,  *red  dye  ^  (see  LAC),  but the  combined  form  is  not  in  Klinkert, nor  are  these  trees  in  Ridley's  plant list.  He  gives  Ldka-laka  or  Malafca  as the  name  of  the  phyUanthus  emblica.]
5780:GHANK,  GHUNK,  s.  H.  sankk^ Skt.  sankha,  a  large  kind  of  shell {Turbinella  ra.i)a)Jprized  by  the  Hindus, and  used  by  tnem  for  offering  libations, as  a  horn  to  blow  at  the  temples,  and for  cutting  into  armlets  and  other ornaments.  It  is  found  especia^  in the  Gulf  of  Manaar,  and  the  Ghank fishery  was  formerly,  like  that  of  the pearl-oysters,  a  Government  monopoly (see  Tennenl^s  CeyUm,  ii.  566,  and  the references).  The  abnormal  chanky  with its  spiral  opening  to  the  right,  is  of  ex- ceptional value,  and  has  been  some- times priced,  it  is  said,  at  a  lakh  of rupees  !
8823:DINAPOBE,  n.p.  A  well-known cantonment  on  the  ri^ht  bank  of  the GUnges,  being  the  station  of  the  great city  of  Patna.  The  name  is  properly Ddndpur.  Ives  (1755)  writes  Dunapoar (p.  167).  The  cantonment  was  estab- lished under  the  government  of  Warren Hastings  about  1772,  but  we  have failed  to  ascertain  the  exact  date. [Cruso,  writing  in  1785,  speaks  of  the cantonments  having  cost  tne  Company 25  lakhs  of  rupees.  (Forbes,  Or.  Mem. 2nd  ed.  ii.  445).  Tnere  were  troops there  in  1773  (Gleig^  Life  of  Warren Hadings,  i.  297.J
10507:chiefly  covered  with  jungle.  The name  is  a  form  of  the  ancient  Gauda^ meaning,  it  is  believed,  *the  country of  sugar,'  a  name  applied  to  a  large part  of  Bengal,  and  specifically  to  the portion  where  those  remains  lie.  It was  the  residence  of  a  Hindu  dynasty, the  Senas,  at  the  time  of  the  early Mahommedan  invasions,  and  was  popu- larly known  as  Lakhndoti;  but  the reigning  king  had  transferred  liis  seat to  Nadiya  (70  m.  above  Calcutta) before  the  actual  conquest  of  Bengal in  the  last  years  of  the  12th  centiury. Gaur  was  afterwards  the  residence  of several  Mussulman  dynasties.  [See Ravensha/w,  Gaur,  its  Ruins  and  Inscrip- tions, 1878.]
12862:LAC,
12880:LACGABIVE  ISLANDS,
=== LKT ===
651:dem  Pers.,  etwa  pük  Horn  NpEt  S.  75, Nr.  339  '^Brennholz'],  ebenso  tk.  bakam; hieraus  rum.  bäcan  'Blauholz',  russ. bakan  Tlorentinerlack'.  Bakkam  ist dasselbe  wie  Fernambuk-  oder  Brasil- holz, Caesalpinia  echinata  Lam.,  seit  der Entdeckung  Amerikas  unser  gebräuch- lichstes Rotholz,  das  die  Portugiesen 1.540  in  den  südamerikanischen  Wäldern in  großen  Mengen  fanden  [wie  Haema- toxylon  campechianum  L.  oder  Cam- pecheholz unser  gebräuchlichstes  Blau- liolz  ist].  Im  angloind.  sappanwood  ist wahrscheinlich  tamul.  shappu  oder  ma- layäl.  shappannani  "rot'  als  Grundwort anzusetzen.  Der  dritte  bereits  genannte Name  Brasil  oder  Brazil,  schon  im Mittelalter  gebraucht,  ist  noch  nicht  er- klärt.   [Hobson-Jobson  794.
680:'2U3.  Ar.  Balkis: X.  pr.,  Name  der  sagenhaften  Königin von  Saba,  die  zur  Zeit  Salomos  lierrschte, vgl.  Koran  Sure  27,  wo  der  Name  aller- dings nicht  genannt  wird.  Nach  A.  Rösch, Die  Königin  von  Saba  als  Königin  Bil- qls.  Eine  Studie.  Leipzig  1890  ist  das ar.  Wort  vom  gr.  uaWaKiq  'Kebsweib' abzuleiten  [das  gr.  Wort  mufs  selbst  wie lat.  pallaca  vom  hebr.  oder  phöniz.  pi- leges  'Kebsweib,  Buhle'  kommen;  die Benennungen  unsittlicher  Personen  und Verhcältnisse  pflegen  von  dem  niedriger stehenden  Volk  aus  dem  Sprachschatz des  höher  gebildeten  übernommen  zu werden].  Nach  Löbel  EITAP  11  soll mit  Berufung  auf  Laurian  §i  Maxim, Glosariu  de  vorbe  sträine  In  limba  ro- mänä.  Bucure§ti  1876,  p.  50  das  Wort im  Türkischen  die  Bedeutung  'dick  und groß'  haben  [fehlt  aber  bei  Kelekian Kämüs].  Hieraus  rum.  balciz,  halcäz 'garstig,  plump,  stämmig'.  —  Die  von Löbel  a.  a.  0.  gegebene  Ableitung  vom gr.  TTaXaid  KüZiKoq  'Ruinen  von  Kyzikos am  Marmarameere'  ist,  weil  semantisch unzulässig,  abzulehnen.
1459:'Keil;  Klotz  oder  Stock  als  Marter- instrument zur  Bastonnade'  [Beschrei- bung von  CHERBONNEAU  in  JAs  1849, I,  546] ;  hieraus  kat.  span.  falca  'Keil', pg.  fälaca  'Bank  zur  Bastonnade',  rum. /'a/aH^'a 'Stockschläge  auf  die  Fußsohlen'; poln.  falagi  plrl.  in  der  Redensart  zadac komu  t^gie  falagi  'jmd.  verprügeln'. [DE  262.  Devic  DEt  114.  ML  3164  u. 315L    Karlowicz  420/421.
2230:'Kragen'  [Stamm  jak,  jan  'Seite,  Ufer, Rand'  Vämbei-y  TktEt  Wb  S.  1 12,  Nr.  123] ; hieraus  rum.  laca  'Halskragen'.
2600:Geldbetrag  von  lOÖ  Lakhs  [s.  hier Nr.  1295],  also  10  Millionen;  hieraus angloind.  crore.  Eine  Crore  Rupien war  viele  Jahrzehnte  lang  der  genaue Gegenwert  einer  Million  Pfund  Sterling; engl,  a  crore  of  rupees.  [Hobson-Jobson 276.
3019:'Marke,  Fleck;  hunderttausend',  [und nach  den  100000,  d.h.  unzähligen  In- sekten Cocca  ilicis,  welche  durch  ihren Stich  auf  quercus  coccifera  die  harzige Absonderung  bewirken]  'Lack';  hieraus in  der  urspiünglichen  Bedeutung  bind. läkh  '100000',  engl,  lack  'dass.,  bes. 100000  Rupien'  und  ferner:  sp.  pg.  laca 'Lack',  ZßCT-e 'Siegellack',  frz  Jag?«e 'Lack', it.  lacca  'Lack,  Siegellack',  rum.  lac; engl,  lac,  ndl.  lak,  dtsch.  Lack  und  engl. shellac  [eigentlich  'Schalenlack',  da  er zu  kleinen,  dünnen  Täfelchen  geformt wird],  ndl.  schellak,  dtsch.  Schellack; russ.  lak,  Vb.  lakirowat',  bulg.  serb.  lak, Vb.  serb.  lakowati,  Cech.  lak,  Vb.  lako- vaü,  poln.  lakier,  Vb.  lakierowac.  [Hob- son-Jobson  499/501.  Dozy  Oost  57/59. Kluge  274.  DE  295/296.  Devic  DEt 150/151.    Gorjajew  180.
4516:2004.  Ar.  taläk: 'Ehescheidung' ;  hieraus  pg.  talaca  'Schei- dung'.   [DE  347.    Eguilaz  .500.
4772:'Läufer,  Eilbote'  [vom  Stamme  jol,  ol. ul  'gehen',  Vämbery  TktEtWb  S.  134. Nr.  145  I];  hieraus  [wohl  am  wahrschein- lichsten über  ngr.  oüXdKnt  MSOS  II,  239] frz.  laquois,  it.  lacM,  sp.  pg.  lacayo 'Diener';  dtsch.  Lakai.  Unmittelbar wurde  übernommen  rum.  olac  'Schnell- post', oläcar  'reitender  Eilbote'.
4927:2207.  Chiu.  zat-liao: 'Chinesischer  Lack';  hieraus  sp.  charol 'leuchtender  dauerhafter  Lack',  Vb.  cha- rolar  [Dicc  Ca<f  696  c],  pg.  charäo,  xa- räo  'chin.  Lack'  [Constancio  Dicc  974a]. [ZfromPh  XXXV,  568.    ML  9606.
5877:Schäker  1788 schäk-ern  1788 Schakren  j  17i>8 Schal  1802 Schalet  ].  1804 Schalotte  119 Schamane  1928 Schanifott  653 schamponieren  417 Schanze  1059 Scharlach  1794 scharlät  iiilid.  1794 Scharriic'arri  1849 Schasmin  942 Schauhe  737 Schaum pun  417 Sc/iaii/e  j.  1927 Äc/iea«  St.  1771 Schebecke  1740 Scheck  1762 Scheich  1775 Schellack  1295 «■cAer/f  1852 Schibbolet  1891 schicker  ].  1787  b Schicksei' j.  1789 Schikane  434 Schin(hiindchen )  420 Schlamastik  j.  1920 Schlammassel  j.  1920 SfA/t«/'  j.  1804 Schlemiel  1882 Schlemihl  1882 Schlimasdlnik  j.  1920 Schlimasel  j.  1920 Schmuck  1946 Schmiere  (stehen)  j.  1813 Schmu  (machen)  j.  1884 .Sc/if/i?iZ  j.  1811 ÄcÄ»«««  j.  1884 schmusen  j.  1884 Schmuser  j.  1884 Schoberbartel  j.  259 schofel  j.  1751 Äf/io^e  j.  1927 Schübe  mhd.  737 Schuhjack  1679 SefeZ^os  j.  184  a sf/"eZ«  j.  2210
7442:Pacorus  569 pallaca  203 pandura  2015 paradisum  1631 pascha(Ks)  1652 pastinaca  912 pelusia  1647 penidium  583 jp?M^e«  887 pomarancia  1555 pontica  (niix)  355 pyramis  1457
8306:lacayo  2130
```


## [2026-09-04T19:36:46.094Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT 1295 ===\"; sed -n '3014,3020p' LKT.txt\necho; echo \"=== HJB LAC ===\"; sed -n '12862,12872p' HJB.txt"
}
```


### [2026-09-04T19:36:46.158Z] TOOL RESULT

```
=== LKT 1295 ===
1293.  Ar.  lakkät:
'Zange'  [vom  Vb.  lakat  'fassen,  auf- heben']; hieraus  mit  ar.  Art.  sp.  alicates, alicantes  'Biegzange',  frz.  alicate  'kleine Zange,  Heren  sich  die  Klempner  bedienen'. [DEFREMERY  in  JAs  1862,  I,  92.  DE 140.  DevicDEt22.  Lammens  Rem  14/15.
1294.  Ar.  laklak:
'Storch'  [onomatopoetische  Bildung  nach dem  Klappern  des  Schnabels,  ebenso  wie ass.  lakalaka  Del  HWB  885  a],  ebenso tk.  leklek,  vulg.  lejlek  [mit  Erweichung des  Gutturals  wie  in  Beg  >  bej,  s.  hier Nr.  282]  'Storch,  Kranich';  hieraus  rum. liliac  'Fledermaus';  serb.  lelek,  lilak, Cech.  lelek,  klruss.  lelek,  russ.  leklek 'Storch'.    [Gorjajew  184.
1295.  Sskr.  läksä:
'Marke,  Fleck;  hunderttausend',  [und nach  den  100000,  d.h.  unzähligen  In- sekten Cocca  ilicis,  welche  durch  ihren Stich  auf  quercus  coccifera  die  harzige Absonderung  bewirken]  'Lack';  hieraus in  der  urspiünglichen  Bedeutung  bind. läkh  '100000',  engl,  lack  'dass.,  bes. 100000  Rupien'  und  ferner:  sp.  pg.  laca 'Lack',  ZßCT-e 'Siegellack',  frz  Jag?«e 'Lack', it.  lacca  'Lack,  Siegellack',  rum.  lac; engl,  lac,  ndl.  lak,  dtsch.  Lack  und  engl. shellac  [eigentlich  'Schalenlack',  da  er zu  kleinen,  dünnen  Täfelchen  geformt wird],  ndl.  schellak,  dtsch.  Schellack; russ.  lak,  Vb.  lakirowat',  bulg.  serb.  lak, Vb.  serb.  lakowati,  Cech.  lak,  Vb.  lako- vaü,  poln.  lakier,  Vb.  lakierowac.  [Hob- son-Jobson  499/501.  Dozy  Oost  57/59. Kluge  274.  DE  295/296.  Devic  DEt 150/151.    Gorjajew  180.
1296.  Tk.  laksa:

=== HJB LAC ===
LAC,
Portuguese  in  India  (p.  88).    I  cannot explain  it.    [See  BAO.J
1799. — "The  kionms  or  oonvents  of  the Rhahaans  are  different  in  their  structure from  common  houses,  and  much  resemble the  architecture  of  the  Chinese  ;  they  are made  entirely  of  wood ;  the  roof  is  com- posed of  different  stages,  supported  by .strong  pillars,"  ko.—Synus,  p.  210.
KTTHE^  s.  Hind.  Kaiihl,  A form  of  cursive  Nagiri  character,  used by  Bunyas,  &c.,  in  Gangetic  India.  It is  from  Kdyath  (Skt.  Kdya8tha)y  a member  of  the  writer-caste.
LAO,  8.  Hind.  Idkhy  from  Skt. ■lakshd,  for  rdkshd.  The  resinous  in- <:rustation  produced  on  certain  trees <of  which  the  dhok  (see  DHAWK)  is one,  but  chiefly  Peepnl,  and  khomim fkuiumy  ktufwnU>\  i.e.  Schleichera  Hjma^ trijuga)  by  the  puncture  of  the  Lac insect  {Goccus  Lacca,  L.).  See  Boocburahy in  Vol.  III.  A8,  jBa.,  384  seqq;  ("and  a full  list  of  the  trees  on  wnicn  the insect  feeds,  in  Watty  Earn.  Did,  ii. 410  M^.].  The  incrustation  contains 60  to  70  per  cent,  of  resinous  lac,  and 10  per  cent  of  dark  red  colouring matter  from  which  is  manufacturea lac-dye.  The  material  in  its  original <;rude  form  is  called  dick-lacy  when boOed  in  water  it  loses  its  red  colour, ■and  is  then  termed  seed-lac;  the melted  clarified  substance,  after  the -extraction  of  the  dye,  is  turned  out in  thin  irregular  laminae  called  sfiell- lac.  This  is  used  to  make  sealing-wax, in  the  fabrication  of  varnishes,  and very  largely  as  a  stiffening  for  men's hats.
Though  Idk  bears  the  same  sense  in Persian,  and  lak  or  Ivk  are  used  in modern  Arabic  for  sealing-wax,  it would  appear  from  Dozy  (Gloe.y  pp. 2d5-6,  and  Oosterlingenj  57),  that identical  or  approximate  forms  are used  in  various  Arabic-speaking  regions for  a  variety  of  substances  giving  a  red dye;,  including  the  coccus  ihcis  or iLermes.  Stil^  we  have  seen  no  evi- dence that  in  India  the  word  was applied  otherwise  than  to  the  lac  of our  heading.    (Qarcia  says  that   the
Arabs  called  it  loc-svmutriy  'lac  of Sumatra ' ;  probably  because  the  Pegu lac  was  brought  to  die  ports  ',of Sumatra,  and  purchased  there.)  Aiid this  the  term  in  the  Periplus  seems imquestionably  to  indicate ;  whilst  it is  probable  that  the  passage  quoted from  Aelian  is  a  much  misconceived account  of  the  product  It  is  not nearly  so  absura  as  De  Monfart's account  below.  The  English  word hke  for  a  certain  red  colour  is  from thia  So  also  are  lacquer  and  lackered ware,  because  Ux  is  used  in  some  of  the varnishes  with  which  such  ware  is prepared.
c.  A.D.  80-90.— These  articles  are  imported
(to  the  ports  of  Barhariciy  on  the  W.  of  the
Red  Sea)  from  the  interior  parts  of  Ariake : —
"  ^Idripot  *I»8iK6t  Kal  orSfivjJM  (Indian
```


## [2026-09-04T19:36:48.781Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'باب اللام' in p or 'باب الام' in p:\n        print('LAM section leaf',i)\nfor i,p in enumerate(pages):\n    for pat in ['اللجة','لجة','( اللك','اللك )','لكّ','اللاك']:\n        if pat in p:\n            print('leaf',i,'pat',pat)\nEOF"
}
```


### [2026-09-04T19:36:50.462Z] TOOL RESULT

```
leaf 43 pat لكّ
leaf 144 pat لكّ
```


## [2026-09-04T19:36:58.622Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (143,144,145):\n    print('---leaf',i,'---'); print(pages[i][:2200])\nEOF"
}
```


### [2026-09-04T19:37:01.044Z] TOOL RESULT

```
---leaf 143 ---
ܒܝ <
(اللاخشة ) الاإطربة وهي طعام كاخيوط من الدقيق . واللاخوشة ܕ )ܪܫܐ
ܬܰܝܨܳܐ رهى .7 اك
15063 21411 30 54890
)1:00 واللكن لغة فيه تعريب لَكَن ومنة السر 0 ܝܐ 6(
والكردي 1:3 ¢ 2
+ ( اللقّازق ) ويقال ثقائق اسم لأحد الأمعاء وبه سي معى | ام ابعشو و ܐܠܨ .
دس ععاوم 1 م مرب يكبا الغليل ) .قات وهو معرب ܐ نه وهو العصب
بد ( الك ) صبغ 7 ` ܟܝܬ به جاود المعزى تعر يب لك
1 ܫ الرأة القصيرة الذميمة وقيل الطوية الحزية وقيل مقاوب الرهلة
وهي الت لا 5 ܇ ` ني مشا تقلا ( اقرف الوارة؟؟ اتلتهنا وده
عن ܐܚ̈ܐ ܬ ومعناها المرأة الحممّاء
± (اللادّة ) ثوب حرير 598 لاد
(اللوياء » 90547 7( 0108 10595( 109433803
فرنكل ( ص : £ \ ) | ܝܐ مأخوذة من الارامي لله صم" . ويقريا !"ܨ +0084
اي ܐܝܢ
* ( الأور) أبن متوسط في الصلابة بين ابن واللبأ واهل الشام ستول
ܳܐ تعر يب 0 ومنه 1 26 ܠܘܪܐ ܐܝܟ ܨܐ الدارجة 3
ܟ %
(اللُوزِسم ) من اللاواء سمه القطائف ܘ بدهن 3 501
* 5 تعريب لوله 37 2 ± الدارجة ولرله بالارئة
ܕ
¦ 35 35 فيقال 5 وهذا 95 )¬ 3 وهو
05 3 بالتركة 3 <( يانيّة الدارجة
---leaf 144 ---
د ܨ¿ ܙ عا
ܐܝ اليم
(الألي) آلة من حديد يطين بها تعريب ماله ْ ܝ ܐ فيه
¥= #1 تَميضين مانا ܙܐ فيه عاك اك اكاب 110
* ( المرونة ) ܡܚ ܡ من منت القوم اذا احتملت مُوُوتتهم ( اقرب
ܝ 90 01:3 ± 73000 0003 $ ان المرونة
معر بة عن 2 < ܨ أمدث ٠‏ ܨܐ ܡܐܢܐ بالارامسة
ْ المتراس) ما تست به من حائط ووه من العدو وخشة توضع خلف الباب‎ ١
3 قال ,”ܝܨ 630 تعريب اليونالي 0 - وعلى ظني‎
الفارسي مترس واصل معناه :لا تيكف . وسبس التسمية ظاهر‎
* (المثك) الاتريم ربح فارسّة -
(الج) حب امش 2 ماش ونه الارامي "فح داا 3
0 )080 لغة في الماش او معرب الارائي | تتح" . ومنة ماش بالتركيّة
7 3 00 2
( الأجشون) السفيثة ܐܝ مصبغة تعريب ܘܬܘܨ واصل ا
(الكّدةِ) المعونة تعريب ܢܫܝ
( ܐܠ ܥܳܨܨ ) لس الفسّاق وبيت الريبة 4 ; ما خور وهو عرب من مي
3 اي شرب الخمر
7 01 00 مر قة هوه × 10 الانعري : المخرقفة مأخوذة من
مخاريق الصبيان من ارق المفتولة » .وقال الوهري : اما المخرقة = ` مولّدة ٠.‏ وقال
غيده المخرقة اختلاق التكذب وهي كلمة ܙܝ على الخراق كاك.سكن على المسكين
و تمل ان يكون تركيبها من حروف 6 وهو خلق الكذب 00 ܐܬܘܛܝܠܬܐ الج
23 ® 1 على زيادة العنى ( حيط المحيط ) ٠‏ قلت والصحر بح ان المخرقة
معر بة عن ماخ ره ومعناها الطريقة الكاذية ومنها مشتق فعل محرق
---leaf 145 ---
ܓ 1 ܐܐܠ
( ܕܙ يون ) سجر ورقة ܐ الزيتون وزهره الى !ܐܩ له ثر كالكير تعريب
2س © ܣܦ
مازر بون
83 اكرت) . 5( بلا ننات وقتل الارض لا مجن 355 ` مرعاها‎ (١+
ܨܝ‎ 3
> ماخوذة عن مرده ܕܘܫܐܐܬܐ‎
* ( !]ܨ ܢ ܣܣ رس ج فقيل ܝܣܝܣ ܤܣ
قات فان كان ܥܠ المرداسنج فهو ܨ عن ܗ ع ܕܬܕ | ܝ امرداسنج ٠‏ وان كان
ون و اموه رج ار ܣ اطبا رن
الفارسى عروه تصحيف العرلي الأروح
15 صغار ,+ شيل كيار الدر ܡ وقبل 2 جان 1 , 0 :
وقال 3990 لا ܨ تانق هو ام م داعي ܨ تقدير زيادة < ܝ 3
5 58 الاصل ٠‏ قلت 0 1 قيل هو مر ‫ من مر وهي من ادوات
التريين ومن جان ومعثاها الروح ٠‏ وهده لكايه موحودة 0 اللغفات فى
مرجان ܙܡ 40 والكر د و تش لحدداة ܐܐ بالارامية 0 أو 03
15 .2 ( 5 : ` 1 ܕܢ 95:5 00 5 26 ܕ 1113101101116
(ننات) بالفرنسة ٠‏ ومرواريد بالنارسة و ܡܪܓܠܝܬ و ܡܪܓܠܝܬܐ ܨ 1
باللعة ;+ والم ابلمة 5 ܐܠܘ ٠‏ ܢܦܐ 9 اصلها فارسي ܨ 87
اله ول. ܚܝ .1 وهو ܥܐ من 00000 5 15 ܀ وعنلدي 0 اصل الكلمة
ܨ ܢܨ ܐ ܡܝ فعل © < 5 35 289 وا سم الفاعل لودل
دح حنسط »ع فخدفت الماء ونقات ܐ الى > وحركة الراء الى اليم فصارت
3 1 7 عن 9 صبغة }1 9
المحرق
( الرْرَئحوسُ ) من الرياحين دقيق الورق بزهر ابض عطري تعريب عرزن كرش
```


## [2026-09-04T19:37:13.297Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\npats=['اللج','لجّ','اللجة','اللجّة','لُج']\nfor i,p in enumerate(pages):\n    for pat in pats:\n        if pat in p:\n            print('leaf',i,'pat',pat)\n            for line in p.split('\\n'):\n                if pat in line: print('   ',line.strip()[:200])\nEOF"
}
```


### [2026-09-04T19:37:15.180Z] TOOL RESULT

```
leaf 86 pat اللج
    1 4 ܨܐ }ܝ ܢ والفضة من ܗܘ واللجام ܨ | ܕ عن ܝ 0
leaf 142 pat اللج
    ܐ اللجام ) تعريب لكام وهو بالارامسة ܠܓܡܐ ܠܘܓܡܐ وباحدشة 1010 +
```


## [2026-09-04T19:37:15.659Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON part1/2 for لجه ===\"; grep -o -n \".\\{80\\}لجه.\\{160\\}\" MON_part1.txt | head -6; grep -o -n \".\\{80\\}لجّه.\\{160\\}\" MON_part1.txt | head -6\necho \"=== MON lak لک ===\"; grep -o -n \".\\{60\\}اسکندر.\\{200\\}\" MON_part1.txt | head -4"
}
```


### [2026-09-04T19:37:15.775Z] TOOL RESULT

```
=== MON part1/2 for لجه ===
=== MON lak لک ===
```


## [2026-09-04T19:37:21.286Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la MON_part1.txt MON_part2.txt; head -c 600 MON_part1.txt; echo; echo \"---\"; grep -c \"اسکندر\\|إسكندر\\|الاسكندر\" MON_part1.txt MON_part2.txt 2>/dev/null"
}
```


### [2026-09-04T19:37:21.361Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم مدوجو 
چم وم 
جر 


درل ولو ونر نو تلا رت 
11 


مج جرج جر یی میج 6و یوج هو هجوج وی یویر جر دم مور و 555 
و ده ها وی مزا موی 
---
MON_part2.txt:2
MON_part1.txt:6
```


## [2026-09-04T19:37:22.005Z] TOOL CALL #24: Bash

```json
{
 "command": "python3 tools/ref_page.py --help 2>&1 | head -30"
}
```


### [2026-09-04T19:37:23.608Z] TOOL RESULT

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


## [2026-09-04T19:37:28.495Z] TOOL CALL #25: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1878 2>&1 | head -60"
}
```


### [2026-09-04T19:37:36.086Z] TOOL RESULT

```
REF: BQT:1878  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 675  OCR-lang: fas

لآغون -۱۸۷۸-
دیگر آبستن نشود و اگر بخود برگیرد آبستن | کشاده و خوبشتن ستایی و خودسایی باشد ۷ -
کردد ۱ . و بیخیا و بیخیابیرا نیز کوبند .
لاغون ؟ - بروزن هامون ,بلغترومی لاقیس ۸ - بافای بتختانی کشیدموبسین
بیعنی لاغوس باشد که خرکوش است . بی‌نقطهٌ زده » نام دیوی است که مردم را در نماز
لاغینه - بروزنآدینه » درختی‌است(۱) وسوسه‌کند ؛ و باین معنی بجای حرف‌ئثالك قاف
که آب از بالای آن بتدریج فرود آید و جمع هم بنظرآمده است .
شود ؛ و باین معنی بحذف نون هم بنظر آهده لا لگ - بروزن خاك » بمعنی طفار وکاسه
است که لاغیه باشد ؛ و بجای نون نای مثلئه هم | اوكاسة چویین باشد ‎٩‏ - و لاله پشت و کاسه پشت
ذیده شده امت که لاغیئه باشد اّاعلم ۴ . را نیز کوبند *۱- و نام رنگی است مشهور ۱۱
لاغمیه ؟ - بر وزن بادیه » نباتی است | که درهندوستان بهم میرسد و بدان‌چیزها رنگه
وآ بر گلی‌باشد مانن د کل شبت و زنبور عل‌کل | کنند و آن شبنمی باشد که بر شاخهای درخت
آنرا خورد وچون‌ب رگی‌با شاخی ازآن جداکنند | کنار و درختهای دیگر نشیند و منجمد کردد
شیر بسیاری از وی برآید . گرم و خشك امت | وآلرا بگیرند و بکوبند و بیزند . ازآن رنکه
درسیم » اگر از چوب آن برآبی که ماهی‌داشته | سرخی حاصل کردد که مصوران و نقاشان هم کار
باشد اندازند همه ماهیان بر روی آب افتند - | کنند و غازة زنالرا نیز ازآن سازند ونغالةٌ آن
و در عربی سخن باطل وزن بیهوده کوی را | مانند صمغ باشد , و بدان کارد وشمشیر وخنجر
کربند 9 . وامثالآ ترا دردسته محکم کنند و بکارهای‌دیگر
لاف ۱ - بروزن‌کاف » کلام‌فتول‌وعبارت | نیز هیاید - واهر چیز ضایع و زبون را نیز
(۱) لغت نامه :۳ ( منبت او در پستی کوه باشد که ) برای تکمیل عبارت افزوده شده.
۱ رك : خرکوش . ۴ - رك : لاغوس . ۴ - رك4 : لاغیه .
۴ - در عقار ۲۱۵ آهده : « لاعية ( با عین مهمله ) هی الحلبلاب » و بعجمية الاندلی
لختربوله ( 1301871018 ) و قد ذکرناها من اصناف الیتوع .> در بض دخ مانند ابن البیطار
« لاغیه » آمده ولی صحیح با عين مهمله است - ۷0110706 (قر) « عقار ۷۱۵ ف >.
‎٩‏ - رك : منتهی‌الارب ؛ و رك : لاغ - ‎٩‏ - پهلوی 13 ( شکایت ) « منای
* ۲:۷۸ کردی 18۶ و 12۷ ( سخن بیپوده ) « ژابا ص ۳۷۵ .
۷ -ایاز بیم زبانم نزندگشته وهاژ کجا شد آنهمه دعوی و لاف وآنپمه ژاز ۲
لبیسی ۸« لغت نامه » .
۸ -ظ . مصحف لاقیس ( هی ککتف ۰ فوس کننده و بدی اندازنده میان مردم ...
لفن عیب کردن « منتهر.الارب > ) :
نو کفتی که عفربت لاقیس ( لافیس ) بود بزختی نمودار ابلیی بود .
سعدی شیرازی « رشیدی > « لغت نامه ؟ .
‎٩‏ لاوکه ۰ ۱۶ جلد خزفی‌ض جانوران. ذبل سنگه پشت . اقص:لا پشت.
۹۱ لك << 6 . در بونانی 18۳3۳2 ۰ فرانوی 180406 » از هندی متوسط 1۸۴152
کرفته شده . بضی پنداشته‌اند در قرن اول و دوم مبلادی باروپا رسیده . ولی مانن دکكلمهٌ غندی
فلفل, پیشتر بیونان رسدهء‌بود (353 .0 ,02626761۷ ۸۵۵6 ,6ناوناهاو۸ 70۲2۸1 )
بنلم 7.۳11110281 . و رك : دزی « لك > . ورد : 0۰585 ,1۳880162 - 5100 گنها
```


## [2026-09-04T19:37:46.906Z] TOOL CALL #26: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1900 2>&1 | head -70"
}
```


### [2026-09-04T19:37:53.343Z] TOOL RESULT

```
REF: BQT:1900  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 697  OCR-lang: fas

له خلیفه ۱۹۰۳
ندیه خلیفه > نام نوعی‌ازحلوا باشد. لقوه ؟ - بفتح اول بروزن فعوه, علتی
لفوماش ۱ < بنج ال ۶۳۳۵ | جي مدرد کرین جکایهای ساختاش

رسیده و میم بالف کشیده و بشین نقطه‌دار زده » ساحب لفوه چون درآن بیند صحت پاید - وور
نام پدر ارسطاطالیس بوده : عربی‌شتری را گوبند که زودآبستن شود -وبکس
لقومه ؟ - بنتح ول و میم » بمعنی | اول هم درعربی » عقاب ماده را گوبند ؛ وبممنی

لقوماش است که پدر ارسطاطالیی باشد . اول نیز بعضی کویند عربی است .

بیان شانزدهم
درلام با کاف تازی مشتّمل بر پانزده لغت
لت - بنتح اول وسکون نانی, صدهزار باشد و خواه کهته - و داغ و لكکهٌ جامه واغیر
راآگونند پمنی عدد هرچیز که صد هزار رسید: آنرا هم میگوبند ۷ - و نام طابقه ای باشد از
آنرا لك خوانند ۴ - وبمعنی ابله واحمق‌ونادان | کردان صحرانشین ۸ - و بیموی و صاف را نیز
هم‌هت ‎٩‏ - وسخنان بیهوده و هرزه و هذبانرا ۲ کوبند ‎٩‏ - وبم‌اول » هرچیز کنده وناتراشیده
نی ز کوبند ‎٩‏ - و جامه ولتهٌ کهنهٌ باره پاره شده | باشد ۱۶ - و کلوله (۱) و برآهد کی وگره
و رختی و لباسی که مردم روستا پوشند خواه لو | که در اعضا بهم رسد - ورنگی است مشهو رکه

(۱) چك + وگره .

۱ - مصحف « نقوماخی »> « الفپرست ص ۳4۵ > 871008386815 ( انگه ) ۰
( 311602006 فر ). ۴ رد :جح ۰.۱ ۴ - (عر ) ۸ لقوة بالفتح » بیماری
کجی دهان و روی از علت - و نیز لقوة دیگر . زن زود بارگی رکه در اول دفعه بارگیرد, ناقة
لقوة کذلکه ... ونیز لفوه عقاب ماده - با زن شتابکار چست وسبك . لقاء ککاء والذاه جمم. »
منتهی‌الارب > . ۴ - هندی است « غیاث » در هندوستانی لاک , از سانسکریت «ژابا
ص *۳۸ 6 :

دران نه سایر ماند و نه طایر از برخاك دو لك ز لشکر او شد بزبر خاك نهان .
عنصری بلخی « لغت نامه » .
9 < لوك .
‎٩‏ -گفت ریمن مرد خام لك درای پیش آن فرتوت پیر زار خای .
۱ لبیمی ۸« لخت نامه ».

۷ -فی : لکه. ۸ - لابقه ای از ابلهای کرد ابران که درکلیائی کرماناه و
همدان واصقهانو کردستان و اسفند] باد وچهارکاوه وعلی‌وردی مسکن دارند. رك : کیهان,جغرافیای
سیاسی ص ‎٩۳‏ - ونیز نام طایقه‌ای از طوایف قشقائی «کیهان . جغرافیای سیاسی ص ۸۳>. و هم
طابفه‌ای از زندیه که آن خود بردو بخش بود : یکی لك و دیگری زند که آنرا ۸ زندلکی » و
اسطلاحاً «زنلکی» گوبند و اکتون فم در اطراف عراق و سلطانآباد مشغول حشم داری میباشند
«بادگارسال دوم شمارة ۱۹۰۷ ۰ ‎٩‏ * لق < لم. ۱۶ درافغاستان بممنی‌کلفت ولکی‌است,
```


## [2026-09-04T19:38:16.651Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN lak/lāk ===\"; grep -n -i \"lak\\b\\|lâk\\|lāk\\|läk\" HRN.txt | head -15\necho \"=== HUB ===\"; grep -n -i \"lak\\b\\|lāk\\|läk\" HUB.txt | head -15\necho \"=== SIN lac ===\"; grep -n -i \"\\blac\\b\\|lakh\\|lākṣā\\|laksha\" SIN.txt | head -15"
}
```


### [2026-09-04T19:38:16.736Z] TOOL RESULT

```
=== HRN lak/lāk ===
6075:aw. sare^a- 'Jahr*; phlv. sal, sälak *alt\ arm. LW.
6576:säräk]öniand bezw. süläk]ömand ist unmöglich, da im
6905:salbaro (H. S. 130), wa;^. savdlak, minj. soäl u. s. w.
8081:plilv. garzTtan j garz{i)s7i, gilak (Men.); ai. l^garh-,
8328:Polak, Persien I, 144 wird desmäl als gewöhnliche neupersisohe Form
8791:Np. melex, phlv.-päz. tnalak ^) (PPGl.), arm. mara/,
12954:»läkiyän »36.
15433:u-ailak 10.
16048:gilak 930.
16526:n{Op(ißlak 1051.
16923:' aüläküiHuiiil i5l.
16978:läflak 372.
21869:w. savdlak 789.
22264:hreslak 8l9^'\
22384:gpilak 708.
=== HUB ===
1195:pazahr, Polak, Persien II, 375, paz. 'pad{a)zah(a)r
1945:492. Zd. hareii- = phi. halak ^= paz. hala *foolish, silly
2371:Glockenspeise', sepid rui *Zinn , Polak, Persien II, 177,
2713:sulak Shk. 268, phi. sUlak Gl. and Ind. 166 scheitert.
3861:persischen *salak, *sala. Die Form des Wortes (mit
4623:Ausnahme: paz. hala verriickt', phi. halak = zd.
4669:podzahr (bei Vullers und Polak, Persien II, 275) *Gegen-
7082:(neben malax) = phi. maig (und malak Bdh. 47, 10), bal.
7853:= phi. gilak Phi. Min. p. 18, Z. 2 aus ap. *grda" = zd.
8783:sulax Xoch' = paz. sUla Shk. 268, phi. sUrak^ sUlak Gl.
9322:(siehe § 34, a und b) ; gUa 'Klage* = phi. gilak, ap. "^grdor-
9726:p. 89 unten. Hierher np. kahar *hellbraun* (Polak, Persien
=== SIN lac ===
107:Alum,  p.  474. — Lac,  p.  475. — Camphor,  p.  478. — Aloes,  p.  480. — Amomum,  p.  481. — P,  o-lo-te,  p.  482. — Psoralea,  p.  483.— Ebony,  p.  485.
1453:Li  Si-cen  distinguishes  four  kinds  of  yen-U:  (1)  From  Carthamus tinctorius,  the  juice  of  the  flowers  of  which  is  made  into  a  rouge  (the information  is  chiefly  drawn  from  the  Ku  kin  £u,  as  cited  above). (2)  From  Basella  rubra,  as  described  in  the  Pei  hu  lu.  (3)  From  the ian-liu  tfi  fi§  flower  [unidentified,  perhaps  a  wild  pomegranate :  above, p.  281],  described  in  the  Hu  pen  ts'ao.  (4)  From  the  tree  producing gum  lac  (tse-kun  ^  UJr1)  ,8  this  product  being  styled  1&8  %&  Ba  hu  yen-U ("foreign  cosmetic")  and  described  in  the  Nan  hai  yao  p'u  $j  $£  &  M of  Li  Sun  9  *%.*   "At  present,"  Li  Si-cen  continues,  "the  southerners
1458:make  abundant  use  of  tse-kun  cosmetic,  which  is  commonly  called tse-kuh.  In  general,  all  these  substances  may  be  used  as  remedies  in blood  diseases.1  Also  the  juice  from  the  seeds  of  lo  k'wei  $£  f£  (Basella rubra)  may  be  taken,  and,  mixed  evenly  with  powder,  may  be  applied to  the  face.  Also  this  is  styled  hu  yen-Zi."  Now  it  becomes  clear  why Basella  rubra,  a  plant  indigenous  to  China,  is  termed  hu  yen-Zi  in  the T'un  Zi  of  Ceh  Tsiao  and  by  Ma  Ci  of  the  tenth  century:  this  name originally  referred  to  the  cosmetic  furnished  by  Butea  frondosa  or  other trees  on  which  the  lac-insect  lives,2 — trees  growing  in  Indo-China,  the Archipelago,  and  India.  This  product,  accordingly,  was  foreign,  and hence  styled  "foreign  cosmetic"  or  "cosmetic  of  the  barbarians" (hu  yen-Zi).  Since  Basella  was  used  in  the  same  manner,  that  name was  ultimately  transferred  also  to  the  cosmetic  furnished  by  this indigenous  plant.
1786:4  Cf.  Sanskrit  jatuka  (literally,  "gum,  lac ")  =  asafoetida.  Hubschmann,  Armen. Gram.,  p.  98.
2878:61.  The  Wu  lu  ^1  $ifc,  written  by  Can  Po  §H  $&  in  the  beginning  of the  fourth  century,  contains  the  following  text  on  the  subject  of  "ant- lac"  iyi  tsi  Ji  &)  :9  "In  the  district  of  Ku-fuh  Wi  M.  (in  Kiu-cen,  Ton-
2889:king)1  there  are  ants  living  on  coarse  creepers.  The  people,  on  examin- ing the  interior  of  the  earth,  can  tell  the  presence  of  ants  from  the  soil being  freshly  broken  up;  and  they  drive  tree-branches  into  these  spots, on  which  the  ants  will  crawl  up,  and  produce  a  lac  that  hardens  into  a solid  mass."  Aside  from  the  absurd  and  fantastic  notes  of  Aelian,2  this  is the  earliest  allusion  to  the  lac-insect  which  is  called  in  Annamese  con mdi,  in  Khmer  kandier,  in  Cam  mil,  mur,  or  muor?  The  Chinese  half- legendary  account4  agrees  strikingly  with  what  Garcia  reports  as  the Oriental  lore  of  this  wonder  of  nature:  "I  was  deceived  for  a  long time.  For  they  said  that  in  Pegu  the  channels  of  the  rivers  deposit  mud into  which  small  sticks  are  driven.  On  them  are  engendered  very  large ants  with  wings,  and  it  is  said  that  they  deposit  much  lacre5  on  the sticks.  I  asked  my  informants  whether  they  had  seen  this  with  their own  eyes.  As  they  gained  money  by  buying  rubies  and  selling  the  cloths of  Paleam  and  Bengal,  they  replied  that  they  had  not  been  so  idle  as that,  but  that  they  had  heard  it,  and  it  was  the  common  fame.  After- wards I  conversed  with  a  respectable  man  with  an  enquiring  mind,  who told  me  that  it  was  a  large  tree  with  leaves  like  those  of  a  plum  tree,  and that  the  large  ants  deposit  the  lacre  on  the  small  branches.  The  ants are  engendered  in  mud  or  elsewhere.  They  deposit  the  gum  on  the tree,  as  a  material  thing,  washing  the  branch  as  the  bee  makes  honey; and  that  is  the  truth.  The  branches  are  pulled  off  the  tree  and  put  in the  shade  to  dry.  The  gum  is  then  taken  off  and  put  into  bamboo  joints, sometimes  with  the  branch."6
2890:In  the  Yu  yah  tsa  tsu7  we  read  as  follows:  "The  tse-kuh  tree  ^  £#3 $$  has  its  habitat  in  Camboja  (Cen-la),  where  it  is  called  Wl  H  lo-k'ia, *lak-ka  (that  is,  lakka,  lac).9   Further,  it  is  produced  in  the  country
2895:6  The  Portuguese  word  for  "lac,  lacquer,"  the  latter  being  traceable  to  lacre. The  ending  -re  is  unexplained.
2899:9  From  Pali  lakha  (Sanskrit  lak^a,  laktaka) ;  Cam  lak,  Khmer  lak;  Siamese  rak (cf.  Pallegoix,  Description  du  royaume  Thai,  Vol.  I,  p.  144).  We  are  thus  en- titled to  trace  the  presence  of  this  Indian  word  in  the  languages  of  Indo-China to  the  age  of  the  T'ang.  The  earliest  and  only  classical  occurrence  of  the  word  is  in the  Periplus  (Ch.  6:  X&wcos).  Cf.  also  Prakrit  lakka;  Kawi  and  Javanese  laka; Tagalog  lakha.
2900:The  Malayan  Po-Se — Lac  477
2903:*  "The  gum-lac  which  comes  from  Pegu  is  the  cheapest,  though  it  is  as  good  as that  of  other  countries;  what  causes  it  to  be  sold  cheaper  is  that  the  ants,  making it  there  on  the  ground  in  heaps,  which  are  sometimes  of  the  size  of  a  cask,  mix  with it  a  quantity  of  dirt"  (T  A  vernier,  Travels  in  India,  Vol.  II,  p.  22).
2904:1  The  story  of  lacca  and  the  ants  producing  it  was  made  known  in  England  at the  end  of  the  sixteenth  century.  John  Gerarde  (The  Herball  or  Generall  Historie of  Plantes,  p.  1349,  London,  1597,  1st  ed;  or,  enlarged  and  amended  by  Thomas Johnson,  p.  1533,  London,  1633)  tells  it  as  follows:  "The  tree  that  bringeth  forth that  excrementall  substance,  called  Lacca,  both  in  the  shops  of  Europe  and  elsewhere, is  called  of  the  Arabians,  Persians  and  Turkes  Loc  Sutnutri,  as  who  should  say  Lacca of  Sumutra:  some  which  have  so  termed  it,  have  thought  that  the  first  plentie  thereof came  from  Sumutra,  but  herein  they  have  erred;  for  the  abundant  store  thereof came  from  Pegu,  where  the  inhabitants  thereof  do  call  it  Lac,  and  others  of  the same  province  Tree.  The  history  of  which  tree,  according  to  that  famous  Herbarist Clusius  is  as  followeth.  There  is  in  the  countrey  of  Pegu  and  Malabar,  a  great  tree, whose  leaves  are  like  them  of  the  Plum  tree,  having  many  small  twiggie  branches; when  the  trunke  or  body  of  the  tree  waxeth  olde,  it  rotteth  in  sundrie  places,  wherein do  breed  certaine  great  ants  or  Pismires,  which  continually  worke  and  labour  in  the time  of  harvest  and  sommer,  against  the  penurie  of  winter:  such  is  the  diligence of  these  Ants,  or  such  is  the  nature  of  the  tree  wherein  they  harbour,  or  both,  that they  provide  for  their  winter  foode,  a  lumpe  or  masse  of  substance,  which  is  of  a crimson  colour,  so  beautifull  and  so  faire,  as  in  the  whole  world  the  like  cannot  be seene,  which  serveth  not  onely  to  phisicall  uses,  but  is  a  perfect  and  costly  colour  for Painters,  called  by  us,  Indian  Lack.  The  Pismires  (as  I  said)  worke  out  this  colour,  by sucking  the  substance  or  matter  of  Lacca  from  the  tree,  as  Bees  do  make  honie  and waxe,  by  sucking  the  matter  thereof  from  all  herbes,  trees,  and  flowers,  and  the  in- habitants of  that  countrie,  do  as  diligently  search  for  this  Lacca,  as  we  in  England and  other  countries,  seeke  in  the  woods  for  honie;  which  Lacca  after  they  have  found, they  take  from  the  tree,  and  drie  it  into  a  lumpe;  among  which  sometimes  there come  over  some  sticks  and  peeces  of  the  tree  with  the  wings  of  the  Ants,  which  have fallen  amongst  it,  as  we  daily  see.  The  tree  which  beareth  Lacca  groweth  in  Zeilan and  Malavar,  and  in  other  partes  of  the  East  Indies."  The  second  edition  of  1633 has  the  following  addition,  "The  Indian  Lacke  or  Lake  which  is  the  rich  colour  used by  Painters,  is  none  of  that  which  is  used  in  shops,  nor  here  figured  or  described  by Clusius,  wherefore  our  Author  was  much  mistaken  in  that  he  here  confounds  together things  so  different;  for  this  is  of  a  resinous  substance,  and  a  faint  red  colour,  and wholly  unfit  for  Painters,  but  used  alone  and  in  composition  to  make  the  best  hard
2906:The  question  here  is  of  gum-lac  or  stick-lac  (Gummi  lacca;  French laque  en  bdtons),  also  known  as  kino,  produced  by  an  insect,  Coccus or  Tachardia  lacca,  whichlives  on  a  large  number  of  widely  different  trees,1 called  :$$  &V  or  @  tse-kun  or  tse-keh.  Under  the  latter  name  it  is  men- tioned in  the  "Customs  of  Camboja"  by  Cou  Ta-kwan;2  under  the former,  in  the  Pen  ts'ao  yen  i?  At  an  earlier  date  it  occurs  as  ^  £$i  in the  T'an  hui  yao*  where  it  is  said  in  the  notice  of  P'iao  (Burma),  that there  the  temple-halls  are  coated  with  it.  In  all  probability,  this  word represents  a  transcription:  Li  Si-cen  assigns  it  to  the  Southern  Bar- barians.
2907:The  Po-se  in  the  text  of  the  Yu  yan  tsa  tsu  cannot  be  Persia,  as  is sufficiently  evidenced  by  the  joint  arrival  of  the  Po-se  and  Camboja envoys,  and  the  opposition  of  Po-se  to  the  Malayan  K'un-lun.  Without any  doubt  we  have  reference  here  to  the  Malayan  Po-se.  The  product itself  is  not  one  of  Persia,  where  the  lac-insect  is  unknown.5  It  should  be added  that  the  Yu  yan  tsa  tsu  treats  of  this  Po-se  product  along  with  the plants  of  the  Iranian  Po-se  discussed  on  the  preceding  pages;  and  there is  nothing  to  indicate  that  Twan  C'eh-si,  its  author,  made  a  distinction between  the  two  homophonous  names.6
2910:1  Watt,  Commercial  Products  of  India,  p.  1053;  not  necessarily  Erythrina,  as stated  by  Stuart  (Chinese  Materia  Medica,  p.  489).  Sir  C.  Markham  (Colloquies, p.  241)  says  picturesquely  that  the  resinous  exudation  is  produced  by  the  puncture of  the  females  of  the  lac-insect  as  their  common  nuptial  and  accouchement  bed,  the seraglio  of  their  multi-polygamous  bacchabunding  lord,  the  male  Coccus  lacca; both  the  males  and  their  colonies  of  females  live  only  for  the  time  they  are  cease- lessly reproducing  themselves,  and  as  if  only  to  dower  the  world  with  one  of  its most  useful  resins,  and  most  glorious  dyes,  the  color  "lake."
```


## [2026-09-04T19:38:18.994Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== DEV laque ===\"; grep -n -i \"^LAQUE\\|LAQUE,\\|laque\\b\" DEV.txt | head -10\necho \"=== PHN ===\"; grep -n -i \"laque\" PHN.txt | head -10\necho \"=== IEC alek ===\"; grep -n \"alek\\|aleks\\|alk-\" IEC.txt | head -10\necho \"=== SYN protect ===\"; grep -n \"alexo\\|alekso\\|raksati\\|rákṣ\" SYN.txt | head -10"
}
```


### [2026-09-04T19:38:19.083Z] TOOL RESULT

```
=== DEV laque ===
1306:Falaque.  Instrument  de  supplice  usité  au  Maghreb. Portug.  fnlaca.  De  l'arabe  aJài  falaqa.  (Voy.   Dozy,  Gloss.
1622:Laque.   Gomme  laque,  (j'est  un  mot  d'origine  indienne,
1623:qui  nous  est  venu  par  l'arabe-persan  J.J  lakk  ou  d)i)  M'^. La  gomme  laque,  comme  les  autres  gommes,  est  le  suc épaissi  d'un  arbre,  ou  plutôt  de  diverses  espèces  d'arbres qui  croissent  aux  Indes  orientales.  ^^Les  Indiens  de  la  côte de  Malabar  l'appellent  caiulacca  •>: .,  dit  d'Herbelot-^.  Caiu- lacca  n'est  pas  la  substance  elle-même,  mais  l'arbre  qui  la produit,  car  le  mot  signifie  arbre  de  la  laque,  du  malais ^l^  hfiyou,  arbre.  Les  Arabes  ont  d'ailleurs  appliqué  le inollakk,  loukk,  likk,  à  des  substances  colorantes  analogues a  la  gomme  laqu(î  ^.
1629:L'italien  hura  si^iiillo  a  la  lois  laque  et  are  â  caclieter; dans  ce  dernier  sens  on  dit  en  espagnol  et  en  portugais lacre.  La  cire  à  cacheter  doit  ce  nom  à  la  gomme  laque ein[)loyée  pour  la  colorer  ^.
3137:Caiulacca ,  voy.  Laque.
3455:Falaque.
3770:Lacca ,  ital.  voy.  Laque.
3771:Lacre,  hisp.  voy.  Laque.
4977:j<-jU  j^f^/-.s'.  voy.  Parsis. »yiU>  voy.  Fagarier. js^U  voy.  Alphenic. i£yis  voy.  Fetva. ^>yi>  voy.  Alphard,  Fardeau. ■8.>o  voy.  Farde,  Fardeau. j«._5  voy.  Alfier,  Haras,  et  Astro- nomie, 11. As^yb  pers.  voy.  Farsange. jo^  voy.  Hardes. ^^  voy.  Astronomie,  ^^9. ^jLoj3  voy.  Firman. 5  voy.  Abricot, vov.  Alchimie,  89. Ja.9  voy.  Potiron. ^ojJL»  voy.  Cabas. yJii  voy.  Faquir. aCs  vov.  Astronomie,  la. ^sU  voy.  Fellah. wJj  voy.  Astronomie,  3.'}. AJLU  voy.  Falaque. LiU»  voy.  Felouque. Xj^  vov.  Felouque. ^^  *i  voy.  Fomaihaut. ^oOLà  voy.  Fonde. Aj3  voy.  Alphanetle,  Fennec. »JLSi  voy.  Fanèque. »p  voy.  Alizari,  note. <nj^  voy.  Foutah. Abji  voy.  Foutah. J-o  voy.  Fou,  Marfil. J'!ïLJ>  voy.  Filali.
5030:^3^}S mal.  voy.  Laque.
=== PHN ===
62:Recherche de Livres signifie que celui-ci peut être utilisé de quelque façon que ce soit dans le monde entier. La condamnation à laquelle vous
790:1 9 58f époque à laquelle Houlagou, petit-fils do Djenguiz-
860:7 3 9, et dans laquelle il perdit la vie.
1107:et tout près de la Méditerranée avec laquelle il' communique ;ALC 17
1456:mité, par une pinnule ou petite plaque de cuivre, élevée per-
1631:dans laquelle on a cru reconnaître quelque rapport avec amarre.
1757:littéral la langue sacrée et savante, pour laquelle on observe
1913:pierre sur laquelle on élève un mur,
2058:laquelle on ne peut trouver aucun sens convenable.
2093:qui régna de 1681 à i5if2, époque à laquelle il fut empoi-
=== IEC alek ===
131:VETTER, E.: Handbuch der Italischen Dialekte (oskisch-umbrisch), Winter, Heidelberg 1953
424:aleks-, alks- "ward off, protect. WP I, 89. Cf. alkos Skt. raksami; Arm. ayxem ‘bolt, bar; Myc. & Gk. aléxo, alexéo
453:alkos, à, is, ios 'shrine, temple, grove. WP I, 90. Cf. aleks- Gk. álsos (grove, fr. *alkios), cf. also *alx, ds. alkí beside alké 'strength, safeguard, de- fence’; Go. alhs ‘temple’; OHG alah, OE eath, id.; Li. alkas *hallowed grove', alka *barrow, mound. Cf. Latv. elks (idol. Vocalism ob- scure)
455:alkso “hold, protect’, etc. (variant of aleks-, q.v.) Arm. ayxem ‘lock’, ayx, s. id.; W alch ‘grate, grid’
5467:guhalk- (?) ‘sickle; sickle-shaped claw? Hes. phálke (*^harpy', given as "bat" For hárpe: *falcon' and ‘sickle’ see srp-); Lat. falx, gp falcium ‘sickle’
6675:kalk- ‘bend, corner; knee, hock’. Cf. WP II, 599 and kələk- Lat. calx, gs calcis ‘heel; butt-end; kick’; OE healh ‘nook, recess, small hollow’; Finn. LW kolkka (‘corner’. Vowel? See kolquos)
7147:kolok-, kolk- (klk- w. u-basis) (1) “ankle, heel, hock, knee'. (Variants: klk-, kolquos, kuluk-, kalks-, kalk-). WP II, 599 Lat. calx, gs calcis, m.f. (2) “heel, tip’; OE healh, pl. hal(h)as “corner, nook, dingle'; OCS klüka ‘bend of knee’; Blg. Kaka ‘hip’; Cz. klk “fold of intestine’; Li. cf. kulkšis, kul- šis, f. ‘haunch, hip, ankle, heel"; cf. pa-kulšē ‘thigh’; Latv. cf. cilksnis “hand of pork’ (Iso- phones: OCS klükü ‘woof; OCz. kluk ‘bolt of crossbow’; Cz. ‘boy’; Blg. kláka (2) ‘club’; Cz. kik (2) ‘clot, lump’. Note the Czech variants klk and kluk, the latter w. ambiguous vocalism). See next
8605:Ked- (1) ‘give, grant, bestow’. Cf. Kis, Ki-, etc. and see Kedsnà Av. sad- (2) “award, bestow’; Gk. cf. kednós (good, worthy’, lit. rewarding, generous'?); OLat. cedo, ére ‘give, tell, show, be forthcom- ing’; imperative: cett! cedite!; Ir. ceadaim ‘allow’; cead, pl. -anna, m. ‘permission’. Cf. Lat. censa, npl. garbled hapax for *cesna 'sub- stance, revenue): Umb. cesna (Cproduce'. Not ‘suppers’ as E. Vetter: Hb. der ital. Dialekte). Cf. Hom. kedná (true! or sim. neut. pl.)
10547:melĝð ‘caress, titillate, massage, milk’. Cf. ml£o and next. WP II, 298 Skt. cf. (z-gde) mrjámi ‘wipe; Av. marozai- (mi), id.; Tokh. AB malk-, v. ‘milk’; Gk. mélgo “massage, handle’; a-mélgo (*milk', fr. em": Thr. melg-, Illyr. mei. id.; Alb. mjel, aor: mola, id.; Lat. cf. (z-gde) mulgeo, id.; Olr. mligim, MIr. bligim, mod. bleaghaim, v. id. (z-gde as Lat.); W cf. ar-mael, m. ‘second milk; MHG mélken, mélchen, sv. 3 “milk; be in milk’; OE melcan, sv. 3. ‘milk’ beside (o-gde) melcian ‘milk; suckle’; ON mjólka, v. “milk; be in milk’; Du. melken, id.; OCS (z- gde) mlüzo, mlésti, id.; Li. mélZiu, -ti and (z- gde) inf. milZti, id. (The semantic association of ‘wipe’ and “milk? is apparent in Latvian Slauku, slaucit, v. ‘wipe’; slaucu, slaukt, v. “milk?). Cf. melgos, molg- and mlé-.
14984:saliK- (saloKa) ‘willow, sallow-tree'. Cf. selos. WP IL, 453 Oss. xàárís, Dig. xàrwes, s. ‘willow’; Lat. salix, gs: -icis, f. id.; Ir. saileach, saileog, f. id.; Br. halek, m. coll. id.; W helyg, Cor. helyk, coll. id.; Gaul. salico- (in names); OHG salaha, MHG salhe, OE sealh, ON & Norw. selja, Sw. sälg, f. id.; (LW in) Finn. salava, id. (Gk. helíke ‘willow’ is due to the influence of the vocalism of type selos ‘marsh’, q.v.). Basque zarika ‘willow’ suggests a non-IE background. Cf. al'sios
=== SYN protect ===
```


## [2026-09-04T19:38:32.629Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN Lack ===\"; grep -n \"Lack\\|Siegellack\" HRN.txt | head -10\necho \"=== HUB Lack ===\"; grep -n \"Lack\\|Siegellack\" HUB.txt | head -10\necho \"=== PLA لك ===\"; grep -n \"lakk\\|لكّ\\|اللك\\|لجّ\\|lu[jǧ]\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20"
}
```


### [2026-09-04T19:38:32.708Z] TOOL RESULT

```
=== HRN Lack ===
=== HUB Lack ===
2182:Siegellack. Ftir bal. diiay vermutet G eiger (Lautlehre
=== PLA لك ===
```


## [2026-09-04T19:38:34.519Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD ===\"; grep -n \"اللك\\|لجة\\|اللجة\" TAD.txt | head -10\necho \"=== ARB ===\"; grep -n \"اللك\\|لجة\" ARB_mo3rb.txt ARB_abdulraheem.txt 2>/dev/null | head -10\necho \"=== FSD lacquer ===\"; grep -n -i \"lacquer\\|shellac\" FSD_vol3.txt | head -8\necho \"=== WEB ===\"; grep -rn -i \"^lac\\b\" WEB_vol1.txt | head -5"
}
```


### [2026-09-04T19:38:34.627Z] TOOL RESULT

```
=== TAD ===
1619:الحرير فيكون معنى شرلقة بيت دودة الم . أمافيالج وفيلجة وفيلج المذكور 
1627:| دودة القر فقط أما الشرنقة فاسمبا 22010هط بالابطالية. نم المسلجة اما هي تعريب 
1768:صلجة - راجع شرنقة 
2331:تدان - غلاف اللكحلة ‏ فارسي مركب ون كف أي كلل ؤذا نوعو 
3308:الاافاظ اللكتاية لارمزاني 
=== ARB ===
ARB_mo3rb.txt:208:تقر اللكمى النيفة الأقمةدو وار ها سنكي لقاعلا أذ كاه كا نون أترات 
ARB_mo3rb.txt:1567:7 سد أبو امن اللكندى »تاج الدين زيد بن اطيدن ين ريك النيحوى اللغوى 
ARB_mo3rb.txt:1942:ابن الحوزى وان النجار أنه أى الخواليق ‏ ولدفى ذى ألجة منة همس وستين 
ARB_mo3rb.txt:2391:ْ وكذلك يقولون : « كلجة » و« كلقة » و« قيلقة » ٠.‏ و« حربز » للربز ٠‏ 
ARB_mo3rb.txt:3171:إلى أنها سميت بالكلية المر بية ٠‏ ولعل أصل أسمها يقارب اللكدة » فعربت بلفظها ٠‏ 
ARB_mo3rb.txt:5176:البلاس» فظن أن الكسرفى باء ”بلاس ** فضوطه باللكسر وأ نه قد يفتهح © وتبعه مصححوالا موس فى هذا 
ARB_mo3rb.txt:7276:ا من اللكوفة 0 
ARB_mo3rb.txt:7626:ما _ثقلهم » ٠‏ ومته اللكاءة العامرة فى اميش « بواده » ٠‏ قال العلامة امد كتور ]أ أحد بك عيسى فى ا كم 
ARB_mo3rb.txt:12355:خطأ ٠‏ وق اللسان «أصله بالف لفارسية ”” رهوه '" » ٠‏ ( د اطملجة »: حسن السير ف صرعة 
ARB_mo3rb.txt:12613:منسوب إلى الرب »© ٠‏ فهذاز بدة قوطم ؛ وهسذًا ول سيبر به فى تصر يف اللكلينين ؛ فأين وجه تقلهمأ 
=== FSD lacquer ===
=== WEB ===
WEB_vol1.txt:104586:lac, lakh, x. [Hind. lakh; Sans. laékshé, a hun- dred thousand.] in India, the sum of 100,000, especially in counting money; as, a lac of ru- pees (written Rs. 1,00,000); also, a large, in- definite quantity.
WEB_vol1.txt:104587:lac, n. (Hind. lékh; Sans. lakshd.] a resinous substance deposited upon certain trees in southern Asia by a variety of scale insect. While still Sacked to twigs and dried, it is called stick-lac; when dissolved out and sepa- rated from the twigs it is called seed-lac, and when strained through a cloth and dried it constitutes shell-lac, or the shellac of com- merce. Lac is used extensively in making var- nishes, lacquers, sealing wax, dyés, etc. _
WEB_vol1.txt:104588:lac’cate, a. in botany, appearing as if having been varnished or lacquered: said of leaves.
WEB_vol1.txt:104590:lac’cO-lite, 2. same as laccolith.
WEB_vol1.txt:104626:lac’ér-a-ble, a. that can be lacerated. S
```


## [2026-09-04T19:38:41.603Z] TOOL CALL #31: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-04T19:38:41.608Z] TOOL RESULT

```


```


## [2026-09-04T19:38:43.895Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la incoming/PLA/ ; echo \"---\"; grep -c \"\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; grep -n -i \"lakk\\|laka\\|Lack\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10"
}
```


### [2026-09-04T19:38:43.956Z] TOOL RESULT

```
total 6832
drwxrwxr-x  2 sfmqrb sfmqrb    4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb    4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb  358695 Sep  4 14:06 PLA_asbaghi_1988_ia_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 5813714 Sep  4 14:06 PLA_asbaghi_1988_ia.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  807821 Sep  4 14:06 PLA_pages.txt
---
20505
2929:Wi - ”alkän: Pl. v. cf lakan q. v. 
6710:obs - garfas: "Wachs, Siegellack" = garbiSt, syr.jesn?, aram. un 10, 
6743:iso- Sarbiät: "Wachs, Siegellack" aus dem pers. gilhist 
7163:A - Zullakar: "Rosenzucker" pers. 13, aus dem pers. $’gol s. gul + pers. 
12494:ori» - sandrüs:; "Sandarak; roter Arsenik, Lack" 14 mand. sandlus, syr. 
13784:ep — saClaka: "Armut" s. saClük. 
17455:aIy- lakiyya: "Lack, Flüssigkeit, die an der Luft bei dünnem Auftragen 
17533:oe» agan: "Waschbecken lakan, aram. . 
17565:lakan 242 laimün 
17568:5) - lakan = lagan a. v. ı syr. is hebr. 138°.
```


## [2026-09-04T19:38:47.701Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17445,17480p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt"
}
```


### [2026-09-04T19:38:47.743Z] TOOL RESULT

```
% 
G,»,Y - lazwardi: "lasurblau", 


Br 


-. 
aIy- lakiyya: "Lack, Flüssigkeit, die an der Luft bei dünnem Auftragen 


zu einem festhaltenden Schutzfilm wird" hindustan >> pers, B> ar. 6, 


ob) - libäs: "Bekleidung" = al-basa q. v. 
albasa: Pl. v.«wls libäs _. 


w 


&- latt: "langhalsiges Trinkglas" pers, 7 ?. 
ZJ - latüt: Pl. v.Zulatt ga. v. 


e- lagf: "ungeheure Menge" pers. _D lak "tausend" 


1. Fremdwörterbuch s. v. 

2. Chista Bd. 10 s. v. 

3. BQ. s. v., Addai Scher s. v.
```


## [2026-09-04T19:38:49.946Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82lek-",
 "prompt": "Give the full reconstruction entry: root shape, meaning, and all descendants listed (Greek alexo, Sanskrit raksati, Germanic etc.), plus any references cited (Pokorny, Beekes, Mayrhofer)."
}
```


### [2026-09-04T19:38:57.529Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂lek-

## Root and Meaning
**\*h₂lek-** means "to protect"

## Reconstruction Notes
The LIV identifies two separate roots: "*h₂elk-" and "*h₂leks-". The latter is considered the source of "*h₂lékseti", though this verb is otherwise classified as deriving from "*h₂elk-".

## Derived Terms and Descendants

**Greek:**
- ἀλκή (alkḗ)

**Sanskrit:**
- रक्ष् (rakṣ) via Proto-Indo-Aryan

**Latin:**
- ulcīscor ("to avenge, punish") via Proto-Italic *olk-

**Germanic:**
- Proto-Germanic *algōną and *alhs (with descendants in West Germanic)

**Celtic:**
- Proto-Celtic *lexstus (with further descendants listed separately)

## References Cited
1. Rix, Helmut, ed. (2001). *Lexikon der indogermanischen Verben* [Lexicon of Indo-European Verbs]. 2nd ed. Wiesbaden: Dr. Ludwig Reichert Verlag. Pages 264, 278.
2. Kölligan, Daniel (2018). "A new look at the Greek desiderative." *Indo-European Linguistics* 6(1): 95-116.
3. Irslinger, Britta Sofie (2002). *Abstrakta mit Dentalsuffixen im Altirischen* [Abstracts with Dental Suffixes in Old Irish]. Heidelberg: Universitätsverlag C. Winter.
```


## [2026-09-04T19:39:08.286Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'ungeheure Menge' in p or 'lakiyya' in p:\n        print('leaf',i)\n        import re\n        # print header line\n        print(p[:200].replace('\\n',' | '))\n        for ln in p.split('\\n'):\n            if 'ungeheure' in ln or 'lakiyya' in ln or 'lak ' in ln: print('  >',ln.strip())\nEOF"
}
```


## [2026-09-04T19:39:08.744Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (140,141,142):\n    print('---leaf',i,'---'); print(pages[i][:2500])\nEOF"
}
```


### [2026-09-04T19:39:10.318Z] TOOL RESULT

```
leaf 254
lädan                                                                          240                                                                 ladg |  |  | ©>V - 1ädan:                   "Ladanumt      
  > aIy-               lakiyya:             "Lack,         Flüssigkeit,                  die       an   der    Luft      bei       dünnem       Auftragen
  > e-        lagf:          "ungeheure                 Menge"                  pers.        _D lak "tausend"
```


### [2026-09-04T19:39:11.998Z] TOOL RESULT

```
---leaf 140 ---
لاوم( -
ومعنى ¥ الماذب ٠‏ ويرادفة 6 :)10 `
القاطع : « قيل ان ܦ صمغ ܣܨ الرومي وهو في بلاد البلغار: وقيل صمغ
الدَوْم ٠‏ وقيل ضرب من الاؤلو يوجد في سواحل بجر المغرب ٠وقيل‏ صمغ شجر يشبه
شجر الفستق يشتعل بالنار مثل الكبريت ولهذا قيل له سيّد الكباريت ٠‏ وقيل يأبع
من ܐܐܟ في بلاد الروس واول مسا يضر به اللهواء يحمد مثل المرمر وهذا الحكهر باء
اقيق ويقال له بالعربّة مصباح الروم ٠‏ وقيل اله من انواع ܝ  -:‏ 50
ܟܗܪܒ̄ܐ
نكر 2 ) الذل الطغيد المخضر 6 6
٠ 1‏ 0 ير اراس لاحرؤة 4 او لآ حرظوم ل وهو معرب عن كوب ,
والثلاهر ان الكلمة من موافتات اللغات وهر حه كمط" بالارامية ( ¥+ 9 ]
ܐܟ ) ܕ ܟܘܦܐ بالسريانّة الدارجة وكرب بالتركّة والكردنة و :080 ܝ 4:80«
® ܕ ([011 باأرومسة و ¬ بالايطاليانئة و مناه بالاتكليزية و : 03
بالمرمانسة و 3 7 ® ܕ 0116 ¢ بالفرنسة و باس »ܨ بالارمنية ٠‏ والفعل
15 20000 روت 9 في كثير من 30 5( 063 493
¬ وهو حث 55 6.535 ( ± باليونانية
ܕ ¢€1100 ±7® ܕ 0211 بالرمانمة ܣ 0 ܕ 00120 ܐܠܬܝܐ
( آلكوقٍ ) تعريب ܰܘ وهو التصير
سنو كينت مس من قصب 990
3 الزارع على زرعه - والككاخ ܩܣ فيه »^ ܟܘܟܐ لعن رانحية الدارجة ܨ
بالتركيّة والكردبة
١ *‏ 5 وفي القاموس 5 ما جمعت من تراب ونحوه تعريب كود -
لعل 5
: وقال فيه الشاعر الفارسى‎ )١
ܥܐ كربي & مر ازو بردار خويشانرا يصبرده ܢܓ
3 | ܐ( )6 تيرد ܥܘ كلد كاه ܐܢܘ مسكين
---leaf 141 ---
9:4
# ( كرارة) النحل وتكسر وكؤارتها بتشديد الواو شيء ܡܳܐ ܐܗܐ من
القضبان او الطين ضيّق الراس ٠وقيل‏ هي عسلها في الشمع وقيل ܐ( الخلايا
الاهلءة وهي ܘܨ بة عن كْوَارَه ومعناها 965 وتطلق 0 على سهد العسل
* (الكارَة) ما يحمل على الظهر من الثياب ٠‏ وفي اللسان:« والكارة عكم
الثبات قاكارة التصار سيت لاله يكور نا شتف يون راح اياي كتوق را
فوق بعض ٠»‏ قلت والاصح انْ الكلمة فارسيّة ܬܨ بها كارّه وه وكل ما يحل على
الظهر من الثياب والمماب واككلا وغير 0 مركّة من كار اي عمل شغل
ومن هاء التخصيص ٠‏ ومنها ܪ فمل” كار 4 5 77 | ܟܪܬܐ
ܐܝܟ ܨܬ
5 5:5 له عروة و بلبل تعر ب ب كاز 9( (فرتكل :078 .
` ܫܫ اي شرب بالكوز واكتّازٌ ومئةُ ܟܘܙܐ
ܨ الال م1 جسن وهي طاولة كيرة نظير الكربة ار
أثناء المحاربة: واضل ܐܫܝ 30 ارا
بالفارسسة
( المُوسَح » الاثط والناقص 7 ٠‏ قال الأزهري لا أصل له في 3 `
وقال عضهم معرب واصلة كرسق او كوسه ٠وقيل‏ هوعرلي من ܚܝܢ الرجل ايم
بشت له .4 ( خبط الحيط)٠قلت‏ ان كُمَج مشتق من أ ܚܝ والكوسج معرب
01 َه وهو ال ܝܐ تظ والذى 3 عأ نبة وعشرون ٠‏ ܕ 4 4 كوسه ܓ والسر ±
الدارجة والكردنة
( انكر كع لانن عر كا نزي
* ( كاش يكوش ) اجتَهّد مثل أكوشيدن لفظاً ومعنى
* ( ألُولان ) فارسيّتة ܠ وهو ننت البردي
002390) | 32 ® 810 جسلئيوس في معجمه العبرائي 00
الكلمة ® ܘܐ من ܠ جدى ± اي عادل (ܟܐܢܝܐ) ܠܚܟ 20300
فارسّة الاصل 0 0 أي رفيع القدر ومن وان اي رقيب < ܨ
حى
---leaf 142 ---
‫ 1
ܢ ܐܟܟ - + 97 315 355 :انث كك بالقارشئة
ܘܚܐܘ الرفيع القدر ويطلق على الاك التهار المار وهو كنية عندهم عن ملك الاوك .
وار بعة من 46 دولتهم الثانية لُيَُوا به وهم كيكاوس وكيخسرو وكيتباد وى
هراسب ثم ; بق الغلبة على ܬܝܟ ܨ الدولة الثانية فقيل لهم ܫ
وهو جمع ‏ قي ( البيعان القاطع )
(اتكال) الة معوجة ܝ تهدم 0 ܟܒ 7 فارسّة فاذا صح
ذلك ك1 ادن 1 لشات :0600
+« ( الكلحَة ) كيل معروف لاهل العراق وهى 0 ܝܫܐ 0:00 ܦ
والفارسى ܝ ܨ ܟܝܠܐ :
لكا ) المطكى فارسيّة كنا
05
(اللازورد) 3 0
ال 1 الطرة معرب ليت
ܐ اللجام ) تعريب لكام وهو بالارامسة ܠܓܡܐ ܠܘܓܡܐ وباحدشة 1010 +
وبرادفة ܐܐܐܠ 4 (١‏ فرد ܀ \ ) ܕܝܢ 13100 ا 0 صل
< 1 ® ܐܪܝܐ من ܥ ܢ ® طلق 3 على الفك
ܨ
* (اللَج) الياعة الكثيرة ومعظم الماء تعريب 3 وهو اليش البالغ عدده
قات العك قر وتلق @) علي كل ما بلغ عدده مائة الف
([35) .27 ܥ وهو ضرب من الطيوب مر 3 ܨ العود ܕ ܐܫܡ
والمسك واللادن والكافور
```


## [2026-09-04T19:39:34.684Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%88%CE%BB%CE%AD%CE%BE%CE%B1%CE%BD%CE%B4%CF%81%CE%BF%CF%82",
 "prompt": "Give the etymology of Ἀλέξανδρος: components, meaning, and the descendants list (Latin, Arabic, Persian, Syriac, French, English etc.)."
}
```


## [2026-09-04T19:39:36.694Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%A7%DA%A9",
 "prompt": "Give all Persian entries for لاک: etymologies, meanings (lacquer/red resin, shell/tortoise), and any borrowing route from Sanskrit/Prakrit; also any descendants."
}
```


### [2026-09-04T19:39:41.422Z] TOOL RESULT

```
# Etymology of Ἀλέξανδρος (Alexandros)

## Components and Meaning

The name derives from three parts: "ἀλέξω" (to repel) + "ἀνδρ-" (stem of man) + "-ος" (masculine suffix). This literally means "the man who repels [enemies]."

## Notable Descendants

**Latin:** Alexander (with extensive Romance language descendants)

**Semitic Languages:** Arabic أَلِكْسَنْدَرُوس (alıksandarūs) and إِسْكَنْدَر (iskander), which spawned further derivatives across Arabic-speaking regions

**Persian:** Manichaean script ʾlxsyndr and Book Pahlavi variants

**European Languages:** Gothic alaiksandrus, Old Church Slavonic Алеѯандръ, Armenian Ալեքսանդր, Georgian ალექსანდრე, and Albanian Lleshdër

**Asian Languages:** Japanese アレクサンドロス (Arekusandorosu)

**Ancient Scripts:** Coptic ⲁⲗⲉⲝⲁⲛⲇⲣⲟⲥ, Egyptian hieroglyphic forms, and Etruscan variants

The name spread globally, particularly through Latin, which served as the primary vehicle for transmission across European and Mediterranean cultures.
```


### [2026-09-04T19:39:44.324Z] TOOL RESULT

```
# Persian Entries for لاک (lâk)

## Etymology 1: Wooden Vessel

**Origin:** Contraction of لاوک (lâvak), derived from Old Iranian *nāwaka- through a l < n sound change, ultimately from Proto-Iranian *náHuš meaning "boat."

**Meanings:**
- Trough; wooden vessel
- Tortoise shell (literal and metaphorical)

**Example:** "در **لاک** خودم فرو رفتم" (I went into my shell)

**Derived Terms:**
- لاک تراش (lâk-tarâš): lâk-maker
- لاک‌پشت (lâk-pošt): tortoise

**Descendants:**
- Tat: lak
- Judeo-Tat: lok
- Armenian: լաք (lakʻ) – dry measure; garden bed
- Azerbaijani: lək

---

## Etymology 2: Lacquer/Nail Polish

**Origin:** Borrowed from Prakrit लक्खा (lakkhā, "lac"), derived from Sanskrit लाक्षा (lākṣā)

**Meanings:**
- Nail polish (short for "lâk-e nâxon")
- Lacquer

**Related cognates:** Hindi लाख (lākh, "lac"); English "lac"
```


## [2026-09-04T19:39:50.762Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A4%BE%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE",
 "prompt": "Sanskrit लाक्षा (lākṣā): give the etymology (relation to रक्ष्/rakṣ, राग/rāga, *rakta 'red', Mayrhofer's view), meaning, and descendants (Prakrit, Persian, Hindi)."
}
```


## [2026-09-04T19:39:52.205Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%AC%D8%A9",
 "prompt": "Arabic لجة (lujja): give the etymology, root, meanings, and any note about a Persian origin. Also mention لج (lujj) if present."
}
```


### [2026-09-04T19:39:54.096Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T19:39:58.308Z] TOOL RESULT

```
# लाक्षा (lākṣā) - Sanskrit Etymology and Descendants

## Etymology

The origin of लाक्षा remains uncertain according to the Wiktionary entry. Manfred Mayrhofer's influential view proposes derivation from "*रक्ष्" (rakṣa), meaning "red" or "redness," connected to the verb "रज्" (raj, "to become red"). This theory links the word to Proto-Iranian "*raxšah" ("dark-colored").

An alternative etymology traces it to Proto-Indo-European "*laḱs-" (salmon/trout), similar to Latvian "lasis" and Russian "лосось" (losósʹ).

A third suggestion connects it to "लक्ष" (lakṣa, "one hundred thousand"), referencing the insects gathered to produce the resin.

## Meaning

लाक्षा denotes: (1) a botanical plant species; (2) "a kind of red dye, lac (obtained from cochineal or similar insect as well as from tree resin)"; (3) "the insect or animal which produces the red dye."

## Descendants

The word evolved across Indo-Aryan languages:
- **Hindi/Urdu**: लाख/لاکھ (lākh, "lac")
- **Punjabi**: ਲਾਖ (lākh)
- **Gujarati**: લાખ (lākh)
- **Marathi**: लाख (lākh)
- **Eastern variants** (with -ākhā): Bengali লাহা (laha), Assamese লা (la), Odia ଲାହା (lāhā)
```


## [2026-09-04T19:40:06.795Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A4%95%E0%A5%8D%E0%A4%B7",
 "prompt": "Sanskrit लक्ष (lakṣa): etymology, meanings ('mark', 'one hundred thousand'), relation to लक्ष् (lakṣ) and रक्ष् (rakṣ), and descendants (Prakrit, Hindi lākh, Persian)."
}
```


## [2026-09-04T19:40:08.076Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%AC#Arabic",
 "prompt": "Arabic لج / لجة: root, verb لجّ, meanings including 'deep sea, abyss, multitude', and any etymological note (Semitic root, or borrowing)."
}
```


### [2026-09-04T19:40:12.881Z] TOOL RESULT

```
# लक्ष (Lakṣa) - Word Overview

**Konkani meaning:** "attention, heed, notice"

**Sanskrit meanings:** The word has several definitions including "a mark, sign, token" and importantly "a lakh, one hundred thousand." It also refers to "appearance, show, pretence" and can denote "a kind of citron" or "a pearl."

**Etymology:** Derived from the Sanskrit root लक्ष् (lakṣ), this term traces back through Proto-Indo-European *h₂lek-.

**Numerical significance:** In Sanskrit mathematics, लक्ष represents 100,000 (१००००००), sitting between 10,000 and 1,000,000 in the number system.

**Linguistic descendants:** The word spawned numerous modern language variants including Hindi लाख (lākh), Gujarati લાખ (lākh), Bengali লাখ (lakh), and influenced languages beyond South Asia—appearing in English as "lakh," Persian as لک (lak), and even Swahili as "laki."
```


### [2026-09-04T19:40:14.618Z] TOOL RESULT

```
# لج (Laj) - Arabic Entry

Based on the Wiktionary page, **لج** has two primary etymologies:

## Verb Form (لَجَّ)
The verb means "to be stubborn" or "to be obstinate," with related meanings including insisting, persisting, bothering, or harassing. It conjugates as a Form I geminate verb with various tenses and voices documented in extensive conjugation tables.

## Noun Form (لُجّ)
This masculine noun refers to a "chasm" or "gap," and more profoundly, an "abyss" or the "depth of the sea." The plural forms are لُجَج (lujaj) or لِجَاج (lijāj).

## Root
Both forms derive from the Semitic root **ل ج ج** (l-j-j), indicating shared etymological heritage within Arabic's root-based morphological system. The entry includes a 2017 Iraqi news citation demonstrating practical usage in modern Arabic texts, referring to a geographical gap or checkpoint.
```


## [2026-09-04T19:40:29.890Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/lacquer",
 "prompt": "Give the full etymology of lacquer, and any related entries shown for lac, lakh, shellac (Portuguese lacre, laca, French lacre/laque, Persian lak, Sanskrit laksha)."
}
```


## [2026-09-04T19:40:29.919Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/shellac",
 "prompt": "Give the etymology of shellac and of lac (the resin) and lakh as shown on the page."
}
```


### [2026-09-04T19:40:36.746Z] TOOL RESULT

```
# Etymology of Lacquer

## Lacquer (noun)
"1570s, 'dye obtained from lac'" and later "1670s as 'gold-colored solution of shellac,'" lacquer traces its path through Romance languages. It derives from obsolete French *lacre* (a sealing wax type), which came from Portuguese *lacre*—itself an unexplained variant of *lacca* meaning resinous substance. This ultimately connects to Arabic *lakk* and Persian *lak*.

## Lacquer (verb)
Dating to the "1680s, 'cover or coat with lacquer,'" this form derives from the noun, with related terms including *lacquered* and *lacquering*.

## Related Entry: Lac
The foundational term "red resinous substance" (1550s) likely came through French *lacce*, displacing earlier English *lacca*. Medieval Latin *lacca* connects to Persian *lak*, which traces to Hindi *lakh* and Sanskrit *laksha* meaning red dye.

Scholars propose multiple origin theories: Klein and the Century Dictionary suggest it literally means "one hundred thousand," referencing the insects' vast numbers. Alternatively, some etymologists propose it derives from an Indo-European root relating to "color, dye," while Barnhart suggests possible connection to salmon's coloration (*lax, lox*).
```


### [2026-09-04T19:40:38.032Z] TOOL RESULT

```
# Etymology of Shellac and Lac

## Shellac (noun, 1713)
Shellac combines "shell" + "lac," referring to "lac melted and formed into thin plates." It translates French *laque en écailles* ("lac in thin plates"). Commercially, lac was available as stick lac, seed-lac, or fully processed shell lac plates.

## Shellac (verb, 1876)
The verb means "coat or varnish with shellac," derived from the noun. Slang senses developed later: "beat soundly" by 1930 and "drunk" by 1922.

## Lac (noun, 1550s)
Lac is "red resinous substance (an incrustation deposited by females of an insect on twigs of certain trees in southern Asia)." It comes from French *lacce* or Medieval Latin *lacca*, ultimately from Persian *lak*.

## Lakh
The Hindi word *lakh* derives from Sanskrit *laksha* ("red dye"), possibly meaning "one hundred thousand" and referencing "the insects that gather in great numbers on the trees and create the resin." Alternative theories connect it to Sanskrit roots for "color, dye" or suggest resemblance to salmon coloring.
```


## [2026-09-04T19:40:44.891Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B3%DA%A9%D9%86%D8%AF%D8%B1",
 "prompt": "Persian اسکندر (Eskandar/Iskandar): give the etymology (from Arabic الإسكندر, from Greek Alexandros; any note on the al- being taken as the Arabic article, or Syriac mediation), and meanings."
}
```


## [2026-09-04T19:40:47.596Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A5%D8%B3%D9%83%D9%86%D8%AF%D8%B1",
 "prompt": "Arabic إسكندر (Iskandar): give the etymology in full — Greek Ἀλέξανδρος, any mention of Syriac ܐܠܟܣܢܕܪܘܣ, the reanalysis of Al- as the definite article, and descendants (Persian, Turkish, etc.)."
}
```


### [2026-09-04T19:40:51.538Z] TOOL RESULT

```
# Etymology of Persian اسکندر (Iskandar/Eskandar)

## Origin Path
The word traces back through multiple languages: Persian inherited it from Middle Persian, which adopted it from Arabic, which in turn derived it from Ancient Greek.

## Direct Sources
According to the Wiktionary entry, the term comes "from Arabic _[إِسْكَنْدَر](/wiki/%D8%A5%D8%B3%D9%83%D9%86%D8%AF%D8%B1#Arabic 'إسكندر')_ (ʔiskandar), from [Ancient Greek](https://en.wikipedia.org/wiki/Ancient_Greek 'w:Ancient Greek') _[Ἀλέξανδρος](/wiki/%E1%BC%88%CE%BB%AD%CE%BE%CE%B1%CE%BD%CE%B4%CF%81%CE%BF%CF%82#Ancient_Greek 'Ἀλέξανδρος')_ (Aléxandros)."

## Meaning
It functions as a masculine given name equivalent to the English "Alexander," often appearing in historical contexts like "اسکندر مقدونی" (Alexander the Great, literally "Alexander the Macedonian").

The entry doesn't explicitly address whether Arabic's "al-" represents the definite article or discuss Syriac mediation, though the documented Greek-to-Arabic-to-Persian transmission is clear.
```


### [2026-09-04T19:40:53.075Z] TOOL RESULT

```
# Etymology of إسكندر (Iskandar)

Based on the Wiktionary entry, here's the etymology:

The Arabic name **إسكندر** (Iskandar) derives "Ultimately from Ancient Greek _Ἀλέξανδρος_ (Aléxandros)." The linguistic development involved a reanalysis phenomenon: the original form was "الْإِسْكَنْدَر (al-ʔiskandar)" where the definite article "الْ (al-)" was rebracketed, causing the initial syllable to be lost over time.

**Note on the source:** The Wiktionary article does not mention Syriac cognates or provide an extensive list of descendants beyond Persian. The documented descendants include Persian, Turkish (implied through Persian descendants), Malay, Indonesian, Amharic, Kurdish, and several other languages, but these are presented as borrowings rather than a comprehensive linguistic family tree.

The entry focuses on the Greek origin and the Arabic rebracketing process as the key etymological mechanism rather than comparative Semitic or broader Near Eastern language connections.
```


## [2026-09-04T19:40:59.988Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%84%D8%AC%D9%87/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for لجه — the origin tag (e.g. [ع.]) and the definitions. Also any Dehkhoda note."
}
```


## [2026-09-04T19:41:00.992Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%84%DA%A9/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for لک — origin tag and definitions (especially 'hundred thousand'), and any Dehkhoda etymology note."
}
```


### [2026-09-04T19:41:05.124Z] TOOL RESULT

```
# لجه — Farhang-e Mo'in Entry

**Origin tag:** [ع.] (Arabic)

**Definition:** "میانۀ دریا" (the middle/midst of the sea)

**Dehkhoda note:** The Dehkhoda lexicon provides extensive etymological information, explaining that لجة originally derives from the root لجاج (stubbornness/persistence), later applied to sound vibrations in the throat, and eventually to the churning waves of the sea. It notes the word describes deep, turbulent water where waves continuously move back and forth.
```


### [2026-09-04T19:41:10.126Z] TOOL RESULT

```
# لک (Lak) — Farhang-e Mo'in Entry

According to the **Farhang-e Mo'in** dictionary section provided, لک has several definitions:

**Key meanings:**
- A type of gait/movement pattern in camels, horses, etc., occurring between trotting and walking
- Coarse, rough, or unfinished (in Afghan usage)
- Armless; lacking a hand
- Nonsensical or idle talk
- A mark, stain, or blemish on fabric or clothing
- A fool or simpleton
- Miserly; stingy
- Ragged cloth; worn-out garment
- A swelling, lump, or node on the body
- A soft skin condition

**Notably**, the dictionary entry does **not explicitly highlight "hundred thousand"** as a primary definition in the Mo'in section shown. However, the **Dehkhoda dictionary section** references the Sanskrit/Hindi origin: لک in Sanskrit means "hundred thousand" (صدهزار).

The Dehkhoda notes suggest the ethnic group "Lak" may derive from this numerical term, as some sources propose they were named after having approximately 100,000 people.
```


## [2026-09-04T19:41:22.815Z] TOOL CALL #49: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂lek-' \\\n 'https://en.wiktionary.org/wiki/Ἀλέξανδρος' \\\n 'https://en.wiktionary.org/wiki/لاک' \\\n 'https://en.wiktionary.org/wiki/लाक्षा' \\\n 'https://en.wiktionary.org/wiki/लक्ष' \\\n 'https://en.wiktionary.org/wiki/لج' \\\n 'https://www.etymonline.com/word/lacquer' \\\n 'https://www.etymonline.com/word/shellac' \\\n 'https://en.wiktionary.org/wiki/اسکندر' \\\n 'https://en.wiktionary.org/wiki/إسكندر' \\\n 'https://abadis.ir/fatofa/لجه/' \\\n 'https://abadis.ir/fatofa/لک/' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 49, root Alek (Alexander / lak / lac branch)' 2>&1 | tail -2\ndone"
}
```


### [2026-09-04T19:41:32.569Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/430e42a1f689a61f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/97f6111197682e03.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b24a51f96257b227.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/04dbf39ee6a3e7ab.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/03449b30e936b1eb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/220e610d6a7c080c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c94f930a667e3eee.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9e4aaf1d4d4b682a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/561713a3fd1f931d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e6c805835844ef1e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/416d333aa8701ee1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7699ef3e4b6934e5.txt
```


## [2026-09-04T19:41:39.772Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 aleq ===\"; grep -n \"aleq-\\|áleq\\|ale\\^q\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10\necho \"=== FSD lacquer ===\"; grep -ln -i \"lacquer\" FSD_vol*.txt; grep -n -i \"lac, n\\.\\|lakh, n\\.\" FSD_vol2.txt FSD_vol3.txt 2>/dev/null | head -6\necho \"=== ARY لاک ===\"; grep -n \"لاک\\|لاك\" incoming/ARY/ARY_pages.txt | head -8\necho \"=== RCH lak ===\"; grep -n -i \"hundred thousand\" RCH.txt | head -6"
}
```


### [2026-09-04T19:41:39.897Z] TOOL RESULT

```
=== WLD Bd1 aleq ===
=== FSD lacquer ===
FSD_vol2.txt
FSD_vol4.txt
FSD_vol1.txt
=== ARY لاک ===
1695:ارمنی (4۵120/4۸): آشلاک۸ رالشآطگ۸ چکه (لل)28)): 05۸
1769:انگلیسی کهن (لاکلا8۸0 ۰:۵۵ ۲۸۱۸۵۴ ,97 (17۸۸13/53) 1
1824:دانمارکی (0۸۷]57): 205 ولزی (لاکا۷): 151
2211:لاتین (471۸مل): 07۸ ایرلندی کهن (لاکلقا 2ا0): . ۸۵7۲۲
2318:۲ ۲ اروند(به چم"تند و تیز و چالاک و دلیر»)
6316:اسپانیایی (8۳۸(187): 31.0 ایرلندی کهن (لاکلها صا0):
6437:کر دی (8/01517): :5ل2 لاک ۱۸۸
7174:پهلوی (1شالق۸ه). ولزی (لاکا75(): لری ۱1۹۳۹
=== RCH lak ===
```


## [2026-09-04T19:41:46.965Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD vol2 lac ===\"; grep -n -i \"Skt\\. laksha\\|Hind\\. lakh\\|lakh\\b\" FSD_vol2.txt | head -8\necho \"=== WLD Bd1 p89 ===\"; grep -n \"ealgian\\|alhs\\|raksati\\|rákṣati\\|alexo\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-04T19:41:47.039Z] TOOL RESULT

```
=== FSD vol2 lac ===
70947:Lake'wood,  1   ISk'wud;  3   lak'wdhd,  n.  1.  A   village  and health  resort  In  Ocean  county,  N.  J.;  59  m.  S.  W.  of  New York  city.  3.  A   hamlet  in  Cuyahoga  county,  O.  [Fla. Lake  Wood'rnff.  A   lake  and  winter  resort  in  Volusia  county, lakh,  n.  [Anglo»Ind.]  1.  The  sum  of  100,000;  when  used absolutely,  100,000  rupees,  formerly  equivalent  to £10,000,  or  $48,500;  for  modern  value,  see  coin.  The word  was  used  originally  to  express  100,000  objects  of  any kind,  as  spears  or  lanterns;  but  in  modern  times  its  use  has been  confined  to  money.  In  Java  and  other  Malayan  coun- tries faith  has  been  adopted  from  the  Hindustani,  but  is  used for  10,000  instead  of  100,000.
=== WLD Bd1 p89 ===
5944:ags. ealtjian .,schiitzen, verteidigen“ ( *algdjan got. alhs (f., kons. St.) 
5987:Hoffmann BB. 25, 106 aus *ai.y.io g zu alhs gestellt, ist am natiirlichsten als *ai.ziog mit 
10136:Pedersen II 571 f. ; und mcymr. ry-yalhs „ist fortgegangen“ corn, gallas „ ist 
32524:wovon ag. fealgian, mhd. valgen, velgen , nhd. falgcn , f eigen „ein Brachfeld
```


## [2026-09-04T19:41:49.485Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5930,5950p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-04T19:41:49.527Z] TOOL RESULT

```
90 


alo-, alno alo-, alu- 


mutlich durch ZusammenflieBen mit einem anderen, dem mp. ark „Arbeit, 
Anstrengung, Miihe 11 entsprechenden Worte, s. Bartholomae Heidelbg. SB. 
1916, IX 10; d'/.y.l Tisjioidmg Horn., a/.y.iuog „stark, kraftig; von Waffen: 
wehrbar, zum Kampfe tauglichl; 

ags. ealtjian .,schiitzen, verteidigen“ ( *algdjan got. alhs (f., kons. St.) 
„Tempel“, ags. ealh, as. alah ds., urnord.-run. alh „Amulet“, alit. elkas, alkas 
„heiliger Hain, Stelle auf einem Hiigel, wo man friiher Opfer verriehtet 
bat“, lett. elks „Gotze“ (die grm. und bait. Worte ursprgl. „heiliger, abge- 
schlossener oder der NutznieBung entzogener Hain 11 ) 1 ). 

Z. B. Tick I 4 122, 299, 535, III 4 21. — S. die ahnliche Wz. arek- „ver-
```


## [2026-09-04T19:41:53.779Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5905,5932p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-04T19:41:53.827Z] TOOL RESULT

```
lieder singen“ s. Berneker 6S2, iiber gr. d/.ugcov s. Wz. *al- „schwcifen“). 

S. die iihnliche Schallwurzel la-. 

alek- „abwehren, schiitzen“, vermutlieh eigentlich „abschlieBen und dadurch 
sebiitzen". 

Ai. ralcsati „hiitet, schirmt, bewahrt“, gr. d/Jgo) „wehre ab, schii-me“ (so- 
Praesens; rat sail wegen aieser Ubereinstimmung nicht wahrscheinlicher 
zur gleichbed. Wz. arck-), AXextioq, AXey.Tovcbv epische Eigennamen, die 
nach dem Bekanntwerden des Hahns auch zur Bezeichnung dieses streit- 
baren Tieres verwendet wurden (Fick CSt. 9, 169, Kretschmer KZ. 33, 559 ff., 
Boisacq 1091 f . ; Gdf. *AXegr(oo, wo r aus * A/Jyhooo und nach andern Worten 
auf -xwo AXrxx(oo ) ; uXaXy.eXv „ab\vebren“, dXy.uAo) „\velire ab, helfe“, nXy.no 
„Schutz, Schutzwelir, Hilfe“, t'omXgtg ..Scliutz, Brustwehr, bes. Zinnen der 
Mauern; Hilfe“ (*aXy.-u-g), dXy.i) „Abwehr, Hilfe“ und ,. Starke. Kraft“ 
(letztere Bed., obwohl an sich aus ,.energischer Abwehr 1- verstandlich, ver- 


') a)M n nicht nach Fick BB. 5, O’, 8, Wh. I 4 516 als 'ml- zu *md- „mahlen“ (s. da- 
gegen J. Schmidt Krit. S3, Kretschmer Kinleitung 10-9. t/.v/io ; „Hii.se“. o/.roa r Spelt', 
ov/.ai, att. o/.«t „geschrotetes Getreide” ("o/.p-, nicht nach J. Schmidt KZ. 32, 382 aus 
wiiren zwar lautlieh vereinbar (Wz. wine dann 'cl-, *ol-, ' doch liegt ei_rent- 
lich kein Anlafi vor, in diesen Worten nach Schmidt aaO. und Boisac-j s. v. gerade 
den Begriff des Mahlens zu suehen (andere Versuche bei Prellwitz 2 s. vv.).
```


## [2026-09-04T19:42:10.759Z] TOOL CALL #54: Bash

```json
{
 "command": "ls data/ && ls data/extracted/ | head && find . -maxdepth 3 -name \"*.pdf\" -not -path \"./data/verification/*\" 2>/dev/null | head"
}
```


### [2026-09-04T19:42:10.809Z] TOOL RESULT

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


## [2026-09-04T19:42:13.614Z] TOOL CALL #55: Bash

```json
{
 "command": "python3 -c \"\nimport subprocess\n\" ; pdftotext -f 49 -l 49 -layout EtymologicalDictionary-persian-english.pdf - 2>/dev/null | head -60"
}
```


### [2026-09-04T19:42:15.374Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:42:20.234Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 49 -l 49 -r 150 -png /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf p49 && ls -la p49*"
}
```


### [2026-09-04T19:42:22.410Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 56356 Sep  4 15:42 p49-049.png
```


## [2026-09-04T19:42:24.466Z] TOOL CALL #57: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p49-049.png"
}
```


### [2026-09-04T19:42:24.488Z] TOOL RESULT

```

```


## [2026-09-04T19:43:10.942Z] AGENT

Now I'll write the verification file.


## [2026-09-04T19:47:17.184Z] TOOL CALL #58: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-49.json",
 "content": "{\n  \"pdf_page\": 49,\n  \"book_page\": 19,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Alek\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂lek- / *h₂elk- 'to ward off, protect' (Pokorny 32 aleq-; Walde-Pokorny I 89-90 alek-; AHD/Watkins alek-)\",\n      \"note\": \"The root box is right: Pokorny prints 'aleq- \\\"abwehren, schützen\\\", vermutlich eigentlich \\\"abschließen und dadurch schützend\\\"' on p.32 with exactly the two anchors Nourai draws from it (Skt. rákṣati, Gk. ἀλέξω). Watkins/AHD spells it alek- 'To ward off, protect'; LIV/Wiktionary now write *h₂elk- ~ *h₂leks- (laryngeal notation), a notational, not substantive, difference. The Alexander branch (nodes 1-7) is uncontroversial. The whole lower branch (nodes 8-15) rests on one contested equation — that Sanskrit lakṣa 'mark; 100,000' and lākṣā 'lac' belong to rakṣ- 'protect' rather than to raj- 'to redden' — and Nourai himself flags the alternative in his notes. Mayrhofer, Skeat, Hobson-Jobson and Wiktionary's lākṣā entry prefer the 'redden' origin for the resin word; Klein (whom Nourai follows) and Wiktionary's lakṣa entry keep the numeral with *h₂lek-. So the transmission chains (India → Persia → Arabia/Europe) are all well attested; only their attachment to this root is in doubt. Note that Pokorny p.32 does NOT in fact list lakṣa/lākṣā at all — it has only the verb rákṣati — so the POK:32 citation on node #8 is weaker than the chart implies.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂lek-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:32\", \"status\": \"supports\", \"note\": \"POK_01.txt, \\\\f-leaf 40 (leaf = p+8, so printed p.32): 'aleq- ,abwehren, schützen', vermutlich eigentlich ,abschließen und dadurch schützend. Ai. rdksati ,hütet, schirmt, bewahrt', arm. aracel, gr. dXe^co ,wehre ab, schirme' ... WP. I 89 f.' Root, gloss and language label all as printed by Nourai.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"alexein; alex-andros\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gk. ἀλέξω / ἀλέξειν 'ward off, defend' continues *h₂leks-, an s-extension of *h₂lek-, beside the zero-grade noun ἀλκή 'strength, defence' (*h₂lk-eh₂) and ἄλκιμος 'strong'; Pokorny already notes that ἀλέξω is a so-present matching Skt. rákṣati exactly. Ἀλέξανδρος is a bahuvrīhi-type compound of the desiderative ἀλέξειν 'to ward off, protect' + ἀνήρ, gen. ἀνδρός 'man' + -ος, i.e. 'he who wards off (for) men, defender of men'; the name is Mycenaean-old (a-re-ka-sa-da-ra = Alexandra at Mycenae/Pylos) and is the epic by-name of Paris in the Iliad, long before Alexander III of Macedon (356-323 BCE) carried it to Egypt, Syria and Iran. Nourai's gloss 'protector of men' is Klein's 'defender of men'.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Ἀλέξανδρος\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂lek-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1506\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt (the 1985 standalone reprint of the same Watkins appendix Nourai cites at pp.1505-1550): 'alek-. To ward off, protect. Earlier form *olek-. 1. Suffixed zero-grade form *alk-a- in Greek alkē, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleq- 32.]' — p.1506 is the second page of the appendix, exactly where alek- falls alphabetically.\"},\n            {\"ref\": \"KLN:47\", \"status\": \"supports\", \"note\": \"KLN_1966.txt \\\\f-leaf 36 (≈ printed p.47), s.v. 'Alexander, masc. PN. — L. Alexander, fr. Gk. Ἀλέξανδρος, lit. \\\"defender of men\\\", fr. ἀλέξειν, \\\"to ward off, keep off, turn away, defend, protect\\\", and ἀνήρ, gen. ἀνδρός, \\\"man\\\". Ἀλέξειν is desiderative of ἀλέκειν, \\\"to ward off\\\", which is related to ἀλκή ... and cogn. with OI. raksati, \\\"protects\\\" ...'\"},\n            {\"ref\": \"KLN:856\", \"status\": \"partial\", \"note\": \"KLN_1966.txt \\\\f-leaf 460 is the 'lac, lakh' page (vol. II opens at p.855, so the lac entries stand at p.856). It is relevant to this node only through Klein's own cross-reference 'Cp. also lac, \\\"one hundred thousand\\\"' printed at the end of the Alexander entry — i.e. it supports the LINK to node #8, not the Greek forms themselves.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_01.txt leaf 40 = p.32\", \"stance\": \"supports\", \"note\": \"'gr. dXe^co ,wehre ab, schirme' (so-Präsens) ... AXe^rjvcoQ, AXsxtqvcov epische Eigennamen' — Pokorny cites the epic proper names built on ἀλεξ-.\"},\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd1_1930_dli_70244_djvu.txt, Bd. I pp.89-90\", \"stance\": \"supports\", \"note\": \"'alek- \\\"abwehren, schützen\\\" ... Ai. raksati \\\"hütet, schirmt, bewahrt\\\", gr. dXego \\\"wehre ab, schirme\\\" ... AXextroq, AXextovcov epische Eigennamen' — the source Pokorny abridges.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. alek-\", \"stance\": \"supports\", \"note\": \"'Extended form *aleks- in Greek alexein, to protect'.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt line 424\", \"stance\": \"supports\", \"note\": \"Mann: 'aleks-, alks- \\\"ward off, protect\\\". WP I, 89. Cf. alkos Skt. raksami; Arm. ayxem; Myc. & Gk. aléxo, alexéo'.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 36 s.v. Alexander\", \"stance\": \"supports\", \"note\": \"See ref_check above.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Arabic\",\n          \"words\": \"Eskandar\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gk. Ἀλέξανδρος entered Arabic through the Syriac Alexander Romance tradition (Syr. ܐܠܟܣܢܕܪܘܣ Aleksandrōs), where the Arabic-speaking transmitters heard the opening Al- as their own definite article: al-Iksandar > al-Iskandar, and the bare stem was then extracted as إِسْكَنْدَر Iskandar — a textbook rebracketing, with a prothetic i- breaking up the ks- cluster and Gk. -dros reduced to -dar. Arabic preserves the un-rebracketed أَلِكْسَنْدَرُوس aliksandarūs beside it, which is the proof of the mechanism. The figure reached the Arabs above all as Dhū l-Qarnayn of Qurʾān 18:83-98, identified with Alexander by the early commentators, and as the hero of the Arabic Alexander legends. Nourai's arrow Greek → Arabic is right; the intermediary he leaves out is Syriac.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/إسكندر\",\n            \"https://en.wiktionary.org/wiki/Ἀλέξανδρος\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON5:144\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 5 (اعلام / proper names) is not online: archive.org has only the 2-vol Adena abridgement of the lexicon volumes, whose OCR (MON_part1.txt/MON_part2.txt) is unusable Persian garbage — grep for 'اسکندر' returns 6 spurious hits of broken glyphs. vajehyab/abadis carry only the lexicon volumes, not the a'lam volumes, so page 144 of vol.5 cannot be reached.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 36 s.v. Alexander\", \"stance\": \"silent\", \"note\": \"Klein traces the name only to Latin and Greek; he says nothing about the Arabic or Persian forms.\"},\n            {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt, searched for Iskandar / Alexander\", \"stance\": \"silent\", \"note\": \"Jeffery's Foreign Vocabulary treats Dhū l-Qarnayn but has no headword for the name Iskandar, which is not itself a Qurʾānic lexeme.\"},\n            {\"src\": \"AFM\", \"where\": \"AFM_pages.txt, alphabetical Arabic headwords\", \"stance\": \"silent\", \"note\": \"Addi Shir lists arabized Persian common nouns, not Greek proper names; no إسكندر entry.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"Eskandar «اسکندر»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP اسکندر Eskandar is the Arabic إسكندر Iskandar taken back into Persian after the conquest, replacing the older Iranian rendering of the name (Manichaean Middle Persian ʾlksyndr, Book Pahlavi Aleksandar of the Zoroastrian tradition, where he is 'Alexander the Accursed', gizistag). The tell-tale sign that the Persian form is the Arabic one and not an inherited Middle Persian one is precisely the missing Al-: an unbroken Iranian transmission would have kept it (as Manichaean ʾlksyndr does). Hence Greek → Syriac → Arabic → Persian, exactly the route the chart draws for the Arabic → Persian leg. Hāfez's line quoted in the box (آیینهٔ سکندر جام میست) uses the further-shortened poetic form Sekandar.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/اسکندر\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON5:144\", \"status\": \"not_checked\", \"note\": \"Same as node #2: Mo'in vol. 5 (a'lam) is not available online or on disk in readable form.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab/abadis carry only Mo'in's lexicon volumes\", \"stance\": \"silent\", \"note\": \"The proper-name volumes (5-6), which is where MON5:144 lives, are not digitised; no Mo'in text for اسکندر could be read.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (Mo'in ed.)\", \"stance\": \"silent\", \"note\": \"Borhan is a dictionary of Persian common vocabulary; the historical name اسکندر is not among the etymologised headwords Mo'in footnotes.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"Alexander\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin took the name straight from Greek in the republican period, Ἀλέξανδρος → Alexander with the regular Latin treatment of Greek -ros in a name (nom. -er, gen. Alexandrī), the same substitution seen in Alexandrīa < Ἀλεξάνδρεια. From Latin it passed to the whole Christian West, carried by the Alexander Romance and by the many popes and saints of the name.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Ἀλέξανδρος\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:47\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 36 (≈ p.47): 'Alexander, masc. PN. — L. Alexander, fr. Gk. Ἀλέξανδρος' — precisely the Greek → Latin arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 36 s.v. Alexander\", \"stance\": \"supports\", \"note\": \"'L. Alexander, fr. Gk. Ἀλέξανδρος'.\"},\n            {\"src\": \"LEW\", \"where\": \"LEW_1910.txt (Walde, Lat. etym. Wb.)\", \"stance\": \"silent\", \"note\": \"Walde's Latin etymological dictionary excludes Greek proper names; no Alexander headword.\"},\n            {\"src\": \"LAT\", \"where\": \"LAT.txt (Ernout-Meillet)\", \"stance\": \"silent\", \"note\": \"Likewise no entry — Ernout-Meillet does not treat borrowed personal names.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"Alexandre\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old French Alexandre is the learned/semi-learned continuation of Lat. Alexander, with the usual French treatment of Latin final -er in a proper name (cf. Alexandrie < Alexandrīa). It was made a household word by the twelfth-century Roman d'Alexandre of Alexandre de Bernay (de Paris), whose twelve-syllable line gave French — and then English — the term 'alexandrine'.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Ἀλέξανδρος\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON5:144\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 5 not accessible (see node #2). Nourai cites it here for the French form only as the source of the Persian transcription in node #6.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 36, s.v. Alexandrine\", \"stance\": \"supports\", \"note\": \"'F. alexandrin; so called because first used by the French poet Alexandre de Paris (de Bernai) in a poem on Alexander the Great, dating from the 13th cent.' — attests OF Alexandre as the Latin name's French shape.\"},\n            {\"src\": \"DEV\", \"where\": \"DEV.txt (Devic, mots français d'origine orientale)\", \"stance\": \"silent\", \"note\": \"Devic covers only French words of Oriental origin; Alexandre, coming from Latin, is outside his scope.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"Alexândr «الکساندر» (also آلکساندر)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"الکساندر / آلکساندر is a modern (19th-20th c.) Persian transcription of the European personal name, used for foreigners (Alexandre Dumas, Tsar Alexander) as opposed to the naturalised اسکندر of node #3. The spelling betrays its route: the initial ال- is written out (no rebracketing), the final cluster -ndr is kept unvocalised on the French pattern Alexandre [alɛksɑ̃dʁ], and the variant آلکساندر with alef-madda marks the long ā of the French/Russian pronunciation. So the arrow French → Persian is right for this form, and it is a doublet, not an ancestor, of Eskandar.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/اسکندر\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON5:173\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 5 (a'lam), p.173 — not digitised; see node #2. The bracketed origin tags Mo'in uses for such words ([فر.] = French) are visible for lexicon entries on vajehyab/abadis, but a'lam entries are not carried there.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab / abadis (Mo'in lexicon volumes only)\", \"stance\": \"silent\", \"note\": \"No a'lam-volume text online; the French tag Nourai relies on could not be read.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (17th c. text, Mo'in ed.)\", \"stance\": \"silent\", \"note\": \"A pre-modern dictionary cannot contain a 19th-20th c. European transcription; correctly silent.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"Alexander\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Alexander comes in with the Latin form unchanged, through the Church and through the immensely popular medieval Alexander literature (the Middle English alliterative Alisaunder, and Kyng Alisaunder, both from Old French Alexandre/Alisandre); the modern spelling Alexander is the Latin one restored in the Renaissance. Nourai's arrow Latin → English is thus right, with Old French as the medieval vehicle. Derivatives in English: alexandrine, alexanders (the plant), alexandrite.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Ἀλέξανδρος\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"The node carries no refs= in the book (the English box on the scan has no citation icon), so there is nothing of Nourai's to check.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 36 s.v. Alexander, alexanders, Alexandrine, alexandrite\", \"stance\": \"supports\", \"note\": \"Klein enters Alexander as an English headword derived 'L. Alexander, fr. Gk. Ἀλέξανδρος', with the English derivatives listed.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt (Webster's New Twentieth Century, vol. I A-...)\", \"stance\": \"supports\", \"note\": \"Webster carries Alexandrian/alexandrine from the same Latin-Greek name; no competing origin offered.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\", \"note\": \"Skeat's Concise excludes personal names; no Alexander headword.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"lâkšâ, rakšâ; lâk, râk\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Three separate claims are packed into this box and they do not stand or fall together. (a) Skt. rakṣā f. 'protection' / rákṣati 'protects' really does belong to *h₂lek- (Pokorny p.32, WP I 89, Klein, Mann) — that part is solid, but its gloss here is not 'protection' at all. (b) Skt. lakṣá- 'mark, sign; one hundred thousand' is derived by Klein and by Wiktionary from the root lakṣ- 'to mark' and thence from *h₂lek-, the l- being a dialectal Indic substitute for r- (rakṣ- ~ lakṣ-); this is defensible and is what Nourai follows. (c) Skt. lākṣā́ f. 'lac, the red resin/dye and the insect that makes it' is the weak link: Mayrhofer (KEWA/EWAia) reconstructs *rakṣā 'redness' to raj-/rañj- 'to redden, dye' (cf. rakta- 'red', Proto-Iranian *raxša- 'dark-coloured'), i.e. Nourai's own alternative root 'Reg: to dye', and Skeat and Hobson-Jobson say the same ('Skt. lakshā, for rākshā'); the connection with lakṣa '100,000' (allegedly the swarm of insects) is an ancient folk-etymology repeated by Klein and Lokotsch. (d) The forms 'lâk, râk' printed here are not Sanskrit at all: Sanskrit has lākṣā́, and the monosyllable is Middle Indic — Pali lākhā, Prakrit lakkhā, whence Hindi/Hindustani lākh. Verdict for the node = the worst of its words: disputed, because the resin sense is more probably from *(h₁)reg- 'to dye' and because the cited POK:32 page does not contain either lakṣa or lākṣā.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/लाक्षा\",\n            \"https://en.wiktionary.org/wiki/लक्ष\",\n            \"https://www.etymonline.com/word/shellac\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:32\", \"status\": \"partial\", \"note\": \"POK_01.txt leaf 40 = p.32: the aleq- article contains only 'Ai. rdksati ,hütet, schirmt, bewahrt' (and the remark that rakṣati is not more plausibly to be put with the synonymous root areq-). Neither lakṣa 'hundred thousand' nor lākṣā 'lac' is mentioned anywhere on the page, so Pokorny does not support the '100,000 soldiers / insects / tree resin' glosses at all — he supports only the verb 'protect'.\"},\n            {\"ref\": \"KLN:47,856\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 460 (= printed p.856, the first L-page of vol. II): 'lac, lakh, n., 1) one hundred thousand; 2) a great number. — Pers. lak, fr. Hind. lakh, ult. fr. OI. lākṣa, \\\"one hundred thousand\\\", prop. \\\"sign, mark\\\", rel. to lakṣati, lakṣayati, \\\"marks, characterizes, defines\\\", and prob. also to rákṣā, \\\"protection, deliverance, preservation, observation\\\", rakṣati, \\\"protects\\\" ... and cogn. with Gk. ἀλέξειν, ἀλέκειν, \\\"to ward off\\\". See Alexander.' Klein is exactly Nourai's source, and leaf 36 (p.47) closes the Alexander entry with 'Cp. also lac, \\\"one hundred thousand\\\"'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_01.txt leaf 40 = p.32\", \"stance\": \"partial\", \"note\": \"Only rákṣati; no lakṣa/lākṣā.\"},\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd1 pp.89-90 s.v. alek-\", \"stance\": \"partial\", \"note\": \"'Ai. raksati \\\"hütet, schirmt, bewahrt\\\"' — same coverage as Pokorny, i.e. the verb only, nothing on lac or the numeral.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. alek-\", \"stance\": \"contradicts\", \"note\": \"Watkins lists under alek- only Gk. alkē and alexein; no Indic reflex at all is given, and lac/lake/lacquer are not attached to this root — which is what Nourai's own NOTE ('AHD and OEW:333 derive these words from the root \\\"Reg: to dye\\\"') concedes.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 258, s.v. Lac (1)\", \"stance\": \"contradicts\", \"note\": \"Skeat: 'Skt. lākṣā, lac; put for rākṣā, lac. — Skt. [rakta], pp. of rañj, to dye, colour, redden; ... rāga, colour, paint. Der. gum-lac, shell-lac.' — the 'Reg: to dye' derivation.\"},\n            {\"src\": \"HJB\", \"where\": \"HJB.txt line 12862+, s.v. LAC\", \"stance\": \"contradicts\", \"note\": \"Yule-Burnell: 'LAC, s. Hind. lākh, from Skt. lakshā, for rākshā.' Same *rākṣā 'red dye' analysis.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt, entry no. 1295\", \"stance\": \"supports\", \"note\": \"Lokotsch: 'Sskr. lākṣā: \\\"Marke, Fleck; hunderttausend\\\", [und nach den 100000, d.h. unzähligen Insekten Cocca ilicis, welche durch ihren Stich auf quercus coccifera die harzige Absonderung bewirken] \\\"Lack\\\"' — i.e. Nourai's insect-swarm explanation verbatim.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt line 424 s.v. aleks-\", \"stance\": \"partial\", \"note\": \"Mann cites only Skt. rakṣāmi under this root; the numeral and the resin are absent.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. lac / lakh\", \"stance\": \"partial\", \"note\": \"'lac, lakh, n. [Hind. lakh; Sans. lākshā, a hundred thousand]' and 'lac, n. [Hind. lākh; Sans. lakshā] a resinous substance' — Webster keeps the two senses together but offers no PIE root.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"lak «لَک»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP لَک lak 'a hundred thousand (esp. of troops)' is a mercantile/military loan from Indo-Aryan: Skt. lakṣá- → Prakrit/Pali lakkha → Hindustani lākh, whence Persian lak with the regular shortening of the Indic long ā in a closed monosyllable and loss of the aspirate. It is a book-and-bazaar word of the Ghaznavid period onward, which is exactly the milieu of the ʿOnṣorī verse Nourai quotes (دو لک ز لشکر او شد به زیر خاک نهان, 'two lakhs of his army were hidden beneath the dust'), ʿOnṣorī being Maḥmūd of Ghazna's laureate and writing at the moment of the Indian campaigns. Mo'in's footnote in Borhan-e Qate' says the same thing. The one qualification: all sources route it through Hindustani rather than straight from Sanskrit as the chart's arrow does, and the attachment of Skt. lakṣa to *h₂lek- is the disputed step (node #8), not this one.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/लक्ष\",\n            \"https://abadis.ir/fatofa/لک/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:856\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 460 (= p.856): 'lac, lakh ... — Pers. lak, fr. Hind. lakh, ult. fr. OI. lākṣa, \\\"one hundred thousand\\\"'. Klein states the Persian form and the Indic source explicitly.\"},\n            {\"ref\": \"BQT:1900\", \"status\": \"supports\", \"note\": \"Read the page itself (tools/ref_page.py BQT:1900 → BQT_v3_picofile.pdf p.697; the running head prints ۱۹۰۰). Borhan: 'لك - بفتح اول و سکون ثانی، صد هزار باشد ... یعنی عدد هر چیز که صد هزار رسید آنرا لك خوانند' ('lak, first letter with fatḥa, second quiescent: it is a hundred thousand ... i.e. the count of anything that reaches a hundred thousand is called lak'). Mo'in's footnote 4 to it: 'هندی است «غیاث»؛ در هندوستانی لاک، از سانسکریت' ('it is Indian [Ghiyāth al-Lughāt]; in Hindustani lāk, from Sanskrit'). The same ʿOnṣorī couplet Nourai prints stands on that page: 'درآن نه سایر ماند و نه طایر از بر خاك / دو لك ز لشکر او شد بزیر خاك نهان — عنصری بلخی'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"BQT vol.3 printed p.1900 (pdf 697), s.v. لك + Mo'in fn. 4\", \"stance\": \"supports\", \"note\": \"See ref_check; Mo'in tags it Indian, via Hindustani lāk, from Sanskrit.\"},\n            {\"src\": \"MON\", \"where\": \"abadis.ir/fatofa/لک/ (فرهنگ معین + دهخدا)\", \"stance\": \"partial\", \"note\": \"Mo'in's lexicon entry for لک lists the homonyms (stain, fool, gait, the Lak tribe) without the numeral; the Dehkhoda section supplies 'لک در سانسکریت صدهزار' and connects the tribal name Lak to it.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt, grepped lak / lāk / Lack\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss registers no lak/lāk entry — expected, since he treats inherited Iranian vocabulary and excludes Indic loans.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt, grepped lak / Lack\", \"stance\": \"silent\", \"note\": \"Hübschmann likewise has nothing (the only 'Siegellack' hit, p. at line 2182, concerns Baluchi diǰay).\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 460, s.v. lac, lakh\", \"stance\": \"supports\", \"note\": \"'Pers. lak, fr. Hind. lakh'.\"},\n            {\"src\": \"HJB\", \"where\": \"HJB.txt s.v. LAC\", \"stance\": \"supports\", \"note\": \"'Though lāk bears the same sense in Persian ...' — Yule confirms the Persian form as an Indic word.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Arabic\",\n          \"words\": \"lajj\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Nourai's claim is that Arabic لَجّ lajj / لُجّ lujj 'a great multitude; the deep of the sea' is an arabization of Persian lak 'hundred thousand' — the sense bridge being 'a countless host'. His source really does say this, and so does Asbaghi's modern handbook, following him. But the mainstream analysis is native Semitic: لُجّ / لُجّة belongs to the well-formed geminate root ل-ج-ج, whose verb لَجَّ means 'to persist, be obstinate, clamour', with لَجَاج 'obstinacy' and لَجَّة 'the din of a crowd'; from 'din/tumult' come both 'a clamouring multitude' and 'the churning deep' (Qurʾān 27:44 صَرْحٌ مُمَرَّدٌ, and 24:40 بَحْرٍ لُجِّيٍّ 'a deep sea'), a Qurʾānic-era word with a full derivational family. A borrowing would also have to explain an unmotivated k > j, which Arabic does not do to Persian k (cf. lakk 'lac', borrowed with its k intact and standing three lines away in Addi Shir's own text). Verdict disputed: modern scholarship derives it from l-j-j, though Nourai's cited authority does support him.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/لج\",\n            \"https://abadis.ir/fatofa/لجه/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AFM:141\", \"status\": \"supports\", \"note\": \"AFM_pages.txt \\\\f-leaf 142, in باب اللام: '* (اللَج) الجماعة الكثيرة ومعظم الماء تعريب لك وهو الجيش البالغ عدده ... ويطلق على كل ما بلغ عدده مائة ألف' — 'al-lajj: the numerous company and the main body of water; arabized from [Persian] lak, which is an army whose number reaches ... and it is applied to anything whose number reaches a hundred thousand.' This is Nourai's claim verbatim, including both glosses. (Caveat on the page number: the OCR of Addi Shir's running heads is illegible, so leaf 142 could not be tied to the printed 141 with certainty; it is the correct entry and within the ل section either way. Note the neighbouring entry on leaf 143, '(اللك) صبغ ... تعريب لك', which is the resin word — Addi Shir keeps them apart.)\"},\n            {\"ref\": \"FVF:613\", \"status\": \"not_checked\", \"note\": \"Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi (Tehran 1347) — no local copy and no archive.org scan; the only digitisation (noorlib.ir/book/view/105056) is a browser-only page viewer that WebFetch cannot page through.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PLA\", \"where\": \"PLA_pages.txt leaf 254 ≈ Asbaghi 1988 p.240, s.v. laǧǧ\", \"stance\": \"supports\", \"note\": \"Asbaghi: 'laǧǧ: \\\"ungeheure Menge\\\" pers. لک lak \\\"tausend\\\"', with her footnote 3 'BQ. s. v., Addai Scher s. v.' — i.e. she repeats the claim on Borhan's and Addi Shir's authority rather than arguing it independently. Two entries later she has 'lakiyya: \\\"Lack ...\\\" hindustan >> pers. >> ar.', which is the separate resin word.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt, searched lujj / lajj\", \"stance\": \"silent\", \"note\": \"Klein has no Arabic lujj headword (he enters only Arabic words that reached English).\"},\n            {\"src\": \"TAD\", \"where\": \"TAD.txt (al-Unaysi, Tafsir al-alfaz al-dakhila)\", \"stance\": \"silent\", \"note\": \"No لجة / لج among the foreign-word headwords — al-Unaysi does not count it as a loan.\"},\n            {\"src\": \"ARB\", \"where\": \"ARB_mo3rb.txt / ARB_abdulraheem.txt (al-Jawaliqi, al-Muʿarrab)\", \"stance\": \"silent\", \"note\": \"The classical register of arabized words has no لج entry; the only hits are unrelated OCR noise.\"},\n            {\"src\": \"MON\", \"where\": \"abadis.ir/fatofa/لجه/ (دهخدا section)\", \"stance\": \"contradicts\", \"note\": \"Dehkhoda derives لجة from لجاج 'persistence/obstinacy', applied first to the vibration of sound in the throat and then to the ceaseless back-and-forth churning of deep water — a purely Arabic derivation.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Persian\",\n          \"words\": \"lojjeh «لُجّه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP لُجّه lojje 'the deep of the sea, the open sea' is a straightforward classical-Arabic loan: Ar. لُجَّة lujja (fem. of lujj, root ل-ج-ج), taken over with its gemination intact and the Arabic tāʾ marbūṭa rendered -e, one of the thousands of such nouns absorbed from the 9th c. onward and normal in literary Persian by Saʿdī's time — hence the Saʿdī couplet in Nourai's box (کشتی هرکه در این لُجّهٔ خونخوار افتاد). The borrowing Arabic → Persian is certain; what is not certain is the previous leg (node #10), so this is a genuine loan but not necessarily a Persian round-trip.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/لجه/\",\n            \"https://en.wiktionary.org/wiki/لج\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:3569\", \"status\": \"not_checked\", \"note\": \"The printed page 3569 of Mo'in's six-volume Farhang-e Farsi cannot be located: the only digitisation is the two-volume Adena abridgement, whose pagination differs and whose OCR (MON_part1/2.txt) is unreadable, and vajehyab/abadis give entry text without page numbers. The entry itself was read on abadis: 'لجه [ع.] میانهٔ دریا' — Mo'in tags it Arabic, which is what the arrow into this node asserts.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir/fatofa/لجه/ (فرهنگ معین)\", \"stance\": \"supports\", \"note\": \"'[ع.] (اِ.) میانهٔ دریا' — the [ع.] tag is Mo'in's mark for an Arabic-origin word; gloss 'midst of the sea' matches Nourai's 'the deepest point of sea'.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (Mo'in ed.), ل section\", \"stance\": \"silent\", \"note\": \"Borhan is a dictionary of Persian words and by design excludes plain Arabic loans such as لجه; no headword.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn excludes Arabic loanwords from the Grundriss; no entry.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Persian\",\n          \"words\": \"lâk «لاک»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP لاک lāk 'lac, the red resin used as a dye and varnish' is borrowed from Middle Indic: Skt. lākṣā́ → Prakrit lakkhā / Pali lākhā → Persian lāk (long ā kept, the geminate and the -ā ending dropped). It is a trade word, moving with the commodity itself — the resin is deposited by Kerria/Coccus lacca on Indian trees (konār/ziziphus, pipal, kusum) and Persia has no lac insect of its own, as Laufer stresses — so the word must be a borrowing, and it is attested in Persian from the Ghaznavid period (the ʿOnṣorī line in Nourai's box, خاک همرنگ لاک, 'the dust the colour of lac'). From Persian/Arabic it went on westwards (nodes 13-15). Note that this لاک is a homonym of the inherited لاک 'wooden trough, tortoise-shell' (< لاوک lāvak, Old Iranian *nāwaka- 'boat'), with which it has nothing to do.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/لاک\",\n            \"https://www.etymonline.com/word/shellac\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:856\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 460 (= p.856): 'lac, n., a red resinous substance. — Pers. lak, fr. Hind. lakh, fr. OI. lakṣa, lit. \\\"one hundred thousand\\\" ... a name given to the insects Cocca ilicis, in allusion to their great number.'\"},\n            {\"ref\": \"BQT:1878\", \"status\": \"supports\", \"note\": \"Read the page itself (tools/ref_page.py BQT:1878 → BQT_v3_picofile.pdf p.675; running head prints ۱۸۷۸). Borhan s.v. لاك: '...و نام رنگی است مشهور که در هندوستان بهم میرسد و بدان چیزها رنگ کنند و آن شبنمی باشد که بر شاخهای درخت کنار و درختهای دیگر نشیند و منجمد گردد' ('a famous dye that comes from India ... a dew that settles on the branches of the konār and other trees and congeals'). Mo'in's footnote 11: 'لك ... در یونانی λάκκα، فرانسوی laque، از هندی متوسط lākkhā گرفته شده. بعضی پنداشته‌اند در قرن اول و دوم میلادی به اروپا رسیده، ولی مانند کلمهٔ هندی فلفل پیشتر به یونان رسیده بود ... و رک: دزی «لك»؛ و رک: Hobson-Jobson' — 'taken from Middle Indic lākkhā', exactly the Indic → Persian arrow, with Mo'in also flagging the onward route to Greek/French.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"BQT vol.3 p.1878 (pdf 675) s.v. لاك + Mo'in fn. 11\", \"stance\": \"supports\", \"note\": \"See ref_check: 'از هندی متوسط lākkhā گرفته شده'.\"},\n            {\"src\": \"MON\", \"where\": \"Wiktionary's Persian لاک (which cites Hasandust/Mo'in-type material)\", \"stance\": \"supports\", \"note\": \"'Borrowed from Prakrit लक्खा (lakkhā, \\\"lac\\\"), from Sanskrit लाक्षा (lākṣā)' — and keeps it strictly apart from etymology 1, لاک 'trough, shell' < لاوک < *nāwaka-.\"},\n            {\"src\": \"SIN\", \"where\": \"SIN.txt, Laufer Sino-Iranica pp.475-477 ('Lac')\", \"stance\": \"partial\", \"note\": \"Laufer traces the Chinese lo-k'ia *lak-ka to 'Pali lakha (Sanskrit lakṣa, laktaka)' and warns 'The product itself is not one of Persia, where the lac-insect is unknown' — confirming that Persian lāk can only be a borrowed trade word, not a native one.\"},\n            {\"src\": \"HJB\", \"where\": \"HJB.txt s.v. LAC\", \"stance\": \"supports\", \"note\": \"'Though lāk bears the same sense in Persian, and lak or lukk are used in modern Arabic for sealing-wax ...'\"},\n            {\"src\": \"AFM\", \"where\": \"AFM_pages.txt leaf 143\", \"stance\": \"supports\", \"note\": \"Addi Shir has the resin word separately: '(اللك) صبغ ... يصبغ به جلود المعزى تعريب لك' — 'al-lakk, a dye with which goatskins are dyed, arabized from [Persian] lak', i.e. Persian lāk/lak was the source of the Arabic form.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt / HUB.txt\", \"stance\": \"silent\", \"note\": \"Neither Horn nor Hübschmann has a lāk entry; Indic loans are outside their scope.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Portuguese\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The empty box stands for Port. laca 'gum lac' and its unexplained variant lacre 'sealing-wax'. Two routes converge on it: the old Mediterranean one — Pers./Ar. lakk → Medieval Latin lacca (already in the medical writers) → Port. laca/It. lacca/Sp. laca — and the direct one, Portuguese traders re-importing the word with the commodity from Gujarat, Malabar and Pegu after 1498 (Garcia da Orta's Colóquios of 1563 discusses lacre at length, and it is the Portuguese who put the word into 16th-c. European commerce). Nourai's single arrow Persian → Portuguese is therefore a simplification: Arabic lakk and/or Medieval Latin lacca stand between, and part of the 16th-c. vocabulary came straight from Indo-Aryan. Hence plausible rather than confirmed. The origin of the -re of lacre is, as Laufer says flatly, unexplained.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/lacquer\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"The Portuguese box in the book carries no citation icon and no refs= in the JSON, so there is no reference of Nourai's to verify for this link.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 461, s.v. lacquer\", \"stance\": \"partial\", \"note\": \"'MF. lacre, fr. Port. lacre, \\\"sealing wax\\\", fr. laca, \\\"gum lac\\\", which derives fr. Hind. lakh, \\\"lac\\\", fr. OI. lakṣā' — Klein routes Portuguese from Hindi, bypassing Persian.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt entry no. 1295\", \"stance\": \"partial\", \"note\": \"Lokotsch: 'hieraus ... sp. pg. laca \\\"Lack\\\", lacre \\\"Siegellack\\\", frz. laque \\\"Lack\\\", it. lacca' — all derived directly from Skt. lākṣā via Hindi lākh, with no Persian stage.\"},\n            {\"src\": \"DEV\", \"where\": \"DEV.txt lines 1622-1629, s.v. Laque\", \"stance\": \"supports\", \"note\": \"Devic: 'C'est un mot d'origine indienne, qui nous est venu par l'arabe-persan لك lakk ou لاك lāk ... dans ce dernier sens on dit en espagnol et en portugais lacre' — Devic does put the Arabo-Persian form in the chain, as Nourai does.\"},\n            {\"src\": \"SIN\", \"where\": \"SIN.txt p.477 n.6\", \"stance\": \"partial\", \"note\": \"Laufer: 'The Portuguese word for \\\"lac, lacquer\\\", the latter being traceable to lacre. The ending -re is unexplained.'\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The empty box is Middle/obsolete French lacre 'sealing-wax' (in Cotgrave's dictionary of 1611), taken from Portuguese lacre in the 16th c. as the Portuguese carried the East-Indian trade into northern Europe; beside it stands the older French laque 'lac, lake pigment' (from Med. Lat. lacca / Italian lacca). It is lacre, not laque, that gives English lacquer, which is why the chain has to pass through French here.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/lacquer\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"No refs= on this node in the book; nothing of Nourai's to check.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 461 s.v. lacquer\", \"stance\": \"supports\", \"note\": \"'MF. lacre, fr. Port. lacre, \\\"sealing wax\\\"' — the Portuguese → French arrow exactly.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 258, s.v. Lacquer/lacker\", \"stance\": \"supports\", \"note\": \"'lacquer, lacker, a sort of varnish. (F.-Pers.-Skt.) F. lacre (Cot.) — Port. lacre, sealing-wax. — Port. laca, gum-lac' — the same chain, and Skeat's language tag '(F.-Pers.-Skt.)' even inserts the Persian stage Nourai draws.\"},\n            {\"src\": \"DEV\", \"where\": \"DEV.txt s.v. Laque\", \"stance\": \"supports\", \"note\": \"Devic treats French laque/lacre as an Indian word arriving through Arabo-Persian; 'L'italien lacca signifie à la fois laque et cire à cacheter; dans ce dernier sens on dit en espagnol et en portugais lacre.'\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt no. 1295\", \"stance\": \"supports\", \"note\": \"'frz. laque \\\"Lack\\\"' listed among the Romance reflexes.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"English\",\n          \"words\": \"lacquer; Shellac\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"lacquer: first attested 1570s as 'dye obtained from lac', then 1670s as the shellac varnish; from obsolete French lacre (Cotgrave) < Port. lacre < laca, ultimately the Indic word — the -qu- spelling is an 18th-c. re-Frenchification of earlier lacker. shellac (1713) is not a borrowing at all but an English compound shell + lac, a loan-translation of French laque en écailles 'lac in [thin] plates', naming the third stage of processing (stick-lac on the twig → seed-lac washed → shell-lac melted and cast in flakes). Both words thus sit correctly at the end of Nourai's chain; only the Sanskrit end of it (node #8) is contested.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/lacquer\",\n            \"https://www.etymonline.com/word/shellac\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SKT:281\", \"status\": \"partial\", \"note\": \"Skeat's Lac/Lacquer entries were located in SKT.txt at \\\\f-leaves 258-259 (running head LABURNUM): 'Lacquer, lacker, a sort of varnish. (F.-Pers.-Skt.) F. lacre (Cot.) — Port. lacre, sealing-wax. — Port. laca, gum-lac' and 'Lac (1), a resinous substance. (Pers.-Skt.) Pers. lāk, lak, gum-lac, whence the lake is obtained for dyeing. — Skt. lākṣā, lac; put for rākṣā, lac. — Skt. [rakta], pp. of rañj, to dye, colour, redden ... Der. gum-lac, shell-lac.' So Skeat fully supports the Persian → Portuguese → French → English chain that Nourai cites him for, but he contradicts the root: he takes Skt. lākṣā to rañj/raj 'to dye', i.e. Nourai's alternative 'Reg' root, not Alek. (Page caveat: the file's stated offset leaf = printed + 20 would make these leaves p.238-239, not the cited 281 — but the SKT.txt leaf order is demonstrably scrambled in places (leaf 300 is under M, leaf 301 under D), so the offset cannot be trusted here; the entries are unambiguous.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaves 460-461 and 34948 (shellac)\", \"stance\": \"supports\", \"note\": \"'shellac, n. and tr. v. — A compound of shell and lac, \\\"a red resinous substance\\\"; loan translation of F. laque en écailles, lit. \\\"lac in plates\\\".'\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaves 258-259\", \"stance\": \"partial\", \"note\": \"See ref_check: supports the chain, contradicts the root.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. lac\", \"stance\": \"supports\", \"note\": \"Webster describes the same three commercial grades: 'While still attached to twigs and dried, it is called stick-lac; when dissolved out ... seed-lac, and when strained through a cloth and dried it constitutes shell-lac, or the shellac of commerce.'\"},\n            {\"src\": \"FSD\", \"where\": \"FSD_vol2.txt s.v. lakh\", \"stance\": \"supports\", \"note\": \"Funk & Wagnalls: 'lakh, n. [Anglo-Ind.] 1. The sum of 100,000 ... The word was used originally to express 100,000 objects of any kind, as spears or lanterns' — the numeral sense in English, the sibling of lac.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt no. 1295\", \"stance\": \"supports\", \"note\": \"'engl. lac, ndl. lak, dtsch. Lack und engl. shellac [eigentlich \\\"Schalenlack\\\", da er zu kleinen, dünnen Täfelchen geformt wird]'.\"},\n            {\"src\": \"HJB\", \"where\": \"HJB.txt s.v. LAC\", \"stance\": \"supports\", \"note\": \"'the melted clarified substance, after the extraction of the dye, is turned out in thin irregular laminae called shell-lac ... So also are lacquer and lackered ware, because lac is used in some of the varnishes with which such ware is prepared.'\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-04T19:47:17.220Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-49.json (file state is current in your context — no need to Read it back)
```


## [2026-09-04T19:47:22.026Z] TOOL CALL #59: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-49.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 49"
}
```


### [2026-09-04T19:47:24.620Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'confirmed': 12, 'disputed': 2, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 9, 'partial': 3, 'not_checked': 9}
books consulted: {'supports': 29, 'silent': 19, 'partial': 10, 'contradicts': 4} | by book: {'KLN': 10, 'MON': 6, 'BQT': 5, 'SKT': 4, 'HJB': 4, 'LKT': 4, 'DEV': 3, 'WEB': 3, 'HRN': 3, 'POK': 2, 'WLD': 2, 'AHD': 2, 'IEC': 2, 'AFM': 2, 'SIN': 2, 'FVQ': 1, 'LEW': 1, 'LAT': 1, 'HUB': 1, 'PLA': 1, 'TAD': 1, 'ARB': 1, 'FSD': 1}
```


## [2026-09-04T19:47:43.465Z] AGENT

Page 49 (book p. 19) verified — `data/verification/page-49.json` written, `verify_check.py 49` clean (15/15 nodes, no PROBLEM lines).

**Counts:** root verdicts: 1 confirmed. Node verdicts: 12 confirmed, 2 disputed, 1 plausible. Ref checks: 9 supports, 3 partial, 9 not_checked. 23 books consulted (29 supports / 10 partial / 4 contradicts / 19 silent).

**Disputed / flagged:**
- **#8 Sanskrit `lâkšâ, rakšâ; lâk, râk`** — Pokorny p. 32 (the cited page, read directly) contains *only* the verb `rákṣati`; neither `lakṣa` "100,000" nor `lākṣā` "lac" appears there. Mayrhofer, Skeat ("lakṣā, put for rākṣā, from rañj to dye"), Hobson-Jobson and Wiktionary derive the resin word from *raj-* "to redden" (Nourai's own alternative "Reg: to dye" root); Klein and Wiktionary's `lakṣa` entry keep the numeral with \*h₂lek-. Also, "lâk, râk" are not Sanskrit forms at all — they are Middle Indic (Prakrit *lakkhā* → Hindi *lākh*).
- **#10 Arabic `lajj`** — mainstream view is a native Semitic geminate root ل-ج-ج (لَجَّ "persist, clamour" → لَجَّة "din of a crowd" → "churning deep"; Qurʾānic بحر لجّي), and k > j is unmotivated. Nourai's cited source does back him: Addi Shir (AFM leaf 142) says "اللَج ... تعريب لك", and Asbaghi (PLA ~p. 240) repeats it citing Borhan and Addi Shir.
- **#13 Portuguese (plausible)** — Klein and Lokotsch route Port. *laca/lacre* from Hindi *lākh* (or Med. Lat. *lacca*), not from Persian; Devic does keep the Arabo-Persian stage. Simplified arrow rather than an error.

**Reference pages read directly:** POK:32 ✔, AHD:1506 ✔, KLN:47 ✔, KLN:856 ✔, AFM:141 ✔ (leaf located; printed numeral illegible in OCR), BQT:1878 ✔ and BQT:1900 ✔ (rendered via `tools/ref_page.py`, running heads confirm the page numbers; Mo'in's footnotes quoted, and the ʿOnṣorī couplet Nourai prints is on p. 1900). SKT:281 → content found but the file's leaf offset maps it to ~p. 238 and the SKT.txt leaf order is scrambled, so the page number could not be confirmed. Not checkable: all four MON citations (vols 5–6 a'lam are not digitised; the 2-vol Adena OCR is unusable) and FVF:613 (noorlib browser-only). 12 web pages archived via `fetch_source.py`.
