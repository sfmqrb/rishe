# Verification process log — verify-page-42


## [2026-09-04T19:00:40.307Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 42 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-42.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-42.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-42.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 42` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T19:00:41.719Z] AGENT

I'll start by reading the instructions.


## [2026-09-04T19:00:43.516Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:00:43.535Z] TOOL RESULT

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


## [2026-09-04T19:00:44.246Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-42.txt"
}
```


### [2026-09-04T19:00:44.276Z] TOOL RESULT

```
1	=== PDF page 42 (book page 12) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ak, Aq, Aken : sharp, also a sharp stone  (refs POK:18; KNT:173)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:19; KLN:18; KNT | as 1, asan : stone ; as-man, as-mana : like stone, sky ☞Men 1
5	  #2 (parent #1) [Pahlavi] refs=BQT:39,42,43 | âs : mill, mill stone ; âs-âp : water mill ☞Ab 1 ; vât-âs : wind mill ☞Wě 1 ; âs-mân : sky ☞Men1
6	    #3 (parent #2) [Persian] refs=BQT | âs «آس» : mill ; âsiyâb «آسیاب ، آسیا۱» : water mill ; bâdâs «بادآس» : wind mill ; âsmân «آسمان» : sky
7	#4 (parent #0) [Avestan / Old Persian] refs=SYN:52; BRT:208; KNT:166; FFD:60; SPG:202 | athagaina, athangaina : stone ; âthanga, asenga, asan : stone ; sang, sax : to weigh
8	  #5 (parent #4) [Pahlavi] refs=BQT:1175; SNS:193 | sang : stone ; sang-gil : hard clay ; saxt : weigh
9	    #6 (parent #5) [Arabic] refs=PLA:155; FVQ:164 | sijjîl : baked clay
10	    #7 (parent #5) [Persian] refs=BQT:1175; FFD:60; FSF:224 | sang «سنگ» : stone ; sanjîdan «سنجیدن ( سنجه )» : to weigh ; sanješ «سنجش» : weighing ; saxtan «سختن ( سختیدن )» : to weigh
11	#8 (parent #0) [Greek] refs=AHD | akros : top most ; akrobates : one who walks on tiptoe ☞Gwa ; oxus : sharp, sour
12	  #9 (parent #8) [French] refs=AHD:12 | acrobate ; oxygene : acid former
13	    #10 (parent #9) [Persian] refs=MON:75,331 | âkrobât «آکروبات» ; oksîžen «اکسیژن»
14	    #11 (parent #9) [English] refs=AHD | acrobat, oxygen
15	#12 (parent #0) [Latin] refs=AHD | acere : to be sharp ; vinum-acer : sharp (soar) wine, vinegar ☞Woin ; acus, acetum
16	  #13 (parent #12) [French] refs=None | acide : sour (sharp) substance, acid ; vinaigre : vinegar
17	    #14 (parent #13) [Persian] refs=MON:260,276 | asîd «اسید» ; aseton «استن»
18	    #15 (parent #13) [English] refs=None | acid, acute, vinegar
19	  #16 (parent #12) [Persian] refs=HJB:3 ? | âčâr «آچار» : pickles
20	    #17 (parent #16) [Hindustani] refs=OXF:3 | achar : pickles
21	      #18 (parent #17) [English] refs=OXF:3 | achar
22	#19 (parent #0) [Germanic] refs=AHD | ak-jô : sharp side ; ha-maraz : sharp tool
23	  #20 (parent #19) [English] refs=None | edge ; hammer
24	
```


## [2026-09-04T19:00:49.142Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T19:00:49.188Z] TOOL RESULT

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


## [2026-09-04T19:00:52.272Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','KNT','KLN','SYN','BRT','FFD','SPG','BQT','SNS','PLA','FVQ','FSF','AHD','MON','HJB','OXF','HRN','HUB','PHD','NYB','WLD','IEC','SKT','FSD','WEB','AID','LKT','TTS','CHEUNG','ARY','AFM','DEV','DOZ','LAM','PHN','AFA','SOD','ISS']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False))\n\""
}
```


### [2026-09-04T19:00:54.896Z] TOOL RESULT

```
<persisted-output>
Output too large (52.8KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b680ms36o.txt

Preview (first 2KB):
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)", "local_files": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_0
...
</persisted-output>
```


## [2026-09-04T19:01:00.283Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['KNT','SYN','BRT','FFD','SPG','BQT','SNS','PLA','FVQ','FSF','MON','HJB','OXF','AHD','KLN']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print('==',k,v.get('title','')[:90])\n    print('  kind:',v.get('kind'),'| offset:',str(v.get('page_offset'))[:300])\n    print('  hint:',str(v.get('lookup_hint'))[:400])\n    print('  local:',v.get('local_file'), v.get('local_files'))\n\""
}
```


## [2026-09-04T19:01:00.911Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-42.json | head -200"
}
```


### [2026-09-04T19:01:04.172Z] TOOL RESULT

```
== KNT R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  kind: archive_djvu | offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt None
== SYN C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Ch
  kind: archive_djvu | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt None
== BRT C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pag
  kind: archive_djvu | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th 
  hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt None
== FFD Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
  kind: local_scan_ocr | offset: 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).
  hint: Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
  local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt'] None
== SPG F. Spiegel - title lost in the bibliography OCR (Table IV no. 93 is missing); Table III li
  kind: archive_djvu | offset: Keilinschriften 1881: leaf = printed + 11 for the texts, leaf = printed - 29 for the Glossar (e.g. leaf 182 = p.211). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: IDENTIFICATION UNCERTAIN. Check whether Nourai's SPG page numbers fit the Keilinschriften glossary (pp. ~200-250) or the Alterthumskunde; grep the OP word.
  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SPG_keilinschriften1881.txt None
== BQT Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cite
  kind: archive_djvu+local_scan_ocr | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vo
  hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metada
  local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] None
== SNS Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shir
  kind: archive_djvu | offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
  hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
  local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt'] None
== PLA A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
  kind: archive_djvu | offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
  hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
  local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] None
== FVQ Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Bar
  kind: archive_djvu | offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves)
  hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
  local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] None
== FSF Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Sha
  kind: archive_djvu | offset: 484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking
  hint: grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).
  local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt'] None
== MON Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 for
  kind: website+archive_djvu | offset: None
  hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab
  local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] None
== HJB H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1
  kind: archive_djvu | offset: leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers.
  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt None
== OXF J. Speake, Oxford Dictionary of Foreign Words and Phrases, New York 1997
  kind: archive_restricted | offset: None
  hint: Borrow via IA lending; in-book search ?q=<word>.
  local: None None
== AHD W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edi
  kind: archive_djvu+website+archive_restricted | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
  hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.
  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt None
== KLN E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevi
  kind: archive_djvu | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/detai
  hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt ['/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt']
```


### [2026-09-04T19:01:05.864Z] TOOL RESULT

```
{
    "pdf_page": 42,
    "book_page": 12,
    "entries": [
        {
            "root": {
                "name": "Ak, Aq, Aken",
                "lang": "Indo-European",
                "refs": "POK:18; KNT:173",
                "gloss": "sharp, also a sharp stone",
                "part": 1
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan / Old Persian",
                    "refs": "POK:19; KLN:18; KNT",
                    "words": [
                        {
                            "translit": "as 1, asan",
                            "gloss": "stone",
                            "script": null
                        },
                        {
                            "translit": "as-man, as-mana",
                            "gloss": "like stone, sky",
                            "script": null,
                            "see": [
                                "Men 1"
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
                    "refs": "BQT:39,42,43",
                    "words": [
                        {
                            "translit": "\u00e2s",
                            "gloss": "mill, mill stone",
                            "script": null
                        },
                        {
                            "translit": "\u00e2s-\u00e2p",
                            "gloss": "water mill",
                            "script": null,
                            "see": [
                                "Ab 1"
                            ]
                        },
                        {
                            "translit": "v\u00e2t-\u00e2s",
                            "gloss": "wind mill",
                            "script": null,
                            "see": [
                                "W\u011b 1"
                            ]
                        },
                        {
                            "translit": "\u00e2s-m\u00e2n",
                            "gloss": "sky",
                            "script": null,
                            "see": [
                                "Men1"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Persian",
                    "refs": "BQT",
                    "words": [
                        {
                            "translit": "\u00e2s",
                            "gloss": "mill",
                            "script": "\u0622\u0633"
                        },
                        {
                            "translit": "\u00e2siy\u00e2b",
                            "gloss": "water mill",
                            "script": "\u0622\u0633\u06cc\u0627\u0628 \u060c \u0622\u0633\u06cc\u0627\u06f1"
                        },
                        {
                            "translit": "b\u00e2d\u00e2s",
                            "gloss": "wind mill",
                            "script": "\u0628\u0627\u062f\u0622\u0633"
                        },
                        {
                            "translit": "\u00e2sm\u00e2n",
                            "gloss": "sky",
                            "script": "\u0622\u0633\u0645\u0627\u0646"
                        }
                    ],
                    "note": null,
                    "quote": {
                        "text": "\u0622\u0633\u0645\u0627\u0646 \u0622\u0633\u06cc\u0627\u06cc \u06af\u0631\u062f\u0627\u0646\u0633\u062a - \u0627\u06cc\u0646 \u0686\u0647 \u062e\u0648\u0627\u0647\u062f \u06a9\u0631\u062f\u0646 \u0622\u062e\u0631 \u0622\u0633",
                        "poet": "Onsor\u00ee"
                    }
                },
                {
                    "id": 4,
                    "parent": 0,
                    "lang": "Avestan / Old Persian",
                    "refs": "SYN:52; BRT:208; KNT:166; FFD:60; SPG:202",
                    "words": [
                        {
                            "translit": "athagaina, athangaina",
                            "gloss": "stone",
                            "script": null
                        },
                        {
                            "translit": "\u00e2thanga, asenga, asan",
                            "gloss": "stone",
                            "script": null
                        },
                        {
                            "translit": "sang, sax",
                            "gloss": "to weigh",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "Pahlavi",
                    "refs": "BQT:1175; SNS:193",
                    "words": [
                        {
                            "translit": "sang",
                            "gloss": "stone",
                            "script": null
                        },
                        {
                            "translit": "sang-gil",
                            "gloss": "hard clay",
                            "script": null
                        },
                        {
                            "translit": "saxt",
                            "gloss": "weigh",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 5,
                    "lang": "Arabic",
                    "refs": "PLA:155; FVQ:164",
                    "words": [
                        {
                            "translit": "sijj\u00eel",
                            "gloss": "baked clay",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 5,
                    "lang": "Persian",
                    "refs": "BQT:1175; FFD:60; FSF:224",
                    "words": [
                        {
                            "translit": "sang",
                            "gloss": "stone",
                            "script": "\u0633\u0646\u06af"
                        },
                        {
                            "translit": "sanj\u00eedan",
                            "gloss": "to weigh",
                            "script": "\u0633\u0646\u062c\u06cc\u062f\u0646 ( \u0633\u0646\u062c\u0647 )"
                        },
                        {
                            "translit": "sanje\u0161",
                            "gloss": "weighing",
                            "script": "\u0633\u0646\u062c\u0634"
                        },
                        {
                            "translit": "saxtan",
                            "gloss": "to weigh",
                            "script": "\u0633\u062e\u062a\u0646 ( \u0633\u062e\u062a\u06cc\u062f\u0646 )"
                        }
                    ],
```


## [2026-09-04T19:01:09.180Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-42.json | sed -n '200,400p'"
}
```


## [2026-09-04T19:01:09.568Z] TOOL CALL #8: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py"
}
```


### [2026-09-04T19:01:11.044Z] TOOL RESULT

```
                    ],
                    "note": null,
                    "quote": {
                        "text": "\u0647\u0645\u0647 \u06af\u0646\u062c \u0627\u0631\u062c\u0627\u0633\u067e \u062f\u0631 \u0628\u0627\u0632 \u06a9\u0631\u062f - \u0628\u0647 \u06a9\u067e\u0627\u0646 \u062f\u0631\u0645 \u0633\u062e\u062a\u0646 \u0622\u063a\u0627\u0632 \u06a9\u0631\u062f",
                        "poet": "Ferdows\u00ee"
                    }
                },
                {
                    "id": 8,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "akros",
                            "gloss": "top most",
                            "script": null
                        },
                        {
                            "translit": "akrobates",
                            "gloss": "one who walks on tiptoe",
                            "script": null,
                            "see": [
                                "Gwa"
                            ]
                        },
                        {
                            "translit": "oxus",
                            "gloss": "sharp, sour",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 8,
                    "lang": "French",
                    "refs": "AHD:12",
                    "words": [
                        {
                            "translit": "acrobate",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "oxygene",
                            "gloss": "acid former",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 10,
                    "parent": 9,
                    "lang": "Persian",
                    "refs": "MON:75,331",
                    "words": [
                        {
                            "translit": "\u00e2krob\u00e2t",
                            "gloss": null,
                            "script": "\u0622\u06a9\u0631\u0648\u0628\u0627\u062a"
                        },
                        {
                            "translit": "oks\u00ee\u017een",
                            "gloss": null,
                            "script": "\u0627\u06a9\u0633\u06cc\u0698\u0646"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 9,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "acrobat, oxygen",
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
                    "words": [
                        {
                            "translit": "acere",
                            "gloss": "to be sharp",
                            "script": null
                        },
                        {
                            "translit": "vinum-acer",
                            "gloss": "sharp (soar) wine, vinegar",
                            "script": null,
                            "see": [
                                "Woin"
                            ]
                        },
                        {
                            "translit": "acus, acetum",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 13,
                    "parent": 12,
                    "lang": "French",
                    "refs": null,
                    "words": [
                        {
                            "translit": "acide",
                            "gloss": "sour (sharp) substance, acid",
                            "script": null
                        },
                        {
                            "translit": "vinaigre",
                            "gloss": "vinegar",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 14,
                    "parent": 13,
                    "lang": "Persian",
                    "refs": "MON:260,276",
                    "words": [
                        {
                            "translit": "as\u00eed",
                            "gloss": null,
                            "script": "\u0627\u0633\u06cc\u062f"
                        },
                        {
                            "translit": "aseton",
                            "gloss": null,
                            "script": "\u0627\u0633\u062a\u0646"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 15,
                    "parent": 13,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "acid, acute, vinegar",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 16,
                    "parent": 12,
                    "lang": "Persian",
                    "refs": "HJB:3 ?",
                    "words": [
                        {
                            "translit": "\u00e2\u010d\u00e2r",
                            "gloss": "pickles",
                            "script": "\u0622\u0686\u0627\u0631"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 17,
                    "parent": 16,
                    "lang": "Hindustani",
                    "refs": "OXF:3",
                    "words": [
                        {
                            "translit": "achar",
                            "gloss": "pickles",
                            "script": null
                        }
                    ],
                    "note": null,
```


### [2026-09-04T19:01:11.082Z] TOOL RESULT

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


## [2026-09-04T19:01:15.355Z] TOOL CALL #9: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/ | head -30; echo ---; ls /home/sfmqrb/git/rishe/data/verification/page-*.json 2>/dev/null | head"
}
```


### [2026-09-04T19:01:15.407Z] TOOL RESULT

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
process
sources
---
/home/sfmqrb/git/rishe/data/verification/page-101.json
/home/sfmqrb/git/rishe/data/verification/page-126.json
/home/sfmqrb/git/rishe/data/verification/page-311.json
/home/sfmqrb/git/rishe/data/verification/page-31.json
/home/sfmqrb/git/rishe/data/verification/page-32.json
/home/sfmqrb/git/rishe/data/verification/page-33.json
/home/sfmqrb/git/rishe/data/verification/page-345.json
/home/sfmqrb/git/rishe/data/verification/page-34.json
/home/sfmqrb/git/rishe/data/verification/page-35.json
/home/sfmqrb/git/rishe/data/verification/page-36.json
```


## [2026-09-04T19:01:15.652Z] TOOL CALL #10: Bash

```json
{
 "command": "python3 -m json.tool /home/sfmqrb/git/rishe/data/extracted/batch/page-42.json | sed -n '400,520p'"
}
```


### [2026-09-04T19:01:17.493Z] TOOL RESULT

```
                    "note": null,
                    "quote": null
                },
                {
                    "id": 18,
                    "parent": 17,
                    "lang": "English",
                    "refs": "OXF:3",
                    "words": [
                        {
                            "translit": "achar",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 19,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "ak-j\u00f4",
                            "gloss": "sharp side",
                            "script": null
                        },
                        {
                            "translit": "ha-maraz",
                            "gloss": "sharp tool",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 20,
                    "parent": 19,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "edge",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "hammer",
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
}
```


## [2026-09-04T19:02:24.131Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: ak\" -A 12 POK_full.txt | head -80"
}
```


### [2026-09-04T19:02:24.193Z] TOOL RESULT

```
1731:From Root/ lemma: ang''(h)i-\ "snake, worm' derived Root/ lemma: ak^'a- {more properly 
1732-
1733-alci). ek"- 
1734-
1735-: "water, river'; Root/ lemma: eghero-: "lake, inner sea'; Root/ lemma: ad(u)-, ad-ro-\ 
1736-
1737-"water current': lllyrian Pannonian VN 'Oaspiareg [common alb.- 1 llyrian-Baltic -^^- >-«/-, - 
1738-
1739-z\ 
1740-
1741:From Root/ lemma: ak^a-^ water, river' nasalized in *a/r^e/7/- (suffixed in -er, -o/) derived 
1742-
1743-Root/ lemma: au(e)-9, aued-, auer-\ "to flow, to wet; water, etc' 
1744-
1745-Material: Avestan adu^ water run, brook, canal ', Venetic-lllyrian FIN Ad(d)ua {ior Po), 
1746-
1747-*AdulJa> Attel{\.o Danube in Bavaria), Mons ofAdula^ St. Gotthard ' (probably named after 
1748-
1749-the rivers streaming there), oberosterr. FIN *Adra> Attersee, Attergau, FIN Adrana> Eder 
1750-
1751-
1752-
1753-(Hessen), maybe also PN Aclria\v\ Venetien (afterwards mare Adriaticum), sizil. FIN 
--
3224:Root / lemma: akka 
3225-
3226-Meaning: "mother (children's speech)' 
3227-
3228-Material: Old Indie a/r/ra 'mother' (gram.), gr. Akku) " nurse of Demeter ', qkku) ' ghost ', 
3229-
3230-OKKi^saGai " be coy, position oneself stupidly ', Latin Acca Larentia ' Laren mother, Roman 
3231-
3232-hall goddess ' (probably Etruscan); also into Small-Asian languages; compare lapp. 
3233-
3234-Madder-akka'earih mother'. 
3235-
3236-Maybe alb. /4//ri//7a "great mother' in alb. epos. 
--
3820:Root/ lemma: ak*'a-{more properly ak^i). ek"- 
3821-
3822-Meaning: "water, river' 
3823-
3824-Note: 
3825-
3826:From Root/ lemma: ang''(h)i-\ "snake, worm' derived Root/ lemma: ak''a- {more properly 
3827-
3828-ak"^. ek"- 
3829-
3830-
3831-
3832-: "water, river'; Root / lemma: eghero-: "lake, inner sea'; Root/ lemma: ad(u)-, ad-ro-\ 
3833-
3834-"water current': lllyrian Pannonian VN 'Oa£piC(T£(; [common alb.- Illyrian -Baltic -^^- > -«/-, - 
3835-
3836-z\ 
3837-
3838-From Root/ lemma: a/ca-^yNster, river' nasalized in *a/r^e/7/- (suffixed in -er, -or) derived 
--
3903:Root / lemma: ak"- 
3904-
3905-Meaning: "to hurt' 
3906-
3907-Material: Old Indie aka m^ grief, pain ', Avestan ako^ nasty, bad ', axtis'^ grief, pain, 
3908-
3909-illness '; gr. noun *anap, *anv6(;, thereof nnavsT anopsT, nnavia anopia, nTT£pon£U(; 
3910-
3911-'swindler'; Verbalst. an- in anarn 'deception' {*apnta), redupl. Present ianru) 'damage'. 
3912-
3913-Note: common gr. -k"- > -p-, -g"- > -b- 
3914-
3915-References: Kuiper Gl. 21 , 282 f. 
--
7813:Both Root/ lemma: auei- [auei-?) {*hek''ei-): bird, *water bird : Root/ lemma: ak^a- {* a/cra): 
7814-
7815-ek"- : water, river, derived from zero grade of Root / lemma: ghag^h- : young of an animal 
7816-
7817-or bird; common gr. gh- > h-. 
7818-
7819-Material: Old Indie vih, vehm. 'bird' (Gen. veh, Akk. v/m), Avestan vis 6s. (G. PI. vayqm, 
7820-
```


## [2026-09-04T19:02:24.759Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=25 && NR<=31 {print \"=== leaf\",NR-1,\"===\"; print}' POK_01.txt | head -160"
}
```


### [2026-09-04T19:02:26.988Z] TOOL RESULT

```
=== leaf 24 ===
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
=== leaf 25 ===
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
=== leaf 26 ===
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
=== leaf 27 ===
�rfe;  höchster  Punkt,  Höhepunkt,  Ent- scheidungspunkt'(ax^(?jv  Adv.,  ax^ttatog,  dyt^dCo))  ]  schwed.  dial.  am  ,Sumpf- gras,  Cladium  mariscus'  (germ.  *ahma-^  vg\.  finn.  Lw.  ahma  ,equisetum').
ak-men-  j-mer-
Ai.  asman-  n.  ,Stein,  Himmel'  (als  Steingewölbe,  Reichelt  IF.  32,  23  ff.), asmard-  ,steinern',  av.  asman-  ,Stein,  Himmel'  (ai.  Gen.  dsnah,  Instr.  dsnäj av.  Gen.  asnö,  Abi.  asnäat  mit  -n-  aus  -m?2-;  Instr.  PI.  ai.  asnäih  nach den  o-St.);  phryg.  ON  ^^/.fxoyla',  gr.  IxKfxcov  ,Amboß',  U^lmv  b  ovgavög] lit.  äsmens  m.  PI.  ,Schneide',  akmud,  -eüs  m.  ,Stein'.
5.  Mit  12-Formantien :
aken-
Ai.   asdni-h  ,Pfeilspitze,    Geschoß';    av.   asdnga-,  apers.   ad-anga-   ,Stein'
2*
20  t
{*ak-en-go,  Benveniste  Orig.  28);  gr.  ^xatm  .Spitze,  Stachel;  Längenmaße (aber  über  lat.  acnna  s.  WH.  I  9),  d^övr}  .Wetzstein^  ^xwj^,  -ovTog  ,Wurf-  \ spieß'  (für  älteres  Utluv,  *-ovog  nach  den  Partizipien),  dAOvz'ilu)  .schleudre den  Wurfspieß^  ^'^avog  ,Distelart,  dorniger  PflanzenkopF,  d^aviteiv  .dornige Fruchtköpfe  tragen',  äy^avd-og  .Distel'  (aus  *dxav-(xv&og  ,Stachelblume'). Hytavd-a  .Distel.  Stachel.  Dorn.  Rückgrat,  bes.  der  Fische'.  &7ialav^ig  .Distel- fink' (aus  *äy,avOaXLg),  ä^ca&og  .Nachen'.  dy,drrp  dxdTiov  .Frauenschuh' \*aknto-,  wohl  von  der  spitzigen  Form);  lat.  agna  ,Ähre'  (aus  ^a/mä); got.  ahana  f.  .Spreu',  anord.  qgn,  ags.  egenu  f.  und  oegnan  PI.,  ahd. agana  ds..  nhd.  Ahne,  dial.  Agen  .Stengelsplitter  vom  Flachs  oder  Hanf (germ.  *ag-,  ^ahanö,  idg.  "^alcdnä)]  lit.  zem.  asnis  .Schneide,  aufkeimende Saat',  lett.  asns  m.  .hervorbrechender  Keim'.
6.  Mit  r-Formantien:  .
aker-,  oker- ■  Air.  a{i)clier  ,scharf'  (vom  Winde),  wegen  des  Gen.  Sg.  Akeras  (PN  im Ogham)  kein  lat.  Lw,;  abret.  acer-uission  ,mit  spitzen  Fingern'  (hlss), ocerou  PI.  .gespitzt',  acymr.  ar-ocrlon  gl.  atrocia;  lit.  a^erys,  eserys  .Fluß- barsch'; pol.  dial.  jesiora  (aus  *ase7-ä);  anord.  qgr  ds.  (aus  urgei-m.  *agura-, idg.  *okr-o-),  westnorw.  augur  (aus  *ggur7',  jüngere  Entwicklung  aus  Qgr), von-  auga  ,Auge'  beeinflußt.
Hierher  auch  vielleicht  der  Name  des  Ahorns  (wegen  der  spitzen  Blatt- abschnitte):
lat.  acer,  -eris  n.  .Ahorn'  (aus  acer  arhor  wurde  vlat.  acerabulus,  Meyer- Lübke  REW.  93).  dän.  xr  ds.  (germ.  *ahira-)\  nhd.  dial.  Aclier  ds.  (germ. *aliura-)]
^\\  U'/.aaiog'  fj  ocpevöaixvog  Hes.  {*äyxioGTog,  Bildung  wie  Ttlardvioiog neben  nXdravog]  zum  St.  vgl.  auch  H'AaQva'  ödcpvrj  Hes.);  gallo- rom.  *akaros, *akarnos  .Ahorn'  (Hubschmied  RC.  50,  263  f.);  ahd.  ahorn  , Ahorn'  (aus Schweiz,  und  anderen  Mundarten  wird  allerdings  ä-  erschlossen,  doch  wird das  ä-  ebenso  einer  volksetvmologischen  Entstellung  entspru
=== leaf 28 ===
ngen  sein, wie  mnd.  änhorn,  älliorn,  da  -liorn  als  2.  Kompositionsglied  aufgefaßt auch  die  1.  Silbe  Deuteleien  aussetzte);  ahorn  (idg.  *ak2'}io-)  ist  bis  auf die  Deklinationsklasse  =  ä^agra,  während  lat.  acernus  ,von  Ahorn'  aus *acer-inos  synkopiert  ist;  doch  ist  auch  das  n  ersterer  wohl  aus  dem Stoffadjektive  bildenden  Formans  -no-  und  nicht  aus  einem  r/n-St.  durch Häufung  beider  Elemente  erwachsen.
Eher  gilt   das   für  gr.  äxogva   (*-ia)  .gelbe   Distelart'  neben  äxavog  ds..
vielleicht  hierher  auch   IxxoQog  .Kalmus',   aytogov  .dessen  würzige  Wurzel'.
vgl.  mit  anderem  Formans   noch  ^mvog  f.  .wohlriechende   Blume',  djxi(xov
•  .^Basilienkraut'  (wenn  hierher  gehörig,  nach  dem  scharfen  Geruch  benannt?).
21
akri-,   akro-
Ai.  dsrih  ;,Ecke;  Kante^  Schneide^,  catur-asra-h  ^viereckig";  g'r.  äAQog spitz^;  ^'/-Qov,  ä-/.oa,  ^'Aoiq  ^Spitze^,  Berggipfel^  (auch  in  dyiQodouai.  als  ^scharfes Gehör  haben;,  das  Ohr  spitzen^;  and  ä/,olg,  -i(^o^  ^Heuschrecke^;  Kurzform für  d'AQoßarovaa  ;auf  den  Fußspitzen  gehend^^  d-^gi^ovaa;  d'Aosixcjv  ^Spitze des  Astes'',  s.  zur  Bildung  Brugmann  Grdr.  TP  1,  241);  lat.  (zum  a  s. Frisk  IF.  56,  113  f.)  äcer,  äcris,  -e  (alat.  äa-a^  -um)  ^scharf',  osk.  akrid acriter^,  umbr.  peracrl-  ^opimus^  (=  lat.  peräcer,  vgl.  zur  Bed.  gr.  ^v.qoq, autjh  ^oberst,  vortrefflich'^,  und  dy,}j,aLog),  lat.  acei-hus  ,herb,  sauer,  traurig^  (aus *-äcri-bho-s)',  vgl.  gall.  ÄXPOTÄLVS  ,init  hoher  Stirn^,  air.  er  ,hoch^  (aus *akros)]   lit.  asints,  astras,  alit.  astras,  aksl.  ostii>  ,scharf^  {t  Einschublaut).
okri-,  okro-
Mit  Abtönung  o-i  gr.  oy.Qig  f.  ,Spitze^  Bergspitze,  Ecke,  Kante^, alat.  ocris  m.  ,mons  confragosus^,  lat.  mediocrls  ,mittelmäßig',  eigentlich ,auf  halber  Höhe  befindlich^  (hier  könnte  Ablaut  im  Kompositum  wie in  extorris :  terra,  meditulliiim  :  tellüs  vorliegen),  Ocriculum,  Interocrea, ocrea  ,Beinschiene^,  umbr.  ocar,  ukar.  Gen.  ocrer  ,mons,  Burgberg^,  marr. ocres  ,montis^,  mir.  och{a)ir  ,Ecke,  Rand^,  daraus  entlehnt  cymr.  ochr ,Rand^
Zum  heteroklitischen  Paradigma  *ak-r-(g),  *ak-ri-es  (auch  der  i-St.  *akt- kann  sich  damit  verbunden  haben)  vgl.  oben  akmenjmer-,  Pedersen  KZ.  32, 247,  Johansson  Beitr.  9,  Petersson  IF.  24,  269  ff. ;  als  beachtenswert  er- scheint mir  davon  die  Anreihung  von  gv.  Kody-og  ,Name  verschiedener Berge^,    '^y.ody-ag    ,Agrigentum^,    die    ursprüngl.    ,Fels^    bedeutet    haben
7.  Mit  s-Formantien:
akes- :  aks-
Gr.  ä'x»'^  ,Spr
=== leaf 29 ===
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
=== leaf 30 ===
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
```


## [2026-09-04T19:02:47.494Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ak-\" -A 40 AHD_watkins1985.txt | head -70"
}
```


### [2026-09-04T19:02:47.547Z] TOOL RESULT

```
275:ak-. Sharp. 1. Suffixed form *ak-yd- in: a. Germanic *akjo in Old English ecg, sharp side: EDGE; b. Germanic *akjan in Old Norse eggja, to incite, goad: EGG?. 2. Suf- fixed form *ak-u- in: a. Germanic *ahuz in Old English éar, zr, zhher, spike, ear of grain: EAR?; ACROSPIRE; b. Latin acus, needle: ACICULA, (ACUITY), ACUMEN, ACUTE, AGLET, EGLANTINE. 3. Suffixed form *ak-men, stone, sharp stone used as a tool, with metathetic variant *ka-men, with variants: a. *ka-mer- in Germanic *hama- raz in Old English hamor, hammer: HAMMER; b. *ke- men- (probable variant) in Germanic *himin-, in dissimi- lated form *hibin-, “the stony vault of heaven,” in Old English heofon, hefn, heaven: HEAVEN. 4. Suffixed form *ak-ond- in Germanic *agan6d in Old Norse dgn, chaff: awn. 5. Suffixed lengthened form *dk-ri- in Latin dcer, sharp, bitter: ACERATE, ACRID, ACRIMONY, EAGER}; CAR- VACROL, VINEGAR. 6. Suffixed form *ak-ri-bhwo- in Latin acerbus, bitter, sharp, tart: ACERB; EXACERBATE. 7. Suffixed (stative) form *ak-é- in Latin acére, to be sharp: ACID. 8. Suffixed form *ak-éto- in Latin acétum, vinegar: ACETABULUM, (ACETIC), ACETUM; ESTER. 9. Greek akantha (second element of Mediterranean origin), thorn, thorny plant: ACANTHO-, ACANTHUS; COELACANTH, PYRACANTHA, TRAGACANTH. 10. Suffixed form *ak-md- in Greek akmé, point: ACME, ACNE. 11. Suffixed form *ak-ro- in Greek akros, topmost: ACRO-; (ACROBAT), ACROMION. 12. Variant suffixed form *ok-su- in Greek oxus, sharp, sour: AMPHIOXUS, OXALIS, OXYGEN, OXYURIASIS, PAROXYSM. [Pok. 2. ak- 18, 3. kem- 556.]
276-aks-. Axis. 1. Suffixed form *aks-lo- in Old Norse éxull, axle: AXLE. 2. Suffixed form *aks-i- in: a. Latin axis, axle, pivot: axis; b. Latin diminutive axilla, armpit (< “axis point of the arm and shoulder”): AXILLA. 3. Suf- fixed form *aks-ld- in Latin dla (< *axla), wing, upper arm (see axilla in 2. b. for semantic transition): AISLE, ALA, ALAR, ALARY, ALATE, ALULA; ALIFORM. 4, Suffixed form *aks-on- in Greek ax6n, axis: AKON; MONAXON. [In Pok. ag- 4.]
277-akwa-. Water. 1. Germanic *agwjd becoming *auj6, “thing on the water,” in Old English ig, ieg, island, and
278-al-'
279-igland, iegland (land, land; see lendh-2), island: ISLAND. 2. Latin aqua, water: AQUA, AQUARELLE, AQUARIUM, AQUATIC, AQUI-, EWER, GOUACHE; SEWER!. [Pok. akva 23.
280-al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
281-ang"hi-
282-b. Old Norse um/(b), about, around: OMBUDSMAN; c. Old High German umbi, around: UMLAUT. 3. Latin ambi-, around, about: AMBI-. 4. Greek amphi, around, about: AMPHI-. 5. Celtic *ambi (see ag-). [Pok. ambhi 34.] ambhé. Both. 1. Reduced form *bAd in Germanic *b6-, *bé in Old Norse bdthir, both: BOTH. 2. Latin ambé, both: AMBSACE. 3. Greek amphé, both: AMPHOTERIC. [In Pok. ambhi 34.] amer-. Day. Suffixed form “Gmer-d in Greek hémera, day: EPHEMERAL, HEMERALOPIA. [Pok. dmer- 35.] ames-. Blackbird. 1. Suffixed variant form *ams-ol- in Old English dsle, blackbird: ouzEL. 2. Suffixed variant forms *mes-old, *mes-olo- in Latin merula, merulus, merle, blackbird: MERLE, MERLON. [Pok. ames- 35.] [amma. Various nursery words. Latin root. 1. Medieval Latin amma, mother: AMAH. 2. Reduced form *am- in: a. Latin amare, to love: AMATEUR, AMATIVE, AMATORY, AMORETTO, AMOUR; ENAMOR, INAMORATA, PARAMOUR; b. Latin amita, aunt: AUNT; c. Latin amicus, friend: AMICABLE, AMIGO, AMITY; ENEMY, INIMICAL.] an’. On. Extended form *ana. 1. Germanic *ana, ané in: a. Old English an, on, a, on: ON; b. Old Norse 4, in, on: ALOFT; ¢. Old High German ana (> Middle High Ger- man ane), on: ANLAGE; d. Middle Dutch aan, on: ON- SLAUGHT. 2. Greek ana, on, up, at the rate of: ANA?, ANA-. [Pok. 4. an 39.] an?, Demonstrative particle. Suffixed form “*an-tero-, “other (of two)” (compare *al-tero- under al-') in Ger- manic *antharaz in Old English 6ther, other: OTHER. [Pok. 2. an 37.] an-', Old woman, ancestor (nursery word). Latin anus, old woman: ANILE. [Pok. 1. an- 36.] an-2. To pour, draw water. Suffixed form *an-tlo- in Greek antlos, bilge water, bucket: ANTLIA. [In Pok. 1. sem- 901.] andh-. Bloom. Suffixed form *andh-es- in Greek anthos, flower: ANTHEMION, ANTHER, ANTHESIS, ANTHO-, -AN- THOUS; AGAPANTHUS, CHRYSANTHEMUM, DIANTHUS, EX- ANTHEMA, HYDRANTH, (MONANTHOUS), STROPHANTHIN. [Pok. andh- 40.] andho-. Blind, dark. Suffixed variant form *ondh-ro- perhaps in Latin umbra, shadow: UMBEL, UMBRA, UM- BRELLA; ADUMBRATE. [Pok. andho- 41.] ane-. To breathe. Suffixed form *ana-mo- in: a. Latin animus, reason, mind, and anima, soul, spirit, life, breath: ANIMA, ANIMADVERT, ANIMAL, ANIMATE, (ANI- MATO), ANIMISM, ANIMOSITY, ANIMUS; EQUANIMITY, LONGANIMITY, MAGNANIMOUS, PUSILLANIMOUS, UNANI- mous; b. Greek anemos, wind: ANEMO-. [Pok. 3. an(9)- 38.] anata. Doorjamb. Latin antae (plural), a pair of pillars on the opposite sides of a door: ANTA. [Pok. anatd- 42.] [angelos. Messenger. Greek noun, akin to Greek anga- ros, mounted courier, both from an unknown Oriental source. 1. Greek angelos, messenger: ANGEL, (ANGELIC), ANGELICA, (ANGELUS); ARCHANGEL, EVANGEL. 2. Greek angaros, mounted courier: ANGARY.] angh-. Tight, painfully constricted, painful. 1. Germanic *ang-, compressed, hard, painful, in Old English ang- nzgl, “painful spike (in the flesh),” corn, excrescence (nzgl, spike; see nogh-): AGNAIL. 2. Suffixed form *angh-os- in Germanic *angaz in Old Norse angr, sor- row, grief: ANGER. 3. Suffixed form *angh-os-ti- in Ger- manic *angusti- in Old High German angust (> German Angst), anxiety: ANGST. 4. Latin angere, to strangle, draw tight: ANxious. 5. Suffixed form *angh-os-to- in Latin angustus, narrow: ANGUISH. 6. Greek ankhein, to squeeze, embrace: QUINSY. 7. Greek ankhoné, a stran- gling: ANGINA. [Pok. angh- 42.] angvhi-. Snake, eel. 1. Latin anguis, snake: ANGUINE; ANGUILLIFORM. 2. Taboo deformation or separate root *ogvhi- in Greek ophis, snake, serpent: OPHIDIAN, OPHITE; OPHIOLOGY, OPHIUCHUS. 3. Taboo deformation or separate root *eghi- in Greek ekhis, snake, in deriva-
283-ank-
284-tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
285-POSTICHE, POSTURE, PREPOSITION, PROPOSE, PROVOST, REPOSIT, SUPPOSE. [Pok. apo- 53.]
286-apsa. Aspen. Germanic aspdn- in Old English zxspe, aspen: ASPEN. [Pok. apsd 55.]
287-ar-. Also are-. To fit together. I. Basic form *are-. 1. Suf- fixed form *ar(g)-mo- in: a. Germanic armaz in Old English earm, arm: ARM}; b. Latin arma, tools, arms: ARM?2, ARMADA, ARMADILLO, ARMATURE, ARMOIRE, ARMY; ALARM, DISARM; C. Latin armus, upper arm: ARMILLARY SPHERE. 2. Suffixed form *ar(e)-smo- in Greek harmos, joint, shoulder: HARMONY. 3. Suffixed form *ar()-ti- in: a. Latin ars (stem art-), art, skill, craft: ART!, ARTEL, ARTISAN, ARTIST; INERT, (INERTIA); b. fur- ther suffixed form ‘*ar()-ti-o- in Greek artios, fitting, even: ARTIODACTYL. 4, Suffixed form *ar()-tu- in Latin artus, joint: ARTICLE. 5. Suffixed form *ar()-to- in Latin artus, tight: COARCTATE. 6. Suffixed form “*ar(e)-dhro- in Greek arthron, joint: ARTHRO-; ANARTHROUS, DIAR- THROSIS, ENARTHROSIS, SYNARTHROSIS. 7. Suffixed (su- perlative) form *ar(g)-isto- in Greek aristos, best: ARISTOCRACY. II. Possibly suffixed variant form (or separate root) *dr-dh-. 1. Latin drdé, order (originally a row of threads in a loom): ORDAIN, ORDER, ORDINAL, ORDINANCE, ORDINARY, ORDINATE, ORDO; COORDINA- TION, INORDINATE, SUBORDINATE. 2. Latin drdiri, to begin to weave: EXORDIUM, PRIMORDIAL. 3. Latin or- ndre, to adorn: ORNAMENT, ORNATE; ADORN, SUBORN. III. Variant or separate root *ré- (< *reo-). 1. Latin réri (past participle ratus), to consider, confirm, ratify: RATE!, RATIO, REASON; (ARRAIGN). 2. Suffixed form ré-dh- in: a. Germanic *rédan in (i) Old English rédan, to advise: READ, REDE (ii) Old English réden, condition: HATRED, KINDRED; b. Germanic *rédaz in (i) Old High German rat (> German Rat), counsel: BUNDESRAT, RATHSKELLER (ii) Old English rédels(e), opinion, riddle: RIDDLE?. 3. Zero-grade form *ra- in Germanic *radam, number (see dekm). IV. Variant (or separate root) *ri-. 1. Suffixed form *ri-tu- in Latin ritus, rite, custom, usage: RITE. 2. Suffixed form *(a)ri-dhmo- in Greek arithmos, number, amount: ARITHMETIC, LOGARITHM. [Pok. 1. ar- 55.]
288-arek-. To hold, contain, guard. Variant *ark-. 1. Latin arca, chest, box: ARCANE, ARK. 2. Latin arcére, to en- close, confine, contain, ward off: COERCE, EXERCISE. 3. Greek arkein, to ward off, suffice: AUTARKY. [Pok. areq- 65.]
289-are-. To plow. Latin ardre, to plow: ARABLE. [Pok. ar(a)- 62.]
290-arg-. To shine; white; the shining or white metal, silver. 1. Suffixed form *arg-ent- in Latin argentum, silver: ARGENT, ARGENTINE. 2. Suffixed form “arg-i-U/l)- in Greek argillos, white clay: ARGIL. 3. Suffixed form *arg- u-ro- in Greek arguros, silver: LITHARGE, PYRARGYRITE. 4. Suffixed form *arg-i-n- in Greek arginoeis, brilliant, bright-shining: ARGININE. 5. Extended form “argu-, brilliance, clarity, in Latin denominative arguere, to make clear, demonstrate: ARGUE. 6. Suffixed form *arg- ro- in Greek argos (< *argros), white (see pel-2). [Pok. ar(e)g- 64.]
291-[arkhein. To begin, rule, command. Greek verb of un- known origin; with derivatives arkhé, rule, beginning, and arkhos, ruler. (ARCH-), -ARCH, ARCHAEO-, ARCHAIC, ARCHI-, ARCHIVES, ARCHON, (-ARCHY); AUTARCHY, EXARCH, MENARCHE.]
292-arku-. Bow and arrow (uncertain which, perhaps both as a unit). 1. Germanic *arhwo in Old English ar(e)we, earh, and Old Norse *arw-, arrow: ARROW. 2. Latin arcus, bow: ARC, ARCADE, ARCH!, ARCHER; ARBALEST, ARCHI- VOLT, (ARCIFORM), ARCUATE. [Pok. arqu- 67.]
293-aryo-. Lord, ruler; self-designation of the Indo-Iranians and perhaps of the Indo-Europeans. Lengthened-grade form *dryo- in Sanskrit drya-, noble, Aryan: ARYAN. [Pok. arjo- 67.]
294-as-. To burn, glow. 1. Extended form *asg- in Germanic
295-asinus
296-*askon- in Old English zsce, asce, ash: ASH!. 2. Suffixed form *ds-d- in Latin Gra, altar, hearth: Ara. 3. Suffixed (stative) form *ds-é- in: a. Latin Grére, to be dry, hence dridus, dry, parched: ARID; b. Latin ardére, to burn, be on fire, from dridus, parched: ARDENT, ARDOR, ARSON. 4. Extended form *asd- in: a. Greek azein, to dry: ZAMIA; b. Greek azaleos, dry: AZALEA. [Pok. as- 68.]
297-[asinus. Ass. Latin noun, akin to Greek onos, probably ultimately from the same source as Sumerian anée. 1. Latin asinus, ass: ASININE, EASEL. 2. Greek onos, ass: ONAGER.]
298-at-. To go; with Germanic and Latin derivatives meaning a year (conceived as “the period gone through, the revolving year”). Suffixed form *at-no- in Latin annus, year: ANNALS, ANNUAL, ANNUITY; ANNIVERSARY, BIEN- NIUM, DECENNIUM, MILLENNIUM, OCTENNIAL, PEREN- NIAL, QUADRENNIUM, QUINDECENNIAL, QUINQUENNIUM, SEPTENNIAL, SEXENNIAL, SUPERANNUATED, TRIENNIUM, VICENNIAL. [Pok. at- 69.]
299-ater-. Fire. 1. Suffixed zero-grade form *dér-o- in Latin ater (feminine dtra), black (< “blackened by fire’): ATRABILIOUS. 2. Suffixed zero-grade form *dér-yo- in Latin dtrium, forecourt, hall, atrium (perhaps originally the place where the smoke from the hearth escaped through a hole in the roof): ATRIUM. 3. Compound shortened zero-grade form “atro-akv- (*ok¥-, “-looking”; see ok"-) in Latin dtréx, “black-looking,” frightful: aTRocIOUvS. [Pok. die)r- 69.]
300-[athal-. Race, family. Germanic root, possibly related to Greek atallein, to foster. 1. Germanic *athal- in Old English ztheling, prince: ATHELING. 2, Variant Germanic *6thel- in Old High German edili, noble: EDELWEIss. [In Pok. atos 71.]]
301-atto-. Father (nursery word). Possibly Latin atta, father: ATAVISM. [In Pok. atos 71.]
302-au-', To stay the night, dwell. Suffixed form *au-/d- in Greek aulé, court, dwelling: autic. [Pok. 2. au- 72.]
303-au-?. Pronominal base appearing in particles and adverbs. Suffixed form *au-ge in Germanic ‘*auke in Old English éac, éc, also: EKE?. [Pok. 4. au- 73.]
304-au-3, Off, away. 1. Old Russian u-, away, in Russian ukazat’, to order: UKASE. 2. Sanskrit ava, off, down: AvaTAR. [Pok. 3. au- 72.]
305-au-‘4, To weave. Extended form *wedh- (< *awedh-). 1. Germanic *wédiz in Old English wed, wéde, garment, cloth: WEED?, 2. Germanic *wadlaz in Old English watel, watul, wattle: WATTLE. [Pok. 5. au- 75.]
306-au-5, To perceive. Compound forms *aw-dh-, *awis-dh-, “to place perception” (see dhé-'). 1. Suffixed form *awisdh-yo- or *awdh-yo- in Latin audire, to hear: AUDIBLE, AUDIENCE, AUDIENT, AUDILE, AUDING, AUDIO-, AUDIT, AUDITOR, AUDITORIUM, AUDITORY, OYEZ; OBEY, SUBAUDITION. 2. Greek aisthanesthai, to feel: AES- THETIC; ANESTHESIA. [Pok. 8. au- 78.]
307-aug-'. To increase. Variant *(a)weg- (< *aweg-). 1. Ger- manic *aukan in: a. Old English éacan, écan, to increase: EKE!; b. Old English éaca, an addition: NICKNAME. 2. Variant extended forms *wogs-, *wegs- in Germanic *wahsan in Old English weaxan, to grow: WAX. 3. Form *aug-é- in: Latin augére, to increase: AUCTION, AUGEND, AUGMENT, AUTHOR, (AUTHORIZE), (OCTROI). 4. Latin augur, diviner (< “he who obtains favorable presage” < “divine favor, increase”): AUGUR; INAUGURATE. 5. Latin augustus, majestic, august: AUGUST. 6. Suffixed form *aug-s- in: a. Latin auxilium, aid, support, assistance: AUXILIARY; b. Greek auxein, to increase: AUXIN; ¢. Greek auxanein, to increase: AUXESIS. [Pok. aweg- 84.]
308-aug-?. To shine. Suffixed form *aug-d- in Greek augé,
309-light, ray: AUGITE. [Pok. aug- 87.]
310-aukv-, Cooking pot. 1. Germanic suffixed form *uhw-na- in *ufna- in Old English ofen, furnace, oven: OVEN. 2. Suffixed form *auk-sld- in Latin aulla, aula, olla, pot,
311-jar: OLLA. [Pok. aug(h)- 88.]
312-aulo-. Hole, cavity. 1. Metathetic form *alwo- in Latin
313-bat-
314-alvus, the belly, stomach: ALVEOLUuS. 2. Greek aulos, pipe, flute, hollow tube: CAROL, HYDRAULIC. [Pok. au- lo-s 88.]
315-[aurum. Gold. Latin noun with preform *aus-o- probably from a root *aus-. Latin aurum (> French or), gold: AUREATE, AUREOLE, AURIC; AURIFEROUS, DORY?, EYRIR, OR’, ORE, ORIFLAMME, ORIOLE, ORMOLU, OROIDE, OR- PHREY, ORPIMENT.]
```


## [2026-09-04T19:02:49.087Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aθanga\\|athanga\\|a0anga\\|aOanga\" KNT.txt | head -20; echo \"=== asman\"; grep -n \"asman\\|asan-\" KNT.txt | head -20"
}
```


### [2026-09-04T19:02:49.159Z] TOOL RESULT

```
=== asman
397:asan- ‘stone’, with s from Ё.
902:*akmon-, OP acc. asmanam, Skt. dimanam, ОК. nom. &xpov ‘anvil’.
1118:thus the pAr. *aratn- aratan- gave Av. dual arana, but OP arašn- and (with extension of the $) arasan- ‘cubit’, in inst. pl. arašaniš (see
1152:asan- "stone! with Med. s, in nom. asd, and
1153:possibly in Asa-garta- (see Lex. s.v.). Cf. also aec. asmdnam ‘sky’, Av. asman- ‘sky, stone’,
1222:(with Med. s) asan- ‘stone’, $87. pIE *ghem- in Lith. Zémé ‘earth’, Lt. humus, but
1826:-ga- in аба"-да-, cf. asan-.
4443:2 dà : hv& : avam : asmanam : ada
4952:abaga- (ie. аба"да-) sb. ‘stone’: Av. asanga-, NPers. säng, cf. OP asan-, asman- (S87, S151, $155.1); see also a(againa-. afagam asm. DSf 24, 48.
5113:Asagarta- sb. ‘Sagartia’, a northwestern prov- ince of the Persian Empire (§29.n2, $81): Elam. ad]. a&-Sa-kar-tt-a, Akk. adj. sa-ga-ar-ta-a-a, Gk. Yayapria. Probably asan- ‘stone’ (with Med. s < pIE Ё; $9.1, 587) + *garta- ‘cave’ (Skt. gdria-), ‘Land of Stone-Cave Dwellers’ ($161.10, §166.1; Bthl. AiW 207, zAiW 119-20); hardly asa- ‘horse’ (with OP s < plE ky, §90) + *garta- ‘wagon’ (Skt. gária-), ‘Land of Horse-drawn Wagons’. See also Asagartiya-. Asagartansm. DPe 15. Asagartam asm. DB 4.23. Asagartaty lsm. DB 2.80f; 4.22; DBg 8f.
5117:asan- sb. ‘stone’: plE *aken- (§9.V, $87, §155.1), ef. asman-. See also Asagaria-. ай (8124.5, $187) nsm. DSf 40f; but see also under daru-.
5122:asman- sb. ‘sky’: Av. asman-, Skt. áéman-, Gk. йкроу ‘anvil’, Lith. akmud ‘stone’, pIE *akmen- /mon- (§95, 5155.11); for variant meanings, cf. Reichelt, ТЕ 82.28-57; for lranian ideas of its cre- ation, ef. Bailey, Zoroastrian Problems 120-48. Not dsman-, despite NPers. dsmén, which has length of later origin (Debrunner, IF 52.153, against Bv. Gr. $175). See also asan-, абаја-. asmünam asm. (§67.II, $124.6, $187) DNa 2f; DSe 2f; DSf 2; DSt 2f; DZc 1; DE 3f; XPa 2; XPb 3f; ХРе 2; XPd 3; XPE 2f; XPh 2; XE 4; XV 3; A'Pa 3°; A?He 3. asmanam (853) A?Pa 3.
5382:speak’, derivatives cdksas- cakşu- cakgus- caksan-, and Ау. čašman-, Phi. NPers. čašm ‘eye’; initial u- of ucasma is an error (Bv. TPS 1945.53-4, quoting Jn. IF 25.182). The stem is caSa-, not caKman- (Kent, Lg. 19.225-6), since the nom.-acc. of nt. casman- would be cašmā and not ca$ma. Cf. $102, $143.I, $187.n1l. Attempts to explain the erroneous u- of ucaima, Wb. ZDMG 61.726; Wackernagel, KZ 61.205-8. саат asn. DB 2.75, 89 (Cameron found ст“ legible in 89, but only the final me in 75); caSa{m} (case and form uncer- tain) DSq 2.
```


## [2026-09-04T19:03:02.542Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\n# map line number -> leaf\nimport re\nleaf=0\nfor i,l in enumerate(lines,1):\n    if '\\f' in l: pass\n# instead: compute char offsets\noffs=[]\npos=0\nfor i,l in enumerate(lines,1):\n    offs.append(pos); pos+=len(l)+1\nff=[m.start() for m in re.finditer('\\f',data)]\ndef leafof(ln):\n    p=offs[ln-1]\n    import bisect\n    return bisect.bisect_right(ff,p)\nfor ln in [397,902,1152,4952,5113,5117,5122]:\n    print(ln, 'leaf',leafof(ln), 'printed~', leafof(ln)-15)\nEOF"
}
```


## [2026-09-04T19:03:03.209Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==182 || NR==189 {print \"=== leaf\", NR-1, \"===\"; print substr($0,1,600)}' KNT.txt"
}
```


### [2026-09-04T19:03:04.092Z] TOOL RESULT

```
397 leaf 20 printed~ 5
902 leaf 39 printed~ 24
1152 leaf 47 printed~ 32
4952 leaf 187 printed~ 172
5113 leaf 195 printed~ 180
5117 leaf 195 printed~ 180
5122 leaf 195 printed~ 180
```


### [2026-09-04T19:03:07.448Z] TOOL RESULT

```
=== leaf 181 ===
sed him, him- self becoming now king in Parsua, later called Ратѕа. Arsames, however, was not put to death, but (as the OP inscriptions tell us) lived on until after his grandson Darius got the throne of the Persian Empire. Thus Hystaspes never was king, and is not counted among the nine Achaemenian kings. Cyrus II thereafter conquered Media and added it to his dominions, and then extended his conquests in all directions. But he did belong by ancestry to the Achaemenian line; one can hardly brand him as a rank outsider.
Possibly Ctesias’ story, as repeated by Nicolaus Damascenus, origin
=== leaf 188 ===
’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadtya- ‘truth’, with late loss of h-, + deriv. of d-baud- ‘be fragrant’, cf. Av. baoót- ‘fra-
OLD PERSIAN
grance’, therefore ‘having the fragrance of the truth’).  <Aé@iydbausinahya gsm. Sa 4-7.
Aéura sb. ‘Assyria (and Syria)’, a province of the Persian Empire ($6, $106.11): Elam. aš- &i-ra, АКК. áš-šur, Gk. 'Аттурв‚ but Aram. абиг. Aéuré nsf. DB 1.14f; 2.7; DPe 11; DNa 26f; DSe 26°; DSm 7°; XPh 22. Aéurayd lsf. (5186) DB 2.58f.
A@uriya- adj. ‘Assyrian’: deriv. to preceding .
($144.
```


## [2026-09-04T19:03:15.733Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 186 187 188 194 195 196; do echo \"--- leaf $((n-1)) ---\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N {print}' KNT.txt | grep -oE '^[^A-Za-z]*[0-9]{3}|LEXICON|OLD PERSIAN|[0-9]{3}[^0-9]{0,3}$' | head -5; done"
}
```


### [2026-09-04T19:03:17.367Z] TOOL RESULT

```
--- leaf 185 ---
164
LEXICON
199.
368,
$388
--- leaf 186 ---
117).
LEXICON
311.
165
--- leaf 187 ---
166
103).
--- leaf 193 ---
LEXICON
171
881).
--- leaf 194 ---
172
200.
OLD PERSIAN
--- leaf 195 ---
LEXICON
792.
730.
173
```


## [2026-09-04T19:03:28.878Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"a0againa\\|aθagaina\\|aOagaina\" KNT.txt | head; echo \"=== BRT 208 area\"; grep -n \"asenga\\|asanga\\|as[əe]nga\" BRT.txt | head -20"
}
```


### [2026-09-04T19:03:28.944Z] TOOL RESULT

```
=== BRT 208 area
```


## [2026-09-04T19:03:29.515Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Mühlstein\\|asan- \\|asman-\" BRT.txt | head -30"
}
```


### [2026-09-04T19:03:29.566Z] TOOL RESULT

```
4698:\)amm  Y.$4.2,  G,  j.6; — yä  {ar?ävi) 'vaiti fratalaili  Y.  Ö5. 3 ;  Yt.  5. 1 5 ;  —  a^tn  vatau- hlm  .  .  hrpsailTm  'vattTm  Y.  3. 14;  Yt /J. I,  7;  —  drvaspqm  . .  'vaitlm  YL9.2;  — fravaiayö  .  .  yä  'vaifli  Yt  13.  29;  —  at töi  atrjm  . .  *asXsttin  'vanhm  Y.j^4;  — tiiirim  .  .  'vant?m  YtÄ4;  —  vatianttm 'vant»m  Yt  21.  i;  —  °vatS  amai  'vatÖ virp^raynäi  'vat^yO.  »rütyi  'vai'iya aiöii  'vai^ya  astdil  'vaüyä  paurvatälo 'vai'i'yB  uparatälö  'va^byä  yazatoAbyö  Vr. g.i,.  b)  sonst;  uströ . ,  b)r?zB  "vä  Yt i.^.  1 2 ;  —  srlra  urusta  'vaiti  (VSf.)  .  . UfTaireY.it^.iB,Vyt22; — srayarfhö  vouru- ka?ahe  'vatö  Yt.<S.46;  —  vasnm..  zaröil ayanhö  frahixt»m  'vatö  \L  10.96;  —  'vat iimäfum  Y.  57. 10;  —  ptiüm . .  yim  aiwatö 'vantim  Vyt.^;  —  'vaitlm  sitiqin  dävöi (sd.)  dr»gvasa  Y.  44. 14.  —  IstJm  . .  pouru.- sarioam  'vaitlm  Y.  65. 1 1 ;  —  hazö  "vat  Y. jj^.  iz;  —  yahmi  maza  'va  (NSn.l')J' '  iiiäälpm  Yt  10. 64  (?) ;  —  *°vata  vaca  F.3  e. AbleiL  —  ai.  dmm-ant-  Adj.;  vgl.  mp.  (PS.) amäz-nnd.  —  ')  %  jg4.  —  •)  Zur  Zusammen- Stellung  von  amai'aaf-  mit  ^'/ri^ravan ,  viri- %rasan-  s.  'amn-  2.-3)  Wenn  richtig,  wohl Neubildung  lum  NSm.  'va  nach  der  n-Dekt.
5024:•  j.  ava.Jasan-  Adj.  "her-,  hinzukommend, gehend  zu  — '  (mit  a  und  Akk):  yasca.. frS.vS  iüsa  (NS.)  haca  daiähaot  °sa  dahyUm ä  Yt/.i?.
5724:•  j-t  E-  (.  P-)  asan-iaj«-,  j.,  p.  asman-  m." i)  'Stein':  *ja«s(alsAP.)  äi/i{sd.)  maya  äiti darSii"V.g.  11;  —  'sSnaShia'^ ..  vtHiaeh-a' . .  tBiuxha  (sd.)  V,  6. 5 1,  a)  als  Amulet: °samm  *siyaire.ci^rim  (sd.)  abars  *aAurö.- puirS  (sd.)  Yl;4.59-  b)  als  Waffe, 'Schleuderstein,  Steingeschoss':  Uavasca  . . •sanas(a  . .  (NP.)  fraäaxlaitya  V.  Z7.9;  — karjtS  .  .  vazrö .  .  'sänS  atymSJütä  Yt.  JJ. 72;  /.18;  —  jainti  mqm  ahuna  vairya avavata  snai^isa  ya'^a  'sma  iatS.masa (sd.)  Yt/7.20;  —  'sanS  (als  AP.)  tasia drazimnS  katä-masatiks  Aynti  V,  117.43); —  yahmai  .  .  aurvan/a  *yuxta  vJsa %an/asante  (sd.)  .  .  asUnas/a  (als  AP.) vispeMvia  "dem  .  .  die  Renner  am  ge- schirrten Wagen   ziehen  -  .  und  die  all-
5746:j.  asfnga-,  p.  a^a'ga-  m.  'Stein">. KompA.;  Abtrat.  —  Vgl.  np.  mult-äsaiii;,  mp., np.  lanf.  —  VgL  auch  asman-.  —  1)  Im  Iran, muss  äi',  as'  und  1'  vorhanden  gewesen  sein, E.  dRn.  np.  niiist-äiang,  j.  asingS',  mp.  sangi vgl.  zum  Ablaut  gr.  üap,  iap  und  Ut.  sniii;iiis; Bthl.  IF.  a.  z68;  Hbm.  PSt.  76.  Das  p.  Wort kann  auch  ä%'  gelesen  werden. j.  as«ngö.gav-  Adj.  'mit  Händen  aus
5907:•  j.,  p.  asman-  m.:  s.  unter  asan-.
5909:Ableit.  aus  asman-.  —  Pü.:  asimni  'silbern'i durch   den  Anklang   veranlasst;    falsch  DST.
8068:•  j.  iSva.vasman-  n.  'Pfeilflug':  hö  aci'v . .  °sma  apayeiti  .  .  yatcit  vazaite  hvashm "er  alleinholt  denPfeilflug  ein..;  auch  wenn er  guigeschossen  dahinfliegt"  Yt,  14.  20.
9136:•  j.  kava'rasman-  m.  F.N.  eines  Cliiubigen : -«Hj''  «.tiiö«,- Vt.  ij.103.
10145:dem,  was  das  Rind  liefert;  i) 'Fell,  Haut':  ahurai  a  mS  urva  'Suscit  azya  Y.2g. mä  .  ,  yaia  *'aof  drafsö  (sd.)  .  .  Y.  /o.  1  5  '3>.  a)  neben  'gaya-  (sd.):  nimS  °Sus 14.  2)Tleisch':  pars xh'isca{sd.)  5zBi-\  mmö  gayehe  Y.68.  22;  Vr.  z/.  a;  —  fra tisca'jus  matY.13.%9,;  —  nöii  payS  fsula  .vasayS  ..  yqmca  asnö  ..  spu  ..  zsmS (sd.)  nSii  'Jul  .  .  paiti.baire  V.  7.  77;  —  I .  .  un-arayd  .  .  -Jus  .  .  gayeke  Vl  13. kat  na  .  .  -Jus'  ataifya  (sd.)    aslryeiti  N. '  86.  a)    GS.    mit  tasan-  m.  (sd.,   auch
12160:.  j.,  g.  tasan-  m.  'Büdner,  Schöpfer',  nur'*  g-  *^s  ä  adv.-artige  Verb,  'auf  solche
13692:äsnaila  zbayantsi  'ratca  Yt.  77.  * ;  ■ — ■  nara . .  ya  nasaum  avaJiUta  'ire  asahi  rasan- hqm  (sd.)  V.Ä'.g?;  YX.i4.^l\  —  Wp^r- sahyü  .  .  ari'tii  'raiy'''  paragmatä  "des Persers  Speer  ist  fernhin  gekommen"  D. ff.  4;  —  mit  Abi:  agibyS  'in  voha  as mand  (sd.)  Y.J4.  8.  a)  |  in  Verbindung mit  apiy  (sd.):  ahyäyä  bümiya  'raiapiy  D. 6.3;  X.I.3  (wo  'raiy  apty): —  mit  Aacä und  Abi.:  pSrs<^  marliytr  *'rayapiy''> hacä  pärsS^  kamaram  paliyajatä  D.  6. 4.  2)  Abis,  'von   fem;  fem;    femhin,
16493:•  j.  baevar«.spasan-  Adj.  'der  zehn- tausend Späher,  Wächter  hat',  von  Mikra: mi%rs  .  .  yS  'sanS  (NS,)"'  Yt  to.  24;  — mi^rB  .  .  yS  'sänö  (NS.)"  Yt  10.  60.
16982:barasman-  Noten
16984:•  j.  barasman-  n^  meist  kollekt  Sing., Bezeichnung  eines  beim  Gottesdienst  ge- brauchten ZweigbUndeIs*':*Äa/a  nä  *mbma 'tnana   ratufrisi  %rilurvara  (sd.)  N.fjo;
20116:•  j,  'masan-  n.  'Grösse,  Eedeutendheit': "sanaca  (IS.)  vatvhanaca  srayanaca  (sd.) V.J.  22,  Yt/p.  sS,  K.i.\z,  H.J.6,  2.  II, *P.  42.  a)  Plur. 'Glosstaten':  li^ra  vö buyäryS  'sänh  (NP.)''  H%ra  vS  zavanif.- sav^(s±)  Ny.j.ii.
20118:•  j.  'masan-  Adj.  'gross,  bedeutend':^ffi>,*? .  ,  'sä/ias^ä  (GS.)  vauhänasiä  srayanascJ (sd.)  carpktnmahi  Y.  3Ä4.
20119:Ableit  aus  'masan-  n.,  durch  Ilaplol.  auä *masanaH-(i)'i;  man  beachte  das  ä  des  GS. and  S  403  I-  —  Pü.:  masiA  'Grösse'. —  ■)  S. auch  ai.  varmirt-,  nämin-  u.  a.  (bei  Wh.  Gr.' S  rijoi);  vll.  hat  sich  der  Typus  schon  im Arischen  ausgebildet
25216:»  ].  rasman-  m.,  n.  'Schlachtreihe ,  Pha- lanx': spala  . .  raihm  (sd.)  rasma  (NSn.) katarasHt  Yt  /4. 43 ;  —  ys  'manS  (APm.) sandaydti  Yti^öa;  61',  10.36,  41;  — antan  rSlta  'mana  (ADm.)  Yt74.47;  —
26885:•  j.  spasan-  Adj.  Iiinspähend  (auf  — )';
26999:•  j.  spantö.frasan-  Adj.  'heilige  Fragen stellend,    heilige    Unterredung    führend':
```


## [2026-09-04T19:03:40.988Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,bisect\ndata=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\noffs=[];pos=0\nfor l in lines: offs.append(pos); pos+=len(l)+1\nff=[m.start() for m in re.finditer('\\f',data)]\ndef leafof(ln): return bisect.bisect_right(ff,offs[ln-1])\nfor ln in [5724,5746,5907]:\n    print(ln,'leaf',leafof(ln))\nEOF\necho \"--- leaf content page numbers ---\"\nawk 'BEGIN{RS=\"\\f\"} NR==118 || NR==119 || NR==120 {print \"=== awkNR\",NR,\" leaf\",NR-1; print substr($0,1,300); print \"...TAIL...\"; print substr($0,length($0)-200)}' BRT.txt"
}
```


### [2026-09-04T19:03:42.651Z] TOOL RESULT

```
5724 leaf 147
5746 leaf 148
5907 leaf 153
--- leaf content page numbers ---
=== awkNR 118  leaf 117
Lok.  des Ziels :  fravaSayS  xinüth  ayantu  ahtnya nmäne  YL/j.  136.  Vgl.  auch  Simpl.
mit  <J  und  upa  'heran-,  herzukommen zu—'  (Akk.):  Aävanim  ä  ratüm  a  haomö tipäit  tardhustrsm  Y.g^-i,
mit  a  und  kam  'heran-  und  zusammen- kommen, sich  in  Verbindung  setzen  (mit�
...TAIL...
;  — xraosyS-taraca  (sd.)  .  .  hv5  urva  paräiti par3.asnäi  amihe  yaia  . .  V,  13. 8;  —  ya- tärö  paurvs  us>hiUaiti  paräiti  vahiltahe atshsus  y .  iS.^d.  2)  'aus  (dem  Haus) g
=== awkNR 119  leaf 118
ehen  auf  — ,  zum  Zweck  der  Verrichtung von-'  (Akk.):  *kat!lmS  timänahe  a'iauru- fi9m{sd.)  pärayäf^''  N.  /;—  para  paoiryö äiti  (näml.  a^aururitm)  para  bityö  aiti para  "hrityS  äiti  aita  paräyaiti  ycc^a gae'^äbyS  *k)nti  "es  geht  der  erste  (auf Priesterdienst
...TAIL...
^ariel  buland*') uzet.  Vgl.  lu  (KU-  No.  2,  'ar-  No.  8  f.,  usinidyäi, gam-  Ho.  16,  'Vax!-  No.  7  und  ^raod-  No.  5. Ganz  merkwürdige  Lesungen  bei  Gdn.  KZ. ja 332  und  Mills  la
=== awkNR 120  leaf 119
usit^idyäi;  s.  auch  WEST SBE.  J7. 387.  —  »*J  Nach  dem  Metrum  blos ytinti  IM  lesen.  —  =91  H.l.  faiti\iytU;  ai. iyaie.  Hds.  pailiiU.  Pü.:  pt,  verstümmelt. — 30)  D.  i.  faiH\iy&nle,  Neubildung  zu  lySili, N0.I3.  Pu.:  tmdeutlich.  —  3>)  Pü. : /alQEtd ;  s. dazu
...TAIL...
��        ,,  /.■i^\i  tt
fNo.i.-  «  Bthl.  AF:  2. 4. -J)  »bezieht  (eisern)':  'na  (AD.)  Ailvana  Vt.ii.s;  12. sich  auf  j/riVä  in  Strophe  7 ;  so  Gdn.  CIrPh. '  5,  Y.22.  a;  —  '
```


## [2026-09-04T19:03:54.616Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=147 && NR<=150 {print \"=== awkNR\",NR,\"(leaf\",NR-1\")\"; print}' BRT.txt | grep -nE \"^ *[0-9]{3} *$|=== awkNR|asan|asenga|as.nga\" | head -40"
}
```


### [2026-09-04T19:03:56.233Z] TOOL RESULT

```
1:=== awkNR 147 (leaf 146)
26:207
39:Ableit  —  Vll.  Komp.  asan-Jr'garta.  'Stein- höhlen  habend,  bewohnend',  also  eig.  Volks- nanie,  ai.  gärla-  m.  (wozu  MMülles  SBE.  32. 433).  —  ->  JusTi  GIrPh.  3.  455-
51:=== awkNR 148 (leaf 147)
58:Eiß.  Bed.?  Wohl  Komp.  mit  asan-i\.  —  Vgl.  l asa-iaiia-.  —  O  Gaui  Unsicheres  bei  Jusxl . NB.  42,  HoRN  NpEt   165.  '
61:•  j-t  E-  (.  P-)  asan-iaj«-,  j.,  p.  asman-  m." i)  'Stein':  *ja«s(alsAP.)  äi/i{sd.)  maya  äiti darSii"V.g.  11;  —  'sSnaShia'^ ..  vtHiaeh-a' . .  tBiuxha  (sd.)  V,  6. 5 1,  a)  als  Amulet: °samm  *siyaire.ci^rim  (sd.)  abars  *aAurö.- puirS  (sd.)  Yl;4.59-  b)  als  Waffe, 'Schleuderstein,  Steingeschoss':  Uavasca  . . •sanas(a  . .  (NP.)  fraäaxlaitya  V.  Z7.9;  — karjtS  .  .  vazrö .  .  'sänS  atymSJütä  Yt.  JJ. 72;  /.18;  —  jainti  mqm  ahuna  vairya avavata  snai^isa  ya'^a  'sma  iatS.masa (sd.)  Yt/7.20;  —  'sanS  (als  AP.)  tasia drazimnS  katä-masatiks  Aynti  V,  117.43); —  yahmai  .  .  aurvan/a  *yuxta  vJsa %an/asante  (sd.)  .  .  asUnas/a  (als  AP.) vispeMvia  "dem  .  .  die  Renner  am  ge- schirrten Wagen   ziehen  -  .  und  die  all-
68:109
75:=== awkNR 149 (leaf 148)
85:j.  asfnga-,  p.  a^a'ga-  m.  'Stein">. KompA.;  Abtrat.  —  Vgl.  np.  mult-äsaiii;,  mp., np.  lanf.  —  VgL  auch  asman-.  —  1)  Im  Iran, muss  äi',  as'  und  1'  vorhanden  gewesen  sein, E.  dRn.  np.  niiist-äiang,  j.  asingS',  mp.  sangi vgl.  zum  Ablaut  gr.  üap,  iap  und  Ut.  sniii;iiis; Bthl.  IF.  a.  z68;  Hbm.  PSt.  76.  Das  p.  Wort kann  auch  ä%'  gelesen  werden. j.  as«ngö.gav-  Adj.  'mit  Händen  aus
89:•  j.  »♦asanti  asmaji-fl  bammaca^.jil. Vorn  verstümmeltes  Wort.
108:=== awkNR 150 (leaf 149)
130:314
```


## [2026-09-04T19:04:03.696Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HRN asiya/asman\"; grep -n \"äsijä\\|asija\\|äsmän\\|asman\\|Mühle\" HRN.txt | head -25; echo \"### HRN sang/sanjidan/saxtan\"; grep -n \"sang\\|sangin\\|sanǧ\\|sangīdan\\|saxtan\\|sanjīdan\" HRN.txt | head -30"
}
```


### [2026-09-04T19:04:03.773Z] TOOL RESULT

```
### HRN asiya/asman
699:27. äsmän *Himmel', äsmä, semän,
701:ap. asman- 'Himmel'; aw. asman-; phlv. äsmän; ai.
703:kiird. LW. asmärij äsimün, asmm; a{y, LW. äsmän;
705:si/n. LW. äsmän,
3971:nur 'Stütze, Mittel zu halten etc.*) ; bei. Janfar Mühle,
4070:aw. dasman- 'Auge'; phlv. casm, casm[gäh, öasmak
5450:zu aw. rasman- 'Schlachtreihe', ai. ragmän-^ racmi'^
5470:An Ableitung von aw. rasman- 'Schlachtreihe' zu
### HRN sang/sanjidan/saxtan
704:bei. n. äzmän (22); sangl. minj. LW. asma, wa/. sar.
1020:wruy, sangl. wurij.
1151:minj. asti, sangl. astak.
1531:augar, §iyn. angast, sar. ingä/t, sangl. ingit.
1785:worz, worö^ uorc, wäre, sangl. worak Tferd' (aus
2097:sangl. tt'wrd.
2168:sangl. varf, min], värfa,
2255:bilc, sangl. wuz, minj. woza, si/n. sar. waz,
3127:sangl. paw2^, minj. panc.
3175:aiy, pöza^ paza ; sangl. fuzik, minj. foska,
3272:päd, sangl. p%iö, minj. pald 'Fuss' gehören zu aw. päd-
4074:sar. cem^ sangl. sam^ minj. cam,
4171:%n. cavor, cavdr, yayn. t/ö, sangl. sa/ör, niinj. ca//r.
4303:«ar. cer, üer, sangl. //tr, minj. xara.
4535:;^m/, sar. ya;^, minj. yayvd, sangl. i/vd.
4578:ydr-am, sar. yör-am, sangl. y^är-afn.
4618:hon (162); wa/. vu/c^n, Uyn. vlyTn, sar. va/ln, sangl.
4847:kurd. du/t, ditt; af/. lär; wa/. da yd, sangl. da/,
5108:siyn. döst, sar. düst, sangl. dast, minj. last, yidg. lust.
5132:sangl. mrütj^ minj. 2?/.
5178:hüi, sar. däu, si/n. Jö, yaj'n. sangl. du, minj. do.
5269:ya;ai. sangl. das, minj. LW. daÄ.
5608:si;n. rosnagd 'Tageslicht*, sangl. rösnäi 'Feuer.
5616:sangl. röy, sar. rdim,
5754:wa;^. zatij sar. zm^ sangl. zong.
6107:diese Weise'; afy. San; bei. sang (236).
6220:(166); LW. sar. spSid, sangl. ispSd, sijn. sufed, rtiinj.
6249:asiäri, sangl. ustürak.
6358:kurd. afj'. bei. (884) sar; oss. sär (220) ; wa/. sangl.
6412:srayltan^ sräy(i)su^ srüt 'Gesang; ai. l/'grav-^ Caus.
```


## [2026-09-04T19:04:08.539Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '694,712p' HRN.txt; echo \"======\"; sed -n '6095,6120p' HRN.txt"
}
```


### [2026-09-04T19:04:08.604Z] TOOL RESULT

```
^) Darmesteters^s Etymologie für np. äsän *leicht' (Et ir. II,
134) aus &yf, aspen[clf, a8pen[cä ist trotz \ih\y. nspln (Darmesteter,
Textes Pehlvis relatifs au judaisme 6 Note 4) kaum richtig, da auch
die Bedeutung von aw. aspen nicht passt (vergl. Bartholomae^
^Z, 28, 14, BB. 13, 90).— 8
27. äsmän *Himmel', äsmä, semän,
g. asbän,
ap. asman- 'Himmel'; aw. asman-; phlv. äsmän; ai.
dgmafi-.
kiird. LW. asmärij äsimün, asmm; a{y, LW. äsmän;
bei. n. äzmän (22); sangl. minj. LW. asma, wa/. sar.
si/n. LW. äsmän,
28. äsüden ^beruhigen, ruhen', Praes. äsäy-em, -äsä,
äsäijis^ äsäyist (jüd.-per$.).
aw. *ä + sävayeitl (Bedeutung?); phlv. äsiitan^
äsäy(i)sn,
29. äs *Brühe, Speise .
skr. äga- in prataräga- Trühstück'. säyamäga- 'Abend-
essen ; vergl. aw. kahrkäsa- *Hühnerfresser.
======
(\)8än 'Wetzstein.
Siehe efsan (No. 98) 0.
*) Nachträglich sei hier noch np. sumhäde (goschr. sunb"), Käs.
K. sunbötä, arab. LW. sunbäSaj^ sunhäSat (Bibl.' geogr. arab. IV, 277)
'"Wetzstein* erwähnt
■}\*m^t!/*m.^i— 154 -
694. (2)säii 'Teil, Stück; Art und Weise'; -$an gleich,
ähnlich, -sä.
Die Deutung von aw. sü^ia- (yt. 19, 44) als *Stück'
(Studien, I, 148) hat Geldner BB. XV, 254 wider-
rufon.
LW. kuid. säriy z. B. kH\sän *öü; wie?', va]suna auf
diese Weise'; afy. San; bei. sang (236).
Np. -sä^) hat das auslautende n verloren, wie äsuid,
a (No. 52), senrjso (Käs. Z. zu 1. süh) u. a. ni. Gehört
np. 'äsan 'äsä gleich, ähnlich* auch hierher?
695. säf/e 'Schatten, Schutz'.
ai. chayd' 'Schatten'; plilv. sayak,
kurd. se^ si\ bei. säig, n. saJ (340); wa;^. LW. sayd,
sar. suyä,
696. supär Tflug .
ai. phdla- Tflugscliar*, zu l^phal-, splial- *aufreissen'.
sar. spur 'Pflug .
697. Hiipävden anvertrauen, übergeben*, jüd.-pers. p1N?10,
supiirden, sipäris (sifärls).
g. vaspartmün.
```


## [2026-09-04T19:04:09.632Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"'Stein'\" HRN.txt | head -20; echo \"=== HUB\"; grep -n \"asan\\|asenga\\|asmän\\|äsmän\\|sang\" HUB.txt | head -30"
}
```


### [2026-09-04T19:04:09.703Z] TOOL RESULT

```
=== HUB
679:p. 5, Z. 15, und die Dialectformen vonKasan wie dervostdn
785:ban 'Haus' = ap. vahana- (vgl. skr. vasana- 'Wohnen*,
1072:Fr. M tiller zu skr. vasana- *Gewand' stelle. Der Be-
1407:kommen', paz. pasandfdan *to approve* Skh. 263 ist mit
1434:— phi. "^patsincat = np. pasanjad. Sehr friih er-
1604:379. Die zu np. tadarv Tasan ^ (Fird. I, 485, Z. 3) ge-
1882:(= hu-rasant' gut-kommend' ab.)
2542:belli u. s. w., vgl. bal. sang 'Grund, Ursache, Zweck,
2547:skr. gasana- Torschriff (ZDMG. 47, 702) ist auch nicht
2549:p. 147 s. V. aunbada) vgl. np. sang i sal 'Schleifstein'
2639:'Gesang, Lied' (mit d) zu sprechen ist, vgl. die LW.
2660:ausserdem auch angi^t (Nr. 126) und zuyaly {zuyOl i sang
2683:747. Die Erklarung von sang *Stein, Gewicht* stimmt, wenn
2685:-asang) 'Stein und *&anga' {^= np. sang) ^) *Steiu' an-
2689:•) Zd. asenga-, wenn es hierher gehort, konnte fiir asenga"
2691:nimmt, da ^d&anga- im Phi. als asang vorliegen
3616:Dazu auch nava 'Melodic, Gesang , arm. nuag *Melodie,
3691:1079. Die Zusammenstellung von varsang mit skr. urugqsa^
4020:den Dialekten von Kasan, Shukovski p. 75 und 176 gegen-
4064:bar *Thur* (Jezd und Kasan, ZDMG. 35, 405; 36, 70, Shuk. p. 122),
4336:np. pasand u. s. w. ;
4464:jfidan = pasanjldan 'besprengt werden, aus "^pal-sinc-Uan
4483:adada), zu dem np. dihis 'Gehen = np. dasan *Gabe, Geschenk'
4787:pasanjidan 'besprengt werden' aus ^paUsind-ltan zu skr.
5070:Vgl. § 23. In den Dialekten von Kasan, Semnan u. s. w.
5819:307; Pahlav 'Parthien' --=^ ap. Pardava-; fadarv Tasan' H.
6024:Folge Ausfalls von h : dasan *Geschenk' ') = phi. dahisn ;
6029:gebildet ist, nach dem das Ultere dahisn bereits zu *dasn ■= dasan
6097:surod 'Gesang, Lied' = zd. sraota-; surudan (pr. sardyam)
6127:afsan 'Wetzstein* = fasan H. 98; afsurdan *frieren' = fu-
```


## [2026-09-04T19:04:15.094Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2678,2700p' HUB.txt; echo \"==== 2535-2555\"; sed -n '2535,2555p' HUB.txt"
}
```


### [2026-09-04T19:04:15.155Z] TOOL RESULT

```
^sumpdmi angesetzt werden. In beiden Fallen stimmt
der Inf. np. suftan. Dazu np. sufra = afgh. LW.
sufra *the anus* = ap. *sufra- aus ^gupra- ? Zd. si/^
und suwrO- (var. sufrO-) sind in der Bedeutung un-
sicher.
747. Die Erklarung von sang *Stein, Gewicht* stimmt, wenn
man fiir das Altpersische die Formen ^a&anga- (=:np.
-asang) 'Stein und *&anga' {^= np. sang) ^) *Steiu' an-
*) In asabara- *Reiter* = np. asvar und in ap. *asatara = np.
aatar 'Maulesel*, skr. agvatara- (neben ap. uvaapa^ ViStaspa, Aspacana,
*) Ap. & (aus k^) im Anlaut = np. s.
•) Zd. asenga-, wenn es hierher gehort, konnte fiir asenga"
stehen.— 77 —
nimmt, da ^d&anga- im Phi. als asang vorliegen
mtisste.^) Denn anlaut. a geht erst im Neupersischen
verloren. Die Bemerkung iiber sanjvdan Vagen* ist
unklar. Als alte Formen sind offenbar anzusetzen:
inf. saxtan (ptc. saxta gewogen ), praes. sanjam {-sanj
Vagend', sanja ^Gewicht*), von letzterem aus ist der
Infinitiv sanjTdan neu gebildet worden.
748. Lies so, sot = phi. sdk. Vgl. die Nachtrage bei
Horn p. 259.
749. Fiir aspvOrakan BB. 4, 39 und 62 ist vaspuhraMn
==== 2535-2555
II, 31). Np. sardar ist wieder neugebildet.
693. Ist phi. sdmdn = arm. sahman, so ist als altere
Pehleviform wohl sdhmdn anzusetzen? Die Zusammen-
stellung mit skr. gad 1) *sich auszeichnen, hervorthun,
2) abfallen' ist zu unsicher.
694 ***' Die Zusammenstellung von np. sdn *Art und Weise'
(Vullers: mos, institutum, modus, ratio; apparatus
belli u. s. w., vgl. bal. sang 'Grund, Ursache, Zweck,
Absicht', afgh. san ^) muster, review of an army' ?) mit
') Jetzt stellt Geiger np. san mit afgh. sdn *Aehnlichkeit, &hn-
lioh, way, manner, method* zusammen, fur das man daqq freilich *Sfin
erwarten soUte.— 73 —
skr. gasana- Torschriff (ZDMG. 47, 702) ist auch nicht
sicher. — Zu dem hier angefuhrten setigso (Shuk.
p. 147 s. V. aunbada) vgl. np. sang i sal 'Schleifstein'
(Rosen, Np. Sprachf. p. 50). Das in der Anmerkung
erwahnte np. sa Tribut = phi. sak (Matikan i 5atrang,
phi. Text p. 1, 12) ist = arm. LW. sak 'Tribut' (Elise
35, 6). Zu np. sav vgl. afgh. LW. sav a taxe, a tribute*.
697. Im Phi. ist apspurtan zu lesen, vgl. arm. ap-spar-em
'iibergebe, iiberlasse, vertraue an . Als iranische Wurzel
```


## [2026-09-04T19:04:27.283Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sanjīdan\\|sanjidan\\|sanǰīdan\\|saxtan\\|θanǰ\\|Oan[jǰ]\\|\\*θanj\" CHEUNG.txt | head -30"
}
```


### [2026-09-04T19:04:27.336Z] TOOL RESULT

```
9085:pisanjidan ‘to sprinkle’, Khor. pšing ‘spraying, explosion’ 
21228:/passaxtan/ || (+ *ham-) Pass.: pres. SUBJ. 3sg. MMP hs’cyh’d; Partic.: perf. pass. MMP hs’xt, hs xt 
21265:*NWIR: Widely attested: NP sazad ‘it is fitting’, saxtan/saz- ‘to build, construct, 
21672:*Oanj ? 
25464:Pres. aja-: IND. 3sg. YAv. fradanjaiieiti (Yt 17.2), med. 3р1. YAv. Oanjaüente (Yt 17.12), SUBJ. 15р. 
25465:YAv. Oanjaiieni (Yt 5.50), 3pl. YAv. Oanjaiiante (Yt 19.44) 
25508:*NWIR: NP sanjidan ‘to measure; reflect; compare, put in balance’, (LW) NP linj- ‘to 
25892:development can be noticed in OCS pri-teZo (pri-teZati) ‘I acquire, work’, s.v. *Oanj. 
41333:pisanjidan, 127 
41450:sanjidan, 392 
41462:saxtan/saz-, 324
```


## [2026-09-04T19:04:29.384Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25455,25530p' CHEUNG.txt"
}
```


### [2026-09-04T19:04:29.436Z] TOOL RESULT

```
*PIE— > LIV: – | Pok.: 
*REFERENCES: Schwartz 1970: 292; Sims-Williams, 1985: 131 


*Өапј ‘to pull, draw’ 

*AVESTAN: Y Av. anj- ‘to pull, draw’ || (+ *fra-) ‘to drive to’ = Liste: 26 

Pres. aja-: IND. 3sg. YAv. fradanjaiieiti (Yt 17.2), med. 3р1. YAv. Oanjaüente (Yt 17.12), SUBJ. 15р. 
YAv. Oanjaiieni (Yt 5.50), 3pl. YAv. Oanjaiiante (Yt 19.44) 

*MIDDLE PERSIAN: BMP hnc- /hanj-/ ‘to draw (water)’ (h- is from *haié or the pre- 
figated forms?) || (+ *a-) MMP "hynz- ‘to pull, draw up, tow’, BMP "hnc- ‘to draw 
up (water)’ || (+ *fra-) BMP pl’hnc- /frahanj-/ ‘to educate, instruct, teach’ || (+ *ni-) 
MMP nhynz-, BMP nhh- /nihax-/ (pret. stem) ‘to hold back = DMMPP: 36a, 242b 
Pres.: IND. 1sg. BMP hncm /hanjam/, 3sg. BMP hncyt /hanjéd/; Inf: BMP hyhtn /hixtan/; Partic.: BMP 
hyxt /hixt/ || (+ *а-) Pres.: IND. 3sg. MMP *’hynzyd, 3р1. MMP "hynzynd (MacKenzie 1980: 291), BMP 
/ahanjénd/, SUBJ. 3sg. MMP ’hynz’d, 3pl. MMP ’hynz’nd, IMPV. 2р1. BMP ’hncyt /ahanjéd/; Partic.: 
pres. MMP ’hynz’g, perf. pass. MMP "hxt, BMP ’hht /ähixt/ || (+ *fra-) Partic.: perf. pass. BMP plhhtk(-) 
/frahixtag(-)/ ‘educated, trained’, BMP plhht /frahixt/ || (+ *ni-) Pres.: IND. 3pl. MMP nhynzynd, SUBJ. 
3sg. MMP nhynz’d, IMPV. 2sg. MMP “nyhynj; Pass.: perf. pass. ВМР nh'ht (HWH)nd /nihaxt/, nhht 
/nihaxt/ 

*PARTHIAN: (+ *4-) "hynj- ‘to draw up’ || (+ *pati-) pdhynj- ‘to weigh’ || (+ *fra-) 
frhynj- ‘to instruct, educate’ || (+ *ni-) nhynj- ‘to retain, hold back’, nhng 
‘oppression’ — Ghilain: 51 | DMMPP: 36a, 269b, 155, 242a f. 

(+ *4-) Pres.: IND. 3sg. "hynjyyd, *’hynjyd, 3р1. "hynjynd || (+ *pati-) Pres.: SUBJ. 2sg. pdhynj’h ‘weigh 
[i.e. judge]’ || (+ *fra-) Pres.: SUBJ. 2sg. frhynj’h || (+ *ni-) Pres.: SUBJ. 3sg. nhynj’, IMPV. 2pl. 
“nhynjyd ‘protect!’; Partic.: perf. pass. nhxt|| (+ *ui-) Pres.: IND. 2sg. whynj’h; Partic.: perf. pass. whxt 
*KHOTANESE: OKh. this- (this-) ‘to pull at’, OKh. thamj- (caus.) ‘to pull’ || (+ *apa-) 
OKh. pathis- (pathis-) ‘to refrain’, OKh. pathamj- ‘to restrain’ || (+ *upa-a-) LKh. 
bathamy- ‘to pluck out’ || (+ *us-) OKh. usthamj- ‘to draw, pull out’ || (+ *ni-) OKh. 
nuhamj- ‘to hold back; open’ = SGS: 42, 94, 68, 18, 59 


392 *0jaj (*ti(n)j2) 


*SOGDIAN: BSogd. óync ‘to pull out’ || (+ *pati-) BSogd. pö’ync, MSogd. pddync ‘to 
pull out’ || (+ *pari-) BSogd. prö’y, CSogd. prOync ‘to stretch’ 

Partic.: pres. BSogd. dync’k || (+ *pati-) Pres.: SUBJ. 35р. BSogd. pö’ync’t, Pass.: pres. IND. 35р. 
MSogd. pöö’ytyy Pwt ‘is pulled out’ || (+ *pari-) Impf.: IND. 3pl. CSogd. pry@ynent, Pret.: intr. IND. 3sg. 
BSogd. pró'yt'kw y’y, (£) BSogd. prö’ytch y’y; Partic.: perf. pass. BSogd. prö’yt’kw, BSogd. prö’ytch 
(#); Pass.: pperf. IND. 3sg. intr. BSogd. pró yt'kw х у, BSogd. prö’ytch "y 

*CHORESMIAN: (+ *pati-) ? p@xs- ‘to take refuge in (God)’ © Samadi: 163 f. 
*BACTRIAN: vayyo ‘load’ || (+ *apa-) aBavay- ‘to charge’ ? || (+ *4-) av-avaydo 
‘without deduction’, avayyo ‘neighbourhood’ || (+ *ni-) vavayyo, vavayyivdo 
c» S-W, Bact.: 227b, 174a, 173a, 179b, 208a 

*NWIR: NP sanjidan ‘to measure; reflect; compare, put in balance’, (LW) NP linj- ‘to 
pull’ (< Sogd./Bactr.), Gz. säng-/sängä ‘to rock’, Semn. (impv.) bi-hänj ‘stab !’, 
-tä/-änj- ‘to draw || (+ *a- NP ahixtam/ahiz- ‘to draw (a sword), NP 
ahanjidan/ahanj- (caus.) ‘to drink; to drag; to fling’, Zaz. antis/anjen- ‘to pull’ || (+ 
*fra-) NP farhang ‘culture, education; dictionary’ || (+ *ni-) NP nihang ‘a kind of 
sea-monster, crocodile; sword’ 

*NEIR: Pash. länga (Ё) ‘lace or rope for tightening the web of a charpoy’ || (+ *abi-) 
Oss. I. ivtynzyn/ivtygd, D. evtinzun/evtigd ‘to yoke a horse; to load a gun; to wind 
up a watch, vel sim.’, I. ivtong, D. evtong ‘equipped, ready for action, under way, 
sim.)’ || (+ *a-) Pash. anang, alang ‘span from thumb to forefinger’ || (+ *ui-) Oss. I. 
tynzyn/tygd, D. itinzun/itigd ‘to spread, stretch out; to crucify’ 

*MISC: (+ *ni-) Arm. (LW) nhang ‘a kind of water beast’ 

9 The initial *0- of the root is puzzling: does it point to the presence of a following 
laryngeal ? The assumption of an older IE *f’-, as found in LIV, l.c. is unacceptable. 
One may also think of influence from the antonym *@ra(n)é ‘to press’. 

«PIE *teng"- ‘to draw, pull back’. > A slightly different preform is reconstructed by 
Kümmel in LIV, Le: zeng. His objections against the postulation of *tH- (on 
account of the Iranian evidence) and his explanation (invoking the loss of an 
s-mobile variant) are incomprehensible to me. *teng^- is clearly an enlarged root of
```


## [2026-09-04T19:04:42.026Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD\"; grep -nE \"^(sang|ās|āsmān|as|asman|sanj|saxt|xist|wād)\" PHD.txt PHD_mackenzie.txt | head -40"
}
```


### [2026-09-04T19:04:42.085Z] TOOL RESULT

```
### PHD
PHD.txt:108:astr. astrology, astronomy Av. Avestan
PHD.txt:218:asém Deum | = M, N sim] silver. „ēn [-yn! | N -in] silver(n). asmān (тл! | = M, N āsmān) sky, heavens; cal. 27th day.
PHD.txt:219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
PHD.txt:220:aswür 13 āwēnidan
PHD.txt:221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
PHD.txt:563:sang 74 sén murw
PHD.txt:564:sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-s?1] stony place. sanj-, v. saxtan. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) danger, trouble. --ómand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
PHD.txt:858:as (av.) won, čiyēn; (cj.) čē; ~ if ¿iyon ka.
PHD.txt:859:ascendant ul-āmadān.
PHD.txt:860:ascribe to abāz dādan 6.
PHD.txt:861:ashamed šarmgēn; be ~ pafšir-.
PHD.txt:862:ashen ādurestarēn.
PHD.txt:863:ashes ādurestar. .
PHD.txt:864:ask pursidan, zastan, (zayistan).
PHD.txt:865:aspen spéd-dar.
PHD.txt:866:ass xar; wild — gor.
PHD.txt:867:assembly hanjaman.
PHD.txt:868:assignment paymar.
PHD.txt:869:assist ayaridan, frayadidan.
PHD.txt:870:assistance abāgīh, dastyārīh, frayād(išn).
PHD.txt:871:assoctation hamīh, nišast.
PHD.txt:872:assured(ly) éwar.
PHD.txt:873:astonished widimušt.
PHD.txt:874:astonishing škeft.
PHD.txt:875:astonishment Skeftih, widimuštīh.
PHD.txt:876:astray wiyābān; lead ~ wiyābānēn- īdan.
PHD.txt:877:astrologer (-6Émur).
PHD.txt:878:astrology axtar(a)marih, kundāgīh.
PHD.txt:4813:saxt
PHD.txt:4814:saxtan, saxtan süg, sak say- sahigih sahig, sivag sas
PHD.txt:5137:asnaw-!
PHD.txt:5503:sang, suy sneh
PHD.txt:5505:asp!
PHD_mackenzie.txt:119:asterisk.
PHD_mackenzie.txt:337:as possible realizations of postvocalic b, d, g, j.1
PHD_mackenzie.txt:469:astr.     astrology, astronomy
PHD_mackenzie.txt:1206:asAn ['s'n l IN .....] at rest, easy, peaceful.
PHD_mackenzie.txt:1209:asay~, . . . . i§n,v.asfidan.
PHD_mackenzie.txt:1216:asem ['sym I = M, N sim] silver.
PHD_mackenzie.txt:1218:asrnAn ['sm)n l I = M, N asman] sky, heavens; cal. 27th day.
```


## [2026-09-04T19:04:59.918Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -nE \"āsyā|asyā|'sy'k|ʾsyʾ|āsmān|asmān|^sang|sng\\]|wād-ās|vāt|xist\" NYB_vol2_glossary.txt | head -30"
}
```


### [2026-09-04T19:04:59.979Z] TOOL RESULT

```
78:"YT', "YTY (inser.): ’ITAY it exists, there is 'ZLWN-: "ZL to go
286:a-frac-saci8néh [’pr’c sešnyh] the quality of not passing away, continuance, con- tinued existence (of the family) 597°. — Av. (1554) pasca frasaxtahe mašyehe ‘after mankind has come to an end’, Vd. 1928, is rendered in Phl. by pas hac fräc-sacisneh i martömän, v. sacišneh.
417:heard as such a ''modesty pronoun" = I. — This pron. is, however, obsolete in BP, and the cas. obl. man (q. v.) is regu- larly used as the cas. rect. The Pazandists had lost all tradition regarding the equi- valent of the ideogr., which they trans- literate mechanically aomen (Mx, SGV), when occurring in the texts. It was omitted in most MSS of the FrP (want- ing in Junker’s text), but exists in Codd. P and S, though with misunderstood Ir. equivalents.
431:an-aryan [’n’ry’n] (Prth) non-Aryans HajA: 2. ŠPrth: 5.11, = Prs anörän. anäst ['n'st'] nothingness, that which is vain, worthless: dróv u ~ 83%. 8427. — Paz. anäst, Skr. v. nästikya (Mx), nästika (SGV); anahast ‘non existent’, Skr. v. asat, nāsti; anahasti ‘unreality, extinction’ (SGV, Aog.). From the neg. pref. and (v.s.v. anāvinast) + *hast; anāst < ana- hast with contraction seems to be the older form, anahast to be a recent for- mation.
468:"p: api-š, ”pm’n' or (Ps.) *pmn: api- man, ’pt’n': api-tän, "p$^n! or (Ps.) *pšn: api-ščin: 1. and, introducing and coordi- nating sentences, e.g. andar-rón andar šut api-$ guft 1818-14; coordinating substan- tives if the second subst. is determined by an encl. pron., e. g. zantšn + Ahriman api-š visütakän 8819; also preceded by u: u api-t 6°, u api-š 7822, u api-sdn 79°, etc. — 2. introducing the apodosis after ka 94. 1025, 5225-27, 5418; after cigon 931; after an isolated w. having the character of a protasis: hämöden api-š hàn zan... ayyāt būt all this [to supply: engaging his attention], the remembrance of that woman came upon him 11'!-!*; — taking up the sentence again after a preceding digression: han zan u hàn fradand 1-8... api-man ne özat 1212-3. — Av. (82 sg.) aipi, OP apiy ‘moreover, further’, both encl. and often only emphasizing: OP düraiy apiy (and other spellings) ‘very far’; surviving in Milr -p(?), g. v. Along with it there must have existed a fully stressed form "dpi; id.-europ. "dpi (Gr postp. Ézt, prep. èni), whence the gen- uine Arm. eu ‘and’; it is the counterpart of Gr ču, Lat et (eti-am). This "dpi > Milr ap, in the sense of ‘and’ and in the apodosis, is normally used in the Sassa- nian official language as the bearer of encl. pronouns beginning the sentence, but in fact occasionally occurs alone, as in the Ps. (several instances, v. Gloss.); PR 231.14, 347. 404; PhlY 31! (intro- ducing the apodosis). Apparently it was counted among the archaisms which need- ed explanation, because it was included in the FrP (ch. 24). Paz. has preserved some remnants of the archaic form: awam = api-m SGV VII, 22, awama = api-mān ibd. VI, 47. X, 28. 35; Paz. AV, ed. Antiā, Päz. texts 35818; hawasq = api- gan SGV V, 62, etc.; the Paz. forms reg- ularly occurring may be shortened allegro forms of api-m ete., v.s.v. u. The equi- valents of api-m etc. given by the FrP are wm, wt, wš, which seem to coincide
557:urvar har cé ne ~ (se. hösitan) à nē hošet 9612-13, 9810-11; — apāyet būtan it is bound to happen, of predestination, explains jäyisn 271, brihenisn 16°; used itself as a nominal expression of Predestination: apäyet-bütan rād 16!!; — b) taking a v. n. as its complement: -šān ... gošt z"arisneh ne — it is not allowed for them to eat meat 10420-21; — e) governing a subordinate clause introduced by kū 8!. 1181-14 by ka 56?? (gl); without an introductory particle, with the governed vb. in ind. or in Subju.: ~ stdyé thou shalt profess 596; bē ~ apesihät 4419-19, v.s. v. apa- sistan. — MPrs ’b’yd with inf. (A-H II); Paz. āwāyastan āwāyad; āwāyastaa ‘re- quisite, desire’ (SGV); NP bäyistan, bā- yad; andar-vdi ‘desire, need (cf above no. 3; to be distinguished from andarvāt ‘atmosphere’, g. v.). Den. of OIr *updya- < *upa-aya- ‘that which comes upon, is imposed upon, affects a p.' = 1. need, 2. duty, cf Av. (150) upa-ay-, v. HP II, 17 sg.; Verbum 168; Ghilain 48. apāyišnīk ['p'dányk] proper, fit, fitting, handsome, nice, exquisite, comp. ~-tar, 33-5. 422, etc. passim; pl. cas. obl. ~-dn the qualified ones 1052,
646:artži [’lt’y], artäk [*lt*k] righteous 2214, 239. 249. 128%; vāt 1 ~ the good wind (wind sent by the Righteous Powers) 717.23 Plek]. — artāi < *artāv < OP artävä, the nom. sg. of artävan-, is the genuine Prs form of the w. which appears in the religious language as ahlav (q. v.); final -v > -y is the common rule in SW. — artak is only a secondary spelling of artāi; Ps. also ’U’dy = artäi. MPrs abstr. Pyy (S) = Ps. "'lP?dyhy, v. Sogd 504 (and 31). — Artäk Virdz n. pr.: v. Viraz.
717:āstišnēh: mēnēi ~ existence at the heav- enly stage of development 3821; gētē m existence at the earthly stage of develop- ment 393-28; pas hac dam pat menči m after the existence of the creation at the heavenly stage (= after the creation had entered upon the heavenly existence) 3871-22; rai ~ ever-lastingness of splen- dour 5918,
819:axistan [hstn'; KDMWM-tn']  dzéz- Phyc-, KDMWN-] to stand up 1418. 3217. 33; apar ~ id. 233-74, passim; apde = to rise from the dead 105'7. — Ps. ^hstny hyc-; MPrs ’zystn ’xyz- (S, A-H I); < ā- + BP vistan [hstn'] x&- [hyc-];
826:ax" ['hw] existence, life: ~ ti astomand the material, terrestrian world 378. 40! etc., passim. — Av. (106 sqq.) ahu-, anhu-; FrP, Cod. P fol. 7a with the Paz. reading axti and the NP gl. dunyā. Paz. common- ly óx. — Another ax“ v. patvast-axteh.
951:bavišn [YHWWN-šn'] v. n. of bütan: the act of entering into material existence; material existence 109° (opp. vindsišn). — Corresponds exactly to the Arab. philo- sophical term kaun (opp. fasdd), Gr yeveoic. Cf bütak.
1044:burtan [bwltn'; YBLWN-, YDLWN-tn'; forms v. I, 178] bar-, to carry, to bring, to bear, to wear, to procure; to take away, to remove (6 or pat ‘to’); arišk ~ to bear envy 691. 8419; !a&, bes, dast, dašn, gobišn, nam, namāc, nipart, paitäk, srav, stēžak, vāng, pat xrat ~: v. these ws.; bahr ~ v. barišneh; — to place on the top of (apar) 444; to lay a p. on (6) 4720-21; — andar 6 tan ~ to bring into corporeal existence 92t; — andarg ~, v. göbisn; — apar ~ to send out against 3711; to bring 6016; dmdcisn apar ~ to give instruction, to teach 80%; v. also apar-barisneh and apar-burtäreh ; — frac ~ to bring, to present 411; to bring forth, to light (a fire) 44°; — fröt ~ to bring down, to shed (water) 417°; v. also fröt- barišneh; — 6 ham ~ to collect, to amass 4815; pret. construed as an act. 187% Common Iranian; Av. OP (933 sqq.) also — (act. and middle) ‘to ride’, cf barak and asvār; cf also apar-barišneh from bar- ‘to move’.
1061:become, to occur, to happen, to come true; to arise, to come into existence, to grow, to originate; to exist, to be, passim; héc ké büt hénd u héc ké bavénd u héc ké hend 6417-18, cf bütün, hame-buteh, hame- baveteh, bavētān ; dané ku fratäk rēc ce bavet thou knowest what will happen to-mor- row 21°; apdyet butan, v. apčiyistan; būt i zivist u būt i murt hend there were some who survived, and there were some who died 95?” sg.; būt dastavar ké-§ guft there was a certain Dastur who said 1018; būt kē-š guft there was someone who said, erat gut diceret 103?9; h&c kas nē būt ke ... dänist there was nobody
1064:nē būt 675-26; bavēt... Zartuxst it must be Z. 6023; nē yatük: [YHWWN-#'] bavat he cannot possibly be a sorcerer 3774, v. Grammar 53. — 3. In the 3d p., together with a subst. virtually in dat., or with a pron. in cas.obl., it expresses the notion ‘to have’, e.g. õi kē-š zan nē būt he who did not have a wife 101!; amdvandéh ... i-m būt the vigour which I had 341; -t dānākēh bavét wisdom will be allotted to thee 595; duxtar i varzēkarān én hunar ... i to hast ne bavet a farmer's daughter cannot have such an ability as thou hast 18520-21; with rád as in NP: Pdpak ràd hec fradand nē but P. had no child 19-7. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions: (7) matār būt hēnd who used to go 61”; nikeräi (g. v.) bavét 8214; tō . . . ästisn ne but hah thou wouldst not have subsisted 3515-16, 3421-22; _$ hàm zan... ayyät bit he remembered that woman 1111-12; 123-4; -§ vat hayyär bavét the wind helps him 25; Ohurmazd ziyān ne bavēt O. will suffer no harm 7727; v. also äkasi, hangir- tikeh. — 5. With preverbs: andar ~, v. andar; — apäc ~ to become again 7714-15, 10021-22, 12025; to come into existence again, to be restored to life 46°. 10416-26; to be left, to remain 39277. 4416; — apäk m = apāc ~ 3423; as to 161-7, 2426-27, v, apäk; — apar ~ to be imparted to 80%; — fräc ~ to recover (hac from) 5419.12, 6022; — 6 ~ to approach, to come on 65; to pass into 4216-17; — 6 ham ~ to be put together, to be formed (from different elements) 4317; v. also hambavisneh. — 6. As an auxiliary vb. added to the pt. pret., būt forms the pluperf. in dependent clauses, as against ēstāt in independent sentences: pas hac han + Artaxser han kirm ēzat būt after A. had slain this
1069:who knew 121°; būt i ka nē būt ... u bavet ka ne bavet ches was a time when he did not exist, and there will be a time when he will not exist 642-3; ö(h) ~, v. ē(h); cf bavisn. — 2. as copula, with a noun, a pron. or a prep. + subst. as its complement, passim: hàn but Vahuman 56%; martom ... hamäk ahēš ... bavēnd willbe immortal 1049-19; kanicak pat giyäk bütàn (YHWWN-t*n'] pl. cas. obl. of the pret. büt used as a subst. ‘he who has been’ 5518, ~. V. bavétün.
1123:cigon [cygwn] adv. and conj. A. interrog. adv. how? 1. direct interrogation: nun ~ kunom ?] 272; asmān ~? 921; exclama- tory: how...! 614. — 2. indirect inter- rogation: äkäh hom ku ~ hän 571; vēnēt ki Bastvar kārēcār ~ nev kunēt saw how valiantly B. fought 2815-16; ~ 6, 6 ham pursem 57°, andar Garodman dätistän ~, api-m nē dit 527-3; ete. — B. rel. adv. so as: l. har 3 šap x"amn ~ dit Estät ... guft such as he had seen it 2%; 215, 48, 520, 4527, ete.; introducing quotations: ~ den göbet 387, ~... paitāk ku 4571-5, etc. passim; parenthetic, e.g. 7718, 818%; — with a demonstr. antecedent: hamgönak hast ~-am guft 1216-17; šmāh bat ētūn m to gobeh 2329; 4524-25, 782.4, etc. — 2. with- out a clause, used prepositionally: as, as (for instance), as it were, like: ~ agäh aköc martom 2678-27; ~~ martom kë šarm 43913; 12813; varcāvandān i ~ Yam u Frétón ... 45°; hàn 4 ~ én such a th. 438; namely 1078; — with a demonstr. antecedent: &ön ~ āluh-ē 9%; eton ~ to 1516; ét6n but ~ amahraspand-ē 38°”; — čton, or ógón, homänäk (a. v.) ~ 69%, ete.; mänäk(k)äi (g. v.) i õi ~ ke pus... bare (opt.) 418. — C. conj. 1. causal be- cause: ~~... hdn mazantom bit 613-4; 1081. 11812; almost as a rel. pron. with a sec- ondary causal sense (as in Lat. quippe qui): 6 xuähar i x*"e$, ~ zan 4 Artaxsér būt, nämak nipišt 822; 718%, 7916. 116%. 11819; — hac han ~ in view of the fact that, considering that 38. — 2. temporal as soon as: 6°. 15°. 44°, more emphatically ham-~ 1317. - 3. ~ ka as if 11214.17, 10120722 — 4. almost = that 8722. — MPrth cw'gwn; MPrs ewn (read ci'on < *ciwön <
1229:to deposit 922. 10912; — bē ~ to deposit 395.7:22. 402. 4910. 48?2. 4098-9.22-23, 5015, 9427; pat damīk bē ~ to lay (an enemy) in the dust 3329; to take off (clothes) 577; — (bé) 0 . . . — to transfer to . . . 88%. 953. 12016, — 2. to create 397. 577-8, 76 20.22 etc. passim. — to prepare 4216, with the gl. kū sāxt; — to bring about 451, v. ax"àyis- neh; — fräc ~ to put into existence by creation 932, 949. — Av. OP (711 sqq.) lda-; MPrth d?dn dh-; MPrs d'dn dy-, dyy-; Paz. dädan dah- (deh-, dih-); NP dadan dth-.
1324:ing duš-kanik (an independent w. "duš does not exist), but perhaps meant as dust-tar, NP dust ‘foul, ugly’, — Paz. doši ‘folly’ (SGV X, 58 ete.).
1406:*duš-viyāk [dwSwyd’k] *nasty-smelling, *stinking 859-13-20; Paz. substitutes duš- gand. — Y suppose viyāk < *vayäk, pt. of Av. (1406) va- ‘to blow’ (Skr also ‘to smell’) whence Av. vayu-, v.S. v. vāt; Mir vénik, NP bini ‘nose’ < *vayana-.
1426:3.8 [the figure l; -’y, -y, -yh] the enel. indef. art.: tigr-é [-1] 339; duxt-ē [BRTH- ^y] 14%; gad-ē [gt'-”y] one stroke with the mace 312°, 4 ēvak-ē [HD-wk!-y] one fourth 998; vāt-ē [-1] 4 hubod 73°; hec ctš-ē [-l] nö 16%; har kas-ē PYS-1] 10018; and cand yašt-ē [-1] 651°; pat har 40 sal hac zan-ē u mart-é frazand-é [al -ē's spelt -1] zāyēt every forthieth year a child is born of a woman and a man (= of one couple) 8622-23; 6 artestäreh for 6 artēštār-ē 4517. — Identical with ?e; MPrs ‘yw placed after its subst.; Paz. -é, NP -é. — The spelling [-1] is sometimes erroneously used for other suffixes -é: mēd4-1 = mode cas. obl. 72??; har marg- arzanik+-1 = -aržānīkē for the abstr. -arzanikéh 10199.
1498:frācēh [pr'eyh] 1. paž ~ only emphasizes the prev. frāc 52%, v. s. v. pat. — 2. subst. appearanče, the coming into existence 3927 = pat-fräceh q. v.).
1541:frasang [plsng] a parasang, the Persian league, estimated at an average of 6232 m., but varying in length (31/,-4 English miles): 719. 89.6, 7225, 937-11, 9623, 9817, 11471. — OP *frasanga- borrowed in Gr as rapacodyyns, Paz. NP farsang; NW form *frasaxa-, Arm. lw. hrasax, Syr. lw. prsh’, Talm prse, Mand prs’, Arab fjarsax-. V. Christensen, Iranier 283; How and Wells, Comm. on Herodotus Y, 161; EI? II, 832.
1543:Frasiyak [pl’syd’k, -sy’k], Fräsiyäp [pl’syd’p'], Frāsyā [Paz.] n. pr. 4614-16, 783. 113%, 116%. 1179 = Frangräsiyäk ete. (g. v.). - NP Afräsiyäb.
1554:fratom-danišn [~-d’n’n'] whose know- ledge was the first (existing), pl. cas. obl. ~-dn those who received the first know- ledge (of the Zoroastrian religion), defines poryotkésan 62}.
1750:h- (HWH- ; 3d p. sg. "YT', neg. L'YT', inser. and Ps. ^Y TY, L'YTY 2nd p. pl. enel. -ét in amahraspand-é 58"; forms v. I, 175] to be, only in the pres. ind., subju. and opt., other forms from bütan (q. v ): l. as an independent vb. in the 3d p.: exist(s), e.g. hast hàn ke ahlayeh the One who is Righteousness exists 57°; héc ke but hénd u hec ke bavénd u h&c ke hend all who have been, and all who will be, and all who exist (now) 6417-18, cf subst. hast and nesteh; im roc 7 mähakän hast tdi ... to-day it is seven months since 1011-12. kë hast ke ...? who is there who ...? 257-7; andar Ērān-šahr asvār-ē nest ke ... in Eran-shahr there is no horseman who ... 15; hast 4-8 ... u hast 1-§ ... u hast i .. . there is some (of it) that ... and there is some (of it) ... and there is some (of it) that... = part of it... part of it... ete. 9317-18.26; hast kč-š veš, hast ké-§ kam some have more, others less 96°; astömandän mar- tömän (gen. part.) hast i ... of earthly men there are some who 10519; hast <a> šāhān šāh, hast <i> kesar some belong to the King of Kings, others to the Emperor 11519-20; nē hast kū there is no place where, nowhere 611°; hast (i) ka there is a time when, sometimes, at times 7725-26, 8122, 12018-1?; — with prev.: šusr i Gayomart cis andar hast there is some part of the sperm of G. in it 9422-23; kū-š ataxš andar nést where there is no fire 3721, — 2. copula, with a noun, a pron., or a prep. -- subst. as its complement, pas- sim; the 3d p. sg. ‘is’ is very often not
1815:'he will always be', thus: the guality of having eternal, future existence (Arab ’abadiya) 63°.
1816:hamé-bitéh [hm’y bwtyh] abstr. of the sentence hamé bit ‘he has always been’, thus: the quality of having existed from eternity (Arab ?azaliya) 63°; cf also hastéh.
1952:hast PYT'] 1. pres. 3d p. sg. of h-, g. v. — 2. as subst. pl. hastän those who exist 578; 5518 v. bavētān. — 3. abstr. subst. existence, mode of existence 312. 4218, frac hac ~ raft he disappeared 501,
1953:hastčh [^YT'-yh] 1. abstr. of hast 2: pat ~ hamē būtēh hamé bavētēh in the quality of existing, of always having existed and destined always to exist 63°, v. bavetän. — 2. the quality of having existence, reality 8418,
1954:hastik [’YT'-yk] possessing real existence 5627, 571. .
```


## [2026-09-04T19:05:06.301Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -nE \"^asmān|^asmān \\[|^sang \\[|^sang\\b\" NYB_vol2_glossary.txt | head -10; echo \"---grep asmān entry\"; grep -n \"asmān \\[\" NYB_vol2_glossary.txt | head -5"
}
```


### [2026-09-04T19:05:06.387Z] TOOL RESULT

```
---grep asmān entry
```


## [2026-09-04T19:05:08.336Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"asmān\" NYB_vol2_glossary.txt | head -8"
}
```


### [2026-09-04T19:05:08.413Z] TOOL RESULT

```
1123:cigon [cygwn] adv. and conj. A. interrog. adv. how? 1. direct interrogation: nun ~ kunom ?] 272; asmān ~? 921; exclama- tory: how...! 614. — 2. indirect inter- rogation: äkäh hom ku ~ hän 571; vēnēt ki Bastvar kārēcār ~ nev kunēt saw how valiantly B. fought 2815-16; ~ 6, 6 ham pursem 57°, andar Garodman dätistän ~, api-m nē dit 527-3; ete. — B. rel. adv. so as: l. har 3 šap x"amn ~ dit Estät ... guft such as he had seen it 2%; 215, 48, 520, 4527, ete.; introducing quotations: ~ den göbet 387, ~... paitāk ku 4571-5, etc. passim; parenthetic, e.g. 7718, 818%; — with a demonstr. antecedent: hamgönak hast ~-am guft 1216-17; šmāh bat ētūn m to gobeh 2329; 4524-25, 782.4, etc. — 2. with- out a clause, used prepositionally: as, as (for instance), as it were, like: ~ agäh aköc martom 2678-27; ~~ martom kë šarm 43913; 12813; varcāvandān i ~ Yam u Frétón ... 45°; hàn 4 ~ én such a th. 438; namely 1078; — with a demonstr. antecedent: &ön ~ āluh-ē 9%; eton ~ to 1516; ét6n but ~ amahraspand-ē 38°”; — čton, or ógón, homänäk (a. v.) ~ 69%, ete.; mänäk(k)äi (g. v.) i õi ~ ke pus... bare (opt.) 418. — C. conj. 1. causal be- cause: ~~... hdn mazantom bit 613-4; 1081. 11812; almost as a rel. pron. with a sec- ondary causal sense (as in Lat. quippe qui): 6 xuähar i x*"e$, ~ zan 4 Artaxsér būt, nämak nipišt 822; 718%, 7916. 116%. 11819; — hac han ~ in view of the fact that, considering that 38. — 2. temporal as soon as: 6°. 15°. 44°, more emphatically ham-~ 1317. - 3. ~ ka as if 11214.17, 10120722 — 4. almost = that 8722. — MPrth cw'gwn; MPrs ewn (read ci'on < *ciwön <
2576:miyàn [myd’n'] 1. the middle, the centre: bun ...miyün... frazdm 81; x"atài 4 ~ i asmān 78; han-tāi 6 ~ van to the middle of the tree 415; andar ~ 4 asmän 865; hac ~ dp from the middle of the water 564; — pat ~ kartan to make manifest to all, splendid 67°; 6 ~ apa- kandan to spread, disseminate 10715, — 2. prep. between: + smäh u oan damik i 30 frasang 8%; vimand i ~ Eran u Türän 4519-311; in the middle of 4815, 865. — Av. (1115 sq.) Tmaiöya-, (116 sq.) matčyčna-; MPrth mdyn; MPrs my; Paz. NP myàn.
```


## [2026-09-04T19:05:16.610Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 248 249 250 251 252 253 254; do echo \"=== leaf $L ===\"; awk -v N=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==N {print substr($0,1,700)}' BQT_v1_pages.txt; done"
}
```


### [2026-09-04T19:05:18.283Z] TOOL RESULT

```
=== leaf 248 ===
رود 5 با زای هوژ بر وزن ساطور »
صاحب حرص و آز را کونند که حریص باشد .
این لفظ م رکب است حمجو گندور و رنجور -
و بممنی هوسناله هم گفته‌اند ؛ و بر وزن داد کر
آمده‌است که ساحب و خداوند حرص و شره
واز باشده چه آز بمعنی حرص است و وربمعنی
صاحب وخداوند . *
]دوش « بروزن‌آروغ؛ بمعنی پیراستن
باشد بعنی برمدن شاخهای ز.ادنی - و بعضی
ختقوای را کرت مرت رد و وفیره
بربده باشند ؟..
7و با زای فارسی بروزن و ععنی
آزوغ ا
=== leaf 249 ===
۳ آسا
آن را « حب الآس » خوانند ۴. کونند عمای
موسی علیه السلام از چوب آس بوده » ودر مك
روم درخت آن از جاهای دمگر بزرکتر مشود »
وشکوفةً آن خوشبوی میباشد » هرک سکه آنرا
ببوبد و جخواب رود البته محتلم شود - و مق
علرا نیز گون که درشان ائگین مانده باشد -
و بقیةٌ خاکستر را نیز گویند که در جایی مانده
باشد - و نشانهای عمارت خراب را عم کفته‌اند -
و در هندی بمعنی امیدواری باشد - و کمان
تراندازی را یز گونند 
=== leaf 250 ===
آسیابان باشد چه آسیا راآس میگویند .
آس بری « بکس تالث و فتح بای
ابجد و کسر رای قرشت با عشدید بتحتانی زده .
مورد صحرابی است و هترین آن رومی‌مباشد »
طبیمت آن کرم و خشك است و علت صرع را
فایده دهد و آبرا «موردأسفرم» نز کوشد .
آ ستان - بسکون ثالت و فوفانی بالف
کشیده بر وزن آسمان » معروفت که کفشکن
و مان در خانه باشد وآنرا «آستانه» حم گوبند
و بر پشت خواییدن را نیز گویند وبکسر ثالث
استخراج سالهایمخو�
=== leaf 251 ===
بمعثی بطانه است - و کنابه
باشد.
اسقی » بر وزن راستی » بمعنی آستن
است که مخفف آستن (۱) باشد.
] سقیم » با میم» بروزن و معنی آستین
است - و خونی باشد که از جراحت (۲) رود و
بسی جراحتی را گونند که مندمل شده باشد و
چرك در میان آن مانده باشد ۴ - و سرمابی را
نیز گوبندکه برجراحت زند وجراحث ببب آن
آما ی کند - و بممنی دهان ظروف و اوانی حم
امه ات ۷
ستبی افشا فدن -کنابه ازترك دادن
و انکارنمودن باشد - و یمعنی رقص کر
=== leaf 252 ===
آسمار با میم بروزن شاخار , ورخت ]| کهکثانرا کویند و بعربی مجره خوانند .
وود 1 کرت و مرش ان ا: آ سهان‌ور بسمان - این مثل ات
آیما .۱۰ ۳ زااد ب درجایی کون که شخصی درب رآبر معفول‌جواب
| سهان " ه ممررفت وبعربی سما وفلك ۱
نادرست (۱) گومد .
خوانند» ومعنی ترکیبی آن آسیا مانند است . : ِ
بابار گردیین چه آسیا را آی یز کوشد ۴- سها 4 » بروزن‌آسنانه» سقف خانه را
ویام فرخته‌ایست که مو کل است بر ممات واو را کونند . 
=== leaf 253 ===
اندلختن و عداوت بهمر‌سانبدن علق باو دارد .
ستستان » بکس تون بر وزن
کافرستای ؛ غلم پدر زن وامق ات و او عاقبت
بردست وامق کشته شد ۱ . 3
سو ده - بر وزن آلوده » بمعنی بی
زحمت و بی‌عزاحمت ومی‌مشقت باشد - و بمعنی
خقته و خوایده هم آمده است , #
آسه ۴ - پروژن کاسه »کدت و زرات
باشد - و زمینی را نی ز کون که مجهت زراعت
کردن عستمد و مهیاکرده باشند - و دوائی حم
آسیا ۴ - متروف لت هو آن نکن
باشد مسطح و مدور بربالای �
=== leaf 254 ===
است که موسی علیه‌اللام را پرورد . ۶
]شام - بائن .قطمدار بروزن بادام ؛
خوردن و آشامیدنکم و اندك را کویند و بعرمی
قوت لایموت خوانند ۴ - و بمعنی وشیدن
و آشامیندن آب و شراب و مانند آن باشد -
وامر بان هعنی هم حست عتی بیاشام و بنوش -
و آشامنده را نیز گوبند که فاعل آشامیدن
باشد ٩‏ - و ام ولایتی است مان مشرق وشمال
بنگاله و درآ ئولابت عود بفابت خوب میشود
و آیرا نیز گویند که در وقت برنج پخته شدن
از آن کرن
```


## [2026-09-04T19:05:34.779Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json; d=json.load(open('refs_online.json'));print(d['BQT']['page_offset'])\""
}
```


## [2026-09-04T19:05:36.136Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==253 {print}' BQT_v1_pages.txt; echo \"#### leaf 249 full\"; awk 'BEGIN{RS=\"\\f\"} NR==250 {print}' BQT_v1_pages.txt"
}
```


### [2026-09-04T19:05:36.308Z] TOOL RESULT

```
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
```


### [2026-09-04T19:05:37.871Z] TOOL RESULT

```
آسمار با میم بروزن شاخار , ورخت ]| کهکثانرا کویند و بعربی مجره خوانند .
وود 1 کرت و مرش ان ا: آ سهان‌ور بسمان - این مثل ات
آیما .۱۰ ۳ زااد ب درجایی کون که شخصی درب رآبر معفول‌جواب
| سهان " ه ممررفت وبعربی سما وفلك ۱
نادرست (۱) گومد .
خوانند» ومعنی ترکیبی آن آسیا مانند است . : ِ
بابار گردیین چه آسیا را آی یز کوشد ۴- سها 4 » بروزن‌آسنانه» سقف خانه را
ویام فرخته‌ایست که مو کل است بر ممات واو را کونند . 0
" عزرائیل خوانند - ونام روز بیست وهفتم باشد از آسمانی ر بان س یعنی زبان آسمانی
هر ماه شمسی و تدییر و مسالح روز مذ کور باو | که مراد از آن زبان ملاشکه باشد .
ملق رد دج ریت وم | هتفرن دشن منک
شمی‌را آسمان گوند ۴ وافداعلم . بغربب و خدعه باشد - و سرگشته و حیران را
سمان مت سس ون رشق یز گوبند .
ایجد .فك دهم را گوید و آن را نك انا آسموغ ۴ - بر وزن آبنوغ » دام
خوانند . دبوست از منابمان اهرمن که سخن چیتی رفتنه
انگیزی و دروغ گفتن و میان د مکس جنگه
(۱) چب ۲ , چش : جواب تا در مقایل .
- اوستا 358080 بمعنیسشکه « بارتولمه ۲۰۷ و ۲۲۰» رگ : آس . چون آسمان را
بان سنکی پنداشته اد از اين رو نام آن در اوستا و پارسی باستان نیز 2511120 میباشد که در
پهلوی و فارسی آسمان کویم « خرده اوستا ۹ ح | » پهلوی 257028 « منای ۲۹۸ *.
کیلکی 250020 , فریزندی 250100110, بر نی 2519110 نطنزی 251۳020 « . اس ۶۲۸5 :
2 0 , سنانی 25۳027 <4 .۲ ص ۱۸۰ وی 0 .۰ 2570210 ۰
بازغلامی 25۳000 , سریکلی 82511188 «گربرسن ص ۰*۷۲ تهرانی 2560008 .
۴ - این توجیه درست نیست. ۳ - آسمان در مزدینا مقدس است وچندبار با زمین
یکجا نام برده شده ( چنانکه در نشتر بشت بند ۸ ۰ مهربشت بند ٩۵‏ وغیره ) . بلر ها از زمين
و آسمان ؛ ایزدانی اراده شده که بنگهیانی سیهر و خالك کماسته شده‌اند : همه ساله زاشتاد واز
آسمسان نن‌وجانت باشادی وکاعتان ؟ (فردوسی بتقل جهاتگیری ) درستا؟۱ بنده ودر دوسپروز؛
کوچك و بزرک بندهای ۷۷ و ۲۸ هردو ابزد آسمان و زاعیاد (زمین) درردبف فرشتگان ماه
باد شده اند . نگهبانی روز یت و هفتم هر ماه با ایزد آسمان است . ابورسسان بیروئی دد
فهرست روز های ایرالی این روز را «اسمان» و در فهرست سغدی «سمن» و در فهرست خوارزمی
۶ اسمان » باد کرده . « زرتشتان امروز تیزآنرا ۶ آسمان » خوانند . «روژ شماری۱۲-۱» نطبیق
ایزد آحمان باعزرائیل مأخذی صحیح تدارد . ۴ - <- آشموغ , اوسنا 3511610082138 , پهلوی
۵ با 2511001181 لفة بمعنی بر همزننده «اشا» ( راستی) و غالبا در اوستا بمعن ی کمراه
کننده اسث . در هرهزدهت بند*۱ درتفیر پهلوی ( زند ) همین بند » سه قسم اشموغ تشخیص
داده شده : نخست فربفتار» دوم خود دوستار ( خودپرست )» سوم فربفته یعنی کسیکه بغربفتاری
دل‌دهد و وبرا پیروی کند « خرده‌اوستا ۷۳ * :
گفته اش جماتگی دروغ بود او سخن چین چو آسموغ بود. طیان « لفت نامه > .
#### leaf 249 full
۳ آسا
آن را « حب الآس » خوانند ۴. کونند عمای
موسی علیه السلام از چوب آس بوده » ودر مك
روم درخت آن از جاهای دمگر بزرکتر مشود »
وشکوفةً آن خوشبوی میباشد » هرک سکه آنرا
ببوبد و جخواب رود البته محتلم شود - و مق
علرا نیز گون که درشان ائگین مانده باشد -
و بقیةٌ خاکستر را نیز گویند که در جایی مانده
باشد - و نشانهای عمارت خراب را عم کفته‌اند -
و در هندی بمعنی امیدواری باشد - و کمان
تراندازی را یز گونند ۴ .
سا - با سین بالف کشیده , زیب‌وزینت
و آرایش باشد - و بمعنی دهان دره عم اس ت که
خ ازه باشد (۲) و بعربی « تشاب * خوانند -
7 بنه با زای قارسی بر وزن آبینه ء
آلتی باشدازفولاد که سنگهآ سا رابدان تي زکنند.
"س ۱ ۰ بر وزن طی. مطلق آسیا را
کونند خواء بدست گردانند و خواه بآب و خواء
بیاروا . وآن سنگی است دور وسطح - ولرم
شدن و خرد گردیدن دانهُکندم و جو را یز
کویند در زبی آسیا - و نوعی از ریحان باشد
بغایت خوشبوی (۱) - و نام جانورست سفید و
سر دم او سیاه میباشد و از پوستش پوسنین‌سازند
و آنرا بعربی « فاقم » خوانند - و شتربرا نیز
کونند که موی او ریخته باشد - وفام قربه‌ایست
ازقرای فاری - ودرتر کی نام شهریست از ولامت
قبچاق - و در عربی درخت مورد است و بار وبر
۱ - ساتسکرت 4580 « وبلیایز ۱۱۲ : ۳ »: اوستا 280020 و2581 بممنی سنگه
+ پارتولیه ۲۰۷ », آس در لفات کپ آسیا و آسياب و بادای وخرای و دستای و پادای دیشه
میشود « خرده اوستا ۱۷۷ ح | *. ۴ - انامه کب۲ د تابتی ۱۵۷ >
۴ - آ سکردن » سودن و خر دکردن .
بقبه از سفحهٌ ۳۸
اسث که در.کوه مسکن دارد ودیوان را بیاری خود میطلبد . اهی رعد سیاء بوران وطوفان است که
با زاران حلقه و پیج و تاب بر فراز قله کوه می‌پیچد و دبوار ماشد بسوی آممان بالا میرود »
ایندره 19012 - رب‌النوع رعد - با او مصاف دهد واورا بکشد. درر بگه ودا بارها از اين مبارزه
سخی رفته است و قیناً ماری که در اساطیر وادیبات حماسی و انانه عای آغلب مثل موجوداست
حمان اهی با اژی آربائیان قدیم است که متدرجاً علت تشبیه که ابر های سیاه باشد از میان رفته,
مشبه‌به نی مار با آژدهای بدکار درخاطرها محفوظ مانده است. داستان اژی‌دهاك نیز با این‌اضانه
مرتبط است #مزدیتا ۳۹-۳۵ .
»آژی‌دهاك _ 02812 از۸۵ ( جزء او آن همان اژی ۳ اهی است )که در
ادبیات اسلامی ضحاكشده . در ودا افسانةٌ تراع مصهانعع1 با مار سه سرآمده وهمن دانان حد
اوستا صورت منز؛ 110212082 ( < فربدون ) با هار سه سر شیبا
تاععو۷تاید ۳۱۱۵۵۲60۵ 122۳812 ۸ آمده. فردوسی‌دز شحاك رابنام‌اژدها میخواید:
نهان بود ( جمشد ) چند از دم اژدها ( ناه )
فرجلم عم زو نيامه رها « شاهنامةٌ یخ ج | ص۳4 »
(خورشگر هرروز مردی‌جواند) بکشتی و مفزش برون آختی
مرآن اژدها (ضحال) را خورش ماختی «ابسناً ص ۳۵ >
و نیز او را «ازدهافش؛؟ و «اژدهایکر» میشواند . لمزدستا ٩۳۱‏ .
```


## [2026-09-04T19:05:58.146Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 631 632 633; do echo \"=== leaf $L ===\"; awk -v N=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==N {print substr($0,1,1800)}' BQT_v2_pages.txt; done"
}
```


### [2026-09-04T19:05:59.719Z] TOOL RESULT

```
=== leaf 631 ===
                                                                                                       ‫—‬

           ‫سهام بممنی آش هم آمده است"‬
                                    ‫چ‬                         ‫است که در آتش متکون میشود ‪ .‬گوبند مافند‬
 ‫‪ = 3‬بفتح اول وکاف فارسی‬                                      ‫موش بزرکی است وچون ازآتش برهیاً بدمیمیرد‬
 ‫ااستهدوراز ‪ ۴‬که‬         ‫رامی‬
                            ‫ه‪,‬‬  ‫و بعضیکوبند همیشه درآتش لیت کاهی بر بالف کشی‬
                              ‫شده‬
 ‫دختر پ"ااده افجا را رستم خواست و سهراب‌ازو‬                   ‫میا بددر آلوفت او را میگیرند و از پوست او‬
‫بوجود آمد ؛ و پم انی حم گفته اند و درىن‬                        ‫کلاء و رومال میازند وچون چر کن میشود در‬
‫زمان آن شهر را رامهرمز خوانند و عوام رامز‬                      ‫آتش میاندازند کچهرای اومیسوزد وپاكمیشود؛‬
‫گوبند ‪ - .‬و بعضی کوبند نام شهپری است در‬                       ‫و بعضی گوبند بصورت سوسمار وچلپاسه است از‬
                                           ‫توران ‪.‬‬
                                                              ‫پوست اچوتر سازند تاگرمی را نگاه دارد و از‬
 ‫د بفتح اول والی و نون‌مضموم‬     ‫سمنو ‏‬                        ‫موی او جا�
=== leaf 632 ===
  ‫‪۱۱ ۹۸ -‬‬                                                                                               ‫سمور‬


                        ‫کردن وبویدن باشد‪.‬‬                                           ‫ید‬       ‫سمو ر‬
 ‫سمیر = بنتح اول بروزن صیرا ‪.‬شاخی‬                                                       ‫بر وزن تنور» جالوری‬
 ‫رکوابند که بدان حجامت کنند ‪ -‬و نام موضعی‬                                           ‫است‌معروف که‌ازیوست‬
‫است درراه مکهٌ مه‌ظمه ‪ -‬وبشم اول و فتح ثالی‬                       ‫سمور‬                    ‫آن بوستین‌سازند ‪5‬‬

         ‫ام مهین بانوی (ش‪)۷‬یعرمین باشد ‪٩‬‏ ‪.‬‬            ‫سمو ر لبود = سمور معلوم است‌بکس‬
 ‫سهیر ‪ = ۵‬بفتح اووثلالیتحتالی رسیده‬                    ‫ب)اوی حطی (ب‪۲‬و)او کشیده‬       ‫بای ابجد (‪۱‬‬
 ‫وای بی‌نقطۂ (‪ )۸‬مفتوح بمیم زده »ناحیتی‌است‬
                                          ‫ر‬            ‫و برای قرشت زده » بلغت بوفالی کرفی‌صحرابی‬
 ‫ماین عراق و فاریکه آب ملخ را اآنز‌ناحیت‬                                                                ‫باشد ‪.‬‬
 ‫آورند‪ .‬گویندوقتی که این آب را مذیر ندمنباید‬           ‫سمو زر سه ه بکر رای قرشت (‪)۳‬‬
‫که طرف آبرا بر زمين نگذارند و نگاه بع�
=== leaf 633 ===
                                              ‫بیان ليست ویکم‬
          ‫ونایت‬
              ‫در سین بی نقطه بانون مشتمل برربکصد وییست وهفت لغت ک‬
 ‫سناك = بفتح اول سوکرن آرخکه دال‬                          ‫سن = بفتح اولبروزن من » رستنیی‌باشد‬
 ‫بی لقطه باشد بروزن مواد " بمعنی‌بیاروفراوان‬               ‫که بردرختها پیچد و بعربی عشقه خواناد ‪- ۷‬‬
‫و وافر بود ® ‪ -‬و یکی از عيوب ملقبة قافیه هم‬               ‫و یمعتی سان هم هت که مثل و مانند ورسم‬
 ‫ردف اصلی باشد‬       ‫و آن عبارت از اختلاف‬          ‫هت‬
                                                           ‫لويزه‬      ‫‪-‬ن‬
                                                                       ‫ا‬‫ن‪۴‬‬
                                                                         ‫ساشد‬
                                                                            ‫وش ب‬
                                                                               ‫وادت و طرز و رو‬
                                                                                             ‫ع‬
 ‫چون داد ودید ودود ‪ - ۱‬دورعربی‌بمعنی‌مخالفت‬               ‫رایز گوبند ‪ ۴‬و‪-‬بترترک بیهمنی‌نو دباشد که‌عربان‬
                                  ‫آمده ات ‪. ۷‬‬

 ‫سنار ‪ -‬بفتح اول بروزن کنار » تنکه‬
‫ان بود وکل‬
```


## [2026-09-04T19:06:15.385Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"سنگ\" BQT_v2_pages.txt | head -5 >/dev/null; python3 - <<'EOF'\nimport re\nd=open('BQT_v2_pages.txt',encoding='utf-8').read()\npages=d.split('\\f')\nfor i,p in enumerate(pages):\n    if 'سنگ' in p and i>600:\n        print(i, p[:120].replace('\\n',' | '))\n        if i>645: break\nEOF"
}
```


### [2026-09-04T19:06:17.114Z] TOOL RESULT

```
605                                           ‫بیان چهاردهم‬ |               ‫بر بانزده لغت‬          ‫سین بی‌نقطه باغین نقطه‌
613                                                                                              ‫‪۷۱۷ 6-‬‬ |  | ‫و شروع بحر کنن
614             ‫‪۱‬‬ |             ‫= هی‬                                                                                    
623   ‫سلشوق‬                                                                                               ‫‪۱‬‬ |           
626   ‫‪-۱۱۲ -‬‬ | ‫آن گذارند ‪ -‬و هر سبد را لمز‬                 ‫که چزها در‬            ‫وثانی‌درعربی‬    ‫ویفتح اول‬      
639   ‫سنگه پرستوك‬                                                                                ‫«‬ |                      
640  ‫‪Aha‬‬                                                                                               ‫سنگه برشیشهزدن‬ | 
641   ‫منگه روشثابی‬                                                                         ‫سپا‬ | ‫بشکل مخروطی برهوا برد وب
642  ‫‪ ۷ ۷‬اس‬                                                                                                   ‫سنگه زخم‬
643 ‫و کوچك‬   ‫و دام نوعی از غله است و آن سل‬                    ‫سنگ شکن = مخفف منکه اشکن‬ | ‫میباشد ‪ -‬و نام مرغیست کوچك و
644     ‫‪= ۱‬‬    ‫حس ‪۵‬‬ |  |  |  |  |   ‫دو کس کرده‌اند‪ :‬مردی و زنی؛مرد مازلین وزن‬                   ‫شزد‬ |                     
648  ‫‪‎6‬زب ‪٩ ۱‬‬ |  |  | ‫سید‬       ‫وی‬ |            ‫عن‬‫عوزن‬ |                 ‫بر‬         ‫اول ثوالی‬     ‫توح‬ |
```


## [2026-09-04T19:06:23.291Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8').read()\npages=d.split('\\f')\nfor i in (637,638,639):\n    print(\"=== leaf\",i,\"===\")\n    print(pages[i][:2500])\nEOF"
}
```


### [2026-09-04T19:06:24.954Z] TOOL RESULT

```
=== leaf 637 ===
    ‫سندل‬                                                                                   ‫‪۳۷-‬ات‬
                                                                                               ‫‪۱‬‬
    ‫نافع بواسیر باشد ‪ -‬رونگه سرخ را لگیوزبند‬        ‫خانه را خبردار کند حلقه را بر‬      ‫صاحب‬      ‫خواهد‬

‫و دبتش برنگه زرد خود ظاهر است » ونفرقة‬                                       ‫آن تنگة آحثی زد ‪.‬‬
‫میان میندروی وکاه‌ربا ابن است که کامربا راچون‬      ‫»کر اول و سکون الی‬
                                                                    ‫سند با‪ ۱ ۵‬ب‬
 ‫دآرش‌نهند از آن‌بوی مصطکیآید وازسندروس‬            ‫لام‬   ‫بالف کشیده و بدال زده»‬      ‫وئاك و بای بد‬

                           ‫بوی بفایت لاخوش ‪. ۴‬‬      ‫عملی»‬   ‫وحکمت‬    ‫تصایح وشدیات‬     ‫در‬   ‫کتابی است‬


‫سئدر ه ‪ = ۲‬بر وزن چندره ‪ ۰‬بمعنی‬                                     ‫و حکیم ازرقی بنظم آورده ات‬


‫‪-‬‬          ‫با‬
            ‫ربیه‬
               ‫هد ش‬
                  ‫کباش‬
                     ‫بفی‬
                       ‫سندروی است که صم‬             ‫بفتح اول‌بروزن بندره صمفی‬     ‫ر ‪= ۳‬‬    ‫سنل‬

‫و بم‌عنی حرام زاده گهفمته‌اند ‪ ۱‬؛ وباین معنی‬                              ‫باشد زرد وشبیه بکاه ربا‪.‬‬
                ‫بكر اول و ثالث نیز آمده است ‪.‬‬      ‫سید ر و س ‪ = ۳‬بفتح‌اول وئاك وسکون‬
‫سنف‌ل = بفتح اول و اك و سکون‌الی‬                    ‫ثالی و رای قرشت بواو مجهول رسیده و بسن‌بی‬
‫ولام » کفش و پایافزار را کوبند ‪ - ۷‬و بیعقل‬          ‫است کهصمفی باشف‬     ‫نةمله رده » یمعنی اول صنثر‬

‫و ابله واحمق را نیزکفته‌الد ‪ -‬و کشتی کوچکی‬           ‫شبیه بکاه ربا وروشن کمان را ازآن یدز‪.‬دخاش‬


     ‫‪ - ۱‬مسمودی‌در «مروحالذمب» درباب اخبار هند وملوك قدیمة آن کوید‪« :‬ثم ملك‌بعده‬
     ‫کوش فاحدث هند آراء فی الدبانات على حب مارأی من صلاح الوقت و مابسمله من‌التکلیف‬
    ‫اهل العصر وخرح من مذهب من‌ساف وکان فی‌مملکته و عصره سندباز وله کتاب الوزراء السبمة‪:‬‬
     ‫والمملم والفلام وامرأةالملك وهذا [هو] الکتاب المترجم بکتاب‌السند باذ» و ابن‌الندهمدرالفهرست‬
     ‫ولخلف فيه مثل الخلف فكىليلة‬      ‫كوبد ‪ :‬ک«تاب سندبان الحكيم وهونسختان كبيرة وصفيرة ا‬
     ‫ودمنه وااغالب والاقرب الی‌الحق‌ان بکون‌الهند صنفته»(الفهرست چاپ فل وکل ص‪. )4۰۳-۵۰۳‬‬
      ‫درهرصورت بك نسخهٌ پهلوی ازابن کناب تازمان سامانیان وجود داشته و در عپد نوح بن منصور‬
     ‫سامانی (‪ )۱۹۳-۷۸۳‬بفرمان وی خواجه عمیدابوالفواری قناوزی آنرا از زبان پپلوی بپارسی‬
    ‫واد سنهٌ ‪ ۰۰‬ه‪ .‬بهباء الدین محمد ظهیری‬   ‫ترجمه کرد و این نخه ظاهراً از ميان رفته و در ح‬
    ‫سمرقندی دبیرطمفاح خان ابر
=== leaf 638 ===
     ‫)‪۱‬ات‬

 ‫ونام درخت بلوط هم حت بلفت اهل شام ‪. ۷‬‬                           ‫باشد که آنرا از کنار دربا بر از آب شفرین‬
                                                                 ‫و اسباب و مابحتاج کف کرده بکشتی‬
‫سنز = نم اول و کر ای وسکون‌زای‬                                                                          ‫بزرگه در نف‬
‫تطه‌دار » سیاه داته را گونده و آن تخمی باشد‬

                       ‫که برروی خمس نان باشند ‪۰‬‬                  ‫= بالام بروزن کمترك‪,‬مصنر‬            ‫سند لت‬
                                                                             ‫و با افزار است‪.‬‬       ‫سمفال باشد که کش‬

                                                                 ‫وزن مزبله «یمعتی سدد لت‬       ‫ص‬    ‫سند له ‪-‬‬
‫بالف کشیده بروزن دندان » سخن غیرفصیحوبلیغ‬
                                                                                ‫و دای اف ار باشد ‪۹‬‬       ‫است که کف‬
                                                  ‫را گوشد ‪.‬‬

                                                                 ‫سند لی ‪ » ۲‬بروزن جنگلی »کرسیی‬
‫ارزن »‬    ‫زرن‬
            ‫ول ب‬
               ‫ستس ‏‪ = ٩‬بفتح او‬
‫بمعنی سنسان است که سخن غير فصیح و بایغ‬
                                                                 ‫وای افزار را ببارلای آن‬
                                                                                       ‫گروابند که کفش پ‬
                                                                                                         ‫‪۰‬‬   ‫گذار ند ‪۳‬‬
                                                       ‫باشد ‪.‬‬
                                                                 ‫سند و فی ‌ِ بقتح اول و سکون ثالی‬
‫را‬       ‫سنس ر = بر وزن زلبور » خرطوم‬                            ‫ودال بواو رسیده وقاف عکور يبسن بی‌لقطه‌زده‪:‬‬
                 ‫گونند و آیرا فبل ویشه هردو دارلد‪.‬‬
                                                                 ‫راکی باشد‬    ‫‪ ۰‬وان‬    ‫بلفت بونانی سر اج را گونشد‬

‫سکون الی و فتح‬           ‫بضم اول و‬          ‫ت‬    ‫سنه‬              ‫که نفاشان ومصوران بکار بر لد و سوختکی اش‬

‫تالك » زلبور سیاه را گوبند ‪ -‬و بمعنی انگور‬
                               ‫‪۰‬‬     ‫لز آمده اسع ‪۰۱‬‬      ‫سياه‬     ‫حنده؛ سندان‬    ‫‪ 6‬كت بقتح اول بروزن‬         ‫سف‬



                                                                  ‫را گلوزنند؛ وباینمعنی جنماول‌همآ مده‌است ‪۵‬‬
                        ‫وقاف وسکون‌ثالی ورای‌قرشت»‬
                        ‫مرعی‬       ‫وان‬      ‫بمعتی شن
=== leaf 639 ===
  ‫سنگه پرستوك‬                                                                                ‫«‬
                                                                                             ‫ی‪۷‬‬‫‪۱‬‬


 ‫سنگ اسگاف ‪ - ۱‬حجرالا اکن ‪۷‬‬                             ‫‪ = ۱‬بفتح اول بر وزن رنگ ‪,‬‬        ‫سگ‬
 ‫شهگران بدان‬      ‫است » و آسننگی اکستف ک‬                ‫معروف است ‪ ۴‬و بعربی حجرخوانند ‪ -‬وبمعنی‬
   ‫افزار تکینزند‪ .‬سود آن ملاژه را نافع است‪.‬‬              ‫زن‬
                                                          ‫وو‬‫تمکین و وقار و اعتبار گهفمته‌اند ‪- ۴‬‬
  ‫سنگاش ‪ - ۸‬باکان فارسی بورزن‬                                             ‫وکرالی چبزها را گیوزبند‪.‬‬
              ‫پرخاش » بمعنی رشدگه وحسد باشد ‪.‬‬          ‫سنگ [ تش د بمربی‌حجرالنار گوبند‪.‬‬
 ‫سنگاشکی ‏‪ = ٩‬بکر همزه »نام غله‬                         ‫اگرزلی دشوار زايد بر ران او بندند زایدن‌برو‬
 ‫انت ‪ -‬و نام لوعی از خرما باشد که آبراسنگه‬                                               ‫آمان گردد‬

                                 ‫اشکنك خوانند ‪.‬‬         ‫سنگ احمر = بربی حجر الاحس‬
‫‪-‬هایی باشد که‬    ‫سدوارراخ‬ ‫سنگ ان‬                       ‫برنگ مرجان‪ .‬گونند‬        ‫خوالند وان ا‬
 ‫زکیذرگرهای دبوار قلمه سازند ناچون دشمن‬                 ‫ازسموم قانله است‪ .‬يك‌دانک کوشینده‌میباشد؛‬
  ‫نزديك دبوارآبد سنگه و خله و آنش بسررش‬                             ‫ری کته پوس نی انت‬
‫برف انداز و کلوخ انداز هم‬          ‫تی‬
                                    ‫عو‬‫م‪-‬‬
                                       ‫بزلد‬
                                          ‫ری‬            ‫؛ممنی همراه‬
                                                                  ‫سنگار ؟ «بروزن زنگار ب‬
‫ویر کشتی باشد که‬
               ‫آمده است وآن جشن س‬                       ‫و رفیق باشد پس در ایتصورت دوکس که باهم‬
 ‫اندازان‬    ‫در آخر ماه شعبان کنند و آ یر| سنگه‬          ‫بجابی رولد حم منگار بکدیگر باشند‪ ,‬وهمجنین‬
 ‫هم میگویند*‪ - ۱‬و دایمالخمر و شراب خوردن‬               ‫اگردو کشتی در دریا باهم براه رو لد یزهم‌منگار‬
 ‫دایمی را لز کفه‌اندچنانکه مکروزدرهیانه(‪)۱‬‬                                             ‫خواهند بود ‪.‬‬
                                    ‫فاصله نشود ‪.‬‬        ‫‪ -‬را تعریی ‏ حجر ‪-‬‬     ‫سنگ اسینگ‬
‫سنگا نه ه باکاف فارسی بروزن دندانه »‬                    ‫الاسفنج ‪ ۵‬و حصاء الاسفنج خوانند » وآن‌سنکی‬
   ‫ند‪.‬‬      ‫پرنده ایست کوچك و بعربی آنراصموه‬           ‫است که در ميان بوتهةٌ اسفنج بهم میرسد ‪ .‬آنرا‬

 ‫سنگ پسرتو ‪ -‬حجر الخطاطیف‬
```


## [2026-09-04T19:06:32.642Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8').read()\npages=d.split('\\f')\nprint(\"=== leaf 639 tail ===\")\nprint(pages[639][2400:])\nEOF"
}
```


### [2026-09-04T19:06:34.551Z] TOOL RESULT

```
=== leaf 639 tail ===
 که در ميان بوتهةٌ اسفنج بهم میرسد ‪ .‬آنرا‬

 ‫سنگ پسرتو ‪ -‬حجر الخطاطیف‬                              ‫ساشد و با شراب بخورند منک مثانه را‬
‫‪.‬وبند بجهٌ اول اورا چون بگیرند رشکم‬
                                  ‫است ک‬                                                      ‫بربزالد ‪.‬‬


                                                                        ‫)‪ (۱‬چش ‪:‬ميان ‪.‬‬

  ‫‪- ٩‬یسراپ ناتساب ‪ = ۱ ۵2002082‬یسراف هگنسآ ) ( رجح ) ‪‎‬و ‪6۱0208 -‬‬
  ‫و‪ . 806‬اففالی ‪.45 €1‬‬
                     ‫(جر) » پهلوی ‪ 8(0)25‬و‪ 825۰‬کردی ‪5 065‬‬
                                                        ‫( فارسی سنگه ) ح‬
   ‫ورك ‪ :‬تبرکه‬      ‫دو شمان ‪YEV‬‏‬      ‫«اسشق ‪5‬‬     ‫‪ .‬فقس ‪ :‬مدن‬       ‫‪8‬‬      ‫‪gnis‬‏ ‪ ۰‬لي‬         ‫بارچی‬

    ‫‪۵- 6‬؛ ‪ . 0025۱۷ :‬سنکه در بهاوی بمعنی ارزش وقیمت آمده « تاوادبا ‪٤۹۱۰‬‏ کیلکی‬
      ‫ری‬ ‫گ‪. 8‬‬‫ن‪0۵۹‬‬   ‫سانی‬‫ص‪ » › ۵۸‬سمن‬  ‫فریز»ندی ‪ ۰‬برلی و نطنزی ‪ « 8785‬ك ‪۲ ۱ .‬‬  ‫‪8‬‬
   ‫ولاسگردی ‪ » 8085‬سرخهیی ‪.8085‬شهمیرزادی ‪.+ « 8025‬ص‪,»۱۸۱‬دزفولی ‪« 8065‬امام» ‪.‬‬
            ‫‪O‬‏ ودرساختمان بکاز بزلد ‪5‬‬       ‫و محکم که از زمین استخراح‬    ‫مخت‬   ‫جسمی‬     ‫‪۳‬‬

           ‫چوسابه لاجرم بی سنگه ماندم‪.‬‬                     ‫برآن سایه چو مه دامن فشاندم‬        ‫‪۴‬‬

           ‫‪ - ۴‬قس‪:‬سنگم ‪.‬‬            ‫‪۰٩‬‏ ‪.‬‬       ‫نه‬
                                                 ‫ی «‬
                                                   ‫جوی‪.‬‬
                                                      ‫نکنج‬
                                                         ‫کمی‬
                                                           ‫نظا‬
                 ‫‪۲٩ :‬‏ ‪.‬‬
                   ‫©‏ = ‪« Pierre ۳6800۳60 cystéolithe‬دزی جاص*‪۵۲‬‬
   ‫‪ - ۷‬اسکاف (عر) بکرارل کفش دوز وموزه دوز * هرکار گری سوای کفش دوز ”شرج‬
                ‫‪« 5101‬رزی جاص ‪.›“ ۲ : ۱۵۲‬‬               ‫‪۳1۷701181066126 = ۷‬‬                 ‫فاموی» ‪۰‬‬
              ‫‪ - ٩‬رك ‪ :‬سنگه شکن‪.‬‬                   ‫‪.‬‬   ‫‪ - ۸‬از دماتیر «فرهنگه دساتیر ‪۳6۲٩‬‏‬

                           ‫‏‪ ١‬۔ در کیلکی « منک انداز » فلاخنو قلاب سک را گویند ‪.‬‬
```


## [2026-09-04T19:06:55.378Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('BQT_v2_pages.txt',encoding='utf-8').read()\npages=d.split('\\f')\ndef digits(s):\n    return re.findall(r'[۰-۹]{3,4}', s)\nfor i in range(596,650):\n    head=pages[i][:400]\n    print(i, digits(head))\nEOF"
}
```


### [2026-09-04T19:06:56.959Z] TOOL RESULT

```
596 []
597 []
598 ['۱۳۹']
599 []
600 ['۱۱۳']
601 ['۱۳۹']
602 ['۹۳۱۱']
603 []
604 []
605 []
606 []
607 []
608 []
609 []
610 []
611 []
612 []
613 ['۷۱۷']
614 []
615 []
616 []
617 []
618 []
619 []
620 []
621 []
622 []
623 []
624 []
625 []
626 ['۱۱۲']
627 []
628 []
629 []
630 []
631 []
632 []
633 []
634 []
635 []
636 []
637 []
638 []
639 []
640 []
641 []
642 []
643 []
644 []
645 []
646 []
647 []
648 []
649 []
```


## [2026-09-04T19:07:12.852Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sijjil\\|Sijjil\\|sijjīl\\|sanj-i gil\\|sang-i gil\" FVQ_pages.txt | head; echo \"=== leaf 180-182\"; awk 'BEGIN{RS=\"\\f\"} NR>=181 && NR<=183 {print \"=== awkNR\",NR,\"leaf\",NR-1,\"===\"; print}' FVQ_pages.txt | head -80"
}
```


### [2026-09-04T19:07:14.569Z] TOOL RESULT

```
=== leaf 180-182
=== awkNR 181 leaf 180 ===
FOREIGN VOCABULARY OF THE QUR^AN 163
This root H30 is an Aram, formation. Even in 0. Aram, it meant
" prostration of reverence ", as is evident from the X*P30 of Sachau's
Edessa inscription No. 3 (ZDMG, xxxvi, 158 ; cf. Dan. iii, 6). In
later Aram. "120 is to bow down, NT130 is worship, adoration, and
XT*30 ITS an idol temple. Similarly Syr. ror 00 , from a primitive
meaning of " to salute reverentially " (cf. 2 Sam. ix, 6), comes to
mean to'adore, translating both creftco and irpocrKwea), and giving
IZOyyJC and U'rvr 00 adoration, and IjO.^ a worshipper, etc.
It is from the Aram, that we get the Heb. H30 (Noldeke, ZDMG,
xli, 719) and the Eth fll& (Noldeke, New Beitrage, 36), and it was
from Aram, that the word passed into Arabic, 1 probably at an early
period, as we see from the Mu'allaqa of 'Amr b. Kulthum, 1. 112.
(Sijill).
xxi, 104.
The meaning of Sigill in this eschatological passage was unknown
to the early interpreters of the Qur'an. Some took it to be the name
of an Angel, or of the Prophet's amanuensis, but the majority are
in favour of its meaning some kind of writing or writing material.
(Tab. and Bagh. on the passage, and Raghib, Mufraddt, 223.)
There was also some difference of opinion as to its origin, some
like Bagh. taking it as an Arabic word derived from 4\>-w4, and
others admitting that it was a foreign word, of Abyssinian or Persian
origin. 2 It is, however, neither Persian 3 nor Abyssinian, but the
Gk. criyiXXov ~ Lat. sigillum, used in Byzantine Greek for an Imperial
edict. 4 The word came into very general use in the eastern part of
the Empire, so that we find Syr. tpAi^. ifn (PSm, 2607) 5 meaning
1 Noldeke, op. cit. ; Hirschfeld, Beitrage, 41 ; Schwally, ZDMG, Iii, 134 ; Von
Kremer, Streifztige, p. ix, n.
* al-Jawallqi, Mu l arrab, 87 ; al-Khafaji, 104 ; as-Suyutf, Itq, 321 ; Mutaw, 41. W. Y.
Bell in his translation of the Mutaw. is quite wrong in taking the word J,>- j to mean
part, portion, blank paper. It means man as is clear from LA, xiii, 347.
3 Pers. A*^' me &ning syngrapha indicis, is a borrowing from the Arabic, Vullers,
Lex, ii, 231.
4 Vollers, ZDMG, 1, 611 ; li, 314 ; Bell, Origin, 74 ; Vacca, El, sub voc. ; Fraenkel,
Vocab, 17 ; Fremdw, 251.
8 Noldeke, Neue Beitrage, 27.
=== awkNR 182 leaf 181 ===
. 164 FOREIGN VOCABULARY OF THE QUR AN
diploma, and Arm. "/?/_ meaning seal 1 It may have come through
Syriac to Arabic as Mingana, Syriac Influence, 90, claims, but the
word appears not to occur in Arabic earlier than the Qur'an, and may
be one of the words picked up by Muhammad himself as used among
the people of N. Arabia in its Greek form. In any case, as Noldeke
insists, 2 it is clear that he quite misunderstood its real meaning.
xi, 84 ; xv, 74 ; cv, 4.
Lumps of baked clay.
The last of these passages refers to the destruction of the army of
the Elephant, and the others to the destruction of Sodom and
Gomorrah. In both cases the J-** is something rained down from
heaven, and as the latter event is referred to in Sura li, 33, we get the
equivalence of J-s*^ ^U, which gives the Commentators their
cue for its interpretation. 3
It was early recognized as a foreign word, and generally taken as
of Persian origin, 4 Tab. going so far as to tell us ^Ux-M, iv-jUJl j*)
\j, which is a very fair representation of L-X-^ and JJ (Fraenkel,
Vocab, 25 ; Siddiqi, StiMen, 73). cX^- meaning stone is the Phlv.
S)0 san 9 from Av - >*** asan > 5 and <& meanin 8 da V thc Phlv -
)^3 gil* related to Arm. /'/ (Horn, Grundriss, 207). 7 From Middle
1 Hiibschmann, Arm. Gramm, i, 378.
2 Neue Beitrdge, 27.
8 Others, however, would not admit this identification, and we learn from Tab.
that some took it to mean the lowest heaven, others connected it with sjllST and
others made it a form J^i from Jsc-l meaning J-jl. Finally, BaicJ. tells us that
some thought it a variant of /t-se meaning hell.
* al-Jawallqi, Mu'arrab, 81 ; Ibn Qutaiba, Adab al-Katib, 527 ; al-Khafaji, 103 ;
Raghib, Mufradat, 223 ; Baid on xi, 84 ; as-Suyiitf, Jty, 321 ; Mutaw, 35, and see
Horovitz, KU, 11 ; Siddiqi, 8, n., 2.
Bartholomew, AIW, 207. $ PPOl, 120.
7 But see Hubschmann, Arm. Gramm, i, 172.
=== awkNR 183 leaf 182 ===
FOREIGN VOCABULARY OF THE QUR*AN 165
Persian it passed directly into Arabic. Grimme, ZA, xxvi, 164, 165,
suggests S. Arabian influence, but there seems nothing to support
this.
IxxxSi, 7, 8.
The early authorities differed widely as to what the Sijjln of this
eschatological passage might be. It was generally agreed that it
was a place, but some said it meant the lowest earth <U> LJ' (j*J)* '
```


## [2026-09-04T19:07:23.504Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=169 && NR<=171 {print \"=== 1-based\",NR,\"===\"; print}' incoming/PLA/PLA_pages.txt | head -60"
}
```


### [2026-09-04T19:07:25.142Z] TOOL RESULT

```
=== 1-based 169 ===
 sabsär                                                                         154                                                   sagistäni


„Lu - sabsär:                       "Agent,             Vermittler"                 =    safsir       a.   v.


ol. _- sabistän:                              "cordia         myxa"           aus       pers.olL_un         sepestän          Ic      MP . Mreway»
       sepistän,                SYT           aan           pers.        2,


«you» - sabanguba:                                   "himmelblau"              = asmänfüni             q. v.

ars - sabanfüna:                                    "himmelblau"              - sabanfüba             u.   asmanfüni,          es    ist wahr-
       scheinlich                   eine             Nisba    v.     pers.              fu       sepan&-gün,           das     aus    pers.
        se-panß           + gün               besteht.            sepan&        selbst          heißt      drei      mal    fünf,
       welches            die        Kürze             des    Lebens           symbolisiert.               Es   ist    die     Eigenschaft
       des      Lebens              u.        die      der    Welt        u.    im       abstrakten         Sinn      die     des    Himmels.
       So     bedeutet               sepanf-gün                   "Himmelsart-und-Farbe"                        2,


@&”-        sabi$:             "ärmelloses                   Kleid,           Hemd"       aus    pers.      .» Sabi 3 mp.                   23% sabig


oa - sabiga = sabif g. v.

Slaw-       sagäf:             "Vorhang,                Franse"           4

Solo» - sagäwand:                             aus dem pers.                   FR          sagawand         5

law.                safbistäan:                      "eine    Pflanze"                    pers ol                 sag-pestän,           syr. NORR)


Go - saßzi:                Nisba                    v.Oli.n„        saßistän             7.      saßistän.

Ol          - sagistän:                       "Sistan"            aus     pers.         ol.        sistan       ec         MP .ıre»>s3,„,   sakistän
                                          9
                ap.       saka                _°.


Gluose -            saßistäni:                       Nisba    v.     safistän,             mand.       sigistaniia,



 1.   Addai         Scher           s.        v.,      Kamäl        s.    v.,       Löw    s.    v.
 2.   Brockelmann                   s.        v.
3. Wahrmund               s.        v.,             Muhit    s.     v.,       al-MuCarrab             s.   v.
4.    ebda.
5.    BQ.     Ss.    v.
6.    Brockelmann                   s.        v.
7. Muhit            s.    v.
8.    ebda.
 9.   Mayrhofer                s.    v.

=== 1-based 170 ===
sabsaslına                                                                        155                                               sahtiyän



mau           -    saßsasüna:                  "Himmelblau"                   =    sabanfüba           q.   v.
```


## [2026-09-04T19:07:33.993Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"iggil\\|iggil\\|siggil\\|siǧǧīl\\|sigg\\|sijjil\\|ıggıl\\|Bil:\" incoming/PLA/PLA_pages.txt | head -20; echo \"=== search sang gil\"; grep -n \"sang.*gil\\|sang-i\" incoming/PLA/PLA_pages.txt | head -20"
}
```


### [2026-09-04T19:07:34.066Z] TOOL RESULT

```
=== search sang gil
8815:de     - safil:             "harte        Backsteine"                    aus       pers.         Ya.    sang-gil            1 mp.      >     sang
8816:        <T aw.              asanga,           asan        2, ap.            asan         °, Sail mp.                    d gil 4,
```


## [2026-09-04T19:07:38.168Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8800,8830p' incoming/PLA/PLA_pages.txt; echo \"=== page index\"; python3 - <<'EOF'\nimport re,bisect\nd=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n'); offs=[];pos=0\nfor l in lines: offs.append(pos); pos+=len(l)+1\nff=[m.start() for m in re.finditer('\\f',d)]\nprint('leaf(1-based) of line 8815:', bisect.bisect_right(ff,offs[8814])+1)\nEOF"
}
```


### [2026-09-04T19:07:39.690Z] TOOL RESULT

```
mau           -    saßsasüna:                  "Himmelblau"                   =    sabanfüba           q.   v.


ausw          - safsafüya:                    = sabanfüba                   q. v.


Lima - safsanbüya                               = sabangüba                   q. v.

aw-      saßaf:             "Vorhang,              Franse"             = saßäf q. v.

am - safuf?:                 Pl. v. sabäf s. sabaf.

A ssuupun —            safanasfüya                 =    sabandbüya                 gG.    v.


de     - safil:             "harte        Backsteine"                    aus       pers.         Ya.    sang-gil            1 mp.      >     sang
        <T aw.              asanga,           asan        2, ap.            asan         °, Sail mp.                    d gil 4,
        griech.             sigillum            >,


Je -     sifill:              "öffentliches                   Aktenstück,                  Edikt,       Diplom"         Sf     safil,      mand.
        SGM       "to       seal        up"     6,


=        sgin               safil MP.                        0» sagen               "steinig"          7,

& -     subh:          "24        ratl"       pers.          8, wahrscheinlich                       aus    pers.       you   sahtan    U.
        sangidan              "wiegen"             mp.            eu»         sahtan           9

Saw-     saht:          "heftig            (Hitze)"               pers.           10           mp.   u» saxt          11,

=== page index
leaf(1-based) of line 8815: 170
```


## [2026-09-04T19:07:52.215Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### FFD pdf65 (p.60)\"; awk 'BEGIN{RS=\"\\f\"} NR==65 {print}' incoming/FFD/FFD_pages.txt | head -60"
}
```


### [2026-09-04T19:07:53.969Z] TOOL RESULT

```
### FFD pdf65 (p.60)
[pdf page 65]
انا انا فعلهای فارسی دری
«ستاند» ج «ستانید» مادهٌ ماضی جعلی از «ستان» است.
۱ ستودن
ستود + فارسی میانه 5100 < ایرانی باستان ۹18-12*. برای 2 آراست. صورت
ضعیف 514۷ است و ريشهٌ 912۷ به معنی «ستودن» است.
ستای < فارسی میانه 513 < ایرانی باستان 8ر813۷-۵*. 278 نشانه‌ای بوده که
برای ساختن مادهٌ مضارع از ريشه به کار می‌رفته است. ‎٩13‏ صورت بالاندةٌ ریشهٌ 312۷
است.
دا
سخت + فارسی میانه 3231 < ایرانی باستان ۶۵-1*. برای ۵ > آراست. 8 صورت
اصلی است و آن صورت ضعیف ريشهٌ 8 به معنی «کشیدن» است. برای
ضعیف‌کردن ريشه 8 حذف شده است.
سنج + فارسی میانه [828 < پهلوی اشکانی [8۵2 < ایرانی باستان ۵-[۶28*. برای 8 ->
آرای. [به جای ج آمده است.
سرشتن
سرشت < فارسی میانه 85151 + ایرانی باستان ۶713-1۵*. برای ۵ > آراست. کزرّه
صورت ضعیف ريشةٌ 8788 است و آن به معنی «چسباندن» است.
سریش < فارسی میانه 8783 < ایرانی باستان ۶۲۵15-2*. برای 2 > آرای.
«(سریش)» به معنی «رستنی‌ای که ... بعد از رسیدگی خشک کنند و آرد سازند و
کفشگران و صحافان چیزها بدان چسبانند.» (برهان قاطع)» از ریشهٌ 788 است.
سرودن
سرود + فارسی میانه ۶734 < ایرانی باستان ۹۳8-1۵" برای 1۵ > آراست. ‎٩۳3‏
‏صورت ضعیف ريشةٌ 818۷ است. به معنی «خواندن».
```


## [2026-09-04T19:08:04.298Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint(len(pages))\nfor i,p in enumerate(pages):\n    if 'سختن' in p:\n        print('leaf',i, p[:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T19:08:07.267Z] TOOL RESULT

```
485
leaf 41                                          ‫‪۸۳‬‬                                 
leaf 100 ‫برز‬                   ‫ی‬‫کر‬                   ‫ید ه‬                      ‫خ
leaf 163                                              ‫‪۱۰‬‬                             
leaf 187 ‫‪«- ۲‬جامه مانند کوزه باشد که شراب در‬                         ‫جاثلیق (تازی‪ .
leaf 300                                                   ‫‪۳۹۲‬‬           ‫از آهو سخن 
leaf 308  ‫سنجیدن (سنگیدن)‬                             ‫‪۵۰۳‬‬   ‫[‪ :‬بی‌سلاح] گویند (م
leaf 397                                             ‫‪۳۹۳‬‬                             
leaf 399                                               ‫‪۳۹۹‬‬                           
leaf 400 ‫کسلانیدن‬                                    ‫‪۳۹۲‬‬                 ‫که دل راز
```


## [2026-09-04T19:08:12.475Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint(pages[308][:2200])\nEOF"
}
```


### [2026-09-04T19:08:14.153Z] TOOL RESULT

```
 ‫سنجیدن (سنگیدن)‬                             ‫‪۵۰۳‬‬

 ‫[‪ :‬بی‌سلاح] گویند (منتخب غیاٹ) به‬                       ‫چو من رفته باشم نماند به جای‬
                 ‫معنی مجازی‪ :‬سپهر آسمان‪:‬‬           ‫وگرنه مرا خود جزین نیست رای‬
             ‫چه مايه شبان دیده اندر سماک‬                  ‫یکی دخمه کردش ز سم ستور‬
 ‫حروشان بدم پیش یزدان پاک‬                          ‫جهانی ز زاری همی گشت کور‬
 ‫(‪)۱-۱۷۱-۷۴۵‬‬                                       ‫(‪)۲-۹۴۲-۲۵۰۱‬‬
                  ‫سمند (بازبر اول و دوم)‬            ‫یعنی رستم به‌خود می‌گفت‪ :‬اگر دخمة‬
‫‪«-۱‬اسب‌زرده بود» (لغت فرس) اسبی که‬                 ‫زرینی بسازم‪ .‬ساییده می‌شود و از بین‬
                    ‫زنکین مایل به زردیست‪:‬‬      ‫می‌رود» پس دخمه‌ای مانند خانه یا آغل‬
               ‫نشست از بر تازی اسب سمند‬                                       ‫ستور ساخت‪.‬‬

‫چو زرین درخشنده کوهی بلند‬                          ‫گ‌آور است که بنداری اصفهانی‬
                                                                             ‫فت‬‫ش‬
‫‏(‪)٩۶۱-۱۹۹-۱‬‬                                   ‫ترجمة این مصراع را کی دخمه کردش‬
                            ‫‪-۲‬مطلق اسب‪:‬‬            ‫ز سم ستور» چنین می‌آورد‪« :‬و دفنوا و‬
               ‫وه‬
                ‫پی‌اندر گرفتم همه دشتکو‬                    ‫بنوا عليه تربته من حوافرالخیل»‪.‬‬
 ‫که از تأختن شد سمندم ستوه‬                         ‫خوافن جمم حافر بای تاشن بایان‬
 ‫(هم‪)۸۳۰-۲۰۵‬‬                                       ‫است‪ .‬بنداری وارهُ «سم» را در این بیت‬
                           ‫سنحیدن (سنگیدن)‬
 ‫‪-۱‬سختن اندازه گرفتن» کشیدن‪ ,‬وزن‬
                                               ‫ببه‌معنی معروف آگنرفته و بیت را‬
                                                   ‫نادرست ترجمه کرده است‪ .‬چون با خرد‬
 ‫کردن (از این ريشه سنجه س=نگ ترازو)‪:‬‬
                                                   ‫جور نمی‌آید که رستم بگوید دخمه زرین‬
               ‫جوانی هنوز‪ .‬این بلندی مجوی‬
                                                   ‫بجای نمی‌ماند و انوقت دخمه را از ناخن‬
 ‫سخن را بسنج و به‌اندازه گوی‬
 ‫(‪)۶-۱۱-۶۴‬‬
                                                                      ‫چارپایان بسازد‪.‬‬
                            ‫(مسعود ‪:)۷۰۳‬‬
```


## [2026-09-04T19:08:26.825Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i in list(range(80,90))+list(range(300,312)):\n    m=re.findall(r'[۰-۹]{2,4}', pages[i][:200])\n    print(i, m, pages[i][:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T19:08:28.558Z] TOOL RESULT

```
80 [] ‫بازار‬     ‫کشتی شکستگانیم ای باد شرطه برخحیز‬             
81 ['۷۸']                                                   ‫‪۷۸‬‬    
82 []                         ‫=اژخواه ب=اژدار‬                   
83 []                                                             
84 []  ‫بالیدن‬   ‫نگ باهستقبال او [‬       ‫سیک‬                 
85 []                                                             
86 ['۸۳'] ‫بایست‪ .‬بابسته‬                                ‫‪۸۳‬‬  ‫را
87 []                                                             
88 []  ‫بجای‪ .‬برجای‬                          ‫ببینم‪ ,‬آپنسگاه‪
89 []                                                  ‫‪۸1‬‬     
300 ['۳۹۲']                                                   ‫‪۳۹۲‬‬   
301 ['۳۹۸']                                              ‫‪۳۹۸‬‬        
302 ['۳۹']                                               ‫‪۳۹‬‬        
303 []                                              ‫‪۰‬‬          
304 [] ‫سریاز‬   ‫دست سروی این گاو گرفت و به دیگر‬                 
305 ['۳۰۲']                                               ‫‪۳۰۲‬‬       
306 []  ‫سگزی‬                                       ‫‪۳.۳‬‬       
307 ['۲۹۳']                                               ‫‪۳.۳‬‬       
308 ['۵۰۳']  ‫سنجیدن (سنگیدن)‬                             ‫‪۵۰۳‬‬   ‫[‪
309 ['۹۰۳']                                            ‫‪۹۰۳‬‬          
310 []  ‫سودن‬                                        ‫‪۳.۷‬‬    ‫ب
311 ['۷۵۱']
```


## [2026-09-04T19:08:34.711Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint(pages[227][:900])\nEOF"
}
```


### [2026-09-04T19:08:36.379Z] TOOL RESULT

```
                                                ‫‪۳۳۴۳‬‬                                       ‫داستانیی‬



             ‫نگه کرد گودرز تیر حدنگ‬                                   ‫بدو گفت گیو ای سر راستان‬
‫که آهن ندارد مرااو رانه سنگ‬                            ‫ز گودرز با تو که زد داستان؟‬
 ‫(‪)۵-۱۰۲-۹۸۹۱‬‬                                          ‫(‪)۳-۶۱۰۲-۲۴۱۳‬‬


  ‫به بر گستوان بر زد و بر درید‬                                          ‫پزوهندة نامه بساستان‬

  ‫کرشید‬‫تگاور بسلرزید و دم د‬                            ‫که از پهلوانان زند داستان‬
       ‫وا‬‫راد‬
           ‫ن ب‬
             ‫چون‬
               ‫متا‬
                 ‫ر رف‬‫فی‬
                      ‫هم‬                               ‫(‪)۱-۸۲-۵‬‬

 ‫یکی کوه دیدش سراندر هرا‬                                           ‫ولاه‬
                                                                      ‫تخت ک‬        ‫ین‬
```


## [2026-09-04T19:08:42.555Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SNS grep sang\"; grep -n \"sang\" SNS_pages.txt | head -10; echo; echo \"### SYN leaf 76 (p.52)\"; awk 'BEGIN{RS=\"\\f\"} NR==77 {print}' SYN.txt | head -60"
}
```


### [2026-09-04T19:08:44.257Z] TOOL RESULT

```
### SNS grep sang
5556:                                          ,^j» <i&«> rfrasang:       3V->^0                                                                                   1       *A>>C>tV/?1 iS
5560:                                     U/T^ •(&&*) frasang :^                   |
11514:                                                                                                                                                              :Neryosang:                a*?o^s|
11521:                                                                                                                                             f                .   ^1 Neryosang:
15879: sang 193/15-313/14       si Gvak 10/8
15990:NSryGsang 290/5        nihufSnd 286/3                                 nflzdah 304/19             SzanSd 164/1
15991:NSryOsang 290/4        nihuft 262/10                                  nivlt-zadlh 284/21         SzanSnd 164/4
16082:                        husangd 65/14
16300:                                                         fraz 136/4-8                frasang 129/1

### SYN leaf 76 (p.52)
es’ (1.41).
Br. gwezenn, sg. of coll. gwez ‘trees’ = ' Ir. fid, W. gwydd ‘woods’ (1.41).
5. Goth. bagms, ON badmr (poet.), OE béam (‘tree’ and ‘beam’, NE beam),
Du. boom, OHG, MHG boum, NHG baum, etym. dub. (: Grk. diya ‘growth’, etc.?). Walde-P. 2.143. Feist 73. Falk-Torp 92.
ON tré, OE tréow, etc., above, 1.
6. Lith. medis ‘tree’ and ‘wood’ : Lett. mezs, OPruss. median ‘woods’ (1.41).
Lett. kuoks ‘tree’ and ‘wood’ : Lith. kuoka ‘stick, cudgel’, further connec- tion? Miuhl-Endz. 2.343.
7. ChSI. drévo, etc., above, 1.
ChSl. dqbi (Supr., etc.; in gospels only drévo, cf. Jagié, Entstehungsgesch. 342), orig. ‘oak’ as general Slavic (8.61). Berneker 216.
Boh. strom : strméti ‘project, tower up’, strmy ‘precipitous’, ChSl. striéimi, SCr. strm ‘precipitous’. Miklosich 325, 326. Gebauer 1.60.
8. Skt. vrksa- ‘tree’, Av. varasa- ‘tree’ or ‘woods’ (? cf. Barth. IF 9.273, ftn.), etym.? Walde-P. 1.286, 289.
Skt. taru-, late and possibly a dial. form belonging with daru. BR s.v. Uhlenbeck 109.
Skt. padapa- ‘tree, plant’, a poet. ex- pression, lit. ‘drinking with the foot, root’ (pada- and pa- ‘drink’).
Av. vana- : Skt. vana- ‘woods, tree, wood’ (1.41).
143 WOOD me ed Goth. triu Lith. medis Lat. ier ON tré, vor Lett. kuoks ieee ee Dan. tre, ved ChSI.  dritva (pl.) Fr, ans Sw. rd, ved SCr.  drvo Spanpebnade; OE tréow, wudu Boh. devo Rum. lemn ME tre, wode Pol.  drzewo = fid NE peed Russ. derevo iy. u. out Skt. daru-, kastha-
W. ae al OHG  holz, witu Av. pee ial: Bre stan MHG holz
» prenn NHG holz
Gurukul Kangri Collection, Haridwar
“~=—""Digitized by Arya Samaj Foundation Chennai and eGangotri
50
Most of the words for ‘wood’ as mate- rial are the same as, or connected with, those for ‘woods’ or ‘tree’ (from the standing tree through the felled tree, ‘timber, log’ to ‘wood’), and have been included in the discussion of these (1.41, 1.42).
There remain for notice here.
1. Grk. bd\ov, perh.: Lith. Sulas ‘post’, Goth. sauls, OE syl ‘pillar’, etc., with initial doublets (fs, s). Walde-P. 2.503 f. Boisacq 679.
2. Lat. lignum : legere ‘collect’, hence first used of the collected ‘fire- wood’ (cf. NHG leseholz ‘firewood’), and in actual use most commonly pl. lzgna
SELECTED INDO-EUROPEAN SYNONYMS
Hence It. legno, OF r. leigne (replaced by bots), Rum. lemn. But Sp. leo is ‘timber, log’ and lefia ‘firewood’ (fr. Lat. pl. ligna), being replaced in sense of ‘wood’ as material by madera fr. Lat. materia ‘material’ and especially ‘build- ing material, timber’. Cf. the opposite development in Grk. vdn ‘woods, timber, material’, and NIX timber in the more general sense of ‘stuff, material’.
3. NIr. adhmad ‘timber, wood’ (in- cluding firewood), also ‘matter, stuff’, Mir. admat ‘timber, material’ : NIr. maide ‘stick’, Lat. malus ‘mast’, OF mest ‘mast’, etc. Walde-P. 2.235.
‘firewood’. Ernout-M. 549. Walde-H. | NIv. fiod
```


## [2026-09-04T19:08:50.837Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=78 && NR<=80 {print \"=== awkNR\",NR,\"===\"; print}' SYN.txt | grep -n \"STONE\\|Stein\\|asan\\|asenga\\|sang\\|akmon\\|akmen\\|52\\|53\" | head -30"
}
```


### [2026-09-04T19:08:53.390Z] TOOL RESULT

```
2:h (Iv. fid, 1.41) still used for 1.799. ‘wood’ in cpds. and derivs. 144 STONE; ROCK Grk. — Aifos; wérpa Goth. stains; hallus Lith. akmuo; uola NG mérpa, ABdpt ON steinn Lett. akmens; klinis Lat. lapis; sacum, petra Dan. _ sten; klippe ChSl. kamy (skala) It. ptelra, sasso; roccia Sw. sten; klippa SCr. kamen; strijena Fr. pierre; roche, rocher (0) 0} slan Boh. kdaen; skdla Sp. piedra; roca ME stone; rokke Pol. kamien; skala, opoka Rum. piatrd; stined, rocd NE stone; rock Russ. kamen’; skala Ir. cloch, lia; carric, all, Du. steen; rots Skt. agman-, acan-, cild- craic OHG - stein; felis, feliso pasana, etc. NIr. loch; carraig, craig MHG stein; vels, velse Av. asan-, zarslva- W. carreg, maen; craig MHG stein; fels, felsen Br. maen; karreg
15:2. Lat. lapis ‘stone’ : Grk. Néras ‘bare rock’ (this apparently fr. Nérw ‘peel’)? Walde-P. 2.431.  Ernout-M. 523. Walde-H. 1.761.
40:52 SELECTED INDO-EUROPEAN SYNONYMS
41:‘climb’, NHG hleben ‘stick to’, NE cleave, etc. Walde-P. 1.620. Falk- Torp 533, 531.
42:OHG felis, feliso, MHG vels, velse, NHG fels, felsen : ON fjall ‘mountain’, Grk. 7@&da ‘stone’ (Ulp. ad Dem., Hesych.), Ir. all ‘rock, cliff’, Skt. pasya-, pasana- ‘stone’, root connection? Walde-P. 2.66 ff. Falk-Torp 223.
43:5. Lith. akmuo, Lett. akmens ‘stone’, ChSI. kamy ‘stone, rock’ (renders both NOos and zérpa), SCr. kamen, etc. ‘stone’, Skt. agman-, acgan-, Av. asan- (asman- ‘sky’) ‘stone’, adj. Av. asmana-, OPers. aéa(n)gaina- ‘of stone’, NPers. sang ‘stone’, the general Balto-Slavic and Indo-Iranian word for ‘stone’, Grk. axpov ‘anvil’ (‘meteoric stone’ in Hesi- od) : Grk. dxpy ‘point, edge’, axpos ‘top- most’, Skt. acri- ‘edge’, Lat. acer ‘sharp’, etc. Walde-P. 1.28 ff.
51:6. Skt. agman-, agan-, Av. asan-, above, 5.
61:Tr. nem Du. hemel Skt. div-, nabhas- Nir. — spéir (neamh) OHG  himil Ay. asman-, asan- (div-, W. wybr, wybr
```


## [2026-09-04T19:09:15.832Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt; for w in \"آکروبات\" \"اکسیژن\" \"اسید\" \"استن\" \"آسیاب\" \"سنجیدن\"; do echo \"--- $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null; done"
}
```


### [2026-09-04T19:09:17.519Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
--- آکروبات
MON_part2.txt:0
MON_part1.txt:0
--- اکسیژن
MON_part1.txt:26
MON_part2.txt:29
--- اسید
MON_part2.txt:82
MON_part1.txt:89
--- استن
MON_part2.txt:124
MON_part1.txt:330
--- آسیاب
MON_part2.txt:4
MON_part1.txt:3
--- سنجیدن
MON_part1.txt:10
MON_part2.txt:6
```


## [2026-09-04T19:09:21.173Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 600 MON_part1.txt; echo; echo \"=== اکسیژن context\"; grep -n -m3 \"اکسیژن\" MON_part1.txt | cut -c1-400"
}
```


### [2026-09-04T19:09:21.237Z] TOOL RESULT

```
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
=== اکسیژن context
749:بی‌بو؛ مر کب از دو عنصر اکسیژن و تیدرژن. 
833:ترکسی داشته باشند مولد اکسیژن. آب 
1582:خرچنک‌ها و نوزاد قورباغه) اکسیژن محلول
```


## [2026-09-04T19:09:33.234Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HJB ACHAR\"; grep -n \"^ACHAR\\|ACHAR,\" HJB.txt | head; grep -n -A 12 \"ACHÁR\\|ACHAR, s\" HJB.txt | head -30"
}
```


### [2026-09-04T19:09:33.316Z] TOOL RESULT

```
### HJB ACHAR
1518:ACHAR
```


## [2026-09-04T19:09:34.479Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### AID\"; grep -n -i \"achar\" AID.txt | head -10; echo \"### LKT\"; grep -n -i \"atschar\\|achar\" LKT.txt | head -10; echo \"### DEV\"; grep -n -i \"achar\\|atchar\" DEV.txt | head"
}
```


### [2026-09-04T19:09:34.595Z] TOOL RESULT

```
### AID
266:AchArjya.  [Bengali,  from  the  Sanskrit dchdrya ,   q.v.]  The  name  of  a   caste in  Bengal ;   they  are  astrologers  and fortune  -   tellers,  and  generally  re- semble the  Bhdts.  They  claim  to be  of  Brdhman  origin.
1271:Brahmachdri.  A   Brdhman  in  his first,  or  brahmacharya,  dsrama,  in which  he  learns  the  veda  in  the house  of  a   preceptor.  A   brah- machdri, instead  of  passing  on  into the  other  dramas,  may  bind  himself to  remain  a   student  for  life,  and such  persons  now  constitute  a numerous  order.  Colebrooke  re- marks of  them  that  they  seem  to hold  the  austerities  as  more  essential than  the  studies  connected  with  the brahmacharya  discipline,  and  that many  of  them  appear  to  be  wholly illiterate.
1272:Brahmacharya.  [Sanskrit  charya, practice.]  The  first  of  the  four ddraxnas  into  which  the  Brahman’s
3866:Korachar.  [Kanarese.]  The  name of  a   wandering  tribe  who  carry  salt and  grain  from  one  market  to another  by  means  of  large  droves of  cattle  and  asses,  and  also  make bamboo  mats  and  baskets.  The men  wear  their  hair  tied  in  a   large knot  on  one  side  of  the  top  of  the head  in  the  manner  seen  in  the sculptured  figures  on  old  stone monuments.  The  women  wear  nu- merous strings  of  small  red  and white  glass  beads  and  shells  round the  neck  and  falling  over  the  bosom, which  also  accords  with  the  ancient practice  as  seen  in  old  bas-reliefs.
3867:The  Korachars  carry  with  them  the framework  of  a   rude  description  of hut,  and  while  one  part  of  the  tribe proceeds  with  the  baggage  animals, the  others  settle  for  a   time  and  em- ploy themselves  in  making  mats  and baskets  and  in  begging  and  stealing. They  often  commit  burglaries  and dacoities.  They  speak  Telugu  and Tamil,  and  also  a   peculiar  dialect  a mixture  of  the  two  (Z.  Rice).
3868:Koramar.  The  name  of  a   wandering tribe  in  Coorg;  they  are  distin- guished as  Uppu  and  Kdge  Kora- mar ;   the  former  engage  in  traffic, and  are  held  superior  to  the  latter. They  appear  to  be  the  same  tribe  as the  Korachars  of  Mysore.
3873:Korawa.  The  name  of  a   tribe  in Cutch  detached  from  the  Korachars of  Mysore.
3877:Korwa.  See  Korachar.
3973:Kurawan.  [Tamil.]  The  name  of  a tribe  who  wander  about  with  tents, hawking  goods  and  telling  fortunes. They  deal  largely  in  salt,  which  they carry  from  the  salt-pans  on  the  coast into  the  interior,  returning  with grain.  Some  make  boxes  and baskets  of  bamboo,  twigs,  and  pal- myra leaves  ;   others  breed  pigs  and donkeys  ;   others  collect  hohey  and other  jungle  produce.  They  are perhaps  the  same  as  the  Korachars of  Mysore.
6609:SwAmi-N  dr  Ay  an.  The  name  of  a Vaishnawa  sect  founded  in  GujarAt, in  the  present  century,  by  SwAmi- NArAyan,  or  SahAjAnand,  a   native of  Oudh.  Professor  Monier  Wil- liams describes  SwAmi-NArAyan’s teaching  as  a   modern  Puritan movement  against  the  WallabhA- chAryan  corruption  of  the  Vaishnawa faith,  and  says  he  made  chastity  and purity  of  life  the  key-note  of  all  his teaching,  and  ended  by  boldly  as- serting that  he  himself,  and  not WallabhAchArya,  was  the  true  incar- nation of  Krishna.  SwAmi-NArAyan appointed  his  two  nephews,  Raghu-
### LKT
252:'Sauer',  hieraus  malay.  a£ar  [Pijn  237] in  der  Bedeutung  'Eingemachtes,  pickles' und  ebenso  in  allen  Eingeborenen- sprachen Indiens;  daher  angloind.  achar 'dass.';  frz.  achars  'Obst  od.  Gemüse, das  in  Essig  eingemacht  ist',  ein  im indischen  Archipel,  auf  Mauritius  usw. sehr  beliebtes  Gericht.  [Devic  DEt  3/4. Hobson-Jobson  3.
5894:Englisch  (euischl.  angel- sächsisch u.  angloindisch). ^&io^  1 aööo^  ags.  1 abcaree  7 abkarg  7 aboogerdan  11 achar  15 Adam's  apple  19 adau)lut  18 admiral  69  a adoöe  2083 agar-agar  30 ag-boat  27 agdaun  27 agun-boat  27 ailant(h)us  1141 alang- alang  54 albairos(s)  988 alcaide  1006
6332:achars  16
### DEV
252:AcHARs.  Fruits,  légumes,  bourgeons  confits  dans  le  vi- naigre, comme  nos  cornichons,  ou  dans  d'autres  prépa- rations fortement  épicées.  C'est  un  condiment  très-goûté dans  l'archipel  Indien,  à  Maurice,  à  l'île  Bourbon,  etc.
257:On  écrit  aussi  achards  :  c<  Les  acliards  colores  parle  safran,  v (Simonin,  Voyage  à  l'île  de  la  Réunion  '.)  Le  Dictionnaire  de Déterville  écrit  atchar,  qui  est  la  forme  ori^jinidle.  C'est  le persan  ^l=^t  aicluir,  en  malais  -^î  atchar.  Je  ne  saurais dire  quel  est  le  sens  primitif  de  ce  mot,  qui  nous  est  venu, non  de  la  Perse,  mais  des  Indes.
259:AcHouR.  ^Nom  d'un  impôt  payé  par  les  indigènes  de l'Algérie  au  gouvernement  français.?)  (Littré,  Dict.  Addit.) C'est  l'arabe  )y**^  \ichoûr,  dîme,  venant  de  yi^  'achar, dix.  Le  mot  aciiour  n'est  pas  dans  le  Diction,  fr.-ar.  de M.  Cherbonneau,  qui,  du  reste,  a  laissé  de  côté  un  grand nombre  des  termes  introduits  chez  nous  par  la  conquête de  l'Algérie.
2380:AcHARS. ACHERNAR.
4550:Alchimie,  12. ^L^l  pei's.  voy.  Achars. jgjJl  jà.1  voy.  Achernar. (jil  voy.  Muezzin. 8i>Ul  voy.  Iradë. o*s?y  pers.  voy.  Arlicliaul. ^jUk.rl  voy.  Argan. S^^\  voy.  Arzel. <_jk>^i  voy.  Ardeb. a5^j>,I  voy.  Artichaut, p^l  voy.  Raze. jSA^^t  turc,  voy.  Patard.
```


## [2026-09-04T19:09:43.674Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### LKT 244-256\"; sed -n '244,256p' LKT.txt; echo; echo \"### HJB 1510-1530\"; sed -n '1510,1530p' HJB.txt"
}
```


### [2026-09-04T19:09:43.740Z] TOOL RESULT

```
### LKT 244-256
[Wörtlich  „Vater  der  Zecken",  die  ar. kiräd,  plr.  kirdän  heißen].  Der  rein weifae  'Kuhreiher',  Ardea  bubuleus  Sa- vigny,  ein  afrikanischer  Vogel  [die Schreibung  aboogerdan  bei  ML  36  wie schon  vorher  bei  Körting,  Lateinisch- romanisches Wörterbuch.  3.  Aufl.  Pader- born 1907,  s.  V.  ist  englisch].  Durch volksetymologische  Neugestaltung  hier- aus vielleicht  frz.  bwuf-garde,  garde- bcfuf  'eine  Art  Silberreiher'.  [FASS in  RomForsch  III,  488.  KURYLOWICZ in  Rocznik  Orientalistyczny.  Tom  II. Lwöw  1925.    S.  252.
12.  Ar.  'abar:
In  der  Zusammensetzung  as-sirä  al- "abiir  'der  [sc.  auf  der  Milchstraße] wandernde  Sirius'  [hierzu  s.  hier  Nr.  1915] vom  ar.  Stamme  'fcr  'wandern'  [vgl. hebr.  "ibrl  'Hebräer',  d.  h.  derjenige,  der gewandert  ist  od.  überschritten  hat  sc. den  Euphrat  od.  Jordan].  Hieraus  Alha- bor,  Alchabar  als  Name  des  Sirius  a Ganis  majoris.  [Devic  DEt  40/41. Ideler  Sternn  237  und  246.
13.  Ar.  abü  rag':
'Vater  des  Schweißes',  hieraus  lat.  bor- rago,  eine  Pflanze,  die  durch  die  ar. Medizin  im  Mittelalter  verbreitet  wurde. Die  romanischen  Formen  sind:  it.  bor- race,  borragine,  borrana;  prov.  borrage; sp.  borraja ;  pg.  borragem ;  frz.  hourrache. Auch  germanisch,  z.  B.  engl,  borage, dtsch.  Burrich,  Bor( rjetsch.  Wohl  über das  Ngr.  entstand  rum.  boranjä  'dass.'. Trotz  ML  1412  scheint  diese  Ableitung noch  immer  die  beste  und  wenig  an- fechtbar zu  sein.    [Kluge  64.
14.  Ar.  abü  tilün:
[Vgl.  Ihn  Sinä,  Kitäb  al-känün  fi't-tibb. Romae.  In  typographia  Medicea  1593. S.  137]  'eine  Zierpflanze'  aus  der  Familie der  Malvaceen:  Abutilon  indicum.  Hier- aus frz.  abutilon  'dass.',  nämlich  abutilon striS  Abutilon  striatum  Diks.  (Sida  striata Hort.)  und  abutilon  itendard  A.  vexilla- rium  Ed.  Morrea  (S.  vexillaria  Hort.). [Devic  DEt  3.    Lammens  Rem  3.
15.  Pers.  acär:
'Sauer',  hieraus  malay.  a£ar  [Pijn  237] in  der  Bedeutung  'Eingemachtes,  pickles' und  ebenso  in  allen  Eingeborenen- sprachen Indiens;  daher  angloind.  achar 'dass.';  frz.  achars  'Obst  od.  Gemüse, das  in  Essig  eingemacht  ist',  ein  im indischen  Archipel,  auf  Mauritius  usw. sehr  beliebtes  Gericht.  [Devic  DEt  3/4. Hobson-Jobson  3.
16.  Ar.  'äda:
'Sitte,  Gebrauch',  ebenso  Ik.  adet  'dass.'; hieraus  rum.  adet  'Brauch,  Sitte,  Regel', früher  'Steuer'.    [Sain  46.
17.  Malayälam  adakka:
[Aus  arfa/ 'enge  Anordnung  einer  Traube' und  kay  'Nuß'].  Hieraus  pg.  areca, angloind.  Areca,  worunter  man  allge- mein den  Samen  od.  die  Nuß  der  Palme, Areca  catechu  L.,  versteht.  [Hobson- Jobson  35.

### HJB 1510-1530
1797. — "  The  stamps  are  to  have  the  words* *Aboaree  licenses '  inscribed  in  the  Persian and  Hindu  languages  and  character." — Ben- gal RegulatiorUf  x.  33.
ABISOWA.  Proprly  P.  db-o- hatoAj  *  water  and  air.'  The  usual Hindustani  expression  for  'climate.'
1786.— "What  you  write  concerning  the death  of  500  Eoorgs  from  small-pox  is understood  ....  they  must  be  kept  where the  climate  [&b-o-liaw&]  may  best  agree with  them,"— Tippoo^a  Letters,  269.
ABYSSINIA,  n.p.  This  geogra- phical name  is  a  16-century  Latin- isation  of  the  Arabic  Habash,  through the  Portuguese  ^6esB,  *  bearing  much the  same  pronunciation,  minus  tlie aspirate.    [See  HT7B8HEE.]
[1608.— "Theoountreyof  the  Abexynes, at  Prester  John's  land.^ — Linschoten,  Hnk. Soc.  i.  88.
1617.— "He  sent  mee  to  buy  three Abasailim."— iSir  T,  Roe,  Travels,  Hak. Soc.  ii.  446.]
A.O.  (i.«.  *  after  compliments*).  In official  versions  of  native  letters  these letters  stand  for  the  omitted  formalitie^s of  native  compliments.
ACHANOCK,  n.p.  H.  Chdnak  and Achdnak,  The  name  by  which  tlie station  of  Barrackpore  is  commonly known  to  Sepoys  and  other  natives. Some  have  connected  the  name  with that  of  Job  Chamock,  or,  as  A. Hamilton  calls  him,  Channock,  tlie founder  of  Calcutta,  and  the  quotations render  this  probable.  Formerly  the Cantonment  of  Secrole  at  Benares  w^JLs also  known,  by  a  transfer  no  doubt,  us Chhotd  (or  < Little')  Achan&k.  Two additional  remarks  may  l)e  rele\^itly made :  (1)  Job's  name  was  certainly Ghamock,  and  not  Channock.  It  is distinctly  signed  "Job  Chamock,"  in a  MS.  letter  from  the  factory  at "Chutta,"  i.e.  Chuttanuttee  (or  Cal- cutta) in  the  India  Office  records, which  I  have  seen.  (2)  Tlie  map  in Valentijn  which  shows  the  village  of T^jannok,  though  published  in  1726, was  apparently  compiled  by  Van  der
ACHAR
A  CHE  EN.
Broecke  in    1662.      Hence  it  is  not
Jrobable  that  it  took  its  name  from ob  Chamock,  who  seems  to  have entered  the  Company's  service  in  1668. When  he  went  to  Bengal  we  have  not Iteen  able  to  ascertain.  [See  Diary  of HedgeSf  edited  by  Sir  H.  Yule,  ii.,  xcix. In  some  "Documentary  Memoirs  of Job  Chamock,"  which  form  part  of voL  Ixxv.  (1888)  of  the  Hakluyt  Soc., Job  is  said  to  have  "  arrived  in  India in  1655  or  leae.*^
1677. — "The  ship  Falcone  to  ffo  up  the riTer  to  Hnghly,  or  at  least  to  Chaimook." —Court's  Letter  to  Ft.  St.  Geo.  of  12th December.  In  Notes  and  JBxtrads,  Madras, 1871,  No.  1.,  p.  21 ;  see  also  p.  23.
1711.— "Chaaook-Reach  hath  two  shoals, the  upper  one  in  Ghaaook,  and  the  lower one  on  the  opposite  side  ....  you  must from  below  Degon  as  aforesaid,  keep  the starboard  shore  aboard  until  you  come  up with  a  lime-Tree  ....  and  then  steer  oyer with  Chanock  Trees  and  house  between  the two  shoals,  until  you  come  mid-river,  but  no nearer  the  house.''— rA«  English,  JHlot,  55.
1728.— "'t  stedeken  Ttajaanook."— To^ entifUj  y.  153^  In  Val.'s  map  of  Bengal also,  we  find  opposite  to  Oegli  (Hoogly), T^Jjumok,  and  then  CoUecatte,  and  Cdleula,
1758. — "Notwithstanding  these  solemn aasmanoes  from  the  Dutcm  it  was  judged expedient  to  send  a  detachment  of  troops ....  to  take  possession  of  Tanna  Fort  and Ghaxnoc's  Battery  opposite  to  it."— Nar- rative of  Dutch  attempt  in  the  Hoogly,  in Malcolm's  lAfe  ofClvee,  ii.  76.
1810.— "The   old   village   of   Aohaaook
stood  on  the  groimd  which  the  post  of Barrackpore  now  occupies." — M,  Oraham, 142.
1848. — "From  an  oral  tradition  still  pre- valent among  the  natives  at  Barrackpore ...  we  learn  that  Mr.  Chamock  buut  a bungalow  there,  and  a  flourishing  bazar arose  under  his  patronage,  before  the settlement  of  Calcutta  had  been  deter- mined on.  Barrackpore  is  at  this  day best  known  to  the  natives  by  the  name of  Chanook."— Jft«  Bengal  ObUuaryy  Calc. p.  2.
AOHAB,  8.  P.  achdr^  Malay  dchOr^ adopted  in  nearly  all  the  vernaculars of  India  for  acid  and  salt  relishes.  By Europeans  it  is  used  as  the  equivalent of  *  pickles,'  and  is  applied  to  all  the Atoies  of  Crosse  and  felackwell  in  that kind.  We  have  adopted  the  word through  the  Portuguese ;  but  it  is  not impossible  that  Western  Asiatics  got  it originally  from  the  Latin  acda/ria,— (See  PlifL  Hid,  Nat.  xiz.  19).
1568. — *'And  they  prepare  a  conserve  of it  {Amaeardiinn)  with  salt,  and  when  it  is greeo  (and  this  they  call  Adhar),  and  this
```


## [2026-09-04T19:10:01.997Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,bisect\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nff=[m.start() for m in re.finditer('\\f',d)]\ndef leaf(p): return bisect.bisect_right(ff,p)\nfor w in ['\\nacrobat,','\\noxygen,','\\nacid,','\\nvinegar,','\\nacute,','\\nedge,','\\nhammer,','\\nacme,','\\nacerb','\\nacetone']:\n    for m in re.finditer(re.escape(w), d):\n        print(w.strip(), 'leaf', leaf(m.start()), '|', d[m.start():m.start()+430].replace('\\n',' '))\n        break\nEOF"
}
```


### [2026-09-04T19:10:03.894Z] TOOL RESULT

```
acerb leaf 19 |  acerb 14 pref.  a-,  Gk.  xfpas,  gen.  x£paTO?,  ‘horn’,  and ■9-rjplov,  ‘animal’.  See  cerato-  and  therio-  and cp.  prec.  word. acerb,  adj.,  sour,  sharp,  bitter.  —  L.  acerbus, ‘harsh  to  the  taste,  sharp,  bitter,  sour’,  fr.  acer, ‘sharp’ ;  see  acrid.  For  the  formation  cp.  super- bus,  ‘haughty,  proud,  excellent’ ,  fr.  super,  ‘above, over’  (see  superb). Derivatives:  acerbate  (q.v.),  acerb
```


## [2026-09-04T19:10:08.737Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,bisect\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nff=[m.start() for m in re.finditer('\\f',d)]\ndef leaf(p): return bisect.bisect_right(ff,p)\npats=[r'acrobat,\\s+n', r'oxygen,\\s+n', r'acid,\\s+adj', r'vinegar,\\s+n', r'acute,\\s+adj', r'edge,\\s+n', r'hammer,\\s+n', r'acme,\\s+n', r'acetone']\nfor p in pats:\n    m=re.search(p,d)\n    if not m: print(p,'NOT FOUND'); continue\n    print('---',p,'leaf',leaf(m.start()))\n    print(d[m.start():m.start()+700].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T19:10:10.440Z] TOOL RESULT

```
--- acrobat,\s+n leaf 21
acrobat,  n.  —  F.  acrobate,  fr.  Gk.  4xpo(3axop, ‘walking  on  tiptoe’,  fr.  Sxpop,  ‘at  the  end,  outer¬ most,  highest’,  and  pax-,  ‘going’,  from  the  stem of  Patvav,  ‘to  go,  walk’.  (Cp.  (foxfip,  ‘passable’, verbal  adj.  of  (JatvEiv.)  For  the  first  element see  aero-,  for  the  second  see  base,  n.,  and  cp. the  second  element  in  aerobatics. Derivatives:  acrobat-ic,  adj.,  acrobat-ic-al-ly , adv.,  acrobat-ics,  n.,  acrobat-ism.  n. acrocarpous,  adj.,  bearing  fruit  at  the  end  of  the stalk  ( bot .)  —  Gk.  4xp6xap7rop,  ‘bearing  fruit at  the  top’,  compounded  of  Sxpop,  ‘at  the  end, outermost,  highest’,  and  xaprrfip,  ‘fruit’.  See aer
--- oxygen,\s+n leaf 592
oxygen,  n.,  a  gaseous  chemical  element.  —  F. oxygene,  short  for principe  oxygene  (earlier  prin- cipe  oxygine),  lit.  ‘the  acidifying  principle’ ;  coin¬ ed  by  the  French  chemist  Antoine-Laurent  La¬ voisier  (1743-94)  in  1777  fr.  Gk.  d£us,  ‘sharp, acid’,  and  yeivopai.  T  beget,  bear,  bring  forth’, which  stands  for  'vew.ciuxi  and  is  rel.  to  yev- vxro,  T  beget,  bring  forth,  generate, produce’;  see oxy-,  ‘sharp;  acid’,  and  -gen.  Hence  oxygen  lit. means  ‘producing  acids’;  Lavoisier  and  the other  chemists  of  his  time  believed  that  oxygen was  an  important  compound  of  every  acid, oxygenate,  tr.  v.,  to  combine  with  oxygen 
--- acid,\s+adj leaf 20
acid,  adj.,  sour,  sharp  to  the  taste.  —  Either  fr. F.  acide  or  directly  fr.  L.  acidus,  ‘sour’,  fr.  acere, ‘to  be  sour’,  whence  also  acetum,  ‘vinegar’  (see acetum);  introduced  into  English  by  Francis Bacon  (1561-1626)  in  1626. Derivatives:  acid,  n.,  acid-ic,  adj. Acidaspis,  n.,  a  genus  of  Trilobites.  —  ModL., compounded  of  Gk.  dxip,  gen.  dxtSoi;,  ‘pointed object,  point,  needle’  (fr.  axf),  ‘point’),  and dram?,  ‘shield’.  See  acid  and  aspidistra, acidify,  tr.  v.,  to  make  sour;  intr.  v.,  to  become sour.  —  See  acid  and  -fy  and  cp.  F.  acidifier. Derivatives:  acidif-ic,  adj.,  acidif-ic-ation,  n., acidifi-er,  n. acidi
vinegar,\s+n NOT FOUND
--- acute,\s+adj leaf 23
acute,  adj.  —  L.  acutus,  ‘sharp  ,  lit.  sharpened  , pp.  of  acuere,  ‘to  sharpen’,  which  is  rel.  to  acus, ‘needle’.  See  acrid  and  cp.  cute  and  ague. Derivatives:  acute-ly,  adv.,  acute-ness,  n. -acy,  suff.  denoting  quality,  state  or  dignity.  — 1)  F.  -atie,  fr.  L.  -acia,  fr.  adjectives  in  -ax,  gen. -m  is  (cp.  fallacy)',  2)  F.  -atie,  fr.  L.  -dtia  (whence ML.  -dcia),  fr.  L.  -as  gen.  -atis  (cp.  abbacy)', 3)  ML.  -dtia,  fr.  L.  nouns  ending  in  -atus  (cp. magistracy)',  4)  ML.  -dtia,  fr.  Gk.  -dxcia  (cp. piracy);  5)  from  English  nouns  and  adjectives in  -ate  (cp.  privacy).  Cp.  the  suffixes  -cy  and -cracy.  Cp.  al
--- edge,\s+n leaf 174
edge,  notice.  —  ME.  coni- saunce,  fr.  OF.  conoissance  (F.  connaissance), ‘knowledge’,  fr.  conoistre  (F.  connaitre),  ‘to know’,  fr.  L.  cognoscere;  see  cognition  and -ance.  E.  cognizance  was  refashioned  after  L. cognoscentia. cognize,  tr.  v,  —  Back  formation  fr.  cognizance. Derivatives:  cogniz-am,  adj.,  cogniz-er,  n. cognomen,  n.,  the  family  name  of  an  ancient Roman.  —  L.  cognomen,  ‘a  Roman  family name,  surname’,  formed  fr.  ndmen  on  analogy of  cognoscere,  ‘to  know’,  which  derives  fr.  no¬ scere,  ‘to  know’  (i.e.  cognomen  stands  to  ndmen, as  cognoscere  to  noscere).  See  nominal  and  cp. cognition. cognominal,  adj.  —  For
--- hammer,\s+n leaf 377
hammer,  n.  — -  ME.  hamur,  hamer,  fr.  OE.  hamor, hamer,  rel.  to  OS.,  OHG.  hamur,  hamar,  ON. hamarr,  Dan.  hammer,  Swed.  hammare,  MDu., Du.,  MHG.  hamer,  G.  Hammer,  ‘hammer’, orig.  ‘stone  hammer';  cogn.  with  OI.  asman-, ‘stone;  rock;  sky’,  Avestic  asman-,  of  s.m.,  Gk. Sxpwv,  ‘(stone)  anvil’,  Lith.  akmuo ,  OSlav. kamy,  ‘stone’.  All  these  words  are  traceable  to hammock hap I.-E.  base  *ak-,  ‘sharp,  pointed’.  See  acrid  and cp.  words  there  referred  to. Derivatives :  hammer,  tr.  and  intr.  v.,  hammer-ed, adj.,  hammer -er,  n.,  hammer-ing,  n.  and  adj. hammock,  n.,  a  swinging  bed  or  couch,  usually made  of  canvas.  —  Sp.  ha
--- acme,\s+n leaf 20
acme,  n.,  the  highest  point.  —  Gk.  axiri),  ‘point, edge;  the  highest  point  of  anything,  the  flower, prime  of  man’s  age’,  rel.  to  ax?),  ‘point’,  and cogn.  with  L.  acies,  ‘point,  edge;  battle  array’, fr.  l.-E.  base  *ak-,  ‘sharp,  pointed’.  See  acrid and  words  there  referred  to,  and  cp.  paracme. Cp.  also  acne. acmite,  n.,  a  sodium  ferrum  silicate  (mineral.)  — Formed  with  subst.  suff.  -ite  fr.  Gk.  axaf,, ‘point,  edge’  (see  prec.  word) ;  so  called  in  allu¬ sion  to  the  crystal  form. acne,  n.,  a  skin  disease  caused  by  the  inflamma¬ tion  of  the  sebaceous  glands  ( med .)  —  This  word owes  its  existence  to  a  cle
--- acetone leaf 19
acetone,  n.,  a  colorless  volatile  liquid,  CH3COCH, (chem.)  —  A  hybrid  coined  fr.  L.  acetum, ‘vinegar’,  and  the  Greek  suff.  -<6vr).  See  acetic and  -one  and  cp.  ketone, acetous,  adj.,  pertaining  to,  or  like,  vinegar; sour  —  Formed  with  suff.  -ous  fr.  L.  acetum, ‘vinegar*.  See  next  word, acetum,  n.,  vinegar.  —  L.  acetum,  ‘vinegar’,  prop. virtum  (acetum),  ‘wine  turned  sour,  neut.  pp.  of acescere,  ‘to  turn  sour’,  fr.  acere,  ‘to  be  sour’, which  is  rel.  to  acer,  ‘sharp’.  See  acrid  and  cp. acescent,  acetic.  For  sense  development  cp.  Gk. 35°?,  ‘wine  vinegar’ ,  which  is  rel.  to  0^04, ‘sharp’. Cp.  also  eisel  and  th
```


## [2026-09-04T19:10:22.069Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,bisect\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nff=[m.start() for m in re.finditer('\\f',d)]\ndef leaf(p): return bisect.bisect_right(ff,p)\nfor p in [r'acrid,\\s+adj', r'vinegar', r'acro-', r'\\bacer\\b,\\s+adj']:\n    m=re.search(p,d)\n    if not m: print(p,'NOT FOUND'); continue\n    print('---',p,'leaf',leaf(m.start()))\n    print(d[m.start():m.start()+900].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T19:10:24.106Z] TOOL RESULT

```
--- acrid,\s+adj leaf 21
acrid,  adj.  —  A  blend  of  L.  deer  (fern,  acris ,  neut. acre),  ‘sharp,  bitter’,  and  acidus,  ‘sour’,  which are  both  related  to  L.  acus,  ‘needle’,  acies,  ‘sharp edge,  point,  the  front  of  an  army,  line  of  battle, battle  array’,  acuere,  ‘to  sharpen’,  fr.  I.-E.  base *ak-,  *aq-,  ‘sharp,  pointed’,  whence  also  Oscan acrid  (=  L.  deriter),  ‘sharply’,  Umbr.  per-acri, ‘fruitful,  fertile’,  Gk.  axpop,  ‘at  the  farthest  point, highest;  pointed’,  4x4),  ‘a  point,  edge’,  4x1?,  ‘a point’,  axavS-a,  ‘thorn,  prickle’,  4 kwv,  ‘a  jave¬ lin’,  4x|X(ov,  ‘an  anvil’,  OI.  asrih,  ‘edge’,  asman-, ‘stone,  rock,  sky’,  Avestic,  asman-,  of  s.m.  Lith. akmuo,  ‘stone’,  asmuo  ,‘sharpness’,  OSlav.  kamy (a  metathesized  form),  ‘stone’,  OIr.  er  (for •akros ),  ‘high’,  Arm.  as-eln,  ‘stone’  (the  force of  the  suff.  -eln  is  yet  unk
--- vinegar leaf 19
vinegar  ( Roman  an- tiq.)  ;  2)  the  cup-shaped  socket  of  the  hip  bone ( anat .);  3)  a  sucker  of  an  octopus,  a  leech,  etc. (zool.)  —  L.  acetabulum,  lit.  ‘a  vessel  for  vinegar’, formed  fr.  acetum,  ‘vinegar’,  with  -dbulum,  a suffix  used  to  form  names  of  tools  and  vessels. See  acetum.  For  the  suff.  cp.  tintinnabulum. Derivatives:  acetabul-ar,  acetabuli-ferous,  aceta- buli-form,  adjs. acetanilide,  also  acetanilid,  n.,  a  crystalline  sub¬ stance,  CjHON  (chem.).  —  A  hybrid  coined  fr. L.  acetum,  ‘vinegar’  (see  acetum),  and  anibd(e). acetarious,  adj.,  used  in  salad.  —  Formed  with suff.  -ous  fr.  L.  acetaria  (pi.),  ‘vegetables  pre¬ pared  with  vinegar,  salad’,  fr.  acetum,  ‘vinegar’. See  acetum  and  -ous. acetate,  n.,  salt  of  acetic  acid  (chem.)  —  Formed with  chem.  suff.  -ate  fr.  L.  acetum,  ‘vine
--- acro- leaf 22
acro- terium,  fr.  Gk.  4xptox4)ptov,  ‘extremity,  sum¬ mit,  top’,  fr.  4xpop,  ‘at  the  end,  outermost’. See  aero-. acrotomous,  adj.,  having  a  cleavage  parallel  with the  base  (mineral.)  —  Gk.  4xp6xopop,  ‘cut  off, sharp,  abrupt’,  compounded  of  ilxpop,  ‘at  the end,  outermost’,  and  -xo|zo?,  which  is  rel.  to x6fj.op,  ‘a  cut,  piece  cut  off,  section’,  xop.6p, ‘cutting’.  See  tome  and  cp.  words  there  refer¬ red  to.  For  E.  -ous,  as  equivalent  to  Gk.  -op, see  -ous. act,  n.  —  F.  acte,  ‘action’,  partly  fr.  L.  actus,  ‘a doing,  an  action’  (fr.  actus,  pp.  of  agere,  ‘to  set in  motion,  drive;  to  do,  act’),  partly  fr.  actum, ‘something  done’  (which  is  prop.  neut.  of  actus, pp.  of  agere).  See  agent  and  words  there  re¬ ferred  to  and  cp.  esp.  entr’acte,  interact. Derivatives:  act,  tr.  and  tr.  v.,  a
\bacer\b,\s+adj NOT FOUND
```


## [2026-09-04T19:10:35.028Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SPG grep athanga\"; grep -n -i \"athanga\\|açanga\\|asanga\\|aganga\\|Stein\" SPG_keilinschriften1881.txt | head -20"
}
```


### [2026-09-04T19:10:35.089Z] TOOL RESULT

```
### SPG grep athanga
258:durch ein Versehen des Steinhauers ausgelassen sein kann.
321:Sug'uda nicht Sug'da steht hier auf dem Steine, wie Rawlinson nach wieder-
330:dem Steine erkennen, nur der Schlussbuchstabe voft agata (1. 21) ist etwas
888:diesem Wort der Steinmetze nach Belieben die Orthographie gewechselt zu
1958:Hochbau von Stein, durch einen Clangenossen des Königs Darius
2019:framaläram, es wird also auch diese Form auf dem Steine stehen.INSCHBIPTEN VON PEESEPOLIS. 53
2539:Es spricht der König Artaxerxes: Diesen steinernen Hochbau
2561:faches steinernes Gebäude auf, zu dem eine Anzahl von Stufen hinauf-
2563:und 10 Fuss Länge, der Boden besteht aus zwei ungeheuren Steinen.
2614:erforderte, war ungeheuer, der ganze Stein ist polirt, wo eine schadhafte78 BIB FUKDOBTE BEB IN8GHBIPTEH.
3093:Das lückenhafte ashm . . • wäre dann vielleicht mit Stein zu übersetzen,
3094:aniyahyä aber in der Bedeutung des Dativs zu fassen: ich warf Steine
3400:Sicherheit auf dem Steine zu erkennen (cf. die krit Bem.), ieh wollte
3820:Äthafigaina hat Oppert gewiss richtig an neup. (^Jum, Stein, (vgl. aw.
3842:Diese Inschrift findet sich auf einem Stein in Suez, nahe bei der
4479:den ursprünglichen Steinhauern zugeschrieben werden, was noch unzu-
4612:sicht des Steines von Behistan gewährte und die RawUnson bald darauf
6149:Atliangaina (ffjf f^f ^fT" TT ^^) steinern acc. dthanffainam L,
6151:Wort mit steinern, indem ich in k die Partikel ft, in thailg aber dasselbe
6152:Wort sehe wie in Neup. iSJ^j Stein, dessen Alter durch die in das
```


## [2026-09-04T19:10:37.259Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### WLD Bd1 ak-\"; grep -n \"ak-, ok-\\|scharf, spitz, kantig\" incoming/WLD/WLD_Bd1_pages.txt | head; echo \"### IEC\"; grep -nE \"^ak[ .]|^akmen|^akri\" IEC.txt | head -10; echo \"### SKT edge/hammer\"; grep -n -E \"^EDGE|^HAMMER|^ACID|^VINEGAR|^ACUTE\" SKT.txt | head"
}
```


### [2026-09-04T19:10:37.360Z] TOOL RESULT

```
### WLD Bd1 ak-
2630:ak- (z. T. auch ak-) „scharf, spitz, kantig; Stein“ (altere Lit. z. B. bei Yf.
### IEC
333:ak “but, and” Lat. ac; W ac; OE ah
346:akris, os “sharp; point. Cf. aKris. WP I, 28, 33 Arm. akir (i-stem and o-stem); Ir. acar, acaire
380:akris, os “point, tip, edge’; pointed, sharp’. WP I, 28. Cf. okris Skt. (ambig.) asrih (*ak- or *ok-); Hitt. cf. hekur (summit. Vocalism obscure); Gk. ákris; ákros; Lat. cf. acer, gs. ácris; Umb. akru-tu (abl.sg. ‘from the beginning"). Osc. akri-d ‘from the top’; Olr. achar, aicher *bit- ter”; aichre ‘fury’; achaire ‘sharpness’; W egr ‘sharp, sour; OE zhher, ear of corn’: OHG ahar, ahir, n. id. (MHG eher: G Aehre); Pol. (ambig.) ostrze 'knife-edge'. See aKtros
381:akris, os “keen, swift. WP I, 28. See akris Lat. áàcer; OBr. ar-ocrion, adj. pl. ‘fierce’ (but see óK-); OCS cf. jastr-ebü (a cpd. = “hawk?)
### SKT edge/hammer
```


## [2026-09-04T19:10:45.058Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,bisect\nd=open('SPG_keilinschriften1881.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n'); offs=[];pos=0\nfor l in lines: offs.append(pos); pos+=len(l)+1\nff=[m.start() for m in re.finditer('\\f',d)]\nfor ln in (3820,6149):\n    lf=bisect.bisect_right(ff,offs[ln-1])\n    print(ln,'leaf',lf)\nprint('----')\nprint('\\n'.join(lines[6142:6160]))\nEOF"
}
```


### [2026-09-04T19:10:46.885Z] TOOL RESULT

```
3820 leaf 113
6149 leaf 174
----
Vgl. oben die kritischen Noten zu der St.
aj (fTf --T0 treiben, stossen (skr. aj, altb. az, griech. lat
ayeiPy agere).
-|- pati. vollführen, ausfechten 3. ps. imperf. pa^^^ato NRa) 47.
Cf. die Bem. zu d. St.
^^W (Th ^'^^^^TT K*") hinüber, in atiyäisha cf. unter i.
Atliangaina (ffjf f^f ^fT" TT ^^) steinern acc. dthanffainam L,
solöcistisch äihanganäm P, 29 (cf. oben p. 116. 127.). Ich übersetze das
Wort mit steinern, indem ich in k die Partikel ft, in thailg aber dasselbe
Wort sehe wie in Neup. iSJ^j Stein, dessen Alter durch die in das
Griechische übergegangene Form nccpaaäyyvs erwiesen ist Ich lese
übrigens äthangaina wie Rawiinson thut, nicht ätha&gina, was auch
möglich wäre. Ueber die Endung aina cf. Gramm. § 35. 11)
Athiy (Tfif T^f ff |f^— ) gegen, Bh. I, 91. J am not quite certain
of the orthography of the word, but I believe the form of athiya to beGLOSSAB. 303
correct" bemerkt Rawlinson in seinem Glossar zu diesem Worte. Cf.
auch oben die kritischen Noten zu d. St. Wenn diese Lesart richtig
ist, muss das Wort mit skr. anti, griech. ^i^^ identisch sein; störend
```


## [2026-09-04T19:10:54.252Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('SPG_keilinschriften1881.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint(len(pages))\np=pages[113]\nprint(p[:1500])\nEOF"
}
```


### [2026-09-04T19:10:56.240Z] TOOL RESULT

```
224
116 n. DABIÜ8.
auch kann v'ithiyä nimmermehr für skr. vijnayä stehen. Rawlinson, der
seine frühere Uebersetzung selbst aufgeg^eben hat, übersetzt zuletzt: a
worthily placed building (or the building of Arda^täna) made for the
family of Darius the king. Norris: marble hall (or areh) built for the
family of Darius the king. Endlich Oppert: Colonnade voüt^e b&tie dans
la maison de Darius. Es bleibt uns nun noch übrig, unsere eigene obige
Uebersetzung zu rechtfertigen.
Was die beiden ersten Wörter betriflfl, so glaube ich, dass nach
Opperts Erörterungen nichts Wesentliches mehr über dieselben zu sagen
ist. Arda wird allgemein als yerwandt mit aw. eredhwo, skr. drdhva,
hoch, angenommen, stäna ist uns bereits in der Bedeutung Ort, Platz
bekannt. Die Benennung hoher Platz passt denn auch ganz gut für die
Gesimse, an welchen diese Inschrift angeschrieben steht. Die scythische
Uebersetzung umschreibt das Wort blos, es ist also entweder Eigen-
name oder Kunstausdruck. Ersteres würde auf R*s oben erwähnte Er-
klärung führen, allein dann würde man Ardastänä erwarten; das Wort
müsste, wie v'ithiyä, im Instr. stehen, und dieser würde auf ä endigen,
mag nun das Thema auf a oder auf n geendigt haben; das Wort muss
also hier nom. eines Masculins sein. Dies ist auffallend, da stänam
sonst immer als Neutr. gebraucht wird, ich halte daher äthafigaina für
das Hauptwort, da es auch im Scythischen mit dem Queerkeil >» aus-
gezeichnet wird, den nur wichtige Wörter und zwar stets Subst. erhalten.
Äth
```


## [2026-09-04T19:11:05.699Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2625,2660p' incoming/WLD/WLD_Bd1_pages.txt; echo \"=== find pdf page tag\"; awk 'NR<=2640 && /\\[pdf page/ {last=$0; ln=NR} END{}' incoming/WLD/WLD_Bd1_pages.txt; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd1_pages.txt | awk -F: '$1<2640' | tail -3"
}
```


### [2026-09-04T19:11:07.573Z] TOOL RESULT

```
dafiir) ;doch kann trotzdem haurire die urspriingliche Lautung gewesen
sein, woraus vulgar drire.     Bewiesen ist daber Einmischung eines zu Wz.
*ghos- .,fressen, verzehren“ gehorigen Vidrio „fresse“ (Gunther aaO.) nicht.


ak- (z. T. auch ak-) „scharf, spitz, kantig; Stein“ (altere Lit. z. B. bei Yf.
    LEWb. 2 7, Boisacq 32 f„ 36, 37).
   Mit r-Formantien:
   ai. agri-h „Ecke, Kante,     Schneide“, catur-agra- „viereckig“ (vielleicht
bloB mit Ersatz des ?'-St. dureh den a-St. in der Zs. nach Wackernagel
Ai. Gr. 2, 1, 119, also dann nur zufallig sich deckend mit:) gr. axgog
„spitz“, dy.gov, ay.oa, dy.otg „Spitze, Berggipfel“ (auch in axg-odopeu als
„scharfes Gehor haben, das Ohr spitzen“, und axgig-, -idog „Heuschrecke“,
nach Prellwitz 2 22 Kurzform fur aygofiaxovoa „auf den FnBspitzen gehend“,
axgiCovoa; dy.gepeov ,.Ende des Astes, Wipfel“, s. zur Bildung Brugmann
Grdr. II 2 1, 241); lat. (mit Dehnstufe) Clcer, acr is, -c (altlat. acra, -tan)
„scharf ‘. osk. akrid „acri oder acriter", umbr. peracri- „opimus“ (= lat.
               -




perfreer, Brugmann BSGW. 1893, 144ff., v. Planta II 28, Fay Cl. Qu. 4, 83,
vgl. zur Bed. gr. dy.gog, auch „oberst, vortrefflich“, und dxuaiog), lat. aeer-
bus „herb, sauer, traurig“ (aus * ucri-dho-s oder eher *acri-clho-s mit der-
 selben Yokalkiirzung vorgeschlossener Tonsilbe wie in mblestus gegeniiber
moles;  Fay IF. 26, 34, 36, Brugmann Grdr. II 2 1, 383), acervus „Haufen“
(wenn eigentlich „Steinhaufen“; Gdf. *acri-uo-s Yf. LEWb. 8, oder acerg-             ,


uo-s Petersson IF. 24, 269ff, vgl. gall. AXPOTALVS d. i. „mit hoher
           ,


Stirn“, air. er „hock“ (aus *akros dagegen air. acher „scharf, vom Winde“,
                                                           ;
=== find pdf page tag
```


## [2026-09-04T19:11:14.245Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2660,2780p' incoming/WLD/WLD_Bd1_pages.txt | grep -n -i \"asman\\|asenga\\|acanga\\|athanga\\|akmen\\|Amboss\\|Himmel\\|Mühlstein\\|npers\" "
}
```


### [2026-09-04T19:11:14.301Z] TOOL RESULT

```
93:   ai. dqman- m. „Stein, Fels; Himmel“ (zur Yorstellung des Himmels als
96:auf einen r-w-St., s. Meillet Ft. 424, Berneker 478), av. asman- „Stein,
97:Himmel“, asmana- „steinern“, ap. asman- „Himmel“ f ai. gen. dniali instr.                                        ,
```


## [2026-09-04T19:11:16.563Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2745,2790p' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-04T19:11:16.625Z] TOOL RESULT

```
mbret.     ebil       „Pflock,             Stift,    Kagel" (urkelt. *aiuilio-s; Pick II 4 5, Zupitza
GG. 63).
  Mit jw-Formantien:
   gr. dxjnrj „Spitze, Schneide, Scharfe; hochster Punkt, Hobepunkt (des
Lebens); Entscheidungspunkt“ (ay./ugv Adv., axpaios, dy./udCco ), schwed.
dial, dm „Sumpfgras, Cladium Mariscus“ (Gdf. grm. *abna-, vgl. finn. Lw.
ahma „equisetum“);
   ai. dqman- m. „Stein, Fels; Himmel“ (zur Yorstellung des Himmels als

eines Steingewolbes s. Beichelt IF. 32, 23 ff.), acmard- „steinern“ (weisen
auf einen r-w-St., s. Meillet Ft. 424, Berneker 478), av. asman- „Stein,
Himmel“, asmana- „steinern“, ap. asman- „Himmel“ f ai. gen. dniali instr.                                        ,



acnd, av. gen. a mo, abl. asnuat nach J. Schmidt Krit. SS f. mit -n- aus
-mn- und darum nicht unmittelbar den n-Bildungen vergleichbar instr.                                             ;



pi. ai. agnaih nach den o-St.); av. asongo-gav- „mit Hiinden aus Stein“.
ap. adan yaina- „stoinern“ (mit -g- aus dem n. sg. des rjn- St., s. Bartho-
lomae IF. 2, 269 ob auch hier -n- auf -mn- zuriickgeht, ist sehr fraglich,
                                ;


und urspriingliches *ak-en-g- weit wahrscheinlicher) gr. uyguov „AmboB
                                                                                                                               !!

                                                                                           ;


ux/uwv 6 ovgarog (s. Reichelt aaO. 26); gall, aumnum „saxum“ (aus *akamno-
mit friiher Lenierung des m zu w?); lit. asmno -ehs „Schiirfe“, lett. asmens      ,


m. „Schneide‘ lit. akmud, -ens „Stein“, aksl. kanuj, -cne „Stein“ (Umstellung
                       :


                           ,


aus *akmy, das durch Anlautdehnung aus *dkmon entstanden sei, erwagt Ber-
neker 47S wo Lit. iiber andere Erklarungen von diesen bevorzuge ich die Iler-
                                                                            :
```


## [2026-09-04T19:11:24.190Z] TOOL CALL #66: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T19:11:24.198Z] TOOL RESULT

```


```


## [2026-09-04T19:11:29.907Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82e%E1%B8%B1-",
 "prompt": "Give the reconstructed root, its meaning, and all listed derivatives (especially *h₂éḱmō 'stone/heaven', Greek akros/oxus, Latin acer/acus, Germanic *agjō, *hamaraz, Indo-Iranian aśman-). Quote the etymology notes verbatim where possible."
}
```


## [2026-09-04T19:11:31.550Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B3%DB%8C%D8%A7",
 "prompt": "Give the Persian entry آسیا: meaning and full etymology (Middle Persian form, Proto-Iranian, relation to asan- 'stone'). Also any related terms like آسیاب, آس, بادآس. Quote verbatim."
}
```


### [2026-09-04T19:11:36.630Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂eḱ-

## Root and Meaning
The reconstructed root is **\*h₂eḱ-**, meaning "sharp."

## Major Derivatives

**Key formations include:**

- **\*h₂eḱ-u-**: Latin *acus*, Latvian *ass* ("sharp")
- **\*h₂éḱ-mō ~ \*h₂ḱ-m̥n-és**: "stone" (referenced in derived terms)
- **\*h₂éḱ-ih₂ ~ h₂ḱ-yéh₂-s**: Latin *aciēs* ("sharp edge")
- **\*h₂ḱ-méh₂**: Ancient Greek *ἀκμή* (akmḗ)
- **\*h₂óḱ-s-u-**: Ancient Greek *ὀξύς* (oxús)
- **\*h₂eḱ-stí-**: Lithuanian *akstis* ("spit, thorn"), Russian *ость* (ostʹ)
- **\*h₂(e)ḱ-i-**: Ancient Greek *ἀκίς* (akís)

The root disperses across Latin, Greek, Germanic, Balto-Slavic, and other Indo-European language families, consistently expressing concepts related to sharpness, pointed objects, and related semantic extensions.
```


### [2026-09-04T19:11:37.789Z] TOOL RESULT

```
# Persian Entry آسیا

Based on the Wiktionary page provided, here's what's documented:

## Meaning
The Persian entry آسیا (āsiyā / âsiyâ) has two definitions:

1. **Asia** - "the largest continent, located between Europe and the Pacific Ocean"
2. **Historical Asia** - "an ancient province of the Roman Empire in western Anatolia, existing between 133 BC and the 7th century AD"

## Etymology
**The page does not provide etymological information for the Persian entry.** Unlike the Ottoman Turkish sections, which include detailed etymologies tracing the word back through Italian, Latin, Ancient Greek, Mycenaean Greek, and Hittite, the Persian section contains only pronunciation data and definitions.

## Related Terms
The page lists one derived term:
- **آسیایی** (âsiyâyi) - an adjective form

One alternative form is noted:
- **آسیاب** (âsiyâb) - described as an alternative form in Etymology 2's noun section

**Note:** The document does not mention Middle Persian forms, Proto-Iranian connections, relations to asan- 'stone', or etymologies for آس or بادآس.
```


## [2026-09-04T19:11:43.075Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B3%DB%8C%D8%A7%D8%A8",
 "prompt": "Persian آسیاب: meaning and etymology. Quote the etymology section verbatim, including Middle Persian and Proto-Iranian forms and any mention of āb 'water' or as- 'stone'."
}
```


## [2026-09-04T19:11:44.954Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D9%85%D8%A7%D9%86",
 "prompt": "Persian آسمان: meaning and etymology. Quote verbatim, including Middle Persian, Old Persian asman-, Avestan asman-, Proto-Indo-European *h₂éḱmō and any note about the meaning 'stone/sky'."
}
```


### [2026-09-04T19:11:48.675Z] TOOL RESULT

```
# Persian آسیاب: Etymology

The word **آسیاب** (āsiyāb / âsiyâb) derives from Middle Persian and carries the meaning of "mill" or "watermill."

## Etymology Section

According to the Wiktionary entry, the term originates as follows:

"From Middle Persian [Book Pahlavi needed] (ʾsyʾp̄ /⁠āsyāb⁠/). By surface analysis, _آس_ (ās / âs, 'millstone') +‎ _ـیـ_ (-y-, linking element) +‎ _آب_ (āb / âb, 'water')."

The word thus compounds "millstone" with "water," reflecting its original referent—a water-powered grinding device. The entry also notes a related term, آسباد (âsbâd, "windmill"), demonstrating variant applications of the root concept.
```


### [2026-09-04T19:11:52.902Z] TOOL RESULT

```
# Persian آسمان: Meaning and Etymology

**Meaning:** The Persian word آسمان (āsmān) means "sky" or, in literary contexts, "heaven."

**Etymology Summary:**

The word inherited from Middle Persian آسْمَان (āsmān), which derived from Old Persian 𐎠𐎿𐎶𐎠𐎴𐎶 (asmānam). This ancient lineage traces back through Proto-Iranian *Hácmā and Proto-Indo-Iranian *Háćmā to the Proto-Indo-European root *h₂éḱmō.

**Key Etymology Note:**

The Proto-Indo-European foundation *h₂éḱmō originally meant "stone" but underwent semantic shift to denote "sky" or "firmament" in the Iranian branch. This transformation reflects how the concept evolved from the literal (stone/hard substance) to the celestial (sky as a hard dome or vault).

The word shares cognate status with Sanskrit अश्मन् (áśman, "stone"), demonstrating the semantic divergence between Indo-European language families in their treatment of this ancient root.
```


## [2026-09-04T19:11:59.248Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%86%DA%AF",
 "prompt": "Persian سنگ (sang): meaning and etymology, quoted verbatim — Middle Persian, Old Persian aθanga-, Avestan asenga-, Proto-Iranian, PIE. Also note any derived terms."
}
```


## [2026-09-04T19:12:01.365Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%86%D8%AC%DB%8C%D8%AF%D9%86",
 "prompt": "Persian سنجیدن (sanjidan): meaning and etymology quoted verbatim. Which root does it come from (*θanj- 'to pull/draw'?), what is the past stem (سختن saxtan)? Any mention of سنگ 'stone'?"
}
```


### [2026-09-04T19:12:05.496Z] TOOL RESULT

```
# Persian سنگ (sang)

## Meaning
The primary sense is "stone" or "rock." Secondary meanings include "tombstone" and an archaic sense of "authority" or "dignity." A dated usage refers to "weight," "value," or "worth."

## Etymology
According to the Wiktionary entry, the word is "inherited from Middle Persian _sng_ (sang, 'stone, rock')." The etymological chain extends backward through Proto-Iranian *Hacangáh, ultimately connecting to Proto-Indo-European roots.

## Related Historical Forms
The entry documents cognates across Old Iranian languages:
- Old Persian: aθaⁿga-
- Avestan: asenga-

## Derived Terms
The entry lists numerous compounds, including:
- سنگدل (sangdel)
- سنگین (sangin)
- سنگک (sangak) — a type of flatbread
- سنگسار (sangsâr)

The word has also spawned descendants in other languages, including Hindi संग (saṅg), Punjabi ਸੰਗ (saṅg), and Ottoman Turkish.
```


### [2026-09-04T19:12:06.884Z] TOOL RESULT

```
# Etymology of سنجیدن (sanjidan)

**Root Origin:** The word traces to the Proto-Iranian root *θanǰ- meaning "to weigh," derived from Proto-Indo-European *t(ʰ)engʰ-, which means "to draw, pull back."

**Past Stem:** The past stem is **سنجید** (sanjid), not derived from سختن (saxtan). However, سختن represents an earlier form of the verb: "From earlier سختن (saxtan), from Middle Persian."

**Connection to سنگ (sang):** Yes, there is a connection. The entry lists "سنگ (sang, 'weight')" as a derived term, indicating semantic relationship between the verb "to weigh/measure" and the noun for weight/stone. The semantic link reflects the root's original sense of weighing or measuring by weight.

The verb developed four main meanings: to weigh (archaic/dialectal), to measure, to evaluate, and to ponder/reflect.
```


## [2026-09-04T19:12:13.960Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%AC%D9%8A%D9%84",
 "prompt": "Arabic سجيل (sijjīl): meaning and etymology quoted verbatim. Does it derive from Persian سنگ گل (sang-gil) 'stone-clay', or from Greek/Latin sigillum? Give both views if listed."
}
```


## [2026-09-04T19:12:15.434Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/vinegar",
 "prompt": "Give the full etymology entries for vinegar (and any linked acid, acetum) verbatim: Old French vin aigre, Latin acer/acetum, PIE root *ak-."
}
```


### [2026-09-04T19:12:16.004Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T19:12:22.877Z] TOOL RESULT

```
# Etymology of Vinegar

**Vinegar (early 14c.):**
"diluted impure acetic acid" from Anglo-French and Old French _vinaigre_, meaning "vin 'wine' + aigre 'sour'." The Latin equivalent was _vinum acetum_ ("wine turned sour"), shortened to _acetum_.

**Acetum (Latin):**
_Acetum_ originally functioned as "the past participle of _acere_ 'be sharp; be sour'" and was also used figuratively for "wit, shrewdness."

**Aigre (Old French):**
Meaning "sour, acid; harsh, bitter, rough," this term derived from Vulgar Latin _\*acrus_, which connects to Latin _acer_ ("keen, sharp, pointed, piercing").

**PIE Root \*ak-:**
The ultimate origin traces to the Proto-Indo-European root "_ak-_" signifying "be sharp, rise (out) to a point, pierce." This same root underlies Greek _oxys_ ("sharp") and _oxos_ ("wine vinegar").

The etymological chain demonstrates how the concept of sourness linguistically connects to sharpness and piercing sensations across multiple language families.
```


## [2026-09-04T19:12:26.376Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%AC%D9%91%D9%8A%D9%84",
 "prompt": "Arabic سِجِّيل (sijjīl): meaning and etymology quoted verbatim. Persian sang-gil or Greek sigillum?"
}
```


## [2026-09-04T19:12:27.075Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/acrobat",
 "prompt": "Full etymology of acrobat verbatim: French acrobate, Greek akrobates, akros, PIE *ak-. Also date of English adoption."
}
```


### [2026-09-04T19:12:28.274Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T19:12:33.610Z] TOOL RESULT

```
# Etymology of Acrobat

**Origin Date:** 1845

**Language Path:** The word entered English from French *acrobate* (14th century), which derived from a Latinized form of Greek *akrobatēs* meaning "rope dancer, gymnastic performer."

**Root Components:** The Greek term combines:
- *akros* ("topmost, at the point end") from PIE root *\*ak-* ("be sharp, rise to a point, pierce")
- Greek agential element *-batēs* ("one that goes, one that treads") from *bainein* ("to go, walk, step"), rooted in PIE *\*gwa-* ("to go, come")

**Key Quote:** The word is "related to *akrobatos* 'going on tip-toe, climbing up high'" and combines elements meaning "sharp/pointed" with "one who goes/walks."

The term essentially describes someone who walks or climbs to high, pointed places—an apt description for tightrope walkers and gymnastic performers.
```


## [2026-09-04T19:12:38.475Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/oxygen",
 "prompt": "Full etymology of oxygen verbatim: French oxygène, Lavoisier, Greek oxys, PIE *ak-, and dates."
}
```


## [2026-09-04T19:12:39.278Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hammer",
 "prompt": "Full etymology of hammer verbatim: Old English hamor, Proto-Germanic *hamaraz, connection to 'stone tool', Old Church Slavonic kamy, Sanskrit asman, PIE *ak-."
}
```


### [2026-09-04T19:12:43.659Z] TOOL RESULT

```
# Etymology of Oxygen

The word "oxygen" originates from French chemist Antoine-Laurent Lavoisier, who coined it in 1777. The term combines two Greek-derived elements:

- **Oxys** ("sharp, acid") from the Proto-Indo-European root *ak- meaning "be sharp" or "pierce"
- **-gène** ("something that produces") from Greek -genēs

Lavoisier intended the compound to mean "acidifying principle," essentially a Greek rendering of the French *principe acidifiant*. This reflected the contemporary (but incorrect) belief that oxygen was essential for acid formation.

The element itself had been isolated earlier by Joseph Priestley in 1774, who called it "dephlogisticated air" under the phlogiston model of chemistry. When that theory fell out of favor, Lavoisier's new nomenclature became the standard. The term "oxygen-mask" appeared by 1912.
```


### [2026-09-04T19:12:53.774Z] TOOL RESULT

```
# Etymology of "Hammer"

The word "hammer" has ancient roots tracing back through multiple language families. According to the Online Etymology Dictionary, the term comes from "Old English _hamor_ 'hammer,' from Proto-Germanic _\*hamaraz_."

## Original Meaning

The original sense likely referred to a tool with a stone head. The Old Norse cognate _hamarr_ meant "stone, crag," suggesting the Germanic words derived from "a PIE _\*ka-mer-_" with sound reversal, ultimately connected to "_\*akmen_ 'stone, sharp stone used as a tool.'"

## Semantic Evolution

Beyond its primary meaning as a striking tool, "hammer" gained several specialized uses:
- In firearms (1580s)
- As a piano component (1774)
- To describe a small ear bone (1610s)

The phrase "hammer and tongs" (1708) references blacksmithing imagery, while "hammer and sickle" (1921) became symbolic of Soviet communism, representing industrial and agricultural labor.

## Verb Form

The verb emerged in the late 14c., initially meaning "deal blows with a hammer or axe," later expanding to figurative uses like "work (something) out laboriously" (1580s).
```


## [2026-09-04T19:12:56.706Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/edge",
 "prompt": "Full etymology of edge verbatim: Old English ecg, Proto-Germanic *agjo, PIE *ak-."
}
```


## [2026-09-04T19:12:59.125Z] TOOL CALL #80: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%DA%86%D8%A7%D8%B1",
 "prompt": "Persian آچار: all etymologies and senses (pickle; wrench). Quote the etymology verbatim — is it from Latin acetaria, from Sanskrit, or unknown/uncertain? Any Turkish origin for the 'wrench' sense?"
}
```


### [2026-09-04T19:13:02.456Z] TOOL RESULT

```
# Etymology of "Edge"

The word "edge" has ancient roots tracing back through multiple language families. It originates from Old English *ecg*, meaning "corner, edge, point," which also referred to a sword in poetic contexts.

The term evolved from Proto-Germanic *agjo*, which appears in related forms across Germanic languages—Old Frisian *egg*, Old Saxon *eggia*, and Old High German *ecka*. These all share a common ancestor in the Proto-Indo-European root *ak-, meaning "be sharp, rise (out) to a point, pierce."

As a noun, "edge" has maintained its core meaning of a sharp or thin border. The verb form emerged in the late 13th century with the sense of "to give an edge to." By the 1620s, it acquired the nautical meaning of moving edgeways, and by 1953, it came to mean defeating someone by a narrow margin.

The modern spelling shift from Old English *-cg* to Middle English *-gg* to Modern English *-dge* reflects broader pronunciation changes in the language's development. Phrases like "on edge" (meaning excited or irritable) date to 1872, while "have one's teeth on edge" is documented from the late 14th century.
```


### [2026-09-04T19:13:04.740Z] TOOL RESULT

```
# Etymology of Persian آچار (āčār)

## Pickle/Marinade Sense

The etymology is **not** from Latin or Sanskrit. According to the source, it derives from Middle Iranian origins, specifically:

"Originally *'spice, garnish', from a similar Middle Iranian source as Middle Persian" and traces back to a "Proto-Iranian compound *Habí-čārna-" with ultimate roots in Proto-Indo-European.

## Wrench/Spanner Sense

This sense has a **different origin**. It was "Borrowed from Azerbaijani _açar_" (meaning "key"), representing a modern Iranian Persian adaptation rather than a historical linguistic development.

The two senses represent distinct etymological paths—the marinade meaning has deep Indo-European ancestry, while the tool meaning is a recent borrowing from Azerbaijani Turkish.
```


## [2026-09-04T19:13:11.960Z] TOOL CALL #81: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%AC%D9%8A%D9%84#Arabic",
 "prompt": "Arabic سجيل: etymology and meaning. Quote verbatim."
}
```


## [2026-09-04T19:13:13.376Z] TOOL CALL #82: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%9A%E0%A4%BE%E0%A4%B0",
 "prompt": "Hindi अचार: meaning and etymology quoted verbatim (from Persian آچار?)."
}
```


### [2026-09-04T19:13:13.417Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T19:13:18.620Z] TOOL RESULT

```
# अचार (Achar)

**Meaning:** According to the Wiktionary entry, अचार refers to "a spicy and salty pickle of Indian cuisine."

**Etymology:** The word was "Borrowed from Classical Persian _آچَار_ (āčār)." This Persian origin applies across multiple South Asian languages documented here—Bhojpuri, Hindi, and Magahi all trace their versions back to the same Persian source. Nepali borrowed it through Hindi rather than directly from Persian.

The term appears in at least nine languages and represents a culinary concept that traveled from Persian-speaking regions into South Asian food traditions.
```


## [2026-09-04T19:13:26.165Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### AFM\"; grep -n \"سجيل\\|سجّيل\\|سنك كل\\|سنگ گل\" AFM.txt AFM_pages.txt 2>/dev/null | head -5; echo \"### ARB\"; grep -n \"سجيل\" ARB_mo3rb.txt ARB_abdulraheem.txt 2>/dev/null | head -5; echo \"### TAD\"; grep -n \"سجيل\" TAD.txt TAD_pages.txt 2>/dev/null | head -5; echo \"### AFA\"; grep -n -i \"siggil\\|sigill\\|sang\" AFA.txt | head -5"
}
```


### [2026-09-04T19:13:26.265Z] TOOL RESULT

```
### AFM
### ARB
ARB_mo3rb.txt:762:لكنة أعجمية» لا مثالّ لها فى حروف العرب » وتسجيل هذه الغرائب من الروف» 
ARB_mo3rb.txt:1409:وتسجيلها » وتعليمهم كف بعححون أصول كتهم على الشيوخ 6 وكيف يحفظونا 
ARB_mo3rb.txt:13825:٠ فى ب « والسجيل » الواوليست ف النسخ المخطوطة‎ )١( 
ARB_mo3rb.txt:13827:: ** وقد اختلف فى كلهة *” السجيل‎ ٠ هكذا أطلق المؤاف القول تقلءد! لابن نتيبة‎ (١ 
ARB_mo3rb.txt:13831:ومن كلام الفرس ما لا يخصى‎ ٠ فقسد بين ألعرب ما عنى سجيل‎ ٠ ) لزسل علهسم خارة ءن طين‎ ( 
### TAD
### AFA
2176:^^jSV^ = »sigillatus**; Mu^arrab 82 auch ganz richtig
15051:sang
```


## [2026-09-04T19:13:29.827Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13815,13840p' ARB_mo3rb.txt; echo \"=== AFA\"; sed -n '2168,2182p' AFA.txt"
}
```


### [2026-09-04T19:13:29.886Z] TOOL RESULT

```
8 قال ان قتدبة : 2 الل “ بالفارسية : ” سك 1 الم و« كن > ل 


0 
غارة وطين ٠.‏ 


٠ فى ب « والسجيل » الواوليست ف النسخ المخطوطة‎ )١( 

: ** وقد اختلف فى كلهة *” السجيل‎ ٠ هكذا أطلق المؤاف القول تقلءد! لابن نتيبة‎ (١ 
وف اللسان : « قال أهل‎ ٠ وه من الألفاظ القرآنية‎ ٠ فى معناها » وق أتهباعربية أو معربة‎ 
قال الازهيرى” : والذى عندثنا رالله أعل : أنه إذا كان‎ ٠ الأفة : هذا فارسى ؛ والعرب لا تعرف هذا‎ 
: التفسير صصبحا فهو فارمى أعررب » لأن الله :عالى قد ذكر هذه اخارة فى قصة قوم ارط ققال‎ 
ومن كلام الفرس ما لا يخصى‎ ٠ فقسد بين ألعرب ما عنى سجيل‎ ٠ ) لزسل علهسم خارة ءن طين‎ ( 
قال أبوعييدة:‎ ٠ قد أعر بته العرب » نحو جاموس ودياج» فلا أن أت يكون هذا ما أعرب‎ )# 
وقال بهطمم : جيل من‎ ٠ من مل » تأو يله : كثير شديد .., قال : وسمين وسميل يمعنى واحد‎ 
: أعنلته ؛ إذا أرسته » فكأتها مرسله علييسم » ء ثم تقل عن أنى إسحق قال : «دقيل : من حول‎ 
قال : وهذا القول إذا فسر هو أ ينها » لأن مر كاب الله‎ ٠. كقواك من محل ؛ أى ما كتب لم‎ 
كاب‎ ٠ وما أدراك ما سمين‎ ٠ قال الله تعالى : ( كلا إن كَاب الفجار لنى مين‎ ٠ تصالى ديلا عليه‎ 
: وسميل فى معتى “ين © ألمنى : أنها خارة فا كتب الله تعالى أنه يسذبهم بها. قال‎ ٠ ) عقوم‎ 
قالوا » وانظر التفصيل فى اللسارف وى كتب‎ ١ وهذا أحسن ما م'فيا عندى »4 . هذا بعض‎ 
6“ والدذى أراه أرح وأحم » أنها عرية ؛ لأنها لوكانت معرية عن *” سنك © و”” كل‎ ٠ التفسير‎ 
معى : ججارة وعاين » للا جاءت وصدفا لحجارة » لأن لاظها حبنه_1 يدل على اخوارة » فلا يوصف‎ 
=== AFA
8 a. f . (Dozy vetements 261) , das nach Gauh. ein grünes
Kleid ist, wage ich nichts zu sagen. i^.Jlim »Indigo"
(auch persisch bei VuUers II. 240. 11 JuJ) wird schwer-
lich damit etwas zu thun haben , da es gewiss nichts an-
deres ist , als 'laartc. Aber auch zu arab. i^Jum wird man
es kaum stellen wollen; ebenso wenig zu dem, überdies
unsicheren D^^D Levy, Nhbr. Wtb. III. 480.
Swhon von den Arabern als fremd erkannt ist ^mioikAm *
^^jSV^ = »sigillatus**; Mu^arrab 82 auch ganz richtig
durch i^L^ erläutert. Ob die Bedeutung > Decke" b^rün-
det ist, ist nicht mehr festzustellen.
Neben den Gewändern , die aus dem Norden und Osten
nach dem ^i^z kamen , sind hauptsachlich die jemenischen
Gewänder zu nennen, die viel begehrt und verbreitet wa-
ren. Bezeichnend dafür ist, dass bei der Eroberung Jemens
```


## [2026-09-04T19:13:42.666Z] TOOL CALL #85: WebFetch

```json
{
 "url": "https://www.vajehyab.com/moein/%D8%A7%D8%B3%D8%AA%D9%86",
 "prompt": "What does Mo'in's Farhang-e Farsi give for the headword استن? Is there an entry meaning 'acetone' with a French origin tag [فر.]? Quote it."
}
```


## [2026-09-04T19:13:43.655Z] TOOL CALL #86: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D8%AA%D9%86",
 "prompt": "Persian استن: list all senses and etymologies. Is one of them 'acetone' borrowed from French acétone?"
}
```


### [2026-09-04T19:13:46.797Z] TOOL RESULT

```
Based on the webpage content provided, Mo'in's Farhang-e Farsi dictionary gives the following entry for the headword استن:

"(اُ تُ) (اِ.) = استون : ستون ، رکن"

This indicates the word means "column" or "pillar" (ستون) and "foundation/pillar" (رکن).

There is **no entry for acetone with a French origin tag [فر.]** shown in the content displayed on this page.
```


### [2026-09-04T19:13:49.208Z] TOOL RESULT

```
I cannot answer your question based on the provided content. The webpage shown is the English Wiktionary entry for the Arabic word **استن** (istanna), which is a verb meaning "to clean and polish one's teeth" and has several other meanings related to prescribing laws, sharpening knives, and flowing quickly.

The page does not include information about the Persian word **استن** or its meanings. While the page header indicates that this entry exists in Persian Wiktionary (among French, Hungarian, and Kurdish versions), the actual Persian definitions are not displayed in the content provided.

To answer whether Persian **استن** means "acetone" or relates to the French "acétone," you would need to access the Persian Wiktionary entry directly.
```


## [2026-09-04T19:13:59.508Z] TOOL CALL #87: WebFetch

```json
{
 "url": "https://www.vajehyab.com/moein/%D8%A7%D8%B3%DB%8C%D8%AF",
 "prompt": "What does Mo'in's Farhang-e Farsi give for اسید? Quote the entry including any origin tag such as [فر.] (French)."
}
```


## [2026-09-04T19:14:00.524Z] TOOL CALL #88: WebFetch

```json
{
 "url": "https://www.vajehyab.com/moein/%D8%A7%D8%B3%D8%AA%D9%88%D9%86",
 "prompt": "What does Mo'in's Farhang-e Farsi give for استون? Quote all senses and any origin tags (e.g. [فر.] French, acetone)."
}
```


### [2026-09-04T19:14:03.200Z] TOOL RESULT

```
According to Mo'in's Farhang-e Farsi, the entry for اسید (acid) is:

"( اَ ) [ فر. ] (اِ.) هر جسم هیدروژن داری که به حالت محلول ، یون هیدروژن (پروتون ) آزاد کند"

The entry includes the origin tag [فر.] indicating French origin, and defines acid as a hydrogen-containing substance that releases hydrogen ions (protons) in solution and forms salts, noting that most acids are corrosive and have a sour taste.
```


### [2026-09-04T19:14:14.351Z] TOOL RESULT

```
# Mo'in's Farhang-e Definition of استون

According to the dictionary entry shown, Mo'in's Farhang-e Farsi provides this definition:

**"(اُ) [ په . ] ( اِ.) ستون ، پایه"**

This indicates two senses:
1. **ستون** (setoon) - pillar/column
2. **پایه** (pāyeh) - base/foundation

The entry includes a phonetic notation but does not provide an explicit origin tag (such as [فر.] for French or other language markers) for the word استون.
```


## [2026-09-04T19:14:21.285Z] TOOL CALL #89: WebSearch

```json
{
 "query": "\"استن\" معین \"فر.\" استون acetone فرهنگ فارسی معین شیمی"
}
```


### [2026-09-04T19:14:28.651Z] TOOL RESULT

```
Web search results for query: ""استن" معین "فر." استون acetone فرهنگ فارسی معین شیمی"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T19:14:34.298Z] TOOL CALL #90: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B3%D8%AA%D9%86/",
 "prompt": "List all dictionary entries for Persian استن (Dehkhoda, Mo'in, Amid). Is any sense 'acetone' (استون) borrowed from French acétone? Quote."
}
```


### [2026-09-04T19:14:42.918Z] TOOL RESULT

```
# Persian Dictionary Entries for استن

Based on the Abadis dictionary content, here are the main entries:

## Dehkhoda Dictionary
1. **آستن (sleeve)**: "آستین" - the sleeve of a garment
2. **استن (verb)**: The infinitive "to be" with conjugations: استم، استی، است، etc.
3. **استن (column)**: "ستون" - a pillar, support structure, or architectural element
4. **استن (tree root)**: A decayed tree root or trunk with dispersed branches

## Mo'in Dictionary
**اَ س ِ تُ استن**: "مایعی است بی رنگ، فرار، سریع التبخیر و قابل اشتعال" (a colorless, volatile, flammable liquid used as solvent)

## Amid Dictionary
Defines استن as: "ستون: رکن" (column: pillar/support)

---

## Regarding "Acetone"
The dictionary confirms acetone sense exists but does **not explicitly state** French etymology. The Mo'in entry notes it derives "از تقطیر یکی از استات ها" (from distillation of acetates), suggesting a chemical rather than linguistic origin for the Persian term.
```


## [2026-09-04T19:14:50.492Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### IEC akmen\"; grep -nE \"^akmon|^akmen|akmon,|akmen,\" IEC.txt | head -5; echo \"### SKT\"; grep -nE \"^Edge|^Hammer|^Acid|^Vinegar|^Acrobat|^Oxygen\" SKT.txt | head; echo \"### RCH achar\"; grep -n -i \"achar\\|A'char\" RCH.txt | head -5"
}
```


### [2026-09-04T19:14:50.579Z] TOOL RESULT

```
### IEC akmen
### SKT
### RCH achar
15305:p   bachark  or  bichirky  Derided,  mocked.  A   dup^.
45809:A   4^j  zakanjf  (or  \ijj  zakarlya)^  (Heb.  nn3?)  Zachariai*
79849:machargy  Ordering  any  one  to  work  gratuitously. nutchafsy  Do  not  stick.
98111:a]^j  zoqfrd^  (fern,  of jfji  azejar)  Timid,  trembling  (female). zcqfargar  (or  zoachargar)y  A   chief,  interpreter of  the  law,  a   cl^ef  justice,  a   mufti.
```


## [2026-09-04T19:14:53.600Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### IEC akmen variants\"; grep -n \"akmen\\|akmon\\|akmn\" IEC.txt | head -8; echo \"### SKT sample headwords\"; grep -n -m3 \"EDGE\\|HAMMER\" SKT.txt | cut -c1-300"
}
```


### [2026-09-04T19:14:53.678Z] TOOL RESULT

```
### IEC akmen variants
340:9 akmó(n), akmen- — akmo(n), aKmen-
341:akmó(n), akmen- ‘stone, boulder, crag’. WP I, 29, 33. Cf. aKmo(n)
342:OCS kamy, gs. kamene; Srb. kam, kamen; Li. akmuo, eps Latv. akmens
6232:distinguishes relationship from content, as in Cz. krevní ‘relating to blood": Li. kraujinis, id., cf. the Ligurian river-name Beverin (in the Engadine), and the Sequanian aidrini “bright in the Coligny weather-diary, cf. Gk. aithrinós “of early morning’. The passage from adj. to noun is illustrated in Arm. grean, gs greno Cliterature': gir ^writing"); cf. also Per. pūst- in (ffurcoat? :püst (fur); Gk. eruthrinos Ca red fish": eruthrós); Alb. dulli, gs dullini (ju- niper, lit. ‘fragrant bush’, cf. dhülos (1) above); Lat. scrinium (^writing-case' in rela- tion to scribo); sterquilinium (tdungheap'": stercus); Ir. goirm-ín (*woad, indigo’: gorm “blue”); Li. gandrynas (‘swarm of storks’: gañ- dras); akmenynas, akmenjne (‘pile of stones? :akmuoó). For the fem. suffix cf. Alb. kopshtin- je (market garden’ : kopsht *garden"). An ad- jectival extn. of an adj. occurs in Skt. navinah (new': navah), and cf. Arm. mi£in (‘mid- most': me£). A dim. extn. arises in Ir. goib-ín (small mouth": gob) and in Go. gait-ein Cd": gaits); W dern-yn (‘small piece’: darn); Li. merg-inà ("little girl: mergà)
### SKT sample headwords
14200:PLEDGE.
16814:SEDGE,
```


## [2026-09-04T19:14:57.904Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -A4 \"^EDGE,\" SKT.txt | head -12; echo ---; grep -n -A5 \"^HAMMER,\" SKT.txt | head -12; echo ---; grep -n -A5 \"^ACID,\" SKT.txt | head -10; echo ---; grep -n -A6 \"^VINEGAR,\" SKT.txt | head -12"
}
```


### [2026-09-04T19:14:58.012Z] TOOL RESULT

```
---
---
---
```


## [2026-09-04T19:15:00.831Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Edge, a border\\|EDGE, a\\|Hammer, an\\|HAMMER\\|Acid, sour\\|ACID\\|Vinegar\" SKT.txt | head -10"
}
```


### [2026-09-04T19:15:00.919Z] TOOL RESULT

```
20912:Vine.  Vinegar  ;  fee  Wine,
```


## [2026-09-04T19:15:04.686Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -m4 \"^edge\\b\\|^ EDGE\\|edge, \" SKT.txt | cut -c1-300; echo \"=== head\"; head -c 400 SKT.txt; echo; grep -n -i -m3 \"hammer\" SKT.txt | cut -c1-300"
}
```


### [2026-09-04T19:15:04.749Z] TOOL RESULT

```
1170:PHtom  of  gilding  apart- >td  standard  of  France. he,  the  sacrrd  standard L.  aMrifiamma,  lit bcoraw  the  banner  wu  cat rtrips  at  the  outer  edge,  nn-i
5637:Earnest  {%\  a  pledge,  (F. -L.)  Tht- /  is  added.  M.  E.  tmts\  also  spelt  «r/«, ar/£r.  Dlmin.  of  O.  !•".  f  rtj,  arrw^,  pL  — L.  drMa.^Gk.  ippa^wv.  a  pledge
7419:OarnlBh.  (F.-O.  Low  G.)  AWj nish.  —  Q.  f.gamit;  wamit ,  stem  of pi.  ofgamir^  loarmir,  lo  warn,  avert,  fol garnish  ;  all  from  the  notion  of  '  waiU or  protection  (hence  decoration).  J an  O.  Low  G.  source  ;  O.  Friea  werwi give  a  pledge,  A.  S.  wtanttam :  
8250:Hog.  (E.)  M.  E  heiggg\  with  same sense  as  .\.S.  hagi^stt,  a  witch,  a  hag.  ^ G.  ktxe,  M.  H.  G-  hackt,  a  witch,  O.  U.  G. ktiitjia  [prob.  short  for  hagasissa*]^  a witch.  Moit  likely  (rom  A.  S  ka^^  a hedge,  bu^h;  it  being  >uppo5ci1  thot  witches were  seen  
=== head
This  is  a  digital  copy  of  a  book  that  was  preserved  for  generations  on  library  shelves  before  it  was  carefully  scanned  by  Google  as  part  of  a  project to  make  the  world's  books  discoverable  online.
It  has  survived  long  enough  for  the  copyright  to  expire  and  the  book  to  enter  the  public  domain.  A  public  domain  book  is  one  that  was  never  sub
1375:Bang  (I),  to  beat  (Scand.)  Ii:  - banke,  to  beat ;  O.  Swetl.  bdn^^  I , a  hammering.     Cf.  Ski.  bhaui,  to  br bungle,   to    mend   clumsily.     (I Swed,  dial,  bangta,  to  work  iucflcctl from  Swed.  dial,  bunka,  bonka,  or to  strike:  see  Bang  (x).
1624:botch  (1),  to  patch.  (0,  LowG.)  M.E. bOichfH.  —  Du.  boisen,  to  strike ;  O.  Du. butitH,  to  Strike,  repair  From  the  notion of  repairing  roughly  by  hammering.  Du. bcf-sem   is   from  the   nme  root   as  A.  S.
8644:Hew.  (E.)   M.  E.  Ataten.   K.  S. to  cut.  +  D12.  k^ntutn,  loel ^^ggo,  Dan.  kmggt,  G.  hatum  -. to  hammer,  forge.     Allied  to  I* beat.    (VKU.)
```


## [2026-09-04T19:15:11.373Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in FSD_vol1.txt WEB_vol1.txt; do echo \"### $f\"; grep -n -i -m3 \"achar\\b\" $f | cut -c1-300; done"
}
```


### [2026-09-04T19:15:13.012Z] TOOL RESULT

```
### FSD_vol1.txt
6430:the  Actuemenians,  which  Is  one  of  cuneiform  Inscriptions,  France.  l<  Salnt-AcfceuZ,  near  Amiens,  France.) found  at  Behlstun  and  Persepolis,  and  held  to  represent  the  ach'l-ai»  ach'i-ar,  n.  Some  as  achar,  2. second  stage  In  the  growth  of  the  Persian  language
27853:at-char/,  n.  [Ango-Ind.]  Same  as  achar*.  at-chaar'f. Atch'l-ncse,  n.  Same  as  Achinese.
28576:republic.  At-tl-ke'i  [Gr.].  2.  A   city  in  Fountain  county,  att-jar',  1   at-ynri;  2   fit-yur7,  n.  Same  as  achar.
### WEB_vol1.txt
56264:bore. dis-pas’sion (-pash’un), 7. freedom from pas- sion, from emotion, or from bias. dis-pas’/sion-dte, a. free from passion, emo- tion, or bias; calm; composed; impartial; tem- perate; unmoved by feelings; as, dispassionate men or judges. dis:pas’sion-Ate-ly, adv. in a dispassionate
```


## [2026-09-04T19:15:16.392Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -i \".\\{0,300\\}ach'ar.\\{0,300\\}\" FSD_vol1.txt | head -5"
}
```


### [2026-09-04T19:15:23.731Z] TOOL RESULT

```
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,300}
                         \___exceeds complexity limits
```


## [2026-09-04T19:15:26.683Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('FSD_vol1.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r\"ach.?ar\", d[:2000000], re.I):\n    s=max(0,m.start()-250); print(repr(d[s:m.start()+350])); print('---')\nEOF"
}
```


### [2026-09-04T19:15:28.652Z] TOOL RESULT

```
'.  E.  Young  People’s  So- ciety of  Christian  Endeavor, yr.  [yrs.,  pi.]  Year,  younger,  your. Yt.  Yttrium.  [tlan  Association. Y.  XV.  C.  A.  Young  Women’s  Chrls- Y.  \\Y.  C.  T.  U.  Young  Women’s Christian  Temperance  Union.\nZach.  Zachary.\nZecb.  Zcchariah.\nZcph.  Zepbanlah.\nZ.  G.  Zoological  Gardens. Zn.  Zinc.\nzoogeog.  Zoogeography, zool.  Zoology,  zoological, zoopb.  Zoophytology.\nZr.  Zirconium.\nab-bre\'vI-a"tor,  1   a-bri\'vi-e\'ter;  2   S.-brS\'vi-a.\'tor,  n. 1.  One  who  shortens  or  abbreviates.  2.  R.  C.  Ch. An  officer  at  the  Vatican  who  prepares #   the'
---
'al  period  in  northern\nthe  Actuemenians,  which  Is  one  of  cuneiform  Inscriptions,  France.  l<  Salnt-AcfceuZ,  near  Amiens,  France.) found  at  Behlstun  and  Persepolis,  and  held  to  represent  the  ach\'l-ai»  ach\'i-ar,  n.  Some  as  achar,  2. second  stage  In  the  growth  of  the  Persian  language,  as  dls-  A-chl\'a1, 1   a-kal\'s;  2   n-cl\'a,  n.  Bib.  (Douai). tingulshed  from  the  earlier  Accadlan  and  the  later  Huz-  A"cbl-ach \'a-ms,  1   C\'kal-nk\'a-rus;  2   S’CI-iic\'a-ms,  n.  Bib. varesh  or  Pahlavl.  (Apocrypha).  Tob.  1,  21.\nAch"£C-men\'l-d2c,  1   ak\'ton'
---
```


## [2026-09-04T19:15:39.884Z] TOOL CALL #99: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/acid",
 "prompt": "Full etymology of acid verbatim: French acide, Latin acidus/acere, PIE *ak-, dates of English use; also mention of acetone if present."
}
```


### [2026-09-04T19:15:45.639Z] TOOL RESULT

```
# Etymology of Acid

**Language Lineage:**
The word traces back through French *acide* and Latin *acidus* (meaning "sour, sharp, tart"), which derives from the Latin verb *acere* ("to be sour, be sharp"). The ultimate root is the Proto-Indo-European *ak-, meaning "be sharp, rise to a point, pierce."

**English Timeline:**
- **1620s (adjective):** First appeared describing "the taste of vinegar"
- **1690s (noun):** Adopted from the adjective; originally applied loosely to any sour-tasting substance
- **Early 18c:** Gained more precise scientific definitions in chemistry
- **1775:** Figurative sense ("sour, sharp, biting") emerged
- **1966:** Slang term for LSD-25 documented

**Key Historical Notes:**
The page notes that "acid rain" was recorded by 1859, "acid test" entered American English in 1881 (originally referring to using nitric acid to distinguish gold), and "acid rock" appeared in 1966. However, acetone is not mentioned in this etymological entry.
```


## [2026-09-04T19:15:54.795Z] TOOL CALL #100: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82e%E1%B8%B1-\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%B3%DB%8C%D8%A7%D8%A8\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D9%85%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%86%DA%AF\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%86%D8%AC%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%DA%86%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%9A%E0%A4%BE%E0%A4%B0\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 42, root Ak/Aq/Aken: Wiktionary check of PIE *h2ek- and its Iranian/Persian reflexes (asman, sang, sanjidan, asyab, achar)\" 2>&1 | tail -2; done"
}
```


### [2026-09-04T19:15:58.362Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/73a1a1d4c4035b90.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/95a1188aaa2295d1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/375eeb1c945fffe7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8efe08951489c398.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e549722b00c37bc9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/136c44ff6cd41301.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7c8bf182b0bbcf69.txt
```


## [2026-09-04T19:16:04.421Z] TOOL CALL #101: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/vinegar\" \\\n \"https://www.etymonline.com/word/acrobat\" \\\n \"https://www.etymonline.com/word/oxygen\" \\\n \"https://www.etymonline.com/word/hammer\" \\\n \"https://www.etymonline.com/word/edge\" \\\n \"https://www.etymonline.com/word/acid\" \\\n \"https://www.vajehyab.com/moein/%D8%A7%D8%B3%DB%8C%D8%AF\" \\\n \"https://www.vajehyab.com/moein/%D8%A7%D8%B3%D8%AA%D9%86\" \\\n \"https://abadis.ir/fatofa/%D8%A7%D8%B3%D8%AA%D9%86/\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 42, root Ak/Aq/Aken: English/French/Persian reflexes (acrobat, oxygen, acid, vinegar, edge, hammer; Mo'in on asid/aseton)\" 2>&1 | tail -2; done"
}
```


### [2026-09-04T19:16:09.518Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/81bae94ad15b6157.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b469a7f4325ae3fc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1172cb9f2ab5808e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ed22d5a0f2145b9b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c11cb1f6782c8eb0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4ffd1ba9d7a0a8b0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f04161878da93e72.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/06002bb7b0850bbe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/71391c242f0b58e3.txt
```


## [2026-09-04T19:16:14.981Z] TOOL CALL #102: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15870,15885p' SNS_pages.txt"
}
```


### [2026-09-04T19:16:15.023Z] TOOL RESULT

```
                                                         srSyiin 183/2                     stOtgar 180/5
 sahfih 250/4             si 10/3-148/13-172/4
                                                         srlt 186/20                       st5r 180/17
 sahmgSn/sahmgOn 174/17   sidlgar 181/15
                                                         srOs 184/8                        stOr I gOsn 180/19
 sakatOm 182/6            sidOs 180/10
                                                         srOl ahrav 184/15                 star 180/20
 saraad 187/7             sidOs rOzaglha 18/12
                                                         srOscarnam 184/21                 sQd 190/16
 sang 193/15-313/14       si Gvak 10/8
                                                         srCsOcarnaio 185/4                sQdag 190/19
 sar 182/10-230/18        siganag 10/9-172/5
                                                         srubSn 183/7-184/6                sOdaglh 191/15
 sar 3 sar 231/3          siya(h)   172/6
                                                         srtld    134/17                   sfldan 191/7
 sar brldan 230/20         si yak-S 10/10
```


## [2026-09-04T19:16:26.917Z] TOOL CALL #103: WebFetch

```json
{
 "url": "https://www.vajehyab.com/moein/%D8%A2%DA%A9%D8%B1%D9%88%D8%A8%D8%A7%D8%AA",
 "prompt": "Does Mo'in's Farhang-e Farsi have an entry for آکروبات? Quote it with any origin tag such as [فر.] (French)."
}
```


## [2026-09-04T19:16:28.104Z] TOOL CALL #104: WebFetch

```json
{
 "url": "https://www.vajehyab.com/moein/%D8%A7%DA%A9%D8%B3%DB%8C%DA%98%D9%86",
 "prompt": "Does Mo'in's Farhang-e Farsi have an entry for اکسیژن? Quote it with any origin tag such as [فر.] (French)."
}
```


### [2026-09-04T19:16:30.329Z] TOOL RESULT

```
Yes, Mo'in's Farhang-e Farsi has an entry for آکروبات. Here is the quoted definition:

"(رُ) [ فر. ] ( اِ.) بندباز، ورزشکاری که کارهایی مانند بندبازی ، ژیمناستیک و ... را انجام می دهد."

The entry indicates a French origin [فر.] and defines the term as an acrobat or athlete who performs acrobatic activities.
```


### [2026-09-04T19:16:32.107Z] TOOL RESULT

```
Yes, Mo'in's Farhang-e Farsi does have an entry for اکسیژن (oxygen). Here is the quoted definition with its origin tag:

"(اُ ژِ) [فر.] (اِ.) گازی است بی رنگ ، بی بو، بی طعم ، کمی سنگین تر از هوا"

The [فر.] tag indicates the word derives from French. The entry describes oxygen as a colorless, odorless, tasteless gas slightly heavier than air.
```


## [2026-09-04T19:16:36.864Z] TOOL CALL #105: Bash

```json
{
 "command": "for u in \"https://www.vajehyab.com/moein/%D8%A2%DA%A9%D8%B1%D9%88%D8%A8%D8%A7%D8%AA\" \"https://www.vajehyab.com/moein/%D8%A7%DA%A9%D8%B3%DB%8C%DA%98%D9%86\" \"https://www.vajehyab.com/moein/%D8%A7%D8%B3%D8%AA%D9%88%D9%86\"; do python3 tools/fetch_source.py \"$u\" --note \"pdf page 42, root Ak/Aq/Aken: Mo'in entries for the French loans akrobat/oksizhen and for aston/aseton\" 2>&1 | tail -1; done"
}
```


### [2026-09-04T19:16:39.150Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6a3a1faf137366f4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e43f420b56e2bdb0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c5fc59923fc5178a.txt
```


## [2026-09-04T19:17:42.784Z] AGENT

Now I'll write the verification file.


## [2026-09-04T19:24:40.805Z] TOOL CALL #106: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build42.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\ndata = {\n \"pdf_page\": 42,\n \"book_page\": 12,\n \"verified_by\": \"claude-fable-5-1\",\n \"verified_on\": \"2026-09-04\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Ak, Aq, Aken\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₂eḱ- (trad. *ak-/*ok-) 'sharp, pointed, edged', with the derived n-stem *h₂éḱ-mon- 'stone, sky' and the n-formant stem *ak-en- 'stone'\",\n   \"note\": (\"Pokorny I 18-22 heads the entry '2. ak-, ok- ‚scharf, spitz, kantig‘ und ‚Stein‘', i.e. exactly Nourai's gloss \"\n            \"'sharp, also a sharp stone'; Walde-Pokorny I 28 has the same lemma 'ak- (z. T. auch āk-) ‚scharf, spitz, kantig; Stein‘'. \"\n            \"Nourai's three-part root name reproduces three sources: Klein s.v. 'acrid' writes the base '*ak-, *aq-' (whence 'Ak, Aq'), and \"\n            \"Pokorny p.19 has the sub-stem 'aken-' (Av. asǝnga-, OP aθanga-) (whence 'Aken'). Language label 'Indo-European' correct. \"\n            \"TWO CROSS-CUTTING PROBLEMS on this page. (1) The Persian 'weighing' words — sang/sax 'to weigh', Pahl. saxt, NP sanjīdan, sanješ, \"\n            \"saxtan (nodes #4, #5, #7) — do NOT belong to this root. They are the verb MP saxtan/sanj- 'to weigh', from Old Iranian *θanǵ- 'to pull, \"\n            \"draw' (Cheung, EDIV p.392; Abolghasemi FFD p.60; Hübschmann PSt §747 already called Horn's remark on sanjīdan 'unklar'). The \"\n            \"association with sang 'stone' is a Persian folk etymology helped by the variant sangīdan and by sanje 'balance-weight (a stone)'. \"\n            \"(2) Nourai analyses Av./OP asman- as 'as-man = like stone' with a cross-reference to root 'Men 1' — that is the Borhān-e Qāteʽ \"\n            \"explanation ('معنی ترکیبی آن آسیا مانند است', p.42), which Moʿin's own footnote on that very page flatly rejects: '۴ - این توجیه درست نیست' \"\n            \"('this explanation is not correct'). asman- is a plain n-stem *h₂éḱ-mon- 'stone > stone vault of heaven', not a compound with a \"\n            \"word for 'like'.\"),\n   \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%82e%E1%B8%B1-\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:18\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt ↵-leaf 25 (printed p.18): '2. ak-, ok- ‚scharf, spitz, kantig‘ und ‚Stein‘.' The very first item of the e/o-stems on that page is 'Npers. ās (dehnstufig) ‚Mühlstein‘' — Pokorny himself puts Persian ās under this root. Entry closes 'WP. I 28 ff., WH. I 6 ff.'\"},\n    {\"ref\": \"KNT:173\", \"status\": \"supports\",\n     \"note\": \"KNT.txt leaf 195 (running head '173'): 'asan- sb. ‚stone‘: pIE *aken- (§9.V, §87, §155.1), cf. asman-'; and 'asman- sb. ‚sky‘: Av. asman-, Skt. áśman-, Gk. ἄκμον ‚anvil‘, Lith. akmuõ ‚stone‘, pIE *akmen-/mon-'. Kent's '*aken-' is Nourai's third root name.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"as 1, asan : stone; as-man, as-mana : like stone, sky\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"Av. asan- (gen. asnō) 'stone' and asman- 'stone; heaven', OP asman- 'sky' (Bartholomae AiW col. 207; Kent p.173) continue \"\n                    \"PIE *h₂eḱ-/*h₂éḱ-mon- (Skt. áśman- 'stone, rock, sky', Gk. ἄκμων 'anvil', Lith. akmuõ 'stone', OCS kamy with metathesis). \"\n                    \"The semantic bridge 'stone' > 'sky' is the Indo-Iranian conception of the firmament as a stone vault (Reichelt IF 32, 23 ff., quoted \"\n                    \"verbatim by both Pokorny and Walde-Pokorny). Nourai's forms and glosses are right, but his morphological analysis is not: 'as-man, \"\n                    \"as-mana = like stone' treats -man as a separate morph 'like' (his cross-reference '☞ Men 1'), whereas asman- is an inherited \"\n                    \"n-stem *h₂éḱ-mon- with the ordinary Indo-Iranian -man- suffix; asmana- is simply the derived adjective 'of stone, stony' \"\n                    \"(Av. asmana-, OP aθan(g)aina-), not 'like stone'. Kent adds that OP is asman-, 'Not āsman-, despite NPers. āsmān, which has \"\n                    \"length of later origin'.\"),\n     \"sources\": [W + \"%D8%A2%D8%B3%D9%85%D8%A7%D9%86\", W + \"Reconstruction:Proto-Indo-European/h%E2%82%82e%E1%B8%B1-\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:19\", \"status\": \"supports\",\n       \"note\": \"POK_01.txt ↵-leaf 27 (printed p.19), section '4. Mit m-Formantien: ak-men-/-mer-': 'Ai. aśman- n. ‚Stein, Himmel‘ ... av. asman- ‚Stein, Himmel‘ ... gr. ἄκμων ‚Amboß‘ ... lit. akmuõ ‚Stein‘.' The following section '5. Mit n-Formantien: aken-' has 'av. asǝnga-, apers. aθanga- ‚Stein‘'.\"},\n      {\"ref\": \"KLN:18\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 21 = printed p.18, s.v. 'acrid': '... fr. I.-E. base *ak-, *aq-, ‚sharp, pointed‘, whence also ... Gk. ἄκρον ..., ἀκμών ‚an anvil‘, OI. aśriḥ ‚edge‘, aśman- ‚stone, rock, sky‘, Avestic asman- of s.m., Lith. akmuo ‚stone‘ ... OSlav. kamy (a metathesized form) ‚stone‘.' Exactly the arrow Nourai draws, and the source of his root-name variant 'Aq'.\"},\n      {\"ref\": \"KNT\", \"status\": \"supports\",\n       \"note\": \"KNT.txt leaf 195 (p.173): 'asan- sb. ‚stone‘: pIE *aken-'; 'asman- sb. ‚sky‘ ... pIE *akmen-/mon-'; also leaf 47 (p.32) 'asan- ‚stone‘ with Med. s ... cf. also acc. asmānam ‚sky‘, Av. asman- ‚sky, stone‘'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. 207 (BRT.txt leaf 147; column number '207' printed on the preceding leaf, and confirmed by Kent's citation 'Bthl. AiW 207' s.v. Asagarta- and by Jeffery FVQ 164 n.5 'Bartholomew, AIW, 207')\", \"stance\": \"supports\", \"note\": \"'j., g. (, p.) asan-, [asan-tar-], j., p. asman- m. 1) ‚Stein‘ ... a) als Amulet ... b) als Waffe, ‚Schleuderstein, Steingeschoss‘'; asman- is cross-referred 's. unter asan-'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.28 ff. (WLD_Bd1_pages.txt, section 'Mit m(e)n-Formantien')\", \"stance\": \"supports\", \"note\": \"'ai. áçman- m. ‚Stein, Fels; Himmel‘ (zur Vorstellung des Himmels als eines Steingewölbes s. Reichelt IF. 32, 23 ff.) ... av. asman- ‚Stein, Himmel‘, asmana- ‚steinern‘, ap. asman- ‚Himmel‘ ... ap. aθan(g)aina- ‚steinern‘.' Note WLD glosses asmana- 'steinern' (of stone), not 'like stone'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 1.44 STONE; ROCK, p.52 (SYN.txt leaf 78)\", \"stance\": \"supports\", \"note\": \"'Skt. açman-, açan-, Av. asan- (asman- ‚sky‘) ‚stone‘, adj. Av. asmana-, OPers. aθa(n)gaina- ‚of stone‘, NPers. sang ‚stone‘ ... Grk. ἄκμων ‚anvil‘ ... Walde-P. 1.28 ff.'\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. akmó(n), akmen-\", \"stance\": \"supports\", \"note\": \"'akmó(n), akmen- ‚stone, boulder, crag‘. WP I, 29, 33' with OCS kamy, Lith. akmuo, Latv. akmens.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ak-, §3\", \"stance\": \"supports\", \"note\": \"'Suffixed form *ak-men, stone, sharp stone used as a tool, with metathetic variant *ka-men-'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\",\n     \"words\": \"âs : mill, mill stone; âs-âp : water mill; vât-âs : wind mill; âs-mân : sky\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"Old Iranian *āsa- (lengthened grade *āḱ- of the 'stone' root; Pokorny p.18 lists 'Npers. ās (dehnstufig) ‚Mühlstein‘' under ak-) \"\n                    \"gives Middle Persian āsyāg [ʾisʾk'] 'mill(-stone)' and the compound āsyāb [ʾisʾp] '(water-)mill' = āsyā + āb 'water' \"\n                    \"(MacKenzie CPD p.13); āsmān [ʾismʾān'] 'sky, heavens' (CPD p.12) continues OP asman- with secondary lengthening of the initial \"\n                    \"vowel already in Middle Persian. Two of Nourai's four forms are only approximately Pahlavi: the simplex 'ās' and the compound \"\n                    \"'vāt-ās' (wād 'wind' + ās) are not in MacKenzie or Nyberg; MP has āsyāg/āsyāb, and the wind-mill compound is attested as New \"\n                    \"Persian bādās (BQT p.39 footnote lists آسیا، آسیاب، بادآس، خرآس، دستآس، پادآس). Also, āsmān does not descend from ās 'mill' \"\n                    \"but in parallel with it from Av./OP asman-.\"),\n     \"sources\": [W + \"%D8%A2%D8%B3%DB%8C%D8%A7%D8%A8\", W + \"%D8%A2%D8%B3%D9%85%D8%A7%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:39,42,43\", \"status\": \"supports\",\n       \"note\": (\"BQT_v1_pages.txt leaves 249/252/253 = printed pp.39/42/43. p.39-40 s.v. آس: 'آسیابان باشد چه آسیا را آس میگویند' ('... because āsyā is \"\n                \"called ās'), with Moʿin's footnote 1: 'سانسکرت aśman ... اوستا asanga و asan بمعنی سنگ «بارتولمه ۲۰۷»، آس در لغات آسیا و آسیاب و بادآس و خرآس \"\n                \"و دستآس و پادآس ...'. p.42 s.v. آسمان: 'معروفست و بعربی سما و فلک خوانند، و معنی ترکیبی آن آسیا مانند است ... چه آسیا را آس نیز گویند', \"\n                \"with Moʿin's footnote 'اوستا asan بمعنی سنگ «بارتولمه ۲۰۷ و ۲۲۰» ... چون آسمان را سنگی پنداشته‌اند ... پهلوی āsmān' and the \"\n                \"correction '۴ - این توجیه درست نیست'. p.43 s.v. آسیا. So the three cited pages carry exactly the four words of this node.\")}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD pp.12-13\", \"stance\": \"partial\", \"note\": \"'āsmān [ʾismʾān' | = M, N āsmān] sky, heavens; cal. 27th day'; 'āsyāb [ʾisyʾp] (water-)mill. āsyāg [ʾisyʾk' | N āsyā] mill(-stone)'. Supports ās-āb and ās-mān but has no bare 'ās' and no 'wād-ās'.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (Glossary)\", \"stance\": \"silent\", \"note\": \"The Kārnāmag glossary attests asmān only inside phrases (e.g. 'xʻatāi i miyān i asmān' s.v. miyān, 'asmān čigōn?' s.v. čigōn); no headword entry and no mill word.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss no. 27, p.8\", \"stance\": \"supports\", \"note\": \"'27. āsmān ‚Himmel‘ ... ap. asman- ‚Himmel‘; aw. asman-; phlv. āsmān; ai. çáman-', with Kurdish/Baluchi/Pamir loans.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\",\n     \"words\": \"âs «آس» : mill; âsiyâb «آسیاب ، آسیا۱» : water mill; bâdâs «بادآس» : wind mill; âsmân «آسمان» : sky\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"NP ās 'millstone, mill' < MP *ās / āsyāg < Old Iranian *āča- (lengthened-grade *āḱ-o- of *h₂eḱ-), cf. Av. asan- 'stone'; Pokorny \"\n                    \"prints 'Npers. ās (dehnstufig) ‚Mühlstein‘' as the first Iranian witness of the root (IEW p.18). āsiyāb < MP āsyāb = ās(yā) \"\n                    \"'millstone' + linking -y- + āb 'water' (Wiktionary s.v. آسیاب, 'From Middle Persian ʾisyʾp̄ /āsyāb/. By surface analysis, آس \"\n                    \"(ās, ‚millstone‘) + ـیـ + آب (āb, ‚water‘)'); the mirror-image compound آسباد āsbād / بادآس bādās 'windmill' uses bād 'wind' \"\n                    \"and is listed by Moʿin among the ās-compounds at BQT p.39. āsmān < MP āsmān < OP asman- 'sky', the initial ā- being a \"\n                    \"secondary Middle Persian lengthening (Kent p.173, after Debrunner IF 52.153). The 'Onsōrī' verse quoted in the chart \"\n                    \"('آسمان آسیای گردانست ...') is a poetic pun on sky/mill, not evidence of derivation.\"),\n     \"sources\": [W + \"%D8%A2%D8%B3%DB%8C%D8%A7%D8%A8\", W + \"%D8%A2%D8%B3%D9%85%D8%A7%D9%86\", W + \"%D8%A2%D8%B3%DB%8C%D8%A7\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT\", \"status\": \"supports\",\n       \"note\": \"Borhān-e Qāteʽ (ed. Moʿin) vol. 1 pp.39-43 carries all four headwords آس، آسیا، آسیاب، آسمان with Moʿin's etymological footnotes (see node #2). BQT p.39 fn.1 explicitly lists بادآس among the ās-compounds.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"vol. 1 pp.39, 42, 43 with Moʿin's footnotes\", \"stance\": \"partial\", \"note\": \"Confirms all four words and their Avestan background, but Moʿin's note '۴ - این توجیه درست نیست' rejects Borhān's derivation of آسمان from آس 'mill' + مان 'like'.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 27 (āsmān)\", \"stance\": \"supports\", \"note\": \"'āsmān ‚Himmel‘ ... ap. asman-; aw. asman-; phlv. āsmān'.\"},\n      {\"src\": \"PHD\", \"where\": \"CPD pp.12-13\", \"stance\": \"supports\", \"note\": \"MP āsyāg > 'N āsyā', āsyāb '(water-)mill', āsmān '= N āsmān'.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien\", \"stance\": \"silent\", \"note\": \"No note on ās/āsyāb/āsmān (Hübschmann's corrections to Horn skip no. 27).\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"athagaina, athangaina : stone; âthanga, asenga, asan : stone; sang, sax : to weigh\",\n     \"verdict\": \"disputed\",\n     \"derivation\": (\"The 'stone' half is right: OP aθanga- m. 'stone' and the adjective aθaṅgaina-/aθagaina- 'of stone' (Dāriyāvaš Susa foundation \"\n                    \"charter DSf 24, 48), Av. asǝnga- 'stone', Av./OP asan- 'stone'. Kent p.166: 'aθanga- (i.e. aθanᵒga-) sb. ‚stone‘: Av. asanga-, \"\n                    \"NPers. sāng, cf. OP asan-, asman-'. The forms go back to *ak-en-g- (Benveniste, Origines 28; Bartholomae IF 2.268), i.e. the \"\n                    \"n-formant stem 'aken-' of Pokorny p.19. — The third item, 'sang, sax : to weigh', is NOT Avestan/Old Persian and does not belong \"\n                    \"to this root at all. NP sanǵīdan/saxtan 'to weigh' (pres. stem sanj-, past stem saxt) continues Old Iranian *θanǵ- 'to pull, \"\n                    \"draw' (Y.Av. θanjaiieiti, Parth. pad-hinj- 'to weigh', MP āhixtan/āhanj-), PIE *tengʰ- 'to draw, pull back' — Cheung, EDIV \"\n                    \"p.392; Abolghasemi FFD p.60. Nourai has merged two homonymous families because NP sang also acquired the sense 'weight'.\"),\n     \"sources\": [W + \"%D8%B3%D9%86%DA%AF\", W + \"%D8%B3%D9%86%D8%AC%DB%8C%D8%AF%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"SYN:52\", \"status\": \"supports\",\n       \"note\": \"SYN.txt leaf 78, printed p.52 (Buck 1.44 STONE; ROCK), §5: 'Skt. açman-, açan-, Av. asan- (asman- ‚sky‘) ‚stone‘, adj. Av. asmana-, OPers. aθa(n)gaina- ‚of stone‘, NPers. sang ‚stone‘, the general Balto-Slavic and Indo-Iranian word for ‚stone‘ ... Walde-P. 1.28 ff.'\"},\n      {\"ref\": \"BRT:208\", \"status\": \"supports\",\n       \"note\": \"BRT.txt leaf 148 (col. ~208, immediately after the column numbered 207 that carries asan-): 'j. asǝnga-, p. aθaⁿga- m. ‚Stein‘. ... Vgl. np. must-āsang, mp., np. sang. — Vgl. auch asman-. ... Bthl. IF. 2.268; Hbm. PSt. 76.'\"},\n      {\"ref\": \"KNT:166\", \"status\": \"supports\",\n       \"note\": \"KNT.txt leaf 187 (running head '166'): 'aθanga- (i.e. aθanᵒga-) sb. ‚stone‘: Av. asanga-, NPers. sāng, cf. OP asan-, asman- (§87, §151, §155.1); see also aθagaina-. aθangam asm. DSf 24, 48.' — both of Nourai's adjective forms and the noun.\"},\n      {\"ref\": \"FFD:60\", \"status\": \"contradicts\",\n       \"note\": \"FFD_pages.txt pdf p.65 = printed p.60 (Abolghasemi, فعل‌های فارسی دری), s.v. سختن: 'سخت < فارسی میانه saxt < ایرانی باستان *θaxta- ... θax صورت اصلی است و آن صورت ضعیف ریشهٔ θanj به معنی «کشیدن» است'; 'سنج < فارسی میانه sanj < پهلوی اشکانی hanj < ایرانی باستان *θanja-'. The page Nourai cites derives sanj/saxt from *θanj- 'to pull', not from the stone word.\"},\n      {\"ref\": \"SPG:202\", \"status\": \"not_found\",\n       \"note\": \"In Spiegel, Die altpersischen Keilinschriften (1881) — the tentative identification of 'SPG' — āθangaina is discussed on p.116 ('Āthangaina hat Oppert gewiss richtig an neup. سنگ, Stein, [angeknüpft]') and in the Glossar on p.303 ('Āthangaina ... steinern ... in thang aber dasselbe Wort sehe wie in Neup. سنگ Stein'). p.202 of that book is unrelated, so either the identification of SPG or the page number is wrong; the substance of the claim is nevertheless in Spiegel.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV p.392 s.v. *θanǵ 'to pull, draw'\", \"stance\": \"contradicts\", \"note\": \"'*NWIR: NP sanjidan ‚to measure; reflect; compare, put in balance‘ ... (+ *pati-) Parth. pdhynj- ‚to weigh‘ ... «PIE *tengʷ- ‚to draw, pull back‘.' No connection with asan-/aθanga-.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien §747, pp.76-77\", \"stance\": \"partial\", \"note\": \"'Die Erklärung von sang ‚Stein, Gewicht‘ stimmt, wenn man für das Altpersische die Formen *aθanga- (= np. -āsang) ‚Stein‘ und *θanga- (= np. sang) ‚Stein‘ ansetzt ... Die Bemerkung über sanjīdan ‚wägen‘ ist unklar. Als alte Formen sind offenbar anzusetzen: inf. saxtan (ptc. saxta ‚gewogen‘), praes. sanjam' — i.e. sang 'stone' yes, but the weighing verb is kept apart.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.29\", \"stance\": \"supports\", \"note\": \"'av. asǝngo-gav- ‚mit Händen aus Stein‘. ap. aθanᵍgaina- ‚steinern‘ (mit -g- aus dem n. sg. des r/n-St., s. Bartholomae IF. 2, 269 ... ursprüngliches *ak-en-g- weit wahrscheinlicher).'\"},\n      {\"src\": \"POK\", \"where\": \"IEW p.19 s.v. aken-\", \"stance\": \"supports\", \"note\": \"'Ai. aśániḥ ‚Pfeilspitze, Geschoß‘; av. asǝnga-, apers. aθ-anga- ‚Stein‘ (*ak-en-go, Benveniste Orig. 28).'\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Pahlavi\",\n     \"words\": \"sang : stone; sang-gil : hard clay; saxt : weigh\",\n     \"verdict\": \"disputed\",\n     \"derivation\": (\"MP sang [KYPA / sng] 'stone, rock' (MacKenzie CPD p.74) continues OP aθanga- / Av. asǝnga- with the regular Middle Persian loss \"\n                    \"of the unstressed initial syllable (*aθanga- > *θang > sang; OP θ in initial position corresponds to NP s, Hübschmann PSt §747 n.2), \"\n                    \"so Nourai's arrow #4 > #5 is correct for this word. sang-gil 'stone-clay' is the transparent compound sang + gil 'clay' that Arabic \"\n                    \"borrowed as siǵǵīl (Asbaghi PLA p.155). But 'saxt : weigh' is a different word: MP saxtan, sanj- 'weigh' (CPD p.74) belongs to \"\n                    \"*θanǵ- 'to pull, draw', while MP saxt 'strong, hard, severe' (CPD p.74) is yet a third item; neither derives from sang/aθanga-.\"),\n     \"sources\": [W + \"%D8%B3%D9%86%DA%AF\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1175\", \"status\": \"supports\",\n       \"note\": (\"BQT_v2_pages.txt leaves 638-639 (running head 1139 at leaf 602 ⇒ printed pp.1175-1176) s.v. سنگ: 'سنگ = بفتح اول بر وزن رنگ، معروف است \"\n                \"و بعربی حجر خوانند - و بمعنی تمکین و وقار و اعتبار هم گفته‌اند - و کرانی چیزها را گویند'; Moʿin's footnote gives 'پارسی باستان aθanga (حجر) ... \"\n                \"asanga (حجر)، پهلوی sa(n)g و sang' plus dialect forms and 'سنگ در پهلوی بمعنی ارزش و قیمت آمده «نیبرگ»'.\")},\n      {\"ref\": \"SNS:193\", \"status\": \"partial\",\n       \"note\": \"SNS_pages.txt word-index: 'sang 193/15-313/14' — Tavoosi's glossary of Šāyast nē Šāyast attests Pahlavi sang at text p.193 line 15 (and 313/14). It is an attestation, not an etymology, and there is no sang-gil or saxt entry.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.74\", \"stance\": \"partial\", \"note\": \"'sang [KYPA < A kypʾ; sng | N ~] stone, rock. ~sar stony place. sanj-, v. saxtan.' and separately 'saxt [s(ḥ)tʾ | N ~] strong, hard, severe(ly)'; 'saxtan, sanj- [sʾḥtnʾ, snc- | N ~] weigh.' MacKenzie files the weighing verb under saxtan, not under sang.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II\", \"stance\": \"silent\", \"note\": \"No headword sang / saxtan in the Kārnāmag glossary (only frasang 'parasang').\"},\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV p.392\", \"stance\": \"contradicts\", \"note\": \"MP/Parthian pad-hinj- 'to weigh', NP sanjidan, all under *θanǵ 'to pull, draw'.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi p.155\", \"stance\": \"supports\", \"note\": \"For sang-gil: 'siǵǵīl: ‚harte Backsteine‘ aus pers. سنگ گل sang-gil, mp. sang < aw. asanga, asan, ap. asan, mp. gil.'\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Arabic\",\n     \"words\": \"sijjîl : baked clay\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Arabic سِجِّيل siǵǵīl 'lumps of baked clay' (Qurʾān 11:82, 15:74, 105:4, of the stones rained on Sodom and on the Army of the \"\n                    \"Elephant) is a Middle Persian loan, from sang 'stone' + gil 'clay'. The identification is already in the Arab lexicographers: Ibn \"\n                    \"Qutayba, quoted by al-Jawālīqī (al-Muʿarrab, ed. Shākir p.82), 'قال ابن قتیبة: السجيل بالفارسية سنگ و گل ... حجارة وطين', and Ṭabarī \"\n                    \"glosses it سنگ وگل. Phonetically Iranian *sang-gil was reshaped to the Arabic quadriliteral pattern fiʿʿīl (with -n- assimilated), \"\n                    \"which is why the borrowing looks like a native Arabic form to the grammarians. A minority view (adopted by the modern editor of \"\n                    \"al-Muʿarrab, and by those who confuse it with siǵill) makes it Greek/Latin sigillum 'seal'; Jeffery keeps the two words apart, \"\n                    \"deriving siǵill from sigillum but siǵǵīl from Persian.\"),\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"PLA:155\", \"status\": \"supports\",\n       \"note\": \"PLA_pages.txt 1-based leaf 170 = printed p.155 (Asbaghi, Persische Lehnwörter im Arabischen): 'سجيل - siǵǵīl: ‚harte Backsteine‘ aus pers. سنگ گل sang-gil, mp. sang < aw. asanga, asan, ap. asan, mp. gil, griech. sigillum.' Same page also has 'سجل siǵill: ‚öffentliches Aktenstück, Edikt, Diplom‘' and 'سجين siǵǵīn ... mp. sagēn ‚steinig‘'.\"},\n      {\"ref\": \"FVQ:164\", \"status\": \"supports\",\n       \"note\": \"FVQ_pages.txt leaf 181 (printed p.164, running head '164 FOREIGN VOCABULARY OF THE QURʾAN'), s.v. سجيل 'Lumps of baked clay': 'It was early recognized as a foreign word, and generally taken as of Persian origin, Tab. going so far as to tell us ... which is a very fair representation of سنگ and گل (Fraenkel, Vocab, 25; Siddiqi, Studien, 73). سنگ meaning stone is the Phlv. sang from Av. asan [n.5: Bartholomae, AiW, 207], and گل meaning clay the Phlv. gil ... From Middle Persian it passed directly into Arabic.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"ARB\", \"where\": \"al-Jawālīqī, al-Muʿarrab (ed. Shākir) p.82 with editor's note\", \"stance\": \"partial\", \"note\": \"Text: 'قال ابن قتيبة: السجيل بالفارسية سنگ و گل ... حجارة وطين'; the editor objects 'والذي أراه أرجح وأصح، أنها عربية' and quotes al-Azharī/Lisān 'قال أهل اللغة: هذا فارسي، والعرب لا تعرف هذا'.\"},\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, Aramäische Fremdwörter\", \"stance\": \"silent\", \"note\": \"Fraenkel treats only سجلاطي ('= sigillatus; Muʿarrab 82'), a textile word; no entry for siǵǵīl.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-Fārisiyya al-Muʿarraba\", \"stance\": \"silent\", \"note\": \"grep of AFM.txt / AFM_pages.txt for سجيل returns nothing.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein, CEDEL\", \"stance\": \"silent\", \"note\": \"No entry (the word has no English reflex).\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Persian\",\n     \"words\": \"sang «سنگ» : stone; sanjîdan «سنجیدن ( سنجه )» : to weigh; sanješ «سنجش» : weighing; saxtan «سختن ( سختیدن )» : to weigh\",\n     \"verdict\": \"disputed\",\n     \"derivation\": (\"NP sang 'stone' < MP sang < OP aθanga- / Av. asǝnga- is correct and uncontroversial (Wiktionary s.v. سنگ: 'inherited from Middle \"\n                    \"Persian sng (sang), ... Old Persian aθaⁿga-, Avestan asenga-'). The three verbal items are not. NP sanǵīdan (older saxtan, past \"\n                    \"stem saxt, present stem sanj-) 'to weigh, measure, weigh up' and its verbal noun sanješ belong to Proto-Iranian *θanǵ- 'to weigh \"\n                    \"< to pull, draw' < PIE *t(ʰ)engʰ- 'to draw, pull back' (Cheung EDIV 392; Wiktionary s.v. سنجیدن; Abolghasemi FFD 60), cognate \"\n                    \"with NP āhanjīdan/āhixtan 'to draw', farhang < *fra-θanga- 'education' and nihang. The by-form سنگیدن sangīdan recorded by \"\n                    \"Noushin, and the noun sanje 'balance weight' (a stone), invited the association with sang, but the -j-/-xt- alternation is that of \"\n                    \"the *θanǵ- verb, not a denominative of sang. The extra infinitive 'سختیدن' in the chart is a late analogical formation.\"),\n     \"sources\": [W + \"%D8%B3%D9%86%DA%AF\", W + \"%D8%B3%D9%86%D8%AC%DB%8C%D8%AF%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1175\", \"status\": \"supports\",\n       \"note\": \"See node #5: BQT vol.2 pp.1175-1176 s.v. سنگ with Moʿin's footnote 'پارسی باستان aθanga ... پهلوی sang'. Supports the noun only; the page has no derivation of سنجیدن from سنگ.\"},\n      {\"ref\": \"FFD:60\", \"status\": \"contradicts\",\n       \"note\": \"Abolghasemi, FFD p.60 (pdf 65): 'سخت < فارسی میانه saxt < ایرانی باستان *θaxta- ... صورت ضعیف ریشهٔ θanj به معنی «کشیدن»'; 'سنج ... < ایرانی باستان *θanja-'.\"},\n      {\"ref\": \"FSF:224\", \"status\": \"partial\",\n       \"note\": \"The entry exists but on p.305 of the scanned printing (FSF_pages.txt leaf 308; leaf-3 = printed page, checked against leaf 81 = p.78 and leaf 86 = p.83): 'سنجیدن (سنگیدن) ۱- سختن، اندازه گرفتن، کشیدن، وزن کردن (از این ریشه سنجه = سنگ ترازو)', with the شاهنامه line 'سخن را بسنج و به‌اندازه گوی'. Noushin glosses, and notes the variant سنگیدن and سنجه 'balance stone', but gives no derivation from سنگ. p.224 of this printing is in the داستان entries, so Nourai's page belongs to a different printing.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"CPD p.74\", \"stance\": \"partial\", \"note\": \"'sang ... stone, rock'; 'saxtan, sanj- ... weigh' — listed as two separate lemmas.\"},\n      {\"src\": \"HUB\", \"where\": \"PSt §747\", \"stance\": \"contradicts\", \"note\": \"'Die Bemerkung über sanjīdan ‚wägen‘ ist unklar. Als alte Formen sind offenbar anzusetzen: inf. saxtan (ptc. saxta ‚gewogen‘), praes. sanjam (-sanj ‚wägend‘, sanja ‚Gewicht‘), von letzterem aus ist der Infinitiv sanjīdan neu gebildet worden.'\"},\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV p.392 *θanǵ\", \"stance\": \"contradicts\", \"note\": \"'NP sanjidan ‚to measure; reflect; compare, put in balance‘ ... «PIE *tengʷ- ‚to draw, pull back‘.'\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi p.155\", \"stance\": \"partial\", \"note\": \"Asbaghi likewise keeps them apart, deriving an Arabic weight-term 'wahrscheinlich aus pers. سختن sāḫtan u. sangīdan ‚wiegen‘ mp. sāḫtan' — the verb, not the stone.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Greek\",\n     \"words\": \"akros : top most; akrobates : one who walks on tiptoe; oxus : sharp, sour\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Gk. ἄκρος 'topmost, at the point' < *h₂eḱ-ro- (Pokorny p.21 'akri-, akro-': 'gr. ἄκρος ‚spitz‘, ἄκρον, ἄκρα, ἄκρις ‚Spitze, \"\n                    \"Berggipfel‘'), beside Skt. áśri- 'edge' and Lat. ācer. ἀκροβάτης is a compound ἄκρο- + -βάτης 'goer' (from βαίνω < PIE \"\n                    \"*gʷeh₂- 'to go' — Nourai's '☞ Gwa' is correct), lit. 'one who walks on tiptoe'; Pokorny even cites the Homeric-lexicon form \"\n                    \"ἀκροβατοῦσα 'walking on the toes' under this root. ὀξύς 'sharp, keen; sour' goes back to the o-grade s-extension *h₂oḱ-su- \"\n                    \"(Pokorny p.22 'Weitergebildet in gr. ὀξύς ‚scharf‘ ... ὄξος ‚Weinessig‘'), the vinegar noun ὄξος showing the same \"\n                    \"sharp > sour shift as Latin acer/acetum.\"),\n     \"sources\": [\"https://www.etymonline.com/word/acrobat\", \"https://www.etymonline.com/word/oxygen\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt s.v. ak-: '10. Suffixed form *ak-mā- in Greek akmē, point ... 11. Suffixed form *ak-ro- in Greek akros, topmost: ACRO-; (ACROBAT), ACROMION. 12. Variant suffixed form *ok-su- in Greek oxus, sharp, sour: AMPHIOXUS, OXALIS, OXYGEN, OXYURIASIS, PAROXYSM. [Pok. 2. ak- 18 ...]'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW pp.21-22 (akri-, akro-; akes-/aks-)\", \"stance\": \"supports\", \"note\": \"'gr. ἄκρος ‚spitz‘, ἄκρον, ἄκρα, ἄκρις ‚Spitze, Berggipfel‘ ... Kurzform für ἀκροβατοῦσα ‚auf den Fußspitzen gehend‘' and 'Weitergebildet in gr. ὀξύς ‚scharf‘ ... ὄξος ‚Weinessig‘'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.28 (Mit r-Formantien)\", \"stance\": \"supports\", \"note\": \"'gr. ἄκρος ‚spitz‘, ἄκρον, ἄκρα, ἄκρις ‚Spitze, Berggipfel‘ (auch in ἀκρ-οαομαι ...), ἀκρις, -ιδος ‚Heuschrecke‘, nach Prellwitz Kurzform für ἀκροβατοῦσα ‚auf den Fußspitzen gehend‘.'\"},\n      {\"src\": \"KLN\", \"where\": \"CEDEL s.v. acrobat, oxygen\", \"stance\": \"supports\", \"note\": \"'acrobat, n. — F. acrobate, fr. Gk. ἀκροβάτος, ‚walking on tiptoe‘, fr. ἄκρον ... and βατ-, ‚going‘'; 'oxygen ... fr. Gk. ὀξύς, ‚sharp, acid‘'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. akris, os\", \"stance\": \"supports\", \"note\": \"'akris, os ‚point, tip, edge‘; ‚pointed, sharp‘. WP I, 28 ... Gk. ákris; ákros; Lat. cf. acer.'\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"French\",\n     \"words\": \"acrobate; oxygene : acid former\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Fr. acrobate is a learned 16th-18th c. borrowing of Gk. ἀκροβάτης through a Latinised acrobates. Fr. oxygène was coined by \"\n                    \"Antoine-Laurent Lavoisier in 1777 (published 1786/1787 in the Méthode de nomenclature chimique), short for principe oxygène \"\n                    \"'acidifying principle', from Gk. ὀξύς 'sharp, acid' + -γενής 'producing' — exactly Nourai's gloss 'acid former'; the name \"\n                    \"embodies Lavoisier's (mistaken) belief that oxygen was a constituent of every acid.\"),\n     \"sources\": [\"https://www.etymonline.com/word/acrobat\", \"https://www.etymonline.com/word/oxygen\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:12\", \"status\": \"partial\",\n       \"note\": \"The root entry that carries ACROBAT and OXYGEN is AHD's Indo-European appendix s.v. ak- (1985 Watkins ed. p.1; 1976 appendix pp.1505 ff.), not p.12; p.12 of the AHD New College Edition is the alphabetical page on which the English headword 'acrobat' falls, which is presumably what Nourai means. The content of the claim is supported (see node #8).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"CEDEL s.v. acrobat, oxygen\", \"stance\": \"supports\", \"note\": \"'oxygen, n. ... — F. oxygène, short for principe oxygène (earlier principe oxygine), lit. ‚the acidifying principle‘; coined by the French chemist Antoine-Laurent Lavoisier (1743-94) in 1777 fr. Gk. ὀξύς ... Hence oxygen lit. means ‚producing acids‘.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ak- §11-12\", \"stance\": \"supports\", \"note\": \"Greek akros → (ACROBAT); Greek oxus → OXYGEN.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. acrobat, oxygen\", \"stance\": \"supports\", \"note\": \"Standard F. acrobate < Gk. akrobates; oxygen < F. oxygène.\"}\n     ]\n    },\n    {\n     \"id\": 10, \"lang\": \"Persian\",\n     \"words\": \"âkrobât «آکروبات»; oksîžen «اکسیژن»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Both are 20th-century Persian borrowings from French, taken over with French phonetics: Fr. acrobate [akʁɔbat] > آکروبات \"\n                    \"ākrobāt, Fr. oxygène [ɔksiʒɛn] > اکسیژن oksīžen, the ژ /ʒ/ being the letter Persian reserves for French j/g. Moʿin tags both \"\n                    \"[فر.] = French. French was the language of Iranian scientific borrowing from the Dār al-Fonūn (1851) onwards, which is why \"\n                    \"these chemistry and circus words entered through French rather than English.\"),\n     \"sources\": [\"https://www.vajehyab.com/moein/%D8%A2%DA%A9%D8%B1%D9%88%D8%A8%D8%A7%D8%AA\", \"https://www.vajehyab.com/moein/%D8%A7%DA%A9%D8%B3%DB%8C%DA%98%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:75,331\", \"status\": \"partial\",\n       \"note\": \"Moʿin's Farhang-e Fārsi has both entries with the French tag — آکروبات: '(رُ) [ فر. ] (ا\\u650.) بندباز، ورزشکاری که کارهایی مانند بندبازی، ژیمناستیک ... را انجام می دهد'; اکسیژن: '(ُ ژ\\u650) [فر.] (ا\\u650.) گازی است بی رنگ، بی بو، بی طعم، کمی سنگین تر از هوا' (vajehyab, Moʿin). The volume/page numbers 75 and 331 cannot be checked because no paginated copy of the 6-volume Amir Kabir edition is online and the local OCR (MON_part1/2.txt) has no page structure; the alphabetical positions (آ-section, then اک-) are consistent with them.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"vajehyab, Moʿin s.vv. آکروبات, اکسیژن\", \"stance\": \"supports\", \"note\": \"Both carry the origin tag [فر.] 'French'.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhān-e Qāteʽ (17th c.)\", \"stance\": \"silent\", \"note\": \"A pre-modern dictionary; naturally has no European chemistry or circus loans.\"}\n     ]\n    },\n    {\n     \"id\": 11, \"lang\": \"English\",\n     \"words\": \"acrobat, oxygen\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"English acrobat (1825/1845) is taken from French acrobate; oxygen (1790) from French oxygène, both listed by Watkins under \"\n                    \"PIE *ak-. Etymonline: acrobat 'from French acrobate (14c.), from a Latinized form of Greek akrobates ‚rope dancer, gymnastic \"\n                    \"performer‘ ... akros ‚topmost‘ ... from PIE root *ak- ‚be sharp, rise to a point, pierce‘'; oxygen 'coined 1777 by Lavoisier ... \"\n                    \"oxys ‚sharp, acid‘ ... a Greek rendering of French principe acidifiant'.\"),\n     \"sources\": [\"https://www.etymonline.com/word/acrobat\", \"https://www.etymonline.com/word/oxygen\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt s.v. ak-: '§11 ... Greek akros, topmost: ACRO-; (ACROBAT), ACROMION. §12 ... Greek oxus, sharp, sour: ... OXYGEN ...'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"CEDEL s.v. acrobat, oxygen\", \"stance\": \"supports\", \"note\": \"See node #9; Klein derives both from the French forms.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary\", \"stance\": \"supports\", \"note\": \"Both English headwords are present with the same French > Greek route.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\", \"note\": \"The local SKT.txt is a badly garbled two-column Google scan; the headwords could not be located reliably.\"}\n     ]\n    },\n    {\n     \"id\": 12, \"lang\": \"Latin\",\n     \"words\": \"acere : to be sharp; vinum-acer : sharp (soar) wine, vinegar; acus, acetum\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Latin acēre 'to be sharp/sour' is the stative *h₂eḱ-eh₁- (Pokorny p.18: 'lat. acere ‚sauer sein‘, acidus ‚sauer‘, acetum \"\n                    \"‚Essig‘'); acētum 'vinegar' is properly the neuter participle of acescere, short for vīnum acētum 'wine turned sour' — exactly \"\n                    \"Nourai's 'vinum-acer' (his cross-reference '☞ Woin' to the wine root is right); ācer, ācris 'sharp' is the lengthened r-stem \"\n                    \"*āk-ri- (Pokorny p.21) and gives Vulgar Latin *acrus > OFr. aigre; acus, -ūs 'needle' is the u-stem *h₂eḱ-u- (Pokorny p.19).\"),\n     \"sources\": [\"https://www.etymonline.com/word/vinegar\", \"https://www.etymonline.com/word/acid\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt s.v. ak-: '2.b. Latin acus, needle: ACICULA, (ACUITY), ACUMEN, ACUTE ... 5. Suffixed lengthened form *āk-ri- in Latin ācer, sharp, bitter: ... VINEGAR. 7. Suffixed (stative) form *ak-ē- in Latin acēre, to be sharp: ACID. 8. Suffixed form *ak-ēto- in Latin acētum, vinegar: ACETABULUM, (ACETIC), ACETUM; ESTER.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW pp.18-21\", \"stance\": \"supports\", \"note\": \"'lat. acere ‚sauer sein‘, acidus ‚sauer‘, acetum ‚Essig‘' (p.18); 'lat. acus, -ūs f. ‚Nadel‘ ... acuere ‚schärfen‘, acumen ‚Spitze‘' (p.19); 'lat. ācer, ācris, -e ‚scharf‘' (p.21).\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.28\", \"stance\": \"supports\", \"note\": \"'lat. (mit Dehnstufe) ācer, ācris, -e (altlat. ācra, -um) ‚scharf‘ ... lat. acerbus ‚herb, sauer, traurig‘.'\"},\n      {\"src\": \"KLN\", \"where\": \"CEDEL s.v. acetum, acid, acrid\", \"stance\": \"supports\", \"note\": \"'acetum, n., vinegar. — L. acetum, ‚vinegar‘, prop. vīnum (acetum), ‚wine turned sour‘, neut. pp. of acescere, ‚to turn sour‘, fr. acere, ‚to be sour‘, which is rel. to acer, ‚sharp‘.'\"}\n     ]\n    },\n    {\n     \"id\": 13, \"lang\": \"French\",\n     \"words\": \"acide : sour (sharp) substance, acid; vinaigre : vinegar\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Fr. acide is a 16th-century learned borrowing of Lat. acidus 'sour' (from acēre). Fr. vinaigre (Old French vin aigre, 12th c.) \"\n                    \"is the transparent compound vin 'wine' (Lat. vīnum) + aigre 'sour' (Vulgar Latin *acrus for Lat. ācer), a calque of the Latin \"\n                    \"phrase vīnum acētum; the two words were later univerbated and the French form was carried into English.\"),\n     \"sources\": [\"https://www.etymonline.com/word/vinegar\", \"https://www.etymonline.com/word/acid\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"CEDEL s.v. acid\", \"stance\": \"supports\", \"note\": \"'acid, adj., sour, sharp to the taste. — Either fr. F. acide or directly fr. L. acidus, ‚sour‘, fr. acere, ‚to be sour‘, whence also acetum, ‚vinegar‘.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ak- §5, §7\", \"stance\": \"supports\", \"note\": \"Latin ācer → VINEGAR; Latin acēre → ACID.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary\", \"stance\": \"silent\", \"note\": \"Consulted for vinaigre/acide; the local WEB_vol1.txt OCR did not yield the entries.\"}\n     ]\n    },\n    {\n     \"id\": 14, \"lang\": \"Persian\",\n     \"words\": \"asîd «اسید»; aseton «استن»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"NP اسید asīd is a direct 19th-20th c. borrowing of French acide; Moʿin: '(َ) [ فر. ] (ا\\u650.) هر جسم هیدروژن داری که به حالت محلول، \"\n                    \"یون هیدروژن (پروتون) آزاد کند' — the [فر.] tag confirming the French source. استن aseton is likewise from French acétone \"\n                    \"(Moʿin has a separate chemical entry 'اَس\\u650تُن: مایعی است بی‌رنگ، فرار، سریع‌التبخیر و قابل اشتعال ... از تقطیر یکی از استات‌ها', distinct from the \"\n                    \"homograph استن = ستون 'pillar'), so the spelling in the chart is not a scan error. The one inaccuracy is the placement: \"\n                    \"acétone was coined (Bussy 1833, German Aceton) on Latin acētum 'vinegar' + -one, i.e. it hangs from the Latin node #12, not \"\n                    \"from Fr. acide/vinaigre; and Persian asīd is a chemistry loan, not a descendant of French vinaigre.\"),\n     \"sources\": [\"https://www.vajehyab.com/moein/%D8%A7%D8%B3%DB%8C%D8%AF\", \"https://abadis.ir/fatofa/%D8%A7%D8%B3%D8%AA%D9%86/\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:260,276\", \"status\": \"partial\",\n       \"note\": \"Moʿin does have both words in the alphabetical order the two page numbers imply (استن before اسید), and اسید carries the tag [فر.]; the printed pages cannot be verified because no paginated copy of Moʿin is online (see node #10).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"vajehyab / abadis, Moʿin s.vv. اسید, استن\", \"stance\": \"supports\", \"note\": \"اسید '[فر.]'; استن (chemical sense) 'a colourless, volatile, quickly evaporating and flammable liquid ... from the distillation of one of the acetates'.\"},\n      {\"src\": \"KLN\", \"where\": \"CEDEL s.v. acetone\", \"stance\": \"partial\", \"note\": \"'acetone, n. ... — A hybrid coined fr. L. acetum, ‚vinegar‘, and the Greek suff. -ώνη' — i.e. built on Latin acetum, not on French acide.\"}\n     ]\n    },\n    {\n     \"id\": 15, \"lang\": \"English\",\n     \"words\": \"acid, acute, vinegar\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"vinegar is a genuine French borrowing: ME vinegre < Anglo-French/Old French vinaigre 'vin ‚wine‘ + aigre ‚sour‘', first \"\n                    \"attested early 14c. acid entered in 1620s (adj., 'of the taste of vinegar'), 1690s as a noun — Klein: 'Either fr. F. acide or \"\n                    \"directly fr. L. acidus ... introduced into English by Francis Bacon (1561-1626) in 1626', so the French mediation is optional. \"\n                    \"acute, however, does not come through French at all: it is a direct Latin borrowing, ME acut < L. acūtus, pp. of acuere 'to \"\n                    \"sharpen' (Klein s.v. acute: 'L. acutus, ‚sharp‘, lit. ‚sharpened‘, pp. of acuere ... which is rel. to acus, ‚needle‘'), so it \"\n                    \"belongs under the Latin node #12, not under the French node #13.\"),\n     \"sources\": [\"https://www.etymonline.com/word/vinegar\", \"https://www.etymonline.com/word/acid\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"CEDEL s.vv. acid, acute\", \"stance\": \"partial\", \"note\": \"acid 'Either fr. F. acide or directly fr. L. acidus'; acute 'L. acutus ... pp. of acuere' — no French stage.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ak- §2.b, §5, §7\", \"stance\": \"supports\", \"note\": \"ACUTE under Latin acus; VINEGAR under Latin ācer; ACID under Latin acēre — all three under *ak-.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls\", \"stance\": \"supports\", \"note\": \"Standard routes: vinegar < OF vinaigre; acute < L. acutus.\"}\n     ]\n    },\n    {\n     \"id\": 16, \"lang\": \"Persian\",\n     \"words\": \"âčâr «آچار» : pickles\",\n     \"verdict\": \"disputed\",\n     \"derivation\": (\"The word is real: NP آچار āčār 'pickle, fruit or vegetables preserved in vinegar/brine'. Its origin, however, is not Latin. \"\n                    \"Nourai himself flags the arrow with a question mark, and his source only speculates: Hobson-Jobson p.3 says 'it is not impossible \"\n                    \"that Western Asiatics got it originally from the Latin acetāria' — a guess, not a derivation, and phonetically hard \"\n                    \"(acetāria would not give āčār). Modern lexicography derives āčār from an Iranian source, Proto-Iranian *Habi-čārna- \"\n                    \"(originally 'spice, garnish'), shared with a Middle Iranian form; Lokotsch no.15 simply files it as 'Pers. ačār ‚sauer‘' with \"\n                    \"no European ancestor, and Devic pp.3-4 says outright 'Je ne saurais dire quel est le sens primitif de ce mot, qui nous est venu, \"\n                    \"non de la Perse, mais des Indes'. (The homograph آچار 'spanner, wrench' is a separate, modern loan from Azerbaijani açar 'key'.)\"),\n     \"sources\": [W + \"%D8%A2%DA%86%D8%A7%D8%B1\"],\n     \"ref_check\": [\n      {\"ref\": \"HJB:3\", \"status\": \"partial\",\n       \"note\": \"HJB.txt s.v. 'ACHAR, s.' on p.3: 'P. āchār, Malay āchār, adopted in nearly all the vernaculars of India for acid and salt relishes. By Europeans it is used as the equivalent of ‚pickles‘ ... We have adopted the word through the Portuguese; but it is not impossible that Western Asiatics got it originally from the Latin acetaria — (See Plin. Hist. Nat. xix. 19).' Yule offers the Latin link only as a possibility, which is why Nourai's own citation carries a '?'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no.15, p.2\", \"stance\": \"contradicts\", \"note\": \"'15. Pers. ačār: ‚Sauer‘, hieraus malay. ačar ... in der Bedeutung ‚Eingemachtes, pickles‘ und ebenso in allen Eingeborenensprachen Indiens; daher angloind. achar ‚dass.‘; frz. achars ...' — Persian is the ultimate source for Lokotsch; no Latin.\"},\n      {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d'origine orientale, pp.3-4 s.v. ACHARS\", \"stance\": \"contradicts\", \"note\": \"'C'est le persan آچار āchār, en malais atchar. Je ne saurais dire quel est le sens primitif de ce mot, qui nous est venu, non de la Perse, mais des Indes.'\"},\n      {\"src\": \"RCH\", \"where\": \"Richardson, Persian-Arabic-English Dictionary\", \"stance\": \"silent\", \"note\": \"grep of RCH.txt for achar/āchār found only unrelated strings (OCR of the Persian-script columns is poor).\"}\n     ]\n    },\n    {\n     \"id\": 17, \"lang\": \"Hindustani\",\n     \"words\": \"achar : pickles\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Hindi/Urdu अचार / اچار acār 'a spicy and salty pickle' is a straightforward borrowing of Classical Persian آچار āčār during the \"\n                    \"Persian-language administration of northern India (Delhi Sultanate/Mughal period); Wiktionary: 'Borrowed from Classical Persian \"\n                    \"آچَار (āčār)', with the same borrowing in Bhojpuri and Magahi and via Hindi into Nepali. Yule confirms the spread: 'adopted \"\n                    \"in nearly all the vernaculars of India for acid and salt relishes'. So the arrow Persian > Hindustani is correct, even though the \"\n                    \"arrow above it (Latin > Persian) is not.\"),\n     \"sources\": [W + \"%E0%A4%85%E0%A4%9A%E0%A4%BE%E0%A4%B0\"],\n     \"ref_check\": [\n      {\"ref\": \"OXF:3\", \"status\": \"not_checked\",\n       \"note\": \"J. Speake, Oxford Dictionary of Foreign Words and Phrases (1997) is on archive.org only as a lending copy; no readable text was obtainable.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.3 s.v. ACHAR\", \"stance\": \"supports\", \"note\": \"'P. āchār, Malay āchār, adopted in nearly all the vernaculars of India for acid and salt relishes.'\"},\n      {\"src\": \"AID\", \"where\": \"Whitworth, An Anglo-Indian Dictionary\", \"stance\": \"silent\", \"note\": \"No headword achar/achār (only unrelated āchārya, Korachar).\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no.15\", \"stance\": \"supports\", \"note\": \"Persian ačār > Malay ačar 'and likewise in all the native languages of India'.\"}\n     ]\n    },\n    {\n     \"id\": 18, \"lang\": \"English\",\n     \"words\": \"achar\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"English achar (also atchar, achiar, attjar) is an Anglo-Indian word of the 16th c. onwards, taken from Hindustani/Persian \"\n                    \"āčār — according to Yule via Portuguese achar, since the Portuguese met the word in Goa and Malacca before the English did \"\n                    \"(Hobson-Jobson quotes Garcia de Orta, 1568: 'and this they call Achar'). Funk & Wagnalls lists achar with the variants ach'i-ar, \"\n                    \"at-char' and att-jar', marked '[Anglo-Ind.]'. Nourai's route Persian > Hindustani > English is right in substance; the Portuguese \"\n                    \"intermediary is missing.\"),\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"OXF:3\", \"status\": \"not_checked\",\n       \"note\": \"Same as node #17: no accessible copy of Speake's Oxford Dictionary of Foreign Words and Phrases.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.3 s.v. ACHAR\", \"stance\": \"partial\", \"note\": \"'We have adopted the word through the Portuguese', with the 1568 quotation from Garcia de Orta — supports the English word but adds a Portuguese stage Nourai omits.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary, vol. 1\", \"stance\": \"supports\", \"note\": \"'ach'i-ar, n. Same as achar, 2'; 'at-char', n. [Anglo-Ind.] Same as achar'; 'att-jar', n. Same as achar.'\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no.15\", \"stance\": \"supports\", \"note\": \"'daher angloind. achar ‚dass.‘; frz. achars ‚Obst od. Gemüse, das in Essig eingemacht ist‘.'\"}\n     ]\n    },\n    {\n     \"id\": 19, \"lang\": \"Germanic\",\n     \"words\": \"ak-jô : sharp side; ha-maraz : sharp tool\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Proto-Germanic *agjō 'edge, sharp side' (OE ecg, OS eggia, OHG ekka, ON egg) is the yā-stem *h₂eḱ-yéh₂ of the root — Pokorny \"\n                    \"p.19 lists it under the i-/y-stems ('as. eggja f., ahd. usw. ekka ‚Spitze, Schwertschneide‘ ... anord. egg ‚Schneide‘'), and \"\n                    \"Nourai's spelling 'ak-jô' reproduces Watkins's *ak-yā-. Proto-Germanic *hamaraz 'hammer' (OE hamor, ON hamarr, which still \"\n                    \"means 'stone, crag') is the same *ak-men- 'stone, sharp stone used as a tool' with the metathesis *ak-men- > *kə-mer-, i.e. the \"\n                    \"zero-grade k- stems Pokorny lists at the end of the entry (p.22: 'Schwundstufiges k- steckt wahrscheinlich in den Stämmen kemen-, \"\n                    \"kemel-, komen- ‚Stein, Himmel‘, komor- ‚Steinhammer‘'), the same stem as OCS kamy 'stone'. Nourai's gloss 'sharp tool' is a \"\n                    \"little off — the tool was named from the stone it was made of, not from sharpness.\"),\n     \"sources\": [\"https://www.etymonline.com/word/edge\", \"https://www.etymonline.com/word/hammer\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt s.v. ak-: '1. Suffixed form *ak-yā- in: a. Germanic *akjō in Old English ecg, sharp side: EDGE ... 3. Suffixed form *ak-men, stone, sharp stone used as a tool, with metathetic variant *kə-men, with variants: a. *kə-mer- in Germanic *hamaraz in Old English hamor, hammer: HAMMER; b. *ke-men- ... ‚the stony vault of heaven‘ ... HEAVEN.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW pp.19, 22\", \"stance\": \"supports\", \"note\": \"p.19 'as. eggja f., ahd. usw. ekka ‚Spitze, Schwertschneide‘; nhd. Ecke (urgerm. *agjiō), anord. egg ‚Schneide‘ ... ags. ecg ‚Kante, Schneide, Schwert‘'; p.22 'Schwundstufiges k- steckt wahrscheinlich in den Stämmen kemen-, kemel-, komen- ‚Stein, Himmel‘, komor- ‚Steinhammer‘' — so Pokorny files hammer under the metathesised variant, as Watkins does.\"},\n      {\"src\": \"KLN\", \"where\": \"CEDEL s.v. hammer\", \"stance\": \"supports\", \"note\": \"'hammer, n. — ME. hamur, hamer, fr. OE. hamor ... orig. ‚stone hammer‘; cogn. with OI. aśman-, ‚stone; rock; sky‘, Avestic asman-, of s.m., Gk. ἄκμων, ‚(stone) anvil‘, Lith. akmuo, OSlav. kamy, ‚stone‘. All these words are traceable to I.-E. base *ak-, ‚sharp, pointed‘.'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I pp.28-29\", \"stance\": \"supports\", \"note\": \"'as. eggja, ahd. ekka ‚Spitze, Schwertschneide‘' among the i-/j-stems; the *akmen- section includes Gk. ἄκμων and OCS kamy.\"}\n     ]\n    },\n    {\n     \"id\": 20, \"lang\": \"English\",\n     \"words\": \"edge; hammer\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"OE ecg 'corner, edge, point; (poet.) sword' > ME egge > NE edge, the OE -cg /dʒ/ being spelled -dge from Middle English on; \"\n                    \"from Proto-Germanic *agjō, PIE *h₂eḱ-. OE hamor/hamer > ME hamur > NE hammer, from Proto-Germanic *hamaraz; the original \"\n                    \"sense 'tool with a stone head' is still visible in the ON cognate hamarr 'stone, crag' (Etymonline: 'the Germanic words are from \"\n                    \"a PIE *ka-mer-, with reversal of the initial sounds, from *akmen ‚stone, sharp stone used as a tool‘').\"),\n     \"sources\": [\"https://www.etymonline.com/word/edge\", \"https://www.etymonline.com/word/hammer\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ak- §1.a, §3.a\", \"stance\": \"supports\", \"note\": \"'Old English ecg, sharp side: EDGE'; 'Old English hamor, hammer: HAMMER'.\"},\n      {\"src\": \"KLN\", \"where\": \"CEDEL s.v. hammer\", \"stance\": \"supports\", \"note\": \"See node #19 — Klein traces OE hamor to I.-E. *ak- through the 'stone' words.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\", \"note\": \"The local scan (SKT.txt) is too corrupt to locate the headwords Edge and Hammer.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-42.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build42.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-42.json > /dev/null && echo \"VALID JSON\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 42"
}
```


### [2026-09-04T19:24:43.680Z] TOOL RESULT

```
Exit code 1
  File "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build42.py", line 274
    "note": "Moʿin's Farhang-e Fārsi has both entries with the French tag — آکروبات: '(رُ) [ فر. ] (ا\u650.) بندباز، ورزشکاری که کارهایی مانند بندبازی، ژیمناستیک ... را انجام می دهد'; اکسیژن: '(ُ ژ\u650) [فر.] (ا\u650.) گازی است بی رنگ، بی بو، بی طعم، کمی سنگین تر از هوا' (vajehyab, Moʿin). The volume/page numbers 75 and 331 cannot be checked because no paginated copy of the 6-volume Amir Kabir edition is online and the local OCR (MON_part1/2.txt) has no page structure; the alphabetical positions (آ-section, then اک-) are consistent with them."}
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 223-227: truncated \uXXXX escape
```


## [2026-09-04T19:24:51.085Z] TOOL CALL #107: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 - <<'EOF'\np='build42.py'\ns=open(p,encoding='utf-8').read()\ns=s.replace('\\\\u650','')\nopen(p,'w',encoding='utf-8').write(s)\nprint(s.count('\\\\u650'))\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build42.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-42.json > /dev/null && echo \"VALID JSON\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 42"
}
```


### [2026-09-04T19:24:53.031Z] TOOL RESULT

```
0
ok
VALID JSON
nodes verified: 20/20
node verdicts: {'plausible': 4, 'confirmed': 12, 'disputed': 4}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 16, 'contradicts': 2, 'not_found': 1, 'partial': 6, 'not_checked': 5}
books consulted: {'supports': 38, 'partial': 10, 'silent': 12, 'contradicts': 6} | by book: {'KLN': 10, 'WLD': 5, 'AHD': 5, 'PHD': 4, 'POK': 4, 'FSD': 4, 'HUB': 3, 'CHEUNG': 3, 'LKT': 3, 'IEC': 2, 'NYB': 2, 'HRN': 2, 'BQT': 2, 'PLA': 2, 'MON': 2, 'SKT': 2, 'HJB': 2, 'BRT': 1, 'SYN': 1, 'ARB': 1, 'AFA': 1, 'AFM': 1, 'WEB': 1, 'DEV': 1, 'RCH': 1, 'AID': 1}
```


## [2026-09-04T19:25:13.470Z] AGENT

Done. `data/verification/page-42.json` written; `verify_check.py 42` reports 20/20 nodes, no PROBLEM lines.

**Page 42 (book p.12) — one entry, root "Ak, Aq, Aken" [IE] "sharp, also a sharp stone" → confirmed**
- Root verdicts: confirmed 1. Node verdicts: confirmed 12, plausible 4, disputed 4.
- Ref checks: supports 16, partial 6, contradicts 2, not_found 1, not_checked 5. Books consulted: 26 distinct (POK, WLD, AHD, KLN, BRT, KNT, SYN, IEC, PHD, NYB, HRN, HUB, CHEUNG, BQT+Moʿin, FSF, FFD, PLA, FVQ, ARB, SNS, HJB, LKT, DEV, FSD, MON, RCH).

**disputed**
- #4 Av./OP node — "sang, sax : to weigh" is neither Avestan/OP nor from this root; FFD:60 (the page Nourai cites) derives سنج/سخت from Old Iranian *θanǰ- "to pull".
- #5 Pahlavi "saxt : weigh" — MacKenzie files *saxtan, sanj-* "weigh" separately from *sang* "stone"; Cheung EDIV 392 puts it under *θanǰ-.
- #7 Persian sanjīdan / sanješ / saxtan — same; Hübschmann §747 already called Horn's remark on sanjīdan "unklar". (sang itself is fine.)
- #16 Persian āčār "pickles" ← Latin — Hobson-Jobson p.3 only says "not impossible… from the Latin acetaria"; Lokotsch no.15 and Devic pp.3-4 keep it Persian/Indian, and modern lexicography derives it from Proto-Iranian *Habi-čārna-.

**plausible** (not flagged as errors): #1 (asman- is an n-stem *h₂éḱ-mon-, not "as-man = like stone"; Moʿin's own BQT p.42 footnote says "این توجیه درست نیست"); #2 (Pahlavi has āsyāg/āsyāb, not bare *ās* / *vāt-ās*); #14 (aseton is built on Latin acētum, not on Fr. acide); #15 (English *acute* is straight from Latin acūtus, not via French).

**transcription_suspect**: none. «استن» *aseton* checked and correct — Moʿin has a separate chemical entry اَسِتُن alongside the homograph "pillar".

Notable positive finds: Pokorny p.18 himself prints "Npers. ās (dehnstufig) ‚Mühlstein'"; BQT pp.39/42/43 and 1175-76 match Nourai's citations exactly; FVQ:164 and PLA:155 both state sijjīl < Persian sang-gil verbatim. SPG:202 not found (āθangaina is on pp.116/303 of Spiegel 1881; the SPG identification itself is flagged uncertain in refs_online.json). FSF:224 is p.305 in the scanned printing. 19 web pages archived via `tools/fetch_source.py`.
