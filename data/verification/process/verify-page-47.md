# Verification process log — verify-page-47


## [2026-09-04T19:28:21.855Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 47 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-47.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-47.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-47.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 47` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T19:28:23.541Z] AGENT

I'll start by reading the instructions and the relevant files.


## [2026-09-04T19:28:25.660Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:28:25.675Z] TOOL RESULT

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


## [2026-09-04T19:28:25.929Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-47.txt"
}
```


### [2026-09-04T19:28:25.943Z] TOOL RESULT

```
1	=== PDF page 47 (book page 17) ===
2	--- entry 0 ---
3	ROOT [Arabic] Al 3 : definite article "the" used as a prefix  (refs SAP:43)
4	#1 (parent #0) [Persian] refs=MON |  | extra: الله ، الکل ، المثنّی
5	#2 (parent #0) [Arabic] refs=KLN; AHD; OEW | Amir al-bahr : sea commander, admiral ☞A`.m.r ; al-fesfeseh : horse food ☞Ed,Ekwos
6	  #3 (parent #2) [English] refs=AHD; OEW | admiral ; alfalfa
7	    #4 (parent #3) [Persian] refs=MON | âdmîral «آدمیرال» : admiral ; âlfâlfâ «آلفا آلفا» : alfalfa
8	#5 (parent #0) [Arabic] refs=KLN; AHD; OEW | al-kahl : highly purified spirits, alcohol ☞K.h.l ; al-Xwârazmî : the 9th century mathematician who devised "algebra". ☞Ghdhem ; al-ithmud : antimony
9	  #6 (parent #5) [Latin] refs=None | 
10	    #7 (parent #6) [French] refs=None | 
11	      #8 (parent #7) [Persian] refs=MON; VOP | alkol «الکل» : alcohol ; âlgoritm «آلگوریتم» : algorithm ; ântîmoân «آنتیموان» : antimony
12	    #9 (parent #6) [English] refs=AHD; KLN | alcohol, algorithm, antimony
13	#10 (parent #0) [Arabic] refs=KLN; AHD; OEW; SKT | al-qela : alkaline material obtained from wood ashes ; az-zarnîx : arsenic ☞Ghel ; al-mâlâgma : the soft material, amalgam ☞Mel 3
14	  #11 (parent #10) [French] refs=None | 
15	    #12 (parent #11) [Persian] refs=VOP | âlkâlî «آلکالی» : alkaline ; ârsenîk «آرسنیک» : arsenic
16	    #13 (parent #11) [English] refs=AHD | alkali, alkaline, arsenic, amalgam
17	#14 (parent #0) [Arabic] refs=KLN; AHD; OEW | Al-lah : the God ☞Layh ; al-qadŭs : water carrier, albatross ; al-anbîq : distilling apparatus ☞Nei 1,Ab 1 ; al-bâdenjân : aubergine ☞Vatin-ganah ; al-nil : the indigo ☞Nei 1
18	  #15 (parent #14) [English] refs=AHD; OEW | Allah ; albatross ; alembic ; aubergine ; anil, aniline
19	#16 (parent #0) [Arabic] refs=KLN; AHD; OEW | al-iksir : a dry medicine, elixir ☞Ksero ; al-a`sârah : the juice, dye ☞A`.s.r ; al-jabr-w`al- moqâbeleh : reunion and comparison, algebra ☞J.b.r ; al-kîmîyâ : the art of transmutation. ☞Kers 2,Gheu ; al-oud : the wood, lute ☞Agaruth
20	  #17 (parent #16) [English] refs=AHD; KLN | elixir ; alizarin ; algebra ; alchemy, chemistry ; lute, flute, aloe
21	#18 (parent #0) [Arabic] refs=KLN; AHD; OEW | al-bîrquq : early ripening (plum) ☞Pekw ; dr-as-sanâ : house of fabrication, factory ☞S.n.`a,D.v.r ; as-sumut : the directions ☞Mei 3 ; Jabal-al-Târiq : "mountain of Tariq" who invaded Spain in 711 ☞J.b.l ; al-qubbah : the arch, alcove ☞Gabbah
22	  #19 (parent #18) [English] refs=KLN; OEW | apricot ; arsenal ; azimuth ; Gibraltar ; alcove
23	
```


## [2026-09-04T19:28:28.926Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-47.json",
 "description": "Read page 47 source JSON"
}
```


### [2026-09-04T19:28:28.966Z] TOOL RESULT

```
{
  "pdf_page": 47,
  "book_page": 17,
  "entries": [
    {
      "root": {
        "name": "Al 3",
        "lang": "Arabic",
        "refs": "SAP:43",
        "gloss": "definite article \"the\" used as a prefix",
        "note": "The letter \"L\" changes to the first letter of the following word under certain rules; for example \"al-sanâ`a\" becomes \"as-sanâ`a\". Most of these Arabic words have reached Europe through Spanish and French."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON",
          "words": [],
          "script_extra": "الله ، الکل ، المثنّی",
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN; AHD; OEW",
          "words": [
            {"translit": "Amir al-bahr", "gloss": "sea commander, admiral", "script": null, "see": ["A`.m.r"]},
            {"translit": "al-fesfeseh", "gloss": "horse food", "script": null, "see": ["Ed", "Ekwos"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "AHD; OEW",
          "words": [
            {"translit": "admiral", "gloss": null, "script": null},
            {"translit": "alfalfa", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "âdmîral", "gloss": "admiral", "script": "آدمیرال"},
            {"translit": "âlfâlfâ", "gloss": "alfalfa", "script": "آلفا آلفا"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN; AHD; OEW",
          "words": [
            {"translit": "al-kahl", "gloss": "highly purified spirits, alcohol", "script": null, "see": ["K.h.l"]},
            {"translit": "al-Xwârazmî", "gloss": "the 9th century mathematician who devised \"algebra\".", "script": null, "see": ["Ghdhem"]},
            {"translit": "al-ithmud", "gloss": "antimony", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON; VOP",
          "words": [
            {"translit": "alkol", "gloss": "alcohol", "script": "الکل"},
            {"translit": "âlgoritm", "gloss": "algorithm", "script": "آلگوریتم"},
            {"translit": "ântîmoân", "gloss": "antimony", "script": "آنتیموان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 6,
          "lang": "English",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "alcohol, algorithm, antimony", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN; AHD; OEW; SKT",
          "words": [
            {"translit": "al-qela", "gloss": "alkaline material obtained from wood ashes", "script": null},
            {"translit": "az-zarnîx", "gloss": "arsenic", "script": null, "see": ["Ghel"]},
            {"translit": "al-mâlâgma", "gloss": "the soft material, amalgam", "script": null, "see": ["Mel 3"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "VOP",
          "words": [
            {"translit": "âlkâlî", "gloss": "alkaline", "script": "آلکالی"},
            {"translit": "ârsenîk", "gloss": "arsenic", "script": "آرسنیک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 11,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "alkali, alkaline, arsenic, amalgam", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN; AHD; OEW",
          "words": [
            {"translit": "Al-lah", "gloss": "the God", "script": null, "see": ["Layh"]},
            {"translit": "al-qadŭs", "gloss": "water carrier, albatross", "script": null},
            {"translit": "al-anbîq", "gloss": "distilling apparatus", "script": null, "see": ["Nei 1", "Ab 1"]},
            {"translit": "al-bâdenjân", "gloss": "aubergine", "script": null, "see": ["Vatin-ganah"]},
            {"translit": "al-nil", "gloss": "the indigo", "script": null, "see": ["Nei 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": "AHD; OEW",
          "words": [
            {"translit": "Allah", "gloss": null, "script": null},
            {"translit": "albatross", "gloss": null, "script": null},
            {"translit": "alembic", "gloss": null, "script": null},
            {"translit": "aubergine", "gloss": null, "script": null},
            {"translit": "anil, aniline", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN; AHD; OEW",
          "words": [
            {"translit": "al-iksir", "gloss": "a dry medicine, elixir", "script": null, "see": ["Ksero"]},
            {"translit": "al-a`sârah", "gloss": "the juice, dye", "script": null, "see": ["A`.s.r"]},
            {"translit": "al-jabr-w`al- moqâbeleh", "gloss": "reunion and comparison, algebra", "script": null, "see": ["J.b.r"]},
            {"translit": "al-kîmîyâ", "gloss": "the art of transmutation.", "script": null, "see": ["Kers 2", "Gheu"]},
            {"translit": "al-oud", "gloss": "the wood, lute", "script": null, "see": ["Agaruth"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "English",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "elixir", "gloss": null, "script": null},
            {"translit": "alizarin", "gloss": null, "script": null},
            {"translit": "algebra", "gloss": null, "script": null},
            {"translit": "alchemy, chemistry", "gloss": null, "script": null},
            {"translit": "lute, flute, aloe", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN; AHD; OEW",
          "words": [
            {"translit": "al-bîrquq", "gloss": "early ripening (plum)", "script": null, "see": ["Pekw"]},
            {"translit": "dr-as-sanâ", "gloss": "house of fabrication, factory", "script": null, "see": ["S.n.`a", "D.v.r"]},
            {"translit": "as-sumut", "gloss": "the directions", "script": null, "see": ["Mei 3"]},
            {"translit": "Jabal-al-Târiq", "gloss": "\"mountain of Tariq\" who invaded Spain in 711", "script": null, "see": ["J.b.l"]},
            {"translit": "al-qubbah", "gloss": "the arch, alcove", "script": null, "see": ["Gabbah"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "English",
          "refs": "KLN; OEW",
          "words": [
            {"translit": "apricot", "gloss": null, "script": null},
            {"translit": "arsenal", "gloss": null, "script": null},
            {"translit": "azimuth", "gloss": null, "script": null},
            {"translit": "Gibraltar", "gloss": null, "script": null},
            {"translit": "alcove", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-04T19:28:30.975Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat SOURCE_MATRIX.md && echo \"=====REFS ONLINE=====\" && cat refs_online.json",
 "description": "Read source matrix and refs online"
}
```


### [2026-09-04T19:28:31.029Z] TOOL RESULT

```
<persisted-output>
Output too large (126.6KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/blef2k8a0.txt

Preview (first 2KB):
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
...
</persisted-output>
```


## [2026-09-04T19:28:37.280Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['SAP','MON','KLN','AHD','OEW','SKT','VOP','FVQ','AFM','PLA','AFA','LKT','PHN','DEV','LAM','DOZ','FSD','WEB','HJB','AID','BQT','ARY','SYN']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False))\n\""
}
```


## [2026-09-04T19:28:38.232Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && sed -n '/Arabic/,/Turkic/p' SOURCE_MATRIX.md | head -120"
}
```


### [2026-09-04T19:28:39.055Z] TOOL RESULT

```
<persisted-output>
Output too large (33.5KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b7o27r6u4.txt

Preview (first 2KB):
SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only. Google Books no-view records 4yQPAQAAMAAJ (1977), NoplAAAAMAAJ (1985), HcGipwAACAAJ (2001)."}
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_
...
</persisted-output>
```


### [2026-09-04T19:28:40.594Z] TOOL RESULT

```
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
```


## [2026-09-04T19:28:45.951Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json,textwrap\nd=json.load(open('refs_online.json'))\nfor k in ['OEW','VOP','SKT','AHD','KLN']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print('===',k)\n    for f in ['title','kind','url','lookup_hint','local_file','page_offset','notes']:\n        print(' ',f,':',str(v.get(f))[:600])\n\""
}
```


## [2026-09-04T19:28:46.695Z] TOOL CALL #8: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---\" && sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-04T19:28:48.607Z] TOOL RESULT

```
=== OEW
  title : J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984
  kind : archive_restricted
  url : https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view
  lookup_hint : Borrow via IA lending (djvu.txt returns 401/403). Entries are IE roots in alphabetical order; use IA's in-book search: https://archive.org/details/originsofenglish00jose?q=<root>
  local_file : None
  page_offset : None
  notes : RE-SEARCH 2026-09: borrowable only (Internet Archive lending, 1 hr / 14 days with a free account).
=== VOP
  title : Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992
  kind : none
  url : None
  lookup_hint : Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).
  local_file : None
  page_offset : None
  notes : RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only.
=== SKT
  title : W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)
  kind : archive_djvu
  url : https://archive.org/details/aconciseetymolo01skeagoog
  lookup_hint : Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
  page_offset : leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  notes : Nourai says '1882-1967'; the 1967 Oxford reprint reproduces the 1911 rewritten edition, so the 1911 scan is the right pagination.
=== AHD
  title : W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)
  kind : archive_djvu+website+archive_restricted
  url : https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only
  lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves 
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
  page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
  notes : AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.
=== KLN
  title : E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  kind : archive_djvu
  url : https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein
  lookup_hint : Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
  page_offset : KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  notes : Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)
```


### [2026-09-04T19:28:48.658Z] TOOL RESULT

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
process
sources
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


## [2026-09-04T19:28:52.656Z] TOOL CALL #9: Bash

```json
{
 "command": "sed -n '80,200p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-04T19:28:52.699Z] TOOL RESULT

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


## [2026-09-04T19:28:53.239Z] TOOL CALL #10: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-43.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:3000])\n\""
}
```


### [2026-09-04T19:28:54.918Z] TOOL RESULT

```
{
 "pdf_page": 43,
 "book_page": 13,
 "verified_by": "claude-fable-5-1",
 "verified_on": "2026-09-04",
 "entries": [
  {
   "entry": 0,
   "root": "Ak, Aq, Aken",
   "verdict": "confirmed",
   "modern_form": "PIE *h₂eḱ- (Pokorny *ak̑-, ok̑-) 'sharp, pointed; stone'; n-stem *h₂eḱ-en- (Pokorny/Kent *ak̑-en-) 'stone, whetstone' — Nourai's third variant 'Aken'",
   "note": "Root box, language label and gloss are all right: Pokorny p.18 heads the lemma 'ak̑-, ok̑- (*hek-)  Meaning: \"sharp; stone\"' (POK_full.txt line 3242, Page(s): 18-22), i.e. exactly Nourai's 'sharp, also a sharp stone'; the n-stem 'Aken' is Kent's pIE *aken- (OP asan- 'stone') and Walde-Pokorny I 30 'Mit n-Formantien: ai. aśáni-ḥ ..., gr. ἀκόνη \"Wetzstein\"'. The whole chart hangs on Pokorny's own remark at the head of lemma k̑ē(i)-: 'Note: probably further formations from ak̑- \"sharp\" (see 18 ff.)', and the ak̑- entry reciprocally lists 'k̑ei-, k̑oi-, k̑ə(i)- \"sharpen, whet\"' among its zero-grade offshoots — so the root→#1 arrow is Pokorny's, flagged by him as 'probably'. THREE data points on this page are the author's own errors rather than scan errors (checked against the page image, pdftoppm p.43: the book really prints them): (a) node #2 files Sanskrit śāṇa- / abhi-śāṇa- ('čâna', 'abhi-čâna') under the Avestan box — Nourai regularly writes Sanskrit ś as č (cf. 'čvitra' = śvitra, 'črî' = śrī elsewhere in the book) and took the pair straight from Horn no. 98 ('skr. śāna- \"Wetzstein\" + abhi') and Pokorny 541 ('ai. śāna- m.'); (b) node #4's second Old Persian form 'asam' is not an OP word for stone (Kent's asam is the acc. of asa- 'horse'); it is a misreading of Mann IEC:11 'OPer. asa, asan-'; (c) node #3's 'fsân' is a misprint for fasân/fesân (the Persian script فسان on the same line is correct).",
   "sources": [
    "https://en.wiktionary.org/wiki/hone",
    "https://en.wiktionary.org/wiki/%CE%BA%E1%BF%B6%CE%BD%CE%BF%CF%82",
    "https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%BE%E0%A4%A3"
   ],
   "ref_check": [
    {
     "ref": "POK:18",
     "status": "supports",
     "note": "POK_full.txt line 3242 (starling dump of IEW): 'Root / lemma: ak̑-, ok̑- (*hek-) | Meaning: \"sharp; stone\" ... Page(s): 18-22'. The entry closes: 'zero grades k̑- stuck probably in stems k̑emen-, k̑emel-, k̑omen- \"stone, skies\", k̑omor- \"stone hammer\", k̑ei-, k̑oi-, k̑ə(i)- \"sharpen, whet\", k̑u- \"sharp, spit, spear\"' — i.e. Pokorny himself subordinates Nourai's node #1 to this root."
    },
    {
     "ref": "KNT:173",
     "status": "supports",
     "note": "KNT.txt lines 5118-5124 (page marker '173' at line 5118, entry straddles the p.172/173 column break): 'asan- sb. \"stone\": pIE *aken- (§9.V, §87, §155.I), cf. asman-. See also Asagarta-. asā (§124.5, §187) nsm. DSf 40f'. Kent p.173 thus gives precisely the root Nourai calls 'Aken' and the OP word of node #4."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I p. 28 ff. (WLD_Bd1_1930_dli_70244_djvu.txt li
```


## [2026-09-04T19:30:06.534Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80; echo \"--- incoming:\"; ls incoming 2>/dev/null"
}
```


### [2026-09-04T19:30:06.583Z] TOOL RESULT

```
AFA.txt
AFM_alt.txt
AFM_pages.txt
AFM.pdf
AFM.txt
AHD_watkins1985.txt
AHM.txt
AID.txt
AIN.txt
AKD.txt
ARB_abdulraheem.txt
ARB_mo3rb.txt
ARP.txt
AVG.txt
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
BRT.txt
BST.txt
CHEUNG.txt
DEV.txt
DOZ.txt
DRM.txt
EAV_studies.txt
FRS_pages.txt
FRS.txt
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
FSF_pages.txt
FSF.txt
FVQ_pages.txt
FVQ.txt
GPL.txt
HENNING_selected_papers.txt
HID.txt
HJB.txt
HRN.txt
HUB.txt
IEC.txt
incoming
ISS_alt_DKS.txt
KFL.txt
KLN_1966.txt
KLN_1971.txt
KNT.txt
LAM.txt
LAT.txt
LEW_1910.txt
LKT.txt
LST.txt
MON_part1.txt
MON_part2.txt
MPP.txt
NAT_2005.txt
NYB.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
ocr
pageimg
PEI.txt
PHD_mackenzie.pdf
PHD_mackenzie.txt
PHD_pages.txt
PHD.pdf
PHD.txt
PHN.txt
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
RCH.txt
SBK.txt
SDQ.txt
SIN.txt
--- incoming:
AHD
ARY
BLY
BQT
CEL
FFD
IRN
ISS
KGW
MAG
MFL
MON
OEW
PLA
PRT
_tessdata
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
```


## [2026-09-04T19:30:06.862Z] TOOL CALL #12: Bash

```json
{
 "command": "ls data/ ; ls *.pdf 2>/dev/null; find . -name \"*.pdf\" -maxdepth 3 2>/dev/null | grep -v verification | head"
}
```


### [2026-09-04T19:30:06.924Z] TOOL RESULT

```
ANOMALIES.md
extracted
EXTRACTION_SPEC.md
research
translations
verification
EtymologicalDictionary-persian-english.pdf
./EtymologicalDictionary-persian-english.pdf
```


## [2026-09-04T19:30:12.485Z] TOOL CALL #13: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/img && pdftoppm -f 47 -l 47 -r 190 -png EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/img/p47 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/img/"
}
```


## [2026-09-04T19:30:14.295Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN admiral ===\" && grep -n \"^admiral\" KLN_1966.txt | head; echo \"=== KLN alfalfa ===\" && grep -n \"^alfalfa\" KLN_1966.txt | head; echo \"=== KLN alcohol ===\" && grep -n \"^alcohol\" KLN_1966.txt|head; echo \"=== KLN antimony ===\" && grep -n \"^antimony\" KLN_1966.txt|head; echo \"=== KLN algorithm/algorism ===\" && grep -n \"^algori\" KLN_1966.txt|head"
}
```


### [2026-09-04T19:30:14.676Z] TOOL RESULT

```
total 104
drwxrwxr-x  2 sfmqrb sfmqrb  4096 Sep  4 15:30 .
drwx------ 15 sfmqrb sfmqrb  4096 Sep  4 15:30 ..
-rw-rw-r--  1 sfmqrb sfmqrb 97385 Sep  4 15:30 p47-047.png
```


### [2026-09-04T19:30:14.771Z] TOOL RESULT

```
=== KLN admiral ===
=== KLN alfalfa ===
2169:alfalfa,  n.,  lucerne.  —  Sp.,  fr.  Arab,  al-fasfasa  . (Cp.  the  collateral  Sp.  form  alfalfez,  which  rep¬ resents  the  intermediate  form  between  Arab. al-fdsfasah  and  Sp.  alfalfa.). alfaqui,  n.,  a  Mohammedan  scholar.  —  Sp.,  fr. Arab,  al-faqfh,  fr.  al-,  ‘the’,  and  faqih,  ‘learned, intelligent’,  fr.  fiqh,  ‘knowledge,  intelligence’, alfenide,  n.,  an  alloy  of  nickel  and  silver.  —  So called  after  the  chemist  Halphen,  who  invented this  alloy  in  1850.  For  the  ending  see  suff.  -ide. Alfred,  masc.  PN.  —  OE.  Mfrsed,  compounded of  self,  ‘elf’,  and  rted,  ‘counsel’.  See  elf  and  read, alfresco,  adv.  and  adj.,  in  the  open  air.  It.  al fresco ,  lit.  ‘in  the  fresh  (air)’.  It.  al,  lit.  ‘to  the  , is  formed  fr.  a,  ‘to’  (fr.  L.  ad), and  the  dcf.  article il  (fr.  L.  ille,  ‘that’);  see  ad-  and  ille  and  cp.  al segno.  For  It.  fresco  see  fresco, alga,  n.  —  L.,  ‘sea  weed’,  cogn.  with  OI.  pifdh, ‘viscous,  sticky’,  Norw.  ulka,  ‘moldy ;  slime  , fr.  I.-E.  base  *el-,  *ol-,  ‘to  putrefy,  rot’,  whence also  Norw.  ul,  ‘moldy’,  Swed.  ul,  rancid  ,  L. ulva,  ‘sedge’.  Cp.  Ulva.
=== KLN alcohol ===
=== KLN antimony ===
2983:antimony,  n.,  a  brittle  metallic  element  (chem.)  — ML.  antimonium,  prob.  fr.  Arab,  al-uthmud, al-ithmid,  from  al-,  ‘the’,  and  uthmud,  ithmid, ‘stibium’,  which  prob.,  derives  fr.  Gk.  ox tpqu, ‘stibium’.  See  stibium  and  -y  (representing  L. -ium).
=== KLN algorithm/algorism ===
```


## [2026-09-04T19:30:19.674Z] TOOL CALL #15: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/img/p47-047.png"
}
```


### [2026-09-04T19:30:20.134Z] TOOL RESULT

```

```


## [2026-09-04T19:30:20.132Z] INPUT

[Image: original 1615x2090, displayed at 1545x2000. Multiply coordinates by 1.05 to map to original image.]


## [2026-09-04T19:30:35.466Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/img && pdftoppm -f 47 -l 47 -r 500 -png -x 2400 -y 1050 -W 900 -H 350 /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf crop1 && ls"
}
```


### [2026-09-04T19:30:38.460Z] TOOL RESULT

```
crop1-047.png
p47-047.png
```


## [2026-09-04T19:30:40.268Z] TOOL CALL #17: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/img/crop1-047.png"
}
```


### [2026-09-04T19:30:40.286Z] TOOL RESULT

```

```


## [2026-09-04T19:30:43.799Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/img && pdftoppm -f 47 -l 47 -r 500 -png -x 2400 -y 1330 -W 900 -H 160 /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf crop2 && echo ok"
}
```


### [2026-09-04T19:30:45.720Z] TOOL RESULT

```
ok
```


## [2026-09-04T19:30:47.687Z] TOOL CALL #19: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/img/crop2-047.png"
}
```


### [2026-09-04T19:30:47.701Z] TOOL RESULT

```

```


## [2026-09-04T19:31:00.296Z] TOOL CALL #20: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py <<'EOF'\nimport sys, re, io\npath, pat = sys.argv[1], sys.argv[2]\nwidth = int(sys.argv[3]) if len(sys.argv)>3 else 400\nmaxn = int(sys.argv[4]) if len(sys.argv)>4 else 6\ndata = open(path, encoding='utf-8', errors='replace').read()\npages = data.split('\\f')\nrx = re.compile(pat, re.I)\nn=0\nfor i,pg in enumerate(pages):\n    for m in rx.finditer(pg):\n        s=max(0,m.start()-60); e=min(len(pg), m.start()+width)\n        print(f\"--- [ffpage {i}] {' '.join(pg[s:e].split())}\")\n        n+=1\n        if n>=maxn: sys.exit()\nif n==0: print(\"NO MATCH\", path, pat)\nEOF\necho ok"
}
```


### [2026-09-04T19:31:00.333Z] TOOL RESULT

```
ok
```


## [2026-09-04T19:31:04.729Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###KLN admiral\"; python3 $S KLN_1966.txt 'admiral,\\s+n' 700 2\necho \"###KLN alcohol\"; python3 $S KLN_1966.txt 'alcohol,\\s+n' 700 2\necho \"###KLN algorism\"; python3 $S KLN_1966.txt 'algori[sz]m' 700 3\necho \"###KLN alkali\"; python3 $S KLN_1966.txt 'alkali,\\s+n' 700 2\necho \"###KLN arsenic\"; python3 $S KLN_1966.txt 'arsenic,\\s+n' 800 2\necho \"###KLN amalgam\"; python3 $S KLN_1966.txt 'amalgam,\\s+n' 700 2"
}
```


### [2026-09-04T19:31:07.259Z] TOOL RESULT

```
###KLN admiral
--- [ffpage 25] Mirabel. Derivatives: admirable, n., admirabl-y, adv. admiral, n. — OF. amiral, amiralt <F. amiral), prob. shortened fr. Arab, amtr-ar-rahl, ‘com¬ mander of transport, officer commanding a (transport) fleet', whence also Port, amiralhs, amiral, It. ammiraglio (.It. almiraglio and It., Sp. and Port, almirante arose from a confusion of am-, the beginning of the word amir, with the Arab. art. a!-; It., Sp. and Port, almirante were transformed after the pres. part. suff. -ante, fr. L. -antem; see -ant); influenced in form by L. admirari, ‘to admire’. See ameer, amir, admiralty, n. — ME., fr. OF. admiralte (whence MF. amiralte, F. amiraute). See admiral and -ty. adm
###KLN alcohol
--- [ffpage 36] trength, power’. See Alexander, alcohol, n. — ML., fr. Arab, al-kohl , vulgar pro¬ nunciation of al-kuhl, fr. a/-, the , and kohl, resp. kuhl, ‘antimony (used for painting the eye¬ lids)’, which is rel. to Heb. kahal (Ezek. 23.40), ‘he painted the eyelids with antimony’, Aram.- Syr. kfhal, Ethiop. kahala, of s.m., Aram. kuhld, Ethiop. kuhel, ‘antimony’. (Akkad, guhlu, ‘antimony’, is prob. a WSem. loan word.)Its mod¬ em sense (‘highly rectified spirits’) is due to the analogy of the fineness of this powder. Cp. kohl. Derivatives: alcohol-ic, adj., alcohol-ic-ally , adv., alcohol-ism , n., alcohol-ize , tr. v. alcoholometer, n., an instrument
###KLN algorism
--- [ffpage 37] o the s/crbja'bara, ‘he bound together, united’. Cp. algorism. Derivatives; algebra-ic, algebra-ic-al , adjs., al- gebra-ic-al-ly, adv., algebraization (q.v.), alge¬ braist (q.v.) algebraist, n., an expert in algebra. — A hybrid coined fr. algebra and -ist, a suff. of Greek origin. . algebraization, n., reduction of algebraic sym¬ bols (philos.) — G. Algebraisierung, fr. algebra- isieren, a hybrid coined by Edmund Husserl (1859-1938) fr. algebra and suff. -isieren, fr. Gk. -£eiv. See -ize and -ation. algebraize, tr. v. — See prec. word, algedonic, adj., characterized by the association of pain and pleasure. — Compounded of Gk. aXyo?, ‘pain, and IjSovixos, ‘pleasant’,
--- [ffpage 37] n’, albor, ‘white color’, fr. albere, ‘to be white’, algorism, n., the Arabic system of numerals. — ME. algorisme, fr. OF. algorisme (F. algorith- me), fr. ML. algorismus , from the inexact trans¬ literation of Arab. al-Khowarizmi, ‘the man of Khowarizm (the modern Khiva), surname of Abu Jafar Mohammed ibn Musa, great mathe¬ matician of the 9th cent. His famous work Al- jabr w’al muqdbalab (‘Reunion and compar¬ ison’), introduced the use of Arabic numerals in Europe, which denoted a turning point in the history of mathematics. Cp. algebra, algous, adj., pertaining to algae. — L. algosus, fr. alga, ‘seaweed’. See Alga and -ous. alguazil, n., peace officer in S
--- [ffpage 37] algorism, n., the Arabic system of numerals. — ME. algorisme, fr. OF. algorisme (F. algorith- me), fr. ML. algorismus , from the inexact trans¬ literation of Arab. al-Khowarizmi, ‘the man of Khowarizm (the modern Khiva), surname of Abu Jafar Mohammed ibn Musa, great mathe¬ matician of the 9th cent. His famous work Al- jabr w’al muqdbalab (‘Reunion and compar¬ ison’), introduced the use of Arabic numerals in Europe, which denoted a turning point in the history of mathematics. Cp. algebra, algous, adj., pertaining to algae. — L. algosus, fr. alga, ‘seaweed’. See Alga and -ous. alguazil, n., peace officer in Spain. — Sp. alguacil, fr. earlier alguazil, fr. Arab
###KLN alkali
--- [ffpage 38] t, a pseudo- Arabic word prob. coined by Paracelsus, alkali, n. — F. alcalli (now spelled alcali), fr. Arab, al-qilt, fr. al-, ‘the’, and qilt, ‘charred ashes of the saltwort’, fr. qala, ‘he fried, roast¬ ed’, which is rel. to Heb. qaldh, ‘he roasted, parched’, Aram. qeld, ‘burned’, Akkad, qalu. ‘to burn’ ; cp. kali. The word alkali first appears in the writings of Albertus Magnus (i 2o6?-i 280). alkalimeter, n., an instrument for measuring the strength of alkalis. — A hybrid coined fr. alkali and Gk. piTpov, ‘measure’. See meter, ‘poet¬ ical rhythm’. alkaline, adj. — A hybrid coined fr. alkali and -ine, a chem. suff. of Latin origin. alkaloid, n. — A hy
###KLN arsenic
--- [ffpage 68] ade’. For the ending of arsenal see adj. suff. -al. arsenic, n., a chemical element. — OF. (= F.) arsenic, fr. L. arsenicum, arrhenicum, fr. Gk. dptrsvixov, appevvxov, ‘yellow orpiment', fr. MPers. *zarnik, ‘gold, golden ; orpiment’(whence ModPers.-Arab. zarnikh, ‘orpiment’), through the medium of a Semitic language; cp. Mish- naic Heb. zarnikh, Syr. zarnikhd, ‘orpiment’. Cp. Avestic zaranya, Pers. zar, ‘gold’, and the first element in zermahbub, and see yellow and words there referred to. Cp. also jargon, ‘a variety of zircon’. Gk. apctevtxov, appsvtx&v, ‘orpiment’, was influenced in form by apcrevtxop, appevixic, ‘male’, fr. ape rc;v, ap pr,v, ‘male’. For the sense development of MPers. *zarnik, cp. L. auripigmentum, fr. aurum, ‘gold’ (see orpiment). De
###KLN amalgam
--- [ffpage 42] , adv. — Formed fr. a-, on , and main, ‘strength’. amalgam, n., i) a mixture of mercury with a metal or metals ; 2) a mixture, blend. — F. amal- game, fr. ML. amalgama, dissimil. fr. Arab, al- malgham, which is formed fr. Arab, al-, the and Syr. malagmd, fr. Gk. paXocyp-a, ‘a soft mass’, fr. paXdcmeiv, ‘to soften’, fr. paXaxo?, ‘soft’. See malaco- and cp. Amalthaea. Derivatives: amalgam, v. (q.v.), amalgam-ate, tr. and intr. v., amalgam-at-ion, n., amalgam-al¬ ive, adj., amalgam-at-or , n., amalgam-ist, n., amalgam-ize, tr. v., amalgam-iz-al-ion, n. amalgam, tr. and intr. v., to amalgamate. F. amalgamer, fr. amalgame. See amalgam, n. Amalthaea, Amalthea, n„ th
--- [ffpage 42] v., to amalgamate. F. amalgamer, fr. amalgame. See amalgam, n. Amalthaea, Amalthea, n„ the nurse of Zeus (Creek mythol.) — L., fr. Gk. ’ApdXffcia, which is prob. rel. to paXdxxos;, ‘soft, light, weak’, paXax6?, ‘soft’. See malaco- and cp. amalgam. Amanda, fem. PN. — Lit. ‘worthy to be loved’, fem. of amandus, gerundive of amare, ‘to love’. See amatory and cp. Amabel and names there referred to. For other Latin gerundives used in English cp. agenda and words there referred to. Amandus, masc. PN. — L. See prec. word, amanuensis, n., a person employed to write from dictation; secretary. — L. amanuensis, formed with suff. -ertsis from the phrase servus a ma
```


## [2026-09-04T19:31:24.595Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\nfor p in 'albatross,\\s+n' 'alembic,\\s+n' 'aubergine,\\s+n' 'anil,\\s+n' 'aniline,\\s+n' 'elixir,\\s+n' 'alizarin' 'algebra,\\s+n' 'alchemy,\\s+n'; do echo \"###KLN $p\"; python3 $S KLN_1966.txt \"$p\" 650 1; done"
}
```


## [2026-09-04T19:31:26.508Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\nfor p in 'lute,\\s+n' 'flute,\\s+n' 'aloe,\\s+n' 'apricot,\\s+n' 'arsenal,\\s+n' 'azimuth,\\s+n' 'Gibraltar' 'alcove,\\s+n' 'chemistry,\\s+n'; do echo \"###KLN $p\"; python3 $S KLN_1966.txt \"$p\" 650 1; done"
}
```


### [2026-09-04T19:31:27.462Z] TOOL RESULT

```
###KLN albatross,\s+n
--- [ffpage 35] kkurfm, ‘first fruits’, Ethiop. bakur, ‘first bom’. 44 albatross, n. — Port alcatraz, ‘cormorant, peli¬ can’ (whence also F. albatros), a variant of alcatruz, ‘the bucket of a water wheel', fr. Arab. al-qddds, 'machine for drawing water; jar’, fr. al-, ‘the’, and Gk. xd8o?, ‘jar’, which is a loan word from Heb. kadh, of s.m. The name was orig. applied to the pelican as ‘the water carrier’, i.e. the bird that carries water in its pouch. For sense development cp. Arab, saqqd, ‘pelican’, lit. ‘water carrier’. The alteration of Port, alca¬ traz to E. albatross (after L. albus, ‘white’) was prob. suggested by the whit
###KLN alembic,\s+n
--- [ffpage 36] hich also derives fr. Teut. Alamann- (see allemande). alembic, n. — ME., fr. OF. (=F.) alambic, fr. OSp. (= Sp.) alambique fr. Arab, al-anbtq, ‘the still’, which is formed fr. al-, ‘the’, and Gk. 4p.(3tl;, ‘cup, cap of a still, alembic’, which is of uncer¬ tain, possibly Semitic origin. Cp. It. lambicco, which is of the same origin as Sp. alambique. Alenu, n., concluding prayer ( Jewish liturgy). — Heb. ‘dlimi, lit. ‘upon us’, formed fr. 'al, ‘on, upon’, with -dnu, the pronom. suff. of the 1st person in the plural. The prayer is so called from the first words ‘alenu leshabbiah, ‘it is (in¬ cumbent) upon us to
###KLN aubergine,\s+n
--- [ffpage 77] . (q.v.) See Bloch-Wartburg, DELF., p.43 s.v. aubain. aubergine, n., the eggplant. — G., fr. Catal. al- berginera, alberginia, fr. Arab, al-badinjan, ‘the eggplant’, fr. al-, ‘the’, and badinjdn, ‘eggplant’, fr. Pers. badin-gan, fr. OI. vatin-ganah. Cp. berengena. aubin, n., canter. — F., fr. earlier hobin, fr. hauby (15th cent.), fr. E. hobby (q.v.) Aubrey, masc. PN. — F. Auberi, fr. G. Alberich, lit. ‘ruler of elfs’. For the first element cp. ON. alfr, OE. self, ‘elf’, and see elf. For the second element see rich and cp. words there referred to. Aubrietia, n., a genus of plants of the mustard auburn aulacO' 126 12
###KLN anil,\s+n
--- [ffpage 52] nihte; see a-, ‘on’, night, and the adv. suff. -s. anil, n., 1) a West Indian shrub, from which in¬ digo is made; 2) indigo. — Port, anil, fr. Arab. an-ntl, assimilated fr. al-nil, fr. al-, ‘the’, and nil, ‘indigo’, fr. Pers. nila, ult. fr. OI. nili, ‘indi¬ go’, fr. ntlah, ‘dark blue’. Cp. lilac. Derivatives: anil-ic, adj., anil-ide, n., aniline (q.v.) anile, adj., like an old woman. — L. anilis, ‘per¬ taining to an old woman’, fr. anus, gen. anus, ‘old woman', from the I.-E. imitative base *an-, whence also Hitt, annash, ’mother’, hannash, ‘grandmother’, Gk. avvip, ‘grandmother’, Lith. ahyta, ‘mother-in-law’, OPr
###KLN aniline,\s+n
--- [ffpage 722] , fr. rosa. See rose and -aceous and cp. rosace. rosaniline, n., a crystalline compound obtained from aniline, C20H21ON3 ( chem .) — Compound¬ ed of rose and aniline. rosarian, n., a rose grower. — Formed with suff. -an fr. L. rosarium, ‘rose garden’. See rosary. rosarium, n., rose garden. — L. See next word and -arium. rosary, n., rose garden; string of beads used for counting series of prayers. — ME. rosarie, fr. L. rosarium, ‘rose garden’, in ML. also used in the sense of ‘garland; string of beads; series of prayers’, fr. L. rosa. See rose and subst. suff. -ary. roscherite, n., a hydrous basic phosphate of a
###KLN elixir,\s+n
--- [ffpage 277] ctus, pp. of eligere. See elect and cp. prec. word. elixir, n., 1) asubstance supposed to prolonglife; 2) a substance supposed to change all metals into gold. — ML., fr. Arab, al-iksir, which is formed fr. Arab, al-, ‘the’, and Gk. jjp'.ov, ‘dry medicinal substance, cataplasm’, fr. ‘dry’. See serene and cp. xero-. Elizabeth, 1) fern. PN.; 2) in the Bible, the name of the wife of Aaron. — Late L. Elisabeth, fr. Gk. ’EXELaotJUeft, ’EXtaafte-r, fr. Heb. Elishebha', lit. ‘God is an oath’. For the first element see El. The second element is rel. to shivfdh, fem. sheva‘, ‘seven’, and to nishbd‘, ‘he swore’, orig. ‘he
###KLN alizarin
--- [ffpage 38] el. to Heb. ‘atzar, Aram.-Syr. ‘dtzdr, ‘he retained’, alizarin, alizarine, n., a dye (chem.) — F. ali¬ zarine, fr. alizari. See prec. word and chem. suff. -in, -ine. aljama, n., a Jewish congregation in Spain. — Sp., fr. Arab. al-jamd'ah, fr. al-, ‘the’, and ja- md'a’', ‘assembly’, fr. jama'a, ‘he gathered to¬ gether, assembled’. aljamia, n., Moorish name of the Spanish lan¬ guage. — Sp. aljamia, fr. Arab. al-‘ajamtyah, ‘the non-Arabic, barbarian (language)’, fr. al-, ‘the’, and fern. oVajamt, ‘non-Arabic, barbarian’, aljofaina, n., wash basin. — Sp., fr. Arab, al- jufaynah, dimin. of al-jdfnah (whence Sp, alja- fana),
###KLN algebra,\s+n
--- [ffpage 37] pis juiiflora. — Sp., a dimin. formed fr. algarroba. algebra, n. — Fr. Arab, al-jabr (in vulgar pro¬ nunciation al-jebr), ‘reunion (of broken parts in equations)’, short for al-jabr w‘ al-muqdbalah , ‘re¬ union and comparison’, title of a work written by Mohammed ibn Musa al-Khowarizrru, great mathematician of the 9th cent. The title refers to, and the work deals with, the solution of equations, which was the original scope of algebra. Al-jabr is formed fr. al-, ‘the’, and jahr, ‘reunion’, which is rel. to the s/crbja'bara, ‘he bound together, united’. Cp. algorism. Derivatives; algebra-ic, algebra-ic-al , adjs., al- geb
###KLN alchemy,\s+n
--- [ffpage 35] ‘crown’. For the second element see malik, Mameluke, alchemy, n. medieval chemistry. — OF. alquemie (13th cent.), alchimie (14th cent.) (F. alchimie), fr. ML. alchemia, fr. Arab, al-kimiyd, fr. al-, "the’, and MGk. yr(uda, a, prop, ’the art of the black land (Egypt)’, fr. Gk. Xrjuta, ‘Black- land, Egypt’, fr. Egypt, khem, khame, ‘black’. The derivation from Gk. x'JireiS, ‘pouring’, from the stem of y_£e iv, ‘to pour’, is folk ety¬ mology. See W. Muss-Amolt, Transactions of the American Philological Association, vol. alcmaeon aiexipnarmic XXIII, p- 149. Cp. chemical, chemist, chemistry. Derivatives: alchem-ic, alchem-ic-al, a
```


### [2026-09-04T19:31:30.539Z] TOOL RESULT

```
###KLN lute,\s+n
--- [ffpage 15] nd cp. consolute, dissolute, resolute. Derivatives: absolute, n., absolute-ly, adv., ab- solule-ness, n. absolution, n. — OF. (= F.) absolution, fr. L. ab- solutionem, acc. of absolutid, ‘an acquittal’, fr. absolutus. See prec. word and -ion. absolutism, n. — Formed with suff. -ism fr. L. absolutus. See absolute. ■haolutist, n. — Formed with suff. -ist fr. L. ab¬ solutus. See absolute. ■**<*lve, tr. v. — L. absolvere, ‘to set free’, fr. •h- and solvere, ‘to loosen, set free'. See solve and cp. assoil. Cp. also dissolve, resolve. ^*orb, tr. v. — L. absorbere, ‘to swallow up’, fr. ab- and sorbere, ‘to suck in, swallo
###KLN flute,\s+n
--- [ffpage 327] s-tra and derives fr. fluere, ‘to flow’. See fluent. flute, n. — ME. floute , floite, fr. OF. flaiite, fleiite (F. flute), fr. OProven?. flaiit, which is prob. a blend of OProven q.flaujol, ‘flageolet’, and laid, ‘lute’. See flageolet and lute, ‘a musical in¬ strument’. It .flauto and Sp. flauta are OProven?. loan words. Cp. flout. flute, intr. v. — ME. flouten, floiten, fr. OF, flak¬ ier, fleiiter (F. fluter ), fr. OF. flaiite, fleiite, ‘flute’. See flute, n. Derivatives: flut-ed, adj ., flut-er, n., flut-ing, n., flut-y, adj. flutist, n. — A hybrid coined fr. flute and -ist, a suff. of Greek origin. Cp. flautist, f
###KLN aloe,\s+n
--- [ffpage 41] alder. alodial, alodium, n. — See allodial, allodium, aloe, n. — L. aloe, fr. Gk. aX6r), ‘aloe’, prob. borrowed fr. Heb. ahaltm, ahaldth (pi.), which are perhaps borrowed fr. OI. agaruh, aguruh, ‘aloewood’, these latter being prob. of Dravid- ian origin. Cp. agalloch. aloetic, adj. containing, or of the nature of, aloes ; n., an aloetic medicine. — Formed with suff. -etic fr. Gk. aXot], ‘aloe’. See aloe, aloft, adv. — ON. a lopt, ‘in the air’, whence arose the meaning ‘on high’. See a-, ‘on’, and loft, aloin, n., a bitter crystalline substance (chem.) — Formed fr. aloe with chem. suff. -in; so called because it
###KLN apricot,\s+n
--- [ffpage 62] ent and verbal suff. -ate. Derivative: aprication, n. apricot, n. — F. abricot, fr. Port, albricoque fr. Arab. al-barqdq fr. al-, ‘the’, and upamixiov, Grecized form oih. praecoquum, ‘apricot’, neut. of praecoquus = praecox, ‘early ripe’, for which see precocious. See also cook. For the interchangeability of -c (= -k) and -t cp. havoc (fr. OF. havot), bat (fr. orig. bakke), and the words milt and milk , ‘milt of fishes . April, n. — L. ( mensis ) Aprilis, lit. ‘the month of Aphrodite’, fr. Gk. ’A<ppw, a short form of ’ AippoSfrr). See Aphrodite. Cp. L. mensis Maius, ‘the month of May’, prop, ‘the month of Jupite
###KLN arsenal,\s+n
--- [ffpage 68] k’, OIr. err (for *ersa), ‘tail’. Cp. uro-, ‘tail-’. arsenal, n., a place for manufacturing and storing ammunition and weapons. — It. arsenale (Olt. arzanale), ‘dock’, borrowed — prob. through the medium of MGk. d.pm]'tdkt)C, — fr. Arab, dar- a?-sind'ah (whence also Sp. darsena and It. dar- sena, ‘dock’), lit. ‘house of construction’, fr. ddr, ‘house’, as-, assimilated form of al-, ‘the’, and Sind'ah, ‘construction, art’, fr. Sana' a, ‘he made’. For the ending of arsenal see adj. suff. -al. arsenic, n., a chemical element. — OF. (= F.) arsenic, fr. L. arsenicum, arrhenicum, fr. Gk. dptrsvixov, appevvxov, ‘yellow orpiment'
###KLN azimuth,\s+n
--- [ffpage 41] alter, outer (F. autel). Derivative: altar-ed, adj. altazimuth, n., an instrument for observing the altitude and azimuth of a star (astron.) — Com¬ pounded of the abbreviation of altitude and of azimuth. alter, tr. and intr. v. — F. alterer, fr. Late L. al¬ ter are, ‘to change’, fr. L. alter, ‘the other (of two)’, which stands for *aliteros, *alitros, *altros, and is formed with the compar. suff. -ter fr. base *ali-, ‘there, beyond’, whence also alius, ‘an¬ other’. Hence alter and alius lit. denote ‘one who stands there’; the former— in keeping with the sense of the compar. suff. -ter — denotes ‘the other of two’,
###KLN Gibraltar
--- [ffpage 354] Frankish *gabaiti) fr. 61330/1, ‘to bite’. See bite. Gibraltar, n., name of the Rock at the western entrance to the Mediterranean. — Fr. Arab. jabal (in vulgar pronunciation jebel) al Tdriq, ‘mount of Tariq’, named after Tariq, the Mos¬ lem invader of Spain who landed there in 71 1. See javali and cp. Bible. gibraltar, n., American name of a hard (‘rocky’) candy. — Named after the fortress Gibraltar. See prec. word. gibus, n., an opera hat. — F., named after its in¬ ventor, a Parisian hatmaker, who lived in the 1st half of the 19th century, gid, n., a brain disease of sheep. — Back for¬ mation fr. giddy. gidd
###KLN alcove,\s+n
--- [ffpage 36] changed into *quer - nus. See cork and cp. Quercus. alcove, n., 1) a recessed section in a room; 2) any recess. — F. alcove , fr. Sp. alcoba, fr. Arab, al- qubbah, fr. al-, ‘the’, and qubbah, ‘arch, vaulted tent’, which is rel. to Arab, qabba, ‘it was bent’, and to Heb. qubbd \ ‘vaulted tent’, Syr. qebha- bhd, ‘vault, vaulted tent’, Akkad, qababu, ‘shield’. All these words are derivatives of the Sem. base q-b-b, ‘to be bent, crooked, vaulted’, aldea, n., hamlet, villa. — Sp. and Port., ham¬ let’, fr. Arab, al-, ‘the’, and dayah, ‘farm, ham¬ let’. Cp. aldeia. Aldebaran, n., a red star in the constellation Taur
###KLN chemistry,\s+n
--- [ffpage 103] iotic, ne¬ crobiosis, Rhizobium, symbion, symbiosis, biochemistry, n., chemistry dealing with animal and plant life. — See bio- and chemistry, biogen, n., a protoplasmic unit ( biol .) — Coined by the German physiologist Max Verwom (1863-1921) in 1903 fr. bio- and -gen. biogenesis, n., the theory that living organisms can only arise from pre-existing living matter (biol.)— Coined by the English biologist Thomas Henry Huxley (1825-95) in 1870 fr. Gk. pto?, ‘life’, and y^veoic, ‘origin, source’. See bio- and genesis and cp. abiogenesis. biogenesist, n., one who believes in the theory of biogenesis. — See prec. word and -i
```


## [2026-09-04T19:32:03.800Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###KLN lute\"; python3 $S KLN_1966.txt 'lute, n\\., a stringed' 600 2; python3 $S KLN_1966.txt \"lute.{0,40}musical instrument.{0,20}—\" 600 3\necho \"###KLN azimuth\"; python3 $S KLN_1966.txt 'azimuth, n' 600 2\necho \"###KLN chemistry\"; python3 $S KLN_1966.txt 'chemistry, n\\.' 600 2\necho \"###KLN Allah\"; python3 $S KLN_1966.txt 'Allah, n' 600 2"
}
```


## [2026-09-04T19:32:05.657Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###SKT alkali\"; python3 $S SKT.txt 'ALKALI' 500 2\necho \"###SKT arsenic\"; python3 $S SKT.txt 'ARSENIC' 500 2\necho \"###SKT amalgam\"; python3 $S SKT.txt 'AMALGAM' 500 2\necho \"###SKT admiral\"; python3 $S SKT.txt 'ADMIRAL' 500 2\necho \"###SKT alcohol\"; python3 $S SKT.txt 'ALCOHOL' 500 2"
}
```


### [2026-09-04T19:32:06.545Z] TOOL RESULT

```
###KLN lute
NO MATCH KLN_1966.txt lute, n\., a stringed
NO MATCH KLN_1966.txt lute.{0,40}musical instrument.{0,20}—
###KLN azimuth
NO MATCH KLN_1966.txt azimuth, n
###KLN chemistry
NO MATCH KLN_1966.txt chemistry, n\.
###KLN Allah
NO MATCH KLN_1966.txt Allah, n
```


### [2026-09-04T19:32:08.672Z] TOOL RESULT

```
###SKT alkali
--- [ffpage 28] n life (E.) For en Ihu » in life ; s«eI4f«. Swc phr. Alkali, a salt. tArab.^ AmK «/, amlya//, ashes of glass-wort, ^\hich al in soda. All. (E.) M. E. al, sing.; A.S. m/, pi. eaJle. + Icel. allf, Dan.a/; Du. a/; O. H.G. a/; pi. a/lai; Irwh uile ; W.^/A all. adv., otierly. In the &raJie (correctly u// to-braJ:e'^, Jut!ge«, Here the incorrect atlte, for 'utterly, up about Aj>. 1500, in pl.ice of iJiom which linked to to the verb: cCii is tebrokm Ihilkc retjioun/ Chaucer, 3750.
--- [ffpage 31] (i). see Mid. r. SceMias(i). . — t*) See Ajziatory. .aaalkali. (I. -Gk.^EgTpt- lactiaafor L. tai ammcnia^um, f, «al ammoniac. »k. 4^M*M*«i^ Ijbyan.*>Gk. ittyan Zrus>Amman: a wuni irigin; llerocl. ii. 4J. ^ It » ^mmoHtac was fint obtaixicO ^ of Ammnn. ^f<mil%hcn. (Gk.^ Coined Ef/ t,Gk. -trTi) from the nnme the shell resembles the oa the head of the imon. MunimeDt. : of ofTcuccs, -.- — L- amrtfjiia. ;»S cap. of wrong. I, — Gk. i-. not ; (VMAN.) It (£.) Sec MiDgla. ~ .matory. )k,) From >n.
###SKT arsenic
--- [ffpage 43] . oimoudrt, in, which from L. ifiShyw ralpharrt of arsenic ' gold ptint-' F. ot-timtnt. ifw. gold paint. * L. Avn-. IxL fismtnlum, a pigment, f»rr. 1 V— • ;>itl slnnc-crop. od M 'i>ut. M b. l\u», * orpiD, or lire'long ; * Cot A docked form of ^UMUltAUon ; seeAadi- AVAST, «3 Aurora, the dawn. (L.) L. avrem, the dawn ; put for an oldtri ausosa *.+Gk. ijif, ..4iolic afaff ; Skt. uikAsd, dawn. (^US.) Auepioe. (F.-L.) See Aviary. Austere. (F.-L.-Gk.) '^A.'E. amUrt. — O. h' .
###SKT amalgam
--- [ffpage 29] for aJita^e. to apjifi ▲Uionoai mc LU^^iu-vat rCATOR. AMALGAM. lee IiiMTd. i ; sc< lilnimcnt. t« I^ooui. . hKT Itoqiiiioiou*. L.T L -(). Low G.) Low ■um, aiaJtutn, of itlaJu^ a free in- It means * entire ' i, «/(*./; where oV »w ng: i.ics 'property' or I O. 1j>w G. oti I* cognate vili/, Iccl. auiSr, wealth. itment by medicines >(KMtlc cHcct to that of to kpmtref^ihy, for dXXof, othtr ; nnd r; MtAU«aandF«tl&o«. ft attSgn, grant ; see I«ootu. to pnuse, apt>rove of; see D See p. 143.
###SKT admiral
--- [ffpage 24] F. ajeuttr. Adjutant: see Aid. Administer ; see Minor. Admiral. (F.-Arab.) M.E. more often amiraLm^O. F. amiral, also amirt\ cf. Low L. admu prince, chief.* Arab, amlr^ a pri Elmir. The suffix is due to Arab.] amir-ai-baJir, pnncc of ihc sea. Admire : sec Mtraola. Admit : see Blisaile. Admonish ; sec Monition. A-do, 10 dc, oablc. (E.) M. E. to do; a Norlhcru idiom, whereby used as the sign of the infiu. mt Iccl., Swedish, &c. See Do < (). Adoleaoent; see Aliment. Adopt; see Optative. Ador
--- [ffpage 571] . to carry un, rule ; see Oesture. % So also viie- admiral, vitt-roy (from F. rci, L. rtgem, Iting), vite-regai, vioisaitude. (L.) L. uicisiUuHo, change. Allied to nicissim^ by turns. — I,. «fU'-fi (genitive), a change. viscount. (F. - L.) The nsual old spelling was vicetmtt (and the t is not pro- nounced even at this day).— F. vicomUy 'a vicount, at 6rst the deputy of an earl ; * Col. O. F. visccmte (i ath cent.). — L. uit^e, in place of : ccmiitm, ace. of (&nt4s, a count ; sec Cc
###SKT alcohol
--- [ffpage 640] {but uUiniatelje Greek), French from Arabic: admiral, alcohol, assassin, barberry (berberry), bedouin, calif (caliph), cipher, civet, fardel?, furl?, ga- zelle, lute (1), Mamaloke (Mameluke), mattress, mohair (moiic), saflron, sultaa. Persian from Arabic, mussulmati. Frenek from Flerrian from Arabic ; mate (3). Turkish from Arabic: coffee, giaoar. HinJi from Arabic ; nabob. Italian from Malay from Arabic soon. of ASUTIC origin, bat NEITHER ARYAN NOR SEMITIC h anna, bangle, cowry, sham Idy. Italian from
```


## [2026-09-04T19:32:21.639Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###KLN as-sumut/azimuth\"; python3 $S KLN_1966.txt 'as-sum|assumut|sumut|zenith, n' 600 4\necho \"###KLN chemist\"; python3 $S KLN_1966.txt 'chemist, n' 600 2\necho \"###KLN lute al-ud\"; python3 $S KLN_1966.txt \"al-'?[ou]ud|al-ʻ?ud|OProven.{0,3} la.d\" 500 6"
}
```


## [2026-09-04T19:32:23.585Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###KLN71 azimuth\"; python3 $S KLN_1971.txt 'azimuth' 600 3\necho \"###KLN71 lute\"; python3 $S KLN_1971.txt 'lute, n' 600 3\necho \"###KLN71 Allah\"; python3 $S KLN_1971.txt 'Allah' 400 4"
}
```


### [2026-09-04T19:32:24.938Z] TOOL RESULT

```
###KLN as-sumut/azimuth
--- [ffpage 83] the meridian ( astron .) — F. azi- mut, fr. Arab. as-sumBt, pi. of as-samt, ‘the way’, fr. as-, assimilated form of al-, ‘the’, and saint, ‘way’. See zenith and cp. altazimuth. azo-, before a vowel az-, combining form de¬ noting the presence of nitrogen ( client .) — Short¬ ened fr. azote (q.v.) Cp. diazo-, thiazine. azoic, adj., without life. — Formed with suff. -ic fr. Gk. aCcooc, ‘without life’, fr. a- (see priv. pref. a-) and qo>f„ ‘life’. See zoo- and cp. azote. Azolla, n., a genus of plants of the salvinia family (bot.) — ModL., compounded of Gk. oiTetv, ‘to d
###KLN chemist
NO MATCH KLN_1966.txt chemist, n
###KLN lute al-ud
NO MATCH KLN_1966.txt al-'?[ou]ud|al-ʻ?ud|OProven.{0,3} la.d
```


### [2026-09-04T19:32:26.867Z] TOOL RESULT

```
###KLN71 azimuth
--- [ffpage 0] cp. a-, ‘away from’, apo-, post-. aba, n., a form of altazimuth instrument. — So called after its inventor Antoine Thomson d 'Abbadie. aback, adv. — OE. on bsec. See a-, ‘on’, and back, abacus, n., 1) frame with beads for calculation; 2) ( archit .) slab at the top of a column. — L. abacus, fr. Gk. gen. aflaxoc;, ‘a square tablet strewn with dust’, fr. Heb. abhdq , ‘dust*, fr. root a-b-q, ‘to fly off’. The first type of abacus was a board covered with dust, whence its name. Abaddon, n., the bottomless pit. — Heb. dbhad - dSn, ‘destruction’, fr. abhadh, ‘he perished’, which is rel. to Aram, tibhddh, ‘he perished’, Ugar. ’ bd , ‘to per
--- [ffpage 0] alter, outer (F. autel). Derivative: altar-ed , adj. altazimuth, n., an instrument for observing the altitude and azimuth of a star (astron) — Com- pounded of the abbreviation of altitude and of azimuth. alter, tr. and intr. v. — F. alterer , fr. Late L. al- ter are, ‘to change’, fr. L. alter, ‘the other (of two)’, which stands for *aliteros, *alitros, *altros, and is formed with the compar. suff. -ter fr. base *ali- y ‘there, beyond’, whence also alius , ‘an- other’. Hence alter and alius lit. denote ‘one who stands there’ ; the former — in keeping with the sense of the compar. suff. -ter— denotes ‘the other of two’, the latter mea
--- [ffpage 0] tazimuth, n., an instrument for observing the altitude and azimuth of a star (astron) — Com- pounded of the abbreviation of altitude and of azimuth. alter, tr. and intr. v. — F. alterer , fr. Late L. al- ter are, ‘to change’, fr. L. alter, ‘the other (of two)’, which stands for *aliteros, *alitros, *altros, and is formed with the compar. suff. -ter fr. base *ali- y ‘there, beyond’, whence also alius , ‘an- other’. Hence alter and alius lit. denote ‘one who stands there’ ; the former — in keeping with the sense of the compar. suff. -ter— denotes ‘the other of two’, the latter means ‘another picked out of many (at least three) persons’.
###KLN71 lute
--- [ffpage 0] ‘to call’, from vdx, gen. vdcis , ‘voice’. See voice, evolute, n., a curve which is the locus of the cen- ter of curvatures of another curve ( geom .) — L. ivolutus, pp. of evolvere. See next word and cp. involute. evolution, n. — L. ivolutid , gen. -onis, ‘an un- rolling (of a scroll), an opening (of a book)’, fr. ivolutus , pp. of ivoivere, ‘to unroll, unfold’, fr. e- and volvere, ‘to roll’. See volute and cp. words there referred to. Derivatives: evolution-al, adj., evolution-al-ly, adv., evolution-ary , adj., evolutionism (q.v.), evolutionist (q.v.) evolutionism, n., the theory of evolution. — Formed with suff. -ism fr. L. ivolut
--- [ffpage 0] lugs-tra and derives fr. fluere, ‘to flow’. See fluent. flute, n. — ME. floute , floite, fr. OF. flaiite , fleiite (F. flute), fr. OProven9. flaiit , which is prob. a blend of OProven q.flaujol, ‘flageolet’, and laiit , ‘lute’. See flageolet and lute, ‘a musical in- strument’. It .flauto and Sp./fawtaareOProveng. loan words. Cp. flout. flute, intr. v. — ME. flouten, floiten, fr. OF. flaii- ter, fleiiter (F. fluter), fr. OF. flaiite , fleiiie, ‘flute’. See flute, n. Derivatives: flut-ed , adj., flutter, n., flut-ing, n., flut-y , adj. flutist, n. — A hybrid coined fr. flute and -ist, a suff. of Greek origin. Cp. flautist, flutter, int
--- [ffpage 0] iter (F. fluter), fr. OF. flaiite , fleiiie, ‘flute’. See flute, n. Derivatives: flut-ed , adj., flutter, n., flut-ing, n., flut-y , adj. flutist, n. — A hybrid coined fr. flute and -ist, a suff. of Greek origin. Cp. flautist, flutter, intr. v., to flap the wings; tr. v., to move quickly. — ME. floteren, fr. OE. floterian, ‘to be tossed by waves, to flutter’, freq. of flotian, ‘to float’. See float, v. Derivatives: flutter , n., flutter-er, n., fluttering, adj., flutter-ing-ly, adv., flutter-y , adj. fluvial, adj., pertaining to a river. — L. fluvialis, fr. fluvius , ‘river’, which is rel. to fluere , ‘to flow’. See fluent and adj. suf
###KLN71 Allah
--- [ffpage 0] s there referred to. Cp. also agio, diallage, hypallage. Allah, n.-, Mohammedan name of the Supreme Being. — Arab. AUdhu, contraction of al-lldhu , fr. al-, ‘the’, and Ildh. ‘God’. See Eiohim. allanto-, combining form meaning ‘sausage’. — Gk. dXXavro-, fr. dXXas, gen. <£XXavro<;, ‘sau- sage’, a loan word fr. L. dlium, allium , ‘gar- lic’, the orig. meaning of Gk. AXXot? being ‘garlicky (sausage)’. Ion. &XXtj, glossed by He- sychius, and rendered
--- [ffpage 0] , members of a Mohammedan sect, founded by Mohammed ibn Abdallah. — Lit. ‘the Unitarians’ ; shortened fT*Al-movahides, from Arab, al-muwahhidun, ‘they who profess the unity of God’, fr. al-, ‘the’, and active part, of the 2nd conjugation of wdhuda, ‘he was alone’ whence also wafifd, ‘solitary’ ; rel. to Heb. ydhtd, ‘only one, solitary’, yahad, yahddw, ‘together’, almond, n. — ME., fr. OF. almande (F. amande ), fr. VL. amandula , fr. L. amygdala, f
--- [ffpage 0] the church for charity and) opened on Christmas day. boxwallah, n., a native peddlar in India (Anglo- Ind.) — Hind, bakaswata, a hybrid coined fr. bakas = English box, ‘case’, and Hind. suff. -wald; see wallah. For sense development cp. Scot, packman , ‘peddlar’. boy, n. — ME. boi, rel. to the OE. PN. Bofa, OFris. boy, ‘a young gentleman’, MDu. boeve, Du. boef \ ‘knave, villain’, the OHG. PN. Buobo , MHG. buobe , G. Bube, ‘boy’, and in vowel gr
--- [ffpage 0] bakas = English box, ‘case’, and Hind. suff. -wald; see wallah. For sense development cp. Scot, packman , ‘peddlar’. boy, n. — ME. boi, rel. to the OE. PN. Bofa, OFris. boy, ‘a young gentleman’, MDu. boeve, Du. boef \ ‘knave, villain’, the OHG. PN. Buobo , MHG. buobe , G. Bube, ‘boy’, and in vowel gradational relationship to E. babe, baby (qq.v) Derivatives : boy, tr. and intr. v., boy-hood, n., boy-ish, adj., boy-ish-ly, adv., boy-ish-ness, n
```


## [2026-09-04T19:32:36.764Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###KLN71 lute stringed\"; python3 $S KLN_1971.txt \"lute,? n\\.,? [a-z ]{0,20}string|stringed instrument.{0,120}\" 450 6\necho \"### KLN71 chemistry\"; python3 $S KLN_1971.txt \"chemistry, n\" 500 3\necho \"### KLN66 chemistry\"; python3 $S KLN_1966.txt \"chemistry\" 400 4"
}
```


### [2026-09-04T19:32:38.789Z] TOOL RESULT

```
###KLN71 lute stringed
--- [ffpage 0] equivalent to Gk. -oq, see -ous. asor, n., a Hebrew ten-stringed instrument. — Heb. *ds 6 r, fr. ‘eser (masc.), 'dsard* (fem.), ‘ten’, which i * rel. to Aram. *dsdr (masc.), 'asra (fem.), Ugar. ‘shr (masc.), 'shrh (fem.), Arab. 'ashr (masc.), i dskara h (fem,), Ethiop. *askru (masc.), ‘ ashartu (fem.), Akkad, eshri (masc.), eskertu, esherit (fem.), ‘ten’. (The masc. forms are used with fem. nouns, the fem. ones with masc. nouns.) In the Sem. lan- guages the orig. meaning of ‘ten* seems to ha
--- [ffpage 0] bove’, and Hind, ghat , ‘a pass’, balalaika, n., a Russian stringed instrument with a triangular body. — Russ, balalaika , which, according to Erich Bemeker, Etymologisches Wbrterbuch der russischen Sprache, I, p.40, Heidelberg, 1908-13, is rel. to Russ, balabdlit \ ‘to chatter, babble’, from the I.-E. imitative base *balb-, whence also L. balbus, ‘stammering’. See booby and cp. words there referred to. balan-, form of balano- before a vowel, balance, n. — OF. (= F.) balance, fr. L. bi ‘two, tw
--- [ffpage 0] re- sembling a crow's beak’, crowd, n., an ancient Celtic stringed instrument. — ME, crowde, fr. W. crwth , ‘anything swelling, bulging’, which is rel. to OIr. crot , ‘harp’, Gael. cruit, ‘harp, violin’, Ir. cruit, ‘violin’, and to OW. crunn, Gael, cruinn, ‘round, curved’. See crown, n., and cp. rote, ‘a musical instrument’. crowd, intr. and tr. v., to press. — ME. cruden , crouden, fr. OE. crucian, ‘to press, push’, rel. to MDu. cruden, later kruyden, kruyen, Du. kruien, ‘to push’, MHG. krot
--- [ffpage 0] ikes 5 , Gk. ^aXXsw, ‘to pluck, twitch the harp, play on a stringed instrument’, t^aX^a, ‘tune played on a musical instrument’, ^aX^o?, ‘a plucking, twitching of the harp’, later ‘song, psalm’, 4 ^tz}P« ‘harper’, ^aXnfjpiov, ‘stringed instrument, harp’, <fwcX[i.(p8ca, ‘a singing to the harp’, ‘I feel or grope about’ (com- pounded of *^aXa, ‘a twitching’, and a<pa<o, ‘I touch’), L. palpdre , ‘to touch softly, stroke’, pal - pitdre , ‘to move quickly’, palpebra, ‘eyelid’, lit. ‘that which moves q
--- [ffpage 0] ). These words probably derive fr. VL. vitula , name of a stringed instrument, which is of uncertain origin. It is possibly a back formation fr. L. vitulari, ‘to exult, be joyful*, which prob. stands for vi-tuldri and orig. meant ‘to lift up one’s voice in joy’, fr. *w, exclamation of joy (cp. Gk. euo l, exclamation used in the cult of Dio- nysus) and tula, a secondary form of to lid, ‘I raise’. See tolerate and cp. words there referred to. Cp. also viol. Derivatives: fiddle, v. , fiddler (q.v
--- [ffpage 0] pe’. Fidibus is the pi. ablative of L. fides, ‘gut string, stringed instrument, lyre’, which is cogn. with Gk. (Hesy chius), ‘sausage’. The word fidibus was introduced into English by the American poet Henry Wadsworth Long- fellow (1807-82) in 1829. fiducial, adj., 1) based on faith; 2) like a trust. — L. fiducialis, ‘reliable’, fr. fiducia, ‘trust, faith’, ir.fidere, ‘to trust’. Sec fidelity and adj. suff. -al. fiduciary, adj., 1) of a trustee; 2) held in trust; n., a trustee. — L. fiduciarius
### KLN71 chemistry
--- [ffpage 0] obiotic, ne- crobiosis, Rhizobium, symbion, symbiosis, biochemistry, n., chemistry dealing with animal and plant life. — See bio- and chemistry, biogen, n., a protoplasmic unit (biol.) — Coined by the German physiologist Max Verworn (1863-1921) in 1903 fr. bio- and -gen. biogenesis, n., the theory that living organisms can only arise from pre-existing living matter (biol.) — Coined by the English biologistThomas Henry Huxley (1825-95) in 1870 fr. Gk. pto;, ‘life’, and y^veaiq, ‘origin, source’. See bio- and genesis and cp. abiogenesis. bioge
--- [ffpage 0] entr-al, metacentr-ic , adjs., metacentr-ic-ity , n. metachemistry, n., higher chemistry. — Formed fr. meta- and chemistry. metachromatism, n., change of color (esp. due to a change in temperature). — Formed fr. meta- and Gk. xp&pcx, ‘color’. See chrome and -ism. metachronism, n., an error in chronology consist- ing in placing an event after its real date. — ML. metachronismus, irregularly formed fr. Gk. pExaxpovo?, pexaxp6vio?, ‘after the time, done afterward’, fr. pexa- (see meta-) and XP^vo?, Fractidor, Thermidor. messieurs, n., pi. of
--- [ffpage 0] ic. — See prec. word and -y (representing Gk. -la). microchemistry, n., that branch of chemistry which deals with microscopicrobjects or quanti- ties. — Compounded of micro- and chemistry, microcline, n., a kind of feldspar belonging to the triclinic system (mineral.) — Compounded of micro- and Gk. xXfveiv, ‘to incline’. See clinical, microcosm, n., a miniature world. — F. micro- cosme , fr. Late L. microcosmus, fr. Gk. puxp6<; x6ct(jloi;, ‘little world’. See micro- and cosmos and cp. macrocosm. Derivatives : microcosm-ic, microcosm-ic-al ,
### KLN66 chemistry
--- [ffpage 4] atures of this dictionary: What the elements are to chemistry, what the sounds are to music, are words to language. However, words are not only the elements of a language but also of the history of the people speaking it. They are important milestones along the way leading to the majestic Palace of Human Knowledge. One of the basic features of this dictionary is that — in contradistinction to
--- [ffpage 5] logy, geography, geology, history, astronomy, physics, chemistry, mathematics, grammar, p 1 o- sophy. The entries treating these branches of science in this dictionary, virtually contain the most important phases of their history. Two other characteristic features of this dictionary: HYBRID WORDS Scientists are rarely also linguists. This is why many scientific terms are inexactly coined and often erroneous
--- [ffpage 9] 956 — in progress. J. R. Partington, The History of Chemistry, London, 1961-62. Skeat, W. W., An Etymological Dictionary of the English Language, New Edition, Oxfor , 1946. Skinner, Henry Alan, The Origin of Medical Terms, 2nd ed., Baltimore, 1961. Weekley, E., A Concise Etymological Dictionary of Modern English, 2nd ed., 1952. Yule, H., and A. C. Burnell, Hobson-Jobson, revised by Crooke, 1903. abl. a
--- [ffpage 9] Celtic Akkad. Akkadian cent. century AL. Anglo-Latin chem. chemistry; chemical Alb. Albanian Chin. Chinese alg. algebra chronol. chronology alt. alteration class. classical Am. American Co. Cornish an at. anatomy cogn. cognate Anglo-Ind. Anglo-Indian coll. collective, collectively Annam. Annamese colloq. colloquial, colloquially anthropol. anthropology compar. comparative anthropom. anthropometry conj. conjunction antiq antiquity Copt. Coptic aor. aor
```


## [2026-09-04T19:32:47.948Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###LKT sample head\"; head -c 1500 LKT.txt\necho; echo \"###LKT ud/laute\"; python3 $S LKT.txt \"Laute|luth\\b\" 400 5"
}
```


### [2026-09-04T19:32:49.703Z] TOOL RESULT

```
###LKT sample head
SE  PROHIBE
Subroyar  y/o  morginar  este  libfOf te  cojo  de  devclverlo  subrayado« SE  COBRARA  SU  VALOR
INDOGERMANISCHE  BIBLIOTHEK
HERAUSGEGEBEN  VON H.  HIRT  UND  W.  STREITBERG  t
ERSTE  ABTEILUNG
SAMMLUNG  INDOGERMANISCHER  LEHR- UND  HANDBÜCHER
II.  REIHE:  WÖRTERBÜCHER DRITTER  BAND
ETYMOLOGISCHES  WÖRTERBUCH  DER EUROPÄISCHEN  WÖRTER  ORIENTALISCHEN URSPRUNGS
VON
KARL  LOKOTSCH
HEIDELBERG  1927 CARL  WINTER'S  UNIVERSITÄTSBUCHHANDLUNG
I
ETYMOLOGISCHES WÖRTERBUCH
DER  EUROPÄISCHEN  (germanischen,
ROMANISCHEN  UND  SLAVISCHEN)  WÖRTER
HEIDELBERG  1927
CARL  WINTER'S  UNIVERSITÄTSBUCHHANDLUNG
Verlags-Nr.  1988.
AUa  Utobt«,  beioDden  dai  Reolit  der  Oberaetzuug  lo  tremdi  Spntoheo, werden  vorbehalteu
014139
Dem  Ni'slor  der  ilciilsrlicii  Orientalisten
Herrn  Prof.  Dr.  Theodor  Nöldeke
~ii  seinem  iieinr;iosten  Gehurtsjcste in  (Idnklhirer  Verehrnng i^eiuidmet
2.  M(U  ~  11)26.
Digitized  by  the  Internet  Archive in  2014
/
https://archive.org/details/etymologischeOOIokoguat
Vorwort.
Das  etymologische  Wörterbuch  der  europäischen  Wörter  urieulaHschen Ursprungs  verdankt  seine  erste  Anregung  dem  häufig  ausgesprochenen Wunsche  meiner  Hörer  an  der  Kölner  Handelshochschule  und  Universität, die  Hinweise  auf  das  Weiterleben  orientalischer  Grundwörter  in  den  ver- schiedenen europäischen  Sprachen,  die  ich  in  meinen  Vorlesungen  und Übungen  zahlreich  zu  geben  pflegte,  in  einer  gedruc
###LKT ud/laute
--- [ffpage 43] 7. [Gorjajew 9 u. 10. ML 890. 198. Tat. balaliiika: 'Laute' ; hieraus russ. h
--- [ffpage 44] balalajka, öech. bala- lajka 'russische Zither oder Laute mit zwei oder drei Saiten' ; frz. la balale'ika, dtsch. Balalaika. [Gorjajew 10. 199. Mongrol. balamnt: Hieraus russ. balamut, öech. balanmt, poln. balamut 'Schwätzer, Klatsch er' ; Tum. balamut 'dumm'. Dazu auch Verba: russ. balamutit' , Cech. balamutiti, poln. balamucic und mit Abstoßung der ersten Silben: bulg. mUja, serb. mutiti 'verwirren, trüben
--- [ffpage 45] ört [obwohl der Bantu-Name dafür bi-tebbe oder ähnhch lautet] und um die Mitte des 16. Jahrhunderts nach Europa ge- bracht; sp. pg. banana, it. banano, rum. bananä, frz. banane 'Pisangfrucht', ba- nanier 'Pisangbaum', ndl. banaan, engl. banana, dtsch. Banane, russ. banan. — Nach einem Vorschlage von HÜMMEL, soll Banane von babyl. banu 'süß schmek- ken, gut sein' [wohl banu II, 1) bei Del HWB 180 a] komm
--- [ffpage 55] Lakritze', vulgär gesprochen mit Dissi- milation der anlautenden Labiale mijan baly, mijambaly; liieraus rum. tniambnl 'Lakritzwasser'. [Löbel EITAP 63. 345. Tk. bujrak: 'Kluff [nicht osm., Stamm bök, boj 'biegen, wenden' Vämbery TktEtWb S. 210, Nr. 227]; hieraus russ. bugrak, klruss. bairak 'Erdkluft'. [Gorjajew 32. 346. Tk. bujur-: Bujurmak 'befehlen, geruhen', imper. bujur, bujurua 'belieben Sie!', 'Bitte!'
--- [ffpage 58] 'große Schüs- sel. Teller'. 39-2. Fers, cäng: 'Harfe, Laute', ar. nang 'pers. Harfe, Leier' [KM II. 1161, 3]; hieraus mit ar. Art. Asangue 'Sternbild der Leier, Lyra'. [Devic DEt 41. 392 a. Pers. cäng'äl: 'Haken', tk. ebenso cengel; hieraus rum. cinghiel 'Wandhaken'. 393. Np. cäiitä: 'Sack', besonders aus Leder oder Lein- Avand; er hängt am Sattel, und in ihn wird die Wasserpfeife hineingesteckt, vkI. ZDMG
```


## [2026-09-04T19:32:50.096Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###DEV luth\"; python3 $S DEV.txt \"LUTH|luth\\b\" 500 3\necho \"###PHN luth\"; python3 $S PHN.txt \"LUTH|Luth\" 500 3\necho \"###DEV alcool\"; python3 $S DEV.txt \"ALCOOL|alcool\" 400 3\necho \"###DEV arsenic\"; python3 $S DEV.txt \"ARSENIC|arsenic\" 500 3"
}
```


### [2026-09-04T19:32:51.792Z] TOOL RESULT

```
###DEV luth
--- [ffpage 68] une altération du ^qy- sdLXi 3^j^=s^ tcheng , harpe, luth. i6. Aschémie, l'étoile Procyon; en arabe, ^^UJi ach- clulmi, le Syrien, ^^UJI <.^yt*«Ji ach-chtra ach-cltâml, Sirius de Syrie. (Voy. Aliémini, ci-dessus.) L'e final de aschémie montre que le mot a été fait sur le féminin <XA-«UiJi ach- châmia. 17. Aschère, Sirius. C'est l'arabe <^*x*iJi ach-ckira, qui repr�
--- [ffpage 287] IK. Laranja, pg. voy. Orange. Lascar. Laud, esp. vov. Luth. Lazarino , ital. voy. Azerolle. Lazuli (Lapis-), voy. Azur. Lazulum, b. lat. voy. Azur. Lazur, b. lat. voy. Azur. Lazurius, b. lat. voy. Azur. Lazzarolo, ital. voy. Azerolle. Lazzeruola, ital. voy. Azerolle. Lebbeck. LeUlies, esp. voy. Hallali. Léviathan. \iSdvos, voy. Oliban. ^Lilac, esp. voy. Lilas. LiLAS. Lilazaro , pg-. voy. Lilas. Lima, hisp. voy. Limon. Limâo, pg. voy. Limon. Lime, voy. Limon. Limon. Limone, ital. voy. Limon. Liquidambar,
--- [ffpage 287] mon. Liquidambar, voy. Ambre. LiSME. Liuto, ital. voy. Luth. LoG. Lontarus, lat. bot. voy. Lantard. LoocH. LoRi. Luth. Macabes>, esp. voy. Macabre. Macabre (Danse). Macaleb, voy. Mahaleb. Macalep, voy. Mahaleb. Mâche. Macholeb, voy. Mahaleb. Madrague. Magacen, esp. voy. Magasin. Magasin. Magazzino, ital. voy. Magasin. Magreb, voy. Garbin. Mahaleb. Mahari. Maharram, voy. Moharrem. Mauométan. Mahona, esp. voy. Mahonne. t t I IMDEX DES MOTS EUROPEENS. 253 Mauonne. Maidan, voy. Méidan. Maihari, voy. Maliari. Mail , voy
###PHN luth
--- [ffpage 271] ques dictionnaires géographiques offrent la variante Luxor. LUTH, s. m. (a.) jyJI [a/^ou^] le bois en général , et en particulier le bois d'aloès. Nom d'un instrument de musique à cordes , abandonné depuis longtemps, — La transcription luth est tellement corrompue, qu'il paraît assez difficile, au premier coup d'œil, d'y recon- naître quelque affinité avec le mot oriental; mais on y parvient^ soit à l'aide de l'espagnol laud, soit au moyen du portugais alaude, dans lequel l'article al figure intégralement. Le même instrument s'appelle leuto ou liuto chez
--- [ffpage 271] e à cordes , abandonné depuis longtemps, — La transcription luth est tellement corrompue, qu'il paraît assez difficile, au premier coup d'œil, d'y recon- naître quelque affinité avec le mot oriental; mais on y parvient^ soit à l'aide de l'espagnol laud, soit au moyen du portugais alaude, dans lequel l'article al figure intégralement. Le même instrument s'appelle leuto ou liuto chez les Italiens, et lute chez les Anglais.
--- [ffpage 422] .-t.) sSg Lippe, s. f. (p.) a3g Look et Lok, s. m. (a.) 939 Luth, s. m. (a.) .« aAo M Macabre, adj. f. (a.) ùbt Madrague, s. f. (a.) ait Magasin, s. m. (a) a^a Mage, s. m. (p.) < a43 Maghreb, s. m. (a.) — Maghrébin, e, adj a43 Mahmil , s. ni. (a.) qAA Mahmoud, n. pr. (a.) — Mahmoudi, s. m 9^4 Mahomet, n. pr. (a.) — Mohammed, Méhëmed, Méhémet, n. pr. 9&5 Maïmon, s. m. (t.) 967 Malëkite, s. m. (a.) 967 Mamiouk, s. m. (a.) 9A7 Manne, s. f. (a.) 948 Mantil, s. m. (a.) t- Mantille, s. f. 9/19 Maquereau , elle, subst. (a.) 9(9
###DEV alcool
--- [ffpage 39] b, ziibd, zcIhJ, beurre, de Jo^ zoiibd, rneme sens. Alcool. Esp. et portug. alcohol, aragon. alcofol^, catal. (ilcofoIJ. 11 est bien démontré que l'étymologie de ce mot est l'arabe J^=5^î nl-kohl, le cobeul ou poudre d'antimoine'^, dont les femmes, en Orient, se teignent les paupières. On sait que ce mot a été employé à désigner un grand nombre de collyres divers, tels que yX^\ JA^, y^s] J^, y/yS.
--- [ffpage 54] V Algérie, p. 29 (dans le GJoss. de Do/y, au mot alcool, p. 92 ). M. Dozy n'a [)as nolo le Icime alqiiijhl. 28 DICTIONNAIRE ÉTYMOLOGIQUE tilloii ([ue j'ai apporté. C'est à tort que plusieurs auteurs ont traduit le mot cohol par antimoine. •)•> Alquifoux est donc u
--- [ffpage 55] les intermédiaires aholiol, alcofol, alquifol. (Voy. Alcool.) Altaïr. Etoile de première grandeur, a de la constel- lation de l'Aigle. De l'arabe >r>ikJî al-iair, qui vole. On prononce ai-lâiv, aussi trouve-t-on quelquefois cliez nos auteurs atdir ou athaïr. La conservation de / peut être due à la prononciation emphatique du i^ /. Cazwini dit que la constellation de l'Aigle c->U*Jî <x>^^ comprend quinz
###DEV arsenic
--- [ffpage 37] ermhh, qui est le même mot que le grec àpcreviKos, arsenic jaune, orpi- ment. 3o. Azazeze, verre, de ^^==»-J^ az-zadjàdj, même sens. 3 1 . Azeg, vitriol , esp. aceclic, aciche, acige; port, azeche, de ^Uî az-zâdj , même sens. ' Le même mot se retrouve dans l'expression hlanc rasis , bianc de plomb : "Le plomb aussi qui est noir, quand il est calciné par la vapeur salsilive du vinaigre, il se réduit en blanc de plomb, dequoy la cérusc est faite, et blanc rasis, cjui est la plus
--- [ffpage 225] , littéralement poudre de caverne, nom que portait l'arsenic chez les Arabes du Maghreb ^. Rebec. Instrument de musique de la famille du violon. Vieux franc, rehebe, esp. rahel, portug. rabel, rabil, arrabil, rahem, rebeca, ital. ribeca, ribeba. De l'arabe cjIj^ rabâb, ioLj rabâba, même signification^. Il ne faut pas oublier que la dernière consonne arabe mal entendue par l'oreille est souvent altérée en passant dans les langues euro- péennes. Quant au ch
```


## [2026-09-04T19:33:19.882Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\nfor p in 'fisfisa|fasfasa|Luzerne' 'zarnik|zernik|Auripigment' 'malgam|Amalgam' 'qili|kili.*Aschen|Alkali' 'barquq|Aprikose' 'qubba|Alkoven' 'qadus|Albatros' 'anbiq|Alambik|Alembik' 'badingan|Aubergine' 'iksir|Elixier' 'kimija|Alchimie|Chemie' ; do echo \"###LKT $p\"; python3 $S LKT.txt \"$p\" 400 2; done"
}
```


### [2026-09-04T19:33:22.386Z] TOOL RESULT

```
###LKT fisfisa|fasfasa|Luzerne
--- [ffpage 74] ancio Dice 49 b und c. Dl-: 112. 59S. Ar. fasfasu: 'Luzerne Medicag-o sativa L.', auch fis- fifa; hieraus sp. alfalfa, alfafe 'dass., spanischer Klee, foenum Burgundiacum', engl, amerik. alfalfa. [DE 100/101. Eguilaz 156. ML 4002 Anm. 599. Ar. fasha: 'Leerer, weiter Raum'; hieraus mit ar. Art. sp. alfeiza 'Tür- oder Fenster- öffnung'. [DE 112. 600. Ar. falil: 'Gedreht; Docht', ebenso ik.fitil 'Docht': hie
--- [ffpage 210] äh 59 a darbfhänaj 489 /«'s 597 iiwä' 309 darmaka 494 fasfasa 598 fcirfca 312 darünag 486 /"aNÄ« 599 bitäna 316 dasJsa 497 fr» ^(2 602 bittiha 319 d^'M 504 fatalta 916 bizzäf 320 d"MA; 2212 600 6fe 892 daur 501 /ai/a 601 buhür 343 datiu'&r 502 fattäta 601 ftwl; 347 däwa 504 fa^M'ä 602. 1493 bunduk 355 da'^wa .505 faicwära 585 büränija 358 d''6 513 /■jfc/i 572 6ur(i 360 dj/7ä 515 6U5 ÖMrp' 362 dijäta 516 A/ö^t 606 bur
###LKT zarnik|zernik|Auripigment
NO MATCH LKT.txt zarnik|zernik|Auripigment
###LKT malgam|Amalgam
--- [ffpage 137] gr. |id\aY|ua mit Metathesis]; hieraus sp. pg. kat. amalgama, frz. amalgame; engl, aniaf- gam, Vb. amalgamate, dtsch. Amalgam, Vb. amalgamieren; russ. amal'gama [und über tk. melhem, ebenso tat.] mal - han, bulg. mehlem, serb. meiern 'Saloe'. — [Devic DEt 29/30 und Eguilaz 256/257 geben andere unhaltbare Ableitungen, Lammens Rem 21/22 spricht schon Zweifel daran aus; die hier gegebene Etymologie deutetschon
--- [ffpage 137] mit Metathesis]; hieraus sp. pg. kat. amalgama, frz. amalgame; engl, aniaf- gam, Vb. amalgamate, dtsch. Amalgam, Vb. amalgamieren; russ. amal'gama [und über tk. melhem, ebenso tat.] mal - han, bulg. mehlem, serb. meiern 'Saloe'. — [Devic DEt 29/30 und Eguilaz 256/257 geben andere unhaltbare Ableitungen, Lammens Rem 21/22 spricht schon Zweifel daran aus; die hier gegebene Etymologie deutetschonGorjajew201 an].
###LKT qili|kili.*Aschen|Alkali
--- [ffpage 110] ou 'Asche aus den Reb- stöcken', engl, alhdi, dtsch. Alkali usw. Auch der Namen des Elementes Kalium, Calium gehört hierhin, [Devic DEt 7. Lammens Rem 7. 1030. Ar. kälib: 'Leisten eines Schusters', ebenso tk. kalyh, Icahjp 'Modell, Form'; hieraus rum. calib, calip, calup 'Gießform, Mo- dell, Leiste', calupciü 'Betrüger'; aus dem Ar. unmittelbar sp. gälibo 'Schiffs- modell', frz. gabarit; asp. calibo, sp. calib
###LKT barquq|Aprikose
--- [ffpage 47] übrigens die Bedeutung 'Pflaume' erhalten, während die Aprikose mismas (s. hier Nr. 1471) heißt]; hieraus sp. albaricoque, alber- coque, pg. albricoqtie, alboquorque, prov. aubricot, frz. abricot, it. albicocco, al- bercocco, siz. varcoccu; engl, apricot. 21 [Ar. barnija. ndl. abrikoos, dtsch. Aprikose, schwed. aprikos; russ. abrikos, öech. aprikozn. — Ferner infolge Betonung der ersten Silbe mit romanischem Suf
--- [ffpage 47] engl, apricot. 21 [Ar. barnija. ndl. abrikoos, dtsch. Aprikose, schwed. aprikos; russ. abrikos, öech. aprikozn. — Ferner infolge Betonung der ersten Silbe mit romanischem Suffix sp. cilber- chigo, it. albergese 'Art Pfirsich oder Aprikose' [dagegen DEFREMERY in JAs (1869) I, 531, wohl ohne Grund]. [Dozy Oost 1—4. DE 67/68. Hobson- Jobson 33. Devic DEt 2/3. ML 6712. Kluge 20. 248. Ar. barnija: Topf, Krug au
###LKT qubba|Alkoven
--- [ffpage 91] Bogen, Gewölbe'; hieraus mit ar. Art. sp. alhania 'Alkoven, Nische zum Schlafen' [wie bereits in den ar. Häusern Spaniens, vgl. Graf Schack, Poesie und Kunst in Spanien und Sizilieu. II, 324, wo allerdings das dort ge- nannte Alhamia mit m ein Irrtum sein muß]. — [DE 135. 816. Ar. hanzal: 'Koloquinte', Frucht von CitruUus colo- cynlhis; hieraus mit ar. Art. sp. frz. alhandal pharmazeutischer Name der K
--- [ffpage 125] cher Demin.-Endung it. ctipola, frz. coiipole. Dtsch. Alkoven, Ktqypel, mhd. ekub 'Zelt' [bei WOLFRAM VON ESCHENBACH], ndl. alkoof, engl, alcove 'Zimmervvinkei für Sitz oder Bett' [m einem Zimmer oder einer Bibliothek].. Bulg. kube, serb. kube, kuba 'Kuppel, Gewölbe', russ. alkow 'Alkoven'; über vulg. ar. kiibbat, kas.-tat. kibbet, kirgis. kibü wurde russ. kibitka 'Verdeck über einem russ. Wagen, halbverdeckte
###LKT qadus|Albatros
--- [ffpage 106] ung'. Aus dem pg. alcadroz entwickelte sich angloind. albatross, engl, albatros, albatross, frz. albatros, sp. alcatraz, dtsch. Albatros 'Diomeda exulans L.', ein großer Seevogel aus der Familie der Sturmvögel, nach der Gestalt seines Schnabels so benannt [dagegen : Eguilaz 225 und Lammens Rem 5]. — Der plr. des ar. Grundworts ist kawädts 'Röhren'; hieraus mit ar. Art. sp. alcaraviz, pg. alcribis 'Eisenrohr,
--- [ffpage 106] alcadroz entwickelte sich angloind. albatross, engl, albatros, albatross, frz. albatros, sp. alcatraz, dtsch. Albatros 'Diomeda exulans L.', ein großer Seevogel aus der Familie der Sturmvögel, nach der Gestalt seines Schnabels so benannt [dagegen : Eguilaz 225 und Lammens Rem 5]. — Der plr. des ar. Grundworts ist kawädts 'Röhren'; hieraus mit ar. Art. sp. alcaraviz, pg. alcribis 'Eisenrohr, mit dem die Sc
###LKT anbiq|Alambik|Alembik
NO MATCH LKT.txt anbiq|Alambik|Alembik
###LKT badingan|Aubergine
--- [ffpage 41] . berengena, pg. berin- gala, kat. alberginera, frz. aubergine, melanghne, merangene, it. melangola, marignano, melanzana, siz. milinciana. Über vulg. tk. ■paüygan wurde rum. pätlägea, demin. pätlägicä 'Tomate'. Russ. badidzan, badarzan, batlamn, baklazan. [DE 239. Eguilaz 344. De- vic DEt 46/47. ML 876. Löbel EITAP 75. 162. Pers. bädjäu: 'Anis'. Hieraus sp. badian, badiana, pg. badiana 'chinesischer Slernanis',
--- [ffpage 228] e 2208 »thanor 2019 a^fcar 2075 a«a6a? 1971 ffM&^e 874 aubergine 161 «MCTtöe afz. 1221 uufage afz. 586. 777 auferrant afz. 586 aw/fe 796 au^n afz. 605 auforget 884 «M^r^ 135 aumasor afz. 1399 aumucelle afz. 1520 utimusse afz. 1520 nuqueton afz. 1272 avarie 138 avicenniie 893 ayan 38 azidarac 140 ««ciT 2180 memine 29 uzeroUe 2206 azimut 1818 rtso^A 2208 «0My 1311 babiroussu 148 babouche 1625 bacasse 171 bachibouzouck
###LKT iksir|Elixier
--- [ffpage 99] Sternbildes Corona borealis [Devic DEt 40]. 903. Ar. iksir: [Aus gr. Zr)piov 'das Trockene'] 'Stein der Weisen', d. h. die besondere Sub- stanz, die bewirken sollte, daß unedle Metalle in edle verwandelt würden ; ins- besondere sollte die Masse auch die Kraft besitzen, den menschlichen Kör- per zu gesunden, zu stärken und zu verjüngen, also 'Lebenssaft' ; hieraus it. elissire, elisire 'Heiltrank', frz. elixir,
###LKT kimija|Alchimie|Chemie
--- [ffpage 110] in alle europäischen Sprachen als Fach- ausdruck der Chemie übergegangen: sp. pg. alcali, frz. alcali, als alchemistischer Ausdruck algali 'Salpeter', dial. (Süd- frankreich) caliou 'Asche aus den Reb- stöcken', engl, alhdi, dtsch. Alkali usw. Auch der Namen des Elementes Kalium, Calium gehört hierhin, [Devic DEt 7. Lammens Rem 7. 1030. Ar. kälib: 'Leisten eines Schusters', ebenso tk. kalyh, Icahjp 'Modell, Fo
--- [ffpage 120] DE- MEISTER in ZDMG XXX, 534/538], dann 'Scheidekunst, Chemie'. Aus dem Ar. kommt: it. alchimia 'Goldmacher- kunst' [fast synonym zu inganno 'Be- trug'], alchimia 'ein aus Messing, Kupfer und Erz zusammengesetztes Metall', modern chimica, arte chimica 'Chemie', frz. alnhimie, chimie, sp. pg. alqtdmia; dtsch. Alchimie [für Alchimisterei heißt es bei Schuppius zur Verspottung dieser Afterwissenschaft ungemein treffen
```


## [2026-09-04T19:33:42.845Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\nfor p in 'Ar. kuhl|kohl.*Spießglanz|Alkohol' 'Ha?wärizmi|Choresm|Algorithmus|algorismo' 'itmid|ithmid|Antimon' 'sinaa|sina.a.*Haus|Arsenal' 'Tarik|Tariq|Gibraltar' 'Ar. samt|as-sumut|Azimut' 'Ar. nil\\b|Indigo' 'Ar. .abr|Algebra' 'Ar. .ud:|Ar. ud:|Laute.*sp. laud|alaude' 'isara|Alizarin|alizari' 'amir al-bahr|Admiral' ; do echo \"###LKT $p\"; python3 $S LKT.txt \"$p\" 420 2; done"
}
```


### [2026-09-04T19:33:45.224Z] TOOL RESULT

```
###LKT Ar. kuhl|kohl.*Spießglanz|Alkohol
--- [ffpage 126] foux, coheul, alcohol, it. alcool, rum. alcool; ndl. alkohol, engl, alcohol, dtsch. Alkohol; russ. alkogoV. — [Pers. und tk. heißt die Augenschminke übrigens sürme, subst. Inf. des tk. Vbs. siirmek 'glätten' vom Slamme seb, sit<>, süp 'glatt, 99 [Tk. kujruk. rein, glätten', Causativ süpür silr, Vämbery TktEtWb S. 148, Nr. 160.] [Mahn EtUnt 107. DE 42. Eguilaz 140. Devic DEt 13. 28/29. Lammens Rem 20/21. RomForsch IV, 364.
--- [ffpage 126] ool, rum. alcool; ndl. alkohol, engl, alcohol, dtsch. Alkohol; russ. alkogoV. — [Pers. und tk. heißt die Augenschminke übrigens sürme, subst. Inf. des tk. Vbs. siirmek 'glätten' vom Slamme seb, sit<>, süp 'glatt, 99 [Tk. kujruk. rein, glätten', Causativ süpür silr, Vämbery TktEtWb S. 148, Nr. 160.] [Mahn EtUnt 107. DE 42. Eguilaz 140. Devic DEt 13. 28/29. Lammens Rem 20/21. RomForsch IV, 364. ML 4732. Kluge 11. 1228. Tk.
###LKT Ha?wärizmi|Choresm|Algorithmus|algorismo
--- [ffpage 98] hlen um das Jahr 1200 nach Europa; daher wurde lat. algorithmus, algorismus [mit Anlehnung an gr. öpi&|ui6<;] die Bezeichnung für das Rechnen mit ar. Ziffern u. schließlich für Rechnungsverfahren überhaupt. Hieraus afrz. algofisme,frz. algorithme,it.alguaris- nio 'Rechenart, Arithmetik', sp. alguaris- nio, guarismo 'Ziffer', engl, algorism, algorithm 'Rechenart'. [DE 130/131. WOEPGKE in JAs (1863) I, 519. Devic DEt 18. Lammens Re
--- [ffpage 242] aegyptus 1222 alambicum 79 alchanna 867 algorismus 890 algorithmus 890 alleluia 793 ahnageshim 1348 almutium 1520 amaracum 1411 amen 68 amolimentum 866 amuletum 866 angraecum 82 angrecum 82 antiaris 85 antimonium 918 ascalonia (cepa) 119 augurium 1589 avicennia 893 halascius 151 balsatnum 293 bambagium 1617 Barabbas 220 ftarca 2148 harracanus 250 basilica (vena) 262 bezoar 1605 birrus 365 bisamutn 293 bombacium 1617 borrago 13 bronzium 1657
###LKT itmid|ithmid|Antimon
--- [ffpage 100] so tk. etba; hieraus rum. ecpaea 'Gefolge'. 918. Ar. itmid: [Aus äg. kopt. stün, altäg. sdm, woraus auch gr. oti|U|ui, lat. sfibium] 'Antimon'; hieraus mit starker Verstümmelung [viel- leicht aus der ar. Vokalisation utmud heraus] mlat. antimonium, frz. antinwine [woraus die spafähafte Volksetymologie von dem dtsch. Mönche entstanden, der seinen Bi üdern statt eines Purgiermittels Antimonium reichte, um sie zu vergiften : anti
--- [ffpage 100] altäg. sdm, woraus auch gr. oti|U|ui, lat. sfibium] 'Antimon'; hieraus mit starker Verstümmelung [viel- leicht aus der ar. Vokalisation utmud heraus] mlat. antimonium, frz. antinwine [woraus die spafähafte Volksetymologie von dem dtsch. Mönche entstanden, der seinen Bi üdern statt eines Purgiermittels Antimonium reichte, um sie zu vergiften : anti < gr. üivti 'gegen', frz. moine 'Mönch'], sp. pg. it. anlimonio; engl. antimony^
###LKT sinaa|sina.a.*Haus|Arsenal
--- [ffpage 65] en Korps der bengalischen Artillerie war. Im dortigen Arsenale wurden zuerst mit stumpfem Vorderende versehene, daher stark zer- reißende Geschosse liergestellt, die man engl, dum-dum, dtsch. Dimidumgeschosse nennt. [Hobson-Jobson 330. 478. Tk. damga: 'Stempel, Siegel' [vom Stamme tarn, dam 'Tropfen, tröpfeln' Vämbery Tkt EtWb S. 167, Nr. 180; aus 'Tropfen', nämlich 'zur Bekräftigung oder Unter- schrift eines gegenseitigen Vertrag
--- [ffpage 66] darsena, siz. tirzanä 'iniiei'es Hafenbecken', arzanä, arsenale, terzana 'Zeughaus'; frz. darse, darsine 'kleiner Binnenhafen', arsenal; sp. atarazana, atarazanal 'Schuppen', arsenal; pg. taracena, tercena 'Schuppen', arsenal; rum. arsenal, darsena. Dtsch. Arsenal, ndl. arsenaal, engl, arsenal, russ. a?*- senal. [Dozy Oost 16/18. DE 205/206. Eguilaz 304. Gorjaiew 6. Kluge 23. Devic DEt 35/36. ML 2474. 496. Pßrs« ilär^vGS • 'Bettl
###LKT Tarik|Tariq|Gibraltar
NO MATCH LKT.txt Tarik|Tariq|Gibraltar
###LKT Ar. samt|as-sumut|Azimut
--- [ffpage 172] htung', plr. sumüt, simüt; hieraus mit ar. Art. it. azimut, azimutto, frz. azimut; dtsch. Azimut [oder meistens mit grundlos angefügtem h:] Azimuth, engl, azimuth 'Bogen eines Scheitelkreises'. — Aus samt ar-ru'üs 'Richtung der Köpfe' oder kurz as-samt wurde mit Verschreibung von m zu ni it. zenit, frz. engl. ndl. zenith, dtsch. Ze- nit oder Zenith 'Scheitelpunkt' im Ge- gensatz zu Nadir [s. hier Nr. 1565). [Devic DEt 54.
--- [ffpage 172] plr. sumüt, simüt; hieraus mit ar. Art. it. azimut, azimutto, frz. azimut; dtsch. Azimut [oder meistens mit grundlos angefügtem h:] Azimuth, engl, azimuth 'Bogen eines Scheitelkreises'. — Aus samt ar-ru'üs 'Richtung der Köpfe' oder kurz as-samt wurde mit Verschreibung von m zu ni it. zenit, frz. engl. ndl. zenith, dtsch. Ze- nit oder Zenith 'Scheitelpunkt' im Ge- gensatz zu Nadir [s. hier Nr. 1565). [Devic DEt 54. NALLIN
###LKT Ar. nil|Indigo
--- [ffpage 61] area 'Kattun'. 429. Tk. cmid: Auch ciwit gesprochen: 'Indigopflanze, Indigofera tinctoria, indigofarben' ; hier- aus rum. civit 'indigoblau'. 430. Pers. cTz: 'Etwas' [Horn NpEt S. 101, Nr. 457], hieraus hind. chlz 'etwas, ein Ding' und schließlich angloind. cheeze, ebenso im engl. Slang, mit der Bedeutung 'etwas Gutes, Echtes, Ausgezeichnetes oder Vor- teilhaltes', z. B. 'my neiv arab is the real cheeze'. [Hobson-Jobson 187. 43
--- [ffpage 61] 429. Tk. cmid: Auch ciwit gesprochen: 'Indigopflanze, Indigofera tinctoria, indigofarben' ; hier- aus rum. civit 'indigoblau'. 430. Pers. cTz: 'Etwas' [Horn NpEt S. 101, Nr. 457], hieraus hind. chlz 'etwas, ein Ding' und schließlich angloind. cheeze, ebenso im engl. Slang, mit der Bedeutung 'etwas Gutes, Echtes, Ausgezeichnetes oder Vor- teilhaltes', z. B. 'my neiv arab is the real cheeze'. [Hobson-Jobson 187. 431. Tk. cizme:
###LKT Ar. .abr|Algebra
--- [ffpage 28] mel ausbreitende Wolkenge- bilde. [Wartbg FEWb 8. 9. Ar. abras: Auch tk. 'Pferd mit weißen und schwar- zen Füßen'. Hieraus rum. abra§ 'ge- fleckt, buntscheckig', tig. 'Unheil ver- kündend'; im walachischen Dialekt iabrai^, iambra^ 'Pferd mit weißen Flecken'. 10. Pers. äbresäui: [Horn NpEt S. 16, Nr. 65] 'Seide', ent- weder gehaspelte od, gedrehte, gezwirnte 1 Ar. ahn kirdäii.] 2 Ganzseide [auch ins Semitische über- gegangen : syr.
--- [ffpage 77] mmte Rechnungsart sp. pg. älgebra, frz. algkbre, it. algebra; engl, algebra, dtsch. Algebra usw. — In der ursprüng- lichen Bedeutung des ar. Vbs. gabara 'wiederherstellen, einrichten' ist noch sp. algebrista 'Chirurg' [Dicc Cast 121b; vgl. ähnlich engl, bone-setter] erhalten; pg. algebrista, algebista 'dass ', algebra 'dessen Kunst' [Gonstancio Dicc 50 c]. [DE 123. Eguilaz 179. ML 3941. 632. Pers. gäbr: 'Feueranbeter' [wohl
###LKT Ar. .ud:|Ar. ud:|Laute.*sp. laud|alaude
--- [ffpage 195] Uuto, liudo, afrz. leüt, frz. luth. sp. laud, pg. alaude, rum. lautä; ndl. luit, engl, lute, dtsch. Laute; [über tk. lauta, ICi'uta Kelekian KämQs 1073, das wie ngr. \aoöTa aus dem Rum. kommt] bulg. lauta 'Geige', serb. Icut 'Laute', klruss. lavuta 'Laute, Geige; Dummkopf, l'utn'a, russ. Ijtitnja, poln. lutnia, öech. loutna 'Laute'. — Wie die Laute, das Begleitinstrument der Lieheslieder, aus dem islamischen Orient zu un
###LKT isara|Alizarin|alizari
--- [ffpage 37] aus einer Pflanze gewonnen wird' ; hieraus sp. frz. alizari als Handelsausdruck für garance 'Fär- berröte, Krapprot' und weiter der che- 11 [Tk. ascy. mische Ausdruck Alizarin zur Bezeich- nung bestimmter Farbstoffe; frz. alisa- rine. Alizarintinte wurde i. J. 1855 zuerst in Dresden hergestellt. [Devic DEt 23. Lammens Rem 15. 117. Tk. ascy: [Aus as 'Suppe' und dem Suffix des Berufes gi; nicht npers. äs 'Brühe, Speise', wie
--- [ffpage 37] t' und weiter der che- 11 [Tk. ascy. mische Ausdruck Alizarin zur Bezeich- nung bestimmter Farbstoffe; frz. alisa- rine. Alizarintinte wurde i. J. 1855 zuerst in Dresden hergestellt. [Devic DEt 23. Lammens Rem 15. 117. Tk. ascy: [Aus as 'Suppe' und dem Suffix des Berufes gi; nicht npers. äs 'Brühe, Speise', wie Horn NpEt S. 8, Nr. 29 an- gibt; vgl. auch MO XVll, 145] 'Koch'; in vulgärer Aussprache ahgy; hieraus bulg. a
###LKT amir al-bahr|Admiral
--- [ffpage 32] t falscher etymologischer Beziehung zu lat. admirari] admiral, rum. amiral, it. ammiraglio [u. wie im sp. pg. mit Verkennung des ar. Stammes am ... als ar. Artikel] almiraglio, sp. pg. almirante [mit volksetymologischer Umbildung gemäß dem lat. partic. praes.], afrz. aumirant, prov. amiran, it. almi- rante. Die Bedeutung ist überall 'Ober- befehlshaber der Flotte'. Ebenso mhd. admirät [als Titel des Kalifen], dtsch. Admiral,
--- [ffpage 32] Ebenso mhd. admirät [als Titel des Kalifen], dtsch. Admiral, ndl. admiraal, engl, admiral. — Daß die Worte aus amlr-al-bahr 'Befehlshaber der See, des Meeres' ent- standen sein sollen, scheint wenig wahr- scheinlich, wenn auch ein solcher Weg- fall des arab. Wortes hahr an und für sich möglich ist, vgl. z. B. Denebola [s. hier Nr. 482], Abdul [wurde bei einem tk. Schüler, der 'Abd-ul-hädl hieß, stets als Name gebucht].
```


## [2026-09-04T19:34:08.330Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\nfor p in 'fisfisa|fi.fi.a|aspast' 'badingan|bäd|badinjan' 'zarnih|zarnīh|zarnik' 'nil\\b' ; do echo \"###PLA $p\"; python3 $S PLA_asbaghi_1988_ia_djvu.txt \"$p\" 420 3; done"
}
```


### [2026-09-04T19:34:10.058Z] TOOL RESULT

```
###PLA fisfisa|fi.fi.a|aspast
--- [ffpage 0] el - "asfast: "Luzerne, Futterpflanze" pers. 7 aus pers. ul aspast MP. ana aspast 8 gut - ”isfanab: "Spinat" = ”isbänäh q. v. 9 .93 Seel. ”isfand: "Wein" pers. ° aus dem pers. x..spand MP. 10» Spand 1. Lokotsch S. v. 2. Wahrig s. v. 3. al-Marfa® s. v. 4. Fremdwörterbuch 5. Mackenzie S. v. 6. LD. s. v. 7. al-Marfa° s. v., Muhit s. v. 8. Mackenzie s. v. 9. al-MuCarrab s. v. °isfand 19 ’ askudär aw. spantä spanta- spanta- *&Syanta-; nw. *spanta
--- [ffpage 0] uzerne, Futterpflanze" pers. 7 aus pers. ul aspast MP. ana aspast 8 gut - ”isfanab: "Spinat" = ”isbänäh q. v. 9 .93 Seel. ”isfand: "Wein" pers. ° aus dem pers. x..spand MP. 10» Spand 1. Lokotsch S. v. 2. Wahrig s. v. 3. al-Marfa® s. v. 4. Fremdwörterbuch 5. Mackenzie S. v. 6. LD. s. v. 7. al-Marfa° s. v., Muhit s. v. 8. Mackenzie s. v. 9. al-MuCarrab s. v. °isfand 19 ’ askudär aw. spantä spanta- spanta- *&Syanta-; nw. *spanta-, sw. *santa "
--- [ffpage 0] ne Pistazie". OR - fustugi: "pistaziengrün". ansıms - fisfisa: "Luzerne" pers. ?. 7, dtsch. Alfalfa. o5lhs - faßsäga: "Rakete", “. ’ Als- faß$äka - fafääga q. v. Aas_ fafakı: Pl. v. Es fafaka ga. v . Ais- fafaka: "Patrone". a, ls _ faSaka: "Patronentasche". E- fi$anf: ägypt. Ar. = ar. faßaka vers. Ks fe$ang 8, wLs3_ fisaäfis: Pl. veoes fisfisa q. v. 29 _ fisfisa: "Luzerne" pers.cuuul asbast od. a, asfast 9 1. Muhlit s. v. 2. Genaust s. v., F
###PLA badingan|bäd|badinjan
--- [ffpage 0] ar. sadaqga .ı pers. zarnih —> ar. zarniq .: pers. bädhiz —>ar. bädgais .ı pers. badiye, rud >> ar. batiyya, rut z. B.: pers. sarband —> ar. salband B B B 2..B.: pers. husraw ar. kasrä B B pers. äbriz ar. äbrig 2. B.: pers. SurI2 ar. IbrIq 2. B.: pers. zaryäb —> ar. daryäab z. B.: pers. az- kü- dari > ar. askudär z. B.: pers. arziz —>ar. rasäs z. B.: pers. rod mp. rodcT aw. raod / ap. raza, 2 ka fa m ober rer ko wo ir [y] fe) 2. B.: pe
--- [ffpage 0] a .ı pers. zarnih —> ar. zarniq .: pers. bädhiz —>ar. bädgais .ı pers. badiye, rud >> ar. batiyya, rut z. B.: pers. sarband —> ar. salband B B B 2..B.: pers. husraw ar. kasrä B B pers. äbriz ar. äbrig 2. B.: pers. SurI2 ar. IbrIq 2. B.: pers. zaryäb —> ar. daryäab z. B.: pers. az- kü- dari > ar. askudär z. B.: pers. arziz —>ar. rasäs z. B.: pers. rod mp. rodcT aw. raod / ap. raza, 2 ka fa m ober rer ko wo ir [y] fe) 2. B.: pers. sarpüs —>
--- [ffpage 0] ol ’ibbän "Zeit, Zeitraum, Zeitpunkt" s. ”ibbän. - „bi- äbäd: "Stadt" aus dem pers. „LI äbäd "bebaut, kultiviert" Io mp. Ir @or äpäatän eir. *ä-päta, im Ar. kommt es eigentl. mehr in zusammengesetzten Ortsnamen wie z. B. li ’istiräbäd und ähnl. vor. „LT- Abär: "Archiv" stammt nach Dehhodä aus dem pers. „Li’ämär "Statistik" ® mp. eo ämär "Auflistung der Toten" — aw. nar "rechnen", daraus in Targ. und Talm. ”’mrkr "Kassierer" °- Obi - ”abärig: Pl. v. Glri ”abräg "L
###PLA zarnih|zarnīh|zarnik
--- [ffpage 0] . rüzig —> ar. rizg, mp. sadyik> ar. sadaqga .ı pers. zarnih —> ar. zarniq .: pers. bädhiz —>ar. bädgais .ı pers. badiye, rud >> ar. batiyya, rut z. B.: pers. sarband —> ar. salband B B B 2..B.: pers. husraw ar. kasrä B B pers. äbriz ar. äbrig 2. B.: pers. SurI2 ar. IbrIq 2. B.: pers. zaryäb —> ar. daryäab z. B.: pers. az- kü- dari > ar. askudär z. B.: pers. arziz —>ar. rasäs z. B.: pers. rod mp. rodcT aw. raod / ap. raza, 2 ka fa m ober re
--- [ffpage 0] v. 11. Nyberg Bd. II s. v., Mackenzie s. v. zarrag 144 zarnih &)- zarrag: "eine Vogelart" pers. 1, a3, - zurga = zaragq q. v. Pr 4 - zarkaß: "Goldbrokat" aus pers. oJ; zarkes 2 mp. Is zarr +-.9 kaß v. VerbautkasIdan — mp. ws kaßitan au. karg °. al, - zurmänaga: "wollene Tunika ohne Ärmel" aus pers. bir usturbäne "Kamelwollware" 4 mn. E. ist es wahrscheinlich nur eine arabisierte Form v. pers. ut, zarmanak "wie Gold", wegen der gelben Farbe der Kamelwol
--- [ffpage 0] nart" pers. 10, Yo. - zaranbuk = zaranbuk q. v. Me] - zarnih: "Arsenik, Sandarak" pers. 11 < ap. daraniyä "Gold" 1. Fraenkel s. v. 2. Wahrmund s. v., Muhit s. v., Addai Scher s. v. 3. Nyberg Bd. II s. v. 4. Muhit s. v., albasa s. v. 5. Mackenzie Ss. v. 6. Brockelmann Ss. v. 7. Addai Scher s. v. 8. ebda. 9, Genaust Ss. v. 10. Muhit s. v. 11. Wahrmund s. v., al-MuCarrab s. v., Muhit s. v. Arsenik 145 za°faräni daher Arsenik u. Arsen aus dem ar.
###PLA nil
--- [ffpage 0] Weg!" pers. 10 ?. ol£,> - nisan = nißän a. v. "!. I- nil: "blau" pers. 120 mp.)ı nil. 1. Löw s. v. 2. Chista Bd. 10. S. 1188. 3. al-MuCarrab s. v. 4. Wahrmund s. v., Muhit s. v., Addai scher s. v. 5. Nyberg Bd. II s. v., Mackenzie s. v. 6. Addai Scher s. v. 7. Wahrmund s. v., Addai Scher s. v. 8. Nyberg Bd. II s. v. 9. Farawaäi s. v. 10. Addai Scher s. v. 11. Wahrmund s. v. 12. Addai Scher s. v., Genaust s. v. nilag 266 häla de - nilaß: "Is
--- [ffpage 0] - nisan = nißän a. v. "!. I- nil: "blau" pers. 120 mp.)ı nil. 1. Löw s. v. 2. Chista Bd. 10. S. 1188. 3. al-MuCarrab s. v. 4. Wahrmund s. v., Muhit s. v., Addai scher s. v. 5. Nyberg Bd. II s. v., Mackenzie s. v. 6. Addai Scher s. v. 7. Wahrmund s. v., Addai Scher s. v. 8. Nyberg Bd. II s. v. 9. Farawaäi s. v. 10. Addai Scher s. v. 11. Wahrmund s. v. 12. Addai Scher s. v., Genaust s. v. nilag 266 häla de - nilaß: "Isatis tinetoria, getrockneter
--- [ffpage 0] "Isatis tinetoria, getrockneter Indigosaft; Indigo" pers. vnil mp.) nil "Indigo" 1 syr.. Kos (pers. u) ®, BI - nilüfar: "Wasserlilie" —T pers. ,W nilüfar ® m. do. nilö- pal '"Wasserlilie", wahrscheinlich aus pers. )& nil "blau" + .„ par "Blatt" a mand. ninupar (p. Le), neuphar 5, syr. ?*D8% (pers. se) 6, aram. 7 7, pers. nil "blau" u. nüfär "Seerose", daraus der botanische Name Nuphar "> ar. nainüfar, näönüfar >sp. neufar, it. neufar, frz. nenuphar 8, ug - nimbri$
```


## [2026-09-04T19:34:10.929Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###AFM fisfisa\"; python3 $S AFM.txt \"فصفصة|اسپست|بادنجان|زرنيخ\" 300 6\necho \"###TAD\"; python3 $S TAD.txt \"فصفصة|بادنجان|زرنيخ\" 300 4"
}
```


### [2026-09-04T19:34:12.419Z] TOOL RESULT

```
###AFM fisfisa
NO MATCH AFM.txt فصفصة|اسپست|بادنجان|زرنيخ
###TAD
--- [ffpage 0] د صاروج -- فارسي « سارو » وهو الدورة اي حجر الكلس مخلط بالزرنيخ ومنه الصهر يج لحوض الماء لانه يطلل به صاقور وصوقر - بوناني 5 ولا'يتي 5 معنام الفأس صالون وصالية 9؟ - ايطالي 3اد5 معناه الاعة والردهة والهو صياوت - عيراني « صباؤت 6 جمع ومعناه الجند والمسكر والحاربون وهو تشدق من سباع أي حارب وعارك .' وساه بالثارسية معناه عكر وصابا بالاشورية مناه حار
```


## [2026-09-04T19:34:28.286Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###PLA zarnih full\"; python3 $S PLA_asbaghi_1988_ia_djvu.txt \"zarnih: \\\"Arsenik\" 700 2\necho \"###PLA badingan\"; python3 $S PLA_asbaghi_1988_ia_djvu.txt \"b.dingän|bädingan|bädin[gğ]\" 500 4\necho \"###PLA kimiya\"; python3 $S PLA_asbaghi_1988_ia_djvu.txt \"kImiy|kimiy\" 400 3"
}
```


## [2026-09-04T19:34:28.654Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 600 AFM.txt; echo; echo \"=== AFM_alt\"; head -c 600 AFM_alt.txt"
}
```


### [2026-09-04T19:34:29.984Z] TOOL RESULT

```
###PLA zarnih full
--- [ffpage 0] nart" pers. 10, Yo. - zaranbuk = zaranbuk q. v. Me] - zarnih: "Arsenik, Sandarak" pers. 11 < ap. daraniyä "Gold" 1. Fraenkel s. v. 2. Wahrmund s. v., Muhit s. v., Addai Scher s. v. 3. Nyberg Bd. II s. v. 4. Muhit s. v., albasa s. v. 5. Mackenzie Ss. v. 6. Brockelmann Ss. v. 7. Addai Scher s. v. 8. ebda. 9, Genaust Ss. v. 10. Muhit s. v. 11. Wahrmund s. v., al-MuCarrab s. v., Muhit s. v. Arsenik 145 za°faräni daher Arsenik u. Arsen aus dem ar. sernik pers. g zarnih g. v. 1 frz. sandaraque, griech. sandarake zu pers. sandar sy r. pn, 3, S,- zami = zamip g. v. % .. _ - 4 Sr - zarnig = zarnih q. v. .» o an, - zarniyya: "Zerumbet" s. zarunbad 5, >2,- zurüd: Pl. v.2„, zarad q. v. >, - zarwand = zaräw
###PLA badingan
--- [ffpage 0] 10, eb - bädanf: "Kokosnuß" pers. 11, barang . oSlos>l - bädingän = bädimgän s, bädimkan . &e>L - bädhanf = bädähanf s. bädähan . >„>L - bädward = bädäward s. bädäward. Pd &e'>L - vädähanf = bädähang s. bädähang . Fa z!>L - vädäward = bädäward s. bädäward . 1. Wahrmund s. v., al-Marga° Ss. Ve. 2. Steingaß s. v. 39. ebda. 4. ebda. 5. al-MuCarrab s. v., Addai Scher s. v., Mu°&am al-Wasit Ss. Vs 6. pahl.-pa2. S. v. 7. Mackenzie s. v. 8. Steingaß s. v. 9. Lokotsch Ss, v. 10. Wahrmund Ss. v. 11. BQ. s. v. bägrüg 35 bärnäm
--- [ffpage 0] °. zb - bädan$ = bädanf s. bädan . Olos»L - bädinkan = bädingän s. bädingan. zze>\. - bädhand = bädhanf s. bädhanf . >33, - bädward = bädward s. bädward . \,L - bärka = bärfäh s. barkäh ® ole,L - bärdän: "Kriegsschiff; Gasthof" aus dem pers. „UL bärgäh m. 2, bar "Festmahl" +. gäh "Platz" au. gatu / ap. gadu 4, a&,L_- värkan = bärkäh s. bärkän °. pl - bär$üba: "asparagus, Schlangenholz, Spargel" = >,>e,L mar- tübe s. märdüba syr. Lo 6, ab - bärih: "heißer Wind aus Jemen", aus dem pers. o,. bahre << mp . Du) bahrag . sul - bä
--- [ffpage 0] ädan$ = bädanf s. bädan . Olos»L - bädinkan = bädingän s. bädingan. zze>\. - bädhand = bädhanf s. bädhanf . >33, - bädward = bädward s. bädward . \,L - bärka = bärfäh s. barkäh ® ole,L - bärdän: "Kriegsschiff; Gasthof" aus dem pers. „UL bärgäh m. 2, bar "Festmahl" +. gäh "Platz" au. gatu / ap. gadu 4, a&,L_- värkan = bärkäh s. bärkän °. pl - bär$üba: "asparagus, Schlangenholz, Spargel" = >,>e,L mar- tübe s. märdüba syr. Lo 6, ab - bärih: "heißer Wind aus Jemen", aus dem pers. o,. bahre << mp . Du) bahrag . sul - bärzad: "Galba
###PLA kimiya
--- [ffpage 0] = kailafa q. v., aram. bo. 7 -_ = = 102. Go - kimawi = kimiyawi q. v. Too 5 <es- kimuht: "Ruhe" pers. ?. I. - G,.3- kimaw = kKimiyawi q. v. >41 Le» - kimiyä: "Chemie" pers. 675, 5 - ,_ SL. - kimiyawi: Nisba v. kimiya q. v. “ -_—_.._ -_ sLeJ- kImiyäwiyya: s. I. kimiyä q. v. oJ - a Pr AwS2)- lahsa: "eine Speiseart", pers. 4 Wahrmund s. v., Chista Bd. 10 s. Macuch S. v. Muhit s. v., Fraenkel s. v. Löw s. v. Wah
--- [ffpage 0] o 5 <es- kimuht: "Ruhe" pers. ?. I. - G,.3- kimaw = kKimiyawi q. v. >41 Le» - kimiyä: "Chemie" pers. 675, 5 - ,_ SL. - kimiyawi: Nisba v. kimiya q. v. “ -_—_.._ -_ sLeJ- kImiyäwiyya: s. I. kimiyä q. v. oJ - a Pr AwS2)- lahsa: "eine Speiseart", pers. 4 Wahrmund s. v., Chista Bd. 10 s. Macuch S. v. Muhit s. v., Fraenkel s. v. Löw s. v. Wahrmund s. v. al-Mu°arrab Ss. Vs Bartholomae s. v. Muhit s. v., Addai Scher
--- [ffpage 0] ?. I. - G,.3- kimaw = kKimiyawi q. v. >41 Le» - kimiyä: "Chemie" pers. 675, 5 - ,_ SL. - kimiyawi: Nisba v. kimiya q. v. “ -_—_.._ -_ sLeJ- kImiyäwiyya: s. I. kimiyä q. v. oJ - a Pr AwS2)- lahsa: "eine Speiseart", pers. 4 Wahrmund s. v., Chista Bd. 10 s. Macuch S. v. Muhit s. v., Fraenkel s. v. Löw s. v. Wahrmund s. v. al-Mu°arrab Ss. Vs Bartholomae s. v. Muhit s. v., Addai Scher s. v. 8,, 1192. dal, h
```


### [2026-09-04T19:34:30.033Z] TOOL RESULT

```
8 


0 
ܥܝ 


ܶܡ 7 
ܫ ܢ 0 ܣܚ 
.ܡܨ >  )‏ اعم ܨ 
3 ܛ 5 62 ܨ ܗ 

ܡ 5 

1 ` < 3[ 
1 , 3 5 ܢ 
ل ܨ( : : 
`( × 2 7 : ̄ܡ 

ܝ 2 -. و 

/ ܪ ܇ ܐ ܢ 
. ܥ يبد < ܲܗ 

ܘܨ ܝ ܓ 


بي بهم 0 1 1 
ܗܨ . ܢ 1 ` 
ܙ ^ ܢܢ 
9 ܪ 1 .° 2 
3 0 : 
1 : ܫ" 
ܫ ܠ 1 ܨܢ 7 1 
" ܐ . ܢ 
ܨ.܀ .ܝ 4 ܙ ܗܩ 1 
ل رار ܨ 
هيه ܘ 
ܫ @ < ܟ 
227 5 ܪܐ 8 
` ܫ ܨ 
ܡ ܨܝ بسح ܬ 
: ܕ ܝܚ 
ܝܢ ܗ 
ܬ ܛܠ ܝܚ ص 1 
: 3 3 1 
2 : 
1 ܝ ܼܪ ܝ 1 3 
ܫܡܚ ل 
ܓܥ 1 
9 ܨ 


ܗ : 


1 


ܝܝ 
1 


ܝ 
ܝ 


ܬܚ 
ܢ 


5 

‫, 

5 
ܝ 


ܛܡ 2 


9 
1 


2 ܢ 50 0
=== AFM_alt
الالفاظ الفارں س عر بت 


اليف 
ا 2 


رسس اة سعرد ET‏ 


N 


ج 


في المطبعة الكاثوليكة للاباء السوعين 


باروت سنه ٧۹۰۸‏ 


فاتت اکتا 


ان اللغة العر بمة مشحونة بالفاظ اعجب.ة كثيرة ٠‏ ولا غرو من ذلك فان القائل 
ابسرطة في معيشتها وسياستها متى خالطت الامم الغريمة التمدنة ادخلت لا عالة 
الفاظا اعحسىة الى لغتها وهذا ما ری مع العرب فانم زاوا 2 م�
```


## [2026-09-04T19:34:49.542Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\nfor p in 'بادنجان' 'فصفصة' 'زرنيخ' 'النيل' 'كيمياء' 'الانبيق|الأنبيق' 'الاكسير|الإكسير' ; do echo \"###AFM_alt $p\"; python3 $S AFM_alt.txt \"$p\" 260 2; done"
}
```


## [2026-09-04T19:34:51.191Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\npython3 $S PLA_asbaghi_1988_ia_djvu.txt \"bädimgän|bädimkan\" 500 4\necho \"=== pages file for zarnih\"; grep -n \"zarnih\" PLA_pages.txt | head -5"
}
```


### [2026-09-04T19:34:51.365Z] TOOL RESULT

```
###AFM_alt بادنجان
NO MATCH AFM_alt.txt بادنجان
###AFM_alt فصفصة
NO MATCH AFM_alt.txt فصفصة
###AFM_alt زرنيخ
NO MATCH AFM_alt.txt زرنيخ
###AFM_alt النيل
--- [ffpage 0] من العظلم بان شل ورت بالاء ما عله من الزرقة وبتر الاء يرس النيلح اسفله کالطین فنصت الاء E‏ ل ارف : ضرب ق ار ياعين ينتاف الباه الراكدة 4 أصل کال زر وساق اماس بماول بحسب عق الاء فاذا ساؤی سماة أرق وأزهر واذا بلغ 2 ِء 5 : 3 ۴ ص بب سقط عن رأسه مر داخ بزر اسود ۰ فارسله يأو پر وهو مرگب من نیل وهو ال ۱١ —‏ — يصغ
###AFM_alt كيمياء
NO MATCH AFM_alt.txt كيمياء
###AFM_alt الانبيق|الأنبيق
NO MATCH AFM_alt.txt الانبيق|الأنبيق
###AFM_alt الاكسير|الإكسير
NO MATCH AFM_alt.txt الاكسير|الإكسير
```


### [2026-09-04T19:34:53.223Z] TOOL RESULT

```
--- [ffpage 0] bädanf: "Kokosnuß" pers. 11, barang . oSlos>l - bädingän = bädimgän s, bädimkan . &e>L - bädhanf = bädähanf s. bädähan . >„>L - bädward = bädäward s. bädäward. Pd &e'>L - vädähanf = bädähang s. bädähang . Fa z!>L - vädäward = bädäward s. bädäward . 1. Wahrmund s. v., al-Marga° Ss. Ve. 2. Steingaß s. v. 39. ebda. 4. ebda. 5. al-MuCarrab s. v., Addai Scher s. v., Mu°&am al-Wasit Ss. Vs 6. pahl.-pa2. S. v. 7. Mackenzie s. v. 8. Steingaß s. v. 9. Lokotsch Ss, v. 10. Wahrmund Ss. v. 11. BQ. s. v. bägrüg 35 bärnäma &>l - bä
--- [ffpage 0] osnuß" pers. 11, barang . oSlos>l - bädingän = bädimgän s, bädimkan . &e>L - bädhanf = bädähanf s. bädähan . >„>L - bädward = bädäward s. bädäward. Pd &e'>L - vädähanf = bädähang s. bädähang . Fa z!>L - vädäward = bädäward s. bädäward . 1. Wahrmund s. v., al-Marga° Ss. Ve. 2. Steingaß s. v. 39. ebda. 4. ebda. 5. al-MuCarrab s. v., Addai Scher s. v., Mu°&am al-Wasit Ss. Vs 6. pahl.-pa2. S. v. 7. Mackenzie s. v. 8. Steingaß s. v. 9. Lokotsch Ss, v. 10. Wahrmund Ss. v. 11. BQ. s. v. bägrüg 35 bärnäma &>l - bägrüß = bädrü
=== pages file for zarnih
382:           pers.    5 >       ar.                B .ı    pers.       zarnih —> ar.                 zarniq
8187:zarrag                                                                         144                                                            zarnih
8227:Me] - zarnih:                         "Arsenik,              Sandarak"          pers.       11 < ap.             daraniyä         "Gold"
8244:         daher                Arsenik             u.     Arsen     aus          dem        ar.        sernik             pers.      g         zarnih      g.    v.    1
8254:Sr           -       zarnig             =    zarnih        q.    v.        .»
```


## [2026-09-04T19:34:58.411Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && sed -n '8180,8260p' PLA_pages.txt | sed 's/  */ /g'; echo \"=== pdf page tag near\"; awk 'NR>=8100 && NR<=8260 && /pdf page/' PLA_pages.txt"
}
```


### [2026-09-04T19:34:59.943Z] TOOL RESULT

```
5. Mackenzie s. v.
6. Löw s. v.
7. Addai Scher s. v.
8. Wahrmund s. v.
9. Macuch s. v.
10. Wahrmund s. v.
11. Nyberg Bd. II s. v., Mackenzie s. v.
zarrag 144 zarnih



&)- zarrag: "eine Vogelart" pers. 1,

a3, - zurga = zaragq q. v.
 Pr 4

 - zarkaß: "Goldbrokat" aus pers. oJ; zarkes 2 mp. Is zarr +-.9 kaß
 v. VerbautkasIdan — mp. ws kaßitan au. karg °.

al, - zurmänaga: "wollene Tunika ohne Ärmel" aus pers. bir usturbäne
 "Kamelwollware" 4 mn. E. ist es wahrscheinlich nur eine arabisierte
 Form v. pers. ut, zarmanak "wie Gold", wegen der gelben Farbe der
 Kamelwolle.


> - zarmug: "eine Art Schuhe" es kommt wahrscheinlich vom pers. 2
 zirmu& "unter dem Fußgelenk" od. mp.» mög "Schuhe" 5,

 oo = - s.
ER, - zarnafa: "pures Gold" aus pers. ..L,, zarnäb s. zarbäb, *syr.=)> 6


<&)),- zarnab: "eine wohlriechende Pflanze" aus pers. —, zarnab 7,


>», - zarunbäd: "Zerumbet" (bot.) pers. 8, port. zerumbet, engl. zerumbet.
 dtsch. Zerumbet °,


>) - zarunbad = zarunbäd q. v.

Öıs,)- zaranbuk: "eine Pflanzenart" pers. 10,


Yo. - zaranbuk = zaranbuk q. v.


Me] - zarnih: "Arsenik, Sandarak" pers. 11 < ap. daraniyä "Gold"


1. Fraenkel s. v.
2. Wahrmund s. v., Muhit s. v., Addai Scher s. v.
3. Nyberg Bd. II s. v.
4. Muhit s. v., albasa s. v.
5. Mackenzie Ss. v.
6. Brockelmann Ss. v.
7. Addai Scher s. v.
8. ebda.
9, Genaust Ss. v.
10. Muhit s. v.
11. Wahrmund s. v., al-MuCarrab s. v., Muhit s. v.
Arsenik 145 za°faräni


 daher Arsenik u. Arsen aus dem ar. sernik pers. g zarnih g. v. 1
 frz. sandaraque, griech. sandarake zu pers. sandar sy r. pn, 3,


S,- zami = zamip g. v.
 %



 .. _ - 4
Sr - zarnig = zarnih q. v. .»

 o
an, - zarniyya: "Zerumbet" s. zarunbad 5,


>2,- zurüd: Pl. v.2„, zarad q. v.
=== pdf page tag near
```


## [2026-09-04T19:35:17.465Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\nfor f in MON_part1.txt MON_part2.txt; do for p in 'آدمیرال|آدميرال' 'الکل|الكل' 'آنتیموان|آنتيموان' 'آلکالی|آلكالی' 'آرسنیک|آرسنيك' 'آلفالفا' 'آلگوریتم' ; do echo \"###$f $p\"; python3 $S $f \"$p\" 220 2; done; done 2>&1 | head -80"
}
```


### [2026-09-04T19:35:20.434Z] TOOL RESULT

```
###MON_part1.txt آدمیرال|آدميرال
--- [ffpage 0] ات ال 301121 [ع. امیرالس حر] (ا.) امیرالبحرء دریاسالار. آدمیرال. ام 7 زر د. آمیزیدن؛ قس. آمیغ ] آمیزش» مخلوط کردن. معاشرت. مباشرت» 0 آمیغ. . (افا.) در بعضی کلمات مررکب سه معنی «آمیزنده) ات مردم آمیز» رنگ امیز. (امف.) در برخی کلمات مرکب 4 نی «آمبخته»: حسرت آمیزه شهوت آ
###MON_part1.txt الکل|الكل
--- [ffpage 0] نوشابه‌ای که از تخمیر جو نیش زده تهبه کنند و ۲/۵ و ۵ درصد الکل دارد. شراب جوء فوگان؛ فقاع. اب جوش: 2-155 (امر.) آبی که در حال جوشیدن است» آب جوشان. آب گرم آبچی مععد‌نی. اسی که در آن جوش بعنی بی‌کربنات سود و اسید طرطیر کنند و مانند گوارشی بياشامند. آبسجی: آ[20 [تر
--- [ffpage 0] ک فرار و سریع التسخبری است که از ترکیب وت معدنی یا آلی با الکل بدست می‌آید» اترسل. (شیم.) ماده‌ای که از گرفتن یک مولکول آب از دو مولکلول الکل حاصل شود؛ اتر اکسید. اتراق: 5۲ ([تر - او تراق ] (.) توقف جند روزه در سفری بجایی. اترج: سور می. تر نج فارسی] (ا.) (گیا.) ترنج» با
###MON_part1.txt آنتیموان|آنتيموان
--- [ffpage 0] کحل. : ضح.- شلیمر در کتاب با فوالذکر ‏ را مرادف با سولفور آنتیموان نیز ذکر کرده که جهت ساختن فشفشه‌های آتش‌بازی بکار می‌رود. ترکیبات اسمی: ۰5۴ فرهنگ فارسی معیر سر مه‌دان مترمه جا کین سرمهاق از آن صرو پرویر که نور چشم را زیاد می‌کرد (داستان). سر مه کشت مازایکت: میل سرم
###MON_part1.txt آلکالی|آلكالی
NO MATCH MON_part1.txt آلکالی|آلكالی
###MON_part1.txt آرسنیک|آرسنيك
NO MATCH MON_part1.txt آرسنیک|آرسنيك
###MON_part1.txt آلفالفا
NO MATCH MON_part1.txt آلفالفا
###MON_part1.txt آلگوریتم
NO MATCH MON_part1.txt آلگوریتم
###MON_part2.txt آدمیرال|آدميرال
NO MATCH MON_part2.txt آدمیرال|آدميرال
###MON_part2.txt الکل|الكل
--- [ffpage 0] لاوه میوة مذکور شامل یک رزین تند و سوزاننده محلول در اتر و الکل و یک آلکالوئید بنام پی‌پرین است. فلفل دارای آنتتز تخر یک کنتئند: مسخاط و عطسه آور است و معمولا به مقدار کم و زیادش موجب ترشحات معده و پانک رآس می‌گردد. گرد فلفل دارای اثر متفرق کنندة حشرات است. از این نظر پارچ
--- [ffpage 0] و در ۱ اس ۱۱ ۲ می‌شود و باقیمانده‌اش پس از سوختن در آب و الکل قابل حل است. بهترین قطران قطرانی است که از زغال سنکك حاصل می‌شود. قطرانی که از چوب‌ها و انساج گیاهی بدست می آید بنام قطران گیاهی موسوم است و قطرانی را که از زغال سنگ می‌گیرند بنام قطران زغال سنکك می‌نامند. در
###MON_part2.txt آنتیموان|آنتيموان
--- [ffpage 0] : ا فان دارداف تر کت: آن عسبارت است از اکسی‌سولفور مسعدئی آنتیموان و آن بصورت سوزن‌های قرمز رنگی متبلور می‌شود. ترکیب آن را می‌توان سصورت ٩0۲0۳۲۹۳۹۷۲۳‏ نوشت. وزن تخضو اش اس ۳۵ ۴/۹۲ مغر امنت و سختیش بین ۱ تا ۵ متغیر است. در رنگرزی و نقاشی بکار می‌رود. فرمز شد ل: 7-0027 [سن
--- [ffpage 0] الت خالص دیدهامی‌شود و یشتز با کمی نقره یا آهن یا روی و یا آنتیموان همراه است؛ حجر رصاص؛ حجر الرصاص. گالن: ۵510 (ا.) مقیاسی است برای سنجیدن مابعات و آن معادل ۲/۷۸ لیتر است. گاله: (2۱«0: (- گسوال - جوال] (.) خورجینی که بر پشت خر و ستوران دیگر کسترند و در هر دو خانةٌ آن خاکك
###MON_part2.txt آلکالی|آلكالی
NO MATCH MON_part2.txt آلکالی|آلكالی
###MON_part2.txt آرسنیک|آرسنيك
--- [ffpage 0] به این بیماری بیشتر مبتلی سی‌شوند) مداوای آن الب با املاح آرسنیکث یا آنتی‌پیرین به عمل می آ ید و در صورت نداشتن ناراحتی قلبی کلرال نیز مفید است و نیز تزریق محلول ۵ سولفات دومنیزی به مقدار ۵ سانتیمتر مکعب هر دو روز یک مرتبه دارای اثر نیکو است و بهتر از همه بهبود وضع تغذ یه
--- [ffpage 0] ند. (پز.) مخلوطی از هک زنده و زرنیخ زرد (سولفور سه ظرفیتی آرسنیک) به بت( وم و خاکستر چوب که به قدر لزوم با اب خمیر می‌کنند و جهت ازالهٌ موهای اضافی بدن بکار می‌برند» نوره» تنویر. واجبی: -9ع[۷2 [ع. ف.] (حامص.) واجب بودن؛ وجوت)؟ مق. ممکن. واحد: ۷310 [ع.] (افا. ص.) دار نده
###MON_part2.txt آلفالفا
NO MATCH MON_part2.txt آلفالفا
###MON_part2.txt آلگوریتم
NO MATCH MON_part2.txt آلگوریتم
```


## [2026-09-04T19:35:39.048Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###HRN zarnik\"; python3 $S HRN.txt \"zarni|zernī|zarnī\" 400 4\necho \"###HUB zarnik\"; python3 $S HUB.txt \"zarni|zarnī\" 400 3\necho \"###PHD zarnik\"; python3 $S PHD_mackenzie.txt \"zarnīg|zarnig\" 250 3"
}
```


### [2026-09-04T19:35:40.698Z] TOOL RESULT

```
###HRN zarnik
--- [ffpage 363] a^-M? 654. Zarin gün 661. ' ZanvBr 654 Anm. I znrmän 659. : zarniämh 659. ' ««>-^ 656. zartlh. 656. Zartu^st 1070 Anm. 2:äs/ 257. 2^ä^an 645. 2;a/n»i 653. Äd^är 653. zavän 650. zäyOßn 615. zäyU(ni 2'i7. zbnyltnn 41. zSn 240. zBmivand 240. zendän 671 Anm. 2;*« 2iO. zOJndäH 671. ziiiltan 24 L zlnUär 241. zist 662. zivandak 683. : zlvastan 683. ; zlvfißn 683. j z(i)yän 679. ' ! <2röAr 675. ! ;eö/- 674 bi«, 675. arör*/* 674*»'». 2;räc? 660. zräl 660. a^rc 561.
###HUB zarnik
--- [ffpage 268] r arm. zarik (Mos. Geogr.) *Auripigment, Ar- senik' (= ap. *zarnii/a ftir zd. zaranya- *6old*) neben
###PHD zarnik
NO MATCH PHD_mackenzie.txt zarnīg|zarnig
```


## [2026-09-04T19:35:40.730Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###GPL arabic article\"; python3 $S GPL.txt \"article al|definite article\" 400 4\necho \"###BQT v1 الکل\"; python3 $S BQT_v1.txt \"الكل|الکل\" 200 2\necho \"###BQT v2 زرنیخ\"; python3 $S BQT_v2.txt \"زرنيخ|زرنیخ\" 250 3"
}
```


### [2026-09-04T19:35:42.762Z] TOOL RESULT

```
###GPL arabic article
--- [ffpage 9] 31. The other Cases, 32. Example of Declen- sion, 33. The Indefinite Article, 33. The Adjective, 34. Concord of the Adjective and Substantive, 34-36. Comparison of Adjectives, 36-39. Intensive Adjectives, 39. Superlative of Eminence, 39. Adverbial Superlative, 39. Adjective of Admira- tion, 40. NoumERALS, 41. Words used Idiomatically in Numbering, 43. Dis- tributive Numerals, 44. Multiplicative Numerals, 45. Approxi- mate Numbers, 45. Fractional Numbers, 4
--- [ffpage 28] as will be shown in treating of the ¢zafat (§ 26) and the indefinite article (§ 36). Orthographical Signs 15 Rem. The Arabic * is a small ¢, and indicates that the pronuncia- tion of | approximates to that of ‘ain. § 12. Madda. The sound of long a )2( at the beginning of a word or sate is represented by 7 instead of را‎ as آب‎ ab, heal: adsman, ole qur'am. The mark ~ is a relic of the word 3» madd, ‘ prolonga- tion’, which when hastily written becomes ~. P
--- [ffpage 31] ); e.g. خدایا‎ 000000. 4) Gs i, ‘the 2 of unity ’, or the indefinite article (§ 36), پادشاهی‎ padshahi, eee buztirg?. 5) The enclitics -am, -at, -ash, &c. (§ 59), ۰ os pidaram, دخترش‎ dukhtdérash. b) Verbs in the Past tense where the last syllable is one of the personal endings -
--- [ffpage 49] ith a spear. ] Sociative با پدر‎ with the father. II. THE INDEFINITE ARTICLE § 36, The indefinite article وحدت)‎ ul ‘the ی‎ of unity’, and pe یای‎ ‘the ی‎ of indefiniteness’) is expressed in Persian by an ی‎ 7 (originally, and, in India, still 2) affixed to a noun; e.g. مردی‎ mardi (archaic mardé) ‘a man’; cabs ee pe “B آمویی‎ fa deer’ ; Zale or ماهی‎ ‘a fish’; نامع‎ ‘a letter, a book’; ae kast (kasé) ‘ some. person, some one’ ; یکی‎ ‘some one, a certain o
###BQT v1 الکل
--- [ffpage 0] لوی چاپ علاه|لدوله ۱۲۹۹ ص۲۰ س ۲۷ بیعد. تا اليه یصعد اطیاب الکلم صاعدا منا الی حیث علم . .. پارسی کوییم یعنی اين کشش ز آن‌طر فآید که آمداین چشش. مشوی . ابضا ص۲۳ ۲4۳ بعد. اتتلونی افتلونی یبائقات ان فی فتلی حیاتا فی حیات ... پارسی گو گر چه‌تازی‌خوشتررست
--- [ffpage 0] ا نند کتابالاصنامو کتابا لخیل‌باا نساب الخیل تألیف هشام‌بن الکلبی متوفی درع ۲۰ و کتاب الخیل تألیف ابوعبیده معمر بن مشنی نیمی‌متوفی در ۲۰۹ و کتاب‌الپمز و کتاب النطر و کتاب اللبا واللبن هرسه‌از ابوزید سعیدین لوس‌انصاری متوفی در ۲۱۵ ووکتابالدارات و کتاب النبا
###BQT v2 زرنیخ
--- [ffpage 0] . چون نرآنرا بآب بایند مانئد شنجرف سرخ شود » وماد آن همجو زرنیخ زرد گردد.و کون آن نوعی ازآهن است وطبیمت هردو سرد بود . چون برورمهای صفراوی ودموی طلا کنند نافع باشد خاصه ماده آنرا که درو برودت بشتراست و اکر در ظرف آن شراب خورند مستی نیاورد و آنرا بعر بی حجر جدیندی وصندل جدیدی خوانن:. وای کو شه گی است
--- [ffpage 0] رد آب کل کاوشه رالیز کوند ۳ . رد نی - بر وزن برتی ۰ مخفف زرنیخ است؟ ۰ وآن جوهری باشد کانی رآن بر دو لوع است : احمر واصفر. احمر را ال صنعت كيا کار برند و اصفی را استادان نقاش. * رر نق - بفتح اول و سکون آخ رکه رر نله = بفتح ارل بر وزن غریله » ربوای را کوبند. و آن‌رستنیی باشد معروف که خورند ومعرب آن
```


## [2026-09-04T19:35:50.346Z] TOOL CALL #43: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-04T19:35:50.390Z] TOOL RESULT

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
```


## [2026-09-04T19:35:54.344Z] TOOL CALL #44: Bash

```json
{
 "command": "for w in admiral alfalfa alcohol algorithm antimony alkali arsenic amalgam; do python3 tools/fetch_source.py \"https://www.etymonline.com/word/$w\" --note \"page 47, root Al 3, English node $w\" ; done 2>&1 | tail -20"
}
```


### [2026-09-04T19:35:58.273Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5c5fd5f304537f2a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/01b2b5ab2d62475e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3ad7d93151ff9988.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a4d7501a1c70bce5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c85b6a402cb6810f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0070109655be6e11.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0cf3e23ff5e8626b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c2ab61cbb80fefe4.txt
```


## [2026-09-04T19:36:01.052Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 5c5fd5f304537f2a 01b2b5ab2d62475e 3ad7d93151ff9988 a4d7501a1c70bce5; do echo \"=== $f\"; sed -n '1,6p' $f.txt; grep -o \"Advertisement.\\{0,1800\\}\" $f.txt | head -1; done"
}
```


### [2026-09-04T19:36:02.611Z] TOOL RESULT

```
=== 5c5fd5f304537f2a
URL: https://www.etymonline.com/word/admiral
FETCHED: 2026-09-04T19:35:56Z
STATUS: 200
TITLE: Admiral - Etymology, Origin & Meaning

Admiral - Etymology, Origin & Meaning 
Advertisement Remove Ads 
=== 01b2b5ab2d62475e
URL: https://www.etymonline.com/word/alfalfa
FETCHED: 2026-09-04T19:35:56Z
STATUS: 200
TITLE: Alfalfa - Etymology, Origin & Meaning

Alfalfa - Etymology, Origin & Meaning 
Advertisement Remove Ads 
=== 3ad7d93151ff9988
URL: https://www.etymonline.com/word/alcohol
FETCHED: 2026-09-04T19:35:56Z
STATUS: 200
TITLE: Alcohol - Etymology, Origin & Meaning

Alcohol - Etymology, Origin & Meaning 
Advertisement Remove Ads 
=== a4d7501a1c70bce5
URL: https://www.etymonline.com/word/algorithm
FETCHED: 2026-09-04T19:35:57Z
STATUS: 200
TITLE: Algorithm - Etymology, Origin & Meaning

Algorithm - Etymology, Origin & Meaning 
Advertisement Remove Ads
```


## [2026-09-04T19:36:05.935Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 5c5fd5f304537f2a 01b2b5ab2d62475e 3ad7d93151ff9988 a4d7501a1c70bce5 c85b6a402cb6810f 0070109655be6e11 0cf3e23ff5e8626b c2ab61cbb80fefe4; do echo \"###################### $f\"; sed -n '5,80p' $f.txt | tr -s ' ' | head -60; done 2>&1 | head -250"
}
```


### [2026-09-04T19:36:07.875Z] TOOL RESULT

```
###################### 5c5fd5f304537f2a

Admiral - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of admiral 

 admiral (n.) 

 c. 1200, amiral , admirail , "Saracen commander or chieftain," from Old French amirail (12c.) "Saracen military commander; any military commander," ultimately from medieval Arabic amir "military commander," probably via Medieval Latin use of the word for "Muslim military leader."

 Amiral de la mer "commander of a fleet of ships" is in late 13c. Anglo-French documents. Meaning "highest-ranking naval officer" in English is from early 15c. The extension of the word's meaning from "commander on land" to "commander at sea" likely began in 12c. Sicily with Medieval Latin amiratus and then spread to the continent, but the word also continued to mean "Muslim military commander" in Europe in the Middle Ages. The Arabic word was later Englished as emir .

 As 
 amīr is constantly followed by 
 -al- in all such titles, 
 amīr-al- was naturally assumed by Christian writers as a substantive word, and variously Latinized .... [OED]

 Also in Old French and Middle English the word was further conformed to familiar patterns as amirauld , amiraunt . The unetymological -d- probably is from influence of Latin ad-mirabilis (see admire ). Italian form almiraglio , Spanish almirante are from confusion with Arabic words in al- . As the name of a type of butterfly from 1720, according to OED possibly a corruption of admirable .
 also from c. 1200 

 Entries linking to admiral 

 admire (v.) 

 early 15c. (implied in admired ), "regard with wonder, marvel at," from Old French admirer "look upon, contemplate" (correcting earlier amirer , 14c.), or directly from Latin admirari "regard with wonder, be astonished," from ad "to, with regard to" (see ad- ) + mirari "to wonder," from mirus "wonderful" (see smile (v.)). The sense has gradually weakened toward "regard with pleasure and esteem," but for a time they overlapped.

 Doe not admire why I admire :

 My fever is no other's fire :

 Each severall heart hath his desire ;

 Els proof is false, and truth a lier.

 [Campion, "And would You Faine the Reason Knowe," in "Rosseter's Booke of Ayres Part II," 1601]

 Related: Admiring ; admiringly .

 emir (n.) 

 among Arabic or Muslim peoples, "chief of a family or tribe; a ruling prince," 1590s, from Arabic amir "commander" (see admiral ).

 admiralship 
 admiralty 
 See All Related Words (4) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

###################### 01b2b5ab2d62475e

Alfalfa - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of alfalfa 

 alfalfa (n.) 

 common name in North America for "lucerne," a plant in the legume family important as a forage crop, 1845, from Spanish alfalfa , earlier alfalfez , said by Iberian sources to be from Arabic al-fisfisa "fresh fodder." Watkins says it is ultimately from an Old Iranian compound *aspa-sti- "alfalfa, clover," from *aspa- "horse" (from PIE root *ekwo- "horse") + -sti- "food," from suffixed form of PIE root *ed- "to eat."
 also from 1845 

 Entries linking to alfalfa 

 *ed- 

 Proto-Indo-European root meaning "to eat," originally "to bite." 

 It might form all or part of: alfalfa ; anodyne ; comedo ; comestible ; eat ; edacious ; edible ; escarole ; esculent ; esurient ; etch ; ettin ; fret (v.); frass ; jotun ; obese ; obesity ; ort ; postprandial ; prandial .

 It might also be the source of: Sanskrit admi "I eat;" Avestan ad- "to eat;" Greek edo "I eat;" Latin edere "to eat;" Lithuanian ėdu "I eat," ėdžioti "to devour, bite;" Hittite edmi "I eat," adanna "food;" Armenian utem "I eat;" Old Church Slavonic jasti "to eat," Russian jest "to eat;" Old Irish ithim "I eat;" Gothic itan , Old Swedish and Old English etan , Old High German essan "to eat."

 *ekwo- 

 Proto-Indo-European root meaning "horse." Perhaps related to *ōku- "swift."

 It might form all or part of: alfalfa ; Eohippus ; equestrian ; equine ; equus ; hippo- ; hippocampus ; Hippocratic ; Hippocrene ; hippocrepian ; hippodrome ; hippogriff ; Hippolytus ; hippopotamus ; Philip ; philippic ; Philippines ; Xanthippe .

 It might also be the source of: Sanskrit açva- , Avestan aspa- , Greek hippos , Latin equus , Old Irish ech , Old Church Slavonic ehu- , Old English eoh , Gothic aihwa- all meaning "horse."

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 sativa 

 in scientific plant name classifications from late 18c., indicating a cultivated form, is from Latin sativus "cultivated, that is sown or planted," from satus, past participle of serere "to sow, plant seed" (from PIE root *sē-  "to sow"). Sative (adj.) formerly was used in E

 theory 

 1590s, "conception, mental scheme," from Late Latin theoria (Jerome), from Greek theōria "contemplation, speculation; a looking at, viewing; a sight, show, spectacle, things looked at," from theōrein "to consider, speculate, look at," from theōros "spectator," from thea "a view" 

 blackmail 

 1550s, "tribute paid to men allied with criminals as protection against pillage, etc.," from black (adj.) + Middle English male "rent, tribute." This is from Old English mal "lawsuit, terms, bargaining, agreement," from Old Norse mal "speech, agreement;" related to Old English mæ

 brute 

 early 15c., "of or belonging to animals, non-human," from Old French brut "coarse, brutal, raw, crude," from Latin brutus "heavy, dull, stupid, insensible, unreasonable" (source also of Spanish and Italian bruto), said to be an Oscan word, from PIE *gwruto-, suffixed form of root
###################### 3ad7d93151ff9988

Alcohol - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of alcohol 

 alcohol (n.) 

 1540s (early 15c. as alcofol ), "fine powder produced by sublimation," from Medieval Latin alcohol "powdered ore of antimony," from Arabic al-kuhul "kohl," the fine metallic powder used to darken the eyelids, from kahala "to stain, paint." The al- is the Arabic definite article, "the."

 Paracelsus (1493-1541) used the word to refer to a fine powder but also a volatile liquid. By 1670s it was being used in English for "any sublimated substance, the pure spirit of anything," including liquids.

 The sense of "intoxicating ingredient in strong liquor" is attested by 1753, short for alcohol of wine , which then was extended to the intoxicating element in fermented liquors. The formerly preferred terms for the substance were rectified spirits or brandy .

 In organic chemistry, the word was extended by 1808 to the class of compounds of the same type as this (a 1790 translation of Lavoisier's "Elements of Chemistry" has alkoholic gas for "the combination of alkohol with caloric").
 also from 1540s 

 Entries linking to alcohol 

 brandy (n.) 

 "spirits distilled from other liquors" (especially wine), 1650s, abbreviation of brandy-wine (1620s) from Dutch brandewijn "burnt wine," earlier brand-wijn , so called because it is distilled (compare German cognate Branntwein and Czech palenka "brandy," from paliti "to burn"). The Brandywine Creek in Pennsylvania, site of the 1777 Revolutionary War battle, supposedly was so named 17c. by the Dutch explorers for the color of its waters.

 In familiar use abbreviated as 
 brandy as early as 1657; but the fuller form was retained in official use (customs tariffs, acts of parliament, etc.) down to the end of 17th c., being latterly, as the spelling shows, regarded as a compound of 
 brandy + 
 wine . [OED]

 alcoholic (adj.) 

 1790, "of or pertaining to alcohol;" see alcohol + -ic . The meaning "caused by drunkenness" is attested by 1872; the meaning "habitually drunk" by 1910. The noun sense of "one who is addicted to drinking in excess, chronic drunkard, old rounder" is recorded from 1891; an earlier term for one was alcoholist (1877 in clinical writing, earlier in temperance literature this word simply meant "a drinker of alcohol"). Alcoholics Anonymous was founded 1935 in Akron, Ohio, U.S.

 alcoholism 
 chloral 
 gasohol 
 kohl 
 synovia 
 al- 
 -ol 
 See All Related Words (9) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 alcoholism 

 "disease of alcohol addiction," by 1882, from alcohol + -ism, or else from Modern Latin alcoholismus, coined in 1852 by Swedish professor of medicine Magnus Huss to mean what we now would call "alcohol poisoning, effects of excessive ingestion of alcohol." In earlier times, alcoh
###################### a4d7501a1c70bce5

Algorithm - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 

 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.

 About
 Who Did This 
 Sources 
 Introduction 
 Links 

 Support
 Premium 
 Patreon 
 Donate with PayPal 
 Merch 

 Apps

Get Chrome Extension 

Get iOS App 

Get Android App 

 Dark
 Auto
 Light

 Terms of Services Privacy Policy 

 English (English) 
 © 2001–2026 Douglas Harper & Talia Felix 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of algorithm 

 algorithm (n.) 

 1690s, "Arabic system of computation," from French algorithme , refashioned (under mistaken connection with Greek arithmos "number") from Old French algorisme "the Arabic numeral system" (13c.), from Medieval Latin algorismus , a mangled transliteration of Arabic al-Khwarizmi "native of Khwarazm" (modern Khiva in Uzbekistan), surname of the mathematician whose works introduced sophisticated mathematics to the West (see algebra ). The earlier form in Middle English was algorism (early 13c.), from Old French. The meaning broadened to any method of computation; from mid-20c. especially with reference to computing.
 also from 1690s 

 Entries linking to algorithm 

 algebra (n.) 

###################### c85b6a402cb6810f

Antimony - Etymology, Origin & Meaning 

 Search 
 Log in
```


## [2026-09-04T19:36:16.003Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in c85b6a402cb6810f 0070109655be6e11 0cf3e23ff5e8626b c2ab61cbb80fefe4; do echo \"###################### $f\"; grep -o \"Origin and history of.\\{0,2200\\}\" $f.txt | head -1 | tr -s ' '; echo; done"
}
```


### [2026-09-04T19:36:17.549Z] TOOL RESULT

```
###################### c85b6a402cb6810f
Origin and history of antimony 

###################### 0070109655be6e11
Origin and history of alkali 

###################### 0cf3e23ff5e8626b
Origin and history of arsenic 

###################### c2ab61cbb80fefe4
Origin and history of amalgam
```


## [2026-09-04T19:36:20.009Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in c85b6a402cb6810f 0070109655be6e11 0cf3e23ff5e8626b c2ab61cbb80fefe4; do echo \"###################### $f\"; awk '/Origin and history of/{p=1} p' $f.txt | tr -s ' ' | sed -n '1,22p'; done"
}
```


### [2026-09-04T19:36:21.683Z] TOOL RESULT

```
###################### c85b6a402cb6810f
 Origin and history of antimony 

 antimony (n.) 

 early 15c., "black antimony, antimony sulfide" (a powder used medicinally and in alchemy), from Old French antimoine and directly from Medieval Latin antimonium (11c.), a word of obscure origin.

 Probably it is a Latinization of later Greek stimmi "powdered antimony, black antimony" (a cosmetic used to paint the eyelids), from an Arabic source (such as al 'othmud ), unless the Arabic word is from the Greek and the Latin is from Arabic (which would explain the a- as the Arabic direct article al- ). Probably it is ultimately from Egyptian stm "powdered antimony;" the substance was used there as a cosmetic from at least 3000 B.C.E.

 In French, by folk etymology, it became anti-moine "monk's bane." As the name of a brittle metallic element in a pure form, it is attested in English from 1788. Its chemical symbol Sb is for Stibium , the Latin name for "black antimony," which word also was used in English for black antimony. Related: Antimonial ; antimoniac .
 also from early 15c. 

 Entries linking to antimony 

 stibial (adj.) 

 "like or resembling antimony," 1660s, with -al (1) + stibium , Latin for "black antimony," also used as a word in English. Alternative stibic (from Medieval Latin stibicus ) is from c. 1600. Compare antimony .

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 alcohol 
###################### 0070109655be6e11
 Origin and history of alkali 

 alkali (n.) 

 late 14c., "soda ash," from Medieval Latin alkali , from Arabic al-qaliy "the ashes, burnt ashes" (of saltwort, which abounds in soda due to growing in alkaline soils), from qala "to roast in a pan." Later extended to similar substances, natural or manufactured. The modern chemistry sense is from 1813.
 also from late 14c. 

 Entries linking to alkali 

 alkalescent (adj.) 

 "becoming or tending to become alkaline," 1732, from alkali + -escent . Related: Alkalescence .

 alkaline (adj.) 

 1670s, "pertaining to alkalis," from alkali + -ine (1). Of soils, from 1850. Related: Alkalinity .

 alkalize 
 alkaloid 
 potassium 
 See All Related Words (5) 

###################### 0cf3e23ff5e8626b
 Origin and history of arsenic 

 arsenic (n.) 

 late 14c., "yellow arsenic, arsenic trisulphide," from Old French arsenic , from Latin arsenicum , from late Greek arsenikon "arsenic" (Dioscorides; Aristotle has it as sandarakē ), adapted from Syriac (al) zarniqa "arsenic," from Middle Persian zarnik "gold-colored" (arsenic trisulphide has a lemon-yellow color), from Old Iranian *zarna- "golden" (from PIE root *ghel- (2) "to shine," with derivatives referring to bright materials and gold).

 The form of the Greek word is folk etymology, literally "masculine," from arsen "male, strong, virile" (compare arseno-koites "lying with men" in New Testament) supposedly in reference to the powerful properties of the substance. As an element, from 1812. The mineral (as opposed to the element) is properly orpiment , from Latin auri pigmentum , so called because it was used to make golden dyes. Related: Arsenical .

 ... se lo pueden comer las hormigas o le puede caer en la cabeza una gran langosta de arsenico ... [Lorca, on the poet overmastered by intellect]
 also from late 14c. 

 Entries linking to arsenic 

 *ghel- (2) 

 Proto-Indo-European root meaning "to shine;" it forms words for "gold" (the "bright" metal), words denoting colors, especially "yellow" and "green," also "bile, gall," for its color, and a large group of Germanic gl- words having to do with shining and glittering and, perhaps, sliding. Buck says the interchange of words for yellow and green is "perhaps because they were applied to vegetation like grass, cereals, etc., which changed from green to yellow."

 It might form all or part of: arsenic ; Chloe ; chloral ; chloride ; chlorinate ; chlorine ; chloro- ; chloroform ; chlorophyll ; chloroplast ; cholecyst ; choler ; cholera ; choleric ; cholesterol ; cholinergic ; Cloris ; gall (n.1) "bile, liver secretion;" gild ; glad ; glance ; glare ; glass ; glaze ; glazier ; gleam ; glee ; glib ; glide ; glimmer ; glimpse ; glint ; glissade ; glisten ; glister ; glitch ; glitter ; glitzy ; gloaming ; gloat ; gloss (n.1) "glistening smoothness, luster;" glow ; glower ; gold ; guilder ; jaundice ; melancholic ; melancholy ; yellow ; zloty .

 It might also be the source of: Sanskrit harih "yellow, tawny yellow," hiranyam "gold;" Avestan zari "yellow;" Old Persian daraniya- , Avestan zaranya- "gold;" Greek khlōros "greenish-yellow color," kholos "bile, gall, wrath;" Latin helvus "yellowish, bay," Gallo-Latin gilvus "light bay;" Lithuanian geltonas "yellow;" Old Church Slavonic zlutu , Polish żółty , Russian zeltyj "yellow;" Latin galbus "greenish-yellow," fellis "bile, gall;" Lithuanian žalias "green," želvas "greenish," tulžis "bile;" Old Church Slavonic zelenu , Polish zielony , Russian zelenyj "green;" Old Irish glass , Welsh and Breton glas "green," also "gray, blue;" Old English galla "gall, bile," geolu , geolwe , German gelb , Old Norse gulr "yellow;" Old Church Slavonic zlato , Russian zoloto , Old English gold , Gothic gulþ "gold;" Old English glæs "glass; a glass vessel."

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
###################### c2ab61cbb80fefe4
 Origin and history of amalgam 

 amalgam (n.) 

 c. 1400, "a blend of mercury with another metal; soft mass formed by chemical manipulation," from Old French amalgame or directly from Medieval Latin amalgama , "alloy of mercury (especially with gold or silver)," c. 1300, an alchemists' word, probably from Arabic al-malgham "an emollient poultice or unguent for sores (especially warm)" [Francis Johnson, "A Dictionary of Persian, Arabic, and English"], which is itself perhaps from Greek malagma "softening substance," from malassein "to soften," from malakos "soft" (from PIE *meldh- , from root *mel- (1) "soft"). The figurative meaning "compound of different things" is from 1790.
 also from c. 1400 

 Entries linking to amalgam 

 amalgamate (v.) 

 1650s, "mix (a metal) with mercury," a back-formation from amalgamation , or else from the obsolete adjective amalgamate (1640s) from amalgam (q.v.). Originally in metallurgy. The figurative transitive sense of "to unite" (races, etc.) is attested from 1802; the intransitive sense of "to combine, unite into one body" is from 1797. Related: Amalgamated ; amalgamating . Earlier verbs were amalgam (1540s); amalgamize (1590s).

 amalgamize (v.) 

 1590s, "reduce to a soft mass by combination with mercury," from amalgam + -ize . Related: Amalgamized ; amalgamizing .

 *mel- (1) 

 Proto-Indo-European root meaning "soft," with derivatives referring to soft or softened materials.

 It might form all or part of: amblyopia ; bland ; blandish ; blenny ; emollient ; enamel ; malacia ; malaxation ; malt ; melt ; mild ; Mildred ; milt ; moil ; mollify ; Mollusca ; mollusk ; mulch ; mullein ; mutton ; schmaltz ; smelt (v.); smelt (n.).
```


## [2026-09-04T19:36:27.914Z] TOOL CALL #49: Bash

```json
{
 "command": "for w in albatross alembic aubergine anil elixir alizarin algebra alchemy lute flute aloe apricot arsenal azimuth Gibraltar alcove Allah al- chemistry; do python3 tools/fetch_source.py \"https://www.etymonline.com/word/$w\" --note \"page 47, root Al 3, node word $w\" >/dev/null 2>&1 ; done; echo done"
}
```


### [2026-09-04T19:36:34.375Z] TOOL RESULT

```
done
```


## [2026-09-04T19:36:39.429Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nimport json,os,re\nidx=[json.loads(l) for l in open('index.jsonl')]\nwant={'albatross','alembic','aubergine','anil','elixir','alizarin','algebra','alchemy','lute','flute','aloe','apricot','arsenal','azimuth','Gibraltar','alcove','Allah','al-','chemistry'}\nfor r in idx:\n    m=re.search(r'etymonline.com/word/(.+)$', r['url'])\n    if m and m.group(1) in want:\n        t=open(r['file'] if os.path.isabs(r['file']) else r['file']).read()\n        seg=t.split('Origin and history of',1)\n        print('#####',m.group(1), r['url'], r.get('status'))\n        if len(seg)>1:\n            body=' '.join(seg[1].split())\n            print(body[:1300])\n        print()\nEOF"
}
```


### [2026-09-04T19:36:41.250Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'data/verification/sources/web/36b71d3f79e008e4.txt'
```


## [2026-09-04T19:36:45.576Z] TOOL CALL #51: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,os,re\nW='data/verification/sources/web'\nidx=[json.loads(l) for l in open(os.path.join(W,'index.jsonl'))]\nwant={'albatross','alembic','aubergine','anil','elixir','alizarin','algebra','alchemy','lute','flute','aloe','apricot','arsenal','azimuth','Gibraltar','alcove','Allah','al-','chemistry'}\nseen=set()\nfor r in idx:\n    m=re.search(r'etymonline.com/word/(.+)$', r['url'])\n    if m and m.group(1) in want and m.group(1) not in seen:\n        seen.add(m.group(1))\n        t=open(r['file']).read()\n        seg=t.split('Origin and history of',1)\n        print('#####',m.group(1), r.get('status'))\n        if len(seg)>1:\n            print(' '.join(seg[1].split())[:1100])\n        print()\nprint('missing:', want-seen)\nEOF"
}
```


### [2026-09-04T19:36:47.324Z] TOOL RESULT

```
##### alembic 200
alembic alembic (n.) "distillation vessel used in old chemistry," late 14c., earlier limbeck (mid-14c.), from Old French alambic (13c.), via Old Spanish, from Arabic al-anbiq "distilling flask," via Persian, from Greek ambix "cup," a word of unknown, possibly Semitic, origin. Often spelled limbeck 15c.-17c. The al- is the Arabic definite article, "the." also from late 14c. Entries linking to alembic lambic (n.) also lambick , kind of strong Belgian beer, 1829, related to French alambic "a still" (see alembic ). Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads. More to explore retort 1550s, "make return in kind" (especially of an injury), from Old French retort and directly from Latin retortus, past participle of retorquere "turn back, twist back, throw back," from re- "back" (see re-) + torquere "to twist" (from PIE root *terkw- "to twist"). Applied to excha virtue c. 1200, vertu, "moral life and conduct; a particular moral excellence," from Anglo-French and Old French vertu "force, strength, vigor; moral strength; qualities, ab

##### aloe 200
aloe aloe (n.) name of a group of shrubs or herbs with spiky flowers and thick leaves, yielding bitter juice which was used as a purgative drug, late 14c., originally in reference to the drug, from Latin aloe , from Greek aloē , which is of uncertain origin, probably a loan-word from an Oriental language. A secondary sense is older in English: "Fragrant resin or heartwood of an East Indian tree" (Old English alewe , aloe ), which is from misuse of Latin/Greek aloe in Biblical translations for Hebrew akhalim (plural), which ultimately is perhaps from a Dravidian language. OED says the Greek word probably was chosen for sound-resemblance to the Hebrew one. The word then was misapplied in 1680s to the American agave plant, which has a similar appearance (and also a Greek name) but is unrelated. The "true aloe" (producing the drug) consequently is called aloe vera (with Latin vera "true;" see very ). Related: Aloetic . also from late 14c. Entries linking to aloe agave (n.) American aloe plant, 1797, from Latin agave , from Greek agauē , proper name in mythology (mother of Pentheus), from

##### lute 200
lute lute (n.) stringed musical instrument, late 13c., from Old French lut , leut (Modern French luth ), from Old Provençal laut , a misdivision of Arabic al-'ud , the Arabian lute, literally "the wood" (source of Medieval Latin lutana , Spanish laud , Portuguese alaude , Italian liuto ), where al is the definite article. Dutch luit , German Laute , Danish luth are from Romanic. A player is a luter (Middle English), a lutist (1620s) or a lutanist (c. 1600, from Medieval Latin lutanista ). also from late 13c. Entries linking to lute lute-string (n.) 1520s, from lute (n.) + string (n.). luthier (n.) "lute-maker," 1879, from French luthier , from luth (see lute ). N oud See All Related Words (4) Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads. More to explore mandolin "lute-like musical instrument with four to six single or double metallic strings stretched over an almond-shaped body and...from Italian mandolino, diminutive of mandola, a larger kind of mandolin, altered from Late Latin pandura "three-stringed lute... lutose Hence 

##### flute 200
flute flute (n.) early 14c., floute , "(musical) flute, shepherd's pipe," from Old French flaut , flahute , fleute (12c.), from Old Provençal flaut , which is of uncertain origin. Perhaps imitative or from Latin flare "to blow" (according to Watkins, from PIE root *bhle- "to blow"); perhaps influenced by Provençal laut "lute." Other Germanic words (such as German flöte ) likewise are borrowings from French. Ancient flutes were direct, blown straight through a mouthpiece but held away from the player's mouth; the modern transverse or German flute developed 18c. The older style then sometimes were called flûte-a-bec (French, literally "flute with a beak"). The modern design and key system of the concert flute were perfected 1834 by Theobald Boehm. The architectural sense of "furrow in a pillar" (1650s) is from fancied resemblance to the inside of a flute split down the middle. The meaning "tall, slender wine glass" is by 1640s. also from early 14c. flute (v.) late 14c., flouten , "play upon the flute," from flute (n.). The meaning "to make (architectural) flutes" is from 1570s. Related

##### albatross 200
albatross albatross (n.) "large web-footed sea-bird of the petrel family," 1670s, probably from Spanish or Portuguese albatros , an alteration of alcatraz "web-footed sea-bird; cormorant," originally "pelican" (16c.). This name is perhaps from Arabic al-ghattas "sea eagle" [Barnhart]; or from Portuguese alcatruz "the bucket of a water wheel" [OED 1989], from Arabic al-qadus "machine for drawing water, jar" (which is said to be from Greek kados "jar"). If the second, the name would be a reference to the pelican's pouch (compare Arabic saqqa "pelican," literally "water carrier"). The spelling was influenced by Latin albus "white." The name was extended by 17c. English sailors to a larger sea-bird (order Tubinares ), which is not found in the North Atlantic. [In English the word also formerly was extended to the frigate-bird.] These albatrosses follow ships for days without resting and were held in superstitious awe by sailors. The figurative sense of "burden" (by 1936) is from Coleridge's "Rime of the Ancient Mariner" (1798) about a sailor who shoots an albatross and then is forced to 

##### aubergine 200
aubergine aubergine (n.) "fruit of the eggplant" ( Solanum esculentum ), 1775, from French aubergine , from Catalan alberginera (showing typical change of al- to au- in French), from Arabic al-badinjan "the eggplant" (source also of Spanish alberengena , 15c.), from Persian badin-gan , from Sanskrit vatigagama . The plant, native to Southeast Asia, was unknown to the ancients and introduced to the Mediterranean by the Arabs. As the name of a color like that of the eggplant fruit, it is attested from 1895. also from 1775 Entries linking to aubergine eggplant (n.) also egg-plant , plant cultivated for its large oblong or ovate fruit, which is highly esteemed as a vegetable, 1763, from egg (n.) + plant (n.). Originally of the white variety. Compare aubergine . Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads. More to explore herb c. 1300, erbe "non-woody plant," especially a leafy vegetable used for human food, from Old French erbe "grass, herb, plant fed to animals" (12c., Modern French herbe), from Latin herba "grass, an herb; he

##### anil 200
anil anil (n.) West Indian shrub from which indigo is made, 1580s, from French or Portuguese anil "the indigo shrub," from Arabic an-nil "the indigo," assimilated from al-nil , from Persian nila , ultimately from Sanskrit nili "indigo," from nilah "dark blue." also from 1580s Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads. More to explore indigo 17c. spelling change of indico (1550s), "blue powder obtained from certain plants and used as a dye," from Spanish indico, Portuguese endego, and Dutch (via Portuguese) indigo, all from Latin indicum "indigo," from Greek indikon "blue dye from India," literally "Indian (substance aniline colorful dyes, 1843, coined 1841 by German chemist Carl Julius Fritzsche and adopted by Hofmann, ultimately from Portuguese anil... dey Old English dæge "female servant, woman who handles food in a household, housekeeper," from Proto-Germanic *daigjon (source also of Old Norse deigja "maid, female servant," Swedish deja "dairymaid"), from PIE root *dheigh- "to form, build." Now obsolete (though OED say

##### elixir 200
elixir elixir (n.) mid-13c., from Medieval Latin elixir "philosopher's stone," believed by alchemists to transmute baser metals into gold and/or to cure diseases and prolong life, from Arabic al-iksir "the philosopher's stone," probably from late Greek xerion "powder for drying wounds," from xeros "dry" (see xerasia ). Later in medical use for "a tincture with more than one base." General sense of "strong tonic" is 1590s; used for quack medicines from at least 1630s. also from mid-13c. Entries linking to elixir xerasia (n.) "excessive dryness of hair," 1706, medical Latin, from Greek xerasia "dryness," from xeros "dry, withered" (see xero- ). Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads. More to explore philosopher , a reputed solid substance supposed by alchemists to change baser metals into gold or silver; also identified with the elixir... nostrum c. 1600, "a medicine made of secret ingredients by secret methods," but commonly "quack medicine," from Latin nostrum remedium "our remedy" (or some similar phrase), presumably 

##### alizarin 200

##### algebra 200
algebra algebra (n.) "formal mathematics; the analysis of equations; the art of reasoning about quantitative relations by the aid of a compact and highly systematized notation," 1550s, from Medieval Latin algebra , from Arabic "al-mukhtasar fi hisab al-jabr wa al-muqabala" ("the compendium on calculation by restoring and balancing"), the title of the famous 9c. treatise on equations by Baghdad mathematician Abu Ja'far Muhammad ibn Musa al-Khwarizmi. Arabic al jabr ("in vulgar pronunciation, al-jebr " [Klein]) "reunion of broken parts" (reducing fractions to integers in computation) was one of the two preparatory steps to solving algebraic equations; it is from Arabic jabara "reintegrate, reunite, consolidate." Al-Khwarizmi's book (translated into Latin in 12c.) also introduced Arabic numerals to the West. John Dee (16c.) calls the work algiebar and almachabel . The accent shifted 17c. from second syllable to first. The same word was used in English 15c.-16c. to mean "bone-setting," as was Medieval Latin algebra , a usage picked up probably from Arab medical men in Spain. also from 15

##### alchemy 200
alchemy alchemy (n.) "medieval chemistry; the supposed science of transmutation of base metals into silver or gold" (involving also the quest for the universal solvent, quintessence, etc.), mid-14c., from Old French alchimie (14c.), alquemie (13c.), from Medieval Latin alkimia , from Arabic al-kimiya , from Greek khemeioa (found c.300 C.E. in a decree of Diocletian against "the old writings of the Egyptians"), all meaning "alchemy," and of uncertain origin. Perhaps from an old name for Egypt ( Khemia , literally "land of black earth," found in Plutarch), or from Greek khymatos "that which is poured out," from khein "to pour," from PIE root *gheu- "to pour" [Watkins, but Klein, citing W. Muss-Arnolt, calls this folk etymology]. The word seems to have elements of both origins. Mahn ... concludes, after an elaborate investigation, that Gr. khymeia was probably the original, being first applied to pharmaceutical chemistry, which was chiefly concerned with juices or infusions of plants; that the pursuits of the Alexandrian alchemists were a subsequent development of chemical study, and th

##### apricot 200
apricot apricot (n.) roundish, orange-colored, plum-like fruit, 1550s, abrecock , from Catalan abercoc , related to Portuguese albricoque , from Arabic al-birquq , through Byzantine Greek berikokkia which is probably from Latin (mālum) praecoquum "early-ripening (fruit)" (see precocious ). The form has been assimilated to French abricot . Latin praecoquis early-ripe, can probably be attributed to the fact that the fruit was considered a variety of peach that ripened sooner than other peaches .... [Barnhart] Native to the Himalayas, it was introduced in England in 1524. The older Latin name for it was prunum Armeniacum or mālum Armeniacum , in reference to supposed origin in Armenia. As a color name, by 1906. also from 1550s Entries linking to apricot precocious (adj.) 1640s, "developed or ripe before the usual time," originally of plants, with -ous + Latin praecox (genitive praecocis ) "maturing early," from prae "before" (see pre- ) + coquere "to ripen," literally "to cook" (from PIE root *pekw- "to cook, ripen"). Originally of flowers or fruits. Figurative use, of persons, dates, e

##### arsenal 200
arsenal arsenal (n.) c. 1500, "dockyard, dock with naval stores," from Italian arzenale , from Arabic dar as-sina'ah "workshop," literally "house of manufacture," from dar "house" + sina'ah "art, craft, skill," from sana'a "he made." The word was applied by the Venetians to a large wharf in their city, and English picked it up in this sense. The meaning "public place for making or storing weapons and ammunition" is from 1570s. The London football club (1886) was named for the Royal Arsenal , Woolwich, where the original players worked. also from c. 1500 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads. More to explore armory c. 1300, armurie, "arms and weapons collectively; defensive armor;" see arm (n.2) + -ory and compare Old French armeurerie, armoirie. The meaning "place where arms are manufactured" is from mid-15c. (see armor + -y (1)). Also in Middle English as "arsenal, storehouse of weapons" flirt To flirt a fan (1660s) was to snap it open or closed with a brisk jerk and was long considered part of the coquette's arsenal

##### azimuth 200
azimuth azimuth (n.) "arc marking the distance of a star from the north or south point of the meridian," late 14c., from Old French azimut , from Arabic as-sumut "the ways," plural of as-samt "the way, direction" (see zenith ). Related: Azimuthal . also from late 14c. Entries linking to azimuth zenith (n.) "point of the heavens directly overhead at any place," late 14c., zineth , from Old French cenith (Anglo-French zenith , Modern French zénith ) and directly from Medieval Latin zyneth , zymeth , cenit , senit , bungled scribal transliterations of Arabic samt "road, path," abbreviation of samt ar-ras , literally "the way over the head." Letter -m- misread as -ni- . The Medieval Latin word could as well be influenced by the rough agreement of the Arabic term with classical Latin semita "sidetrack, side path" (notion of "thing going off to the side"), from se- "apart" + *mi-ta- , a suffixed form of PIE root *mei- (1) "to change, go, move." The figurative sense of "highest point or state" of anything capable of having one is from c. 1600. Related: Zenithal . *mei- (1) Proto-Indo-Europe

##### Gibraltar 200
Gibraltar Gibraltar 1590s, ancient Calpe , captured 710 C.E. by Saracen leader Tariq, renamed Jebel el Tarik "the Mountain of Tarik," hence the English name. A British possession since 1704. Figurative of impregnability by 1856. Formerly also the name of a kind of rock-candy (1831). also from 1590s Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads. More to explore prudential Prudential, the U.S. insurance company, dates to the 1870s; its logo featuring the Rock of Gibraltar dates from c. 1900 and... ape The only native apes in Europe are the Barbary apes of Gibraltar, intelligent and docile, and these were the showman's apes... pillar The Pillars of Hercules are the two hills on opposite sides of the Straits of Gibraltar, Abyla in Africa and Calpe in Europe... Europe from Latin Europa "Europe," from Greek Europe, which is of uncertain origin; as a geographic name first recorded in the Homeric hymn to Apollo (522 B.C.E. or earlier): "Telphusa, here I am minded to make a glorious temple, an oracle for men, and hither they will alwa

##### alcove 200
alcove alcove (n.) "vaulted recess," 1670s, from French alcôve (17c.), from Spanish alcoba , from Arabic al-qobbah "the vaulted chamber," from Semitic base q-b-b "to be bent, crooked, vaulted." The al- is the Arabic definite article, "the." also from 1670s Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads. More to explore bay "inlet, recess in the shore of a sea or lake," c. 1400, from Old French baie, Late Latin baia (source of Spanish and Portuguese bahia, Italian baja), which is perhaps ultimately from Iberian (Celtic) bahia...."opening in a wall," especially a space between two columns, late 14c. dinette "small room or alcove set aside for meals," 1930, from dine + diminutive (or false French) suffix -ette.... cubicle mid-15c., "bedroom, bedchamber," from Latin cubiculum "bedroom," from cubare "to lie down," which is perhaps from a PIE *kub-, with cognates in Middle Welsh kyscu, Middle Cornish koska, Middle Breton cousquet "to sleep," but de Vaan regards the PIE origin of the Latin word as "un stall [place in a stable for ani

##### Allah 200
Allah Allah Arabic name for the Supreme Being, 1702, Alha , from Arabic Allah , contraction of al-Ilah , literally "the God," from al "the" + Ilah "God," which is cognate with Aramaic elah , Hebrew eloah (see Elohim ). also from 1702 Entries linking to Allah Elohim a name of God in the Bible, c. 1600, from Hebrew, plural (of majesty?) of Eloh "God" (cognate with Allah ), a word of unknown etymology, perhaps an augmentation of El "God," also of unknown origin. Generally taken as singular, the use of this word instead of Yahveh is taken by biblical scholars as an important clue to authorship in the Old Testament, hence Elohist (1830; Elohistic is from 1841), title of the supposed writer of passages of the Pentateuch where the word is used. Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads. More to explore kismet Allah kehrim!' (God hath willed it! God is great!) [Dr. James O.... Hezbollah Lebanon, founded c. 1982, from Persian hezbollah, Arabic hizbullah, literally "Party of God," from hezb/hizb "party" + allah... algebra "formal m

##### al- 200
al- al- in words from Arabic (or assumed to be), it is the definite article "the." Sometimes rendered in English as el- . Often assimilated to following consonants ( as- , az- , ar- , am- , an- , etc.). Examples include almanac , alchemy , alcohol , algebra . Entries linking to al- alchemy (n.) "medieval chemistry; the supposed science of transmutation of base metals into silver or gold" (involving also the quest for the universal solvent, quintessence, etc.), mid-14c., from Old French alchimie (14c.), alquemie (13c.), from Medieval Latin alkimia , from Arabic al-kimiya , from Greek khemeioa (found c.300 C.E. in a decree of Diocletian against "the old writings of the Egyptians"), all meaning "alchemy," and of uncertain origin. Perhaps from an old name for Egypt ( Khemia , literally "land of black earth," found in Plutarch), or from Greek khymatos "that which is poured out," from khein "to pour," from PIE root *gheu- "to pour" [Watkins, but Klein, citing W. Muss-Arnolt, calls this folk etymology]. The word seems to have elements of both origins. Mahn ... concludes, after an elaborate 

##### chemistry 200
chemistry chemistry (n.) c. 1600, "alchemy," from chemist + -ry ; also see chemical (adj.). The meaning "natural physical process" is from 1640s; the sense of "scientific study of the composition of material things and the changes they undergo" is by 1788. Chemistry in the European mind disengaged itself from alchemy in the mid-1600s; The Academy del Cimento was established in Italy in 1657, the Royal Society in London in 1660, and the Academy of Sciences in Paris in 1666. The figurative sense of "instinctual attraction or affinity" is also attested by c. 1600, from the alchemical sense. also from c. 1600 Entries linking to chemistry chemical (adj.) 1570s, "relating to chemistry, pertaining to the phenomena with which chemistry deals," from chemic "of alchemy" (a worn-down derivative of Medieval Latin alchimicus ; see alchemy ) + -al (1). In early use also of alchemy. Related: Chemically . Chemical warfare is attested from 1917. chemist (n.) 1560s, chymist , "alchemist," from French chimiste , from Medieval Latin chimista , reduced from alchimista (see alchemy ). The modern spelling 

missing: set()
```


## [2026-09-04T19:37:05.001Z] TOOL CALL #52: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/alizarin\" \"https://en.wiktionary.org/wiki/%D9%81%D8%B5%D9%81%D8%B5%D8%A9\" \"https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D9%86%D9%8A%D8%AE\" \"https://en.wiktionary.org/wiki/%D8%A7%D9%84%DA%A9%D9%84\" \"https://en.wiktionary.org/wiki/%D8%A2%D9%86%D8%AA%DB%8C%D9%85%D9%88%D8%A7%D9%86\" \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B0%D9%86%D8%AC%D8%A7%D9%86\" \"https://en.wiktionary.org/wiki/%D8%A5%D8%AB%D9%85%D8%AF\"; do python3 tools/fetch_source.py \"$u\" --note \"page 47, root Al 3\" >/dev/null 2>&1; done; echo done"
}
```


### [2026-09-04T19:37:09.532Z] TOOL RESULT

```
done
```


## [2026-09-04T19:37:13.038Z] TOOL CALL #53: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,os,re\nW='data/verification/sources/web'\nidx=[json.loads(l) for l in open(os.path.join(W,'index.jsonl'))]\nfor r in idx:\n    if 'wiktionary' in r['url']:\n        t=open(r['file']).read()\n        print('#####', r['url'], r.get('status'), len(t))\n        # find Etymology sections\n        for m in re.finditer(r'Etymology.{0,900}', t, re.S):\n            print(' '.join(m.group(0).split())[:850]); print('---')\n            break\n        print()\nEOF"
}
```


### [2026-09-04T19:37:14.612Z] TOOL RESULT

```
<persisted-output>
Output too large (181.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b3uwwg29b.txt

Preview (first 2KB):
##### https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D8%AF%DB%8C%D8%B3 200 4993
Etymology 1.2 Pronunciation 1.3 Noun 1.3.1 Descendants 1.4 Proper noun 2 Punjabi Toggle Punjabi subsection 2.1 Etymology 2.2 Pronunciation 2.3 Noun 2.3.1 Declension 2.4 Further reading Toggle the table of contents پردیس 9 languages العربية বাংলা فارسی Kurdî Malagasy پنجابی Русский سرائیکی 中文 Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Cite this page Get shortened URL Print/export Create a book Download as PDF Printable version In other projects Appearance move to sidebar hide From Wiktionary, the free dictionary Persian [ edit ] Persian Wikipedia has an article on: پردیس Wikipedia fa
---

##### https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/birk- 200 5305
Etymology 1.2 Noun 1.2.1 Reconstruction notes 1.2.2 Inflection 1.2.3 Descendants Toggle the table of contents Reconstruction:Proto-Semitic/ birk- Add languages Reconstruction Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read Edit View history General What links here Related changes Upload file Permanent link Page information Get shortened URL Print/export Download as PDF Printable version In other projects Appearance move to sidebar hide From Wiktionary, the free dictionary This Proto-Semitic entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence. Proto-Semitic [ edit ] Etymology [ edit ] Often compared to Egyptian bꜣk and to C
---

##### https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%83%D8%A9 200 12827
...
</persisted-output>
```


## [2026-09-04T19:37:22.623Z] TOOL CALL #54: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,os,re,urllib.parse\nW='data/verification/sources/web'\nidx=[json.loads(l) for l in open(os.path.join(W,'index.jsonl'))]\nwant=['alizarin','%D9%81%D8%B5%D9%81%D8%B5%D8%A9','%D8%B2%D8%B1%D9%86%D9%8A%D8%AE','%D8%A7%D9%84%DA%A9%D9%84','%D8%A2%D9%86%D8%AA%DB%8C%D9%85%D9%88%D8%A7%D9%86','%D8%A8%D8%A7%D8%B0%D9%86%D8%AC%D8%A7%D9%86','%D8%A5%D8%AB%D9%85%D8%AF']\nseen=set()\nfor r in idx:\n    for w in want:\n        if r['url'].endswith('/'+w) and w not in seen:\n            seen.add(w)\n            t=open(r['file']).read()\n            print('#####', urllib.parse.unquote(w), r.get('status'), len(t))\n            i=t.find('From Wiktionary, the free dictionary')\n            print(' '.join(t[i:i+2500].split()))\n            print()\nprint('missing', set(want)-seen)\nEOF"
}
```


### [2026-09-04T19:37:24.143Z] TOOL RESULT

```
##### alizarin 200 691
x

##### فصفصة 200 6210
From Wiktionary, the free dictionary Arabic [ edit ] Noun [ edit ] فَصْفَصَة or فِصْفِصَة • ( faṣfaṣa or fiṣfiṣa ) f ( singulative , collective فَصْفَص m ( faṣfaṣ ) or فِصْفِصَ m ( fiṣfiṣa ) , plural فَصَافِص ( faṣāfiṣ ) ) singulative of فِصْفِص ( fiṣfiṣ ) alternative form of فِصْفِص ( fiṣfiṣ ) Declension [ edit ] Declension of noun فَصْفَصَة ( faṣfaṣa )‎; فِصْفِصَة ( fiṣfiṣa ) singulative singulative triptote in ـَة ( -a ) indefinite definite construct informal فَصْفَصَة ‎; فِصْفِصَة faṣfaṣa ‎; fiṣfiṣa الْفَصْفَصَة ‎; الْفِصْفِصَة al-faṣfaṣa ‎; al-fiṣfiṣa فَصْفَصَة ‎; فِصْفِصَة faṣfaṣat ‎; fiṣfiṣat nominative فَصْفَصَةٌ ‎; فِصْفِصَةٌ faṣfaṣatun ‎; fiṣfiṣatun الْفَصْفَصَةُ ‎; الْفِصْفِصَةُ al-faṣfaṣatu ‎; al-fiṣfiṣatu فَصْفَصَةُ ‎; فِصْفِصَةُ faṣfaṣatu ‎; fiṣfiṣatu accusative فَصْفَصَةً ‎; فِصْفِصَةً faṣfaṣatan ‎; fiṣfiṣatan الْفَصْفَصَةَ ‎; الْفِصْفِصَةَ al-faṣfaṣata ‎; al-fiṣfiṣata فَصْفَصَةَ ‎; فِصْفِصَةَ faṣfaṣata ‎; fiṣfiṣata genitive فَصْفَصَةٍ ‎; فِصْفِصَةٍ faṣfaṣatin ‎; fiṣfiṣatin الْفَصْفَصَةِ ‎; الْفِصْفِصَةِ al-faṣfaṣati ‎; al-fiṣfiṣati فَصْفَصَةِ ‎; فِصْفِصَةِ faṣfaṣati ‎; fiṣfiṣati collective basic collective triptote indefinite definite construct informal فَصْفَص ‎; فِصْفِص faṣfaṣ ‎; fiṣfiṣ الْفَصْفَص ‎; الْفِصْفِص al-faṣfaṣ ‎; al-fiṣfiṣ فَصْفَص ‎; فِصْفِص faṣfaṣ ‎; fiṣfiṣ nominative فَصْفَصٌ ‎; فِصْفِصٌ faṣfaṣun ‎; fiṣfiṣun الْفَصْفَصُ ‎; الْفِصْفِصُ al-faṣfaṣu ‎; al-fiṣfiṣu فَصْفَصُ ‎; فِصْفِصُ faṣfaṣu ‎; fiṣfiṣu accusative فَصْفَصًا ‎; فِصْفِصًا faṣfaṣan ‎; fiṣfiṣan الْفَصْفَصَ ‎; الْفِصْفِصَ al-faṣfaṣa ‎; al-fiṣfiṣa فَصْفَصَ ‎; فِصْفِصَ faṣfaṣa ‎; fiṣfiṣa genitive فَصْفَصٍ ‎; فِصْفِصٍ faṣfaṣin ‎; fiṣfiṣin الْفَصْفَصِ ‎; الْفِصْفِصِ al-faṣfaṣi ‎; al-fiṣfiṣi فَصْفَصِ ‎; فِصْفِصِ faṣfaṣi ‎; fiṣfiṣi dual indefinite definite construct informal فَصْفَصَتَيْن ‎; فِصْفِصَتَيْن faṣfaṣatayn ‎; fiṣfiṣatayn الْفَصْفَصَتَيْن ‎; الْفِصْفِصَتَيْن al-faṣfaṣatayn ‎; al-fiṣfiṣatayn فَصْفَصَتَيْ ‎; فِصْفِصَتَيْ faṣfaṣatay ‎; fiṣfiṣatay nominative فَصْفَصَتَانِ ‎; فِصْفِصَتَانِ faṣfaṣatāni ‎; fiṣfiṣatāni الْفَصْفَصَتَانِ ‎; الْفِصْفِصَتَانِ al-faṣfaṣatāni ‎; al-fiṣfiṣatāni فَصْفَصَتَا ‎; فِصْفِصَتَا faṣfaṣatā ‎; fiṣfiṣatā accusative فَصْفَصَتَيْنِ ‎; فِصْفِصَتَيْنِ faṣfaṣatayni ‎; fiṣfiṣatayni الْفَصْفَصَتَيْنِ ‎; الْفِصْفِصَ

##### زرنيخ 200 4610
From Wiktionary, the free dictionary Arabic [ edit ] Chemical element ( edit ) As Atomic number 33 زِرْنِيخ ( zirnīḵ ) Classification data Period 4 Group 15 Block p-block Class metalloid Previous: ← جِرْمَانْيُوم ( jirmānyum ) (Ge) Next: سِيلِينْيُوم ( silīnyum ) (Se) → Arabic Wikipedia has an article on: زرنيخ Wikipedia ar Alternative forms [ edit ] زَرْنِيق ( zarnīq ) Etymology [ edit ] Etymology tree Proto-Indo-European *ǵʰelh₃- Proto-Indo-European *ǵʰl̥h₃enyom der. Proto-Indo-Iranian *ȷ́ʰr̥Hanyam Proto-Iranian *jr̥Hanyam Old Median *zaranyam Old Median *kā Old Median *zaraniyakā der. Middle Persian *zarnīk bor. Classical Syriac ܙܪܢܝܟܐ ( zarnīḵā ) der. Arabic زرنيخ From Middle Persian [script needed] ( zarnīk ) or [script needed] ( zarīk , “ golden ” ) . Compare Persian زرنی ( zarni , “ orpiment ” ) . Pronunciation [ edit ] IPA ( key ) : /zir.niːx/ Noun [ edit ] زِرْنِيخ • ( zirnīḵ ) m arsenic Declension [ edit ] Declension of noun زِرْنِيخ ( zirnīḵ ) singular basic singular triptote indefinite definite construct informal زِرْنِيخ zirnīḵ الزِّرْنِيخ az-zirnīḵ زِرْنِيخ zirnīḵ nominative زِرْنِيخٌ zirnīḵun الزِّرْنِيخُ az-zirnīḵu زِرْنِيخُ zirnīḵu accusative زِرْنِيخًا zirnīḵan الزِّرْنِيخَ az-zirnīḵa زِرْنِيخَ zirnīḵa genitive زِرْنِيخٍ zirnīḵin الزِّرْنِيخِ az-zirnīḵi زِرْنِيخِ zirnīḵi Descendants [ edit ] → Middle Armenian: զառնեխ ( zaṙnex ) , զառնիխ ( zaṙnix ) , զռնեխ ( zṙnex ) ( or from Persian ) → Maltese: żarnieq , żernieq not to be confused with żerniq Retrieved from " https://en.wiktionary.org/w/index.php?title=زرنيخ&oldid=92436046 " Categories : ar:Chemical elements ar:Metalloids ar:Period 4 elements ar:Pnictogens ar:P-block elements Arabic terms derived from Old Median Arabic terms derived from Middle Persian Arabic terms derived from Proto-Indo-Iranian Arabic terms derived from Proto-Iranian Arabic terms derived from Proto-Indo-European Arabic terms derived from the Proto-Indo-European root *ǵʰelh₃- Arabic terms derived from Classical Syriac Arabic terms borrowed from Middle Persian Arabic 2-syllable words Arabic terms with IPA pronunciation Arabic lemmas Arabic nouns Arabic masculine nouns Arabic nouns with basic triptote singular Hidden categories: Arabic terms with non-redundant manual transliterations

##### الکل 200 3389
From Wiktionary, the free dictionary Persian [ edit ] Persian Wikipedia has an article on: الکل Wikipedia fa Etymology [ edit ] Etymology tree Akkadian 𒎎𒋆𒁉𒍣𒁕 ( guḫlum ) bor. Aramaic כוחלא ( kuḥlā ) bor. Arabic كُحْل ( kuḥl ) Andalusian Arabic كُحُول ( kuḥūl ) bor. Medieval Latin alcohol lbor. French alcool bor. Persian الکل Borrowed from French alcool , from Arabic الْكُحُل ( al-kuḥul ) (a direct boring from Arabic would drop the definite article ال ( al- ) ), see there for more. Doublet of کحل ( kuhl / kohl ) and الکحل ( alkuhul / alkohol ) . Pronunciation [ edit ] ( Iran, formal ) IPA ( key ) : [ʔæl.kʰól̥] Readings Iranian reading ? alkol Noun [ edit ] الکل • ( alkol ) ( plural الکل‌ها ( alkol-hâ ) ) ( Iran ) alcohol Related terms [ edit ] الکلی ( alkoli ) Retrieved from " https://en.wiktionary.org/w/index.php?title=الکل&oldid=90946392 " Categories : Persian terms derived from Akkadian Persian terms derived from the Arabic root ك ح ل Persian terms derived from Aramaic Persian terms derived from Medieval Latin Persian terms borrowed from French Persian terms derived from Arabic Persian terms derived from French Persian terms derived from Andalusian Arabic Persian doublets Persian terms with IPA pronunciation Persian lemmas Persian nouns Iranian Persian fa:Organic chemistry Hidden categories: Pages with etymon Persian entries with etymon Pages with etymology trees Persian entries with etymology trees Arabic terms with redundant transliterations Pages with entries Pages with 1 entry This page was last edited on 26 May 2026, at 03:43. Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Privacy policy About Wiktionary Disclaimers Legal & safety contacts Code of Conduct Developers Statistics Cookie statement Mobile view Search Search Toggle the table of contents الکل 8 languages Add topic

##### آنتیموان 200 3335
From Wiktionary, the free dictionary Persian [ edit ] Chemical element ( edit ) Sb Atomic number 51 آنتیموان Classification data Period 5 Group 15 Block p-block Class metalloid Previous: ← قلع , اَرزیز (Sn) Next: تلوریم (Te) → Persian Wikipedia has an article on: آنتیموان Wikipedia fa Etymology [ edit ] Etymology tree Egyptian sdm der. Ancient Greek στίμμι ( stímmi ) der. Coptic ⲉⲥⲑⲏⲙ ( esthēm ) bor. Arabic إِثْمِد ( ʔiṯmid ) bor. Latin antimonium der. French antimoine bor. Persian آنتیموان Borrowed from French antimoine . Pronunciation [ edit ] ( Iran, formal ) IPA ( key ) : [ân̪t̪ʰiː.mo.ʔǽn] Readings Iranian reading ? ântimo'an Noun [ edit ] آنتیموان • ( ântimo'an ) ( Iran ) antimony Retrieved from " https://en.wiktionary.org/w/index.php?title=آنتیموان&oldid=92400511 " Categories : fa:Chemical elements fa:Metalloids fa:Period 5 elements fa:Pnictogens fa:P-block elements Persian terms derived from Latin Persian terms derived from Ancient Greek Persian terms derived from Arabic Persian terms borrowed from French Persian terms derived from Coptic Persian terms derived from French Persian terms derived from Egyptian Persian terms with IPA pronunciation Persian lemmas Persian nouns Iranian Persian Hidden categories: Pages with etymon Persian entries with etymon Pages with etymology trees Persian entries with etymology trees Persian entries with etymology texts Pages using etymon with no ID Pages with entries Pages with 1 entry This page was last edited on 30 August 2026, at 23:19. Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Privacy policy About Wiktionary Disclaimers Legal & safety contacts Code of Conduct Developers Statistics Cookie statement Mobile view Search Search Toggle the table of contents آنتیموان 3 languages Add topic

##### باذنجان 200 8017
From Wiktionary, the free dictionary See also: بادنجان Arabic [ edit ] Alternative forms [ edit ] بَاتِنْجَان ( bātinjān ) , بَتِنْجَان ( batinjān ) , بِدِنْجَان ( bidinjān ) Etymology [ edit ] Etymology tree Proto-Dravidian *waẓVtV der. Sanskrit वातिङ्गण ( vātiṅgaṇa ) bor. Classical Persian بَاذِنْگَان ( bāzingān ) bor. Arabic باذنجان Borrowed from Classical Persian بَاذِنْگَان ( bāzingān ) , بَاتِنْگَان ( bātingān ) , an Indo-Aryan borrowing, from Sanskrit वातिङ्गण ( vātiṅgaṇa ) , from Dravidian , ultimately from Proto-Dravidian *waẓVtV . Pronunciation [ edit ] IPA ( key ) : /baː.ðin.d͡ʒaːn/ Noun [ edit ] بَاذِنْجَان • ( bāḏinjān ) m ( collective ) eggplant , aubergine Declension [ edit ] Declension of noun بَاذِنْجَان ( bāḏinjān ) singular basic singular triptote indefinite definite construct informal بَاذِنْجَان bāḏinjān الْبَاذِنْجَان al-bāḏinjān بَاذِنْجَان bāḏinjān nominative بَاذِنْجَانٌ bāḏinjānun الْبَاذِنْجَانُ al-bāḏinjānu بَاذِنْجَانُ bāḏinjānu accusative بَاذِنْجَانًا bāḏinjānan الْبَاذِنْجَانَ al-bāḏinjāna بَاذِنْجَانَ bāḏinjāna genitive بَاذِنْجَانٍ bāḏinjānin الْبَاذِنْجَانِ al-bāḏinjāni بَاذِنْجَانِ bāḏinjāni Descendants [ edit ] Egyptian Arabic: بتنجان ( betengān ) , برنجان ( berengān ) Gulf Arabic: بيذيان ( bēḏyān ) , بيديان ( bēdyān ) Hijazi Arabic: بادنجان ( bādinjān ) , باتنجان ( bātinjān ) Maltese: brunġiel , brinġiel Moroccan Arabic: دنجال ( danjāl ) , دنجان ( danjān ) , دمنجال ( dmanjāl ) , دمنجان ( dmanjān ) , بودنجال ( būdanjāl ) Najdi Arabic: بيذجان ( bēḏjān ) , بذنجان ( baḏinjān ) Borrowings: → Asturian: berenxena → Azerbaijani: badımcan → Banjarese: balinjan ( “ tomato ” ) → Italian: petonciano ( regional ) → Mandailing Batak: balinjan → Middle Armenian: պատինճան ( patinčan ) , պանջան ( panǰan ) , պատընճ ( patənč ) , պատընճան ( patənčan ) , պատընջան ( patənǰan ) , պատնիճան ( patničan ) , պատնճան ( patnčan ) , պատնջան ( patnǰan ) , պորինճան ( porinčan ) , վադրճան ( vadrčan ) , վարճան ( varčan ) Armenian: բադրիջան ( badriǰan ) , բադրջան ( badrǰan ) , բադինջան ( badinǰan ) , բադիրջան ( badirǰan ) , բադումջան ( badumǰan ) , բալդըրջան ( baldərǰan ) , պաթլիջան ( patʻliǰan ) , պատըլճան ( patəlčan ) , պատըրջան ( patərǰan ) , պատիծան ( patican ) , պատիճան ( patičan ) , պատինճան ( patinčan ) , պատնճան ( patnčan ) , պատնչան ( patnčʻan ) , պատնջան ( patnǰan ) , պատր

##### إثمد 200 4880
From Wiktionary, the free dictionary Arabic [ edit ] Chemical element ( edit ) Sb Atomic number 51 إِثْمِد ( ʔiṯmid ) Classification data Period 5 Group 15 Block p-block Class metalloid Previous: ← قَصْدِير ( qaṣdīr ) (Sn) Next: تِيلُورْيُوم ( tilūryum ) (Te) → Arabic Wikipedia has an article on: إثمد Wikipedia ar Etymology [ edit ] Etymology tree Egyptian sdm der. Ancient Greek στίμμι ( stímmi ) der. Coptic ⲉⲥⲑⲏⲙ ( esthēm ) bor. Arabic إثمد By form a metathesis away from Coptic ⲉⲥⲑⲏⲙ ( esthēm ) , though derivation from an unattested oblique δ ( d ) form of Ancient Greek στίμμι ( stímmi ) has been suggested, ultimately from Egyptian sdm , possibly also conflated with Egyptian msdmt . Pronunciation [ edit ] IPA ( key ) : /ʔiθ.mid/ Noun [ edit ] إِثْمِد • ( ʔiṯmid ) m antimony , antimony ore antimony powder ointment , kohl Declension [ edit ] Declension of noun إِثْمِد ( ʔiṯmid ) singular basic singular triptote indefinite definite construct informal إِثْمِد ʔiṯmid الْإِثْمِد al-ʔiṯmid إِثْمِد ʔiṯmid nominative إِثْمِدٌ ʔiṯmidun الْإِثْمِدُ al-ʔiṯmidu إِثْمِدُ ʔiṯmidu accusative إِثْمِدًا ʔiṯmidan الْإِثْمِدَ al-ʔiṯmida إِثْمِدَ ʔiṯmida genitive إِثْمِدٍ ʔiṯmidin الْإِثْمِدِ al-ʔiṯmidi إِثْمِدِ ʔiṯmidi Synonyms [ edit ] ( antimony or antimony powder ) : كُحْل ( kuḥl ) , أَنْتِيمُون ( ʔantīmūn ) , رَاسُخْت ( rāsuḵt ) , تمونية ( timūnya ) ( Egyptian Arabic ) Descendants [ edit ] → Latin: antimonium Catalan: antimoni French: antimoine Galician: antimonio Italian: antimonio Portuguese: antimónio , antimônio ( Brazil ) Romanian: antimoniu Spanish: antimonio → English: antimony References [ edit ] “ إثمد ” in Almaany Fraenkel, Siegmund ( 1886 ), Die aramäischen Fremdwörter im Arabischen (in German), Leiden: E. J. Brill, page 153 Wehr, Hans with Kropfitsch, Lorenz ( 1985 ), “ إثمد ”, in Arabisches Wörterbuch für die Schriftsprache der Gegenwart ‎ [1] (in German), 5th edition, Wiesbaden: Otto Harrassowitz, published 2011 , →ISBN , page 7 Retrieved from " https://en.wiktionary.org/w/index.php?title=إثمد&oldid=92400454 " Categories : ar:Chemical elements ar:Metalloids ar:Period 5 elements ar:Pnictogens ar:P-block elements Arabic terms derived from Ancient Greek Arabic terms borrowed from Coptic Arabic terms derived from Egyptian Arabic ter

missing set()
```


## [2026-09-04T19:37:44.043Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\nfor p in 'Alambic' 'Albatros' 'Aubergine|Berengena' 'Alcali' 'Azimut' 'Alcove|Alcôve' 'Abricot' 'Arsenal' 'Amiral' 'Elixir|Élixir' 'Alchimie' 'Algebre|Algèbre' ; do echo \"###DEV $p\"; python3 $S DEV.txt \"^$p|\\b$p\\b\" 380 1; done"
}
```


### [2026-09-04T19:37:46.830Z] TOOL RESULT

```
###DEV Alambic
--- [ffpage 32] 'Her- belot. Bibliothèque orient, au mot aschrajioun.^ Alambic Esp. alamhique, port, lamhique, itai. lambico, de l'arabe (^^^^j^î al-anhiq, venant du grec a^^i^^ vase à distiller, précédé de l'article arabe al. Alancabuth. Terme d'astronomie. Partie de l'astrolabe. De l'arabe ci^^-aX^x)! al-anhahoût, dont le sens propre est l'araignée. L'alancabutli, en effet, rappelle assez bien l'idée d'une
###DEV Albatros
--- [ffpage 32] né l'espagnol alharazo et le portugais alvaraz.. **•" Albatros. Ce mot, écni aJgatroa par Flacourt et Dam- pier, est une altération de l'espagnol et portugais rt/c^fraz^ qui désigne le pélican onocrotale, mais fjui a été appliqué à plusieurs autres oiseaux aquatiques (entre autres au petit cormoran). Je ne doute pas qu'il ne faille l'assimiJer au portugais alcatniz, signifiant seau cVu
###DEV Aubergine|Berengena
--- [ffpage 73] (petite ou- tarde) fut notre première victime ^. ?' Aubergine. L'aubergine est une plante originaire de l'Orient, ainsi que l'atteste Dominique Ghabré qui, dans son Stirpium icônes (1678), l'appelle Melongena Arabum et ajoute : «Melongena in Arabum codicibus primum cele- brata fuit. 75 Le nom arabe-persan ^L^^L hâdindjân serait assez difficile à reconnaître dans notre aubergine, si nous
###DEV Alcali
--- [ffpage 33] e ce mot, comme étymologie, avec alcaide. Voy. Caïd. Alcali. Esp. et port, alcali. De l'arabe JkiJÎ al-qali, cendres de soude ou la plante elle-même. Dans certaines régions du midi de la France, on réserve le nom de caliou aux cendres de sarments
###DEV Azimut
NO MATCH DEV.txt ^Azimut|\bAzimut\b
###DEV Alcove|Alcôve
--- [ffpage 40] sages où on l'a traduit par lire. ?5 (E. Renan ^) AlcÔve. Esp. alcoba, portug. alcova, ital. alcova, alcovo; de l'arabe aIaJ! al-qohha, qui, entre autres sens, a celui de petite chambre, cabinet, ainsi que le montre M. Lane (jTAc thousand and one Nights, I, 281). Voir l'intéressant article de M. Dozy, Gloss. p. 90, ()i. Le mot est employé avec son sens le plus ordinaire dans
###DEV Abricot
--- [ffpage 28] t plusieurs espèces de sterne, sans citer Vaboumras. Abricot. La curieuse histoire de ce mot a été faite par Diez, Mahn, Dozy. Parti du \Riin prœcox, précoce, passé chez les Grecs sous la forme TspaiKOKKiov, il a été adopté par les Arabes, qui en ont fait , avec l'article , ^yvîJî al-har- qoïiq ou al-birqoûq. Puis il est revenu dans les langues romanes : alharcoqiie, alvarcoque,
###DEV Arsenal
--- [ffpage 20] précédemment émises sur des termes comme artichaut, arsenal, avanie, avarie, caraque, escarpin, nuque, siroc, etc. L'examen de quelques ouvrages scientifiques arabes, dont les tra- ductions latines étaient fort répandues au moyen âge, mais dont le texte arabe n'a jamais été publié, ' Les noms arabes de plantes, de drogues, etc.
###DEV Amiral
--- [ffpage 58] i soit-il. Les Musulmans disent de même ^j-ç«î amïn. Amiral. Aucun étymologiste ne doute que ce ne soit là le mot arabe •A^î amïr, commandant, émir. Mais la termi- naison al a paru d'autant plus embarrassante qu'on la re- trouve dans le portugais amiralh, l'italien almiragUo, am- miraglio, et sous d'autres formes dans l'ancien espagnol ahnirage, l'espagnol moderne almirante, le bas lat
###DEV Elixir|Élixir
--- [ffpage 40] xemple d'un changement pareil dans le sens moderne ^'élixir. (Voy. ce mot.) ^ Les anciens, Pline, Vitruve, Gaiien, confondent sans cesse le cinabre et le minium. Dans le Dioscoride latin do J. Ruel ( i5i6), celle confusion est relevée en ces termes : « Argentum vivuni lit ex minio , qiiod abusive cin- vabaris dicilur.55 (Lib. V, cap. ci, fol. 820 recto.) Dans ce passage, c'est p
###DEV Alchimie
--- [ffpage 14] arabes de mathématiques, d'astronomie, de médecine, d'alchimie. Ce sont des faits connus de tous et qui justifient pleinement la recherche, dans l'arabe, de toute étymologie française, dont le latin, le germa- nique, le celtique ne peuvent rendre compte. Ces recherches, à vrai dire, sont parfois bien scabreuses. La richesse, ou plutôt le chaos, je ne dis pas de la langue, mais des l
###DEV Algebre|Algèbre
--- [ffpage 44] cle d'Engel- mann sur ce mot (^GJoss. p. 129, laS). Algèbre. Esp. portug. et ital. aJgebra. De l'arabe jj^A aJ-djehr, réduction. On nomme l'algèbre icLjUUî^ -^4 i^ science des réductions et des comparaisons. En espagnol, aJge- Jmsta se dit du bailleul ou rebouteur, qui réduit les frac- tures. r Algénib. Etoile 7 de la constellation de Pégase, sur le flanc du cheval. De l'arabe t^xil
```


## [2026-09-04T19:37:54.159Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py DEV.txt \"Amiral\\. Aucun\" 1600 1"
}
```


### [2026-09-04T19:37:55.896Z] TOOL RESULT

```
NO MATCH DEV.txt Amiral\. Aucun
```


## [2026-09-04T19:37:58.454Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py DEV.txt \"Amiral\" 1700 1"
}
```


### [2026-09-04T19:38:00.038Z] TOOL RESULT

```
--- [ffpage 58] i soit-il. Les Musulmans disent de même ^j-ç«î amïn. Amiral. Aucun étymologiste ne doute que ce ne soit là le mot arabe •A^î amïr, commandant, émir. Mais la termi- naison al a paru d'autant plus embarrassante qu'on la re- trouve dans le portugais amiralh, l'italien almiragUo, am- miraglio, et sous d'autres formes dans l'ancien espagnol ahnirage, l'espagnol moderne almirante, le bas latin admi- ralius, admirallus, amiraldus, admiratus, amirarius, ami- randus , admirandiis , admirantius , amireda, amirœus, etc. Engelmann avait supposé que le «/final était l'article pré- cédant un mot tombé depuis, par exemple ^ bahr, mer: amir-al-bahr, commandant de la mer, serait devenu amir- al tout court '^. Cette explication, au moins quant au mot bahr, ne semble guère admissible, vu qu'on a de nombreux exemples du Roman d'Alexandre, du Roman de Rou, de Garin, cVAiibery^, qui prouvent ([uamiraut, amirant, amiratz, ' Dioscoridœ pharmacorum lihri VIIl , 1629, fol. h6 verso. Marcello Ver- jjilio dit aussi : «Succinum , quod electrum veteres, nostri ambram dicunt.?i Ihid. ïo\. /j7 recto. Ces commentateurs rangent sous la même dénomination l'ambre jaune
```


## [2026-09-04T19:38:51.457Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###KLN alizari\"; python3 $S KLN_1966.txt \"alizari, n\" 600 1\necho \"###GPL al article\"; python3 $S GPL.txt \"Arabic article|al-|the article ال\" 400 4\necho \"###MON المثنی\"; python3 $S MON_part2.txt \"المثنی|المثنى|مثنی\" 250 2"
}
```


### [2026-09-04T19:38:53.262Z] TOOL RESULT

```
###KLN alizari
NO MATCH KLN_1966.txt alizari, n
###GPL al article
--- [ffpage 25] shortened in pronunciation when immediately followed by the Arabic article (§ 13, ). Rem. c. Native grammarians and lexicographers generally call the initial spiritus lenis (\ alif) of any Persian or Arabic word alif+- magstra ‘short alif’. §8. Tanwin. The marks of the short vowels, when doubled, are generally pronounced with the addition of the sound z (represented in English by 2), as — an, — in, — un. This is called tanwin (تنوین)‎ or ‘nunation’ (from t
--- [ffpage 27] called ‘solar letters’ Gone cane hurif-i- ری‎ or Pao وف‎ yl al-hurifu ’sh-shamsiya), because the word شمش‎ ‘sun’ happens to begin with one of them ; and = remaining Weber of ae Arabic alphabet, ‘lunar letters’ وف 325 مربه)‎ = hurif-i- gamariya or ال وف مر‎ al-hurifu ’l-qgamariya), because the word قمر مر‎ gamar ‘ moon ’ begins with one of them. § 11. Hamza. a. The spiritus lenis, or hamza رهمزه)‎ signifying ‘compression’, i.e. of the larynx), is a mark * w
--- [ffpage 27] nar letters’ وف 325 مربه)‎ = hurif-i- gamariya or ال وف مر‎ al-hurifu ’l-qgamariya), because the word قمر مر‎ gamar ‘ moon ’ begins with one of them. § 11. Hamza. a. The spiritus lenis, or hamza رهمزه)‎ signifying ‘compression’, i.e. of the larynx), is a mark * which, in Arabic words, is placed over the consonant, \, or over the consonants و‎ and ی‎ when they stand in place of |; as es » .ی‎ But the name hamza is commonly applied to the epee with the mark
--- [ffpage 191] e verbs causal. action تال بر فاد IV ast‏ Prefixing‏ hamzat al-‏ gat to the basic form. MEANING OF THE BASIC FORM
###MON المثنی
--- [ffpage 0] از آستم. جر متصر فت (صرفت ( آن است که در ر صورت لکد کات و مثنی و جمع» همیشه در حالت واحدی باشد. فعل غیرمتصرف: (صرف ع.) آن است که تمام مشتقات از آن نیاید. متصف: 0۱۵۱۱۵5:۲ [ع (امف.) صفت کر ده سل ۵. بسچ ۱۱0۱۱۸5۵1 [ع.] (افا.) دارندة ۱ 1 [ع. .| (افا.) ) تأمل کننده تظر کننده؛ ملاحظه کننده؛ ج. متصفحین.
--- [ffpage 0] گویند. منظومه‌ای که به شوه مننوی سروده شده؟ ج. متتو بات. مثنی : 2 [ع. ]| (۱.) دو زانو و دو مرفق ستور (غم.) (مت.) تار دوم از عود؛ ج. متانی. (ق.) دو دی دو تا دو تا. متنی : ۳۵ (امف.) دو کرده شده. دو برابر مه ما 5 له تستنمه شده. حرفی که دارای دو نقطه است. دوباره آورده. مکرر. مثنی : ()1 :۱02 [ع.] دو تا
```


## [2026-09-04T19:39:04.953Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###KLN alizari\"; python3 $S KLN_1966.txt \"alizari\" 500 1\necho \"###LKT isara full\"; python3 $S LKT.txt \"isära|i.ära.*Saft|al-.i.ära\" 700 2"
}
```


### [2026-09-04T19:39:06.951Z] TOOL RESULT

```
###KLN alizari
--- [ffpage 38] d11, ‘step, stair’, ma'ldh, ‘upward’. Cp. Alenu, Eli. alizari, n., madder root. — F., fr. Sp. alizari, fr. Arab. al-'a$draK, ‘the juice’, fr. al-, ‘the’, and a?ara, ‘he squeezed, pressed’, which is rel. to Heb. ‘atzar, Aram.-Syr. ‘dtzdr, ‘he retained’, alizarin, alizarine, n., a dye (chem.) — F. ali¬ zarine, fr. alizari. See prec. word and chem. suff. -in, -ine. aljama, n., a Jewish congregation in Spain. — Sp., fr. Arab. al-jamd'ah, fr. al-, ‘the’, and ja- md'a’', ‘assembly’, fr. jama'
###LKT isara full
--- [ffpage 53] . [Giov. Romani, Sinonimi italiani I, 251. 315. Ar. bisära: 'Gute Nachricht'; hieraus mit ar. Art. sp. albricias 'Geschenk für eine gute Nachricht', Vb. albriciar; pg. alvi^aras 'Trinkgeld, Botenlohn', alvigareiro 'an- genehmer Bote; einer, der Trinkgeld spenden will'. [DE 74. Eguilaz 118. ML 970. 316. Ar. bitäna: 'Futter eines Kleides oder eines Stiefels' [vgl. hier Nr. 273 b], in Ägypten mit vulgärer Vokalisation butäna [A. Nallino, L'arabo parlato in Egitto, S. 288]; hier- aus siz. butana 'Rockfutter'. — Ferner mit leichtem Bedeutungswandel sp. pg. 27 [Tk. bilir-. hadana 'gegerbtes Schaf leder', pg. 'altes mageres Schaf, it. hasana, baszana 'ge- gerbtes Hammelfeir, kat.
```


## [2026-09-04T19:39:15.713Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###FSD1 admiral\"; python3 $S FSD_vol1.txt \"amir-al-bahr|amir al bahr|amîr-al\" 400 3\necho \"###WEB admiral\"; python3 $S WEB_vol1.txt \"amir-al-bahr|amir al-bahr|emir al bahr\" 400 3\necho \"###FSD alfalfa\"; python3 $S FSD_vol1.txt \"alfalfa\" 300 2"
}
```


### [2026-09-04T19:39:18.875Z] TOOL RESULT

```
###FSD1 admiral
NO MATCH FSD_vol1.txt amir-al-bahr|amir al bahr|amîr-al
###WEB admiral
NO MATCH WEB_vol1.txt amir-al-bahr|amir al-bahr|emir al bahr
###FSD alfalfa
--- [ffpage 99] are omitted. AD*riww>a'riwis n -ni 7^1 a fnmuw »« alfalfa almond apple, a.-peeler apricot artichoke asparagus aveler avocado awner jumper kibbling-machine kumquat land-marker, 1.- parlng machine lawn-mower lemon lentil dumping-reel ear-lifter endive ensilage fan fence-jack fence-post driver fencing-machine fertilizer, f.-dis- lettuce ax trlb
--- [ffpage 165] fumery. Forms of Antiiracnose. N\me. Description, etc. Alfalfa-a CoUctotrichum trlfolii Apple-a A very destructive disease of the fruit, twigs, and branches of the apple, caused by Gfrrosporlum fructigenum (conldlal stage of Glomerella rufomaculans) Avocada*a A disease of the leaf, Colletotrichum glczo- s par tot des Be
```


## [2026-09-04T19:39:26.426Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###AHD alfalfa\"; python3 $S AHD_watkins1985.txt \"alfalfa\" 500 4\necho \"###AHD arsenic\"; python3 $S AHD_watkins1985.txt \"arsenic\" 400 3"
}
```


### [2026-09-04T19:39:28.337Z] TOOL RESULT

```
###AHD alfalfa
NO MATCH AHD_watkins1985.txt alfalfa
###AHD arsenic
--- [ffpage 51] c zarnikd, orpiment: ARSENIC. III. Words denoting bile. 1. Suffixed o-grade form “ghol-no- in Germanic *gallon-, bile, in Old English gealla, gall: GALL!. 2. Suffixed o-grade form *ghol-& in Greek kholé, bile: CHOLE-, CHOLER, (CHOL- ERA); ACHOLIA, MELANCHOLY. 3. Suffixed full-grade form *ghel-n- in Latin fel, bile: FELON?. IV. A range of Germanic words (where no preforms are given, the words are late creations). 1. Ge
--- [ffpage 113] - ARRIERE-BAN koro- ARRIVE rei-1 ARROGATE reg-1 ARROW arku- ARSENIC ghel-2 ARSIS wer-2 ARSON as- ART! ar- ART? er-1 ARTEL ar- ARTERIO- wer-2 ARTERIOLE wer-2 ARTERY wer-2 ARTHRO- ar- ARTHUR rtko- ARTICLE ar- ARTIFACT dhé-1 ARTIFICE dhé-1 ARTIODACTYL ar- ARTISAN ar- ARTIST ar- ARYAN aryo- ASBESTOS gWes- ASCEND skand- ASCRIBE skribh- ASH! as- ASH? os- ASININE asinus ASK ais- ASPECT spek- ASPEN apsa ASPERSE (s)preg- ASPIRATE spirare Ass? ors- ASSAI? Sa- ASSAIL
```


## [2026-09-04T19:39:33.232Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py\necho \"###AHD ghel2 arsenic ctx\"; python3 $S AHD_watkins1985.txt \"zarnikd, orpiment\" 900 1\necho \"###AHD ekwo\"; python3 $S AHD_watkins1985.txt \"^ekwo-|ekwo-\\.\" 700 3"
}
```


### [2026-09-04T19:39:34.885Z] TOOL RESULT

```
###AHD ghel2 arsenic ctx
--- [ffpage 51] c zarnikd, orpiment: ARSENIC. III. Words denoting bile. 1. Suffixed o-grade form “ghol-no- in Germanic *gallon-, bile, in Old English gealla, gall: GALL!. 2. Suffixed o-grade form *ghol-& in Greek kholé, bile: CHOLE-, CHOLER, (CHOL- ERA); ACHOLIA, MELANCHOLY. 3. Suffixed full-grade form *ghel-n- in Latin fel, bile: FELON?. IV. A range of Germanic words (where no preforms are given, the words are late creations). 1. Germanic *glaimiz in Old English glém, bright light, gleam: GLEAM. 2. Middle High Ger- man glimsen, to gleam, akin to the source of Middle English glimsen, to glimpse: GLIMPSE. 3. Swedish dialec- tal glinta, to shine, akin to the source of Middle English glent, a glint: GLINT. 4. Swedish glimra, akin to the source of Middle English glimeren, to glimmer: GLIM- MER. 5. Old Norse glitra, to shine: GLITTER. 6. Old English glisnian, to shine: GLISTEN. 7. Middle Dutch glisteren, to sh
###AHD ekwo
--- [ffpage 23] name may underlie the common Indo-European word for horse, ekwo-. The expansion and migration of the Indo- European-speaking peoples in the later third and early second millennia B.c. is intimately bound up with the diffusion of the horse. The verbal root deme-?, “to force,” acquired the special sense of “‘to tame horses,” whence English TAME. Stock was a source and meas- ure of wealth; the original sense of peku- was probably “wealth, riches,” as in Latin pecu- nia, whence “wealth in cattle” and finally “cattle” proper. The same evolution from the general to the particular may be observed in the root neud-, “to make use of,” whence English NEAT?. The verbal roots pa-, “to protect,” and k“el-', “to revolve, move around,” are widely used for the noti
--- [ffpage 46] - in Old English is, ice: ICE; ICICLE. [Pok. 2. ei-s- 301.] ekwo-. Horse. Possibly originally derived from kwon-. 1. Latin equus, horse: EQUESTRIAN, EQUINE, EQUITANT, (EQUITATION); EQUISETUM. 2. Greek hippos, horse: EO- HIPPUS, HIPPOCAMPUS, HIPPOGRIFF, HIPPOPOTAMUS. [Pok. ekuo-s 301.] el-1. Elbow, forearm. Extended o-grade form *olind, elbow, in: a. Germanic “alind in Old English ein, fore- arm, cubit: ELL?; b. Germanic compound *alino-bugén-, “bend of the forearm,” elbow (*bugén-, bend, bow; see bheug-’), in Old English elnboga, elbow: ELBOW; c. Lat- in ulna, forearm: ULNA; d. lengthened variant form *6lena in Greek dlené, elbow: OLECRANON, [Pok. 8. el- 307.] el-2. Red, brown (forming animal and tree names). 1. Ex- el-? tended form *elmo- in Germani
```


## [2026-09-04T19:39:40.189Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://ahdictionary.com/word/indoeurop.html\" --note \"page 47, root Al 3: AHD IE roots appendix, checking ekwo-/ed- for alfalfa\" 2>&1 | tail -2"
}
```


### [2026-09-04T19:39:42.227Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/24cd7948c66bfb96.txt
```


## [2026-09-04T19:39:44.709Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -c 24cd7948c66bfb96.txt && grep -io \"alfalfa.\\{0,200\\}\" 24cd7948c66bfb96.txt | head -3; grep -o \"ekwo-.\\{0,300\\}\" 24cd7948c66bfb96.txt | head -2"
}
```


### [2026-09-04T19:39:46.282Z] TOOL RESULT

```
526309 24cd7948c66bfb96.txt
alfalfa , from Old Iranian *-sti‑ , food, in compound. *aspa-sti‑ clover, alfalfa ("horse food") ( *aspa‑ , horse; see ekwo- ).
alfalfa , from Old Iranian *aspa‑ , horse.
ekwo- ).
ekwo-
```


## [2026-09-04T19:39:50.141Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -o \".\\{400\\}alfalfa , from Old Iranian \\*-sti.\\{100\\}\" 24cd7948c66bfb96.txt | head -1 | tr -s ' '"
}
```


### [2026-09-04T19:39:52.171Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:39:55.016Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 -c \"\nt=open('24cd7948c66bfb96.txt',encoding='utf-8',errors='replace').read()\ni=t.find('alfalfa , from Old Iranian *-sti')\nprint(' '.join(t[max(0,i-700):i+260].split()))\nprint('=====')\nj=t.find('alfalfa , from Old Iranian *aspa')\nprint(' '.join(t[max(0,j-500):j+200].split()))\n\""
}
```


### [2026-09-04T19:39:56.936Z] TOOL RESULT

```
o devour; frass , from Old High German frezzan , to devour. Both (i) and (ii) from Germanic compound *fra-etan , to eat up ( *fra‑ , completely; see per 1 ). a-d all from Germanic *etan . edacious , edible , escarole , esculent , esurient ; comedo , comestible , obese , from Latin edere , to eat. prandial , from Latin compound prandium , lunch, probably from *prām-(e)d-yo‑ , "first meal," *prām‑ , first; see per 1 . Suffixed form *ed-un-o‑ . jotun , from Old Norse jötunn , giant, jotun, from Germanic idunaz (perhaps < "immense eater" or "man-eating giant"). Suffixed form *ed-un-ā‑ . anodyne , pleurodynia , from Greek odunē , pain (< "gnawing care"). Suffixed zero-grade form *əd-ti‑ . alfalfa , from Old Iranian *-sti‑ , food, in compound. *aspa-sti‑ clover, alfalfa ("horse food") ( *aspa‑ , horse; see ekwo- ). Samoyed , from Russian -ed , eater. [Pokorny ed‑ 287.] See also derivative dent- . ‌ ‌ eg I. Nominative form of the personal
=====
ng madness. Suffixed form *eis-mo . Asmodeus , from Avestan aēšma‑ , anger. [Pokorny 1. eis‑ 299.] ‌ ‌ ekwo- Horse. Probably to be segmented *ekw-o‑ , a suffixed form akin to the lengthened o-grade adjective ōku- , swift. Oldest form h 1 ek̑wo‑ , becoming ekwo‑ in centum languages. equestrian , equid , equine , equitant , equitation , Equuleus ; equisetum , from Latin equus , horse. eohippus , hippocampus , Hippocrene , hippodrome , hippogriff , hippopotamus , from Greek hippos , horse. alfalfa , from Old Iranian *aspa‑ , horse. [Pokorny ek̑u̯o-s 301.] ‌ ‌ el- Elbow, forearm. Extended form *el-inā‑ , elbow. ell 2 , from Old English eln , forearm, cubit, from Germanic *elinō ; e
```


## [2026-09-04T19:40:11.712Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,os\nW='data/verification/sources/web'\nfor r in [json.loads(l) for l in open(os.path.join(W,'index.jsonl'))]:\n    if r['fetched'].startswith('2026-09-04T19:3') or r['fetched'].startswith('2026-09-04T19:4'):\n        print(r.get('status'), r.get('bytes'), r['url'])\nEOF"
}
```


### [2026-09-04T19:40:13.399Z] TOOL RESULT

```
200 8608 https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%AF
200 4207 https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hr%CC%A5Ht%C3%A1h
200 6165 https://en.wiktionary.org/wiki/%E1%BC%84%CE%BB%CE%B5%CF%85%CF%81%CE%BF%CE%BD
200 3636 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82elh%E2%82%81-
200 17713 https://en.wiktionary.org/wiki/%E1%BC%80%CE%BB%CE%AD%CF%89
200 4280 https://en.wiktionary.org/wiki/aleurone
200 3715 https://en.wiktionary.org/wiki/%D8%A2%D9%88%D8%A7%D8%B1%D9%87
200 2996 https://en.wiktionary.org/wiki/%D8%A2%D9%88%D8%A7%D8%B1
200 5981 https://en.wiktionary.org/wiki/%D5%A1%D6%82%D5%A1%D6%80
200 11226 https://en.wiktionary.org/wiki/ambulo
200 3712 https://en.wiktionary.org/wiki/exsul
200 3904 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82elh%E2%82%82-
200 6965 https://www.etymonline.com/word/alley
200 7421 https://www.etymonline.com/word/exile
200 394 https://www.vajehyab.com/dehkhoda/%D8%A2%D9%88%D8%A7%D8%B1%D9%87
200 6385 https://www.etymonline.com/word/admiral
200 6820 https://www.etymonline.com/word/alfalfa
200 6743 https://www.etymonline.com/word/alcohol
200 7291 https://www.etymonline.com/word/algorithm
200 6274 https://www.etymonline.com/word/antimony
200 5371 https://www.etymonline.com/word/alkali
200 7933 https://www.etymonline.com/word/arsenic
200 6984 https://www.etymonline.com/word/amalgam
200 6588 https://www.etymonline.com/word/albatross
200 5614 https://www.etymonline.com/word/aubergine
200 5196 https://www.etymonline.com/word/anil
200 5303 https://www.etymonline.com/word/elixir
200 554 https://www.etymonline.com/word/alizarin
200 7125 https://www.etymonline.com/word/algebra
200 6859 https://www.etymonline.com/word/alchemy
200 6823 https://www.etymonline.com/word/apricot
200 4719 https://www.etymonline.com/word/arsenal
200 7369 https://www.etymonline.com/word/azimuth
200 4994 https://www.etymonline.com/word/Gibraltar
200 5169 https://www.etymonline.com/word/alcove
200 5482 https://www.etymonline.com/word/Allah
200 8096 https://www.etymonline.com/word/al-
200 5641 https://www.etymonline.com/word/chemistry
200 5095 https://en.wiktionary.org/wiki/alizarin
200 6053 https://en.wiktionary.org/wiki/%D9%81%D8%B5%D9%81%D8%B5%D8%A9
200 4453 https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D9%86%D9%8A%D8%AE
200 3239 https://en.wiktionary.org/wiki/%D8%A7%D9%84%DA%A9%D9%84
200 3157 https://en.wiktionary.org/wiki/%D8%A2%D9%86%D8%AA%DB%8C%D9%85%D9%88%D8%A7%D9%86
200 7846 https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B0%D9%86%D8%AC%D8%A7%D9%86
200 4730 https://en.wiktionary.org/wiki/%D8%A5%D8%AB%D9%85%D8%AF
```


## [2026-09-04T19:40:19.847Z] TOOL CALL #68: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,os\nW='data/verification/sources/web'\nfor r in [json.loads(l) for l in open(os.path.join(W,'index.jsonl'))]:\n    if any(k in r['url'] for k in ['/lute','/flute','/aloe']):\n        print(r['fetched'], r.get('status'), r.get('bytes'), r['url'])\nEOF\necho \"--- alizarin wikt\"; python3 -c \"\nimport json,os\nW='data/verification/sources/web'\nfor r in [json.loads(l) for l in open(os.path.join(W,'index.jsonl'))]:\n    if r['url'].endswith('/alizarin') and 'wiktionary' in r['url']:\n        t=open(r['file']).read(); i=t.find('From Wiktionary'); print(' '.join(t[i:i+1200].split()))\n\""
}
```


### [2026-09-04T19:40:21.561Z] TOOL RESULT

```
2026-09-04T18:38:10Z 200 6540 https://www.etymonline.com/word/aloe
2026-09-04T18:38:10Z 200 4842 https://www.etymonline.com/word/lute
2026-09-04T18:38:10Z 200 5884 https://www.etymonline.com/word/flute
--- alizarin wikt
From Wiktionary, the free dictionary See also: Alizarin English [ edit ] English Wikipedia has an article on: alizarin Wikipedia Alternative forms [ edit ] alizarine Etymology [ edit ] Borrowed from French alizarine , corresponding to alizari +‎ -in . Pronunciation [ edit ] ( UK ) IPA ( key ) : /əˈlɪzəɹɪn/ Noun [ edit ] alizarin ( countable and uncountable , plural alizarins ) ( organic chemistry ) A red substance, 1,2-dihydroxyanthraquinone, extracted from madder root and used as a dye . 1946 , Elizabeth Bishop , “Roosters”, in North and South : glass headed pins, oil-golds and copper greens, anthracite blues, alizarins, 2010 , Siddhartha Mukherjee , The Emperor of all Maladies , Fourth Estate, published 2011 , page 82 : In 1883, the German output of alizarin , the brilliant red chemical that imitated natural carmine, reached twelve thousand tons, dwarfing the amount being produced by Perkin's factory in London. Derived terms [ edit ] alizaric alizarin crimson alizarin red diacetylalizarin naphthazarin nitroalizarin quinizarin Translations [ edit ] 1,2-dihydroxyanthraquinone Chinese: Mandarin: 茜素 (zh) ( q
```


## [2026-09-04T19:41:11.669Z] AGENT

Now I have enough material. Let me write the verification file.


## [2026-09-04T19:47:01.023Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nE = \"https://www.etymonline.com/word/\"\nW = \"https://en.wiktionary.org/wiki/\"\nAHD_ONLINE = \"https://ahdictionary.com/word/indoeurop.html\"\n\ndef rc(ref, status, note): return {\"ref\": ref, \"status\": status, \"note\": note}\ndef co(src, where, stance, note): return {\"src\": src, \"where\": where, \"stance\": stance, \"note\": note}\n\nNOT_SAP = rc(\"SAP:43\", \"not_checked\",\n    \"Sayyah's Farhang (Persian translation of al-Munjid) exists only as a paid ebook (fidibo 142427/142430); refs_online.json lists kind='purchase', no scan, so p.43 could not be read.\")\nNOT_OEW = rc(\"OEW\", \"not_checked\",\n    \"Shipley, The Origins of English Words, is lending-only on archive.org (originsofenglish0000ship / originsofenglish00jose); djvu.txt returns 401, so it could not be consulted.\")\nNOT_VOP = rc(\"VOP\", \"not_checked\",\n    \"Moshiri, Farhang-e vazheha-ye orupayi dar farsi (Alborz 1371) — refs_online.json kind='none': no scan, no ebook, no catalogue copy found anywhere.\")\nMON_PARTIAL = rc(\"MON\", \"partial\",\n    \"Only the 2-vol Adena abridgement of Mo'in is on disk (MON_part1.txt/MON_part2.txt, no page breaks), so Nourai's volume/page cannot be checked; the headwords themselves are there — see the consulted entry.\")\n\nnodes = []\n\n# ---------------- node 1 ----------------\nnodes.append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"(script only) الله ، الکل ، المثنّی\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian has no definite article of its own; what it has are whole Arabic phrases taken over unanalysed with ال al- still attached. الله allāh < al-ilāh 'the god' (the ه of the Persian pronunciation allâh is the Arabic form exactly); الکل al-koll 'the whole, the totality' (Arabic al-kull, the abstract used in Persian philosophical/administrative idiom, e.g. الکل فی الکل); المثنّی al-mothannā 'the doubled one, the dual' (passive participle of Arabic ثنّى thannā 'to double', also a proper name). In all three the article is inseparable in Persian: Persian speakers never strip the al- and never inflect it, which is exactly Nourai's point in the root box. Note that الکل here is al-koll 'the all', not the alcohol word of node #8 (Persian alkol, from French), although the two are written identically.\",\n \"sources\": [E+\"al-\", E+\"Allah\"],\n \"ref_check\": [MON_PARTIAL],\n \"consulted\": [\n   co(\"MON\", \"MON_part2.txt s.v. مثنی (grep 'المثنی|مثنی')\", \"supports\",\n      \"'مثنی : [ع.] (اِ.) دو زانو و دو مرفق ستور … دو تا دو تا' — Mo'in lemmatises the word with the origin tag [ع.] 'Arabic', confirming that the form Nourai cites is an Arabic borrowing used in Persian.\"),\n   co(\"GPL\", \"GPL.txt ff-page 27, §10 (Platts–Ranking, Grammar of the Persian Language)\", \"supports\",\n      \"Platts teaches the Arabic article inside a Persian grammar: 'called \\\"solar letters\\\" (huruf-i shamsiya … al-hurufu 'sh-shamsiya) … the remaining letters of the Arabic alphabet, \\\"lunar letters\\\" (huruf-i qamariya)' — i.e. Persian grammar takes over the al- and its assimilation rule wholesale, exactly the root box's claim.\"),\n   co(\"Etymonline\", E+\"al-\", \"supports\",\n      \"'al- : in words from Arabic (or assumed to be), it is the definite article \\\"the\\\". Sometimes rendered in English as el-. Often assimilated to following consonants (as-, az-, ar-, am-, an-, etc.)'\")\n ]})\n\n# ---------------- node 2 ----------------\nnodes.append({\n \"id\": 2, \"lang\": \"Arabic\", \"words\": \"Amir al-bahr; al-fesfeseh\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Two Arabic al- phrases. (1) أمير البحر amīr al-baḥr 'commander of the sea': amīr is the active participle of أمر amara 'to command' (Nourai's ☞A`.m.r), baḥr 'sea'. The word really did reach Europe as an Arabic amīr + article, but the specific phrase is contested: the OED explains that 'as amīr is constantly followed by -al- in all such titles, amīr-al- was naturally assumed by Christian writers as a substantive word', and Klein prefers amīr-ar-raḥl 'commander of transport'. Devic reports the amīr al-baḥr guess as Engelmann's and rejects it, Lokotsch calls it 'wenig wahrscheinlich'. So the al- is genuine, the baḥr is not established — hence 'plausible' rather than 'confirmed'. (2) فصفصة al-fiṣfiṣa / al-faṣfaṣa 'lucerne, green fodder' is itself an Iranian loan in Arabic: Middle Persian aspast (asp 'horse' + -ast 'food', PIE *h₁ed- 'eat' + *h₁eḱwo- 'horse' — Nourai's ☞Ed, Ekwos), whence Andalusian Arabic al-fáṣfaṣa and Spanish alfalfa (earlier alfalfez). Nourai's gloss 'horse food' is literally Watkins's gloss for the Iranian compound.\",\n \"sources\": [E+\"admiral\", E+\"alfalfa\", AHD_ONLINE, W+\"%D9%81%D8%B5%D9%81%D8%B5%D8%A9\"],\n \"ref_check\": [\n   rc(\"KLN\", \"contradicts\",\n      \"KLN_1966.txt ff-page 25 (≈ printed p.26), s.v. admiral: 'OF. amiral … prob. shortened fr. Arab. amīr-ar-raḥl, \\\"commander of transport, officer commanding a (transport) fleet\\\" … (It., Sp. and Port. almirante arose from a confusion of am-, the beginning of the word amir, with the Arab. art. al-)'. Klein — the reference Nourai cites here — gives a different phrase and calls the al- of the Romance forms a confusion. Klein DOES support the other word: 'alfalfa, n., lucerne. — Sp., fr. Arab. al-fasfasa'.\"),\n   rc(\"AHD\", \"supports\",\n      \"AHD online Indo-European appendix, s.v. *ed-: 'alfalfa, from Old Iranian *-sti-, food, in compound *aspa-sti- clover, alfalfa (\\\"horse food\\\") (*aspa-, horse; see ekwo-)'; and s.v. *ekwo-: 'alfalfa, from Old Iranian *aspa-, horse.' This is exactly Nourai's ☞Ed, Ekwos double cross-reference. (The 1985 Watkins text on disk, AHD_watkins1985.txt, does not yet list alfalfa under ekwo-; the online revision does.)\"),\n   NOT_OEW],\n \"consulted\": [\n   co(\"LKT\", \"LKT.txt no. 598 (ff-page 74) and the Admiral entry at ff-page 32\", \"partial\",\n      \"no.598: 'Ar. fasfasa: \\\"Luzerne Medicago sativa L.\\\", auch fisfisa; hieraus sp. alfalfa, alfafe … engl. amerik. alfalfa' (supports). But on admiral Lokotsch writes: 'Daß die Worte aus amīr-al-baḥr \\\"Befehlshaber der See, des Meeres\\\" entstanden sein sollen, scheint wenig wahrscheinlich' — and notes sp./pg. almirante arose 'mit Verkennung des ar. Stammes am… als ar. Artikel' (contradicts).\"),\n   co(\"DEV\", \"DEV.txt ff-page 58, s.v. Amiral\", \"contradicts\",\n      \"'Engelmann avait supposé que l'al final était l'article précédant un mot tombé depuis, par exemple بحر bahr, mer: amir-al-bahr, commandant de la mer, serait devenu amir-al tout court. Cette explication, au moins quant au mot bahr, ne semble guère admissible' — Devic rejects precisely Nourai's phrase.\"),\n   co(\"PLA\", \"Asbaghi, Persische Lehnwörter im Arabischen, s.v. fiṣfiṣa (PLA_asbaghi_1988_ia_djvu.txt)\", \"supports\",\n      \"'fisfisa: \\\"Luzerne\\\" pers. — asbast od. asfast'; and at the ʾisfist entry: '\\\"asfast: \\\"Luzerne, Futterpflanze\\\" pers., aus pers. aspast, MP aspast' — the Arabic word is a Middle-Persian loan, as Nourai's cross-reference implies.\"),\n   co(\"SKT\", \"SKT.txt ff-page 24, s.v. Admiral\", \"supports\",\n      \"'Admiral. (F.-Arab.) M.E. more often amiral … O.F. amiral … Arab. amīr, a prince … The suffix is due to Arab. [al-] … amir-al-bahr, prince of the sea.' Skeat is the one book on the shelf that still gives Nourai's phrase without demur.\")\n ]})\n\n# ---------------- node 3 ----------------\nnodes.append({\n \"id\": 3, \"lang\": \"English\", \"words\": \"admiral; alfalfa\",\n \"verdict\": \"plausible\",\n \"derivation\": \"admiral: Middle English amiral/admirail 'Saracen commander' c.1200, from Old French amirail (12c.), itself from Medieval Latin amiratus/admiralis, a title that acquired its naval sense in 12th-c. Norman Sicily; 'amiral de la mer' appears in late-13c. Anglo-French, and the sense 'highest naval officer' is early-15c. English. The unetymological -d- is from Latin admirari 'to wonder at' (whence admire). So the al- is Arabic, but as the frozen tail of amīr-al-, not demonstrably from baḥr. alfalfa: borrowed into American English in 1845 from Spanish alfalfa (earlier alfalfez) < Andalusian Arabic al-fáṣfaṣa < Classical Arabic fiṣfiṣa < Middle Persian aspast; the plant is the European 'lucerne', renamed in the New World from the Spanish form.\",\n \"sources\": [E+\"admiral\", E+\"alfalfa\"],\n \"ref_check\": [\n   rc(\"AHD\", \"partial\",\n      \"The local AHD text is only the Indo-European appendix (AHD_watkins1985.txt); its 1985 *ekwo- entry ('ekwo-. Horse … [Pok. ekuo-s 301.]') does not yet list alfalfa, but the revised online appendix does (see node #2). AHD's main-dictionary admiral entry is not open online (New College Edition is lending-only), so Nourai's AHD citation for 'admiral' is unverifiable.\"),\n   NOT_OEW],\n \"consulted\": [\n   co(\"KLN\", \"KLN_1966.txt ff-page 25 s.v. admiral; s.v. alfalfa\", \"partial\",\n      \"admiral: 'influenced in form by L. admirari, \\\"to admire\\\"' — Klein confirms the English form history but not amīr al-baḥr; alfalfa: 'Sp., fr. Arab. al-fasfasa. (Cp. the collateral Sp. form alfalfez, which represents the intermediate form between Arab. al-fáṣfaṣah and Sp. alfalfa.)' — confirms.\"),\n   co(\"Etymonline\", E+\"admiral\", \"partial\",\n      \"Quotes OED: 'As amīr is constantly followed by -al- in all such titles, amīr-al- was naturally assumed by Christian writers as a substantive word, and variously Latinized'; 'Italian form almiraglio, Spanish almirante are from confusion with Arabic words in al-.' The al- link is accepted, the sea-commander phrase is not asserted.\"),\n   co(\"SKT\", \"SKT.txt ff-page 640 (Skeat's list of borrowings)\", \"supports\",\n      \"Skeat files admiral among 'French from Arabic: admiral, alcohol, assassin, … lute (1), … saffron, sultan' — the same route class Nourai draws.\")\n ]})\n\n# ---------------- node 4 ----------------\nnodes.append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"âdmîral «آدمیرال»; âlfâlfâ «آلفا آلفا»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Modern Persian technical loans that re-enter Persian from the West, closing Nourai's Arabic → Europe → Persian loop. آدمیرال âdmirâl 'admiral' is taken from English/French admiral–amiral (the -d- shows it is the Western, not the Arabic, form; a direct Arabic borrowing would be امیرالبحر amir-al-bahr, which Persian also has as دریاسالار's Arabic equivalent). Mo'in glosses آدمیرال precisely by that Arabic phrase. آلفالفا 'alfalfa' is a 20th-c. re-borrowing of the Spanish/English name for a plant Persian already had as یونجه yonje — a genuine round trip, since the Arabic word behind alfalfa is itself from Middle Persian aspast. Caveat: the book prints the Persian of the second word as two separate words, «آلفا آلفا» (verified on the page image, pdftoppm p.47), i.e. âlfâ âlfâ, which does not match its own transliteration âlfâlfâ and is not the normal Persian spelling آلفالفا; and neither آلفالفا nor آلفا آلفا is in the Mo'in text on disk. Hence 'plausible' rather than 'confirmed'.\",\n \"sources\": [E+\"alfalfa\"],\n \"ref_check\": [\n   rc(\"MON\", \"supports\",\n      \"MON_part1.txt (grep 'آدمیرال'): 'آدمیرال Admiral [ع. امیرالبحر] (اِ.) امیرالبحر، دریاسالار' — Mo'in has the headword with the origin tag [ع. امیرالبحر] 'Arabic amīr al-baḥr', which is exactly the etymology Nourai draws and the reference he cites. No آلفالفا entry could be found in the 2-vol abridgement, so that half is not verified.\")],\n \"consulted\": [\n   co(\"MON\", \"MON_part1.txt s.v. آدمیرال\", \"supports\",\n      \"'[ع. امیرالبحر] (اِ.) امیرالبحر، دریاسالار. آدمیرال' — Mo'in derives the Persian word from Arabic amīr al-baḥr.\"),\n   co(\"Nourai's own page image\", \"EtymologicalDictionary-persian-english.pdf p.47, Persian box under English\", \"partial\",\n      \"Rendered at 500 dpi the Persian line unambiguously reads «آلفا آلفا» as two words against the transliteration 'âlfâlfâ' — the oddity is the book's own, not a transcription error in the JSON.\"),\n   co(\"Wiktionary\", W+\"%D8%A7%D9%84%DA%A9%D9%84\", \"supports\",\n      \"Parallel case documented for the sister node: Persian الکل is 'Borrowed from French alcool … (a direct borrowing from Arabic would drop the definite article ال)' — the same Europe→Persian return route Nourai draws for آدمیرال.\")\n ]})\n\n# ---------------- node 5 ----------------\nnodes.append({\n \"id\": 5, \"lang\": \"Arabic\", \"words\": \"al-kahl; al-Xwârazmî; al-ithmud\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Three al- forms that fed medieval Latin science. (1) الكحل al-kuḥl (vulgar al-kohl; Nourai's 'al-kahl' renders the root vowel of كحل k-ḥ-l, his ☞K.h.l) is the impalpable powder of antimony sulphide used as eye-paint; the sense 'highly rectified spirit' that Nourai glosses is the later European development, from Paracelsus's use of the word for anything reduced to its finest essence. (2) الخوارزمي al-Khwārizmī 'the man of Khwārazm' (modern Khiva), nisba of Abū Jaʿfar Muḥammad b. Mūsā, the Baghdad mathematician of the 9th c. whose Kitāb al-jabr wa-l-muqābala gave Europe both 'algebra' and, from his name, 'algorism/algorithm'; the al- is the article of the nisba. Nourai's ☞Ghdhem points at the Iranian place-name element. (3) الإثمد al-ithmid (also uthmud) 'stibnite, antimony', a metathesised borrowing of Coptic ⲉⲥⲑⲏⲙ esthēm / Greek στίμμι stímmi, ultimately Egyptian sdm.\",\n \"sources\": [E+\"alcohol\", E+\"algorithm\", E+\"antimony\", W+\"%D8%A5%D8%AB%D9%85%D8%AF\"],\n \"ref_check\": [\n   rc(\"KLN\", \"supports\",\n      \"KLN_1966.txt ff-page 36 (≈ p.48) s.v. alcohol: 'ML., fr. Arab. al-kohl, vulgar pronunciation of al-kuhl, fr. al-, \\\"the\\\", and kohl, resp. kuhl, \\\"antimony (used for painting the eyelids)\\\" … Its modern sense (\\\"highly rectified spirits\\\") is due to the analogy of the fineness of this powder' — Klein's last clause is Nourai's gloss. ff-page 37 s.v. algorism: 'fr. ML. algorismus, from the inexact transliteration of Arab. al-Khowarizmi, \\\"the man of Khowarizm (the modern Khiva)\\\", surname of Abu Jafar Mohammed ibn Musa, great mathematician of the 9th cent.' ff-page (grep '^antimony') s.v. antimony: 'ML. antimonium, prob. fr. Arab. al-uthmud, al-ithmid, from al-, \\\"the\\\", and uthmud, ithmid, \\\"stibium\\\"'. All three of Nourai's words are Klein's.\"),\n   rc(\"AHD\", \"not_checked\",\n      \"Only the Indo-European appendix of AHD is available locally/online; these are Semitic and Iranian words with no IE root entry, so the AHD citation (a main-dictionary entry in the 1975 New College Edition, lending-only) cannot be read.\"),\n   NOT_OEW],\n \"consulted\": [\n   co(\"LKT\", \"LKT.txt no. 918 (ff-page 100) and the kuhl / algorismus entries (ff-pages 126, 98)\", \"supports\",\n      \"no.918: 'Ar. itmid: [Aus äg. kopt. stēm, altäg. sdm, woraus auch gr. stimmi, lat. stibium] \\\"Antimon\\\"; hieraus mit starker Verstümmelung [vielleicht aus der ar. Vokalisation utmud heraus] mlat. antimonium, frz. antimoine … engl. antimony'. algorismus: 'daher wurde lat. algorithmus, algorismus [mit Anlehnung an gr. arithmos] die Bezeichnung für das Rechnen mit ar. Ziffern'.\"),\n   co(\"Wiktionary\", W+\"%D8%A5%D8%AB%D9%85%D8%AF\", \"supports\",\n      \"Arabic إِثْمِد ʔiṯmid 'antimony, antimony ore, kohl', 'By form a metathesis away from Coptic ⲉⲥⲑⲏⲙ (esthēm) … ultimately from Egyptian sdm'; Descendants: '→ Latin: antimonium → English: antimony'.\"),\n   co(\"DEV\", \"DEV.txt ff-page 39, s.v. Alcool\", \"supports\",\n      \"'Il est bien démontré que l'étymologie de ce mot est l'arabe الكحل al-kohl, le cohol ou poudre d'antimoine, dont les femmes, en Orient, se teignent les paupières.'\")\n ]})\n\n# ---------------- node 6 ----------------\nnodes.append({\n \"id\": 6, \"lang\": \"Latin\", \"words\": \"(no words printed — Medieval Latin pass-through)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The empty box stands for the Medieval Latin of the translators and alchemists, which is where all three words of node #5 actually entered Europe: ML alcohol / alcofol 'powdered ore of antimony' (Paracelsus, d.1541, extends it to any sublimate and to volatile liquids); ML algorismus (12th-c. Latin versions of al-Khwārizmī's arithmetic, Liber algorismi de numero Indorum, with the second syllable pulled toward Greek ἀριθμός arithmos); ML antimonium (11th c.), a heavy Latin mangling of al-ithmid. The 12th–13th c. Toledo translation workshops are the concrete channel.\",\n \"sources\": [E+\"alcohol\", E+\"algorithm\", E+\"antimony\"],\n \"ref_check\": [rc(\"None\", \"not_checked\", \"The box carries no reference in the book (refs=None), so there is nothing of Nourai's to check.\")],\n \"consulted\": [\n   co(\"KLN\", \"KLN_1966.txt ff-pages 36, 37 and s.v. antimony\", \"supports\",\n      \"Klein routes every one of the three through Medieval Latin: 'alcohol, n. — ML., fr. Arab. al-kohl'; 'algorism … fr. ML. algorismus'; 'antimony … ML. antimonium, prob. fr. Arab. al-uthmud'.\"),\n   co(\"Etymonline\", E+\"antimony\", \"supports\",\n      \"'from Old French antimoine and directly from Medieval Latin antimonium (11c.) … unless the Arabic word is from the Greek and the Latin is from Arabic (which would explain the a- as the Arabic direct article al-)' — the Latin stage is where the al- is absorbed.\"),\n   co(\"LKT\", \"LKT.txt Latin index (ff-page 242): 'algorismus 890, algorithmus 890, antimonium 918, alambicum 79'\", \"supports\",\n      \"Lokotsch's index of Medieval Latin forms lists exactly these Latin intermediates for the Arabic numbers cited.\")\n ]})\n\n# ---------------- node 7 ----------------\nnodes.append({\n \"id\": 7, \"lang\": \"French\", \"words\": \"(no words printed — French pass-through)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"French alcool, algorithme, antimoine. French refashioned Old French algorisme into algorithme under the mistaken pull of Greek arithmos 'number'; antimoine acquired in French the joke folk-etymology anti-moine 'monk's bane'. This French stage is the one that matters for node #8, because modern Persian took all three words from French, not from Latin or Arabic.\",\n \"sources\": [E+\"algorithm\", E+\"antimony\", W+\"%D8%A7%D9%84%DA%A9%D9%84\"],\n \"ref_check\": [rc(\"None\", \"not_checked\", \"The box carries no reference in the book (refs=None).\")],\n \"consulted\": [\n   co(\"LKT\", \"LKT.txt no. 890 (ff-page 98) and no. 918 (ff-page 100)\", \"supports\",\n      \"'Hieraus afrz. algorisme, frz. algorithme, it. alguarismo …'; 'mlat. antimonium, frz. antimoine [woraus die spaßhafte Volksetymologie von dem dtsch. Mönche … anti- < gr. anti \\\"gegen\\\", frz. moine \\\"Mönch\\\"]'.\"),\n   co(\"DEV\", \"DEV.txt ff-page 39 s.v. Alcool\", \"supports\",\n      \"Devic's whole book is the French reception of these Arabic words; s.v. Alcool he gives 'Esp. et portug. alcohol, aragon. alcofol, catal. alcofoll' as the Iberian stage feeding French alcool.\"),\n   co(\"Wiktionary\", W+\"%D8%A2%D9%86%D8%AA%DB%8C%D9%85%D9%88%D8%A7%D9%86\", \"supports\",\n      \"Etymology tree: 'Egyptian sdm → Ancient Greek στίμμι → Coptic ⲉⲥⲑⲏⲙ → Arabic إِثْمِد → Latin antimonium → French antimoine → Persian آنتیموان' — the French link is explicit.\")\n ]})\n\n# ---------------- node 8 ----------------\nnodes.append({\n \"id\": 8, \"lang\": \"Persian\", \"words\": \"alkol «الکل»; âlgoritm «آلگوریتم»; ântîmoân «آنتیموان»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three are 19th–20th c. Persian borrowings from French, as their phonetic shape shows. الکل alkol keeps the French -ool of alcool (a direct Arabic borrowing would have given kohl/kuḥl without the article, as Persian کحل kohl in fact does); آنتیموان ântimo'ân is French antimoine with the nasal rendered -oân; آلگوریتم âlgoritm is French algorithme, with the Greek-influenced -ith- that only the French form has (Arabic and Latin had algorism-). The last word is an especially neat round trip: al-Khwārizmī was an Iranian from Khwārazm, so the Persian word is his own name returned after a thousand years by way of Baghdad, Toledo and Paris.\",\n \"sources\": [W+\"%D8%A7%D9%84%DA%A9%D9%84\", W+\"%D8%A2%D9%86%D8%AA%DB%8C%D9%85%D9%88%D8%A7%D9%86\", E+\"algorithm\"],\n \"ref_check\": [MON_PARTIAL, NOT_VOP],\n \"consulted\": [\n   co(\"Wiktionary\", W+\"%D8%A7%D9%84%DA%A9%D9%84\", \"supports\",\n      \"Persian الکل (alkol): 'Borrowed from French alcool, from Arabic الْكُحُل (al-kuḥul) (a direct borrowing from Arabic would drop the definite article ال (al-)) … Doublet of کحل (kohl) and الکحل (alkohol).' Exactly Nourai's Arabic → Latin → French → Persian arrow.\"),\n   co(\"Wiktionary\", W+\"%D8%A2%D9%86%D8%AA%DB%8C%D9%85%D9%88%D8%A7%D9%86\", \"supports\",\n      \"Persian آنتیموان (ântimo'an) 'antimony': 'Borrowed from French antimoine', with the tree Egyptian sdm > Greek stímmi > Coptic esthēm > Arabic ʔiṯmid > Latin antimonium > French antimoine > Persian.\"),\n   co(\"MON\", \"MON_part1.txt / MON_part2.txt (grep 'الکل', 'آنتیموان')\", \"partial\",\n      \"The abridged Mo'in uses both words in running definitions ('… ۲/۵ و ۵ درصد الکل دارد'; '… سولفور آنتیموان …'), so they are current Persian vocabulary in Mo'in's own text, but the abridgement has no separate etymological headword for either.\")\n ]})\n\n# ---------------- node 9 ----------------\nnodes.append({\n \"id\": 9, \"lang\": \"English\", \"words\": \"alcohol, algorithm, antimony\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The three English words are right, but Nourai's single Latin→English arrow flattens three different routes. alcohol really is a direct Medieval Latin borrowing (1540s, earlier alcofol early 15c., 'fine powder produced by sublimation'; 'intoxicating ingredient' only by 1753, short for alcohol of wine). antimony is early 15c. from Old French antimoine AND directly from ML antimonium — so French is in the chain, not bypassed. algorithm is not from Latin at all in its modern shape: Middle English had algorism (early 13c.) from Old French algorisme, and the -ith- form is a 1690s borrowing of French algorithme; so English inherits the French refashioning, which Nourai's chart routes only to Persian. Hence 'plausible': right words, over-simplified arrow.\",\n \"sources\": [E+\"alcohol\", E+\"algorithm\", E+\"antimony\"],\n \"ref_check\": [\n   rc(\"AHD\", \"not_checked\", \"AHD's main-dictionary entries for these three are not open online (New College Edition lending-only); the local AHD file is only the IE-roots appendix, which has no entry for Semitic loans.\"),\n   rc(\"KLN\", \"partial\",\n      \"KLN_1966.txt gives all three but with French/OF in the chain for two of them: 'algorism, n. … ME. algorisme, fr. OF. algorisme (F. algorithme), fr. ML. algorismus' (ff-page 37); 'antimony … ML. antimonium'; only 'alcohol, n. — ML.' matches a straight Latin→English arrow.\")],\n \"consulted\": [\n   co(\"Etymonline\", E+\"algorithm\", \"partial\",\n      \"'1690s, \\\"Arabic system of computation\\\", from French algorithme, refashioned (under mistaken connection with Greek arithmos \\\"number\\\") from Old French algorisme … The earlier form in Middle English was algorism (early 13c.), from Old French.' — English took it from French, not from Latin directly.\"),\n   co(\"SKT\", \"SKT.txt ff-page 640 (list of loan classes)\", \"supports\",\n      \"Skeat classes alcohol under 'French from Arabic: admiral, alcohol, assassin …' — i.e. even alcohol he routes through French, further loosening Nourai's Latin→English arrow.\"),\n   co(\"LKT\", \"LKT.txt no. 890, no. 918\", \"supports\",\n      \"Lokotsch gives the same terminal English forms: 'engl. algorism, algorithm \\\"Rechenart\\\"'; 'engl. antimony'; 'engl. alcohol'.\")\n ]})\n\n# ---------------- node 10 ----------------\nnodes.append({\n \"id\": 10, \"lang\": \"Arabic\", \"words\": \"al-qela; az-zarnîx; al-mâlâgma\",\n \"verdict\": \"disputed\",\n \"derivation\": \"(1) القلي al-qilī 'the calcined ashes of the saltwort (Salsola), rich in soda', from قلى qalā 'he roasted, fried' — Nourai's gloss is exactly right and the word is the source of alkali. (2) المالغم al-malgham 'soft mass, emollient poultice', which Arabic itself took (via Syriac malagmā) from Greek μάλαγμα malagma 'softening substance' — right, and Nourai's ☞Mel 3 points at PIE *mel- 'soft'. (3) الزرنيخ az-zarnīkh 'orpiment, arsenic' is a genuine Arabic word and genuinely Iranian in origin (Middle Persian zarnīk 'golden', OP *daraniya- 'gold', Nourai's ☞Ghel = PIE *ǵʰel- 'to shine, yellow') — but it is NOT the source of European 'arsenic'. Greek ἀρσενικόν arsenikon (Dioscorides, 1st c. CE, reshaped by folk etymology after ἄρσην 'male') was borrowed from Iranian through Syriac ܙܪܢܝܟܐ zarnīkā some six centuries before Arabic existed as a literary language, and Latin arsenicum > Old French arsenic > English arsenic descends from the Greek. The az- of Nourai's chart is the Aramaic/Syriac, not the Arabic, definite state. That is why this node is 'disputed'.\",\n \"sources\": [E+\"alkali\", E+\"amalgam\", E+\"arsenic\", W+\"%D8%B2%D8%B1%D9%86%D9%8A%D8%AE\"],\n \"ref_check\": [\n   rc(\"KLN\", \"contradicts\",\n      \"KLN_1966.txt ff-page 38 s.v. alkali: 'F. alcalli (now spelled alcali), fr. Arab. al-qilī, fr. al-, \\\"the\\\", and qilī, \\\"charred ashes of the saltwort\\\", fr. qala, \\\"he fried, roasted\\\"' (supports); ff-page 42 s.v. amalgam: 'F. amalgame, fr. ML. amalgama, dissimil. fr. Arab. al-malgham, which is formed fr. Arab. al-, \\\"the\\\", and Syr. malagmā, fr. Gk. μάλαγμα' (supports). But ff-page 68 s.v. arsenic: 'OF. (= F.) arsenic, fr. L. arsenicum, arrhenicum, fr. Gk. ἀρσενικόν … fr. MPers. *zarnik, \\\"gold, golden; orpiment\\\" (whence ModPers.-Arab. zarnikh, \\\"orpiment\\\"), through the medium of a Semitic language; cp. Mishnaic Heb. zarnikh, Syr. zarnikhā' — Klein makes Arabic zarnīkh a sibling of the Greek word, not its ancestor.\"),\n   rc(\"SKT\", \"supports\",\n      \"SKT.txt ff-page 28, s.v. Alkali (OCR partly damaged but legible): 'Alkali, a salt. (Arab.) Arab. al-qilī, ashes of glass-wort, which abound in soda.' Skeat's arsenic entry (ff-page 43) is too badly OCR'd to read.\"),\n   rc(\"AHD\", \"contradicts\",\n      \"AHD_watkins1985.txt, root *ghel-2 (ff-page 51): '… Syriac zarnikā, orpiment: ARSENIC.' Watkins routes English ARSENIC through Syriac, not Arabic — so the AHD Nourai cites for this box does not support the Arabic step.\"),\n   NOT_OEW],\n \"consulted\": [\n   co(\"LKT\", \"LKT.txt no. 1029-ish al-qilī (ff-page 110) and the amalgam entry (ff-page 137)\", \"supports\",\n      \"'…hieraus … sp. pg. alcali, frz. alcali … engl. alkali, dtsch. Alkali usw. Auch der Name des Elementes Kalium … gehört hierhin'; amalgam: 'gr. malagma mit Metathesis; hieraus sp. pg. kat. amalgama, frz. amalgame; engl. amalgam'. Notably Lokotsch has NO entry for arsenic/Arsenik among his 'europäische Wörter orientalischen Ursprungs' route through Arabic.\"),\n   co(\"PLA\", \"Asbaghi p.144–145 s.v. zarnīḫ (PLA_pages.txt lines 8227, 8244)\", \"partial\",\n      \"'zarnīh: \\\"Arsenik, Sandarak\\\" pers. < ap. daraniyā \\\"Gold\\\"', with the continuation on p.145 '… daher Arsenik u. Arsen aus dem ar. …'. Asbaghi therefore does derive European Arsenik from the Arabic word — the only book on the shelf that agrees with Nourai here, and he is arguing about Persian→Arabic, not about Greek chronology.\"),\n   co(\"HUB\", \"HUB.txt ff-page 268 (Hübschmann, Persische Studien)\", \"partial\",\n      \"'arm. zarik (Mos. Geogr.) \\\"Auripigment, Arsenik\\\" (= ap. *zarnika für zd. zaranya- \\\"Gold\\\")' — Hübschmann reconstructs the Old Persian etymon Nourai's ☞Ghel implies, but attaches the western words to the Iranian form, not to Arabic.\"),\n   co(\"Wiktionary\", W+\"%D8%B2%D8%B1%D9%86%D9%8A%D8%AE\", \"contradicts\",\n      \"Arabic زِرْنِيخ zirnīḵ: 'From Middle Persian zarnīk', with the tree PIE *ǵʰelh₃- > … > Old Median *zaraniyakā > Middle Persian *zarnīk > Classical Syriac ܙܪܢܝܟܐ zarnīḵā > Arabic زرنيخ. Its Descendants are only Middle Armenian and Maltese — European 'arsenic' is not among them.\"),\n   co(\"DEV\", \"DEV.txt ff-page 37\", \"partial\",\n      \"'… qui est le même mot que le grec ἀρσενικός, arsenic jaune, orpiment' — Devic equates Arabic az-zarnīkh with the Greek word rather than deriving the Greek from it.\")\n ]})\n\n# ---------------- node 11 ----------------\nnodes.append({\n \"id\": 11, \"lang\": \"French\", \"words\": \"(no words printed — French pass-through)\",\n \"verdict\": \"plausible\",\n \"derivation\": \"French alcali, arsenic, amalgame. Two of the three sit correctly on an Arabic parent: alcali is first found in Albertus Magnus's Latin (alkali) and is French alcali/alcalli by the 16th c.; amalgame is French from Medieval Latin amalgama, an alchemists' word for a mercury alloy, itself dissimilated from al-malgham. The third, arsenic, is French only in the sense that Old French arsenic continues Latin arsenicum from Greek — it does not descend from the Arabic box above it, so this pass-through box inherits node #10's problem for one of its three words.\",\n \"sources\": [E+\"alkali\", E+\"amalgam\", E+\"arsenic\"],\n \"ref_check\": [rc(\"None\", \"not_checked\", \"The box carries no reference in the book (refs=None).\")],\n \"consulted\": [\n   co(\"KLN\", \"KLN_1966.txt ff-page 38 (alkali), ff-page 42 (amalgam), ff-page 68 (arsenic)\", \"partial\",\n      \"'alkali, n. — F. alcalli (now spelled alcali), fr. Arab. al-qilī'; 'amalgam, n. … — F. amalgame, fr. ML. amalgama … fr. Arab. al-malgham'; but 'arsenic, n. … — OF. (= F.) arsenic, fr. L. arsenicum … fr. Gk. ἀρσενικόν'.\"),\n   co(\"DEV\", \"DEV.txt ff-page 33 s.v. Alcali\", \"supports\",\n      \"'Alcali. Esp. et port. alcali. De l'arabe القلي al-qali, cendres de soude ou la plante elle-même. Dans certaines régions du midi de la France, on réserve le nom de caliou aux cendres de sarments.'\"),\n   co(\"LKT\", \"LKT.txt ff-page 110 and ff-page 137\", \"partial\",\n      \"'frz. alcali'; 'frz. amalgame' are both derived from the Arabic words; arsenic is absent from Lokotsch's Arabic material altogether.\")\n ]})\n\n# ---------------- node 12 ----------------\nnodes.append({\n \"id\": 12, \"lang\": \"Persian\", \"words\": \"âlkâlî «آلکالی»; ârsenîk «آرسنیک»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Both are modern chemical loans from French: آلکالی âlkâlî < French alcali (Persian's older, Arabic-mediated word for the same substance is قلیا qalyā, straight from al-qilī, which is what makes the French form recognisably a second, Western borrowing), and آرسنیک ârsenik < French arsenic. The Persian→French step Nourai draws is correct for both; what is wrong is only the ancestry he assigns to arsenic above node #11, since French arsenic comes from Latin/Greek and not from Arabic az-zarnīkh — Persian's genuinely inherited word for the same substance is زرنیخ zarnīkh, which Borhān-e Qāṭeʿ still lists. Neither Persian form is in the Moʿin text available on disk, and Nourai's only reference here (VOP) is unobtainable, so the node cannot be raised above 'plausible'.\",\n \"sources\": [E+\"arsenic\", E+\"alkali\"],\n \"ref_check\": [NOT_VOP],\n \"consulted\": [\n   co(\"MON\", \"MON_part1.txt / MON_part2.txt (grep 'آلکالی', 'آرسنیک')\", \"partial\",\n      \"No headword for either; but آرسنیک occurs in Moʿin's running text ('مداوای آن … با املاح آرسنیک یا آنتی‌پیرین …'), so the loan is real Persian, just not lemmatised in the abridgement.\"),\n   co(\"BQT\", \"BQT_v2.txt s.v. زرنیخ (grep 'زرنیخ')\", \"supports\",\n      \"'… مخفف زرنیخ است، و آن جوهری باشد کانی و آن بر دو نوع است: احمر و اصفر. احمر را اهل صنعت کیمیا کار برند و اصفر را استادان نقاش' — Borhān-e Qāṭeʿ confirms zarnīkh as the inherited Persian mineral name (and, incidentally, its use by the کیمیا practitioners), against which آرسنیک is plainly the later European import.\"),\n   co(\"HUB\", \"HUB.txt ff-page 268\", \"supports\",\n      \"'arm. zarik … (= ap. *zarnika für zd. zaranya- \\\"Gold\\\")' — the Iranian pedigree of the native word.\")\n ]})\n\n# ---------------- node 13 ----------------\nnodes.append({\n \"id\": 13, \"lang\": \"English\", \"words\": \"alkali, alkaline, arsenic, amalgam\",\n \"verdict\": \"disputed\",\n \"derivation\": \"alkali is late 14c. English 'soda ash', from Medieval Latin alkali < Arabic al-qilī, with alkaline a 1670s English derivative in -ine — confirmed. amalgam is c.1400, from Old French amalgame or directly from ML amalgama (c.1300, an alchemists' word), probably from al-malgham — confirmed. arsenic, however, is late 14c. from Old French arsenic < Latin arsenicum < late Greek arsenikon, adapted from Syriac (al-)zarniqā < Middle Persian zarnīk 'gold-coloured'; the word entered Greek from Iranian through Aramaic in antiquity and never passed through Arabic, so listing it as an al- word is a mistake — the al/az- in the Syriac form is the Aramaic determinate state, not the Arabic article. Because the chart makes arsenic a descendant of the Arabic definite article, the node is disputed.\",\n \"sources\": [E+\"alkali\", E+\"arsenic\", E+\"amalgam\"],\n \"ref_check\": [\n   rc(\"AHD\", \"contradicts\",\n      \"AHD_watkins1985.txt root *ghel-2 (ff-page 51): '… Syriac zarnikā, orpiment: ARSENIC' — Watkins's only pathway for English ARSENIC is the Syriac one; the AHD index (ff-page 113) likewise files 'ARSENIC ghel-2'. AHD's alkali/amalgam main entries are not open online.\")],\n \"consulted\": [\n   co(\"KLN\", \"KLN_1966.txt ff-page 68 s.v. arsenic; ff-page 38 s.v. alkali; ff-page 42 s.v. amalgam\", \"partial\",\n      \"Supports alkali and amalgam verbatim; on arsenic: 'fr. Gk. ἀρσενικόν … fr. MPers. *zarnik … through the medium of a Semitic language; cp. Mishnaic Heb. zarnikh, Syr. zarnikhā. … Gk. ἀρσενικόν was influenced in form by ἀρσενικός, \\\"male\\\", fr. ἄρσην.'\"),\n   co(\"Etymonline\", E+\"arsenic\", \"contradicts\",\n      \"'late 14c. … from Old French arsenic, from Latin arsenicum, from late Greek arsenikon (Dioscorides) … adapted from Syriac (al) zarniqa \\\"arsenic\\\", from Middle Persian zarnik \\\"gold-colored\\\" … The form of the Greek word is folk etymology, literally \\\"masculine\\\".'\"),\n   co(\"SKT\", \"SKT.txt ff-page 28 s.v. Alkali\", \"supports\",\n      \"'Alkali, a salt. (Arab.) Arab. al-qilī, ashes of glass-wort, which abound in soda' — supports the alkali half of the node (SKT is one of the references Nourai cites for the parent box #10).\")\n ]})\n\n# ---------------- node 14 ----------------\nnodes.append({\n \"id\": 14, \"lang\": \"Arabic\", \"words\": \"Al-lah; al-qadŭs; al-anbîq; al-bâdenjân; al-nil\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Five al- forms, four of them exported. الله Allāh is a contraction of al-ilāh 'the god' (Nourai's ☞Layh = the Semitic ʾ-l-h stem, cognate with Aramaic ʾelāh, Hebrew ʾĕlōah). القادوس al-qādūs is the pot or bucket of a water-wheel (< Greek κάδος kados 'jar', itself a Semitic loan, Hebrew kad); it named the pelican 'the water-carrier' (compare Arabic saqqā 'pelican', literally 'water carrier'), whence Portuguese alcatruz > alcatraz > albatross. الأنبيق al-anbīq 'the still, the cap of a still' is Greek ἄμβιξ ambix taken over with the article, reaching Europe through Old Spanish alambique. الباذنجان al-bādhinjān is a Persian loan in Arabic (Classical Persian bādingān/bāzingān < Sanskrit vātiṅgaṇa < Dravidian — exactly Nourai's ☞Vatin-ganah). النيل al-nīl 'the indigo' is likewise Persian nīl < Sanskrit nīlī 'indigo', nīla- 'dark blue'.\",\n \"sources\": [E+\"Allah\", E+\"albatross\", E+\"alembic\", E+\"aubergine\", E+\"anil\", W+\"%D8%A8%D8%A7%D8%B0%D9%86%D8%AC%D8%A7%D9%86\"],\n \"ref_check\": [\n   rc(\"KLN\", \"supports\",\n      \"KLN_1971.txt s.v. Allah: 'Arab. Allāhu, contraction of al-Ilāhu, fr. al-, \\\"the\\\", and Ilāh, \\\"God\\\"'. KLN_1966.txt ff-page 35 s.v. albatross: 'Port. alcatraz … a variant of alcatruz, \\\"the bucket of a water wheel\\\", fr. Arab. al-qādūs, \\\"machine for drawing water; jar\\\", fr. al-, \\\"the\\\", and Gk. κάδος … The name was orig. applied to the pelican as \\\"the water carrier\\\"' — Nourai's gloss 'water carrier, albatross' is Klein's sentence. ff-page 36 s.v. alembic: 'fr. Arab. al-anbīq, \\\"the still\\\" … and Gk. ἄμβιξ'. ff-page 77 s.v. aubergine: 'fr. Arab. al-bādinjān … fr. Pers. bādin-gan, fr. OI. vatin-ganah'. ff-page 52 s.v. anil: 'Port. anil, fr. Arab. an-nīl, assimilated fr. al-nīl … fr. Pers. nīla, ult. fr. OI. nīlī'. All five of Nourai's words are Klein's, with his glosses.\"),\n   rc(\"AHD\", \"not_checked\", \"Semitic/Iranian loans with no entry in the only AHD text available (the IE-roots appendix).\"),\n   NOT_OEW],\n \"consulted\": [\n   co(\"LKT\", \"LKT.txt ff-page 106 (qādūs), ff-page 41 (bādinjān), ff-page 91/125 (qubba, for comparison)\", \"supports\",\n      \"qādūs: 'Aus dem pg. alcadroz entwickelte sich angloind. albatross, engl. albatros, albatross, frz. albatros, sp. alcatraz, dtsch. Albatros \\\"Diomedea exulans L.\\\"'; bādinjān: '… sp. berengena, pg. beringela, kat. alberginera, frz. aubergine …'.\"),\n   co(\"DEV\", \"DEV.txt ff-page 32 (Alambic, Albatros) and ff-page 73 (Aubergine)\", \"supports\",\n      \"'Alambic. Esp. alambique, port. lambique, ital. lambico, de l'arabe الأنبيق al-anbiq, venant du grec ἄμβιξ vase à distiller, précédé de l'article arabe al.'; 'Albatros … est une altération de l'espagnol et portugais alcatraz … Je ne doute pas qu'il ne faille l'assimiler au portugais alcatruz, signifiant seau d'une noria'; 'Le nom arabe-persan باذنجان bâdindjân …'.\"),\n   co(\"Wiktionary\", W+\"%D8%A8%D8%A7%D8%B0%D9%86%D8%AC%D8%A7%D9%86\", \"supports\",\n      \"Arabic بَاذِنْجَان bāḏinjān: 'Borrowed from Classical Persian بَاذِنْگَان (bāzingān), an Indo-Aryan borrowing, from Sanskrit वातिङ्गण (vātiṅgaṇa), from Dravidian' — Nourai's ☞Vatin-ganah exactly.\"),\n   co(\"PLA\", \"Asbaghi s.v. nīl / nīlaǧ (PLA_asbaghi_1988_ia_djvu.txt)\", \"supports\",\n      \"'nīl: \\\"blau\\\" pers., mp. nīl'; 'nīlaǧ: \\\"Isatis tinctoria, getrockneter Indigosaft; Indigo\\\" pers. nīl, mp. nīl \\\"Indigo\\\"' — the Arabic al-nīl is a Persian loan, as Nourai's ☞Nei 1 implies.\")\n ]})\n\n# ---------------- node 15 ----------------\nnodes.append({\n \"id\": 15, \"lang\": \"English\", \"words\": \"Allah; albatross; alembic; aubergine; anil, aniline\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Allah entered English in 1702 (Alha) directly from Arabic as a religious term. albatross, 1670s, is an alteration (after Latin albus 'white', for the bird's plumage) of Spanish/Portuguese albatros < alcatraz 'pelican, cormorant', from al-qādūs; OED prints Nourai's al-qādūs route, Barnhart prefers al-ghaṭṭās 'the diver', so Nourai has picked the better-documented of the two. alembic is late 14c. (earlier limbeck mid-14c.) from Old French alambic < Old Spanish alambique < al-anbīq. aubergine, 1775, is French aubergine < Catalan alberginera (the regular French change of al- to au-) < al-bādhinjān. anil is 1580s from Portuguese/French anil < an-nīl (assimilated al-nīl), and aniline is a chemical coinage of 1841 (C. J. Fritzsche) on anil + -ine. The chart's straight Arabic→English arrows compress the Iberian, French and Portuguese intermediaries, but the root box itself says so ('Most of these Arabic words have reached Europe through Spanish and French').\",\n \"sources\": [E+\"Allah\", E+\"albatross\", E+\"alembic\", E+\"aubergine\", E+\"anil\"],\n \"ref_check\": [\n   rc(\"AHD\", \"not_checked\", \"Main-dictionary entries; the 1975 New College Edition is lending-only and the local AHD file is the IE-roots appendix only.\"),\n   NOT_OEW],\n \"consulted\": [\n   co(\"KLN\", \"KLN_1971.txt s.v. Allah; KLN_1966.txt ff-pages 35, 36, 77, 52\", \"supports\",\n      \"Klein has all five English words with the Arabic al- etymon and the Romance intermediary: 'albatross, n. — Port. alcatraz'; 'alembic, n. — ME., fr. OF. (=F.) alambic, fr. OSp. (= Sp.) alambique'; 'aubergine … fr. Catal. alberginera'; 'anil … Port. anil'.\"),\n   co(\"Etymonline\", E+\"albatross\", \"partial\",\n      \"'probably from Spanish or Portuguese albatros, an alteration of alcatraz … This name is perhaps from Arabic al-ghattas \\\"sea eagle\\\" [Barnhart]; or from Portuguese alcatruz \\\"the bucket of a water wheel\\\" [OED 1989], from Arabic al-qadus … The spelling was influenced by Latin albus \\\"white\\\".' — Nourai's al-qādūs is the OED option; a rival Arabic etymon exists.\"),\n   co(\"LKT\", \"LKT.txt ff-page 106, ff-page 41\", \"supports\",\n      \"Lokotsch's descendant lists end in exactly these English words: 'angloind. albatross, engl. albatros, albatross'; 'frz. aubergine' (English aubergine being the French form taken over unchanged).\")\n ]})\n\n# ---------------- node 16 ----------------\nnodes.append({\n \"id\": 16, \"lang\": \"Arabic\", \"words\": \"al-iksir; al-a`sârah; al-jabr-w`al- moqâbeleh; al-kîmîyâ; al-oud\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Five al- forms of the Arabic scientific vocabulary. الإكسير al-iksīr 'the philosophers' stone, the dry medicine' is late Greek ξηρίον xērion 'drying powder for wounds' (from ξηρός xēros 'dry' — Nourai's ☞Ksero) taken over with the article. العصارة al-ʿaṣāra 'the pressed-out juice', from عصر ʿaṣara 'he squeezed' (☞A`.s.r), was the Levantine trade name of madder root (alizari) and gave the dye name alizarin. الجبر والمقابلة al-jabr wa-l-muqābala 'restoration and balancing' is the title of al-Khwārizmī's treatise, al-jabr from جبر jabara 'to set (a bone), reunite' (☞J.b.r) — which is why Spanish algebrista still means 'bone-setter'. الكيمياء al-kīmiyāʾ is from Greek χημεία khēmeia, itself of contested origin: either Egyptian khem/kēme 'the black land' (Nourai's ☞Kers 2) or χεῖν khein 'to pour' (☞Gheu); Nourai cites both, which is the honest position, though Klein calls the second folk etymology. العود al-ʿūd 'the wood' is the Arab lute; the aloewood sense of ʿūd is why Nourai cross-refers ☞Agaruth (Sanskrit agaru 'aloewood').\",\n \"sources\": [E+\"elixir\", E+\"algebra\", E+\"alchemy\", E+\"lute\", W+\"alizarin\"],\n \"ref_check\": [\n   rc(\"KLN\", \"supports\",\n      \"KLN_1966.txt ff-page 277 s.v. elixir: 'ML., fr. Arab. al-iksir … and Gk. ξηρίον, \\\"dry medicinal substance, cataplasm\\\", fr. ξηρός \\\"dry\\\"'. ff-page 38 s.v. alizari: 'F., fr. Sp. alizari, fr. Arab. al-ʿaṣārah, \\\"the juice\\\", fr. al-, \\\"the\\\", and ʿaṣara, \\\"he squeezed, pressed\\\"' — Nourai's transliteration 'al-a`sârah' and gloss 'the juice' are Klein's verbatim. ff-page 37 s.v. algebra: 'Fr. Arab. al-jabr … \\\"reunion (of broken parts in equations)\\\", short for al-jabr w'al-muqābalah, \\\"reunion and comparison\\\", title of a work written by Mohammed ibn Musa al-Khowarizmi' — Nourai's gloss 'reunion and comparison' is Klein's phrase. ff-page 35 s.v. alchemy: 'fr. ML. alchemia, fr. Arab. al-kimiyā … fr. MGk. χημεία, prop. \\\"the art of the black land (Egypt)\\\" … The derivation from Gk. χύσις, \\\"pouring\\\" … is folk etymology.'\"),\n   rc(\"AHD\", \"not_checked\", \"Main-dictionary entries only; not open online.\"),\n   NOT_OEW],\n \"consulted\": [\n   co(\"LKT\", \"LKT.txt no. 903 (ff-page 99), the alizari entry (ff-page 37), the alchimia entry (ff-page 120), the lute entry (ff-page 195)\", \"supports\",\n      \"no.903: 'Ar. iksīr: [Aus gr. ξηρίον \\\"das Trockene\\\"] \\\"Stein der Weisen\\\" … hieraus it. elissire, frz. elixir'; alizari: '… hieraus sp. frz. alizari als Handelsausdruck für garance \\\"Färberröte, Krapprot\\\" und weiter der chemische Ausdruck Alizarin'; kīmiyā: 'dann \\\"Scheidekunst, Chemie\\\". Aus dem Ar. kommt: it. alchimia … frz. alchimie, chimie'; ʿūd: '… it. liuto, afrz. leüt, frz. luth, sp. laud, pg. alaude … engl. lute, dtsch. Laute'.\"),\n   co(\"PHN\", \"PHN.txt ff-page 271, s.v. LUTH\", \"supports\",\n      \"'LUTH, s. m. (a.) العود [al-‘oud] le bois en général, et en particulier le bois d'aloès. Nom d'un instrument de musique à cordes … on y parvient soit à l'aide de l'espagnol laud, soit au moyen du portugais alaude, dans lequel l'article al figure intégralement.' Pihan even supplies Nourai's 'the wood' gloss and the aloeswood association.\"),\n   co(\"PLA\", \"Asbaghi s.v. kīmiyā\", \"contradicts\",\n      \"'kīmiyā: \\\"Chemie\\\" pers.' — Asbaghi files the Arabic word among Persian loanwords, a minority position against Klein's and Etymonline's Greek/Egyptian derivation; worth recording as a dissenting voice on Nourai's ☞Kers 2/Gheu.\"),\n   co(\"DEV\", \"DEV.txt ff-page 44 s.v. Algèbre\", \"supports\",\n      \"'Algèbre. Esp. portug. et ital. algebra. De l'arabe الجبر al-djebr, réduction. On nomme l'algèbre علم الجبر والمقابلة, science des réductions et des comparaisons. En espagnol, algebrista se dit du bailleul ou rebouteur, qui réduit les fractures.'\")\n ]})\n\n# ---------------- node 17 ----------------\nnodes.append({\n \"id\": 17, \"lang\": \"English\", \"words\": \"elixir; alizarin; algebra; alchemy, chemistry; lute, flute, aloe\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Four of the five lines are right. elixir, mid-13c., from ML elixir < al-iksīr. alizarin, from French alizarine (1830s–50s dye chemistry) = alizari + -in, alizari being the Levantine madder trade-name from al-ʿaṣāra. algebra, 1550s, from ML algebra < al-jabr (the accent moved from the second to the first syllable in the 17th c.; English also used algebra for 'bone-setting' in the 15th–16th c., from Arab medical men in Spain). alchemy, mid-14c., from Old French alquemie/alchimie < ML alkimia < al-kīmiyāʾ, with chemistry a c.1600 back-formation on chemist (French chimiste < ML alchimista, the al- shed). lute, late 13c., from Old French lut/leüt < Old Provençal laut, 'a misdivision of Arabic al-ʿūd … where al is the definite article'. But the last two words of the last line do not belong: flute (early 14c. floute, OF flaüte, OProv flaüt) is of uncertain origin — perhaps imitative, perhaps from Latin flare 'to blow' — and is at most 'influenced by' or blended with laüt 'lute' (Klein: 'prob. a blend of OProvenç. flaujol \\\"flageolet\\\" and laüt \\\"lute\\\"'), not descended from al-ʿūd. aloe is not an Arabic al- word at all: it is Latin aloe < Greek ἀλόη, of uncertain (probably Oriental) origin, with the older English 'fragrant heartwood' sense coming from the Biblical translators' use of aloe for Hebrew ʾăhālīm, ultimately perhaps Dravidian (Sanskrit agaru — which is exactly what Nourai's own ☞Agaruth points at, so his cross-reference contradicts his arrow). Because two words of the node are wrongly filiated to al-, the node is disputed.\",\n \"sources\": [E+\"elixir\", E+\"algebra\", E+\"alchemy\", E+\"chemistry\", E+\"lute\", E+\"flute\", E+\"aloe\", W+\"alizarin\"],\n \"ref_check\": [\n   rc(\"KLN\", \"partial\",\n      \"Klein supports elixir, alizarin, algebra, alchemy and (implicitly, via alizari) the dye; but KLN_1966.txt ff-page 327 s.v. flute: 'ME. floute, floite, fr. OF. flaüte, fleüte (F. flûte), fr. OProvenç. flaüt, which is prob. a blend of OProvenç. flaujol, \\\"flageolet\\\", and laüt, \\\"lute\\\"' — a blend, not a descent; and ff-page 41 s.v. aloe: 'L. aloe, fr. Gk. ἀλόη, \\\"aloe\\\", prob. borrowed fr. Heb. ahalim, ahalōth (pl.), which are perhaps borrowed fr. OI. agaruh, aguruh, \\\"aloewood\\\", these latter being prob. of Dravidian origin' — no Arabic al- anywhere.\"),\n   rc(\"AHD\", \"not_checked\", \"Main-dictionary entries; not open online.\")],\n \"consulted\": [\n   co(\"Etymonline\", E+\"aloe\", \"contradicts\",\n      \"'late 14c., originally in reference to the drug, from Latin aloe, from Greek aloē, which is of uncertain origin, probably a loan-word from an Oriental language. A secondary sense is older in English: \\\"Fragrant resin or heartwood of an East Indian tree\\\" … which is from misuse of Latin/Greek aloe in Biblical translations for Hebrew akhalim (plural), which ultimately is perhaps from a Dravidian language.'\"),\n   co(\"Etymonline\", E+\"flute\", \"contradicts\",\n      \"'early 14c., floute … from Old Provençal flaut, which is of uncertain origin. Perhaps imitative or from Latin flare \\\"to blow\\\" … perhaps influenced by Provençal laut \\\"lute\\\".'\"),\n   co(\"Etymonline\", E+\"lute\", \"supports\",\n      \"'late 13c., from Old French lut, leut …, from Old Provençal laut, a misdivision of Arabic al-'ud, the Arabian lute, literally \\\"the wood\\\" (source of Medieval Latin lutana, Spanish laud, Portuguese alaude, Italian liuto), where al is the definite article.'\"),\n   co(\"Wiktionary\", W+\"alizarin\", \"supports\",\n      \"'Borrowed from French alizarine, corresponding to alizari + -in.'\"),\n   co(\"LKT\", \"LKT.txt ff-page 195 (Laute), ff-page 37 (alizari), ff-page 120 (Alchimie)\", \"supports\",\n      \"Lokotsch's descendant chains end in 'engl. lute', 'Alizarin … frz. alisarine', 'frz. alchimie, chimie' — but he has no entry attaching either flute or aloe to Arabic.\")\n ]})\n\n# ---------------- node 18 ----------------\nnodes.append({\n \"id\": 18, \"lang\": \"Arabic\", \"words\": \"al-bîrquq; dr-as-sanâ; as-sumut; Jabal-al-Târiq; al-qubbah\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Five more al- exports, three of them showing the assimilation the root box describes. البرقوق al-birqūq/al-barqūq is Byzantine Greek βερικόκκιον berikokkion, itself Latin (mālum) praecoquum 'early-ripening (fruit)' (Nourai's ☞Pekw = PIE *pekʷ- 'to cook, ripen'); his parenthesis '(plum)' is exact, because modern Arabic barqūq means 'plum', the apricot being mishmish. دار الصناعة dār aṣ-ṣināʿa 'house of manufacture' (☞S.n.`a, D.v.r) shows al- assimilated to ṣ before a sun letter — Nourai's 'dr-as-sanâ' is the book's shorthand for it. السموت as-sumūt, plural of السمت as-samt 'the way, direction' (☞Mei 3), again with sun-letter assimilation. جبل طارق Jabal Ṭāriq 'mountain of Ṭāriq', after Ṭāriq b. Ziyād, who landed there in 711 and opened the conquest of Spain (☞J.b.l 'mountain'); note that the received Arabic name has no article between the two words, so the al- Nourai writes is Klein's citation form rather than standard Arabic. القبة al-qubba 'the vault, vaulted chamber, vaulted tent', from the Semitic base q-b-b 'to be bent, vaulted' (☞Gabbah).\",\n \"sources\": [E+\"apricot\", E+\"arsenal\", E+\"azimuth\", E+\"Gibraltar\", E+\"alcove\"],\n \"ref_check\": [\n   rc(\"KLN\", \"supports\",\n      \"KLN_1966.txt ff-page 62 s.v. apricot: 'F. abricot, fr. Port. albricoque, fr. Arab. al-barqūq, fr. al-, \\\"the\\\", and πραικόκιον, Grecized form of L. praecoquum, \\\"apricot\\\" … praecox, \\\"early ripe\\\"'. ff-page 68 s.v. arsenal: 'It. arsenale (OIt. arzanale), \\\"dock\\\", borrowed — prob. through the medium of MGk. ἀρσηνάλης — fr. Arab. dār-aṣ-ṣināʿah … lit. \\\"house of construction\\\", fr. dār, \\\"house\\\", aṣ-, assimilated form of al-, \\\"the\\\", and ṣināʿah, \\\"construction, art\\\", fr. ṣanaʿa, \\\"he made\\\"' — Klein even makes the assimilation point Nourai's root box makes. ff-page 83 s.v. azimuth: 'F. azimut, fr. Arab. as-sumūt, pl. of as-samt, \\\"the way\\\", fr. as-, assimilated form of al-, \\\"the\\\", and samt, \\\"way\\\"'. ff-page 354 s.v. Gibraltar: 'Fr. Arab. jabal (in vulgar pronunciation jebel) al Tāriq, \\\"mount of Tariq\\\", named after Tariq, the Moslem invader of Spain who landed there in 711' — including Nourai's date. ff-page 36 s.v. alcove: 'F. alcôve, fr. Sp. alcoba, fr. Arab. al-qubbah, fr. al-, \\\"the\\\", and qubbah, \\\"arch, vaulted tent\\\"'. Every one of Nourai's five words and glosses is Klein's.\"),\n   rc(\"AHD\", \"not_checked\", \"Main-dictionary entries, not open online.\"),\n   NOT_OEW],\n \"consulted\": [\n   co(\"LKT\", \"LKT.txt ff-page 47 (barqūq), ff-page 66 (dār aṣ-ṣināʿa), ff-page 172 (samt), ff-page 91/125 (qubba)\", \"supports\",\n      \"barqūq: '[ar. barqūq hat übrigens die Bedeutung \\\"Pflaume\\\" erhalten, während die Aprikose mishmish heißt]; hieraus sp. albaricoque … frz. abricot … engl. apricot' — Lokotsch confirms Nourai's '(plum)'. dār aṣ-ṣināʿa: 'it. darsena … arzanà, arsenale, terzana \\\"Zeughaus\\\"; frz. darse … arsenal … engl. arsenal'. samt: 'plr. sumūt, simūt; hieraus mit ar. Art. it. azimut, azimutto, frz. azimut … engl. azimuth'. qubba: 'Bogen, Gewölbe … dtsch. Alkoven … ndl. alkoof, engl. alcove'.\"),\n   co(\"DEV\", \"DEV.txt ff-page 28 (Abricot), ff-page 40 (Alcôve)\", \"supports\",\n      \"'Abricot … Parti du latin praecox, précoce, passé chez les Grecs sous la forme πραικόκκιον, il a été adopté par les Arabes, qui en ont fait, avec l'article, البرقوق al-barqoûq ou al-birqoûq. Puis il est revenu dans les langues romanes'; 'Alcôve. Esp. alcoba, portug. alcova, ital. alcova; de l'arabe القبة al-qobba, qui, entre autres sens, a celui de petite chambre, cabinet.'\"),\n   co(\"Etymonline\", E+\"Gibraltar\", \"supports\",\n      \"'1590s, ancient Calpe, captured 710 C.E. by Saracen leader Tariq, renamed Jebel el Tarik \\\"the Mountain of Tarik\\\", hence the English name.'\")\n ]})\n\n# ---------------- node 19 ----------------\nnodes.append({\n \"id\": 19, \"lang\": \"English\", \"words\": \"apricot; arsenal; azimuth; Gibraltar; alcove\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"apricot, 1550s abrecock, from Catalan abercoc / Portuguese albricoque < al-birqūq, the modern form assimilated to French abricot; the fruit was introduced to England in 1524. arsenal, c.1500 'dockyard, dock with naval stores', from Italian arzenale (Venetian arzanà, the great Arsenale of Venice) < dār aṣ-ṣināʿa; the sense 'store of weapons' is 1570s. azimuth, late 14c., from Old French azimut < as-sumūt (its doublet zenith comes from the singular samt ar-raʾs, with -m- misread as -ni- by Latin scribes). Gibraltar, 1590s, from Jabal Ṭāriq, ancient Calpe. alcove, 1670s, from French alcôve < Spanish alcoba < al-qubba. Nourai's direct Arabic→English arrows again pass over the Italian, Iberian and French carriers, which the root box's own note covers.\",\n \"sources\": [E+\"apricot\", E+\"arsenal\", E+\"azimuth\", E+\"Gibraltar\", E+\"alcove\"],\n \"ref_check\": [\n   rc(\"KLN\", \"supports\",\n      \"See node #18: KLN_1966.txt has all five English words with these Arabic etyma and the Romance intermediaries — 'apricot, n. — F. abricot, fr. Port. albricoque'; 'arsenal, n. … — It. arsenale'; 'azimuth, n. … — F. azimut'; 'Gibraltar, n. … — Fr. Arab. jabal … al Tāriq'; 'alcove, n. … — F. alcôve, fr. Sp. alcoba'.\"),\n   NOT_OEW],\n \"consulted\": [\n   co(\"Etymonline\", E+\"arsenal\", \"supports\",\n      \"'c. 1500, \\\"dockyard, dock with naval stores\\\", from Italian arzenale, from Arabic dar as-sina'ah \\\"workshop\\\", literally \\\"house of manufacture\\\", from dar \\\"house\\\" + sina'ah \\\"art, craft, skill\\\", from sana'a \\\"he made\\\". The word was applied by the Venetians to a large wharf in their city.'\"),\n   co(\"Etymonline\", E+\"azimuth\", \"supports\",\n      \"'late 14c., from Old French azimut, from Arabic as-sumut \\\"the ways\\\", plural of as-samt \\\"the way, direction\\\"' — with the zenith entry explaining the scribal m→ni misreading.\"),\n   co(\"LKT\", \"LKT.txt ff-pages 47, 66, 172, 125\", \"supports\",\n      \"Lokotsch's chains terminate in 'engl. apricot', 'engl. arsenal', 'engl. azimuth', 'engl. alcove \\\"Zimmerwinkel für Sitz oder Bett\\\"'.\"),\n   co(\"SKT\", \"SKT.txt ff-page 640\", \"supports\",\n      \"Skeat's summary lists of orientalisms put this whole class under 'French from Arabic' and 'Spanish from Arabic', i.e. the Iberian/French carriers Nourai's root note names.\")\n ]})\n\ndoc = {\n \"pdf_page\": 47,\n \"book_page\": 17,\n \"verified_by\": \"claude-fable-5-1\",\n \"verified_on\": \"2026-09-04\",\n \"entries\": [{\n   \"entry\": 0,\n   \"root\": \"Al 3\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Arabic ال al- , the definite article 'the', proclitic and inseparable; assimilated to a following 'sun letter' (t, ṯ, d, ḏ, r, z, s, š, ṣ, ḍ, ṭ, ẓ, l, n): al-šams > aš-šams\",\n   \"note\": \"The root box is right on all three counts: the language label (Arabic), the form (al- used as a prefix) and the gloss ('definite article \\\"the\\\"'), and its printed note about assimilation is the standard sun-letter rule, which Persian grammars teach unchanged (Platts–Ranking §10, 'solar letters … lunar letters'). Nourai's added remark that 'most of these Arabic words have reached Europe through Spanish and French' is also correct and is confirmed word by word by Klein, Devic and Lokotsch — though the carriers are wider than Spanish and French alone (Italian for arsenal and lute, Portuguese for albatross and anil, Catalan for aubergine and apricot). Three problems in the chart itself: (1) 'Amir al-bahr' as the source of admiral is rejected by Klein (who prefers amīr-ar-raḥl), by Devic (who attributes it to Engelmann and calls it 'guère admissible') and by Lokotsch ('wenig wahrscheinlich'); the OED accepts only the generic amīr-al-. (2) 'az-zarnîx : arsenic' is a real Arabic word but not the source of European arsenic — Greek arsenikon was taken from Iranian *zarnika- through Syriac zarnīkā centuries before Arabic, and Latin/Old French carried it to English; Watkins (AHD, root *ghel-2) says 'Syriac zarnikā, orpiment: ARSENIC'. (3) 'aloe' under al-oud is wrong — aloe is Greek ἀλόη of uncertain, probably Semitic-or-Dravidian ancestry, and Nourai's own cross-reference ☞Agaruth (Sanskrit agaru) points at that different etymology; 'flute' on the same line is at best a blend with laüt 'lute', not a descendant of al-ʿūd. Everything else on the page is standard and well supported. The Persian script of the page was checked against the page image (pdftoppm p.47): «آلفا آلفا» for âlfâlfâ really is printed as two words in the book, so the JSON is a faithful transcription and no transcription_suspect verdict is warranted.\",\n   \"sources\": [\"https://www.etymonline.com/word/al-\", \"https://www.etymonline.com/word/Allah\", \"https://ahdictionary.com/word/indoeurop.html\"],\n   \"ref_check\": [\n     {\"ref\": \"SAP:43\", \"status\": \"not_checked\",\n      \"note\": \"Ahmad Sayyah's Farhang (the Persian rendering of al-Munjid) is available only as a paid ebook (fidibo.com/book/142427 and /142430); refs_online.json records kind='purchase' with no scan anywhere, so p.43 could not be read. The claim it is cited for — that al- is the Arabic definite article prefixed to nouns, with sun-letter assimilation — is elementary and is confirmed by Platts–Ranking's Persian grammar (GPL ff-page 27) and by Klein passim ('fr. al-, \\\"the\\\"').\"}\n   ],\n   \"consulted\": [\n     co(\"GPL\", \"GPL.txt ff-page 27, §10 (Platts & Ranking, A Grammar of the Persian Language)\", \"supports\",\n        \"'… called \\\"solar letters\\\" (huruf-i shamsiya … al-hurufu 'sh-shamsiya), because the word شمس \\\"sun\\\" happens to begin with one of them; and the remaining letters of the Arabic alphabet, \\\"lunar letters\\\" (huruf-i qamariya …), because the word قمر qamar \\\"moon\\\" begins with one of them.' Exactly the rule Nourai states in the box.\"),\n     co(\"KLN\", \"KLN_1966.txt, passim (e.g. ff-pages 35–38: alchemy, alcohol, alcove, alembic, alkali, alizari)\", \"supports\",\n        \"Klein's standard formula for this whole class is 'fr. Arab. al-X, fr. al-, \\\"the\\\", and X' — e.g. 'alcove … fr. Arab. al-qubbah, fr. al-, \\\"the\\\", and qubbah, \\\"arch, vaulted tent\\\"'; and he spells out the assimilation at arsenal: 'aṣ-, assimilated form of al-, \\\"the\\\"'.\"),\n     co(\"Etymonline\", \"https://www.etymonline.com/word/al-\", \"supports\",\n        \"'al- : in words from Arabic (or assumed to be), it is the definite article \\\"the\\\" … Often assimilated to following consonants (as-, az-, ar-, am-, an-, etc.). Examples include almanac, alchemy, alcohol, algebra.'\"),\n     co(\"LKT\", \"LKT.txt, passim (the recurring formula 'hieraus mit ar. Art. …')\", \"supports\",\n        \"Lokotsch's whole dictionary marks this class with the phrase 'hieraus mit ar. Art.' ('hence, with the Arabic article'), e.g. at samt: 'hieraus mit ar. Art. it. azimut, azimutto, frz. azimut … engl. azimuth'.\")\n   ],\n   \"nodes\": nodes\n }]\n}\n\nwith open(\"data/verification/page-47.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(doc,f,ensure_ascii=False,indent=1)\nprint(\"written\", len(nodes), \"nodes\")\nPYEOF\npython3 -m json.tool data/verification/page-47.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-04T19:47:04.252Z] TOOL RESULT

```
written 19 nodes
JSON OK
```


## [2026-09-04T19:47:08.424Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 tools/verify_check.py 47"
}
```


### [2026-09-04T19:47:10.302Z] TOOL RESULT

```
nodes verified: 19/19
node verdicts: {'confirmed': 10, 'plausible': 6, 'disputed': 3}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 5, 'contradicts': 4, 'supports': 8, 'not_checked': 21}
books consulted: {'supports': 45, 'partial': 14, 'contradicts': 6} | by book: {'LKT': 13, 'Etymonline': 12, 'DEV': 8, 'Wiktionary': 8, 'SKT': 5, 'KLN': 5, 'MON': 4, 'PLA': 4, 'HUB': 2, 'GPL': 1, "Nourai's own page image": 1, 'BQT': 1, 'PHN': 1}
```


## [2026-09-04T19:47:27.404Z] AGENT

`verify_check.py 47` passes with no PROBLEM lines: 19/19 nodes verified.

**Page 47 (book p. 17), single entry — ROOT "Al 3" [Arabic], the definite article: confirmed**

- Node verdicts: **10 confirmed, 6 plausible, 3 disputed**. Root: confirmed (label, form and the sun-letter assimilation note are all correct; the "reached Europe through Spanish and French" remark is right, though Italian/Portuguese/Catalan also carry several).
- Ref checks: 8 supports, 5 partial, 4 contradicts, 21 not_checked (SAP, OEW and VOP have no accessible copy at all; AHD's main-dictionary entries are lending-only, only its IE-root appendix is readable).
- Books consulted: KLN, SKT, LKT, DEV, PHN, PLA (Asbaghi), HUB, BQT, MON, GPL, AHD (1985 + online appendix), plus Etymonline and Wiktionary; 24 web pages archived via `fetch_source.py`.

Disputed items:
- **#10 Arabic `az-zarnîx` → arsenic** — al-qilī and al-malgham are fine, but Greek *arsenikon* was taken from Iranian \*zarnika- through Syriac zarnīkā centuries before Arabic; Watkins (AHD *ghel-2) says "Syriac zarnikā, orpiment: ARSENIC".
- **#13 English arsenic** (same reason) — the al/az- in the chain is the Aramaic determinate state, not the Arabic article; Klein, Etymonline and Wiktionary all route it Greek → Latin → OF.
- **#17 English `aloe`, `flute` under al-oud** — aloe is Greek ἀλόη (Klein: from Heb. ʾahālōth, perhaps Skt. agaruh, i.e. Nourai's own ☞Agaruth contradicts his arrow); flute is at most a blend with OProv. laüt, not a descendant of al-ʿūd. Elixir, alizarin, algebra, alchemy and lute on the same node are solid.

Also worth flagging (kept at *plausible*, not disputed): **`Amir al-bahr` → admiral** (#2/#3) — Klein prefers *amīr-ar-raḥl*, Devic calls the *baḥr* guess "guère admissible", Lokotsch "wenig wahrscheinlich"; only the generic *amīr-al-* is accepted (OED). Skeat and Mo'in (who glosses آدمیرال as [ع. امیرالبحر]) still print Nourai's version.

No transcription_suspect: the odd Persian «آلفا آلفا» for *âlfâlfâ* (#4) was checked against the page image at 500 dpi — the book really prints it as two words, so the JSON is faithful.
