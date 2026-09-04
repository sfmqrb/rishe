# Verification process log — verify-page-59


## [2026-09-04T22:40:42.448Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 59 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-59.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-59.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-59.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 59` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T22:40:44.340Z] AGENT

I'll start by reading the instructions and the relevant files.


## [2026-09-04T22:40:46.412Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T22:40:46.424Z] TOOL RESULT

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


## [2026-09-04T22:40:46.866Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-59.txt"
}
```


### [2026-09-04T22:40:46.879Z] TOOL RESULT

```
1	=== PDF page 59 (book page 29) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Apo, Apâ, Apu, Pu 3, Pô 1 : off  (refs POK:53)  PART 1
4	#1 (parent #0) [Avestan] refs=POK:54; BQT:1086 | ap 2, apa : off, away, to ; apama, apatama : last
5	  #2 (parent #1) [Pahlavi] refs=AEF:309 | apě, ape : apart, without
6	    #3 (parent #2) [Persian] refs=AEF:309; MON:131 | bî «بی-» : without ; bî-dastar «بیدستر» : beaver that is able to cut trees "without sickles". ☞Dâ 1 | extra: ابی- ، بی نیاز ، بی بهره ، بی شمار
7	  #4 (parent #1) [Pahlavi] refs=SNS:26 | afdom, awdum : last
8	    #5 (parent #4) [Persian] refs=MON:72,462; FRS:184 | âfdom «آفدُم» : last, at last | extra: افدُم، بافدُم
9	#6 (parent #0) [Avestan] refs=KNT:168; BQT:1086; FFD:24 | â 1 : a prefix for making verbs ; â-vare : to bring ☞Bher 1 ; â-gam : to come ☞Gwa ; â-râd, â-râiti 1 : to set up ☞Ar ; apa-spar : walk away from, trust ☞Spher ; â-kand : to fill ☞Gwhen 1
10	  #7 (parent #6) [Persian] refs=BQT:1086; HRN:1; FFD:24 | â-, a- «آ- ، ا-» : a verbal prefix ; -â- «-ا-» : used to repeat a word | extra: آوردن، آمدن، آراستن، اسپاردن، آکندن، برابر، دمادم، سراسر، گرداگرد
11	#8 (parent #0) [Avestan] refs=KLN:168; POK:844 | apa-dâna : off place, secret room of a palace ☞Dhě 2 ; â-frî-nami : I praise ☞Prî ; â-fritan : to create ☞Prî ; â-part : battle ☞Per 3
12	  #9 (parent #8) [Persian] refs=KNT:168 | âpâdânâ «آپادانا» : throne room ; âfarîn «آفرین» : praise ; âvard «آورد» : battle | extra: آفریدن ، آفریدگار ، نفرین ، آوردگاه
13	    #10 (parent #9) [Arabic] refs=AHD:23; PLA:203 | ifrît : demon creature
14	      #11 (parent #10) [Persian] refs=MON | efrît «عفریت» : demon | extra: عفریته
15	#12 (parent #0) [Old Persian] refs=POK:53-55; KNT:168 | ap 2, apa : from, away ; apa-dâna : off (secret) place ☞Dhě 2 ; pa 2, pô : under
16	  #13 (parent #12) [Old Persian] refs=POK:53,55; KNT:168 | apa-had : put away ☞Sed ; apa-ra : back, later ; apa-taram : elsewhere ; pan-s-dau : after that ; apa-nyâka : ancestors ☞Nyâka
17	  #14 (parent #12) [Old Persian] refs=POK:53-55 | apa-ardha : pushed off, reverse ☞Ardha
18	    #15 (parent #14) [Pahlavi] refs=NYB:23 | apârôn : wrong, upside down
19	      #16 (parent #15) [Persian] refs=MON:4941 | vârŭn «وارون» : upside down | extra: وارونه
20	#17 (parent #0) [Latin] refs=AHD | ab : away
21	  #18 (parent #17) [English] refs=None | abnormal
22	
```


## [2026-09-04T22:40:49.696Z] AGENT

I'll read the supporting files and source JSON.


## [2026-09-04T22:40:52.531Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T22:40:52.570Z] TOOL RESULT

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


## [2026-09-04T22:40:52.790Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/extracted/batch/page-59.json | head -200",
 "description": "Read page 59 JSON"
}
```


### [2026-09-04T22:40:52.828Z] TOOL RESULT

```
{
  "pdf_page": 59,
  "book_page": 29,
  "entries": [
    {
      "root": {
        "name": "Apo, Apâ, Apu, Pu 3, Pô 1",
        "lang": "Indo-European",
        "refs": "POK:53",
        "gloss": "off"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:54; BQT:1086",
          "words": [
            {"translit": "ap 2, apa", "gloss": "off, away, to", "script": null},
            {"translit": "apama, apatama", "gloss": "last", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "AEF:309",
          "words": [
            {"translit": "apě, ape", "gloss": "apart, without", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "AEF:309; MON:131",
          "words": [
            {"translit": "bî", "gloss": "without", "script": "بی-"},
            {"translit": "bî-dastar", "gloss": "beaver that is able to cut trees \"without sickles\".", "script": "بیدستر", "see": ["Dâ 1"]}
          ],
          "script_extra": "ابی- ، بی نیاز ، بی بهره ، بی شمار",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:26",
          "words": [
            {"translit": "afdom, awdum", "gloss": "last", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:72,462; FRS:184",
          "words": [
            {"translit": "âfdom", "gloss": "last, at last", "script": "آفدُم"}
          ],
          "script_extra": "افدُم، بافدُم",
          "note": null,
          "quote": {
            "text": "گرچه هرروز اندکی برداردش - بافدُم روزی به پایان آردش",
            "poet": "Rūdakî"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KNT:168; BQT:1086; FFD:24",
          "words": [
            {"translit": "â 1", "gloss": "a prefix for making verbs", "script": null},
            {"translit": "â-vare", "gloss": "to bring", "script": null, "see": ["Bher 1"]},
            {"translit": "â-gam", "gloss": "to come", "script": null, "see": ["Gwa"]},
            {"translit": "â-râd, â-râiti 1", "gloss": "to set up", "script": null, "see": ["Ar"]},
            {"translit": "apa-spar", "gloss": "walk away from, trust", "script": null, "see": ["Spher"]},
            {"translit": "â-kand", "gloss": "to fill", "script": null, "see": ["Gwhen 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT:1086; HRN:1; FFD:24",
          "words": [
            {"translit": "â-, a-", "gloss": "a verbal prefix", "script": "آ- ، ا-"},
            {"translit": "-â-", "gloss": "used to repeat a word", "script": "-ا-"}
          ],
          "script_extra": "آوردن، آمدن، آراستن، اسپاردن، آکندن، برابر، دمادم، سراسر، گرداگرد",
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KLN:168; POK:844",
          "words": [
            {"translit": "apa-dâna", "gloss": "off place, secret room of a palace", "script": null, "see": ["Dhě 2"]},
            {"translit": "â-frî-nami", "gloss": "I praise", "script": null, "see": ["Prî"]},
            {"translit": "â-fritan", "gloss": "to create", "script": null, "see": ["Prî"]},
            {"translit": "â-part", "gloss": "battle", "script": null, "see": ["Per 3"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "KNT:168",
          "words": [
            {"translit": "âpâdânâ", "gloss": "throne room", "script": "آپادانا"},
            {"translit": "âfarîn", "gloss": "praise", "script": "آفرین"},
            {"translit": "âvard", "gloss": "battle", "script": "آورد"}
          ],
          "script_extra": "آفریدن ، آفریدگار ، نفرین ، آوردگاه",
          "note": null,
          "quote": {
            "text": "من آورد رستم بسی دیده ام - زجنگاوران نیز بشنیده ام",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Arabic",
          "refs": "AHD:23; PLA:203",
          "words": [
            {"translit": "ifrît", "gloss": "demon creature", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "efrît", "gloss": "demon", "script": "عفریت"}
          ],
          "script_extra": "عفریته",
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:53-55; KNT:168",
          "words": [
            {"translit": "ap 2, apa", "gloss": "from, away", "script": null},
            {"translit": "apa-dâna", "gloss": "off (secret) place", "script": null, "see": ["Dhě 2"]},
            {"translit": "pa 2, pô", "gloss": "under", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Old Persian",
          "refs": "POK:53,55; KNT:168",
          "words": [
            {"translit": "apa-had", "gloss": "put away", "script": null, "see": ["Sed"]},
            {"translit": "apa-ra", "gloss": "back, later", "script": null},
            {"translit": "apa-taram", "gloss": "elsewhere", "script": null},
            {"translit": "pan-s-dau", "gloss": "after that", "script": null},
            {"translit": "apa-nyâka", "gloss": "ancestors", "script": null, "see": ["Nyâka"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 12,
          "lang": "Old Persian",
          "refs": "POK:53-55",
          "words": [
            {"translit": "apa-ardha", "gloss": "pushed off, reverse", "script": null, "see": ["Ardha"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
```


## [2026-09-04T22:40:59.032Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '200,300p' data/extracted/batch/page-59.json; echo \"=== refs_online ===\"; python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','BQT','AEF','MON','SNS','FRS','KNT','FFD','HRN','KLN','AHD','PLA','NYB','PHD','BRT','HUB','WLD','SKT','IEC','SYN']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"",
 "description": "Rest of JSON and refs_online"
}
```


### [2026-09-04T22:41:00.934Z] TOOL RESULT

```
          "parent": 14,
          "lang": "Pahlavi",
          "refs": "NYB:23",
          "words": [
            {"translit": "apârôn", "gloss": "wrong, upside down", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": "MON:4941",
          "words": [
            {"translit": "vârŭn", "gloss": "upside down", "script": "وارون"}
          ],
          "script_extra": "وارونه",
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "ab", "gloss": "away", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "abnormal", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== refs_online ===
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_p
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
```


## [2026-09-04T22:41:08.867Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','KNT','NYB','HRN','BRT','PHD','KLN','AHD','MON','FRS','SNS','FFD','BQT','PLA','HUB','IEC','SYN','WLD','SKT','CHEUNG','AEF','FVQ','AFM','LKT','WEB','FSD','LEW','LAT']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print(k,'|local:',v.get('local_file'),'|offset:',v.get('page_offset'),'|hint:',str(v.get('lookup_hint'))[:200])\n    print()\n\"",
 "description": "Get page offsets"
}
```


### [2026-09-04T22:41:11.107Z] TOOL RESULT

```
POK |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt |offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.i

KNT |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt |offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall i

NYB |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt |offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.

HRN |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt |offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered ent

BRT |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt |offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin glos

PHD |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt |offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A

KLN |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt |offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume p

AHD |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt |offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. |hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the 

MON |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] |offset: None |hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Aves

FRS |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt'] |offset: different edition — no mapping |hint: Look up the headword (entries grouped by final letter); FRS_pages.txt has \f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.

SNS |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt'] |offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image |hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) fo

FFD |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt'] |offset: 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). |hint: Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a d

BQT |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] |offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). |hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'http

PLA |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] |offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). |hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --

HUB |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt |offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.

IEC |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt |offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.

SYN |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt |offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed p

WLD |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] |offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). |hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, u

SKT |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt |offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.

CHEUNG MISSING
AEF |local: None |offset: None |hint: Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's re

FVQ |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] |offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) |hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).

AFM |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] |offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image |hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أ

LKT |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt |offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.

WEB |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt |offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabe

FSD |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt |offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.

LEW |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt |offset: 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.

LAT |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt |offset: leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
```


## [2026-09-04T22:41:16.247Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 61 62 63; do echo \"=== leaf $n (p.$((n-8))) ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((n+1)) POK_01.txt | head -70; done",
 "description": "Pokorny p.53-55"
}
```


### [2026-09-04T22:41:18.309Z] TOOL RESULT

```
=== leaf 61 (p.53) ===
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
=== leaf 62 (p.54) ===
dd.  ebbe,  woher  nhd.  Ebbe  entlehnt,  als  , Abfluten'^).
Ai.  dpäka-  ,abseits  liegend,  entfernt,  von  vorn  kommend^,  arm.  haka- als  1.  Kompositionsglied  ,entgegen'^,  hakem  ,piegare  ad  una  parte,  inclinare^, aksl.  opaky  ,wiederum'^,  ksl.  opako,  opaky,  opace  ,zurück,  verkehrt^  in welchen  freilich  z.  T.  auch  zu  *opi,  gr.  otil^bv  gehörige  Formen  stecken können  (vgl.  lat.  opäcus  ,schattig^  =  ,von  der  Sonne  abgewendet^;  Liter, zur  Bildung  bei  Brugmann  Grdr.  IP  1,  482).  Daneben  anord.  ofugr  ,nach rückwärts  gekehrt^,  as.  abuh,  avuh,  ahd.  abuh,  abah  ,abgekehrt,  verkehrt, böse^  (nhd.  äbig,  äbicht),  ags.  *afoc  in  engl,  awkicard,  aus  *apu-ko-s  (oder aus  "^opu-ko-s :  ojtL&sv,  so  daß  im  Ablaut  zu  got.  ibiiks  ,rückwärts  gehend^, ahd.  ippihhön  ,zurückrollen^?  Johansson  PBrB.  15,  230,  im  Konsonanten auf  Ttv-yrj  verweisend,  s.  auch  Falk-Torp*  u.  avet).
po:
av.  pa-zdayeiti  ,läßt  wegrücken,*scheucht'^;  lat.  2:)o-sitiis,pönö  aus  *po-s[{]nö, po-liö,  po-lübrum,  pörcet  aus  *po-arcet]  alb.  pa  m.  Akk.  ,ohne-,  pa-  ,un-^ (Gl.  Meyer  Alb.  Wb.  317);  afries.  fän  ,von',  as./awa,  /an,  ahd./ona,  fon m.  Dat.  (=  *Abl.)  ,von^  (das  ahd.  -o-  ist  nach  Persson  IF.  2,  215  aus  idg. *pu  neben  *po  herzuleiten).  Eine  ähnliche  Form  sucht  Trautmann  Apr.  389 in  apr.  pan-s-dau  ,danach'^.  GänzKch  unsicher  ist,  ob  arm.  olork  ,poliert, schlüpfrig,  glatt'  nach  Liden  Arm.  St.  60  ff.  o-  aus  ""po-  enthält.  Dagegen hierher  trotz  vielfach  abweichender  Bed.  (Brugmann  Grdr.  II ^  2,  808 erwägt  Aufsaugung  von  idg.  "^upo,  und  für  sl.  po  in  der  Bed.  ,hinter, nach'  m.  Lok.  wohl  richtig  Entstehung  aus  '^pos):  aksl.  po  ,nach,  an,  bei, über  etwas  hin'  (lit.  pö  mit  Gen.  u.  Dat.  ,nach',  mit  Instr.  ,unter'),  als wesentlich  nur  mehr  perfektivierendes  Verbalpräfix  lit.  pa-,  aksl.  po-  (als Nominalpräfix  aksl.  pa-,  lit.  pa  und  pö-,  vgl.  z.  B.  aksl.  pamhnUi  ,sich erinnern',  pa772^^6  ,Andenken');  apr.  pa-  wesentlich  in  nominaler,  pö-  in verbaler  Kompos.,  vgl.  Trautmann  203,  Meillet  Slave  comm.^  505.
55
Über  slav.  po-d^  ^unterhalb,  unter^  s.  Brugmann  Grdr.  IP  2,  733  f.  — S.  noch  idg.  ""po-ti  und  "po-s.
ap-u  steht  neben  ^ajw  (Lit.  s.  u.  *pu)  in  ark.  kjpr.  lesb.  thess.  äftv^'  in alid  abo  ='  ciba,  anord.  au-virdi  n.  ^verächtliche  Person^  (Falk-Torp  HL), yo-l,  auch  oben  *a'pu-ro-  neben  '^^apero-,  *apu-ko-,  und  *pu  neben  *po.  Das -u  vielleicht  enklit.  Partikel  ;,und,  au
=== leaf 63 (p.55) ===
ch^  (Feist  Sa^  508  a^  WH.  I  87). Y«fl.  auch  Schwyzer  Gr.  Gr.  1  182.
pu  (s.  o.'^apu)  meist  in  der  Bed.  (,abge wendet^  =)  ^hinter^  zurück^*
ahd.  fona   (s.  o.);,   ai.  punar  ^wieder  zurück^^   gr.  nviiarog   ^der   letzte^ ;
o-anz  unsicher  lat.  puppis  ^Hinterteil  des  Schiffest o
WP.  I  47  ff.,  WH.  I  If.,  842,  Feist  3  a,  Trautmann  11.
apsä  ,Espe^
Ahd.  aspa,  nhd.  Espe,  ags.  cespe,  anord.  (^sp  L  ds.,  lett.  apse  (aus  *apuse), apr.  abse  ds.,  nordlit.  apitsis  f.,  lit.  apuse,  epuSe  f.  ,Espe,  Zitterpappel^ (nach  Bezzenberger  BB.  23,  298  angeblich  eine  freie  Deminutivbildung aus  *apsa),  russ.  osina  (*opslna)  ,Espe'^,  poln.  osa,  osika,  osina  ,Espe^ Daß  in  diesen  Espennamen  die  Lautfolge  -ps-,  nicht  -sp-  das  Ursprüngliche ist,  bestätigen  u.  a.  tiirk.-osm.  apsak  ,Pappel^,  tschuw.  eives  ,Espe^  als Lehnwörter  aus  dem  Urarmenischen  nach  Pedersen  KZ.  30,  462.  Specht setzt  wegen  gr.  dfteXXöv  aiyeigog,  8  ian  eidog  divSoov  Hes.  ein  Wurzel- nomen ap-  an.
WP.  I  50,  Specht  Dekl.  60.
I.  ar-^),  themat.  (a)re-,  schwere  Basis  ars-,  re-  und  i-Basis  (a.)ri-,  rei-  (ent- weder aus  dem  lo-Präs.  *(a)re-iö  entwickelt  oder  ursprünglich,  so  daß *(a)re-  vorkonsonantische  Entwicklung  daraus)  ,fügen,  passen^,  mehrfach und  vielleicht  ältest  vom  planmäßigen  Aufeinanderlegen  beim  Holzbau (auch   Steinbau??    Meringer   IF.  17,    124)   und  vom  Aufstapeln   von Hölzern,  aber  auch  vielfach  auf  geistiges  Zurechtlegen,  Berechnen  über- tragen. Ausführlich  bes.  Persson  Beitr.  632  f.,  666,  741  f.,  856. Av.  aränte  ,sie  setzen  sich  fest,  bleiben  stecken^,  ai.  ard-h  ,Radspeiche^, aram,  dlam  Adv.  {dramkar-,  alamkar  ,zurechtmachen^  und  ,dienen^,  wozu wohl  ara-ti-  ,Diener'^  und  rä-ti-  ,bereitwillig'^,  av.  räiü  ,dienstwillig,  Diener^) ,passend,  genug'^,   av.  ardm   ,passend,    entsprechend'^  (ardm-pid-tvä   ,Mittag^
^)  E.-M.  74  will  wegen  arm.  eri  ,Bug,  Schulter  von  Tieren',  y-eriurel  , anpassen'  eine Grundform  *er-  postulieren.  Aber  arm.  eri  geht  nach  Lidön  Mel.  Pedersen  88  f.  auf  idg. *reito-,  *reiti  zurück!     Vgl.  Trautmann  242.
56
=  ^die  zum  Mahle  passende  Zeh'^  woneben  ra-pid-wä  ds.  mit  Schwund- stufigem  ra-  neben  ^ara-,  wovon  ardin  Adv.^  Bartholoraae  Airan.  Wb.  189/ 1509)^  ratu-  m.,  ^Richter^  Schiedsrichter^  und  ^Zeitraum^  (gemeinsame Grundbedeutung  etwa  ^Zurechtlegung^^  woraus  .Zurechtlegung  des  Rechts^ und  ^richtiger  Zeitpunkt^);  ai.  ar-p-dyati  ^steckt  hinein^,  befestigt^;  über hett.  har-ap-  (karp-)  jhinstellen*^?  vgl.  Couvreur  H  114  f.;
arm.  arnem   ^mache^;,   y-ar   ^consentaneo^   congiunto^  contiguO;,    appresso' (arar  ^hat  gemacht^  =  gr.  Hoage),  wovon  yarem  ^aggiungere^  congiungere^ (Bugge  KZ.  S2,  21)^  car  ,schlecht^  mit  negativem  c  [=  oc]  ^nicht  passend'  | (Bugge  aaO.  23);
gr.  ägaglayicü,  Perf.  llgäga  ;,füge  zusammen'^,  Ugiisvog  ^angefügt^  passend'^ 'oag  ^Gattin'   (wohl  nach  Brugmann  IF.  2'S,
```


## [2026-09-04T22:41:31.549Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==61' POK_01.txt | tail -30",
 "description": "Pokorny p.52 end / entry head"
}
```


### [2026-09-04T22:41:33.539Z] TOOL RESULT

```
der  gehört  up-  eher  zu aksl.  vopa  ^See^?).  Hierher  Ach-{^aps-)  in  cymr.  FIN,  gall.  Axonal
Daneben  kelt.-lat.  ah-,  s.  u.  ah-.
Zur  Erklärung  der  6-Form  geht  Johansson  IF.  4^  137  f.  von  dem durch  ^Atzlööjv,  ^Amdavög  sowie  durch  ai.  dbda-h  m.  ^Wolke^  und  den  mit äpah  paradigmatisch  zusammengeschweißten  Instr.  Dat.  PI.  ai.  adhliih, adbhyah  vorausgesetzten  St.  *ap(9)d-  (vielleicht  ^Wasser  gebend'^  mit  zu dö-  ^geben''  gehörigem  2.  Gliede)  aus:  *ahd5(n),  Gen.  *abdnes,  woraus *abnes',  aus  den  obl.  Kasus  entsprang  lat.  amnisj  während  im  keltischen *abdö(n) :  *abnes  zu  *abä  (mir.  ab),  ^abonä  (daher  mir.  abann)  ausgeglichen wurde.
WP.  I  46  f.,  WH.  I  40,  846,  Krabe  Gl.  20,  188  ff.,  Pokornj  UriUyrier 110  ff.,  130  f.,  Krabe  Würzburg.  Jahrb.  1,  86  ff.
3.  ap-,  äp-  ,gebrechlich;  Schadend
Ai.  apvd  ,Krankheit,  Durchfall,  av.  (von  einem  -es-St.)  afia-  m.  ,Schaden, Unheil;  lit.  opus  ,schwach,  wund,  gebrechlich^  (Charpentier  KZ.  40,  442  f.), vermutlich  gr.  '^TTsöavög  ,gebrechlich,  schwach"  (Bezzenberger  BB.  1,  164; zum  Ausgang  s.  Risch  98;  anders  Schwyzer  Gr.  Gr.  I  530).
WP.  I  47,  Specht  Dekl.  345.
appa  ,Vater^;  Lallwort.
Vgl.  gr.  äTtTTcc,  dncpa,  ^ncpa,  ärccpvg  (Theokrit)  ,Papa';  toch.  B  appakke ,Vater^  (das  -{a)kke  von  ammakki  ,Mutter^). WP.  I  47.  Vgl.  auch  pap(p)a.
apelo-  ,Kraft^
Gr.  dv-a7teXdaag'  dvaQQcja&elg  Hes.,  ion.  E^nelrjg  ,kräftig^,  hom.  dXiyrjTreliT) ,Ohnmacht',  ion.  dvr^nslit}'  äad-sveia  Hes.,  elischer  MN  Tevrl-artlog (nach  Prellwitz  BB.  24,  214  ff.,  Kretschmer  Gl.  18,  205  hierher  'ArtBlluiv, "Aitolloiv,  mit  Vokalabstufung  thess.  "Anlow^  nach  Sommer  IF.  55, 1762  vielmehr  vorgriechisch)  ;_ill.  ym  Mag-aplinus,  Aplus,  Aplo,  Aplis,  -inis, FN  Aplo,  -onis-  gall.  VN  Di-ablintes  ,'die  Kraftlosen^  (aus  *-aplentes)', germ.  GN  Matroms  Aflims,  Afliabus  ,den  (Zauber)  Wirkenden^  aisl.  afi  n., ags.  afol,  abal  n.  ,Kraft^
WP.  I  176,  Feist  la,  Kretschmer  Gl.  24,  250.
53
ipero-  ;Ufer^
Gr.  iJTtsLQOQy  dor.  äTzsioog  L  ^Ufer;  Festland^;  ags.  ofer,  rand.  over^  mhd. (md..)  uover,  nhd.  Ufer]  aber  arra.  a'p^n  ^Ufer^  erfordert  idg.  j9Ä  und  bleibt
daher  fern.
Beziehung  zu  *«2^o  ^ab^^  ai.  dpara-  ^hinterer^  späterer^  als  Dehnstufen- bildun^''  wird  von  Specht  Dekl.  23  angenommen.
WP°  I  48.
apo'   {po,  ap-u,  pu)  ,ab,  weg^
Ai.  dpa  ^weg;  fort^  zurück^  als  adnominale  Präp.  m.  Abi.  ;,von— weg^^^ av.  ap.  apa  ^von-weg^;  über  privatives  *a^-  im  Iran,  und  Gr.  s.  Schwjzer ZII.  6;  230 ff. ;  gr.  ^tco,  änö  m.  Gen.  (=  *Ablativ)  ^von�
```


## [2026-09-04T22:41:40.783Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 182 183 184; do echo \"=== leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((n+1)) KNT.txt | head -60; done",
 "description": "Kent p.168 area"
}
```


### [2026-09-04T22:41:45.323Z] TOOL RESULT

```
=== leaf 182 ===
he field of historical romance. See also PW 3A.710-2, s.v. Smerdis.
III. Tae HELPERS or DARIUS
The names of the six Persian noblemen who co- operated with Darius in slaying Gaumata the false Smerdis, are given in Behistan §68 and in Herodotus 3.70; there is agreement in the names of the first five:
Behistan Herodotus Vi"dafarnd son of Vayaspdra —— Intaphernes {Дата son of 8uxra Otanes son of
Pharnaspes
Gaubaruva son of Mardunitya ^ Gobryas Vidarna son of Bagübigna Hydarnes Bagabuxsa son of Détuvahya ^ Megabyzus Ardumamé son of Vahauka Aspathines
Herodotus, it will be seen, differs from the Behistan account in the name of the father of
Utana-Otanes; but he gives (7.82) Mardonius, the general in the third invasion of Greece, as son of Gobryas, which indicates agreement as to the name of Gobryas’s father. But Megabyzus son of Zopyrus (7.82) may or may not be the Behistan Bagabuxía son of Datuvahya, or his grandson. Herodotus does, in fact, mention all six of the helpers of Darius in passages outside 3.68-88, in passages which may be found in any Index Nomi- num Propriorum to the text of Herodotus.
The Behistan inscription mentions Vidarna again in §25, as defeating one of Phraortes’ armies in Media; Vi"dafarna in $50, as defeating the rebels at Babylon; Gaubaruva in $71, as crushing the last revolt of the Elamites.
IV. Tug Persian CALENDAR AND Benistan I-IV
In Behistan 4.4, Darius states that the 19 battles recorded by him in the first three columns of the inscription, with the attendant capture of 9 usurpers, took place hamahyáyà 6arda ‘in one and the same year’. For eighteen of the battles dates are given in the Persian calendar, with translation into the Elamite and the Akkadian. The difficulty has been to arrange these dates within one year, beginning with the killing of Gaumata, the false Smerdis; for the order of the months in the Persian
calendar, and in the other calendars, was by no means certain. Now, however, with evidence from additional Akkadian and Elamite tablets which have no Old Persian version, Arno Poebel has suc-
ceeded in reconstructing the lists of months, as
follows:!
! AJSLL 55.139-42. The Persian calendar has been the subject of many studies, but Poebel’s studies have sup- planted them all: ALSLL 55.130-65, 285-314, 56.121-45. Cf. also Hinz, ZDMG 96.326-31;
TEXTSIWITH NOTES AND TRANSLATION
Old Persian Elamite Akkadian Equivalent
1 Adukanaiša Hadukanna$ Nisabbu Mch.- Apr. 2 Otiravahara Turmár Andru Apr.- May 30üigarci$ — Sdkurrisif —— Simannu May- June 4 Garmapada Karmabada$ Dwūzu June- July ОТОТ Turnabagi$ Abu July- Aug. ена агра (та) & — Ulülu Aug.- Spt. 7 Bügayüdi$ — Bagijüti Taxritu = Spt.- Oct. 8 *Vurkazana Margaíana$ Arahsamna Oct.- Nov. 9 Aciyadiya  Haifuüt(;a)& Küslimu — Nov.- Dec. 10 Anémaka HandmakaS Tebétu Dec.- Jan. It Sami(ia)maS Sabitu Jan.- Feb. 12 Viyarna = =Mitia)kannaS Addàru Кер. Мер.
The narrative of the revolts, however, is not given in temporal sequence in Columns Т-Ш, but rather in а geographical order conditioned by the order in which the rebellious provinces are named in $22: Persia, Elam, Media, Assyria, Egypt, Parthia, Margiana, Sattagydia, Seythia. If we should reduce the story to a more easily intelligible pattern, it would be аз follows:
After Cambyses, son of Cyrus the Great, secretly slew his full-brother Smerdis and went on the expedition to conquer Egypt, uprisings against his rule took place in Persia and in Media and elsewhere (810). Notably a Magian named Gaumata led the revolt, claiming to be Smerdis, whose death was known to but few; he started his revolt on XII 14 of 528/2, and received the adherence of the entire Empire, becoming King on IV 9 of 522/1? Cambyses died by his own hand, either intentionally or accidentally, in Egypt soon after hearing of Gaumata’s revolt, (§11).
Three months later Darius and his associates killed Gaumata and his ehief followers at Sikayau- vati in Media, on VII 10 of 522/1. Thereby Darius
2 The months will be indicated by Roman numerals.
161
became King, but at the very outset his rule was contested by Agina in Elam, and by Nidintu-Bel (claiming to be Nebuchadrezzar son of Nabonidus) in Babylon, who were recognized as King each in his locality. But Аспа did not last long; Darius, after organizing the gove
=== leaf 183 ===
rnment in Media and Persia, gathered an army of Medes and Persians and marched toward Babylon, passing near Elam. As he passed he sent orders to the Elamites, and in terror they seized Acina and brought him in fetters to Darius, who slew him ($17).
Darius with his army went on toward Babylon against Nidintu-Bel ($18), and in his absence from Media and Persia several rebellions started (§21)— some perhaps started earlier, but news of them did not reach Darius before he had set out against Nidintu-Bel: (a) that of Vahyazdata in Persia, with the adherence of Sattagydia and perhaps of a faction in Arachosia (§45); (b) that of Martiya in Elam; (с) that of Phraortes in Media, with the adherence of Armenia (§26), of Assyria, and of Parthia, including Hyreania (885); (d) that of Frada in Margiana; (e) that of Egypt; (f) that of Skunkha in Seythia (821).
Darius came upon Nidintu-Bel and his army at the Tigris, forced the crossing, and defeated him in IX 26 ($18), and though Nidintu-Bel rallied his forces and took the offensive, again defeated him at Zazana on the Euphrates, X 2 ($19); he pursued him and his few remaining horsemen to Babylon, took that city and Nidintu-Bel with it, and put the rebel to death ($20).
Meanwhile events were progressing elsewhere. Against Frada, who had made himself ruler of Margiana, Darius had sent Dadarshi, a Persian officer who was governor of the neighboring prov- ince of Bactria, with his local forces, and Dadarshi won a decisive victory on IX 23 (838), restoring Darius’s rule in Margiana (839).
Phraortes, claiming to be Khshathrita, of the family of Cyaxares, had made himself king of a great part of the Empire ($21). Darius’s first step was to send Vaumisa, a Persian officer, against the rebels in Armenia; he must have sent Vaumisa early in the Babylonian campaign, for Vaumisa, on the way north, was met by the rebels at [zala in Assyria, on X 15. What forces Vaumisa had at his disposal is not stated, but no mention 1s made of sending troops with him; presumably he gathered up loyal troops on the way. By,this battle Vaumisa
162
drove the rebels back into Armenia, where he fought a second battle with them some months later ($80; see below).
Although the force of Medes and Persians which Darius had with him in Babylonia was small, he had been obliged, at an early date, probably not much after the battle at the Tigris, to send Hydarnes, a Persian officer, with a strong force against Phraortes in Media. Hydarnes met an army of Phraortes (but not Phraortes himself) in battle at Maru in Media, and fought a battle on X 21; but it seems to have been indecisive, for thereafter Hydarnes waited for the arrival of Darius and his army from Babylonia (825).
Parthia and the neighboring distriet of Hyreania had both gone over to Phraortes, but Darius's father Hystaspes was in command of the army in Parthia, and the army remained loyal. In a battle at Vishpauzati, on ХП 22, Hystaspes fought the rebels, but the victory was not decisive.
After the death of Nidintu-Bel at Babylon, Darius set forth for Media against Phraortes (§31). His march took him near Elam, where a Persian named Martiya had set himself up as King under the name of Imanish. At the approach of Darius the Elamites were terrified, and seized Martiya and killed him (§22-§23) Darius now sent a force of Persians and Medes under Arta- vardiya, a Persian officer, against Vahyazdata, who had made himself King in Persia; he himself, with the rest of the Persian force, went on into Media (§41) and at Kunduru was attacked by Phraortes himself and his army, on I 25, 521/0 (§31). Phraortes’ army was routed; he himself es- caped with a few horsemen, but was overtaken and captured at Raga, and mutilated and put to death with torture at Ecbatana ($32). From Raga Darius sent a force of Persians to reinforce Hystaspes in Parthia (§36).
Hereupon a Sagartian named Cicantakhma, perhaps commander of local forces that had ad-
3 Poebel, AJSLL 55.154, sets the undated killing of Martiya after the death of Phraortes, because in the sculptured line of captives on the Behistan Rock the order is Gaumata, Аста, Nidintu-Bel, Phraortes, Martiya, Cigantakhma, Vahyazdata, Arkha, Frada. 
=== leaf 184 ===
I re- ject this interpretation of the series of sculptures, since it would oblige us to set the death of Frada at the very end of the series, dating his defeat not IX 23, 522/1, but IX 28, 521/0, and thus extending the series of events from 13 months 12 days to 14 months 13 days.
OLD PERSIAN
hered to Phraortes, declared himself King in Sagartia, a distriet of northern Media; he claimed to be of the family of Cyaxares. Darius sent а force of Medes and Persians under Takhmaspada, a Median officer, who defeated and captured Cicantakhma, bringing him to Darius. Darius mu- tilated him and put him to death with torture, at Arbela ($33). Thus ended rebellion in Media (884) ; but there was still a strong rebel force in Armenia, against which Darius sent an Armenian officer named Dadarshi. Dadarshi, thrice attacked by the rebels, defeated them successively at Zuzaya on II 8 (§26), at Tigra on II 18 (§27), and at Uyama on III 9, whereafter he waited for Darius to come and make final governmental dispositions (828). This third battle by Dadarshi was only nine days after Vaumisa in а second engagement beat off the other force of Armenian rebels in the dis- trict of Autiyara, on IT 30; after which he also awaited Darius’s arrival (530). There was по fur- ther fighting in Armenia.
Hystaspes, reinforced in Parthia by the Persians whom Darius had sent to him from Raga, sought out the rebel army and crushed it at Patigrabana, on IV 1 ($86). This restored Darius's rule in Parthia.
While Darius was in Babylon, one Vahyazdata, a Persian, claiming to be Smerdis son of Cyrus, had revolted and made himself King of Persia (§40). Apparently confident in his own position, he had sent a force east to Arachosia,‘ against the Persian governor Vivana, who had remained loyal to Darius; but Vivana beat off the rebels at Kapishakani, on X 13 (§45). The rebels again at- tacked at Gandutava on XII 7, and here were decisively defeated (§46); their commander and a few horsemen escaped, but were overtaken and captured at Arshada by Vivana, who put them to death (847).
Vahyazdata in Persia had a few months of un- disturbed rule, but this was ended by the ap- proach of Artavardiya, sent by Darius on his way to Media, with a force of Persians and Medes. Vahyazdata attacked Artavardiya at Rakha on II 12 (§41), and again near Mt. Parga on IV 5. In the second battle Vahyazdata and his chief fol- lowers were taken prisoner (§42); they were handed over to Darius at the Persian town of
t Т regard the revolt in Sattagydia (822) as to be in- cluded under the events in Arachosia (§45-§47).
TEXTS WITH NOTES AND TRANSLATION
Uvadaicaya, and Darius executed them with tor- ture (§43). Darius was now back in Persia, which had been restored to his rule (§44), as well as the other rebellious territories except Egypt and Scythia. It was not quite nine months since he had slain the usurper Gaumata.
But while Darius was putting down the rebel- lions in Media and in Persia, an Armenian named Arkha, claiming to be Nebuchadrezzar son of Nabonidus, had established himself as King in Babylon (§49). Against him Darius sent a Persian officer named Intaphernes with an army, and Intaphernes routed Arkha and his forces on VIII 22, capturing and executing at Babylon both Arkha and his chief officers (§50).
This is the latest event related in the first three
163
columns of the Behistan inscription, 13 months and 12 days after the death of Gaumata; the time does not seriously exceed the one year which Darius boastfully mentions m Column IV.
Column V gives an account of a third rebellion in Elam, under Atamaita; against him Gobryas was sent with an army by Darius, and he defeated and captured him, bringing him to Darius, who put him to death (§71). The date of this rebellion seems to be in the third year of Darius’ reign, 520/19,5 though the Behistan text is here badly mutilated. After this rebellion in Elam Darius went to Seythia and defeated and captured Skunkha (§74). The reconquest of Egypt, tho
```


## [2026-09-04T22:41:51.202Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"apadāna\\|apadana\\|apadàna\\|apadána\" KNT.txt | head -20; echo \"---\"; grep -n \"^apa\\b\\|^apa \" KNT.txt | head; echo \"--- leaf 189/190\"; for n in 189 190; do echo \"== leaf $n ==\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((n+1)) KNT.txt | head -50; done",
 "description": "Kent lexicon apa"
}
```


### [2026-09-04T22:41:55.161Z] TOOL RESULT

```
749:V. Final m is lackmg in туа DB 4.90; tuva XPh 46; X Syana A'Sb; apadāna A'Sa 3, A?Ha 5; ab*yapara A’Sa 4. For all but the last, the forms with -m are found in other passages. Cf. also буа AsH 9, 13°, for буйт ($52. ПІ, $56. V).
4680:1 imam : apadánam : stünàya : afagainam :
4705:A’Ha = Artaxerxes IT, HAMADAN A. 1 Gatiy : Artax&agà : XS : vazraka : XS : XSyanim : XS : DHyünàm : XŠ : ah 2 yaya : BUyà : Dárayavasahy& : XShya : puça : Dérayavasahyd : ArtaxSatra 3 hyà : XShy& : puça : Artaxšaðrahyā : Xšayāršahyā : XShya : puça : XSayar 4 šahyā : Darayavagahya : XShya : puça : Dérayavasahyd : V?Stáspahyà : puça 5 : Haxàmanisiya : imam : apadàna : vašnā : AM : Anah*la : иа : Mitra : adam : akun 6 ат : AM : Anah'ta : uta : Mitra : mam : püluv : ћасӣ : vispd : gaslá : ut Т & : imam : tya : akunà : mà : vijanátiy : mà : vinátayàtuy Notes то А?На: *? ArtazXatrahyá, acc. to Tm. Lex. 54, and not -cahyd. * [hacd : gastá] WB; [utàmaiy : zsagam] Tm.; [ћасӣ : vispé : gasta] Kent, after A°Sd. " akuna for akundm, and ma with following lost verb, as in A'Sa;
4708:АНЬ = Artaxerxes П, HAMADAN В. apadànam : stünàya : afagainam : ArtaxSaca : XS : vazraka : akunaus : hya : Dārayavauš : XS : руё : Haxdmanigiya : Mitra : mam : paluv
4709:Nore то АНЬ: Probably the demonstrative imam stood before apadānam at the beginning, and other
4999:apaddna- sb. ‘palace’: from apa- + déna- ($147.I) to root *dà-, cf. Skt. apadhá- ‘conceal- ment’, Gk. атоблк ‘storehouse’. For development in later Iranian, with ара- by secondary length- ening (but not OP appa-, cf. $130), see Henning, Trans. Philol. Soc. 1944.110n. apadünam asm. D*Sal; АНЬ. apadàna (852.V) A’Sa 3, 4; A?Ha 5.
5516:dàna-, in apadana-, daivadàna-: Skt. dhana-m ‘container, receptacle’; from OP *dé- + suffix -na- ($147.1).
---
2255:apa-. A
4994:apa- prefix (§206b) ‘away’: Av. Skt. apa, Gk.
--- leaf 189/190
== leaf 189 ==
n., asn.); AÁuramazdü, АМ; ava (nsn.); avdkaram, avükaramca-; ucdram; uld, uta-; tya (nsn., asn.); dahydus; duvarayd; nat-; pati-; pasdva; уава; haw, hau-: Asl 12; DB 1.25 bis, 55, 87, 94; 2.24, 34, 40, 45, 54, 60, 68, 75, 79, 86, 90, 96; 3.6, 11, 17, 37, 441, 61, G6f, 87; 4.39, 46, 60, 64; DPd 28°; DPh 8, 10; DNa 50 (m° omitted, $52.VI), 52#, 544; DNb 13, 28, 28f, 31, 32f, 33, 48, 51, 52; DSe 51°, 52°; DSE 10, 19°, 20°, 58; Ds} 4°, 6°; DSk 5; DSI 4f; DSm 3°; D8s 7°; DSt 9°; DH 6, 8; Хра 15, 18f, 191; XPb 24, 29, 30; XPe 13 bis; ХРа 18f, 19; ХР 32, 38, 41, 45f, 47; XPg 14; XPh 32, 45, 58,
167
60; Хе 5° bis; XV 261°, 27°; A!Pa 23°, 24°: A’Sdb 4 (-may de, $52. VT); А?Не 20 bis.
-ma gsm. for -maty ($198.11); apan*yáka-ma А?За 3; [n"yà |kama for n*yàkam-ma (5130) A’Sa 4. Not kamna-ma DB 2.19, as taken by Tolman.
-ma absm. enel. (Av. maf, Skt. mat, pIE *med, $193.IV; orthotone pIE *méd in oLt. méd, elLt. mē); only in hacd-ma DB 1.19, 23; 2.6, 12°, 16, 98; 3.27, 78, 81; 4.92; DPe 9; DNa 20; DSe 19°; XPh 18. Not duviliya-ma DB 3.24 (with Bthl.); not apara-ma DB 4.37, 68, 87 (with Bthl.), nor DSt 10°.
vayam npm. (Av. vaém, Skt. vaydm, рї Е *uei + pAr. -am, cf. Gt. wei-s; §193.V) DB 1.7, 10°; DBa 10, 17.
amazam gpm. (Ау. ahmakem, Skt. asmákam; $118.11, §193.VI) DB 1.8, 28, 45, 49, 61, 69, 71; DBa 12.
Adukanaisa- adj. ‘Adukanaisha’ , first month, March-April: Elam. ha-du-kan-na-1§, АКК. nisannu: -natsa- on the evidence of the Elam., acc. to MB Or. $96, rather than -nisa- ($117). Cpd. of adu- ^ + kan- ‘dig’, possibly with vriddhi ($126; Adu- ?): "Irrigation-Canal-Cleaning Month’, re- ferring to the cleaning of the underground con- duits for irrigation water, regularly done in the spring (cf. РЕШ. AiW 61). Adukalnaz]Sahya gsm. DB 2.69.
an- neg. prefix before vowels, ef. !a- before consonants: Ау. Skt. an-, Gk. &»-, Lt. in-, Gt. un-, pIE *on- (867.1); in Anáhatà-.
and ism. to ?a- (q.v.); DPe 8 (not to Av. Skt. ana-); XPa 14 (not prep.).
Anàümaka- adj. ‘Anamaka’, tenth month, Dec.-Jan.: Elam. handémakas, АКК. febétu. Cpd. of neg. a- + ndma- ‘name’ (see ndman-) + adj. suffix -ka- ($146.11), possibly with vriddhi (8126; Anámaka- ?): ‘Month of the Nameless (= High- est) God’. Anàmakahya gsm. DB 1.96; 2.26, 56; 3.63.
Andhita- sb. ‘Anahita, Anaitis’, a goddess: Elam. a-na-hi-ud-da, Akk. a-na-ah-t-tu-’, Gk. ’Avairs; Av. andhitd-. Cpd. of neg. an- + pte. pass. dhita- ‘spotted, defiled’, of uncertain connec- tions (§67.J, §118.V, §242.1): ‘The Spotless’. The OP writings, being late, fail to show length of б in either position. Anahita (827, $52.11) nsf. A’Sd 3f; Anah*ta, A’Sa 4 (as gen., §313.11), 4f; A?Ha 5° (as gen.), б.
4
168
antya- adj. ‘the one or the other (of two), other (of any number), rest of’ (JNES 3.2334; not ‘enemy’, cf. Kent, JAOS 35.345.n6 and Bv. TPS 1945.56-9): Av. ainya-, Skt. anyd-, pIE *anjo-, cf. *аЦо- in Gk. ados, Lt. alius, and *an- tero- in Gt. anpara-, Gm. ander, NEng. other (889, 144.1, $204.17; decl, $203). aniya nsm. DB 1.95; 3.32; DSe 33°, 35. aniyam asm. DB 1.86; 0.25, 28; DSe 33, 35f. aniyahyd gsm. DB 1.87. aniyanā absm. DPd 11; DPe 20f. aniyai-ciy npm. XPf 29. aniyaha npm. ($10, $172) DB 4.61, 62f. aniyä nsf. ПЕ 25, 26 (not with Bv. Gr. $834, inst. as adv. ‘on one side ... on the other). aniyām asf. DSe 48f. aniya прі. DB 1.41. aniyüapf.DB 1.47, 67. aniyāwvä lpf. ($72) DB 1.35. aniya asn. XPf 39. aniyaš-ciy nsn. (§9.VI, 8105) DB 4.46; XPa 13; ХР 41f (written antyase*, §52.1).
an|iya|éa adv. ‘in other ways’ ($191.17); Cam- eron's interpretation for his reading але ++ wms, DB 4.89.
атш) (ie. anu) prep. ‘along, according to’: Av. anu with acc., loc., ‘toward, along’, Skt. ánu with acc. ‘after, along’; see also anuSiya-. (1) With inst., DB 1.92; DNb 25 (ef. Lg. 15.176). (2) With gen., DNb 16, 18 ($137, $267.IV ; anu-dim + gen.).
anuxiya- adj. as sb. ‘follower, ally’: from anu- (see anw) + adj. suffix -ja- (S80, §144.VI). anusiya nsm. DB 2.95. anusiya npm. DB 1.58; 2.77; 3.49, 51, 74, 90, 91f; 4.82.
apa- prefix (§206b) ‘away’: Av
== leaf 190 ==
. Skt. apa, Gk.
and, Lt. ab, Gt. af, Gm. ab, NEng. оў, off, pIE *apo. Used with vb. gaud- and in sbb. apaddna-, apa- niydka-; with suffix in apalara-, apara-.
apataram adv. ‘farther off, far off’; nsn. of
apatara-, which is apa- + comp. -fara- ($82,
5190.111), ef. Gk. adv. ётотіро. DNa 18; DSe 16f; XPb 25; XPh 16.
apaddna- sb. ‘palace’: from apa- + déna- ($147.I) to root *dà-, cf. Skt. apadhá- ‘conceal- ment’, Gk. атоблк ‘storehouse’. For development in later Iranian, with ара- by secondary length- ening (but not OP appa-, cf. $130), see Henning, Trans. Philol. Soc. 1944.110n. apadünam asm. D*Sal; АНЬ. apadàna (852.V) A’Sa 3, 4; A?Ha 5.
apantyüka- sb. ‘great-great-grandfather’: from apa- + niyäka- ‘grandfather’, cf. Lt. ab-avos
OLD PERSIAN
'great-great-grandfather'. §52.1) пет. A’Sa 3.
apara- adj. "later, after’: Av. Skt. apara-, from apa- + comp. -ra- ($32, 419.11). арата пет, XPh 47. aparam asn. as adv. DB 4.37, 42, 48, 68, 70, 87; DSt 10° (not apara-ma, nsm. with enel. abl., DB 4.37, 68, 87—and DSt 10°—as Bthl. AiW 77 suggests, following АКК. $a be-la-a ar-kt-a ‘who shall rule after me’).
apan*ydka-ma — (822,
pi- sb. ‘water’: Av. áp-, NPers. db, Skt. pl. nom. dpas, acc. apás, pIE *йр-, with or without i-extension, which seems to have become 5 in OP ($422). āpišim (= apis-Sim; $41, $130) nsf. DB 1.95f. apiyálsf. DB 1.95. abis (Skt. adbhts, and dat.-abl. Skt. adbhyds, Av. aiwyó, both from *ap- bh-; §75.1V, $130, §188.V, JAOS 62.269-70; see also s.v. abi) ipf. DB 1.86.
apiy adv. ‘thereto, very’: Av. arpi, Skt. ápi, Gk. prep. &t ‘on’, pIE *epi (§44, §191.1). In OP, normally enclitic, but sometimes written sepa- rately; often with dūraiy ‘afar’ (5136): dürai-apty ‘far and wide’ DNa 12; düray-apiy DNa 46; dū- raiy apiy as two words, DSe 11, DZe 6, DE 19, ХРа 9, XPb 18f, ХРе 8, XPd 13, ХР? 13, XPh 10f, XE 18, XV 14, A!Pa 14^, A*He 17f. Prob- ably vafsna[pi]y X Pg 7f (Ву. BSLP 34.1.32-4) with crasis, rather than vadsnd-[cily or vasnà-[di]y (Lg.
9.230); KT's lapli-maiy is eliminated by - -
-€
Cameron’s reading of utämaiy as completely visi- -
ble, DB 4.46 (ef. note ad loc.).
afuvayd, error of writing for aruvdya (855.11); see aruva-.
abiy prep. and prefix ‘to, against, in addition to’: GAv. aibi. LAv. aiwi, Skt. abht; conflux of pIE *mbhi, oHG umbi ‘round about’, and pIE *obhi, oCS ой ‘beside, by’.
(1) Prep. with acc., DB 140, 76, 80, 82, 84; 2.12,17, 73, 88; 3.2, 3, 14, 27, 56, 60, 71, 82; 5.12f, 21, 22^, 28, 26, 28°; DPd 18; DPe 24; DZc 9f, 12; XPg 10.
(2) Prefix with verb jav-, and first element in abicaris, abyapara, perhaps in Abirddus, but prob- ably not the base of abif. — —
abicari& DB 1.64f, word of uncertain form and meaning, probably asn. of s-stem (5185.11), to abi- + root car- ‘move, go’ (Av. caraiti, Skt. cárati, Lt. colit, 8”; $107), giving, in association
with the following gaidam ‘living personal prop- — .
LEXICON
erty’, а meaning ‘pasture lands’, cf. NPers. cáridán ‘to pasture’ (Spiegel, KT, Bthl. AW 89). Cf. also Tm. Lex. 64-5; Gray, JAOS 33.281-8; Hüsing, KZ 48.155-6; Hz. Ар] 51-4.
abiyaparam. adv. ‘later, afterward’, from abiy + aparam (§191.1V). ab*yapara (822, §52.V) A’Sa 4.
Abirüdu- sb. ‘Abiradu’, a village in Elam: first part perhaps abi-.— Abirüdus пэт. DSf 46.
abi$ DB 1.86, probably not adv. ‘thereby’, abi- + adverbial -s, but ipf. of арі- ‘water’ (q.v.): not an error for äpiš nsf. ‘water’ as proposed by König, Кар 70-1.
abyapara see abiyaparam.
-am, enclitic particle extracted by wrong di- vision from pAr. *azham T’, perhaps even in pIE times, and therefore *-om from *ej(h)om; seen in OP tuvam (cf. adam T’), iyam, imam, patisam, cf. Skt. fuvám тубт imám ete.
ama- sb. ‘offensive power’, see ArSdama-.
amaxamaté, DB 4.92, read by KT, and ap- parently corresponding to Elam. ‘were pleased (at the inscription)’ (cf. Wb. KIA 72n, quoting vari- ant interpretations): possibly for ham-axmatá, aor. mid. of ham- + kam- ‘like, love’ (OP Хата- ‘wish’, Skt. vb. kam- ‘love’),
```


## [2026-09-04T22:42:47.193Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD abdom/abe/abaron ===\"; grep -n \"^abdom\\|^abē\\|^abe \\|^abāz\\|^abārōn\\|^abaron\\|^abar[oō]n\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== PHD grep loose ===\"; grep -n \"abdom\\|abārōn\\|abārōn\" PHD.txt | head -20",
 "description": "MacKenzie Pahlavi entries"
}
```


### [2026-09-04T22:42:47.289Z] TOOL RESULT

```
=== PHD abdom/abe/abaron ===
PHD.txt:3597:abēyīh,
PHD_mackenzie.txt:704:abaron ['p'lwn' I N warun] contrary, wrong, sinful.
PHD_mackenzie.txt:750:abdom ef>dwm I M 'bdwm] last, final(ly).
PHD_mackenzie.txt:11557:abaronih
=== PHD grep loose ===
166:~ih: wonder. àb-dàn [^5d?n!] water-holder. abdast ['5dst!] hand-guard. abdom Pfdwm | М ?bdwm] last, final(ly). ~ih: finality, end. abd-sahist [pdshst'] wonderful. abē- [5»(y)- | M ?by-, N bé] without, Jess. ~-bar [-5/] fruitless. ---bé$ [-bys] unharmed. ~-bim [-bym] fearless. ~-bimih: fearlessness. e--boy [-bwd] senseless. ---bēyih : senselessness. —-büd(ih) [-bwt', -bwtyh] deficiency. «=čim [-cym] without reason, cause. abēdān рругп!] of use, wanted. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. ~=-68 [ws] M *by?wš, N béhóf] senseless, unconscious. -~-6Sih : senselessness, unconsciousness. abér [yl] very, much. abē-rāh Payis] e erring. abesar [fysl | M ?bysr, N afsar] crown. abesīhēnīdan, abesihén- [Ashyn-ytn', v. abesihidan] destroy. išn(īh): destruction. abesihidan, abesih- Pžs(y)%-ytn! | M? bysyh-] perish, be destroyed. —išn(ih): destruction, ruin. abespardan Pžļsp?/tn!) = abespurdan. abespurdan, abespār- [’fspwltn', ?psp'l- | M ?byspwrd, ?byspr-, N sipurdan, sipàr-] commit, entrust, consign. ubestag [5(y)s? k!] Avesta, the Mazdean scriptures, abestām [ēst m] = abestān. abestàn [°25/°п!] refuge, support, trust. ābestan Dóystn! | P ?bystn, N abtstan] = ābustan, abé-süd [yý swt'] profitless. “Аһ: profitlessness. a-bëš Буў] harmless; unharmed, invulnerable. ~ih: harmlessness; invulnerability. abē-|-wināh [-cwz?^s | M?bywr? 1] innocent. ~-wizend [-wznd] harmless, invulnerable, safe. abézag Pfyck! | M ?bycg, (N *oëza)] pure, holy. ~th: purity, holiness, abēzār Pye’, ?Буе?1 | N bézdr] free.
1761:end abdomih, frazam, hanjām, karan, Sar; come to an — 6 ham madan; v. finish; from ~ to ~ sarasar.
1935:final(ly) abdom, pasén.
1936:finality abdomih.
2566:last (a.) abdom, pasén.
```


## [2026-09-04T22:42:58.028Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '700,710p;745,755p' PHD_mackenzie.txt; echo \"=== NYB p.23 (leaf 31) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==32' NYB_vol2_glossary.txt | head -60",
 "description": "MacKenzie abaron; Nyberg p.23"
}
```


### [2026-09-04T22:43:00.440Z] TOOL RESULT

```
abarmind ['plm'nd] inheritance, privilege.
abarmlnig ['plm'nyk l ] noble.
abar-meniin ['Plmjmfn ] proud, haughty.
                             '
abaron ['p'lwn' I N warun] contrary, wrong, sinful.
 .....ih: sin.
abar-oz ['pl'wc] stronger.
 .....ih: mastery.
abar-tan ['Pltn l ] arrogant.
 .....ih: arrogance.
abarwez ['plwyc I (M 'brwyj, N parwt?z)] triumphant, victorious.
  -- sahistan: seem wonderful (to) > marvel.
abdih                            3                          abezir
 ......ih: wonder.
ab-dan ['pd'nlJ water-holder.
abdast epdst'] hand-guard.
abdom ef>dwm I M 'bdwm] last, final(ly).
 ~ih: finality, end.
abd-sahlst [Y>dshst l ] wonderful.
abe- epy(y)- I M 'by-, N be] without, -less.
 ,...,- bar [-bl] fruitless.
 ~- bes [-by!] unharmed.
=== NYB p.23 (leaf 31) ===
brdr, sup. ’brdwm; Ps. ?pldl; Paz. awartar, awardar (SGV); NP bar ‘height, top, summit’, bartar ‘higher’. ?apar [MDM, erroneous reading of OAram QDM] 1. adv. above: (3 päs) i-m guft ~ of which I spoke above 65°; či nümak" cé hac ~ nipišt" éstat the inscription that had been written here above P2:3, cf hacapar; — prev. over, on, upon, up, or simply expressing the initiation of the action, with varying vbs., cf esp. (@)ma- tan, burtan, grätan, raftan, rasitan ; follow- ed by enclitics: apar-p-im ravišn I must needs ascend 4076, v.s.v. -p(i); — refer- ring back to an encl. pron.: api-š Vidrafš . ~ mšast and V. got on it (the horse) 25W5; cē-t avdom margéh ~ raset for at the end Death will come upon thee 726-7; (martömän) tāi-šān āmēcišn ~ nē barend as long as one does not impart instruction to them 801. — 2. prep. a) local: over, on, on to, down on: Krisäsp ~ én damik raset K. is roaming all over this earth 3318; ~ giyāk on the spot 3", 102; ~ ki Zartuxst bé dahém where we shall deposit Z. 3957; ~ pad ēstāt rose to his feet 1821; asp ... — rahy vartét harness the horse! 5418-14; srišk ~ srišk drop after drop 214
apar-gar
(cf 41?" and 89%); ~ fravartak in the letter 1822; — combined with another prep.: ~ 6 pad estat 28%. 1189. 11917 (cf above 1871); ~ 6 ax“ i astomand 401; m andar äyiyänak 409; ~ tdi sdxdn 401; ~ pat óstak 48% (ete.). — b) temporal: ~ sal 2 mazdesn bag’ Šāhpuhr” in the year 2 of the Mazdayasnian Divine Sh. Pl:l; ~ sal "68 in the year 68 P2:1; ~ pat han jamān ka at the time when 41%, adak ~ pat jamän at that time 619; 4214; 3 sap td three nights ago 512-3, — c) figurative: on, about (esp. in headings and book titles), concerning; (reigning) over, (merciful) to, (hostile) to- wards; (means) for; ete.; — with an inf. or a v.n.: in order to 3714-15, 4515; 1185 (continued by inf. + rād, l. 6). - ~ does not govern encl. pronouns; single excep- tion apar-aš 54° (late passage). — Av. (394 sq.) upati, OP upariy; MPrthPrs br; Paz. awar; NP bar. Cf aper. — On MDM 43" v. hàreftan.
apar-apakčh [MDM ’p’kyh] heavenly, di- vine help 591°.
apar-āstišnēh [’pl’stSnyh] the act of ac- cepting and taking care of: ~ % én den rād 589, with the gl. kū tà? pat én den bē éstat (subju. 3d p. sg., v. estátan) ; 5919. — < apar + ēstātan; as to the alternation é-: à- cf ästenisn.
apar-barišnēh ['plbišnyh, MDM blšnyh, MDM YBLWN-šnyh, MDM YDLWN- Snyh] the act of ascending, ascension; transport, ecstasy 5121-25. 524.9, 5319; cf taš. — < apar + burtan (q.v.); opp. frēt-barišnēh (g. v.).
apar-burtārēh [MDM bwlt'lyh] the act of procuring, or the state of having procured 4425-26, — V, s. v. burtan.
apar-gar [’plgl] the Supreme Power, Fate 137. — Cf Av. (394) uparö.kairya- "whose work is transcendent’; Paz. awargar (SGV XIV” ‘supreme’ of Adonai); NP bar-gar ‘fortune’.
www.parsianjoman.org | ool jb
apar-gumext
apar-guméxt ['plgwmyht'] alloyed: äsen ~ alloyed with iron 110% — Pt. of apar + guméztan (g. v.).
apārīk [’p’ryk; Prs inser. ’p’lyk] other l. attribute, placed before its subst., passim; seldom inflected in pl. before a subst. in pl. cas. obl.: hac ~-dn giyākān u röstäkän 8617-18, — 2. independent: ~ other people 5026-27; han i evak ... the one ... and the other 1093; ēvak-ē ... u ~ one... and another 12115; ~ har cé all other things that ... 862. 10411, 1211
```


## [2026-09-04T22:43:08.316Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"apārōn\\|apārön\\|ap'rōn\\|apāron\\|aparon\\|awàrūn\\|warun\\|wārūn\" NYB_vol2_glossary.txt | head -20; echo \"=== apē / avdom in NYB ===\"; grep -n \"^apē\\|^apě\\|avdom\\|abdom\\|apdom\" NYB_vol2_glossary.txt | head -20",
 "description": "Nyberg apārōn"
}
```


### [2026-09-04T22:43:08.379Z] TOOL RESULT

```
521:apürón ['p'lwn'; Ps. *p’lwny] 1. adj. wrong 664-11, 691, etc., opp. frärön (g.v.). — 2. adv. backward (= apäc) 1281, — Paz. dwārūn, Skr. v. asadācārin (Mx); NP vārūn ‘inverted, turned upside down’; < OIr apdrda-van-, derived, by means of the suff. -van-, from *apärda- < *apa- arda- ‘whose side is turned away’ (HP II, 15). V. ärak; cf apärik and frärön.
1539:frärön [pl’lwn'] righteous, upright, hon- est 18%, 6919.22.23, 7516. 843, 9024; comp. ~ -tar 552°. — Paz. frürün, Skr v. sadā- cārin; Olr *frürda-van- < *fra-arda-, cf aparon.
7493:värun: aparon
=== apē / avdom in NYB ===
505:lapar [’pl; MDM, v. 2apar] adj. situated above, lying above: évak ~, apäk dit, v.s.v. žapāk (2); — heavenly, often in compounds: apar-apükeh etc., v. below; comp. ~-tar [’pltl] higher 5426, 581°, highest 1097; sup. ~-tom highest 415. 102°; v. also apartaréh; — adv. empha- sizing an adj.: highly, extremely: apar- aržānīk, v. aržānīk. — Av. (393) upara-, adv. upara (instr.), uparam; MPrth ’br adj. and adv. (MHC), comp. ’brdr, sup. ’brdwm; Ps. ?pldl; Paz. awartar, awardar (SGV); NP bar ‘height, top, summit’, bartar ‘higher’. ?apar [MDM, erroneous reading of OAram QDM] 1. adv. above: (3 päs) i-m guft ~ of which I spoke above 65°; či nümak" cé hac ~ nipišt" éstat the inscription that had been written here above P2:3, cf hacapar; — prev. over, on, upon, up, or simply expressing the initiation of the action, with varying vbs., cf esp. (@)ma- tan, burtan, grätan, raftan, rasitan ; follow- ed by enclitics: apar-p-im ravišn I must needs ascend 4076, v.s.v. -p(i); — refer- ring back to an encl. pron.: api-š Vidrafš . ~ mšast and V. got on it (the horse) 25W5; cē-t avdom margéh ~ raset for at the end Death will come upon thee 726-7; (martömän) tāi-šān āmēcišn ~ nē barend as long as one does not impart instruction to them 801. — 2. prep. a) local: over, on, on to, down on: Krisäsp ~ én damik raset K. is roaming all over this earth 3318; ~ giyāk on the spot 3", 102; ~ ki Zartuxst bé dahém where we shall deposit Z. 3957; ~ pad ēstāt rose to his feet 1821; asp ... — rahy vartét harness the horse! 5418-14; srišk ~ srišk drop after drop 214
571:apē- (*py-, ’pyd] v.s. v. apa-. apč-bim ['pybym] fearless, living with- out fear 62%, 8113,
572:apē-brāt ['pvdbbt'] brotherless, having lost his brother 227.
576:apē-cār [’pyc’l]] being without ex- pedient, being at a loss, falling short of (hac): ke (for kū) rāi [restore Py; not +L’!] <i> Pourusäsp hac višopišn i haciš ~ bavét for P.’s judgment will be powerless (defenseless) against destruc- tion from him (viz. Zartuxšt) 4813-14 (gl.), cf 1. 8-9. — V. cār and ?rde.
580:apēgumānēh the state of being without doubts, assurance, firm faith 8324-26, 1073.
582:apē-martūm [pyd ’NSWT?] being with- out men, unpeopled 1055-1,
788:avdom [’pdwm] last 4415. 469, 495.20; adv. in the end, finally, ultimately 729. 10119; pat ~ id. 69; cas. obl. pat avdomeh id. 7718, — OIr *apa-tama-, borrowed in B.- Ar. ’appetom Ezr. 443; MPrs 'bdum, pd ’bdwmyy (S); Paz. awadum, awadim.
969:bé [BR”; Sas. inser. BL”; Prth. LBR"] with enel. bé-c 3812, bé-p 53%, cf also 2bēš: l. adv. outside HajB:8; HajA:7 LBR = ö bé outward; ibd. 9 ‘L LBR? STR? = 6 bē ärak id.; — hac bē Xvanirah from outside Kh. 10812; — bē hac to out- side thee, thy domain 1035 (v.s. v. tē):!!; — together with a following prep.: bé 6 emphasizing the sense of direction inherent in 6, very frequent; still more emphatic tdi bē 6 right up to 9218; bē apar Zartuxst nīšān (g. v.) dräyit 487-8; — bē! away! 14%, — 2. prev.: a) off, out, away, forth, esp. with vbs. designating a motion or a change of place or of condition, v. each separate vb.; cf fratom 6 ünód apar raft, avdom bē raft he (the horse) was the first to come there, and the last to go away 49%; HajB:8 (first BL’). In this case be, as giving the vb. its specific sense, is not dropped when other preverbs or the negation are added;
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
3201:. raftan to keep company with, to communicate with 702-8; — apar én zamik ravét he moves on this earth 3333; apar zanišn raft hend they went to slay (him) 4515-16. — hac from 62. 569.809; — 6 to 3726, 385-9 etc. passim ; — pat gehän *hamāi raft hom I roamed the world all about 318-9 (kame would not suit the context; cf 952° s, v. hamäk); — with prev.: andar ~ : ka srav ... 0$ (prep.) mart (+...) andar rajt ēstāt when the report had reached that man (who ...) 4424-26; došar"% ... andar 6 [KN] ravét will move, roam freely in Hell 347-8; — apar ~ : 6 õi ket apar raft hénd they went off to the sooth- sayer 379; 3811-15, 415, ete. — be ~ : fra- tom 6 änöd apar raft, avdom be raft (he was the first to step in there) and the last to step out 496-?-20; 5714-15; pas patvand hac oisan be raft then offspring proceeded from them 941°; very often bē only indicates the aspect: ētēn sart bē raft i-š ... went ahead so vehemently that 3315; bē rav! 6019; adak ēišān bē raft hend 5712; — frac ~ : frac raft Pourusäsp
3988:vartišn [wltšn'] the act of turning: 1. han i avdom ~ the last turn, of the end of the world and the fraškart (q. v.) 4619; ~ 4 axtarün u gartišn 4 spahr the revolu- tion of the fixed stars and the rotation of the sphere 1205-5; ~ u gartišn + muhrak the moving and transposing of the draughtsmen 12015, — 2. pred.: turned, became 41??, — V. vastan.
5698:’b’ryg: apārīk ’p’yd: apayistan ’p’xtr: apäxtar ’bdwm: avdom
6404:awadum, -dim: avdom
```


## [2026-09-04T22:43:21.615Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# map line no -> leaf\nleaf=0\nlineleaf=[]\nfor ln in lines:\n    lineleaf.append(leaf)\n    leaf+=ln.count('\\f')\nfor n in (505,521,571,788,1539):\n    print(n, 'leaf', lineleaf[n-1], 'printed~', lineleaf[n-1]-8)\nEOF",
 "description": "Find Nyberg leaf numbers"
}
```


### [2026-09-04T22:43:24.080Z] TOOL RESULT

```
505 leaf 30 printed~ 22
521 leaf 32 printed~ 24
571 leaf 36 printed~ 28
788 leaf 46 printed~ 38
1539 leaf 88 printed~ 80
```


## [2026-09-04T22:43:33.617Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"apəma\\|apdma\\|apəma-\\|apatəma\\|apatdma\\|apatema\" BRT.txt | head -20; echo \"=== apa- entry ===\"; grep -n \"^apa\\b\\|^apa-\\|^apa \" BRT.txt | head -20",
 "description": "Bartholomae apəma"
}
```


### [2026-09-04T22:43:33.684Z] TOOL RESULT

```
=== apa- entry ===
3484:apa-gaSa-  Ti
3503:apa-gaya-
19869:apa  . .  gSu^la  västrät  aa/fym  'tum  ". .  und von  der  Weide  des  Rinds  den  schlechtesten Walter"  Y.JJ.  4.
```


## [2026-09-04T22:43:39.731Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"der letzte\\|letzte\\b\" BRT.txt | head -20; echo \"=== search apam ===\"; grep -n \"apam\" BRT.txt | head -30",
 "description": "Bartholomae letzte"
}
```


### [2026-09-04T22:43:39.803Z] TOOL RESULT

```
2893:Pü.;  aivahe  kum  (in  Av.-Bucbst)  tahäk.  Das letzte  Wort  der  Pü.  sowie  K.  po  lassen  »uf .  .  vansijluvBOhö  (NP.)  «chliessen.  'von  der Stärke,  Dicke  eines  .  ■  haars';  Tgl.  vatiü.- stttvah:
3650:•  j.,  g.  apama-'',  g.  ap«ma-  Adj.  (fem. "ffiii-)  Adj.  'der  (zeitlich)  letzte',  ntir  von dem,  was  am  Ende  der  Dinge  (des  ersten Lebens)  eintreten  wird  ('jüngst')'':  'ml arihSus    unalsZ {sA.)    Y.J/.6;  43. S\    —
8447:fernste,  letzte:  mryamanmi  fsim..yS  'mo  j^_  ■'  '  unu™
8549:•  j.  ust9ma<  Adj.  'der  äusserstc,  letzte (zeitlich)':  't?me  urvasse  gayehe  Y.  7/.  14, 15,  H.  1. 15.  a)  ASn.  als  Adv.  'zuletzt, am  Ende':  s?raosö  (sd.)  /üJ  am  . .  hyal paoun'Jm  tat  'm^mUt  ". .  wie  am  Anfang so  am  Ende"  Y.  j6.  i,  VT.ff.j'\  1
10098:meist  mit  mantan-  'menschlich'  verbun- den": 'am  F.  21;  —  'yeÄe  marii!tüS  .  . yS  paoiryS  ahuräi  mazääi  manasca  *gulta silsnifsca  yahmat  haca  fr^W3r?sai  näfö airyanqm  dahyunqm  Yt/_J.  87;  V.  2  j.  2, 2Ö.  5;  —  haca  "yJt  mari^nat  ä  saosyantäi Y.  26.  10;  —  'yehylcä  mnra>nö  \.  13. 7.  a)  neben  ^gav-  (III):  tams  gsui  .. 'yehe  Y.öVi'.aa;  Vr.2;.2;  — fravaiayS.. yqmca  gSui yqm^a  'yehe  Yt  13.86.  Vu- deutlich:  _j'ar«/o  "yehe  maraia"  F.  ^e", ')  Vgl.  Yt  IJ.  87:  "OJH.,  der  als  erster  des AhuraM.  Willen  und  Gebole  annahm,  aus  dem er  schnf  die  Familie  der  ariBchcn  Länder,  den Stamm  der  arischen  Länder".  GM.  ist  der  ersle. Saesyant  der  letzte  Mensch,  Y.  26.  10.  Vgl. noch  Bd.  24.  1,  j,  igff.,  31.  1,  10.  7;  s.  Justi NB.   108.
11071:Glieder  sind  verbal:  yBi  ztjvä  (nämL  hitOt) *ar»har3La  bvanticS{sA)\.4^.T.  3)bci allen;  a)  D  im  Ap.;  das  letzte  Mal  steht Uta  statt  cä:  pärsamcä  mädamcä  utä  aniyä dakyiivaf"  Bh.  /.  14.  b)  im  Aw,;  i)  die Glieder  sind  nominal ;  a)  sie  folgen  sich  un- mittelbar: nmänyasca  visyasca  santumasca Y.  if).  18  (s.  dazu  18  aA.);  —  aojasca  v»ty- 'inmca  j^armas^a  lavania  Y.  7/.  8 ;  —  sta- rasca  mäsca  >fe'<i/vi-'(7  YL72,25(s.dagegeni_j. 57);  —  vätftnca  vänmca  tnafy^mca  Jyau- humca  Yt  5.120; — hubprvtlmca  uslaMin- tlmca  vanta.bintTmca  Y.  61. 2  (s.  dagegen  7 ; Sp.  570U.);  —  maziUäsca  vahiitasca  srais- tas^a  asayS  Y.  52.  3;  —  apasca  urvaräsca xadirdsca  Y. A3;  —  asavafom  htnümca bavaniiinla  busyantimla  Yr.lS.i; — vTspayä ..slöis  haihyJica  bavqihyäica  büiyqi^yäica \.6S.i3i  —  nm3nanqmcä  vlsqm^a  satttu- nqmca  dahyunqmca  Y.  Ä  7 ;  —  damayä  anu- matayal'a  aiiuxtayaica  * aim.varstayai^a Y.Ä7;  —  d^aurunqscä  rä^aistiscä  väs- tryqscä  ßuyants  Y.  ig.  3;  Yt  ig.  8;  — ahamca  ratümca  paoirimca  tkaisim  Yt/^J. 152;  —  ha^ra  miiräca  rasnuta  uyraca dämSis  upamana  Yt/_J.  47;  —  vispss^a paiti  vansajls  vTspSsca  paiti  frasparrjJ i'JspSsca  paiti  fravaxsS  Y.  jo.  5 ; — haurva- tasca^  fiö  am)r>täta  gSuica  taSnB  gSusca urunS  ä%rasi-a  aoxtsjiämand  hadisasca  Vr. g.  5;  —  beim  Zahlwort:  navaia  navaittfca navaca  sota  navaca  Aazavra  navasSsca baivqn  Yl;_J.S9.  a)mitTmesis:*«ai/x
13199:Bezug  auf  die  letzte  Abrechnung  gebraucht:
19645:*)  Ursprünglich  das  Jul(WinteTEOnnwend)fest (s.  unten)  iil  es  später  dem  Andenken  tut  die SchafTang  der  Tiere  geweiht.  Der  letzte  (So.) Tag  fällt  auf  den  30.  des  10.  Monats  und  ist der  185.  Tag  nach  dem  Sommcrsonnwendfeit (30.  Joni),  woraus  sicU  für  die  ältere  Zeit  eben der  12.  Dezember,  der  Winters onnwend tag  er- gibt; heutzutage  fällt  er  auf  Anfang  Juli.  S. übrigens  unter  yäirya  und  maüyäiiam-.
19659:*)  Ursprünglich  ein  Frühüngsfest  (s.  unten) ist  es  später  dem  Andenken  an  die  ScbafTuDf; de*  Himmels  geweiht  Der  letzte  Tag  fällt  auf den  15.  des  3.  Monats,  45  Tage  nach  dem Jahresanfang,  d.  i.  in  alter  Zeit  45  Tage  nach dem  S.März,  also  anf  den  31.  April;  heutzalage auf  Anfang  November.  S.  im  Übrigen  unter yäirya-  und  mattyiHain:
19665:tagnndnachtgleiclie,  Sp.  auf  den  i.  Min.  Die Angaben  in  Bd.  35.  3,  6  widersprechen  licb, indem  einerseits  der  letzte  Tag  von  Maiiyöi- hma  als  der  längste  —  und  entsprechend  der von  Maüyäirya  als  der  künette  —  bezeichnet, anderseits  der  leCite  Tig  des  Jahrs  aur  den  Tag des  Frühlingiäquinoktiums  verlegt  irird.  Vgl Bthl.  IF.  5.  261,
21480:•  j-,  g.  yazav-  Adj.  (fem.  yetivl-)  ■>  'der jüngste':  yasui pu%r3  F.  4g;  —  yasüm pu'hnm  'VyX.26;  —  pouruMstaisA.)  yesiv (VS.)  dt^rqm  (sd.)  tardku^rahl  Y 53-  3-         a)    sva,    'der   letzte':   o/   Saca
21481:i5>^f^r  ^paourvim  mOMdä  *yaxBm'^  stsi manaaha  "ich  erkannte  von  dir  im  Sinn, dass  du,  der  erste,  (und  auch)  der  letzte '-^st"  Y.^/.83).
23373:•  j,  vahi§t»iätay-  fem.  Adj.  'die  Worte  i vahism  r/AV enthaltend,  damit  beginnend': •H/ Aaiti/ (sA.y'i  Y.5^Überschr.;  —  'tim häitim  yazamaide  Y.jj.  lo;  —  'tlm  ga%qm (sd.)''  .  ■  yasamaide  Y,  5_J.  lo;  Vr.  2j.  i, 2.9;  —  'tBis  ga'hayi  handäta  yazamaide Y.  5j.  10;  Vr.  /.  ■},  23',  A.  2. 1,  V,  ig.  38, ^y^53-  ä)  ii's  Subst."  'die  mit  vaA" TiVf'/ beginnende  Ga%ä':  aval  vfr3%raymm ,  .  yat  asli  antanca  (sd.)  vohuxsd^rqm •tlm  Vr.  20.  a.  A)  'tdil  (näml  ayan) heisst  der  letzte  der  am  Jahresende  einge- schobenen 5  Schalttage:  pancaca  Aaptäitlm hamaspa%maidayeAe  {si^  'tBis  gähayä  A.
24600:*)  So  nennt  man  den  8.  und  23.  Tag  jeden Monats;  der  Tag  des  SchSpfers  {äa%uiai  heUst und  als  7.  auf  den  Neumonds-  (i.),  bz.  Voll- monds- (lö.)  Ta£  folgt  Auf  die  beiden  Tage falien,  die  Mondphase  in  30  Tagen  gerechnet, das  erste  und  letzte  Viertel,  Vgl.  dazu  Ggr, OK.  319.  —  Pü.  erläutert  das  Wort  mit  jtaBäti /  sitiiar  'dritte  Peatade',  die  nach  GrBd,  auf den  20,  bis  25.  Tag  der  Mondphaie  fallen  soll; s.  DsT.  6tlr.  3.  294,  ZA.  7.   12.
28142:—  >)  Oder  GS.  lu  'm-?;  S  3S6-  —  J>  So  nach der  unlergeschri ebenen  /'Jsini/Iesung  in  K. Der  Pahlaviteit  hat  zrdli,  worin  man  da* letzte  Zeichen  fälschlich  für  'und'  genommen hat.
29255:•  ').,  g.  haptaS-a-  Adj.  'der  siebente':  »üff (nämt^a/m)  Yt/^.a;  r.7,  14- 19.  ^.14.9; —  °^;i«  ajaw^tffftta..  V./.9;  .^24,  5.29', N.  <y2 ;  —  -äa  (statt  NSm.)  N.  702.  a)  ASn. •ä;!«  als  Adv,  'beim  7.  Mal';  *3  Ae  asti /Ha?  . .  -hfm  navaitim  upäzananqm  upä- z3itV.4.\<^■,8.^^.  A)Substneutr.;a)'der siebente  (und  in  der  Reihenfolge  letzte)  Teil der  Erde',  d.  L  das  Karh-ar  iCanira'ka:\
=== search apam ===
2767:(sd.) N.52 ; 53{yio*up5is»mne)  ■".  4) 'Jem. besuchen,  sich  einfinden  bei  — ';  upä  tu  (sd.) nö  ioa  yti  asaonqm  nwsu*i>:^ntö{iVlk)"^ /ravasayd  Ylij.  146.  a)  insbes.  'einen Lehrer  besuchen,  zu  ihm  in  die  Schule gehen':  ivat  nj  *ai^rapaitint  (sd.)  upöi- sät"^  N. /j;  —  ..  *ainim  ai%rapailim (sd.)  upsissi/^'''  a'ia  "i^ritTtn  upsisöil  ai- va'ha  ioirim  upäisi}it"1^.ii.  5>'erfahren, '  erleben' :  upa  aBqm  xiapamm  üvavat  sätüis urva  *  Haiti  yaia  .,  H,  2.a.
3650:•  j.,  g.  apama-'',  g.  ap«ma-  Adj.  (fem. "ffiii-)  Adj.  'der  (zeitlich)  letzte',  ntir  von dem,  was  am  Ende  der  Dinge  (des  ersten Lebens)  eintreten  wird  ('jüngst')'':  'ml arihSus    unalsZ {sA.)    Y.J/.6;  43. S\    —
3655:(sd.)  anftat  'imm  Y.  45. 3, SnperL  aus  a/a;    vgl.  apara-.   —    u.  apamä- Adj.  —    Pü. :  ^atum,  läk  d  an  i  af.  —    ')  » im  gAw.  nur  V.  45.  3.   —    ')   Im  Gegensatz
3684:sa3^3rJ{iA.)  . .  ya  ..  vav}r?SSi  pairlJült ..  yäia  var?^aitg  '/LcTblJ  Y.  25,4;  — ai^qmät  ä  ahtnJ  .  .  vTci>3i  (sd.)  -/)"■■>  Y. j2. 8.  a)  mit  Neg.;  'nicht  hinfort  mehr, länger":  »»3  ^I^ä  *fX  äsbävayal  (sd.)  Y. Jt.i7.  3)  'auch,  gar,  besonders',  das vorherg.  Wort  hervorhebend:  maS^a  .  . pirs^u  'pi  ffi/ajii/Vjy  "die  Wolken,  die  sich gar  weithin  verbreiten"  YLA40;  io.44; —  \daraiy  'piy  "gar  fernhin"  X.7. 2;  D, 6'.a,  4";  —  ai'e  °pi  dai'jyanlS  "'äx£  y^a^ besonders  hinsehend"  Yt/0.45;  45;  — *avat  'pi  ya^a  . .  "soviel  gerade  (,  eben) aIs.."V.ö'.io;22,Äa3,J7.7.  I^Praen. 1)  mit  Akk.  a)  'über  —  hin';  a)  zeitlich: dar>-^3mHt  °pi  zrvätam  Y.  6-1. 3 ;  Yt  i^. aö,  ß)  räumlich:  vTspqmHl  'pi  imqm  sqm Y. 57.33; — liuire fraväitUßA.)  tq%ryqm  °pi xSapamm  Yt  74. 1 3 ;  —  yavat  anu  "pi  *i}iti garayS  visasiar?  vlsptm  aval  °pi..  "so  gross der  Raum  ist,  über  den  hin  sich  die  üerge erstrecken,  über  all  den  Raum  hin  . ." Yt. 7p.8.  b)  'bei':  k?m  ksm  °pi  nmäm "bei  Jedem  im  Haus"  Yt.  5. 102.  2)  mit Lok.  'bei',  zeitlich:  mi^nm ..yahmi  ssire m%%rS.dru}5  'pi  %n<isi  paun'a{sA.)  masyS- kunhs  ". .  bei  dessen  Gericht  . ."  Yt.  lo. 8of?).  3)  mit  Instr.  'nach',  zeitlich: s.  aipi  tä,  aipi  taiS  bes.  III)  Praev. {m\\.kan',  karat-,  gart-,  gam-,  vai-,  varpi- ua.).  [IIBh.4.8:  lies  utämaty^'»; —  Y.
4146:der  Gesammtheit  der  stofflich  Seienden, 'die  Welt,  Menschheil'  (s.  I  la);  yasnyasla vahmyaüa  'nuhe  astvaite  Yt-fS*.  15;  Y.  65. 1%  Yt  y.146,  V.  2.24,  P.J5  (wo  arikeY\ *Vyt  J<?;  —  apam  napiss  tä  äps  .  .  -t3uhe astvaite . .  vl6ax/aiti  Yt.  Ä  34 ;  —  syai)^  na . . yä  'ühus  astvä  vfifzyäü  V.  75.  i;  Yt.  y. 12;  —  avi  °hüm  astvantpta  a-fpm  (sd.) *e}mS  jaiihintuY.  2.22*;  —  kascit  'ufiSus astfats  "ein  jeglicher  Mensch"  F.  2()", V.Äioo;  7.50,  70.19,  'Äaa.  P.y,  .<3;  — anys  kascit  "nhSu^  ash'atö  N.  63;  — yeiftyö  .  .  vlsp^mili  -uuÄe''  astvaite  Yt  10. 5.  aa)  mit  vispa-  Adj.  'die  gesammte
4905:•  j.  a-yaz9mna-  Adj.  'nicht  betend':  y^ saSte  haurvqm  tarüsca  xsapamm  °«5| ". .  ohne  zu'beten"  V.JÄs;—  mitAkk. 'zu  -':  yüi  °na  am>Ss  sp>nl!"ä\t  nicht  zu den  ASp.  beten"  Vyt  12.
5213:agaqm   vä   'vi  xiapamm  duyi  vä  .  .  Yt.
5876:•  j.  aspö.k^hrp-  i)  £  'Rossgestalt' 1  bäia vairlm  Hcaraiti  'Pqm  (AS.?)"'  asaonim  Vt. Ä8'*.  2)  Adj.  'rossgestaltig*:  'fam (ASf.)  ■>  ap?m  Yt.  2. 1 7;  —  apam  . .  *°pai»i' (GPf.)  N.47.
5880:•  j.  asp5.stao/ah-  Adj.  (fem.  °ye/tJ-) 'starker,  umfangreicher  als  ein  Pferd, Pferdeleib"':  xä  'yehls  apam  \'t.8.$,A2; —  srira  vü  ar»)im  b.lzava  aurusa  "ythTs'^
6505:•  j.  as.dSnav-  Adj.  'mit  starken,  grossen  •  P-  aSna-  m.  'Marschiren',  mit  astty  'er (Samen-)Körnem':  us  apam  aoavS  .  .  befindet  sich  auf  dem  Marsch  nach  — ' jasänti  -nunqmca  yavanq'm  kasuJätm-  («^V  »"'*  Akk.):  *adaiiy  adam  ^naiy^^ natnca  västra'nam  "die  wässerbäche  wer-  •'^'"»  "^'y  ''uv'^jam  pasäv<^  kacämi/' den.,  hervorbrechen  hin  zum  Getreide  atars<^^y^  uz-aßyä  "damals  war  ich mit  den  grossen  und  zum  Gras  mit  den  ^  d^™  Marsch  nach  Susa;  drauf  bc- kleinen  Körnern"  YtÄig".  kamen  die  Suser  Furcht  vor  mir"  Bh.2.4.
7235:ahüm  fraparayeni  .  .  3  vakistat  atfhaot  a . .  as3t  a  . .  raocSby3  '^.ig.6. '  b)  zeit- lich :  fravasayS  . .  ya  kaca  gayät  marp^nat 3  saosyaHtät  vfrsiiraynat  Y.  s6. 10;  — pu^rS . .  apara.itCbintS  *3  d3tai'*^  vii3taot (sd.)  Yl/^.  II,  22,  28; —  apam  ..fratiS .. kaca  hü  vaxi'at  ä  ^An'^'  frasml!.datsit pairisafaiH  '^.48;  Yt5.9r,  V.  y.i;  — a  tnaiiyat  xlapat  N.  50, 46;  —  a  darr/at :^3Miry3l  (sd.)  Y.O'0.6;  —  vTsp^m  3 ahmai  sbes.  c)    'in,    bei',   räumlich:
7280:heisst  der  10.  Monatstag:  apqm  vanu/il- riqm  mazdd'jätanqm  S./.io;  vgl2.io,  Y. ;6'.  4.  [Vt  7J.  I :   lies  apamca,  s.  apü-A
7609:•  j,  »-var«zyant-  Adj.  i)  mit  Akk,  'nicht wirkend,  begehend':  'zinbyd^"^  pascaila araiwya  syaoina  V.J.  40.  2)  ohne Obj.  'sich  nicht  übend  (tn  den  Werken der  Religion)';  yö  saite  haurvqm  tarasca xsapamm  ayazsmns  . .  'zyö  ".  ,  ohne  zu beten  . .  ohne  sich  (im  Guten)  zu  üben" V./&S-
8751:Lebenskraft'^':  hyat  astvant»m  (sd.)  dada 'tatum  y.j/.  ij;  —  tal  ii  .  .  vairim  ast- rwV?  (sd.)  'tänäi''''  data  Y.^j.,^.  14;  —  at rätqm  zara'^uÜrö  tanvascti  x^ahya  'tattpm dadaiti  paurvatätpm\.33.i^;  —  f^ra  vS rahl  .  .  tanvasclt  c^'ahyS  'tatum  V.  //.  18; /_9.4;  — darsyö.xia'irpm  xsa'^raAe  dury/ö.- jUim  'tilnahe  A.  1.8]  Y.  17. 19;  —  m-^irpswa slün'i  gayehe  mprpzu^a (sd.)  xa  'tänahe  Yt. JO.  7 1 ;  —  avai  he  astt  masyö  ar^i^pm  yat \  'tatum  bttnjayüt  (sd.)  V.  7.  7 1 ;  —  ava \  apamm  (sd.)  gayehe  *frasatu>m  'tanahe  Yt.
9432:(GPf.)  apam  *avi.frädavaiU  (sd)  V.5.  24;       ■>  Vgl.  iBed.  p.  pou-Aoc,  ai.  pari-cari-  m.;
10038:tra  ayu,  sd.)  jaypiyqm  agvqm  va  avi x^apamm  ". .  wUrde  ich  hinzukommen  aui ^ine  Nacht  . ."  Yt.  Ä.  11.
10066:aoi  karh'qn  Y.  6^.  5;  —  tha  apam  vl- Jasaiti  . .  dalna  . .  vlspäii  avt  karh'an  Yt. y-94; —  kiii:a  tJiig  a  vXpmyat  Srmaitis yaHbyB  .  .  "ob  sich  wohl  die  Fromm- ergebenheit zu  denen  hin  ausbreiten  wird, welchen.."  Y.  44.  11.  Wertlos:  aÄmai
10536:•  j.  xan-  f.  'Quelle,  Brunnen':  xä  (NP.) aspS-stdoyehl^  apam  Vt.  Ä  5 ,  42;  —  apamui xä  (AP.)  Y..,^2.'i;  V.y.si;  —  xa  'paiti afrajyamna  Yt.  ;_J.  14^;  —  vupa  äp5  x'i paiti  '^raoid.siätascü  (sd.)  Y.  Ji.  9 ;  —  »nzöis (sd.)  xh  Ytj^ag;  —  m^rtzuca  (sd.)  xa u^tünahe  Yl  /0. 7 1 ;  —  frä  tl  hazat^rsin xqm  (GP.)  .  .  gaoiaiDin  (sd.)  avi  hanta- una'^.21.'};  —  fiaoma..  hai'hlmca  asahe xa  (NS.)  ahi  "o  H.  .  .  und  wahrlich  des
10612:fromme  Weisheit',  d.  i.  Inbegriff  des  reli- giösen,   in    den   heiligen   Büchern    aufge- zeichneten Wissens:  yd  haurvqm  farasca xsapamm  'tum  p^risät  asavamm  "wer  .  . die    fromme  Weisheit   ausforscht  V,  jA'.  6; Vyt.^/;  —  *naire  aiaone  .  .  aiwica  *  hatte (sd.,Sp.  277)*i''ti/r7«iJ/V'i2  paitica  *p»r>smanai 'tum  alavamm  a.84;  ii,  j2.        Undeut- lich ^iffii  asfa  (sd.)  a/a  'iwa  V. /j.39. KompA.,  E. :   Ableit.   —   ai,  irälav-  m-,  np. xiiaJ,  arm.  LW.ira/.  —  Pö. :  xrai,  SQ. :  buadhih \ s.  noch  No.  5.  —  i|  Vgl.  iBed.  der  ar.  Wörler Bergaign'E,  Eel.  v^d.  .?.  313,   Gdn.  sYt  95, VSt.  I.  267-  —  ')  S.  dam  Bthl.  IF.  7.  223. —  3)  VII.  ist  auf  diese  Stelle  ^.46.  3  (lansyan- Iqni  xratavS)  von  Einfluss   gewesen;    s.  noch No.  6,    —    4)  Vgl.  No.  3,  6.    —    J)  Pü.:  ha sralik,  erl. ;  kian  sral  i  lai  i  näeak.  —  *)  Wie No.  3.
11883:•  j.  tadLäp-  i)  'ßiessendes  Wasser":  yat alte  (sd.)  ysi  mazdayasna  ..  'apaya  (LS.)" nasaum  frajasqrt  V.<?,  26.  i)  Adj.  (auch fem.)  'mit  fiiessendem  Wasser':  vat^lm (sd.)  'apam  (A.SQ'i  V.  14.12.
12052:äjAtärti  . .  f  aisraAe  mainySus  ,  .  zae/a Yt.iO.ii8.  h)  leiHich: yS  sa^e  Aaurvam P  xlapamm  ".  ■  den  ganzen  Tag  über" V.jÄs,  6;  VyL4/'.  3)  'seitwärts  vor-
12424:oAurischta  Religion :  kahmät  paoiryS  mal-  \ yänqm  , ,  frada^ayS  'nqm  ,  .1  . .  yimäi .  .  fradaisalm  °nqm  .  .  äai  hi  mraom  . . vUanha  ml  minlff  b^ntala  (sd)  "nayäi (als  Gen.)  äat  . .  pailyaoxta  yimS  .  .  nSit dato  ahmt  . ,  tnirstl!  b3r?tala  'nayäi  V. 2.1  ff.;  Ytn.  14;  —  vXltäspaht.  .yS  batuUa upastaca  vTsata  .  .  •nayä  Yt  13.  99;  — ya%a  axsm  Asüyene .  .  zara%uänm  anu- matSe  'nayäi  anuxtie  'nay3i  anu.värltSe •nayäi  Yt.  j,  18;  Y.t?.  7;  —  hutaosqm  .  . yä  rrn  °nam . .  zraiia  (sd.)  dät  apica  aotaf Yt  ().26;'Vyt.  Jo(?);  —  ks  .  .  'nam  .  . vJbarat  aitaisva  vanfsva  ySyimö  ktnrtaoi^ .  .  vTs  iarsipia  V.  2. 42 ;  —  satö  .  .  zara- huiirS  .  .  ita  apam  vTjasaiH  .  .  °na  .  . vlspais  avi  karsvqn  Yt  jj.  94; —  mi^nm . .  yahmi  vyane  (sd.)  °nayäi  (als  Gen.) srirayai  p}r>^u.fräkaysi  . .  Yt  10.  64;  — sraoi^m  .  .  yB  damsJisS  *°nayä  Y. 57.23;
14472:•  j.  d-raotö.stak-  Adj.  (auch  fem.)  'in Flüssen  laufend,  fliessend':  yeähä  paiti 'stacö  äpö  taHnti  Yt.y.  lo;  —  %risum apam  'siUcam ''  .  .  pairistaydH  V.  18.  63.
15262:j.  pan^-sant- *>  fem.  Zw.  'fünfzig': paitica  hl  anya  dva  vä  nara  anhiti  panca vü  'sahm  (als  Nom.)''  va  V.  5.  27;  — aivam  va  avi  x^apamm  duyS  pJ  'satim (als'Akk.)')  va  YtÄii.  a)  mit  Gen.: ^  pasca  'satitn  sar^qm  V.  7,  48;  —  'sat»m \iitr?.saokanqm  V.S.gx;  4, 19',  6'.  13',  12.9, F. /o.  a)  adjekt  gebraucht:  ha^ra.. ^yazataiibyS  . .  'satblsca  sataista  . .  Vr.  Ä  i, I  KompA. ;  Ableit  —  ai.  fonoiiäl-  f.,  np. /on- I  jäh  i).  —  Pü.  i  SO.  —  »  Mit  fl  lu  F.  und  Vr. —  ')  Vgl.  lu  %titanl:  —  3)  S  ^ro  udW.
15719:•  j.  paurva-"',  paourva-'',  pourva-'', p.  paruva- Adj.  (fem.  'va-)  'prior';  I)  dem Ort  nach,  r)  'der  vordere';  banlhBm  At vay&an?m  (sd.)  'rum'^  paiti.hincBa  V.S, 40;  41;  —  yaf  nä  'rva  (AD.)^  ß-aida (sÄ)  jrabdB.dräje  /rama&aiti  V.  i8.  40; — fra  mi  gahaa  tazayqn  nisbinla  (sd.)  . . 'rvaäbya*^  {riinA.  pataäbya)  V.  6".  37;  — aparaya  ..*'ruya*'>^  (LS.)  paüi  *mastrr]- naya  F.  9c;  —  *yatB  (sd.)  °rvatibya^'>  ya%a rdhaeää  V.ij.  45;  48.  a)  ISn.  paourva undASf.  paurvqn''^  als  Adv,  'vorn,  voraus'; mä  apama  *paourvitvaySit  (d.  L  'rva-\- avay*)    "wir    wollen    (ihm)    nicht    nach*
17911:•  j.  fra-sätui-  n.  'ZerstÖruDg,  Vernichtung* : ava  apamm  (sd.)  gayehe  *°ram  '^  ultänahe Yt  ig.  44.
18082:*kaia  apam  *vaautanam  *'tii'^  frajasaiä  ■  A&dk  vermöge  deiner  Henscbgewalt  durch
18541:•  ).,  g.,  p.  naplt-:ffa//-  m.,  j.  naptar-: nafsir-  m.",  j.  naptl-  f.  'Enkel;  Enkelin': '  adam  d3ray^v(^ui . .  vistäspahya  puh^e^ arSätnakyä  '/J(NS.)'*  Eh.  j.  i;  —  'pS (NS.)"  ..  ■■//("  (NSf.)  i/a  V./2.11;  10;  — nyaka  haca  'ptöisSs,  (^\%y^  nyske  haca  'pti (statt  AblSf.)  V.  J2. 1 1 ;  —  hyai  us  alä napiyaisii  na/i'uCLP.yVä ..uzp//  (Sp.4gSm.)  ' fryänakya  aojyaiiü  '^.46.12.  a)  mit GP.  apam''  'Enkel  derWasser',  Name  einer Gottheit**;  a  dim  (näml.  3^ar)nö)  Hahra kangturvayat  apum  'ph  (NS.)  aun'at.aspö Yt.  rp.  s  1 ;  5 '".  '.7-  95^';  —  «/>?'»  >'»  (NS.) t&  ups  ,  .  aiiuhe  .  .  vi.baxsaiti  Yt  8.  34; —  b^ntantfm  ahuntn  xsa^rlm  xSaltitn apqm  'pättm  aurvat.asp?m  .  .  yB  upäpB yazatS  Yt  ig.  51 ;  Y.  2,  5;  —  apqm  'ptär?m yasamaide  nairJm  sanh^m  Y.  7/.  23;  — b»->sat3  ahurake  'fiorS  aPqm  apasca  maida- la/aya  Y.  r.  5;  —  b^ryza  a/iura  xsa^rya apqm  V»?(VS.)Y.6'5.ia.  _  a)Nameeiner jener  Gottheit  geweihten  Örtlichkeit*'  (oder eines  Husses,  einer  Quelle,  eines  Berges): tarn  (näml.  andriin)  yaznäa  . .  sSyuidrSis pu%ra  upa  b3r?zant?m  ahur>m  xsairim xsaWm  apqm  'paism  Ylj.  73.  [na/jonm Y. ij.ii:  s.  x/alirB.napiar-.\
19421:—  a%a  ml  zae'kra  lyänte  ..  ti.6S;  — äaj  mg  tum  . .  Ausk>m  pflum  ra^aya  Yt 5.77;  V.2.4^,  Y.io,  iz;  —  aal  ml  afm paityaexta  Y.g.  2,  V.  2.  3;  —  nüit  tng  apam ährava . .  daiähava  äir3J{sd.)  Y.ff.  24;  — ma  ml  jamyäi  akäi  aSs  Y.  59. 31 ;  Yt.5. 92,93,  V. /().  6;  —  US  ml  pita  kaomäi dra&ns  frSrsnaot  Y,  //,  4 ;  V,  iÄ  i  g ;  —  upa ml  srayamtha  vasahe  Yt  iT-2\;  — pairi ml  tümHt  daya  . .  Y.ii.io;  Ytl.S,  12.1, F.  ^  d,  Vd.  20;  —  jasa  ml  avatthe  Y.  ■]2. 9 ;  Ny.  /.  1 8 ;  —  däyä  m  l  atarl. .  afä'hrsm Y.ö'2. 4;  GS.$';  —  dazäi  mi . .  yai  .. Ytp.  4;  V,  2.  3;  —  Aaema  \dazdi  ml  .  . Y.  iO.  9';  —  üaita  ml yaozdäilTm  V.  & roo;  —  dalva  ml.,  aostm  kqmp>nstnie V./p.3;  —  ulia  ml  .  .  VtÄag;  23;  — vaxhm  miasqsa/..  V./5.15;  Yt77.ao, Az.i,  Vyti; —  havatahum  ml  buyalaY. 7/,  11;  —  mo!u  ml  Java  avaoke  \nur3m ml  bara  upasiqm  Ytj.Ös.  zu  1  a): As  ba  ml  aetaäqm  arinam  paotryl  "V .  18. 34;  —  yasca  ml  .  .  imä  namSnTs  . .  Yt '■  16;  3-  9,  "i  P-  '»;  —  ^«"S'  »r  ml  nsit da&Ti  upasiqm  . .  Yty.  la;  —  mä  &' ml  änhqm  zao%ranqm  frattuharät . .  Yt 10.  \22\  17.54;  —  3  tu  ml  aOayä  zatf- ^rayä  frattAarSil  YL5.  91.  zu  3}: ydha  yaf  ml  sahayeht  H.a.  11;  —  avat äyaphm  dazdi  ml  Yt  5.  iS,  15.  5,  17.2$;
21264:Undeutlich:  y  v°  ya^a  *U£ayarvm  y (v)  ya^a  xiapamn  N.  47-  [V-A*.  75  z.SL: streiche  vä;  s.  Sp.  41a  m.]  yat  vä  mit yat  als  Konjn.  s,  unter  '^a/.
```


## [2026-09-04T22:43:54.216Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT had- / ā prefix ===\"; grep -n \"^had-\\|^hàd\\|^ā prep\\|^ā- \\|^à prep\\|niyaSādaya\\|nišādaya\" KNT.txt | head -20; echo \"=== KNT gaud ===\"; grep -n \"apagaud\\|apa-gaud\\|gaud-\" KNT.txt | head -10; echo \"=== KNT ardha / apa-ardha ===\"; grep -n \"arda-\\|ardha\" KNT.txt | head -10",
 "description": "Kent had-, ā-, gaud-"
}
```


### [2026-09-04T22:43:54.293Z] TOOL RESULT

```
=== KNT had- / ā prefix ===
=== KNT gaud ===
1183:in adánd, vardana-; from plE gh in gaud-, Bar- diya; from pIE ĝ or gh in yaud-. For materials
2539:II. Thematic stems have subjunctives with the long thematie vowel throughout, Ist sg. and 181 and 3d pl. o, other forms é; 2d and 3d sg. and mid. as in Skt. bhár-àsi -àt -àse -äte : OP zšnāsāhy, Gahy (for *6aháhy), apa-gaudayàhy, \drau\jiyahy, pati-parsühy, pari-barühy (and -Gh*-d13), vainahy; ni-rasütty, xsndsdtiy, pati~parsatiy, bavatiy, vaind- tty; maniyahaty (for variant spellings, see Lex. s.v. ‘man-); maniydtaiy, gaubdtaty, 6adayátaty, yadataiy, vainātaiy. 3d pl. act. as in Skt. -dnis: OP vi-naéaya*tty (restored form).
2549:$224. Тнк INiuNCTIVE FORMATIONS are merely secondary indicative forms lacking the augment; the following forms have been found in OP: Ist sg. tarsam; 2d sg. stabava* apa-gaudaya* ava-rada*; 3d sg. fadaya'. See also $237.
2566:І. The primary ending -si was attached directly to the present stem, whether thematic or non- thematie, but happens to oceur in OP only in sub- junetive forms: pali-parsühy (on -hy, $87), Skt. prechasi; pari-barühy and -barüh*-di& ($136), vi- kanühy and -kanáh-dif, kunavahy, xindsdhy, à- tínavühy, vainahy, apa-gaudayahy, Idrau|jtyahy; 6ühy for *даћаћу ($131); ahy for short-vowel sub- junctive (8222.1) *ahahy = Skt. dsast.
2567:II. The secondary ending -s is seen in Skt. ábharas, Gk. édepes; in OP it happens to occur only in injunctive ava-rada, apa-gaudaya, slabava, and in opt. [biylà, in which it is not written be- cause it is final after a (§36).
2924:mand or a prayer, once a future statement (DPe 22): apagaudayahy DB 4.55; 6ahy DB 4.55, 58; vaindhy DB 4.78, 77; vikanàhy DB 4.73; wikanàle-di$ DB 4.77; pattbarah*-dis DB 4.74; patibarühy DB 4.78; maniyáhaty DB 4.89, DPe 20, DNa 38, XPh 47; ahatty DPe 22.
2946:$281. Tug Insunctive Моор, which is a sec- ondary indicative form lacking the augment, has in OP only the use in a negative prohibition, with má: in the first person, iarsam DPe 21; in the second person, apagaudaya DB 4.54, avarada and stabava DNa 60; in the third person, &adaya DNa 58, DNb 58.
3849:55 hadugàm : naiy : apagaudaydhy : kürahy& :8àhy : Auramazdà : fuvām :
3851:57 :08ty : Darayavaus : zXiyatiya : yadiy : imam : hadugüm : apagaudaya
3896:WB, from Wb.'s reading of Rl.s squeezes, add the fol- lowing, also in roman, which were not visible to KT, nor to RI.: ! абаһа : adam; ** draujana ; 5 apagaudayihy; " miyapaiBam : imaivd; ^ ahatiy; 78 iaumá : ahatiy : naiydis; 9 алаа; ** Vàyaspàrahya; % puça : Pārsa : Gaubarusa; * puça : Рагва : Vidarna; 9 g&bignahy& : puça; 95 Bagabuzsa; * Ardumanis : nàma : Vahaukahyá : puça; 9? kå : z5agafiya.
=== KNT ardha / apa-ardha ===
1767:Skudra-, Sparda-, Zazüna-, Züzahya-, Zra*ka-,
1792:Ш. Forming ethnics: Akaufac-iya- to * Akau- faka-; Aéur-iya- to Aéurd-; Armin-iya- to Ar- mina-; Asagart-iya- to Asagarta-; U(v)j-iya- to 0(0)ја-; Uvürazmiya-; Küfiya- to Küša-; Ga"dara-ya- (possibly error for -riya-) to Ga"dara-; Gatagu-iya- (error for -uviya- or -udaya- or -udiya- ?) to 8alagu-; Pulü-ya-; Bäbiruv-tya-; Mac-iya- to Maka-; Spard-iya- to Sparda-; Haxámanis- iya-; Harawati-ya-; Hi"du-ya (error for Hi"duv- iya- ?).
1805:Expressing place: apa-dd-na-, daiva-di-na-, à- yada-na-, fem. us-tasa-nd-, d-vaha-na-, std-na-, varda-na-.
1899:arda-stána- ‘place of light’; datva-dána- ‘holder of demons’.
5068:ardata- sb. ‘silver’: Av. arazata-, Skt. rajatá-, cf. Gk. &pyvpos, Lt. argentum. (S30, §88, $145); Yezdi ait ‘silver’ has Iran. ar-, not r- (Ву. BSLP 30.1.60, Origines 12). See also ardastdna-. arda- tam nsn. DSf 40.
5069:ardastāna- sb. ‘window-frame, window cor- nice’: arda- ‘light’ as in OP ardata- ‘silver’, Skt. rajatd- ‘white’, rjrá- ‘red’, Gk. àpyós ‘shining’ + stāna- ‘place’ (831, §160.Ib; Foy, KZ 35.48; hardly as with Bthl. AiW 193, or Hz. Ар! 74-6); ‘light- place’. ardasténa nsm. DPc.
```


## [2026-09-04T22:44:06.963Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"‘sit’\\|'sit'\\|niyaSādayam\\|niyaśādayam\\|nisadayam\" KNT.txt | head -20; echo \"=== hadis ===\"; grep -n \"^hadis\\|^had-\\|hadis-\" KNT.txt | head",
 "description": "Kent had- sit"
}
```


### [2026-09-04T22:44:07.028Z] TOOL RESULT

```
1066:pIE *sed- ‘sit’, OP had-iš ‘seat, abode’, Gk.
2500:pIE *sed- ‘sit’: pAr. *sddaza- ‘seat’ in Skt. sdddyatt;
5123:ašnaiy adv. ‘near’, lsn. of ašna- ‘near’ (Hz. Ap] 98-9), Av. dsna- ‘near’, in loc. dsnaé-ca, asne ‘near’, abl. asna ‘from near’; from pAr. root end- ing in $ or 2 (pIE Ё or ў: Skt. aánóti ‘attains’ and djatt ‘drives’ hardly suit); not *à-zd-na-, pte. to à + *had- ‘herangehen’ (Bthl. AiW 1755; but *had-, which always has prefix d, is only a semantic vari- ation of thad- ‘sit’), cf. Skt. dsanna- as adj. ‘near’ (Bthl. AW 220). Possibly from plE *afijh- ‘choke, throttle’, cf. Lt. атаб, Gk. &yxw, sb. Lt. angor, Av. azah-, Skt. qhas-: *afijh- + pte. -no- (806, §147.1, $191.11I, $243); for semantics, cf. Gk. &yx« adv. ‘near’ (JAOS 62.276-7). Not ‘on the march’, to pAr. root *aé-, Skt. djatt, Lt. agit (Bthl. А 264); nor ‘m friendship’ on the basis of the Elam. kanna ети git (WB; KT); nor ‘at peace’, cf. Av. dxsitd ‘peace’, dx Sta- ‘peaceful’ (Ву. BSLP 31.2.67-9). Elam. kan- recurs as the translation of dausid ‘friend’, but this meaning eliminates only ‘on the march’, since ‘friendship’, ‘peace’, and ‘nearness’ are related ideas. asnaty DB 2.11f; [aSnajiy DB 5.23.
5701:Fraéda- sb. ‘Frada’, a Margian rebel: Elam. pir-ra-da, АКК. pa-ra-da-’ ; perhaps thematic noun- stem (§141) to fra- + *dà-, with vriddhi ($126), cf. Av. früd- ‘to further, increase’ (ТИМ. AiW 1012), but more probably hypocoristie to a com- pound name ($164.П1; Bthl. AiW 1018) of which the prior part was the participial stem to the same compound verb (§162), ef. Av. adj. fradat.qaéa- ‘prospering the household’, sb. frddaj.fsav- ‘Pro- moter of flocks’ (name of a divinity; Bthl. AiW 1013-4). Not with Sen 52 (fra- + OP *ad- ‘drive’, Av. azaiti, Skt. djati, Lt. agit), nor with Justi, INB 101 (fra- + had- ‘sit’, with loss of intervocalic -h-). Fraéda nsm. DB 3.12; 4.23; ОВ] 1.
=== hadis ===
```


## [2026-09-04T22:44:14.786Z] TOOL CALL #19: Bash

```json
{
 "command": "ls data/ ; ls data/extracted | head; ls tools/ | head -40; ls *.pdf 2>/dev/null; find . -maxdepth 3 -name \"*.pdf\" | head",
 "description": "Look for source PDF"
}
```


### [2026-09-04T22:44:14.870Z] TOOL RESULT

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
EtymologicalDictionary-persian-english.pdf
./EtymologicalDictionary-persian-english.pdf
```


## [2026-09-04T22:44:20.318Z] TOOL CALL #20: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/img && (pdftoppm -f 59 -l 59 -r 200 -png EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/img/p59 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/img/)",
 "description": "Render page 59"
}
```


### [2026-09-04T22:44:22.703Z] TOOL RESULT

```
total 300
drwxrwxr-x  2 sfmqrb sfmqrb  4096 Sep  4 18:44 .
drwx------ 15 sfmqrb sfmqrb  4096 Sep  4 18:43 ..
-rw-rw-r--  1 sfmqrb sfmqrb  4797 Sep  4 15:30 crop1-047.png
-rw-rw-r--  1 sfmqrb sfmqrb  2799 Sep  4 15:30 crop2-047.png
-rw-rw-r--  1 sfmqrb sfmqrb 97385 Sep  4 15:30 p47-047.png
-rw-rw-r--  1 sfmqrb sfmqrb 86113 Sep  4 15:59 p56-056.png
-rw-rw-r--  1 sfmqrb sfmqrb 96510 Sep  4 18:44 p59-059.png
```


## [2026-09-04T22:44:25.201Z] TOOL CALL #21: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/img/p59-059.png"
}
```


### [2026-09-04T22:44:25.723Z] TOOL RESULT

```

```


## [2026-09-04T22:44:25.721Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-04T22:44:36.212Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 22 (p.1) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==23' HRN.txt | head -60",
 "description": "Horn p.1"
}
```


### [2026-09-04T22:44:37.826Z] TOOL RESULT

```
=== HRN leaf 22 (p.1) ===
Ä.
1. ä. 1) Praefix, z. B. in ämeden^ ardi/is.
ap. aw. phlv. ä; ai. d,
2) Praeposition , z. B. in her ä her, gird ä gird,
aw. ai. ä,
/2^' ab, ätv *Wasser ; vergl. slm]ab (*Quecksilber, wortl.
'Silberwasser' d. i. flüssiges Silber), i^'^i^M Jer. 41, 8
(Etymologie Nüldeke's bei de Goeje, Bibliotheea geo-
— • mm
graphorum arabicorum, IV, 240), DN*:?!*! Is. 2, 9, 2^'ii^^^
Is. 36, 12, 2X^^D Jer. 31, 12 u. a. m.
ap. öp- 'Wasser ^); aw. äp-; phlv. fJp (päz. äw); ai. äp-,
kurd. äw; afy. öba (fem.); bei. ap, n. äf (12); wa;^.
ywpÄ:, ydpak, minj. ydoya; yidg. t/ow?;\
3. ä& *Glanz , (Sahn. I S. 14 Vers 7), vergl. ab[rö, ah[tah,
äb[mendy Röd]äbe, Suhr]ab^ Mihr\äb^ Ardä VTr\af, af[täb,
phlv. üb] skr. äbha- *Glanz'-).
afy. bei. LW. ab, abrü; kurd. LW. äwrü.
*) So lautet das Thema nach Bartholomae BB. 14, 244.
*) Im Arabischen bedeutet mäun auch zugleich ^Wasser' und
*Glanz', worauf mich Herr Dr. Schwally aufmerksam macht. Etwa
in Anlehnung an das Persische? Die Zusammenstellung von np. ab
und skr. abhä- ist keineswegs sicher; von der Bedeutung ^glitzernder)
Wasserspieger könnte man sehr leicht zu 'Glanz* kommen.
U o r n , GrundrisB d. neup. Etyiuolog-io. 1
```


## [2026-09-04T22:45:04.837Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN apadana ===\"; grep -n \"^apadana\\|apadana\\|Apadana\" KLN_1966.txt KLN_1971.txt | head -10; echo \"=== KLN afreet/ifrit ===\"; grep -n \"^afreet\\|afreet\\|afrit\\|ifrit\" KLN_1966.txt KLN_1971.txt | head -10; echo \"=== KLN ab- prefix ===\"; grep -n \"^ab-, \" KLN_1966.txt | head -5",
 "description": "Klein apadana, afreet"
}
```


### [2026-09-04T22:45:04.951Z] TOOL RESULT

```
=== KLN apadana ===
=== KLN afreet/ifrit ===
KLN_1971.txt:9020:afreet, n., an evil demon or jinni. — Translitera- 
KLN_1971.txt:9022:‘afrit) ; name of an evil demon or monstrous 
KLN_1971.txt:171623:MDu. peert, paert, Du. paard, OHG. pfarifrit, 
KLN_1966.txt:1891:afraid,  adj.  —  Orig.  pp.  of  affray,  ‘to  frighten’, afreet,  n.,  an  evil  demon  or  jinni. —  Translitera¬ tion  of  Arab.  ‘ ifrit  (in  vulgar  pronunciation ‘ afrft) ;  name  of  an  evil  demon  or  monstrous giant  in  Mohammedan  mythology, afresh,  adv.  —  Formed  fr.  a-,  ‘on’,  and  fresh. African,  adj.  and  n.  —  L.  Africanus,  fr.  Africa, fr.  Afer,  ‘African’.
KLN_1966.txt:27004:palfrey,  n.,  saddle  horse  (archaic).  —  ME.,  fr. OF.  palefrei  (F.  palefroi),  fr.  ML.  palafredus, dissimilated  fr.  Late  L.  paraveredus,  generally supposed  to  be  a  hybrid  coined  fr.  Gk.  xapa (see  para-,  ‘beside’)  and  Late  L.  veredus,  ‘cour¬ ier’s  horse’,  which  is  usually  derived  from  Cel¬ tic  *  voredos ;  cp.  W.  gorwydd,  ‘horse’,  OIr.  ria- daim,  ‘I  ride’,  and  see  ride.  It  is  more  probable, however,  that  Late  L.  veredus  is  borrowed  fr. Heb.  peredh,  pheredh,  ‘mule’  (through  the  me¬ dium  of  Arab.-Pers.  bar  id,  ‘courier’).  OS.  perid, MDu.  peert,  paert,  Du.  paard,  OHG.  pfarifrit, pferfrit  (MHG  .pharvrit,phart,  G.  Pferd),  ‘horse’, are  borrowed  fr.  ML  .paraveredus.
=== KLN ab- prefix ===
```


## [2026-09-04T22:45:11.460Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 95 96 97; do echo \"=== leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((n+1)) KLN_1966.txt | head -8; done",
 "description": "Klein p.168 area"
}
```


### [2026-09-04T22:45:17.965Z] TOOL RESULT

```
=== leaf 95 ===
.  bed,  Swed.  bddd,  MLG.,  MDu. bedde,  Du.  bed,  OHG.  betti,  MHG.  bette,  bet, G.  Belt,  Goth,  badi,  ‘bed’,  prop,  ‘a  couch  dug into  the  ground’,  fr.  I.-E.  base  *bhedh,  *bhod-, ‘to  dig,  pierce’,  whence  also  Hitt,  beda-,  ‘to  pier¬ ce,  prick’,  Gk.  p6fhjpo<;,  ‘pit’,  L.  fodere,  ‘to  dig’, fossa,  ‘ditch’,  Lith.  badau,  badyti,  ‘to  pierce, prick’,  bedu,  bisti,  ‘to  dig’,  Lett,  badu,  badit,  ‘to pierce,  prick’,  Lith.  bedre,  Lett.  bpdu,  best,  ‘to dig’,  bedre,  ‘pit’,  OPruss.  boadis,  ‘prick’,  OSlav. bodp,  bosti,  ‘to  prick’,  bodli,  ‘thorn’,  W.  bedd, Co.  bedh,  Bret,  bez,  ‘grave’.  G.  Beet,  ‘garden- bed’,  is  a  variant  of  Bett,  ‘bed’.  Cp.  bothrium, fosse,  fossil.
bed,  tr.  v.  —  ME.  beddien,  bedden,  fr.  OE.  beddian, ‘to  place  in  a  bed,  to  bed’,  fr.  bedd,  ‘bed’.  See bed,  n.
Derivatives:  bedd-ed,  adj.  bedd-er,  n. bedding,  n.  —  OE.,  fr.  bedd.  See  bed,  n.,  and  subst. suff.  -ing.
bedeck,  tr.  v.  —  Formed  fr.  be-  and  deck,  v. bedeguar,  bedegar,  n.,  a  mossy  growth  on  rose¬ bushes.  —  F.  bedeguar,  bedegar,  fr.  Pers.  bada- ward,  lit.  ‘wind  rose’,  fr.  bad,  ‘wind’,  and  ward, ‘rose’.  The  first  element  is  rel.  to  Avestic  vata-, ‘wind’,  vaiti,  ‘blows’,  OI.  vAtah,  ‘wind’,  vditi, ‘blows’;  see  wind,  n.  For  the  second  element see  rose.
bedel,  bedell,  n.  —  Variants  of  beadle, bedevil,  tr.  v.  —  Formed  fr.  be-  and  deviL
bedew,  tr.  v.  —  Formed  fr.  be-  and  dew. bedight,  v.,  to  adorn.  —  Formed  fr.  be-  and  dight. bedikah,  n.,  examination,  required  by  Jewish religious  law.  —  Mishnaic  Heb.  bldhiqdh,  ‘exam¬ ination,  inspection,  search’,  verbal  noun  of bddhaq,  ‘he  examined,  tested,  scrutinized’,  fr. Biblical  Hebrew,  bddhaq,  ‘he  mended,  repaired’, which  is  rel.  to  Biblical  Hebrew  bedheq,  ‘fissure, rent,  breach’,  Aram.  bedhaq,  ‘he  examined,  ex¬ plored’,  bidhqd,  ‘fissure,  rent,  breach’, bedim,  tr.  v.  —  Formed  fr.  be-  and  dim. bedizen,  tr.  v.  —  Formed  fr.  be-  and  dizen. bedlam,  n.,  a  lunatic  asylum.  —  From  Bedlam, fr.  ME.  Bedlem,  fr.  earlier  Bethlem,  fr.  Betle- hem  (q.v.) ;  originally  name  of  a  hospital  in  Lon¬ don,  converted  later  into  a  lunatic  asylum. Derivatives:  bedlam-ism,  n.,  bedlam-ite,  n.,  bed- lam-ize,  tr.  v.
Bedlington  terrier,  bedlington,  n.  —  From  Bed- lington,  town  in  Northumberland,  England, where  it  was  first  bred.
Bedouin,  n.  —  F.  bedouin,  fr.  Arab,  badawtn,  lit. ‘desert  dwellers’,  pi .  of  badawi,  fr.  badw  (in  vulgar pronunciation  bedu),  ‘camp;  desert’.  The  plural suff.  -in  in  Arab,  badawtn  was  mistaken  for  part of  the  word.  Cp.  assassin. bedraggle,  tr.  v.  —  Formed  fr.  be-  and  draggle, bedridden,  adj.  —  ME.  bedrede,  fr.  OE.  bedrida, lit.  ‘bed  rider’  (in  contradistinction  to  a  ‘horse rider’),  formed  fr.  bed  and  ridan,  ‘to  ride’.  See bed,  n.,  and  ride.
=== leaf 96 ===
b. behemoth  with  Egypt,  p-ehe-mau,  ‘ox  of  the water’,  was  justly  rejected  by  W.Max  MUller. behen,  n.,  the  plant  Centaurca  behen.  —  Arab. bahman,  in  vulgar  pronunciation  behmen,  fr. Pers.  bahman,  a  kind  of  root  resembling  a  large radish.
behest,  n.  —  ME.  behest,  bihest,  fr.  OE.  behxs, ‘promise,  vow’,  fr.  behdtan.  See  next  word  and cp.  hest.
behight,  tr.  v.,  to  entrust,  commit.  —  The  orig. meaning  was  ‘to  promise,  vow’;  ME.  bihaten, fr.  OE.  behdtan,  ‘to  promise,  vow’,  fr.  be-  and hatan,  ‘to  command’.  See  hight  and  cp.  prec, word.
behind,  prep,  and  adv.  —  ME.  behinden,  fr.  OE. behindan,  fr.  be-  and  hindan,  ‘behind’.  See  hind, adj.
Derivative:  behind,  n.
behold,  tr.  v.  —  ME.  beholden,  fr.  OE.  hehealdan. behaldan,  ‘  to  hold  by,  possess’,  fr.  be-  and  heaklan. haldan,  ‘to  hold’.  See  hold,  v.
Derivatives:  beholden  (q.v.),  behold-er,  n. beholden,  adj.  —  Prop.  pp.  of  behold,  used  in  its earlier  sense  as  ‘held  by,  attached  to’, behoof,  n.  —  ME.  behof  (ch\ef\y  in  the  dat.  behove with  the  prep,  to,  ‘for  the  use  of’),  fr.  OE.  behof. ‘profit,  benefit,  advantage,  need’,  rel.  to  OFris., MLG.  behof,  Du.  behoef,  MHG.  behuof,  G. Behuf  ‘benefit,  use,  advantage’,  Dan.  behov, Swcd.  behof,  ’need,  necessity’,  and  in  gradational relationship  to  E.  have  and  heave, behove,  tr.  and  intr.  v.  —  ME.  behoven,  fr.  OF.. behofian,  ‘to  need,  require’,  fr.  behof.  See  prec. word.
beige, n.,  1)  undyed  and  unbleached  wool  fabric: 2)  its  grayish  brown  color;  adj.  grayish  brown.
=== leaf 97 ===
nt  on’,  which  is  rel.  to  MDu. belanghen,  Du.  belangen,  G.  belangen,  ‘to  con¬ cern;  to  belong  to’  (whence  Du.  belong,  resp. G.  Belong,  ‘concern,  interest,  importance’),  and to  OE.  lang,  etc.,  ‘long’.  The  orig.  meaning  of the  above  verbs  prob.  was  ‘to  be  alongside  of. See  long,  adj.,  and  cp.  along.
Derivatives:  belong-er,  n.,  belong-ings,  n.  pi. Belostoma,  n.,  a  genus  of  aquatic  bugs  (zool.)  — ModL.,  lit.  ‘arrow-mouthed’,  fr.  Gk.  tplXoq, ‘arrow,  dart’,  and  <jT6|za,  ‘mouth’.  The  first element  stands  in  gradational  relationship  to flakkeiv,  ‘to  throw’;  see  ballistic.  For  the  se¬ cond  element  see  stoma.
belove,  tr.  v.;  now  only  in  the  passive.  —  ME. biluven,  formed  fr.  bi-  and  luven,  ‘to  love’.  See be-  and  love,  v.
beloved,  adj.  — •  Prop.  pp.  of  belove. below,  adv.  and  prep.  —  Formed  fr.  be-  and  the adj.  low.
Belshazzar,  n.,  the  last  Chaldaean  king  of  Baby¬ lon  (Bible).  —  Heb.  Belshatztzar,  contraction of  Akkad.  Bel-shar-usur  i.e.  ‘Bel,  protect  the king’.
belt,  n.  —  ME.,  fr.  OE.,  rel.  to  ON.  belli,  OHG. balz,  fr.  L.  balteus,  ‘girdle’,  a  word  of  Etruscan origin.  Cp.  balteus,  baldric,  bauson,  bausond, bauxite.
Derivative:  belt,  tr.  v.
Beltane,  n.,  an  ancient  Celtic  festival  on  May Day.  —  Gael,  bealtuinn,  a  compound  lit.  mean¬ ing  ‘blazing  fire’.  For  the  first  element  see  bale¬ fire.  The  second  element  is  rel.  to  Olr.  ten,  ‘fire’ (for  I.-E.  *tepnos),  and  cogn.  with  L.  tepere,  ‘to be  lukewarm’,  tepidus,  ‘lukewarm’.  See  tepid and  cp.  words  there  referred  to. beluga,  n.,  a  kind  of  dolphin.  —  Russ,  beluga,  fr. beliy,  ‘white’,  which  is  rel.  to  OSlav.  bilu,  ‘white’, Lith.  bciltas,  ‘white’,  Lett,  bdls,  ‘pale’,  and  cogn. with  OE.  bail,  ‘a  blazing  fire’,  ON.  bal,  ‘a  great fire’.  See  balefire  and  cp.  the  first  element  in Beltane.
```


## [2026-09-04T22:45:28.011Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 80 81 82 83; do echo \"=== POK_03 leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((n+1)) POK_03.txt | head -12; done",
 "description": "Pokorny p.844"
}
```


### [2026-09-04T22:45:31.060Z] TOOL RESULT

```
=== POK_03 leaf 80 ===
 sich  auszeichnend';  d^eo-ngÖTtog  , Seher'  (,der  sich  von  Gott  aus vernehmlich  Machende');  vielleicht  rtgaTclg  , Zwerchfell';  anders  oben  S.  620.
air.  rieht  ,Form,  Gestalt',  cjmr.  rhith  ,species'  {*pYp-tu-)]
ahd.  furhen  , reinigen,  putzen,  fegen'  (,in  die  Augen  fallend  machen, ein  Ansehen  geben'),  mhd.  vUrbe  , Reinigung;  Sternschnuppe',  and.  wel gifurvid  ,casta'.
WP.  II  89.
pret-,  pr^t-  ,verstehen'.
Mir.  räthaigid  ,bemerkt';  got.  frapi  n.  Sinn,  Verstand',  frapjan,  fröp ,verstehen',  fröps  ,klug,  verständig',  aisl.  frödr,  as.  ags.  fröd,  ahd.  fruot ds.,  mhd.  vruotec,  vrüetec  , schnell  entschlossen,  munter,  tapfer',  nhd.  Schweiz. fruetig  ,froh,  frisch,  tapfer,  schnell',  auch  ahd.  frad  ,strenuus  efficax', fradah-lih  ,procax';  vielleicht  ahd.  antfrist  ,interpretatio'  {*pret-sti-)'^  lit. prantü,  prästi  , gewohnt  werden',  su-prästi  ,versteheQ',  protas  , Verstand', lett.  prüotu,  prast  ,verstehen,  begreifen,  merken',  präts  ,Verstand,  Sinn, Wille,  Meinung,  Gemüt',  apr.  prätin  Akk.  ,Rat',  iss-jprestun  ,verstehen', is-presnan  Akk.  ,Vernunft',  issprettingi  Adv.  ,nämlich';
toch.  A  pratim,  B  jpratim  ^Entschluß'.
WP.  II  86,  WH.  I  711,  Trautmann  230.
preu'  ^springen,  hüpfen';  plouo-  , springend'.
Ai.  prdvate  ,springt  auf,  hüpft,  eilt^,  pravä-  ,flatternd,  schwebend,  fliegend', upa-prü-t  ,heranschwebend,  heranwallend'  (Zusammenschluß  mit   den  Ab-
846  f
kömmlingen  von  *jpleu-  ^rinnen^,  s.  dort),  plava-  m.  ^Froscli'^  eig.  ,Springei mandüka-pluti-  m.  ,Froschsprung  =  Überspringung  mehrerer  Suträ* plava-ga-, plavq-gama-  m.  ,Frosch,  Affe^  (d.  h.  ,im  Sprunge  gehend');  aia]^ frar  ^schnell,  flink',  urnord.  Fraioa-  (eig.  .springend'  ==  ai.  pravd-)^  ^ frä  ,iroh',  ahd.  frao,  frö,  frawer  ,strenuus,  alacer  (GL);  froTi',  wovon  ah(__ frouwen,  frewen  ,sich  freuen',  frewi,  frewida  ,Freude';  russ.  pryt%  f^ , schneller  Lauf,  prytkij  ,hurtig,  eilig^
=== POK_03 leaf 81 ===
ren  ,ge- frieren  machen',  ahd.  as.  frost  (*frus-taz)]  3Lgs.  forst  m.  aisl.  frost  n.  ,Frost'»  1
B.  Ai.  plösati  ,versengt,  brennt',  plusta-  ,versengt,  verbrannt';  alb. prüsh  .brennende  Kohlen,  Glut';  lat.  prüna  ,glühende  Kohlen*  (*p)ru8na) prürlre  ,jucken'.
WP.  II  88,  WH.  II  378  f.
pris-  .zerkleinern'??  nur  griech.  und  alban.
Gr.   Ttgiü)   {ßTtqia&TjVj   TtQLGtög)    .durchsäge,   knirsche    mit   den   Zähnen',
nQtü)Vj  -ovog  ,Säge',  nqiaiia  ,das  Gesägte,  Sägespäne;   dreiseitige  Säule*;   ^
alb.  jprish  ,verderbe,  zerbreche,  zerstöre'. WP.  11  89.
pro-  s.  2.  per-  S.  813  f.
prokto- :  prokto-  , Steiß',  nur  gr.  und  armen.?  "^
Arm.    erastank   PI.   ,edQai^    (von  *erast  =  prdkto-)  kann  die  Redukt.-St. neben  gr.  Tr^wxrog  ,Steiß,  After'  sein. WP.  II  89,  Meillet  Esquisse^  142.
prso-  (?)  ,Lauch',  ist  mediterranes  Lehnwort.
Gr.  ftgdaov  ,Lauch':  lat.  porrum,  porrus  , Lauch'. WP.  II  84,  WH.  II  343,  Szemerenji  Gl.  33,  261  f.
=== POK_03 leaf 82 ===
e,  lett.  paüna  ,Ränzel,  Bündel'.
pU'g- :  gr.  Ttvyri  ,der  Hintere' ;  aisl.  fjük  ,Schneesturm',  fjüka  , schnell durch  die  Luft  fahren,  stieben',  fok  , Schneegestöber',  mhd.  fochen  , blasen'; lett.  püga  ,Windstoß',  pauga  ,Polster,  Kopf.
p{h)u-k-'.  arm.  p^'uH  ,Hauch,  Wind,  Furz',  PL  , Blasebalg',  p^^äem ,hauche',  p'"Jham  ,blase  mich  auf;  npers.  pük  ,das  Blasen  (um  Feuer  an- zufachen) ,Blasebalg',  afgh.  pü,  püh  ,a  puff,  a  blast,  the  act  of  blowing';
lit.  pukne  ,Blatter',  pukUe  ,Beule',  püks^iü,  püksti  ,keuchen,  schnaufen', pükysj  pukis  , Kaulbarsch'  (*,Dickkopf') ;  Iqü.  pukuls  ,Troddel'  (eig.  ,dicke Quaste').
348  f
pu-p-  (wohl  o-ebrochene  Redupi.):  alb.  pupe  ,Quark,  Weintraube, Hügel«, püpeze  ^Knospe,  Mohn^  püpule  ,Rückeii^;  lat.  püpus  ^kleines  Kind,  Knabe, Bübchen^,  *püpa  ^kleines  Mädchen'  und  (spät)  .Pupille  des  Auges'  (das kleine  Spiegelbild  des  Beschauers  im  Auge  des  Angesprochenen'),  vulgär- lat.  *puppa  (hz.jpoupe,  ital.poppa)  jBrustwarze';  air.  ucht  ,Brust'  {*puptu-y^ lett.  jpups  ,Weiberbrust',  paupt  ,schwellen',  püpuoVi  püpuoVi  ,Weiden- kätzchen'  (mit  Media  pubulis  .Blase  auf  Bier.  Knoten  im  Garn'),  üt. pupele,  pupela,  pupuole  , Knospe',  wohl  auch  lit.  pupä,  lett.  pupa  .Bohne^
p{h)u-s-:  ai.  püSyati,  pumäti,  pösati  .gedeiht,  macht  gedeihen,  wächst zu.  ernährt',  pustd-  .wohlgenährt,  reichlich',  pusti-y  pusti-  f.  .Gedeihen, Wachstum.  Fülle',  pösa-  ds..  puspa-m  ,Blume.  Blüte',  pushald-  .reichlich, prächtig,  in  voller  Lebenskraft';  gr.  cpvaa  .Blasen,  Blasebalg.  Blase' {*(ptaaa  oder  *pliüt-ia),  cpvadu  .blase,  blase  auf.  (fDoiaa)  .schnaube', cpvaiy^  f.  .Knoblauch,  Zwiebel'.  (pvaal(l)ig  f.  .Blase',  cpvaxa  f.  .Blase, Schwiele',  cpvayirj  f.  .Darm,  Wurst'.  cpvay,cüv  ,Dickbauch'.  7toi-(pvGöa)  .blase, schnaube';  lat.  pussula,  pustula  .Blase.  Bläschen.  Blatter';  norw.  feysa {*fausian)  .aufschwellen,  aufgähren'.  f{j)usa  .sausen,  mit  Gewalt  aus- strömen'; lit.püsU  ,Blase',  lett.  püslis  ds.,  lit.  pusnis^  pusnynas  , zusammen- gewehter Schneehaufe',  püse  (pü§e)  ,Blatter',  pü§kas  , Hitzbläschen  auf der  Haut',  lett.  puSJcis  .Blumenstrauß,  Bänderstrauß,  Büschel'  u.  dgl.;  aksl. *puchati  .blasen'  *opucJinpti  .anschwellen',  puchh  .cavus  (aufgedunsen)', russ.  pychdH  .keuchen.  Gluthitze  von  sich  geben*,  pychah  .aufgeblasen, hochmütig  sein',  pysnyj  .üppig,  aufgeblasen,  hochmütig*  usw.,  aksl.  napyUiti s^  ,sich  aufblasen',  russ.  pyscüh  ds.  (*pyskiti]  wohl  auch  öech.-poln.  usw. pysTc  ,Schnauze,  Maul  mit  dicken  Lippen');  vgl.  oben  S.  790  päuson-?
pu-t-i  ai.  piipputa-  ,Anschwellung  an  Gaumen  und  Zahnfleisch';  gr. nvvvog  ,Steiß'  Hes.  {*put-snos)]  lat.  praepütium  ,Vorhaut'  (von  einem "^pütos  ,penis'.  vgl.  wruss.  potka  ds.);  vielleicht  ir.  uth  .Euter'  {*putus)', halt.  *putiö  , blase'  in  lit.  puciilj  pusti  ,blasen,  wehen', 
=== POK_03 leaf 83 ===
 reflex.  ,schwellen', puntü,  püsti  ,schwellen,  sich  aufblasen',  püsle  f.  .Blase,  Harnblase',  putlüs ,sich  blähend,  aufgeblasen,  stolz',  putä  .Schaumblase',  pütmenos  t  PI. , Geschwulst',  pari-putelis  .aufgeblasener  Mensch',  päpautas  ,Schwiele', auch  pautas  ,Ei,  Hode',  piisu,  püst  ,blasen.  wehen,  hauchen,  atmen', püsma  .Atemzug',  püte  ,Blase,  Blatter',  wohl  auch  lit.  puträ  .Grütze', lett.  putra  , Grütze,  Brei';  auf  Media:  lett.  pudurs,  puduris  ,Büschel, Haufe',  pudra  ,Haufe';  wruss.  potka  {*pztbka)  , männliches  Glied'.
WP.  II  79ff.,  WH.  II  389 f.,  392,  Trautmann  233 f.;  vgl.  oben  2.  b(e)u'.
2.  pu-:peu.9-  .faulen;  stinken';  vermutlich  aus  einem  pu  ,pfui!'  entwickelt; pü-ti-  , Fäulnis',  pu-tro-  , verfault';  pu-to-  ,podex,  cunnus'.
849
Ai.  f'iiyati  ,wird  faul^  stinkt^  =  av.  puyeiti  ,wird  fauP,  ai.  püya-,  -m Biter^,  'pii'ti-  ,faul,  stinkend;  Jauche,  Eiter^  =  av.  pütay-  _,Fauligwerden, Verwesung^;  pashto  pül  ^Trübung  des  Auges^,  westosset.  ambud  ,faul';  ai. putäu  (:  aisl.  fud)  ,Hinterbacken^;  mit  -sko-:  mpers.  püsinltan  , faulen', aisl.  fauskr  , morsches  Holz';  arm.  hu  , eitriges  Blut';  gr.  n'öd^o)  ,manche faulen',  uid-oy-ai  ,faule',  rtvov  (*pu^om),  rtvog,  -sog  n.  ,Eiter';  vielleicht auch  ^vög  m.,  rrvagy  Tföazog,  uvaria  ,Biestmilch';  lat.  püs,  püris  ,Eiter' (*puuos\  jpüteö,  -ere  , faulen',  pütidus  ,faul'  (von  einem  Partiz.  *pü-to-s)j püter,  -trisj  -tre  ,faul,  morsch'  mit  w-,  wie  mir.  othrach  ,Misthaufen',  wohl auch  othar  ,ein  Kranker'  (*putro-)j  othar-lige  ,Krankenbett,  Begräbnis- platz'; aisl.  füinn  ,verfault,  rott^,  füi  ,Fäulnis',  füna  ,faulen',  feyja  ,ver- faulen  lassen,  verrotten  lassen',  got.  füls,   aisl.  füll,  ags.  ahd.  fül  ,faul* ;
aisl.  fud  f.  ,cunnus',  mhd.  vut  ,cunnus',  alem.  vüdeli  Kinderwort  ,Popo', geminiert  mhd.  votze^  lit.  pif^vü,  püti  ,faulen',  Kausat.  püdau,  -yti  ,faulen machen',  lett.  put  ,faulen',  Kausat.  püdet  ,faulen  machen',  lit.  pidulas (*peu-lo-s)  m.  ,verfaulter  Baum',  lett.  praüls  ,verfaultes  Holz'  {*plauls), lit.  puliai  m.  PI.  ,Eiter',  puves{i)ai  m.  PI.  ,verfaulte  Sachen',  lett.  puvesi m.  PI.  , Eiter',  pü^ni  m.  PL  ds.,  papuve  f.  ,Brachfeld'.
mit  g:  aisl.  füki  , Stank',  nisl.  füki  auch  ,verfaultes  Seegras,  Seetang', wie  l
```


## [2026-09-04T22:45:40.566Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^prāi\\|^prai-\\|^prI-\\|prai-, prI-\\|priyás\\|priyá-\\|frInAmi\\|frīnāmi\\|afrīnāmi\" POK_03.txt | head -20; echo \"---\"; grep -n \"lieben.*erfreuen\\|priyas\\|āfrīnāmi\\|āfrinami\" POK_03.txt | head -20",
 "description": "Pokorny prāi- root"
}
```


### [2026-09-04T22:45:40.627Z] TOOL RESULT

```
---
```


## [2026-09-04T22:45:43.928Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 76 77 78; do echo \"=== POK_03 leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((n+1)) POK_03.txt | head -40; done",
 "description": "Pokorny p.844 area"
}
```


### [2026-09-04T22:45:46.672Z] TOOL RESULT

```
=== POK_03 leaf 76 ===
sk.  pustma[s\  ,postremae';  umbr.  postne,  lat.  pöne  aus  *posti-ne'y  osk. pustin,  umbr.  pustin  (aus  "^posti  en)  ,je  nach'  Präp.  m.  Akk. ;  umbr.  pust- naiaf  ,posticas',  purnaes  ,posticis';  lat.  posticus  ,hinten  befindlich'.
2.  -ko-  ai.  pascä  (Instr.)  Adv.  , hinten,  westlich,  später'  =  av.  pa§ca Präp.  ,hinter,  nach',  örtlich  und  zeitlich,  ai.  paäcät  (Abi.)  Präp.  ,hinter,. nach,  westlich',  av.  paskät  Adv.  ,von  hinten  her,  hinterdrein'  räumlich und  zeitlich ;  lit.  paskui,  päskui  (Dat.)  Adv.  ,hinterher,  nachher',  Präp, .nach'.
842  f
3.  Im  Ausgang  noch  strittig  ist  ap.  pasä  ,nach^  Präp.  örtlich  und  zeit-
lieh;   alb.  pas,  geg.  mbas  Präp.  ,hinter,   nach'  (idg.  *pos  +  Demonstr.  si).  i
WP.  II  78  f.,  WH.  II  347  ff.,  Trautmann  207,  Schwyzer  Gr.  Gr.  2,  508.    i
po-ti  »gegenüber,  entgegen,  gegen',  durch  das  Adv.-Formans  -ti  (vgl.  *proti. :     ; *pro  oben  S.  815  f.)  aus  *po  (s.  unter  *apo  ,abO  erweitert. Av.  paiti,  ^.^.patiy  Präverb,  und  Präp.  ,gegen,  entgegen,  zu,  auf,  bei'; ,an;  für,  um';  ,von — aus';  ,an — hin,  in';  hom.,  böot.,  lak.  usw.  noxi  ,nQ6g' Präverb,  und  Präp.  ,gegen — hin,  gegen,  gegenüber;  an,  zu^  ,an — hin,  von-'. WP.  II  77,  Schwyzer  Gr.  Gr.  2,  508  f.
poti-s  ,Hausherr,  Herr ;  Gatte^  neben  -pot-  im  Kompositum ;  fem.  *potni  j zugrunde  liegt  unflektiertes  poti  , selbst'.  ,^
Ai.  pdti-,  av.  paiti-  ,Herr,  Gebieter,  Gemahl' ;  ai.  pdtnl  ,Herrin,  Gattin',  i av.  pa-d-nl'  ,Herrin' ;  ai.  pdtyate  ,herrscht,  ist  teilhaftig'  ( :  lat.  potior) ;        ^
av.  x^ae-pati'  ,er  selbst';  ^
gr.  n:6aig  , Gatte',  nözvLa  , Herrin  (des  Hauses),  Gattin';  dea-noiva  ''-\ , Herrin  des  Hauses'  {^ÖBa-Ttovici,  aus  *dsa-7Vorvia)  dsa-fcövr^g,  -ov  ,Herr  1 des  Hauses'  (s.  oben  S.  198);  alb.  pata  ,hatte',  pashe  ,gehabt'  (*pot'tO')  4 (zu  einem  Präs.  wie  lat.  potior,  ai.  pdtyate) ;  i^
lat.  potis  (potior j  potissimus)  , vermögend,  mächtig',  possum,  alat.  auch potis  sum  ,kann*,  potui,  potens  von  einem  e-Denominativ  wie  osk.  putiad ,possit',  pütians  ,possint',  lat.  potestas  , Macht*,  potiorj  -Irl  [potUur  und potitur)  ,sich  bemächtigen';  com-pos  ,teilhaftig'  (*,Mitherr'),  hospes,  -itis , Gastfreund',  pael.  hospus  (*ghosti-pots  , Gastherr') ;  ein  unflektiertes  *poti , selbst'  steckt  in  utpote  ,wie  natürlich,  da  nämlich,  nämlich',  eig.  *w^  *pote (est)  ,wie  es  möglich  ist  =  natürlich',  ferner  mit  Synkope  in  mihi-,  meö-, suäpte  usw.;
got.  brup-faps  ,Bräutigam',  hunda-faps  ,Befehlshaber  über  100  Mann'; engh  
=== POK_03 leaf 77 ===
fad  , stark,  tapfer,  groß';
lit.  päts  , Ehemann'  und  , selbst'  (alt  patis),  lett.  pats  , Hausherr'  und ,selbst',  lit.  vie§pats  ,Herr'  (alt  viespatls),  apr.  pattiniskun  Akk.  f.  ,Ehe'; f.  alit.  vieSpatni]  *patni  unter  Einfluß  von  "^pati-  umgestaltet  zu  *pati  in apr.  waispattin  Akk.  ,Frau',  \ii.  pati  , Ehefrau',  Iqü.  pati  ,Wirtin';  indekl. Partikel  lit.  pät,  lett.  pat  , selbst,  sogar,  gerade' ;  über  aksl.  gospodh  ,Herr', s.  oben  S.  453;
hitt.  -pat  , eben  (so),  auch,  vielmehr';  toch.  A  pats  , Ehemann'.
WP.  II  77  f.,  WH.  I  660 f.,  II  350 f.,  379 f.,  Trautmann  208,  Benveniste Origines  1,  63  f.,  Pedersen  Hitt.  77  f.,  Endzelin  Lett.  Gr.  396  f.
pöu-  :  p9U'  :  pü-  ,klein,   gering,   wenig',  vielfach   für  ,Junges,  Tierjunges, kleines  Tier';  pö[u]-lo-s  ,Junges',  pou-ko-  , wenig',  pu-tlo-s  Kind^
843
1.  Mit  -o-  Suffix:  got.  fawai  PL  , wenige',  aisl.  fär  ,wenig,  wortkarg^ fä-tekr  ,arm'  (wie  lat.  'paujper),  abd.  fao,  fö  , wenig',  Dat.  PL  fouuem, as.  fä,  ags.  fea,  PL  feawe,  engL  few  ^wenige'.
2.  Mit  Formans  -ko-:  lat.  jpaucus  , wenig',  jpaujper  ,arm'  (*pauco-paros Q^er  pato-paros?  ,wenig  erwerbend,  wenig  sieb  schaffend');  abd. /öÄ  ,wenig';
Mit  Suffix  -Zo- :  lat.  paul(l)us  ^klein,  wenig'  (*pauJcs-lo-),  pauxillus  ,ganz wenig'  i^pauk-s-lo-lo-).
3.  Mit  Formans  -ro-i  gr.  rravQog  , klein,  gering',  lat.  mit  Umstellung parvus  , klein',  parum  (*parvo7n)  ,zu  wenig'.
4.  , Junges,  Tierjunges':
gr.  Ttavg  (att.  Vasen),  Gen.  naJ^öq  (kjpr.,  dazu  ein  neuer  Nom.  nao) Ttalg,  Gen.  naidög  m.  f.,  bom.  Ttaig,  rtafiö-  ,Kind' ;  lat.  puer  ,Kind,  Knabe, Mädcben'  (^puuero-),  puella  ,Mädcben'5
got.  fula,  aisl.  foli  m.,  fyl  n.  i^fulja-),  u.  fylja  f.,  ags.  fola^  abd.  folo, fuU(n)  , Füllen,  Foblen';  daneben  *pö[u]los  in  arm.  ul  , Ziege',  am-ul  ,un- frucbtbar'  (*^-jpöZo-),  yii  f.  ,scb wanger'  (*i-pölniya)  ]  gr.  TtwXog  ,Foblen', aucb  ,junger  Mann,  junges  Mädcben',  nwXlov  ,kleines  Foblen,  Junges',  alb. pele,  pele  , Stute'  (Fem.  zu  *pölos)]  vielleicbt  med.  Arbu-pales,  wenn  es , weiße  Foblen  besitzend'  bedeutet.
5.  Mit  f-Formantien :  putrd-  m.,  av.  ap.  pud-ra-  m.  (letztere  rxis  pütlo-  = osk.  puklo-)  ,Sobn,  Kind';  gr.  Namen  wie  IIcü-TaXog',  lat.  putus,  putilliis ,Knabe',  woneben  ^püt-so-  in  püs{s)us,  -a  ,Knabe,  Mädcben',  aber  püsillus ,sebr  klein'  ist  Demin.  von  pullus  (^putslo-lo-s) ;  osk.  puklo-  ,Kind'  (=  ai. putrd-),  pälign.  puclois  Dat.  PL  ,pueris',  mars.  pucles;  lat.  pullus  ,jung, Tierjunges'  (*put-s-lo-) ;
baltoslav.  "^putä  , Vogel'  in  russ.-ksl.  pita  , Vogel',  p^t^§th  »kleiner  Vogel' (, Vogel'  eigentL  ,junger  Vogel'),  lit.  putytis  ,junges  Tier,  junger  Vogel' (Zärtlicbkeitsausdruck),  balt.  ^put-n-a-  in  lett.  putns  , Vogel*;  mit  anderer, demin.  Formansverbindung  lit.  paü-kstis  ,Vogel^
VTP.  II  75  f.,  WH.  II  259,  265  f.,  382  f.,  385  f.,  394,  Trautmann  233.
pougo-  oder  pougho-  , integer,  lauter
=== POK_03 leaf 78 ===
';  nur  kelt.  und  slav.
Air.  ög  ,jungfräulicb',  öge  , Jungfräulichkeit' ;    cecb.  pouhy  ,lauter,  bloß, einfach'. WP.  II  77.
prä-  , biegen'  ? ;  nur  lat.  und  kelt.
Lat.  prävus  ,verkebrt;  schief;  schlecht';  dazu  prätum  , Wiese'  (als  ,Ein- biegung  des  Bodens',  vgl.  z.  B.  lit.  lankä  ,Einsenkung,  Wiese':  leükti jbiegen')  und  (als  , Aufbiegung,  Wölbung,  Hügel');  mir.  räthj  raith  m.  f. , Erdwall,  Festung',  mcjmr.  hed-rawtj  ncjmr.  hedd-rod  m. , Grabhügel,  Grab',
844  •
bret.    hez-ret    f.    ,Begräbnisplatz,    Friedhof^    gall.    rätin   Akk.    Sg.   ,Burg- (hügel)S  ON  Argento-räte. WP.  II  86,  WH.  II  358  f.
präi-,  prQi-,  pri-  (pri-)  ,gerii  haben,  schonen,  friedlich-frohe  Gesinnung*  j  \^^m pri-tö'  ,geliebt^  priio-  ,liebS  priiä-  , Gattin*,  priio-tä  ,Liebe',  pnio-  *^| tuo-  ,das  Lieben^  \i^
Ai.  prlnäti  ,erfreut'.  Med.  ,ist  vergnügt  über  etwas',  jprlyate  ds.,  ,liebt*, prltd-  ,vergnügt,  befriedigt;  geliebt',  prlti-  f.  ,Freude,  Befriedigung',  pri, yäydte  ,behandelt  liebevoll,  befreundet  sich'  ( :  got.  frijön,  aksl.  prija-jg)^ priyd-  ,lieb,  erwünscht,  beliebt',  m.  , Geliebter,  Gatte',  f.  , Geliebte,  Gattin' (==  av.  frya-,  aisl.  Frigg  usw.,  und  got.  freis,  c.  rhydd  ,frei'),  pHyatvd-m ,das  Liebsein  oder  -haben'  (:  got.  frijapwa  L  ,Liebe*),  priydtä  ds.  (==  ags. freod  ,Liebe');  mit  *jpr9i-  :  prdyah  n.  , Vergnügen,  Genuß',  jpremdn-  m.  n.  ^„„.^^^ jLiebe,  Gunst',  jpretdr-  , Wohltäter,  Liebhaber,  Pfleger',  Superl.  prdistha- (ved.),  prBstha-  ,liebst,  teuerst',  wonach  Kompar.  prSyas-  ,lieber'  für älteres  *präyas-]  av.  fräy-  , befriedigen',  z.  B.  frlnämahi  Partiz.  frita-^ frlna-,  fri&a-  ,iv oh]  befriedigt;  geliebt',  /ri^i- f.  ,Gebet',  frya-  ,lieb,  wert'; vielleicht  der  hispan.  (ven.-illyr.  ?)  VN  Praesta-marci  (:  ags.  frid-hengest)'^
gr.  7tQGiüg  , sanft,  mild'  aus  ^Ttgaiv-  mit  jüngerer  o-Flexion  ngaog,  beweist idg.  äi;  hingegen  gehört  air.  riar  f.  , Wille,  Wunsch'  zu  erez-,  S.  330;
cymr.  rhydd  ,frei'  ==  got.  freis  (akk.  frijana),  ahd.  as.  frl,  ags.  freo, frl  ,frei,  los,  frei  von',  aisl.  in  frjäls  aus  *frlhals  (die  Bed.  ,frei'  ur- sprüngl.  ,zu  den  Lieben  gehörig') ;  aisl.  Frigg,  ahd.  Frija  , Gattin  Wotans', ags.  freo  f.,  as.  frl  n.  ,Weib  von  edler  Abkunft'  (,die  liebe') ;  got.  frijön ,lieben',  aisl. /r/ä  ds.,  ags.  friogan  ,lieben,  befreien*,  mdn.  vrien,  3.3.  friohan , freien,  werben',  Partiz.  got.  frijönds  , Freund',  aisl.  frcendi,  PL  fröendr ,Freund,  Verwandter',  ags.  friond,  as.  f
```


## [2026-09-04T22:45:59.944Z] TOOL CALL #28: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-04T22:45:59.948Z] TOOL RESULT

```


```


## [2026-09-04T22:46:05.234Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82epo",
 "prompt": "Give the full reconstruction entry: form, gloss, descendants (especially Indo-Iranian, Avestan, Old Persian, Latin ab), and any note on variants *apo/*po/*apu/*pu."
}
```


## [2026-09-04T22:46:06.778Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C#Persian",
 "prompt": "Give the Persian etymology of بی (bi) 'without': Middle Persian form, Old Iranian/Proto-Iranian ancestor, cited authorities, and any related forms like ابی abē."
}
```


### [2026-09-04T22:46:11.781Z] TOOL RESULT

```
# Proto-Indo-European *h₂epó

**Form & Gloss:** The reconstructed adverb *h₂epó means "off, away," derived from *h₂ep + the allative suffix *-o.

**Key Variants:** Alternative reconstructions include *ápo, *apó (omitting the laryngeal), *h₂épo, and *h₁opó.

**Indo-Iranian Descendants:**
- Proto-Indo-Iranian: *Hápa
- Sanskrit: अपर (ápara, "other")
- Avestan: apara
- Old Persian: a-p-r (apara)

**Latin & Other Major Descendants:**
- Latin: abs (possibly from Proto-Italic *ap)
- Hittite & Luwian: āppa
- Gothic: afar
- Ancient Greek: ἄψ (áps)

**Related Formations:** The root appears in compounds like *h₂ep-ero- (comparative: "after," "other") and *h₂ep-tero- (also yielding "after" in Germanic).

**Note on Variants:** The page documents debate over whether the laryngeal *h₂ was present in Anatolian languages, suggesting possible alternation between forms with and without this element.
```


### [2026-09-04T22:46:13.501Z] TOOL RESULT

```
# Persian Etymology of بی (bi) 'without'

**Middle Persian Form:**
The word derives from Middle Persian with script notation needed, represented as (apē).

**Proto-Iranian Ancestor:**
The etymological chain traces back to Proto-Indo-European *h₂epó, meaning "off, away."

**Etymology Summary:**
According to the Wiktionary entry, بی evolved "from earlier ابی (abê), from Middle Persian (apē), from Proto-Indo-European *h₂epó ('off, away')."

**Related Forms:**
The article notes ابی (abē) as an earlier Persian variant, with a cognate appearing in Old Armenian ապա- (apa-), identified as "an Iranian borrowing."

**Usage Note:**
The source indicates that prepositional usage "is now relatively unusual in Iran" with بدون (bedun-e) being preferred, though it "remains common elsewhere."
```


## [2026-09-04T22:46:24.015Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%AF%D8%B3%D8%AA%D8%B1",
 "prompt": "Give the Persian entry بیدستر: meaning and full etymology, including any Middle Persian or Avestan forms and the \"without dastar\" folk etymology."
}
```


## [2026-09-04T22:46:25.339Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%81%D8%B1%DB%8C%D9%86",
 "prompt": "Give the Persian entry آفرین: meaning and full etymology (Middle Persian, Avestan ā-frī-, Proto-Iranian, PIE root), and any related verbs آفریدن."
}
```


### [2026-09-04T22:46:29.233Z] TOOL RESULT

```
# Persian Entry: بیدستر (bidastar)

**Meaning:** The word denotes a "beaver."

**Etymology:** According to the Wiktionary source, the term appears to derive from Proto-Indo-European roots. Specifically, it likely combines *widʰu- ("tree, beam") and *h₁ed- ("to eat"), yielding a literal meaning of "wood-eater."

**Note on Folk Etymology:** The provided source does not mention a "without dastar" folk etymology or any Middle Persian or Avestan forms. The entry only presents the Proto-Indo-European derivation as the documented etymology, with an alternative form listed as ویدستر (vidastar).
```


### [2026-09-04T22:46:32.646Z] TOOL RESULT

```
# Persian Entry: آفرین

## Meaning
The word آفرین (āfarīn / âfarin) functions as:
- **Noun**: "acclamation"
- **Verb**: present stem of آفریدن (âfaridan)
- **Interjection**: "well done" or "bravo"

## Etymology

The entry traces this term back through several linguistic layers:

**Middle Persian origin**: The word derives from Middle Persian āfrīn, meaning "praise, blessing."

**Proto-Iranian composition**: It combines two elements—a prefix and a verbal root: *ā-* plus *fraiH-* (meaning "to rejoice, atone, please").

**Indo-European ancestry**: 
- The prefix connects to Proto-Indo-European *h₂éd* ("to, at")
- The verbal component derives from Proto-Indo-European *preyH-* ("to please; to love")

## Related Verb
The interjection and noun forms relate to **آفریدن** (âfaridan), of which آفرین represents the present stem.

**Antonym**: نفرین (nifrīn / nefrin)
```


## [2026-09-04T22:46:43.317Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9%D9%81%D8%B1%D9%8A%D8%AA",
 "prompt": "Give the Arabic entry عفريت (ʿifrīt): meaning, root, and full etymology. Does it mention a Persian origin (e.g. from āfarīd/āfarīn) or a Semitic root ʿ-f-r? Quote the etymology."
}
```


## [2026-09-04T22:46:44.733Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%88%D8%A7%D8%B1%D9%88%D9%86",
 "prompt": "Give the Persian entry وارون (vārūn): meaning and etymology, including Middle Persian abārōn and any Old Iranian reconstruction."
}
```


### [2026-09-04T22:46:49.439Z] TOOL RESULT

```
# Arabic Entry: عفريت (ʿifrīt)

## Meaning
The term refers to a supernatural being from Arabian folklore, also translated as demon, devil, fiend, or evil spirit. It can describe any infernal or supernatural being in general.

## Root
The word belongs to the Arabic root ع ف ر (ʿ-f-r), which relates to "ash."

## Etymology
The entry presents two possible origins:

**Primary theory (Middle Iranian):** "From a Middle Iranian past participle _āfrīd_ ('created'), originally an elliptic expression for _\*dīw afrīt_ ('demon's creation')"

**Alternative theory (Semitic):** Derived from the root ع ف ر related to "ash", with a comparable derivation type to عَكْرُوت (ʿakrūt, "scoundrel").

The etymology notably mentions a **Persian origin** through the Middle Iranian source, though it also preserves the possibility of internal Semitic derivation.
```


### [2026-09-04T22:46:50.948Z] TOOL RESULT

```
# Persian Entry: وارون (vārūn)

## Meaning

The Persian adjective وارون functions as "an alternative form of وارونه (inverted)." In Classical Persian usage, it carries figurative senses meaning "wicked, evil" or "pitiful."

## Etymology

The word has deep historical roots, being "inherited from Middle Persian" (ʾp̄lʾlwn' /⁠abārōn⁠/, "contrary, wrong, sinful"). The entry notes that the Middle Persian form required Book Pahlavi script documentation, indicating scholarly recognition of its ancient provenance through the Persian language family.

## Linguistic Context

Multiple Persian dialects preserve this term across different regions—from Classical and Iranian Persian to Dari and Tajik varieties—each with documented phonetic variations reflecting their respective sound systems.
```


## [2026-09-04T22:46:58.545Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && awk 'BEGIN{RS=\"\\f\"} NR==218' PLA_pages.txt | head -40; echo \"=== grep ifrit ===\"; grep -n \"ifrīt\\|'ifrit\\|ifrit\\|Ifrit\\|afrid\" PLA_pages.txt | head -20",
 "description": "Asbaghi p.203 ifrit"
}
```


### [2026-09-04T22:47:00.618Z] TOOL RESULT

```
Saraba                                                                       203                                                  Saı amdar


=         -       Saraba:        "Wagen"           ist        nach    Ml.         ein    arabisiertes         tk.    Wort,        Johnson
         bezeichnet               es       als     Wort           persischen            Ursprungs        1,


     -                                                  Pr
lu            -    Casäkir:           Pl.     v.       Lu askar          q.        vv

 Pr
me        - Caskar:              "Soldat,              Armee"            pers.           X) laskar        ? mp.           BER) laSkar        °,
         mand.        Caskar *, aram.                             Nas.
          Laskar:
          ind.       Matrose
                            "Matrose,
                                       od.
                                                   Soldat"
                                                  Kanonier           _
                                                                         pers.
                                                                         pers.. is
                                                                                        >    ar.
                                                                                             Laschkar
                                                                                                     >    engl. B>) frz.
                                                                                                              >
                                                                                                                                   lascar,/



     _                       _
SA - Caskari:                         "Soldat" s. Caskar,

=.                - Saskariyya:               "Heeresdienst".

2-12:! - Catärid:
            -
                                      "Merkur"               pers.                “Tr
                                                                                   Stir ep.                7     n
                                                                                                         *tira-däta.

=== grep ifrit ===
1738:>                   - ’afridam:                         "Seide"          = ’abrisam                    s. > abrisam .
5137:      afridan            "schaffen!"               mit       der Bed.            "geschaffen"               mp      ID ar äfritak a.
11433:urue - Safarit: Pl. v.                                       ws. Sifrit g. v.
11435:uss -              Sifrit:        "Dämon"              pers.             ra [ äfarid            v.   äfaridan            "schaffen"    mp.
11440:CyYas - Cifrin:                   "mächtig"                  s.    Cifrit u.            pers.      Aus f afaridan           q. ”
```


## [2026-09-04T22:47:06.464Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && python3 - <<'EOF'\nt=open('PLA_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nleaf=1\nll=[]\nfor ln in lines:\n    ll.append(leaf); leaf+=ln.count('\\f')\nfor n in (11433,11435,11440,5137):\n    print(n,'leaf',ll[n-1],'printed',ll[n-1]-15)\nEOF\nsed -n '11425,11445p' PLA_pages.txt",
 "description": "PLA ifrit page"
}
```


### [2026-09-04T22:47:08.818Z] TOOL RESULT

```
11433 leaf 218 printed 203
11435 leaf 218 printed 203
11440 leaf 218 printed 203
5137 leaf 102 printed 87
=.                - Saskariyya:               "Heeresdienst".

2-12:! - Catärid:
            -
                                      "Merkur"               pers.                “Tr
                                                                                   Stir ep.                7     n
                                                                                                         *tira-däta.

urue - Safarit: Pl. v.                                       ws. Sifrit g. v.

uss -              Sifrit:        "Dämon"              pers.             ra [ äfarid            v.   äfaridan            "schaffen"    mp.
                  uweo» afritan
                        afritan a.                            a-fräy          .


CyYas - Cifrin:                   "mächtig"                  s.    Cifrit u.            pers.      Aus f afaridan           q. ”


4         - Cakkäz:              "Stock"           v.        pers.    0, |, kawäze od.               gawäze         7,    mand.     gauaza
```


## [2026-09-04T22:47:18.291Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FRS afdom ===\"; grep -n \"آفدم\\|افدم\\|بافدم\" FRS.txt FRS_pages.txt | head -10; echo \"=== SNS afdom ===\"; grep -n \"afdom\\|awdum\\|abdom\\|apdom\" SNS.txt SNS_pages.txt | head -20",
 "description": "FRS and SNS afdom"
}
```


### [2026-09-04T22:47:18.357Z] TOOL RESULT

```
=== FRS afdom ===
FRS.txt:13123:مکن خویشتن از ره راست گم که‌خودرا بدوز خ بری بافدم ۱۱ 
FRS.txt:13130:باندم عاقبت کار باشد » چ ؛ بافدم آخر باشد ۱ - فقط در ون ۰ 
FRS.txt:13137:چه بایدت کردن کنون پافدم مکرخانه روبی چوروبه بدم! 
FRS_pages.txt:14517:   ‫مکن خویشتن از ره راست گم که‌خودرا بدوز خ بری بافدم ‪۱۱‬‬
FRS_pages.txt:14529:                 ‫‪ -‬فقط در ون‪۰‬‬    ‫‪۱‬‬          ‫باندمعاقبت کارباشد » چ ؛ بافدم آخر باشد‬
FRS_pages.txt:14533:      ‫مکرخانه روبی چوروبه بدم!‬            ‫چه بایدت کردن کنون پافدم‬
=== SNS afdom ===
```


## [2026-09-04T22:47:24.230Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13118,13140p' FRS.txt; echo \"=== leaf ===\"; python3 - <<'EOF'\nt=open('FRS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=1; ll=[]\nfor ln in lines:\n    ll.append(leaf); leaf+=ln.count('\\f')\nfor n in (14517,14529,14533): print(n,'leaf',ll[n-1])\nEOF",
 "description": "FRS bafdom entry"
}
```


### [2026-09-04T22:47:26.122Z] TOOL RESULT

```
کر درم داری گزند آرد بدین بفکن‌اورا گرم ودرویث یگزین" ] 
تعوید بود [ ۵ شهید کو ید : ] 
بیا٩‏ نگارا ازچشم ند برس ومکن چر انداری‌باخودهمیشه حشم بنام ] 
۰ 
عاقبت باشد [رود عی کوید : 
مکن خویشتن از ره راست گم که‌خودرا بدوز خ بری بافدم ۱۱ 
7 رجوع کنیدبلفت «نکس > درصفحة ۲ 0-۲ : شمباليك بود بزبان ماورا الّهر» 
س : شم دای انز اری بود مسافر ان وروستایبانآ ذربایجان دارند ؛ : شم چار ود 
۴ چ ؛چندی‌مدیح ۰ س: چندینت‌مدح ‏ 4 س:« چندین ۵ - س وچ «کرسیم 
نست‌باری  .‏ 9-1 + کرماندوهي‌سخت‌بوده س: گرم اندوه ودلتنگي‌بود » چ مثل 
متن . ۷-این‌یتفقط درچ هستبجایبیت‌تبل ۰ ۸ - لن: چشم بنام تمویذی‌باشد چشم 
بدرا چ وس این‌لت‌راندارند . ٩‏ - :تا ۱۰ - ل : باندم عاقت‌بود » س » 
باندم عاقبت کار باشد » چ ؛ بافدم آخر باشد ۱ - فقط در ون ۰ 


۳۱ 


بوشکور کفت 
چه بایدت کردن کنون پافدم مکرخانه روبی چوروبه بدم! 
رود کی گوید : 
همچنان سرمه که دخت خوبروی هم بسان کردبردارد زروی ۲۰۰۰۰] 
۳ 
=== leaf ===
14517 leaf 360
14529 leaf 360
14533 leaf 361
```


## [2026-09-04T22:47:36.731Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"avdom\\|afdum\\|apdum\\|abdum\\|آفدم\\|افدم\\|واپسین\" SNS.txt | head -20; echo \"--- head of SNS\"; head -40 SNS.txt",
 "description": "SNS afdom"
}
```


### [2026-09-04T22:47:36.780Z] TOOL RESULT

```
3135:. (.U^i^- . >f < (•Jjl : abdum/dfdurn: ^v^ 
--- head of SNS




♦ A 



>l»>'i 





O^t' 



« 



*>& 



/ 




Shiraz University Publication 



A GLOSSARY OF 

SAYIST NE SAYIST
```


## [2026-09-04T22:47:41.513Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3125,3145p' SNS.txt; echo \"=== leaf calc ===\"; python3 - <<'EOF'\nt=open('SNS.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0; ll=[]\nfor ln in lines:\n    ll.append(leaf); leaf+=ln.count('\\f')\nprint(ll[3134])\nEOF",
 "description": "SNS abdum entry"
}
```


### [2026-09-04T22:47:43.457Z] TOOL RESULT

```
•YY/t6^ 

(•^IjlJ^* :Sa) a+tav3n+Ig . |j-b a-tavanlg &>£m«*' 

Star : s-««£i- -4cM>»er : ^ .^pT.jjT :a<fur/atur: >»*•■ 
To LMir.Man.*&wrijstiatr : ^^V: Utfcfc.312) 30r 



. (.U^i^- . >f < (•Jjl : abdum/dfdurn: ^v^ 
{GNPE. '•&&) ULiVb. 80-81) *apat9ma, apama : L_ 
awadum ^ (Mir. Man. 11,44) bdwm: .^li 9-10) 

•Y/A^ -An/Y^ ,/y-> ei/; f oil ^jU/jj**^ 

ji^^» :^Sj) «bS vinah +rf * ab§ .•b^ :abevinah: ^^mv a 

.ft/UiS .^Ab^- :abSvinah!h: -o-o-»»*o' 

:^ Utr. Man. II, 44) ->gr zjsL<j\ agar:>* HT: y*>* 
=== leaf calc ===
0
```


## [2026-09-04T22:47:52.582Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"abdum\\|dfdurn\\|afdum\" SNS_pages.txt | head; python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0; ll=[]\nfor ln in lines:\n    ll.append(leaf); leaf+=ln.count('\\f')\nimport re\nfor i,l in enumerate(lines):\n    if 'abdum' in l or 'afdum' in l:\n        print(i+1, ll[i], l[:120])\nEOF",
 "description": "SNS page leaf"
}
```


### [2026-09-04T22:47:54.336Z] TOOL RESULT

```
1842:                                                                                                                                                          >f   <   (•Jjl   :   abdum/dfdurn:                        ^v^
1842 29
```


## [2026-09-04T22:48:02.319Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 543 544; do echo \"=== BQT v2 leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((n+1)) BQT_v2_pages.txt | head -40; done",
 "description": "BQT p.1086"
}
```


### [2026-09-04T22:48:03.897Z] TOOL RESULT

```
=== BQT v2 leaf 543 ===
                                                                                         ‫—‬   ‫‪0‬‬
  ‫سیزیوشان بهشت‬

 ‫سپژ پا= با بای فارسی‌بالف کشیده»مردم‬              ‫گوبنذ سرمه کشیدن از میلی کهشبه (‪ )۱‬باشد‬
                  ‫شوم فدم و دامبارك پی باشد‪.‬‬       ‫روشنامی جشم را زیاده کند وه رکه ماخود دارد‬

                                                                           ‫آزچشم زخم ایمن گردد‪.‬‬
‫سبز باع ‪ -‬کنابه از تن و بدن آدمی‬
‫کنابه از آسمان هم‌هست ‪ -‬وبهشت را‬                   ‫سیخ = بکر اون وفتح‌ثالی‌وسگون‌خای‬
                                    ‫باشد ‪ -‬و‬
                                  ‫یگوزبند ‪.‬‬        ‫لبك را گونند مطلقاً خواه درآ دمی‌باشد‬      ‫شطمار‪,‬‬

‫سبز بال ‪ -‬بروزن قحط سال ‪ .‬نام نوعی‬                                                ‫در طعام ‪#.‬‬     ‫وخواه‬

‫ور است ؛ و بجای بای ابجد میم‌هم بنظر‬
                                      ‫از انگ‬        ‫سيد جين = با دال‌ایجد بروزن‌عرقحین»‬
                  ‫باشد‪.‬‬   ‫مبال‬
                             ‫آمده ات که س‬          ‫شمه مبوه‬   ‫و‬   ‫شه‬    ‫أست» وآن‬        ‫بمعنى بماچین‬

  ‫سلیعن»ی‬
        ‫سببزالی ب‪-‬روزن قحبطسا‬                      ‫بود که دخررهای فصل میوه درباغپا‬               ‫‪2‬‬
          ‫سبزبال است که نوعی از انکور است‪.‬‬                        ‫ای‬   ‫باشد ‪۱‬‬   ‫مانده‬   ‫ودرختها حایجا‬



 ‫ز ار ی » بروزن چرخ کری ‪ ,‬فصل‬                      ‫مب اج زور و‬             ‫خری‬
                                                                             ‫سبزآ‬
                              ‫سب‬
                  ‫است‬     ‫اهر‬
                            ‫هک‬‫ببند‬
                                 ‫رییم را گو‬
 ‫اب‪-‬ه از زاهدان اوهل‬
                   ‫کزنپوش‬
                        ‫سب‬
                                                   ‫‪ :‬و باواو معدو له لسر لو سند‬    ‫همهت‬
                                                                                      ‫از ‪i‬‏‬




=== BQT v2 leaf 544 ===
  ‫‪ ۷‬با ‪— ۵‬‬


‫گ بروزن نفزك‪ .‬مصفر سبز باشد‬
                          ‫سپز ل =‬                            ‫یکه‬
                                                               ‫ابه‬
                                                                 ‫زم‪-‬لکنا‬
                                                                       ‫فالك‬             ‫اون‬
                                                                                          ‫شز ب‬
                                                                                             ‫سب‬
‫‪ -‬وبمعنی صراحی شراب هم‌هست ‪ -‬و نام مرغی‬                                                               ‫باشد ‪.‬‬
‫سبز دلگ بسرخیآهخته و تاجی هم دارد‬              ‫أت‬            ‫سبز بهار = ناملحنی‌امت ازموسقی‪۱‬‬
‫مائند عدهدو" نرا بعربی شقراق (‪ )۲‬خواند ؟؛‬                    ‫سز خو ان » کنابه از آسمان اش‬
  ‫عرکاه‬
      ‫و بعضی کوبند سبزك پرنده ات که او‬
                                                         ‫‪ = ۲‬بكر الك " بمعنی‬            ‫از‬  ‫سی‬
                                                                                         ‫رزهد‬
                                          ‫نف‬
                                                        ‫امت ‪.‬که نام لحن نهم باشد از سی‬             ‫سابنزدرسبز‬
 ‫سب کار گاه = بمعتی سز طشت است‬
                  ‫تابه اآزسمان باشد‪.‬‬
                                   ‫که‬
                                                                                                   ‫لحن پاربد‪.‬‬
                                                         ‫سز ‪ = ۵۵‬بکر دال ابجد (‪ )۱‬و ظپور‬
 ‫سمز گرا = باکاف فارسی‌ورای‌فرشت(‪)۳‬‬                                       ‫آزسمان است‪.‬‬
                                                                                    ‫های هوز؛ کنابه ا‬
‫بااف کشیده ‪ .‬به‌عنی سبزقب) است‪ .‬وآن مرغی‬
‫باشد بز برخی مایل و تاح‌دار‪,‬و باتشدید رای‬                ‫سبز راع = با زای هوز بر وزن مبز‬
                                                        ‫را نیز‬        ‫سستم‪ -‬و‬
                                                                     ‫ان‬         ‫باغ ک‪۰‬نابه از‬
                                                                            ‫آدنیا‬
                  ‫فرشت (‪ )۳‬هم بنظار |عده هن‬
                                                                                                     ‫گویند ‪.‬‬
‫د بمعنی سز کارگاه است‬      ‫سبز کو شك‬
                                                        ‫‪ -‬کنابه از فلك‌است که‬       ‫سبز طاوس‬
                       ‫که کتانه ار اسان اشد‬
                                                                                              ‫آسمان‪:‬ناقه‪::‬‬
                                                        ‫سیز طشت ‪ -‬بمعنی سبزخوان است که‬
‫سیز ها ند ر سز ه ‪ = 5‬یمعنی سبزأندر‬
```


## [2026-09-04T22:48:21.402Z] TOOL CALL #43: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1086 --image 2>&1 | head -60",
 "description": "Render BQT page 1086"
}
```


### [2026-09-04T22:48:23.321Z] TOOL RESULT

```
no scan of BQT covers printed page 1086 (see 'scans' in refs_online.json)
```


## [2026-09-04T22:48:28.016Z] TOOL CALL #44: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1)[:3000])\n\"",
 "description": "BQT record details"
}
```


### [2026-09-04T22:48:30.427Z] TOOL RESULT

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
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT
```


## [2026-09-04T22:48:52.325Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(538,549):\n    p=pages[i]\n    nums=re.findall(r'[۰-۹]{3,4}',p)\n    first=p.strip().split('\\n')[0][:80]\n    print(i, nums[:6], '|', first)\nEOF",
 "description": "BQT v2 running heads"
}
```


### [2026-09-04T22:48:54.462Z] TOOL RESULT

```
538 ['۱۸۴', '۱۸۳'] | ‫اس‬      ‫‪۷۵‬‬                                                                
539 ['۰۸۳', '۳۵۱', '۵۳۲', '۶۱۸'] | ‫ساو‬                                                                           
540 ['۲۳۱', '۷۹۳', '۰۴۱'] | ‫ه‬
541 ['۸۹۲', '۰۹۹'] | ‫سابه خوش‬                                                                      
542 ['۷۳۲'] | ‫‪«۹‬‬                                                                          
543 ['۲۸۳', '۲۲۲', '۹۲۱'] | ‫—‬   ‫‪0‬‬
544 ['۳۹۱', '۸۷۱', '۹۸۲', '۲۸۱۰'] | ‫‪ ۷‬با ‪— ۵‬‬
545 ['۲۳۳', '۰۲۰۱', '۰۲۹۲', '۷۳۵', '۱۹۲', '۵۰۳'] | ‫ره باس‬
546 [] | ‫زا‬                                                                            
547 ['۹۹۹', '۷۲۱', '۵۵۱', '۷۲۱', '۸۸۲'] | ‫سڀار‬                                                                          
548 ['۸۹۱', '۵۰۲', '۷۹۹', '۱۳۱'] | ‫رک ها‬
```


## [2026-09-04T22:49:01.559Z] TOOL CALL #46: Bash

```json
{
 "command": "ls data/verification/ | head -40; echo \"---\"; grep -ho '\"ref\": \"BQT:[0-9]*\"[^}]*' data/verification/page-*.json 2>/dev/null | head -20",
 "description": "Existing verification files"
}
```


### [2026-09-04T22:49:01.615Z] TOOL RESULT

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
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
page-51.json
page-52.json
page-53.json
page-54.json
page-55.json
process
sources
---
"ref": "BQT:103",
"ref": "BQT:58",
"ref": "BQT:58",
"ref": "BQT:944",
"ref": "BQT:944",
"ref": "BQT:1077", "status": "supports", "note": "Borhān-e Qāṭeʿ vol. 2 (BQT_v2_pages.txt, leaves 539-540, printed pp. ≈1076-1082 — the offset is independently pinned by Aryanpur, who cites 'برهان قاطع: ۱۰۷۶-۷' under the very same headword سان): 'سان ... مطلق سوهان را نیز گفته‌اند ... و فسان را گفته‌اند و آن سنگ باشد که کارد و شمشیر و غیره بدان تیز کنند' ('sān ... also used absolutely for a file (sūhān) ... and they say fasān, which is the stone on which knife and sword are sharpened'), and on the next leaf 'سای ... فاعل ساییدن را گویند که ساینده باشد' ('sāy: the agent of sāyīdan') and 'ساو ... بمعنی مطلق سودن و ساییدن باشد'. Exactly the node's words and the chart's extra forms سای، ساو، سان، سوهان."
"ref": "BQT:1488", "status": "supports", "note": "Fetched with tools/ref_page.py BQT:1488 (vol. 3 pdf p.281; cached at data/verification/sources/refs/ocr/BQT/1488.png|.txt): 'فسان ← بفتح اول بروزن زبان، سنگی باشد که کارد و شمشیر بدان تیز کنند' ('fasān: a stone on which knife and sword are sharpened'), 'فسانیدن ← بر وزن رسانیدن، بمعنی مالیدن و راست کردن' ('fasānīdan: to rub and make straight'), with Moʿin's footnotes 'رك: افسان، ارسان، سان' and '۸ از: فسان (سنگ) + یدن (پسوند مصدری)', plus Farroḵi Sistāni's line 'چه حاجتی بفسان روز رزم تیغ تو را'. Supports both fasān and fasānīdan and Nourai's spelling variant افسان."
"ref": "BQT:2407",
"ref": "BQT:750",
"ref": "BQT:218",
"ref": "BQT:218",
"ref": "BQT:212",
"ref": "BQT:219",
"ref": "BQT:1225",
"ref": "BQT:918",
"ref": "BQT:851",
"ref": "BQT:359",
"ref": "BQT:1455",
"ref": "BQT:1997",
"ref": "BQT:1981",
```


## [2026-09-04T22:49:18.888Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN bi ===\"; grep -n \"^ *[0-9]*\\. *bi \\|bi 'ohne'\\|,ohne'\\|bi-dester\\|bidester\\|bidastar\" HRN.txt | head -20; echo \"=== HRN avard/afrin ===\"; grep -n \"äfrin\\|afrin\\|ävard\\|avard\\|äverd\" HRN.txt | head -20",
 "description": "Horn bi, afrin, avard"
}
```


### [2026-09-04T22:49:18.952Z] TOOL RESULT

```
=== HRN bi ===
=== HRN avard/afrin ===
776:39. äfvtden ^schaffen, Praes. afrin-em, afrUegär (AM.);
2109:mäz. bavarden^ gel. barden.
18378:m. bavarden 196.
19288:)iavarde 1078.
```


## [2026-09-04T22:49:22.337Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '770,790p' HRN.txt; echo \"=== HRN 'ohne' ===\"; grep -n \"ohne'\" HRN.txt | head -20",
 "description": "Horn no.39 afriden"
}
```


### [2026-09-04T22:49:22.397Z] TOOL RESULT

```
FR, FJ, Metrum Muteqärib:
b^r esb-i gümän ez reh-i räst^ x^m
q^räret bedöze-^ büved bäj^dum
Esedl.— 10 -
aw. *up((tama' letzter ; phlv. afdiim, päz. awdum
'letzter.
39. äfvtden ^schaffen, Praes. afrin-em, afrUegär (AM.);
afrtn 1) 'schaffend' 2) 'Lob', vergl. nefnn 'Fluch'.
aw. afrmami 'ich preise' etc., äfrlna- 'Segen'; phlv.
äfritan 'schaffen', afrm 'Lob', nafrm 'Fluch' (AV.);
ai. Ä + i^prT' 'befriedigen' etc.
Die Bedeutung 'schaffen' geht nicht über das Pehlevl
hinaus. Oder zwei ganz verschiedene Verba?
40. ägäh, kundig, Kunde'.
aw. ä + i^kas-, äkasat er erblickte'; phlv. äkäs, äkäslh^
äkäsimtan, arm. LW. akah 'kundig'; ai. Kiä^-, ka^ate
'sichtbar sein, erscheinen, überblicken'.
afy. bei. LW. ägäh.
41. ägenden 'anfüllen', ägenis^ ägm 'voll'.
skr. ghana- 'dick, voll von etwas', m. 'Klumpen',
ähandS' 'schwellend, strotzend'; vergl. lit. (/awd 'genug,
=== HRN 'ohne' ===
2523:247. be, ehe 'ohne'.
2626:np. be- *ohne' sei, könnte man nach sar. LW. bhnar
8306:ai. mäsa- 'Bohne'; sar. ma/ Erbse*.
```


## [2026-09-04T22:49:33.478Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== around 760-776 ===\"; sed -n '755,776p' HRN.txt; echo; echo \"=== 247. be ===\"; sed -n '2520,2545p' HRN.txt; echo; echo \"=== 2620-2640 ===\"; sed -n '2618,2640p' HRN.txt",
 "description": "Horn afdum and be entries"
}
```


### [2026-09-04T22:49:33.545Z] TOOL RESULT

```
=== around 760-776 ===
(Jaba-Justi).
38. äfdutn 'letzter', nur im Mujmil ettevärT;^ (ed. Mohl,
Journ. asiat. 1841, S. 178)^), vergl. hafdum zuletzt*^).
«) Hübschmann, ZDMG. 38, 431.
') Bartholomae, Arische Forsch ungren II, 102.
*) Dazu wohl auch äyisten, z. B. AM. 14 Zeile 16, 193 Zeile 11.
do Lagarde, Ges. Abh. 290 ist natürlich unmöglich.
*) Vergl. Spiegel, Grammatik der- Huzväresch-Sprache, 76.
^) Für bäfdum (d. i. be äfdum) haben die Wörterbücher folgende
Belegstellen: SF (S. 95 Vers 53), Metrum Remel:
kär-i dänä nek^ gerded bäf^dum
FR, Metrum Muteqärib:
ci bäyedf kerden kenün bäf^dum
meger -j^äne-röbl cü robeh bMum
Abu SukUr.
FR, FJ, Metrum Muteqärib:
b^r esb-i gümän ez reh-i räst^ x^m
q^räret bedöze-^ büved bäj^dum
Esedl.— 10 -
aw. *up((tama' letzter ; phlv. afdiim, päz. awdum
'letzter.
39. äfvtden ^schaffen, Praes. afrin-em, afrUegär (AM.);

=== 247. be ===
LW. kurd. behist.
Die Aussprache behist ist die ursprüngliche ; in bihist
ist der erste Vokal dem zweiten angeglichen.
247. be, ehe 'ohne'.
phlv. ape- (päz. atve-)^ z. B. ape'\htm, ape]vnäs etc.,
be (ZPGl.), vergl. arm. LW. ape]niaz,
kurd. af/. bei. LW. bt- resp. he-.
*) Fr. Müller, WZKM. 5, 186, Anm. vergleicht aw. vahhana'
*Kleid\ was ganz unwahrscheinlich iat.- 57 ~
Eine über das Pehlevi hinausgehende iranische Form
kommt nicht vor ; ape resp. ii12 stehen im PehlevT für
die verschiedensten Praepositionen des Awestatextes,
z. B. für vi {vi)y para^ paiti u. a. m.
Wohl ein Casus zur Praeposition apa getrennt, fem
von', vergl. gr. anai, das allerdings selbst sehr zweifel-
haft ist; vergl. aber gr. xar«/, napai, vnai bei Homer
(6. Meyer, Griechische Grammatik ^ § 351).
Fr. Müller's Erklärung (Beeinflussung durch vi) in
der WZKM. 5, 256 ist nach meiner Ansicht verfehlt;
arm. api-j das Müller dazu stellt, wird aber herge-
hören.
248. biyäbän Wüste.
g. vläbün.
aw. vergleicht man viväp- 'wasserlos' ; phlv. viijäpän^
viyäpamh (Y. 13, 8, 12).
Die Ableitung von aw. vioäp- ist alt, aber lautlich

=== 2620-2640 ===
39. bimär 'krank^^ bimürJ.
aw. v% ■-\;- v^war-) (vergl. vJ-merencalt^); phlv.
vimär, vlmärlh (Men.), virnärinltan (y. 30, 6 nach
Darmesteter's Correctur, Et. ir. II, 138).
Die Etymologie ist gewiss falsch, da altes vi- im
Neupersischen consequent zu gu- wird, und selbst bei
Annahme eines Ausnahmefalles (z. B. biüer^ No. 218)
das i völlig unerklärt bliebe. Dass das erste Glied
np. be- *ohne' sei, könnte man nach sar. LW. bhnar
(d. i. bemar) vermuten; doch erhält man bei dieser
Ableitung keinen guten Sinn. Bartholomae schlägt
mir die Etymologie upai (s. No. 247) + mära-y also
*am Tode' vor, aber dafür spricht nicht das phlv. v
(oder auch w),
30. bin *sehend', hin-em^ binä^ bmis,
ap. vainähiy Conj. (Venn) du siehst'; aw. vaenämi
*ich sehe'; phlv. ven-am, ven(i)sn^ venäk^ venastan (päz.
vm-), vergl. üben (vd. 19 (43)).
af/. vm-am; oss. d. mmin, t. ünin (82); wa;^. §iyn.
viti-am, sar. veln-am.
*) Gul. (Sprenger) S. 26 Zeile 8 reimt es ausnahmsweise auf piL— 60 —
261. Mm 'Nase.
Semn. vlm; mäz. v^it,
```


## [2026-09-04T22:49:49.451Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 'Kampf' entries ===\"; grep -n \"Kampf\" HRN.txt | head -20; echo \"=== HUB 247 / 38 ===\"; grep -n \"^ *247\\.\\|^ *38\\.\\|ape-\\|apS-\" HUB.txt | head -20",
 "description": "Horn Kampf; Hübschmann"
}
```


### [2026-09-04T22:49:49.509Z] TOOL RESULT

```
=== HRN 'Kampf' entries ===
1718:ai. vergl. vdja-^ väjäyati (spec. von Kampf spielen) 2);
3393:360. peikär, peigär *Kampf'.
3395:phlv. patkär 'Kampf (z. B. vd. 5 (33) GL), patkäritan
3397:arm. LW. payUar *Kampf' .
5467:612. rezm 'Schlacht, Kampf.
5469:'Kampf, auch razm.
6326:722. fiite^ *Kampf, Krieg*, süeziden,
6327:aw. vergl. stij- *Kampf, Streit'; phlv. stej 'Kampf*
7244:834. kär[»är 'Kampf, Schlachtfeld*, vergl. karJ 'Kämpfer.
8510:(AV.); ai. midhd- 'Kampf, Wettkampf; got. mizdö
8899:1025. neberd "Kampf, newerd, neberde 'tapfer (Sahn. I, 93
8902:n{i)part "Kampf (AV.).
8903:Vergl. np. äwerd "Kampf (Sahn. I, 218 Vers 1506),
=== HUB 247 / 38 ===
150:38. Man mtisste lautgesetzlich afdum erwarten. „Viel-
1096:247. Np. he = paz. atvS, phi. apB setze ich = ap. *apaiy
4180:be- *ohne* in Komp. = paz. awe-, phi. ape-, arm. ape-,
6233:be. abe ohne = phi. ape- ; bumd *Jungling , zd. aperen-
```


## [2026-09-04T22:49:53.330Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 1025 neberd ===\"; sed -n '8896,8915p' HRN.txt; echo; echo \"=== HUB 247 ===\"; sed -n '1093,1112p' HUB.txt; echo; echo \"=== HUB 38 ===\"; sed -n '146,160p' HUB.txt",
 "description": "Horn neberd/awerd; Hübschmann be, afdum"
}
```


### [2026-09-04T22:49:53.412Z] TOOL RESULT

```
=== HRN 1025 neberd ===
Buchstaben auf dem Steine.
«j Vergl. Bartholomae, BB. XVII, 132.230 —
V
1025. neberd "Kampf, newerd, neberde 'tapfer (Sahn. I, 93
Vers 586).
aw. *ni -r l/^parU^ peretente sie kämpfen'; phlv.
n{i)part "Kampf (AV.).
Vergl. np. äwerd "Kampf (Sahn. I, 218 Vers 1506),
äwerdgäh (häufig), äweriden,
1025*»*« nebld, nebtd 'Fruchtsaft, Wein »).
ap. ^nipita- 'Trank', vergl. ai. pltd- etc. (Nöldeke,
mündliche Mitteilung) 2).
nehire "Enkel' siehe unter newade (No. 1047).
1026. ner, nerr (AM.) "Mann; männlich', nere [nerre), nenne
"männlich*.
aw. naV' "Mann ; phlv. war; ai. när-,
kurd. ner 'männlich'; afy. nar\ oss. d. nale, t. nal
'Männchen von Tieren' (197) ; bei. nar 'männlich'
(258); sangl. narak.
1027. nirx, nerx "Preis, Wert' (z. B. Schefer, Chresto-

=== HUB 247 ===
durch 'revenue' und stellt es zu bhaj *teilen, zuteilen*,
vgl. ap. baji' *Tribut'. So wird auch np. 6aAr = barx
= zd. baxdra- sein.
247. Np. he = paz. atvS, phi. apB setze ich = ap. *apaiy
aus apa + id, wie naiy nicht' = fia + id (skr. ned)
ist. Die Form ist in der Composition entstanden, sonst
ware *apaii/ zu np. ab geworden. Im Phi. und Pazend
findet sich apS, awS nur als 1. Glied von Compositis,
wie auch im Neupersischen bS noch moistens in Com-
position erscheint.
249. Zu beoctan *sieben' (nach Noldeke *streuen) stellt
Geiger jetzt afgh. mnjql reinigen, saubern, waschen'.
Als Lehnwort gehSrt dazu afgh. badpBzt 'Absurditat
(== Windsieberei nach Raverty) sowie bSzql, pSzql
sieben, Geiger, Etym. und Lautl. d. Afghan. Nr. 360.
250. Zu bddbe»9 badbSzan u. s. w. Tacher' vgl. Journ.
asiat. 1893, p. 256.
251. Dazu afgh. vala 'Weide* (nach Geiger), als Lehn-
wort afgh. bSd *Weide'.
252. Vgl. dagegen Darmesteter, Etud. iran. I, 281, der

=== HUB 38 ===
leicht zur Wurzel sad *sitzen' gestellt werden konnte.^)
Vgl. np. nisastan *sitzen' und nis^m *Nest'. v. Stackel-
berg denkt an osset. axston (aus dxs-don oder dxst-don)
'Nest', NSldeke jetzt an skr. a-ksi Veilen.
38. Man mtisste lautgesetzlich afdum erwarten. „Viel-
leicht war das Wort schon zur Zeit der altesten neu-
V
persischen Dichter (Abu Suktir!) veraltet und wurde
falsch ausgesprochen." No Id eke.
42. Np. dludan *beschmutzen, sich verunreinigen* kann
trotz des pr. olayam auf eine Wurzel lu zuriickgehen,
wie situdan, pr. sitayam (Horn Nr. 719) zeigt. Man hat
dann dlayam auf ein caus. *alavayami zuriickzufuhren.
Phi. lutaJc wird (Gl. and Ind. p. 139) durch nackt* iiber-
setzt, obwohl 'schmutzig' besser passt. Lautlich ist
```


## [2026-09-04T22:50:09.579Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ā prep\\|^à prep\\|^ā prev\\|^d prep\\|prefix ‘to\\|prep. and prefix ‘to\" KNT.txt | head; echo \"---\"; grep -n \"âyadana\\|ayadana\\|à-yada\\|ā-yadana\" KNT.txt | head -5; echo \"=== POK e/o particle ===\"; grep -n \"^ē, ō\\|^e, o \\|^ě, ō\" POK_01.txt | head",
 "description": "Kent ā preverb; Pokorny ē/ō"
}
```


### [2026-09-04T22:50:09.651Z] TOOL RESULT

```
5012:abiy prep. and prefix ‘to, against, in addition to’: GAv. aibi. LAv. aiwi, Skt. abht; conflux of pIE *mbhi, oHG umbi ‘round about’, and pIE *obhi, oCS ой ‘beside, by’.
5178:ира (i.e. upd, cf. 5140.1) prep. and prefix ‘to- ward’: Av. ира, Skt. úpa, Gk. iad, Lt. s-ub ‘under’, pIE “иро.
---
=== POK e/o particle ===
```


## [2026-09-04T22:50:14.488Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ä prep\\|^â prep\\|^a prep\\|^ā-\\| à \\b\" KNT.txt | sed -n '1,10p'; echo \"===\"; grep -n \"Skt. ā́\\|Skt. à ‘\\|Skt. d ‘to\\|‘to, unto’\\|‘unto, to’\" KNT.txt | head; echo \"=== search lexicon entry a- ===\"; awk 'BEGIN{RS=\"\\f\"} NR==188' KNT.txt | head -40",
 "description": "Kent lexicon ā entry"
}
```


### [2026-09-04T22:50:16.282Z] TOOL RESULT

```
184:V. Scheil, Inseriptions des Achéménides à Suse, in Mémoires de la Mission Archéologique de Perse, tome xxi; Paris 1929. The inscriptions, with English translation and partial vocabu- lary, are repeated by J. M. Unvala, The Ancient Persian Inscriptions of the Achae- menides found at Susa, Paris 1929.
228:Rec. Trav. = Recueil de Travaux relatifs à la philologie et à l'arehéologie égyptiennes et assyriennes.
285:Scheil 21 = V. Scheil, Inscriptions des Achémé- nides à Suse, in Mémoires de 1а Mission archéologique de Perse, tome XXI, Mission en Susiane; Paris 1929.
486:$21. Tue REPRESENTATION OF a IN OP Writ- inG. The character а at the beginning of a word represents either d or d, and decision must be made on etymological and morphological grounds. Elsewhere in the word the character a is used only after an a-inherent character, the value being à; thus m'am*a = пата. When the a-con- stant is immediately followed by another con- sonant, or is final, the a of the consonant either represents d or has no value at all; thus dsm? . = daríam. For a or à in diphthongs, see $24: for
545:$29. Тнк Persistence OF VoweL y into ОР! makes difficulties in the normalization. The nor- malized form of some words containing т is certain: thus дт in the month-name Garma- pada- might theoretically be grama- or garama- or grma-, but is actually garma-, a form assured by etymological cognates. The name атат is Тата, though the characters might equally well stand for Атёйта; and those who would normal- ize with r as à vowel write ’rSdéma, using the sign for the glottal stop to represent the character which elsewhere has the vowel value a. But in £r^m*i3^ we have no clue to the vowel of the first syllable; it may be &arm:$ ог багата or 0pmió (though hardly 6rami$, since ør became с). То avoid the necessity of making decisions in cases where there is no evidence, the normalization here employed is ar alike for phonetic ar and for phonetic 7, and for those instances where we do not have proof of the value, which may also be ara or та.
617:П. But graphic final à represents regularly also any absolutely final à or any à followed by an unwritten minimal final consonant (840): pilta = pitä, Skt. pita; napa = парӣ’, Skt. ndpat; abl. Рата = Püarsü?, Skt. abl. -dd; прі. {уй = tyä, Skt. tds.
675:A. The vowel character a initial becomes (nor- malized) @ or à, or the prior part of a diph- thong & or йи: medial, à or the prior part of di du: final, à.
695:Lack of ? after à consonant with inherent a, to denote 7; $22. : |
889:I. The vowels à f i a7 and the diphthongs ği ài du du, may occur anywhere in the word; there are extant examples initially of & à 1 ùr ği du, medially of all, final of à $ ? 4 ği du.
955:П. When final in the word, pIE т and m beeame pAr. a, which of course was written à in OP ($36.1): асс. *nomn ‘name’, OP nama, Skt. пата, Lt.
===
=== search lexicon entry a- ===
t built, unrepaired’; neg. a- + pte. of kar- ‘make’. {akarta] nsf. DSe 47 (conj. of Kent, JAOS 54.43).
azíaina- adj, with kdsaka-, ‘turquois’ (so Bleichsteiner, WZKM 37.103-4, and Konig, Burg- bau 63-4, but considered dubious by Hinz, ZDMG 95.235-6; hardly ‘gray amber’, with Hz. AMI 3.05—7, ApI 232; not ‘hematite’, with Scheil 21.29- 30): Av. arSaéna- ‘dark-colored’, borrowed in Gk. Порто “Atevos ‘Black Sea’ (‘in-hospitable’, by Gk. popular etymology, and euphemistically changed to Еф о), from neg. a- + z&atna-, cf. Av. xSaéta- ‘shining’ (§102, 5147.1). azšaina nsm. DSf 39.
axsata- adj. ‘unhurt, undisturbed’: neg. a- + pte. of xSan- ($102, §242.1), Skt. ksanóti ‘injures’, Gk. ктен, ‘kills’ (otherwise Foy KZ 35.49, Hz. Apl 70-1). azšałā nsf, DPe 23.
aguru- sb. ‘baked brick’ (8158.1). lagurum] asm. DSf 53, supplied by König, Burgbau 52, after a-gur-ru of the АКК. text, ef. NPers. ágür in the same meaning. alg|ura[và] Ism. DB 4.89 (restored by Kent, JAOS 62.267, after König, Klotho 4.45); but read амуй аһа with Cameron.
agriya- adj. ‘topmost, excellent, loyal’: Av. ayrya- ‘first in quality, etc.’, Skt. agriyd- agryd- ‘foremost, principal, etc.’, deriv. ($144.1V) to Av. ayra ‘der erste, oberste; (nt.) Anfang, Spitze’, Skt. dgra- ‘foremost, prominent, best; (nt.) tip, sum- mit, best part’ ($148.I). agriya пет. DB 1.21, as read by Cameron, replacing KT’s ag*r^ ++ (and the restorations thereof: dgar[ia] Wb. ZDMG 61.725, Tm. Vdt. Stud. 1.9, ef. Bthl. WZKM 22.72; ágra"|6a] Jn. Indian Stud. Lanman 255-7; ügr[mata] Konig, RuID 65; ágr[mà] Hz. Арі. 59- 62).
aciy adv. ‘then, at that time’ ($291.1V): Av. ajčit ‘and indeed’, Lt. ecquid (interrog.) ‘anything’, pIE *ed-g*id, see *a- ‘this’ and particle -cty ($105, $130; Ву. BSLP 33.2.152-3; Hz. AMI 4.125-6, 8.41, ApI 55-6; Wb. ЖА 41.319). ХРЇ 21.
Atamaita- sb. ‘Atamaita’, an Elamite rebel: Elam. Atameta (854.I, §76.V; Hüsing ар. Prašek,
166
IMP 2.78.08; König, Кир 78; not Umamaita after the Ummaima of Oppert, Médes 158, based on Rawlmnson’s J-im"im*^, later altered by KT's тт). {[Ajtamacta nsm. DB 5.5.
_ ütar- sb. ‘fire’: Av. diar- dór-, NPers. абат; in Á ciyadiya- and verhaps in Acina- ($152.Г).
atar (i.e. ачат), prep. with ace., ‘within, among’: Av. antara, Skt. antar, Lt. inter, pIE tenter (831). DB 1.21; 2.78; 4.32, 92; XPh 30, 35.
ali-, prefix, ‘beyond, across’: Av. aiti, Skt. dti, Gk. ёт ‘yet, longer’, Lt. et ‘and’, pIE *eti ; with ay-, yam-. Cf. also айту.
abaga- (ie. аба"да-) sb. ‘stone’: Av. asanga-, NPers. säng, cf. OP asan-, asman- (S87, S151, $155.1); see also a(againa-. afagam asm. DSf 24, 48.
abagaina- (Le. aba^gaina-) adj. ‘of stone’: deriv. of абада- (147.11), perhaps with vriddhi (§126; déagaina-?). alagaina nsm. DPe. abagainam asm. D'Sa 1; A*Hb. afagainüm asf. ASe 6; abagandm asf. (852. VI) for nsf. (856.V) A’Pa 22. afagainiya прі. (S152.IT, $179.11, $190.I; JAOS 53.20; wrongly Konig, Burgbau 68; not abagainiy nsf. to sg. collective stind, as taken by Hz. AMI 3.68) DSf 45.
Gahavaja, word of unknown meaning, DB 4.90 (reading of KT); hardly, with Morgenstierne, Acta Or. 1.252, d@a*ha-vaja ‘word, speech of proc- lamation’, ef. Skt. aqsd- ‘hope, expectation’, + vacas- ‘word’. Perhaps G@aha- (§143.1; with Morgenstierne) + root-noun vaj- ($142) ‘procla- mation-strengthener, seal’, gsm. (JAOS 62.268; not abl. as instr., with Konig, Klotho 444—5).
abiy prep. with acc. ‘to’: DB 1.91. Apparently doublet to айу (Ву. Gr. §102), possibly by con- tamination of *a; antevocalic and ati antecon- sonantal, in sandhi ($80; Mt. Gr. $103).
Aéiydbausna- sb. ‘Athiyabaushna’, father of Arsaces ($168.11): cpd. of (Av.) ai- ‘destruction, misfortune’ + pass. pte. of d-baug- ‘to free’ ($248) with late -šn- from -aén- (Bv. BSLP 29.2.104, cf. Av. pouru-baozóna- ‘bringing abundant rescue, Bthl. AiW 901): ‘Freed from misfortune’ ($160.14; not active ‘bringing freedom from misfortune
```


## [2026-09-04T22:50:26.552Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^apo-\\|apo- *Off, away\" AHD_watkins1985.txt | head; echo \"---\"; grep -n -A25 \"^apo-\" AHD_watkins1985.txt | head -50",
 "description": "AHD Watkins apo-"
}
```


### [2026-09-04T22:50:26.625Z] TOOL RESULT

```
---
```


## [2026-09-04T22:50:29.262Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"apo-\" AHD_watkins1985.txt | head -20",
 "description": "grep apo- in AHD"
}
```


### [2026-09-04T22:50:29.306Z] TOOL RESULT

```
280:al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
285:POSTICHE, POSTURE, PREPOSITION, PROPOSE, PROVOST, REPOSIT, SUPPOSE. [Pok. apo- 53.]
1052:swer-'. To speak, talk. O-grade form *swor- in: a. Ger- manic *swarjan in Old English swerian, to swear, pro- claim: SWEAR; b. Germanic “*and-swar6, “a swearing against,” “rebuttal” (*andi-, against; see ant-), in Old English andswaru, answer: ANSWER. [Pok. 1. swer- 1049.] swer-2. To buzz, whisper. Imitative root. I. O-grade form *swor-. 1. Suffixed form *swor-mo- in Germanic *swar- maz in Old English swearm, swarm: SWARM. 2. Germanic *swar- in Dutch zwirrelen, to whirl, akin to the Low German source of Middle English swyrl, eddy: SWIRL. II. Zero-grade form *sur-. 1. Suffixed form *sur-do- perhaps in: a. Latin surdus, deaf, mute: SORDINO, SOUR- DINE, SURD; b. Latin absurdus, discordant, away from the right sound, harsh (ab-, away; see apo-): ABSURD. 2. Reduplicated expressive form *su-surr- in Latin susur- rus, whisper: SUSURRATION. [Pok. 2. swer- 1049.] swer-3, Post, rod. Suffixed zero-grade form *sur-o- in Latin surus, branch: SURCULOSE. [Pok. 3. suer- 1050.] swer-4. To cut, pierce. Germanic *swerdam in Old Eng- lish sweord, sword, sword: sworD. [Pok. 4. suer- 1050.] swer-5. Also ser-. To lift, hang on the scale; heavy. Variant *ser- in suffixed lengthened-grade form *sér-yo- in Latin sérius, serious, grave: SERIOUS.
1148:wer-5. To cover. I. Basic form *wer-. 1. Germanic *wer- jon- in Old English wer, dam, fish trap: WEIR. 2. Com- pound form *ap-wer-yo- (*ap-, off, away; see apo-) in Latin aperire, to open, uncover: APERIENT, APERITIF, APERTURE; OVERT, OVERTURE, PERT. 3. Compound form
1207:4-1 ne AARDVARK  er-2, porko- AARDWOLF er-2, wikwo- AB-!  apo-
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1218:AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE aiw- AGENDUM ag- AGENT ag- AGERATUM gere-1 AGGLOMERATE gel-1 AGGLUTINATE gel-1 AGGRAVATE gWere-2 AGGREGATE ger-? AGGRESS ghredh- AGGRIEVE gWere-2 AGHAST gheis- AGILE ag-
1253:APO- apo- APOCALYPSE kel-2 APOCOPE skep- APOCRINE krei- APOCRYPHA krau- APODAL ped-! APODICTIC deik- APODOSIS do- APOGEE gé APOLOGUE leg-1 APOLOGY leg-! APOMIXIS meik- APONEUROSIS (s)neau- APOPHYGE bheug-! APOPLEXY plak-2 APOSIOPESIS sWi- APOSTASY sta- APOSTLE stel- APOSTROPHE! streb(h)- APOTHECARY dhé-1 APOTHECIUM dhé-1 APOTHEOSIS dhés- APOTROPAIC trep-2 APPALL pel-2 APPANAGE pa- APPARATUS pere-1 APPAREL pere-! APPEAL pel-6 APPEASE pag- APPEND (s)pen- APPENDIX (S)pen- APPETITE pet- APPLE abel- APPLY plek- APPOGGIATURA ped-1 APPOSITE apo- APPOSITION apo- APPRAISE per-6 APPRECIATE per-6 APPREHEND ghend- APPRENTICE ghend- APPRESSED per-5 APPRISE ghend- APPROACH per! APPROPRIATE pert APPROVE per! APPROXIMATE per! APRICOT pekw- APRON mappa APT ap-!
1271:AUTOPSY OkW- AUXESIS aug-! AUXILIARY aug-! AUXIN aug-! AVAIL wal- AVAST  kel-3, past- AVATAR auc’, tera-? AVENGE deik- AVENUE gWa- AVER wéro- AVERT wer-3 AVIAN awi- AVIARY awi- AVIATION awi- AVICULTURE awi- AVIFAUNA awi- AVOCATION wekW- AVOID eu-2 AVULSE wel-4 AVUNCULAR awo- AWARE wer-4 AWAY wegh- AWE agh-1 AWKWARD apo- AWN ak-
1387:COMMODITY med- COMMON mei-! COMMOTION meue- COMMUNE mei-1 COMMUNICATE mei-1 COMMUNISM mei-1 COMMUTE mei-1 COMPACT! pag- COMPANION pa- COMPANY pa- COMPARE pera-2 COMPART pere-2 COMPASSION pé(i)- COMPEL pel-6 COMPELLATION pel-6 COMPENDIUM (s)pen- COMPENSATE (s)pen- COMPETE pet- COMPLACENT plak-! COMPLAIN plak-2 COMPLECT plek- COMPLETE pele-1 COMPLEX plek- COMPLICATE plek- COMPLICE plek- COMPLIMENT pele-1 COMPLY pele-1 COMPONENT apo- COMPORT per-2 COMPOSE apo-, paus-, COMPOSITE apo- COMPOSITION apo- COMPOUND apo- COMPRADOR pere-1 COMPREHEND ghend- COMPRESS per-5 COMPRISE ghend- COMPROMISE (s)meit(9)- COMPUNCTION peuk- COMPURGATION peue- COMPUTE peu- COMRADE kamer- con! kom
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1440:EAVES upo EAVESDROP upo EBB apo-
1442:EDIBLE ed- EpicT deik- EDIFICE aidh-, dhé-1 EDIFY aidh-, dhé-1 EDITION d6- EDUCATE deuk- EDUCE deuk- EFFACE dhé-1 EFFECT dhé-1 EFFEMINATE dhé(i)- EFFERENT bher-1 EFFERVESCE bhreu-2 EFFETE dh@(i)- EFFICACIOUS dhé-1 EFFICIENT dhé-1 EFFIGY dheigh- EFFLORESCE bhel-3 EFFLUENT bhleu- EFFLUVIUM bhieu- EFFLUX bhlieu- EFFORT bhergh-2 EFFULGENT bhel-1 EFFUSE gheu- EFTSOONS apo- EGEST gerere EGG! awi-
1487:EXPOSTULATE prek- EXPOUND apo- EXPRESS per-5 EXPUNGE peuk- EXPURGATE peue- EXQUISITE quaerere EXSCIND skei- EXSECT sek- EXSICCATE seikw- EXTANT sta- EXTEND ten- EXTENUATE ten- EXTERIOR eghs EXTERMINATE ter- EXTERNAL eghs EXTINGUISH  steig-
1673:ILLATION tele- ILLITERATE deph- ILLUMINATE leuk- ILLUSION leid- ILLUSTRATE leuk- IMBECILE bak- IMBIBE p6(i)- IMBRICATE ombh-ro- IMBRUE_bhreu-2 IMBUE ombh-ro- IMMACULATE macula IMMANENT men-3 IMMATURE ma-1 IMMENSE mé6-2 IMMERSE mezg-! IMMINENT men-2 IMMIX meik- IMMODERATE med- IMMODEST med- IMMOLATE mele- IMMORTAL mer-2 IMMUNE mei-1 IMMURE mei-3 IMP bheue- IMPAIR ped-1 IMPALE pag- IMPARITY pere-2 IMPART pere-2 IMPEACH ped-1 IMPECCABLE ped-1 IMPECUNIOUS peku- IMPEDE ped-! IMPEL pel-6 IMPEND (s)pen- IMPERATIVE pere-1 IMPERIAL pere-1 IMPETRATE peter- IMPETUS _pet- IMPINGE pag- IMPIOUS pius IMPLEMENT pele-1 IMPLICATE plek- IMPONE apo- IMPORT per-2 IMPORTANT per-2 IMPORTUNE per-2 IMPOSE apo- IMPOTENT poti- IMPOUND bend- IMPRECATE prek- IMPRESS! per-5 IMPRIMIS_ per! IMPRINT per-5 IMPROBITY pert IMPROMPTU em- IMPROVE es-, pert IMPUDENT (s)peud- IMPUGN peuk- IMPUNITY kweij-1 IMPUTE peu- IN-l ne
1682:INTER en, ters- INTERCALATE kela-2 INTERCEDE ked- INTERCEPT kap- INTERCOSTAL kost- INTERCOURSE kers-2 INTERDICT deik- INTEREST es- INTERIM en INTERIOR en INTERJECT yé- INTERLOCUTION  tolkw- INTERLOPE klou- INTERLUDE leid- INTERMEDIATE medhyo- INTERMIT (S)meit(a)- INTERNAL en INTERNECINE nek-1 INTERPELLATE pel-6 INTERPOSE apo- INTERPRET per-68 INTERREX reg-1 INTERROGATE reg-1 INTERRUPT reup- INTERSECT sek- INTERSPERSE (s)preg- INTERSTICE sta- INTERVAL walso- INTERVENE gWa- INTERVIEW weid- INTESTINE en INTIMA en INTIMATE? en INTINCTION  teng- INTINE en
1959:-ODONT dent- ODONTO- dent- opor od-1 OENOLOGY vinum OENOMEL melit-, vinum OF apo-
1960:OFF apo-
```


## [2026-09-04T22:50:37.180Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && awk 'BEGIN{RS=\"\\f\"} NR==29' FFD_pages.txt | head -50",
 "description": "FFD p.24"
}
```


### [2026-09-04T22:50:38.943Z] TOOL RESULT

```
[pdf page 29]
در شرح ریشه‌شناختی فعلهاء نخست مادهٌ ماضی و آنگاه مادهٌ مضارع آمده است.
گاهی هم نخست مادهٌ مضارع و پس از آن ماده ماضی آورده شده است. در شرح.
صورتهای ایرانی باستان و گاهی همراه با آن» صورتهای فارسی باستان ماده‌ها ذکر شده

آراستن

آراست + فارسی میانه 3738۳ + ایرانی باستان 12 - 739 - 3*. 8 پیشوند فعلی است که
در اصل بر انجام گرفتن کار به سوی متکلم دلالت می‌کرده است. 734 صورت اصلی 739
است. 7 پیش از 1 به 8بدل شده است. 734 به معنی «منظم کردن» است. 18 پسوندی بوده
که از ریشهٌ لازم» صفت فاعلی گذشته, و از ريشهٌ متعدی» صفت مفعولی گذشته
می‌ساخته است.

آرای + فارسی میانه 273 < ایرانی باستان 2 - 734 - 3*. 2 برای ساختن ماده از ريشه
به کار می‌رفته است.

آرامیدن. آرمیدن
«آرامید» مادةٌ ماضی جعلی است» از مادةٌ مضارع ساخته شده است.
آرام < ایرانی باستان 2 - 1308 - 3* برای 8 > آرای. 5 پیشوند فعلی است.
```


## [2026-09-04T22:50:57.013Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt; grep -c \"\" MON_part1.txt; grep -n \"آفدم\" MON_part1.txt MON_part2.txt | head; echo \"=== varun ===\"; grep -n \"وارون\" MON_part1.txt MON_part2.txt | head -5",
 "description": "Mo'in local OCR"
}
```


### [2026-09-04T22:50:57.097Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
99339
MON_part1.txt:3841:آفدم: 07 (ص.) آخرین» سین» نهائی. 
=== varun ===
MON_part1.txt:18048:وارون شدن. آوازه شدن» شهرت یافتن. 
MON_part1.txt:18050:(امص.) باژگونگیء وارونی؛ ج. انعکاسات. 
MON_part1.txt:20512:باشگونه] (ص‌مر.) سرنگون» وارون. 
MON_part1.txt:77446:کردن: (عم.) (کذ.) کار وارونه کردن. 
MON_part1.txt:92539:چنانکه هست يا وارونهٌ آن خواندن.
```


## [2026-09-04T22:51:03.031Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3830,3850p' MON_part1.txt; echo \"=== formfeeds? ===\"; python3 -c \"\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nprint('FF count',t.count('\\f'))\nprint(repr(t[:300]))\n\"",
 "description": "Mo'in afdom context"
}
```


### [2026-09-04T22:51:05.534Z] TOOL RESULT

```
لنگک حمام خشکک و بی‌نم. ظرفی آهنین. 
نوعی کشمش که در افتاب خشکك کنند؛ 
مق. سایه خشک. 

افتومات: 20-80 [خودکار] () (مکن.) 
کلید خودکاری است که جریان برق را بین 
دینام و باتری موقعی وصل می‌کند که ولت 
دینام بالاتر از ولت باتری گردد یعنی فقط 
اجازه می‌دهد که برق از جانب دینام به باتری 
رود ولی اجازة باز گشت نمی دهد. 

آفدم: 07 (ص.) آخرین» سین» نهائی. 
۳ 

افرازه: (0-)5]12322 (۱.) شعله» زبانه؛ لهب. 
افسروزه: ()«حت26 (- افروز] (ا1.) 
فروزینه» گیره» ۳ زنه. فسله چراغ» بلیته. 
افروشه: (6-)2]71152 [- افر وشه ] (ا.) قسمی 
حلوا که از آرد و عسل و روغن يا از زردة 
تخومرع و شیره و شکر سازند» حلوای 
خانگی؛ حلوای سفید» خبیص. بلغور گندم. 
=== formfeeds? ===
FF count 0
'0 \n2 \n\n\nچم \nنسم ی \n\n\nتمه موی موم \n3 \n\n\nماما نا موس ملاس \nروم و3 \n\n\n2 \n7 \nس \n\n\nهمجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 \nادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع \n\nمه مر وه ود \n\n3 ور 133131313 \n\n\nهم مشب جج جب بیج چم مدوجو \nچم وم \nجر \n\n\nدرل ولو ونر نو تلا رت \n'
```


## [2026-09-04T22:51:14.511Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%D9%81%D8%AF%D9%85/",
 "prompt": "Quote the فرهنگ معین (Mo'in) and لغت‌نامه دهخدا entries for آفدم — meaning and any etymological bracket/origin note."
}
```


## [2026-09-04T22:51:15.608Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ab-",
 "prompt": "Give the etymology of the Latin prefix ab- and the entry for abnormal if present: PIE root, Latin ab, cognates (Greek apo, Sanskrit apa, Gothic af, English of)."
}
```


### [2026-09-04T22:51:18.856Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T22:51:21.464Z] TOOL RESULT

```
# Etymology of Latin Prefix *ab-*

## Origin and Development

The prefix *ab-* derives from Latin *ab* (prep.) meaning "off, away from." According to the source, it ultimately traces to the PIE root *\*apo-* "off, away," which also generated related terms across Indo-European languages.

## Cognates

The document identifies these cognate forms:
- **Greek**: *apo* "off, away from"
- **Sanskrit**: *apa* "away from"
- **Gothic**: *af*
- **English**: *of* and *off*

## Latin Development

In classical Latin, *ab-* underwent phonetic reduction: it became *a-* before m, p, or v, and typically *abs-* before c, q, or t.

## Note on "Abnormal"

The provided content does not include a dedicated entry for "abnormal," so I cannot offer etymological details for that specific word based on this source material.
```


## [2026-09-04T22:51:24.557Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.vajehyab.com/moein/%D8%A2%D9%81%D8%AF%D9%85",
 "prompt": "Quote the Mo'in (فرهنگ معین) entry for آفدم: meaning, part of speech, any origin bracket."
}
```


## [2026-09-04T22:51:26.089Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%88%D8%B1%D8%AF",
 "prompt": "Give the Persian entry آورد (āvard): meanings ('battle/combat' and past stem of آوردن) and etymologies for each."
}
```


### [2026-09-04T22:51:29.191Z] TOOL RESULT

```
Based on the Mo'in dictionary entry shown, here is the information for آفدم:

**Meaning:** "(دُ)(ص .)" indicates it is a noun (ص = صفت/adjective marker). The entry defines it as: "1 - آخرین ، نها ی ی" (final, ultimate) and "2 - سرانجام ، فرجام" (end, conclusion).

The concise quote: "آخرین ، نها ی ی" and "سرانجام ، فرجام" convey that آفدم means final/ultimate or end/conclusion respectively.
```


### [2026-09-04T22:51:32.588Z] TOOL RESULT

```
# Persian Entry: آورد (āvard)

## Meanings

Based on the Wiktionary content provided, **آورد** has the following meanings in Persian:

1. **Third-person singular past indicative** of آوردن (âvordan) - the standard formal past tense form
2. **Third-person singular aorist indicative** of آوردن (âvordan) - a less common aspectual variant
3. **Colloquial past indicative** of آوردن (âvordan) - an informal variant

The page does not list "battle/combat" as a meaning for the Persian entry. That definition appears only in the Ottoman Turkish section, where آورد (avurd) means "cheek pouch."

## Etymology

The Wiktionary entry does not provide a separate etymology section for the Persian verb آورد. The etymology given is only for the Ottoman Turkish noun. Since آورد in Persian functions as a verb form derived from آوردن (âvordan, meaning "to bring"), its etymology would trace back through that root verb rather than being listed independently.
```


## [2026-09-04T22:51:42.968Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"بیدستر\\|بید ستر\\|ببدستر\" BQT_v1_pages.txt BQT_v2_pages.txt MON_part1.txt MON_part2.txt | head -10",
 "description": "bidastar in BQT/MON"
}
```


### [2026-09-04T22:51:43.063Z] TOOL RESULT

```
BQT_v1_pages.txt:15477:۸ - درتر کی بمعنی‌چکمه است وایتو کجی بمعنی سازند؛ کفش ازیوست ببدستراست «جتتابی۹۸».
BQT_v2_pages.txt:11937:  ‫تش‌هم‌باشد » وی‬       ‫سوزنده را گودند که درآنآ‬         ‫جند بیدستر باشد ‪ .‬گوبند خایة سک آبی‬
BQT_v2_pages.txt:37460: ‫میباشد و بتازی‌عنب‌التعلب کوبند ‪ -‬ودرفرهنگه‬                       ‫مجگان است که جند بیدستر باشد‪.‬‬
MON_part1.txt:26892:بید ستر: 27 ( بی + دس + تر (داس 
MON_part1.txt:48625:جند بید ستر : 000-00]02518۲]. [- جند 
MON_part1.txt:48627:سضه ببدستر است که سابقاً در تداوی صد
```


## [2026-09-04T22:51:47.956Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26885,26905p' MON_part1.txt; echo \"===\"; sed -n '48620,48635p' MON_part1.txt",
 "description": "Mo'in bidastar entry"
}
```


### [2026-09-04T22:51:48.027Z] TOOL RESULT

```
(فر ه.) غیرقابل علاج. 

بیدرنگ: 8-] (ق مر .) بی‌تأمل» فورآ 
بی‌تو قف. 

پید ربع. 1-2 (ق مر.) بی‌مضابقه. 

بید ستر: 27 ( بی + دس + تر (داس 
کوجچکد. ار ه)؛ بی‌اره] (امسر ۰( (جاذ 0( 
پستانداری از راسته جوندگان که نسبة بز رگ 
است و به وزن ۲ کیلوگرم می‌رسد. موهای 
می‌شود. باهای خلفی‌اش برده‌دار است و 
می گیرد. بادستر» بتر» وبر. 

بیدق: (-2/02)۵۲۰ [معر . پیادکث» بباده] 
بیاده. تو از مهر ه‌های شطرنج» پیاده. 
راهنما در سفر (غم.)) ج. سادق. سدق سسیم. 
( کد.) ستاره؛ ک و کب. 

سیدل: 061-]0 (ص مر.) آزرده» گرفته» 
دلتنگك. عاشقء دلداده» شیدا. 
===

جندار: 16-027 [معر. جاندار ] (.) سربازی 
که مأمور حفاظت فرمانده قشون؛ حاکم و 
جز آنان است» نگهبان؛ ج. جنادر ه. 

جند بید ستر : 000-00]02518۲]. [- جند 
بادستر » معزرد کتل‌ستاشتر:] (امر.) (جاد. بز.) 
سضه ببدستر است که سابقاً در تداوی صد 
دردهای عصبی و ناراحتی‌های روحی و 
ضایعات سیفیلیسی و امراض عفونی دیگر 
بکار می‌رفته است؛ خصية الکلب البحرء 
خاباٌ سگ آبی. 

حندر: ۱(1:0027.) رخت» جامه. 

حند ره۵. (12002۳2)۵ (۱.) جامه ژنده و باره.
```


## [2026-09-04T22:52:02.517Z] TOOL CALL #65: Bash

```json
{
 "command": "curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%A8%DB%8C%D8%AF%D8%B3%D8%AA%D8%B1&action=raw\" | head -60; echo \"=== varun raw ===\"; curl -s \"https://en.wiktionary.org/w/index.php?title=%D9%88%D8%A7%D8%B1%D9%88%D9%86&action=raw\" | head -40",
 "description": "Wiktionary raw bidastar, varun"
}
```


### [2026-09-04T22:52:05.125Z] TOOL RESULT

```
==Persian==

===Alternative forms===
* {{alt|fa|ویدستر|tr=vidastar}}

===Etymology===
Perhaps a compound word from {{der|fa|ine-pro|*widʰu-||tree, beam}} and {{m|ine-pro|*h₁ed-|t=to eat}}, literally means a "wood-eater".

===Noun===
{{fa-noun|tr=bidastar|pl=بیدستران|pl2=بیدسترها|pltr=bidastarân|pl2tr=bidastar-hâ}}

# [[beaver]]=== varun raw ===
==Ottoman Turkish==

===Alternative forms===
* {{alter|ota|وارونه|tr=varune}}

===Etymology===
{{bor+|ota|fa|وارون|tr=vârun|t=upside down, inverted}}.

===Adjective===
{{head|ota|adjective|tr=varun}}

# [[upside down]], [[inverted]], [[reverse]], [[upturned]]
#: {{syn|ota|ترس|tr1=ters}}
# {{lb|ota|of a building}} [[thrown down]], [[demolished]]
# [[inauspicious]], [[ill-omened]], [[unfortunate]], [[unfavorable]]

====Descendants====
* {{desc|tr|varun}}

===Further reading===
* {{R:tr:OTK|varun|vol=1|page=5093}}
* {{R:ota:Kelekian|page=1299}}
* {{R:ota:Meninski|C|column=861|Iversus}}
* {{R:ota:Meninski|T|column=5317}}
* {{R:ota:Redhouse|page=2122}}

==Persian==

===Etymology===
{{inh+|fa|pal|tr=ʾp̄lʾlwn'|ts=abārōn|t=contrary, wrong, sinful|sc=Phlv}}.<ref>{{R:pal:Mackenzie|abārōn|page=2}}</ref>

===Pronunciation===
{{fa-IPA|wā`rūn}}

===Adjective===
{{fa-adj|cls=وَارُون}}

# {{alternative form of|fa|وارونه|tr={{fa-xlit|وَارُونَه}}|t=inverted}}
# {{lb|fa|Classical|figurative}}
## [[wicked]], [[evil]]
```


## [2026-09-04T22:52:11.850Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Biber\" HRN.txt HUB.txt BRT.txt LKT.txt | head -20",
 "description": "Biber in Horn/Hübschmann/Bartholomae"
}
```


### [2026-09-04T22:52:11.901Z] TOOL RESULT

```
HUB.txt:814:'Biber' (Horn Nr. 181). So kommen wir uber np. habr,
HRN.txt:1984:aw. bawri' 'Biber*; phlv. baprak d. i. bawrak *Biber
HRN.txt:1986:Das np. Wort bezeichnet den *Biber' nicht, es scheint
HRN.txt:1987:aber lautlich identisch zu sein. Ob Biber heute in
HRN.txt:10247:48. batvrak Biber, siehe oben No. 181.
BRT.txt:16683:"Biberkleider  1
BRT.txt:16685:'Biber':  bawraini  vastra  . . iqm  *caturS  elzanatqm{s6..) 3n  dreihundert  Bibern  . ."
BRT.txt:16687:•  j.  'bawray-m.'Biber',  f. 'Biberweibchen': yat  asti  'ris  sragsta  yä^a  yat  asti  gaonS.- t?ma  'ris  öavaili  upäpö  "da^  Biberweibchen ist  am  schönsten,  insofern  es  am  dichtesten behaart  ist;  der  Biber  ist  ein  Wassertier" Yt.5.129').
BRT.txt:16691:•  j.  bawrinay-  Adj,  'vom  Biber  stammend, Biber"';  'wraini'^  (APn.)  vasträ  .  ,  Sma- tanam  bauiranqtn  (sd.)  Yt.5.  129.
BRT.txt:16769:a)  '(sein  sva.)  da  sein,  existiren':  yat  .  . paiti  frali^titn  bavainti  .  .  ggrihqm  (sd.) V.^.  10;  —  yai  kvqm  näirika  bavaiti "wenn  eine  rechtmässige  Frau  da  ist" Vd.2;  —  aSäunqm  ..  fravasayB  .  .  häiti^ hätqm  . .  3ffAu/qm  . .  bBsyantqm  "..  fide- lium  qui  sunt  .  .  fiicre  .  .  erunt"  Yt.  13. 21;  —  daSnqm  .  .  yä  häitinqmcä  bss- ytintinqmcä  tnazistäcä  . .  "dieReligion  . ., die  unter  allen,  die  es  gibt  und  geben wird, die  grösste  ist.."  Y./2.9.  b)  'sein' als  Praedikatsverbum  (Kopula):  bawris bavaiti  upäps  "der  Biber  ist  ein  Wasser- tier" Yt.5.  12g  Gl.;  —  *frayaire  ayqn bavaiti  kubatrS  .  .  aia  apare  (sd.)  ayqn duzäinm  "vormittags  ist  er  (noch) glücklich,  dann  (aber)  .  ."  Aog.5^;  — pairihwS  (sA.)  bavaiti  partiä  yim  .  .  "evi- tanda  est  via  quam  , ."  Aog.  7";  V.  ig. 43(?),  Vyt.Jo(?),  Nik.2,  j(?).  Unklar: kuymte  Yt.j5.s3*,  werüose  Stelle.
BRT.txt:27622:'gebären';  1)  von  Menschen;  a)  Ait: SicöM  (nJimlandvIin)  Üaräitii zizanaitt^ (NPf.)  Jaihyante  huzämim  (sd.)  ".  .  ge- bärende Frauen  . ."  Yt.5.87;  —  3r»hqm raya  .  .  Auzämitö  (sd.)  zTzan?nH'''>  (näml. hairiSis)  Yty.  15;  —  ya%a  ha  tsm  zi- zanäp^  yS  .  .  Ytl^.  142;  —  gal%anqm Stshairyeke  (sd.)  .  .  yat  anAairyS  tlzatun Vr. /.  3;  2.3.  b)  Pass.  und  Med.  in pass.  Sinn:  yahmai  zayata  %raltaonS  V, /.  1 7 ;  —  ahmat  haea  puhra  (sd.)  zayaiti^^ Nik.  1;  —  zaySnte  .  .  dasa  ^%ra  Az.5; Vyt.  I,  j;  —  ndil  akmi  nmäne  *zänaite'''* (3PPM,)  ä^rava  naiita  . ,  äat  ,  .  zayinte "nicht  werden  in  diesem  Haus  geboren ein  Priester  noch  .  .,  sondern  es  werden ..geboren  werden  .."  Y.  j/. 6;  —  narqmca zätanqmca  zqkyamnanqmca  ".  .  die geboren  sind  und  künftig  geboren  werden" Y. ^5;  —  s.  noch  zata-  bes.  a)  von Tieren:  bawranqm  */atur3{sd.)  *sTzana- tarn    "der  Biber,  die  vier  Junge  werfen"
```


## [2026-09-04T22:52:26.407Z] TOOL CALL #67: WebSearch

```json
{
 "query": "بیدستر ریشه‌شناسی واژه سگ آبی حسن‌دوست etymology bidastar Persian beaver"
}
```


### [2026-09-04T22:52:28.246Z] TOOL RESULT

```
Web search results for query: "بیدستر ریشه‌شناسی واژه سگ آبی حسن‌دوست etymology bidastar Persian beaver"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T22:52:39.534Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ ifrit ===\"; grep -n -i \"ifrit\\|'ifrīt\\|عفريت\" FVQ.txt FVQ_pages.txt | head -10; echo \"=== AFM ifrit ===\"; grep -n \"عفريت\\|عفریت\" AFM.txt AFM_pages.txt | head -10; echo \"=== TAD/ARB ===\"; grep -n \"عفريت\\|عفریت\" TAD.txt ARB_mo3rb.txt ARB_abdulraheem.txt 2>/dev/null | head -10",
 "description": "Semitic books ifrit"
}
```


### [2026-09-04T22:52:39.615Z] TOOL RESULT

```
=== FVQ ifrit ===
=== AFM ifrit ===
=== TAD/ARB ===
```


## [2026-09-04T22:52:44.273Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"ifrit\\|'ifrit\\|Ifrit\" FVQ_pages.txt LKT.txt AFA.txt | head -20; echo \"=== AFM search afarid ===\"; grep -n \"آفرید\\|أفريد\" AFM_pages.txt | head -5; echo \"=== TAD grep afarid ===\"; grep -n \"عفر\" TAD.txt | head -5",
 "description": "More Semitic refs"
}
```


### [2026-09-04T22:52:44.360Z] TOOL RESULT

```
=== AFM search afarid ===
=== TAD grep afarid ===
1410:تصغير 831011 لان ف سردينيا اعفرهوا نط عاك نيك لزنت
```


## [2026-09-04T22:52:50.827Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls CHEUNG*; grep -n \"^\\*fraiH\\|fraiH\\|\\*frai\" CHEUNG.txt | head -10; echo \"=== par2 fight ===\"; grep -n \"to fight\\|\\*parH\\|\\*par\" CHEUNG.txt | head -10; echo \"=== had ===\"; grep -n \"^\\*had\\|\\*had-\" CHEUNG.txt | head -5",
 "description": "Cheung roots"
}
```


### [2026-09-04T22:52:50.905Z] TOOL RESULT

```
CHEUNG.txt
492:*saucé ‘to burn, light", *rai9! / *frait/9 ‘to die, decompose’, *caud / *paud ‘to run’. 
6610:*fraiH 87 
6613:*fraiH ‘to rejoice, ? to atone, [med.] please’ 
6665:88 *frait/0 
6693:© Тһе root *frait/0 is probably related to Skt. mret. The Iranian form with f- may 
55136:*baud' (s.v.), *fraiH (s.v.), 
55231:*čať , *fraiH 
55365:*bauf, *fraiH, *gaHz (s.v.), 
55773:*fraiH (s.v.), *huanH (s.v.), 
56288:*frait/9. 
=== par2 fight ===
1387:CSogd. ptbyw ‘honour, respect’ || (+ *pari-) BSogd. prB’s, CSogd. prf’- ‘to change 
1389:redupl. *pari-b'/,-bà-sa-, with - < *-B-f- < *-B-B- (Sims-Williams 1984: 148). 
1391:(+ *pari-) Impf.: IND. 3sg. BSogd. pr’yB’s; Partic.: perf. pass. CSogd. prf’c (f.) ‘changed in colour, pale 
1471:*MIDDLE PERSIAN: (+ *pari-) MMP frbys- (inch.) ‘to be afflicted, suffer’ 
1606:prison; band’ || (+ *pati-) MMP pywyn- ‘to bind, join’ || (+ *pari-) BMP plwnd- 
1618:(YK‘YWMWN-)yt /paywast éstéd/ || (+ *pari-) Partic.: perf. pass. BMP plwstk /parwastag/ || (+ *ni-) 
1635:MSogd. ptß’ynt ‘to prolong; connect; overtake, join’ || (+ *pari-) CSogd. prbnty (m.) 
1678:*MISC: Par. beZ-/bóst- ‘to bind’ || (+ *pari-) Toch. (LW) perpente ‘burden, load’ (< 
1706:*para-) ‘to carry off, forth’ || (+ *pari-) ‘to take around ? || (+ *fra-) ‘proferre, to 
1747:back’ || (+ *pari-ä-) ‘to bring back, restore’ || (+ *para-) ‘to bear way, take away’ || 
=== had ===
8914:*had 125 
8937:*had ‘to sit, be seated’ 
55508:*had, *HaHh 
57834:*had, *HaHh
```


## [2026-09-04T22:52:54.364Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6610,6665p' CHEUNG.txt; echo \"=== had ===\"; sed -n '8937,8990p' CHEUNG.txt | head -60",
 "description": "Cheung fraiH and had"
}
```


### [2026-09-04T22:52:54.430Z] TOOL RESULT

```
*fraiH 87 


*fraiH ‘to rejoice, ? to atone, [med.] please’ 

*AVESTAN: fiT- (frii-) ‘to rejoice, please’ || (+ *a-) ‘to bless’ = Liste: 36 

Pres. {1} na-: IND. 1sg. YAv. afrinami (Y 11.15, Y 52.1, Y 52.8, etc.), 1р1. OAv. friianmahi (Y 38.4), 
3р1. YAv. afrinonti (Yt 13.51), SUBJ. 1sg. YAv. afrinani (V 22.5), med. 1sg. OAv. frinai (Y 49.12), 3sg. 
Y Av. frmät (Yt 13.50), IMPV. 3р1. YAv. äfrinontu (Yt 13.157); Pres. {2} them. па-: IND. 3sg. YAv. à 
frmaiti (Y 62.9),1pl. YAv. frinamahi (Yt 12.3, Yt 12.5, V 20.5); Partic.: pres. {2} med. OAv. frinomna- 
(Y 29.5) 

*MIDDLE PERSIAN: (+ *4-) MMP ’fryn-, BMP "plyn- /afrin-/, MMP "fwr-, ’pwr-, 
BMP Gul /afur-/ ‘to create; bless’ || (+ *ni-) BMP nplytk /nifridag/ (ppp.) ‘cursed’, 
BMP nplyn /nifrin/ ‘curse’. 0 MMP ’fwr-, 'pwr-, BMP "pwl- /afur-/ are later forms, 
deriving from the past participle /afrid/, Henning 1933: 200. = DMMPP: 27a f. 
Widely attested: Pres.: IND. 1sg. MMP ’fryn’m, MMP ’pwrym, 1р1. MMP ’pwrym, MMP *’pwrwm, 3р1. 
MMP ’pwrynd, etc. 

*PARTHIAN: бур ‘dear, beloved’ || (+ *a-) "fryn- ‘to bless’ || (+ *ni-) nfryd- (pret. 
stem) ‘to curse’ = Ghilain: 84 | DMMPP: 158b f., 27a f., 240a 

Pres.: IND. Ipl. "fryn'm, 3р1. "friynynd, SUBJ. lsg. ’fryn’m, 2sg. ’fryn’h, 1р1. ’fryn’m, IMPV. 2pl. 
"frynyd; Partic.: perf. pass. "fryd, "frydg 

*KHOTANESE: briya- ‘beloved, dear, treasured’ || (+ *a-) ävun- ‘to approve’. 0 
briyanda ‘beloved’, in DKS: 315b, should be interpreted as two transparent words: 
acc. sg. m. bri ‘dear’ and inj. 3sg. yanda ‘makes’, SVK I: 100 f. Another entry, the 
hapax form phrrinä ‘love, friendliness’, DKS: 263b, is unconnected as well: it rather 
means ‘message’ and "is clearly a loanword from Tibetan (h)phrin ‘message’.", 
SVK Т: 81. || SGS: 11 f. 

*SOGDIAN: BSogd. pry-, CSogd. fry-, MSogd. fry- ‘dear’, SSogd. Brywk (m.) ‘praise 
(?), joy (?)’ || + *a-) BSogd. ’’pryn, CSogd. ‘уп, MSogd. "un, MSogd. "Bryn ‘to 
praise’ || (+ *us-) CSogd. sfryn, SSogd. sBryt-, MSogd. sfryt- ‘to create’ || (+ *pati-) 
BSogd. ptßr’yn ‘to bless back’, MSogd. ptfryn ‘to send greetings’ || (+ *ni-) BSogd. 
nBryc (Ё), MSogd., CSogd. nfryty (ppp.) ‘accursed’ 

(+ *а-) Impf.: IND. 35р. SSogd. "Bryn; Partic.: perf. pass. SSogd. ’’Bryt’k, (comp.) CSogd. ’frytystr 
‘more blessed’ || (+ *us-) Impf.: IND. 3sg. CSogd. syfryn, MSogd. syfryn (Cosmog.: 307); Partic.: pres. 
CSogd. sfrynn ° (m.) ‘creator’, perf. pass. CSogd. sfryt- ‘created’; Pass.: pres. SUBJ. 3р1. MSogd. sfrytyt 
wß’nd ‘will be created’, pret. IND. 3sg. SSogd. sBryty L’ “kty ‘was not created’ || (+ *pati-) Pres.: IND. 
2р1. dur. MSogd “ptfrynd’sk; Impf.: IND. 3sg. BSogd. pt’yBr’yn, (med. ?) dur. MSogd. "ptfryd'sk 
*CHORESMIAN: ? fn- ‘to sing’ (< *to praise, please with a song’ ?), Bry’k “honoured, 
esteemed’ || (+ *upa-) bfn- ‘to create’, bfy- (denomin. ?) ‘to please’ © Samadi: 69 
*NWIR: (+ *а-) NP 4faridan/afarin- ‘to create’ || (+ *ni-) NP nifrin, Nn. nifrin ‘curse’ 
*NEIR: Oss. I. lymzn, D. limæn, nimzl ‘friend, lover’, Pash. wrin ‘open, happy, 
sincere’ || (+ *4-) Oss. arfze ‘blessings’ 

*SANSKRIT: pray ‘to please, be pleased, enjoy, satisfy’ > EWAia II: 181 

«PIE *preiH- ‘to please, be pleased, enjoy’ = LIV: 490 | Pok.: 844 


88 *frait/0 
=== had ===
*had ‘to sit, be seated’ 

*AVESTAN: hiö- ‘to sit, be seated’ || (+ *abi-) ‘to be seated on (a horse)’ || (+ *ni-) ‘to 
sit down’ — Liste: 71 

Pres. them. red.: IND. 3sg. YAv. nishióaiti (Y 10.15), SUBJ. 3sg. Y Av. nishióat (V 16.1), OPT. 2sg. 
Y Av. nishiööis (Н 2.13, Vyt 59), 3sg. Y Av. nishióoit (V 9.29), med. 3sg. Y Av. nishióaeta (V 8.11, V 9.33 
ff., V 16.8 f£); Perf.: ОРТ. 3sg. YAv. ni hazdiiat (Yt 13.13); Inf.: ҮАУ. aiBi.Sasta; Caus.: IND. 35р. YAv. 
"nisaóaiieiti (FrA 24), INJ. 35р. YAv. nisaóaiiat (Y 9.24), OPT. 2sg. Y Av. nisaóaiiois (H 2.14); Desid.: 
INJ. 3sg. OAv. hisasat (Y 32.13) 

*OLD PERSIAN: (+ *ni-) ni-sad- (caus.) ‘to establish’ = Kent: 212 

Caus.: impf. IND. 1sg. niyasadayam <n-i-y-S-a-d-y-m> (DNa 36), niSadayam <n-i-8-a-d-y-m> (XPh 34) 
*MIDDLE PERSIAN: (+ *ni- MMP nsyy- ‘to sit down, settle oneself’, MMP ns’y-, 
BMP n3’n- (caus.) ‘to place, settle, ground, establish = DMMPP: 245b f. 

Pres.: IND. 3sg. MMP nsyyd, SUBJ. 3р1. MMP *nsyy’nd, IMPV. 2sg. nsyd; Partic.: perf. pass. MMP nšst, 
etc. 

*PARTHIAN: (+ *ni-) nšyd- ‘to sit (down), settle oneself’, also nšyl- (< Bact./Sogd. ?). 
= Ghilain: 50 | DMMPP: 245b f. 

Pres.: IND. 3sg. nsydyd, 3р1. nSylynd; Partic.: perf. pass. nšst; Inf.: "nsstn 

*KHOTANESE: (+ *ati-) tva’y- (ttuva’-) ‘to bring across’ || (+ *abi-) bvai(’)- ‘to 
mount; ride’ || (+ *ni-) nät- ‘to sit down’, näta’s- (na’s-) (inch.) ‘to end’ = SGS: 39, 
102, 53 f., 57 

*SOGDIAN: (+ *pati-) BSogd. ’pc’t ‘time, instant’ || (+ *pari-) SSogd. prsyö (old 
caus.) ‘to sit through, out’ || (+ *ni-) BSogd. пуб, CSogd. пуа, MSogd. пуб ‘to sit 
down’, BSogd. n(y)s’y6, BSogd. nysyö, CSogd. nsyd (caus.) ‘to plant; establish’ 

(+ *pari-) Impf.: IND. 2sg. SSogd. prysyöy || (+ *ni-) Well attested: Pres.: IND. 3sg. BSogd. nyöt, 3pl. 
BSogd. nyö’nt, SUBJ. 3sg. BSogd. nyö’t, etc. 

*CHORESMIAN: (+ *ni-) ny0- ‘to sit; to be, become’, m/nh’zy- (caus.) ‘to place’ 
c» Samadi: 127 


126 *hah 


*BACTRIAN: (+ *ni-) vipoApo, мролцо ‘seat (of the gods), throne, dwelling’. 0 Cf. 
Pth. nsdm, MMP nëm, BMP nsdm ‘seat’. = S-W, Bact.: 208b 

*NWIR: (+ *4-) Abz. avad/av-, Abyan. aya(y)-/ay-, Qohr. aha(d)-/ah-, Ard. axo/ax-, 
Tr. axa(y)-/ax-, Nn. āšis-/āš- ‘to become seated’ (influenced by *HaHh ‘to be seated, 
sit’ ?) || (+ *ni-) Widely attested: NP niSastan/nisin-, Bal. nist/nind-, Kurd. nistin, 
Zaz. ro-nistis/ro-sen-, Awrom. nistáy/-nis-, Tt. (Esh.) ansin/ansest, Gz. ni(y)-/nist, 
Gil. (Rsht.) nistaen/nisin-, Gur. (Kand.) nist-/-nisan-, Ham. he-nistän/ he-i-ni-, Semn. 
nia- ‘to sit’, Sang. -nést-/ neeroen-, Shamerz. -nist-am-/näsin-am-, Sorkh. -niäst-, 
(supplet. ?) nin-, Lasg. -nest-/nieroen-, Isfah. nišdän (supplet. ?) niy-, Sist. rsin-, Siv. 
rsin-/nist ‘to sit down’ (with dissim. n- > r-), Gz. nan-/nast (caus.) ‘to make to sit
```


## [2026-09-04T22:53:09.184Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3600,3700p' BRT.txt",
 "description": "Bartholomae apa- compounds region"
}
```


### [2026-09-04T22:53:09.244Z] TOOL RESULT

```
•  j.  *a-pairi.aya- "  Adj.  'um  was  man nicht  herumgehen,  dem  man  nicht  aus- weichen kann':  asts.viüötui . .  'yS  Aog.57.
Zum  V.  ay-.  —  ai.  paryaya-  m.  'Umtaur.  — 'Sii.\{a'tytp' rauiisn.  —  ')  Ausg. ohne Trennungs-
•  j.  a-pairi^äftra-  Adj.  'nicht  verkommend,
unvergänglich':  däya  .  .  xratüm  paslaaa masitim  mazänUm  "nm  "gib  .  .  alsdann Gedächtniskrafi,  grosse,  umfassende,  un- vergängliche" Y.  62.4.
*pairiM%ra-  n.  "Untergang',  zumV.  ä4-;  Gdn.
KZ.  30.  514.  —  Pü. :  fehlt;  vgl.  DST.  ZA.  /.
388.
•  j.  apairi.gaed'ä-  Adj.  -?-:  dusxratum ''^am  *asravayai^a%qm  Aog. AD.
^Ü.i  undeutlich;  afarö'ii  ...
•  j.  a-pairi1hva-  Adj.  'um  was  man  nicht herumgehen,  dem  man  nicht  ausweichen kann' :  pairi^wö  bavaiti  panta  yim .  .päiti . . hä  dit  asvs  "'irvS  yS  vayaol  anamaridi- kake  Aog.  yj—Sl^.
"~\.:  m'i/arai,  SÜ.:  aHaiiiramaiiiyah,
p.  apariyäyd' :  lies  äp'\    S.  Unter  hapariya-.
•  j.  apairi.vava8't9ina-  Adj.  (fem.  -va-) 'der  am  wenigsten  überwunden,  bewältigt werden  kann':  fravaiayS  . .  'tama  snaU %isqmca  varütanamca  ". .  die  am  wenig- sten zu  bewältigenden  unter  den  Waffen und  Wehren"  Yt  13. 26.
Snperl.  ans  'vanl:  HapIoL  flir  'pairiwava- vas'  (Sji'ö);  *pairiwm-a.  m.,  zum  V.  <!,«'-;  ai. faribhttva-  m.  "Geringschätzung'.
db,Google
79
a-paourrän
ap^ma-
80
•  g.  a-paourvim  Adv.  'in  noch  nicht  da- gewesener Weise,  wie  nie  zuvor":  yS  va aia  ufySnl  tnanaüa  vohü  ap'  mazdqmcä.. "der  ich  euch,  o  A.,  besingen  will  wie nie  zuvor,   und   den    VM.   und   . ,"    Y.
ASn.  aus  *a-pai>uruya'    Adj.  —    ai.  äpünyam Adv.   —    Vü.:fraätm.    —    ")  Ved.  ParsUelen
bei  Bthl.  AT.  2.  138,  Mills  G.  396.
•  j.  apa.skaraka-  Adj.  'hohnsüchtig,  höh- nisch': nivßyaka  nipasnaka  °^a{NP.)  apa.- xraosaka  imä  paifi.vlsmte  Yt.  5.95.
Ableit.  BPS  "apa-skara-  m.;  Et.  und  Bed.?
•  j.  apa-stanah-  Adj.  —?—'':  kmsäsps .  ,  yö  jtnat  anssJamafuni  .  .  apa.dis»m nyaidäuru  °nanhs  (NSin.  ?)  gats  (sd.)  ar?- zahe  YL/3.42.
>)  Sicher  falsch  DST.  ZA.  2.  627;   vgl.  GIrPh. /.  309.
j.  afasidt^  N.  41:  lies  afastvSa.
•  j.  apa-stütay-  f.  'das  Sichabgeloben, Abschwören':  yä  haca  damayat  mazda- yasnSii  'Biiis  "das  Abschwören  dei  mazd. Religion"  N.41.
VgL  ättülay^.  —  Pü. :  ie  den  .  .  ajä!  släyiU
•  j.  apa-srayamna-  Adj..,  PPM.:  s.  sray-. m  j.  apa-za<)ah-  Adj.  (auch  fem.)  'den Steiss  ab-,  weghaltend  (nach  oben?)''*, von  der  Fliege:  ^maxsiJiihrpa  prrfaitya frasnaol  °Sawi4ff(GSf.))  * akaramm.driwya (sd.)  V.7.2.
PQ. :  apäc  kün.  —  ')  Falsch  Cld.  GGA.  18^3. 400-
•  j.  apa§8  Adv.:  s.  apänk-.
j.  afoH  Yt  10.  20:  s.  apink'  mit  No.  t.
•  j.  apaSütöit  Inf.:  s.  unter  sütsil.
•  j.  apä-£ "Erreichen;  Erfolg*:  yazai  *apqm- ca^^  baystnca  ..  äxäim  hqmvainnmca  Yl 75. 1.
KompE.  —  Zum  V.  a/..  —    •)  So  F  i  nsw. ; NA.  ajumla.    S.  auch  N.  4/.
•  j.  apäxtara-,  apIx^Ära-  Adj.  'rück- wärts, hinten  gelegen'  sva.  'nördlich'*^: Harat  haca  nafmst  'tara^byB  haca  naf- maiibya  fradvarat  aarö  mainyus  V.  ig.  i ; H.  2.25,  FrW.  70.42;  —  druxs  ya  nasus upaJvqsaid  'Xraäbyö  nalmaäbyB  V.  7.  s 8. 16;  —  °W''  apanasythe  "im  Norden sollst  du  verschwinden"  SrB.j.
♦)  Das  awestische  Volk  orienlirte  sich  mu dem  Blick  nach  Süden;  daher  'südlich'  durch fralara-  'vorn  gelegen'  oder/i«(«/fl- 'dervordere' bezeichnet  wird,  'nördlich'  dagegen  durch  obige Wörter  oder  durch /uj/.jiV''- (sd.)^    Damit  steht
in  Einklang  die  BeneoDung  des  Ost-  und  West- winds durch  väß  aparä  (sd.)  und  ainrö  (sd.)  'der Gebirg",  'der  aus  dem  Tiefland  kommende Wird';  BthU  BB.  14-  250.  daünäl  fairi  V.  3. 4z  ist  mir  »onach  'von  Westen  her',  nicht  'von Süden  her",  wie  aL  däksinät  pari.  Die  luft- gende  Wirkung  des  Westwinds,  von  dem der  Text  spricht  (s.  unter  '%tväsa^,  mag  an  dem "  ■  einer  Entstehung  durch  besondre  Verhält- bedingt gewesen  sein.  Auf  Vi.  j.  :6  ist nichts  lu  geben.  Vgl.  {auch  lEt.)  Hbm.  ZDMG. 38.  428,  PSt.  izo.  AGr.  I.  94,  Bthu  ZDMG. 42.  154,  4_j,  67o,BB.  J-J.69,  i-^.  250,  s?»?,  Bang ~"  '5-  317-  FrMüller  WZKM.  S.  187,  Hörn GlrPh.  /b.  Iti.
KompA.,  E.  —  Kompor.  aus  apanh-  [%  20^'). —  mp.  (Pü.)  apäxtar,  np.  bäilar  (Hbm.  PSl. läo  No.).  —  ■)  Ergänze  nährte.  — t)  Die  Zer- legung in  apa+'ajflara-  (np.  iLxlar)  ist  falsch. Mp.  apäxlar  ist  ])  'Norden',  aus  ir.  *ap', 2)  Tlanet',  aus  *»/'  {iipa-\-axtar°  "was  bei  den Sternbildern  ist').
•  j.  apäx9Sra.iiaema-  n.  "Nordseite,  Nor- den': pasca  hü  /räsmS.däütm  ^namjanaiti Yt4.8(?).
•  j.  a-patar-  m.  'Beschützer,   Bewahrer': v»rikririn?mca  afrlnami  dva  'tära
dva  nipätära  YL/4-45-
Npö. !  pSiiäni  ml  kunad.
j.  apä%a  :  s.  öV.
•  j.  apäi9i$  — ?— :  np^m  . .  vsiusavaitim (si)  draogsm  viku^  ap"  V.4.54'>;  —  y5 äp?m  ..  vt^usavaitTm  draogsm  viius  ap'
Pü.:  dnddtdd.  —  0  Die  beiden  Stellen können  ursprunglich  nicht  den  gleichen  Wort- laut gehabt  haben.  An  der  1.  Stelle  wird  etwa gestanden  haben:  Wer  eines  Verbrechens  be- zichtigt wird  und  leugnet ,  soll  das  Ordal- wasser  trinken.  An  der  2.:  Wer  das  Ordal- wasser  trinkt,  (rolzdem  er  sich  einer  Schuld bewusst  ist,  wird. .  bestraft.  H erste II ungs ver- suche —  von  vornherein  aussichtslos  —  bei Sp.  Komm.  i.  156,  Gdn.  Stud.  i.  103.
•  j.  apäna-  Adj.,  PPfM.:  s.  ap-.
•  j.  apävaya-  m.  Name  einer  Krankheit oder  eines  Gebrechens:  ma  {a>ra)  °jJ  V. 2.29.
EL?  — Pü.:  ipdrd,  erl.;  kii  ddt  n  n  k  a»dar vor  fröt  Hast  eilet.
•  j.,  g.  apama-'',  g.  ap«ma-  Adj.  (fem. "ffiii-)  Adj.  'der  (zeitlich)  letzte',  ntir  von dem,  was  am  Ende  der  Dinge  (des  ersten Lebens)  eintreten  wird  ('jüngst')'':  'ml arihSus    unalsZ {sA.)    Y.J/.6;  43. S\    —
.  *mamii  (sd.)  . .  *paouruyl  vXdvS  avqm  yä im  anhat  'mä  ". .  jene  kenn  ich,  die  ihn zuletzt  treffen  wird"  Y.4.^19;  —  •mS'B,
dby  Google
Si  apnnsin
7.  a)  ASn.  'num  als  Adv.  'zuletzt,  am letzten  Ende,  zu  Ende  der  Dinge' :  ya'iä/l'ä aukat  'm>m  arshui  acilte  drpgvatqm  af as3um  vakist^m  manö  "und  dass  zu  Ende der  Dinge  den  Z>/Ttjgenossen  das  schlech- teste Leben,  aber  dem  Gläubigen  der beste  Aufenthalt  zu  Teil  werden  solle" Y.^.  4;  —  at  vJ  vayli  (sd.)  anhaitl 'wum  vacs  Y.5J.7;  ^.4,  5^-14;  — ^a^i' •fHfwt  Mom'vä  arfkal  nhäiti/ (sd.)  Y.io. 16,  a)  mit  Gen.:   alibyS  at/hSuf  ai'öi
(sd.)  anftat  'imm  Y.  45. 3, SnperL  aus  a/a;    vgl.  apara-.   —    u.  apamä- Adj.  —    Pü. :  ^atum,  läk  d  an  i  af.  —    ')  » im  gAw.  nur  V.  45.  3.   —    ')   Im  Gegensatz
aipi
82
•  j.  ap«m9n),  g.  ap3ni9m  Adv.:  s.  apma-, ■  j.  a-p9r9tö.tanü-  Adj.  'auf  des  Leib kein  Makel  haftet,  makellosen  Leibes"*: Aagat^rnt  gavam  axsaenanqm  'nunqnt  V. 22.4.
Bed.  Dach  K.  Vgl.  pariiö.tanü:  —  Pü.:  man- ftkr,  erL:  vinäikärik  . .  ?  .  .  lü  mal  esiil,  — ■)  Anders  Gdn.  KZ.  30.  517.
•  j.  a-p»r»näyav-  Adj.  "nicht  volljährig, minderjährig, unmündig':/w^^iTÄÄ  ^'näyaoS N.54;  —  kimHi  daAmanqm  'nSyunqm 'S.iO-{;  —  vispaiibys  'tiayubyd  lÜ.ii;  — tisil  (okmäi  'nHyunqm  N,  //;  —  "nayu  (als NSm.)  "  aimi  nsit  p?rmäyu  (sd.)  Yt.  i(). 43;  —  ms  °nayu  (alsNPm.)"  iaunmii(sd.) mJl  iaintna  YL77.54;S5.  a)  m.'Kind'; 3faß0yaha  'niJyus  "verschlafen  (ist  der Hund)  wie  ein  Kind"  V.  73.48;  483.
.\bleit.  —  mp.  apurnäy,  np.  iuraä,  —  Pü. : aftiniäyai.  —  ')  %  40/,  Unsicher.  —  >)  Ob Doal-  »tatt  Pluralfonn,  weil  diese  bei  der  a- Deklination  iDsammeoficIen?
•  j.  apvmniyuka- ')  Adj.  'minderjährig, unmündig;  Kind':  *'ill  . .  *°ia  (ND.)  .  . *'iatiqm  F.  2e*';  —  ^r^nm  hrmavai yat  aisa  yS  'ks  usjasaf  (sd.)  V,  i  5. 1 5 ;  1 6 ;
—  5rJ5r?»i  (sd.)  .  .  Aapla  tar^a  'kahe V.75,4s;  —  yat  .  .  mazdayainS  'kS  avt hl  hapia  sania  frajasäiti  .  .  aiwyarahänS {sA^  paUis  he  ma^yäi  bBjyaman!!  VA-iS;
—  ym  'k3  frashavat  (sd.)  satta  ki  paoi- rfm  frasnäoay^n  aitahe  yat  'kahe  V.  16.  ^ ; /J.44.4S;  —  näirika  'kasiaV.3.\\;y, — nitrHatüt  •iahecil  N..40;  —  näirikqm w  *'ibm  (va)  N.  105;  —  nairinqmca 'ioMOMca  kainikanamca  Y.6S.12;  —  ttai- riie  'keQ)  kainike  Y.'2?.5;  —  nairikqm ..  mbmtmiit  (sd.)    "Awi^V. 5.38;  75.48;
—  y!^  anyake  nairika  . .  yS  anyahe  *°ha (IS.)^  ..  a'^aurutum  *pararikacaiii  (sd.) N.  7;  77;  —  yat  he  aoxte  aisa  yeiihe  'ks hacatsuha  ms  *ana  "ka  (VS.)  N.5;  7,  *y, *io,  10 ;  —  'ktm  iiahmB.kßrpl)m  *syaokn3m.- v>r}Nm  (sd.)  V.7J.23;  ¥.2^.27.
KompE.  —  Ableit.  aus  apirmäym-'^'i.—  Pü, : apurnäy,  afvrnäyat.  —  ')  Mit  u  in  F.  und  im Komp.  —  ")  Hds.  •näiui'.  —  3)  Hds.  'iiihf.
—  4)  Vgl.  CK  'ü-ia-  HBM.  PSt.  241,  KZ.  S'i. 153,  HoRN  GlrPb.  /b,  184-
j.  aptrimnäi  N.  Zj:  lies  apiritutiiiiäi.
•  j.  ape  Praen.  mit  Akk.  'nach',  zeitlich: para  asnS  danhsit . .  ape  amp^anqm  spm- tanam  dahim  "vor. .nach  der  Schaffung.." Y.79.8.
Vgl.  aipi,  apaya,  apqm  und  lum  Ausgang  aoe.
—  Pü.:  pa  ape  ayäpakJh  'mit  Erlangung'  (s. ap-\  aber  SQ.:  anäbki.
\.  yazim  aipt  N.  20:  Viti  yaamnahe.
•  g.  ap5  Praev.  (nur  mit  yam-),  dnw.  apä.
Aus  ar.  'fl/oH  (d.  i.  apa-\-ii);  %  303.  3,  BtHL. BB.  13.  74.  —  Pü.;  a^ j.  apäis  N.  26:  E.  apayav:
•  j.  apänk-  :  apak-  Adj.  (fem.  apacl-)  'nach hinten,  rückwärts  gewendet':  "^//(NSf)" vazaili  arstiS  yqm  . .  "rückwärts  fliegt  die Lanze,  die  . ."  Yt.  10.  ao.  a)  NSm. als  Adv.'>:  °Pq^  ^avS  damayäti  "nach hinten  (auf  den  Rücken)  fesselt  er  ihre Hände"  Vt.70. 48.  b)  IS.  als  Adv. 'zurück': *'pasa^'>  vi  *zamar?  ana  duye*  {%A.)\i.i. 2g;  —  uzg?r>pt3mHt  saa'^pm  -pasa  apa.- j^anvainti  (sd^  Yt  14.46.
Ableil.  —  Ableit,  aus  apa,  %  lyS  a.  &  sSg.  — ai.  äpääi-  Adj.  'fem.  ä/ää-):  mp.  apiir,  np.  t3z, vä  'lurück'.  —  Fü. :  undeuüich.  —  >)  Zur  Her- kunft  des  i  s.  %  S  und  BtHL.  IF.  i.  266,  — •)  Vgl.  unter  paräni-.
•  j.  ap^m  Adv.  'hernach,  fernerhin,  künftig": nSif  ff»?  ap'  a^rava  ..  larat  Y.q.  24;  — vis  ap°  tha  patmtu  vT  daivh?ks  Y.  10. I.  a)  tia  apqm  'nunc  deinde,  von  nun an':  ita  af°  vJjasäUi  .  .  daSna  Yt  75.94; 95'-
Vgl.  apt.  —  Pü.:  pas.
•  j.  ap^S  Adv.:  s.  apattk-.
•  j.,  g.  aipi,  p.  apiy  I)  Adv.  i)  'dazu auch,  desgleichen  auch',  ein  neues  Subjekt anreihend,  von  dem  die  gleiche  Aussage gilt:  at  yuS  dasva  .  .  akät  mananhs  sl<l cihr^m  . .  yasca  vä  . .  yazatte  . .  ^yaotnqm 'pl  daibitilnn  yäis  ..  "..  desgleichen  auch die   (eure)  Taten,    durch   die  . ."  Y.32.
dby  Google
83  aipi  I  2  a
3-  a)   'hernach,  später;    kUnftighii
sa3^3rJ{iA.)  . .  ya  ..  vav}r?SSi  pairlJült ..  yäia  var?^aitg  '/LcTblJ  Y.  25,4;  — ai^qmät  ä  ahtnJ  .  .  vTci>3i  (sd.)  -/)"■■>  Y. j2. 8.  a)  mit  Neg.;  'nicht  hinfort  mehr, länger":  »»3  ^I^ä  *fX  äsbävayal  (sd.)  Y. Jt.i7.  3)  'auch,  gar,  besonders',  das vorherg.  Wort  hervorhebend:  maS^a  .  . pirs^u  'pi  ffi/ajii/Vjy  "die  Wolken,  die  sich gar  weithin  verbreiten"  YLA40;  io.44; —  \daraiy  'piy  "gar  fernhin"  X.7. 2;  D, 6'.a,  4";  —  ai'e  °pi  dai'jyanlS  "'äx£  y^a^ besonders  hinsehend"  Yt/0.45;  45;  — *avat  'pi  ya^a  . .  "soviel  gerade  (,  eben) aIs.."V.ö'.io;22,Äa3,J7.7.  I^Praen. 1)  mit  Akk.  a)  'über  —  hin';  a)  zeitlich: dar>-^3mHt  °pi  zrvätam  Y.  6-1. 3 ;  Yt  i^. aö,  ß)  räumlich:  vTspqmHl  'pi  imqm  sqm Y. 57.33; — liuire fraväitUßA.)  tq%ryqm  °pi xSapamm  Yt  74. 1 3 ;  —  yavat  anu  "pi  *i}iti garayS  visasiar?  vlsptm  aval  °pi..  "so  gross der  Raum  ist,  über  den  hin  sich  die  üerge erstrecken,  über  all  den  Raum  hin  . ." Yt. 7p.8.  b)  'bei':  k?m  ksm  °pi  nmäm "bei  Jedem  im  Haus"  Yt.  5. 102.  2)  mit Lok.  'bei',  zeitlich:  mi^nm ..yahmi  ssire m%%rS.dru}5  'pi  %n<isi  paun'a{sA.)  masyS- kunhs  ". .  bei  dessen  Gericht  . ."  Yt.  lo. 8of?).  3)  mit  Instr.  'nach',  zeitlich: s.  aipi  tä,  aipi  taiS  bes.  III)  Praev. {m\\.kan',  karat-,  gart-,  gam-,  vai-,  varpi- ua.).  [IIBh.4.8:  lies  utämaty^'»; —  Y.
.,^.5:  lies  aipisq^^m^
KompA.  —  ai.  äpi,  gr,  iiri.  S.  d»iu  Hbm. ZC.  305,  Cld.  KZ.  31.  262.  —  S.  auch  fl/<-, fr  und  fisinah:  —  Pu.  (lu  Y.  ig,  31,  33):  fas, ha? paslh.  (lu  -i.62):  m  S,  (lu  Y.  57):  fa, flu  V.  if):  afar,  (lu  V.  6,  g):  ausgelassen; (in  Komp.  auch):  andar.  —  ■)  Im  Sinn  von apfirnm.  —  ')  Wo  afiy  in  den  Ausg.  fehlt; B.  FoY  KZ.  3S.  7.  —  3>  Vgl-  Rl.  iS(.:  'Ihe four  last  characiets  are  ceitainly  am"!}/".
•  j.  aipi.awra-  Adj.  (fem.  °rä-)  'bewölkt': iq'iryaiHt  haca  xsafnS  .  .  "rayü  Yt  14.. 31  •>.
NpQ.!  az  bulandi.  —  0  Vgl.  Yl.  II.  4,
•  j.  *aipi.9r«tö.-gitav- ')  Adj.  (auch  fem.) 'der  einen  fest  bestimmten,  fest  zugewie- senen Platz  hat  (,  den  er  nicht  verlassen darf)':  yat  ahmt  nmJne..  nilirika  daxsta- vaitj  anhat  yat  v.l  *sk^dS.aipi.jatS [pisirsY'>  'tus  (NSf)  "wenn  in  dem  Haus . .  eine  Frau  die  Regel  hat''  oder  wenn sie  wegen   eines   ihr   zugefügten  körper- 1
aipi.daßdav-
84
liehen  Schadens  auf  einen  bestimmten Platz  angewiesen  ist"  V.  5. 59,
Zum  V.  iar:  —  Pü. :  a/ar  drnd  ,fäi4),  tri.; ia  yasi  «?  karl  esifl;  s.  unter iomfii.  —  ■)  NA. aifiJHlS  gnt'i  s.  Var.  und  ahm.ir)td.gätav-. — >l  In  den  Text  geratene  Glosse  zu  skiitdö.  — 3)  In  welchem  Fall  sie  eo  ipso  abgesondert wird;  vgl.  V.  16.  1  ff.  —  t)  S.  Tixai'h.ijivl.\gäl<n-.
•  j.  '''aipi.karata'^  Inf.,  mit  asii  'er  ist eingedenk,  hat  Acht  auf  — '  (Gen.):  vis- paz'a  vilcS  mazds.fraoxta  .  .  ySi  huiti  "la dusmatahe  ".  .  die  Acht  haben  auf  das, was  übel  gedacht  ist"  Y.  71.7;  7*.
Zum  V.  'Aar:  —  Pu. ;  ie  kiiid  afar  nikitilät i  diiimal.  —  1)  So  Pt4;  NA.  aiwi',  s.  Frol. XXIX  No.  2.  wogegen  lu  bemerken,  dass  aifii in  Pü.  auch  sonst  durch  afar  (bb  m  dm) wiedergegeben  wiid,  iB.  gleich  Y.  //.  8.
•  j.  aipi-dara- Adj. 'hinterhergehend':  'n (NSm.)  nqma  ahmi  YtJ5.45.
gr,  iirkäKii  "bedienend'.
•  j.  aipLJatay-  f  i)  'Einschlagen  auf —' (Akk.):  'IS  (LS.)  gqm  hufJnA^m  ya'ia ra'^oFstä  "im  Einschlage^  auf  das . .  Rind (ist  der  Hund)  wie  der  Krieger"  V.  j  j, 4S(?).  a)  'Schlagen,  Zufügen  durch Schlag'  (nur  Komp.).  °jaiti  als  Inf. sbes.         [V.5.59:  lies  sk3nd0.aipi.jats.]
KompE.  —  Pü.:  ap7  zaiär  {!)  gSspand  . .,  erl. ; d»zd  H  zvrt  afii  Mrrl'-).  —  ')  Daher  DST. ZA.  2.  205:  'il  combat  pour  le  boeuf. .'  mit der  Bemerkung:  'expression  presque  brahma-
•  j.  *aipi.Jaiti"  Inf  'einzuschlagen  auf—, zu  erschlagen':  i'ia  mi'inilt  daiiia  0°  ,  , gundayäi  (sd.)  ", .  um  auf  die  D.  einzu- schlagen , .""  V.J.32.
```


## [2026-09-04T22:53:23.475Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"spurdan\\|sipurdan\\|sipārdan\\|\\*sparH\\|\\*spar\\b\" CHEUNG.txt | head -10; echo \"=== Cheung spar entry ===\"; grep -n \"^\\*spar\" CHEUNG.txt | head",
 "description": "Cheung spar"
}
```


### [2026-09-04T22:53:23.533Z] TOOL RESULT

```
22942:*spar 351 
22960:*spar ‘to hand over, entrust’ 
22984:*NWIR: NP sipär-/sipurdan, Bal. siparit/sipar- (< NP), Fariz. -spärd/-spär-, Yar. 
22987:isperd ‘to hand over; to say’, ? Gur. (Kand.) -spär- ‘to bury’ (rather *sparH ?) 
23037:*sparH ‘to tread, kick’ 
41476:sipar-/sipurdan, 351 
56475:*spar 
56777:*spar 
56944:*sparH 
58239:*sparH, *xramH 
=== Cheung spar entry ===
22942:*spar 351 
22960:*spar ‘to hand over, entrust’ 
23013:*spard ‘to twitch, quiver’ 
23037:*sparH ‘to tread, kick’ 
23095:*sparz ? ‘to aspire to, strive’ 
55223:*sparz 
56475:*spar 
56777:*spar 
56944:*sparH 
57508:*spard
```


## [2026-09-04T22:53:26.069Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22960,23012p' CHEUNG.txt",
 "description": "Cheung *spar entrust"
}
```


### [2026-09-04T22:53:26.116Z] TOOL RESULT

```
*spar ‘to hand over, entrust’ 

*MIDDLE PERSIAN: BMP spwit /spurd/ (ppp.) ‘conducted (away)’ || (+ *upa-) BMP 
"psp ’I- /abespar-/ ‘to hand over, entrust [+ ’w 407], give up one's honour, life; to 
commit suicide, extradite someone (to be executed, tormented)’ = DMMPP: 17a 

(+ *upa-) Pres.: IND. 2sg. BMP ’psp’lyh /abesparéh/, 3sg. BMP ’psp’lyt /abespared/, 1р1. BMP 
"bsp'I(y)m /abesparem/, 3р1. BMP ’psp’lynd /abesparénd/; Partic.: pres. BMP ‘psp К /abesparag/, perf. 
pass. BMP ’bsp’It/abespard/, BMP "pswlt /abespurd/; Inf.: BMP ’psp’Itn /abespardan/ 

*PARTHIAN: (+ *upa-) "bysp'r- ‘to hand over" = Ghilain: 75 | DMMPP: 17a 

Pres.: IND. 3pl. ’bysp’rynd; Partic.: perf. pass. 'byspwrd 

*SOGDIAN: (+ *pati-) ? SSogd. pspr- ‘to fix, compose, level’, CSogd. pepr- ‘to alight, 
rest’, MSogd. ptspr(t)- (pass) ‘to be arranged’, ? SSogd. ptspr PN (UppInd.4, 
UppInd.71, UppInd.227, etc.) 

Pres.: IND. 35р. CSogd. pcprty; Impf.: IND. 3pl. CSogd. ptysprnt; Partic.: perf. pass. SSogd. ptsprtyy; 
Pass.: pres. IND. 3sg. MSogd. ptsprtyy ‘is arranged’ 


*CHORESMIAN: (+ *upa-) bsp’ry- ‘to hand over, entrust to” = Samadi: 26 

*NWIR: NP sipär-/sipurdan, Bal. siparit/sipar- (< NP), Fariz. -spärd/-spär-, Yar. 
-spard, Gz. ispär-/ispärt, Gil. (Rsht.) ispurdoen/ispur-, Ham. espartan/espar-, Isfah. 
espartän/separ-, Khuns. ispar-/ispart, Soi bé-spar ‘to hand over, entrust to’, Siv. 
isperd ‘to hand over; to say’, ? Gur. (Kand.) -spär- ‘to bury’ (rather *sparH ?) 

*NEIR: Sh. sipör-/sipört ‘to charge, commission’ (< Pers. ?), Yzgh. s(a)pard/s(a)par-, 
Wa. s(a)por-/s(a)pord/t- ‘to hand over’, Pash. spär- ‘to entrust, commission’ (< Pers. 
?) 

*MISC: Arm. (LW) apsparem ‘I hand over? 

*SANSKRIT: ? spar ‘to save, secure; deliver; gain” > EWAia II: 773 f. 

© This amply attested root may have an IE provenance, being connected to the 
Germanic spare forms. 

«PIE *sper- ‘to deliver, secure’ — LIV: 579 | Pok.: 992 

*IE COGNATES: ON spara, OHG sparön, OSax. sparon, OE sparian, Engl. to spare 
*REFERENCES: КРЕТ. 246b; KPF II: 203; Christensen, Contributions I: 67 f., 165; Abrahamian 1936: 112, 


129; Edel’man 1971: 239; EVS: 74; Nyberg II: 27b f.; DKS: 69; WIM II/1: 77; WIM III: 110; Werba 
1997: 262 f.; Steblin-Kamenskij 1999: 323; Shahbakhsh: s.v. sipar- 


352 *spard
```


## [2026-09-04T22:53:38.205Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3470,3520p' BRT.txt",
 "description": "Bartholomae apa- compounds early"
}
```


### [2026-09-04T22:53:38.250Z] TOOL RESULT

```
at  zl  tSi  vaxfyä  vTdusl  zl  nä  mruyät  {sd.) V.5'-8.
Pü.!  aSi;  n  ?lm.
•  i-j  g-  ^'P"  ^-  'erreichen'.    Praes.  2  apa-,
20  afa-  (mit  <i)'>,  24  apaya-;  Perf.  3  ap'.
—  Inf.  apatse.
1)   'erreichen,    einholen':  ysi  vtsp»   ti
dby  Google
71  ap-  3
a/ayeinti  ya  *ace  paskät  vyänli  (sd.)  nsit *aoe  paskii  äfinU  "welche  all  die  ein- holen, denen  sie  .  .,  nicht  werden  sie (selber)  von  hinten  her  eingeholt"  Y.57. 39;  —  kam  «J  arsa  gavai^Tm  apayst pasiä/(sd.)  vaz^mnH  Yt. /0.86; — h5  alvS .  .  iiva.vasma  {sd.)  apayeiti  YL  14.10;  — aval  "apayaie  nama  ahmi  yat  uva  dama apayemi  ..  Yt.  J5.43.  a)  ohne  Obj. 'nachkommen'  (i^umüch):  ma  apaima paourvavaysii  {sd.)   Vr.  22.2'*.  2)  'ge-
langen zu  — ,  teilhaftig  werden',  mit  Al;k. : voAa  xsa^nm  toi  mazdJ ..  apaimä  vTspai yai'l  Y.41.2^'';  — yaiU  .  .  apan5  äangS.- Jyäinm  ä  xia^rnn  . .  Y.^.s  (s.  bei  ä)*i; —  yaha  aam  avat  3^ar»nS  apayemi  Yt. 5.43.  3)  'treffen', vom Geschoss:  yatUt (aHHf)  tanüm  apaynli\X.io.2\.  4)'(ei- nem  Gebot  usw.)  nachkommen',  sva.  'es erfüllen,  befolgen':  abmaoyahe  .  .  aiiihn äainay&  mas  (sd.)  vaca  da'isanakt  mit iyaohnäis  apayantaAei^  "der  die  Worte . .,  aber  in  seinem  Handeln  nicht  befolgt" Y.p-3i.  s)'(^'°^"i  Gegner,  Akk.)gleich- kommen,  sich  gewachsen  zeigen,  bemei- stem':  äal  mqm  aivs  zaraiustrS  anusm- hm  apayeiti  Yt.77. 19.  6)  '(einem  Ge- räusch usw.  mit  derStimme)  gleichkommen, es  gleichtun  können'  (ohne  Obj.) :  yS  gä'^ä srävayeiü  aps  v3  faiti^-sfatne  (sd.) . .  ye%i .  .  fisit  M>asibya  usibya  aiwisurunvaiU apayät  yezi  apffis(sd.)  ..  "..  wenn  er  (den Vortrag)  mit  seinen  eigenen  Ohren  nicht hören  kann,  soll  er  es  (dem  Geräusch) gleichzutun  versuchen  .  ."  N.  2Ö*'.
mit  avi  'einholen':  yest  ahi  paurva.- nafmät  aal  "lam  avi  nmänaya  (sd.)  yezt paskät  aai  ma'm  avi  apaya^sS.)  Yt.i&.a.
mit  ä  1)  'erreichen,  einholen':  yöi  vups t!  apayeinH{s^)  . .  nsit  *aoe  paskäl  äfinie Y.57.29.  2)  'hingelangen  zu  —  (Akk.): yastl  .  .  apänS  darvgs.jyjülm  ä  (näml. apans)  x^a'krtm  vaahSus  manat?hs  astll ä  (näml.  apänd)  »nsQi  (sd.)  paiiS  .  . ". .  wenn  ich  zu  dem  dauernden  Leben gelange,  hin  zu  dem  Reich  des  VM.,  zu  .," Y.J^.5*^
mit  paiti  'hinzugelangen  zu  — '  {avi  mit Akk,):  vTspsm  3  aimät  yat  aZm  (näml. Hyris)  paiti.apayat . ,  sfanvantftn  avi  gai- rlm  VtÄ38.
mit  frU  I )  "hingelangen  zu  — '  {avi  mit Akk.) :  yezi  jum  frapayemi  avi  xam  . .  Yt.
apa-gaSa-  Ti
5.63.  2)    'bekommen,    erhalten':   yä
aiaifi*yrSraihyaHai»(5d.)_/rapa{zSPifk.)»
N.54.  ,
ai._prafia/,  prapryam^'i.  Tgl.  SpnSti;  Tgl.  np. yä'iai/9),  PDE,  firäpam,  wöbe,  yä/un  (s.  No.  1)
—  Pü. :  ayäftan;  s.  noch  No.  2  ff.  —  •)  /  aus ar-/j?.  S  141-     Dieses  /  steckt  im  an.  yä/'.
—  Pö. ;  ape  mä  äfvnim  pa  fcl  naeihiih.  — 3)  Ptt. :  ^aläiJh  i  tÖ.,ape  ayäpent,  —  *)  Pü. : apc  am  ayipenl  fa  diriaiiinik  an  i  pa  ifalällk i  vahuman.  —  ä)  Them.  —  6)  Pü.  erl. :  k»  a/v *vang  boret.  —  7)  S  268. 3  b.  —  »>  ÄV.,  Pldap. pra-af.  Aber  äpilay-  f,  'Einholen'  sctit  ein ♦fl/öva/j  voraus,  vgl.  •^/■ÄJ/o»'.  und  Bthl.  Stud. 2.  170.  —  9)  Aus  mp.  ayäp' ,  wo  ay  Praefix ist,  lu  IF.  12.  Uo;  vgl.  mp,  äpenitan  (No.  2) neben  aySpenltan  (No,  3  f.).
l-t  Z'  "t"  'Wasser';  s,  unter  ö>. '  i-  (j  g'.  P-)  spa  i)  Adv.  'weg,  getrennt von—'  (nur  Komp.) 'J.  2)  Praev.  (mit karit-,  gauä-,  gatn-,  bar-,  yam-,  itai'- usw.).  A)  bei  Ellipse  des  Verbums: aiwica  apanm  (sd.)  patica  apanm  (sd.) I  'paca  paourvatibya  nSit  dim  ava'i^a  iri- ^an  (sd.)  V.  r5.48 "';  —  daiuan  'pa  asaTan (sd.)  Yt7p.84(?).  tZu  apa  F.2d  und Vyt.44  s.  No.  i.J KompA.;  Ableit  —  S.  auch  apäaadpajcraifa-.
—  ai.  äpa,  np.  af-gandan  ('wegwerfen',  Bthl. IF.  //.  il6)JJ.  —  Pü.:  ii;tf,  (Komp.  auch): ape  hac,  apäl;  s.  nocli  No.  1.  —  "J  apa  F2d (Pü.:  <?^i-'und<t//)ist  aus  Komp.  losgeschält. — apa  x'aitju!  VyC.  44  stammt  aus  Y.  JJ,  4,  — »)  Pü.!  mideuilich.  —  J)  S.  noch  ^bar-  No.  19.
•  j.  apaosB-m.  Name  eines  Z>ii^'a*\  beson- ders des  Gegners  des  Tisiry a  {sd.):  a  dim (näml.  tistrim)  paiti.yas  nizdvaraiti  dalvd yö  °sö  aspake  k)hrpa  sämake  Yt.  tV.  21; 22';  —  ä  dim  bavaiti  aiwi.vanya  tistryö . .  daFnm  yim  °S>m  Yt  <.V.  28;  —  tauna- yeiti  dalum  "sjm  Yt  /Ä  2;  6.
*)  Der  austrocknenden  Sommerhitze;  vgl.  Yt. S.  2iff,,  Bd.  7.  8ff.,  2S.  39,  Dd.  gj.  II  (,  wo der  Name  volksetymotogiscji  als  „the  destructioti of  water"  —  äfi  ös  —  gedeutet  wird).
*apa-usa-  eig.  'austrocknend,  ausdörrend',  »um ai.V.  hati  'urit',  gr.  ä^ii».  —  iSchr.  des  mp, afiai-ai  (in  Aw.-Buchst)  s.  West  SBE.  5.  37  No.
•  j.  apa-kava- 1 )  Adj,  'der  hinten,  auf  dem Rücken  einen  Höcker  hat':  mit  ml  aeta- yiisäl  zao^rayä  /mnharintu  frakavö  nttl 'vB  Yt  5.  93.  2)  m.  Name  fUr  solches Gebrechen:  mä  (a%ra)  'vö  2.  29.
Pü.:  afäiköfak,  erl.:  ö  p«s.
•  j,  apa>gat«e  Inf.:  s.  unter  gatJe.
•  j.  apa-gaSa-  Adj.  — ?— :  gaoahe  '%aA£  V. 21.  2,
Komp.  mit  »gaia:  —  Pfi.:  afiäi  da  da.
dby  Google
73
apa-gaya-
apana-
74
•  j.  apa-gaya-  m.  'Ausscheiden  aus  dem LebcQ,  Ableben':  'gayehe  Y.  46.  4  PUZ,, 4g.  10  PiiZ.,  41.  3  PQZ.,  5j.  8  PüZ.,  16. 10  PüZ.,  62.  4  PiiZ.JJ
Sa. :  apafivatvam,  apajaiah.  —  »)  Pü.  verwendet das  Wort,  als  wäre  es  mp.  Y.  46.  4q  wird fröt  muri  bavel  mit  kus  i^gaytht  bavet,  Y.  41 flön  Aar  ti  amii  Ioh  m  yän  bavät  mit  ku  man apagayihi  mä  bavät  erläutert;  s.  noch  jUay- No.  1,
•  j.  apa-j-zära-  m.  'Abfluss,  {Wasser)ab- zwejgung'  a)  des  VouruAasa:  srayä  vouru.- kasaya  .  .  yeäke  . .  Aazannm  -ranam  . . kasal  aSsqm  °ranqm  c(&war>.sat»m  ayan.- baranqm..*arihas(a  me  *afi:aAka  Spö 'rö *vt)asaiti  vispJis  aoi  karsvqn  Y.  65.  4  £; —  aija  käu  'rö  bvat  zrayanAs  vouru.- kaiahe  vairil  yH  Aaosravä  nqma  Yt  ig. 56;  —  zrayauhs  vouru.kasahe  ,  .  vTspJ rairi/  a^araiti  vlsp}sca..nimraoi!  vlspSsca srlr!  'äire (AP.)'> \i.8.i,f>;~ katiht kaüht •,lire(XS.)  Ytj.ioi.  b)  der  Ratfka:\ tipa  guoim  'r>m  ra»hayh  Yt/5. 27,  j
Zum  V.  Tiar-.  — Vgl.  ai.  fikforä-m,  'Abflnss',  I prtkr.  nijjha/a-  m,  'Wasserfall'  (Wn.  AiGr.  i. 164,  241}.  —  Fü.;  apaa  und  apaaZiiJ  (bei Jamaspji  Dict.  245;  ävgatäS),  Npü.:  aävdän, —  «)  Pron.  flektirL
•  j.  apajcraosaka-  Adj.  'schmähsUchtig' : nivayaka  mpalnaka  apa.skaraka  'ia(NP.) ima  paiti.vJsfTUe  Yt5.95.
Ableit.  ins  ^apajrattsa-  m.,  zum  V.  xraos-.  — ■i.  vgL   aptirBSa-  m.  'Schmätiung'.
•  j.  apa.JcäadTa-  Adj.  'fort  von  der  Herr- schaft': hagmS  .  .  k^nsOnTm  °'hnm  nisä- \ayai  "H.  verjagte  den  K.  aus  seiner Herrschaft"  Y.f;.24".
Pü.:  afii  hal  i^atS^k.  —  •)  Eig.  'er  machte ihn  fort  . .'.
•  j.  apaxäirä-  f.  Name  eines  Landes: parsatgavS  dazgrSgavS  °rayS  daiAhSus "des  P.  und  D.  aus  dem  Land  A"  Yt IJ.127.
AngebL  a/u-xum-  Adj.  "milchlos',  »u  np.  ITr,
•  p.  apataram  Adv.  i)  'abseits,  anders- wo': t}\^  mann  kartam  id3  utä  ty^maiy 'ram  kariam  H.  2. 3.  2)  mit  ha!ä 'ausser,  abgesehen  von  — ':  'ram  hacä pärs^  "ausser  Persien"  D.  6. 3.
ASn.  aus  *apalara-  Adj.,  Kompar.  aus  apa.  — >i.  afaiaram  Adv.;  vgl.  got  aflarS.
•  j.  apat^e  Inf.  'zu  erreichen,  einzuholen': ap"  sbayäti  vyqs  apagatSe  vyära  "um  ein- zuholen ruft  (ihn)  der  Verfolger,  um  zu entkommen  der  Verfolgte"  Yty.35".
Zom  V.  af--    —    »)  S.  iSt.  Y.  S7-  *9J    Gr>N. KZ.  30.  520.
j.  afaili  Idt  N.  S4'-  1>'^  apailiti^,
```


## [2026-09-04T22:53:48.639Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC apo ===\"; grep -n \"^apo\\|^apo-\\|^apo \" IEC.txt | head -10; echo \"=== WLD Bd1 leaf 56 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==56' incoming/WLD/WLD_Bd1_pages.txt | head -35",
 "description": "Mann and Walde-Pokorny apo"
}
```


### [2026-09-04T22:53:50.366Z] TOOL RESULT

```
=== IEC apo ===
631:apolos “strong; strength’. Cf. opalos, op- Gk. cf. eü-epelia; an-epelia, n-ēpeléð olig- epelie; Illyr. (ambig.) Aplus, a, o (proper names) beside Dalmatian Oplus, a (cf. opolos); Lat. cf. copula (&bond', for *co-ap-); OE (ambig.) afol ‘power’; ON afl
632:apomos “last, furthest'. Cf. apo. WP I, 49 Skt. apamáh, apama; Av. apomo; Hitt. cf. appan “after, warde": OAIb. i pér-apém “last? (*pro-apomo-)
633:apotes, aptos (strong; strength’. Cf. apnu-, apolos, op-. WP I, 46 Alb. i aftë (Cable, if not a Lat. LW); Lat. aptus “tied, joined, fitted, close, proper; OE eafop 'strength' . apis (?) ‘insect’. Cf. empis Lat. cf. apis, gp. apium ‘bee’; OCz. op-oka, -uka, ap-oka ‘honeycomb’ beside Cz. jepice ‘mayfiy’.
645:apo (apo, apo, po) “away; from, after", WP L 47. See next Skt. ápa; Av. apa; Oss. fá-, px.; Tokh. -àp, suffix; Arm. v-, px.; Hitt. appa 'afterwards; again, back"); -apa (suff. ‘so, then" queried); Myc. apu; Gk. apó; Alb. pa ‘without’; f-, px.; Lat. ab (perhaps also as a fused px. in Lat. p-arco, p-av6o, paro, pudeo, pando, etc.); Ir. fo-, px.; OBr. W o; Bret. (WSP) a; Cor. a; Go. af; OHG aba “away; from’, abo "but: OE of; ON af; OCS po ('after. In sense of "about see upo); Srb. pa (fr. *po “and, then, so’: Hitt. -apa); Li. po (WSP in sense of 'after); cf. apa-6ià ((bottom?. See apetios above); Latv. cf. apa-k3 “below? apo-, px. *not-, un-'. See apo above Skt. cf. ápa-bhis ‘fearless’; Gk. apó-thrix ‘hair- less"; Alb. pa, pa- ‘without; un-'; Go. af-guds ‘godless’
646:apos, ios (1) ‘miid, gentle, thoughtful Skt. apyam ‘friendship’; Gk. épios; OCS cf. za-japü ‘thought’; Li. opüs ‘sensitive, tender, gentle’ |
647:apos, ios (2) “taking, seizing, snatching’. Cf. āpnu-. WP I, 46, 47; I, 121 Skt. åpyah ‘obtainable’; apyam ‘alliance’; Av. apa-; Gk. cf. n-épios (simple, childish’: Cz. nejapny 'inept'); ON œfr ‘vehement’; Cz. japny “clever, smart’; OCS cf. ne-za-japü “care- lessness'
648:aposthos, us, ios ‘stopping; stop, confronta- tion’. Cf. apo, sthà- Skt. apasthuh; Ir. fos “stop, rest; OE æfest ‘hate’; aphetic in fæsten ‘fasting’; ON fasta; OCS postü “fasting”
649:apo-teros ‘further, following’. WP I, 47. Cf. apo, -teros Skt. OPer. apataram; Arm. var, varo, i vajr, vajra- ‘down, below’; Gk. apóteros; Cor. ater, adar “out of, without’; Go. aftaro (:Gk. apo- . téro); OHG aftaro; ON aptr, eptir; OE efter
650:apo-tokos, à flow from, stream, derivation’. See apo, tek- Gk. (formally) apótokos “resulting from'; Arm. vtak, i, av ‘brook’; OCS potokü ‘stream’; Li. patakà 'flow, drip, leak; pl. small beer
=== WLD Bd1 leaf 56 ===
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
*abnes   aus den obi. Kasus entsprang lat. amnis , wahrend im keltischen
         ;


abdo(n) abnes zu *aba (mir. ah), *abnes (daher abann) ausgeglichen wurde.
             :




  Ygl. im allgem. Curtius 5 469.                           — Uber      gr. ojiog „pflanzlicher Saft“    s.   u.
suaq'ios.


3. ap-,          ap- „gebrechlieh; Schaden“.
  Ai. apva „Krankheit, Krankheitsdamon“, av. (von einem -es-St.) af'sa- m.
„Schaden, Unheil“, afinnan- n. „Schaden, Nachteil“; lit. opus „schwach, wund,
                     11
gebrechlich    (Charpentier KZ. 40, 442ff.), vermutlich gr. pn edavog „ge-
```


## [2026-09-04T22:54:01.644Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT AB- ===\"; grep -n \"^AB-\\|^ABNORMAL\\|^OF\\b\\|^OFF\" SKT.txt | head; echo \"=== KLN ab-, abnormal ===\"; grep -n \"abnormal\" KLN_1966.txt KLN_1971.txt | head -5; echo \"=== LEW ab ===\"; grep -n \"^ab, \\|^ab \" LEW_1910.txt LAT.txt | head -5",
 "description": "Skeat/Klein/Walde Latin ab"
}
```


### [2026-09-04T22:54:01.745Z] TOOL RESULT

```
=== SKT AB- ===
78:OF
22812:OF   DOUBLETS.
=== KLN ab-, abnormal ===
KLN_1971.txt:4485:abnormal, adj. — A blend of L. abnormis and 
KLN_1971.txt:4490:Derivatives: abnormal-ity, n., abnormal-ly, adv., 
KLN_1971.txt:4491:abnormal-ness, n. 
KLN_1971.txt:15883:See abnormal. 
KLN_1971.txt:15895:anoxemia, anoxaemia, n., abnormal condition of 
=== LEW ab ===
LEW_1910.txt:5030:ab LT
LEW_1910.txt:6873:ab (air.) I 40 — aball (air.) I 3  abann (air.) I 40, | xa
LAT.txt:746:ab, abs, a: preverbe et preposition. Abs presente vis-a—vis de ab le meme
LAT.txt:3204:ab "eo" compositum solum mutauit paenultimam e iri i; itaque in -io
LAT.txt:3740:ab ambitu et frangendo: ab eo leges iubent in directo pedum VIII octo
```


## [2026-09-04T22:54:05.227Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4478,4496p' KLN_1971.txt; echo \"=== LAT ab ===\"; sed -n '744,775p' LAT.txt",
 "description": "Klein abnormal; Ernout-Meillet ab"
}
```


### [2026-09-04T22:54:05.310Z] TOOL RESULT

```
See prec. word and negation. 

Abner, n., masc. PN.; in the Bible, commander 
of Saul. — Heb. AbhnSr, lit. ‘my father is light’, 
fr. abh, ‘father’, and ner, ‘light’; cp. the Baby- 
lonian PN. Abunuri. For the first element see 
Aboth, for the second see Menorah. 
abnormal, adj. — A blend of L. abnormis and 
ML. anormalis, this latter itself being a blend 
of L. anomalus and normalis. See anomalous and 
norm and cp. anormal. 

Derivatives: abnormal-ity, n., abnormal-ly, adv., 
abnormal-ness, n. 

abnormity, n. — L. abnormitds, formed with suff. 
-itas fr. abnormis. See prec. word and -ity. 
aboard, adv. and prep. — Formed fr. a-, ‘on’, 
and board. 
=== LAT ab ===
issue sans doute de ah + a, cf.J.-B.nofmann, Lat .Umgangsspr., p.19. Cf.gr. a.,
oa., a, etc.
ab, abs, a: preverbe et preposition. Abs presente vis-a—vis de ab le meme
elargissement en -s que sus- de *subs>*sups, os- de *obs>*ops vis-a—vis de ob,
sub. En composition, ab s'emploie devant voyelle, devant h et devant les con?
sonnes d, l,n, r,s: abauus, abegi, abigo, aborior, abuti,-, abdo, ablatus, abnuo,
abripio, absum (prononce apsun ); abs- devant les explosives c et t: abscondo,
abstraho, abstineo, abstuli (en face de ablatum)-, devant un p initial, abs se
r<*duit a as-: asporto, aspello et aspernor de *ab(s)pemor-, a est la forme
reduite de *abs devant les labiales m,u,b; anoueo, duello de a(b)znoueo,
*a(b)zuelld, abito, cf. seuiri de *sexuiri. Afui, parfait de absum, est une
forme analogique; devant / le latin recourait d'ordinaire a un autre preverbe,
au-, cf. plus bas. Dans la phrase, les emplois de ab, abs, a sont aussi regles
par 1'initiale du mot suivant, et suivant les memes rfegles qu'en composition;
toutefois 1'usage comporte plus de liberte: on trouvera par ex. abs te et
d te, etc.
Ab signifie "en s' 61 oignant, en partant de, depuis, de", et marque le point
de depart (des environs, du voisinage d'un endroit, et non de 1 1 interieur de),
ce qui explique qu'il aceompagne 1'ablatif; il se dit de 1'espace comme du
temps, avec ou sans idee de mouveraent: Caesar maturat ab urbe proficisci, Ces.,
BG. I7; hic locus aequo fere spatio ab castris Ariouisti aberat, id., ibid., I 43,
x; mulieres... ab re diuina ("au sortir de", d'ou "aprbs") apparebunt domi,
Pl., Poe.617; secundus a rege, Hirt., B.A 1 . 66 . C'est le sens de "en s'eloignant
de" qui explique ab re "contrairement’ aux int6rets" (par opp. a in ren). A
absum s'oppose adsum, et A absens, praesens (la variation de preverbe est
instructive)db se distingue de ex et de de. Ex marque la sortie de 1 'interieur
d'un lieu, et s'oppose k in qui indique la presence ou 1'arrivee a 1'interieur
d'un endroit. Quant a de-, il exprime une idee de retranchement, de diminution,
et aussi un mouveraent de haut en bas, cf.Varron,fgra.ap.Scaurum GOC VII 32,3.
Gcneralement les differences de sens sont observees par les bons ecrivains.
Ennius distingue: Diana facem iacit a laeua, Sc.33; olli crateris ex auratis
hauserunt, A. 624; Hectoris natam de Troiano muro iactari, Sc.83.Cic4ron,Caec.
```


## [2026-09-04T22:54:24.084Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"prep\\. and prefix\\|prep\\. with abl\\|prefix ‘to,\\|‘unto’\\|prev\\. ‘to\" KNT.txt | head -20",
 "description": "Kent preverbs list"
}
```


### [2026-09-04T22:54:24.126Z] TOOL RESULT

```
2858:yàtà ‘unto’, of goal in place; see also уйй à, П. $271. Prepositions wiru Two ов Моке Cases
5012:abiy prep. and prefix ‘to, against, in addition to’: GAv. aibi. LAv. aiwi, Skt. abht; conflux of pIE *mbhi, oHG umbi ‘round about’, and pIE *obhi, oCS ой ‘beside, by’.
5177:ud prep. and prefix ‘up’, becoming Iran. us- uz- before dentals ($85): Av. us- uz-, Skt. ud, pIE *ud (and *üd in NEng. out, NHG aus): ud with verbal root раф, us- in ustaxand-, u(z)- in uzma- (S84).
5178:ира (i.e. upd, cf. 5140.1) prep. and prefix ‘to- ward’: Av. ира, Skt. úpa, Gk. iad, Lt. s-ub ‘under’, pIE “иро.
5655:pariy prep. and prefix ‘around, about’: Av. pairi, Skt. pári, Gk. тері, Lt. per ‘through’, pIE *peri ($64, §75.1, $113, §140.1). Prep. with aec. ‘about’ DB 1.54. Prefix-with ay-, bar-; ef. also pariyana-.
5819:(2) Prep. with loc., ‘unto’: DSf 32, 34.
5820:(3) Double prep., yàtà à, with abl. (not with ace., as taken by Schwentner, ZII 6.173), ‘unto’: DPh 6, 7; DH 5, 6.
```


## [2026-09-04T22:54:26.851Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5810,5825p' KNT.txt",
 "description": "Kent ā entry"
}
```


### [2026-09-04T22:54:26.903Z] TOOL RESULT

```
(1) ‘Ionian’: Yauna nsm. A?P 26. Yaund npm. DSf 33f, 48; as nam. (556.1) А?Р 23.
(2) ‘Ionians’, as province: Yauná npm. DPe 12{; DNa 29; DSe 271°; DSm 10°; XPh 23.
(3) ‘Tonia’: Yauna nsm. DB 1.15; DNa 28; DSm 8°. Yaund absm. DSf 42.
yaumant- adj. ‘trained, skilled’: adj. to *yauman-, with vriddhi (5126, $152.T, ў}155.Ш), from root seen in Skt. уйин ‘harnesses, fastens’, ef. Hz. ApI 365-6 (not with Sen 249, ‘agile’, from *yduman-aina-, fem. -2). See also ayáu- mani-.  yüumainii пзш. (with epenthesis, $127; Lg. 15.173) DNb 40.
уашлуй- sb. ‘canal’ (§48): NPers. Joi ^water- course, canal’, cf. perhaps Skt. (Vedic) yavyd isf. ‘stream, river’; perhaps deriv. (§144.V) of root ay-/i-/yà- ‘go’ (JAOS 62.271). yauviyd nsf. DZe 10. yaunydm asf. Оле 8f, 12.
yaka- sb. (§6, $143.IV) a kind of wood (oak, Scheil 25.28, but if so, not cognate, Bv. BSLP 30.1.01; Afghan cypress, Kónig, Burgbau 54-61; mulberry, Wb. AfOF 7.42; teak, Hz. AMI 3.61-2; certainly not ‘timber’ in general, as taken by Gray, AJP 53.68). yaka nsf. DSf 34.
yacty, see ya-.
yaté conj. and prep.; perhaps уй isn. or уй! absn. of ya- + -tă as in сий, q.v. (wrongly Sen 11). (1) Соп]. ($294) ‘until’: DB 1.25, 54, 69; 2.28, 48, 63; DNa 51; DNb 23; DSf 24; XPh 45. ‘when’ DB 481. ‘while’ DB 2.6; 3.77. ‘as long as’ DB 4.51.
OLD PERSIAN
(2) Prep. with loc., ‘unto’: DSf 32, 34.
(3) Double prep., yàtà à, with abl. (not with ace., as taken by Schwentner, ZII 6.173), ‘unto’: DPh 6, 7; DH 5, 6.
yatà conj.: GAv. уаба, LAv. yada, Skt. ydtha: rel. ya- + adv. Suffix -tha (876.1I, 4118). It takeg a verb in the indie, except that the pres. subj. shows future time in temporal clauses (DNb 281); details of syntax, $295.
(1) ‘as’: DB 1.28 (уада-50т), 63, 67, 69; 4.35, 52; 5.17°, 29, 33^; DNa 37; DS] 3; DZe 11°, 12.
(2) ‘as well as’, comparing clauses: DNb 39 (wrongly Hz. ApI 362).
(3) ‘when’: CMb 3; DB 131, 91°; 2.22, 65; 3.34; DNb 28f (yatà-maiy); DSi 3; XPf 25, 32 (yaba-maiy), 36; XPh 29 (уада tya).
(4) ‘after’, with prec. or foll. pasáva: DB 1.27, 33, 72, 73; 2.32, 52; 3.3; 4.5; 5.3, 28°; DNa 311; DSf 25; XSc 3°.
```


## [2026-09-04T22:54:35.184Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^وارون\\|^وارونه\\|^عفریت\\|^بی:\" MON_part1.txt MON_part2.txt | head -10; echo \"=== search efrit ===\"; grep -n \"عفریت\" MON_part1.txt MON_part2.txt | head -10",
 "description": "Mo'in varun, efrit"
}
```


### [2026-09-04T22:54:35.294Z] TOOL RESULT

```
MON_part2.txt:14065:وارونه کردن حروف یک کلمه. . صسح.- 
MON_part2.txt:83342:وارون: «ت22*[- وارونه] (ص.) باژگونه, 
MON_part1.txt:18048:وارون شدن. آوازه شدن» شهرت یافتن. 
MON_part1.txt:26595:بی: آ" [- ابی] (پش.) علامت نفی و سلب 
MON_part1.txt:33796:بی: ۷-6 ,-۳2۷ (حر. اض.) برای» به جهت 
MON_part1.txt:93676:بی: اجه [ع.] (.) آهو؛ ج 
=== search efrit ===
```


## [2026-09-04T22:54:39.145Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26593,26605p' MON_part1.txt; echo \"===\"; sed -n '83340,83350p' MON_part2.txt; echo \"=== efrit search alt ===\"; grep -n \"عفريت\\|عفر یت\\|عفر بت\" MON_part1.txt MON_part2.txt | head -5",
 "description": "Mo'in bi and varun entries"
}
```


### [2026-09-04T22:54:39.247Z] TOOL RESULT

```
گزیده‌ترین. 

بی: آ" [- ابی] (پش.) علامت نفی و سلب 
است که بر سر اسم درآید و کلمه را صفت 
سازد (معنی صفت منفی دهد): بیجاره؛ 
بی‌خرد» بی‌ریا» بی‌زور» بیکار. گاه بر سر 
اسمی در آبد و قید مر کب سازد: بی‌شکد» 
بی شبهه» بی‌گفتگو. 

بی‌اب: 0 (ص‌مر.) بدون آب؛ فاقد 
آب. بسی‌رونق» بسی‌طروات. بی آبرو» 
بی‌اعتبار. 

===

زگیل. 
وارون: «ت22*[- وارونه] (ص.) باژگونه, 
واژگون» سرنگون» نگونسار» معکوس. 


بررعکس؛ مخالف. (مج.) ناسا رک نحس» 
شوم. بخت وارون: بخت بد» طالع شوم. 
واروف: (6-):۷2۳50 [- وارون] (ص.) 
بازگونه» وازگون» سرنگون. برعکس» 
مخالف. (مج.) نامبا رکك» نحس» شوم. 
=== efrit search alt ===
MON_part1.txt:96994:عفر یت: ۰1:1 [ع.] (.) دیو» اهریمن. غول.
```


## [2026-09-04T22:54:55.909Z] TOOL CALL #83: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ep%C3%B3|PIE root apo- (page 59 root box Apo/Apa/Apu/Pu/Po)\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%DB%8C|Persian bi 'without' < MP ape < PIE h2epo (page 59 node 3)\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%AF%D8%B3%D8%AA%D8%B1|Persian bidastar 'beaver' etymology (page 59 node 3)\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D9%81%D8%B1%DB%8C%D9%86|Persian afarin < MP afrin < PIr *a-fraiH (page 59 nodes 8-9)\" \\\n \"https://en.wiktionary.org/wiki/%D8%B9%D9%81%D8%B1%D9%8A%D8%AA|Arabic ifrit < Middle Iranian afrid (page 59 node 10)\" \\\n \"https://en.wiktionary.org/wiki/%D9%88%D8%A7%D8%B1%D9%88%D9%86|Persian varun < MP abaron (page 59 node 16)\" \\\n \"https://www.etymonline.com/word/ab-|Latin ab- < PIE apo- (page 59 nodes 17-18)\" \\\n \"https://www.vajehyab.com/moein/%D8%A2%D9%81%D8%AF%D9%85|Mo'in s.v. afdom 'last' (page 59 node 5)\" \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-04T22:55:02.254Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/20b07da4d882eaeb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/53d27b33f9803406.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f287e6eab01e8406.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8cabccc1fd67ab25.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d6f9db27bac45962.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/83a48a758af942d9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/432186cf2d1f9b58.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c80c10b02602be75.txt
```


## [2026-09-04T22:55:05.084Z] TOOL CALL #84: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py",
 "description": "Read verify_check"
}
```


### [2026-09-04T22:55:05.126Z] TOOL RESULT

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


## [2026-09-04T22:56:12.429Z] AGENT

Now I'll write the verification file.


## [2026-09-04T23:02:38.634Z] TOOL CALL #85: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/out && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/out/build.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nout = {\n \"pdf_page\": 59,\n \"book_page\": 29,\n \"verified_by\": \"claude-fable-5-1\",\n \"verified_on\": \"2026-09-04\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Apo, Apâ, Apu, Pu 3, Pô 1\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *apo / *h₂epo (also *ap-u, *pu, *po) 'off, away'\",\n   \"note\": (\"Pokorny IEW p.53 heads the entry exactly 'apo (po, ap-u, pu) ‚ab, weg‘' and runs it to p.55, \"\n            \"so four of Nourai's five variants (Apo, Apu, Pu 3, Pô 1), the language label and the gloss 'off' \"\n            \"are literally Pokorny's; Walde-Pokorny I 47ff. and Watkins/AHD 'apo-. Also ap-. Off, away' agree. \"\n            \"The one addition is 'Apâ' with long ā, which is not in Pokorny, WP, Watkins or Mann, and it is the \"\n            \"peg on which Nourai hangs the whole ā- branch (nodes #6-#9). Old Iranian/Indo-Iranian ā 'to, toward' \"\n            \"(Skt. ā́, Av./OP ā) is a separate particle (PIE *ē/*ō, Wiktionary *h₂ed), not an ablaut grade of *apo-; \"\n            \"Horn (Grundriss no.1) and Cheung both handle it as an independent preverb. Hence the root box is right \"\n            \"but over-extended, and everything under 'Apâ' has to be judged separately. A second cross-cutting problem: \"\n            \"Nourai's BQT:1086 (cited on nodes #1, #6, #7) falls in the س- section of Borhān-e Qāţeʿ vol. 2 and has \"\n            \"nothing to do with apa/ā, and KLN:168 on node #8 is Klein's 'behemoth–beige' page — almost certainly a \"\n            \"slip for KNT:168, which does carry apadāna-.\"),\n   \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%82ep%C3%B3\",\n               \"https://www.etymonline.com/word/ab-\"],\n   \"ref_check\": [\n     {\"ref\": \"POK:53\", \"status\": \"supports\",\n      \"note\": (\"POK_01.txt leaf 61 (= printed p.53): 'apo (po, ap-u, pu) ‚ab, weg‘ — Ai. ápa ‚weg, fort, zurück‘ … \"\n               \"av. ap. apa ‚von-weg‘ … gr. ἀπό … lat. ab …'; the entry continues 'po:' (p.54) and 'ap-u … pu' (p.55). \"\n               \"Also on p.53: 'über privatives *ap- im Iran. und Gr. s. Schwyzer ZII. 6, 230ff.' — the privative that \"\n               \"underlies node #2/#3. Exactly the root, language and gloss Nourai prints; only 'Apâ' is absent.\")}\n   ],\n   \"nodes\": [\n\n    {\"id\": 1, \"lang\": \"Avestan\", \"words\": \"ap 2, apa; apama, apatama\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Avestan apa is the inherited continuant of PIE *apo 'off, away' with regular Iranian retention of \"\n                    \"the medial -p- (unlike Indic, which also keeps it: Skt. ápa). Bartholomae AiW col. 71-72 lists \"\n                    \"'apa 1) Adv. ‚weg, getrennt von—‘ (nur Komp.) 2) Praev. (mit karət-, gaud-, gam-, bar-, yam-, štar- usw.)', \"\n                    \"i.e. it survives mainly as a preverb, which is exactly the use Nourai's daughter nodes need. \"\n                    \"The superlative is formed with PIE *-m⌥o-: *apo-mo- > Av. apəma- 'the last (in time)', and with the \"\n                    \"double superlative *-t̥mo- (Skt. -tama-) *apa-tama- > MIr. abdom. Nourai's added gloss 'to' for apa is \"\n                    \"wrong (apa is ablatival, 'away from'), and 'apatama' is a reconstruction, not an attested Avestan form.\"),\n     \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%82ep%C3%B3\"],\n     \"ref_check\": [\n       {\"ref\": \"POK:54\", \"status\": \"supports\",\n        \"note\": (\"POK_01.txt leaf 62 (= p.54): 'Ai. ápara- ‚hinterer; späterer, folgender; anderer‘ … av. ap. apara- \"\n                 \"‚hinterer, späterer, folgender‘ … Sup. ai. apamá-, av. apəma- ‚der entfernteste, letzte‘' — precisely \"\n                 \"Nourai's 'apama … last'.\")},\n       {\"ref\": \"BQT:1086\", \"status\": \"not_found\",\n        \"note\": (\"BQT_v2_pages.txt leaf 543 (printed p. ≈1086, offset independently pinned on this repo's page-101 check \"\n                 \"at BQT:1077 = leaves 539-540) is in the س section — سبز باغ، سبز بال، سبزراغ — with no entry on apa or on \"\n                 \"the prefix آ-. Could not confirm this citation in the Amir Kabir/Moʿin pagination Nourai says he used.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"AiW col. 71-72 (apa) and col. 79-80 (apəma-)\", \"stance\": \"supports\",\n        \"note\": (\"BRT.txt: 'apa 1) Adv. ‚weg, getrennt von—‘ … 2) Praev.'; and 'j., g. apama-, g. apəma- Adj. ‚der \"\n                 \"(zeitlich) letzte‘, nur von dem, was am Ende der Dinge … eintreten wird … Superl. aus apa; vgl. apara-'. \"\n                 \"Bartholomae has no apatama- headword.\")},\n       {\"src\": \"IEC\", \"where\": \"Mann, s.v. apo and apomos\", \"stance\": \"supports\",\n        \"note\": (\"IEC.txt: 'apo (apo, apo, po) ‚away; from, after‘, WP I, 47 … Av. apa … Lat. ab …' and 'apomos \"\n                 \"‚last, furthest‘. Cf. apo. WP I, 49 Skt. apamáḥ … Av. apəmə'.\")},\n       {\"src\": \"SNS\", \"where\": \"glossary p.26 s.v. abdum/āfdum\", \"stance\": \"supports\",\n        \"note\": \"SNS.txt line 3135: 'abdum/āfdum … (Bthl. 80-81) *apatəma, apama … awadum'. Nourai's pair 'apama, apatama' is verbatim this.\"},\n       {\"src\": \"WLD\", \"where\": \"WP I 47ff.\", \"stance\": \"supports\",\n        \"note\": \"WLD_Bd1_pages.txt leaf 56 running head 'ap-, ap- — apo, po 47': the *apo entry that Pokorny cites as 'WP. I 47 ff.'\"}\n     ]},\n\n    {\"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"apě, ape\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Middle Persian abē- (Book Pahlavi ʾPʿ(y)-, Manichaean ʾby-) 'without, -less' goes back to an Old \"\n                    \"Iranian instrumental/locative *apa-i ‘away from’ built on the preposition apa; Hübschmann sets it up \"\n                    \"as OP *apaiy from apa + i (like naiy 'not' = na + i), and notes that the form arose in composition, \"\n                    \"because a free *apaiy would have given NP āb. It is productive only as first member of compounds \"\n                    \"(abē-bīm 'fearless', abē-gumān 'certain', abē-niyāz 'free from want'). This is the standard modern \"\n                    \"account and matches Nourai's arrow Av. apa → Phlv. apē exactly.\"),\n     \"sources\": [W + \"%D8%A8%DB%8C\"],\n     \"ref_check\": [\n       {\"ref\": \"AEF:309\", \"status\": \"not_checked\",\n        \"note\": (\"Khaleqi Motlaq's Asās-e Ešteqāq-e Fārsi is not online (refs_online: 'catalog' only). It is the Persian \"\n                 \"translation of Horn's Grundriss with Hübschmann's notes, and the corresponding original, Horn no.247, \"\n                 \"does say what Nourai's arrow says (quoted under 'consulted').\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"MacKenzie p.3 s.v. abē-\", \"stance\": \"supports\",\n        \"note\": \"PHD_mackenzie.txt: 'abē- [ʾP(y)- | M ʾby-, N bē] without, -less. ~-bar [-bl] fruitless. ~-bēš unharmed. ~-bīm fearless … abē-gumān without doubt, certain'.\"},\n       {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p.≈28 s.v. apē-\", \"stance\": \"supports\",\n        \"note\": \"NYB_vol2_glossary.txt line 571: 'apē- [ʾpy-, ʾpyd] v.s.v. apa-', with apē-bīm 'fearless', apē-brāt 'brotherless', apē-cār, apēgumānēh.\"},\n       {\"src\": \"HRN\", \"where\": \"no. 247, p.56-57\", \"stance\": \"supports\",\n        \"note\": (\"HRN.txt: '247. bē, ebē ‚ohne‘. phlv. ape- (päz. awe-), z.B. ape-bīm, ape-gumān etc. … Wohl ein Casus \"\n                 \"zur Praeposition apa ‚getrennt, fern von‘' — with Horn's own caution 'wohl'.\")},\n       {\"src\": \"HUB\", \"where\": \"Persische Studien no. 247\", \"stance\": \"supports\",\n        \"note\": \"HUB.txt line 1096: 'Np. bē = pāz. awē, phl. apē setze ich = ap. *apaiy aus apa + id, wie naiy ‚nicht‘ = na + id … sonst wäre *apaiy zu np. āb geworden.'\"}\n     ]},\n\n    {\"id\": 3, \"lang\": \"Persian\", \"words\": \"bî «بی-»; bî-dastar «بیدستر»\", \"verdict\": \"disputed\",\n     \"derivation\": (\"New Persian بی bī- 'without' is the regular continuation of MP abē-: the initial a- of the \"\n                    \"unstressed prefix was lost in NP (MP abē-bīm > NP bī-bīm), the older stage surviving as ابی abē/ebē \"\n                    \"in early NP verse, which Nourai correctly prints in the box (ابی-) and Moʿin glosses \"\n                    \"'بی: [= ابی] (پش.) علامت نفی و سلب'. That half is confirmed and is the standard view (Horn 247, \"\n                    \"Hübschmann 247, MacKenzie s.v. abē-, Wiktionary بی < ابی < MP apē < PIE *h₂epo); the compounds in the \"\n                    \"extras (بی‌نیاز، بی‌بهره، بی‌شمار) are all straightforward bī- privatives. The second word is the problem. \"\n                    \"بیدستر bīdastar 'beaver' is analysed by Moʿin (and before him by Borhān-e Qāţeʿ) as بی 'without' + \"\n                    \"دستر glossed 'داس کوچک، اره' — 'without a sickle/saw', i.e. an animal that fells trees with no tool. \"\n                    \"That is a transparent folk etymology of the Borhān type: دستر 'small sickle' is not otherwise attested, \"\n                    \"and the word has the variants ویدستر vidastar and بادستر bādastar (the latter in Moʿin's own entry), whose \"\n                    \"v-/bā- cannot come from the privative bī-. Wiktionary (tentatively) takes the first element to be \"\n                    \"*widʰu- 'wood, tree', giving a 'wood-eater/wood-cutter' compound; Horn, Hübschmann and Bartholomae treat \"\n                    \"the Iranian beaver word as Av. baβri- / MP bawrak (Horn no.181) and never connect bīdastar with bī-. \"\n                    \"So the node's first word is confirmed and its second is a folk etymology inherited from Nourai's source.\"),\n     \"sources\": [W + \"%D8%A8%DB%8C\", W + \"%D8%A8%DB%8C%D8%AF%D8%B3%D8%AA%D8%B1\"],\n     \"ref_check\": [\n       {\"ref\": \"AEF:309\", \"status\": \"not_checked\", \"note\": \"Not online; its original, Horn no.247, supports the bī < apē half (quoted at node #2).\"},\n       {\"ref\": \"MON:131\", \"status\": \"supports\",\n        \"note\": (\"Moʿin does say what Nourai says, for both words. MON_part1.txt: 'بی: [= ابی] (پش.) علامت نفی و سلب \"\n                 \"است که بر سر اسم درآید … بی‌خرد، بی‌ریا، بیکار'; and 'بیدستر: [بی + دستر (داس کوچک، اره)؛ بی‌اره] \"\n                 \"… پستانداری از راسته جوندگان … بادستر، بتر، وبر'. The page number could not be pinned in the 2-vol \"\n                 \"Adena OCR (no page markers), but the entries are verbatim as Nourai reports them — including the \"\n                 \"'without a saw' gloss that modern etymology rejects.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"MacKenzie p.3 s.v. abē-\", \"stance\": \"supports\", \"note\": \"'abē- [ʾP(y)- | M ʾby-, N bē] without, -less' — MacKenzie himself gives the New Persian outcome bē.\"},\n       {\"src\": \"HRN\", \"where\": \"no. 247 and no. 181\", \"stance\": \"partial\",\n        \"note\": (\"Horn 247 gives bē/ebē 'ohne' < phlv. ape-, supporting bī; but Horn's beaver word is no.181, 'aw. bawri- \"\n                 \"‚Biber‘; phlv. baprak d. i. bawrak ‚Biber‘', and he has no entry bīdastar at all.\")},\n       {\"src\": \"MON\", \"where\": \"s.v. بی and بیدستر, جند بیدستر\", \"stance\": \"supports\",\n        \"note\": \"Also 'جند بیدستر [= جند بادستر] … خصیة الکلب البحر، خایهٔ سگ آبی' (castoreum), which shows the bādastar variant.\"},\n       {\"src\": \"BQT\", \"where\": \"vol. 2, s.v. جند بیدستر\", \"stance\": \"partial\",\n        \"note\": \"BQT_v2_pages.txt: 'جند بیدستر باشد. گویند خایهٔ سگ آبی' — Borhān knows the word but here gives only the substance, not an etymology.\"}\n     ]},\n\n    {\"id\": 4, \"lang\": \"Pahlavi\", \"words\": \"afdom, awdum\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Middle Persian abdom / afdom (Book Pahlavi ʾp̄dwm, Manichaean ʾbdwm, Pāzand awadum) 'last, finally' \"\n                    \"continues Old Iranian *apa-tama-, the *-tama- superlative of apa 'away, behind' — the same formation as \"\n                    \"Avestan apəma- but with the longer suffix. Intervocalic *-t- after the labial gave the Book Pahlavi \"\n                    \"spelling with p/f, and the word was borrowed into Biblical Aramaic as ʾappetōm (Ezra 4:13). Nourai's two \"\n                    \"spellings afdom and awdum are exactly the Book Pahlavi and Pāzand readings the handbooks print.\"),\n     \"sources\": [],\n     \"ref_check\": [\n       {\"ref\": \"SNS:26\", \"status\": \"supports\",\n        \"note\": (\"SNS_pages.txt leaf 29 (≈ printed p.26 — offset 3 for the front matter), headword \"\n                 \"'abdum/āfdum: … (Bthl. 80-81) *apatəma, apama … awadum … (Mir. Man. II,44) ʾbdwm'. Tavoosi's glossary \"\n                 \"gives both of Nourai's forms and the Old Iranian etymon.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"MacKenzie p.3 s.v. abdom\", \"stance\": \"supports\",\n        \"note\": \"PHD_mackenzie.txt: 'abdom [ʾp̄dwm | M ʾbdwm] last, final(ly). ~ih: finality, end.'; the English index has 'final(ly) abdom, pasēn' and 'last (a.) abdom'.\"},\n       {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p.≈38 s.v. avdom\", \"stance\": \"supports\",\n        \"note\": \"NYB_vol2_glossary.txt line 788: 'avdom [ʾpdwm] last … adv. in the end, finally, ultimately … OIr *apa-tama-, borrowed in B.-Ar. ʾappetom Ezr. 4:13; MPrs ʾbdum … Paz. awadum, awadim.'\"},\n       {\"src\": \"HRN\", \"where\": \"no. 38, p.10\", \"stance\": \"supports\",\n        \"note\": \"HRN.txt: '38. āfdum ‚letzter‘ … aw. *apətama ‚letzter‘; phlv. afdūm, päz. awdum ‚letzter‘.'\"}\n     ]},\n\n    {\"id\": 5, \"lang\": \"Persian\", \"words\": \"âfdom «آفدُم»\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"NP آفدم āfdom 'last, at last' is MP abdom taken over into early New Persian; it is a rare, early word \"\n                    \"(Mojmal al-tawārīkh, Rūdakī, Abū Šukūr, Asadī), usually met in the frozen adverbial بافدم bāfdom = \"\n                    \"be + āfdom 'in the end', which is the form Nourai's extras and Rūdakī quotation give. Hübschmann's \"\n                    \"caveat is worth recording: phonologically one expects short a-, afdum, and Nöldeke suggested (ap. \"\n                    \"Hübschmann no.38) that the word was already obsolete in the earliest NP poets' day and was therefore \"\n                    \"mispronounced with ā-. The word died out and has no modern currency.\"),\n     \"sources\": [\"https://www.vajehyab.com/moein/%D8%A2%D9%81%D8%AF%D9%85\"],\n     \"ref_check\": [\n       {\"ref\": \"MON:72,462\", \"status\": \"supports\",\n        \"note\": (\"Moʿin s.v. آفدم: MON_part1.txt line 3841 'آفدم: … (ص.) آخرین، پسین، نهائی'; vajehyab's Moʿin text \"\n                 \"gives '۱ - آخرین، نهایی ۲ - سرانجام، فرجام'. Two page references presumably = آفدم and افدم; the 2-vol OCR \"\n                 \"carries no page markers, so only the entries, not the numbers, could be checked.\")},\n       {\"ref\": \"FRS:184\", \"status\": \"supports\",\n        \"note\": (\"Asadī's Loghat-e Fors, FRS.txt line 13123ff.: 'عاقبت باشد [رودکی گوید:] مکن خویشتن از ره راست گم / \"\n                 \"که خود را بدوزخ بری بافدم', variant note 'باندم عاقبت کار باشد » چ ؛ بافدم آخر باشد', and Abū Šukūr's \"\n                 \"'چه بایدت کردن کنون بافدم'. This is the 1319 Eqbāl edition (leaf 360-361), not the 1365 Kharāzmi one \"\n                 \"Nourai paginates, so the entry rather than the page number is confirmed.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"HRN\", \"where\": \"no. 38, p.10\", \"stance\": \"supports\",\n        \"note\": \"Horn cites for bāfdum exactly the same three verses (SF, FR/FJ Abū Šukūr and Asadī) and glosses 'āfdum ‚letzter‘ … phlv. afdūm, päz. awdum'.\"},\n       {\"src\": \"HUB\", \"where\": \"Persische Studien, note to Horn no. 38\", \"stance\": \"partial\",\n        \"note\": \"HUB.txt line 150: 'Man müsste lautgesetzlich afdum erwarten. „Vielleicht war das Wort schon zur Zeit der ältesten neupersischen Dichter (Abū Sukūr!) veraltet und wurde falsch ausgesprochen.“ Nöldeke.'\"},\n       {\"src\": \"MON\", \"where\": \"s.v. آفدم\", \"stance\": \"supports\", \"note\": \"'آفدم … (ص.) آخرین، پسین، نهائی' — same sense as the chart's 'last, at last'.\"}\n     ]},\n\n    {\"id\": 6, \"lang\": \"Avestan\",\n     \"words\": \"â 1; â-vare; â-gam; â-râd, â-râiti 1; apa-spar; â-kand\", \"verdict\": \"disputed\",\n     \"derivation\": (\"The words themselves are real: Av./OP ā is a preverb/preposition 'to, toward, hither' that combines \"\n                    \"with bar- (ā-bar- 'bring'), gam- (ā-gam- 'come'), rād-/rāta- (ā-rā- 'set in order'), kan- (ā-kan- 'fill up'). \"\n                    \"But its ancestry is not *apo-. Skt. ā́, Av./OP ā and Gk. ὦ go back to an independent particle (PIE *ē/*ō; \"\n                    \"Wiktionary reconstructs *h₂ed), and every specialist treatment keeps the two apart: Horn's very first \"\n                    \"entry lists NP ā- under 'ap. aw. phlv. ā; ai. ā́' with no reference to apa, Cheung files āfrīnāmi under \"\n                    \"'*fraiH (+ *ā-)', and Pokorny's own apo- entry (pp.53-55) contains no ā-. Nourai's Avestan box therefore \"\n                    \"hangs a different preverb on the *apo- root by way of the invented root variant 'Apâ'. The one genuinely \"\n                    \"apa- item in the box, apa-spar 'walk away from, entrust', is also mis-prefixed: the ancestor of MP \"\n                    \"abespurdan / NP sepārdan is *upa-spar- (Cheung) or *abi-spar- (MacKenzie's Manichaean ʾbyspwrd), not \"\n                    \"*apa-spar-. Hence: right words, wrong parent.\"),\n     \"sources\": [W + \"%D8%A2%D9%81%D8%B1%DB%8C%D9%86\"],\n     \"ref_check\": [\n       {\"ref\": \"KNT:168\", \"status\": \"partial\",\n        \"note\": (\"KNT.txt leaf 190 (= printed p.168) is the apa- page: 'apa- prefix (§206b) ‚away‘: Av. Skt. apa, Gk. ἀπό, \"\n                 \"Lt. ab, Gt. af … pIE *apo. Used with vb. gaud- and in sbb. apadāna-, apa-niyāka-; with suffix in apatara-, \"\n                 \"apara-'. It has apataram, apadāna-, apaniyāka-, apara-, āpi-, apiy, abiy — but no entry for the preverb ā, \"\n                 \"which is what this box is mainly about. Kent's ā appears elsewhere (e.g. s.v. yātā: 'Double prep., yātā ā').\")},\n       {\"ref\": \"BQT:1086\", \"status\": \"not_found\", \"note\": \"As at node #1: BQT vol. 2 p.≈1086 (leaf 543) is the سبز- run of headwords; no آ-prefix or apa material there.\"},\n       {\"ref\": \"FFD:24\", \"status\": \"partial\",\n        \"note\": (\"FFD_pages.txt pdf p.29 = printed p.24, s.v. آراستن: 'آراست < فارسی میانه ārāst < ایرانی باستان \"\n                 \"*ā-rād-ta. ā پیشوند فعلی است که در اصل بر انجام گرفتن کار به سوی متکلم دلالت می‌کرده است' — Abolghāsemi confirms ā- as a \"\n                 \"verbal prefix and confirms ā-rād, but derives it from Old Iranian *ā-, never from apa-.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"AiW cols. 71-84 (apa, apa- compounds, aipi)\", \"stance\": \"partial\",\n        \"note\": \"Bartholomae's apa- run (apa-gaēθa-, apa-gaya-, apa-ɣžāra-, apa-xšaθra-, apa-stūtay-, apəma-, apəm) contains none of Nourai's ā- compounds; ā- is a separate headword in AiW.\"},\n       {\"src\": \"CHEUNG\", \"where\": \"s.v. *spar 'to hand over, entrust', p.351\", \"stance\": \"contradicts\",\n        \"note\": \"'*spar … (+ *upa-) BMP ʾpspʾl- /abespar-/ ‚to hand over, entrust‘ … NWIR: NP sipār-/sipurdan … PIE *sper- ‚to deliver, secure‘ — LIV: 579 | Pok.: 992' — preverb *upa-, not *apa-.\"},\n       {\"src\": \"HRN\", \"where\": \"no. 1, p.1\", \"stance\": \"contradicts\",\n        \"note\": \"'1. ā. 1) Praefix, z. B. in āmeden, ārāyiš. ap. aw. phlv. ā; ai. ā́. 2) Praeposition, z. B. in her ā her, gird ā gird, aw. ai. ā.' Horn equates NP ā- with Skt. ā́ and says nothing of apa.\"},\n       {\"src\": \"PHD\", \"where\": \"MacKenzie p.3 s.v. abespurdan\", \"stance\": \"contradicts\",\n        \"note\": \"'abespurdan, abespār- [ʾfspwltnʹ, ʾpspʾl- | M ʾbyspwrd, ʾbyspr-, N sipurdan, sipār-] commit, entrust, consign' — the Manichaean ʾby- spelling points to *abi-/upa-, not apa-.\"}\n     ]},\n\n    {\"id\": 7, \"lang\": \"Persian\", \"words\": \"â-, a- «آ- ، ا-»; -â- «-ا-»\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"The edge itself is right: NP آ-/ا- is the direct continuation of the Old Iranian preverb ā, preserved \"\n                    \"fossilised in verbs whose Middle Persian ancestors already carried it — آوردن (< *ā-bar-), آمدن (< *ā-gam-), \"\n                    \"آراستن (< *ā-rād-ta-), آکندن (< *ā-kan-) — all four of which stand in Nourai's extras. The separate \"\n                    \"'-ā-' is the same particle in its adverbial/prepositional use, used to link a repeated noun: Horn's own \"\n                    \"examples her ā her and gird ā gird are precisely Nourai's برابر، دمادم، سراسر، گرداگرد type. \"\n                    \"The only defect is inherited from the parent box: the preverb goes back to PIE *ē/*ō (*h₂ed), not to \"\n                    \"*apo-; and اسپاردن in the extras belongs to *upa-spar-, not to ā-.\"),\n     \"sources\": [W + \"%D8%A2%D9%81%D8%B1%DB%8C%D9%86\"],\n     \"ref_check\": [\n       {\"ref\": \"BQT:1086\", \"status\": \"not_found\", \"note\": \"See node #1: BQT vol. 2 leaf 543 (≈ p.1086) is the سبز- section; nothing on the prefix آ-.\"},\n       {\"ref\": \"HRN:1\", \"status\": \"supports\",\n        \"note\": \"HRN.txt leaf 22 = printed p.1, entry no.1: 'ā. 1) Praefix, z. B. in āmeden, ārāyiš. ap. aw. phlv. ā; ai. ā́. 2) Praeposition, z. B. in her ā her, gird ā gird, aw. ai. ā.' Both of Nourai's two uses, verbatim.\"},\n       {\"ref\": \"FFD:24\", \"status\": \"supports\",\n        \"note\": \"FFD printed p.24: 'ā پیشوند فعلی است', with آراستن < MP ārāst < OIr *ā-rād-ta and آرای < MP ārāy < *ā-rād-a.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"HUB\", \"where\": \"Persische Studien (Horn's numbering, no.1)\", \"stance\": \"silent\",\n        \"note\": \"Hübschmann adds no note to Horn no.1; the entry stands unchallenged.\"},\n       {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. ā-verbs\", \"stance\": \"supports\",\n        \"note\": \"MacKenzie's ā- compounds (āwar-, āmad-, ārāy-, āgand-) are the Middle Persian stage between Nourai's Avestan and Persian boxes.\"},\n       {\"src\": \"CHEUNG\", \"where\": \"s.v. *bar, *gam, *kan (+ *ā-)\", \"stance\": \"supports\",\n        \"note\": \"Cheung consistently marks these NP verbs as root + preverb *ā-, e.g. '(+ *ā-) ‚to bring back, restore‘' under *bar.\"}\n     ]},\n\n    {\"id\": 8, \"lang\": \"Avestan\", \"words\": \"apa-dâna; â-frî-nami; â-fritan; â-part\", \"verdict\": \"disputed\",\n     \"derivation\": (\"Three separate problems. (a) apa-dāna- 'off place, secret room of a palace' is a genuine word with \"\n                    \"exactly Nourai's analysis — but it is Old Persian, not Avestan: Kent p.168 'apadāna- sb. ‚palace‘: from \"\n                    \"apa- + dāna- to root *dā-, cf. Skt. apadhā- ‚concealment‘, Gk. ἀποθήκη ‚storehouse‘', attested in \"\n                    \"Artaxerxes II's Susa and Hamadan inscriptions (D²Sa, A²Ha imam apadāna); Bartholomae's AiW apa- run has \"\n                    \"no such Avestan compound, and Nourai himself puts it (rightly) in the Old Persian box #12 as well. \"\n                    \"(b) ā-frīnāmi 'I praise/bless' is genuine Young Avestan (Y 11.15, Y 52.1, Yt 13.51 āfrīnənti) and ā-pərəta- \"\n                    \"'battle' is a real ā + parət- 'to fight' formation — but both contain the preverb ā-, from PIE *ē/*ō, \"\n                    \"not *apo-. (c) 'ā-fritan to create' is not Avestan at all: it is the Middle Persian infinitive āfrītan \"\n                    \"(BMP ʾplyn-/ʾplyt-), as Horn's no.39 explicitly labels it ('phlv. āfrītan ‚schaffen‘'). So the box mixes \"\n                    \"an Old Persian noun, two Avestan ā- formations and one Middle Persian verb, and none of the ā- items \"\n                    \"descends from the root of the chart.\"),\n     \"sources\": [W + \"%D8%A2%D9%81%D8%B1%DB%8C%D9%86\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:168\", \"status\": \"not_found\",\n        \"note\": (\"Klein 1966 p.168 (KLN_1966.txt leaf 96) runs 'behemoth … behen … behest … behind … behold … beige' — \"\n                 \"nothing on apadāna, āfrīn or āvard, and Klein has no headword 'apadana' anywhere. Almost certainly a \"\n                 \"typo for KNT:168 (Kent), which is the page that does carry apadāna- and is cited on the two neighbouring boxes.\")},\n       {\"ref\": \"POK:844\", \"status\": \"supports\",\n        \"note\": (\"POK_03.txt leaf 78 (= printed p.844): 'prāi-, prəi-, prī- (prī-) ‚gern haben, schonen, friedlich-frohe \"\n                 \"Gesinnung‘ … av. frāy- ‚befriedigen‘, z. B. frīnāmahi, Partiz. frīta-, frīna-, friθa- ‚wohl befriedigt; \"\n                 \"geliebt‘, frīti- f. ‚Gebet‘'. Supports the frī- half (Nourai's ☞ Prî) but has no ā- from apo-.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"KNT\", \"where\": \"Kent p.168 s.v. apadāna-\", \"stance\": \"partial\",\n        \"note\": \"'apadāna- sb. ‚palace‘: from apa- + dāna- (§147.I) to root *dā- … apadānam asm. D²Sa1; A²Hb' — confirms the word and Nourai's analysis, but as Old Persian.\"},\n       {\"src\": \"BRT\", \"where\": \"AiW cols. 71-84\", \"stance\": \"contradicts\",\n        \"note\": \"Bartholomae's Avestan apa- compounds are apa-gaēθa-, apa-gaya-, apa-ɣžāra-, apa-kava-, apa-xšaθra-, apa-skaraka-, apa-stanah-, apa-stūtay-, apa-zaδah- — there is no Avestan apa-dāna-.\"},\n       {\"src\": \"CHEUNG\", \"where\": \"s.v. *fraiH, p.87\", \"stance\": \"supports\",\n        \"note\": \"'*fraiH ‚to rejoice, ? to atone, [med.] please‘. AVESTAN: friī- ‚to rejoice, please‘ || (+ *ā-) ‚to bless‘ … IND. 1sg. YAv. āfrīnāmi (Y 11.15, Y 52.1 …) … PIE *preiH- … Pok.: 844' — the prefix is *ā-.\"},\n       {\"src\": \"HRN\", \"where\": \"no. 39, p.10 and no. 1025, p.230\", \"stance\": \"partial\",\n        \"note\": \"'39. āfrīden ‚schaffen‘ … aw. āfrīnāmi ‚ich preise‘ etc., āfrīna- ‚Segen‘; phlv. āfrītan ‚schaffen‘ … ai. ā + √prī-' (so ā-fritan is Pahlavi); '1025. neberd ‚Kampf‘ … aw. *ni + √parət- … Vergl. np. āwerd ‚Kampf‘'.\"}\n     ]},\n\n    {\"id\": 9, \"lang\": \"Persian\", \"words\": \"âpâdânâ «آپادانا»; âfarîn «آفرین»; âvard «آورد»\", \"verdict\": \"plausible\",\n     \"derivation\": (\"آفرین and آورد are inherited and confirmed. āfarīn 'praise, bravo' is the present stem of آفریدن < MP \"\n                    \"āfrīn-/āfrītan 'to bless, create' < Av. ā-frīnāmi, PIE *preiH-; the antonym نفرین nifrīn < MP nifrīn \"\n                    \"'curse' (*ni-frī-) and the agent آفریدگار in Nourai's extras belong to the same family. āvard 'combat' is \"\n                    \"the Shahnameh word (آوردگاه 'battlefield', آوردیدن), from ā- + parət- 'to fight', the exact counterpart \"\n                    \"of نبرد neberd < *ni-parət- (Horn no.1025); it must be kept apart from the homograph آورد 'he brought' \"\n                    \"(< ā-bar-). آپادانا is different in kind: it is not an inherited Persian word but a 20th-century learned \"\n                    \"re-borrowing of Old Persian apadāna from the Achaemenid inscriptions and archaeological literature \"\n                    \"(the Apadana of Persepolis/Susa); and its source is the Old Persian box #12, not an Avestan one. \"\n                    \"Hence 'plausible': two words confirmed, one with a mis-drawn parent and a learned rather than \"\n                    \"inherited transmission.\"),\n     \"sources\": [W + \"%D8%A2%D9%81%D8%B1%DB%8C%D9%86\"],\n     \"ref_check\": [\n       {\"ref\": \"KNT:168\", \"status\": \"partial\",\n        \"note\": (\"Kent p.168 (KNT.txt leaf 190) gives 'apadāna- sb. ‚palace‘: from apa- + dāna- … For development in later \"\n                 \"Iranian, with āpa- by secondary lengthening … see Henning, TPS 1944.110n' — which is the source of \"\n                 \"Nourai's spelling āpādānā and supports that word. Kent says nothing about āfarīn or āvard.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"HRN\", \"where\": \"no. 39 (p.10) and no. 1025 (p.230)\", \"stance\": \"supports\",\n        \"note\": \"'āfrīden ‚schaffen‘, Praes. āfrīn-em, āfrīnegār; āfrīn 1) ‚schaffend‘ 2) ‚Lob‘, vergl. nefrīn ‚Fluch‘'; and 'Vergl. np. āwerd ‚Kampf‘ (Šāhn. I, 218 Vers 1506), āwerdgāh (häufig), āwerīden.'\"},\n       {\"src\": \"CHEUNG\", \"where\": \"s.v. *fraiH, p.87\", \"stance\": \"supports\",\n        \"note\": \"'*NWIR: (+ *ā-) NP āfaridan/āfarīn- ‚to create‘ || (+ *ni-) NP nifrīn … ‚curse‘'.\"},\n       {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. āfrīn, āfrīdan\", \"stance\": \"supports\",\n        \"note\": \"MacKenzie's āfrīn 'blessing, praise' and āfrīdan 'to create, bless' are the Middle Persian link the chart omits.\"},\n       {\"src\": \"MON\", \"where\": \"Moʿin s.v. آفرین\", \"stance\": \"supports\",\n        \"note\": \"Moʿin gives آفرین 'ستایش، مدح؛ تحسین' with the Pahlavi tag, matching the chart's 'praise'.\"}\n     ]},\n\n    {\"id\": 10, \"lang\": \"Arabic\", \"words\": \"ifrît\", \"verdict\": \"plausible\",\n     \"derivation\": (\"Arabic عِفْريت ʿifrīt (vulgar ʿafrīt), a powerful demon; Qurʾanic (Q 27:39 ʿifrītun min al-jinn), whence \"\n                    \"English afreet. Asbaghi and Wiktionary both make it a Middle Iranian loan: from the past participle \"\n                    \"āfrīd 'created' (MP āfrītan/āfrīd-, the very verb of Nourai's parent box), originally elliptical for \"\n                    \"*dēw āfrīd 'a demon's creature' — which is exactly the chart's gloss 'demon creature'. The vocalisation \"\n                    \"ʿifrīt with initial ʿayn and the fiʿlīt shape are the usual Arabic adaptation of a foreign form to a \"\n                    \"native pattern. It is only 'plausible' because a purely internal Arabic derivation is also current: \"\n                    \"from the root ع-ف-ر 'dust, ashes' (cf. ʿafara 'to roll in the dust'), formed like عَكْرُوت ʿakrūt \"\n                    \"'scoundrel'; Klein s.v. 'afreet' gives no Iranian source at all, and Jeffery's Foreign Vocabulary of \"\n                    \"the Qurʾān does not treat the word, i.e. he did not regard it as a loan.\"),\n     \"sources\": [W + \"%D8%B9%D9%81%D8%B1%D9%8A%D8%AA\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD:23\", \"status\": \"not_checked\",\n        \"note\": (\"Nourai's AHD page numbers below 1500 refer to the main body of the 1975/76 American Heritage Dictionary \"\n                 \"(p.23 would be the 'afreet' page), which is not open online; the local AHD file is only Watkins's \"\n                 \"Indo-European roots appendix, and 'afreet' is not an IE-root entry there.\")},\n       {\"ref\": \"PLA:203\", \"status\": \"supports\",\n        \"note\": (\"PLA_pages.txt leaf 218 = printed p.203 (leaf − 15), running head 'Saraba … 203': 'عفريت - ʿifrīt: „Dämon“ \"\n                 \"pers. آفرید āfarīd v. āfarīdan „schaffen“ mp. ʾplytnʹ āfrītan … ā-frāy', with 'عفاریت - ʿafārīt: Pl. v. ʿifrīt' and \"\n                 \"'عفرین - ʿifrīn: „mächtig“ s. ʿifrīt u. pers. aus āfarīdan'. Asbaghi says exactly what Nourai's arrow says, \"\n                 \"and even supplies the Avestan ā-frāy- that Nourai's parent box has.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"Klein 1966 p.≈ s.v. afreet\", \"stance\": \"partial\",\n        \"note\": \"'afreet, n., an evil demon or jinni. — Transliteration of Arab. ʿifrīt (in vulgar pronunciation ʿafrīt); name of an evil demon or monstrous giant in Mohammedan mythology.' Klein records the Arabic but offers no Persian etymology.\"},\n       {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān\", \"stance\": \"silent\",\n        \"note\": \"grep of FVQ.txt / FVQ_pages.txt for 'ifrit', 'ʿifrīt', 'عفريت' returns nothing: Jeffery has no entry, i.e. he did not class the Qurʾanic ʿifrīt (Q 27:39) as a foreign word.\"},\n       {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāز al-Fārisiyya al-Muʿarraba\", \"stance\": \"silent\",\n        \"note\": \"grep of AFM.txt / AFM_pages.txt for عفريت returns nothing — Addi Shir does not list it among the Persian loans in Arabic.\"},\n       {\"src\": \"LKT\", \"where\": \"Lokotsch\", \"stance\": \"silent\",\n        \"note\": \"grep of LKT.txt for 'ifrit' returns nothing; Lokotsch has no entry for the word.\"}\n     ]},\n\n    {\"id\": 11, \"lang\": \"Persian\", \"words\": \"efrît «عفریت»\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Modern Persian عفریت ʿefrīt 'demon, fiend' (with the feminine عفریته ʿefrīte in the extras) is a \"\n                    \"straightforward Arabic loan back into Persian, taken over with its Arabic عاین spelling and its \"\n                    \"Arabic feminine in -a; Moʿin tags it '[ع.]' (Arabic). If Asbaghi and Wiktionary are right about node \"\n                    \"#10, this is a round trip: MP āfrīd → Arabic ʿifrīt → NP ʿefrīt, and the modern Persian word is thus \"\n                    \"unrelated in form to its own ancestor آفریدن, which is presumably why Nourai draws it as a separate \"\n                    \"Arabic-mediated branch. The borrowing is medieval and spread through Qurʾanic and 1001-Nights usage.\"),\n     \"sources\": [W + \"%D8%B9%D9%81%D8%B1%D9%8A%D8%AA\"],\n     \"ref_check\": [\n       {\"ref\": \"MON\", \"status\": \"supports\",\n        \"note\": \"MON_part1.txt line 96994: 'عفریت: … [ع.] (ا.) دیو، اهریمن، غول' — Moʿin marks it explicitly as an Arabic loanword meaning 'demon, Ahriman, ghoul', exactly the chart's gloss. (No page cited by Nourai; the 2-vol OCR has no page markers.)\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"PLA\", \"where\": \"Asbaghi p.203\", \"stance\": \"supports\",\n        \"note\": \"Asbaghi's whole entry is about the Persian→Arabic direction, which presupposes the Arabic form that Persian then re-borrowed.\"},\n       {\"src\": \"KLN\", \"where\": \"s.v. afreet\", \"stance\": \"supports\",\n        \"note\": \"Klein confirms the Arabic form and its 'evil demon or jinni' sense, the sense in which Persian has it.\"},\n       {\"src\": \"MON\", \"where\": \"s.v. عفریت\", \"stance\": \"supports\", \"note\": \"'[ع.]' origin tag = عربی, Arabic.\"}\n     ]},\n\n    {\"id\": 12, \"lang\": \"Old Persian\", \"words\": \"ap 2, apa; apa-dâna; pa 2, pô\", \"verdict\": \"plausible\",\n     \"derivation\": (\"OP apa- and apadāna- are exactly right. Kent p.168: 'apa- prefix ‚away‘: Av. Skt. apa, Gk. ἀπό, Lt. ab, \"\n                    \"Gt. af, Gm. ab, NEng. of, off, pIE *apo. Used with vb. gaud- and in sbb. apadāna-, apa-niyāka-; with \"\n                    \"suffix in apatara-, apara-'; and 'apadāna- ‚palace‘: from apa- + dāna- to root *dā-, cf. Skt. apadhā- \"\n                    \"‚concealment‘, Gk. ἀποθήκη ‚storehouse‘' — which is precisely Nourai's gloss 'off (secret) place' and \"\n                    \"his cross-reference to root Dhē 2 (*dheh₁-). Attested in A²Sa/A²Ha/D²Sa (imam apadāna(m)). The third \"\n                    \"item is the weak one: there is no Old Persian preposition pa or pō. Pokorny's 'po:' section (p.54) \"\n                    \"illustrates it from Avestan pa-zdayeiti, Latin pō-situs/pōnō, Albanian pa, Old High German fona and \"\n                    \"Slavic/Baltic po — not from Old Persian, and Kent's lexicon has no such entry.\"),\n     \"sources\": [],\n     \"ref_check\": [\n       {\"ref\": \"POK:53-55\", \"status\": \"partial\",\n        \"note\": (\"POK_01.txt leaves 61-63 = pp.53-55 cover apo / po / ap-u / pu, including 'av. ap. apa ‚von-weg‘'. But the \"\n                 \"'po:' paragraph on p.54 lists 'av. pa-zdayeiti ‚lässt wegrücken‘; lat. po-situs, pōnō … alb. pa … afries. \"\n                 \"fān … aksl. po' — no Old Persian pa/pō, so that word of the box is not supported by the cited pages.\")},\n       {\"ref\": \"KNT:168\", \"status\": \"supports\",\n        \"note\": \"KNT.txt leaf 190 (printed p.168) carries 'apa- prefix (§206b) ‚away‘ … pIE *apo' and 'apadāna- sb. ‚palace‘: from apa- + dāna-', i.e. two of the box's three words verbatim.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"AiW col. 74 (p. apataram) and cols. 71-72 (apa)\", \"stance\": \"supports\",\n        \"note\": \"Bartholomae marks the Old Persian forms with 'p.' in the same apa- article, e.g. 'p. apataram Adv. 1) ‚abseits, anderswo‘ … 2) mit hacā ‚ausser‘'.\"},\n       {\"src\": \"IEC\", \"where\": \"Mann s.v. apo\", \"stance\": \"supports\",\n        \"note\": \"'apo (apo, apo, po) ‚away; from, after‘ … OCS po … Li. po' — Mann too attaches po to Slavic/Baltic, not to Old Persian.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins s.v. apo-\", \"stance\": \"partial\",\n        \"note\": \"'7. Possible root *po(s), on, in: a. Russian po … b. Latin post … c. Latin pōnere' — Watkins likewise gives the po- variant no Iranian, let alone Old Persian, reflex.\"}\n     ]},\n\n    {\"id\": 13, \"lang\": \"Old Persian\", \"words\": \"apa-had; apa-ra; apa-taram; pan-s-dau; apa-nyâka\", \"verdict\": \"disputed\",\n     \"derivation\": (\"Three of the five are solid Old Persian: apara- 'later, after' (Kent p.168, apa- + comparative -ra-, \"\n                    \"asn. adverb aparam DB 4.37 etc.), apataram 'farther off, elsewhere' (nsn. of apatara- = apa- + -tara-, \"\n                    \"DNa 18, DSe 16f, XPb 25, XPh 16, cf. Gk. ἀπωτέρω), and apaniyāka- 'great-great-grandfather' (apa- + \"\n                    \"niyāka- 'grandfather', cf. Lat. abavus; A²Sa 3), where Nourai's gloss 'ancestors' is loose but the \"\n                    \"formation is Kent's. The other two fail. 'apa-had ‚put away‘' is unattested: Old Persian uses apa- with \"\n                    \"gaud- (apagaudaya- 'conceal', DB 4.54-57), and the root *had- 'sit' appears only in ni-šad-/niyašādayam \"\n                    \"(Kent, Cheung s.v. *had) — neither Kent nor Bartholomae nor Cheung has an *apa-had-. 'pan-s-dau ‚after \"\n                    \"that‘' is not Old Persian at all but OLD PRUSSIAN: it comes straight out of the page Nourai cites, \"\n                    \"Pokorny p.54, 'Eine ähnliche Form sucht Trautmann Apr. 389 in apr. pan-s-dau ‚danach‘' — where apr. = \"\n                    \"altpreußisch. Nourai evidently read the abbreviation as 'Old Persian'. The book page (pdf 59) does print \"\n                    \"it inside the Old Persian box, so this is the author's error, not a scan artefact.\"),\n     \"sources\": [],\n     \"ref_check\": [\n       {\"ref\": \"POK:53,55\", \"status\": \"contradicts\",\n        \"note\": (\"POK_01.txt leaf 62 (= p.54, within the cited range): 'Eine ähnliche Form sucht Trautmann Apr. 389 in apr. \"\n                 \"pan-s-dau ‚danach‘' — apr. = Old Prussian, in the Baltic part of the 'po' paragraph. Pokorny does support \"\n                 \"ap. apataram ('ap. apataram Adv. ‚abseits, anderswo‘', p.54) and av./ap. apara-, but he flatly contradicts \"\n                 \"the Old Persian label on pan-s-dau, and has no apa-had.\")},\n       {\"ref\": \"KNT:168\", \"status\": \"partial\",\n        \"note\": (\"Kent p.168 (leaf 190) has 'apataram adv. ‚farther off, far off‘ … DNa 18; DSe 16f; XPb 25; XPh 16', \"\n                 \"'apara- adj. ‚later, after‘ … aparam asn. as adv. DB 4.37 …', 'apaniyāka- sb. ‚great-great-grandfather‘: \"\n                 \"from apa- + niyāka- ‚grandfather‘, cf. Lt. ab-avos … A²Sa 3' — three of five. It has neither apa-had nor \"\n                 \"pan-s-dau; for *had- it offers only 'pIE *sed- ‚sit‘, OP had-iš ‚seat, abode‘' and the causative ni-šādaya-.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"KNT\", \"where\": \"Kent p.168 and §224, §281\", \"stance\": \"partial\",\n        \"note\": \"For the apa- verb Kent gives only apa-gaud-: 'inj. 2sg. … apa-gaudaya (DB 4.54)', 'mā … apagaudaya' — the Old Persian apa- verb is 'conceal', not 'put away'.\"},\n       {\"src\": \"CHEUNG\", \"where\": \"s.v. *had 'to sit, be seated', p.125\", \"stance\": \"contradicts\",\n        \"note\": \"Cheung lists the preverbs attested with *had as *abi- and *ni- only ('OLD PERSIAN: (+ *ni-) ni-sad- (caus.) ‚to establish‘ … niyašādayam'); no *apa-had- anywhere in Iranian.\"},\n       {\"src\": \"IEC\", \"where\": \"Mann s.v. apo-teros\", \"stance\": \"supports\",\n        \"note\": \"'apo-teros ‚further, following‘. WP I, 47 … Skt. OPer. apataram; Gk. apóteros; Go. aftaro' — independent confirmation of the Old Persian apataram.\"},\n       {\"src\": \"BRT\", \"where\": \"AiW col. 74\", \"stance\": \"supports\",\n        \"note\": \"'p. apataram Adv. 1) ‚abseits, anderswo‘: tyāmaiy apataram kartam H 2.3; 2) mit hacā ‚ausser‘: apataram hacā Pārsā ‚ausser Persien‘ D 6.3.'\"}\n     ]},\n\n    {\"id\": 14, \"lang\": \"Old Persian\", \"words\": \"apa-ardha\", \"verdict\": \"plausible\",\n     \"derivation\": (\"The compound is real but is a reconstruction, and 'Old Iranian' rather than specifically Old Persian \"\n                    \"is the right label: Nyberg sets up MP apārōn < OIr *apārda-van-, formed with the suffix -van- from \"\n                    \"*apārda- < *apa-arda- 'whose side is turned away' (apa- 'away' + arda- 'side, half', the same *ardha- \"\n                    \"as in Skt. árdha- 'half, side'). The mirror-image compound *frārda-van- > MP frārōn 'righteous, upright' \"\n                    \"(< *fra-arda- 'whose side is turned forward') guarantees the analysis. No such word is attested in the \"\n                    \"Achaemenid inscriptions, so Kent has nothing; Kent's OP arda- is a different word, 'light' (ardata- \"\n                    \"'silver', ardastāna-).\"),\n     \"sources\": [],\n     \"ref_check\": [\n       {\"ref\": \"POK:53-55\", \"status\": \"partial\",\n        \"note\": (\"Pokorny pp.53-55 give the apo- root and its derivatives apo-tero-, ap-ero-, ap-io-, ap-ōko-, but there is \"\n                 \"no apa-ardha compound on those pages; the compound has to be got from Nyberg (node #15) or from \"\n                 \"Pokorny's separate *ardh- article.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p.≈24 s.v. apārōn\", \"stance\": \"supports\",\n        \"note\": \"'< OIr apārda-van-, derived, by means of the suff. -van-, from *apārda- < *apa-arda- ‚whose side is turned away‘ (HP II, 15)' — verbatim Nourai's apa-ardha.\"},\n       {\"src\": \"KNT\", \"where\": \"Kent lexicon s.v. arda-, ardata-, ardastāna-\", \"stance\": \"silent\",\n        \"note\": \"'ardastāna- sb. ‚window-frame‘: arda- ‚light‘ as in OP ardata- ‚silver‘' — Kent's OP arda- is 'light', and he has no apa-arda- compound at all.\"},\n       {\"src\": \"BRT\", \"where\": \"AiW apa- article, cols. 71-84\", \"stance\": \"silent\",\n        \"note\": \"No Avestan apa-arəδa- among Bartholomae's apa- compounds; the form is a Middle-Iranian-based reconstruction.\"}\n     ]},\n\n    {\"id\": 15, \"lang\": \"Pahlavi\", \"words\": \"apârôn\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Middle Persian abārōn (Book Pahlavi ʾpʾlʹlwnʹ/ʾpʾlwnʹ) 'contrary, wrong, perverse, sinful', adverbially \"\n                    \"'backward' (= abāz), Pāzand āwārūn, is the regular outcome of *apārda-van-: the cluster *-rd- gives \"\n                    \"Middle Persian -r-/-l- in the Book Pahlavi orthography, and the suffix *-āna-/-ōn is the same as in its \"\n                    \"antonym frārōn 'righteous'. The word is a technical term of Zoroastrian moral vocabulary, abārōnīh \"\n                    \"meaning 'sin' and being the standing opposite of frārōnīh.\"),\n     \"sources\": [],\n     \"ref_check\": [\n       {\"ref\": \"NYB:23\", \"status\": \"supports\",\n        \"note\": (\"NYB_vol2_glossary.txt line 521, form-feed leaf 32 ≈ printed p.24 (Part II offset leaf = printed + 8, so \"\n                 \"within a page of Nourai's 23): 'apārōn [ʾpʾlwnʹ; Ps. ʾpʾlwny] 1. adj. wrong 66⁴⁻¹¹, 69¹, etc., opp. frārōn. \"\n                 \"— 2. adv. backward (= apāc). — Paz. āwārūn … NP vārūn ‚inverted, turned upside down‘; < OIr apārda-van- \"\n                 \"… < *apa-arda-'. Both of Nourai's glosses ('wrong, upside down') and the whole three-box chain are here.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"MacKenzie p.2 s.v. abaron\", \"stance\": \"supports\",\n        \"note\": \"PHD_mackenzie.txt: 'abaron [ʾpʾlwnʹ | N warun] contrary, wrong, sinful. ~ih: sin.' MacKenzie gives the New Persian outcome directly.\"},\n       {\"src\": \"NYB\", \"where\": \"s.v. frārōn\", \"stance\": \"supports\",\n        \"note\": \"'frārōn [plʾlwnʹ] righteous, upright, honest … OIr *frārda-van- < *fra-arda-, cf apārōn' — the parallel that secures the analysis.\"}\n     ]},\n\n    {\"id\": 16, \"lang\": \"Persian\", \"words\": \"vârŭn «وارون»\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"NP وارون vārūn 'upside down, inverted, perverse' (with the extended وارونه vārūne of the extras) is \"\n                    \"inherited directly from MP abārōn: initial ab-/aw- regularly yields NP wā-/vā- (cf. MP abāz > NP باز/واز), \"\n                    \"so *abārōn > wārūn. Classical Persian keeps the moral sense of the Pahlavi word ('wicked, ill-omened, \"\n                    \"بخت وارون ‚ill fortune‘'), while modern Persian has generalised the physical sense 'inverted'. The word \"\n                    \"was borrowed onward into Ottoman Turkish as varun.\"),\n     \"sources\": [W + \"%D9%88%D8%A7%D8%B1%D9%88%D9%86\"],\n     \"ref_check\": [\n       {\"ref\": \"MON:4941\", \"status\": \"supports\",\n        \"note\": (\"Moʿin s.v. وارون, MON_part2.txt line 83342: 'وارون: [= وارونه] (ص.) باژگونه، واژگون، سرنگون، نگونسار، \"\n                 \"معکوس … برعکس؛ مخالف. (مج.) نامبارک، نحس، شوم. بخت وارون: بخت بد' — exactly the chart's 'upside down', \"\n                 \"plus the classical figurative sense. Page number not verifiable in the 2-vol OCR (no page markers).\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"MacKenzie p.2 s.v. abaron\", \"stance\": \"supports\",\n        \"note\": \"'abaron [ʾpʾlwnʹ | N warun] contrary, wrong, sinful' — MacKenzie's own bracket gives NP warun as the descendant.\"},\n       {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p.≈24\", \"stance\": \"supports\",\n        \"note\": \"'… NP vārūn ‚inverted, turned upside down‘' in the apārōn entry; also the index entry 'vārun: apāron'.\"},\n       {\"src\": \"MON\", \"where\": \"s.v. وارون / وارونه\", \"stance\": \"supports\",\n        \"note\": \"Moʿin also has the doublet 'وارون … [= وارون] (ص.) بازگونه، واژگون، سرنگون'.\"}\n     ]},\n\n    {\"id\": 17, \"lang\": \"Latin\", \"words\": \"ab\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Latin ab 'from, away from' (governing the ablative) is the direct Italic reflex of PIE *apo: \"\n                    \"intervocalic/pre-voiced *-p- was voiced to -b-, the older *ap surviving in aperiō < *ap-weriō and in \"\n                    \"the by-forms abs (before c, t: abstineō, abscondō), as- (before p: asportō), and ā- (before m, u, b: \"\n                    \"āmoveō, āvellō, ābitō). Cognate with Gk. ἀπό, Skt. ápa, Goth. af, OE of/off. Nourai's gloss 'away' and \"\n                    \"the language label are correct.\"),\n     \"sources\": [\"https://www.etymonline.com/word/ab-\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": (\"AHD_watkins1985.txt s.v. apo-: 'apo-. Also ap-. Off, away. 1. Germanic *af … 2. Latin ab, ab-, away from: \"\n                 \"AB-¹. 3. Greek apo, away from, from: APO- … [Pok. apo- 53.]' — the very entry Nourai cites as AHD.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"IEW p.53\", \"stance\": \"supports\",\n        \"note\": \"'lat. ab m. Abl. ‚von‘ (vor tönenden Kons. aus ap, das noch in aperiō aus *ap-weriō …); abs = gr. ἄψ ‚zurück; wieder‘; daraus as- vor p-, as-portō; ā vor tönenden Konsonanten.'\"},\n       {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. ab, abs, ā\", \"stance\": \"supports\",\n        \"note\": \"'ab, abs, a: preverbe et preposition … Ab signifie „en s’éloignant, en partant de, depuis, de”, et marque le point de départ … ce qui explique qu’il accompagne l’ablatif.'\"},\n       {\"src\": \"IEC\", \"where\": \"Mann s.v. apo\", \"stance\": \"supports\",\n        \"note\": \"'apo … Lat. ab (perhaps also as a fused px. in Lat. p-arco, p-aveo, paro, pudeo, pando, etc.)'.\"}\n     ]},\n\n    {\"id\": 18, \"lang\": \"English\", \"words\": \"abnormal\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"English abnormal (17th c.) is a Latinate formation whose first element is the Latin preposition/prefix \"\n                    \"ab- of node #17: Klein describes it as a blend of Latin abnormis 'deviating from a rule' (ab + norma \"\n                    \"'carpenter's square, rule') with Medieval Latin anormalis, itself a blend of Latin anomalus (< Gk. \"\n                    \"ἀνώμαλος) and normalis — which is why the earlier English form was anormal and why the -b- was \"\n                    \"restored on the model of Latin ab-. Only the prefix comes from *apo-; the stem is from PIE *ǵneh₃- \"\n                    \"'to know' via Latin norma (Watkins indexes ABNORMAL under gnō-, and ABLAUT, AFTER, EBB, OF, OFF, \"\n                    \"AWKWARD under apo-). The empty ref field is correct — Nourai cites nothing for this box.\"),\n     \"sources\": [\"https://www.etymonline.com/word/ab-\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart gives no reference for this box; nothing to check.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"Klein s.v. abnormal\", \"stance\": \"supports\",\n        \"note\": \"KLN_1971.txt: 'abnormal, adj. — A blend of L. abnormis and ML. anormalis, this latter itself being a blend of L. anomalus and normalis. See anomalous and norm and cp. anormal.'\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins, index and s.v. apo-\", \"stance\": \"partial\",\n        \"note\": \"The index has 'AB-¹ apo-' and 'ABNORMAL gnē-': the prefix is from apo-, the stem from the 'know' root, so Nourai's arrow holds only for ab-.\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat, s.v. OF\", \"stance\": \"silent\",\n        \"note\": \"Skeat has no abnormal entry; his relevant material is s.v. OF, where English of/off is put with Latin ab and Greek apo.\"}\n     ]}\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-59.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/out/build.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-59.json > /dev/null && echo \"JSON OK\"",
 "description": "Write page-59.json"
}
```


### [2026-09-04T23:02:42.804Z] TOOL RESULT

```
ok
JSON OK
```


## [2026-09-04T23:02:48.693Z] TOOL CALL #86: Bash

```json
{
 "command": "python3 tools/verify_check.py 59",
 "description": "Run verify_check"
}
```


### [2026-09-04T23:02:50.879Z] TOOL RESULT

```
nodes verified: 18/18
node verdicts: {'confirmed': 10, 'disputed': 4, 'plausible': 4}
root verdicts: {'plausible': 1}
ref checks: {'supports': 14, 'not_found': 4, 'not_checked': 4, 'partial': 6, 'contradicts': 1}
books consulted: {'supports': 39, 'partial': 10, 'contradicts': 5, 'silent': 7} | by book: {'PHD': 8, 'HRN': 7, 'BRT': 6, 'NYB': 5, 'MON': 5, 'CHEUNG': 5, 'IEC': 4, 'HUB': 3, 'KNT': 3, 'KLN': 3, 'AHD': 2, 'SNS': 1, 'WLD': 1, 'BQT': 1, 'FVQ': 1, 'AFM': 1, 'LKT': 1, 'PLA': 1, 'POK': 1, 'LAT': 1, 'SKT': 1}
```


## [2026-09-04T23:02:54.776Z] TOOL CALL #87: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | tail -20",
 "description": "Verify archived sources"
}
```


### [2026-09-04T23:02:59.564Z] TOOL RESULT

```
473 cited URLs, 21 not yet archived
archived 21, failed 0
```


## [2026-09-04T23:03:20.524Z] AGENT

Wrote `/home/sfmqrb/git/rishe/data/verification/page-59.json`; `verify_check.py 59` reports 18/18 nodes, no PROBLEM lines.

**Page 59 (book p.29), entry 0 — root "Apo, Apâ, Apu, Pu 3, Pô 1" [IE] "off"**
- Root verdict: **plausible**. Node verdicts: **10 confirmed, 4 plausible, 4 disputed**.
- Ref checks: 14 supports, 6 partial, 4 not_found, 4 not_checked, 1 contradicts. 21 books consulted (POK, WLD, AHD/Watkins, IEC, BRT, KNT, PHD, NYB, HRN, HUB, CHEUNG, SNS, FRS, FFD, BQT, MON, PLA, FVQ, AFM, LKT, KLN, LAT, SKT); 8 web pages archived via `fetch_source.py`.

Disputed / problem items:
- **Root box** – "Apâ" (long ā) is not in Pokorny 53–55, WP I 47ff., Watkins or Mann. It is the peg for the whole ā- branch; OIr ā "to, toward" is an independent particle (PIE *ē/*ō / *h₂ed), not an ablaut grade of *apo-.
- **#3 Persian bî-dastar** "beaver = 'without sickles'" – Moʿin's/Borhān's folk etymology (Moʿin: بی + دستر «داس کوچک، اره»). Variants ویدستر / بادستر rule out the privative bī-; Wiktionary takes the first element as *widʰu- "wood". (bī itself is confirmed.)
- **#6 Avestan â 1 etc.** – ā- preverb misattributed to *apo-; and apa-spar belongs to *upa-spar- (Cheung p.351) / *abi-spar- (MacKenzie ʾbyspwrd), not *apa-spar-.
- **#8 Avestan box** – mixes an Old Persian noun (apadāna-, Kent 168; no Avestan apa-dāna- in Bartholomae), two genuine Avestan ā- forms, and a Middle Persian verb (ā-frītan is Phlv., per Horn no.39).
- **#13 Old Persian "pan-s-dau: after that"** – this is **Old Prussian**, taken from the very page cited: Pokorny p.54 "apr. pan-s-dau ‚danach‘" (apr. = altpreußisch). Also "apa-had" is unattested in OP (Kent has apa-gaud-; *had- only in ni-šad-).

Citation slips found: **KLN:168** (node #8) is Klein's "behemoth–beige" page — almost certainly a typo for KNT:168; **BQT:1086** (nodes #1, #6, #7) falls in the س section of Borhān vol. 2 and has nothing on apa/ā.

Strongest confirmations: SNS p.26 gives "abdum/āfdum … *apatəma, apama"; Nyberg p.23/24 gives apārōn < OIr *apārda-van- < *apa-arda- with "NP vārūn" — Nourai's #14→#15→#16 chain verbatim; Asbaghi PLA p.203 supports Arabic ʿifrīt < Pers. āfarīd; Horn p.1 and FFD p.24 support the Persian ā- prefix node.
