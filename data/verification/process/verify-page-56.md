# Verification process log — verify-page-56


## [2026-09-04T22:40:28.490Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 56 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-56.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-56.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-56.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 56` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T22:40:29.929Z] AGENT

I'll start by reading the instructions.


## [2026-09-04T22:40:32.265Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T22:40:32.281Z] TOOL RESULT

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


## [2026-09-04T22:40:32.747Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-56.txt"
}
```


### [2026-09-04T22:40:32.764Z] TOOL RESULT

```
1	=== PDF page 56 (book page 26) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ang, Ank, Anq : to bend  (refs POK:46)
4	#1 (parent #0) [Avestan] refs=KLN:75 | angušta : toe, finger
5	  #2 (parent #1) [Persian] refs=MON:392 | angošt «انگشت» : finger, toe | extra: انگشتر ، انگ ١ ، انگلک ، انگولک
6	  #3 (parent #1) [Sogdian] refs=SOD:41 | ʿngwšt : finger
7	#4 (parent #0) [Avestan] refs=POK:45; BRT:755 | anku, aka : hook ; duž-aka : with bad sting hooks, porcupine ☞Dus | NOTE: BRT:755 is not quite certain about "duž-aka" etymology.
8	  #5 (parent #4) [Pahlavi] refs=SNS:168; BQT:1063 | žužag, zuzag, jujag : porcupine
9	    #6 (parent #5) [Persian] refs=BRT:755; BQT:1063 | žŭž «ژوژ» : porcupine | extra: ژوژه
10	#7 (parent #0) [Sogdian] refs=SOD:32 | ʿkšye : hook
11	#8 (parent #0) [Greek] refs=AHD | ankura : anchor
12	  #9 (parent #8) [Persian] refs=BQT:1908 | langar «لنگر» : anchor
13	  #10 (parent #8) [English] refs=AHD | anchor
14	#11 (parent #0) [Sanskrit] refs=POK:46; BQT:1254 | angam : member, part ; catur-anga : the four parts (castle, Knight, Bishop and Pawn) in the game of chess. ☞Kwetwer
15	  #12 (parent #11) [Pahlavi] refs=None | catrang
16	    #13 (parent #12) [Persian] refs=BQT:1254; FVF:404 | šatrang «شترنگ» : chess | extra: کترنگ ، شطرنج
17	#14 (parent #0) [Sanskrit] refs=AHD:943; OEW:14 | ancati : he bends ; pari-ancati : he bends around, PER 1 ; pary-anka, palyanka : a bed carried on poles on the shoulder of two or four men. This name is due to the sagging cloth bottom.
18	  #15 (parent #14) [English] refs=AHD; OEW:14 | palanquin, palankee
19	#16 (parent #0) [Latin] refs=AHD; KLN | angulus : angle, corner
20	  #17 (parent #16) [English] refs=None | angle, rectangle, triangle
21	#18 (parent #0) [Germanic] refs=AHD; OEW:14 | Angul : an angle-shaped land in Schleswig, W. Germany near Denmark.
22	  #19 (parent #18) [Old English] refs=KLN:522; AWH1:129 | Engle, Angle : people of "Angul" who landed in Britain (Engle-Land) around 450 AD
23	    #20 (parent #19) [French] refs=None | angle-
24	      #21 (parent #20) [Persian] refs=MON | Engelîs «انگلیس» | extra: انگلیسی ، انگلستان
25	    #22 (parent #19) [English] refs=None | English, England, Anglo-, Anglo-Saxon
26	
```


## [2026-09-04T22:40:36.199Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-56.json | head -200",
 "description": "Read source JSON for page 56"
}
```


### [2026-09-04T22:40:36.247Z] TOOL RESULT

```
{
  "pdf_page": 56,
  "book_page": 26,
  "entries": [
    {
      "root": {
        "name": "Ang, Ank, Anq",
        "lang": "Indo-European",
        "refs": "POK:46",
        "gloss": "to bend"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KLN:75",
          "words": [
            {"translit": "angušta", "gloss": "toe, finger", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:392",
          "words": [
            {"translit": "angošt", "gloss": "finger, toe", "script": "انگشت"}
          ],
          "script_extra": "انگشتر ، انگ ١ ، انگلک ، انگولک",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:41",
          "words": [
            {"translit": "ʿngwšt", "gloss": "finger", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:45; BRT:755",
          "words": [
            {"translit": "anku, aka", "gloss": "hook", "script": null},
            {"translit": "duž-aka", "gloss": "with bad sting hooks, porcupine", "script": null, "see": ["Dus"]}
          ],
          "note": "BRT:755 is not quite certain about \"duž-aka\" etymology.",
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Pahlavi",
          "refs": "SNS:168; BQT:1063",
          "words": [
            {"translit": "žužag, zuzag, jujag", "gloss": "porcupine", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BRT:755; BQT:1063",
          "words": [
            {"translit": "žŭž", "gloss": "porcupine", "script": "ژوژ"}
          ],
          "script_extra": "ژوژه",
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:32",
          "words": [
            {"translit": "ʿkšye", "gloss": "hook", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "ankura", "gloss": "anchor", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "BQT:1908",
          "words": [
            {"translit": "langar", "gloss": "anchor", "script": "لنگر"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "anchor", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:46; BQT:1254",
          "words": [
            {"translit": "angam", "gloss": "member, part", "script": null},
            {"translit": "catur-anga", "gloss": "the four parts (castle, Knight, Bishop and Pawn) in the game of chess.", "script": null, "see": ["Kwetwer"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "catrang", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "BQT:1254; FVF:404",
          "words": [
            {"translit": "šatrang", "gloss": "chess", "script": "شترنگ"}
          ],
          "script_extra": "کترنگ ، شطرنج",
          "note": null,
          "quote": {"text": "تا جز از بیست و چهارش نبود خانهٔ نرد - همچو دو سی و دو خانست نهادش شترنگ", "poet": "Najjâr"}
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "AHD:943; OEW:14",
          "words": [
            {"translit": "ancati", "gloss": "he bends", "script": null},
            {"translit": "pari-ancati", "gloss": "he bends around, PER 1", "script": null},
            {"translit": "pary-anka, palyanka", "gloss": "a bed carried on poles on the shoulder of two or four men. This name is due to the sagging cloth bottom.", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": "AHD; OEW:14",
          "words": [
            {"translit": "palanquin, palankee", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "angulus", "gloss": "angle, corner", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "English",
          "refs": null,
```


## [2026-09-04T22:40:38.057Z] TOOL CALL #4: Bash

```json
{
 "command": "cat \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md\"",
 "description": "Read source matrix"
}
```


### [2026-09-04T22:40:38.097Z] TOOL RESULT

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


## [2026-09-04T22:40:42.208Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-56.json'))\nprint(json.dumps(d['entries'][0]['nodes'][16:], ensure_ascii=False, indent=1))\nprint('num entries', len(d['entries']))\nprint('num nodes', len(d['entries'][0]['nodes']))\n\""
}
```


### [2026-09-04T22:40:44.275Z] TOOL RESULT

```
[
 {
  "id": 17,
  "parent": 16,
  "lang": "English",
  "refs": null,
  "words": [
   {
    "translit": "angle, rectangle, triangle",
    "gloss": null,
    "script": null
   }
  ],
  "note": null,
  "quote": null
 },
 {
  "id": 18,
  "parent": 0,
  "lang": "Germanic",
  "refs": "AHD; OEW:14",
  "words": [
   {
    "translit": "Angul",
    "gloss": "an angle-shaped land in Schleswig, W. Germany near Denmark.",
    "script": null
   }
  ],
  "note": null,
  "quote": null
 },
 {
  "id": 19,
  "parent": 18,
  "lang": "Old English",
  "refs": "KLN:522; AWH1:129",
  "words": [
   {
    "translit": "Engle, Angle",
    "gloss": "people of \"Angul\" who landed in Britain (Engle-Land) around 450 AD",
    "script": null
   }
  ],
  "note": null,
  "quote": null
 },
 {
  "id": 20,
  "parent": 19,
  "lang": "French",
  "refs": null,
  "words": [
   {
    "translit": "angle-",
    "gloss": null,
    "script": null
   }
  ],
  "note": null,
  "quote": null
 },
 {
  "id": 21,
  "parent": 20,
  "lang": "Persian",
  "refs": "MON",
  "words": [
   {
    "translit": "Engelîs",
    "gloss": null,
    "script": "انگلیس"
   }
  ],
  "script_extra": "انگلیسی ، انگلستان",
  "note": null,
  "quote": null
 },
 {
  "id": 22,
  "parent": 19,
  "lang": "English",
  "refs": null,
  "words": [
   {
    "translit": "English, England, Anglo-, Anglo-Saxon",
    "gloss": null,
    "script": null
   }
  ],
  "note": null,
  "quote": null
 }
]
num entries 1
num nodes 22
```


## [2026-09-04T22:40:45.515Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','KLN','MON','SOD','BRT','SNS','BQT','AHD','FVF','OEW','AWH1','FVQ','PHD','HRN','HUB','LKT','SKT','HJB','AID','IEC','SYN','WLD','LEW','LAT','FSD','WEB','NYB','ARY','CHEUNG']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-04T22:40:48.166Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabeti
OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC n
AWH1 null
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_f
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnair
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG null
```


## [2026-09-04T22:41:14.195Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== bibliography AWH OEW FVF SNS ===\"\ngrep -n -i -E '^(AWH|OEW|FVF|SNS|SOD|BQT|MON|FVQ)' \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt\" | head -30\necho \"=== grep AWH in bib ===\"\ngrep -n -i 'AWH' \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt\" | head"
}
```


### [2026-09-04T22:41:14.275Z] TOOL RESULT

```
=== bibliography AWH OEW FVF SNS ===
=== grep AWH in bib ===
3: TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
6: TABLE IV - Reference Abbreviations 1 AEF 2 AFA 3 AFM 4 AHD 5 AHM 6 AID 7 AIN 8 AKD 9 AKM 0 AMD i ARB 2 ARK 3 ARM 4 ARP 5 AVG 6 AWH Jalal KhaleqT Motlaq, Asas Eshteqaq Farsi, ^j1* JISsAl o"1-'' Vol. I (a - kh), Bonyad Farhang Iran, 1977. Siegmund Fraenkel, Die Aramaischen Fremdworter im Arabischen, Hildesheim, 1962. Addi Shir, Al-Alfaz Al-Farsiyya Al-Mu'arraba, (A Dictionary of Persian Words in the Arabic Language), Library of Lebanon, 1980.. W. Morris, The American Heritage Dictionary, New College Edition, 1975, Appendix on Indo-European Roots, pp 1505-1550. I. Gershevitch, The Avestan Hymn to Mithra, Oriental Publications No.4, Cambridge University Press, 1959. G. C. Withworth, Anglo-Indian Dictionary. Kegan Paul, Trench &amp; Co, London 1885. E. Liden, Studien zur Altindischen und Vergleichenden Sprachgeschichte , Almqvist &amp; Wiksells, Upsala 1897. H. Zimmem, Akkadische Fremdworter Als Beweis Fur Babylonischen Kultureinfluss, Leipzig 1917. Amir J. ATam, Farhang A'alam Ketab Moqaddas or, A Dictionary of Proper Names in the Bible, English - Persian, Iran University Press, Tehran 1988. H. A" mid, Farhang Farsi Amid, Two volumes, Amir Kabir Press, Tehran, 1369 (1990). Jawaliqi, Al-Mu'arrab, Tehran 1966. M. H. Rokn Zadeh - Adammiyat, Arkan Sokhan, Sharq Press, Tehran 1347 (1968). ^W-\A£ h_)UT joMc' OwJbjd -W*c ^— *&gt;jl^ OwJfcjd £^~&gt; O^j' A. Aryan, ks~'j'* lSj^ ^)~&gt;^ ^*j' -ujUa ^la o^lj oiajs Farhang Vajheh-hay Hamanand, Armani - AvestaT, Pahlavi, FarsT, Vol. I (a), Bonyad Nayshabflr, Tehran 1363 (1984). F. Spiegel, Die Arische Periode und ihre Zustande, Leipzig ,1887. A. V. W. Jackson, An Avesta Grammer, W. Kohl Hammer, Stuttgart 1892. H. Kinder &amp; W. Hilgemann, Atlas of World History. 2 vol., Anchor Books, 1974. A-9
```


## [2026-09-04T22:41:14.745Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK ank- ===\"\ngrep -n -E 'a[nṇ]k-, a[nṇ]g-|ank-, ang-' POK_full.txt | head -20"
}
```


### [2026-09-04T22:41:14.795Z] TOOL RESULT

```
=== POK ank- ===
```


## [2026-09-04T22:41:20.636Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la POK*.txt\necho \"=== search 'biegen' near ank ===\"\ngrep -n \"ank-\" POK_01.txt | head -30"
}
```


### [2026-09-04T22:41:20.690Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
=== search 'biegen' near ank ===
616:air.  ecen  (ec-  aus  *ank-  oder  *n^c-),  mcymr.  anghen^  cymr.  angen,  corn. bret.  anken  ,Not,  Notwendigkeit^,  im  Ir.  auch  ,Gewalttat^
619:2.  ank-,  ang-  , biegen^;  Nominalstämme  anko-,  onko-;  ankes-;  anku-lo-; anken-,  -on-;  ankoto- ;  ankro-.
1584:germ.  *bank-  in  aschwed.  banka,  abl.  bunka  ,schlagen,  klopfen^,  obd. hunken  ,klopfen,  stoßen^,  mnd.  bunken,  ndl.  bonken  ,schlagen,  prügeln'.
1749:ihd.  hlecchen  (*blakjan)j  mhd.  blecken  ^sichtbar  werden^  sehen  lassen', nhd.  blecken  ,die  Zähne  zeigen';  ahd.  blecchazzeUj  mhd.  blecken  , blitzen^, mßdl.  nndl.  blaken  , flammen,  glühen',  ags.  blmcern,  blacern  , Leuchter', aisl.  blakra  , blinken';  hierher  wohl  als  ,angeb rannt  (vgl.  nd.  blaken  von rußender  Lampenflamme),  angerußt',  ags.  bloec  ,schwarz',  n.  , Tinte',  ahd. llah  ds.;  nasaliertes  germ.  *blenk-,  *blank-  in  mhd.  nhd.  blinken^  mhd. blinzen  (*blinkatjan),  nhd.  blinzeln  (daneben  mit  germ.  g  älter  dän.  blinge blinken'  u.  dgl.,  s.  Falk-Torp  u.  blingse);  ahd.  blanch,  mhd.  blank  ,blin- kend  glänzend,  weiß',  nhd.  blank,  ags.  blanca  m.  ,Roß'  (eig.  von  heller Farbe,  vgl.:)  aisL  blakkr  ,fahl',  poet.  ,Roß'  (,Falbe,  Schimmel'),  aschwed. hlakker  ,fahl,  falb',  aber  auch  , schwarz,  dunkel' (aus  dem  Germ,  entlehnt frz.  blanCj  ital.  bianco).     Von    dieser  Nasalform  auch  pr.  blingis  , Bleibe';
2134:(:  aisl.  bod)j  air.  buide  , Zufriedenheit,   Dank-;   hierher  auch  air.   ad-bond-
4771:fern  bleibt  wohl  phryg.  vi  ,und'  (in  loq  vi  ,und  wer');  über  toch.  A .ne  in  hus-ne  ,welcher',  vgl.  Couvreur  (Tochaarse  Klank-  en  Vormleer  50) ; 5  auch  Schwyzer  Gr.  Gr.  I  612;
```


## [2026-09-04T22:41:22.725Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f in ['POK_full.txt','POK_01.txt']:\n    try:\n        t=open(f,encoding='utf-8',errors='replace').read()\n    except Exception as e:\n        print(f,e); continue\n    print('==',f,len(t))\n    for m in re.finditer(r'a[nṇńŋ][kg]-', t[:400000]):\n        print(f, m.start(), repr(t[max(0,m.start()-120):m.start()+160]))\n        break\nEOF"
}
```


### [2026-09-04T22:41:25.869Z] TOOL RESULT

```
== POK_full.txt 3967710
POK_full.txt 81957 '; Old English n- \na, engl. /7o\' not, no \'; \n\nMaybe alb. (*d)yb"not, no\' (common alb. -slav. j- prefix. \n\nOld Icelandic lang-ger = \\-aWv\\ longaevus^ of great age, aged, ancient \'; /-stem also in Old \nIcelandic 3efi, ^i//f. {*aiui-) " life, age \'; a-stem in Old High German ewai. " '
== POK_01.txt 966268
POK_01.txt 21468 "ch  .im  Anfang zuerst',  agrimd-  .der  erste',  av.  ayra-  .der  erste,  oberste  nach  Zeit   Raum\nusw/;  1).  ; Anfang-;  das  oberste^  Spitze^;  lett.  agrs  (Adj.)  ^frühe^;  agri  Adv. früh;  frühzeitig-;  agrums  ^die  Frühe^\nOb  hierher  der  lat.  MN  Ägrlppa  aus  '^"
```


## [2026-09-04T22:41:30.475Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '600,700p' POK_01.txt"
}
```


### [2026-09-04T22:41:30.528Z] TOOL RESULT

```
Lat.  anguis  =  lit.  angis  (f.),  apr.  angis  ,Schlange^  (lett.  üodze  f.  ,Schlange*), aksl.  *gzh,  russ.  uz,  poln.  wqz  ,Schlange'^,  ai-m.  auj  (Gen.  -i)  , Schlange* (Meillet  Esquisse  154,  Dumezil  BSL.  39,  100);  mir.  esc-ung  ,Aal'  (*,Wasäer- schlange',  esc  , Wasser^  +  *ang'":ho),  cymr.  llys-yic-en,  PL  -yio-od  ds.  (Fick II  ^  15;  zum  brit.  Schwunde  von  i^g  vor  m  siehe  Pedersen  KG.  I  107).
44
Dazu  mit  Schwundstufe  und  unaspirierter  Media  (letztere  konnte  an  sich.« auch  im  Lat.  und  Balt.-Slav.  vorliegen)  ahd.  unc  ^Schlange,  Natter^  gr.j (illjr.)  ^ßsLQ'  sxeig  Hes.  (*ng^i-).
Diesen  Formen  mit  Media  zunächst  steht  Yußrjoig'  eVx^^t'g,  Msd-vixvaToil Hes.  (^eng^r^rl- :  zum  i  vgl.  Solmsen  ßeitr.  I  215),  woran  wegen  des  7'-Suffixes  i anzuschließen  sind  balto-slav.  *anguria-  in  slav.  *0(/orb  m.  russ.  i(g(o)n,] poln.  icegorz,  cech.  illiovy  serb.  ügor,  sloven.  ogor  ,Aal',  lit.  ungurys  ds.  (assim. ' aus  *angurijs,  vgl.  finn.  ankerlas),  apr.  angurgis  ,kdX'  (ksl.  (igulja,  jegidja^ ^AaF  wohl  aus  dem  Lat.).  Hirt  IF.  22,  67  verbindet  diese  gr.  und  balt.-^ slav.  Aalnamen  zu  einer  selbständigen  Gleichung  (doch  vgl.  das  ?"-Suffix  r von  ahd.  angar  usw.,  s.  unten).  j
Eine  andere  idg.  Gleichung  für  ^Aal'  ist  vielleicht  gr.  eyxekvg  i.,  lat.  5 anguilla  (s.  bes.  W.  Meyer  KZ.  28,  163,  Johansson  KZ.  30,  425,  J.  Schmidt KZ.  32,  369,  Osthoff  IF.  4,  270,  29j^,  Hirt  IF.  22,  67,  Idg.  619  f.),  wenn- gleich die  Einzelheiten  noch  unklar  sind  (im  Gr.  *äyxeXvog  usw.  zu  iyxs^vog  ' assimiliert,  oder  das  s  und  der  i-eine  Gutt.  durch  Einfluß  von  .e'xig]  im  ^ Lat.  -üla  statt  -ella  nach  dem  Schwanken  in  echten  Deminutiven  unter  1 entscheidendem  Einfluß  des  i  von  anguis7).
In   der  Bed.  ,Wurm,  Made^  und   mit  r-Suffix   (vgl.  oben  üfißr^gig  usw.):; ahd.    angar    ,Kornmade^    eugirinc    ,Larve^,    nhd.    Engerling,   lit.    anksfirai ,Maden,  Engerlinge'  (und  ähnliche  Formen,  s.  Trautmann  Apr.  301),  lett.  ; anksteri   ,Maden,   Engerlinge",   apr.    anxdris   (d.   i.    anxtris)    aber   ,Natter^ (über  das  -st-  dieser  halt.  Formen  vgl.  Mühlenbach-Endzelin  Lett.-D.  Wb.  I  ; 71),  russ.  ug{o)rh  , Hitzblatter,    Finne^    (auch    ,AaP,    s.  oben),   poln.    icagry ,Schweinsfinnen'  (Bezzenberger  GGA.  1874,  1236,  BB.  2,  154;  nicht  besser über  angar,  ugorh  ders.   GGA.  1898,  554 f.).  i
Nasallose  Formen: .    Gr.  exig  m.  (f.)  .Schlange',  Mx^^va   ds.  (für  *ey^idvLa,  Specht  Dekl.  377), ahd.  egala  ,Egel^,  dän.  norw.  igle  ,ein   schmarotzender  Blattwurm   in  den Eingeweiden  der  Tiere  und  in  der  Haut  und  den  Kiemen  der  Fischet
Hierzu  gr.  sxivog,  ahd.  ags.  igll  (idg.  '^eghinos),  nhd.  Igel,  eigentl. ,Schlangenfresser^,  W.  Schulze  Gnomon  11,  407,  lit.  ezys,   ksl.  jeh  Jgel*.
Arm.  iz  ,Schlange,  Viper^  kann  als  *6g'^hls  zu  h'q)ig  gestellt  werden (Meillet  Esquisse  75);
gr.  ocfLg  ,Schlange^  (^og^his):  cymr.  euod  (*og'^h-)  ,Schafwürmer:  ai.aÄi-, av.  azi-  ,Schlange^
Unsicher  ist  Anreihung  von  as.  egithassa,  mnd.  egidesse,  ags.  (verderbt) äpexe,  ahd.  egidehsa,  nhd.  Eidechse  mit  ewi-,  egi-,  idg.  *og]'hl-  =  Ucpig (Zupitza  Gutt.  99  nach  Kluge;  Falk-Torp  u.  0(jle)  +  germ.  ^pahsiö,  ahd. "^dehsa  ,Spindel'.
45
Ol)    in  diese  Mannig-faltig-keit  so  Ordnung  zu  bring-en  sei^  daß  *a7dg]iJä- nd  *eghi-,  '^ogld-   (gh)  eine  Kreuzungsform   *eglihi-^  '^o(ßhl-  liervorgerufeii 1  ••Uten    bleibe  dahingestellt.  Wahrscheinlich  haben   dabei   aucli  Tabu-Vor- stellungen mitgewirkt.
AVP.  I  63 ff.,  WH.  I  48,  Specht  KZ.  64,  13:  ^:>^^,  56  f.,  Ilavers  Sprach- tnbn  44  f.
/.  ank'  ,Zwang,  Notwendigkeit^
Gr.  dvdyyiT]  ,Not wendigkeit,  Zwangt  (gewöhnlich  als  i-edupliziert  ange- sehen),  ion.   ävayxair]   ds.    (von  dvayy.aTog  ,notwendig^,  dvayÄaCcx)  ,zwinge');
air.  ecen  (ec-  aus  *ank-  oder  *n^c-),  mcymr.  anghen^  cymr.  angen,  corn. bret.  anken  ,Not,  Notwendigkeit^,  im  Ir.  auch  ,Gewalttat^
Obwohl  , Zwangt  aus  ,feiudlicher  Bedrängnis,  Verfolgung^  verständlich wäre,  macht  die  gr.-kelt.  Bed. -Übereinstimmung  es  doch  fraglich,  ob  das lautlich  übereinstimmende  ahd.  ähta  ,feindliche  Verfolgung^,  nhd.  Achty ags.  öht  (urgerm.  *anxto),  germ.  EN  Äctumerus  (d.  i.  AytuweraZy  1.  Jh. n.  Chr.;  Brugmann  Grdr.  P  382),  womit  ir.  echt  (*anktu-  oder  *nktu-, *e7iktu-)  ,Totschlag'^  zunächst  zu  verbinden  ist  (s.  Falk-Torp  17,  1430), wLirzelhaft  mit  anÄ:-  , Zwangt  (:, bedrängen,  töten^?)  ursprünglich  gleich ist,  oder  zu  *enek-  ,töten^  gehört,  wie  auch  hitt.  hi-in-kdn^  ht-en-kdn (henkan)  ,Tod^
WP.  I  60,  Pedersen  Hittitisch  183  f.,  Hendriksen  Unters.  28,  Benve- niste  Origines  155.
2.  ank-,  ang-  , biegen^;  Nominalstämme  anko-,  onko-;  ankes-;  anku-lo-; anken-,  -on-;  ankoto- ;  ankro-.
Ai.  ancati  (mpers.  ancUan)  und  (tiefstufig)  dcati  ^biegt,  krümmt^,  Partiz. -akna-  (mit  ä-,  ny-,  sam-),  -akta-  (mit  ud-^  ny-)  ,gebogen^;  aidkd-h  m. , Biegung,  Haken,  Biegung  zwischen  Brust  und  Hüfte*^,  ardkas-  n.  ,Biegung, Krümmung^  (=  gr.  to  liyy.og  ,Tal,  Schlucht^,  ar^kasdm  ,Seite,  Weiche'; cwku-  in  aTdküydnt-  ,Krümmungen,  Seiten Avege  suchend.*^;
av.  anku-pdsdmna-  ,mit  Haken,  Spangen  sich  schmückend"^,  ai.  ankucd-h ;Haken,  Angelhaken,  ElefantenstacheP,  aTdkurd-h  ,junger  Sproß,  Schößling (ursprüngl.  Keimspitze,  gebogener  Keim),  Anschwellung^  (=--^  gr.  dyy.vlog ,krumm^,  dt.  Angel,  anord.  öll,  äZZ-, Keimblatt,  Keim^  s.  u.);
av.  aka-  m.  ,Haken,  Zapfen^,  axnah  (ßartholomae  Stud.  2,  101,  Airan. Wb.  359)  ,ZügeF;
gr.  dyy.(bv  ^Bug,  Ellenbogen^  (D.Pl.  dymoi  zu  dyAri  =  dyy.dlri),  iTt-rjy^isv-Ldsg .die  an  den  dyKÖvsg  (Rippen?)  des  Schiffes  befestigten  Bohlen^  (Döderlein, Bechtel   Lexil.   129),   IcyytOLva   ,alles   Gekrümmte^,   UyY.iorQOv  .Angelhaken';
4G
äyycvXog  ^krumm^^   dyxvXi]  ^Riemen*    (=  anord.  ol^  al  ds.),  ^yy.voa  .Anlcei dyAccXfj  .Ellenl)Og-en^  Bucht,  alles  Gekrümmte^;  tö  äy/.og  (s.  o.).
Mit  o:  oyxog  ^Widerhaken^  ==  lat.  uncus  ^g-ekrümmt;  Subst.  Flaken] {oy'/.lvog=  unclnus  Jfaken^  Widerhaken'^);  nngulus  ^Fing-erring^  Pacuvius] von  Festus  514  L.  als  oskisch  bezeichnet^  ungustiis  ^fiistis  uncus'  Paulus ex  Fest.  519,  s.  unten  unter  ang-)]  ^y/,fj'  ywria   Hes. ;
lat.  anciLS  ^qui  aduncum  brachium  habet^_,  ancrae  .convalles.  vallis^ (^Krümmung;  Einbuchtung^  wie  tö  fy/.og  =  germ.   *angra-)]
air.  tcath  ^»Fischhaken^  =  cymr.  angliad  ^Griff,  Hand'  (zu  craf-arn ,Klaue^)  aus  "^cmkato-  =  aksl.  gkoth  ^Haken'^;
gallorom.  ancoi'ago,  ancora(y)iLS  aus  ^miko-räkos  ^Rheinsalm,  Hakenlachs' schwd.  Anke  ^Bodenseeforelle'  (g"^^l-  *cinko-  ^gekrümmt'  und  *7'äko-  ,vorne^ aus  *prökO',  cymr.  o^hag  ;Yor^);
ahd.  angoj    angul   ^Fischhaken^    Stachel'^    aisl.  angi^    ags.   onga   ^Spitze] Stachel'  i^aidkön-]    über   got.  halsagga  ^Halshiegung,   Nacken'   s.  vielmehi angh-);  "^-angra  (bis  aufs  Geschlecht  =  lat.  ^^ancrae)  in  anord.  angr  ^Bucht^ (in  Ortsnamen  wie  Hardangr),   ahd.  angar,  nhd.  Anger  (germ.  VN  Angri- varil)]  gleichbedeutend  aisl.  eng  (^angiö-)  ,Wiese';  ahd.  angul  (=  gr.  äy%v- Xog,  s.  0.);    mhd.  angel  ,Stachel;  Angel;    der   ins  Heft   eingefügte   Teil  des? Schwertes';   anord.    gngoll   ^Angelhaken',   ags.    ongel  ^Angel'.     Much    stelltJ hierher    den    lat. -germ.  VN  Anglil,    ags.  Angel,    Ongel   als  ^Anwohner    der! Holsteiner  Bucht'  zum  aisl.  ON  Ongull,  mit  einer  sonst  nicht  belegten  Bed.lj ,Winkel;  Bucht'  (Hoops   Reallex.  I  61);    mit    ui'sprünglicher  AnfangsbetoJ] nung  anord.  öU,  all  ^Keimblatt,  Keim'  {^anhla-,   Noreen  Ltl.  25:  zur  Bed.J vgl.  außer  ai.  avkurd-h  noch  norw.  dial.  ange  ^Keim.  Zacke'  aus  *ankön-)j^ anord.  öl,  äl  f.  ^Riemen'  (Gdf.  '^dnhulö,  vgl.  dyy.vXrj,  oder  allenfalls  *a7i/iZö,i das  dem  gr.  dy/idlrj  näher  stünde);
slav.  jecbmy  ^Gerste'  als  ^grannig,  stachelig'  (Berneker  268),  vgl.  die obigen  Worte  für  .Spitze,  Stachel,  Zacke';
preuß.-lit.  anka  f.  .Schlinge,  Schleife'  (=  gr.  b'yxrj'  ywvia  Hes.);  aksl. okoth  ;Haken'  (s.  o.) ;
toch.  A  ancäl  ^Bogen',  ähkar-  ^Fangzähne.  Bollwerk';  auch  A  ohkaläm, B  onkolmo  ^Elefant'?     Van  Windekens   Lexique  6,  13,  82.
ang-,  bes.  zur  Bezeichnung  von  Gliedmaßen  (ngl.  got.  lijnis  .Glied': *lei-  ;b legen')  :
Ai.  ärdgam  ^Glied',  ai9güli-h,  aidgüri-k  f.  ^Finger,  Zehe'  (davon  aTagidlyam ^Fingerring');  cmgustha-h  ,große  Zehe,  Daumen'  ==  av.  angusta-  m.  ;Zehe', arm.  ankiun,  angiun  ^W^inkel'  und  anjali-h  m.  ;die  beiden  hohl  aneinander, gelegten  Hände';
!
47
o-v.  liyyog  n.  ^Eimer,  Schale^;  dyysTov  (^^ayyea-iov)  ^Gefäß%  eig-entl.  ,o-e- Hoclitenes  Gefaßt;
mir.  aigen  ^Pfanne*^  ist  dial.  Nebenform  von  *aingen  ds.;
ahd.  ancha,  enka  f.  ^Genick^  und  ^Schenkel^  Knochenrohre^  (*ank{ön-), inord.  ekkja  ^Knöchel,  Ferse^;  Derain.  alid.  anchal,  enchil  (umgedeutet (inkldo  m.;  anchala,  enchila  i.,  mhd.  mnd.  enkely  afries.  onkel,  onkleu^  iihd. Enkel,  ag-s.  (umgedeutet)  andeoic,  engl,  ankle,  anord.  okkla  {*ankulan-) .Knöchel  am  Fuß^;  auch  lat.  angidus  (womit  aksL  gg(7>)h  _,WinkeP  ur- verwandt ist)  , Winkel'   (daneben   mit   o-Stufe  lat.  tingulus,  ungnstus  s.  o.).
WP.  I  60f.,  WH.  I  46,  49  f.,  Meringer  WuS.  7,  9  ff.  ,
SnO'  ,Ring'.
Arm.  anu7' , Halsband,  Ring'^,  lat.  änus  ,Kreis,  Ring^,  air.  äinne  {*äninio-) m.  ,Ring,  After^ WP.  I  61,  WH.  I  55,  Pedersen  Litt.  2,  80.
ans-  ^wohlgeneigt,  günstig  sein^
Got.  ansts  f.,  ahd.  anst  und  (tiefstufig)  unst,  mhd.  giinst  aus  *ge-unst, ags.  est,  Gunst,  Gnade'',  anord.  äst,  öst  ,Gunst,  Liebe'^,  ahd.  ahanst,  ahunst, as.  avunstj  ags.  3efest  , Abgunst,  Ungnade^;  mhd.  gund  m.  ,Gunst^,  anord. qf-und  f.  ,Ungnade^;  Präteritopräsens  ahd.  an,  unnum  (Inf.  icnnan,  Prät. onsta,  onda)  ,gönnen^  (gi-unnan),  as.  ags.  unnan  ,gönnen,  einräumen, wünschen^,  anord.  unna  (ann,  unnom,  Prät.  tinnan  aus  *unpa)  ,lieben, gönnen,  einräumend  un-nu-m  (aus  *imz-nu-m-)  ist  ein  altes  Präs:  der  neu-, w?f-Klasse,  wozu  der  neue  Sg.  ann.  Wer  die  Wz.  als  germ.  an-,  un-  an- setzt, hat  in  ansts  die  Suffixverbindung  -s-ti-  zu  sehen  (s.  Brugmann  Grdr. n^  2,  437),  während  mhd.  gund,  an.  gfund  das  einfachere  -ti-  enthielten. Doch  ist  wegen  des  gemeingerm.  *anst(s)  die  Wz.  wohl  als  germ,  ans-, uns-  anzusetzen  (Kluge  ZfdtWtf.  9,  317,  Brugmann  Grdr.  IP  3,  332), unnum  mithin  aus  "^unz-num  (idg.  *ns-nu-me)  entstanden,  wonach  dann  Sg. ann,  und  das  neue  schwache  Prät.  '^un-pa  (ahd.  onda,  anord.  unna)  neben ahd.  onsta,  as.  gi-onsta:  auch  mhd.  gund,  anord.  gfund  (Suffix  -ti-)  sind dann  Neuschöpfungen  nach  dem   5-los  gewordenen  unnum,  unnan.
Auch  gr,  Ttooo-rjvrig  , freundlich'^,  dTt-rjvrjg  ,unfreundlich,  hart^  (:  ah-imst) ist  am  wahrscheinlichsten  =  '^tvqog-^  ccTV-avarjg  (s.  Brugmann  aaO.).
In  abweichender  formaler  Beurteilung  bezieht  Bechtel  LexiL  49  gr. -ävrjg   auf   ein   neutr.  Subst.  "^änos,    dessen    suffixale  Tiefstufe   dem  germ.
an-s-ti-  zugrunde  liege. WP.  I  68.  Feist  53.
48
ansä,  ansi-  ^Schlinge^  Schleife^^  z.  T.  als  HandliaLe  von  Gefäßen   (Henkel^ oder  als  dem  Zugvieh  umgeleg'ter  Zügel. Lat.  änsa  ^Griff^  Henkel^  Handhabe^;  ansäe  crepidae  ,die  Ösen  am  Rand^ der  Schuhsohlen,    durch   welche   die   Bindriemen   gezogen   wurden^  =  litj qsä  f.  (Akk.  äsq)  ^Topfhenkel;  Schleife   heim   Knotenschürzen'^   (vgl.  auch] lat.  ansätus  ==  lit.  qsötas  ^gehenkelt^),   lett.  nosa  ^Henkel,   Schleife^,    Öse' woneben   2-St.    apr.  ansis   ^Kesselhaken^    lett.    üoss    (Akk.  iiosi)    , Henkel aisl.  ces  L  {^ansjo)  ^Loch  am  oberen  Kande   des  Schuhleders  zum  Durch.] ziehen  der  Riemen'  =  mnd.  Öse  f.  »ringförmige  Handhabe^  Schlinge'  (dar- aus spätmhd.  nhd.   Ose;   oder   das  wgerm.  Wort  zu  Ohr  nach   Kluge  und? Weigand-Hirt  s.  v.?);  mir.  e(i)si  PL  ^Zügel'.  gr.  fjv'ia,  dor.  ävia  ds.  {*ävGia)\ WP.  T  m,  WH.  I  51,  Trautmann  10.
ansu-,  nsu-  ^Geist;,  Dämon'.
Ai.  cisii-,  av.  atdhu-  , Lebenshauch,  Welt',  davon  ai.  dsii-ra-,  av.  almra- ,Machthaber'  {*nsu-)]  ven.  ahsu-  {==  äsu-)  ,Kultbild'  =  germ.  *ansuz  ,Gott;j Ase'   in   aisl.  äss,   run.  a[n]suR^   ags.  ös  ,Ase',  got.-lat,   anses  ^Halbgötter
Vielleicht  zu  an(d)-  ,atmen'.
H.  Güntert  Der  ar.  Weltkönig  102,  Feist  52  b.
ant-s  ,Vorderseite,  Stirn',  mit  o-Erweiterung  anto-,  usw.
Ai.  dnta-h  ,Ende,  Grenze,  Rand'  (davon  antya-li  ,der  letzte');  |
gr.  Gen.  Sg.  xdvavTeg  {j=  %aT   dvzsg)  ,die  Vorderseite  herab',  Dat.-Lok.l dvri  (Schwyzer  Gr.  Gr.  I  548 ß,  6225)^  Akk.  eta-dvia  ,ins  Gesicht'  (*ant.m),  . h-avxa,   Uv-avva,   xdx-avxa   usw.    (W.  Schulze,    Kl.  Sehr.   669,    Schwyzer Gr.  Gr.  I  632  u.),  adverbiell  &Vra   ,gegenüber',   danach   dv-tdü)   ,begegne'; über   UvTOi.iai   s.    Schwyzer    Gr.  Gr.  I   722   u.;    über    Uvttiv   s.  Brugraann Grdr.  TP  2,  687;
air.  etan  (*antono-)  ,Stirn';  vielleicht  hierher  mcymr.  enhyt,  cymr.  ennyd ,Zeit,  Augenblick'  (*a?it-iti-  zu  ai.  iti-  ,Gang'),  mcymr.  anhaiv  ,alt'  (*ant-auo-), nir.  eata  ,alt;  Alter'  (*ant.odio-?%  vgl.  Loth  Rc.  48,  32;  50,  63;
hitt.  ha-an-za  (Äani5-s)  , Vorderseite',  davon  ha-an-te-iz-zi-is  {hantezzis) =  *ant-etios]
lyk.  x^^ta^^ata  , Anführer'  (Pedersen  Lyk.  u.  Hitt.  17);
toch.  A  antide  »außerhalb,  bis  .  .  .  vor',  antus  .also'.
S.  auch  unter  antios.
Dazu  als  ursprüngliche  Kasus:
anti  ,im  Angesicht'  >  ,gegenüber',  usw.
Ai.  anti  Adv.  ,sich  gegenüber,  vor  sich,  nahe',  wovon  antikd-h  ,nahe', n.  ,Nähe'.
49
Arm    ««^^  .dort-,  dnd  Präp.  ,für,  anstatt'  m.  Gen.  und  ^längs,  über  (an,
n  etwas  bin'  m.  Akk.  (vg'l.  got.  and),  in   der  Bed.  ,zur  Seite'   m.  Abi.
1       lit    bei'  m.  Lok.  (welcher  Vokal   im  Auslaut  geschwunden  ist,   ist
.  1 /bestimmbar;  anl.  9-  aus  a-  infolge  der  Proklise),  als  Präverb  ,auf-';
dlzu    andraiük   ^Erstgeborener,    erster'    (Bugge   KZ.  32,  2;    vgl.   zur    Be-
/utun^   lat.    ante   ,vor'   und    die    oben   genannten   Worte    für   ,Stirn'    als
Vorderseite')^  wohl  auch  ancanem  ,gehe  vorüber'  (Pedersen  KZ.  39,  425,
yo-l    tri«.  Icvxo^aL  ]  c  aus  t  4"  dem  aoristischen  s,  vgl.  den  Aor.  e-anc).
Gr.  ävrl  ,angesichts,  gegenüber,  vor;  für,  anstatt'  m.  Gen.,  auch  Präverb,
B.  äyO-i(Trrj(,Li',  hom.  xar'  ^vcrjaziv  ,am  gegenüberliegenden  Standpunkt, «»•et»-enüber'  ist  wohl  nach  Bechtel  Lexil.  46  aus  *^vvi-(yTL-g  nach  ävrrjv XatriLU  umgebildet;  dvxi-AQVy  att.  ävzL'Aovg  ,geradezu,  entgegen'  (Ausgang unklar),  ävridüj,  ävTiäl;ü)  ,begegne'.
Lat.  ante  (aus  *a?i^i,  vgl.  antistö,  sowie  anflcus,  antiquus)  Präp.  m.  Akk. riUmilich  ,gegenüber,  vor',  zeitlich  ,vor',  auch  Präverb  (z.  B.  antecedo), antid-eä, -liäc  ,YOvhQv' ,  antid-lre  ,vorangehen'  {-d  nach_prö<^);  dazu  anterior früherer',  antärium  bellum  , Krieg  vor  der  Stadt',  antlcas  ,der  vordere' (c  nach  posticus  ,hinter'),  antiquus  ,alt'  (der  Ausgang  und  die  Verengerung auf  die  zeitliche  Bed.  nach  novus]  idg.  *anti -\- *olm-  ,aussehend'),  antes, -mm  ,Reihen  (von  Soldaten,  Weinstöcken  u.  dgl.)',  ursprünglich  etwa ,Fronten'  (über  antae  s.  aber  unter  "^andtä  ,Türpfosten').
Hitt.  ha-an-ti  (hanti)  ,vorne,  besonders'.
anta  ,gegenüber  hin'  (Richtung);  zum  -a  s.  Sclnvyzer  Gr.  Gr.  I  622 f.
Got.  and  Präp.  m.  Akk.  ,auf— hin,  über— hin,  entlang'.  Mit  davon  ab- weichender Bed.  das  Nominal-  und  Verbalpräfix  germ.  anda-,  and-  ,ent- gegen,  gegenüber'  und  —  indem  ein  Dagegenhandeln  in  ein  Trennen  aus- läuft —  in  Verben  perfektivierend  gewöhnlich  ,von— weg' :  got.  anda-,  and- (z.  B.  andniman  ,eutgegennehmen',  andanüms  ,annehmlich,  angenehm', andbindan  ,losbinden,  entbinden'),  anord.  as.  ags.  and-,  ahd.  ant-,  int-, mhd.  nhd.  ant-,  ent-  (z.  B.  Antlitz,  Antwort,  entbinden).
Komp.  anord.  endr,  enn  ,früher,  vormals,  wieder,  nach'  (endr  =  got. andiz-uh  ,entweder'),  ags.  end  ,vorher'  (^andis),  ahd.  enti  ,früher,  voi-mals' (germ.  "^andiaz),  mhd.  e^it,  end  Konj.  ,ehe,  vor'  (z.  B.  Falk-Torp  192,  1455).
Lit.  ant,  älter  anta  m.  Gen.  ,nach— hin,  auf.
über  gr.  ävTcc  s.  oben.
nti
Eine  schwächere  Ablautform  ("^nt-)  zeigt  got.  und  m.  Dat.  ,dyTi,  für, um',  unpa-  (*nto-)  in  unpa-piiuJian  ,entfliehen',  ags.  od-  (*unp-)  in  oägangan ,entgehen',  üdgenge  ,fliüchtig'  =  anord.  unningi,  undingi  (*unp-,  *und- gangia-)  ,entwichener  Sklave'  (Brugmann  Grdr.  II-  2,  803),
4
50
Andere  Bed.  zeigt  got.  und  m.  Akk.  ^bis*^,  ahd.  unt  in  unt-az  jhW  undj unzi  (=  untzi)  ,\i\s',  as.  und  ,Vis^,  unti,  unt  {und  -J-  te  ,zvi^),  unto  {und  -f-  tö)^ engl,  unto  ,7m,  bis^,  anord.  unz  {und  es)  ,bis  daß^^  ags.  (mit  grammatischeruj Wechsel)  o^  ^hin  zu^  bis^^^,  osk.  ant  m.  Akk.  ^bis  zu^  (ebenfalls  aus  *nid s.  Walde  Kelten  und  Italiker  54;  wegen  der  zu  germ.  und  genau  stimmenden] Bed.  nicht  =  lat.  ante  zu  setzen,  z.  B.  v.  Planta  II  443),  lit.  int  ,nacVl (eher  Kontamination  von  in  und  ant).  Daß  diese  Formen  eine  Erweiterung] der  Präp.  *en,  *n  ,in^  darstellen  (Schwyzer  Gr.  Gr.  I  629  f.,  wo  auch] über  gr.  dial.  svts)^  ist  möglich,  wie  denn  lit.  int  mit  f  ,nach^  in  der  An- wendung sich  deckt.  Doch  könnte  dies  eine  nachträgliche  Gebrauchsan- gleichung infolge  der  Lautähnlichkeit  sein  und  idg.  *nt{-i^  -a?)  ,bis^  als ^gegenüber  hin,  auf  die  entgegengesetzte  Seite  hinüber^  zu  anti  gehören;  auch die  Worte  für  ,Ende^  (s.  u.)  sind  ursprüngl.  das  auf  der  gegenüberliegen- den Seite  winkende  Ziel,  und  mit  as.  unt  ist  auch  ant  {and  -\-  te)  Präp.  m. Akk.  ,usque  ad^  bedeutungsgleich,  was,  selbst  wenn  nur  junge  Kreuzung  von unt  mit  and-  vorläge,   doch   die  Begriffsverwandtschaft   beider  beleuchtet.
antios  , gegenüber,  vor  einem  liegend'^  (vom  Adverb  anti  gebildet): *antiö-  (gerra.  *andja-)  in  got.  andeis^  anord.  endir,  as.  endi,  ags.  ende m.,   ahd.    anti,   entl   m.    und   n.,   nhd.   Ende]   auch   gr.  ävTtog  ,gegenüber^ {d3iZ\i ivavzlov  ds.,  ivavvlog  ,gegenüber  befindlich;  Gegner^)  geht  wahrschein- lich (vgl.  Schwyzer  Gr.  Gr.  I  379)  auf  *ävTiög  zurück.
Dagegen  ist  von  *anto-  (s.  oben)  abgeleitet  dntio-  in  anord.  enni  n., ahd.  andi,  endi  n.  ,Stirn^  =  lat.  antiae  ,capilli  demissi  in  frontem^»
Ein  ganz  verschiedenes  Wort  ist  nhd.  und^  ahd.  unii^  anti,  enti  u.  dgl., as.  endi,  ags.  engl,  and  ,und^,  anord.  en{n)  ,und,  aber^,  das  mit  ai.  dtlm ,darauf,  dann,  desgleichen^,  av.  a&n  ,ebenso^,  osk.  ant  m.  Akk.  ,usque  ad^, lit.  int  m.  Akk.  ,nach'^  (aber  s.  oben),  toch.  B  entwe  ,also^  zu  *en,  iq.  ,in^ gehört.
WP.  I.  65  ff.,  WH.  I  53  f.,  Feist  46,  Schwyzer  Gr.  Gr.  I  619,  621, 629  f.,  632  f.,  722,  726,  II  (B  V  2  b  d  3).
antro-m  ,Höhle,  Luftlochs
Arm.   ayr,  Gen.  PL   ayric  ,Höhle^,  gr.  ävzgov  ds. Vielleicht  zu  an{9)-  ,atmen^,  als  ursprüngl.  ,Luftloch^ WP.  I  561,  Schwyzer  Mel.  Boisacq  II  234 1,   KZ.  68,  222,    Gr.  Gr.  I 532,  Pisani  KZ.  68,  161  f.
I.  ap-  (richtiger  dp-)  :  ep-  ,fassen,  nehmen,  erreichend
Ai.  äpnötierreicht,  erlangt',  jünger  äptd-h  ,geschickt,  geeignet,  vertraut'; av.  apayeiti  ,erreicht',  3.  PL  äpdnte  aus  *äpuantai;
51
arm.  itnim  ^besitze^  (*öp-n-?)^  dnd-unim  ^erlange"^;
o-r.  ärtto)  ^anfassen^  anheften^,  anbinden^  anzünden^^  tlmEa^ca  ;berühren% cicpn  Berührung^  Haften  usw/  wird  trotz  dem  Spiritus  hierherzustellen sein.  Kretschmer  Gl.  1,  352  nimmt  Beeinflussung  durch  ertoj  an;  hom. dwcict)  (äq)dü))  ^berühre^  betaste^^  ion.  acpäaoo)  ds.^  hom.  dcrtaq)ia'/.(x),  }jrca(pov (mit  äol.  o:  ärtocpeiv'  ärcazfiaai  Hes.)  ^betrügen;,  täuschen^^  dTrocpcbXiog trüo-erisch^;,  '/.airjcprjg  ^niedergeschlagen^  (eigentl.  ^untergekriegt^).  Pedersen KZ.  39^  428  stellt  mit  gr.  Utito)  arm.  a//  ^die  hohle  Hand^  (o-St.^  doch Lok.  y-(^p'^  3-^3  -i-St.,  also  wohl  ätler  neutr.  -o-i-St.)  zusammen,  welches Wort  dem  gr.  äxpog  ;,Gelenk^  entsprechen  soll;  wegen  des  p*  (=  idg.  pA) jedoch  unsicher  (vgl.  Meillet  BSL.  36^  HO);
lat.  apiscor  ^fasse,  erreiche^^  adipzscor  ^erlange^;,  coe.'pi  ,habe  angefangen^; später  coepl.  Der  Zusammenhang  mit  lat.  *a2nö,  *apere  ^comprehendere vinculO;  verbinden,  umbinden^  (imper.  ape  ,prohibe,  compesce'^),  aptus ^verknüpft,  ausgestattet  mit^,  cöpula  (co-apida)  ,Band*  steht  wohl  fest. Vielleicht  ist  von  einer  gemeinsamen  Grundbedeutung  ^fassen,  zusammen- fassen^ auszugehen.
```


## [2026-09-04T22:41:53.816Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT page markers style ===\"\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=t.find('duz-aka')\nprint('duz-aka',i)\nfor pat in ['dužaka','duz-aka','dus-aka','duž','aka-']:\n    idx=[m.start() for m in re.finditer(re.escape(pat),t)][:5]\n    print(pat, idx)\nEOF"
}
```


### [2026-09-04T22:41:55.714Z] TOOL RESULT

```
=== BRT page markers style ===
duz-aka -1
dužaka []
duz-aka []
dus-aka []
duž []
aka- [200712, 206089, 274513, 287599, 739539]
```


## [2026-09-04T22:41:55.798Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('npages',len(pages))\n# find printed page 755\nimport re\nfor n,p in enumerate(pages):\n    if re.match(r'\\s*755\\b', p) or '\\n755\\n' in p[:200]:\n        print('candidate',n)\nprint(repr(pages[400][:300]))\nEOF"
}
```


### [2026-09-04T22:41:57.711Z] TOOL RESULT

```
npages 1041
'l\'ü.:  mk/iilan;  s.  No.  13.  —  ")  Wort].:  non Sicram  curat  sibi  es^e  ärmatim.  —  \'1)  Pü.:  pa «ikSUiH;  s.  Xo.  II.  —  M)  FOT  KZ,  ^.  560 will  adäravam  wegen  Eü.  —  \'J)  El  scheint etwas  ausgefallen  in  sein.  Vgl.  Gdn.  KZ. lg.  544,  der  \'ein  jedes\'  ergänzt;  iihnlich  '
```


## [2026-09-04T22:42:04.650Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# print first 60 chars of pages 380-400 to find numbering\nfor n in range(370,400):\n    head=' '.join(pages[n].split())[:80]\n    print(n, '|', head)\nEOF"
}
```


### [2026-09-04T22:42:06.516Z] TOOL RESULT

```
370 | Vfrs^nm ..Y. 68.11; Yt.io.io8; — "nvS vlspayä drvatätim °nvS vTspayä vazdvar) Yt
371 | n. 'Grösse des Leibes': V.Ä91. LW. aus dem s (M.), np. I..ir. iraud- mit afa I n
372 | cht mit den Füssen, nicht mit den Händen sollst du etwas ausrichten können" Y.5,
373 | einer Ableit «ns iarö; % 178. ~ ai. äraJcd Adv. 'quer duicb'. — Pi. : taräf. • ]
374 | . 13; V.ltj.jo; — | I'ü, (lu Vyt.h lar i'ariin,(ra'S.): *tar fihn'\ tUTBObOMAS, 
375 | vä *na (IS.) va N. IS' "'. Aus ir. '(r^*. I?- 9- >6i' — ™P- (Pö-)t "P- liin, ai.
376 | mraot "was dein Aia, was dem A. J- y^""" '"'" ^- ^^- ^- =■ y^'''^'- der Schöpfer
377 | . •tarn t?masairjm t^tnanhim V. 5. 63, /(?. 76; — drujim yqm . . 'nun Yt. '9- 9S
378 | , 464. — 3) Kann auch auf BT. *lansra- gehen. • j. ti^'d-rö. JUnah- '^ Adj. 'der
379 | �ml. ayan) heisst der 13. Monats- tag: 'ryeie stärJ ra^fa/ff s^armanuhaiS S.Z. 1
380 | Y.4i.y, — ä ta mg altayä zao'hraya frtmhardis Yt. j. 9 1 ; — vasas^a ta ahura . 
381 | türa- m. EN. eines Gläubigen**: arsJatfuAatö 'rahe aiaotas Yt/5, 113; — /rärazSi
382 | va- (Sp, 166 o.): ya^säm Aa/ama* ahahyJ' . . avi^ *akunavayi^t3 Eh. 7. 7 ; D. 6.
383 | (Unsicheres bei GCR. GliPh. / b. 218, 393.) Zum / und zSchr. % 416 a No. 1 mil F
384 | /raourvaaayäiti drujS vais- mmda " aztmnqm (sd.) Yt 10. 86. Vgl. gr. *ij iilKi^i
385 | 42; — 'na . . p3r?näyul cihqm %wfnsaiti W.j. 41 (?). a) meist mit einem bestimme
386 | (sd.) äatü . . ahuri> asahya axäyai (sd.) ggnedim Y. 37, 17; — aiäunqm . . uruns
387 | �r die Gottheiten der vor Zard^ustra in Iran geltenden Religion: cüma . . Auxs'd
388 | rt: mürym . . yahmal haca frabr^SMii vTspe mainyava (Stverz.) •va yaica varsnya 
389 | Adj. (fem. "«-) 'von den Daiva geschlagen': haea avaakät tanvai yai 'tayä (sUtt 
390 | S. 3 : koAmäi fradasayö dalnam V. 2. i ; — ahmäi fradalsaim dag- nam V. 2. 2; — 
391 | Et, KZ. 3S- 479 ist sehr iweifelbarr. I • j. daxma- m. 'Leichenstätte, Leichen- 
392 | erU: ilakmaklar trwel. — J) Abweichend Gdn. 3Vt ii9i s. aber V, J. 59. — *) Vi.:
393 | Y./6. 4-6; — xsvastlm ^maibysihmahe (sd.) HstryAe •%uis K3.Z^; 7^. PPfA. luni V.
394 | . Zum V. fl^. — aj. ddmsai- n. — Pü.i httvän dÖHäi. • j. daisbav-, da^hay-, daah
395 | ÖHT/ali 'er rinnt' ; np. vgl. äaiiidan, — ') Them., wie ai. dhanvati. Doch ist a
396 | . V. 2. 3a; — psurvS . , yat< 'im usla uzävqnayat (sd.) . . ^ra^aonff Yt5.6i; J0
397 | V. 2. j PiiZ.; — yai,cit 'im dava . . T.^4'} — yaica *'im . , Vyt.47i — «äV zI d
398 | Bn. Stud. /, 351. — Pu. (zu \.2g): shrmaad an i pa Timänlt (Sn.; sanidtAiyam) ha
399 | der ZV»/genosse sich anschickt mich zn ver- gewaltigen" Y. 46. T- 6) 'in Besitz
```


## [2026-09-04T22:42:14.324Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor pat in ['Stachelschwein','duzaka','duz-aka','dužaka','duJaka','du5aka','ilnzaka','zuzag','žužag']:\n    for n,p in enumerate(pages):\n        if pat.lower() in p.lower():\n            i=p.lower().find(pat.lower())\n            print('>>',pat,'page',n,'::',' '.join(p[max(0,i-400):i+400].split()))\nEOF"
}
```


### [2026-09-04T22:43:24.373Z] TOOL RESULT

```
claude-sonnet-5[1m] is temporarily unavailable (timed out), so auto mode cannot determine the safety of Bash right now. Wait a moment and then try this action again. If it keeps failing, continue with other tasks that don't require this action and come back to it later. Note: reading files, searching code, and other read-only operations do not require the classifier and can still be used.
```


## [2026-09-04T22:43:28.798Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"Stachelschwein\" BRT.txt | head -20",
 "description": "Search Bartholomae for Stachelschwein"
}
```


### [2026-09-04T22:43:28.854Z] TOOL RESULT

```
26367:'Stachelschwein':  hau  'rTnake  .  .  hau vlspanqm  .  .  spacihranqm  V.  7J.  16;  — spa  °T3n5  V.5.  31,
```


## [2026-09-04T22:43:34.562Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26340,26400p' BRT.txt",
 "description": "Print Bartholomae context around Stachelschwein"
}
```


### [2026-09-04T22:43:34.610Z] TOOL RESULT

```
'Halsring',  d.  i.  ein  vom  Joch  ausgehendes, den  Hals  des  Pferdes  umfassendes  Rmid- holz:  aat  tl  (näml.  aurvantlf)  vTspa  frä.- yuxta  *Aqni.ivam{sA)ca  °mqmia  simSi- "^rqmca  YLJO.  laf.
kompA.  — VgL  iEl  und  zBed.  Lagercrantz
KZ.  34-  396.
•  j.  simöiSrä-  f.  ein  Teil  vom  Geschirr des  mit  Pferden  bespannten  Wagens,  vU. 'Joch':  aat  U  (oäml.  aurvantff)  vupa  frS.- yuxta  *Aqm.ivqm{sA.)ca  simqmca  'rqmla Yt /0.12s.
Komp.:  rimÄ-+*Afä-(?).
•  j.  sispsmna-,  sispimna-  Adj.  (fem. 'nä-),  PPM.:s.J/50')-.
•  j.,  g.  ji'ii^_y(7-Praes.  18b 'zurücktreiben;
zurückweichen'.
i)  'zurücktreiben':  vlstäsf^m  .  .  yat imqm  dainqm  ästaota  dulmainyäm  sisdyl äatvqn  apa  "alavatt  (sd.)  Yt./5.84.  2)  'zu Tückweichen,  sich  entfernen  von  — '  (Abi.): ma^ä  .  .  vattlaul  sizdyamnS  mananhö .  .  ahurahyä  xratsus  nasyantS  (sd.)  a/J- atca  ",  .  die  sich  entfernen  vom  guten Denken  . ."  Y.J2.4.
Vgl.  lyasda-  und  «äfra-.  —  El.?')  ar.  "iiH^aidlfif :j(iy5rf:4*.  — Pü.!  aiän  -.-akuman  +/t£r/ (Trans - skr.)'),  ttX.:  kuiän  hal dür;  Sü.:  iiUamam  sida- yiUi  manah  ,  erl- :  . .  tifäm  dekäl  gvaAnattah düri  äste.  '—  D  Ohne  Wert  S  139-  —  '>  Am Ende  mit  t  statt  d  geschrieben.  S.  lu  syazdal und  zu  siidra:
•  j.  sizdyant-  Adj,,  PPA.:  S.  sisdya-.
•  g.  sizdyamna-  Adj.,  PPM.:  &.st;dya-
•  j.  Sizdra-  Adj.  'scheu':  spsnim  slidr?» .  .  yim  var?hapartm  "den  scheuen  Hund V.  (Igel)"  V.  13.  z;—  auruna{sA.ya  gairi- säcB  sizdra^a  ravascarats  Yt  8.  36.
Zq  syaa^a-,  siidya-;  vgl.  lEl.  Gdn.  KZ.  2^.407, zBild.  ni^dra-  und  ai.  nudhirä-  mit  IF.  7.  57,  — Pü.i  +jarf(Transskr.)'>,  erl.:  k^Jlk —  0  S.  za  sildya-  nod  syazdal,
•  j-  (1  gO  3Ü-  f.  'Nutzen,  Vorteil':  nai^is *i6a  .  .  sUs  *yd^a  hxm  ädan  mar^äka "es  ist  da  kein  Nutzen  vorhanden,  weil es  die  Menschen  wegnehmen  können" FrD.jf?);  —  JfJ  (GS.)"  F./2.  DS. suyi  als  Inf  sbes.
KompE.  ~  Zum  V.  sm/-.  —  Pü.i  ™(.  — »  D.  i.  "suvQ,  %  268.   13.
•  j.  süka-'>,  j.,  g.  süda-"'  i)  Adj.  'sehend, licht':  sraota  ^gSulMsiy^^)  vahistä  avainatä •c3  mananfiä  ". .  seht  es  euch  an  mit  lichtem
suxra-  1 583
Sinn"  Y.jo.2'>;  —  •&  F./2J>.  2)  m,; a)  'Sehkraft,  Augenlicht':  apa  (näml.  barahi) ^aimanä  'ktm  apa  gaeiayä  sraoma  Yt. 10.  33;  P.^^(?)*l,  F.  J2(?)«;  —  aomla 'k>m  yim  baraiti . .  Yt  /4. 3  9  *'.  b)  'Licht Erleuchtung':  'kni  manarjhe  'käi  valanhe 'käi  ryao%naAe  Y.  68.  4"*.
KompE.  —   Zum  V.  saai:   —    ai.  hicä-  Adj.
•lieht'.   —  Pü. ;  s.  No.  »ff,   —    ')  Mit  h  nur
F.—  ')  Pd,;  röht.—  3)  Pü.i  vtiiäi.  —  A)  Pö.;
vhtSnXh.  —  M  Pü. :    vinän.  —  *)  Npü. :    süd;
M4  hat  saokim'.
•  j.  sükä-  f  'Nadel';  avaviüctl ya%a  °kaya bräzayä  bräs»m  avavatcit  ya'ha  'kayü na/am  "auch  was  nur  so  gross  ist  wie der  Schein  einer  blinkenden  Nadel, . .  wie das  Öhr  einer  Nadel"  Yt  74.33.
ai.  iüka-  m.  'Cetreidegranne' ■),  np.  vgl.  jäun •Nadel'.  —  ü-pü.:  sSdmaiui{,\).  —  ')  Wegen ai.  süa-  f.  •Nadel'  s-  Horh  NpEt.  167,  Hbh. PSt.  77,  Wn.  AiGr.  T.  226  p.
•  j.  sukurana-  m.  (auch  mit  ^span-  m.) Name  einer  Art  des  'Hunde' ''geschlechts,
'Stachelschwein':  hau  'rTnake  .  .  hau vlspanqm  .  .  spacihranqm  V.  7J.  16;  — spa  °T3n5  V.5.  31,
np.  sugur.  —  Pu.!  *iuiurr.  —  D  Vgl.  'ifiaif*i.
•  p.  suguda-,  j.  suj-Sa-  Adj.,  be- zeichnet ein  Volk,  'Sogdianer'  (nur Komp.).  a)  Sing,  (koll.)  für  Volk  imd Land:  Wimä  dahyava*  tyä  manä  pati- yäi/a'  . .  bllxtri¥  'da*  . .  "..  Sogdiane  . ." Bh.l.6;  D.5.  2,  7.3;  —  yahmya  apB  .  . %waxsfnte . .  gaomca  *sirfiim  '>  x^äiriz»m&i Yt  10. 14.
KompA.  —  ')  Hds.  suxiim;  das  Wort  ist inlerpolirt,  s.  'gana-*).
•  j.  su}'J)ö.§ayana-  Adj.  'die  Wohnmig der  Sogdianti  bildend,  wo  die  S.  wohnen': gäum  (Sp.  509  u.)  yitn  'mm  V,  1.  4.
Pü.:  ddnrdk  (statt  ddndd  =  nigdl)  mäniht. j.  TOj-fcw  Yt.  10.  14:  lies  iwtJj«.
•  j.,  g.  suxra-  Adj.  'rot',  vom  Feuer:  äal he  Jm  zh  bvat  pirane  .  .  ährqmca  'rqm  " saoantqm  "voll . .  und  von  roten  flammen- den Feuern"  V.  2. 8;  —  Sica  S'hrS  'rä (IS.)  .  .  vaahau  vidäta  rqnayä  (sd.)  Y. 5/.  r9;5/.9.
Zum  V.  laoi:  —  Vgl.  auch  %uxra-  EN.  ~ ai.  hiirä-  Adj.  licht',  np.  ™rj:  'rot'.  —  Pü.: mxr.  —  ■>  NA.J  die  meisten  Hds,  fBgen  co zu,  weil  sechs  vorhergehende  Wörter  damit Ecbliessen.    UDnchtig  FrMOllbr  WZKM.  6.
dby  Google
1 583  "suttm
•  j.  "anjiatnea  sutsm  vaahSna^  nanm  1 na  araiufry^  N.pz.
Pü. :  anH  ätt  i  ddn  pt  n  /u  tiUüM  nfe  draptnd (i.  Sp.  1394  u.  No.  s).
•  }.  8u8u§-  □.  'Getreidemühle':  yal  '\us dayäi  Bat  dagva  iustn  (sd)  "wenn,  die Mühle  (zum  Mahlen  des  Getreides)  zurecht gemacht  wird,  dann  . ."  V._^.  32.
Bed.  nnsicher;   vgl.  unter  ^aid-,  pSlra-  und
gunda-.     Anders  bei  Gdn.  KZ.  24. 549,  Ggr.
ZDMG.  34.  4*4,  DST.  ZA.  2. 43.  —  Pu. :  ai/l
'durchbohrt'. ■  g.  süidyäi  Inf.  'zu  nutzen,  den  (ewigen) '' Nutzen  zu  schaffen':  a^lä  ahmäi  varmäi . .  nidätim  ahm  s'  tkal^äi  (sd.)  räiayeAkl druxs  Y.  4g.  3 ;  —  kä^B  aahSid  vahiitakys paourvlm  ka%S  (sd.)  s'  yi  I  fattisäi  Y. 44- i-
Zum  V.  sav-.  —  Pü. :  sül  doMln,  lu  Y.  4g erl.;  ai  mizd  dahel,  —  ')  Vgl.  saV'  2.
•  j.  suptay-  f.  'Schulter*:  haoyqm  (bz.  dasi- lum,  sd)  'tim  V.i'.46-47',p.  17*.
ü.  iuptay-  f.;  mp,  {Pü.*,  np.  nj/"/.  —  S.  noch S  S'-  '■
•  j.  suptiJIar^nga-  Adj.  'Gaugenosse,  aus dem  selben  Gau  gebürtig':  visaifivä  asii mihm  anian  hasa  'ga  (AD.)  %risd^w3 antarf  vanzäna  cähwarjsahwa  antan ht^gaiSia  pancasa^wA  antar»  Auyäyna "zwanzigfach  (bindend)  ist  M.  zwischen ein  Paar  Genossen  aus  dero  selben  Gau, . .  aus  der  selben  Gemeinde,  . .  aus  dem selben  Haus,  . .  aus  der  selben  Stube" YtiO.  116.
Et.?  Die  üblicheHeraniiehangdesrihd.jiviifä'fr. magen  (snletit  bei  DsT.  ZA.  2. 473)  ist  nichts
•  j.  suwrä- 1 'Pfeil':  aai  hl  eaya /rabanm .  .  'rqm  saranamXm  a^frqmca  saranyl!.- faisTm  "da  übergab  ich  (nämL  AhM.) ihm  (näml.  Yima)  zwei  Geräte  (als  Hoheits- zeichen): einen  goldenen  Pfeil  und  eine ..  Peitsche"  V.  2. 6;  —  hS  imqm  tarn aiwilvat  'rya  (IS.)  saranatnya  "der  ritzte die  Erde  ..  mit  dem  goldenen  Pfeil"  V. 2. 10;  —  aiwica  tl  van/fua  (Sp.  1371  o.) *rya  saranamya  V.  2. 30;  38.
PDi.  sHtb  'Pfeil';  BTtO,  ZDMG.  4^.  294-  — PS,;  lüräiimand  'was  ein  Loch  hat',  crl. : mtrak  daslai,  s.  dazuDsT.  ZA.  2.  31,  Hokn HpEt.  314.  —  ')  Man  üherietzt  jetzt  meist 'Ring',  nach  Gü.;  %.  DsT.  SBE.  4.  13,  Bang WZKM.  j.  1 1 7,  JN.  JAOS.  14-  cxxiv,  FrMOller WZKM.p.  i68,jDSTiNB.  144-  DsT.  gibt  aber jetit,  ZA.  2.  21  'Siegel'.  Doch  wird  mit  dem Siu-StM  bei  Dakax  FahlVend.  13  diese  Bc-
'süra-  I 584
deutuDg  nicht  erwiesen.  Das  Hoheitszeichen auf  dem  Bild  292/3  in  Jn.s  Zot.  ist  doch kein  Ring,  sondern  ein  Kranz.  —  >)  Die Etymologie  des  np,  süräx  in  GIrPh.  /  b,  49 ist  falsch. j.  sQit',  Kasulf. ;  s.  'ifaH;  'sfati:
•  j.  süni-''  m."  'Hund':  yat  'nJi para.- irihyäti  ^nastä.ismanasca  pairista.xlu- drasca  "wenn  ein  Hund  stirbt,  der  sein Brod  nicht  mehr  verdient  imd  dem  der Same  versiegt  ist"  V,  y.  50;  —  Aaianrsis 'nl/  slrlMämanö  hasanräis  'nJ/  nairyS.- nämanS  mihwana  strica  nairyasca  "auf tausend  weibliche  und  tausend  mannliche Hunde  kommt  paarweise  ein  Weibchen und  ein  Männchen"  V.  y.  5iä>; —  hasa- tträU  °nXi  strJJiätnanS  haxanrnii  'tüs nairyS.nämattS  V.  14.  i  Gl.
Ableit.  aus  'sfan-.  —  ai.  hiiä-  f.  'Hündin'.  — Pü.:  sai;  s.  noch  Ko.  3.  —  D  So  NA.;  K  1, L4  haben  tun'.  —  >)  Eig.  jedenfalls  wie  ai. äitd-  Feminin,  'Hündin'.  Dann  aber  diente dai  Wort  ebenso  wie  <i/an-  ohne  Rücksicht auf  das  Geschlecht  alsGattungsbeicichnung. — J>  Das  ist  gemeint.  Aber  der  Satibau  ist nicht  in  Ordnong.  PO.:  ie  hal  1000  sai  i mätai  näm  hal  lOOO  sai  i  nar  pa  vimicak mSlai  u  nar.
•  j.  suyamna-  Adj,,  PPM.:  s,  sav-.
•  '].  suyä-  f.  'Nutzen'(?):  yazai  *apqmca tay^mca  . ,  axiUm  kqm.vaintlmta  'yamca kalarTmlil  Yt.  1$.  1.
Zum  V./fli".  —  Geringe  Stelle.
•  g-  suye  Inf.  'zu  nützen,  den  (ewigen) Nutzen  zu  schaffen':  sraotB  säsnä  fsSttghyS (sd.)  f '  tastü  Y.  49. 9.
ZumV.joi;.,  Bed.  a;  %368.l%  —  VgL  sü-.— Pfi.;  Sil;  U  lai-  No.  2.
•  j.  'sura-")  Adj.  (fem.  'ra-)  'stark,  ge- wiütig';  a)  von  a)  Menschen  und  ß) Göttern; zu  a):  tara'kustrahe  .  .  yS  *rS  Yty.  90; — yimahe..'rake  Yt  13. 130;  —  tOit  käu 'rS  .  .  (ys)  nsit  asa  'rS  P.  47,  zu  ß) : mikjrB  'rü  Yt.lO.15;  '4i  60,  76,  6,  7;  — apqm  naph  'rS  YLjj.  95;  —  'rahe  .  . ahurahe  Yt  ij.  78;  —  aomna  .  .  sraosaca afya  -ra  (IS.)  Yt  ;j,  146;  to.  52,  Y.57.I  i; ^  /iärim  . .  °nm  Yt  Ä  4;  —  salavoMsaiie 'rahe  YtiRo;  S.2,13;  —  airyamanam iltm  °r»n  S.  2. 3;  /,  3;  —  °ra  (VS.)  mi^ra ..  sni/ia  mihra  Yt70,3i;33;  —  -rä (statt  NSm.)  nqma  oAmt  szvtita  nqma oÄmi  (näml.  AÄM.)  Yt  j.  15;  —  oBs  .  . 'ra  Yt77.6;—  andvl  {Stvtiz.)  -«(VSC) anähite  Yt5. 18  usw.;  —  drvS^ayä  'rayä
```


## [2026-09-04T22:43:44.945Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E \"d[uüi][zJ5js3][.\\-]?[a-zA-Z]{1,8}\" BRT.txt | sort -t: -k2 | awk -F: '{print $2}' | sort | uniq -c | sort -rn | head -60",
 "description": "List duz- forms in Bartholomae OCR"
}
```


### [2026-09-04T22:43:47.529Z] TOOL RESULT

```
     16 dista
     14 dischen
     10 disch
      8 dische
      7 dusa
      7 disyata
      6 dusl
      5 dists
      4 duzy
      4 duzd
      4 dusmainy
      4 dizional
      4 distanqm
      4 dist
      4 disme
      4 dischmann
      3 duz-d
      3 dusme
      3 dusmatim
      3 dusmata
      3 dusma
      3 dusi
      3 disy
      3 distqm
      3 distim
      3 diss
      3 disl
      3 disa
      2 duzak
      2 dustra
      2 dusman
      2 dusiiie
      2 dusd
      2 dusc
      2 dizionalis
      2 disyehe
      2 distS
      2 diste
      2 disra
      2 disque
      2 disi
      2 discover
      2 disches
      2 disc
      1 duz-yaStay
      1 duzyairya
      1 duzvarsttm
      1 duzvarstana
      1 duzvarsSanq
      1 duzvarsnati
      1 duzvarmanhS
      1 duzvari
      1 duzvarHm
      1 duz-varana
      1 duz-vandrav
      1 duzvalanA
      1 duzvaHta
      1 duzvacanhS
      1 duz-va
      1 duzuxta
```


## [2026-09-04T22:43:50.987Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"duzak\" BRT.txt | head",
 "description": "Find duzaka in Bartholomae"
}
```


### [2026-09-04T22:43:51.033Z] TOOL RESULT

```
13811:•  j.  duzaka-  m.  (gemeiner  oder  Spott) Name  des  sfis  va»AaparS {'\gi\')*^:  spämm .  .  yim  vankäpanm  (sd)  yim  tnasyaka avi  duzvacanhS  'k>m  nama  aojaitt  V.  ig.  2.
13812:*>   Vgl.    Bd.  74-  19:    J'^a^   (in    Aw.-Buchst.) i/  xärpuSt   (=  np.  xStpasi  'Igel')  i^änend',    lg. £Ü    gilt    der    Igel    als    .ipezi elter   Gegner    der Ameisen ;  iäiak  fa  AamislJriA  1  mör  i  i/änai  t:s da    eslel,    H^ön   xdwet   ku    iälai    Aar  *iärak  *i  1 andar  mar  xSHoi  i  mizet  (ü)  lOCO  mar  iaHft. KorapA.   —   Et.?    Vgl.    HORN   KZ.  J^.  437, 1 HBM.AGT.AI4l.VI!.Va/+»fl*fl.'derRch]imme Haken  (Stacheln)  hat'7  -  mp.  (Pü.):  iüSal;  np.  I £uia;  A3;similation  der  silbenanl.  Kons. ■  j.  duzakö.sayana-  Adj.  'wo  der  Auf- enthalt, dieHeimat  desIgels  isf :  i'alk^ntim (sd)  yim  -mm  V,  /.  9.
20830:—  N.-APn,:  vjspi..yä  h?nti  haptöMars- vShva  Yt.  6.  3;  —  dama  .  .  ya  k?nti  sp?n- tahe  mainySus  Yt,  6.  a ;  —  draomJbyS  .  , y  ä  aism3  . .  drävayäi  Y.  57.  a  5 ;  —  ASm, ; ../anal  azim  srvar»m yim  (s.II)  asps^anm .  .  yim  upairi  *vis  ''raooai  yim  upairi ktnsäsp»  .  .  pitam  pacata  Y,  5. 1 1 ;  Yt /4.  7,  9,  70.66;  —  va^am yim  (&,'n.)  vär?- hrayrum  yim  öarat  .  .  %raltaonl!  yim^ barat  ..  Ytig-^it;  8.6,  77.15,  '4-39*. 48,  ig.  35,  81;  —  mi'^rfm  ..yim  yazsnte daiAhupatayB  YL  /0.8;  11,47,  66,  68,83  f.^ 88,  89,  103,  109,  123,  8.  5,  36,  41,  44', 48,  7_5. 147,  Aog.  77;  —  spänam  ..yim (s.  II)  vavkäpar^m  yim  ..  duzak^m  nama aojaite  V.13.  2;  6,  18. 15;  —  ASf.:  avqm vanqm  yqm(s.11)  salnahe  yS  hiStaüe  mai- äüw  srayanhö  ..yqm  upairi  urvaranqm  .. taoxma  nt^ayal  yx.  12.  17;  —  arltis  ..yqm *ai9hyeiti  avi.mi%riS  Yt/o.  20;  21,  5.  6;
```


## [2026-09-04T22:44:02.394Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13780,13815p' BRT.txt | grep -n -E \"^[^a-zA-Z]*7[0-9][0-9]\" ; echo \"---\"; sed -n '13795,13830p' BRT.txt | cut -c1-200",
 "description": "Find column numbers near duzaka in Bartholomae"
}
```


### [2026-09-04T22:44:02.457Z] TOOL RESULT

```
14:755
17:756
---
duzuxta-
756
•  j.  dus.sravah'  Adj.  'der  einen  üblen Rur,  Leumund  hat,  Su7KXr)j^.
Ableit.  (s.  auch  diuLir').
•  j.  duS.sravahyä-  f.  'Übelberiichtigtheit, übler  Leumund':  'vaMi  (NS.  oder  IS.) Y.i4.
Ableit.  aus  '*diä.sriaiak-.  —  Vgl.  lOuijravah:
—  Pä.!  dulsriw-ik,
•  g.  duä.syaoft'ana-,  j.  "Diia-  Adj.  'des Tun  Übel  ist,  des  Taten  Übel  sind':  dui- manatihe  .  .  Jusva/ar^Ae  .  .  *'^ftai'*  Y. tfj.  7;    —  yOnS  .  .  'hnaAe  H.  2.  36;  
'haiiing  duivacatihs  duidalnSng  *duimana' nhs  y.  4:p-  1 1 ;  —  yai  .  .  '^ans  (NP.)  Y. 34.');  —  dngvaiti . .  °^anai  Y.31. 15. Pü. :  duliunün.  —  0  NA.  '%iiitäi.
•  j.  du§.-ha,m.sästa-  Adj.  (fem.  '/ä-) 'schwer  zurechtzuweisen,  unlenksam':  näi- riiayäi  . .  AusJtam^äsfqyHi  .  .  jahikayäi  .  . 'tayäi  H.  2. 18-36.
SQ.:  äuiämSxt.
•  g.  duS-x^araS^-  n,  'üble  Speise"*; dar>gim  äyü  (sd.)  timanks  *°'i3m  ''. .  üble Speise"  Y.31.  20;  —  vaya.b?r?dubyB  (sd.) '%Sm  Y.5;.  6.
Pu.:  äuS^ariSn,  mit  denErl.!  tui x'ariSn  i  vat äahmd  und  kid  vUaia  (in  Aw.-Buchst.,  aus H.  2.  36)  dakend.  —  ')  Wie  sie  den  Seelen der  Gottloien  gereicht  wird;  s.  V.  4g. 
•  j.  duä-x*ar9nah-  Adj.  'übelberüchtigt': 'na  (NS.)  naStS  rasüta  asätS  asti  anuhaya (sd.)  Yt.  10.  105;  105;  —  alsmö..  "na  Yt. ^9-  95  i  —  ""''  *w^  mainyui  Vyt4S-
•  }.,    g.    dui'    Adv.,    nur    KompA.:    s.
dui\
•  j.  duzaka-  m.  (gemeiner  oder  Spott) Name  des  sfis  va»AaparS {'\gi\')*^:  spämm .  .  yim  vankäpanm  (sd)  yim  tnasyaka avi  duzvacanhS  'k>m  nama  aojaitt  V.  ig.  2.
*>   Vgl.    Bd.  74-  19:    J'^a^   (in    Aw.-Buchst.) i/  xärpuSt   (=  np.  xStpasi  'Igel')  i^änend',    lg. £Ü    gilt    der    Igel    als    .ipezi elter   Gegner    der Ameisen ;  iäi
*sayana-Ti.,  lum  V.  jiiy- ;  ai,  inj'««.!- n. 'Lager'
—  ['iL:  duliilya/:')  'mit  schlechtem  Schatten'
erl. :  mm  säyatJA  l  hi  *s3yai  1  draxiän  pa tan  val  asi;  dazu  als  Glosse:  {ait)  ii  äii  i iSfän  gffmtt.  —  ■>  Ohne  Berechtigung  vermutet FkMOller  WZKM.  4.  ZÖ2  deshalb 
•  j.  duz-aohav-  m.  'Hölle':  spmt>m  main- yüm  haca  raox^a  garö  nmäna  .  .  a/^rtm mainyäm  »nyata  haüa  'iawAi/'' Yt  Jp.  44; —  aHihm  -ianhavö  (GS.)  P.  i4.
Ableit.  (s.  daBi'\  —  Eig,  'schlechtes  Sein'  sva. 'Ort  des  schlechten  Seins',  s.  Sp.  109  m. ; falsch  BB.  15.  209.  —  Pü.:  */  an  1  vat  ajr*" ääret.  —  >)  Statt  'iaifuh
•  j.  dui£-anay-  Adj.  'der  einen  üblen  Atem, d.  i.  Geruch  hat' :  macirinam  artukanam  . . 'aininqm  V.  14.  5-
Zum  V.  an-,  —  pa.:  di^amün.
•  g.   du^-azöbä-  Adj.  'übelberufea,  be-
riichtigt":  dr^gvä  .  .  'bä  (NSm.)  Jias  a^üis lyaolianais  ähSmuits  (sd.)  Y.46.^.
ö  ist  Fjnschubvolcal,  S  JOO.  5.  —  'a-itä-  f., lum  V.  tiä-i  ai.  äAvä-  f.  -Name";  GON.  BB. 14.  II').  —  Pü.:  dusilaxmai.  —  O  Andre, mir  unglaubliche  Deutungen  bei  M
•  j.  duz-ä*ra-  n.  '(schlechtes  Atmen  sva.) Miäsbehagen':  ravash  :!fä'hnmca..asaonö stBii  qzasca  'nmia  .  .  drvatS  stuis  Y.  <V. 8.  a)  'Not,  Ungliick':  aha  apare  (sd.) ayan  '
Pü.:  duii^ärlA,  Sii.:  ahdAant.
•  j,  duzäpya-  n.  'Schwer-,  Unbeikömm- lichkeit',  mit  Akk.  (des  Obj.):  yaesam anhat  'fim  änval.psntum  "für  welche  die (^-Brücke  schwer  (beikömmlich,  sva.)  _un- überschreitba
Ableit.  aus  'dui-äfa-  Adj.  'dem  man  achwer beikommen  kann';  zumV.  a/-;  ai.  .l'urä^- Adj. —  Pii.:  *dulayäfai.  —  ')  W6rtl.:  'quorom  erit insaperabilitas  . .'.
•  j.  diiz-ita-  i)  Adj.  a)  'schwer  gangbar, schwer  zugänglich':  upa  kvirint^m  *t»m Yt.  J5.  19.  b)  'gefUhrlich'  (nur  Ab- leit.) 2)  n.  'Schwierigkeit,  Not,  Gefahr': bdiwranam  'l
Ableit  —  ai,  dunlä'  1)  Adj.  'schwierig',  i)  n. 'Not'.
i  j.  duzitctara-  Adj.  'der  gefährlichere':
'tarasea..ydha  anya  v^Aria  V.  ij. 4^;  4a-
```


## [2026-09-04T22:44:20.929Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13786,13800p' BRT.txt | cut -c1-160",
 "description": "Print lines around column markers 755/756"
}
```


### [2026-09-04T22:44:20.975Z] TOOL RESULT

```
Komp.;  *dui-^yar-,%370ii.'2\  \g\.  duiyairya- und  S  ^04  n.  9  No.  ~   ')  Them.
•  j.  duä-soDha-  Adj.  'übte,  böse  Sprüche sprechend.Verwiinschungen  aussprechend':
Hat  ml  ake  °nhake  paräca  valfaya  manS aal  ahe  ni  manS  manS  yö  ml  'nhs  hislaiU (sd.)  "so  wend  denn  ab  den  Anschlag des,  der  mich  verwü
ai.  duhiamsa-  Adj.  —  Pü.;  diäiOA'aH,  SÜ.: du!t<uz»iräh.
•  j.,  g.  duä.8astay-  i)  f  'üble  Lehre, Misslehre':  '/ii  F.  j4'\  2)  Adj.  'des Lehre  übel  ist,  Misslehrer':  -ft'/  sravä mönndat  (sd.)  Y
Pü.  (dRn.)';  du^mSlilttlh,  pa  duiämöasriih,  duilh ämöxlär  (Sü.:  diifloHfyäpilä).  —  ■)  Stammt  vll. aus  Y.  32.  9,  s.  2  und  Pu.
dby  Google
755
tiuI.sravaA-
duzuxta-
756
•  j.  dus.sravah'  Adj.  'der  einen  üblen Rur,  Leumund  hat,  Su7KXr)j^.
Ableit.  (s.  auch  diuLir').
•  j.  duS.sravahyä-  f.  'Übelberiichtigtheit, übler  Leumund':  'vaMi  (NS.  oder  IS.) Y.i4.
Ableit.  aus  '*diä.sriaiak-.  —  Vgl.  lOuijravah:
```


## [2026-09-04T22:44:30.001Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"angusta\\|anguSta\\|angu.ta\" KLN_1966.txt | head -20; echo \"=== 1971 ===\"; grep -n -i \"angusta\" KLN_1971.txt | head -20",
 "description": "Grep Klein for angusta"
}
```


### [2026-09-04T22:44:30.072Z] TOOL RESULT

```
22799:—  Malay  mangustan.
=== 1971 ===
144365:— Malay mangustan.
```


## [2026-09-04T22:44:36.769Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nprint(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['SOD'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['SNS'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\n\"",
 "description": "Show refs_online details for KLN SOD SNS BQT"
}
```


### [2026-09-04T22:44:38.704Z] TOOL RESULT

```
{
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
{
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
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


## [2026-09-04T22:44:45.719Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i in (48,49,50):\n    print('--- leaf',i,'---')\n    print(leaves[i][:2500])\nPY",
 "description": "Print Klein 1966 leaves around page 75"
}
```


### [2026-09-04T22:44:48.055Z] TOOL RESULT

```
903
--- leaf 48 ---
o peel’,  and  E.  cleave,  to  split  (q.v.)  Cp.  the  second element  in  hieroglyph,  triglyph, anaglyptic,  adj.,  pertaining  to  anaglyphs.  —  Gk. dvayX’j-TLXop,  fr.  dvdvXu-rop,  ‘wrought  in  re¬ lief’,  verbal  adj.  of  dvayX'1; :pe'-v.  See  prec.  word and  -ic.
anagogy,  n.,  mystical  interpretation  of  Scrip¬ tures.  —  Gk.  dvayoiyT),  a  leading  up  ,  fr. dvdyeiv,  ‘to  lead  up',  fr.  dvd  (see  ana-)  and  xyav, ‘to  lead’;  cp.  dycoyr),  a  leading’.  See  agent  and cp.  -agogue,  apagoge,  pedagogue,  synagogue. Derivatives:  anagog-ic,  anagog-ic-al,  adjs.,  ana- gog-ic-al-ly,  adv.
anagram,  n.,  transposition  of  the  letters  of  a word  or  phrase  so  as  to  form  another.  —  ModL.
69
anagramma,  fr.  Gk.  dvaypafapaTiapi;,  ‘a  trans¬ position  of  letters’,  fr.  dvaypappa-rUjEiv,  ‘to transpose  the  letters  of  a  word’,  which  is formed  fr.  dvd,  ‘back’  (see  ana-),  and  ypappa, gen.  ypdp.p.aT09,  ‘written  character,  letter  .  See -graph  and  cp.  grammar.
Derivatives:  anagrarnmat-ic,  anagrammat-ic-al , adjs.,  anagrammat-i-cal-ly ,  SLdv.,anagrammatism (q.v.),  anagrammat-ist, n.,  anagrammatize  (q.v.) anagrammatism,  n.,  the  making  of  anagrams.  — ModL.  anagrammatismus,  fr.  Gk.  avaypappa- xiop. 6?.  See  anagram  and  -ism. anagrammatize,  tr.  v.,  to  make  an  anagram  of; intr.  v„  to  make  anagrams.  —  Gk.  dvaypaupia- TtyEtv.  See  anagram  and  -ize. anal,  adj.,  pertaining  to,  or  connected  with,  the anus.  See  anus  and  adj.  suff.  -al. analcite,  n.,  a  white  zeolite  (mineral.)  —  Formed with  subst.  suff.  -ite  fr.  Gk.  dvaXx-fc,  ‘weak, feeble’,  fr.  dv-  (see  priv.  pref.  an-)  and  dXxr), ‘protection,  help,  strength’;  so  called  in  allusion to  the  weak  electricity  it  acquires  when  rubbed. Gk.  dXxfj  is  rel.  to  dXsxE'.v,  ‘to  ward  off’, whence  the  desiderative  verb  dXl'Eiv,  ‘to  ward off,  keep  off,  turn  away,  defend,  protect’.  See Alexander.
analectic,  adj.,  relating  to  analects.  —  See  next word  and  -ic.
analects,  also  analecta,  n.  pi.,  collected  writings; literary  gleanings.  —  Gk.  dvdXexxa,  ‘things, chosen’,  neut.  pi.  of  dvdXexxot; ,  ‘select,  choice’, verbal  adj.  of  dvaXcyEiv,  ‘to  pick  up,  gather up,  collect’,  fr.  avd  (see  ana-)  and  XeyEiv,  ‘to speak’,  prop,  ‘to  choose  (words)’,  which  is  cogn. with  L.  legere ,  ‘to  read’.  See  lecture, analemma,  n.,  an  orthographical  pr
--- leaf 49 ---
ed,  MDu.  sent,  OHG.  anut, MHG.  ant,  G.  Ente,  and  prob.  also  with  Gk. vVjaaa,  Att.  vijxxa,  Boeot.  vaaaa,  ‘duck’,  OI. atih,  ‘waterfowl’.  Cp.  Anatidae,  Nesonetta.  Cp. also  smew.
anasarca,  n.,  a  form  of  subcutaneous  dropsy. (med.)  —  Medical  L.,  fr.  Gk.  dvd  adpxa,  ab¬ breviation  of  u8p<o4i  dvd  odpxa,  ‘dropsy  through¬ out  the  flesh’;  fr.  dvd,  ‘throughout’  (see  ana-), and  adp9,  gen.  nap X09,  ‘flesh’.  See  sarco-. anaspadias,  n.,  a  condition  in  which  the  urethra opens  on  the  upper  surface  of  the  penis  (med.)
—  Medical  L.,  fr.  ana-  and  the  stem  of  orrav,  ‘to draw’.  See  spasm  and  cp.  words  there  referred  to.
Anastasia,  fern.  PN.  —  Late  L.,  fern,  of  Anasta- sius  (q.v.).
anastasis,  n.,  convalescence  (med.)  —  Medical  L., fr.  Gk.  dvdaxam?,  ‘a  standing  up’,  fr.  dvioxdvat, ‘to  make  to  stand  up’,  fr.  dvd  (see  ana-)  and icrrdvaL,  ‘to  make  to  stand’.  See  state  and  cp. apocatastasis,  catastasis,  hypostasis,  metastasis. Anastasius,  masc.  PN.  —  Late  L.  Anastasius,  fr. Gk.  ’ Avaaxdaioc,  fr.  avaaxaau;,  ‘resurrection  , lit.  a  rising  up'.  See  prec.  word  and  cp.  Ana¬ stasia.
anastomose,  tr.  v.,  to  communicate  by  anasto¬ mosis.  —  F.  anastomoser,  fr.  anastomose,  fr.  Gk. dvaax6(ji{oai9.  See  next  word.
anastomosis,  n.,  intercommunication  of  vessels  in the  animal  body  or  of  parts  in  any  branching system  (anat.)  —  Gk.  dvanTouwai-:,  ‘outlet, opening’,  fr.  dvaa-ropiouv,  ‘to  furnish  with  a mouth’,  fr.  dvd  (see  ana-)  and  ordpa,  ‘mouth’. See  stoma,  stomach.
anastomotic,  adj.  —  See  prec.  word  and  -otic, anastrophe,  n.,  inversion  of  the  usual  order  of words  (rhet.)  —  L.,  fr.  Gk.  avacrrpcupf),  ‘a  turning upside  down;  a  turning  up  or  back,  inversion’, fr.  dvaoTpdqiEiv,  ‘to  turn  up  or  back’,  fr.  dvd (see  ana-)  and  axp^ELv,  ‘to  turn’.  See  strophe and  cp.  antistrophe,  apostrophe,  catastrophe, anathema,  n.,  curse,  malediction;  a  thing  or  per¬ son  accursed.  —  L.  anathema,  fr.  Gk.  dvaDepa, ‘anything  devoted’,  later  used  in  the  sense  of ‘anything  devoted  to  evil,  an  accursed  thing’, a  later  variant  of  dvdSr,|j.x,  ‘an  offering',  lit. ‘that  which  is  set  up’,  fr.  dvaxiSivai,  ‘to  lay upon’,  which  is  formed  fr.  dvd  (see  ana-)  and xiffevai,  ‘to  put,  place’.  See  thesis  and  cp.  words there  referred  to.
Deriva
--- leaf 50 ---
��to  go  round’.  See  ambient, andantino,  adj.,  somewhat  quicker  (sometimes, slower)  than  andante;adv.,in  andantino  tempo; n.,  an  andantino  movement  (musical direction). — It.,  dimin.  of  andante.
andesine,  n.,  a  mineral  of  the  group  of  feldspars.
—  Coined  by  the  German  geologist  Wilhelm Hermann  Abich  (1806-86)  from  the  name  of  the Andes  Mountains.  For  the  ending  see  chem. suff.  -ine.
andesite,  n.,  name  of  a  family  of  rocks  ( petrogr .)
—  Coined  by  the  German  geologist  Baton  Chris¬ tian  Leopold  von  Buch  (1774-1853)  from  the name  of  the  Andes  Mountains.  For  the  ending see  subst.  suff.  -ite.
Derivative:  andesit-ic,  adj. andiron,  n.,  either  of  a  pair  of  metal  supports  for logs  in  a  fireplace.  —  ME.  anderne,  aundirne, aundiren,  fr.  OF.  andier  (F.  landier),  fr.  Gaul. *andero-,  ‘a  young  bull’  (cp.  Ir.  ainder,  ‘a  young woman’,  W.  anner,  ‘heifer’);  so  called  because andirons  were  frequently  adorned  with  the heads  of  animals.  Andiron  was  influenced  in form  by,  but  is  not  related  to,  iron.  Cp.  gridiron. andouille,  n.,  a  kind  of  sausage.  —  F.,  fr.  VL. *inductile,  neut.  of  the  adjective  *inductilis,  used as  a  noun,  fr.  L.  induclus,  pp.  of  inducere,  ‘to introduce’;  see  induce.  Andouille  must  have  de¬ noted  originally  the  filling  that  was  ‘introduced’ into  the  sausage.
andr-,  form  of  andro-  before  a  vowel.
Andrew,  masc.  PN.  —  OF.  Andreu,  Andrieu  (F. Andre),  fr.  L.  Andreas,  fr.  Gk.  ’  AvSpsac,  which is  rel.  to  AvSpeToi;,  ‘manly’,  fr.  avljp,  gen.  avSpoi;, ‘man’.  See  andro-  and  cp.  dandy.
andrewsite,  n.,  a  hydrous  phosphate  (mineral.)  — Named  after  the  Irish  physicist  and  chemist Thomas  Andrew  (1813-58).  For  the  ending  see subst.  suff.  -ite.
Andrias,  n.,  a  genus  of  fossil  salamanders  (zool.) — •  ModL.,  fr.  Gr.  dvSpidi;,  ‘image  of  a  man’, diminutive  formed  fr.  dvfjp,  gen.  avSpoc,  ‘man’; see  andro-.  For  the  diminutive  character  of  the -nf-formative  element  see  Kretschmer  in  Glotta, 14,  84L
andro-,  before  a  vowel  andr-,  combining  form meaning  ‘man’.  —  Gk.  avSpo-,  avSp-,  fr.  avfjp, gen.  avSpfS?,  ‘man’,  which  is  cogn.  with  OI. ndram  (acc.),  ‘man’,  naryah,  ‘virile’,  Arm.  ayr, gen.-dat.  arn,  ‘man’,  Alb.  n'er,  ‘man’,  Umbr. nerus  (pi.  acc.),  ‘men’,  Sabine-L.  Nerd,  PN.,  lit. ‘strong’,  W.
```


## [2026-09-04T22:44:55.489Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (51,52):\n    print('=== leaf',i,'===')\n    print(leaves[i])\nPY",
 "description": "Print Klein leaf 51-52"
}
```


### [2026-09-04T22:44:57.608Z] TOOL RESULT

```
=== leaf 51 ===
 con¬ fusion  with  words  ending  in  -ism.
Derivatives:  aneurysm-al,  adj.,  aneurysm-al-ly, adv.,  aneurysm-at-ic,  adj. anfractuosity,  n.,  circuitousness.  —  F.  anfractu- osite,  fr.  L.  anfrdctus.  See  anfractuous  and  -ity. anfractuous,  adj.,  circuitous.  —  F.  anfractueux (fem.  anfractueuse),  fr.  L.  anfractudsus,  fr.  am- fractus,  anfrdctus,  ‘a  breaking  round;  a  turning, winding’,  fr.  am-,  shortened  form  of  ambi-, amb-,  ‘about,  around’,  and  fractus,  pp.  of frangere,  ‘to  break’.  See  ambi-  and  fraction. Derivatives:  anfractuous-ness,  n. anew,  adv.  —  Formed  fr.  a-,  ‘of’,  and  new. angaralite,  n.,  a  magnesium  aluminum  iron  sili¬ cate  (mineral.)  —  Named  after  Angara  River  in Siberia.  For  the  ending  see  subst.  suff.  -ite. angaria,  n„  a  system  of  relays  of  couriers  for  dis¬ patching  official  letters  in  ancient  Persia,  later also  in  the  Roman  empire.  —  L.,  ‘service  to  a lord’,  fr.  Gk.  ayyapeta,  ‘impressment  for  the public  service’,  fr.  ayyapot;,  ‘mounted  courier, messenger’,  of  Persian,  ult.  Semitic,  origin.  See angel.
angary,  n.,  the  right  of  a  warring  nation  to  use or  destroy  the  property  of  neutrals.  F.  an- garie,  fr.  L.  angaria.  See  prec.  word, angel,  n.  —  ME.,  fr.  OF.  angele  (F.  ange),  fr.  L. angelus,  fr.  Gk.  oiyyeXo-,  ‘messenger,  divine messenger,  angel’  (whence  the  verb  dyyeXXetv, ‘to  bear  a  message,  report,  tell’),  which  is  rel.  to dyyapo?,  ‘mounted  courier,  messenger’;  of Persian,  ult.  of  Sem.  origin.  Cp.  Akkad,  agarru, ‘hireling,  hired  laborer’,  fr.  agaru,  to  hire  , which  is  rel.  to  Aram,  agar,  eggdr,  ‘he  hired’, (whence  Arab,  ajara,  of  s.m.),  Heb.  iggereth, Aram.  igglri,  iggartd,  ‘letter’,  prop,  message Cp.  angaria,  the  first  element  in  Ingram  and  the second  element  in  evangel.  The  sense  develop¬ ment  of  Gk.  ayyapo<;,  resp.  6cyyeXo<;,  from  a Sem.  noun  meaning  ‘hireling’,  may  be  illustrated by  the  phases :  ‘hireling,  hired  messenger,  mes¬ senger’.  Gk.  dyyeXoi;  in  the  sense  of  angel ,  is a  loan  translation  of.  Heb.  mat  dkh,  messenger, divine  messenger,  angel’,  fr.  base  l-'-k,  ‘to  send  . Derivatives:  angel-ic,  adj.,  angelica  (q.v.),  angel- ic-al,  adj.,  angel-ic-al-ly,  adv.,  angel-ic-ize,  tr.  v., angel-ize,  tr.  v.
Angela,  fem.  PN.  —  Fem.  of  L.  angelus,  ‘angel’. See  prec.  word  and  cp.  angelica,  Angelina, angelfish,  n.  —  The  name  is  prob.  due  to  the  mis¬ reading  of  the  Dutch  name  of  this  fish  zeeegel, lit.  ‘sea  urchin’,  as  zeeengel,  ‘sea  angel’  (cp.  its French  name  ange  de  mer),  a  mistake  suggested by  the  winglike  fins  of  this  fish, angelic,  adj.  —  F .angelique,  fr.  L.  angelicus,  fr.  Gk. dyysXixoc,  ‘angelic’,  fr.  avyeXo;.  See  angel  and -ic.
Angelica,  fem.  PN.  —  Fem.  of  L.  angelicus,  ‘an¬ gelic’.  See  prec.  word  and  cp.  Angela,  Angelina. Angelica,  n.,  a  genus  of  plants  (bot.)  —  ModL., lit.  ‘the  angelic  (herb)’,  fr.  L.  ( herba )  angelica, fem.  of  angelicus  (see  prec.  word);  so  called because  of  its  medicinal  properties.
Angelina,  fem.  PN.  —  Dimin.  of  Angela  (q.v.). angelo-,  combining  form  meaning  ‘angel’.  See angel.
angelolatry,  n.,  the  worship  of  angels.  —  Com¬ pounded  of  angelo-  and  Gk.  -XaxpEia,  -Xaxpta,
fr.  Xa-pela,  ‘hired  labor,  worship’.  See  -latry. angelot,  n.,  1)  a  gold  coin ;  2)  a  sort  of  cheese  made
in  Normandy;  3)  a  musical  instrument.  — OF.,  dimin.  of  angele,  ‘angel’.  See  angel, anger,  n.  —  ME.,  fr.  ON.  angr,  ‘sorrow,  afflic¬ tion’,  rel.  to  ON.  ongr,  OE.  enge,  ‘narrow,  pain¬ ful’,  OS.  engi,  MDu.  enghe,  Du.  eng,  OHG.  an-
gi,  engi,  MHG.  enge,  G.  eng,  Goth,  aggwus, ‘narrow’,  and  cogn.  with  OI.  amhu-,  ‘narrow’, arrihah,  ‘anguish,  need,  anxiety’,  Avestic  qzah-, ‘distress,  oppression’,  Gk.  ayyeiv,  ‘to  squeeze’ (esp.  the  throat),  ‘strangle,  throttle,  hang’, ayyovY),  ‘strangling,  hanging;  rope’,  ivyi, ayyou,  ‘near’  (lit.  ‘narrow’),  anaov  (for  *<5iyy-iov), ‘nearer’,  L.  angere,  ‘to  press  together,  throttle, torment’,  angustus,  ‘narrow’.  Arm.  anjuk,  ‘nar¬ row’,  OSlav.  qzQ,  qziti,  ‘to  narrow,  compress’, qzota,  ‘narrowness’,  'qzosti,  ‘a  narrowing,  nar¬ rowness’,  qziiku,  ‘narrow’,  Lith.  ahkstas,  ‘nar¬ row’,  fr.  I.-E.  base  *angh-,  ‘to  narrow,  com¬ press’  ;  the  corresponding  Celtic  base  is  *engh-, *%gh-,  whence  Bret,  enk ,  ‘narrow’,  Ir.  cumung, ‘narrow’,  Ir.,  W.  ing,  ‘distress’.  Cp.  agnail,  an¬ gina,  anguish,  anxious,  and  the  second  element in  cynanche,  quinsy,  squinancy,  Orobanche. Derivatives:  angr-y,  adj.,  angr-i-ly,  adv.
anger,  tr.  v.  —  ON.  angra,  fr.  angr,  ‘anger’.  See anger,  n.
angina,  n.,  inflammation  of  the  throat;  quinsy.  - — L.  angina,  ‘quinsy’,  prob.  a  loan  word  fr.  Gk. iyyovr),  ‘a  throttling,  strangling,  hanging'.  The form  angina  (instead  of  *aneina)  is  due  to  the influence  of  angere,  ‘to  throttle’.  See  anger, tt.,  and  cp.  words  there  referred  to.
Derivative:  angin-al,  adj.
angio-  before  a  vowel  angi-,  combining  form meaning  ‘covered  by  a  seed  or  blood  vessel’,  as in  angiosperm.  —  Gk.  dyyeio-,  fr.  dyyeTov, ‘vessel’,  fr.  Syyo?,  ‘vessel’,  a  word  of  uncertain origin.  Cp.  the  second  element  in  Hydrangea, sporangium,  synangium.
angiology,  n.,  that  branch  of  anatomy  which deals  with  the  blood  vessels.  —  Compounded of  angio-,  and  Gk.  -Xoyia,  fr.  -Xoyoc,  ‘one  who speaks  (in  a  certain  manner);  one  who  deals (with  a  certain  topic).  See  -logy, angioma,  n.,  a  tumor  consisting  of  dilated  blood vessels  (med.)  —  Medical  L.,  formed  with  suff. -oma  fr.  Gk.  ayysiov,  ‘vessel’.  See  angio-. angiosperm,  n.,  name  of  a  large  class  of  plants which  has  its  seeds  inclosed  in  an  ovary.  — Coined  (in  the  Modern  Latin  form  Angiosper- tnae)  by  Paul  Hermann  in  1690  fr.  Gk.  dyyeiov, ‘vessel,  receptacle’  and  cmeppia,  ‘seed’.  See angio-  and  sperm.
Derivatives :  angiosperm-al,  angiosperm-atous, angiosperm-ic,  angiosperm-ous,  adjs. angle,  n.,  comer.  —  F.,  fr.  L.  angulus,  ‘angle, comer’,  which  is  cogn.  with  Arm.  angiun,  anki- un,  OSlav.  qg(u)lu,  ‘comer’,  OSlav.  qkotu, ‘hook’,  Lith.  anka,  ‘loop’,  OI.  angam,  ‘limb’, angulih,  angurih,  ‘finger,  toe’,  angusfhdh,  ‘big toe,  thumb’,  Avestic  angushta-,  ‘toe,  finger’,  OI. ankah,  ‘hook;  bent’,  ancati,  ‘bends,  curves’,  Gk. a'f/.oc,,  ‘a  bend,  hollow’,  dyxtov,  ‘elbow’,  dyxuXo?, ‘crooked,  curved’,  SyxOpa,  ‘anchor’,  L.  ancus, ‘crooked,  curved’,  OE.  ancleo,  ancleow,  ‘ankle’, OE.  anga,  OHG.  ango,  ‘hook’.  All  these  words derive  fr.  I.-E.  base  *ang-,  resp.  *anq-,  ‘to  bend’. Cp.  angle,  ‘fishhook’,  Angle,  anchor,  ancon, angula,  angular,  ankle,  ankylosis,  and  the  second element  in  triangle.  Cp.  also  the  second  element in  sarangousty.  The  above  I.-E,  words  stand  in gradational  relationship  to  Gk.  oyxo?,  L.  un¬ cus ,  ‘hook’,  Mir.  ecath,  ‘fishhook’;  cp.  Uncaria, unciferous,  uncinal,  uncinate,  uncinus,  uncus, aduncus,  Redunca.
angle,  n.,  a  fishhook.  —  OE.  angel,  fr.  anga, ‘hook’,  rel.  to  ON.  ongull,  OHG.  angul  (MHG., G.  angel),  ‘fishhook’,  and  cogn.  with  L.  ancus, ‘crooked,  curved’,  uncus,  ‘hook’.  See  angle, ‘corner’.
Derivatives:  angle,  tr.  and  intr.  v.,  angl-er,  n., angl-ing,  n.
Angle,  n.,  member  of  a  Teutonic  tribe  that  came  in the  5th  century  from  what  is  now  known  as Schleswig-Holstein  to  Britain  and  conquered  it. —  L.  Anglus,  pi.  Angli,  of  Teut.  origin.  Cp.  OE. Angle,  Engle,  prop,  ‘the  people  coming  from Angul  ( =  ON.  Ongull),  ‘a  hookshaped  district in  Schleswig’,  fr.  angul  (=  ON.  ongull),  ‘fish¬ hook,  angle’,  which  is  rel.  to  anga,  OHG.  ango, ‘hook’.  See  angle,  ‘fishhook’,  and  angle,  ‘comer’, and  cp.  English,  Anglican,  Anglo-Saxon, anglesite,  n.,  a  mineral  containing  lead  sulfate.  — Coined  by  the  French  mineralogist  and  physi¬ cist  Francois  Sulpice  Beudant  in  1832;  so  called by  him  in  allusion  to  the  fact  that  it  was  dis¬ covered  by  Withering  in  Anglesey  (in  1783). For  the  ending  see  subst.  suff.  -ite.
Anglican,  adj.  and  n.  —  ML.  Anglicanus,  fr.  An- glicus,  ‘English’,  fr.  Late  L.  Anglus.  See  Angle and  -an.
anglice
76
anglice,  adv.,  in  English.  —  ML.  Anglice,  fr.  Ang- licus.  See  prec.  word.
Anglicism,  anglicism,  n.  —  Formed  with  suff. -ism  fr.  ML.  Anglicus.  See  Anglican.
Anglicize,  anglicize,  tr.  and  intr.  v.  —  Formed with  suff.  -ize,  fr.  ML.  Anglicus.  See  Anglican. Derivative:  angliciz-ation ,  n.
Anglo-,  combining  form  meaning  ‘English’.  — Fr.  Late  L.  Angli,  ‘the  English’.  See  Angle, Anglo-Saxon.
Anglomania,  n.,  a  mania  for  what  is  English.  — Compounded  of  Anglo-  and  Gk.  [zavla,  ‘mad¬ ness,  frenzy’.  See  mania.
Derivative:  Anglomani-ac,  adj.
Anglophile,  Anglophil,  n.,  a  friend  of  England  or the  English;  adj.,  friendly  to  England  or  the English.  —  Compounded  of  Anglo-  and  Gk. <plXo?,  ‘friend’.  See  -phile,  -phil.
Anglophobe,  n.,  one  who  fears  or  hates  England or  the  English.  —  Compounded  of  Anglo-  and Gk.  -<p6[lo<;,  fr.  tp ‘fear’.  See  -phobe. Derivative:  Anglophob-ic,  adj.
Anglophobia,  n.,  fear  or  hatred  of  England  or  the English.  —  Compounded  of  Anglo-  and  Gk. -cpopix,  ‘fear  of’,  fr.  96(309,  ‘fear’.  See  -phobia. Derivative:  Anglophob-ic,  adj.
Anglo-Saxon,  n.  —  ML.  Anglo-Saxones,  fr.  ear¬ lier  Angli  Saxones,  ‘the  English’,  fr.  L.  Angli, ‘the  Angles’,  in  Late  L.  ‘the  English’,  and  L. Saxones ,  ‘the  Saxons’,  in  Late  L.  the  English  . Accordingly  the  term  Anglo-Saxon  is  tautolog¬ ical,  inasmuch  as  both  elements  of  this  com¬ pound  denote  ‘the  English’.  See  Angle  and Saxon.
angola,  n.  —  Corruption  of  angora, angora,  n.,  1)  an  Angora  cat;  2)  Angora  wool  or anything  made  of  it.  —  Named  from  the  town Angora  (now  Ankara)  in  Asia  Minor,  fr.  L.  An- cyra ,  fr.  Gk.”Avy.0px,  fr.  ayxupot,  ‘anchor  .  See anchor.
angostura,  n.,  a  bitter  aromatic  bark.  —  Short¬ ened  fr.  angostura  bark,  lit.  ‘bark  of  the  tree growing  at  Angostura' ,  now  Ciudad  Bolivar,  in Venezuela,  on  the  narrows  of  the  Orinoco  River; so  called  fr.  Sp.  angostura,  ‘a  narrow  pass’,  fr. angosto,  fr.  L.  angustus,  ‘narrow’.  See  anguish, n.,  and  -ure.
angrite,  n.,  a  meteorite  stone.  —  Named  after Angra  dos  Reis  in  Brazil.  For  the  ending  see subst.  suff.  -ite.
angry,  adj.  —  Formed  fr.  anger  with  suff.  -y  (re¬ presenting  OE.  -ig).
Derivatives:  angri-ly,  adv.,  angri-ness,  n. angstrom  unit,  angstrom,  n.,  unit  of  length  equal to  one  hundred-millionth  of  a  centimeter;  used to  measure  the  wavelengths  of  light.  —  Named after  the  Swedish  physicist  Anders  Jonas  Ang¬ strom  (1814-1874).
Anguidae,  n.  pi.,  a  family  of  lizards  (zoo/.)  — ModL.,  formed  with  suff.  -idae  fr.  L.  anguis, ‘serpent,  snake’.  See  anguine.
Anguilla,  n.,  a  genus  of  fishes,  the  common  eel
(iehthyol.)  —  L.  anguilla ,  ‘eel’,  prop,  ‘the  snake¬ like  fish’,  fr.  anguis,  ‘snake’;  see  next  word.  Cp the  cognate  Gk.  eyzeau?  (see  Encelia),  OPruss. angurgis,  Lith.  ungurys,  OSlav.  *qgor[  (appear¬ ing  in 
=== leaf 52 ===
 Russ,  ugori,  Pol.  wfgorz),  ‘eel’,  which  all mean  derivatively  ‘the  snakelike  fish’.  It.  an¬ guilla,  F.  anguille,  Sp.  anguila,  Port,  enguia  and prob.  also  OSlav.  qgulja,  fegulja,  ‘eel’,  derive  fr.
L.  anguilla.
anguine,  adj.,  pertaining  to  a  serpent.  —  L.  an- guinus,  fr.  anguis,  ‘serpent,  snake’,  which  is  cogn. with  Arm.  auj,  oj,  Lith.  angis,  OPruss.  angis, Lett,  itodze,  Russ,  az,  Pol.  wqz,  and  prob.  also with  01.  ahih,  Avestic  azish,  ‘snake’,  Gk.  'iyiQ, ‘viper’.  See  echidna  and  cp.  Anguidae,  Anguilla, Anguis.  Cp.  also  Ahi,  Encelia,  ask,  ‘water  newt’. For  the  ending  see  suff.  -ine  (representing  L. -inus).
anguineous,  adj.,  serpentlike.  —  L.  anguineus,  fr. anguis,  ‘serpent’ ;  see  prec.  word.  For  E.  -ous,  as equivalent  to  L.  -us,  see  suff.  -ous.
Anguis,  n.,  a  genus  of  lizards,  the  blindworm (zoo/.)  —  L.  anguis,  ‘serpent,  snake’.  See  an¬ guine.
anguish,  n.  —  ME.  anguise,  angoise,  fr.  OF.  an- guisse,  angoisse  (F.  angoisse ),  fr.  L.  angustia  (in classical  Latin  used  mostly  in  the  pi.),  ‘narrow¬ ness,  deficiency’,  fr.  angustus,  ‘narrow  ,  fr.  an- gere,  ‘to  throttle,  torment’.  See  anger  and  words there  referred  to  and  cp.  esp.  angostura. anguish,  tr.  and  intr.  v.  —  OF.  anguissier,  an- goissier  (F.  angoisser),  fr.  anguisse,  angoisse.  See prec.  word.
Derivative:  anguish-ed,  adj. anguishous,  adj.,  causing  anguish;  anguished, anxious,  (obsol.)  —  OF.  angoissos ,  fr.  VL.  *an- gustidsus,  fr.  L.  angustus,  ‘narrow  .  See  an¬ guish,  n.
Derivative:  anguishous-ly,  avd. angula,  n.,  a  measure  in  ancient  India,  corre¬ sponding  to  1.05  inches,  lit.,  ‘finger’.  —  OI. ahgulah,  ‘finger’,  rel.  to  artgitlih,  angurih,  ‘finger, toe;  angusthdh,  ‘big  toe,  thumb’,  ahcali,  he bends,  curves’,  and  cogn.  with  Gk.  d'^xcav,  el¬ bow’,  L.  ancus,  ‘crooked,  curved’,  angulus, ‘angle,  corner’.  See  angle,  ‘corner’, angular,  adj.  —  L.  angularis,  ‘having  corners  or angles’,  fr.  angulus.  See  angle,  ‘corner  ,  and  -ar. Derivatives:  angular-ity,  n.,  angular-ly,  adv., angular-ness,  n.
angulate,  adj.  —  L.  angulatus,  pp.  of  angulare, ‘to  make  angular’,  fr.  angulus.  See  angle,  ‘cor¬ ner’,  and  adj.  suff.  -ate.
anguria,  n.,  the  gourd ;  the  watermelon.  —  ModL., fr.  Late  Gk.  aYvoofi-GV,  ‘watermelon  ,  which derives  fr.  Pers.  angarah.  See  gherkin.
Angus,  masc.  PN.  —  Scot.,  rel.  to  Ir.  Aonghus, a  compound  whose  two  elements  are  cognate with  E.  one,  resp.  choice, anhelation,  n„  panting,  asthma  (archaic).  —  F. anhelation,  fr.  L.  anheldtionem,  acc  of  anhelatio, ‘difficulty  of  breathing,  panting’,  fr  anhelatus.
77
animism
pp.  of  anhelare,  ‘to  breathe  with  difficulty’,  which is  prob.  compounded  of  pref.  an-,  ‘up,  upward’ (see  ana-),  and  helare,  ‘to  breathe’,  which  prob. stands  for  *anslare,  fr.  I.-E.  base  *an-,  ‘to  blow, breathe’.  See  animus  and  cp.  exhale,  inhale.  For the  ending  see  suff.  -ation. anhistous,  adj.,  with  no  recognizable  structure (biol.)  —  Formed  with  suff.  -ous  fr.  priv.  pref. an-  and  Gk.  laroq,  ‘tissue’,  which  stands  for *aicszbc,  and  lit.  means  ‘that  which  makes  to stand’,  from  the  stem  of  {<rn][u  (for  *o(<rr/)[xi),
‘1  make  to  stand’.  See  histo-  and  cp.  the  second element  in  Actinistia.
anhydride,  anhydrid,  n.,  an  oxide  which  is  capable of  forming  an  acid,  if  added  to  water  (chem.)  — Formed  with  suff.  -ide  resp.  -id,  fr.  Gk.  cNoSpo;, ‘waterless’.  See  anhydrous, anhydrite,  n. ,  anhydrous  calcium  sulfate  (mineral.) —  Formed  with  subst.  suff.  -ite  fr.  Gk.  avuSpop, ‘waterless’.  See  next  word  and  cp.  prec.  word, anhydrous,  adj.,  containing  no  water  (chem!)  — Gk.  avuSpop,  ‘waterless’,  fr.  av-  (see  priv.  pref. an-)  and  u§o>p,  ‘water’.  See  hydro-.  For  E. -ous,  as  equivalent  to  Gk.  -op,  see  suff.  -ous. ani,  n.,  any  of  certain  black  birds  of  the  cuckoo family.  —  Sp.  ani.  Port,  ani,  fr.  Tupi  ani. anicut,  annicut,  n.,  a  dam  (Anglo-lnd.)  —  Tamil anai  kattu,  ‘dam  building’, anigh,  adv.,  new  (pseudo-archaic).  —  Formed on  analogy  of  afar,  etc.,  fr.  a-,  ‘on’,  and nigh.
anights,  adv.  ( archaic )  —  Formed  fr.  OE.  on nihte;  see  a-,  ‘on’,  night,  and  the  adv.  suff.  -s. anil,  n.,  1)  a  West  Indian  shrub,  from  which  in¬ digo  is  made;  2)  indigo.  —  Port,  anil,  fr.  Arab. an-ntl,  assimilated  fr.  al-nil,  fr.  al-,  ‘the’,  and nil,  ‘indigo’,  fr.  Pers.  nila,  ult.  fr.  OI.  nili,  ‘indi¬ go’,  fr.  ntlah,  ‘dark  blue’.  Cp.  lilac. Derivatives:  anil-ic,  adj.,  anil-ide,  n.,  aniline (q.v.)
anile,  adj.,  like  an  old  woman.  —  L.  anilis,  ‘per¬ taining  to  an  old  woman’,  fr.  anus,  gen.  anus, ‘old  woman',  from  the  I.-E.  imitative  base  *an-, whence  also  Hitt,  annash,  ’mother’,  hannash, ‘grandmother’,  Gk.  avvip,  ‘grandmother’, Lith.  ahyta,  ‘mother-in-law’,  OPruss.  ane,  ‘old mother’,  OHG.  ano,  MHG.  ane,  an,  ‘grand¬ father,  great  grandfather’,  OHG.  ana,  ‘grand¬ mother,  great  grandmother’,  G.  Ahnen,  ‘ances¬ tors’,  OHG.  eninchili  (whence  MHG.  eninkel, enenkel,  G.  Enkel),  ‘grandson’,  prop,  dimin. of  OHG.  ano,  ‘great  grandfather'.  Cp.  the  first element  in  Olaf.
Derivative:  anile-ness,  n. aniline,  also  anilin,  r„,  an  oily,  poisonous  liquid, C6H,N A2  (chem.)  —  Coined  by  C.  J.  Fritzsche in  1841  fr.  anil  and  chem.  suff.  -ine,  resp.  -in. Derivative:  aniline,  anilin,  adj. anility,  n.,  quality  of  being  anile.  —  L.  anilitas, 'the  old  age  of  a  woman,  anility’,  fr.  anilis.  See anile  and  -ity.
animadversion,  n.,  criticism;  blame.  —  L.  ani-
madversid,  gen.  -onis,  ‘perception,  observation, attention’,  fr.  anirnadversus,  pp.  of  animadver- tere.  See  animadvert  and  -ion.
Derivative:  animadversion-al,  adj, animadversive,  adj.,  percipient.  —  Formed  with suff.  -ive  fr.  L.  anirnadversus,  pp.  of  animadver- tere.  See  next  word.
Derivative:  animadversive-ness,  n. animadvert,  intr.  v.,  to  criticize,  blame,  censure. —  L.  animadvertere,  contraction  of  animum  ad- vertere,  ‘to  direct  one’s  mind,  attend’,  fr.  ani¬ mum,  acc.  of  animus,  ‘mind’,  and  advertere,  ‘to turn  toward’.  See  animus  and  advert, animal,  n.  —  L.,  lit.  ‘a  living  being’,  fr.  animale, neut.  of  animalis,  ‘of  air,  living’,  fr.  anima, ‘breath  of  air,  air,  breath,  soul,  life’;  see  animus and  adj.  suff.  -al.  For  sense  development  cp.  Gk. £<oov,  ‘animal,  which  is  rel.  to  tj&W),  ‘life’,  and OE.  deor,  ‘a  wild  animal’,  lit.  ‘a  breathing  being’, which  is  cogn.  with  OSlav.  duchu,  ‘breath, spirit’,  dusa,  ‘soul’.  Cp.  also  Heb.  hayydh,  ‘wild animal,  beast’,  which  is  rel.  to  hdydh,  ‘he  lived’, hayyim,  ‘life’.
animal,  adj.  —  L.  animalis,  ‘of  air,  living,  ani¬ mate’.  See  animal,  n.
animalcular,  adj.  —  Formed  with  suff.  -ar  fr.  L. aninialculum.  See  next  word, animalcule,  n.,  a  very  small  animal,  esp.  one  per¬ ceptible  only  by  a  microscope.  —  Late  L.  ani- malculum,  dimin.  of  L.  animal.  See  animal,  n., and  -cule.
animalism,  n.,  animal  character;  the  doctrine  that man  is  a  mere  animal.  —  See  animal  and  -ism. animalist,  n.,  1)  one  who  believes  in  animalism; 2)  an  artist  representing  animals.  —  See  animal and  -ist.
animalize,  tr.  v.,  to  make  like  an  animal.  —  See animal  and  -ize.
Derivative:  animaliz-ation,  n. animate,  tr.  v.,  to  give  life  to,  to  enliven.  —  L. animatus,  pp.  of  animate,  ‘to  fill  with  air  or breath,  to  animate’,  fr.  anima.  See  animus  and verbal  suff.  -ate.
Derivatives:  animat-cd,  adj.  animat-ed-ly,  adv., animut-er,  n.,  animat-ing,  adj.,  animat-ing-ly, adv.,  animation,  animalism  (qq.v.) animate,  adj.,  living.  —  L.  animatus,  pp.  of  ani- mare.  See  animate,  v.
Derivatives:  animate-Iy,  adv.,  animate-ness,  n. animation,  n.,  life;  vivacity.  —  L.  animatio,  gen. -onis,  ‘an  animating’,  fr.  animatus,  pp.  of  ani- mare.  See  animate  and  -ion. animatism,  n.,  the  primitive  belief  that  the  inani¬ mate  is  regarded  as  if  it  w-ere  animated.  — Coined  by  Maretti  in  1899  in  contradistinction to  animism.  See  animate,  adj.  and  -ism. animatistic,  adj.  —  See  prec.  word  and  -istic. anime,  n.,  any  of  various  resins.  -  -  F  fr.  Sp. anime,  which  is  a  Tupi  loan  word, animism,  n.,  a  word  of  many  meanings,  but  used esp.  in  the  sense  of  ‘theory  of  the  universal  ani¬ mation  of  nature’  (Sir  Edward  Burnett  Tylor’s
animist
annulation
78
79
definition  in  Primitive  Culture,  chapter  n).  — Coined  by  the  German  physicist  and  chemist Georg  Ernst  Stahl  (1660-1734)  and  re-intro- duced  by  E.  B.  Tylor  in  1 87 1 .  See  animus  and  -ism and  cp.  animatism.
animist,  n.,  one  who  believes  in  animism.  —  See animism  and  -ist.
Derivative:  animist-ic ,  adj. animosity,  n.,  ill  will;  enmity.  —  F.  animosite ,  fr. L.  animositatem,  acc.  of  animositas,  ‘boldness, vehemence’,  fr.  animdsus ,  ‘bold,  vehement’,  fr. animus.  See  next  word,  adj.  suff.  -ose  and  suff.
-ity.
animus,  n.,  1)  intention;  2)  animosity.  —  L., ‘soul,  spirit,  mind,  courage,  wish,  desire’,  rel.  to anima,  ‘breath  of  air,  air,  breath,  soul,  life’,  and cogn.  with  Gk.  avE|jto<;,  ‘wind’,  fr.  I.-E.  base *an-,  ‘to  blow,  breathe’,  whence  also  OI.  ani-ti, ana-ti,  ‘breathes’,  ani-lah,  ‘breath’,  OIr.  anal,  W. anadl,  MBret.  (with  metathesis)  alazn,  ‘breath’, OIr.  animm,  Co.,  Bret,  eneff,  ‘soul’,  Goth,  uz- anan,  ‘to  exhale’,  ON.  anda,  ‘to  breathe’,  andi, ond,  ‘breath,  soul,  spirit’,  OE.  edian  (for  *an- j>jan ),  ‘to  breathe’,  OSlav,  vonja,  ‘smell’.  Alb. Gheg  o/.Tosk  Jh/I  sweH’,  Toch.  A  afima.  Arm. anjn ,  ‘soul’.  Cp.  animadvert,  animal,  animal¬ cule,  animate,  animosity,  equanimity,  exanimate, exhale,  inhale,  longanimity,  magnanimous,  mag¬ nanimity,  pusillanimous,  pusillanimity,  unani¬ mous,  unanimity.  Cp.  also  ahura,  anemo-,  an- helation,  asthma,  asura,  prana, anion,  n.,  a  negatively  charged  ion  ( physical chem.)  —  Gk.  aviov,  neut.  of  avicbv,  pres, part,  of  avi£vai,  ‘to  go  up’,  fr,  ava  (see  ana-) and  isvai,  ‘to  go’,  which  is  cogn.  with  L.  ire, ‘to  go’.  See  itinerate.  The  word  anion  was  in¬ troduced  into  electricity  by  the  English  physi¬ cist  and  chemist  Michael  Faraday  (1791-1867); cp.  ion,  cation.
Derivative:  anion-ic,  adj. anis-,  combining  form.  See  aniso-. anise,  n.  —  F.,  fr.  L.  anisum,  fr.  Gk.  Svlaov, ‘anise,  dill’.  Cp.  Gk.  iivrj&ov,  L.  anethum,  and see  anet.
Derivative:  anis-ic,  adj. aniseed,  n.  —  Contraction  of  anise-seed, anisette,  n.,  liqueur  flavored  with  aniseed.  —  F., dimin.  of  anise.  For  the  ending  see  suff.  -ette. aniso-,  anis-,  combining  form  meaning  ‘a  deri¬ vative  of  anise'  (chem.)  —  Gk.  avia-,  aviao-, fr.  Svlaov,  ‘anise’.  See  anise, aniso-,  anis-,  combining  form  meaning  ‘unequal, unsymmetrical’.  —  Gk.  aviao-,  fr.  itviao;,  ‘un¬ equal’,  fr.  av-  (see  priv.  pref.  an-)  and  laoc, equal’.  See  iso-.
anisomerous,  adj.,  not  isomerous  (hot.)  —  Formed fr.  priv.  pref.  an-  and  isomerous. anisotropic,  adj.,  not  isotropic  (physics).  —  Form¬ ed  fr.  priv.  pref.  an-  and  isotropic, anker,  n.,  a
```


## [2026-09-04T22:45:10.629Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^anchor,\" KLN_1966.txt | head; echo \"===\"; grep -n \"^English,\" KLN_1966.txt | head; echo \"=== 1971 anchor ===\"; grep -n -A6 \"^anchor, n\" KLN_1971.txt | head -20",
 "description": "Find anchor and English entries in Klein"
}
```


### [2026-09-04T22:45:10.699Z] TOOL RESULT

```
2686:anchor,  n.  —  ME.  anker,  fr.  OE.  ancor,  fr.  L.  an- cora,  fr.  Gk.  dyxOpa,  ‘anchor’,  which  is  rel.  to Gk.  dyxoiv,  ‘a  bend’,  dyxvXo;,  ‘crooked, curved’.  See  angle,  ‘corner’,  and  cp.  ancon, ankylosis.  Cp.  also  angora.
===
13168:English,  adj.  and  n.  —  OE.  Englisc ,  Aenglisc, ‘English’,  fr.  Engle,  Angle,  name  of  a  Teutonic tribe  that  settled  in  Britain,  prop,  ‘the  people coming  from  Angul'.  See  Angle  and  adj.  suff.  -ish. Derivatives:  English,  tr.  v.,  English-ry,  n. engorge,  tr.  v.  —  F.  engorger,  ‘to  obstruct,  block ;
=== 1971 anchor ===
14547:anchor, n. — ME. anker , fr. OE. ancor, fr. L. an - 
14548-cora , fr. Gk. dtyxupa, ‘anchor’, which is rel. to 
14549-Gk. ayxti>v, ‘a bend’, orpcoXoc, ‘crooked, 
14550-curved’. See angle, ‘comer’, and cp. ancon, 
14551-ankylosis. Cp. also angora. 
14552-
14553-Derivatives: anchor , tr. and intr. v., anchor-age ,
```


## [2026-09-04T22:45:15.508Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\n# locate line 13168 offset\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:13167])\nleaf=t[:off].count('\\f')\nprint('leaf',leaf)\nleaves=t.split('\\f')\nimport re\nprint(re.findall(r'\\b5[12][0-9]\\b', leaves[leaf]))\nprint(leaves[leaf][:200])\nPY",
 "description": "Locate Klein leaf for English entry"
}
```


### [2026-09-04T22:45:17.352Z] TOOL RESULT

```
leaf 284
['522', '523']
s).  According to  the  opinion  of  several  scholars  Endymion  was orig.  worshiped  as  a  solar  deity  and  his  name is  a  personification  of  the  Setting  Sun  Sinking into  the  Sea.  See
```


## [2026-09-04T22:45:23.545Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"ngwst\\|ngwšt\\|ngw\" SOD.txt | head -20; echo \"=== hook ===\"; grep -n -i \"hook\" SOD.txt | head -20",
 "description": "Grep Sogdian dictionary for finger and hook"
}
```


### [2026-09-04T22:45:23.608Z] TOOL RESULT

```
6083:M  }ngwst 
14420:1041  *ngwpyn    M  =¥  'nkwpyn 
14429:1044  >ngwst   M 
14591:angupen    Ongwpyn)   ©<*angupaina-;  Av. 
14601:}ngwsl 
47344:ngws-,  MP  nyws-   ©impf.  nyY(y)ws   ^nywst-, 
47636:niyosak-pat   (ngwskpt)  ^nyws'qpt'nc 
47641:5945  ngwskpt  =$  nywskpt 
=== hook ===
7675:hook,  pulling  instrument 
8464:hook,  pulling  instrument 
12900:hook 
59862:hanged,  hooked,  pierced 
60031:hanged,  hooked,  pierced 
90464:hook    2,  139,  837 
90465:hooked    7748
```


## [2026-09-04T22:45:28.319Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14415,14440p' SOD.txt; echo \"=== 14585-14610 ===\"; sed -n '14585,14610p' SOD.txt; echo \"=== hook contexts ===\"; sed -n '7665,7690p' SOD.txt; echo \"---12890\"; sed -n '12890,12910p' SOD.txt",
 "description": "Print Sogdian dictionary contexts"
}
```


### [2026-09-04T22:45:28.432Z] TOOL RESULT

```
GMS  1109;  TSP  2.927;  BSTBL;  MDii;  Bugut.  Insc. 
-w,  MDii  3R  15 

1040  }nywncy5  =*  'nywnc'yS 

1041  *ngwpyn    M  =¥  'nkwpyn 

1042  'nywst-    B  =»  'nyw'st- 

1043  'nywst'k   B 
anxwastc   ©pp.   ^nyw'st 
cut,  broken 
TSP  2.118,  119  n  pl70 

1044  >ngwst   M 
angust   Onk'wst)   ©<Av.  angusta   =»>nkwst(h) 
finger 
GMS  91,  253 

1045  >nywt   S 
anyut  ?   ©Oss.  amVud 
period,  date 
MDii  B-4R10, -y,  n  p60 

1046  'nywy-  =*  ^yw'y-1 

=== 14585-14610 ===
angryp  ?   ©impf.  mnk^yp 

Go)agitate 
VJ  1000 

1066  'nkwpyn   B,  S  ^i 
angupen    Ongwpyn)   ©<*angupaina-;  Av. 

paena 
honey  4 

TSP  19.7,  16  n  p232;  BSTBL,  Padm.  40;  KG  368 

1067  'nkwst(h)    B,  S  ^i 
angusl   OnkHvst)   ©ob.  -y;  pi.  -//    ^p>5y  >nkwst, 

}ngwsl 
finger 
BSTBL,  Padm.  42;  Dhy.  21,  29;  MDiii;  TSP  14.23, 

24,  25;ob.  pi.  >nkwstyt,  TSP  5.24 

1068  'nkyrcykh   S  (^A*  fk)<o~*» 
angcrcik  ? 

{name  of  a/i)illness 
=== hook contexts ===

1  "tfnc   M  (f^V^)^j^* 
ab/Panc  Cb'nc)  ©f.  adj.  ^•p^c,  >p}nz 

Aban,  eighth  month  of  the  year 
GMS  1274  n  2;  Hen.  Orientalia.  n94,  JRAS  1945, 
149.9 

2  "p'rp   B  aJLAS^Ta.^ 
aparP  ©<*a-barbcn>  Khot.  bira   ^'k'ys'k 
hook,  pulling  instrument 

BSTBL,  Vim.  155;  Bailey.  BSOAS  23,  25 

3  »pVYS*k   B  ->  'pr'YS* 

4  »p>st-  =»  >bst-,  ,nP'st- 

5  »p}stk   B  (tj*<jJL><4^^ 
apaste   ©<*abastaka  ©pp.  -^bynt-,  ^st-, 

top^t-,  Jbsty 
bound,  joined,  permanent 
TSP  2.550;  S  W,  C2  n  p75.26 

aPici  (»pcy)  ©<Skt.  avid 
---12890

836  »ksty(y)    M 
(o)kiste,  koste 
OcOsow,  sowing,  tilling 

BBB  570;  Tales.  470.55;  GMS  926,  931 

837  >ksyc  M,  C  (£l  <^1)J& 
akasec  ?   CksMc)  ©Av.  aka-   ^'xsyc 

hook 

Hen.  Sogdica.  30.11a 

838  >kt-   M,  C 

(o)k(o)t   Cqt-)   ©pt.  st. 
krt-,  qt- 

0o)do,  (r6»)become 
GMS  144,  148,  578,  603
```


## [2026-09-04T22:45:42.338Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('nleaves',len(leaves))\nimport re\nfor target in ['1044','837 ','1067']:\n    for i,L in enumerate(leaves):\n        if re.search(r'\\b'+target.strip()+r'\\b', L) and ('ngwst' in L or 'ksyc' in L or 'nkwst' in L):\n            print(target,'leaf',i,'printed~',i-66)\nPY",
 "description": "Locate Sogdian dictionary entry pages"
}
```


### [2026-09-04T22:45:44.720Z] TOOL RESULT

```
nleaves 645
1044 leaf 106 printed~ 40
837  leaf 97 printed~ 31
1067 leaf 107 printed~ 41
1067 leaf 323 printed~ 257
```


## [2026-09-04T22:45:51.298Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (97,107):\n    print('=== leaf',i,'===')\n    print(leaves[i][:1400])\nPY",
 "description": "Print Sogdian dictionary leaves 97 and 107"
}
```


### [2026-09-04T22:45:53.025Z] TOOL RESULT

```
=== leaf 97 ===
'krt'rzt'k

                                                                                                                            32
 815 'krt'rzt'k B                                     L^.Suir    827 'krty'kh      S                                fluf .xj-*
      Okr^rztk) ^krt'rzt'w                                           (a)krtyak
      absolutely                                                     sin, evil deed
                                                                     Sund. MHC p27.10
      TSP 6.188, 14.14 n p203; Benv. Notesiv 496;
                                                                 828 >krty>kryyh      M
        Mack, n p50, 22 BSTBL
 816 »krt'rzt'w    B                                UiW              (o)krtya-kare                                  15^'lM*

      ^krt'rzt'k                                                     performer
                                                                     Hen. Sogdica. 55.14 p57
      absolutely
      BSTBL, Padm. 61, 67; Dhy. 22(N); TSP 6.28                  829 'krtyh     B, S =» }krty>

 817 'krt'rztk =* ^rl'rzt'k                                     830 'krtyy M => >krty, >krt>y
                                                                831 >ks- B                                      *J^./<jy
 818 'krt'sp's B                              ^LUUij,^!*,            (o)kasc, (o)kos(e)?    
=== leaf 107 ===
                                                                                                                        42


 'nkrtot-

        STSC 144                                                    (fo)copy
                                                                      =^nw>ys-, m'np'ys- ?

 1064 ^kr'nt-      B                           O^AO-^
                                                                    Panjk. Insc. Livsic. HMV    p26
      angrand ©<*ham-krnta ^ngr'nd-, 'skr'nt-
      (to)cut in pieces, cut up                               1074 >np5 B                                          ?k^
      TSP 2.159; SCE 183, 223; GMS 152; BBB p58,                   anpa6
         500; AVS 112                                               footless, without feet ?
                                                                    TSP 9.133
 1065 'nkr'yp- B                      J-h~^- (oJ^lj^^y^
      angryp ? ©impf. mnk^yp                                  1075 >npst-    S                                        o^i
      Go)agitate                                                    anpast   ©pt. st. ^'np'st-, 'mpst- 'mst-, 'mpd-
      VJ 1000
                                                                    (w)fall453; Hen. Tales. 483.19; Frag. Len. 57.5
                                                                    GMS
 1066 'nkwpyn      B, S
```


## [2026-09-04T22:46:01.759Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ===\"; grep -n -i \"zuzag\\|žūžag\\|zwzg\\|jujag\\|porcupine\\|hedgehog\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n -i \"zuzag\\|zwzg\\|porcupine\\|Igel\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg for porcupine"
}
```


### [2026-09-04T22:46:01.820Z] TOOL RESULT

```
=== PHD ===
PHD.txt:125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD.txt:685:züzag [zwzk! | (N žūža)] hedgehog.
PHD.txt:2249:hedgehog xārpušt, xūkar(ag), züzag.
PHD.txt:3181:porcupine xārpušt,
PHD_mackenzie.txt:559:add    hiikar(ag) Ihwkl(k') I N xiikaraj porcupine. (not hedgehog)
PHD_mackenzie.txt:5545:xar-puAt [h)lpwst IN.......,] porcupine, hedgehog.
PHD_mackenzie.txt:5581:xiikar(ag) [hwkl(k ) I N xiikara] hedgehog.
PHD_mackenzie.txt:5868:zQ.zag [zwzk I (N ziiza)] hedgehog.
PHD_mackenzie.txt:6764:happy farrox, huram, hunsand,            hedgehog xiirpust, xukar(ag), zuzag.
PHD_mackenzie.txt:7291:pit cah, may.                              porcupine xarpust.
=== NYB ===
```


## [2026-09-04T22:46:20.501Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== v2 ژوژ ===\"; grep -n \"ژوژ\" BQT_v2_pages.txt | head -20; echo \"=== v2 leaf count ===\"; python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read(); print(len(t.split(chr(12))))\"",
 "description": "Grep Borhan-e Qate vol2 for zhuzh"
}
```


### [2026-09-04T22:46:22.946Z] TOOL RESULT

```
=== v2 ژوژ ===
23225:  ‫‪ ۴‬ره‪ :‬ژرژه ‪.‬ژوژ‪.‬‬                   ‫وموزه تا دو فرسنك‌در یی اهیر بردند به برونه » « چپارمقاله ‪۳۳‬‬
31277:  ‫‪ - ۱‬اومتا ‪ » 268۷0‬د رگرارش‬                    ‫‪۰‬‬   ‫رك ‪ :‬خارشت‬         ‫® _‬           ‫‪ ۴‬رك ‪ :‬ژوژه ‪.‬‬
31279:   ‫شده و در میان آنها از ژوژه نیز تام برده شده کوبدآن را خاریشت خوانند‪ .‬رك ‪ :‬فاب ‪۱‬ص ‪۲۱۷‬‬
=== v2 leaf count ===
684
```


## [2026-09-04T22:46:26.406Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (23225,31277):\n    off=sum(len(l)+1 for l in lines[:ln-1])\n    leaf=t[:off].count('\\f')\n    print('line',ln,'leaf',leaf,'printed~',leaf+543)\nPY",
 "description": "Map Borhan v2 lines to printed pages"
}
```


### [2026-09-04T22:46:28.538Z] TOOL RESULT

```
line 23225 leaf 393 printed~ 936
line 31277 leaf 525 printed~ 1068
```


## [2026-09-04T22:46:32.849Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (519,520,521,524,525):\n    print('=== leaf',i,'(printed ~',i+543,') ===')\n    print(leaves[i][:2500])\nPY",
 "description": "Print Borhan v2 leaves near 1063"
}
```


### [2026-09-04T22:46:34.593Z] TOOL RESULT

```
=== leaf 519 (printed ~ 1062 ) ===
                                                                                               ‫وی ‪— ۵‬‬

‫و سیب آن چنان است که چون بشار بهوا رود‬                   ‫بأکله‌البعیریمنی علفی است که آنرا شتر خورد‬
‫وسرما درو اثرکند غلیظ شود وقطر‪ :‬بارانکردد‬                ‫‪-‬نوانه‬
                                                              ‫ورزن حرس خوالند ک‬
                                                                              ‫ویعربی غلیص ب‬
‫‌ در محل فرود آمدن فعل برودت زیاده درو‬                  ‫هرزه و یاوه و بی مزه و هذبان هم‬             ‫اسزخنان‬
‫تأثیر کند اورا بفشرد وبخ بندد ® ‪ -‬و شینم را‬                                                        ‫همست ‪. ۱‬‬

‫ایز گوبند و سبب آن چنان باشد که شدت‌سرما‬
                                                         ‫راو مك ‪ -‬بثالك بواورسیدہ و میم‬
  ‫یزن‬‫ززدموا‬
          ‫هوای صافی را غلیظ کند وبخار سا‬                 ‫مفتوح بکاف‌زده ‪ ۰‬لوببارا گویند‪,‬وآن تخمی‌است‬


‫اند کی بلند شود و بربر کهای ببانات شیند واز‬                             ‫که بعربی لیا خوانند بکسر لام ‪.‬‬
‫آن قطرها پدید کردد ‪٩‬‏ ‪ -‬و باران تساتراحم‬
                                                            ‫‪ll‬‬                            ‫‪۲‬‬    ‫‪‎ 4‬ا‬
                                                         ‫' = با زای قارسی بروزن تازه »‬              ‫‪2‬‬
‫کفته‌اند ‪ -‬وجاله را نیز گوبند؛ وآن‌چیزی‌باشد‬             ‫بمعنی زار است که علف‌بی‌مزه ‪ -‬کوذابه‌ازسخنان‬
‫که ازچوب وعلف سازند‪ .‬ومش‌کهلی پرباد برآن‬                                                      ‫باشف ‪۰‬‬    ‫هرزه‬


  ‫بوسی‬‫بندند وبرآن شته از آب گذرند ‪ ۷‬؛‬                    ‫ڪر ‪= ۴‬و بررنزن لااعغررا‪ .‬چچےینه‌دان‌مرغان‬
                                                                                                 ‫ژاغر‬
‫آن مشکهای برباد را و مشکی که شناوران بر‬                                 ‫را گوبند و بعربی حوصله خوالنف‪.‬‬
                   ‫پشت بندند ژاله گویشد‪.‬‬
‫او ب=كون واو » خالس وخلاصة هر‬
       ‫‪۰‬‬                                      ‫ھ‬
                                                         ‫کیاهی است دوابی شبیه‌بانگشتان چلیاسه وزفن‪.‬‬
                                     ‫‪۰‬‬   ‫چیز را گوند‬    ‫رال ‪ » ۴‬بروزن لاله‪ .‬تگرك رااگوند‬




             ‫که چرب کوبان آ بجا شود کند زبان ‪.‬‬             ‫‏‪ ٩‬کیکه ژاژ درابد بدرکیش نشود‬
  ‫‪۰‬‬        ‫(‪FA‬‏‬   ‫فری‬   ‫«لت‬   ‫فرخی‌سستالی‪.‬‬



  ‫‪ = ۴‬زاغر (ه‪.‬م‪ ).‬عنصری باخی درخطاب بساپزید بزاغگوبد ‪:‬‬                           ‫رك‪ :‬ژاز ‪.‬‬    ‫؟‏‬
   
=== leaf 520 (printed ~ 1063 ) ===
                                          ‫بیان دوم‬

                ‫در زای فارسی باخای لقطه دار مشتمل بر دو لفت‬
                  ‫‪.‬‬   ‫ند‬
                       ‫ینیز‬
                          ‫گلهورا‬
                               ‫زاری و نا‬               ‫رخ = بفتح اول و سکون انی ‪ .‬مخفف‬
  ‫زخار ؟ = یکسر اول بر وزن شکار‬                         ‫آزخ است؛ وآن‌دانه ای باشد سخت وبی ددرکه‬
‫دراعضای آدمی بهم میرسد و آنرا بعربی تولول | بان و لعره را گوبند ‪ -‬و بممنی سختی لیز‬
                               ‫‪-‬صدای | آمده است ‪.‬‬
                                                ‫خوالنند ‪ - ۱‬وآواز حزین وآهته ؟ و‬



                                          ‫بیان سوم‬


 ‫معرب‬    ‫ار‬
          ‫وو‬‫داند‬
               ‫جته‌‬
                  ‫زو ‪ ۴‬ت شنح اول وسکون انی‪ .‬مطلق | مشهور؛ و سم اول نیز گف‬
                                   ‫‪۰‬‬     ‫ات‬      ‫‪۱‬‬     ‫را گونند‪ ,‬وآن چیزی است چبند هکه از‬              ‫صمغ‬


‫بکر اول و فتحایی» مخفف‬                        ‫‪"...‬ده‬                                               ‫‪a‬‬
 ‫زدوار ت بفتح اولبروزن و معنی‌جدوار‪ | ‎‬آژده‌است ‪ ۲‬که‌سوزن زدن وآژننه بنگه‌آسا‬
                                 ‫زدن باشد ‪۰‬‬            ‫باشد وآن دوایبی است‪‎‬‬      ‫‪ e‬که ماه بروین‬        ‫اش‪‎‬‬




                                         ‫بیان چهارم‬

              ‫زای فارسی بارای می نقطه مشتمل بر چهار لفت‬                               ‫در‬


                          ‫باشد ‪¥‬‬   ‫‪۱‬وبرخوری‬             ‫بمعنی بسبارخوردن‬     ‫بروزن زرد‬         ‫زرد‬


                           ‫ت‬                                          ‫‪.‬‬    ‫آزخ‬   ‫آزخ ‪۰‬‬   ‫رك‪:‬‬   ‫‪-‬‬   ‫‪۱‬‬


        ‫بانگ برآورد مرخ باژخ طنبور ‪.‬‬                   ‫‪ - ۴‬بوی برانگیخت کل چو عنبر اشهب‬
   ‫ترمذی‪« .‬لفت‌فری‪ )۹۷‬ورك ‪ :‬لعت‌نامه ‪.‬‬    ‫مك‬
   ‫‪ - ۴‬از اوستابی ‪( [21312‬صمغ) «یشتها ‪ ۱‬ص ‪۹۲۳‬ح‪»۱‬‬                          ‫‪ = ۴‬ژغار (ه‪.‬م‪. ).‬‬
                       ‫‪MS‬‏‬                ‫‪۷‬‬              ‫® _ رك ‪ :‬جدوار ‪.‬‬                ‫و رك‪ :‬انگزد ‪.‬‬

    ‫‪ - ۲‬در عربی ”زرد“ (بفتح اول) فروبردنلقمه است «منتهی‌آلارب» ومقلف غباث البنفت‬
                ‫را مشترك بین‌فارسی وعربی داند با تفاوت زای عربی و زای فارسی‪ .‬لفت نامه“ ‪.‬‬

=== leaf 521 (printed ~ 1064 ) ===
 ‫ژغاله‬                                                                                       ‫ها‬       ‫هی‬

 ‫ژر قا‪ - ۴‬با فا بکافلیفده‪.‬بمسنی‌عسق‬                    ‫زرف ‪ = ۲‬بروزن حرف ‪ ۰‬بمعنی عمیق‬
                    ‫وعمقیت وعمیق بودن باشد‪.‬‬            ‫است مطلقاً خواه دربا باشد و خراء چاه و خواه‬
   ‫ر‬
   ‫فدهک ›‬
        ‫لی رسی‬
             ‫ژبرگتیح‪-‬تبااای‬                            ‫رودخاله وحوض و امثال آن ‪ -‬وکنابه ازاحتیاط‬
‫عمیق واحتیاط کردن وباریك‌بینی‌باشد؟ سویمعنی‬
 ‫احتاط کننده‌هم هست؟ ‪-‬وعمقیت هرچیزرالیز‬
                                                        ‫نمودن واظر بدقت کردن وباريك‌بینی وفکردقيق‬
                                     ‫‪۴۵‬‬       ‫کون‬                 ‫لمودن هم هست‪ .‬وبعربی‌غور گویند‪.‬‬


                                              ‫بیان پنحم‬
                ‫در زای فارسی با غین نقطه دار مشتمل برشش لغت‬

‫وغازه را نیز کوبند که‬   ‫وسرخی‬   ‫ارزن بادد ‪۳ ۸‬‬              ‫غاد ‪, -‬نتم اول بورزن تفار گی‬
                                                        ‫‪,‬اهی‬
 ‫زدان برروی مالند ‪٩‬‏ و‪-‬لاف حبوانات رگاویند‬                   ‫‪-‬و‬  ‫یکنن‬
                                                               ‫‌دس‬    ‫عه رن‬
                                                                    ‫نگگ‬        ‫باشد که بدا‬
                                                                            ‫بن ج‬
                                                                          ‫مام‬
                                                           ‫ختی‬
‫عموماً و افکاورا خصوصاً ‪٩‬‏ ‪ -‬و بمعتی فرباد‬               ‫هم‌آمده است کهلقیض ستی باش ‪٩‬‏ آ‪-‬وواز‬
                        ‫وفغان هم آمده است ‪۰‬‬
                                                                 ‫بلند و فریاد سهمناك را یز کوند ‪۷‬‬

 ‫ن حواله » بمعنی‬
               ‫ژغاله ‪۱‬و=زبر‬           ‫>‬   ‫‪۵‬‬

                                                       ‫بروزن کناره ‪ .‬بان‬         ‫شر‬
                                                                                              ‫‪°‬‬   ‫‪۵‬‬




  ‫»ردی ‪ , ۲6102‬زازا ‪,[10‬‬
                       ‫‪ ۳18.‬ک‬‫ا‪-‬وستا ‪( 8]12012-‬عمیق) ‪ .‬پهلوی ‪2 2 ۲۵‬‬
   ‫‪۰‬یلکی‬‫* پلوچی انا و انز « اسدق‪ .» ۵۸۱‬استی ‪ 172‬دك ‪ .‬امت ‪ ۷۰۱‬ک‬   ‫افتانی ت‬
  ‫‪۰‬ازند‬
      ‫(هلوی ) ‪ ( ۷۳772‬عمق ) پ‬
                            ‫‪( [0‬کود) » دامغانی ‪( [10‬کاة کود)‪ .‬دراوراق مانوی ب‬
           ‫ر‪:‬هنینگه‪ .‬فپرست لفات پارسی میانه ‪, 50051 ,...‬ج ×‪.1, 1‬س ‪۰٩‬‏ ‪:‬‬                   
=== leaf 524 (printed ~ 1067 ) ===
                                             ‫بیان هشتم‬
                      ‫در رای فارسی با نون مشتمل بر هشت لغت‬
‫و یک اول یمعئی قطرء باران است ؛ و باین‬
                                                        ‫ر فك = بفتح اول بروزن چند ‪ .‬بمعنی‬
   ‫محنی بجای نون بای حطی همآ مده است (‪.)۱‬‬
                                                         ‫پاره باشد وژند ژد بمعثی پاره پارهم؟ ب‪-‬موعتی‬
‫رنکدان ‏‪ ٩‬ه پروزن سنگدان‪.‬بمعتی‬                           ‫وزچضماق‬
                                                               ‫سهتش‬
                                                                  ‫وآ‬‫خرقه کوهنه همآمده‌است ‪ ۴‬ه‬
‫زنگ وزنگاله (‪ )۲‬و جلاجل باشد؛ بواین‌معنی‬                ‫را کیزویند ؟ ‪ -‬ونام کتاب زردشت است که‬
                  ‫بحذف الف هم بنظرآمده است‬                                                    ‫بزلد اشتهار دارد ‪۴‬‬
‫ز نکله ه بورزن زلگله» سمی‌را گویند‬                       ‫زرنده = بر وزن خنده ‪ ۰‬بمعنیژنداست‬
‫که شکافته باشف حمچو‪ -‬مآ هو و گاو و گوسفند‬
                                                         ‫‪ - 8‬و هرچیزی‬                  ‫د‬
                                                                                       ‫شنه‬
                                                                                         ‫برهاوکه‬
                                                                                               ‫خهرفه وپا‬
                                                                                                       ‫ک‬
                                       ‫وامثالآن ‪۵‬‬
                                                         ‫بز رک وعظیم ومهیب را نیز کوبندهمچوژنده‌ییل‬
‫ر نګه ‪e‬‏ بقتح اول وکاف فارسی وسکون‬                                                        ‫بعنی فیل بززکه ‪. ۲‬‬
‫ثالی » آفتی است که بغله رسد " وآن‌چنان‌باشد‬             ‫ز نگ = بفتح اول پروزن رنگه ‪٠‬‏ کتاب‬
  ‫که خوشۀ غله از دانه خالی کردد و زرد شود‪.‬‬              ‫مانی قش است» وآن مشتمل برده بر تصوبرات‬
 ‫صوزن‬   ‫‪a‬‏ بقتح اول وئالی ‪ 0‬لش‬     ‫‪۰‬‬   ‫رنه‬              ‫ونقشهایی که اختراعاوست ‪ - ۷‬وچین‌وشکنجی‬
‫ویشه‬    ‫ر‬
        ‫وز‬‫لند‬
            ‫ولیش جالوران کزنده را گویند ماق‬              ‫راز کوبند که برروی واندام مردم پدیدآید‪- ۸‬‬
                       ‫(‪ )۲‬چك ‪ :‬ژنگه وژنگله ‪۰‬‬                            ‫(‪ )۱‬چك ‪ :‬باهمآمده است‬
                    ‫رك‪ :‬زلف ‪.‬‬      ‫‪۳‬‬         ‫رك‪ :‬ژللہ ‪.‬‬          ‫‪۴‬‬             ‫‪۰‬‬   ‫ژلده (ه‪.‬م‪‎).‬‬       ‫‪-‬‬     ‫‪٩‬‬

   ‫‪ -‬د
=== leaf 525 (printed ~ 1068 ) ===
 ‫زون‬                                                                                                      ‫سس‬
‫بر وزن بربان ‪ ۰‬تانشواه را گوشد‪.‬وآن تخمی‌است‬                                                           ‫وامثال آن ‪.‬‬
                ‫که بر رو‪.‬ی ‪.‬خمیر نان باشند ‪.‬‬           ‫= بکر اول و سکون ثالی‬                 ‫ژنیان ‪۱‬‬


                                               ‫بیان نهم‬
                      ‫دز زای فارسی باواو مشتمل بر بازده لفت‬

‫رو له « بنم‌اول بروزن لوله ؛ناممرغی‬                     ‫*واغار ‪ -‬بناقغطیهن‌دار بروزن‬
                                                                                   ‫ژ‬
                                                             ‫برستان بوده ‪*. ۴‬‬          ‫هوادار ‪ ۰‬لام یکی از‬

                                      ‫گومند ‪.‬‬          ‫ژور ك ‪ - ۴‬بنتم اول و رای قرشت‬
‫لویدن ‪ ۰ ۲‬با انی مجهول بر وزن‬
                            ‫ژ‬                           ‫ریگ‬       ‫وسکون انی و کاف ‪ .‬پرنده ایست سرخ‬

                                                        ‫؛ و بعضی گوبند پرنده ست‬              ‫کنجشك‬         ‫ببزرگی‬
‫جوشیدن » بمعئی درهم شدن ‪ -‬و درهم رفتن‬
                                                        ‫که سرو گردن او سرخ میباشد و او را سرخاب‬
                         ‫ویریشان گردیدن باشد‪.‬‬
                                                                                                          ‫میگومند‪.‬‬
‫بر وزن شوریده > درهم‬        ‫رو لیده ‪۸‬‬
                                                             ‫زاوی‬
                                                                ‫بیده‬
                                                                   ‫ژور" ‪ -‬با اول بثالی رس‬
‫وم شده و‪-‬آمیخته ‪ -‬وبدست مالیده‬
                             ‫ردفترهه‬                    ‫زده » خاریشت را گونند‪ ,‬وآن حالوری‬                       ‫فارسی‬
‫و پرشالرا گونند » واین هعنی را بیشتر‬       ‫شده ‪-‬‬
                                                                                             ‫‪.‬‬    ‫®‬   ‫است معروف‬

              ‫در زلف وک کل استعمال مکاند‪.‬‬                                        ‫‪۳‬‬                    ‫‪۵. ۵‬‬
                                                        ‫ژو ره ‪ » ۱‬بزای فارسی بروزن موزه‪.‬‬
‫ویده ‪ -‬با میم بروزن ژولیده‪ ,‬کشت‬
                              ‫ه‬                                          ‫باشد‪.‬‬   ‫" بمعنی زور است که خارشت‬
                   ‫وزراعت آب زده را گوید‪.‬‬                               ‫کا‬
```


## [2026-09-04T22:46:56.876Z] TOOL CALL #36: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py; echo ...; grep -n \"def \\|BQT\\|volume\" tools/ref_page.py | head -40",
 "description": "Inspect ref_page tool"
}
```


### [2026-09-04T22:46:56.927Z] TOOL RESULT

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
...
4:    python3 tools/ref_page.py BQT:918          # printed page 918 of Borhan-e Qate'
6:    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping
31:def main(argv):
37:        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
43:        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
46:        if s.get("requires_volume") and not vol:
```


## [2026-09-04T22:47:03.798Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"شترنگ\\|شطرنج\" BQT_v3_pages.txt | head -20; echo \"=== langar ===\"; grep -n \"لنگر\" BQT_v3_pages.txt | head -20",
 "description": "Grep Borhan vol3 for chess and anchor"
}
```


### [2026-09-04T22:47:03.862Z] TOOL RESULT

```
1306:آلات شطرنج را هم شاه میگونند - و کشت
1307:کردن شاه شطرنج را ‎hi ja‏ و کشت بکسی
1309:از مپرهای شطرنج را درخانه‌ای گذارند که‌بحسب
3153:‎ote )۳(‏ : شطرنجی .
3185:در برایر آن رد را ساخت و شطرنج معرب ‎OT‏
3191:وآن کیاهیباشد . . شترنگه (عطررنج)
3244:‏معرب آن شطرنج :
3247:‏همچو در سی ودو خانه است ‎GLE‏ شترنگه .
4322:‏شش خنج ‏ بروزن شطرنج؛ ‎POS‏
4469:# قطر لح - رلد: شترنگه .
17938:‎ES‏ بروزن (۳) شطرنج » بممنی
18133:از ‎tLe‏ مهره‌های شطرنج و ‎Vea OT‏ وزس
18293:۲ص ۲:۲۵۲]؛ ‎oT‏ مهر# از شطرنج که بمنزلهٌ وزیراست :
19718:که دو حریف را باهم درنرد وشطرنج وامثاآن
19789:فرهنج ‎ones‏ شطرنج ۰ بمعنی علم
22256:‏۴ - زین وزان ‎wt)‏ و شطرنج ) چند ‎oy‏ ب رکه ومه
30149:کرسنج ۴ - بر وزن شطرنج ۰ بععنی
38510:‏چو شطرنجی از عاج و از آبنوی .
40357:است که مهره‌ای ازمهره‌های شطرنج را درجابی
50819:نام شخصی است که واضم شطرنج است ؛ وبسنی
=== langar ===
33909:‎aN ia 0‏ لنگر ۰
```


## [2026-09-04T22:47:08.303Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'PY'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\nfor ln in (3185,3191,3244,3247,33909):\n    off=sum(len(l)+1 for l in lines[:ln-1])\n    seg=t[:off]\n    # find last [pdf page N]\n    m=list(re.finditer(r'\\[pdf page (\\d+)\\]', seg))\n    print(ln, 'pdf page', m[-1].group(1) if m else '?')\nPY",
 "description": "Map Borhan v3 lines to pdf pages"
}
```


### [2026-09-04T22:47:10.196Z] TOOL RESULT

```
3185 pdf page 45
3191 pdf page 45
3244 pdf page 45
3247 pdf page 45
33909 pdf page 462
```


## [2026-09-04T22:47:18.216Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'PY'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\nblocks=t.split('\\f')\ndef pdfnum(b):\n    m=re.search(r'\\[pdf page (\\d+)\\]',b)\n    return m.group(1) if m else '?'\nfor b in blocks:\n    n=pdfnum(b)\n    if n!='?' and 700<=int(n)<=712:\n        print('=== pdf',n,'printed~',int(n)+1203,'===')\n        print(b[:1800])\nPY",
 "description": "Print Borhan v3 pages 700-712"
}
```


### [2026-09-04T22:47:20.210Z] TOOL RESULT

```
=== pdf 700 printed~ 1903 ===
[pdf page 700]
[NOT OCRED - use tools/ref_page.py]

=== pdf 701 printed~ 1904 ===
[pdf page 701]
[NOT OCRED - use tools/ref_page.py]

=== pdf 702 printed~ 1905 ===
[pdf page 702]
[NOT OCRED - use tools/ref_page.py]

=== pdf 703 printed~ 1906 ===
[pdf page 703]
[NOT OCRED - use tools/ref_page.py]

=== pdf 704 printed~ 1907 ===
[pdf page 704]
[NOT OCRED - use tools/ref_page.py]

=== pdf 705 printed~ 1908 ===
[pdf page 705]
[NOT OCRED - use tools/ref_page.py]

=== pdf 706 printed~ 1909 ===
[pdf page 706]
[NOT OCRED - use tools/ref_page.py]

=== pdf 707 printed~ 1910 ===
[pdf page 707]
[NOT OCRED - use tools/ref_page.py]

=== pdf 708 printed~ 1911 ===
[pdf page 708]
[NOT OCRED - use tools/ref_page.py]

=== pdf 709 printed~ 1912 ===
[pdf page 709]
[NOT OCRED - use tools/ref_page.py]

=== pdf 710 printed~ 1913 ===
[pdf page 710]
[NOT OCRED - use tools/ref_page.py]

=== pdf 711 printed~ 1914 ===
[pdf page 711]
[NOT OCRED - use tools/ref_page.py]

=== pdf 712 printed~ 1915 ===
[pdf page 712]
[NOT OCRED - use tools/ref_page.py]
```


## [2026-09-04T22:47:24.049Z] TOOL CALL #40: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1908 --image 2>&1 | tail -60",
 "description": "Fetch Borhan page 1908 for langar"
}
```


### [2026-09-04T22:47:26.297Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1908.png
REF: BQT:1908  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 705  OCR-lang: fas

لاد و۱
لنکاك - بر وزن غمناك » سخن زعغت درجهٌ اعلی داشته بادد وبهرجا رود سنگین ی کند
و ناخوش را کویند ‎٩‏ . بعنی ناگوار و نادل چپ وبدرزق باشدیرخلاف
لنگر * بفتح اول و کاف فارسی بروزن یادبان که هردم سبکروح ودلچپ راکوند؟۴ .
بندر , آهنی باشد بسیار سنگین که کعتی را نکن * - بفتح اول و نالك بر وزن
بدان از رفتار نگاهدارند ۴ - 8 | بهمن » بمعنی کرسنگی و فاقه و روزه باشد
و جابیرانیز کوین که هن روز که هندوان موافق آبین و کیش و ملت خود
درا نجابمردم طعام دهند ۳ بجاآرند .
رای لنگوته ۱ - بنم اود و سکون ۳
- و محجریرا نیز
سنکه با ازچوب‌با خشت وکل لنگر وکاف فارسی بواو رسیده و فتح فوقالی » لنگی
که بر دور مزار بزرکان کشند و بعربی ضر دح باشد کوچکه که درویشان و ققیران و مردم
خوانند - وبمعنی تمکین و وقار هم‌آمده است- | بیمروپا بر میان بندند وبهندی نیز همین معنی
وشخصیرا| نیز کویند که درمکر وحیله وخیرکی | دارد .
۱ - من با تو سخن بلابه کویم از چه دهیم جواب لنکاك ؟
طیان هرغزی « لفت نامه » .
۴ - اسل کلمه بونانی است « تقی‌زاده . باد کار 54 ص ۰۹۲۷ در بونانی 2819۳2 ۰
لاتسنی 286072 «مرچنت؟ » و معرب آن « انجر» «تفی» » قس : فرانوی 286076 ۰ انگلسی
07۳ مآلمانی ۸8۳6۳ :
سخن لنگر و بادپانش خرد بدریا خردمند چون بگذرد .
فردوسی طوسی « لفت نامه ؟ ۰
۴ - مو آن رندم که نالم بی قلندر نه خون دیرم نه مون دیرم نه لنگر.
بابا طاهرهمدانی ۶ لغت نامه ».
۴ - « بادبانی » بمعنی حرکت سربع ( همچو نکشتی بادبان کشیده ) » و « لنگری >
بمعنی توقف ( همچون کشتی لنگرانداخته ) استعمال شود :
آسمان با کشتی‌عمرم ندارد جز دوکار : وقت شادی بادبانی » وقت محنت‌لنگری.
آنوری آپبوردی . رك : آسم مصدر بقلم نگارنده ص ۵4 .۰
۴ - مسحف « لنگپن » رك : لکهن . انندراج همان ببت سنائی را که در ؟ لکهن >
شاهد آ ورده شده» برای‌لنکن‌هم شاهد آورده است . ۱ تحقیق آست که لفت هندی‌است
مر کب از : لنگه:بالکسر بمعنی مزه و اوت بواومجپول بمعنی پناء وپرده» و فارسیان هائی بدان
ملحق نموده استعمال کنند . » « بهار عجم » در هندی 12808040 و 128801808 و هردو با تاه
هندی استعمال شود * فرهنگه لفات (۱ ردو ) » « فیروزاللغات اردو جدید ؟ +
```


## [2026-09-04T22:47:36.310Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'PY'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor b in t.split('\\f'):\n    m=re.search(r'\\[pdf page (\\d+)\\]',b)\n    if m and m.group(1)=='45':\n        print(b)\nPY",
 "description": "Print Borhan v3 pdf page 45"
}
```


### [2026-09-04T22:47:38.245Z] TOOL RESULT

```
[pdf page 45]
شتر نگ ۱« با کاف فارسی » بر وزن
و ‎gine‏ شطرلح است » و ‎OT‏ بازبی باشد ‎agate‏
‏و ‎Ke LT Sym‏ داهر هندی یا پسر او
درزمان الوشیروان اختراع کرده بود وابوزرجمهر
در برایر آن رد را ساخت و شطرنج معرب ‎OT‏
‏باشد - و بزد:
محققین تردآشاره
بجبراست وشطر نج
باختیار - ومردم
‎sill‏ کویند.
وآن کیاهیباشد . . شترنگه (عطررنج)
که بیشتر از چین‌آورند +

شتفت ‎<a‏ ارل و فتح ثالی وسکون
فا وفوقانی . بممنی ‎ath‏ و علو باشد - وسقف
‎ole‏ را نیز گویند- وپوشش هرچیز را میگویند
عموماً و پوشش عمارت و خانه و امثال ‎WaT‏
‏خمرماً ! و بکس اول و ثالی هم بنظر آمده
است ۴ .

شتکار ۴ - جتح اود بر وزن ‎Gl‏ .

)0 چك: زری شاید ؛ چش: زریرا گوشد .

—\vet—

‎fan‏ شدبار است که شکافتن زمین باشد بجهت
زراعت کردن ؛ ‎Sal Gry‏ وضم اولهم گفته‌اند.

‎)٩( ath ‏زری‎ » deo ‏بر وزن‎ = je
‏و بحاضران مجلی دهند.‎ aia glad ‏که در‎

‏شتلم ° بطم اول و انی ولام وسکون
میم ۰ بجمنی اشتلم است. و ‎OT‏ درشتی کردن
بفیر موق وبیجا وظلم‌ونه‌دی لمودن باشدیامردم.

‏شتمین ۲ » بنتح اول وسکون ابی و کسر
میم و نون ‎QSL‏ بلفت زند وپازد ‎HS)‏
‏گاه را کویند و بعربی مقعد خوانند.

‎pe‏ ۲ ۰ بنتح اول بر وزن چمن ؛ به
لت زند و پازاد (۷) بمعنی شهر باشد و بعربی
‎Aire‏ کویند.

‏شته = ‎poe‏ اول و ‎IC‏ + بسنی انکور
باشد ۸ - وهرچرز را یز گوبند که شب برآن
کذشته باشد و صباح‌خورند؟ ؛وبکراول‌وشدید
ثانی هم آمده است.

‎7

‎ws
‎Wh ‏وآن خرانی است که از‎ ath gine ‏بمعتی‎

‏من

‏”!= بفتح اول وثالیبتحتانی کشیده»

‎. ‏چك : ژندویاژند‎ (x)

‏۱ - پپلوی 6۵1۳258 , ارمنیع ‎nt? Shitranj‏ که 4۳ * ازسانسکریت ‎catur_‏
‏8 ( دارای چهارلبه باچهارحد) شامل چهار جزه: فیل,رخ " اسب , پیاده فوبلیامز ۱:۳۸۶»

‏معرب آن شطرنج :
ناجز از بیست وچهارش نبود ‎BIS‏ نرد

‏همچو در سی ودو خانه است ‎GLE‏ شترنگه .

‎. ۲۸۹ ‏لغت فرس‎ « . sat

‎cits - ۴‏ درمهذب‌الامماه پیمتی « دستهبی و « مغاک ی که بر‌ای صید شیر ساز ند
آمده > فرهنگه نظام» ‎Ken by‏ رشیدی این‌لفت را ندارد و درجهانگیری به‌عنی «بلندی ویودش
هرچیز عموماً ویوشش خانه» آمده و شاهدی ندارد , ظ . مصحف «سقف؟است .

‏۴ 2-2 شدبار < شرار ‎Base‏ .

‏6 مخنف «اشتلم» ‎Cen)‏ +

‏۴ هت ‎(Gime)‏ («.م.) در تهرالی 502121 .

‏1 - صحیفی است ازهز , 502020 ,

‎shman. shakaman‏ . پرلوی 108 ‎Sy? oS‏ ۰۸4 . ۷ - قراءتی درپولوی
که ‎oo.‏ 5847( شبر) را بعنوان 31,5 ‎shtan‏ و ‎Shatin‏ میخواندند .رك:یونکر ‎Ao‏

‎ هتس‎ : ‏رکه‎ A

‎. Cem) wilt ‏-ظ . مصحفثشبه»‎ ٩

‏*- در رشیدی

‏و جهانگری وفرهنگه تظام ‎uals‏ وشاهدی مم دیده لشده » ظ.مصحفه شینی * .

‏( برهان لاطع ‎Cow‏
```


## [2026-09-04T22:47:54.445Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt; grep -c \"\" MON_part1.txt; grep -n \"انگشت\" MON_part1.txt | head -10",
 "description": "Inspect Moin dictionary text"
}
```


### [2026-09-04T22:47:54.510Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
99339
4081:انگشتان نو از ند. 
4208:شباهت به آخر کلمات ملحق شود: انگشتال 
4268:آلاس: 5 (.) رغال» زگال؛ انگشت. 
4801:چنانکه گوهری را در انگشتری. به سلکك 
6555:تاریکی. (ا) انگشت ستبر و کو تاه دست يا با 
6556:از جانب انسی» انگشت نر انگشت بزرگد» 
7133:اثلق: ساعه [ع.] (.) (گیا.) پنج انگشت. 
8680:اخگر کشته: زغال» انگشت. 
9778:کارینات‌ها است. انگشتان پایش توسط 
9994:سرانگشت؛ دراع» رش.
```


## [2026-09-04T22:47:59.117Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^انگشت\\|انگشت: \\|انگشت (\" MON_part1.txt | head -20; echo \"=== search 'انگشت' with pahlavi ===\"; grep -n \"angust\\|angušt\\|anguSt\" MON_part1.txt MON_part2.txt | head -20; echo \"=== انگلیس ===\"; grep -n \"انگلیس\" MON_part1.txt | head -10",
 "description": "Search Moin for angosht and Engelis"
}
```


### [2026-09-04T22:47:59.205Z] TOOL RESULT

```
4081:انگشتان نو از ند. 
15114:انگشته» هسته. 
18379:انگشت: اقهوه (.) زغال» زگال. 
18380:انگشت: ۱ (.) مر یک از ات 
18384:انگشتال: ۸7:52 (رص.) مردم صعف و 
18387:انگشتانه: ۰ (6-)2:0۵051202 (امر .) ۳ فلری 
18392:انگشت به‌لب: -06-.۸ (ص‌مر.) متحیر» 
18395:انگشت پیچ: 200۵5۱-6 (ص مر .) هر چبز 
18406:انگشت 
18408:انگشت شان: نانو د» محو. 
18410:انگشت سس 2.0 (مسص‌ل.) 
18411:انگشت گذاشتن ۰ انتخاب کردن آن؛ 
18420:انگشت‌نگاری: -] 2-1622 (حامص.) 
18423:انگشت‌نسما(ی): (02)6,0(018)۷-.2 
18425:انگشت نشان» انگشت کش. کسی که به بدی 
19789:انگشتم باد کرده» باد گرفتن گلو با زیر دنده 
20818:انگشتان؛ بر و بال» جناح. 
23802:انگشتان یک دست خود را باز گذارده و 
23804:انگشت‌های باز را می‌شمارد و مثلاً یست و 
23876:انگشتان شخص در حال رقص و غیر آن 
=== search 'انگشت' with pahlavi ===
=== انگلیس ===
142:استاد هنینگ ودنههع .۷۰۵ (انگلیسی) ر استاد بنونیست »اهنده8007 (فرانسوی) و 
152:به انگلیسی سخنرانی کرد که در مجموعة موتمر به تبع رسید. 
336:۲ کتیبه‌های پهلوی. (ترجمه از انگلیسی) به قلم و.ب. هنینگ وونه«ه812 ۷ 
340:۴ -ايران تألیف دکتر ر. گیرشمن (فرانسوی ‏ انگلیسی) از انتشارات بنگاه 
636:(مانند ث عربی و «انگلیسی) 
5103:که طرفدار انگلستان است» انگلیس دو 
10285:ارویسا متداول است مانند: انگلیسی؛ 
27617:انگلیسی از این کلمه ماخ رات 
33827:۴ است. ضح. و یلیام شانکس انگلیسی 
43769:کیلوگرم با ۲۲۹۱/۲۴ پوند انگلیسی
```


## [2026-09-04T22:48:05.303Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18375,18400p' MON_part1.txt; echo \"=== 5095-5115 ===\"; sed -n '5095,5115p' MON_part1.txt",
 "description": "Print Moin context for angosht and englestan"
}
```


### [2026-09-04T22:48:05.378Z] TOOL RESULT

```
انگد: یرجه [- انگز ] ((.) بیلی پهن که با آن 
زمین را هموار کنند؛ بیل. آلتی که پیلبانان با 
آن بیل را برانند؛ کچکت. 

انگشت: اقهوه (.) زغال» زگال. 
انگشت: ۱ (.) مر یک از ات 
متحرک ینجگانةٌ دست و پای انسان. | ۱ 
ج. انگشتان» انگشت‌ها. واحدی معادل 3 
چهارم قبضه (تاریخ قم ص ۳۱-۹ 
انگشتال: ۸7:52 (رص.) مردم صعف و 
نحیف و علیل» بیمار؛ ناخوش. 

انگشتانه: ۰ (6-)2:0۵051202 (امر .) ۳ فلری 
است به شکل مخروط ناقص که در بدنهة آن 
به قطر ته سوزن معمولی فرورفتگی‌هایی 
مو جو د د است و خیاطان به هنگام دوحتن 0 
را به انگشت کنند. (گیاء) گل انگشتانه. 
انگشت به‌لب: -06-.۸ (ص‌مر.) متحیر» 
متعجب. خاموس. 

انگشت پیچ: 200۵5۱-6 (ص مر .) هر چبز 
غلیظ و بسته که دور انگشت پیجد» مانند: 
عسل» سیره» دوشاب. (امر.) عهد» شرط» 
بیمان. انعام اند کك. (ص‌مر.) معارض» 


=== 5095-5115 ===
آن کس که. آنجه. 

انگاه: ۰ 270-888 (ق. زمان) زرمان» آن 
وفت» آن هنگام. , پس از آن» سپس بعد» در 
آخر. . مع‌هدذ اه مع‌دلکک. نعلاوه؛ از آن 
کذ شته. 

انگلوفیل: آ50810-1 (ص. .) (سبا كٍِ 
که طرفدار انگلستان است» انگلیس دو 
آنگونه: (م-) 02 ع-27 (ق‌مر.) ۱ آ: 
و جه. 

انوری 20070 [یو.] (.) (یز.) غدة 
مشکل از خون که غالبا به شریان مربوط 
اتشت و محتویات آن ممکن است خون مایع 
پا خون منعقد باشد؛ انوریسماء» انوریسماء 


اوانس»
```


## [2026-09-04T22:48:13.174Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON && ls -la; grep -n \"انگشت\" MON_2vol_Adena_v1_djvu.txt | head -20",
 "description": "Grep Moin 2-vol scan for angosht"
}
```


### [2026-09-04T22:48:13.237Z] TOOL RESULT

```
total 48684
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 20113727 Sep  4 14:06 MON_2vol_Adena_v1_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4377831 Sep  4 14:06 MON_2vol_Adena_v1_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 21014767 Sep  4 14:06 MON_2vol_Adena_v2_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4331421 Sep  4 14:06 MON_2vol_Adena_v2_djvu.txt
4081:انگشتان نو از ند. 
4208:شباهت به آخر کلمات ملحق شود: انگشتال 
4268:آلاس: 5 (.) رغال» زگال؛ انگشت. 
4801:چنانکه گوهری را در انگشتری. به سلکك 
6555:تاریکی. (ا) انگشت ستبر و کو تاه دست يا با 
6556:از جانب انسی» انگشت نر انگشت بزرگد» 
7133:اثلق: ساعه [ع.] (.) (گیا.) پنج انگشت. 
8680:اخگر کشته: زغال» انگشت. 
9778:کارینات‌ها است. انگشتان پایش توسط 
9994:سرانگشت؛ دراع» رش. 
10095:زن‌ند. آوازی که با سودن انگشتان به 
10097:خوشحالی و شادمانی» بشکن؛ انگشتکك. 
12362:را به انگشت پااکك کردن. 
13523:است به مقدار چهار انگشت که وسط آن 
13526:بکار رود. چوبی که لای انگشتان متهمان 
13716:اصبع: مه [ع.] (.) انگشت» ج. اصابع. 
15114:انگشته» هسته. 
16441:در نوازندگی با الواح انگشت‌های دست 
18379:انگشت: اقهوه (.) زغال» زگال. 
18380:انگشت: ۱ (.) مر یک از ات
```


## [2026-09-04T22:48:21.184Z] TOOL CALL #46: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-04T22:48:21.192Z] TOOL RESULT

```


```


## [2026-09-04T22:48:24.933Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂enk-",
 "prompt": "Give the reconstructed root, its meaning, and the full list of descendants (Indo-Iranian, Greek, Latin, Germanic, Sanskrit). Quote the etymology section."
}
```


## [2026-09-04T22:48:26.756Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%86%DA%AF%D8%B4%D8%AA",
 "prompt": "Give the full Persian etymology of انگشت (angošt) 'finger': Middle Persian form, Old Iranian/Avestan form, Proto-Indo-European root, and any cited sources."
}
```


### [2026-09-04T22:48:31.984Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂enk-

## Reconstructed Root and Meaning
The root is **\*h₂enk-** with the meaning: "curve, bend"

## Descendants by Language Family

**Indo-Iranian:**
- Sanskrit: ácati, áñcati

**Greek:**
- Ancient Greek: ἀγκών (ankṓn), ἀγκύλος (ankúlos), ἀγκύλη (ankúlē), ἄγκυρα (ánkūra)

**Latin:**
- ancus

**Germanic:**
- Old Norse: áll, ǫ́ll, ǫ́l, ál

**Other:**
- Armenian: անթ (antʻ), անutil (anutʻ), անգղ (angł)
- Celtic and Italic descendants also attested

## Etymology Section
The page states: "This Proto-Indo-European entry contains reconstructed terms and roots. As such, the term(s) in this entry are not directly attested, but are hypothesized to have existed based on comparative evidence."

The root derives from multiple scholarly sources including Pokorny (1959) and Rix (2001), demonstrating widespread attestation across ancient language families connected through systematic sound correspondences.
```


### [2026-09-04T22:48:33.048Z] TOOL RESULT

```
# Persian Etymology of انگشت (angošt) 'finger'

**Middle Persian form:** ʾngwst'

**Proto-Indo-Iranian:** *Hangúštʰas

**Proto-Indo-European root:** *h₂eng-

**Avestan cognate:** 𐬀𐬧𐬔𐬎𐬱𐬙𐬀 (aṇgušta)

**Sanskrit cognate:** अङ्गुष्ठ (aṅguṣṭha, "thumb, big toe")

**Cited source:** Rastorgujeva and Edelʹman's *Etimologičeskij slovarʹ iranskix jazykov* [Etymological Dictionary of Iranian Languages] (2000), volume 1, Moscow: Vostochnaya Literatura, page 169.

The word traces back through Middle Persian to Proto-Indo-Iranian, ultimately deriving from the Proto-Indo-European root signifying a grasping or gripping action, with cognates appearing across multiple ancient language families.
```


## [2026-09-04T22:48:41.100Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D9%86%DA%AF%D8%B1",
 "prompt": "Give the Persian etymology of لنگر (langar) 'anchor' in full: what does Wiktionary say it comes from (Greek ἄγκυρα? Sanskrit laṅgara? Middle Persian?), and list all cited sources and descendants."
}
```


## [2026-09-04T22:48:42.571Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%B7%D8%B1%D9%86%D8%AC",
 "prompt": "Give the etymology of شطرنج in Persian and Arabic: Middle Persian čatrang, Sanskrit caturaṅga, and the route of borrowing. Quote the etymology sections."
}
```


### [2026-09-04T22:48:48.253Z] TOOL RESULT

```
# Etymology of Persian لنگر (langar)

According to Wiktionary, the word has **two proposed etymologies**:

1. **Greek origin**: "From Ancient Greek _ἄγκῡρα_ (ánkūra)" – deriving from the classical Greek term for anchor.

2. **Iranian origin**: Described as "Alternately of Iranian origin, cognate with Sanskrit _लङ्गल_ (laṅgala)," suggesting a shared root within Indo-Iranian languages rather than Greek borrowing.

The entry does not specify Middle Persian as a source, nor does it indicate which theory is preferred.

## Descendants

The word spread widely through various languages:
- Arabic: أَنْجَر (ʔanjar)
- Turkish/Ottoman Turkish: lenger
- Uyghur, Uzbek, Turkmen
- Gujarati, Kazakh
- Armenian (via Turkish)
- Mandarin Chinese: 蘭干 (Lángān)

The extensive descendant list suggests significant historical circulation of this maritime term across trade routes and linguistic regions.
```


### [2026-09-04T22:48:49.515Z] TOOL RESULT

```
# Etymology of شطرنج (Shatranj)

## Arabic Etymology

The Arabic term was borrowed from Classical Persian. According to the etymology section:

> "Borrowed from Classical Persian چَتْرَنگ (čatrang), from Middle Persian 𐭰𐭠𐭲𐭫𐭠𐭭𐭢 (cʾtlʾng /⁠čatrang⁠/, "chess"), borrowed from Sanskrit चतुरङ्ग (caturaṅga)"

The Sanskrit root combines "four" (चतुर् catúr) with "limb/member" (अङ्ग áṅga), literally meaning "four limbs; four members."

## Persian Etymology

Modern Persian also adopted this term through borrowing. The Persian section states:

> "Borrowed from Arabic شَطْرَنْج (šaṭranj), borrowed from Classical Persian چَتْرَنگ (čatrang), from Middle Persian...borrowed from Sanskrit चतुरङ्ग (caturaṅga)"

## Borrowing Route

The word traveled: **Sanskrit → Middle Persian → Classical Persian → Arabic → Modern Persian** (and other languages including Turkish, Russian, and Romance languages).
```


## [2026-09-04T22:49:03.743Z] TOOL CALL #51: Bash

```json
{
 "command": "ls data/ ; ls data/extracted | head; find . -name \"*56*\" -path \"*page*\" -not -path \"./.git/*\" | head -20",
 "description": "Look for page 56 assets"
}
```


### [2026-09-04T22:49:03.811Z] TOOL RESULT

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
./site/pages/568.jpg
./site/pages/562.jpg
./site/pages/256.jpg
./site/pages/563.jpg
./site/pages/56.jpg
./site/pages/564.jpg
./site/pages/565.jpg
./site/pages/567.jpg
./site/pages/556.jpg
./site/pages/356.jpg
./site/pages/569.jpg
./site/pages/156.jpg
./site/pages/456.jpg
./site/pages/561.jpg
./site/pages/560.jpg
./site/pages/566.jpg
./data/extracted/batch/page-456.json
./data/extracted/batch/page-565.json
./data/extracted/batch/page-256.json
./data/extracted/batch/page-56.json
```


## [2026-09-04T22:49:06.077Z] TOOL CALL #52: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/56.jpg"
}
```


### [2026-09-04T22:49:06.113Z] TOOL RESULT

```

```


## [2026-09-04T22:49:25.540Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HRN angust\"; grep -n -i \"angust\\|angušt\\|anguSt\" HRN.txt | head -10; echo \"### HRN zuza\"; grep -n -i \"zuza\\|žūža\\|Igel\" HRN.txt | head -10; echo \"### HRN langar\"; grep -n -i \"langar\\|Anker\" HRN.txt | head -10; echo \"### HUB\"; grep -n -i \"angust\\|zuza\\|langar\" HUB.txt | head -10",
 "description": "Grep Horn and Hübschmann"
}
```


### [2026-09-04T22:49:25.622Z] TOOL RESULT

```
### HRN angust
1527:aw. angusta- 'Zehe'; phlv. angust^)\ skr. angtistha-
### HRN zuza
1532:Dialektisch findet sich Kä§. engxdt, mäz. e)igel^
4214:(aus *;^6Zr^^r ?) 3), x^^P^^^ Igel-
4216:Igel* (Bund.); arm. fear 'Stein*.
5318:phlv. deg 'Topf; lat. figulus^) Töpfer*; mhd. tigel^
6050:687. zü$e 'Igel'.
6052:aw. duzaka- Igel' (als Schimpfname des Hundes
6053:verwandt) ; phlv. zUzak,
9942:602. Ein anderes räz 'Stacheligel' wird zu [/^reg- (s. No. 93j
10093:aw. *Ä + V^iiay-; ai. cL -i [/^yiay- 'herbeigeleiten,
### HRN langar
1460:aw. hanlcärat/emi j hankere&a-, hankereti- 'Zählung'
7925:da weder ein Gesunder noch ein Kranker es ent-— 204 —
### HUB
594:angu§t 'Finger', angustdna *Ring, Fingerbut* neben orig. giUa *Finger*.
1656:ziehen', auch angusto et aegro esse animo', skr. tanc
4174:Blei\ ars *Thrane*, asp Tferd', ast *ist', angust Tinger ')
8435:= phi. "^mustik; angust 'Finger, Zehe' = zd. angusta";
8451:Ygl. angust H. 125 (np. angust), must 'Fau.t' Gl. and Ind.
8815:zd. ga^sa-; gehan *Welt* = zd. gaedanqm (gen.pl.); angust
```


## [2026-09-04T22:49:29.666Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1520,1535p' HRN.txt; echo \"=== HRN 687 zuze ===\"; sed -n '6045,6060p' HRN.txt; echo \"=== HUB 594 ===\"; sed -n '588,600p' HUB.txt; echo \"=== HUB 8435 ===\"; sed -n '8430,8455p' HUB.txt",
 "description": "Print Horn and Hübschmann entries"
}
```


### [2026-09-04T22:49:29.738Z] TOOL RESULT

```
Synonyma naxavStjc, aayavStjz (aoTfivSv]:.) und herld nur aus dem Babylo-
nischen befriedigend erklärt werden können: ''AnxavStjg, uayavSrjg =
^^^^^^(X) — b*^' (asgandu (askandii?) etc. = älterem ^aknu; herld =
babyl. biirldu (für älteres *(p)hurädn) = 'Eilbote' und 'schnelles Pferd'."— 80 -
125. enguM Tinger, Zehe'; vergl. etigustetl 'Ring'^
engusfioäne Tingerhut* *).
Kä§. ungüss^) (neben engüst, mgüs etc.); mäz. nngus.
aw. angusta- 'Zehe'; phlv. angust^)\ skr. angtistha-
*Daunien, grosse Zehe*.
kurd. LW. engust; oss. d. at'ndje^ ünguljä Tinger
(LW.), t. ängursf (26); af/. güta; wa/. yangl, minj.
augar, §iyn. angast, sar. ingä/t, sangl. ingit.
Dialektisch findet sich Kä§. engxdt, mäz. e)igel^
vergl. skr. atlgün-, angüli- Tinger, Zehe'.
126. efiffist 'Kohle'.
Vergl. skr. angärä- 'Kohle'.
=== HRN 687 zuze ===
Delem gebräuchlich)', pDIT (Jer. 50, 42).
LW. ^ißvvt] (^Cvßivrj) etc. , arm. suin , syr. JOID
(de Lagarde, Ges. Abh. 67).
Die Herkunft des Wortes ist dunkel; vergl.
Hübschmann, ZDMG. 46, 250 No. 110.
687. zü$e 'Igel'.
mäz. arzarnldijl (?) ; g. jujlk,
aw. duzaka- Igel' (als Schimpfname des Hundes
verwandt) ; phlv. zUzak,
kurd. LW. arm]ijl (H.-Sch.)?, züzl (J.-J.).
S.
688. süyfeii 'machen, ausführen', Praes. säz-em, säz 'Gerät*.
Käs. Q. bäsöj, K. lesöj.
aw. i/^saC' , mit aiwi 'darbringen , ausführen
{yasnenif ; phlv. säxtan, sac(i)sn.
*) Nach Castle (bei Vullers) ,7V/.
=== HUB 594 ===
132. Np. ^obdS" liederlicher Kerl, Gesindel' liegt als LW.
im Afgh. in der Form aubos vor und wurde so wohl
auch im Persischen gesprochen. Dann ist es arabisirt
Oder aus dem Arabischen entlehnt. Vgl. bei Freitag:
*) Vgl. auch jiid. tat. heng *Hummer (Miller p. 85).
•) Vgl. daneben das LW. angalnn bei R a v e r t y und vgl. das L W.
angu§t 'Finger', angustdna *Ring, Fingerbut* neben orig. giUa *Finger*.
') Oegen Fr. M filler, WZKM. 5, 264.
2*— 20 --
vabaSf pi. aubas ^GesindeF. — Auch Noldeke halt
aubas fiir echt arabisch.
133. Np. . aurang (so , resp. jetzt durdng gesprochen,
Sal. Shuk. p. 7) 'Thron*, nach VuUers mit der
=== HUB 8435 ===
so sollte man im Np. *xis erwarten, wie umgekehrt np. xirs
eher auf iran. *fsa- (als fsa-) weist.
§ 130. Idg. st (nach i, u etc.) und kH = iran. ap. st
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
= zd. xsvasti- ; pist 'Mehl' = skr. pista- ; mahist (ZDM6.
46, 139) = ap. mad^ista- ; bargustuvan 'Pferdepanzer H. 205,
oben p. 27. Durch spateren Vokalausfall entstand st aus
sat in bTst 'zwanzig* = zd. visaiti und diivest zweihundert*
= zd. duy^ saite.
Im Phi. steht st hauiBiger fiir urspr. st im Auslaut,
Ygl. angust H. 125 (np. angust), must 'Fau.t' Gl. and Ind.
^J Dazu haStdah 'achtzehn* = hazdah (Fird. I, 46, 216, vgl. die
Anm.) und hajdah (Vullers, Gram. p. 185), hizdah, hijdah Sal,
Shuk. p. 39,— 237 —
218 (np. must), besonders in Superlativen : paz. mahest
```


## [2026-09-04T22:49:46.154Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### IEC ank\"; grep -n -E \"^(ank|ang|anku|ankos|angos)\" IEC.txt | head -20; echo \"### SYN finger\"; grep -n -i \"angusta\\|angustha\" SYN.txt IEC.txt | head -10; echo \"### WLD band3\"; grep -n -i \"ank-\\|angulus\" WLD_band3.txt | head -10",
 "description": "Grep Mann, Buck, Walde-Pokorny"
}
```


### [2026-09-04T22:49:46.228Z] TOOL RESULT

```
### IEC ank
538:ang- ‘tapering; wedge, angle, cleft. Cf. angh-, anĝh- and ank- Gk. cf. phál-agx, -aggos “front wedge’; phár- agx ‘cleft wedge’, hence ‘chasm’; OHG ancha “leg, shin’; MHG anke “ankle, nape’. Cf. G Enk, Enke (1) “fork, Y-piece': ON akka
542:angólos (angol-, angil-, angl-), is, iə “coal, coal fire’. WP I, 181 Skt. ángarab; Ir. aingeal, pl. aingle “fire, hearth, cinder; W engyl "Drei: OCS ogli ‘coal; Li. anglis; Latv: ogle, pl. id. The con- nexions of Alb. thëngjill ‘coal and OHG kol, kolo, id. with the above forms are not clear.
543:angulos, see ongulos, anghulos, ankulos
544:anghostis, see an2uhəstis
545:anghó, ið “press, squeeze, strain, confine’. WP I, 62. Cf. angho, anguho. (Much of the evidence for these forms is ambiguous) Av. aíigh-; Arm. z-angem, cpd. ‘knead’, ç- angem, cpd. ‘hedge round’; Gk. ánkho; Alb. cf. ang ‘nightmare’; Lat. ango, -ére; Osc. cf. angitust (‘shall demand’ or sim.); MIr. angim, con- ‘protect beside angtha (pp. as adj. "dit. ficult); Ir. cumh-angaim ‘confine’; W angu ‘contain’; OE angian ‘grieve’; OFris. angia ‘fear; MDu. cf. ang. ‘afraid’; Li. (ambig.) éngiu, ti ‘squeeze’ beside angà ‘doorway’, cf. Pol. weg-ar, id. (Li. engti is e-grade, see un- der eng-. Go. ga-aggwjan: MHG engen derive
551:anghros, å ‘raging, bitter; rage, bitterness’ Av. añgra; Tokh. (?) ankāre ‘profligacy’; Olr. égair ‘ferocious ON angr, gs. angrs: Nor. anger: Sw. ånger; Finn.LW ankara ‘severe’
552:anghulos, anghlos, is “angle, corner’. WP I, 61. Cf. ank-, onk-, onk- Skt. ánghrih ‘foot’; Oss. ángurá (ambig.) “fish- hook; Lat. angulus; Umb. anglo-; OHG (ambig.) angul “fish-hook; MHG angel “hinge, fish-hook'; OE angel; ON ongull, pl. onglar; OCS oglü ‘corner’ and com. SI.
553:anguó (?) ‘go’. See next. Only in Skt. an- gami, id.; inge, mp. ‘move’
554:anguos, om, à (?) ‘limb; gait’. Cf. anguó Skt. (ambig.) ángam; cf. Gk. -ambos in the cpds. thrí-, í-, dithur-, itthumbos (see dhreiu-, i- and eimi, didhur-, suidh-); cf. kher-ámbe (a mollusc: *hand-limb'. Pelasgian wds. accdg. to H. Frisk GEW)
555:anguhis, io ‘snake, grass-snake, eel, adder.
561:anguhros, ios, (anguhər-) ‘worm, grub, eel; blackhead’. WP I, 64 Ir.-eagur in gil-eagur ‘horseleech’; OHG angar, angari (‘grub’°: MHG anger, cf. G. Enger- ling); Pol. wegórz (Cz. úhoř, R ùgorí, etc.) beside Pol. wagr (‘blackheaď’: Cz. uber, R ügori (2), etc.); Finn. LW ankerias (“eel , LW); Li. cf. ungurýs (eel, vocalism obscure), be- side ankštaras, -Stiras, -a ‘blackhead; grub’ (consonantism obscure); Latv. angsters ‘grub, cockchafer’. Of unknown history is Arm. andzruk ‘anchovy’, mng. influenced by Sp. anchoa, from Basque antxo-a ‘leech, an- chovy’. Cf. Br. aer ‘snake? and Est. LW angerjas ‘eel
564:angho, ið ‘cramp, straiten, force’. WP I, 62. Cf. anghó, anguho (Most of the evidence is ambiguous. For Per. Go. ON and OCS forms, cf. anguho. For Av.Gk.Lat.OlIr. forms see angho)
565:anguháa, see anguhis, anguhos
566:anguhostos, is “narrow; constrained; anxi- ous; strain, anguish’. WP I, 62. Cf. anguhis, os, anguhó, anghó and WP I, 61-63 Av. ásto; n. gs. -áh- ‘oppressor; oppression"; Alb. anksht ‘wild’; Lat. angustus, angustia; OHG angust 'fear'; OFris. angost; Sw; àn- gest; ON angist: OCz. üZest, d: Li. afik3tas; afikStis, f. “narrow; strait beside ankstis, f. “fear”. (For Latv. oksts, oksta and OE ohsta see ankst- below)
567:anguhinà ‘strait, stricture’. WP I, 63. Cf.
569:anguhis, os Lat. angina; Cor. ynny; OCS ọzina beside Cz. úžina; Srb. uzan, adj. f. uzna “narrow, close’.
571:anguho ‘narrow, squeeze’. WP I, 62. Cf. angho, angho Per. anjam, -idan (/bend'. Ambig. cf. onk-); Arm. denom. andzkam ‘ʻI yearn’; Go. ga- aggwjan; ON ongva; MHG engen; OCS o£o, oziti
573:ankolos, see ankulos
574:ankoros, see ankuros
575:ankotos, anktos, à “bend; bent’. Cf. onkos, onkos. Skt. aficitab; cf. Per. anjidan (ambig. *bend"); W. angad (‘handshake’, ambig.); Olr. écht, Ir. éacht ‘foul deed’; OHG åhta *'outlawry'; OE obt *manhunt' beside ahtian ‘to ambush’. (The Ir. and Gmc. forms are ambig.); OCS okotí (‘hook’, ambig. cf. onk-)
### SYN finger
IEC.txt:12165:-ön (-ünos, -ónà, -ónom), derivative suffix relating to a radical simplex. Examples are numerous. The simplex is given in brackets. Av. Caranom, acc. sg. m. (ffield, plot: Carai(mi) "go: Per. angustane, s. ( finger-ring': angust); Tadjik somon, saman (Cquietude': Av. samo); Arm. durn, pl: drunk (fgate': durk, pl. door: Gk. thurón (‘halľ: thüra); Lat. falcon ('hawk': falx); Osc. eituns ('soldiers': ei-, i- go); MIr. cammán ('crook': camm); W byson ('finger- ring’: bys); Go. auga-daüron, pl. ong (&win- dow’: daür); R. Cz. velikán (‘gianť: velikü); Li. dubuó, gs. -efis (“hollow?: dubus) beside pirmuonis, gs. -iés, m. f. (firstborn': pirmas); cf. Latv. kustonis (animal, being’: kustet, v. "move?
SYN.txt:6190:Russ. alec (perst) Skt. angult- - Av. arazu-, angusta-
SYN.txt:6199:6. Skt. aviguli-, Av. angusta- (as ‘finger’ only in epds., otherwise ‘toe’ = Skt. avigustha- ‘thumb, big toe’) : Skt, anga- ‘limb’, OHG ancha ‘nape of the neck, thigh’, NE ankle, etc., all prob. as ‘crooked’ : Lat. angulus ‘corner’, etc, Walde-P. 1.61. Walde-H. 1.48 f.
SYN.txt:6209:Rum. degetul cel gros, NE thumb Russ. bol! Soj palec policar Du. duim Skt. angustha-
SYN.txt:6313:4.38 TOE Grk.  daxrvdos Goth. Lith. pirStas (kojos) NG daxr7vd0 (Tod zodtod) ON ta Lett. (kdjas) pirksts Lat.  digitus Dan. taa ChSl.  priistii(?) It. dito (del piede) Sw. td SCr. _ prst (od noge) Fr. orteil, doigt du pied OE ta Boh.  prst (na nahou) Sp. dedo (del pie) ME to Pol. palec (u nogi) Rum. deget de la picior NE toe Russ. alec (na noge) Ir. mér (coise) Du. teen Skt.  anguli-, padaiiguli- NIr. = méar (coise) OHG zaha Av. angusta- W. bys troed MHG ze(he) Br. biz troad NHG zehe
### WLD band3
689:XI, Lateinisch. a, Ga 1. affabré 524. ammenium 35, 46 ab 47. agire 36. anmnta Ath. abdomen ‘TTT ager 37. amonua 63, | agilie 36, caren plea, afnes (5). 51) agina 36. aneptrue, -dre Tai 36. elo ps aurea a re 87 agna dil. an, anne Ot, aba 47 egnimen 132, an-(hélo) 58, | agnus 30, amas Gi), abolfiine 721 -ere 35. anatina G0. * age, -Gmne ah. ancrae 61, ae 44. a. uncunulente dAcen Larentia 34. i¢ oie ot hat accendo, -ere 352. grestia G04" accipiter (34.) 172. 21° aie 114. anda al -lat. 162, 126". aceon, -?re 32. ala $7. ng acer, Flee 2h alacer rc ey #2. deer a hd je i , ua 28, “tion gali-lnt. 98 anger 62. acernua 29. alburnis i. anguilla tht aeervus 28. alfroe {ht. onguie 63. actiwm 32. alcido 155. angulus (38, 39), 01 acia od. alegs iM, anguatus G2 oodus 32 dlew (88). animal St. aciza 32 oO, 7ere 87. crm Gi a2 1a. anna 65, acnuo 20, 30 , algére 01 dAnna Perenna 55 eer tid wee alénus Sih. anndna en aculews 20. alimentum 87. annus 4 aeuo, acumen 33. alimo, -<inie 87 ansa 62. 68 acupedius 172. aliquia 86. aveer 636 oust ,,Granne” 31. dlium 57, #0. anlae 50. aous ,,Nadel" 34. aliua BG. anidriue 63, 66, acua ,,Hornhecht™ 32. willera (H). ante (50), 66- acl 4. allium 57. anterior 64. ne 14. alicdivwm mist. 16. ontie 66. iduls, -duif B15. almws 57, anfiae 03. adipiscor 46. alnus LBL. anficus Ob. aditue 102 ‘alo, -ere BE anfided 66. adoleo, -re 6, (87), 83. Alpes 93. antidio, -ire G6. adolZeco, -ere.auflodern” 88. alldre 88. anfiquus 66. ader 45. alter 8H. onfiaies G0". adito, -ire 297. altue 86. anfidper 34* adulter 86.. alicinor 38. onus vr oe 7}. , (12), ers ae Owe it a [ aitimen Yl. anzare |i4 alita 1. , alvua (24), 26, (02). aper 121. afa(ejua 4 Amanus 63. | ) cmdres 1TH. (235*). opie (258). 125, (176). geguas 7, 102, GOS amb- Gel. piscor 46. aeruema (205). wmbdges BB. oplada 1. gerusco, -ire (12). cninguuse 3H. oper, apur 46. ars 4. embo 55. appello, ~ire (G77"). aesculus 10), ambiricta 54. 76. dprinius a eatiis, actus ambulo, -are (88), nar 121,
3110:Nicslant net ; (mit solinftartigon’ Bten- faved Wie Nord Deyero ai7.| me | sey er : Fayence $77. (mit verdickter Wurzel) as ee Notwendigkeit 1. ank- 60, mull ni jlo 303, S17", | Pilanzenachaft 7. (aver-G41" wd- 315", | Pflanzenatache! 3. gher- 06, | Guillen omnd- 178 nin 4. or. Pilangensta nas v" >
```


## [2026-09-04T22:49:58.304Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -B2 -A12 \"^ang-\\|ang- To bend\\|ank- To bend\" AHD_watkins1985.txt | head -60",
 "description": "Grep Watkins AHD for ang- root"
}
```


### [2026-09-04T22:49:58.364Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T22:50:01.443Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"palanquin\\|ankura\\|angulus\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins for palanquin, ankura, angulus"
}
```


### [2026-09-04T22:50:01.488Z] TOOL RESULT

```
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
837:“around.” I. Basic form *per and extended form *peri. 1. Germanic *fer-, *far-, used chiefly as an intensive prefix denoting destruction, reversal, or completion, in: a. Old High German far-, in German vereinen, to unite: TURNVEREIN; b. Middle Dutch vieren, to let out, slacken: VEER; C. compound “*fer-getan, “‘to lose one’s hold,” forget (see ghend-). 2. Suffixed (comparative) form *per-ero-, farther away, in Germanic *fer(e)ra’in Old English feor(r), far: FAR. 3. Compound “per-n-yo-, of last year (*-n-, year; see en-), in Germanic *fernja- in Old High German firni, old: FmRN. 4. Latin per, through, for, by: PER, PER-; PARAMOUNT, PARAMOUR, PARGET, PAR- VENU. 5. Greek peri, around, near, beyond: PERI-; PERIS- SODACTYL. 6. Sanskrit pari, through, around: PALANQUIN. 7. Avestan pairi, around: PARADISE. II. Zero-grade form *pr-. 1.Germanic *fur, before, in: a. Old English for, before, instead of, on account of: FOR; b. Old English for-, prefix denoting destruction, pejora- tion, exclusion, or completion: For-. 2. Extended form *prt- in Germanic *furth-, forward, in Old English forth, forth: FORTH; AFFORD. 3. Suffixed (comparative) form *pr-tero- in Germanic *furthera- in Old English furthra, furthor, farther away: FURTHER. 4. Compound *pr-st-i- (or *por-st-i-, with o-grade form *por-), “that which stands before,” stake, post (see sta-). III. Extended zero-grade form “pro-. 1. Suffixed (superlative) form *pro-mo- in: a. Germanic *fruma-, *furma- in Old Eng- lish forma, first, foremost: FOREMOST, FORMER?; b. Latin compound prandium, “first meal,” late breakfast, lunch (probably < *pram-d-ium < *pram-(e)d-yo-; second ele- ment *-(e)d-, to eat; see ed-). 2. Suffixed (superlative) form *pro-isto- in Germanic *furista-, foremost, in Old English fyrst, fyrest, first: FIRST. 3. Suffixed form *pre-wo- in Greek *prowo-, first, foremost, in: a. analogi- cally suffixed Greek form *préw-arya in Greek prdira, forward part of a ship: PROw; b. suffixed (superlative) Greek form *préw-ato- in Greek prétos, first, foremost: PROTEIN, PROTIST, PROTO-, PROTON. 4. Suffixed form *pro-i in Celtic *(p)ari, *are in Gaulish ari (combining form are-), before, in Latin arepennis, half-acre (second element obscure): ARPENT. IV. Extended form “prod. 1. Germanic *fura, before, in: a. Old English fore, for (> Middle English fore-), before: FORE, FORE-; FOREFA- THER; b. Old High German fora (> German vor), before: VORLAGE; Cc. Germanic prefixed and suffixed form *bi-fora-na, in the front (*bi-, at, by; see ambhi), in Old English beforan, before: BEFORE. 2. Greek para, beside, alongside of, beyond: PARA-); PALFREY. V. Extended form *pré. 1. a. Germanic *fra, forward, away from, in Old Norse *frd (> Middle English fro), from: FRO; FROWARD; b. Germanic *fra-, completely (see ed-, éik-). 2. Suffixed form *pro-mo- in: a. Germanic *fram, from, in Old English from, from: FROM; b. Germanic *frum, forward, hence derivative verb *frumjan, to further, in Old French f(ojurnir, to supply, provide: FURNISH, VE- NEER; C. Czech pram, raft: PRAAM. 3. Suffixed form *pr6é-wo- in Germanic *frdw6-, lady, in: a. Old High German frouwa, lady: FRAU, (FRAULEIN); b. Middle Dutch vrouwe, woman: vRouw. 4. Latin pré, pro-, be- fore, for, instead of: PRO!, PRO-!; PURCHASE. 5. Suffixed form *pr6-no- in Latin prénus, leaning forward: PRONE. 6. Possible suffixed form *pro-ko- in Latin compound reciprocus, alternating, ‘‘backward and forward” (*re-ko-, backward; see re-): RECIPROCAL. 7. Suffixed adverb *pro-kve in: a. Latin prope, near: APPROACH, RAPPROCHEMENT, REPROACH; b. suffixed form *prok- ink“o- in Latin propinquus, near: PROPINQUITY; Cc. suf- fixed (superlative) form *prok’-samo- in Latin proximus, nearest: PROXIMATE; APPROXIMATE. 8. Compound *pro-bhw-o-, growing well or straightforward (*bhw-o-, to grow; see bheue-), in Latin probus, upright, good, virtuous: (PROBABLE), PROBE, PROBITY, (PROOF), PROVE; APPROVE, IMPROBITY, (IMPROVE), (REPROVE). 9. Greek pro, before, in front, forward: PRO-2. 10. Suffixed (com-
2036:PAL bhrater- PALANQUIN ank-, per! PALAVER gWele-1 PALE! pag-
```


## [2026-09-04T22:50:19.517Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"zuzag\\|zuzak\\|zuz\\|jujag\\|Zuzag\" SNS.txt SNS_pages.txt | head -20",
 "description": "Grep Shayast ne Shayast glossary for zuzag"
}
```


### [2026-09-04T22:50:19.565Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T22:50:23.689Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -E \"z.z.g|zuz|žuž|jvj|ژوژ\" SNS_pages.txt | head -20; echo \"=== leaves ===\"; python3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read(); L=t.split(chr(12)); print(len(L)); print(L[100][:800])\"",
 "description": "Search Shayast glossary"
}
```


### [2026-09-04T22:50:26.349Z] TOOL RESULT

```
1906:     ( \      Yf u» T E   V J* t-* **) a-V-^ jVJ**y< **W C K »**
7256:                                                         .j-V-       :spas:o"e>JJ            "-JjIj^a^-jVJU^jI^^j.i^^i^Ujj^"                                             .jL   :sar:\<o»
15648:                                                            zQzag 168/10
=== leaves ===
243
                                                                                                                                *-u .,<>                                           i    f f*




                   U *b 0*J
                                                                                                                         VY/T^                 j^:              zufay: -*»oP



       {AiVb
                                                                                          •oft*         VJ^Ij^^^^^^^j'V*!^*^
                                                                                                                                                                               H
                                                   (Mir. ton.
```


## [2026-09-04T22:50:30.615Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15630,15665p' SNS_pages.txt; echo \"=== leaf of that line ===\"; python3 - <<'PY'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:15647])\nprint('leaf',t[:off].count('\\f'))\nPY",
 "description": "Print Shayast glossary zuzag context"
}
```


### [2026-09-04T22:50:32.667Z] TOOL RESULT

```
                                                            zlvSh 171/1
yazisn I arday fravard   zamistSn 325/9
                                                            zlvisnlh 170/21
  311/15                 zan 167/10-288/4
                                                            ziyan 170/7
yazisn I sr&s 311/17     zan3n 167/14-288/18
                                                            ziy3nag 170/10
yazis 1 yazdan 311/20    zand 169/8-10
                                                            zChr 167/15
yazisn kardan 311/14     zandbad 169/12
                                                            z5r 169/4
yOzdahr 334/8            zandbadan 169/14
                                                            zOrmandtar 169/7
y5zdahran 334/12         zandlg 169/15
                                                            z3t 168/13
y&zdahrgar 212/14-334/13 zanSd 241/6-10
                                                            zStlh 168/22
yBzdahrgarlh 334/15      zan x apustan 288/13
                                                            zQzag 168/10
ySzdahrlh 334/17         zan I dastan 288/16
                                                            zufr 168/2
                         zanlh 167/24-288/20
                                                             zufray 168/9
                         zan I zadag 288/15
zad 164/19                zanisn 169/1
zadag 163/2               zan Xv 5stan 111/12-288/11
zadan 164/14              zarcr3 162/11
zad hSnd 164/20           zartust 165/10
 zara-yazad 166/17        zartustan 165/17
 zayfid 165/6             zartustOgtura 166/6
 zayEnd 165/5             zartustrOturo 165/19
 z3yisn 165/1             zartuItrOtuman 166/2
 zayisnlh 165/3           zartuItrOtumlh 166/4
 zad 241/7-9              zaspan 163/7
 zadSrlh 163/4            zSfanC?) 163/8
 zahag 162/1-4-10         zfih 155/8-169/18
=== leaf of that line ===
leaf 220
```


## [2026-09-04T22:50:39.696Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"zuzag\\|zQzag\\|z0zag\\|zOzag\\|zuzag\" SNS_pages.txt | head; echo \"=== find body page with zufr/zufray ===\"; grep -n \"zufr\\|zufay\\|zufray\" SNS_pages.txt | head",
 "description": "Locate zuzag entry in Shayast glossary body"
}
```


### [2026-09-04T22:50:39.755Z] TOOL RESULT

```
15648:                                                            zQzag 168/10
=== find body page with zufr/zufray ===
7069:                                                                                                                         VY/T^                 j^:              zufay: -*»oP
7079:                                                                                          ^sij) «*iUj5j>i-*:zufr
7085:                                                                                                                                      j-^.Ujjrzufray J^J^p                 •
15253:                      zufay 168/1                         Qrisat- 227/21                 disti- 313/13
15650:                                                            zufr 168/2
15652:                                                             zufray 168/9
```


## [2026-09-04T22:50:42.439Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7060,7100p' SNS_pages.txt",
 "description": "Print Shayast glossary page 168 body"
}
```


### [2026-09-04T22:50:42.491Z] TOOL RESULT

```
                                                            j~** '       1       :zanlh:                                                                                                       To
                                         \ff\\£       • tf                   J
                                                                                                                                *-u .,<>                                           i    f f*




                   U *b 0*J
                                                                                                                         VY/T^                 j^:              zufay: -*»oP



       {AiVb
                                                                                          •oft*         VJ^Ij^^^^^^^j'V*!^*^
                                                                                                                                                                               H
                                                   (Mir. ton.                                   jfr,           :       /LUt(/i).603)                          5afra-:U
                                                                                                                                      y   X/) nS                    111,56)
                                                                                                   ro s tag :iu *»>>*>•£
                                                                                          ^sij) «*iUj5j>i-*:zufr

tMtr. Man.                                                            (ci^fc^c-ffcAou. :,& low- lying region : J to*)



                                                                                                                                      j-^.Ujjrzufray J^J^p                 •

                                                                                  •   VY/Y^S             [3W tfM'j : *&)



                                                                                                                                                                               j   ,J
                                                                                                                                                                                       ^
                              ^   -zand:     Jp<
                                           (Y.

                                                                 .
                                                                     W   H^.n/l^.M/T^                                       UiW». 755)duzaka                                   r *.
```


## [2026-09-04T22:50:52.004Z] TOOL CALL #63: WebSearch

```json
{
 "query": "ریشه واژه «انگلیس» فارسی از فرانسوی anglais یا روسی"
}
```


## [2026-09-04T22:50:52.813Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/palanquin",
 "prompt": "Give the full etymology of palanquin: Portuguese, Javanese/Malay, Prakrit, Sanskrit paryanka/palyanka, and the root. Quote it."
}
```


### [2026-09-04T22:50:54.120Z] TOOL RESULT

```
Web search results for query: "ریشه واژه «انگلیس» فارسی از فرانسوی anglais یا روسی"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T22:50:59.914Z] TOOL RESULT

```
# Etymology of Palanquin

According to the Online Etymology Dictionary, palanquin traces through multiple languages:

**Portuguese → Malay/Javanese → Sanskrit**

The entry states: "from Portuguese _palanquim_ (early 16c.), from Malay and Javanese _palangki_ 'litter, sedan,' ultimately from Sanskrit _palyanka-s_ 'couch, bed, litter.'"

The Sanskrit root breaks down further as: "_pari_ 'around' + _ancati_ 'it bends, curves,' related to _anka-s_ 'a bend, hook, angle.'" The word essentially means "that which bends around the body"—referring to how the litter molds to accommodate a passenger.

The term entered English in the 1580s through Portuguese traders, with the nasal ending being "a Portuguese addition," similar to how "mandarin" was adapted.
```


## [2026-09-04T22:51:08.655Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HJB palanquin\"; grep -n -i \"palanquin\" HJB.txt | head -6; echo \"### AID\"; grep -n -i \"palanquin\\|palkee\" AID.txt | head -6; echo \"### LKT langar/anker\"; grep -n -i \"langar\\|lenger\\|anker\" LKT.txt | head -10; echo \"### SKT angle\"; grep -n -i \"^angle\\|^anchor\\|^English\" SKT.txt | head -10",
 "description": "Grep Hobson-Jobson, Whitworth, Lokotsch, Skeat"
}
```


### [2026-09-04T22:51:08.740Z] TOOL RESULT

```
### HJB palanquin
132:Of  words  that  seem  to  have  been  admitted  to  full  franchise,  we  may  give examples  in  curry^  toddy^  veranda,  cheroot,  loot,  nahob,  teapoy,  sepoy,  cowry ;  and of  others  familiar  enough  to  the  English  ear,  though  hardly  yet  received into  citizenship,  compound,  batta,  pucka,  chowry,  baboo,  mahout,  aya,  nauU^,* first-chop,  competition-toa/^,  griffin,  &c.  But  beyond  these  two  classes  of words,  received  within  the  last  century  or  so,  and  gradually,  into  half  or whole  recognition,  there  are  a  good  many  others,  long  since  fully  assimilated, which  really  originated  in  the  adoption  of  an  Indian  word,  or  the  modifica- tion of  an  Indian  proper  name.  Such  words  are  the  three  quoted  at  the beginning  of  these  remarks,  chintz,  calico,  gingham,  also  shawl,  bamboo,  pagoda^ typhoon,  m/msoon,  mandarin,  palanquin,f  &c.,  and  I  may  mention  among further  examples  which  may  perhaps  surprise  my  readers,  the  names  of  three of  the  boats  of  a  man-of-war,  viz.  the  cutter,  the  jolly-boat,  and  the  dijigy,  as all  (probably)  of  Indian  origin.!  Even  phrases  of  a  different  character — slang  indeed,  but  slang  generally  supposed  to  be  vernacular  as  well  as  vulgar — e.g,  'that  is  the  cheese* ;%  or  supposed  to  be  vernacular  and  profane — e,g, *I  don't  care  a  dam^X — are  in  reality,  however  vulgar  they  may  be,  neither vernacular  nor  profane,  but  phrases  turning  upon  innocent  Hindustani vocables.
162:onr  Anglo-Indian  coUoquiaUsmS)  even  if  eventually  traceable  to  native sources  (and  especially  to  Mahratti,  or  Dravidian  originals)  have  come  to us  throngb  a  Portuguese  medium,  and  often  bear  traces  of  having  passed through  that  alembic.  Not  a  few  of  these  are  familiar  all  over  India,  but the  number  current  in  the  South  is  larger  still.  Some  other  Portuguese woids  also,  though  they  can  hardly  be  said  to  be  recognized  elements  in  the Anglo-Indian  colloquial,  have  been  introduced  either  into  Hindustani generally,  or  into  that  shade  of  it  which  is  in  use  among  natives  in  habitual contact  with  Europeans.  Of  words  which  are  essentially  Portuguese,  among Anglo-Indian  colloquialisms,  persistent  or  obsolete,  we  may  quote  goglet, framy  plantain,  muster^  caste,  peon,  padre,  midry  or  maistry,  almyra,  aya,  cohray masqutlo,  pom/ret,  cartuez,  palmyra,  still  in  general  use ;  picoUa,  rolong,  pial, fogass,  margosa,  preserved  in  the  South  ;  hotel,  brab,  foras,  oart,  veUard  in Bombay  ;  joss,  compradore,  linguist  in  the  ports  of  China  ;  and  among  more or  less  obsolete  terms,  Moor,  for  a  Mahommedan,  still  surviving  under  the modified  form  Moorman,  in  Madras  and  Ceylon  ;  Gentoo,  still  partially  kept up,  I  believe,  at  Madras  in  application  to  the  Telugu  language,  mustees,  castees, bandeja  (*  a  tray '),  Kittysol  (*  an  umbrella,*  and  this  survived  ten  years  ago  in the  Calcutta  customs  tariff),  cuspadore  (^  a  spittoon '),  and  covid  ('  a  cubit  or ell*).  Words  of  native  origin  which  bear  the  mark  of  having  come  to  us through  the  Portuguese  may  be  illustrated  by  such  as  palanquin,  mandarin, nangelin  (a  small  weight  for  pearls,  &c.)  m^onsoon,  typhoon,  mango,  mangosteen^ jack-fruit,  batta,  curry,  chop,  congee,  coir,  cutch,  catamaran,  cassanar,  nabobs avadavat,  betel,  areca,  benzoin,  corge,  copra.*  A  few  examples  of  Hindustani words  borrowed  from  the  Portuguese  are  chdbl  (*a  key'),  bdola  (*a  port- manteau'),  6aft«  (*  a  bucket'),  martol  (*a  hammer*),  tauliya  (*a  towel,' Port. toalha),  sdbun  (*soap'),  bdsan  (* plate'  from  Port,  bctcia),  llldm  and  nlldm  (*an auction'),  besides  a  number  of  terms  used  by  Lascars  on  board  ship.
165:*  The  nasal  termination  given  to  many  Indian  words,  when  adopted  into  European QBQ,  M  in  palanquin,  niandarijij  &c.,  must  bo  attributed  mainly  to  the  Portuguese  ;  but it  cannot  be  entirely  due  to  them.  For  we  find  the  nasal  termination  of  AchiUy  in MAbommedan  writers  (see  p.  3),  and  that  of  Cochin  before  the  Portuguese  time  (see p.  22&%  whilst  the  conversion  of  Paaei,  in  Sumatra,  into  Facem,  as  the  Portuguese  call it,  is  alieady  indicated  in  the  Bama  of  Marco  Polo.
185:An  example  of  this  is  &oy,  in  its  application  to  a  native  servant.  To  this application  have  contributed  both  the  old  English  use  of  hoy  (analogous  to that  of  pueTf  gargcyn^  Knabe)  for  a  camp-servant,  or  for  a  slave,  and  the  Hindi- Marathi  hhoi^  the  name  of  a  caste  which  has  furnished  palanquin  and umbrella-bearers  to  many  generations  of  Europeans  in  India.  The  habitual use  of  the  word  by  the  Portuguese,  for  many  years  before  any  English influence  had  touched  the  shores  of  India  {e,g.  bdy  ds  sonibreroj  b6y  d^aguoHj hdy  de  palanqtiy)y  shows  that  the  earliest  source  was  the  Indian  one.
1694:1608-10.— "Quand  elles  vont  k  I'Eglise  on les  porte  en  palanquin  .  .  .  .  le  dedans  est d'vn  grand  tapis  de  Perse,  qu'ils  appellent AleaSf  .  .  .  r^Pyrard,  ii.  62 ;  [flak.  Soc. ii.  102].
2663:c.  1610. — "  Les  Portugais  et  les  Indiens  ne 86  sement  point  d'autres  bastons  pour  porter leurs  palanquins  ou  litieres.  lis  I'appellent partout  Bamboo."— Pymref,  i.  287 ;  [Hak.
### AID
949:B&uri.  [Bengali.]  The  name  of  a semi-Hinduised  tribe  of  Bengal and  Orissa  ;   they  are  cultivators, labourers,  swine-keepers,  fishermen, salt-makers,  and  palanquin-bearers.
978:Behdrd.  [Bengali.]  The  name  of  a low  caste ;   they  are  palanquin-bearers and  domestic  servants.
1016:Besta.  [Kanarese.]  The  name  of  a caste,  perhaps  the  same  as  the  Te- lugu  Boi’s,  and  allied  to  the  Kahdrs of  Bengal.  They  are  fishermen  and palanquin  -   bearers  specially,  but many  are  engaged  as  husbandmen, labourers,  weavers  of  cloth,  and lime-burners.  Many  of  the  women are  cotton-spinners.  They  are  ac- counted pure  3udras,  and  worship all  the  Hindu  deities,  but  especially Gangamma,  mother  Ganges.
1237:Bo'i. .   [Telugu.]  The  name  of  a   caste  ; they  are  fresh-water  fishermen  and palanquin-bearers,  but  are  much  used in  Madras  as  domestic  servants/
1474:The  Chanels  of  Bengal  are  now very  numerous,  and  in  some  parts, as  Rdjshdhi,  are  becoming  well-to- do.  They  are  cultivators,  boatmen, grass-cutters,  gardeners,  palanquin- bearers,  and  labourers.  Their  real origin  is  unknown,  nor  has  it  been determined  to  what  other  tribes  they are  related.
2739:palanquin-bearer.  Also,  in  Bombay, a   subordinate  house-servant ;   a bearer.
### LKT langar/anker
1827:'Schiffstau,  Seil';  hieraus  mit  partieller Assimilation  der  Liquida  l  ait.  gumina, it.  gomena,  sp.  pg.  gümena,  frz.  goumhne, gumhie  'Ankerlau'.  —  [Die  Form  ar. gainal  ML  3666  paßt  wegen  der  Voka- lisation lautlich  nicht.]
1865:'Stil' ;  hieraus  mlat.  capulum  'Fangseil', frz.  cäble,  sp.  cablo  'Ankertau',  engl. cable,  ndl.  kabel,  dtsch.  Kabel  [schon  im Gudrunliede  heißt  es :  ankersail  von Arabe,  wozu  Flachs  kaitän  benutzt Avurde.]
2140:'Krampe  od.  Haken  mit  zurückgebogener Spitze,  Harpune' ;  vulg.  hattäf,  mit  Imäia: hatfef;  hieraus  mit  Metathesis  pg.  fatexa 'Ankerhaken,  großer  Angelhaken'  [Gon- stancio Dicc  550c.]  —  DE  267.
2466:'Sichere  Bucht,  Ankerplatz'  [vom  Vb. kald'a  'bewachen,  behüten'];  hieraus sp.  it.  cala  'Bucht,  Reede',  frz.  cale 'dass.'.  [Vgl.  Globus  LXVII,  156:  ,Cala ist  der  kleine  seichte  Strand  der  alten Hafenbucht  in  Palermo,  der  heute  noch den  Fischerbooten  dient".]  [GrSVociSic 230.    ZfromPh  XXXII,  33.    ML  4664.
3052:stattfand  und  aus  *Nazaretum  dann lazzaretto  wurde;  vgl.  auch  Herrigs  Ar- chiv CXXXVII,  225];  prov.  frz.  ladre 'aussätzig',  dial.  (Picardie)  lasaire  'arm, elend',  lazaret  'Krankenhaus',  sp.  lazaro 'Bettler,  aussätzig',  pg.  lazarino  'aus- sätzig', sp.  laceria,  pg.  lazeira  'Armut', Vb.  sp.  lazdrar  'Mühsal  und  Elend  er- leiden', sp.  pg.  lazareto  'Krankenhaus'; dtsch.  Lazarett,  engl,  lazaret,  lazaretto 'Krankenhaus',  lazar-house  'dass.',  lazar- ly,  lazarlike  'elend,  aussätzig',  ndl.  la- zartis  'aussätzig',  lazarij  'Aussatz',  la- zarushuis  'Leproserie',  lazaret  'Kranken- haus', schwed.  lasarett  'Hospital',  dän. lazaret  'dass.';  russ.  lazar  'Bettler',  Vb. lazarit'  'betteln',  öech.  lazar  'Aussätzi- ger', poln.  tazarz  'Kranker,  Armseliger Bettler'.  [ML  4958.  Kluge  277.  Bern' SlEtWb  696.
3700:pzJimnr  'langer  Strick';  rum.  pälämar 'Ankertau',  it.  palamaro  'dass.'.  [Löbel EITAP  73.    Mikl  SIEtWb  230.
4297:'Ein  Affe  Hylobates  syndactylus  Wagn.' [Pijii  147];  hieraus  trz.  engl,  siamang, dlsch.  Siamang  'derselbe  Langarmaffe'. [Devic  DEt  207.   JAOS  XVIII,  101/102.
5786:Janitschar  954 Jasmin  942 Jatagan  944 janker  j.  928 Jauner  j.  932 Jelsomin  942 Jerboa  936 jiddisch  949 Joghurt  9ü0 Jo</j  2J69 Jonen  j.  932 Joner  j.  932 Jb/)j[)e  737 Jroükoz  1113 jMfcf/  959 jubeln  959 Jubiläum  959 Juchten  2128 JweZe  949 Jw/Ye«  2128 junen  j.  932 Jwfe  693
8321:langarote  86
### SKT angle
20:ENGLISH    LANGUAGE
25:ENGLISH    LANGUAGE
631:ANCHOR.
672:Anchor.  (L.-Gk.)  lletter  spelt  without lhe4.  M.E  ^mAtt.    A.^.ampr.^X^AtutfrA
673:ANCHORET.
676:Anchoret,  Anchorite^  a  recluse.  (F. —  Low  L.  —  Cik.)  K  anarhffrete  (Cot.)  — Low  L.  iinar/)ore/a.  —  ^J\c.  di-axajpijr^r,  one who  retires  Irom  the  woild.  —  Gk.  &vfi- XwpciV.  10  retire.  —  Gk.  ova,  back:  and Xvp^^v,  to  Withdraw,  from  x^P^*  sp^oc, room.    (VGHA)
696:Angle  (Of  «  comer.  <F.  -  L.)     M.  B.
699:Angle  ( 2),  a  hook,  ti-;li-lu.ok    1  E. tf«^v/,  a  fish  book. ■+ Dan.  a/i^v/;  G^ (^  AK,  ANK.)    Dor.  an^'e,  verb,
21296:anchor)  ;   to  weigh.  ^  Du.  uv^^n* vega.  to  move,  lift ;  Dan.  viit,  Swed. G.  we^n,  to  move,  unrxm,  to  rock, to  wagh.     Allied  to  L  M^^rv,  Skt.  ucJ to  carry.     (V  WAGH.)
```


## [2026-09-04T22:51:18.006Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/anchor",
 "prompt": "Full etymology of anchor: Old English ancor, Latin ancora, Greek ankyra, PIE root. Quote it."
}
```


## [2026-09-04T22:51:18.320Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Angles",
 "prompt": "Full etymology of Angles / Angle (the Germanic tribe), Angul in Schleswig, England, English. Quote it."
}
```


### [2026-09-04T22:51:23.338Z] TOOL RESULT

```
# Etymology of Anchor

The word "anchor" comes from Old English *ancor*, which was borrowed from Latin *ancora*. The Latin term traces back to Greek *ankyra*, both meaning "an anchor" or "a hook."

The ultimate origin is the Proto-Indo-European root **\*ang-/\*ank-**, meaning "to bend." This same root produced related words across Indo-European languages, including the English word "angle."

As the source states: "The unetymological -ch- emerged late 16c., a pedantic imitation of a corrupt spelling of the Latin word."

The figurative sense—"that which gives stability or security"—developed by the late 14th century. The modern meaning referring to a TV or radio presenter dates to 1965, derived from the earlier term "anchorman" (1903).
```


### [2026-09-04T22:51:30.323Z] TOOL RESULT

```
I appreciate your request, but I need to let you know that the webpage content provided doesn't actually contain the etymology information you're asking for. 

The page shown is the **homepage/header** of Etymonline.com, which displays:
- Navigation menus
- Search functionality
- Links to columns, forums, apps, and premium content
- Footer information about the site's creator (Douglas Harper & Talia Felix)
- Support and legal links

To provide you with the full etymology of "Angles," "Angle," or related terms, I would need to see the actual article content from an Etymonline entry page, which isn't included in what you've shared.

**Recommendation:** Visit etymonline.com directly and search for "Angles" or "Angle" to access the complete etymological entry, which would contain the detailed historical information about the Germanic tribe, Angul in Schleswig, and connections to England and English.
```


## [2026-09-04T22:51:33.792Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/England",
 "prompt": "Full etymology of England and of the Angles tribe: Old English Engla land, Engle, the district Angul in Schleswig, the hook-shape explanation. Quote it."
}
```


## [2026-09-04T22:51:36.493Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3",
 "prompt": "Give the Persian etymology of انگلیس (Engelis) 'England/English': what language is it borrowed from (French anglais? Ottoman Turkish? Italian?), and any cited sources. Also list related terms انگلیسی، انگلستان."
}
```


### [2026-09-04T22:51:39.446Z] TOOL RESULT

```
# Etymology of England

**Origin:** Old English *Engla land*, meaning "the land of the Angles," a Germanic tribe that invaded Britain in the 5th century.

**The Angles:** The name derives from *Engle* (plural), referring to one of the Germanic groups. According to etymological sources, they were "supposedly so-called because *Angul*, the land they inhabited on the Jutland coast, was shaped like a fish hook."

**Historical Development:** Initially, the term referenced the people rather than the place, used alongside *Angelcynn* ("the English race"). By late Old English times, it had shifted to denote a geographical region. A Danish king, Canute, was the first to call himself "King of England."

**Linguistic Note:** The word's modern pronunciation shifted from "En-" to "In-," possibly due to the frequency of "-ing" words in English.
```


### [2026-09-04T22:51:42.997Z] TOOL RESULT

```
# Persian Etymology of انگلیس (Engelis)

## Source Language
According to the Wiktionary entry, انگلیس is "Borrowed from Italian _inglese_, probably via Ottoman Turkish _انگلیز_ (ingiliz)."

The word thus has a multi-stage borrowing path: **Italian → Ottoman Turkish → Persian**

## Related Terms
The entry lists these connected words:

- **انگلیسی** (inglīsī / englisi) - listed as a derived term
- **انگلستان** (inglistān / englestân) - noted as a synonym specifically meaning "England"
- **آنگل** (āngil / ângel) - listed as a related term

## Note on Sources
The Wiktionary article does not provide citations to academic sources documenting this etymological claim. The etymology section presents the borrowing pathway but without linked references.
```


## [2026-09-04T22:51:55.749Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%AC%CE%B3%CE%BA%CF%85%CF%81%CE%B1",
 "prompt": "Ancient Greek ἄγκυρα: etymology, root, meaning, and descendants (Latin ancora, Persian langar, Arabic anjar). Quote the etymology."
}
```


## [2026-09-04T22:51:58.411Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%9A%E0%A4%A4%E0%A5%81%E0%A4%B0%E0%A4%99%E0%A5%8D%E0%A4%97",
 "prompt": "Sanskrit चतुरङ्ग (caturaṅga): meaning, composition (catur + aṅga), and descendants (Middle Persian čatrang, Persian, Arabic shatranj). Quote it. Also what does अङ्ग (aṅga) mean and derive from?"
}
```


### [2026-09-04T22:52:00.692Z] TOOL RESULT

```
# Etymology of άγκυρα (Anchor)

Based on the Wiktionary entry, the modern Greek word **άγκυρα** (ágkyra) comes from Ancient Greek:

> "From Ancient Greek ἄγκυρα (ánkura)."

The entry indicates this term has deeper Proto-Indo-European roots, as evidenced by the categories mentioning derivation from the PIE root *h₂enk-. However, the page does not provide detailed information about cognates in Latin, Persian, or Arabic, so I cannot quote etymological connections to those languages from this source.

The word is a feminine noun in modern Greek with nautical significance, meaning "anchor," and follows standard Greek declension patterns for words of its type.
```


### [2026-09-04T22:52:06.488Z] TOOL RESULT

```
# Sanskrit चतुरङ्ग (Caturaṅga)

## Meaning and Composition

The term literally means "having 4 limbs." It combines two Sanskrit elements:
- **चतुर् (catúr)**: "four"
- **अङ्ग (áṅga)**: "limb, member"

## Definition

According to the Wiktionary entry, चतुरङ्ग functions as both an adjective and noun. As an adjective, it describes something with four components. The noun form has multiple senses, including a type of chess played by four parties and a reference to a four-part military formation (elephants, chariots, cavalry, and infantry).

## Historical Quote

The term appears in ancient Sanskrit literature: *"ते हि द्यावा॑पृथि॒वी भूरि॑रेतसा॒ नरा॒शंस॒श्चतु॑रङ्गो य॒मोऽदि॑तिः"* from the Rigveda (10.92.11, circa 1500-1000 BCE).

## Linguistic Descendants

The word traveled extensively through historical trade and cultural routes:
- **Middle Persian**: čatrang
- **Persian**: چترنگ (čatrang)
- **Arabic**: شطرنج (šaṭranj)
- **Malay**: catur
- **Malayalam**: ചതുരംഗം (caturaṅgaṁ)
```


## [2026-09-04T22:52:12.790Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%98%D9%88%DA%98%D9%87",
 "prompt": "Persian ژوژه: meaning and etymology (Middle Persian zūzag, Avestan duždaka?). Quote whatever the page says. If the page does not exist, say so."
}
```


### [2026-09-04T22:52:14.947Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T22:52:15.314Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D9%86%DA%AF%D8%B4%D8%AA/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for انگشت, including any bracketed etymology such as [پهلوی angušt] or Avestan/Pahlavi forms. Also quote the لغت‌نامه دهخدا etymology if present."
}
```


### [2026-09-04T22:52:28.433Z] TOOL RESULT

```
# انگشت (Finger/Digit)

## Dehkhoda Dictionary Etymology
The Dehkhoda entry traces the word through Persian literary tradition, citing classical poets like Ferdowsi and providing extensive metaphorical uses. The dictionary notes synonyms including "اصبع" and "بنان."

## Mo'in Dictionary Entry
According to Mo'in: *"(اَ گُ ) هر یک از اجزای متحرک پنجة دست و پای انسان که بر سر آن ها ناخن روییده است"* — each of the five moving parts of human hands and feet that have nails.

The entry also documents the alternate meaning: *"(اَ گِ ) زغال، زگال"* — charcoal or coal (with different vowelization).

## Primary Meanings
1. **Anatomical**: One of five digits on hands or feet
2. **Historical**: A measurement unit (15-20 millimeters)
3. **Alternative**: Charcoal produced from incomplete combustion of wood

The page notes this dual meaning distinction is important—the two pronunciations (ضمه vs. کسره on the first letter) differentiate the anatomical from the combustion-related sense.
```


## [2026-09-04T22:52:40.526Z] TOOL CALL #74: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂enk-\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%DA%AF%D8%B4%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%D9%84%D9%86%DA%AF%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D8%B7%D8%B1%D9%86%D8%AC\" \\\n \"https://www.etymonline.com/word/palanquin\" \\\n \"https://www.etymonline.com/word/anchor\" \\\n \"https://www.etymonline.com/word/England\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%9A%E0%A4%A4%E0%A5%81%E0%A4%B0%E0%A4%99%E0%A5%8D%E0%A4%97\" \\\n ; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 56, root Ang/Ank/Anq\" 2>&1 | tail -2; done",
 "description": "Archive web sources used"
}
```


### [2026-09-04T22:52:44.318Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9226fe598862fa48.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bf3815529bf894ec.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b149a3e7fcf34285.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4cb87853e3138977.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3247fbcdd9dbeb4b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5be8043936e16396.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2e47fefd0cfdee4f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0e41c3bff20a3e07.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0988ce575b67871f.txt
```


## [2026-09-04T22:52:52.157Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/ingiliz",
 "prompt": "Give the etymology of Turkish İngiliz: source language (Italian inglese?), date of first attestation, and quote the entry."
}
```


## [2026-09-04T22:52:52.641Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/anglais",
 "prompt": "French anglais: etymology — from Old French, from Latin Anglenses/Anglicus, from Angli. Quote it."
}
```


### [2026-09-04T22:52:56.939Z] TOOL RESULT

```
I cannot provide the requested information based on the content shown. The webpage displays only the header, navigation elements, and footer of Nişanyan Sözlük (Nişanyan Dictionary), but does not include the actual dictionary entry for "İngiliz" that would contain its etymology, source language, date of first attestation, or the quoted entry text.

To obtain this information, you would need to access the full entry for "İngiliz" on the Nişanyan Sözlük website directly.
```


### [2026-09-04T22:52:59.542Z] TOOL RESULT

```
# Analysis of "anglais"

Based on the Wiktionary entry, **anglais** has two primary meanings:

## French Usage

As an adjective, it means "English" (relating to England or English people). As a noun, it refers to the English language itself.

The etymology traces back through Middle French and Old French *anglois*, ultimately deriving from Latin *Anglus* and Proto-Germanic roots meaning "pertaining to the Angles."

## Irish Usage

In Irish, **anglais** is a feminine noun with a completely different meaning: "milk diluted with water" or, figuratively, "a milksop" (a weak person). It descends from Old Irish *englas/anglas*.

The French and Irish definitions are entirely unrelated despite sharing the same spelling, representing a case of homonymy across languages.
```


## [2026-09-04T22:53:06.740Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### ARY انگشت\"; grep -n \"انگشت\" incoming/ARY/ARY_pages.txt | head -8; echo \"### ARY لنگر\"; grep -n \"لنگر\" incoming/ARY/ARY_pages.txt | head -8; echo \"### ARY latin index ANG\"; grep -n -i \"ANK\\b\\|ANG-\\|ANGUSHT\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Grep Aryanpur IE roots dictionary"
}
```


### [2026-09-04T22:53:06.832Z] TOOL RESULT

```
### ARY انگشت
4488:۴ واژه‌ی لاتین ۳01183 به چم اانگشت شست" نیز از همین ربشه است.
4978:معنی واژه‌ی لیتوانی و اسلاوکهن این فهرست: انگشت,.
6678:۱- چم این واژه در برهان قاطع : چنین است: قلاب» کجکه (قلابی که با آن فبل را رانند)» پنجه و انگشتان مردم»
12035:چم اپن واژه در زبان آلمانی: بند انگشت.
### ARY لنگر
### ARY latin index ANG
2653:ONELEOW OLD ENGLISH) aS 5S: ANGUSHTA YAVESTAN) gle
5841:TANK :(TOKHARIAN A) A 5,55 » AUAAVESTAN) gle)
5842:TANK -(TOKHARIAN B) B 5 5 ‘TAXMA, TANGCISHTA
5846:THETTR TANK ABALUCHD) oo sh
5934:wank Fy oFy 9 Ce SAS eS Os 22 0513 ool pe
6182:YAOUANK HBRETON) 35 2 PORTUGUESE) J
8123:DAMP, DANK (ENGLISH) 55S! SANSKRIT) <p Suile
10885:PECKU "(OLD PRUSSIAN) 45 gos. SHAWANK, HBALUCHD) gr gy
10886:SHIPANK
13201:LAG (SWEDISH) 55 y LINK, LANK, LINGE :(KURDISH) 52,5
```


## [2026-09-04T22:53:09.966Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4470,4500p' incoming/ARY/ARY_pages.txt; echo \"=== 6665-6700 ===\"; sed -n '6665,6700p' incoming/ARY/ARY_pages.txt",
 "description": "Print Aryanpur context"
}
```


### [2026-09-04T22:53:10.027Z] TOOL RESULT

```
فریزی کهن ((۳8/514): #لشآ ۲ بش71 ایرلندی کهن (87ل17 2ا0): 11
آلمانی کهن (08721404 04اب )+ 8
501 پسگشت‌ها ۲ آشک رت دا
آلمانی (08794/(0): ۳1 :۶۵00 1
انگلیسی کهن (8۸/01380 ۰:0۵ ۴8۲۸ 4 (ا۴۴5) 7
انگلیسی (8ا/۵: اد داد ناسنا ِ نا
دانمارکی (0۸(/757): 80 9 (585) :0705
هلندی (ع7ا0): ۷۵8 (ا5ظ۲۴) +347
اسلاوی کهن 7ل0(0376 ملک (0). 81 :که #متتمهد
ت۴۸ ,2۸11 برهان قاطع : ۳۵۹
روسی (/#5514): ۳۸33۴ ,887-8۸817 فرهنگ معین : ۰ ۶۸۰
بلغاری (ا#ملمه.الاه: ۲۸۷ لغت‌نامه دهخدا: ۵۳۸۸
صربی (587814۷): ۳۳ 0
یادداشت:,
۱ معنی این واژه در اپرلندی کهن: کف دست.
۲ معنی این واژه در زبان‌های ژرمنی: احساس کردن» پرماسیدن,
۳- واژه‌ی "پرماس ""پرماسیدن (پهلری: ۳۸188۸8) به چم "با دست احساس کردن" نیز به احتمال ضعیف با این
واجريشه خویشی دارد.
۴ واژه‌ی لاتین ۳01183 به چم اانگشت شست" نیز از همین ربشه است.
فارسی (2885]4۸): پالیز, فالیز, جالیز, پردیس (به چم "باغ" ابوستان)
اوستایی (4ل۸874): ۳۸۸۸ لانین (7700ضا): 05
پارسی باستان (۷مماق۴8۴ صاه): فرانسه ‎ :)۳88(/601(‏ 5
۳105 اسپانبایی (52۸/187): ۳0
کردی (70154): 7 ,8855 ایتالیایی (۸۸لم17): 50
سانسکریت (54۸/58/7): آ۹۳21+05178/1 رومانی (8714۸۸۵/4): ۳5
ارمنی (/448014): 8۸82082 ۳۸752 پر تغالی (۳07701582): زان ات اما
بونانی (0۸54): آلمانی (/05701۸2): ۳5
5 ,۲۸۹08018085 انگلیسی کهن (4ل8الا800 ص۵): ۰8۸۸0188
۹
[pdf page 154]
ی
=== 6665-6700 ===
انگلیسی کهن (80لا20 ۰:02 1104 اسلوا کی (81.01420): 3
انگلیسی (3لولا6۸/0): 1100 لیترانی (4(۷هنا 72 ل): ید4
دانمارکی (3ل0۸(75): 1۸0 ایرلندی میانه (52ل8ز ۵/0202 ۰.17806
سوئدی (8178015[4): 1
[pdf page 227]
۸ | _چه چي (به چم "چه چیزی)
پسگشت‌ها دشر داد 7 (11006) :01025
۳ 17
0 (1300) 8۸82/0 برهان قاطع زا 9 : ۶۶۴
10 84 او

یادداشت: 1

۱- چم این واژه در برهان قاطع : چنین است: قلاب» کجکه (قلابی که با آن فبل را رانند)» پنجه و انگشتان مردم»

چنگال مرغان و جانوران دیگر (برهان قاطع :: ۹3۴)

۲ چم این واژه در اوستی: بازو,

چم این واژه در کردی: دست.

چم این واژه در ایسلندی کهن: خانه,

چم این واژه در اکثر زبان‌های ژرمنی: قلاب, ۱

1

| جمانگلیس سرواژهی را ی ۵5
اوستایی ((4874): 37 ,۲17 نروژی (08۷۴01۵۷/): 11۷۸ ,3۷1 ,11۷1
پارسی باستان (۶88814۷ 010): لهستانی (۳0[5): اد

,030 روسی (//551۸)+ 11

پپلوی (41آللم). دز چکه (2504)): 40 باآ۳03
تخاری ۸ (۸ ۸(7ل70727۸7): 18 اسلواکی (5701430): 1
تخاری 8 (8 (4۸7ق707): ناه ایرلندی کهن (5[0ل1# صان): ه
```


## [2026-09-04T22:53:19.006Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ANGUSHTA\\|۸۸60513۸\\|ANGUSHT\" incoming/ARY/ARY_pages.txt incoming/ARY/ARY_latin_index_pages.txt | head; echo \"---\"; sed -n '2648,2660p' incoming/ARY/ARY_latin_index_pages.txt",
 "description": "Find Aryanpur ANGUSHTA reference"
}
```


### [2026-09-04T22:53:19.069Z] TOOL RESULT

```
incoming/ARY/ARY_latin_index_pages.txt:2653:ONELEOW OLD ENGLISH) aS 5S: ANGUSHTA YAVESTAN) gle
---
ror! lapaas dato) DELAMARRE: (VISCERES) 146
BUCK: 282
Jeetloak
sagls Sealan y ote lal oats Slay Ugly cl aly! OE Sead claslety 5h ey jail” BeSly -1
aa gith ig BY
ONELEOW OLD ENGLISH) aS 5S: ANGUSHTA YAVESTAN) gle
ANKLE ENGLISH) godt} ANGST — «(OLD PERSIAN) gals)
ANKEL . (DANISH) Sails ANGUST (PAHLAVI) 5 hay
ANKEL SWEDISH) (54 pe ANGAM, (SANSKRIT) ny Site
ANKEL (NORWEGIAN) 5335 ANGULI, ANGA, ANKA
ENKEL (DUTCH) sche ANGIUN, ANKIUN (ARMENIAN) .)\
MYKSHTIS (LITHUANIAN) gi g-3 ANKOS, AGKOS, (GREER) lin
ANKULUS
```


## [2026-09-04T22:53:33.097Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### NYB zwzk\"; grep -n -i \"zwzk\\|zuzag\\|zūzag\" NYB_vol2_glossary.txt NYB_vol1.txt | head -5; echo \"### RCH langar\"; grep -n -i \"langar\" RCH.txt | head -5; echo \"### AFM shatranj/anjar\"; grep -n \"شطرنج\\|أنجر\\|الأنجر\" AFM.txt | head -8; echo \"### PLA\"; grep -n -i \"satrang\\|šatrang\\|Schach\\|Anker\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10",
 "description": "Grep Nyberg, Richardson, Addi Shir, Asbaghi"
}
```


### [2026-09-04T22:53:33.189Z] TOOL RESULT

```
### NYB zwzk
### RCH langar
20298:Palangary  Name  of  a   king  slain  by  Alexander, p   palang-rangy  (A*  horse)  spotted  like  a   leoparu*
32395:p chahar  langary  The  legs  or  feet  of  quadrupeds, p   chahdrumy  The  fourth#
43267:p   rasan^  A   rope,  string,  cord,  thread. kishit^  A   hawser.  rasan-i  langar^  A   ship’s  cable.
74675:p langar^  An  anchor.  A   stay  or  rope  for  supporting  a   i tent.  The  house  or  monastery  of  the  Calendars  or  Muhairima-  ! dan  monks.  An  alms-house.  The  plaits  of  a   robe.  Worthless,  ■ mean,  fraudulent,  deceitful,  disliked  by  every  body.  Strong,  j powerful.  Majesty,  authority.  Modesty,  mildness. langar  andakhlan  (or  langar  nihadan)^  To  cast  an- chor. ^   langar  bar  uzoardan  (or  langar
74678:p   langar tf  Provisions  distributed  to  the  poor.  A   kind  of drinking-glass.
### AFM shatranj/anjar
2604:الغاب في الشطرنج ٠‏ فارسيّتها دست أخذتمهسا العرب وتصرفت بها ١‏ وقد اجتمع أكثر 
4138:وان وذ بره بإد#هر ܠܝ قبالتها لعبة الترد ܝܨ معروفة ٠‏ والشطرنج معرب 29 
4139:سترنك ٠‏ وقال المعض ان الذي اخترع الشطرنج رجل اسمة ضصه والظاهر اانه ابن 
4830:5 صار فرزانً من الفرزان وهي الملكة في لعبة الشطرنج مشتق 
5516:دكش ) 0 رقعة الشطرنج فارسيّة اضلها كشت أي 0) 
### PLA
3096:jeDi - "Anker" pers. 3 aus pers. _{J langar, mand. angara 4 lat. ancora. 
10232:E- ruh: "der Turm beim Schachspiel" pers. 2, 
12895:Schach <T Ders. >; ar. > frz. ”, mhd. schach, afrz. eschac zu pers. 
12963:Osuelü - Sähsawan: "Schahseven od. Schachseven; iranische Fußtruppe" pers. 
12970:bLoll - Sähmät: "Schachmatt" pers. >>ar. 3 s. an. 
13240:e> $Satrang: "Schachspiel sd satrang pers. $Satrang mp. 
13242:dtsch. Schach <T afrz. echac zu pers. Schah 4, 
15159:ob - farzän: "die Königin im Schach" pers. s. farzäna 
15606:a“ - fil?: "der Läufer im Schach".
```


## [2026-09-04T22:53:42.331Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3090,3100p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; echo \"=== 13235-13250 ===\"; sed -n '13235,13250p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; echo \"=== AFM 4130-4145 ===\"; sed -n '4130,4145p' AFM.txt",
 "description": "Print Asbaghi and Addi Shir entries"
}
```


### [2026-09-04T22:53:42.396Z] TOOL RESULT

```
Slası - ”’anfudän: "Sylphium, Laserpitium, Assafatida" pers. 2, aram. gl 
ots - ”ankudan = ’anfudän s. ”ankudän , 


: Fr 
jeDi - "Anker" pers. 3 aus pers. _{J langar, mand. angara 4 lat. ancora. 


5 
e,»1 - ”anfura: "Nessel" pers. 
=== 13235-13250 ===
or Sass: "Angelhaken" _ pers... Sast 2, 


. £ . L. 
-._ . u" nv RT) 
e> $Satrang: "Schachspiel sd satrang pers. $Satrang mp. 
yPpyg catrang skr. caturanga ”. 
dtsch. Schach <T afrz. echac zu pers. Schah 4, 


Juü - Sagal: "Schakal" tk. tschakal pers. Ju schagal < mp. 
Y- wu shaghal 6, syr.\e pers. ger 7, dtsch. Schakal <T skr. >> pers, 


SbLS - Sarfapäna: "Hospital" ägypt. Ar, 9 

=== AFM 4130-4145 ===
يلبيب ومن هناك تناولة الفرس ( حيط المحيط ) ‹ قال في الإبهان القاطع : « ܚܡ ܙܝ 
باتكاف الفارسية السطرنج وهو لعبة معروفة من مخترعات داهر الحكيٍ الحندي وقيل 


> )7 ܀ [ ܨ 


بل من مخترعات ابنه ٠‏ وذهب قوم الى ان هذه اللععة رمك فى لكان انوشروان 
وان وذ بره بإد#هر ܠܝ قبالتها لعبة الترد ܝܨ معروفة ٠‏ والشطرنج معرب 29 
سترنك ٠‏ وقال المعض ان الذي اخترع الشطرنج رجل اسمة ضصه والظاهر اانه ابن 
داهر المذ كور ». ٠وعلدي‏ 0 الفارسي 2 10 ا اي الشاه لطيف او | ܐܚܐܘ 
اللطيف او 2 ܓ ` يعطيها 
بعد 5 الى 5 9 ومعناة القهارء او ܇ 
وهو العدو ܐܚ المندنة نه ومن 58 رسا + والمشة اي حيلة الوذ اف عست 
ومن الفارسي 0 ܐܐܠ (00:0?§ ` ܕܐܡܥ والكردي ل رنج 1 
ܝܝ ٠‏ وكذلك 9055 5 - :3:9 الموجودة £ 0:30000
```


## [2026-09-04T22:53:56.693Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### LAT angulus\"; grep -n -A6 \"^angulus\" LAT.txt | head -20; echo \"### LEW angulus\"; grep -n -i \"angulus\" LEW_1910.txt | head -5; echo \"### HJB palankeen\"; grep -n -i \"PALANKEEN\\|PALANQUIN, s\\.\" HJB.txt | head -6",
 "description": "Grep Ernout-Meillet, Walde, Hobson-Jobson"
}
```


### [2026-09-04T22:53:56.768Z] TOOL RESULT

```
### LAT angulus
3858:angulus, -i (anglus dans l'app. Probi) m.: eoin [d'un edifice], angle
3859-(yuwux). — Ancien, technique, usuel. M.L.465. Britt . ong l.
3860-Deriv 4 s: angellus: petit coin, petit angle; angularis (lapisj ; angu¬
3861-larius (cx.X.); angulatus: muni d'angles; d'ou angulare, M.L.464;
3862-angulosus: 7roXuywv lo£;
3863-Second terme de composes: acuti-, obtusi-, rect-, tri-, quadri-,
3864-sex-, oct-, uiginti-angulus, qui traduisent des ccmposes techniques
### LEW angulus
### HJB palankeen
2805:[184S.— "  I  engaged  eight  bearers  to  carry my  palankeen.  Besides  these  I  had  four lMUigfay-&«re2izr«,  men  who  are  each  obliged to  carry  forty  pound  weight,  in  small wooden  or  tin  boxes,  called  petarrahi.** — TrattUn't  aeeommt,  Carey,  Good  Old  Days, ii.91.]
3213:1768-71.— "Every  house  has  likewise  .  .  . one  or  two  sets  of  bems,  or  palankeen- bearers." — StavorimMMj  i.  528.
3217:1782.—".  .  .  imposition  .  .  .  that  a gentleman  should  pay  a  rascal  of  a  Sirdar Bearer  monthly  wa^es  for  8  or  10  men  .  .  . out  of  whom  he  gives  4,  or  may  perha^ indulffe  his  master  with  5,  to  carry  lus palankeen."— /iMttd  Qazette^  Sept.  2.
3977:1785.— "The  boys  with  Colonel  Law- renoe's  palankeen  having  straggled  a  little ont  of  the  line  of  march,  were  ]ncked  up  b^ the  Morattas." — Carracciolt^  Life  of  Clive,  i. 207.
3980:1810. — "The  palankeen-bearers  are  called Bhoii,  and  are  remarkable  for  strength  and swiftnees.  "—i/aria  Grukam,  128.
5477:quently  in  Mr.  Talboys  Wheeler's extracts  from  them.  They  are  men- tioned by  Couto.  [See  Nelwn,  Maduray Pt  ii.  p.  4  ;  Opvert,  Orig,  Inhab.  p.  67.1 Sir  Walter  Elliot  considers  this  feud to  be  ^*  nothing  else  than  the  occasional outbreak  of  the  smouldering  antagonism between  Brahmanism  and  Buddhism, although  in  the  lapse  of  ages  both parties  have  lost  sight  of  tne  fact. The  points  on  whicn  they  split  now are  mere  trifles,  such  as  parading  on horse-back  or  in  a  palankeen  in  pro- cession, erecting  a  patTiila.l  or  marriage- shed  on  a  given  number  of  pillars,  and claiming  to  carry  certain  flags,  &c.  The right-hand  party  is  headed  bv  the Brahmans,  and  includes  the  l^arias, who  assume  the  van,  beating  their tom-toms  when  they  come  to  blows. The  chief  of  the  left-hand  are  the Panchalars  [i.e,  the  Five  Classes, workers  in  metal  and  stone,  &c.], followed  by  the  Pallars  and  workers in  leather,  who  sound  their  long trumpets  and  engage  the  Farias."  (In Joum,  Ethnol  Soc.  N.S.  1869,  p.  112.)
```


## [2026-09-04T22:54:01.324Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"PALANKEEN\" HJB.txt | head -3; grep -n -i \"palki\\|palanquim\\|palyanka\\|paryanka\" HJB.txt | head -10",
 "description": "Find Hobson-Jobson palankeen headword"
}
```


### [2026-09-04T22:54:01.416Z] TOOL RESULT

```
16332:669    PALANKEEN,  PALANQUIN.
16335:PALANKEEN,  PALANQUIN,  s.
16345:PALANKEEN,  PALANQUIN.    660    PALANKEEN,  PALANQUIN.
3208:BEABES,  s.  The  word  has  two meanings  in  Anglo-Indian  colloquial : a.  A  palanauin-carrier ;  b.  (In  the Bengal  Fresiaency)  a  domestic  servant who  has  charge  ol  his  master's  clothes, household  furniture,  and  (often)  of his  ready  money.  The  word  in  the latter  meaning  has  been  regarded  as distinct  in  origin,  and  is  stated  by Wilson  to  be  a  corruption  of  the Bengali  wMra  from  Skt.  vyavahdrty a  domestic  servant.  There  seems, however,  to  be  no  historiccU  evidence for  such  an  origin,  e.g,  in  any  ha- bitual use  of  the  term  vehdrdy  whilst as  a  matter  of  fact  the  domestic  bearer (or  drddr-bearery  as  he  is  usually  styled by  his  fellow-servants,  often  even  when he  has  no  one  under  him)  was  in Calcutta,  in  the  penultimate  generation when  English  gentlemen  still  kept palankins,  usually  just  what  this literally  implies,  viz.  the  head-man of  a  set  of  palankin-bearers.  And throughout  the  Presidency  the  bearer, or  valet^  still,  as  a  rule,  belongs  to the  caste  of  Kahdrs  (see  KUHi^,  or palki-bearers.    [See  BOY.]
16337:The  origin  of  the  word  is  not  doubt- ful, thou^  it  is  by  no  means  clear how  the  Portuguese  got  the  exact  form which  they  have  handed  over  to  us. The  nasal  termination  may  be  dismissed as  a  usual  Portuguese  addition,  such as  occurs  in  mandarin,  Bagaim  (JVasai), and  many  other  words  and  names  as used  by  them.  The  basis  of  all  the forms  IS  Skt.  paryanka,  or  palyanka, *a  bed,'  from  which  we  have  Hind, and  Mahr.  palang,  *  a  bed,'  Hind,  pdlki, *a  palankin,'  [Telugu  palUtM,  which  is pernaps  the  origin  of  the  Port,  word], l^ali  pallanko,  *a  couch,  bed,  litter,  or palankin'  (Ohilders),  and  in  Javanese and  Malay  palangki,  '  a  litter  or  sedan ' {Ora/wfurd).*
16447:1878. — "The  Governor-General's  carriage .  .  .  may  be  jostled  by  the  hired  'palki- gharry,'  with  its  two  wretched  ponies,  rope harness,  nearly  naked  driver,  and  wheels whose  sinuous  motions  impress  one  with the  idea  that  they  roust  come  off  at  the next  revolution." — Life  in  the  Mofussil,  i.  38.
```


## [2026-09-04T22:54:19.152Z] TOOL CALL #84: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3/",
 "prompt": "Quote the Dehkhoda (لغت‌نامه دهخدا) and Mo'in (فرهنگ معین) entries for انگلیس, especially any statement of the word's origin (e.g. فرانسوی anglais, ایتالیایی inglese, ترکی ingiliz)."
}
```


### [2026-09-04T22:54:25.252Z] TOOL RESULT

```
# Dehkhoda and Mo'in Entries for انگلیس

Based on the dictionary content provided, here are the relevant entries:

## Dehkhoda Dictionary (لغت‌نامه دهخدا)

The Dehkhoda entry defines انگلیس in two ways:

1. As a noun: "مردم انگلستان" (the people of England), specifically "شعبه ای از نژاد ژرمن ساکن بریتانیای کبیر" (a branch of the Germanic race inhabiting Great Britain)

2. As an adjective: Used colloquially as a substitute for "انگلیسی" (English)

The entry lists variants including: انکلیس، انقلیس، مارماهی

## Mo'in Dictionary (فرهنگ معین)

The Mo'in entry provides similar definitions but notably does not include an explicit statement about the word's etymological origin (such as derivation from French *anglais*, Italian *inglese*, or Turkish *ingiliz*) in the sections presented here.

**Note:** The document does not contain clear etymological citations tracing انگلیس to Romance language sources in the Dehkhoda or Mo'in sections shown.
```


## [2026-09-04T22:56:04.420Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD catrang\"; grep -n -i \"catrang\\|čatrang\\|chess\" PHD.txt PHD_mackenzie.txt | head -6; echo \"### PHD angust\"; grep -n -i \"angust\" PHD.txt PHD_mackenzie.txt | head -6; echo \"### FRS shatrang\"; grep -n \"شترنگ\\|شترنج\" FRS.txt FRS_pages.txt | head -6; echo \"### NYB angust\"; grep -n -i \"angust\" NYB_vol2_glossary.txt | head -5",
 "description": "Grep MacKenzie, Loghat-e Fors, Nyberg"
}
```


### [2026-09-04T22:56:04.556Z] TOOL RESULT

```
### PHD catrang
PHD.txt:130:delete ozarak ... padist ... add threat. pad-nigerián ... for cared for, guarded read carefully. add  parisp [plsp | M prysp] wall. ?pid ... add (M pyt). purnay [pwin'd = Av. pərənayu-] adult. add  purr-marg |-mlg| deadly, baneful. raz ... add M rz. add rebas [lyp's | N ~] rhubarb. ?ristag ... add N rasta. add гох [lhw' | N <] rook, castle (chess). sahistan ... read (M shyd, P s‘y-). add sārwār [s ]w I helmet. add  sayistan, say- [ŠKBHWN-tn < A Vškb | P sy-] lie down.
PHD.txt:219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
PHD.txt:298:čāšt [ой | N ~] lunch, meal. 1~ag [-k'] food. &а$їар [c'štk'] doctrine. čāštan, čāš- [c?s-tn'] teach. ~išn: teaching. čatrang [cting | (Ar. šatranj)] chess. *taw(la)gan [cwpk'n!! | Ar. sawlajan, N čaugān] (curved) polo-stick ; polo. CaxSágih [ch kyh] (sense of) taste. čaxšišn [chsfn! | M, J схі, N ¿aš-] taste, flavour. 148 [ME < A mh | M cy, N či] what, which. ~ ray: for what, why. ~ih: quiddity, essence. tčē [ME, v. 166] for, because, since, as, that. &ë-ëwënag [ME ^ dwynk!] how. ~ith : circumstances. čegām-iz [су?т-с | M cyg^myc], —-6(w): a little; whatever. Cegámag [cyk”mk! | N &(ag)áma] song, snatch. €éh- , —išn, v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr, № ~] form, shape, appearance, face. žčihr(aģ) [cyhl(k') | M сулу, P -g, № ~] seed, origin; nature, essence. Cihrénidan, čihrēn- (cyhlyn-ytn'] form. Cihrig [cyhlyk'] natural. čihr-šnāsīh [суйру] physics. čim [c(y)m | M сут, N ~] reason, cause, purpose, meaning. ~ (ray): why? Cim-gó6wáàgih [сут gwh’kyh] logic. čimīģ [cymyk!] purposeful. čīn-, ~i8n, v. idan. čīnag [cynk! | P cyng, N ~a] grain, bait. Cinàr [су | N ~] oriental plane tree. činwad [cynw(p)t'], ~ puhl: the ‘divider bridge’ which separates the souls of the righteous dead, who cross, from those of the wicked, who fall off.
PHD.txt:358:frazën [plcyn' | N farzin] (chess) queen (lit. ‘guard’).
PHD.txt:439:~ith: femininity. *madag [mtk' | (M myg, N māya)] essence, substance. ~ig [-yÀ!] essential. ~war [-w/] essential, especial, principal. madan [mtn! | M mdn] come. madār [т comer. mādar [AMYtl < А т-у; mtl | M mdr, N ~] mother. imādayān [m!tgd?n! | М m'dy'n] book. *mādayān [m tyd?n'] essence, basis, core; essential, chief. mādayār [m tgd’l] steward; (chess) rook, castle. mādišt [m’tyst'] *matter, protoplasm. mādīyān [m’tyg?n | N ~] mare. may [my | N ~] hole, pit. magas [mks | P mgs, N ~] fly. ~ i angubén: honey-bee. magind [mkn'd | M mgyn(d)] shield, protection.
PHD.txt:545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
### PHD angust
PHD.txt:212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
PHD.txt:1942:finger angust.
PHD.txt:1943:finger-guard angustbàn.
PHD.txt:1944:finger ring angustarig.
PHD.txt:4023:toe angust.
PHD.txt:4427:I angust = š іп. ‘finger’ 1 widest (12 a.) = 9 in. 'span'
### FRS shatrang
### NYB angust
453:angust
454:angust [’ngwst'] finger 2611, 2911; a linear measure 9374, — SW form with -st < -št; NP angust NW form. Paz. both angust and angušt.
841:ayinaftan [’dynptn'] to reach, to get at, to touch: 6 mar gav ayinaft as for the scoundrel, (his) hands touched 61", with the gl. kū-š ēvak pat dit frac zat he clapped his hands together; 6¢ mar han i dašn gav 6 rān apar ayinaft as for the secundrel, (his) right hand got at his hip = the scoundrel put his right hand on his hip 61%; [yērtāt bē ahi/ayi/-naftak 4 angust but the corn had reached the height of 4 fingers PR 29° (written *hdynptk', a
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
6370:andaxtan, andaz-: han- daxtan andčxtan: handčxtan ančran: anagr ančrang: ~ anast: ~ angàra: hangärak angärdan: hangärtan angidi: hangatöh angirdi: hangirtikéh angošidaa: hangošitak angust | angušt | anžamešn: hanjam- ānō: änöd aoj: OZ apar: appar apardan apar-| eaipuntan aparasn | apatūihā: apatundihā apēdā: apaitāk apčišn: apöhisn apurašn: appurišn apurnāē: apurnāi ārāmed: ahrām- ārāstan ārāēd: ārāstan ar(a)šk: arišk ar(a)tištara: artēštār
```


## [2026-09-04T22:56:17.919Z] TOOL CALL #86: Bash

```json
{
 "command": "for u in \\\n \"https://abadis.ir/fatofa/%D8%A7%D9%86%DA%AF%D8%B4%D8%AA/\" \\\n \"https://abadis.ir/fatofa/%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3/\" \\\n \"https://en.wiktionary.org/wiki/anglais\" \\\n \"https://en.wiktionary.org/wiki/%CE%AC%CE%B3%CE%BA%CF%85%CF%81%CE%B1\" \\\n ; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 56, root Ang/Ank/Anq\" 2>&1 | tail -1; done",
 "description": "Archive remaining sources"
}
```


### [2026-09-04T22:56:24.391Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/839e73f53001405e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9d8f72780bec0a2e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/adae17388b0f3fec.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8b2dbd2897dcdca6.txt
```


## [2026-09-04T22:56:26.947Z] TOOL CALL #87: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Inspect verify_check script"
}
```


### [2026-09-04T22:56:27.003Z] TOOL RESULT

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


## [2026-09-04T22:56:29.939Z] TOOL CALL #88: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-04T22:56:29.998Z] TOOL RESULT

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
```


## [2026-09-04T23:03:03.109Z] TOOL CALL #89: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build56.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nentry = {\n \"entry\": 0,\n \"root\": \"Ang, Ank, Anq\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₂enk- / *h₂eng- 'to bend, curve' (Pokorny '2. ank-, ang- „biegen“', IEW 45–47; Watkins/AHD 'ank-, also ang-. To bend')\",\n \"note\": \"Root, language label and gloss are all correct and standard. Nourai's three-way root name 'Ang, Ank, Anq' is taken verbatim from Klein, who ends his 'angle (corner)' article (KLN p.75) with 'All these words derive fr. I.-E. base *ang-, resp. *anq-, “to bend”'. Pokorny's article runs IEW 45–47: the headword '2. ank-, ang- „biegen“; Nominalstämme anko-, onko-; ankes-; anku-lo-; anken-, -on-; ankoto-; ankro-' stands on p.45 (so Watkins cites '[Pok. 2. ank-, ang- 45]'), the sub-article 'ang-, bes. zur Bezeichnung von Gliedmaßen' with ai. áṅgam / aṅguṣṭha- = av. aṅgušta- and lat. angulus stands on p.46–47 — so POK:46 is a fair citation for the branches Nourai draws from it. Caveat for modern practice: laryngeal-era scholarship splits Pokorny's single lemma. Wiktionary keeps *h₂enk- 'curve, bend' (Skt. áñcati, Gk. ἄγκυρα, ἀγκὼν, Lat. ancus) apart from the 'limb/finger' family *h₂eng- (Skt. áṅga-, aṅguṣṭha-, Av. aṅgušta-, MP angust), and Mann (IEC) lists ang-, anghulos, anguos, ankotos, ankuros as separate lemmata, deriving Lat. angulus from *anghulos rather than *ank-. Nourai's single root box therefore merges two (probably but not certainly related) roots — the traditional Pokorny/Klein/Watkins position. Two whole limbs of the chart are, additionally, cultural loans rather than inherited descent (Gk. ἄγκυρα → Pers. langar; Skt. caturaṅga → Pahl. čatrang), which the chart's arrows do not distinguish; and the French→Persian limb (#20–#21) is wrong, see those nodes.\",\n \"sources\": [\n   W+\"Reconstruction:Proto-Indo-European/h₂enk-\",\n   \"https://www.etymonline.com/word/anchor\"\n ],\n \"ref_check\": [\n   {\"ref\": \"POK:46\", \"status\": \"supports\",\n    \"note\": \"POK_01.txt (Pokorny IEW Band I) — page marker '45' precedes '2. ank-, ang- ,biegen‘; Nominalstämme anko-, onko-; ankes-; anku-lo-; anken-, -on-; ankoto-; ankro-', and between markers '4G'(=46) and '47' stands the sub-article 'ang-, bes. zur Bezeichnung von Gliedmaßen (vgl. got. lipus ‚Glied‘: *lei- ‚biegen‘): Ai. áṅgam ‚Glied‘, aṅgūli-ḥ, aṅgūri-ḥ f. ‚Finger, Zehe‘ ... aṅguṣṭha-ḥ ‚große Zehe, Daumen‘ == av. aṅgušta- m. ‚Zehe‘' plus 'lat. angulus ... ‚Winkel‘' — exactly the material Nourai hangs on this page. Reference: WP. I 60f., WH. I 46, 49f.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW I 45–47 s.v. 2. ank-, ang-\", \"stance\": \"supports\",\n    \"note\": \"the whole page-56 chart is essentially an English redrawing of this one Pokorny article: 'Ai. ancati (mpers. ancītan) ... ‚biegt, krümmt‘ ... av. anku-pəsəmna- ‚mit Haken, Spangen sich schmückend‘ ... av. aka- m. ‚Haken, Zapfen‘ ... ἄγκυρα ‚Anker‘ ... lat. angulus ... Much stellt hierher den lat.-germ. VN Anglii, ags. Angel, Ongel'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. ank-\", \"stance\": \"supports\",\n    \"note\": \"'ank-. Also ang-. To bend. I. Germanic *ank- ... ANKLE. II. Suffixed form *ank-ulo-. 1. Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE; b. probably Latin Angli, the Angles: ANGLE. ... III. Greek ankura, anchor: ANCHOR. ... V. Sanskrit anka, hook, ancati, he bends: PALANQUIN. ... VII. Suffixed form *ang-olo- in Latin angulus, angle, corner: ANGLE. [Pok. 2. ank-, ang- 45.]' — covers seven of Nourai's eleven root-level branches.\"},\n   {\"src\": \"KLN\", \"where\": \"p.75 s.v. angle, n., corner\", \"stance\": \"supports\",\n    \"note\": \"'L. angulus ... cogn. with Arm. angiun, ankiun, OSlav. ǫg(u)lu “corner”, OSlav. ǫkotu “hook”, Lith. anka “loop”, OI. angam “limb”, angulih, angurih “finger, toe”, angusthah “big toe, thumb”, Avestic angushta- “toe, finger”, OI. ankah “hook; bent”, ancati “bends, curves”, Gk. ἄγκος ... ἄγκυρα “anchor”, L. ancus ... All these words derive fr. I.-E. base *ang-, resp. *anq-, “to bend”' — the direct source of Nourai's root name.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny, index vol. III s.v. 'ank- 60' (Latin index: angulus 61, ancrae 61)\", \"stance\": \"supports\",\n    \"note\": \"the Register volume points to WP I 60–61 for ank- 'biegen', i.e. the earlier form of Pokorny's article; Bd. I–II text itself is not on disk in searchable form.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.34 'FINGER' / 4.38 'TOE'\", \"stance\": \"supports\",\n    \"note\": \"'Skt. aṅguli-, Av. aṅgušta- (as “finger” only in cpds., otherwise “toe” = Skt. aṅguṣṭha- “thumb, big toe”): Skt. aṅga- “limb”, OHG ancha “nape of the neck, thigh”, NE ankle, etc., all prob. as “crooked” : Lat. angulus “corner”, etc. Walde-P. 1.61.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, cols. s.vv. ang-, anghulos, anguos, ankotos, ankuros\", \"stance\": \"partial\",\n    \"note\": \"Mann does NOT run these together: 'anghulos, anghlos “angle, corner”. WP I, 61. Cf. ank-, onk- ... Lat. angulus' and separately 'anguos “limb; gait” ... Skt. ángam' and 'ankotos, anktos “bend; bent” ... Skt. añcitab'. So a modern comparatist splits Nourai's one root into several.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index (ANGUSHTA – ANKULUS block)\", \"stance\": \"supports\",\n    \"note\": \"one Persian headword collects AVESTAN ANGUSHTA, OLD PERSIAN ANGST, PAHLAVI ANGUST, SANSKRIT ANGAM / ANGULI / ANGA / ANKA, ARMENIAN ANGIUN, ANKIUN, GREEK ANKOS, AGKOS, ANKULUS, OLD ENGLISH ONELEOW, ENGLISH ANKLE, DANISH/SWEDISH/NORWEGIAN ANKEL, DUTCH ENKEL, LITHUANIAN — an independent modern Persian handbook grouping the family exactly as Nourai does.\"}\n ],\n \"nodes\": []\n}\n\nN = entry[\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"angušta\", \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan aṅgušta- m. 'toe' (Bartholomae AiW 106; the sense 'finger' only in compounds, Buck 4.34) is the exact match of Sanskrit aṅguṣṭha-ḥ 'thumb, big toe' — Indo-Iranian *Hanguštʰa- built on the 'limb' base *h₂eng-u- (Skt. aṅgúli- 'finger', áṅga- 'limb') with the -stʰ(a)- formant; Indo-Iranian *-stʰ- gives Av. -št- after u. Pokorny prints the equation 'ai. aṅguṣṭha-ḥ ‚große Zehe, Daumen‘ == av. aṅgušta- m. ‚Zehe‘' (IEW 46), which is the arrow Nourai draws from the root. The word is the everyday Iranian word for 'toe/finger' and is the ancestor of every form in nodes #2 and #3.\",\n \"sources\": [W+\"%D8%A7%D9%86%DA%AF%D8%B4%D8%AA\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:75\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 51 (= printed pp.74–76; the page numeral '76' stands in the middle of the leaf, at 'anglice 76'), s.v. 'angle, n., corner': '... OI. angam “limb”, angulih, angurih “finger, toe”, angusthah “big toe, thumb”, Avestic angushta-, “toe, finger” ...'. Klein's gloss 'toe, finger' is verbatim Nourai's gloss, and Klein's page is p.75. Exactly what the arrow claims.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 46 (sub-article ang-)\", \"stance\": \"supports\",\n    \"note\": \"'aṅguṣṭha-ḥ ‚große Zehe, Daumen‘ == av. aṅgušta- m. ‚Zehe‘'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.34 FINGER / 4.38 TOE\", \"stance\": \"partial\",\n    \"note\": \"'Av. aṅgušta- (as “finger” only in cpds., otherwise “toe”)' — i.e. the primary Avestan sense is 'toe', 'finger' secondary; Nourai's order 'toe, finger' is right.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss no. 125 (engušt)\", \"stance\": \"supports\",\n    \"note\": \"'aw. angusta- ‚Zehe‘; phlv. angust; skr. aṅguṣṭha- ‚Daumen, grosse Zehe‘'.\"},\n   {\"src\": \"ARY\", \"where\": \"Latin index, ANGUSHTA (AVESTAN)\", \"stance\": \"supports\",\n    \"note\": \"Aryanpur lists AVESTAN ANGUSHTA beside PAHLAVI ANGUST and SANSKRIT ANGULI/ANGA under the Persian headword.\"}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"angošt «انگشت»\", \"verdict\": \"confirmed\",\n \"derivation\": \"Old Iranian *angušta- (= Av. aṅgušta-) > Middle Persian angust [ʾNGWST'] 'finger, toe; a unit of length (¾ in.)' (MacKenzie PHD 10) > New Persian angušt / angošt انگشت. Nyberg notes the dialect detail: 'angust ... SW form with -st < -št; NP angušt NW form. Paz. both angust and angušt' — i.e. the standard NP -št is the North-Western (Parthian-type) treatment, the Book-Pahlavi -st the South-Western one, so NP angošt continues the Old Iranian cluster directly rather than the SW Middle Persian output. The derivatives on the chart are transparent NP formations: انگشتر angoštar 'finger-ring' (MP angustarīg, PHD 10), انگ ۱ ang 'mark/stamp made with the finger', انگلک / انگولک angolak 'poking with a finger'. Strictly, the arrow should hang NP angošt on Middle Persian, not directly on Avestan (Avestan is a sister, not the mother, of Persian).\",\n \"sources\": [W+\"%D8%A7%D9%86%DA%AF%D8%B4%D8%AA\", \"https://abadis.ir/fatofa/%D8%A7%D9%86%DA%AF%D8%B4%D8%AA/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:392\", \"status\": \"not_checked\",\n    \"note\": \"Mo'in's 6-vol. Farhang-e Farsi (Amir Kabir), vol. 1 p.392, is not on disk: the local MON_part1.txt/MON_2vol_Adena_v1_djvu.txt is the 2-volume abridgement, unpaginated, and its انگشت article ('انگشت: هر یک از اجزای متحرک پنجگانهٔ دست و پای انسان') carries no bracketed etymology; the abadis.ir reproduction of Mo'in likewise gives only the definition. So the page number could not be confirmed, though Mo'in routinely brackets '[په. angust]' here.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.10 s.v. angust\", \"stance\": \"supports\",\n    \"note\": \"'angust [ʾNGWSTʹ | (N angušt)] finger, toe; unit of length (¾ in.). ~arīg [-lykʹ] finger ring. ~bān [-pʾānʹ] finger-guard, -stall.'\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (Glossary) s.v. angust\", \"stance\": \"supports\",\n    \"note\": \"'angust [ʾNGWSTʹ] finger 26¹¹, 29¹¹; a linear measure 93⁷⁴, — SW form with -st < -št; NP angušt NW form. Paz. both angust and angušt.'\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss no. 125\", \"stance\": \"supports\",\n    \"note\": \"'engušt ‚Finger, Zehe‘; vergl. engusteri ‚Ring‘, enguštāne ‚Fingerhut‘ ... aw. angusta- ‚Zehe‘; phlv. angust; skr. aṅguṣṭha-' — plus the dialect forms Kāš. ungūss, māz. angus, Oss. ängursf, Waḵī yangl, Šuġnī angast.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien §130\", \"stance\": \"supports\",\n    \"note\": \"'angust ‚Finger, Zehe‘ = zd. angušta-' (listed among np. -st/-št < idg. -st after i, u).\"},\n   {\"src\": \"MON\", \"where\": \"local 2-vol. text (unpaginated), s.v. انگشت\", \"stance\": \"silent\",\n    \"note\": \"definition only, no etymology in this edition.\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Sogdian\", \"words\": \"ʿngwšt\", \"verdict\": \"confirmed\",\n \"derivation\": \"Sogdian ʾng(w)št / ʾnkwšt(h) 'finger' — written ʾṅgwšt in the Manichaean script and ʾnkwšt(h) in the Sogdian ('Buddhist') script, both /angušt/ — continues the same Old Iranian *angušta- as Persian angošt; Gharib's dictionary explicitly derives it from the Avestan word. The plural ʾnkwštyt and the compound pʾdʹy ʾngwšt 'toe' (lit. 'foot-finger') are attested in the Buddhist Sogdian Padmacintāmaṇi and Vimalakīrti texts.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:41\", \"status\": \"supports\",\n    \"note\": \"Gharib, Sogdian Dictionary. SOD_pages.txt leaf 106 (printed p.41, cf. leaf 107 whose running head reads '42') carries entry '1044 ʾngwšt M — angust (ʾnkʾwst) ©<Av. angusta ⇒ ʾnkwšt(h) — finger — GMS 91, 253'; the companion entry '1067 ʾnkwšt(h) B, S — angust ... ⇒ pʾḍy ʾngwšt, ʾngwšt — finger — BSTBL, Padm. 42; Dhy. 21, 29; MDiii; TSP 14.23–25' begins p.41/42. Nourai's page number is exact and the '©<Av. angusta' note is precisely the arrow he draws.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"entries 1044 and 1067 (pp.41–42)\", \"stance\": \"supports\",\n    \"note\": \"see ref_check; Gharib himself writes '©<Av. angusta'.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 46\", \"stance\": \"partial\",\n    \"note\": \"Pokorny lists the Avestan and Indic forms but no Sogdian.\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Avestan\", \"words\": \"anku, aka; duž-aka\", \"verdict\": \"plausible\",\n \"derivation\": \"Two Avestan words, one secure and one not. (a) aka- m. 'hook, peg' (AiW 359, also in aḵnah- 'rein') and anku- in the hapax anku-pəsəmna- 'adorning oneself with hooks/clasps' are the direct Iranian reflexes of *h₂enk-u- (= Gk. ἀγκὼν, Skt. aṅká-ḥ 'hook'); Pokorny prints both on IEW 45. That part is confirmed. (b) duždka- m. is attested only at Vidēvdād 13.2, where it is the abusive name that 'men of evil speech' (dužvacaŋhō) give the hedgehog (vaŋhāpara-, Bd. gloss xārpušt). Bartholomae's analysis *duž- 'bad' + aka- 'hook' = 'the one that has nasty hooks (spines)' is offered with an explicit '?' after 'Et.?', i.e. as a guess — which is exactly what Nourai's own NOTE says. Two further caveats: the animal is the HEDGEHOG (Igel), not the porcupine; and the first element duž- is the well-known Iranian pejorative prefix (☆ Dus), so if the etymology is right the word is a compound of two roots, only the second of which belongs on this chart.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:45\", \"status\": \"supports\",\n    \"note\": \"POK_01.txt, between the page markers '45' and '4G'(=46): 'av. anku-pəsəmna- ‚mit Haken, Spangen sich schmückend‘ ... av. aka- m. ‚Haken, Zapfen‘, aḵnah- (Bartholomae Stud. 2, 101, Airan. Wb. 359) ‚Zügel‘'. Both of Nourai's Avestan 'hook' words, on the cited page.\"},\n   {\"ref\": \"BRT:755\", \"status\": \"partial\",\n    \"note\": \"BRT.txt, the spread headed '755 | duš.sravah- ... duzuxta- | 756': 'j. duzaka- m. (gemeiner oder Spott)Name des sūis vaŋhāparə (‚Igel‘): spānəm .. yim vaŋhāparəm yim mašyāka avi dužvacaŋhō duzakəm nama aojaitī V.13.2. ... KompA. — Et.? Vgl. HORN KZ.34.437, HBM.AGr. ... VII. *duž+aka- ‚der schlimme Haken (Stacheln) hat‘? — mp. (Pü.): žūžak; np. žūža; Assimilation der silbenanl. Kons.' So Bartholomae has exactly Nourai's derivation but flags it 'Et.?' and appends '?' — partial support, and Nourai's NOTE correctly records the doubt. Bartholomae's gloss is 'Igel' = hedgehog, not porcupine.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. 755 s.v. duzaka-, col. 359 s.v. aka-\", \"stance\": \"partial\", \"note\": \"see ref_check.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss no. 687\", \"stance\": \"supports\",\n    \"note\": \"'žūže ‚Igel‘ ... aw. duzaka- ‚Igel‘ (als Schimpfname des Hundes verwandt); phlv. žūžak' — Horn accepts the Avestan→Pahlavi→NP chain without questioning the internal analysis.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. xārpušt, xūkar(ag), zūzag\", \"stance\": \"partial\",\n    \"note\": \"'hedgehog xārpušt, xūkar(ag), zūzag' — the Pahlavi synonyms are all 'hedgehog'; MacKenzie's addenda even correct 'xūkar(ag) ... hedgehog' to 'porcupine' for that other word, showing the two animals are lexically distinct and zūzag is the hedgehog.\"},\n   {\"src\": \"SNS\", \"where\": \"Tavoosi, glossary p.168 (entry zūzag)\", \"stance\": \"supports\",\n    \"note\": \"the Shayast-ne-Shayast glossary entry for zūzag cites '(AiW. 755) duzaka' — i.e. the same Bartholomae column Nourai cites.\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"Pahlavi\", \"words\": \"žužag, zuzag, jujag\", \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian zūzag / žūžag [zwzkʹ] 'hedgehog', from Avestan duždka- by assimilation of the two syllable-initial consonants: *dužaka- > *žužag (d…ž > ž…ž), which Bartholomae states in so many words ('Assimilation der silbenanl. Kons.'). MacKenzie normalises the Book Pahlavi spelling zwzkʹ as zūzag; Bartholomae and Horn read the Pahlavi translation's form as žūžak. Nourai's third variant 'jujag' reflects the Gilaki/dialect form (Horn cites g. jūjīk) and the ambiguity of Pahlavi <z> for /ž/. The gloss should be 'hedgehog'; 'porcupine' is a loose rendering of NP خارپشت.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SNS:168\", \"status\": \"supports\",\n    \"note\": \"Tavoosi, Vāže-nāme-ye Šāyast ne Šāyast. The book's own index (SNS_pages.txt) reads 'zūzag 168/10', i.e. page 168 line 10 — Nourai's page is exact; and the body of p.168 (SNS_pages.txt around line 7098, between the entries zufr 168/2 and zufray 168/9) carries the reference '(AiW. 755) duzaka' beside the entry, i.e. Tavoosi derives Pahlavi zūzag from Av. duzaka- citing Bartholomae col. 755 — precisely Nourai's pair of citations.\"},\n   {\"ref\": \"BQT:1063\", \"status\": \"partial\",\n    \"note\": \"Borhan-e Qate' (Mo'in's ed.), BQT_v2_pages.txt leaf 525 (printed ≈ 1063–1068 on the stated leaf+543±3 mapping) is the ژوژ / ژوژه entry: 'ژوژ ... خارپشت را گویند، و آن جانوری است معروف' and 'ژوژه ... بمعنی ژوژ است که خارپشت باشد' (with Mo'in's cross-reference footnotes 'رک: خارپشت' and 'رک: ژوژه'). The page therefore documents the NEW PERSIAN word, not the Pahlavi form; it is the right citation for node #6 rather than for this node.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.100 s.v. zūzag\", \"stance\": \"supports\",\n    \"note\": \"'zūzag [zwzkʹ | (N žūža)] hedgehog.' — the Pahlavi form and its New Persian outcome, exactly the #5→#6 arrow.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss no. 687\", \"stance\": \"supports\",\n    \"note\": \"'aw. duzaka- ‚Igel‘ ...; phlv. žūžak; kurd. LW. ..., žūžī'.\"},\n   {\"src\": \"BRT\", \"where\": \"AiW 755\", \"stance\": \"supports\",\n    \"note\": \"'mp. (Pü.): žūžak; np. žūža; Assimilation der silbenanl. Kons.'\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary\", \"stance\": \"silent\",\n    \"note\": \"no entry for zūzag/žūžag (Nyberg's glossary covers only the texts of Part I).\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"žŭž «ژوژ»\", \"verdict\": \"confirmed\",\n \"derivation\": \"MP zūzag/žūžag > NP ژوژه žūža by the regular loss of Middle Persian final -g (-ag > -a), with the shortened by-form ژوژ žūž; both are entered in Borhan-e Qate' and both are glossed خارپشت 'hedgehog'. The word survives dialectally as Gilaki jūjīk and was borrowed into Kurdish (žūžī). Nourai's gloss 'porcupine' should read 'hedgehog'.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BRT:755\", \"status\": \"supports\",\n    \"note\": \"AiW 755 s.v. duzaka-, closing line: 'mp. (Pü.): žūžak; np. žūža'.\"},\n   {\"ref\": \"BQT:1063\", \"status\": \"supports\",\n    \"note\": \"BQT_v2_pages.txt leaf 525 (printed ≈ 1063–1068): 'ژوژ ... خارپشت را گویند، وآن جانوری است معروف' / 'ژوژه ... بمعنی ژوژ است که خارپشت باشد' — both the headword and the ژوژه variant of Nourai's box. (The vol.-2 OCR text has no printed page numerals, so the page is placed by the stated leaf+543±3 offset; the entry is at most a few pages from the cited 1063.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol. 2, بیان نهم of the letter ژ\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss no. 687 'žūže ‚Igel‘'\", \"stance\": \"supports\",\n    \"note\": \"Horn lemmatises the New Persian word as žūže and derives it from Av. duzaka- via phlv. žūžak.\"},\n   {\"src\": \"PHD\", \"where\": \"s.v. zūzag\", \"stance\": \"supports\", \"note\": \"'| (N žūža)'.\"},\n   {\"src\": \"MON\", \"where\": \"local 2-vol. text\", \"stance\": \"silent\", \"note\": \"no ژوژ entry in the abridgement on disk.\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"Sogdian\", \"words\": \"ʿkšye\", \"verdict\": \"confirmed\",\n \"derivation\": \"Sogdian ʾksyc / ʾxšyc 'hook' (Manichaean and Christian Sogdian, Henning, Sogdica 30.11a), read by Gharib as akaseč; Gharib derives it directly from Avestan aka- 'hook', i.e. from Nourai's node #4 rather than straight from the root as the chart draws it. Formally it is *aka- plus the diminutive/adjectival suffix -č (Sogd. -c), with the usual Sogdian -k- ~ -x- fluctuation before s. One caveat on the reading: the final letter is Sogdian <c>, not <e> — Nourai's 'ʿkšye' should be ʾkšyc/ʾksyc.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:32\", \"status\": \"supports\",\n    \"note\": \"Gharib, entry '837 ʾksyc M, C — akaseč ? (ʾksyʾc) ©Av. aka- ⇒ ʾxšyc — hook — Hen. Sogdica. 30.11a'. It stands on SOD_pages.txt leaf 97, whose running head numeral is printed '32' — Nourai's page number is exact, and the '©Av. aka-' note is his arrow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"entry 837, p.32; index 'hook 2, 139, 837'\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 45\", \"stance\": \"supports\",\n    \"note\": \"'av. aka- m. ‚Haken, Zapfen‘' — the Avestan base of the Sogdian word, though Pokorny has no Sogdian.\"},\n   {\"src\": \"BRT\", \"where\": \"AiW 359 s.v. aka-\", \"stance\": \"supports\",\n    \"note\": \"cited by Pokorny for Av. aka- 'Haken'; the Sogdian is not in Bartholomae.\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"Greek\", \"words\": \"ankura\", \"verdict\": \"confirmed\",\n \"derivation\": \"Ancient Greek ἄγκῦρα (ánkūra) f. 'anchor', from *h₂enk- 'bend' with the -ūra suffix, beside ἀγκὼν 'elbow, bend', ἀγκύλος 'crooked', ἄγκιστρον 'fish-hook' — the anchor named from its hooks/flukes. Attested from Homeric times onward; the place-name Ἄγκυρα (Ancyra, mod. Ankara) is the same word. Nourai's transliteration 'ankura' is a bare Latinisation of the Greek nominative.\",\n \"sources\": [W+\"%CE%AC%CE%B3%CE%BA%CF%85%CF%81%CE%B1\", \"https://www.etymonline.com/word/anchor\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. ank-: 'III. Greek ankura, anchor: ANCHOR. ... [Pok. 2. ank-, ang- 45.]' — the exact form, gloss and root Nourai gives.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 46\", \"stance\": \"supports\",\n    \"note\": \"'ἀγκύλη ‚Riemen‘ (= anord. ól, ál ds.), ἄγκυρα ‚Anker‘, ἀγκάλη ‚Ellenbogen, Bucht, alles Gekrümmte‘'.\"},\n   {\"src\": \"KLN\", \"where\": \"p.75 s.v. angle, corner\", \"stance\": \"supports\",\n    \"note\": \"lists 'ἄγκυρα “anchor”' among the *ang-/*anq- family; and p.72 s.v. anchor: 'fr. Gk. ἄγκυρα “anchor”, which is rel. to Gk. ἀγκὼν “a bend”, ἀγκύλος “crooked, curved”'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Anchor. (L.–Gk.)\", \"stance\": \"supports\", \"note\": \"'Anchor. (L.–Gk.) ... A.S. ancor' — Latin from Greek.\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"Persian\", \"words\": \"langar «لنگر»\", \"verdict\": \"confirmed\",\n \"derivation\": \"A Mediterranean culture-word, not an inherited Iranian form: Gk. ἄγκυρα > Lat. ancora, whence Aramaic/Mandaic angarā and thence Middle/New Persian لنگر langar. The l- is the usual Aramaic-mediated treatment of the initial vowel + nasal (cf. the same l-/n- alternation in the Arabic reflex), and the Persian word was in turn Arabicised as أنجر ʾanjar and re-exported to Ottoman Turkish lenger, Uzbek/Turkmen langar, Gujarati, Kazakh, and Mandarin 蘭干. Mo'in's own footnote to the Borhan entry states the borrowing outright. The chart's single arrow Greek → Persian is therefore right in substance but skips the Latin/Aramaic relay. A minority view on Wiktionary keeps an alternative 'of Iranian origin, cognate with Sanskrit लङ्गल (laṅgala)', but Taqizadeh, Mo'in and Asbaghi all take the Greek/Latin route.\",\n \"sources\": [W+\"%D9%84%D9%86%DA%AF%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1908\", \"status\": \"supports\",\n    \"note\": \"Fetched with tools/ref_page.py BQT:1908 (BQT vol.3 pdf p.705). The page is the لنگر entry — 'لنگر – بفتح اول و کاف فارسی ... آهنی باشد بسیار سنگین که کشتی را بدان از رفتار نگاهدارند' — and Mo'in's footnote 2 reads: 'اصل کلمه یونانی است «تقی‌زاده، یادگار ... ص ۹۲۷»، در یونانی ἄγκυρα، لاتینی ancora ... و معرب آن «انجر»، قس: فرانسوی ancre، انگلیسی anchor، آلمانی Anker.' That is Nourai's arrow verbatim, on the exact page cited. (OCR cached at data/verification/sources/refs/ocr/BQT/1908.txt.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, s.v. أنجر\", \"stance\": \"supports\",\n    \"note\": \"'أنجر – ‚Anker‘ pers. ... aus pers. لنگر langar, mand. angara ← lat. ancora.' — the Latin→Mandaic→Persian→Arabic relay.\"},\n   {\"src\": \"RCH\", \"where\": \"Richardson–Johnson s.v. langar\", \"stance\": \"supports\",\n    \"note\": \"'p langar, An anchor. A stay or rope for supporting a tent. ... langar andakhtan (or langar nihadan), To cast anchor' — confirms the word, form and sense in Persian.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch\", \"stance\": \"silent\",\n    \"note\": \"Lokotsch treats only Oriental words that entered European languages; langar is not among them (his Anker material is under Arabic cable/rope words).\"},\n   {\"src\": \"MON\", \"where\": \"local 2-vol. text\", \"stance\": \"silent\", \"note\": \"no etymological note in the abridgement.\"}\n ]\n})\n\nN.append({\n \"id\": 10, \"lang\": \"English\", \"words\": \"anchor\", \"verdict\": \"confirmed\",\n \"derivation\": \"Gk. ἄγκυρα > Lat. ancora (a very early Latin borrowing) > Old English ancor/ancra (borrowed with the ships and the Church) > Middle English anker > anchor; the unetymological -ch- is a late-16c. pedantic spelling based on a corrupt Latin spelling anchora, and the pronunciation stayed /k/. Sense 'presenter of a broadcast' from anchorman, 1903/1965.\",\n \"sources\": [\"https://www.etymonline.com/word/anchor\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. ank-: 'III. Greek ankura, anchor: ANCHOR.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p.72 s.v. anchor, n.\", \"stance\": \"supports\",\n    \"note\": \"'anchor, n. — ME. anker, fr. OE. ancor, fr. L. ancora, fr. Gk. ἄγκυρα “anchor”, which is rel. to Gk. ἀγκὼν “a bend” ... See angle, “corner”.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Anchor\", \"stance\": \"supports\", \"note\": \"'Anchor. (L.–Gk.) Better spelt without the h. M.E. anker. A.S. ancor.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins ank- III\", \"stance\": \"supports\", \"note\": \"as ref_check.\"}\n ]\n})\n\nN.append({\n \"id\": 11, \"lang\": \"Sanskrit\", \"words\": \"angam; catur-anga\", \"verdict\": \"confirmed\",\n \"derivation\": \"Sanskrit áṅga- n. 'limb, member, part of the body' (< *h₂eng-, the 'limb' branch of Pokorny's ank-/ang-), and the bahuvrīhi catur-aṅga- 'having four limbs/members' (catúr 'four', ☆ Kwetwer). In its original military sense caturaṅga- names the four arms of the Indian army — elephants, chariots, cavalry and infantry (Rigveda 10.92.11 already has catúraṅga-) — and it is from that army metaphor that the 6th-c. board game takes its name, its four pieces being precisely elephant (→ bishop), chariot/rook (→ castle), horse (→ knight) and foot-soldier (→ pawn). Nourai's gloss 'the four parts (castle, Knight, Bishop and Pawn)' therefore names the chess pieces rather than the literal 'four limbs' — the same shortcut Mo'in takes in his Borhan footnote ('شامل چهار جزء: فیل، رخ، اسب، پیاده').\",\n \"sources\": [W+\"%E0%A4%9A%E0%A4%A4%E0%A5%81%E0%A4%B0%E0%A4%99%E0%A5%8D%E0%A4%97\"],\n \"ref_check\": [\n   {\"ref\": \"POK:46\", \"status\": \"supports\",\n    \"note\": \"IEW 46, sub-article 'ang-, bes. zur Bezeichnung von Gliedmaßen': 'Ai. áṅgam ‚Glied‘, aṅgūli-ḥ, aṅgūri-ḥ f. ‚Finger, Zehe‘ (davon aṅgulīyam ‚Fingerring‘); aṅguṣṭha-ḥ ‚große Zehe, Daumen‘ == av. aṅgušta- m.' — the 'member, part' gloss is Pokorny's.\"},\n   {\"ref\": \"BQT:1254\", \"status\": \"supports\",\n    \"note\": \"BQT vol.3, pdf p.45 = printed 1254 (the page numeral '۱۲۵۴' is visible at the foot). Mo'in's footnote 1 to the شترنگ entry: 'پهلوی čatrang، ارمنی ... از سانسکریت catur-aṅga (دارای چهار لبه با چهار حد) شامل چهار جزء: فیل، رخ، اسب، پیاده — Monier-Williams 1:386؛ معرب آن شطرنج'. Exactly Nourai's Sanskrit form, gloss and 'four parts'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SYN\", \"where\": \"Buck 4.34\", \"stance\": \"supports\", \"note\": \"'Skt. aṅga- “limb” ... prob. as “crooked” : Lat. angulus “corner”, Walde-P. 1.61.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. anguos\", \"stance\": \"partial\",\n    \"note\": \"'anguos, om, ā (?) “limb; gait” ... Skt. (ambig.) ángam' — Mann accepts the form but marks its root affiliation ambiguous.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins ank- V\", \"stance\": \"supports\", \"note\": \"'V. Sanskrit anka, hook, ancati, he bends: PALANQUIN.'\"},\n   {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. Chess is absent; s.v. Palankeen p.669\", \"stance\": \"silent\",\n    \"note\": \"Yule has no caturaṅga article.\"}\n ]\n})\n\nN.append({\n \"id\": 12, \"lang\": \"Pahlavi\", \"words\": \"catrang\", \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian čatrang [cʾtʾlʾng], borrowed from Sanskrit caturaṅga- with loss of the unstressed medial -u- (*čaturaṅg > čatrang) and the regular Iranian rendering of Indic -aṅga as -ang; Indic c- = MP č-. It is the title-word of the Pahlavi tract Wīzārišn ī čatrang ud nihišn ī nēw-ardaхšīr ('The Explanation of Chess and the Invention of Backgammon'), which stages the game's arrival from India at Khosrow I's court — the story Borhan-e Qate' repeats. MacKenzie lemmatises it and already flags the Arabic outcome.\",\n \"sources\": [W+\"%D8%B4%D8%B7%D8%B1%D9%86%D8%AC\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"Nourai gives no reference on this node; the claim is however carried by the reference on its child (#13), BQT:1254, whose footnote reads 'پهلوی čatrang ... از سانسکریت catur-aṅga'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.22 s.v. čatrang\", \"stance\": \"supports\",\n    \"note\": \"'čatrang [cʾtʾlʾng | (Ar. šatranj)] chess.'\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi s.v. شطرنج\", \"stance\": \"supports\",\n    \"note\": \"'شطرنج šaṭranj: ‚Schachspiel‘ ... pers. šatrang, mp. čatrang, skr. caturanga.'\"},\n   {\"src\": \"BQT\", \"where\": \"vol.3 p.1254, Mo'in's footnote 1\", \"stance\": \"supports\", \"note\": \"see node #11 ref_check.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II\", \"stance\": \"silent\", \"note\": \"the word is not in Nyberg's text-glossary.\"}\n ]\n})\n\nN.append({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"šatrang «شترنگ»\", \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The word itself and the chain are certain: MP čatrang > Classical NP چترنگ čatrang / شترنگ šatrang 'chess', Arabicised as شطرنج šaṭranj (Arabic has no /č/, so چ is rendered ش, and the t is written ط by attraction to the emphatic environment), and then re-borrowed into New Persian in that Arabic dress — a Persian→Arabic→Persian round trip. Asadi's Loġat-e Fors p.289 already has Nourai's shahid verse ('تا جز از بیست و چهارش نبود خانهٔ نرد / همچو در سی و دو خانه است نهادش شترنگ'), which Borhan quotes on the very page Nourai cites. What is suspect is the first of the two variants printed in the box, «کترنگ»: *katrang is not a Persian word, and ک vs چ differ only by the three dots — the book must be printing (or the scan misreading) چترنگ čatrang, the direct continuation of the Pahlavi form in node #12 and the form given by Mo'in, MacKenzie and Asbaghi. The second variant شطرنج is correct.\",\n \"sources\": [W+\"%D8%B4%D8%B7%D8%B1%D9%86%D8%AC\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1254\", \"status\": \"supports\",\n    \"note\": \"BQT vol.3 pdf p.45 = printed 1254: headword 'شترنگ «با کاف فارسی» ... بمعنی شطرنج است، و آن بازی‌ای باشد معروف که ... داهر هندی یا پسر او در زمان انوشیروان اختراع کرده بود و بزرجمهر در برابر آن نرد را ساخت و شطرنج معرب آن باشد'; footnote 1 gives پهلوی čatrang < سانسکریت catur-aṅga; and the page carries Nourai's verse with the source 'لغت فرس ۲۸۹'. Note in passing that Borhan credits the verse to Asadi's Loġat-e Fors, where Nourai's chart credits 'Najjār'.\"},\n   {\"ref\": \"FVF:404\", \"status\": \"not_checked\",\n    \"note\": \"Emam Shushtari, Farhang-e Vāžehā-ye Fārsi dar Zabān-e ʿArabi — no copy on disk and the noorlib viewer is behind a login; the page could not be opened.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PLA\", \"where\": \"Asbaghi s.v. شطرنج\", \"stance\": \"supports\",\n    \"note\": \"'šaṭranj: ‚Schachspiel‘ ... pers. šatrang, mp. čatrang, skr. caturanga' — note that Asbaghi's Persian form is exactly Nourai's šatrang.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, s.v. شطرنج\", \"stance\": \"supports\",\n    \"note\": \"quoting Borhan-e Qate': '... والشطرنج معرب شترنك' — šaṭranj is the Arabicised šatrang.\"},\n   {\"src\": \"PHD\", \"where\": \"s.v. čatrang\", \"stance\": \"supports\", \"note\": \"'čatrang ... | (Ar. šatranj)] chess'.\"},\n   {\"src\": \"FRS\", \"where\": \"Asadi, Loġat-e Fors (local OCR)\", \"stance\": \"silent\",\n    \"note\": \"the headword could not be located in the OCR text, but Borhan cites it as لغت فرس ۲۸۹ for this very verse.\"}\n ]\n})\n\nN.append({\n \"id\": 14, \"lang\": \"Sanskrit\", \"words\": \"ancati; pari-ancati; pary-anka, palyanka\", \"verdict\": \"confirmed\",\n \"derivation\": \"Skt. áñcati / (zero-grade) ácati 'bends, curves' is the primary verb of *h₂enk- (Pokorny prints 'Ai. ancati (mpers. ancītan) und (tiefstufig) acati ‚biegt, krümmt‘' on IEW 45), with aṅká-ḥ 'bend, hook, the hollow between chest and hip, lap' beside it. Compounded with pári 'around' (☆ Per 1) it gives pary-aṅka- ~ paly-aṅka- m. 'couch, bed, litter' — literally 'that which bends/curves around (the body)'; the ry ~ ly variation is the familiar Indic r/l fluctuation, and it is the l-form that all the borrowed words descend from (Pali pallaṅko, Prakrit pallaṅka). Nourai's gloss 'a bed carried on poles on the shoulder of two or four men … due to the sagging cloth bottom' is his own rationalisation of the palanquin sense; the standard analysis is 'bending around'.\",\n \"sources\": [\"https://www.etymonline.com/word/palanquin\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:943\", \"status\": \"not_checked\",\n    \"note\": \"AHD:943 is a page of the main 1975 New College dictionary (the 'palanquin' entry), and only Watkins's Indo-European appendix is on disk. The appendix does support the substance: s.v. ank- 'V. Sanskrit anka, hook, ancati, he bends: PALANQUIN', and s.v. per¹ '6. Sanskrit pari, through, around: PALANQUIN' — which is also Nourai's cross-reference 'PER 1'.\"},\n   {\"ref\": \"OEW:14\", \"status\": \"not_checked\",\n    \"note\": \"Shipley, The Origins of English Words (1984) is lending-only on archive.org and not on disk; p.14 would fall in the a-roots, consistent with an 'ank-' article, but could not be opened.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 45\", \"stance\": \"supports\",\n    \"note\": \"'Ai. ancati (mpers. ancītan) und (tiefstufig) acati ‚biegt, krümmt‘, Partiz. -akna-, -akta- ‚gebogen‘; aṅká-ḥ m. ‚Biegung, Haken, Biegung zwischen Brust und Hüfte‘'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins ank- V and per¹ 6\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.669 s.v. PALANKEEN, PALANQUIN\", \"stance\": \"supports\",\n    \"note\": \"'The basis of all the forms is Skt. paryanka, or palyanka, “a bed”, from which we have Hind. and Mahr. palang “a bed”, Hind. pālkī “a palankin”, ... Pali pallanko “a couch, bed, litter, or palankin”, and in Javanese and Malay palangki “a litter or sedan”.'\"},\n   {\"src\": \"AID\", \"where\": \"Whitworth, Anglo-Indian Dictionary\", \"stance\": \"silent\",\n    \"note\": \"no headword palanquin/paryanka; the word appears only in caste descriptions ('palanquin-bearers').\"}\n ]\n})\n\nN.append({\n \"id\": 15, \"lang\": \"English\", \"words\": \"palanquin, palankee\", \"verdict\": \"plausible\",\n \"derivation\": \"The two ends of the chain are right but the chart's single Sanskrit→English arrow leaves out the actual carriers. Skt. paly-aṅka- > Pali pallaṅko / Prakrit pallaṅka > Javanese and Malay palangki 'litter, sedan' (the Indian Ocean trade term) > Portuguese palanquim (early 16c.; the nasal -m is a standard Portuguese addition, as in mandarim, Bagaim) > English palanquin, first attested in the 1580s. The Anglo-Indian by-form palankeen/palankee comes instead from the Hindi pālkī (< Prakrit pallaṅkī), the light litter itself. Verdict 'plausible' rather than 'confirmed' only because Nourai's arrow suppresses the Prakrit–Malay–Portuguese relay that every source insists on.\",\n \"sources\": [\"https://www.etymonline.com/word/palanquin\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. ank-: 'V. Sanskrit anka, hook, ancati, he bends: PALANQUIN'; and the index line 'PALANQUIN ank-, per¹'.\"},\n   {\"ref\": \"OEW:14\", \"status\": \"not_checked\", \"note\": \"Shipley not on disk (lending-only).\"}\n ],\n \"consulted\": [\n   {\"src\": \"HJB\", \"where\": \"Hobson-Jobson pp.669–670 s.v. PALANKEEN, PALANQUIN\", \"stance\": \"partial\",\n    \"note\": \"'The origin of the word is not doubtful, though it is by no means clear how the Portuguese got the exact form which they have handed over to us. The nasal termination may be dismissed as a usual Portuguese addition, such as occurs in mandarin, Bagaim ... The basis of all the forms is Skt. paryanka, or palyanka' — confirms the ultimate source but insists on the Malay/Portuguese route Nourai omits.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. palanquin\", \"stance\": \"supports\",\n    \"note\": \"Klein likewise routes it Portuguese palanquim < Javanese/Malay palangki < Skt. palyanka-.\"},\n   {\"src\": \"AID\", \"where\": \"Whitworth\", \"stance\": \"silent\", \"note\": \"no etymological entry.\"}\n ]\n})\n\nN.append({\n \"id\": 16, \"lang\": \"Latin\", \"words\": \"angulus\", \"verdict\": \"confirmed\",\n \"derivation\": \"Latin angulus m. 'corner, angle' (Ernout–Meillet: 'coin [d'un édifice], angle (γωνία). Ancien, technique, usuel'), from *ang-olo-, a diminutive-looking -lo- derivative of the same 'bend' base; exact cognates OCS ǫg˕l˕ 'corner' and Armenian angiwn/ankiwn 'corner', with the o-grade beside it in Lat. uncus 'hook'. Derivatives angulāris, angulātus, and the numeral compounds tri-, quadri-, rect-angulus that give English triangle and rectangle. (Mann, alone, sets it up as *anghulos with a voiced aspirate, so the exact root shape is not universally agreed.)\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. ank-: 'VII. Suffixed form *ang-olo- in Latin angulus, angle, corner: ANGLE.'\"},\n   {\"ref\": \"KLN\", \"status\": \"supports\",\n    \"note\": \"KLN p.75 s.v. angle, n., corner: 'F., fr. L. angulus, “angle, corner”, which is cogn. with Arm. angiun, ankiun, OSlav. ǫg(u)lu “corner” ... All these words derive fr. I.-E. base *ang-, resp. *anq-, “to bend”.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 46–47\", \"stance\": \"supports\",\n    \"note\": \"'auch lat. angulus (womit aksl. ǫg˕l˕ ‚Winkel‘ urverwandt ist) ‚Winkel‘ (daneben mit o-Stufe lat. ungulus, ungustus)'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout–Meillet s.v. angulus\", \"stance\": \"supports\",\n    \"note\": \"'angulus, -ī (anglus dans l'app. Probi) m.: coin [d'un édifice], angle (γωνία). — Ancien, technique, usuel. M.L.465. ... Dérivés: angellus; angularis; angulatus; angulosus ... Second terme de composés: acuti-, obtusi-, rect-, tri-, quadri-, sex-, oct-, uiginti-angulus.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. anghulos\", \"stance\": \"partial\",\n    \"note\": \"'anghulos, anghlos, is “angle, corner”. WP I, 61. Cf. ank-, onk-, ōnk- ... Lat. angulus; Umb. anglo-; OHG angul “fish-hook”; OE angel; ON ǫngull; OCS ǫglŭ “corner”' — same family, but reconstructed with -gh-.\"},\n   {\"src\": \"LEW\", \"where\": \"Walde 1910\", \"stance\": \"silent\", \"note\": \"the entry could not be located in the OCR of the 1910 edition on disk.\"}\n ]\n})\n\nN.append({\n \"id\": 17, \"lang\": \"English\", \"words\": \"angle, rectangle, triangle\", \"verdict\": \"confirmed\",\n \"derivation\": \"All three are learned Latin-via-French borrowings, not native words: L. angulus > Old French/French angle > Middle English angle (14c.) 'corner, angle'; L. tri-angulum > OF triangle > ME triangle; Late L. rect-angulum ('right-angled figure') > F rectangle > E rectangle (16c.). Klein and Skeat both label the English word '(F.–L.)'. Note that the homonym angle 'fish-hook, to fish' is NOT from Latin but the inherited Old English angel (same root, native line) — Nourai rightly keeps it off this branch, though it is the very word that node #18 depends on.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; the parent node's AHD and KLN cover it.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p.75 s.v. angle, n., corner\", \"stance\": \"supports\",\n    \"note\": \"'angle, n., corner. — F., fr. L. angulus ... Cp. angle, “fishhook”, Angle, anchor, ancon, angula, angular, ankle, ankylosis, and the second element in triangle.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Angle (1)\", \"stance\": \"supports\",\n    \"note\": \"'Angle (1), a corner. (F.–L.) M.E. ...' beside 'Angle (2), a hook, fish-hook. (E.) A.S. angel, a fish hook. + Dan. angel; G. ... (√AK, ANK.)'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins ank- VII\", \"stance\": \"supports\", \"note\": \"'Latin angulus, angle, corner: ANGLE.'\"}\n ]\n})\n\nN.append({\n \"id\": 18, \"lang\": \"Germanic\", \"words\": \"Angul\", \"verdict\": \"plausible\",\n \"derivation\": \"Angul (Old English Angel, Ongel; modern German Angeln, Danish Angel) is the small district on the east coast of the Jutland/Schleswig peninsula between the Schlei and Flensburg fjords, from which the Angles are said to have come. The traditional etymology, going back to Rudolf Much, identifies the name with Gmc *angul- 'fish-hook, angle' (OE angel, ON ǫngull, OHG angul) < *h₂enk-ulo-, i.e. 'the hook-shaped land' — which is exactly Nourai's gloss. It is a good but not a proven etymology: Pokorny reports it as Much's suggestion and objects that it requires 'eine sonst nicht belegte Bed. ‚Winkel; Bucht‘', and Watkins hedges with 'probably'. The language label 'Germanic' is also loose — the name is attested in Latin (Anglii, Tacitus Germania 40) and Old English/Old Norse, not in a reconstructed Proto-Germanic source.\",\n \"sources\": [\"https://www.etymonline.com/word/England\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins s.v. ank-, II.1: 'Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE; b. probably Latin Angli, the Angles: ANGLE.' — supports the derivation but marks it 'probably'.\"},\n   {\"ref\": \"OEW:14\", \"status\": \"not_checked\", \"note\": \"Shipley not on disk (lending-only on archive.org).\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 46\", \"stance\": \"partial\",\n    \"note\": \"'Much stellt hierher den lat.-germ. VN Anglii, ags. Angel, Ongel als ‚Anwohner der Holsteiner Bucht‘ zum aisl. ON ǫngull, mit einer sonst nicht belegten Bed. ‚Winkel; Bucht‘ (Hoops Reallex. I 61)' — Pokorny attributes it to Much and flags the semantic difficulty.\"},\n   {\"src\": \"KLN\", \"where\": \"p.75 s.v. Angle, n.\", \"stance\": \"supports\",\n    \"note\": \"'L. Anglus, pl. Angli, of Teut. origin. Cp. OE. Angle, Engle, prop. “the people coming from Angul (= ON. ǫngull), a hookshaped district in Schleswig”, fr. angul (= ON. ǫngull), “fishhook, angle”, which is rel. to anga, OHG. ango, “hook”.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Angle (2)\", \"stance\": \"supports\",\n    \"note\": \"'Angle (2), a hook, fish-hook. (E.) A.S. angel, a fish hook' — the appellative behind the place-name.\"}\n ]\n})\n\nN.append({\n \"id\": 19, \"lang\": \"Old English\", \"words\": \"Engle, Angle\", \"verdict\": \"confirmed\",\n \"derivation\": \"Old English Engle / Angle (nom. pl.) 'the Angles', Latin Anglī, the Germanic people who, with the Saxons and Jutes, crossed to Britain in the mid-5th century (Bede's traditional date for the adventus Saxonum is 449; Nourai's 'around 450 AD' is the standard rounding). The i-umlaut of a > e before the following i/j of the tribal stem gives Engle beside Angle. From it: Engla land (gen. pl. 'land of the Angles') > England, and Englisc > English; the word first denoted the people, only in late Old English the country — Canute was the first king to style himself 'King of England'. Nourai's parenthesis 'Engle-Land' should be Engla land.\",\n \"sources\": [\"https://www.etymonline.com/word/England\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:522\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 284 (which carries the page numerals 522 and 523), s.v. English: 'English, adj. and n. — OE. Englisc, Ænglisc, “English”, fr. Engle, Angle, name of a Teutonic tribe that settled in Britain, prop. “the people coming from Angul”. See Angle and adj. suff. -ish.' Klein p.75 adds the 5th-century date: 'member of a Teutonic tribe that came in the 5th century from what is now known as Schleswig-Holstein to Britain and conquered it.'\"},\n   {\"ref\": \"AWH1:129\", \"status\": \"not_checked\",\n    \"note\": \"AWH = H. Kinder & W. Hilgemann, Atlas of World History (Anchor Books 1974), vol. 1 p.129 — a historical atlas, not in the local library and not digitised openly; presumably the map/chronology of the Anglo-Saxon migration. Cannot be checked.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"pp.75 and 522\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins ank- II.1.b\", \"stance\": \"supports\", \"note\": \"'probably Latin Angli, the Angles'.\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls\", \"stance\": \"silent\", \"note\": \"no separate etymological article located in the OCR.\"}\n ]\n})\n\nN.append({\n \"id\": 20, \"lang\": \"French\", \"words\": \"angle-\", \"verdict\": \"disputed\",\n \"derivation\": \"There is no French form 'angle-' meaning 'English' and no French link in this chain. French for 'English' is anglais, from Middle/Old French anglois, from Latin Anglus / Late Latin Anglenses — i.e. from the LATIN form of the tribal name (Tacitus's Anglii, Bede's Angli), not from Old English Engle as the chart's arrow claims; Latin took the name from Germanic independently of Old English. The French word angle is a different lexeme altogether: 'corner', from Latin angulus, which is Nourai's own node #16. The node therefore conflates two homographs and inserts an intermediary that no source supports; and its child, Persian انگلیس, is not derived from French anyway (see #21).\",\n \"sources\": [W+\"anglais\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given by Nourai on this node.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"pp.75–76 s.vv. Angle, Anglican, anglice, Anglo-\", \"stance\": \"contradicts\",\n    \"note\": \"Klein routes all the 'English' words through Latin, not French: 'Anglican — ML. Anglicanus, fr. Anglicus, “English”, fr. Late L. Anglus'; 'Anglo-, combining form meaning “English”. — Fr. Late L. Angli, “the English”'. French appears nowhere in the chain, and Klein's French-derived 'angle' is the corner word.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout–Meillet s.v. angulus\", \"stance\": \"contradicts\",\n    \"note\": \"'angulus ... coin [d'un édifice], angle' — the source of French angle is the Latin word for 'corner', unrelated to the tribal name.\"}\n ]\n})\n\nN.append({\n \"id\": 21, \"lang\": \"Persian\", \"words\": \"Engelîs «انگلیس»\", \"verdict\": \"disputed\",\n \"derivation\": \"Persian انگلیس is a modern European loan, but the accepted source is Italian inglese, most probably relayed through Ottoman Turkish انگلیز ingiliz — the Levantine-trade route by which most early-modern European ethnonyms reached Persian — not the French route Nourai draws (and certainly not from any French 'angle-'). The final -s of انگلیس matches Italian -se, not French -ais /ɛ/; انگلیسی englisi is the ordinary Persian nisba of it, and انگلستان englestān is an internal Persian -stān formation ('land of the English'), not a borrowing at all. The ultimate origin in Latin Anglus < the Germanic tribal name is of course correct; it is the immediate donor language that is wrong.\",\n \"sources\": [W+\"%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3\", \"https://abadis.ir/fatofa/%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3/\"],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"not_found\",\n    \"note\": \"Nourai cites Mo'in without a page. Mo'in's انگلیس article, both in the 2-vol. text on disk and in the abadis.ir reproduction of the Farhang-e Farsi, gives only the definition ('مردم انگلستان', 'شعبه‌ای از نژاد ژرمن ساکن بریتانیای کبیر' in Dehkhoda) with no statement of origin, French or otherwise. Nothing in Mo'in supports a French etymon.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. انگلیس (via abadis.ir)\", \"stance\": \"silent\",\n    \"note\": \"definition only; no etymology.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch\", \"stance\": \"silent\",\n    \"note\": \"Lokotsch covers Oriental words in European languages, not the reverse; nothing on ingiliz.\"}\n ]\n})\n\nN.append({\n \"id\": 22, \"lang\": \"English\", \"words\": \"English, England, Anglo-, Anglo-Saxon\", \"verdict\": \"confirmed\",\n \"derivation\": \"OE Englisc (adj. to Engle) > English; OE Engla land 'land of the Angles' > Engleland > England (the modern In- pronunciation is a later shift, probably by analogy with the many -ing- words); Anglo- is a combining form taken from Late Latin Anglī 'the English'; Anglo-Saxon comes from Medieval Latin Anglo-Saxones, earlier Anglī Saxones 'the English Saxons' — as Klein notes, tautological in later use since by Late Latin both elements had come to mean 'the English'.\",\n \"sources\": [\"https://www.etymonline.com/word/England\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given by Nourai; the parent node's KLN:522 covers 'English'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"pp.75–76 and 522\", \"stance\": \"supports\",\n    \"note\": \"'Anglo-, combining form meaning “English”. — Fr. Late L. Angli, “the English”. See Angle, Anglo-Saxon.'; 'Anglo-Saxon, n. — ML. Anglo-Saxones, fr. earlier Angli Saxones, “the English” ... Accordingly the term Anglo-Saxon is tautological, inasmuch as both elements of this compound denote “the English”.'; 'English, adj. and n. — OE. Englisc, Ænglisc, fr. Engle, Angle.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins ank- II.1.b\", \"stance\": \"supports\", \"note\": \"'probably Latin Angli, the Angles: ANGLE.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Angle (2)\", \"stance\": \"partial\",\n    \"note\": \"Skeat connects the tribal name to the fish-hook word but gives no separate England article in the concise edition.\"}\n ]\n})\n\ndoc = {\n \"pdf_page\": 56,\n \"book_page\": 26,\n \"verified_by\": \"claude-fable-5-1\",\n \"verified_on\": \"2026-09-04\",\n \"entries\": [entry]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-56.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build56.py",
 "description": "Write verification JSON for page 56"
}
```


### [2026-09-04T23:03:06.339Z] TOOL RESULT

```
ok 22
```


## [2026-09-04T23:03:11.675Z] TOOL CALL #90: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-56.json > /dev/null && echo \"JSON OK\" && FLAGGED=1 python3 tools/verify_check.py 56",
 "description": "Validate and run verify_check for page 56"
}
```


### [2026-09-04T23:03:13.877Z] TOOL RESULT

```
JSON OK
nodes verified: 22/22
node verdicts: {'confirmed': 16, 'plausible': 3, 'transcription_suspect': 1, 'disputed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 17, 'not_checked': 11, 'partial': 3, 'not_found': 1}
books consulted: {'supports': 50, 'partial': 9, 'silent': 14, 'contradicts': 2} | by book: {'KLN': 8, 'POK': 7, 'PHD': 6, 'AHD': 6, 'HRN': 5, 'SKT': 5, 'MON': 4, 'NYB': 3, 'BRT': 3, 'PLA': 3, 'HJB': 3, 'SYN': 2, 'SOD': 2, 'BQT': 2, 'LKT': 2, 'IEC': 2, 'AID': 2, 'LAT': 2, 'ARY': 1, 'HUB': 1, 'SNS': 1, 'RCH': 1, 'AFM': 1, 'FRS': 1, 'LEW': 1, 'FSD': 1}
FLAG: 56 Ang, Ank, Anq #13 šatrang «شترنگ» transcription_suspect | The word itself and the chain are certain: MP čatrang > Classical NP چترنگ čatrang / شترنگ šatrang 'chess', Arabicised as شطرنج šaṭranj (Arabic has no /č/, so چ is rendered ش, and the t is written ط b
FLAG: 56 Ang, Ank, Anq #20 angle- disputed | There is no French form 'angle-' meaning 'English' and no French link in this chain. French for 'English' is anglais, from Middle/Old French anglois, from Latin Anglus / Late Latin Anglenses — i.e. fr
FLAG: 56 Ang, Ank, Anq #21 Engelîs «انگلیس» disputed | Persian انگلیس is a modern European loan, but the accepted source is Italian inglese, most probably relayed through Ottoman Turkish انگلیز ingiliz — the Levantine-trade route by which most early-moder
```


## [2026-09-04T23:03:33.046Z] AGENT

Written `/home/sfmqrb/git/rishe/data/verification/page-56.json`; `python3 tools/verify_check.py 56` reports 22/22 nodes, no PROBLEM lines.

**PDF page 56 (book p.26) — one entry, root "Ang, Ank, Anq" [IE] "to bend"**

- Root: **confirmed** (= Pokorny IEW 45–47 *2. ank-, ang- "biegen"*; Nourai's three-way root name is lifted verbatim from Klein p.75 "*ang-, resp. *anq-"). Noted that modern practice splits it (*h₂enk- "bend" vs *h₂eng- "limb"), and that two branches are loans, not descent.
- Node verdicts: **16 confirmed, 3 plausible, 2 disputed, 1 transcription_suspect**.
- Ref checks: 17 supports, 3 partial, 1 not_found, 11 not_checked (AWH1, OEW, FVF, and the un-referenced nodes).

Flagged items:
- **#20 French "angle-" — disputed.** No such French form; French for "English" is *anglais* < OF *anglois* < Latin *Anglus*, not from Old English *Engle*; French *angle* "corner" is a different word (Nourai's own node #16).
- **#21 Persian انگلیس Engelîs — disputed.** Wiktionary/standard view: from Italian *inglese*, probably via Ottoman Turkish *ingiliz*, not French; Mo'in (the cited ref) gives no etymology at all (`not_found`).
- **#13 «کترنگ» — transcription_suspect.** *katrang* is not a word; the printed variant must be **چترنگ** *čatrang* (ک/چ differ by three dots) — the direct continuation of the Pahlavi form in #12.

Notable positive findings: BQT:1908 (fetched via `ref_page.py`) is exactly Mo'in's لنگر footnote deriving it from Greek ἄγκυρα/Latin *ancora*; BQT:1254 is exactly the شترنگ page with the *čatrang < caturaṅga* note; SNS's own index reads "zūzag 168/10" and the entry cites "(AiW. 755) duzaka" — Nourai's SNS:168 + BRT:755 pair is precise; SOD:41 and SOD:32 are page-exact in Gharib. Bartholomae AiW 755 does print "Et.? … *duž+aka- 'der schlimme Haken (Stacheln) hat'?", vindicating Nourai's own NOTE. Two gloss corrections recorded: the *duž-aka*/žūžag animal is the **hedgehog** (Igel/خارپشت), not the porcupine, and *caturaṅga* originally names the army's four arms, not the chess pieces.
