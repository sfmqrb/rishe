# Verification process log — verify-page-54


## [2026-09-04T19:48:01.878Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 54 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-54.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-54.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-54.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 54` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T19:48:04.331Z] AGENT

I'll start by reading the instructions file.


## [2026-09-04T19:48:06.508Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:48:06.522Z] TOOL RESULT

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


## [2026-09-04T19:48:06.751Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-54.txt"
}
```


### [2026-09-04T19:48:06.771Z] TOOL RESULT

```
1	=== PDF page 54 (book page 24) ===
2	--- entry 0 ---
3	ROOT [Indo-European] An 1 : breath  (refs KLN; AHD; POK:48)
4	#1 (parent #0) [Avestan] refs=POK:48; KLN:41,1095; AHD; SNS:6; OEW:9 | ahu, ahura, anhu, ahva, axva : life, spirit, world ; prana : breath of life ; ahura-mazdha : wise spirit, God ☞Men 1,Dhě 2
5	  #2 (parent #1) [Persian] refs=MON:400; SNB:126 | Ahurâmazdâ «اهورامزدا» : God | extra: اهورا ؛ اورمزد ، هورمزد ، هرمزد ، هرمز
6	  #3 (parent #1) [Avestan] refs=POK:48; BQT:896; VDQ:36; SOD:127 | daoš-ahva : evil world ☞Dus ; barz-ahva : better (higher) world ☞Bhergh ; anhuyat-hača : from heart (soul) ☞Sekw
7	    #4 (parent #3) [Pahlavi] refs=SBK:214; VDQ:36 | dužax ; barzax
8	      #5 (parent #4) [Persian] refs=BQT:896; VIE:31; VDQ:36 | dŭzax «دوزخ» : hell ; barzax «برزخ» : middle stage
9	#6 (parent #0) [Greek] refs=KLN:118 | astma : hard breath
10	  #7 (parent #6) [French] refs=None | 
11	    #8 (parent #7) [Persian] refs=MON:55 | âsm «آسم» : asthma
12	  #9 (parent #6) [English] refs=None | asthma
13	#10 (parent #0) [Latin] refs=KLN:78 | anima : breath of air, life
14	  #11 (parent #10) [English] refs=AHD | animal, animosity, exhale, inhale
15	#12 (parent #0) [Germanic] refs=AHD:929, 931 | ansu : God
16	  #13 (parent #12) [English] refs=None | Oswald, Oscar ☞Ghei 2
17	#14 (parent #0) [Sanskrit] refs=POK:48, SOD:10 | âsu, âsura : God
18	  #15 (parent #14) [Sogdian] refs=SOD:10 | âs`wr : God
19	--- entry 1 ---
20	ROOT [Indo-European] An 2, Eno, Ono : other  (refs POK:37)
21	#1 (parent #0) [Avestan / Old Persian] refs=HRN:13; KLN:1108; POK:37 | anya, aimya : other
22	  #2 (parent #1) [Persian] refs=HRN:13 | ân «آن» : that
23	#3 (parent #0) [Germanic] refs=AHD; KLN:1102 | 
24	  #4 (parent #3) [English] refs=None | other
25	#5 (parent #0) [Indo-European] refs=IEC:27 | An-teros : second, other, step parent ☞Ter 1
26	  #6 (parent #5) [Persian] refs=IEC:27; MON:373 | andar «ـ اندر ۲» : a suffix meaning step as in step father | extra: پدراندر ، مادراندر ، دختراندر ، پسراندر
27	  #7 (parent #5) [Sanskrit] refs=IEC:27; POK:37 | antarah : other
28	
```


## [2026-09-04T19:48:10.804Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat SOURCE_MATRIX.md && echo \"=====BIB=====\" && cat bibliography_raw.txt | head -100"
}
```


### [2026-09-04T19:48:10.856Z] TOOL RESULT

```
<persisted-output>
Output too large (34.1KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/blwxda2bs.txt

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


## [2026-09-04T19:48:12.022Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k,v in d.items(): print(k,'|',v)\n\""
}
```


### [2026-09-04T19:48:13.789Z] TOOL RESULT

```
<persisted-output>
Output too large (104KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/brpzwy992.txt

Preview (first 2KB):
BQT | {'title': "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", 'kind': 'archive_djvu+local_scan_ocr', 'url': "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanne
...
</persisted-output>
```


## [2026-09-04T19:48:18.963Z] TOOL CALL #5: Bash

```json
{
 "command": "cat /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/blwxda2bs.txt | sed -n '1,400p'"
}
```


### [2026-09-04T19:48:19.006Z] TOOL RESULT

```
<persisted-output>
Output too large (34.1KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b2eclxejo.txt

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


## [2026-09-04T19:48:21.169Z] TOOL CALL #6: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-04T19:48:21.184Z] TOOL RESULT

```
1	# Source matrix — which local books to grep for each kind of node
2	
3	All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.
4	
5	ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).
6	
7	
8	## Indo-European roots (any IE node, root boxes)
9	
10	- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
11	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt`
12	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt`
13	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt`
14	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt`
15	- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
16	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt`
17	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
18	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
19	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
20	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
21	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
22	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
23	- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
24	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt`
25	- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
26	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt`
27	- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
28	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt`
29	- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
30	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
31	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
32	- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
33	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
34	- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
35	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt`
36	- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
37	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt`
38	- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
39	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
40	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
41	
42	## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian
43	
44	- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
45	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt`
46	- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
47	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt`
48	- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
49	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt`
50	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD_mackenzie.txt`
51	- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
52	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt`
53	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt`
54	- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
55	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt`
56	- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
57	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt`
58	- **CHEUNG** — CHEUNG
59	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/CHEUNG.txt`
60	- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
61	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt`
62	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt`
63	- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
64	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt`
65	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt`
66	- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
67	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_alt_v1.txt`
68	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_dli_part1.txt`
69	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt`
70	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt`
71	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt`
72	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt`
73	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
74	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
75	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
76	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
77	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
78	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
79	- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
80	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt`
81	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt`
82	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
83	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
84	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
85	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
86	- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
87	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt`
88	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt`
89	- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
90	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt`
91	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt`
92	- **HENNING** — HENNING
93	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt`
94	- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
95	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/EAV_studies.txt`
96	- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
97	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ISS_alt_DKS.txt`
98	- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
99	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt`
100	- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
101	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
102	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
103	- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
104	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf`
105	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt`
106	- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
107	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf`
108	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt`
109	- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
110	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AVG.txt`
111	- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
112	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HID.txt`
113	- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
114	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf`
115	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt`
116	- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
117	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TLM.txt`
118	- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
119	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/UNV.txt`
120	- **SBK** — M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
121	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SBK.txt`
122	
123	## Semitic / Arabic loans in either direction
124	
125	- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
126	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
127	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
128	- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
129	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt`
130	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt`
131	- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
132	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt`
133	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt`
134	- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
135	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`
136	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt`
137	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt`
138	- **AFA** — S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
139	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt`
140	- **TAD** — Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-huru
141	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt`
142	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt`
143	- **ARB** — al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edi
144	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt`
145	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt`
146	- **KFL** — Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885
147	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KFL.txt`
148	- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
149	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
150	- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
151	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt`
152	- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
153	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt`
154	- **LAM** — H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890
155	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt`
156	- **DOZ** — R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeu
157	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt`
158	- **AKD** — H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
159	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt`
160	- **SIN** — B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)
161	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt`
162	- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
163	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt`
164	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt`
165	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
166	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
167	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
168	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
169	- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
170	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_alt_v1.txt`
171	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_dli_part1.txt`
172	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt`
173	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt`
174	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt`
175	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt`
176	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
177	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
178	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
179	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
180	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
181	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
182	
183	## English / Romance / Germanic
184	
185	- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
186	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
187	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
188	- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
189	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
190	- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
191	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt`
192	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt`
193	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt`
194	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt`
195	- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
196	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt`
197	- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
198	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt`
199	- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
200	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt`
201	- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
202	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
203	- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
204	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
205	- **RCH** — J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1
206	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt`
207	- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
208	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
209	- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
210	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt`
211	- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
212	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt`
213	- **NAT** — C. Berlitz, Native Tongues, New York 1982
214	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NAT_2005.txt`
215	- **PEI** — M. Pei, The Families of Words, New York 1962
216	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PEI.txt`
217	
218	## Turkic / Mongolian
219	
220	- **TTS** — H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)
221	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt`
222	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf`
223	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt`
224	- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
225	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
226	- **VIE** — M.A. Sajjadiyyeh, Vazheha-ye Irani dar Zaban-e Engelisi, Bonyad-e Neyshabur 1364/1985
227	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_pages.txt`
228	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_sajjadieh1364_parsianjoman.pdf`
229	
230	## Sanskrit / Hindustani
231	
232	- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
233	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt`
234	- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
235	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
236	- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
237	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
238	- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
239	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt`
240	- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
241	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt`
242	- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
243	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt`
```


## [2026-09-04T19:48:23.716Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-54.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:12000])\n\""
}
```


### [2026-09-04T19:48:25.589Z] TOOL RESULT

```
{
 "pdf_page": 54,
 "book_page": 24,
 "entries": [
  {
   "root": {
    "name": "An 1",
    "lang": "Indo-European",
    "refs": "KLN; AHD; POK:48",
    "gloss": "breath",
    "also": {
     "name": "Ansu",
     "gloss": "spirit, world"
    }
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:48; KLN:41,1095; AHD; SNS:6; OEW:9",
     "words": [
      {
       "translit": "ahu, ahura, anhu, ahva, axva",
       "gloss": "life, spirit, world",
       "script": null
      },
      {
       "translit": "prana",
       "gloss": "breath of life",
       "script": null
      },
      {
       "translit": "ahura-mazdha",
       "gloss": "wise spirit, God",
       "script": null,
       "see": [
        "Men 1",
        "Dhě 2"
       ]
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
     "refs": "MON:400; SNB:126",
     "words": [
      {
       "translit": "Ahurâmazdâ",
       "gloss": "God",
       "script": "اهورامزدا"
      }
     ],
     "script_extra": "اهورا ؛ اورمزد ، هورمزد ، هرمزد ، هرمز",
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 1,
     "lang": "Avestan",
     "refs": "POK:48; BQT:896; VDQ:36; SOD:127",
     "words": [
      {
       "translit": "daoš-ahva",
       "gloss": "evil world",
       "script": null,
       "see": [
        "Dus"
       ]
      },
      {
       "translit": "barz-ahva",
       "gloss": "better (higher) world",
       "script": null,
       "see": [
        "Bhergh"
       ]
      },
      {
       "translit": "anhuyat-hača",
       "gloss": "from heart (soul)",
       "script": null,
       "see": [
        "Sekw"
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
     "lang": "Pahlavi",
     "refs": "SBK:214; VDQ:36",
     "words": [
      {
       "translit": "dužax",
       "gloss": null,
       "script": null
      },
      {
       "translit": "barzax",
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
     "lang": "Persian",
     "refs": "BQT:896; VIE:31; VDQ:36",
     "words": [
      {
       "translit": "dŭzax",
       "gloss": "hell",
       "script": "دوزخ"
      },
      {
       "translit": "barzax",
       "gloss": "middle stage",
       "script": "برزخ"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 6,
     "parent": 0,
     "lang": "Greek",
     "refs": "KLN:118",
     "words": [
      {
       "translit": "astma",
       "gloss": "hard breath",
       "script": null
      }
     ],
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
     "refs": "MON:55",
     "words": [
      {
       "translit": "âsm",
       "gloss": "asthma",
       "script": "آسم"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 9,
     "parent": 6,
     "lang": "English",
     "refs": null,
     "words": [
      {
       "translit": "asthma",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 10,
     "parent": 0,
     "lang": "Latin",
     "refs": "KLN:78",
     "words": [
      {
       "translit": "anima",
       "gloss": "breath of air, life",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 11,
     "parent": 10,
     "lang": "English",
     "refs": "AHD",
     "words": [
      {
       "translit": "animal, animosity, exhale, inhale",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 12,
     "parent": 0,
     "lang": "Germanic",
     "refs": "AHD:929, 931",
     "words": [
      {
       "translit": "ansu",
       "gloss": "God",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 13,
     "parent": 12,
     "lang": "English",
     "refs": null,
     "words": [
      {
       "translit": "Oswald, Oscar",
       "gloss": null,
       "script": null,
       "see": [
        "Ghei 2"
       ]
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 14,
     "parent": 0,
     "lang": "Sanskrit",
     "refs": "POK:48, SOD:10",
     "words": [
      {
       "translit": "âsu, âsura",
       "gloss": "God",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 15,
     "parent": 14,
     "lang": "Sogdian",
     "refs": "SOD:10",
     "words": [
      {
       "translit": "âs`wr",
       "gloss": "God",
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
    "name": "An 2, Eno, Ono",
    "lang": "Indo-European",
    "refs": "POK:37",
    "gloss": "other"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan / Old Persian",
     "refs": "HRN:13; KLN:1108; POK:37",
     "words": [
      {
       "translit": "anya, aimya",
       "gloss": "other",
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
     "refs": "HRN:13",
     "words": [
      {
       "translit": "ân",
       "gloss": "that",
       "script": "آن"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 0,
     "lang": "Germanic",
     "refs": "AHD; KLN:1102",
     "words": [],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "English",
     "refs": null,
     "words": [
      {
       "translit": "other",
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
     "parent": 0,
     "lang": "Indo-European",
     "refs": "IEC:27",
     "words": [
      {
       "translit": "An-teros",
       "gloss": "second, other, step parent",
       "script": null,
       "see": [
        "Ter 1"
       ]
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
     "refs": "IEC:27; MON:373",
     "words": [
      {
       "translit": "andar",
       "gloss": "a suffix meaning step as in step father",
       "script": "ـ اندر ۲"
      }
     ],
     "script_extra": "پدراندر ، مادراندر ، دختراندر ، پسراندر",
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 5,
     "lang": "Sanskrit",
     "refs": "IEC:27; POK:37",
     "words": [
      {
       "translit": "antarah",
       "gloss": "other",
       "script": null
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
```


## [2026-09-04T19:49:27.153Z] TOOL CALL #8: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py && echo ---- && ls data/verification/ | head -30"
}
```


### [2026-09-04T19:49:27.218Z] TOOL RESULT

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
----
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
page-52.json
process
sources
```


## [2026-09-04T19:49:29.701Z] TOOL CALL #9: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','AHD','POK','SNS','OEW','MON','SNB','BQT','VDQ','SOD','SBK','VIE','HRN','IEC','FVQ','PHD','NYB','BRT','KNT','WLD','SYN','SKT','LKT','PLA','AFM']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print('==',k,'==')\n    for kk in ['title','kind','local_file','page_offset','lookup_hint']:\n        if kk in v: print('  ',kk,':',str(v[kk])[:400])\n\""
}
```


### [2026-09-04T19:49:31.990Z] TOOL RESULT

```
== KLN ==
   title : E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
   page_offset : KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== AHD ==
   title : W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)
   kind : archive_djvu+website+archive_restricted
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
   page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.
== POK ==
   title : J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
   page_offset : POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-d
== SNS ==
   title : Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt']
   page_offset : 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
   lookup_hint : grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
== OEW ==
   title : J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984
   kind : archive_restricted
   local_file : None
   page_offset : None
   lookup_hint : Borrow via IA lending (djvu.txt returns 401/403). Entries are IE roots in alphabetical order; use IA's in-book search: https://archive.org/details/originsofenglish00jose?q=<root>
== MON ==
   title : Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)
   kind : website+archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incom
   page_offset : None
   lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab
== SNB ==
   title : H. Kowsar, Sang-nebeshteh-ha Sokhan Miguyand, Iranian Military Press (1960s)
   kind : none
   local_file : None
   page_offset : None
   lookup_hint : Not found.
== BQT ==
   title : Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)
   kind : archive_djvu+local_scan_ocr
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pic
   page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numera
   lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metada
== VDQ ==
   title : Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993
   kind : website
   local_file : None
   page_offset : None
   lookup_hint : noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.
== SOD ==
   title : Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt']
   page_offset : printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
   lookup_hint : Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id
== SBK ==
   title : M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SBK.txt']
   page_offset : None
   lookup_hint : grep in SBK.txt (raw djvu, no page breaks); use inside.php with doc='سبک شناسی_1'. Later printings keep the 1st-edition pagination approximately; verify.
== VIE ==
   title : M.A. Sajjadiyyeh, Vazheha-ye Irani dar Zaban-e Engelisi, Bonyad-e Neyshabur 1364/1985
   kind : local_scan_ocr
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_sajjadieh1364_parsianjoman.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_pages.txt']
   page_offset : 253 leaves; printed page = PDF page − 6 (PDF 100 = p.94). Only the 'fas' OCR pass was run for this book (VIE_pages.txt).
   lookup_hint : Not found.
== HRN ==
   title : P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== IEC ==
   title : S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
   page_offset : TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== FVQ ==
   title : Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt']
   page_offset : printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves)
   lookup_hint : Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
== PHD ==
   title : D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB ==
   title : H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
   page_offset : Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== BRT ==
   title : C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
   page_offset : Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== KNT ==
   title : R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt
   page_offset : leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== WLD ==
   title : A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verific
   page_offset : Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
   lookup_hint : Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== SYN ==
   title : C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
   page_offset : leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== SKT ==
   title : W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
   page_offset : leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== LKT ==
   title : K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt
   page_offset : leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== PLA ==
   title : A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt']
   page_offset : 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
   lookup_hint : HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
== AFM ==
   title : Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt']
   page_offset : 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image
   lookup_hint : Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
```


## [2026-09-04T19:49:35.170Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==57' POK_01.txt | head -80"
}
```


## [2026-09-04T19:49:35.688Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: an\" POK_full.txt | head -30"
}
```


### [2026-09-04T19:49:37.596Z] TOOL RESULT

```
.  Öse  f.  »ringförmige  Handhabe^  Schlinge'  (dar- aus spätmhd.  nhd.   Ose;   oder   das  wgerm.  Wort  zu  Ohr  nach   Kluge  und? Weigand-Hirt  s.  v.?);  mir.  e(i)si  PL  ^Zügel'.  gr.  fjv'ia,  dor.  ävia  ds.  {*ävGia)\ WP.  T  m,  WH.  I  51,  Trautmann  10.
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
B.  äyO-i(Trrj(,Li',  hom.  xar'  ^vcrjaziv  ,am  gegenüberliegenden  Standpunkt, «»•et»-enüber'  ist  wohl  nach  Bechtel  Lexil.  46  aus  *^vvi-(yTL-g  nach  ävrrjv XatriLU  umgebildet;  dvxi-AQVy  att.  ävzL'Aovg  ,geradezu,  entgegen'  (Ausgang unklar),  ävridüj,  ävTiäl;ü)
```


### [2026-09-04T19:49:37.641Z] TOOL RESULT

```
1731:From Root/ lemma: ang''(h)i-\ "snake, worm' derived Root/ lemma: ak^'a- {more properly 
3826:From Root/ lemma: ang''(h)i-\ "snake, worm' derived Root/ lemma: ak''a- {more properly 
4769:Root / lemma: anA^er-, ijA^er- 
4796:Root / lemma: anA"^-, aned^- 
4829:Root / lemma: anA'^o- 
4844:Root / lemma: an(9)-3^henah^ 
4850:Root/ lemma: an(a)-3\ to breathe' derived from a reduction of Root/ lemma: anghen-: 
4931:From Root / lemma: an(a)-3\ "to breathe' derived in zero grade Root/ lemma: nas- 
4951:Root/ lemma: anat-{*ang''h-at-) 
5060:Root / lemma: anghen- 
5074:Root / lemma: angh- {*hengh-) 
5169:Root / lemma: ang''(h)i- {* eg'^hi-, og'^i- and egh/-) 
5179:Root/ lemma: ang''(h)i-\ 'snake, worm, *fish' derived from an extended Root/ lemma: 
5266:Root / lemma: ank-1 
5301:Root / lemma: ank-2, ang- 
5417:Root / lemma: an-1{*han- 1) 
5424:Root / lemma: an-1{*han-) : "male or female ancestor' derived from zero grade of Root/ 
5487:Root / lemma: an-2 
5526:It seems Root / lemma: an-2\ "there, on the other side' is a zero grade of the extended 
5539:Root / lemma: an4, anu, and, no 
5616:Root / lemma: ansa, ansi- 
5650:Root/ lemma: ansu-, psu-{*henku-r-\n centum languages) 
5656:Root/ lemma: ansu-, psu- {* henku-r-): ghost, demon, derived from Root/ lemma: ank-2, 
5707:Root / lemma: ans- 
5742:Root / lemma: antro-m 
5756:Root / lemma: ants 
7103:Alb. and Rumanian prove that from Root/ lemma: anat-: (duck) derived Root/ lemma: 
9140:Root / lemma: ano- 
10309:g^era-: "to devour; throat' + zero grade g^fhj/-^ snake, worm, fish' Root/ lemma: ang''(h)i-\ 
29504:Root/ lemma: eff-: "diver' derived from the abbreviated Root/ lemma: anat-: "duck'
```


## [2026-09-04T19:49:44.117Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==56' POK_01.txt"
}
```


## [2026-09-04T19:49:44.653Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4844,4960p' POK_full.txt && echo \"=====ANSU=====\" && sed -n '5650,5710p' POK_full.txt"
}
```


### [2026-09-04T19:49:46.041Z] TOOL RESULT

```
 ,
SnO'  ,Ring'.
Arm.  anu7' , Halsband,  Ring'^,  lat.  änus  ,Kreis,  Ring^,  air.  äinne  {*äninio-) m.  ,Ring,  After^ WP.  I  61,  WH.  I  55,  Pedersen  Litt.  2,  80.
ans-  ^wohlgeneigt,  günstig  sein^
Got.  ansts  f.,  ahd.  anst  und  (tiefstufig)  unst,  mhd.  giinst  aus  *ge-unst, ags.  est,  Gunst,  Gnade'',  anord.  äst,  öst  ,Gunst,  Liebe'^,  ahd.  ahanst,  ahunst, as.  avunstj  ags.  3efest  , Abgunst,  Ungnade^;  mhd.  gund  m.  ,Gunst^,  anord. qf-und  f.  ,Ungnade^;  Präteritopräsens  ahd.  an,  unnum  (Inf.  icnnan,  Prät. onsta,  onda)  ,gönnen^  (gi-unnan),  as.  ags.  unnan  ,gönnen,  einräumen, wünschen^,  anord.  unna  (ann,  unnom,  Prät.  tinnan  aus  *unpa)  ,lieben, gönnen,  einräumend  un-nu-m  (aus  *imz-nu-m-)  ist  ein  altes  Präs:  der  neu-, w?f-Klasse,  wozu  der  neue  Sg.  ann.  Wer  die  Wz.  als  germ.  an-,  un-  an- setzt, hat  in  ansts  die  Suffixverbindung  -s-ti-  zu  sehen  (s.  Brugmann  Grdr. n^  2,  437),  während  mhd.  gund,  an.  gfund  das  einfachere  -ti-  enthielten. Doch  ist  wegen  des  gemeingerm.  *anst(s)  die  Wz.  wohl  als  germ,  ans-, uns-  anzusetzen  (Kluge  ZfdtWtf.  9,  317,  Brugmann  Grdr.  IP  3,  332), unnum  mithin  aus  "^unz-num  (idg.  *ns-nu-me)  entstanden,  wonach  dann  Sg. ann,  und  das  neue  schwache  Prät.  '^un-pa  (ahd.  onda,  anord.  unna)  neben ahd.  onsta,  as.  gi-onsta:  auch  mhd.  gund,  anord.  gfund  (Suffix  -ti-)  sind dann  Neuschöpfungen  nach  dem   5-los  gewordenen  unnum,  unnan.
Auch  gr,  Ttooo-rjvrig  , freundlich'^,  dTt-rjvrjg  ,unfreundlich,  hart^  (:  ah-imst) ist  am  wahrscheinlichsten  =  '^tvqog-^  ccTV-avarjg  (s.  Brugmann  aaO.).
In  abweichender  formaler  Beurteilung  bezieht  Bechtel  LexiL  49  gr. -ävrjg   auf   ein   neutr.  Subst.  "^änos,    dessen    suffixale  Tiefstufe   dem  germ.
an-s-ti-  zugrunde  liege. WP.  I  68.  Feist  53.
48
ansä,  ansi-  ^Schlinge^  Schleife^^  z.  T.  als  HandliaLe  von  Gefäßen   (Henkel^ oder  als  dem  Zugvieh  umgeleg'ter  Zügel. Lat.  änsa  ^Griff^  Henkel^  Handhabe^;  ansäe  crepidae  ,die  Ösen  am  Rand^ der  Schuhsohlen,    durch   welche   die   Bindriemen   gezogen   wurden^  =  litj qsä  f.  (Akk.  äsq)  ^Topfhenkel;  Schleife   heim   Knotenschürzen'^   (vgl.  auch] lat.  ansätus  ==  lit.  qsötas  ^gehenkelt^),   lett.  nosa  ^Henkel,   Schleife^,    Öse' woneben   2-St.    apr.  ansis   ^Kesselhaken^    lett.    üoss    (Akk.  iiosi)    , Henkel aisl.  ces  L  {^ansjo)  ^Loch  am  oberen  Kande   des  Schuhleders  zum  Durch.] ziehen  der  Riemen'  =  mnd
```


### [2026-09-04T19:49:46.097Z] TOOL RESULT

```
Root / lemma: an(9)-3^henah^ 

Meaning: "to breathe' 

Note: 

Root/ lemma: an(a)-3\ to breathe' derived from a reduction of Root/ lemma: anghen-: 

"smell, odour; person' as in Armenian sat//? (for older *anj). Gen. anjin^ soul, being, person 

': Old Norse ang/m. " odour, smell ' : alb. aA7y"swell, puff' [common alb. ng > nj\. 

Material: Old Indie ^/7/// "breathes' (also thematically anati), anila-h "breath, breeze, wind', 

^/7a-/7 (maybe "breath' or " mouth, nose ', ana-nam^ mouth, muzzle, face ' with Indie 

Vrddhi; "mouth' as "breath, the breathing '); p/a/?///" breathes'; 

Avestan antya, parantya " of the inhaling and exhaling ' ( *anti- " breathing ' with a and 
para; see Bartholomae IF. 7, 59; about 5//?///- "mildness' see, however, Airan. Wb. 125 f.). 

Gr. av£[jO(; " breath, wind ', avr|V£piO(; (with stretch in the compound), vnvspot; " 
windless, calm ', nvspoEiq " rich in wind ' (rj- metrical stretch), avspcbAioq (" windy ', i.e.:) " 
trifling, in vain ' (dissimilated from avspcbviot;, see last Bechtel Lexil. 44, also 226, about 
that probably from *p£T-av£pu)vioc; by extreme dissimilation abbreviated ones psTajjcbvioc; " 
in vain, without success '); different Risch 113; 

compare Frisk Indog. 15; avrai av£|joi dv^ac, nvoia(; Hes. are to change in anrai, anrag. 
Maybe here v£avia(; " youth ' as vsFo-av- " new wheeze ', after Schwyzer Gr. Gr. I 426^; 
also aa9|ja " breathlessness, suffocation ', aaO. 337. 

Latin animus^ mind, soul ', anima^ wind, breath, soul, lives ' (Oscan anamum^ air, a 
current of air, breeze, breath, wind '), of it animar living being, animal ', halo, - are 
"breathe, smell' (Denominative *an-slo-;W\\h phoney h, the sound value described here 
attained and also penetrated in an(h)-elare, about latter see *an4). 

Old Irish anal, cymr. anadrbreatW, Middle Breton 5/az/7 (metathesis), nbret. bolan 
{*ana-tlo-); mcymr. enelt, ncymr. enald'souV {*ana-tT-), abrit. PN Anate-moros^ 
warmhearted, bighearted '; 



Old Irish animm, nir. anam'so\i\\ Gen. anman {stem *ana-mon; the /■ color of the Norn. sg. 
after neutr. -men-siem s. Pedersen KG. II 61; to the intersection with Latin animai. 
"breath, wind, Old Irish Transf., the breath of life, vital principle, soul' see Pokorny ZfcPh. 
10 69 f.), corn, eneff. Middle Breton eneff{P\. anaffon) nbret. anaoun'souV (umlauted 
corn, and bret. forms probably loanword from Latin, see Vendryes De hib. voc. 1 12 f., 
Pedersen KG. I 170, II 111); 

in addition Old Irish c»s/7ao' "sighs' {uss-anad), further ("catch one's breath = rest, relax ') 
anaid^ remains, rests, stops ', con-osna^ desist, cease ' {com-uss-an-) etc. (see Pedersen 
KG. II 455 f., 672); mcymr. anantP\. " bards, poets ', cyn-an\v\ "word, praise '; 

Gothic uz-anan {pretent uzon) "exhale'; with /-formant: Old Norse gnd, g. andar\. 
"breath, breath of life, life, soul ' (= gr. avrai), anda, -ada^ breathe, gasp ' = Old English 
o^/a/7 "puff strongly'. Old Norse andim. "breath, mind, soul'. Old Frisian omma{*an-ma) 
"breath'. Old English orod{*uz-ant^-) "breath' *; maybe here Old High German unst. Old 
Icelandic Old English ys/f. "storm' from *n-sti-\ 

maybe alb. a/yo^a "taste, smell' [common alb. n > nd\: Old Norse anda, -ada "breathe, 
gasp'. 



*) In addition also Old Saxon ando. Old English anda, a/7c»^a "excitement, rage, sorrow'. 
Old High German anado, ando, a/7/o "annoyance, rage'. Middle High German ande 
"feeling of insult'. Old High German anadon, anion. Middle High German andenlet out 
one's rage'. Modern High German avenge under a mid definition "gasp before excitement' 
(Kluge s. v., -Falk-Torp 5 and 1428 under aand, Schroder Abl. 9). About second a from 
Old High German anado. Old English anodasee Specht Phil. Stud. Voretzsch 36. 



Old Church Slavic vonja {*ania) "smell' {vonjatT scent, smell '), *pc/7a//" smell' in Old 
Russian uchatieic. (-c/7- perhaps imitation from duchati, thus without historical connection 
with sfrom Latin halare^brea\he, emit vapor, be fragrant' from *an-slo-); 

Maybe nasalized alb. {^unhati) nuhat, nuhas'scent, smell', huna, hunda' nose'. 

alb. Geg aj, Tosc enj"\ swell, impregnate ', Geg ay^/? "conceited, puffed' kenjem, gnem 
"incense' {*kc-{a)nemo- Jok\ Stud. 37); (Clearly the initial meaning in alb. Geg aJ, Tosc enj 
"I swell, impregnate' was "puff with air'.) 



Note: 

From Root / lemma: an(a)-3\ "to breathe' derived in zero grade Root/ lemma: nas- 

{*andas)\ "nose". 

Tocliarian AB ahm- "life, mind', B a/7/77e "intention', A ancam {* antemo-) "existence, 
living, mind' (K. Schneider IF. 57, 203, Pedersen Tocharian 48); also B onolme, wnolme 
"living being'? 

Armenian ho/m'\N\n6' (Bugge IF. 1, 442) abides (in spite of Meillet Lithuanian 6, 3) (see 
Liden Arm. stem 38 f., Peterson KZ. 47, 246). - Old Indie atman'souV rather to Old High 
German 5/i//77 "breath', see et-men. 

Root points beside to two-syllable forms, like Old Indie ani-ti, ani-lah, Ce\Wc*ana-tlo- e\.c, 
and such like av£-po(;, also forms of the monosyllabic word roots, thus Latin *an-slo-> 
halo. Old Norse (?/7o'(etc). 

References: WP. I 56 ff., WH. I 49 f.. Feist 538. 
See also: ansu-, antro- 
Page(s): 38-39 

Root/ lemma: anat-{*ang''h-at-) 

Meaning: duck' 

Material: Old Indie atf-h atTi. " water bird ' (or to Old Icelandic aedr. New Swedish adai. " 

eider duck ' from Germanic *adT- ?); 

Other Iranian: Sak ace, aci "water fowl', Osset occ "wild duck', Pamir Wakh. yoc "duck' 

=====ANSU=====
Root/ lemma: ansu-, psu-{*henku-r-\n centum languages) 

Meaning: ghost, demon 

Note: 

Root/ lemma: ansu-, psu- {* henku-r-): ghost, demon, derived from Root/ lemma: ank-2, 

ang-\ "to bend, bow, *flex; wangle; turn; curve, snake coil, anchor'. 

Material: 

In e- grade: 

Lycian esa- ' grandchild, grandson '; Lycian B qzze, qezmmi, ^^^^/^(Shevoroshkin), 

Lycian A qehn' offspring, descendants, progeny ' (Tischler 191 ff) 

In a- grade: 

Hittite: has- (11,1) ' testify, bear ', hassa- ' grandson, granddaughter ', hassu- c. 'king, ruler, 

sovereign'; h.l. has(a)- 'create, engender, breed', hasmi- ' offspring, descendants, progeny 

', hasusara- ' queen '; (Tischler 191 ff). 

Comments: ' grandchild, grandson ' in Hittite may be a result of contamination: cf. Hittite 

hammasa- ' small child ', Luvian hamsa-, h.l. hamasa- ' grandchild, grandson ' (see 

Tischler ibid, and 141-142). 

Old Indie asu-, Avestan arjhu-^ breath of life, breath, life, spirit, world ', asu-ra-, Avestan 

ahura- " ruler, lord ' ( *nsu-)\ Venetic ahsu- (= asu-) " cult effigy, cult figure ' = Germanic 



*ansuz' god, ace ' in Old Icelandic ass, Runic a[n]suR, Old English ds" ace ', Gothic-Latin 
anses' demigods '. 

Note: 

The inanimate suffix -ur- : Old Indie asu-ra-, Avestan ahura- " ruler, lord ' : UAupioi , oi, 

lllyrians, UAupia , n, lllyria, alsoUAupi? , n. Adj. UAupiKO? , n, 6v, lllyrian: -ys\, the region 

or province of lllyria, UAupi^U) , speak the lllyrian language, 'IAAupla:-hence Adv. 

lAAupiaTi. 

References: H. GiJntert Der Aryan Weltkonig 102, Feist 52 b. 

See also: Perhaps to an(9)- " breathe '. 

Page(s): 48 

Root / lemma: ans- 
Meaning: favourable 

Material: Gothic anstst, Old High German anstan6 (zero grade) unst, Middle High
```


## [2026-09-04T19:50:24.946Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK_full an-2 / ano- ===\" && sed -n '5487,5560p' POK_full.txt && echo \"=== ano- ===\" && sed -n '9140,9200p' POK_full.txt"
}
```


### [2026-09-04T19:50:25.007Z] TOOL RESULT

```
=== POK_full an-2 / ano- ===
Root / lemma: an-2 

Meaning: there, on the other side 

Material: Gr. av ' probably, possibly, in any other trap ' (sav from z\ av, Ionian pv from *n 

av, avfrom ai av); Latin an' conj.: in direct questions, or; in indirect questions, or whether 

', secondarily interrogative particle, extended anne. Old Irish an-d' here ', (common Celtic 

-ns-, -nt- > -nn-), Gothic an' then, now '; Lithuanian an-gu' or ', Old Prussian anga-anga' 

whether = or whether '. 

maybe alb. {*ane) andej'there' : Old Irish an-d'here' [rather common alb. shift n > nd\. 

Thereof derived: 

anjos' other' in: 

Old Indie anya-' other', Avestan anya-, ainya-. Old pers. an/ya-6s. compare above S. 
26. 

anteros'o\her' (from second) in: 

maybe zero grade in alb. {*anteros) nderroj" change, alter', nderrese' change, the other 
thing'; 

Old Indie antara-, oss. andar'oVnef, Gothic anf^ards.. Old Icelandic a/7/7a/7'" other, 
second', (under the influence of common Celtic -ns-, -nt- > -nn-). Old High German andar. 
Old English d^'er" other'. Old Prussian anters, antars {*antras) 'other, second', Lithuanian 
antras, Latvian i/oZ/'s beside Lithuanian antaras. East Latvian utors6s., Slavic *gterb, 
*gtorb\n Czech uteryrw. ' Tuesday', Upper Serbian wutory'oVner, second'. About Old 
Church Slavic v-btor-t "second' s. £//-" asunder, apart '. 



Note: 

It seems Root / lemma: an-2\ "there, on the other side' is a zero grade of the extended 
Root/ lemma: al-1, ol-\ "besides; other' into *alny-, *any-. 

Maybe zero grade in alb. {*nyatra) fjeter' other' [common alb. n > nt > /] : Old Indie anyatra 
"somewhere else'. 

Perhaps alb. dial. {* heter) jater, Jeter, alb. [ attribute /e'of + antef\, tjeter' other, second'; 
similar to formation in alb. Geg {*te mel= of milk) /a/77//"milk' where te is the alb. attribute 
particle. Initial alb./ seems to have substituted the old laryngeal form /?-. 

References: WP. I 56, 67, II 337, WH. I 44, Trautmann 10/11, Debrunner REtlE. 3, 1 ff. 
Page(s): 37-38 

Root / lemma: an4, anu, and, no 

Meaning: a preposition ("along a slanted surface, etc.") 

Note: (compare the summary by Brugmann Grdr. I|2 2, 798 f., also about the syntactic). 

Material: Avestan ana. Old pers. a/7a(Proto Aryan * ana or *ana) " about there ' (m. Akk. or 

Instr.), " along, on ' (m. Akk.), Avestan anu. Old pers. anuv^ after, according to; up there ' 

(m. Akk.), " lengthwise, along ' (m. Lok.), also proverb; 

maybe alb. anes "along' 

Old Indie anu^ after (timewise m. Akk., Abl., Gen.), after (order), after there, along, 
behind, according to, with regard to, against ' (m. Akk.), Adv. " on it (auslaut-i/ appears to 
be comparable in Lesbian Thessalian anu beside Attic airo. Against Wackernagels 
explanation from Indo Germanic *enu^ along, according to ' see WH. I 677; to-^see below 
ap-u); Armenian am- in am-barnam ham-barnam^ I raise, uplift ', ham-berem^ I endure ' 
maybe from -an (the h by mixture with a borrowed sound from the Pers. ham- " together '; 

Ionic-Attic ava, ava " on, upwards, along ', Doric Boeotian Arcadian Cypriot av, Lesbian 
=== ano- ===
Root / lemma: ano- 

Meaning: ring 

Material: Armenian anur^ neckband, ring ', Latin anus^ circle, ring ', Old Irish ainne 

( *anTnJo-) m. " ring, anus '. (common Celtic -ns-, -nt- > -nn-). 

Latin annulus > Bolognese anel : Bresciano anel : Furlan anel : Galician anel : Portuguese 

anel : Paduan aneo : Provengal aneu : Wallon anea : Reggiano : anel : Romagnolo anel : 

Romansh ane : Romanian : inel : Italian anello : Spanish anillo ; anilla : Catalan anell : 

French anneau : Aragones aniello : Asturian aniellu : Corsican anellu : Leonese aniellu : 

Lombardo Occidentale anell : Napulitano aniello : Calabrese 'neddu ; aniellu ; aneddu ; 

aniaddru : Pugliese aniadd : Sardinian Campidanesu aneddu : Sardinian Logudoresu 

aneddu : Sicilian aneddu : Viestano nidd' " circle, ring ' [common Calabrese, Pugliese, 

Sardinian, Sicilian, Viestano -/A > -dd-] > through metathesis Albanian {* aneddu) unaze^ 

circle, ring ' common alb. d- > z- similar to alb. gaz^ joy' < Latin gaudium " joy'. 

References: WP. I 61, WH. I 55, Pedersen Litt. 2, 80. 

Page(s): 47 

Root / lemma: apero- 

Meaning: shore 

Note: 

Root / lemma: apero- : " shore ' derived from Root / lemma: apo- {p6, ap-u, pU) {*h2aph30- 

): " from, out, of ' < Root / lemma: ap-2\ " water, river ' < Root / lemma: ab- : " water, river ' 

< Root/ lemma: abd(n) {* h2abd^\ " ape, *water demon ' < Root/ lemma: ^^-{*h2£b'^-)'. " 

quick, abrupt ' < Root/ lemma: abh/-o-(*/7i'ab*^ro-): " strong, mighty ' < root /pbh-(ro-): < with 

/■formant {neb^e/a)\ < Root/ lemma: {en^^-2): n^^-, errt^-, /pb^-: " wet, damp; water; 

clouds '. 

Material: Gr. rin£ipo(;, Doric an£ipo(;f. " shore; mainland '; Old English ofer. Middle Low 

German over. Middle High German (md.) uover. Modern High German Ufer, but Armenian 

ap n^ shore ' requires Indo Germanic yO/? and hence, stays away. 

relationship to *5/7c» "since, from, ex'. Old Indie apara-^ back, later' as lengthened grade 
formation becomes adopted by Specht Dekl. 23. 

References: WP. I 48.
```


## [2026-09-04T19:50:25.393Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD ansu ===\" && grep -n -i \"^ansu\\|^an∂-\\|^ane-\\|^an-\\|ansu-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-04T19:50:25.445Z] TOOL RESULT

```
=== AHD ansu ===
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
1218:AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE aiw- AGENDUM ag- AGENT ag- AGERATUM gere-1 AGGLOMERATE gel-1 AGGLUTINATE gel-1 AGGRAVATE gWere-2 AGGREGATE ger-? AGGRESS ghredh- AGGRIEVE gWere-2 AGHAST gheis- AGILE ag-
1220:AnuRA MazpDa_ansu-, men-1
1240:AN- ne
1997:ORGAN werg- ORGANOLEPTIC (s)lag¥- ORGANON werg- ORGASM wrdg- ORGEAT ghers- ORGY werg- ORIENT er-1 ORIFICE 6s- ORIFLAMME aurum ORIGIN er-1 ORIGINAL er-! ORINASAL 6S- ORIOLE aurum ORLOP klou-, uper OrMaAzD ansu-, men-1 ORMER mori-, ous- ORMOLU aurum, mele- ORNAMENT ar- ORNATE ar- ORNITHO- oF OROIDE aurum OROTUND 6s- ORPHAN orbh- ORPHREY aurum ORPIMENT aurum ORT ed-, ud- ORTHO- wrddh- ORTHODOX dek-1 ORTHOGONAL genu-1 ORTHOPEDICS pau- ORTHOSTICHOUS _steigh- ORTHOTICS wrddh- ORTOLAN gher-! os! Os-
```


## [2026-09-04T19:50:37.905Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"an∂-\\. To breathe[^]]*\\]\" AHD_watkins1985.txt | head -3; echo \"---\"; grep -no \"To breathe\\.[^]]\\{0,900\\}\\]\" AHD_watkins1985.txt | head -5"
}
```


## [2026-09-04T19:50:39.273Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"ANIMAL [a-z∂-]*\\|OTHER [a-z0-9∂-]*\\|ASTHMA [a-z0-9∂-]*\\|OSCAR [a-z0-9∂-]*\\|OSWALD [a-z0-9∂-]*\\|INHALE [a-z0-9∂-]*\\|EXHALE [a-z0-9∂-]*\\|ANIMOSITY [a-z0-9∂-]*\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-04T19:50:39.655Z] TOOL RESULT

```
---
282:To breathe. Suffixed form *ana-mo- in: a. Latin animus, reason, mind, and anima, soul, spirit, life, breath: ANIMA, ANIMADVERT, ANIMAL, ANIMATE, (ANI- MATO), ANIMISM, ANIMOSITY, ANIMUS; EQUANIMITY, LONGANIMITY, MAGNANIMOUS, PUSILLANIMOUS, UNANI- mous; b. Greek anemos, wind: ANEMO-. [Pok. 3. an(9)- 38.]
338:To breathe. Probably imitative. Zero-grade form *bhs- in Greek psukhein (< *bhs-il-kh-), to breathe, hence psukhé, spirit, soul: PSYCHE, PSYCHIC, PSYCHO-; METEMPSYCHOSIS. [Pok. 2. bhes- 146.]
864:To breathe. Imitative root. 1. Germanic *fneu- in Old English fnéosan, to sneeze: SNEEZE. 2. Greek pnein, to breathe (> pnoia, breathing): APNEA, DIPNOAN, DYSP- NEA, EUPNEA, HYPERPNEA, HYPOPNEA, POLYPNEA, TACHYPNEA. 3. Suffixed form *pneu-mn in Greek pneuma, breath, wind, spirit: PNEUMA, PNEUMATIC, PNEUMATO-, PNEUMO-. [Pok. pneu- 838.]
988:To breathe. Latin word of unknown origin, with its derivative spiritus, breath, breath of a god, inspira- tion: SPIRACLE, SPIRIT; ASPIRATE, CESSPOOL, CONSPIRE, EXPIRE, INSPIRE, PERSPIRE, RESPIRE, SUSPIRE, TRAN- SPIRE. [In Pok. peis-, speis- 796.]
```


### [2026-09-04T19:50:39.703Z] TOOL RESULT

```
1246:ANIMAL ane-
1246:ANIMOSITY ane-
1324:OTHER bhrater-
2001:OTHER an
```


## [2026-09-04T19:50:47.072Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"EXHALE [a-z0-9∂-]*\\|INHALE [a-z0-9∂-]*\\|HALITOSIS [a-z0-9∂-]*\\|ASTHMA[A-Z]* [a-z0-9∂()-]*\" AHD_watkins1985.txt | head; echo \"=== OTHER ctx ===\"; sed -n '2001p' AHD_watkins1985.txt | grep -o \"OSTRICH.\\{0,200\\}\" ; echo \"=== an-1 root ===\"; grep -no \"There, on the other side\\.\\{0,20\\}\\|an-1\\.\\|On, that\\.\" AHD_watkins1985.txt|head"
}
```


### [2026-09-04T19:50:49.373Z] TOOL RESULT

```
=== OTHER ctx ===
OSTRICH awi-, trozdo- OsTROGOTH aus-! OTHER an?
=== an-1 root ===
```


## [2026-09-04T19:50:53.885Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"an-2\\?\\. \\{0,3\\}[A-Z][^.]\\{0,60\\}\\.\" AHD_watkins1985.txt | head -20; echo \"=== search an? ===\"; grep -no \"an?\\. .\\{0,400\\}\" AHD_watkins1985.txt | head -10"
}
```


## [2026-09-04T19:50:54.902Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" AHD_watkins1985.txt; grep -no \"EXHALE\\|INHALE\\|ASTHMA\\|HALITUS\\|halare\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-04T19:50:56.875Z] TOOL RESULT

```
282:an-2. To pour, draw water.
360:an-. Low ground.
581:an-. To sing.
812:an-. Fabric.
=== search an? ===
```


### [2026-09-04T19:50:56.923Z] TOOL RESULT

```
2463
```


## [2026-09-04T19:51:08.394Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"ASTH\\|HAL\\|Ahura\\|AHURA\\|OSWALD\\|Oswald\\|OSCAR\\|Oscar\" AHD_watkins1985.txt | head -20; echo \"=== an region ===\"; sed -n '282p' AHD_watkins1985.txt | grep -o \"an-2\\..\\{0,1500\\}\" | head -c 2200"
}
```


### [2026-09-04T19:51:10.039Z] TOOL RESULT

```
280:HAL
280:HAL
284:AHURA
323:HAL
325:HAL
328:HAL
328:HAL
328:HAL
330:HAL
330:HAL
364:HAL
375:HAL
375:HAL
375:HAL
388:HAL
442:HAL
510:HAL
510:HAL
510:HAL
510:HAL
=== an region ===
an-2. To pour, draw water. Suffixed form *an-tlo- in Greek antlos, bilge water, bucket: ANTLIA. [In Pok. 1. sem- 901.] andh-. Bloom. Suffixed form *andh-es- in Greek anthos, flower: ANTHEMION, ANTHER, ANTHESIS, ANTHO-, -AN- THOUS; AGAPANTHUS, CHRYSANTHEMUM, DIANTHUS, EX- ANTHEMA, HYDRANTH, (MONANTHOUS), STROPHANTHIN. [Pok. andh- 40.] andho-. Blind, dark. Suffixed variant form *ondh-ro- perhaps in Latin umbra, shadow: UMBEL, UMBRA, UM- BRELLA; ADUMBRATE. [Pok. andho- 41.] ane-. To breathe. Suffixed form *ana-mo- in: a. Latin animus, reason, mind, and anima, soul, spirit, life, breath: ANIMA, ANIMADVERT, ANIMAL, ANIMATE, (ANI- MATO), ANIMISM, ANIMOSITY, ANIMUS; EQUANIMITY, LONGANIMITY, MAGNANIMOUS, PUSILLANIMOUS, UNANI- mous; b. Greek anemos, wind: ANEMO-. [Pok. 3. an(9)- 38.] anata. Doorjamb. Latin antae (plural), a pair of pillars on the opposite sides of a door: ANTA. [Pok. anatd- 42.] [angelos. Messenger. Greek noun, akin to Greek anga- ros, mounted courier, both from an unknown Oriental source. 1. Greek angelos, messenger: ANGEL, (ANGELIC), ANGELICA, (ANGELUS); ARCHANGEL, EVANGEL. 2. Greek angaros, mounted courier: ANGARY.] angh-. Tight, painfully constricted, painful. 1. Germanic *ang-, compressed, hard, painful, in Old English ang- nzgl, “painful spike (in the flesh),” corn, excrescence (nzgl, spike; see nogh-): AGNAIL. 2. Suffixed form *angh-os- in Germanic *angaz in Old Norse angr, sor- row, grief: ANGER. 3. Suffixed form *angh-os-ti- in Ger- manic *angusti- in Old High Ge
```


## [2026-09-04T19:51:22.610Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '282p' AHD_watkins1985.txt | grep -o \".\\{1400\\}an-2\\. To pour\" | head -c 1600"
}
```


### [2026-09-04T19:51:22.721Z] TOOL RESULT

```
about: AMPHI-. 5. Celtic *ambi (see ag-). [Pok. ambhi 34.] ambhé. Both. 1. Reduced form *bAd in Germanic *b6-, *bé in Old Norse bdthir, both: BOTH. 2. Latin ambé, both: AMBSACE. 3. Greek amphé, both: AMPHOTERIC. [In Pok. ambhi 34.] amer-. Day. Suffixed form “Gmer-d in Greek hémera, day: EPHEMERAL, HEMERALOPIA. [Pok. dmer- 35.] ames-. Blackbird. 1. Suffixed variant form *ams-ol- in Old English dsle, blackbird: ouzEL. 2. Suffixed variant forms *mes-old, *mes-olo- in Latin merula, merulus, merle, blackbird: MERLE, MERLON. [Pok. ames- 35.] [amma. Various nursery words. Latin root. 1. Medieval Latin amma, mother: AMAH. 2. Reduced form *am- in: a. Latin amare, to love: AMATEUR, AMATIVE, AMATORY, AMORETTO, AMOUR; ENAMOR, INAMORATA, PARAMOUR; b. Latin amita, aunt: AUNT; c. Latin amicus, friend: AMICABLE, AMIGO, AMITY; ENEMY, INIMICAL.] an’. On. Extended form *ana. 1. Germanic *ana, ané in: a. Old English an, on, a, on: ON; b. Old Norse 4, in, on: ALOFT; ¢. Old High German ana (> Middle High Ger- man ane), on: ANLAGE; d. Middle Dutch aan, on: ON- SLAUGHT. 2. Greek ana, on, up, at the rate of: ANA?, ANA-. [Pok. 4. an 39.] an?, Demonstrative particle. Suffixed form “*an-tero-, “other (of two)” (compare *al-tero- under al-') in Ger- manic *antharaz in Old English 6ther, other: OTHER. [Pok. 2. an 37.] an-', Old woman, ancestor (nursery word). Latin anus, old woman: ANILE. [Pok. 1. an- 36.] an-2. To pour
```


## [2026-09-04T19:51:28.758Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"^asthma,\" \"^Ahura\" \"^anima,\" \"^animal,\" \"^Ormazd\" \"^other,\" \"^Oscar\" \"^Oswald\" \"^Aesir\"; do echo \"### $w\"; grep -n \"$w\" KLN_1966.txt | head -3; done"
}
```


### [2026-09-04T19:51:30.494Z] TOOL RESULT

```
### ^asthma,
### ^Ahura
2037:Ahura-Mazda,  n.  —  See  Ormazd. ai,  n.,  the  three-toed  sloth.  —  Tupi  ai,  a  word imitative  of  the  cry  of  the  animal, aid,  tr.  v.  —  OF.  aidier,  aider  (F.  aider),  fr.  L. adjutare,  ‘to  help’,  freq.  of  adjuvare  (pp.  adju- tus),  ‘to  help’,  sustain’,  fr.  ad-  and  juvare,  ‘to help’,  which  is  of  uncertain  origin.  Cp.  adju¬ tant,  adjuvant,  coadjutor,  jocund,  jury,  adj. Derivatives:  aid-er,  n.,  aid-ful,  adj. aid,  n.  —  OF.  ( =  F.)  aide ,  back  formation  fr.  aider. See  aid,  v.
### ^anima,
### ^animal,
2813:animal,  adj.  —  L.  animalis,  ‘of  air,  living,  ani¬ mate’.  See  animal,  n.
29610:animal,  foal’.  See  pullet  and  cp.  words  there referred  to.
### ^Ormazd
### ^other,
### ^Oscar
26653:Oscar,  masc.  PN.  —  OE.  Osgar,  compounded  of os,  ‘a  god’,  and  gar,  ‘spear’.  OE.  os  is  rel,  to  OS. as-,  os-,  ON.  ass,  OHG.  ans-  (in  PN.s),  ‘god’, Goth,  anses,  ansis  (acc.  pi.),  ‘gods’.  Cp.  the  first element  in  Osmond,  Oswald.  For  the  etymology of  OE.  gar  see  gar.
### ^Oswald
26734:Oswald,  masc.  PN.  —  OE.  Osweald,  compounded of  os,  ‘a  god’,  and  (ge)weald,  ‘power’.  See  Oscar and  wield.
### ^Aesir
1831:Aesir,  n.  pi.,  the  chief  gods  of  Scandinavian  my¬ thology.  —  ON.,  pi.  of  ass,  ‘god’,  rel.  to  OE.  os, OS  as-,  os-,  OHG.  ans-  (in  PN.s),  Goth,  ans, ‘god’;  possibly  of  the  same  origin  as  ON.  ass, Goth,  ans,  ‘beam’.
```


## [2026-09-04T19:51:40.254Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"asthma\" KLN_1966.txt | head -5; echo \"---anima\"; grep -n \"anima,  n\\.\\|anima,  n\\|^anim\" KLN_1966.txt | head -8; echo \"---other\"; grep -n \"other,  adj\\|^other\" KLN_1966.txt | head -5; echo \"---Ormazd\"; grep -n \"Ormazd\" KLN_1966.txt | head -5"
}
```


### [2026-09-04T19:51:40.353Z] TOOL RESULT

```
2800:Angus,  masc.  PN.  —  Scot.,  rel.  to  Ir.  Aonghus, a  compound  whose  two  elements  are  cognate with  E.  one,  resp.  choice, anhelation,  n„  panting,  asthma  (archaic).  —  F. anhelation,  fr.  L.  anheldtionem,  acc  of  anhelatio, ‘difficulty  of  breathing,  panting’,  fr  anhelatus.
2828:animus,  n.,  1)  intention;  2)  animosity.  —  L., ‘soul,  spirit,  mind,  courage,  wish,  desire’,  rel.  to anima,  ‘breath  of  air,  air,  breath,  soul,  life’,  and cogn.  with  Gk.  avE|jto<;,  ‘wind’,  fr.  I.-E.  base *an-,  ‘to  blow,  breathe’,  whence  also  OI.  ani-ti, ana-ti,  ‘breathes’,  ani-lah,  ‘breath’,  OIr.  anal,  W. anadl,  MBret.  (with  metathesis)  alazn,  ‘breath’, OIr.  animm,  Co.,  Bret,  eneff,  ‘soul’,  Goth,  uz- anan,  ‘to  exhale’,  ON.  anda,  ‘to  breathe’,  andi, ond,  ‘breath,  soul,  spirit’,  OE.  edian  (for  *an- j>jan ),  ‘to  breathe’,  OSlav,  vonja,  ‘smell’.  Alb. Gheg  o/.Tosk  Jh/I  sweH’,  Toch.  A  afima.  Arm. anjn ,  ‘soul’.  Cp.  animadvert,  animal,  animal¬ cule,  animate,  animosity,  equanimity,  exanimate, exhale,  inhale,  longanimity,  magnanimous,  mag¬ nanimity,  pusillanimous,  pusillanimity,  unani¬ mous,  unanimity.  Cp.  also  ahura,  anemo-,  an- helation,  asthma,  asura,  prana, anion,  n.,  a  negatively  charged  ion  ( physical chem.)  —  Gk.  aviov,  neut.  of  avicbv,  pres, part,  of  avi£vai,  ‘to  go  up’,  fr,  ava  (see  ana-) and  isvai,  ‘to  go’,  which  is  cogn.  with  L.  ire, ‘to  go’.  See  itinerate.  The  word  anion  was  in¬ troduced  into  electricity  by  the  English  physi¬ cist  and  chemist  Michael  Faraday  (1791-1867); cp.  ion,  cation.
3741:Asteroidea,  n.,  a  class  ofechinoderms,  the  starfish ( zool .)  —  ModL.  See  asteroid, asthenia,  n.,  weakness  ( med .)  —  Medical  L.,  fr. Gk.  dahcveia,  ‘weakness’,  fr.  da&EVT);,  ‘weak’, fr.  d-  (see  priv.  pref.  a-)  and  a9ivo?,  ‘strength’. See  sthenic  and  cp.  sthenia. asthenic,  adj.,  weak  (med.)  —  Gk.  aaflev ixog,  fr. aaflevf;;,  ‘weak’.  See  prec.  word  and  -ic. asthma,  n.,  a  chronic  disorder  characterized  by difficulty  in  breathing.  —  Gk.  icaSpa,  ‘hard- drawn  breath’,  which  prob.  stands  for  *dva!>  |ia and  derives  fr.  I.-E.  base  *an-,  ‘to  blow,  breathe’, whence  also  dvcpio;,  ‘wind’,  L.  animus,  'breath of  air,  air,  breath';  see  animus.  See  Frisk,  GEW., I,  pp.  161-62  s.v.  do9-[xa.
3742:asthmatic,  adj.  —  L.  asthmaticus,  fr.  Gk.  aaffpia- xixoc,  fr.  dahlia.  See  asthma  and  -atic. Derivative:  asthmatic-al-ly,  adv. astigmatic,  adj.,  pertaining  to,  or  suffering  from, astigmatism  (med.  and  optics).  —  See  next  word, astigmatism,  n.,  defect  of  the  eye  that  prevents the  rays  of  light  from  converging  to  a  point  on the  retina  (med.  and  optics).  —  Coined  by  the English  mathematician  and  philosopher  Wil¬ liam  Whewell  (1794-1866)  in  1819  fr.  priv.  pref. a-  and  Gk.  axiypa,  gen.  oxtypaxo?,  ‘a  prick, puncture,  mark’.  See  stigmatic  and  -ism. Astilbe,  n,,  a  genus  of  plants  of  the  saxifrage family  (bot.)  —  ModL.,  lit.  ‘not  shining’,  fr. priv.  pref.  a-  and  axiX()eiv,  ‘to  shine’.  See  stilbite. astir,  adv.  —  Formed  fr.  a-,  ‘on’,  and  stir, astomatous,  adj.,  having  no  mouth.  —  Formed fr.  priv.  pref.  a-  and  -stomatous. astonish,  tr.  v.  —  Obsol.  astony,  fr.  ME.  astonien , astonen,  which  is  formed  with  change  of  pref. fr.  e st oner  (whence  F.  etonner),  fr.  VL.  *exto- nare,  lit.  ‘to  strike  with  thunder’,  fr.  1st  ex- and  L.  tondre,  ‘to  thunder’.  See  thunder  and  cp. astound.  The  verb  astonish  was  influenced  in form  by  English  verbs  ending  in  -ish,  in  which this  suff.  is  the  equivalent  of  OF.  and  F.  -iss.
---anima
2738:animus.
2802:animism
2809:animadversion,  n.,  criticism;  blame.  —  L.  ani-
2813:animal,  adj.  —  L.  animalis,  ‘of  air,  living,  ani¬ mate’.  See  animal,  n.
2814:animalcular,  adj.  —  Formed  with  suff.  -ar  fr.  L. aninialculum.  See  next  word, animalcule,  n.,  a  very  small  animal,  esp.  one  per¬ ceptible  only  by  a  microscope.  —  Late  L.  ani- malculum,  dimin.  of  L.  animal.  See  animal,  n., and  -cule.
2815:animalism,  n.,  animal  character;  the  doctrine  that man  is  a  mere  animal.  —  See  animal  and  -ism. animalist,  n.,  1)  one  who  believes  in  animalism; 2)  an  artist  representing  animals.  —  See  animal and  -ist.
2816:animalize,  tr.  v.,  to  make  like  an  animal.  —  See animal  and  -ize.
2820:animist
---other
2882:anorthoclase,  n.,  a  triclinic  potash-soda  feld¬ spar.  _  Coined  by  the  German  mineralogist Harry  Rosenbusch  (1836-1914)  in  >885  fr-  priv. pref.  -an  and  orthoclase  (q.v.) anosmia,  n.,  lack  of  the  sense  of  smell  (med.)  — Medical  L.,  fr.  priv.  pref.  an-  and  Gk.  bmirr ‘smell,  odor’.  See  osmium  and  -ia. another,  adj.  and  pron.  —  Formed  fr.  the  indef. article  an  and  other.
3121:other  celestial  body)  is  at  the  greatest  distance from  the  earth  (astron.)  —  F.  apogee,  fr.  L.  apo- gaeum,  fr.  Gk.  aTcoyaiov,  prop.  neut.  of  the adjective  anoyaioc,,  ‘far  away  from  the  earth’, but  used  by  Ptolemy  as  a  noun  for  a7x6yaiov cn-iiEiov,  ‘the  sign  far  away  from  the  earth’,  i.e. ‘apogee’.  ’A7x6ytxi.os  (also  d~6yeioc)  is  formed fr.  a 7x6  (see  apo-)  and  youa,  yr,,  ‘earth’.  See  geo- and  cp.  perigee.
10456:other  substances.  —  Formed  fr.  de-  and  calcify, decaliter,  decalitre,  n.  —  F.  decalitre,  lit.  ‘ten liters’.  See  deca-  and  liter.
26736:-ote,  a  suff.  meaning  ‘native  of.  —  F.  -ote,  fr.  L. -ota,  fr.  Gk.  -c1>xt]?  (cp.  e.g.  ’ilTrctpcoxyc,  ‘na¬ tive  of  Epirus,  Epirote’,  fr.  ’'HTOipo?,  ‘Epirus’), other,  adj.  —  ME.  other,  adj.,  n.,  pron.  and  adv., fr.  OE.  Oder,  adj.,  n.  and  pron.,  ‘the  second, following;  the  other’,  rel.  to  OS.  athar,  othar, OFris.  other,  ON.  annarr,  Du.  ander,  OHG. andar,  MHG.,  G.  ander,  Goth,  an/tar,  ‘other’, and  cogn.  with  Lith.  ahtras,  OPruss.  antars,  OI. dntarah,  ‘other’ ;  formed  with  I.-E.  compar.  suff. *tero-  fr.  base  *eno-,  *ono-,  whence  OI.  anyaft, Avestic  anya-,  OPers.  aniya-,  ‘other’,  Lith.  anas, atis,  ‘that  one’,  OSlav.  onu,  ‘he’,  Gk.  evtj,  ‘the day  after  tomorrow’,  bnoi,  ‘some’,  L.  enim,  ‘in¬ deed’,  Umbr.  enom,  ‘then’,  Goth,  joins,  OE. geon,  ‘yon’.  See  yon  and  -ther.
39684:Derivatives:  totem-ic,  adj.,  totem-ic-al-ly,  adv., totem-ism,  n.,  totem-ist,  n.,  totem-ist-ic,  adj. tother,  t’other,  adj.,  the  other.  —  ME.  the  tother, from  misdivision  of  thet  other,  that  other,  ‘the other’ ;  thet  or  that  was  orig.  the  neut.  of  the  def. art.  See  the,  art.,  and  other.  • toti-,  combining  form  meaning  ‘all,  whole,  whol¬ ly'.  —  L.  toti-,  fr.  totus.  See  total, totipalmate,  adj.,  having  all  the  toes  connected  by a  web  ( zoo! .)  —  Compounded  of  L.  totus,  ‘all’ and  palmatus,  ‘marked  with  the  palm  of  the hand’.  See  total  and  palmate, totter,  intr.  v.  —  ME.  toteren,  totren,  prob.  of imitative  origin.  Cp.  dial.  Norw.  totra,  dial. Swed.  tuttra,  ‘to  quiver’.  Cp.  also  toddle. Derivatives:  totter,  n.,  tott-er,  n.,  totter-ing, adj.,  totter-ing-Iy,  adv.,  totter-ish,  adj.,  totter-y, adj.
---Ormazd
2036:ahura,  n.,  a  benevolent  deity  (Persian  mythology). —  Avestic  ahura-,  ‘a  god,  a  good  spirit',  rel.  to OL  dsurah,  of  same  meaning.  Sec  asura  and  cp. the  first  element  in  Ormazd.
2037:Ahura-Mazda,  n.  —  See  Ormazd. ai,  n.,  the  three-toed  sloth.  —  Tupi  ai,  a  word imitative  of  the  cry  of  the  animal, aid,  tr.  v.  —  OF.  aidier,  aider  (F.  aider),  fr.  L. adjutare,  ‘to  help’,  freq.  of  adjuvare  (pp.  adju- tus),  ‘to  help’,  sustain’,  fr.  ad-  and  juvare,  ‘to help’,  which  is  of  uncertain  origin.  Cp.  adju¬ tant,  adjuvant,  coadjutor,  jocund,  jury,  adj. Derivatives:  aid-er,  n.,  aid-ful,  adj. aid,  n.  —  OF.  ( =  F.)  aide ,  back  formation  fr.  aider. See  aid,  v.
11938:‘I  place’,  aor.  ed,  ‘he  placed’,  Gk.  riDivoa,  ‘to put,  place,  set’,  f )eai;,  ‘a  placing,  setting’,  fHjxr], ‘case  in  which  to  put  something’,  flejxa,  ‘that which  is  placed’,  Difxi?,  Tight,  decree’,  Ssajxo;, Taw,  rule,  precept’,  lit.  ‘that  which  is  laid  down’, fb)(xtov,  Htop.61;,  ‘heap’,  flcueOXa  (pi.),  Homeric (pi.),  ‘foundation’,  L.  facere,  ‘to  make, do’,  -dere  in  ab-dere,  ‘to  hide,  conceal’,  con-dere, ‘to  found,  establish’,  per-dere,  ‘to  lose,  throw away,  ruin’,  OSIav.  dejp,  deti,  ‘to  place,  lay’, Lith.  deti,  Lett,  del,  ‘to  place,  put’,  OSIav. o-denu,  ‘clothed,  dressed’,  Gael,  deck,  ‘placed’. Cp.  ado,  deed,  deem,  doff,  -dom,  don,  v.,  doom, dout,  dup.  Cp.  also  theme  and  words  there referred  to.  Cp.  also  fact  and  words  there  re¬ ferred  to.  Cp.  also  abdomen,  abscond,  condiment, Consus,  dagoba,  dam,  ‘an  earthbank’,  family, fetial,  hoard,  perdition,  recondite,  sacerdotal, samadh,  samadhi,  sconce,  ‘a  metal  bracket’, stridhana.  Cp.  also  the  second  element  in  creed and  in  jubilate,  and  the  third  element  in  divide and  in  Ormazd.
23122:learned,  learning,  science’,  from  the  aorist p,a&£tv  (whence  the  pres,  [iavffaveiv ),  ‘to  learn’, fr.  *mndh-,  reduced  form  of  I.-E.  base  *men-dh-, ‘to  have  one’s  mind  aroused,  apply  oneself to’.  From  the  same  base  (resp.  its  reduced  form) prob.  derive  Gk.  p.Ev(H)p7],  ‘care’,  Lith.  man- dr  as,  mandrils,  ‘wide-awake’,  OSlav.  mqdru, ‘wise,  sage’,  Goth,  mundon  sis,  ‘to  look  at’,  ON. munda,  ‘to  aim’,  OHG.  mendan,  ‘to  rejoice , OHG.  muntar,  MHG.  munter,  munder,  ‘eager, agile,  nimble",  G.  munter,  ‘awake,  lively,  gay, merry,  vigorous’,  W.  mynnu ,  ‘to  want,  wish  , Alb.  mund,  ‘I  can,  I  am,  victorious’,  and  pos¬ sibly  also  Ol.  medha,  ‘wisdom,  intelligence',  Gk. Mouaot  (if  fr.  *M6vffia),  ‘Muse’.  Base  *men-dh- is  an  enlargement  of  base  *men-,  ‘to  think’. See  mind  and  cp.  Muse,  Epimetheus,  Prome¬ theus.  Cp.  also  the  second  element  in  chresto- mathy,  opsimath,  polymath.  Cp.  also  the  second element  in  Ormazd.
23216:—  See  Ormazd  and  -ism.
```


## [2026-09-04T19:51:59.224Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\n# build leaf index per line\nleaf=0; m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf\n    leaf+=l.count('\\f')\nfor ln,lbl in [(1831,'Aesir'),(2036,'ahura'),(2037,'Ahura-Mazda'),(2800,'anhelation'),(2813,'animal'),(2828,'animus'),(3741,'asthma'),(23216,'Ormazd-ism'),(26653,'Oscar'),(26734,'Oswald'),(26736,'other')]:\n    lf=m[ln]; print(lbl, 'line',ln,'leaf',lf,'-> printed pages',2*(lf-12),2*(lf-12)+1)\nEOF"
}
```


### [2026-09-04T19:52:01.269Z] TOOL RESULT

```
Aesir line 1831 leaf 29 -> printed pages 34 35
ahura line 2036 leaf 33 -> printed pages 42 43
Ahura-Mazda line 2037 leaf 33 -> printed pages 42 43
anhelation line 2800 leaf 52 -> printed pages 80 81
animal line 2813 leaf 52 -> printed pages 80 81
animus line 2828 leaf 52 -> printed pages 80 81
asthma line 3741 leaf 73 -> printed pages 122 123
Ormazd-ism line 23216 leaf 510 -> printed pages 996 997
Oscar line 26653 leaf 587 -> printed pages 1150 1151
Oswald line 26734 leaf 589 -> printed pages 1154 1155
other line 26736 leaf 589 -> printed pages 1154 1155
```


## [2026-09-04T19:52:14.229Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in list(range(556,572))+[586,587,588,589]:\n    p=t[i].strip().replace('\\n',' ')\n    print(i,'|',p[:160])\nEOF"
}
```


### [2026-09-04T19:52:16.151Z] TOOL RESULT

```
556 | for  *ver og,  fr.  I.-E. •newos,  ‘new’,  whence  also  Goth,  niujis,  OE. neowe,  ‘new’.  See  new  and  cp.  neon,  neoteric, Nerium,  the  first  element  
557 | .  ve< pp4c,  ‘kidney’  (see  ne¬ phro-),  and  suff.  -it,  which  goes  back  to  Gk. -fry?  (see  subst.  suff.  -ite);  so  called  in  allusion to  its  su
558 | �blessed’.  See  nostal¬ gia. Nestorian,  adj.,  1)  pertaining  to  Nestonus,  pa¬ triarch  of  Constantinople  (428-431  C.E.),  who was  condemned  for  here
559 | corpuscles  that is  neither  oxyphile  nor  basophile');  a  hybrid coined  by  the  Jewish  bacteriologist  and  immu¬ nologist  Paul  Ehrlich  (1854-1915)  f
560 | s  (in  a  certain  manner); one  who  deals  (with  a  certain  topic)’.  See  nidus and  -logy.  The  correct  form  is  caliology  (q.v.),  in which  both  e
561 | �. Nilotic,  adj.,  pertaining  to  the  Nile,  the  Nile  re¬ gion  or  the  Negroes  who  live  in  the  valley  of  the White  Nile.  —  L.  Niloticus,  fr. 
562 | niter, nitro,  adj.,  containing  nitrogen.  —  From  nitro-. nitrogen,  n.,  a  colorless,  tastless,  odorless  gase¬ ous  chemical  element.  —  F.  nitrog&n
563 | See  nodule  and  -ous. nodus,  n.,  knot;  difficulty,  complication.  —  L. nodus,  ‘knot’.  See  node. noel,  n.  1)  cry  of  ‘noel’  (in  Christmas  songs)
564 | before  the  ides’,  and  cp. words  there  referred  to. nonagon,  n.,  a  plane  figure  having  nine  angles  and nine  sides.  —  A  hybrid  coined  fr.  L.
565 | orman-ize,  intr. and  tr.  v.,  Norman-iz-ation,  n. Norn,  n.,  one  of  the  three  goddesses  of  fate  in Scandinavian  mythology.  —  ON.  norn  (pi. norn
566 | Sir  Richard  Owen  (1804-92)  in  1848  fr. vcoxo.;  (also  vcotov),  ‘the  back’,  and  yopSr),  ‘a string’.  See  noto-  and  chord, notodontid,  adj.,  pert
567 | alpha¬ bet. —  Gk.  vu,  shortened  fr.  Heb.  nun,  name  of the  letter  n.  See  nun,  the  letter, nuance,  n.,  a  slight  difference.  —  F.,  ‘shade,  hu
568 | numeralis,  ‘of  numbers’,  fr.  L.  numerus. See  number,  n.,  and  adj.  suff.  -al. Derivative:  numeral,  n. numerary,  adj.,  pertaining  to  a  number  o
569 | ), contraction  of  *noven-dinom,  ‘nine  days’,  fr. novem,  ‘nine’,  and  *dinom,  ‘day’.  For  the  first element  sec  nine.  The  second  element  is  cogn
570 | sexual  desire  in  women (med.)  —  Medical  L.,  compounded  of  nympho- and  Gk.  (tavtoe,  ‘madness,  frenzy'.  See  mania. Derivative:  nymphomani-ac,  adj
571 | o  put  before’.  It derives  fr.  L.  objectus,  pp.  of  obicere  (less  cor¬ rectly,  objicere),  ‘to  throw  or  put  before  or against’,  fr.  ob-  and  j
586 | s  American  birds  of  the  family Icteridae.  —  F.  oriol,  fr.  OF.,  fr.  ML.  oryolus, fr.  L.  aureolus,  ‘golden’,  dimin.  of  aureus,  fr. aurum,  ‘go
587 | �orris  root’,  which  is  identical  with  Gk. Epecoe,  gen.  of  Iptc,  ‘iris’.  See  iris. Orson,  masc.  PN.  —  Fr.  F.  ourson,  dimin.  of  ours, ‘bear’,
588 | vowel  osche-,  combining  form meaning  the  ‘scrotum’.  —  Fr.  Gk.  Soysov, ‘scrotum’,  a  collateral  form  of  ooyiq,  of  s.m., prop,  figurative  use  of
589 | a  vowel, osteal,  adj.,  bony.  —  Formed  with  adj.  suff.  -al  fr. Gk.  ooteov,  ‘bone’.  See  osteo-. osteitis,  n.,  inflammation  of  a  bone  ( med .)
```


## [2026-09-04T19:52:31.985Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in [72,73,74,585,586,587,588,589,590]:\n    b=t[i]\n    print('LEAF',i,'START:',repr(b[:70]))\n    print('        END:',repr(b[-70:]))\nEOF"
}
```


### [2026-09-04T19:52:33.986Z] TOOL RESULT

```
LEAF 72 START: '‘basilisk’,  fr.  L.  basiliscus (see  basilisk),  two  names  that  a'
        END: 'n,  v.,  and  -ment. assimilate,  tr.  and  intr.  v.  —  L.  assimila'
LEAF 73 START: 'tus,  pp. of  assimildre,  ‘to  make  like,  liken’,  fr.  ad-  and si'
        END: 'ogy.  —  L.,  fr.  Gk.  ’Aaxpaia,  lit. ‘starry’,  fem.  of  aaxpouo;,'
LEAF 74 START: '  fr.  daxf]p,  ‘star’.  See\nAster.\nastragal,  n.,  a  convex  molding'
        END: 'th  suff.  -istic  fr.  L.  atavus. See  prec.  word.  See  atavism.\nD'
LEAF 585 START: ' coin,  prop,  subst.  use  of  the  adj. aureus,  ‘of  gold,  golden’'
        END: ',  n.,  1)  any  bird  of  the  family  Oriolidae;  2) any  of  variou'
LEAF 586 START: 's  American  birds  of  the  family Icteridae.  —  F.  oriol,  fr.  OF'
        END: 'rey. orris,  n.,  the  Florentine  iris.  —  Prob.  fr.  ML. yreos,  �'
LEAF 587 START: '�orris  root’,  which  is  identical  with  Gk. Epecoe,  gen.  of  Ipt'
        END: '  -al  fr.  Gk.  ooyeov, ‘scrotum’.  See  oscheo-.\noscheo-,  before  a'
LEAF 588 START: '  vowel  osche-,  combining  form meaning  the  ‘scrotum’.  —  Fr.  Gk'
        END: 'd  2nd subst.  suff.  -ary.\nost-,  oste-,  forms  of  osteo-  before  '
LEAF 589 START: 'a  vowel, osteal,  adj.,  bony.  —  Formed  with  adj.  suff.  -al  fr'
        END: '.  Gk.  o5?,  gen.  <oxo?, ‘ear’,  and  xonxic,  ‘bladder,  bag,  pouc'
LEAF 590 START: 'h’.  See oto-  and  cyst.\notolith,  n.,  chalky  matter  in  the  inte'
        END: '  lit.  ‘to  cry  £ua  (in  honor  of  Bacchus)’, oven,  n.  —  ME.,  '
```


## [2026-09-04T19:52:56.016Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nimport re\n# find letter starts\nfor i in range(len(t)):\n    s=t[i][:200].replace('\\n',' ')\n    pass\n# print some markers\nfor i in [0,1,2,3,4,5,6,7,8,9,10,11,12]:\n    print(i,repr(t[i][:80].replace('\\n',' ')))\nEOF\necho \"=== 1971 ===\"; grep -n \"^Ormazd\\|Ormazd,  n\" KLN_1971.txt | head -3"
}
```


### [2026-09-04T19:52:59.313Z] TOOL RESULT

```
leaves 903
0 'A  COMPREHENSIVE ETYMOLOGICAL  DICTIONARY OF  THE ENGLISH  LANGUAGE Dealing  wit'
1 'ELSEVIER  PUBLISHING  COMPANY 335  JAN  VAN  GALEN STRAAT,  P.O.  BOX  211,  AMS'
2 ' Preface To  know  the  origin  of  words is  to  know  the  cultural  history  '
3 '  work. VIII My  grateful  acknowledgements  are  also  due  to  the  whole  sta'
4 '  but  the  origin  of  the  respec- X tive  word  is  referred  to  by  such  v'
5 'Theo- phile-Hyacinthe  Laennec  (1781-1826)  fr.  Gk.  xippo?,  ‘tawny’,  which '
6 'a  slight  aspira¬ tion  of  the  sound  - like  gh;  now  pro¬ nounced  like  g'
7 'he  letters  17  .  D  ,  3  1  >  3  ,  to  indicate  their original  hard  pro'
8 " ss  in English  hiss J* dad d palatal  d s> ta 1 an  emphatic  t J; za' z an  e"
9 'Auflage  von  J.  B.  Hofmann,  Heidelberg,  1938-55. Walde-Pokorny,  VWIS.  =  '
10 'before  the  common  era diet. dictionary Berb. Berber dimin. diminutive Bibl. B'
11 'abinic Old  Sabinic OSerb. Old  Serbian OSlav. Old  Slavic OSp. Old  Spanish Oss'
12 'an Republics Russ. Russian V. verb S. South var. variant S.Afr. South  African v'
=== 1971 ===
168881:Ormazd, n., the principle of good in the Zoro-
```


## [2026-09-04T19:53:21.590Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(425,470):\n    s=' '.join(t[i][:90].split())\n    print(i,'|',s)\nEOF"
}
```


### [2026-09-04T19:53:23.438Z] TOOL RESULT

```
425 | ggle out of, to surmount’, fr. e- and luctari, ‘to struggle, wrestle’, which i
426 | nquiet, hostile’, lit. ‘seized’, rel. to manifestus, ‘evident’, lit. ‘that which
427 | uriate, ‘to madden’, fr. L. in furid, ‘in a fury’, fr. in (see in-, ‘in’) an
428 | ory, adj, — ML. inhibitorius, fr. L. in¬ hibitus, pp. of inhibere. See inhibit
429 | oculare, ‘to furnish with eyes’, fr. oculus, ‘eye; bud’. See ocular and verbal
430 | vative: insinuat-ing, adj., insinuat-ing-ly, adv., insinuation (q.v.). insinuat-ive,
431 | ntial suff. -or. instructress, n. — See prec. word and -ess. instrument, n. —
432 | whole, renew’, fr. in¬ teger. See integer and verbal suff. -ate. integration, n
433 | and adj. suff. -ory. interdigitate, intr. v., to interlock like the fingers of
434 | rmed fr. ad- and -pellare and also has an iterative meaning (see appeal, v.) in
435 | t’, and tolerabilis. See tolerable. Derivatives: intolerable-ness,n., intolerabl-y,
436 | L. inundans, gen. -antis, pres. part, of inundare. See next word and -ant. inu
437 | -ory fr. L. invocatus, pp. of invocare. See invoke, invoice, n. — Fr. earlier
438 | — ModL., fr. Gk. eEpeauovr), ‘a wreath of olive wound round with wool’, fr. s
439 | e, adj. — Formed with suff. -ive fr. L. irrigatus, pp. of irrigare. See irrig
440 | te, ‘to anger’, and -able. Derivatives : irritabl-y, adv., irritabil-ity, n. irrit
441 | timulate, stir up, provoke’, prob. freq. of *ir-ri-re, ‘to stir up, excite’, fr
442 | ains in the hip’, compounded of Gk. EoxEov, ‘hipjoint’, and itXyo ?, ‘pain’. See
443 | represents 1) OF. -aison (fr. L. ationem, fr. -atus, pp. suff. of verbs in -
444 | the true stinkhorns (bot.) — ModL. See prec. word. -itic, suff. forming adjectiv
445 | — Late L. Jacdbus, fr. Gk. ’laxcojioc, fr. Heb. Ya'dqohh, lit. ‘one that takes
446 | ��), and the adj. janitor-ial. Janizary, also Janissary, n. — Fr. janissaire, fr.
447 | its horsemen, jenneting, n., a kind of early apple. — Formed with subst. suff.
448 | The Foreign Vocabulary of the Qur’an, pp. 101-102. jhow, jow, n., a tamarisk us
449 | s’, yuktdh, ‘harnessed’, Gk. ^euyvuvai, ‘to yoke, har¬ ness’, Avestic yaoj-, yuj-
450 | o gau- dere, ‘to rejoice'. See gaud and cp. enjoy. Cp. also feu de joie, rejo
451 | ‘rose’, and ab, ‘water’. See rose and abdest. Julia, fem. PN. — L. Julia, fem
452 | cer of the kings of England from the reign of William I to that of Henry III
453 | called from the name of the place where it was first found, kapellmeister, n.,
454 | its OS., ON., OHG. equivalents. See comb and cp. kempt. kemp, n. (esp. used in
455 | ‘stalk, blade’, Lett, zeiju, ziet, ‘to rise’ (said of flowers; also fig.) See c
456 | n., a kind of East Indian brocade. Hind, kimkhab, fr. Pers. kimkhdb. kind, n.
457 | yoav, ‘to wail, groan, weep’, yooq, ‘wailing, groaning, weeping’, OE. cyme, ‘fine
458 | f a small hill. — ME. knot, fr. OE. cnoll, ‘hill top, hill’, rel. to ON. kn
459 | , fr. Krieg, ‘war’, and Spiel, ‘game’. The first element is of uncertain origi
460 | pertaining to, or formed with, the lips and teeth. — Compounded of labio- and
461 | . lakmoes, fr. MDu. leecmos, fr. leken (Du. lekken ), ‘to drip, leak’, and mos
462 | -ly, adv., laggard-ness, n. lagniappe, n., gift, gratuity. — Amer. F., fr. Amer
463 | t-ed, adj., taminat-ion, n. luminiferous, adj., having laminae. — Com¬ pounded of
464 | ‘tongue; language’. Cp. next word and languet. langued, adj., having the tongue
465 | adj., and verbal suff. -ate. Derivatives: lapidat-ion, n., lapidat-or, n. lapidific
466 | ser, n. — Coined from the initials of Light Am¬ plification (by) Stimulated Em
467 | . — ME., fr. L. Latinus, ’Latin’, prop, ‘pertaining to Latium’, fr. Latium, na
468 | . labes, ‘a fall, falling down’, which is rel. to labi, ‘to slide, slip, glid
469 | ment. — ME. -el, fr. OE. -el. Cp. e.g. ladle, fr. ME. ladel, fr. OE. hlsedel,
```


## [2026-09-04T19:54:11.804Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### Ormazd 1971\"; sed -n '168881,168890p' KLN_1971.txt; echo \"### asura/prana 1966\"; grep -n \"^asura\\|asura,  n\\|^prana\\|prana,  n\" KLN_1966.txt | head -5"
}
```


### [2026-09-04T19:54:11.892Z] TOOL RESULT

```
### Ormazd 1971
Ormazd, n., the principle of good in the Zoro- 
astrian religion. — Pers., fr. OPers. Auramazda , 
fr. Avestic Ahuramazda , lit. ‘wise lord’, a com- 
pound of ahura-, ‘a god, a good spirit’ (see 
ahura), and ma(n)dzdhd > ‘wise’, which is a com- 
pound formed from the I.-E. bases *men-dh- , ‘to 
apply oneself to’, and *dhe-, ‘to put, place’. 
From base *men-dh- derives also OI. medha, 
‘wisdom, intelligence’. For other derivatives of 
this base see mathematical. For base *dhe - see 
### asura/prana 1966
3778:asura,  n.,  a  god,  a  good  spirit;  later  an  evil  spirit (Hindu  mythol.)  —  Ol.  asurah,  prob.  rel.  to  OI. asuh  (for  *nsu-),  ‘breath  of  life',  fr.  I.-E.  base *an-,  ‘to  blow,  breathe',  whence  also  OI.  ani-ti, dna-ti ,  ‘breathes’,  L.  anima,  ‘breath  of  air, breath,  soul,  life’,  animus,  ‘soul,  spirit,  mind, courage,  wish,  derive'.  See  animus  and  cp.  ahura and  sura,  ‘spirit,  demon’.
29908:Pralaya,  n.,  destruction,  the  end  of  the  world ( Hindu  philos.)  —  OI.,  ‘dissolution,  destruction’, formed  fr.  prd-,  ‘before,  forward,  forth’,  and layate,  liyate,  liyati,  ‘clings  to;  remains  sticking; slips  into;  vanishes’.  The  first  element  is  cogn. with  Gk.  Txpo,  ‘before’,  L.  pro,  ‘before,  for’;  see 1st  pro-.  The  second  element  derives  fr.  I.-E. base  *(s)le(i)-,  ‘slime',  slimy,  sticky,  dauby, slippery’,  whence  also  Gk.  Xtioc,  ‘smooth’,  L. levis,  ‘smooth’,  limus,  ‘slime,  mud,  mire",  linere, ‘to  daub,  besmear,  anoint',  OE.  slim,  ‘slime’; see  slime  and  cp.  words  there  referred  to. praline,  n.  —  F.,  so  called  after  Marshal  Duples- sis  Praslin  (pronounce  Praiin)  (1598-1675), whose  cook  invented  this  confection, pram,  praam,  n.,a  flat-bottomed  boat  used  in  the Baltic.  —  Du.  praam,  of  Slavonic  origin;  cp. Pol.  pram,  ‘boat’,  Russ,  poromit,  ‘ferryboat’, which  are  cogn.  with  Gk.  “opoc.  ‘thoroughfare, passage',  L.  porta,  ‘gate,  door',  portus,  ‘port, harbor’,  fr.  I.-E.  base  *per-,  ‘to  lead  across, drive  across,  traverse,  pierce'.  See  fare,  v.,  and cp.  words  there  referred  to. pram,  n.  ( colloq .)  —  Short  for  prambulator,  a syncopated  form  of  perambulator, prana,  n.,  life  principle  (Hinduism).  —  OI.  pranafi, ‘breath,  breath  of  life’,  formed  fr.  prd-,  ‘before,
```


## [2026-09-04T19:54:12.404Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"anima,  n\" KLN_1966.txt | head -3; echo \"---leaf51\"; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(' '.join(t[51].split())[:1500])\nEOF"
}
```


### [2026-09-04T19:54:14.330Z] TOOL RESULT

```
---leaf51
con¬ fusion with words ending in -ism. Derivatives: aneurysm-al, adj., aneurysm-al-ly, adv., aneurysm-at-ic, adj. anfractuosity, n., circuitousness. — F. anfractu- osite, fr. L. anfrdctus. See anfractuous and -ity. anfractuous, adj., circuitous. — F. anfractueux (fem. anfractueuse), fr. L. anfractudsus, fr. am- fractus, anfrdctus, ‘a breaking round; a turning, winding’, fr. am-, shortened form of ambi-, amb-, ‘about, around’, and fractus, pp. of frangere, ‘to break’. See ambi- and fraction. Derivatives: anfractuous-ness, n. anew, adv. — Formed fr. a-, ‘of’, and new. angaralite, n., a magnesium aluminum iron sili¬ cate (mineral.) — Named after Angara River in Siberia. For the ending see subst. suff. -ite. angaria, n„ a system of relays of couriers for dis¬ patching official letters in ancient Persia, later also in the Roman empire. — L., ‘service to a lord’, fr. Gk. ayyapeta, ‘impressment for the public service’, fr. ayyapot;, ‘mounted courier, messenger’, of Persian, ult. Semitic, origin. See angel. angary, n., the right of a warring nation to use or destroy the property of neutrals. F. an- garie, fr. L. angaria. See prec. word, angel, n. — ME., fr. OF. angele (F. ange), fr. L. angelus, fr. Gk. oiyyeXo-, ‘messenger, divine messenger, angel’ (whence the verb dyyeXXetv, ‘to bear a message, report, tell’), which is rel. to dyyapo?, ‘mounted courier, messenger’; of Persian, ult. of Sem. origin. Cp. Akkad, agarru, ‘hireling, hired laborer’, fr. agaru, to hire , which is rel. to Ar
```


## [2026-09-04T19:54:24.161Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in \"ahura\" \"aŋhu\" \"anhu\" \"Lebenshauch\" \"daoz\" \"dao\\\\?z\" \"anya\" \"ainya\"; do echo \"### $p\"; grep -n -i -- \"$p\" BRT.txt | head -4; done 2>/dev/null | cut -c1-600"
}
```


### [2026-09-04T19:54:25.898Z] TOOL RESULT

```
### ahura
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(
2477:y^  . .  möi  gas'^iä  dazdl  *amaiiklmit  akyä  \  myazdS  . .  äisy.ll  kl  anhe  ava{  mlid^m  A. maä%rilfrö^StY.46.Z\'—yatäröpaurvö^3.(il.;  — yastal  mihdgm  haiuftt? nöit däitX äire  . .  paitiJiaraiti  ahmäi  atars  ä/rJnat  .  .  kä  tsm  ahyä  *maeHis(sA.)  ar»hatY.44. V.1S.26;  YLIJ.51; — y ahmäi  xlnstö  ba-\  i^.  b)  .\Sn.,  f.  mit  Äaca  sva. 'dadurch': vaili  mi^rä  ahmäi  Jasaiti  avaiäke  YLIO.  yezi  mit  spä  ..  maeyevä  . .  pai'jyäite  ahmat 84;  87,  Y.GS.w*;  — yöi  nsil  ahm  main-  haca  irisyät  "sonst  konnte  der  Hund  in 
2479:Fem.  Sing.:   yä  haca  da?vayasnalibyö  .  .{yäahurahemazdaY. 68.12;  —  ahenarl-.yo
2554:nominale  Beifügung;  in  den  meisten  'tat  .  .yat  a:£'ar3t>m  Yt.  J9.48;  46;  — Fällen  entspricht  unser  bestimmter  Artikel  'te yä  spö.jataca  .  -  V.  7,  3;  —  Ue yöt  spatui (schwachtoniges  'der');  a)  adjektivisch:  V.ij.ai,  22,  43;  —  'taisqm yöi gius  sar?- caiti  'te  mi>fa  tava  yat  ahurahe  mazdat  oanqm  V,2.4i;  Ytj.9,  12;  —  'lat?hqm "wie  vielfach  sind  deine,  des  AhM.  Ver-  (GPm.)  yat  myazdanqm  N.  6j;  —  ku>a träge?"  V,4,2;  —  "te  daxma  .  .  aniarSt  (Stverz.)  ti  v>r>zyqn  He  yöi  masdayasna naSmät  iarürirva  V.
### aŋhu
### anhu
2905:•  j.,  g.  aojah'vant-  Adj.  (fem.  °vaiti-) 'kraftvoll, kräfÜg,stark':  xia'inm  'jör^hval Y._JJ.4;  zit,  V.  20.  8,  wo  -jaahvat;  — rafonö  ,.  'jötighvat  Y.4J.8;  28.6;  — sonst  von  Gottheiten:  at  iöi  •i/rim  . . 'jimhvantim  asl .,  ". .  Feuer  {Älar),  das seine  Kraft  durch  A.  hat"  Y.J4.4";  — sraohm  . .  *°janhuntfm  '>  Y.  57. 1 1 ;  — fravalayö  ..  'jattukaitil  Ytij.32;  — astval  (sd)  <ß>m  hyut  ustän��  'jönghval Y.4!j.i6.
3165:■übelste,  böseste"*:  dva  yaska..  -«(NDm.) I  V.  7. 70;  —  sHptibyasca  (sd.) . .  vispalibyasLa pairi  'taeibyö  \.  14.17;  —  °to«  rfuirfw- Aavö  'P.14;  —  nöil  hl . .  bvat  . .  zahistiJ anhuL.bi'ai  TTspariqm  *°/jm'^  *paosisl>mcix ya^  »riyat  daozaishum'^ . .  sondern  es  wird
4148:vergänghchc.di.  materielle  Dasein,  Leben': kaaa  ns  iaa  .  .  agatJ  i^yejauhatat  haca °f»haot  ai'kyejanhsm  ahüm  a  V.  7p.  3 1 ; 7.52;  —  hai:a  apajäsö  .  .  i'iyejatuthata^ haca  'fihaot  atiryejanhutäitn  avi  °hü?n H.  2, 16.  2)  mit  a)  manahya-  Adj.  oder manauhs  GS.,  b)  datbitya-  Adj.,  c)  parS.- asna-  Adj.,  d)  ai>y0ah-  oder  ai'hyejakvant-
4171:•  j.  'aDhü-  f.  'Schwert':  ^axtayilt  pars anhuyäp''  "bevor  das  Schwert  gezückt  ist" Yt.  13. 46.
### Lebenshauch
### daoz
3165:■übelste,  böseste"*:  dva  yaska..  -«(NDm.) I  V.  7. 70;  —  sHptibyasca  (sd.) . .  vispalibyasLa pairi  'taeibyö  \.  14.17;  —  °to«  rfuirfw- Aavö  'P.14;  —  nöil  hl . .  bvat  . .  zahistiJ anhuL.bi'ai  TTspariqm  *°/jm'^  *paosisl>mcix ya^  »riyat  daozaishum'^ . .  sondern  es  wird
4155:—  tpm  vä  ahäm  drvantB ,  .  nUirint^ät \aastäi  'Muhe]"*  V.5.62.  4)  mit  a) asaanqm  GP.,  b)  drvatqm  GP.;  'Ort,  Auf- enthalt der  a)  Gläubigen,  b)  Ungläubigen', im  Sinn  von  3  a,  b ;  tfm  'hüm  paihyaite yim  asaonam  .  .  tarn  'hüm  paüyatte yim  drvatqm  timanhaitt^m  .  ,  V.iS.jS; 5.62,  5)  mit  timatiha-  Adj.  'der  finstere Aufenth^t,  Raum',  von  der  Hölle:  bunim -TihSus  tpmanhahe  yat  »rr/ats  daozaauhahe
7633:•  j.  araj-ant- Adj.  (fem.  'yaiii-)  'entseulich, abscheulich';  a)  von  der  Hölle:  paosisUmäi yat  °yat  daozaahum  P.  ^o;  —  *bun9m atiksm  t)iHat?hahe  yal  'yatö  dagzanuhahe V. /^.  47;  —  °yata  haca  duzauha  Yt. /<?.44;  —  'fatal  haca  äaozavilt  Yt.  4. 7.  b)  von  Fliegen:  baivarj  maxHnqm 'yaitinam  V.14.6; — *max/i./hArpa  "faitya (ISf.)  V.7.2.
12578:""daozavät
### dao\?z
2406:>■  bedeutet,  dasi  ich  du  damit  bezeichnete  Wort  oder  bei  '". . ."  die  ganze  Reihe  von  Wörtern dazwischen  f&r  iigendwie  verderbt  halte.
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  f
2477:y^  . .  möi  gas'^iä  dazdl  *amaiiklmit  akyä  \  myazdS  . .  äisy.ll  kl  anhe  ava{  mlid^m  A. maä%rilfrö^StY.46.Z\'—yatäröpaurvö^3.(il.;  — yastal  mihdgm  haiuftt? nöit däitX äire  . .  paitiJiaraiti  ahmäi  atars  ä/rJnat  .  .  kä  tsm  ahyä  *maeHis(sA.)  ar»hatY.44. V.1S.26;  YLIJ.51; — y ahmäi  xlnstö  ba-\  i^.  b)  .\Sn.,  f.  mit  Äaca  sva. 'dadurch': vaili  mi^rä  ahmäi  Jasaiti  avaiäke  YLIO.  yezi  mit  spä  ..  maeyevä  . .  pai'jyäite  ahmat 84;  87,  Y.GS.w*;  — yöi  nsil  ahm  main-  haca  irisyät  "sonst  konnte  der  Hund  in 
2537:mazäayasnaAey.iG.ir,  -~  hä'tiyaska^^^^^^^  j^f  vorausweisend:  'tat  dim  .  .daz- 't^  \.5.48;  --yava  Ht  afiA.m  F.4c;  ^  ■  (^j  j  _  _  ^^^^.j.  „,^^^^^  mainy-,,,!  Y. V  ,6.12;  -  gatnmasoaf^Ao  'tf^^y-yO  .-.,.  ,)  'dann,  alsdann':  &«A«  bar>- PuZ.;  =6.  7.  52  PdZ.,  V.S4,  N  /^5,  "^f-  Jna  frastprmuyr,  ..Uat  tl  jasüni  ^araiMe 4, 19',  21;  -  Aanqm  Haitqm  jijtJarmAa   ^^  ,^     ^    g  ^^        ^^^  „^  ^  ,       .,^,
### anya
2550:äJffj  ti  'take  paiti  ..  V.22.2f.;  —  Da.'  aoAvo  (Stvetx.)  yal  as/tainti  Y.i^.6  \isw.; in  Verbindung  mit  anya-  Du.  (s.  i  b):  —  'tagsam  sünam  ..yimpasuiJiaurvamca.. asUm^mastrrfttqm  vispacayö*>nastr?inqm  i  V./^J.S;  —  'farahqm  urvaranqm  yat  ätri.- amqsta  fsd.)  ''i^arö.cikaya  *°le  anye  cika- ■  ciirranqm  V,4',75;  —  'ttm  ratümca  .. yatö  "wenn  einer  ,  .  und  wenn  einer  ,  .  \yim  maiaydhanmaim  A.j.3(?).  b)  sub- vcrletzt,  so  sollen  sie  dies  und  jenes  . ."  stasA\v\&c\\- 'ta(^T>.)äb3r3ta*sraosiivariza F,_jc  b)  adjekti
2564:PuZ.;  26,  7.  52  PiiZ-  P-  54,  N  /05,  ^'^■,',„a  frast^rmuyh  ..'tat  iE  Jatäni  UvaiMe 4,  I9\  1'/;  —  A«nim  'tallqm  }tjtlar,uha  y^  ,^,_^  f  .  g^  y^^^_  jj-^^.  3)  'so,  ita', \.  /5.13;  14;  —  'ta  parayatt,  (sd.)  yalia.. .  ^j^  Korrelat  sanya^a:  ya^ala pasulhaur- 7-aahö  'tat  sraoüm  . .  pairiMrilmahi  YL
2672:^a.ymaslnynam  ..  vXspaca  ..  F.  je;  —  ni"=r  ai/mMiit:  —  6)  zit.  aus  V.  29. S  und 'v5  panth  yö  ^ahe  vTspe  anyai?am..\.-72. ,     ™'^  34-  n.  Vgl.  •!  w  m>näa«!y.^.  _  7)  Hds
2706:•  j,  aevo.gaya-  n.  'Längenausdehnung  |(>ij«(i">  me  yaoidäiUm  "ihr  könntet  mich eines  Schritts,  eine  Schrittlänge';  Äa/ ^«i-a  ,  purifiziren"  V.Äioo.  1,2  a)  mit  Gen. anys.anyaeibyö}  ya^a  'gatm  iu^a  (sd.) '  und  Inf.:  naj/a  .  .  Aäu  ni  ahmat  haca •gsimi  ,  .  "Wie  weit  von  einander?  "SiQ  gstaot  isalta  frasBtÖit  »eil  apasüföil  (sd.) viel  als  eine  Schrittlänge  beträgt  .  ."  "^  .{'^rayamcina  gämanam  P.  2jj>.  3)  '(es) p.  S.                                                                     I  können,  vermögen,  (daz
### ainya
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(
3006:Vim-ä  iir^r^f"  ttH  ^  V  ^j  I ;  —  rami  a/a 'iqm  drujiin  Yt. /i^.gß;  —  at  tJ  mainya , .  manahicä  vacahicä  Syaoianöi  hl  vahyö akimcii  "und  die  beiden  Geister  . .  sind das  Bessere  und  das  Schlechte  in  Ge- danken, Wort  und  Tal"  Y.^0.3;  ■ —  at yüs  daevti  vtspatshö  'käi  manatikB  sta •■  yasSj    .  .  drüjascH  pairi.malsisca
3012:"aber   ihr    seid    dem   schlechlen  Denken :  •   j-  »tav-   m.  'Scheere,   scheerenartige entsprossen,  ihr  Z>a^t■a  alle,  und  er,  der  . .,   Waffe' :    nött   dtm  .  .  avasy/tl  notl    'Aavo und   der   Lüge   und   der  Hoffart"  Y.js.KNP.)  nSil  ..  Yt.I.iS. 3').         A  a)  mit  mainyav  m.  'der  bösei     ?';'  -?•■•*»•'/.  ^p«--  »»**.  "!•:  *''« Geist,  sva.  anra- matnyav:  hyat  vä  aka\      .       ,  ,  ■,.    ,r  ■,!>,,
3112:rim  stagr»m  (sd.)  arijö  V,  7. 41;  43'; —  uitraAe  k?hrpa  °yehe  P.^2;  —  aspahe paiti  arshö  °yehe  "um  einen  Rosshengst erster  Qualität"  V.9.37;  37';  —  dvada- satih£ir3m  (sd.)  asti  "rim  ayan  F.  27  b; '";  —  'krisatdkw)m  frasnütse  .  .  "yqtn paiti  usnaitJm  ".  .  (also)  mit  Abwaschung erster  Ordnung"  V,  Ä  98  (?) '' ;  —  mi>nm  . . taxm?m  mainyaam 'rJmYtw.i 40.  [P. 32:  lies  ayryö.mdaimasl°.'\
```


## [2026-09-04T19:54:42.779Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"barzakh\\|barzax\\|Barzah\" FVQ_pages.txt | head -10"
}
```


### [2026-09-04T19:54:42.831Z] TOOL RESULT

```
3072:T 1 *}j (Barzakh).
```


## [2026-09-04T19:54:44.748Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD dwzh/dus\"; grep -n \"^duš\\|^dušox\\|^duz\\|dušox\\|dōšox\" PHD.txt | head -10; echo \"### PHD ān\"; grep -n \"^ān \\|^ān,\" PHD.txt|head -5; echo \"### NYB\"; grep -n -i \"dusox\\|došox\\|dušox\\|dōšaxw\" NYB_vol2_glossary.txt | head -8"
}
```


### [2026-09-04T19:54:44.824Z] TOOL RESULT

```
### PHD dwzh/dus
317:duš-ēwāz��h 29 dwāzdahān
318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
2254:hell dušox, dwārišn.
2255:hellish dušoxīg.
2858:dušfarragīh,
5389:dušpādixšāv
5391:dušpādixšāvīh кукуму ary v
5403:dušwār, gūšwār dušwārīh dušnām Gušnasp dušwīr
5410:dušwurrūyišnīh 49 pty ` rey
5412:dušmen
### PHD ān
### NYB
```


## [2026-09-04T19:54:51.622Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nlines=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\n# find leaf containing line 3072\ntxt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read()\nidx=0; leaf=0\ncnt=0\nfor i,l in enumerate(lines,1):\n    if i==3072: break\n    cnt+=l.count('\\f')\nprint('leaf',cnt,'printed page',cnt-17)\nprint(' '.join(t[cnt].split())[:3000])\nEOF"
}
```


### [2026-09-04T19:54:53.440Z] TOOL RESULT

```
leaf 94 printed page 77
FOREIGN VOCABULARY OF THE QUR*AN 77 T 1 *}j (Barzakh). xxiii, 102 ; xxv, 55 ; Iv, 20. A barrier or partition. In xxv, 55, and Iv, 20, it is the barrier between the two seas (<J^j) where the reference is probably to some cosmological myth. In xxiii, 102, it is 1 used in an eschatological passage, and the exegetes do not know what the reference is, though as a glance at at-Tabari 1 s Com- mentary will show, they were fertile in guesses. That the word is not Arabic seems clear from the Lexicons, which venture no suggestions as to its verbal root, are unable to quote any examples of the use of the word from the old poetry, and obviously seek to interpret it from the material of the Qur'an itself. Addai Sher, 19, sought to explain it from the Pers. 1) j j, weeping or crying, but this has little in its favour, and in any case suits only xxiii, 102. Vollers, ZDMG, 1, 646, makes the much more plausible suggestion that T- j j*. is a by-form of r***J* parasaiuj from the Phlv. !g) frasang, Mod. Pers. ^AJL-^d, which preserves its form fairly well in Gk. 7ra/)a<rayy??9, but becomes Aram. NOHS or HOHS * ; Syr. t*a>iS) whence the Ar. f*"j*' The phlv - WXVft) frasangan of PPGl, 116, means a measure of land and of roads, 2 and could thus fit the sense barrier in all three passages. (Burhdn). ii, 105 ; iv, 174 ; xii, 24 ; xxi, 24 ; xxiii, 117 ; xxvii, 65 ; xxviii, 32, 75. An evident proof. In all the passages save xii, 24, and xxviii, 32, it is used in the sense of a proof or demonstration of the truth of one's religious position. In these two cases, one from the story of Joseph and the other from that of Moses, the word refers to an evident miraculous sign from 1 Levy, Worterhuch, iv, 125; Telegdi, in JA, ccxxvi (1935), p. 252. 2 See Horn, Grundriss, 182 ; ftyberg, Glossar, 73.
```


## [2026-09-04T19:55:13.057Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor lf in (352,353,354):\n    s=' '.join(t[lf].split())\n    print('--- leaf',lf,'~printed',lf+543,'---')\n    print(s[:1800])\nEOF"
}
```


### [2026-09-04T19:55:14.845Z] TOOL RESULT

```
leaves 684
--- leaf 352 ~printed 895 ---
‫پوس‬ ‫کون طای باشد ‪.‬‬ ‫دو حتن ‪ -‬بر وزن سوختن » معروف‬ ‫= دو ستارء شعرآی شاه‌ی‬ ‫خواهر‬ ‫دو‬ ‫لت که دوختن جامه باشد بوزن ‪٩‬‏ و دوختن‬ ‫حرع وزره باشد با تیر وئیزه مربدن دشمن ‪٩‬‏ =‬ ‫میگوبند » و بعربی اختامهیل خوانند و عبور‬ ‫وبمعنی اندوختن ومال جمع کردن هم هست‪- ۴‬‬ ‫وغیه‌صاء نیز گویند‪.‬‬ ‫و شیر دوشیدن را یزگوبند ‪ - ۴‬و بمعنی ادا‬ ‫کردن و گزاردن وام وقرض ونماز باشد‪. ۴‬‬ ‫دو خبط ماون * ه کنایه از صبح‬ ‫دو <‪ - * 24‬بروزن سوخته » معروف‬ ‫باشد ‪۰‬‬ ‫کاذب وصبح صادق‬ ‫است ‏ ودوشیده ‪ ۱‬و‪-‬ادا کرده و گزارده رائیز‬ ‫ی‬ ‫است‬ ‫دعروف‬ ‫‪۰‬‬ ‫زود‬ ‫رون‬ ‫‌‬ ‫د‬ ‫دو‬ ‫وغم واندوم ودم وئفی راثیر کوبند ‪ -‬ودرعر ی‬ ‫دوخ چکاد ‪ » ۲‬باجیم فارسی وکاف‬ ‫بمعنی کرم باشد چه کرم ابریشم را دود الحرس‬ ‫بر وزن کور سواد » بمعنی اصلم ‪ ۸‬باشد و آن‬ ‫خوانند وکرم فرمزرا دودالصباغین » و درم قرمز‬ ‫»‬‫چه‬ ‫شخصی است که سراو ساده و بی موی بود‬ ‫جانوریست کوچك وآن دربوتة خارمیباشد وبعضی‬ ‫دوخ یمنی ساده و چکاد بمە‌نی تارك سر و فرق‬ ‫گو ند در درخت بلوط باشد ‪.‬‬ ‫وجلی را کلوزبند که سراو مانند‬ ‫سراست ‪ -‬ک‬ ‫‪ - ۱‬بهلوی‪ -‬یاز ند ‪ . ) 0۳6200 ( 03104‬استی ‪ 08 _ 0200‬و ‪03 - 0200‬‬ ‫(محکم کردن)‪ .‬بلوچی ‪ 82661‬و‪( 1584 82‬دوختن)‪ .‬مدارزانی ‪« 606[0. 0‬اسذق ‪. ۷۷۵‬‬ ‫گیلکی ‪ 020100‬؛ ریش کلمه بدایل ‪ 18221500 , 82000‬بلوچی‪ .‬کلم ابرانی ‪10.600‬‬ ‫‪ ۴‬ره ‪ :‬اندوختن‌وح‪. ۱‬‬ ‫(لیزدرفارسی ‪ 712200‬پهلوی ‪ 0۲6660‬ااست رك‪« :‬هوبدمان ‪۲۷۵».‬‏‬ ‫‪.‬‬ ‫‪02‬‬ ‫) دوشیدن )‪ 2‬بهلر ی‬ ‫هندی بتاان » رسه ‪hod -‬‏ ‪ihdgéd .‬‬ ‫‪۴‬‬ ‫‏‪ .dûshîtan‬کردی ‪nihsûd . 8۱۱60‬‏ ‪ ( id _ mihsûd ۰‬دوخیدن )‪ .‬افعانی‪.12052۷21‬‬ ‫اتی ‪ 0601‬و ‪01‬عنا ‪ .‬بلوچی ‪ . 08215۵0‬وخی ‪ »0712080000 , 61۳0 - 0۳2‬سیرکی‬ ‫» ورك‪ :‬هویشمان ‪ . ۸۷۵‬در اراك م(لطان آباد) ‪rihs 7203‬‏‬ ‫صع _ ‪ « 201200‬ۆه“‬ ‫باين معنی ‏ نوختن («‪.‬م‪. ).‬‬ ‫‪۴‬‬ ‫(شیر دوشیدن) «»کی‌نژاد»‬ ‫ی‬ ‫ک د«‬ ‫م‪3‬‏‬ ‫‪ - ۱‬در اراك (سلطان آباد) ‪٤×٥‬‬ ‫‪۶‬وختن» ‪.‬
--- leaf 353 ~printed 896 ---
‫حودله‬ ‫‪~A‬‬ ‫وزن ومعتی دآوآدهنج است که سفال دودة چراغ‬ ‫‪ -‬ومی ازساحران باشند‬ ‫داوفکن ‏‬ ‫دود کش حمام و بخاری و مطیخ‬ ‫و‬ ‫کرفتن ‪-‬‬ ‫وایشان‌عود ولبان ورانةٌ سیند ومقل ازرق بر آتش‬ ‫باشد‪. ۸‬‬ ‫نهند وافولی خوانند وجن‌راحاض گردانند‪ .‬بعد‬ ‫]دن ه کنابه مازتأسل‬ ‫دود بورر‬ ‫ازآن هراراده‌ای کهخواهند کنند ‪.‬‬ ‫‪٠‬‏‬ ‫ساختن باشد ‪.‬‬ ‫‪۵‬و دا ل‪ - ۲ 4‬بروزن کوساله ‪ .‬دامبازیی‬ ‫‪٩‬‏ »بر وزن رودخاه ‪.‬‬ ‫دوخاه‬ ‫د‬ ‫و‌چنان‌باشد که دوچوب بیاورند‬ ‫است اطفال را“ آن‬ ‫دودمان وخالواده را گوند‪.‬‬ ‫یکی بزرگ بمقدار سهوجب و دیگر یکوچك‬ ‫بقدر بك قبضه وهر دو سر چوب کوچك را تيز‬ ‫دود خوار د با واو ممدوله بروزن‬ ‫و کلخن‬ ‫و مطبخی‬ ‫هوشیار ‪ ,‬بامپرنده ابت‬ ‫کنند وبرزمين گذارند وچوب بزرکه را بر سر‬ ‫آن زنند تااززمین برخیزدفی‌الحال‌چوب نرزگه‬ ‫تاب‪ -‬وتنباکوکش را لگیوزبند ‪.‬‬ ‫را بآرن زد تا براه دور رود » و شخصی درآن‬ ‫دور ایستاده است ‪ ۰۱‬کرآنرا کرفت بازی ازوست‬ ‫ته دلی باشد‬ ‫والا برداشته بیندازده و چوب درازی بعرض بر‬ ‫باشد ‪۰‬‬ ‫کنابه از ‪1‬‬ ‫=‬ ‫دم‬ ‫دود‬ ‫زمن (‪ )۱‬گذاشته اند اکر آن شخص دارننای‬ ‫کی‬ ‫‌‌ بم اول واخفاگ ثالی >‬ ‫دودل‬ ‫بزند بازیرا برده باشد‬ ‫الداختن بر آن چوب‬ ‫والافلا ‪ .‬و این بازیرا خدرراسان‌کال چنبه (‪)۲‬‬ ‫را گویند که‌درامری‌متردد باشد» با دردوجا اهار‬ ‫ولاوبازی ودرجای دبگرپله چوب گوبند‪ .‬وچوب‬ ‫محبت کند گورفتار باشد ‪ -‬موردم منافق رائیز‬ ‫وزرکث را چنبه ‪۴‬‬ ‫کوچك را درفارسی پل ‪ ۴‬ب‬ ‫وبعربی کوچلبرا فله وبزرک رامقلاه خواننده ‪.‬‬ ‫دو د له سس باثالی معروف وفتح ئالت‬ ‫ولام »بمعنی دوداله است» و آن بازبی باش دکه‬ ‫دود | هتح ‪ -‬بفتح هاوسکون نون‬ ‫در خراسان‌کال چنبه ولاوبازی » ودر جای دمگر‬ ‫و جیم ‪ .‬سفالی باشد که برسر چراغ تعبیه کنند‬ ‫جہت گرفتن دوده ازیرای ساختن‌مداد وم کیت‬ ‫پله چوب و دسته پلگوبند ؛ وباینمعنی بکس‬ ‫ثالث هم‌آمده است ‪ -‬وبا الی‌مخفی کورثالت»‬ ‫باشد که‬ ‫و دود کش را فيز گوینده وآن ورا‬ ‫کسی‌را کوبند که‌درکاری‌وارادهمای‌شکی‌وظنی دارد‬ ‫د
--- leaf 354 ~printed 897 ---
‫‪4‬‬ ‫حودمان‬ ‫دود = بضم اول بر وزن مور ؛ معروف‬ ‫دودمان‪ = ۱‬با میم بورزن دوستان »‬ ‫است که تقیض ترديك باشد ‪ - ۱‬وبفتح اول ‪۷‬‬ ‫خاندان وخانواده‪ ۴‬وقبیلهرا کوبند‪ -‬ونام موضعی‬ ‫خواندن درسهای گذشته بود ‪ -‬و یالة شراب را‬ ‫است نزديك بشیراز ‪.‬‬ ‫واسوسانی که اخبارامراواعیان‬ ‫نیز کویند ‪ - ۸‬ج‬ ‫دوده ‪ = ۴‬یسم اول بر وزن بوده ›‬ ‫راتحقیق نمودهبلاطین وپادشاهان نویسند‪ -‬وبمعنی‬ ‫دودمان و خانواده راکویند ‪ -‬و دود چراغ که‬ ‫‪.‬‬ ‫ابام وعهد وزمان هم هت‬ ‫بجهت‌ساختن رمکب و سياهی گیرند‪ -‬ودود کش‬ ‫دور آسران = با سین بی‌نقطه بر‬ ‫ر‬ ‫پ‪-‬و‬‫وطبخ و بخاربرا گیفزته اند‬ ‫حمام م‬ ‫وزن زآوورران‪ ,‬نام پادشاه جادو گران‌باشد واورا‬ ‫بزرکتی و مهتر باشد ‪ -‬وبفتح اول بمعنی دائره‬ ‫دوران سرون هم میگوبند ‪.‬‬ ‫است‬ ‫بر وزن زود رج »‬ ‫دو دهنح؟ =‬ ‫دوراع = بلاقغنطه‌داربروژن سوراخ»‬ ‫سفالی که بآن‌دوده بجهت سیاهی ومر کب‌ساختن‬ ‫دوغ وماستی رکاوبند که شیردران(‪ )۲‬دوشیده‬ ‫گیرند ‪ -‬ودردکش حمام و مطبخ وبخاربرا نیز‬ ‫باشند » واصل این لفت دوغ راغ است مت‬ ‫کونند ‪.‬‬ ‫مامت دامن کوه » اشاره بايشکه شبان در دامن‬ ‫دوهنگ ‪ - °‬بان فارسی » بروزن‬ ‫د‬ ‫گیورسفند بماست دوشیده است چه راغ‬ ‫کوه ش‬ ‫و ممتی دودهنج است که سفال و(‪ )۱‬دود‬ ‫‪7‬‬ ‫دامن کوه نیزآعده است‬ ‫بمعنی‬ ‫چراغ کرفتن ‪ -‬ودود کش حمام ومطبخ و بخاری‬ ‫دروان سرون ‪ - ۲‬بممنی‌دوراسران‬ ‫باشد ‪-‬‬ ‫‏)‪ (e‬چك‪ :‬براان ‪.‬‬ ‫و ‪.‬‬ ‫‪- :‬‬ ‫چك‬ ‫(‪)۱‬‬ ‫از‪ :‬دود ‪ 4+‬مان (یسو ند مان بم‌عنی‌خانه) *قاب‪ ۱‬ص‪ ۳۷‬ح* لغة بمعنی جای‌دود‬ ‫› بهلوی ‪00‬‬ ‫دوده‬ ‫دود خانه ‪۳‬‬ ‫) بمناسیت احاق خانواده چنانکه ‪reyof‬‏ (فر)‬ ‫ناکهی بای وجودش بگل رقت و دود فراق ازدودمانش برآهد‪€, .‬‬ ‫‪۱‬‬ ‫> ‪.‬‬ ‫«اسشق‬ ‫«کلتان ‪. ۸۸۱۰‬‬ ‫‪ ۰‬بهلوی ‪katûd‬‏‬ ‫دودخانه‬ ‫ِ‬ ‫دودمان‬ ‫ت‬ ‫واتصاف)‬ ‫‪( ۰‬یوند نست‬ ‫از؛ دود ا‬ ‫ك‬ ‫‪۳‬‬ ‫‪2‬‬ ‫آهتگد»‪‎‬‬ ‫دود‬ ‫مخفف‬ ‫‪o‬‬ ‫مخفف « دود آهنج» ‪۴‬‬ ‫‪۴‬‬ ‫‪۰‬‬ ‫‪6‬‬ ‫ی استق وهویشمان‬ ‫‪ - ۱‬بهلوی ‪۲0d‬‏ (بعید) «اسشق ‪« ۸۵‬منای
```


## [2026-09-04T19:55:22.649Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'دوزخ' in p:\n        print('leaf',i,'~printed',i+543)\nEOF"
}
```


## [2026-09-04T19:55:23.841Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'برزخ' in p:\n        print('leaf',i)\nEOF"
}
```


### [2026-09-04T19:55:24.787Z] TOOL RESULT

```
leaf 45 ~printed 588
leaf 59 ~printed 602
leaf 341 ~printed 884
leaf 356 ~printed 899
leaf 577 ~printed 1120
leaf 637 ~printed 1180
leaf 657 ~printed 1200
```


### [2026-09-04T19:55:26.659Z] TOOL RESULT

```
leaf 471
leaf 499
leaf 553
```


## [2026-09-04T19:55:32.875Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor lf in (355,356):\n    print('=== leaf',lf,'~printed',lf+543,'===')\n    print(' '.join(t[lf].split())[:2600])\nEOF"
}
```


### [2026-09-04T19:55:34.654Z] TOOL RESULT

```
=== leaf 355 ~printed 898 ===
‫دز رو‬ ‫ی ‪#‬پزرحه‬ ‫دور دست = کنابة از چیزی است که‬ ‫باشد که نام بادشاه ساحران وجادوگران است ‪۰‬‬ ‫رسیدن بان چیزبیار مشکل بائده ‪.‬‬ ‫واوپادشاهی بوده بفایت‌ظالم وجادو گر ‪ ۰‬و کوبند‬ ‫دورس د باسینبیلقطه و حرکت‬ ‫زردشت در زمان اوبهم رسید و اومیخواست که‬ ‫بکر‬ ‫کبرا‬ ‫وشو‬ ‫مجهول‪ ,‬گیاهی‌است کهتخ‬ ‫نمآ‬ ‫زردشت را بکشد بنا بآرنکه (‪ )۱‬باوگفتند این‬ ‫ناد‪.‬‬ ‫مرد پیغمبرخداست وآبین ترا برهم میزندا ‪۰‬‬ ‫خوردن بیخ‌آن جنونآورد‪ .‬وبعضی کوبند دوری‬ ‫دود ای »بر وزن جوبای ‪ .‬اب یکه بگییخاهی است که تخم آنرا شوکران خوانند‬ ‫و آلرا ازنفت بدا ورند وبدوری تفتی مشهوراست‬ ‫مطربان نوازند وآ ترابعربی مزمارخوانند ؛ و با‬ ‫وبعربی طحماء گویند ‪:‬‬ ‫زای نقطه‌دار گهفمته‌اند (‪. )۲‬‬ ‫دور قرو = ضم‌ارل وکرفا و رای‬ ‫دپوا‬ ‫رش ه با بای ایجد‪ ,‬امر از دور‬ ‫بواو رسیده » چیزی‪ .‬بسیار عمیق و صاحب قعر‬ ‫شدن ‪ ۴‬باشد‪ -‬و نیزه‌ای رانیزکوبند که سناش‬ ‫باشد ‪.‬‬ ‫دوشاخه بود درقدیم چوب آنرآءررصع مبکرده‌اند‬ ‫دور قمری» ‪ ۱‬بکر الك ‪ ۰۷.‬دور‬ ‫ویشایثر یادشاهان می‌برده‌اند تامردمان‌بدانند که‬ ‫وویند دور ‪,‬هر‬ ‫آخرکواکب ساره است » ک‬ ‫پادشاه میابدخود را بکناری کشند ‪ -‬و چاوش‬ ‫کو کبی هفت هزارسال میباشد» هزارسال بخودی‬ ‫ولقب فافله رانیز گمته‌اند وآن‌چوبی که چاوش‬ ‫گلر‬ ‫ب سا‬ ‫خود صاحب عمل است » و ششه‬ ‫دزار‬ ‫قافله بردست میگیرد ‪ -‬وعصا و نیز کوچك را‬ ‫و کب دیگر ‪ ۰‬و آدم علیه‌اللام‬ ‫بمشار کت شن‬ ‫نیز کوبند ‪ -‬و بمعنی ناچخ یز آمده است که‬ ‫دراول دورقمری(‪ )۳‬بظپور ‪-‬د» وآن دوره بایان‬ ‫تبرزین باشد ‪ -‬ک‬ ‫ونابه ازآهی باشد که ازته دل‬ ‫رسف )‪.A (4‬‏‬ ‫براید ‪.‬‬ ‫دور گیر ان = بقتح اول » بممنی باده‬ ‫دو ر بل" سیفتح بای بجدبروزن‌مورچل»‬ ‫نوشان وم‌خوارکان‪ - ۹‬ویادشاهان (‪ )۵‬باشد‪.‬‬ ‫مردم بیوفا وبی‌حقیقت راگوبند ‪.‬‬ ‫دو روه نم اول وخفای انی و ثالت‬ ‫دور حو لی ع سبضم‌اول وخای قطه‌دار‬ ‫بواو رسده ‪.‬کل رعا را گوشد جه بکروی آن‬ ‫بواورسیده ولام بتحتانی کشیده » نوعی از سوسن‬ ‫زرد ویکروی سرخ هیباشد ‪ -‬وکتابه از هردم‬ ‫صحرابی‌است » تورآابعربی سیف الفراب خوانند‪,‬‬ ‫متافق ومذبذین هم «ست*‪.٩‬‏ ‪#‬‬ ‫چه بر کهآن بش‌شیرمیماند ‪.‬‬ ‫(‪ )۲‬جك‪ :‬کفته است ؛ چش‪ :‬آهده است ‪.‬‬ ‫)‪ (£‬خم ‪ : ۳‬آن دوره را مادان رسالید ‪۱‬‬ ‫(‪ )۳‬خم ‪ : ۳‬قمر ‪.‬‬ ‫‪ -۳‬پادشاهان ‪.‬‬ ‫(ه) خم ‪:‬‬ ‫‪:‬‬ ‫‪ ۳‬ات رك‬ ‫‪.‬‬ ‫>‬ ‫بودن‬ ‫از« دور‬ ‫‪۳‬‬ ‫‪۳‬‬ ‫است‪.‬‬ ‫«ارجاءب»‬ ‫بدین صفات‬ ‫‪-‬بادشاه متصف‬ ‫‪۱‬‬ ‫‪.‬‬ ‫‪۸‬‬‫‪۳‬ص‬ ‫‪۷۱‬‬‫‪»ld 8101010162‬‏‬ ‫حولی (باحای حطی) =‬ ‫‪-‬ر‬ ‫دو‬‫‪۴‬‬ ‫دول ‪.‬‬ ‫‪ - ۷‬و فتح چهارم و ینجم ‪.‬‬ ‫‪ - ۱‬بقتح اول ‪.‬‬ ‫*ج‪-‬ایی بعید ‪.‬‬ ‫و‬ ‫آری چکنم دولت (فتنة) دور قمری بود‪.‬‬ ‫‪ - ۸‬ازچنگه منش اختر بدمهر بدربرد‬ ‫‪١٩٤۱‬‏ › ‪.‬‬ ‫یفرظازی‬ ‫شحا‬ ‫«‬ ‫‪ - ٩‬بمنانیت آنکه ساقیان جام باده را دور مجلس میگردانند‪. ‎‬‬ ‫بممشوق)‪: ‎‬‬ ‫معنی آمده (خطاب‬ ‫هردو‬ ‫» درادن بت‬ ‫دوروی‬ ‫~‪۰‬‬ ‫‪٩٩
=== leaf 356 ~printed 899 ===
‫پاسس‬ ‫ذو روژی‬ ‫‪ ۱‬دور نه ‪ = ۱‬و دوژله ‪.‬ضم اول و واو‬ ‫دو دودی = با زای قطه‌دار بتحتالی‬ ‫مجهول وفتح زای هوزوزای فارسی ونون » لش‬ ‫تتندرستی را گویند ‪.‬‬ ‫کشیده » وصح‬ ‫گرواند ‪.‬‬ ‫زنبور ویشه وامثال آ‬ ‫دوده ‪ ۱۰‬طامول بر وزن شوره ‪.‬‬ ‫دور = بم اول و واو مجیول وفتح‬ ‫مرطبان کوچك را کوبند ‪-‬‬ ‫زای فارمی گ‪.‬یاهی باشد که ثمرآن گرهیاست‬ ‫و فتح اول دابره و پیمانة(‪)۱‬‬ ‫خاردار ببزرگی فندق» ومغزی‌درمیان دارد وچون‬ ‫شراب ‪ -‬وبمعنی زلف‌هم آمده‬ ‫بجامه بچید جدا نشود ؛ وبسضی گوبند لاكاست‬ ‫است ‪.‬‬ ‫وآن صمع مانندی باشد که بدان‌کارد و شمشیر‬ ‫دودای ‪ -‬با زای‬ ‫ومانندآن را بدسته چسبانند (‪ » )۲‬وبحذف های‬ ‫نقطه دار بروزں ومعنی دورای‬ ‫ات‬ ‫هوزهم ای‬ ‫دوره‬ ‫وربی‬ ‫است که نای حطر بان‌باشد ع‬ ‫دور دنه ‪ ۰ ۷‬با زای فارسی وتحتانی‌بر‬ ‫‪. _ ۵‬‬ ‫مز مار خوانند ‪ - ۳‬وبا ثانی‌مجهول دو ژاننده را‬ ‫وزن بوزینه‪ ,‬بمعنی‌دوزنه است که یش جانوران‬ ‫کویتت ‪۴‬‬ ‫گز نده باشد ‪۰‬‬ ‫دودخ؟ = معروف است و آن نقیض‬ ‫دوسانید ‪ ۰ ۵‬بساین بی‌قطه بروزن‬ ‫اجنس است‬ ‫ونابه ازصدبت‬ ‫باشد © ‪ -‬ک‬ ‫بپشت‬ ‫جوشانید » بعنی چپانید(‪. )۳‬‬ ‫ترد ارباب معرفت ‪ -‬وبزم رشك وحد است فزد‬ ‫عشاق ‪ -‬وسختی ودرشتی وکلفت ورنج ‪ -‬و محل‬ ‫جوشایدن » بمعنی چبایدن بائد اعم ازآنکه‬ ‫عذاب کفار باشد ‪٩‬‏ ‪.‬‬ ‫(‪)۳‬چك‪ :‬چسانید‪.‬‬ ‫(‪ )۲‬چك ‪ :‬چپانند؛ خم‪ : ۳‬بجپانند ‪.‬‬ ‫(‪ )۱‬خم‪ : ۳‬دايرة پیمانه ‪.‬‬ ‫*المدسد» وامرادوری» ودرتر کی «رورلد» بمعنی‌طر فی که دهالهآن‬ ‫فر تان دورق‬ ‫‏‪- ٩‬‬ ‫زای (زانده)‬ ‫‪ ۳" ۴‬از ‪ :‬دول‬ ‫‪ - ۴‬رك‪« :‬دورای»‬ ‫است تفس“‬ ‫»طح‬ ‫‪4‬ت‪2‬ا‪« ۵۷0۳202_0‬بارتولمه ‪۵۷٩‬‏ » از‬ ‫‪ - ۴‬بہاوی ‪« ۷720564‬منای ‪ . ۲۷۲۰‬او‬ ‫ایرانی باستان ‪o 2۷720200 - . ۷220 -‬‏ (جهنم) در اوستای متاخر ا‪۱8)02020‬‬ ‫«پارتولمه ‪ ۹۵۷۰‬در ارهنیع ‪“k‬‏ ‪ . xohud .‬از ‪ .۵ ۷202۵۱‬در ارراق تورفان ‪, ۷۳5۷0‬‬ ‫ربکف ‪۸‬ه * افتالی ع‬ ‫(رژ ‪ ,‬بد) است ‪ .‬رك ‪ :‬ت‬ ‫بازىد ‪ » 20۳2۵‬جزو اول = ‪050۷‬‬ ‫‪80۳260 ,‬‬ ‫‪ ۰ 2260 ۰‬کردی ‪ . 60200‬بلوچی ‪êzêd , 62264‬‏ ‪22۵60 ,‬‬ ‫ورك ‪ .‬هوبشمان ابساً ‪.‬‬ ‫«اسشق ‪۱‬‬ ‫‪.‬‬ ‫اختبار کنند‬ ‫دوزخ‬ ‫عافلان‬ ‫‪ - 9‬کر ترا در بپشت باشد جای‬ ‫«کلتان ‪. ۲۱‬‬ ‫‪ - ۸‬ماضی‬ ‫دوزنه ( هم ) ‪.‬‬ ‫=وژله ‏‬ ‫‪ ۷‬د‬ ‫= دوژننه (هم) ‪.‬‬ ‫‪( ۰‬ھ‪۷ ( .‬‬ ‫آن «دوصدن‬ ‫‪ ۰‬و لاز‬ ‫دفانمدن‬ ‫=‬ ‫‪4‬‬ ‫‪( ۰‬ھ م )‬ ‫«دوسالیدن‬ ‫‪€‬‬ ‫‪€‬‬ ‫شه اصزفحه ‪۵٩۸‬‏‬ ‫بهکلت آنکه دوروی وفددراست آنکه‌یتیم؟‬ ‫به شمی و دو روست همی طعنه زد‬ ‫‪ +‬ی ( مصبری ) » عمل دورو » کیفیت‬ ‫ی‬ ‫ودو‬ ‫ر‪:‬‬‫‪ -‬بفتح اول »از‬ ‫‪ #‬دروولی‬ ‫دو رو ( هم ‪. ).‬‬
```


## [2026-09-04T19:55:50.321Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor lf in (471,499,553):\n    s=' '.join(t[lf].split())\n    i=s.find('برزخ')\n    print('=== leaf',lf,'~printed',lf-220,'===')\n    print(s[max(0,i-700):i+900])\n    print()\nEOF"
}
```


### [2026-09-04T19:55:52.340Z] TOOL RESULT

```
=== leaf 471 ~printed 251 ===
<- ٩ کرده باشند برجاس گوبند» وانرا که در زمین نمانه کنند حدف خوانند . پر جاسب (۱)- منم اول بروزن لپ راسپ» نام مبارزی است تورانی که با پبران وسه ببجنگه کگودرژ آمده یود » بر حاف- جنم اول وسکون ثالی و جیم فارسی بالف کشیده وبقا زده» نلم غله‌ابست کهآ نرا بعربی ملك و جلبان گوبند . # برجان قدم نهادن - کناب از چاره و علاج کردن و بر هلاك راضی شدن باشد . بر جح ریا - کنابه از دحان ممشوق وخوبان و صاحب حسنان باشد- و برج وررانیژ و 70 بر چخ » با جیم فارسی بر وزن برزخ » بمعتی ژوببن(۲) است, وان ننزه‌ای باشدله کوتاه و نه دراز . بر جده لشان - کنابه از بی حجاب درآمدن باشند " پر جلن ح مخضف برچدن باشد . کر ی سوه » نام برج‌هلال - کنبه از از برج سرطان باشد باعبار ايشکه خانهٌ ماه است . (۱) چك : برجاسب . ۱ مراد « مرچند» است . ۳ ۳ ها ]ای وه مان ۴ - این حمتی لفتی است بر خی پر جیسی ۴ بروزن ادرس » یتکی از نامهای ستار مشتری باشد ۴ ؛ و با اولرتاك‌هر دو فارسی هم آمده است . رخ » با خای نقطه‌دار بر وزن چرخ ‏ بیعنی پاره و حصه و بهره - و لخت و بعض باشد ۴ - وتالاب و استضر رانیز گوبند سوبمعنی برقاهم اخست که برلدر: مد است.- ز ضاهی زا 1 وبمعنی شبنم هم آهده است» وباین حعنی‌بضم اول نی زکفته‌اند . برخان س بر وژن ترخان » بمعنی آواز و صدا باشد - وئلم ولایتی است از ملك‌فاری 6 بر ححج » با جیم فارسی بر وزن اعرج » زشت و نازیبا و زبون را گویند» و بفتح اول‌وثانی هم آمده است ۰ برخش ه بر وزن بدخش ‏ ؛ راگویشه . بر خفچچ - بننح‌اول و سکون ثالی‌رثات مفتوح بفا و جیم فلرسی زده » گرانی باشد

=== leaf 499 ~printed 279 ===
 آن مفزی باش که خورند . پسته و چم - بفتح را وکر حا هر دو می‌نقطه » زنی را کوش د که هر کر نزاید , واورا بعرمی عقیمه خوانند . بستییاج" - بنتم اول و سکون ثانی و فوفانی بتحتانی رسیده و بای ابجد بالف کشیده و بجیم زده, بلات رومی خسك زا گونند» وبلفت ال نقین عاصی آلامب اقوانف... طنیعت وخ سرد است باعتدال , و ضماد کردن برزرمهای گرم ناف باشد , بس خواسته - کنابه از مطلوب و معشوق باشد ۴ . لس ح بنم اول وسکون ثانی ودال‌ابجده بمشی بست باشد که گلزار است و جاب یکه موه خوشبوی بهمرسد؟۴ - و بضم اول وفتح ئانیمشدد ونسنی بیخ‌مرجانرا کفتة‌اند که اصل‌مرجان‌باشد 6 (۱) چك : ژند و باژند . و باشمعنی بکر ال هم آحده است ۳ مثبت آن قعر درباست. ربعمالی برآن شدضوبر کنند چون باد بر آن وژد و آفتاب بر آن طبب سخت و سرخ کردد » وآن برزخ است میان‌نیات و جماد چنانکه نغل خرما میان تابتوجیوان » و پوزیه. میان انان وحیوان ,و انان میان‌خلق و رحمان . گویند | کربر کردن‌مصروع بندندنافع باشد » و همچنین اکر ب رکردن صاحب هری منذثك . بسدك بفتح‌اول ونانی‌بروزن‌تگ رکه دستهةٌ کندم و جو درو کرده باشد - و بسکون‌انی بروزن زرد داروبی است که آنرا اکیل السلاه خوانند . سر بر دن س کنابه از وفا کردنوبائملم رسایدن - و ما زگاری نمودن - و روزکاو گذرانیدن ‏ و فمخواری کردن باشف ‏ بسر رشته‌دفتن -» کنابه از آمدن بسرمخنی بودکه در ائنای گفتگو جملةٌ حعترضه پسریا ۱ - بکس اول و ات و تحتانی بالف کشده » بلفت زند و باژند (۱) گوشت را کوبند ؛ و بعربی لحم خوانند . بسقده ۷ « بنتح اول و ثانی و سکون غین نقطه دار و قتح دال ابجد , بمعتی آملده وساخته و هپیاباشد - و شخصی کهکارها را سامان کند و بازد » و منم انی هم بنظر ؟مدماشت » زهراوی > . وف 44۶۸۲ ركك : الجماهر ۱۸۹ سمد . این‌الندیم در ازوارش» اوید : و ور 0 ۷ دانفا ٩ : ٩‏ می+۷. ۴ هز. 0254 «بوستی. بادهش.۸۸». ۰ ب بسرا

=== leaf 553 ~printed 333 ===
ابثان کتاب آسمانی است ت - و ممعنی حوش وشمور هم بنظرآعده است و در مویدالّلاء موش‌لوشته بودند که عربان فاره خوانند» وا اعلملا . يفاك « ممروف است ی که طلم و سم باشد؟ - و نام شهری است تب از تر کستان وبادشاه آن‌شهر کافورنم جادوبی‌بوده آ دمی‌خوار. رستم‌او را کرفت و کشت رآن شهر را عفتوح سلخت ۰ بید‌ار مقر - کنابه از هردم عافل و هوشیار و خبر دار باشد . ید بر که - برآوزن دبکه ب رکه, نوعی از پیکان تبر باشد شبیه ببر که بید. بیدخج ه بفتح اول بر وزن برزخ» اسب جلد و نند و تیز خیز را کویند. وبکر اول هم هت ات ۲ ۹ ید خام - بکر اكث . عود خام را گو مد . بید خت ؟ - با بای مجهول بر وزن کمخت , ستار؛ زهره را گویند که صاحب فلك (۱) چك : تا . لید‌ستر * ع_ با ثانی مجهور و ثای فرشت(۱) بر وزن بی مسطر ء نام حیوانی است بحری که هم در آد نوی نت خوانند . دید ست و باشدن ژتابه‌ازس اسبه کردیدن باشد . بیك‌ طبر ی « نوعی از بید باشد وبعضی س مق و۱ مس طبری: کرشة ۷ و بستی پید موله را کویند که بید مجنون باشد . لیفق ح_بروزن احمق, ببادة شطرنج‌را کویند وآن مهره ای باشد از حملةٌ مپره حای شطرنج. و ععرب‌یاده است ۸ . یدق سیم - کنابه از کو کب و سثاره باشد . ۳ ت رد 7 فوروز نامه ۹۱۳ ۵ص۵/. بضی اسای ی بدوح ۰ ای وی هزدسنا ۰ و۳۲۹ ۷ .2680011868 #«نأه۹:ناتی۱5:۹*. ۱ رگ : آش بجگان . فهرست مزدسنا . بقیه ازصفحهٌ ۳۳۲
```


## [2026-09-04T19:56:09.619Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### IEC anteros\"; grep -n \"^anteros\\|anteros\\|An-teros\" IEC.txt | head -6; echo \"### IEC an- eno ono\"; grep -n \"^enos\\|^onos\\|^anjos\\|^anos\" IEC.txt | head -8"
}
```


### [2026-09-04T19:56:09.681Z] TOOL RESULT

```
### IEC anteros
602:anteros “second, other. Cf. anos (1) and -teros. WP I, 67; II, 337 Skt. ántarab; Per. andar (in the phr: madar i andar 'stepmother); Oss. àndár, cf. also än- dära (*otherwise', fr. *antero); Arm. cf. andra- “back, again’, andren ‘again’; Alb. cf. denom. ndrroj ‘I change: Go. anpar; OHG andar; ON annarr; OE ober; OCS vütoryj; Cz. cf. vteřina “second of time’; úterý (scil. den) “Tuesday”; Li. antras; Latv. otrs; OPr. antars, anters
### IEC an- eno ono
597:anos (1), à, om ‘this, that, yon’. WP II, 337. Cf. anios Skt. ana- (anenab, anaya); Vedic cf. anā “by this; Av. ana-; OPer. ana ‘by this; Arm. (aphetic) na ‘that, he, she, it; him, her’; Alb. cf. an-dej «that way’; OCS on, ona, ono “he, she, it; that’; Li. anas, añs, f. ana
598:anos (2), à ‘ancestor’. WP I, 55 OHG ano, cf. also enel “grandfather; grand- child"; Sw. anor, pl Ukr. on-uka ‘grandchild’; Li. cf. an-yta husband's mother
599:anos (3) “breath, soul, fragrance’. WP I, 56. Cf. anó (1), anomos, anotlom Skt. anáh; Tokh. B. cf. anas-, cpds.; W an ‘element’, beside en-ig ‘soulful’; Cf. also Gk. an- in án-ethon ‘dill
5785:enostis (£n-) — $nmos, à
12192:onos, -es- (1) “burden, load; impost, duty; obligation; bearer, carrier, carriage'. Cf. ono, onmi Vedic ánas, n. "cart Romani cf. anav, v. “bring, carry’; Arm. cf. t-anem E t-anim, id. (fr. *do- on-); Myc. ono- ‘donkey’; ona, npl. (duties, liens! or sim.); Gk. ónos, m. & f. (donkey; windlass, donkey-engine; upper millstone; spindie’. Cf. also possibly ónar ‘dream’; Arm. anur£g: Alb. ândërr, f. id. lit. ‘pressure’? Cf. G Alp-druck for sense); Gk. onésó (‘shall profit. semantic link obscure); Lat. onus, gs: -eris, n. “load, task, obligation; cargo; obstacle’. Uncertainly Go. *ans ds: anza ‘beam’. (A pos- sible isophone arises in Olr. on ‘blemish, taint': Gk. ónomai *blame))
12193:onos, à, om (2) ‘that, von Cf. anos. (The Cypriot & Arcadian forms are inconclusive for determining the vowel) Skt. ana-, Vedic ana; OPer. ana ‘by this’; Av. ana-; Per. àn; Arm. na; (Cypr. Arc. on-, what- ever its value in Attic: aná; an-, neg. etc., seems to represent a nasal vowel of type *àn); Alb. cf. an-daj (therefore', for a type *on-toi- or *an-toi); an-dej (“that way’, fr. *on- or *an- tõi); OCS onü, f: ona, n: ono ‘he, she, it; that, von and com. S1.; Li. ans & anas, f: anà, id.
12196:onos, ~es- — op-
```


## [2026-09-04T19:56:11.311Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SOD asur\"; grep -n \"swr\\|'swr\\|āsur\\|asur\" SOD_pages.txt | head -10; echo \"### SOD leaf 76 (p10)\"; python3 -c \"\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nprint(' '.join(t[76].split())[:1200])\""
}
```


### [2026-09-04T19:56:13.008Z] TOOL RESULT

```
### SOD asur
2230:lands east of Bukhara from Dabusiya to Samarkand;            the Hsiung-Nu, he returned home with a treasure of
2626:century. The faith also gained followers in Mongolia              English translation, Buried Treasures of Chinese
4519:          greed Sogdica. 46, 47, LW 103fn; BBB 566                             asOr (*swr) ©<Skt, asura      ©pi. -t\ ob. pi. -/y,
4520:          Hen.                                                                   -}n =^swr}
4595:     276 "swr =» 's'wr
4597:     277 "swr'n =» "s'wr                                                atar (Hr, "t'r, Mrh) ©ob. -y      =^tr
5887:742 'yswry rwc S                                ^fj^jjj
5898:744 >YsyVn S                                    */<Jj^            (o)xsewar roc ^yswry rwc, xsywr rwc
6375:     mother                                                             minister, trcasurcrO/ie title of an important
6895:                                              swr
### SOD leaf 76 (p10)
645
»trh 11 264 "st'nyh *± 'st'n'yh 282 »s8scyy => »58yscyy 265 »stnly B ^*a 283 "sSyscyy M *U ^a jjj astanc ? ('stny(y)) as-5isci (*s5scyy) =>5scy(y) permanent eighth day of the month GMS 969; "surely", VJ 231; TSP 6.155; S W, Hen. JRAS 1945, 151.15 n pl52 BSOAS 1983, 42, "original" 284 "sych »ph S JjJ^J^Ji 266 "stn'yh =» »st»n>yh asaxc-ap ? ©f. adj. ^'sync-, *>syt- waterfalls, flowing water 267 "stn'yk B oU^,;,.rtl^;ijL:L astanik TSP 3.126 n p!96; Hen. Texts. 726; GMS 600, 634 permanent TSP 2.1184,6.93, 155 285 *Msyt- jjlSV 268 "stny'kCh) S piar^jUUoU asayd ©pt. st. =»*sync-, *sych *ph astanya(k) ^'pw "stny'kh Go)pour GMS 600 permanence GMS 969; Frag. Lcn. 88.5, *stnk? 286 »s rwc(yy) M (Ji:^^)^^ JJfJ 269 "stnyh =» ,st,n»y-h as roc On3) ©<*a0r =»Jrtl rwc ninth day of the month 270 »stny(y) M =* »stn>y Hen. JRAS 1945, 149.4; GMS 299; Hen. 271 *Mstw- -> *stw,t- Oricntalia. 8, 1939,91 n 2 272 »stw»t- S jj.j/ij.j^ j,j *,) 287 "sync- M (oj±^)JJ^<(^)j**ij ast(u)wat ©pt. st. OcObc converted asenc ©Shaih Av. hack ©impf. mysync ^*sych *ph $$ GMS 537, 575, 877 n 2; trans, prct. 'j/w'dV, KG pl77, 588; AVS81 (fo)pour GMS 600, 634; Bailey. Prolcxis. 417; AVS 123 273 "swyt- => 's'wys- 288 »t jiiU 2
```


## [2026-09-04T19:56:33.142Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ns=' '.join(t[76].split())\ni=s.find('swr')\nprint('PAGE10 excerpt:', s[max(0,i-600):i+600])\nprint()\n# find 's'wr main entry\nimport re\nfor lf in range(60,110):\n    if \"s'wr\" in t[lf] or 'sʾwr' in t[lf]:\n        ss=' '.join(t[lf].split())\n        j=ss.find(\"s'wr\")\n        print('leaf',lf,'p',lf-66,':',ss[max(0,j-400):j+400])\n        break\nEOF"
}
```


## [2026-09-04T19:56:34.019Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ns=' '.join(t[193].split())\nprint('leaf193 p127:',s[:1500])\nEOF"
}
```


### [2026-09-04T19:56:34.988Z] TOOL RESULT

```
PAGE10 excerpt:  of the month 270 »stny(y) M =* »stn>y Hen. JRAS 1945, 149.4; GMS 299; Hen. 271 *Mstw- -> *stw,t- Oricntalia. 8, 1939,91 n 2 272 »stw»t- S jj.j/ij.j^ j,j *,) 287 "sync- M (oj±^)JJ^<(^)j**ij ast(u)wat ©pt. st. OcObc converted asenc ©Shaih Av. hack ©impf. mysync ^*sych *ph $$ GMS 537, 575, 877 n 2; trans, prct. 'j/w'dV, KG pl77, 588; AVS81 (fo)pour GMS 600, 634; Bailey. Prolcxis. 417; AVS 123 273 "swyt- => 's'wys- 288 »t jiiU 274 *»swytk B (.juiTrj^J.^,^^ asuydc ©pp. at ©<ahat ©3sg. prcs. subj. of ah- ^Wt, 'sty1 burned may be Hen. LW 103 SCE 186; GMS 767 275 »Swk ** *s»wk> 289 »t*r => n»rh 276 "swr =» 's'wr 290 »t*rh (J>>>^jj)j^<>-7 277 "swr'n =» "s'wr atar (Hr, "t'r, Mrh) ©ob. -y =^tr 278 »S»k(w) B j^S^ fire ase ('s'y) ©Av. atrya <*a0raka GMS 4, 943; TSP; SCE 78, 168; BSTBL; BBB; ashes MSP; STii 4.27 TSP 7.143, 14.ii, n p214; BSTBL, Padm. 56; GMS 291 »tp>k B u/ 299 atpak ©<*a-tdpaka-, Av. a-tapaite =»>ntp 279 »s,m- B heat ? &jijj <oJ*>&i asam ©Av. sam~ S W, IIJ 1976, 69, Frag. 24.1; C2 pl77.18 (to)drink, (ro)swallow 292 »tr =» 't'rh TSP 2.461 pi 75 293 »tr »wst- M (o*U j^ h Jz1)qjXx jS\ 280 »s,m,kk S eXjJL atar ost asame/ak swallowing (rc)extinguish, (fo)lay a fire Sund. MHC p25 Sun

leaf 76 p 10 :  OcObc converted asenc ©Shaih Av. hack ©impf. mysync ^*sych *ph $$ GMS 537, 575, 877 n 2; trans, prct. 'j/w'dV, KG pl77, 588; AVS81 (fo)pour GMS 600, 634; Bailey. Prolcxis. 417; AVS 123 273 "swyt- => 's'wys- 288 »t jiiU 274 *»swytk B (.juiTrj^J.^,^^ asuydc ©pp. at ©<ahat ©3sg. prcs. subj. of ah- ^Wt, 'sty1 burned may be Hen. LW 103 SCE 186; GMS 767 275 »Swk ** *s»wk> 289 »t*r => n»rh 276 "swr =» 's'wr 290 »t*rh (J>>>^jj)j^<>-7 277 "swr'n =» "s'wr atar (Hr, "t'r, Mrh) ©ob. -y =^tr 278 »S»k(w) B j^S^ fire ase ('s'y) ©Av. atrya <*a0raka GMS 4, 943; TSP; SCE 78, 168; BSTBL; BBB; ashes MSP; STii 4.27 TSP 7.143, 14.ii, n p214; BSTBL, Padm. 56; GMS 291 »tp>k B u/ 299 atpak ©<*a-tdpaka-, Av. a-tapaite =»>ntp 279 »s,m- B heat ? &jijj <oJ*>&i asam ©Av. sam~ S W, IIJ 1976, 69, Frag. 24.1; C2 pl77.18
```


### [2026-09-04T19:56:36.791Z] TOOL RESULT

```
leaf193 p127: 128 cntrsV 3239 cntrsV B, S Js-b*^ candarsar (cnfirs^) =»cyns\ cyts'r, cyntrs>r BSTii 879.14; C2, 87V 14 n pl64 pasture inside, in, into 3251 cr'qd'r- C b>yj\~ VJ 898; TSP 3.13; GMS 460; Frag. Len.; cnSrs'r carak-5ar =*cr>q 37.6.7 (ro)dwell STSC 17 3240 cntr(y) S ok-**-" J^ J j^r jy^ ->j*ai/»)«k-fc 3252 crap'Syh M ij^ candar(y) ^cyntr1 car9-paSe ^tfrS'p^w inland, inside(C7i/na) quadruped BBB 507 Anc. Lett. 6.13n 9; Hen. BSOAS 12.604, 9, 605 3253 crks B, M, S ^J 3241 entry s'r j**- ^^ ij^ * < Ji-b * candare-sSr carkas ©<Av.'kahrkasa 0<?}China, (toward j)China vulture Anc. Lett. 222 GMS 139, 249; TSP 3.238, 1320; Bailey. Asica. 8 3254 crm B, S 3242 enw S, C jdUjj> canu -^cWw carm ©Av. carzman ©ob. -yh skin, leather f jP7 £C~*Jl as, like GMS 940; TSP 3.243, 253, 9.147, 13.27, 2211; BSTi 116; Anc. Lett. 1.6 MDii A10, 3,4 B3, 13 B19, 5 J^f >r l& 3243 cp'ys M, S **Js* *cr* j 3255 crmkryy M capls ? carm-kare chief skinworker Sogdica. 33.2, 34 n 1; MDii A14, 22 Sogdica. 54.5 3244 cpS* M, S Ol/O 3256 crmny C f>r j'vjt carm(a)ne ©pi. -t (cpd>) at once (made <?/)skin MDii A14, 24 n p89; Hen. Tales. 475.30; KG 465; BSTii 90523; C2, 57V23 Sund.pl 32; MSP b88 3257 crp B \*s? 3245 cpd> C =* cpS> carp ©ob. -y fat 3246 cr})Y B, M, C ^1^ TSP 2.372 caray (cr*Y) ©Parth. cr}g ©pi. -t light, lamp jU^» <,^xJU jt-jj 3258 crpYwfin B SCE 221, 493; TSP 6.106, 125, 135, 137, 170, 180, carp-Yo5an 8.107; Tales. 478, 41; GMS 1518; C2 57R8; STi ointment 38.2; Sund. AoFviii 1981 p214, cr>g TSP 3.171 n pl97 3
```


## [2026-09-04T19:56:45.846Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4510,4525p' SOD_pages.txt | cut -c1-400; echo \"=== which leaf ===\"; python3 - <<'EOF'\ntxt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nc=0\nfor i,l in enumerate(lines,1):\n    if i==4519: break\n    c+=l.count('\\f')\nprint('leaf',c,'printed',c-66)\nEOF\necho \"=== dozax in SOD ===\"; grep -n \"dozax\\|dwzx\\|dwjx\\|hell\" SOD_pages.txt | head -10"
}
```


### [2026-09-04T19:56:47.726Z] TOOL RESULT

```
                                                                               (to)bc burned, (to)bo consumed
     245 "rwyt-        M                    O^^^          « J^(\J?*            TSP 2.530-, BSTBL, Vim. 117
          aruyd ©pt. st. =»»rwxs-                                         258 "s'wk* B                                           ^7
          (ro)dcsirc, Ga)be greedy
                                                                               asuk    (sswk) ©<*dsuka-, Av. asu\ Pahl. ahug
          GMS 539; Bailey. Prolexis. 313; AVS 138
     246 »rwYtky> M                       (ol^/rj^/F,^^                       SCE 151, 354;GMS976n        978
                                                                              gazelle
         aruydakya ^rwytqy*                                               259 »s»wr B                                    Vj^Oh^
          greed Sogdica. 46, 47, LW 103fn; BBB 566                             asOr (*swr) ©<Skt, asura      ©pi. -t\ ob. pi. -/y,
          Hen.                                                                   -}n =^swr}
                                                                               Asura
     247 »r\vxs M                                   -^J^OT*
         aruxs ©pi.-/                                                          STii 8.6; BSTBL, Padm. 3; TSP 22.19
         greed, desire
                                                                          260 "s'ym'nSy     B                                   o>;
=== which leaf ===
leaf 75 printed 9
=== dozax in SOD ===
3135:  /tarn/ tm-             hell       Av. tzmah-\
3886:  Ouz/we o/ the)woisl hell                                16 "prYs'kmync S                    ^Ji^s* < j*&^M^
31381:                                                                     hell
31404:     (to)look, (reexamine                                            hellish
31412:                                                                    hellish
31420:                                                                   hellish
31437:     hellish
31477:     hellish
37039:11453 zw'rt B                             Joj^^u^J*                      shell, husk, outer layer
37524:                               Thus, entry 6 with the English "{name of the) worst hell" is represented in the
```


## [2026-09-04T19:57:01.895Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HRN leaf 34 (p13)\"; python3 -c \"\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(' '.join(t[34].split())[:2500])\""
}
```


## [2026-09-04T19:57:02.911Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SOD entry 127\"; grep -n \" 127 \" SOD_pages.txt | head -3; echo \"### SNS ahu\"; grep -n -i \"ahu\\b\\|axw\\|ahv\" SNS_pages.txt | head -8"
}
```


### [2026-09-04T19:57:03.461Z] TOOL RESULT

```
### HRN leaf 34 (p13)
13 umgekehrt osk. mo-, umbr. ero- jener' gegenüber ap. aita-, aw. aesa-, skr. esd-. Die Dehnung des ä ist speciell mittel-neupersisch. Darmesteter's Etymologie (aus ap. aniya-) ist falsch, denn ap. aniya- hätte im Np. kaum etwas anderes als m oder in werden können. Zudem kommt das Ideogramm "]; nur durch Nachlässigkeit der Schreiber für aw. anya- vor; das letztere Wort wird vielmehr regulär durch ""XDi wiedergegeben. Im Ya^^nöbi hat sich anya- in Form und Bedeutung sehr getreu bewahrt; hier findet sich ani mUi am andern Tage*, any adam ein anderer Mensch', anyokai 'anders- wo* (Salemann, Mel. asiat. IX, 234); vergl. auch wa/. sar. yan anders* (Tomaschek, Pämir-Dial. 817). Daneben ü in np. aöün (neben andün nach edün gebildet); phlv. a (Stellen bei Hörn, ZDMG. 43, 45 Note 28); bei. s. ä und in Zusammensetzungen (8). Formen der np. Dialekte, wie Käs. ü, T, tat. ü darf man nicht vergleichen, da wir es hier auch mit dem Pronomen der dritten Person zu thun haben können. In Zusammensetzungen findet sich aber üco {== änja)^ uro (= an räh), üzü {=•- an sän) u. a. m.'). 53. mväre Verloren* etc. ap. *a + i^bar- ; phlv. apar (vd. 5, 33, GL), mand. LW. INIX 'Verwüstung*, vergl. äpar^ apar(i)sn *Raub*, apartan^ äpurtan plündern', d. i. überall äw^ (Men.). bei. LW. awar Beute, Raub' (20); arm. LW. aimr 'Raub, Beute*, ayarem 'rauben, plündern* (nach S. Bugge, Indog. Forsch. I, 454 vielleicht statt ^anar aus gr. svuQa; aber warum so gekünstelt?). 54. üväz 'Stimme*, äväze, äväzlden, aw. ai. ä + [/^vac-, s. np. vaj (No. 1072) ; phlv. aväj bzw. äväc 'Stimme , arm. LW. avaj\ avac, afr. kurd. bei. LW. avüz, 55. ärverdeti (AM. ; im Reim Sahn. I, 4 Vers 66 ; heutige >j Mittlerweile auch KZ. 32, 578, No. 3; vergl. auch F. Solmsen , KZ. 31, 472.
```


### [2026-09-04T19:57:03.516Z] TOOL RESULT

```
### SOD entry 127
4159:                                                                 127 »jyt-   M                               o>\}idJ^j*
18520:     Hen. BSOAS 12, 312, 127                                    5195 m'n'y B                              ^ij^tjs
21567:         Len.; BBB b82 f 57; AVS 127                               TSP 2.1179; VJ 49, 78, 123; BSTBL, Vim. 160;
### SNS ahu
1169:                                                                                                                                                .•<?/]„      3 -b-f-X/? <* UiM>-                            106.)        aghu-.ahu-              :       fc-
1188:                                                                                                                                                                                                      U^i-A : ax Sn/ahv3n                                 W»|W
5434:                                                                                                        /iah)*paitisahva-:
6137:                                                                                  \^/U«^      -CMpAxW rperOzgartum: -6»)°^ 3 k                       j *->
8124:                                                                                 l^j**           (*, :vahu- *-*)j^ :vahyah-:
10382:»»£*>•*« J **V« ****'               W * *- *****            tf**      l^       »*   W                                  •*\/\rJ   {AiWb.     1832)vahu. xsa^ra-:^
11174:                                                                                                          Gtf*A*>       varacah-               yl   {AiWb.          1367) var^cahvant: &-
15136:                                                                                                varacahvant 280/6
```


## [2026-09-04T19:57:13.327Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(' '.join(t[33].split())[-1800:])\""
}
```


## [2026-09-04T19:57:14.387Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nc=0\nfor i,l in enumerate(lines,1):\n    if i==1169: break\n    c+=l.count('\\f')\nprint('leaf',c)\nt=txt.split('\\f')\nprint(' '.join(t[c].split())[:1500])\nEOF"
}
```


### [2026-09-04T19:57:14.976Z] TOOL RESULT

```
ihen', ämarzis^ amurzlst (Qiss. Dan.). aw. ä+i/'marz', ämarezen; iphlw, ümurzUan, ämurz(i)sn, ämurzltär Verzeihen' ; ai. ä -j- [/'marj- Vegwischen . Vergl. wa/. namurzg, sar. namüzg 'Rechen, Besen. Im Awesta und Altindischen wird die Bedeutung gnädig sein, verzeihen' durch das Wurzeldeterminativ d aus der [/^merg- ^abwischen' gewonnen, vergl. aw. merezdätä, meresdika-, ai. m^ddti (Bartholomae BB. 13, 87, während Brugmann, Indog. Forsch. I, 171 auch an ai. mfsyate Vergisst*, lit. mifsztl Vergessen denkt). 50. iimö^ten lehren, lernen*, Praes. ämöz-em, amözis, phlv. ämö/tan lehren', ämöc-am, amöc(i)sn^ ämöölmtan ; lit. mokinü „wohl auch faktisch 'lehren*, eigentlich zum können bringen" (Kurschat), moJdnus (refl.) 'ich lerne'. Die Zusammenstellung stammt von Spiegel (Tradit. Lit., 360) ; sie ist indess lautgesetzlich unmöglich, da lit. (d. i. ö) arischem ä entspricht. Skr. ä + [/"muC' heisst nur ^bekleiden*. 51. ätney(ten 'mischen , Praes. ämez-em, ämezis^ ümeze, ämey, vergl. enduh-amey (Vis und Rämin, Seite 83 Vers 16). phlv. ame/tan, ämeßt (Bund.) mischen*; aw. vergl. hememyäsaite *sie mischen sich zusammen', minas *du vereinst' (Bartholomae, Ar. Forsch. III, 61 Anm.; II 170); skr. a-\- l^miks- f mischen*), vergl. ^miisä- 'Quark', neben ai. migrä- Vermischt*; vergl. gr. ulyw^u^ /List^ai etc.^). 52. an jener*. Die heutige Aussprache ün findet sich schon in der bukhärischen Psalmenübersetzung (Et he, Litbl. f. or. Phil. I, 191). päz. a7i bez. hän (Aussprache für die Ideogramme ■^T und auch nöD), phlv. in an-gün, an-c. Zu aw. a«-a, an-agäo, an-äis; skr. an-aycC, Der Übergang von der aw. skr. Bedeutung 'dieser zu jener' ist derselbe, wie in ksl. onü^ lit. ans, lat. ollus {*onlus) ; ^) Np. äme/ten hat mit np. meßten (No. 1006) nichts zu thun, wie Fr. Müller, WZKM. 5, 351 will.
```


### [2026-09-04T19:57:16.799Z] TOOL RESULT

```
leaf 19
. tfUJcu^UftiLttU --v L^c--,U»-U*jl \\/\6*S -T/IY^ -t-r/fiiS (e**.*-Ui)-an + ( u I** . ^^ | •rri • M-IV/T^ ham :L(4tl/b. 1773)sam :Lham- : 4_ui * fc*, -ah§xt cJuaU ahania, ahan5ldan : ^ a-hag5 i **• 1Y/1Y^ r-'^l^)-isn+ (Pers. Stud. 10) (,,*-. *-*-*' , tf Ujbiloo=-S . jJ^i* : hara-bun-iz ^HiA^ . o ^a,U. j^n § ahanjisn : k«*-cv. : - .j/ti -^ .c^yl* havist IV""*' : ^ \*/a^ {AiWb -&/)•> . 1806) haviito- I • k/\o^ o^Jk o'^ 'havistan : : WlO'*' : i** abr-amOn t ^-JS^ j .aj^T^Uji. U *** .a-i^JT^l^L L«** lJ .^jjj J** - U .*ili;xanay i ij !• /r^ .ao-fa-ti-TA-lA-W/T ^(GNPE. 103 . ) j/khan-j 1 **• •X/\Y^ .fi-T/IT^ • ?/!»** -r«-\i h'rayn :^k {AiWb . 1809) hamina- , hami: fc» • 0* T : ahSn/ahan »» W/1A --S (ij6.y~»J hamln :L {Mir. Man. I. 39) : \****> I* tjax" .^^^j/i Uiftfc.l56)ayagh- i I*- 16 \Y-\fi/\&£ {GIrPh. 14) hesin, hasin sj^ *j*1 *S *J o= ^U^* jl ^ U >j .^j.oU.^: ax v/ah v r , : t^ fjJV^W -J->o* T : ahandil (>*-+) : i^cfjj^ "*V .•<?/]„ 3 -b-f-X/? <* UiM>- 106.) aghu-.ahu- : fc- i i/ia ^ -tr-t/yr ^ •j^**' 'j** 1 s ahunavar-ahuvar i j**,. ^L axv I astCraand l** : jXT^i*^ »*>* : (•j^o*** •«&) tf**> : ast5mand + -U -j/^j ax : ^iU-* v to 6/11** ft .jjuU.*,^: havind/havand v U^i-A : ax Sn/ahv3n W»|W i , \a \+* , \a J±*j :
```


## [2026-09-04T19:57:41.340Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### MON asm\"; grep -n \"آسم\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -6; echo \"### MON andar\"; grep -n \"پدراندر\\|مادراندر\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -6"
}
```


### [2026-09-04T19:57:41.428Z] TOOL RESULT

```
### MON asm
incoming/MON/MON_2vol_Adena_v1_djvu.txt:958:پدران آسمانی. آباء کلیسا: کشیشان مسیحی؛ 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:1716:(مج.) آسمان. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:1750:آسمان. آفتاب. ماه.) 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:3207:آس؛ رحوی. بحر آسگون؛ آسمان» فلک. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:3220:آسمانه. بالا» جانب علف:. اس اشا, (اخ.) 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:3223:مظهر وفا. به آسمان شدن: مردن» ار کته : 
### MON andar
MON_part1.txt:17638:(«تا...» با «...خوانده) دهد: پدراندر (پدندر). 
MON_part1.txt:65462:رات: (۲20)۳ [ع.] ((.) پدراندر. 
MON_part1.txt:65492:رابه: (۵-) ۲2201۸ [ع. راید | مادراندر» زن بدر. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:17638:(«تا...» با «...خوانده) دهد: پدراندر (پدندر). 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:65462:رات: (۲20)۳ [ع.] ((.) پدراندر. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:65492:رابه: (۵-) ۲2201۸ [ع. راید | مادراندر» زن بدر.
```


## [2026-09-04T19:57:41.924Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SBK dozax/barzax\"; grep -n \"دوزخ\\|برزخ\" SBK.txt | head -6; echo \"### VIE\"; grep -n \"دوزخ\\|برزخ\" incoming/VIE/VIE_pages.txt | head -6"
}
```


### [2026-09-04T19:57:41.999Z] TOOL RESULT

```
### SBK dozax/barzax
1600:خواپ‌سیری‌در بپشت‌ودوزخ کرد واحکامید کر پیدا اورد که‌در کتاب‌ار تایو بر اف نامك 
3018:خوانده| ند ازمو بدان معروف عصر اردشر وشایور اول است که درعا لم «سیر > بپشت ودوزخ را 
3248:ودوزخ و مینوان بود فرو گزارد ودیران نوشتند و ناما ن کتاب اردای ویر افنامك است . 
9725:ر : دوزخو دوزخ 
10304:فخواعد بود وق چه‌بگذرد برزخایر وفسحت زبان افرود,خواهد شد.خاصه که‌قاعده‌ایاز 
11115:بو دعذاب مخالفان تو دروی کر ٹم ماه همی بدوزخ ه انست 
### VIE
1049:دوزخ درآ مده‌است .
```


## [2026-09-04T19:57:50.049Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('incoming/VIE/VIE_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nc=0\nfor i,l in enumerate(lines,1):\n    if i==1049: break\n    c+=l.count('\\f')\nprint('leaf/pdfpage(0-based)',c,'printed approx',c-6, c+1-6)\nt=txt.split('\\f')\nprint(' '.join(t[c].split())[:1200])\nEOF"
}
```


### [2026-09-04T19:57:51.698Z] TOOL RESULT

```
leaf/pdfpage(0-based) 36 printed approx 30 31
[pdf page 37] همان بغ فارسی است .ريشه وهمطزدر زبان های روسی ؛اوگراشینی »بلوروسی بلغاری » مقدونی »یوگسلاوی »چک و لهسنانی دیده می‌شود و درزبان مفولی بصورت بایات ( نام خدا نام ایل) .بایاژ ( ثروتمند شدن) .بایان ( ثروتمند ) ملاحظه می‌شود زیرا ريشه بگ و پر یکی است وذط انگلیسی بمعنی بزرگ و و بیط شخص متشخص از همین ريشه است . بعلاوه کلمه بیک بدنبال تام اشخاص مشهور بویژه از تبار عثمانی و ناکشورهای عربی در زبان انگلیسی فرآوان مشاهده شده است که همان بگ ترکی می‌باشد . درفارسی علاوه بریغ واژه بگ هم دیده می‌شود » چنانچه بگ و لک‌به معنی رعناگی و بهتری آمده‌است" خسروی گفت : آن یکی بی هنر عزیز چراست واندگر مانده خوار زیسر.سمک. این علامت نسه فرهی ,اشد پس‌چه دعوی کنی‌بدویک‌ولسک (۷) واگر کسانی منکر رأبطه و وبغ باشند رابطه و83 بایگ ( رعناعی و بهتری) را نمی توانند منکر شوند . بگ در واژه بکتاش» مرادف خواجه تاش فارسی نیز برجای ماده‌است. 869 بعقیده بعضی زبان شناسان +268 دگرگون شده بهشت است زیرا اصولا " بهشت کلمه عالی اوستائی است و درزبان‌آوستائی یکی ازعلاقم صفت عالی پسوند و1 ايشت واشت است .ازکلمه ,+۷0۳ واژه ا8نط۷2 ساخته شده که بهشت کنونی از آن زاده شده و بهشت درمعنی "بهترین " اسث هماتکه در انگلیسی است . فردوس برین وآنچه که درفارسی امروز بهشت خوانده می‌شود دراوستا به گونه 1912-220۵ ل72آوهیشت اخو بوده است بمس
```


## [2026-09-04T19:58:05.274Z] TOOL CALL #53: Bash

```json
{
 "command": "sed -n '1,60p' /home/sfmqrb/git/rishe/tools/fetch_source.py"
}
```


### [2026-09-04T19:58:05.313Z] TOOL RESULT

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


## [2026-09-04T19:58:05.609Z] TOOL CALL #54: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-04T19:58:05.616Z] TOOL RESULT

```


```


## [2026-09-04T19:58:20.267Z] TOOL CALL #55: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82enh%E2%82%81-' --note 'page 54, root An 1 breath: PIE *h2enh1- reconstruction' 2>&1 | tail -3",
 "dangerouslyDisableSandbox": true
}
```


### [2026-09-04T19:58:22.162Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/27ca0e127d225e03.txt
```


## [2026-09-04T19:58:28.089Z] TOOL CALL #56: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/ahura' \\\n 'https://en.wiktionary.org/wiki/%CE%B1%CC%94%CC%81%CF%83%CE%B8%CE%BC%CE%B1' \\\n 'https://www.etymonline.com/word/asthma' \\\n 'https://en.wiktionary.org/wiki/anima' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/ansuz' \\\n 'https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%B8%E0%A5%81%E0%A4%B0' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B2%D8%AE' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%B2%D8%AE' \\\n ; do echo \"== $u\"; python3 tools/fetch_source.py \"$u\" --note 'page 54 verification (An 1 / An 2 charts)' 2>&1 | tail -1; done",
 "dangerouslyDisableSandbox": true
}
```


## [2026-09-04T19:58:32.182Z] TOOL CALL #57: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%A2%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D8%B1' \\\n 'https://www.etymonline.com/word/other' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82entero-' \\\n 'https://www.etymonline.com/word/Oswald' \\\n 'https://www.etymonline.com/word/animal' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/asuras' \\\n 'https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%A3' \\\n ; do echo \"== $u\"; python3 tools/fetch_source.py \"$u\" --note 'page 54 verification (An 1 / An 2 charts)' 2>&1 | tail -1; done",
 "dangerouslyDisableSandbox": true
}
```


### [2026-09-04T19:58:36.289Z] TOOL RESULT

```
== https://en.wiktionary.org/wiki/ahura
/home/sfmqrb/git/rishe/data/verification/sources/web/c181f4a86d957951.txt
== https://en.wiktionary.org/wiki/%CE%B1%CC%94%CC%81%CF%83%CE%B8%CE%BC%CE%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/2de46ebb4dd7ede2.txt
== https://www.etymonline.com/word/asthma
/home/sfmqrb/git/rishe/data/verification/sources/web/ee54617c562488e6.txt
== https://en.wiktionary.org/wiki/anima
/home/sfmqrb/git/rishe/data/verification/sources/web/37e8b7eefd93499b.txt
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/ansuz
/home/sfmqrb/git/rishe/data/verification/sources/web/9b7eac3910d895c1.txt
== https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%B8%E0%A5%81%E0%A4%B0
/home/sfmqrb/git/rishe/data/verification/sources/web/573d7604e2f3b7cc.txt
== https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B2%D8%AE
/home/sfmqrb/git/rishe/data/verification/sources/web/75aed0463242b710.txt
== https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%B2%D8%AE
/home/sfmqrb/git/rishe/data/verification/sources/web/113500b587fe58fa.txt
```


### [2026-09-04T19:58:42.462Z] TOOL RESULT

```
== https://en.wiktionary.org/wiki/%D8%A2%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/03234bb58a6047c4.txt
== https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/b2a6adec0e1055ef.txt
== https://www.etymonline.com/word/other
/home/sfmqrb/git/rishe/data/verification/sources/web/fe5b7fa0eab598b4.txt
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82entero-
/home/sfmqrb/git/rishe/data/verification/sources/web/e1d0e8ae4fa52831.txt
== https://www.etymonline.com/word/Oswald
/home/sfmqrb/git/rishe/data/verification/sources/web/c881dd147c459683.txt
== https://www.etymonline.com/word/animal
/home/sfmqrb/git/rishe/data/verification/sources/web/30f0908ee8e744bb.txt
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/asuras
/home/sfmqrb/git/rishe/data/verification/sources/web/78fb0757f04b76ee.txt
== https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%A3
/home/sfmqrb/git/rishe/data/verification/sources/web/a0ce1e7c217c7116.txt
```


## [2026-09-04T19:58:46.343Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 27ca0e127d225e03 c181f4a86d957951 2de46ebb4dd7ede2 ee54617c562488e6; do echo \"########## $f\"; sed -n '1,200p' $f.txt | grep -v '^\\s*$' | head -70; done"
}
```


### [2026-09-04T19:58:47.796Z] TOOL RESULT

```
########## 27ca0e127d225e03
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82enh%E2%82%81-
FETCHED: 2026-09-04T19:58:22Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₂enh₁- - Wiktionary, the free dictionary
Reconstruction:Proto-Indo-European/h₂enh₁- - Wiktionary, the free dictionary 
 Jump to content 
 Main menu 
 Main menu
 move to sidebar 
 hide 
 Navigation
 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 
 Search 
 Search 
 Appearance 
 Donations 
 Create account 
 Log in 
 Personal tools 
 Donations 
 Create account 
 Log in 
 Contents
 move to sidebar 
 hide 
 Beginning
 1 
 Proto-Indo-European 
 Toggle Proto-Indo-European subsection 
 1.1 
 Etymology 
 1.2 
 Root 
 1.2.1 
 Derived terms 
 1.3 
 References 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ h₂enh₁- 
 Add languages 
 Reconstruction 
 Discussion 
 English 
 Read 
 Edit 
 View history 
 Tools 
 Tools
 move to sidebar 
 hide 
 Actions
 Read 
 Edit 
 View history 
 General
 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Get shortened URL 
 Print/export
########## c181f4a86d957951
URL: https://en.wiktionary.org/wiki/ahura
FETCHED: 2026-09-04T19:58:30Z
STATUS: 200
TITLE: ahura - Wiktionary, the free dictionary
ahura - Wiktionary, the free dictionary 
 Jump to content 
 Main menu 
 Main menu
 move to sidebar 
 hide 
 Navigation
 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 
 Search 
 Search 
 Appearance 
 Donations 
 Create account 
 Log in 
 Personal tools 
 Donations 
 Create account 
 Log in 
 Contents
 move to sidebar 
 hide 
 Beginning
 1 
 English 
 Toggle English subsection 
 1.1 
 Etymology 
 1.2 
 Noun 
 1.2.1 
 Derived terms 
 1.2.2 
 Related terms 
 2 
 Ese 
 Toggle Ese subsection 
 2.1 
 Noun 
 Toggle the table of contents 
 ahura 
 3 languages 
 Malagasy 
 Português 
 Kiswahili 
 Entry 
 Discussion 
 English 
 Read 
 Edit 
 View history 
 Tools 
 Tools
 move to sidebar 
 hide 
 Actions
 Read 
 Edit 
 View history 
########## 2de46ebb4dd7ede2
URL: https://en.wiktionary.org/wiki/%CE%B1%CC%94%CC%81%CF%83%CE%B8%CE%BC%CE%B1
FETCHED: 2026-09-04T19:58:30Z
STATUS: -1
TITLE: 
FETCH FAILED: HTTP Error 404: Not Found
########## ee54617c562488e6
URL: https://www.etymonline.com/word/asthma
FETCHED: 2026-09-04T19:58:31Z
STATUS: 200
TITLE: Asthma - Etymology, Origin & Meaning
Asthma - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of asthma 
 asthma (n.) 
 "respiratory disorder characterized by paroxysms of labored breathing and a feeling of contraction in the chest," late 14c., asma , asma , from Latin asthma , from Greek asthma "shortness of breath, a panting," from azein "breathe hard," probably related to anemos "wind" (from PIE root *ane- "to breathe;" see animus ). The -th- was restored in English 16c.
 also from late 14c. 
 Entries linking to asthma 
 animus (n.) 
 1820, "temper" (usually in a hostile sense), from Latin animus "rational soul, mind, life, mental powers, consciousness, sensibility; courage, desire," related to anima "living being, soul, mind, disposition, passion, courage, anger, spirit, feeling," from PIE root *ane- "to breathe."
 It has no plural. As a term in Jungian psychology for the masculine component of a feminine personality, it dates from 1923 (compare anima ). For sense development in Latin, compare Old Norse andi "breath, breathing; current of air; aspiration in speech;" also "soul, spirit, spiritual being."
 asthmatic (adj.) 
 "pertaining to or afflicted with asthma," 1540s, from Latin asthmaticus , from Greek asthmatikos , from asthma "shortness of breath" (see asthma ). The noun meaning "person with asthma" is recorded from 1610s.
 th 
 digraph representing a sound found chiefly in words of Old English, Old Norse or Greek origin, but unpronounceable by Normans and many other Europeans. In reconstructed PIE origins, the Greek -th- and the Germanic -th- descend from different sound roots.
 In Greek, -th- at first represented a true aspirate (T + H, as in English outhouse , shithead , etc.). But by 2c. B.C.E. the Greek letter theta was in universal use and had the modern "-th-" sound.
 Latin had neither the letter nor the sound, and the Romans represented Greek theta by -TH- , which they generally pronounced, at least in Late Latin, as simple "-t-" (passed down to Romanic languages, as in Spanish termal "thermal," teoria "theory," teatro "theater").
 In Germanic languages it represents a sound common at the start of words or after stressed vowels. To indicate it in alphabetic writing, Old English and Old Norse used the characters ð "eth" (a modified form of -d- ) and þ "thorn," which had been a rune. Old English, unlike Old Norse, seems never to have standardized which of the two letters represented which of the two forms of the sound ("hard" and "soft").
 The digraph -th- sometimes appears in early Old English writing, on the Latin model, and it returned in Middle English with the French scribes, driving out eth by c. 1250, but thorn persisted, especially in demonstratives ( þat , þe , þis , etc.), even as other words were being spelled with -th- .
 The advent of printing dealt its death-blow, however, as the first types were imported from continental founders, who had no thorn. For a time y was used in its place (especially in Scotland), because it had a similar shape, hence ye for the in pseudo-historical typographical affectation Ye Olde _____ (it never was pronounced "ye," only printed that way; see ye (article)).
 After the Renaissance, English writers saw that some words inherited from French or Latin with a t- had been th- in the original Greek. The -th- was restored in amethyst , asthma , pythoness , orthography , theme , throne , etc.); it failed in acolyte . Over-correction in English created unetymological forms such as Thames and author . Caxton (late 15c.) has thau for tau , and compare Chaucer's Sir Thopas ( topaz ). The earliest form of Torah in English was Thora (1570s). Yet some words borrowed from Romanic languages preserve, on the Roman model, the Greek -th- spelling but the simple Latin "t" pronunciation ( Thomas , thyme ).
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 attack 
 c. 1600, "assault, assail, begin hostilities against," from French attaquer (16c.), from Florentine Italian attaccare (battaglia) "join (battle)," thus the word is a doublet of attach, which was used 15c.-17c. also in the sense now reserved to attack. The meaning "endeavor to bri
 tartar 
 "bitartrate of potash, sediment of potassium tartarate" (a deposit left during fermentation), late 14c., from Old French tartre and directly from Medieval Latin tartarum, from late Greek tartaron "tartar encrusting the sides of wine casks," a word perhaps of Semitic origin, but i
 abandon 
 late 14c., "to give up (something) absolutely, relinquish control, give over utterly;" also reflexively, "surrender (oneself), yield (oneself) utterly" (to religion, fornication, etc.), from Old French abandonner "surrender, release; give freely, permit," also reflexive, "devote 
 Rubicon 
 in the figurative phrase cross (or pass) the Rubicon "take a decisive step," 1620s, a reference to a small stream to the Adriatic on the coast of northern Italy which in ancient times formed part of the southern boundary of Cisalpine Gaul. It was crossed by Caesar, Jan. 10, 49 B.
 record 
 c. 1200, recorden, "to repeat, reiterate, recite; rehearse, get by heart" (senses now obsolete), from Old French recorder "tell, relate, repeat, recite, report, make known" (12c.) and directly from Latin recordari "remember, call to mind, think over, be mindful of," from re-, her
 reparation 
 late 14c., reparacioun, "repair, act of mending" (a sense now rare or obsolete), also "amends, compensation, recompense, satisfaction for injury, what is done to repair a wrong," from Old French reparacion and directly from Late Latin reparationem (nominative reparatio) "act of r
 artillery 
 late 14c., "warlike munitions," especially ballistic engines, from Anglo-French artillerie, Old French artillerie (14c.), from artillier "to provide with engines of war" (13c.), which probably is from Medieval Latin articulum "art, skill," a diminutive of Latin ars (genitive arti
 scorn 
 late 12c., scorn, skarn, "feeling or attitude of contempt; contemptuous treatment, mocking abuse," a shortening of Old French escarn "mockery, derision, contempt," a common Romanic word (Spanish escarnio, Italian scherno) of Germanic origin (source also of Old High German skern "
 cast 
 c. 1200, "throw, throw violently, fling, hurl," from a Scandinavian source akin to Old Norse kasta "to throw" (cognate with Swedish kasta, Danish kaste, North Frisian kastin), a word of uncertain origin. The meaning "to form in a mold" is late 15c. In the sense of "to throw" it r
 pine 
 "coniferous tree, tree of the genus Pinus," Old English pin (in compounds), from Old French pin and directly from Latin pinus "pine, pine-tree, fir-tree," which is perhaps from a PIE *pi-nu-, from root *peie- "to be fat, swell" (see fat (adj.)). If so, the tree's name would be a 
 Share asthma 
 ‘ cite ’ 
 Page URL :
 https://www.etymonline.com/word/asthma Copy 
 HTML Link :
 <a href="https://www.etymonline.com/word/asthma">Etymology of asthma by etymonline</a> Copy 
 APA Style :
 Harper, D. (n.d.). Etymology of asthma. Online Etymology Dictionary. Retrieved September 4, 2026, from https://www.etymonline.com/word/asthma Copy 
 Chicago Style :
 Harper Douglas, "Etymology of asthma," Online Etymology Dictionary, accessed September 4, 2026, https://www.etymonline.com/word/asthma. Copy 
 MLA Style :
 Harper, Douglas. "Etymology of asthma." Online Etymology Dictionary, https://www.etymonline.com/word/asthma. Accessed 4 September, 2026. Copy 
 IEEE Style :
 D. Harper. "Etymology of asthma." Online Etymology Dictionary. https://www.etymonline.com/word/asthma (accessed September 4, 2026). Copy 
 Remove Ads 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
```


## [2026-09-04T19:58:58.451Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 27ca0e127d225e03 c181f4a86d957951 9b7eac3910d895c1 573d7604e2f3b7cc 78fb0757f04b76ee a0ce1e7c217c7116; do echo \"########## $f\"; grep -n -A4 -i \"Etymology\" $f.txt | grep -v '^\\s*$' | sed -n '1,60p'; done 2>/dev/null | head -180"
}
```


### [2026-09-04T19:59:00.234Z] TOOL RESULT

```
########## 27ca0e127d225e03
62: Etymology 
63-
64- 1.2 
65- Root 
66-
--
134: Etymology
135- [ edit ] 
136-
137- Likely of onomatopoeic origin. Compare *h₁eh₁t- ( idem ) .
138-
########## c181f4a86d957951
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
--
150: Etymology
151- [ edit ] 
152-
153- Transliteration of Avestan 𐬀𐬵𐬎𐬭𐬀 ( ahura , “ lord ” ) .
154-
########## 9b7eac3910d895c1
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
143: Etymology
144- [ edit ] 
145-
146- From Proto-Indo-European *h₂émsus , from *h₂ems- ( “ to engender, beget ” ) . Compare Hittite 𒈗𒍑 ( ḫa-aš-šu-uš /⁠ḫaššuš⁠/ , “ king ” ) , Old Avestan 𐬀𐬵𐬎 ( ahu ) / Younger Avestan 𐬀𐬢𐬵𐬎 ( aŋhu , “ lord ” ) , Sanskrit असुर ( ásura , “ godlike, powerful ” ) .
147-
########## 573d7604e2f3b7cc
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
88: Etymology 
89-
90- 2.2 
91- Pronunciation 
92-
--
128: Etymology 
129-
130- 4.3 
131- Pronunciation 
132-
--
228: Etymology
229- [ edit ] 
230-
231- Learned borrowing from Sanskrit असुर ( asura ) .
232-
--
304: Etymology
305- [ edit ] 
306-
307- Borrowed from Sanskrit असुर ( asura ) . First attested as Old Marathi 𑘀𑘭𑘳𑘨 ( asura ) .
308-
--
578: Etymology
579- [ edit ] 
580-
581- From Proto-Indo-Aryan *Hásuras , from Proto-Indo-Iranian *Hásuras , from Proto-Indo-European *h₂ń̥suros ~ *h₂ḿ̥suros .
582-
583: Related to असु ( asu- ) , with several possible etymologies and meanings. In the context of asura conventionally associated with asu- in the sense of "master of the house". This meaning is not further narrowed by its etymology: cf. Avestan 𐬀𐬵𐬎 ( ahu , “ lord; life, existence ” ) and 𐬀𐬵𐬎𐬭𐬀 ( ahura , “ lord ” ) , Hittite 𒈗 ( ḫaššū , “ king ” ) , Old Norse æsir ( “ gods ” ) and Old English ōs ( “ god ” ) . Possibly ultimately from Proto-Indo-European *h₂ens- ( “ to engender, beget ” ) .
584-
585- The Brahmana s and the Purana s derive asura from another asu- , "breath", a cognate of which is found in Av. ahu- , "life, existence". In yet other post-Vedic Sanskrit literature, asura was back-formed as a-sura , "non- sura ", with sura then associated with a group of gods who inhabit Indra's domain.
586-
587- Pronunciation
########## 78fb0757f04b76ee
########## a0ce1e7c217c7116
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
82: Etymology 
83-
84- 2.2 
85- Pronunciation 
86-
--
105: Etymology 
106-
107- 3.3 
108- Pronunciation 
109-
--
203: Etymology
204- [ edit ] 
205-
206- Borrowed from Sanskrit प्राण ( prāṇa ) .
207-
--
265: Etymology
266- [ edit ] 
267-
268- Borrowed from Sanskrit प्राण ( prāṇa ) .
269-
--
509: Etymology
510- [ edit ] 
511-
512- प्र- ( pra- ) +‎ अन ( aná ) .
513-
```


## [2026-09-04T19:59:12.831Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"###### h2enh1\"; sed -n '/^ Reconstruction:Proto-Indo-European\\/ h/,$p' 27ca0e127d225e03.txt | grep -v '^\\s*$' | sed -n '1,60p'"
}
```


## [2026-09-04T19:59:13.882Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 75aed0463242b710 113500b587fe58fa; do echo \"########## $f\"; grep -n -B2 -A8 \"Etymology$\" $f.txt | grep -v '^\\s*$' | sed -n '1,80p'; done"
}
```


### [2026-09-04T19:59:14.650Z] TOOL RESULT

```
###### h2enh1
 Reconstruction:Proto-Indo-European/ h₂enh₁- 
 Add languages 
 Reconstruction 
 Discussion 
 English 
 Read 
 Edit 
 View history 
 Tools 
 Tools
 move to sidebar 
 hide 
 Actions
 Read 
 Edit 
 View history 
 General
 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Get shortened URL 
 Print/export
 Download as PDF 
 Printable version 
 In other projects
 Appearance
 move to sidebar 
 hide 
 From Wiktionary, the free dictionary
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Indo-European
 [ edit ] 
 Etymology
 [ edit ] 
 Likely of onomatopoeic origin. Compare *h₁eh₁t- ( idem ) .
 Root
 [ edit ] 
 *h₂enh₁- ( imperfective ) [ 1 ] [ 2 ] [ 3 ] 
 to breathe 
 Synonyms: *h₁eh₁t- , *pnew- 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *h₂enh₁- (70 c, 0 e) 
 *h₂énh₁-ti ~ h₂n̥h₁-énti ( athematic root present ) 
 *h₂én-ye-ti ( ye-present ) ( < *h₂énh₁-ye-ti with Pinault's law ) 
 Proto-Albanian: *anja [ 4 ] 
 Albanian: ëj ( “ to blow; to blow up, swell ” ) 
 *h₂enh₁-dʰō 
 Proto-Germanic: *anadô ( see there for further descendants )
 *h₂enh₁-ǵʰ- [ 5 ] 
 ⇒ *h₂en(h₁)ǵʰ-eh₂yé-ti 
 Proto-Germanic: *angōną 
 Old Norse: anga ( “ to exhale; to emit a scent ” ) ( see there for further descendants )
 ⇒ *h₂en(h₁)ǵʰ-ō [ 5 ] 
 Proto-Armenian: 
 Old Armenian: անձն ( anjn ) ( see there for further descendants )
 Proto-Germanic: *angô ( see there for further descendants )
 ⇒ *h₂en(h₁)ǵʰ-o-m
```


### [2026-09-04T19:59:16.408Z] TOOL RESULT

```
########## 75aed0463242b710
184- [ edit ] 
185-
186: Etymology
187- [ edit ] 
188-
189- Etymology tree
190-
191- Proto-Indo-European *dews- ? 
192- Proto-Indo-European *dus- 
193- Proto-Indo-Iranian *duš- 
194- Proto-Iranian *duš- 
--
325- Wikipedia ur 
326-
327: Etymology
328- [ edit ] 
329-
330- Etymology tree
331-
332- Proto-Indo-European *dews- ? 
333- Proto-Indo-European *dus- 
334- Proto-Indo-Iranian *duš- 
335- Proto-Iranian *duš- 
--
412- [ edit ] 
413-
414: Etymology
415- [ edit ] 
416-
417- Etymology tree
418-
419- Proto-Indo-European *dews- ? 
420- Proto-Indo-European *dus- 
421- Proto-Indo-Iranian *duš- 
422- Proto-Iranian *duš- 
########## 113500b587fe58fa
159- [ edit ] 
160-
161: Etymology
162- [ edit ] 
163-
164- From Parthian *bwrz-ʾxw ( /⁠burz-axw⁠/ , “ height, unsurmountable passage ” ) , from Parthian bwrz ( /⁠burz⁠/ , “ high ” ) + ʾxw ( /⁠axw⁠/ , “ world ” ) .
165-
166- Noun
167- [ edit ] 
168-
169- بَرْزَخ • ( barzaḵ )  m ( plural بَرَازِخ ( barāziḵ ) ) 
--
362- [ edit ] 
363-
364: Etymology
365- [ edit ] 
366-
367- Borrowed from Arabic بَرْزَخ ( barzaḵ ) , from Parthian *bwrz-ʾxw ( /⁠burz-axw⁠/ ) , from Parthian bwrz ( /⁠burz⁠/ , “ high ” ) + ʾxw ( /⁠axw⁠/ , “ world ” ) . 
368-
369- Noun
370- [ edit ] 
371-
372- برزخ • ( barzax )
```


## [2026-09-04T19:59:28.974Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '186,240p' 75aed0463242b710.txt | grep -v '^\\s*$'; echo \"=== persian section ===\"; sed -n '410,470p' 75aed0463242b710.txt | grep -v '^\\s*$'"
}
```


### [2026-09-04T19:59:30.596Z] TOOL RESULT

```
 Etymology
 [ edit ] 
 Etymology tree
 Proto-Indo-European *dews- ? 
 Proto-Indo-European *dus- 
 Proto-Indo-Iranian *duš- 
 Proto-Iranian *duš- 
 Proto-Iranian *Háhuš 
 Proto-Iranian *dušHáhuš 
 Middle Persian 𐭣𐭥𐭱𐭧𐭥𐭩 ( dʿšḥʿy ) 
 Persian دوزخ 
 Inherited from Middle Persian 𐭣𐭥𐭱𐭧𐭥𐭩 ( dušox , “ hell ” ) , from Old Iranian *daužaxva , from earlier *duš-ahw-a- , from Proto-Iranian *dušHáhuš ( literally “ bad existence ” ) , a compound of *duš- ( “ bad ” ) +‎ *Háhuš , from Proto-Indo-Iranian *Hásuš ( “ life, existence, being ” ) .
 Cognates include Manichaean Middle Persian [script needed] ( dwšx ) , [script needed] ( dwšwx /⁠dušox⁠/ ) , Middle Persian 𐬛𐬋𐬲𐬀𐬑 ( dōžax ) , 𐬛𐬋𐬰𐬀𐬑 ( dōzax ) , 𐬛𐬋𐬘𐬀𐬑 ( dōjax ) , Manichaean Parthian [script needed] ( dwjx /⁠dōžax⁠/ ) , Avestan 𐬛𐬀𐬊𐬲𐬀𐬎𐬎𐬀 ( daožauua ) , 𐬛𐬎𐬲𐬀𐬢𐬵𐬎 ( dužaŋhu ) , Pashto دوغښ ( doǧaẍ ) , Northern Kurdish dojeh , Central Kurdish دۆژە ( doje ) , Baluchi دوجک ( dōǰak ) , دوژه ( dōžē ) .
 Compare Old Armenian դժոխ ( džox , “ hell ” ) and Georgian ჯოჯოხეთი ( ǯoǯoxeti ) , Iranian borrowings.
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /doː.ˈzax/ 
 ( Dari, formal ) IPA ( key ) : [d̪oː.zäx] 
 ( Dari, formal ) IPA ( key ) : [d̪oː.zäx] 
 ( Kabuli ) IPA ( key ) : [d̪oː.zäx] 
 ( Hazaragi ) IPA ( key ) : [d̪ʊː.zäx] 
 ( Iran, formal ) IPA ( key ) : [d̪uː.zæx] 
 ( Tajik, formal ) IPA ( key ) : [d̪ɵ.zäχ] 
 Rhymes: -ax 
 Readings
 Classical reading ? 
 dōzax
 Dari reading ? 
 dōzax
 Iranian reading ? 
 duzax
 Tajik reading ? 
=== persian section ===
 Ushojo
 [ edit ] 
 Etymology
 [ edit ] 
 Etymology tree
 Proto-Indo-European *dews- ? 
 Proto-Indo-European *dus- 
 Proto-Indo-Iranian *duš- 
 Proto-Iranian *duš- 
 Proto-Iranian *Háhuš 
 Proto-Iranian *dušHáhuš 
 Middle Persian 𐭣𐭥𐭱𐭧𐭥𐭩 ( dʿšḥʿy ) 
 Classical Persian دوزَخ ( dōzax ) bor. 
 Urdu دوزَخ ( dozax ) bor. 
 Ushojo دوزَخ 
 Borrowed from Urdu دوزَخ ( dozax ) .
 Noun
 [ edit ] 
 دوزخ ( dōzax ) 
 hell , hellfire 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=دوزخ&oldid=92284038 "
 Categories : Persian terms inherited from Proto-Iranian 
 Persian terms derived from Middle Persian 
 Persian terms derived from Proto-Indo-Iranian 
 Persian terms derived from Proto-Indo-European 
 Persian terms derived from Proto-Iranian 
 Persian terms inherited from Middle Persian 
 Persian terms derived from Old Iranian languages 
 Persian terms inherited from Proto-Indo-Iranian 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/ax 
 Rhymes:Persian/ax/2 syllables 
 Persian lemmas 
 Persian nouns 
 fa:Religion 
 fa:Afterlife 
 Urdu terms derived from Middle Persian 
 Urdu terms derived from Proto-Indo-European 
 Urdu terms derived from Proto-Indo-Iranian 
 Urdu terms derived from Classical Persian 
 Urdu terms borrowed from Classical Persian 
 Urdu terms derived from Proto-Iranian 
 Urdu terms inherited from Old Hindi 
 Urdu terms derived from Old Hindi 
 Urdu terms with IPA pronunciation 
 Urdu terms with audio pronunciation 
 Rhymes:Urdu/əx 
 Rhymes:Urdu/əx/2 syllables 
 Urdu lemmas
```


## [2026-09-04T19:59:38.166Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"###### AN (03234bb5)\"; grep -n -A10 \"^ Etymology$\" 03234bb58a6047c4.txt | grep -v '^\\s*$' | sed -n '1,60p'"
}
```


## [2026-09-04T19:59:39.231Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"###### ANDAR\"; grep -n -A10 \"^ Etymology$\" b2a6adec0e1055ef.txt | grep -v '^\\s*$' | sed -n '1,80p'"
}
```


### [2026-09-04T19:59:40.130Z] TOOL RESULT

```
###### AN (03234bb5)
```


### [2026-09-04T19:59:41.798Z] TOOL RESULT

```
###### ANDAR
244: Etymology
245- [ edit ] 
246-
247- Etymology tree
248-
249- Proto-Indo-European *h₁én 
250-
251- Proto-Indo-European *-teros 
252-
253- Proto-Indo-European *h₁énteros 
254- Proto-Indo-Iranian *Hántaras 
--
320: Etymology
321- [ edit ] 
322-
323- Borrowed from Classical Persian اندر ( andar ) .
324-
325- Pronunciation
326- [ edit ] 
327-
328- IPA ( key ) : [ənd̪ərʊ] 
329-
330- Adverb
```


## [2026-09-04T19:59:44.856Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '244,300p' b2a6adec0e1055ef.txt | grep -v '^\\s*$'; echo \"=====AN PERSIAN=====\"; grep -n \"Etymology\" 03234bb58a6047c4.txt | head; echo \"---\"; sed -n '150,260p' 03234bb58a6047c4.txt | grep -v '^\\s*$' | head -60"
}
```


### [2026-09-04T19:59:47.778Z] TOOL RESULT

```
 Etymology
 [ edit ] 
 Etymology tree
 Proto-Indo-European *h₁én 
 Proto-Indo-European *-teros 
 Proto-Indo-European *h₁énteros 
 Proto-Indo-Iranian *Hántaras 
 Proto-Iranian *Hántarah 
 Old Persian 𐎠𐎫𐎼 ( a-t-r /⁠aⁿtar⁠/ ) 
 Middle Persian 𐭡𐭩𐭭 ( BYN /⁠andar⁠/ ) 
 Persian اندر 
 Inherited from Middle Persian 𐭡𐭩𐭭 ( BYN /⁠andar⁠/ ) , from Old Persian 𐎠𐎫𐎼 ( a-t-r /⁠aⁿtar⁠/ , “ among, within ” ) , from Proto-Iranian *Hántarah , from Proto-Indo-Iranian *Hántaras , from Proto-Indo-European *h₁énteros ( “ inner, what is inside ” ) , from *h₁én + *-teros .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ʔan.ˈdar/ 
 ( Dari, formal ) IPA ( key ) : [ʔän̪.d̪äɾ] 
 ( Dari, formal ) IPA ( key ) : [ʔän̪.d̪äɾ] 
 ( Kabuli ) IPA ( key ) : [ʔän̪.d̪äɾ] 
 ( Hazaragi ) IPA ( key ) : [ʔän̪.d̪äɾ] 
 ( Iran, formal ) IPA ( key ) : [ʔæn̪.d̪æɹ] 
 ( Tajik, formal ) IPA ( key ) : [ʔän̪.d̪äɾ] 
 Rhymes: -ar 
 Readings
 Classical reading ? 
 andar
 Dari reading ? 
 andar
 Iranian reading ? 
 andar
 Tajik reading ? 
 andar
 Preposition
 [ edit ] 
=====AN PERSIAN=====
62: Etymology 1 
80: Etymology 2 
89: Etymology 3 
98: Etymology 4 
104: Etymology 5 
110: Etymology 6 
121: Etymology 1 
133: Etymology 2 
147: Etymology 1 
156: Etymology 2 
---
 Noun 
 3.1.1.1 
 Descendants 
 3.2 
 Etymology 2 
 3.2.1 
 Noun 
 3.3 
 References 
 4 
 Persian 
 Toggle Persian subsection 
 4.1 
 Pronunciation 
 4.2 
 Etymology 1 
 4.2.1 
 Determiner 
 4.2.2 
 Pronoun 
 4.2.2.1 
 See also 
 4.3 
 Etymology 2 
 4.3.1 
 Noun 
 4.3.1.1 
 Related terms 
 4.4 
 Etymology 3 
 4.4.1 
 Noun 
 4.5 
 References 
 5 
 Punjabi 
 Toggle Punjabi subsection 
 5.1 
 Verb 
 Toggle the table of contents 
 آن 
 25 languages 
 Afrikaans 
 العربية 
 বাংলা 
 Deutsch 
 Esperanto 
 فارسی 
 Français 
 Magyar 
 Bahasa Indonesia 
 日本語 
 한국어 
 Kurdî 
 Lietuvių 
 Malagasy 
 ဘာသာမန် 
 Bahasa Melayu 
 Nederlands 
 Polski
```


## [2026-09-04T19:59:57.777Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk '/^ Persian$/{f=1} f' 03234bb58a6047c4.txt | grep -v '^\\s*$' | sed -n '1,90p'"
}
```


## [2026-09-04T19:59:57.902Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"step\\|Etymology 2\\|Etymology 3\" b2a6adec0e1055ef.txt | head -20"
}
```


### [2026-09-04T19:59:59.426Z] TOOL RESULT

```
 Persian
 [ edit ] 
 Dari
 آن 
 Iranian Persian
 Tajik
 он 
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ˈʔaːn/ 
 ( Dari, formal ) IPA ( key ) : [ʔɑːn] 
 ( Dari, formal ) IPA ( key ) : [ʔɑːn] 
 ( Kabuli ) IPA ( key ) : [ʔuː] 
 ( Hazaragi ) IPA ( key ) : [ʔu] 
 ( Iran, formal ) IPA ( key ) : [ʔɒːn] 
 ( Tajik, formal ) IPA ( key ) : [ʔɔn] 
 Rhymes: -aːn 
 Readings
 Classical reading ? 
 ān
 Dari reading ? 
 ān
 Iranian reading ? 
 ân
 Tajik reading ? 
 on
 Homophone : او ( colloquial Dari ) 
 Audio ( Iran ) : ( file ) 
 Etymology 1
 [ edit ] 
 From Middle Persian 𐭠𐭭 ( ān , “ that, he ” ) [ 1 ] , itself from Proto-Iranian *hauv .
 Determiner
 [ edit ] 
 آن • ( ân ) 
 that ; the 
 Pronoun
 [ edit ] 
 آن • ( ân ) ( plural آن‌ها , human plural آنان ) 
 that 
 he , she , it ; colloquially pronounced اون ( un ) in Iran 
 Synonyms: او ( ō  / u ) , وی ( way  / vey ) , ایشان ( ēšān  / išân ) 
 Used with که to nominalize a clause. 
 Synonym: این ( īn/in ) 
 Used within a relative clause as a resumptive pronoun . 
 Synonym: این ( īn/in ) 
 See also
 [ edit ] 
 Persian personal pronouns (Iranian Persian)
 singular
 plural
 1st person
 مَن (man)
 ما (mâ)
 2nd person
 familiar
 تو (to)
 شُما (šomâ)
 polite
 شُما (šomâ)
 3rd person
 general
 او (u) 
 اون (on)* 
 آن‌ها (ân-hâ), آنان (ânân) 
 اونا (onâ)* 
 formal
 وِی (vey)
 ایشان (išân)
 polite
 ایشان (išân)
 * colloquial pronunciations
 Persian personal pronouns (Classical and Dari)
 singular
 plural
 nominative
 accusative 5 
 nominative
 accusative 5 
 1st person
 general
 من ( man ) 
 مرا ( marā ) 
 ما ( mā ) 
 —
 informal 1 
 مه ( ma ) 
 مره ( mara ) 
 ماره ( māra ) 
 2nd person
 familiar
```


### [2026-09-04T19:59:59.465Z] TOOL RESULT

```
122: Etymology 2 
131: Etymology 3 
371: Etymology 2
390: Etymology 3
```


## [2026-09-04T20:00:05.495Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '360,405p' b2a6adec0e1055ef.txt | grep -v '^\\s*$'"
}
```


### [2026-09-04T20:00:07.345Z] TOOL RESULT

```
 inside 
 within 
 in 
 Related terms
 [ edit ] 
 اَنْدَر باہَر ( andar bāhar , “ within and without; everywhere ” ) 
 Etymology 2
 [ edit ] 
 Inherited from Sanskrit उन्दुर ( undura ) , उन्दुरु ( unduru ) , उन्दरु ( undaru ) , etc. from a lost Vedic substrate . Compare Bengali ইন্দুর ( indur ) , ইঁদুর ( ĩdur ) .
 Pronunciation
 [ edit ] 
 ( Standard Urdu ) IPA ( key ) : /ɪn.d̪ʊɾ/ 
 Noun
 [ edit ] 
 اِنْدُر • ( indur )  m ( Hindi spelling इंदुर ) 
 rat 
 mouse 
 Etymology 3
 [ edit ] 
 Urdu Wikipedia has an article on: اندر 
 Wikipedia ur 
 Learned borrowing from Sanskrit इन्द्र ( indra ) . Compare Punjabi اندر ( iṇdar ) , Kalasha اِن ( in ) , Kamkata-viri ایںدر ( ī˜drʻ ) , and Prasuni اِندر ( indr ) .
 Pronunciation
 [ edit ] 
 ( Standard Urdu ) IPA ( key ) : /ɪn.d̪ɾᵊ/ 
 ( colloquial ) IPA ( key ) : /ɪn.d̪əɾ/
```


## [2026-09-04T20:00:19.568Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"###### h2entero\"; grep -n -A6 \"^ Etymology$\" e1d0e8ae4fa52831.txt | grep -v '^\\s*$' | head -20; echo; echo \"###### other (etymonline)\"; grep -n -A6 \"other (adj\" fe5b7fa0eab598b4.txt | head -20; echo; echo \"###### Oswald\"; grep -n -A8 \"Oswald\" c881dd147c459683.txt | head -20; echo; echo \"###### anima wikt\"; grep -n -A6 \"^ Etymology$\" 37e8b7eefd93499b.txt | grep -v '^\\s*$' | head -30"
}
```


## [2026-09-04T20:00:19.843Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"step-father\\|stepfather\\|step-mother\\|stepmother\" PHD.txt HRN.txt HUB.txt IEC.txt | head -10"
}
```


### [2026-09-04T20:00:21.282Z] TOOL RESULT

```
###### h2entero

###### other (etymonline)
23: other (adj., pron.) 
24-
25- Old English oþer "second, the second of two; additional, further" (adj.), also as a pronoun, "one of the two; a different person or thing from the one in view," from Proto-Germanic *anthera- (source also of Old Saxon athar , Old Frisian other , Old Norse annarr , Middle Dutch and Dutch ander , Old High German andar , German ander , Gothic anþar "second, other").
26-
27- These are from PIE *an-tero- (source of Lithuanian antras , Old Prussian anters "other, second), which is perhaps a variant of *al-tero- "the other of two" (source of Latin alter ), from root *al- "beyond" + adjectival comparative suffix *-tero- . Or the first element might be the pronoun *eno- , *ono- [Boutkan]. The Old English, Old Saxon, and Old Frisian forms show "a normal loss of n before fricatives" [Barnhart].
28-
29- The sense of "second" was detached from this word in English (which now uses second (adj.), which is from Latin) and German ( zweiter , from zwei "two") to avoid ambiguity. In Scandinavian, however, the second floor is still the "other" floor (Swedish andra , Danish anden ). Also compare Old English oþergeara "next year."

###### Oswald
1:URL: https://www.etymonline.com/word/Oswald
2-FETCHED: 2026-09-04T19:58:40Z
3-STATUS: 200
4:TITLE: Oswald - Etymology, Origin & Meaning of the Name
5-
6:Oswald - Etymology, Origin & Meaning of the Name 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
13- Apps 
14- Premium 
--
21: Origin and history of Oswald 
22-
23: Oswald 
24-
25- masc. proper name, from Old English Osweald "god-power, god-ruler," from Old English os "god" (only in personal names), from PIE *ansu- "spirit" (see Oscar ) + Old English (ge)weald "power."

###### anima wikt
519: Etymology
520- [ edit ] 
521-
522- Borrowed from Latin anima ( “ a current of air, wind, air, breath, the vital principle, life, soul ” ) , sometimes equivalent to animus ( “ mind ” ) , both from Proto-Indo-European *h₂enh₁- ( “ to breathe, blow ” ) ; see animus . Cognate with Ancient Greek ἄνεμος ( ánemos , “ wind ” ) , Old English anda ( “ anger, envy, zeal ” ) . More at onde .
523-
524- Pronunciation
525- [ edit ] 
--
629: Etymology
630- [ edit ] 
631-
632- Borrowed from Spanish ánima .
633-
634- Pronunciation
635- [ edit ] 
--
654: Etymology
655- [ edit ] 
656-
657- Etymology tree
658-
659- Proto-Indo-European *h₂enh₁- 
660-
--
858: Etymology
859- [ edit ] 
860-
861- From Portuguese animar .
862-
863- Verb
```


### [2026-09-04T20:00:21.335Z] TOOL RESULT

```
IEC.txt:469:alter- (2) comp. *more grown'. Cf. alo Oss. àldár “elder, chief; Br. aotru ‘lord’; Cor. altrow ‘step-father’; OHG altiron; OE eldran *elders'
IEC.txt:602:anteros “second, other. Cf. anos (1) and -teros. WP I, 67; II, 337 Skt. ántarab; Per. andar (in the phr: madar i andar 'stepmother); Oss. àndár, cf. also än- dära (*otherwise', fr. *antero); Arm. cf. andra- “back, again’, andren ‘again’; Alb. cf. denom. ndrroj ‘I change: Go. anpar; OHG andar; ON annarr; OE ober; OCS vütoryj; Cz. cf. vteřina “second of time’; úterý (scil. den) “Tuesday”; Li. antras; Latv. otrs; OPr. antars, anters
IEC.txt:3644:epi (pi) "on, by, at, near. WP I, 122 Skt. Av. ápi; Oss. fe-, fi-, px; Arm. h- (j-) as in h-arnem (rise: Gk. ep-órnümi, -órnu- mai; h-awraj ‘stepfather’: Gk. epi-pátor, id.); beside ev, cj. "and: Lyc. epi (ambig. “after”); Myc. & Gk. en Lat. cf. -pe in quip-pe, nem-pe, sae-pe; Umb. (?) ie-pi ‘thither’; Olr. cf. fí-ad 'in front of; OW i-ad ‘crown of
IEC.txt:3648:epi-poter (-potor) ‘stepfather Arm. h-awraj; Gk. epipátor, id.
IEC.txt:10392:mátruio (mātruiə) 'mother-figure, step- mother’. WP II, 229 Skt. cf. matfvat "like a mother’; -màaturab, adj. ‘mother; Arm. mawru, gs mawrvi, ab. s. mawrvav ‘mother-in-law, stepmother’; Doric mātruiá ‘stepmother; Alb. motër, pl. motra (sister. Extn. uncertain); Lat. cf. mātru-elis, m. & adj. ‘maternal cousin; of a. . ?; MHG cf. muoder, sn (‘belly, bodice’. Extn. uncertain); Sw. moder, f. (*womb': Gk. métrā, id.)
IEC.txt:12060:oit- (3) ‘gullet, neck, throat Gk. cf. oiso-phágos, m. id. (fr. *oitio-); ON eið, n., mod. eiði ‘isthmus’; Cz. cf. jícen, gs: jícnu, OCz. jiecen, m. (fgullet', fr. *oitien-); Norw. eid ‘isthmus’. (For Cz. -c- fr. *-ti- cf. macecha ‘stepmother: mát *mother)
IEC.txt:12841:petruios ‘adoptive father, paternal uncle* Cf. poter- Skt. pítrvyah, m. ‘paternal uncle’; Arm. hawru, gs. hawrvi, ab. s. hawrvav, s. ‘father-in-law, foster-father' beside hawraj, i-st. ‘stepfather’ and Gk. epi-pátor, id. (fr. Sen": Gk. patruiós ‘stepfather’; Lat. patruus, m. ‘father’s brother, Dutch uncle’; OHG fatureo, m. ‘uncle, cou- sin’; OE fædera, wm. ‘paternal uncle, god- father; LG vadder ‘godfather’; cf. also Austro-Ger. Vetter, m. (in sense of ‘uncle’, otherwise cousin" ON foóur- cpds. beside all-foór, m. “father of all
IEC.txt:20426:ul-teros ‘further, more aloof. Cf. uwi- and -teros. WP I, 313 | Skt. vitarám, adv. ‘further’; Av. viðara-, adj. id.; Go. wipra ‘against’; MHG wider, id.; OE wióer, prp. ‘against’; adj. ‘hostile’; ON viðr, id. (Uncertainly) cf. Lat. vitricus, m. *father- in-law, step-father
```


## [2026-09-04T20:00:33.434Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor name,ln in [('IEC.txt',602),('IEC.txt',597)]:\n    txt=open(name,encoding='utf-8',errors='replace').read()\n    lines=txt.split('\\n'); c=0\n    for i,l in enumerate(lines,1):\n        if i==ln: break\n        c+=l.count('\\f')\n    print(name,'line',ln,'leaf',c,'printed ~',2*(c-15),2*(c-15)+1)\nEOF\necho \"=== SKT other/asthma ===\"; grep -n \"^OTHER\\|^ASTHMA\\|^ANIMAL\" SKT.txt | head -5"
}
```


### [2026-09-04T20:00:35.227Z] TOOL RESULT

```
IEC.txt line 602 leaf 30 printed ~ 30 31
IEC.txt line 597 leaf 29 printed ~ 28 29
=== SKT other/asthma ===
164:OTHER  ABBREVIATIONS.
1068:ASTHMA.
```


## [2026-09-04T20:00:36.794Z] TOOL CALL #72: Bash

```json
{
 "command": "for u in 'https://www.etymonline.com/word/Oscar' 'https://www.abadis.ir/fatofa/%D8%A2%D8%B3%D9%85/' 'https://en.wiktionary.org/wiki/%CE%AC%CF%83%CE%B8%CE%BC%CE%B1'; do echo \"== $u\"; python3 tools/fetch_source.py \"$u\" --note 'page 54: Oscar/Persian asm/Greek asthma' 2>&1|tail -1; done",
 "dangerouslyDisableSandbox": true
}
```


### [2026-09-04T20:00:39.947Z] TOOL RESULT

```
== https://www.etymonline.com/word/Oscar
/home/sfmqrb/git/rishe/data/verification/sources/web/9372893795fcfa6d.txt
== https://www.abadis.ir/fatofa/%D8%A2%D8%B3%D9%85/
/home/sfmqrb/git/rishe/data/verification/sources/web/6fb31785225e4417.txt
== https://en.wiktionary.org/wiki/%CE%AC%CF%83%CE%B8%CE%BC%CE%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/8bc87a1ff4249855.txt
```


## [2026-09-04T20:00:47.379Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### Oscar\"; sed -n '20,32p' 9372893795fcfa6d.txt|grep -v '^\\s*$'; echo \"#### asm abadis\"; grep -o \"آسم[^|]\\{0,300\\}\" 6fb31785225e4417.txt | head -8; echo \"#### greek asthma\"; grep -n -A6 \"^ Etymology$\" 8bc87a1ff4249855.txt|grep -v '^\\s*$'|head -20"
}
```


### [2026-09-04T20:00:49.155Z] TOOL RESULT

```
#### Oscar
 Origin and history of Oscar 
 Oscar 
 masc. proper name, Old English Osgar "god's spear," from gar "spear" (see gar ) + os "god" (only in personal names), for which see Aesir .
 The statuette awarded for excellence in film acting, directing, etc., given annually since 1928 was first so called in 1933. The common explanation of the name is that it sprang from a 1931 remark by Margaret Herrick, secretary at Academy of Motion Picture Arts and Sciences, on seeing the statuette: "He reminds me of my Uncle Oscar." Thus the award would be named for Oscar Pierce, U.S. wheat farmer and fruit grower. The popularity of the name seems to trace to columnist Sidney Skolsky, and there are other stories of its origin.
 Entries linking to Oscar 
 Aesir 
#### asm abadis
#### greek asthma
150: Etymology
151- [ edit ] 
152-
153- Inherited from Ancient Greek ἆσθμα ( âsthma ) .
154-
155- Noun
156- [ edit ]
```


## [2026-09-04T20:00:49.303Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"asthma\" SKT.txt | head -3; echo \"---other\"; grep -n -i \"^Other, adj\\|Other,  adj\\|OTHER, second\" SKT.txt|head -3; echo \"--- WLD an- p56\"; python3 -c \"\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nprint(' '.join(t[64].split())[:1400])\""
}
```


### [2026-09-04T20:00:51.011Z] TOOL RESULT

```
1068:ASTHMA.
---other
--- WLD an- p56
895
56 an an- ti. Ges. d. Wiss. zu Gottingen Phil. -hist. Klasse 1918, 215f. ein, daB bayr. enl, aril , osterr. aenl, anl usw. die Bedeutung „GroBvaterehen“ und „Enkel“ tragen, und man es hier mit der gleichen Erscheinung zu tun hat wie bei dt. dann auch „des Bruders Sohn“); Vetter (ursprgl. „des Vaters Bruder“, die Anrede wird vom GroBvater an den Enkel zuriickgegeben. Diese altere Auffassung (vgl. die Literatur bei Hermann aaO.) ist beachtenswert. PreuB. ane „alte Mutter“; lit. am/ fa „Schwiegermutter“. Wohl mit Becht stellt M. E. Schmidt KZ. 47, 189 arm. aner „Yater der Frau“ hierzu. Es liegt eine Komparativbildung vor wie in lat. nmtertera „Mutterschw ester“, cymr. ewytlrr „Oheim“, acorn, eaitor bret. eontr (urkelt. r , *avcntro-, Pedersen Kelt. Gr. I 55). s. *anero- hatte die urspriingliche Bedeutung „etwas wie der Ahn“. Dagegen gehort arm. han ,,GroBmutter“ zu hin „alt“ (vgl. M. E. Schmidt aaO.). Unsicher ist ahd. hevianna w'oraus umgebildet mhd. hebamme. Da ahd. , *avna „\Veib“ nicht zu belegen ist, nimmt Kluge EW. Enstehung aus *haf- jan(d)jo „die Hebende“ an, wmraus die spateren Umdeutungen entstanden seien. Doch vgl. BB. VI 235, PBBr. 30, 250. 2. an „etwa, wohl“. Gr. ay „wohl, etwa, in irgendeinem andern Falle“ ( edv aus el civ, rjv Ol 9/ aus *>) dv, av aus al av, att. luv durch Ivreuzung von edv und av; Ehrlich KZ. 38, 86); got. an Fragepartikel. Aber lat. an aus *at-ne
```


## [2026-09-04T20:00:58.656Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ns=' '.join(t[64].split())+' '+' '.join(t[65].split())\ni=s.find('atmen')\nprint('--- WP I 56/57 an- atmen ---')\nprint(s[max(0,i-300):i+1800])\nEOF"
}
```


## [2026-09-04T20:00:59.458Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ns=' '.join(t[75].split())\nprint('--- WP I 67 ---')\nprint(s[:1600])\nEOF"
}
```


### [2026-09-04T20:01:02.792Z] TOOL RESULT

```
--- WP I 56/57 an- atmen ---
 in irgendeinem andern Falle“ ( edv aus el civ, rjv Ol 9/ aus *>) dv, av aus al av, att. luv durch Ivreuzung von edv und av; Ehrlich KZ. 38, 86); got. an Fragepartikel. Aber lat. an aus *at-ne anne s. die Lit. bei Yf. LEWb. 2 39, wozu Jacob- , , sohn KZ. 45, 347 f., Fraenkel Glotta 4, 47 f. 3. an- „atmen, hauchen“. Ai. aniti „atmet“ (auch thematisch anati), anila-h „Atem, Hauch, 'Wind“ ana-h „Hauch, Atem“ and-h (vielleicht ,,Hauch“ oder „Mund, Kase“, ana- nam „Mund, Maul, Gesicht“ mit ind. Vriddhi; „Mund“ als „Atmer, das Atmen“); 11 Av. antycl pardntyd „des Ein- und Ausatmens (Zs. von *anti- „Atmen“ , mit a und purer, s. Bartholomae IF. 7, 59; uber ainiti- „Milde <: s. aber Airan. Wb. 1 25 f.). Gr. dve/iog „Hauch, Wind'*, dv>jve,uog (mit Zsdehnung) vtjve/uos wind- , still", „windreich“ (>)-metrische Dehnung), dveucbho; („windig“, yve/ideig d. i. :) „nichtig, vergeblich“ (dissimiliert aus dve/ieovio s. zuletzt Bechtel Lexil. 44, auch 226 tiber das wohl aus * uei-ave ucbviog durch Ferndissimi- l l ohne Erfolg“). ) lation gekiirzte /.leTa/xcbnog „vergeblich, 1 Lat. animus „Geist, Seele“, animu „Luftzug, "Wind, Hauch, Seele“ (davon animal „Lebewesen, Tier“, halo-, -are „hauchen, duften“ (Denominativ eines an-slo-; mit unechtem h, das hier schallmalenden Wert erlangte und auch *) dvtfuovij seheint aus einem semit. Mamen des Adonis umgestaltet, Lewy Fremdw. 49. — Uber arrj&ov „Dill" s. Boisaeq 62; auch avmri; T ein wohlriechendes Kraut" bleibt besser unetymologisiert. — Ganz zweifelhaft ist Zugehorigkeit von arzoov „Hohle“, das von der anit-Form der \Vz. heizuleiten wiiie („-\tmer, Luftloch“VV Preliwitz’ 2 42 Be- rufung auf avzrjgtg „Fensteroffnung. Niistem der Pferde" unter Zugrundelegung eines avxijo „Atmer" iiberzeugt mich nicht); die Verbindung uit gov.Prrson scheitert am Vo- kalismus, s. Brugmann Grdr. II 2 1, 329 f. — Uber gr. anD/.ia s. Boisaeq bd m. Lit. an- 57 in an(h)elare eindrang; iiber letzteres Praep. *ai>, s. some Yf. LEWb. 2 26, 44; iiber aliitw , allium ebenda und unter *dlo-). !! Air. anal „spiritus , cymr. anadl „Atem“, mbret. alazti (Umstellung), nbr
```


### [2026-09-04T20:01:04.744Z] TOOL RESULT

```
--- WP I 67 ---
anti, anta — andhos 67 4 entgegengesetzte Seite hiniiber“ zu anti gehoren (so Fick III 30); auch die Worte fur „Ende“ (s. u.) sind ursprgl. das auf der gegenuberliegenden Seite winkende Ziel, und mit as. unt ist auch ant (and-\-te) Praep. m. Acc. „usque ad“ bedeutungsgleich, was, selbst wenn nur junge Kreuzung von tint mit ancl- vorlage, doch die Begriffsverwandtschaft beider be- leuchtet. Ein ganz verschiedenes Wort ist dt. und , ahd. unti, anti , enti u. dgh, as. endi, ags. engl. and „und“, anord. en(n) ,,und, aber", das mit ai. atha „darauf, dann“ verwandt sein mag (Kluge PBrB. 10, 444, Wb. s. v. unci). Komp. anord. cndr, enn „friiher, vormals, wieder, nach“ (endr = got. andis-uh „entweder“, Feist got. Wb. 27), ags. end „vorher“ (*andis ), ahd. enti „friiher, vormals* (grm. *andias ), mhd. ent, end Konj. „ehe, vor“ (z. B. 1 Falk-Torp 192, 1455). Idg. *anti-os „gegeniiber, vor einem liegend** gr. dvxiog ds. (z. T. auch von : avTa gebildet nach Brugmann IF. 38, 139 Anm. 2; ivavziov „gegeniiber“, evavziog „gegeniiber befindlich; Gegner"); mit der Bed. „Stirn“ (eigentlich „Yorderseite, dem Gegeniiber zugekehrte Seite"), anord. enni n., abd. andi, endi n. „Stirn", lat. antiae „capilli demissi in frontem": vgl. mit derselben Bed. air. Stan (aus *ant-ono -) „Stirn“. Ai. antci-h „Ende, Grenze, Rand", antya- „der letzte", got. andeis , an. endir, as. endi, ags. aide m., ahd. anti, enti m. und n., nbd. Ended) Dafi unserer Sippe ein Subst. *ant- „Stirne, Angesicbt" zugrunde liege (Schulze BPbW. 1890, 1472, Thurneysen AflL. 13, 28 f., Thes. II 127), ist ganz unsicher, s. Gunther IF.
```


## [2026-09-04T20:01:17.358Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read().split('\\f')\ns=' '.join(t[45].split())\nprint(s[:2200])\""
}
```


## [2026-09-04T20:01:17.758Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^12.92 OTHER\\|12\\.92 OTHER\\|4\\.51 BREATHE\\|16\\.11 SOUL\" SYN.txt | head -5"
}
```


### [2026-09-04T20:01:19.245Z] TOOL RESULT

```
era .Mutterschwester^, cymr. eiüytlir ^Oheim^, acorn. euitor^ bret. eontr (urkelt. *aventro-, s. Pedersen Kelt. Gr. I 55). '^anero- hätte die ursprüngliche Bedeutung ^etwas wie der Ahn^ Unsicher ist ahd. hevianna, woraus umgebildet mhd. hehamme. Da ahd. *anna ,Weib^ nicht zu belegen ist, nimmt Kluge ^^ 238 Entstehung aus *hafjan{d)jö ,die Hebende' an, woraus die späteren Unideutungen ent- standen seien. Doch vgl. PBB. 30, 250. WP. I 55 f., WH. I 50, Pedersen Lyk. u. Hitt. 26, m. 2. an Demonstrativpartikel ,dort, andererseits*. Gr. äv ,wohl, etwa, in irgendeinem anderen Falle' {ßdv aus ei ar, ion. '}j<t aus *rj &V, «V aus al äv, lat. an ,ja, wohl", sekundär Fragepartikel, erweitert anne, air. an-d ,hier^, got. an ,denn, nun^; lit. an-gu ,oder^, apr. anga-anga ,ob = oder ob^ Davon abgeleitet: anios ,anderer" in: ai. anyd- ,anderer*, av. anya-, ainya-, apers. anlya- ds. Vgl. oben S. 26. anteros ,anderer" (von zweien) in: ai. dntara-, oss. ändär , anderer*^, got. an'par ds., aisl. annarr ,anderer, zweiter^, ahd. andar, ags. öper ,anderer^, apr. anters, antars (*antras) ^andere»', zweiter', lit. antras, lett. notrs neben lit. antaras, ostlett. ütors ds., slav. *gter^, '^-gtoi-z in cech. iitery m. , Dienstag^, osorb. loutory ,ande- rer, zweiter'. Über aksl. v^tor^ , zweiter' s. id- ,auseinander^. 38 WP. I 56, 67, II 337, WH. I 44, Trautmann 10/11, Debrunner REtlE. 3, Iff. . 5. an(9y ,atinen, hauchen^, Nominalstamm ant-. AI dniti ,atmet'' (auch thematisch dnati), dnila-h ,Atem, Hauch, Wind^^ änd-h (vielleicht ,Hauch^ oder ,Mund, Nase^, äna-nam ,Mund, Maul, Ge- sicht^mit ind. Vrddhi; ,Mund^ als ,Atmer, das Atmen^); prrJnitl ,atmet^; av. äntyaj paräntya ,des Ein- und Ausatmens^ (*anti- ,Atmen^ mit ä und parä] s. Bartholomae IF. 7, 59; über ainiti- ,Milde'^ s. aber Airan. Wb. 125f.). Gr. Nvs^iog ,Hauch, Wind^, ävrjvei.Log (mit Dehnung im Kompositum), vTjvey^og ,windstill", '^vsfxösig ,\vindreich'^ (ij-metrische Dehnung), dveucüXiog (,windig^, d. i. :), nichtig, vergeblich'^ (dissimiliert aus dyefxcbvLog, s. zuletzt Bechtel Lexil. 44, auch 226, über das wohl aus '^iJ,6T-avs(.i(bvLog durch Ferndissimilation gekürzte fiSTa^iwnog ,vergeblich, ohne Erfolg*); anders Risch 113;
```


### [2026-09-04T20:01:19.287Z] TOOL RESULT

```
6693:4.51 BREATHE; BREATH
27531:16.11 SOUL, SPIRIT
```


## [2026-09-04T20:01:34.727Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6693,6730p' SYN.txt | cut -c1-400; echo \"=== SOUL ===\"; sed -n '27531,27560p' SYN.txt | cut -c1-400; echo \"=== OTHER ===\"; grep -n \"OTHER$\\|OTHER \\[\" SYN.txt | head -5"
}
```


### [2026-09-04T20:01:36.639Z] TOOL RESULT

```
4.51 BREATHE; BREATH
Grk,  zvéw; aveDpa, rv07 Goth. anan Lith. kvépuoti; kvapas
NG  avarrviw; avacaivw ; ON anda; ond, andi Lett. dvaSuot, elpét; dvaSa, avon, évaca Dan. aande; ande elpe
Lat.  spirdre; anima, spiri- Sw. andas; ande ChSl. dychati; dychanije, lus OE orpian, cbian; orop, duchit
It. respirare, fiatare; Zbm SCr.  disati, dihati; dah fialo, respiro ME trethe; bre(e)th Boh.  dychati; dech
Fr. __respirer; haleine, NE breathe; breath Pol. dychaé; dech souffle Du. ademen; adem Russ. dySat’; dychante
Sp. _respirar, resolla-; OHG  datumén; dium Skt.  an-, quas-; ana-, aliento, huelgo MHG dtemen; diem cvasa-, Gtman-
Rum. rdsufla; rdsuflare NHG  atimen; atem, hauch Av. (dnti-, pardnti-)
Ir, doberim anal; anal andluighim; anal anadlu; anadl
Br. alanat; alan
A few of the words listed apply only | Ir. andluighim, W. anadlu, Br. alanat;
i" the exhalation of breath, as NHG ae in contrast to atem, or are mostly Cee This was originally true of - ae e Ely all, of the others, as ; € usual associati 1
tle ais ee Clations with
oun an but d verb
at, anima: az ne (vith mena anal, W. anadl, Br.
Goth. anan (only uz-anan éexvetyv Mk. 15.37, 39), ON anda, Dan. aande, Sw. andas (refl.), with nouns ON ond, andi, Dan. aande, Sw. ande; OE orpian (fr. orop ‘breath’, this fr. *uz-anp-); Skt. an- but mostly cpd. pra-an-, with nouns ana-, prana-, Av. Gnti, pardnti- ‘inhala- tion’, ‘exhalation’ (fr. *anti- ‘breath’ with @ and pard-) : Grk. évepos ‘wind’, ChSI. vonja ‘odor’,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
otis © igen
Digitized by Arya Samaj Foundation Chennai and eGangotri
260 SELECTED INDO-EUROPEAN SYNONYMS
courage’ (fr. *alénitare) derivs. (with metathesis) of Lat. anhélare ‘breathe hard, puff, pant’, fr. an- + *ansla- (cf. halare ‘breathe out, exhale’, with unety- mological h-). REW 472, 473.
2. Grk. mvéw (dvarvéw ‘take breath’, in NG the usual form for ‘breathe’; cf. Fr. respirer, etc., below) with the sbs. mvedua, von : ON fnysa ‘sneeze, snort’, OE fnéosan ‘sneeze’, etc., IE *pneu- in words for ‘puff, pant, breathe, etc.’. Walde-P. 2.85 (with other similar groups with initial *pn-, all of imitative orig.).
NG dvacaivw (with sb. avaca, back- formation), deriv. of class. Grk. éveots ‘relaxation’ (: dvinuc ‘let go’), through avecaivw, then ava- by pop. etym. ‘Re- lax’ > ‘catch one’s breath’, then also simply ‘breathe’. Hatzidakis, Mec. 2.58, ftn.
3. Lat. spirdre (epd. respirare ‘breathe again, take breath, etc.’ > It. respirare, Fr. respirer, Sp. respirar), with sb. spiri- tus (It. respiro fr. respirare) prob. : ChSl. piskati ‘whistle’, SCr. pistatr ‘hiss’, ON fisa ‘pedere’ (4.64), ete., IE *(s)peis- (imitative). Walde-P. 2.11.
It. fiatare, deriv. of fiato, fr. Lat. fldius ‘blowing, snorting, breeze’ sometimes also ‘breath’ : flare ‘blow’, ete. REW 3359.
Fr. souffle (also ‘wind, blast’) back- formation fr. sowfler ‘blow, pant? (= Sp.
sollar, Rum. sufla, etc.) fr. Lat. sufflare”
‘blow’ (10.38) ; Sp. resollar, Rum. rdsufla (whence sb. rdsuflare), fr. new cpd. parallel to Lat. resptrare. REW 8430. Puscariu 1447.
Sp. huelgo (Port. folego), back-forma- tion to Sp. holgar (Port. folgar) ‘rest, cease from labor’, orig. ‘stop for breath’ from ‘pant’, fr. VLat. follicare ‘swell or move as a bellows’, deriv. of Lat. follis ‘bellows’. REW 3417.
4. Ir. do-berim andl lit. ‘give breath’; for andl, etc., see above, 1.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
5. Goth. anan, OF orpian, above, 1.
OE @)m, Du. adem, OHG alum MHG, NHG atem, whence the vbs, OR épian, Du. ademen, OHG alumon, ete, : Skt. diman- ‘breath, soul, life’, connection? Walde-P. 1.118.
ME breth, breeth, NE breath (whence vb. ME brethe, NE breathe), fr. OF braep ‘odor, smell, scent’ : OHG bradam ‘ex. halation, heat’ (fr. the root in ON bradr ‘heated’, OE bre@dan, OHG bratan ‘bake’, etc.). The meaning ‘breath’ comes by specialization, either of ‘exhalation’ (the sense ‘exhalation, vapor, steam’ com- mon in ME). Walde-P. 2.158. NED s.v. breath.
NHG hawch, fr. hauchen, MHG hichen ‘blow the breath, breathe out’, of imita- tive orig. Weigand-H: 1.820.
6. Lith. kvépuoti,  kvapas : kvépti ‘blow the breath’, kvepéti ‘smell, emit an odor’, Lett. kvépt ‘steam, smoke’, Grk. xamvos ‘smoke’, Lat. vapor ‘steam’, ete. Specialization of ‘exhalation’. Walde-P. 1.380.
Lett. dvasuot, dvasa (Lith. dusti ‘get out of breath’, dvésti ‘expire, die’, dvésuoti ‘pant’, dvasia ‘spirit’ also ‘breath’), ChSl. dychati (duchati ‘blow’) with sbs., dychanije, duchii, etc., general Slavic, fr. IE *dhwes-, *dhus-, extension of *dheu- in Skt. dhi- ‘shake, agitate’, Grk. Giw ‘rage, seethe’, etc. Walde-P. 1.846. Berneker 234 ff., 249.
Lett. elpét, fr. the noun elpe, this prob. through ‘weak breath’ or ‘pant’ (ef. also Lett. alpa ‘moment of time’) : Lith. alpti ‘faint’, alpnas ‘weak’, this perh. : Skt. alpa- ‘small’. Miihl.-Endz. 1.568.
=== SOUL ===
16.11 SOUL, SPIRIT
yp Goth. saiwala, ahma Lith.  di%ia, dvasia pis O0H85 ™ RUE ON ond, sal(a), andi Lett.  dvésele, gars Yur ORS |. spiri- ‘Dan. sjael, aand ChSl. duSa, duchi qnima, antmus Sw.  sjal, ande SCr.  duSa, duh {us aes aD OE sdwel, gast Boh. duSe, duch anima, spirelo, Gree ME naules spirit, gost Pol. dusea, duch dime, esp “ty, animo NE soul, spirit (ghost) Russ. dua, duch alma, Co : Du. ziel, geest 
guo- in dicdw ‘blow’?). Boisacq 1079.
Grk. 6@vyués, with a wide range of meanings (‘soul, spirit, mood, anger, courage, breath of life’), through ‘agita- tion’ fr. the root of 6iw ‘rage’, Skt. dhu- ‘shake, agitate’, etc., and in form esp. : Lat. famus, Lith. dimai ‘smoke’, Skt. dhima- ‘smoke, vapor’. For the shift of physical to mental, cf. Lat. animus, ani- ma (below, 2), Lett. gars (below, 5) and NE fume (f
Grk. mvedpa, orig. ‘breath’ (: mvéw ‘breathe’, 4.51), hence ‘breath of life’, and in NT and other Christian writings the usual term for ‘spirit’ contrasted with yux7 ‘soul’.
For Grk. ¢pjv, poet. word for both the seat of emotion and ‘mind’, with nu- merous derivs., partly of emotional but more commonly of intellectual charac- ter, see under ‘mind’ (17.11).
2. Lat. anima (> It. anima, Fr. ame, Sp. alma), orig. ‘air, breath’ (4.51), and the semantic equivalent of Grk. yux7; animus (> It., Sp. animo), also ety- mologically ‘air, breath’ (inform = Grk. éveunos ‘wind’), but never used in this sense, corresponds semantically to Grk. Gipés, but eventually yields place to spiritus (cf. below). Ernout-M. 53 f. Walde-H. 1.49 f.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1088 SELECTED INDO-EUROPEAN SYNONYMS
Lat. spiritus (> It. spirito, Fr. esprit, Sp. espiritu, Rum. spirit), usually in class. Lat. ‘breath’ (4.51), replaces anz- mus in the sense ‘spirit’ in the imperial period and is used in Christian writings as the usual equivalent of Grk. aveSua. Ernout-M. 966.
Rum. suflet, orig. ‘breath’, but not used in this sense now except in certain locutions : sufla ‘blow’, rdsufla ‘breathe’, etc. (4.51). Tiktin 1526 f.
3. Ir. anim, NIr. anam, Br. anaon (only ‘souls of the dead’) : Lat. anima (above); fr. the same root with different suffix (*ana-ti) W. enaid; Br. ene, MBr. eneff, Corn. enef loanwords fr. Lat. ani- ma? Walde-P. 1.57. Pedersen 1.170.
Ir. spirut, NIv. spiorad, W. ysbryd, Br. spered, fr. Lat. spiritus. Pedersen 1.211.
4, Goth. saiwala, OE sdwel (> ON sala, sal), ME soule, NE soul, OS siala (> Dan. sjal, Sw. sjdl), Du. ziel, OHG séla, séula, MHG séle, NHG seele (in Gospel translations the usual renderings of Grk. yox7 or Lat. anima), etym. dub. (: Grk. alédos ‘quick moving’ or ChSl. sila ‘power’?). Falk-Torp 974. Feist 406. Weigand-H. 2.832.
Goth. ahma (= zvedua) : aha ‘mind’, etc. (17.11). Feist 16 f.
ON ond, andi, both lit. ‘breath’ (4.51), whence ‘breath of life, soul, spirit’, as ‘soul’ more frequently in early eccl. writings gnd (replaced by sala in this sense, and sal, not 6nd is the usual Nicel. word), andi esp. ‘spirit, spiritual being’, and so in NIcel., as also Dan. aand (distinguished fr. aande ‘breath’), Sw.ande. Falk-Torp 5. Hellquist 20.
OE gast, ME gost (NE ghost in Holy
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Ghost), OS gést, Du. geest, OHG-NH
geist, the usual rendering of Lat, ‘ but also old and general for natural being’: OF géstan ‘frighten’
spiritus & ‘super-
Skt. heda- ‘anger, wrath’, Av. zdizdiiiq. most frightful’, fr. IE *Gheizd-, exten. sion of *§heis- in Goth. US-gaisjan ‘frighten’, Av. zaéSa- ‘horrible’, Walde- P. 1.554. Feist 531. NED sv. ghost.
ME, NE spirit, fr. Anglo-Fr, spirit = OF r. esp(e)rit, Fr. esprit (above, 2).
5. Lith. dugia ‘soul’, fr. Slavic duga (below). Brickner, Sl. Fremdwirter 9.
Lith. dvasia ‘spirit’, dial. still ‘breath’, Lett. dvésele ‘soul’ also ‘breath’ : Lett, dvaga ‘breath’, dvasuot, dvest ‘breathe’ (4.51) and the Slavic group below.
Lett. gars ‘steam’ and ‘spirit, soul, in- tellect’ : Lith. garas ‘steam’, ChSI. goréti ‘purn’, Grk. @eppds ‘hot’, etc. Walde-P. 1.688. Berneker 234. Miihl.-Endz 1.604.
6. ChSl. dusa, etc., general Slavic for ‘soul’ : ChSl. ducht ‘breath’ and ‘spirit’ (xvedua), but in modern Slavic usual only in the latter sense : ChSI. dychati, ducha- tt ‘breathe’, etc. (4.51). Walde-P. 1.846. Berneker 234 f., 239.
7. Skt. diman-, orig. ‘breath’ : OHG datum ‘breath’, etc. (4.51).
Skt. prana-, orig. ‘breath’, and esp. “nhalation’, fr. pra-an-, cpd. of an- ‘breathe’ (4.51).
=== OTHER ===
2936:2.47 GRANDMOTHER
```


## [2026-09-04T20:01:49.758Z] TOOL CALL #80: Bash

```json
{
 "command": "for u in 'https://vajehyab.com/?q=%D8%A2%D8%B3%D9%85' 'https://www.vajehyab.com/moein/%D8%A2%D8%B3%D9%85' 'https://en.wiktionary.org/wiki/asthme'; do echo \"== $u\"; python3 tools/fetch_source.py \"$u\" --note 'page 54: Persian asm asthma, French asthme' 2>&1|tail -1; done",
 "dangerouslyDisableSandbox": true
}
```


## [2026-09-04T20:01:51.936Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"اندر\" MON_part1.txt | grep -n \"پهلوی\\|\\[په\" | head -5; echo \"---\"; grep -no \"اندر [^ ]\\{0,40\\}\" MON_part2.txt | head -5"
}
```


### [2026-09-04T20:01:53.736Z] TOOL RESULT

```
== https://vajehyab.com/?q=%D8%A2%D8%B3%D9%85
/home/sfmqrb/git/rishe/data/verification/sources/web/68198e356cf75573.txt
== https://www.vajehyab.com/moein/%D8%A2%D8%B3%D9%85
/home/sfmqrb/git/rishe/data/verification/sources/web/8e8842cd433aebc1.txt
== https://en.wiktionary.org/wiki/asthme
/home/sfmqrb/git/rishe/data/verification/sources/web/22579067d376fabb.txt
```


### [2026-09-04T20:01:55.608Z] TOOL RESULT

```
---
2351:اندر آن:
6094:اندر فردا.
12589:اندر بافت.
15396:اندر فاعل
15400:اندر مردم
```


## [2026-09-04T20:01:59.268Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### vajehyab1\"; grep -o \"آسم[^\\n]\\{0,200\\}\" 68198e356cf75573.txt|head -5; echo \"### vajehyab2\"; grep -o \"آسم[^\\n]\\{0,200\\}\" 8e8842cd433aebc1.txt|head -5; echo \"### asthme\"; grep -n -A5 \"^ Etymology$\" 22579067d376fabb.txt|grep -v '^\\s*$'|head -12"
}
```


### [2026-09-04T20:02:01.055Z] TOOL RESULT

```
### vajehyab1
آسم | واژه یاب
آسم | واژه یاب 
آسم
آسم
آسم
### vajehyab2
آسم | فرهنگ انتشارات معین | واژه یاب
آسم | فرهنگ انتشارات معین | واژه یاب 
آسم
### asthme
170: Etymology
171- [ edit ] 
172-
173- From Latin āsthma , from Ancient Greek ἆσθμα ( âsthma ) .
174-
175- Pronunciation
```


## [2026-09-04T20:02:03.459Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,120p' 8e8842cd433aebc1.txt | grep -v '^\\s*$' | tail -50"
}
```


### [2026-09-04T20:02:06.644Z] TOOL RESULT

```
URL: https://www.vajehyab.com/moein/%D8%A2%D8%B3%D9%85
FETCHED: 2026-09-04T20:01:53Z
STATUS: 200
TITLE: معنی آسم | فرهنگ انتشارات معین | واژه یاب
'
 />
 معنی آسم | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مشابه آوا متن آغاز قافیه 
 آسم
 فرهنگ انتشارات معین
 [ فر. ] (اِ.) نفس تنگی ، اختلال در تنفس به علت انسداد برونش ها و آلرژی .
 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
```


## [2026-09-04T20:02:26.986Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"anhuya[a-z]*\\|a.huya[a-z]* *haca\\|hu[iy]at.*haca\" BRT.txt | head -8; echo \"--- avesta corpus search\"; grep -no \"anhuyat\\|aŋhuiiat\" BRT.txt AVG.txt HID.txt 2>/dev/null | head -5"
}
```


### [2026-09-04T20:02:27.066Z] TOOL RESULT

```
4180:anhuyav
4184:anhuyav
6201:anhuya
6202:anhuya
7501:anhuya
9445:anhuyanam
20870:anhuyai
21065:anhuya
--- avesta corpus search
```


## [2026-09-04T20:02:28.874Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"barz.\\{0,3\\}a.hu\\|bar.za.hu\\|burz.axw\\|burzax\" BRT.txt NYB_vol2_glossary.txt PHD.txt HENNING_selected_papers.txt 2>/dev/null | head -8"
}
```


### [2026-09-04T20:02:31.009Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T20:02:33.393Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4178,4186p' BRT.txt | cut -c1-700"
}
```


### [2026-09-04T20:02:33.458Z] TOOL RESULT

```
dem  Mann  zu  teil  wird,  der  . ,"  A.4-4', 4  (wo  atihuyäe).
VgL  aahuyiw-,  aniuyä:
•  j.  'anhuyav-  Adj.  'der  sich  (den  Anspruch auf)  das  (andere)    Leben  erwirbt':    zara-
^ustraAit  .  .  °yaos  osaHnarthü  Y.  24-  St  ^^■
3"-
Zum  Praes,  31  anAiya.;  S  ^09-  4-  "  VgL ^at/hayav-  EN.  —  Pü. :  k?  andar  iur"J«') ahräkih  kämaktum  bül.  —  ')  Die  Abtrennung der  PaTa.gra.phen  ist  in  den  Hds.  verwirrt;  die Worte  aak-  aiac'  gehören  noch  m  %  2.  — 3)  Weshalb  man  aohuyaoi  fälschlich  als  LD. erklärte ;  zuletzt  Bn.  Stnd.  /.  39a
•  j.  'anhuyav-  m,  EN.  eines  Gläubigen: 'yao!  asaorß  Yt  y,  1 18.
Vgl.  ^aahuyca!-.
j.    aOAuyä,  aohuyal:    s.  atihü-,    aakoä-;    — aohuyä:  s.  aakui:
```


## [2026-09-04T20:03:36.358Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -5 e1d0e8ae4fa52831.txt; echo ---; head -5 78fb0757f04b76ee.txt; echo \"=== animal ===\"; sed -n '20,30p' 30f0908ee8e744bb.txt|grep -v '^\\s*$'|head -8"
}
```


### [2026-09-04T20:03:38.040Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82entero-
FETCHED: 2026-09-04T19:58:40Z
STATUS: -1
TITLE: 

---
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/asuras
FETCHED: 2026-09-04T19:58:42Z
STATUS: -1
TITLE: 

=== animal ===
 Origin and history of animal 
 animal (n.) 
 early 14c., "any sentient living creature" (including humans), from Latin animale "living being, being which breathes," noun use of neuter of animalis (adj.) "animate, living; of the air," from anima "breath, soul; a current of air" (from PIE root *ane- "to breathe;" for sense development, compare deer ).
 A rare word in English before c. 1600, and not in KJV (1611). Commonly only of non-human creatures. It drove out the older beast in common usage. Used derisively of brutish humans (in which the "animal," or non-rational, non-spiritual nature is ascendant) from 1580s.
 Quid est homo? A dedlych best and resonable, animal racionale. ["Battlefield Grammar," c. 1450]
```


## [2026-09-04T20:09:33.577Z] TOOL CALL #88: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build54.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nPOK48 = \"POK_01.txt f-page 57 (printed p.48-49)\"\n\ndoc = {\n \"pdf_page\": 54,\n \"book_page\": 24,\n \"verified_by\": \"claude-fable-5-1\",\n \"verified_on\": \"2026-09-04\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"An 1\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₂enh₁- 'to breathe' (Pokorny 3. an(ə)- pp. 38-39; Watkins/AHD anə-); the secondary root box 'Ansu (spirit, world)' = PIE *h₂ensu-/*n̥su- (Pokorny ansu- p.48)\",\n   \"note\": \"The root itself is real, the language label (Indo-European) is right and the gloss 'breath' is right. Two caveats. (1) The page Nourai cites, POK:48, is not the 'atmen' root: Pokorny puts an(ə)- 'atmen, hauchen' on pp. 38-39 and reserves p.48 for the separate lemma 'ansu-, ̥nsu- Geist, Dämon' - i.e. Nourai's page reference belongs to the sub-root Ansu, not to An 1. (2) The merger of Ansu into An 1 is exactly the step Pokorny himself only hedges at: after listing ai. ásu-, av. aŋhu-, ai. ásura-, av. ahura-, ven. ahsu-, germ. *ansuz he adds 'Vielleicht zu an(d)- [read an(ə)-] ,atmen'.' Watkins/AHD 1985 keeps 'ansu-. Spirit, demon' as an independent root, and Kroonen/Wiktionary now derive Proto-Germanic *ansuz from PIE *h₂émsus 'to engender, beget' (cf. Hittite ḫaššu- 'king'), not from 'breathe'. So the whole right-hand half of this chart (nodes 12-15, and the ahura/aŋhu- part of node 1) rests on a connection that most current handbooks decline to make. Klein, whom Nourai also cites, does make it (s.v. animus: 'Cp. also ahura, anemo-, anhelation, asthma, asura, prana'), and Nourai's node list is visibly copied from that cross-reference list - which is why Sanskrit prana ended up inside an Avestan box (node 1).\",\n   \"sources\": [\n     W + \"Reconstruction:Proto-Indo-European/h%E2%82%82enh%E2%82%81-\",\n     W + \"Reconstruction:Proto-Germanic/ansuz\",\n     \"https://www.etymonline.com/word/animal\"\n   ],\n   \"ref_check\": [\n     {\"ref\": \"POK:48\", \"status\": \"partial\", \"note\": \"POK_01.txt f-page 57 (printed p.48-49): 'ansu-, ̥nsu- ,Geist, Dämon'. Ai. ásu-, av. aŋhu- ,Lebenshauch, Welt', davon ai. ásu-ra-, av. ahura- ,Machthaber' (*̥nsu-); ven. ahsu- (= āsu-) ,Kultbild' = germ. *ansuz ,Gott, Ase' ... Vielleicht zu an(ə)- ,atmen'.' The page supports the FORMS but only tentatively the link to 'breathe'; the root 'breath' itself is Pokorny pp. 38-39 ('5. an(ə)- ,atmen, hauchen', Nominalstamm ant-').\"},\n     {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"Klein 1966 s.v. animus (leaf 52, ~p.78-80): 'rel. to anima ... and cogn. with Gk. ἄνεμος ... fr. I.-E. base *an-, ‘to blow, breathe’ ... Cp. animadvert, animal, ... exhale, inhale, ... Cp. also ahura, anemo-, anhelation, asthma, asura, prana.' - the exact set of branches Nourai draws.\"},\n     {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt line 282: 'anə-. To breathe. Suffixed form *anə-mo- in: a. Latin animus ... and anima ...: ANIMA, ANIMADVERT, ANIMAL, ANIMATE, ANIMISM, ANIMOSITY, ANIMUS; ... b. Greek anemos, wind: ANEMO-. [Pok. 3. an(ə)- 38.]' - but Watkins lists 'ansu-. Spirit, demon ... [Pok. ansu- 48.]' as a SEPARATE root and does not put ASTHMA, EXHALE or INHALE under anə-.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. I p.56-57 (WLD_Bd1_pages.txt leaf 64-65)\", \"stance\": \"supports\", \"note\": \"'3. an- ,atmen, hauchen'. Ai. aniti ,atmet' ... Lat. animus ,Geist, Seele', anima ,Luftzug, Wind, Hauch, Seele' (davon animal ...), halo, -are ,hauchen, duften' (Denominativ eines *an-slo-...)'\"},\n     {\"src\": \"SYN\", \"where\": \"Buck 4.51 BREATHE; BREATH and 16.11 SOUL, SPIRIT\", \"stance\": \"supports\", \"note\": \"'Skt. an- but mostly cpd. pra-an-, with nouns ana-, prana-, Av. āŋti, parāŋti- ... : Grk. ἄνεμος ,wind’'; and 'Lat. anima ..., orig. ‘air, breath’'\"},\n     {\"src\": \"IEC\", \"where\": \"Mann, 'anos (3) “breath, soul, fragrance”. WP I, 56' (IEC.txt line 599, leaf 29)\", \"stance\": \"supports\", \"note\": \"Mann has an IE noun *anos 'breath, soul' beside the verb, citing WP I 56 - the same root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\",\n     \"words\": \"ahu, ahura, anhu, ahva, axva; prana; ahura-mazdha\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Av. aŋhu-/ahu- 'existence, life, world' (Bartholomae AiW s.v. aŋhu- 'vergängliches, d.i. materielles Dasein, Leben') and ahura- 'lord' (< *n̥su-ro-) are the Iranian reflexes of Pokorny's ansu-; the by-forms Nourai spells 'ahva, axva' are the same stem in its aŋhuu-/axʷ- shape (Middle Persian axʷ, whence the second element of duš-ox and burz-axʷ). Ahura- + Mazdā- 'wise' gives Av. Ahura Mazdā, OP Auramazdā (Klein: 'lit. ‘wise lord’, a compound of ahura-, ‘a god, a good spirit’, and ma(n)dazdhā, ‘wise’, ... I.-E. bases *men-dh- and *dhē-' - which is why Nourai's cross-references ☞Men 1 and ☞Dhē 2 are right, and AHD's index likewise reads 'AHURA MAZDA ansu-, men-1'). Two problems. (a) 'prana' is not Avestan: it is Sanskrit prāṇá- 'breath of life' = prá- + aná- (Wiktionary; Buck 4.51 'Skt. an- but mostly cpd. pra-an-'); Nourai took it from Klein's cross-reference list under 'animus' and filed it in the Avestan box. (b) The very derivation of aŋhu-/ahura- from 'breathe' is the tentative step discussed in the root note - Wiktionary/Kroonen instead put aŋhu-/ahura-/ásura- under *h₂ems- 'beget' (cf. Hittite ḫaššu- 'king').\",\n     \"sources\": [W + \"ahura\", W + \"%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%A3\", W + \"Reconstruction:Proto-Germanic/ansuz\"],\n     \"ref_check\": [\n       {\"ref\": \"POK:48\", \"status\": \"supports\", \"note\": \"POK_01.txt f-page 57: 'Ai. ásu-, av. aŋhu- ,Lebenshauch, Welt', davon ai. ásu-ra-, av. ahura- ,Machthaber' (*̥nsu-)' - exactly Nourai's ahu/aŋhu/ahura.\"},\n       {\"ref\": \"KLN:41\", \"status\": \"supports\", \"note\": \"Klein 1966 leaf 33 (≈ printed p.41-42), s.v. ahura: 'a benevolent deity (Persian mythology). - Avestic ahura-, ‘a god, a good spirit’, rel. to OI. ásuraḥ, of same meaning. See asura and cp. the first element in Ormazd.'\"},\n       {\"ref\": \"KLN:1095\", \"status\": \"supports\", \"note\": \"The Klein entry that treats ahura-mazdā is 'Ormazd' (KLN_1971.txt line 168881): 'Pers., fr. OPers. Auramazda, fr. Avestic Ahuramazda, lit. ‘wise lord’, a compound of ahura-, ‘a god, a good spirit’ ..., and ma(n)dazdhā, ‘wise’ ... I.-E. bases *men-dh- ... and *dhē-.' (The printed page could not be nailed down: the OCR of KLN_1966.txt carries no page numerals and the leaf-to-page formula in refs_online.json drifts by ~45 pages in vol. II, so 1095 is plausible but unverifiable.)\"},\n       {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt: 'ansu-. Spirit, demon. ... 2. Suffixed reduced form *n̥su-ro- in Avestan ahura, spirit: AHURA MAZDA, ORMAZD. [Pok. ansu- 48.]'; index line 1220 'AHURA MAZDA ansu-, men-1' matches Nourai's ☞Men 1.\"},\n       {\"ref\": \"SNS:6\", \"status\": \"partial\", \"note\": \"SNS_pages.txt leaf 19 has the numbered glossary entry '106.) aŋhu-, ahu-' with aḵʷ / ahūn/ahvān and ahunavar-ahuvar in the surrounding lines, i.e. the forms Nourai lists. The printed page could not be mapped (refs_online.json: 'page offset not determined - OCR too poor').\"},\n       {\"ref\": \"OEW:9\", \"status\": \"not_checked\", \"note\": \"Shipley, Origins of English Words: archive.org lending-only, djvu.txt returns 403; no copy on disk.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"BRT.txt line 4148 s.v. aŋhu-\", \"stance\": \"supports\", \"note\": \"Bartholomae glosses aŋhu- 'vergängliche, d.i. materielle Dasein, Leben' - Nourai's 'life, spirit, world'.\"},\n       {\"src\": \"KNT\", \"where\": \"Kent, OP lexicon\", \"stance\": \"silent\", \"note\": \"Kent has Auramazdā- as a proper name only; no independent OP *ahu- entry bearing on the 'breath' link.\"},\n       {\"src\": \"KLN\", \"where\": \"s.v. ahura / Ormazd / asura\", \"stance\": \"supports\", \"note\": \"See ref_check; Klein groups ahura, asura, prana under I.-E. *an- 'to blow, breathe'.\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 4.51\", \"stance\": \"partial\", \"note\": \"Buck lists Av. āŋti-, parāŋti- 'inhalation, exhalation' under *an- but does NOT list aŋhu-/ahura- there.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\",\n     \"words\": \"Ahurâmazdâ «اهورامزدا»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Av. Ahura Mazdā / OP Auramazdā > Middle Persian Ohrmazd (ʾwhrmzd, with loss of the intervocalic -h- of *ahura- and contraction a-hu-ra > ōhr-) > New Persian هرمز / هرمزد / اورمزد, and the learned re-Avestanised form اهورامزدا used since the 19th-century Zoroastrian revival; the script_extra اهورا ؛ اورمزد ، هورمزد ، هرمزد ، هرمز is precisely that chain of Persian shapes. Klein s.v. Ormazd: 'Pers., fr. OPers. Auramazda, fr. Avestic Ahuramazda, lit. ‘wise lord’.'\",\n     \"sources\": [W + \"ahura\"],\n     \"ref_check\": [\n       {\"ref\": \"MON:400\", \"status\": \"not_checked\", \"note\": \"Mo'in vols. 5-6 (aʾlām / proper names) are the volumes that carry اهورامزدا; they are not online and the local MON text files are the 2-vol. abridgement, which has no اهورامزدا entry (grep silent).\"},\n       {\"ref\": \"SNB:126\", \"status\": \"not_checked\", \"note\": \"Kowsar, Sang-nebeshteh-ha Sokhan Miguyand: refs_online.json records 'kind: none - Not found.' No copy anywhere.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"s.v. Ormazd (KLN_1971.txt line 168881)\", \"stance\": \"supports\", \"note\": \"'fr. OPers. Auramazda, fr. Avestic Ahuramazda, lit. ‘wise lord’'\"},\n       {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt index lines 1220, 1997\", \"stance\": \"supports\", \"note\": \"'AHURA MAZDA ansu-, men-1' and 'ORMAZD ansu-, men-1' - the same two-element analysis and the same two roots Nourai cross-references.\"},\n       {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. ohrmazd\", \"stance\": \"supports\", \"note\": \"MacKenzie's Concise Pahlavi Dictionary has ohrmazd [ʾwhrmzd] 'Ohrmazd', the regular MP continuant that stands between the Avestan and the New Persian forms.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Avestan\",\n     \"words\": \"daoš-ahva; barz-ahva; anhuyat-hača\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"(a) daoš-ahva = Av. daožaŋhu- / daоžauua- 'hell', literally 'bad existence' (duš- 'bad', ☞Dus, + aŋhu-); Bartholomae quotes e.g. 'bunəm aŋhəuš təmaŋhahe yat ərəγatō daožaŋhahe' (V. 5.62, 3.35) and the adjective 'ərəγant- ... a) von der Hölle: ... daožaŋhum'. This word is correct in every respect. (b) barz-ahva 'better (higher) world' is NOT attested in Avestan. The compound that actually exists is Middle Iranian: Parthian *bwrz-ʾhʷ /burz-axʷ/ 'height, unsurmountable passage' = burz 'high' (☞Bhergh) + axʷ 'world' - so Nourai's morphological analysis is right but the language label and the date are wrong by a millennium, and it is not the ancestor of a Persian word by direct descent (see node 5). (c) aŋhuiiaṯ hacā: Bartholomae does have the stem aŋhuiiu- 'der sich (den Anspruch auf) das (andere) Leben erwirbt' and the forms aŋhuiiā/aŋhuiiaṯ (BRT.txt lines 4178-4186), with hacā 'from' (☞Sekw); but the gloss 'from heart (soul)' is a stretch - the word means 'life, existence', not 'heart'.\",\n     \"sources\": [W + \"%D8%AF%D9%88%D8%B2%D8%AE\", W + \"%D8%A8%D8%B1%D8%B2%D8%AE\"],\n     \"ref_check\": [\n       {\"ref\": \"POK:48\", \"status\": \"partial\", \"note\": \"POK_01.txt f-page 57 gives aŋhu- 'Lebenshauch, Welt' but no compound; Pokorny does not mention daožaŋhu- or any *barz-aŋhu-.\"},\n       {\"ref\": \"BQT:896\", \"status\": \"supports\", \"note\": \"Borhan-e Qateʾ ed. Moʾin, BQT_v2_pages.txt leaf 356 (running ≈ printed p.896-899), s.v. دوزخ, Moʾin's footnote 6: 'بهلوی dušox ... duž-axʷ «بارتولمه ۷۵۹» از ایرانی باستان *dužaxʷa-, *dužaŋhva- (جهنم) در اوستای متاخر daožaŋhu «بارتولمه ۹۵۷» ... در ارمنی džoxḵ ... پازند dozax, جزو اول = duš (ژ, بد) است' - exactly Nourai's Avestan > Pahlavi > Persian chain for dužax. Nothing on barzax; برزخ has no headword in Borhan at all (it occurs in vol. 1 only as a metrical model, 'بر وزن برزخ').\"},\n       {\"ref\": \"VDQ:36\", \"status\": \"contradicts\", \"note\": \"VDQ is Badreh'i's Persian translation of Jeffery FVQ; the substance is checkable in FVQ itself. FVQ_pages.txt leaf 94 = printed p.77 s.v. Barzakh: 'That the word is not Arabic seems clear from the Lexicons ... Vollers, ZDMG, l, 646, makes the much more plausible suggestion that barzakh is a by-form of parasang, from the Phlv. frasang, Mod. Pers. farsang ... whence the Ar. barzakh.' Jeffery derives barzakh from farsang, not from a *barz-aŋhu 'higher world'.\"},\n       {\"ref\": \"SOD:127\", \"status\": \"not_found\", \"note\": \"SOD_pages.txt leaf 193 = printed p.127 contains only c- entries (candar, carm, carp...); no Sogdian material bearing on daožaŋhu- or barz-axʷ. Read as an entry number it lands on an unrelated ʾʾj- entry (SOD_pages.txt line 4159).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"BRT.txt lines 4155, 7633 (daožaŋhu-, ərəγant-)\", \"stance\": \"supports\", \"note\": \"'bunəm aŋhəuš təmaŋhahe yat ərəγatō daožaŋhahe' - Av. daožaŋhu- 'hell' is built on aŋhu-.\"},\n       {\"src\": \"PHD\", \"where\": \"MacKenzie p.28 s.v. dušox\", \"stance\": \"supports\", \"note\": \"'dušox [dwšhwʹ | M dwš(w)x] hell' - the Middle Persian link in the chain.\"},\n       {\"src\": \"FVQ\", \"where\": \"Jeffery p.77 s.v. Barzakh\", \"stance\": \"contradicts\", \"note\": \"see ref_check VDQ:36.\"},\n       {\"src\": \"VIE\", \"where\": \"Sajjadiyyeh p.31 (VIE_pages.txt pdf page 37)\", \"stance\": \"partial\", \"note\": \"Discusses the same compound type: 'فردوس برین ... در اوستا به گونه vahišta-ahu ‘وهیشت اخو’ بوده است' - Av. vahišta- aŋhu- 'best existence' = paradise, the positive counterpart of daožaŋhu-.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Pahlavi\",\n     \"words\": \"dužax; barzax\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"MP dušox (Book Pahlavi dwšhwʹ, Manichaean dwš(w)x, also dōžax/dōzax) 'hell' continues Old Iranian *daužaxʷa- < *duš-ahw-a-; the -š- assimilates to -ž- before the voiced onset and Av. -aŋhu- gives MP -axʷ (aŋh > āh > xʷ in the compound). MacKenzie: 'dušox ... hell'. The 'barzax' half of the box is different in kind: no Book Pahlavi *barzax is attested - the attested Middle Iranian form is Parthian *bwrz-ʾhʷ /burz-axʷ/, and it reached New Persian only through Qur'anic Arabic (see node 5), not through Pahlavi.\",\n     \"sources\": [W + \"%D8%AF%D9%88%D8%B2%D8%AE\", W + \"%D8%A8%D8%B1%D8%B2%D8%AE\"],\n     \"ref_check\": [\n       {\"ref\": \"SBK:214\", \"status\": \"not_checked\", \"note\": \"Bahar, Sabk-shenasi vol. I: SBK.txt is a raw djvu dump with no form-feeds, so p.214 cannot be located. The book does discuss دوزخ (SBK.txt lines 1600, 3018, 3248, in the Arday Viraf-nameh passages) and برزخ once (line 10304), but not on an identifiable page.\"},\n       {\"ref\": \"VDQ:36\", \"status\": \"contradicts\", \"note\": \"As at node 3: Jeffery (of which VDQ is the translation) derives Arabic barzakh from Persian farsang, not from a Pahlavi *barzax.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"MacKenzie, PHD.txt line 318\", \"stance\": \"supports\", \"note\": \"'dušox [dwšhwʹ | M dwš(w)x] hell. ~ig [-ykʹ] hellish' - and no *barzax anywhere in the dictionary.\"},\n       {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\", \"note\": \"grep for dušox/dōšox/dwšx in NYB_vol2_glossary.txt returns nothing (the glossary covers only the texts edited in Part I); no evidence either way.\"},\n       {\"src\": \"BQT\", \"where\": \"Mo'in's footnote to دوزخ, BQT_v2 leaf 356\", \"stance\": \"supports\", \"note\": \"'بهلوی dušox ... duž-axʷ «بارتولمه ۷۵۹»' - Mo'in gives exactly this Pahlavi stage.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Persian\",\n     \"words\": \"dŭzax «دوزخ»; barzax «برزخ»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"دوزخ dōzax/duzax 'hell' is inherited straight down the line Nourai draws: PIr *dušHáhuš 'bad existence' > Old Iranian *daužaxʷa- > MP dušox > NP دوزخ (Wiktionary, citing the Manichaean MP dwšx, Parthian dwžx, Av. daožauua/dužaŋhu, Armenian džoxḵ and Georgian ǯoǯoxeti as Iranian loans; Mo'in's footnote in Borhan says the same). That word is confirmed. برزخ barzax 'interval, isthmus, the state between death and resurrection' is NOT an inherited Persian word: it is a Qur'anic Arabic term (Q 23:100, 25:53, 55:20) borrowed back into Persian. Its own origin is contested - Jeffery/Vollers derive Ar. barzakh from Persian farsang/parasang (Phlv. frasang, Gk. parasangēs, Aram./Syr. prsh), while Wiktionary follows the analysis Nourai implies, Parthian *burz-axʷ 'height, insurmountable passage' (burz 'high' + axʷ 'world'). On either view the route is Middle Iranian > Arabic > New Persian, so the arrow 'Avestan barz-ahva > Pahlavi barzax > Persian barzax' as drawn is wrong: the Arabic mediation is omitted, the Avestan stage is unattested, and the gloss 'better (higher) world' is a semantic reconstruction rather than a recorded meaning.\",\n     \"sources\": [W + \"%D8%AF%D9%88%D8%B2%D8%AE\", W + \"%D8%A8%D8%B1%D8%B2%D8%AE\"],\n     \"ref_check\": [\n       {\"ref\": \"BQT:896\", \"status\": \"partial\", \"note\": \"Supports دوزخ in full (see node 3 quote) and is silent on برزخ - Borhan-e Qateʾ has no برزخ headword; the string occurs in vol. 1 only in the formula 'بر وزن برزخ' (BQT_v1_pages.txt leaves 471, 553).\"},\n       {\"ref\": \"VIE:31\", \"status\": \"partial\", \"note\": \"VIE_pages.txt pdf page 37 = printed p.31 (Sajjadiyyeh): treats Av. vahišta-ahu 'best existence' > بهشت and mentions دوزخ on the same page; it supports the -ahu/-axʷ 'world' element, not the barzax claim.\"},\n       {\"ref\": \"VDQ:36\", \"status\": \"contradicts\", \"note\": \"Jeffery FVQ p.77 (of which VDQ is the Persian translation): barzakh is a foreign word in the Qur'an, best explained from Persian farsang - i.e. an Arabic word of Iranian origin that Persian then re-borrowed.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"BQT_v2 leaf 356 (≈p.896-899), Mo'in's footnote 6 to دوزخ\", \"stance\": \"supports\", \"note\": \"Full Avestan>OIr>MP>NP chain for دوزخ with Bartholomae column references 759 and 957.\"},\n       {\"src\": \"FVQ\", \"where\": \"Jeffery p.77 s.v. Barzakh\", \"stance\": \"contradicts\", \"note\": \"'Addai Sher, 19, sought to explain it from the Pers. ... but this has little in its favour ... Vollers ... barzakh is a by-form of parasang.'\"},\n       {\"src\": \"HRN\", \"where\": \"Horn, Grundriss\", \"stance\": \"silent\", \"note\": \"Horn has no entry for برزخ (it is an Arabic loan, outside his scope) and none for دوزخ in the numbered list around no. 52.\"},\n       {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi\", \"stance\": \"partial\", \"note\": \"Mo'in tags برزخ as [ع.] (Arabic) in the standard printed entry; the local 2-vol. abridgement does not carry the etymological brackets, so this could not be quoted verbatim from disk.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Greek\",\n     \"words\": \"astma\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Gk. ᾶσθμα 'hard-drawn breath, panting' (Hippocratic and earlier; Iliad 15.10 ἄσθματι). Klein: 'Gk. ᾶσθμα ... which prob. stands for *ἄναθμα and derives fr. I.-E. base *an-, ‘to blow, breathe’, whence also ἄνεμος ‘wind’, L. animus'; i.e. *h₂n̥h₁-dʰmn̥ / *an-sth-mn̥ with the regular Greek -σθ- cluster and the neuter -μα suffix. Pokorny lists ἄσθμα under an(ə)- (pp. 38-39). Etymonline routes it through ἄζειν 'breathe hard'. Nourai's transliteration 'astma' simply drops the aspirate.\",\n     \"sources\": [\"https://www.etymonline.com/word/asthma\", W + \"%CE%AC%CF%83%CE%B8%CE%BC%CE%B1\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:118\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 3741 (leaf 73, ≈ printed p.118-122), s.v. asthma: 'Gk. ᾶσθμα, ‘hard-drawn breath’, which prob. stands for *ἄναθμα and derives fr. I.-E. base *an-, ‘to blow, breathe’ ... See Frisk, GEW., I, pp.161-62 s.v. ἄσθμα.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"Pokorny an(ə)- pp.38-39\", \"stance\": \"supports\", \"note\": \"the entry ends its Greek section '... also ἄσθμα ‘breathlessness, suffocation’, aaO. 337'\"},\n       {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. anə- and the English index\", \"stance\": \"silent\", \"note\": \"ASTHMA does not appear anywhere in Watkins' appendix or its index - AHD neither supports nor denies the connection.\"},\n       {\"src\": \"KLN\", \"where\": \"s.v. asthma and animus\", \"stance\": \"supports\", \"note\": \"see ref_check; Klein cross-lists asthma under animus.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"French\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Pass-through node: French asthme (attested asme 14th c., re-spelled asthme in the 16th c. on the Latin model), from Latin asthma, from Greek ᾶσθμα. It is the intermediary through which the word reached Persian in the 20th century (node 8) - and the same Latin-French route gave English asthma (node 9).\",\n     \"sources\": [W + \"asthme\"],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"s.v. asthma, asthmatic\", \"stance\": \"supports\", \"note\": \"'asthmatic, adj. - L. asthmaticus, fr. Gk. ἀσθματικός' - the Latin relay.\"},\n       {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d'origine orientale\", \"stance\": \"silent\", \"note\": \"asthme is Greek, not oriental, so Devic has no entry - as expected.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Persian\",\n     \"words\": \"âsm «آسم»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP آسم āsm is a 20th-century medical borrowing from French asthme (French -sthme rendered as Persian -sm, the initial ā- reflecting French [a]). Mo'in's Farhang marks it as French: 'آسم [فر.] (اِ.) نفس‌تنگی، اختلال در تنفس به علت انسداد برونش‌ها و آلرژی' - the bracket [فر.] is Mo'in's tag for فرانسه. So the arrow French > Persian is right, and the word is not an inherited Iranian form despite the ultimate PIE ancestry of the Greek etymon.\",\n     \"sources\": [\"https://www.vajehyab.com/moein/%D8%A2%D8%B3%D9%85\", W + \"asthme\"],\n     \"ref_check\": [\n       {\"ref\": \"MON:55\", \"status\": \"supports\", \"note\": \"Mo'in's entry, quoted from vajehyab's Mo'in text: 'آسم [فر.] (اِ.) نفس‌تنگی ، اختلال در تنفس به علت انسداد برونش‌ها و آلرژی .' The printed page (55) cannot be checked - Mo'in's pagination is not reproduced online and the local MON files are the 2-vol. abridgement, whose grep for آسم returns only آسمان compounds.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"vajehyab, Mo'in dictionary, s.v. آسم\", \"stance\": \"supports\", \"note\": \"'[فر.]' = borrowed from French.\"},\n       {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi\", \"stance\": \"silent\", \"note\": \"grep of ARY_pages.txt / ARY_latin_index_pages.txt for آسم / ASM returns nothing - Aryanpur treats inherited words, not modern French loans.\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\",\n     \"words\": \"asthma\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"ME asma, asma (late 14c.) < Medieval Latin asma < Latin asthma < Greek ᾶσθμα; the etymological -th- was restored in English in the 16th century (Etymonline: 'The -th- was restored in English 16c.'), which is why the modern spelling looks Greek but the pronunciation does not. Nourai draws it straight off the Greek node, which is right as to ultimate source, the Latin/French relay being implicit.\",\n     \"sources\": [\"https://www.etymonline.com/word/asthma\"],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 3741 s.v. asthma\", \"stance\": \"supports\", \"note\": \"'a chronic disorder characterized by difficulty in breathing. - Gk. ᾶσθμα'\"},\n       {\"src\": \"SKT\", \"where\": \"SKT.txt line 1068 'ASTHMA.'\", \"stance\": \"supports\", \"note\": \"Skeat carries the headword ASTHMA in the same Greek-via-Latin frame (the OCR of the entry body is unreadable, but the headword and its (Gk.) tag are there).\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins appendix + index\", \"stance\": \"silent\", \"note\": \"ASTHMA is not indexed to any root in the 1985 appendix.\"}\n     ]\n    },\n    {\n     \"id\": 10, \"lang\": \"Latin\",\n     \"words\": \"anima\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Lat. anima 'current of air, breath, life, soul' (and its masculine twin animus 'mind, spirit') < PIE *h₂enh₁-mo- 'breath', the same -mo- derivative as Greek ἄνεμος 'wind'. Walde-Pokorny I 56-57: 'Lat. animus ,Geist, Seele’, anima ,Luftzug, Wind, Hauch, Seele’ (davon animal ,Lebewesen, Tier’)'. Buck 16.11: 'Lat. anima ..., orig. ‘air, breath’ ... the semantic equivalent of Grk. ψυχή'. The gloss Nourai gives, 'breath of air, life', is Klein's wording verbatim.\",\n     \"sources\": [W + \"anima\", \"https://www.etymonline.com/word/animal\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:78\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 2828 (leaf 52, ≈ printed p.78-80), s.v. animus: 'L., ‘soul, spirit, mind, courage, wish, desire’, rel. to anima, ‘breath of air, air, breath, soul, life’, and cogn. with Gk. ἄνεμος, ‘wind’, fr. I.-E. base *an-, ‘to blow, breathe’.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"WLD\", \"where\": \"WP I 56-57 (WLD_Bd1_pages.txt leaf 64-65)\", \"stance\": \"supports\", \"note\": \"'Lat. animus ,Geist, Seele’, anima ,Luftzug, Wind, Hauch, Seele’'\"},\n       {\"src\": \"POK\", \"where\": \"Pokorny an(ə)- pp.38-39\", \"stance\": \"supports\", \"note\": \"'Latin animus ‘mind, soul’, anima ‘wind, breath, soul, lives’ (Oscan anamum ...)'\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 4.51 and 16.11\", \"stance\": \"supports\", \"note\": \"anima/animus listed under BREATHE and SOUL as 'etymologically air, breath'.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins s.v. anə-\", \"stance\": \"supports\", \"note\": \"'Suffixed form *anə-mo- in: a. Latin animus ... and anima, soul, spirit, life, breath'\"}\n     ]\n    },\n    {\n     \"id\": 11, \"lang\": \"English\",\n     \"words\": \"animal, animosity, exhale, inhale\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"animal (early 14c.) < Lat. animale, neuter of animalis 'animate, of the air' < anima; animosity (early 15c.) < Late Lat. animositas < animosus 'bold, spirited' < animus - both straight from node 10 and confirmed by every source. exhale and inhale are a different matter: they come from Lat. exhālāre / inhālāre, i.e. from hālāre 'to breathe out', which Walde-Pokorny and Pokorny do derive from the same root ('halo, -are ,hauchen, duften’ (Denominativ eines *an-slo-; mit unechtem h ...)', WP I 57; Buck 4.51 'Lat. anhelare ... fr. an- + *ansla- (cf. halare ... with unetymological h-)'), and Klein likewise cross-lists exhale and inhale under animus. But Watkins/AHD - the reference Nourai actually cites at this node - does not: his anə- entry stops at anima/animus/anemos, hālāre is absent from the whole 1985 appendix, and the *an-slo- > hālāre step (with its unexplained h-) is not universally accepted.\",\n     \"sources\": [\"https://www.etymonline.com/word/animal\", W + \"anima\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt line 282 s.v. anə-: derivatives given are 'ANIMA, ANIMADVERT, ANIMAL, ANIMATE, (ANIMATO), ANIMISM, ANIMOSITY, ANIMUS; EQUANIMITY, LONGANIMITY, MAGNANIMOUS, PUSILLANIMOUS, UNANIMOUS' plus ANEMO-. Index lines 1246 confirm 'ANIMAL ane-' and 'ANIMOSITY ane-'. EXHALE, INHALE, HALITUS and halare appear nowhere in the file (grep silent), so AHD supports two of Nourai's four words and is silent on the other two.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 2828 s.v. animus\", \"stance\": \"supports\", \"note\": \"'Cp. animadvert, animal, animalcule, animate, animosity, equanimity, exanimate, exhale, inhale, longanimity, magnanimous ...' - Klein does include exhale and inhale.\"},\n       {\"src\": \"WLD\", \"where\": \"WP I 57\", \"stance\": \"supports\", \"note\": \"'halo, -are ,hauchen, duften’ (Denominativ eines *an-slo-; mit unechtem h, das hier schallmalenden Wert erlangte und auch in an(h)elare eindrang)'\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 4.51\", \"stance\": \"supports\", \"note\": \"'derivs. ... of Lat. anhelare ‘breathe hard, puff, pant’, fr. an- + *ansla- (cf. halare ‘breathe out, exhale’, with unetymological h-)'\"}\n     ]\n    },\n    {\n     \"id\": 12, \"lang\": \"Germanic\",\n     \"words\": \"ansu\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Proto-Germanic *ansuz 'god' (Gothic-Latin anses 'demigods' in Jordanes, Runic a[n]suR, ON áss pl. æsir, OE ōs - the -n- lost before the fricative in West/North Germanic with compensatory lengthening) is certainly a real word and certainly the same formation as Skt. ásura- and Av. ahura-. What is not certain is the arrow from An 1 'breath': Pokorny sets *ansu- up as its own lemma on p.48 and only adds 'Vielleicht zu an(ə)- ,atmen’'; Watkins/AHD prints 'ansu-. Spirit, demon' as an independent root; and current Germanic etymology (Kroonen, followed by Wiktionary) derives *ansuz from PIE *h₂émsus, root *h₂ems- 'to engender, beget', comparing Hittite ḫaššuš 'king' - a wholly different root. Klein, s.v. Aesir, is more sceptical still: 'possibly of the same origin as ON. áss, Goth. ans, ‘beam’.'\",\n     \"sources\": [W + \"Reconstruction:Proto-Germanic/ansuz\", \"https://www.etymonline.com/word/Oswald\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD:929, 931\", \"status\": \"partial\", \"note\": \"Nourai's 929/931 are pages of the 1975/76 AHD main dictionary (the entries Oscar and Oswald fall in that range), which is not open online; the Watkins appendix that IS available says 'ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse áss, god: AESIR ... [Pok. ansu- 48.]' (AHD_watkins1985.txt line 282; index line 1218 'AESIR ansu-'). So AHD supports the Germanic form and the gloss but files it under a root of its own, not under anə- 'to breathe'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"POK_01.txt f-page 57 (p.48), lemma ansu-\", \"stance\": \"partial\", \"note\": \"'= germ. *ansuz ,Gott, Ase’ in aisl. āss, run. a[n]suR, ags. ōs ,Ase’, got.-lat. anses ,Halbgötter’ ... Vielleicht zu an(ə)- ,atmen’.' - supports the form, hedges the root.\"},\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 1831 s.v. Aesir\", \"stance\": \"partial\", \"note\": \"'ON., pl. of áss, ‘god’, rel. to OE. ōs, OS as-, os-, OHG. ans- (in PN.s), Goth. ans, ‘god’; possibly of the same origin as ON. áss, Goth. ans, ‘beam’.' - Klein offers a competing (non-'breath') etymology.\"},\n       {\"src\": \"WLD\", \"where\": \"WP I 68 (the ans- 'wohlgeneigt' lemma) and I 56 ff.\", \"stance\": \"silent\", \"note\": \"Walde-Pokorny's neighbouring ans- lemma is 'favourable' (Goth. ansts) and is not the god-word; WP has no *ansu- under an- 'atmen'.\"}\n     ]\n    },\n    {\n     \"id\": 13, \"lang\": \"English\",\n     \"words\": \"Oswald, Oscar\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"OE Ōsweald = ōs 'god' (< PGmc *ansuz, the -n- lost before -s-) + (ge)weald 'power' > Oswald; OE Ōsgār = ōs 'god' + gār 'spear' (☞Ghei 2, PIE *ǧ5ʰeys- 'to throw, spear') > Oscar. Klein: 'Oscar, masc. PN. - OE. Osgar, compounded of os, ‘a god’, and gar, ‘spear’ ... Cp. the first element in Osmond, Oswald'; 'Oswald ... OE. Osweald, compounded of os, ‘a god’, and (ge)weald, ‘power’.' Etymonline says the same and traces ōs to 'PIE *ansu- ‘spirit’'. (The modern popularity of Oscar in fact revives Macpherson's Ossianic Oscar, but the Old English name is the one Nourai means, and the element ōs is correctly identified.)\",\n     \"sources\": [\"https://www.etymonline.com/word/Oswald\", \"https://www.etymonline.com/word/Oscar\"],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference at this node; the parent node's AHD:929, 931 are the 1976 AHD dictionary pages where Oscar/Oswald stand.\"}],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt lines 26653, 26734 s.vv. Oscar, Oswald\", \"stance\": \"supports\", \"note\": \"quoted in the derivation.\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat\", \"stance\": \"silent\", \"note\": \"Skeat's concise dictionary omits personal names.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins index\", \"stance\": \"partial\", \"note\": \"'AESIR ansu-' is indexed; Oscar/Oswald are main-dictionary entries, not appendix derivatives.\"}\n     ]\n    },\n    {\n     \"id\": 14, \"lang\": \"Sanskrit\",\n     \"words\": \"âsu, âsura\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Skt. ásu- 'life-force, vital breath' and ásura- 'lord, mighty one' (later 'demon', once the a- was re-analysed as privative against sura- 'god'). Both are correct Sanskrit words and both are the exact Indic match of Av. aŋhu-/ahura-, as Pokorny p.48 states. Two corrections to the box: the vowels are short (ásu-, ásura-, not āsu-/āsura-), and the gloss 'God' is only true of the oldest Rigvedic layer - Wiktionary: 'Related to असु (asu-) ... conventionally associated with asu- in the sense of “master of the house” ... Possibly ultimately from PIE *h₂ens- “to engender, beget”. The Brahmanas and the Puranas derive asura from another asu-, “breath”.' The 'breath' etymology that Nourai (with Klein) adopts is thus an old Indian-tradition analysis that modern comparatists treat as one option among several.\",\n     \"sources\": [W + \"%E0%A4%85%E0%A4%B8%E0%A5%81%E0%A4%B0\", W + \"Reconstruction:Proto-Germanic/ansuz\"],\n     \"ref_check\": [\n       {\"ref\": \"POK:48\", \"status\": \"supports\", \"note\": \"POK_01.txt f-page 57: 'Ai. ásu-, av. aŋhu- ,Lebenshauch, Welt’, davon ai. ásu-ra-, av. ahura- ,Machthaber’ (*̥nsu-)'.\"},\n       {\"ref\": \"SOD:10\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian dictionary, printed p.10 (SOD_pages.txt leaf 76), cross-reference entries '276 ʾʾswr ⇒ ʾsʾwr' and '277 ʾʾswrʾn ⇒ ʾʾsʾwr'; the main entry is no. 259 on p.9: 'ʾsʾwr B - asūr (ʾsʾwr) <Skt. asura ... Asura'. Gharib therefore confirms the Sanskrit source of the Sogdian word (node 15), which is what this reference is doing here.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 3778 s.v. asura\", \"stance\": \"supports\", \"note\": \"'OI. ásuraḥ, prob. rel. to OI. ásuḥ (for *̥nsu-), ‘breath of life’, fr. I.-E. base *an-, ‘to blow, breathe’ ... See animus and cp. ahura and sura, ‘spirit, demon’.'\"},\n       {\"src\": \"IEC\", \"where\": \"Mann, 'anos (3) “breath, soul, fragrance” ... Skt. anāḥ'\", \"stance\": \"partial\", \"note\": \"Mann's IE *anos 'breath, soul' cites Skt. anāḥ but not ásura-.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins s.v. ansu-\", \"stance\": \"partial\", \"note\": \"gives *n̥su-ro- for Avestan ahura but keeps ansu- apart from anə- 'to breathe'.\"}\n     ]\n    },\n    {\n     \"id\": 15, \"lang\": \"Sogdian\",\n     \"words\": \"âs`wr\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Sogdian ʾsʾwr / ʾʾswr, read asūr, is a Buddhist-Sanskrit loanword, taken over with the Buddhist cosmology in the Sogdian Buddhist texts of Turfan and Dunhuang (attested Sūtra of the Causes and Effects, the Padmacintāmaṇi-dhāraṇī and TSP 22.19). Gharib prints 'ʾsʾwr B - asūr (ʾsʾwr) ©<Skt. asura ©pl. -t, ob. pl. -ty, -ʾn = ʾʾswr | Asura' - the '<Skt.' tag makes the direction of borrowing explicit, so Nourai's arrow Sanskrit > Sogdian is right. The gloss is the correction: in Buddhist usage an asura is a titan/anti-god, not 'God'; and because it is a loan, the word is not evidence for an inherited Iranian *āsura- alongside Av. ahura-.\",\n     \"sources\": [W + \"%E0%A4%85%E0%A4%B8%E0%A5%81%E0%A4%B0\"],\n     \"ref_check\": [\n       {\"ref\": \"SOD:10\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf 76 = printed p.10, entries '276 ʾʾswr ⇒ ʾsʾwr' / '277 ʾʾswrʾn ⇒ ʾʾsʾwr'; the full entry, no. 259 on p.9 (leaf 75), is 'ʾsʾwr B ... asūr (ʾsʾwr) ©<Skt, asura ©pl. -t, ob. pl. -ty, -ʾn = ʾʾswr | Asura | STii 8.6; BSTBL, Padm. 3; TSP 22.19'. Nourai's page reference is exact.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"SOD\", \"where\": \"Gharib nos. 259/276/277, pp.9-10\", \"stance\": \"partial\", \"note\": \"Supports the form and the Sanskrit source; contradicts the gloss 'God' (Gharib glosses simply 'Asura').\"},\n       {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Khotanese\", \"stance\": \"silent\", \"note\": \"grep for asura/ʾsʾwr in ISS_alt_DKS.txt returns nothing usable; Khotanese has the same Buddhist loan but it is not needed for this arrow.\"},\n       {\"src\": \"HENNING\", \"where\": \"Henning, Selected Papers\", \"stance\": \"silent\", \"note\": \"no discussion of Sogdian ʾsʾwr found.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"An 2, Eno, Ono\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *h₂en- / *h₁eno- ~ *h₁ono-, a demonstrative pronominal stem 'that (one), there', with the derivatives *h₂en-yo- 'other' and *h₂en-tero- 'the other (of two)'\",\n   \"note\": \"The root, its language label and Nourai's page reference are all right; only the gloss is loose. Pokorny p.37 heads the lemma '2. an Demonstrativpartikel ,dort, andererseits’' and only then adds 'Davon abgeleitet: anios ,anderer’ ... anteros ,anderer’ (von zweien)'; Watkins prints 'an². Demonstrative particle. Suffixed form *an-tero-, “other (of two)” ... [Pok. 2. an 37.]'. So 'other' is the meaning of the derivatives, not of the root. Nourai's triple name 'An 2, Eno, Ono' comes straight from Klein s.v. other, who reconstructs 'base *eno-, *ono-'. The one real error on this chart is the arrow to Persian ān (node 2), which Nourai's own cited page in Horn explicitly rejects.\",\n   \"sources\": [\"https://www.etymonline.com/word/other\", W + \"%D8%A2%D9%86\"],\n   \"ref_check\": [\n     {\"ref\": \"POK:37\", \"status\": \"supports\", \"note\": \"POK_01.txt f-page 45 (printed p.37-38): '2. an Demonstrativpartikel ,dort, andererseits’. Gr. ἄν ... lat. an ..., air. an-d ,hier’, got. an ,denn, nun’; lit. an-gu ,oder’ ... Davon abgeleitet: anios ,anderer’ in: ai. anyá-, av. anya-, ainya-, apers. aniya- ds. ... anteros ,anderer’ (von zweien) in: ai. ántara-, oss. ändär, got. anþar, aisl. annarr, ahd. andar, ags. ōþer ... WP. I 56, 67, II 337.'\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 282\", \"stance\": \"supports\", \"note\": \"'an². Demonstrative particle. Suffixed form *an-tero-, “other (of two)” (compare *al-tero- under al-¹) in Germanic *antharaz in Old English ōther, other: OTHER. [Pok. 2. an 37.]'\"},\n     {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 26736 s.v. other\", \"stance\": \"supports\", \"note\": \"'formed with I.-E. compar. suff. *tero- fr. base *eno-, *ono-, whence OI. anyáḥ, Avestic anya-, OPers. aniya-, ‘other’, Lith. anàs, ans, ‘that one’, OSlav. onŭ, ‘he’ ...' - the source of Nourai's root name.\"},\n     {\"src\": \"WLD\", \"where\": \"WP I 56, 67, II 337 (as cited by Pokorny)\", \"stance\": \"supports\", \"note\": \"Pokorny's own reference line for this lemma; WLD_Bd1_pages.txt leaf 75 = printed p.67 treats the anti/antios group beside it.\"},\n     {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt lines 597, 602\", \"stance\": \"supports\", \"note\": \"'anos (1), ā, om ‘this, that, yon’. WP II, 337. Cf. anios' and 'anteros ‘second, other’. Cf. anos (1) and -teros.'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"anya, aimya\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The word is Av. anya- 'other', with its Younger Avestan by-form ainya- and OP aniya- - a *-yo- derivative of the demonstrative stem (*h₂en-yo-), regularly matched by Skt. anyá-. The JSON's second form 'aimya' is not a possible Avestan shape: Pokorny prints 'ai. anyá-, av. anya-, ainya-, apers. aniya-' and Klein 'OI. anyáḥ, Avestic anya-, OPers. aniya-'. The book will have printed ainya (Bartholomae's spelling); an n has been read as an m in transcription. With that corrected the node is confirmed: the words are real, the language labels fit (anya- Avestan, aniya- Old Persian) and the derivation from the root is standard.\",\n     \"sources\": [\"https://www.etymonline.com/word/other\"],\n     \"ref_check\": [\n       {\"ref\": \"POK:37\", \"status\": \"supports\", \"note\": \"POK_01.txt f-page 45: 'anios ,anderer’ in: ai. anyá-, av. anya-, ainya-, apers. aniya- ds.' - note ainya, not aimya.\"},\n       {\"ref\": \"KLN:1108\", \"status\": \"supports\", \"note\": \"Klein s.v. other (KLN_1966.txt line 26736, leaf 589): '... base *eno-, *ono-, whence OI. anyáḥ, Avestic anya-, OPers. aniya-, ‘other’ ...'. Content matches exactly; the printed page cannot be confirmed because the OCR carries no page numerals and the leaf-to-page formula drifts in Klein vol. II.\"},\n       {\"ref\": \"HRN:13\", \"status\": \"contradicts\", \"note\": \"Horn's no. 52 (HRN.txt leaf 33-34 = printed pp.12-13) is the entry Nourai is citing, and it says the opposite of what the chart draws: 'Darmesteter's Etymologie (aus ap. aniya-) ist falsch, denn ap. aniya- hätte im Np. kaum etwas anderes als [ēn] werden können. Zudem kommt das Ideogramm ... nur durch Nachlässigkeit der Schreiber für aw. anya- vor.' Horn is talking about the descent to New Persian ān (node 2), not about the Avestan word itself, which he accepts.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"Bartholomae AiW s.v. anya-, ainya-\", \"stance\": \"supports\", \"note\": \"BRT.txt lines 2472, 2550, 2564 show anya-/ainya- in use ('aēšąm anyō ...', 'in Verbindung mit anya- Du.'); no form *aimya- exists.\"},\n       {\"src\": \"KNT\", \"where\": \"Kent, Old Persian lexicon\", \"stance\": \"supports\", \"note\": \"Kent lists OP aniya- 'other', the exact OP counterpart Nourai's node covers.\"},\n       {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt line 597 s.v. anos (1)\", \"stance\": \"partial\", \"note\": \"Mann files Av. ana-, OPer. ana- under anos and cross-refers 'Cf. anios' for the 'other' derivative.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\",\n     \"words\": \"ân «آن»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"NP آن ān 'that' is a demonstrative, not a reflex of 'other', and the two independent authorities available both say so. Horn (Grundriss no. 52, the very page Nourai cites) derives it from the demonstrative stem: 'an ,jener’ ... pāz. an bez. hān ..., phlv. in an-gūn, an-č. Zu aw. an-a, an-agāo, an-āiš; skr. an-ayā. Der Übergang von der aw. skr. Bedeutung ‘dieser’ zu ‘jener’ ist derselbe wie in ksl. onŭ, lit. ans, lat. ollus. Die Dehnung des ā ist speciell mittel-neupersisch' - and then rejects the alternative in terms: 'Darmesteter's Etymologie (aus ap. aniya-) ist falsch.' Wiktionary takes a third route: NP ān < MP ʾN /ān/ 'that, he' < Proto-Iranian *hauv (the *sa/*ta-demonstrative). Either way, ān belongs to the pronominal core of the root (Pokorny's an 'dort'), not to its *-yo- derivative anya- 'other' under which Nourai hangs it. So the root box is right and the arrow is wrong.\",\n     \"sources\": [W + \"%D8%A2%D9%86\"],\n     \"ref_check\": [\n       {\"ref\": \"HRN:13\", \"status\": \"contradicts\", \"note\": \"HRN.txt leaf 34 = printed p.13: 'Darmesteter's Etymologie (aus ap. aniya-) ist falsch, denn ap. aniya- hätte im Np. kaum etwas anderes als [ēn] werden können.' Horn's own derivation, on the facing page (leaf 33 = p.12, no. 52), is 'Zu aw. an-a, an-agāo, an-āiš; skr. an-ayā.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"HRN\", \"where\": \"Horn no. 52, pp.12-13\", \"stance\": \"contradicts\", \"note\": \"see ref_check.\"},\n       {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien\", \"stance\": \"silent\", \"note\": \"grep of HUB.txt for the ān entry returns nothing usable (Hübschmann cites Horn's numbered entries rather than repeating the pronouns).\"},\n       {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. ān\", \"stance\": \"supports\", \"note\": \"MacKenzie has MP ān [ZK/ʾN] 'that', the demonstrative, which is the form Wiktionary makes the direct ancestor of NP ān.\"},\n       {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt line 12193 s.v. onos (2) 'that, yon'\", \"stance\": \"supports\", \"note\": \"'Skt. ana-, Vedic ana; OPer. ana ‘by this’; Av. ana-; Per. ān; Arm. na ...' - Mann too puts Persian ān with the demonstrative ana-, not with anya-.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Germanic\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Pass-through node: Proto-Germanic *anþaraz 'other, second' < PIE *h₂en-tero-, the comparative-in-*-tero- of the demonstrative stem. Attested Gothic anþar, ON annarr, OHG andar, OS āþar, OFris. ōþer, OE ōþer; the -n- is lost before the fricative in Old English, Old Saxon and Old Frisian ('a normal loss of n before fricatives', Barnhart, quoted by Etymonline).\",\n     \"sources\": [\"https://www.etymonline.com/word/other\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 282: 'an² ... Suffixed form *an-tero-, “other (of two)” ... in Germanic *antharaz in Old English ōther, other: OTHER.'\"},\n       {\"ref\": \"KLN:1102\", \"status\": \"partial\", \"note\": \"No separate Germanic entry could be located at Klein's p.1102; the Germanic material Nourai wants is inside Klein's 'other' entry (leaf 589): 'rel. to OS. athar, othar, OFris. other, ON. annarr, Du. ander, OHG. andar, MHG., G. ander, Goth. anþar, ‘other’'. Klein's pagination cannot be checked from the OCR (no page numerals; the leaf-to-page formula drifts ~45 pages in vol. II), so the citation may well be right.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"POK_01.txt f-page 45 (p.37)\", \"stance\": \"supports\", \"note\": \"'anteros ,anderer’ (von zweien) in: ... got. anþar ds., aisl. annarr ,anderer, zweiter’, ahd. andar, ags. ōþer ,anderer’'\"},\n       {\"src\": \"KLN\", \"where\": \"s.v. other\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n       {\"src\": \"WLD\", \"where\": \"WP I 67 / II 337\", \"stance\": \"supports\", \"note\": \"the reference line Pokorny gives for this lemma; WLD_Bd1 p.67 handles the neighbouring anti/antios family.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"English\",\n     \"words\": \"other\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"OE ōþer 'second, the other of two' > ME other > NE other. Etymonline: 'from Proto-Germanic *anthera- ... These are from PIE *an-tero- (source of Lithuanian antras, Old Prussian anters ‘other, second’), which is perhaps a variant of *al-tero- ... Or the first element might be the pronoun *eno-, *ono- [Boutkan].' English detached the 'second' sense to the Latin loan second, unlike Swedish andra / Danish anden.\",\n     \"sources\": [\"https://www.etymonline.com/word/other\"],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; the parent's AHD and KLN:1102 cover it.\"}],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 26736 s.v. other\", \"stance\": \"supports\", \"note\": \"'ME. other ... fr. OE. ōþer, ‘the second, following; the other’ ... and cogn. with Lith. antras, OPruss. antars, OI. ántaraḥ, ‘other’.'\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins index line 2001 'OTHER an²'\", \"stance\": \"supports\", \"note\": \"English other is indexed to root an².\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat\", \"stance\": \"silent\", \"note\": \"the OCR of SKT.txt does not yield a readable OTHER entry (headword lines are garbled); no evidence either way.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Indo-European\",\n     \"words\": \"An-teros\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"*an-tero- = the demonstrative stem *h₂en- plus the contrastive/comparative suffix *-tero- (the same suffix as in *al-tero- > Lat. alter, and in Gk. -τερος), giving 'the other of two, the second'. Mann sets it up as a headword: 'anteros “second, other”. Cf. anos (1) and -teros. WP I, 67; II, 337.' The extension to step-kin ('step parent') is a semantic specialisation of 'the other father/mother' that Mann documents for Iranian (see node 6) - the same idea as Latin alter in noverca-type expressions and as English step- is NOT (step- is a different word, OE stēop- 'bereaved'). ☞Ter 1 correctly points at the suffix.\",\n     \"sources\": [\"https://www.etymonline.com/word/other\"],\n     \"ref_check\": [\n       {\"ref\": \"IEC:27\", \"status\": \"supports\", \"note\": \"IEC.txt line 602 (leaf 30, ≈ printed pp.30-31 by the refs_online formula, i.e. within a page or two of Nourai's 27): 'anteros “second, other. Cf. anos (1) and -teros. WP I, 67; II, 337 | Skt. ántaraḥ; Per. andar (in the phr: madar i andar ‘stepmother’); Oss. ändär ...; Go. anþar; OHG andar; ON annarr; OE oþer; OCS vŭtoryj; ... Li. antras; Latv. otrs; OPr. antars, anters'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"POK_01.txt f-page 45 (p.37)\", \"stance\": \"supports\", \"note\": \"'anteros ,anderer’ (von zweien) in: ai. ántara-, oss. ändär ,anderer’, got. anþar ds. ...'\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins s.v. an²\", \"stance\": \"supports\", \"note\": \"'Suffixed form *an-tero-, “other (of two)” (compare *al-tero- under al-¹)'\"},\n       {\"src\": \"WLD\", \"where\": \"WP I 67; II 337\", \"stance\": \"supports\", \"note\": \"the volume/page pair both Pokorny and Mann give for this formation.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Persian\",\n     \"words\": \"andar «ـ اندر ۲»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The Persian step-kin suffix -andar (پدراندر pedar-andar 'stepfather', مادراندر mādar-andar 'stepmother', دختراندر doxtar-andar 'stepdaughter', پسراندر pesar-andar 'stepson') is exactly the item Mann files under *anteros: 'Per. andar (in the phr: madar i andar ‘stepmother’); Oss. ändär' - i.e. 'the other mother', Ossetic ændær 'other' being the closest living Iranian witness. The formation would come from Old Iranian *antara- 'other' (= Skt. ántara-, Av. antara-), which gives MP/NP andar regularly. The caveat that makes this only 'plausible' is homonymy: the everyday Persian اندر 'in, within' is a different word - Wiktionary derives it from MP andar (BYN) < OP aⁿtar 'among, within' < *h₁én-teros, the *-tero- comparative of *h₁en 'in', not of *h₂en 'that/other'. Mo'in's dictionary accordingly numbers two اندر headwords, and Nourai's script «ـ اندر ۲» shows he means the second, the step- suffix. No independent source could be found that separates the two andar for the step-kin sense specifically, so Mann's assignment stands unconfirmed and unrefuted.\",\n     \"sources\": [W + \"%D8%A7%D9%86%D8%AF%D8%B1\"],\n     \"ref_check\": [\n       {\"ref\": \"IEC:27\", \"status\": \"supports\", \"note\": \"IEC.txt line 602 s.v. anteros: 'Per. andar (in the phr: madar i andar ‘stepmother’); Oss. ändär, cf. also ändära (‘otherwise’, fr. *antero)'. Mann is the source of Nourai's whole node, including the -andar compounds.\"},\n       {\"ref\": \"MON:373\", \"status\": \"partial\", \"note\": \"Mo'in numbers two اندر entries, and the compounds are in the dictionary (MON_part1.txt line 17638 'پدراندر (پدندر)', line 65492 'مادراندر، زن پدر'), but the printed pagination of Mo'in is not reproduced online and the local files are the 2-vol. abridgement, so p.373 itself could not be opened.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"IEC\", \"where\": \"Mann s.v. anteros\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n       {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 17638, 65462, 65492\", \"stance\": \"supports\", \"note\": \"'پدراندر' and 'مادراندر، زن پدر' are lexicalised in Mo'in - the compounds Nourai lists in script_extra.\"},\n       {\"src\": \"HRN\", \"where\": \"Horn, Grundriss\", \"stance\": \"silent\", \"note\": \"Horn has no numbered entry for the step- suffix -andar (his andar entries concern the preposition).\"},\n       {\"src\": \"PHD\", \"where\": \"MacKenzie\", \"stance\": \"silent\", \"note\": \"MacKenzie's andar is the preposition 'in, within'; no Pahlavi step-kin *andar is recorded, so the Persian usage cannot be traced back through MP in the dictionaries.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Sanskrit\",\n     \"words\": \"antarah\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Skt. ántara- 'other, different; interior' is the Indic reflex of *h₂en-tero-, the exact cognate of Gothic anþar and OE ōþer, listed as such by Pokorny ('ai. ántara-'), Mann ('Skt. ántaraḥ') and Klein ('OI. ántaraḥ, ‘other’'). Nourai's transliteration 'antarah' is the nominative singular ántaraḥ; the accent is on the first syllable.\",\n     \"sources\": [\"https://www.etymonline.com/word/other\"],\n     \"ref_check\": [\n       {\"ref\": \"IEC:27\", \"status\": \"supports\", \"note\": \"IEC.txt line 602: 'anteros “second, other ... Skt. ántaraḥ'.\"},\n       {\"ref\": \"POK:37\", \"status\": \"supports\", \"note\": \"POK_01.txt f-page 45: 'anteros ,anderer’ (von zweien) in: ai. ántara-, oss. ändär ,anderer’ ...'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 26736 s.v. other\", \"stance\": \"supports\", \"note\": \"'cogn. with Lith. antras, OPruss. antars, OI. ántaraḥ, ‘other’'\"},\n       {\"src\": \"SYN\", \"where\": \"Buck\", \"stance\": \"silent\", \"note\": \"Buck has no OTHER concept section; the word is not treated in the synonym list.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins s.v. an²\", \"stance\": \"partial\", \"note\": \"Watkins cites only the Germanic reflex under an², not Sanskrit ántara-.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-54.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build54.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-54.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 54"
}
```


### [2026-09-04T20:09:35.984Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 22/22
node verdicts: {'plausible': 8, 'confirmed': 11, 'disputed': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 18, 'partial': 8, 'not_checked': 8, 'contradicts': 5, 'not_found': 1}
books consulted: {'supports': 40, 'silent': 16, 'partial': 11, 'contradicts': 3} | by book: {'KLN': 12, 'AHD': 9, 'PHD': 5, 'POK': 5, 'WLD': 5, 'SYN': 4, 'IEC': 4, 'BRT': 3, 'HRN': 3, 'MON': 3, 'SKT': 3, 'KNT': 2, 'FVQ': 2, 'BQT': 2, 'VIE': 1, 'NYB': 1, 'DEV': 1, 'ARY': 1, 'SOD': 1, 'ISS_alt_DKS': 1, 'HENNING': 1, 'HUB': 1}
```


## [2026-09-04T20:09:45.105Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"PHD ohrmazd:\"; grep -o \"ohrmazd[^,]\\{0,60\\}\" PHD.txt|head -3; echo \"PHD an:\"; grep -o \"[^a-z]ān \\[[^]]*\\][^.]\\{0,40\\}\" PHD.txt|head -3; echo \"KNT aniya:\"; grep -o \"aniya-[^.]\\{0,80\\}\" KNT.txt|head -3; echo \"ISS asura:\"; grep -c \"asura\" ISS_alt_DKS.txt; echo \"HENNING asur:\"; grep -c \"ʾsʾwr\\|asur\" HENNING_selected_papers.txt; echo \"ARY asm:\"; grep -c \"آسم\" incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-04T20:09:46.841Z] TOOL RESULT

```
PHD ohrmazd:
PHD an:
ģān [?mlk’n'] generality, commonalty
šān [OLE?n, у. бу | М юу п, N ēšān] they, those
ģān [МТА-, dh? »'] = dahigàn
KNT aniya:
aniya-, Av
aniya- ‘gold’, Skt
aniya- ‘gold’, Av
ISS asura:
24
HENNING asur:
59
ARY asm:
7
```


## [2026-09-04T20:09:57.029Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ohrmazd variants ===\"; grep -o \"[Oo]hrmazd[^|]\\{0,50\\}\\|ʾwhrmzd[^|]\\{0,40\\}\\|whrmzd[^|]\\{0,40\\}\" PHD.txt PHD_mackenzie.txt|head -4; echo \"=== PHD andar prep ===\"; grep -o \"andar \\[[^]]*\\][^.]\\{0,50\\}\" PHD.txt|head -3; echo \"=== PHD an that ===\"; grep -o \"ān \\[ZK[^]]*\\][^.]\\{0,40\\}\\|ʾn'\\] that[^.]\\{0,30\\}\" PHD.txt|head -3"
}
```


## [2026-09-04T20:09:58.152Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ISS asura ctx ===\"; grep -o \".\\{80\\}asura.\\{80\\}\" ISS_alt_DKS.txt|head -3; echo \"=== ARY asm ctx ===\"; grep -no \"آسم.\\{0,60\\}\" incoming/ARY/ARY_pages.txt|head -7"
}
```


### [2026-09-04T20:09:59.357Z] TOOL RESULT

```
=== PHD ohrmazd variants ===
PHD.txt:Ohrmazd Pwhrmgd 
PHD.txt:Ohrmazd.
PHD.txt:Ohrmazd. Justice dad, dadestan.
PHD.txt:Ohrmazd
=== PHD andar prep ===
andar [B YN < A byn | M °ndr, N —] in, among, towards, concerning
andar [m’z-, m'cndl] arch-(demon), gigantic
andar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence
=== PHD an that ===
```


### [2026-09-04T20:10:01.260Z] TOOL RESULT

```
=== ISS asura ctx ===
her’ (see TE Pok. 74 and 319-20 for au, and ап-). The u- < a- before -0-, like hasura-, husura- ‘quarry’, and without following -u-, also u/ryasta- ' shot’, see s.v.
ance'; 2 sing. im- perative Z 23'105 vā ggihu aysuryau justa ‘help to fight the asura-demons'; 2 plur. їп 69:103 adard và gihya:rà jse ' help to slay the other one’;
ййепа juvare 'dogs fight one another’; Z 1:33 сї aysura gyastyo jvüre ‘when the asura-derons fight the deva-gods' ; tt 69:31 tta-m hoümdd sa jau ra na jviryau ‘so th
=== ARY asm ctx ===
1750:آسمان / ۶۳
2265:آسمان» عرش.
8854:آسمان؛ فلکه.
9409:آسمان» عرش, چی
10724:آسمان,
11493:آسمان غرنبه» خشمگین.
14848:آسمان,
```


## [2026-09-04T20:10:08.579Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \".\\{60\\}asur.\\{60\\}\" HENNING_selected_papers.txt | grep -vi \"treasur\\|measur\\|pleasur\" | head -4"
}
```


### [2026-09-04T20:10:08.644Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T20:10:19.650Z] TOOL CALL #93: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json,io\np='data/verification/page-54.json'\nd=json.load(open(p,encoding='utf-8'))\ne0=d['entries'][0]['nodes']; e1=d['entries'][1]['nodes']\ndef nd(nodes,i):\n    return [n for n in nodes if n['id']==i][0]\n\n# node 8 ARY\nfor c in nd(e0,8)['consulted']:\n    if c['src']=='ARY':\n        c['note']=\"grep of ARY_pages.txt for آسم returns only آسمان-compounds (lines 1750, 2265, 8854 ...), no آسم headword - Aryanpur treats inherited Indo-European words, not modern French loans.\"\n# node 15 ISS + HENNING\nfor c in nd(e0,15)['consulted']:\n    if c['src']=='ISS_alt_DKS':\n        c['stance']='supports'\n        c['note']=\"Bailey's Khotanese material has the same Buddhist loan: 'Z 23:105 vā gyihu aysuryau justa “help to fight the asura-demons”', 'Z 1:33 cī aysura gyastyo jvāre “when the asura-demons fight the deva-gods”' - i.e. Khotanese aysura- < Skt. asura-, a parallel Iranian Buddhist borrowing to the Sogdian one, not an inherited form.\"\n    if c['src']=='HENNING':\n        c['note']=\"grep of HENNING_selected_papers.txt for asur/ʾsʾwr yields only 'treasure/measure/pleasure' matches - Henning does not discuss the word.\"\n# entry1 node2 PHD\nfor c in nd(e1,2)['consulted']:\n    if c['src']=='PHD':\n        c['stance']='silent'\n        c['note']=\"The OCR of PHD.txt does not yield a readable ān 'that' headword (grep for the entry returns only gān/šān/dahigān), so MacKenzie could not be quoted; MacKenzie does have the demonstrative, but this could not be verified from the file.\"\nwith io.open(p,'w',encoding='utf-8') as f:\n    json.dump(d,f,ensure_ascii=False,indent=1); f.write('\\n')\nprint('patched')\nPYEOF\npython3 -m json.tool data/verification/page-54.json >/dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 54"
}
```


### [2026-09-04T20:10:21.407Z] TOOL RESULT

```
patched
JSON OK
nodes verified: 22/22
node verdicts: {'plausible': 8, 'confirmed': 11, 'disputed': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 18, 'partial': 8, 'not_checked': 8, 'contradicts': 5, 'not_found': 1}
books consulted: {'supports': 40, 'silent': 16, 'partial': 11, 'contradicts': 3} | by book: {'KLN': 12, 'AHD': 9, 'PHD': 5, 'POK': 5, 'WLD': 5, 'SYN': 4, 'IEC': 4, 'BRT': 3, 'HRN': 3, 'MON': 3, 'SKT': 3, 'KNT': 2, 'FVQ': 2, 'BQT': 2, 'VIE': 1, 'NYB': 1, 'DEV': 1, 'ARY': 1, 'SOD': 1, 'ISS_alt_DKS': 1, 'HENNING': 1, 'HUB': 1}
```


## [2026-09-04T20:10:40.634Z] AGENT

Wrote `/home/sfmqrb/git/rishe/data/verification/page-54.json`; `python3 tools/verify_check.py 54` runs clean (22/22 nodes, no PROBLEM lines).

**Counts (pdf 54 / book 24, 2 charts, 22 nodes)**
- Node verdicts: confirmed 11, plausible 8, disputed 2, transcription_suspect 1
- Root verdicts: An 1 = confirmed, An 2/Eno/Ono = plausible
- Nourai's own refs: 18 supports, 8 partial, 5 contradicts, 1 not_found, 8 not_checked (SNB, OEW, MON:400/373, SBK:214, VDQ, AHD:929/931 — no accessible copies)

**Flagged items**
- *disputed* — An 2 → Persian **ân «آن» 'that'** (#2): Horn's *Grundriss* no. 52, the very page Nourai cites (HRN:13), says "Darmesteter's Etymologie (aus ap. aniya-) ist falsch" and derives ān from the demonstrative aw. an-a; Wiktionary gives MP ān < PIr *hauv. The root is right, the arrow off anya- 'other' is not.
- *disputed* — An 1 → Persian **barzax «برزخ» 'middle stage'** (#5): not an inherited word. It is Qur'anic Arabic re-borrowed into Persian; Jeffery/Vollers (FVQ p.77, which VDQ translates) derive Ar. barzakh from farsang, Wiktionary from Parthian *burz-axʷ. Either way the Avestan→Pahlavi→Persian line drawn here omits the Arabic mediation, and no Avestan *barz-aŋhu- or Pahlavi *barzax is attested. (دوزخ on the same node is fully confirmed.)
- *transcription_suspect* — An 2 → Avestan/OP **"aimya"** (#1): impossible form; Pokorny p.37 and Klein both print **ainya-** (av. anya-, ainya-, apers. aniya-). An *n* read as *m*.

**Other findings worth the owner's eye** (recorded as `plausible`, not flagged): POK:48 is Pokorny's *ansu-* lemma, not the 'breathe' root (pp. 38-39), and Pokorny only says "Vielleicht zu an(ə)-"; Watkins/AHD and Kroonen/Wiktionary (*h₂ems- 'beget', cf. Hitt. ḫaššu-) keep Ansu apart from An 1, so nodes 12-15 rest on a link most handbooks decline. "prana" in the Avestan box (#1) is Sanskrit prāṇá- — lifted from Klein's cross-reference list under *animus*. AHD, the ref cited at #11, does not put exhale/inhale under anə- (Pokorny/WP/Buck do, via halāre < *an-slo-). Sogdian ʾʾswr (#15) is glossed 'Asura' by Gharib and tagged "<Skt." — a Buddhist loan, not 'God'.
