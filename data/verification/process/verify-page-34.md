# Verification process log — verify-page-34


## [2026-09-04T18:30:29.954Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 34 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-34.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-34.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-34.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 34` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T18:30:31.618Z] AGENT

I'll start by reading the instructions.


## [2026-09-04T18:30:33.042Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T18:30:33.060Z] TOOL RESULT

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


## [2026-09-04T18:30:33.737Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-34.txt"
}
```


### [2026-09-04T18:30:33.751Z] TOOL RESULT

```
1	=== PDF page 34 (book page 4) ===
2	--- entry 0 ---
3	ROOT [Sanskrit / Old Persian] Abâ, Sabha : to assemble together  (refs BQT:218; DRM:129; LKT)
4	#1 (parent #0) [Old Persian] refs=BQT:218; DRM:129; LKT | abâ-cari : place of assembly ☞Kwel
5	  #2 (parent #1) [Pahlavi] refs=BQT:212 | vâ-čar : trade center | NOTE: See AEF:219 for further discussion.
6	    #3 (parent #2) [Persian] refs=MON; KLN | bâzâr «بازار» : bazaar
7	      #4 (parent #3) [Persian] refs=BQT:219; HRN:38 | bâzargân «بازرگان» : merchant
8	      #5 (parent #3) [Turkish] refs=None | 
9	        #6 (parent #5) [Italian] refs=None | 
10	          #7 (parent #6) [English] refs=AHD | bazaar
11	--- entry 1 ---
12	ROOT [Semitic] A`.b.r : to pass, cross  (refs KLN:712)
13	#1 (parent #0) [Arabic] refs=KLN:712 | a`.b.r : to pass, cross ; abara : he passes across
14	  #2 (parent #1) [Persian] refs=FVA:260 | obŭr «عبور» : passing, crossing | extra: عابر ، معبر ، معابر
15	  #3 (parent #1) [Arabic] refs=SBK:69 | a`.r.b : distorted form of "a`.b.r" meaning to cross (dwell in) deserts
16	    #4 (parent #3) [Arabic] refs=SBK:69; KLN:98 | a`rab : desert dweller, Arab
17	      #5 (parent #4) [Persian] refs=FVA:265 | Arab «عرب» | extra: إعراب ، أعرابی ، معرّب
18	      #6 (parent #4) [Greek] refs=KLN:98 | 
19	        #7 (parent #6) [French] refs=None | 
20	          #8 (parent #7) [English] refs=KLN:98 | Arab
21	#9 (parent #0) [Hebrew] refs=KLN:712 | âbhar : he passed across ; ibhri : he who came from across the river, the Hebrew people who had crossed the river were referred to as "Ibhri".
22	  #10 (parent #9) [Aramaic] refs=KLN:712 | Ibhray
23	    #11 (parent #10) [Arabic] refs=None | 
24	      #12 (parent #11) [Persian] refs=MON | ebrî «عبری» : Hebrew ; ebrânî «عبرانی» : Hebrew
25	    #13 (parent #10) [Greek] refs=None | Ebraios
26	      #14 (parent #13) [Latin] refs=None | Hebraeus
27	        #15 (parent #14) [English] refs=KLN:712 | Hebrew
28	--- entry 2 ---
29	ROOT Âbu -> redirect to Yb
30	
```


## [2026-09-04T18:30:35.474Z] AGENT

I'll read the supporting files.


## [2026-09-04T18:30:37.942Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T18:30:37.983Z] TOOL RESULT

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


## [2026-09-04T18:30:40.840Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['BQT','DRM','LKT','MON','KLN','HRN','AHD','FVA','SBK','AEF','POK','WLD','PHD','NYB','HUB','FVQ','AFM','PLA','AFA','SKT','FSD','WEB','TTS','IEC','SYN','BRT','KNT','CHEUNG','ARY']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False))\n    else: print(k,'--MISSING--')\n\""
}
```


### [2026-09-04T18:30:42.472Z] TOOL RESULT

```
<persisted-output>
Output too large (43.5KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bbcepusr5.txt

Preview (first 2KB):
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned 
...
</persisted-output>
```


## [2026-09-04T18:30:49.544Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['DRM','FVA','SBK','AEF','LKT','KLN','HRN','MON','AHD']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print('==',k, v.get('title','')[:200])\n    print('  kind:',v.get('kind'))\n    print('  local_file:',v.get('local_file'))\n    print('  page_offset:',v.get('page_offset'))\n    print('  hint:',str(v.get('lookup_hint'))[:400])\n\""
}
```


## [2026-09-04T18:30:50.074Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-34.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1))\" | head -200"
}
```


### [2026-09-04T18:30:51.244Z] TOOL RESULT

```
== DRM J. Darmesteter, Études iraniennes, 2 vols., Paris 1883
  kind: archive_djvu
  local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/DRM.txt
  page_offset: Tome I: leaf = p + 22 (e.g. leaf 26 = p.4); Tome II (starts ~leaf 364): leaf = p + 364 (e.g. leaf 368 = p.4). Nourai does not say which tome - try both. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Tome I is the historical grammar of Persian (numbered §§); Tome II contains the 'Études sur la langue...' incl. etymological notes on Persian words. grep the Persian word in transliteration.
== FVA S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989
  kind: catalog
  local_file: None
  page_offset: None
  hint: Searched archive.org, ketabnak, noorlib, web: no digital copy found.
== SBK M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
  kind: archive_djvu
  local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SBK.txt']
  page_offset: None
  hint: grep in SBK.txt (raw djvu, no page breaks); use inside.php with doc='سبک شناسی_1'. Later printings keep the 1st-edition pagination approximately; verify.
== AEF Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübsch
  kind: catalog
  local_file: None
  page_offset: None
  hint: Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فرهنگ ریشه‌شناختی فارسی' (Mehrafarin), also not online.
== LKT K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  kind: archive_djvu
  local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt
  page_offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== KLN E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  kind: archive_djvu
  local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
  page_offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== HRN P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  kind: archive_djvu
  local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
  page_offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== MON Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)
  kind: website+archive_djvu
  local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
  page_offset: None
  hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab
== AHD W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)
  kind: archive_djvu+website+archive_restricted
  local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
  page_offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
  hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.
```


### [2026-09-04T18:30:53.169Z] TOOL RESULT

```
{
 "pdf_page": 34,
 "book_page": 4,
 "entries": [
  {
   "root": {
    "name": "Abâ, Sabha",
    "lang": "Sanskrit / Old Persian",
    "refs": "BQT:218; DRM:129; LKT",
    "gloss": "to assemble together"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Old Persian",
     "refs": "BQT:218; DRM:129; LKT",
     "words": [
      {
       "translit": "abâ-cari",
       "gloss": "place of assembly",
       "script": null,
       "see": [
        "Kwel"
       ]
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Pahlavi",
     "refs": "BQT:212",
     "words": [
      {
       "translit": "vâ-čar",
       "gloss": "trade center",
       "script": null
      }
     ],
     "note": "See AEF:219 for further discussion.",
     "quote": null
    },
    {
     "id": 3,
     "parent": 2,
     "lang": "Persian",
     "refs": "MON; KLN",
     "words": [
      {
       "translit": "bâzâr",
       "gloss": "bazaar",
       "script": "بازار"
      }
     ],
     "note": null,
     "quote": {
      "text": "این همه مشتری وگرمی بازار نداشت - یوسفی بود، ولی هیچ خریدار نداشت",
      "poet": "Vahshî Bâfqî"
     }
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "Persian",
     "refs": "BQT:219; HRN:38",
     "words": [
      {
       "translit": "bâzargân",
       "gloss": "merchant",
       "script": "بازرگان"
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 5,
     "parent": 3,
     "lang": "Turkish",
     "refs": null,
     "words": [],
     "note": null,
     "quote": null
    },
    {
     "id": 6,
     "parent": 5,
     "lang": "Italian",
     "refs": null,
     "words": [],
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 6,
     "lang": "English",
     "refs": "AHD",
     "words": [
      {
       "translit": "bazaar",
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
    "name": "A`.b.r",
    "lang": "Semitic",
    "refs": "KLN:712",
    "gloss": "to pass, cross"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Arabic",
     "refs": "KLN:712",
     "words": [
      {
       "translit": "a`.b.r",
       "gloss": "to pass, cross",
       "script": null
      },
      {
       "translit": "abara",
       "gloss": "he passes across",
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
     "refs": "FVA:260",
     "words": [
      {
       "translit": "obŭr",
       "gloss": "passing, crossing",
       "script": "عبور"
      }
     ],
     "script_extra": "عابر ، معبر ، معابر",
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 1,
     "lang": "Arabic",
     "refs": "SBK:69",
     "words": [
      {
       "translit": "a`.r.b",
       "gloss": "distorted form of \"a`.b.r\" meaning to cross (dwell in) deserts",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "Arabic",
     "refs": "SBK:69; KLN:98",
     "words": [
      {
       "translit": "a`rab",
       "gloss": "desert dweller, Arab",
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
     "refs": "FVA:265",
     "words": [
      {
       "translit": "Arab",
       "gloss": null,
       "script": "عرب"
      }
     ],
     "script_extra": "إعراب ، أعرابی ، معرّب",
```


## [2026-09-04T18:30:57.221Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-34.json'))\nprint(json.dumps(d['entries'][1]['nodes'][5:],ensure_ascii=False,indent=1))\nprint('---entry2---')\nprint(json.dumps(d['entries'][2:],ensure_ascii=False,indent=1))\""
}
```


## [2026-09-04T18:30:57.798Z] TOOL CALL #8: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py"
}
```


### [2026-09-04T18:30:58.931Z] TOOL RESULT

```
[
 {
  "id": 6,
  "parent": 4,
  "lang": "Greek",
  "refs": "KLN:98",
  "words": [],
  "note": null,
  "quote": null
 },
 {
  "id": 7,
  "parent": 6,
  "lang": "French",
  "refs": null,
  "words": [],
  "note": null,
  "quote": null
 },
 {
  "id": 8,
  "parent": 7,
  "lang": "English",
  "refs": "KLN:98",
  "words": [
   {
    "translit": "Arab",
    "gloss": null,
    "script": null
   }
  ],
  "note": null,
  "quote": null
 },
 {
  "id": 9,
  "parent": 0,
  "lang": "Hebrew",
  "refs": "KLN:712",
  "words": [
   {
    "translit": "âbhar",
    "gloss": "he passed across",
    "script": null
   },
   {
    "translit": "ibhri",
    "gloss": "he who came from across the river, the Hebrew people who had crossed the river were referred to as \"Ibhri\".",
    "script": null
   }
  ],
  "note": null,
  "quote": null
 },
 {
  "id": 10,
  "parent": 9,
  "lang": "Aramaic",
  "refs": "KLN:712",
  "words": [
   {
    "translit": "Ibhray",
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
  "lang": "Arabic",
  "refs": null,
  "words": [],
  "note": null,
  "quote": null
 },
 {
  "id": 12,
  "parent": 11,
  "lang": "Persian",
  "refs": "MON",
  "words": [
   {
    "translit": "ebrî",
    "gloss": "Hebrew",
    "script": "عبری"
   },
   {
    "translit": "ebrânî",
    "gloss": "Hebrew",
    "script": "عبرانی"
   }
  ],
  "note": null,
  "quote": null
 },
 {
  "id": 13,
  "parent": 10,
  "lang": "Greek",
  "refs": null,
  "words": [
   {
    "translit": "Ebraios",
    "gloss": null,
    "script": null
   }
  ],
  "note": null,
  "quote": null
 },
 {
  "id": 14,
  "parent": 13,
  "lang": "Latin",
  "refs": null,
  "words": [
   {
    "translit": "Hebraeus",
    "gloss": null,
    "script": null
   }
  ],
  "note": null,
  "quote": null
 },
 {
  "id": 15,
  "parent": 14,
  "lang": "English",
  "refs": "KLN:712",
  "words": [
   {
    "translit": "Hebrew",
    "gloss": null,
    "script": null
   }
  ],
  "note": null,
  "quote": null
 }
]
---entry2---
[
 {
  "root": {
   "name": "Âbu",
   "redirect": "Yb"
  },
  "nodes": []
 }
]
```


### [2026-09-04T18:30:58.964Z] TOOL RESULT

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


## [2026-09-04T18:31:22.412Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo \"---KLN awk page 712---\"; python3 - <<'EOF'\nimport re\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nEOF"
}
```


### [2026-09-04T18:31:24.070Z] TOOL RESULT

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
---KLN awk page 712---
903
```


## [2026-09-04T18:31:26.714Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^Hebrew\" KLN_1966.txt | head; echo \"=== Arab ===\"; grep -n \"^Arab\" KLN_1966.txt | head -20; echo \"=== bazaar ===\"; grep -n -i \"^bazaar\" KLN_1966.txt | head"
}
```


### [2026-09-04T18:31:26.807Z] TOOL RESULT

```
17390:Hebrew,  n.  and  adj.  —  ME.  Ebreu,  fr.  OF.  Ebreu, Ebrieu  (F.  Hebreu),  fr.  L.  Hebraeus,  fr.  Gk. ‘EPpafop,  fr.  Aram,  'ibhray,  'ebhray,  fr.  Heb. ‘ibhrf,  ‘Hebrew’,  lit.  ‘he  who  came  from  across (the  RiverV,  fr.  'ibher,  ‘region  across,  side’, from  the  stem  of  'abhar,  ‘he  passed  across  or over’,  which  is  rel.  to  Aram. -Syr.  'abhar,  Arab. 'dbara,  ‘he  passed  across’,  Akkad,  eberu,  ‘to pass  over’,  Heb.  ‘ ebhrdh ,  ‘fury,  anger’  (lit.  ‘over¬ flow’),  Mishnaic  Heb.  'dbherd’1,  ‘transgression, sin’  (for  tense  development  cp.  E.  transgression), Heb.  ma'dbhdr,  ma'dbhardh,  ‘ford,  pass’.  Cp. Habiru.  Cp.  also  averah.
=== Arab ===
523:Arab.
524:Arabic
3277:Arabe!,  Arabella,  fem.  PN.  —  This  name  of  Scot¬ tish  origin  prob.  arose  from  the  blend  of  the name  Annabel(la)  with  the  ethnic  name  Arab, arabesque,  n.  —  F.,  It.  arabesco,  fr.  Arabo, ‘Arab’.  See  Arab  and  -esque.
3279:Arabic,  adj.  —  OF.,  fr.  L.  Arabicus,  ‘Arabic’,  fr. Arabs.  See  Arab  and  -ic.
3281:Arabis,  n.,  a  genus  of  clustering  plants  containing the  rock  cresses.  —  ML.  Arabis,  ‘Arabian’,  fr. L.  Arabs.  See  Arab.
4880:Arabico-Latinum,  I,  79a  and  b),  ult.  fr.  Pers. badzahr,  padzahr,  ‘counterpoison,  bezoar  stone’, lit.  ‘protecting  (against)  poison’,  fr.  pad,  ‘pro¬ tecting,  guarding;  guardian,  lord,  master’,  and zahr,  ‘poison’.  For  the  first  element  see  padi- shah.  The  second  element  is  rel.  to  Pers.  zehre, ‘gall,  bile’,  Pahlavi  zahr,  ‘poison’,  Avestic  zara-, ‘gall,  bile’,  and  cogn.  with  Gk.  yoXf],  ‘gall,  bile’. See  choler.
20201:Arab,  jawdb,  ‘answer’,  which  is  rel.  to  ajdba, jdwaba,  ‘he  answered’.
25485:Arab,  nizam,  ‘arrangement,  order,  administra¬ tion,  reign’,  fr.  nazama,  ‘he  put  in  order,  ar¬ ranged’.  Cp.  nazim.
31436:Arab,  qintar.  See  kantar  and  cp.  kilderkin, quintan,  adj.,  occurring  every  fifth  day;  n.,  fever recurring  every  fifth  day  (counting  both  days  of consecutive  occurrence).  —  L .quintanus,  ‘fifth  in order’,  fr.  quintus,  ’fifth’.  See  quint  and  cp. quintain.
40917:Arab.  ushnah,  ‘moss’,  which  is  of  Persian  origin. Usneaceae,  n.  pi.,  a  family  of  lichens  (bot.)  — ModL.,  formed  from  prec.  word  with  suff. -aceae.
=== bazaar ===
4585:bazaar
```


## [2026-09-04T18:31:31.211Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3265,3282p' KLN_1966.txt; echo \"=====BAZAAR=====\"; sed -n '4580,4595p' KLN_1966.txt"
}
```


### [2026-09-04T18:31:31.279Z] TOOL RESULT

```
senic.  —  L„  ‘water  of  Tofana',  name  of  a  Sicilian woman,  who  lived  in  the  17th  cent,  and  invented this  poison,  using  it  for  criminal  purposes, aqua  vitae,  1)  alcohol;  2)  brandy.  ■  L.,  water  of
life’.  See  aquatic  and  vital.  For  sense  develop¬ ment  cp.  F.  eau-de-vie,  ‘spirits,  brandy  ,  lit. ‘water  of  life’,  and  E.  usquebaugh  and  whisky. aqueduct,  n.  —  L.  aquae  ductus ,  a  conduit ,  lit.
‘a  conveyance  of  water’,  fr.  aquae,  gen.  of  aqua, ‘water’,  and  ductus,  ‘a  leading’,  fr.  ductus,  pp. of  ducere,  ‘to  lead’.  See  aquatic  and  duke  and cp.  the  second  element  in  viaduct,  ventiduct, aqueous,  adj.,  watery;  like  water.  —  Formed  fr. L.  aqua,  ‘water’,  on  analogy  of  F.  aqueux,  the English  suff.  -cous  having  been  substituted  for its  usual  French  equivalent  -eux.  F.  aqueux, however,  goes  back  directly  to  L.  aquosus, ‘abounding  in  water’,  whence  also  E.  aquose. See  aquatic.
Derivatives:  aqueous-ly,  adv.,  aqueous-ness,  n. Aquila,  n.,  the  genus  of  eagles  (zool.)  —  L.  aquila, ‘eagle’.  See  aquiline.
Aquilegia,  n.,  a  genus  of  plants,  the  columbine (hot.)  —  ModL.,  called  also  aquileia,  fr.  L.  aqui¬ la,  ‘eagle’.  See  next  word, aquiline,  adj.,  1)  like  an  eagle;  2)  like  an  eagle’s. —  L.  aquilinus,  ‘of,  or  pertaining  to,  the  eagle’, fr.  aquila,  ‘eagle’,  prob.  lit.  ‘the  dark-colored (bird)’,  fern,  of  aquilus,  ‘dark-colored’,  prop, ‘water-colored’,  fr.  aqua,  ‘water  .  See  aquatic and  adj.  suff.  -ine  (representing  L.  -inus)  and  cp. eagle.  For  the  form  of  the  word  cp.  L.  nubilus, ‘cloudy’,  fr.  nubes,  ‘cloud’.
Aquilo,  n„  the  north  wind  (Roman  antiq.)  —  L. aquilo,  ‘north  wind’,  lit.  ‘the  dark  one ,  fr. aquilus,  ‘dark-colored’  [cp.  aquila,  ‘eagle’, prop,  ‘the  dark-colored  (bird)’];  see  prec.  word. For  sense  development  cp.  Gk.  xaixla?,  ‘north east  wind’,  lit.  ‘the  dark  one’,  cogn.  with  L. caecus,  ‘blind’  (see  Caecias). aquose,  adj.,  aqueous.  —  L.  aquosus,  abounding in  water’,  fr.  aqua,  ‘water’.  See  aquatic  and  cp. aqueous.
ar-,  assimilated  form  of  ad-  before  r.
-ar,  subst.  suff.  denoting  an  agent,  as  in  vicar.  — Fr.  L.  -drius  (either  directly  or  through  the  me¬ dium  of  OF.  -ier,  -er,  of  F.  -ier).  Cp.  -ary  (re¬ presenting  L.  -drius).
-ar,  adj.  suff.  meaning  ‘pertaining  to,  of  the  na¬ ture  of’,  as  in  insular.  —  Fr.  L.  -aris  (either directly  or  through  the  medium  of  OF.  -ier,  -er, or  F.  -air,  -ier).  L.  -aris  is  a  secondary  form  of - alls  (see  adj.  suff.  -al)  and  is  used  when  the  syl¬ lable  preceding  the  suff.  has  an  /.  So  e.g.  L. *dt-dlis,  *consul-d!is,  *insul-dlis,  *liin-alis,  *re- gul-dlis,  *simil-dlis,  *sol-dlis,  *stell-dlts  became dl-aris  (see  alar),  resp.  consul-arts  (see  consular), insul-aris  (see  insular),  lun-aris  (see  lunar),  regul¬ ars  (see  regular),  simil-aris  (see  simil-ar),  Sol¬ aris  (see  solar),  stell-aris  (see  stellar ).  The  change of  suff.  -alis  to  -aris  is  due  to  dissimilation.  Cp. -ary  (representing  L.  -drius).
-ar,  a  rare  variant  of  the  agential  suffixes  -er,  -or. Cp.  beggar,  liar.
ara,  n.,  altar.  • —  L.,  prob.  denoting  orig.  ‘a parched  place’,  fr.  I.-E.  base  *&-,  ‘to  bum, parch’,  whence  also  L.  arere,  ‘to  be  dry’,  aridus, ‘dry,  withered,  parched’,  ardere,  ‘to  bum’.  See ash,  ‘powdery  substance’,  and  cp.  ardent,  arid. Arab,  n.  —  F.  Arabe,  fr.  L.  Arabem,  acc.  oi  Arabs, fr.  Gk.  ’'Apooj),  gen.  "Apocpo?,  fr.  Arab.  ‘Arab, which  lit.  means  ‘inhabitant  of  the  desert’,  and is  rel.  to  Heb.  ‘arabhdh,  ‘desert’,  and  to  Ethiop. ‘dbra,  ‘was  dry,  was  waste’.  For  sense  develop¬ ment  cp.  Arab,  badawi,  ‘Bedouin’,  lit.  ‘desert dweller’,  fr.  badw,  ‘camp,  desert’  (see  Bedouin). Cp.  Mozarab.
Derivatives:  Arabesque (q.v.),  Arab-ian,  adj.  and n.,  Arabic  (q.v.),  Arab-ic-ism,  n.,  Arab-ic-ize, tr.  v.,  Arabis  (q.v.),  Arab-ist,  n.
Arabe!,  Arabella,  fem.  PN.  —  This  name  of  Scot¬ tish  origin  prob.  arose  from  the  blend  of  the name  Annabel(la)  with  the  ethnic  name  Arab, arabesque,  n.  —  F.,  It.  arabesco,  fr.  Arabo, ‘Arab’.  See  Arab  and  -esque.
Derivatives:  arabesque,  adj.  and  tr.  v.,  arabes- que-ly,  adv.
Arabic,  adj.  —  OF.,  fr.  L.  Arabicus,  ‘Arabic’,  fr. Arabs.  See  Arab  and  -ic.
Derivative:  Arabic,  n.
Arabis,  n.,  a  genus  of  clustering  plants  containing the  rock  cresses.  —  ML.  Arabis,  ‘Arabian’,  fr. L.  Arabs.  See  Arab.
arable,  adj.,  suitable  for  plowing.  —  F.,  fr.  L. arabilis,  fr.  arare,  ‘to  plow’  (whence  aratrum, ‘plow’),  fr.  I.-E.  base  *ard-,  ‘to  plow’,  whence also  Gk.  apouv,  OSlav.  orjq,  orati,  Lith.  ariu, arti,  ‘to  plow’,  Lett,  aru,  ‘I  plow’,  Goth,  arjan, OS.,  OE.  erian,  W.  arddu,  ‘to  plow’,  Mir.  airim, ‘I  plow’,  Gk.  itpoxpov,  Cret.  Stparpov,  Arm. araur,  Mir.  arathar,  OSlav.  ralo,  Lith.  drklas, ON.  arfir,  Toch.  AB  are,  ‘plow’,  Gk.  Spoupa, ‘arable  land’.  See  ear,  ‘to  plow’,  and  -able  and cp.  Arval.
=====BAZAAR=====
bayard,  n.,  a  bay  horse.  —  OF.,  fr.  bai.  See  bay, adj.  and  -ard.
Bayard,  n.,  a  gentleman  of  great  courage  and  in¬ tegrity.  —  From  the  name  of  Pierre  du  Terrail, seigneur  de  Bayard  (1473-1524),  the  celebrated ‘Chevalier  sans  peur  et  sans  reproche’  (‘knight without  fear  and  without  reproach’), bayberry,  n.  —  Compounded  of  bay,  ‘the  laurel’, and  berry.
bayonet,  n.  —  F.  bayonnette,  balonnette,  fr. Bayonne  in  Southern  France;  so  called  because the  first  bayonets  were  made  at  Bayonne.  For sense  development  cp.  bilbo,  Toledo. Derivatives  ‘.bayonet,  tr.  and  intr.  v.,  bayonet-ed, adj.,  bayonet-eer,  n.
bayou,  n.,  a  creek.  —  Amer.  F.,  fr.  Chocktaw bayuk.
baysalt,  n.  —  Fr.  Bai,  place  in  France  (near  Nan¬ tes),  renowned  as  a  shipping  port  for  sea  salt  in
bazaar
beauteous
the  15th  century.  Cp.  MDu.  bayesout ,  G.  Bai- salz,  which  are  of  the  same  meaning  and  origin, bazaar,  n.,  a  market  place.  —  Ult.  fr.  Pers.  bazar.
‘market’,  which  is  rel.  to  Pahlavi  vacar,  of  s.m. bazooka,  n.,  a  weapon  consisting  of  a  metal  tube and  used  for  launching  an  explosive  rocket; first  used  in  World  War  II. —  Fr.  bazooka,  name of  a  kind  of  wind  instrument  invented  and named  by  the  American  comedian  Bob  Burns (died  in  1956).
bazzite,  n.,  a  silicate  of  scandium,  etc.  {mineral.) —  Named  after  the  Italian  enigineer  Alessandro E.  Bazzi  (died  in  1929).  For  the  ending  see subst.  suff.  -itc.
bdellium,  n.,  1)  a  substance  mentioned  in  the Bible,  Gen.  2:12  and  Num.  11:7;  2)  a  gum resin.  —  L.,  fr.  Gk.  [iSeX’/.'.ov,  ‘a  fragrant  gum’, fr.  Heb.  bedf>lah .
be,  intr.  v.  —  ME.  been,  beon,  fr.  OE.  beon,  ‘to be',  rel.  to  biom,  OS.  bium,  OHG.  him,  OHG., MHG.,  G.  bin,  ‘I  am’,  and  cogn.  with  L.  fui, ‘I  have  been ' .fueram,  ‘I  had  been’,  fuero,  ‘I  shall have  been’,  fu-turus,  ‘about  to  be’,  Oscan  fust, ’will  be’,  L.  fid,  ‘I  become’,  Gk.  (pueiv,  ‘to  make to  grow’,  (punt?,  ‘nature’,  OI.  bhavati,  ‘be¬ comes,  happens’,  bhutdh,  ‘been’,  bhavitram, world’,  bluimih,  bhitman-,  ‘earth,  world’.  Alb. buj,  ‘I  dwell,  spend  the  night’,  bote,  ‘earth, world’,  ban(e),  ‘dwelling  place’,  OSlav.  byti,  ‘to be’,  by  lit,  ‘was’,  Lith.  buti,  ‘to  be’,  buvo,  ‘was’, OIr.  biu,  ‘I  am’,  buith,  ‘to  be’,  boi,  ‘was’,  OE., OS.,  OHG.  biian,  ON.  bita,  Goth,  bauan,  ‘to dwell’,  Dan.,  Swed.  bo,  ‘to  dwell’,  Lith.  biitas, 'house',  biikla ,  ‘dwelling  place’,  Ir.  both,  ‘hut’. AH  these  words  derive  fr.  I. -E.  base  *bheu-,*bhu-, to  be,  exist,  grow’.  Cp.  bhava,  bhumi-devi,  bhut, big,  ‘to  build’,  bond,  ‘serf’,  boor,  booth,  bound, adj.,  bower,  ‘cottage’,  bower,  ‘the  knave  in cards’,  build,  busk,  ‘to  prepare’,  byre,  the  first clement  in  bylaw,  and  the  second  element  in neighbor.  Cp.  also  fiat,  future,  phyle,  physic, physio-,  -phyte,  and  the  second  element  in  du¬ bious,  eisteddfod,  prabhu,  probate,  prove,  superb, Symphytum,  tribe,  tribune,  tribute, be-  pref.  with  transitive  or  intensifying  force.  — OE.  be-,  toneless  form  of  bi  (see  by);  cp.  OS.  be, resp.  bi,  MHG.,  G.  be-,  resp.  bei,  Goth  bi, (used  both  as  a  pref.  and  an  adverb;  in  the latter  case  it  means  ‘round  about,  by’).  See  by. beach,  n.  —  Of  uncertain  origin.
Derivatives;  beach,  tr.  v.,  beach-y,  adj. beacon,  n.  —  ME.  beekne,  fr.  OE.  beacen,  becen, sign,  signal’,  rel.  to  OS.  bokan,  OHG.  bouhhan, MHG.  boitchen.  OFris.  baken  [whence  MLG. bake,  G.  Bake,  MDu.  baken,  Du.  baak,  baken, ON.  bakn,  Dan.  barn,  Swed.  (fyr)bdk],  ‘beacon’, fr.  Teut.  *baukna-,  which  is  prob.  borrowed  fr. L.  bucina,  ‘a  crooked  horn  or  trumpet,  signal horn’;  see  Kluge-Mitzka,  EWDS.,  p.45  s.v. Bake.  See  buccinator  and  cp.  beckon,  buoy. Derivatives ;  beacon,  tr.  and  intr.  v.,  beaconage,  n . bead,  n.  —  ME.  bede,  ‘prayer;  prayer  bead’,  fr.
156
OE.  bed,  gebed,  ‘prayer’,  rel.  to  OS.  beda,  gibed, OHG.  beta,  ‘request’,  gibet,  MHG.,  G.  gebet , ‘prayer’,  Du.  bede,  ‘prayer,  request’,  gebed, ‘prayer’,  G.  Bitte,  ‘request,  entreaty’,  Goth,  bida, ‘prayer,  request’,  OHG.,  MHG.,  G.  bitten,  ‘to ask,  request’,  OHG.  beton,  MHG.,  G.  beten,  ‘to pray’,  Goth,  bidjan,  OE.  biddan,  ‘to  ask,  pray’. See  bid.
Derivatives:  bead,  tr.  and  intr.  v.,  bead-ed,  adj., bead-ing,  n.,  bead-y,  adj. beadle,  n.  —  ME.  bedel,  fr.  OF.  bedel  (F.  bedeau), a  Teut.  loan  word.  Cp.  OE.  bydel,  OS.  budil, MLG.  bodel,  boddel,  MDu.  buel,  Du.  beul, OHG.  butil,  MHG.  biitel,  G.  Biittel,  which  are formed  fr.  OE.  beodan,  OS.  biodan ,  etc.,  ‘to  an¬ nounce,  proclaim’,  with  agential  suflf.  -el,  -il. See  bid  and  agential  suff.  -le.
```


## [2026-09-04T18:31:45.483Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=3200 && NR<=3300 && /^[0-9]{1,4}$/ {print NR\": \"$0}' KLN_1966.txt; echo \"--- leaf index for line 3277 ---\"; python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt'\nlines=open(p,encoding='utf-8',errors='replace').read().split('\\n')\ndef leaf(n):\n    return ''.join(lines[:n]).count('\\f')\nfor n in (3277,4585,17390):\n    print(n, 'leaf', leaf(n))\nEOF"
}
```


### [2026-09-04T18:31:47.639Z] TOOL RESULT

```
3233: 96
--- leaf index for line 3277 ---
3277 leaf 63
4585 leaf 93
17390 leaf 384
```


## [2026-09-04T18:31:52.247Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=17300 && NR<=17450 && /^[0-9]{2,4}$/ {print NR\": \"$0}' KLN_1966.txt | head"
}
```


### [2026-09-04T18:31:54.098Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:31:57.227Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=17100 && NR<=17600 && /[0-9]{3}/ && length($0)<12 {print NR\": \"$0}' KLN_1966.txt | head -20"
}
```


### [2026-09-04T18:31:58.906Z] TOOL RESULT

```
17109: 698
17123: 699
17150: 700
17159: 701
17184: 702
17195: 703
17236: 704
17250: 705
17271: 706
17279: 707
17306: 708
17314: 709
17339: 710
17349: 711
17381: 712
17393: 713
17419: 714
17442: 715
17485: 716
17486: 717
```


## [2026-09-04T18:32:08.013Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"vacar\\|vāčar\\|bāzār\\|bazar\\|bâzâr\" HRN.txt | head -20; echo \"=== leaf 59 (p.38) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==60' HRN.txt | head -60"
}
```


### [2026-09-04T18:32:09.494Z] TOOL RESULT

```
1821:1466. bäzär 'Markt', bazargan, hazergän Kaufmann'.
1823:phlv. f)ä6ar *Markt' (vergl. arm. LW. vacar^ vacara-
1824:kan^ vacarik, und Xüfistän vajär, Nöldeke, TabarT-
1825:übersetzung, 13 Note 3), ba£ar (PP61.), vacarakanth
2257:mäz. bazarg.
22486:vacarakan 166.
22487:vacarik 166.
=== leaf 59 (p.38) ===
Die Praeposition findet sich nur in der jüd.-pers.
/ Bibelübersetzung.
1466. bäzär 'Markt', bazargan, hazergän Kaufmann'.
g. vijüLrx Käs. böz6r, vö}6r.
phlv. f)ä6ar *Markt' (vergl. arm. LW. vacar^ vacara-
kan^ vacarik, und Xüfistän vajär, Nöldeke, TabarT-
übersetzung, 13 Note 3), ba£ar (PP61.), vacarakanth
•Handel' (PPGl.).
Wegen phlv. c ist die Zusammenstellung mit ap.
abaiaris^) unmöglich.
np. bäzär ist allgemein entlehnt.
167. häzvL *Arm'.
g. bat (aus *baht), Kas. bot, böht böhu etc.; ""inNZ
(Is. 3, 20).
aw. bäzu' *Ärm'; phlv. bäzüh^). bazak]masih^) (ZPGl.);
ai. bahü-,
kurd. bOsk, bäsik: bei. bozk (35).
LW. arm. bazuk (H. No. 48); oss. d. bäzug (Hübsch-
mann, S. 120, v. Stackeiberg, 3AMSTKA 5).
Gehört hierher auch np. boz 'Klafter (Vullers: 8),
'Spanne' (Vullers: 9)^), vergl. boze, also ursprünglich
'Armlänge, Elle'? Dann würde np. yüz 'Elle' (vergl.
sestyazt kernend. Sahn. I, 59 Vers 474) wohl nur auf
falscher Punktation beruhen und phlv. väz (AV.)
müsste für bäz stehen.
\;i68. haften 'weben', baf, n^ND 'Garbe' (Jer. 9, 21).
g. vaftmün.
Nach Bezzenberger bei Fick, Vergl. Wörtbch.*, I, 326
'Gemeindeweide', zu ai. sabhä- *Sippe*, das auch schon Darmesteter)
^t. ir. II, 131 in abä gesacht und wogegen Bartholomae, Litbl. f.
or. PhiL I, 19 sich ausgesprochen hatte.
Bartholomae schlägt mir brieflich für ap. ahäcuris die folgende
Etymologie vor: a(m)häcari8 d. i. a(m)ha'\-äcaris'^ zu ambhas' oder
*ahhas- vergL Geldner, KZ. 28, 186, zu äcan's vergl. ai. öXrard-,
demnach würde aCmJbäcaris 'Wasserwerk, Brunnen* bedeuten.
«) Vergl. Hörn, KZ. 32, 582 No. 8.
') Vis und RSmIn S. 82 Vers 10 steht bäz als 'Spanne' (ein Grab
von 60 Spanneu).
```


## [2026-09-04T18:32:28.119Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD wazar ===\"; grep -n -i \"wʾcʾl\\|wazar\\|wāzār\\|wcʾl\" PHD_mackenzie.txt PHD.txt | head -10; echo \"=== NYB ===\"; grep -n -i \"wʾcʾl\\|wazar\\|vacar\" NYB_vol2_glossary.txt | head -10; echo \"=== HUB ===\"; grep -n -i \"bazar\\|bāzār\\|vacar\" HUB.txt | head -10; echo \"=== BRT abacari ===\"; grep -n -i \"abacari\\|abāčari\\|vahā\\|vaha-\" BRT.txt | head -20; echo \"=== KNT ===\"; grep -n -i \"abacari\\|abācari\" KNT.txt | head"
}
```


### [2026-09-04T18:32:28.235Z] TOOL RESULT

```
=== PHD wazar ===
PHD.txt:649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
PHD.txt:2734:market wāzār,
PHD.txt:2783:merchant wāzāragān.
PHD.txt:4042:trade pēšag; wāzār(a)gānīh.
PHD.txt:5254:naf, wiz 12waz-, wüz- wazar wāzāragānīh wāzāragān wāzīg
PHD_mackenzie.txt:5295:wAzAr [w)e)ll M w)e)r-, N bazar] market.
PHD_mackenzie.txt:5296:wazaragan [w)c)lk)n l I M w)e)rg)n, N haztirgan] merchant.
PHD_mackenzie.txt:7051:market wazar.                                warm, wir, wiromandih.
PHD_mackenzie.txt:7055:marrow mazg.                               merchant wazaragan.
PHD_mackenzie.txt:7821:trade pesag; wazar(a)ganih.              truth rastih, wabar, wizurdih.
=== NYB ===
4116:Cod. K has wel 818, is wanting for Mx 2719; the other MSS have weyl = vicir in both places, accepted by S and A. BQ quotes NP vajar, vacar ‘judicial decree’ from the legal language, probably from Zoroastrian usage. Olr *vi-cara- from vi--car- (v. the preceding w.) which also signifies in Skr ‘to perform, to accomplish’ (caus. vi-cärayati ‘to deliberate’, v. vicär- tan). From this vi-car- also inf. vicurtan ‘to perform, to bring about’ DkM 834}, pt. vicurt, vicart ‘valid, authentic, true’, v. Dhabhar, PYV, Gl. 177. Cf also NP guzar, guzir ‘remedy, help’, also guzard; guzardan ‘to apply a remedy’. Arm. lw. véar ‘payment, achievement’, véar-em ‘to accomplish’ (< vicar- or vicär-).
=== HUB ===
4710:= bazOrgan von bazar *Markt'.
5429:in pairivara-; bazar *Markt' = paz. vazar Shk. 272, phi.
5446:vacar, arm. vacar-^ baftan *weben, baL gvafay, d. weben;
5606:*Handel, Markt' = np. bazar -^ vank, vang Xaut* = np. bang;
8048:*Luft zuf acheln ; bazar *Markt' = arm. vacar ; pazam *koche',
=== BRT abacari ===
8140:•  j.,  g.  ux$a-  I)  Adj.  '(von  den  Göttern) verkündet,  geoffenbart',  xmv  m\t  vahA- n.: im,l  at  °'i„j  vüM  . .  fravaocäma  Y.jj.9;
20624:AbleiL;  vgl.  ninmyatdavaHa-,  —  ai.  miyidha- m.,  np.  miyazd,  gelW.  —  Pii. ;  transskr.  (myacif), erl.  (lu  N.  6/):  ,^rd!/,  {zu  Y.  34):  tar  {,  Sä.: /Aalam),  Npü.  (nu  A.  3,  3) :  xurdan  (,  Sü. ;  ähä- rah,  —  I)  Im  Gegensati  lu  zai^rä-\  vgl.  pä- /i^wä-.  —  1)  Rynt.  Dicht  in  Ordnung.  Pü. : äahisn  Bsän  maidayasnän  3  an  ralih  u  myasä ke  pa  mi%Sksarm.  —  3)  Nach  der  proo.  Dekl.
29431:•  j.  hani-flraB'a-  m.  'Gegner,  Widersacher': vUämn  (sd.)  paskät  '%}m  Jantärim  pars dulmainyüm  Yt.iy.ii;  —  •'^»m  *paiii.- yBiliStS  (sd.)  Yt.  j^.  107;  r.^35;  —  ye^fie hasannm  vasyanqm  patti  °%ai  jasaiti Yt.iO.69;  —  y^  ^/rq/(sd.)  ia^  *^a\a.. sHja  mjainti  '%S  (AP.)  Yt  /o.  7 1 ;  13.  33; —  narqm  . .  *ia'^ravanan/qm  'S/  Ny. j.io;  —  Aa'hra.nivaitSm  •'^anam  aurvaha- namtbi^antqm  Y.57.b6;  YLy.133,  J5.1, V'yt/p;  —  ta  daiAkavö  ti  *'>ä^"  (NP.) YK.io.i.Z'^;-- yai!a..vanäma  vups  *-ä7 (AP.))'  Yt. /O.  34;  —  dämum  (sd.)  . . ^'%anamai  Yt2.  la.
=== KNT ===
```


## [2026-09-04T18:32:38.599Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB context ===\"; sed -n '4705,4715p;5425,5450p;5600,5612p' HUB.txt; echo \"=== KNT abaca ===\"; grep -n -i \"abāca\\|abaca\\|hačā\\|vahā\" KNT.txt | head; echo \"=== LKT bazar ===\"; grep -n -i \"basar\\|bazar\" LKT.txt | head -20"
}
```


### [2026-09-04T18:32:38.684Z] TOOL RESULT

```
=== HUB context ===
Ausserdem : Balx = phi. Baxr und BalXj ap. Baxtri-S^
zd. haxStm (ace); pers./ariwaJcJr (Noldeke, Tab. p.9 Anm.)
= phi. framatOr^), ap. framatar- 'Gebieter (ace. frama-
taram, einmal framataram, einmal framataram geschrieben,
aber wohl framataram gesprochen) ; hazargan Kaufmann*
= bazOrgan von bazar *Markt'.
*) Dlnkart III, Gl. p. 12, West, PT. I, 145; II, 152, 276. -
Zu phi. matan *kommen' gehort phi. y^axarmatar*^ d. i. pasmatar *di8-
oiple* und peimatar 'master*, Dlnkart VII, Gl. p. 2 und 4.— 135 -
Ap. a = mp. a = e = np. i in zirih *Panzer , paz.
2reh Min. cap. 43, 7, phi. zrah?, arm. zrah-U, zd. ^^rdda-.
(oben p. 22), bal. gvazi; bad *Wind* = paz. vad Min. 61.
212, zd. vdta-; bddrang 'Citrone =^ phi. vatrang\ badam
*Mander, sTvend. vayam^ skr. vatama-; baran *Regen' =
paz. varan Min. 61. 212, zd. vara- ; bara 'Mauer , zd. vara-
in pairivara-; bazar *Markt' = paz. vazar Shk. 272, phi.
^) Also ap.
va-
— np. 6a-,
n
vat-
= r, ^^'1 ^*-»
n
vi-
= n bl-
n
vt-
- n 9^'
T>
«T- =
v'r-
- n 9^r',— 155 —
vacar, arm. vacar-^ baftan *weben, baL gvafay, d. weben;
baltdan 'wachsen, phi. caus. valfmdan, zd. vared-^ vareday-,
skr. vardh ; bang *Euf, Stimme* = bal. gvcLnfc, paz. phi. vang,
arm. vank, vang ; ba§ama = vOsama Velum* = arm. varsa-
mak (oben p. 23); bavar 'Glaube' = paz. vdwar Shk. 272,
aus Gusnasp, phi. V(i)sna8p West, PT. I, 173, Anm. 5,
skr. vrsafTLagva- \ Vstasp (Pseudocall. 55, 92) = np. Gus-
tasp, phi. V(i)stasp Yatk. i. Zar. 51, Bdh. Gl. 262, ap. Vis-
taspa-\ Vrhm 'Hyrcanien (EliSe 110 u. s. w.) -= ap.
Vrkana-'^ Vrken (Faustus von Byz. 104) = np. Gurgtn;
vagr *Tiger = np. babr'i (aus bagr?), skr. vycLghra-; va6ar
*Handel, Markt' = np. bazar -^ vank, vang Xaut* = np. bang;
vasx *Wucher' =^ plil. vaxs Ganj. 61. p. 19; vat *schlecht*
= li^.^bad; varaz *Eber (Eznik 66 u. s. w.) = np. guraz;
varapanak-U *Waffenrock' 1 Kg. 17, 38, varapan *Panzer
Thom. Artsr. 37, 2 v. u., eigentlich: *Bru8t-schiitzer zu
np. bar *Brust*; vard *Rose' = np. gul; varz 'Stock' = np.
gurz\ varsamak ^Schweisstuch' = np. bfisclma , vdsama
=== KNT abaca ===
=== LKT bazar ===
817:'Markt'  [Horn  NpEt  S.  38,  Nr.  166].  Das Wort  wurde  im  17.  Jahrhundert  durch Reisende  zunächst  mit  Bezug  auf  orien- talisi-he  Verhältnisse  eingeführt  und  drang dann,  vor  allem  auch  durch  die  Kennt- nis von  1001  Nacht,  in  alle  europäischen Sprachen  ein:  frz.  pg.  sp.  bazar,  it.  ba- zar,  bazzar,  rum.  bazar,  basar;  russ. bazar,  bulg.  serb.  pazar,  cech.  poln. bazar;  eng\. bazar,  bazaar,  ndl.  bazaar, dtsch.  Bazar.  Da  das  Grundwort  stimm- haftes s  [z]  hat,  gehört  sicherlich  auch it.  bazzarare  'täuschen,  betrügen',  siz. bazzariotu  'Betrüger'  hierher  [gegen ML  1010].  [Gorjajew  9.  Kluge  42.  DE GREGORIO  in  ZfromPh  XXV,  747. GrSVociSic  228.
2413:1011.  Ar.  kaisärija: 'Ladenreihe,  Bazar'  (noch  jetzt  in  Da- maskus und  Beirtit  Bezeichnung  der großen  Karawanserais,  vom  gr.  Adj. Kaiaapeia,  d.  h.  der  'kaiserliche',  sc. Markt,  vgl.  Dozy  Suppl  II,  432] ;  hieraus sp.  alcaiceria,  alcaeceria,  pg.  alcaqarias, kat.  (alt)  alcaceria  'die  Waren,  die  im Bazar  verkauft  werden'  [DE  76].
6356:bazar  278
7008:bazar  278
8027:bate(g)a  269 bazar  278
```


## [2026-09-04T18:32:43.697Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '805,825p' LKT.txt"
}
```


### [2026-09-04T18:32:43.754Z] TOOL RESULT

```
273.  Ar.  batn:
'Inneres,  Bauch'.  Hieraus  a)  mit  rotnan. Suffix  und  Metiithesis  sp.  banduUo,  ban- dujo  'Wanst  mit  den  Eingeweiden'.
b)  Bätin,  plr.  bäta'in  sind  'auswat- tierte Kleider',  hieraus  möglicherweise it.  ovate,  ovatta,  frz.  ouate,  sp.  bata 'Schlafrock',  dtsch.  Watte,  engl,  wad, russ.  tmtä  [jedoch  sp.  pg.  algodön  und algodäo  s.  hier  Nr.  1272].  Allerdings ist  der  Nachweis  des  Weges,  auf  dem
das  Wort  in  Europa  eingewandert  ist, noch  nicht  erbracht.
c)  Aus  batn  und  ar.  kaitus  [aus  gr. Kf|Toq  'Walfisch']  ergibt  sich  der  Stern- name Baten-Kaitos  Z  Baleni.  [DE  236. SEYBOLD  in  ZfdWf  X,  222  ff'.  Devic DEt42.  ZfromPh  XXXII,  47.  ML  9 170.
274.  Ar.  batrah:
Sing,  zu  batärih,  butärih  'Rogen,  Ka- viar' [aus  gr.  rapixiov  mit  vorgesetztem altäg.  oder  kopt.  Art.  p;  ZDMG  L,  654]; hieraus  it.  bottarga,  siz.  buttaraca,  vut- taraca  'Kaviar  aus  den  Eiern  der  Meer- äsche', frz.  boutargue,  botargue,  pmitar- gue  'Speise  aus  Eiern  der  Seebarbe,  die gesalzen  und  an  der  Sonne  getrocknet oder  geräuchert  werden'.
275.  Tk.  batrak:
[Nicht  osm.,  sondern  tat.]  'Arbeiter': hieraus  russ.  batrak,  batraöka  'Arbeiter, Knecht;  Arbeiterin, Magd'.  [Gorjajew  13.
276.  Ar.  batta: Einheitsnomen  zu  baft  'Enten'  [aus  pers. bat  'Ente'  Horn  NpEt  S.  51,  Nr.  226] ; hieraus  sp.  pg.  pato,  pata  'Ente',  pg. patinho  'junge  Gans';  pg.  pato  'leicht zu  betrügender  Mensch'  [Constancio Dicc  752  b;  schon  npers.  här-bäf  'Idiot' Horn  a.  a.  0.].
277.  Ar.  bazaga:
'Sich  rühmen'.  Von  diesem  Stamme, vielleicht  von  einem  ar.  Adj.  *bazgän, kommt  siz.  baggianu  'eitel,  dünkelhaft' und  it.  albagia  'Eigendünkel',  Adj.  al- bagioso.    [GrSVociSic  228.
'Markt'  [Horn  NpEt  S.  38,  Nr.  166].  Das Wort  wurde  im  17.  Jahrhundert  durch Reisende  zunächst  mit  Bezug  auf  orien- talisi-he  Verhältnisse  eingeführt  und  drang dann,  vor  allem  auch  durch  die  Kennt- nis von  1001  Nacht,  in  alle  europäischen Sprachen  ein:  frz.  pg.  sp.  bazar,  it.  ba- zar,  bazzar,  rum.  bazar,  basar;  russ. bazar,  bulg.  serb.  pazar,  cech.  poln. bazar;  eng\. bazar,  bazaar,  ndl.  bazaar, dtsch.  Bazar.  Da  das  Grundwort  stimm- haftes s  [z]  hat,  gehört  sicherlich  auch it.  bazzarare  'täuschen,  betrügen',  siz. bazzariotu  'Betrüger'  hierher  [gegen ML  1010].  [Gorjajew  9.  Kluge  42.  DE GREGORIO  in  ZfromPh  XXV,  747. GrSVociSic  228.
279.  Ar.  bazrn-katünä:
Aus  ar.  bazr  'Samen'  und  katünä  [wohl pers.  Ursprungs;  ar.  auch  kasisa  al- bar  gut,  d.  h.  'Flohkraut']  'Flohkraut, Plantago  psyllium'.  Hieraus  sp.  zara- gatona,  pg.  zaragatoa,  zaragota  'Fioh- kraut'.    [DE  365.
280.  Ar.  bazz:
'Feine  Leinwand',  ebenso  tk.  bazz,  bez;
Ar.  bazza.]
24
hieraus  rum.  b<i:ea,  basea  '^ekflperter Barchent".  Auch  fiz.  ba.nn  'ilass.'  ge- hört liierhin  Iwährend  es  üblicherweise als  Verstümmelung  aus  boiiibasin,  lat. bombiicimcs  aus  lat.  honibtjx  betrachtet wird).  Poln.  bezextan  'Murkt'  [aus  pers. büzistän  'Stofflagcr'  mit  dem  pers.  Suf- fix -stän  zur  Bezeichnung  eines  (Jrtes, s.  hier  Nr.  332].  [Löbel  EITAP  12. Karlowicz  422.
281.  Ar.  bazza:
```


## [2026-09-04T18:32:57.110Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT ===\"; grep -n -i \"^bazaar\\|bazaar\" SKT.txt | head -5; echo \"=== FSD ===\"; grep -n -i \"vacar\\|bazaar, n\" FSD_vol1.txt | head -5; echo \"=== WEB ===\"; grep -n -i \"bazaar\" WEB_vol1.txt | head -5; echo \"=== SBK 3rb ===\"; grep -n \"عرب\\|عبر\" SBK.txt | head -20"
}
```


### [2026-09-04T18:32:57.219Z] TOOL RESULT

```
=== SKT ===
=== FSD ===
=== WEB ===
18324:3. a public performance at a theater, a dance, a bazaar, etc., the proceeds of which are given in aid of some individual, group, or cause.
70312:2. a festival or carnival where there is en- tertainment and things are sold, often for charity; a bazaar.
=== SBK 3rb ===
170:کتبی که ازفارسی بعربی ترجه شد > > ۱۵ > ۱۵۸ 
172:تاریخ ویسی‌درعرب & € ۱۵۹ :۱ 
281:تندروی ادبا درادخال لفت عرب 
483:تر کیب‌فعل فارسی بامصدر عربی € 4 ۲۰ 4 1۲۱ 
530:عرب ۰ دیگر تتبعات ومطالمات درمتن زبان‌فارسی وفرا گرفتن قواعدناقصزبانوتاریخ لفت 
545:و نشر تواریخ قدیم عرب مانند تاریخ طبری و مسعودی و بعةو بی و دینوری و غیر دم 
559:هخامنشی واشکانیان و ساسانیان طبق منابم عربی و فرنگی و آشناشدن با « ااستا » 
624:کلمات و انتخاب الفاظ وطرز عبر _ سبك بيك اثر ادبی وحپه خاص خود را از لحاظ صورت 
1182:الف ۔ زبانیای سامی مانند عبری دعر بی و آرامی که رود بان نامیده شد . و در 
1407:بعنی ز ندة هیرا - وعربان : << ی ناطق‌عیت» معني کر ده | ند . دراوستا و« K3‏ مرتن € ودد یپلوی 
1474:نیز بدان اشازه شده دمسعودی مورخ عرب و<هعی دیگر از مورخان اسلاهی: هم‌نقل کر ده‌اند 
1518:محمد رسولعرب بروت ات 
1596:آذر پاف مار سپندان = که هو بدی بز رګ و سخنگوئی گرانهابه بود ۳ بهص مور خان عرب 
1862:۱ - جنات ار بءه که عربذ کر کردها ند: غوطةد مشق ۰ | بله» شعب‌بوانفاوس وسفدسی قند, 
1916:ج ) غالب عبارات فارسی که در کتب عربی از قول شاهنشاهان ساسانی ورجال 
2010:بدست نمی آورده اند و آنچه گفته و نوشته اند بعربی بوده است بر خلاف خر اسان و 
2011:سیستان که بواسطة دور بودن از پایتخت دولت عرب و داشتن امیران مستقل د گردنکش * 
2021:دیری دنگ عربی بخود گر فته بود و ادبای آن‌سامان درس ر ودن‌شعر و الف کتاب بربان 
2022:عربی دست کم از مردم سایز شورستانهای غربی و مر کزی وشمالی نداشتند. د با مراجعه 
2025:که‌توجه سامانیانو پمضی از صفار بان و غز وبانبهمرعربی کمترازتوجه آل بو ب4وصاحب
```


## [2026-09-04T18:33:02.563Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1160,1230p' SBK.txt"
}
```


### [2026-09-04T18:33:02.615Z] TOOL RESULT

```
فر گی است . ۳ Langues Aggulinantes-‏ 

Basques. 4 


— ۷ - 


ose 5 


نور بی ( جنوب مصردر آفریقا ) مردم ۶ هوت نت ۰ مردم کا و سباه پوستان افریقیا. 
7 مردم استرالیا . 

سوم ۔ بخش زبانہای پیوندی" - در این ذبانها بر دیشه و ماد لفات هجا هائی 
افزوده میشود ولی نه تنپا با خرديشه . بلکه بآخرو اول ریشه هم ب دیگر اینکه ده لفت 
براثرافزایش تفییر هیکند .گوئی که ریه با آنچه بروی افزو ده شده است جوش خورده د 
پیو ند یافته‌است - بخلافزبان ملتصق که چون دیشه تغیر نمیکند هجاهائی که برد يشه افزوده 
است مث ل آن است که بر بشه چسبانده باشند نه با اوپیوسته باشد . 

زبانپای پیوندی اینهاست : 

الف ۔ زبانیای سامی مانند عبری دعر بی و آرامی که رود بان نامیده شد . و در 
عد قدیم زیانپای فنیقی دبابلی و آشوری وزبان مردم قرطاجنه که شعبة بوده اند از فنبقیان 
وزبان حمیری . 

ب زبانی‌ای عردم هند و اروپائی بمعنی اعم : ار یائیان هند - اریسالیان ایران ٤‏ 
پونانیان - ایتالیئیان - مردا سأّت (بومیان اروباقی غربی) ژدمنی (آلمان و آنگلوساکسون 
و مردم اسکاندیناوی) _ ك و لیتوانی و سلاد ( که روس و سلادهای شرقی ادوبا دمردم ۱ 
بلفار وصرب «سایرسلژوهای بالکان با شند ) ۱ 

عا مای زبان شیاس ا آنند که ذ بانپای بخش سوم ازمر احل زبانای بخش اول و 
دوم در گنشته دار قی کرده تابدیندرجه رسیده است - رمنی این دبانها مستقلا درسي ر نطو ر 
کمال‌بافته د بمرحله‌ای رسیده‌است که| کنون مشاهده ميکنیم؛ ومادراین باره بتفصیل گفتگو 
خواهیم کرد : 

۲“ زبان بار سی 

فارسی ز بانیست که امروز بیشترمردم ایران وافغانستان وتاجیکستان و قءتی اژهند 

و تر کستان وقفقاز دبن النهرین بدان زبان سخن هیگویند ونامه مینویسند وشەرهیسرایند. 


Flectives [۳ Caffres - Y Hottentots - \ 

£ س زبان فارسی در بعضی از افعال قیاسی ملتصق استو لی‌درغا لب افعال سماعی وقیاسی 
غبرتام و تر کیبهای مزجی در شمار زبانهای پیوندیست و این حاات از امتزاج لرجه‌های مختلف و 
شاخه‌های گو نا گون ز بان‌های ایرانی در یکدیگر موجود شده‌است . 


بت ۳ مه 


تاریخ زبان ایران تا هفتصد سال پیش از «سیح دوشن و در دست است و از آن 
پیش نیراز روی! گاهیهای علمی دیگرمیدانیم که ددسرزمین پهنادد ایران- سرذمینی که از 
سوی خراسان (مشرق) بمرزتبت وریگزاد تر کستان چین و از جنوب شرقی بکشودپنجاب 
واز نیمر ود (حنوب) سید و خلیج بارس و بحرعمان واز شمال بکشود سکاها و سارمانها 
(جنوبی دوسییهامروز) تادانوبویونان داژمفرب بکشورسوربه‌ودشتحجاز #یمن‌می‌پروست 
مردم بزبانی که ریشه داصل زبان امروزماست سخن میگته‌اند . 

زرتشت پیمبر ایرانی میگوید که ایرانیان ازیسرذمینی که * آیران ویچ » نام 
داشت و ویز ایرانیان بود » بسبب سرمای سخت و پیدا آمدن ادواح اهریمنی کوچ 
کر دئد و بسرزمن ايران در ۳ . دانژمندان دیگر نیز در بافته اند که طابفة » ات ۰ 
ازسرزمینی که زاد گاه‌اصلی آ نان بود بر خاسته گروهی‌بایر ان و گر وهیبهپنجاب وبر خی‌بارو با 
شتافته اند ودراین کشورها بکار کشاورژی دچوبانی پرداخته اند وزبان مردم ايران و هند 
وارویا همه شاخه هائی AES‏ از آن بيخ رسته وباژ هرشاخ شاخ دیگرزده وهر شاخة 
ب رگ وباری دیگر گون بر آورده اس . 

درعلم نژاد شناسی مردم اریائی را بپشت شعبه بخش کرده اند و زبان آنانرا نیز از 
يك اصل دانسته‌اند بطریقی که گذشت" .
```


## [2026-09-04T18:33:07.992Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^[^ء-ی]*[۰-۹]\\{1,3\\}[^ء-ی]*$\" SBK.txt | sed -n '1,60p'"
}
```


### [2026-09-04T18:33:09.590Z] TOOL RESULT

```
102:AN ۸ A A A A ۵ ۵ RAA A A 
108:AKAN RAA A A A A ۵ 
148:۱۰۸ 4 ۱۲۰۷ > 
356:&« ۰ 
367:۳:4 
368:۳:۰ 
380:۸ 
538:۰ ۰ 5 
630:۰ ۳ ۰ 4 
636:Conception — ۳‏ 
637:Genré - ۶‏ 
674:۰ 
848:4 ۲ 4 
1015:۳ 
1153:۳ 
1165:— ۷ - 
1203:Flectives [۳ Caffres - Y Hottentots - \ 
1439:1 4۶ ۶ 
1614:9 ۳۳ 
1622:۳ 
1655:۳ 
1668:1 ۳ .9 
2375:۶ 
2410:۳ 
2792:۹" 
2905:۳۹ ۰ ۳ ۰ 
2922:Nes. ۴ 
3014:۰ 
3195:۰ of 
3283:۲ 
3624:۳" 
3637:` Outlina Archai ۳ 
3699:۳-1 )( 
3716:4۲ (u) 
3730:(se)‏ ۲ 
3732:(ri‏ 4۲ 
3736:Ell ۸‏ 
3740:() ۲[<- 
3775:۳ 
3787:2-۱1 (v4) 
3789:4۲--]|] (er) 
3796:8 #۲ (ie) 
3797:۱ 
3804:(۰) = 
3815:Dok | ۲۲ ۲۲ (aû 21۲ (a)‏ 
3817:۲ 
3876:۱ 
3883:(Jii _ ۲۷۰-۷‏ 
3885:۹4 
3913:ZC 6۵ (-e,-o) ZC Na (=e) 
3914:7۶۶ 89 (-e) <F No 
3922:۳>> Fa E Sa (-e,=0) 
3923:۳۳ ca TF $a (-e,-=o) 
3927:<۳> Ja (a) ۲> Fa (-e,-o) 
3930:۲2 Ka 7۳ Ve 
3934:~r Ma < ۲ 22 )-۵,-۵( 
4610:۳ ۱ 2 2 
4680:۳۰ 3 
4681:۳۱ ۴ 
4779:۳(
```


## [2026-09-04T18:33:13.409Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"مقلوب\\|عبری\\|بیابان\" SBK.txt | head -30"
}
```


### [2026-09-04T18:33:13.461Z] TOOL RESULT

```
1182:الف ۔ زبانیای سامی مانند عبری دعر بی و آرامی که رود بان نامیده شد . و در 
1930:« یا اهل خراسان مردمان خانه بیابان هستید برخیز ید » داین دوعبادت هم بز بان‌ددیست. 
3360:دین دبیری س خطوط اسلامدی تب خط فنیقی ب عبری = 
3448:عقیدة دیگری نیز هست که گویند خط فنیقی و خط عبری از خطی دیگر که نمونۀ 
3453:الفبائی دنیای قدییم بوده . خط عبری و سریانی و تبطی و عربی د مسند و آرامی و 
3473:کردن چراگاه وخورش‌سوی خوارزم وایر ان رهسیار شدند غالا هر دمی بیابانی دچوبانو 
3660:این نمونه بهیثه شامل سایر خطہا مانند هیر یوغاف و فنیقی د فنیقی قدیم و عبری د 
3967:مربع (خط عبری) دیده میشود . در اینصورت معنی ندارد که اصلاح خط میخی از ناحیۀ 
4024:در اصل ل ہی می‌شود بد طا قدیم 1 یکی فينية یس قی [ دبک ر عبری است. 
4039:در اخبار بو آمده است که «عبری» نام « ابراهیم » جد بز دگ بنی‌اسرائیل 
4041:ار دن است با اور فرات ونت ی گویند » عبری ۰ نام کن از اجداد ابر اهیم بوده است. 
4042:وعلمای معاصر ترجیح میدهند که عبری دا ازماد ه عبور گرفته د آنرا شامل بنی‌اسرائیل که 
4047:باید دانست که اقوام عبری اختصاص بفرزندان « ابر اهوم » داشته‌اند چه طوایف 
4061:و چون اين دو کتیبه er!‏ شباهت ندارد ۰ تصور کرده‌اند که خط فنیقی از خط عبری گرفته 
4211:شکل باخط دیگ ر تفاات داشته است وماصودت‌خطوط قدیم عبری « فندقی و آرامی و 2طوط 
4494:سافی مانندعبری وکلداني وغبره واقف باشد . متأسفانه علمای زردشتی هند که ازهردوی این وسایل 
4769:شده‌بودوآتر ا«قلم‌عبری» 
7403:زبانهای یو ناتی دهندی د قبطید عبری باردیگر بزبان‌سریانید پهلوی تر جمه‌شد. 
7804:بکتاب آخربدانیم_ونیز فضلائی‌چونابن خر داذبه‌وبعدها اصطخر ی و سپسابعبری 
8953:هور کلمن» که‌اصل ترتب‌غط فینیقیو عبری دآرامی بودوخط پهلوی‌نیز بهمان 
10124:را بطر یقمقلوب ادا کنند وازین عمل گاهی‌لفت فدرم آزبین‌مبرود و گاهی‌دولغت بوجود 
11300:لغاتی که درزبان عرب دیده می‌شود که‌نظیر آنهادر سایں ملل‌سامی از عبری و سربانی 
11477:نین عربی‌همان‌لفت است واین هردولات دراصل عبری یکی‌است . مثل کنشت که عربیآن کنیسه است 
12407:چماق - غرغاول - ساو - قراول (قلاور - قلاوز ظ ازین ماده با مقلوب آنت ؟) 
16249:ناحیت مشرق ازاوبیابانی اس ت که بغوروخوارزم پیوسته است وناحیت شمال بفوروبعضی
```


## [2026-09-04T18:33:22.626Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4030,4060p' SBK.txt"
}
```


### [2026-09-04T18:33:22.683Z] TOOL RESULT

```
عبر بان که بدون شك از ملل‌سامی‌نژاد می باشند از شبه حزيرةٌ طور سینا و بقول 
استاد مر گلیوس از بمن‌و رقول‌دانشه‌ندی‌دیگراز حجاز که زاد گاء اصلی آن‌قوم‌بوده‌است 
بر خاسته و بعادت صحرا گردی و بادیه‌نشینی هجرت کردند و عاقبت در حوالی قرن سیزده 
قبل از میلاد در حدود فلسطین و ارش کنعان با کنعانیان همسایه شدند و بعد ازجنگهای 
خونینی وارد فاسطین گردیدنده ,مدها شپر اروشليم را عمارت کرده در انجا خانه کردند 
نام «عبر ک» ازماد ه «عبر» وبمعنی عبور وحر کت و اشاره بصحرا نوردی آن طایفه است ‏ 
بمناسیت » اسر الیل « که لقب (« عوقو ب» بوده 4 نى اسر اليل موسوم شد ند . 

در اخبار بو آمده است که «عبری» نام « ابراهیم » جد بز دگ بنی‌اسرائیل 
است که از شهر «اور» کلده گریخته و از نېر عبور کرده است - و ععلوم نیست که این نهر 
ار دن است با اور فرات ونت ی گویند » عبری ۰ نام کن از اجداد ابر اهیم بوده است. 
وعلمای معاصر ترجیح میدهند که عبری دا ازماد ه عبور گرفته د آنرا شامل بنی‌اسرائیل که 
از صحادی عبور می کرده ودرحال بدوی یز بسته‌اند بشمارند _ چنانکه جر را هم ازهمین : 
ات 8 دبہمان هعنی میدانند وثلائی مجر د يەنى اصل د زیده‌فصل «عبر» و« « 

را یکی‌دانند که‌بقاعدة قلب لفات اختلاف یافته است ,۱ 
باید دانست که اقوام عبری اختصاص بفرزندان « ابر اهوم » داشته‌اند چه طوایف 


(۱) رك = تاريخ اللغات ااسامیه ص ۷۹ - ۸۰ - ۸۱ وتعدها: 


س لس 


دیگری نیز باین‌تام خوانده شده‌اند که پعدها با اعراب e‏ آمیخته و ازیوودحداشده‌اند. 
ده 4 
قدیمتر ین نمونه‌ایکه از خط فنیقی بافته‌اندء کتببه (ستونمهزا) است که تاریخ 
أن به ۸٩۵‏ ق ۰ میرسد - دیگر جامی است سه قطعه که در حزیر قبرس یافته‌اند که 
تاریخ آنرا با عہد «سلیمان » پادشاء بپود ۹۷۱ ۔ ٩۳۱‏ ق م به‌حدس وتخمین‌برایر گرده‌اند
```


## [2026-09-04T18:33:44.255Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"بازار\" BQT_v1_pages.txt | head -20; echo \"=== count pages ===\"; python3 -c \"\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nprint(len(t.split('\\f')))\""
}
```


### [2026-09-04T18:33:45.863Z] TOOL RESULT

```
1210:بازار زبان ۵ری نفان یافت ومنیاشیر و عبود و رسالات بدین عبارت
1788:ناصرالدین‌شاه برای‌اینکه‌چیز نو ببازار آورند بتاراج‌دسانير دست گشودنده
2028:کتاب‌العین در بازار طهران بفروش رفت وبرسر مالکیت آن‌ماجرایی در
4160:بادام » باده » باران » باریدن *"بازار » بازو » باغبان » بسامداد »بخشش »
5897:۲ بار - بروزن بازار (۵) » سرب سوخته
16717:ن‌ بازار - در پهلوی و [در: هوحتان واچار ‌ سوق‌الاحواز ۰ رك 0 خوزستان ]
16790:پاز ر گان - بتح‌اك. مخنفبازارگان
32458:بازار تهران).
=== count pages ===
777
```


## [2026-09-04T18:33:48.846Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=16800 && /\\[pdf page/ {p=$0; n=NR} END{print n\": \"p}' BQT_v1_pages.txt; echo \"---\"; sed -n '16700,16800p' BQT_v1_pages.txt"
}
```


### [2026-09-04T18:33:50.557Z] TOOL RESULT

```
: 
---
خواه کردن باشد ۷ . ۱
باز ار خاك - بکررای‌بی‌هطه وخای
قض فراز باشد - وبازماندن و واماندن بمعنی
طرمیدن هم هست- و بمعنی تمیز کردن وغرقه
لمودن میان درچیز باشد - و پمعتی جداه‌عت
_که بربی فصل کوبند - و بمعنی عکس و قلب
نیزآمده است - وشراب راهم میگوبند که‌بعریی
خمر خواشد - و سوی و طرف و جالب را یز
کنته اند - و پیعتی گذر کاه سل هم آمده
است - وباج وخراج‌را لیز کویند, و باینمعنی
بازای فارسی هم‌درست ات
باز س بنزای فارسی » بروزن و «حنی‌باج
و خراج باشد. و آن زرست که زبر دستان از
زبردسان گپررند بمنی پادشاهان یزركك ازیادشاهان
کوچك‌سنانند ؟ ؛ومالیکه حکام از رعابا وراهدار
از سودااگر گرند - و جزبه را نز گفته اید»
وآن زری باشد که ملمانان ازکافران‌یگ ود -
ن‌ بازار - در پهلوی و [در: هوحتان واچار ‌ سوق‌الاحواز ۰ رك 0 خوزستان ]
( یز 02227 .م ) » فریزندی ویریی 2286 , نطنزی 9202۲ «ه . ۱ص ۲۹۰ > , ممنانی
۲ منگری ۷۵28۲ , سرخه ؛ لاسگردی و شهمیرزادی 08226 « د . ۲ ص ۱۸۸
استی 08226 ده . استی 6۱۱4 ؛ محل خرید و فروش‌کالا وخوراك وبوشالك. لغت فرانة 27هت .
از پرقالی کرفته شده و پرتفالیان یز از ابرانیان گرفته‌اند. «نداب ۳ : ۳- 4. فرامرزی» ورلك :
داگرةالمعارف فرانه .
شه ازسفحهة ۲۱۷
همچنان‌سنگ یکه اوراسیلکرداند زکوه ‏ کاء زین‌سوگاه آ نس وکه فرازوگاه باز
کامرهواری‌چ و کبك و کامجولان‌چونفاب ‏ گاه‌برجستن چوباشه گاءب رکشتن‌چوباز.
«فرهنک شاهنامه 4۰-۳4»
2 باریدت - پپلوی ۷۵1020 «بندهش۱۳4» مشتق ازمسدر اوستابی۷۵۲ (باریدن)«بارنولمه
۰ استی ۱۷۵۲15 «. است۱۳۸»» کیلکی 1#46600؛ فرودآ مدن قطراتآب ازابر» بارش, آعدن,نشطه‌دار بالف کشیده و یکاف زده » کتابه ازقالب
آدمیست - وعظمت بشریت رالیز کویتس وکنابه
از رونق اور دنبوی و اخروی باشد .
بار ار گان ۱ - ب کاف فارسی بالف
کشیده و بنون زده » سودا کررا کویند .
باز اکن بافا و کاف بر وزن‌مادرزن,
ژنده وینه‌ای باشد که فقیران ودرویشان برجامه
و خرقه دوزند - و مداخل مانندیرا نیز کویشد
که بضی از سپاهیان‌بریشت گربان جامه‌ینبهدار
و چارقب دوزند چنانکه سر مداخل بر میان هر
دوشانه افتد .
باژ بان ۳ - بازای فارسی و بای ابجد
پروزن کاروان » شخصی که باج و خراج از مردم
و ۳7 و اورابازداره میگویشد وطا نقه‌ای باشند
از ترکان .
باد پیج بروزن‌مارییج.مهرچندست
که بر ربسمان بندند و از بالای گهوارة اطفال
آویزند تا اشان بدان بازی کنند» و آترا بعربی
داداة کوند ؛ ویضی کفتهاند چهارچوب است
و بر آن تخته باجامه‌ای وصل کنند که بمنرلة
کهواره باشد اطفال را - و رسمانی را نی زکویند
۰ بازدار
که در ایام جشن و عید از جایی آویز هد و زنان
ر دختران بر آن نشته در هوا آیند: وروند .
ربامن‌معنی بجای بای‌فارسی بون‌هم آمدماست؟ .
یار خشیی . بکر اك و قح خای
نقطه دار و شین فرشت بتحتانی رسیده و بنون
زده » نوم از بازباشد که پشت‌آن سیاه و ثیره
ريك و چشمهایش سرخ بود.ه و این قس باز ا
نرکان قزل قوش خوانند ۴ ۰
پاز خمید ‏ بکس میم وسکون‌نحنالی
و دال , کیکه بسوان طعنه صدارت کی کند
و یکنابه مشن شخصی را یاز نماید کوبند « باز
خمید » یمنی بطمنه سخن او را کفت و صدارت
او کرد .
باردار - بر وزن رازدار ۰ برزیگر
و زراعت کننده را گوبند - و میرشکار و صیاد
ونگاه دارندث باز را عم کقته‌اند ٩‏ - وشخصی را
نیز کوب دکه مردمرا از کاری وازچیزی بازدازد
و منم کنه - وامر ببازداشتن و خنم . کردن عم
2
باژ۵اد - بای فارسی بر وزن تانجداره
بمعنی بلجبان باشد بعنی کسیکه باج وخراج از
است . رک : بازر کان .
۴ آقای نفیسی نوشته‌اند (بادنامه پورداود صس۲۱-۲۲۰۶: در بارٌ چند لفت فارسی) : «باز پیچ »
پیداست که این همان چیزست که امروز «تاب» کویند و درتر کی «صاللینجق» نوسندو از محنی
کلمه پیداست که بابد از «باد» مشتق باشد نه از «باز» و تاچار کلمه در اصل «بادییج» بوده وبلملای
قدیم آنرا «بانییج» نوشته بوده‌اند و سپس آرا «بازییج» پنداشته‌اند و دربن بیت ابوالمثل بخاری
که گوید : ۱
زءاك خوشه فروهشته و زبلدنوان چو زنگیانی بریادپیج بازیگو
کلبه را تحریف کردماند. دریرخی از فرهنگها همين کلمه را «بازییج» ضبطکرده‌اند و درمعنی‌آن
نوشته‌اند : مهردای چند که بر رسمان:. . . و مدین ست شهید بلخی استشهاد کردماند :
پی‌مهد اطفال جاعت‌سزد که عقد ثربا شود بازبيج
پیداست که این همان کلمه اس ت که مرینجاً عم جابد «بادییچ» خوائد و عراد از آن هنان‌رسمانی
است که مانند تاب از کاهواره آوبزاست. و عمکن است که برای بازی کودك عهره حابی بر آن
بندند .* ۴ رگ : خشن. ...۰ ۵ - ممرب آن پهردو معنی اخیردییزار» است . «تضی؟.برداعتن
مردم میگیرد .
باز داشتی - کنابه از :ان کردن
ومنم نمودن باشد ۷ .
بان - بای نرسی و دال یبد بر
وزن پاسبان » ظرفی‌را کوبند که زر باج ی که از
مردم میگیرند در آن ریزند .
پاز ر گان - بتح‌اك. مخنفبازارگان
است که سوداگر باشف ۲۳
اد فك » بر وزن باربند » سینه بند
طفلان و پتان‌بند زانرا گوبند .
باژر نگ - با کلف‌فارسی» بر رزنومعنی
باشد .
باز سفید در . کنابه از آفتاب عالمتاب
است . ۱
دار بالف کشیده » فوت ممیزه انسالی را گونند :
باژ گو نه - بازای فارسی . بر وزن
و معنی وا گونه است که بمربی عکس و قلب
```


## [2026-09-04T18:34:08.634Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" BQT_v1_pages.txt | head -3; echo \"---\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf containing line 16717\nimport itertools\ncnt=0\nfor i,l in enumerate(lines):\n    if i>=16717: break\n    cnt+=l.count('\\f')\nprint('leaf idx for line 16717:',cnt)\nEOF"
}
```


### [2026-09-04T18:34:10.166Z] TOOL RESULT

```
---
leaf idx for line 16717: 438
```


## [2026-09-04T18:34:14.717Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 432 433 434; do echo \"===== leaf $((n-1)) =====\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v1_pages.txt | head -40; done"
}
```


### [2026-09-04T18:34:16.179Z] TOOL RESULT

```
===== leaf 431 =====
است که عوام یازهر کوبند و بعربی حجرالئیس
خوانند - وبسنی مهر# مار رانیز بادزهر کفته‌اند
باد ز هر د- فتح رای قرشت ۰ تلم
میضیست و آلرا پعریی خناق گویند .
باد ساده بروزن خاکسار » بمعنی‌سبكك
سیر و رونده باشد - و مردم سبك و بی تمکن
و وقار را ی زگویه .
وخای نقطهدار بالف کشبده » کنابه ازدنیاباشد -
و مودم صاحب‌همت وکریم طبع رانیز گویند .
باث سره بروزن دادگر , صاحب نضوت
و گرونکش و متکیر را گویشد .
باك سر هه بنتح رای فرشت » نوعی از
آزار باشدکه اسب را تهمررسد ۰
پاد سرگ» بک رای فرخت وسکون
بای‌حطی» عجب‌ونکیر کردن ومفرور و گردنکش
مودن ماشف .
باد سنج- بفتم رابم و سکون تون
و جیم » مردم متکبر و خام طمم راکوشه -
وکی را نیز گویند که خیال ها و اندبشهای
باش - بروژن‌خارش ۰ بمعنی بادژاست
و آن سرخی بسیاهی مابل‌باش د که در روی مردم
بهمرسن و آنرا بعضی‌سرخ‌باد میگوبند ؛ و بعطی
مقدمه جذام‌میدانند ۷ .
بادشفا ۵ ح بروزن و ممتی بادژفاماست
که سرخی و کمودنی باشد که در دوی حردم
بهم میرسد ۳ ۰
بادشگام - باکاف؛بروزنو معنی بادشفام
است که سرخی بسیاهی مابل روی‌مردم باشد ؟.
پادشنام - با نون » ب وزن و معنی
بادشفام است ۴ .
بادشوام - باراو. بر وزن‌ومنی‌بادشنام
است که مقدمة دام باشد ۵ .
پا صبا - بنتح صاد . بادی است که از
مابن مشرق و شمال وزد . و باد برین همن
ی
پادغد - بفتح غین تقطمدار وستون‌دال
اطراف آن باد گیر ساخته باشند * .
یأر « بر وزن کاشفر ی یمعتی ماد
غداست که خاةٌ تامتانی و اد گیر باشد۷ .
بادغرد بروزنلاجورد م باد کیروخانةً
===== leaf 432 =====
مار از اعمال هرات و اصل آن بادخیز بوده
است که معل هبوب ریاح باشد ۷ .
باثقر « با فایروزن‌داد کر ؛ جزاومکافات
بدیرا کویند ۴ - و بمعنی خشت بادهم هت
و آن بادزنی باشد بزر که که‌از سغف‌خانه آ ویز ند
و در کشا کش آورند تا بادبهمه جای خائه‌برسد -
وبلد پررا تیز کوند وآن چویی‌باشد تراشید که
اطفال رسمانی در آن می پیچند و از دست رها
را نیز گفته‌اند مدرر که رسمانی بر آن گذارند
وور کثاکتشس آورندتااز آن‌صدابی ظاهر گردد ۴ .
بادفر اه ه ختح تاك بروزن آصفجاه ,
مععتی بادفراست که جزا ومعافات بدی باشد ۲ -
و مسکون ناكك بازبچة اطفال را گوبند وآنچوبی
ماچرمی باشد که‌رسمانی‌بر آن شدندودر کثاکس
آرند تا صدايی از آن ظاهر کردد و آنرا در
خراسان بادفر نگ خوانند بکر فا و فتح‌نون ۴ ۰
بادفر نگ - بکر نا و دابع وفتح
رای قررشت و سکون نون وکاف فارسی .جوششی
بائد بقایت سوزان و دردناك و رنگك آن بزردی
مایل و صاحب این مرض بیشتی اوفات با حرارت
و ب میباشد , و علاج آنرابچیز های سرد بابد
گرا بکون ثالث و فح نون بازیه اطفال
است و آن چوب با چرمی اش د کهریسمان‌برآن
کرود ۵ .
پاذفرو ددین * بسنی بادبرین است
که بادمقرب‌باشد وبعربی باد دبور میخوانند نم
بای ابجد , و بعضی بادبرین را باد صبا میدانتد
مت ۲ -ت
باشد و بسکون الث وفتح رابع و خامس بازيچة
اطفال است وآن چوب باچرمی باش که رسمانی
برآن بندند و حز کتاکش آرند تا صدابی ازآن
طاعر کردد ٩‏
بادفوردنن بفتع رآبع وواو » بمعنی
بادفروردین است که باد دبور باشد و آن تموج
هواست از جانب فرب بطرف مشرف » و مهب
آن میان سهیل و مغرب است . وهشگام آن‌آ خر
روز میباشد برعکس بادسب. وضرر این باد زباده
از نم است. .
باد گان - باکاف فادسی‌بروزن آسمان,
حافظ و حفظ کننده ۷ - و خازن و خزانه. دار
===== leaf 433 =====
کوننه بادام پلیله که خاطران بر یای خود
باد کنجی ۰ بکس الث و شم رأبع
و سکون تون و جیم بتحتالی رسیده » فولنج | بشدند .
و نفخی را گونن که دریشت آدمی بهم‌رسدوسبب باد نج بکسر دال وسکون‌نون‌وجیم »
بمعنی‌تار کیل است و آنرا جوز حندی کوبند .*
باد نگان ‏ با کاف فرسی . بر وزن
و عمنی بلدنجان است و آنرا بعربی حد قگونده
و باین همثی بجای فاف جیم هم بنظر آمده
.ِ
باد و ) - بکسر ثالث و فتح نون و واو
بالف کشیده,صوت, نقص وخواشد کیو کویند کی‌را
آن پشت خم گردد .
باد گنل ۱ - یکس ثاكث و ضم رابم
طرسین و عگون نون و دالامجد , بادی است که
بزر که شود و درد کند ؛ و آن را بعریی فتق
۲
باد گیسو - بکرثاكت , کنابه‌ازضوت
و تکبر و عظمت باشد مرزنانر! چنانجه بادیروت
بش ۴ .
انا
هو داتی! .۰ تورور
پاد ود ود » بمنی باد بهار است -
پادهسیج - ر پادمیجا کنابه از فس و نام لحنی باشد از مویقی.
عبی علبه‌السلام است که مرده را زنده میکرد . : ۱
1 0 با و لیف" منم ثاكربای ابجدبتحتانی
وه ار ات که اد | ویو بداز یاج ینمی ان فامت. را
قفای سرآفمی‌برمی آورند. وآن‌سیامرنگه میباشد.
اک سوه کون مافنضنضه رود
و هر چند بشویند نرود و همچنان صوف داغدار
بماته و امتصان آن باین است . و گزرندگی مار
را بافع است » چون برجاب یکه مار گزیده باشد
بگذاوند فی‌الحال بچسبد - وعوام مه سقیدی‌را
سودمند باشد .
بادودم - نم داد اول و فتح دا
دوم (۱) و سکون میم » غرور و تکبر و عجب
و تجبر و خودستابی و خودنمابی باشد . <
بات هر ات باد شمار راکوند .وآن
٩‏ - م رکب از: باد + کند ( جندص خایه) . ۴ رک : بادیجان و پانشگان.
۴ - در فرهنکگ دساتیر (س۷۲۳4) بهمن معنی آمده ۱
» بادفجای _ باندگان , بلدنگان » ور طبری ۷3۳۵84۳0 < واژه نامه ۸۱۸ » »کلکی
```


## [2026-09-04T18:34:36.158Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"sabhâ\\|sabha\\|abâçaris\\|abacaris\\|abāçaris\\|açaris\\|bâzâr\\|bazar\" DRM.txt | head -30"
}
```


### [2026-09-04T18:34:36.263Z] TOOL RESULT

```
2364:bazar*
5840:§   217.  Suffixe  (a)gnn;  polilvi  akân.  —   On  a   déjà  vu dans  l’histoire  de  la  déclinaison  un  pluriel  abusif  eu  gmt  ^-,15 naître  des  pluriels  en  agân,  que  la  chute  du  g   thématique  au singulier  a   détachés  du  thème  primitif  et  rendus  irréductibles à   ce  thème  (p.  123).  Le  même  fait  s’est  produit  avec  le  suffixe d’adjectif  an,  qui  s’était  produit  avec  la  désinence  du  pluriel  an. Le  thème  *bâzârak,  marchand,  augmenté  du  suffixe  d’adjectif (ht,  donne  bdzâragân  et,  par  suite  de  la  chute  du  mot  bâzârak, bâzârgân  semble  formé  de  bazar,  par  suffixe  gân  :
6577:p.  é   bâzâr,  marché  (perse  abâcari;  vol.  II,  131).
8457:p.  1 1 1   V-tcles  voyelles  finales  (I, §   88),  la  réduction  decmédial  a   z (vol.I,§27,  1°),  l’allongement  fréquent  des  voyelles  brèves  dans les  suffixes  (ef.  §   212.  tin),  abâcari-  (le  sh  étant  le  signe  du  plu- riel) devait  donner  :   bazar  ou  bâzâr:  on  reconnaît  le  persan ^\jl>
8458:Quant  a   l’origine  même  du  mot,  il  est  clair  que  ce  n’est  pas un  mot  simple,  mais  un  composé.  11  se  décompose  naturelle- ment en  ahâ  et  cari ;   dans  cari  on  reconnaît  le  substantif  qui  a donné  au  persan  le  suffixe  de  lieu  (vol.  I,  §   257)  :   c’est  sans doute  un  abstrait  de  car,  aller,  se  rendre.  Reste  ahâ.  Si  les exemples  de  la  persistance  de  h   devant»  sont  nombreux  ( haeâ , hadd,  huma  etc.),  si  cette  persistance  est  la  règle  générale,  elle n’est  pourtant  pas  absolue  :   on  a   vu  plus  haut  (vol.  I,  6),  thà- hati,  thàhahi  écrits  thà-ati  thà-ahi  :   abâ  semble  être  un  exemple analogue;  ce  serait  le  sanscrit  sabhd,  lieu  de  réunion,  réunion. L’ abâcari'1,  le  bâzâr,  est  donc  littéralement  comitii  locus.
8467:1.  Cf.  le  sanscrit  sabhâ-cara,  qui  se  rend  à   la  réunion,  au  conseil  ( JDict . de  St-Pétersbourg,  s.  v.).
```


## [2026-09-04T18:34:48.548Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('DRM.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in (6577,8457,8467):\n    cnt=sum(l.count('\\f') for l in lines[:target])\n    print(target,'leaf',cnt,'-> T2 printed p.',cnt-364)\nEOF\necho \"--- context 8450-8470 ---\"; sed -n '8448,8470p' DRM.txt"
}
```


### [2026-09-04T18:34:50.368Z] TOOL RESULT

```
6577 leaf 335 -> T2 printed p. -29
8457 leaf 516 -> T2 printed p. 152
8467 leaf 517 -> T2 printed p. 153
--- context 8450-8470 ---
M.  Oppert  traduit  :
«Je  rétablis  les  temples  des  dieux  que  Gomatès  le  Mage avait  détruits  et  je  restituai,  eu  faveur  du  peuple,  et  la  croyance et  la  langue,  et  je  rendis  aux  familles  ce  que  Gomatès  le  Mage leur  avait  enlevé».  Il  fait  de  abâcarish,  lu  abicarish,  une  post- position à   kârahyâ  :   il  traduit  gaithâ,  «   croyance  »,  littéralement «monde,  peut-être  le  calendrier»  et  mâniya  «le  langage  sacré, le  rite  »   b
M.  Rawlinson  également  voit  dans  cette  ligne  une  allusion aux  réformes  religieuses  de  Gomatès.  M.  Spiegel  au  contraire semble  y   voir  une  allusion  a   des  mesures  purement  politiques, car  il  traduit  :   die  Weideplcltze  (?),  die  Herden,  die  Wolinungen je  nach  Clanen.
Je  crois  que  c’est  dans  ce  sens  qu’il  faut  chercher.  Gaithâ  et mâniya  rappellent  invinciblement  le  zend  gaetha  et  nmâna  : nmâma  signifie  «   maison  »;  gaetha  qui,  au  pluriel,  signifie  «   monde, l’ensemble  des  choses»  désigne  au  propre  «un  bien  rural,  une ferme».  En  effet,  le  Vendidad,  distinguant  le  chien  de  troupeau du  chien  de  maison,  le  paçvsh-liaurva  du  vish-haarva,  met  la place  du  premier  dans  la  gaetha,  celle  du  second  dans  la  vîç. Le  chien  de  troupeau  est  à   sa  place  (dâityô-gâtu),  quand  il  rode dans  un  cercle  d’un  yujyèshti  du  gaetha  pour  écarter  le  loup  et le  voleur;  le  chien  de  maison,  dans  un  cercle  d’un  hâthra  autour de  la  vîç  (XIII,  17-18  [49-52];  cf.  10-11  [26-35]).
Dans  notre  texte  perse,  gaitlia  et  nmâniya  répondent  à   gaetha et  vîç  du  texte  zend  :   l’emploi  technique  et  plus  large  du  mot vîç  (vith)  en  perse,  emploi  d’ailleurs  également  connu  du  zend2, a   seul  amené  ici  la  substitution  du  mot  mâniya  au  mot  vîç.  La mesure  de  Darius  a   donc  consiste  a   rendre  aux  vith,  aux  clans, aux  grandes  familles,  les  propriétés  rurales  et  bâties,  les  terres et  les  bourgs  qu’elles  possédaient  ou  sur  lesquelles  elles  avaient droit  seigneurial  et  dont  Gomatès  les  avait  dépouillées.
Reste  abâcari  (telle  est  la  lecture  exacte).  Le  mot  étant isolé  en  perse  et  sans  équivalent  apparent  en  sanscrit,  il  ne reste  qu’une  ressource  pour  l’éclairer,  c’est  de  voir  s’il  n'a  pas subsisté  en  persan,  et,  pour  cela,  de  se  demander  ce  qu’il  serait devenu  eu  ce  cas.  Avec  la  chute  des  voyelles  initiales  (vol.  I,
1.  Le  peuple  et  la  langue  des  Mèdcs,  119,  167.
2.  Voir  l’article  Barbît p.  139.
131
p.  1 1 1   V-tcles  voyelles  finales  (I, §   88),  la  réduction  decmédial  a   z (vol.I,§27,  1°),  l’allongement  fréquent  des  voyelles  brèves  dans les  suffixes  (ef.  §   212.  tin),  abâcari-  (le  sh  étant  le  signe  du  plu- riel) devait  donner  :   bazar  ou  bâzâr:  on  reconnaît  le  persan ^\jl>
Quant  a   l’origine  même  du  mot,  il  est  clair  que  ce  n’est  pas un  mot  simple,  mais  un  composé.  11  se  décompose  naturelle- ment en  ahâ  et  cari ;   dans  cari  on  reconnaît  le  substantif  qui  a donné  au  persan  le  suffixe  de  lieu  (vol.  I,  §   257)  :   c’est  sans doute  un  abstrait  de  car,  aller,  se  rendre.  Reste  ahâ.  Si  les exemples  de  la  persistance  de  h   devant»  sont  nombreux  ( haeâ , hadd,  huma  etc.),  si  cette  persistance  est  la  règle  générale,  elle n’est  pourtant  pas  absolue  :   on  a   vu  plus  haut  (vol.  I,  6),  thà- hati,  thàhahi  écrits  thà-ati  thà-ahi  :   abâ  semble  être  un  exemple analogue;  ce  serait  le  sanscrit  sabhd,  lieu  de  réunion,  réunion. L’ abâcari'1,  le  bâzâr,  est  donc  littéralement  comitii  locus.
AFÇÔÇ,  -
Le  pehlvi  afçôç  -ctoey.  persan  raillerie,  insulte,  tra-
duit le  zend  çaoca  dans  le  Hâdhôkht  Nosh  (II,  28,  ed.  Haug)  : z.  vat  tum  ainim  avâenôish  çaocaya  kerenavantem', pli.  amat  lak  zaki  zak  anâ  khazîtûnt  havmaud  amatshân afçôç  kart  :
«quand  tu  voyais  un  homme  qui  se  livrait  a   la  raillerie». afçôç  suppose  une  forme  zende  * aiwi-çaoca ;   c   médial  devient régulièrement  z   (vol.  I,  §   27,  1”),  *   afçôz  :   il  y   a   eu  seulement durcissement  de  la  consonne  finale.
1.  En  moyen  persan,  le  seul  exemple  que  nous  connaissions  du  mot  est dans  le  nom  ancien  de  la  ville  appelée  Ahvâz  ou  Çùq  el  Ahvâz,
littéralement  Marché  d’Ahvâz  ou  du  Khûzistan,  anciennement  Khü- ziçtân  Vajàr,  (fondée  par  Ardshîr;  Mujmil  attevarikh,  Jour-
nal asiatique,  18-H,  II;  Tabari,  tr.  Noldeke,  p.  13,  n.  3).
M.  Halévy  me  signale  le  hongrois  vâsdr,  marché  (prononcez  vâshâr)  que les  Magyars  ont  dû  emprunter  avant  leur  émigration  d’Asie  et  qui  montre déjà  la  chute  de  l’a  initial.
1.  Cf.  le  sanscrit  sabhâ-cara,  qui  se  rend  à   la  réunion,  au  conseil  ( JDict . de  St-Pétersbourg,  s.  v.).
9*
132
Çaoca,  raillerie,  vient  de  la  même  racine  que  çaoca,  combus- tion :   l’insulte  brûle.  Par  une  métaphore  analogue,  la  même  ra- cine çuc  a   donné  le  sanscrit  çoka,  «flamme»  et  «chagrin»;  le zend  çaoka,  flamme,  a   eu  sans  doute  aussi  le  sens  de  chagrin; car  c’est  le  sens  du  persan  çôg,  ^ cf.  l’article  çaokenta.
```


## [2026-09-04T18:34:59.586Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"abicari\\|abičari\\|abiçari\\|pasture\" KNT.txt | head -20"
}
```


### [2026-09-04T18:34:59.635Z] TOOL RESULT

```
1351:pIE *g%el- in ОР car- in abicariš ‘pasture land’, ‘$
2196:III. Apparently there was also a nt. suffix -as-, not varying within the paradigm nor in the corre- sponding masc. formation: type Skt. kravís ‘Taw flesh’, Gk. xpéas. OP nom.-ace. hadiš from *sed- as, cf. ОК. éðos from *sed-os; ace. abicaris *pasture- land’, see Lex. s.v. In names, Hazd-manis, Ardu- mants, perhaps I-mami$; late gen. Haxdmanis- ahyd adds the gen. ending of -o- stems to the nom. as stem.!
2720:1, As a general case-form, added as the last of a series of accusatives: DB 1.64f abicari$ gaifümcü müniyamca v'übiseaà; XPh 50f and 53f Auramaz-
3573:$14. 1.61~71. Saith Darius the King: The king- dom which had been taken away from our family, that I put in its place; I reestablished it on its foundation. As before, so I made the sanctuaries which Gaumata ће Magian destroyed. І restored to the people the pastures and the herds, the household property and the houses which Gaumata the Magian took away from them. I reestablished the people on its foundation, both
5014:(2) Prefix with verb jav-, and first element in abicaris, abyapara, perhaps in Abirddus, but prob- ably not the base of abif. — —
5015:abicari& DB 1.64f, word of uncertain form and meaning, probably asn. of s-stem (5185.11), to abi- + root car- ‘move, go’ (Av. caraiti, Skt. cárati, Lt. colit, 8”; $107), giving, in association
5018:erty’, а meaning ‘pasture lands’, cf. NPers. cáridán ‘to pasture’ (Spiegel, KT, Bthl. AW 89). Cf. also Tm. Lex. 64-5; Gray, JAOS 33.281-8; Hüsing, KZ 48.155-6; Hz. Ар] 51-4.
5379:184 | 631689 V, ОГ car- vb. ‘move’, see abicarig; cf. also under
```


## [2026-09-04T18:35:10.066Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aibi.čari\\|abicari\\|aibicari\\|ap. abi\" BRT.txt | head; echo \"=== try 'ǰari' / column 89 ===\"; python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=t.find('abicari')\nprint('find abicari',i)\nfor pat in ['abiçari','abi.cari','abicaris','abicariš']:\n    print(pat, t.find(pat))\nEOF"
}
```


### [2026-09-04T18:35:12.011Z] TOOL RESULT

```
20309:p.  mäiiiya-  n.  'liegende  Habe'  im  Gegen- satz zu  gaiha-  (Sp.  478  m.):    äyaäana  .  . \iya%'^ärayam  (sd.)  iärahya  abicaris  gai- ^amca  'yamcä  *vi^aibii{sä.)ca  tyddts  gau- mata*  . .  adm/^  Bh./.  14. Et  und  eig.  Bed.  unsicher.  Vgl.  Btiil.  GlrPh.  /. 183,  Fov  KZ.J5.  73,  ZDMG.  J4.346,  Jusn GIrPh.3.4z6.  ZDMG.j;j.9i,G«AvAJPh.3/.  17. j.  inäm>mt!aiml  V.  S.  zl ;  lies  mä  mprin?.
=== try 'ǰari' / column 89 ===
find abicari 2942572
abiçari -1
abi.cari -1
abicaris 2942572
abicariš -1
```


## [2026-09-04T18:35:20.287Z] TOOL CALL #32: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T18:35:20.295Z] TOOL RESULT

```


```


## [2026-09-04T18:35:25.193Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1",
 "prompt": "Give the full Persian etymology of بازار (bāzār): Middle Persian form, Proto-Iranian reconstruction, components, and any cited authorities (Hasandust, MacKenzie, etc.). Also list descendants/borrowings (Turkish, Italian, English, Arabic)."
}
```


## [2026-09-04T18:35:25.344Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/bazaar",
 "prompt": "Give the full etymology chain for 'bazaar' including Italian, Turkish, Persian, Pahlavi forms and dates."
}
```


### [2026-09-04T18:35:31.672Z] TOOL RESULT

```
# Persian Etymology of بازار (bāzār)

## Middle Persian Origin
The word derives from Middle Persian **wʾčʾl** (wāzār), meaning "market."

## Proto-Iranian Reconstruction
According to the etymology tree provided, the word traces back through:
- Proto-Indo-European **\*wes-** ("sell")
- Proto-Indo-European **\*kʷel-** ("turn")

These proto-roots combined to form the Middle Persian term.

## Etymology Statement
The Wiktionary entry states: "Inherited from Middle Persian wʾčʾl (wāzār, 'market'); see it for further information."

## Major Descendants and Borrowings

**Turkish:** bazar, pazar (inherited)
**Arabic:** بازار (bāzār) — borrowed
**English:** bazaar, bazar (via Italian/French)
**Italian:** bazar
**French:** bazar
**Ottoman Turkish:** بازار (bâzâr), پازار (pazar)

The word also spread to numerous South Asian languages (Bengali, Hindi, Urdu), Southeast Asian languages (Malay, Indonesian), and many European languages through Ottoman Turkish and Romance language intermediaries.
```


### [2026-09-04T18:35:32.565Z] TOOL RESULT

```
# Etymology of Bazaar

Based on the Online Etymology Dictionary, here's the documented etymology chain:

**Starting Point (1580s):** The word entered English from Italian *bazarra*.

**Persian Origin:** The Italian form ultimately derives from Persian *bazar* (also spelled *bazar* in Pahlavi as *vacar*), meaning "a market."

**Deeper Roots:** The Persian term traces back to Old Iranian *\*vaha-carana*, literally meaning "sale, traffic." This compound combines:
- A suffix form of the PIE root *\*wes-* meaning "to buy, sell"
- PIE *\*kwoleno-*, a suffixed form of root *\*kwel-* meaning "revolve, move round; sojourn, dwell"

**Key Quote:** According to the source, bazaar comes from "Persian *bazar* (Pahlavi *vacar*) 'a market,' from Old Iranian *\*vaha-carana* 'sale, traffic.'"

The etymology illustrates how Persian commercial terminology entered European languages through Italian during the 16th century, reflecting historical trade routes and cultural contact.
```


## [2026-09-04T18:35:40.739Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/w%CA%BE%C4%8D%CA%BEl",
 "prompt": "Middle Persian wʾčʾl (wāzār): give the etymology, Proto-Iranian reconstruction, components, cited authorities, and descendants."
}
```


## [2026-09-04T18:35:41.841Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=bazaar",
 "prompt": "Give the American Heritage Dictionary etymology of 'bazaar' verbatim."
}
```


### [2026-09-04T18:35:45.449Z] TOOL RESULT

```
According to the American Heritage Dictionary, the etymology of "bazaar" is:

"[Italian _bazarro_ and Urdu _bāzār_, both from Persian _bāzār_; see **wes-**3 in the Appendix of Indo-European roots]."
```


### [2026-09-04T18:35:47.215Z] TOOL RESULT

```
# Middle Persian wʾčʾl (wāzār)

## Etymology
The word derives from Old Iranian *wahā-čā̆rana-, literally meaning "trade-walkabout." The first element comes from Proto-Indo-European *wes- ("to sell"), while the latter derives from *kʷel- ("to turn, revolve").

## Proto-Iranian Reconstruction
**wahā-čā̆rana-** - compound term denoting a marketplace or trading location

## Components
- **wahā-**: related to selling/commerce (cognate with Persian بها *bahâ*)
- **čā̆rana-**: related to movement or circulation (from the root meaning "to turn, revolve")

## Cited Authorities
The article references several scholarly sources:
- Benveniste, Émile (1969) on Indo-European institutional vocabulary
- MacKenzie, D. N. (1971) in his Concise Pahlavi Dictionary
- Mayrhofer, Manfred (1996) on Old Indo-Aryan etymology
- Henning, W. B. (1977) in Selected Papers

## Descendants
The term evolved into Classical Persian بازار (bāzār) and spread across numerous languages including Arabic, Hindi, Turkish, English (bazaar), and many Asian languages through Persian and Ottoman Turkish mediation.
```


## [2026-09-04T18:35:54.090Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^wes-\\|^kʷel\\|^kwel\" AHD_watkins1985.txt | head; echo \"---\"; grep -n -A6 \"^wes-3\\|^wes-\" AHD_watkins1985.txt | grep -i -m5 \"bazaar\\|vaha\\|venal\" ; echo \"=== search bazaar ===\"; grep -n -i \"bazaar\" AHD_watkins1985.txt | head"
}
```


### [2026-09-04T18:35:54.177Z] TOOL RESULT

```
133:wes-pero-. The Indo-Europeans oriented themselves by facing east. Therefore the root deks-, “right,” could also denote “south.” “Right” was considered lucky; the terms for “left” vary from language to language (one Indo-European term is laiwo-) and were evi- dently subject to taboo.
651:kwelek-
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
1157:wes-!
1159:wes-1. To buy. 1. Suffixed form *wes-no- in Latin vénum, sale: VENAL, VEND. 2. Suffixed o-grade form *wos-nd- in Greek dneisthai, to buy: DUOPSONY. [Pok. 8. wes- 1173.]
1160:wes-?. Wet. Germanic *wdés- in Old English wés, juice: 00ZE}. [Pok. 3. wes- 1171.]
1161:wes-3. To stay, dwell, pass the night, with derivatives meaning “to be.” 1.O-grade form *wos- in Germanic *was- in Old English wes, was: was. 2. Length- ened-grade form *wés- in Germanic *wéz- in Old English wére (subjunctive), w#ron (plural), were: WERE. 3. Ger- manic *wesan in Old Norse vesa, vera, to be: WASSAIL. 4. Suffixed form *wes-td- perhaps in Latin Vesta, house- hold goddess: Vesta. 5. Suffixed variant form *was-tu- possibly in Greek astu, town (< “place where one dwells”), whence Latin astus, skill, craft (practiced in a town): ASTUTE. [Pok. 1. wes- 1170.]
1162:wes-‘. To clothe. Extension of eu-'. 1. Suffixed o-grade form *wos-eyo- in Germanic *wazjan in Old English werian, to wear, carry: WEAR}, 2. Suffixed form *wes-ti- in Latin vestis, garment: VEST; DEVEST, INVEST, REVEST, TRAVESTY. 3. Suffixed form *wes-nu- in Greek hennunai, to clothe: HIMATION. [Pok. 5. wes- 1172.]
1163:wes-pero-. Evening, night. I. Reduced form “wes-. 1. Suffixed form *wes-to- in Germanic *west- in: a. Old English west, west: WEST; b. Old English westerne, western: WESTERN; C. Old English westra, more west- erly: WESTERLY. 2. Possibly Germanic *wis- in Late Latin Visigothi, “West Goths” (Gothi, the Goths): Vist- GorTu. II. Basic form *wespero-. 1. Latin vesper, evening: VESPER, VESPERTILIONID. 2. Greek hesperos, evening: HESPERIAN. [Pok. wesperos 1173.]
---
1159:wes-1. To buy. 1. Suffixed form *wes-no- in Latin vénum, sale: VENAL, VEND. 2. Suffixed o-grade form *wos-nd- in Greek dneisthai, to buy: DUOPSONY. [Pok. 8. wes- 1173.]
=== search bazaar ===
```


## [2026-09-04T18:36:04.052Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK wes kaufen ===\"; grep -n \"kaufen\" POK_full.txt | grep -n -i \"ves-\\|u̯es-\\|ues-\" | head; echo \"--- direct ---\"; grep -n \"8\\. u̯es-\\|u̯es-  *: *.kaufen\\|ai\\. vasná-\\|vasna-\" POK_full.txt | head -10; echo \"=== SYN market ===\"; grep -n -i \"bazar\\|bāzār\" SYN.txt IEC.txt | head"
}
```


### [2026-09-04T18:36:04.213Z] TOOL RESULT

```
=== POK wes kaufen ===
--- direct ---
92527:Material: By den einzelnen Sprachen sways e-and ovocalism: Old Indie vasna- m. " 
=== SYN market ===
SYN.txt:20972:Rum. itirg NE market Russ. bazar, rynok (torg) rs céle, marcad Du. markt Skt. panyavithi-, apana-, NIr.  margadh OHG marc(h)at vipana : W. marchnad MHG mark(e)t Av. Stans
SYN.txt:20976:NG woatapi, fr. Turk. pazar, this fr. Pers. bazar ‘market’ (etym.? Horn 166). The Persian word has been the source of a general Eur. borrowing, used more or less generally for ‘market’ as Russ. bazar, or with restricted use as NE bazaar, Fr., Sp. bazar, It. baz(z)ar. Lokotsch 278.
SYN.txt:20997:Russ. bazar, see above, NG wafapu.
```


## [2026-09-04T18:36:09.211Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '92515,92535p' POK_full.txt"
}
```


### [2026-09-04T18:36:09.270Z] TOOL RESULT

```
Old Icelandic veslu. "dress' {*wesala-), ver^ coating, layer' {*waza-); 

Hittite uas-, ues-, Luvian uas(s)-^beV\e\6ev\, lure, tempt '; Tocharian B wastsi, wastsi 
"dress' (neologism); A wsal6s.\ 

References: WP. I 309, WH. II 775 f.. Frisk 521 f. 
Page(s): 1172-1173 

Root / lemma: ues-no- {* haues-no-) 

Meaning: price 

Material: By den einzelnen Sprachen sways e-and ovocalism: Old Indie vasna- m. " 

purchase price', n. "earnings', i/5S/7ay5//"feilscht'; Armenian gin^ purchase price'; gr. hom. 

(I)vo(; " purchase price', Lesbian ovva {*uosnS), Ionian Attic cJbvri " purchase', cbv£0|jai " buy 

', gort. u)vr|v " sell '; Latin venus{ov\\)j in Akk. venum, Dat. veno, later venui) "sale' {vendo, - 

dere' sell ' is *venom+ do, i/e/7eo "verkauft become' = *venom+ eo); marr. eituam
```


## [2026-09-04T18:36:21.288Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK sabha ===\"; grep -n \"sabhā\\|sabha-\\|sabhá\" POK_full.txt | head -10; echo \"=== WLD sabha ===\"; grep -n \"sabha\" WLD_band3.txt incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt 2>/dev/null | head -10; echo \"=== IEC sabha ===\"; grep -n \"sabha\" IEC.txt | head"
}
```


### [2026-09-04T18:36:21.391Z] TOOL RESULT

```
=== POK sabha ===
8281:thereof derived Avestan 1/3/^5/73- 'virile'. Old Indie vrsa-, vrsabha-'buW, i/Zs/?/- 'virile', m. 
27513:seeds ') Old Indie /sa-M^/? "bull', aja-rsabha-h^\\e-Qoa\! , Avestan Old pers. arsan^man, 
=== WLD sabha ===
incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt:7879:Ai. wahrscheinlich in sabha „Yersammlung“ (*,,Zssprechen“ ; bhd- im 
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:9715:„benetzend, Samen ergieBend“) ai. rsabha-h „Stier“, aja-riabha-h „Ziegen- 
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:17092:av. varssna- „mannlich“, ai. vrsa-, vrsabha- „Stier", vrsnl- „mannlich“, 
=== IEC sabha ===
15041:sebh-, sebhi (sobh-) “self; like; kin; separate- (ly. WP II, 123 & 456 Skt. cf. sabha, f. (company, meeting-place'; Av. haba, f. id.; Lat. sibi, Osc. sífeí, ds. 'to self; W ef, efe, efo “he, him’; Cor. cf. nes-he- fyn, m. 'next-of-kin'; Go. sibja, f. ‘kinship’; MHG (Alemannic) sippe, adj. "related: OE sibb, adj. id.; f. ‘kinship, affection, peace’; ON sifjar, fpl. ‘affinity’; OCS sebe, gs ‘of self be- side sobě, o — ‘by oneself ; sobü, m., sobije, n. ‘substance’; OPr. sebei ‘to self
```


## [2026-09-04T18:36:33.924Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TTS ===\"; grep -n -i \"pazar\\|bazar\" incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -10; echo \"=== NYB wazar ===\"; grep -n \"wāzār\\|w'c'l\\|wazar\" NYB_vol2_glossary.txt | head -5; echo \"=== CHEUNG car ===\"; grep -n \"wāzār\\|bāzār\\|bazar\" CHEUNG.txt | head -5; echo \"=== WLD ctx ===\"; sed -n '7870,7885p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
}
```


### [2026-09-04T18:36:34.049Z] TOOL RESULT

```
=== TTS ===
=== NYB wazar ===
=== CHEUNG car ===
=== WLD ctx ===
mehr eine scharf umrissene Gdbed. erkennen lassen, und wegen slaY. 
b^ho „wei6“, aisl. bal „Scheiterhaufen“, die aber Dehnstufe der durch gall. 
Belenos Yorausgesetzten TYz. bJiel- sein konnen (Meillet Et. 17S), gegen 
Prellwitz s. Persson Beitr. 117 f., 509 a 1, der wie Curtius 296 f. bha- ,,.glan- 
zen“ und bha- „sprechen‘^ fiir ursprgl. dasselbe halt, da beide Bedd. sich 
auch bei andern Wzln. Yereint fin den. 

2. bha- „sprechen‘^ 

Ai. wahrscheinlich in sabha „Yersammlung“ (*,,Zssprechen“ ; bhd- im 
Ai. allerdings sonst — bis auf bhanati, s. u. — nur in der Bed. „scheinen, 
glanzen“; Edgerton KZ. 46, 173); arm. ban, gen. -/ „Wort, Kede, Yer- 
nunft, Urteil, Sache'^ (Hiibschmann Arm. Gr. I, 428; vgl. unten das no- 
Pras.), bay, gen. bayi ,,^Vort, Ausdruck^ = gr. gDarig; Bugge KZ, 

32,3 wo S. 13 anfechtbares weitere — , Hiibschmann aaO.);
```


## [2026-09-04T18:36:42.540Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9%D8%B1%D8%A8",
 "prompt": "Give the Arabic etymology section for عرب (ʿarab / ʿarab \"Arabs\") — the proposed origins (Semitic root ʿ-r-b, connections to \"west\", \"desert\", \"nomad\", Akkadian, Hebrew ʿărābāh), and whether any metathesis from ʿ-b-r \"to cross\" is mentioned. Also give the Persian section if present."
}
```


## [2026-09-04T18:36:43.031Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Hebrew",
 "prompt": "Give the full etymology of the English word 'Hebrew': Middle English, Old French, Latin, Greek, Aramaic, Hebrew forms, and the root ʿ-b-r 'to cross'."
}
```


### [2026-09-04T18:36:48.714Z] TOOL RESULT

```
# Etymology of عرب (ʿarab)

## Arabic Section

The webpage provides limited etymological detail for the Arabic entry. It references the **Semitic root ع ر ب (ʿ r b)** and notes there are "16 terms" belonging to this root, instructing readers to "Regard its root entry" for further information. However, the specific etymological connections you mentioned—such as links to "west," "desert," "nomad," Akkadian, Hebrew ʿărābāh, or potential metathesis from ʿ-b-r—are **not detailed** in this Wiktionary excerpt.

## Persian Section

The Persian entry is present but contains no etymological narrative. It simply indicates the word derives from Classical Persian عرب (arab), with pronunciation data and basic definitions (Arab/Arabian). No deeper etymological analysis appears in the Persian section provided.

**Summary:** The source material offers minimal etymological exposition beyond identifying the Semitic root; deeper historical connections would require consulting the referenced root entry not shown here.
```


### [2026-09-04T18:36:49.789Z] TOOL RESULT

```
# Etymology of "Hebrew"

The word "Hebrew" has a rich etymological journey through multiple languages:

**Middle English → Old French → Latin → Greek → Aramaic → Hebrew**

According to Wiktionary, the term derives from Middle English *Ebreu*, which came from Old French *Ebreu*. These ultimately trace back to Latin *hebraeus* or *hebraicus*, borrowed from Ancient Greek *Ἑβραῖος* (Hebraîos).

The Greek form itself was borrowed from Aramaic *עִבְרַי* (ʿiḇray), which came from Hebrew *עִבְרִי* (ʿiḇrī́).

The root *ʿ-b-r* fundamentally means "to cross," reflecting the ancient Semitic origins of the term used to describe the Hebrew people and their language.
```


## [2026-09-04T18:36:54.053Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Arab",
 "prompt": "Give the full etymology of 'Arab' — French, Latin, Greek, Arabic ʿarab, and the proposed Semitic root meaning ('nomad', 'desert', 'west'). Quote it."
}
```


## [2026-09-04T18:36:55.380Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9_%D8%B1_%D8%A8",
 "prompt": "Give the Arabic root ع ر ب entry: the meanings of the root and any etymological discussion (Proto-Semitic, connection to 'west', 'desert', 'to mix', or metathesis of ع ب ر)."
}
```


### [2026-09-04T18:36:58.159Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T18:36:59.111Z] TOOL RESULT

```
# Etymology of Arab

The word traces back through multiple language layers:

**Arabic → Greek → Latin → Old French → English**

According to the source, the term originates from Arabic *'arab*, described as the "indigenous name of the people, perhaps literally 'inhabitant of the desert'" and potentially connected to Hebrew *arabha* meaning "desert."

The path proceeds: Arabic *'arab* → Greek *Araps* → Latin *Arabs* → Old French *Arabi* → English *Arab* (attested from late 14c.).

The secondary meaning developed later: "The meaning 'homeless little wanderer, child of the street' is from 1848...an allusion to the nomadic ways of the Bedouin," reflecting the association with desert nomadism embedded in the original term.
```


## [2026-09-04T18:37:09.573Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9_%D8%B1_%D8%A8",
 "prompt": "Give the Arabic root ع ر ب entry: root meanings and any etymological discussion (Proto-Semitic, 'west', 'desert', 'to mix', metathesis of ع ب ر)."
}
```


### [2026-09-04T18:37:11.436Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T18:37:11.539Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9_%D8%A8_%D8%B1",
 "prompt": "Give the Arabic root ع ب ر entry: root meaning ('to cross'), Proto-Semitic reconstruction, related Hebrew/Aramaic/Akkadian forms, and derived terms such as عَبَرَ, عُبُور, عِبْرِيّ."
}
```


### [2026-09-04T18:37:13.456Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T18:37:17.081Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9%D8%A8%D8%B1",
 "prompt": "Give the Arabic entry for عبر: etymology of the root ʿ-b-r 'to cross', Proto-Semitic reconstruction, cognates (Hebrew עָבַר, Aramaic, Akkadian ebēru), and the Persian entry if present."
}
```


## [2026-09-04T18:37:18.765Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9%D8%A8%D9%88%D8%B1",
 "prompt": "Give the entries for عبور: Arabic (ʿubūr, verbal noun of عَبَرَ) and Persian (obur), with etymologies."
}
```


### [2026-09-04T18:37:23.089Z] TOOL RESULT

```
# Arabic Entry: عبر

## Etymology and Root

The root **ع ب ر** (ʕ-b-r) means "to cross." It is inherited from **Proto-Semitic *ʕabar-**.

## Cognates

Related words appear across Semitic languages:
- **Hebrew**: עָבַר (ʿāḇar, "to cross")
- **Old South Arabian**: 𐩲𐩨𐩧 (ʿbr, "to transgress")
- **Akkadian**: 𒁄 (ebēru, "to cross")

## Main Definitions

Under Etymology 1, the verb عَبَرَ (ʕabara) means: "to cross, to traverse, to ford, to swim (something), to pass over."

Under Etymology 2, a second sense appears as a transitive verb meaning "to interpret."

Etymology 4 describes عَبَّرَ (ʕabbara) as a causative form meaning "to express" or "to interpret," influenced by Middle Persian semantic patterns.

The preposition عَبْرَ (ʕabra) simply means "across."
```


### [2026-09-04T18:37:24.136Z] TOOL RESULT

```
# Entries for عبور

## Arabic
**عُبُور** (ʕubūr) is a masculine noun functioning as a verbal noun of عَبَرَ (ʕabara, "to cross"). The term carries multiple meanings: it serves as the verbal noun form, and denotes "crossing" or "passing." In contemporary usage, it also functions as a clipping for "عُبُور جِنْدَرِيّ" relating to gender transition.

**Etymology:** Derived as the verbal noun of the verb عَبَرَ.

## Persian
**عبور** (obur) is a noun borrowed directly from its Arabic counterpart. It carries the primary meaning of "crossing" or "passing," with a synonym listed as گذرش (gozareš).

**Etymology:** The Persian term was borrowed from Arabic عُبُور (ʕubūr), establishing a linguistic connection between the two languages through this semantic concept of crossing or transition.
```


## [2026-09-04T18:37:31.116Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"عبرانی\" \"عبری\" \"عبور\"; do echo \"=== $w ===\"; grep -n \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null | head -4; done; echo \"=== bazar in MON ===\"; grep -n \"بازار\" MON_part1.txt | head -3"
}
```


### [2026-09-04T18:37:32.616Z] TOOL RESULT

```
=== عبرانی ===
MON_part1.txt:6614:عبرانیان که سپس نام نبیسان گرفت 7 تقریاً 
MON_part1.txt:94758:عبرانی: 60۲ [ع.] (ص‌نس..) عبری» 
MON_part1.txt:94759:یهودی؟ ج. عبرانیون» عبرانیین. زبان یهود؛ 
=== عبری ===
MON_part2.txt:39654:لعل که نگین‌وار پهن باشد. لعل معبری: 
MON_part2.txt:74413:عالی‌مقام» از جمله این العبری رابولونیوس» 
MON_part1.txt:6024:عبری - آرامی است و اين امر با دلابل 
MON_part1.txt:6032:ندارند با عبری و آرامی در اینکه حروف 
=== عبور ===
MON_part2.txt:4931:بعد از عبور از منازل نفس چنانکه فرمود 
MON_part2.txt:9212:عبور کند. 
MON_part2.txt:12534:قسمت قرنیه به خوبی عبور می‌کند. قرنیه 
MON_part2.txt:13736:سبب بسیار شدن آب چنانکه عبور از آن 
=== bazar in MON ===
2876:خواهد آزارید» بازار» آزارنده» آزاریده) 
10133:0 عددها. در تداول بازاربان مجموع 
19581:بات مسحلی بودن: در آزیجا بازار رواج و
```


## [2026-09-04T18:37:35.298Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '94750,94775p' MON_part1.txt; echo \"=== search عبری headword ===\"; grep -n \"^عبری\\|عبری:\" MON_part1.txt | head -5"
}
```


### [2026-09-04T18:37:35.375Z] TOOL RESULT

```
گذشتن. در گذشتن» مردن. (مص‌م.) جاری 


کردن اشکد. 
عبر: 201 [ع.] (مص م.) تعبیر کردن خوات و 
ما لکار. 


عبرانی: 60۲ [ع.] (ص‌نس..) عبری» 
یهودی؟ ج. عبرانیون» عبرانیین. زبان یهود؛ 
۱ 

عبرت: احاء [غ. عبرة] (مصل.) بند 
گرفتن. (مص‌م.) مقیاس گرفتن» سنجیدن. 
() نسوع» قسم. بند. محصولاتی که از 
کشتی‌نشینان» چادرنشینان یابه جهت 
راهداری میگرفتند. خراج» باج. (ص.) 
آنچه که مورد عبرت گرفتن شود؛ موجب 
عبرت. شگفت. عبرت شش روزه: (کن.) 
آسمان و زمین و آنچه در میان انها است از 
مخلوقات. (کذ.) آنچه که از ما به فعل آورده 
شود. عبرت دیگران گُردانیدن: کسی را 
سخت تنبیه کردن تا دیگران پند گپرند. 
موجب عبرت شدن: به سبب مصایب و 
بدبخت‌هایی که نتیجه اعمال شخص است» 
موجب پند گرفتن دیگران شدن. 
=== search عبری headword ===
6024:عبری - آرامی است و اين امر با دلابل 
35528:سیاه باران بار. پیل معبری: پیل بزرگك که بر
```


## [2026-09-04T18:37:41.228Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=94700 && NR<=95100' MON_part1.txt | grep -n \"عبری\\|عبور\" | head -20"
}
```


### [2026-09-04T18:37:42.822Z] TOOL RESULT

```
59:عبرانی: 60۲ [ع.] (ص‌نس..) عبری» 
80:عبر ه. (0-)۵0۲-2 [ع. عبرة] (مص‌ل.) عبور 
81:کردن» عبر. (امص.) عبور. 
114:عبور: 00۲ [ع.] (مص‌ل.) گذشتن» عسور 
115:کردن (از نهر» وادی و غیره). عبور و مرور:
```


## [2026-09-04T18:37:53.236Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ ===\"; grep -n -i \"ibri\\|Hebrew.*'abar\\|'abara\" FVQ.txt | head -8; echo \"=== AFA ===\"; grep -n -i \"'ibri\\|ibrani\\|Hebräer\" AFA.txt | head -8; echo \"=== LKT Araber ===\"; grep -n -i \"Ar\\. 'arab\\|Araber\\|Hebraer\\|Hebräer\" LKT.txt | head -8; echo \"=== AKD eberu ===\"; grep -n -i \"eberu\\|ebêru\" AKD.txt | head -5"
}
```


### [2026-09-04T18:37:53.337Z] TOOL RESULT

```
=== FVQ ===
15469:ftLj^^j (Kibriya). 
=== AFA ===
676:und Hebräer bereits zu festen Ansiedelungen gelangt waren ,
1467:es, wie die Hebräer, natürlich von den Persern empfangen.
=== LKT Araber ===
96:Huart  GA  =  Gl.  Huart.  Geschichte  der  Araber.  Autorisierte  Übersetzung  von Sebastian  Beck  und  Montz  Färber.    Leipzig.   Bd.  L  1914:  11.  1915.
97:IB  =  Die  Reisen  des  Arabers  Ibn  Batata  durch  Indien  und  China  (14.  Jahrhun- dert). Bearbeitet  von  Hans  von  Mzik.  (Bibliothek  denkwürdiger  Reisen,  heraus- gegeben von  Ernst  Srhultze.  5.  Bd.)  Hamburg  191 1.  —  (Verweisungen  auf  den arabischen  Urtext  des  Ibn  BattOta  beziehen  sich  auf  Voyages  d'Ibn  Batoutah, texte  arabe.  arcompasrne  d'une  traduction  par  C.  Defremery  et  H.  B.  San- guinetli.    4  Buo.    Paris  1853/59.)
246:In  der  Zusammensetzung  as-sirä  al- "abiir  'der  [sc.  auf  der  Milchstraße] wandernde  Sirius'  [hierzu  s.  hier  Nr.  1915] vom  ar.  Stamme  'fcr  'wandern'  [vgl. hebr.  "ibrl  'Hebräer',  d.  h.  derjenige,  der gewandert  ist  od.  überschritten  hat  sc. den  Euphrat  od.  Jordan].  Hieraus  Alha- bor,  Alchabar  als  Name  des  Sirius  a Ganis  majoris.  [Devic  DEt  40/41. Ideler  Sternn  237  und  246.
282:Einheitsnomen  "agamt  'Barbar,  Fremder, Nichtaraber',  besonders  'Perser'.  Tk. agemi;  hieraus  rum.  agemiu,  ageamiü 'unbewandert,  Anfänger';  poln.  (alt)  ad- ziamski  'persisch'  in  Verbindung  mit Substantiven  wie  'Teppich,  Kostüm, Sattel'.  —  Altit.  agemina,  mittelfrz.  aze- mine  'Ziselierarbeit'.  Das  sp.  aljamia, lengua  aljamiada,  bezeichnet  die  Sprache der  Moriscos,  zu  deren  Eigentümlich- keiten es  gehörte,  daß  in  ihr  viele arabische  Ausdrücke,  z.  T.  mit  spanischer Endung,  sowie  Arabismen  und  alt- spanische Wörter  vorkommen,  die  sonst schon  außer  Gebrauch  gekommen  waren. Da  diese  Sprache  mit  arabischer  Schrift geschrieben  wurde,  sind  textos  aljamia- dos  also  spanische  Schriftstücke,  die arabisch  geschrieben  sind,  z.  B.  das Poema  de  Yosuf,  vgl.  Ad.  Zauner,  Alt- spanisches Elementarbuch. ^  Heidel- berg 1921.  S.  155.  [DE  145.  ML  298. ZromPh  XXXIl,  41.  XXXIII,  62.  Kar- lovvicz  435.
294:'Kiide';  ähir  an-nahr  'das  Ende  des Flusses'  ist  bei  den  Arabern  ein  glän- zender Stern  am  äußersten  Ende  des Sternbildes  Eridanus,  das  ar.  an-nahr 'dei-  Fluß'  wie  schon  bei  Ptoleniaeus "EaxuToq  toö  irotaiaoö  heißt.  Aus  dem Ar.  wurde  der  heutige  Name  Acarnar, Acheriiar ,  frz.  achet-nar,  akharnar,  'a Eridani'.  |  Devic  DEt  4.  Lammens Rem  3/4.    Ideler  Sternn  232/3.
423:Npr.  'die  Araber',  a)  Schon  im  Ar.  und besonders  im  Tk.  nahm  das  Wort  die Bedeutung  'Neger'  an,  daher  rum.  arab, araj),  harap  'Araber,  Neger';  russ.  arap, bulg.  serb.  arapin,  bulg.  arap  'Neger'. —  b)  In  den  romanischen  Sprachen wurde  das  AVort  zur  Bezeichnung  einer sittlichen  Minderwertigkeit  benutzt:  frz. arabe  'Wucherer,  Beutelschneider',  dial. 'habsüchtig,  geizig',  prov.  arabe  'hab- gierig, geizig',  alabre  'gefräßig'.  Die ar.  Adjektivform  'arabl  'arabisch'  liegt vor  in  sp.  alarbe  'roher,  ungebildeter Mensch'  [mit  ar.  Art.],  pg.  alarre  'dass.', kat.  alarb  'd:iss.'.  —  c)  Bezeichnung des  arabischen  Pferdes  im  engl,  angloind. arah  [für  an  Arab  horse],  dtsch.  Araber, so  schon  bei  Marco  Polo:  de  bons  des- triers  arrabins.  Weitere  Belege  bei Hobson-Jobson  33/34.  —  d)  Mit  roma- nischer Endung  -iscus  wird  it.  arabeseo, rabesco  'Schnörkelzeichnung  nach  arab. Weise',  frz.  arabcsque,  rum.  aräpesc, dtsch.  Arabeske  usw.  —  e)  Zur  Bezeich-
449:Namen  des  Sommersitzes  der  granadi- nisclien  Könige  in  Granada,  dem  Gene- ralife [s.  Baedeker,  Spanien  und  Portu- RalA  Leipzig  1912.  S.  350;  v.  Schack, Poesie  und  Kunst  der  Araber  in  Spanien und  Sicilien.2.  Stuttgart  1877.  II,  328 bis  333;  Kurt  Hielscher,  Das  unbekannte Spanien.  Berlin  s.  a.  (1922).  S.  17/22], früher  Ginalarife,  d.  h.  gannai  aVarlf 'Garten  des  Baumeisters'.    [DE  57.
732:2'i7.  Ar.  barbäris: [Entstanden  aus  nnnr  hüris  über  ambar bäris,  vgl.  FLEISCHER  in  BSGW  phil. bist.  Kl.  1881,  XXXill,  9]  'eine  Pflanze Berberis  vulgaris',  deren  Beeren  zu  Mar- mel.ide,  Sirup  oder  Eis  verarbeitet  wer- den; die  Apotheker  benutzen  ihre  Wur- zalrinde;  zuerst  wurde  die  Pflanze  von den  Arabern  verwertet.  Frz.  berberis, engl,  barberry  [aber  berberine  'die  dar- aus gewonnene  Substanz  zum  Gelb- färben'], dtsch.  Berberize,  Berberstaude, Berberisbeere.  Russ.  barbaris  'Sauer- dorn'.
=== AKD eberu ===
```


## [2026-09-04T18:38:05.989Z] TOOL CALL #54: WebSearch

```json
{
 "query": "etymology of \"Arab\" Semitic root ʿ-r-b metathesis of ʿ-b-r \"to cross\" scholarly"
}
```


### [2026-09-04T18:38:07.752Z] TOOL RESULT

```
Web search results for query: "etymology of "Arab" Semitic root ʿ-r-b metathesis of ʿ-b-r "to cross" scholarly"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T18:38:13.242Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Arabs",
 "prompt": "Quote the Etymology section: the proposed origins of the word \"Arab\" (Semitic root ʿ-r-b, 'west', 'nomad', 'desert', Akkadian, connection or metathesis with ʿ-b-r 'to cross' / Hebrew ʿibri), and which explanations scholars favour."
}
```


## [2026-09-04T18:38:13.528Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Arab",
 "prompt": "Give the English etymology of 'Arab' (Middle English, Old French, Latin, Greek, Arabic) verbatim."
}
```


### [2026-09-04T18:38:18.745Z] TOOL RESULT

```
# Etymology of 'Arab'

Based on the Wiktionary article provided, the English etymology is:

"Borrowed from Arabic عَرَب (ʕarab, 'Arabs') or back-formation from Arabic."

The article does not trace the word through Middle English, Old French, Latin, or Greek stages. It indicates the English term derives directly from Arabic, either as a borrowing or as a back-formation from the English word "Arabic."
```


### [2026-09-04T18:38:20.460Z] TOOL RESULT

```
# Etymology of "Arab": Proposed Origins

The Wikipedia article presents several theories about the Semitic root **ʿ-r-b** and its meanings:

## Primary Root Meanings

The root carries multiple related senses: **"'west, sunset', 'desert', 'mingle', 'mixed', 'merchant' and 'raven'"** according to scholars examining Semitic languages.

## Alternative Metathetical Origin

One hypothesis suggests the term derives from a different root through linguistic transformation: **"ʿ-B-R, 'moving around' (Arabic: ʿ-B-R, 'traverse') and hence...it is alleged, 'nomadic.'"** This theory connects nomadic lifestyles to the word's etymology.

## Hebrew Etymology

The article notes a desert-based origin in Hebrew tradition, where **"Arab...comes from the desert origin of the Bedouins whom it originally described as arava..., meaning 'desert' or 'wilderness.'"**

## Scholar Consensus

Rather than unanimously favoring one explanation, the article indicates these various meanings are **"'comprehensible' with all of these having varying degrees of relevance"** to how the name emerged, suggesting scholars recognize multiple plausible etymological pathways rather than establishing definitive scholarly consensus on a single origin.
```


## [2026-09-04T18:38:38.342Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON bazar headword ===\"; grep -n \"بازار:\" MON_part1.txt | head -5; echo \"=== TTS pazar variants ===\"; grep -n -i \"bâzâr\\|bazâr\\|Markt\" incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -8; echo \"=== FSD bazaar ===\"; grep -n -i \"bazaar\" FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt | head -5; echo \"=== WEB bazaar entry ===\"; grep -n -i \"Pers. bazar\\|bazar\\]\" WEB_vol1.txt | head -5"
}
```


### [2026-09-04T18:38:38.491Z] TOOL RESULT

```
=== MON bazar headword ===
20350:بازار: :معا (.) محل خرید و فروش کالا 
28697:بازار: فالوذج السوق. آنچه خوش ظاهر و بد 
68965:روز بازار: روزی که مردم در جایی جمع 
=== TTS pazar variants ===
=== FSD bazaar ===
FSD_vol4.txt:54701:varies  locaUy  from  280  lb  to  400  lb  Used  on  the  North Sea  Baltic  etc  2“shoo?.  *“  Factory  weight  At  bazaars - 179  64  gr  tola?  5   ***  At  Mangalore  Shlplast?
FSD_vol4.txt:109662:1912*  Great  bazaar  quarters  In  Damascus  100b*  William  Buck  Dwight,  American  ge-  1907*  John  Joseph  Williams,  archblshon  of destroyed  by  Art,  losses  sio  000,000  ologlst  and  educator,  died  Boston,  Mass  ,   died.
FSD_vol1.txt:41137:Be'zer,  1   brzar;  2   bfi'zer,  n.  Bib.  Deut.  iv,  43. bez'es-tecn,  l   bez'es-tln;  2   b?z'Ss-t£n,  n.  An  Oriental  mar- ket-place; bazaar.  [<  Turk,  harlrtdn  (<  Per.),  clothes- market.]  bez'es-tant;  bez’es-telnj.
FSD_vol1.txt:48701:[F.,  <   W.  bran,  husk.]  —   bran  bread,  bread  made  of  un- bolted flour.— bran'*dust"er,  tj.  A   machine  for  remov- ing the  flour  that  remains  In  bran  after  bolting.— b.  pie, a   box  or  tub  filled  with  bran  in  which  email  packages are  hidden  to  be  drawn  out  at  random,  sometimes  at  a trifling  charge;  used  at  church  bazaars  and  children’s parties.
FSD_vol1.txt:84529:<   L.  curlosita(t-)s,  <   curiosus;  see  curious.]  cu"rI-os'i- teef;  cu"rl-os'I-tlet* —   cu"rI-os'I-ty*shop",  n.  A   bazaar, store,  or  place  where  curiosities  are  collected  for  sale. cu"rI-o'so,  1   kiG'ri-O'so  or  (It.)  kfi’rl-6'so;  2   cG'ri-6'so  or  (It.) cu'ri-6'so,  n.  [-si,  1   -si;  2   -si,  pi.]  [It.]  A   connoisseur  or collector  of  curios;  one  interested  in  art;  a   virtuoso, cu'rl-ous,  1   kiu'n-tis;  2   cu'ri-Ss,  a.  1.  Eager  for  in- formation or  knowledge;  desirous  to  see  or  know;  in- clined to  scrutiny,  or  research;  sometimes,  in  a   bad sense,  inquisitive;  prying  into  the  affairs  of  others.  2.
=== WEB bazaar entry ===
```


## [2026-09-04T18:38:43.796Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"ba-zaar\\|bazar'\\|Per\\. bazar\\|Pers\\. bazar\\|bazar,\\|bazar\\]\" FSD_vol1.txt WEB_vol1.txt | head -10; echo \"=== MON bazar entry ===\"; sed -n '20345,20370p' MON_part1.txt"
}
```


### [2026-09-04T18:38:43.904Z] TOOL RESULT

```
WEB_vol1.txt:16947:ba-ziiar’, ba-zir’, n. [Per. bazar, a market.]
FSD_vol1.txt:37535:ba-zaar',  11  ba-zar';  2   bn-zar',  n.  1.  An  Oriental ba-zar',  J   market-place  or  range  of  shops,  often  includ- ing a   street  or  series  of  streets,  sometimes  under  a   com- mon roof;  in  southern  India  and  Ceylon,  a   single  shop or  stall  kept  by  a   native.
FSD_vol1.txt:37540:2.  A   fancy  fair  for  charity.  3.  A   large  fancy-store  or shop.  [   <   F.  bazar ,   <   Per.  bazar,  market.]
=== MON bazar entry ===
جای خویش شد. ضح. این کلمه بدین معنی 


لازم الاضافه است. 

بازار: :معا (.) محل خرید و فروش کالا 
و خوراک. کوچه سرپوشیده که از دو سوی 
دارای دکان‌ها باشد: بازارگاه. بازار خاک: 
(کد.) قالب آدمی. عظمت شربت. رونق 
امور دنبوی. 

بازاری: ۰2271 (ص‌نسب.) منسوب به 
بازار» مردم بازار» اهل بازاره سوقه. (هنر.) 
مبتذل» اثری که در آن رعایت اصول نشده 
و خالی از حس و حساب باشد. اثری که 
فقط به منظور انتفاع ساخته شده باشد. 
بگٌازالت: (.) (زم.) یکسی از 
سنگک‌های آذرین که دارای سختی نسبة زباد 
و سیا‌رنگ و لب بریدگی‌هایش کند است. 
این سنگ در دستگاه شش وجهی متلور 
می‌شو د. 

بازبین: ۰22-70 (انا.) آنکه بلیت‌های 
ورودی را بازدید کند. 

باز پرس: 22-5 (افا. امر.) کسی که
```


## [2026-09-04T18:38:56.702Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%9Ebra%E1%BF%96os",
 "prompt": "Ancient Greek Ἑβραῖος: etymology (Aramaic source), meaning, first attestations (Septuagint, Josephus)."
}
```


## [2026-09-04T18:38:58.329Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Hebrew",
 "prompt": "Full etymology chain for 'Hebrew': Old French, Latin, Greek, Aramaic, Hebrew ʿibhri, and the 'one from across the river' explanation, with dates."
}
```


### [2026-09-04T18:38:58.786Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T18:39:04.847Z] TOOL RESULT

```
# Etymology of Hebrew

The word "Hebrew" has an interesting linguistic journey. According to etymonline, the term comes from "Old French _Ebreu_, from Latin _Hebraeus_, from Greek _Hebraios_, from Aramaic (Semitic) _'ebhrai_."

The ultimate origin likely refers to geographical or social status rather than a proper name. The source indicates the word probably means **"one from the other side,"** possibly alluding to the River Euphrates or simply denoting an immigrant. This derives from the Hebrew root _'ebher_, meaning "region on the other or opposite side."

## Historical Usage

The English adjective appears in late Old English texts, while the noun form emerged around 1200 to describe the Hebrew language specifically. By the late 14th century, it was used to refer to people, particularly biblical Israelites. Notably, the initial H- was restored in English starting in the 16th century.

The etymology reflects how the word traveled westward through multiple languages before settling into English, with its meaning shifting from a descriptive geographic or social designation to an ethnic and linguistic identifier.
```


## [2026-09-04T18:39:07.363Z] AGENT

Now let me archive all the web sources.


## [2026-09-04T18:39:13.061Z] TOOL CALL #61: Bash

```json
{
 "command": "for u in \\\n\"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1|page 34 entry 0 root Aba/Sabha: Persian bazar etymology (MP wazar < OIr *waha-carana)\" \\\n\"https://en.wiktionary.org/wiki/w%CA%BE%C4%8D%CA%BEl|page 34 entry 0 node 2: Middle Persian wazar etymology and descendants\" \\\n\"https://www.etymonline.com/word/bazaar|page 34 entry 0 nodes 3-7: bazaar chain Persian>Turkish>Italian>English and Old Iranian *vaha-carana\" \\\n\"https://www.ahdictionary.com/word/search.html?q=bazaar|page 34 entry 0 node 7: AHD etymology of English bazaar (Nourai cites AHD)\" \\\n; do url=\"${u%%|*}\"; note=\"${u##*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\"; done 2>&1 | tail -20"
}
```


### [2026-09-04T18:39:16.072Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1354a0009a99a521.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1cdb183a78f5b229.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/577a680138a66ff6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/41cdb778a5af7678.txt
```


## [2026-09-04T18:39:24.339Z] TOOL CALL #62: Bash

```json
{
 "command": "for u in \\\n\"https://en.wiktionary.org/wiki/%D8%B9%D8%A8%D8%B1|page 34 entry 1 root: Arabic root 3-b-r 'to cross', Proto-Semitic *3abar-, cognates Hebrew/Akkadian\" \\\n\"https://en.wiktionary.org/wiki/%D8%B9%D8%A8%D9%88%D8%B1|page 34 entry 1 node 2: Persian obur borrowed from Arabic 3ubur\" \\\n\"https://en.wiktionary.org/wiki/%D8%B9%D8%B1%D8%A8|page 34 entry 1 nodes 4-5: Arabic 3arab and Persian 3arab\" \\\n\"https://en.wikipedia.org/wiki/Arabs|page 34 entry 1 node 3: competing etymologies of 'Arab', including the alleged 3-b-r metathesis\" \\\n\"https://www.etymonline.com/word/Arab|page 34 entry 1 nodes 6-8: Arab via Greek Araps, Latin Arabs, Old French\" \\\n\"https://en.wiktionary.org/wiki/Arab|page 34 entry 1 node 8: English Arab\" \\\n\"https://en.wiktionary.org/wiki/Hebrew|page 34 entry 1 nodes 9-15: English Hebrew chain Hebrew>Aramaic>Greek>Latin>OF>ME\" \\\n\"https://www.etymonline.com/word/Hebrew|page 34 entry 1 nodes 13-15: Hebrew chain and 'one from the other side'\" \\\n; do url=\"${u%%|*}\"; note=\"${u##*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\"; done 2>&1 | tail -20"
}
```


### [2026-09-04T18:39:29.848Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4d743e6a7fa1563f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f3fbdfd9287a1e9c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a03deed3900bf954.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9b732b617eee8b4b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/afed5bde12632208.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ab8a330620110f72.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c0a5c5d4fb32120b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/154563583777f39c.txt
```


## [2026-09-04T18:39:37.279Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HJB bazaar ===\"; grep -n -i \"BAZAR, s\\.\\|BAZAAR\" HJB.txt | head -5; echo \"=== TTS broad ===\"; grep -c \"\" incoming/TTS/TTS_vambery1878_uoft_djvu.txt; grep -n -io \"bazar[a-z]*\\|pazar[a-z]*\" incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head; echo \"=== MON عرب ===\"; grep -n \"عرب:\" MON_part1.txt MON_part2.txt | head -3; echo \"=== AID ===\"; grep -n -i \"bazar\" AID.txt | head -3"
}
```


### [2026-09-04T18:39:37.391Z] TOOL RESULT

```
=== HJB bazaar ===
144:The  trade  and  conquests  of  the  Arabs  both  brought  foreign  words  to India  and  picked  up  and  carried  westward,  in  form  more  or  less  corrupted, words  of  Indian  origin,  some  of  which  have  in  one  way  or  other  become  part of  the  heritage  of  all  succeeding  foreigners  in  the  East.  Among  terms  which are  familiar  items  in  the  Anglo-Indian  colloquial,  but  which  had,  in  some shape  or  other,  found  their  way  at  an  early  date  into  use  on  the  shores  of the  Mediterranean,  we  may  instance  bazaar,  cazee,  hummaul,  brinjaul,  gingely, mjffUnoer,  grab,  maramut,  devxiun  (dogana,  douane,  &c.).  Of  others  which  are found  in  medieval  literature,  either  West- Asiatic  or  European,  and  which still  have  a  place  in  Anglo-Indian  or  English  vocabulary,  we  may  mention amher-gnB,  chank,  junk,  jogy,  Jcincob,  kedgeree,  fana/m,  calay,  bankshall,  mudiliar, tindal,  cranny.
3157:BAZAAR.
5929:1686.—".  .  .  And  that  if  the  Chetty Bazaar  people  do  not  immediately  open their  shops,  and  sell  their  min,  etc.,  as usually,  &at  the  j^ooda  ancT  commodities in  their  several  ships  be  confiscated." — In Wheeler,  i.  152.
7599:CX)88IMBA2^AB,  n.p.  Properly Kdmmbdzdr,  A  town  no  longer  existing, which  closely  adjoined  the  city  of Munhidabad,  but  preceded  the  latter. It  was  the  site  of  one  of  the  most  im- portant factories  of  the  East  India Company  in  their  mercantile  days,  and was  indeed  a  chief  centre  of  all  foreign trade  in  Bengal  during  the  17  th  cen- tury. ["  In  1668  the  Company  estab- lished a  factory  at  Cossimbazaar, *  Castle  Basaar.'''— <^tn2i£woc2  Rep,  on Old  Bee,  219.)]  Fryer  (1673)  calls  it Oastle  Bazzar  (p.  is),
8112:giiis  name  is  said  to  signify  '^Custom- ouse" ;  [mandufiy  'a  temporary  hut,* is  a  term  commonly  app]|^ed  to  a bazaar  in  N.  India].
=== TTS broad ===
14642
=== MON عرب ===
MON_part2.txt:4161:فوارس. فارس عرب: آنکه الفاظ عرس را د 
MON_part2.txt:49491:م.‌های دوازده گکانة قمری عرب: 
MON_part2.txt:56156:مسستعرب: ۱۱10۹۲۲۵ [ع.] (افا.) (ف.) 
=== AID ===
```


## [2026-09-04T18:39:40.006Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3150,3175p' HJB.txt"
}
```


### [2026-09-04T18:39:40.055Z] TOOL RESULT

```
H.  bepdrif  and  byopdri  (from  Skt. vifdpdrtn) ;  a  trader,  and  especially  a petty  trader  or  dealer.
A  friend  long  engaged  in  business in  Calcutta  (Mr  J.  T.  O^vy,  of Qillanders  &  Co.)  communicates  a letter  from  an  intelligent  Bengalee gentleman,  illustrating  tbe  course  of trade  in  country  produce  before  it reaches  the  hands  of  the  EurQpean shipper :
1878.—"  .  .  .  the  enhanced  rates  .  .  . do  not  practicalljr  benefit  the  producer  in a  markea,  or  even  in  a  corresponding  degree ; for  the  lion's  share  goes  into  the  pockets of  certain  intermediate  classes,  who  are  the growth  of  the  aboTe  system  of  business.
"  Following  the  course  of  trade  as  it  flows into  Oalcutto,  we  find  that  between  the cultiTators  and  the  exporter  these  are :  1st. The  Bappanee,  or  petty  trader ;  2nd.  The AunU-dar;*  and  8rd.  The  Mahajim,  in- terested in  the  Calcutta  trade.  As  soon  as the  orope  are  cut^  BeplMiZTee  appears  upon the  scene;  he  Tisits  Tillage  after  Tillajge, and  goes  from  homestead  to  homestead, buying  there,  or  at  the  Tillage  marts,  from the  lyots;  he  then  takes  his  purchases  to the  Aurut-doTi  who  is  stationed  at  a  centre of  trade,  and  to  whom  he  is  petiiaps  under adTanoes,  and  from  the  AunU-dar  the Calcutta  Mahajun  obtains  his  supplies  .  .  . for  CTcntual  despatch  to  the  capital.  There is  also  a  fourth  class  of  dealers  called Pkoreatf  who  buy  from  the  Mahajun  and sell  to  the  European  exporter,  llius,  be- tween the  cultiTator  and  the  shipper  there are  so  many  middlemen,  whose  participation in  the  tnule  iuToWes  a   multiplication   of
Erofits,  which  goes  a  great  way  towards  en- ancing  the  price  of  commodities  before they  reach  the  shipper's  hands." — Letter from  Baboo  Nohohiunn  Gho&e,  [Similar  de- tails for  Northern  India  will  be  found  in Hoevy  Mom,  Trade  and  Mawv^aetxre»  of lAwhwWy  59  Kqq.'\
HA^AAH,  s.  H.  &c.  From  P.  hdzchr, apermanent  market  or  street  of  shops. Tne  word  has  spread  westward  into
*  Auruldar  is  drhat-dOr^  from  U.  drhaL, '  agency ' ;  phorea^B..  phariydf  *  a  retailer.'
BAZAAR.
76
BEADALA.
Arabic,  Turkish,  and,  in  special  senses, into  European  languages,  and  eastward into  India,  where  it  has  generally  been adopted  into  the  vernaculars.  The popular  pronunciation  is  bdzdr.  In S.  India  and  Ceylon  the  word  is  used for  a  single  shop  or  stall  kept  by  a native.  The  word  seems  to  have  come to  S.  Euroj)e  very  early.  F.  Balducci Pegolotti,  in  his  Mercantile  Hand- book (c.  1340)  gives  Bazaiia  as  a Genoese  word  for  'market-place' {Cathay,  &c.  ii.  286).  The  word  is adopted  into  Malay  as  pdsOr,  [or  in the  poems  patara],
1474. — Ambrose  Contarini  writes  of  EaBan, that  it  is  *'  walled  like  Como,  and  with  ba- zars {bazzari)  like  it."— iSamtmo,  ii.  f.  117.
1478.— Joeafat  Barbaro  writes:  "An  Ar- menian Choza  Mirech,  a  rich  merchant  in the  baiar"  {bazarro),—/^.  f.  111*.
1563. — '*.  .  .  baiar,  as  muoh  as  to  say the  place  where  things  are  sold." — Oareia,
f.  im
1.564.— A  privilege  by  Don  Sebastian  of Portugal  gives  authority  *'  to  sell  garden  pro- duce freely  in  the  baiars  (bazara),  markets, and  streets  (of  Goa)  without  necessity  for consent  or  license  from  the  farmers  of  the garden  produce,  or  from  any  other  person whatsoever."- XrcA.  Part,  Or,,  fasc.  2,  157.
c.  1566.— "La  Pescaria  delle  Perle  .  .  . si  fa  ogn'  anno  .  .  .  e  su  la  costa  all'  in contro  piantano  vna  villa  di  case,  e  basaxri di  pagha." — Cetare  de*  Federictf  in  Ramutio, iii.  3^.
1606.—".  .  .  the  Christians  of  the Banr."— ti'outwa,  29.
1610.— "En  la  Yille  de  Cananor  il  y  a  vn beau  march^  tons  les  jours,  qu'ils  appellent Basare."- Pvmn;  de  Laval,  i.  825 ;  [Hak. Soc.  i.  448].
[1615. — "To  buy  pepper  as  cheap  as  we could  in  the  tnuser.  — Foster,  Letters, iii.  114.]
[  „  "He  forbad  all  the  bear  to  sell  us victuals  or  else.  .  ."—Ibid.  iv.  80.]
[1623.— "They  caU  it  Beiail  Kelan,  that is  the  Great  Merkat.  .  ."—P.  della  ValU, Hak.  Soc.  i.  96.  (P.  KalOn,  'great').]
1638.— "We  came  into  a  Bonar,  or  very faire  Market  place."— fT.  BruUm,  in  Hakl. v.  50.
1666. — "Les  Baiarda  ou  March^  sont dans  une  grande  rue  qui  est  au  pi^  de  la montagne.  — Thevetiot,  v.  18.
1672.—".  .  .  Let  us  now  naas  the  Pale to  the  Heathen  Town  (of  Madras)  only parted  by  a  wide  Parrade,  which  is  used  for a  Bniar  or  Mercate-plaoe.  "—^ryer,  38.
[1826.—"  The  Kotwall  went  to  the  banar- muitn.**—Pandttrang  Eari,  ed.  1878,  p. 156.]
```


## [2026-09-04T18:41:04.217Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON arab ===\"; grep -n \"عرب» \\|عرب:\\|أعرابی\\|اعرابی\" MON_part1.txt MON_part2.txt | head -5; echo \"=== SKT Hebrew/Arab ===\"; grep -n -i \"^Hebrew\\|Hebrew,\\|Arab,\" SKT.txt | head -5; echo \"=== RCH ===\"; grep -n -i \"bazar\\|bāzār\" RCH.txt | head -3; echo \"=== NYB wazar2 ===\"; grep -n -i \"market\" NYB_vol2_glossary.txt | head -5"
}
```


### [2026-09-04T18:41:04.346Z] TOOL RESULT

```
=== MON arab ===
MON_part2.txt:1005:آماس بگشاید نا آن را «غعرب» 
MON_part2.txt:4161:فوارس. فارس عرب: آنکه الفاظ عرس را د 
MON_part2.txt:46042:بگردانیدن اعرابی معنی بگردد (جامع 
MON_part2.txt:49491:م.‌های دوازده گکانة قمری عرب: 
MON_part2.txt:56156:مسستعرب: ۱۱10۹۲۲۵ [ع.] (افا.) (ف.) 
=== SKT Hebrew/Arab ===
373:Admiral.  (F.-Arab.)  M.E. more  often  amiraLm^O.  F.  amiral, also  amirt\  cf.  Low  L.  admu prince,  chief.* Arab,  amlr^  a  pri Elmir.  The  suffix  is  due  to  Arab.] amir-ai-baJir,  pnncc  of  ihc  sea.
519:Alchemy.  (F.-Arab.- Gk.)  O.F.  a/- chemit.  dtyiu/Nii.  ^  Arab,  a/,  the;  and I'imyA,  alchemy,  — Late  Gk.  xv/"'**.  chemis- try; for  xf^^'o.  «  mingling.  — Gk.  xiuv^  to pour  out,  mix.  (^GKU.)
520:chomiBt,  Christ.  (Ck.)  Shortened form*  of  akhtnttsff  (xlckymist,  formed  by dropping  the  Arab,  article  al,
521:AJcohoL  (F.  — Arab.)  F.  akoot,  furmerlv also  alcohal^  applied  to  pure  •spirit,  though the  orig.  »en»e  was  a  fine  impalpable  pow- der. *  Arab,  at,  the;  and  kahiil,  kokl^  or ktAl^  a  coUyrium,  very  fine  powder  of  anti- mony, nsctl  to  paint  the  cycbtows  with.
523:Alcove,  a  recess.  (F.-Ilal.  — Arab.)  F. a/r<Tcr.  — Ital.  aUot'o,  the  same  a<>  Span. aUo&a,  a  recess  in  a  room.  — Arab,  a/,  the; and  qubhah,  qobbah,  a  vault  arcii,  dome^ cupola ;  hence  a  vaulted  space.
=== RCH ===
1762:of  liquors  and  other  articles  in  bazars  attached  to  the  garrisons.
14761:F   ;::.^'tjb  bdz^ddshty  Hindering,  preventing,  keeping  back, p   ^;^jb  bazargduy  A   merchant,  a   trader, p   bdzarganj  kardatiy  To  trade,  to  buy  and  sell.
14767:baz-kuskSy  Discriminating,  distinguishing. kSzgSn  (for  bazargan),  A   merchant.
=== NYB wazar2 ===
631:*Arhest [’Ihyst] the name of a town 117°. — Probably = Arm. Arest, a village and market-place on the shore of Lake Van where the Great King had fisheries, v. P*aust. Buz. Patm. p. 35, 181.
3320:2ristak [lystk', Istk'] 1. custom, rule, law: v. yuvat-ristak. — 2. adj. firm, reliable, truthful 1101’; sup. ~-tom 59", cf ristake- nitan. — From Av. rād-, v. s. v. patrāstak and ef rdyénitan; MPrth pt. ryst ‘exact, correct’, Ghilain 60; Paz. subst. (SGV) rastaa ‘law, element’ (= Gr ototxetov, thus de Menasce); NP rast ‘firm, steady’, rastah ‘rule, institute, market’; Talm lw. rystq? ‘market-place’, Telegdi 255.
3353:rötastäk [lwtst’k], rostak [lwst’k] district, province 377. 8618. — In FrP 2 it is the first subdivision under šahr ‘dominion, kingdom’, and placed above déh ‘village’ and zänak ‘house’, cf Nyberg, Byzantion XXXVILI, 1968, 114-115. — MPrth rwdyst’g (A-H III); Paz. röstä, pl. rostčiga ; NP rēstā(i) ‘any inhabited place; a market-town, a village’; Arab. lw. rustäg, ruzdäg ‘arable land’.
```


## [2026-09-04T18:48:03.388Z] TOOL CALL #66: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build34.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nETY = \"https://www.etymonline.com/word/\"\n\ndoc = {\n \"pdf_page\": 34,\n \"book_page\": 4,\n \"verified_by\": \"claude-fable-5-1\",\n \"verified_on\": \"2026-09-04\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Abâ, Sabha\",\n   \"verdict\": \"disputed\",\n   \"modern_form\": \"NP bāzār < MP wāzār (Book Pahlavi wʾCʾl) < Old Iranian *wahā-čaraņa- 'place of sale, trade-traffic' (PIE *wes- 'buy, sell' + *kʷel- 'turn, move about'); NOT Skt sabhā 'assembly' / OP *abā-čari-\",\n   \"note\": \"Nourai here reproduces verbatim Darmesteter's 1883 etymology (Études iraniennes II, article 'ABÂCARI', pp.129-131): OP abācari- = abā (= Skt sabhā 'lieu de réunion') + cari (abstract of car- 'to go'), hence 'comitii locus', giving NP bāzār. That analysis was rejected within a decade and has not been revived. (a) Horn, Grundriss no.166 (p.38) — the very page Nourai cites at node #4 — says flatly 'Wegen phlv. č ist die Zusammenstellung mit ap. abācaris unmöglich' ('because of the Pahlavi č the connection with OP abācaris is impossible'), and reports in the same footnote that Bartholomae (Litbl. f. or. Phil. I,19) had already argued against Darmesteter's abā = sabhā and proposed instead a(m)bācaris 'Wasserwerk, Brunnen'. (b) The Old Persian hapax of DB I.64 is read abicariš (abi- not abā-) by Kent, Old Persian, Lex. s.v., who glosses it 'pasture lands' (abi- + čar- 'to graze', cf. NP čarīdan); Bartholomae, AiW s.v. māniya-, cites it and says 'Et. und eig. Bed. unsicher'. (c) Phonologically the Iranian reflex of PIIr *sabhā keeps h-: Mann, IEC s.v. sebh- gives 'Av. haba, f.' beside 'Skt. sabha, f. company, meeting-place'; and Walde-Pokorny (Bd. II, root 2. bhā- 'sprechen') derive sabhā itself from *bhā- 'speak' (*'Zusammensprechen'), not from a root 'assemble'. (d) The consensus etymology since Watkins/AHD is *wahā-čaraņa-, i.e. Av. vahā- / NP bahā 'price, sale' (PIE *wes-no-, Pokorny 1173) + *čaraņa- (PIE *kʷel-, which is exactly the 'Kwel' cross-reference Nourai himself puts on node #1). Buck (SYN 11.85) already flagged the older etymology as unsettled ('etym.? Horn 166'). The language label is also odd: 'Sanskrit / Old Persian' pairs a real Sanskrit word (sabhā 'assembly hall') with a disputed reading of an Old Persian hapax.\",\n   \"sources\": [\n    W + \"%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1\",\n    W + \"w%CA%BE%C4%8D%CA%BEl\",\n    ETY + \"bazaar\",\n    \"https://www.ahdictionary.com/word/search.html?q=bazaar\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"BQT:218\", \"status\": \"partial\",\n     \"note\": \"BQT_v1_pages.txt ↵-leaf 438 (the leaf carries 'شه از صفحهٔ ۲۱۷' = 'continued from p.217', so this is printed p.218). Mo'in's footnote s.v. بازار: 'بازار - در پهلوی [و در: هوجستان واچار = سوق‌الاحواز، رک: خوزستان] … محل خرید و فروش کالا و خوراک و پوشاک. لغت فرانسه bazar از پرتقالی گرفته شده و پرتغالیان نیز از ایرانیان گرفته‌اند'. So BQT:218 supports Pahlavi wāčār > NP bāzār (and the Hozēstān wāčār = Sūq al-Ahwāz attestation), but says nothing about Sanskrit sabhā or an Old Persian abācari-, and routes the European word through Portuguese, not Turkish/Italian.\"},\n    {\"ref\": \"DRM:129\", \"status\": \"supports\",\n     \"note\": \"DRM.txt leaves 516-517 = Études iraniennes t. II pp.131-132 (printed page numbers '131' and '132' visible in the OCR; the article 'ABÂCARI' begins on p.129, which is why Nourai cites 129). Darmesteter: 'abâcari- … devait donner: bazar ou bâzâr: on reconnaît le persan بازار … Il se décompose naturellement en abâ et cari; dans cari on reconnaît le substantif qui a donné au persan le suffixe de lieu … c'est sans doute un abstrait de car, aller … abâ semble être un exemple analogue; ce serait le sanscrit sabhâ, lieu de réunion, réunion. L'abâcari, le bâzâr, est donc littéralement comitii locus.' Footnote: 'Cf. le sanscrit sabhâ-cara, qui se rend à la réunion, au conseil.' This is exactly Nourai's root box and node #1 — but it is an 1883 proposal that Horn and Bartholomae rejected.\"},\n    {\"ref\": \"LKT\", \"status\": \"partial\",\n     \"note\": \"LKT.txt leaf ~50, entry no. 278 (printed p.24): '[Pers. bāzār] ‘Markt’ [Horn NpEt S.38, Nr.166]. Das Wort wurde im 17. Jahrhundert durch Reisende zunächst mit Bezug auf orientalische Verhältnisse eingeführt und drang dann … in alle europäischen Sprachen ein: frz. pg. sp. bazar, it. bazar, bazzar … engl. bazar, bazaar …'. Lokotsch documents the European spread from Persian, but gives no Sanskrit/Old Persian root at all — he simply refers the etymology to Horn no.166, which denies the abācari- connection.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Old Persian\", \"words\": \"abâ-cari\", \"verdict\": \"disputed\",\n     \"derivation\": \"The form exists only as one hapax in Darius' Bisotun inscription, DB I.64: 'adām niyāčam kārahyā abičariš gaiθāmčā māniyamčā viθbiščā …'. Darmesteter (Ét. ir. II 129-131) read it abācari-, split it abā + cari-, equated abā with Skt sabhā 'assembly' (assuming exceptional loss of Iranian h- < s-, on the analogy of OP θā-ati for θāhati) and cari- with an abstract of car- 'to go', giving 'place where one goes to assemble' = comitii locus, whence NP bāzār. Kent (Old Persian, Lex.) instead reads abičariš (abi- + čar- 'to move, graze'), acc. of an s-stem, and translates DB I.64 'I restored to the people the pastures and the herds, the household property and the houses', i.e. 'pasture lands' — a reading now standard. Bartholomae (AiW s.v. māniya-) quotes the word and says 'Et. und eig. Bed. unsicher'. Phonetically the Iranian outcome of *sabhā would be *habā- (Av. haba-, Mann IEC s.v. sebh-), so the loss of h- is ad hoc; and Horn adds the decisive objection that Pahlavi wāčār has č, which cannot continue an OP -c- ([ts]/[s]) of abācari-. So the node's gloss ('place of assembly') and its role as the ancestor of bāzār are both rejected by modern Iranian scholarship.\",\n     \"sources\": [W + \"w%CA%BE%C4%8D%CA%BEl\", ETY + \"bazaar\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:218\", \"status\": \"not_found\", \"note\": \"Mo'in's footnote on printed p.218 (BQT_v1_pages.txt leaf 438) gives only Pahlavi واچار and modern dialect forms (نطنزی, سمنانی, سنگسری wazar, استی …); there is no Old Persian abācari- and no Sanskrit on the page.\"},\n      {\"ref\": \"DRM:129\", \"status\": \"supports\", \"note\": \"Ét. ir. II p.131: 'abâ semble être un exemple analogue; ce serait le sanscrit sabhâ, lieu de réunion … L'abâcari, le bâzâr, est donc littéralement comitii locus.' Word-for-word Nourai's node.\"},\n      {\"ref\": \"LKT\", \"status\": \"not_found\", \"note\": \"LKT no. 278 (p.24) gives no Old Persian form; it defers to Horn no.166, which rejects abācaris.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Lexicon s.v. abicariš (KNT.txt l.5015-5018) and §14 translation (l.3573)\", \"stance\": \"contradicts\", \"note\": \"'abicariš DB 1.64f, word of uncertain form and meaning, probably asn. of s-stem, to abi- + root car- ‘move, go’ … giving, in association [with gaiθā and māniya], a meaning ‘pasture lands’, cf. NPers. čarīdan ‘to pasture’ (Spiegel, KT, Bthl. AW 89)'; §14: 'I restored to the people the pastures and the herds…'. Kent reads abi-, not abā-, and glosses 'pasture', not 'place of assembly'.\"},\n      {\"src\": \"BRT\", \"where\": \"AiW s.v. p. māniya- (BRT.txt l.20309)\", \"stance\": \"partial\", \"note\": \"Bartholomae quotes 'kārahya abicaris gaiθamca … Bh. I.14' and comments 'Et. und eig. Bed. unsicher' — he registers the word but refuses both the reading abā- and the meaning 'assembly'.\"},\n      {\"src\": \"IEC\", \"where\": \"s.v. sebh-, sebhi (IEC.txt l.15041)\", \"stance\": \"contradicts\", \"note\": \"Mann: 'sebh-, sebhi (sobh-) ‘self; like; kin…’ … Skt. cf. sabha, f. ‘company, meeting-place’; Av. haba, f. id.; … Go. sibja, f. ‘kinship’'. The Iranian cognate of sabhā is haba- WITH h-, so an Old Persian abā- from this root is not expected.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II, root '2. bhā- ‘sprechen’' (WLD_Bd2 l.7879)\", \"stance\": \"contradicts\", \"note\": \"'Ai. wahrscheinlich in sabha „Versammlung“ (*„Zusammensprechen“…)' — Walde-Pokorny put Skt sabhā under *bhā- 'to speak' with sa-, not under any root 'assemble'.\"},\n      {\"src\": \"POK\", \"where\": \"POK_full.txt (searched 'sabhā', 'sabha-')\", \"stance\": \"silent\", \"note\": \"Pokorny's IEW has no lemma for Skt sabhā and no Iranian abā- 'assembly'; the only 'sabha' hits are the unrelated -ṣabha of ṛṣabhá- 'bull'.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 166, p. 38 (HRN.txt leaf 59)\", \"stance\": \"contradicts\", \"note\": \"'Wegen phlv. č ist die Zusammenstellung mit ap. abācaris unmöglich.' Footnote: '… zu ai. sabhā- ‘Sippe’, das auch schon Darmesteter Ét. ir. II,131 in abā gesucht und wogegen Bartholomae, Litbl. f. or. Phil. I,19 sich ausgesprochen hatte.'\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"vâ-čar\", \"verdict\": \"disputed\",\n     \"derivation\": \"The Middle Persian word itself is well attested and correctly given: Book Pahlavi wʾCʾl = wāzār 'market' (Manichaean MP wʾCʾr-), best known from the place-name Hūzēstān wāzār 'the market of Khuzistan', the old name of Ahvāz, rendered in Arabic Sūq al-Ahwāz (Mujmal al-tawārīkh; Tabari, tr. Nöldeke p.13 n.3), and borrowed early into Armenian as vačaṛ, vačaṛakan, vačaṛik. What is disputed is the ARROW: wāzār cannot come from OP abācari-, because Pahlavi č cannot continue OP c, and because the word's real ancestor is Old Iranian *wahā-čaraņa- 'trade-circulation, place of sale' — *wahā- 'sale, price' (Av. vahā-, NP bahā; PIE *wes-no-, Pokorny 1173) + *čaraņa- 'going about' (PIE *kʷel-). Loss of the intervocalic -ņ- and contraction give MP wāzār; Iranian *č > z before the following vowel is regular in this compound (cf. NP bahā). Nourai's 'trade center' gloss is right; his parentage is not.\",\n     \"sources\": [W + \"w%CA%BE%C4%8D%CA%BEl\", ETY + \"bazaar\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:212\", \"status\": \"not_found\", \"note\": \"Wrong page. BQT_v1_pages.txt leaf 432 = printed p.212 contains only باد- headwords (بادقر، بادفراه، بادفرنگ، بادگان …); there is no بازار and no Pahlavi form. The passage Nourai wants (Mo'in's footnote 'بازار - در پهلوی [و در: هوجستان واچار = سوق‌الاحواز]') is on p.218 (leaf 438) — BQT:212 looks like a typo for BQT:218.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dict. s.v. wāzār (PHD.txt l.649)\", \"stance\": \"supports\", \"note\": \"'wāzār [wʾCʾl | M wʾCʾr-, N bāzār] market. wāzāraġān [wʾCʾlkʾn | M wʾCʾrgʾn, N bāzārgān] merchant.' The MP word and its NP outcome are exactly as Nourai draws them (the Old Persian step is not MacKenzie's).\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary (searched wāzār / wʾCʾl)\", \"stance\": \"silent\", \"note\": \"Nyberg's glossary (limited to the texts he edits) has no wāzār entry; the nearest form, wičīr 'judicial decree' (l.4116), is a different word (< OIr *vi-čara-) and Nyberg keeps it apart.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien pp.135, 155 (HUB.txt l.5429, 5446, 5606)\", \"stance\": \"supports\", \"note\": \"'bāzār ‘Markt’ = pāz. vazar Shk. 272, phl. vačar, arm. vačar-'; and in the Armenian list 'vačar ‘Handel, Markt’ = np. bāzār'. Hübschmann confirms Phl. vačar > NP bāzār and the Armenian loan, and gives no Old Persian antecedent.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 166, p.38\", \"stance\": \"contradicts\", \"note\": \"'phlv. ƀāδar ‘Markt’ (vergl. arm. LW. vačar, vačarakan, vačarik, und Xūfistan vajār, Nöldeke, Tabari-übersetzung, 13 Note 3) … Wegen phlv. č ist die Zusammenstellung mit ap. abācaris unmöglich.'\"},\n      {\"src\": \"BQT\", \"where\": \"printed p.218 s.v. بازار (leaf 438)\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote gives Pahlavi واچار and the phrase هوجستان واچار = سوق الاحواز — i.e. the same MP form Nourai prints, but reached from Persian, not from Old Persian.\"},\n      {\"src\": \"AEF\", \"where\": \"AEF:219 (Nourai's cross-reference note on this node)\", \"stance\": \"partial\", \"note\": \"Khaleqi Motlaq's Asās-e Ešteqāq-e Fārsi is the Persian translation of Horn's Grundriss and is not digitised; the corresponding original is HRN no.166 p.38, which — far from 'further discussion' in support — declares the abācaris connection impossible.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"bâzâr «بازار»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP bāzār 'market' is the regular inherited continuation of MP wāzār: initial Middle Persian w- > NP b- (the standard change, cf. MP wād > NP bād 'wind', MP wed > NP bed 'willow'), the rest unchanged. It is attested from the earliest New Persian poetry onward (the verse Nourai quotes is Vaḥši Bāfqi, 16th c.). From Persian the word was lent out in every direction: Armenian vačaṛ, Aramaic/Talmudic, Arabic bāzār, Ottoman Turkish bāzār/pazar, Hindi-Urdu bāzār, Malay pasar, and thence the European family. Only the pre-Middle-Persian step (node #1) is in doubt; this node is not.\",\n     \"sources\": [W + \"%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1\", W + \"w%CA%BE%C4%8D%CA%BEl\", ETY + \"bazaar\"],\n     \"ref_check\": [\n      {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Fārsi s.v. (MON_part1.txt l.20350): 'بازار: bāzār (ا.) محل خرید و فروش کالا و خوراک. کوچه سرپوشیده که از دو سوی دارای دکان‌ها باشد: بازارگاه' — no foreign-origin tag (i.e. native Persian, in contrast to e.g. '[ع.]' for Arabic loans), and in his Borhān footnote he gives the Pahlavi antecedent واچار.\"},\n      {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 93 (printed p.156) s.v. 'bazaar': 'bazaar, n., a market place. — Ult. fr. Pers. bāzar, ‘market’, which is rel. to Pahlavi vacar, of s.m.' Klein confirms exactly the Pahlavi vačar ~ Persian bāzār pair.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"s.v. wāzār\", \"stance\": \"supports\", \"note\": \"'[wʾCʾl | M wʾCʾr-, N bāzār] market' — MacKenzie himself equates the MP and NP forms.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p.135\", \"stance\": \"supports\", \"note\": \"'bāzār ‘Markt’ = pāz. vazar Shk. 272, phl. vačar, arm. vačar-' — listed among Hübschmann's examples of ap./mp. va- > np. bā-.\"},\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.76 s.v. BAZAAR\", \"stance\": \"supports\", \"note\": \"'From P. bāzār, a permanent market or street of shops. The word has spread westward into Arabic, Turkish, and, in special senses, into European languages, and eastward into India … The word is adopted into Malay as pāsār.'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck, Selected Synonyms 11.85 'market' (SYN.txt l.20976)\", \"stance\": \"partial\", \"note\": \"'NG παζάρι, fr. Turk. pazar, this fr. Pers. bazar ‘market’ (etym.? Horn 166).' Buck accepts the Persian word as the source of the Turkish and European forms but marks its own etymology as unsettled.\"},\n      {\"src\": \"RCH\", \"where\": \"Richardson-Johnson, Persian-Arabic-English Dict. (RCH.txt l.14761)\", \"stance\": \"supports\", \"note\": \"Persian headwords 'بازرگان bāzargān, A merchant, a trader' / 'bāzargānī kardan, To trade, to buy and sell' — the family is treated as native Persian.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Persian\", \"words\": \"bâzargân «بازرگان»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"'Merchant' is right and the connection with bāzār is right, but the word was not coined in New Persian: MacKenzie records MP wāzāraġān [wʾCʾlkʾn], Manichaean MP wʾCʾrgʾn 'merchant', so NP bāzargān/bāzergān is inherited alongside bāzār rather than derived from it in Persian. Darmesteter (Ét. ir. I §217) explains the morphology: an adjective in -ān was added to a stem *bāzārak 'merchant', giving bāzāragān; once *bāzārak dropped out of use the word 'semble formé de bazar, par suffixe gān', which is how the productive Persian suffix -gān arose. The vowel of the second syllable is shortened in bāzargān < bāzāragān by regular medial reduction. The abstract bāzargānī 'trade' continues MP wāzāraġānīh.\",\n     \"sources\": [W + \"%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1\", W + \"w%CA%BE%C4%8D%CA%BEl\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:219\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 438/439 (printed pp.218-219), immediately after بازار: 'بازارگان - با کاف فارسی بالف کشیده و بنون زده، سوداگر را گویند' and 'بازرگان - مخفف بازارگان است که سوداگر باشد' — Borhān gives exactly Nourai's gloss 'merchant' and derives bāzargān as the contracted form of bāzāragān.\"},\n      {\"ref\": \"HRN:38\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 59 = printed p.38, entry no. 166: 'bāzār ‘Markt’, bāzargan, bāzergān ‘Kaufmann’.' Horn heads the entry with exactly this pair. (The same page, however, denies the Old Persian abācaris etymology of the root box.)\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"s.v. wāzāraġān\", \"stance\": \"supports\", \"note\": \"'wāzāraġān [wʾCʾlkʾn | M wʾCʾrgʾn, N bāzārgān] merchant. ~īh: trade.' — shows the word is already Middle Persian.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p.134 (HUB.txt l.4710)\", \"stance\": \"supports\", \"note\": \"'ḥazargan ‘Kaufmann’ = bāzorgan von bāzār ‘Markt’' — Hübschmann derives the merchant word from the market word.\"},\n      {\"src\": \"DRM\", \"where\": \"Ét. ir. I §217 (DRM.txt l.5840)\", \"stance\": \"partial\", \"note\": \"'Le thème *bâzârak, marchand, augmenté du suffixe d’adjectif ān, donne bāzâragan et, par suite de la chute du mot bâzârak, bâzârgan semble formé de bazar, par suffixe gan' — i.e. the bāzār > bāzargān arrow is only an apparent one.\"},\n      {\"src\": \"RCH\", \"where\": \"RCH.txt l.14761, 14767\", \"stance\": \"supports\", \"note\": \"'بازرگان bāzargān, A merchant, a trader'; 'bāzgān (for bāzargān), A merchant.'\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Turkish\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Empty pass-through node: Ottoman Turkish بازار bāzār, with the regular Turkish devoicing of the initial in the popular form pazar 'market; Sunday (market-day)', borrowed from Persian bāzār during the long Persianate phase of Ottoman/Seljuq lexis. Turkish is the vehicle by which the word reached the Balkans and the Mediterranean (Bulgarian/Serbian pazar, Modern Greek παζάρι), and the 1976 AHD, Etymonline and Nourai all make it the link between Persian and Italian. Hobson-Jobson's early Genoese attestation (c.1340) suggests direct Levantine trade contact could also have carried it, so Turkish is the likely but not the only possible conduit.\",\n     \"sources\": [ETY + \"bazaar\", W + \"%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1\"],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node.\"}],\n     \"consulted\": [\n      {\"src\": \"SYN\", \"where\": \"Buck 11.85 (SYN.txt l.20976)\", \"stance\": \"supports\", \"note\": \"'NG παζάρι, fr. Turk. pazar, this fr. Pers. bazar ‘market’' — explicit Persian > Turkish > (Greek/European).\"},\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.76 s.v. BAZAAR\", \"stance\": \"supports\", \"note\": \"'The word has spread westward into Arabic, Turkish, and, in special senses, into European languages.'\"},\n      {\"src\": \"LKT\", \"where\": \"no. 278, p.24\", \"stance\": \"partial\", \"note\": \"Lokotsch heads the entry 'Pers. bāzār' and lists Bulgarian/Serbian pazar among the outcomes, but he attributes the European spread to 17th-c. travellers and the Arabian Nights rather than naming a Turkish intermediary.\"},\n      {\"src\": \"TTS\", \"where\": \"Vámbéry, Etym. Wb. der turko-tatarischen Sprachen (grepped 'bazar', 'pazar', 'Markt')\", \"stance\": \"silent\", \"note\": \"No entry — expected, since Vámbéry's dictionary treats inherited Turkic stems, not Persian loanwords.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Italian\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Empty pass-through node: Italian bazarra / bazzarro / bazarro 'market', with the doubling and the -a/-o ending typical of Italian adaptations of Levantine words. It is attested strikingly early: Francesco Balducci Pegolotti's merchant handbook (c.1340) already lists Bazarra as the Genoese word for 'market-place', and the Venetian envoys to Persia use it — Ambrogio Contarini 1474 'con bazzari come quello', Giosafat Barbaro 1478 'un ricco mercante in bazarro'. Italian bazzarare 'to cheat' is a derivative. From Italian the word passed to English (1580s) and, in parallel, French bazar.\",\n     \"sources\": [ETY + \"bazaar\", \"https://www.ahdictionary.com/word/search.html?q=bazaar\"],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node.\"}],\n     \"consulted\": [\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.76 s.v. BAZAAR\", \"stance\": \"supports\", \"note\": \"'The word seems to have come to S. Europe very early. F. Balducci Pegolotti, in his Mercantile Handbook (c. 1340) gives Bazarra as a Genoese word for ‘market-place’ (Cathay, &c. ii. 286)'; then the citations '1474 … with bazars (bazzari)' and '1478 … in the bazar (bazarro)'.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 278, p.24\", \"stance\": \"supports\", \"note\": \"'… it. bazar, bazzar … Da das Grundwort stimmhaftes s [z] hat, gehört sicherlich auch it. bazzarare ‘täuschen, betrügen’, siz. bazzariotu ‘Betrüger’ hierher.'\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. bazaar (FSD_vol1.txt l.37535-37540)\", \"stance\": \"contradicts\", \"note\": \"'[< F. bazar, < Per. bazar, market.]' — Funk & Wagnalls routes English bazaar through French, not Italian.\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966 p.156 s.v. bazaar\", \"stance\": \"silent\", \"note\": \"Klein writes only 'Ult. fr. Pers. bāzar' and names no European intermediary at all.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"bazaar\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English bazaar is first recorded in the 1580s in accounts of the East, taken from Italian bazarra (so Etymonline and the 1976 AHD, which spell the chain out as Italian bazarra < Turkish pazar < Persian bāzār < Pahlavi vacar < Old Iranian *vahā-čarana 'sale, traffic'). The spelling with -aar and the stress bə-ZÄR follow the Persian; the senses 'fancy fair for charity' (19th c.) and 'large fancy store' are English developments. Anglo-Indian usage reinforced the word in the 18th-19th c. through Hindi-Urdu bāzār.\",\n     \"sources\": [ETY + \"bazaar\", \"https://www.ahdictionary.com/word/search.html?q=bazaar\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Current AHD online s.v. bazaar: '[Italian bazarro and Urdu bāzār, both from Persian bāzār; see wes-3 in the Appendix of Indo-European roots.]' — supports the Italian > English step and the Persian source, but files the root under *wes- 'to buy, sell', not under any root 'assemble'. (The local AHD_watkins1985.txt has 'wes-1. To buy. … [Pok. 8. wes- 1173]' but, being only the root appendix, lists no bazaar; Nourai's AHD page numbers are the 1976 appendix, whose bazaar entry also read 'Italian bazarra, from Turkish pazar, from Persian bāzār'.)\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966 p.156 s.v. bazaar\", \"stance\": \"partial\", \"note\": \"'bazaar, n., a market place. — Ult. fr. Pers. bāzar, ‘market’, which is rel. to Pahlavi vacar' — same ultimate source, but Klein says 'ultimately' and names no Turkish or Italian stage.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict. s.v. (WEB_vol1.txt l.16947)\", \"stance\": \"partial\", \"note\": \"'ba-zaar’, ba-zar’, n. [Per. bazar, a market.]' — Persian source only.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. bazaar\", \"stance\": \"partial\", \"note\": \"'1. An Oriental market-place or range of shops … 2. A fancy fair for charity. 3. A large fancy-store or shop. [< F. bazar, < Per. bazar, market.]' — French rather than Italian intermediary.\"},\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.76\", \"stance\": \"supports\", \"note\": \"Traces the English word's Anglo-Indian career from 1563 ('bazar, as much as to say the place where things are sold') and 1638 ('We came into a Bazar, or very faire Market place').\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"A`.b.r\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Proto-Semitic *ʕabar- 'to cross, pass over'\",\n   \"note\": \"The root box is right: ʕ-b-r 'to cross over' is a genuine common-Semitic root (Arabic ʕabara, Hebrew ʕāḇar, Aramaic/Syriac ʕăḇar, Akkadian ebēru, Old South Arabian ʕbr 'to transgress', Geʿez), and the Hebrew branch (ʕibrī 'Hebrew' = 'he from across the river' > Aram. ʕibray > Gk Ἑβραῖος > Lat. Hebraeus > English Hebrew) is Klein's entry almost word for word. The one contested limb is the middle one: the claim that Arabic ʕ-r-b (ʕarab 'Arab') is a metathesised ('distorted') form of ʕ-b-r, making 'Arab' and 'Hebrew' the same word. Nourai's own source Bahar (SBK) reports that as the view of 'modern scholars', but Nourai's other own source Klein (KLN:98) does NOT: Klein derives ʕarab from the sense 'desert' (Heb. ʕărāḇāh), and current handbooks list the ʕ-b-r metathesis as only one of several competing hypotheses ('west, sunset', 'desert', 'mingle', 'merchant', 'raven'). Two smaller drawing faults: the Latin stage (L. Arabs, acc. Arabem) is missing between Greek and French for 'Arab', and the Old French/Middle English stage (OF Ebreu > ME Ebreu, H- restored in the 16th c.) is missing between Latin and English for 'Hebrew'.\",\n   \"sources\": [W + \"%D8%B9%D8%A8%D8%B1\", W + \"Hebrew\", ETY + \"Hebrew\", ETY + \"Arab\", \"https://en.wikipedia.org/wiki/Arabs\"],\n   \"ref_check\": [\n    {\"ref\": \"KLN:712\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.17390, between the printed page markers 712 (l.17381) and 713 (l.17393), i.e. exactly p.712, s.v. 'Hebrew': '… fr. Heb. ‘ibhrī, ‘Hebrew’, lit. ‘he who came from across (the River)’, fr. ‘ibher, ‘region across, side’, from the stem of ‘abhar, ‘he passed across or over’, which is rel. to Aram.-Syr. ‘abhar, Arab. ‘ābara, ‘he passed across’, Akkad. eberu, ‘to pass over’ … Cp. Habiru.' The Semitic root box, its gloss and the Arabic/Hebrew/Aramaic branches are all Klein's.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Arabic\", \"words\": \"a`.b.r; abara\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic عبر ʕ-b-r is the direct Arabic continuation of Proto-Semitic *ʕabar- 'to cross'; the form Nourai transliterates 'abara' is the 3 m.sg. perfect عَبَرَ ʕabara 'he crossed, traversed, forded' (his gloss 'he passes across' should be a past, as in Klein's 'he passed across'). Same root: عَبْر ʕabr 'crossing', عِبْرَة ʕibra 'lesson' (< 'what one crosses over to'), عَبَّرَ ʕabbara 'to express, interpret'. Cognates: Hebrew עָבַר ʕāḇar, Akkadian ebēru, OSA ʕbr.\",\n     \"sources\": [W + \"%D8%B9%D8%A8%D8%B1\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:712\", \"status\": \"supports\", \"note\": \"KLN_1966 p.712 s.v. Hebrew: '… which is rel. to Aram.-Syr. ‘abhar, Arab. ‘ābara, ‘he passed across’, Akkad. eberu, ‘to pass over’.' Klein cites the Arabic verb in precisely Nourai's shape and sense.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966 p.712 s.v. Hebrew\", \"stance\": \"supports\", \"note\": \"See above; Klein makes Arabic ʕabara a cognate (not a source) of Hebrew ʕāḇar, which is what a common Semitic root box means.\"},\n      {\"src\": \"LKT\", \"where\": \"LKT.txt l.246, entry on ar. as-šiʕrā al-ʕabūr (Sirius)\", \"stance\": \"supports\", \"note\": \"'… vom ar. Stamme ‘br ‘wandern’ [vgl. hebr. ‘ibrī ‘Hebräer’, d. h. derjenige, der gewandert ist od. überschritten hat sc. den Euphrat od. Jordan]' — Lokotsch uses the same root and the same 'crossed the river' explanation.\"},\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (grepped ‘ibri, ‘abara)\", \"stance\": \"silent\", \"note\": \"Fraenkel lists no ʕ-b-r item — consistent with the root being inherited Arabic rather than an Aramaic loan.\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʼān (grepped 'ibri', 'abara')\", \"stance\": \"silent\", \"note\": \"No entry; Jeffery treats only foreign words, and ʕabara is native Arabic.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"obŭr «عبور»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian عبور obūr is the Arabic verbal noun (maṣdar) عُبُور ʕubūr, pattern fuʕūl, of ʕabara 'to cross', taken into Persian with the usual Persian pronunciation of the Arabic ʕu- as o- and no change of consonants. The extras Nourai prints are all further ʕ-b-r derivatives borrowed alongside it: عابر ʕābir 'one who crosses, passer-by' (active participle fāʕil), معبر maʕbar 'crossing-place, ford' (noun of place mafʕal), pl. معابر maʕābir. Direction of borrowing is Arabic > Persian (post-conquest lexical Arabising), not a round trip.\",\n     \"sources\": [W + \"%D8%B9%D8%A8%D9%88%D8%B1\", W + \"%D8%B9%D8%A8%D8%B1\"],\n     \"ref_check\": [\n      {\"ref\": \"FVA:260\", \"status\": \"not_checked\", \"note\": \"S.M. Nahvi, Farhang-e Vāžehā-ye ʿArabi dar Fārsi (1368/1989): refs_online.json records 'Searched archive.org, ketabnak, noorlib, web: no digital copy found.' Not accessible.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi s.v. عبور (MON_part1.txt, ~l.94814)\", \"stance\": \"supports\", \"note\": \"'عبور: obūr [ع.] (مص ل.) گذشتن، عبور کردن (از نهر، وادی و غیره). عبور و مرور…' — the tag [ع.] marks it as an Arabic loan, and Mo'in's reading obūr matches Nourai's 'obŭr'.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. عبور\", \"stance\": \"supports\", \"note\": \"Arabic عُبُور ʕubūr 'verbal noun of عَبَرَ (ʕabara, ‘to cross’)'; Persian عبور obur 'borrowed from Arabic عُبُور'.\"},\n      {\"src\": \"PLA/AFM\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen; Addi Shir, al-Alfāẓ al-Fārisiyya al-Muʕarraba\", \"stance\": \"silent\", \"note\": \"Neither lists عبور — as expected, since both catalogue Persian words in Arabic, the opposite direction to this node.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Arabic\", \"words\": \"a`.r.b\", \"verdict\": \"disputed\",\n     \"derivation\": \"Nourai (following Bahar) treats عرب ʕ-r-b as a metathesised 'distortion' of عبر ʕ-b-r, so that 'to cross the desert' > 'to dwell in the desert'. Metathesis of the 2nd and 3rd radicals is a real Semitic phenomenon and the equation ʕ-b-r ~ ʕ-r-b was current in 19th-/early-20th-c. Semitic philology (Bahar cites Tārīḫ al-luġāt al-sāmiyya pp.79-81 for it). Modern reference works do not accept it as established: they treat ʕ-r-b as an independent root whose recorded senses are 'west, sunset' (cf. Akk. erēbu 'to enter, to set'), 'desert, steppe' (Heb. עֲרָבָה ʕărāḇāh), 'to mix, mingle', 'merchant' and 'raven', and list the ʕ-b-r derivation only as one alleged hypothesis among these. Decisively for this chart, the very reference Nourai cites for the next node — Klein p.98 — chooses a different origin. So the arrow ʕ-b-r > ʕ-r-b is a minority view presented here as fact.\",\n     \"sources\": [\"https://en.wikipedia.org/wiki/Arabs\", ETY + \"Arab\", W + \"%D8%B9%D8%B1%D8%A8\"],\n     \"ref_check\": [\n      {\"ref\": \"SBK:69\", \"status\": \"supports\", \"note\": \"SBK.txt ll.4035-4046 (Bahar's chapter on the Semitic peoples and the Phoenician script, printed p. ~69): 'نام «عبری» از مادهٔ «عبر» و بمعنی عبور و حرکت و اشاره بصحرانوردی آن طایفه است' and, decisively, 'وعلمای معاصر ترجیح میدهند که عبری را از مادهٔ عبور گرفته … چنانکه «عرب» را هم از همین [ماده] و بهمان معنی میدانند و ثلاثی مجرد … «عبر» و «عرب» را یکی دانند که بقاعدهٔ قلب لغات اختلاف یافته است' ('… they hold the triliteral roots ʕ-b-r and ʕ-r-b to be one and the same, differentiated by the rule of metathesis'), with the footnote 'رک: تاریخ اللغات السامیه ص ۷۹-۸۰-۸۱ وبعدها'. This is Nourai's claim verbatim. (SBK.txt carries no page breaks; the passage sits in the section that in the 1st ed. runs pp. ~66-72, so p.69 is consistent but could not be confirmed to the page.)\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966 p.98 s.v. Arab (l.3277; the printed marker '96' stands at l.3233)\", \"stance\": \"contradicts\", \"note\": \"'Arab, n. — F. Arabe, fr. L. Arabem, acc. of Arabs, fr. Gk. Ἄραψ, gen. Ἄραβος, fr. Arab. ‘Arab, which lit. means ‘inhabitant of the desert’, and is rel. to Heb. ‘arabhāh, ‘desert’, and to Ethiop. ‘abra, ‘was dry, was waste’.' Klein derives ʕarab from a root meaning 'desert/dry', not from a metathesis of ʕ-b-r.\"},\n      {\"src\": \"Wikipedia\", \"where\": \"en.wikipedia.org/wiki/Arabs, Etymology\", \"stance\": \"partial\", \"note\": \"Lists the root senses \\\"'west, sunset', 'desert', 'mingle', 'mixed', 'merchant' and 'raven'\\\" and reports the metathesis view only as an allegation — \\\"ʕ-B-R, 'moving around' (Arabic ʕ-B-R, 'traverse') and hence, it is alleged, 'nomadic'\\\" — with no single explanation favoured.\"},\n      {\"src\": \"LKT\", \"where\": \"LKT.txt l.423, entry 'Ar. ‘arab'\", \"stance\": \"silent\", \"note\": \"Lokotsch traces the spread of ʕarab into Romanian, Russian, Romance and English but offers no etymology of the Arabic root itself.\"},\n      {\"src\": \"AFA\", \"where\": \"Fraenkel (grepped 'arab, Hebräer)\", \"stance\": \"silent\", \"note\": \"No treatment of the ethnonym's root; Fraenkel's concern is Aramaic loans.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Arabic\", \"words\": \"a`rab\", \"verdict\": \"confirmed\",\n     \"derivation\": \"The word and the gloss are correct: عَرَب ʕarab is the collective 'the Arabs', and أَعْرَاب aʕrāb (the form Nourai transliterates 'a`rab') is its plural used specifically of the desert-dwelling Bedouin, as opposed to settled ʕarab — the distinction the Qurʼān itself draws (S. 9:97 al-aʕrāb). Both are formations on the root ʕ-r-b, so the arrow from node #3 is right as a root-to-derivative step; what is disputed is only where that root itself comes from (see node #3). Klein glosses ʕarab 'inhabitant of the desert', matching Nourai's 'desert dweller, Arab'.\",\n     \"sources\": [ETY + \"Arab\", \"https://en.wikipedia.org/wiki/Arabs\"],\n     \"ref_check\": [\n      {\"ref\": \"SBK:69\", \"status\": \"supports\", \"note\": \"Bahar, same passage: 'چنانکه «عرب» را هم از همین و بهمان معنی میدانند' — ʕarab from the same root and with the same 'crossing/wandering the desert' sense.\"},\n      {\"ref\": \"KLN:98\", \"status\": \"partial\", \"note\": \"KLN_1966 p.98 s.v. Arab: 'fr. Arab. ‘Arab, which lit. means ‘inhabitant of the desert’' — supports the word and the gloss exactly, but explicitly relates it to Heb. ‘arabhāh 'desert' and Ethiop. ‘abra 'was dry', i.e. NOT to a metathesised ʕ-b-r. Klein adds the parallel 'cp. Arab. badawī, ‘Bedouin’, lit. ‘desert dweller’, fr. badw, ‘camp, desert’.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966 p.98 s.v. Arab\", \"stance\": \"partial\", \"note\": \"Same entry; confirms the meaning 'inhabitant of the desert', contradicts the parentage drawn above it.\"},\n      {\"src\": \"LKT\", \"where\": \"LKT.txt l.423 'Ar. ‘arab'\", \"stance\": \"supports\", \"note\": \"Treats ʕarab as the Arabic ethnonym and source of all the European reflexes ('Npr. ‘die Araber’ … rum. arab, russ. arap … sp. alarbe [with the Arabic article]').\"},\n      {\"src\": \"Wikipedia\", \"where\": \"en.wikipedia.org/wiki/Arabs\", \"stance\": \"supports\", \"note\": \"'Arab … comes from the desert origin of the Bedouins whom it originally described as arava … meaning ‘desert’ or ‘wilderness’.'\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Persian\", \"words\": \"Arab «عرب»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian عرب ʕarab is a straight lexical borrowing of the Arabic collective عَرَب, unchanged in consonants and written with ع in the Arabic manner (pronounced arab in Persian, the ʕayn being lost). The three extras are likewise Arabic derivatives of ʕ-r-b borrowed wholesale: إعراب eʕrāb, form-IV verbal noun, 'making (speech) Arabic clear' → the technical term for the inflectional vowels/case-endings of Arabic grammar; أعرابی aʕrābī, nisba to aʕrāb, 'a Bedouin'; معرّب muʕarrab, passive participle of form II ʕarraba, 'Arabicised (word)' — the standard term in Persian and Arabic philology for a loanword adapted into Arabic.\",\n     \"sources\": [W + \"%D8%B9%D8%B1%D8%A8\"],\n     \"ref_check\": [\n      {\"ref\": \"FVA:265\", \"status\": \"not_checked\", \"note\": \"Nahvi's Farhang-e Vāžehā-ye ʿArabi dar Fārsi has no digital copy (refs_online.json: 'Searched archive.org, ketabnak, noorlib, web: no digital copy found').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi (MON_part2.txt l.56156 and the عرب family)\", \"stance\": \"supports\", \"note\": \"Mo'in tags the whole family as Arabic, e.g. 'مستعرب: mostaʕrab [ع.] (افا.)' — the bracketed [ع.] is his mark for an Arabic loan, the same tag he puts on عبرانی and عبور.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. عرب (Persian section)\", \"stance\": \"supports\", \"note\": \"Persian عرب is given as inherited from Classical Persian عرب, itself the Arabic word; no independent Iranian etymology.\"},\n      {\"src\": \"AFM/PLA\", \"where\": \"Addi Shir; Asbaghi\", \"stance\": \"silent\", \"note\": \"Both catalogue Persian words Arabicised, so an Arabic word Persianised is outside their scope — confirming the direction is Arabic > Persian.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Greek\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Empty pass-through node: Ancient Greek Ἄραψ Áraps, gen. Ἄραβος Árabos, with the country-name Ἀραβία Arabía, taken from the Semitic ethnonym ʕarab (already Assyrian Ḵur-ba-a-a / Aribi in the 9th-8th c. BCE) and used by Aeschylus and Herodotus from the 5th c. BCE. The Greek nom. Ἄραψ is a labial-stem formation (Ἀραβ- + -ς > -ψ), which is why the Latin nominative is Arabs.\",\n     \"sources\": [ETY + \"Arab\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:98\", \"status\": \"supports\", \"note\": \"KLN_1966 p.98 s.v. Arab: '… fr. Gk. Ἄραψ, gen. Ἄραβος, fr. Arab. ‘Arab' — exactly this node and its parent.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966 p.98 s.v. Arab, Arabic, Arabis\", \"stance\": \"supports\", \"note\": \"Klein derives L. Arabicus and ML Arabis from L. Arabs < Gk Ἄραψ, confirming the Greek link is the pivot of the whole Western family.\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/Arab\", \"stance\": \"supports\", \"note\": \"'Arabic ‘arab → Greek Araps → Latin Arabs → Old French Arabi → English Arab.'\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"plausible\",\n     \"derivation\": \"Empty pass-through node: Old French Arabi / arabe, Modern French Arabe, the immediate source of the English noun. The chart is right that French mediates, but it omits the Latin stage that both Klein and Etymonline insert: Greek Ἄραψ/Ἄραβος was borrowed into Latin as Arabs, acc. Arabem, and it is the Latin accusative (the regular input to Old French nouns) that yields OF Arabe/Arabi — Greek could not have given French directly. Hence 'plausible' rather than 'confirmed': the route is compatible with the sources but a link is missing.\",\n     \"sources\": [ETY + \"Arab\"],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node.\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966 p.98 s.v. Arab\", \"stance\": \"partial\", \"note\": \"'Arab, n. — F. Arabe, fr. L. Arabem, acc. of Arabs, fr. Gk. Ἄραψ' — French yes, but from Latin, not straight from Greek.\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/Arab\", \"stance\": \"partial\", \"note\": \"'… from Latin Arabs → Old French Arabi → English Arab (late 14c.)' — same missing Latin link.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"English\", \"words\": \"Arab\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English Arab is attested from the late 14th century, borrowed from Old French Arabe/Arabi (Latin Arabem, Greek Ἄραψ, Arabic ʕarab). Derivatives followed the same route: Arabic (adj.) from OF, from L. Arabicus; arabesque from French/Italian arabesco. The 19th-c. sense 'street Arab, homeless little wanderer' (1848) is a metaphor on Bedouin nomadism, not a separate word.\",\n     \"sources\": [ETY + \"Arab\", W + \"Arab\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:98\", \"status\": \"supports\", \"note\": \"KLN_1966 p.98: 'Arab, n. — F. Arabe, fr. L. Arabem, acc. of Arabs, fr. Gk. Ἄραψ, gen. Ἄραβος, fr. Arab. ‘Arab … Derivatives: Arabesque (q.v.), Arab-ian, adj. and n., Arabic (q.v.) …'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/Arab\", \"stance\": \"supports\", \"note\": \"'Arabic ‘arab, indigenous name of the people, perhaps literally ‘inhabitant of the desert’ … English Arab, attested from late 14c.'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (grepped '^Arab')\", \"stance\": \"silent\", \"note\": \"Skeat has no headword 'Arab'; he cites '(F.-Arab.)' only as a source language for words like admiral, alchemy, alcohol.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. Arab\", \"stance\": \"partial\", \"note\": \"'Borrowed from Arabic عَرَب (ʕarab, ‘Arabs’) or back-formation from Arabic' — Wiktionary short-circuits the Romance chain that Klein and Etymonline spell out.\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"Hebrew\", \"words\": \"âbhar; ibhri\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Hebrew עָבַר ʕāḇar 'he passed over, crossed' is the direct Hebrew reflex of Proto-Semitic *ʕabar-; from its noun עֵבֶר ʕēḇer 'region across, the other side' is formed the gentilic עִבְרִי ʕiḇrī 'Hebrew', literally 'he (who came) from across (the River)' — the epithet used of Abram in Gen. 14:13 and of the Israelites in the Joseph and Exodus narratives, characteristically in the mouths of foreigners. Whether 'the River' is the Euphrates or the Jordan is undecided; Klein and Etymonline both note the possibility that it simply meant 'immigrant, one from the other side', and Klein cross-refers to the Amarna-age Ḫabiru. Nourai's gloss for ʕiḇrī reproduces this explanation.\",\n     \"sources\": [W + \"Hebrew\", ETY + \"Hebrew\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:712\", \"status\": \"supports\", \"note\": \"KLN_1966 p.712 s.v. Hebrew: 'fr. Heb. ‘ibhrī, ‘Hebrew’, lit. ‘he who came from across (the River)’, fr. ‘ibher, ‘region across, side’, from the stem of ‘abhar, ‘he passed across or over’ … Cp. Habiru.' Nourai's two words and both glosses come straight from here.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966 p.712 s.v. Hebrew\", \"stance\": \"supports\", \"note\": \"As quoted; Klein also lists the cognate nouns Heb. ‘ebhrāh 'fury' (lit. 'overflow') and ma‘ăbhār 'ford, pass' from the same stem.\"},\n      {\"src\": \"SBK\", \"where\": \"Bahar, Sabk-shenāsi I (SBK.txt ll.4035-4046)\", \"stance\": \"supports\", \"note\": \"'نام «عبری» از مادهٔ «عبر» و بمعنی عبور و حرکت و اشاره بصحرانوردی آن طایفه است' — and reports the tradition that ʕibrī refers to Abraham's crossing of the river from Ur, 'and it is not known whether that river is the Jordan or the Euphrates'.\"},\n      {\"src\": \"LKT\", \"where\": \"LKT.txt l.246\", \"stance\": \"supports\", \"note\": \"'hebr. ‘ibrī ‘Hebräer’, d. h. derjenige, der gewandert ist od. überschritten hat sc. den Euphrat od. Jordan'.\"}\n     ]\n    },\n    {\n     \"id\": 10, \"lang\": \"Aramaic\", \"words\": \"Ibhray\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Aramaic עִבְרַי ʕiḇray / ʕeḇray (Syriac ʕeḇrāyā) is the Aramaic gentilic corresponding to Hebrew ʕiḇrī, with the Aramaic nisba ending -ay for Hebrew -ī. It is the form that stood behind the Greek transcription, since Greek Ἑβραῖος has -ai- reflecting Aramaic -ay, not Hebrew -ī — which is Klein's and Wiktionary's reason for inserting an Aramaic stage at all. Aramaic was the everyday language of Palestinian Jewry in the Hellenistic period, so the mediation is historically as well as phonetically expected.\",\n     \"sources\": [W + \"Hebrew\", ETY + \"Hebrew\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:712\", \"status\": \"supports\", \"note\": \"KLN_1966 p.712 s.v. Hebrew: 'fr. Gk. Ἑβραῖος, fr. Aram. ‘ibhray, ‘ebhray, fr. Heb. ‘ibhrī' — both forms Nourai prints, in Nourai's order.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. Hebrew\", \"stance\": \"supports\", \"note\": \"'… borrowed from Ancient Greek Ἑβραῖος (Hebraîos), borrowed from Aramaic עִבְרַי (ʕiḇray), from Hebrew עִבְרִי (ʕiḇrí).'\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/Hebrew\", \"stance\": \"supports\", \"note\": \"'from Old French Ebreu, from Latin Hebraeus, from Greek Hebraios, from Aramaic (Semitic) ‘ebhrai.'\"},\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen\", \"stance\": \"silent\", \"note\": \"No ʕibray entry — Fraenkel does not treat the ethnonym, so he neither confirms nor denies an Aramaic > Arabic passage (relevant to node #11).\"}\n     ]\n    },\n    {\n     \"id\": 11, \"lang\": \"Arabic\", \"words\": \"\", \"verdict\": \"plausible\",\n     \"derivation\": \"Empty pass-through node: Arabic عِبْرِيّ ʕibrī and عِبْرَانِيّ ʕibrānī 'Hebrew (language, person)'. Because the root ʕ-b-r exists in Arabic in its own right, the Arabic word could in principle be a native formation; but the reference of the nisba to the people, and above all the -ān- of ʕibrānī, point to a calque or borrowing on the Aramaic/Syriac ʕeḇrāyā (with Aramaic -āyā reanalysed and re-suffixed with Arabic -ī), which is how the biblical vocabulary generally entered Arabic — through Syriac-speaking Christians and Jews. The route drawn (Hebrew > Aramaic > Arabic) is therefore likely, but none of the works checked (Fraenkel's Aramaic loanwords in Arabic, Jeffery's Foreign Vocabulary of the Qurʼān, Klein) states it, so it stands as plausible rather than documented.\",\n     \"sources\": [W + \"Hebrew\", W + \"%D8%B9%D8%A8%D8%B1\"],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node.\"}],\n     \"consulted\": [\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (grepped ‘ibri, ibrani, Hebräer)\", \"stance\": \"silent\", \"note\": \"The two 'Hebräer' hits (ll.676, 1467) are historical remarks, not an entry for ʕibrī; Fraenkel does not list the word among his Aramaic loans.\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʼān (grepped ibri, ‘abara)\", \"stance\": \"silent\", \"note\": \"No entry — the word does not occur in the Qurʼān, so Jeffery has no occasion to trace it.\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in s.v. عبرانی (MON_part1.txt l.94758)\", \"stance\": \"supports\", \"note\": \"'عبرانی: ʕebrānī [ع.] (ص نس.) عبری، یهودی؛ ج. عبرانیون، عبرانیین. زبان یهود' — the Arabic-plural forms عبرانیون/عبرانیین show the word had a full Arabic life before reaching Persian, which is what this node asserts.\"}\n     ]\n    },\n    {\n     \"id\": 12, \"lang\": \"Persian\", \"words\": \"ebrî «عبری»; ebrânî «عبرانی»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Both Persian words are Arabic nisbas borrowed unchanged: عبری ebrī and its extended doublet عبرانی ebrānī, both 'Hebrew (person, language)'. Persian keeps the Arabic spelling with ع and simply drops the ʕayn in pronunciation; the choice between the two is stylistic, ebrānī being the commoner in Persian for the language. Note that these do NOT continue any Persian root — they are part of the general post-conquest importation of Arabic religious/ethnographic vocabulary.\",\n     \"sources\": [W + \"Hebrew\"],\n     \"ref_check\": [\n      {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Fārsi (MON_part1.txt l.94758): 'عبرانی: ʕebrānī [ع.] (ص نس.) عبری، یهودی؛ ج. عبرانیون، عبرانیین. زبان یهود' — the [ع.] tag is Mo'in's mark for an Arabic loan, and he glosses عبرانی by عبری, exactly Nourai's pair of words with exactly his gloss 'Hebrew'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"MON_part1.txt l.94758 (عبرانی) and l.94814 (عبور)\", \"stance\": \"supports\", \"note\": \"Both members of the ʕ-b-r family in Persian carry the Arabic-loan tag [ع.].\"},\n      {\"src\": \"BQT\", \"where\": \"Borhān-e Qāʕeʼ (Borhān excludes Arabic words on principle)\", \"stance\": \"silent\", \"note\": \"Borhān is a dictionary of Persian (dari) words; عبری/عبرانی as Arabic loans have no entry, which is itself consistent with the Arabic origin.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. Hebrew / عبر\", \"stance\": \"supports\", \"note\": \"The Arabic nisba عِبْرِيّ is given under the root ع ب ر 'to cross', with Persian among its borrowers.\"}\n     ]\n    },\n    {\n     \"id\": 13, \"lang\": \"Greek\", \"words\": \"Ebraios\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Ancient Greek Ἑβραῖος Hebraîos, borrowed from Aramaic ʕiḇray (the -ai- of the Greek renders Aramaic -ay), with the Greek adjectival/ethnic ending -ος. It is the word of the Septuagint and of Hellenistic Jewish writers (Philo, Josephus) and of the New Testament (e.g. 2 Cor. 11:22, Phil. 3:5, and the title προς Ἑβραίους), which is how it reached Latin Christendom. The rough breathing gives the initial H- that Latin and, eventually, English restore.\",\n     \"sources\": [W + \"Hebrew\", ETY + \"Hebrew\"],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; the parent and child nodes carry KLN:712, which covers it.\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966 p.712 s.v. Hebrew\", \"stance\": \"supports\", \"note\": \"'… fr. L. Hebraeus, fr. Gk. Ἑβραῖος, fr. Aram. ‘ibhray' — the Greek node with both its parent and its child.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. Hebrew\", \"stance\": \"supports\", \"note\": \"Same chain: Latin hebraeus < Ancient Greek Ἑβραῖος < Aramaic עִבְרַי.\"}\n     ]\n    },\n    {\n     \"id\": 14, \"lang\": \"Latin\", \"words\": \"Hebraeus\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin Hebraeus (also Hebraicus 'Hebrew, in Hebrew'), a Christian-Latin transcription of Greek Ἑβραῖος with -αι- rendered by -ae- and the rough breathing by H-. It is the form of the Vetus Latina and of Jerome's Vulgate (Epistula ad Hebraeos; hebraice 'in Hebrew'), and it is from the Latin of the Church that the word entered all the Western vernaculars.\",\n     \"sources\": [W + \"Hebrew\", ETY + \"Hebrew\"],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; KLN:712 on nodes #10 and #15 covers the Latin step.\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966 p.712 s.v. Hebrew\", \"stance\": \"supports\", \"note\": \"'ME. Ebreu, fr. OF. Ebreu, Ebrieu (F. Hébreu), fr. L. Hebraeus, fr. Gk. Ἑβραῖος.'\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/Hebrew\", \"stance\": \"supports\", \"note\": \"'from Old French Ebreu, from Latin Hebraeus, from Greek Hebraios.'\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. Hebrew\", \"stance\": \"supports\", \"note\": \"'from Latin hebraeus, hebraicus, borrowed from Ancient Greek Ἑβραῖος.'\"}\n     ]\n    },\n    {\n     \"id\": 15, \"lang\": \"English\", \"words\": \"Hebrew\", \"verdict\": \"plausible\",\n     \"derivation\": \"English Hebrew is right as the end of the chain, but not straight from Latin: the actual route is Latin Hebraeus > Old French Ebreu / Ebrieu > Middle English Ebreu (adj. in late Old English; the noun for the language c.1200; of the people by the late 14th c.), and the H- was restored in English spelling only in the 16th century under the influence of the Latin form. The chart's Latin > English arrow therefore compresses two attested stages; the etymology is otherwise exactly Klein's. Hence 'plausible' rather than 'confirmed'.\",\n     \"sources\": [W + \"Hebrew\", ETY + \"Hebrew\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:712\", \"status\": \"partial\", \"note\": \"KLN_1966 p.712: 'Hebrew, n. and adj. — ME. Ebreu, fr. OF. Ebreu, Ebrieu (F. Hébreu), fr. L. Hebraeus, fr. Gk. Ἑβραῖος …'. Supports the word and its Latin ancestry, but inserts Old French and Middle English between them, which the chart omits.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/Hebrew\", \"stance\": \"partial\", \"note\": \"'from Old French Ebreu, from Latin Hebraeus … The adjective appears in late Old English, the noun c.1200 for the language, late 14c. for the people; the initial H- was restored in English from the 16th century.'\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. Hebrew\", \"stance\": \"partial\", \"note\": \"'From Middle English Ebreu, from Old French Ebreu, from Latin hebraeus' — same two intermediate stages.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (grepped '^Hebrew')\", \"stance\": \"silent\", \"note\": \"No headword 'Hebrew' in the concise edition.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-34.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build34.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-34.json > /dev/null && echo \"JSON VALID\""
}
```


### [2026-09-04T18:48:09.289Z] TOOL RESULT

```
ok
JSON VALID
```


## [2026-09-04T18:48:12.984Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 tools/verify_check.py 34; echo \"exit=$?\""
}
```


### [2026-09-04T18:48:14.743Z] TOOL RESULT

```
nodes verified: 22/22
node verdicts: {'disputed': 3, 'confirmed': 16, 'plausible': 3}
root verdicts: {'disputed': 1, 'confirmed': 1}
ref checks: {'not_found': 3, 'supports': 14, 'not_checked': 8, 'partial': 2}
books consulted: {'contradicts': 7, 'partial': 15, 'silent': 16, 'supports': 39} | by book: {'KLN': 10, 'Wiktionary': 8, 'LKT': 6, 'Etymonline': 6, 'HJB': 4, 'AFA': 4, 'MON': 4, 'PHD': 3, 'HUB': 3, 'HRN': 2, 'BQT': 2, 'SYN': 2, 'RCH': 2, 'FSD': 2, 'FVQ': 2, 'Wikipedia': 2, 'SKT': 2, 'KNT': 1, 'BRT': 1, 'IEC': 1, 'WLD': 1, 'POK': 1, 'NYB': 1, 'AEF': 1, 'DRM': 1, 'TTS': 1, 'WEB': 1, 'PLA/AFM': 1, 'AFM/PLA': 1, 'SBK': 1}
exit=0
```


## [2026-09-04T18:48:31.275Z] AGENT

Done. `data/verification/page-34.json` written; `verify_check.py 34` reports 22/22 nodes, no PROBLEM lines.

**Page 34 (book p. 4) — 2 entries, 22 nodes**
- Node verdicts: confirmed 16, plausible 3, disputed 3. Root verdicts: confirmed 1, disputed 1.
- Ref checks: supports 14, partial 2, not_found 3, not_checked 8 (FVA has no digital copy; empty-ref nodes).

**Disputed / flagged**
- ROOT `Abâ, Sabha` (Skt/OP, "to assemble") — Nourai reproduces Darmesteter, Ét. ir. II 129-131 verbatim ("abâ … ce serait le sanscrit sabhâ … L'abâcari, le bâzâr, est donc littéralement comitii locus"). Rejected since 1893; consensus is MP wāzār < OIr *wahā-čaraṇa- "place of sale" (*wes- + *kʷel-).
- `#1 OP abâ-cari` — Kent reads the DB I.64 hapax **abicariš** "pasture lands"; Bartholomae: "Et. und eig. Bed. unsicher"; Mann/IEC shows the Iranian cognate of sabhā is Av. *haba-* (with h-).
- `#2 Pahlavi vâ-čar` — word correct (PHD "wāzār [wʾcʾl] market"), but Horn no. 166 p.38 — the page Nourai himself cites at node #4 — says "**Wegen phlv. č ist die Zusammenstellung mit ap. abācaris unmöglich**".
- `#3 Arabic a`.r.b` (metathesis of ʿ-b-r) — SBK:69 *does* support it (Bahar: the two roots are one, "بقاعدهٔ قلب لغات"), but Klein p.98 (Nourai's own next-node ref) derives ʿarab from "desert" (Heb. ʿarabhāh); modern handbooks list metathesis as one hypothesis among several.

**Other findings**
- `BQT:212` (node #2) is a wrong page: p.212 holds only *bād-* headwords; Mo'in's Pahlavi واچار footnote is on **p.218**, the root's own citation.
- `KLN:712` and `KLN:98` verified to the exact printed page and quoted; the whole Hebrew branch is Klein almost verbatim.
- Two chart short-cuts marked *plausible*: Greek→French for "Arab" (Latin *Arabem* missing) and Latin→English for "Hebrew" (OF *Ebreu* / ME missing).
- 12 web pages archived via `fetch_source.py`.
