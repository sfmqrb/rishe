# Verification process log — verify-page-60


## [2026-09-04T22:40:45.546Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 60 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-60.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-60.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-60.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 60` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T22:40:47.562Z] AGENT

I'll start by reading the instructions and the relevant files.


## [2026-09-04T22:40:49.674Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T22:40:49.685Z] TOOL RESULT

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


## [2026-09-04T22:40:49.893Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-60.txt"
}
```


### [2026-09-04T22:40:49.905Z] TOOL RESULT

```
1	=== PDF page 60 (book page 30) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Apo, Apâ, Apu, Pu 3, Pô 1 : off  (refs POK:53)  PART 2
4	#1 (parent #0) [Germanic] refs=AHD | af : of ; apo-tero : after ; eben : later time, evening ; afug : turned back
5	  #2 (parent #1) [English] refs=None | of, off ; after ; evening ; awkward
6	#3 (parent #0) [Indo-European] refs=POK:841; AHD:1506 | P-os, Pos : after, behind
7	  #4 (parent #3) [Avestan / Old Persian] refs=POK:842 | pasča, pasca, pasâ : after, behind ; paskât : from behind here
8	    #5 (parent #4) [Persian] refs=HRN:70; BQT:403; IEC:29 | pas «پس ۱» : after | extra: پسین ، واپسین ، پسوند ، پس‌انداز
9	  #6 (parent #3) [Sogdian] refs=SOD:55,300 | `pyš, pš : then, afterwards
10	  #7 (parent #3) [Latin] refs=AHD | post : after ; pônere : to place
11	    #8 (parent #7) [English] refs=None | postpone ; oppose, propose, compose, impose, posture
12	--- entry 1 ---
13	ROOT Apu -> redirect to Apo
14	--- entry 2 ---
15	ROOT Aq -> redirect to Ak
16	--- entry 3 ---
17	ROOT [Syriac] A`.q.b : to follow, succeed  (refs KLN:823)
18	#1 (parent #0) [Arabic] refs=KLN:823; FVQ:291 | a`.q.b : to follow ; a`qeb : heel ; Ya`qŭb : A prophet's name (follower, successor)
19	  #2 (parent #1) [Persian] refs=FVA:276 | aqab «عقب» : back, behind ; Ya`qŭb «یعقوب» : Jacob | extra: تعقیب ، عقبیٰ ، عقوبت ، عاقبت
20	#3 (parent #0) [Hebrew] refs=KLN:823; FSD:1307 | âqebh : heel ; Ya`aqôbh : one that takes by the heel, follower, name of a prophet
21	  #4 (parent #3) [Greek] refs=FSD:1307 | Jacobos
22	    #5 (parent #4) [Late Latin] refs=FSD:1307 | Jacobŭs
23	      #6 (parent #5) [French] refs=None | Jaques
24	        #7 (parent #6) [Persian] refs=MON | žâk «ژاک» | extra: ژاکلین
25	        #8 (parent #6) [English] refs=AHD:699 | Jacqueline
26	      #9 (parent #5) [English] refs=KLN:823 | Jacob, Jack, Jim, James
27	        #10 (parent #9) [Persian] refs=MON:1233 | jak «جَک» : jack (for lifting)
28	
```


## [2026-09-04T22:40:55.189Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat SOURCE_MATRIX.md"
}
```


### [2026-09-04T22:40:55.229Z] TOOL RESULT

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


## [2026-09-04T22:40:57.876Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','AHD','KLN','FVQ','FSD','HRN','BQT','IEC','SOD','MON','FVA','WLD','SYN','HUB','PHD','NYB','CHEUNG','AFM','PLA','SKT','WEB','ARY','BRT','KNT','LKT','AFA','DOZ','TTS']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False))\n    else: print(k,'MISSING')\n\""
}
```


### [2026-09-04T22:40:59.842Z] TOOL RESULT

```
<persisted-output>
Output too large (42.9KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bqxbdk69c.txt

Preview (first 2KB):
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)", "local_files": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_0
...
</persisted-output>
```


## [2026-09-04T22:41:04.659Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['AHD','KLN','FVQ','FSD','HRN','BQT','IEC','SOD','MON','FVA']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print('==',k, v.get('title'))\n    print('  page_offset:', v.get('page_offset'))\n    print('  lookup_hint:', (v.get('lookup_hint') or '')[:600])\n    print('  local_file:', v.get('local_file'), v.get('local_files'))\n\""
}
```


## [2026-09-04T22:41:05.230Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-60.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:6000])\n\""
}
```


### [2026-09-04T22:41:06.955Z] TOOL RESULT

```
== AHD W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)
  page_offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
  lookup_hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves 
  local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt None
== KLN E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  page_offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
  local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt ['/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt']
== FVQ Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
  page_offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves)
  lookup_hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
  local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] None
== FSD Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)
  page_offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
  local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt']
== HRN P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  page_offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
  local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt None
== BQT Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)
  page_offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
  lookup_hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=deh
  local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] None
== IEC S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  page_offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
  local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt None
== SOD Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  page_offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
  lookup_hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/Sog
  local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'] None
== MON Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)
  page_offset: None
  lookup_hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded a
  local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] None
== FVA S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989
  page_offset: None
  lookup_hint: Searched archive.org, ketabnak, noorlib, web: no digital copy found.
  local_file: None None
```


### [2026-09-04T22:41:08.911Z] TOOL RESULT

```
{
 "pdf_page": 60,
 "book_page": 30,
 "entries": [
  {
   "root": {
    "name": "Apo, Apâ, Apu, Pu 3, Pô 1",
    "lang": "Indo-European",
    "refs": "POK:53",
    "gloss": "off"
   },
   "part": 2,
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Germanic",
     "refs": "AHD",
     "words": [
      {
       "translit": "af",
       "gloss": "of",
       "script": null
      },
      {
       "translit": "apo-tero",
       "gloss": "after",
       "script": null
      },
      {
       "translit": "eben",
       "gloss": "later time, evening",
       "script": null
      },
      {
       "translit": "afug",
       "gloss": "turned back",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "English",
     "refs": null,
     "words": [
      {
       "translit": "of, off",
       "gloss": null,
       "script": null
      },
      {
       "translit": "after",
       "gloss": null,
       "script": null
      },
      {
       "translit": "evening",
       "gloss": null,
       "script": null
      },
      {
       "translit": "awkward",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 0,
     "lang": "Indo-European",
     "refs": "POK:841; AHD:1506",
     "words": [
      {
       "translit": "P-os, Pos",
       "gloss": "after, behind",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "Avestan / Old Persian",
     "refs": "POK:842",
     "words": [
      {
       "translit": "pasča, pasca, pasâ",
       "gloss": "after, behind",
       "script": null
      },
      {
       "translit": "paskât",
       "gloss": "from behind here",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 5,
     "parent": 4,
     "lang": "Persian",
     "refs": "HRN:70; BQT:403; IEC:29",
     "words": [
      {
       "translit": "pas",
       "gloss": "after",
       "script": "پس ۱"
      }
     ],
     "script_extra": "پسین ، واپسین ، پسوند ، پس‌انداز",
     "note": null,
     "quote": {
      "text": "آن نیست که حافظ را رندی بشد از خاطر - کاین سابقهٔ پیشین تا روز پسین باشد",
      "poet": "Hâfez"
     }
    },
    {
     "id": 6,
     "parent": 3,
     "lang": "Sogdian",
     "refs": "SOD:55,300",
     "words": [
      {
       "translit": "`pyš, pš",
       "gloss": "then, afterwards",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 3,
     "lang": "Latin",
     "refs": "AHD",
     "words": [
      {
       "translit": "post",
       "gloss": "after",
       "script": null
      },
      {
       "translit": "pônere",
       "gloss": "to place",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 8,
     "parent": 7,
     "lang": "English",
     "refs": null,
     "words": [
      {
       "translit": "postpone",
       "gloss": null,
       "script": null
      },
      {
       "translit": "oppose, propose, compose, impose, posture",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    }
   ]
  },
  {
   "root": {
    "name": "Apu",
    "redirect": "Apo"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Aq",
    "redirect": "Ak"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "A`.q.b",
    "lang": "Syriac",
    "refs": "KLN:823",
    "gloss": "to follow, succeed"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Arabic",
     "refs": "KLN:823; FVQ:291",
     "words": [
      {
       "translit": "a`.q.b",
       "gloss": "to follow",
       "script": null
      },
      {
       "translit": "a`qeb",
       "gloss": "heel",
       "script": null
      },
      {
       "translit": "Ya`qŭb",
       "gloss": "A prophet's name (follower, successor)",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Persian",
     "refs": "FVA:276",
     "words": [
      {
       "translit": "aqab",
       "gloss": "back, behind",
       "script": "عقب"
      },
      {
       "translit": "Ya`qŭb",
       "gloss": "Jacob",
       "script": "یعقوب"
      }
     ],
     "script_extra": "تعقیب ، عقبیٰ ، عقوبت ، عاقبت",
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 0,
     "lang": "Hebrew",
     "refs": "KLN:823; FSD:1307",
     "words": [
      {
       "translit": "âqebh",
       "gloss": "heel",
       "script": null
      },
      {
       "translit": "Ya`aqôbh",
       "gloss": "one that takes by the heel, follower, name of a prophet",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "Greek",
     "refs": "FSD:1307",
     "words": [
      {
       "translit": "Jacobos",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 5,
     "parent": 4,
     "lang": "Late Latin",
     "refs": "FSD:1307",
     "words": [
      {
       "translit": "Jacobŭs",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 6,
     "parent": 5,
     "lang": "French",
     "refs": null,
     "words": [
      {
       "translit": "Jaques",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 6,
     "lang": "Persian",
     "refs": "MON",
     "words": [
      {
       "translit": "žâk",
       "gloss": null,
       "script": "ژاک"
      }
     ],
     "script_extra": "ژاکلین",
     "note": null,
     "quote": null
    },
    {
     "id": 8,
     "parent": 6,
     "lang": "English",
     "refs": "AHD:699",
     "w
```


## [2026-09-04T22:41:16.568Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 53\" -B40 POK_full.txt | grep -n \"lemma:\" | tail -5; echo \"---apo---\"; awk 'BEGIN{RS=\"\\f\"} NR==62' POK_01.txt | head -60"
}
```


## [2026-09-04T22:41:17.059Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: pos\" POK_full.txt; echo \"===\"; grep -n \"lemma: apo\" POK_full.txt"
}
```


### [2026-09-04T22:41:18.341Z] TOOL RESULT

```
662:49363-Root / lemma: Rank- 
666:49367-Root / lemma: Ras-, Ras-no- 
702:49403-Root / lemma: Rat- 
755:49555-Root / lemma: Ras-, Ras- 
853:50993-Root / lemma: Re- 
---apo---
�� weg^  ab^;  maked. art-,  aß-]  alb.  prajpe  ^wieder^  zurück^  {*per-ape)]  lat.  ah  m.  Abl._,  ^von^ (vor  tönenden  Kons,  aus  ap^  das  noch  in  aperiö  aus  *ap-ueriö]  vielleicht auch  in  apricus,  s.  WH.  I  59;  über  lat.  af  s.  ebenda  1;  ahs  =  gr.  Ixip ^zurück;  wieder'^;  daraus  as-  vor  p-,  as-portö]  ä  vor  tönenden  Konsonanten)^, umbr.  ap-ehtre  ^ab  extra^  extrinsecus^  (über  andere^,  unsichere  osk.-umbr. Belege  s.  v.  Planta  I  209,  426,  II  454 f.);
got.  af  Präf.  und  Präp.  m.  Dat.  ,von,  von— weg,  von— her^,  anord.  af  Adv. und  Präp.  m.  Dat.,  ags.  ^/,  o/,  as.  a/,  ahd.  aba,  ab-  ,von,  von— weg^,  nhd.  ah-.
Vgl.  auch  lit.  apaciä  ,der  untere  Teil^  (als  ,abgewandter  Teil^,  *apotia, zu  ai.  dpatya-  n.  ,Nachkommenschaft^  und  hitt.  ap-pe-iz-zi-ia-as  (appeziias) ,hinterer^  Als  kelt.  Abkömmlinge  von  *apo  werden  in  Anspruch  ge- nommen acymr.  ncymr.  o  ,ex,  ab,  de*^,  a.-mcorn.,  a.-nbret.  a  ds.  Doch kommt  für  diese  lautarmen  brit.  Gebilde  eher  Zugehörigkeit  zu  air.  ö, ua  in  Betracht  (Thurnejsen  Gr.  524),  so  daß  alles  Brit.  ganz  unsicher bleibt.
In  hett.  a-ap-pa  (apa)  ,hinter,  zurück^  (^ö^-  ö''-  ^^o-dldo)iii  ,gebe  zurück^) sind  vielleicht  idg.  apo  und  epi  zusammengefallen  (Pedersen  Hitt.  188, Couvreur  H  94  f.,  Lohmann  IF.  51,  324  f.).
Ableitungen:  apo-tero-,  ap-ero-,  ap-io-,  ap-öko-  und  oben  apotiäj apetio-.
Ai.  apataram  Adv^.  ,weiter  weg^,  ap.  apataram  Adv.  ,abseits,  anderswo^, gr.  aTtwraqo)  ,weiter  entfernt^  («TrwTarcü  ,sehr  weit  entfernt^);  vielleicht got.  aftarö  ,von  hinten,  rückwärts^,  aftuma,  aftumists  ,der  letzte^,  ags. oßftemest  ds.  und  got.  aftra  ,zurück,  wiederum^,  ahd.  as.  aftar  Adv.  ,hinten, nach^  und  Präp.  m.  Dat.  ,nach,  hinter— her,  gemäße,  ags.  oefter  ds.,  anord. eptir  Adv.  und  Präp.  m.  Dat.  und  Akk.  ,nach^,  aptr  Adv.  ,zurück,  rückwärts^
Für  diese  gerüi.  Worte  steht  aber  auch  Verwandtschaft  mit  gr.  ^ircid^ev, idg.  *epi,  *opi  zur  Erwägung  (Schulze   KZ.  40,  414  Anm.  3),  vgl.  noch
54
got.  afta  ^hinten^;  ags.  oßft  ^binter^  später^,  got.  aftana  ,von  hinten^,  anord. a'ptan,  ag's.  ozftan,  as.  aftan,  mhd.  «/i^en  ^hernach^
Ai.  dpara-  ^hinterer;  späterer,  folgender;,  anderer^,  Adv.  -dm  ^nachher,' später^;  av.  ap.  apara-  ^hinterer,  späterer,  folgender^,  Adv.  -dm^  -am,  Sup. ai.  apamd-j  av.  apdma-  ,der  entfernteste,  letzte^;  got.  afar  Adv.  und  Präp. mit  Dat.  und  Akk.  ,nacb,  nachher^,  ahd.  avar,  abur  (letzteres  aus  *apu-rö-mj wie  anord.  cmr-  ^unterer,  hinterer^  in  Kompos.,  s.  Falk-Torp,  11  f.)  ^wieder, abermals,  dagegen^  (nbd.  aber),  anord.  afar  ,besonders,  sehr^  (vgl.  zur Bed.  ai.  dpara-  aucb  ,absonderlicb;  außergewöhnlich^,  Liden  Stud.  74  ff.; ags.  eafora,  as.  abaro  ,Nachkomme^).    S.  noch  *äpero-  ,Ufer'^.
Gr.  ärtLog  ,abgelegen,  fern*^  (wohl  auch  anord.  efja  f.  Bucht  in  einem Fluß,  in  der  die  Strömung  zurückläuft^,  ags.  ebba  m.  ,Ebbe^,  as.  ebbia  f., mn
```


### [2026-09-04T22:41:18.395Z] TOOL RESULT

```
68658:Root / lemma: pos 
===
6020:Root / lemma: apo-{p6, ap-u, pU) {*h2aph30^ 
6028:Root / lemma: apo-{p6, ap-u, pU) {*h2aph30-)\ "from, out, of derived from Root / lemma: 
6036:Gradually Root/ lemma: apo-{pd, ap-u, pU) {*h2aph30^\ "from, out, of became the prefix 
6180:podb 'below, under ' from Root / lemma: apo- {po, ap-u, pU)\ (from, out, of) not from Root 
9176:Root / lemma: apero- : " shore ' derived from Root / lemma: apo- {p6, ap-u, pU) {*h2aph30- 
67655:po-d-b " below, under ' from zero grade of Root / lemma: apo- {p6, ap-u, pU)\ (from, out, of)
```


## [2026-09-04T22:41:22.169Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6018,6035p' POK_full.txt; echo \"=====POS=====\"; sed -n '68658,68700p' POK_full.txt"
}
```


### [2026-09-04T22:41:22.291Z] TOOL RESULT

```
Page(s): 52 

Root / lemma: apo-{p6, ap-u, pU) {*h2aph30^ 

Meaning: from, out, of 

Note: 



Root / lemma: apo-{p6, ap-u, pU) {*h2aph30-)\ "from, out, of derived from Root / lemma: 

abh-(*/72abh-): "quick, abrupt' < Root/ lemma: sb'^ro-{^h2Sb'^ro^\ "strong, mighty' < root 

/pbh-(A?-): < with /-formant {n^'^eli): < Root/ lemma: {en^^-2)\ /7ebh-, errio'^-, /pb^-: " wet, 

damp; water; clouds '. 

=====POS=====
Root / lemma: pos 

Meaning: by, about, around, beside 

Note: probably *p+ os, Gen.-Abl. to Y^Jp-^ above S. 53 f. 

Material: Gr. in Arcadian-Cypriot and auf gr. Inschriften Phrygiens TToq, vor vowel also no-, 

geltungsgleich with rrpoc; (see *per'out - about', Nr. 8) and Doric rroTi; Lithuanian pas 

preposition "an, by'; probably also Old Church Slavic yoo in the meaning " behind, after'; 

compare das erhaltene 5- in Old Church Slavic poz-dbA6']. "late', poz-de Mn. "late', 

pozderije {paz-derije) "KaAapin, arunsTov'. To Lithuanian pas a\so pastaras'\he letzte, 

hinterste'. 



derivatives: 1. witli -//probably Armenian as/'after', Adverbal and preposition "after = 
secundum, gemaft'; in addition stor'the untere part'?; Latin post, Old Latin poste'aiter, 
behind ', ortlich and zeitlich, Adverbal and preposition m. Akk., Oscan pust, post, Umbrian 
post, pus'post' ortlich and zeitlich, preposition m. Abl., therefrom Latin posterns, Oscan 
pustrer\x\ postero', Umbrian postra, Latin postumus, Oscan pustmafsj 'postremae'; 
Umbrian postne, Latin poneirom *posti-ne, Oscan pustin, Umbrian pustin {irom *posti en) 
"je after' preposition m. Akk.; Umbrian pust-na/af' post\cas', purnaes ^post\c\s'; Latin 
/7c»s//c^s"hinten situated'. 

2. -ko-0\6 Indie /75sca(lnstr.) Adv. "behind, westlich, later' = Avestan pasca preposition 
" behind, after', ortlich and zeitlich. Old Indie pasca/ (Abl.) preposition " behind, after, 
westlich', Avestan paskatAdv. "vonhinten her, hinterdrein' spacial and zeitlich; Lithuanian 
paskul pasku/ (Dat) Adv. "afterwards, nachher', preposition "after'. 

3. In ending still controversial is ap. pasa ^aiter', preposition ortlich and zeitlich; alb. pas, 
Geg /77i6'as preposition " behind, after' (Indo Germanic *pos+ Demonstr. s/). 

References: WP. II 78 f., WH. II 347 ff., Trautmann 207, Schwyzer Gr. Gr. 2, 508. 
Page(s): 841-842 

Root / lemma: pot/s 

Meaning: owner, host, master, husband
```


## [2026-09-04T22:41:33.202Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==62' POK_01.txt | head -8; echo \"=====leaf63(p54-55)=====\"; awk 'BEGIN{RS=\"\\f\"} NR==63' POK_01.txt | head -30"
}
```


### [2026-09-04T22:41:35.388Z] TOOL RESULT

```
�� weg^  ab^;  maked. art-,  aß-]  alb.  prajpe  ^wieder^  zurück^  {*per-ape)]  lat.  ah  m.  Abl._,  ^von^ (vor  tönenden  Kons,  aus  ap^  das  noch  in  aperiö  aus  *ap-ueriö]  vielleicht auch  in  apricus,  s.  WH.  I  59;  über  lat.  af  s.  ebenda  1;  ahs  =  gr.  Ixip ^zurück;  wieder'^;  daraus  as-  vor  p-,  as-portö]  ä  vor  tönenden  Konsonanten)^, umbr.  ap-ehtre  ^ab  extra^  extrinsecus^  (über  andere^,  unsichere  osk.-umbr. Belege  s.  v.  Planta  I  209,  426,  II  454 f.);
got.  af  Präf.  und  Präp.  m.  Dat.  ,von,  von— weg,  von— her^,  anord.  af  Adv. und  Präp.  m.  Dat.,  ags.  ^/,  o/,  as.  a/,  ahd.  aba,  ab-  ,von,  von— weg^,  nhd.  ah-.
Vgl.  auch  lit.  apaciä  ,der  untere  Teil^  (als  ,abgewandter  Teil^,  *apotia, zu  ai.  dpatya-  n.  ,Nachkommenschaft^  und  hitt.  ap-pe-iz-zi-ia-as  (appeziias) ,hinterer^  Als  kelt.  Abkömmlinge  von  *apo  werden  in  Anspruch  ge- nommen acymr.  ncymr.  o  ,ex,  ab,  de*^,  a.-mcorn.,  a.-nbret.  a  ds.  Doch kommt  für  diese  lautarmen  brit.  Gebilde  eher  Zugehörigkeit  zu  air.  ö, ua  in  Betracht  (Thurnejsen  Gr.  524),  so  daß  alles  Brit.  ganz  unsicher bleibt.
In  hett.  a-ap-pa  (apa)  ,hinter,  zurück^  (^ö^-  ö''-  ^^o-dldo)iii  ,gebe  zurück^) sind  vielleicht  idg.  apo  und  epi  zusammengefallen  (Pedersen  Hitt.  188, Couvreur  H  94  f.,  Lohmann  IF.  51,  324  f.).
Ableitungen:  apo-tero-,  ap-ero-,  ap-io-,  ap-öko-  und  oben  apotiäj apetio-.
Ai.  apataram  Adv^.  ,weiter  weg^,  ap.  apataram  Adv.  ,abseits,  anderswo^, gr.  aTtwraqo)  ,weiter  entfernt^  («TrwTarcü  ,sehr  weit  entfernt^);  vielleicht got.  aftarö  ,von  hinten,  rückwärts^,  aftuma,  aftumists  ,der  letzte^,  ags. oßftemest  ds.  und  got.  aftra  ,zurück,  wiederum^,  ahd.  as.  aftar  Adv.  ,hinten, nach^  und  Präp.  m.  Dat.  ,nach,  hinter— her,  gemäße,  ags.  oefter  ds.,  anord. eptir  Adv.  und  Präp.  m.  Dat.  und  Akk.  ,nach^,  aptr  Adv.  ,zurück,  rückwärts^
Für  diese  gerüi.  Worte  steht  aber  auch  Verwandtschaft  mit  gr.  ^ircid^ev, idg.  *epi,  *opi  zur  Erwägung  (Schulze   KZ.  40,  414  Anm.  3),  vgl.  noch
54
=====leaf63(p54-55)=====
dd.  ebbe,  woher  nhd.  Ebbe  entlehnt,  als  , Abfluten'^).
Ai.  dpäka-  ,abseits  liegend,  entfernt,  von  vorn  kommend^,  arm.  haka- als  1.  Kompositionsglied  ,entgegen'^,  hakem  ,piegare  ad  una  parte,  inclinare^, aksl.  opaky  ,wiederum'^,  ksl.  opako,  opaky,  opace  ,zurück,  verkehrt^  in welchen  freilich  z.  T.  auch  zu  *opi,  gr.  otil^bv  gehörige  Formen  stecken können  (vgl.  lat.  opäcus  ,schattig^  =  ,von  der  Sonne  abgewendet^;  Liter, zur  Bildung  bei  Brugmann  Grdr.  IP  1,  482).  Daneben  anord.  ofugr  ,nach rückwärts  gekehrt^,  as.  abuh,  avuh,  ahd.  abuh,  abah  ,abgekehrt,  verkehrt, böse^  (nhd.  äbig,  äbicht),  ags.  *afoc  in  engl,  awkicard,  aus  *apu-ko-s  (oder aus  "^opu-ko-s :  ojtL&sv,  so  daß  im  Ablaut  zu  got.  ibiiks  ,rückwärts  gehend^, ahd.  ippihhön  ,zurückrollen^?  Johansson  PBrB.  15,  230,  im  Konsonanten auf  Ttv-yrj  verweisend,  s.  auch  Falk-Torp*  u.  avet).
po:
av.  pa-zdayeiti  ,läßt  wegrücken,*scheucht'^;  lat.  2:)o-sitiis,pönö  aus  *po-s[{]nö, po-liö,  po-lübrum,  pörcet  aus  *po-arcet]  alb.  pa  m.  Akk.  ,ohne-,  pa-  ,un-^ (Gl.  Meyer  Alb.  Wb.  317);  afries.  fän  ,von',  as./awa,  /an,  ahd./ona,  fon m.  Dat.  (=  *Abl.)  ,von^  (das  ahd.  -o-  ist  nach  Persson  IF.  2,  215  aus  idg. *pu  neben  *po  herzuleiten).  Eine  ähnliche  Form  sucht  Trautmann  Apr.  389 in  apr.  pan-s-dau  ,danach'^.  GänzKch  unsicher  ist,  ob  arm.  olork  ,poliert, schlüpfrig,  glatt'  nach  Liden  Arm.  St.  60  ff.  o-  aus  ""po-  enthält.  Dagegen hierher  trotz  vielfach  abweichender  Bed.  (Brugmann  Grdr.  II ^  2,  808 erwägt  Aufsaugung  von  idg.  "^upo,  und  für  sl.  po  in  der  Bed.  ,hinter, nach'  m.  Lok.  wohl  richtig  Entstehung  aus  '^pos):  aksl.  po  ,nach,  an,  bei, über  etwas  hin'  (lit.  pö  mit  Gen.  u.  Dat.  ,nach',  mit  Instr.  ,unter'),  als wesentlich  nur  mehr  perfektivierendes  Verbalpräfix  lit.  pa-,  aksl.  po-  (als Nominalpräfix  aksl.  pa-,  lit.  pa  und  pö-,  vgl.  z.  B.  aksl.  pamhnUi  ,sich erinnern',  pa772^^6  ,Andenken');  apr.  pa-  wesentlich  in  nominaler,  pö-  in verbaler  Kompos.,  vgl.  Trautmann  203,  Meillet  Slave  comm.^  505.
55
Über  slav.  po-d^  ^unterhalb,  unter^  s.  Brugmann  Grdr.  IP  2,  733  f.  — S.  noch  idg.  ""po-ti  und  "po-s.
ap-u  steht  neben  ^ajw  (Lit.  s.  u.  *pu)  in  ark.  kjpr.  lesb.  thess.  äftv^'  in alid  abo  ='  ciba,  anord.  au-virdi  n.  ^verächtliche  Person^  (Falk-Torp  HL), yo-l,  auch  oben  *a'pu-ro-  neben  '^^apero-,  *apu-ko-,  und  *pu  neben  *po.  Das -u  vielleicht  enklit.  Partikel  ;,und,  au
```


## [2026-09-04T22:41:48.160Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^apo-\" -A25 AHD_watkins1985.txt | head -60"
}
```


### [2026-09-04T22:41:48.205Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T22:41:49.158Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"AWKWARD\\|awkward\" AHD_watkins1985.txt | head; echo \"===evening===\"; grep -n \"EVENING\\|evening\" AHD_watkins1985.txt | head"
}
```


### [2026-09-04T22:41:49.219Z] TOOL RESULT

```
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
1271:AUTOPSY OkW- AUXESIS aug-! AUXILIARY aug-! AUXIN aug-! AVAIL wal- AVAST  kel-3, past- AVATAR auc’, tera-? AVENGE deik- AVENUE gWa- AVER wéro- AVERT wer-3 AVIAN awi- AVIARY awi- AVIATION awi- AVICULTURE awi- AVIFAUNA awi- AVOCATION wekW- AVOID eu-2 AVULSE wel-4 AVUNCULAR awo- AWARE wer-4 AWAY wegh- AWE agh-1 AWKWARD apo- AWN ak-
===evening===
131:The other celestial bodies recognized were the sun, sawel-, and the stars, ster-3. There is evidence from several traditions for similar designations of the constellation Ursa Major, though these may not go back to the earliest Indo-European times. The movement of the sun dictated the names for the points of the compass. EAST is derived from a verbal root aus-', “to shine,” as is the word for “dawn” (Latin Aurora), divinized since Indo- European times on the evidence of Greek, Lithuanian, and Sanskrit. The setting sun furnished the word for “evening” and “west”:
1163:wes-pero-. Evening, night. I. Reduced form “wes-. 1. Suffixed form *wes-to- in Germanic *west- in: a. Old English west, west: WEST; b. Old English westerne, western: WESTERN; C. Old English westra, more west- erly: WESTERLY. 2. Possibly Germanic *wis- in Late Latin Visigothi, “West Goths” (Gothi, the Goths): Vist- GorTu. II. Basic form *wespero-. 1. Latin vesper, evening: VESPER, VESPERTILIONID. 2. Greek hesperos, evening: HESPERIAN. [Pok. wesperos 1173.]
```


## [2026-09-04T22:42:04.931Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"EVEN[A-Z]* [a-z0-9W'’-]*\" AHD_watkins1985.txt | head -20; echo \"=== e-pi/epi ===\"; grep -on \"epi. Near, at, against[^.]*\\.\" AHD_watkins1985.txt | head"
}
```


### [2026-09-04T22:42:04.989Z] TOOL RESULT

```
1448:EVEN oi-no-
1479:EVENT gWa-
1479:EVENTIDE da-
2129:EVENIENT gWa-
2129:EVENT gWa-
2181:EVENANT gWa-
2181:EVENGE deik-
2181:EVENUE gWa-
2249:EVEN septm
=== e-pi/epi ===
```


## [2026-09-04T22:42:06.545Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^evening,\\|^even, adj\\|^even, adv\\|^eve, \" KLN_1966.txt | head; echo \"===\"; grep -n \"^of, prep\\|^off, adv\\|^after, prep\\|^awkward, adj\" KLN_1966.txt | head"
}
```


### [2026-09-04T22:42:06.603Z] TOOL RESULT

```
===
```


## [2026-09-04T22:42:13.241Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"evening\" KLN_1966.txt | head -20; echo \"=== size\"; wc -l KLN_1966.txt KLN_1971.txt"
}
```


### [2026-09-04T22:42:13.300Z] TOOL RESULT

```
2032:^■hath  Olam,  the  second  of  the  two  benedic¬ tions  preceding  the  Shema  in  the  evening  prayer
4539:Derivatives:  bat.  intr.  v.,  to  use  a  bat,  batt-ing,n. bat,  n.,  a  nocturnal  mammal.  — -  A  dialectal  form of  ME.  bakke,  a  word  of  Scand.  origin.  Cp. Swed.  natt-backa,  natt-batta,  ‘bat’  (lit.  ‘night bat’),  Dan.  aften-bakke,  ‘bat’  (lit.  ‘evening  bat’). For  the  change  of  k  (in  ME.  bakke )  to  t  (in  E. bat)  cp.  apricot  (from  orig.  apricock),  havoc  (fr. OF.  havot),  and  the  English  words  milt  and  milk, ‘milt  of  fishes'.
9957:curette,  n.,  name  of  a  surgical  instrument.  —  F., fr.  curer,  ‘to  cleanse’.  See  cure,  v.,  and  -ette. Derivative :  curette,  tr.  v. curfew,  n.,  evening  signal.  —  ME.  courfew,  cor- few,  fr.  AF.  cotverfu,  covrefeu,  corresponding  to OF.  covrefeu,  lit.  ‘cover  the  fire’,  fr.  covre,  im- per.  of  OF.  covrir  (F.  couvrir),  ‘to  cover’,  and feu,  fr.  L.  focus,  ‘hearth,  fireside’,  in  Late  L..
13351:epi-,  before  a  vowel  ep-,  before  an  aspirate  eph-, pref.  meaning  ‘on,  beside,  among,  above,  an¬ terior’.  In  chemistry  this  pref.  denotes  relation of  some  kind  to  a  specified  compound.  —  Gk. ini-,  in-,  £9-,  fr.  ini,  ‘on,  upon;  up  to,  over, after;  at;  beyond,  besides’,  cogn.  with  OI.  dpi, ‘also,  besides’,  Avestic  aipi,  ‘also;  to,  toward’, Toch.  -pi.  Arm.  ev,  ‘also,  and’,  and  in  gradat¬ ional  relationship  to  Gk.  6m-  in  omlle(v).  Ion. and  Att.  5ma9i(*),  ‘after,  behind’,  L.  ob,  ‘to¬ ward,  against,  in  the  way  of;  about;  before;  on account  of;  instead  of’.  Cp.  ob-  and  words  there referred  to.  Cp.  also  the  first  element  in  bias, bishop.  For  Teut.  cognates  see  even,  ‘evening’, epiblast,  n.,  the  outer  layer  of  the  embryo  (biot.) —  Compounded  of  epi-  and  Gk.  (UXacrn iq,  ‘bud, sprout,  shoot’.  See  -blast.
13523:Erebus,  n.,  a  place  of  nether  darkness  leading from  Earth  to  Hades  ( Greek  mythol.)  —  L.,  fr. Gk.  vEpe|3os,  fr.  Heb.  ‘ erebh ,  ‘sunset,  evening’. See  maarib  and  cp.  Europe.
13836:Europe,  n.  —  L.  Europa,  fr.  Gk.  Eupdjxr),  ‘Europa  ; Europe’,  which  is  prob.  of  Semitic  origin.  Cp. Akkad,  erebu ,  ‘to  enter,  go  in;  to  go  down,  set’ (said  of  the  sun),  ereb  shamshi,  ‘sunset’,  Heb. 'erebh,  ‘sunset,  evening’;  see  Heinrich  Lewy, Die  semitischen  Fremdwdrter  im  Griechischen, Berlin,  1895,  pp.  139-140.  Accordingly  Eupw— r, orig.  meant  ‘the  Region  of  the  Setting  Sun'.  Cp Hesychius,  who  renders  Eoptirr r,  with  the  words -/copx  t f,p  8'jaetop  (=  ‘the  Land  of  the  Setting Sun’).  Cp.  also  Gk.  ’'Epspop,  ‘place  of  nether darkness’,  which  derives  fr.  Heb.  'erebh.  See maarib  and  cp.  Erebus.  The  form  Eup  cutty;  (as  if the  name  meant  evp-com;,  ‘broad  face’)  is  due  - to  the  natural  tendency  of  the  Greeks  to  Grecize words  foreign  to  their  language.  For  the  sense development  of  Gk.  EupcoTrc;  from  a  Semitic word  meaning  ‘sunset,  evening’,  cp.  Asia.
13878:evasive,  adj.  —  F.  evasif  (fem.  evasive),  fr.  L.  eva- sus,  pp.  of  evadere.  See  evade  and  -ive. Derivatives:  evasive-ly,  adv.,  evasive-ness,  n. eve,  n.,  l)  evening ;  2)  time  immediately  preceding an  event.  —  ME.  eve;  a  variant  of  even, ‘evening’.
13881:Evelyn,  masc.  PN.  —  Prob.  fr.  prec.  word, even,  n.,  evening  (poet.)  —  ME.  eve,  even,  fr.  OE. it  fen,  rel.  to  OS.  aVand,  ON.  aptann,  Dan.  of¬ ten,  OFris.  evend,  Du.  avond,  OHG.  aband, MHG.  abend,  G.  Abend,  and  cogn.  with  Gk. 6m-  in  6ra#s(v),  Ion.  and  Att.  om<j(ls(v), ‘after,  behind’,  6i|;s,  ‘late  in  the  day,  at  even’, hid,  ‘upon,  after’;  hence  evening)  lit.  means ‘the  hinder’  (=  latter)  part  of  the  day’.  See  epi- and  cp.  words  there  referred  to.  Cp.  also  the second  element  in  Halloween, even,  adj.  —  ME.  even,  fr.  OE.  efen,  efn,  ‘level, even’,  rel.  to  OS.  eVan,  OFris.  even,  Du.  even, effen,  OHG.  eban,  MHG.,  G.  eben,  ON.  jafn, Dan.  jxvn,  Goth,  ibns,  fr.  Teut.  base  *etfna-, which  possibly  corresponds  to  I.-E.  *im-no-,  en¬ largement  of  base  *im-,  whence  L.  im-itdri,  ‘to represent,  copy,  imitate’.  See  imitate  and  cp. anent.
13882:Derivatives:  even,  n.,  adv.  and  tr.  v.,  even-er,  n., even-ly,  adv.,  even-ness,  n. evening,  n.  —  ME.,  fr.  OE.  atfnung,  ‘evening’, prop,  verbal  n.  fr.  xfnian,  ‘to  become  evening’, fr.  tefen,  ‘evening’.  See  even,  ‘evening’,  and  -tag, suff.  forming  verbal  nouns,  and  cp.  morning (fr.  morn).
13883:evensong,  n.  —  ME.,  fr.  OE.  xfensang,  compound¬ ed  of  xfen,  ‘evening’,  and  sang,  ‘song’.  See even,  ‘evening’,  and  song, event,  n.  —  OF.  event,  fr.  L.  eventus,  ‘occurrence, event’,  fr.  event-(um),  pp.  stem  of  evenire,  ‘to come  forth,  happen,  occur’,  fr.  e-  and  venire, ‘to  come’.  See  come  and  cp.  venue,  ‘arrival’, eventful,  adj.  —  Compounded  of  event  and  -fill; first  used  by  Shakespeare.
13884:Derivatives:  eventful-ly ,  adv.,  event ful-ness,  n. eventide,  n.  —  ME.,  fr.  OE.  zfentid,  compounded of  xfen,  ‘evening’,  and  tid,  ‘time’.  See  even, ‘evening’,  and  tide.
15487:Fuchsia,  n.,  a  genus  of  plants  of  the  evening  prim¬ rose  family  (bot.)  —  ModL.,  named  after  the German  botanist  Leonhart  Fuchs  (1501-1566). For  the  ending  see  suff.  -ia. fuchsin,  fuchsine,  n.,  a  variety  of  rosaniline ( mineralogy ).  —  Formed  fr.  Fuchsia  with  suff.
16090:Geullah,  n.,  the  benediction  which  follows  the Shema  in  the  morning  and  evening  service ( Jewish  liturgy).  —  Heb.  g('ullih,  ‘redemption’, from  the  stem  of  gd'dl,  ‘he  has  redeemed’:  so called  because  it  ends  with  the  words  “who  has redeemed  Israel”.  Cp.  goel.
16391:Godetia,  n.,  a  genus  of  plants  of  the  evening  prim¬ rose  family  ( bot .)  —  ModL.,  named  after  the Swiss  botanist  Charles-H.  Godet  (1797-1879). For  the  ending  see  suff.  -ia.
17095:Halloween,  n.  —  Shortened  fr.  all  hallow  e'en. See  hallow,  n.,  and  even,  ‘evening’.
17670:Hesperian,  adj.,  Western.  —  Formed  with  suff. -an  fr.  L.  hesperius,  fr.  Gk.  kankpioq,  ‘western’, fr.  kampoq  (for  *f£<j7repoi;),  n.,  ‘evening’;  adj., of  the  evening,  western’,  which  is  cogn.  with L.  vesper,  ‘evening’.  See  vesper.
17675:Hesperis,  n.,  a  genus  of  plants  of  the  family  Bras- sicaceae  {bot.)  —  L.  hesperis,  ‘the  damewort’, fr.  Gk.  kamplq,  prop.  fem.  of  the  adjective ioTxipioq,  ‘of  the  evening;  western’,  fr.  Sampoq, ‘evening’.  See  Hesperian  and  cp.  Hesperides. Hesperornis,  n.,  a  genus  of  very  large  swimming birds  from  the  Cretaceous  of  Kansas  {pale- ontol.)  —  ModL.,  compounded  of  Gk.  konepoq, ‘of  the  evening;  western’,  and  Spvu;,  ‘bird’.  See Hesperian  and  ornitho-.
17676:Hesperus,  also  (poet.)  Hesper,  n.,  the  evening star,  esp.  Venus.  —  L.  Hesperus,  fr.  Gk.  e a- TOpoc,  short  for  kampoq  aerr rjp,  ‘evening  star’. See  Hesperian.
20829:Kol  Nidre,  declaration  made  in  Aramaic  at  the beginning  of  the  evening  service  on  the  eve  of Yom  Kippur.  —  Aramaic  kol nidhri,  ‘all  vows’; so  called  from  the  opening  words  of  the  de¬ claration.
21428:Leicester,  a  county  in  Leicestershire,  England. Leila,  Leilab,  fem.  PN.  —  Arab.  Ldylah,  prop, ‘dark  as  night’,  fr.  laylah,  ‘night’,  which  is  rel.  to Heb.  layil,  layldh,  Aram,  lela,  lelya,  Syr.  lelya, Ethiop.  I  Hit,  ‘night’,  Akkad,  lilatu,  ‘evening’. Cp.  Lilith.
=== size
   41262 KLN_1966.txt
  271509 KLN_1971.txt
  312771 total
```


## [2026-09-04T22:42:38.502Z] TOOL CALL #16: Bash

```json
{
 "command": "ls; ls tools/ | head -40; ls data/ ; ls data/verification | head"
}
```


### [2026-09-04T22:42:38.563Z] TOOL RESULT

```
CONTRIBUTING.md
data
docs
EtymologicalDictionary-persian-english.epub
EtymologicalDictionary-persian-english.pdf
README.fa.md
README.md
site
tools
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


## [2026-09-04T22:42:49.620Z] TOOL CALL #17: Bash

```json
{
 "command": "(pdftotext -f 60 -l 60 -layout EtymologicalDictionary-persian-english.pdf - 2>/dev/null | head -80) ; echo \"EXIT $?\""
}
```


### [2026-09-04T22:42:52.046Z] TOOL RESULT

```
EXIT 0
```


## [2026-09-04T22:42:55.114Z] TOOL CALL #18: Bash

```json
{
 "command": "which pdftoppm pdftotext; ls data/extracted | head"
}
```


### [2026-09-04T22:42:55.160Z] TOOL RESULT

```
/usr/bin/pdftoppm
/usr/bin/pdftotext
batch
NEXT_CHUNK
RETRY.txt
test
```


## [2026-09-04T22:43:00.380Z] TOOL CALL #19: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 60 -l 60 -r 150 -png EtymologicalDictionary-persian-english.pdf $S/p60 && ls -la $S/p60*"
}
```


### [2026-09-04T22:43:03.847Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 60499 Sep  4 18:43 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p60-060.png
```


## [2026-09-04T22:43:09.979Z] TOOL CALL #20: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p60-060.png"
}
```


### [2026-09-04T22:43:10.008Z] TOOL RESULT

```

```


## [2026-09-04T22:43:27.805Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==92' HRN.txt | head -60"
}
```


## [2026-09-04T22:43:28.917Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pas \" HRN.txt | head -20; echo \"=== numbered\"; grep -n \"^ *3[0-9][0-9]\\. \" HRN.txt | head -5"
}
```


### [2026-09-04T22:43:29.922Z] TOOL RESULT

```
70 ~
phlv. ^patv(i)hltan , vergl. u^v(i)hTtan^ vd. 19 (16),
nv(i)himtan ^).
aw. *paitis + 1 [/'va^d-^ caeday^mi] ai. prati +
i/^ved'.
Np. h aus altem d zwischen Vokalen z. B. auch in
/'ähem aus ^svädämL Die gleiche Behandlung von d
und d (bei letzterem häufige Fälle des Übergangs in h)
zeigt, dass das d zwischen Vokalen im Persischen
ebenfalls spirantisch gesprochen wurde, daher auch
keine Scheidung im Altpersischen durch besondere
Buchstaben ; vergl. auch die allgemein durchgeführte
Spirans d bei AM., also im älteren Neupersisch, über
die Behandlung im Reim siehe Rückert, ZDM6. 8,
285, 286, 10, 263.
315. pes 'hinter, nachher, pesin 'letzter.
Käs. peCj pdc]es, pes.
ap. pasa, 'hinter', pasäva 'nachher ; aw. pasda 'nach',
paskät nachher, hinter , pasne 'hinter' ; phlv. paSj pasTn
'letzter ; ai. pagdd *hinter, nachher , pagcdt Von hinten,
hernach*.
kurd. püstve, pfisl; af/. LW. pas; oss. d. fastäge, t.
fästäg 'hinterer, nachher, zuletzt, am Ende' (280) ; bei.
pas^ Comp, pastara (287).
316. pest 'niedrig, nnoilN (Is. 2, 9; 11, 17).
ai. vergl. üpastiä, upastis 'Untergebener .
Bartholomae (briefliche Mitteilung).
LW. wa/. past, siyn. pist,
317. pistän 'Brust (der Frau)'.
a.w./stana' *Brust'; phlv. p(i)stan (vd. 9 (71)), pistän
(vd. 15 (26) 61.); ai. stdna-; arm. stin (H. No. 259).
LW. af/. pistän.
Vergl. Bartholomae, Indog. Forsch. I, 187 Anm. 2.
318. puser, pur 'Sohn, pus (Sahn. III, 1516 Vers 336,
1517 Vers 358 2), 1523 Vers 473).
*) So lese ich statt nvedlnltan.
*) An den beiden ersten SteUen vielleicht für puser zu emendireD,
doch kann bei puser wie bei pider die Izäfe fehlen, vergl. Landauer
zu S. 1517 Note 4.
```


### [2026-09-04T22:43:29.982Z] TOOL RESULT

```
2717:aw. pädra- 'Schutz'; phlv. pas (Bund.), pOspäti, vd.
6130:spas 'Dienst'.
6503:*) Vergl. hyrkän. spas bei de Lagarde, Ges. Abh. 226, 227.
10839:fis 'Schaaf (295); bei. pas, n. pas 'Kleinvieh' (286);
=== numbered
2907:300. perrisiym^uS, perrisiyCLvesän ^) , 'Frauenhaar (Pflanze),
2912:301. pers 'Bach, Quell'.
2920:302. pergene 'Provinz, Distrikt'.
2923:303. peren 'gestern', perendös 'gestern Nacht'.
2934:304. pervär *Stair^).
```


## [2026-09-04T22:43:42.947Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 625 626 627 628 629 630; do echo \"--- leaf $n ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -6; done"
}
```


## [2026-09-04T22:43:43.855Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==30 || NR==31' IEC.txt | grep -n \"apo\\|ap-\\|aps\" | head -30"
}
```


### [2026-09-04T22:43:44.907Z] TOOL RESULT

```
--- leaf 625 ---
ات
برخست باشد ۰ و آن کیاهی است خود روی
و خوشبوی مانند اسفناج که داخل آش کنند
چون در کوه و کنبذ باواز بلند چیزی بگویند
در جوا ب‌همانرا نو ند » وآن‌را بمرمی‌صد اخو انند.
یر ول - بروزن‌قبول, کمب پا واسشخوان
--- leaf 626 ---
وتجسی وجستجوی را کوبندب وبمعنی مصدر نیز
آمده است که جستجوکی زن باشد.
۰ 4 9 فروشند کی
پژوهنده ۴ بر وژن فروشنده »
بمعنی بازیرس کننده و قحص نماننده باشد
وحکیم و عاقل و خردمند و زبرك را لیز
--- leaf 627 ---
لس ۱ « جنم اول و سکون ثالی مخفف
بسر است که درمقابل دختر باشد . #۶
فسا - بر وزن و معنی با باشد. و آن
شهریت درملك فاری وضا معرب آنست ۴ .
پساچین - با جیم فارسی بر وزن
مساکین » بقيةٌ میوه ای باشد که در باغها بعد از
--- leaf 628 ---
سا نیدن- بروزن «سانیدن, آب دادن
باغ وزراعت را کویند ۱ .
بی‌او کند . با واوه بروزن و همتی
ساو ند ۲ ‌ِ پروزن دما تد, قاف؛شمررا
گومند همحو دچار ونگار و بهار ۰
پساو هدن - بر وزن رسانیدن » بمعنی
--- leaf 629 ---
حمشوق است.
بی جانشین ۳ ۳
شخصی ات که چون صاحب دکان برخیزد او
یجای صاحب د کان بنشیند وکالا بقروشد
ی خم زدن - کنابه از کریختن
باشث .
--- leaf 630 ---
پربچه ی ۱ ۱ وت
مخنور " مخذف پسواندو است که پسر ژن باشد
از شوهر دبگر با پسر شوهر باشد اززن دمگو»
و بکس اول بروزن سکندر همآمده‌است.
بسنده؟ سٍ بروزن‌دهنده مخفف بند نده
باشد که بمعنی بر گزیده است .* .
```


### [2026-09-04T22:43:47.009Z] TOOL RESULT

```
22:ankulos (ankolos, anklos), à “bent, bend, hook’. WP I, 61. Cf. onkulos Skt. ankuráh “blade, shoot? beside aficalah ‘hem’; Tokh. A ancål ‘bow’ (the weapon); Arm. anky (‘handle’. The Skt. Tokh. and Ar- menian forms are ambig.); Gk. agkúlos, ag- kúlē, agkále; Olr. écal, ēccell ‘danger’; OHG angul (*fish-hook', ambig. cf. anghulos)
24:and, ið (1) “blow, breathe’. WP I, 56. Cf. anomos Skt. anàmi, animi; Av. an-; Arm. cf. c-anem (‘scatter’, fr. *eks-an-); v-anem (blow, scare off. fr. *apo-an-); cf. Gk. an- in án-ethon “a fragrant plant, dil; cf. Lat. an- in an-he- lus; an-centus “planting; trumpet-blast'; Olr, anaim ‘breathe’; W cf. an-adl (‘breath’, fr. *an-atla-); Go. cf. us-anan ‘breathe out; Sw.
54:ap-, radical of āpnu-, āpos, aptos, q.v.
55:ap-aĝð, see apo, ag0 Skt. apåjami; Arm. v-azem “dash, trespass, pass away, spill; Gk. apágo; Lat. ab-igo; Ir. f-ágaim ‘quit
56:ap-anó (apana, apono) cf. apo, ana (ono) Av. apano “distant; distance’; Gk. cf. epano (epi, ano); OHG (aphetic) fona, fana “from
59:aperos “beyond, later, further'. Cf. apoteros. WP I, 49 , Skt. áparah; Av. aparo; Ober apara; Arm. varo, var ‘down, below’; Olr. far, for ‘behind’; Go. afar, afara: OHG afara; avar; C: MHG aber, MLG aver); avaro (fposterit
```


## [2026-09-04T22:44:01.632Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==628' BQT_v1_pages.txt"
}
```


### [2026-09-04T22:44:03.972Z] TOOL RESULT

```
لس ۱ « جنم اول و سکون ثالی مخفف
بسر است که درمقابل دختر باشد . #۶
فسا - بر وزن و معنی با باشد. و آن
شهریت درملك فاری وضا معرب آنست ۴ .
پساچین - با جیم فارسی بر وزن
مساکین » بقيةٌ میوه ای باشد که در باغها بعد از
چیدن وه وا بسا ماندء باشد.
پساذدست.- بفتح اول ودال ابجد وثانی
بالف کشیده و سکون سین سعقص ونای قرشت »
بمعنی سیه باشدیمنی امروز چیزی بخر ند و(۱)
قیت‌آن را پی(۲) چندروز دبگر دهند(۳)۳ .
بی‌افتاده ه کی را گویتد که
در راه از رفقا ( ء ) باز مانده باشد - و بمعنی
پی انداز و ذخیره و اسوخته ليز آمده است.
)( خم ۳ رفتار ۰
باشد که اندوخته و ذخسره و یی انداز است
مطلفاً خواه فلز اموال و اساب هت خروونات
دیوی و خواء از اعمال صالحه و طالحه بجپت
لفع « نان اخروی- وبمعنی میراث هم آمده
است .
پس اقکندن- چیزی از بوم الشرج
خود نگاهداشتن وذخیره کردن باشد - و بمعنی
سرا اث گذاشتن هم‌آمده ور
پسالتن ۴ ه بنتم اول و انی بالف
کشیده و نون مکسور و فوفانی مفتوح بنون
دیگر زده, بلفت زند ویازند (۵) بمعنی‌افشاندن
باشد» وباین معنی باضافةٌ ها نیز بنظر آمده است
که پهاتن بائد , ویسانمی ویسهانمی بمعنی
افشانم ویسانید و پپانید بعنی بیفشالید .
(۳) خم ۳ بدهند .
سس ۲ گاه کردند ز آن کارزار
بت و سا
ستد و داد مکن هر کر جز دستادست
س شاه را فرخ اسفند یار ۰
ی ره و بو
که بسادست خلاف‌آرد وصحست برد.
ابوشکور بلخی. < لت نامه * .
```


## [2026-09-04T22:44:16.262Z] TOOL CALL #26: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:403 --image 2>&1 | tail -40"
}
```


### [2026-09-04T22:44:18.461Z] TOOL RESULT

```
no scan of BQT covers printed page 403 (see 'scans' in refs_online.json)
```


## [2026-09-04T22:44:23.459Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"پسین\" BQT_v1_pages.txt | head -20; echo \"=== count leaves before\"; grep -c \"\" /dev/null"
}
```


### [2026-09-04T22:44:25.612Z] TOOL RESULT

```
192:من پیش ازین ازشاجان بودند ومن‌نپسین آنانم.> بنابراین اگر دولوحه‌نامبرده
367:سوم » پسین بادشاه دوده‌ان سامانی است که ازفارس بودند , باین مدت باز
25842:شین فطرت پسین شمار توبی, خوبشتن را ببازی مدار . فرنوسی طوسی .
=== count leaves before
0
```


## [2026-09-04T22:44:29.090Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport io\nt=open('BQT_v1_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'پسین' in p or 'پسبن' in p:\n        print(i, repr(p[:80]))\nEOF"
}
```


### [2026-09-04T22:44:31.009Z] TOOL RESULT

```
10 'مقد مه دو\n( در ارمشتان) وسوئز ( درمصر ) . نوشتة بفستان ازداریوش بزرگ که\u200cمانند\nبی'
16 'ههد عه هت\nشده است . کلمه بپلوی بز بان دور اشکانیان و بزبان دور ساسانیان\u200cاطلاق\nمی'
631 'ییان سیزدهم\nدر بای فارسی باشین نقطه دار مشتمل برشصت لغت د کداهت\nکزر با زای نقطه '
```


## [2026-09-04T22:44:33.971Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nfor i in (629,630,631,632):\n    print('=== leaf',i,'===')\n    print(pages[i][:2000])\nEOF"
}
```


### [2026-09-04T22:44:36.793Z] TOOL RESULT

```
=== leaf 629 ===
حمشوق است.
بی جانشین ۳ ۳
شخصی ات که چون صاحب دکان برخیزد او
یجای صاحب د کان بنشیند وکالا بقروشد
ی خم زدن - کنابه از کریختن
باشث .
ی دست گردن ۰ کنابه از پنبان
کردن وذخیره‌نهادن باشد .#8
پستادست - با دال ابجد بروزن
هرجا هست + بمعنی نسیه پاشد و آن خربدن
اسباب واچناسی است که بعد از چند روز قیمت
مدهند ۱ # .
پستان مادد بر بدن « کنابه از
حرعی رشره وبی‌همنی- وحق‌ناشناسی وبی‌حشفتی
ویی هقی سنارتن بنشد. 9
سته‌شکر فشان- کنایه‌از لب ودهان
9 رد : مساوست .
پستای - بکس اول , اوستا 15100202 (یستان) .
پهلوی ۳)(5020 و ۳15428 , حتدی‌باستان - 81888, ارمنی
هناد .انبانی 5)20ا0 < اسعق ۰۰۳۱۷ کیلکی ۳540 ؛
غده‌های بزر که برسينةٌ جانوران که از آنها شیری فراود . دوغده
بزر که برسيتة آدمی که فزه وتا در کتر است و از آنها شیز
مقطح مت
یرون میا بد:
تهی‌دید پستان کاوش زشیر دل میزبان جوان کشت پیر .
فردوسی طوسی. «لفت نامه».
۵ پستاقك - بکسر اول وفتح پنجم ( از: منان ۵ پوند شباحت) »
ظرفی ازبلور با غیر آن شبیه بستان که مادران بی‌شیر» شیرحیوان با زنی دیگر
پتانك در آن‌کنند وبدهان طفل هند . * لفت نامه *.
۵ پسه ‏ بکر اول وشتح سوم» درتازی فستق ازآرامی فتفا (بکسراول), چه معا آن
شام ( سوربه ) است و بونانی نقل شد ۳۱50۵108 و از آن
بدیگر زبانهای ارویابی داخن شد . در ابتالیابی نمی 5)2ز۳ هه
«لفس» ؛ درختی است میوه دار که درآب و هوای معتدل واراضی --
سيك خوب میروید . مهمترین نوع آن همان یسته معمولی تک
( ۷۵۲2 ۱582012 ) است . مراکز مهم یس ابران کرمان,
آذرباجان» داعفان وفزوناست.رگ: فرهنگه روستابی۲۷۵ بعد بسله
وثابتی ۱۷۰ و کل کلاب ۰۲۱۷ ۱
۵ پسر - بکس اول وفتح دوم (درلهجةٌ مر کری) » در پارسی باستان واوستا ۳09072 ؛
پهلوی ۳فکنا۳ و کنام [ رك و ره سیون , کردی 15 . استی +5
واع1] , بلوچی 0۱1528 , وخی 0۵4۲ : شغنی 0۷6 . سربکلی ۳4: عنجی ۳۲ » ممرب
آن قور در قنفور؛ امه ها ور مه راک ممصص :ریات
#9" , نطنزی ۳0۲ <2 . ۱ص ۸۵ ۰ ۰ سمثانی ۳1۳ ۶ مشگکری و نرخةٌ
ولاسگردی0ا۳» شهمیرزاوی ۳6526۲ 4 ,۲ صس ۱۸۷ در فارسی نیز پس ویور؛ فرژند فرینه
این . ولد .
=== leaf 630 ===
پربچه ی ۱ ۱ وت
مخنور " مخذف پسواندو است که پسر ژن باشد
از شوهر دبگر با پسر شوهر باشد اززن دمگو»
و بکس اول بروزن سکندر همآمده‌است.
بسنده؟ سٍ بروزن‌دهنده مخفف بند نده
باشد که بمعنی بر گزیده است .* .
پستگاگ* - بتتح اول و شالی و کاف
فارسی و سکون ثالث وکاف » بیعنی تگراك وژاله
باشد .
پر یچ ۱ ح بارای‌ترشت وتحتالی
مجهول و جیم فارسی بروزن سرخیجه . بسران
بدکاره - ومردم سفله را گویند .
پس سر نمودن ‏ کنابه از دو
کرداتیدن بخجالت باشد.. و کی را که مخل
طبمت باشد بلطایف الحیل ازسروا کردن.
پی شام - بائین قطه دار بر وزن
بدتلم» بمعنی سحورباشد» وآن .طعامی‌است که در
ایام رمتان تردمك بصح‌خور نف.
سغده با عن نقطه دار ودأل بی نفطه: بسو ده بروزن نبوده» ممعنی‌دست‌زده
ودست زسثه و دست‌هالمده باشدب وسوراخ کرده را
یز گویند؟ .*
پسها نت۷ - باهای هوز و نون وتای
فرشت بروزن صفراشکن ۰ بلغت‌زند و باز ند )۱(
بمشی افثاندن پاشد و پسهانمی بممنی افثانم .
و پسهانید بعنی بیفشانید .8
برودت طقحه: ماده وعهیا ساخته باشد۴ ۴
پ ی گوش افکندن ۰ کنابه از
قراموش کردن بانشد .
پسند؟ - بر ون سمند ؛ قبول کرده
ویترقه باشد - و قبو ل کننده رانیز گوند.
پسنالر - ینم اول و فتح دال بر وزن
٩‏ سپس + یچه ( ابچك پهلوی علامت تسفیر و تحقیر ) . ۴ رك : فده
و مدیدن . ۴ - پارسی باستان -80) +۰ 11۳2 ۵ : اوستا 584 ( شستن) , قس :»
حندی‌باستان 28004 (سندلی) «امشق ۳۱۹). نبرک کلمُ‌پهلوی4ظ2598را از284عاه0ه
لز ۵0۵12-59002 (بنظر آمدن) داسته . فی : خرمند «یی رکه 4۳-۱۷۲ .
۴ از: بسن (ه م) + ه (شبت) :
آنچیست زکردار پسد که توالت آن‌چیست زنیکوبی وخوبی که‌نداری؟
فرخی سیستانی . «لفت نامه».
۵ - ظاهر! مسحف کلم مك « لفت‌نامه » با بشکك است. ۹
۴ 4 : پاتن . . .
6 پستدشی - بفتح أول ودوم وششم 1 از: بنند (ه .م) (-بدن (پسوند مصدر) [ بپلوی
093780 «ارنوالا 0۷۶» : «کفتم ( احمدبن ابی‌دواد) : اف ان با امپرالمومنین ! که ان
خولی است وایزد عزذکرء نسندد.» «تارئخ بیهقی ۰۱۷۳ . ۱
۵ پسووی - جتح اول وچهارم. رك: سودن. ۵ پسوند - بفتح اول وسوم» ره :
ملواف ‏ ۶ پسیی - بفتح اول. مر کب از: پس - بن (پسوند شبت) ویهلوی 82418
(فز یی آینده)؛ آخرین, اخیر؛ خلاف ختی :
ت اضف 9 ۱ بقبه درصفحعه 1۰۷
=== leaf 631 ===
ییان سیزدهم
در بای فارسی باشین نقطه دار مشتمل برشصت لغت د کداهت
کزر با زای نقطه دار ۰ وا اعلمه .
دشت عم یشم أول بر وزن مشت» معروف
است‌و رین یر ع رات ۱ ویناه و یشتیبانب
و بیرون هرچیز را نیز کوبند - ونلم پلدماست
در نواحی تیشابور مشتمل بردوست وست‌دخش
قربه وچون این‌بنده بمنزلة پشتی باشد نیشاپوررا
بدین تلم خواننه ۷ - و تلم ۳ج
از ولات‌بادغیی در خراسان۸ - وحیزومختت‌را
پیز گوند .
شتاده - بی وزن رخساره ». مخقف
پشتواره است وآن مفداری باشد از هر چیز که
به پشت نوان برداشت* .
پش « بفتح ارل و سکون ثالی » موی
کردن وک کل اسب راگونند! - وطره‌ای که بر
سردستار و کم رگذارند و فش معرب آئست -
و نات وفرومایه از هرچیز باشد - وشبیفونظیر
و ماشدرا نیز کفته‌ادد ۴ - و بضم اول جفد را.
کونند ۴ وآن پرندم‌ایست نامبارگ و بکراول
مخف پیش باشد؟ .
بشام - بر وزن سلام ؛ هر چیز نیره
رتکه راگوشد ۱
یشان » بنتم اول » بررزن و عمنی‌چشان
ی
نوشته بودند بانال تقطه‌دار. ودر دوفرهنگهدیگی
- کفلهاتی گرد و یش و دم دراز بر وبال فریی و لاغر یفن
پوربپای جامی. «لنت نلمه» .
؟ ‏ رك : فتي ور : ص له از ده مولف. ۴ - ر: پشكه .
ط وق شقن  »‏ ظاعراً ميچيك از درسنی که صاحب برعان بهیتان داده
صحیم لیست چمخود اودر کلمهُ اعزار جشان» بعنی کرمةالبیناه میگوید معنی آن هزار کزاست
چدچشان بمعنی «کزه , باشد واگر اين دعوی صاحب پرها که میگوبد پثان « شان» است‌سحیح
اشدنلةکذرن لظکزر يچيك ستبکه هرد مسحفه کزه است وااملزت نم
, اوستا ۳2۳۵/04 ( پشت ) , پپلوی ۳۷15۳۸ . هندی باستانی ات۳۲5 , (قطاطویم‎ . ٩
۰ ۳۷۲۱ کردی ۳1994 . زازا 2251 ء افتانی ۳0۵1۵6 » بلوچی کی ۷ « استق‎
کربرمن ۹۷ ۰ . کیلکی )نکنام . ۷ - مرب آن به بشت بضم اول » شهری منواحی‎ +
یخاپود وان کوومایت که قمیةٌ آن طیبئیث ( نرهیز) است وگو یشک مدین تلم‌خوانده شده زرا‎
آن بمتر له به بشت است نبشابور را و شامل ۲۲۹ قربه است ت از جمله کندر که ابرضر کندری وزیر‎
ر4 : مشتو‎ ٩ . مدان متسوب است. «معجم البلدان» . ۸ مراد بست است. رك: بت‎
4۰5٩ ها زصنحهٌ‎
شین فطرت پسین شمار توبی, خوبشتن را ببازی مدار . فرنوسی طوسی .
- مایین ظهر وغروب وصر .« از ملخص اللفات حسن خطیب کرمالی ». نم سین +
نمازعصر.«لهت نامه», درف یز ندی و نطنزی حصلحاکزن, مر لین 0 (ظهی) دك. :اص ۰۲۸4 در
لهج اطراف اسفهان ۳۵/۸1۳ (صر) . درخواداری 00عام «سالنامة
=== leaf 632 ===
پشت پاخارمدن
شدن و خوش آمدن و خوشحال کردبدن
جاشد ۱ ۰
فست با ردن کنابه از ترك دادن
واعراض نمودن - ومنهزم شدن باشد.
پشت پای - حیز ومختث را خواننده
و گاهی حنوان دشنام هم این
کومف .
فشت دست - کلیمی با شالی باش دکه
برزمگران 3 باغبانان چبر ی درآن نهند و بریشت
بتدند .
پشت چمی ۰ کتابه از سحن چمن
پشت دادن «کنایه از روی کردایدن
ورو ردان شدن و گریختن باشد .
پشت دار - پروزن‌بردیار » پشتیبانرا
گوبند - و هر چیز که باو (۱) شخامتی باشد
خصوصا از جنس پوشیدنی .
پشت دست گز یدن ویشت دست
بد فدا ی گر دی ۰ کنابه از ندامت و پشیمانی
وتأسف باشد
بدلدای کندی. بمعنی یشت دست گزدن باشد
که کتابه از ندامت ویشمالی است
پشتاث - بنم بروزن جفتك , جامةٌ
(۱) خم ۳: بااو .
کمرگاه باشد و پشتر
و ۰ و مه
مردم دارالمرز پوشند ۱ - و عرضی است. که
عارش اسب و استر و خر میشود چنانکه دانها
بردست وپای آنها برمیآمد ویخته‌میشودوسیب
آن از رفتار باز میمانند 7 ولوعی از بازی حم
هت وآن چنان باشدکه شضصی کف دتم ای
خود را برزانوها کذاشنه خم شود ۲ دیگری از
پشت او بجهد . و بسنی کوبند پشتك‌آنست که
کف دسنپا را بر زمین گذارند و پاهارا بر هوا
کرده براه روند .
پشت لک بالام بروزن جفت‌رنگه,
پمعئی هرزه - و اقص و معیوب - و بی معنی
باشد - و بمعنی پس افتاده هم بنظر آمده است.
پشت هار ۵ - با میم بالف کشیده‌وفتم
زای نقطه دار » سلك استخوانهای میان پشت
کوبند و بعربی صلب خوانند - و کوشتی را
نیز کویند که در طرف درونی استخوان پشت
عمباشد .
بشت ماهی بکر الت بر وزن
پر سیاهی » کنابه از شب است که بعربی لیل
خوانند؟ .
بشت 0 پشت مازه است
که ساك لنتعوان مان به یشت باشد .
بشت نمودن - کنابمه از روی بر
کرداندن - ورگ دادن - ور و گردان شدن -
و گرنشتن باشد .
بشتو س نم ول و تال و سکون تب
و واو مجهول , زبان اففانیرا کوبتد۴ - و بقتح
۰ سوادی که در وی سیاهی نبود
حاهی نود . نظام ی کنجوی.
. «ابران باستان
```


## [2026-09-04T22:45:01.786Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8').read()\npages=t.split('\\f')\nfor i in (29,30,31):\n    print('=== leaf',i,'===')\n    print(pages[i][:2500])\nEOF"
}
```


### [2026-09-04T22:45:04.041Z] TOOL RESULT

```
=== leaf 29 ===
 ‘fragrance’, see onguh-)
anguho ‘narrow, squeeze’. WP I, 62. Cf. angho, angho Per. anjam, -idan (/bend'. Ambig. cf. onk-); Arm. denom. andzkam ‘ʻI yearn’; Go. ga- aggwjan; ON ongva; MHG engen; OCS o£o, oziti
anios “yon, that; other;. WP I, 67, 86 and II, 337. Cf. anos (1) Skt. anyáh; Av. anyð; OPer. aniya-; Oss. ánnä, innà; Arm. ajn; Hitt. annis, eni, enin
ankolos, see ankulos
ankoros, see ankuros
ankotos, anktos, à “bend; bent’. Cf. onkos, onkos. Skt. aficitab; cf. Per. anjidan (ambig. *bend"); W. angad (‘handshake’, ambig.); Olr. écht, Ir. éacht ‘foul deed’; OHG åhta *'outlawry'; OE obt *manhunt' beside ahtian ‘to ambush’. (The Ir. and Gmc. forms are ambig.); OCS okotí (‘hook’, ambig. cf. onk-)
anko, ið “bend, cramp'. (The evidence is ambig. cf. onk-). See next
ankos, à, on “bend; cramp; strait; constraint; end, death". WP I, 60. Cf. ankoato-, and onk- (for forms in the sense of “bend, bent) Skt. ánkas, n. ankáh (“bend, hook”. See onk-);
anguhis, anghus — ang, ið
10
15
20
25
30
35
40
45
26
Av. afiku; Tokh. B enku ‘complaint’; Arm. ank ‘propriety’, cf. dr-ank (*door-presser', Le *beggar), ankiwn ‘corner’, h-ank (‘to the end’, fr. Sen ank-); Gank (Cendlessly', fr. *eks-ank-); Hitt. henkan ‘death’; Gk. ágkos, agké, agkón, cf. an-ágké; Alb. ang ‘bogey’; Lat. ancus; Umb. ançif *bends'; Olr. éc, Ir. éag ‘death’; cf. OIr. écen, Ir. éigean, m. f. ‘force, neces- sity’; eagán ‘throat, gorge, abyss’; Gaul. anco- ‘bent’; OBr. ankou ‘death’; Br. ank ‘corner’; anken ‘sorrow’; cf. enk (‘narrow’. See enk-, eng-); Cor. ancow ‘death’; anken, pl. -yow “grief, pain’; W angen ‘need’; pl. -od ‘death’; Go. cf. halsagga ‘neck’; OE anga ‘sting, goad’; MHG ange (‘hinge; bosom’. Ambig.); ON ambig. eng, engi ‘meadow’; Pol. -ek (in osek *boathook', from a type *ak-ank-?). Note: all the Gmc. and the Alb. and Hitt. forms are ambiguous.
ankros, à, see ankuros, à
ankst- ‘recess’ (?). Cf. anguhestos, and cf. onk- Arm. cf. anck, pl. ‘passage’; OR ohsta ‘armpit’; Latv. oksts, oksta *buttocks'
ankulos (ankolos, anklos), à “bent, bend, hook’. WP I, 61. Cf. onkulos Skt. ankuráh “blade, shoot? beside aficalah ‘hem’; Tokh. A ancål ‘bow’ (the weapon); Arm. anky (‘handle’. The Skt. Tokh. and Ar- menian forms are ambig.); Gk. agkúlos, ag- kúlē, agkále; Olr. écal, ēccell ‘danger’; OHG angul (*fish-hook', ambig. cf. anghulos)
ankuros (anküros, ankoros, ankros), à “hook, angle; creek’. Oss. ángurá, ángur (hook, ambig. cf. ankulos, onk-); Tokh. A ankar- ‘tooth, tusk’; Gk. agkura; Alb. angérr ‘hinge’:
=== leaf 30 ===
is; Arm. (aphetic) na ‘that, he, she, it; him, her’; Alb. cf. an-dej «that way’; OCS on, ona, ono “he, she, it; that’; Li. anas, añs, f. ana
anos (2), à ‘ancestor’. WP I, 55 OHG ano, cf. also enel “grandfather; grand- child"; Sw. anor, pl Ukr. on-uka ‘grandchild’; Li. cf. an-yta husband's mother
anos (3) “breath, soul, fragrance’. WP I, 56. Cf. anó (1), anomos, anotlom Skt. anáh; Tokh. B. cf. anas-, cpds.; W an ‘element’, beside en-ig ‘soulful’; Cf. also Gk. an- in án-ethon ‘dill
ans-, àns-, see ams-, ams-
anta ‘doorway, entrance’. WP I, 59 Sk. atà ‘frame’; Arm. cf. -and in dr-and *thres- hold”, dr-andik (^jambs', fr. *dhur-antes); Lat. antae, pl; ON ond ‘porch’, anddyri, id. (*-dhurio); Pol. cf. jet-ka *rooftimber, beam’; Latv. ots, ote ‘entrance to clamp’
anteros “second, other. Cf. anos (1) and -teros. WP I, 67; II, 337 Skt. ántarab; Per. andar (in the phr: madar i andar 'stepmother); Oss. àndár, cf. also än- dära (*otherwise', fr. *antero); Arm. cf. andra- “back, again’, andren ‘again’; Alb. cf. denom. ndrroj ‘I change: Go. anpar; OHG andar; ON annarr; OE ober; OCS vütoryj; Cz. cf. vteřina “second of time’; úterý (scil. den) “Tuesday”; Li. antras; Latv. otrs; OPr. antars, anters
anti (onti, anti, "onti). (The aspirated variant is implied in Hittite hanti); antis, os, ios ‘towards, against, facing; face, front, side, edge, end WP I, oi Skt. ánti; ántah; Av. afito; Tokh. A ant, B ante; Arm. cf. h-andiman (facing, opposite’, fr. *en-anti-mn-, cf. Gk. énanti: Lat. inante);
10
15
20
25
30
35
40
45
Hitt. hanti; hanca (for *hants “front); Gk. antí; antíon, antía, ánta; Alb. ané 'side', ende "and: Lat. ante, antea, antes, antiae; Osc. ant ‘til; MIr. étan, Ir. éadan “front, fore- head”; Br. ant ‘ridge’; Go. and, anda-, andeis: OHG andi, endi ‘forehead, end”, ante, endi , ‘and’, OS ande, endi, id.; MHG ende “side, end, forehead', etc. and comm. Gmc.; and- px. in and-ouge 'presently); ON enn, and-, en, enda, endr, enni, endi, endir; OE and, and-; OCS cf. vot-ükü ‘woof; OLi. ant, anta ‘on’, Li. ant, id.; afitis, gs. ančio ‘bosom’; Latv. ots ‘boarded side, gutter’. See onti
antimn-, see anti above
antis (2), see anotis
antlos (?), ntolos (?) ‘frail, tender, young". Gk. atalós; OCS otlü; Pol. wątły; Cz. útlý; R utlyj
antoi ‘yonder’. Cf. anos (1) and tð, toi Alb. andej, Li. antai, añt ‘behold’
antro- “interior; hollow'. Cf. entero- Gk. antron (‘cave’. LW in Lat. antrum, id.); OCS cf. otrí “inside”, otro-ba ‘intestines’, and com. Sl.
ants- (?) “forepiece, crosspiece'.
=== leaf 31 ===
y. The v- forms of OHG fr. LG); cf. SG afern ‘to repeat’; OE eafora (*descendant': Go. afara, id.); ON. afar ‘very’, efri "later
apetios (apətios, apotios) “back, rear; last. Cf. apo, opi
'Skt. apatyam ‘progeny’; Av. apás, apaða; Per. |
pas (aphetic? or to poti, q.v.); Hitt. apecis, apicis (ambig. cf. opi); Gk. cf. áps; OE OS cf. eft (back, again’, etc.); Li. apacià "base, foot.
apolos “strong; strength’. Cf. opalos, op- Gk. cf. eü-epelia; an-epelia, n-ēpeléð olig- epelie; Illyr. (ambig.) Aplus, a, o (proper names) beside Dalmatian Oplus, a (cf. opolos); Lat. cf. copula (&bond', for *co-ap-); OE (ambig.) afol ‘power’; ON afl
apomos “last, furthest'. Cf. apo. WP I, 49 Skt. apamáh, apama; Av. apomo; Hitt. cf. appan “after, warde": OAIb. i pér-apém “last? (*pro-apomo-)
apotes, aptos (strong; strength’. Cf. apnu-, apolos, op-. WP I, 46 Alb. i aftë (Cable, if not a Lat. LW); Lat. aptus “tied, joined, fitted, close, proper; OE eafop 'strength' . apis (?) ‘insect’. Cf. empis Lat. cf. apis, gp. apium ‘bee’; OCz. op-oka, -uka, ap-oka ‘honeycomb’ beside Cz. jepice ‘mayfiy’.
apios ‘distant’. WP I, 49. Cf. apo- aper-, apomos Arm. cf. ap, apn ‘shore’; Hitt. apa “back, again’; Gk. ápios; ON efja ‘recess, backwash’
apnu-mi (apneumi, àp-) ‘get, reach". WP I, 46. Cf. apó, àpos Skt. apnómi; Av. ap-; Hitt. cf. ep-ci (“takes, begins’, 3pl. apanci); Gk. cf. (?) epáomai ‘mend’, cf. n-epios “silly, inept’; Lat. cf. apiscor, co-epi beside OLat. apo, apio ('attach'. Fest.) and ind-ipiscor, -eptus; OE zfnan (3. “hold, sustain, endure"); Cz. cf. japny, adj. “quick, smart; OCS za-japiti se ‘think, su-
20
25
30
35
40
45
aperos — aps
30
spect’; Li. cf. opus ('sensitive', see apos below)
apo (apo, apo, po) “away; from, after", WP L 47. See next Skt. ápa; Av. apa; Oss. fá-, px.; Tokh. -àp, suffix; Arm. v-, px.; Hitt. appa 'afterwards; again, back"); -apa (suff. ‘so, then" queried); Myc. apu; Gk. apó; Alb. pa ‘without’; f-, px.; Lat. ab (perhaps also as a fused px. in Lat. p-arco, p-av6o, paro, pudeo, pando, etc.); Ir. fo-, px.; OBr. W o; Bret. (WSP) a; Cor. a; Go. af; OHG aba “away; from’, abo "but: OE of; ON af; OCS po ('after. In sense of "about see upo); Srb. pa (fr. *po “and, then, so’: Hitt. -apa); Li. po (WSP in sense of 'after); cf. apa-6ià ((bottom?. See apetios above); Latv. cf. apa-k3 “below? apo-, px. *not-, un-'. See apo above Skt. cf. ápa-bhis ‘fearless’; Gk. apó-thrix ‘hair- less"; Alb. pa, pa- ‘without; un-'; Go. af-guds ‘godless’
apos, ios (1) ‘miid, gentle, thoughtful Sk
```


## [2026-09-04T22:45:14.627Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pyš\\|'pyš\\|py-s\" SOD_pages.txt | head -20; echo \"=== afterwards\"; grep -n \"afterwards\" SOD_pages.txt | head -30"
}
```


### [2026-09-04T22:45:14.684Z] TOOL RESULT

```
=== afterwards
7428:                                                                    afterwards, then
7520:      then, afterwards                                                      pswe- B
7620:        (rc)rcject,(/o)throw                                               then, afterwards
7835:     then, afterwards                                                      and, that, then
16654: 4527 yyntwh B                               ^i~(<^>/-i0              later, afterwards
25083:     parez ©<*pari-razaya-           ©impf. p>ryz                 then, afterwards, on the other hand
25341:        BSTii: C2.51V13, 120R4                                    then, afterwards
25435:     then, afterwards                                              7553 pt^pr'yn- B
27840:                                                                   later, afterwards
28340:        then, afterwards, again                                         8557 rwcn B                                     Jjjj"./*H
37591: afterwards    1280, 1297, 1353,           altar   5289,8138                        anything     30, 40, 45
```


## [2026-09-04T22:45:20.062Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *55 [ʾ'A-Za-z]\\|[^0-9]55 ['ʾ][a-zA-Z]\" SOD_pages.txt | head -10; echo \"===300===\"; grep -n \"[^0-9]300 ['ʾ][a-zA-Z]\\|^ *300 \" SOD_pages.txt | head -10"
}
```


### [2026-09-04T22:45:21.125Z] TOOL RESULT

```
===300===
4659:300 »try swc»y 8ynh S     (^U ^ Oiy*)oijsJ J^                               awkarsne ('wqrsny(yXh)) ^'wqrsn'wt
```


## [2026-09-04T22:45:26.382Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i in (120,121,122):\n    print('=== leaf',i,'===')\n    print(pages[i][:1500])\nEOF"
}
```


### [2026-09-04T22:45:31.690Z] TOOL RESULT

```
645
=== leaf 120 ===
       (o)pu sfarme                                                    1404 'pys^r =» ps»pr
       sexless                                                                                                                  ^Uaji ij>}^
                                                                       1405 >pysm B.
       SCE 356
                                                        V^LSi
                                                                            pism ? ©<*pasca-ima           =»pysm
                                                                            according to
 1392 >pw ymwn B
      (o)pu y(i)man                                                         BSTBL; STii, GMS 373, 7.15, 22; Benv. Notesii
      faultless                                                               215
       BSTBL, Vim. 3
                                                                      1406 'pystr'yck1 B                                    JJtw.»x/
 1393 >pw zn'kh B                               jbU t^h JjJj               opistarick (pystycyk)
                                                                           future
      (o)pu znak
      ignorant                                                              SCE 489, 494; BSTBL, Dhu. 250; GMS 373, 1013
      SCE 43; BSTBL, Vim. 185
                                                                      1407 >pystrw        B
1394 'pxyyr- =* pcyyr-                                                      opistar(u)    
=== leaf 121 ===
 }pzymy$

                                                                      radiance                                        56
          CI 1991, 178-185
                                                       JJ>->v
                                                                      GMS 439; KG 365
 1416 'pzymyS S
      (3)poze-me0 ? =^zyy my5                                   1428 >r8\p-       B                              u-u^^
      the day before yesterday ?                                      ar5yf, ar5ef   0r8yf-)     ©<*drafaya
      S W, Rock. Insc. Indus Valley 1989, 134                         (ro)shine
1417 V C                                                              SCE 496; GMS 439
     ar ©conj.                                                  1429 ar&efa
                                                                     Wyp" OrSypO
                                                                            B                                  j^'J^Kp
      and, then                                         u-i'J

      C2 gloss. p65, 183-4                                            splendour, radiance
                                                                      SCE
                                                                        etc. 76; TSP 14.33; STii 7.29; BSTBL, Dhy. 48 &
1418 Vy'n B                                            h^^ii
     arhan ©< Skt. arhat
      Buddha's title                                            1430 VS'y p
=== leaf 122 ===
 51
                                                                                                                  V^stMc
                                                                     from Argi
 1440 »r5wk      M                                  o-lj
      ar5uk      ©<*ardu-ka; OP; Av. ardda-t ardumanls               Sogdica. 8.13, 10.1 13c; Hen. BSOS 9, 564; GMS
         -^rdq, >r5kw, yw>rdq                                          1016.L >rkc*nch; Frag. Len. 44.7
       sincere                                                 1452 »rkh B, S =» >rk
       GMS      154,423                                        1453 'rkr'k S                                        fjf
1441 Mwky'     M                                 coj^^Ij             ark-are     (Wry)   ©<V£-Htr>£   ©pi. -f
                                                                     worker
     arSukya   ^'yw'rSwky*
     sincerity
                                                                     MDii  pl59.13;
                                                                       ark-kare   ? Y/rVy, Sund. MSP p41, "work",
       GMS 423

1442 >rSyf-       M =» Wyp-                                    1454 Vkrwn'y      B                     >'<J><J^^X
                                                                     ark(k)arune    Orkrwny)
1443 'rSyp' «> 'rS'yp*
                                                                     (related fcOwork, effective, effect
1444 *rdyw- C                     o^d
```


## [2026-09-04T22:45:41.577Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nfor i in (119,120):\n    print('=== leaf',i,'===')\n    print(pages[i])\nEOF"
}
```


### [2026-09-04T22:45:43.387Z] TOOL RESULT

```
=== leaf 119 ===
 >pW   »y>m

                                                          1379 'pw pekwyr           B                             54
        (o)pu astanya                                                                                  ^\^ <(_r> ^>^
        impermanence                                            (o)pu packwer       =*pckwyr'(kh)
        BSTBL, Vim. 119                                         fearless
                                                                Vim. 109, BSTBL
 1366 >pw Vm        B                              jLU^
        (o)pu ayam =**y'm                                 1380 *pw pekwyr'k => pw pekwyr'k
        endless
                                                          1381 >pw pckwyr'k(h)        M, B                         jTl^
        SCE 271, 513; BSTBL, Vim. 160, 179; Dhu. 103
                                                               (o)pu packwerak
                                                               fearlessness
1367 >pw »zr => »zr                                                                                                              jj^
                                                               Hen. Tales. 476.6; BSTBL, Vim. 57, 167
 1368 'pw "zrmy'h => 'zrmy'h
                                                          1382 'pw p5kh         B                               ^>
1369 >pw'5'k B,S                       o&^^ix^
     (o)pwa5e (pw'dy, 'pw'5'y) ©<*hapa (=Skt.                  illegal pa5ka
                                                               (o)pu
          sap- "to worship")+wa£ ©ace. -w ^pw'S'k              SCE 295
        temple, sanctuary *
        SCE n p37, 176, 276, 335, 348; STSC 137; Frag.    1383 'pw pryt'tt B                           ^^'J^Oj^
          Lcn. 96.1, lOOal, 3, 5, c9; Mack. BSTBL p!54
                                                               (o)pu
                                                               lovelessfritat
1370 'pw'6'y =* 'pw'5'k
                                                               SCE 306
1371 'pw 'ps'yS B                                  u**^
     (o)pu (o)/apse5                                      1384 'pw pstnh        B
     faultless                                                                                                        w.
                                                               without  delay ^pstn-, pw1
                                                               (o)pu pastan
       SCE 37f
                                                               VJ 561, 724
1372 »pw Vy        M, S, B                 (M^>^^         1385 >pw ptpy6y B                           oifTu, j*&
                                                                                                              jt€ \ oj-^
       (o)pu ary    ^pw'ry
       priceless                                               (o)pu patPcSe
                                                               unconsciously
       GMS 1164; Tales 469.33; MSP bl09; BSTBL,
         Vim. 38                                               BSTBL, Intox. 13

1373 'pw'rstk      B                        .ju^^u^f^     1386 'pw ptmJ,k B
                                                               (o)pu patmak                                                \J
       spwarste ©pp. ^pw'st-1                                  immeasurably
       turned away
       BSTBL, Vim. 169; GMS    14                              BSTBL, Intox. 31

1374 >pw>rt-                                              1387 'pw ptinVr B
                   B                       O^jj^j^
                                                               (o)pu patsmar                                       jUi,
       spwart =»pw}rt-
       (to)tum away                                            innumerable
                                                                                                                           \ji

       BSTBL; TSP; SCE; GMS 585; inf. ->y, TSP 2.893           BSTBL, Vim. 120 etc.; Dhy. 174 etc.; SCE 3 etc.

1375 'pw'st- =» pw'st-2                                   1388 'pw ptzm'n       B       ({_L-^l oj-^^-^jr*   lj,..^}*i£jr~

1376 »pw5pn    B                           J^^^^               (o)pu patzman
                                                               insatiable
     (o)pu 60an ^5pn-'h, pw dbn                                SCE 460
     without doubt         *                                                             >r>p(h)
     BSTBL, Padm. 67                                      1389 'pw r'p S

1377 'pw kyr'n B                                               (o)pu raf ©ace. -w
                                                  ^/^          without illness
     (a)pu-kiran =*kyr'n, pw kyr'n                                                                            \S j^   Oj-k
     unlimited                                                 Anc. Lett. 2.3, -w, 3.2, 5.2
       BSTBL, Dhu. 58                                     1390 'pw rywsny'kh        B               (<j^jjJj±)J&
                                                               (o)pu r(a)xusnyak ^rywsny'kOO
1378 'pw pcYw'k   B                             £^dj±          ignoranccQightless)
     (o)pu paexwak -^pcyw'k
     without obstacle                                          BSTBL, Intox. 5

       BSTBL, Vim. 116; -kwy Padm. 9, 11                  1391 'pw spWk             B                Lr^     ollJ^ jjJb

=== leaf 120 ===
       (o)pu sfarme                                                    1404 'pys^r =» ps»pr
       sexless                                                                                                                  ^Uaji ij>}^
                                                                       1405 >pysm B.
       SCE 356
                                                        V^LSi
                                                                            pism ? ©<*pasca-ima           =»pysm
                                                                            according to
 1392 >pw ymwn B
      (o)pu y(i)man                                                         BSTBL; STii, GMS 373, 7.15, 22; Benv. Notesii
      faultless                                                               215
       BSTBL, Vim. 3
                                                                      1406 'pystr'yck1 B                                    JJtw.»x/
 1393 >pw zn'kh B                               jbU t^h JjJj               opistarick (pystycyk)
                                                                           future
      (o)pu znak
      ignorant                                                              SCE 489, 494; BSTBL, Dhu. 250; GMS 373, 1013
      SCE 43; BSTBL, Vim. 185
                                                                      1407 >pystrw        B
1394 'pxyyr- =* pcyyr-                                                      opistar(u)        ©comp. adj. =*pystrw
                                                                            later
1395 >py- C                   :   o*/^ j^bzj'^y                                                                                   J* J>*   i JjU

     apay ©lsg. opt. *pyym ^"p'y-                                           VJ; SCE; BSTBL, Vim. 135, 167; GMS 373;
     (ftf)considcr
                                                                             >pystrwhtVi 1030
     C2, 54 V27: BSTii 895.57                                         1408 'pysy B                                         JjO (u-if    <0-lj

1396 >py>rh B                                  j^^^s                        (o)pisc ?
     opyar ©*upa-yar          -^PyVk                                        after, behind
     the night before                                                       BSTBL, Dhy. 99
      VJ 3 n p89; BBB 697; GMS 969                                    1409 'pysys'r       B
1397 >py>st- B                               C»S&Lj~*cr>lJ                  opisc-sar -Vpsys'r
                                                                            backwards
     opyast ©pt. st. =*py»t-, py'st-
     (to)adorn, (fo)ornatc                                                  VJ 788, 791, 900; GMS 373
     EGSii 15; AVS 110                                                1410 »pzVn      B
                                                                                                                       O^jXl i ji 0" <^>lju
1398 >py>stk B                                                             (o)pzarn =>ptzrn, pzrn
                                          j_y<^J
     opyaste Opy'sty) ©pp. =»py}t-, pysty(y), py>stk                       trouble, sorrow
     ornate                                                                 VJ 82, 126 etc.; GMS 957
      SCE 311, 523
                                                                      1411 'pz'rn-        B, S                   jj^ JL. O-^^ljl;
1399 'py'sty => }py>stk                                                    (o)pzarn       Opzrn-)    ©Av. zar-
1400 »pyc,t B                                        -w^jUj                (to)disturb
                                                                           VJ 1458
     (o)p(D)cat =>pcyt(y)
     time
                                                                      1412 »pz»t(h) M                                     ji*j»^'j
      BSTBL, Vim. 121; GMS 179; Benv. Et. Oss. 28                          opzat ©<*upa-zata           ©ob. -yy; ob. pi. ~yt
                                                           ^J'
                                                                  ^
1401 'pyk      M
                                                    kSJ>.S l^                =»pz}t
                                                                           homeland, birth place(/?/ace of origin)
      apik =>»pyk
      aquatic                                                              GMS 99; *pzVykw, Hen. BSOAS 11; Giants. 70.4
      BBB 512; GMS      394
                                                                      1413 >pzn\vty7h S                                   ^>iT<^Li
1402 'pysp'y       B                                                       (o)pzanautya
     opospay =»*pspy-, pspy-                               la~%            acquaintance
     rcjection                                                             GMS 1079; KG 403
     BSTBL, Vim. 204; Benv. Notesi 33
                                                                      1414 >pzrn- =¥ 'pz'rn-
1403 >pys   B                                          ju,^           1415 >PZY B,S                     (Oj^^^jj)(y>)^^<j
                               (DAv. pasca    =*ps(,), pys-1,              utsti, tuti ? Cpny)       ©*uta-uti<*utti      ©Idg.        =»>ty,
       psy ops, opis Ops-)
     opos,
                                                                             >t\ rty, >rty\ -n, twty1, ZY, ty2
     then, afterwards                                                      and, that, then
     GMS 179
                                                                           GMS 307A; S W, C2 p66; BSOAS              1985, 112-3;
```


## [2026-09-04T22:45:52.399Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nimport re\nfor i in range(360,372):\n    p=pages[i]\n    if re.search(r'\\bp[sš]\\b|then, afterwards', p):\n        print('=== leaf',i,'===')\n        print(p[:2500])\nEOF"
}
```


### [2026-09-04T22:45:54.381Z] TOOL RESULT

```
=== leaf 364 ===
                                                                                                                        298




  prywnt


 7409 prywnt C, B          (j^ ^j jjjjl^ ^ U o*l -o
      pariwand ^pr'yw'nt, prywynd                                  STi  19.14, 11.4, 73.19, 74.1, 75.12; Sund. AoFiii
                                                                   parable
      to, on it,on/to them                                           p69, 16R 4, V2;C2 gloss.
      GMS 107, 1404, 1460, TSP 7.33; STi; STii; BSTii:
                                                              7426 przy'm     B, S                               ^Lj ^>uf
           C2 gloss.
                                                                   absolutely,
                                                                   parzyam     entirely
 7410 prywr      S ^ pry'wr
                                                                   SCE 461; TSP 2.341, 9.9a, BSTBL, ne przVm
 7411 prywrt      M =* pr'ywrt-
                                                                     "not at all"; Frag. Len. 38.10, 92.7
 7412 prywyS B, M, S           (j^ ^^ j-OjJ^jJ ^^J*
      pariwe5, pariwiO        (prywyd, prywy55)              7427 przpV       B                               c^p-fc^
        ^pr'yw'ySh, prywyO, pr,w>y8, pr                            straight
                                                                   parzpar
      to/for/in(/7), according to
                                                                   VJ 167
      GMS 1453, 1627; S W, C2 pi 16.10
 7413 prywyd      C =¥ prywy5                                7428 przpV2 ? B =» prnp>r
                                                             7429 przr                            (uy> >^* >>)^j <J~-
 7414 prywyd-          C =* prwyd-
7415 prywy86       M =» prywy5
                                                                   extremely, very much, excessive
7416 prywynd      M                            \&)j**j>Jj>         parzarf 5; BSTBL, Padm. 55; VJ 39 etc.; TSP; STii
                                                                   BBB
     pariwond     =*prywnt                                           4.37; KG 329; SCE 379; Frag. Len.; MDii; C2
     in, lo(them)
                                                                  gloss-, MSP e2
      GMS 107, 1404, 1460
                                                             7430 ps-1                                             o^j
=== leaf 365 ===
 299
                                                                        ^'pstkVk
       Hen. JRAS 1945, 149.5, 151.18
                                                                      helper
7437 ps,t5,r- M                                 jx-.>T                                                                   s-
                                                                      Hen. Tales. 486.20; GMS 552n 1, 663, 1125 pswx
     pasat-Sar (pst'r-) ©perf. st. «>ps-\ psd'r-
     (ftf)ask                                                   7449 pstq'ryy *> pstk'r'k
     GMS 536                                                    7450 pstn— B, S, C             j^j t^t* t*S^j* t\J&y i^-^
7438 psNv-       M, S, B            (j^jQ^jc^^ji/^                    pastan (pst>n) ©<*apa- stana ©f. nom.; ace.
       pasaw ^ps^v-                                                     -h, ->; pi. -/ =^>pw pstnh, >pstnh
       (to)touch                                                      delay, time, respite, postponement
       GMS 571; TSP 15.8; SCE 87; BBB 490, 663; Frag.                 GMS 89; VJ 561, 724; STii 2.14; Frag. Len. 27.3,
         Len. 81, 6, 12                                                 8; C2, 17R4, 51R27, 54R14

7439 ps'wyty S                         ajiUXL <^^jl& i^Jii*     7451 pstw-     C                          jj^aj < jjjfj&l
     pasuyde ©pp.                                                     pastaw   ©<*apa-stav-     ©impf. pPstw-, pt. st.
     sacred, purified
     MSP b84                                                            pstwH -^ps^w-
                                                                      (to)disown, (ro)deny

7440 ps'wt- M                                                         STi 10.14, 13.9; AoFi 225, 3; AoFiii 76. p>st*n
                                                   o*/^
     pasut ©pt. st.                                                     Sund. AI 28, 1988, 183; perf. pstwd}r-y STi
       (untouch                                                         58.3; GMS 89, 575

       BBB p72.576; perf. st. ps}wt5}r-> pp. ps*wty,            7452 pstxwmp- =* fstxwmp-
         Fr<\g. Len. 81.7                                       7453 psw B, C                                       JUL./
7441 psd*r- C                                  o*~*j,                 cattle, sheep
                                                                      pasu -»Jps-, ps-2
     pss5ar- (pst'r-) ©perf. st. -^ps'tS'r-
    
=== leaf 366 ===
                                                                                                                    300



 psxnt

7461 psxnt        C                        xj*l*j <*j*~a    7475 ps*pr   B, M                        o^iu<i<y m^T
         pasxand                                                  pasaPar (ps>br) ©Av. pi$wa\ <*pati- a- bara\
         making fun                                                 <*pasca-dbara- ?; Arm. psar =»pssPr
         STi 45.12                                                provisions, supplies
                                                                  TSP 12.20; BBB 523; GMS 298; Bailey. BSOAS
7462 psyd- C                               j^Jg ioj^S
                                                                    11, 795; Hen. BSOAS 28, 246n 32; Szemerenyi.
     pase5 Ops'yS-)
                                                                    HMV p418; Weber. IF 80, 1975, If, KG 366,
     (fo)fail, OcOdecrease
     BSTii 827.51: C2, 94V21
7463 psyng C                                 <u^<(^fjb-     7476 ps'br  C =» ps>pr
                                                                   pypfir
     pasing ?                                 -z'^s*1       7477 ps'bwty M                                    '■>j; J' -*«
     leprous                                                     pasa-bute (ps>pwty) ©pi. -ty
     BSTi 220                                                    after Buddha
                                                                 Hen. JRAS 1945, 154.10; GMS 1143
7464 psyp     C
                                                           7478 ps'd'r- C                           o^->j «j=^UIjja
      pasep ? ^Ps'yp-                        tjr^i "—■
      slander                                                   pasa(t)5ar- (ps'tS'r-) ©perf. ^ps'y-, ps*t-
      BSTii: C2, 52V14                                          GcOthrow away, GcOreject
                                                                STi 79.5; STii 5.45; Hen. Tales. 471.12
7465 psypw^ky* M                   l>l^jc^;
                                                           7479 ps'yrywCy) M       •juiU<(^U<(j>- j/-lu)jJl;U
     pasep-wapakya Opsypw) ^'ps^pw
                                                                pasa-yriw ©Parth.^asa^nw; MP psygryw\
     slandering
                                                                   Aiam.psgrb* =*Yrvw
      Hen. JRAS 1944, 138.26, I40n 2: Gersh. Sogd.          
=== leaf 367 ===
 301

       occiput                                                      pursuit, persecution
       GMS 1143                                                     BSTii 843.44; Mack. BSOAS 33, 119; C2, 68V 13
7488 ps't- C, M                         ^Wjjp 'o^^'           7499 pskfs- M                                 (^jOjdKi
     posat ©pt. st^ inf. ^ps'y-, psWr-                             paskafs ©pass. st.
     OeOthrow, (to)casi                                             (to)bc split
     STii 5.38, 40; C2, 22V6, 25V5; perf. st. /tfdV-,               GMS 177; BBB f 37; AVS 74
       STi 79.5; STii 5.45
                                                              7500 psknt B, M                               ?«>"<^Uj
7489 psWr-      M =» psWr-                                         paskand =*psknt
7490 ps'ty C, S                          ^^   uj&i <^U;I           havoc
       posate ©pp. pi. -t ^'ps'ty                                   Frag. 6.8 apud. S W, IIJ 1976, 50n 37
       thrown, cast down
       STii 5.42; C2, 60V10, 77V18, 94R8; Frag. Len. 40,      7501 pskr- S                      O^Ve^" <o*h lo*J^jj*
                                                                   paskar ^pskr-, pskyr-, psq»r
          13
                                                                   (to)drive out, (fo)persecute
7491 ps'x'rycyk M                         li* jl jl~ <, L_^        MSP b9ft BSTii 82927; Benv. Eti 300; C2, 102R
     pasaxarecik
                                                                     27; AVS 76
       belonging to the aftermeal
       BBB p98 c43; GMS 1017                                  7502 psqrty C                         <t^i- >j <v*^" v^5*
                                                                   paskarte ©pp.; pi. -/ ^psqJr
7492 psVryy M               (^'j^crt'^J'^)^
     pasaxare (ps'h^y, psWry)                                      persecuted
                                                                   BSTii: C2, 48R22
     aftermeal
                                                              7503 psqwr(y) C                                         ^j
       GMS 1143; Gersh. Sogd. Cpds. 1945, 142.1; BBB
         c43                                                       paskwsr (psqyr(y)) -^pckwyKkh), pcwqyr
                                                                   fear
7493 ps'y- B, M, C                  d^^'j^^Kjjj)                   BSTi 226; GMS 132A
     pa/asay ©impf. pypy =*psy-, ps't-, '
=== leaf 368 ===
                                                                                                                       302



 psp'cyg

           GMS 121                                           7521 pst>t- C                                       Ju^uT
7510 psp'cyq C                                       jt/u         pastat ©pt. st. ^pst'y-, prst't-
     paspacik                                                     (to)prepare                                          <oUI
     suddenly                                                     GMS 562; inf. psfyt, C2t 31V8

      BSTii 896.58: C2, 54V28 pl08                           7522 pst'ty C

7511 pspVy =$ prsp'r                                              pastate ©pp.; pi. -t =>prst»ty
                                                                  prepared, ready
7512 pspVyy M                                ci^- ^j^             STi 86.8; BSTii 889.29: C2, 60R29
      paspare ©<*pati-spar-
      advancing                                             7523 pstNvn      C                                  jjX\ljjZ^}

      GMS 962; BBB pi 32                                          pastawan ©pi. -t ^'pstWnh
                                                                  order, admonition
7513 psp'ty    C                                     Ol/u         BSTii 862.11: C2, 25V11 p62; Schwartz. STSC
      paspate =*pcp}t(yy)                                           45V; Sund. AoFviii 1981, 23V10
      suddenly
                                                            7524 pst>y- C                                        j^uT
      BSTii: C2 gloss.; Benv. JA 1951, 50 n 2; C2 p50n
                                                                  pastay ©pt. inf. pstyyt ^prst'y-, pst't-
        4
                                                                  (fo)prepare
                                                                  STi 31.8; BSTii 893.8: C2, 31V8
7514 pspr- B, M, C      j^ J>U>1 I td^J'j^A id^J'^y
     paspar ©impf. p*spr =»psprty
                                                            7525 pstf'r- M ^ ps>d>r-
     OcOfix, GcOlevel, (/o)trample                          7526 pstrw B
      GMS 370, 616; Frag. Len. 37.4; perf. psprd'r^               pastar(u) =»pystrw
        BSTii: C2.51V13, 120R4                                    then, afterwards
                                                                  TSP 7.66, 192, 12.46 etc.
7515 pspr'mndyCy) M                       j^jjl 
=== leaf 369 ===
303                                                                                                                   pfocdo
      latter, later                                                7544 psyy Sfr       M                                c~t>v j*
      BSTBL, Dhu. 281; BSTii 905.27: C2, 57V27                           pase-5par
                                                                         back door
7533 psycyq        C =4 psycyk
                                                                         GMS 373
7534 psyd- C                                   j*fjj<cr~x
      pasy5 ^psycPr-, prsyS-                                       7545 pt»m M                                           U"M*

      (to)sit down, (fcOsettle down                                     patam ©<*apa- tama-           ^prt'mch
                                                                        in a swoon, unconscious
      STi 39.9; Sund. AoFiii 1975 p79.9, 19R9                                                                       c/^
                                                                         Sogdica. 47.1 n p48; GMS A1003            jj^ (<^y)
7535 psydV- C                                    j^jj
     pase58ar, pasiSar- ? ©perf. of p(r)syd-                       7546 pt»pch B
                                                                        patafc ?, patapc ?                                 k*j!
     (to)sit down
                                                                        (a kind of)di\xg
     STi 52.10; Sund. AoFi 1974, 8V 12 p242; Hen.
                                                                        TSP 19.18n p232
       BSOAS 11, 1946, 715 apud. GMS 877 n 2

7536 psyn-     M         o>lsff b* ijzZhjl <o>jjTji^o <j^LuUb*     7547 ptVn'k B
                                                                        pattawne ©pres. part. =^pt>w-
      pasen ©<Skt. ksan ©impf. p*sy(y)n =*psn-
      (fo)trap, (ro)be trapped                                           SCE  68; GMS 893
                                                                         patient
      GMS 6l6n 1; Benv. Eti 329 n 60; AHM 192,
                                                                   7548 ptwwyn>k       B                            JJr* 'Ji^ji
        san-,S W, C2p51 n5
                                                                         pattawene ©pres. part. ^pt1wn,k
7537 psync- C                   (p j-^'.^j^j *6^l
     pas^c ©Shaek;
```


## [2026-09-04T22:46:03.230Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nprint(pages[366])\nEOF"
}
```


### [2026-09-04T22:46:05.339Z] TOOL RESULT

```
                                                                                                                    300



 psxnt

7461 psxnt        C                        xj*l*j <*j*~a    7475 ps*pr   B, M                        o^iu<i<y m^T
         pasxand                                                  pasaPar (ps>br) ©Av. pi$wa\ <*pati- a- bara\
         making fun                                                 <*pasca-dbara- ?; Arm. psar =»pssPr
         STi 45.12                                                provisions, supplies
                                                                  TSP 12.20; BBB 523; GMS 298; Bailey. BSOAS
7462 psyd- C                               j^Jg ioj^S
                                                                    11, 795; Hen. BSOAS 28, 246n 32; Szemerenyi.
     pase5 Ops'yS-)
                                                                    HMV p418; Weber. IF 80, 1975, If, KG 366,
     (fo)fail, OcOdecrease
     BSTii 827.51: C2, 94V21
7463 psyng C                                 <u^<(^fjb-     7476 ps'br  C =» ps>pr
                                                                   pypfir
     pasing ?                                 -z'^s*1       7477 ps'bwty M                                    '■>j; J' -*«
     leprous                                                     pasa-bute (ps>pwty) ©pi. -ty
     BSTi 220                                                    after Buddha
                                                                 Hen. JRAS 1945, 154.10; GMS 1143
7464 psyp     C
                                                           7478 ps'd'r- C                           o^->j «j=^UIjja
      pasep ? ^Ps'yp-                        tjr^i "—■
      slander                                                   pasa(t)5ar- (ps'tS'r-) ©perf. ^ps'y-, ps*t-
      BSTii: C2, 52V14                                          GcOthrow away, GcOreject
                                                                STi 79.5; STii 5.45; Hen. Tales. 471.12
7465 psypw^ky* M                   l>l^jc^;
                                                           7479 ps'yrywCy) M       •juiU<(^U<(j>- j/-lu)jJl;U
     pasep-wapakya Opsypw) ^'ps^pw
                                                                pasa-yriw ©Parth.^asa^nw; MP psygryw\
     slandering
                                                                   Aiam.psgrb* =*Yrvw
      Hen. JRAS 1944, 138.26, I40n 2: Gersh. Sogd.               dcputyia fter-self)
        Cpds. 1945, 145                                          BBB c43; GMS 1143; Gersh. TPS 1945, 143a, n p,
7466 psyr'mndyCy) M             J'^^^^^^                           PYrywy, Benv. Titres et Noms Propres. 58
     pasl/er-amande ©<*apa-s(a)r(a)ya-y MP                 7480 psWry       M «* ps>x>ryy
        ^ps^ysn-, Pahl. afsdr                              7481 ps'q M                       l?J^'j^ '(j^)^"-*
      cooling
                                                                pasak (pzwk, ps>k, pjwq) ©pi. -t
      Sogdica. 21.12b, n p22; CMS 1100                          abortion
                                                                GMS 980, 1648; Hen. BSOAS 11, 68; Sund. 1994,
7467 psyy M =* ps-2
                                                                  45
7468 psyyS M                       >^£ tj^Jf «cJjjJb*i
                                                           7482 ps'm ? M                              ? jju*l <v>jl,uJ
      pasc5
      restriction                                                pasam ? ©<*apa-sama- ?
                                                                 0c)swallow, (to)gulp ?
      Hen. BSOAS 12, 307.53
                                                                 Sogdica. 21.20, 21.22, 23 n p23, 24; >p?mnyt,
7469 ps *± pst1                                                    prest. part. pi. Sogdica 21.20; BBB p86
                                                                                                                 <IJ <f b
7470 ps- =* pc-
                                                           7483 ps'myh =» psmty*
7471 ps'^r    B                              &y <«£\
     pasaPar (pys*Pr, 'pys'Pr) =»ps>Pr                     7484 ps>nkC)) B
                                                                p(a)sank Opstokty) «»psn-, 'ps'nk
     provisions, supplies                                       net, snare
     VJ 347, 895n p93                                           TSP 2.847, 908

7472 ps^h'ry =* ps'x^yy                                    7485 ps'nk 'ns^y      B                        JjffhuXL*
7473 ps»y- B => ps»y-                                           pasank-ansace
                                                                trapper
7474 ps-Cj) M,C                         jl^^,^                  SCE 361
     pasa Ops-) ©<Av. pasca     ©adv.. & pref.
                                                           7486 ps*pwty =» ps>bwty
       =>psy, >pys
     then, after                                           7487 ps'sry   M                             s-ofs**^
     GMS 179,373, 1143;BBBp98
                                                                pasa-sare
```


## [2026-09-04T22:46:13.553Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"paskät\\|paskat\\|pasca\\|pascä\\|pasča\" BRT.txt | head -20"
}
```


### [2026-09-04T22:46:13.593Z] TOOL RESULT

```
190:Die  angeführten  Texte  bringen  ausserordentlich  zahlreiche  Wiederholungen. Und  zwar  sind  entweder  zwei  oder  mehr  Stellen  einander  völlig  gleich  oder  sie unterscheiden  sich  nur  in  untergeordneten  —  d.  h.  für  das  Wörterbuch  wenigstens untei^e ordneten  —  Stücken.  Als  Beispiel  für  die  erste  Art  von  Wiederholungen mögen  dienen:  Y.  65.  2-5  —  Yt.  3.  2-5;  Yt.  5.  10  =  12,  14,  16,  20  (usw.);  Yt. 5. 19  =  23,  27,  35,  39  (usw.);  Yt.  JO.  98  =  135;  Yt.  j^.  15  (von  hü  bis  taxmahe')  ^ Yt.  10.  70,  127;  Y.  57.  25  (von  akeca  an)  —  Yt.  10.  93  usw.  —  Die  Wiederholungen der  zweiten  Art  zerfallen  in  verschiedene  Gruppen:  Yt io.  103  wiederholt  sich  von yS  hantaia  an  wörtlich  in  Y.57.  isfl,  nur  dass  hier  das  ca  hinter  har>ta  fehlt; irgend  ein  Grund  für  die  Abweichung  ist  nicht  vorhanden.  Yt. /o.  94  (^=  114I und  Y.57. 26  stimmen  völlig  lusammen,  nur  dass  auf  die  Eingangsworte  aäa  nS tum  dort  der  Vokativ  mikira  vouru.gaoyaoite,  hier  aber  traosa  afya  huraöha  folgt; die  Gebetsformel  ist  die  selbe,  aber  die  Adresse  ist  verschieden.  Ähnlich  steht es  mit  den  vier  in  Yljo.  igof.  enthaltenen  Stücken,  die  von  vier  Waffenarten Mihras  durchaus  das  Gleiche  aussagen;  nur  eben  die  Namen  der  Waffe,  sowie deren  Beiwörter  machen  die  Verschiedenheit  der  Stücke  aus.  Besonders  zahlreich findet  sich  diese  Art  der  Wiederholung  im  Viälvdäi  {Vendidad);  z.B.  unterscheiden sich  in  dem  Kapitel  über  die  Verträge  (V.  4)  die  Abschnitte  6  bis  10  und  ander- seits II  bis  16  nur  durch  den  Namen  des  Vertrags  und  der  Zahl  in  der  Buss- bestimmung. Femer  haben  V.p,  53,  54,  55  und  S7  '^'on  üäca  an  den  gleichen Wortlaut,  nur  dass  das  dreimalige  para  von  53  in  54  durch  kaha,  in  55  durch nöü,  in  57  durch  pascalta  ersetzt  ist  In  den  liturgischen  Teilen  des  Yasna  wieder sind  grosse  Stücke  bis  auf  die  Eingangs-  oder  Schlussformel  gleichlautend.  So decken  sich  Y,  i.  3  ff.  und  5.  5  ff.,  4. 8  ff.,  7.  5  ff.  vollständig  bis  auf  die  Eingangs- worte, die  zu  Y.  1:  nivaiöayemi  hankärayemi,  zu  Y.^:  äyese yeSH,  zu  Y.  4:  Hat  dis äva^ayamahl,  zu  Y.  7:  alaya  daöami  lauten,  während  anderseits  Y.  2.  äff.  und 6.\S.  nur  darin  auseinandergehen,  dass  hier  (Y.  6)  jeder  Abschnitt  mit  yatamatde endet,  dort  (Y.  4)  jeder  mit  ahmya  zaohre  bar>smanaica  eingeleitet  und  mit  äyese yeiti  geschlossen  wird.
2463:paiti  vä  xsa/ne  . .  nöit  . .  aiähe  ayqn  nöit aiiihä  xiapö  .  .  Yti.iS;  —  asankatca iöi'irSatca  ..  kaoa  nö  ahmäii*  asarahaica läiiraiüi  ..V.ff.Sif.;  55'\  56i\Y.^S.2; — sraoi»m  .  .  yö  dalnöJiisö  *da?nayä  . .  aya dalnaya  . .  Y,  57. 24;  —  , .  parö  jbi^anbyö .  .  alsqm  tbifyaniqm  Yt-  io.T%i.;  —  yaoz- däiqm  saeirqm  . .  änhqm  zaoiranqm  Yt. io. lai f.;  Y.2(j. 2;  —  vä^^m  srJr^m  .. ahmya  väse  Yt/o.  12411;  5.11;  —  äp)m andvim  . .  *atihasca  mi  *aSva^hä  apö ¥.(75.1—5;  5,  V.ö,32  (aitiha);  —  nmS- mm  .  ,  äat  ahe  nmänahe  V.^.3;  14,  40; —  narö  . .  äat  aisam  naram  aivS  iri^yai (vat  antarp  *n3rius  .  .  V.j.z?;  5.43,  44, A.4.6,  Yt.iO,i37;  —  ygi  nmüni  hqm. barämahi  . .  äat  pascaeta  ahe  nmänahe , .
2514:-  g.  'a-  Pron,  ident.  'ich,  du,  er  selbst',  humata  'ta'  ..  aat  mam  narö  paskat  ya- nur  NS. :  yi  maibya  yaos  (sd.)  akmai  astu  g3„ie . .  "um  dieses  (deines)  guten  Denkens vakUta  mahyä  isfois  voha  eöihm  mananM  willen  .  ."  H.2.14''.        2)  substantivisch: ".  .  dem  verspreche   auch  ich  selber  das  ,  ^tai  ti  .  .  avayam  *danmaM  Y.  öS.  i  '>;  — beste  meines  Besitzes  durch  VM."  y.4''-   am  yasna  .  .  ''ta  patti    ava.jasa  .  .  aoi \Z;    —    ai   -3    vaocal  ahurö  mazda    ''da  zam  ".  .    um    dessentwülen  (was  hier  ge- sprach er  selbst,  ^/iM."  Y.sp.ö.  [schiebt)    komm  . ."  Yt. 5.132  (s.  i);   — zBed._s.  Gdn.  GIrPh.   '  52      Ich   '^'^^<=^'^^'- -faimat puir.lt  (sUtt  AS.)  Kimar^xsaf^u/ia dass  f.  as'  aus  einerrart.  idg.  'n  'selber  er-    ,    ,  ,   ,.,       .,•.,..'        ,     .  ,        „ wachsen  ist,  die  in  aUi;  (aus  'a-u-r,  wie , (sd-)    damit  (was  ich  dir  gebe)  such  ..' eJroiaus*jn-H-/°)steckl.Dochs.B(;M,GrGr.3244-    V.  1^.  14;  —  in  Kongruenz  mit  dem  Prae-
3478:a/ayeinti  ya  *ace  paskät  vyänli  (sd.)  nsit *aoe  paskii  äfinU  "welche  all  die  ein- holen, denen  sie  .  .,  nicht  werden  sie (selber)  von  hinten  her  eingeholt"  Y.57. 39;  —  kam  «J  arsa  gavai^Tm  apayst pasiä/(sd.)  vaz^mnH  Yt. /0.86; — h5  alvS .  .  iiva.vasma  {sd.)  apayeiti  YL  14.10;  — aval  "apayaie  nama  ahmi  yat  uva  dama apayemi  ..  Yt.  J5.43.  a)  ohne  Obj. 'nachkommen'  (i^umüch):  ma  apaima paourvavaysii  {sd.)   Vr.  22.2'*.  2)  'ge-
3480:mit  avi  'einholen':  yest  ahi  paurva.- nafmät  aal  "lam  avi  nmänaya  (sd.)  yezt paskät  aai  ma'm  avi  apaya^sS.)  Yt.i&.a.
3583:—  ma%rym  spmttm  . .  pmrumca  . .  'r^mca V.  4.45;  45;  —  ahun?m  vairJm  . .  Tim sraoidyehya  (^^  frasrüiti  Y.  5. 14;  — apanmta  tiais^mi&A.)  G.3.T, —  'raheca yamahe  haplanhatdis  Vr.2/.o;  0,4^;  — ranuhlsla  a'A  .  .  hupaurva  (sd.)  vahehiS Ti/"  räsaintü  ¥.52.3;  —  aiwiea  'rim patiia  'rym  apsca  paurvalibya  "und  (man soll)  einen  zweiten  (Rüden)  und  dann noch  einen  weiteren  (zulassen)  und  zwar (soll  man  ihn)  gesondert  von  den  beiden ersten  (halten)"  V.  i^.  48.  3)  '>  der  Zeit nach 'der  spätere,  kUnftige'rja^a  mä  'racil (NPm.)  saoiyanis  stavqn  V.9.  2;  — yastä datrSMg  °rö  .  .  tarS.mqstä  "wer  darum künftighin  (eig.  posterior)^  den  D.  ..  auf- sagen wird"  V.  4:5. 11;  —  huzantSus  paiti •raya  YL  13. 134.  a)  mit  ayan-  n.  'der spätere  Teil  des  Tags,  Nachmittag':  */ra- \aire  ayqn  bavaiiii^A.)  hubar,rS  ..  a',a  "re ayqrt  duWirjm  ". .  dann  am  Nachmittag (kommt)  das  Unglück"  Aog.jJ.  A)  ASn. 'r?m,  'ram  und  IS.  °ra  als  Adv.  'postea, später,  künftig' :  yezi  nairyS  aukat  pasca hl  pourum  (sd.)  paiti.hin£öi^  paitisa  "r^m V.ÄSS;  v,%;  —  \mätyi^hy(r'ramimam dipim  patiparsiltiy  .  ,  BL4.8;6,  15,  ^.y,
3640:•  j.  apäx9Sra.iiaema-  n.  "Nordseite,  Nor- den': pasca  hü  /räsmS.däütm  ^namjanaiti Yt4.8(?).
3782:•  j.  aiwLgatay-  f.  'Herzukommen',  sva. 'Eintreten,  Beginnen':  pas:a  hamS  'gaitim .  .  pasca  z»m3  .  .  'gaitim  V.(j.6;  —  l^ma- tiham  vä  *°gats  (LS.)  '*  "bei  Einbruch  der Dunkelheit"  V.Ä4.
3987:■  j.  aiwylnhana-  n.  i)  'Gürtel,  Gürtel- schnur'*>:  'n^m  r3  aiwya»hayamnS  'mm bO/ayarnnS  (sd.)  Yti.iT,  —  /rä  i! mazdä  harat  ..  'n^m  ..  vanuhim  daSnqm mäzdayasnlm  "dir  (dem  Haoma)  brachte M.  einen  Gürtel  . .,  (näml.)  die  gute mazday.  Religion"  Y.9. 26'*;  —  yat  alle yö  mazdayasnS  ap^rmäyBks  avi  hs  hapta ■na  /rajasäiti . .  °nö "'  paitis  h!  maiayai bU)yamanS  avi  hlnara pascaili  tamauhmti 'wenn  dem  jungen  Masday.  sieben  Jahre vergangen  sind,  soll  man  ihm  den  Gürtel um  die  Hüften  legen,  worauf  ihn  die Männer  (als  ihresgleichen)  achten"  Vd, 18;  20'; — jairyö  °nö  ißjyamanff  "vieitem legt  man  (dem  Toten)  die  Gürtelschnur um"  Vd. /23),  a)  von  der  Schnur,  mit der  die  Barvsmanzvreigt  in  Bündel  zusam- mengebunden werden"":  a^a  'na  N. ioS(?).  2)  'Gewand,  Kleid';  ^5  iama *°«o"  aiitryia^qyanii  "wenn  zwei  gleiche Kleider  anziehen"  N.p4(?);  — yaii  tarasca 'na  aipi.vancainii'^.gs^); — bilyS  ant?ma 'nH  "zweitens  (soll  man  dem  Toten  mit- geben) das  Untergewand"  Vd./i>3'.
4053:•  j.  a-fra'säh-,  a-fra^säh-  Adj.  'der  am Ziel  seiner  Wünsche  ist,  des  Hoffnung  er- füllt ist'  ava.  'selig' :  pascaita  azsm  . .  aoi urune  unmsma  (sd.)  daisaymi  attayraca raocä  °sat»karua  (GP.)  ■'  :^ä^ra  ".  ,  und die  wohligen  Stätten  der  Seligen"  P.  j8; —  anayrH  raocil  . .  'sattAamca'*  ifä^r^-m G.^.6.
4058:•  j.  a-fra'srutay-  f.  "Nichtzugehörbringen, NichtVortrag  (der  Gsias):  pasca  *hähra 'sruiti  jV  paiti  ianBm  *piryäte  N.  7.
4222:yänäis  zaranaemä  (sd. )  Y.2Ä  8  £  b)  sub- stantivisch: jajA  mg . . /rabarät . .  *st»ri- naoiti  'na  *  avavat  starsm  (sd.)  . .  ya"iia  . . P.22f.  2)  vorausweisead;  i)  adjek- tivisch, a)  auf  direkte  Rede :  apasca  vajmhls yatnda'^äne  hala  °na  ga^ivya  vaca:  garS nmane  (usw.,  Y.jj.rs)  Ny.4.8;  Y.ö'5.14, Y.  10. 19.  b)  auf  ein  Relativ  als  dessen Korrelat:  °na  ^wa  yasnayazane  -na  ^wä yasna  frayazäne  yasi  ircd  yazaia  vlstäspö Yt/7,61;  —  Aauca  ^'nayiVi  nara  vohu manS  jag?r?buitarS  {anhat)  yö  .  .  ya"^a hau  yS  .  .  V.  4-48-  2)  substantivisch, a)  auf  ein  mit  ya'^anä  angeschlossenes ' Nomen,  sva.  'er,  wer  es  auch  sei,  jed- . weder':  vi.,  'tiä  sanm  mruyg  ya'kana dngvatä  rqxsyantä  "ich  entsage  der  Ge- meinschaft mit  jedwedem  feindseligen  ^r." Y.  J2.4*>.  b)  auf  einen  Satz:  tum  "na miirs^rujqm  .  .  "ä^wyqm  avaiarahi:  apa alsqm  .  .  at^d  .  .  barahi  Yl  10. 23.
4301:*asaya  *arpdusa  . .  nSiS  *°vis(i^  ästrydii vaHmaini  *asaya  (sd.)  x'a/na  vd  'vtsti astryeiti  N.  15.  2)  'Nichtlesen,  Nicht- vorlescn ,  Verweigerung  des  liturgischen Lesens':  yS  baoyö  (sd.)  aelahmSt  paräiti nöit pascalia  "Wistlm  ästryanti  (statt  Sing.) ". .  dann  macht  er  sich  durch  Verweige- rung des  (Liturgie-)  Lesens  nicht  sündig" N.4.
4441:•  j.  an-ä'st9r«tay-  f. 'Sichnicht  versündigen. Nichtgeraten  in  den  Zustand  der  Sündig- keit': *°t5  (LS.)  *pascaSa  avä  ya  any.r (gä'^ä)  srävay^it  "ohne  sich  zu  versün- digen ')  kann  er  alsdann  die  andern  ( Gä%<ls) au&agen"  N.  46;  — y^  *upsissil  nsit  7>inasli ^'t5  *pas^aSa''>  srävayöit  "wenn  er  {Bans-
4446:•  j.  an-ä'st^rstam  Absol."  'mit  Nicht- sichversündigen,  ohne  sich  zu  versündigen': %<asS  pascaiia  mazdayama  ake  nmünahe myazdim  dati^yani .  .  \yaoidayqfi\ ''  an" hama^a  ya'ia  paracil  "nach  Gefallen können  alsdann  die  M.  dieses  Hauses  das My.  bereiten  . .  ohne  sich  zu  versündigen: ganz  wie  zuvor"  V.  Ä22.
4642:•  j,  'an'tara-  Adj.  'der  andere,  zweite': hrizarpmalm  .  .  'rat  naSmäl  ailaAe  {Aa- hraAe)  ". .  von  der  zweiten  Hälfte  dieser Frist  an"  N.7/;  ;/;*'  —  pascaita ..niSAi- oöit  . .  *°r}m  arS(i?m  mayaAe  (sd.)  *par3ii- tarpm  ..W.g.aq;  — yim  antar?  vi/a(sd.) *'/■«//''  7}rjy:!  maya  V.ij.ii;  11',
4674:mit  vorausg.  ta-  dnw.  I;'  mä^a  .  .  tqm zqm  k3ray)n  .  .  vasff  .  .  tqm  'nyam  zqm k3ray>n  V.  ö.  a ;  —  yat  . .  bavül  paseaita ava  ta  'nya  maya  ifi/i  (sd.)  jasBiJ  V.5. 31.  d)  Sing,  mit  \oia.usg.  /tiseag/a  'der nächstfolgende':     asnyeke    (sd.)    pascauta
4807:mit  US  i)  'heraus-,  hinausgehen':  isar» pasca  paradristim  .  .  US  haia  baooS  (sd.) \ayap'^  \,y.2;  — ,  usayeiii  parayeni  V.  22.
4869:•  ).  ayan-,  j-,  g.  ayar-  n.  'Tag';  a) Gegensatz  zur  Nacht:  *oim  . .  'yar>  (NS.) tYjasaiti  .  .  a?va  v3  xsapa  Aog.  J/;  ■ — ai»ke  'yan  (GS.)  .  .  airikh  xsaj>ö  \t.  i .-iZ, i/.S;  Vyt.J0(?);  —  hamahe  °yqn  hamayn 1-3  xsa/w  Y.  S7-3I,  Yt.ÄS4;  '  10.  iij  (f), Vyt^f?);  —  vlspsU  'yqnia  (AP.)  xlaf- nas.'a  Y.  57. 1 7,  Yl  /.  i  i  ;  —  *frayaire  "yan (LS.)  bavaiti  (sd.j  hubai,rü  .  .  aia  apare 'y<pi  ■-  Aog.  35;  —  */rayarfne  vä  uza- yariu^fsd.)  va  *'yan''>  N.5;  —  dvadasati- hiinm  (sd.)  asü  *ayrim  °yar)  F.  27  b 27b;  —  °yqn  (LS.)  va  varstafsö  var»t3.vTrt [sd.)JaiJnti  V.S.^.  b)  als  der  Zeitraum von  Sonnenaufgang  zu  Sonnenaufgang: iiz£.a  yan  mainyenie yaty3r)N.2.^\ ^räyö  yara''  Vd.  ly;  <),  if),  si;  —  pasca xsavaidim  (sd.)  yaranqm^a'''  Vd.  f)\  11, '5>  '9  '■  c)  sva.  festgesetzter,  bestimmter Tag:  myazdahe  ''ya''''  (LS.)  "am  Tag  des My:'  N. Si-,  "y:;  *^jj  —  kaia  (sd.)  yiri (AP.)  daxiärS  .  .  drfs  Y.  43-  T,  —  yan ami^näitii&d.)  juye  tanus  Aog.^j.  d) 'Zeit':  vUpI  'yärj  (AP.)  dangö.jyäiöU (sd.)  .  .  "alle  Tage  . ."  Y.  43-  2.
4923:unsTcs  schwachbetonten  'er'*':  fravasayB ..  yä  ahurahe  xiayatö  daiinam  ufayüÜt- ynnii  yai  aim  bavaiti  *alavaxmul  yai fi  bavainti  anäzaritä  Yt.  /J.63;  —  ä  dim paskät  anumar»zatim  aHila  . .  färfndtl'a  . . visp>m  ä  akmät  yat  aim  paiti.apayat.,'H\.. iV.38;  —  vispaeibyS  sastim  baraiti  älarS. . yaübyS  alm'''*  *ham.paeaili  ..  \.62.T,  — iim  Aaxa  Aase  baraiti  . .  ?  äat  yai  s!  a^m  " baraiti  .  .  Y.  62.  8f.;  —  yim?m  .  .  yerihe xsä^rä',a  ndit  aotim  inha  . .  para  akmät yat  hlm  a!m  *draogpm  välim  .  .  patti.- barata  Yt.  ig.  33 ;  —  tvai  na  *ai^rapaitim updisai  .  .  iim  *aSm  at^^  aS^rapaitim upayat  (sd.)  N.  Jlt;  —  mürtm  .  .  yd .  . frä  rasmanö  scandayeiti  .  .  ari  dlsalm.  . Ji^iM  *baraiti  Vtio-^Gt;  loi,  71  (yavata aim),  .5', 43  {yezi  alm),  47  (ya^a  am); —  aom  asmatum  ,  ,  mariay^n  ahe  yäiia vis  aim  .  .  Yt.  ij,2.  2)  auf  ein  Nomen vorausweisend:  äa^  mg  alm'°^  pait- yaoxta  AaomU..Y.ff.i;  V.2.3.  III)  ver- doppelt, substantivisch  sva,  'irgend  ein  be- liebiger': _)(7/  hl  nazdiUö  dahmö :'dü'/(sd.)  yavat  vä  aSm  aim^^^ uübya  N.2;.
```


## [2026-09-04T22:46:13.754Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pasā\\|pasa \\|pasāva\\|pasava\" KNT.txt | head -20"
}
```


### [2026-09-04T22:46:13.793Z] TOOL RESULT

```
2313:П. Ace. -dim (Av. dim), not differentiated in function from -5im, seems to have originated by wrong division in such combinations as pasdvad- im (cf. DNa 33, where we divide it pasava-dim), in which -im was acc. to *is, Lt. is ‘this, he’. Асе. pl. -diš (Av. di8) is formed by analogy to -И$, and is sometimes written as a pee word (DB 4.34, 35, 36); for a misread aec. pl. dary (DB 5. ы see Lex. s.v. daty.
2700:К. With prepositions, the mixed use with -ройу (see E); DB 3.32 pasa mand ‘behind me’; with anu- ‘according to’, in DNb 16, 18; with following rüdiy, to express agent, in DNb 9, 10f; with encli- tic -rddiy, in avahyarddiy ‘on account of this’.
2856:д, enclitic postposition attached to the locative singular of all common nouns and adjectives ex- cept in phrasal adverbs, and to all locatives plural; also preposition with phrasal adverb pasava to denote limit in time (DSe 48); see also уйй à, П.
3487:31 büjiya : avam : Bardiyam : avàja * уаба : Kabüjiya : Bardiyam : avaja : kürahy 32 à : пазу : azdà : abava : (уа : Bardiya : avajata : раѕауа : Kabijiya : Mudráyam 33 : akiyava : уада : Kabūjiya : Mudrayam : aSiyava : pasáva : kara : апка : abava 34 : pasava : drauga : dahyauvi : vasiy : abava : uta : Parsaiy : ша : Mádaiy : ut 35 d:aniy&uvà : dahyuSuvà ; 0àtiy : Dàrayavaus :х3йуайуа : pa
3529:78 à : puça : hauv : udapatatà : Babirauv : káram : ауада : adurujiya : adam : Nab 79 uk"dracara : amiy : hya : Nabunaitahy& : риса : pasava : kära : һуа : Babiruviya 80 : hamva : ably : avam : Naditabairam : aSiyava : Babirus : hamigiya : abava : x
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
3633:90 maiy : basta : adáriya : haruvasim : kara : avaina : pasavasim : Arbair&yá :
3637:94 uv : Paréavaty : aha : avam : Ката : avaharda : hamigiya : abava : pasava : Vištāspa :
3715:31 iya : пата : Parsa : mand : badaka : avamSàm : maistam, : aku 32 navam : hya : aniya : kara : Рагза : pasā : mana : аўуауа : Mā
3742:59 vahaus : xsayatiyahyà : gaubataiy : pasāva : hauv : kara : айуа
3753:: 80у : Dárayavaus : xSdyafiya : pasava : dahyaus : ma 76 nai : abava : ima : tya : mand : kartam : Harauvatiy&
4249:25 PT ju abis: pasāva : re avaniya : aniyā : 26 XL : araXanis : baršnā : aniyd : XX : arašaniš : bars
4685:D'Sb = Darius IT, Sesa B. 1 айат: Dárayasaus : XS : vazraka : XŠ : XSyanam : XŠ : DHyünàm XŠ : а 2 hydyd : Вуй: Artazsagahyá : XShyá : puça : Haxamanisiya : 3 batiy : Dürayavaus : XS : ima : hadiš : Arlaxíacü : paranam : akunaus : 4 hya : mand : pilà : ima : hadis : pasava : vasnà : ÁMha : adam : akunavam Notes то D'Sb: Вга. WZKM 39.85-7, after the Akk., restored ? [apara]m ‘upper part’ = ‘part at the top of the slope’, and * [adaram] ‘lower part’ = ‘part lower on the hill’; but Hinz, ZDMG 91.251-2, restores [paranalm and [pasava], in temporal sense, which is preferable. *akunas in copy b. TRANSLATION OF D'Sb: $1. 1-2. ... (= DNa 8-12, with one omission), son of Artaxerxes the King, an Achaemenian. §2. 3-4. Saith Darius the King: This palace Artaxerxes previously built, who was my father; this palace, by the favor of Ahuramazda, I after- wards built (to completion).
```


## [2026-09-04T22:46:20.418Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pasa-\\|pasā\\b\\|pasáva : adv\\|pasāva\\.\" KNT.txt | grep -i \"adv\\|prep\\|Av\\.\" | head -20; echo \"===\"; grep -n \"‘after\" KNT.txt | grep -i \"pas\" | head"
}
```


### [2026-09-04T22:46:20.490Z] TOOL RESULT

```
===
2676:A. Possessive, as in DB 2.19f тапа badaka ‘my - subject’; DB 4.82f anusiyà mand ‘my followers’, 3 whence also with its opposite m DB 2.79f haup. E | maty hamigiya abava ‘he became rebellious toward 3 me’ (also DB 3.11, 4.12, instead of hacéma ‘from “$ me’ and the like, DB 1.40, 2.6f, 3.27, 8.78, 3.810); «4 DB 1.4 mand pita, 1.29f Kabujiyahya brátà, and “$ with other words of relationship. This is found also 3 in the predicate: DB 3.9f pasiva dahyäuš manā 4 abava ‘afterwards the province became mine’, cf, 4 DB 5.19f, 35f, and DB 3.58f avam Катат hya ` Dérayavahaus х&ауабтуаћуа goubataiy ‘that army ‘$
2702:A. Expressing place where, without a preposi- tion, as in DB 1.34f pasdva drauga dahyauvā vasiy abava щй Parsaty ша Madaty ша aniyãwā dah- yusued ‘afterwards the Lie waxed great in the country, both in Persia and in Media and in the other provinces’; DB 2.75 duvarayãmaiy basta аййттуа ‘he was held bound at my palace en-
2704:trance’; DB 2.76 pasávasim Hagmatinary uzmayā- patiy akunavam ‘afterwards I put him on the stake (= impaled him) at Ecbatana’; DB 1.15 уату drayahyü ‘(those) who (dwell) by the sea’ (not ‘islanders’, since the term denotes the sa- trapy of which Dascylium was the capital, JNES 2.304). With ‘king’, singular nouns are in the loca- tive, as in DB 1.2 xSéyatiya Pérsary ‘king in Persia’, though plurals are in the genitive (§250.C); similarly DB 1.81 zšaçam tya Babtrauy ‘the kingship in Babylon’. It is a substitute for the genitive in DB 2.23f hya Madaisuvd тайа dha ‘who was chief among the Medes’ (cf. §250.D).
2711:A. With hada, to denote accompaniment either friendly or hostile: DB 2.21f pasdva haw Vidarna hada kärä ašiyava ‘after that this Hydarnes with the army marched forth’; DB 2.23 avadé hamar- anam akunaus hadi Müdaibi$ ‘there he made battle with the Medes’.
2760:67. ApPosrTIVES occur in the following cases; lack of examples in the other cases is accidental: nom. DB 1.1, 1.53, and almost everywhere; ace. DB 1.54, DPd 2, DNb 4, etc.; gen. DB 3.59, DPd 9-11, XPe 14, etc.; loc. infrequent, DB 1.34f. More often the appositive, if more than а single word or if to an oblique ease, is expressed by an anacoluthie nominative phrase, followed by a resumptive pronoun or adverb ($314a; 8312). Partial appositives occur as in DB 1.34f pasdva drauga dahyawd vasiy аата щй Parsaiy ша Mädaiy utü aniyãwā dahyušuvā ‘afterward the Lie became great in the country, both in Persia and in Media and in other provinces’; also DB 1.401, 1.48f, DSf 25f ikä avaniya aniyā XL ara- Santis baránà ата X X атаќаті bar snd ‘the rubble
2867:pasd ‘after’, with accusative of time in pasd tanüm
2868:‘after himself’ and in the phrasal adverb pasáva
2869:‘after that’; with genitive of place in pasd mand
2911:(c) In temporal clauses introduced by ‘when’, ‘after’, ‘while’, ‘as long as’, ‘until’, in past time (8804.2, b, d, e, f), and by ‘whenever’, ‘until’ in present time as generalizations (§304.c, f).
2987:8295. THe CONJUNCTION yaéd has the meanings ‘as’ (marked by the correlative алабӣ, once mis- written avd; sometimes no correlative with yofá mim Гата аһа); ‘when’, shading into ‘after’ (which is marked by the correlative pasdva ‘after
```


## [2026-09-04T22:46:27.005Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pasā\\s*:\\|^pasa\\|pasi, prep\\|pasà, prep\\|pasā, prep\" KNT.txt | head; echo \"=== lexicon area ===\"; grep -n \"Av. pasca\\|Av. pasča\\|Skt. pascā\\|paSca\" KNT.txt | head"
}
```


### [2026-09-04T22:46:27.075Z] TOOL RESULT

```
3715:31 iya : пата : Parsa : mand : badaka : avamSàm : maistam, : aku 32 navam : hya : aniya : kara : Рагза : pasā : mana : аўуауа : Mā
=== lexicon area ===
```


## [2026-09-04T22:46:31.015Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pasáva\\|pasāva\\|pasáva,\" KNT.txt | sed -n '1,60p' | grep -n \"adv\\|prep\\|OP\\|Av\" | head; echo \"---\"; grep -n \"^parsa\\|^pasa\\|^paru\\|^pati\" KNT.txt | head -20; echo \"--- try lexicon markers\"; grep -n \"‘after, behind’\\|'after, behind'\\|after; adv\" KNT.txt | head"
}
```


### [2026-09-04T22:46:31.088Z] TOOL RESULT

```
2:2868:‘after himself’ and in the phrasal adverb pasáva
26:5680:pasáva phrasal adv. (§191.IV) ‘after that, afterwards’: pasé + asn. ava (8181). DB 1.27, 30, 32, 33, 34°, 35f, 40, 43, 46, 54, 72, 731, 75, 79, 82, 83, 86, 91, 94; 2.1, 3, 4, 12, 16, 19, 21, 27, 31, 32, 47, 49°, 51, 52, 62, 64, 67, 71, 72, 81, 84f, 94; 3.1,4, 9, 12f, 15, 20, 25, 29, 33, 36f, 41, 50, 59, 70, 73,75, 81, 84, 86, 90f°; 4.5, 35, 91; 5.3, 6, 9, 10f, 13, 21°, 28, 25°, 29; DSe 48; DSf 25; DZe 10; XPh 36; XSe 3; XV 23; А:Ра 21°; Рр 4°. pasãva-šim DB 2.76, 90. pasdva-Saiy DB 2.88.  pasáva-dim DNa 33. pasdva-mary XPh 32.
---
392:paru-zana- ‘having many men’, with z from j.
401:patiyazbayam ‘I proclaimed’, with Med. -zb-, but h*zdnam (acc.) ‘tongue’ with OP -z-, both from ТЕ ди; see also $91.
610:paruvam (and derivatives), corresponding to Skt.
771:patiyabaram DB 1.68, perhaps for patiyabaram; 4
1063:pati-padam ‘on its base’, Skt. padd- ‘step’, Gk.
2844:patiš ‘against’, governing a person as goal.
2863:patiy with accusative, ‘against’ (DNb 22), ‘on’ in phrasal adverb patipadam (DB 1.62); as ortho- tone postposition with accusative, ‘on’, express- ing time when (DB 2.62); as enclitic postposi- tion, local ‘in, at’ with instrumental in v@apairy
2865:patiy (DB 2.76, 91; 3.52, 92), temporal ‘during’
5035:pati- + ay- ‘come to, come into the possession of’: patiyãiša” За pl. imf. ($140.11, $208, §232.- П) DB 1.18, 18.
5626:patiy adv., prep., prefix ($140.I, $1911): Av. рай, Gk. (dial.) rori, pIE *poti, cf. pIE *proti in Skt. prát, Gk. Hom. троті, classical rpés (cf. Lg. 20.9-10).
5632:patikara- sb. ‘picture, (sculptured) likeness’: .
5641:patisam adv. ‘in addition’: extension of patiš, ef. for formation Ose. per-um ‘without’ to (Lt.) per, and for meaning Gk. трд ё ‘and besides’, Lit. atque from *ad-que ‘and thereto’ (OP patiy, Gk. тро, Lt. ad agree in marking something as an ad- dition). patišam DB 4.89 (p* probable but not certain KT); (раат DB 4.90 (restoration of Konig, Klotho 4.45; see also Kent, JAOS 62.267- 8).
5658:paru- adj. ‘much, many’: Av. pouru-, Skt. purú-, Gk. modts, Gt. filu, pIE *palu- (§63.1, $107). See also paruzana-. рати) nsm. ($114, $127, $140.I) DB 449; DSf 56 bis. pariindm gpm. DSi 4, 5; DE 9, 10; XPa 5 bis; XPb 9, 10; XPc 4f, 5; XPd 6f, 7f; XPf 6, 7; XPh 5, 6; XE 9f, 11; XV 7,8; А:Ра 7°, 8°; А°Нс 6 bis. parünàm gpf. DPe 4. parüenüm ($28.П) gpm. DNa 6, 7; DSe 6, 7; Азра 6, 7.
5659:paruva- adj. ‘being before in time or place’ (§35.1[): Av. paurva-, Skt. pürva-, pIE *pruos (868, $150), ef. Gk. Ion. трохоѕ ‘early’. See also paruviyata, paruviyaüd. parwā npm. ‘former’ DB 4.51. parwam asn. as adv. ‘formerly’ DB 1.9; DBa 15f; DSe 43°, 47; XPh 36, 39; paruvam- ciy DB 1.63, 67, 69.
5662:paruzana- adj. ‘having many men, or many kinds of men’ (‘having men of all tongues’, Wb. ZfA 44.165, after the Akk.): paru- ‘many’ + zana- ‘man’ ($9.11, $88, $120, $161.ППа). paru- zanānām (5140.1) gpf. DE 15f; XE 15f; А!Ра 12°. poruvzandndm (523.1) XPb 15f; XPd 11. раги zandnam ($23.11, $44) XPa 8; XPe 7; XPf 11; XPh 9; XV 12.
5732:pati- + à + bar- ‘bring back, restore’: райуй- baram Ist sg. imf. DB 1.68 (but -à- perhaps only by influence of pardbartam, JAOS 62.275; 558, $206c).
--- try lexicon markers
```


## [2026-09-04T22:46:34.850Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5675,5682p' KNT.txt"
}
```


### [2026-09-04T22:46:34.889Z] TOOL RESULT

```
pasü prep. ‘after’, temporal with асе. and local with gen. (Bv. BSLP 33.2.153): Av. paséa, NPers. pds, Skt. paácá, isn. to stem in Lith. (dat.) adv. and prep. різки ‘behind, later, after’ (Foy, KZ 35.26); pIE *po as in Lt. po-lið, positus, Gk. &-vó, + *sg*é, inst. to root noun from *seq*- ‘fol- low’, Av... hacatte, Skt) Gdeate, Gk. trerai, Lt.
See nada lai baa a D Lo AMA tae io at OT IPE Ауаз a зз
~
LEXICON
sequitur (§105; Uhlenbeck, Etym. Wtb. d. altind. Spr., s.v. paced). The s in pasá is OP for Med. $c, Av. sé, from pAr. $c (Ву. Gr. §114; otherwise Mt. Gr. §114). Less probably pAr. *pas (Lith. pds ‘at, to’) from the same *po + adv. -s as in OP patiš, + -cà isn. of stems in -айс-, for -acã (from *-ncà) by influence of contracted forms like Skt. praca (*pra-acd) to ртайс- (*pra-atic-) ‘forward’, cf. similar analogical form in Skt. adv. nica ‘downward’ (for *ni-acd) to пуайс-. Hardly from *pas (as above) + -à after its opposite para ‘before’ (Bthl. AiW 879). Direct cognation with Lith. páskw: is eliminated by the second and third etymologies; with Av. pasta, Skt. paícá, by the third. pasã with gen. DB 3.32; with асе. XPf 31 and in pasdva (q.v.).
pasáva phrasal adv. (§191.IV) ‘after that, afterwards’: pasé + asn. ava (8181). DB 1.27, 30, 32, 33, 34°, 35f, 40, 43, 46, 54, 72, 731, 75, 79, 82, 83, 86, 91, 94; 2.1, 3, 4, 12, 16, 19, 21, 27, 31, 32, 47, 49°, 51, 52, 62, 64, 67, 71, 72, 81, 84f, 94; 3.1,4, 9, 12f, 15, 20, 25, 29, 33, 36f, 41, 50, 59, 70, 73,75, 81, 84, 86, 90f°; 4.5, 35, 91; 5.3, 6, 9, 10f, 13, 21°, 28, 25°, 29; DSe 48; DSf 25; DZe 10; XPh 36; XSe 3; XV 23; А:Ра 21°; Рр 4°. pasãva-šim DB 2.76, 90. pasdva-Saiy DB 2.88.  pasáva-dim DNa 33. pasdva-mary XPh 32.
pasti- sb. ‘foot-soldier’: Skt. pailt-, from pIE *ped- ‘foot’ (OP pad-) + suffix -t&- ($85, 5152.11; Wb. Grab 40, Hz. ApI 94-8). — pasti$ nsm. DNb 48, 45.
pilar- sb. ‘father’: Av. pilar-, NPers. pióür, Skt. pitdr-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.11, 875.1, 576.1, $154.II); see also hamapilar-. pita пет. ($86.П, $124.5, $186.1T) DB 1.4 bis, 5 bis, 6; 2.93; DBa 5, 6, 6f, 7, 8; DSf 12, 58; XPa 15; ХРе 12; XPf 16, 17, 19, 23, 31, 33, 42; XPg 7; X8a 2; XV 18; А!Ра 20f; D?Sb 4°. pica gsm. ($78, $124.5, $186.If) XPa 20; ХРе 14; XPf 35, 38, 47.
```


## [2026-09-04T22:46:43.042Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pasca-\\|pasča-\\|j\\. pasca\\|paskät  Adv\\|paskat Adv\" BRT.txt | head -20; echo \"===\"; grep -n \"hinterher\\|'nachher'\" BRT.txt | grep -i \"pas\" | head -10"
}
```


### [2026-09-04T22:46:43.111Z] TOOL RESULT

```
15887:•  j.  paskät  Adv.  1)  räumlich  'von  hinten her,  hinterher,  hinterdrein':  _)'«zja^i/aan'a.-
===
15887:•  j.  paskät  Adv.  1)  räumlich  'von  hinten her,  hinterher,  hinterdrein':  _)'«zja^i/aan'a.-
15888:naf^mJl . .ym  pasiSt . .  Yt. x6.%;  —  vlt3r>m fsd.)  /*  kamif^jm  jantSrim  pars  dul' mainvBm  Yt.  17.  11;  —  k^a  nS  arsa gavati^Tm  apayät P'  vaztmnS  mihrS  "wzan wird  M.  . .  einholen,  hinterher  fahrend?" Yt  10.  86;  —  /rava/ayff  .  .  %wSs9m  p' fravaz3nte  Yt.  7j.  39;  —  S  dim  p°  anu- mar3sat?m  (sd.)  aSfta  .  .  plnndica  Yt. 8. 38.  a)  mit  voranstellendem  enkl. fproltl.?)  Gen.:  spu^am  yS  mS  p'  vataite "das  Heer,  das  hinter  mir  her  zieht"  Yt. 14.  58;  —  äat  hl  p'  fradvarat  äsi(  Yt. 19.47;  —  aal  hi  p'  hqm.räzayata  Yt.  Zp, 49.  a)  in  Verbindung  mit  *aoe  dn.:  ydi
```


## [2026-09-04T22:46:46.294Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pasca\\b\\|pasca  \\|•  j\\.  pasca\\|pasce\\|pasca,\" BRT.txt | head -10; echo \"===\"; sed -n '15870,15895p' BRT.txt | cut -c1-400"
}
```


### [2026-09-04T22:46:46.356Z] TOOL RESULT

```
3583:—  ma%rym  spmttm  . .  pmrumca  . .  'r^mca V.  4.45;  45;  —  ahun?m  vairJm  . .  Tim sraoidyehya  (^^  frasrüiti  Y.  5. 14;  — apanmta  tiais^mi&A.)  G.3.T, —  'raheca yamahe  haplanhatdis  Vr.2/.o;  0,4^;  — ranuhlsla  a'A  .  .  hupaurva  (sd.)  vahehiS Ti/"  räsaintü  ¥.52.3;  —  aiwiea  'rim patiia  'rym  apsca  paurvalibya  "und  (man soll)  einen  zweiten  (Rüden)  und  dann noch  einen  weiteren  (zulassen)  und  zwar (soll  man  ihn)  gesondert  von  den  beiden ersten  (halten)"  V.  i^.  48.  3)  '>  der  Zeit nach 'der  spätere,  kUnftige'rja^a  mä  'racil (NPm.)  saoiyanis  stavqn  V.9.  2;  — yastä datrSMg  °rö  .  .  tarS.mqstä  "wer  darum künftighin  (eig.  posterior)^  den  D.  ..  auf- sagen wird"  V.  4:5. 11;  —  huzantSus  paiti •raya  YL  13. 134.  a)  mit  ayan-  n.  'der spätere  Teil  des  Tags,  Nachmittag':  */ra- \aire  ayqn  bavaiiii^A.)  hubar,rS  ..  a',a  "re ayqrt  duWirjm  ". .  dann  am  Nachmittag (kommt)  das  Unglück"  Aog.jJ.  A)  ASn. 'r?m,  'ram  und  IS.  °ra  als  Adv.  'postea, später,  künftig' :  yezi  nairyS  aukat  pasca hl  pourum  (sd.)  paiti.hin£öi^  paitisa  "r^m V.ÄSS;  v,%;  —  \mätyi^hy(r'ramimam dipim  patiparsiltiy  .  ,  BL4.8;6,  15,  ^.y,
3640:•  j.  apäx9Sra.iiaema-  n.  "Nordseite,  Nor- den': pasca  hü  /räsmS.däütm  ^namjanaiti Yt4.8(?).
3782:•  j.  aiwLgatay-  f.  'Herzukommen',  sva. 'Eintreten,  Beginnen':  pas:a  hamS  'gaitim .  .  pasca  z»m3  .  .  'gaitim  V.(j.6;  —  l^ma- tiham  vä  *°gats  (LS.)  '*  "bei  Einbruch  der Dunkelheit"  V.Ä4.
4058:•  j.  a-fra'srutay-  f.  "Nichtzugehörbringen, NichtVortrag  (der  Gsias):  pasca  *hähra 'sruiti  jV  paiti  ianBm  *piryäte  N.  7.
4222:yänäis  zaranaemä  (sd. )  Y.2Ä  8  £  b)  sub- stantivisch: jajA  mg . . /rabarät . .  *st»ri- naoiti  'na  *  avavat  starsm  (sd.)  . .  ya"iia  . . P.22f.  2)  vorausweisead;  i)  adjek- tivisch, a)  auf  direkte  Rede :  apasca  vajmhls yatnda'^äne  hala  °na  ga^ivya  vaca:  garS nmane  (usw.,  Y.jj.rs)  Ny.4.8;  Y.ö'5.14, Y.  10. 19.  b)  auf  ein  Relativ  als  dessen Korrelat:  °na  ^wa  yasnayazane  -na  ^wä yasna  frayazäne  yasi  ircd  yazaia  vlstäspö Yt/7,61;  —  Aauca  ^'nayiVi  nara  vohu manS  jag?r?buitarS  {anhat)  yö  .  .  ya"^a hau  yS  .  .  V.  4-48-  2)  substantivisch, a)  auf  ein  mit  ya'^anä  angeschlossenes ' Nomen,  sva.  'er,  wer  es  auch  sei,  jed- . weder':  vi.,  'tiä  sanm  mruyg  ya'kana dngvatä  rqxsyantä  "ich  entsage  der  Ge- meinschaft mit  jedwedem  feindseligen  ^r." Y.  J2.4*>.  b)  auf  einen  Satz:  tum  "na miirs^rujqm  .  .  "ä^wyqm  avaiarahi:  apa alsqm  .  .  at^d  .  .  barahi  Yl  10. 23.
4807:mit  US  i)  'heraus-,  hinausgehen':  isar» pasca  paradristim  .  .  US  haia  baooS  (sd.) \ayap'^  \,y.2;  — ,  usayeiii  parayeni  V.  22.
4869:•  ).  ayan-,  j-,  g.  ayar-  n.  'Tag';  a) Gegensatz  zur  Nacht:  *oim  . .  'yar>  (NS.) tYjasaiti  .  .  a?va  v3  xsapa  Aog.  J/;  ■ — ai»ke  'yan  (GS.)  .  .  airikh  xsaj>ö  \t.  i .-iZ, i/.S;  Vyt.J0(?);  —  hamahe  °yqn  hamayn 1-3  xsa/w  Y.  S7-3I,  Yt.ÄS4;  '  10.  iij  (f), Vyt^f?);  —  vlspsU  'yqnia  (AP.)  xlaf- nas.'a  Y.  57. 1 7,  Yl  /.  i  i  ;  —  *frayaire  "yan (LS.)  bavaiti  (sd.j  hubai,rü  .  .  aia  apare 'y<pi  ■-  Aog.  35;  —  */rayarfne  vä  uza- yariu^fsd.)  va  *'yan''>  N.5;  —  dvadasati- hiinm  (sd.)  asü  *ayrim  °yar)  F.  27  b 27b;  —  °yqn  (LS.)  va  varstafsö  var»t3.vTrt [sd.)JaiJnti  V.S.^.  b)  als  der  Zeitraum von  Sonnenaufgang  zu  Sonnenaufgang: iiz£.a  yan  mainyenie yaty3r)N.2.^\ ^räyö  yara''  Vd.  ly;  <),  if),  si;  —  pasca xsavaidim  (sd.)  yaranqm^a'''  Vd.  f)\  11, '5>  '9  '■  c)  sva.  festgesetzter,  bestimmter Tag:  myazdahe  ''ya''''  (LS.)  "am  Tag  des My:'  N. Si-,  "y:;  *^jj  —  kaia  (sd.)  yiri (AP.)  daxiärS  .  .  drfs  Y.  43-  T,  —  yan ami^näitii&d.)  juye  tanus  Aog.^j.  d) 'Zeit':  vUpI  'yärj  (AP.)  dangö.jyäiöU (sd.)  .  .  "alle  Tage  . ."  Y.  43-  2.
5050:'in  der  angegebenen  Weise':  U . ,  nüram %74väm  vamavatäm  ty<^  manä  kartam  °'hil *abava'"'>  ". ,  soll  dich  jetzt  überzeugen: was  von  mir  getan  wurde,  so  (wie  an- gegeben) geschah  es"  Bh.4.10;  —  ll^rf- käram  dUÜy  ..'>ä^  xmäsahidis  ada  (sd.)- taiy  .  .  D.  tf.4;  —  aAmiii  bityS  üjasal  .  . gSu^  iihrpa  ..'ha  äjasat\x.  14.6;  9-27*; ~ paiti  mqm  pinsaituka  ..  'ha  te  ar?hal  ^ vatihs  N.jS.T,  7,  Vyt.42;  —  pasca  hri- ,
5103:•  j.  ava,m9r«tay-  f.  'Sterben,  Tod'  uzw. i/dA^cher  Wesen'*:  tat  asti  yUnd  duhna- nat?hs  . .  i^arshfm  pasca    'ntfim    H.  2.
5308:•  j.  a-ratu'fri-  Adj.  'der  nicht  r.  ist,  die Ratav  nicht  befriedigt,  es  ihnen  nicht  zu Dank  macht,  gegen  ihren  Willen  ver- stösst':  äahms  zaota  dahmS  upa.sraolärü vispe  ratu/ryö  tanupirii^ö  zaota  tarnt- p>r3%5  upü.sraotltrS  vupe  '/ryüti.^i);  — yai  ig  däiti  dalätH  ^rafufrÜ . .  yesi  aal hSnDit  däiti  daoäiti  '/ris'ü.io^;  wo,  loi'^, S03, 104,55,  *55  ■';  — yi  ^ri/*Aa>räricS yätayeinle  ratufryS  yai  Hat  (ä-ri/)  nSii *Aa>r.'rtci>  yataytinti  'fryO  N.  S8;  gj,  gi, 9-',  93>  95;  —  y^i  •  ■  »o  ratu/ryö  yezi *aai  .  .  uva  -/ryJ  (ND.)  ü.$4;  —  yai arastnm  (sd.)  .  .  pairi.iioa  .  .  °/rya  pasca vä  pars  vä  pairi.ä6a  °/ryS  ii.32;  —  yä yastam  *yazfnti..  nva  *ratu/rya  Aam.srul.- väcayala  (sd.)  ^yax^nti  *«va  *'fiya  (ND.)'' N.  24',  — yö  aiwyänhayäiti  kar>tSsca  °/ryS pasca  aiitiySstim  nitaohydti  ratufrys  N. tV^.  a)  mit  Gen.  dessen,  wodurch  (und wofür)  man  ar.  ist  oder  wird:  yasnahe advakt  (sd.)  ratu/ris  'frii gä'iianqm  N.22; —  kaithqm  ml  gä'^anqm  srutanqm  °/rii3 yä  ^maizö  vä  . .  *srävayeiti  aetaesqm  vacqm "fris  "mit  welchen  aufgesagten  G.  verstbsst
===
8Si
*pasu.vastra-
pasJ£a
SSz
(sd.)  fraät^aiti  V.4-^\  —  yjs  mihnm ahoi.druzaiti  yim  *sj«  V.  4-i3-
')  Eig.  wobei  Verpfandung  eines  Schafs  statt- findet.  Unter  den  6  Verlragsarten  nimmt  dieser die  vierte  Stelle  ein,  iwischen  dem  «Arönui'ii.. maritS  nnd  stav5.mas5  ttehend.    S.  noch  lu  Pfi. Vgl.  aimmayö.maza:   —   Pü.:  pah  maiät,  erl. _j  ilb-  'drei  SHr'   (nlml.    ist  das   Pfandobjekt wert).  —  >)  N.\,  hat  «reimal  •zamö;  Druck- fehler.
•  j.  'pasu.vastra-  n.  TCleid  aus  Tier-, /spez.i  Schaffell':  carimanam  'ranamca N.  >8;  8v,  —  'rahe  F.^b.
Eig.  'Tier-,  Schaftleid',  —  Pü. :  fak  vas/rak.
•  j.  'pasu.vastra-  n.  "Viehstall';  az3m  . .
/T   nipayemi  .  .  yäia  pasBm  'r»m  (Subj.,
näml.  tiipayeiti)  Yt.5.  89''.
*fa<tra-  n.  'Wohnung',  lum  V.  'z-ai-'l.  — >1  Vgl.  zSt.  Ggr.  OK.  48.  —  ')  Cot.  invis/r (Kluge  Stammbitdungslehre<4S]könntehaptol. für  *inBi-7aiifr  stehen.
•  '].  pasuS.haurva>  Adj.,  mit  ^sfian-  m 'Schäferhund':  itr'a  asti  spä  'rt'S  dlifyS.- gStu^l  .  .  yS  yn/yastlin  ha:a  gai^aby^ paräiti  sraXsfiiini  fsd.)  /-Ivfi/  vihrkim^a •^i  wem  ist  der  Schäferhund  richtig  am Platz?  .  .  (Bei  dem)  der  eine  Y.  weit  von seinem  Hof  weggeht  .  ."  V. /j.  17;  49', ^■t^\  —  ipSmm  yim  ..  °rum  V.r^.12, 20,  24; — s
E^^.  "der  das  Kleinvieh,  die  Schafe  beschütit'; S  387.  CrBd,:  sak  i  hipäti,  Riv. :  sai  i  rama. —  Pü.;  trantskr.;  in  Sü.  (lu  V.  19.  a):  fxiMi- paiä.  —  I)  Unthem.,  lu  S  4i3.  3  a.  —  ')  GP. aU  SubJ.j  s.  iSt.  Hbm.  ZDMG.  36.  %S-
•  j.  pasuä.hasta-m,,'hastay-m  'Hürde, Pferch    für    Kleinvieh,    Schafe":    mai\ySi
•taihia  V,Jv47;  —  yeti^a  alsa  ge^wa 'tazlva  frajasät  .  .  yS  alfym  °t?m  uzäasia yeAhh  vS  a^  °Hi  atghat  V.J5.3zf.'^ Komp.!/ffJni'-(-**ai/.7..  *ha$lay  (S  ^P/).  eig. 'Niederlassung',  lum  V.  'haii-;  vgl.  ai.  sAdma pahiminti  RV.  9.  97.  I.  —  PQ.':  paha^l  (d.  i, fioA-ait,  s.  in  asM-).  —   ")  S.  iSt.  unter  iillrä.-
•  j.  pasus.x*ar99a-  n.  'Nahrung  tür  die Haustiere':  •'ijm  V.SQ.^i  Gl.
•  j.  paskät  Adv.  1)  räumlich  'von  hinten her,  hinterher,  hinterdrein':  _)'«zja^i/aan'a.-
naf^mJl . .ym  pasiSt . .  Yt. x6.%;  —  vlt3r>m fsd.)  /*  kamif^jm  jantSrim  pars  dul' mainvBm  Yt.  17.  11;  —  k^a  nS  arsa gavati^Tm  apayät P'  vaztmnS  mihrS  "wzan wird  M.  . .  einholen,  hinterher  fahrend?" Yt  10.  86;  —  /rava/ayff  .  .  %wSs9m  p' fravaz3nte  Yt.  7j.  39;  —  S  dim  p°  anu- mar3sat?m  (sd.)  aSfta  .  .  plnndica  Yt. 8. 38.  a)  mit  voranstellen
vTspe  te  apayeinli(5p.Ti  o.)yq*aoep''  7'yeinti iim'i  *aoe  p*  äfmle  Y.57.  29,  a)  zeit-
lich 'darauf,  alsdann':  äat  mqm  narS  p' vaz^iiU  ahtirsm  masdam  dariyS ya¥t>mh . . H.  2. 14.  a)  mit  voranstehendem  enkl. Gen.  neutr.  h?  Avt.:  apa  hl p°  */raoirisyeiti .  .  aisa  drux¥  yl  nasul  nfnhanat  haca "alsdann  kommt  die  Dr.  wieder  zum  Vor- schein von  der  Nase  her"  V,^.  40.
Zum  lat.  /flj/j  idg.  -,'i-  aus  -ilk-\    Wn.  AiGr.
7.  269,  Bthl.   ZDMG,   c,o.  722;    S  178  a  (!.
357.  4.  —  Vgl.  fasä  (usw.\  —  ai.  Tgl.  paicAl
Adv.  —  Fü. ;  pas,  pas  haK
•  j.  pasfa  'post';  i)  Adv.;  a)  räumlich, a)  "hinten":  p' pavii pars pava  spasvXoaita Yt.  10,46;  F.  ?g;  —  /'  hi  vaylansm  .  . upa.dvqsaiH  "..hinten  auf  seinen  Kopf.." V.^.42;  9.16;  —  yezi  nairyB  anhat  p° fa püurum  (Sp.  872  o.)  paiti.hinMl  paiti^a aparim  V.  ÄgS;  58;  — yezi  aiwySnhana aipi.var)cainti  p°  vä  palri  (t'S)  bar»ttti ^■95-  b)  zei
```


## [2026-09-04T22:46:54.593Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ===\"; grep -n \"^pas \\|^pas,\\|pas \\[p(t)\\|pasēn\\|pasen\" PHD_mackenzie.txt PHD.txt | head -20; echo \"=== NYB ===\"; grep -n \"^pas\\b\\|pas  'after\\|pasēn\" NYB_vol2_glossary.txt | head -20; echo \"=== HUB ===\"; grep -n \"pas \\|pasin\\|pasča\" HUB.txt | head -20"
}
```


### [2026-09-04T22:46:54.676Z] TOOL RESULT

```
=== PHD ===
PHD.txt:545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
PHD.txt:4644:frašn frašagirdīg frašagird frašamurw fradāg fradom fradomīh pardag pambagén pambag passaxt passáxtan passox passáz- passāzišn pasen pasēmāl pasēmālīh brin-t bridan™ passazagih passazag past, pist pistag
PHD_mackenzie.txt:4071:pas [AHL < A '?zr; BATL < A b-'tr;ps 1= M, N ......] then, afterwards,
PHD_mackenzie.txt:4075:pas [p's I = M, N ......] guard, watch.
PHD_mackenzie.txt:4084:pasen [psyn l I N pasin] final, last.
PHD_mackenzie.txt:6966:last (a.) abdom, pasen.                   libation zOhr.
PHD_mackenzie.txt:8605:passinJag               \~~~Q)          pasen                        \K» eu
PHD_mackenzie.txt:8804:pas,1-2pay                    -()Q)            padixiayih         ~tUQ)
=== NYB ===
2980:pas PHL; B’TL 5726], with -c: pas-ic PHL-c] adv. 1. behind: bē raft hend... Vahuman pes, Zartuxšt pas they went away, V. first, Z. behind 5712-33; ~ ~ one after the other 11012; ~ andarg haxt on her back between her thighs 572%; hac ~ from behind 25%. 2817; 6 peš... 6 ~ forwards ... backwards 6811-12; — hac ~ + prep. behind 31%; api-šan ... hac ~ behind them 717-18; õi . . . hac m in her footsteps 3718-19, — 2. afterwards, then: ~, or u ~, or ~-ic, pursuing a narration, passim; introducing the apo- dosis after a subordinate clause 243-8, 27273, 4411-13, 914-5; ka vas-ic ... ~ -ic however much yet 9112-13; apäk
2983:pas [p's] watch, guard 65°. — OP *päga-, SW form of padra-, v. pahr. - MPrs p’sb’n ‘watchman, guardian’.
2984:pasčh ['HL-yh], with -c: pasé-c PHL-ye], adv. = pas: behind 577% (to be joined with the preceding sentence, v.s. v. hu- orón) ; hac ~ from behind 5724; 6 ~ back- wards 48°, rightabout 57? twice; pasé-c ka inasmuch as 6714. — pas + the ad- verbial ending -č (not identical with the abstract ending -eh, though confounded with it graphically), found also in pēšē [inser. pyšydy, SM passim] and others, v. S. v. padé.
2985:pasén [psyn'] ultimate, final: tan i ~, v. tan.
=== HUB ===
1199:274. Zu pas *Wache, Nachtwache' vgl. Nr. 341: pahra^
1426:phi. pasindUan Viesein Bdh. 26, 10 kann sehr wohl
1481:341. Np. pahra = pas Nr. 274. Bal. pahar =^ afgh.
4540:von arm. kerpas 'feines Linnen mit np. kirpas^ arab. kirhas
6283:gr. xaAo770()ioi^, arm. kalapar. Aber kirpas *ein femes 6e-
6284:webe' = arm. kerpas *feines Linnen', gr. auQnaooq, skr. kar-
6290:H. 696; supurdan 'anvertrauen H. 697; sipas Dank, Lob'
6763:phi. pasincitati, ap. 3. pr. *patisin6ataiy (s. oben p. 42);
7252:nach pidar u. s. w.) = ap. pud^a-; pas 'Wache', phi. pOs
7826:Hinter s ist ein Laut abgefallen in pas hinter = ap.
8115:kascit, ap. kasciy, Vgl. pas *hinter = zd. pasha {paskCU),
8471:{= skr. ^makaga- oder '^makaska-, vgl. np. pas = ap. pasa
9062:skr. tapas *Hitze, Gluth*)? Das Verhaltniss dieser Formen
10529:Arjrpas 130, 178.
10636:pas 36, 204.
```


## [2026-09-04T22:47:03.578Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7824,7830p' HUB.txt; echo \"---8113\"; sed -n '8113,8118p' HUB.txt; echo \"---8469\"; sed -n '8468,8474p' HUB.txt; echo \"--- page for line 8115\"; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8').read()\nlines=t.split('\\n')\nimport bisect\n# find leaf index for a line number\npos=0\nleaves=[]\nfor i,l in enumerate(lines):\n    if '\\f' in l: leaves.append(i)\nfor target in (7826,8115,8471,10636):\n    n=bisect.bisect_left(leaves,target)\n    print(target,'leaf',n)\nEOF"
}
```


### [2026-09-04T22:47:05.573Z] TOOL RESULT

```
'neidet* (oben p. 13) ; jask H. 421 ist unsicher, ebenso sikar
H. 742, oben p. 76.
Hinter s ist ein Laut abgefallen in pas hinter = ap.
pasa, vgl. zd. pasca, paskdt; kas 'Jemand', zd. kascii, ap.
kasciy-, Vgl. § 117.
Idg. rs = ap. rs siehe Kap. 29; idg. ps = ap, fs,
idg. ks =^ ap. xs, idg. kh ^= ap, s siehe Kap. 23; idg.
---8113
'Rettich' bei Rosen, Np. Sprachf. p. 36).
Geschwunden ist c vielleicht in kas *jemand' = zd.
kascit, ap. kasciy, Vgl. pas *hinter = zd. pasha {paskCU),
dem aber schon im Ap. pasa (nicht *pasca u. dgl.) gegen-
iibersteht.
Ueber anl. eg = ap. sg = np. S siehe Kap. 23.
---8469
Ic^yu.
Unklar ist das Verhaltniss von np. magas 'Fliege* =
phi. makas Gl. and Ind. 215, bal. makask = ap. ^makasa-
{= skr. ^makaga- oder '^makaska-, vgl. np. pas = ap. pasa
'hinter : zd. paskat?) zu afgh. mac^) = iran. ^maika- (oben
p. 98) und zd. *max$i, gen. maxsya, skr. maksa-, maksikil-,
Vielleicht ist arisch ^makaga- neben ^makga- anzusetzen.
--- page for line 8115
7826 leaf 222
8115 leaf 229
8471 leaf 239
10636 leaf 288
```


## [2026-09-04T22:47:14.551Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['HUB','PHD','NYB','BRT','KNT','SKT','WEB','LKT','AFM','PLA','TAD','ARB','AFA','SYN','WLD','LEW','LAT','RCH','HJB','DEV','PHN']:\n    v=d.get(k) or {}\n    print(k,'|',v.get('page_offset'))\n\""
}
```


### [2026-09-04T22:47:16.724Z] TOOL RESULT

```
HUB | leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
PHD | leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
NYB | Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
BRT | Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
KNT | leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
SKT | leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
WEB | not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
LKT | leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
AFM | 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image
PLA | 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
TAD | 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image
ARB | None
AFA | leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
SYN | leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
WLD | Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
LEW | 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
LAT | leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
RCH | leaf ~= printed + 93..94 (e.g. leaf 336 = p.242, leaf 587 = p.494); weakly detected, verify by grepping the page number. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
HJB | leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
DEV | leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
PHN | leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


## [2026-09-04T22:47:24.943Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Ya‘aqobh\\|Ya'aqobh\\|Yaaqobh\\|Jacob,\" KLN_1966.txt | head -10"
}
```


### [2026-09-04T22:47:25.002Z] TOOL RESULT

```
20116:Jacksonia,  n.,  a  genus  of  plants  of  the  pea  family (bot.)  —  Named  after  the  English  botanist George  Jackson.  For  the  ending  see  suff.  -ia. Jacob,  1)  masc.  PN.;  2)  in  the  Bible,  one  of  the patriarchs,  son  of  Isaac  and  Rebecca  and  father of  the  founders  of  the  twelve  tribes.  —  Late  L. Jacdbus,  fr.  Gk.  ’laxcojioc,  fr.  Heb.  Ya'dqohh, lit.  ‘one  that  takes  by  the  heel’,  a  derivative  of ‘aqfbh,  ‘heel’,  whence  ‘aqabh,  ‘he  followed  at the  heel,  he  overreached,  circumvented’,  whi  1 is  rel.  to  Aram,  ‘iqbi,  Akkad,  iqbu,  ‘heel;  trace, mark’,  Arab,  ‘dqib,  ‘heel’,  ‘iqhah,  ‘mark,  trace, sign’,  ‘aqaba,  ‘he  followed  (at  the  heel),  suc¬ ceeded’.  Cp.  Jack,  jack,  ‘sleeveless  coat’,  Jaco¬ bin,  jacobus,  jacquery,  jakes,  James.
20119:Jacobite,  n.,  an  adherent  of  James  II  after  his  ab¬ dication  (English  hist.)  —  Formed  with  subst. suff.  -ite  fr.  Late  L.  Jacdbus,  ‘Jacob,  James’.  For the  etymology  of  the  name  see  Jacob.  Cp.  next word.
```


## [2026-09-04T22:47:36.451Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8').read()\nlines=t.split('\\n')\nleaf=0; \nfor i,l in enumerate(lines,1):\n    if i in (20116,20119,13881,13882): print('line',i,'-> leaf',leaf)\n    leaf += l.count('\\f')\nEOF"
}
```


### [2026-09-04T22:47:38.376Z] TOOL RESULT

```
line 13881 -> leaf 300
line 13882 -> leaf 300
line 20116 -> leaf 444
line 20119 -> leaf 445
```


## [2026-09-04T22:47:49.008Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8').read()\npg=t.split('\\f')\nfor i in (422,423,424):\n    print('=== leaf',i,'===', pg[i][:200].replace('\\n',' | '))\nEOF\necho \"=== 1971 ===\"\ngrep -n \"Jacob,  1)  masc\\|Jacob, 1) masc\" KLN_1971.txt | head"
}
```


### [2026-09-04T22:47:50.844Z] TOOL RESULT

```
=== leaf 422 === dj.,  obligatory.  —  L.  incumbens,  gen. -entis,  pres.  part,  of  incumbere,  ‘to  lie  upon, apply  oneself  to’,  fr.  in-,  ‘in’,  and  -cumbere  (found only  in  compounds),  ‘to  lie’.  See  
=== leaf 423 === nt’,  esp.  ‘appointment  of  tax’,  fr.  indictus, pp.  of  indicere,  ‘to  declare,  appoint’,  fr.  in-,  ‘in’, and  dicere,  ‘to  say’.  See  diction  and  -ion  and  cp. prec.  word. | Indies,  n. 
=== leaf 424 === . word  and  -ion. | indivisible, adj. — LateL.  indivisibilis,  ‘indivisible’, fr.  in-,  ‘not’,  and  divisibilis.  See  divisible. Derivatives:  indivisible,  n.,  indivisibil-ity,  n.,  in- divisibl
=== 1971 ===
127974:Jacob, 1) masc. PN. ; 2) in the Bible , one of the
```


## [2026-09-04T22:47:56.035Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '127960,127990p' KLN_1971.txt; echo \"=== find nearest page numbers ===\"; awk 'NR>=127700 && NR<=128100 && /^[0-9]{3,4}$/ {print NR\": \"$0}' KLN_1971.txt | head"
}
```


### [2026-09-04T22:47:57.833Z] TOOL RESULT

```
chakazi copal , fr. Zanzibar chakazi, chakazzi. 
jackdaw, n. — Compounded of jack, ‘male of 
animals’, and daw. 

jacket, n. — OF. jaquet (F. jaquette ), dimin. of 
jaque. See jack, ‘a sleeveless coat’, and -et. 
jack rabbit, a long eared American hare. — 
Short for jackass rabbit; so called in allusion 
to its long ears. Cp. its earlier names mule-eared 
rabbity mule rabbit . 

Jacksonia, n., a genus of plants of the pea family 
(bot.) — Named after the English botanist 
George Jackson . For the ending see suff. -la. 
Jacob, 1) masc. PN. ; 2) in the Bible , one of the 
patriarchs, son of Isaac and Rebecca and father 




of the founders of the twelve tribes. — Late L. 
Jacobus, fr. Gk. ’Idbcmpoq, fr. Heb. Ya'dqSbh, 
lit. ‘one that takes by the heel’, a derivative of 
‘ dqSbh , ‘heel’, whence ‘ aqabh , ‘he followed at 
the heel, he overreached, circumvented’, whirl 
is rel. to Aram. Uqbd, Akkad, iqbu, ‘heel; trace, 
mark’, Arab. * dqib , ‘heel’, ‘ iqba h , ‘mark, trace, 
sign’, l dqaba , ‘he followed (at the heel), suc- 
ceeded’. Cp. Jack, jack, ‘sleeveless coat’. Jaco- 
bin, jacobus, jacquery, jakes, James. 

=== find nearest page numbers ===
```


## [2026-09-04T22:48:01.777Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1971.txt',encoding='utf-8').read()\nlines=t.split('\\n')\nleaf=0\nfor i,l in enumerate(lines,1):\n    if i==127974: print('line 127974 leaf',leaf); break\n    leaf+=l.count('\\f')\npg=t.split('\\f')\nprint(len(pg))\nprint(repr(pg[leaf][:150]))\nprint(repr(pg[leaf+1][:150]))\nEOF"
}
```


### [2026-09-04T22:48:03.561Z] TOOL RESULT

```
Exit code 1
line 127974 leaf 0
1
"Klein’s Comprehensive \nEtymological Dictionary \nof the English Language \n\n\n\nUNABRIDGED ONL' r VOLU\\1E EDITION \n\n\n\nELSEVIER \n\n\n\n\nA COMPREHENSIVE ETYMOL"
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
IndexError: list index out of range
```


## [2026-09-04T22:48:18.051Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8').read()\npg=t.split('\\f')\nprint('leaves',len(pg))\nimport re\nfor i in (430,435,440,441,442,443,446,450,455,460):\n    print(i, pg[i][:90].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T22:48:20.157Z] TOOL RESULT

```
leaves 903
430 vative:  insinuat-ing,  adj.,  insinuat-ing-ly, adv.,  insinuation  (q.v.).  insinuat-ive,
435 t’,  and  tolerabilis.  See  tolerable. Derivatives:  intolerable-ness,n.,  intolerabl-y, 
440 te,  ‘to  anger’,  and -able.  Derivatives :  irritabl-y,  adv.,  irritabil-ity,  n. irrit
441 timulate,  stir  up,  provoke’, prob.  freq.  of  *ir-ri-re,  ‘to  stir  up,  excite’,  fr
442 ains  in the  hip’,  compounded  of  Gk.  EoxEov,  ‘hipjoint’, and  itXyo ?,  ‘pain’.  See
443   represents  1)  OF. -aison  (fr.  L.  ationem,  fr.  -atus,  pp.  suff.  of  verbs in  -
446 ��), and the  adj.  janitor-ial. Janizary,  also  Janissary,  n.  —  Fr.  janissaire,  fr.
450 o  gau- dere,  ‘to  rejoice'.  See  gaud  and  cp.  enjoy.  Cp. also  feu  de  joie,  rejo
455 ‘stalk,  blade’, Lett,  zeiju,  ziet,  ‘to  rise’  (said  of  flowers;  also fig.)  See  c
460 pertaining  to,  or  formed  with, the  lips  and  teeth.  —  Compounded  of  labio-  and
```


## [2026-09-04T22:48:37.508Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8').read()\npg=t.split('\\f')\nfor i in range(436,452):\n    nums=re.findall(r'\\b(8[0-9]{2}|9[0-9]{2})\\b', pg[i][:400]+pg[i][-400:])\n    print(i, nums, pg[i][:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T22:48:39.753Z] TOOL RESULT

```
436 []   L.  inundans,  gen. -antis,  pres.  part,  of  inundare.  
437 []   -ory fr.  L.  invocatus,  pp.  of  invocare.  See  invoke,
438 []  —  ModL.,  fr.  Gk.  eEpeauovr),  ‘a wreath  of  olive  wou
439 [] e,  adj.  —  Formed  with  suff.  -ive  fr.  L. irrigatus,  
440 [] te,  ‘to  anger’,  and -able.  Derivatives :  irritabl-y,  a
441 [] timulate,  stir  up,  provoke’, prob.  freq.  of  *ir-ri-re,
442 [] ains  in the  hip’,  compounded  of  Gk.  EoxEov,  ‘hipjoint
443 []   represents  1)  OF. -aison  (fr.  L.  ationem,  fr.  -atus
444 [] the  true  stinkhorns  (bot.)  —  ModL.  See  prec. word. -i
445 []  —  Late  L. Jacdbus,  fr.  Gk.  ’laxcojioc,  fr.  Heb.  Ya'
446 [] ��), and the  adj.  janitor-ial. Janizary,  also  Janissary,
447 [] its  horsemen, jenneting,  n.,  a  kind  of  early  apple.  
448 [] The  Foreign Vocabulary  of  the  Qur’an,  pp.  101-102. jho
449 [] s’,  yuktdh, ‘harnessed’,  Gk.  ^euyvuvai,  ‘to  yoke,  har¬
450 [] o  gau- dere,  ‘to  rejoice'.  See  gaud  and  cp.  enjoy.  
451 []  ‘rose’, and  ab,  ‘water’.  See  rose  and  abdest. Julia,
```


## [2026-09-04T22:49:05.494Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8').read()\npg=t.split('\\f')\nfor i,p in enumerate(pg):\n    if 'cherub,  n.' in p or 'cherub, n.' in p:\n        print('cherub leaf',i); break\nfor i,p in enumerate(pg):\n    if 'paradise,  n.' in p:\n        print('paradise leaf',i); break\nEOF"
}
```


### [2026-09-04T22:49:07.342Z] TOOL RESULT

```
cherub leaf 155
paradise leaf 600
```


## [2026-09-04T22:49:18.122Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8').read()\npg=t.split('\\f')\nfound=[]\nfor i,p in enumerate(pg):\n    m=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', p)\n    if m: found.append((i,m))\nprint(len(found))\nfor x in found[:40]: print(x)\nEOF"
}
```


### [2026-09-04T22:49:19.988Z] TOOL RESULT

```
644
(0, ['1966'])
(6, ['37'])
(17, ['10', '11'])
(18, ['12', '13'])
(19, ['14', '15'])
(20, ['16'])
(21, ['18', '19'])
(22, ['20'])
(23, ['22'])
(24, ['23', '24'])
(25, ['25', '26'])
(26, ['27', '28'])
(27, ['29', '30'])
(29, ['04', '35'])
(31, ['36', '37'])
(32, ['39'])
(33, ['40', '41'])
(34, ['42', '43'])
(35, ['44', '45'])
(36, ['46'])
(37, ['49'])
(38, ['50', '51'])
(39, ['52', '53'])
(40, ['54', '55'])
(42, ['58', '59'])
(43, ['60', '61'])
(44, ['62', '63'])
(45, ['64', '65'])
(46, ['66'])
(47, ['67', '68'])
(48, ['69', '70', '71'])
(49, ['72', '73'])
(50, ['74', '75'])
(51, ['76'])
(52, ['77', '78', '79'])
(54, ['80', '81'])
(55, ['82', '83', '84'])
(56, ['85'])
(57, ['86', '87'])
(60, ['92', '93'])
```


## [2026-09-04T22:49:25.519Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8').read()\npg=t.split('\\f')\nfor i in range(438,452):\n    m=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', pg[i])\n    print(i, m)\nEOF"
}
```


### [2026-09-04T22:49:27.408Z] TOOL RESULT

```
438 ['815']
439 []
440 []
441 ['816', '817']
442 []
443 ['820', '821']
444 ['822']
445 ['824', '825']
446 ['826', '827']
447 ['828', '829']
448 ['830', '831']
449 ['832', '833']
450 ['834', '835']
451 ['636', '837']
```


## [2026-09-04T22:49:39.804Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8').read()\npg=t.split('\\f')\nimport re\ns=pg[443]+pg[444]+pg[445]\nfor m in re.finditer(r'(Jack,|jack,|James,|Jacobin|jacquerie|jaques|Jaques)', s):\n    print('...',s[max(0,m.start()-20):m.start()+700].replace('\\n',' '))\n    print('-----')\nEOF"
}
```


### [2026-09-04T22:49:41.540Z] TOOL RESULT

```
... i;.  See  hyacinth. Jack,  masc.  PN.  —  Familiar  form  of  John,  but derived  fr.  OF.  Jaques  (F.  Jacques),  fr.  Late  L. Jacdbus,  for  earlier  Jacobus,  fr.  Gk.  fr,  Heb. YadqSbh,  ‘Jacob’.  See  Jacob  and  cp.  next  word, jack,  n.,  1)  fellow;  2)  knave  in  playing-cards; 3)  the  male  of  certain  animals;  4)  a  small  flag; 5)  the  name  of  various  machines,  vessels  and devices.  —  Fr.  prec.  word.  For  the  use  of  proper names  to  form  names  of  vessels  cp.  jeroboam, toby. jack,  n.,  1)  a  sleeveless  coat;  2)  a  vessel  for  liquor. —  OF.  jaque,  ‘sleeveless  coat’,  fr.  Jacques, ‘Jack’,  a  nickname  given  to  the  French  peasant in  the  14th  century,  for  
-----
...  derived  fr.  OF.  Jaques  (F.  Jacques),  fr.  Late  L. Jacdbus,  for  earlier  Jacobus,  fr.  Gk.  fr,  Heb. YadqSbh,  ‘Jacob’.  See  Jacob  and  cp.  next  word, jack,  n.,  1)  fellow;  2)  knave  in  playing-cards; 3)  the  male  of  certain  animals;  4)  a  small  flag; 5)  the  name  of  various  machines,  vessels  and devices.  —  Fr.  prec.  word.  For  the  use  of  proper names  to  form  names  of  vessels  cp.  jeroboam, toby. jack,  n.,  1)  a  sleeveless  coat;  2)  a  vessel  for  liquor. —  OF.  jaque,  ‘sleeveless  coat’,  fr.  Jacques, ‘Jack’,  a  nickname  given  to  the  French  peasant in  the  14th  century,  for  this  kind  of  garment was  used  especially  by  the  peasants  of  th
-----
... d  cp.  next  word, jack,  n.,  1)  fellow;  2)  knave  in  playing-cards; 3)  the  male  of  certain  animals;  4)  a  small  flag; 5)  the  name  of  various  machines,  vessels  and devices.  —  Fr.  prec.  word.  For  the  use  of  proper names  to  form  names  of  vessels  cp.  jeroboam, toby. jack,  n.,  1)  a  sleeveless  coat;  2)  a  vessel  for  liquor. —  OF.  jaque,  ‘sleeveless  coat’,  fr.  Jacques, ‘Jack’,  a  nickname  given  to  the  French  peasant in  the  14th  century,  for  this  kind  of  garment was  used  especially  by  the  peasants  of  that  era. See  Jack  and  cp.  Bloch-Wartburg,  DELF., p,  333  s.v.  jaquette.  Cp.  also  jacket.  For  sense development  cp.  jacquerie, jack, 
-----
... p.  jeroboam, toby. jack,  n.,  1)  a  sleeveless  coat;  2)  a  vessel  for  liquor. —  OF.  jaque,  ‘sleeveless  coat’,  fr.  Jacques, ‘Jack’,  a  nickname  given  to  the  French  peasant in  the  14th  century,  for  this  kind  of  garment was  used  especially  by  the  peasants  of  that  era. See  Jack  and  cp.  Bloch-Wartburg,  DELF., p,  333  s.v.  jaquette.  Cp.  also  jacket.  For  sense development  cp.  jacquerie, jack,  n.,  an  East  Indian  tree  ( Artocarpus  inte- grifoiia).  —  Port,  jaca,  fr.  Malayalam  chakka, lit.  ‘something  round’,  fr.  OI.  cakrah,  ‘wheel, circle’,  which  is  cogn.  with  Gk.  y.bw'koq,  ‘ring, circle’.  See  cycle  and  words  there  referred  to and  cp.  esp
-----
... e development  cp.  jacquerie, jack,  n.,  an  East  Indian  tree  ( Artocarpus  inte- grifoiia).  —  Port,  jaca,  fr.  Malayalam  chakka, lit.  ‘something  round’,  fr.  OI.  cakrah,  ‘wheel, circle’,  which  is  cogn.  with  Gk.  y.bw'koq,  ‘ring, circle’.  See  cycle  and  words  there  referred  to and  cp.  esp.  chukker,  hackery, jackal,  n.  —  Turk,  chagal,  fr.  Pers.  shaghal,  fr. OI.  srgaldh,  lit.  ‘the  howler’, jackanapes,  n.,  1)  a  monkey  (archaic);  2)  an  im¬ pertinent,  conceited  fellow,  a  coxcomb.  —  Fr. Jack  a  Napes  =  Jack  o' Napes,  Jack  of  Napes,  = ‘a  monkey  from  Naples  (in  Italy)’, jackaroo,  n.,  a  new  apprentice  on  a  sheep  farm in  Australia  (slang).  —
-----
... nt  cp.  jacquerie, jack,  n.,  an  East  Indian  tree  ( Artocarpus  inte- grifoiia).  —  Port,  jaca,  fr.  Malayalam  chakka, lit.  ‘something  round’,  fr.  OI.  cakrah,  ‘wheel, circle’,  which  is  cogn.  with  Gk.  y.bw'koq,  ‘ring, circle’.  See  cycle  and  words  there  referred  to and  cp.  esp.  chukker,  hackery, jackal,  n.  —  Turk,  chagal,  fr.  Pers.  shaghal,  fr. OI.  srgaldh,  lit.  ‘the  howler’, jackanapes,  n.,  1)  a  monkey  (archaic);  2)  an  im¬ pertinent,  conceited  fellow,  a  coxcomb.  —  Fr. Jack  a  Napes  =  Jack  o' Napes,  Jack  of  Napes,  = ‘a  monkey  from  Naples  (in  Italy)’, jackaroo,  n.,  a  new  apprentice  on  a  sheep  farm in  Australia  (slang).  —  A  blend 
-----
...  —  Compounded  of  jack, ‘male  of  animals’,  and  ass. Derivative:  jackass,  intr.  v.,  to  ride  a  jackass, jackass  copal,  Zanzibar  copal.  —  Corruption  of chakazi  copal,  fr.  Zanzibar  chakazi,  chakazzi. jackdaw,  n.  —  Compounded  of  jack,  ‘male  of animals’,  and  daw. jacket,  n.  —  OF.  jaquet  (F.  jaquette),  dimin.  of jaque.  See  jack,  ‘a  sleeveless  coat’,  and  -et. jack  rabbit,  a  long  eared  American  hare.  — Short  for  jackass  rabbit;  so  called  in  allusion to  its  long  ears.  Cp.  its  earlier  names  mule-eared rabbit,  mule  rabbit. Jacksonia,  n.,  a  genus  of  plants  of  the  pea  family (bot.)  —  Named  after  the  English  botanist George  Jackson.  For  
-----
...  —  Compounded  of  jack,  ‘male  of animals’,  and  daw. jacket,  n.  —  OF.  jaquet  (F.  jaquette),  dimin.  of jaque.  See  jack,  ‘a  sleeveless  coat’,  and  -et. jack  rabbit,  a  long  eared  American  hare.  — Short  for  jackass  rabbit;  so  called  in  allusion to  its  long  ears.  Cp.  its  earlier  names  mule-eared rabbit,  mule  rabbit. Jacksonia,  n.,  a  genus  of  plants  of  the  pea  family (bot.)  —  Named  after  the  English  botanist George  Jackson.  For  the  ending  see  suff.  -ia. Jacob,  1)  masc.  PN.;  2)  in  the  Bible,  one  of  the patriarchs,  son  of  Isaac  and  Rebecca  and  father of  the  founders  of  the  twelve  tribes.  —  Late  L. Jacdbus,  fr.  Gk.  ’laxcojioc, 
-----
... n.  of jaque.  See  jack,  ‘a  sleeveless  coat’,  and  -et. jack  rabbit,  a  long  eared  American  hare.  — Short  for  jackass  rabbit;  so  called  in  allusion to  its  long  ears.  Cp.  its  earlier  names  mule-eared rabbit,  mule  rabbit. Jacksonia,  n.,  a  genus  of  plants  of  the  pea  family (bot.)  —  Named  after  the  English  botanist George  Jackson.  For  the  ending  see  suff.  -ia. Jacob,  1)  masc.  PN.;  2)  in  the  Bible,  one  of  the patriarchs,  son  of  Isaac  and  Rebecca  and  father of  the  founders  of  the  twelve  tribes.  —  Late  L. Jacdbus,  fr.  Gk.  ’laxcojioc,  fr.  Heb.  Ya'dqohh, lit.  ‘one  that  takes  by  the  heel’,  a  derivative  of ‘aqfbh,  ‘heel’,  whence  
-----
... suc¬ ceeded’.  Cp.  Jack,  jack,  ‘sleeveless  coat’,  Jaco¬ bin,  jacobus,  jacquery,  jakes,  James. Jacobin,  n.,  1)  a  Dominican  friar;  2)  a  member  of the  political  club  of  the  Jacobins.  —  F.,  fr.  ML. Jacdbinus,  fr.  L.  Jacdbus  [see  Jacob  and  -ine (representing  L.  -inus)].  The  Dominican  friars are  so  called  because  their  first  convent  in  Paris was  established  in  the  rue  St.  Jacques  (=  St. James  Street).  As  a  political  term,  the  word Jacobin  refers  to  the  fact  that  (after  Oct.  6,  1 789) the  club  of  the  Jacobins  used  to  meet  in  the monastery  of  the  Jacobins  in  the  rue  St. Honore. Derivatives:  Jacobin,  Jacobin-ic,  Jacobin-ic-al, adjs
-----
... eded’.  Cp.  Jack,  jack,  ‘sleeveless  coat’,  Jaco¬ bin,  jacobus,  jacquery,  jakes,  James. Jacobin,  n.,  1)  a  Dominican  friar;  2)  a  member  of the  political  club  of  the  Jacobins.  —  F.,  fr.  ML. Jacdbinus,  fr.  L.  Jacdbus  [see  Jacob  and  -ine (representing  L.  -inus)].  The  Dominican  friars are  so  called  because  their  first  convent  in  Paris was  established  in  the  rue  St.  Jacques  (=  St. James  Street).  As  a  political  term,  the  word Jacobin  refers  to  the  fact  that  (after  Oct.  6,  1 789) the  club  of  the  Jacobins  used  to  meet  in  the monastery  of  the  Jacobins  in  the  rue  St. Honore. Derivatives:  Jacobin,  Jacobin-ic,  Jacobin-ic-al, adjs.,  Jac
-----
... ry,  jakes,  James. Jacobin,  n.,  1)  a  Dominican  friar;  2)  a  member  of the  political  club  of  the  Jacobins.  —  F.,  fr.  ML. Jacdbinus,  fr.  L.  Jacdbus  [see  Jacob  and  -ine (representing  L.  -inus)].  The  Dominican  friars are  so  called  because  their  first  convent  in  Paris was  established  in  the  rue  St.  Jacques  (=  St. James  Street).  As  a  political  term,  the  word Jacobin  refers  to  the  fact  that  (after  Oct.  6,  1 789) the  club  of  the  Jacobins  used  to  meet  in  the monastery  of  the  Jacobins  in  the  rue  St. Honore. Derivatives:  Jacobin,  Jacobin-ic,  Jacobin-ic-al, adjs.,  Jacobin-ic-al-ly,  adv.,  Jacobin-ism,  n.,  Ja- cobin-ize,  tr.  v.,  Jacobin-
-----
... cal  club  of  the  Jacobins.  —  F.,  fr.  ML. Jacdbinus,  fr.  L.  Jacdbus  [see  Jacob  and  -ine (representing  L.  -inus)].  The  Dominican  friars are  so  called  because  their  first  convent  in  Paris was  established  in  the  rue  St.  Jacques  (=  St. James  Street).  As  a  political  term,  the  word Jacobin  refers  to  the  fact  that  (after  Oct.  6,  1 789) the  club  of  the  Jacobins  used  to  meet  in  the monastery  of  the  Jacobins  in  the  rue  St. Honore. Derivatives:  Jacobin,  Jacobin-ic,  Jacobin-ic-al, adjs.,  Jacobin-ic-al-ly,  adv.,  Jacobin-ism,  n.,  Ja- cobin-ize,  tr.  v.,  Jacobin-iz-ation,  n. jacobin,  n.,  a  kind  of  pigeon.  —  F.  jacobine,  fem. form  of  jacobi
-----
... l  term,  the  word Jacobin  refers  to  the  fact  that  (after  Oct.  6,  1 789) the  club  of  the  Jacobins  used  to  meet  in  the monastery  of  the  Jacobins  in  the  rue  St. Honore. Derivatives:  Jacobin,  Jacobin-ic,  Jacobin-ic-al, adjs.,  Jacobin-ic-al-ly,  adv.,  Jacobin-ism,  n.,  Ja- cobin-ize,  tr.  v.,  Jacobin-iz-ation,  n. jacobin,  n.,  a  kind  of  pigeon.  —  F.  jacobine,  fem. form  of  jacobin,  ‘Jacobin,  Dominican’ ;  so  called because  the  neck-feathers  resemble  a  monk's cowl. Jacobite,  n.,  an  adherent  of  James  II  after  his  ab¬ dication  (English  hist.)  —  Formed  with  subst. suff.  -ite  fr.  Late  L.  Jacdbus,  ‘Jacob,  James’.  For the  etymology  of  the  name 
-----
... the  club  of  the  Jacobins  used  to  meet  in  the monastery  of  the  Jacobins  in  the  rue  St. Honore. Derivatives:  Jacobin,  Jacobin-ic,  Jacobin-ic-al, adjs.,  Jacobin-ic-al-ly,  adv.,  Jacobin-ism,  n.,  Ja- cobin-ize,  tr.  v.,  Jacobin-iz-ation,  n. jacobin,  n.,  a  kind  of  pigeon.  —  F.  jacobine,  fem. form  of  jacobin,  ‘Jacobin,  Dominican’ ;  so  called because  the  neck-feathers  resemble  a  monk's cowl. Jacobite,  n.,  an  adherent  of  James  II  after  his  ab¬ dication  (English  hist.)  —  Formed  with  subst. suff.  -ite  fr.  Late  L.  Jacdbus,  ‘Jacob,  James’.  For the  etymology  of  the  name  see  Jacob.  Cp.  next word. Derivatives:  jacobit-icai,  adj.,  Jacobit-ism,  n. 
-----
... monastery  of  the  Jacobins  in  the  rue  St. Honore. Derivatives:  Jacobin,  Jacobin-ic,  Jacobin-ic-al, adjs.,  Jacobin-ic-al-ly,  adv.,  Jacobin-ism,  n.,  Ja- cobin-ize,  tr.  v.,  Jacobin-iz-ation,  n. jacobin,  n.,  a  kind  of  pigeon.  —  F.  jacobine,  fem. form  of  jacobin,  ‘Jacobin,  Dominican’ ;  so  called because  the  neck-feathers  resemble  a  monk's cowl. Jacobite,  n.,  an  adherent  of  James  II  after  his  ab¬ dication  (English  hist.)  —  Formed  with  subst. suff.  -ite  fr.  Late  L.  Jacdbus,  ‘Jacob,  James’.  For the  etymology  of  the  name  see  Jacob.  Cp.  next word. Derivatives:  jacobit-icai,  adj.,  Jacobit-ism,  n. jacobus jargon jacobus,  n.,  an  English  gold  coin.
-----
... nore. Derivatives:  Jacobin,  Jacobin-ic,  Jacobin-ic-al, adjs.,  Jacobin-ic-al-ly,  adv.,  Jacobin-ism,  n.,  Ja- cobin-ize,  tr.  v.,  Jacobin-iz-ation,  n. jacobin,  n.,  a  kind  of  pigeon.  —  F.  jacobine,  fem. form  of  jacobin,  ‘Jacobin,  Dominican’ ;  so  called because  the  neck-feathers  resemble  a  monk's cowl. Jacobite,  n.,  an  adherent  of  James  II  after  his  ab¬ dication  (English  hist.)  —  Formed  with  subst. suff.  -ite  fr.  Late  L.  Jacdbus,  ‘Jacob,  James’.  For the  etymology  of  the  name  see  Jacob.  Cp.  next word. Derivatives:  jacobit-icai,  adj.,  Jacobit-ism,  n. jacobus jargon jacobus,  n.,  an  English  gold  coin.  —  From  Latin Jacobus ,  ‘James’  (see  Jacob);
-----
... vatives:  Jacobin,  Jacobin-ic,  Jacobin-ic-al, adjs.,  Jacobin-ic-al-ly,  adv.,  Jacobin-ism,  n.,  Ja- cobin-ize,  tr.  v.,  Jacobin-iz-ation,  n. jacobin,  n.,  a  kind  of  pigeon.  —  F.  jacobine,  fem. form  of  jacobin,  ‘Jacobin,  Dominican’ ;  so  called because  the  neck-feathers  resemble  a  monk's cowl. Jacobite,  n.,  an  adherent  of  James  II  after  his  ab¬ dication  (English  hist.)  —  Formed  with  subst. suff.  -ite  fr.  Late  L.  Jacdbus,  ‘Jacob,  James’.  For the  etymology  of  the  name  see  Jacob.  Cp.  next word. Derivatives:  jacobit-icai,  adj.,  Jacobit-ism,  n. jacobus jargon jacobus,  n.,  an  English  gold  coin.  —  From  Latin Jacobus ,  ‘James’  (see  Jacob);  so  call
-----
... obin,  Jacobin-ic,  Jacobin-ic-al, adjs.,  Jacobin-ic-al-ly,  adv.,  Jacobin-ism,  n.,  Ja- cobin-ize,  tr.  v.,  Jacobin-iz-ation,  n. jacobin,  n.,  a  kind  of  pigeon.  —  F.  jacobine,  fem. form  of  jacobin,  ‘Jacobin,  Dominican’ ;  so  called because  the  neck-feathers  resemble  a  monk's cowl. Jacobite,  n.,  an  adherent  of  James  II  after  his  ab¬ dication  (English  hist.)  —  Formed  with  subst. suff.  -ite  fr.  Late  L.  Jacdbus,  ‘Jacob,  James’.  For the  etymology  of  the  name  see  Jacob.  Cp.  next word. Derivatives:  jacobit-icai,  adj.,  Jacobit-ism,  n. jacobus jargon jacobus,  n.,  an  English  gold  coin.  —  From  Latin Jacobus ,  ‘James’  (see  Jacob);  so  called  because s
-----
... obin-ic-al, adjs.,  Jacobin-ic-al-ly,  adv.,  Jacobin-ism,  n.,  Ja- cobin-ize,  tr.  v.,  Jacobin-iz-ation,  n. jacobin,  n.,  a  kind  of  pigeon.  —  F.  jacobine,  fem. form  of  jacobin,  ‘Jacobin,  Dominican’ ;  so  called because  the  neck-feathers  resemble  a  monk's cowl. Jacobite,  n.,  an  adherent  of  James  II  after  his  ab¬ dication  (English  hist.)  —  Formed  with  subst. suff.  -ite  fr.  Late  L.  Jacdbus,  ‘Jacob,  James’.  For the  etymology  of  the  name  see  Jacob.  Cp.  next word. Derivatives:  jacobit-icai,  adj.,  Jacobit-ism,  n. jacobus jargon jacobus,  n.,  an  English  gold  coin.  —  From  Latin Jacobus ,  ‘James’  (see  Jacob);  so  called  because struck  during  the  rei
-----
... n-ic-al-ly,  adv.,  Jacobin-ism,  n.,  Ja- cobin-ize,  tr.  v.,  Jacobin-iz-ation,  n. jacobin,  n.,  a  kind  of  pigeon.  —  F.  jacobine,  fem. form  of  jacobin,  ‘Jacobin,  Dominican’ ;  so  called because  the  neck-feathers  resemble  a  monk's cowl. Jacobite,  n.,  an  adherent  of  James  II  after  his  ab¬ dication  (English  hist.)  —  Formed  with  subst. suff.  -ite  fr.  Late  L.  Jacdbus,  ‘Jacob,  James’.  For the  etymology  of  the  name  see  Jacob.  Cp.  next word. Derivatives:  jacobit-icai,  adj.,  Jacobit-ism,  n. jacobus jargon jacobus,  n.,  an  English  gold  coin.  —  From  Latin Jacobus ,  ‘James’  (see  Jacob);  so  called  because struck  during  the  reign  of  James  I. jaconet,
-----
... bin-ize,  tr.  v.,  Jacobin-iz-ation,  n. jacobin,  n.,  a  kind  of  pigeon.  —  F.  jacobine,  fem. form  of  jacobin,  ‘Jacobin,  Dominican’ ;  so  called because  the  neck-feathers  resemble  a  monk's cowl. Jacobite,  n.,  an  adherent  of  James  II  after  his  ab¬ dication  (English  hist.)  —  Formed  with  subst. suff.  -ite  fr.  Late  L.  Jacdbus,  ‘Jacob,  James’.  For the  etymology  of  the  name  see  Jacob.  Cp.  next word. Derivatives:  jacobit-icai,  adj.,  Jacobit-ism,  n. jacobus jargon jacobus,  n.,  an  English  gold  coin.  —  From  Latin Jacobus ,  ‘James’  (see  Jacob);  so  called  because struck  during  the  reign  of  James  I. jaconet,  n.,  a  kind  of  soft  white  cotton  fabr
-----
... orm  of  jacobin,  ‘Jacobin,  Dominican’ ;  so  called because  the  neck-feathers  resemble  a  monk's cowl. Jacobite,  n.,  an  adherent  of  James  II  after  his  ab¬ dication  (English  hist.)  —  Formed  with  subst. suff.  -ite  fr.  Late  L.  Jacdbus,  ‘Jacob,  James’.  For the  etymology  of  the  name  see  Jacob.  Cp.  next word. Derivatives:  jacobit-icai,  adj.,  Jacobit-ism,  n. jacobus jargon jacobus,  n.,  an  English  gold  coin.  —  From  Latin Jacobus ,  ‘James’  (see  Jacob);  so  called  because struck  during  the  reign  of  James  I. jaconet,  n.,  a  kind  of  soft  white  cotton  fabric.  — Corruption  of  Jagannath,  name  of  a  town  in Bengal,  where  it  was  first  manufactured. 
-----
... cquard (1752-1834). jacquerie,  n.,  peasants’  revolt,  esp.  revolt  of  the French  peasants  in  1358.  —  F.  jacquerie,  prop, ‘rising  of  peasants’,  fr.  Jacques,  a  contemptuous name  given  by  the  nobles  to  the  French  peasant. See  jack,  ‘sleeveless  coat’  and  -ery. jactitation,  n.,  restlessness  (med.) ;  assertion  of  a false  claim  (law).  —  ML.  jactitatio,  gen.  -onis, fr .  jactitatus,  pp.  of  jactitare,  ‘to  toss  about’,  fr. L.  Jactus,  pp.  of  jacere,  ‘to  throw,  cast,  hurl’. See  jet,  ‘to  spirt  forth’,  and  -ation. jade,  n.,  a  kind  of  silicate.  —  F.  le  jade,  fr.  earlier I’ejade,  fr.  Sp.  ( piedra  de)  ijada,  ‘stone  for  curing pains  in  the  sid
-----
...   in  1358.  —  F.  jacquerie,  prop, ‘rising  of  peasants’,  fr.  Jacques,  a  contemptuous name  given  by  the  nobles  to  the  French  peasant. See  jack,  ‘sleeveless  coat’  and  -ery. jactitation,  n.,  restlessness  (med.) ;  assertion  of  a false  claim  (law).  —  ML.  jactitatio,  gen.  -onis, fr .  jactitatus,  pp.  of  jactitare,  ‘to  toss  about’,  fr. L.  Jactus,  pp.  of  jacere,  ‘to  throw,  cast,  hurl’. See  jet,  ‘to  spirt  forth’,  and  -ation. jade,  n.,  a  kind  of  silicate.  —  F.  le  jade,  fr.  earlier I’ejade,  fr.  Sp.  ( piedra  de)  ijada,  ‘stone  for  curing pains  in  the  side’,  a  derivative  of  L.  ilia,  ‘the flanks’.  See  iliac. jade,  n.,  a  worn-out  horse.  
-----
... ench  peasant. See  jack,  ‘sleeveless  coat’  and  -ery. jactitation,  n.,  restlessness  (med.) ;  assertion  of  a false  claim  (law).  —  ML.  jactitatio,  gen.  -onis, fr .  jactitatus,  pp.  of  jactitare,  ‘to  toss  about’,  fr. L.  Jactus,  pp.  of  jacere,  ‘to  throw,  cast,  hurl’. See  jet,  ‘to  spirt  forth’,  and  -ation. jade,  n.,  a  kind  of  silicate.  —  F.  le  jade,  fr.  earlier I’ejade,  fr.  Sp.  ( piedra  de)  ijada,  ‘stone  for  curing pains  in  the  side’,  a  derivative  of  L.  ilia,  ‘the flanks’.  See  iliac. jade,  n.,  a  worn-out  horse.  —  ME.,  fr.  OH.jalda, ‘mare’,  whence  also  dial.  Swed.  jcildd,  ‘mare’. Derivatives:  jade,  tr.  v.,  to  make  a  jade  of  (a 
-----
... pling  (1865-1936). James,  masc.  PN.  • —  Late  L.  Jacdmus,  altered fr.  Jacdbus.  See  Jacob  and  cp.  jimmy, jamesonite,  n.,  a  lead  antimony  sulfide  (mineral.) —  Named  after  Professor  Robert  Jameson  of Edinburgh  (1774-1854),  who  analyzed  it.  For the  ending  see  subst.  suff.  -ite. jampan,  also  jompon,  n.,  a  kind  of  sedan  (India). —  Bengali  jhapdn,  fr.  Hind,  japan,  jhappan,  fr. jSp,  ‘a  cover’. Jane,  fern.  PN.  —  F.  Jeanne,  fr.  OF.  Jehane,  fr. ML.  Johanna,  Joanna.  See  Joan  and  cp.  Jean, fern.  PN.  Cp.  also  demijohn,  jenny. Jane,  n.,  a  small  Genoese  coin.  —  OF.  Jane,  fr. ML.  Janua,  ‘Genoa’.  Cp.  L.  Genua,  whence  It. Genova,  F.  Genes. 
-----
```


## [2026-09-04T22:50:05.276Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FVQ_pages.txt',encoding='utf-8').read()\npg=t.split('\\f')\nprint(len(pg))\nfor i in (307,308,309):\n    print('=== leaf',i,'===')\n    print(pg[i][:2200])\nEOF"
}
```


### [2026-09-04T22:50:07.367Z] TOOL RESULT

```
335
=== leaf 307 ===
290 FOREIGN VOCABULARY OF THE QUR J AN
^2w (Yakya).
iii, 34 ; vi, 85 ; xix, 7, 13 ; xxi, 90.
John the Baptist.
Usually the Muslim authorities derive the name from the Arabic
verb of similar form, and say that John was so called because of his
quickening virtue, either in quickening the barrenness of his mother, or
in quickening the faith of his people. 1 Some felt that they were com-
>' ' ' '
mitted to an Arabic origin of the name by Sura xix, 8 <) Jf* J
> ' *
, which, however, as Marracci pointed out, 2 is merely
a misunderstanding of Lk. i, 61, and there were some (e.g. Baid. on iii,
34, and xix, 8) 3 who knew and admitted that it was a foreign name.
We may be sure that the name came into Arabic from some
Christian or Christianized source.
Sprenger, Leben, ii, 335, thought that perhaps it might have come
from the Sabians, for in the Mandaean books we find the name in the
form KTIN 1 * (Lidzbarski, Johannesbuch, ii, 73), but the probability
is that this form is due to Islamic influence. 4 ^
A more subtle theory is that it is a misreading for /^*-^ which
would be derived from the Syr. ^l*Q.a. 5 The primitive script had no
. & ** } X'O X"
vowel points, and ,g>* might have been read /4-*-=*^ as easily as /^-^^
This solution has much in its favour, and might be accepted were
it not for the fact that we have epigraphical evidence from N. Arabia
that in pre-Islamic times Christians in that area were using a form XTP,
probably derived from the Syriac. 7 Jaussen and Savignac found this
1 Tab. on iii, 34, and ath-Tha'labi, (?tVwfl. 262.
2 Refutationes, 435. So Sayous, 27, n. ; Palmer, Qoran, ii, 27, n. ; Pautz, Offen-
barung, 254.
3 So al-Khafaji, 215; al-'Ukbarl, Imld\ i, 88. Zam. halts between two opinions.
4 Noldeke, ZA, xxx, 159.
5 Noldeke noted that |3m\ from which .IxtCLfc was formed, can occur in a
hypochoristic form ^Xm 1 , and as a matter of fact ^T\T or Tll^ does occur in late
Jewish names, and Fraenkel, W ZKM, iv, 337, and Grimme, Mohammed, ii, 96, n. 8,
have thought that .^ could be derived from this. Barth, Der Islam, vi, 126, n., and
Mingana, Syrian Influence, 84, have rightly insisted, however, that the name is of
Christian not Jewish origin.
Barth, op. c
=== leaf 308 ===
FOREIGN VOCABULARY OP THE QUR ? AN 291
form KTP in a graffito at Al-'Ala, 1 and it is possibly found again
in another inscription from the same area. 2 It would thus seem that
Muhammad was using a form of the name already naturalized among
the northern Arabs, though there appears to be no trace of the name
in the early literature.
ii, 126-134 ; iii, 78 ; iv, 161 ; vi, 84 ; xi, 74 ; xii, 6, 38, 68 ; xix, 6,
50 ; xxi, 72 ; xxix, 26 ; xxxviii, 45.
Jacob.
He is never mentioned save in connection with some other member
of the Patriarchal group.
There were some who considered it as Arabic derived from
but in general it was recognized as a foreign word, cf. al-Jawallql, 155 ;
Zam. on xix, 57 ; Baid. on ii, 29 ; as-Suyutl, Muzhir, i, 138, 140 ;
al-Khaf aji, 215. Apparently it was known among the Arabs inpre-Islamic
days. 3
Tt may have come from the Ileb. SpIT 1 , though the fact that
Muhammad has got his relationship somewhat mixed 4 might argue
that he got the name from Christian sources, probably from the Syr.
tOQQL^, 5 which was the source of the name in the Manichaean frag-
ments (tSalemann, Manichaeische Studien, i, 86).
> A /. ^
<*~> j*j> ( Yayh uth ) .
Ixxi, 23.
Yaghuth.
It is said to have been an idol in the form of a lion, worshipped
among the people of Jurash and the Banu Madhhij. 6 It would thus
1 Mission archeologique, ii, 228. For the form TIT see Euting, Sin. Inschr.,
No. 585 ; CIS, ii, 1026.
2 Lidzbarski, Ephemeris, iii, 296, and cf. Horovitz, KU, 151, for an inscription
from Harnln. It is possible that a Jewish form ""IT occurs in the Elephantine papyri
(cf. Cowley, Aramaic, Papyri, No. 81, 1. 28), but the reading is not sure.
3 Cheikho, Naxraniya, 234 ; Horovitz, K U, 153. Horovitz plays with the idea
that it may have been a genuine old Arab name. Cf. JPN, 152.
4 xi, 74, on which see Hurgronjo, Verspreide Geschriften, i, 24.
6 Mingana, Syriac Influence, 82.
Ibn al-Kalbi, Kitab al-Amam, p. 10 ; Wellhausen, Reste, 19 if. ; Kyckmans,
Noms propres, i, 16.
=== leaf 309 ===
292 FOREIGN VOCABULARY OF THE QUR ? AN
appear to be of S. Arabian origin, and this is confirmed by the fact that
we find HiT~Dn in the Thamudic inscriptions, 1 and laovdo?
in Safaite 2 and Thamudic. 3
The name would seem to mean helper (Yaqut, Mu'jam, iv, 1022),
and the S. Arabian X^U means to help (cf. Ar. <*1> ; Heb.
Rossini, Glossarium, 215).
xxxvii, 146.
A gourd.
The word occurs in the Jonah story for the gourd tree which
Allah caused to grow up over the Prophet. The reference is obviously
to the Biblical story in Jonah iv, 6-11, and ^^ seems to be an
attempt to reproduce the IVp^j? of the Hebrew story. 4 The word was
apparently heard during an oral recitation of the story, and then
reproduced from memory in this garbled form.
^
!. (Yaqm).
iv, 156 ; xv, 99 ; xxvii, 22 ; Ivi, 95 ; Ixix, 51 ; Ixxiv, 48 ; cii, 5, 7.
Certain. ^ i
The simple verb sji ,j does not occur in the Qur'an, but we find ^AJ I
* ~ - I
ii, 3; v, 55, etc. ; ^LJuJ xxvii, 14 ; Ixxiv, 31, and the participles
(J*JA and ^LJu^*, besides ( ^^.
At first sight it seems clearly to be a borrowing, for there is no
Semitic V ]p\ and yet we find both ^JI^ and the verbal forms there-
from used in the oldest poetry, so it must have come into the language
1 D. H. Miiller, Epigraphische flenkmdler aus Arabian, p. 19 ; Littmann, Entziffer-
ung, 27, 32. It is possible that we have a parallel to the name in the Edomitish
proper name OTJ^ in Gen. xxxvi, 18.
2 DuBsaud et Macler, Voyage arcMol. an Safd, p. 77 ; Wuthnow, Die semitischen
Menschennamen, p. 56.
3 Ryckmans, JVoww propres, i, 174 ; Hess, Entzifferung, Nos. 46, 67.
4 So Torrey, Foundation, 52.
```


## [2026-09-04T22:50:17.262Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Ya‘aqob\\|Ya'aqob\\|Iakobos\\|'Ia*fo)/3os\\|Jacob\\b\" FSD_vol2.txt | head -20"
}
```


### [2026-09-04T22:50:17.326Z] TOOL RESULT

```
3312:mean  either  of  twQ  contraUictione.  ^   J>U-che',  1   du-Hhe';  2   du-f.*he^  Jacob  {1739?-V'»179S) .   An
4069:Dyce,  1   dais;  2   dye,  William (»/ul806-Vi4lS64).  A   Scot- tish historian  and  painter; frescoes  at  Buckingham  Pal- ace and  Osborne:  Jacob  and Rachel.
5307:bon  telephone  transmitter,  8torago»battery,  high»ro!ls,  E'dom-Ite,  1 1'clam-ait;  2   e'dom-Tt,  n.  A   descendant  of monolithic  concrete  dwellings,  etc.— Edison  effect  (TJfec.),  Edom  or  Esau,  brother  of  Jacob;  an  Idumean.— a   blackening  effect,  duo  to  convection  of  carbon,  observed  E'dom-lt"lsh,  a.  [lx,  35,
11908:e'sa'fl'.  L,  E-sa'vus,  1   i-se'- vua,  2   e^ia'vus.  3,  Bib,  The oldest  son  of  Isaac;  ancestor of  Edomites:  sold  his  birth- right to  Jacob,  Gen.  XXV.  25. IHeb.,  hairy;  rough.I
13702:4.  Seeking  the  conversion  of  sinners;  pertaining  to  the work  of  an  evangelist;  evangelistic;  as,  evangelical  la- bors or  preaching.  [   <   LL.  evangelicua,  <   Gr.  euangeli- Jeos,  <   euangelion;  see  evangel.)  ev"an-gcrict;  ev"an- gelT-cant;  ev"an-geJ'lckt.— Evangelical  Alliance,  an association  of  members  of  the  various  evangelical  denomi- nations to  promote  courtesy.  Intercourse,  and  cooperation among  evangelical  Christians.  It  was  organized  In  London In  1840,  and  now  has  branches  In  moat  Christian  churches. —   E.  Association,  a   denomination  originating  In  the  labors of  Jacob  Albright  among  the  Germans  of  eastern  Pennsyl- vania at  the  beginning  of  the  19th  century:  at  llmt  called Albrights.—  E.  Church.  1.  The  Prussian  United  Evangeli- cal Church,  formed  In  1817  by  the  fusion  of  Lutherans  and
16272:B-ze'ki-as,  n.  Bf6.  (Apocrypha),  2   Afnc.  xv,  22. E-ze'ki-el,  l   i-zI'ki-el;  2   e-zS'ki-SI,  n.  1.  A   mas- culine personal  name.  Zeke  (dim.).  D.  O.  He- .se'kl-ei,  1   hS-sS'ki-gl,  2   hg-se'ki-gl.  E-ze'kl-elfj F.  i"z€"chl"el',  1   6’z6'ki"el',  2   s’ze'trei';  Sp. E-ze"quI-el',  1   6-QiS"kr-<5l',  2   e-th§'M-eI'.  3. Bib.  A   Jewish  personal  name:  specif.,  one  of  the four  greater  prophets  (590  B.  C.).  3.  A   pro- phetical book  of  the  Old  Testament,  by  Ezekiel, who  was  one  of  the  prophets  of  the  captivity. It  foretells  the  destruction  of  Jerusalem  and prepares  the  Jews  for  the  restoration.  Com- pare Daniel;  Obadlah.  4.  SXoses  (Jacob) (>/islS44-a/ajl917),  an  American  sculptor  resid- ing latterly  at  Rome;  Religious  Liberty,  etc.  [Heb..  strength of  God.]
22947:hone.vsuckIe,  coral  (fidcllly). honeysuckle,  wild  (inconstancy). hop  (injustice). hornbeam  (ornament). horse-chestnut  (luxury). houseleek  (vivaeUy;  domestic  industry). houstoiUa  (contentment). hyaelnth,  blue  (constancy). hyacinth,  purple  (jealousy;  sorrow). hyacinth,  whits  (modest  lovelines.s) hydrangea  (a  boaster;  hcartlessness). hyssop  (cleanliness). lee-plant  (an  old  beau;  rejected), irli  (message;  my  compliments). iris,  German  (a/Iamc,-  I   burn). ivy  (fidelity;  friendship;  weddedlove). Jacob’s  ladder  (come  down).
22986:Jacob’s  ladder  (come  dmaa).  ,
28926:Gad',  re,  Bib.  1.  Jacob’s  seventh,  son;  also,  the  ti ,   scended  from  hln,  or  its  territory  E.  of  Jordan.  Gun. [Heb„  fortune,]  3.  A   Hebrew  prophet  and  adviser  of .   ,   J   CArore,  xxl,  S.  3.  The  god  of  fortune,  a   deity  hon :   . ,   Semitic  peoples:  possibly  identical  with  Jupiter. Gad'a-ba,  i   gad'e-ba;  2   gad'a-ba,  re.  A   Muiida  hang Southern  India,  belonging  to  the  Dravido-Munda spoken  by  the  Gadabas  of  Ganjam  and  Vizagapatii
34281:mainsail  or  foresail  wdien  the  middle  part  is  furled.  Gor-dl'l-dce,  l   gor-dol'i-dl;  2   gOr-dl'l-dg,  re.  pi.  Helminth. goose'winged",  1   gflsViod”;  2   goos'wingd',  a.  Naut.  A   family  of  nematode  worms  with  a   Imlr-llke  body,  mouth 1.  Having  a   goosewing  clew.  3.  In  fore«ana»aft  rigged  and  adoral  alimentary  canal  obsolete  In  maturity,  and  tall vessels,  having  the  mainsail  on  one  side  and  the  foresail  of  male  forked;  hairworms.—  got'dl-ld,  gor'dl-oid,  a. on  the  other,  so  as  to  sail  wing*and»wing.  Gor'dlu,  1   g§r'dm;  2   gSr'dln,  Jacob  M.  ('/il853-*/iil909).
36591:2.  Resembling  the  Greeks,  as  in  intellectual  keenness and  devotion  to  reason,  or  in  love  for  literary  and  artistic excellence  and  in  delicacy  of  taste;  also,  thoroughly versed  in  Greek  literatmre  and  antiqnitl^.—  Greek  archi- tecture, the  orders  developed  In  ancient  Greece.  For  the styles,  see  Cobinthian;  Doric;  Ionic.  See  also  lUus.  under CAPITAL,  and  plate  of  architecture.— G.  art,  the  art  de- veloped in  ancient  Greece.  It  included  architecture,  sculp- ture, painting,  detail  in  bronzes,  pottery,  and  vase-decora- tion, and  attained  its  apogee  in  the  Stli  century  B.  C.—  G. Church.  1.  The  Eastern  or  Oriental  Church  (officially,  the Holy  Oriental  Orthodox  Catholic  Apostolic  Church),  which finally  separated  from  the  Roman  or  WMtern  Church  In  the 11th  century,  chiefly  upon  doctrinal  and  liturgical  grounds. Its  chief  creed  Is  the  Nlcene-Goustantlnopolltan,  omitting the  FlUoque;  the  Byz.antlne  rite  is  followed  in  Its  services. The  principal  divisions  of  the  Greek  Church  are:  the Patriarchate  of  Constantinople  (covering  Turkey  in Europe  and  Asia  Minor,  and  governed  by  an  ecumenical patriarch,  who  enjoys  an  honorary  precedence  over  all others);  the  Patriarchate  of  AIe.Taadria  (covering  all Egypt):  the  Patriarchate  of  Antioch  (covering  SiTia); the  Patriarchate  of  Jerusalem  (extending  over  Balastine) ; the  Autocephalous  Church  of  Cyprus;  the  National Church  of  Russia  or  Russian  Church  (independent  since 1SS9,  and  governed  by  the  Holy  Synod);  the  Servian Church  In  Hungary  (organized  in  170.5):  the  Indepen- dentDlocc.se  of  Czernagora  (in  Montenegro,  extstlng  since 176,5):  the  Church  of  Sinai  (Independent  since  1782);  the Hellenic  or  Greek  Church  (independent  since  1850);  the Church  of  the  Vlaclis  (Independent  in  Hungary  since 1804);  the  Bulgarian  Church  (excommunicated  in  1872. and  considered  sehlsmatioal) :   the  Servian  Church  (organ- ized in  1879):  the  Roumanian  Church  (a  national  church since  1885).  Branches  of  these  various  churches  are  found In  almost  all  Western  countries.  2.  [Colloq.]  The  group of  non-Ijatln  churches.  Including  Nestorians,  Copts,  Jacob- ites. and  Armenians,  as  well  as  the  Greek  Orthodox  Church, and  more  correctly  known  as  the  Eastern  Church.— G.  em- broidery, a   design  in  needlework.  In  which  fancifully grouped  pieces  of  silk  or  colored  cloth  are  stitched  to  another fabric.— G.  gift,  a   treacherous  gift;  in  allusion  to  Vergil's line  (AS«rid  II,  49) ,   “   I   fear  the  Greeks  when  bringing  gifts." — G.  masonry,  a   style  of  masonry  In  which  each  alternate stone  is  of  the  full  thickness  of  the  wall.— G,  music,  music clilefly  melodic.  See  mode.— G.  philosophy,  the  various systems  and  schools  of  reflective  thinking  developed  among the  ancient  Greeks.  The  line  of  philosophical  development along  which  ail  Europe  has  moved  is  said  to  have  had  its origin  in  early  Greece,  because  her  thinkers  were  the  first  to separate  between  the  poetlco-rellglous  and  mythical  way  of explaining  the  universe  and  man's  experience  and  the  way which  employs  reason  In  the  investigation,  scientifically,  of "tlie  ultimate  bases  of  Knowledge  and  Being.”  While  all sohoohs  of  philosophy  flourished  to  a   greater  or  less  extent among  the  Greeks,  as  they  have  in  India,  Greek  philosophy bore  two  distinguishing  allied  characteristics;  these  were  re- gard for  beauty  of  form  in  thought  and  in  expression,  and great  freedom  on  the  one  hand  from  the  conventional,  and on  the  other  from  the  superstitious  and  the  monstrous. Without  taking  the  divisions  too  strictly,  three  great periods  may  be  distinguished  in  Greek  philosophy:  (1)  the pre-Soeratlc  period;  (2)  the  period  of  Socrates,  Plato,  and Aristotle;  and  (3)  the  post-Aristotelian  philosophy,  during which  stoicism,  epicureanism,  skeptlctsm,  and  eclecticism developed,  and  led  the  way  —   especially  the  last-named  — to  the  dominance  of  Neo-Platonism.— G.  point,  a   needle- made  lace  dating  from  the  fifteenth  century.— G.  rose,  the flower  campion.
37097:Bbhjamin  F.  Taylob  Rhymes  of  the  River  st.  1. Grimm,  1   grim:  3   grim,  n.  1.  Friedrich  Melchior,  Baron ff/itl72Z'-ts/x,i807),  a   German  writer,  diplomatist,  and critic.  3.  Jakob  Lndwig  Karl  (i/a785-»/»1863),  a   Ger- man philologist;  Deutsche  Grammatik  (with  hla  brother  Wil- helm Karl),  Deutsche  WUrterbuch,  and  Kindere  und  Haus- mdreften.  fairy  tale.  3.  Wilhelm  Karl  (*/«  17 8C-i»/u 1869), a   German  philologist;  brother  of  Jacob  Ludwig  Karl:  Die Deutsche  fleldensage  (with  his  brother),  the  WSrterbuch,  and MUTchen.— Grimm’s  law,  sec  under  iaw,  n.
39579:Hack'ert,  1   hak'ert;  2   hak'ert,  n.  The  name  of  several  hack'thorn",  1   hak'QiSrn';  2   hak'thorn’.  n.  The  horny brotiiens;  1.  Georg  Abraham  <1755-1805),  a   German  acacia  (Aeacfa  deiinens),  or  wait«a*bit  thorn,  which  some engraver.  3.  Jacob  Philipp  (»/ul737-‘/s8lS07).  a   Ger-  Sonth-Afrlcan  tribes  consider  sacred.  [<  hacki,  »„ + man  landscape-painter.  3.  Johann  Gottlieb  (1744-1773),  thohn.]
43657:Hel'mont,  1   hel'ment;  3   hei'mfint,  n.  1.  Jan  Baptlsta  van (1577-12 /3o1644),  a   Flemish  chemist,  pliyslologist,  and  vi- sionary. 2.  Segres  Jacob  van  (i/i7l6S3-syail726),  a   Flem- ish historical  painter.
44055:lienee  fo^r  HUrtl,  i   hens  ier  ward,  8   imne  for  w.trd,  aar.  Hen'le,  1   hen'ln;  3   hSn'le,  Jacob  (Vit)1809-Vnl8.S5).  AGer-  all  colors  from  single  worsted  yarn,  with  silk  mi.xtures  in  the
49006:,   a.  n-i-i-  rapher.  3.  Jacob  (‘2/25I69S-u/m17S0),  a   Dutch  engraver;
50605:Huys'mans",  I   ii.s'’mSn':  2   {is’’mafi',  n.  1.  Jacob  (1056?- 1096),  a   Flemish  portrait-painter  who  practised  In  En- gland. 3.  Jorls  Karl  (z/ilS/S-®/i2l907),  a   French  novelist of  the  ultrarealist  school,  who  la  hls  later  years  changed  to mysticism.
61767:son  of  Abraham  and  Sarah,  and  father  of  Esau  and  I'sa-mate,  1   al'sa-met;  2 1'sa-roat,  n.  A   salt  of  Isamlc  acid,  is/vhi-at'ie  i   i«i“in ii'ri  ntuo  ^   nr Jacob;  lived  about  ISOO  B.C.  Gcn._xxi,  3.  3.  Is.  It,  I''.sam''bert/,  I   r'zanW;  2   rsanW,  Francois
62198:Is'ra-cl,  1   iz'n-el;  2   5t§'ra-SI,  n,  1,  A   masculine  personal name.  F.  Is"ra"elMl8''ra''el'.  2!s''ra"6F;  G.  Is"ra-el', 1   Ts’ra-SF,  2   Is"ra-el';  L.  Is'ra-el.  3.  The  patriarch Jacob:  so  called  after  his  wrestling  with  the  angel  at  Pen- iel  (Ge7i.  xx.xii,  28).  3.  The  twelve  Israelitiah  tribes  un- til the  division  of  the  kingdom.  4.  The  northern  king- dom after  the  division.  5.  Those  who  returned  from the  Babylonian  captivity;  also,  their  descendants,  the Jews.
62205:region  below  the  Isothermal  layer,  ceases,  often  giving  place,  Is'ra-el-iie,  1   iz'n-el-ait;  2 1§  ra-el-It,  7t.  Bib.  J ohn  i,  47. in  the  lower  part  of  this  layer,  to  a   marked  rise  of  tempera-  A   doscend.ant  of  Israel  (or  Jacob) ;   Hebrew;  Jew;  especially
```


## [2026-09-04T22:50:24.505Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Ja'cob\\|Ja’cob\\|Jacobus\\|I-a'ko-bos\\|Ia-ko\" FSD_vol2.txt FSD_vol3.txt | head -20"
}
```


### [2026-09-04T22:50:24.560Z] TOOL RESULT

```
FSD_vol2.txt:46797:Horf,  Ihe'f;  2 h6k  Jacobus Hcndrlcus  van’t  (s/jo  1852-1911),  oOielnale)  of  the  parsley  family;  sulfurweed,  2-  The  may-
FSD_vol2.txt:62728:Jac.,  abbr.  Jacob:  Jacobus  (.lames),
FSD_vol2.txt:62777:A   com  of  small  vafue,  probably  a   farthing;  hence  money. 17.  [Old  Slang,]  (1)  (j-]  A   Jacobite.  (2)  An  iinprea.SMi seal,  t   <   OF.  Jacques,  Jacob  ( =   OF.  Jakemes,  James,  > E.  James),  <   LL.  Jacobus,  <   Gr.  lakdhos,  <   Heb. Ya’aqob,  lit.  supplanter,  <   ’&qab,  supplant.]
FSD_vol2.txt:62909:Dan.  Poi.  Sw.  Ja'kob,  1   yfl'kob,  2   ja'cob;  D.  G.  Ja'cob, 1   ja'kop,  2   ya'cOp;  F.  Ja"cob',  1   sa'kSb',  2   zha"c6b':  Hung. Ja'kob,  1   yq'kob,  2 ya'eOb;  It.  Gla-cob'be,  1   ja-kOb'bg,  2   ja- cQb'bg;  L.  Ja-co'bus,  1   je-kS'bia,  2   jn-cO'bfis;  Sp.  Ja-co'bo, 1   ha-kS'bo,  2   ha-e6'bo.  2.  See  Jambs.  3.  jB1&.  A   Hebrew  patri- arch;   secondson  of  Isaac;  progenitor  of  the  Israelites.  Gen.xxv, 26.  4.  A   Hungarian  adventurer;  instigated  French  crusade to  liberate  St.  Louis;  lived  about  1250.  5.  Henry  (1562?- 1626?),  an  English  Puritan:  pastor  of  first  Independent  or Congregational  church  in  England;  settled  in  Virginia.  6. Ludwig  Heinrich  von  (V2iil759-VrlS27),  a   German  pro- fessor of  political  economy  and  'writer.  7.  Violet,  pen- name  of  Mrs.  Arthur  Jacob,  an  English  novelist.  [Heb., supplanter.l
FSD_vol2.txt:62910:—   Ja'cob’ssla(l"der,  n.  Bot.  A   common  cultivated  orna- mental herb  (Polemonium  creruleum),  having  an  arrange- ment of  its  leaves  and  leaflets  suggestive  of  a   ladder.  See  al- so JACOB’S  LADDBn,  Under  ladder.—  American  Jacob’s* ladder,  a   herbaceous  perennial  (Polemonium  van-brvntix) with  stout  rootstock,  stem  1-3  feet  high,  leafy  to  the  top, bluish  eymose  flowers  in  clustered  panicles,  stamens  and style  projecting:  found  in  swampy  places  in  the  northeastern United  States.— Jacob’s -rod,  n.  [Prov.  Eng.)  The  yellow asphodel  (Asphodelus  luieus)  .—  Jacob’s  shell,  a   palmer’s  or pilgrim’s  shell:  the  emblem  of  St.  James  the  Grcater:‘worn by  pilgrims  to  his  shrine  at  Compostella  in  Spain.-  Jacob’s* staff,  n.  1.  A   pilgrim’s  staff.  2.  A   staff  to  support  a   sur- veyor's compass.  3.  An  Instrument  once  used  by  naviga- tors to  measure  altitudes.  4.  The  three  bright  stars  In  the belt  of  Orion.  5,  A   staff  concealing  a   dagger.— Jacob’s stone,  same  as  Lia  Fail.—  Jacob’s-sword,  n.  The  yellow iris.  See  under  YELLOW,  a.
FSD_vol2.txt:62915:Ja"cob-a-ba(l',  l   ju'kab-o-bucl';  2   j5'«ob-a-t)ad%  n.  A   town in  Upper  Sind,  Frontier  district,  Bombay,  British  Imila. |ac"o-i><ie'a,  1   jak'o-ul'a;  2   jiie’o-bs'a,  u.  Bat.  The  European ragwort  (Senecio  jacohxa),  [   <   LL.  Jacobus,  Jacob.]
FSD_vol2.txt:62923:Jacobus,’  see  jack'.]  Jac'o-blnef.
FSD_vol2.txt:62931:Jfac'o-blte,  n.  1.  Eng.  Hist.  An  adherent  of  James  II. after  bis  abdication  in  1688,  or  of  his  royal  line;  often, a   believer  in  the  divine  right  of  kings,  as  opposed  to  con- stitutional government.  2.  Ch.  Hist.  One  of  a   sect  of Syrian  Monophysites.  See  Jacobite  Church.  [   <   LL. JacobUa,  <   Jacobus;  see  jack'.]  —   Jacobite  Church  {Ch. Hist.),  a   sect  found  In  Syria,  Mesopotamia,  and  Kurdistan, called  after  its  founder.  Jacobus  Baradteus  (d,  578),  a   Greek monk  of  Constantinople,  consecrated  bishop  of  Edessa  In 541  or  543.  Their  doctrinal  peculiarity  is  Monophysltism, and  they  are  looked  on  as  heretics  by  the  Greek  Church. Their  head  Is  known  as  “   Patriarch  of  Antioch  and  all  the East,’’and  always  takes  the  name  of  Mar  Ignatius;  not  being allowed  by  the  Greek  monks  to  reside  at  Antioch,  he  makes his  home  at  Dlarbeklr  or  Mardln.  Under  him  as  first  of  the Metropolitans  Is  the  Maphrian,  who  is  generally  chosen  as his  successor.  The  sect  has  12  bishops,  and  numbers 80,000  members,  not  including  the  Shamslyeh. JTac'o-blt-ismj  1   jak'o-boit-izm;  2   jac'o-blt-ism  (xni), n.  The  tenets  of  the  English  J acobites,  or  of  the  Syrian sect  of  Jacobites.
FSD_vol2.txt:62932:Ja'cobs,  1   je'ksbz  or  {G.)  ya'kops;  2   jS'eoba  or  ((?.)  yii'kops, n.  1.  Friedrich  Christian  Wilhelm  ('o/cl7G4:-3/3olS47), a   German  scholar  and  writer.  2.  Joseph  (VsalSSI-VaolOlS), an  Australian  author  and  editor  In  England  and  the  United States:  historian,  folk-lorist,  and  archeologist;  The  Jews  of Angevin  England.  3.  Lucas,  see  Leyden,  Lucas  Van.  4. William  Wymark  (i>/al863-  ),  an  English  author  and
FSD_vol2.txt:62934:Ja'cobs-dal,  l   yS'kops-dal;  2   yii'cOps-dlil,  n.  1.  A   former  dis- trict in  Orange  Free  State,  South  Africa;  area,  1,313  sq.m.
FSD_vol2.txt:62935:2.  A   town  In  the  district,  near  the  Modder  river. Ja'cobs-Ite,  l   je'kebz-ait;  2   ia'cobs-lt,  n.  A   metallic,  deep-
FSD_vol2.txt:62936:black,  magnetic  spinel,  (Mn,Mg)(FeMn)304,  crystallizing  in the  isometric  system.  [   <   J akobsberg.  In  Sweden.] Ja-co'bus,  1   ja-kS'bns;  2   ]a-e5'bfis,  a.  An  English  gold coin  of  the  reign  of  James  1.  See  coin.  [<  LL.  Jacobus;
FSD_vol2.txt:74254:lolden  Legend.  1.  A   medieval  collection  of  lives  of the  greater  saints  composed  in  Latin  by  Jacobus  de  Voragine (1230-1298),  a   Dominican,  archbishop  of  Genoa,  published In  translation  by  Caxton  in  1483.  2-  A   poem  by  Longfel- low, based  on  a   story  by  Hartmann  von  der  Aue,  a   minne- singer ot  the  12th  century.  The  legend  runs  that  Henry, prince  of  Hohencok,  being  afflicted  by  leprosy.  Is  told  that he  can  be  cured  only  by  the  voluntary  sacrlflee  of  a   chaste virgin.  Elsie,  daughter  of  one  of  his  vassals,  offers  herself, but  at  Salerno  the  leprosy  disappears  and  the  pair  are  mar- ried.—le-gen'da, «.  pf.  Eccl.  Things  to  be  read,  as  dis- tinguished from  credmda,  or  things  to  he  believed.— leg'- eud-lst,  M.  One  who  writes  legends:  a   fabulist.—  leg'end- ize,  vt.  To  write,  paint,  or  engrave  a   legend  upon;  furnish with  a   legend.—  leg'end-ry,  n.  Legend:  legends  collectively.
```


## [2026-09-04T22:50:34.176Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSD_vol2.txt',encoding='utf-8').read()\nlines=t.split('\\n')\nleaf=0\ntgt={62777:None,62909:None}\nfor i,l in enumerate(lines,1):\n    if i in tgt: tgt[i]=leaf\n    leaf+=l.count('\\f')\nprint(tgt)\npg=t.split('\\f')\nfor i in sorted(set(tgt.values())):\n    for j in (i-1,i,i+1):\n        m=re.findall(r'(?m)^\\s*(1[0-9]{3})\\s*$', pg[j])\n        print(j,m, pg[j][:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T22:50:36.126Z] TOOL RESULT

```
{62777: 601, 62909: 602}
600 []  Iz'baTiVba;  2   ^915.  nV' [Rus.]  A   log  cabin mVhichTm
601 ['1308'] e  to  prevent back-draft  in  a   chimney  or  vent-pipe.  
602 [] an like  bird  (Corvus  monedula),  '   — glossy-black,  wit
601 ['1308'] e  to  prevent back-draft  in  a   chimney  or  vent-pipe.  
602 [] an like  bird  (Corvus  monedula),  '   — glossy-black,  wit
603 []  the Metropolitans  Is  the  Maphrian,  who  is  generally
```


## [2026-09-04T22:50:43.603Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON جک ===\"; grep -c \"\" MON_part1.txt MON_part2.txt; grep -n \"جک\" MON_part2.txt | head -5; echo \"=== ژاک ===\"; grep -n \"ژاک\" MON_part1.txt MON_part2.txt | head -5; echo \"=== عقب ===\"; grep -n \"عقب \\[\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-04T22:50:43.705Z] TOOL RESULT

```
=== MON جک ===
MON_part2.txt:94500
MON_part1.txt:99339
1035:جستجوی بسیار کردن؛ کنجکاوی کر دن. 
1701:غژک: ,۵22( [- جک - جک - 
5355:درفنحک. فر نجکك. فر هانح | (۱.) دبوی که 
5803:درفنجک. برفنجکک] (.) سنگینی که در 
6645:فرنحک: 2۵21) [- فر ونجکك» قس. 
=== ژاک ===
MON_part1.txt:31425:پذاگن: 0- ۳21-5 [یز + ۳ - فژاکن] 
MON_part1.txt:31427:فژاکن» بژوین» دنس. زشت» نازیبا. 
MON_part1.txt:73022:ژاکت: 260 (.) جامةٌ مردانه که تا زانو 
MON_part2.txt:7279:نژاکن: 220 [قس. بز ه] (.) بزهء گناه. 
MON_part2.txt:7283:فژاک: ۱21-0 (ص‌مر.) چرکین؛ چرکن» 
=== عقب ===
```


## [2026-09-04T22:50:50.049Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^جک\\|جَک\\|جک:\" MON_part1.txt MON_part2.txt | head -10; echo \"=== aqab ===\"; grep -n \"^عقب\\|عقب:\" MON_part1.txt MON_part2.txt | head -10; echo \"=== yaqub ===\"; grep -n \"یعقوب\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-04T22:50:50.137Z] TOOL RESULT

```
MON_part2.txt:36130:جکیده‌ای است که شیر خام در آن داخل 
MON_part2.txt:39002:لجک: ۱۸66۸۲ ,اد [تنر.] (.) چارقد 
MON_part2.txt:42533:جکاندن ماشه: (نظ.) کشیدن ماشه. 
MON_part2.txt:46718:جکنده. دسته‌های ببابی 6 
MON_part2.txt:48822:مجک: (قس. مج ] .۲ (کیا.) عدس 
MON_part2.txt:71444:جکر شکستن: تصرف کردن در مزاج اثر 
MON_part1.txt:6190:ابسرنجک: 20۲2016 (ا.مسصف.) سرق» 
MON_part1.txt:22320:جکن نبل» پایروس» حقی» حفاء. 
MON_part1.txt:22541:بسرفنجک: 1 [۲2۱ دا [- درفنحک 2 
MON_part1.txt:26736:بیجک: 0110 [- بجک] (.) قطعةٌ کاغذی 
=== aqab ===
MON_part2.txt:5644:(یعنی از آن سال به بعد). عقب: پس. بیش 
MON_part2.txt:11537:عقب بین و استخوان قمحدوه و دو 
MON_part2.txt:11716:عقب‌نشینی کردن» عقّب رفتن. قدم به روی 
MON_part2.txt:13676:عقب به مهره‌های پشتی 
MON_part2.txt:16005:عقب ب رگشتن» سپسایگی رفتن.(امص.)به 
MON_part2.txt:16006:عقب کتک 
MON_part2.txt:16009:عقب برگشتگی. سیر قهقرایی: حرکت به 
MON_part2.txt:16010:عقب دون آنکه روی را برگر دانند. 
MON_part2.txt:19097:عقب آنان می‌دود و به هر کس که سرپای 
MON_part2.txt:36323:عقب متوجه فرورفتگی‌ها و برآمدگی‌هایی 
=== yaqub ===
MON_part1.txt:34379:پیرکنعان (کد.) یعقوب. پیر گبر: خطابی 
MON_part1.txt:71662:زنبق یعقوبی: ( کیاء) نر گس یعقوبی. 
MON_part2.txt:43323:کنعان: (کد.) بوسف(ع) بن یعقوب(ع). ماه 
MON_part2.txt:43324:مصر : ( کت:) یوسف(ع) ن یعقوب(ع). ماه 
MON_part2.txt:75202:گونه‌های نرگس که بنام زنبق یعقوبی نیز
```


## [2026-09-04T22:50:58.916Z] TOOL CALL #65: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T22:50:58.923Z] TOOL RESULT

```


```


## [2026-09-04T22:51:04.088Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82epo",
 "prompt": "Give the reconstructed root, its meaning, derived terms (especially *h₂epo-teros, *h₂po-, *pos), and descendants in Germanic (Gothic af, Old English of/æf, æfter), Latin (ab, post), Greek. Also any note on *h₁epi vs *h₂epo. Quote key lines."
}
```


## [2026-09-04T22:51:05.793Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B3",
 "prompt": "For the Persian entry پس (pas): give the full etymology (Middle Persian, Old Persian/Avestan forms, Proto-Iranian, Proto-Indo-European reconstruction) and any cited sources (Hasandust, MacKenzie, Cheung). Quote it."
}
```


### [2026-09-04T22:51:10.596Z] TOOL RESULT

```
# Proto-Indo-European *h₂epó

## Reconstructed Root and Meaning
The root is **\*h₂epó**, meaning "off" and "away." It derives from "\*h₂ep + \*-o" (allative suffix).

## Key Alternative Reconstructions
The article notes several variants: "\*ápo, \*apó (based on the missing laryngeal \*h₂ in Anatolian)" and "\*h₂épo."

## Major Derived Terms
Important derivatives include:
- **\*h₂ep-tero-** (comparative form)
- **\*h₂ep-ero-** (producing words like "after")
- **\*h₂ep-s** (producing Greek áps and Latin abs)

## Germanic Descendants
The article traces "\*h₂epó" to Proto-Germanic "\*ab," which yielded Gothic "afar" and related forms in Old English.

## Latin and Greek Descendants
- **Latin**: Proto-Italic "\*ap" developed from this root
- **Greek**: Proto-Hellenic "\*apó" descended from it
- The Hittite "āppa" represents the Anatolian branch

## Laryngeal Question
The document notes uncertainty regarding "\*h₁epi vs \*h₂epo," with alternative reconstructions reflecting debate about which laryngeal consonant belonged in this morpheme.
```


### [2026-09-04T22:51:11.203Z] TOOL RESULT

```
# Etymology of Persian پس (pas)

Based on the Wiktionary entry, here is the complete etymological chain:

**Middle Persian:** 𐭯𐭮 (ps /pas/, "then, afterwards, behind")

**Old Persian:** 𐎱𐎿𐎠 (p-s-a /pasā/)

**Proto-Indo-Iranian:** *pasčáH

**Proto-Indo-European:** *pos-(sḱ)-kʷéh₁

## Cited Source

The entry includes one scholarly reference:

MacKenzie, D. N. (1971): "pas" entry in *A concise Pahlavi dictionary* (Oxford University Press, page 65).

This is the only external source explicitly cited in the Persian section of this Wiktionary entry.
```


## [2026-09-04T22:51:15.300Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/awkward",
 "prompt": "Give the full etymology of \"awkward\", including Old Norse öfugr/afugr, PIE root, and the meaning \"turned backward\". Quote it."
}
```


## [2026-09-04T22:51:16.999Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/evening",
 "prompt": "Give the full etymology of \"evening\" and \"even (n.)\" — Old English æfnung, æfen, Proto-Germanic *æbandiz, and which PIE root it is traced to (*epi? *apo?). Quote it."
}
```


### [2026-09-04T22:51:22.415Z] TOOL RESULT

```
# Etymology of "Awkward"

The word "awkward" traces back through multiple linguistic layers:

**Original Formation (mid-14c.):**
"awkward(adv., adj.)" originated as "in the wrong direction," combining the adjective "awk" meaning "back-handed" with the adverbial suffix "-weard" (related to "-ward").

**Old Norse Root:**
The adjective "awk" derives from Old Norse *afugr* meaning "turned backwards, wrong, contrary," which is itself from Proto-Germanic *\*afug-* (found in related Old Saxon, Old High German, and Dutch forms).

**Proto-Indo-European Root:**
This Germanic term ultimately traces to PIE *\*apu-ko-*, stemming from the root *\*apo-* meaning "off, away."

**Semantic Evolution:**
The original sense of being turned the wrong way became obsolete. By the 1510s, it described something "turned the wrong way," then shifted to mean "clumsy, wanting ease and grace in movement" by the 1520s, and eventually encompassed the social sense of being "embarrassed, ill-at-ease" from around 1713 onward.

This progression illustrates how a physical directional concept evolved into descriptions of both bodily clumsiness and emotional discomfort.
```


### [2026-09-04T22:51:23.475Z] TOOL RESULT

```
# Etymology of "Evening" and "Even"

**Evening (n.):** Derives from Old English *æfnung* ("the coming of evening, sunset"), formed as a verbal noun from *æfnian* ("become evening, grow toward evening"), which stems from *æfen* ("evening").

**Even (n.):** Comes directly from Old English *æfen* (Mercian *efen*, Northumbrian *efern*), meaning "end of the day."

**Proto-Germanic origin:** Both trace to Proto-Germanic *æbando-*, which produced cognates across Germanic languages: Old Saxon *aband*, Old Frisian *ewnd*, Dutch *avond*, Old High German *aband*, German *Abend*, Old Norse *aptann*, and Danish *aften*.

**PIE root:** The document states the Proto-Germanic origin "is of uncertain origin" and does not identify a specific PIE root (*epi*, *apo*, or otherwise) for these words. The etymology terminates at the Proto-Germanic level without confirming a deeper Indo-European ancestor.
```


## [2026-09-04T22:51:42.989Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/%C4%93banths",
 "prompt": "Give the reconstruction, meaning and the etymology discussion of Proto-Germanic *ēbanþs 'evening' — which PIE root(s) are proposed (*h₁epi, *h₂epo, or unknown), and what sources are cited (Kroonen etc.). Quote."
}
```


## [2026-09-04T22:51:44.233Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Jack",
 "prompt": "Give the etymology of the masculine name \"Jack\" — is it from Old French Jaques/Jacques (Latin Jacobus) or from Jankin, a diminutive of John? Quote the relevant text, including any discussion of Jacques."
}
```


### [2026-09-04T22:51:46.249Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T22:51:51.586Z] TOOL RESULT

```
I appreciate your question, but I must be honest: the web page content provided does not contain the etymological details you're asking about. 

The page appears to be a React/Next.js application interface for etymonline.com, but it consists primarily of technical component code, metadata tags, and UI structure rather than the actual etymology text for "Jack."

While the metadata indicates this is an etymology page for "Jack" with the description mentioning "Jackie" and "Jock," the substantive etymological content discussing whether the name derives from Old French *Jacques*/Latin *Jacobus* or from *Jankin* (a diminutive of John) is not present in the provided content.

To answer your question properly, I would need the actual article text from the word page, not just the page's technical structure and metadata.
```


## [2026-09-04T22:51:59.098Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && for u in \"https://www.etymonline.com/word/Jack\" \"https://www.etymonline.com/word/jack\" \"https://www.etymonline.com/word/James\"; do echo \"##### $u\"; curl -sL -A \"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36\" \"$u\" | python3 -c \"\nimport sys,re,html\nt=sys.stdin.read()\nt=re.sub(r'<script.*?</script>','',t,flags=re.S)\nt=re.sub(r'<style.*?</style>','',t,flags=re.S)\nt=re.sub(r'<[^>]+>',' ',t)\nt=html.unescape(t)\nt=re.sub(r'\\s+',' ',t)\nprint(t[:3000])\n\"; done"
}
```


### [2026-09-04T22:52:01.740Z] TOOL RESULT

```
##### https://www.etymonline.com/word/Jack
1:"$Sreact.fragment" 2:I[81874,[],""] 3:I[78560,[],""] 5:I[7909,["6360","static/chunks/app/(main)/%5Blang%5D/(main)/loading-d96e4f903710f125.js"],"Loading"] 6:I[57643,[],"MetadataBoundary"] 8:I[57643,[],"ViewportBoundary"] a:I[61844,["5776","static/chunks/0db7ecf4-29d5b9f39e9decf4.js","485","static/chunks/49be8a9f-62061ade99ef863d.js","3916","static/chunks/f39be7fe-d7468c1f4703ff48.js","5728","static/chunks/5728-2ef4ab29ae4ef138.js","5716","static/chunks/5716-8fad2bb84e9aded1.js","8725","static/chunks/8725-00c383461aa59d7a.js","6027","static/chunks/6027-96f57253a9f92d64.js","9048","static/chunks/9048-381405e5d74defd1.js","4965","static/chunks/4965-6f3293007b6bb3d9.js","7748","static/chunks/7748-57e479ff13533efe.js","1751","static/chunks/1751-16aef6782fa67492.js","3704","static/chunks/3704-20ca8b1c898429f7.js","9380","static/chunks/9380-7c63c04415b7b21f.js","3694","static/chunks/3694-625f13da28600b75.js","6402","static/chunks/6402-b2278d3090d3224c.js","1504","static/chunks/1504-721fc24d10adbd88.js","5932","static/chunks/5932-c0238a966fa69be7.js","2157","static/chunks/2157-b955a7f755649943.js","3027","static/chunks/3027-546a7110bb8c6104.js","15","static/chunks/15-462e8367018baec8.js","8023","static/chunks/8023-a7393a9bd34d9b7f.js","993","static/chunks/993-2662e5592d015a33.js","4601","static/chunks/4601-1bce4a48d360ebce.js","3499","static/chunks/3499-610ec416e705b550.js","4087","static/chunks/4087-7ecbebf7c46f6a85.js","9446","static/chunks/9446-94c38c358486faef.js","2165","static/chunks/2165-37404638fe84be7b.js","164","static/chunks/164-806f3b49efe93f1c.js","7086","static/chunks/7086-696effd4c652afc6.js","1478","static/chunks/1478-6e488222d1f07d43.js","3347","static/chunks/3347-fcf66f2168faf488.js","7755","static/chunks/7755-569e0018b98ffc2c.js","6342","static/chunks/app/(main)/%5Blang%5D/(main)/layout-9280f0282fa24935.js"],"HeaderLogo"] b:I[58048,["5776","static/chunks/0db7ecf4-29d5b9f39e9decf4.js","485","static/chunks/49be8a9f-62061ade99ef863d.js","3916","static/chunks/f39be7fe-d7468c1f4703ff48.js","5728","static/chunks/5728-2ef4ab29ae4ef138.js","5716","static/chunks/5716-8fad2bb84e9aded1.js","8725","static/chunks/8725-00c383461aa59d7a.js","6027","static/chunks/6027-96f57253a9f92d64.js","9048","static/chunks/9048-381405e5d74defd1.js","4965","static/chunks/4965-6f3293007b6bb3d9.js","7748","static/chunks/7748-57e479ff13533efe.js","1751","static/chunks/1751-16aef6782fa67492.js","3704","static/chunks/3704-20ca8b1c898429f7.js","9380","static/chunks/9380-7c63c04415b7b21f.js","3694","static/chunks/3694-625f13da28600b75.js","6402","static/chunks/6402-b2278d3090d3224c.js","1504","static/chunks/1504-721fc24d10adbd88.js","5932","static/chunks/5932-c0238a966fa69be7.js","2157","static/chunks/2157-b955a7f755649943.js","3027","static/chunks/3027-546a7110bb8c6104.js","15","static/chunks/15-462e8367018baec8.js","8023","static/chunks/8023-a7393a9bd34d9b7f.js","993","static/chunks/993-2662e5592d015a33.js","4601","static/chunks/4601-1bce4a48d360ebce.js","3499","stati
##### https://www.etymonline.com/word/jack
1:"$Sreact.fragment" 2:I[81874,[],""] 3:I[78560,[],""] 5:I[7909,["6360","static/chunks/app/(main)/%5Blang%5D/(main)/loading-d96e4f903710f125.js"],"Loading"] 6:I[57643,[],"MetadataBoundary"] 8:I[57643,[],"ViewportBoundary"] a:I[61844,["5776","static/chunks/0db7ecf4-29d5b9f39e9decf4.js","485","static/chunks/49be8a9f-62061ade99ef863d.js","3916","static/chunks/f39be7fe-d7468c1f4703ff48.js","5728","static/chunks/5728-2ef4ab29ae4ef138.js","5716","static/chunks/5716-8fad2bb84e9aded1.js","8725","static/chunks/8725-00c383461aa59d7a.js","6027","static/chunks/6027-96f57253a9f92d64.js","9048","static/chunks/9048-381405e5d74defd1.js","4965","static/chunks/4965-6f3293007b6bb3d9.js","7748","static/chunks/7748-57e479ff13533efe.js","1751","static/chunks/1751-16aef6782fa67492.js","3704","static/chunks/3704-20ca8b1c898429f7.js","9380","static/chunks/9380-7c63c04415b7b21f.js","3694","static/chunks/3694-625f13da28600b75.js","6402","static/chunks/6402-b2278d3090d3224c.js","1504","static/chunks/1504-721fc24d10adbd88.js","5932","static/chunks/5932-c0238a966fa69be7.js","2157","static/chunks/2157-b955a7f755649943.js","3027","static/chunks/3027-546a7110bb8c6104.js","15","static/chunks/15-462e8367018baec8.js","8023","static/chunks/8023-a7393a9bd34d9b7f.js","993","static/chunks/993-2662e5592d015a33.js","4601","static/chunks/4601-1bce4a48d360ebce.js","3499","static/chunks/3499-610ec416e705b550.js","4087","static/chunks/4087-7ecbebf7c46f6a85.js","9446","static/chunks/9446-94c38c358486faef.js","2165","static/chunks/2165-37404638fe84be7b.js","164","static/chunks/164-806f3b49efe93f1c.js","7086","static/chunks/7086-696effd4c652afc6.js","1478","static/chunks/1478-6e488222d1f07d43.js","3347","static/chunks/3347-fcf66f2168faf488.js","7755","static/chunks/7755-569e0018b98ffc2c.js","6342","static/chunks/app/(main)/%5Blang%5D/(main)/layout-9280f0282fa24935.js"],"HeaderLogo"] b:I[58048,["5776","static/chunks/0db7ecf4-29d5b9f39e9decf4.js","485","static/chunks/49be8a9f-62061ade99ef863d.js","3916","static/chunks/f39be7fe-d7468c1f4703ff48.js","5728","static/chunks/5728-2ef4ab29ae4ef138.js","5716","static/chunks/5716-8fad2bb84e9aded1.js","8725","static/chunks/8725-00c383461aa59d7a.js","6027","static/chunks/6027-96f57253a9f92d64.js","9048","static/chunks/9048-381405e5d74defd1.js","4965","static/chunks/4965-6f3293007b6bb3d9.js","7748","static/chunks/7748-57e479ff13533efe.js","1751","static/chunks/1751-16aef6782fa67492.js","3704","static/chunks/3704-20ca8b1c898429f7.js","9380","static/chunks/9380-7c63c04415b7b21f.js","3694","static/chunks/3694-625f13da28600b75.js","6402","static/chunks/6402-b2278d3090d3224c.js","1504","static/chunks/1504-721fc24d10adbd88.js","5932","static/chunks/5932-c0238a966fa69be7.js","2157","static/chunks/2157-b955a7f755649943.js","3027","static/chunks/3027-546a7110bb8c6104.js","15","static/chunks/15-462e8367018baec8.js","8023","static/chunks/8023-a7393a9bd34d9b7f.js","993","static/chunks/993-2662e5592d015a33.js","4601","static/chunks/4601-1bce4a48d360ebce.js","3499","stati
##### https://www.etymonline.com/word/James
 James - Etymology, Origin & Meaning of the Name Search Log in Columns Forum Apps Premium Log in Advertisement Remove Ads Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads. Origin and history of James James masc. proper name, New Testament name of two of Christ's disciples, late 12c. Middle English vernacular form of Late Latin Jacomus (source of Old French James , Spanish Jaime , Italian Giacomo ), altered from Latin Jacobus (see Jacob ). The Welsh form was Iago , the Cornish Jago . James the Greater (July 25) was son of Zebedee and brother of St. John; James the Less (May 1) is obscure and scarcely mentioned in Scripture; he is said to have been called that for being shorter or younger than the other. Fictional British spy James Bond dates from 1953, created by British author Ian Fleming (1908-1964), who plausibly is said to have taken the name from that of U.S. ornithologist James Bond (1900-1989), an expert on Caribbean birds. also from late 12c. Entries linking to James Jacob masc. proper name; Old Testament patriarch, son of Isaac and Rebecca and father of the founders of the twelve tribes, from Late Latin Iacobus , from Greek Iakobos , from Hebrew Ya'aqobh , literally "one that takes by the heel; a supplanter" (Genesis xxv.26), a derivative of 'aqebh "heel." In Spanish as Jago , Iago , also Diego ; with alterations as Italian Giacomo , James , and (contracted) Spanish Jaime . Old French Jacques is from a diminutive of Iacobus (see Jack ). The most popular name for boys born in the U.S. from 1999 through 2008. Jacob's ladder , in various transferred uses is attested by 1733, is from Genesis xxviii.12. Dago (n.) 1823, from Spanish Diego "James" (see James ). Said to have been originally American English slang for "one born of Spanish parents," especially in New Orleans; it was also used of Spanish or Portuguese sailors on English or American ships. By 1900 it had broadened to include non-sailors and shifted to mean chiefly "Italian." James the Greater is the patron saint of Spain, and Diego as generic for "a Spaniard" is attested in English from 1610s. Dago red "cheap Italian wine" is attested by 1899. Jacobean Jemmy Jimbo See All Related Words (5) Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads. More to explore Jamesian "of or in the mode of James," 1875 in reference to William James (1842-1910), U.S. philosopher and exponent of pragmatism...; 1905 in reference to his brother Henry James (1843-1916), U.S. expatriate novelist....seldom, yet it is all unforgettable. […] No man who has not lived on both sides of the Atlantic can well appraise Henry James...[Ezra Pound, from “Henry James,” Little Review, August 1918]... sirloin is because the cut of beef was "knighted" by an English king for its superiority, a tale variously told of Henry VIII, James...English dictionary writer Charles] Richardson) by James I....Chronology makes short work of this
```


## [2026-09-04T22:52:08.675Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /tmp && for u in \"https://www.etymonline.com/word/Jack\" \"https://www.etymonline.com/word/jack\"; do echo \"##### $u\"; curl -sL -A \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15\" \"$u\" | python3 -c \"\nimport sys,re,html\nt=sys.stdin.read()\nt=re.sub(r'<script.*?</script>','',t,flags=re.S)\nt=re.sub(r'<style.*?</style>','',t,flags=re.S)\nt=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t); t=re.sub(r'\\s+',' ',t)\ni=t.find('Origin and history')\nprint(t[i:i+2500] if i>0 else t[:600])\n\"; done"
}
```


### [2026-09-04T22:52:11.052Z] TOOL RESULT

```
##### https://www.etymonline.com/word/Jack
1:"$Sreact.fragment" 2:I[81874,[],""] 3:I[78560,[],""] 5:I[7909,["6360","static/chunks/app/(main)/%5Blang%5D/(main)/loading-d96e4f903710f125.js"],"Loading"] 6:I[57643,[],"MetadataBoundary"] 8:I[57643,[],"ViewportBoundary"] a:I[61844,["5776","static/chunks/0db7ecf4-29d5b9f39e9decf4.js","485","static/chunks/49be8a9f-62061ade99ef863d.js","3916","static/chunks/f39be7fe-d7468c1f4703ff48.js","5728","static/chunks/5728-2ef4ab29ae4ef138.js","5716","static/chunks/5716-8fad2bb84e9aded1.js","8725","static/chunks/8725-00c383461aa59d7a.js","6027","static/chunks/6027-96f57253a9f92d64.js","9048","static/chun
##### https://www.etymonline.com/word/jack
1:"$Sreact.fragment" 2:I[81874,[],""] 3:I[78560,[],""] 5:I[7909,["6360","static/chunks/app/(main)/%5Blang%5D/(main)/loading-d96e4f903710f125.js"],"Loading"] 6:I[57643,[],"MetadataBoundary"] 8:I[57643,[],"ViewportBoundary"] a:I[61844,["5776","static/chunks/0db7ecf4-29d5b9f39e9decf4.js","485","static/chunks/49be8a9f-62061ade99ef863d.js","3916","static/chunks/f39be7fe-d7468c1f4703ff48.js","5728","static/chunks/5728-2ef4ab29ae4ef138.js","5716","static/chunks/5716-8fad2bb84e9aded1.js","8725","static/chunks/8725-00c383461aa59d7a.js","6027","static/chunks/6027-96f57253a9f92d64.js","9048","static/chun
```


## [2026-09-04T22:52:14.928Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Jack",
 "prompt": "Give the English etymology of the given name \"Jack\" — is it from Jankin (diminutive of John) or from French Jacques/Latin Jacobus? Quote the etymology section exactly."
}
```


## [2026-09-04T22:52:17.080Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9%D9%82%D8%A8",
 "prompt": "Give the Arabic entry عقب — root ع ق ب, verb ʿaqaba, noun ʿaqib/ʿaqb 'heel', and the Persian entry عقب (aqab) if present, with its stated origin (borrowed from Arabic). Also list Semitic cognates mentioned (Hebrew, Aramaic/Syriac, Akkadian). Quote."
}
```


### [2026-09-04T22:52:21.660Z] TOOL RESULT

```
# Etymology of "Jack"

Based on the Wiktionary entry, **Jack has dual etymological origins**:

## Primary Etymology (pet form of John)

The main English etymology traces through Middle English:

> "From Middle English Jak, Jakke (also Jackin, Jankyn, etc.), from Anglo-Norman Jakke, *Janke, from Middle Dutch Janke, diminutive of Jan ("John")"

This establishes Jack as ultimately deriving from a diminutive form meaning "little John."

## Secondary Etymology (from Jacques/Jacobus)

The entry also notes Jack can function as "an anglicized form of Jacques," linking it to the Latin Jacobus tradition. The translations section distinguishes between:

- **"pet name of John"** (the Jankin derivation)
- **"anglicized form of Jacques"** (the Jacobus derivation)

## Conclusion

Both pathways are valid. Jack originates as a diminutive of John via Middle Dutch/Anglo-Norman, but it's also used as an English version of the French name Jacques, which itself derives from Latin Jacobus. The name has "become more of an independent name" despite its original pet form status.
```


### [2026-09-04T22:52:23.335Z] TOOL RESULT

```
# Arabic عقب (ʿaqb)

**Root:** ع ق ب (ʿ q b)

**Noun ʿaqib/ʿaqb** — Primary meanings include "heel" (feminine) and "end" (masculine). The entry notes: "heel," "end," "grandson," and "offspring, progeny."

**Verb ʿaqaba (Form I)** — Means "to follow, to succeed, to come after"

**Verb ʿaqqaba (Form II)** — Means "to follow, to succeed; to ensue, to pursue, to trail, to tail; to return to" and "to comment, to revise"

---

# Persian عقب (aqab)

**Etymology:** "Borrowed from Arabic ʿaqb"

**Noun** — Denotes "heel" and "back part"

**Preposition** — Means "behind"

---

# Semitic Cognates

The Arabic entry references: "Hebrew עָקֵב (ʿāqēḇ, 'heel')" — establishing etymological connection across Semitic languages.
```


## [2026-09-04T22:52:31.963Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%99%D7%A2%D7%A7%D7%91",
 "prompt": "Give the Hebrew entry יעקב (Yaʿaqov) — its etymology (from עָקֵב ʿaqev 'heel', or from a root meaning 'protect'), and any note on Proto-Semitic / Akkadian / Amorite parallels. Quote."
}
```


## [2026-09-04T22:52:33.833Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/post#Latin",
 "prompt": "Give the Latin entry \"post\" — its etymology (Proto-Italic, PIE *pos / *h₂epo, Old Latin poste), and the derivation of pōnō/pōnere (from *po-sinō). Quote."
}
```


### [2026-09-04T22:52:37.600Z] TOOL RESULT

```
# Hebrew Entry: יעקב (Ya'akóv)

## Etymology

According to the Wiktionary entry, the name derives "from the imperfect of עָקַב, related to עָקֵב (heel)."

The root is listed as **ע־ק־ב** (ʿ-q-b), which connects the name to the concept of a heel. This aligns with the biblical narrative where Jacob's name relates to his birth circumstance.

## Note on Ancient Cognates

The source document does not provide information about Proto-Semitic, Akkadian, or Amorite parallels. However, it does indicate that the name was transmitted into other ancient languages through the descendants section, notably Ancient Greek (Ἰακώβ) and Arabic (يَعْقُوب), suggesting the name's significance in Near Eastern linguistic traditions.

The documented etymology focuses specifically on the Hebrew verbal root connected to "heel" rather than exploring broader comparative Semitic etymology.
```


### [2026-09-04T22:52:41.631Z] TOOL RESULT

```
# Latin Entry "post" — Etymology and Derivation

Based on the Wiktionary content provided, here is the Latin etymology:

## Etymology

The Latin word *post* derives from Proto-Italic *\*postis*, which traces back to Proto-Indo-European roots. The etymological tree shows two possible PIE sources: *\*pró* (meaning "before") combined with *\*steh₂-* ("to stand"), or *\*h₂pó* ("away") similarly combined with the "stand" root.

## Derivation of pōnō/pōnere

The content indicates that *pōnō* comes from a different etymological path. According to the material, it derives from Proto-Italic *\*sinō*, which itself developed from PIE *\*tḱinéti*. The prefix *po-* (from *\*h₂pó*, meaning "away") combines with this root to form *pōnō*.

The document states: "Latin _[posita](/wiki/positus#Latin:_participle "positus")_" showing the participial form that connects to the sense of "placing" or "positioned."

This dual etymology explains why *post* (the physical upright) and *pōnō* (to place/position) share semantic territory but different linguistic origins in Latin.
```


## [2026-09-04T22:52:50.677Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW post ===\"; grep -n \"^post,\\|^post \\|poste \" LEW_1910.txt | head -5; echo \"=== LAT post ===\"; grep -n \"^post\\b\\|^post,\" LAT.txt | head -5; echo \"=== LAT pono ===\"; grep -n \"^pono\\|^pōnō\\|pono,\" LAT.txt | head -5; echo \"=== LEW pono ===\"; grep -n \"^pono\\|pono,\" LEW_1910.txt | head -5"
}
```


### [2026-09-04T22:52:50.765Z] TOOL RESULT

```
=== LEW post ===
5553:pisé IT 308 pjekete IT 270 pjet IT 386 per? IT 273 plak IT 239 plest IT 385 pl’af I 321 pl’aje IT 314 pl’enk, pl’engu IT 315 pl ép IT 340 pl chure IT 321 plis IT 505 pl’ok, pl’oge I 352 plot II 322 pl’uar I 834 porda IT 273 porde IL 75, 273 poste IT 294 pots IT 351 prape I 1 prift i 360 prus IT 379 pruva, prura IT 344 prua Il 223, 438 psin I 460 pstet II 598 putum IT 242 pune IT 608 pustét IT 347 ptt I 243 ragal I 63 ré I 418 retere II 665 re (geg.) I 418 remp IT 416 ren (alt) I 419 rit I 64 rjep IT 417 rode, rozge II 416 Fa, Tani Il 438 Fed IT 435 7oda IT 435 fuajy IT 416 sa I 371 sete IT 462 sember II 457 site IT 462 sivjet I 193 sjet I 246 skuy IT 497
=== LAT post ===
4090:post(i) de la particale -die): antid (cf. postid) conserve dans antidea,
18149:post norte* durare uidetur en face de 349 [artus] pereunt... conque-
27284:post-habitO. Le sena de "tenir" apparait dans lea expressions habere
48735:post-ne ; 1'ombrien appuie la seconde explication qui a aussi pour
49336:post s'est g^neralisee, tandis que l'e final du mot du sens oppose
=== LAT pono ===
29727:a le sens de: i° "entre", inter-calo,-cedo,-pono,-uenio, etc.; 3 0 "par
48737:pono, -i s, poslul (puis posui), positum, ponere. Pono est issu
56805:•premier terme de compos 4 s: secedo, sepono, se-curus, sedulo, se¬
=== LEW pono ===
```


## [2026-09-04T22:52:53.425Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '48720,48760p' LAT.txt; echo \"----49320----\"; sed -n '49320,49345p' LAT.txt"
}
```


### [2026-09-04T22:52:53.493Z] TOOL RESULT

```
iGloss.j; pomosus-, Pomona: dc?esse des fruits; pomStium, mollis et
liquidus cibus ex pomis (Gloss.); pomifer. Faut-il y rattacherysi
p5nS
Poemanae qu'on lit sur une inscription d'Espagne, CIL II «573? 11 est a noter
que le diminutif pGmulum est atteste a basse epoque arec le sens de "petite
pomme", qui correspond au sens pris par pGmum dans certaines langues romanes.
Pour la coexistence de pomus et pomum, cf. pirus et pirum . Aucune
etymologie n'est connue. Doit etre emprunte, comme le sont en general
les nona latins de fruits.
pondus: v. pendG.
pone: — graui sono ponitur pro loci significatione, F.3y3,iG.
Adverbe et preposition archafque, repris par la 1 . imperiale "derribre"
et "par derribre". Cf. super-ne. Cf.ombr .postne (oppose a perne "ante"),
d'ob pustnaiaf "posticas". Remplace par post.
V. post. On ne peut determiner si pSne repose sur *pos-ne ou sur
post-ne ; 1'ombrien appuie la seconde explication qui a aussi pour
elle l 1 existence de post.
pono, -i s, poslul (puis posui), positum, ponere. Pono est issu
de po-sino > pozno > ponG. le parfait ancien est poslui (poseiuei
CIL I 3 6383» 13« av. J.-C. ). Posui a ete fait sur positum, sur le
modble monitum/monui, le rapport avec sinG ayant cesse d'etre senti.
Sens propre "mettre a 1 ’ecart". S'emploie usuellement dans le sens
de "poser, placer"; mais la valeur ancienne apparaft dans des ex-
pressions comme ponere uitam, arma, dolorem (a cote de deponere
plus fr^quent parce que p 5 nd apparaissait comme un verbe simple,
cf. sumo), ou le verbe signifie "abandonner, deposer". Usite aussi
dans le sens de propGnG "proposer". A remplac^ facid dans le sens
concret de "placer". A traduit dans le langage abstrait le gr. tCGtuxl
comme positid, positura (lucr.) traduit Gecrus, 9 ep.oc, positluus',
GextxoC (d'ou iri. posit). Positio n'apparait du reste qu' a 1 'epoque
imperiale. Cic^ron 1 'ignore, quoiqu'il em^loie prGpositiG (= TipoGeotc
et TcpoTCujt c 7 tpo^Xri(Aa); compositio (= cruvGetxi, s), dispositio (= Sicc-
©ecris et otxovonta, tu.Z i i<;), expositio (= TtpoexGeaxc, 71 po<puy\. i), prae¬
positio (= 7 tpo 0 e< 7 iG, TtpoGrptri). Cf. encore appositum = e 7 H 0 exov, appo-
sitiuus - e7tl.T0tYpxxxi.x0C • la langue de la rhdtorique, de la grammaire
et de la philosophie a ainsi calque sur xt, 0 r|p,l. et ses compos^s tous
les termes techniques dont elle avait besoin. - Usite de tout temps.
Panroman, M.L.6647 et *ponitare 6G48.
En roman, pGnere s'est speci ali s 4 dans la 1 . rustique au sens de
"deposer ses oeufs, pondre" (cf. cubare), tandis que paus&re prenait
le sens de "poser". Ilest probable que la ressemblance de forne
----49320----
archaique on rencontre potestur, possTtur, poteratur, possetur quand
le compl^ment de possum est un infinitif passif: cf.nequitur. - La
l.populaire a refait secondairement sur potui un pr^sent poteo,
repr 4 sent^ dans toutes les 1 . romanes, M.L.CGOa, et qui, bistoriquement,
n'a rien de commun avec le verbe italique commun atteste par 1'accord
de 1'osque et du latin ancien potens, potui.
De possum derivent les adj. savants possibilis, impossibilis,
cre£s a l' 4 poque imperiale (Quintilien) pour traduire le grec Suvaxos,
aSuvaxos, et sur lesquels ont ete faits possibilitas (Arn.), impos¬
sibilitas (Apul., Tertullien).
V. potis.
*postl, poste, post, postid, postea, postidea: post est issu de
*pos-ti (cf. ante de *anti)-, 1 * i en finale absolue a abouti a e (on
a encore la forme poste dans Enn.A.330 poste recumbite, Pl.As.y15,
ete.) et a pu tomber dans certaines conditions syntactiques ( cf.
ac et atque, nec et neque, animal et animale). Finalement la forme
post s'est g^neralisee, tandis que l'e final du mot du sens oppose
ante est constant: postquam (prononce pos quam,, cf. Mar.Victor. GLK
VI aa, 11) mais antequam', la raison de cette difference de traitement
n'apparait pas; 1 'osque a ant- comme pust. Posti pouvait etre renforce
de la particule -d(e), de la postid ( postid locorum, Pl.,Poe.i44, ete.),
d'ou derive postidea. 0'est sans doute d'aprbs postid dont 1'origine
n 1 apparaissait plus qu'a 4 te construite 1'expression ad id locorum.
La forme pos- ne semble pas remonter a un i.-e. *pos~, mais repre-
senter post dont le t serait tombe dans certains groupes: pone, pome¬
rium, de postne, *posne, ete., cf. postmeridianas et posmeridianas
```


## [2026-09-04T22:53:00.923Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8').read()\npg=t.split('\\f')\nprint(len(pg))\nfor i in (82,83,84):\n    s=pg[i]\n    print('=== leaf',i,'===')\n    print(s[:1600])\nEOF"
}
```


### [2026-09-04T22:53:02.844Z] TOOL RESULT

```
725
=== leaf 82 ===
78                                                porkos   — pos
   Bret, ozech ^^Hausherr, Gatfee“ (Fickn^49; zum -z- s. Pedersen KG. I
&27 f., zum oj-Suffix II 25. .Hingegen ist mir. aithech „Zinsbauer, Bauer,
Mann“ nach Thurneysen Abl. von aith-fe „Vergeltung'*, und geht dssae „mog-
lich“, ibd. und Stokes KZ. 38, 459 f., auf ad-staio- zuriick, s. sta~ „stehen‘‘).
   Got. hrup-faps „Brautigam'‘, hunda-faps ..Befehlshaber iiber 100 Mann'‘.
Lit. pafis, pats „Gatte“, vess-patis „Herr, regiereiider Herr, Herrgott“, pat\$,
„selbst“, \Qti.pats „selbst'‘, fern. alit. wesch-patni (d. i. v'esz-patni), woneben als
Keubildung nach dem Masc. lit. pafi „Herrin^', apr. wais-pattin acc. sg. „Haus-
frau‘^ Hieher wohl auch abg. gospodh „Herr'^ (s. auch ^ghostis^ und zum
d Berneker 334 ff, m. Lit.; ein Kons.-St. *poty woneben ^pod?, ist mir
freilich sehr verdachtig; liegt diss. Erweichung des zweiten t in der Yor-
stufe "^ghostir-poti- vor?), gospoda y,7iavdoxeTov^^ (s. auch oben zu dEonoTrig).
   Curtius^ 282 f,       —
                        Arm. hay, pi. hay¥ „Armenier‘‘ bleibt fern (zum Lands-
und Yolksnamen Chati, Uhlenbeck Ai. Wb, 154).                          —
                                                           Die Deutung von ahd.
wJb „Weib“, weibel „Gerichtsdiener‘‘ aus udk-, tioik-p6~ (Bezz. KZ. 41,
282)    s.   u. tieik-   Siedelung“;          trifft sie   zu, so ist wib, *ueik-p6   am ehesten
als Kurzform zu ai. vig^pdtnJ, lit, veizpatni zu deuten; ob in Weibel eine
solche zu v'esz-patis ist der Bed. halber (eher „Schutzer der Ansiedelung
—  Aufseher        —
        
=== leaf 83 ===
                                                                    ;   ;




                                pu, peu-, pou- auch phu-,                            79

Briickner KZ. 45, 54). poz-derije (paz-derije) ..xaXdju}], orvjieTov'\ Zu lit.
pas auch pastaras „der letzte, hinterste'^ (s. Leskien Norn. 446, auch Solm-
sen KZ. 37, 592).
   Ableitungen: 1 mit ~ti (vgl. das Gegenstiick "^anti „ante, dvti*') wohl arm. ost
                    .



„nach‘*, Adverbal und Praep. m. Abl. „Dach, post’’, m. Dat, „nach           = secundum,
gemaB‘‘ (u. dgl., Pedersen KZ. 39, 430 f.; dazu stor „der untere Tei?’??); lat.
post, sAs^tpostc „nach, hinter’^, ortlich undzeitlicb, Adverbal und Praep. m. Acc.,
osk. pilst,post, umbr. post, pus „post'^ ortlich und zeitlich, Praep. m. Abl. (aber
lat. posthac, -ea nicht nach Delbriick Grdr, I 638 mit demselben Abl., sondern

mit adv. erstarrtem, nicht mehr kasuell empfundenen Jicic, ea) davon lat. pos-
terns, osk. pustrei „in postero“, umbr. postra, lat. postumiis, osk. piisima\f\
„postremae‘* (scheint nach Brugmann IF. 24, 72ff. erst ital. aus *posti-tero~,
-t^mo- entstanden, so da6 ohne Zshang mit lit. pastaras) umbr. postne, lat.
pone aus *posti-ne; osk. pustin, u. pustln (aus ^posii en) je nach^* Praep. m.
                                                                ,


Acc.   umbr. pustnaiaf „posticas“, purnaes „posticis“; lat, posticus „hmten
       ;


befindlich‘\ Ohne arm. dst konnte ital. ^pos-ti als erst ital. Erw. nach ^anti
gelten (OsthofF Pf. 531).       —
   2. mit -qo- ai. paged (Instr.) Adv, ,,hinten, westlich, spater‘‘ = av.
=== leaf 84 ===
80                                               pu, peu-, pou" aueh   phu


     Ai. pfda~h, pfilaka-h ^Biindel, Biischel*' (^Ansehwellung, Aufgeblasenes“);
           pule
lett. pulis,            Herde, Kette (von Jungwild), Kest, Strichregen'',
piin „Eegenwolken‘’, sJcudru-pillis „Ameisenhaufe'', pilldl „sich vermehren,
sich sammeln'*; russ.          klr. piiVa ,,Kuger\
                                           pi'ilja,

   Lett,   p'turs^        „Hinterhaupt, Schadel; GipfeP' (*„Wolbung“), lit.
                                  paiire
paras                lett. pars „HohlniaB fiir Getreide (Lof.),   Aussteuer-
kasten“, pUrin'sch „ein Koben, ein sog. Paudel oder Pudel aus Liindenborke^'.
   Lett, puns, pane ,.Auswuchs am Baum, Hocker*, punis „Beule‘‘, pct’nns,
pnUtina „Scbadel, Stirnknochen“, auch Tv^ohl apr. pounian „Hmterbacke“,
lett. pauna ^Rucksack, Ranzel, Bundelchen^', pipaund „auf dem Rucken“,

paundt „buckeli3, auf dem Riicken tragen“, gr. 7im>vog' 6 TtQCoy.jog Hes., lakon.
TiovvidCsiv          (s. u.       "^apo, *pu,         zu   dem sie kaum         wahrscheinlicher       gezogen
wurden).
   p(h)u-q-: arm. p^tik^ ,,Hauch, Wind, Furz'', pi. .,BIasebalg“, p\ym „hauche“,
p^Ifam „blase mich auf’. Xpers. pilk „das Blasen (um Feuer anzufachen),
Blasebalg^S afgh. pil, puk „a puff, a blast, the act of blowing'', pukai ,.a
puff, inflating" (s. Hiibschmann Arm. Gr. I 256, 502, Horn Np. Et. 75, Grdr.
d. iran. Phil. I 2, 74;                    unasp. Anlaut).
     Lit. paJcne „Blatter", pukszle „Beule" (oder dies mit 7j-Einschub oder
mit Umstellung naher zu pitsze, piisz
```


## [2026-09-04T22:53:16.792Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 apo ===\"; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8').read()\npg=t.split('\\f')\nfor i in (55,56,57):\n    print('--- leaf(0-based)',i,'---')\n    print(pg[i][:900])\nEOF"
}
```


## [2026-09-04T22:53:18.350Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA Jakob/aqib ===\"; grep -n \"Jakob\\|'aqib\\|aqib\" AFA.txt | head -10; echo \"=== TAD ===\"; grep -n \"يعقوب\\|عقب\" TAD.txt | head -10; echo \"=== SYN behind ===\"; grep -n \"^12.4[0-9]\\|BEHIND\\|AFTER (\" SYN.txt | head -10"
}
```


### [2026-09-04T22:53:18.760Z] TOOL RESULT

```
=== WLD Bd1 apo ===
--- leaf(0-based) 55 ---
                                               ap-, ap-       — apo, po                                  47

FluBnamen auf -npa, ahd. - affa wie ahd. Eril-affa „Erlaff“ (die also nicht
                                                   ,


eine gall. Entsprechung von lat. aqua voraussetzen).                                Zur Erklarung der
6-Form geht Johansson IF. 4, 137 f. ansprechend von                          dem durch ’Anid cov,
Amdavog sowie durch
                 ,
                                        ai.    dbclct-       m. „Wolke“ und dem mit apah para-
digmatisch zusammengeschweifiten d. i. pi. ai. ddbhih, adbhyah ( *ahdbhis                                     ,


*abdbhyas) vorangesetzten Stamm ap{d)d- (vielleicht „Wasser gebend“, mit
zu do- „geben“ gehorigem 2. Gliede) aus: *abdo(n ), gen. *abdnes , woraus
*abnes   aus den obi. Kasus entsprang lat. amnis , wahrend im kel
--- leaf(0-based) 56 ---
48                                                              apo, po


  got. a/’Praef. und Praep. m. Dat. „von, von— weg, von— her“, anord. af Adv.
und Praep. m. Dat., ags. cef, of as. af, ahd. aba. ah- „von, von— weg“, nhd. ah-.
                                                      ,


     Ygl. auch lit. apacia „der untere Teil i!(s. Brugmann KYG. 470, Schulze

KZ. 40, 418).        Ganz fragliclies aus deni Arm. bei Pedersen KZ. 39, 399,
427.        Als kelt. Abkommlinge von *apo werden in Anspruch genommen
acymr. ncymr. o „ex, ab, de“, a.-mcorn., a.-nbret. a ds. von Fick II 4 4,
Stokes BB. 23, 64; 29, 171, Zimmer ZfceltPb. 2, lOSff., der den Gegen-
satz o a aus idg. *dpo:po erklaren will; liegen darin wirklich Abkomm-
            :



linge unserer Sippe vor, so konnte von einbeitlichem *apo ausgegangen
werden, woraus *o, und im Corn, und Bret, d mit so friiher Proklisen-
kiirzung
--- leaf(0-based) 57 ---
                                                         apo, po                                                      49

navis umgebildetes *pnppos „Hinterer“ zu sein, das als eine Bildung mit
gehrochener Reduplikation, Lewy IP. 32, 160 Anm. 1, und mit aus der
Kindersprache stammender Konsonantenscharfung verstandlich ist); mog-
licherweise auch gr. nvvvog o ngcoxiog Hes., lakon. novviaCeiv no. tdixoTg
                                               '                                                '




%Qi]G&ai.     novviov                      (gegen die Gdf. *nvx-ovog, die
                               yag 6 daxivhog Hes.
Brugmann GrGr. 3 99, 4 16, Grdr. II 2 I, 263, Persson aaO. wegen ai. pu-
                                       1



tdu „die Hinterbacken“ ansetzen, spricht das einfache n von novviov Bally                               ,


Msl. 12, 324; wenn iiberhaupt zugehorig,
```


### [2026-09-04T22:53:18.840Z] TOOL RESULT

```
=== AFA Jakob/aqib ===
2445:denke man daran , dass Jakob Gen. 35 , 4 auch die Ohr-
=== TAD ===
565:ينطلون ايطالي 9281006م معناه نسيج يبلغ الىالعقب . وقد جرى استهاله 
2569:كاسات وقاشين - لانيني 3ع معناه غطاء عقب الرجل . وجورب 
=== SYN behind ===
22095:12.41 RIGHT I,
22120:12.42 LEFT (Adj., vs. Right) + dpiorepés, ebdvupos, Goth. hleiduma Lith. Kairias oxatds, Natds ON vinstri Lett. Kreis Pairrent, CepBbs Dan. venstre Chl. Sujf, Levit sinister, laevus, Sw. _ vdnster SCr. lijevt Scaevus OE _—winestra Boh. levy Epo ME lift, luft Pol.  lewy a NE left Russ. levyj um Mquierdo, siniestro Du. linker Skt.  savya-, vama- iy 40 OHG winistar, slinc Av. — haoya-, vairyastara- eee MHG winster, linc dé (tuath) ETS LET NHG link Gswy, chwith Neiz There is no
22171:12.43 NEAR (adv.)
22198:12.44 FAR (adv.)
22276:12.46. Words for ‘west’ are derived from those for the ‘setting, going down’ (of the sun), or ‘evening’ or ‘behind’ (as opposed to ‘in front’ = ‘east’, cf. 12.45).
22308:12.47. Words for ‘north’ are from the name of a north wind, a northern con- stellation, ‘midnight’, ‘winter’, ‘upper region’, and from ‘left’, or under a south- ern orientation ‘behind’.
```


## [2026-09-04T22:53:29.867Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"12.45\\|BEHIND (adv\\|behind’ (Av\" SYN.txt | head; echo \"---\"; grep -n \"Av. pasca\\|NPers. pas\\|Pers. pas\\b\" SYN.txt | head"
}
```


### [2026-09-04T22:53:29.957Z] TOOL RESULT

```
22241:870 12.45 HAST 12.46 WEST Grk. — dvarody, éws éoxépa, dvopal, dbots NG évarody Shots Lat. _oriéns occidéns, occdsus It. est, levante ovest, ponente Fr. est ouest Sp. este oeste, poniente Rum. est, rdsdrit vest, apus Ir. airther iarthar Nir. oirthear tarthar W. dwyrain gorllewin Br. reler, savheol kuzheol, kornaoueg Goth. urruns saggqs ON austr vesir Dan. gst vest Sw. Oster vdster OE éast west ME est west NE east west Du. oosten westen OHG dstan westan MHG  dsten west(en) NHG  osten westen Lith. rytai vakarat Lett. austrums, rili rielums, vakari ChSl.  vitstokiz zapadit SCr.  istok zapad Boh.  vgchod zdpad Pol. wschéd zachéd Russ. vostok zapad Skt.  purvd-(dig-), pratici-(dig-), praci-(di¢-) paccima-(di¢-) Av. upaosanhva-, daosatara- (adj.)
22276:12.46. Words for ‘west’ are derived from those for the ‘setting, going down’ (of the sun), or ‘evening’ or ‘behind’ (as opposed to ‘in front’ = ‘east’, cf. 12.45).
22338:Lat. auster ‘south wind’, also ‘south’, prob. orig. ‘east wind’ : ON austr, etc., feast’ (12.45), with shift through ‘south- east’ explained by the diagonal position of the axis of Italy. Walde-H. 1.87. Ernout-M. 94 (with some doubt).
---
```


## [2026-09-04T22:53:31.369Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT ==\"; grep -n \"^of\\b\\|^off\\b\\|^after\\b\\|^awkward\\|^post-\\|^even (2\\|^eve,\" SKT.txt | head -20"
}
```


### [2026-09-04T22:53:31.431Z] TOOL RESULT

```
== SKT ==
492:of  ■  church.  (F.-L.) ,«  F.  tfiViT. » \^  itia,  a  wing. dbniD.  of  Axil. XyoU
893:of  a   n£c  (ipplicd  lo   a
895:of  var^p,  a  falher;  and
1163:of  an'oi:  %ct  oriole
1319:of  B  baUuce.
1340:of  bal,  a  dance.
2067:of  >  the
2368:of  brumtt,   brownish.  —  M.  H.  G.    bnin, brown.
2420:of  Ihe  cow-  (E.)    ME. I«C  foonrl  tn  AS.,  but  tbe
2498:of  i«»#tMii)  to  bum.  4"  O.
2597:of  oceidert  \  sec  oooaaion  (above).
2721:of  a  to/.
2759:of  in  fsn^itture,  to  glow  ;
2768:of    burnt
3082:of  F<  tjUiitAin  «  O.  F.  t^AtiJ/r-
3497:of
3648:of  the  lock  of  a  gun. ta.  the  botch  of  an  arrow  ; fit  an  arrow  on  the  bow- •  pnn,  by  the  transrerence ola  archery  teim) ;  cL  lul. Id  off  an  arrow.     The ifnscd  with  F.  £^,  a  cock, 'phrase  Jm  Bakn  spanntn, Orij.'in  of  IiaL  cocta  (  — F. ;  but  sec  Cos. a  bMit ;  see  Conoh. Oocluttoo;  see  Cook(i). lee ;  ac«  Orooodil«. to    pamper.     (C  7)       M.  E. •  W,   orrr*  to  fondle,  indalge; aoubi^  fioodling.     Perhaps  allied ■Br.  C^im.  MTp  Tain,  foolish.
3650:of  fft-i,  a  cockle  (P.
3766:of  Ibe  regimcnl      Diniu).  of
3773:of  tbem  is  always  beneath
```


## [2026-09-04T22:53:41.528Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== RCH pas ==\"; grep -n \"pas, Behind\\|pas, behind\\|A pas, \\|P pas,\" RCH.txt | head -5; echo \"== RCH aqib ==\"; grep -n \"'akib\\|ʿakib\\|akib, A\\|A 'ukb\" RCH.txt | head -5; echo \"== SKT awkward ==\"; grep -on \"awkward[^.]\\{0,200\\}\" SKT.txt | head -3; echo \"== SKT post ==\"; grep -on \"Post (2[^.]\\{0,200\\}\" SKT.txt | head -3"
}
```


### [2026-09-04T22:53:43.998Z] TOOL RESULT

```
== RCH pas ==
== RCH aqib ==
== SKT awkward ==
2706:awkwardly
13486:awkwardly ;  Ijavarian patoft,  to  pat;  see  Pat  (i)
20439:awkward
== SKT post ==
```


## [2026-09-04T22:53:51.145Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WEB awkward ==\"; grep -on \"awkward[ ,][^.]\\{0,300\\}\" WEB_vol1.txt | head -3; echo; echo \"== WEB jack ==\"; grep -on \"jack (jak)[^.]\\{0,400\\}\" WEB_vol1.txt | head -2; echo \"== WEB Jacqueline ==\"; grep -on \"Jacqueline[^.]\\{0,200\\}\" WEB_vol1.txt | head -3"
}
```


### [2026-09-04T22:53:53.282Z] TOOL RESULT

```
== WEB awkward ==
6398:awkward, as though both hands were the left: opposed to ambidextrous
10940:awkward boat
14322:awkward position

== WEB jack ==
== WEB Jacqueline ==
```


## [2026-09-04T22:53:58.881Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"awk'ward[^\\n]\\{0,350\\}\" WEB_vol1.txt | head -3; echo \"---\"; grep -on \"ME\\. *awk\\|ON\\. *ofugr\\|ofugr[^\\n]\\{0,200\\}\" WEB_vol1.txt | head -5; echo \"=== jack ===\"; grep -on \"\\[ME\\. *jakke\\|jak'\\(ass\\)\\|Jacques, *from *LL\\. *Jacobus[^\\n]\\{0,200\\}\" WEB_vol1.txt | head -5"
}
```


### [2026-09-04T22:54:00.766Z] TOOL RESULT

```
---
14318:ME. awk
14322:ME. awk
=== jack ===
101616:[ME. jakke
```


## [2026-09-04T22:54:04.164Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14315,14330p' WEB_vol1.txt; echo \"==== jack ====\"; sed -n '101610,101625p' WEB_vol1.txt"
}
```


### [2026-09-04T22:54:04.240Z] TOOL RESULT

```
a-woke’, v., alterna’
a-work’, adv. Ase, butt, brite, tūrn, up; cry, myth; cat, machine, ace, church, chord; gem, afiger, (Fr.) bon, as:
awork oe
bonnet; also, excessive; great; remarkable; as, an awful lie. {Colloq.] $ a Syn.—dreadful, fearful, solemn, direful, im- pressive, appalling. 3 aw’ful-ly, adv. 1. ina manner to fill with awe; in a reverential manner. J ET exceedingly; as, awfully bad taste. alloq. ; aw’ful-ness, n. 1. the quality of striking with awe or reverence; solemnity; as, the awfulness of this sacred place. f 2. the state of being struck with awe, [Obs.] A help to prayer, producing in us reverence and awfulness. —~Taylor. a-whape’ (-hwap’), v.t. [ME. dead ke. to strike with amazement; to confound. [Obs.] a-while’ (-hwil’), adv. for a while; for a short time. a-wing/, a. or adv. on the wing; in flight. awk, n. an auk, [Obs.] awk, a. (ME. awke, auke, from Ice. Gfigr, Gfugr,
contrary; root af, off, away.
1. contrary; backward; hence, perverse, wrong, erroneous. [Obs.]
2. not dexterous; unhandy; awkward;
clumsy. [Obs.] awk, awk/ly, adv. 1. awkwardly. [Obs.] 2. perversely; in the wrong way. [Obs.] awk/ward, a. [ME. awkwarde, from awk-, off, and -ward; AS. -weard; same root as L, vertere, to turn.] 1. hard to handle; inconvenient to use; un- wieldy. 2. ungainly; ungraceful in manners; clumsy. 3. inopportune; embarrassing; as, an awk- ward situation. 4. inconvenient; uncomfortable; cramped; as, an awkward position. 5. unfavorable; untoward; adverse; unfor- tunate. [Obs.] Syn.—clumsy, uncouth, unhandy, gling., ungainly, unskillful, rough. awk/ward age, early adolescence, character- ized by rapid growth, awkward behavior, and emotional instability. awk’wărd-ly, adv. clumsily; in a bungling man- ner; inelegantly; badly; uneasily. awk/ward-ness, n. clumsiness; ungracefulness in manners; want of dexterity in the use of the hands or instruments; unsuitableness; embarrassment. awl, n. [ME. aul, awel; AS. æl, awel, an awl.) a small, pointed tool for jercing holes in leather, wood, and other soft materials. It is made in various shapes for special uses.
bun-
TYPES OF AWL A. peg awl; B, sewing awl
aw’less, a. same as aweless. aw’less-ness, n. same as awelessness. awl’-shaped (-shapt), a. 1. having the shape of an awl. 2. in botany, subulate; tapering to a point. awl/wort, n. a small water plant of the mustard fa Subularia aquatica: so called from its awl-shaped leaves, which grow in clusters — around the root. awm, aum, n. same as cam. ; awn, n. [ME. awne, agun, from Ice. ögn, chaff] the beard of grain or grass; lende sharp 5 bristles on the head of barley, oats, a awned, a. in botany, furnished with awns. awn/ing, n. [Fr. auvent, a penthouse; āwan, anything suspended; origin uncer 1. a piece of canvas stretched over to shelter from the sun’s rays, the | the wind: originally employed as a a vessel's deck, or a boat, but now various other purposes, as before wit _2. that part of the poop deck wh aed forward, beyond the bulkhead of cabin. i ~ R awn/inged, a. equipped with an awn/less, a. without awn or beard. awn’y, a. having a:
sional past participle
a-w6k’en, obsolete past A. W. O.
often pro:
: ; ; ; } :
_ proof.
==== jack ====
a union jack.
17. in electricity, a plug-in receptacle used to make electric contact.
18, a drinking vessel holding less than a pint, [Brit. Dial.] g
19. any of several fishes, especially the pike, the pike perch, and the Californian rockfish.
20. in textile manufacturing, a creel; in cot- ton spinning, a machine which twists the strand as it leaves the carding machine.
builders’ E a seat or brace used to sup- port a workman while repairing a building.
every man jack; every man; everyone. hydraulic jack; a lifting jack in which the power is obtained by the action of a force pump upon a liquid confined in a cylinder. Jack Ketch; [after a famous public execu- tioner in England, ?-1686.] an official hang- man; a public executioner. [Brit.] jack, v.t. 1. to raise by means of a jack. 2, to hunt or fish for with a jack lamp. to jack up; (a) to raise by means of a jack; 3 iCeltoa,) to raise (prices, salaries, etc.); c) [Collog.] to reproach for misbehavior or neglect; to encourage to duty. jack, v.74. to hunt or fish with a jack lamp. E a. TE of some animals; as, jack rabbit. ack, n. [ME. jakke; OFr. jaque; Sp. jaco; prob. from Ar. shakk.) E pee P
1. asleeveless coat, usually of leather, worn by a medieval foot soldier.
2. a drinking mug of leather.
jack, n. [Port. jaca; Malay chakka.]
1. an East Indian tree like the breadfruit.
2. its large, heavy fruit, which has tasteless pulp and edible seeds.
_ 3. its wood.
jack, n.a Jacqueminot rose. [Colloq.]
jack-, [see jack (a man, boy, etc.).] a combining form meaning: (a) male, as in jackass, jack- daw; m large or strong, as in jackboot, jack- knife; (c) boy, fellow: used in hyphenated compounds, as jack-in-the-box.
Jack Ad’Ams, a simple fellow. [Brit. Dial.]
```


## [2026-09-04T22:54:10.038Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '101580,101610p' WEB_vol1.txt"
}
```


### [2026-09-04T22:54:10.092Z] TOOL RESULT

```
10. a jack rabbit.
11. a jackdaw.
12. a male salmon.
13. money. [Slang.] :
14. in games, 9 a playing card with a page boy’s picture on it; a knave; (b) a small ball used as the center mark in bowling; (c) one of the small metal pieces or stones used in playing jackstones.
LIFTING JACK
jack/ass, n.
Digitized by Arya Samaj Foundation Chennai and eGangotri
1. a yellowish-gray, meat-eating wild dog of Asia and northern Africa, smaller than the wolf: it runs in packs and hunts its prey at night.
JACKAL (Canis aureus)
2. a person who does low or dishonest, work for another: from the notion that the jackal hunts game for the lion and eats the leavings.
3. a person who cheats or swindles in a mean, underhanded way.
jack’/a-napes, n. (earlier Jack a Napes, as if
Jack of Naples; refashioning of Jack Napes, nickname of William de la Pole, Duke of Suf- folk (d. 1450), whose badge was a clog and a chain like a tame ape’s.]
1. formerly, a monkey. i 2. a conceited, insolent, presumptuous fel- ow.
3. a pert, monkeylike, mischievous child. 1. a male donkey. 2. a stupid or foolish person; a nitwit.
jack’bọọt, n. a heavy, sturdy boot that reaches
above the knee: also written jack bool.
jack/daw, n. a European black bird like the
crow, but smaller.
jack’et, n. [OFr. jaquette, dim. of jaque, a coat
of mail, a jack.]
1. a short coat, usually with sleeves.
2. an outer coating or covering, such as the removable paper cover of a book, the metal covering of a bullet, the insulating casing on a pipe or boiler, the skin of a potato, etc.
15. in hunting, (a) a torch or light used to Jack Frost, frost or cold weather personified.
attract game or fish at night; (b) the con- J
tainer holding the lighting fuel.
16. in navigation, a small flag flown on a
ack Horn/ér pie, a container shaped like a large pie, from which favors, trinkets, etc. are pulled at a party.
ship's bow as a signal or to show nationality; jack-in-a-box, 7.; pl. jack-in-A-box’es, 1.a
a union jack.
```


## [2026-09-04T22:54:12.544Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '101560,101580p' WEB_vol1.txt"
}
```


### [2026-09-04T22:54:12.604Z] TOOL RESULT

```
aç'à-mär, n”. [S. Am.}a brilliant tr en bird resembling the kingfisher long. slender bill. ; A ja-çå-na’ (zhä-så-nä’), n. [Port., from Tuy canam, jassanem.] a bird of South America and In- dia, with long toes that enable it to walk on the leaves of water plants. Jaçå-ran’då, n., [Braz.} 1. a genus of bignonia- ceous trees, including the ‘rosewood. 3 f 2. [j-} a tree of this g nus; also, certain trees of other genera resembling the rosewood. a jacaré,
j j
j
j
j
jacconet
aç'çönet, n. same as jaconet, “cent, a. [L. jacens (entis), ppr. of jacere, to jie. |lying at length; recumbent; prone, {Rare.] a/cinth, n. (ME. jacinte, jacinct; OFr. tacinte, jecinct; L. hyacinthus, à hyacinth.] J
1. a reddish-orange precious stone, a vari- ety of zircon; a hyacinth.
2, a reddish-orange color. ac-i-ti/ra pälm, (pam), [S.Am. jacitara, and Eng. palm.) a South American palm with hooked spines at the ends of the leaves, valued for its fiber; the Desmoncus macroacanthus. ack, n. [ME. Jacke, Jake; OFr. Jaque, Jaques; LL Jacobus; Gr. Iakobos, from Heb. ya'aqöb, Jacob, lit., seizing by the heel, a supplanter. From the nickname pene used for a servant or boy who made himsel generally useful, it is applied to lifting instruments.]
1. [often J-] originally, a common fellow or boy assistant.
2. {often J-) a man or boy; a fellow.
3. {often J—] a sailor; a jack-tar.
4. a lumberjack. 7
5. [sometimes J-] a worker at odd jobs; a jack-of-all-trades.
6. a bootjack. 2
7. a device for turning a roast; a kitchen
jack. y x 8. any of various machines used to lift, hoist, or move something
heavy a short distance; as, a jackscrew, hydraulic jack, au- tomobile jack, etc. :
9. a male donkey; a jack-
ass.
10. a jack rabbit.
```


## [2026-09-04T22:54:21.060Z] TOOL CALL #91: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%DA%A9",
 "prompt": "Is there a Persian entry جک (jak)? Give its etymology and meaning (e.g. 'jack, lifting device', borrowed from English/French). Quote whatever the page says for Persian."
}
```


## [2026-09-04T22:54:24.019Z] TOOL CALL #92: Bash

```json
{
 "command": "curl -s \"https://fa.wiktionary.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&titles=%D8%AC%DA%A9\" | python3 -c \"import sys,json;d=json.load(sys.stdin);[print(p.get('extract','')[:1500]) for p in d['query']['pages'].values()]\"; echo \"=== abadis ===\"; curl -s -A \"Mozilla/5.0\" \"https://abadis.ir/fatofa/%D8%AC%DA%A9/\" | python3 -c \"\nimport sys,re,html\nt=sys.stdin.read(); t=re.sub(r'<script.*?</script>','',t,flags=re.S); t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t); t=re.sub(r'\\s+',' ',t); print(t[:1500])\""
}
```


### [2026-09-04T22:54:27.874Z] TOOL RESULT

```
# Persian Entry: جک (jak)

Yes, there is a Persian entry for جک (jak) with multiple etymologies and meanings:

**Etymology 1:** Borrowed from English *jack*
- Meaning: "jack" (the definition requires clarification according to the source)

**Etymology 2:** Originally a churning pot
- Meaning: In Dari dialect, a "jug"
- Synonym listed: پارچ (pârč)

**Etymology 3:** Borrowed from English *Jack*
- Meaning: A male given name, the Persian equivalent of the English name Jack

The page notes that جک derives from a long etymological chain beginning with Biblical Hebrew עָקַב, passing through Ancient Greek, Latin, French, Middle English, and finally English before entering Persian.
```


### [2026-09-04T22:54:31.973Z] TOOL RESULT

```
(~.)


== فارسی ==


=== ریشه‌شناسی ===
انگلیسی


=== اسم ===
دستگاهی به شکل اهرم که برای بالا بردن و نگاه داشتن اشیاء سنگین مانند اتومبیل و غیره به کار برند.


==== منابع ====
فرهنگ لغت معین
(جَ)


=== اسم ===
چک:
برات.
شب پانزدهم ش عبان، شب برات.


==== منابع ====
فرهنگ لغت معین


==== برگردان‌ها ====

انگلیسی
jack
screw jack
jackscrew
=== abadis ===
 جک - معنی در دیکشنری آبادیس @font-face{font-family:"MsYekan";font-display:swap;src:url("/libs/font/web_yekan.woff")}:root{--clr-f5f:#f5f5f9;--clr-f8f:#f8f8f8;--clr-f6f:#f6f6f6;--clr-fff:#fff;--clr-eee:#eee;--clr-aaa:#aaa;--clr-ccc:#ccc;--clr-bbb:#bbb;--clr-e2e:#e2e2e2;--clr-666:#666;--clr-444:#444;--clr-333:#333;--clr-222:#222;--clr-7e1:#7e1975;--clr-598:#4467a5;--clr-ded:#dedfe1}.NM:root{--clr-f5f:#444;--clr-f8f:#444;--clr-f6f:#666;--clr-fff:#444;--clr-eee:#333;--clr-ccc:#333;--clr-aaa:#222;--clr-bbb:#222;--clr-e2e:#666;--clr-444:#bbb;--clr-666:#aaa;--clr-333:#333;--clr-222:#fff;--clr-7e1:#333;--clr-598:#bbb;--clr-ded:#444}html{background-color:var(--clr-fff);color:var(--clr-444);font-size:14px;height:100%}html.DK{font-size:15px;background-color:var(--clr-f5f)}body{font-family:MsYekan;line-height:1.8;margin:0;direction:rtl;overflow-x:hidden;height:100%;border-top:solid 3px var(--clr-7e1)}.NM body{background-color:var(--clr-fff)}body,div,input,textarea,select,label{box-sizing:border-box}input[type=text],input[type=password],textarea,select{border:solid 1px var(--clr-ccc);background-color:var(--clr-f6f);color:var(--clr-444);font-family:MsYekan;font-size:95%;padding:10px;margin:0;width:100%;margin-top:-1px}select option{font-family:MsYekan,Tahoma}.anaTermMean input[type=text]{width:80%!important;height:30px;vertical-align:top;display:table-cell}textarea{height:calc(40vh);max-height:180px}.DK textarea{height:200px;max-height:200px}textarea#rpNote{height:120px}textarea#cmHrefs{h
```


## [2026-09-04T22:54:37.744Z] TOOL CALL #93: Bash

```json
{
 "command": "sed -n '1,200p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-04T22:54:37.787Z] TOOL RESULT

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


## [2026-09-04T22:54:53.536Z] TOOL CALL #94: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82epo|page 60 root Apo: PIE *h2epo 'off, away', derivatives *h2ep-tero-, *h2ep-s, Germanic/Latin/Greek descendants\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%B3|page 60 node 5: Persian pas < MP pas < OP pasa, PIIr *pascaH, cites MacKenzie CPD p.65\" \\\n \"https://www.etymonline.com/word/awkward|page 60 nodes 1-2: awkward < ME awk < ON afugr < PGmc *afug- < PIE *apu-ko- from *apo-\" \\\n \"https://www.etymonline.com/word/evening|page 60 nodes 1-2: evening < OE aefnung < aefen < PGmc *aebando-, 'of uncertain origin' (not from *apo)\" \\\n \"https://www.etymonline.com/word/James|page 60 entry 3: James < LL Jacomus altered from Jacobus; Jacob < Gk Iakobos < Heb Ya'aqobh from 'aqebh 'heel'; OF Jacques a diminutive of Iacobus\" \\\n \"https://en.wiktionary.org/wiki/Jack|page 60 node 9: English Jack primarily from ME Jakke/Jankyn, dim. of Jan/John, not from Jacques\" \\\n \"https://en.wiktionary.org/wiki/%D8%B9%D9%82%D8%A8|page 60 node 2: Arabic root ʿ-q-b, ʿaqb/ʿaqib 'heel', Persian عقب borrowed from Arabic\" \\\n \"https://en.wiktionary.org/wiki/%D7%99%D7%A2%D7%A7%D7%91|page 60 node 3: Hebrew Ya'aqov from imperfect of ʿaqav, rel. to ʿaqev 'heel'\" \\\n \"https://en.wiktionary.org/wiki/post#Latin|page 60 node 7: Latin post < Proto-Italic *posti; pono < po- + sino\" \\\n \"https://en.wiktionary.org/wiki/%D8%AC%DA%A9|page 60 node 10: Persian جک jak borrowed from English jack (lifting device)\" \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done"
}
```


### [2026-09-04T22:54:59.997Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b7f498ada24f2c46.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8bc6990acceaeb00.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b8ae7d3d5d56efee.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/54fe9ee487690b30.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e5806bc592c1d105.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/231dc797616008a1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/06e9133efe1f6577.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/124562513bac7795.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/246d8e3ced5a4c2d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8f39572513a49eaa.txt
```


## [2026-09-04T22:55:10.480Z] TOOL CALL #95: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/indoeurop.html",
 "prompt": "Find the entry for the root \"apo-\" and quote it in full, including all numbered subsections (Germanic *af, *aftar-, *afug-, Latin ab, Greek apo, and the *po(s) section with Latin post and ponere). Also say whether EVENING appears under apo-."
}
```


## [2026-09-04T22:55:12.167Z] TOOL CALL #96: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DC%A5%DC%A9%DC%92",
 "prompt": "Is there a Syriac entry ܥܩܒ (ʿqab)? Give the verb's meaning ('to follow, track, investigate') and the noun ܥܩܒܐ (ʿeqbā 'heel'), plus any Proto-Semitic reconstruction and cognates."
}
```


### [2026-09-04T22:55:14.832Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T22:55:20.883Z] TOOL RESULT

```
# The Entry for "apo-"

Here is the full entry for **apo-**:

"Also ap-. Off, away. Derivatives include [off](/word/search.html?q=off), [ebb](/word/search.html?q=ebb), [awkward](/word/search.html?q=awkward), [puny](/word/search.html?q=puny), and [compote.](/word/search.html?q=compote.)"

The entry contains seven numbered subsections covering Germanic forms (*af, *aftan-, *afug-), Latin (ab-, post-), Greek (apo-), and an extended discussion of *po(s) with numerous Latin derivatives including post-, pōnere, and related words.

**Does EVENING appear under apo-?**

No, EVENING does not appear in the apo- entry. The derivatives listed are: off, ebb, awkward, puny, compote, and various compounds with Latin post- and ponere-, but evening is not among them.
```


## [2026-09-04T22:55:23.885Z] TOOL CALL #97: WebSearch

```json
{
 "query": "Syriac ʿqab ܥܩܒ \"to follow\" ʿeqbā heel Proto-Semitic ʿaqib"
}
```


### [2026-09-04T22:55:25.717Z] TOOL RESULT

```
Web search results for query: "Syriac ʿqab ܥܩܒ "to follow" ʿeqbā heel Proto-Semitic ʿaqib"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T22:55:33.456Z] TOOL CALL #98: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%A2%D7%A7%D7%91",
 "prompt": "List all language sections on this page (Hebrew, Aramaic/Syriac). For Aramaic/Syriac ܥܩܒ / עקב give the meanings ('heel', 'to follow, track') and the Proto-Semitic root reconstruction if given."
}
```


### [2026-09-04T22:55:39.139Z] TOOL RESULT

```
# עקב (Hebrew and Aramaic)

## Hebrew

**Noun (עָקֵב - akév):**
- "heel"
- "trace" or "footprint"

**Preposition (עֵקֶב - ékev):**
- "following," "because of," or "due to"

**Verb (עָקַב - akáv):**
- "to follow, tail, track, trace"
- "to watch, observe"
- "to pay attention"

## Aramaic

**Verb (עקב):**
- "to search, investigate"
- "to trip" (literally "to hold by the heel")

### Etymology
The word relates to Arabic عاقب, meaning "to guard, follow at the heel," reflecting a shared Semitic root (ע־ק־ב).
```


## [2026-09-04T22:55:47.198Z] TOOL CALL #99: Bash

```json
{
 "command": "for u in \\\n \"https://www.ahdictionary.com/word/indoeurop.html|page 60 root Apo and nodes 1,3,7: AHD/Watkins apo- entry (Germanic *af/*aftar-/*afug-, Latin ab, Greek apo, *po(s) with Latin post and ponere); EVENING not listed\" \\\n \"https://en.wiktionary.org/wiki/%D7%A2%D7%A7%D7%91|page 60 entry 3: Hebrew/Aramaic root ʿ-q-b, noun ʿaqev 'heel', verb 'to follow/track', Aramaic 'to search, investigate'\" \\\n \"https://fa.wiktionary.org/wiki/%D8%AC%DA%A9|page 60 node 10: fa.wiktionary جک 'انگلیسی' lever device for lifting, sourced to Farhang-e Mo'in\" \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -1; done"
}
```


### [2026-09-04T22:55:49.864Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3735d75498a331a4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e5bd8d8d586e0b83.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/85863ce51dbedc0f.txt
```


## [2026-09-04T22:56:06.034Z] TOOL CALL #100: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== RCH aqib ==\"; grep -on \"'akib[^\\n]\\{0,120\\}\\|akib, [^\\n]\\{0,120\\}\" RCH.txt | head -5; echo \"== RCH pas ==\"; grep -on \"pas, [Bb]ehind[^\\n]\\{0,120\\}\\|pas, [Aa]fter[^\\n]\\{0,120\\}\" RCH.txt | head -5; echo \"== PHN/DEV Jacques ==\"; grep -c \"Jacques\" PHN.txt DEV.txt LKT.txt; echo \"== MON ژاکلین ==\"; grep -n \"ژاکلین\" MON_part1.txt MON_part2.txt | head -3; echo \"== BQT عقب ==\"; grep -c \"عقب\" BQT_v2_pages.txt"
}
```


### [2026-09-04T22:56:08.229Z] TOOL RESULT

```
== RCH aqib ==
91231:akib,  Bcdiind,  after,
== RCH pas ==
== PHN/DEV Jacques ==
PHN.txt:0
DEV.txt:0
LKT.txt:1
== MON ژاکلین ==
== BQT عقب ==
9
```


## [2026-09-04T22:56:11.414Z] TOOL CALL #101: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '91228,91236p' RCH.txt; echo \"== RCH pas persian ==\"; grep -on \"pas, [^\\n]\\{0,140\\}\" RCH.txt | head -8; echo \"== LKT Jacques ==\"; grep -on \"Jacques[^\\n]\\{0,200\\}\" LKT.txt | head -2"
}
```


### [2026-09-04T22:56:13.236Z] TOOL RESULT

```
curved.  I.ed  away  from  water.
A   Split.  Dissipated,  dispelled  (cloud).  (liiglit-
niiig)  vibrating  like  a   sword.
A   k-  min  ^akib,  Bcdiind,  after,
A   JoiAXc  mun^fikidy  Tied;  bound.  Agreed  upon,  concluded (j)eace,  marriage,  bargain,  and  the  like).
AjLtx<  imuuakiry  AVounded  in  the  feet  (camel  or  horse  with  a sword),  (iul  off.  Cut,  lopped  (a  palm-tree).  Detained,  bound.
A   ^j>SsXX<.  mutiuikisy  inverted,  placed  topsy-turvy,  reverse<l (as  a   figure  in  a   mirror),  contrary,  inverse.
A   nmnuikify  (’iirled  (hair).
A   mutual  (andtdixA.^  man^nlat)y  Hard  ground.  Mun^ify Torn  from  iIk;  panmt  stock  (a  palm-sucker).  (A  horse)  marked with  while  in  the  hinder  part  of  the  pastern.  Mtina^^ly  Shod with  shoes  or  slippers.  Hard-hoofed  (horse).
== RCH pas persian ==
69119:pas,  Fine  linen.  i
== LKT Jacques ==
5011:Jacques  v.  Beauvais  929
```


## [2026-09-04T22:58:13.383Z] AGENT

Now I'll write the verification file.


## [2026-09-04T23:03:16.192Z] TOOL CALL #102: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /home/sfmqrb/git/rishe/data/verification/page-60.json <<'JSONEOF'\n{\n  \"pdf_page\": 60,\n  \"book_page\": 30,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Apo, Apâ, Apu, Pu 3, Pô 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂epo (*apo, with ablaut/enclitic variants *apā, *ap-u, *pu, *po) 'off, away, from'\",\n      \"note\": \"Pokorny IEW 53-55 heads the entry 'apo- (pō̆, ap-u, pu) \\\"ab, weg\\\"', i.e. exactly the five shapes Nourai lists (his 'Apâ' = the long-vowel variant apā, 'Pô 1' = Pokorny's po, 'Pu 3' = Pokorny's pu). Language label (Indo-European) and gloss ('off') are right; the current reconstruction writes it *h₂epó, though Hittite āppa is used to argue for laryngeal-less *apo. The whole Latin/Greek/Iranian half of the chart hangs on Pokorny's own remark under *pos that it is 'probably *p + os, Gen.-Abl. to *apo above S. 53 f.', so the root→#3 arrow is Pokorny's, not Nourai's invention. The single weak link on this chart is the item 'eben : later time, evening' in node #1 (and 'evening' in node #2): neither Pokorny nor Watkins/AHD puts the Germanic word for 'evening' under *apo, and Klein assigns it to *epi/*opi.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82epo\",\n        \"https://www.ahdictionary.com/word/indoeurop.html\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:53\", \"status\": \"supports\", \"note\": \"POK_01.txt 0-based leaf 61 = printed p.53 (leaf 62 carries the running number '54'): the entry 'apo-, (pō̆, ap-u, pu) \\\"ab, weg\\\"' runs pp. 53-55 and contains 'got. af Präf. und Präp. m. Dat. \\\"von, von—weg\\\" ... ags. æf, of, as. af, ahd. aba', 'Ableitungen: apo-tero-, ap-ero-, ap-io-, ap-öko-', 'ags. *afoc in engl. awkward, aus *apu-ko-s', and closes 'S. noch idg. *po-ti und *po-s' — exactly the material Nourai's chart draws.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Germanic\",\n          \"words\": \"af; apo-tero; eben; afug\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Three of the four items are straight reflexes of *apo. (a) 'af' = Proto-Germanic *ab/*af, unstressed preposition/prefix from PIE *h₂epo with regular loss of the final vowel: Gothic af, Old Norse af, Old English of/æf, Old Saxon af, OHG aba/ab- (POK 53; AHD apo- 1a). (b) 'apo-tero' is in fact the PIE comparative *ap(o)-tero- 'further off' (Skt. apataram, OP apataram, Gk. apōtérō), which in Germanic gives *aftar-/*after- > OE æfter, ON eptir, Goth. aftra (AHD apo- 4). Labelling the comparative itself 'Germanic' is a small imprecision, since the formation is PIE, not Germanic. (c) 'afug' = Proto-Germanic *afug-/*abuh- < *apu-ko- 'turned away', whence ON ǫfugr/afugr 'turned backwards', OS avuh, OHG abuh, OE *afoc (POK 54; AHD apo- 6). (d) 'eben : later time, evening' is the problem: this is Proto-Germanic *ēbanþ-/*ēbando- 'evening' (OE ǣfen, OS āƀand, OHG āband, ON aptann). Klein derives it not from *apo but from *epi/*opi — 'cogn. with Gk. ὄπι- in ὄπισθε(ν) \\\"after, behind\\\", ὀψέ \\\"late in the day\\\" ... hence evening lit. means \\\"the hinder (= latter) part of the day\\\"' — and Etymonline calls Proto-Germanic *æbando- 'of uncertain origin'. Neither Pokorny's apo- entry nor Watkins/AHD lists the word. Hence 'disputed' for this one item only.\",\n          \"sources\": [\n            \"https://www.ahdictionary.com/word/indoeurop.html\",\n            \"https://www.etymonline.com/word/awkward\",\n            \"https://www.etymonline.com/word/evening\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. 'apo-. Also ap-. Off, away.': '1. Germanic *af in: a. Old English of, æf (> Middle English of, of-), off: OF, OFF ... 4. Suffixed (comparative) form *ap(o)-tero- in Germanic *aftar- in Old English æfter, after, behind: AFTER ... 6. Suffixed form *apu-ko- in Germanic *afug- in Old Norse ǫfugr, turned backward: AWKWARD.' — supports af, apo-tero and afug verbatim, but the entry has no 'evening' item (the AHD index line reads 'EVEN oi-no-', 'EVENTIDE da-'); the current online AHD apo- entry likewise lists only off, ebb, awkward, puny, compote.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Bd. I pp. 53-55 (POK_01.txt leaves 61-63)\", \"stance\": \"partial\", \"note\": \"'got. af ... ags. æf, of ... ahd. aba, ab-'; 'Ableitungen: apo-tero-'; 'ags. *afoc in engl. awkward, aus *apu-ko-s (oder aus *opu-ko-s: ὄπισθεν ...)'. No Germanic word for 'evening' anywhere in the entry; Pokorny even warns that for the Germanic aft-/eft- group 'steht aber auch Verwandtschaft mit gr. ὄπισθεν, idg. *epi, *opi zur Erwägung'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I pp. 47-49 (WLD_Bd1_pages.txt leaves 55-57), s.v. 'apo, po'\", \"stance\": \"partial\", \"note\": \"'got. af Praef. und Praep. m. Dat. \\\"von, von—weg, von—her\\\", anord. af Adv. und Praep. m. Dat., ags. æf, of, as. af, ahd. aba, ab- \\\"von, von—weg\\\", nhd. ab-.' Same Germanic list; again no 'evening'.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 300 ≈ p.576, s.v. even, n., 'evening'\", \"stance\": \"contradicts\", \"note\": \"'even, n., evening (poet.) — ME. eve, even, fr. OE. æfen, rel. to OS. āƀand, ON. aptann, Dan. aften, OFris. evend, Du. avond, OHG. aband, MHG. abend, G. Abend, and cogn. with Gk. ὄπι- in ὄπισθε(ν) ... ἐπί \\\"upon, after\\\"; hence evening lit. means \\\"the hinder (= latter) part of the day\\\". See epi-.' Klein puts the word under *epi, not *apo.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. awk, awkward\", \"stance\": \"supports\", \"note\": \"'awk, a. [ME. awke, auke, from Ice. ǫfugr, ǫfugr, contrary; root af, off, away] 1. contrary; backward ...' and 'awkward, a. [ME. awkwarde, from awk-, off, and -ward]' — Webster ties afug- to the same root af/off.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt leaf 31 = pp.29-30, s.v. apo, apomos, apetios\", \"stance\": \"supports\", \"note\": \"'apo (apo, apo, po) \\\"away; from, after\\\". WP I, 47 ... Go. af; OHG aba \\\"away; from\\\", abo \\\"but\\\"; OE of; ON af' — Mann has the same Germanic material under *apo.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"English\",\n          \"words\": \"of, off; after; evening; awkward\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"of/off: one Old English word of/æf split in Middle English into the unstressed preposition 'of' and the stressed adverb 'off' (spelling differentiated only from the 16th c.); < PGmc *af < *h₂epo. after: OE æfter (adv./prep.) < PGmc *aftar- < the PIE comparative *ap(o)-tero-, i.e. 'further away/behind'. awkward: mid-14c. awkeward 'in the wrong direction', from ME awk 'back-handed, turned the wrong way' (a Norse loan, ON ǫfugr < PGmc *afug- < *apu-ko-) plus the adverbial suffix -ward; sense 'clumsy' from the 1520s, 'embarrassed' from c.1713. evening: OE ǣfnung, a verbal noun to ǣfnian 'to grow toward evening', from ǣfen 'evening' < PGmc *ēbando- — this last word is exactly the disputed item: Etymonline says the Proto-Germanic form 'is of uncertain origin' and stops there, Klein takes it to *epi/*opi 'after, behind', and no modern IE dictionary files it under *apo. The other three items are secure.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/awkward\",\n            \"https://www.etymonline.com/word/evening\",\n            \"https://www.ahdictionary.com/word/indoeurop.html\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"the English box carries no citation of its own in the book; it inherits the AHD reference of its parent node #1, which was checked there.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 300 (≈ p.576), s.vv. even 'evening', evening, evensong\", \"stance\": \"contradicts\", \"note\": \"'evening, n. — ME., fr. OE. æfnung, \\\"evening\\\", prop. verbal n. fr. æfnian, \\\"to become evening\\\", fr. æfen, \\\"evening\\\". See even, \\\"evening\\\"' — and 'even, evening' is referred to epi-, not to apo-.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. awkward\", \"stance\": \"supports\", \"note\": \"'awkward, a. [ME. awkwarde, from awk-, off, and -ward; AS. -weard ...]' — English awkward from awk 'off, away' (< ON ǫfugr).\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, index and s.v. apo-\", \"stance\": \"partial\", \"note\": \"index line 'AWKWARD apo-'; the apo- entry yields OF, OFF, AFTER, AWKWARD, EFTSOONS. 'EVENING' has no entry in the index at all and 'EVEN' is referred to oi-no-/septm.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Indo-European\",\n          \"words\": \"P-os, Pos : after, behind\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pokorny's headword *pos 'by, about, around, beside', which he himself analyses as 'probably *p + os, Gen.-Abl. to *apo above S. 53 f.' — i.e. an oblique case-form of the very root in the top box, which is exactly the arrow Nourai draws. Nourai's double writing 'P-os, Pos' renders that analysis (p + os). Reflexes: Arcado-Cypriot and Phrygian-Greek πος/πο-, Doric ποτί, Lithuanian pas 'at, by', OCS po 'after', and the -ti- and -kʷo- extensions that give Latin post and Indo-Iranian pasča-. Kent (Old Persian, Lexicon s.v. pasā) prefers a different parsing of the same material — 'pIE *po as in Lat. po-liō, positus, Gk. ἀπό, + *sekʷé, inst. to root noun from *sekʷ- \\\"follow\\\"' — but both analyses start from *(a)po, so the arrow stands either way.\",\n          \"sources\": [\"https://www.ahdictionary.com/word/indoeurop.html\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:841\", \"status\": \"supports\", \"note\": \"POK_full.txt line 68658: 'Root / lemma: pos — Meaning: by, about, around, beside — Note: probably *p + os, Gen.-Abl. to *apo above S. 53 f. ... References: WP. II 78 f., WH. II 347 ff. — Page(s): 841-842'. Exactly Nourai's node and its attachment to the root.\"},\n            {\"ref\": \"AHD:1506\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. apo-, item 7: '7. Possible root *po(s), on, in: a. Russian po ...; b. Latin post, behind, back, afterward: POST-, POSTERIOR ...; c. Latin pōnere, to put, place, from *po-sinere ...'. In the 1975/76 AHD appendix (pp.1505-1550) the alphabetically early root apo- falls on p.1506, so Nourai's page number fits; the *po(s) sub-entry is where AHD keeps this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II pp.78-79 (WLD_Bd2_pages.txt leaves 82-83)\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny II 78 f. is the reference Pokorny himself cites for *pos: 'Zu lit. pas auch pastaras \\\"der letzte, hinterste\\\" ... Ableitungen: 1. mit -ti ... lat. post, alat. poste \\\"nach, hinter\\\" ... 2. mit -qo- ai. paścā (Instr.) Adv. \\\"hinten, westlich, später\\\" = av. [pasča]'.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt leaf 31 = pp.29-30\", \"stance\": \"partial\", \"note\": \"Mann has no separate *pos headword here; he files the Iranian/Slavic 'behind, after' material partly under 'apo ... \\\"away; from, after\\\"' (with 'OCS po \\\"after\\\"') and partly under 'apetios (apətios, apotios) \\\"back, rear; last\\\"'. Same root, different segmentation.\"},\n            {\"src\": \"KNT\", \"where\": \"KNT.txt Lexicon p.194 s.v. pasā\", \"stance\": \"partial\", \"note\": \"'pIE *po as in Lt. po-liō, positus, Gk. ἀπό, + *sekʷé, inst. to root noun from *sekʷ- \\\"follow\\\" ...' — Kent derives the same forms from *po + *sekʷ- rather than from a gen.-abl. *p-os.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"pasča, pasca, pasâ : after, behind; paskât : from behind here\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan pasča (Nourai's 'pasca' is simply the undiacriticked spelling of the same word) 'behind, after', both local and temporal, is *pos + the adverbial -kʷo- suffix, matching Vedic paścā́ 'behind, westward, later'; Avestan paskāt (Vedic paścā́t) is the ablative of the same stem, 'from behind, coming up behind, thereafter' — Nourai's odd gloss 'from behind here' renders Bartholomae's 'von hinten her, hinterdrein'. Old Persian has pasā (never *pasča): the -č- was lost in the south-west Iranian dialect, so OP pasā stands beside Median/Avestan pasča, and OP builds the phrasal adverb pasāva 'after that, afterwards', which is the commonest adverb in the Bīsotūn inscription. Attested in the Yašts and Vidēvdād for Avestan (Yt.10.86, Yt.13.39, V.5.40) and DB 1.27 etc. for Old Persian.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D8%B3\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:842\", \"status\": \"supports\", \"note\": \"POK_full.txt, root 'pos', Page(s) 841-842, derivative 2: '2. -kʷo-: Old Indic paścā (Instr.) Adv. \\\"behind, westlich, later\\\" = Avestan pasča preposition \\\"behind, after\\\", ortlich and zeitlich, Old Indic paścāt (Abl.) preposition \\\"behind, after, westlich\\\", Avestan paskāt Adv. \\\"von hinten her, hinterdrein\\\" spacial and zeitlich'; derivative 3: 'In ending still controversial is ap. pasā \\\"after\\\", preposition ortlich and zeitlich'. All three of Nourai's forms, on the page he cites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW cols. 881-882 s.vv. paskāt, pasča\", \"stance\": \"supports\", \"note\": \"'j. paskāt Adv. 1) räumlich \\\"von hinten her, hinterher, hinterdrein\\\" ... 2) zeitlich \\\"darauf, alsdann\\\" ... Zum lat. post; idg. -ś- aus -śk-. Vgl. pasča ... Pü.: pas, pas hač'; and 'j. pasča \\\"post\\\"; 1) Adv.; a) räumlich, α) \\\"hinten\\\"'. Bartholomae also records the Pahlavi rendering pas.\"},\n            {\"src\": \"KNT\", \"where\": \"Old Persian, Lexicon p.194 s.vv. pasā, pasāva\", \"stance\": \"supports\", \"note\": \"'pasā prep. \\\"after\\\", temporal with acc. and local with gen.: Av. pasča, NPers. pas, Skt. paścā ... The s in pasā is OP for Med. šč, Av. sč, from pAr. ść.' And 'pasāva phrasal adv. \\\"after that, afterwards\\\": pasā + asn. ava' (DB 1.27, 30, 32 ...). Kent even gives the OP → NPers. line Nourai draws next.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p.79\", \"stance\": \"supports\", \"note\": \"'2. mit -qo- ai. paścā (Instr.) Adv. \\\"hinten, westlich, später\\\" = av. [pasča]'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"pas «پس ۱» : after\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Persian pasā 'after, behind' > Middle Persian pas [ps] 'then, afterwards, behind' (MacKenzie, CPD p.65; Nyberg, Manual II s.v. pas, with the by-form pasēh) > New Persian پس pas. The chart's extras are the regular family: پسین pasīn 'last, final' continues MP pasēn [psyn'] (Mo'in's own footnote in Borhān-e Qāṭeʿ derives it 'مرکب از: پس + ین ... و پهلوی pasēn'); واپسین wāpasīn is پسین with the prefix wā- 'back'; پسوند pasvand '(grammatical) suffix' and پس‌انداز pas-andāz 'savings' are modern compounds of the same adverb. Note that Persian pas is a south-west Iranian continuation of OP pasā, not of Avestan pasča: Hübschmann stresses that OP already had pasā 'without *pasča or the like beside it'.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D8%B3\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:70\", \"status\": \"supports\", \"note\": \"HRN.txt 0-based leaf 91 = printed p.70, numbered entry 315: '315. pes \\\"hinter, nachher\\\", pesīn \\\"letzter\\\". ... ap. pasā \\\"hinter\\\", pasāva \\\"nachher\\\"; aw. pasča \\\"nach\\\", paskāt \\\"nachher, hinter\\\", pasne \\\"hinter\\\"; phlv. paš, pasīn \\\"letzter\\\"; ai. paścā \\\"hinter, nachher\\\", paścāt \\\"von hinten, hernach\\\".' Horn's entry is Nourai's node and its parent in one line, and it also covers the extra پسین.\"},\n            {\"ref\": \"BQT:403\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt \\\\f-leaves 627-630 = printed pp. ~402-405 (fixed by the continuation notes: leaf 630 ends 'بقیه در صفحهٔ ۴۰۷' and leaf 631 carries 'بقیه از صفحهٔ ۴۰۵'). Leaf 627 has «پس ۱ [به فتح اول و سکون ثانی] مخفف پسر است که در مقابل دختر باشد» and, lower down, «پس ۲» with Šāhnāma verses, plus پسا، پساچین، پس‌افتاده «... و بمعنی پس‌انداز و ذخیره», پس‌افکندن. So Nourai's page is right to within one leaf, and it does carry both the headword پس (with the homonym numeral he reproduces) and the derivative پس‌انداز. Mo'in's etymological footnote 6 on leaf 630 reads «پسین - بفتح اول. مرکب از: پس + ین (پسوند نسبت) [پهلوی pasēn] (فرجامی، آینده)؛ آخرین، اخیر، خلاف پیشین».\"},\n            {\"ref\": \"IEC:29\", \"status\": \"partial\", \"note\": \"IEC.txt leaf 31 = printed pp.29-30 (running head 'aperos — aps'): 'apetios (apətios, apotios) \\\"back, rear; last\\\". Cf. apo, opi — Skt. apatyam \\\"progeny\\\"; Av. apąš, apaδa; Per. pas (aphetic? or to poti, q.v.); Hitt. apezis ...; Gk. cf. áps; OE OS cf. eft \\\"back, again\\\"; Li. apačià \\\"base, foot\\\".' Mann has Persian pas on exactly the cited page and under *apo, but by a different intermediate (*apetio-) than Nourai's *pos, and he flags it as uncertain.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.65\", \"stance\": \"supports\", \"note\": \"'pas [AHL, BATL, ps | = M, N ~] then, afterwards, behind'; and p.65 'pasēn [psyn' | N pasin] final, last.' The Wiktionary entry for پس cites this same page.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary s.vv. pas, pasēn (NYB_vol2_glossary.txt lines 2980-2985)\", \"stance\": \"supports\", \"note\": \"'pas [PHL; BʿTL], with -c: pas-ic, adv. 1. behind: bē raft hēnd ... Vahuman pēš, Zartuxšt pas ... hač ~ from behind ... 2. afterwards, then'; 'pasēn [psyn'] ultimate, final: tan ī ~'.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien, HUB.txt leaves 222 and 229 (≈ pp.212, 219)\", \"stance\": \"partial\", \"note\": \"'Hinter s ist ein Laut abgefallen in pas \\\"hinter\\\" = ap. pasā, vgl. zd. pasča, paskāt'; and 'Geschwunden ist č vielleicht in kas \\\"jemand\\\" = zd. kaścit, ap. kasciy. Vgl. pas \\\"hinter\\\" = zd. pasča (paskāt), dem aber schon im Ap. pasā (nicht *pasča u. dgl.) gegenübersteht.' Hübschmann insists the New Persian word continues OP pasā specifically, not the Avestan form.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi (MON_part1/part2 OCR)\", \"stance\": \"silent\", \"note\": \"the searchable OCR of the Moʿin lexicon volumes does not yield a clean headword hit for پس; Moʿin's etymological note is however reproduced in his footnotes to Borhān-e Qāṭeʿ, quoted above.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Sogdian\",\n          \"words\": \"`pyš, pš : then, afterwards\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian ʾpyš (Buddhist Sogdian, read opēš/opiš, with the by-forms ʾps-, pš-, pšy) and the prefixal/adverbial psʾ (pš-) 'then, after' both continue Old Iranian pasča directly: prothetic ʾ- (a-) before the cluster, -sč- > -š-, and the vowel raised to -ē-/-i- in the eastern Iranian development. Gharib's dictionary tags both entries '©Av. pasča'. Compounds on the same base are ʾpyšy 'after, behind', ʾpyšsʾr 'backwards', ʾpyštrw / pštrw 'later, then, afterwards'. Nourai's backtick renders the initial aleph.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:55,300\", \"status\": \"supports\", \"note\": \"Both page numbers are exact. SOD_pages.txt 0-based leaf 120 = printed p.55 (leaf 119 carries the numeral 54): entry '1403 ʾpyš B — opos, opis (ʾps-) ©Av. pasča ⇒ ps(-), pyš-1, psy — then, afterwards — GMS 179'. SOD_pages.txt leaf 366 = printed p.300 (numeral visible on the page): entry '7474 psʾ(-) M, C — pasa (pš-) ©<Av. pasča ©adv. & pref. ⇒ pšy, ʾpyš — then, after — GMS 179, 373, 1143; BBB p98'. Gharib derives both from Avestan pasča, which is Nourai's arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary nos. 1403, 1408, 1409, 7474, 7526\", \"stance\": \"supports\", \"note\": \"besides the two cited entries, 1408 'ʾpyšy — opišc? after, behind', 1409 'ʾpyšsʾr — opišc-sar, backwards', 7526 'pštrw — pastar(u), then, afterwards' — the whole family is derived from pasča.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW cols. 881-882 s.v. pasča\", \"stance\": \"supports\", \"note\": \"supplies the Avestan etymon that Gharib's Sogdian entries point to; Bartholomae's Pahlavi gloss 'pas, pas hač' shows the same simplification of -sč- in the Middle Iranian languages.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 841-842 s.v. pos\", \"stance\": \"supports\", \"note\": \"Pokorny's Iranian material is the same Avestan pasča/paskāt from which the Sogdian forms are drawn; no separate Sogdian citation, so 'supports' only indirectly.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Latin\",\n          \"words\": \"post : after; pônere : to place\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"post: from *pos-ti (the -ti extension of *pos, formed on the model of *anti > ante), Old Latin poste, whence by loss of final -e the classical post; cognates Oscan púst/post, Umbrian post/pus, and the derivatives posterus, postumus, posticus, and pōne < *posti-ne. pōnere: Ernout-Meillet's 'pōnō est issu de po-sinō > pozno > pōnō', i.e. the preverb po- (the zero-grade *po of *apo, as in po-liō, po-lūbrum, av. pa-zdayeiti) compounded with sinō 'let, place'; the old perfect posīuī/poslui and the participle positum still show the -s-. Its original sense was 'to set aside', generalised to 'to put, place'. Both words are put under this root by Watkins (AHD apo- 7b, 7c).\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/post#Latin\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. apo-, item 7: '... b. Latin post, behind, back, afterward: POST-, POSTERIOR; POSTMORTEM, PREPOSTEROUS, PUISNE, (PUNY); c. Latin pōnere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, COMPONENT, (COMPOSE), ... DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST ...'. Exactly Nourai's Latin box and the English box below it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, Dict. étym. lat. s.vv. *posti/poste/post and pōnō\", \"stance\": \"supports\", \"note\": \"'*postī, poste, post ... post est issu de *pos-ti (cf. ante de *anti); l'i en finale absolue a abouti à e (on a encore la forme poste dans Enn. A.330 poste recumbite)'; and 'pōnō, -is, poslui (puis posui), positum, pōnere. Pōnō est issu de po-sinō > pozno > pōnō ... Sens propre \\\"mettre à l'écart\\\".'\"},\n            {\"src\": \"POK\", \"where\": \"IEW 841 s.v. pos, derivative 1\", \"stance\": \"supports\", \"note\": \"'derivatives: 1. with -ti ... Latin post, Old Latin poste \\\"after, behind\\\", örtlich and zeitlich ... Latin pōne from *posti-ne'; and IEW 54-55 s.v. po: 'lat. po-situs, pōnō aus *po-s[i]nō, po-liō, po-lūbrum'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II pp.78-79\", \"stance\": \"supports\", \"note\": \"'lat. post, alat. poste \\\"nach, hinter\\\", örtlich und zeitlich ... davon lat. posterus, osk. pustrei, umbr. postra, lat. postumus ... umbr. postne, lat. pone aus *posti-ne'.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"postpone; oppose, propose, compose, impose, posture\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"postpone (15th c.) is a direct Latinism, postpōnere 'to place after' = post + pōnere, so it draws on both words in the parent box. The rest are the pōnere family, all reaching English through French or directly from Latin: oppose < Old French oposer (a French re-formation of Latin oppōnere on poser), propose < OF proposer (Lat. prōpōnere), compose < OF composer (Lat. compōnere), impose < OF imposer (Lat. impōnere); the -pose verbs owe their -pos- to Late Latin pausāre crossed with the pōnere compounds, which is why the nouns keep the Latin stem (opposition, composition). posture < French posture < Italian postura < Latin positūra 'position', from positus, the participle of pōnere.\",\n          \"sources\": [\"https://www.ahdictionary.com/word/indoeurop.html\"],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"the English box carries no citation of its own; it inherits the AHD reference of its parent node #7, checked there — AHD's apo- 7c lists COMPOSE, IMPOSE, OPPOSE, POSITION, POST etc. as derivatives.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. apo- 7c\", \"stance\": \"supports\", \"note\": \"the derivative list 'APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS...' covers every word in Nourai's box.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. pōnō\", \"stance\": \"supports\", \"note\": \"'Positio n'apparaît du reste qu'à l'époque impériale ... positūra (Lucr.) traduit θέσις' — the source of posture; and the compounds prōpōnō, compōnō, oppōnō, impōnō are listed there.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966 s.vv. compose, impose, oppose, posture\", \"stance\": \"supports\", \"note\": \"Klein routes all the -pose verbs through Old French -poser and back to Latin pōnere/positum, and posture through F. posture, It. postura, L. positūra.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"A`.q.b\",\n      \"verdict\": \"disputed\",\n      \"modern_form\": \"Common (Proto-)Semitic root *ʿ-q-b 'heel; to follow at the heel', not specifically Syriac\",\n      \"note\": \"The root itself is real and its gloss is right, but the language label is wrong in a way that inverts the chart. ʿ-q-b is inherited in every branch of Semitic: Akkadian eqbu/iqbu 'heel', Ugaritic and Hebrew ʿāqēb, Aramaic/Syriac ʿeqbā and the verb ʿqab 'to track, investigate', Arabic ʿaqib 'heel' and ʿaqaba 'to follow'. Nourai's own reference says so: Klein (p.823) derives Hebrew Yaʿăqōbh from Hebrew ʿāqēbh and lists 'Aram. ʿiqbā, Akkad. iqbu ... Arab. ʿāqib, ʿaqaba' as words it 'is rel. to' — cognates, not ancestors. Hebrew Yaʿăqōb is moreover attested in Bronze-Age Amorite/Egyptian form (yaʿqub-ʾil) a millennium before Syriac existed, so Hebrew cannot descend from Syriac. The one place where a Syriac source is genuinely defensible is the sub-claim Jeffery makes on the page Nourai cites: Arabic Yaʿqūb, the Qurʾānic name, probably reached Arabic from Syriac Yaʿqūḇ. A correct root box would read 'Semitic ʿ-q-b', with the Syriac→Arabic arrow restricted to the personal name.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D7%A2%D7%A7%D7%91\",\n        \"https://en.wiktionary.org/wiki/%D8%B9%D9%82%D8%A8\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:823\", \"status\": \"partial\", \"note\": \"KLN_1966.txt 0-based leaf 444 (its page numeral is 822; leaf 445 = 824-825), s.v. Jacob: 'Late L. Jacōbus, fr. Gk. Ἰακώβος, fr. Heb. Yaʿăqōbh, lit. \\\"one that takes by the heel\\\", a derivative of ʿaqēbh, \\\"heel\\\", whence ʿaqabh, \\\"he followed at the heel, he overreached, circumvented\\\", which is rel. to Aram. ʿiqbā, Akkad. iqbu, \\\"heel; trace, mark\\\", Arab. ʿāqib, \\\"heel\\\", ʿiqbah, \\\"mark, trace, sign\\\", ʿaqaba, \\\"he followed (at the heel), succeeded\\\".' The page number is exact and every form on Nourai's chart is there, but Klein's structure is Hebrew-internal with Aramaic/Akkadian/Arabic as cognates; he nowhere makes Syriac the source.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"a`.q.b : to follow; a`qeb : heel; Ya`qŭb : A prophet's name (follower, successor)\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The three items need to be separated. (a) The verb ʿaqaba (ʿ-q-b, form I) 'to follow, come after, succeed', with form II ʿaqqaba 'to pursue, to comment' and the verbal noun taʿqīb, and (b) the noun ʿaqib/ʿaqb 'heel; end; offspring' are inherited Arabic, the regular reflexes of the common-Semitic root; they are cognate with Syriac ʿqab/ʿeqbā, not borrowed from it, and Nourai's own reference (Klein) treats them as cognates. (c) The proper name يعقوب Yaʿqūb is a different matter: it is a foreign name in Arabic, and Jeffery, on the very page cited, concludes that it most likely came in from Syriac ܝܥܩܘܒ Yaʿqūḇ through Christian channels rather than directly from Hebrew — so for this word the Syriac→Arabic arrow is exactly right. The Arabic form Yaʿqūb with -ū- reflects the Syriac vocalisation, and it was already known to the pre-Islamic Arabs; Arab lexicographers themselves classed it as a loan (al-Jawālīqī, al-Khafājī, as-Suyūṭī).\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B9%D9%82%D8%A8\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:823\", \"status\": \"partial\", \"note\": \"KLN_1966 leaf 444-445 (p.823), s.v. Jacob: Arabic ʿāqib 'heel', ʿiqbah 'mark, trace, sign', ʿaqaba 'he followed (at the heel), succeeded' are listed, but as words the Hebrew 'is rel. to', i.e. cognates of a shared Semitic root — not as Syriac loans.\"},\n            {\"ref\": \"FVQ:291\", \"status\": \"supports\", \"note\": \"FVQ_pages.txt 0-based leaf 308, running head 'FOREIGN VOCABULARY OF THE QURʾĀN 291', entry Yaʿqūb: 'There were some who considered it as Arabic derived from [ʿaqiba], but in general it was recognized as a foreign word, cf. al-Jawālīqī, 155; Zam. on xix, 57; Baiḍ. on ii, 29; as-Suyūṭī, Muzhir, i, 138, 140; al-Khafājī, 215. Apparently it was known among the Arabs in pre-Islamic days. It may have come from the Heb. Yaʿăqōb, though the fact that Muhammad has got his relationship somewhat mixed might argue that he got the name from Christian sources, probably from the Syr. Yaʿqūḇ, which was the source of the name in the Manichaean fragments (Salemann, Manichaeische Studien, i, 86).' This is precisely Nourai's Syriac→Arabic arrow, for the name.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966 p.823 s.v. Jacob\", \"stance\": \"partial\", \"note\": \"gives the Arabic forms as cognates of Hebrew, not derivatives of Syriac (quoted above).\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary p.291\", \"stance\": \"supports\", \"note\": \"'probably from the Syr. ܝܥܩܘܒ' for the name Yaʿqūb.\"},\n            {\"src\": \"RCH\", \"where\": \"Richardson, Persian-Arabic-English Dictionary, s.v.\", \"stance\": \"supports\", \"note\": \"'A [ʿaqib] ʿaqib, Behind, after' — the Arabic noun in its adverbial use, the form Persian borrowed.\"},\n            {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen\", \"stance\": \"silent\", \"note\": \"grep for ʿaqib / Jakob turns up nothing: Fraenkel does not treat ʿ-q-b as an Aramaic loanword in Arabic, which is consistent with the root being inherited rather than borrowed.\"},\n            {\"src\": \"TAD\", \"where\": \"al-Unaysī, Tafsīr al-alfāẓ al-dākhila\", \"stance\": \"silent\", \"note\": \"no entry for عقب or يعقوب in the OCR text.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"aqab «عقب» : back, behind; Ya`qŭb «یعقوب» : Jacob\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both are ordinary Arabic loans into New Persian, taken over from the post-conquest religious and administrative vocabulary. عقب aqab (Arabic ʿaqb/ʿaqib 'heel, hind part') is used in Persian as a noun 'back part' and a preposition/adverb 'behind, after' (عقبِ خانه, عقب رفتن), displacing native پس in much modern usage. یعقوب Yaʿqūb is the Qurʾānic form of the patriarch's name, hence also a common Persian personal name. The chart's extras are the other Arabic derivatives of the same root that Persian took over ready-made: تعقیب taʿqīb (form II verbal noun) 'pursuit, following up', عقبیٰ ʿuqbā 'the hereafter', عقوبت ʿuqūbat 'punishment' (what follows a deed), عاقبت ʿāqibat 'outcome, end'. Because they are Arabic stem-formations, not Persian coinages, they entered as whole words.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B9%D9%82%D8%A8\"],\n          \"ref_check\": [\n            {\"ref\": \"FVA:276\", \"status\": \"not_checked\", \"note\": \"S. M. Nahvi, Farhang-e Vāzheh-hā-ye ʿArabi dar Fārsi — refs_online.json records 'Searched archive.org, ketabnak, noorlib, web: no digital copy found', and there is no local file, so the page could not be opened.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi (MON_part2 OCR), compounds عقب‌نشینی, عقب رفتن etc.\", \"stance\": \"supports\", \"note\": \"the OCR shows عقب used throughout as an ordinary Persian word ('عقب: پس، پیش', 'عقب‌نشینی کردن، عقب رفتن'); Moʿin's Arabic-origin tag [ع.] is standard for this headword, though the headword line itself is not cleanly recoverable from this OCR.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ (BQT_v1/v2_pages.txt)\", \"stance\": \"silent\", \"note\": \"عقب occurs only inside definitions, never as a headword — expected, since Borhān is a dictionary of Persian (dari) words and excludes plain Arabic loans.\"},\n            {\"src\": \"RCH\", \"where\": \"Richardson, Persian-Arabic-English Dictionary s.v. ʿaqib\", \"stance\": \"supports\", \"note\": \"'A [ʿaqib], Behind, after' — listed with the 'A' (Arabic) tag in a Persian dictionary, i.e. exactly an Arabic word current in Persian.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery p.291\", \"stance\": \"supports\", \"note\": \"establishes Yaʿqūb as the Qurʾānic Arabic form, which is the shape Persian یعقوب reflects.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Hebrew\",\n          \"words\": \"âqebh : heel; Ya`aqôbh : one that takes by the heel, follower, name of a prophet\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The forms and glosses are correct: עָקֵב ʿāqēb 'heel, footprint', verb עָקַב ʿāqab 'to follow at the heel, supplant, overreach', and יַעֲקֹב Yaʿăqōb, formally a prefix-conjugation (imperfect) of that verb, explained in Genesis 25:26 by Esau's heel and in 27:36 by the pun on ʿāqab 'he supplanted'. What is wrong is the arrow: Hebrew did not get this from Syriac. Syriac is a first-millennium-CE dialect of Eastern Aramaic, while Hebrew ʿāqēb and the name Yaʿăqōb are attested in the Iron Age and the name-type Yaʿqub-ʾil already in second-millennium Amorite and Egyptian sources; Hebrew and Syriac are sister reflexes of a common Semitic *ʿaqib-. Klein, the reference Nourai cites, builds the entry the other way round (Hebrew ʿāqēbh → ʿaqabh → Yaʿăqōbh, with Aramaic/Akkadian/Arabic as relatives). Everything below this node — Greek Ἰακώβ/Ἰάκωβος, Latin Jacobus, French Jacques — does come from the Hebrew name, so only the incoming arrow is at fault.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D7%A2%D7%A7%D7%91\",\n            \"https://en.wiktionary.org/wiki/%D7%99%D7%A2%D7%A7%D7%91\",\n            \"https://www.etymonline.com/word/James\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:823\", \"status\": \"supports\", \"note\": \"KLN_1966 leaf 444-445 = p.823 s.v. Jacob: 'fr. Heb. Yaʿăqōbh, lit. \\\"one that takes by the heel\\\", a derivative of ʿaqēbh, \\\"heel\\\", whence ʿaqabh, \\\"he followed at the heel, he overreached, circumvented\\\"'. Klein supports the two Hebrew words and their internal relation exactly as Nourai glosses them (though not the Syriac ancestry claimed for them).\"},\n            {\"ref\": \"FSD:1307\", \"status\": \"supports\", \"note\": \"FSD_vol2.txt 0-based leaf 601 (page numeral 1308 on the leaf; the entry straddles 1307-1308), s.v. jack: '[< OF. Jacques, Jacob (= OF. Jakemes, James, > E. James), < LL. Jacobus, < Gr. Iakōbos, < Heb. Yaʿaqob, lit. supplanter, < ʿāqab, supplant.]' — Funk & Wagnalls gives the whole Hebrew→Greek→Late Latin→French chain on the page cited.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966 p.823\", \"stance\": \"partial\", \"note\": \"supports the Hebrew forms, contradicts the Syriac parentage (cognates, not ancestors).\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, New Standard Dictionary pp.1307-1308 s.v. jack, and s.v. Jacob\", \"stance\": \"supports\", \"note\": \"'Ja'cob ... [Heb., supplanter]', with the Latin/French/Italian/Spanish forms Jacobus, Jacob, Giacobbe, Jacobo listed.\"},\n            {\"src\": \"AFA\", \"where\": \"Fraenkel, Aramäische Fremdwörter\", \"stance\": \"silent\", \"note\": \"no treatment of ʿ-q-b; the root is not an Aramaic import anywhere.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. jack\", \"stance\": \"supports\", \"note\": \"'LL. Jacobus; Gr. Iakobos, from Heb. yaʿaqōb, Jacob, lit., seizing by the heel, a supplanter.'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"Jacobos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek Ἰακώβ (indeclinable) is the Septuagint's transcription of Hebrew יַעֲקֹב, with η/ω rendering the Hebrew vowels and the final -b as β; alongside it the Hellenised, fully declinable Ἰάκωβος (Nourai's 'Jacobos') was formed with the Greek masculine ending -ος and is the form used in the New Testament for James son of Zebedee and James son of Alphaeus. The doublet matters for what follows: Ἰακώβ stayed the patriarch's name, Ἰάκωβος became the apostles' name and so the ancestor of the European personal names.\",\n          \"sources\": [\"https://www.etymonline.com/word/James\"],\n          \"ref_check\": [\n            {\"ref\": \"FSD:1307\", \"status\": \"supports\", \"note\": \"FSD_vol2.txt leaf 601 (pp.1307-1308) s.v. jack: '< LL. Jacobus, < Gr. Iakōbos, < Heb. Yaʿaqob' — the Greek link on the cited page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966 p.823 s.v. Jacob\", \"stance\": \"supports\", \"note\": \"'Late L. Jacōbus, fr. Gk. Ἰακώβος, fr. Heb. Yaʿăqōbh'.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. jack\", \"stance\": \"supports\", \"note\": \"'OFr. Jaque, Jaques; LL. Jacobus; Gr. Iakobos, from Heb. yaʿaqōb'.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls p.1307\", \"stance\": \"supports\", \"note\": \"as quoted.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Late Latin\",\n          \"words\": \"Jacobŭs\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Late Latin Iacōbus, the Vulgate/ecclesiastical Latinisation of Greek Ἰάκωβος with the second-declension ending -us (beside indeclinable Iacob for the patriarch). Within Latin it developed a popular variant Iacōmus (b > m before the labial, or by dissimilation in Vulgar Latin), and the two forms then went separate ways in Romance: Iacōbus > Spanish Jacobo/Iago (whence Sant-Iago, Diego), Old French Jaques; Iacōmus > Old French James, Italian Giacomo, Spanish Jaime, and English James. The chart's later Latin -ŭs marking simply notes the short vowel of the ending.\",\n          \"sources\": [\"https://www.etymonline.com/word/James\"],\n          \"ref_check\": [\n            {\"ref\": \"FSD:1307\", \"status\": \"supports\", \"note\": \"FSD_vol2.txt leaf 601 (pp.1307-1308) s.v. jack: '< OF. Jacques, Jacob (= OF. Jakemes, James, > E. James), < LL. Jacobus' — the Late Latin stage and both Old French continuations are named on the cited page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966 p.823 s.vv. Jacob, Jacobin, Jacobite, jacobus, James\", \"stance\": \"supports\", \"note\": \"'Jacobite ... Formed with subst. suff. -ite fr. Late L. Jacōbus, \\\"Jacob, James\\\"'; 'James, masc. PN. — Late L. Jacōmus, altered fr. Jacōbus.'\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. jack\", \"stance\": \"supports\", \"note\": \"'LL. Jacobus' in the chain OFr. Jaque(s) < LL. Jacobus < Gr. Iakobos.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet\", \"stance\": \"silent\", \"note\": \"a Christian-era proper name; Ernout-Meillet's dictionary of the Latin lexicon has no entry for it.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"Jaques\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old French Jaques (modern Jacques), from Late Latin Iacōbus — more precisely from a hypocoristic/diminutive of it — with the regular Gallo-Romance loss of the intervocalic -b- and of the final syllable; the spelling Jaques is the medieval one, Jacques the modern. Because Jacques was the stock name for a French peasant in the 14th century it also gave the common nouns jaque 'sleeveless coat' (> jaquette > English jacket) and jacquerie 'peasants' revolt'. From the same name France produced the feminine diminutive Jacqueline, the direct source of nodes #7 and #8.\",\n          \"sources\": [\"https://www.etymonline.com/word/James\"],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"the French box carries no citation of its own; the chain is covered by the KLN:823 and FSD:1307 references of its neighbours, both checked.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966 p.823 s.vv. Jack, jack 'a sleeveless coat', jacquerie\", \"stance\": \"supports\", \"note\": \"'OF. Jaques (F. Jacques), fr. Late L. Jacōbus, for earlier Jacobus'; and 'OF. jaque, \\\"sleeveless coat\\\", fr. Jacques, \\\"Jack\\\", a nickname given to the French peasant in the 14th century'.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls pp.1307-1308\", \"stance\": \"supports\", \"note\": \"'< OF. Jacques, Jacob ... < LL. Jacobus'.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d'origine orientale\", \"stance\": \"silent\", \"note\": \"no entry for Jacques — expected: Devic covers Arabic/Persian/Turkish borrowings, and a biblical name transmitted through Latin is outside his scope.\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan, Dict. étym. des mots ... dérivés de l'arabe, du persan ou du turc\", \"stance\": \"silent\", \"note\": \"no occurrence of Jacques.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"žâk «ژاک»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A modern Persian transcription of the French given name Jacques [ʒak], taken over with the twentieth-century wave of French cultural borrowings: French /ʒ/ is written ژ ž (the same letter used in ژورنال, ژنرال, ژاکت), /a/ as ا, /k/ as ک. The chart's extra ژاکلین Žāklin is French Jacqueline, the feminine diminutive of the same name, and it is the far commoner of the two in Persian. These are name transcriptions, not inherited words, so there is no sound change to describe beyond the phonemic substitution.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"not_checked\", \"note\": \"Nourai gives no page. Proper names in Farhang-e Fārsi are in volumes 5-6 (aʿlām), which are not among the digitised volumes; the OCR of the lexicon volumes on disk has ژاکت (jacket) but no ژاک or ژاکلین.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. ژاکت\", \"stance\": \"partial\", \"note\": \"'ژاکت: ... (اِ.) جامهٔ مردانه که تا زانو ...' — Moʿin has the related French borrowing ژاکت (< F. jaquette, itself from jaque < Jacques) with the same ژ for French /ʒ/, which is the transcription convention at issue; the name itself is in the undigitised aʿlām volumes.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch, Etym. Wb. der europäischen Wörter orientalischen Ursprungs\", \"stance\": \"silent\", \"note\": \"the one occurrence of 'Jacques' in the text is a bibliographic name; Lokotsch treats Oriental words in European languages, not the reverse direction, so he has nothing on Persian ژاک.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ\", \"stance\": \"silent\", \"note\": \"a 17th-century dictionary of Persian; a 20th-century French name transcription cannot appear in it.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"Jacqueline\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Jacqueline is French Jacqueline, the feminine of Jacquelin, itself a double diminutive of Jacques (Jacques + -el + -in); it entered English in the Middle Ages (Jacquetta/Jaquelin) and was re-borrowed in its French spelling and pronunciation in the twentieth century. So the parent box (French Jaques) is the right one, and the ultimate source is Late Latin Iacōbus < Greek Ἰάκωβος < Hebrew Yaʿăqōb.\",\n          \"sources\": [\"https://www.etymonline.com/word/James\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:699\", \"status\": \"not_checked\", \"note\": \"AHD:699 is a page in the main body of the 1975/76 American Heritage Dictionary, not in the Indo-European appendix; only the appendix (and the modern online edition's root pages) is accessible, and the 1970s AHD scans on archive.org are lending-restricted (djvu.txt returns 401). The claim itself is uncontroversial.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966 p.823 s.vv. Jacob, Jacobin, jacquerie\", \"stance\": \"partial\", \"note\": \"Klein has no separate Jacqueline entry but establishes the French base: 'OF. Jaques (F. Jacques), fr. Late L. Jacōbus' and 'F. jacquerie, prop. \\\"rising of peasants\\\", fr. Jacques'.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt\", \"stance\": \"silent\", \"note\": \"grep for 'Jacqueline' in Webster's New Twentieth Century vol. 1 returns nothing (the name is in the biographical/given-name supplement, not the main A-Z of this volume).\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls p.1307 s.v. jack\", \"stance\": \"supports\", \"note\": \"gives OF. Jacques as the French base from which the diminutives are formed.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"Jacob, Jack, Jim, James\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Jacob and James are secure. Jacob is the learned/biblical form, taken straight from Late Latin Iacōbus (Wycliffe onwards); James is the Middle English vernacular reflex of Late Latin Iacōmus (the b>m variant of Iacōbus) through Old French James, attested from the late 12th century. Jim is a 19th-century pet form of James (with Jimmy, Jem). Jack is the disputed item. Klein — the reference cited — makes it 'Familiar form of John, but derived fr. OF. Jaques (F. Jacques), fr. Late L. Jacōbus', and Funk & Wagnalls and Webster's say the same. Modern scholarship rejects that: the OED and Wiktionary derive Jack from Middle English Jakke/Jankin/Jankyn, via Anglo-Norman Jakke from Middle Dutch Janke, a diminutive of Jan 'John' — the vowel and the -kin suffix point to John, and the sense-history (Jack as a generic name for a common fellow) matches the John words. Jack is only secondarily used as an anglicisation of French Jacques. So the Jacobus→Jack edge as drawn is at best a minority view, and with it the descent of node #10.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Jack\",\n            \"https://www.etymonline.com/word/James\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:823\", \"status\": \"partial\", \"note\": \"KLN_1966 leaf 444 (p.823): 'Jack, masc. PN. — Familiar form of John, but derived fr. OF. Jaques (F. Jacques), fr. Late L. Jacōbus, for earlier Jacobus, fr. Gk., fr. Heb. Yaʿăqōbh, \\\"Jacob\\\"'; 'James, masc. PN. — Late L. Jacōmus, altered fr. Jacōbus. See Jacob and cp. jimmy'; 'Jacob ... Late L. Jacōbus'. The page supports Jacob, James and Jim exactly; for Jack it supports Nourai's arrow but states the very tension ('familiar form of John, but derived fr. OF. Jaques') that modern dictionaries resolve the other way.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966 p.823 s.vv. Jack, James, Jacob\", \"stance\": \"supports\", \"note\": \"quoted above; Klein routes Jack through OF Jaques.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls pp.1307-1308 s.v. jack\", \"stance\": \"supports\", \"note\": \"'[< OF. Jacques, Jacob (= OF. Jakemes, James, > E. James), < LL. Jacobus, < Gr. Iakōbos, < Heb. Yaʿaqob, lit. supplanter, < ʿāqab, supplant.]'\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. jack\", \"stance\": \"supports\", \"note\": \"'jack, n. [ME. Jacke, Jake; OFr. Jaque, Jaques; LL. Jacobus; Gr. Iakobos, from Heb. yaʿaqōb, Jacob, lit., seizing by the heel, a supplanter. From the nickname ... used for a servant or boy who made himself generally useful, it is applied to lifting instruments.]'\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt (Skeat, Concise Etym. Dict.)\", \"stance\": \"silent\", \"note\": \"the OCR of this scan is too degraded to locate the headwords Jack/James (grep for 'awkward', 'post' returns only stray inflected forms); no usable reading obtained.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Persian\",\n          \"words\": \"jak «جَک» : jack (for lifting)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian جک jak is a twentieth-century borrowing of English 'jack' in the mechanical sense — a screw or hydraulic lifting device, above all the car jack (جک ماشین) — with ج for English /dʒ/ and the short a written only by the fatḥa Nourai marks. The English word itself is the personal name Jack transferred to a labour-saving contrivance ('a boy who made himself generally useful'), so the semantic step 'servant/fellow' → 'device that does the lifting for you' happened in English, not in Persian; Persian took over only the finished technical term. The chain above it (Jack ← Jacques ← Jacobus) is the disputed part, not this last link.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AC%DA%A9\",\n            \"https://fa.wiktionary.org/wiki/%D8%AC%DA%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:1233\", \"status\": \"not_checked\", \"note\": \"the page itself could not be opened: Moʿin's Farhang-e Fārsi has no page-mapped digital copy (refs_online.json: 'Page numbers cannot be mapped online'), and the local OCR of the lexicon volumes gives no clean headword hit for جک. Indirect corroboration: the Persian Wiktionary entry جک gives the etymology 'انگلیسی' and the definition 'دستگاهی به شکل اهرم که برای بالا بردن و نگاه داشتن اشیاء سنگین مانند اتومبیل و غیره به کار برند', citing فرهنگ لغت معین as its source — i.e. it reproduces the very Moʿin entry Nourai cites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin s.v. جک, as reproduced by fa.wiktionary\", \"stance\": \"supports\", \"note\": \"'ریشه‌شناسی: انگلیسی — اسم: دستگاهی به شکل اهرم که برای بالا بردن و نگاه داشتن اشیاء سنگین مانند اتومبیل و غیره به کار برند. منابع: فرهنگ لغت معین'.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. jack, sense 8\", \"stance\": \"supports\", \"note\": \"'8. any of various machines used to lift, hoist, or move something heavy a short distance; as, a jackscrew, hydraulic jack, automobile jack' — the English sense Persian borrowed, and Webster explicitly derives it from the personal name.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ\", \"stance\": \"silent\", \"note\": \"no entry: a modern European technical loan cannot be in a 1062/1652 dictionary.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-60.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-04T23:03:19.196Z] TOOL RESULT

```
JSON OK
```


## [2026-09-04T23:03:24.347Z] TOOL CALL #103: Bash

```json
{
 "command": "python3 tools/verify_check.py 60"
}
```


### [2026-09-04T23:03:26.473Z] TOOL RESULT

```
nodes verified: 18/18
node verdicts: {'disputed': 4, 'confirmed': 13, 'plausible': 1}
root verdicts: {'confirmed': 1, 'disputed': 1}
ref checks: {'partial': 4, 'not_checked': 7, 'supports': 12}
books consulted: {'partial': 10, 'contradicts': 2, 'supports': 38, 'silent': 13} | by book: {'KLN': 10, 'WEB': 8, 'FSD': 5, 'WLD': 4, 'MON': 4, 'POK': 3, 'LAT': 3, 'BQT': 3, 'IEC': 2, 'AHD': 2, 'KNT': 2, 'BRT': 2, 'FVQ': 2, 'RCH': 2, 'AFA': 2, 'PHD': 1, 'NYB': 1, 'HUB': 1, 'SOD': 1, 'TAD': 1, 'DEV': 1, 'PHN': 1, 'LKT': 1, 'SKT': 1}
```


## [2026-09-04T23:03:29.739Z] TOOL CALL #104: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | grep -i \"page-60\\|60:\" | head -20; echo \"exit $?\""
}
```


### [2026-09-04T23:03:34.694Z] TOOL RESULT

```
exit 0
```


## [2026-09-04T23:03:37.021Z] TOOL CALL #105: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | tail -20"
}
```


### [2026-09-04T23:03:41.718Z] TOOL RESULT

```
498 cited URLs, 21 not yet archived
archived 21, failed 0
```


## [2026-09-04T23:03:59.511Z] AGENT

Done. `data/verification/page-60.json` written; `verify_check.py 60` reports 18/18 nodes, no PROBLEM lines.

**Page 60 (book p.30) — 2 non-redirect entries, 18 nodes**

- Node verdicts: 13 confirmed, 1 plausible, 4 disputed. Root verdicts: 1 confirmed (Apo), 1 disputed (A`.q.b).
- Ref checks: 12 supports, 4 partial, 7 not_checked. 63 `consulted` entries across 24 books.
- Nourai's page numbers were unusually accurate: POK:53, POK:841, POK:842, HRN:70 (no. 315), SOD:55 (entry 1403) and SOD:300 (entry 7474), KLN:823, FVQ:291, FSD:1307, IEC:29 all landed on the right page; BQT:403 is right to within one leaf (the پس / پس‌انداز run in Borhān vol. 1).

Disputed items:
- **Apo, node #1 (Germanic) "eben : later time, evening"** — Gmc *ēbanþ- is not put under *apo by Pokorny or Watkins/AHD; Klein assigns it to *epi/*opi ("the hinder part of the day"), Etymonline calls it "of uncertain origin". The other three items (af, apo-tero, afug) are confirmed verbatim by AHD and POK 53-55.
- **Apo, node #2 (English) "evening"** — same issue; of/off, after, awkward confirmed.
- **ROOT A`.q.b labelled [Syriac]** — ʿ-q-b is common Semitic (Akkadian, Hebrew, Aramaic, Arabic all inherit it); Klein, the cited reference, calls Aramaic/Arabic/Akkadian *cognates* of Hebrew, not ancestors. Only the Arabic personal name Yaʿqūb plausibly comes from Syriac (Jeffery, FVQ 291, which does support that sub-claim).
- **Node #3 (Hebrew) âqebh, Ya`aqôbh** — cannot descend from Syriac: Yaʿăqōb is attested a millennium before Syriac existed (Amorite yaʿqub-ʾil); forms/glosses themselves are correct.
- **Node #9 (English) "Jack"** — Klein/FSD/Webster all route Jack through OF Jaques < Jacobus (so Nourai's arrow reflects his sources), but OED/Wiktionary derive it from ME Jakke/Jankyn < Jan "John"; Jacob, James, Jim are fine. This also weakens the chain to node #10 (Persian جک), though that last link (English jack → Persian jak) is itself solid.

No transcription_suspect items — I rendered PDF page 60 to PNG and checked the chart against the JSON; the extraction matches the print exactly, including "eben" and «پس ۱».
